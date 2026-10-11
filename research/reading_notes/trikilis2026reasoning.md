# trikilis2026reasoning

## Citation
Trikilis, Holly; Marasinghe, Pasindu; Rashid, Fariza; Seneviratne, Suranga (2026). *Eliciting Least-to-Most Reasoning for Phishing URL Detection*. arXiv preprint arXiv:2601.20270 (short paper). URL: https://arxiv.org/abs/2601.20270

- Type: preprint | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/trikilis2026reasoning.pdf

## Verification
Checked 2026-10-11: arXiv API record 2601.20270 (2026-01-28) and arXiv PDF read. No DOI.

## Problem
Improve LLM reasoning for phishing URL classification with minimal labelled data.

## Method
Decomposes URL judgement into sub-questions, iterates, uses answer-sensitivity to trigger re-reasoning.

## Dataset(s)
HP, EBBU (Ebbu2017) and ISCX-URL-2016; random balanced 1,000-URL test subsets, 5 repetitions (Sec. 3)

## Features
Raw URL text in prompts.

## Evaluation protocol
Mean F1 over 5 random 1,000-URL draws per dataset (Table 1)

## Metrics reported
Least-to-Most average F1 0.9040 vs 0.8726 one-shot across models/datasets; Gemini best at 0.9621 average F1; URLTran supervised about 0.99 F1 (Table 1).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Prompted LLMs approach but do not reach supervised transformers; reasoning prompts help smaller models most.

## Limitations
- Stated by authors: Small test subsets; API cost.
- Our own caveats: Not peer reviewed; 1,000-URL subsets give wide confidence intervals.

## Research gap
Cost-aware comparison with lightweight models.

## Relevance to our project
Latest LLM-prompting baseline; shows supervised models still lead - supports our lightweight ensemble choice.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
