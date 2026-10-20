# Month-by-Month Dossier (2021-01 to 2026-10)

Generated from `data/monthly_benchmarks_2021_2026.json`. Each score links to its pinned source and cites the ledger claim that verifies it. A score's month is the model's release month as stated by a source or, if no source states it, the month of the reporting document.

## 2021-01

**January 2021.** 4 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-3 X-Large (few-shot) [davinci, 175B] | MMLU | few-shot, up to 5 demonstration examples (5 fixed dev examples per subject) | 43.9 | Hendrycks et al. (MMLU paper), Table 1 | [arxiv_2009.03300](https://arxiv.org/pdf/2009.03300v3) p.5 | `m2021.hendrycks-mmlu.gpt-3-x-large.mmlu.few-shot-5` |
| UnifiedQA (11B, T5 backbone) | MMLU | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 48.9 | Hendrycks et al. (MMLU paper), Table 1 | [arxiv_2009.03300](https://arxiv.org/pdf/2009.03300v3) p.5 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |
| davinci (175B) | GSM8K | EM, 5 in-context examples (# train = 5), mean over 3 trials | 9.0 | Stanford CRFM HELM classic v0.3.0 | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2021.helm-v0.3.0.davinci-175b.gsm8k.em-5-in-context` |
| davinci (175B) | MMLU (HELM 5-subject subset) | EM, 5 in-context examples (# train = 5), mean over trials; MMLU = 5 subjects only | 42.2 | Stanford CRFM HELM classic v0.3.0 | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2021.helm-v0.3.0.davinci-175b.mmlu.em-5-in-context` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |

## 2021-02

**February 2021.** No verified score is dated to this month.

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |

## 2021-03

**March 2021.** 5 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | MATH | pretrained on AMPS, then fine-tuned on MATH | 6.9 | Hendrycks et al. (MATH paper), Table 2 | [arxiv_2103.03874](https://arxiv.org/pdf/2103.03874v2) p.5 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |
| GPT-3 175B* (few-shot) | MATH | few-shot, 8 problems with final answers prepended, temperature 0; no AMPS pretraining | 5.2 | Hendrycks et al. (MATH paper), Table 2 | [arxiv_2103.03874](https://arxiv.org/pdf/2103.03874v2) p.5 | `m2021.hendrycks-math.gpt-3-175b.math.few-shot-8` |
| GPT-Neo 1.3B | HumanEval | pass@1 (0-shot docstring prompt, unbiased estimator over sampled completions, temperature chosen per k) | 4.79 | Chen et al. (Codex paper), Table 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.7 | `m2021.chen-codex.gpt-neo-1.3b.humaneval.pass-at-1` |
| GPT-Neo 2.7B | HumanEval | pass@1 (0-shot docstring prompt, unbiased estimator over sampled completions, temperature chosen per k) | 6.41 | Chen et al. (Codex paper), Table 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.7 | `m2021.chen-codex.gpt-neo-2.7b.humaneval.pass-at-1` |
| GPT-Neo 2.7B | HumanEval | pass@100 (0-shot docstring prompt, unbiased estimator over sampled completions, temperature chosen per k) | 21.37 | Chen et al. (Codex paper), Table 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.7 | `m2021.chen-codex.gpt-neo-2.7b.humaneval.pass-at-100` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Measuring Mathematical Problem Solving With the MATH Dataset, v2, PDF page 5](https://arxiv.org/pdf/2103.03874v2#page=5): Table 2: MATH accuracies across subjects.

## 2021-04

**April 2021.** No verified score is dated to this month.

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |

## 2021-05

**May 2021.** No verified score is dated to this month.

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |

## 2021-06

**June 2021.** 3 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-J (6B) | MMLU (HELM 5-subject subset) | EM, 5 in-context examples (# train = 5), mean over trials; MMLU = 5 subjects only | 24.9 | Stanford CRFM HELM classic v0.3.0 | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2021.helm-v0.3.0.gpt-j-6b.mmlu.em-5-in-context` |
| GPT-J 6B | HumanEval | pass@1 (0-shot docstring prompt, unbiased estimator over sampled completions, temperature chosen per k) | 11.62 | Chen et al. (Codex paper), Table 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.7 | `m2021.chen-codex.gpt-j-6b.humaneval.pass-at-1` |
| GPT-J 6B | HumanEval | pass@100 (0-shot docstring prompt, unbiased estimator over sampled completions, temperature chosen per k) | 27.74 | Chen et al. (Codex paper), Table 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.7 | `m2021.chen-codex.gpt-j-6b.humaneval.pass-at-100` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |

## 2021-07

**July 2021.** 5 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Codex-12B | HumanEval | pass@1 (0-shot docstring prompt, unbiased estimator over sampled completions, temperature chosen per k) | 28.81 | Chen et al. (Codex paper), Table 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.7 | `m2021.chen-codex.codex-12b.humaneval.pass-at-1` |
| Codex-12B | HumanEval | pass@100 (0-shot docstring prompt, unbiased estimator over sampled completions, temperature chosen per k) | 72.31 | Chen et al. (Codex paper), Table 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.7 | `m2021.chen-codex.codex-12b.humaneval.pass-at-100` |
| Codex-S | HumanEval | single sample (pass@1) | 37.7 | Chen et al. (Codex paper), Section 1 / Figure 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.2 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| Codex-S | HumanEval | at least one correct in 100 samples (pass@100-style oracle) | 77.5 | Chen et al. (Codex paper), Section 1 | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.2 | `m2021.chen-codex.codex-s.humaneval.oracle-100-samples` |
| GPT-3 (size not stated) | HumanEval | single sample, abstract | 0.0 | Chen et al. (Codex paper), abstract | [arxiv_2107.03374](https://arxiv.org/pdf/2107.03374v2) p.1 | `m2021.chen-codex.gpt-3.humaneval.abstract` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Evaluating Large Language Models Trained on Code, v2, PDF page 7](https://arxiv.org/pdf/2107.03374v2#page=7): Table 1: Codex, GPT-Neo, & TabNine evaluations for HumanEval.

## 2021-08

**August 2021.** 2 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| J1-Jumbo v1 (178B) | GSM8K | EM, 5 in-context examples (# train = 5), mean over 3 trials | 5.4 | Stanford CRFM HELM classic v0.3.0 | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2021.helm-v0.3.0.j1-jumbo-v1-178b.gsm8k.em-5-in-context` |
| J1-Jumbo v1 (178B) | MMLU (HELM 5-subject subset) | EM, 5 in-context examples (# train = 5), mean over trials; MMLU = 5 subjects only | 25.9 | Stanford CRFM HELM classic v0.3.0 | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2021.helm-v0.3.0.j1-jumbo-v1-178b.mmlu.em-5-in-context` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |

## 2021-09

**September 2021.** No verified score is dated to this month.

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |

## 2021-10

**October 2021.** 4 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-3 175B finetuned plus an additional 175B verifier | GSM8K | fine-tuned generator + 175B verifier reranking | 55.0 | Wang et al. (Self-Consistency, arXiv 2203.11171v4), Table 2 | [arxiv_2203.11171](https://arxiv.org/pdf/2203.11171v4) p.5 | `m2021.wang-selfconsistency.gpt-3-175b-ft-verifier.gsm8k.verifier` |
| GPT-3 175B finetuned with 7.5k examples | GSM8K | fine-tuned on the 7.5k GSM8K training set (single sample) | 35.0 | Wang et al. (Self-Consistency, arXiv 2203.11171v4), Table 2 | [arxiv_2203.11171](https://arxiv.org/pdf/2203.11171v4) p.5 | `m2021.wang-selfconsistency.gpt-3-175b-ft.gsm8k.finetuned-7.5k` |
| TNLG v2 (530B) | GSM8K | EM, 5 in-context examples (# train = 5), mean over 3 trials | 14.6 | Stanford CRFM HELM classic v0.3.0 | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2021.helm-v0.3.0.tnlg-v2-530b.gsm8k.em-5-in-context` |
| TNLG v2 (530B) | MMLU (HELM 5-subject subset) | EM, 5 in-context examples (# train = 5), mean over trials; MMLU = 5 subjects only | 46.9 | Stanford CRFM HELM classic v0.3.0 | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2021.helm-v0.3.0.tnlg-v2-530b.mmlu.em-5-in-context` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Training Verifiers to Solve Math Word Problems, v2, PDF page 8](https://arxiv.org/pdf/2110.14168v2#page=8): Figure 5: A comparison between finetuning and verification using 6B and 175B.

## 2021-11

**November 2021.** No verified score is dated to this month.

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 48.9 | UnifiedQA (11B, T5 backbone) | no further tuning on MMLU (transfer from QA fine-tuning); not few-shot | 2021-01 | `m2021.hendrycks-mmlu.unifiedqa-11b.mmlu.transfer-no-further-tuning` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| MATH | 6.9 | GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | pretrained on AMPS, then fine-tuned on MATH | 2021-11 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |

## 2021-12

**December 2021.** 2 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Gopher (280B) | MMLU | 5-shot | 60.0 | Rae et al. (Gopher), Table 5 | [arxiv_2112.11446](https://arxiv.org/pdf/2112.11446v2) p.11 | `m2021.gopher.gopher-280b.mmlu.5-shot` |
| Gopher (5-shot) 280B | MMLU mathematics subset (5 subjects) | 5-shot | 30.6 | Taylor et al. (Galactica), Table 8 | [arxiv_2211.09085](https://arxiv.org/pdf/2211.09085v1) p.15 | `m2021.galactica.gopher-280b.mmlu-math-subset.5-shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 60.0 | Gopher (280B) | 5-shot | 2021-12 | `m2021.gopher.gopher-280b.mmlu.5-shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| MATH | 6.9 | GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | pretrained on AMPS, then fine-tuned on MATH | 2021-11 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Scaling Language Models: Methods, Analysis &amp; Insights from Training Gopher, v2, PDF page 11](https://arxiv.org/pdf/2112.11446v2#page=11): Table 5: Massive Multitask Language Understanding (MMLU).

## 2022-01

**January 2022.** 15 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| code-davinci-002 | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 56.8 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.code-davinci-002.gsm8k` |
| code-davinci-002 | GSM8K | HELM v0.1.0 (paper text) | 52.1 | Liang et al. (Stanford CRFM), HELM arXiv:2211.09110v2 Sec 1.1 | [arxiv_2211.09110](https://arxiv.org/pdf/2211.09110v2) p.8 | `m2022.helmpaper.code-davinci-002.gsm8k` |
| code-davinci-002 | GSM8K | 8-shot chain-of-thought, greedy | 63.1 | Wei et al. (Google), arXiv:2201.11903v6 Table 1 | [arxiv_2201.11903](https://arxiv.org/pdf/2201.11903v6) p.20 | `m2022.wei.code-davinci-002.gsm8k.8shot-cot` |
| code-davinci-002 | GSM8K | 8-shot standard prompting, greedy | 19.7 | Wei et al. (Google), arXiv:2201.11903v6 Table 1 | [arxiv_2201.11903](https://arxiv.org/pdf/2201.11903v6) p.20 | `m2022.wei.code-davinci-002.gsm8k.8shot-standard` |
| code-davinci-002 | HumanEval | 0-shot pass@1 (unbiased estimator over n samples) on HumanEval with the example input-output cases removed from the prompts | 47.0 | Chen et al. (Microsoft), CodeT, arXiv:2207.10397v2 Table 2 | [arxiv_2207.10397](https://arxiv.org/pdf/2207.10397v2) p.5 | `m2022.codet.code-davinci-002.humaneval.pass1-baseline` |
| code-davinci-002 | HumanEval | HELM v0.3.0 pass@1 | 46.3 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_code_humaneval](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/code_humaneval.json) json | `m2022.helm.code-davinci-002.humaneval` |
| code-davinci-002 | MMLU | 5-shot CoT, validation set (Chung et al. Table 16) | 64.5 | Chung et al. (Google), arXiv:2210.11416v5 Table 16 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.40 | `m2022.flan.code-davinci-002.mmlu.5shot-cot-val` |
| code-davinci-002 | MMLU | 5-shot direct, validation set (Chung et al. Table 16) | 68.2 | Chung et al. (Google), arXiv:2210.11416v5 Table 16 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.40 | `m2022.flan.code-davinci-002.mmlu.5shot-direct-val` |
| text-davinci-002 | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 41.5 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.text-davinci-002.gsm8k` |
| text-davinci-002 | GSM8K | HELM v0.1.0 (paper text) | 35.0 | Liang et al. (Stanford CRFM), HELM arXiv:2211.09110v2 Sec 1.1 | [arxiv_2211.09110](https://arxiv.org/pdf/2211.09110v2) p.8 | `m2022.helmpaper.text-davinci-002.gsm8k` |
| text-davinci-002 | GSM8K | 8-shot chain-of-thought, greedy | 46.9 | Wei et al. (Google), arXiv:2201.11903v6 Table 1 | [arxiv_2201.11903](https://arxiv.org/pdf/2201.11903v6) p.20 | `m2022.wei.text-davinci-002.gsm8k.8shot-cot` |
| text-davinci-002 | GSM8K | 8-shot standard prompting, greedy | 15.6 | Wei et al. (Google), arXiv:2201.11903v6 Table 1 | [arxiv_2201.11903](https://arxiv.org/pdf/2201.11903v6) p.20 | `m2022.wei.text-davinci-002.gsm8k.8shot-standard` |
| text-davinci-002 | MMLU | 5-shot direct, validation set (Chung et al. Table 16) | 63.1 | Chung et al. (Google), arXiv:2210.11416v5 Table 16 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.40 | `m2022.flan.text-davinci-002.mmlu.5shot-direct-val` |
| text-davinci-002 | MMLU (HELM 5-subject subset) | HELM v0.3.0 EM, 5-shot | 56.8 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2022.helm.text-davinci-002.mmlu` |
| text-davinci-002 | MMLU (HELM 5-subject subset) | HELM v0.1.0 (paper text) | 57.0 | Liang et al. (Stanford CRFM), HELM arXiv:2211.09110v2 Sec 8 | [arxiv_2211.09110](https://arxiv.org/pdf/2211.09110v2) p.68 | `m2022.helmpaper.text-davinci-002.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 60.0 | Gopher (280B) | 5-shot | 2021-12 | `m2021.gopher.gopher-280b.mmlu.5-shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| MATH | 6.9 | GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | pretrained on AMPS, then fine-tuned on MATH | 2021-11 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, v6, PDF page 20](https://arxiv.org/pdf/2201.11903v6#page=20): Table 1: Chain of thought prompting outperforms standard prompting for various large language.
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, v6, PDF page 5](https://arxiv.org/pdf/2201.11903v6#page=5): Figure 4: Chain-of-thought prompting enables.

## 2022-02

**February 2022.** 3 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-NeoX-20B | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 5.3 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.gpt-neox-20b.gsm8k` |
| GPT-NeoX-20B | HumanEval | pass@1 (BLOOM Table 9, quoted from prior work) | 15.4 | BigScience, arXiv:2211.05100v4 Table 9 | [arxiv_2211.05100](https://arxiv.org/pdf/2211.05100v4) p.34 | `m2022.bloom.gpt-neox-20b.humaneval.pass1` |
| GPT-NeoX-20B | MMLU (HELM 5-subject subset) | HELM v0.3.0 EM, 5-shot | 27.6 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2022.helm.gpt-neox-20b.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 60.0 | Gopher (280B) | 5-shot | 2021-12 | `m2021.gopher.gopher-280b.mmlu.5-shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| MATH | 6.9 | GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | pretrained on AMPS, then fine-tuned on MATH | 2021-11 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |

## 2022-03

**March 2022.** 5 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Chinchilla 70B | MMLU | 5-shot, 57-task average | 67.6 | Hoffmann et al. (DeepMind), arXiv:2203.15556v1 Table 6 | [arxiv_2203.15556](https://arxiv.org/pdf/2203.15556v1) p.11 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| Chinchilla 70B | MMLU | abstract figure, protocol not stated | 67.5 | Hoffmann et al. (DeepMind), arXiv:2203.15556v1 abstract | [arxiv_2203.15556](https://arxiv.org/pdf/2203.15556v1) p.1 | `m2022.chinchilla.chinchilla-70b.mmlu.abstract` |
| Chinchilla 70B | MMLU Mathematics subset (5 subjects) | 5-shot (Galactica Table 8) | 35.7 | Taylor et al. (Meta), arXiv:2211.09085v1 Table 8 | [arxiv_2211.09085](https://arxiv.org/pdf/2211.09085v1) p.15 | `m2022.galactica.chinchilla.mmlu-math.5shot` |
| code-davinci-002 | GSM8K | few-shot CoT, greedy (Wang et al.) | 60.1 | Wang et al. (Google), arXiv:2203.11171v4 Table 2 | [arxiv_2203.11171](https://arxiv.org/pdf/2203.11171v4) p.5 | `m2022.wang.code-davinci-002.gsm8k.cot-greedy` |
| code-davinci-002 | GSM8K | few-shot CoT, self-consistency 40 samples (Wang et al.) | 78.0 | Wang et al. (Google), arXiv:2203.11171v4 Table 2 | [arxiv_2203.11171](https://arxiv.org/pdf/2203.11171v4) p.5 | `m2022.wang.code-davinci-002.gsm8k.sc-40` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 67.6 | Chinchilla 70B | 5-shot, 57-task average | 2022-03 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| MATH | 6.9 | GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | pretrained on AMPS, then fine-tuned on MATH | 2021-11 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Self-Consistency Improves Chain of Thought Reasoning in Language Models, v4, PDF page 5](https://arxiv.org/pdf/2203.11171v4#page=5): Table 2: Arithmetic reasoning accuracy by self-consistency compared to chain-of-thought prompting.; Table 3: Commonsense and symbolic reasoning accuracy by self-consistency compared to chain-.
- [Training Compute-Optimal Large Language Models, v1, PDF page 11](https://arxiv.org/pdf/2203.15556v1#page=11): Table 6: Massive Multitask Language Understanding (MMLU).
- [Training Compute-Optimal Large Language Models, v1, PDF page 12](https://arxiv.org/pdf/2203.15556v1#page=12): Figure 6: MMLU results compared to Gopher We find that Chinchilla outperforms Gopher by 7.6%.; Table 7: Reading comprehension.

## 2022-04

**April 2022.** 15 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Anthropic-LM v4-s3 (52B) | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 17.1 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.anthropic-lm-v4-s3-52b.gsm8k` |
| Anthropic-LM v4-s3 (52B) | MMLU (HELM 5-subject subset) | HELM v0.3.0 EM, 5-shot | 48.1 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2022.helm.anthropic-lm-v4-s3-52b.mmlu` |
| Anthropic-LM v4-s3 (52B) | MMLU (HELM 5-subject subset) | HELM v0.1.0 (paper text) | 49.8 | Liang et al. (Stanford CRFM), HELM arXiv:2211.09110v2 Sec 8 | [arxiv_2211.09110](https://arxiv.org/pdf/2211.09110v2) p.68 | `m2022.helmpaper.anthropic-lm-52b.mmlu` |
| PaLM 540B | GSM8K | 8-shot CoT, no calculator (PaLM paper) | 54.0 | Chowdhery et al. (Google), arXiv:2204.02311v5 Table 10 | [arxiv_2204.02311](https://arxiv.org/pdf/2204.02311v5) p.21 | `m2022.palm.palm-540b.gsm8k.8shot-cot` |
| PaLM 540B | GSM8K | 8-shot CoT + external calculator (PaLM paper) | 58.0 | Chowdhery et al. (Google), arXiv:2204.02311v5 Table 10 | [arxiv_2204.02311](https://arxiv.org/pdf/2204.02311v5) p.21 | `m2022.palm.palm-540b.gsm8k.8shot-cot-calc` |
| PaLM 540B | GSM8K | few-shot CoT, greedy (Wang et al.) | 56.5 | Wang et al. (Google), arXiv:2203.11171v4 Table 2 | [arxiv_2203.11171](https://arxiv.org/pdf/2203.11171v4) p.5 | `m2022.wang.palm-540b.gsm8k.cot-greedy` |
| PaLM 540B | GSM8K | few-shot CoT, self-consistency 40 samples (Wang et al.) | 74.4 | Wang et al. (Google), arXiv:2203.11171v4 Table 2 | [arxiv_2203.11171](https://arxiv.org/pdf/2203.11171v4) p.5 | `m2022.wang.palm-540b.gsm8k.sc-40` |
| PaLM 540B | GSM8K | 8-shot CoT, greedy (Wei et al.) | 56.9 | Wei et al. (Google), arXiv:2201.11903v6 Table 1 | [arxiv_2201.11903](https://arxiv.org/pdf/2201.11903v6) p.20 | `m2022.wei.palm-540b.gsm8k.8shot-cot` |
| PaLM 540B | HumanEval | 0-shot pass@1 | 26.2 | Chowdhery et al. (Google), arXiv:2204.02311v5 Table 12 | [arxiv_2204.02311](https://arxiv.org/pdf/2204.02311v5) p.25 | `m2022.palm.palm-540b.humaneval.0shot-pass1` |
| PaLM 540B | MATH | fixed 4-shot prompt (Minerva Table 3) | 8.8 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.palm-540b.math.4shot` |
| PaLM 540B | MMLU | 5-shot CoT, test set (Chung et al. Table 4) | 64.5 | Chung et al. (Google), arXiv:2210.11416v5 Table 4 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.8 | `m2022.flan.palm-540b.mmlu.5shot-cot-test` |
| PaLM 540B | MMLU | 5-shot, test set | 69.3 | Chowdhery et al. (Google), arXiv:2204.02311v5 Table 6 | [arxiv_2204.02311](https://arxiv.org/pdf/2204.02311v5) p.13 | `m2022.palm.palm-540b.mmlu.5shot` |
| PaLM 540B | MMLU-STEM | standard 5-shot (Minerva Table 3) | 58.7 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.palm-540b.mmlu-stem.5shot` |
| PaLM-Coder 540B | HumanEval | 0-shot pass@1 | 36.0 | Chowdhery et al. (Google), arXiv:2204.02311v5 Table 12 | [arxiv_2204.02311](https://arxiv.org/pdf/2204.02311v5) p.25 | `m2022.palm.palm-coder-540b.humaneval.0shot-pass1` |
| code-davinci-001 (Davinci Codex) | HumanEval | 0-shot pass@1, Google's API measurement | 36.0 | Chowdhery et al. (Google), arXiv:2204.02311v5 Table 12 | [arxiv_2204.02311](https://arxiv.org/pdf/2204.02311v5) p.25 | `m2022.palm.code-davinci-001.humaneval.0shot-pass1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 67.6 | Chinchilla 70B | 5-shot, 57-task average | 2022-03 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| GSM8K | 58.0 | PaLM 540B | 8-shot CoT + external calculator (PaLM paper) | 2022-04 | `m2022.palm.palm-540b.gsm8k.8shot-cot-calc` |
| MATH | 6.9 | GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | pretrained on AMPS, then fine-tuned on MATH | 2021-11 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [PaLM: Scaling Language Modeling with Pathways, v5, PDF page 22](https://arxiv.org/pdf/2204.02311v5#page=22): Figure 10: Via chain of thought prompting, PaLM achieves strong performance on a range of arithmetic and.
- [PaLM: Scaling Language Modeling with Pathways, v5, PDF page 23](https://arxiv.org/pdf/2204.02311v5#page=23): Figure 11: Examples from the PaLM-Coder 540B model.
- [PaLM: Scaling Language Modeling with Pathways, v5, PDF page 25](https://arxiv.org/pdf/2204.02311v5#page=25): Table 12: Results obtained by the PaLM 540B and PaLM-Coder 540B models across code synthesis and.; Figure 12: Scaling results for HumanEval, MBPP, GSM8K-Python, TransCoder, and DeepFix datasets on.

## 2022-05

**May 2022.** 4 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| OPT-175B | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 4.0 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.opt-175b.gsm8k` |
| OPT-175B | MMLU | 0-shot, test set (OPT-IML Table 14) | 27.3 | Iyer et al. (Meta), OPT-IML, arXiv:2212.12017v3 Table 14 | [arxiv_2212.12017](https://arxiv.org/pdf/2212.12017v3) p.21 | `m2022.optiml.opt-175b.mmlu.0shot` |
| OPT-175B | MMLU | 5-shot, test set (OPT-IML Table 14) | 34.2 | Iyer et al. (Meta), OPT-IML, arXiv:2212.12017v3 Table 14 | [arxiv_2212.12017](https://arxiv.org/pdf/2212.12017v3) p.21 | `m2022.optiml.opt-175b.mmlu.5shot` |
| OPT-175B | MMLU (HELM 5-subject subset) | HELM v0.3.0 EM, 5-shot | 31.8 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2022.helm.opt-175b.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 67.6 | Chinchilla 70B | 5-shot, 57-task average | 2022-03 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| GSM8K | 58.0 | PaLM 540B | 8-shot CoT + external calculator (PaLM paper) | 2022-04 | `m2022.palm.palm-540b.gsm8k.8shot-cot-calc` |
| MATH | 6.9 | GPT-2 1.5B (AMPS-pretrained, MATH fine-tuned) | pretrained on AMPS, then fine-tuned on MATH | 2021-11 | `m2021.hendrycks-math.gpt-2-1.5b.math.amps-pretrain-math-ft` |

## 2022-06

**June 2022.** 8 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Minerva 540B | GSM8K | Wei et al. CoT prompt, no majority vote | 58.8 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.minerva-540b.gsm8k.cot` |
| Minerva 540B | GSM8K | Wei et al. CoT prompt, maj1@40 | 78.5 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.minerva-540b.gsm8k.maj1at40` |
| Minerva 540B | MATH | fixed 4-shot, no majority vote | 33.6 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.minerva-540b.math.4shot` |
| Minerva 540B | MATH | fixed 4-shot, maj1@64 | 50.3 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.minerva-540b.math.maj1at64` |
| Minerva 540B | MMLU-STEM | standard 5-shot, highest-scoring answer | 63.9 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.minerva-540b.mmlu-stem.5shot` |
| Minerva 540B | MMLU-STEM | CoT prompt, maj1@16 | 75.0 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.minerva-540b.mmlu-stem.maj1at16` |
| Minerva 62B | GSM8K | Wei et al. CoT prompt, maj1@100 | 68.5 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.minerva-62b.gsm8k.maj1at100` |
| OpenAI davinci-002 (variant unstated) | MATH | fixed 4-shot, T = 0.2 (Minerva evaluation) | 19.1 | Lewkowycz et al. (Google), arXiv:2206.14858v2 Table 3 | [arxiv_2206.14858](https://arxiv.org/pdf/2206.14858v2) p.8 | `m2022.minerva.openai-davinci-002.math` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 67.6 | Chinchilla 70B | 5-shot, 57-task average | 2022-03 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| GSM8K | 78.5 | Minerva 540B | Wei et al. CoT prompt, maj1@40 | 2022-06 | `m2022.minerva.minerva-540b.gsm8k.maj1at40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Solving Quantitative Reasoning Problems with Language Models, v2, PDF page 7](https://arxiv.org/pdf/2206.14858v2#page=7): Figure 4: Performance on MATH and MMLU-STEM by subtopic.
- [Solving Quantitative Reasoning Problems with Language Models, v2, PDF page 8](https://arxiv.org/pdf/2206.14858v2#page=8): Table 3: Model performance on several quantitative reasoning datasets.

## 2022-07

**July 2022.** 4 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| BLOOM 176B | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 9.5 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.bloom-176b.gsm8k` |
| BLOOM 176B | HumanEval | pass@1 | 15.52 | BigScience, arXiv:2211.05100v4 Table 9 | [arxiv_2211.05100](https://arxiv.org/pdf/2211.05100v4) p.34 | `m2022.bloom.bloom-176b.humaneval.pass1` |
| BLOOM 176B | HumanEval | pass@100 | 55.45 | BigScience, arXiv:2211.05100v4 Table 9 | [arxiv_2211.05100](https://arxiv.org/pdf/2211.05100v4) p.34 | `m2022.bloom.bloom-176b.humaneval.pass100` |
| BLOOM 176B | MMLU (HELM 5-subject subset) | HELM v0.3.0 EM, 5-shot | 29.9 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2022.helm.bloom-176b.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 67.6 | Chinchilla 70B | 5-shot, 57-task average | 2022-03 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| GSM8K | 78.5 | Minerva 540B | Wei et al. CoT prompt, maj1@40 | 2022-06 | `m2022.minerva.minerva-540b.gsm8k.maj1at40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2022-08

**August 2022.** 3 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GLM-130B | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 6.1 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.glm-130b.gsm8k` |
| GLM-130B | MMLU | 5-shot, after 400B tokens | 44.8 | Zeng et al. (Tsinghua/Zhipu), arXiv:2210.02414v2 Sec 5.2 | [arxiv_2210.02414](https://arxiv.org/pdf/2210.02414v2) p.8 | `m2022.glm.glm-130b.mmlu.5shot` |
| GLM-130B | MMLU (HELM 5-subject subset) | HELM v0.3.0 EM, 5-shot | 34.4 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2022.helm.glm-130b.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 67.6 | Chinchilla 70B | 5-shot, 57-task average | 2022-03 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| GSM8K | 78.5 | Minerva 540B | Wei et al. CoT prompt, maj1@40 | 2022-06 | `m2022.minerva.minerva-540b.gsm8k.maj1at40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2022-09

**September 2022.** 1 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| code-davinci-002 + CodeT | HumanEval | 0-shot, CodeT reranking of 100 samples (T=0.8), pass@1, on HumanEval with example input-output cases removed from the prompts | 65.8 | Chen et al. (Microsoft), CodeT, arXiv:2207.10397v2 Table 2 | [arxiv_2207.10397](https://arxiv.org/pdf/2207.10397v2) p.5 | `m2022.codet.code-davinci-002+codet.humaneval.pass1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 67.6 | Chinchilla 70B | 5-shot, 57-task average | 2022-03 | `m2022.chinchilla.chinchilla-70b.mmlu.5shot` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| GSM8K | 78.5 | Minerva 540B | Wei et al. CoT prompt, maj1@40 | 2022-06 | `m2022.minerva.minerva-540b.gsm8k.maj1at40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2022-10

**October 2022.** 4 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Flan-PaLM 540B | GSM8K | CoT + self-consistency (train set held-in) | 83.9 | Chung et al. (Google), arXiv:2210.11416v5 Sec 4.1 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.7 | `m2022.flan.flan-palm-540b.gsm8k.cot-sc` |
| Flan-PaLM 540B | MMLU | 5-shot CoT + self-consistency, test set | 75.2 | Chung et al. (Google), arXiv:2210.11416v5 Table 4 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.8 | `m2022.flan.flan-palm-540b.mmlu.5shot-cot-sc-test` |
| Flan-PaLM 540B | MMLU | 5-shot direct, test set | 72.2 | Chung et al. (Google), arXiv:2210.11416v5 Table 4 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.8 | `m2022.flan.flan-palm-540b.mmlu.5shot-direct-test` |
| Flan-PaLM 540B | MMLU | 5-shot direct, validation set | 73.5 | Chung et al. (Google), arXiv:2210.11416v5 Table 5 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.11 | `m2022.flan.flan-palm-540b.mmlu.5shot-direct-val` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 75.2 | Flan-PaLM 540B | 5-shot CoT + self-consistency, test set | 2022-10 | `m2022.flan.flan-palm-540b.mmlu.5shot-cot-sc-test` |
| HumanEval | 37.7 | Codex-S | single sample (pass@1) | 2021-07 | `m2021.chen-codex.codex-s-12b.humaneval.pass-at-1` |
| GSM8K | 83.9 | Flan-PaLM 540B | CoT + self-consistency (train set held-in) | 2022-10 | `m2022.flan.flan-palm-540b.gsm8k.cot-sc` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [GLM-130B: An Open Bilingual Pre-trained Model, v2, PDF page 8](https://arxiv.org/pdf/2210.02414v2#page=8): Figure 6: GLM-130B on MMLU.; Figure 7: BIG-bench-lite evalua-.; Table 4: Details on BIG-.
- [Scaling Instruction-Finetuned Language Models, v5, PDF page 2](https://arxiv.org/pdf/2210.11416v5#page=2): Table 1: Average 5-shot MMLU scores (%) for 57 tasks with model and human accuracy comparisons.
- [Scaling Instruction-Finetuned Language Models, v5, PDF page 8](https://arxiv.org/pdf/2210.11416v5#page=8): Table 4: Flan-PaLM outperforms PaLM on all evaluation benchmarks.; Figure 5: Jointly finetuning on non-CoT and CoT data improves performance on both evaluations, compared.

## 2022-11

**November 2022.** 11 verified scores for 5 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-3.5 | GSM8K | 5-shot (CoT is stated only for the GPT-4 cell; not stated for GPT-3.5) | 57.1 | OpenAI, GPT-4 Technical Report arXiv:2303.08774v6 Table 2 | [arxiv_2303.08774](https://arxiv.org/pdf/2303.08774v6) p.7 | `m2022.gpt4tr.gpt-3.5.gsm8k.5shot` |
| GPT-3.5 (snapshot not named) | HumanEval | 0-shot | 48.1 | OpenAI, GPT-4 Technical Report arXiv:2303.08774v6 Table 2 | [arxiv_2303.08774](https://arxiv.org/pdf/2303.08774v6) p.7 | `m2022.gpt4tr.gpt-3.5.humaneval.0shot` |
| GPT-3.5 (snapshot not named) | MMLU | 5-shot | 70.0 | OpenAI, GPT-4 Technical Report arXiv:2303.08774v6 Table 2 | [arxiv_2303.08774](https://arxiv.org/pdf/2303.08774v6) p.7 | `m2022.gpt4tr.gpt-3.5.mmlu.5shot` |
| Galactica 120B | MATH | 5-shot mCoT | 20.4 | Taylor et al. (Meta), arXiv:2211.09085v1 Table 9 | [arxiv_2211.09085](https://arxiv.org/pdf/2211.09085v1) p.15 | `m2022.galactica.gal-120b.math.5shot-mcot` |
| Galactica 120B | MATH | <work> token prompt | 16.6 | Taylor et al. (Meta), arXiv:2211.09085v1 Table 9 | [arxiv_2211.09085](https://arxiv.org/pdf/2211.09085v1) p.15 | `m2022.galactica.gal-120b.math.work` |
| Galactica 120B | MMLU Mathematics subset (5 subjects) | <work> token, no few-shot examples | 41.3 | Taylor et al. (Meta), arXiv:2211.09085v1 Table 8 | [arxiv_2211.09085](https://arxiv.org/pdf/2211.09085v1) p.15 | `m2022.galactica.gal-120b.mmlu-math.work` |
| gpt-3.5-turbo | GSM8K | few-shot CoT (CoT Hub own run) | 74.9 | Fu et al., Chain-of-Thought Hub, arXiv:2305.17306v1 Table 1 | [arxiv_2305.17306](https://arxiv.org/pdf/2305.17306v1) p.3 | `m2022.cothub.gpt-3.5-turbo.gsm8k.fewshot-cot` |
| gpt-3.5-turbo | MMLU | few-shot CoT (CoT Hub own run) | 67.3 | Fu et al., Chain-of-Thought Hub, arXiv:2305.17306v1 Table 1 | [arxiv_2305.17306](https://arxiv.org/pdf/2305.17306v1) p.3 | `m2022.cothub.gpt-3.5-turbo.mmlu.fewshot-cot` |
| text-davinci-003 | GSM8K | HELM v0.3.0 EM, 5 in-context examples | 50.6 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_gsm](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/gsm.json) json | `m2022.helm.text-davinci-003.gsm8k` |
| text-davinci-003 | MMLU | 5-shot direct, validation set (Chung et al. Table 16) | 64.8 | Chung et al. (Google), arXiv:2210.11416v5 Table 16 | [arxiv_2210.11416](https://arxiv.org/pdf/2210.11416v5) p.40 | `m2022.flan.text-davinci-003.mmlu.5shot-direct-val` |
| text-davinci-003 | MMLU (HELM 5-subject subset) | HELM v0.3.0 EM, 5-shot | 56.9 | Stanford CRFM, HELM classic v0.3.0 results JSON | [helm_classic_v0.3.0_mmlu](https://storage.googleapis.com/crfm-helm-public/classic/benchmark_output/releases/v0.3.0/groups/mmlu.json) json | `m2022.helm.text-davinci-003.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 75.2 | Flan-PaLM 540B | 5-shot CoT + self-consistency, test set | 2022-10 | `m2022.flan.flan-palm-540b.mmlu.5shot-cot-sc-test` |
| HumanEval | 65.8 | code-davinci-002 + CodeT | 0-shot, CodeT reranking of 100 samples (T=0.8), pass@1, on HumanEval with example input-output cases removed from the prompts | 2022-11 | `m2022.codet.code-davinci-002+codet.humaneval.pass1` |
| GSM8K | 83.9 | Flan-PaLM 540B | CoT + self-consistency (train set held-in) | 2022-10 | `m2022.flan.flan-palm-540b.gsm8k.cot-sc` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Galactica: A Large Language Model for Science, v1, PDF page 15](https://arxiv.org/pdf/2211.09085v1#page=15): Table 8: Results on Mathematics MMLU. Galactica is evaluated without few-shot examples.; Table 9: Results on MATH. With both the chain-of-thought and <work> token prompts, Galactica exceeds.

## 2022-12

**December 2022.** 2 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| OPT-IML-Max 175B | MMLU | 0-shot, test set | 49.1 | Iyer et al. (Meta), OPT-IML, arXiv:2212.12017v3 Table 14 | [arxiv_2212.12017](https://arxiv.org/pdf/2212.12017v3) p.21 | `m2022.optiml.opt-iml-max-175b.mmlu.0shot` |
| OPT-IML-Max 175B | MMLU | 5-shot, test set | 47.1 | Iyer et al. (Meta), OPT-IML, arXiv:2212.12017v3 Table 14 | [arxiv_2212.12017](https://arxiv.org/pdf/2212.12017v3) p.21 | `m2022.optiml.opt-iml-max-175b.mmlu.5shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 75.2 | Flan-PaLM 540B | 5-shot CoT + self-consistency, test set | 2022-10 | `m2022.flan.flan-palm-540b.mmlu.5shot-cot-sc-test` |
| HumanEval | 65.8 | code-davinci-002 + CodeT | 0-shot, CodeT reranking of 100 samples (T=0.8), pass@1, on HumanEval with example input-output cases removed from the prompts | 2022-11 | `m2022.codet.code-davinci-002+codet.humaneval.pass1` |
| GSM8K | 83.9 | Flan-PaLM 540B | CoT + self-consistency (train set held-in) | 2022-10 | `m2022.flan.flan-palm-540b.gsm8k.cot-sc` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2023-01

**January 2023.** 1 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| SantaCoder 1.1B (final) | HumanEval (MultiPL-E, Python) | pass@100 | 49.0 | BigCode (Allal et al. 2023) | [arxiv_2301.03988](https://arxiv.org/pdf/2301.03988v1) p.10 | `m2023.allal2023.santacoder-1.1b.humaneval-python.pass100` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 75.2 | Flan-PaLM 540B | 5-shot CoT + self-consistency, test set | 2022-10 | `m2022.flan.flan-palm-540b.mmlu.5shot-cot-sc-test` |
| HumanEval | 65.8 | code-davinci-002 + CodeT | 0-shot, CodeT reranking of 100 samples (T=0.8), pass@1, on HumanEval with example input-output cases removed from the prompts | 2022-11 | `m2022.codet.code-davinci-002+codet.humaneval.pass1` |
| GSM8K | 83.9 | Flan-PaLM 540B | CoT + self-consistency (train set held-in) | 2022-10 | `m2022.flan.flan-palm-540b.gsm8k.cot-sc` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2023-02

**February 2023.** 8 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| LLaMA 65B | GSM8K | maj1@k, k=100 | 69.7 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.6 | `m2023.touvron2023a.llama-65b.gsm8k.maj1at100` |
| LLaMA 65B | GSM8K | without maj1@k (shot count not stated) | 50.9 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.6 | `m2023.touvron2023a.llama-65b.gsm8k.single` |
| LLaMA 65B | HumanEval | 0-shot pass@1 (T=0.1) | 23.7 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.6 | `m2023.touvron2023a.llama-65b.humaneval.0shot-pass1` |
| LLaMA 65B | HumanEval | 0-shot pass@100 (T=0.8) | 79.3 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.6 | `m2023.touvron2023a.llama-65b.humaneval.0shot-pass100` |
| LLaMA 65B | MATH | maj1@k, k=256 | 20.5 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.6 | `m2023.touvron2023a.llama-65b.math.maj1at256` |
| LLaMA 65B | MATH | without maj1@k (shot count not stated) | 10.6 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.6 | `m2023.touvron2023a.llama-65b.math.single` |
| LLaMA 65B | MMLU | 5-shot | 63.4 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.7 | `m2023.touvron2023a.llama-65b.mmlu.5shot` |
| LLaMA-I 65B | MMLU | 5-shot | 68.9 | Meta (Touvron et al. 2023a) | [arxiv_2302.13971](https://arxiv.org/pdf/2302.13971v1) p.7 | `m2023.touvron2023a.llama-i-65b.mmlu.5shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 75.2 | Flan-PaLM 540B | 5-shot CoT + self-consistency, test set | 2022-10 | `m2022.flan.flan-palm-540b.mmlu.5shot-cot-sc-test` |
| HumanEval | 65.8 | code-davinci-002 + CodeT | 0-shot, CodeT reranking of 100 samples (T=0.8), pass@1, on HumanEval with example input-output cases removed from the prompts | 2022-11 | `m2022.codet.code-davinci-002+codet.humaneval.pass1` |
| GSM8K | 83.9 | Flan-PaLM 540B | CoT + self-consistency (train set held-in) | 2022-10 | `m2022.flan.flan-palm-540b.gsm8k.cot-sc` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [LLaMA: Open and Efficient Foundation Language Models, v1, PDF page 6](https://arxiv.org/pdf/2302.13971v1#page=6): Table 7: Model performance on quantitative reason-.; Table 8: Model performance for code generation.
- [LLaMA: Open and Efficient Foundation Language Models, v1, PDF page 7](https://arxiv.org/pdf/2302.13971v1#page=7): Table 9: Massive Multitask Language Understanding (MMLU).; Table 10: Instruction finetuning - MMLU (5-shot).

## 2023-03

**March 2023.** 3 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-4 | GSM8K | 5-shot chain-of-thought (part of GSM8K train set in pre-training mix) | 92.0 | OpenAI (GPT-4 Technical Report) | [arxiv_2303.08774](https://arxiv.org/pdf/2303.08774v6) p.7 | `m2023.openai2023.gpt-4.gsm8k.5shot-cot` |
| GPT-4 | HumanEval | 0-shot | 67.0 | OpenAI (GPT-4 Technical Report) | [arxiv_2303.08774](https://arxiv.org/pdf/2303.08774v6) p.7 | `m2023.openai2023.gpt-4.humaneval.0shot` |
| GPT-4 | MMLU | 5-shot | 86.4 | OpenAI (GPT-4 Technical Report) | [arxiv_2303.08774](https://arxiv.org/pdf/2303.08774v6) p.7 | `m2023.openai2023.gpt-4.mmlu.5shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 67.0 | GPT-4 | 0-shot | 2023-03 | `m2023.openai2023.gpt-4.humaneval.0shot` |
| GSM8K | 92.0 | GPT-4 | 5-shot chain-of-thought (part of GSM8K train set in pre-training mix) | 2023-03 | `m2023.openai2023.gpt-4.gsm8k.5shot-cot` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [GPT-4 Technical Report, v6, PDF page 7](https://arxiv.org/pdf/2303.08774v6#page=7): Table 2: Performance of GPT-4 on academic benchmarks.

## 2023-04

**April 2023.** No verified score is dated to this month.

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 67.0 | GPT-4 | 0-shot | 2023-03 | `m2023.openai2023.gpt-4.humaneval.0shot` |
| GSM8K | 92.0 | GPT-4 | 5-shot chain-of-thought (part of GSM8K train set in pre-training mix) | 2023-03 | `m2023.openai2023.gpt-4.gsm8k.5shot-cot` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2023-05

**May 2023.** 12 verified scores for 7 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Flan-PaLM 2 | GSM8K | 8-shot CoT + self-consistency, 40 paths | 92.2 | Google (PaLM 2 TR, Table 7) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.15 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| Flan-PaLM 2 (L) | MMLU | 5-shot | 81.2 | Google (PaLM 2 TR, Table 16) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.44 | `m2023.anil2023.flan-palm-2-l.mmlu.5shot` |
| GPT-4 | GSM8K | as reported by OpenAI (SOTA column footnote b) | 92.0 | Google (PaLM 2 TR, Table 7) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.15 | `m2023.anil2023.gpt-4.gsm8k` |
| GPT-4 | HumanEval | pass@1 greedy | 88.4 | EvalPlus (Liu et al. 2023, v3) | [arxiv_2305.01210](https://arxiv.org/pdf/2305.01210v3) p.7 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GPT-4 | MATH | not stated for the GPT-4 column | 42.5 | Google (PaLM 2 TR, Table 7) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.15 | `m2023.anil2023.gpt-4.math.unstated` |
| PaLM 2 | GSM8K | 8-shot CoT without self-consistency (decoding not stated) | 80.7 | Google (PaLM 2 TR, Table 7) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.15 | `m2023.anil2023.palm-2.gsm8k.8shot-cot` |
| PaLM 2 | GSM8K | 8-shot CoT + self-consistency, 40 paths | 91.0 | Google (PaLM 2 TR, Table 7) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.15 | `m2023.anil2023.palm-2.gsm8k.8shot-cot-sc40` |
| PaLM 2 | MATH | 4-shot CoT without self-consistency (decoding not stated) | 34.3 | Google (PaLM 2 TR, Table 7) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.15 | `m2023.anil2023.palm-2.math.4shot-cot` |
| PaLM 2 | MATH | 4-shot CoT + self-consistency, 64 paths | 48.8 | Google (PaLM 2 TR, Table 7) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.15 | `m2023.anil2023.palm-2.math.4shot-cot-sc64` |
| PaLM 2 (L) | MMLU | 5-shot | 78.3 | Google (PaLM 2 TR, Table 16) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.44 | `m2023.anil2023.palm-2-l.mmlu.5shot` |
| PaLM 2-S* | HumanEval | pass@1, greedy (described as few-shot coding task; shot count not given) | 37.6 | Google (PaLM 2 TR, Table 8) | [arxiv_2305.10403](https://arxiv.org/pdf/2305.10403v3) p.16 | `m2023.anil2023.palm-2-s-star.humaneval.pass1-greedy` |
| SantaCoder 1.1B | HumanEval | pass@1 greedy | 14.6 | EvalPlus (Liu et al. 2023, v3) | [arxiv_2305.01210](https://arxiv.org/pdf/2305.01210v3) p.7 | `m2023.liu2023evalplus.santacoder-1.1b.humaneval.greedy` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 67.0 | GPT-4 | 0-shot | 2023-03 | `m2023.openai2023.gpt-4.humaneval.0shot` |
| GSM8K | 92.2 | Flan-PaLM 2 | 8-shot CoT + self-consistency, 40 paths | 2023-05 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [PaLM 2 Technical Report, v3, PDF page 15](https://arxiv.org/pdf/2305.10403v3#page=15): Table 7: Evaluation results on MATH, GSM8K, and MGSM with chain-of-thought prompting (Wei et al., 2022) /.

## 2023-06

**June 2023.** 4 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| StarCoder 15B | HumanEval | pass@1 | 33.6 | Microsoft (Luo et al. 2023), quoting StarCoder paper | [arxiv_2306.08568](https://arxiv.org/pdf/2306.08568v1) p.6 | `m2023.luo2023.starcoder-15b.humaneval.pass1` |
| Vicuna 13B | HumanEval | not stated in Table 5 | 15.2 | Chia et al. 2023 (INSTRUCTEVAL v1) | [arxiv_2306.04757](https://arxiv.org/pdf/2306.04757v1) p.6 | `m2023.chia2023.vicuna-13b.humaneval` |
| Vicuna 13B | MMLU | not stated in Table 5 | 49.7 | Chia et al. 2023 (INSTRUCTEVAL v1) | [arxiv_2306.04757](https://arxiv.org/pdf/2306.04757v1) p.6 | `m2023.chia2023.vicuna-13b.mmlu` |
| WizardCoder 15B | HumanEval | pass@1 (n samples, T=0.2, top_p=0.95) | 57.3 | Microsoft (Luo et al. 2023) | [arxiv_2306.08568](https://arxiv.org/pdf/2306.08568v1) p.6 | `m2023.luo2023.wizardcoder-15b.humaneval.pass1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 67.0 | GPT-4 | 0-shot | 2023-03 | `m2023.openai2023.gpt-4.humaneval.0shot` |
| GSM8K | 92.2 | Flan-PaLM 2 | 8-shot CoT + self-consistency, 40 paths | 2023-05 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2023-07

**July 2023.** 19 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude 1.3 | GSM8K | 0-shot CoT, T=1 | 85.2 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-1.3.gsm8k.0shot-cot` |
| Claude 1.3 | HumanEval (Codex P@1) | 0-shot pass@1, T=1 | 56.0 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-1.3.humaneval.0shot` |
| Claude 1.3 | MMLU | 5-shot CoT, T=1 | 77.0 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-1.3.mmlu.5shot-cot` |
| Claude 2 | GSM8K | 0-shot CoT, T=1 | 88.0 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-2.gsm8k.0shot-cot` |
| Claude 2 | GSM8K | 0-shot | 88.0 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.claude-2.gsm8k.0shot` |
| Claude 2 | HumanEval | 0-shot | 70.0 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.claude-2.humaneval.0shot` |
| Claude 2 | HumanEval (Codex P@1) | 0-shot pass@1, T=1 | 71.2 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-2.humaneval.0shot` |
| Claude 2 | MMLU | 5-shot CoT, T=1 | 78.5 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-2.mmlu.5shot-cot` |
| Claude 2 | MMLU | 5-shot CoT | 78.5 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.claude-2.mmlu.5shot-cot` |
| Claude Instant | GSM8K | 0-shot CoT, T=1 | 80.9 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-instant.gsm8k.0shot-cot` |
| Claude Instant | HumanEval (Codex P@1) | 0-shot pass@1, T=1 | 52.8 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-instant.humaneval.0shot` |
| Claude Instant | MMLU | 5-shot CoT, T=1 | 73.4 | Anthropic (Claude 2 model card) | [anthropic_claude2_card](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf) p.10 | `m2023.anthropic-claude2-card.claude-instant.mmlu.5shot-cot` |
| Llama 2 13B | MMLU | 5-shot | 54.8 | Meta (Touvron et al. 2023b, Table 19) | [arxiv_2307.09288](https://arxiv.org/pdf/2307.09288v2) p.49 | `m2023.touvron2023b.llama-2-13b.mmlu.5shot` |
| Llama 2 70B | GSM8K | 8-shot | 56.8 | Meta (Touvron et al. 2023b, Table 4) | [arxiv_2307.09288](https://arxiv.org/pdf/2307.09288v2) p.8 | `m2023.touvron2023b.llama-2-70b.gsm8k.8shot` |
| Llama 2 70B | HumanEval | 0-shot pass@1 | 29.9 | Meta (Touvron et al. 2023b, Table 4) | [arxiv_2307.09288](https://arxiv.org/pdf/2307.09288v2) p.8 | `m2023.touvron2023b.llama-2-70b.humaneval.0shot` |
| Llama 2 70B | MATH | 4-shot, maj1@1 | 13.5 | Meta (Touvron et al. 2023b, Table 25) | [arxiv_2307.09288](https://arxiv.org/pdf/2307.09288v2) p.51 | `m2023.touvron2023b.llama-2-70b.math.4shot-maj1at1` |
| Llama 2 70B | MMLU | 5-shot | 68.9 | Meta (Touvron et al. 2023b, Table 4) | [arxiv_2307.09288](https://arxiv.org/pdf/2307.09288v2) p.8 | `m2023.touvron2023b.llama-2-70b.mmlu.5shot` |
| Llama 2 70B | MMLU (clean subset) | contamination analysis, clean subset | 68.0 | Meta (Touvron et al. 2023b, Table 51) | [arxiv_2307.09288](https://arxiv.org/pdf/2307.09288v2) p.76 | `m2023.touvron2023b.llama-2-70b.mmlu.clean-subset` |
| PaLM-2-L | MMLU | 5-shot | 78.3 | Meta (Llama 2 paper), quoting Anil et al. 2023 | [arxiv_2307.09288](https://arxiv.org/pdf/2307.09288v2) p.8 | `m2023.touvron2023b.palm-2-l.mmlu.5shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 71.2 | Claude 2 | 0-shot pass@1, T=1 | 2023-07 | `m2023.anthropic-claude2-card.claude-2.humaneval.0shot` |
| GSM8K | 92.2 | Flan-PaLM 2 | 8-shot CoT + self-consistency, 40 paths | 2023-05 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Anthropic Claude 2 Model Card (July 2023), None, PDF page 10](https://www-cdn.anthropic.com/bd2a28d2535bfb0494cc8e2a3bf135d2e7523226/Model-Card-Claude-2.pdf#page=10): no table or figure caption on this page
- [Llama 2: Open Foundation and Fine-Tuned Chat Models, v2, PDF page 8](https://arxiv.org/pdf/2307.09288v2#page=8): Table 3: Overall performance on grouped academic benchmarks compared to open-source base models.; Table 4: Comparison to closed-source models on academic benchmarks.

## 2023-08

**August 2023.** 4 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Code Llama - Instruct 34B | HumanEval | 0-shot pass@1 greedy | 41.5 | Meta (Roziere et al. 2023, v3) | [arxiv_2308.12950](https://arxiv.org/pdf/2308.12950v3) p.6 | `m2023.roziere2023.code-llama-instruct-34b.humaneval.pass1` |
| Code Llama - Python 34B | HumanEval | 0-shot pass@1 greedy | 53.7 | Meta (Roziere et al. 2023, v3) | [arxiv_2308.12950](https://arxiv.org/pdf/2308.12950v3) p.6 | `m2023.roziere2023.code-llama-python-34b.humaneval.pass1` |
| Code Llama 34B | HumanEval | 0-shot pass@1 greedy | 48.8 | Meta (Roziere et al. 2023, v3) | [arxiv_2308.12950](https://arxiv.org/pdf/2308.12950v3) p.6 | `m2023.roziere2023.code-llama-34b.humaneval.pass1` |
| Llama 2 70B | HumanEval | 0-shot pass@1 | 30.5 | Meta (Code Llama paper, v3) | [arxiv_2308.12950](https://arxiv.org/pdf/2308.12950v3) p.6 | `m2023.roziere2023.llama-2-70b.humaneval.pass1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 71.2 | Claude 2 | 0-shot pass@1, T=1 | 2023-07 | `m2023.anthropic-claude2-card.claude-2.humaneval.0shot` |
| GSM8K | 92.2 | Flan-PaLM 2 | 8-shot CoT + self-consistency, 40 paths | 2023-05 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Code Llama: Open Foundation Models for Code, v3, PDF page 6](https://arxiv.org/pdf/2308.12950v3#page=6): Table 2: Code Llama pass@ scores on HumanEval and MBPP. The pass@1 scores of our models are.

## 2023-09

**September 2023.** 6 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| LLaMA 2 13B | MBPP (hand-verified subset, per 'Evaluation Differences' on p4) | 3-shot | 35.4 | Mistral AI (Mistral 7B paper) | [arxiv_2310.06825](https://arxiv.org/pdf/2310.06825v1) p.4 | `m2023.jiang2023mistral.llama-2-13b.mbpp.3shot` |
| LLaMA 2 13B | MMLU | 5-shot (Mistral pipeline) | 55.6 | Mistral AI (Mistral 7B paper) | [arxiv_2310.06825](https://arxiv.org/pdf/2310.06825v1) p.4 | `m2023.jiang2023mistral.llama-2-13b.mmlu.5shot` |
| Mistral 7B | GSM8K | 8-shot maj@8 | 52.2 | Mistral AI (Mistral 7B paper) | [arxiv_2310.06825](https://arxiv.org/pdf/2310.06825v1) p.4 | `m2023.jiang2023mistral.mistral-7b.gsm8k.8shot-maj8` |
| Mistral 7B | HumanEval | 0-shot | 30.5 | Mistral AI (Mistral 7B paper) | [arxiv_2310.06825](https://arxiv.org/pdf/2310.06825v1) p.4 | `m2023.jiang2023mistral.mistral-7b.humaneval.0shot` |
| Mistral 7B | MATH | 4-shot maj@4 | 13.1 | Mistral AI (Mistral 7B paper) | [arxiv_2310.06825](https://arxiv.org/pdf/2310.06825v1) p.4 | `m2023.jiang2023mistral.mistral-7b.math.4shot-maj4` |
| Mistral 7B | MMLU | 5-shot | 60.1 | Mistral AI (Mistral 7B paper) | [arxiv_2310.06825](https://arxiv.org/pdf/2310.06825v1) p.4 | `m2023.jiang2023mistral.mistral-7b.mmlu.5shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 71.2 | Claude 2 | 0-shot pass@1, T=1 | 2023-07 | `m2023.anthropic-claude2-card.claude-2.humaneval.0shot` |
| GSM8K | 92.2 | Flan-PaLM 2 | 8-shot CoT + self-consistency, 40 paths | 2023-05 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

## 2023-10

**October 2023.** 6 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| LLEMMA 34B | GSM8K | 8-shot CoT, greedy | 51.5 | EleutherAI/Princeton (Azerbayev et al. 2023) | [arxiv_2310.10631](https://arxiv.org/pdf/2310.10631v1) p.5 | `m2023.azerbayev2023.llemma-34b.gsm8k.8shot-greedy` |
| LLEMMA 34B | GSM8K | maj@100 | 69.3 | EleutherAI/Princeton (Azerbayev et al. 2023) | [arxiv_2310.10631](https://arxiv.org/pdf/2310.10631v1) p.5 | `m2023.azerbayev2023.llemma-34b.gsm8k.maj1at100` |
| LLEMMA 34B | GSM8k+Python (tool use) | pass@1 | 62.6 | EleutherAI/Princeton (Azerbayev et al. 2023) | [arxiv_2310.10631](https://arxiv.org/pdf/2310.10631v1) p.6 | `m2023.azerbayev2023.llemma-34b.gsm8k-python.pass1` |
| LLEMMA 34B | MATH | 4-example prompt, greedy | 25.0 | EleutherAI/Princeton (Azerbayev et al. 2023) | [arxiv_2310.10631](https://arxiv.org/pdf/2310.10631v1) p.5 | `m2023.azerbayev2023.llemma-34b.math.4shot-greedy` |
| LLEMMA 34B | MATH | maj@256 | 43.1 | EleutherAI/Princeton (Azerbayev et al. 2023) | [arxiv_2310.10631](https://arxiv.org/pdf/2310.10631v1) p.5 | `m2023.azerbayev2023.llemma-34b.math.maj1at256` |
| LLEMMA 34B | MMLU-STEM | 4-example CoT prompt, greedy | 49.0 | EleutherAI/Princeton (Azerbayev et al. 2023) | [arxiv_2310.10631](https://arxiv.org/pdf/2310.10631v1) p.5 | `m2023.azerbayev2023.llemma-34b.mmlu-stem.4shot-greedy` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 88.4 | GPT-4 | pass@1 greedy | 2023-10 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GSM8K | 92.2 | Flan-PaLM 2 | 8-shot CoT + self-consistency, 40 paths | 2023-05 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Mistral 7B, v1, PDF page 3](https://arxiv.org/pdf/2310.06825v1#page=3): Figure 2: Rolling buffer cache.; Figure 3: Pre-fill and chunking.
- [Mistral 7B, v1, PDF page 4](https://arxiv.org/pdf/2310.06825v1#page=4): Figure 4: Performance of Mistral 7B and different Llama models on a wide range of benchmarks.; Table 2: Comparison of Mistral 7B with Llama.; Table 3: Comparison of Chat models.

## 2023-11

**November 2023.** 12 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Falcon-180B | MMLU | 5-shot | 70.6 | TII (Falcon series paper, Table 19) | [arxiv_2311.16867](https://arxiv.org/pdf/2311.16867v1) p.34 | `m2023.almazrouei2023.falcon-180b.mmlu.5shot` |
| GPT-4 | GPQA Diamond | zero-shot CoT | 35.7 | Rein et al. 2023 (GPQA paper) | [arxiv_2311.12022](https://arxiv.org/pdf/2311.12022v1) p.19 | `m2023.rein2023.gpt-4.gpqa-diamond.0shot-cot` |
| GPT-4 | MATH | 4-shot (as labelled by xAI) | 42.5 | xAI (Announcing Grok blog) | [xai_grok1_blog](https://web.archive.org/web/20240317204026id_/https://x.ai/blog/grok) html | `m2023.xai-grok-blog.gpt-4.math.4shot` |
| GPT-4 | MMLU | 5-shot | 86.5 | TII (Falcon series paper, Table 19), quoting GPT-4 paper | [arxiv_2311.16867](https://arxiv.org/pdf/2311.16867v1) p.34 | `m2023.almazrouei2023.gpt-4.mmlu.5shot-as-quoted` |
| Grok-1 | GSM8K | 8-shot (chain-of-thought prompt) | 62.9 | xAI (Announcing Grok blog, Nov 3, 2023) | [xai_grok1_blog](https://web.archive.org/web/20240317204026id_/https://x.ai/blog/grok) html | `m2023.xai-grok-blog.grok-1.gsm8k` |
| Grok-1 | HumanEval | 0-shot pass@1 | 63.2 | xAI (Announcing Grok blog, Nov 3, 2023) | [xai_grok1_blog](https://web.archive.org/web/20240317204026id_/https://x.ai/blog/grok) html | `m2023.xai-grok-blog.grok-1.humaneval` |
| Grok-1 | MATH | 4-shot | 23.9 | xAI (Announcing Grok blog, Nov 3, 2023) | [xai_grok1_blog](https://web.archive.org/web/20240317204026id_/https://x.ai/blog/grok) html | `m2023.xai-grok-blog.grok-1.math` |
| Grok-1 | MMLU | 5-shot | 73.0 | xAI (Announcing Grok blog, Nov 3, 2023) | [xai_grok1_blog](https://web.archive.org/web/20240317204026id_/https://x.ai/blog/grok) html | `m2023.xai-grok-blog.grok-1.mmlu` |
| Qwen-72B (base) | GSM8K | 8-shot | 78.9 | Alibaba Qwen (Hugging Face model card, capture 2023-11-30) | [hf_qwen_72b_card](https://web.archive.org/web/20231130144143id_/https://huggingface.co/Qwen/Qwen-72B) html | `m2023.qwen-72b-card.qwen-72b.gsm8k.8shot` |
| Qwen-72B (base) | HumanEval | 0-shot | 35.4 | Alibaba Qwen (Hugging Face model card, capture 2023-11-30) | [hf_qwen_72b_card](https://web.archive.org/web/20231130144143id_/https://huggingface.co/Qwen/Qwen-72B) html | `m2023.qwen-72b-card.qwen-72b.humaneval.0shot` |
| Qwen-72B (base) | MATH | 4-shot | 35.2 | Alibaba Qwen (Hugging Face model card, capture 2023-11-30) | [hf_qwen_72b_card](https://web.archive.org/web/20231130144143id_/https://huggingface.co/Qwen/Qwen-72B) html | `m2023.qwen-72b-card.qwen-72b.math.4shot` |
| Qwen-72B (base) | MMLU | 5-shot | 77.4 | Alibaba Qwen (Hugging Face model card, capture 2023-11-30) | [hf_qwen_72b_card](https://web.archive.org/web/20231130144143id_/https://huggingface.co/Qwen/Qwen-72B) html | `m2023.qwen-72b-card.qwen-72b.mmlu.5shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 86.4 | GPT-4 | 5-shot | 2023-03 | `m2023.openai2023.gpt-4.mmlu.5shot` |
| HumanEval | 88.4 | GPT-4 | pass@1 greedy | 2023-10 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GSM8K | 92.2 | Flan-PaLM 2 | 8-shot CoT + self-consistency, 40 paths | 2023-05 | `m2023.anil2023.flan-palm-2.gsm8k.8shot-cot-sc40` |
| MATH | 50.3 | Minerva 540B | fixed 4-shot, maj1@64 | 2022-06 | `m2022.minerva.minerva-540b.math.maj1at64` |
| GPQA Diamond | 35.7 | GPT-4 | zero-shot CoT | 2023-11 | `m2023.rein2023.gpt-4.gpqa-diamond.0shot-cot` |

## 2023-12

**December 2023.** 38 verified scores for 11 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-4 | GSM8K | SFT & 5-shot CoT | 92.0 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gpt-4.gsm8k.sft-5shot-cot` |
| GPT-4 | HumanEval | 0-shot (reported) | 67.0 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gpt-4.humaneval.0shot-reported` |
| GPT-4 | MATH | 4-shot (via API, Nov 2023) | 52.9 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gpt-4.math.4shot-api` |
| GPT-4 | MATH | as reported by Zheng et al. (2023) | 50.3 | Gemini Team (Gemini 1.0 TR, Table 2), quoting Zheng et al. 2023 | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gpt-4.math.zheng2023` |
| GPT-4 | MMLU | 5-shot (reported) | 86.4 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gpt-4.mmlu.5shot-reported` |
| GPT-4 | MMLU | CoT@32 (via API, Nov 2023) | 87.29 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gpt-4.mmlu.cot32-api` |
| GPT-4 (gpt-4-0613) | MMLU | CoT@32 (and uncertainty-routed CoT@32) | 87.29 | Gemini Team (Gemini 1.0 TR, Figure 9) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.74 | `m2023.gemini2023.gpt-4-0613.mmlu.cot32-fig9` |
| Gemini Ultra | GSM8K | Maj1@32 | 94.4 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gemini-ultra.gsm8k.maj1at32` |
| Gemini Ultra | MATH | 4-shot | 53.2 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gemini-ultra.math.4shot` |
| Gemini Ultra | MMLU | 5-shot | 83.7 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gemini-ultra.mmlu.5shot` |
| Gemini Ultra | MMLU | CoT@32 uncertainty-routed | 90.04 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gemini-ultra.mmlu.cot32-uncertainty` |
| Gemini Ultra | MMLU | uncertainty-routed CoT@32 | 90.04 | Gemini Team (Gemini 1.0 TR, sec. 5.1.1) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.6 | `m2023.gemini2023.gemini-ultra.mmlu.text-claim` |
| Gemini Ultra | MMLU | not stated in text (blog) | 90.0 | Google (Introducing Gemini blog, Dec 06, 2023) | [google_gemini1_blog](https://web.archive.org/web/20231207230144id_/https://blog.google/technology/ai/google-gemini-ai/) html | `m2023.google-gemini-blog.gemini-ultra.mmlu` |
| Gemini Ultra (post-trained API model) | HumanEval | 0-shot (PT) | 74.4 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.gemini-ultra.humaneval.0shot-pt` |
| Grok 1 | HumanEval | 0-shot | 63.2 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.grok-1.humaneval.0shot` |
| Grok 1 | MATH | 4-shot | 23.9 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.grok-1.math.4shot` |
| Grok 1 | MMLU | 5-shot | 73.0 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.grok-1.mmlu.5shot` |
| LLAMA-2 | GSM8K | 5-shot (as labelled by Gemini TR) | 56.8 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.llama-2.gsm8k.5shot` |
| LLAMA-2 | HumanEval | 0-shot | 29.9 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.llama-2.humaneval.0shot` |
| LLAMA-2 | MATH | 4-shot | 13.5 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.llama-2.math.4shot` |
| LLAMA-2 (70B per Touvron et al. 2023b) | MMLU | decontaminated numbers from Touvron et al. (2023b) | 68.0 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.llama-2.mmlu.decontaminated` |
| LLaMA 2 70B | GSM8K | 5-shot | 53.6 | Mistral AI (Mixtral paper, Table 3) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.5 | `m2023.jiang2024mixtral.llama-2-70b.gsm8k.5shot` |
| LLaMA 2 70B | GSM8K | 8-shot maj@8 | 69.6 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.llama-2-70b.gsm8k.8shot-maj8` |
| LLaMA 2 70B | HumanEval | 0-shot | 29.3 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.llama-2-70b.humaneval.0shot` |
| LLaMA 2 70B | MATH | 4-shot maj@4 | 13.8 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.llama-2-70b.math.4shot-maj4` |
| LLaMA 2 70B | MMLU | 5-shot | 69.9 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.llama-2-70b.mmlu.5shot` |
| Mistral 7B | GSM8K | 8-shot maj@8 | 50.0 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mistral-7b.gsm8k.8shot-maj8` |
| Mistral 7B | HumanEval | 0-shot | 26.2 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mistral-7b.humaneval.0shot` |
| Mistral 7B | MATH | 4-shot maj@4 | 12.7 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mistral-7b.math.4shot-maj4` |
| Mistral 7B | MMLU | 5-shot | 62.5 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mistral-7b.mmlu.5shot` |
| Mixtral 8x7B | GSM8K | 5-shot | 58.4 | Mistral AI (Mixtral paper, Table 3) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.5 | `m2023.jiang2024mixtral.mixtral-8x7b.gsm8k.5shot` |
| Mixtral 8x7B | GSM8K | 8-shot maj@8 | 74.4 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mixtral-8x7b.gsm8k.8shot-maj8` |
| Mixtral 8x7B | HumanEval | 0-shot | 40.2 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mixtral-8x7b.humaneval.0shot` |
| Mixtral 8x7B | MATH | 4-shot maj@4 | 28.4 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mixtral-8x7b.math.4shot-maj4` |
| Mixtral 8x7B | MMLU | 5-shot | 70.6 | Mistral AI (Mixtral paper, Table 2) | [arxiv_2401.04088](https://arxiv.org/pdf/2401.04088v1) p.4 | `m2023.jiang2024mixtral.mixtral-8x7b.mmlu.5shot` |
| PaLM 2-L | GSM8K | 5-shot | 80.0 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.palm-2-l.gsm8k.5shot` |
| PaLM 2-L | MATH | 4-shot | 34.4 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.palm-2-l.math.4shot` |
| PaLM 2-L | MMLU | 5-shot | 78.4 | Gemini Team (Gemini 1.0 TR, Table 2) | [arxiv_2312.11805](https://arxiv.org/pdf/2312.11805v5) p.8 | `m2023.gemini2023.palm-2-l.mmlu.5shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.04 | Gemini Ultra | CoT@32 uncertainty-routed | 2023-12 | `m2023.gemini2023.gemini-ultra.mmlu.cot32-uncertainty` |
| HumanEval | 88.4 | GPT-4 | pass@1 greedy | 2023-10 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GSM8K | 94.4 | Gemini Ultra | Maj1@32 | 2023-12 | `m2023.gemini2023.gemini-ultra.gsm8k.maj1at32` |
| MATH | 53.2 | Gemini Ultra | 4-shot | 2023-12 | `m2023.gemini2023.gemini-ultra.math.4shot` |
| GPQA Diamond | 35.7 | GPT-4 | zero-shot CoT | 2023-11 | `m2023.rein2023.gpt-4.gpqa-diamond.0shot-cot` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Gemini: A Family of Highly Capable Multimodal Models, v5, PDF page 8](https://arxiv.org/pdf/2312.11805v5#page=8): Table 2: Gemini performance on text benchmarks with external comparisons and PaLM 2-L.

## 2024-01

**January 2024.** 19 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Code Llama - Instruct 70B | HumanEval | 0-shot pass@1, greedy | 67.8 | Meta (Code Llama report v3, Table 2) | [arxiv_2308.12950](https://arxiv.org/pdf/2308.12950v3) p.6 | `m2024.codellama.code-llama-instruct-70b.humaneval.pass1` |
| DeepSeek 67B (Base) | MMLU | 5-shot | 71.3 | DeepSeek (DeepSeek LLM report, base-model table) | [arxiv_2401.02954](https://arxiv.org/pdf/2401.02954v1) p.15 | `m2024.dsllm.deepseek-67b-base.mmlu.5-shot` |
| DeepSeek 67B Chat | GSM8K | 0-shot | 84.1 | DeepSeek (DeepSeek LLM report, Table 6) | [arxiv_2401.02954](https://arxiv.org/pdf/2401.02954v1) p.16 | `m2024.dsllm.deepseek-67b-chat.gsm8k.0-shot` |
| DeepSeek 67B Chat | GSM8K | 8-shot | 84.1 | DeepSeek (DeepSeek-V2 report, Table 3) | [arxiv_2405.04434](https://arxiv.org/pdf/2405.04434v5) p.19 | `m2024.dsv2.deepseek-67b-chat.gsm8k.8-shot` |
| DeepSeek 67B Chat | HumanEval | not stated in Table 6 caption (HumanEval is not in the 0-shot list) | 73.8 | DeepSeek (DeepSeek LLM report, Table 6) | [arxiv_2401.02954](https://arxiv.org/pdf/2401.02954v1) p.16 | `m2024.dsllm.deepseek-67b-chat.humaneval.0-shot` |
| DeepSeek 67B Chat | MATH | 0-shot | 32.6 | DeepSeek (DeepSeek LLM report, Table 6) | [arxiv_2401.02954](https://arxiv.org/pdf/2401.02954v1) p.16 | `m2024.dsllm.deepseek-67b-chat.math.0-shot` |
| DeepSeek 67B Chat | MMLU | 0-shot | 71.1 | DeepSeek (DeepSeek LLM report, Table 6) | [arxiv_2401.02954](https://arxiv.org/pdf/2401.02954v1) p.16 | `m2024.dsllm.deepseek-67b-chat.mmlu.0-shot` |
| DeepSeek-Coder-Instruct 33B | HumanEval (Python) | 0-shot, greedy | 79.3 | DeepSeek (Guo et al. 2024) | [arxiv_2401.14196](https://arxiv.org/pdf/2401.14196v1) p.11 | `m2023.guo2024.deepseek-coder-instruct-33b.humaneval.python` |
| GPT-4 (0125) | GPQA | 0-shot CoT (subset not stated in Table 2) | 41.4 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4-0125.gpqa.0-shot-cot` |
| GPT-4 (0125) | GSM8K | 8-shot CoT | 94.2 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4-0125.gsm8k.8-shot-cot` |
| GPT-4 (0125) | HumanEval | 0-shot | 86.6 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4-0125.humaneval.0-shot` |
| GPT-4 (0125) | MATH | 0-shot CoT | 64.5 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4-0125.math.0-shot-cot` |
| GPT-4 (0125) | MMLU | 0-shot CoT | 85.4 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4-0125.mmlu.0-shot-cot` |
| GPT-4 (0125) | MMLU | 5-shot | 85.1 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4-0125.mmlu.5-shot` |
| GPT-4 (0125) | MMLU-Pro | 5-shot CoT | 64.8 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4-0125.mmlu-pro.5-shot-cot` |
| gpt-4-0125-preview | GPQA | 0-shot CoT, 'assistant' system prompt (simple-evals) | 41.4 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-0125-preview.gpqa.0-shot-cot-assistant` |
| gpt-4-0125-preview | HumanEval | 0-shot CoT, 'assistant' system prompt (simple-evals) | 86.6 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-0125-preview.humaneval.0-shot-cot-assistant` |
| gpt-4-0125-preview | MATH | 0-shot CoT, 'assistant' system prompt (simple-evals) | 64.5 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-0125-preview.math.0-shot-cot-assistant` |
| gpt-4-0125-preview | MMLU | 0-shot CoT, 'assistant' system prompt (simple-evals) | 85.4 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-0125-preview.mmlu.0-shot-cot-assistant` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.04 | Gemini Ultra | CoT@32 uncertainty-routed | 2023-12 | `m2023.gemini2023.gemini-ultra.mmlu.cot32-uncertainty` |
| HumanEval | 88.4 | GPT-4 | pass@1 greedy | 2023-10 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GSM8K | 94.4 | Gemini Ultra | Maj1@32 | 2023-12 | `m2023.gemini2023.gemini-ultra.gsm8k.maj1at32` |
| MATH | 53.2 | Gemini Ultra | 4-shot | 2023-12 | `m2023.gemini2023.gemini-ultra.math.4shot` |
| GPQA Diamond | 35.7 | GPT-4 | zero-shot CoT | 2023-11 | `m2023.rein2023.gpt-4.gpqa-diamond.0shot-cot` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Mixtral of Experts, v1, PDF page 4](https://arxiv.org/pdf/2401.04088v1#page=4): Table 2: Comparison of Mixtral with Llama.; Figure 3: Results on MMLU, commonsense reasoning, world knowledge and reading comprehension,.
- [Mixtral of Experts, v1, PDF page 5](https://arxiv.org/pdf/2401.04088v1#page=5): Table 3: Comparison of Mixtral with Llama 2 70B and GPT-3.5.; Table 4: Comparison of Mixtral with Llama on Multilingual Benchmarks.; Figure 4: Long range performance of Mixtral.

## 2024-02

**February 2024.** 13 verified scores for 5 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| DeepSeekMath 7B (variant not named in the sentence) | MATH | self-consistency over 64 samples | 60.9 | DeepSeek (DeepSeekMath report, abstract) | [arxiv_2402.03300](https://arxiv.org/pdf/2402.03300v1) p.1 | `m2024.dsmath.deepseekmath-7b.math.sc64` |
| DeepSeekMath-RL 7B | GSM8K | chain-of-thought, Top1 | 88.2 | DeepSeek (DeepSeekMath report, Table 5) | [arxiv_2402.03300](https://arxiv.org/pdf/2402.03300v1) p.12 | `m2024.dsmath.deepseekmath-rl-7b.gsm8k.top1-cot` |
| DeepSeekMath-RL 7B | MATH | chain-of-thought, Top1 | 51.7 | DeepSeek (DeepSeekMath report, Table 5) | [arxiv_2402.03300](https://arxiv.org/pdf/2402.03300v1) p.12 | `m2024.dsmath.deepseekmath-rl-7b.math.top1-cot` |
| Gemini 1.5 Pro | MATH | 4-shot | 67.7 | Anthropic, quoting Google [9] | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.gemini-1.5-pro.math.4-shot` |
| Gemini 1.5 Pro | MMLU | 5-shot | 81.9 | Anthropic, quoting the Gemini 1.5 report | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2024.c3card.gemini-1.5-pro.mmlu.5-shot` |
| Gemini 1.5 Pro (Feb 2024) | GPQA | 0-shot (subset not stated) | 41.5 | Google DeepMind (Gemini 1.5 report v1, Table 8) | [arxiv_2403.05530v1](https://arxiv.org/pdf/2403.05530v1) p.21 | `m2024.gem15v1.gemini-1.5-pro.gpqa.0-shot` |
| Gemini 1.5 Pro (Feb 2024) | GSM8K | 11-shot | 91.7 | Google DeepMind (Gemini 1.5 report v1, Table 8) | [arxiv_2403.05530v1](https://arxiv.org/pdf/2403.05530v1) p.21 | `m2024.gem15v1.gemini-1.5-pro.gsm8k.11-shot` |
| Gemini 1.5 Pro (Feb 2024) | HumanEval | 0-shot | 71.9 | Google DeepMind (Gemini 1.5 report v1, Table 8) | [arxiv_2403.05530v1](https://arxiv.org/pdf/2403.05530v1) p.21 | `m2024.gem15v1.gemini-1.5-pro.humaneval.0-shot` |
| Gemini 1.5 Pro (Feb 2024) | MATH | 4-shot Minerva prompt | 58.5 | Google DeepMind (Gemini 1.5 report v1, Table 8) | [arxiv_2403.05530v1](https://arxiv.org/pdf/2403.05530v1) p.21 | `m2024.gem15v1.gemini-1.5-pro.math.4-shot-minerva` |
| Gemini 1.5 Pro (Feb 2024) | MMLU | 5-shot | 81.9 | Google DeepMind (Gemini 1.5 report v1, Table 8) | [arxiv_2403.05530v1](https://arxiv.org/pdf/2403.05530v1) p.21 | `m2024.gem15v1.gemini-1.5-pro.mmlu.5-shot` |
| Mistral Large | GSM8K | 5-shot | 81.0 | xAI, reporting Mistral Large | [xai_grok15_blog](https://web.archive.org/web/20240329004621id_/https://x.ai/blog/grok-1.5) html | `m2024.grok15.mistral-large.gsm8k.5-shot` |
| Mistral Large | HumanEval | 0-shot | 45.1 | xAI, reporting Mistral Large | [xai_grok15_blog](https://web.archive.org/web/20240329004621id_/https://x.ai/blog/grok-1.5) html | `m2024.grok15.mistral-large.humaneval.0-shot` |
| Mistral Large | MMLU | 5-shot | 81.2 | xAI, reporting Mistral Large | [xai_grok15_blog](https://web.archive.org/web/20240329004621id_/https://x.ai/blog/grok-1.5) html | `m2024.grok15.mistral-large.mmlu.5-shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.04 | Gemini Ultra | CoT@32 uncertainty-routed | 2023-12 | `m2023.gemini2023.gemini-ultra.mmlu.cot32-uncertainty` |
| HumanEval | 88.4 | GPT-4 | pass@1 greedy | 2023-10 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GSM8K | 94.4 | Gemini Ultra | Maj1@32 | 2023-12 | `m2023.gemini2023.gemini-ultra.gsm8k.maj1at32` |
| MATH | 60.9 | DeepSeekMath 7B (variant not named in the sentence) | self-consistency over 64 samples | 2024-02 | `m2024.dsmath.deepseekmath-7b.math.sc64` |
| GPQA Diamond | 35.7 | GPT-4 | zero-shot CoT | 2023-11 | `m2023.rein2023.gpt-4.gpqa-diamond.0shot-cot` |

## 2024-03

**March 2024.** 13 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude 3 Opus | GPQA Diamond | 0-shot CoT (mean of 10 rollouts) | 50.4 | Anthropic (Claude 3 model card, Table 1) | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2024.c3card.claude-3-opus.gpqa-diamond.0-shot-cot` |
| Claude 3 Opus | GSM8K | 0-shot CoT | 95.0 | Anthropic (Claude 3 model card, Table 1) | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2024.c3card.claude-3-opus.gsm8k.0-shot-cot` |
| Claude 3 Opus | HumanEval | 0-shot | 84.9 | Anthropic (Claude 3 model card, Table 1) | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2024.c3card.claude-3-opus.humaneval.0-shot` |
| Claude 3 Opus | MATH | 0-shot (CoT per footnote 5) | 60.1 | Anthropic (Claude 3 model card, Table 1) | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2024.c3card.claude-3-opus.math.0-shot-cot` |
| Claude 3 Opus | MMLU | 5-shot | 86.8 | Anthropic (Claude 3 model card, Table 1) | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2024.c3card.claude-3-opus.mmlu.5-shot` |
| Claude 3 Opus | MMLU | 5-shot CoT | 88.2 | Anthropic (Claude 3 model card, Table 1) | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2024.c3card.claude-3-opus.mmlu.5-shot-cot` |
| GPT-4 | GPQA Diamond | 0-shot CoT | 35.7 | Anthropic (Claude 3 model card), quoting Rein et al. 2023 [1] | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2023.anthropic-claude3-card.gpt-4.gpqa-diamond.0shot-cot` |
| GPT-4 | MATH | 0-shot | 42.5 | Anthropic (Claude 3 model card), quoting Bubeck et al. 2023 [39] | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2023.anthropic-claude3-card.gpt-4.math.0shot` |
| GPT-4 | MATH | 4-shot CoT | 52.9 | Anthropic (Claude 3 model card), quoting Gemini TR | [anthropic_claude3_card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) p.6 | `m2023.anthropic-claude3-card.gpt-4.math.4shot` |
| Grok-1.5 | GSM8K | 8-shot, maj@1 | 90.0 | xAI (Grok-1.5 post) | [xai_grok15_blog](https://web.archive.org/web/20240329004621id_/https://x.ai/blog/grok-1.5) html | `m2024.grok15.grok-1.5.gsm8k.8-shot` |
| Grok-1.5 | HumanEval | 0-shot pass@1 | 74.1 | xAI (Grok-1.5 post) | [xai_grok15_blog](https://web.archive.org/web/20240329004621id_/https://x.ai/blog/grok-1.5) html | `m2024.grok15.grok-1.5.humaneval.0-shot` |
| Grok-1.5 | MATH | 4-shot, maj@1 | 50.6 | xAI (Grok-1.5 post) | [xai_grok15_blog](https://web.archive.org/web/20240329004621id_/https://x.ai/blog/grok-1.5) html | `m2024.grok15.grok-1.5.math.4-shot` |
| Grok-1.5 | MMLU | 5-shot | 81.3 | xAI (Grok-1.5 post) | [xai_grok15_blog](https://web.archive.org/web/20240329004621id_/https://x.ai/blog/grok-1.5) html | `m2024.grok15.grok-1.5.mmlu.5-shot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.04 | Gemini Ultra | CoT@32 uncertainty-routed | 2023-12 | `m2023.gemini2023.gemini-ultra.mmlu.cot32-uncertainty` |
| HumanEval | 88.4 | GPT-4 | pass@1 greedy | 2023-10 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GSM8K | 95.0 | Claude 3 Opus | 0-shot CoT | 2024-03 | `m2024.c3card.claude-3-opus.gsm8k.0-shot-cot` |
| MATH | 60.9 | DeepSeekMath 7B (variant not named in the sentence) | self-consistency over 64 samples | 2024-02 | `m2024.dsmath.deepseekmath-7b.math.sc64` |
| GPQA Diamond | 50.4 | Claude 3 Opus | 0-shot CoT (mean of 10 rollouts) | 2024-03 | `m2024.c3card.claude-3-opus.gpqa-diamond.0-shot-cot` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Anthropic Claude 3 Model Card (March 2024), None, PDF page 6](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf#page=6): Table 1: We show evaluation results for reasoning, math, coding, reading comprehension, and question.
- [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context, v5, PDF page 30](https://arxiv.org/pdf/2403.05530v5#page=30): Table 11: Evaluation results of Gemini 1.5 Pro, 1.5 Flash and Gemini 1.0 models on standard coding,.

## 2024-04

**April 2024.** 19 verified scores for 5 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Llama 3 70B (instruction tuned) | GPQA | 0-shot | 39.5 | Meta (Llama 3 MODEL_CARD.md, commit 92a325e) | [meta_llama3_model_card_92a325e](https://raw.githubusercontent.com/meta-llama/llama3/92a325ec9925557b5fd64202c91024231a428c08/MODEL_CARD.md) html | `m2024.llama3card.llama-3-70b-instruct.gpqa.0-shot` |
| Llama 3 70B (instruction tuned) | GSM8K | 8-shot CoT | 93.0 | Meta (Llama 3 MODEL_CARD.md, commit 92a325e) | [meta_llama3_model_card_92a325e](https://raw.githubusercontent.com/meta-llama/llama3/92a325ec9925557b5fd64202c91024231a428c08/MODEL_CARD.md) html | `m2024.llama3card.llama-3-70b-instruct.gsm8k.8-shot-cot` |
| Llama 3 70B (instruction tuned) | HumanEval | 0-shot | 81.7 | Meta (Llama 3 MODEL_CARD.md, commit 92a325e) | [meta_llama3_model_card_92a325e](https://raw.githubusercontent.com/meta-llama/llama3/92a325ec9925557b5fd64202c91024231a428c08/MODEL_CARD.md) html | `m2024.llama3card.llama-3-70b-instruct.humaneval.0-shot` |
| Llama 3 70B (instruction tuned) | MATH | 4-shot CoT | 50.4 | Meta (Llama 3 MODEL_CARD.md, commit 92a325e) | [meta_llama3_model_card_92a325e](https://raw.githubusercontent.com/meta-llama/llama3/92a325ec9925557b5fd64202c91024231a428c08/MODEL_CARD.md) html | `m2024.llama3card.llama-3-70b-instruct.math.4-shot-cot` |
| Llama 3 70B (instruction tuned) | MMLU | 5-shot | 82.0 | Meta (Llama 3 MODEL_CARD.md, commit 92a325e) | [meta_llama3_model_card_92a325e](https://raw.githubusercontent.com/meta-llama/llama3/92a325ec9925557b5fd64202c91024231a428c08/MODEL_CARD.md) html | `m2024.llama3card.llama-3-70b-instruct.mmlu.5-shot` |
| Mixtral 8x22B (instructed) | GSM8K | maj@8 | 90.8 | Mistral AI (Mixtral 8x22B post) | [mistral_mixtral8x22b_blog](https://web.archive.org/web/20240417152317id_/https://mistral.ai/news/mixtral-8x22b/) html | `m2024.mixtral8x22b.mixtral-8x22b-instruct.gsm8k.maj8` |
| Mixtral 8x22B (instructed) | MATH | maj@4 | 44.6 | Mistral AI (Mixtral 8x22B post) | [mistral_mixtral8x22b_blog](https://web.archive.org/web/20240417152317id_/https://mistral.ai/news/mixtral-8x22b/) html | `m2024.mixtral8x22b.mixtral-8x22b-instruct.math.maj4` |
| Mixtral 8x22B Inst. | HumanEval | 0-shot | 75.0 | DeepSeek (DeepSeek-V2 report, Table 3) | [arxiv_2405.04434](https://arxiv.org/pdf/2405.04434v5) p.19 | `m2024.dsv2.mixtral-8x22b-instruct.humaneval.0-shot` |
| Mixtral 8x22B Inst. | MMLU | 5-shot | 77.8 | DeepSeek (DeepSeek-V2 report, Table 3) | [arxiv_2405.04434](https://arxiv.org/pdf/2405.04434v5) p.19 | `m2024.dsv2.mixtral-8x22b-instruct.mmlu.5-shot` |
| Phi-3-small 7b | GSM8K | 0-shot CoT | 88.9 | Microsoft (Phi-3 report v1, Apr 2024) | [arxiv_2404.14219](https://arxiv.org/pdf/2404.14219v1) p.5 | `m2024.phi3v1.phi-3-small.gsm8k.0-shot-cot` |
| Phi-3-small 7b | GSM8K | 8-shot CoT | 89.6 | Microsoft (Phi-3 report v4, Aug 2024) | [arxiv_2404.14219v4](https://arxiv.org/pdf/2404.14219v4) p.6 | `m2024.phi3v4.phi-3-small.gsm8k.8-shot-cot` |
| gpt-4-turbo-2024-04-09 | GPQA | 0-shot CoT, 'assistant' system prompt (simple-evals) | 49.3 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.gpqa.0-shot-cot-assistant` |
| gpt-4-turbo-2024-04-09 | GPQA | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 49.1 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.gpqa.0-shot-cot-chatgpt` |
| gpt-4-turbo-2024-04-09 | HumanEval | 0-shot CoT, 'assistant' system prompt (simple-evals) | 88.2 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.humaneval.0-shot-cot-assistant` |
| gpt-4-turbo-2024-04-09 | HumanEval | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 87.6 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.humaneval.0-shot-cot-chatgpt` |
| gpt-4-turbo-2024-04-09 | MATH | 0-shot CoT, 'assistant' system prompt (simple-evals) | 73.4 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.math.0-shot-cot-assistant` |
| gpt-4-turbo-2024-04-09 | MATH | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 72.2 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.math.0-shot-cot-chatgpt` |
| gpt-4-turbo-2024-04-09 | MMLU | 0-shot CoT, 'assistant' system prompt (simple-evals) | 86.7 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.mmlu.0-shot-cot-assistant` |
| gpt-4-turbo-2024-04-09 | MMLU | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 86.5 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4-turbo-2024-04-09.mmlu.0-shot-cot-chatgpt` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.04 | Gemini Ultra | CoT@32 uncertainty-routed | 2023-12 | `m2023.gemini2023.gemini-ultra.mmlu.cot32-uncertainty` |
| HumanEval | 88.4 | GPT-4 | pass@1 greedy | 2023-10 | `m2023.liu2023evalplus.gpt-4.humaneval.greedy` |
| GSM8K | 95.0 | Claude 3 Opus | 0-shot CoT | 2024-03 | `m2024.c3card.claude-3-opus.gsm8k.0-shot-cot` |
| MATH | 60.9 | DeepSeekMath 7B (variant not named in the sentence) | self-consistency over 64 samples | 2024-02 | `m2024.dsmath.deepseekmath-7b.math.sc64` |
| GPQA Diamond | 50.4 | Claude 3 Opus | 0-shot CoT (mean of 10 rollouts) | 2024-03 | `m2024.c3card.claude-3-opus.gpqa-diamond.0-shot-cot` |

## 2024-05

**May 2024.** 36 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| DeepSeek-V2 Chat (RL) | GSM8K | 8-shot | 92.2 | DeepSeek (DeepSeek-V2 report, Table 3) | [arxiv_2405.04434](https://arxiv.org/pdf/2405.04434v5) p.19 | `m2024.dsv2.deepseek-v2-chat-rl.gsm8k.8-shot` |
| DeepSeek-V2 Chat (RL) | HumanEval | 0-shot | 81.1 | DeepSeek (DeepSeek-V2 report, Table 3) | [arxiv_2405.04434](https://arxiv.org/pdf/2405.04434v5) p.19 | `m2024.dsv2.deepseek-v2-chat-rl.humaneval.0-shot` |
| DeepSeek-V2 Chat (RL) | MATH | 4-shot | 53.9 | DeepSeek (DeepSeek-V2 report, Table 3) | [arxiv_2405.04434](https://arxiv.org/pdf/2405.04434v5) p.19 | `m2024.dsv2.deepseek-v2-chat-rl.math.4-shot` |
| GPT-4o | AIME 2024 | 0-shot CoT (as labelled by Anthropic) | 9.3 | Anthropic, quoting OpenAI [9] | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.gpt-4o.aime-2024.0-shot-cot` |
| GPT-4o | GPQA | 0-shot CoT (subset not stated in Table 2) | 53.6 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4o.gpqa.0-shot-cot` |
| GPT-4o | GSM8K | 8-shot CoT | 96.1 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4o.gsm8k.8-shot-cot` |
| GPT-4o | HumanEval | 0-shot | 90.2 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4o.humaneval.0-shot` |
| GPT-4o | MATH | 0-shot CoT | 76.6 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4o.math.0-shot-cot` |
| GPT-4o | MMLU | 0-shot CoT | 88.7 | OpenAI (Hello GPT-4o post) | [openai_gpt4o_blog](https://web.archive.org/web/20240514235217id_/https://openai.com/index/hello-gpt-4o/) html | `m2024.gpt4oblog.gpt-4o.mmlu.0-shot-cot` |
| GPT-4o | MMLU | 5-shot, no CoT | 87.2 | OpenAI (Hello GPT-4o post) | [openai_gpt4o_blog](https://web.archive.org/web/20240514235217id_/https://openai.com/index/hello-gpt-4o/) html | `m2024.gpt4oblog.gpt-4o.mmlu.5-shot-no-cot` |
| GPT-4o | MMLU | 0-shot CoT | 88.7 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4o.mmlu.0-shot-cot` |
| GPT-4o | MMLU | 5-shot | 89.1 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4o.mmlu.5-shot` |
| GPT-4o | MMLU-Pro | as reported by xAI ('May 2024 release') | 72.6 | xAI (Grok-2 post); origin not stated, footnote only says the scores are for the May 2024 release of GPT-4o | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.gpt-4o.mmlu-pro.xai` |
| GPT-4o | MMLU-Pro | 5-shot CoT | 74.0 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.gpt-4o.mmlu-pro.5-shot-cot` |
| GPT-4o 0513 | AIME 2024 | pass@1, temperature 0.7, mean of 16 runs | 9.3 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.gpt-4o-0513.aime-2024.pass@1` |
| GPT-4o 0513 | GPQA Diamond | pass@1 | 49.9 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.gpt-4o-0513.gpqa-diamond.pass@1` |
| GPT-4o 0513 | MATH-500 | EM, greedy decoding | 74.6 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.gpt-4o-0513.math-500.em` |
| GPT-4o 0513 | MMLU | EM (shots not stated for chat models) | 87.2 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.gpt-4o-0513.mmlu.em` |
| GPT-4o 0513 | MMLU-Pro | EM | 72.6 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.gpt-4o-0513.mmlu-pro.em` |
| GPT-4o 0513 | SWE-bench Verified | resolved, Agentless framework | 38.8 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.gpt-4o-0513.swe-bench-verified.resolved` |
| Gemini 1.5 Pro (May 2024) | HumanEval | 0-shot | 84.1 | Google DeepMind (Gemini 1.5 report v5, Table 11) | [arxiv_2403.05530](https://arxiv.org/pdf/2403.05530v5) p.30 | `m2024.gem15v5.gemini-1.5-pro-may.humaneval.0-shot` |
| Gemini 1.5 Pro (May 2024) | MATH | 4-shot Minerva prompt (Table 11) | 67.7 | Google DeepMind (Gemini 1.5 report v5) | [arxiv_2403.05530](https://arxiv.org/pdf/2403.05530v5) p.4 | `m2024.gem15v5.gemini-1.5-pro-may.math.4-shot` |
| Gemini 1.5 Pro (May 2024) | MMLU | 5-shot | 85.9 | Google DeepMind (Gemini 1.5 report v5, Table 11) | [arxiv_2403.05530](https://arxiv.org/pdf/2403.05530v5) p.30 | `m2024.gem15v5.gemini-1.5-pro-may.mmlu.5-shot` |
| gpt-4-1106(-vision)-preview | GPQA (subset not stated in README) | 0-shot CoT, 'assistant' system prompt | 42.5 | OpenAI (simple-evals README, commit 294cb1f) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2023.simple-evals-2024-05-13.gpt-4-1106-preview.gpqa.0shot-cot-assistant` |
| gpt-4-1106(-vision)-preview | HumanEval | 0-shot CoT, 'assistant' system prompt | 83.7 | OpenAI (simple-evals README, commit 294cb1f) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2023.simple-evals-2024-05-13.gpt-4-1106-preview.humaneval.0shot-cot-assistant` |
| gpt-4-1106(-vision)-preview | MATH | 0-shot CoT, 'assistant' system prompt | 64.3 | OpenAI (simple-evals README, commit 294cb1f) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2023.simple-evals-2024-05-13.gpt-4-1106-preview.math.0shot-cot-assistant` |
| gpt-4-1106(-vision)-preview | MMLU | 0-shot CoT, 'assistant' system prompt | 84.7 | OpenAI (simple-evals README, commit 294cb1f) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2023.simple-evals-2024-05-13.gpt-4-1106-preview.mmlu.0shot-cot-assistant` |
| gpt-4o | AIME 2024 | pass@1 | 9.3 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.gpt-4o.aime-2024.pass1` |
| gpt-4o | GPQA | 0-shot CoT, 'assistant' system prompt (simple-evals) | 49.9 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.gpqa.0-shot-cot-assistant` |
| gpt-4o | GPQA | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 53.6 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.gpqa.0-shot-cot-chatgpt` |
| gpt-4o | HumanEval | 0-shot CoT, 'assistant' system prompt (simple-evals) | 91.0 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.humaneval.0-shot-cot-assistant` |
| gpt-4o | HumanEval | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 90.2 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.humaneval.0-shot-cot-chatgpt` |
| gpt-4o | MATH | 0-shot CoT, 'assistant' system prompt (simple-evals) | 76.6 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.math.0-shot-cot-assistant` |
| gpt-4o | MATH | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 76.6 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.math.0-shot-cot-chatgpt` |
| gpt-4o | MMLU | 0-shot CoT, 'assistant' system prompt (simple-evals) | 87.2 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.mmlu.0-shot-cot-assistant` |
| gpt-4o | MMLU | 0-shot CoT, 'chatgpt' system prompt (simple-evals) | 88.7 | OpenAI (simple-evals README, commit 294cb1f, 2024-05-13) | [openai_simple_evals_readme_2024-05-13](https://raw.githubusercontent.com/openai/simple-evals/294cb1fb18f7aed4e21dc567350b0761a9e6f699/README.md) md | `m2024.se0513.gpt-4o.mmlu.0-shot-cot-chatgpt` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.04 | Gemini Ultra | CoT@32 uncertainty-routed | 2023-12 | `m2023.gemini2023.gemini-ultra.mmlu.cot32-uncertainty` |
| HumanEval | 91.0 | gpt-4o | 0-shot CoT, 'assistant' system prompt (simple-evals) | 2024-05 | `m2024.se0513.gpt-4o.humaneval.0-shot-cot-assistant` |
| GSM8K | 95.0 | Claude 3 Opus | 0-shot CoT | 2024-03 | `m2024.c3card.claude-3-opus.gsm8k.0-shot-cot` |
| MATH | 76.6 | gpt-4o | 0-shot CoT, 'assistant' system prompt (simple-evals) | 2024-05 | `m2024.se0513.gpt-4o.math.0-shot-cot-assistant` |
| GPQA Diamond | 50.4 | Claude 3 Opus | 0-shot CoT (mean of 10 rollouts) | 2024-03 | `m2024.c3card.claude-3-opus.gpqa-diamond.0-shot-cot` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model, v5, PDF page 19](https://arxiv.org/pdf/2405.04434v5#page=19): Table 3: Comparison among DeepSeek-V2 Chat (SFT), DeepSeek-V2 Chat (RL), and other.; Table 4: English open-ended conversation evaluations.

## 2024-06

**June 2024.** 25 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude 3.5 Sonnet | GPQA | as reported by xAI ('June 2024 release') | 59.6 | xAI (Grok-2 post); origin not stated, footnote only says the scores are for the June 2024 release of Claude 3.5 Sonnet | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.claude-3.5-sonnet.gpqa.xai` |
| Claude 3.5 Sonnet | GPQA | 0-shot CoT (subset not stated in Table 2) | 59.4 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.claude-3.5-sonnet.gpqa.0-shot-cot` |
| Claude 3.5 Sonnet | GPQA Diamond | 0-shot CoT | 59.4 | Anthropic (Claude 3.5 Sonnet addendum, June 2024, Table 1) | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.claude-3.5-sonnet.gpqa-diamond.0-shot-cot` |
| Claude 3.5 Sonnet | GSM8K | 0-shot CoT | 96.4 | Anthropic (Claude 3.5 Sonnet addendum, June 2024, Table 1) | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.claude-3.5-sonnet.gsm8k.0-shot-cot` |
| Claude 3.5 Sonnet | GSM8K | 0-shot (table marks it with ♢, overriding the row's 8-shot CoT) | 96.4 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.claude-3.5-sonnet.gsm8k.0-shot` |
| Claude 3.5 Sonnet | HumanEval | 0-shot | 92.0 | Anthropic (Claude 3.5 Sonnet addendum, June 2024, Table 1) | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.claude-3.5-sonnet.humaneval.0-shot` |
| Claude 3.5 Sonnet | HumanEval | 0-shot | 92.0 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.claude-3.5-sonnet.humaneval.0-shot` |
| Claude 3.5 Sonnet | MATH | 0-shot CoT | 71.1 | Anthropic (Claude 3.5 Sonnet addendum, June 2024, Table 1) | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.claude-3.5-sonnet.math.0-shot-cot` |
| Claude 3.5 Sonnet | MATH | 0-shot CoT | 71.1 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.claude-3.5-sonnet.math.0-shot-cot` |
| Claude 3.5 Sonnet | MMLU | 0-shot CoT | 88.3 | Anthropic (Claude 3.5 Sonnet addendum, June 2024, Table 1) | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.claude-3.5-sonnet.mmlu.0-shot-cot` |
| Claude 3.5 Sonnet | MMLU | 5-shot | 88.7 | Anthropic (Claude 3.5 Sonnet addendum, June 2024, Table 1) | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.claude-3.5-sonnet.mmlu.5-shot` |
| Claude 3.5 Sonnet | MMLU | 5-shot CoT | 90.4 | Anthropic (Claude 3.5 Sonnet addendum, June 2024, Table 1) | [anthropic_claude35_addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf) p.2 | `m2024.c35jun.claude-3.5-sonnet.mmlu.5-shot-cot` |
| Claude 3.5 Sonnet | MMLU | 0-shot CoT | 88.3 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.claude-3.5-sonnet.mmlu.0-shot-cot` |
| Claude 3.5 Sonnet | MMLU | 5-shot | 89.9 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.claude-3.5-sonnet.mmlu.5-shot` |
| Claude 3.5 Sonnet | MMLU-Pro | 0-shot CoT | 75.1 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet.mmlu-pro.0-shot-cot` |
| Claude 3.5 Sonnet | MMLU-Pro | as reported by xAI ('June 2024 release') | 76.1 | xAI (Grok-2 post); origin not stated, footnote only says the scores are for the June 2024 release | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.claude-3.5-sonnet.mmlu-pro.xai` |
| Claude 3.5 Sonnet | MMLU-Pro | 5-shot CoT | 77.0 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.claude-3.5-sonnet.mmlu-pro.5-shot-cot` |
| Claude 3.5 Sonnet | SWE-bench Verified | pass@1, Anthropic agent scaffold | 33.4 | Anthropic (Oct 2024 addendum, Table 2) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.3 | `m2024.c35oct.claude-3.5-sonnet.swe-bench-verified.pass1` |
| DS-Coder-V2-Instruct | GSM8K | greedy decoding, no tools or voting | 94.9 | DeepSeek (DeepSeek-Coder-V2 report, Table 9) | [arxiv_2406.11931](https://arxiv.org/pdf/2406.11931v1) p.13 | `m2024.dscoderv2.deepseek-coder-v2-instruct.gsm8k.greedy` |
| DS-Coder-V2-Instruct | HumanEval | Python, greedy decoding | 90.2 | DeepSeek (DeepSeek-Coder-V2 report, Table 3) | [arxiv_2406.11931](https://arxiv.org/pdf/2406.11931v1) p.8 | `m2024.dscoderv2.deepseek-coder-v2-instruct.humaneval.greedy` |
| DS-Coder-V2-Instruct | MATH | greedy decoding, no tools or voting | 75.7 | DeepSeek (DeepSeek-Coder-V2 report, Table 9) | [arxiv_2406.11931](https://arxiv.org/pdf/2406.11931v1) p.13 | `m2024.dscoderv2.deepseek-coder-v2-instruct.math.greedy` |
| Qwen2-72B (base) | MMLU | base model (Qwen2 Table 2) | 84.2 | Alibaba (Qwen2 report, Table 2) | [arxiv_2407.10671](https://arxiv.org/pdf/2407.10671v4) p.9 | `m2024.qwen2.qwen2-72b-base.mmlu.base` |
| Qwen2-72B-Instruct | GSM8K | not stated in table | 93.2 | Alibaba (Qwen2 report, Table 6) | [arxiv_2407.10671](https://arxiv.org/pdf/2407.10671v4) p.13 | `m2024.qwen2.qwen2-72b-instruct.gsm8k.instruct` |
| Qwen2-72B-Instruct | HumanEval | not stated in table | 86.0 | Alibaba (Qwen2 report, Table 6) | [arxiv_2407.10671](https://arxiv.org/pdf/2407.10671v4) p.13 | `m2024.qwen2.qwen2-72b-instruct.humaneval.instruct` |
| Qwen2-72B-Instruct | MATH | not stated in table | 69.0 | Alibaba (Qwen2 report, Table 6) | [arxiv_2407.10671](https://arxiv.org/pdf/2407.10671v4) p.13 | `m2024.qwen2.qwen2-72b-instruct.math.instruct` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.4 | Claude 3.5 Sonnet | 5-shot CoT | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.mmlu.5-shot-cot` |
| HumanEval | 92.0 | Claude 3.5 Sonnet | 0-shot | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.humaneval.0-shot` |
| GSM8K | 96.4 | Claude 3.5 Sonnet | 0-shot CoT | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.gsm8k.0-shot-cot` |
| MATH | 76.6 | gpt-4o | 0-shot CoT, 'assistant' system prompt (simple-evals) | 2024-05 | `m2024.se0513.gpt-4o.math.0-shot-cot-assistant` |
| GPQA Diamond | 59.4 | Claude 3.5 Sonnet | 0-shot CoT | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.gpqa-diamond.0-shot-cot` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Anthropic Claude 3.5 Sonnet Model Card Addendum (June 2024), None, PDF page 2](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf#page=2): Table 1: This table shows evaluation results for reasoning, math, coding, reading comprehension, and ques-.; Table 2: This table shows evaluation results for multimodal tasks.

## 2024-07

**July 2024.** 18 verified scores for 7 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT4o-mini | GSM8K | not stated in table | 93.2 | Alibaba (Qwen2.5 report, Table 7) | [arxiv_2412.15115](https://arxiv.org/pdf/2412.15115v1) p.11 | `m2024.qwen25.gpt-4o-mini.gsm8k.qwen-harness` |
| LLaMA-3.1 405B-Inst. | AIME 2024 | pass@1, temperature 0.7, mean of 16 runs | 23.3 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.llama-3.1-405b-instruct.aime-2024.pass@1` |
| LLaMA-3.1 405B-Inst. | MATH-500 | EM, greedy decoding | 73.8 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.llama-3.1-405b-instruct.math-500.em` |
| LLaMA-3.1 405B-Inst. | SWE-bench Verified | resolved, Agentless framework | 24.5 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.llama-3.1-405b-instruct.swe-bench-verified.resolved` |
| Llama 3 405B (Llama 3.1 405B Instruct) | GPQA | 0-shot CoT (subset not stated in Table 2) | 51.1 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.llama-3.1-405b.gpqa.0-shot-cot` |
| Llama 3 405B (Llama 3.1 405B Instruct) | GSM8K | 8-shot CoT | 96.8 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| Llama 3 405B (Llama 3.1 405B Instruct) | HumanEval | 0-shot | 89.0 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.llama-3.1-405b.humaneval.0-shot` |
| Llama 3 405B (Llama 3.1 405B Instruct) | MATH | 0-shot CoT | 73.8 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.llama-3.1-405b.math.0-shot-cot` |
| Llama 3 405B (Llama 3.1 405B Instruct) | MMLU | 0-shot CoT | 88.6 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.llama-3.1-405b.mmlu.0-shot-cot` |
| Llama 3 405B (Llama 3.1 405B Instruct) | MMLU | 5-shot | 87.3 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.llama-3.1-405b.mmlu.5-shot` |
| Llama 3 405B (Llama 3.1 405B Instruct) | MMLU-Pro | 5-shot CoT | 73.3 | Meta (Llama 3 Herd of Models, Table 2) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.3 | `m2024.llama3herd.llama-3.1-405b.mmlu-pro.5-shot-cot` |
| Llama 3 405B (pre-trained) | MMLU | pre-trained model; shot count not stated in Table 13 | 85.2 | Meta (Table 13) | [arxiv_2407.21783](https://arxiv.org/pdf/2407.21783v3) p.31 | `m2024.llama3herd.llama-3.1-405b-base.mmlu.pretrained` |
| Llama 3.1 405B Instruct | GPQA Diamond | 0-shot CoT | 49.0 | Meta (Llama 3.3 MODEL_CARD.md, commit c908f5b) | [meta_llama33_model_card_c908f5b](https://raw.githubusercontent.com/meta-llama/llama-models/c908f5b7bd2c2fbdd89a48f6bc252efd4ebc293f/models/llama3_3/MODEL_CARD.md) html | `m2024.llama33card.llama-3.1-405b-instruct.gpqa-diamond.0-shot-cot` |
| Mistral Large 2 (pretrained) | MMLU | not stated | 84.0 | Mistral AI (Mistral Large 2 post) | [mistral_large2_blog](https://web.archive.org/web/20240724152547id_/https://mistral.ai/news/mistral-large-2407/) html | `m2024.mistrallarge2.mistral-large-2-base.mmlu.unspecified` |
| gpt-4o-mini-2024-07-18 | GPQA | 0-shot CoT (simple-evals), assistant system prompt | 40.2 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-mini-2024-07-18.gpqa.0-shot-cot` |
| gpt-4o-mini-2024-07-18 | HumanEval | 0-shot CoT (simple-evals), assistant system prompt | 87.2 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-mini-2024-07-18.humaneval.0-shot-cot` |
| gpt-4o-mini-2024-07-18 | MATH | 0-shot CoT (simple-evals), assistant system prompt | 70.2 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-mini-2024-07-18.math.0-shot-cot` |
| gpt-4o-mini-2024-07-18 | MMLU | 0-shot CoT (simple-evals), assistant system prompt | 82.0 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-mini-2024-07-18.mmlu.0-shot-cot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.4 | Claude 3.5 Sonnet | 5-shot CoT | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.mmlu.5-shot-cot` |
| MMLU-Pro | 77.0 | Claude 3.5 Sonnet | 5-shot CoT | 2024-07 | `m2024.llama3herd.claude-3.5-sonnet.mmlu-pro.5-shot-cot` |
| HumanEval | 92.0 | Claude 3.5 Sonnet | 0-shot | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 76.6 | gpt-4o | 0-shot CoT, 'assistant' system prompt (simple-evals) | 2024-05 | `m2024.se0513.gpt-4o.math.0-shot-cot-assistant` |
| GPQA Diamond | 59.4 | Claude 3.5 Sonnet | 0-shot CoT | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.gpqa-diamond.0-shot-cot` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Qwen2 Technical Report, v4, PDF page 9](https://arxiv.org/pdf/2407.10671v4#page=9): Table 2: Performance of the 70B+ models.
- [The Llama 3 Herd of Models, v3, PDF page 3](https://arxiv.org/pdf/2407.21783v3#page=3): Table 2: Performance of finetuned Llama 3 models on key benchmark evaluations.

## 2024-08

**August 2024.** 11 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-4o (checkpoint not stated) | SWE-bench Verified | best open-source scaffold (Agentless, per the post's scaffold chart) | 33.2 | OpenAI (Introducing SWE-bench Verified) | [openai_swebench_verified_blog](https://web.archive.org/web/20240815183946id_/https://openai.com/index/introducing-swe-bench-verified/) html | `m2024.swebv.gpt-4o.swe-bench-verified.agentless` |
| Grok-2 | GPQA | not stated (subset not stated) | 56.0 | xAI (Grok-2 post) | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.grok-2.gpqa.unspecified` |
| Grok-2 | HumanEval | pass@1 | 88.4 | xAI (Grok-2 post) | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.grok-2.humaneval.pass1` |
| Grok-2 | MATH | maj@1 | 76.1 | xAI (Grok-2 post) | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.grok-2.math.maj1` |
| Grok-2 | MMLU | 0-shot CoT | 87.5 | xAI (Grok-2 post) | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.grok-2.mmlu.0-shot-cot` |
| Grok-2 | MMLU-Pro | 0-shot CoT | 75.5 | xAI (Grok-2 post) | [xai_grok2_blog](https://web.archive.org/web/20240814061116id_/https://x.ai/blog/grok-2) html | `m2024.grok2.grok-2.mmlu-pro.0-shot-cot` |
| Phi-3.5-MoE 16x3.8B | GSM8K | 8-shot CoT | 88.7 | Microsoft (Phi-3 report v4, Aug 2024, Table 3) | [arxiv_2404.14219v4](https://arxiv.org/pdf/2404.14219v4) p.9 | `m2024.phi3v4.phi-3.5-moe.gsm8k.8-shot-cot` |
| gpt-4o-2024-08-06 | GPQA | 0-shot CoT (simple-evals), assistant system prompt | 53.1 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-2024-08-06.gpqa.0-shot-cot` |
| gpt-4o-2024-08-06 | HumanEval | 0-shot CoT (simple-evals), assistant system prompt | 90.2 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-2024-08-06.humaneval.0-shot-cot` |
| gpt-4o-2024-08-06 | MATH | 0-shot CoT (simple-evals), assistant system prompt | 75.9 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-2024-08-06.math.0-shot-cot` |
| gpt-4o-2024-08-06 | MMLU | 0-shot CoT (simple-evals), assistant system prompt | 88.7 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.gpt-4o-2024-08-06.mmlu.0-shot-cot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 90.4 | Claude 3.5 Sonnet | 5-shot CoT | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.mmlu.5-shot-cot` |
| MMLU-Pro | 77.0 | Claude 3.5 Sonnet | 5-shot CoT | 2024-07 | `m2024.llama3herd.claude-3.5-sonnet.mmlu-pro.5-shot-cot` |
| HumanEval | 92.0 | Claude 3.5 Sonnet | 0-shot | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 76.6 | gpt-4o | 0-shot CoT, 'assistant' system prompt (simple-evals) | 2024-05 | `m2024.se0513.gpt-4o.math.0-shot-cot-assistant` |
| GPQA Diamond | 59.4 | Claude 3.5 Sonnet | 0-shot CoT | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.gpqa-diamond.0-shot-cot` |
| SWE-bench Verified | 33.2 | GPT-4o (checkpoint not stated) | best open-source scaffold (Agentless, per the post's scaffold chart) | 2024-08 | `m2024.swebv.gpt-4o.swe-bench-verified.agentless` |

## 2024-09

**September 2024.** 33 verified scores for 8 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| DeepSeek V2.5-0905 | GPQA Diamond | pass@1 | 41.3 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v2.5-0905.gpqa-diamond.pass@1` |
| Gemini 1.5 Pro (September 2024 release) | GPQA Diamond | 0-shot CoT | 59.1 | Anthropic, quoting Google's September 2024 release | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.gemini-1.5-pro-002.gpqa-diamond.0-shot-cot` |
| Gemini 1.5 Pro (September 2024 release) | MATH | 4-shot CoT | 86.5 | Anthropic, quoting Google's September 2024 release | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.gemini-1.5-pro-002.math.4-shot-cot` |
| Gemini 1.5 Pro (September 2024 release) | MMLU-Pro | 0-shot CoT (as labelled by Anthropic) | 75.8 | Anthropic, quoting Google's September 2024 release | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.gemini-1.5-pro-002.mmlu-pro.0-shot-cot` |
| OpenAI-o1-mini | AIME 2024 | pass@1 | 63.6 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-mini.aime-2024.pass@1` |
| OpenAI-o1-mini | GPQA Diamond | pass@1 | 60.0 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-mini.gpqa-diamond.pass@1` |
| OpenAI-o1-mini | MATH-500 | pass@1 | 90.0 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-mini.math-500.pass@1` |
| OpenAI-o1-mini | MMLU | pass@1 | 85.2 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-mini.mmlu.pass@1` |
| OpenAI-o1-mini | SWE-bench Verified | resolved | 41.6 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-mini.swe-bench-verified.resolved` |
| Qwen2.5-72B (base) | MMLU | 5-shot, base model (Table 2) | 86.1 | Alibaba (Qwen2.5 report, Table 2) | [arxiv_2412.15115](https://arxiv.org/pdf/2412.15115v1) p.8 | `m2024.qwen25.qwen2.5-72b-base.mmlu.base` |
| Qwen2.5-72B-Instruct | GPQA | not stated in table | 49.0 | Alibaba (Qwen2.5 report, Table 6) | [arxiv_2412.15115](https://arxiv.org/pdf/2412.15115v1) p.11 | `m2024.qwen25.qwen2.5-72b-instruct.gpqa.instruct` |
| Qwen2.5-72B-Instruct | GSM8K | not stated in table | 95.8 | Alibaba (Qwen2.5 report, Table 6) | [arxiv_2412.15115](https://arxiv.org/pdf/2412.15115v1) p.11 | `m2024.qwen25.qwen2.5-72b-instruct.gsm8k.instruct` |
| Qwen2.5-72B-Instruct | HumanEval | not stated in table | 86.6 | Alibaba (Qwen2.5 report, Table 6) | [arxiv_2412.15115](https://arxiv.org/pdf/2412.15115v1) p.11 | `m2024.qwen25.qwen2.5-72b-instruct.humaneval.instruct` |
| Qwen2.5-72B-Instruct | MATH | not stated in table | 83.1 | Alibaba (Qwen2.5 report, Table 6) | [arxiv_2412.15115](https://arxiv.org/pdf/2412.15115v1) p.11 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| Qwen2.5-72B-Instruct | MMLU-Pro | not stated in table | 71.1 | Alibaba (Qwen2.5 report, Table 6) | [arxiv_2412.15115](https://arxiv.org/pdf/2412.15115v1) p.11 | `m2024.qwen25.qwen2.5-72b-instruct.mmlu-pro.instruct` |
| o1 (Sept 2024 pre-release) | GPQA Diamond | cons@64 | 78.0 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1.gpqa-diamond.cons64` |
| o1 (Sept 2024 pre-release) | GPQA Diamond | pass@1 | 77.3 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1.gpqa-diamond.pass1` |
| o1 (Sept 2024 pre-release) | MATH-500 | pass@1 | 94.8 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1.math.pass1` |
| o1 (Sept 2024 pre-release) | MMLU | pass@1 | 92.3 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1.mmlu.pass1` |
| o1-mini | AIME 2024 | not stated in the sentence (o1 74.4% matches the o1 blog's pass@1) | 70.0 | OpenAI (o1-mini launch post) | [openai_o1mini_blog](https://web.archive.org/web/20240912183657id_/https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/) html | `m2024.o1mini.o1-mini.aime-2024.unspecified` |
| o1-mini | GPQA | 0-shot CoT (simple-evals), no system prompt (o-series) | 60.0 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-mini.gpqa.0-shot-cot` |
| o1-mini | HumanEval | 0-shot CoT (simple-evals), no system prompt (o-series) | 92.4 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-mini.humaneval.0-shot-cot` |
| o1-mini | MATH-500 | 0-shot CoT (simple-evals), no system prompt (o-series); README footnote: MATH-500 for models on or after o1 (o1-preview/o1-mini status ambiguous) | 90.0 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-mini.math.0-shot-cot` |
| o1-mini | MMLU | 0-shot CoT (simple-evals), no system prompt (o-series) | 85.2 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-mini.mmlu.0-shot-cot` |
| o1-preview | AIME 2024 | pass@1 | 44.6 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1-preview.aime-2024.pass1` |
| o1-preview | GPQA | 0-shot CoT (simple-evals), no system prompt (o-series) | 73.3 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-preview.gpqa.0-shot-cot` |
| o1-preview | GPQA Diamond | cons@64 | 78.3 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| o1-preview | GPQA Diamond | pass@1 | 73.3 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1-preview.gpqa-diamond.pass1` |
| o1-preview | HumanEval | 0-shot CoT (simple-evals), no system prompt (o-series) | 92.4 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-preview.humaneval.0-shot-cot` |
| o1-preview | MATH-500 | pass@1 | 85.5 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1-preview.math.pass1` |
| o1-preview | MATH-500 | 0-shot CoT (simple-evals), no system prompt (o-series); README footnote: MATH-500 for models on or after o1 (o1-preview/o1-mini status ambiguous) | 85.5 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-preview.math.0-shot-cot` |
| o1-preview | MMLU | pass@1 | 90.8 | OpenAI (o1 launch post, Appendix A) | [openai_o1_blog](https://web.archive.org/web/20240913230723id_/https://openai.com/index/learning-to-reason-with-llms/) html | `m2024.o1blog.o1-preview.mmlu.pass1` |
| o1-preview | MMLU | 0-shot CoT (simple-evals), no system prompt (o-series) | 90.8 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1-preview.mmlu.0-shot-cot` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 77.0 | Claude 3.5 Sonnet | 5-shot CoT | 2024-07 | `m2024.llama3herd.claude-3.5-sonnet.mmlu-pro.5-shot-cot` |
| HumanEval | 92.0 | Claude 3.5 Sonnet | 0-shot | 2024-06 | `m2024.c35jun.claude-3.5-sonnet.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 76.6 | gpt-4o | 0-shot CoT, 'assistant' system prompt (simple-evals) | 2024-05 | `m2024.se0513.gpt-4o.math.0-shot-cot-assistant` |
| MATH-500 | 94.8 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.math.pass1` |
| GPQA Diamond | 78.3 | o1-preview | cons@64 | 2024-09 | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| SWE-bench Verified | 33.2 | GPT-4o (checkpoint not stated) | best open-source scaffold (Agentless, per the post's scaffold chart) | 2024-08 | `m2024.swebv.gpt-4o.swe-bench-verified.agentless` |
| AIME 2024 | 70.0 | o1-mini | not stated in the sentence (o1 74.4% matches the o1 blog's pass@1) | 2024-09 | `m2024.o1mini.o1-mini.aime-2024.unspecified` |

## 2024-10

**October 2024.** 23 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude 3.5 Haiku | GPQA Diamond | 0-shot CoT | 41.6 | Anthropic (Oct 2024 addendum, Table 8) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.7 | `m2024.c35oct.claude-3.5-haiku.gpqa-diamond.0-shot-cot` |
| Claude 3.5 Haiku | HumanEval | 0-shot | 88.1 | Anthropic (Oct 2024 addendum, Table 8) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.7 | `m2024.c35oct.claude-3.5-haiku.humaneval.0-shot` |
| Claude 3.5 Haiku | MATH | 0-shot CoT | 69.2 | Anthropic (Oct 2024 addendum, Table 8) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.7 | `m2024.c35oct.claude-3.5-haiku.math.0-shot-cot` |
| Claude 3.5 Haiku | MMLU | 0-shot CoT | 80.3 | Anthropic (Oct 2024 addendum, Table 8) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.7 | `m2024.c35oct.claude-3.5-haiku.mmlu.0-shot-cot` |
| Claude 3.5 Haiku | MMLU | 5-shot CoT | 80.9 | Anthropic (Oct 2024 addendum, Table 8) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.7 | `m2024.c35oct.claude-3.5-haiku.mmlu.5-shot-cot` |
| Claude 3.5 Haiku | MMLU-Pro | 0-shot CoT | 65.0 | Anthropic (Oct 2024 addendum, Table 8) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.7 | `m2024.c35oct.claude-3.5-haiku.mmlu-pro.0-shot-cot` |
| Claude 3.5 Haiku | SWE-bench Verified | pass@1, Anthropic agent scaffold | 40.6 | Anthropic (Oct 2024 addendum, Table 2) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.3 | `m2024.c35oct.claude-3.5-haiku.swe-bench-verified.pass1` |
| Claude 3.5 Sonnet (New) | AIME 2024 | 0-shot CoT | 16.0 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.aime-2024.0-shot-cot` |
| Claude 3.5 Sonnet (New) | GPQA Diamond | 0-shot CoT | 65.0 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.gpqa-diamond.0-shot-cot` |
| Claude 3.5 Sonnet (New) | HumanEval | 0-shot | 93.7 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| Claude 3.5 Sonnet (New) | MATH | 0-shot CoT | 78.3 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.math.0-shot-cot` |
| Claude 3.5 Sonnet (New) | MMLU | 0-shot CoT | 89.3 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.mmlu.0-shot-cot` |
| Claude 3.5 Sonnet (New) | MMLU | 5-shot | 88.7 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.mmlu.5-shot` |
| Claude 3.5 Sonnet (New) | MMLU | 5-shot CoT | 90.5 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.mmlu.5-shot-cot` |
| Claude 3.5 Sonnet (New) | MMLU-Pro | 0-shot CoT | 78.0 | Anthropic (Claude 3.5 Sonnet (New) & Haiku addendum, Oct 2024, Table 7) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.6 | `m2024.c35oct.claude-3.5-sonnet-new.mmlu-pro.0-shot-cot` |
| Claude 3.5 Sonnet (New) | SWE-bench Verified | pass@1, Anthropic agent scaffold | 49.0 | Anthropic (Oct 2024 addendum, Table 2) | [anthropic_claude35_oct_addendum](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) p.3 | `m2024.c35oct.claude-3.5-sonnet-new.swe-bench-verified.pass1` |
| Claude-3.5-Sonnet-1022 | AIME 2024 | pass@1, temperature 0.7, mean of 16 runs | 16.0 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.claude-3.5-sonnet-1022.aime-2024.pass@1` |
| Claude-3.5-Sonnet-1022 | GPQA Diamond | pass@1 | 65.0 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.claude-3.5-sonnet-1022.gpqa-diamond.pass@1` |
| Claude-3.5-Sonnet-1022 | HumanEval-Mul | pass@1, 8-language average | 81.7 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.claude-3.5-sonnet-1022.humaneval-mul.pass@1` |
| Claude-3.5-Sonnet-1022 | MATH-500 | EM, greedy decoding | 78.3 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.claude-3.5-sonnet-1022.math-500.em` |
| Claude-3.5-Sonnet-1022 | MMLU | EM (shots not stated for chat models) | 88.3 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.claude-3.5-sonnet-1022.mmlu.em` |
| Claude-3.5-Sonnet-1022 | MMLU-Pro | EM | 78.0 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.claude-3.5-sonnet-1022.mmlu-pro.em` |
| Claude-3.5-Sonnet-1022 | SWE-bench Verified | resolved, Agentless framework | 50.8 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.claude-3.5-sonnet-1022.swe-bench-verified.resolved` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 78.0 | Claude 3.5 Sonnet (New) | 0-shot CoT | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.mmlu-pro.0-shot-cot` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 78.3 | Claude 3.5 Sonnet (New) | 0-shot CoT | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.math.0-shot-cot` |
| MATH-500 | 94.8 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.math.pass1` |
| GPQA Diamond | 78.3 | o1-preview | cons@64 | 2024-09 | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| SWE-bench Verified | 49.0 | Claude 3.5 Sonnet (New) | pass@1, Anthropic agent scaffold | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.swe-bench-verified.pass1` |
| AIME 2024 | 70.0 | o1-mini | not stated in the sentence (o1 74.4% matches the o1 blog's pass@1) | 2024-09 | `m2024.o1mini.o1-mini.aime-2024.unspecified` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Anthropic Claude 3.5 Sonnet (new) & Haiku Model Card Addendum (Oct 2024), None, PDF page 6](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf#page=6): Table 7: This table shows evaluation results for the upgraded Claude 3.5 Sonnet and peer models on reason-.

## 2024-11

**November 2024.** 9 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Marco-o1-MCTS (step) | MGSM-En | CoT prompt | 90.4 | Alibaba (Marco-o1 report, Table 2) | [arxiv_2411.14405](https://arxiv.org/pdf/2411.14405v1) p.5 | `m2024.marcoo1.marco-o1-mcts-step.mgsm-en.cot` |
| QwQ-32B-Preview | AIME (year not stated) | not stated | 50.0 | Alibaba Qwen (QwQ-32B-Preview post) | [qwen_qwq32b_preview_blog](https://web.archive.org/web/20241127204917id_/https://qwenlm.github.io/blog/qwq-32b-preview/) html | `m2024.qwq.qwq-32b-preview.aime.unspecified` |
| QwQ-32B-Preview | AIME 2024 | pass@1 | 50.0 | DeepSeek (DeepSeek-R1 report v1, Table 5) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.14 | `m2024.r1v1.qwq-32b-preview.aime-2024.pass1` |
| QwQ-32B-Preview | GPQA | not stated | 65.2 | Alibaba Qwen (QwQ-32B-Preview post) | [qwen_qwq32b_preview_blog](https://web.archive.org/web/20241127204917id_/https://qwenlm.github.io/blog/qwq-32b-preview/) html | `m2024.qwq.qwq-32b-preview.gpqa.unspecified` |
| QwQ-32B-Preview | GPQA Diamond | pass@1 | 54.5 | DeepSeek (DeepSeek-R1 report v1, Table 5) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.14 | `m2024.r1v1.qwq-32b-preview.gpqa-diamond.pass1` |
| QwQ-32B-Preview | LiveCodeBench | not stated | 50.0 | Alibaba Qwen (QwQ-32B-Preview post) | [qwen_qwq32b_preview_blog](https://web.archive.org/web/20241127204917id_/https://qwenlm.github.io/blog/qwq-32b-preview/) html | `m2024.qwq.qwq-32b-preview.livecodebench.unspecified` |
| QwQ-32B-Preview | LiveCodeBench | pass@1 | 41.9 | DeepSeek (DeepSeek-R1 report v1, Table 5) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.14 | `m2024.r1v1.qwq-32b-preview.livecodebench.pass1` |
| QwQ-32B-Preview | MATH-500 | not stated | 90.6 | Alibaba Qwen (QwQ-32B-Preview post) | [qwen_qwq32b_preview_blog](https://web.archive.org/web/20241127204917id_/https://qwenlm.github.io/blog/qwq-32b-preview/) html | `m2024.qwq.qwq-32b-preview.math-500.unspecified` |
| QwQ-32B-Preview | MATH-500 | pass@1 | 90.6 | DeepSeek (DeepSeek-R1 report v1, Table 5) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.14 | `m2024.r1v1.qwq-32b-preview.math-500.pass1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 78.0 | Claude 3.5 Sonnet (New) | 0-shot CoT | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.mmlu-pro.0-shot-cot` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 78.3 | Claude 3.5 Sonnet (New) | 0-shot CoT | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.math.0-shot-cot` |
| MATH-500 | 94.8 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.math.pass1` |
| GPQA Diamond | 78.3 | o1-preview | cons@64 | 2024-09 | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| SWE-bench Verified | 49.0 | Claude 3.5 Sonnet (New) | pass@1, Anthropic agent scaffold | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.swe-bench-verified.pass1` |
| AIME 2024 | 70.0 | o1-mini | not stated in the sentence (o1 74.4% matches the o1 blog's pass@1) | 2024-09 | `m2024.o1mini.o1-mini.aime-2024.unspecified` |

## 2024-12

**December 2024.** 26 verified scores for 8 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| DeepSeek-V3 | AIME 2024 | pass@1, temperature 0.7, mean of 16 runs | 39.2 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v3.aime-2024.pass@1` |
| DeepSeek-V3 | GPQA Diamond | pass@1 | 59.1 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v3.gpqa-diamond.pass@1` |
| DeepSeek-V3 | HumanEval-Mul | pass@1, 8-language average | 82.6 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v3.humaneval-mul.pass@1` |
| DeepSeek-V3 | MATH-500 | EM, greedy decoding | 90.2 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v3.math-500.em` |
| DeepSeek-V3 | MMLU | EM (shots not stated for chat models) | 88.5 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v3.mmlu.em` |
| DeepSeek-V3 | MMLU-Pro | EM | 75.9 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v3.mmlu-pro.em` |
| DeepSeek-V3 | SWE-bench Verified | resolved, Agentless framework | 42.0 | DeepSeek (DeepSeek-V3 report, Table 6, own harness) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.31 | `m2024.dsv3.deepseek-v3.swe-bench-verified.resolved` |
| DeepSeek-V3 Base | GSM8K | 8-shot EM | 89.3 | DeepSeek (DeepSeek-V3 report, base-model table) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.25 | `m2024.dsv3.deepseek-v3-base.gsm8k.8-shot` |
| DeepSeek-V3 Base | MMLU | 5-shot EM | 87.1 | DeepSeek (DeepSeek-V3 report, base-model table) | [arxiv_2412.19437](https://arxiv.org/pdf/2412.19437v2) p.25 | `m2024.dsv3.deepseek-v3-base.mmlu.5-shot` |
| Gemini 2.0 Flash (research coding agent) | SWE-bench Verified | agent with code execution tools, samples hundreds of candidate solutions | 51.8 | Google (developers blog, Dec 11 2024) | [google_gemini2_devblog](https://web.archive.org/web/20241211155630id_/https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/) html | `m2024.gemini2dev.gemini-2.0-flash-agent.swe-bench-verified.agent` |
| Llama-3.3 70B Instruct | GPQA Diamond | 0-shot CoT | 50.5 | Meta (Llama 3.3 MODEL_CARD.md, commit c908f5b) | [meta_llama33_model_card_c908f5b](https://raw.githubusercontent.com/meta-llama/llama-models/c908f5b7bd2c2fbdd89a48f6bc252efd4ebc293f/models/llama3_3/MODEL_CARD.md) html | `m2024.llama33card.llama-3.3-70b-instruct.gpqa-diamond.0-shot-cot` |
| Llama-3.3 70B Instruct | HumanEval | 0-shot pass@1 | 88.4 | Meta (Llama 3.3 MODEL_CARD.md, commit c908f5b) | [meta_llama33_model_card_c908f5b](https://raw.githubusercontent.com/meta-llama/llama-models/c908f5b7bd2c2fbdd89a48f6bc252efd4ebc293f/models/llama3_3/MODEL_CARD.md) html | `m2024.llama33card.llama-3.3-70b-instruct.humaneval.0-shot-pass@1` |
| Llama-3.3 70B Instruct | MATH | 0-shot CoT | 77.0 | Meta (Llama 3.3 MODEL_CARD.md, commit c908f5b) | [meta_llama33_model_card_c908f5b](https://raw.githubusercontent.com/meta-llama/llama-models/c908f5b7bd2c2fbdd89a48f6bc252efd4ebc293f/models/llama3_3/MODEL_CARD.md) html | `m2024.llama33card.llama-3.3-70b-instruct.math.0-shot-cot` |
| Llama-3.3 70B Instruct | MMLU | 0-shot CoT | 86.0 | Meta (Llama 3.3 MODEL_CARD.md, commit c908f5b) | [meta_llama33_model_card_c908f5b](https://raw.githubusercontent.com/meta-llama/llama-models/c908f5b7bd2c2fbdd89a48f6bc252efd4ebc293f/models/llama3_3/MODEL_CARD.md) html | `m2024.llama33card.llama-3.3-70b-instruct.mmlu.0-shot-cot` |
| Llama-3.3 70B Instruct | MMLU-Pro | 5-shot CoT | 68.9 | Meta (Llama 3.3 MODEL_CARD.md, commit c908f5b) | [meta_llama33_model_card_c908f5b](https://raw.githubusercontent.com/meta-llama/llama-models/c908f5b7bd2c2fbdd89a48f6bc252efd4ebc293f/models/llama3_3/MODEL_CARD.md) html | `m2024.llama33card.llama-3.3-70b-instruct.mmlu-pro.5-shot-cot` |
| Llama-3.3 70b instruct | MMLU | simple-evals (0-shot CoT), temperature 0.5 | 86.3 | Microsoft (Phi-4 report, Table 1) | [arxiv_2412.08905](https://arxiv.org/pdf/2412.08905v1) p.2 | `m2024.phi4.llama-3.3-70b-instruct.mmlu.simple-evals` |
| OpenAI-o1-1217 | AIME 2024 | pass@1 | 79.2 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-1217.aime-2024.pass@1` |
| OpenAI-o1-1217 | GPQA Diamond | pass@1 | 75.7 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-1217.gpqa-diamond.pass@1` |
| OpenAI-o1-1217 | MATH-500 | pass@1 | 96.4 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-1217.math-500.pass@1` |
| OpenAI-o1-1217 | MMLU | pass@1 | 91.8 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-1217.mmlu.pass@1` |
| OpenAI-o1-1217 | SWE-bench Verified | resolved | 48.9 | DeepSeek (DeepSeek-R1 report v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2024.r1v1.openai-o1-1217.swe-bench-verified.resolved` |
| o1 | GPQA | 0-shot CoT (simple-evals), no system prompt (o-series) | 75.7 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1.gpqa.0-shot-cot` |
| o1 | MATH-500 | 0-shot CoT (simple-evals), no system prompt (o-series) | 96.4 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1.math-500.0-shot-cot` |
| o1 | MMLU | 0-shot CoT (simple-evals), no system prompt (o-series) | 91.8 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2024.se0709.o1.mmlu.0-shot-cot` |
| phi-4 14b | MATH | simple-evals, temperature 0.5 | 80.4 | Microsoft (Phi-4 report, Table 1) | [arxiv_2412.08905](https://arxiv.org/pdf/2412.08905v1) p.2 | `m2024.phi4.phi-4.math.simple-evals` |
| phi-4 14b | MMLU | simple-evals (0-shot CoT), temperature 0.5 | 84.8 | Microsoft (Phi-4 report, Table 1) | [arxiv_2412.08905](https://arxiv.org/pdf/2412.08905v1) p.2 | `m2024.phi4.phi-4.mmlu.simple-evals` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 78.0 | Claude 3.5 Sonnet (New) | 0-shot CoT | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.mmlu-pro.0-shot-cot` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 94.8 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.math.pass1` |
| GPQA Diamond | 78.3 | o1-preview | cons@64 | 2024-09 | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| SWE-bench Verified | 51.8 | Gemini 2.0 Flash (research coding agent) | agent with code execution tools, samples hundreds of candidate solutions | 2024-12 | `m2024.gemini2dev.gemini-2.0-flash-agent.swe-bench-verified.agent` |
| AIME 2024 | 70.0 | o1-mini | not stated in the sentence (o1 74.4% matches the o1 blog's pass@1) | 2024-09 | `m2024.o1mini.o1-mini.aime-2024.unspecified` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [DeepSeek-V3 Technical Report, v2, PDF page 1](https://arxiv.org/pdf/2412.19437v2#page=1): Figure 1: Benchmark performance of DeepSeek-V3 and its counterparts.
- [DeepSeek-V3 Technical Report, v2, PDF page 31](https://arxiv.org/pdf/2412.19437v2#page=31): Table 6: Comparison between DeepSeek-V3 and other representative chat models.

## 2025-01

**January 2025.** 19 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| DeepSeek-R1 | AIME 2024 | Pass@1 | 79.8 | DeepSeek (DeepSeek-R1 TR v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2025.r1v1.deepseek-r1.aime24.pass1` |
| DeepSeek-R1 | GPQA Diamond | Pass@1 | 71.5 | DeepSeek (DeepSeek-R1 TR v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2025.r1v1.deepseek-r1.gpqa.pass1` |
| DeepSeek-R1 | LiveCodeBench | Pass@1-COT | 65.9 | DeepSeek (DeepSeek-R1 TR v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2025.r1v1.deepseek-r1.lcb.pass1-cot` |
| DeepSeek-R1 | MATH-500 | Pass@1 | 97.3 | DeepSeek (DeepSeek-R1 TR v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2025.r1v1.deepseek-r1.math500.pass1` |
| DeepSeek-R1 | MMLU | Pass@1, simple-evals prompt (0-shot) | 90.8 | DeepSeek (DeepSeek-R1 TR v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2025.r1v1.deepseek-r1.mmlu.pass1` |
| DeepSeek-R1 | MMLU-Pro | EM | 84.0 | DeepSeek (DeepSeek-R1 TR v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2025.r1v1.deepseek-r1.mmlu-pro.em` |
| DeepSeek-R1 | SWE-bench Verified | Resolved | 49.2 | DeepSeek (DeepSeek-R1 TR v1, Table 4) | [arxiv_2501.12948v1](https://arxiv.org/pdf/2501.12948v1) p.13 | `m2025.r1v1.deepseek-r1.swebench.resolved` |
| Kimi k1.5 (long-CoT) | AIME 2024 | Pass@1 | 77.5 | Moonshot AI (Kimi k1.5 TR v1, abstract) | [arxiv_2501.12599](https://arxiv.org/pdf/2501.12599v1) p.1 | `m2025.kimi-k15.kimi-k1.5-long-cot.aime24.pass1` |
| Kimi k1.5 (long-CoT) | MATH-500 | EM (Table 2: MATH-500 (EM)) | 96.2 | Moonshot AI (Kimi k1.5 TR v1, abstract) | [arxiv_2501.12599](https://arxiv.org/pdf/2501.12599v1) p.1 | `m2025.kimi-k15.kimi-k1.5-long-cot.math500.em` |
| OpenAI o3-mini (high) | AIME 2024 | launch table | 87.3 | OpenAI (GPT-4.5 launch post, Feb 27 2025) | [openai_gpt45_blog](https://web.archive.org/web/20250301015804id_/https://openai.com/index/introducing-gpt-4-5/) html | `m2025.gpt45-blog.o3-mini-high.aime24` |
| OpenAI o3-mini (high) | GPQA (subset not stated) | launch table | 79.7 | OpenAI (GPT-4.5 launch post, Feb 27 2025) | [openai_gpt45_blog](https://web.archive.org/web/20250301015804id_/https://openai.com/index/introducing-gpt-4-5/) html | `m2025.gpt45-blog.o3-mini-high.gpqa` |
| OpenAI o3-mini (high) | MMMLU | launch table | 81.1 | OpenAI (GPT-4.5 launch post, Feb 27 2025) | [openai_gpt45_blog](https://web.archive.org/web/20250301015804id_/https://openai.com/index/introducing-gpt-4-5/) html | `m2025.gpt45-blog.o3-mini-high.mmmlu` |
| OpenAI o3-mini (high) | SWE-bench Verified (477 of 500 tasks) | 23/500 tasks omitted (footnote 2) | 49.3 | OpenAI (GPT-4.1 launch post, Apr 14 2025, appendix) | [openai_gpt41_blog](https://web.archive.org/web/20250414172812id_/https://openai.com/index/gpt-4-1/) html | `m2025.gpt41-blog.o3-mini-high.swebench` |
| o3-mini (tools), non-final checkpoint | SWE-bench Verified (n=477 subset) | OpenAI internal tool scaffold, pass@1 over 4 tries | 61.0 | OpenAI (o3-mini System Card, Section 5.7.2) | [openai_o3mini_system_card](https://web.archive.org/web/20250212235848id_/https://cdn.openai.com/o3-mini-system-card-feb10.pdf) p.28 | `m2025.o3mini-card.o3-mini-tools.swebench.n477` |
| o3-mini launch candidate | SWE-bench Verified (n=477 subset) | Agentless 1.0 scaffold | 39.0 | OpenAI (o3-mini System Card, Section 5.7.2) | [openai_o3mini_system_card](https://web.archive.org/web/20250212235848id_/https://cdn.openai.com/o3-mini-system-card-feb10.pdf) p.28 | `m2025.o3mini-card.o3-mini.swebench.agentless.n477` |
| o3-mini-high | GPQA (subset not stated) | 0-shot CoT (simple-evals) | 77.2 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.o3-mini-high.gpqa` |
| o3-mini-high | HumanEval | 0-shot CoT (simple-evals) | 97.6 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.o3-mini-high.humaneval` |
| o3-mini-high | MATH-500 | 0-shot CoT (simple-evals) | 97.9 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.o3-mini-high.math500` |
| o3-mini-high | MMLU | 0-shot CoT (simple-evals) | 86.9 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.o3-mini-high.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 84.0 | DeepSeek-R1 | EM | 2025-01 | `m2025.r1v1.deepseek-r1.mmlu-pro.em` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 97.3 | DeepSeek-R1 | Pass@1 | 2025-01 | `m2025.r1v1.deepseek-r1.math500.pass1` |
| GPQA Diamond | 78.3 | o1-preview | cons@64 | 2024-09 | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| SWE-bench Verified | 51.8 | Gemini 2.0 Flash (research coding agent) | agent with code execution tools, samples hundreds of candidate solutions | 2024-12 | `m2024.gemini2dev.gemini-2.0-flash-agent.swe-bench-verified.agent` |
| AIME 2024 | 79.8 | DeepSeek-R1 | Pass@1 | 2025-01 | `m2025.r1v1.deepseek-r1.aime24.pass1` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning, v1, PDF page 13](https://arxiv.org/pdf/2501.12948v1#page=13): Table 4: Comparison between DeepSeek-R1 and other representative models.
- [OpenAI o3-mini System Card (Feb 10, 2025), 20250212235848, PDF page 28](https://web.archive.org/web/20250212235848id_/https://cdn.openai.com/o3-mini-system-card-feb10.pdf#page=28): no table or figure caption on this page

## 2025-02

**February 2025.** 18 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude 3.7 Sonnet | SWE-bench Verified (n=489 subset) | high compute: parallel attempts, regression-test rejection, scoring-model selection | 70.3 | Anthropic (Claude 3.7 Sonnet launch post, appendix) | [anthropic_claude37_blog](https://web.archive.org/web/20250226031458id_/https://www.anthropic.com/news/claude-3-7-sonnet) html | `m2025.claude37-blog.claude-3.7-sonnet.swebench.parallel` |
| Claude 3.7 Sonnet | SWE-bench Verified (n=489 subset) | without the high-compute scaffold | 63.7 | Anthropic (Claude 3.7 Sonnet launch post, appendix) | [anthropic_claude37_blog](https://web.archive.org/web/20250226031458id_/https://www.anthropic.com/news/claude-3-7-sonnet) html | `m2025.claude37-blog.claude-3.7-sonnet.swebench.single` |
| GPT-4.5 | AIME 2024 | launch table | 36.7 | OpenAI (GPT-4.5 launch post, Feb 27 2025) | [openai_gpt45_blog](https://web.archive.org/web/20250301015804id_/https://openai.com/index/introducing-gpt-4-5/) html | `m2025.gpt45-blog.gpt-4.5.aime24` |
| GPT-4.5 | GPQA (subset not stated) | launch table | 71.4 | OpenAI (GPT-4.5 launch post, Feb 27 2025) | [openai_gpt45_blog](https://web.archive.org/web/20250301015804id_/https://openai.com/index/introducing-gpt-4-5/) html | `m2025.gpt45-blog.gpt-4.5.gpqa` |
| GPT-4.5 | MMLU (English, not translated) | 0-shot | 89.6 | OpenAI (GPT-4.5 System Card, Table 16) | [openai_gpt45_system_card](https://web.archive.org/web/20250301122206id_/https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf) p.26 | `m2025.gpt45-card.gpt-4.5.mmlu-english` |
| GPT-4.5 | MMMLU | launch table | 85.1 | OpenAI (GPT-4.5 launch post, Feb 27 2025) | [openai_gpt45_blog](https://web.archive.org/web/20250301015804id_/https://openai.com/index/introducing-gpt-4-5/) html | `m2025.gpt45-blog.gpt-4.5.mmmlu` |
| GPT-4.5 | SWE-bench Verified | 'best internal performance' | 38.0 | OpenAI (GPT-4.5 launch post, Feb 27 2025) | [openai_gpt45_blog](https://web.archive.org/web/20250301015804id_/https://openai.com/index/introducing-gpt-4-5/) html | `m2025.gpt45-blog.gpt-4.5.swebench` |
| Grok 3 (Think) | AIME 2025 | cons@64 | 93.3 | xAI (Grok 3 Beta launch post, prose) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-think.aime25.cons64.prose` |
| Grok 3 (Think) [chart code GROK_3_R] | AIME 2024 | chart scoreMax (inferred highest test-time compute; the prose states cons@64 only for AIME 2025) | 93.3 | xAI (Grok 3 Beta launch post, Feb 19 2025, chart data) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-think.aime24.max` |
| Grok 3 (Think) [chart code GROK_3_R] | AIME 2024 | chart base bar (scoreMax is the highest test-time compute) | 83.9 | xAI (Grok 3 Beta launch post, Feb 19 2025, chart data) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-think.aime24.score` |
| Grok 3 (Think) [chart code GROK_3_R] | GPQA | chart scoreMax (highest test-time compute) | 84.6 | xAI (Grok 3 Beta launch post, Feb 19 2025, chart data) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-think.gpqa.max` |
| Grok 3 (Think) [chart code GROK_3_R] | GPQA | chart base bar | 80.2 | xAI (Grok 3 Beta launch post, Feb 19 2025, chart data) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-think.gpqa.score` |
| Grok 3 (Think) [chart code GROK_3_R] | LiveCodeBench | chart scoreMax (highest test-time compute) | 79.4 | xAI (Grok 3 Beta launch post, Feb 19 2025, chart data) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-think.lcb.max` |
| Grok 3 (Think) [chart code GROK_3_R] | LiveCodeBench | chart base bar | 70.6 | xAI (Grok 3 Beta launch post, Feb 19 2025, chart data) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-think.lcb.score` |
| Grok 3 Beta (reasoning off) | MMLU-Pro | reasoning turned off | 79.9 | xAI (Grok 3 Beta launch post, HTML table) | [xai_grok3_blog](https://web.archive.org/web/20250311172142id_/https://x.ai/news/grok-3) html | `m2025.grok3-blog.grok-3-beta.mmlu-pro` |
| gpt-4.5-preview-2025-02-27 | GPQA (subset not stated) | 0-shot CoT, assistant system prompt | 69.5 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.gpt-4.5-preview.gpqa` |
| gpt-4.5-preview-2025-02-27 | HumanEval | 0-shot CoT, assistant system prompt | 88.6 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.gpt-4.5-preview.humaneval` |
| gpt-4.5-preview-2025-02-27 | MMLU | 0-shot CoT, assistant system prompt | 90.8 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.gpt-4.5-preview.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 84.0 | DeepSeek-R1 | EM | 2025-01 | `m2025.r1v1.deepseek-r1.mmlu-pro.em` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 97.3 | DeepSeek-R1 | Pass@1 | 2025-01 | `m2025.r1v1.deepseek-r1.math500.pass1` |
| GPQA Diamond | 78.3 | o1-preview | cons@64 | 2024-09 | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| SWE-bench Verified | 51.8 | Gemini 2.0 Flash (research coding agent) | agent with code execution tools, samples hundreds of candidate solutions | 2024-12 | `m2024.gemini2dev.gemini-2.0-flash-agent.swe-bench-verified.agent` |
| AIME 2024 | 93.3 | Grok 3 (Think) [chart code GROK_3_R] | chart scoreMax (inferred highest test-time compute; the prose states cons@64 only for AIME 2025) | 2025-02 | `m2025.grok3-blog.grok-3-think.aime24.max` |
| AIME 2025 | 93.3 | Grok 3 (Think) | cons@64 | 2025-02 | `m2025.grok3-blog.grok-3-think.aime25.cons64.prose` |

## 2025-03

**March 2025.** 13 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| DeepSeek-V3-0324 | AIME (year not stated) | model card list | 59.4 | DeepSeek (DeepSeek-V3-0324 Hugging Face model card) | [hf_deepseek_v3_0324_apr](https://web.archive.org/web/20250411142921id_/https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) html | `m2025.hf-v3-0324.deepseek-v3-0324.aime` |
| DeepSeek-V3-0324 | GPQA | model card list | 68.4 | DeepSeek (DeepSeek-V3-0324 Hugging Face model card) | [hf_deepseek_v3_0324_apr](https://web.archive.org/web/20250411142921id_/https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) html | `m2025.hf-v3-0324.deepseek-v3-0324.gpqa` |
| DeepSeek-V3-0324 | LiveCodeBench (window not stated) | model card list | 49.2 | DeepSeek (DeepSeek-V3-0324 Hugging Face model card) | [hf_deepseek_v3_0324_apr](https://web.archive.org/web/20250411142921id_/https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) html | `m2025.hf-v3-0324.deepseek-v3-0324.lcb` |
| DeepSeek-V3-0324 | MATH-500 | Acc.; starred = taken from the model's own report/blog | 94.0 | Moonshot AI (Kimi K2 TR, Table 3) | [arxiv_2507.20534](https://arxiv.org/pdf/2507.20534v2) p.16 | `m2025.kimi-k2.deepseek-v3-0324.math500` |
| DeepSeek-V3-0324 | MMLU-Pro | model card list (predecessor → new) | 81.2 | DeepSeek (DeepSeek-V3-0324 Hugging Face model card) | [hf_deepseek_v3_0324_apr](https://web.archive.org/web/20250411142921id_/https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) html | `m2025.hf-v3-0324.deepseek-v3-0324.mmlu-pro` |
| Gemini 2.5 Pro (Experimental 03-25) | SWE-bench Verified | custom agent setup | 63.8 | Google (Gemini 2.5 launch post, Mar 25 2025) | [google_gemini25_blog](https://web.archive.org/web/20250325170959id_/https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) html | `m2025.gemini25-blog.gemini-2.5-pro.swebench.custom-agent` |
| Gemini2.5-Pro | AIME 2024 | as reported by Qwen | 92.0 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.gemini-2.5-pro.aime24` |
| Gemini2.5-Pro | AIME 2025 | as reported by Qwen | 86.7 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.gemini-2.5-pro.aime25` |
| Gemini2.5-Pro | GPQA Diamond | as reported by Qwen | 84.0 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.gemini-2.5-pro.gpqa` |
| Gemini2.5-Pro | LiveCodeBench v5 | as reported by Qwen | 70.4 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.gemini-2.5-pro.lcb-v5` |
| QwQ-32B | AIME 2024 | as reported by Qwen (Qwen3 TR) | 79.5 | Alibaba Qwen (Qwen3 TR, Table 13) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.16 | `m2025.qwen3.qwq-32b.aime24` |
| QwQ-32B | GPQA Diamond | as reported by Qwen (Qwen3 TR) | 65.6 | Alibaba Qwen (Qwen3 TR, Table 13) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.16 | `m2025.qwen3.qwq-32b.gpqa` |
| QwQ-32B | LiveCodeBench v5 | as reported by Qwen (Qwen3 TR) | 62.7 | Alibaba Qwen (Qwen3 TR, Table 13) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.16 | `m2025.qwen3.qwq-32b.lcb-v5` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 84.0 | DeepSeek-R1 | EM | 2025-01 | `m2025.r1v1.deepseek-r1.mmlu-pro.em` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 97.3 | DeepSeek-R1 | Pass@1 | 2025-01 | `m2025.r1v1.deepseek-r1.math500.pass1` |
| GPQA Diamond | 78.3 | o1-preview | cons@64 | 2024-09 | `m2024.o1blog.o1-preview.gpqa-diamond.cons64` |
| SWE-bench Verified | 63.8 | Gemini 2.5 Pro (Experimental 03-25) | custom agent setup | 2025-03 | `m2025.gemini25-blog.gemini-2.5-pro.swebench.custom-agent` |
| AIME 2024 | 93.3 | Grok 3 (Think) [chart code GROK_3_R] | chart scoreMax (inferred highest test-time compute; the prose states cons@64 only for AIME 2025) | 2025-02 | `m2025.grok3-blog.grok-3-think.aime24.max` |
| AIME 2025 | 93.3 | Grok 3 (Think) | cons@64 | 2025-02 | `m2025.grok3-blog.grok-3-think.aime25.cons64.prose` |

## 2025-04

**April 2025.** 25 verified scores for 12 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-4.1 | AIME 2024 | appendix table | 48.1 | OpenAI (GPT-4.1 launch post, Apr 14 2025, appendix) | [openai_gpt41_blog](https://web.archive.org/web/20250414172812id_/https://openai.com/index/gpt-4-1/) html | `m2025.gpt41-blog.gpt-4.1.aime24` |
| GPT-4.1 | GPQA Diamond | model-based answer extraction (footnote 1) | 66.3 | OpenAI (GPT-4.1 launch post, Apr 14 2025, appendix) | [openai_gpt41_blog](https://web.archive.org/web/20250414172812id_/https://openai.com/index/gpt-4-1/) html | `m2025.gpt41-blog.gpt-4.1.gpqa` |
| GPT-4.1 | MMLU | appendix table | 90.2 | OpenAI (GPT-4.1 launch post, Apr 14 2025, appendix) | [openai_gpt41_blog](https://web.archive.org/web/20250414172812id_/https://openai.com/index/gpt-4-1/) html | `m2025.gpt41-blog.gpt-4.1.mmlu` |
| GPT-4.1 | SWE-bench Verified (477 of 500 tasks) | 23/500 tasks omitted (footnote 2) | 54.6 | OpenAI (GPT-4.1 launch post, Apr 14 2025, appendix) | [openai_gpt41_blog](https://web.archive.org/web/20250414172812id_/https://openai.com/index/gpt-4-1/) html | `m2025.gpt41-blog.gpt-4.1.swebench` |
| Llama 4 Maverick (instruction tuned) | GPQA Diamond | 0-shot, accuracy | 69.8 | Meta (Llama 4 MODEL_CARD.md, llama-models commit 038acb9) | [meta_llama4_model_card_038acb9](https://raw.githubusercontent.com/meta-llama/llama-models/038acb9fe1e1ddc5cf1b3989fb07b311a0ffcae4/models/llama4/MODEL_CARD.md) html | `m2025.llama4-card.llama-4-maverick.gpqa` |
| Llama 4 Maverick (instruction tuned) | MMLU-Pro | 0-shot, macro_avg/acc | 80.5 | Meta (Llama 4 MODEL_CARD.md, llama-models commit 038acb9) | [meta_llama4_model_card_038acb9](https://raw.githubusercontent.com/meta-llama/llama-models/038acb9fe1e1ddc5cf1b3989fb07b311a0ffcae4/models/llama4/MODEL_CARD.md) html | `m2025.llama4-card.llama-4-maverick.mmlu-pro` |
| OpenAI o3 (high) | MMMLU (14-language average) | reasoning effort high | 88.8 | OpenAI (gpt-oss Model Card, Table 2) | [arxiv_2508.10925](https://arxiv.org/pdf/2508.10925v1) p.10 | `m2025.gpt-oss.o3-high.mmmlu-avg` |
| Qwen3-235B-A22B (Non-thinking) | MATH-500 | non-thinking mode | 91.2 | Alibaba Qwen (Qwen3 TR, Table 12) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.qwen3-235b-nothink.math500` |
| Qwen3-235B-A22B (Thinking) | AIME 2024 | thinking mode | 85.7 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.qwen3-235b-think.aime24` |
| Qwen3-235B-A22B (Thinking) | AIME 2025 | thinking mode | 81.5 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.qwen3-235b-think.aime25` |
| Qwen3-235B-A22B (Thinking) | GPQA Diamond | thinking mode | 71.1 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.qwen3-235b-think.gpqa` |
| Qwen3-235B-A22B (Thinking) | LiveCodeBench v5 | thinking mode | 70.7 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.qwen3-235b-think.lcb-v5` |
| Qwen3-235B-A22B (Thinking) | MATH-500 | thinking mode | 98.0 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.qwen3-235b-think.math500` |
| Qwen3-235B-A22B (Thinking) | MMLU-Redux | thinking mode | 92.7 | Alibaba Qwen (Qwen3 TR, Table 11) | [arxiv_2505.09388](https://arxiv.org/pdf/2505.09388v1) p.14 | `m2025.qwen3.qwen3-235b-think.mmlu-redux` |
| gpt-4.1-2025-04-14 | HumanEval | 0-shot CoT, assistant system prompt | 94.5 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.gpt-4.1.humaneval` |
| o3 | SWE-bench Verified | launch chart | 69.1 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o3.swebench` |
| o3 (no tools) | AIME 2024 | no tools | 91.6 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o3.aime24.notools` |
| o3 (no tools) | AIME 2025 | no tools | 88.9 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o3.aime25.notools` |
| o3 (no tools) | GPQA Diamond | no tools | 83.3 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o3.gpqa.notools` |
| o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | MMLU | 0-shot CoT, no tools | 92.9 | OpenAI (simple-evals README, commit 6ead091, 2025-07-09) | [openai_simple_evals_readme](https://raw.githubusercontent.com/openai/simple-evals/6ead091ad8e120d82d08ca67b7dbe9cc4629987d/README.md) md | `m2025.simple-evals.o3.mmlu` |
| o4-mini | SWE-bench Verified | launch chart | 68.1 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o4-mini.swebench` |
| o4-mini (no tools) | AIME 2024 | no tools | 93.4 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o4-mini.aime24.notools` |
| o4-mini (no tools) | AIME 2025 | no tools | 92.7 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o4-mini.aime25.notools` |
| o4-mini (no tools) | GPQA Diamond | no tools | 81.4 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o4-mini.gpqa.notools` |
| o4-mini (with python only) | AIME 2025 | with Python interpreter | 99.5 | OpenAI (o3 and o4-mini launch post, Apr 16 2025, chart data) | [openai_o3_o4mini_blog](https://web.archive.org/web/20250416170840id_/https://openai.com/index/introducing-o3-and-o4-mini/) html | `m2025.o3-blog.o4-mini.aime25.python` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 84.0 | DeepSeek-R1 | EM | 2025-01 | `m2025.r1v1.deepseek-r1.mmlu-pro.em` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 97.3 | DeepSeek-R1 | Pass@1 | 2025-01 | `m2025.r1v1.deepseek-r1.math500.pass1` |
| GPQA Diamond | 83.3 | o3 (no tools) | no tools | 2025-04 | `m2025.o3-blog.o3.gpqa.notools` |
| SWE-bench Verified | 69.1 | o3 | launch chart | 2025-04 | `m2025.o3-blog.o3.swebench` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 99.5 | o4-mini (with python only) | with Python interpreter | 2025-04 | `m2025.o3-blog.o4-mini.aime25.python` |

## 2025-05

**May 2025.** 19 verified scores for 5 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Opus 4 | GPQA Diamond | without extended thinking | 74.9 | Anthropic (Claude 4 launch post, May 22 2025) | [anthropic_claude4_blog](https://web.archive.org/web/20250522163841id_/https://www.anthropic.com/news/claude-4) html | `m2025.claude4-blog.claude-opus-4.gpqa.no-et` |
| Claude Opus 4 | MMMLU | without extended thinking | 87.4 | Anthropic (Claude 4 launch post, May 22 2025) | [anthropic_claude4_blog](https://web.archive.org/web/20250522163841id_/https://www.anthropic.com/news/claude-4) html | `m2025.claude4-blog.claude-opus-4.mmmlu.no-et` |
| Claude Opus 4 | SWE-bench Verified (full 500) | no extended thinking, bash + edit-tool scaffold | 72.5 | Anthropic (Claude 4 launch post, May 22 2025) | [anthropic_claude4_blog](https://web.archive.org/web/20250522163841id_/https://www.anthropic.com/news/claude-4) html | `m2025.claude4-blog.claude-opus-4.swebench` |
| Claude Opus 4 | SWE-bench Verified (full 500) | high compute: parallel attempts + scoring model | 79.4 | Anthropic (Claude 4 launch post, May 22 2025) | [anthropic_claude4_blog](https://web.archive.org/web/20250522163841id_/https://www.anthropic.com/news/claude-4) html | `m2025.claude4-blog.claude-opus-4.swebench.parallel` |
| Claude Sonnet 4 | MMMLU | without extended thinking | 85.4 | Anthropic (Claude 4 launch post, May 22 2025) | [anthropic_claude4_blog](https://web.archive.org/web/20250522163841id_/https://www.anthropic.com/news/claude-4) html | `m2025.claude4-blog.claude-sonnet-4.mmmlu.no-et` |
| Claude Sonnet 4 | SWE-bench Verified (full 500) | no extended thinking, bash + edit-tool scaffold | 72.7 | Anthropic (Claude 4 launch post, May 22 2025) | [anthropic_claude4_blog](https://web.archive.org/web/20250522163841id_/https://www.anthropic.com/news/claude-4) html | `m2025.claude4-blog.claude-sonnet-4.swebench` |
| Claude Sonnet 4 | SWE-bench Verified (full 500) | high compute: parallel attempts + scoring model | 80.2 | Anthropic (Claude 4 launch post, May 22 2025) | [anthropic_claude4_blog](https://web.archive.org/web/20250522163841id_/https://www.anthropic.com/news/claude-4) html | `m2025.claude4-blog.claude-sonnet-4.swebench.parallel` |
| DeepSeek-R1-0528 | AIME 2024 | Pass@1 (16 samples) | 91.4 | DeepSeek (DeepSeek-R1-0528 Hugging Face model card) | [hf_deepseek_r1_0528_jun](https://web.archive.org/web/20250608210249id_/https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) html | `m2025.hf-r1-0528.deepseek-r1-0528.aime24` |
| DeepSeek-R1-0528 | AIME 2025 | Pass@1 (16 samples) | 87.5 | DeepSeek (DeepSeek-R1-0528 Hugging Face model card) | [hf_deepseek_r1_0528_jun](https://web.archive.org/web/20250608210249id_/https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) html | `m2025.hf-r1-0528.deepseek-r1-0528.aime25` |
| DeepSeek-R1-0528 | GPQA Diamond | Pass@1 (16 samples) | 81.0 | DeepSeek (DeepSeek-R1-0528 Hugging Face model card) | [hf_deepseek_r1_0528_jun](https://web.archive.org/web/20250608210249id_/https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) html | `m2025.hf-r1-0528.deepseek-r1-0528.gpqa` |
| DeepSeek-R1-0528 | LiveCodeBench (2408-2505) | Pass@1 | 73.3 | DeepSeek (DeepSeek-R1-0528 Hugging Face model card) | [hf_deepseek_r1_0528_jun](https://web.archive.org/web/20250608210249id_/https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) html | `m2025.hf-r1-0528.deepseek-r1-0528.lcb` |
| DeepSeek-R1-0528 | MMLU-Pro | EM | 85.0 | DeepSeek (DeepSeek-R1-0528 Hugging Face model card) | [hf_deepseek_r1_0528_jun](https://web.archive.org/web/20250608210249id_/https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) html | `m2025.hf-r1-0528.deepseek-r1-0528.mmlu-pro` |
| DeepSeek-R1-0528 | MMLU-Redux | EM | 93.4 | DeepSeek (DeepSeek-R1-0528 Hugging Face model card) | [hf_deepseek_r1_0528_jun](https://web.archive.org/web/20250608210249id_/https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) html | `m2025.hf-r1-0528.deepseek-r1-0528.mmlu-redux` |
| DeepSeek-R1-0528 | SWE-bench Verified | Resolved, Agentless framework (card note: 'We use Agentless framework to evaluate model performance on SWE-Verified') | 57.6 | DeepSeek (DeepSeek-R1-0528 Hugging Face model card) | [hf_deepseek_r1_0528_jun](https://web.archive.org/web/20250608210249id_/https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) html | `m2025.hf-r1-0528.deepseek-r1-0528.swebench` |
| Vicuna-13b | HumanEval | pass@1 | 12.5 | Microsoft (WizardLM v3, May 2025) | [arxiv_2304.12244v3](https://arxiv.org/pdf/2304.12244v3) p.7 | `m2023.xu2023v3.vicuna-13b.humaneval` |
| Vicuna-13b | MMLU | OpenLLM harness (shots not stated) | 50.84 | Microsoft (WizardLM v3, May 2025) | [arxiv_2304.12244v3](https://arxiv.org/pdf/2304.12244v3) p.7 | `m2023.xu2023v3.vicuna-13b.mmlu` |
| WizardLM-13b | GSM8K | 4-shot, pass@1 | 37.15 | Microsoft (WizardLM v3, May 2025) | [arxiv_2304.12244v3](https://arxiv.org/pdf/2304.12244v3) p.7 | `m2023.xu2023v3.wizardlm-13b.gsm8k` |
| WizardLM-13b | HumanEval | pass@1 | 24.0 | Microsoft (WizardLM v3, May 2025) | [arxiv_2304.12244v3](https://arxiv.org/pdf/2304.12244v3) p.7 | `m2023.xu2023v3.wizardlm-13b.humaneval` |
| WizardLM-13b | MMLU | OpenLLM harness (shots not stated) | 52.92 | Microsoft (WizardLM v3, May 2025) | [arxiv_2304.12244v3](https://arxiv.org/pdf/2304.12244v3) p.7 | `m2023.xu2023v3.wizardlm-13b.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 85.0 | DeepSeek-R1-0528 | EM | 2025-05 | `m2025.hf-r1-0528.deepseek-r1-0528.mmlu-pro` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.0 | Qwen3-235B-A22B (Thinking) | thinking mode | 2025-05 | `m2025.qwen3.qwen3-235b-think.math500` |
| GPQA Diamond | 84.0 | Gemini2.5-Pro | as reported by Qwen | 2025-05 | `m2025.qwen3.gemini-2.5-pro.gpqa` |
| SWE-bench Verified | 80.2 | Claude Sonnet 4 | high compute: parallel attempts + scoring model | 2025-05 | `m2025.claude4-blog.claude-sonnet-4.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 99.5 | o4-mini (with python only) | with Python interpreter | 2025-04 | `m2025.o3-blog.o4-mini.aime25.python` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Qwen3 Technical Report, v1, PDF page 14](https://arxiv.org/pdf/2505.09388v1#page=14): Table 11: Comparison among Qwen3-235B-A22B (Thinking) and other reasoning baselines.; Table 12: Comparison among Qwen3-235B-A22B (Non-thinking) and other non-reasoning baselines.

## 2025-06

**June 2025.** 12 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Gemini 2.5 Pro | AIME 2025 | single attempt | 88.0 | Google (Gemini 2.5 TR v1, Table 4) | [arxiv_2507.06261](https://arxiv.org/pdf/2507.06261v1) p.14 | `m2025.gemini25-tr.gemini-2.5-pro.aime25` |
| Gemini 2.5 Pro | GPQA Diamond | single attempt | 86.4 | Google (Gemini 2.5 TR v1, Table 4) | [arxiv_2507.06261](https://arxiv.org/pdf/2507.06261v1) p.14 | `m2025.gemini25-tr.gemini-2.5-pro.gpqa` |
| Gemini 2.5 Pro | Global MMLU (Lite) | Table 3 | 89.2 | Google (Gemini 2.5 TR v1, Table 3) | [arxiv_2507.06261](https://arxiv.org/pdf/2507.06261v1) p.13 | `m2025.gemini25-tr.gemini-2.5-pro.global-mmlu-lite` |
| Gemini 2.5 Pro | LiveCodeBench | Table 4 | 74.2 | Google (Gemini 2.5 TR v1, Table 4) | [arxiv_2507.06261](https://arxiv.org/pdf/2507.06261v1) p.14 | `m2025.gemini25-tr.gemini-2.5-pro.lcb` |
| Gemini 2.5 Pro | SWE-bench Verified | multiple attempts | 67.2 | Google (Gemini 2.5 TR v1, Table 4) | [arxiv_2507.06261](https://arxiv.org/pdf/2507.06261v1) p.14 | `m2025.gemini25-tr.gemini-2.5-pro.swebench.multi` |
| Gemini 2.5 Pro | SWE-bench Verified | single attempt | 59.6 | Google (Gemini 2.5 TR v1, Table 4) | [arxiv_2507.06261](https://arxiv.org/pdf/2507.06261v1) p.14 | `m2025.gemini25-tr.gemini-2.5-pro.swebench.single` |
| Magistral Medium | LiveCodeBench v5 | average over 16 runs | 59.4 | Mistral AI (Magistral TR, Table 2) | [arxiv_2506.10910](https://arxiv.org/pdf/2506.10910v1) p.9 | `m2025.magistral.magistral-medium.lcb-v5` |
| MiniMax-M1-80k | AIME 2024 | 80K thinking budget | 86.0 | MiniMax (MiniMax-M1 TR v1, Table 2) | [arxiv_2506.13585](https://arxiv.org/pdf/2506.13585v1) p.13 | `m2025.minimax-m1.minimax-m1-80k.aime24` |
| MiniMax-M1-80k | GPQA Diamond | 80K thinking budget | 70.0 | MiniMax (MiniMax-M1 TR v1, Table 2) | [arxiv_2506.13585](https://arxiv.org/pdf/2506.13585v1) p.13 | `m2025.minimax-m1.minimax-m1-80k.gpqa` |
| MiniMax-M1-80k | LiveCodeBench (24/8-25/5) | 80K thinking budget | 65.0 | MiniMax (MiniMax-M1 TR v1, Table 2) | [arxiv_2506.13585](https://arxiv.org/pdf/2506.13585v1) p.13 | `m2025.minimax-m1.minimax-m1-80k.lcb` |
| MiniMax-M1-80k | MATH-500 | 80K thinking budget | 96.8 | MiniMax (MiniMax-M1 TR v1, Table 2) | [arxiv_2506.13585](https://arxiv.org/pdf/2506.13585v1) p.13 | `m2025.minimax-m1.minimax-m1-80k.math500` |
| MiniMax-M1-80k | MMLU-Pro | 80K thinking budget | 81.1 | MiniMax (MiniMax-M1 TR v1, Table 2) | [arxiv_2506.13585](https://arxiv.org/pdf/2506.13585v1) p.13 | `m2025.minimax-m1.minimax-m1-80k.mmlu-pro` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.3 | o1 (Sept 2024 pre-release) | pass@1 | 2024-09 | `m2024.o1blog.o1.mmlu.pass1` |
| MMLU-Pro | 85.0 | DeepSeek-R1-0528 | EM | 2025-05 | `m2025.hf-r1-0528.deepseek-r1-0528.mmlu-pro` |
| HumanEval | 93.7 | Claude 3.5 Sonnet (New) | 0-shot | 2024-10 | `m2024.c35oct.claude-3.5-sonnet-new.humaneval.0-shot` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.0 | Qwen3-235B-A22B (Thinking) | thinking mode | 2025-05 | `m2025.qwen3.qwen3-235b-think.math500` |
| GPQA Diamond | 84.0 | Gemini2.5-Pro | as reported by Qwen | 2025-05 | `m2025.qwen3.gemini-2.5-pro.gpqa` |
| SWE-bench Verified | 80.2 | Claude Sonnet 4 | high compute: parallel attempts + scoring model | 2025-05 | `m2025.claude4-blog.claude-sonnet-4.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 99.5 | o4-mini (with python only) | with Python interpreter | 2025-04 | `m2025.o3-blog.o4-mini.aime25.python` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Magistral, v1, PDF page 10](https://arxiv.org/pdf/2506.10910v1#page=10): Table 3: Performance of Magistral Small compared with different training setups across various bench-.; Table 4: Magistral Medium's pass@1 performance on multilingual versions of the AIME 2024 benchmark.; Table 5: Cross-domain generalization during math-only and code-only RL for a 24B model.

## 2025-07

**July 2025.** 17 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GLM-4.5 | LiveCodeBench (2407-2501) | GLM evaluation | 72.9 | Zhipu AI (GLM-4.5 TR, Table 4) | [arxiv_2508.06471](https://arxiv.org/pdf/2508.06471v1) p.16 | `m2025.glm45.glm-4.5.lcb` |
| GLM-4.5 | MATH-500 | GLM evaluation | 98.2 | Zhipu AI (GLM-4.5 TR, Table 4) | [arxiv_2508.06471](https://arxiv.org/pdf/2508.06471v1) p.16 | `m2025.glm45.glm-4.5.math500` |
| GLM-4.5 | MMLU-Pro | GLM evaluation | 84.6 | Zhipu AI (GLM-4.5 TR, Table 4) | [arxiv_2508.06471](https://arxiv.org/pdf/2508.06471v1) p.16 | `m2025.glm45.glm-4.5.mmlu-pro` |
| Grok 4 | MMLU-Pro | as evaluated/reported by Zhipu | 86.6 | Zhipu AI (GLM-4.5 TR, Table 4) | [arxiv_2508.06471](https://arxiv.org/pdf/2508.06471v1) p.16 | `m2025.glm45.grok-4.mmlu-pro` |
| Grok 4 (no tools) [chart code GROK_4_NT] | AIME 2025 | no tools | 91.7 | xAI (Grok 4 launch post, Jul 9 2025, chart data) | [xai_grok4_blog](https://web.archive.org/web/20250711220811id_/https://x.ai/news/grok-4) html | `m2025.grok4-blog.grok-4.aime25.notools` |
| Grok 4 (no tools) [chart code GROK_4_NT] | GPQA | no tools | 87.5 | xAI (Grok 4 launch post, Jul 9 2025, chart data) | [xai_grok4_blog](https://web.archive.org/web/20250711220811id_/https://x.ai/news/grok-4) html | `m2025.grok4-blog.grok-4.gpqa.notools` |
| Grok 4 (no tools) [chart code GROK_4_NT] | LiveCodeBench (Jan-May) | no tools | 79.0 | xAI (Grok 4 launch post, Jul 9 2025, chart data) | [xai_grok4_blog](https://web.archive.org/web/20250711220811id_/https://x.ai/news/grok-4) html | `m2025.grok4-blog.grok-4.lcb.notools` |
| Grok 4 Heavy [chart code GROK_4_HEAVY] | AIME 2025 | with tools (Python) | 100.0 | xAI (Grok 4 launch post, Jul 9 2025, chart data) | [xai_grok4_blog](https://web.archive.org/web/20250711220811id_/https://x.ai/news/grok-4) html | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |
| Grok 4 Heavy [chart code GROK_4_HEAVY] | GPQA | with tools | 88.4 | xAI (Grok 4 launch post, Jul 9 2025, chart data) | [xai_grok4_blog](https://web.archive.org/web/20250711220811id_/https://x.ai/news/grok-4) html | `m2025.grok4-blog.grok-4-heavy.gpqa.tools` |
| Grok 4 Heavy [chart code GROK_4_HEAVY] | LiveCodeBench (Jan-May) | with tools | 79.4 | xAI (Grok 4 launch post, Jul 9 2025, chart data) | [xai_grok4_blog](https://web.archive.org/web/20250711220811id_/https://x.ai/news/grok-4) html | `m2025.grok4-blog.grok-4-heavy.lcb.tools` |
| Kimi-K2-Instruct | MATH-500 | Acc. | 97.4 | Moonshot AI (Kimi K2 TR, Table 3) | [arxiv_2507.20534](https://arxiv.org/pdf/2507.20534v2) p.16 | `m2025.kimi-k2.kimi-k2-instruct.math500` |
| Kimi-K2-Instruct | MMLU | EM | 89.5 | Moonshot AI (Kimi K2 TR, Table 3) | [arxiv_2507.20534](https://arxiv.org/pdf/2507.20534v2) p.16 | `m2025.kimi-k2.kimi-k2-instruct.mmlu` |
| Kimi-K2-Instruct | MMLU-Pro | EM | 81.1 | Moonshot AI (Kimi K2 TR, Table 3) | [arxiv_2507.20534](https://arxiv.org/pdf/2507.20534v2) p.16 | `m2025.kimi-k2.kimi-k2-instruct.mmlu-pro` |
| Qwen3-235B-A22B-Thinking-2507 | AIME 2025 | model card table | 92.3 | Alibaba Qwen (Qwen3-235B-A22B-Thinking-2507 Hugging Face model card) | [hf_qwen3_235b_thinking_2507](https://web.archive.org/web/20250725103434id_/https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) html | `m2025.hf-qwen3-2507.qwen3-235b-thinking-2507.aime25` |
| Qwen3-235B-A22B-Thinking-2507 | GPQA | model card table | 81.1 | Alibaba Qwen (Qwen3-235B-A22B-Thinking-2507 Hugging Face model card) | [hf_qwen3_235b_thinking_2507](https://web.archive.org/web/20250725103434id_/https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) html | `m2025.hf-qwen3-2507.qwen3-235b-thinking-2507.gpqa` |
| Qwen3-235B-A22B-Thinking-2507 | LiveCodeBench v6 (25.02-25.05) | model card table | 74.1 | Alibaba Qwen (Qwen3-235B-A22B-Thinking-2507 Hugging Face model card) | [hf_qwen3_235b_thinking_2507](https://web.archive.org/web/20250725103434id_/https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) html | `m2025.hf-qwen3-2507.qwen3-235b-thinking-2507.lcb-v6` |
| Qwen3-235B-A22B-Thinking-2507 | MMLU-Pro | model card table | 84.4 | Alibaba Qwen (Qwen3-235B-A22B-Thinking-2507 Hugging Face model card) | [hf_qwen3_235b_thinking_2507](https://web.archive.org/web/20250725103434id_/https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) html | `m2025.hf-qwen3-2507.qwen3-235b-thinking-2507.mmlu-pro` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 85.0 | DeepSeek-R1-0528 | EM | 2025-05 | `m2025.hf-r1-0528.deepseek-r1-0528.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.0 | Qwen3-235B-A22B (Thinking) | thinking mode | 2025-05 | `m2025.qwen3.qwen3-235b-think.math500` |
| GPQA Diamond | 86.4 | Gemini 2.5 Pro | single attempt | 2025-07 | `m2025.gemini25-tr.gemini-2.5-pro.gpqa` |
| SWE-bench Verified | 80.2 | Claude Sonnet 4 | high compute: parallel attempts + scoring model | 2025-05 | `m2025.claude4-blog.claude-sonnet-4.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Kimi K2: Open Agentic Intelligence, v2, PDF page 1](https://arxiv.org/pdf/2507.20534v2#page=1): Figure 1: Kimi K2 main results.2.

## 2025-08

**August 2025.** 13 verified scores for 8 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Opus 4.1 | SWE-bench Verified | no extended thinking; simple two-tool scaffold (bash + string-replace file editor); full 500 problems | 74.5 | Anthropic (Claude Opus 4.1 post, Aug 5 2025) | [anthropic_claude_opus41_blog](https://web.archive.org/web/20250805162827id_/https://www.anthropic.com/news/claude-opus-4-1) html | `m2025.opus41-blog.claude-opus-4.1.swebench` |
| DeepSeek V3.1-NonThinking | SWE-bench Verified | agent mode | 66.0 | DeepSeek (DeepSeek-V3.1 Hugging Face model card) | [hf_deepseek_v31](https://web.archive.org/web/20250825140737id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.1) html | `m2025.hf-v31.deepseek-v3.1-nonthinking.swebench` |
| DeepSeek V3.1-Thinking | AIME 2025 | Pass@1 | 88.4 | DeepSeek (DeepSeek-V3.1 Hugging Face model card) | [hf_deepseek_v31](https://web.archive.org/web/20250825140737id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.1) html | `m2025.hf-v31.deepseek-v3.1-thinking.aime25` |
| DeepSeek V3.1-Thinking | GPQA Diamond | Pass@1 | 80.1 | DeepSeek (DeepSeek-V3.1 Hugging Face model card) | [hf_deepseek_v31](https://web.archive.org/web/20250825140737id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.1) html | `m2025.hf-v31.deepseek-v3.1-thinking.gpqa` |
| DeepSeek V3.1-Thinking | LiveCodeBench (2408-2505) | Pass@1 | 74.8 | DeepSeek (DeepSeek-V3.1 Hugging Face model card) | [hf_deepseek_v31](https://web.archive.org/web/20250825140737id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.1) html | `m2025.hf-v31.deepseek-v3.1-thinking.lcb` |
| DeepSeek V3.1-Thinking | MMLU-Pro | EM | 84.8 | DeepSeek (DeepSeek-V3.1 Hugging Face model card) | [hf_deepseek_v31](https://web.archive.org/web/20250825140737id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.1) html | `m2025.hf-v31.deepseek-v3.1-thinking.mmlu-pro` |
| GPT-5 (thinking) | AIME 2025 | without tools | 94.6 | OpenAI (GPT-5 launch post, Aug 7 2025) | [openai_gpt5_blog](https://web.archive.org/web/20250807174456id_/https://openai.com/index/introducing-gpt-5/) html | `m2025.gpt5-blog.gpt-5.aime25.notools` |
| GPT-5 (thinking) | SWE-bench Verified | launch prose | 74.9 | OpenAI (GPT-5 launch post, Aug 7 2025) | [openai_gpt5_blog](https://web.archive.org/web/20250807174456id_/https://openai.com/index/introducing-gpt-5/) html | `m2025.gpt5-blog.gpt-5.swebench` |
| GPT-5 pro | GPQA Diamond | without tools, extended reasoning | 88.4 | OpenAI (GPT-5 launch post, Aug 7 2025) | [openai_gpt5_blog](https://web.archive.org/web/20250807174456id_/https://openai.com/index/introducing-gpt-5/) html | `m2025.gpt5-blog.gpt-5-pro.gpqa.notools` |
| GPT-5 pro (no tools) | AIME 2025 | no tools | 96.7 | OpenAI (GPT-5 launch post, chart data) | [openai_gpt5_blog](https://web.archive.org/web/20250807174456id_/https://openai.com/index/introducing-gpt-5/) html | `m2025.gpt5-blog.gpt-5-pro.aime25.notools` |
| GPT-5 pro (python) | AIME 2025 | with Python tool | 100.0 | OpenAI (GPT-5 launch post, Aug 7 2025) chart data | [openai_gpt5_blog](https://web.archive.org/web/20250807174456id_/https://openai.com/index/introducing-gpt-5/) html | `m2025.gpt5-blog.gpt-5-pro.aime25.python` |
| gpt-oss-120b (high) | AIME 2025 | no tools, reasoning effort high | 92.5 | OpenAI (gpt-oss-120b & gpt-oss-20b Model Card, Table 3) | [arxiv_2508.10925](https://arxiv.org/pdf/2508.10925v1) p.11 | `m2025.gpt-oss.gpt-oss-120b-high.aime25.notools` |
| gpt-oss-120b (high) | MMLU | reasoning effort high | 90.0 | OpenAI (gpt-oss-120b & gpt-oss-20b Model Card, Table 3) | [arxiv_2508.10925](https://arxiv.org/pdf/2508.10925v1) p.11 | `m2025.gpt-oss.gpt-oss-120b-high.mmlu` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 86.6 | Grok 4 | as evaluated/reported by Zhipu | 2025-08 | `m2025.glm45.grok-4.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 88.4 | GPT-5 pro | without tools, extended reasoning | 2025-08 | `m2025.gpt5-blog.gpt-5-pro.gpqa.notools` |
| SWE-bench Verified | 80.2 | Claude Sonnet 4 | high compute: parallel attempts + scoring model | 2025-05 | `m2025.claude4-blog.claude-sonnet-4.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models, v1, PDF page 16](https://arxiv.org/pdf/2508.06471v1#page=16): Figure 11: One example of user prompt we used for TAU-bench.; Table 4: Results on Reasoning Benchmarks.; Table 5: Results on SWE-bench Verified and Terminal-Bench.
- [gpt-oss-120b &amp; gpt-oss-20b Model Card, v1, PDF page 6](https://arxiv.org/pdf/2508.10925v1#page=6): Figure 1: Main capabilities evaluations.

## 2025-09

**September 2025.** 12 verified scores for 4 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Sonnet 4.5 | SWE-bench Verified (full 500) | 10-trial average, no test-time compute, 200K thinking budget, two-tool scaffold | 77.2 | Anthropic (Claude Sonnet 4.5 launch post, Sep 29 2025, methodology) | [anthropic_claude_sonnet45_blog](https://web.archive.org/web/20250929165916id_/https://www.anthropic.com/news/claude-sonnet-4-5) html | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench` |
| Claude Sonnet 4.5 | SWE-bench Verified (full 500) | high compute: parallel attempts + scoring model | 82.0 | Anthropic (Claude Sonnet 4.5 launch post, Sep 29 2025, methodology) | [anthropic_claude_sonnet45_blog](https://web.archive.org/web/20250929165916id_/https://www.anthropic.com/news/claude-sonnet-4-5) html | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| Claude Sonnet 4.5 (Thinking) | AIME 2025 | no tools; non-asterisked baseline 'quoted from' the list of public sources in footnote 3.1 (GPT-5 post, GPT-5 for Developers, GPT-5 system card, claude-sonnet-4-5 post, grok-4 post, deepseek-v3.2 post, Terminal-Bench and Vals AI leaderboards, artificialanalysis); per-cell source not stated | 87.0 | Moonshot AI (Kimi-K2-Thinking Hugging Face model card) | [hf_kimi_k2_thinking](https://web.archive.org/web/20251106153010id_/https://huggingface.co/moonshotai/Kimi-K2-Thinking) html | `m2025.hf-k2-thinking.claude-sonnet-4.5.aime25.notools` |
| Claude Sonnet 4.5 (Thinking) | AIME 2025 | with Python; non-asterisked baseline quoted from the public sources listed in footnote 3.1; per-cell source not stated | 100.0 | Moonshot AI (Kimi-K2-Thinking Hugging Face model card) | [hf_kimi_k2_thinking](https://web.archive.org/web/20251106153010id_/https://huggingface.co/moonshotai/Kimi-K2-Thinking) html | `m2025.hf-k2-thinking.claude-sonnet-4.5.aime25.python` |
| DeepSeek-V3.2-Exp | AIME 2025 | reasoning mode, without tool use | 89.3 | DeepSeek (DeepSeek-V3.2-Exp Hugging Face model card) | [hf_deepseek_v32_exp](https://web.archive.org/web/20250929100447id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) html | `m2025.hf-v32exp.deepseek-v3.2-exp.aime25` |
| DeepSeek-V3.2-Exp | GPQA Diamond | reasoning mode, without tool use | 79.9 | DeepSeek (DeepSeek-V3.2-Exp Hugging Face model card) | [hf_deepseek_v32_exp](https://web.archive.org/web/20250929100447id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) html | `m2025.hf-v32exp.deepseek-v3.2-exp.gpqa` |
| DeepSeek-V3.2-Exp | LiveCodeBench | reasoning mode, without tool use | 74.1 | DeepSeek (DeepSeek-V3.2-Exp Hugging Face model card) | [hf_deepseek_v32_exp](https://web.archive.org/web/20250929100447id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) html | `m2025.hf-v32exp.deepseek-v3.2-exp.lcb` |
| DeepSeek-V3.2-Exp | MMLU-Pro | reasoning mode, without tool use | 85.0 | DeepSeek (DeepSeek-V3.2-Exp Hugging Face model card) | [hf_deepseek_v32_exp](https://web.archive.org/web/20250929100447id_/https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) html | `m2025.hf-v32exp.deepseek-v3.2-exp.mmlu-pro` |
| GLM-4.6 | AIME 2025 | as reported by Z.ai | 93.9 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.6.aime25` |
| GLM-4.6 | LiveCodeBench v6 | as reported by Z.ai | 82.8 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.6.lcb-v6` |
| GLM-4.6 | MMLU-Pro | as reported by Z.ai | 83.2 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.6.mmlu-pro` |
| GLM-4.6 | SWE-bench Verified | as reported by Z.ai | 68.0 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.6.swebench` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 86.6 | Grok 4 | as evaluated/reported by Zhipu | 2025-08 | `m2025.glm45.grok-4.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 88.4 | GPT-5 pro | without tools, extended reasoning | 2025-08 | `m2025.gpt5-blog.gpt-5-pro.gpqa.notools` |
| SWE-bench Verified | 82.0 | Claude Sonnet 4.5 | high compute: parallel attempts + scoring model | 2025-09 | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2025-10

**October 2025.** 1 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Haiku 4.5 | SWE-bench Verified (full 500) | 50-trial average, no test-time compute, 128K thinking budget, default sampling, full 500 problems, two-tool scaffold, WITH a prompt addition ('You should use tools as much as possible, ideally more than 100 times...') | 73.3 | Anthropic (Claude Haiku 4.5 post, Oct 15 2025, methodology) | [anthropic_claude_haiku45_blog](https://web.archive.org/web/20251015170339id_/https://www.anthropic.com/news/claude-haiku-4-5) html | `m2025.haiku45-blog.claude-haiku-4.5.swebench` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 86.6 | Grok 4 | as evaluated/reported by Zhipu | 2025-08 | `m2025.glm45.grok-4.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 88.4 | GPT-5 pro | without tools, extended reasoning | 2025-08 | `m2025.gpt5-blog.gpt-5-pro.gpqa.notools` |
| SWE-bench Verified | 82.0 | Claude Sonnet 4.5 | high compute: parallel attempts + scoring model | 2025-09 | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2025-11

**November 2025.** 19 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Opus 4.5 | AIME 2025 | extended thinking | 92.8 | Moonshot AI (Kimi K2.5 TR, Table 4) | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2025.kimi-k25.claude-opus-4.5.aime25` |
| Claude Opus 4.5 | GPQA Diamond | extended thinking | 87.0 | Moonshot AI (Kimi K2.5 TR, Table 4) | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2025.kimi-k25.claude-opus-4.5.gpqa` |
| Claude Opus 4.5 | MMLU-Pro | extended thinking; starred = Moonshot internal evaluation | 89.3 | Moonshot AI (Kimi K2.5 TR, Table 4) | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2025.kimi-k25.claude-opus-4.5.mmlu-pro` |
| Claude Opus 4.5 | SWE-bench Verified | extended thinking | 80.9 | Moonshot AI (Kimi K2.5 TR, Table 4) | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2025.kimi-k25.claude-opus-4.5.swebench` |
| GPT-5.1 Thinking | AIME 2025 | no tools, high effort | 94.0 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.1-thinking.aime25.notools` |
| GPT-5.1 Thinking | GPQA Diamond | no tools, high effort | 88.1 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.1-thinking.gpqa.notools` |
| GPT-5.1 Thinking | MMMLU | high effort | 89.5 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.1-thinking.mmmlu` |
| GPT-5.1 Thinking | SWE-bench Verified | high effort | 76.3 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.1-thinking.swebench` |
| Gemini 3 Deep Think | GPQA Diamond | launch prose (Deep Think mode) | 93.8 | Google (Gemini 3 launch post, Nov 18 2025) | [google_gemini3_blog](https://web.archive.org/web/20251118160715id_/https://blog.google/products/gemini/gemini-3/) html | `m2025.gemini3-blog.gemini-3-deep-think.gpqa` |
| Gemini 3 Pro | GPQA Diamond | launch prose | 91.9 | Google (Gemini 3 launch post, Nov 18 2025) | [google_gemini3_blog](https://web.archive.org/web/20251118160715id_/https://blog.google/products/gemini/gemini-3/) html | `m2025.gemini3-blog.gemini-3-pro.gpqa` |
| Gemini 3 Pro | SWE-bench Verified | launch prose | 76.2 | Google (Gemini 3 launch post, Nov 18 2025) | [google_gemini3_blog](https://web.archive.org/web/20251118160715id_/https://blog.google/products/gemini/gemini-3/) html | `m2025.gemini3-blog.gemini-3-pro.swebench` |
| Gemini-3.0 Pro | AIME 2025 | Pass@1 | 95.0 | DeepSeek (DeepSeek-V3.2 TR, Table 2) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.13 | `m2025.dsv32.gemini-3-pro.aime25` |
| Gemini-3.0 Pro | LiveCodeBench | Pass@1-COT | 90.7 | DeepSeek (DeepSeek-V3.2 TR, Table 2) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.13 | `m2025.dsv32.gemini-3-pro.lcb` |
| Gemini-3.0 Pro | MMLU-Pro | EM | 90.1 | DeepSeek (DeepSeek-V3.2 TR, Table 2) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.13 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| Kimi K2 Thinking | AIME 2025 | no tools, avg@32 | 94.5 | Moonshot AI (Kimi-K2-Thinking Hugging Face model card) | [hf_kimi_k2_thinking](https://web.archive.org/web/20251106153010id_/https://huggingface.co/moonshotai/Kimi-K2-Thinking) html | `m2025.hf-k2-thinking.kimi-k2-thinking.aime25.notools` |
| Kimi K2 Thinking | AIME 2025 | with Python, avg@16 | 99.1 | Moonshot AI (Kimi-K2-Thinking Hugging Face model card) | [hf_kimi_k2_thinking](https://web.archive.org/web/20251106153010id_/https://huggingface.co/moonshotai/Kimi-K2-Thinking) html | `m2025.hf-k2-thinking.kimi-k2-thinking.aime25.python` |
| Kimi K2 Thinking | LiveCodeBench v6 | no tools; 128k thinking-token budget (2.2); in-house harness with rewritten system prompt, averaged over 5 runs (5.2-5.3) | 83.1 | Moonshot AI (Kimi-K2-Thinking Hugging Face model card) | [hf_kimi_k2_thinking](https://web.archive.org/web/20251106153010id_/https://huggingface.co/moonshotai/Kimi-K2-Thinking) html | `m2025.hf-k2-thinking.kimi-k2-thinking.lcb-v6` |
| Kimi K2 Thinking | MMLU-Pro | no tools | 84.6 | Moonshot AI (Kimi-K2-Thinking Hugging Face model card) | [hf_kimi_k2_thinking](https://web.archive.org/web/20251106153010id_/https://huggingface.co/moonshotai/Kimi-K2-Thinking) html | `m2025.hf-k2-thinking.kimi-k2-thinking.mmlu-pro` |
| Kimi K2 Thinking | SWE-bench Verified | with tools; in-house harness derived from SWE-agent with clamped Bash/Edit context and REWRITTEN system prompt; averaged over 5 runs (footnotes 5.2-5.3); INT4 | 71.3 | Moonshot AI (Kimi-K2-Thinking Hugging Face model card) | [hf_kimi_k2_thinking](https://web.archive.org/web/20251106153010id_/https://huggingface.co/moonshotai/Kimi-K2-Thinking) html | `m2025.hf-k2-thinking.kimi-k2-thinking.swebench` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 86.6 | Grok 4 | as evaluated/reported by Zhipu | 2025-08 | `m2025.glm45.grok-4.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 93.8 | Gemini 3 Deep Think | launch prose (Deep Think mode) | 2025-11 | `m2025.gemini3-blog.gemini-3-deep-think.gpqa` |
| SWE-bench Verified | 82.0 | Claude Sonnet 4.5 | high compute: parallel attempts + scoring model | 2025-09 | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2025-12

**December 2025.** 21 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| DeepSeek-V3.2 Thinking | AIME 2025 | Pass@1 | 93.1 | DeepSeek (DeepSeek-V3.2 TR, Table 2) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.13 | `m2025.dsv32.deepseek-v3.2.aime25` |
| DeepSeek-V3.2 Thinking | LiveCodeBench | Pass@1-COT | 83.3 | DeepSeek (DeepSeek-V3.2 TR, Table 2) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.13 | `m2025.dsv32.deepseek-v3.2.lcb` |
| DeepSeek-V3.2 Thinking | MMLU-Pro | EM | 85.0 | DeepSeek (DeepSeek-V3.2 TR, Table 2) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.13 | `m2025.dsv32.deepseek-v3.2.mmlu-pro` |
| DeepSeek-V3.2 Thinking | SWE-bench Verified | Resolved | 73.1 | DeepSeek (DeepSeek-V3.2 TR, Table 2) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.13 | `m2025.dsv32.deepseek-v3.2.swebench` |
| DeepSeek-V3.2-Speciale | AIME 2025 | Pass@1 | 96.0 | DeepSeek (DeepSeek-V3.2 TR, Table 3) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.15 | `m2025.dsv32.deepseek-v3.2-speciale.aime25` |
| DeepSeek-V3.2-Speciale | GPQA Diamond | Pass@1 | 85.7 | DeepSeek (DeepSeek-V3.2 TR, Table 3) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.15 | `m2025.dsv32.deepseek-v3.2-speciale.gpqa` |
| DeepSeek-V3.2-Speciale | LiveCodeBench | Pass@1-COT | 88.7 | DeepSeek (DeepSeek-V3.2 TR, Table 3) | [arxiv_2512.02556](https://arxiv.org/pdf/2512.02556v1) p.15 | `m2025.dsv32.deepseek-v3.2-speciale.lcb` |
| GLM-4.7 | AIME 2025 | as reported by Z.ai | 95.7 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.7.aime25` |
| GLM-4.7 | GPQA Diamond | as reported by Z.ai | 85.7 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.7.gpqa` |
| GLM-4.7 | LiveCodeBench v6 | as reported by Z.ai | 84.9 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.7.lcb-v6` |
| GLM-4.7 | MMLU-Pro | as reported by Z.ai | 84.3 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.7.mmlu-pro` |
| GLM-4.7 | SWE-bench Verified | as reported by Z.ai | 73.8 | Zhipu AI / Z.ai (GLM-4.7 launch post, table) | [zai_glm47_blog](https://web.archive.org/web/20251222173543id_/https://z.ai/blog/glm-4.7) html | `m2025.glm47-blog.glm-4.7.swebench` |
| GPT-5.2 Pro | AIME 2025 | no tools, xhigh effort | 100.0 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.2-pro.aime25.notools` |
| GPT-5.2 Pro | GPQA Diamond | no tools, xhigh effort | 93.2 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.2-pro.gpqa.notools` |
| GPT-5.2 Thinking | AIME 2025 | no tools, xhigh effort | 100.0 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.2-thinking.aime25.notools` |
| GPT-5.2 Thinking | FrontierMath Tier 1-3 | with Python, xhigh effort | 40.3 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.2-thinking.frontiermath-t1-3` |
| GPT-5.2 Thinking | GPQA Diamond | no tools, xhigh effort | 92.4 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.2-thinking.gpqa.notools` |
| GPT-5.2 Thinking | MMMLU | xhigh effort | 89.6 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.2-thinking.mmmlu` |
| GPT-5.2 Thinking | SWE-bench Verified | xhigh effort | 80.0 | OpenAI (GPT-5.2 launch post, Dec 11 2025) | [openai_gpt52_blog](https://web.archive.org/web/20251211192443id_/https://openai.com/index/introducing-gpt-5-2/) html | `m2025.gpt52-blog.gpt-5.2-thinking.swebench` |
| Gemini 3 Flash | GPQA Diamond | launch prose | 90.4 | Google (Gemini 3 Flash launch post, Dec 17 2025) | [google_gemini3_flash_blog](https://web.archive.org/web/20251217160641id_/https://blog.google/products/gemini/gemini-3-flash/) html | `m2025.gemini3flash-blog.gemini-3-flash.gpqa` |
| Gemini 3 Flash | SWE-bench Verified | launch prose | 78.0 | Google (Gemini 3 Flash launch post, Dec 17 2025) | [google_gemini3_flash_blog](https://web.archive.org/web/20251217160641id_/https://blog.google/products/gemini/gemini-3-flash/) html | `m2025.gemini3flash-blog.gemini-3-flash.swebench` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 93.8 | Gemini 3 Deep Think | launch prose (Deep Think mode) | 2025-11 | `m2025.gemini3-blog.gemini-3-deep-think.gpqa` |
| SWE-bench Verified | 82.0 | Claude Sonnet 4.5 | high compute: parallel attempts + scoring model | 2025-09 | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models, v1, PDF page 1](https://arxiv.org/pdf/2512.02556v1#page=1): Figure 1: Benchmark of DeepSeek-V3.2 and its counterparts.

## 2026-01

**January 2026.** 6 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Kimi K2.5 | AIME 2025 | Avg@64, max 96k completion tokens (appendix E) | 96.1 | Moonshot AI, Kimi K2.5 technical report (arXiv:2602.02276v2) Table 4 | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2026.kimi.kimi-k2-5.aime-2025.table4` |
| Kimi K2.5 | GPQA-Diamond | avg of 8 runs (appendix E) | 87.6 | Moonshot AI, Kimi K2.5 technical report (arXiv:2602.02276v2) Table 4 | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2026.kimi.kimi-k2-5.gpqa-diamond.table4` |
| Kimi K2.5 | LiveCodeBench v6 | Table 4; coding task averaged over 5 runs (Avg@5, appendix E.5); temperature 1.0, top-p 0.95; mode NOT stated | 85.0 | Moonshot AI, Kimi K2.5 technical report (arXiv:2602.02276v2) Table 4 | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2026.kimi.kimi-k2-5.livecodebench-v6.table4` |
| Kimi K2.5 | MMLU-Pro | Table 4, Kimi K2.5 general config (temperature 1.0, top-p 0.95, 256k context); thinking/instant mode NOT stated | 87.1 | Moonshot AI, Kimi K2.5 technical report (arXiv:2602.02276v2) Table 4 | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2026.kimi.kimi-k2-5.mmlu-pro.table4` |
| Kimi K2.5 | SWE-bench Verified | internal minimal-tool framework (bash, create_file, insert, view, str_replace, submit) with system prompts specifically tailored for repository-level code manipulation; non-thinking mode; Avg@5 | 76.8 | Moonshot AI, Kimi K2.5 technical report (arXiv:2602.02276v2) Table 4 | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2026.kimi.kimi-k2-5.swe-bench-verified.table4` |
| Kimi K2.5 | Terminal-Bench 2.0 | Terminus-2 framework with the provided JSON parser, NON-THINKING mode, Avg@5 | 50.8 | Moonshot AI, Kimi K2.5 technical report (arXiv:2602.02276v2) Table 4 | [arxiv_2602.02276](https://arxiv.org/pdf/2602.02276v2) p.12 | `m2026.kimi.kimi-k2-5.terminal-bench-2-0.table4` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 93.8 | Gemini 3 Deep Think | launch prose (Deep Think mode) | 2025-11 | `m2025.gemini3-blog.gemini-3-deep-think.gpqa` |
| SWE-bench Verified | 82.0 | Claude Sonnet 4.5 | high compute: parallel attempts + scoring model | 2025-09 | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-02

**February 2026.** 23 verified scores for 6 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Opus 4.6 | AIME 2025 | 5 trials, adaptive thinking, max effort, no tools; Anthropic flags possible contamination | 99.79 | Anthropic, Claude Opus 4.6 System Card (Feb 2026) | [anthropic_claude_opus46_system_card](https://web.archive.org/web/20260622141913id_/https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd/Claude%20Opus%204.6%20System%20Card.pdf) p.25 | `m2026.opus46card.claude-opus-4-6.aime-2025` |
| Claude Opus 4.6 | GPQA Diamond | 5 trials, adaptive thinking, max effort | 91.31 | Anthropic, Claude Opus 4.6 System Card (Feb 2026) | [anthropic_claude_opus46_system_card](https://web.archive.org/web/20260622141913id_/https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd/Claude%20Opus%204.6%20System%20Card.pdf) p.25 | `m2026.opus46card.claude-opus-4-6.gpqa-diamond` |
| Claude Opus 4.6 | MMMLU | 5 trials, all non-English pairings, adaptive thinking, max effort | 91.05 | Anthropic, Claude Opus 4.6 System Card (Feb 2026) | [anthropic_claude_opus46_system_card](https://web.archive.org/web/20260622141913id_/https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd/Claude%20Opus%204.6%20System%20Card.pdf) p.25 | `m2026.opus46card.claude-opus-4-6.mmmlu` |
| Claude Opus 4.6 | SWE-bench Verified | prompt-modified harness (non-standard) | 81.4 | Anthropic, Claude Opus 4.6 System Card (Feb 2026) | [anthropic_claude_opus46_system_card](https://web.archive.org/web/20260622141913id_/https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd/Claude%20Opus%204.6%20System%20Card.pdf) p.19 | `m2026.opus46card.claude-opus-4-6.swe-bench-verified.prompt-modified` |
| Claude Opus 4.6 | SWE-bench Verified | averaged over 25 trials, adaptive thinking, max effort, standard prompt | 80.84 | Anthropic, Claude Opus 4.6 System Card (Feb 2026) | [anthropic_claude_opus46_system_card](https://web.archive.org/web/20260622141913id_/https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd/Claude%20Opus%204.6%20System%20Card.pdf) p.19 | `m2026.opus46card.claude-opus-4-6.swe-bench-verified.standard` |
| Claude Sonnet 4.6 | GPQA Diamond | 10 trials | 89.9 | Anthropic, Claude Sonnet 4.6 System Card (Feb 17, 2026) | [anthropic_claude_sonnet46_system_card](https://web.archive.org/web/20260622121453id_/https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75/Claude%20Sonnet%204.6%20System%20Card.pdf) p.23 | `m2026.sonnet46card.claude-sonnet-4-6.gpqa-diamond` |
| Claude Sonnet 4.6 | MMMLU | 10 trials, all non-English pairings | 89.3 | Anthropic, Claude Sonnet 4.6 System Card (Feb 17, 2026) | [anthropic_claude_sonnet46_system_card](https://web.archive.org/web/20260622121453id_/https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75/Claude%20Sonnet%204.6%20System%20Card.pdf) p.23 | `m2026.sonnet46card.claude-sonnet-4-6.mmmlu` |
| Claude Sonnet 4.6 | SWE-bench Verified | prompt-modified harness (non-standard) | 80.2 | Anthropic, Claude Sonnet 4.6 System Card (Feb 17, 2026) | [anthropic_claude_sonnet46_system_card](https://web.archive.org/web/20260622121453id_/https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75/Claude%20Sonnet%204.6%20System%20Card.pdf) p.16 | `m2026.sonnet46card.claude-sonnet-4-6.swe-bench-verified.prompt-modified` |
| Claude Sonnet 4.6 | SWE-bench Verified | standard prompt | 79.6 | Anthropic, Claude Sonnet 4.6 System Card (Feb 17, 2026) | [anthropic_claude_sonnet46_system_card](https://web.archive.org/web/20260622121453id_/https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75/Claude%20Sonnet%204.6%20System%20Card.pdf) p.16 | `m2026.sonnet46card.claude-sonnet-4-6.swe-bench-verified.standard` |
| GLM-5 | AIME 2026 I | max generation length 131,072 tokens | 92.7 | Zhipu AI, GLM-5 technical report (arXiv:2602.15763v2) Table 7 | [arxiv_2602.15763](https://arxiv.org/pdf/2602.15763v2) p.23 | `m2026.glm5.glm-5.aime-2026-i.table7` |
| GLM-5 | GPQA-Diamond | max generation length 131,072 tokens | 86.0 | Zhipu AI, GLM-5 technical report (arXiv:2602.15763v2) Table 7 | [arxiv_2602.15763](https://arxiv.org/pdf/2602.15763v2) p.23 | `m2026.glm5.glm-5.gpqa-diamond.table7` |
| GLM-5 | SWE-bench Verified | OpenHands with tailored instruction prompt | 77.8 | Zhipu AI, GLM-5 technical report (arXiv:2602.15763v2) Table 7 | [arxiv_2602.15763](https://arxiv.org/pdf/2602.15763v2) p.23 | `m2026.glm5.glm-5.swe-bench-verified.table7` |
| GPT-5.3-Codex (xhigh) | SWE-Bench Pro (Public) | xhigh | 56.8 | OpenAI, Introducing GPT-5.3-Codex | [openai_gpt53codex_blog](https://web.archive.org/web/20260205194103id_/https://openai.com/index/introducing-gpt-5-3-codex/) html | `m2026.gpt53codex.gpt-5-3-codex.swe-bench-pro` |
| GPT-5.3-Codex (xhigh) | Terminal-Bench 2.0 | xhigh | 77.3 | OpenAI, Introducing GPT-5.3-Codex (Feb 5, 2026) | [openai_gpt53codex_blog](https://web.archive.org/web/20260205194103id_/https://openai.com/index/introducing-gpt-5-3-codex/) html | `m2026.gpt53codex.gpt-5-3-codex.terminal-bench-2-0` |
| Gemini 3.1 Pro | GPQA Diamond | Thinking (High), no tools | 94.3 | Google DeepMind, Gemini 3.1 Pro model card (published 19 Feb 2026) | [google_gemini31pro_model_card](https://web.archive.org/web/20260219160829id_/https://deepmind.google/models/model-cards/gemini-3-1-pro/) html | `m2026.g31card.gemini-3-1-pro.gpqa-diamond` |
| Gemini 3.1 Pro | MMMLU | Thinking (High) | 92.6 | Google DeepMind, Gemini 3.1 Pro model card (published 19 Feb 2026) | [google_gemini31pro_model_card](https://web.archive.org/web/20260219160829id_/https://deepmind.google/models/model-cards/gemini-3-1-pro/) html | `m2026.g31card.gemini-3-1-pro.mmmlu` |
| Gemini 3.1 Pro | SWE-bench Verified | Thinking (High), single attempt | 80.6 | Google DeepMind, Gemini 3.1 Pro model card (published 19 Feb 2026) | [google_gemini31pro_model_card](https://web.archive.org/web/20260219160829id_/https://deepmind.google/models/model-cards/gemini-3-1-pro/) html | `m2026.g31card.gemini-3-1-pro.swe-bench-verified` |
| Gemini 3.1 Pro | Terminal-Bench 2.0 | Thinking (High), Terminus-2 harness | 68.5 | Google DeepMind, Gemini 3.1 Pro model card (published 19 Feb 2026) | [google_gemini31pro_model_card](https://web.archive.org/web/20260219160829id_/https://deepmind.google/models/model-cards/gemini-3-1-pro/) html | `m2026.g31card.gemini-3-1-pro.terminal-bench-2-0` |
| Qwen3.5-397B-A17B | AIME 2026 | as in model card table | 91.3 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.5-397B-A17B (capture 2026-02-16) | [hf_qwen35_397b_model_card](https://web.archive.org/web/20260216104038id_/https://huggingface.co/Qwen/Qwen3.5-397B-A17B) html | `m2026.qwen35card.qwen3-5-397b-a17b.aime26` |
| Qwen3.5-397B-A17B | GPQA (subset not stated) | as in model card table | 88.4 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.5-397B-A17B (capture 2026-02-16) | [hf_qwen35_397b_model_card](https://web.archive.org/web/20260216104038id_/https://huggingface.co/Qwen/Qwen3.5-397B-A17B) html | `m2026.qwen35card.qwen3-5-397b-a17b.gpqa` |
| Qwen3.5-397B-A17B | LiveCodeBench v6 | as in model card table | 83.6 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.5-397B-A17B (capture 2026-02-16) | [hf_qwen35_397b_model_card](https://web.archive.org/web/20260216104038id_/https://huggingface.co/Qwen/Qwen3.5-397B-A17B) html | `m2026.qwen35card.qwen3-5-397b-a17b.livecodebench-v6` |
| Qwen3.5-397B-A17B | MMLU-Pro | thinking, as in model card table | 87.8 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.5-397B-A17B (capture 2026-02-16) | [hf_qwen35_397b_model_card](https://web.archive.org/web/20260216104038id_/https://huggingface.co/Qwen/Qwen3.5-397B-A17B) html | `m2026.qwen35card.qwen3-5-397b-a17b.mmlu-pro` |
| Qwen3.5-397B-A17B | SWE-bench Verified | as in model card table | 76.4 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.5-397B-A17B (capture 2026-02-16) | [hf_qwen35_397b_model_card](https://web.archive.org/web/20260216104038id_/https://huggingface.co/Qwen/Qwen3.5-397B-A17B) html | `m2026.qwen35card.qwen3-5-397b-a17b.swe-bench-verified` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 94.3 | Gemini 3.1 Pro | Thinking (High), no tools | 2026-02 | `m2026.g31card.gemini-3-1-pro.gpqa-diamond` |
| SWE-bench Verified | 82.0 | Claude Sonnet 4.5 | high compute: parallel attempts + scoring model | 2025-09 | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

Primary-source pages from documents first published this month (not redistributed; links open the pinned version at the cited page):

- [Kimi K2.5: Visual Agentic Intelligence, v2, PDF page 12](https://arxiv.org/pdf/2602.02276v2#page=12): Table 4: Performance comparison of Kimi K2.5 against open-source and proprietary models.
- [GLM-5: from Vibe Coding to Agentic Engineering, v2, PDF page 23](https://arxiv.org/pdf/2602.15763v2#page=23): Table 7: Comparison between GLM-5 and open-source/proprietary models.

## 2026-03

**March 2026.** 5 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-5.4 | FrontierMath Tier 1-3 | reasoning effort xhigh | 47.6 | OpenAI, Introducing GPT-5.4 (Mar 5, 2026) | [openai_gpt54_blog](https://web.archive.org/web/20260305182311id_/https://openai.com/index/introducing-gpt-5-4/) html | `m2026.gpt54.gpt-5-4.frontiermath-tier-1-3` |
| GPT-5.4 | GPQA Diamond | reasoning effort xhigh | 92.8 | OpenAI, Introducing GPT-5.4 (Mar 5, 2026) | [openai_gpt54_blog](https://web.archive.org/web/20260305182311id_/https://openai.com/index/introducing-gpt-5-4/) html | `m2026.gpt54.gpt-5-4.gpqa-diamond` |
| GPT-5.4 | SWE-Bench Pro (Public) | reasoning effort xhigh | 57.7 | OpenAI, Introducing GPT-5.4 (Mar 5, 2026) | [openai_gpt54_blog](https://web.archive.org/web/20260305182311id_/https://openai.com/index/introducing-gpt-5-4/) html | `m2026.gpt54.gpt-5-4.swe-bench-pro` |
| GPT-5.4 | Terminal-Bench 2.0 | reasoning effort xhigh | 75.1 | OpenAI, Introducing GPT-5.4 (Mar 5, 2026) | [openai_gpt54_blog](https://web.archive.org/web/20260305182311id_/https://openai.com/index/introducing-gpt-5-4/) html | `m2026.gpt54.gpt-5-4.terminal-bench-2-0` |
| GPT-5.4 Pro | GPQA Diamond | reasoning effort xhigh | 94.4 | OpenAI, Introducing GPT-5.4 (Mar 5, 2026) | [openai_gpt54_blog](https://web.archive.org/web/20260305182311id_/https://openai.com/index/introducing-gpt-5-4/) html | `m2026.gpt54.gpt-5-4-pro.gpqa-diamond` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 94.4 | GPT-5.4 Pro | reasoning effort xhigh | 2026-03 | `m2026.gpt54.gpt-5-4-pro.gpqa-diamond` |
| SWE-bench Verified | 82.0 | Claude Sonnet 4.5 | high compute: parallel attempts + scoring model | 2025-09 | `m2025.sonnet45-blog.claude-sonnet-4.5.swebench.parallel` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-04

**April 2026.** 12 verified scores for 3 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Opus 4.7 | GPQA Diamond | 10 trials | 94.2 | Anthropic, Claude Opus 4.7 System Card | [anthropic_claude_opus47_system_card](https://web.archive.org/web/20260613121259id_/https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf) p.193 | `m2026.opus47card.claude-opus-4-7.gpqa-diamond` |
| Claude Opus 4.7 | MMMLU | 3 trials, adaptive thinking, max effort | 91.5 | Anthropic, Claude Opus 4.7 System Card | [anthropic_claude_opus47_system_card](https://web.archive.org/web/20260613121259id_/https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf) p.193 | `m2026.opus47card.claude-opus-4-7.mmmlu` |
| Claude Opus 4.7 | SWE-bench Pro | adaptive thinking, max effort, 5 trials | 64.3 | Anthropic, Claude Opus 4.7 System Card | [anthropic_claude_opus47_system_card](https://web.archive.org/web/20260613121259id_/https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf) p.192 | `m2026.opus47card.claude-opus-4-7.swe-bench-pro` |
| Claude Opus 4.7 | SWE-bench Verified | adaptive thinking, max effort, 5 trials | 87.6 | Anthropic, Claude Opus 4.7 System Card | [anthropic_claude_opus47_system_card](https://web.archive.org/web/20260613121259id_/https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf) p.192 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| Claude Opus 4.7 | Terminal-Bench 2.0 | Terminus-2 harness, thinking disabled | 69.4 | Anthropic, Claude Opus 4.7 System Card | [anthropic_claude_opus47_system_card](https://web.archive.org/web/20260613121259id_/https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf) p.193 | `m2026.opus47card.claude-opus-4-7.terminal-bench-2-0` |
| DeepSeek-V4-Pro (Think Max) | GPQA Diamond | Think Max, Pass@1 | 90.1 | DeepSeek, Hugging Face model card deepseek-ai/DeepSeek-V4-Pro (capture 2026-04-24) | [hf_deepseek_v4_pro_model_card](https://web.archive.org/web/20260424025428id_/https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) html | `m2026.dsv4card.deepseek-v4-pro-max.gpqa-diamond` |
| DeepSeek-V4-Pro (Think Max) | LiveCodeBench (version not stated) | Think Max, Pass@1 | 93.5 | DeepSeek, Hugging Face model card deepseek-ai/DeepSeek-V4-Pro (capture 2026-04-24) | [hf_deepseek_v4_pro_model_card](https://web.archive.org/web/20260424025428id_/https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) html | `m2026.dsv4card.deepseek-v4-pro-max.livecodebench` |
| DeepSeek-V4-Pro (Think Max) | MMLU-Pro | Think Max, EM | 87.5 | DeepSeek, Hugging Face model card deepseek-ai/DeepSeek-V4-Pro (capture 2026-04-24) | [hf_deepseek_v4_pro_model_card](https://web.archive.org/web/20260424025428id_/https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) html | `m2026.dsv4card.deepseek-v4-pro-max.mmlu-pro` |
| DeepSeek-V4-Pro (Think Max) | SWE-bench Verified | Think Max, resolved rate | 80.6 | DeepSeek, Hugging Face model card deepseek-ai/DeepSeek-V4-Pro (capture 2026-04-24) | [hf_deepseek_v4_pro_model_card](https://web.archive.org/web/20260424025428id_/https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) html | `m2026.dsv4card.deepseek-v4-pro-max.swe-bench-verified` |
| GPT-5.5 | GPQA Diamond | reasoning effort xhigh | 93.6 | OpenAI, Introducing GPT-5.5 (Apr 23, 2026) | [openai_gpt55_blog](https://web.archive.org/web/20260423190022id_/https://openai.com/index/introducing-gpt-5-5/) html | `m2026.gpt55.gpt-5-5.gpqa-diamond` |
| GPT-5.5 | SWE-Bench Pro (Public) | reasoning effort xhigh | 58.6 | OpenAI, Introducing GPT-5.5 (Apr 23, 2026) | [openai_gpt55_blog](https://web.archive.org/web/20260423190022id_/https://openai.com/index/introducing-gpt-5-5/) html | `m2026.gpt55.gpt-5-5.swe-bench-pro` |
| GPT-5.5 | Terminal-Bench 2.0 | reasoning effort xhigh | 82.7 | OpenAI, Introducing GPT-5.5 (Apr 23, 2026) | [openai_gpt55_blog](https://web.archive.org/web/20260423190022id_/https://openai.com/index/introducing-gpt-5-5/) html | `m2026.gpt55.gpt-5-5.terminal-bench-2-0` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 94.4 | GPT-5.4 Pro | reasoning effort xhigh | 2026-03 | `m2026.gpt54.gpt-5-4-pro.gpqa-diamond` |
| SWE-bench Verified | 87.6 | Claude Opus 4.7 | adaptive thinking, max effort, 5 trials | 2026-04 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-05

**May 2026.** 2 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Gemini 3.5 Flash | SWE-Bench Pro (Public) | single attempt | 55.1 | Google DeepMind, Gemini 3.5 Flash model card (published 19 May 2026) | [google_gemini35flash_model_card](https://web.archive.org/web/20260519174844id_/https://deepmind.google/models/model-cards/gemini-3-5-flash/) html | `m2026.g35flash.gemini-3-5-flash.swe-bench-pro` |
| Gemini 3.5 Flash | Terminal-Bench 2.1 | Terminus-2 harness | 76.2 | Google DeepMind, Gemini 3.5 Flash model card (published 19 May 2026) | [google_gemini35flash_model_card](https://web.archive.org/web/20260519174844id_/https://deepmind.google/models/model-cards/gemini-3-5-flash/) html | `m2026.g35flash.gemini-3-5-flash.terminal-bench-2-1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 94.4 | GPT-5.4 Pro | reasoning effort xhigh | 2026-03 | `m2026.gpt54.gpt-5-4-pro.gpqa-diamond` |
| SWE-bench Verified | 87.6 | Claude Opus 4.7 | adaptive thinking, max effort, 5 trials | 2026-04 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-06

**June 2026.** 5 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Sonnet 5 | SWE-bench Pro | standard configuration, 5 trials | 63.2 | Anthropic, Claude Sonnet 5 System Card | [anthropic_claude_sonnet5_system_card](https://web.archive.org/web/20260717084250id_/https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf) p.116 | `m2026.sonnet5card.claude-sonnet-5.swe-bench-pro` |
| Claude Sonnet 5 | SWE-bench Verified | adaptive thinking, max effort, 5 trials (standard configuration) | 85.2 | Anthropic, Claude Sonnet 5 System Card | [anthropic_claude_sonnet5_system_card](https://web.archive.org/web/20260717084250id_/https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf) p.116 | `m2026.sonnet5card.claude-sonnet-5.swe-bench-verified` |
| GLM-5.2 | AIME 2026 | as in model card table | 99.2 | Zhipu AI (Z.ai), Hugging Face model card zai-org/GLM-5.2 (capture 2026-06-16) | [hf_glm52_model_card](https://web.archive.org/web/20260616174545id_/https://huggingface.co/zai-org/GLM-5.2) html | `m2026.glm52card.glm-5-2.aime-2026` |
| GLM-5.2 | GPQA-Diamond | as in model card table | 91.2 | Zhipu AI (Z.ai), Hugging Face model card zai-org/GLM-5.2 (capture 2026-06-16) | [hf_glm52_model_card](https://web.archive.org/web/20260616174545id_/https://huggingface.co/zai-org/GLM-5.2) html | `m2026.glm52card.glm-5-2.gpqa-diamond` |
| GLM-5.2 | SWE-bench Pro | as in model card table | 62.1 | Zhipu AI (Z.ai), Hugging Face model card zai-org/GLM-5.2 (capture 2026-06-16) | [hf_glm52_model_card](https://web.archive.org/web/20260616174545id_/https://huggingface.co/zai-org/GLM-5.2) html | `m2026.glm52card.glm-5-2.swe-bench-pro` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 94.4 | GPT-5.4 Pro | reasoning effort xhigh | 2026-03 | `m2026.gpt54.gpt-5-4-pro.gpqa-diamond` |
| SWE-bench Verified | 87.6 | Claude Opus 4.7 | adaptive thinking, max effort, 5 trials | 2026-04 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-07

**July 2026.** 5 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| GPT-5.6 Sol | GPQA Diamond | effort not stated in the table | 94.6 | OpenAI, GPT-5.6 launch post (Jul 9, 2026) | [openai_gpt56_blog](https://web.archive.org/web/20260709193923id_/https://openai.com/index/gpt-5-6/) html | `m2026.gpt56.gpt-5-6-sol.gpqa-diamond` |
| GPT-5.6 Sol | SWE-Bench Pro | effort not stated in the table | 64.6 | OpenAI, GPT-5.6 launch post (Jul 9, 2026) | [openai_gpt56_blog](https://web.archive.org/web/20260709193923id_/https://openai.com/index/gpt-5-6/) html | `m2026.gpt56.gpt-5-6-sol.swe-bench-pro` |
| GPT-5.6 Sol | Terminal-Bench 2.1 | effort not stated in the table | 88.8 | OpenAI, GPT-5.6 launch post (Jul 9, 2026) | [openai_gpt56_blog](https://web.archive.org/web/20260709193923id_/https://openai.com/index/gpt-5-6/) html | `m2026.gpt56.gpt-5-6-sol.terminal-bench-2-1` |
| Grok 4.5 | SWE-Bench Pro | resolve rate | 64.7 | xAI (page branded SpaceXAI), Introducing Grok 4.5 (Jul 8, 2026) | [xai_grok45_blog](https://web.archive.org/web/20260708180848id_/https://x.ai/news/grok-4-5) html | `m2026.grok45.grok-4-5.swe-bench-pro` |
| Grok 4.5 | Terminal-Bench 2.1 | effort not stated for Grok 4.5 | 83.3 | xAI (page branded SpaceXAI), Introducing Grok 4.5 (Jul 8, 2026) | [xai_grok45_blog](https://web.archive.org/web/20260708180848id_/https://x.ai/news/grok-4-5) html | `m2026.grok45.grok-4-5.terminal-bench-2-1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 94.6 | GPT-5.6 Sol | effort not stated in the table | 2026-07 | `m2026.gpt56.gpt-5-6-sol.gpqa-diamond` |
| SWE-bench Verified | 87.6 | Claude Opus 4.7 | adaptive thinking, max effort, 5 trials | 2026-04 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-08

**August 2026.** 3 verified scores for 1 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Qwen3.8-Max | GPQA Diamond | as in model card table | 92.6 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.8-2.4T-A95B (capture 2026-08-12) | [hf_qwen38_2p4t_model_card](https://web.archive.org/web/20260812150416id_/https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) html | `m2026.qwen38card.qwen3-8-max.gpqa-diamond` |
| Qwen3.8-Max | SWE-bench Pro, Qwen-refined version ('Problematic tasks corrected and all baselines evaluated on the refined benchmark') | Claude Code harness, temp 1.0, top_p 0.95, 256K context (footnote 3) | 67.7 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.8-2.4T-A95B (capture 2026-08-12) | [hf_qwen38_2p4t_model_card](https://web.archive.org/web/20260812150416id_/https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) html | `m2026.qwen38card.qwen3-8-max.swe-bench-pro` |
| Qwen3.8-Max | Terminal-Bench 2.1 | Claude Code harness, avg@10, 5-hour timeout, max_tokens=131,072 (footnote 2); baselines are best published scores across harnesses | 86.6 | Alibaba Qwen, Hugging Face model card Qwen/Qwen3.8-2.4T-A95B (capture 2026-08-12) | [hf_qwen38_2p4t_model_card](https://web.archive.org/web/20260812150416id_/https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) html | `m2026.qwen38card.qwen3-8-max.terminal-bench-2-1` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 94.6 | GPT-5.6 Sol | effort not stated in the table | 2026-07 | `m2026.gpt56.gpt-5-6-sol.gpqa-diamond` |
| SWE-bench Verified | 87.6 | Claude Opus 4.7 | adaptive thinking, max effort, 5 trials | 2026-04 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-09

**September 2026.** 8 verified scores for 5 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Opus 5.5 | Humanity's Last Exam | with tools, adaptive thinking, max effort | 67.7 | Anthropic, Introducing Claude Opus 5.5 (Sep 22, 2026) | [anthropic_claude_opus55_page](https://web.archive.org/web/20261019114417id_/https://www.anthropic.com/claude-opus-5-5) html | `m2026.opus55page.claude-opus-5-5.hle.with-tools` |
| Claude Opus 5.5 | Terminal-Bench 4.0 | xhigh effort (Anthropic setup; harness not named for the Opus 5.5 run) | 66.4 | Anthropic, Introducing Claude Opus 5.5 (Sep 22, 2026) | [anthropic_claude_opus55_page](https://web.archive.org/web/20261019114417id_/https://www.anthropic.com/claude-opus-5-5) html | `m2026.opus55page.claude-opus-5-5.terminal-bench-4-0.xhigh` |
| Claude Opus 5.5 (Artificial Analysis run: Claude Opus 5.5 (Max, Default Fallback)) | Terminal-Bench 4.0 | Artificial Analysis harness, effort 'max' | 59.6 | Artificial Analysis model page (Wayback) | [aa_claude_opus55](https://web.archive.org/web/20261018141251id_/https://artificialanalysis.ai/models/claude-opus-5-5) html | `m2026.aa.claude-opus-5-5.terminal-bench-4-0` |
| Claude Sonnet 5.5 | Humanity's Last Exam | with tools | 64.5 | Anthropic, Introducing Claude Sonnet 5.5 (Sep 28, 2026) | [anthropic_claude_sonnet55_page](https://web.archive.org/web/20261019114547id_/https://www.anthropic.com/claude-sonnet-5-5) html | `m2026.sonnet55page.claude-sonnet-5-5.hle.with-tools` |
| Claude Sonnet 5.5 | Terminal-Bench 4.0 | effort not stated for Sonnet 5.5 (footnote 1 states xhigh only for Opus 5.5) | 70.6 | Anthropic, Introducing Claude Sonnet 5.5 (Sep 28, 2026) | [anthropic_claude_sonnet55_page](https://web.archive.org/web/20261019114547id_/https://www.anthropic.com/claude-sonnet-5-5) html | `m2026.sonnet55page.claude-sonnet-5-5.terminal-bench-4-0` |
| Claude Sonnet 5.5 (Artificial Analysis run: Claude Sonnet 5.5 (max with fallback)) | Terminal-Bench 4.0 | Artificial Analysis harness, effort 'max' | 63.6 | Artificial Analysis model page (Wayback) | [aa_claude_sonnet55](https://web.archive.org/web/20261016153447id_/https://artificialanalysis.ai/models/claude-sonnet-5-5) html | `m2026.aa.claude-sonnet-5-5.terminal-bench-4-0` |
| GPT-6 Astra | GPQA Diamond | maximum at any effort | 96.0 | OpenAI, GPT-6 Astra launch post (Wayback capture 2026-09-03) | [openai_gpt6_astra_blog](https://web.archive.org/web/20260903201137id_/https://openai.com/index/gpt-6-astra/) html | `m2026.astra.gpt-6-astra.gpqa-diamond` |
| GPT-6 Astra | Terminal-Bench 4.0 | maximum at any effort (eval table) | 57.7 | OpenAI, GPT-6 Astra launch post (Wayback capture 2026-09-03) | [openai_gpt6_astra_blog](https://web.archive.org/web/20260903201137id_/https://openai.com/index/gpt-6-astra/) html | `m2026.astra.gpt-6-astra.terminal-bench-4-0.table` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 96.0 | GPT-6 Astra | maximum at any effort | 2026-09 | `m2026.astra.gpt-6-astra.gpqa-diamond` |
| SWE-bench Verified | 87.6 | Claude Opus 4.7 | adaptive thinking, max effort, 5 trials | 2026-04 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

## 2026-10

**October 2026.** 2 verified scores for 2 model(s).

| Model | Benchmark | Protocol (as stated) | Value | Reported by | Source | Claim |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| Claude Haiku 5.5 | Terminal-Bench 4.0 | as in launch table (effort not stated) | 39.2 | Anthropic, Introducing Claude Haiku 5.5 (Oct 7, 2026) | [anthropic_claude_haiku55_page](https://web.archive.org/web/20261007180346id_/https://www.anthropic.com/claude-haiku-5-5) html | `m2026.haiku55page.claude-haiku-5-5.terminal-bench-4-0` |
| Gemini 4 Argon | Terminal-Bench 4.0 | as in model card table | 57.4 | Google DeepMind, Gemini 4 Argon model card (published 13 Oct 2026) | [google_gemini4argon_model_card](https://web.archive.org/web/20261013160532id_/https://deepmind.google/models/model-cards/gemini-4-argon/) html | `m2026.argon.gemini-4-argon.terminal-bench-4-0` |

Highest value published by the end of this month:

| Benchmark | Value | Model | Protocol | Published | Claim |
| :--- | :---: | :--- | :--- | :---: | :--- |
| MMLU | 92.9 | o3 (row label 'o3' with footnote [^9], whose text reads 'The default reasoning level for o3-mini is "medium"') | 0-shot CoT, no tools | 2025-07 | `m2025.simple-evals.o3.mmlu` |
| MMLU-Pro | 90.1 | Gemini-3.0 Pro | EM | 2025-12 | `m2025.dsv32.gemini-3-pro.mmlu-pro` |
| HumanEval | 97.6 | o3-mini-high | 0-shot CoT (simple-evals) | 2025-07 | `m2025.simple-evals.o3-mini-high.humaneval` |
| GSM8K | 96.8 | Llama 3 405B (Llama 3.1 405B Instruct) | 8-shot CoT | 2024-07 | `m2024.llama3herd.llama-3.1-405b.gsm8k.8-shot-cot` |
| MATH | 83.1 | Qwen2.5-72B-Instruct | not stated in table | 2024-12 | `m2024.qwen25.qwen2.5-72b-instruct.math.instruct` |
| MATH-500 | 98.2 | GLM-4.5 | GLM evaluation | 2025-08 | `m2025.glm45.glm-4.5.math500` |
| GPQA Diamond | 96.0 | GPT-6 Astra | maximum at any effort | 2026-09 | `m2026.astra.gpt-6-astra.gpqa-diamond` |
| SWE-bench Verified | 87.6 | Claude Opus 4.7 | adaptive thinking, max effort, 5 trials | 2026-04 | `m2026.opus47card.claude-opus-4-7.swe-bench-verified` |
| AIME 2024 | 93.4 | o4-mini (no tools) | no tools | 2025-04 | `m2025.o3-blog.o4-mini.aime24.notools` |
| AIME 2025 | 100.0 | Grok 4 Heavy [chart code GROK_4_HEAVY] | with tools (Python) | 2025-07 | `m2025.grok4-blog.grok-4-heavy.aime25.tools` |

