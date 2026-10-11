# commoncrawl

## Citation
Common Crawl Foundation (2026). *Common Crawl web corpus and URL index (benign URL source)*. https://commoncrawl.org/overview. URL: https://commoncrawl.org/overview

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text**.
- Evidence: commoncrawl.org/overview fetched 2026-10-11 (scope, access, index); Terms of Use linked but not summarised there.

## Problem
n/a

## Method
n/a

## Dataset(s)
Download: s3://commoncrawl/ (free), URL index https://index.commoncrawl.org/ . License: Common Crawl Terms of Use (crawl data free for use; respect source copyrights). Timestamps: YES (crawl ID and fetch time per record). Labels: none - 'benign' is an assumption; crawls contain malicious pages. Known problems: used as benign in Bahnsen 2017, GramBeddings-style corpora, Mendeley/IEEE DataPort sets; benign label unverified; URL length/format distribution differs from phishing feeds (shortcut risk).

## Features
n/a

## Evaluation protocol
n/a

## Metrics reported (only numbers present in the source)
n/a

## Main findings
n/a

## Limitations
- Authors' stated limitations: n/a
- My assessment: Benign-by-assumption; needs screening (e.g. Google Safe Browsing/VirusTotal) as PhiShark-style papers do.

## Research gap
n/a

## Relevance to our project (score 4/5)
Candidate benign source for a fresh external test set, paired with Tranco ranking.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
