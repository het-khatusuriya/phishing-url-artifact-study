# niculescumizil2005calibration

## Citation
Alexandru Niculescu-Mizil; Rich Caruana (2005). *Predicting good probabilities with supervised learning*. Proceedings of the 22nd International Conference on Machine Learning (ICML '05). DOI: 10.1145/1102351.1102430 URL: https://doi.org/10.1145/1102351.1102430

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Semantic Scholar API record for DOI 10.1145/1102351.1102430 (title, authors, ICML 2005). ACM full text paywalled; not downloaded.

## Problem
Which learning algorithms produce calibrated probabilities and how to fix those that do not?

## Method
Empirical comparison across ten learners; Platt scaling vs isotonic regression on held-out calibration data.

## Dataset(s)
Eight binary classification problems (paper Sec. 3).

## Features
n/a

## Evaluation protocol
Squared error (Brier), log-loss, reliability diagrams

## Metrics reported (only numbers present in the source)
Boosted trees and SVMs push predictions away from 0/1 (sigmoid-shaped reliability diagrams); RF/bagging are better calibrated; isotonic needs >~1000 calibration points (paper Sec. 4-5; numbers not reproduced here).

## Main findings
Boosting (max-margin) methods are systematically miscalibrated and benefit most from Platt/isotonic; RF and bagged trees nearly calibrated.

## Limitations
- Authors' stated limitations: 2005-era learners; no gradient boosting with log-loss.
- My assessment: Modern XGBoost/LightGBM with logistic loss are better calibrated than AdaBoost, so findings need re-checking on our ensemble.

## Research gap
Calibration behaviour of soft-voting/stacked ensembles on security data.

## Relevance to our project (score 5/5)
Canonical justification for calibrating boosting-based members of our ensemble with Platt or isotonic regression and for checking RF separately.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
