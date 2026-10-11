# le2011phishdef

## Citation
Le, Anh; Markopoulou, Athina; Faloutsos, Michalis (2011). *PhishDef: URL names say it all*. 2011 Proceedings IEEE INFOCOM, pp. 191-195 (arXiv:1009.2275). DOI: 10.1109/INFCOM.2011.5934995 URL: https://arxiv.org/abs/1009.2275

- Type: conference | Theme (L1): a-foundational-lexical | Access: full_text | Verified: full
- Local PDF: research/papers/le2011phishdef.pdf

## Verification
Checked 2026-10-11: arXiv API record 1009.2275 and arXiv PDF read; Crossref record for DOI 10.1109/INFCOM.2011.5934995 (INFOCOM 2011, pp. 191-195).

## Problem
Client-side, proactive phishing-URL classification resilient to URL obfuscation and noisy training labels.

## Method
Selects lexical features resistant to obfuscation (host/path tokens, lengths, counts), compares lexical-only vs full (host/WHOIS) features, proposes AROW online learning; PhishDef combines these.

## Dataset(s)
PhishTank (4,082 verified phishing, June 2010), MalwarePatrol (2,001), Yahoo random (4,143) and DMOZ random (4,012) URLs; 5 pairings (Table I)

## Features
Lexical: token bag-of-words, length and delimiter counts; external: WHOIS, blacklist, geolocation (for comparison only).

## Evaluation protocol
Online cumulative error over batches of 400 URLs; label-noise injection experiments

## Metrics reported
Lexical-only accuracy 96-98%, within about 1% of full features (Sec. V, Table II); AROW reduces error up to 27% vs CW on DMOZ-Malware (Table III); about 95% accuracy with 5-10% label noise (Sec. V-C); external feature collection averages 1.64 s/URL.
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Lexical features suffice for practical purposes; online AROW is robust to mislabelled data.

## Limitations
- Stated by authors: Small datasets; obfuscation list may be incomplete.
- Our own caveats: Benign classes are directory/random homepages; no temporal split.

## Research gap
Robustness to adversarial token manipulation beyond listed obfuscations.

## Relevance to our project
Direct support for lexical-only detection and for label-noise robustness, which matters for noisy Kaggle-style datasets like ours.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
