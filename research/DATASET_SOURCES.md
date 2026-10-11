# Dataset sources and provenance

Compiled 2026-10-11. All external files live under `data/external/<name>/` (gitignored via `data/`), each with a `SOURCE.md` (URL, access date, license, size, sha256, columns, label semantics, timestamps, citation) and a `profile.txt` produced by `python -I scripts/data/profile_dataset.py`. Downloaded files were only read, never executed.

## 1. Origin of the project dataset (`data/raw/raw_data.csv`)

Known facts (from notebook outputs): 253,098 rows; columns `url,label`; `legitimate` 129,420 / `phishing` 123,678; 0 duplicates; https 182,717 / http 70,373 / ftp 8; first rows `https://www.visitcanada.com` (legit), `http://218.228.19.9/~yossi/9ssfpkz` (phish), `https://www.msupress.msu.edu/series.php?seriesID=17` (legit), `https://docs.google.com/presentation/d/e/2PACX-1vRBjV4Bm4UxL3gJ8sCyQx...` (phish), `https://www.c250.columbia.edu/c250_celebrates/athletics/athletics_timeline...` (legit).

### Result: no published dataset with these exact counts was found

Searches run (web search + direct API queries, 2026-10-11): "253098", "253,098", "129420", "123678 phishing", "visitcanada.com phishing dataset", "218.228.19.9", "raw_data.csv phishing", Kaggle/HuggingFace/Mendeley/Zenodo/UCI/IEEE-DataPort listings. No hit on the row counts, on the file name, or on the first URLs as a dataset identifier. Kaggle dataset pages cannot be inspected anonymously (reCAPTCHA on both the HTML and the Croissant metadata endpoints), so Kaggle candidates could not be verified row-by-row.

### Evidence found (verified locally by grepping the downloaded files)

| Known first-row URL | Found in | Form found | Label there |
|---|---|---|---|
| https://www.visitcanada.com | HF `Mitake/PhishingURLsANDBenignURLs`, HF `alexkstern/phishing_urls`, HF `kmack/Phishing_urls` | `visitcanada.com/` | 0 = benign |
| http://218.228.19.9/~yossi/9ssfpkz | Mitake, alexkstern | `218.228.19.9/~yossi/9ssfpkz` | 1 = phishing |
| https://www.msupress.msu.edu/series.php?seriesID=17 | Mitake (with and without `www.`), alexkstern, Kaggle sid321axn mirror | `msupress.msu.edu/series.php?seriesID=17` | benign |
| https://www.c250.columbia.edu/c250_celebrates/athletics/athletics_timeline.html | Mitake, Kaggle sid321axn mirror | without scheme | benign |
| https://docs.google.com/presentation/d/e/2PACX-1vRBjV4Bm4UxL3gJ8sCyQx... | not found in any downloaded set (Mitake, alexkstern, sid321axn, PhiUSIIL, ISCX, PhishStorm, Ebbu2017, Hannousse, PhishTank-current) | – | – |

Not found in: PhiUSIIL (UCI 967), ISCX-URL-2016 lists, PhishStorm, Ebbu2017, Hannousse 2021, current PhishTank dump.

### Interpretation (confidence stated per claim)

1. **High confidence:** the legitimate half and the older phishing samples come from the "classic Kaggle URL lineage" — Kaggle `sid321axn/malicious-urls-dataset` (651,191 rows, benign/defacement/phishing/malware; itself built from ISCX-URL-2016 + PhishTank + PhishStorm) and/or Kaggle `taruntiwarihp/phishing-site-urls` (549,346 rows, good/bad), which several HuggingFace re-uploads merge (Mitake 886,181 rows, alexkstern 507,195, kmack 708,820). Four of five first rows are present there with matching labels, and those sources store URLs **without scheme** (`visitcanada.com/`), whereas the project file has `https://www.visitcanada.com`. So the project file is a **derived/normalised** version: someone prefixed a scheme (and apparently `www.`) and stripped trailing slashes.
2. **Medium confidence:** the file is a merge of that lineage with a **newer phishing source** (PhishTank/OpenPhish 2020+): the Google-Docs `2PACX` presentation URL is a 2020s phishing pattern absent from all 2014-2019 sets, and 72% https is far above the classic sets (sid321axn: 8.3% https among scheme-bearing URLs; Ebbu2017 phishing: 1.8%; PhishStorm phishing: 1.5%).
3. **Unverified Kaggle candidates** whose titles/labels match the `legitimate`/`phishing` string scheme but whose row counts could not be read: `harisudhan411/phishing-and-legitimate-urls` (a Gigasheet mirror lists 822,010 rows, columns url/status — too large), `kunal4892/phishingandlegitimateurls` (0/1 labels), `hassaanmustafavi/phishing-urls-dataset` (450K+), `prakashpugazhandhi/phishing-url-detection-dataset` (242,056 rows, 0/1 labels — closest count but not equal). None matches 253,098 / 129,420 / 123,678.
4. Near-miss sizes that are **not** the source: PhiUSIIL 235,795 (134,850/100,945; first rows do not appear), Tamal 2023 Mendeley 10.17632/6tm2d6sz7p 247,950 (128,541 phishing / 119,409 legitimate; 41 feature columns).

**Conclusion:** the project dataset cannot be attributed to a single published artefact. It should be described in the paper as "a 253,098-URL compilation of publicly available phishing/legitimate URL lists (PhishTank/OpenPhish-derived phishing URLs and Alexa/ISCX-derived legitimate URLs, as redistributed on Kaggle/HuggingFace), scheme-normalised and de-duplicated", with the limitation that its exact composition and collection dates are unknown. The team member who assembled `raw_data.csv` should be asked for the originating link(s); the strings above (visitcanada / yossi) can be used to confirm.

Caveat for modelling: because legitimate URLs in that lineage are overwhelmingly `https://www.<domain>` homepages and phishing URLs carry long paths, scheme/`www.`/length features will look highly predictive but are dataset artefacts; the external sets below exist to measure that.

## 2. Datasets obtained

| name (dir) | rows | classes / label | timestamps | license / terms | ext. test | temporal test | benign source | malicious source |
|---|---|---|---|---|---|---|---|---|
| phiusiil | 235,795 | 1=legit 134,850 / 0=phish 100,945 | no (2023-24) | CC BY 4.0 | yes (strong www/https bias) | no | yes (homepages) | yes |
| urlhaus | 72,849 | malware_download only | **yes** (dateadded 2018-2026) | abuse.ch fair use | malware only (not phishing) | yes (malicious class) | no | yes (malware, 59% IP hosts) |
| openphish | 300 | phishing only | feed date only | non-commercial | sanity check only | no | no | yes (tiny, fresh) |
| tranco | 1,000,000 domains | none (ranking) | list date 2026-10-10 (ID 8PXYV) | research use, cite | no (domains, not URLs) | no | yes (domains only) | no |
| hannousse2021 | 11,430 | legitimate 5,715 / phishing 5,715 | no (May 2020) | CC BY 4.0 | **yes** (balanced, independent) | no | yes | yes |
| ebbu2017 | 73,575 (36,400 / 37,175; many dups) | by file | no (2017) | none stated | yes (http/https shortcut) | no | yes | yes |
| kaggle_malicious_urls (HF mirror of sid321axn) | 651,191 | benign 428,103 / defacement 96,457 / phishing 94,111 / malware 32,520 | no | MIT on mirror; Kaggle license unverified | partly — likely overlaps the project data (shared lineage), so NOT independent | no | overlap risk | multi-class malicious |
| phishtank | 67,621 | verified phishing only | **yes** (submission_time 2011-2026, mostly recent) | PhishTank ToU, non-commercial | yes (positive class) | **yes** | no | yes |
| iscx_url_2016_mirror | 35,378 benign + 9,965 phishing | by file | no (2016) | UNB, cite; partial mirror | yes (old) | no | yes | yes |
| phishstorm_mirror | 48,009 legit + 43,378 phishing | by file | no (2014) | unspecified; partial mirror | yes (old) | no | yes | yes |
| hf_mitake | 886,181 | 0 benign 610,832 / 1 phishing 275,349 | no | CC BY-SA 4.0 | no (same lineage as project data) | no | overlap | overlap |

Recommended protocol: external test on **hannousse2021** (independent, balanced, 2020) and **phiusiil** (recent, with the inverse label convention handled); temporal test by training on the project data and scoring **phishtank** (positive) by `submission_time` month plus a benign stream sampled from **tranco** domains or **iscx** benign URLs; keep **urlhaus** as a separate malware-URL robustness check; do not use **kaggle_malicious_urls** / **hf_mitake** as "external" tests because they share the project's lineage.

## 3. Not obtained / blocked

| dataset | reason | manual steps |
|---|---|---|
| GramBeddings (800k) | distributed only after a Google Form request; no direct URL or GitHub release | Fill https://docs.google.com/forms/d/e/1FAIpQLScuwosnH9JIJYKUeTeR26xxiG6bWXhxYoHjoNSketW5MrCUxQ/viewform; link arrives by e-mail; place files in data/external/grambeddings/ |
| ISCX-URL-2016 (official, full) | UNB requires a web form (name, e-mail, organisation, job title, country); only benign+phishing lists obtained via a third-party mirror | Submit the form at https://cicresearch.ca/CICDataset/ISCX-URL-2016/ and download the full archive (spam, malware, defacement lists + feature CSVs) |
| Kaggle originals (sid321axn, taruntiwarihp, harisudhan411, ...) | no Kaggle credentials; Kaggle pages/metadata blocked by reCAPTCHA for anonymous HTTP | `kaggle datasets download -d sid321axn/malicious-urls-dataset` with an API token; verify sha256 against the mirror (d83ce942...) |
| PhishTank (registered access) | downloaded anonymously once (allowed, rate-limited); no key requested | Register at https://www.phishtank.com/register.php for an application key if repeated/automated pulls are needed |
| Hannousse dataset_A (DOM trees) | not exposed through the Mendeley public-files API for v3 | Use the "Download all" button on https://data.mendeley.com/datasets/c2gw7fy2j4/3 in a browser |
| PhishStorm official (Aalto) | portal page lists license "Unspecified"; file download link not resolved; partial mirror used | Download from the Aalto research portal (doi 10.24342/f49465b2-c68a-4182-9171-075f0ed797d5) if the full feature file is needed |
| HuggingFace phishing URL sets with timestamps | none found with per-URL dates: all URL-only sets (Mitake, alexkstern, kmack, flwrlabs, Razvan27 1.9M, imanoop7/darshan8950 synthetic 100k, TFIRE24138 475k) lack dates; `nyuuzyou/phishing-snapshots` (136k, CC0) has `scan_timestamp` but is a page-snapshot set with many null `url` values, >1 GB of HTML | If needed, pull only the `domain, url, scan_timestamp` columns of nyuuzyou/phishing-snapshots with the datasets-server /rows API |

## 4. Scripts

- `scripts/data/profile_dataset.py` — CSV/TXT/JSON profiler (row count, columns, label distribution, scheme distribution, www share, IP-host share, duplicate URLs, min/max of date columns, sha256). Run with `python -I`.
