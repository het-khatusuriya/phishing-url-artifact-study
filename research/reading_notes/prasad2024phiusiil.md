# prasad2024phiusiil

## Citation
Arvind Prasad, Shalini Chandra (2024). PhiUSIIL: A diverse security profile empowered phishing URL detection framework based on similarity index and incremental learning. *Computers & Security*, art. 103545. DOI: 10.1016/j.cose.2023.103545

- URL: https://doi.org/10.1016/j.cose.2023.103545
- Access status: paywalled
- Verified: yes
- Theme (L2): d - domain-grouped evaluation / dataset provenance
- Relevance score (1-5): 4

## Verification
Semantic Scholar record (DOI, Computers & Security, vol. 136 art. 103545) and UCI ML Repository dataset page (235,795 instances, 54 features, 134,850 legitimate / 100,945 phishing, donated 2024-03-03) checked 2026-10-11.

## Problem
Build a large, diverse phishing-URL dataset and an incremental-learning detector using URL similarity features.

## Method
Similarity-index features (URLSimilarityIndex etc.) plus incremental learning framework

## Dataset(s)
PhiUSIIL Phishing URL dataset: 235,795 URLs (134,850 legitimate, 100,945 phishing) with 54 URL and page-derived features (UCI id 967)

## Features
URL lexical features (length, counts, TLD, https flag, subdomain counts), similarity index, page features

## Evaluation protocol
Not accessible (paywalled); UCI page gives dataset composition only

## Metrics reported
Not accessible from abstract/landing page. (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Provides the dataset most likely matching our ~250k binary URL corpus; its legitimate class is dominated by popular https/'www.' sites (observation from our own data, to be confirmed by our artefact statistics).

## Limitations
**Authors' stated:** Not accessible.

**Our caveats:** If our data is PhiUSIIL, the https/www skew is a property of the dataset construction, and results on it should be accompanied by cross-dataset tests. Several features (e.g., similarity index) are near-label-leaking by construction.

## Research gap
Independent audit of PhiUSIIL artefacts and duplicate domains.

## Relevance to our project
Dataset provenance reference for our own data; the artefact audit we plan is effectively an audit of this dataset.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
