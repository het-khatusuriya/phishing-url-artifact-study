# chen2023continuous

## Citation
Yizheng Chen, Zhoujie Ding, David Wagner (2023). Continuous Learning for Android Malware Detection. *32nd USENIX Security Symposium (USENIX Security 23)*, pp. 1127-1144. arXiv: 2302.04332

- URL: https://www.usenix.org/conference/usenixsecurity23/presentation/chen-yizheng
- Access status: full_text (research/papers/chen2023continuous.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 3

## Verification
USENIX presentation page (authors, pages 1127-1144, PDF) and arXiv API record 2302.04332 ('Published at USENIX Security Symposium 2023'), checked 2026-10-11.

## Problem
Android malware classifiers decay rapidly after deployment; how to keep them accurate with a limited labelling budget?

## Method
Hierarchical contrastive learning plus a new active-learning sample-selection strategy to maintain a drifting classifier with limited analyst labels

## Dataset(s)
Android apps over a 7-year period (AndroZoo-based, time-stamped)

## Features
Drebin-style static features and APIGraph features

## Evaluation protocol
Train on one year, deploy over subsequent months/years with a monthly labelling budget; compares against prior active-learning baselines

## Metrics reported
F1 of a static classifier drops from 0.99 to 0.76 after six months on new samples (Sec. 1); proposed method lowers FNR from 14% to 9% and FPR from 0.86% to 0.48% versus prior active learning (abstract/Sec. 1).

## Main findings
Even strong classifiers decay fast under drift; the choice of which new samples to label matters as much as the model.

## Limitations
**Authors' stated:** Relies on timely analyst labels; Android-only.

**Our caveats:** Transferring to URLs needs a time-stamped phishing feed; our dataset has none.

## Research gap
No equivalent labelling-budget study for phishing URLs.

## Relevance to our project
Concrete quantitative example (0.99 to 0.76 in six months) to cite when arguing that our random-split accuracy is an upper bound.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
