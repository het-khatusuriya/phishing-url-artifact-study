# oest2020phishtime

## Citation
Adam Oest, Yeganeh Safaei, Penghui Zhang, Brad Wardman, Kevin Tyers, Yan Shoshitaishvili, Adam Doupé, Gail-Joon Ahn (2020). PhishTime: Continuous Longitudinal Measurement of the Effectiveness of Anti-phishing Blacklists. *29th USENIX Security Symposium (USENIX Security 20)*, pp. 379-396. 

- URL: https://www.usenix.org/conference/usenixsecurity20/presentation/oest-phishtime
- Access status: full_text (research/papers/oest2020phishtime.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 3

## Verification
USENIX presentation page (title, authors, pages 379-396, PDF) checked 2026-10-11.

## Problem
How fast, complete and consistent are anti-phishing blacklists, and how easily are they evaded?

## Method
Controlled, longitudinal experiments measuring blacklist speed, coverage and consistency; reproduces evasion techniques seen in the wild

## Dataset(s)
2,862 researcher-deployed, innocuous PayPal-branded phishing sites across six deployments over nine months

## Features
Not an ML detector paper

## Evaluation protocol
Time-to-blacklist measurement per browser/platform; evasion vs. non-evasion arms

## Metrics reported
2,862 sites launched; identifies a JavaScript/behaviour-based evasion that blacklists failed to detect; mobile protections lag desktop (abstract; Sec. 6-7).

## Main findings
Ground-truth sources such as blacklists are slow, inconsistent, and evasion-sensitive; the labels researchers harvest from them are therefore delayed and biased toward unevasive phish.

## Limitations
**Authors' stated:** Artificial sites; single brand; nine-month window.

**Our caveats:** Implication for us: PhishTank-style labels over-represent the easy-to-detect phish, so our test set is easier than deployment traffic.

## Research gap
Label-source bias in phishing URL datasets is rarely quantified.

## Relevance to our project
Supports the limitation that our positive class (blacklist-derived) is a biased sample of phishing, and that time-to-detection matters more than offline accuracy.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
