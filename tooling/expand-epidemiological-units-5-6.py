#!/usr/bin/env python3
"""
Add final depth to Units 5 and 6 to pass 25,000 words cleanly.
"""
from pathlib import Path

DRAFT_DIR = Path("publishing/drafts/statistics-probability-epidemiological-statistics")

# 1. Expand Unit 5
u5_path = DRAFT_DIR / "unit-5.md"
u5_text = u5_path.read_text(encoding="utf-8")

extra_u5 = r"""
## 5.7 Zero-Inflated and Two-Part Hurdle Models for Excess Zero Counts

In healthcare utilization studies and environmental exposure monitoring, count data often exhibit a massive excess of zero observations far beyond what even a negative binomial distribution can accommodate. For example, in an annual survey of emergency department visits or days absent from work due to acute occupational asthma, $85\%$ of healthy workers may report exactly zero events.

Epidemiologists model this phenomenon through two distinct statistical paradigms:
1. **Zero-Inflated Poisson (ZIP) and Zero-Inflated Negative Binomial (ZINB) Models**:
   Postulate that the population is a mixture of two distinct latent subpopulations: an "always-zero" immune group who cannot experience the event (with probability $p_i$), and a susceptible count group whose event frequencies follow a Poisson or negative binomial distribution:
   $$P(Y_i = 0 \mid \mathbf{x}_i) = p_i + (1 - p_i) \exp(-\mu_i)$$
   $$P(Y_i = y_i \mid \mathbf{x}_i) = (1 - p_i) \frac{\mu_i^{y_i} \exp(-\mu_i)}{y_i!}, \quad y_i \ge 1$$
   The zero probability $p_i$ is modeled via a logistic link ($\text{logit}(p_i) = \mathbf{z}_i^T \boldsymbol{\gamma}$), while the count process $\mu_i$ is modeled via a log link ($\ln(\mu_i) = \mathbf{x}_i^T \boldsymbol{\beta}$).
2. **Two-Part Hurdle Models**:
   Formulate a sequential hurdle process: first, a binary logistic model determines whether an individual crosses the hurdle from zero to at least one event ($P(Y_i > 0)$); second, conditional on crossing the hurdle ($Y_i \ge 1$), a truncated-at-zero count distribution governs event frequency. Unlike zero-inflated models, hurdle models cleanly separate the initial propensity to use healthcare from subsequent frequency of use.
"""

if "## 5.7 Zero-Inflated and Two-Part Hurdle" not in u5_text:
    u5_text = u5_text.replace("## Fully worked question 1:", extra_u5.strip() + "\n\n## Fully worked question 1:")
    u5_path.write_text(u5_text, encoding="utf-8")
    print("Unit 5 expanded.")

# 2. Expand Unit 6
u6_path = DRAFT_DIR / "unit-6.md"
u6_text = u6_path.read_text(encoding="utf-8")

extra_u6 = r"""
## 6.7 Clinical Utility and Decision Curve Analysis (DCA)

While Sensitivity, Specificity, and the Area Under the ROC Curve evaluate statistical discrimination, they do not tell a clinician whether using a diagnostic biomarker will actually improve clinical patient outcomes. An expensive or invasive biomarker with an $AUC = 0.82$ might confer zero clinical utility if its false-positive referrals lead to severe biopsy complications.

To quantify clinical utility across varying patient preferences, Andrew Vickers and Elena Elkin (2006) introduced **Decision Curve Analysis (DCA)** based on the concept of **Net Benefit** ($NB$):

$$NB(p_t) = \frac{TP}{N} - \frac{FP}{N} \left( \frac{p_t}{1 - p_t} \right) = \text{True Positive Fraction} - \text{False Positive Fraction} \times \text{Odds}(p_t)$$

where $p_t \in (0, 1)$ is the **decision threshold probability** at which a patient or clinician is indifferent between initiating treatment and withholding treatment.
- The weighting factor $p_t / (1 - p_t)$ explicitly penalizes false-positive decisions relative to true-positive benefits according to the clinical cost-benefit ratio.
- In a Decision Curve plot, the Net Benefit of the diagnostic strategy is plotted against $p_t$ and compared against two default clinical reference policies: "Treat All Patients" and "Treat No Patients".
- A diagnostic biomarker has clinical utility over the threshold range where its Net Benefit curve lies strictly above both default strategies. Decision Curve Analysis provides the quantitative bridge linking epidemiologic diagnostic accuracy with clinical decision-making.
"""

if "## 6.7 Clinical Utility and Decision Curve Analysis" not in u6_text:
    u6_text = u6_text.replace("## Fully worked question 1:", extra_u6.strip() + "\n\n## Fully worked question 1:")
    u6_path.write_text(u6_text, encoding="utf-8")
    print("Unit 6 expanded.")
