# When the Scheme Is the Signal: Collection Artifacts and Cross-Corpus Failure in Lexical Phishing-URL Detection

## Abstract

Lexical URL classifiers are routinely reported with 95–99 % accuracy on public phishing benchmarks, yet they fail when applied to differently collected data. Starting from a typical detector — 28 lexical features and a weighted soft-voting ensemble of logistic regression, random forest and XGBoost — we audit its implementation and evaluate it on six public corpora with raw URLs and three live feeds, under random, domain-grouped, external-corpus and leave-one-corpus-out protocols. In the widely used PhiUSIIL corpus every benign URL is an `https://www.` homepage, and across corpora the scheme, the `www.` prefix and URL length change in strength and even in direction of association with phishing; a linear probe identifies the source corpus of a benign URL with 83 % accuracy (chance 17 %). Models trained on PhiUSIIL reach ROC-AUC 0.999 with or without domain-grouped splitting, yet at a threshold set for a 1 % false-positive budget they flag 99–100 % of the benign URLs of four other corpora, their ROC-AUC falls to 0.34–0.78, and adding a slash to an empty URL path flips 100 % of their benign decisions. Removing artifact features and post-hoc calibration do not repair this, and the ensemble is statistically indistinguishable from XGBoost alone. Training on five pooled corpora restores the held-out ROC-AUC of XGBoost to 0.87–0.98 and limits decision flips to at most 15 %, but validation-chosen thresholds still over-flag one unseen corpus and under-flag another. We argue that URL detectors must be trained and evaluated across corpora, on canonicalised URLs and at fixed false-positive budgets, and we release a tested, reproducible pipeline.

**Index Terms** — phishing detection, malicious URL detection, lexical features, ensemble learning, dataset bias, shortcut learning, cross-dataset generalisation, calibration, explainable AI

## I. Introduction

Phishing remains one of the highest-volume and most damaging attack vectors on the web. Most phishing campaigns live for hours rather than days, and the majority of victims are reached before blacklists react [oest2020sunrise, oest2020phishtime]. This has motivated *proactive* detectors that judge a URL from its string alone, before the page is fetched. Lexical URL classifiers suit this role well: they need no network access, add negligible latency, and are routinely reported with accuracies between 95 % and 99 % [ma2009beyond, le2011phishdef, mamun2016iscxurl, sahingoz2019machine, sankaranarayanan2024ensemble, khan2026stacking].

These figures are difficult to reconcile with what happens when such models leave the dataset they were trained on. Cross-dataset accuracy of URL classifiers has been reported at 51–59 % [mia2024featurestrust]; detectors "work effectively only when the test sets are split from the same training dataset" [rashid2024domainadapt]; and models trained against homepage-only benign URLs lose 27–39 accuracy points on legitimate login pages [sanchezpaniagua2022phishing]. The security machine-learning community has a name for the likely cause — spurious correlations created by sampling bias [arp2022dosdonts] — and phishing researchers have long warned that benign URLs drawn from popularity lists look structurally different from phishing URLs [marchal2018designing, elaassal2020benchmarking, hannousse2021benchmark, sabir2022reliability]. What has been missing is a measurement: *which* properties of public URL corpora carry the reported performance, whether they point the same way in every corpus, and whether removing them helps.

This study started from a concrete system. A course-project detector — 28 handcrafted lexical features feeding a weighted soft-voting ensemble of logistic regression, random forest and XGBoost — reported a test accuracy of 96.8 % on a 253,098-URL dataset. When we audited it, its two most influential features (by SHAP) were the URL scheme (`https`) and a subdomain count driven by the `www.` prefix, and it classified `https://google.com/` as malicious with 88 % probability. The rest of this paper shows that this is not an implementation accident but a property of the data the field evaluates on, and quantifies what it does to detection in practice.

We ask three research questions:

- **RQ1.** How much of the in-distribution performance of lexical URL classifiers on public phishing corpora is carried by nameable *collection artifacts* — the scheme, the `www.` prefix, homepage-only benign URLs — and by memorisation of registered domains?
- **RQ2.** Do these artifacts point in the same direction across corpora, and does that explain cross-corpus failure?
- **RQ3.** Does an artifact-aware recipe — URL canonicalisation, domain-grouped model selection and validation-chosen operating thresholds — restore performance on unseen corpora, and do probabilities and thresholds stay reliable under shift?

Our contributions are:

1. An audit and faithful re-execution of a representative lexical detector, exposing an evaluation shortcut and a parsing defect that silently disables all host features for URLs without a scheme.
2. A per-class artifact audit of six public phishing-URL corpora and three live feeds, showing that the dominant artifacts change strength and even direction between corpora.
3. A dataset-identification probe showing that the source corpus of a URL is predictable from lexical features far above chance, that dropping artifact columns hardly changes this, and that canonicalising the URL string does.
4. A controlled evaluation of random versus registered-domain-grouped splits, external-corpus and leave-one-corpus-out transfer, calibration, threshold transfer, explanations and robustness to label-preserving URL variants.
5. A tested, reproducible implementation with documented provenance for every dataset and number.

Section II reviews the literature and derives the research gap. Section III states the problem and hypotheses. Section IV describes and audits the baseline system. Section V presents the data, Section VI the methodology and Section VII the experimental setup. Section VIII reports results, Section IX discusses them, Section X lists threats to validity and Section XI concludes.

## II. Literature Review

We reviewed 111 sources identified through searches of IEEE Xplore, the ACM Digital Library, SpringerLink, ScienceDirect, USENIX and NDSS proceedings, arXiv and Google Scholar, with every bibliographic record verified against an authoritative page. This section organises the most relevant work by theme; Table I compares representative studies.

### A. Lexical features and classical learners

Early measurement work established that the URL string alone separates phishing from benign pages. McGrath and Gupta found phishing URLs far longer than benign directory URLs (modal lengths of 67–107 versus 22 characters) and observed brand names in 50–75 % of them [mcgrath2008behind]; Garera et al. catalogued URL obfuscation strategies such as IP hosts, redirection and brand names in the host or path [garera2007framework]. Ma et al. turned these observations into large sparse bag-of-token models combined with host-based features and reported 95–99 % accuracy [ma2009beyond]. Their online variant, evaluated day by day over 100 days of web-mail traffic, showed that the feature distribution of malicious URLs drifts and that stale batch models degrade [ma2009identifying, ma2011learning]. Importantly for this study, Ma et al. also reported that training on one data source and testing on another raised error to roughly 14–21 % [ma2009beyond].

Later work refined the feature space: obfuscation-resistant lexical features with online AROW learning [le2011phishdef], confidence-weighted online learning [blum2010lexical], distributional character statistics [verma2015character], word-level natural-language features [sahingoz2019machine], search-engine word relatedness [marchal2014phishstorm] and fast linear-time extractors [verma2017whatsinaurl]. Benchmarks such as ISCX-URL-2016 [mamun2016iscxurl], the Hannousse–Yahiouche dataset [hannousse2021benchmark] and PhiUSIIL [prasad2024phiusiil] made lexical detection easy to evaluate, and tree ensembles consistently emerged as the strongest classical learners.

### B. Ensembles and hybrid detection systems

Ensembles combine heterogeneous learners or feature views. CatchPhish combined TF-IDF n-grams with handcrafted features in a random forest [rao2020catchphish]; Chiew et al. selected compact feature subsets with an ensemble procedure [chiew2019hybrid]; PhishHaven used unbiased voting over several lexical models [sameen2020phishhaven]; and Lee et al. trained noisy feature-subset ensembles to raise evasion cost [lee2020robustphishing]. The gains are consistently small: on the 651k-URL Kaggle corpus, stacking improved accuracy from 95.7 % (LightGBM) to 96.8 % [sankaranarayanan2024ensemble], and on a 248k-URL feature table a Bayesian-tuned stacking ensemble matched but did not exceed Extra Trees in ROC-AUC (0.9947 versus 0.9948) [khan2026stacking]. These comparisons were made on random splits of a single dataset.

### C. Character-level, sequence and transformer models

Learned representations avoid manual feature design. Character-level CNNs [saxe2017expose], character LSTMs [bahnsen2017rnnurl] and joint character–word CNNs [le2018urlnet] were followed by attention-based hybrids [huang2019phishingnet, wang2019pdrcnn], Inception-style character/word networks evaluated at a 0.01 % false-positive rate on production telemetry [tajaddodianfar2020texception], n-gram embeddings with attention [bozkir2023grambeddings] and multi-million-URL CNN studies [sahingoz2024dephides]. Transformers fine-tuned on browser telemetry raised the true-positive rate at 0.01 % FPR from 71.2 % (URLNet) to 86.8 % [maneriker2021urltran]; URL-specific pre-training at billion-URL scale followed [wang2023phishbert, li2025urlbert, liu2024transurl], as did lightweight on-device transformers [haynes2021lightweight, roy2024phishlang] and large-language-model prompting and fine-tuning [trad2024prompt, kibriya2025lightweight]. Two observations matter here. First, the studies that used temporal splits and low-FPR operating points on production data [le2018urlnet, tajaddodianfar2020texception, maneriker2021urltran] report far more modest true-positive rates than public-benchmark papers. Second, TransURL is the only representation paper we found with a substantial cross-dataset test, in which all models degraded sharply (GramBeddings fell to 70.2 % accuracy) [liu2024transurl]. Aljofey et al. stripped `http://`, `https://` and `www.` before training a character CNN [aljofey2020effective], implicitly treating these prefixes as recording artifacts, but did not measure the effect.

### D. Explainability, robustness and calibration

SHAP provides additive feature attributions with consistency guarantees [lundberg2017shap], and TreeExplainer computes them exactly for tree ensembles [lundberg2020treeexplainer]. In phishing work SHAP is used mainly to select features [alfayoumi2024xaiphd, kehkashan2025explainable, khan2026stacking]; Mia et al. are the exception, using it to show that the same features change sign across datasets [mia2024featurestrust]. Robustness studies show that 50 reproduced URL detectors fell from a median MCC of 0.92 to 0.02 on cheaply registrable adversarial URLs [sabir2022reliability], that realistic problem-space evasions cause statistically significant drops [apruzzese2022spacephish], and that generated URLs evade detectors [aleroud2020gan, bahnsen2018deepphish]; practitioners report that cheap manipulations, not gradient attacks, dominate in practice [apruzzese2023realattackers]. Homograph and squatting domains remain effective [hu2021idnhomograph, tian2018needle, kintis2017combosquatting]. On calibration, boosted trees are known to be mis-calibrated without post-hoc scaling [niculescumizil2005calibration], calibration assumes that deployment matches the calibration data [guo2017calibration], and in Android malware detection calibration degrades under dataset shift [li2021malwarecalibration]. We found no comparable study for phishing URLs.

### E. Evaluation realism: sampling bias, leakage, drift and base rates

Arp et al. showed that sampling bias, spurious correlations and the base-rate fallacy affect most top-venue security ML papers [arp2022dosdonts], echoing earlier warnings about closed-world evaluation [sommer2010closedworld] and base rates [axelsson2000baserate]. TESSERACT showed that temporally inconsistent splits inflate malware-detection F1 [pendlebury2019tesseract, kan2024tesseractext], and drift-aware rejection and continual learning only partly recover performance [jordaney2017transcend, barbero2022transcending, chen2023continuous]; phishing models trained on older data also degrade on newer data [ejaz2023lifelong, sanchezpaniagua2022phishing]. For phishing specifically, the benign class has repeatedly been identified as the weak point: Alexa index pages "create a bias in the data" [sabir2022reliability]; Alexa domain lists lack subdomains and paths [hannousse2021benchmark]; benign sets should contain unpopular sites and URLs with paths, at realistic prevalence [marchal2018designing]; balanced, popularity-derived benchmarks overstate performance [elaassal2020benchmarking, das2020sokphishing, alam2026philter]; popularity lists are unstable and manipulable [lepochat2019tranco, scheitle2018toplists]; and public datasets leak between train and test and use unrealistic base rates [dalton2025phreshphish]. Cross-dataset studies report near-chance transfer [mia2024featurestrust, henry2026ensembletransfer] and propose domain adaptation [rashid2024domainadapt]. Closest to our work, a single-author preprint names the `https://` and `www.` shortcut and tests URL canonicalisation against one external benign set [giri2026shieldphish], and a study of phishing *e-mail* uses a corpus-identification probe and artifact-removal ablations [bhuiyan2026fragility].

### F. Comparative survey

<<TABLE|SURVEY|Comparison of representative studies. Reported results are the authors' own and are not comparable across rows, because datasets, splits, class ratios and metrics differ.>>

### G. Research gap

The literature establishes that lexical detectors score highly in-distribution, that they transfer poorly between datasets, and that popularity-list benign data are biased. It does not establish *which* recording properties of public corpora carry the in-distribution scores, whether those properties point the same way across corpora, how much registered-domain memorisation adds, or whether removing the properties — by dropping features or by canonicalising the URL — restores transfer. Prior cross-dataset studies worked with pre-computed feature tables [mia2024featurestrust, henry2026ensembletransfer], which makes it impossible to ablate raw-string artifacts, or did not isolate the mechanism [rashid2024domainadapt]; the one direct treatment is an unreviewed single-model preprint [giri2026shieldphish]. Calibration and threshold transfer have not been studied for phishing URLs, and robustness work has focused on adversarial manipulation rather than on label-irrelevant recording variants such as a missing scheme or a `www.` prefix. These gaps define the study below.

## III. Research Problem and Hypotheses

A detector maps a URL string *u* to a score *p(u)* that estimates P(malicious | *u*) and flags *u* when *p(u)* ≥ τ. We call a property *a(u)* a **collection artifact** if it is determined by how a source recorded or sampled URLs rather than by the URL's intent, and if its distribution differs between the classes of a corpus. The scheme prefix (absent, `http` or `https`), a leading `www.` label, and the restriction of a benign source to bare homepages satisfy both conditions in the corpora studied (Section V).

We test three hypotheses:

- **H1** (*artifact reliance*). Removing artifact information changes in-distribution ROC-AUC only marginally but changes behaviour on external corpora substantially; the source corpus of a URL is identifiable from lexical features well above chance; and random splits over-estimate grouped-split performance when corpora contain many URLs per registered domain.
- **H2** (*operating points*). Thresholds selected for a 1 % false-positive budget on validation data do not hold on external corpora, and post-hoc calibration does not repair this.
- **H3** (*temporal recall*). Recall on timestamped phishing feeds changes with submission year as the share of https phishing rises.

## IV. The Baseline System and Its Audit

### A. System description

The baseline system extracts 28 lexical features from each URL: lengths and counts of dots, slashes, hyphens, underscores, digits and special characters; the digit-to-letter ratio; path, query and domain lengths; the number of query parameters, `@` symbols and `//` occurrences; Shannon entropy; a subdomain count; the last hostname label (`tld_type`); flags for suspicious TLDs, punycode, IP hosts, `https`, URL shorteners, suspicious keywords, brand names, excessive hyphens and "random-looking" domains. `tld_type` is one-hot encoded (521 columns on the original data). Three classifiers are trained — logistic regression (standardised inputs, balanced class weights), a random forest of 200 trees and XGBoost with 200 rounds of depth 6 — and combined by soft voting with weights 1:2:2. The data are split 60/20/20 at random with stratification and seed 42; predictions use a fixed threshold of 0.5. A Flask application serves single-URL predictions, and SHAP KernelExplainer explains the ensemble.

### B. Audit findings

We read every file of the repository and extracted the stored outputs of its nine notebooks. Four findings shape this study. (i) The dataset (`raw_data.csv`) is not part of the repository and its origin is undocumented; our provenance search traced four of its five visible rows to a Kaggle/HuggingFace URL lineage built from ISCX-URL-2016, PhishTank and PhishStorm, stored there *without* a scheme, whereas the project file prefixes `https://www.` — evidence of a normalisation step applied to the benign class. (ii) The stored SHAP importances are dominated by `https_usage` (0.156) and `num_subdomains` (0.091), and in the stored class means 93 % of legitimate but only 50 % of phishing URLs use https. (iii) The weighted ensemble does not outperform its own random forest (test F1 0.9665 versus 0.9668). (iv) The feature extractor parses no host when a URL has no scheme: `visitcanada.com/` receives a domain length of 0 and the TLD "ip", so all host features collapse to constants for such input. The deployed application also passed a 28-column frame to a model trained on 548 one-hot columns and could not run as committed.

### C. Faithful re-execution

Because the original data are unavailable, we re-executed the unmodified pipeline code on two substitute corpora (Section V). Table II compares the result with the stored numbers.

<<TABLE|T2|Re-execution of the original pipeline code (random 60/20/20 split, seed 42, threshold 0.5) on two substitute corpora, compared with the stored results on the unavailable original dataset.>>

On PhiUSIIL the code scores higher than the project reported on its own data (soft-vote accuracy 0.9970, ROC-AUC 0.9988), and the four models lie within 0.0018 accuracy of one another. On corpus B, 99.8 % of whose URLs lack a scheme, accuracy falls to 0.8484: the parsing defect, not the corpus, limits the baseline there.

## V. Data

### A. Corpora

We assembled six labelled corpora with raw URL strings and three timestamped or live feeds (Table III). Corpus A is PhiUSIIL [prasad2024phiusiil]. Corpus B is a 253,098-URL stratified sample of the Kaggle/HuggingFace lineage, sized and balanced exactly like the unavailable original dataset (129,420 benign, 123,678 phishing). The external labelled corpora are Hannousse and Yahiouche 2021 [hannousse2021benchmark], Ebbu2017 [sahingoz2019machine], PhishStorm [marchal2014phishstorm] and the benign and phishing lists of ISCX-URL-2016 [mamun2016iscxurl]; the 651k-URL Kaggle corpus [siddhartha2021maliciousurls] was scored in the first two runs only because it shares lineage with corpus B. The positive-only feeds are the PhishTank verified-online dump with submission times [phishtank], URLhaus malware URLs [urlhaus] and an OpenPhish snapshot [openphish].

Every source is mapped to a URL and a label with malicious = 1. Duplicates are detected on a normalised key (lower-case scheme and host, default port and fragment removed, empty path collapsed); URLs carrying both labels are removed; features are always computed on the original string. Each URL is assigned a group equal to its registered domain, computed with an offline Public Suffix List snapshot, or its IP address.

<<TABLE|T1|Corpora after cleaning (malicious = 1). Shares are over all URLs of a corpus; PhishTank, URLhaus and OpenPhish contain only malicious URLs.>>

### B. Collection artifacts

Fig. 1 reports, per corpus and class, the share of URLs with an https scheme, a leading `www.` label and an empty path. In PhiUSIIL every benign URL is an `https://www.` homepage with no path, whereas 48 % of phishing URLs use https, 42 % start with `www.` and 72 % are homepages. The same properties behave very differently elsewhere. Corpus B and the Kaggle corpus store no scheme at all; in ISCX-2016 and the Kaggle corpus `www.` is *more* common among phishing URLs than among benign ones; and ISCX-2016's 35,378 benign URLs are deep pages from only about 300 sites. The present-day phishing population differs again: 92 % of PhishTank URLs use https and only 4 % start with `www.`. Measured as single-feature ROC-AUC (values below 0.5 indicate association with the benign class), the `www.` prefix scores 0.21 in PhiUSIIL, 0.27–0.34 in Hannousse, Ebbu2017 and PhishStorm, but 0.71 in ISCX-2016 and 0.69 in the Kaggle corpus; URL length scores 0.72–0.73 in PhiUSIIL and PhishStorm and 0.24 in ISCX-2016.

<<FIG|dataset_artifacts.png|Share of URLs with an https scheme, a leading www. label and an empty path, by class and corpus. Corpus B and the Kaggle corpus store URLs without a scheme.>>

## VI. Methodology

Fig. 2 summarises the pipeline. All fitting uses training rows only; every model, threshold and calibration choice uses validation rows only; test partitions, external corpora and feeds are scored once.

<<FIG|architecture.png|Artifact-aware evaluation pipeline.>>

### A. URL parsing

URLs are untrusted input, so the parser accepts any string and never raises. When no scheme is present it parses the string as `http://` + URL and records that the scheme was absent; malformed authorities and invalid ports set a parse-error flag. It extracts the scheme, user information, host, port, path, query, fragment, subdomain, registered domain, public suffix, IP and IPv6 status and the IDNA-decoded host. Unit tests cover missing schemes, IPv4 and IPv6 literals, ports, user information, punycode, Unicode hosts, single and double percent-encoding, very long strings and non-URL input.

### B. Representations

We compare four handcrafted representations:

- **baseline28** — the original 28 features computed by the original, unmodified code; `tld_type` is one-hot encoded with the encoder fitted on training rows only and TLDs with fewer than 20 occurrences pooled.
- **lexical_v2** — 91 offline features computed from the parsed components: whole-URL shape (length, entropy, character-class counts and ratios, longest digit run, token statistics, hexadecimal tokens, double encoding); scheme and authority (https, explicit scheme, `www.` prefix, user information, ports); host structure (lengths and entropy, label counts with and without the public suffix, registered-domain length, digits and hyphens, consonant runs, IP, punycode and non-ASCII flags, abused suffixes, free-hosting suffixes, shorteners); brand tokens *placed* in subdomain, registered domain or path rather than matched as raw substrings; and path, query and fragment structure.
- **lexical_v2 − artifacts** — lexical_v2 without the five columns that encode recording format (https, explicit scheme, `www.` prefix and two label counts); the analogous ablation of baseline28 removes `https_usage` and `num_subdomains`.
- **lexical_v2_canon** — the URL string is first *canonicalised* by removing the scheme and one leading `www.`/`wwwN.` label; lexical_v2 is computed on the result and the five artifact columns are dropped, leaving 86 features. Every feature is therefore invariant to the presence or form of the scheme and the `www.` prefix, a property verified by unit tests.

### C. Models

We evaluate the baseline's four models with its own hyper-parameters, so that every comparison is faithful to the original system: logistic regression (standardised inputs, C = 1, balanced class weights), a random forest of 200 trees with balanced class weights, XGBoost with 200 rounds of depth 6, learning rate 0.1 and row and column subsampling of 0.8, and the soft vote that averages their probabilities with weights 1:2:2. No hyper-parameter is tuned on test or external data. Linear and tree models were chosen because they dominate published lexical detectors (Section II-A, II-B) and expose the decision mechanism through coefficients and exact tree SHAP values.

### D. Evaluation protocols

We use three split protocols. **Random**: stratified 60/20/20. **Grouped**: ten stratified folds grouped by registered domain, of which two form the test set, two the validation set and six the training set, so that no registered domain appears in two partitions. **Leave-one-corpus-out (LOCO)**: for each of the six labelled corpora, the other five are pooled (each capped at 50,000 URLs, stratified), split by registered domain into training, validation and test partitions, and the entire held-out corpus becomes the evaluation set. In addition, models trained on corpus A or B are applied unchanged to every other corpus and feed (**external** evaluation).

### E. Operating points and calibration

For every model and seed, four thresholds are fixed on validation data: 0.5; the threshold maximising F1; and the most sensitive thresholds whose validation false-positive rate is at most 1 % and 0.1 %. The same thresholds are applied unchanged to test partitions and external corpora. Isotonic regression and Platt scaling are fitted on validation scores to test post-hoc calibration.

### F. Analyses

**Probe.** For each class separately, up to 8,000 URLs per corpus are pooled from the six labelled corpora and a multinomial logistic regression predicts the source corpus, under five-fold cross-validation grouped by registered domain (chance 1/6). **Explanations.** TreeExplainer SHAP values are computed for XGBoost on 3,000 test URLs. **Label-preserving variants.** *Tier A* transformations are equivalent under RFC 3986 and preserve the label by construction: upper-casing scheme and host, adding an empty-path slash, adding the default port, percent-encoding one unreserved path character and adding a fragment. *Tier B* transformations change only presentation and are *assumed* to preserve the label: toggling a leading `www.`, toggling `http`/`https` and appending a tracking parameter. We report how often the decision at 0.5 flips. **Errors.** False positives and false negatives are stratified by domain novelty, scheme, `www.`, length, path depth, encoding and hosting type.

### G. Metrics and statistics

Malicious URLs are the positive class. We report accuracy, precision, recall, specificity, F1, false-positive and false-negative rates, ROC-AUC, PR-AUC, the true-positive rate at 1 % and 0.1 % FPR, log-loss, Brier score and expected calibration error (ECE, 15 bins). On positive-only feeds only recall is defined. Results are averaged over seeds and reported as mean ± standard deviation; single-seed estimates carry 95 % percentile-bootstrap intervals; comparisons on identical test URLs use a paired bootstrap of metric differences and McNemar's exact test. A difference is called significant only if its paired 95 % interval excludes zero and its sign agrees across seeds.

## VII. Experimental Setup

All experiments ran on an Intel Core i7-1355U laptop processor (10 cores) with 16 GB of RAM and no GPU, under Windows 11 with Python 3.10.11, scikit-learn 1.7.2, XGBoost 3.2.0, SHAP 0.49.1 and tldextract 5.3.1. SHAP values for XGBoost are computed with XGBoost's built-in exact TreeSHAP. Runs on corpus A use seeds 42–46 and LOCO runs seeds 42–44. Each run stores its configuration, software environment, split indices with a domain-overlap report, per-URL predictions, metrics and resource measurements, so that every number in this paper can be regenerated. Table IV lists the runs reported and the number of seeds behind each.

<<TABLE|RUNS|Experiment runs reported in this paper. Seeds = completed random seeds per model; every number reported is a mean over these seeds.>>

## VIII. Results

### A. The source corpus of a URL is learnable (RQ1, RQ2)

If collection artifacts differ between corpora, a classifier should be able to tell corpora apart from lexical features alone. Table V confirms this. With lexical_v2, a linear probe identifies which of six corpora a **benign** URL comes from with accuracy 0.830, against a chance level of 0.167, and a malicious URL with accuracy 0.606. Dropping the five artifact columns barely changes this (0.814 and 0.578), because the scheme still leaks through slash, colon and length counts: the two scheme-less corpora remain identifiable with accuracy of 0.97 or more. Canonicalising the URL string before computing features lowers the accuracies to 0.617 and 0.428 and makes the scheme-less corpus B almost indistinguishable among benign URLs (0.184). PhiUSIIL's benign URLs remain identifiable at 0.981 even after canonicalisation, because being a bare homepage is a sampling property that no string transformation can remove. The baseline's own 28 features identify the source corpus with accuracy 0.803 (benign) and 0.577 (malicious).

<<TABLE|T10|Dataset-identification probe: accuracy of a six-way logistic regression predicting the source corpus of a URL (grouped five-fold cross-validation; chance = 0.167), overall and recall per corpus.>>

### B. In-distribution performance and the role of domain leakage (RQ1)

Random splitting leaks registered domains asymmetrically. With seed 42, 59.4 % of the phishing test URLs of corpus A share a registered domain with some training URL, against only 2.4 % of the benign test URLs (26.7 % overall); grouped splitting removes this overlap by construction. Despite the leakage, grouping hardly changes in-distribution performance (Table VI): every model reaches a ROC-AUC of 0.998–0.999 under both protocols, and F1 drops by at most 0.002. The models do not need memorised domains, because the collection artifacts already separate the classes.

<<MDTABLECAP|In-distribution test performance on corpus A with the original 28 features: random vs registered-domain-grouped split (mean ± sd over 5 seeds).>>

| Model | ROC-AUC random | ROC-AUC grouped | F1@0.5 random | F1@0.5 grouped |
|---|---|---|---|---|
| Logistic regression | 0.998 ± 0.000 | 0.998 ± 0.000 | 0.995 ± 0.001 | 0.993 ± 0.003 |
| Random forest | 0.998 ± 0.000 | 0.998 ± 0.000 | 0.996 ± 0.001 | 0.994 ± 0.003 |
| XGBoost | 0.999 ± 0.000 | 0.999 ± 0.000 | 0.996 ± 0.001 | 0.995 ± 0.003 |
| Soft vote 1:2:2 | 0.999 ± 0.000 | 0.999 ± 0.000 | 0.996 ± 0.001 | 0.995 ± 0.003 |

The differences between models are tiny. Paired on identical test URLs (Table VII), XGBoost is significantly better than logistic regression and random forest, but only by 0.0003–0.0004 ROC-AUC. The original 1:2:2 soft-voting ensemble is *not* significantly better than XGBoost alone (ΔROC-AUC = +0.0001, 95 % CI [−0.0000, 0.0002]; McNemar p = 0.21). The ensemble, the original system's main design choice, therefore adds cost but no measurable accuracy.

<<TABLE|PAIRED|Paired comparisons against XGBoost on the 48,181 grouped test URLs of corpus A (seed 42): bootstrap difference in ROC-AUC and F1 with 95 % confidence interval, and McNemar's exact test on paired decisions.>>

The explanations show what the models rely on. For XGBoost trained on corpus A, the mean absolute SHAP value of `https_usage` is 3.65 log-odds, followed by `num_slashes` (2.69), which in this corpus mostly records whether a URL has a path; every other feature contributes less than 0.45 (Fig. 3). In other words, the model has learnt that a URL with an https scheme and no path is benign. A model trained on the five pooled corpora still ranks the scheme first, but with a far smaller weight (0.74) and a flatter profile (`num_slashes` 0.65, `num_hyphens` 0.61, longest token 0.47).

<<FIG|shap_A_b28_grouped_xgb.png|Mean absolute SHAP value (log-odds of the malicious class) of the 20 most important features for XGBoost trained on corpus A with the original features (3,000 grouped test URLs).>>

The few in-distribution errors follow the same pattern. At the 1 % validation-FPR threshold, 70 % of the missed phishing URLs start with `www.`, although such URLs are only 37 % of the phishing test set: phishing URLs that look like the benign class are the ones the model misses. Conversely, every benign URL under a commonly abused suffix is flagged (11 of 11), and benign URLs of 31–50 characters are flagged 3.6 times as often as URLs of at most 30 characters (2.3 % vs 0.6 %).

### C. External corpora (RQ2, H1, H2)

Models trained on corpus A were applied unchanged to every other corpus, using the threshold selected on corpus-A validation data for a 1 % false-positive budget (Fig. 4, Table VIII). In-distribution the threshold holds: the realised test FPR is 0.9–1.0 % at a recall of 0.992–0.995. On every external labelled corpus it fails. **99.4–100 % of the benign URLs of Hannousse 2021, Ebbu2017, PhishStorm and ISCX-2016 are flagged**, as are 74 % (logistic regression) to 100 % (tree models and soft vote) of corpus B's benign URLs. Ranking quality collapses as well: external ROC-AUC lies between 0.56 and 0.76 on Hannousse, Ebbu2017 and PhishStorm and falls *below chance* on ISCX-2016 (0.42–0.47) and the Kaggle corpus (0.35–0.48), the two corpora in which `www.` marks phishing rather than benign URLs (Section V-B). The in-distribution ranking of models says nothing about their external ranking: random forest, tied for best in-distribution, has the lowest external ROC-AUC on Hannousse, Ebbu2017 and PhishStorm (0.56–0.62).

<<FIG|external_roc_auc_A_b28_grouped.png|ROC-AUC on the corpus-A grouped test split and on external labelled corpora for models trained on corpus A with the original features (mean ± sd over 5 seeds). Dotted line: chance.>>

<<TABLE|EXT|External evaluation of corpus-A models (original features, grouped split): ROC-AUC and the share of benign URLs flagged (FPR) at the threshold chosen on corpus-A validation data for FPR ≤ 1 %; PhishTank contains only phishing URLs (recall).>>

Recall on the positive-only feeds is 0.99–1.00 (PhishTank 0.992–0.995, OpenPhish 1.000, URLhaus 1.000). Together with the external false-positive rates, this describes a detector that flags essentially every URL not shaped like an `https://www.` homepage. At an operational prevalence of 1 % malicious URLs, a recall of 0.995 combined with an FPR of 0.994 gives a precision of about 1 %, no better than flagging at random. The models trained with a random split behave identically (external FPR 0.994–1.000 on the four independent corpora; external ROC-AUC 0.34–0.78).

### D. Removing artifact features (H1)

Removing the two artifact columns of the original features (`https_usage` and `num_subdomains`) leaves in-distribution ROC-AUC almost unchanged (0.998 for XGBoost and the soft vote, 0.997 for random forest, 0.981 for logistic regression) and does not repair external behaviour (Table IX). 95–100 % of the benign URLs of the four independent corpora are still flagged, and the ROC-AUC of XGBoost on ISCX-2016 falls further, to 0.11. The shortcut survives because the remaining length and slash features still encode the homepage-only benign class, as the probe predicted. The only notable improvement is for logistic regression on the scheme-less corpus B, whose FPR falls from 0.74 to 0.24, because the linear model can no longer shift all scheme-less URLs at once.

<<TABLE|ABL|Effect of removing the artifact columns (https_usage, num_subdomains) from the original features: external ROC-AUC and FPR at the validation-chosen 1 % FPR threshold (corpus A, grouped split; mean over completed seeds).>>

### E. Training on diverse corpora: leave-one-corpus-out (RQ3)

Training on five pooled corpora changes the failure mode (Fig. 5, Table X). Ranking transfers far better: with lexical_v2, the held-out ROC-AUC of XGBoost reaches 0.977 with PhiUSIIL held out, 0.927 with Hannousse 2021 held out and 0.874 with corpus B held out. Thresholds, however, do not transfer reliably, and they err in *different directions* for different unseen corpora. With PhiUSIIL held out, the threshold chosen for a 1 % false-positive budget flags no benign URL but catches only 15–42 % of phishing. With corpus B held out it flags 16 % (XGBoost), 18 % (random forest) and 95 % (logistic regression) of benign URLs. With Hannousse held out it lands close to the budget for logistic regression (1.2 %) and 6–8 times above it for the tree models.

<<FIG|loco_summary.png|Leave-one-corpus-out transfer (lexical_v2, mean ± sd over seeds): ROC-AUC on the held-out corpus (left) and the share of held-out benign URLs flagged at the threshold chosen on pooled validation data for FPR ≤ 1 % (right).>>

<<TABLE|LOCO|Leave-one-corpus-out results: models trained on the other five corpora and evaluated on the held-out corpus. Recall and FPR use the threshold chosen on pooled validation data for FPR ≤ 1 %.>>

Removing the artifact columns has mixed effects in this setting. With PhiUSIIL held out, held-out ROC-AUC *decreases* (XGBoost 0.977 → 0.878), so the columns carried information that transferred. With corpus B held out, logistic regression's over-flagging disappears (FPR 0.95 → 0.15). With Hannousse held out, ROC-AUC rises slightly (XGBoost 0.927 → 0.937) and the realised FPR moves closer to the budget (7.6 % → 4.5 %).

### F. Calibration under shift (H2)

In-distribution, all models are well calibrated (ECE 0.002–0.004 on the corpus-A test split), because almost all scores lie near 0 or 1 (Fig. 6). On external corpora, ECE rises to 0.42–0.78. Post-hoc calibration fitted on validation data does not help (Table XI): isotonic regression and Platt scaling leave both the external ECE and the external FPR at the 1 % threshold essentially unchanged (FPR 0.99–1.00 on the four independent corpora). In the leave-one-corpus-out setting, isotonic calibration even *increases* the held-out ECE, for example from 0.132 to 0.150 for XGBoost with PhiUSIIL held out. Calibration repairs probabilities only for the distribution it was fitted on; it cannot compensate for a shift in recording conventions.

<<FIG|reliability_A_b28_grouped.png|Reliability diagram on the corpus-A grouped test split (seed 42). Calibration error is small because almost all scores lie near 0 or 1; the few mid-range scores deviate from the diagonal.>>

<<TABLE|CAL|Post-hoc calibration fitted on validation data: expected calibration error (ECE) and FPR at the validation-chosen 1 % threshold, in-distribution and on external corpora (corpus-A models, original features, mean over seeds).>>

### G. Robustness to label-preserving URL variants (H1)

The sharpest evidence comes from transformations that cannot change a URL's meaning (Fig. 7, Table XII). For the corpus-A models, adding a slash to an empty path (`https://www.example.com` becomes `https://www.example.com/`, which RFC 3986 defines as equivalent) flips the decision for **100 % of benign URLs** (XGBoost; 99.8 % for logistic regression) and lowers ROC-AUC from 0.999 to 0.70. Switching between `http` and `https` flips 100 % of benign and 29 % of malicious decisions, and removing or adding a leading `www.` flips 84 % of benign decisions for XGBoost. Upper-casing the host, adding a fragment or percent-encoding a path character changes nothing, because the original features ignore them. The model trained on pooled corpora is far more stable: every transformation flips between 3 % and 15 % of its decisions, and none changes its ROC-AUC by more than 0.05.

<<FIG|mutation_flip_rates.png|Share of decisions (threshold 0.5) that flip under label-preserving URL transformations, for benign and malicious URLs (5,000 test URLs). (A) = equivalent under RFC 3986; (B) = presentation change assumed to preserve the label.>>

<<TABLE|MUT|Effect of label-preserving transformations on 5,000 test URLs: share of URLs to which the transformation applies, share of decisions that flip, and ROC-AUC before and after.>>

### H. Temporal recall on PhishTank (H3)

PhishTank's verified-online URLs carry submission timestamps, but only 64 of 67,326 predate 2021, so recall can be traced only over 2021–2026 (Fig. 8). The corpus-A models detect 98.8–99.8 % of PhishTank URLs in every year, which, given their external false-positive rates, reflects over-flagging rather than detection skill. The LOCO models show no consistent trend either: XGBoost with Hannousse held out ranges between 0.51 and 0.72 without a monotonic pattern, although the share of https phishing rose from 91 % in 2021 to 98 % in 2024. H3 is therefore not supported over this period.

<<FIG|temporal_recall_phishtank.png|Recall on PhishTank verified phishing URLs by submission year at the validation-chosen 1 % FPR threshold (lines) and share of https URLs per year (bars). Years with fewer than 100 URLs omitted.>>

### I. Computational cost

All models are cheap enough for inline use (Table XIII). Feature extraction costs about 0.08 ms per URL for the original features and about 0.9 ms for lexical_v2 on the test laptop. Batch scoring takes 0.005 ms per URL for logistic regression, 0.008 ms for XGBoost and 0.02–0.03 ms for random forest and the soft vote. Model size differs by four orders of magnitude: 16 kB for logistic regression, 0.37 MB for XGBoost, 55 MB for random forest and 56 MB for the soft vote, whose size and fit time (45 s versus 10 s for XGBoost) bring no accuracy benefit (Section VIII-B).

<<TABLE|COST|Computational cost on the test laptop (Intel i7-1355U, CPU only), original features, corpus A, median over seeds. Latency excludes feature extraction.>>

## IX. Discussion

**What the high scores measure.** The baseline reaches a ROC-AUC of 0.999 whether or not registered domains are shared between training and test data, its decisions flip when a slash is added to a homepage URL, and it flags essentially all benign URLs of four independently collected corpora. The simplest explanation consistent with all three observations is that the model learns *how each class was recorded* — benign URLs as `https://www.` homepages and phishing URLs as everything else — rather than properties of phishing. This is the shortcut-learning pitfall described by Arp et al. [arp2022dosdonts], instantiated here with named and measurable artifacts. It agrees with the benign-homepage effect observed for login pages [sanchezpaniagua2022phishing], with the Alexa index-page bias noted by Sabir et al. [sabir2022reliability] and with the `https://`/`www.` shortcut reported in a recent preprint [giri2026shieldphish]. The original system's verdict on `https://google.com/` is the same phenomenon seen through a single URL.

**Why cross-corpus results vary.** Because the artifacts change direction between corpora, a model's external performance depends largely on whether the target corpus shares the training corpus's recording conventions. This explains the below-chance ROC-AUC on ISCX-2016 and the Kaggle corpus, and why published cross-dataset results range from near chance [mia2024featurestrust, henry2026ensembletransfer] to moderate [liu2024transurl]: the outcome is mostly a property of the dataset pair, not of the model.

**Model choice is secondary; data choice is not.** In-distribution, logistic regression, random forest, XGBoost and the soft vote differ by at most 0.001 ROC-AUC, and the ensemble is statistically indistinguishable from XGBoost. Externally the same models differ by up to 0.2, in an order unrelated to their in-distribution ranking. Training data drawn from several corpora had a far larger effect than any modelling choice: it raised the held-out ROC-AUC of XGBoost from 0.35–0.75 (single-corpus training, external corpora) to 0.87–0.98 (0.77–0.98 across all three models) and reduced flip rates under label-preserving transformations from up to 100 % to at most 15 %.

**Feature removal is not enough.** Dropping artifact columns neither stops a probe from identifying the source corpus nor repairs external behaviour, because correlated features carry the same information. Canonicalising the URL string before feature extraction removes the scheme and `www.` information by construction and sharply reduces corpus identifiability; what it cannot remove is a sampling artifact such as a homepage-only benign class, which must be fixed when the data are collected.

**Thresholds are the operational failure.** Even where ranking transfers, a threshold chosen for a 1 % false-positive budget on one distribution over-flags on one unseen corpus and under-flags on another, and post-hoc calibration does not change this. Deployment therefore needs threshold recalibration on traffic from the target environment, a step the public-benchmark protocol never exercises.

**Answers to the research questions.** *RQ1:* in-distribution performance on PhiUSIIL is carried almost entirely by the scheme and homepage artifacts; domain memorisation adds nothing measurable there. *RQ2:* the artifacts change strength and direction across corpora, which explains why external performance ranges from moderate to below chance. *RQ3:* training on diverse corpora restores ranking (held-out ROC-AUC 0.87–0.98 for XGBoost and 0.77–0.98 across models) and stability, but neither feature removal nor calibration makes operating thresholds transferable. H1 and H2 are supported; H3 is not supported over 2021–2026.

**Implications for practice.** Phishing-URL detectors should be (i) trained on several independently collected corpora; (ii) evaluated on held-out *corpora* rather than held-out rows, at fixed false-positive budgets, with precision reported at realistic prevalence; (iii) fed canonicalised URLs so that recording format cannot act as a feature; (iv) checked with a dataset-identification probe and label-preserving transformations before deployment; and (v) recalibrated on traffic from the deployment environment. A deployed system should present its output as a risk estimate, never as a guarantee that a URL is safe.

## X. Threats to Validity

*Construct validity.* All corpora are public compilations with their own artifacts, so "external" means "differently collected", not "real user traffic"; our results expose failure modes rather than estimate deployment performance. Labels are inherited from blacklists and curated lists and were not re-verified. Tier B transformations (scheme and `www.` toggles) are assumed, not proven, to preserve the label.

*Internal validity.* The original project's dataset could not be obtained; conclusions about it rest on PhiUSIIL, whose benign class has the same `https://www.` form, and on a size-matched sample of its probable source lineage. Registered-domain grouping does not remove near-duplicate phishing pages that share a kit across different domains. The canonicalised representation and the leave-one-corpus-out design were added after the dataset probe and after inspecting the first baseline run, and are reported as such; no hyper-parameter or threshold was tuned on test or external data.

*External validity.* All labelled corpora are roughly balanced, so precision at realistic prevalence is derived analytically. Timestamped data are positive-only and concentrated in 2021–2026. Only linear and tree-based models on lexical features were evaluated; character-level and transformer models, which see the raw scheme and `www.` tokens directly, may behave differently.

*Conclusion validity.* Results are averaged over two to five seeds per run (Table IV), and paired comparisons use bootstrap intervals and McNemar's test; differences below about 0.001 ROC-AUC should not be interpreted.

## XI. Conclusion and Future Work

Lexical phishing-URL detectors evaluated on a public corpus can reach a ROC-AUC of 0.999 while flagging 99–100 % of the benign URLs of four other public corpora, and while flipping their decision when a slash is added to a homepage URL. We traced this to how each corpus recorded its classes — the scheme, the `www.` prefix and homepage-only benign URLs — whose predictive direction reverses between corpora, so that the source corpus of a URL can be predicted from lexical features with up to 83 % accuracy against 17 % chance. Removing artifact features and calibrating probabilities do not fix the problem. Training on several corpora restores much of the ranking ability and stability on unseen corpora but leaves operating thresholds unreliable. For the system we started from, the weighted ensemble adds cost without accuracy, and a parsing defect disables its host features for scheme-less URLs.

Future work will evaluate character-level CNNs on raw and canonicalised URLs and canonicalised features in the leave-one-corpus-out setting, build a benign URL collection sampled from real browsing traffic with paths and realistic prevalence, and study threshold adaptation with a small amount of labelled data from the target environment.

