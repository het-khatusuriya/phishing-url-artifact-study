# apruzzese2022spacephish

## Citation
Giovanni Apruzzese, Mauro Conti, Ying Yuan (2022). SpacePhish: The Evasion-space of Adversarial Attacks against Phishing Website Detectors using Machine Learning. *Proceedings of the 38th Annual Computer Security Applications Conference (ACSAC 2022)*, pp. 171-185. DOI: 10.1145/3564625.3567980; arXiv: 2210.13660

- URL: https://doi.org/10.1145/3564625.3567980
- Access status: full_text (research/papers/apruzzese2022spacephish.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 4

## Verification
Crossref record 10.1145/3564625.3567980 (title, authors, ACSAC 2022, pages 171-185) checked 2026-10-11. Note: the downloaded arXiv PDF (2210.13660v3) is the extended journal version titled 'Multi-SpacePhish' with author order Yuan, Apruzzese, Conti.

## Problem
It is unclear where (problem space vs feature space) realistic, cheap adversarial perturbations against ML phishing detectors can be introduced and how damaging they are.

## Method
Formalises the 'evasion-space' (problem-space vs feature-space perturbations) and a realistic threat model; evaluates 12 cheap evasion attacks

## Dataset(s)
Two public phishing website datasets (Zenodo and delta-phish style collections; see Sec. 5 of PDF), 18 ML-PWD configurations

## Features
URL-only, HTML-only and combined feature sets for the ML-PWD

## Evaluation protocol
Statistical significance testing of detection-rate degradation across 18 detectors and 12 attacks, repeated trials

## Metrics reported
Realistic cheap evasions induce a statistically significant 3-10% degradation; combined problem+feature-space perturbations can drop detection rate from 0.95 to 0 (extended version abstract).

## Main findings
Even trivial, cheap URL/HTML manipulations measurably reduce detection; some detectors are immune to some attacks, so robustness must be measured per feature set.

## Limitations
**Authors' stated:** Only two datasets; attacks are heuristic.

**Our caveats:** The URL-feature detectors' sensitivity to small lexical perturbations is the same vulnerability our scheme/www artefact exposes.

## Research gap
Joint analysis of artefact reliance and evasion susceptibility.

## Relevance to our project
Methodological model for our robustness analysis (cheap perturbations, significance tests) on URL-feature ensembles.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
