# sommer2010closedworld

## Citation
Robin Sommer, Vern Paxson (2010). Outside the Closed World: On Using Machine Learning for Network Intrusion Detection. *2010 IEEE Symposium on Security and Privacy*. DOI: 10.1109/SP.2010.25

- URL: https://doi.org/10.1109/SP.2010.25
- Access status: paywalled
- Verified: yes
- Theme (L2): e - class imbalance / base rates
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.1109/SP.2010.25, IEEE S&P 2010) checked 2026-10-11.

## Problem
Why is ML-based anomaly detection, despite strong papers, almost never deployed operationally?

## Method
Analysis of why ML anomaly detection is rarely deployed: high cost of errors, semantic gap, diversity of traffic, difficulty of sound evaluation, adversarial setting

## Dataset(s)
Position paper; no dataset

## Features
N/A

## Evaluation protocol
Recommends evaluation with realistic data, understanding of what the system learns, and attention to false-positive cost

## Metrics reported
None. (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Closed-world assumptions and lack of insight into learned features produce systems that look good in the lab and fail in deployment.

## Limitations
**Authors' stated:** NID-specific.

**Our caveats:** The 'semantic gap' maps to our model learning 'looks like a popular www/https site' instead of 'is legitimate'.

## Research gap
N/A

## Relevance to our project
Classic framing citation for the lab-vs-deployment gap and the need to interpret what the model actually learned.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
