# ma2009beyond

## Citation
Ma, Justin; Saul, Lawrence K.; Savage, Stefan; Voelker, Geoffrey M. (2009). *Beyond blacklists: learning to detect malicious web sites from suspicious URLs*. Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '09), pp. 1245-1254. DOI: 10.1145/1557019.1557153 URL: https://doi.org/10.1145/1557019.1557153

- Type: conference | Theme (L1): a-foundational-lexical | Access: full_text | Verified: full
- Local PDF: research/papers/ma2009beyond.pdf

## Verification
Checked 2026-10-11: Author-hosted PDF (cseweb.ucsd.edu/~voelker/pubs/mal-url-kdd09.pdf) read in full; Crossref record for DOI 10.1145/1557019.1557153 (KDD '09, pp. 1245-1254).

## Problem
Classify URLs as malicious (phishing/spam) vs benign from URL-derived features without visiting the page.

## Method
Automatically extracts tens of thousands of binary lexical tokens (hostname and path tokens, delimiters) plus host-based properties; compares feature groups; L1-LR for sparse interpretable models.

## Dataset(s)
Benign: 15,000 URLs each from Yahoo random-URL feed and DMOZ; malicious: 5,500 PhishTank + Spamscatter URLs; 4 benign/malicious pairings, 20k-30k URLs each (Sec. 4.1)

## Features
Lexical: URL length, hostname length, dot count, bag-of-words tokens for host and path. Host-based: WHOIS registration/age, IP prefix/AS, geolocation, DNS TTL, connection speed, blacklist membership.

## Evaluation protocol
10 random 50/50 splits per dataset; also cross-source training/testing (Table 4)

## Metrics reported
Overall accuracy 95-99% (abstract); error rates 1.2-6% for full feature set and 1.1-3.4% without WHOIS/blacklist features (Sec. 4.2, Fig. 2); lexical-only about 15% error at best vs 10% for host-only on the hardest set (Sec. 4.2); cross-source training degrades strongly (Table 4: e.g. 14-21% error when trained on one source and tested on another).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Lexical and host features are complementary; automatically generated token features beat hand-chosen ones; models trained on one data source generalise poorly to another.

## Limitations
- Stated by authors: Features assume infrastructure lookups (WHOIS/DNS) are available; redirection and short URLs not handled; distribution shift between sources acknowledged (Sec. 4.4).
- Our own caveats: Benign sources (Yahoo/DMOZ) are directory homepages, so length/token artifacts favour the classifier; blacklist features leak labels.

## Research gap
Cross-source generalisation and temporal robustness left largely open.

## Relevance to our project
Canonical baseline for our lexical + classical ML arm; Table 4 is an early cross-dataset result we can cite for the generalisation gap.

Relevance score: 5/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
