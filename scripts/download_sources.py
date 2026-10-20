#!/usr/bin/env python3
"""Download and pin every primary source the evidence ledger (data/claims.json) may cite.

Every source is fetched from an immutable address:
  * arXiv papers by explicit version (https://arxiv.org/pdf/<id>v<N>);
  * vendor web pages and PDFs through a timestamped Wayback Machine capture (".../web/<ts>id_/<url>");
  * GitHub files at a fixed commit;
  * HELM classic results from the public release bucket.

The SHA-256 of each file is recorded in data/downloaded_sources_manifest.json on first download. A later run
that obtains different bytes for an already pinned source fails loudly instead of silently re-pinning.
"""

import concurrent.futures
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MANIFEST_PATH = DATA_DIR / "downloaded_sources_manifest.json"
CACHE_DIR = Path(os.environ.get("SERIOUSLY_MODELS_CACHE", "/tmp/seriously_models_sources"))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Encoding": "identity",
}

WAYBACK = "https://web.archive.org/web/{ts}id_/{url}"
HELM_V030 = "https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/{group}.json"
SIMPLE_EVALS = "https://raw.githubusercontent.com/openai/simple-evals/{commit}/README.md"


def arxiv(sid, version, month, title):
    return {"id": f"arxiv_{sid}", "kind": "arxiv", "arxiv_id": sid, "version": version, "month": month,
            "title": title, "url": f"https://arxiv.org/pdf/{sid}{version}", "ext": "pdf"}


def wayback(sid, ts, url, month, title, ext):
    return {"id": sid, "kind": "wayback", "original_url": url, "capture": ts, "month": month,
            "title": title, "url": WAYBACK.format(ts=ts, url=url), "ext": ext}


SPECS_PATH = DATA_DIR / "source_specs.json"


def load_specs() -> list:
    """Source specifications (what to fetch and from which immutable address) live in data/source_specs.json."""
    specs = json.loads(SPECS_PATH.read_text())
    for sp in specs:
        if sp["kind"] == "arxiv":
            sp["url"] = f"https://arxiv.org/pdf/{sp['arxiv_id']}{sp['version']}"
        elif sp["kind"] == "wayback":
            sp["url"] = WAYBACK.format(ts=sp["capture"], url=sp["original_url"])
    return specs


def _get(url: str) -> bytes:
    # The Wayback Machine answers 429 to Python's urllib under load but serves curl; use curl when available.
    if shutil.which("curl"):
        with tempfile.NamedTemporaryFile() as tmp:
            args = ["curl", "-sSfL", "--max-time", "120", "-A", HEADERS["User-Agent"], "-H", "Accept-Encoding: identity",
                    "-o", tmp.name, "-w", "%{url_effective}", url]
            final = subprocess.run(args, capture_output=True, text=True, check=True).stdout.strip()
            asked = re.search(r"/web/(\d{14})id_/", url)
            got = re.search(r"/web/(\d{14})id_/", final)
            # A Wayback timestamp that is not an exact capture redirects to the nearest one, whose bytes differ.
            if asked and (not got or got.group(1) != asked.group(1)):
                raise RuntimeError(f"Wayback redirected capture {asked.group(1)} to {final}; pin the exact capture")
            return Path(tmp.name).read_bytes()
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def fetch(url: str) -> bytes:
    last = None
    for attempt in range(4):
        try:
            data = _get(url)
            if data[:2] == b"\x1f\x8b":
                data = gzip.decompress(data)
            return data
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep((30 if "429" in str(e) else 5) * (attempt + 1))
    raise RuntimeError(f"download failed after retries: {last}")


def pin_one(item: dict, pinned: dict) -> dict:
    cache_file = f"{item['id']}.{item['ext']}"
    out_path = CACHE_DIR / cache_file
    data = out_path.read_bytes() if out_path.exists() and out_path.stat().st_size > 0 else None
    old = pinned.get(item["id"])
    if data is None or (old and hashlib.sha256(data).hexdigest() != old["sha256"]):
        data = fetch(item["url"])
        out_path.write_bytes(data)
    sha = hashlib.sha256(data).hexdigest()
    if old and old.get("sha256") and old["sha256"] != sha and not item.get("volatile"):
        raise RuntimeError(f"{item['id']}: fetched bytes do not match the pinned SHA-256 {old['sha256'][:16]}... (got {sha[:16]}...)")
    return {**item, "status": "pinned", "bytes": len(data), "sha256": sha, "cache_file": cache_file}


def stage(out_path: str, spec_json: str) -> int:
    """Fetch one new source into the cache and append it to a staging manifest (never the pinned one).

    spec: {"id", "kind": "wayback"|"arxiv"|"url", "month", "title", "ext", and
           wayback: "original_url" + "capture" | arxiv: "arxiv_id" + "version" | url: "url"}
    """
    spec = json.loads(spec_json)
    if spec["kind"] == "wayback":
        spec = wayback(spec["id"], spec["capture"], spec["original_url"], spec["month"], spec["title"], spec["ext"])
    elif spec["kind"] == "arxiv":
        spec = {**arxiv(spec["arxiv_id"], spec["version"], spec["month"], spec["title"]), "id": spec["id"]}
    pinned = {s["id"]: s for s in json.loads(MANIFEST_PATH.read_text())}
    if spec["id"] in pinned:
        print(f"{spec['id']} is already pinned in the main manifest")
        return 0
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    res = pin_one(spec, {})
    out = Path(out_path)
    staged = [s for s in (json.loads(out.read_text()) if out.exists() else []) if s["id"] != res["id"]]
    out.write_text(json.dumps(staged + [res], indent=2) + "\n")
    print(f"[staged] {res['id']} ({res['bytes']} bytes, sha256 {res['sha256'][:12]}) -> {out}")
    return 0


def main() -> int:
    if len(sys.argv) == 4 and sys.argv[1] == "--stage":
        return stage(sys.argv[2], sys.argv[3])
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    pinned = {s["id"]: s for s in json.loads(MANIFEST_PATH.read_text())} if MANIFEST_PATH.exists() else {}
    results, errors = [], []

    def record(item, fn):
        try:
            res = fn()
            results.append(res)
            print(f"[pinned] {res['id']} ({res['bytes']} bytes, sha256 {res['sha256'][:12]})")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{item['id']}: {e}")
            print(f"[ERROR] {item['id']}: {e}")

    # The Wayback Machine rate-limits parallel clients, so captures are fetched one at a time.
    sources = load_specs()
    parallel = [s for s in sources if s["kind"] != "wayback"]
    serial = [s for s in sources if s["kind"] == "wayback"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(pin_one, item, pinned): item for item in parallel}
        for f in concurrent.futures.as_completed(futs):
            record(futs[f], f.result)
    for item in serial:
        record(item, lambda item=item: pin_one(item, pinned))
        time.sleep(6)
    if errors:
        print(f"{len(errors)} source(s) failed; manifest not rewritten.")
        return 1
    results.sort(key=lambda x: (x["month"], x["id"]))
    MANIFEST_PATH.write_text(json.dumps(results, indent=2) + "\n")
    print(f"Done: {len(results)} sources pinned in {MANIFEST_PATH.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
