# aljofey2022effective

## Citation
Ali Aljofey, Qingshan Jiang, Abdur Rasool, Hui Chen, Wenyin Liu, Qiang Qu, Yang Wang (2022). An effective detection approach for phishing websites using URL and HTML features. *Scientific Reports*, art. 8842. DOI: 10.1038/s41598-022-10841-5

- URL: https://doi.org/10.1038/s41598-022-10841-5
- Access status: abstract_only
- Verified: yes
- Theme (L2): c - cross-dataset generalisation
- Relevance score (1-5): 2

## Verification
Semantic Scholar record (DOI, Sci Rep 2022, CC BY, PubMed 35614133) checked 2026-10-11. PDF download from nature.com/PMC blocked for automated clients; abstract only.

## Problem
Detect zero-hour phishing websites without third-party services and validate on more than one dataset.

## Method
XGBoost on URL character sequences, hyperlink features and TF-IDF of noisy HTML/plaintext

## Dataset(s)
Self-built dataset of 60,252 webpages (32,972 benign, 27,280 phishing) plus a benchmark dataset for external validation

## Features
URL char-level sequence features, hyperlink relations, text TF-IDF; no third-party services

## Evaluation protocol
Evaluation on own dataset and on a second benchmark dataset (cross-dataset check)

## Metrics reported
96.76% accuracy with 1.39% FPR on own data; 98.48% accuracy with 2.09% FPR on the benchmark dataset (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Reports that a model built for zero-hour detection transfers to a second dataset; one of the few mainstream papers to include an external dataset.

## Limitations
**Authors' stated:** Lack of large public datasets motivated self-collection.

**Our caveats:** Content-heavy; cross-dataset result involves retraining on the benchmark rather than a frozen-model transfer (verify in full text before citing as generalisation).

## Research gap
Frozen-model external validation is still rare.

## Relevance to our project
Example of a widely cited phishing paper where 'external dataset' evaluation exists but needs careful reading; useful contrast for our frozen-model cross-dataset protocol.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
