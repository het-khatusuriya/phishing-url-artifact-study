# dalton2025phreshphish

## Citation
Thomas Dalton, Hemanth Gowda, Girish Rao, Sachin Pargi, Alireza Hadj Khodabakhshi, Joseph Rombs, Stephan Jou, Manish Marwah (2025). PhreshPhish: A Real-World, High-Quality, Large-Scale Phishing Website Dataset and Benchmark. *arXiv preprint*. arXiv: 2507.10854

- URL: https://arxiv.org/abs/2507.10854
- Access status: full_text (research/papers/dalton2025phreshphish.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 4

## Verification
arXiv abstract page and arXiv API record 2507.10854 (v1 14 Jul 2025, v2 11 Feb 2026; OpenText authors) checked 2026-10-11.

## Problem
Public phishing datasets are small, noisy, leak between train and test, and use unrealistic base rates, inflating reported performance.

## Method
Dataset construction pipeline: temporal train/test split, pruning of near-duplicate test points via locality-sensitive hashing, diversity/difficulty filters, base-rate adjustment; baseline models

## Dataset(s)
New large phishing-website dataset (HTML+URL) crawled with a real browser, quality-checked by heuristics and human annotation; hosted on Hugging Face; benchmark subsets at base rates from 0.05% to 5%

## Features
URL and HTML; baselines include URL-only models

## Evaluation protocol
Temporal split + leakage pruning + five base rates; precision reported as a function of recall, FPR and base rate

## Metrics reported
Benchmarks span base rates 0.05%-5%; states existing public datasets 'suffer from leakage and unrealistic base rates, leading to overly optimistic performance results' (Sec. 1); baseline tables in Sec. 6.

## Main findings
Train/test leakage (same kit/template, near-duplicate pages) and balanced base rates inflate published results; realistic benchmarks need temporal splits, near-duplicate pruning and low prevalence.

## Limitations
**Authors' stated:** Preprint; industrial collection pipeline not fully reproducible; HTML-centric.

**Our caveats:** URL-only baselines are secondary; still the most explicit public treatment of leakage + base rate for phishing benchmarks.

## Research gap
A URL-only benchmark with the same leakage/base-rate discipline.

## Relevance to our project
Direct support for near-duplicate/domain-grouped splitting and for reporting precision at realistic prevalence in our paper.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
