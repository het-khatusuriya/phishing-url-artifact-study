# lepochat2019tranco

## Citation
Victor Le Pochat, Tom Van Goethem, Samaneh Tajalizadehkhoob, Maciej Korczyński, Wouter Joosen (2019). Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation. *Network and Distributed System Security Symposium (NDSS 2019)*. DOI: 10.14722/ndss.2019.23386; arXiv: 1806.01156

- URL: https://doi.org/10.14722/ndss.2019.23386
- Access status: full_text (research/papers/lepochat2019tranco.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.14722/ndss.2019.23386, NDSS) checked 2026-10-11; full text from arXiv 1806.01156.

## Problem
Top-site lists used as benign ground truth are unstable and manipulable.

## Method
Measurement of top-list instability and manipulability (demonstrates cheap insertion into Alexa); proposes Tranco aggregate list

## Dataset(s)
Alexa, Cisco Umbrella, Majestic and Quantcast top lists over time; 133 security papers surveyed for top-list usage

## Features
N/A

## Evaluation protocol
Longitudinal list comparison; manipulation experiments

## Metrics reported
Shows large day-to-day churn in Alexa and that a domain can be inserted into the top 1M cheaply (Sec. 4-5); many security papers (incl. phishing) use Alexa as benign ground truth (Sec. 3).

## Main findings
Using Alexa as 'legitimate' ground truth is unreliable and manipulable; Tranco is proposed for reproducibility.

## Limitations
**Authors' stated:** Any list is a proxy for popularity, not legitimacy.

**Our caveats:** Popularity lists contain only registrable domains/hostnames, which is the root of the 'www./index page' artefact in URL datasets.

## Research gap
Legitimate-URL sampling beyond popularity lists.

## Relevance to our project
Cite when explaining why our legitimate class (popular, https, www) is a popularity sample rather than a sample of benign browsing, and for choosing Tranco as an external benign FPR test.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
