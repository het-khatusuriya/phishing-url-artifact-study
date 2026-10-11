# zeng2020phishbench

## Citation
Victor Zeng, Shahryar Baki, Ayman El Aassal, Rakesh M. Verma, Luis Felipe Teixeira De Moraes, Avisha Das (2020). Diverse Datasets and a Customizable Benchmarking Framework for Phishing. *Proceedings of the Sixth International Workshop on Security and Privacy Analytics (IWSPA '20)*. DOI: 10.1145/3375708.3380313

- URL: https://doi.org/10.1145/3375708.3380313
- Access status: abstract_only
- Verified: yes
- Theme (L2): e - class imbalance / base rates
- Relevance score (1-5): 2

## Verification
Semantic Scholar record (DOI 10.1145/3375708.3380313, IWSPA@CODASPY 2020) and abstract checked 2026-10-11. ACM copy not under an explicit open licence; not downloaded. Page range not verified -> left out of BibTeX.

## Problem
Lack of diverse, shared datasets and a common benchmarking framework for phishing detection.

## Method
Benchmarking framework (PhishBench) for features and classifiers

## Dataset(s)
Diverse phishing email, website and URL datasets released with PhishBench

## Features
Configurable feature sets

## Evaluation protocol
Framework supports metrics beyond accuracy and imbalanced evaluation

## Metrics reported
None in abstract. (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Researchers 'usually test their proposed methods with limited metrics, datasets, and parameters'; a common benchmark is needed.

## Limitations
**Authors' stated:** Workshop paper.

**Our caveats:** Datasets are 2019-2020 and website-heavy.

## Research gap
A maintained URL benchmark with leakage controls.

## Relevance to our project
Companion to El Aassal 2020; cite for the datasets/benchmark motivation.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
