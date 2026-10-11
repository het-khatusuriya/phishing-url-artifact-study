# chen2026memophishagent

## Citation
Chen, Xuan; Liu, Hao; Yuan, Tao; Kafai, Mehran; Habas, Piotr; Zhang, Xiangyu (2026). *MemoPhishAgent: Memory-Augmented Multi-Modal LLM Agent for Phishing URL Detection*. arXiv preprint arXiv:2602.21394 (v3; arXiv comment states ACL 2026 Industry Track camera-ready - venue not independently verified). URL: https://arxiv.org/abs/2602.21394

- Type: preprint | Theme (L1): d-transformer-llm | Access: full_text | Verified: full
- Local PDF: research/papers/chen2026memophishagent.pdf

## Verification
Checked 2026-10-11: arXiv API record 2602.21394 (v3 2026-04-21) and arXiv PDF read. No DOI; ACL venue claim from arXiv comment only.

## Problem
Adaptive, multimodal phishing detection beyond static URL heuristics.

## Method
Tool-using agent (page crawl, screenshot, memory retrieval) with episodic memory; ablations of tools/memory.

## Dataset(s)
TR-OP (5,000 phishing + 5,000 benign, Jul-Dec 2023), DynaPD, and new SocPhish (2,765 URLs: 516 phishing, 2,249 benign from five social platforms) (Sec. 4, Table 6)

## Features
URL + page content + screenshots (multimodal).

## Evaluation protocol
Held-out evaluation on public sets plus real-world SocPhish; production deployment (about 60k URLs/week); prompt-injection robustness test

## Metrics reported
Recall +13.6% over SOTA on public sets, +20% on SocPhish; production 91.44% recall, 90.34% F1 (abstract; Tables 1, 5); 1.07 s/URL latency.
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Agentic multimodal reasoning improves recall on novel threats; URL-only URLTran degrades on real-world social-media URLs.

## Limitations
- Stated by authors: Latency/cost; prompt-injection sensitivity (Appendix A.3).
- Our own caveats: Not URL-only; heavy; included to bound the design space.

## Research gap
n/a

## Relevance to our project
Low direct relevance (multimodal agent), but its URLTran-on-real-world results illustrate URL-only generalisation limits.

Relevance score: 2/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
