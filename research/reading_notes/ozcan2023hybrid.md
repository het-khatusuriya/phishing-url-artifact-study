# ozcan2023hybrid

## Citation
Ozcan, Alper; Catal, Cagatay; Donmez, Emrah; Senturk, Behcet (2023). *A hybrid DNN-LSTM model for detecting phishing URLs*. Neural Computing and Applications, 35(7), pp. 4957-4973 (online 2021). DOI: 10.1007/s00521-021-06401-z URL: https://doi.org/10.1007/s00521-021-06401-z

- Type: journal | Theme (L1): c-char-level | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1007/s00521-021-06401-z (NCA 35(7), 4957-4973, 2023); Semantic Scholar abstract. Springer PDF link returned HTML (not open).

## Problem
Combine char embeddings and NLP features in one deep model.

## Method
DNN branch over NLP features + LSTM over char embeddings, fused.

## Dataset(s)
Phishing URL datasets (sizes not in abstract)

## Features
Char embeddings + NLP lexical features.

## Evaluation protocol
Not in abstract

## Metrics reported
Not in abstract ('outperform other models in accuracy').
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Hybrid feature+sequence model beats single-view models (authors).

## Limitations
- Stated by authors: Not available.
- Our own caveats: No numbers verified.

## Research gap
n/a

## Relevance to our project
Precedent for fusing lexical features with char sequences (our ensemble/hybrid design).

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
