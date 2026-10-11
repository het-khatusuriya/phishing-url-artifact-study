# henry2026ensembletransfer

## Citation
Saviour Henry, Bliss Utibe-Abasi Stephen, Philip Asuquo (2026). Ensemble transfer learning for cross-dataset phishing detection. *Franklin Open*, art. 100579. DOI: 10.1016/j.fraope.2026.100579

- URL: https://doi.org/10.1016/j.fraope.2026.100579
- Access status: abstract_only
- Verified: yes
- Theme (L2): c - cross-dataset generalisation
- Relevance score (1-5): 2

## Verification
Crossref record 10.1016/j.fraope.2026.100579 (vol. 15, art. 100579, June 2026) and OpenAlex abstract (gold OA), checked 2026-10-11. PDF download blocked for automated clients.

## Problem
Phishing classifiers degrade sharply when deployed on a dataset different from the training one.

## Method
Cross-Domain Ensemble Probability Fusion: PCA harmonisation into a 20-dim space plus information-theoretic weighted fusion

## Dataset(s)
UCI Phishing Websites dataset and PhiUSIIL phishing URL dataset (zero feature overlap)

## Features
Pre-extracted feature tables harmonised via PCA

## Evaluation protocol
Cross-dataset accuracy before/after the framework

## Metrics reported
Cross-dataset accuracy 57.4% baseline vs 94.4% with the framework (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Reports a 57.4% cross-dataset baseline, i.e., near chance, between two popular phishing datasets.

## Limitations
**Authors' stated:** Not visible from abstract.

**Our caveats:** PCA-harmonising non-overlapping feature sets is hard to interpret; the 94.4% figure needs scrutiny for leakage. Use only the baseline collapse as evidence.

## Research gap
Interpretable cross-dataset adaptation for URL detectors.

## Relevance to our project
Another data point for the cross-dataset collapse on PhiUSIIL-type data (our dataset size matches PhiUSIIL).

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
