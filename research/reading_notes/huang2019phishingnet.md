# huang2019phishingnet

## Citation
Huang, Yongjie; Yang, Qiping; Qin, Jinghui; Wen, Wushao (2019). *Phishing URL Detection via CNN and Attention-Based Hierarchical RNN*. 2019 18th IEEE International Conference on Trust, Security and Privacy in Computing and Communications / 13th IEEE International Conference on Big Data Science and Engineering (TrustCom/BigDataSE), pp. 112-119. DOI: 10.1109/TrustCom/BigDataSE.2019.00024 URL: https://doi.org/10.1109/TrustCom/BigDataSE.2019.00024

- Type: conference | Theme (L1): c-char-level | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1109/TrustCom/BigDataSE.2019.00024 (TrustCom/BigDataSE 2019, pp. 112-119); Semantic Scholar and OpenAlex abstract. IEEE Xplore page not fetchable.

## Problem
Zero-day phishing URL detection without manual features.

## Method
Character CNN for spatial features, word-level hierarchical RNN with attention for temporal features, CNN fusion, classifier.

## Dataset(s)
'Verified dataset collected from the Internet' (abstract); sizes not available

## Features
Learned char and word representations.

## Evaluation protocol
Not available; abstract emphasises generalisation to newly emerging URLs

## Metrics reported
Not in abstract ('competitive performance').
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Fused char/word representations improve generalisation on new URLs (authors' claim).

## Limitations
- Stated by authors: Not available.
- Our own caveats: No public code/data located.

## Research gap
Reproducibility.

## Relevance to our project
Example of char+word hybrid with attention; attention weights are a potential explainability hook for our char branch.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
