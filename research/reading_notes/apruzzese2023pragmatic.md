# apruzzese2023pragmatic

## Citation
Giovanni Apruzzese, Pavel Laskov, Johannes Schneider (2023). SoK: Pragmatic Assessment of Machine Learning for Network Intrusion Detection. *2023 IEEE 8th European Symposium on Security and Privacy (EuroS&P)*, pp. 592-614. DOI: 10.1109/EuroSP57164.2023.00042; arXiv: 2305.00550

- URL: https://doi.org/10.1109/EuroSP57164.2023.00042
- Access status: full_text (research/papers/apruzzese2023pragmatic.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 3

## Verification
Crossref record 10.1109/eurosp57164.2023.00042 (title, authors, EuroS&P 2023, pages 592-614) and arXiv API record 2305.00550, checked 2026-10-11.

## Problem
Practitioners distrust ML for intrusion detection because papers omit information (variance, costs, cross-dataset behaviour) needed to judge real value.

## Method
Defines 'pragmatic assessment': report what practitioners need (hardware, data pre-processing, costs, multiple datasets, statistical variance over many trials); hundreds of thousands of model runs to quantify variance

## Dataset(s)
Systematisation of NID papers plus large experimental campaign on public NID datasets (Sec. 5-6) and a practitioner survey

## Features
N/A (NID flows)

## Evaluation protocol
Multiple random seeds/splits, multiple datasets, reporting of runtime and resources; shows how single-split results mislead

## Metrics reported
Demonstrates run-to-run variance large enough to change rankings of methods (Sec. 6, full text).

## Main findings
Single-dataset, single-run evaluations are unreliable; cross-dataset and repeated-trial reporting should be standard.

## Limitations
**Authors' stated:** NID-specific datasets.

**Our caveats:** The methodology (repeat trials, cross-dataset, cost reporting) transfers directly to URL classification.

## Research gap
Pragmatic assessment has not been applied to phishing URL detectors.

## Relevance to our project
Template for our evaluation protocol: multiple seeds, multiple datasets, confidence intervals, and deployment-oriented reporting.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
