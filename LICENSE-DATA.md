# Data and documentation license

The code in `scripts/` and `tests/` is licensed under the MIT License (see `LICENSE`).

The data compilation, annotations, classifications and computed values in `data/`, the generated documents
(`README.md`, `DISCREPANCY_AUDIT.md`, `BENCHMARKS_MONTH_BY_MONTH.md`, the PDF report) and the figures in
`assets/synthesis/` are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0):
https://creativecommons.org/licenses/by/4.0/

Attribution: Fabrizio Salmi, "Seriously, Models? A Source-Verified Audit of Frontier LLM Benchmark Reporting
(2021-2026)", https://github.com/fabriziosalmi/seriously-models-verified

## Third-party material

The source documents (papers, model cards, system cards, launch posts, evaluation results) belong to their authors
and publishers and are not redistributed here. The repository stores only their addresses and SHA-256 hashes
(`data/source_specs.json`, `data/downloaded_sources_manifest.json`); `scripts/download_sources.py` fetches them from
the original or archived location.

Two kinds of third-party material appear in this repository, each attributed to its source:

1. Short verbatim excerpts in `data/claims.json` and in the generated documents, quoted to identify the number
   being verified (typically one table row or one sentence).
2. Small crops of tables in `assets/synthesis/fig03_primary_source_crops.png`, rendered from the cited pages to show
   the evidence for specific cases.

These excerpts remain the property of their respective owners and are not covered by the CC BY 4.0 license above.
Benchmark scores are reported as facts with their source; no endorsement by any of the cited organisations is
implied.
