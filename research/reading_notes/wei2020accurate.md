# wei2020accurate

## Citation
Wei, Wei; Ke, Qiao; Nowak, Jakub; Korytkowski, Marcin; Scherer, Rafal; Wozniak, Marcin (2020). *Accurate and fast URL phishing detector: A convolutional neural network approach*. Computer Networks, 178, 107275. DOI: 10.1016/j.comnet.2020.107275 URL: https://doi.org/10.1016/j.comnet.2020.107275

- Type: journal | Theme (L1): c-char-level | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1016/j.comnet.2020.107275 (Comput. Netw. 178:107275, 2020); Semantic Scholar abstract summary.

## Problem
Lightweight, fast URL-text-only phishing detector for mobile.

## Method
Char-CNN sized for mobile inference.

## Dataset(s)
Not in abstract (phishing/legitimate URL text)

## Features
Learned char features.

## Evaluation protocol
Not in abstract

## Metrics reported
'Almost 100% accuracy' (abstract) - no precise figures retrieved.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Char-CNN sufficient and fast.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Near-perfect accuracy claims suggest easy/biased data.

## Research gap
Realistic evaluation.

## Relevance to our project
Minor baseline; example of over-optimistic reporting.

Relevance score: 2/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
