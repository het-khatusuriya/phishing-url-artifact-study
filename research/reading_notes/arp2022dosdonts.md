# arp2022dosdonts

## Citation
Daniel Arp, Erwin Quiring, Feargus Pendlebury, Alexander Warnecke, Fabio Pierazzi, Christian Wressnegger, Lorenzo Cavallaro, Konrad Rieck (2022). Dos and Don'ts of Machine Learning in Computer Security. *31st USENIX Security Symposium (USENIX Security 22)*, pp. 3971-3988. arXiv: 2010.09470

- URL: https://www.usenix.org/conference/usenixsecurity22/presentation/arp
- Access status: full_text (research/papers/arp2022dosdonts.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 5

## Verification
USENIX presentation page (authors/affiliations, pages 3971-3988, Distinguished Paper Award, PDF) and arXiv API record 2010.09470, checked 2026-10-11.

## Problem
Subtle design/evaluation pitfalls make ML security results unrealistic; how prevalent are they and how much do they inflate results?

## Method
Taxonomy of ten pitfalls: P1 sampling bias, P2 label inaccuracy, P3 data snooping, P4 spurious correlations, P5 biased parameter selection, P6 inappropriate baseline, P7 inappropriate performance measures, P8 base rate fallacy, P9 lab-only evaluation, P10 inappropriate threat model; prevalence survey and author feedback

## Dataset(s)
Literature study of 30 top-tier security papers (2010-2020) plus four impact case studies (mobile malware, vulnerability discovery, source-code authorship, network intrusion detection)

## Features
Shows via explanation methods how artefacts create shortcut patterns (P4)

## Evaluation protocol
Prevalence analysis across 30 papers; controlled experiments showing each pitfall's inflation effect

## Metrics reported
Each pitfall is present in a majority of surveyed papers (e.g., sampling bias and data snooping are marked present in most; see Fig. 2/Table 1). Base-rate example: a 1% FPR at a 1:100 ratio yields roughly one false alarm per true positive (Sec. 2, P8).

## Main findings
Spurious correlations ('artifacts unrelated to the security problem create shortcut patterns for separating classes') and sampling bias are endemic; recommends explanation-based artefact checks, temporal splits, realistic base rates and precision/recall reporting.

## Limitations
**Authors' stated:** Survey limited to top venues and 30 papers; pitfall boundaries overlap.

**Our caveats:** Does not include a phishing-URL case study, but P1/P4/P8 map one-to-one to our situation.

## Research gap
A phishing-URL instantiation of the pitfall analysis with concrete artefact ablations.

## Relevance to our project
Primary framing reference. Our https/'www.' imbalance is P1 (sampling bias) producing P4 (spurious correlations); our balanced test set hides P8 (base-rate fallacy). Our artifact-removal ablation is the authors' recommended remedy for P4.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
