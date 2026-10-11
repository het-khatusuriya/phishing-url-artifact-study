# roy2024phishlang

## Citation
Sayak Saha Roy; Shirin Nilizadeh (2024). *PhishLang: A Real-Time, Fully Client-Side Phishing Detection Framework Using MobileBERT*. arXiv:2408.05667 (v3, Apr 2025); CC BY 4.0. URL: https://arxiv.org/abs/2408.05667

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/roy2024phishlang.pdf).
- Evidence: arXiv abs page 2408.05667 (title, authors, versions, licence). PDF from arXiv.

## Problem
Phishing detection usually relies on server-side blocklists/heavy models; need private, real-time client-side detection.

## Method
Fine-tune MobileBERT on URL and parsed source code; ensemble; ship as browser extension.

## Dataset(s)
Author-crawled datasets (paper Sec. 3); sizes in paper.

## Features
Contextual tokens of URL and critical HTML tags.

## Evaluation protocol
Accuracy/precision/recall/F1 of nine language models; median inference time and memory (Table 2); comparison with anti-phishing tools; zero-day evaluation

## Metrics reported (only numbers present in the source)
MobileBERT accuracy 0.96 with precision 0.95 / recall 0.96, fastest among SLMs; Llama 2 F1 0.96 but much slower; memory per model ranges from 74 MB to 7,352 MB (paper Table 2).

## Main findings
Small transformer achieves near-LLM accuracy with far lower memory/latency; fully local operation is feasible.

## Limitations
- Authors' stated limitations: Transformer still heavier than classical models; relies on page source for best accuracy.
- My assessment: No comparison with lexical gradient-boosting baselines on the same hardware.

## Research gap
Head-to-head latency/model-size of lexical ensembles vs. small transformers on identical URL sets.

## Relevance to our project (score 4/5)
Reference point for our latency/model-size table (MobileBERT ~ 74-100 MB class vs. our KB-MB ensemble).

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
