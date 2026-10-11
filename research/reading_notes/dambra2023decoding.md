# dambra2023decoding

## Citation
Savino Dambra, Yufei Han, Simone Aonzo, Platon Kotzias, Antonino Vitale, Juan Caballero, Davide Balzarotti, Leyla Bilge (2023). Decoding the Secrets of Machine Learning in Malware Classification: A Deep Dive into Datasets, Feature Extraction, and Model Performance. *Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security (CCS '23)*. DOI: 10.1145/3576915.3616589; arXiv: 2307.14657

- URL: https://doi.org/10.1145/3576915.3616589
- Access status: full_text (research/papers/dambra2023decoding.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.1145/3576915.3616589, CCS 2023) checked 2026-10-11; full text from arXiv 2307.14657.

## Problem
Malware-classification results depend on dataset construction, feature extraction and family definitions in poorly understood ways.

## Method
Controlled study of how dataset composition (families, samples per family, benign/malware balance), feature type and classifier drive reported performance

## Dataset(s)
67k Windows PE samples from 670 families (100 each) plus benign set; static and dynamic features

## Features
Static and dynamic PE features

## Evaluation protocol
Varies dataset properties systematically; family-aware splits

## Metrics reported
Shows performance strongly tied to dataset nature/distribution (Sec. 5-6).

## Main findings
Near-perfect numbers in prior work are tied to dataset construction choices; family-level grouping and composition matter.

## Limitations
**Authors' stated:** Windows PE only.

**Our caveats:** Analogue: family-aware splits in malware correspond to registered-domain/campaign-grouped splits for URLs.

## Research gap
Equivalent composition study for URL datasets.

## Relevance to our project
Methodological analogue for our domain-grouped split (family-grouped in malware) and for attributing performance to dataset composition.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
