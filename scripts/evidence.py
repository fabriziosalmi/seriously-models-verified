#!/usr/bin/env python3
"""Evidence ledger: every number published by this repository must resolve to a verbatim quote
on a specific page of a SHA-256-pinned source document.

A claim is accepted only if, mechanically:
  1. its source exists in data/downloaded_sources_manifest.json and the cached file matches the pinned SHA-256;
  2. every quote in `quotes` occurs (whitespace-normalised) in the text of `page` of that source;
  3. the claimed `value` occurs as a standalone number inside `quotes[0]`.

Text is extracted with poppler's pdftotext in two modes (layout and raw); a quote passes if it is found in
either. Pages are 1-based physical PDF pages, not printed page numbers.

Usage:
    python3 scripts/evidence.py                 # verify every claim in data/claims.json
    python3 scripts/evidence.py --page SRC N    # print normalised text of page N of source SRC (authoring aid)
    python3 scripts/evidence.py --find SRC TEXT # list pages of SRC whose normalised text contains TEXT
    python3 scripts/evidence.py --ctx SRC N TEXT [W]  # show W chars of context around TEXT on page N
    python3 scripts/evidence.py --claims FILE   # verify the claims in another JSON file

Claim fields:
    id (unique), source (manifest id), page (1-based PDF page; 1 for html/md/json),
    quotes: [str | {"text": str, "page": int}, ...]  every quote must occur verbatim (whitespace-normalised);
    value: number that must occur in quotes[0];
    token: optional index; token `token` of quotes[0] (split on spaces, % and footnote marks stripped) must equal value;
    scale + quoted_value: for sources reporting fractions (HELM, Artificial Analysis): quoted_value must occur in
        quotes[0] and quoted_value * scale must round to value;
    anchor: {"pattern": regex, "expect": str}: the last regex match before quotes[0] must equal expect
        (binds a value to its row/model label in embedded JSON);
    absent: [str, ...]: text that must NOT occur on the page of quotes[0] (negative evidence);
    model, benchmark, protocol, reported_by, note: descriptive fields (not verified mechanically).
"""

import hashlib
import html
import json
import os
import re
import subprocess
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MANIFEST_PATH = DATA_DIR / "downloaded_sources_manifest.json"
CLAIMS_PATH = DATA_DIR / "claims.json"
CACHE_DIR = Path(os.environ.get("SERIOUSLY_MODELS_CACHE", "/tmp/seriously_models_sources"))

MIN_QUOTE_CHARS = 8


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u2212", "-").replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", text).strip()


@lru_cache(maxsize=None)
def manifest() -> dict:
    """Pinned sources; SERIOUSLY_MODELS_EXTRA_MANIFEST may list staged manifests (os.pathsep-separated)."""
    entries = json.loads(MANIFEST_PATH.read_text())
    for extra in filter(None, os.environ.get("SERIOUSLY_MODELS_EXTRA_MANIFEST", "").split(os.pathsep)):
        if Path(extra).exists():
            entries += json.loads(Path(extra).read_text())
    return {s["id"]: s for s in entries}


def source_path(source_id: str) -> Path:
    return CACHE_DIR / manifest()[source_id]["cache_file"]


@lru_cache(maxsize=None)
def source_sha_ok(source_id: str) -> bool:
    p = source_path(source_id)
    return p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == manifest()[source_id]["sha256"]


def _html_to_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return html.unescape(raw)


@lru_cache(maxsize=None)
def page_texts(source_id: str, page: int) -> tuple:
    """Normalised text variants of one page (PDF) or of the whole document (md/html/txt, page must be 1)."""
    p = source_path(source_id)
    ext = manifest()[source_id]["ext"]
    if ext == "pdf":
        out = []
        for mode in ("-layout", "-raw"):
            txt = subprocess.run(
                ["pdftotext", mode, "-f", str(page), "-l", str(page), str(p), "-"],
                capture_output=True, text=True, errors="ignore", check=True,
            ).stdout
            out.append(normalise(txt))
        return tuple(out)
    if page != 1:
        raise ValueError(f"{source_id} is a single-page {ext} document; use page 1")
    raw = p.read_text(errors="ignore")
    variants = [normalise(raw)]
    if ext == "html":
        variants.append(normalise(_html_to_text(raw)))
        # Chart data embedded as escaped JSON inside Next.js/React payloads
        variants.append(normalise(raw.replace('\\"', '"')))
    if ext == "md":
        variants.append(normalise(raw.replace("|", " ").replace("*", "")))
    return tuple(variants)


MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


@lru_cache(maxsize=None)
def published_month(source_id: str) -> str:
    """Month (YYYY-MM) by which the pinned document was public.

    arXiv: the date in the version stamp on page 1 ("arXiv:2204.02311v5 [cs.CL] 5 Oct 2022"); a v1 without a stamp
    falls back to the identifier month. Wayback captures: the manifest month, capped at the capture month (a
    capture proves the page existed by then). Other sources: the manifest month.
    """
    s = manifest()[source_id]
    if s.get("kind") == "arxiv":
        m = re.search(r"arXiv:\d{4}\.\d{4,5}v\d+\s*\[[^\]]+\]\s*\d{1,2} (\w{3}) (\d{4})", page_texts(source_id, 1)[1])
        if m:
            return f"{m.group(2)}-{MONTHS[m.group(1)]:02d}"
        if s.get("version") == "v1":
            return f"20{s['arxiv_id'][:2]}-{s['arxiv_id'][2:4]}"
        raise AssertionError(f"{source_id}: no arXiv date stamp")
    if s.get("kind") == "wayback":
        cap = f"{s['capture'][:4]}-{s['capture'][4:6]}"
        return min(s["month"], cap)
    return s["month"]


def first_public_month(claim: dict) -> tuple:
    """(month, evidence) by which the claimed number was public.

    If the claim cites a later arXiv version and the pinned v1 contains quotes[0] on some page, the number was
    already in v1 and the v1 date applies ("v1"). Otherwise the date of the cited version applies ("cited").
    """
    sid = claim["source"]
    s = manifest()[sid]
    if s.get("kind") == "arxiv" and s.get("version") != "v1":
        v1 = f"arxiv_{s['arxiv_id']}v1"
        if v1 in manifest() and source_sha_ok(v1):
            # Bibliography markers are renumbered between versions ("MMLU [43]" in v1, "MMLU [49]" in v6);
            # they are ignored, every other character of the quote must match.
            strip = lambda t: re.sub(r"\s*\[\d+(?:,\s*\d+)*\]", "", t)  # noqa: E731
            q = claim["quotes"][0]
            nq = strip(normalise(q["text"] if isinstance(q, dict) else q))
            for p in range(1, page_count(v1) + 1):
                if any(nq in strip(v) for v in page_texts(v1, p)):
                    return published_month(v1), "v1"
    return published_month(sid), "cited"


@lru_cache(maxsize=None)
def page_count(source_id: str) -> int:
    if manifest()[source_id]["ext"] != "pdf":
        return 1
    info = subprocess.run(["pdfinfo", str(source_path(source_id))], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", info).group(1))


def fmt_number_pattern(value) -> re.Pattern:
    """Match the value as printed, allowing a trailing zero difference (68.5 vs 68.50) but not a different number."""
    s = f"{value}"
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    int_part, _, frac = s.partition(".")
    # Accept a printed thousands separator: 12032 matches "12,032"
    groups = []
    while len(int_part) > 3:
        groups.insert(0, int_part[-3:])
        int_part = int_part[:-3]
    esc = ",?".join([re.escape(int_part)] + groups)
    esc += (r"\." + re.escape(frac) + r"0*") if frac else r"(?:\.0+)?"
    # Neither more digits nor a further decimal part may follow (60.0 must not match "60.1")
    return re.compile(r"(?<![\d.])" + esc + r"(?!\d)(?!\.\d)")


def _quote(q, default_page):
    """A quote is either a string (on the claim's page) or {"text": ..., "page": N}."""
    if isinstance(q, dict):
        return q["text"], int(q.get("page", default_page))
    return q, int(default_page)


def cell_token(text: str, index: int) -> str:
    """Token `index` of a whitespace-split table row, stripped of %, footnote marks and thousands separators."""
    tokens = normalise(text).split(" ")
    return re.sub(r"[%*†‡§△◁♢∗]+$", "", tokens[index].strip("`*")).replace(",", "")


def check_claim(c: dict) -> list:
    errors = []
    sid = c.get("source")
    if sid not in manifest():
        return [f"unknown source '{sid}'"]
    if not source_sha_ok(sid):
        return [f"source '{sid}' missing from cache or SHA-256 mismatch"]
    quotes = c.get("quotes") or []
    if not quotes:
        return ["no quotes"]
    for q in quotes:
        text, page = _quote(q, c.get("page", 1))
        nq = normalise(text)
        try:
            variants = page_texts(sid, page)
        except Exception as e:  # noqa: BLE001
            errors.append(f"cannot read page {page}: {e}")
            continue
        if len(nq) < MIN_QUOTE_CHARS:
            errors.append(f"quote too short to be evidence: {text!r}")
        elif not any(nq in v for v in variants):
            errors.append(f"quote not found on page {page}: {text!r}")
    first, first_page = _quote(quotes[0], c.get("page", 1))
    for a in c.get("absent", []):
        if any(normalise(a) in v for v in page_texts(sid, first_page)):
            errors.append(f"text asserted absent is present on page {first_page}: {a!r}")
    anchor = c.get("anchor")
    if anchor:
        nq, ok = normalise(first), False
        for v in page_texts(sid, first_page):
            for m in re.finditer(re.escape(nq), v):
                prev = list(re.finditer(anchor["pattern"], v[:m.start()]))
                if prev and prev[-1].group(0) == anchor["expect"]:
                    ok = True
        if not ok:
            errors.append(f"nearest preceding match of {anchor['pattern']!r} before quotes[0] is not {anchor['expect']!r}")
    if c.get("value") is not None and c.get("scale") is not None:
        qv = c.get("quoted_value")
        if qv is None or not re.search(r"(?<![\d.])" + re.escape(repr(qv)) + r"(?!\d)", normalise(first)):
            errors.append(f"quoted_value {qv!r} does not occur in quotes[0]")
        elif abs(qv * c["scale"] - c["value"]) > 0.05 + 1e-9:
            errors.append(f"value {c['value']} is not quoted_value {qv} x {c['scale']} rounded to one decimal")
    elif c.get("value") is not None:
        if not fmt_number_pattern(c["value"]).search(normalise(first)):
            errors.append(f"value {c['value']} does not occur in quotes[0]")
        if c.get("token") is not None:
            try:
                tok = cell_token(first, int(c["token"]))
                if float(tok) != float(c["value"]):
                    errors.append(f"token {c['token']} of quotes[0] is {tok!r}, not {c['value']}")
            except (IndexError, ValueError) as e:
                errors.append(f"token {c['token']} of quotes[0] is not a number: {e}")
    return errors


def load_claims() -> list:
    return json.loads(CLAIMS_PATH.read_text()) if CLAIMS_PATH.exists() else []


def verify_all(claims=None, verbose=True) -> tuple:
    claims = load_claims() if claims is None else claims
    failures = {}
    ids = set()
    for c in claims:
        cid = c.get("id")
        errs = []
        if not cid:
            errs.append("missing id")
        elif cid in ids:
            errs.append("duplicate id")
        ids.add(cid)
        errs += check_claim(c)
        if errs:
            failures[cid] = errs
    if verbose:
        for cid, errs in failures.items():
            for e in errs:
                print(f"[FAIL] {cid}: {e}")
        print(f"{len(claims) - len(failures)}/{len(claims)} claims verified against pinned primary sources.")
    return len(claims), failures


def main(argv):
    if len(argv) >= 3 and argv[0] == "--page":
        for i, v in enumerate(page_texts(argv[1], int(argv[2]))):
            print(f"--- variant {i} ---\n{v}\n")
        return 0
    if len(argv) >= 4 and argv[0] == "--ctx":
        width = int(argv[4]) if len(argv) > 4 else 200
        needle = normalise(argv[3])
        for i, v in enumerate(page_texts(argv[1], int(argv[2]))):
            for m in re.finditer(re.escape(needle), v):
                print(f"[v{i}] ...{v[max(0, m.start() - width):m.end() + width]}...\n")
        return 0
    if len(argv) >= 3 and argv[0] == "--find":
        needle = normalise(" ".join(argv[2:]))
        for p in range(1, page_count(argv[1]) + 1):
            if any(needle in v for v in page_texts(argv[1], p)):
                print(f"{argv[1]} page {p}")
        return 0
    if len(argv) >= 2 and argv[0] == "--claims":
        _, failures = verify_all(json.loads(Path(argv[1]).read_text()))
        return 1 if failures else 0
    _, failures = verify_all()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
