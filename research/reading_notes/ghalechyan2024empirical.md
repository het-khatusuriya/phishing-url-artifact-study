# ghalechyan2024empirical

## Citation
Ghalechyan, Hayk; Israyelyan, Elina; Arakelyan, Avag; Hovhannisyan, Gerasim; Davtyan, Arman (2024). *Phishing URL detection with neural networks: an empirical study*. Scientific Reports, 14, 25134. DOI: 10.1038/s41598-024-74725-6 URL: https://doi.org/10.1038/s41598-024-74725-6

- Type: journal | Theme (L1): c-char-level | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1038/s41598-024-74725-6 (Sci. Rep. 14:25134, 2024, CC BY-NC-ND) and OpenAlex abstract. PDF download blocked (Nature signed-URL error; EuropePMC/PMC 403).

## Problem
Does a model trained on open + private data work in production over time?

## Method
Feature engineering without third-party dependencies; deterministic vs probabilistic NNs; daily re-validation.

## Dataset(s)
Combination of open sources (Alexa, PhishTank, OpenPhish) and EasyDMARC production data; daily validation feed

## Features
Engineered URL features (no external lookups).

## Evaluation protocol
Daily validation on newly reported URLs (temporal, production)

## Metrics reported
About 97% average accuracy on daily validation data labelled by PhishTank/OpenPhish/EasyDMARC (abstract); high accuracy on short (<50 chars) and long URLs.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Model trained on open+private data succeeds in production; probabilistic NN improves accuracy.

## Limitations
- Stated by authors: Validation labels may contain mislabelled data that could not be checked (abstract).
- Our own caveats: Private data not shareable; exact architectures unknown here.

## Research gap
Public temporal benchmark.

## Relevance to our project
Supports production-style temporal validation and length-stratified reporting (short vs long URLs) that we can mirror.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
