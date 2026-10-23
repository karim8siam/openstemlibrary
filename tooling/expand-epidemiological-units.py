#!/usr/bin/env python3
"""
Expand Units 2, 4, and 8 of Epidemiological Statistics to ensure word count comfortably exceeds 25,500.
"""
from pathlib import Path
import re

DRAFT_DIR = Path("publishing/drafts/statistics-probability-epidemiological-statistics")

# 1. Expand Unit 2
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")

extra_u2 = r"""
## 2.6 The E-Value and Quantification of Unmeasured Confounding

In observational studies, investigators frequently encounter the skepticism that an observed relative risk ($RR$) could be entirely explained away by an unmeasured confounder $U$ (such as genetic susceptibility or subtle lifestyle differences). To address this challenge quantitatively without requiring complex parametric simulations, Tyler VanderWeele and Peng Ding (2017) formulated the **E-Value**.

### Mathematical Definition of the E-Value
The E-value is defined as the minimum strength of association, on the risk ratio scale, that an unmeasured confounder $U$ would need to have with both the exposure and the outcome, conditional on the measured covariates, to fully explain away an observed exposure-outcome association:

$$\text{E-value} = RR + \sqrt{RR(RR - 1)}$$

for an observed $RR > 1.0$. (If $RR < 1.0$, one first takes the reciprocal $1 / RR$).

For example, if an observational study reports an observed risk ratio of $RR = 3.0$ between an occupational solvent and pancreatic cancer:
$$\text{E-value} = 3.0 + \sqrt{3.0(3.0 - 1)} = 3.0 + \sqrt{6.0} \approx 3.0 + 2.4495 = 5.45$$
To explain away this observed association, an unmeasured confounder would have to be associated with both solvent exposure and pancreatic cancer by a risk ratio of at least $5.45$-fold, above and beyond all measured covariates. If no known plausible risk factor exhibits an association of that magnitude, the causal finding is remarkably robust.

To evaluate whether the association could be explained away by chance plus unmeasured confounding, the E-value is also evaluated for the confidence interval limit closest to the null ($RR_{\text{lower}}$):
$$\text{E-value}_{\text{lower}} = RR_{\text{lower}} + \sqrt{RR_{\text{lower}}(RR_{\text{lower}} - 1)}$$
If $RR_{\text{lower}} = 2.0$, the E-value for the lower limit is $2.0 + \sqrt{2(1)} \approx 3.41$. Reporting the E-value alongside relative risks transforms vague qualitative discussions of "residual confounding" into transparent, quantitative sensitivity assessments.
"""

if "## 2.6 The E-Value" not in u2_text:
    u2_text = u2_text.replace("## Fully worked question 1:", extra_u2.strip() + "\n\n## Fully worked question 1:")
    u2_path.write_text(u2_text, encoding="utf-8")
    print("Unit 2 expanded.")

# 2. Expand Unit 4
u4_path = DRAFT_DIR / "unit-4.md"
u4_text = u4_path.read_text(encoding="utf-8")

extra_u4 = r"""
## 4.7 Directed Acyclic Graph Topologies: Frontdoor Criterion and Instrumental Variables

Beyond the classical Backdoor Criterion, graphical causal inference provides alternative topological structures for identifying causal effects even in the presence of unmeasured confounding:

### Pearl's Frontdoor Criterion
Suppose an unmeasured confounder $U$ severely confounds the direct link between exposure $E$ and outcome $D$ ($E \leftarrow U \to D$), such that no backdoor adjustment can block the path. If there exists an intermediate variable $M$ on the causal pathway ($E \to M \to D$) that satisfies the **Frontdoor Criterion**:
1. $E$ intercepts all directed causal paths from $E$ to $D$ via $M$.
2. There are no unblocked backdoor paths from $E$ to $M$.
3. All backdoor paths from $M$ to $D$ are blocked by conditioning on $E$.

Then the average causal effect of $E$ on $D$ is completely identified through the frontdoor adjustment formula:
$$P(Y = y \mid \text{do}(E = x)) = \sum_m P(M = m \mid E = x) \sum_{x'} P(Y = y \mid E = x', M = m) P(E = x')$$
This celebrated theorem demonstrates that causal effects can be identified even when an exposure and outcome share intractable unmeasured confounding!

### Instrumental Variables and Mendelian Randomization
An **Instrumental Variable** ($Z$) is an exogenous variable that satisfies three strict core assumptions:
1. **Relevance**: $Z$ has a causal effect on exposure $E$ ($Z \to E$).
2. **Exclusion Restriction**: $Z$ affects outcome $D$ exclusively through its effect on $E$, with no direct causal pathway ($Z \to D$ is absent).
3. **Independence (Unconfoundedness)**: $Z$ shares no common causes with $D$ ($Z \leftarrow U \to D$ is absent).

In genetic epidemiology, **Mendelian Randomization** exploits inherited genetic variants (e.g., single nucleotide polymorphisms, SNPs) as natural instrumental variables. Because alleles are randomly assorted during meiosis at gametogenesis, genetic inheritance acts as a lifelong natural randomized controlled trial, permitting unconfounded estimation of modifiable behavioral or biochemical risk factors (such as circulating LDL cholesterol or uric acid) on chronic cardiovascular endpoints via two-stage least squares estimators:
$$\widehat{\beta}_{\text{causal}} = \frac{\text{Cov}(Z, Y)}{\text{Cov}(Z, E)} = \frac{\widehat{\beta}_{ZY}}{\widehat{\beta}_{ZE}}$$
"""

if "## 4.7 Directed Acyclic Graph Topologies" not in u4_text:
    u4_text = u4_text.replace("## Fully worked question 1:", extra_u4.strip() + "\n\n## Fully worked question 1:")
    u4_path.write_text(u4_text, encoding="utf-8")
    print("Unit 4 expanded.")

# 3. Expand Unit 8
u8_path = DRAFT_DIR / "unit-8.md"
u8_text = u8_path.read_text(encoding="utf-8")

extra_u8 = r"""
## 8.7 Accelerated Failure Time (AFT) Models & Competing Risks Subdistribution Hazards

While the Cox proportional hazards model is the most widely applied survival model in medical literature, two critical alternative frameworks are essential for comprehensive epidemiological mastery:

### Accelerated Failure Time (AFT) Models
Under the **Accelerated Failure Time (AFT)** formulation, the effect of an exposure is modeled not as a multiplicative hazard shift, but as a direct acceleration or deceleration of the biological survival time clock:

$$\ln(T_i) = \mathbf{x}_i^T \boldsymbol{\beta} + \sigma \varepsilon_i$$

where $\varepsilon_i$ is a random error disturbance with a pre-specified distribution (e.g., standard extreme value yielding the Weibull AFT, logistic yielding log-logistic AFT, or Gaussian yielding log-normal AFT). The exponentiated coefficient $\exp(\beta_1)$ represents the **Acceleration Factor** ($\gamma$):
$$T(X = 1) \stackrel{d}{=} \gamma \cdot T(X = 0)$$
- If $\gamma > 1.0$: The exposure prolongs time-to-event (decelerates aging/progression); the median survival time is multiplied by $\gamma$.
- If $\gamma < 1.0$: The exposure accelerates time-to-failure.
Unlike hazard ratios, acceleration factors are easily communicated to non-statistical clinical audiences as percentage changes in survival time.

### Competing Risks and Fine-Gray Subdistribution Hazards
In aging populations, individuals are simultaneously at risk of multiple mutually exclusive terminating events (e.g., death from cardiovascular disease, death from prostate cancer, or fatal motor vehicle trauma). Treating competing deaths as simple independent censoring violates non-informative censoring, producing severe upward bias in the cumulative incidence of the primary event.

Robert Gray (1988) and Jason Fine and Robert Gray (1999) resolved this by modeling the **Cumulative Incidence Function** ($CIF_k(t) = P(T \le t, \text{Cause} = k)$) directly through the **Subdistribution Hazard**:

$$\bar{h}_k(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t, \text{Cause} = k \mid T \ge t \text{ or } (T < t \text{ and } \text{Cause} \neq k))}{\Delta t}$$

In the Fine-Gray subdistribution risk set, an individual who dies from a competing cause (e.g., heart disease at month 12) remains in the denominator risk set indefinitely for the cancer outcome, preventing the false inflation of cancer cumulative incidence. Fitting proportional subdistribution hazards regression models ensures mathematically sound risk prediction in the presence of competing terminal events.
"""

if "## 8.7 Accelerated Failure Time" not in u8_text:
    u8_text = u8_text.replace("## Fully worked question 1:", extra_u8.strip() + "\n\n## Fully worked question 1:")
    u8_path.write_text(u8_text, encoding="utf-8")
    print("Unit 8 expanded.")
