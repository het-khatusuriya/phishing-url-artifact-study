# axelsson2000baserate

## Citation
Stefan Axelsson (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*. DOI: 10.1145/357830.357849

- URL: https://doi.org/10.1145/357830.357849
- Access status: abstract_only
- Verified: yes
- Theme (L2): e - class imbalance / base rates
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.1145/357830.357849, TISSEC 2000) checked 2026-10-11. ACM copy is 'bronze' without an explicit open licence, so not downloaded.

## Problem
Low attack prevalence makes even small false-positive rates dominate alarms, limiting the usefulness of detectors.

## Method
Bayesian analysis of detector alarms under low attack prevalence

## Dataset(s)
Analytical; no dataset

## Features
N/A

## Evaluation protocol
Shows that with realistic base rates the false-alarm rate dominates the Bayesian detection rate (positive predictive value)

## Metrics reported
Classic result: to achieve a useful PPV at low prevalence the FPR must be on the order of 1e-5 (Sec. 4-5 of original). (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Accuracy/TPR on balanced data say little about operational usefulness; precision collapses at low prevalence.

## Limitations
**Authors' stated:** Intrusion-detection framing.

**Our caveats:** Prevalence of phishing among URLs a user visits is far below 50%, so our balanced-set precision is not meaningful operationally.

## Research gap
Base-rate-adjusted reporting is still rare in phishing-URL papers.

## Relevance to our project
Foundational citation for reporting precision at realistic prevalence and for class-imbalance discussion.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
