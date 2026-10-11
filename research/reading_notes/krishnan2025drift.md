# krishnan2025drift

## Citation
Sruthi Krishnan, Manohar Naik S (2025). An Efficient Framework for Phishing URL Detection Using Adaptive Drift-Aware Feature Monitoring and Online Learning. *Security and Privacy (Wiley)*. DOI: 10.1002/spy2.70057

- URL: https://doi.org/10.1002/spy2.70057
- Access status: abstract_only
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 2

## Verification
Crossref record for 10.1002/spy2.70057 (title, authors, journal vol. 8 issue 4, issued 2025-06-23) and Semantic Scholar abstract, checked 2026-10-11. Not open access; PDF not downloaded.

## Problem
Phishing URL feature distributions drift, and frequent full retraining is costly.

## Method
Kolmogorov-Smirnov drift detection on feature distributions plus online SGD updates

## Dataset(s)
Real-time phishing URLs from PhishTank (abstract); benign source not stated in abstract

## Features
URL features (dynamic feature selection)

## Evaluation protocol
Not specified in abstract beyond 'validation using real-time phishing URLs from PhishTank'

## Metrics reported
99.85% accuracy, 0.067% false-positive rate (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Claims that drift-aware online learning sustains near-perfect accuracy.

## Limitations
**Authors' stated:** Not visible from abstract.

**Our caveats:** A 99.85%/0.067% result on a PhishTank-centred set is exactly the kind of figure TESSERACT/Arp et al. warn is inflated; no cross-source or base-rate analysis mentioned. Useful as an example of the prevailing evaluation style, not as a benchmark.

## Research gap
Independent, source-disjoint validation of drift-aware URL detectors.

## Relevance to our project
Illustrates the optimistic-metric norm our paper critiques; cite with care.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
