# wang2019pdrcnn

## Citation
Wang, Weiping; Zhang, Feng; Luo, Xi; Zhang, Shigeng (2019). *PDRCNN: Precise Phishing Detection with Recurrent Convolutional Neural Networks*. Security and Communication Networks, 2019, Article 2595794, pp. 1-15. DOI: 10.1155/2019/2595794 URL: https://doi.org/10.1155/2019/2595794

- Type: journal | Theme (L1): c-char-level | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1155/2019/2595794 (SCN 2019, CC BY) and Crossref/OpenAlex abstract. Hindawi/Wiley PDF blocked by bot protection despite CC BY licence.

## Problem
Fast URL-only phishing detection without page content or third-party services.

## Method
URL encoded as 2-D tensor; BiLSTM extracts global features; CNN selects key characters; fixed-length vector -> classifier.

## Dataset(s)
Nearly 500,000 URLs from Alexa (benign) and PhishTank (phishing) (abstract)

## Features
Learned character features.

## Evaluation protocol
Not in abstract

## Metrics reported
Accuracy 97%, AUC 99%, 0.4 ms per URL (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
RNN+CNN hybrid beats either alone.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Alexa-vs-PhishTank construction (homepage shortcut).

## Research gap
Realistic benign class.

## Relevance to our project
Representative hybrid RNN-CNN baseline; dataset construction illustrates the artifact we study.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
