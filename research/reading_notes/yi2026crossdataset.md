# yi2026crossdataset

## Citation
Yi, Liyan; Omotosho, Adebayo; Balogun, Hamed (2026). *Phishing URL Detection and Interpretability With Machine Learning: A Cross-Dataset Approach*. Security and Privacy (Wiley), 9(1), e70175. DOI: 10.1002/spy2.70175 URL: https://doi.org/10.1002/spy2.70175

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1002/spy2.70175 (Security and Privacy 9(1) e70175, 2026, CC BY) with abstract; OpenAlex. Wiley PDF blocked for automated download.

## Problem
Assess whether a fixed URL feature set generalises across datasets and explain decisions.

## Method
Trains three tree ensembles; evaluates on secondary datasets; SHAP for feature attribution.

## Dataset(s)
Primary email-URL dataset plus secondary/test datasets (four test sets in total; names not in abstract)

## Features
URL structural/lexical features (specifics not in abstract).

## Evaluation protocol
Cross-dataset: train on primary set, evaluate on four secondary test sets

## Metrics reported
Across four test sets: average classification error 4.03%, average accuracy 94% (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Tree ensembles with a common lexical feature set transfer reasonably across datasets; SHAP highlights consistent key features.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Abstract-level only; cannot verify whether test sets share sources with training data.

## Research gap
Domain-grouped splits, calibration, artifact analysis.

## Relevance to our project
Directly comparable 2026 cross-dataset + SHAP study; our work should position against it.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
