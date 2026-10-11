# alfayoumi2024xaiphd

## Citation
Mustafa Al-Fayoumi; Bushra Alhijawi; Qasem Abu Al-Haija; Rakan Armoush (2024). *XAI-PhD: Fortifying Trust of Phishing URL Detection Empowered by Shapley Additive Explanations*. International Journal of Online and Biomedical Engineering (iJOE) 20(11):80-101. DOI: 10.3991/ijoe.v20i11.49533 URL: https://doi.org/10.3991/ijoe.v20i11.49533

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Crossref record for DOI 10.3991/ijoe.v20i11.49533 (title, authors, journal, vol/issue/pages, published 2024-08-08).

## Problem
ML phishing-URL detectors lack transparency and trust.

## Method
Compute SHAP values, retain most influential features, train a lightweight gradient boosting classifier.

## Dataset(s)
Not specified in the abstract (full text not retrieved).

## Features
URL-derived features (as per abstract).

## Evaluation protocol
Hold-out classification; accuracy, F1, per-record prediction time

## Metrics reported (only numbers present in the source)
Abstract reports 99.8% accuracy and 99% F1 and 'very low' per-record prediction time (abstract only; tables not seen).

## Main findings
SHAP-driven feature pruning keeps accuracy while reducing cost.

## Limitations
- Authors' stated limitations: Not available (abstract only).
- My assessment: Venue is low-tier; 99.8% accuracy suggests possible leakage/within-dataset optimism; no external test.

## Research gap
No robustness or calibration analysis; no cross-dataset validation.

## Relevance to our project (score 3/5)
Example of SHAP-for-feature-selection in URL detection; we should go beyond by validating SHAP rankings externally.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
