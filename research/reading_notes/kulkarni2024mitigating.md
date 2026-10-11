# kulkarni2024mitigating

## Citation
Aditya Kulkarni, Vivek Balachandran, Dinil Mon Divakaran, Tamal Das (2024). Mitigating Bias in Machine Learning Models for Phishing Webpage Detection. *arXiv preprint*. arXiv: 2401.08363

- URL: https://arxiv.org/abs/2401.08363
- Access status: full_text (research/papers/kulkarni2024mitigating.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 2

## Verification
arXiv abstract page and arXiv API record 2401.08363 (16 Jan 2024, no journal ref) checked 2026-10-11.

## Problem
Dataset assembly biases (imbalance, staleness, narrow sources) skew phishing-webpage classifiers.

## Method
Identifies dataset-assembly biases (imbalanced, non-diverse, stale datasets; zero-day gap) and proposes a tool to synthesise phishing pages for any set of legitimate URLs to debias/test detectors

## Dataset(s)
Position paper; proposes generating synthetic phishing pages from legitimate URLs

## Features
Content and visual phishing cues injected into legitimate pages

## Evaluation protocol
None reported (short paper)

## Metrics reported
None.

## Main findings
Argues that classifiers 'learn distinctive features from training data' and that biased dataset composition skews decision rules; proposes synthetic augmentation.

## Limitations
**Authors' stated:** No evaluation.

**Our caveats:** Short preprint, limited evidence; include only as a recent explicit statement of dataset bias in phishing detection.

## Research gap
Empirical measurement of how much dataset composition bias changes learned rules.

## Relevance to our project
Minor supporting citation for the dataset-bias problem statement.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
