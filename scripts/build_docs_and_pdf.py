#!/usr/bin/env python3
"""Generate README.md, DISCREPANCY_AUDIT.md, BENCHMARKS_MONTH_BY_MONTH.md and the PDF report from the data files.

No number in these documents is typed here: counts, scores, deltas and statistics are read from data/*.json, which
are themselves built from the verified evidence ledger. The PDF is rendered with pandoc (Markdown to HTML) and
mutool (HTML to PDF, A4 landscape). Every table gets a CSS class with width 100% because mutool ignores the HTML
width attribute.
"""

import html
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docs_audit  # noqa: E402
import evidence  # noqa: E402

ROOT = evidence.ROOT
DATA = ROOT / "data"
PDF_PATH = ROOT / "seriously-models-benchmark-report-2021-2026.pdf"
TITLE = "Seriously, Models? A Source-Verified Audit of Frontier LLM Benchmark Reporting (2021-2026)"
FAMILY_ORDER = ["MMLU", "MMLU-Pro", "HumanEval", "GSM8K", "MATH", "MATH-500", "GPQA Diamond", "SWE-bench Verified",
                "AIME 2024", "AIME 2025"]


def pts(v) -> str:
    return docs_audit.pts(v)


def cell(text) -> str:
    return str(text if text is not None else "").replace("|", "/").replace("\n", " ")


def load():
    catalog, claims, sources = docs_audit.load()
    monthly = json.loads((DATA / "monthly_benchmarks_2021_2026.json").read_text())
    figures = json.loads((DATA / "source_pages.json").read_text())
    return catalog, claims, sources, monthly, figures


def stats(catalog, claims, sources, monthly):
    recs = [r for m in monthly for r in m["records"]]
    return {
        "sources": len(sources), "claims": len(claims), "records": len(recs),
        "models": len({r["model"] for r in recs}), "months": len(monthly),
        "release_months": sum(1 for m in monthly if m["is_release_month"]),
        "A": catalog["summary"]["A"], "B": catalog["summary"]["B"], "C": catalog["summary"]["C"]["n"],
    }


def pct(a, b) -> str:
    return f"{100 * a / b:.1f}%"


# ---------------------------------------------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------------------------------------------

def build_readme(catalog, claims, sources, monthly, s) -> str:
    rv = {}
    for c in claims.values():
        v = c.get("review", {}).get("verdict", "unreviewed")
        rv[v] = rv.get(v, 0) + 1
    rv_total = sum(rv.values())
    a_cases = [c for c in catalog["cases"] if c["class"] == "A"]
    b_cases = [c for c in catalog["cases"] if c["class"] == "B"]
    L = [f"# {TITLE}", "",
         f"Every number in this repository is a verbatim quote on a specific page of a SHA-256-pinned primary source "
         f"({s['sources']} documents: arXiv papers by version, vendor pages and system cards by Wayback Machine capture, "
         f"GitHub files by commit). {s['claims']:,} claims are checked mechanically on every build; a number that cannot "
         f"be found on its cited page is not published.", "",
         "## Findings", "",
         f"1. **{s['A']['n']} contradictions (class A):** the same model, benchmark and declared protocol carry different "
         f"published numbers. Median difference {pts(s['A']['median_delta_pts'])} points, range "
         f"{pts(s['A']['min_delta_pts'])} to {pts(s['A']['max_delta_pts'])}. They include a transcription error in a "
         f"competitor's table, a vendor publishing different numbers for its own model in two papers under identical "
         f"protocol text, competitors reporting a rival higher or lower than the rival itself, and text that disagrees "
         f"with the table next to it.",
         f"2. **{s['B']['n']} protocol asymmetries (class B):** the same model and benchmark under different disclosed "
         f"protocols. Median difference {pts(s['B']['median_delta_pts'])} points, range {pts(s['B']['min_delta_pts'])} "
         f"to {pts(s['B']['max_delta_pts'])}. The protocol a headline chooses (consensus voting, parallel sampling, a "
         f"modified prompt, a different scaffold or checkpoint under the same label) moves the reported number by "
         f"several points.",
         f"3. **{s['C']} pairs are not comparable (class C)** and are shown only as context: different benchmarks or test "
         f"sets, unestablished checkpoint identity, or an unstated protocol. No statistic pools classes.",
         "",
         "| Case | Class | Model | Benchmark | Published values | Difference (pts) |",
         "| :---: | :---: | :--- | :--- | :--- | :---: |"]
    for c in a_cases + b_cases:
        L.append(f"| [{c['case_id']}](DISCREPANCY_AUDIT.md#{c['case_id'].lower()}) | {c['class']} | {cell(c['model'])} | "
                 f"{cell(c['benchmark'])} | {pts(c['score_high'])} ({cell(c['source_high'])}) vs {pts(c['score_low'])} "
                 f"({cell(c['source_low'])}) | {pts(c['delta'])} |")
    L += ["", "![Verified discrepancies by class](assets/synthesis/fig01_verified_discrepancies_by_class.png)", "",
          "![Same quantity, two published numbers](assets/synthesis/fig02_same_quantity_two_numbers.png)", "",
          "![Primary-source crops](assets/synthesis/fig03_primary_source_crops.png)", "",
          "## Month-by-month dataset", "",
          f"{s['records']} verified scores for {s['models']} model names across {s['months']} months (January 2021 to "
          f"October 2026; {s['release_months']} months contain at least one verified score). Each score cites its claim. "
          "Figure 4 tracks, per benchmark, the highest value published by each month, dated by when the reporting "
          "document was public (the first arXiv version when the number is already in it). Protocols differ between "
          "points; oracle metrics such as pass@100 are excluded.", "",
          "![Highest published value by benchmark](assets/synthesis/fig04_highest_published_value_by_benchmark.png)", "",
          "| Month | Verified scores | Models | " + " | ".join(FAMILY_ORDER[:6]) + " |",
          "| :---: | :---: | :--- | " + " | ".join([":---:"] * 6) + " |"]
    for m in monthly:
        h = m["highest_published_to_date"]
        vals = [pts(h[f]["value"]) if f in h else "" for f in FAMILY_ORDER[:6]]
        models = ", ".join(m["models"][:4]) + (f" and {len(m['models']) - 4} more" if len(m["models"]) > 4 else "")
        L.append(f"| [{m['month']}](BENCHMARKS_MONTH_BY_MONTH.md#{m['month']}) | {len(m['records'])} | {cell(models)} | "
                 + " | ".join(vals) + " |")
    L += ["", "## Method and verification", "",
          "```bash",
          "python3 scripts/download_sources.py         # fetch and pin every source; refuses changed bytes",
          "python3 scripts/evidence.py                 # verify every claim against its pinned page",
          "python3 scripts/build_forensic_analysis.py  # build the case catalog and figures 1-3",
          "python3 scripts/build_dataset.py            # build the month-by-month dataset",
          "python3 scripts/generate_charts.py          # figure 4",
          "python3 scripts/extract_original_figures.py # references to the cited source pages",
          "python3 scripts/build_docs_and_pdf.py       # this README, the audit, the dossier and the PDF",
          "python3 scripts/adversarial_verify.py       # all gates plus break tests",
          "python3 -m unittest discover -s tests       # verifier unit and break tests",
          "```", "",
          "Requirements: Python 3, Pillow, poppler (pdftotext, pdftoppm, pdfinfo), curl; pandoc and mutool for the PDF.", "",
          "## Limitations", "",
          "1. Mechanical verification proves that a quoted string occurs on the cited page and that the value sits in the "
          "stated column. It does not prove that the model label in the claim is the one the source means; that "
          "attribution was made by reading the source, and column order was checked on rendered pages where text "
          "extraction is ambiguous.",
          "2. A source can be internally inconsistent. Example: the o3-mini launch post's image alt text gives 48.9 for "
          "o3-mini (high), while the chart itself shows 49.3 for o3-mini (high) and 48.9 for o1. Such cases are "
          "documented when found; the method does not detect them automatically.",
          "3. Numbers that appear only inside images are not used, except where stated as visual checks.",
          "4. Vendor web pages are cited through Wayback Machine captures; a capture shows the page as archived, which "
          "may differ from what was first published.",
          f"5. Most claims were extracted by AI agents working in parallel, each required to pass the same mechanical "
          f"verifier. Every claim was then reviewed a second time by independent reviewers who re-derived model, "
          f"benchmark variant, protocol and reporting party from the source page (rendered where text extraction is "
          f"ambiguous). {rv['OK']:,} of {rv_total:,} claims were confirmed as written; the others were corrected, mostly "
          f"protocol details, benchmark variants and re-quotations. Each claim records the outcome in its 'review' field.",
          "6. The highest-value-to-date series mixes protocols by construction; it is a record of what was published, "
          "not a like-for-like leaderboard.", "",
          "## Repository layout", "",
          "| Path | Content |", "| :--- | :--- |",
          "| `data/claims.json` | Evidence ledger: one entry per number, with source, page, verbatim quotes and column |",
          "| `data/source_specs.json`, `data/downloaded_sources_manifest.json` | Source addresses and SHA-256 pins |",
          "| `data/inconsistencies_catalog.json/.csv` | Case catalog (classes A, B, C), concordant cross-reports, sampling resolution |",
          "| `data/monthly_records.json` | Verified per-model scores, each citing a claim |",
          "| `data/monthly_benchmarks_2021_2026.json/.csv`, `data/model_releases_master.csv` | Month-by-month dataset |",
          "| `data/source_pages.json` | Links to the cited primary-source pages, with the captions found on each page |",
          "| `assets/synthesis/` | Figures 1-4 |",
          "| `scripts/`, `tests/` | Build, verification and tests |", "",
          "## License", "",
          "Code: MIT (`LICENSE`). Data compilation, documents and figures: CC BY 4.0 (`LICENSE-DATA.md`). The source "
          "documents belong to their authors and are not redistributed; the repository stores their pinned addresses "
          "and hashes. Short quoted excerpts and table crops remain the property of their owners.", ""]
    return "\n".join(L)


# ---------------------------------------------------------------------------------------------------------------
# Month-by-month dossier
# ---------------------------------------------------------------------------------------------------------------

def build_monthly(monthly, claims, sources, figures) -> str:
    figs = {}
    for f in figures:
        figs.setdefault(f["month"], []).append(f)
    L = ["# Month-by-Month Dossier (2021-01 to 2026-10)", "",
         "Generated from `data/monthly_benchmarks_2021_2026.json`. Each score links to its pinned source and cites the "
         "ledger claim that verifies it. A score's month is the model's release month as stated by a source or, if no "
         "source states it, the month of the reporting document.", ""]
    for m in monthly:
        L += [f"## {m['month']}", "", f"**{m['month_label']}.** "
              + (f"{len(m['records'])} verified scores for {len(m['models'])} model(s)." if m["records"]
                 else "No verified score is dated to this month."), ""]
        if m["records"]:
            L += ["| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |",
                  "| :--- | :--- | :--- | :---: | :--- | :--- | :--- |"]
            for r in m["records"]:
                s = sources[r["source"]]
                loc = f"p.{r['page']}" if s["ext"] == "pdf" else s["ext"]
                L.append(f"| {cell(r['model'])} | {cell(r['benchmark'])} | {cell(r['protocol'])} | {pts(r['value'])} | "
                         f"{cell(r['reported_by'])} | [{r['source']}]({s['url']}) {loc} | `{r['claim']}` |")
            L.append("")
        h = m["highest_published_to_date"]
        if h:
            L += ["Highest value published by the end of this month:", "",
                  "| Benchmark | Value | Model | Protocol | Published | Claim |", "| :--- | :---: | :--- | :--- | :---: | :--- |"]
            for fam in FAMILY_ORDER:
                if fam in h:
                    x = h[fam]
                    L.append(f"| {fam} | {pts(x['value'])} | {cell(x['model'])} | {cell(x['protocol'])} | "
                             f"{x['published_month']} | `{x['claim']}` |")
            L.append("")
        pages = figs.get(m["month"], [])
        if pages:
            L += ["Primary-source pages from documents first published this month (not redistributed; links open the "
                  "pinned version at the cited page):", ""]
            for f in pages:
                caps = "; ".join(f["captions_on_page"]) or "no table or figure caption on this page"
                L.append(f"- [{cell(f['title'])}, {f['version']}, PDF page {f['page']}]({f['link']}): {cell(caps)}")
            L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------------------------------------------------------
# PDF
# ---------------------------------------------------------------------------------------------------------------

CSS = """
body { font-family: Helvetica, Arial, sans-serif; color: #0f172a; font-size: 8.4pt; line-height: 1.3; margin: 0; }
h1 { font-size: 15pt; border-bottom: 2px solid #0369a1; padding-bottom: 3px; margin: 0 0 6px 0; }
h2 { font-size: 11.5pt; background: #e2e8f0; border-left: 4px solid #0369a1; padding: 3px 8px; margin: 10px 0 5px 0; }
h3 { font-size: 9.5pt; color: #1e3a8a; margin: 8px 0 3px 0; }
p, li { margin: 2px 0; }
table.full { width: 100%; border-collapse: collapse; margin: 4px 0 8px 0; font-size: 7.2pt; }
table.full th { background: #0f172a; color: #ffffff; text-align: left; padding: 3px 4px; }
table.full td { border-bottom: 1px solid #cbd5e1; padding: 2.5px 4px; vertical-align: top; }
code { font-family: Menlo, Courier, monospace; font-size: 6.8pt; }
pre { background: #f1f5f9; padding: 5px; font-size: 7pt; }
.pb { page-break-before: always; }
"""

PAGE_W, PAGE_H, MARGIN = 842, 595, 28


def to_html(markdown: str) -> str:
    out = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"], input=markdown, capture_output=True, text=True, check=True).stdout
    out = re.sub(r"<table[^>]*>", "<table class='full'>", out)
    out = re.sub(r"<colgroup>.*?</colgroup>", "", out, flags=re.S)
    out = re.sub(r"<h1", "<h1 class='pb'", out)

    def size_img(m):
        src = html.unescape(m.group(1))
        p = ROOT / src
        if not p.exists():
            return m.group(0)
        with Image.open(p) as im:
            w, h = im.size
        max_w, max_h = PAGE_W - 2 * MARGIN - 10, PAGE_H - 2 * MARGIN - 70
        width = int(min(max_w, max_h * w / h))
        return f"<p><img src='{src}' width='{width}' /></p>"
    out = re.sub(r"<img src=\"([^\"]+)\"[^>]*/?>", size_img, out)
    return out


def build_pdf(readme_md, audit_md, monthly_md):
    body = "\n".join(to_html(md) for md in (readme_md, audit_md, monthly_md))
    body = body.replace("<h1 class='pb'", "<h1", 1)
    page = (f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>{html.escape(TITLE)}</title>"
            f"<style>{CSS}</style></head><body>{body}</body></html>")
    html_path = ROOT / "report_build.html"
    raw = Path("/tmp/seriously_models_report_raw.pdf")
    html_path.write_text(page)
    try:
        subprocess.run(["mutool", "convert", "-W", str(PAGE_W), "-H", str(PAGE_H), "-S", "8.4", "-o", str(raw),
                        str(html_path)], check=True, capture_output=True)
        subprocess.run(["mutool", "clean", "-gggg", "-z", "-f", "-i", str(raw), str(PDF_PATH)], check=True, capture_output=True)
    finally:
        html_path.unlink(missing_ok=True)
        raw.unlink(missing_ok=True)
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(PDF_PATH)], capture_output=True,
                                                             text=True).stdout).group(1))
    print(f"PDF: {PDF_PATH.name}, {pages} pages, {PDF_PATH.stat().st_size // 1024} KB")


def main():
    catalog, claims, sources, monthly, figures = load()
    s = stats(catalog, claims, sources, monthly)
    readme = build_readme(catalog, claims, sources, monthly, s)
    audit = docs_audit.build_audit_markdown(catalog, claims, sources)
    monthly_md = build_monthly(monthly, claims, sources, figures)
    (ROOT / "README.md").write_text(readme + "\n")
    (ROOT / "DISCREPANCY_AUDIT.md").write_text(audit + "\n")
    (ROOT / "BENCHMARKS_MONTH_BY_MONTH.md").write_text(monthly_md + "\n")
    for name, text in (("README.md", readme), ("DISCREPANCY_AUDIT.md", audit), ("BENCHMARKS_MONTH_BY_MONTH.md", monthly_md)):
        if "\u2014" in text or "\u2013" in text:
            raise AssertionError(f"{name}: em/en dash in generated text")
    build_pdf(readme, audit, monthly_md)


if __name__ == "__main__":
    main()
