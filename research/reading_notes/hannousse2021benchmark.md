# hannousse2021benchmark

## Citation
Abdelhakim Hannousse, Salima Yahiouche (2021). Towards benchmark datasets for machine learning based website phishing detection: An experimental study. *Engineering Applications of Artificial Intelligence*, art. 104347. DOI: 10.1016/j.engappai.2021.104347; arXiv: 2010.12847

- URL: https://doi.org/10.1016/j.engappai.2021.104347
- Access status: full_text (research/papers/hannousse2021benchmark.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 4

## Verification
Crossref record 10.1016/j.engappai.2021.104347 (vol. 104, art. 104347, 2021) and arXiv API record 2010.12847 with matching journal_ref, checked 2026-10-11. Full text from the arXiv preprint.

## Problem
Findings in phishing-detection ML are dataset dependent and non-replicable; no appropriate benchmark dataset exists for fair evaluation.

## Method
Reproducible dataset-construction scheme with guidelines (G1: collect from several sources; do not use Alexa domain lists directly because they lack sub-domains/paths); feature-importance and runtime analysis; comparison of classifiers

## Dataset(s)
New balanced dataset of 11,430 URLs with 87 features (56 URL, 24 content, 7 external services); phishing from PhishTank/OpenPhish, legitimate from Alexa-derived crawls with paths (Mendeley c2gw7fy2j4)

## Features
87 commonly used features incl. URL length, https, 'www', dots, hyphens, digits, content and WHOIS/rank features

## Evaluation protocol
Random stratified splits on the new dataset; feature relevance via several selectors

## Metrics reported
Random forest reaches about 96.6% accuracy on the full feature set (Sec. 6, Table 9 of preprint); hybrid URL+content features outperform URL-only.

## Main findings
States that findings in the literature 'are dataset dependent and are far away from generalization' because of unreplicable datasets and the Alexa-domain-only sampling problem.

## Limitations
**Authors' stated:** Dataset is small and balanced; external-service features are time-varying.

**Our caveats:** Even with their fix for paths, legitimate URLs still come from popular domains, so popularity/format artefacts persist; balanced 50/50 design contradicts base-rate guidance.

## Research gap
Large, time-stamped, source-diverse URL benchmark with documented artefact statistics.

## Relevance to our project
Independent acknowledgement that legitimate-URL sampling (Alexa index pages) biases URL features; our https/www artefact is a direct instance. Their 87-feature list overlaps our lexical features, useful for the ablation design.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
