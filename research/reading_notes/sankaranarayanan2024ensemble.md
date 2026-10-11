# sankaranarayanan2024ensemble

## Citation
Sankaranarayanan, Suresh; Sivachandran, Arvinthan Thevar; Mohd Khairuddin, Anis Salwa; Hasikin, Khairunnisa; Wahab Sait, Abdul Rahman (2024). *An ensemble classification method based on machine learning models for malicious Uniform Resource Locators (URL)*. PLOS ONE, 19(5), e0302196. DOI: 10.1371/journal.pone.0302196 URL: https://doi.org/10.1371/journal.pone.0302196

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: full_text | Verified: full
- Local PDF: research/papers/sankaranarayanan2024ensemble.pdf

## Verification
Checked 2026-10-11: PLOS ONE open-access PDF (CC BY) read; Crossref record for DOI 10.1371/journal.pone.0302196 (PLOS ONE 19(5) e0302196, 2024).

## Problem
Multi-class malicious URL classification on a larger dataset with a stacking ensemble.

## Method
Lexical feature extraction; individual boosted/bagged trees; stacking meta-learner; hyperparameter tuning.

## Dataset(s)
Kaggle 'malicious-urls-dataset' (sid321axn): 651,191 URLs; 4 classes benign/defacement/phishing/malware (Sec. 3)

## Features
Lexical features (lengths, counts of special characters/digits, IP/shortener flags, suspicious words) listed in Table 2 / Fig. 1.

## Evaluation protocol
Stratified 80/20 train/test split (Sec. 3.2.3); no cross-dataset

## Metrics reported
Individual accuracies 93.6% (RF), 95.2% (XGB), 95.7% (LGBM), 94.8% (CatBoost); stacking average accuracy 96.8%; per-class precision 91-99%, recall 87-99% (abstract; Sec. 4).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Stacking adds about 1 point over the best single booster on lexical features.

## Limitations
- Stated by authors: Lexical features only; short-lived URLs (Sec. 2).
- Our own caveats: Kaggle aggregate dataset mixes sources (ISCX, PhishStorm, PhishTank...) so class is partly predictable from source formatting; random split only.

## Research gap
Source-aware / cross-dataset evaluation and calibration.

## Relevance to our project
Closest published analogue of our lexical + tree-ensemble pipeline on a large Kaggle dataset; our artifact analysis extends it.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
