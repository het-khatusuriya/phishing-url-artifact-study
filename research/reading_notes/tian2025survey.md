# tian2025survey

## Citation
Tian, Ye; Yu, Yanqiu; Sun, Jianguo; Wang, Yanbin (2025). *From Past to Present: A Survey of Malicious URL Detection Techniques, Datasets and Code Repositories*. arXiv preprint arXiv:2504.16449 (v2, under review at Computer Science Review). URL: https://arxiv.org/abs/2504.16449

- Type: preprint | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/tian2025survey.pdf

## Verification
Checked 2026-10-11: arXiv API record 2504.16449 (v2 2025-06-01) and arXiv PDF read. No DOI.

## Problem
Update the survey literature with LLM/transformer defenses, datasets and code.

## Method
Reviews blacklists -> classical ML -> deep learning -> LLM prompting/agents; tabulates datasets and reported accuracies.

## Dataset(s)
Survey: catalogues public datasets 2016-2024 and open-source implementations 2013-2025 (GitHub list)

## Features
Catalogue of lexical, host, content, visual features.

## Evaluation protocol
n/a (survey)

## Metrics reported
n/a
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Notes lack of proper baselines and standardised benchmarks; many works report >99% on small sets.

## Limitations
- Stated by authors: Preprint under review.
- Our own caveats: Accuracy tables are copied from papers without protocol normalisation.

## Research gap
Standard benchmarks and protocol reporting.

## Relevance to our project
Up-to-date map of datasets/code for choosing external test sets and baselines.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
