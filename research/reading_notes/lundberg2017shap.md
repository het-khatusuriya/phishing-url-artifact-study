# lundberg2017shap

## Citation
Scott M. Lundberg; Su-In Lee (2017). *A Unified Approach to Interpreting Model Predictions*. Advances in Neural Information Processing Systems 30 (NeurIPS 2017). URL: https://arxiv.org/abs/1705.07874

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/lundberg2017shap.pdf).
- Evidence: Semantic Scholar API record for arXiv:1705.07874 (title/authors/year/venue), arXiv abs page; NeurIPS proceedings have no DOI (the DOI returned by Semantic Scholar, 10.9728/dcs.2024.25.7.1847, is spurious and was discarded). PDF from arXiv.

## Problem
Many feature-attribution methods exist with no principled way to choose among them.

## Method
Defines the class of additive feature attribution methods, shows a unique solution (SHAP values) satisfying three desirable properties, and gives model-agnostic (KernelSHAP) and model-specific estimators.

## Dataset(s)
None specific to security; experiments on standard ML benchmarks and MNIST-style tasks (see paper Sec. 5).

## Features
n/a

## Evaluation protocol
Theoretical axioms (local accuracy, missingness, consistency) + user-study agreement and sample-efficiency experiments

## Metrics reported (only numbers present in the source)
No security metrics; qualitative/user-study results only (paper Sec. 5, Fig. 4-5).

## Main findings
SHAP unifies LIME, DeepLIFT, layer-wise relevance propagation and Shapley sampling; KernelSHAP is more sample-efficient than LIME-style sampling.

## Limitations
- Authors' stated limitations: Exact Shapley computation is exponential; KernelSHAP is an approximation and assumes feature independence under the background distribution.
- My assessment: Explanations on correlated lexical URL features (e.g. url_length vs. path_length) can split credit arbitrarily; needs TreeExplainer or grouped features.

## Research gap
Little guidance on explanation stability under input perturbation, which we need for mutation-robustness tests.

## Relevance to our project (score 5/5)
Foundational citation for our SHAP usage; defines the properties we rely on when reporting global feature importance.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
