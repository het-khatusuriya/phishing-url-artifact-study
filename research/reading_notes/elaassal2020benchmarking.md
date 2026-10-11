# elaassal2020benchmarking

## Citation
Ayman El Aassal, Shahryar Baki, Avisha Das, Rakesh M. Verma (2020). An In-Depth Benchmarking and Evaluation of Phishing Detection Research for Security Needs. *IEEE Access*, pp. 22170-22192. DOI: 10.1109/ACCESS.2020.2969780

- URL: https://doi.org/10.1109/ACCESS.2020.2969780
- Access status: full_text (research/papers/elaassal2020benchmarking.pdf)
- Verified: yes
- Theme (L2): e - class imbalance / base rates
- Relevance score (1-5): 5

## Verification
Semantic Scholar record (DOI, IEEE Access 2020, CC BY) checked 2026-10-11; PDF downloaded from ieeexplore OA link. Page range taken from the PDF.

## Problem
Phishing detection methods are evaluated on inconsistent, often balanced datasets with few metrics; how do they fare under realistic imbalance and on diverse data?

## Method
PhishBench benchmarking framework; systematic feature taxonomies for URLs, websites, emails; evaluation of published methods under varying imbalance and dataset size; feature-importance and extraction-time analysis

## Dataset(s)
New URL, website and email datasets with varying legitimate:phishing ratios; legitimate URLs from diverse sources rather than Alexa domain lists

## Features
Comprehensive URL/website/email feature taxonomy

## Evaluation protocol
Balanced vs imbalanced ratios, scaling experiments, retraining on new attacks

## Metrics reported
Shows that increasing legitimate:phishing ratio degrades the performance of published methods and that 'retraining alone is not enough to defeat new attacks' (abstract; Sec. VII tables).

## Main findings
Explicitly criticises prior work for using balanced datasets and Alexa domain-only legitimate sets; argues for imbalance-aware evaluation, proper metrics and representative datasets.

## Limitations
**Authors' stated:** Feature reproduction of prior work is approximate.

**Our caveats:** 2020-era datasets; still no domain-grouped splitting.

## Research gap
Combining imbalance-aware benchmarking with temporal and domain-grouped splits.

## Relevance to our project
Peer-reviewed support for (i) Alexa-domain sampling bias in legitimate URLs and (ii) evaluating at realistic imbalance; both are central to our paper.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
