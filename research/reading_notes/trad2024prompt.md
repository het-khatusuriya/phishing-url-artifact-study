# trad2024prompt

## Citation
Trad, Fouad; Chehab, Ali (2024). *Prompt Engineering or Fine-Tuning? A Case Study on Phishing Detection with Large Language Models*. Machine Learning and Knowledge Extraction, 6(1), pp. 367-384. DOI: 10.3390/make6010018 URL: https://doi.org/10.3390/make6010018

- Type: journal | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/trad2024prompt.pdf

## Verification
Checked 2026-10-11: MDPI open-access PDF (CC BY) read; Crossref record for DOI 10.3390/make6010018 (MAKE 6(1), 367-384, 2024).

## Problem
Can prompted general LLMs replace task-specific URL classifiers?

## Method
Multiple prompt strategies on chat models; fine-tuning of small base LLMs for binary URL classification; comparison with prior results on the same dataset (Table 3).

## Dataset(s)
Hannousse & Yahiouche Mendeley dataset: 11,430 URLs (balanced); 1,000-sample balanced test subset (500/500); remaining 10,430 for fine-tuning (Sec. 4)

## Features
Raw URL text.

## Evaluation protocol
Fixed 1,000 test subset; also varying phishing ratio experiments (Fig. 8-10)

## Metrics reported
Best prompting F1 92.74% (Claude 2); fine-tuned gpt2-medium F1 97.29%, AUC 99.56% (abstract; Sec. 5); at low phishing ratios GPT-2 F1 76.19%/86.73% vs Claude 2 59.15%/74.58% (Sec. 5.3).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Fine-tuned small LLMs beat prompted frontier chat models; prompted models degrade under class imbalance.

## Limitations
- Stated by authors: Small test set (1,000); single dataset (Sec. 6).
- Our own caveats: Dataset is small; results may not transfer to 250k-scale data.

## Research gap
Larger, temporally split LLM evaluations.

## Relevance to our project
Positions LLM prompting as a weak baseline vs task-specific models; relevant for our discussion of model choice and imbalance.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
