# mamun2016iscxurl

## Citation
Mohammad Saiful Islam Mamun; Mohammad Ahmad Rathore; Arash Habibi Lashkari; Natalia Stakhanova; Ali A. Ghorbani (2016). *Detecting Malicious URLs Using Lexical Analysis*. Network and System Security (NSS 2016), LNCS 9955, pp. 467-482, Springer. DOI: 10.1007/978-3-319-46298-1_30 URL: https://doi.org/10.1007/978-3-319-46298-1_30

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/mamun2016iscxurl.pdf).
- Evidence: Crossref record for DOI 10.1007/978-3-319-46298-1_30 (title, authors, LNCS, pp. 467-482, 2016); UNB CIC dataset page; author chapter PDF from cyberlab.usask.ca.

## Problem
Lightweight categorisation of malicious URLs by attack type using lexical cues.

## Method
Extract lexical features, select sufficient feature subsets, classify with tree-based and kNN methods; study obfuscation techniques per URL type.

## Dataset(s)
ISCX-URL-2016 (see Dataset section). Download: http://cicresearch.ca/CICDataset/ISCX-URL-2016/ (UNB CIC page). License: none stated (UNB copyright). Timestamps: none in released CSVs (lexical feature files). Labels: benign / spam / phishing / malware / defacement by source.

## Features
URL length, token counts, entropy-like and character statistics (paper Table 1).

## Evaluation protocol
Per-class and multi-class accuracy; feature selection

## Metrics reported (only numbers present in the source)
~99% accuracy for single-type detection and 93-99% as a group with Random Forest (abstract/Sec. 5; Table 2a: >97% on single-class datasets).

## Main findings
Lexical analysis is effective and efficient; RF best; obfuscation types differ by attack class.

## Limitations
- Authors' stated limitations: Class labels inherited from sources; dataset era 2016.
- My assessment: Source-per-class design means classifiers can learn source artefacts (Arp et al. pitfall); benign = Alexa top sites only.

## Research gap
Temporal metadata absent; URL strings in the public release are partially feature-only.

## Relevance to our project (score 5/5)
Upstream source of our Kaggle corpus; critical for understanding label provenance and potential shortcut features.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
