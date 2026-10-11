# mia2024featurestrust

## Citation
Maraz Mia, Darius Derakhshan, Mir Mehedi A. Pritom (2024). Can Features for Phishing URL Detection Be Trusted Across Diverse Datasets? A Case Study with Explainable AI. *Proceedings of the 11th International Conference on Networking, Systems, and Security (NSysS 2024)*, pp. 137-145. DOI: 10.1145/3704522.3704532; arXiv: 2411.09813

- URL: https://doi.org/10.1145/3704522.3704532
- Access status: full_text (research/papers/mia2024featurestrust.pdf)
- Verified: yes
- Theme (L2): c - cross-dataset generalisation
- Relevance score (1-5): 5

## Verification
Crossref record 10.1145/3704522.3704532 (title, authors, NSysS 2024, pages 137-145, CC BY) and arXiv abstract page 2411.09813, checked 2026-10-11.

## Problem
Are the features that make phishing-URL classifiers accurate on one dataset trustworthy on another?

## Method
Train/test within and across datasets (Exp-1..6); SHAP global/local explanations to compare feature contribution

## Dataset(s)
Dataset-1: Vrbancic et al. (88,647 instances, 58,000 benign); Dataset-2: Kaggle set with 19,431 rows (9,716 benign); 20 overlapping numeric URL features

## Features
Lexical counts (dots, hyphens, '@', 'and', url length, domain_in_ip, Google index flag, etc.)

## Evaluation protocol
Random splits within dataset; cross-dataset transfer on common features; merged training

## Metrics reported
Within-dataset accuracy is high, but cross-dataset accuracy 'drops drastically to 51%' (train D1, test D2) and 59% (train D2, test D1) (Sec. 3.5); SHAP shows the same feature (e.g., url_google_index, qty_dot_url) changing sign/importance across datasets.

## Main findings
Features are dataset dependent; near-chance cross-dataset accuracy from models that look excellent in-distribution.

## Limitations
**Authors' stated:** Only two datasets; only overlapping features.

**Our caveats:** Datasets are pre-extracted feature tables, so raw-URL artefacts (scheme/www) cannot be ablated.

## Research gap
Cross-dataset tests on raw URLs with controllable artefacts.

## Relevance to our project
Directly quantifies the cross-dataset collapse we expect; SHAP-based comparison is a template for our feature-importance analysis before/after artefact removal.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
