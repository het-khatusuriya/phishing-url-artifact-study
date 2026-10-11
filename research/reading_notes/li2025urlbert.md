# li2025urlbert

## Citation
Li, Yujie; Liu, Yiwei; Li, Peiyue; Jia, Yifan; Wang, Yanbin (2025). *Continuous Multi-Task Pre-training for Malicious URL Detection and Webpage Classification (URLBERT)*. Computer Networks, 270, 111513 (arXiv:2402.11495, first titled 'URLBERT: A Contrastive and Adversarial Pre-trained Model for URL Classification', 2024). DOI: 10.1016/j.comnet.2025.111513 URL: https://arxiv.org/abs/2402.11495

- Type: journal | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/li2025urlbert.pdf

## Verification
Checked 2026-10-11: arXiv API record 2402.11495 (v2 2025-05-24) and arXiv PDF read; Crossref record for journal DOI 10.1016/j.comnet.2025.111513 (Comput. Netw. 270:111513, 2025); Semantic Scholar links the arXiv id to this DOI.

## Problem
URL-specific pre-trained encoder usable across URL tasks.

## Method
Custom URL tokenizer; multi-task pre-training with contrastive and adversarial objectives; evaluation on phishing detection, ad-URL detection, webpage topic classification; code github.com/Davidup1/URLBERT.

## Dataset(s)
Pre-training: 3.28B unique URLs (Common Crawl 2.85B, Open PageRank 338.71M, expired domains 538.2M, malicious sources 8.26M, ODP 3.86M); phishing task: GramBeddings + Mendeley merged, 126,733 phishing / 237,889 benign (Table 1)

## Features
Learned URL sub-word representations.

## Evaluation protocol
60/40 train/test for phishing and ad tasks; 80/20 for topic task; data-scale experiments; TPR at FPR 0.001

## Metrics reported
Phishing detection AUC > 0.99; with 60% of training data accuracy 0.9720 and TPR about 0.8 at FPR 0.001; outperforms BERT (0.9156) and RoBERTa (0.9206) in a low-data setting at 0.9506 (Sec. 5); traditional KNN/RF/NB still > 96% accuracy on this benchmark.
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
URL-domain pre-training helps most in low-data regimes; classical lexical models remain strong on in-distribution benchmarks.

## Limitations
- Stated by authors: Compute; multi-task interference partially addressed.
- Our own caveats: Removed URLs longer than 150 chars from the phishing benchmark (Table 1) - a preprocessing choice that interacts with length artifacts.

## Research gap
Cross-dataset and temporal evaluation of pre-trained URL encoders.

## Relevance to our project
Open-weights URL encoder we could use as a strong baseline or feature extractor; also shows classical models' competitiveness.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
