> **Duplicate record.** Same paper as `sahingoz2019machine` (identical DOI); cite `sahingoz2019machine`. Kept for traceability of the sahingoz2019ebbu2017 search path.

# sahingoz2019ebbu2017

## Citation
Ozgur Koray Sahingoz; Ebubekir Buber; Onder Demir; Banu Diri (2019). *Machine learning based phishing detection from URLs*. Expert Systems with Applications 117:345-357. DOI: 10.1016/j.eswa.2018.09.029 URL: https://doi.org/10.1016/j.eswa.2018.09.029

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Semantic Scholar API record for DOI 10.1016/j.eswa.2018.09.029 (title, authors, ESWA 2019, abstract: RF with NLP features 97.98% accuracy). Volume/pages (117:345-357) from the record's DBLP key and common citations - treat pages as unverified. Dataset file list seen on GitHub (data_phishing_37175.json, data_legitimate_36400.json).

## Problem
Real-time, language-independent URL phishing detection without third-party services.

## Method
Extract NLP word-based features from URL tokens; compare with word-vector features; evaluate seven classifiers.

## Dataset(s)
Ebbu2017. Download: https://github.com/ebubekirbbr/pdd/tree/master/input . License: none stated in repo listing. Timestamps: none. Labels: phishing (PhishTank-sourced) vs legitimate (Yandex search-derived, per commonly cited description - not verified here). Known problems: 2017 vintage; counts inferred from file names.

## Features
Word-level NLP features (brand names, keywords, random-word detection), character statistics.

## Evaluation protocol
Hold-out; accuracy

## Metrics reported (only numbers present in the source)
RF with only NLP features: 97.98% accuracy (abstract).

## Main findings
Word-level lexical features suffice for high accuracy with low latency.

## Limitations
- Authors' stated limitations: n/a (abstract).
- My assessment: Dataset small and old; no timestamps.

## Research gap
n/a

## Relevance to our project (score 4/5)
Third external dataset candidate and a widely cited lexical baseline.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
