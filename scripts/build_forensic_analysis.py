#!/usr/bin/env python3
"""Build the forensic catalog of cross-source benchmark discrepancies from the evidence ledger.

Nothing numeric is typed into this file. Every score is read from data/claims.json (each claim is a verbatim
quote on a page of a SHA-256-pinned source, checked by scripts/evidence.py); deltas and derived statistics are
computed here. The build fails if:
  * a referenced claim does not verify against its pinned source;
  * the text of a case contains a number that is neither a value/quoted number of the claims it cites nor a
    value computed by this script;
  * a derived statistic recomputed from the pinned sources drifts from the value stated in the text.

Classes (applied strictly; only A and B are discrepancies):
  A  Contradiction: same model, same benchmark, same declared protocol, different published numbers.
  B  Protocol asymmetry: same model and benchmark, different protocols, each disclosed somewhere; the delta
     measures how much the reported number depends on the protocol that a headline chose.
  C  Not comparable: different benchmark/test set, an unestablished checkpoint identity, or a protocol not stated
     for one of the two numbers. Shown for context,
     never aggregated with A or B.
"""

import csv
import json
import math
import re
import statistics
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evidence  # noqa: E402

ROOT = evidence.ROOT
DATA_DIR = ROOT / "data"
SYNTH_DIR = ROOT / "assets" / "synthesis"
CLAIMS = {c["id"]: c for c in evidence.load_claims()}


# ---------------------------------------------------------------------------------------------------------------
# Derived quantities, recomputed from pinned sources on every build
# ---------------------------------------------------------------------------------------------------------------

def chinchilla_mmlu_averages() -> dict:
    """Macro (mean of 57 task accuracies) and micro (question-weighted) MMLU averages from Chinchilla Table A6."""
    counts_raw = json.loads(evidence.source_path("hf_cais_mmlu_size").read_text())
    counts = {s["config"]: s["num_rows"] for s in counts_raw["size"]["splits"]
              if s["split"] == "test" and s["config"] not in ("all", "auxiliary_train")}
    counts["high_school_gov_and_politics"] = counts["high_school_government_and_politics"]
    page = evidence.page_texts("arxiv_2203.15556", 31)[0]
    rows = re.findall(r"([a-z_]+) (\d+\.\d) (\d+\.\d)", page[page.find("abstract_algebra"):page.find("Table A6")])
    if len(rows) != 57:
        raise AssertionError(f"Chinchilla Table A6: expected 57 task rows, parsed {len(rows)}")
    out = {}
    for col, name in ((1, "chinchilla"), (2, "gopher")):
        vals = [float(r[col]) for r in rows]
        w = [counts[r[0]] for r in rows]
        out[f"{name}_macro"] = round(sum(vals) / len(vals), 2)
        out[f"{name}_micro"] = round(sum(v * n for v, n in zip(vals, w)) / sum(w), 2)
    out["gap_macro"] = round(out["chinchilla_macro"] - out["gopher_macro"], 1)
    out["gap_micro"] = round(out["chinchilla_micro"] - out["gopher_micro"], 1)
    return out


def mistral_row_differences() -> dict:
    """Count differing cells between the two Mistral AI papers for Mistral 7B and for the LLaMA 2 7B control row."""
    def cells(claim_id, skip):
        return [t.rstrip("%") for t in evidence.normalise(CLAIMS[claim_id]["quotes"][0]).split(" ")[skip:]]
    m1, m2 = cells("mistral7b-tr.mistral-7b.mmlu", 3), cells("mixtral-tr.mistral-7b.mmlu", 3)
    l1, l2 = cells("mistral7b-tr.llama2-7b.mmlu", 4), cells("mixtral-tr.llama2-7b.mmlu", 4)
    if not (len(m1) == len(m2) == len(l1) == len(l2) == 12):
        raise AssertionError("Mistral/Mixtral Table 2 rows must have 12 benchmark cells")
    return {"mistral_cells": 12, "mistral_differ": sum(a != b for a, b in zip(m1, m2)),
            "llama_differ": sum(a != b for a, b in zip(l1, l2)), "llama_same": sum(a == b for a, b in zip(l1, l2))}


def gsm1k_pvalues() -> dict:
    """Two-tailed p for the Z printed in the GSM1k appendix row of Mistral-7B-v0.1 (token 4 of the quoted row)."""
    z = float(evidence.normalise(CLAIMS["gsm1k.mistral-7b-v01.pvalue"]["quotes"][0]).split(" ")[4])
    return {"gsm1k_two_tailed_p": round(math.erfc(z / math.sqrt(2)), 3)}


def sampling_resolution() -> list:
    """Per-benchmark statistical resolution from the item count N (binomial model, independent items).

    one_item: score change from one question.  se_at_p: standard error at accuracy p.  mdd_unpaired: smallest
    difference between two models' scores that a two-sided unpaired z-test at alpha=0.05 can resolve at that p
    (1.96 * sqrt(2) * se). A paired test on the same items (McNemar) needs per-item data and is usually tighter;
    this is a conservative bound, not a measurement of any model.
    """
    rows = []
    for cid, name, p in (("n.mmlu", "MMLU", 0.9), ("n.mmlu-pro", "MMLU-Pro", 0.8), ("n.gsm8k", "GSM8K", 0.95),
                         ("n.math", "MATH (test)", 0.9), ("n.humaneval", "HumanEval", 0.9),
                         ("n.gpqa-diamond", "GPQA Diamond", 0.8), ("n.swebench-verified", "SWE-bench Verified", 0.7),
                         ("n.aime", "AIME (one year)", 0.8)):
        n = CLAIMS[cid]["value"]
        se = math.sqrt(p * (1 - p) / n) * 100
        rows.append({"benchmark": name, "n_items": n, "claim": cid, "p": p, "one_item_pts": round(100 / n, 2),
                     "se_pts": round(se, 2), "ci95_half_width_pts": round(1.96 * se, 2),
                     "mdd_unpaired_pts": round(1.96 * math.sqrt(2) * se, 2)})
    return rows


# ---------------------------------------------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------------------------------------------

CASES = [
    # Class A: contradictions
    {"case_id": "A1", "class": "A", "model": "Minerva 540B", "benchmark": "GSM8K (single sample)",
     "high": "llama1.minerva-540b.gsm8k.greedy", "low": "minerva.minerva-540b.gsm8k.greedy",
     "support": ["minerva.minerva-62b.gsm8k.maj1k", "minerva.minerva-540b.gsm8k.maj1k"],
     "kind": "Transcription error in a competitor's table", "erroneous": "high",
     "finding": "LLaMA-1 Table 7 prints 68.5 in the GSM8k column of the Minerva 540B row. The Minerva paper (Table 3) "
                "gives 58.8 for that cell; 68.5 is the maj1@k value of Minerva 62B, the row directly above. "
                "The other three cells of the row (33.6, 50.3, 78.5) match the Minerva paper."},
    {"case_id": "A2", "class": "A", "model": "Mistral 7B", "benchmark": "HumanEval (0-shot)",
     "high": "mistral7b-tr.mistral-7b.humaneval", "low": "mixtral-tr.mistral-7b.humaneval",
     "support": ["mistral7b-tr.mistral-7b.math", "mixtral-tr.mistral-7b.math", "mistral7b-tr.llama2-7b.mmlu", "mixtral-tr.llama2-7b.mmlu"],
     "kind": "Same vendor, same declared protocol, two papers",
     "finding": "Mistral AI reports Mistral 7B at 30.5 (Mistral 7B paper, Oct 2023) and 26.2 (Mixtral paper, Jan 2024) "
                "under word-identical protocol descriptions and an identical 'Evaluation Differences' note. Across the "
                "two Table 2s, Mistral 7B differs in {mistral_differ} of {mistral_cells} benchmark cells, while the "
                "LLaMA 2 7B control row is reproduced exactly in {llama_same} of {mistral_cells} (only NQ and TriviaQA "
                "change). Neither paper explains the change for Mistral 7B."},
    {"case_id": "A3", "class": "A", "model": "Mistral 7B", "benchmark": "MMLU (5-shot)",
     "high": "mixtral-tr.mistral-7b.mmlu", "low": "mistral7b-tr.mistral-7b.mmlu", "support": [],
     "kind": "Same vendor, same declared protocol, two papers",
     "finding": "Same pair of papers as A2: 60.1 in the Mistral 7B paper, 62.5 in the Mixtral paper, both 5-shot."},
    {"case_id": "A4", "class": "A", "model": "Mistral 7B", "benchmark": "GSM8K (8-shot maj@8)",
     "high": "mistral7b-tr.mistral-7b.gsm8k", "low": "mixtral-tr.mistral-7b.gsm8k", "support": [],
     "kind": "Same vendor, same declared protocol, two papers",
     "finding": "Same pair of papers as A2: 52.2 in the Mistral 7B paper, 50.0 in the Mixtral paper, both declared as "
                "GSM8K (8-shot) with maj@8."},
    {"case_id": "A5", "class": "A", "model": "Claude 3.5 Sonnet (June 2024)", "benchmark": "MMLU (5-shot)",
     "high": "llama31-tr.claude-35-sonnet.mmlu.5shot", "low": "anthropic-35-addendum.claude-35-sonnet.mmlu.5shot",
     "support": ["llama31-tr.claude-35-sonnet.mmlu.0shot-cot", "anthropic-35-addendum.claude-35-sonnet.mmlu.0shot-cot"],
     "kind": "Competitor reports a higher number than the vendor",
     "finding": "Meta's Llama 3 paper lists Claude 3.5 Sonnet at 89.9 on 5-shot MMLU; Anthropic's model card addendum "
                "lists 88.7 for the same protocol. For 0-shot CoT both documents give 88.3."},
    {"case_id": "A6", "class": "A", "model": "Claude 3.5 Sonnet (new, 2024-10-22)", "benchmark": "MMLU (0-shot CoT)",
     "high": "anthropic-35-oct.claude-35-sonnet-new.mmlu.0shot-cot", "low": "deepseek-r1-v1.claude-35-sonnet-1022.mmlu",
     "support": ["anthropic-35-oct.claude-35-sonnet-new.mmlu-pro.0shot-cot", "deepseek-r1-v1.claude-35-sonnet-1022.mmlu-pro",
                 "anthropic-35-oct.claude-35-sonnet-new.gpqa.0shot-cot", "deepseek-r1-v1.claude-35-sonnet-1022.gpqa",
                 "anthropic-35-addendum.claude-35-sonnet.mmlu.0shot-cot", "anthropic-35-oct.simple-evals-mmlu-is-0shot-cot",
                 "anthropic-35-addendum.simple-evals-mmlu-is-0shot-cot"],
     "kind": "Competitor reports a lower number than the vendor",
     "finding": "Anthropic's October 2024 addendum gives 89.3 (0-shot CoT). DeepSeek-R1 v1 Table 4 gives 88.3 for "
                "Claude-3.5-Sonnet-1022 with simple-evals prompts; Anthropic's own addenda state that the simple-evals "
                "MMLU implementation uses 0-shot CoT. 88.3 is the value Anthropic "
                "published for the June model. On MMLU-Pro (78.0) and GPQA Diamond (65.0) the two documents agree."},
    {"case_id": "A7", "class": "A", "model": "Chinchilla", "benchmark": "MMLU (5-shot)",
     "high": "chinchilla-tr.table6.chinchilla.mmlu", "low": "chinchilla-tr.abstract.chinchilla.mmlu",
     "support": ["chinchilla-tr.table6.gopher.mmlu", "n.mmlu"],
     "kind": "Abstract vs table; mixed averaging conventions",
     "finding": "Abstract 67.5, Table 6 67.6. Recomputed from the 57 per-task accuracies in Table A6: macro average "
                "{chinchilla_macro}, question-weighted average {chinchilla_micro}. Gopher's 60.0 in the same table "
                "matches Gopher's question-weighted average ({gopher_micro}), not its macro average ({gopher_macro}). "
                "With one convention for both models the gap is {gap_macro} (macro) or {gap_micro} (weighted) points; "
                "the text states 7.6. The difference is small; it is listed because it is exactly reproducible."},

    {"case_id": "A8", "class": "A", "model": "PaLM 540B", "benchmark": "GSM8K (8-shot chain-of-thought)",
     "high": "m2022.wei.palm-540b.gsm8k.8shot-cot", "low": "m2022.palm.palm-540b.gsm8k.8shot-cot",
     "support": ["m2022.wang.palm-540b.gsm8k.cot-greedy", "m2022.minerva.palm-540b.gsm8k.cot"],
     "kind": "Three Google papers, one model, one protocol",
     "finding": "The chain-of-thought paper reports 56.9, the PaLM paper 54 (using the same eight exemplars), and the "
                "self-consistency paper 56.5 with greedy chain-of-thought. The Minerva paper prints 56.5 and attributes "
                "it to the PaLM paper, which prints 54."},
    {"case_id": "A9", "class": "A", "model": "GPT-4", "benchmark": "MMLU (5-shot)",
     "high": "m2023.almazrouei2023.gpt-4.mmlu.5shot-as-quoted", "low": "m2023.openai2023.gpt-4.mmlu.5shot", "support": [],
     "kind": "Transcription error when quoting another report", "erroneous": "high",
     "finding": "The Falcon paper lists GPT-4 at 86.5 'as reported in GPT-4 paper'; the GPT-4 report gives 86.4."},
    {"case_id": "A10", "class": "A", "model": "GPT-J 6B", "benchmark": "HumanEval pass@1",
     "high": "m2021.chen-codex.gpt-j-6b.humaneval.pass-at-1", "low": "m2021.chen-codex.gpt-j.humaneval.abstract", "support": [],
     "kind": "Abstract vs table in the same paper",
     "finding": "The Codex paper's abstract says GPT-J solves 11.4% of the problems; Table 1 gives pass@1 = 11.62."},
    {"case_id": "A11", "class": "A", "model": "Llama 2 70B", "benchmark": "HumanEval (0-shot pass@1)",
     "high": "m2023.roziere2023.llama-2-70b.humaneval.pass1", "low": "m2023.touvron2023b.llama-2-70b.humaneval.0shot", "support": [],
     "kind": "Same vendor, two papers",
     "finding": "Meta's Code Llama paper lists Llama 2 70B at 30.5 pass@1; the Llama 2 paper lists 29.9 (0-shot)."},
    {"case_id": "A12", "class": "A", "model": "GPT-6 Astra", "benchmark": "Terminal-Bench 4.0",
     "high": "m2026.astra.gpt-6-astra.terminal-bench-4-0.prose", "low": "m2026.astra.gpt-6-astra.terminal-bench-4-0.table", "support": [],
     "kind": "Text vs table in the same launch post",
     "finding": "OpenAI's GPT-6 Astra post states 57.9 in the text and 57.7 in its evaluation table."},

    # Class B: protocol asymmetry
    {"case_id": "B1", "class": "B", "model": "Mixtral 8x7B", "benchmark": "GSM8K",
     "high": "mixtral-tr.mixtral-8x7b.gsm8k.maj8", "low": "mixtral-tr.mixtral-8x7b.gsm8k.5shot", "support": [],
     "kind": "Two protocols in one paper",
     "finding": "Table 2 reports 74.4 (8-shot maj@8); Table 3, the comparison with GPT-3.5, reports 58.4 (5-shot)."},
    {"case_id": "B2", "class": "B", "model": "OpenAI o3-mini (high)", "benchmark": "SWE-bench Verified",
     "high": "gpt45-blog.o3-mini-high.swebench-verified", "low": "m2025.gpt41-blog.o3-mini-high.swebench",
     "support": ["o3mini-card.o3-mini-tools.swebench-verified", "m2025.o3-blog.o3-mini.swebench", "o3mini-blog.o3-mini-high.swebench-verified"],
     "kind": "Same product label, different checkpoint and scaffold",
     "finding": "OpenAI publishes two SWE-bench Verified numbers under the label 'OpenAI o3-mini (high)': 61.0 in the "
                "GPT-4.5 launch table (footnote: 'best internal performance') and 49.3 in the GPT-4.1 launch appendix "
                "and the o3 launch chart. The o3-mini system card explains 61: a non-final checkpoint with an internal "
                "tools scaffold on a 477-task subset; the launch candidate with Agentless scores 39. The o3-mini launch "
                "post's image alt text says 48.9, which in the chart image is o1's bar."},
    {"case_id": "B3", "class": "B", "model": "PaLM 2", "benchmark": "GSM8K",
     "high": "palm2-tr.palm2.gsm8k.sc", "low": "palm2-tr.palm2.gsm8k.cot", "support": [],
     "kind": "Two protocols in one table cell",
     "finding": "PaLM 2 Table 7 prints 80.7 / 91.0 (chain-of-thought / self-consistency) in the same cell."},
    {"case_id": "B4", "class": "B", "model": "Claude Sonnet 5.5", "benchmark": "Terminal-Bench 4.0",
     "high": "anthropic-sonnet55.sonnet-55.terminal-bench-4", "low": "aa.sonnet-55.terminal-bench-4", "support": [],
     "kind": "Vendor harness vs independent harness",
     "finding": "Anthropic reports 70.6; Artificial Analysis reports 63.6 on its own harness, for the configuration it "
                "labels 'Max, Default Fallback'."},
    {"case_id": "B5", "class": "B", "model": "Claude Opus 5.5", "benchmark": "Terminal-Bench 4.0",
     "high": "anthropic-opus55.opus-55.terminal-bench-4", "low": "aa.opus-55.terminal-bench-4", "support": [],
     "kind": "Vendor harness vs independent harness",
     "finding": "Anthropic reports 66.4 at xhigh effort, with production safeguards enabled, and states that its setup "
                "reproduces the public leaderboard for Opus 5 (51.8 vs 52.3); Artificial Analysis reports 59.6 for the "
                "configuration it labels 'Max, Default Fallback'."},
    {"case_id": "B6", "class": "B", "model": "Claude 3.7 Sonnet", "benchmark": "SWE-bench Verified (489-task subset)",
     "high": "claude37-blog.claude-37-sonnet.swebench-verified.parallel", "low": "claude37-blog.claude-37-sonnet.swebench-verified.single",
     "support": [],
     "kind": "Parallel test-time compute shown next to the single-attempt score",
     "finding": "70.3 with parallel attempts and a scoring model, 63.7 without, both on the same 489-task subset."},
    {"case_id": "B7", "class": "B", "model": "Gemini Ultra", "benchmark": "MMLU",
     "high": "gemini1-tr.gemini-ultra.mmlu.cot32", "low": "gemini1-tr.gemini-ultra.mmlu.5shot",
     "support": ["gemini-blog.gemini-ultra.mmlu", "mmlu-paper.human-expert", "gemini1-tr.gpt4.mmlu.5shot-reported"],
     "kind": "Headline uses the protocol that crosses a threshold",
     "finding": "The launch post states 90.0 and 'first model to outperform human experts on MMLU' (expert estimate "
                "89.8). The technical report shows 90.04 with uncertainty-routed CoT@32 and 83.7 with 5-shot, below "
                "GPT-4's reported 86.4."},
    {"case_id": "B8", "class": "B", "model": "gpt-4o (2024-05-13)", "benchmark": "GPQA (subset not named in the README)",
     "high": "simple-evals-2024-05-13.gpt-4o.gpqa.chatgpt-prompt", "low": "simple-evals-2024-05-13.gpt-4o.gpqa.assistant-prompt",
     "support": ["simple-evals-2025-07-09.gpt-4o-0513.gpqa.assistant-prompt"],
     "kind": "Two system prompts; the higher row later removed",
     "finding": "On GPT-4o's launch day OpenAI's simple-evals README listed two rows: 53.6 with the 'chatgpt' system "
                "prompt and 49.9 with the 'assistant' prompt. The July 2025 README lists only the 49.9 row."},
    {"case_id": "B9", "class": "B", "model": "Claude 3.5 Sonnet (June 2024)", "benchmark": "MMLU",
     "high": "anthropic-35-addendum.claude-35-sonnet.mmlu.5shot-cot", "low": "anthropic-35-addendum.claude-35-sonnet.mmlu.0shot-cot",
     "support": ["anthropic-35-addendum.claude-35-sonnet.mmlu.5shot"],
     "kind": "Three protocols in one table",
     "finding": "The addendum gives 90.4 (5-shot CoT), 88.7 (5-shot) and 88.3 (0-shot CoT)."},

    {"case_id": "B10", "class": "B", "model": "Claude 3.5 Sonnet (June 2024)", "benchmark": "MMLU-Pro",
     "high": "m2024.llama3herd.claude-3.5-sonnet.mmlu-pro.5-shot-cot", "low": "m2024.c35oct.claude-3.5-sonnet.mmlu-pro.0-shot-cot", "support": [],
     "kind": "Competitor uses a different protocol",
     "finding": "Meta reports 77.0 (5-shot CoT); Anthropic reports 75.1 (0-shot CoT)."},
    {"case_id": "B11", "class": "B", "model": "Claude Opus 4.6", "benchmark": "SWE-bench Verified",
     "high": "m2026.opus46blog.claude-opus-4-6.swe-bench-verified.prompt-modified", "low": "m2026.opus46card.claude-opus-4-6.swe-bench-verified.standard",
     "support": ["m2026.opus46card.claude-opus-4-6.swe-bench-verified.prompt-modified"],
     "kind": "Prompt modification reported next to the standard score",
     "finding": "The system card reports 80.84 with the standard prompt and 81.4 with a prompt modification; the launch "
                "post gives 81.42 with the prompt modification."},
    {"case_id": "B12", "class": "B", "model": "GPT-6 Astra", "benchmark": "Terminal-Bench 4.0",
     "high": "m2026.aa.gpt-6-astra.terminal-bench-4-0", "low": "m2026.astra.gpt-6-astra.terminal-bench-4-0.table", "support": [],
     "kind": "Independent harness reports a higher number than the vendor",
     "finding": "Artificial Analysis reports 59.1 at max effort; OpenAI's table gives 57.7. Here the independent number "
                "is the higher one."},

    # Class C: not comparable
    {"case_id": "C1", "class": "C", "model": "GPT-4", "benchmark": "MATH",
     "high": "gemini1-tr.gpt4.math.api", "low": "palm2-tr.gpt4.math", "support": ["gemini1-tr.gpt4.math.zheng"],
     "kind": "Checkpoint not identified",
     "finding": "52.9 (Gemini report, own API run in Nov 2023, snapshot not stated), 50.3 (Zheng et al., cited by "
                "Gemini) and 42.5 (PaLM 2 report). The documents do not establish that the same GPT-4 snapshot was "
                "measured, so the spread is not attributed to evaluation alone."},
    {"case_id": "C2", "class": "C", "model": "gpt-3.5-turbo / 'GPT-3.5'", "benchmark": "GSM8K",
     "high": "cothub.gpt-35-turbo.gsm8k", "low": "gpt4-tr.gpt-35.gsm8k", "support": [],
     "kind": "Checkpoint identity asserted by a third party",
     "finding": "Chain-of-Thought Hub measures gpt-3.5-turbo at 74.9 with its own scripts; the GPT-4 report lists "
                "'GPT-3.5' at 57.1 (5-shot). CoT Hub treats the GPT-4 report's GPT-3.5 column as gpt-3.5-turbo; OpenAI "
                "does not name the snapshot."},
    {"case_id": "C3", "class": "C", "model": "Claude Opus 4.5", "benchmark": "SWE-bench Verified vs SWE-bench Pro",
     "high": "kimi-k25.claude-opus-45.swebench-verified", "low": "kimi-k25.claude-opus-45.swebench-pro", "support": [],
     "kind": "Different benchmarks",
     "finding": "80.9 on SWE-bench Verified and 55.4 on SWE-bench Pro (Moonshot internal evaluation). Two benchmarks; "
                "not a discrepancy."},
    {"case_id": "C4", "class": "C", "model": "DeepSeek-R1", "benchmark": "MMLU vs MMLU-Redux",
     "high": "deepseek-r1-v1.deepseek-r1.mmlu-redux", "low": "deepseek-r1-v1.deepseek-r1.mmlu", "support": [],
     "kind": "Different test sets and prompts",
     "finding": "92.9 on MMLU-Redux (ZeroEval prompt) and 90.8 on MMLU (simple-evals prompt), DeepSeek-R1 v1 Table 4."},
    {"case_id": "C5", "class": "C", "model": "GPT-4 / ChatGPT", "benchmark": "HumanEval vs HumanEval+",
     "high": "evalplus.gpt-4.humaneval-base", "low": "evalplus.gpt-4.humaneval-plus",
     "support": ["evalplus.chatgpt.humaneval-base", "evalplus.chatgpt.humaneval-plus"],
     "kind": "Different test suites",
     "finding": "EvalPlus: GPT-4 88.4 on the original tests, 76.2 with the extended tests; ChatGPT 73.2 and 63.4."},
    {"case_id": "C6", "class": "C", "model": "GLM-130B", "benchmark": "MMLU (57 subjects) vs HELM MMLU (5 subjects)",
     "high": "glm130b-tr.glm-130b.mmlu", "low": "helm-v030.glm-130b.mmlu", "support": [],
     "kind": "Different test sets",
     "finding": "44.8 in the GLM-130B paper (5-shot, 57 subjects); 34.4 in HELM, whose MMLU is a 5-subject subset "
                "scored by exact match."},
    {"case_id": "C7", "class": "C", "model": "Mistral-7B-v0.1", "benchmark": "GSM8K vs GSM1k",
     "high": "gsm1k.mistral-7b-v01.gsm8k", "low": "gsm1k.mistral-7b-v01.gsm1k", "support": ["gsm1k.mistral-7b-v01.pvalue", "gsm1k.max-drop"],
     "kind": "Different test sets; difference not significant",
     "finding": "Scale AI measures 39.1 on GSM8K and 36.4 on GSM1k for Mistral-7B-v0.1, p = 0.078 in the paper's own "
                "test. The paper's maximum drop across all models is 8 points."},
    {"case_id": "C8", "class": "C", "model": "GPT-4 (March 2023) vs gpt-4-0125-preview", "benchmark": "HumanEval",
     "high": "simple-evals-2025-07-09.gpt-4-0125.humaneval", "low": "claude3-card.gpt4.humaneval.reported", "support": [],
     "kind": "Different checkpoints; disclosed",
     "finding": "The Claude 3 model card compares against GPT-4's March 2023 HumanEval figure (67.0) and states in "
                "footnote 6 that higher scores were reported for a newer GPT-4T; simple-evals lists 86.6 for "
                "gpt-4-0125-preview."},
    {"case_id": "C9", "class": "C", "model": "GPT-5.5", "benchmark": "SWE-Bench Pro",
     "high": "m2026.gpt56.gpt-5-5.swe-bench-pro", "low": "m2026.gpt55.gpt-5-5.swe-bench-pro", "support": [],
     "kind": "Protocol not stated for one number",
     "finding": "OpenAI's GPT-5.5 post gives 58.6 at xhigh effort; OpenAI's GPT-5.6 post lists GPT-5.5 at 59.4 without "
                "stating the setting."},
    {"case_id": "C10", "class": "C", "model": "QwQ-32B-Preview", "benchmark": "GPQA",
     "high": "m2024.qwq.qwq-32b-preview.gpqa.unspecified", "low": "m2024.r1v1.qwq-32b-preview.gpqa-diamond.pass1", "support": [],
     "kind": "Protocol and subset not stated by the vendor",
     "finding": "Qwen's post states 65.2 on GPQA without naming the subset or protocol; DeepSeek measures 54.5 on GPQA "
                "Diamond, pass@1."},
    {"case_id": "C11", "class": "C", "model": "Codex (size not named in the abstract) vs Codex-12B", "benchmark": "HumanEval, 100 samples per problem",
     "high": "codex-tr.table1.codex-12b.humaneval.pass100", "low": "codex-tr.abstract.codex-12b.humaneval.pass100",
     "support": ["m2021.chen-codex.codex-12b.humaneval.pass-at-1"],
     "kind": "Model identity inferred, not stated",
     "finding": "The Codex abstract says 'our model' solves 70.2% of problems with 100 samples per problem without naming "
                "its size; Table 1 gives Codex-12B pass@100 = 72.31. The abstract's single-sample figure matches "
                "Codex-12B's pass@1 (28.81 in Table 1), which suggests but does not establish that both numbers refer to "
                "the same model."},
    {"case_id": "C12", "class": "C", "model": "Grok 3 (Think)", "benchmark": "AIME 2025",
     "high": "grok3-blog.grok3-think.aime25.cons64", "low": "grok3-blog.grok3-think.aime25.base",
     "support": ["grok3-blog.o3-mini-high.aime25"],
     "kind": "Protocol of one value not stated",
     "finding": "xAI's launch chart shows two values for Grok 3 (Think): 93.3, which the text identifies as cons@64, and "
                "77.3, whose setting the page does not define. A competitor bar coded O3MH shows a single value, 86.5; "
                "the pinned page does not resolve the code to a model name. The headline number is the cons@64 value."},
]

CONCORDANT = [
    ("o1-blog.o1-preview.gpqa.pass1", "simple-evals-2025-07-09.o1-preview.gpqa"),
    ("anthropic-35-addendum.claude-35-sonnet.mmlu.0shot-cot", "llama31-tr.claude-35-sonnet.mmlu.0shot-cot"),
    ("anthropic-35-oct.claude-35-sonnet-new.mmlu-pro.0shot-cot", "deepseek-r1-v1.claude-35-sonnet-1022.mmlu-pro"),
    ("anthropic-35-oct.claude-35-sonnet-new.gpqa.0shot-cot", "deepseek-r1-v1.claude-35-sonnet-1022.gpqa"),
    ("simple-evals-2024-05-13.gpt-4o.gpqa.assistant-prompt", "simple-evals-2025-07-09.gpt-4o-0513.gpqa.assistant-prompt"),
]

# ---------------------------------------------------------------------------------------------------------------
# Assembly and gates
# ---------------------------------------------------------------------------------------------------------------

def claim_numbers(cid: str) -> set:
    c = CLAIMS[cid]
    nums = set()
    for q in c["quotes"]:
        text = q["text"] if isinstance(q, dict) else q
        nums |= {n.replace(",", "") for n in re.findall(r"\d[\d,]*\.?\d*", evidence.normalise(text))}
    if c.get("value") is not None:
        nums.add(str(c["value"]))
        nums.add(f"{float(c['value']):g}")
    return nums


def canonical(num: str) -> str:
    try:
        return f"{float(num):g}"
    except ValueError:
        return num


def build_catalog():
    derived = {**chinchilla_mmlu_averages(), **mistral_row_differences(), **gsm1k_pvalues()}
    referenced = set()
    out_cases = []
    for case in CASES:
        hi, lo = CLAIMS[case["high"]], CLAIMS[case["low"]]
        delta = round(hi["value"] - lo["value"], 2)
        if delta <= 0:
            raise AssertionError(f"{case['case_id']}: high claim must exceed low claim")
        ids = [case["high"], case["low"]] + case["support"]
        referenced |= set(ids)
        finding = case["finding"].format(**derived)
        allowed = set()
        for cid in ids:
            allowed |= {canonical(n) for n in claim_numbers(cid)}
        allowed |= {canonical(str(v)) for v in derived.values()} | {canonical(str(delta))}
        names = " ".join([case["model"], case["benchmark"]] + [CLAIMS[c]["model"] + " " + CLAIMS[c]["benchmark"] for c in ids])
        allowed |= {canonical(n) for n in re.findall(r"\d+(?:\.\d+)?", names)}
        # Score-like tokens: decimals and integers of 2+ digits that are not part of an identifier or a year
        tokens = re.findall(r"(?<![\w.\-])(\d+\.\d+|\d{2,})(?![\w\-]|\.\d)", finding)
        stray = [n for n in tokens if not re.fullmatch(r"(19|20)\d\d", n) and canonical(n) not in allowed]
        if stray:
            raise AssertionError(f"{case['case_id']}: numbers in text not backed by cited claims or computation: {stray}")
        out_cases.append({**{k: v for k, v in case.items() if k not in ("finding",)}, "finding": finding,
                          "score_high": hi["value"], "source_high": hi["reported_by"], "protocol_high": hi.get("protocol"),
                          "score_low": lo["value"], "source_low": lo["reported_by"], "protocol_low": lo.get("protocol"),
                          "delta": delta})
    for a, b in CONCORDANT:
        referenced |= {a, b}
        if CLAIMS[a]["value"] != CLAIMS[b]["value"]:
            raise AssertionError(f"concordant pair differs: {a} vs {b}")
    snr = sampling_resolution()
    referenced |= {r["claim"] for r in snr}

    missing = sorted(referenced - set(CLAIMS))
    if missing:
        raise AssertionError(f"referenced claims missing from ledger: {missing}")
    _, failures = evidence.verify_all([CLAIMS[c] for c in sorted(referenced)], verbose=False)
    if failures:
        raise AssertionError(f"referenced claims fail verification: {failures}")

    def summary(cls):
        d = [c["delta"] for c in out_cases if c["class"] == cls]
        return {"n": len(d), "median_delta_pts": round(statistics.median(d), 2), "min_delta_pts": min(d), "max_delta_pts": max(d)}

    return {
        "schema": "seriously-models/forensic-catalog/v2",
        "classes": {"A": "Contradiction: same model, benchmark and declared protocol; different published numbers",
                    "B": "Protocol asymmetry: same model and benchmark; different disclosed protocols",
                    "C": "Not comparable: different benchmark/test set, unestablished checkpoint identity, or unstated protocol"},
        "summary": {"A": summary("A"), "B": summary("B"), "C": {"n": sum(1 for c in out_cases if c["class"] == "C")}},
        "derived": derived,
        "cases": out_cases,
        "concordant": [{"a": a, "b": b, "value": CLAIMS[a]["value"], "model": CLAIMS[a]["model"],
                        "benchmark": CLAIMS[a]["benchmark"], "reported_by": [CLAIMS[a]["reported_by"], CLAIMS[b]["reported_by"]]}
                       for a, b in CONCORDANT],
        "sampling_resolution": snr,
        "claims_referenced": len(referenced),
    }


# ---------------------------------------------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------------------------------------------

FONT_PATHS = ["/System/Library/Fonts/Helvetica.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
MONO_PATHS = ["/System/Library/Fonts/Menlo.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"]


def font(size: int, bold: bool = False, mono: bool = False):
    for p in (MONO_PATHS if mono else FONT_PATHS):
        if Path(p).exists():
            return ImageFont.truetype(p, size, index=1 if (bold and p.endswith(".ttc")) else 0)
    return ImageFont.load_default()


BG, CARD, BORDER, HDR, TXT, MUTED = (248, 250, 252), (255, 255, 255), (203, 213, 225), (15, 23, 42), (15, 23, 42), (71, 85, 105)
CLASS_COL = {"A": (185, 28, 28), "B": (180, 83, 9), "C": (100, 116, 139)}


def pts(v) -> str:
    """Print a score with the precision it was published with (one decimal, or two when the source has two)."""
    return f"{v:.1f}" if round(v, 1) == v else f"{v:.2f}"


def header(d, w, title, subtitle):
    d.rectangle((0, 0, w, 90), fill=HDR)
    d.text((32, 16), title, fill=(255, 255, 255), font=font(24, bold=True))
    d.text((32, 54), subtitle, fill=(203, 213, 225), font=font(14, bold=True))


def fig_catalog(catalog):
    cases = catalog["cases"]
    W, row_h = 1600, 30
    H = 110 + row_h * (len(cases) + 3) + 3 * 8 + 60
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    header(d, W, "FIG 1: VERIFIED CROSS-SOURCE DISCREPANCIES BY CLASS",
           "Every bar is the difference between two published numbers, each a verbatim quote on a pinned source page (data/claims.json)")
    y = 110
    labels = {"A": "Class A - contradiction (same model, benchmark and declared protocol)",
              "B": "Class B - protocol asymmetry (different protocols, each disclosed)",
              "C": "Class C - not comparable (different test set or checkpoint; context only)"}
    x0, x1, scale_max = 700, 1360, 20.0
    for cls in ("A", "B", "C"):
        d.text((40, y), labels[cls], fill=CLASS_COL[cls], font=font(15, bold=True))
        y += row_h
        for c in sorted([c for c in cases if c["class"] == cls], key=lambda c: -c["delta"]):
            lbl = f"{c['case_id']}  {c['model']} | {c['benchmark']}"
            d.text((56, y + 6), lbl if len(lbl) <= 78 else lbl[:75] + "...", fill=TXT, font=font(13, bold=True))
            values = f"{pts(c['score_high'])} vs {pts(c['score_low'])}"
            if cls == "C":
                d.text((x0, y + 6), f"{values}  (not a discrepancy: {c['kind'].lower()})", fill=MUTED, font=font(13, mono=True))
            else:
                bw = max(4, int((x1 - x0) * min(c["delta"], scale_max) / scale_max))
                d.rectangle((x0, y + 6, x0 + bw, y + row_h - 6), fill=CLASS_COL[cls])
                d.text((x0 + bw + 10, y + 6), f"{pts(c['delta'])} pts  ({values})", fill=TXT, font=font(13, mono=True))
            y += row_h
        y += 8
    d.text((40, H - 40), "Bar length proportional to the difference in percentage points (0-20 scale). "
           "Class C rows are context only: no bar, excluded from every statistic.", fill=MUTED, font=font(12, bold=True))
    im.save(SYNTH_DIR / "fig01_verified_discrepancies_by_class.png", optimize=True)


def fig_same_quantity(catalog):
    """Dot plot: for each case, the two published values on a common axis, coloured by class."""
    cases = [c for c in catalog["cases"] if c["class"] in ("A", "B")]
    W, row_h = 1600, 34
    H = 140 + row_h * len(cases) + 80
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    header(d, W, "FIG 2: THE SAME QUANTITY, TWO PUBLISHED NUMBERS",
           "Class A and B cases: open circle = lower published value, filled circle = higher; scale 0-100%")
    x0, x1 = 620, 1540
    for t in range(0, 101, 10):
        x = x0 + (x1 - x0) * t / 100
        d.line((x, 110, x, H - 60), fill=(226, 232, 240))
        d.text((x - 8, H - 52), str(t), fill=MUTED, font=font(12))
    for i, c in enumerate(sorted(cases, key=lambda c: (c["class"], -c["delta"]))):
        y = 120 + i * row_h
        d.text((40, y), f"{c['case_id']}  {c['model']} | {c['benchmark']}"[:70], fill=TXT, font=font(13, bold=True))
        xl, xh = x0 + (x1 - x0) * c["score_low"] / 100, x0 + (x1 - x0) * c["score_high"] / 100
        col = CLASS_COL[c["class"]]
        d.line((xl, y + 9, xh, y + 9), fill=col, width=3)
        d.ellipse((xl - 7, y + 2, xl + 7, y + 16), outline=col, width=3, fill=CARD)
        d.ellipse((xh - 7, y + 2, xh + 7, y + 16), fill=col)
    im.save(SYNTH_DIR / "fig02_same_quantity_two_numbers.png", optimize=True)


def _word_boxes(source_id: str, page: int):
    xml = subprocess.run(["pdftotext", "-bbox", "-f", str(page), "-l", str(page), str(evidence.source_path(source_id)), "-"],
                         capture_output=True, text=True, check=True).stdout
    return [(float(a), float(b), float(c), float(e), html_unescape(w)) for a, b, c, e, w in
            re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', xml)]


def html_unescape(s):
    import html
    return html.unescape(s)


def crop_pdf_region(source_id, page, top_words, bottom_words, x_range, dpi=170, pad=6, pad_bottom=1.5):
    """Render `page` and crop the band from the first word sequence `top_words` to `bottom_words` within x_range (pt)."""
    boxes = _word_boxes(source_id, page)

    def find(seq):
        for i in range(len(boxes) - len(seq) + 1):
            if all(boxes[i + k][4] == seq[k] for k in range(len(seq))) and x_range[0] <= boxes[i][0] <= x_range[1]:
                return boxes[i:i + len(seq)]
        raise AssertionError(f"{source_id} p{page}: words {seq} not found in x-range {x_range}")
    top, bottom = find(top_words), find(bottom_words)
    y0, y1 = min(b[1] for b in top) - pad, max(b[3] for b in bottom) + pad_bottom
    out = Path("/tmp") / f"seriously_models_crop_{source_id}_{page}"
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi), "-png", "-singlefile",
                    str(evidence.source_path(source_id)), str(out)], check=True)
    im = Image.open(f"{out}.png")
    s = dpi / 72.0
    crop = im.crop((int((x_range[0] - pad) * s), int(y0 * s), int((x_range[1] + pad) * s), int(y1 * s)))
    Path(f"{out}.png").unlink()
    return crop


def fig_proof_plate(catalog):
    W, H = 1600, 1500
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    header(d, W, "FIG 3: PRIMARY-SOURCE CROPS FOR CASES A1, A2-A4 AND B7",
           "Rendered from the SHA-256-pinned PDFs at build time (scripts/build_forensic_analysis.py); physical PDF page numbers")
    panels = [
        ("A1  Meta LLaMA-1 TR, Table 7 (PDF p.6): the Minerva 540B row prints 68.5 in the GSM8k column",
         crop_pdf_region("arxiv_2302.13971", 6, ["MATH", "+maj1@k"], ["Table", "7:"], (60, 300))),
        ("A1  Google Minerva TR, Table 3 (PDF p.8): Minerva 540B GSM8k 58.8; Minerva 62B maj1@k GSM8k 68.5",
         crop_pdf_region("arxiv_2206.14858", 8, ["Table", "3:"], ["Published", "SOTA"], (60, 545))),
        ("A2-A4  Mistral AI, Mistral 7B TR, Table 2 (PDF p.4)",
         crop_pdf_region("arxiv_2310.06825", 4, ["Model", "Modality"], ["Table", "2:"], (100, 515))),
        ("A2-A4  Mistral AI, Mixtral TR, Table 2 (PDF p.4): same models, same declared protocols",
         crop_pdf_region("arxiv_2401.04088", 4, ["Model", "Active"], ["Table", "2:"], (100, 515))),
        ("B7  Google Gemini 1.0 TR, Table 2 (PDF p.8): MMLU and GSM8K rows",
         crop_pdf_region("arxiv_2312.11805", 8, ["Gemini", "Ultra"], ["GSM8K", "94.4%"], (55, 560))),
    ]
    y = 105
    for title, crop in panels:
        crop.thumbnail((W - 80, 250), Image.Resampling.LANCZOS)
        d.text((40, y), title, fill=TXT, font=font(15, bold=True))
        im.paste(crop, (40, y + 26))
        d.rectangle((40, y + 26, 40 + crop.width, y + 26 + crop.height), outline=BORDER, width=1)
        y += 26 + crop.height + 22
    im = im.crop((0, 0, W, min(H, y + 10)))
    im.save(SYNTH_DIR / "fig03_primary_source_crops.png", optimize=True)


def main():
    SYNTH_DIR.mkdir(parents=True, exist_ok=True)
    catalog = build_catalog()
    (DATA_DIR / "inconsistencies_catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n")
    with (DATA_DIR / "inconsistencies_catalog.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["case_id", "class", "kind", "model", "benchmark", "score_high", "protocol_high", "source_high",
                    "claim_high", "score_low", "protocol_low", "source_low", "claim_low", "delta_pts", "finding"])
        for c in catalog["cases"]:
            w.writerow([c["case_id"], c["class"], c["kind"], c["model"], c["benchmark"], c["score_high"], c["protocol_high"],
                        c["source_high"], c["high"], c["score_low"], c["protocol_low"], c["source_low"], c["low"],
                        c["delta"], c["finding"]])
    own = {"fig01_verified_discrepancies_by_class.png", "fig02_same_quantity_two_numbers.png",
           "fig03_primary_source_crops.png", "fig04_highest_published_value_by_benchmark.png"}
    for old in SYNTH_DIR.glob("fig0*_*.png"):
        if old.name not in own:
            old.unlink()
    fig_catalog(catalog)
    fig_same_quantity(catalog)
    fig_proof_plate(catalog)
    s = catalog["summary"]
    print(f"Catalog: A={s['A']['n']} (median {s['A']['median_delta_pts']} pts), B={s['B']['n']} "
          f"(median {s['B']['median_delta_pts']} pts), C={s['C']['n']}; "
          f"{catalog['claims_referenced']} claims referenced, all verified.")


if __name__ == "__main__":
    main()
