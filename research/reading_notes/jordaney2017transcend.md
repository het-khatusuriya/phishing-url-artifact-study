# jordaney2017transcend

## Citation
Roberto Jordaney, Kumar Sharad, Santanu K. Dash, Zhi Wang, Davide Papini, Ilia Nouretdinov, Lorenzo Cavallaro (2017). Transcend: Detecting Concept Drift in Malware Classification Models. *26th USENIX Security Symposium (USENIX Security 17)*, pp. 625-642. 

- URL: https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/jordaney
- Access status: full_text (research/papers/jordaney2017transcend.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 3

## Verification
USENIX presentation page (title, authors/affiliations, pages 625-642, PDF link) checked 2026-10-11.

## Problem
Deployed classifiers silently age under concept drift; how can a model know that its prediction is no longer supported by its training data?

## Method
Conformal-evaluator framework: non-conformity measures and p-value-based credibility/confidence to detect when a deployed classifier's decisions are no longer supported by training data; rejection of drifting samples

## Dataset(s)
Android (Drebin and Marvin datasets) and Windows malware families (Sec. 5)

## Features
Classifier-agnostic; evaluated with Drebin SVM features and others

## Evaluation protocol
Train on older data, test on newer; measures how rejection thresholds trade off kept-accuracy vs rejected fraction

## Metrics reported
Shows that rejecting low-credibility predictions restores high precision on drifted Android/Windows data (Sec. 5 tables; full text).

## Main findings
Statistical assessment of prediction quality can flag aging models before accuracy visibly collapses; ties drift detection to a decision to abstain.

## Limitations
**Authors' stated:** Calibration set requirements and computational cost of conformal p-values; threshold selection needs validation data.

**Our caveats:** Not evaluated on URLs; conformal credibility depends on a meaningful distance in feature space, which is weak for sparse lexical URL features.

## Research gap
Abstention/rejection as an answer to drift is almost absent from phishing-URL papers.

## Relevance to our project
Supports adding a rejection option / credibility score to our ensemble as part of the calibration analysis rather than forcing a binary decision on out-of-distribution URLs like https://google.com/.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
