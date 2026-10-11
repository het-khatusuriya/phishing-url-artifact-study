# rashid2024domainadapt

## Citation
Fariza Rashid, Ben Doyle, Soyeon Caren Han, Suranga Seneviratne (2024). Phishing URL detection generalisation using Unsupervised Domain Adaptation. *Computer Networks*, art. 110398. DOI: 10.1016/j.comnet.2024.110398

- URL: https://doi.org/10.1016/j.comnet.2024.110398
- Access status: abstract_only
- Verified: yes
- Theme (L2): c - cross-dataset generalisation
- Relevance score (1-5): 5

## Verification
Crossref record (vol. 245, art. 110398, May 2024), Semantic Scholar (CC BY hybrid OA) and OpenAlex abstract, checked 2026-10-11. Publisher PDF download blocked for automated clients; abstract only.

## Problem
URL-based phishing detectors work only when the test set is split from the same dataset; they do not generalise across datasets collected at different vantage points.

## Method
Unsupervised domain adaptation framework to transfer URL classifiers between datasets

## Dataset(s)
Three phishing-URL datasets (abstract); pairwise cross-dataset experiments

## Features
Lexical/learned URL representations

## Evaluation protocol
Train on one dataset, test on another (cross-dataset F1), with and without adaptation

## Metrics reported
Cross-dataset F1 improves by 0.06 on average and up to about 0.2 with adaptation (abstract). Secondary reports (not verified from full text) attribute part of the baseline drop to URL-length shift and the classifiers' focus on specific tokens such as 'www'. (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Existing ML/DL URL detectors 'work effectively only when the test sets are split from the same training dataset'; format differences between collection vantage points (how URLs are recorded) are an explicit cause.

## Limitations
**Authors' stated:** Not visible from abstract.

**Our caveats:** Full text not accessed; the 'www' token claim must be verified before citing it as the paper's finding.

## Research gap
Explains cross-dataset drops mechanistically (format artefacts) rather than only reporting them.

## Relevance to our project
Peer-reviewed confirmation that URL classifiers do not generalise across datasets and that recording format matters, which is the rationale for our cross-dataset tests and canonicalisation ablation.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
