#!/usr/bin/env python3
"""Build the month-by-month dataset (2021-01 to 2026-10) from verified records only.

Input:  data/monthly_records.json  one record per (model, benchmark, reporting document), each citing a claim in
                                    data/claims.json; the record value must equal the claim value.
Output: data/monthly_benchmarks_2021_2026.json / .csv  per-month releases and the highest published value to date
        data/model_releases_master.csv                  flat list of all verified records

"Highest published value to date" is computed per benchmark family over all verified records whose reporting
document was public by that month (evidence.published_month), so a number measured later is not back-dated to the
model's release month.
Protocols differ between records (5-shot, CoT, voting, scaffolds); every frontier value carries its protocol and
claim id, and is not presented as a like-for-like comparison. Variants (HELM 5-subject MMLU, MMMLU, HumanEval-Mul,
SWE-bench vendor subsets, GPQA without a stated subset) are kept as records but excluded from the families.
"""

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402

ROOT = evidence.ROOT
DATA_DIR = ROOT / "data"
MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]

FAMILIES = {
    "MMLU": {"MMLU", "MMLU (English, not translated)"},
    "MMLU-Pro": {"MMLU-Pro"},
    "HumanEval": {"HumanEval", "HumanEval (Python)", "HumanEval (Codex P@1)"},
    "GSM8K": {"GSM8K"},
    "MATH": {"MATH"},
    "MATH-500": {"MATH-500"},
    "GPQA Diamond": {"GPQA Diamond", "GPQA-Diamond", "GPQA (Diamond per HF eval metadata gpqa_diamond)"},
    "SWE-bench Verified": {"SWE-bench Verified", "SWE-bench Verified (full 500)"},
    "AIME 2024": {"AIME 2024"},
    "AIME 2025": {"AIME 2025"},
}
FAMILY_OF = {name: fam for fam, names in FAMILIES.items() for name in names}
# Oracle metrics (pass@k with k > 1, "at least one correct in N samples") do not yield one answer per item; they are
# kept as records but never enter a family. Voting (maj@k, cons@k) yields one answer and is kept, with its protocol.
ORACLE = re.compile(r"pass@(?!1\b)\d+|at least one correct|oracle", re.I)
# Re-quotations of another document's number add no measurement and can only add transcription errors; they are
# kept as records but never define the highest-published series.
QUOTED = re.compile(r"as[- ]quoted|as reported in|quoted from|quoting|taken from|copied from|as cited", re.I)


def erroneous_claims() -> set:
    """Claims that the forensic catalog identifies as the erroneous side of a transcription error."""
    catalog = json.loads((DATA_DIR / "inconsistencies_catalog.json").read_text())
    return {c[c["erroneous"]] for c in catalog["cases"] if c.get("erroneous")}


def months():
    out = []
    for y in range(2021, 2027):
        for m in range(1, (10 if y == 2026 else 12) + 1):
            out.append((f"{y:04d}-{m:02d}", f"{MONTH_NAMES[m - 1]} {y}"))
    return out


def load_records():
    claims = {c["id"]: c for c in evidence.load_claims()}
    recs = json.loads((DATA_DIR / "monthly_records.json").read_text())
    bad = erroneous_claims()
    for r in recs:
        c = claims.get(r["claim"])
        if c is None:
            raise AssertionError(f"record cites unknown claim {r['claim']}")
        if c.get("value") != r["value"]:
            raise AssertionError(f"record {r['model']} {r['benchmark']}: value {r['value']} != claim {c.get('value')}")
        text = " ".join(str(c.get(k) or "") for k in ("id", "protocol", "note", "reported_by"))
        r["series_excluded"] = ("oracle metric" if ORACLE.search(r.get("protocol") or "") else
                                "re-quotation of another document" if QUOTED.search(text) else
                                "transcription error (forensic catalog)" if r["claim"] in bad else None)
        r["family"] = FAMILY_OF.get(r["benchmark"])
        r["source"] = c["source"]
        r["page"] = c["page"]
        # A number can only count as "published by month M" if its reporting document was public by M
        pub, basis = evidence.first_public_month(c)
        r["published_month"], r["published_basis"] = max(r["month"], pub), basis
    _, failures = evidence.verify_all([claims[r["claim"]] for r in recs], verbose=False)
    if failures:
        raise AssertionError(f"{len(failures)} cited claims fail verification")
    return recs


def build():
    recs = load_records()
    span = months()
    valid = {m for m, _ in span}
    out_of_range = [r for r in recs if r["month"] not in valid]
    if out_of_range:
        raise AssertionError(f"{len(out_of_range)} records outside 2021-01..2026-10, e.g. {out_of_range[0]}")
    frontier = {}
    monthly = []
    for idx, (ym, label) in enumerate(span, start=1):
        new = sorted([r for r in recs if r["month"] == ym], key=lambda r: (r["model"], r["benchmark"]))
        for r in sorted([r for r in recs if r["published_month"] == ym], key=lambda r: r["claim"]):
            fam = r["family"]
            if fam and not r["series_excluded"] and (fam not in frontier or r["value"] > frontier[fam]["value"]):
                frontier[fam] = {"value": r["value"], "model": r["model"], "protocol": r["protocol"],
                                 "claim": r["claim"], "published_month": ym, "model_month": r["month"],
                                 "reported_by": r["reported_by"]}
        models = sorted({r["model"] for r in new})
        monthly.append({"month_index": idx, "month": ym, "month_label": label, "is_release_month": bool(new),
                        "models": models, "records": new, "highest_published_to_date": json.loads(json.dumps(frontier))})
    (DATA_DIR / "monthly_benchmarks_2021_2026.json").write_text(json.dumps(monthly, indent=1, ensure_ascii=False) + "\n")

    fams = list(FAMILIES)
    with (DATA_DIR / "monthly_benchmarks_2021_2026.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month_index", "month", "verified_records", "models"]
                   + [x for fam in fams for x in (f"{fam} highest", f"{fam} model", f"{fam} claim")])
        for m in monthly:
            row = [m["month_index"], m["month"], len(m["records"]), "; ".join(m["models"])]
            for fam in fams:
                h = m["highest_published_to_date"].get(fam)
                row += [h["value"], h["model"], h["claim"]] if h else ["", "", ""]
            w.writerow(row)
    with (DATA_DIR / "model_releases_master.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "release_date", "model", "org", "benchmark", "family", "protocol", "value", "reported_by",
                    "published_month", "claim", "source", "page"])
        for r in sorted(recs, key=lambda r: (r["month"], r["model"], r["benchmark"])):
            w.writerow([r["month"], r.get("release_date") or "", r["model"], r.get("org") or "", r["benchmark"],
                        r["family"] or "", r["protocol"] or "", r["value"], r["reported_by"] or "", r["published_month"], r["claim"],
                        r["source"], r["page"]])
    n_models = len({r["model"] for r in recs})
    print(f"Built {len(monthly)} months from {len(recs)} verified records ({n_models} model names, "
          f"{sum(1 for r in recs if r['family'] and not r['series_excluded'])} eligible for the highest-published series; "
          f"excluded: {dict(Counter(r['series_excluded'] for r in recs if r['series_excluded']))}).")


if __name__ == "__main__":
    build()
