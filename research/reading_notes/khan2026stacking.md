# khan2026stacking

## Citation
Khan, Hafiz Aziz; Akter, Sonia; Lindon, Abdur Rahman; Akter, Taslima; Rasul, Iftekhar; Rahman, Mamunur; Tohfa, Nasrin Akter; Hossain, Iftekhar (2026). *Explainable AI for phishing URL detection: a Bayesian-optimized stacking ensemble framework with SHAP-guided feature learning*. Frontiers in Artificial Intelligence, 9, 1854934. DOI: 10.3389/frai.2026.1854934 URL: https://doi.org/10.3389/frai.2026.1854934

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: full_text | Verified: full
- Local PDF: research/papers/khan2026stacking.pdf

## Verification
Checked 2026-10-11: Frontiers open-access PDF (CC BY) read; Crossref record for DOI 10.3389/frai.2026.1854934 (Front. Artif. Intell. 9:1854934, 2026).

## Problem
Explainable, statistically validated stacking ensemble for phishing URL detection.

## Method
12-stage pipeline: EDA, SHAP feature selection, benchmarking seven algorithm families, Bayesian optimisation, stacking, threshold tuning, SHAP explanations.

## Dataset(s)
Public Kaggle benchmark (Harisudhan 2024): 247,950 URLs with 41 pre-extracted structural/lexical features; raw URL strings not released (Sec. 3.1)

## Features
41 numeric lexical/structural/entropy descriptors (publisher pre-extracted).

## Evaluation protocol
Stratified 80/20 split, 5-fold CV inside training; no cross-dataset

## Metrics reported
Top tier: Extra Trees Acc 0.9671 / AUC 0.9948, RF Acc 0.9667 / AUC 0.9930; stacking ensemble leads on Acc/F1/MCC/Kappa with AUC 0.9947 vs 0.9948 for Extra Trees; confusion matrix 24,977 TN, 731 FP, 883 FN on test set, FPR 731/25,708 = 2.84% (Sec. 5, Tables 6-10).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Stacking gives marginal gains over tuned Extra Trees; SHAP-selected features retain performance.

## Limitations
- Stated by authors: Dataset lacks raw URLs, undocumented collection windows/sources; single dataset; no temporal validation (Sec. 3.1 and limitations).
- Our own caveats: About 248k pre-featurised Kaggle set is very similar in scale to ours; results on random splits are likely optimistic.

## Research gap
Cross-dataset / temporal evaluation, artifact audit, calibration measurement.

## Relevance to our project
Nearest 2026 competitor: same scale (about 248k), ensemble + SHAP; our contribution should be the generalisation/artifact/calibration analysis they omit.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
