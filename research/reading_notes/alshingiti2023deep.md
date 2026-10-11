# alshingiti2023deep

## Citation
Alshingiti, Zainab; Alaqel, Rabeah; Al-Muhtadi, Jalal; Haq, Qazi Emad Ul; Saleem, Kashif; Faheem, Muhammad Hamza (2023). *A Deep Learning-Based Phishing Detection System Using CNN, LSTM, and LSTM-CNN*. Electronics, 12(1), 232. DOI: 10.3390/electronics12010232 URL: https://doi.org/10.3390/electronics12010232

- Type: journal | Theme (L1): c-char-level | Access: full_text | Verified: full
- Local PDF: research/papers/alshingiti2023deep.pdf

## Verification
Checked 2026-10-11: MDPI open-access PDF (CC BY) read; Crossref record for DOI 10.3390/electronics12010232 (Electronics 12(1):232, 2023).

## Problem
Compare deep architectures for phishing website detection.

## Method
Applies 1D-CNN, LSTM and stacked LSTM-CNN to tabular URL features.

## Dataset(s)
Pre-extracted feature dataset of 20,000 URLs (9,800 phishing) with 80 features, reduced to 30 via SelectKBest (Sec. 3.2)

## Features
30 selected numeric URL/website features (not raw characters).

## Evaluation protocol
80/20 random split (Sec. 3.2)

## Metrics reported
Accuracy 99.2% (CNN), 97.6% (LSTM-CNN), 96.8% (LSTM) (abstract; Sec. 4).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
CNN on tabular features best.

## Limitations
- Stated by authors: Small dataset.
- Our own caveats: Despite the title it is not character-level; 20k pre-featurised samples; random split - results not comparable to raw-URL models.

## Research gap
Raw-URL evaluation.

## Relevance to our project
Low; include only to show how 'deep' phishing papers often use tabular features and random splits.

Relevance score: 2/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
