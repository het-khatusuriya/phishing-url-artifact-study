# ali2025phishurldetect

## Citation
Ali, Irshad; Subba, Basant (2025). *PhishURLDetect: A parameter efficient fine-tuning of LLMs using LoRA for detection of phishing URLs*. Proceedings of the 26th International Conference on Distributed Computing and Networking (ICDCN 2025), pp. 278-279. DOI: 10.1145/3700838.3703658 URL: https://doi.org/10.1145/3700838.3703658

- Type: conference | Theme (L1): d-transformer-llm | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1145/3700838.3703658 (ICDCN 2025, pp. 278-279, CC BY) and Semantic Scholar abstract. ACM PDF blocked.

## Problem
Parameter-efficient LLM fine-tuning for phishing URLs.

## Method
LoRA adapters on RoBERTa/GPT-2.

## Dataset(s)
Proprietary corpus of 573,880 phishing + benign URLs (abstract)

## Features
Raw URL tokens.

## Evaluation protocol
Not in abstract

## Metrics reported
99.86% accuracy (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
LoRA matches full fine-tuning at a fraction of parameters.

## Limitations
- Stated by authors: Not available.
- Our own caveats: 2-page poster; proprietary data; accuracy-only reporting.

## Research gap
Public evaluation.

## Relevance to our project
Minor; shows PEFT trend for URL classifiers.

Relevance score: 2/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
