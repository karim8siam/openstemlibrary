from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-research-methods"
p5 = DRAFT_DIR / "unit-5.md"
t5 = p5.read_text(encoding="utf-8")

extra = r"""
## 5.11 Monte Carlo Simulation-Based Power for Non-Standard Statistical Models
While analytical closed-form sample size formulas exist for classical linear models and tests of two independent proportions, real-world scientific investigations routinely involve non-standard designs for which closed-form sampling distributions do not exist:
- Generalized Linear Mixed Models (GLMMs) with crossed random effects for subjects and experimental stimuli.
- Zero-inflated Poisson or negative binomial regressions modeling overdispersed microbial read counts.
- Survival analysis models under complex, non-proportional hazards with time-varying covariates.
- Structural equation models with latent mediation and non-normal multivariate indicators.

For such complex architectures, methodologists deploy Monte Carlo Simulation-Based Power Analysis. The algorithm proceeds across four systematic phases:
1. Specify the Data-Generating Process (DGP): Define the structural population model, specifying fixed effects (the target effect sizes $\boldsymbol{\beta}$ representing the minimal clinically meaningful difference), random effect covariance matrices $\boldsymbol{\Sigma}$, error distributions, and expected dropout rates.
2. Iterative Synthetic Sampling: Using pseudo-random number generation, generate $B$ independent synthetic datasets (typically $B = 1,000$ to $10,000$ iterations) from the specified DGP at candidate sample size $N$.
3. Model Estimation: Fit the planned complex statistical model to each synthetic dataset, recording the test statistic and $p$-value for the parameter of interest.
4. Empirical Power Calculation: The estimated statistical power is simply the proportion of synthetic iterations that reject the null hypothesis at the specified significance threshold $\alpha$:
$$\widehat{\text{Power}} = \frac{1}{B} \sum_{b=1}^B \mathbb{I}(p_b < \alpha)$$
Because $\widehat{\text{Power}}$ is an empirical proportion, its simulation standard error is:
$$\mathrm{SE}(\widehat{\text{Power}}) = \sqrt{\frac{\widehat{\text{Power}}(1 - \widehat{\text{Power}})}{B}}$$
For $B = 2,500$ iterations at target power $0.80$, the simulation standard error is $\sqrt{0.80 \times 0.20 / 2500} = 0.008$ ($0.8\%$), yielding a tight $95\%$ confidence interval of $[78.4\%, 81.6\%]$. The researcher repeats this simulation across a grid of candidate sample sizes $N \in [50, 500]$ to trace the empirical power curve, identifying the exact sample size where $\widehat{\text{Power}} \ge 0.80$.

## 5.12 Practical Guidelines for Writing Sample Size Justifications in Grants
Funding agencies and Institutional Review Boards require rigorous, transparent sample size justifications. A defensible power analysis section must document:
1. The Primary Outcome: Clearly designate the single primary clinical or behavioral endpoint upon which sample size is calibrated.
2. Target Effect Size Rationale: Justify the selected effect size based on minimal clinically meaningful difference or preliminary pilot data, rather than post-hoc data dredging.
3. Design Specifications: Specify the exact statistical test, whether the test is one-tailed or two-tailed, nominal $\alpha$, target power $1 - \beta$, and anticipated attrition/dropout rates.
4. Software Reproducibility: Report the software packages, versions, and random seeds used to compute power.
"""

t5 = t5.replace("## 5.7 Unit 5 Methodological Synthesis and Review", extra.strip() + "\n\n## 5.7 Unit 5 Methodological Synthesis and Review")
p5.write_text(t5, encoding="utf-8")
print("Unit 5 boosted.")
