# giri2026shieldphish

## Citation
Gandhi Raj Giri (2026). ShieldPhish: Evaluating Representation Robustness and Cross-Source Generalization in Phishing URL Detection. *Zenodo preprint (submitted to IEEE)*. DOI: 10.5281/zenodo.23141305

- URL: https://zenodo.org/records/23141305
- Access status: full_text (research/papers/giri2026shieldphish.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 5

## Verification
Zenodo record 23141305 via Zenodo REST API (title, author, published 2026-10-04, preprint, CC BY 4.0, DOI) checked 2026-10-11. Single-author, non-peer-reviewed.

## Problem
Offline accuracy of lexical phishing-URL classifiers does not transfer to independently sourced traffic; formatting shortcuts (https://, www.) inflate results.

## Method
Diagnoses 'representation shift' (models keying on https:// scheme and leading www.), introduces component-aware URL canonicalisation and hybrid rule fusion, then tests a frozen model on independently sourced, hash-verified post-freeze data

## Dataset(s)
Lexical URL classifier trained on conventional public phishing/benign URL sets; post-freeze external snapshots: OpenPhish (phishing) and a Cisco Umbrella Top-1M snapshot (benign); domain-disjoint

## Features
Lexical URL features / tokens

## Evaluation protocol
Pre-registration-style freeze protocol; domain-disjoint external test; bootstrap 95% CIs; variant-stability tests (same URL re-formatted)

## Metrics reported
Trivial formatting shortcuts (https://, www.) inflate offline accuracy and cause near-100% prediction instability across URL variants; after canonicalisation FPR on secondary benchmarks 0.6%; on the external Umbrella benign set FPR 86.84% (95% CI 83.6-90.0) with phishing recall 91.34% (87.4-94.8) and ROC-AUC 0.460 (0.392-0.524) (abstract).

## Main findings
Removing representation shortcuts is necessary but not sufficient: cross-source benign traffic still breaks a lexical model; the main driver was vocabulary/score distribution shift on unseen benign sources.

## Limitations
**Authors' stated:** Single model family; specific source composition; preprint.

**Our caveats:** Not peer reviewed and single-authored; numbers should be cited as a preprint observation. Nonetheless the failure mode (https/www shortcut, catastrophic FPR on popular benign domains) is exactly ours.

## Research gap
Peer-reviewed replication of the https/www shortcut effect across datasets.

## Relevance to our project
The closest published description of our https://google.com/ failure; supports canonicalisation/artifact-removal ablations and an external benign test set (e.g., Tranco/Umbrella) for FPR.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
