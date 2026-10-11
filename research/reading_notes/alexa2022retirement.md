# alexa2022retirement

## Citation
Amazon (Alexa Internet) (2022). *Alexa.com Top Sites retirement (1 May 2022)*. Alexa.com end-of-service notice; press coverage. URL: https://www.alexa.com/minisiteinfo/

## Verification
- Verified on 2026-10-11. Status: **partial**. Access: **abstract_only**.
- Evidence: PARTIAL: official notice page could not be rendered (redirects to Amazon-hosted JS page; archive.org not reachable from this tool). Date 1 May 2022 and December 2022 API/extension sunset reported consistently by Semrush, Search Engine Journal and Gigazine (search results); Tranco page states Alexa has been removed from its sources.

## Problem
n/a

## Method
n/a

## Dataset(s)
n/a

## Features
n/a

## Evaluation protocol
n/a

## Metrics reported (only numbers present in the source)
n/a

## Main findings
Alexa top-1M, the benign source of ISCX-URL-2016 and many phishing datasets, is no longer maintained; snapshots are frozen as of 2022.

## Limitations
- Authors' stated limitations: n/a
- My assessment: n/a

## Research gap
n/a

## Relevance to our project (score 3/5)
Needed when discussing staleness of Alexa-derived benign URLs and 'in Alexa top-1M' features; recommend Tranco.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
