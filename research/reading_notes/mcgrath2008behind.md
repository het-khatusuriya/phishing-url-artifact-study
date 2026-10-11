# mcgrath2008behind

## Citation
McGrath, D. Kevin; Gupta, Minaxi (2008). *Behind Phishing: An Examination of Phisher Modi Operandi*. USENIX Workshop on Large-Scale Exploits and Emergent Threats (LEET '08). URL: https://www.usenix.org/legacy/event/leet08/tech/full_papers/mcgrath/mcgrath.pdf

- Type: conference | Theme (L1): a-foundational-lexical | Access: full_text | Verified: partial
- Local PDF: research/papers/mcgrath2008behind.pdf

## Verification
Checked 2026-10-11: USENIX LEET'08 official HTML page (usenix.org/legacy/event/leet08/...) and downloaded USENIX PDF; no DOI issued for this workshop, hence verified=partial.

## Problem
Characterise how phishers construct URLs/domains and host sites.

## Method
Compares phishing URL feeds against DMOZ: URL/domain length distributions, character/vowel distributions, brand-name inclusion, subdomain use, IP hosts, shorteners; domain registration-to-activation delays; lifetime.

## Dataset(s)
PhishTank and MarkMonitor real-time phishing feeds (>2 months, 2007-08), MarkMonitor-2006 archive; DMOZ URLs as benign comparison; whois/zone files

## Features
URL length, domain length, vowel ratio, unique-character count, brand presence, subdomain count, IP-as-host, shortener use.

## Evaluation protocol
Descriptive statistics; no classification

## Metrics reported
URL length modes: 22 chars (DMOZ) vs 67 (PhishTank) vs 107 (MarkMonitor) (Sec. 3, Fig. 1); domain length mode 7 vs 10 chars (Fig. 2); 50-75% of phishing URLs contain target brand (Table 3); >3/4 contain subdomains; mean domain lifetime about 3 days (Sec. 5).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Length, vowel ratio, character-diversity and brand-in-URL are strongly discriminative; phishing domains are short-lived.

## Limitations
- Stated by authors: Preliminary work; feeds biased toward reported phishing.
- Our own caveats: 2007-era statistics; DMOZ as 'benign' is homepage-heavy (same shortcut risk as later datasets).

## Research gap
No learning or temporal-drift evaluation.

## Relevance to our project
Empirical justification for several of our lexical features (length, vowel ratio, entropy, brand tokens) and a reminder that benign-homepage baselines inflate length separability.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
