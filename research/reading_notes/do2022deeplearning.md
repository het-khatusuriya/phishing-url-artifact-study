# do2022deeplearning

## Citation
Nguyet Quang Do, Ali Selamat, Ondrej Krejcar, Enrique Herrera-Viedma, Hamido Fujita (2022). Deep Learning for Phishing Detection: Taxonomy, Current Challenges and Future Directions. *IEEE Access*, pp. 36429-36463. DOI: 10.1109/ACCESS.2022.3151903

- URL: https://doi.org/10.1109/ACCESS.2022.3151903
- Access status: full_text (research/papers/do2022deeplearning.pdf)
- Verified: yes
- Theme (L2): f - surveys & SoKs discussing evaluation
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.1109/ACCESS.2022.3151903, IEEE Access 2022, CC BY) checked 2026-10-11; PDF from ieeexplore OA link. Page range taken from the PDF.

## Problem
DL phishing detection lacks a taxonomy and faces dataset, metric and drift challenges.

## Method
Taxonomy of DL approaches; analysis of datasets, features, metrics, challenges

## Dataset(s)
Systematic review of DL phishing-detection papers

## Features
Survey of URL/content/hybrid features

## Evaluation protocol
Reports that many works train on old, non-diverse or highly imbalanced data and use accuracy on imbalanced sets

## Metrics reported
Qualitative; states that 'datasets comprising of old phishing attacks do not represent real attack scenarios', that accuracy/error rate are unsuitable for imbalanced data, and that batch learning adapts poorly to concept drift (Sec. VI-VII).

## Main findings
Dataset recency/diversity/imbalance and metric choice are listed as open challenges; recommends online learning for drift.

## Limitations
**Authors' stated:** Review scope; recommends a 'recent and balanced dataset', which conflicts with base-rate advice.

**Our caveats:** Their 'balanced dataset' recommendation illustrates the field's inconsistency on class ratios.

## Research gap
Clear guidance on realistic prevalence in evaluation.

## Relevance to our project
Survey citation for dataset staleness, imbalance and drift as acknowledged challenges in DL phishing detection.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
