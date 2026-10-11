# liu2024transurl

## Citation
Liu, Ruitong; Wang, Yanbin; Guo, Zhenhao; Xu, Haitao; Qin, Zhan; Ma, Wenrui; Zhang, Fan (2024). *TransURL: Improving malicious URL detection with multi-layer Transformer encoding and multi-scale pyramid features*. Computer Networks, 253, 110707 (arXiv:2312.00508, formerly 'PyraTrans'). DOI: 10.1016/j.comnet.2024.110707 URL: https://arxiv.org/abs/2312.00508

- Type: journal | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/liu2024transurl.pdf

## Verification
Checked 2026-10-11: arXiv API record 2312.00508 (v3 2025-03-21; journal ref Computer Networks 253 (2024) 110707) and arXiv PDF read; Crossref record for DOI 10.1016/j.comnet.2024.110707.

## Problem
Transformers miss local/character/structural cues in URLs; improve robustness and generalisation.

## Method
Co-trains char-aware transformer with pyramid/multi-scale modules; baselines URLNet, GramBeddings, URLTran, TextCNN etc.; code released (github.com/Vul-det/TransURL).

## Dataset(s)
GramBeddings (800k balanced, 2019-2021), Mendeley/MalCrawler (1,561,934; 35,315 malicious), Kaggle-1 (632,503 balanced), Kaggle-2 (4-class, about 651k) (Table 2)

## Features
Learned sub-word + character representations.

## Evaluation protocol
Random splits; class-imbalance subsampling; multi-class; cross-dataset (Table 6); adversarial evasion-character attacks; 30 live-URL case study

## Metrics reported
Peak F1 improvement 40% in class-imbalanced setting and +14.13% accuracy under adversarial attack vs best baseline (abstract); cross-dataset example: TransURL Acc 0.9023 / F1 0.8846 / AUC 0.9839 vs GramBeddings Acc 0.7018 (Table 6); all 30 live malicious pages detected.
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Cross-dataset performance drops sharply for all models (GramBeddings to about 70% accuracy), TransURL degrades least; adversarial character insertion hurts baselines.

## Limitations
- Stated by authors: Compute cost; evasion types limited.
- Our own caveats: Cross-dataset results still far from in-distribution, confirming our generalisation concern; Table 2 shows TLD/length distribution differences across datasets - artifact candidates.

## Research gap
Artifact-aware evaluation; explainability.

## Relevance to our project
Best recent cross-dataset + adversarial evaluation of URL models; dataset statistics (TLD, length) directly inform our shortcut analysis.

Relevance score: 5/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
