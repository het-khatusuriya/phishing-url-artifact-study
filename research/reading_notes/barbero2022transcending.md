# barbero2022transcending

## Citation
Federico Barbero, Feargus Pendlebury, Fabio Pierazzi, Lorenzo Cavallaro (2022). Transcending TRANSCEND: Revisiting Malware Classification in the Presence of Concept Drift. *2022 IEEE Symposium on Security and Privacy (S&P)*. DOI: 10.1109/SP46214.2022.9833659; arXiv: 2010.03856

- URL: https://arxiv.org/abs/2010.03856
- Access status: full_text (research/papers/barbero2022transcending.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.1109/sp46214.2022.9833659, venue IEEE S&P, DBLP conf/sp/BarberoPPC22) and arXiv PDF v6 front matter, checked 2026-10-11.

## Problem
Conformal rejection (Transcend) was empirically useful but lacked a formal basis and was computationally expensive; how to reject drifting samples efficiently and soundly?

## Method
TRANSCENDENT: formal treatment of conformal evaluation; two new conformal evaluators (inductive, cross-conformal) that are cheaper than the original transductive one; classification-with-rejection under drift

## Dataset(s)
Android malware over time (AndroZoo-derived, time-stamped) and other drift settings (Sec. VI)

## Features
Classifier-agnostic

## Evaluation protocol
Time-aware train/test with rejection; compares rejection quality against baselines (probability thresholds, etc.)

## Metrics reported
Reported rejection-vs-performance curves show TRANSCENDENT outperforms the original Transcend and probability-based rejection (Sec. VII; full text).

## Main findings
Rejection via conformal evaluation is a principled, efficient way to cope with drift; naive softmax/probability thresholds are weaker.

## Limitations
**Authors' stated:** Requires periodic calibration; cost of rejected samples must be absorbed by analysts.

**Our caveats:** Benefit for lightweight URL models is untested.

## Research gap
Conformal rejection for URL classifiers remains open.

## Relevance to our project
Reference for the claim that raw ensemble probabilities are a poor out-of-distribution signal; motivates calibration + abstention in our robustness section.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
