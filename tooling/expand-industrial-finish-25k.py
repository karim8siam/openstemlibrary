#!/usr/bin/env python3
"""
Final expansion for Industrial and Official Statistics to exceed 25,000 words.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

# Unit 3 expansion: SPRT and Attribute OC curves
u3_path = DRAFT_DIR / "unit-3.md"
u3_text = u3_path.read_text(encoding="utf-8")
u3_add = r"""
## 3.11 Sequential Probability Ratio Tests (SPRT) for Attributes

When attribute inspection must achieve the absolute minimum average sample size, quality engineers deploy Abraham Wald's **Sequential Probability Ratio Test (SPRT)**. 

Consider testing the simple hypothesis that the defect probability is $H_0: p = p_0$ against the alternative hypothesis $H_1: p = p_1$ (with $p_1 > p_0$), with pre-specified Type I error probability $\alpha$ and Type II error probability $\beta$.

Items are inspected one by one. Let $X_m \in \{0, 1\}$ denote the inspection result of the $m$-th item, and let $d_m = \sum_{j=1}^m X_j$ be the cumulative number of nonconforming items found after inspecting $m$ units.

The likelihood ratio after $m$ observations is:

$$\Lambda_m = \frac{\prod_{j=1}^m P(X_j \mid p_1)}{\prod_{j=1}^m P(X_j \mid p_0)} = \frac{p_1^{d_m} (1 - p_1)^{m - d_m}}{p_0^{d_m} (1 - p_0)^{m - d_m}} = \left(\frac{p_1}{p_0}\right)^{d_m} \left(\frac{1 - p_1}{1 - p_0}\right)^{m - d_m}$$

Wald's decision rule compares $\Lambda_m$ against two boundary thresholds $B \approx \frac{\beta}{1 - \alpha}$ and $A \approx \frac{1 - \beta}{\alpha}$:
- If $\Lambda_m \le B$: Accept $H_0$ (process is in control; cease sampling).
- If $\Lambda_m \ge A$: Reject $H_0$ (process is out of control; trigger immediate alarm).
- If $B < \Lambda_m < A$: Continue inspection (draw the $(m+1)$-th item).

Taking natural logarithms linearizes the decision boundaries:

$$\ln B \le d_m \ln\left(\frac{p_1}{p_0}\right) + (m - d_m) \ln\left(\frac{1 - p_1}{1 - p_0}\right) \le \ln A$$

Solving for the cumulative defect count $d_m$ yields two parallel linear decision lines:

$$d_m \le -h_1 + s \cdot m \quad (\text{Acceptance Line})$$
$$d_m \ge h_2 + s \cdot m \quad (\text{Rejection Line})$$

where the slope $s$ and intercepts $h_1, h_2$ are:

$$s = \frac{\ln\left(\frac{1 - p_0}{1 - p_1}\right)}{\ln\left(\frac{p_1}{p_0}\right) + \ln\left(\frac{1 - p_0}{1 - p_1}\right)}, \qquad h_1 = \frac{\ln\left(\frac{1 - \alpha}{\beta}\right)}{\ln\left(\frac{p_1}{p_0}\right) + \ln\left(\frac{1 - p_0}{1 - p_1}\right)}, \qquad h_2 = \frac{\ln\left(\frac{1 - \beta}{\alpha}\right)}{\ln\left(\frac{p_1}{p_0}\right) + \ln\left(\frac{1 - p_0}{1 - p_1}\right)}$$

The sequential attribute chart inspects parts one by one, halting on average $40\%$ to $60\%$ faster than fixed-sample $p$-charts.
"""
idx3 = u3_text.find("## Fully worked question 1:")
u3_text = u3_text[:idx3] + u3_add.strip() + "\n\n" + u3_text[idx3:]
u3_path.write_text(u3_text, encoding="utf-8")
print("Unit 3 expanded.")

# Unit 4 expansion: Adaptive Sampling (VSI and VSS)
u4_path = DRAFT_DIR / "unit-4.md"
u4_text = u4_path.read_text(encoding="utf-8")
u4_add = r"""
## 4.12 Adaptive Statistical Process Control: Variable Sampling Intervals (VSI) and Sample Sizes (VSS)

Classical Shewhart, CUSUM, and EWMA control charts employ rigid, fixed sampling intervals $h$ (e.g., take a sample of size $n = 5$ every $h = 1.0\text{ hour}$). This static cadence is statistically inefficient: when the monitored sample mean falls very close to the center line (indicating strong evidence of stability), the process is inspected just as frequently as when the sample mean plots dangerously close to the warning limit.

To maximize statistical responsiveness while preserving long-term inspection budgets, Marion R. Reynolds et al. (1988) formulated **Adaptive Control Charts**:

### Variable Sampling Interval (VSI) Charts
In a VSI control chart, the inter-sample inspection interval $h$ switches dynamically between two values:
- $h_1$ (Short sampling interval, e.g., $15\text{ minutes}$): Applied whenever the current sample statistic plots in a **warning region** ($w \le |Z_t| < 3$), indicating heightened suspicion of an incipient assignable cause.
- $h_2$ (Long sampling interval, e.g., $2.0\text{ hours}$): Applied whenever the current sample statistic plots in the **central region** ($|Z_t| < w$), confirming robust in-control operation.

Let $p_0 = P(|Z_t| < w \mid \text{in-control})$ be the probability that a sample falls in the central region under in-control conditions. The average in-control sampling interval is:

$$\bar{h}_0 = p_0 h_2 + (1 - p_0) h_1$$

By setting $\bar{h}_0$ equal to the standard fixed sampling interval $h_{\text{fixed}}$, the VSI chart consumes the exact same long-term inspection budget as a classical chart, but reduces the Average Time to Signal ($ATS_1$) for small and moderate shifts by **over $50\%$**!

### Variable Sample Size (VSS) Charts
Similarly, Variable Sample Size (VSS) charts switch the subgroup size between a small sample $n_1$ (when $|Z_t| < w$) and a large sample $n_2$ (when $w \le |Z_t| < 3$). Combining both approaches yields the **Variable Sample Size and Sampling Interval (VSSI)** chart, achieving near-optimal sequential detection without continuous-time sensor hardware.
"""
idx4 = u4_text.find("## Fully worked question 1:")
u4_text = u4_text[:idx4] + u4_add.strip() + "\n\n" + u4_text[idx4:]
u4_path.write_text(u4_text, encoding="utf-8")
print("Unit 4 expanded.")

# Unit 5 expansion: Unknown Sigma Variables Sampling
u5_path = DRAFT_DIR / "unit-5.md"
u5_text = u5_path.read_text(encoding="utf-8")
u5_add = r"""
## 5.11 Variables Acceptance Sampling with Unknown Process Variance ($s$-Method)

In many procurement and receiving inspection settings, the historical process standard deviation is not known with certainty. The vendor may have modified tooling, introduced a new material batch, or the customer may be inspecting an initial prototype lot. In such environments, the standard deviation must be estimated directly from the sample:

$$S = \sqrt{\frac{1}{n - 1} \sum_{i=1}^n (X_i - \bar{X})^2}$$

### The Quality Index and the Non-Central $t$-Distribution
For an Upper Specification Limit $USL$, the sample quality index is:

$$Q_{USL} = \frac{USL - \bar{X}}{S}$$

The lot is accepted if $Q_{USL} \ge k_s$, where $k_s$ is the critical acceptance constant for the $s$-method.

Because $S$ is a random variable, $Q_{USL}$ does not follow a normal distribution. Instead, multiplying $Q_{USL}$ by $\sqrt{n}$:

$$\sqrt{n} Q_{USL} = \frac{\sqrt{n} (USL - \bar{X})}{S} = \frac{\frac{\sqrt{n} (USL - \mu)}{\sigma} - \frac{\sqrt{n} (\bar{X} - \mu)}{\sigma}}{S / \sigma} = \frac{\delta - Z}{\sqrt{\chi^2_{n-1} / (n-1)}}$$

This random variable follows a **Non-Central Student $t$-Distribution** with $df = n - 1$ degrees of freedom and non-centrality parameter $\delta = \sqrt{n} Z_p$, where $Z_p = \frac{USL - \mu}{\sigma}$:

$$\sqrt{n} Q_{USL} \sim t'_{n-1}(\delta = \sqrt{n} Z_p)$$

### Determination of Sample Size $n_s$ and Constant $k_s$
To satisfy the two contractual benchmark conditions:
$$P(Q_{USL} \ge k_s \mid p = p_1) = 1 - \alpha, \qquad P(Q_{USL} \ge k_s \mid p = p_2) = \beta$$

Using the non-central $t$-distribution quantiles, or applying W. A. Wallis's (1947) standard approximation:

$$n_s \approx n_\sigma \left( 1 + \frac{k^2}{2} \right)$$

where $n_\sigma$ is the sample size derived under the known-$\sigma$ method, and $k \approx k_s$:

$$k_s = \frac{Z_\alpha Z_{p_2} + Z_\beta Z_{p_1}}{Z_\alpha + Z_\beta}$$

Because the estimation of $S$ introduces extra sampling variability, the required sample size under the unknown-$\sigma$ method is typically $2.5$ to $3.5$ times larger than under the known-$\sigma$ method ($n_s \approx 3 n_\sigma$), though still substantially smaller than the equivalent attribute sampling plan.
"""
idx5 = u5_text.find("## Fully worked question 1:")
u5_text = u5_text[:idx5] + u5_add.strip() + "\n\n" + u5_text[idx5:]
u5_path.write_text(u5_text, encoding="utf-8")
print("Unit 5 expanded.")

# Unit 6 expansion: Bayesian Reliability Estimation
u6_path = DRAFT_DIR / "unit-6.md"
u6_text = u6_path.read_text(encoding="utf-8")
u6_add = r"""
## 6.10 Bayesian Reliability Estimation and Zero-Failure Testing Protocols

In ultra-high reliability engineering—such as space mission satellites, commercial aircraft avionics, and deep-well subsea blow-out preventers—qualification tests often terminate with **zero failures observed** ($r = 0$). Under classical Maximum Likelihood Estimation, if $r = 0$, the point estimate for failure rate is $\widehat{\lambda} = 0 / T_{\text{total}} = 0$, implying infinite MTTF—a physical absurdity that cannot guide engineering decisions.

To extract rigorous statistical inference from zero-failure testing, reliability engineers utilize **Bayesian Reliability Methods**, integrating prior engineering physics and historical component data with test observations.

### Conjugate Gamma-Exponential Model
Let the component lifetime follow an exponential distribution with failure rate $\lambda \sim \text{Exp}(\lambda)$. The prior knowledge regarding $\lambda$ is modeled using a conjugate **Gamma Distribution** $\text{Gamma}(\alpha_0, \beta_0)$:

$$\pi(\lambda) = \frac{\beta_0^{\alpha_0}}{\Gamma(\alpha_0)} \lambda^{\alpha_0 - 1} e^{-\beta_0 \lambda}, \qquad \lambda > 0$$

where $\alpha_0$ represents the prior pseudo-failure count and $\beta_0$ represents the prior pseudo-operating hours.

Suppose an empirical life test observes $r$ failures accumulated over total time on test $T_{\text{total}}$. By Bayes' theorem, the posterior distribution is also Gamma:

$$\pi(\lambda \mid r, T_{\text{total}}) \propto L(\lambda) \pi(\lambda) \propto \left( \lambda^r e^{-\lambda T_{\text{total}}} \right) \left( \lambda^{\alpha_0 - 1} e^{-\beta_0 \lambda} \right) = \lambda^{(\alpha_0 + r) - 1} e^{-(\beta_0 + T_{\text{total}}) \lambda}$$

Thus, the posterior distribution is:

$$\lambda \mid \text{data} \sim \text{Gamma}(\alpha_1 = \alpha_0 + r, \; \beta_1 = \beta_0 + T_{\text{total}})$$

### Posterior Point and Interval Estimators
The posterior expected failure rate and posterior MTTF are:

$$\mathbb{E}[\lambda \mid \text{data}] = \frac{\alpha_1}{\beta_1} = \frac{\alpha_0 + r}{\beta_0 + T_{\text{total}}}, \qquad \widehat{\text{MTTF}}_{\text{Bayes}} = \frac{\beta_0 + T_{\text{total}}}{\alpha_0 + r}$$

When **zero failures occur** ($r = 0$) under an uninformative prior ($\alpha_0 = 1, \beta_0 = 0$, corresponding to a uniform prior on $\ln \lambda$):
$$\widehat{\text{MTTF}} = \frac{T_{\text{total}}}{1} = T_{\text{total}}$$
Furthermore, a one-sided $(1 - \alpha)100\%$ Bayesian lower credibility limit on reliability $R(t) = e^{-\lambda t}$ is derived directly from the cumulative chi-square distribution:

$$\lambda_{\text{upper}} = \frac{\chi^2_{1-\alpha, 2(\alpha_0 + r)}}{2(\beta_0 + T_{\text{total}})}$$

$$R_{\text{lower}}(t) = \exp(-\lambda_{\text{upper}} t)$$

Bayesian reliability analysis converts zero-failure test runs into valid contractual qualification certificates, preventing expensive, pointless test overruns.
"""
idx6 = u6_text.find("## Fully worked question 1:")
u6_text = u6_text[:idx6] + u6_add.strip() + "\n\n" + u6_text[idx6:]
u6_path.write_text(u6_text, encoding="utf-8")
print("Unit 6 expanded.")
