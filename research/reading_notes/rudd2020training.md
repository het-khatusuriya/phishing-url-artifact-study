# rudd2020training

## Citation
Rudd, Ethan M.; Abdallah, Ahmed (2020). *Training Transformers for Information Security Tasks: A Case Study on Malicious URL Prediction*. arXiv preprint arXiv:2011.03040. URL: https://arxiv.org/abs/2011.03040

- Type: preprint | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/rudd2020training.pdf

## Verification
Checked 2026-10-11: arXiv API record 2011.03040 and arXiv PDF read. No DOI.

## Problem
How should transformers be trained on URL strings for security tasks?

## Method
Auto-regressive pre-training on 20M unlabeled URLs does not transfer; adding an auxiliary auto-regressive loss while training from scratch (balanced dynamically) helps; compared with baselines.

## Dataset(s)
FireEye URL corpus: 1,007,451 training, 111,930 validation (20,013 malicious, 91,813 benign), 279,874 test URLs; 20M unlabeled URLs for pre-training (Sec. 3)

## Features
Raw characters/bytes.

## Evaluation protocol
Held-out split; ROC-AUC comparison (Fig. 2-3)

## Metrics reported
Mixed-objective transformer on par with the best baseline (1D CNN) by ROC-AUC (Fig. 3); numbers in figure legends.
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Generic NLP pre-training recipes do not transfer directly to URLs; char-CNNs remain a strong baseline.

## Limitations
- Stated by authors: Proprietary data; limited pre-training scale.
- Our own caveats: Not peer reviewed.

## Research gap
Public pre-training corpora for URLs.

## Relevance to our project
Tempering evidence: transformers do not automatically beat char-CNNs on URLs; supports including a strong char-CNN in our ensemble.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
