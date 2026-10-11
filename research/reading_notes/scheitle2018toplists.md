# scheitle2018toplists

## Citation
Quirin Scheitle, Oliver Hohlfeld, Julien Gamba, Jonas Jelten, Torsten Zimmermann, Stephen D. Strowes, Narseo Vallina-Rodriguez (2018). A Long Way to the Top: Significance, Structure, and Stability of Internet Top Lists. *Proceedings of the Internet Measurement Conference 2018 (IMC '18)*. DOI: 10.1145/3278532.3278574; arXiv: 1805.11506

- URL: https://doi.org/10.1145/3278532.3278574
- Access status: full_text (research/papers/scheitle2018toplists.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 2

## Verification
Semantic Scholar record (DOI 10.1145/3278532.3278574, IMC 2018) checked 2026-10-11; full text from arXiv 1805.11506 (ACM page range not verified, so omitted).

## Problem
Research results depend on which top list (and which day) is used, yet lists differ structurally and churn heavily.

## Method
Structural and stability analysis of top lists and their effect on research results

## Dataset(s)
Alexa, Umbrella, Majestic lists; survey of list use in measurement/security papers

## Features
N/A

## Evaluation protocol
Repeats several published measurements with different lists/dates to show result sensitivity

## Metrics reported
Demonstrates that list choice and date materially change research conclusions (Sec. 6).

## Main findings
Top lists differ strongly in structure (e.g., Umbrella contains many non-web hosts) and churn; results that depend on them are fragile.

## Limitations
**Authors' stated:** Measurement scope.

**Our caveats:** Relevance is indirect: it quantifies how arbitrary the 'legitimate' class becomes when sourced from a list.

## Research gap
N/A

## Relevance to our project
Supporting citation for benign-sampling bias; secondary to Tranco.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
