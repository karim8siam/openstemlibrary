#!/usr/bin/env python3
"""
Expand Units 3 and 4 for Industrial and Official Statistics.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

u3_text = (DRAFT_DIR / "unit-3.md").read_text(encoding="utf-8")
u4_text = (DRAFT_DIR / "unit-4.md").read_text(encoding="utf-8")

u3_addon = r"""## 3.9 Demerit Control Charts (Quality Score Rating Systems)

In complex consumer durables and heavy machinery manufacturing (e.g., automobile assembly, commercial aircraft interiors, and medical imaging devices), nonconformities cannot be treated as equally severe. A microscopic paint pinhole (Class D Minor) cannot be treated with the same statistical weight as a defective hydraulic brake fitting (Class A Critical). Counting all defects with equal weight distort process monitoring.

Quality engineering addresses this heterogeneity by establishing **Demerit Control Systems** (also known as Quality Score or Rating charts). Defect types are partitioned into four standardized severity classes:
1. **Class A - Critical**: Completely non-operational, hazardous, or causes catastrophic system failure. Weight: $w_A = 100$.
2. **Class B - Major**: Causes serious operational failure or substantial customer dissatisfaction; requires major field service. Weight: $w_B = 50$.
3. **Class C - Minor**: Minor operational issue or significant cosmetic defect that impairs product marketability. Weight: $w_C = 10$.
4. **Class D - Incidental**: Very minor cosmetic blemish or workmanship imperfection not affecting function. Weight: $w_D = 1$.

### Mathematical Formulation
Let an inspection sample of $n$ units be inspected, and let $C_{iA}, C_{iB}, C_{iC}, C_{iD}$ denote the counts of Class A, B, C, and D defects discovered in subgroup $i$. The total demerit score for the subgroup is:

$$D_i = w_A C_{iA} + w_B C_{iB} + w_C C_{iC} + w_D C_{iD}$$

The demerit score per unit is:

$$u_i = \frac{D_i}{n} = w_A u_{iA} + w_B u_{iB} + w_C u_{iC} + w_D u_{iD}$$

Assuming defect occurrences in each class are independent Poisson random variables with rates $u_A, u_B, u_C, u_D$, the expected demerits per unit and variance are:

$$\bar{u} = \mathbb{E}[u_i] = w_A \bar{u}_A + w_B \bar{u}_B + w_C \bar{u}_C + w_D \bar{u}_D$$

$$\sigma_u^2 = \text{Var}(u_i) = \frac{w_A^2 \bar{u}_A + w_B^2 \bar{u}_B + w_C^2 \bar{u}_C + w_D^2 \bar{u}_D}{n}$$

The $3\sigma$ control limits for the Demerit Chart are:

$$UCL = \bar{u} + 3 \sigma_u, \qquad CL = \bar{u}, \qquad LCL = \max(0, \; \bar{u} - 3 \sigma_u)$$

Demerit charts provide executive leadership and plant directors with a unified, severity-weighted index of manufacturing execution quality.

## 3.10 Zero-Inflated and Clustered Defect Models: Negative Binomial and ZIP

In semiconductor wafer fabrication and advanced additive manufacturing, defects do not distribute uniformly across space. Microscopic airborne particles tend to settle in clusters, violating the independent spatial Poisson assumption:
1. **Compound Poisson / Negative Binomial Model**: If the Poisson parameter $\lambda$ itself fluctuates across wafers according to a Gamma mixing distribution $\lambda \sim \text{Gamma}(\alpha, \beta)$, the marginal distribution of defect count $C$ follows a Negative Binomial distribution:
   $$P(C = c) = \frac{\Gamma(c + r)}{c! \Gamma(r)} \left(\frac{1}{1 + \mu/r}\right)^r \left(\frac{\mu/r}{1 + \mu/r}\right)^c$$
   where $\text{Var}(C) = \mu + \mu^2 / r > \mu$, capturing defect spatial clustering.
2. **Zero-Inflated Poisson (ZIP) Model**: In automated high-precision cleanrooms, a large fraction of wafers are completely defect-free ($C = 0$) due to perfect atmospheric filtration, while occasional vacuum loss produces defects. The ZIP model represents a mixture:
   $$P(C = 0) = \omega + (1 - \omega) e^{-\lambda}$$
   $$P(C = c) = (1 - \omega) \frac{e^{-\lambda} \lambda^c}{c!}, \qquad c = 1, 2, 3, \dots$$
   where $\omega \in [0, 1]$ is the structural zero proportion. Specialized control charts monitor $\omega$ (filtration integrity) and $\lambda$ (contamination intensity) concurrently.
"""

u4_addon = r"""## 4.9 Monitoring Autocorrelated Industrial Processes

A foundational assumption underlying both Shewhart and CUSUM/EWMA control charts is that successive observations $X_1, X_2, \dots, X_t$ are statistically independent. In modern automated manufacturing—such as continuous chemical distillation, petroleum refining, glass sheet floating, and paper mill web rollers—measurements are logged by high-frequency digital sensors every few seconds. Because the physical volume of fluid or thermal mass in the vessel cannot change instantaneously, consecutive measurements exhibit strong positive **autocorrelation** ($\rho_1 = \text{Corr}(X_t, X_{t-1}) > 0$).

### Impact of Autocorrelation on Classical SPC
When positive autocorrelation is present, applying standard Shewhart limits computed from sample variance generates catastrophic false alarm rates:
1. The sample variance $S^2$ severely underestimates the true long-term process variance $\sigma_X^2$:
   $$\mathbb{E}[S^2] = \sigma_X^2 \left( 1 - \frac{2}{n(n-1)} \sum_{k=1}^{n-1} (n - k) \rho_k \right) < \sigma_X^2$$
2. The true variance of the sample mean is inflated:
   $$\text{Var}(\bar{X}) = \frac{\sigma_X^2}{n} \left[ 1 + 2 \sum_{k=1}^{n-1} \left(1 - \frac{k}{n}\right) \rho_k \right] > \frac{\sigma_X^2}{n}$$
3. As a result, the control limits are set artificially too narrow, and the process wanders in smooth serial waves. For an autoregressive process $AR(1)$ with $\rho_1 = 0.70$, the actual in-control ARL collapses from $370$ down to **below 15**! Plant personnel are overwhelmed with continuous false alarms and eventually disable the monitoring software.

### The Residual Control Chart (ARIMA Modeling)
To restore statistical integrity to autocorrelated process monitoring, George Box and T. Luceño (1997) introduced the **Residual Control Chart** (also called the Special Cause Chart, SCC):
1. Fit a time series model (typically an autoregressive integrated moving average model, $\text{ARIMA}(p, d, q)$) to the in-control baseline data:
   $$\Phi(B) (1 - B)^d X_t = \Theta(B) \varepsilon_t$$
2. Compute the one-step-ahead forecasts $\widehat{X}_{t \mid t-1}$ in real time.
3. Compute the one-step-ahead forecast errors (residuals):
   $$e_t = X_t - \widehat{X}_{t \mid t-1}$$
4. Because the ARIMA filter captures all deterministic serial correlation, the residuals $e_t$ are independent and identically distributed Gaussian white noise: $e_t \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma_e^2)$.
5. Plot the residuals $e_t$ on a standard Shewhart, CUSUM, or EWMA control chart with limits:
   $$CL = 0, \qquad \pm 3 \widehat{\sigma}_e$$

An assignable cause in the original physical process manifests as a sudden bias or structural breakdown in the residuals, triggering a statistically valid, uncorrupted alarm.

## 4.10 Nonparametric and Distribution-Free Control Charts

When industrial process data violate normality assumptions and cannot be normalized via mathematical transformations (for instance, multimodal distributions resulting from mixed supply batches, or Cauchy-like heavy-tailed distributions in electronic noise), standard parametric control limits fail. In such environments, quality statisticians deploy **Nonparametric (Distribution-Free) Control Charts**.

### The Shewhart Sign Control Chart
To monitor the median $\widetilde{\mu}$ of an arbitrary continuous distribution without distributional assumptions:
1. In subgroup $i$ of size $n$, count the number of observations strictly exceeding the target median $\widetilde{\mu}_0$:
   $$S_i = \sum_{j=1}^n \mathbb{I}(X_{ij} > \widetilde{\mu}_0)$$
2. Under the in-control null hypothesis, each observation has probability $P(X_{ij} > \widetilde{\mu}_0) = 0.5$, so $S_i \sim \text{Binomial}(n, 0.5)$.
3. Because the distribution of $S_i$ is completely known and independent of the parent continuous distribution $F(x)$, exact symmetric binomial control limits are established.

### The Wilcoxon Signed-Rank and Rank-Sum Charts
To increase statistical power, nonparametric charts incorporate rank magnitude:
- For paired or symmetric continuous data, the **Wilcoxon Signed-Rank Statistic** $W_i$ sums the ranks of absolute deviations $|X_{ij} - \widetilde{\mu}_0|$ with sign indicators.
- For two-sample Phase II monitoring against a Phase I reference sample, the **Mann-Whitney-Wilcoxon Rank-Sum Statistic** combines reference and prospective samples, counting rank inversions.
- Nonparametric CUSUM and EWMA charts replace raw values with standardized rank scores, achieving stable, invariant in-control $ARL_0$ values across any continuous distribution family.
"""

idx3 = u3_text.find("## Fully worked question 1:")
u3_new = u3_text[:idx3] + u3_addon.strip() + "\n\n" + u3_text[idx3:]
(DRAFT_DIR / "unit-3.md").write_text(u3_new, encoding="utf-8")

idx4 = u4_text.find("## Fully worked question 1:")
u4_new = u4_text[:idx4] + u4_addon.strip() + "\n\n" + u4_text[idx4:]
(DRAFT_DIR / "unit-4.md").write_text(u4_new, encoding="utf-8")

print("Units 3 and 4 expanded.")
