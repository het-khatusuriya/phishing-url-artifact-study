# verma2017whatsinaurl

## Citation
Rakesh Verma; Avisha Das (2017). *What's in a URL: Fast Feature Extraction and Malicious URL Detection*. Proceedings of the 3rd ACM International Workshop on Security and Privacy Analytics (IWSPA '17), pp. 55-63. DOI: 10.1145/3041008.3041016 URL: https://doi.org/10.1145/3041008.3041016

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Crossref record for DOI 10.1145/3041008.3041016 (title, authors, proceedings, pages 55-63, 2017); Semantic Scholar record. Full text paywalled.

## Problem
Content-based detectors are slow; can URL-only features be extracted and classified fast?

## Method
Design lexical/character n-gram features computable in linear time; evaluate several classifiers.

## Dataset(s)
Not verified (abstract unavailable).

## Features
Lexical and character-level URL features.

## Evaluation protocol
Classification accuracy and feature-extraction speed

## Metrics reported (only numbers present in the source)
Not verified.

## Main findings
URL-only features allow fast, accurate detection (per title/abstract framing).

## Limitations
- Authors' stated limitations: n/a
- My assessment: Older datasets; no robustness analysis.

## Research gap
n/a

## Relevance to our project (score 3/5)
Early argument for the lexical-only, low-latency design we adopt.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
