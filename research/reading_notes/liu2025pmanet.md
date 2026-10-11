# liu2025pmanet

## Citation
Liu, Ruitong; Wang, Yanbin; Xu, Haitao; Qin, Zhan; Zhang, Fan; Liu, Yiwei; Cao, Zheng (2025). *PMANet: Malicious URL detection via post-trained language model guided multi-level feature attention network*. Information Fusion, 113, 102638. DOI: 10.1016/j.inffus.2024.102638 URL: https://doi.org/10.1016/j.inffus.2024.102638

- Type: journal | Theme (L1): d-transformer-llm | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1016/j.inffus.2024.102638 (Inf. Fusion 113:102638, 2025); Semantic Scholar abstract.

## Problem
Domain adaptation of pre-trained LMs to URLs with multi-level feature fusion.

## Method
Post-training (masked token, noisy-text recognition, domain discrimination) then attention-based fusion network.

## Dataset(s)
Public URL datasets (specifics not in abstract)

## Features
Learned char/sub-word features.

## Evaluation protocol
Small-data, class-imbalance and adversarial scenarios; 20-URL live case study (abstract)

## Metrics reported
AUC 0.9941; all 20 malicious URLs in case study detected (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Post-training + multi-level attention improves robustness.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Same group as TransURL/URLBERT; heavy models.

## Research gap
Explainability, cost.

## Relevance to our project
Strong deep baseline; code/data reported on GitHub.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
