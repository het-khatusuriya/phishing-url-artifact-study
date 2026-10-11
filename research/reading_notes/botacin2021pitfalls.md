# botacin2021pitfalls

## Citation
Marcus Botacin, Fabricio Ceschin, Ruimin Sun, Daniela Oliveira, André Grégio (2021). Challenges and pitfalls in malware research. *Computers & Security*, art. 102287. DOI: 10.1016/j.cose.2021.102287

- URL: https://doi.org/10.1016/j.cose.2021.102287
- Access status: abstract_only
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 2

## Verification
Semantic Scholar record (DOI 10.1016/j.cose.2021.102287, vol. 106 art. 102287, 2021) and abstract checked 2026-10-11. Elsevier bronze access; not downloaded.

## Problem
Malware research suffers recurring methodological pitfalls that limit impact and reproducibility.

## Method
Literature review identifying 20 pitfalls (threat model, closed datasets, ground truth from closed-source AV, etc.)

## Dataset(s)
Systematic review of 491 malware papers (2000-2018)

## Features
N/A

## Evaluation protocol
N/A

## Metrics reported
20 pitfalls identified across 491 papers (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)

## Main findings
Dataset and ground-truth practices (private datasets, AV-label ground truth, non-deterministic analysis) limit validity and reproducibility.

## Limitations
**Authors' stated:** Malware focus; through 2018.

**Our caveats:** Secondary relevance; complements Arp et al. with reproducibility pitfalls.

## Research gap
N/A

## Relevance to our project
Supporting citation for ground-truth/label-source pitfalls (our labels come from blacklists).

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
