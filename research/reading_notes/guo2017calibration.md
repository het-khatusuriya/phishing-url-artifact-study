# guo2017calibration

## Citation
Chuan Guo; Geoff Pleiss; Yu Sun; Kilian Q. Weinberger (2017). *On Calibration of Modern Neural Networks*. Proceedings of the 34th International Conference on Machine Learning (ICML 2017), PMLR 70. URL: https://arxiv.org/abs/1706.04599

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/guo2017calibration.pdf).
- Evidence: arXiv abs page 1706.04599 (title, authors, 'ICML 2017'); PDF from arXiv. (Semantic Scholar API rate-limited; PMLR has no DOI.)

## Problem
Modern deep nets are over-confident; probabilities do not match empirical accuracy.

## Method
Define/popularise ECE and reliability diagrams; evaluate post-hoc calibration methods; propose temperature scaling.

## Dataset(s)
Standard vision/NLP benchmarks (paper Sec. 5).

## Features
n/a

## Evaluation protocol
Expected Calibration Error (ECE), Maximum Calibration Error, NLL, reliability diagrams

## Metrics reported (only numbers present in the source)
Temperature scaling achieves lowest ECE on most datasets (paper Table 1).

## Main findings
Depth/width/BatchNorm/weight decay affect calibration; one-parameter temperature scaling is surprisingly effective.

## Limitations
- Authors' stated limitations: Post-hoc methods assume calibration set from same distribution.
- My assessment: Our models are tree ensembles; temperature scaling applies to logits/scores but Platt/isotonic are more usual for RF/GBDT; distribution shift to external datasets breaks post-hoc calibration guarantees.

## Research gap
Calibration of security classifiers under dataset shift and adversarial mutation.

## Relevance to our project (score 5/5)
Defines ECE/MCE and reliability diagrams we will report; justifies temperature/Platt/isotonic comparison.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
