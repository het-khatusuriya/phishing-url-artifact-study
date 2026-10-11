# kehkashan2025explainable

## Citation
Tanzila Kehkashan; Maha Abdelhaq; Ahmad Sami Al-Shamayleh; Nazish Huda; Imran Ashraf Yaseen; Abdelmuttlib Ibrahim Abdalla Ahmed; Adnan Akhunzada (2025). *Explainable phishing website detection for secure and sustainable cyber infrastructure*. Scientific Reports 15, article 41751. DOI: 10.1038/s41598-025-27984-w URL: https://doi.org/10.1038/s41598-025-27984-w

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/kehkashan2025explainable.pdf).
- Evidence: PMC article page PMC12647635 (title, authors, journal, year, DOI); PDF from nature.com (open access).

## Problem
Phishing detectors are resource-heavy and opaque.

## Method
Rank features with SHAP, retain top features, train five classical classifiers; ablation with/without SHAP selection.

## Dataset(s)
UCI Phishing Websites dataset (Mohammad et al.), 11,055 records, 30 engineered features (the abstract instead mentions a Kaggle dataset of >11,000 URLs; the paper does not reconcile the two).

## Features
30 UCI binary/ternary features (URL, HTML/JS, domain-based).

## Evaluation protocol
Hold-out; accuracy, precision, recall, F1; ablation without SHAP

## Metrics reported (only numbers present in the source)
RF with SHAP selection: accuracy 97.0%, precision 97.0%, recall 97.6%, F1 97.3%; RF without SHAP 90.0% (ablation); other models 93.3-96.0% (results section/tables as read on PMC).

## Main findings
SHAP-guided feature selection improved all classifiers; RF best.

## Limitations
- Authors' stated limitations: Single small dataset; classical models only.
- My assessment: UCI dataset is 2015-era with pre-extracted features, so no raw URLs and no mutation tests are possible; inconsistent dataset description.

## Research gap
No raw-URL lexical pipeline, no latency or calibration reporting.

## Relevance to our project (score 3/5)
Recent XAI+phishing baseline to contrast with; underlines that most XAI phishing work uses tiny feature-vector datasets rather than raw URL corpora.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
