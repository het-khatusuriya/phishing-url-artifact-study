# fernando2026driftphish

## Citation
Warren Fernando, Nikos Komninos (2026). Evaluating and Combating the Impact of Concept Drift on the Performance of Machine Learning-Based Phishing Detection Systems. *arXiv preprint*. arXiv: 2606.11471

- URL: https://arxiv.org/abs/2606.11471
- Access status: full_text (research/papers/fernando2026driftphish.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 2

## Verification
arXiv abstract page and arXiv API record 2606.11471 (submitted 9 Jun 2026, cs.CR/cs.LG, no journal ref) checked 2026-10-11.

## Problem
ML phishing (email) detectors degrade as attacks evolve; how to quantify drift and reduce the degradation?

## Method
Statistical framework (adapted from the FeSAD ransomware drift framework) to quantify similarity of phishing vs benign samples and flag drifted samples; feature-robustness analysis across time

## Dataset(s)
Public phishing/spam email corpora (the paper is email-centric, not URL-centric; see PDF Sec. 2-4)

## Features
Email text/structural features

## Evaluation protocol
Temporal evaluation across dataset periods with drift scoring

## Metrics reported
Full text available, but headline numbers are not summarised in the abstract; treat quantitative claims cautiously (preprint).

## Main findings
Argues that phishing detectors degrade with evolution of attacks and that a drift score can be used to decide re-training.

## Limitations
**Authors' stated:** Preprint; limited datasets.

**Our caveats:** Email modality; relevance to URL lexical models is indirect. Included to show that 2026 work still frames phishing drift mainly through emails, leaving URL drift under-studied.

## Research gap
URL-level drift quantification with public time-stamped data.

## Relevance to our project
Weak direct relevance; cite only as recent evidence that concept drift in phishing detection remains an open problem.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
