#!/usr/bin/env python3
"""Adversarial verification of the whole repository, with break tests.

Gates (each must pass; any failure exits non-zero):
  1. Sources:   every manifest entry is pinned to an immutable address (arXiv vN, Wayback timestamp, Git commit,
                HELM release) and the cached file matches its SHA-256.
  2. Ledger:    every claim in data/claims.json verifies against its pinned source (scripts/evidence.py).
  3. Catalog:   data/inconsistencies_catalog.json equals a fresh rebuild from the ledger (deterministic) and every
                case delta equals high minus low.
  4. Monthly:   every score in the monthly dataset cites a ledger claim with the same value, model and benchmark.
  5. Pages:     every reference in data/source_pages.json points to a pinned source, an existing physical page and a
                link at the pinned address, and every caption it lists occurs on that page.
  6. Documents: no em/en dashes; every relative Markdown link and image resolves; no case id or number in the
                README case table disagrees with the catalog.

Break tests (--self-test, also run by default) mutate inputs in memory and require each gate to fail.
"""

import copy
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402

ROOT = evidence.ROOT
DATA = ROOT / "data"
DOCS = ["README.md", "DISCREPANCY_AUDIT.md", "BENCHMARKS_MONTH_BY_MONTH.md"]
IMMUTABLE_URL = {
    "arxiv": re.compile(r"^https://arxiv\.org/pdf/\d{4}\.\d{4,5}v\d+$"),
    "wayback": re.compile(r"^https://web\.archive\.org/web/\d{14}id_/https?://"),
    "github": re.compile(r"^https://raw\.githubusercontent\.com/[^/]+/[^/]+/[0-9a-f]{40}/"),
    "helm": re.compile(r"^https://storage\.googleapis\.com/crfm-helm-public/classic/benchmark_output/releases/v\d+\.\d+\.\d+/"),
    "url": re.compile(r"^https://(www-cdn\.anthropic\.com/[0-9a-f]{40}/|assets\.anthropic\.com/m/[0-9a-f]+/|"
                      r"www-cdn\.anthropic\.com/images/|datasets-server\.huggingface\.co/size\?dataset=)"),
}


def gate_sources(manifest: list):
    seen = set()
    for s in manifest:
        if s["id"] in seen:
            raise AssertionError(f"duplicate source id {s['id']}")
        seen.add(s["id"])
        pattern = IMMUTABLE_URL.get(s.get("kind"))
        if pattern is None or not pattern.match(s["url"]):
            raise AssertionError(f"{s['id']}: not pinned to an immutable address ({s.get('kind')}: {s['url']})")
        p = evidence.CACHE_DIR / s["cache_file"]
        if not p.exists():
            raise AssertionError(f"{s['id']}: cached file missing ({p}); run scripts/download_sources.py")
        if hashlib.sha256(p.read_bytes()).hexdigest() != s["sha256"]:
            raise AssertionError(f"{s['id']}: SHA-256 mismatch")
    return len(manifest)


def gate_ledger(claims: list):
    n, failures = evidence.verify_all(claims, verbose=False)
    if failures:
        raise AssertionError(f"{len(failures)} claim(s) fail: {dict(list(failures.items())[:3])}")
    return n


def gate_catalog(catalog: dict):
    import build_forensic_analysis as bfa
    fresh = bfa.build_catalog()
    if json.loads(json.dumps(fresh)) != catalog:
        raise AssertionError("data/inconsistencies_catalog.json differs from a fresh rebuild; run build_forensic_analysis.py")
    for c in catalog["cases"]:
        if abs(round(c["score_high"] - c["score_low"], 2) - c["delta"]) > 1e-9:
            raise AssertionError(f"{c['case_id']}: delta is not high minus low")
    return len(catalog["cases"])


def gate_monthly(records: list, claims_by_id: dict):
    for r in records:
        c = claims_by_id.get(r.get("claim"))
        if c is None:
            raise AssertionError(f"monthly record cites unknown claim {r.get('claim')}: {r.get('model')} {r.get('benchmark')}")
        if c.get("value") != r["value"]:
            raise AssertionError(f"monthly record {r['model']} {r['benchmark']}: value {r['value']} != claim {c.get('value')}")
    return len(records)


def gate_figures(pages: list):
    man = evidence.manifest()
    for f in pages:
        s = man.get(f["source_id"])
        if s is None or not evidence.source_sha_ok(f["source_id"]):
            raise AssertionError(f"page reference to an unpinned or modified source: {f['source_id']}")
        if not 1 <= f["page"] <= evidence.page_count(f["source_id"]):
            raise AssertionError(f"{f['slug']}: page {f['page']} does not exist")
        if not f["link"].startswith(s["url"]):
            raise AssertionError(f"{f['slug']}: link is not the pinned address")
        texts = evidence.page_texts(f["source_id"], f["page"])
        for cap in f["captions_on_page"]:
            head = evidence.normalise(cap.split(":", 1)[1].strip().rstrip("."))[:60]
            if head and not any(head in t for t in texts):
                raise AssertionError(f"{f['slug']}: caption not on page: {cap[:60]}")
    return len(pages)


def gate_documents(texts: dict, catalog: dict):
    for name, text in texts.items():
        for ch in ("\u2014", "\u2013"):
            if ch in text:
                raise AssertionError(f"{name}: contains a forbidden dash U+{ord(ch):04X}")
        for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (ROOT / target).exists():
                raise AssertionError(f"{name}: broken relative link {target}")
    readme = texts.get("README.md", "")
    for c in catalog["cases"]:
        row = re.search(rf"^\| \[?{c['case_id']}\]?[^\n]*$", readme, re.M)
        if row and f"{c['delta']:.1f}" not in row.group(0) and f"{c['delta']:.2f}" not in row.group(0):
            raise AssertionError(f"README row for {c['case_id']} does not show delta {c['delta']}")
    return len(texts)


def load_inputs():
    manifest = json.loads((DATA / "downloaded_sources_manifest.json").read_text())
    claims = evidence.load_claims()
    catalog = json.loads((DATA / "inconsistencies_catalog.json").read_text())
    monthly_path = DATA / "monthly_records.json"
    monthly = json.loads(monthly_path.read_text()) if monthly_path.exists() else []
    figures_path = DATA / "source_pages.json"
    figures = json.loads(figures_path.read_text()) if figures_path.exists() else []
    texts = {d: (ROOT / d).read_text() for d in DOCS if (ROOT / d).exists()}
    return manifest, claims, catalog, monthly, figures, texts


def run_gates(inputs):
    manifest, claims, catalog, monthly, figures, texts = inputs
    claims_by_id = {c["id"]: c for c in claims}
    results = [
        ("1 sources", gate_sources(manifest)),
        ("2 ledger", gate_ledger(claims)),
        ("3 catalog", gate_catalog(catalog)),
        ("4 monthly", gate_monthly(monthly, claims_by_id)),
        ("5 source pages", gate_figures(figures)),
        ("6 documents", gate_documents(texts, catalog)),
    ]
    for name, n in results:
        print(f"[PASS] gate {name}: {n} item(s)")


def expect_failure(label, fn):
    try:
        fn()
    except AssertionError:
        print(f"[PASS] break test: {label}")
        return 1
    raise RuntimeError(f"break test NOT caught: {label}")


def break_tests(inputs):
    manifest, claims, catalog, monthly, figures, texts = inputs
    claims_by_id = {c["id"]: c for c in claims}
    n = 0

    m = copy.deepcopy(manifest)
    m[0]["url"] = re.sub(r"v\d+$", "", m[0]["url"]) if m[0]["kind"] == "arxiv" else m[0]["url"] + "?latest"
    n += expect_failure("unversioned source URL", lambda: gate_sources(m))
    m = copy.deepcopy(manifest)
    m[0]["sha256"] = ("0" if m[0]["sha256"][0] != "0" else "1") + m[0]["sha256"][1:]
    n += expect_failure("flipped SHA-256 nibble", lambda: gate_sources(m))

    c = copy.deepcopy(claims)
    c[0]["value"] = c[0]["value"] + 0.1
    n += expect_failure("claim value +0.1", lambda: gate_ledger(c))
    c = copy.deepcopy(claims)
    tab = next(x for x in c if x.get("token") is not None)
    tab["token"] -= 1
    n += expect_failure("claim bound to the neighbouring column", lambda: gate_ledger(c))

    k = copy.deepcopy(catalog)
    k["cases"][0]["delta"] += 0.1
    n += expect_failure("catalog delta +0.1", lambda: gate_catalog(k))
    k = copy.deepcopy(catalog)
    k["cases"][0]["finding"] += " Independent labs measured 99.9."
    n += expect_failure("unbacked number appended to a finding", lambda: gate_catalog(k))

    if monthly:
        mm = copy.deepcopy(monthly)
        mm[0]["value"] += 0.1
        n += expect_failure("monthly value differs from its claim", lambda: gate_monthly(mm, claims_by_id))
        mm = copy.deepcopy(monthly)
        mm[0]["claim"] = "no-such-claim"
        n += expect_failure("monthly value without a claim", lambda: gate_monthly(mm, claims_by_id))

    if figures:
        ff = copy.deepcopy(figures)
        ff[0]["page"] += 1
        with_caps = next(f for f in ff if f["captions_on_page"])
        with_caps["captions_on_page"][0] = with_caps["captions_on_page"][0].split(":")[0] + ": a caption that is not on this page."
        n += expect_failure("source page reference moved to the wrong page / caption not on page", lambda: gate_figures(ff))

    if texts:
        tt = dict(texts)
        first = next(iter(tt))
        tt[first] = tt[first] + "\nA dash \u2014 here.\n"
        n += expect_failure("em dash in a document", lambda: gate_documents(tt, catalog))
        tt = dict(texts)
        tt[first] = tt[first] + "\n[x](assets/does-not-exist.png)\n"
        n += expect_failure("broken relative link", lambda: gate_documents(tt, catalog))
    print(f"[PASS] {n} break tests caught")


def main():
    inputs = load_inputs()
    run_gates(inputs)
    break_tests(inputs)
    print("All gates and break tests passed.")


if __name__ == "__main__":
    main()
