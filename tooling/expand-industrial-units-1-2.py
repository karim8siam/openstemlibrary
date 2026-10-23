#!/usr/bin/env python3
"""
Expand Units 1 and 2 for Industrial and Official Statistics.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

u1_text = (DRAFT_DIR / "unit-1.md").read_text(encoding="utf-8")
u2_text = (DRAFT_DIR / "unit-2.md").read_text(encoding="utf-8")

u1_addon = r"""## 1.8 Phase I Retrospective Setup Versus Phase II Operational Monitoring

Statistical process control operates in two methodologically distinct stages: Phase I (retrospective establishment of control) and Phase II (prospective surveillance).

In **Phase I**, the process parameters $\mu_0$ and $\sigma_0$ are completely unknown. The objective is to collect a baseline set of $m$ historical subgroups (typically $m \ge 20$ to $30$, with $n \ge 4$ or $5$) to examine whether the process was historically in control, estimate baseline parameters, and establish definitive trial limits. In Phase I:
1. All $m$ subgroups are plotted against trial limits computed from the entire dataset.
2. If any subgroup statistic plots outside the limits or displays obvious non-random patterns, an exhaustive engineering investigation is conducted to discover whether an assignable cause was active.
3. If an assignable cause is confirmed, the offending subgroup is purged from the baseline, and trial limits are recomputed from the remaining $(m - 1)$ subgroups.
4. This cycle of plotting, investigating, trimming, and recalculating repeats until all remaining points fall strictly inside the limits.

Crucially, in Phase I, successive plotted points are statistically dependent because the estimated limits $\bar{\bar{X}} \pm 3 \bar{R}/(d_2 \sqrt{n})$ are functions of the very sample points being evaluated. Furthermore, parameter estimation error inflates the true false alarm rate in Phase II. If parameters are estimated from too few Phase I subgroups ($m < 20$), the actual in-control ARL can drop from the nominal $370$ to below $150$.

In **Phase II**, the clean, verified control limits established at the conclusion of Phase I are frozen and applied prospectively to monitor future production in real time. Plotted points represent independent future samples, and the classical run-length properties derived under known parameters apply directly.

## 1.9 Economic Design of Control Charts: Duncan's Stochastic Optimization Model

While Shewhart chosen $3\sigma$ control limits based on heuristic balance, A. J. Duncan (1956) formulated the rigorous mathematical economic design of $\bar{X}$ charts. Duncan recognized that designing a control chart requires choosing three decision parameters:
1. The rational subgroup sample size $n$.
2. The inter-sample inspection interval $h$ (in hours).
3. The control limit coefficient $k$ (where limits are $\mu_0 \pm k \sigma / \sqrt{n}$).

Duncan modeled the production cycle as a four-state semi-Markov renewal process:
- **State 0 (In-Control)**: The process operates at $\mu_0$ producing profit per unit time, incurring sampling costs $C_s = (a_1 + a_2 n)/h$, where $a_1$ is fixed cost per sample and $a_2$ is variable cost per inspected unit.
- **Occurrence of Assignable Cause**: The assignable cause arrives according to a Poisson process with arrival rate $\lambda$ (mean time to failure $1/\lambda$).
- **State 1 (Out-of-Control)**: The process shifts to $\mu_1 = \mu_0 \pm \delta \sigma$, generating defect penalty costs at rate $C_d$ per hour until detected.
- **False Alarm State**: When the process is in control, false alarms occur at rate $\alpha / h$, incurring investigation cost $Y$ per false alarm.
- **Detection and Repair**: Once detected (requiring on average $ARL_1 \cdot h$ hours), an investigation and repair cost $W$ is incurred, taking an average repair downtime of $T$ hours.

Duncan derived the expected cost per unit time $E(C)$:

$$E(C) = \frac{a_1 + a_2 n}{h} + \frac{\lambda Y \alpha + \lambda C_d \left( h ARL_1 - \frac{h}{2} + \lambda \frac{h^2}{12} + \tau \right) + \lambda W}{1 + \lambda \left( h ARL_1 - \frac{h}{2} + \tau + T \right)}$$

where $\tau$ is the expected time to take and analyze a sample. By numerically minimizing $E(C)$ with respect to $(n, h, k)$, an industrial engineer determines the economically optimal chart parameters. Remarkably, Duncan showed that for a broad spectrum of manufacturing cost structures, the optimal control limit multiplier $k$ falls between $2.8\sigma$ and $3.2\sigma$, providing profound theoretical justification for Shewhart's empirical $3\sigma$ convention.

## 1.10 Non-Normality and Robust Control Charting

The classical derivations of Shewhart control limits assume that individual measurements $X_{ij}$ are drawn from a Gaussian distribution. Although the Central Limit Theorem ensures that the sample mean $\bar{X}$ approaches normality rapidly as $n$ increases, real industrial processes—such as chemical contaminant concentrations, tool wear measurements, and semiconductor particulate counts—often exhibit pronounced skewness ($\sqrt{\beta_1} \ne 0$) and heavy tails (kurtosis $\beta_2 > 3$).

### Impact of Skewness and Kurtosis
When individual measurements follow a skewed distribution:
1. The distribution of the sample mean $\bar{X}$ retains residual skewness $\gamma_1(\bar{X}) = \sqrt{\beta_1}/\sqrt{n}$. As a result, symmetric $3\sigma$ control limits result in unequal tail probabilities: $\alpha_{\text{upper}} \ne \alpha_{\text{lower}}$, leading to an excessive false alarm rate on the skewed tail and severe loss of power on the opposite tail.
2. The distribution of the sample range $R$ is exceptionally sensitive to non-normality. For heavy-tailed distributions, the expected value $d_2(n)$ shifts upwards, inflating $\bar{R}$ and generating excessively wide limits for the $\bar{X}$ chart.

### Remedial Methodologies
To preserve statistical integrity in non-normal environments:
- **Box-Cox Power Transformations**: Transform non-normal data $X$ via $Y = (X^\lambda - 1)/\lambda$ for $\lambda \ne 0$ (and $Y = \ln X$ for $\lambda = 0$), estimating $\lambda$ via maximum likelihood to achieve near-Gaussian normality before constructing standard Shewhart limits.
- **Johnson System of Distributions**: Fit four-parameter Johnson bounded ($S_B$), unbounded ($S_U$), or lognormal ($S_L$) systems using empirical moments, mapping measurements directly to standard normal variates $Z$.
- **Empirical Probability Limits**: Rather than relying on rigid $3\sigma$ multipliers, compute control limits corresponding to the exact empirical percentiles of the fitted distribution: $LCL = F^{-1}(\alpha/2)$ and $UCL = F^{-1}(1 - \alpha/2)$, with $\alpha = 0.0027$.
"""

u2_addon = r"""## 2.7 Non-Normal Process Capability Analysis: Clements' Pearson Curves

The standard formulations of $C_p$ and $C_{pk}$ assume that the underlying process follows a Gaussian distribution. When process data exhibit significant skewness or kurtosis (for instance, flatness, surface roughness, or cycle times, which are strictly non-negative and inherently right-skewed), applying standard Gaussian formulas produces catastrophic errors: the estimated defect rate can differ from reality by orders of magnitude.

To analyze non-normal processes without distorting original units, John A. Clements (1989) formulated a distribution-free capability methodology based on the **Pearson System of Frequency Curves**. In Clements' method, the natural process spread is defined not by $6\sigma$, but by the difference between the 99.865th percentile and the 0.135th percentile of the true fitted distribution, which matches the coverage of a Gaussian $6\sigma$ span ($99.73\%$):

$$\text{Natural Spread} = X_{0.99865} - X_{0.00135}$$

The **Clements Potential Capability Index** is defined as:

$$C_p^* = \frac{USL - LSL}{X_{0.99865} - X_{0.00135}}$$

To account for centering, Clements defined upper and lower capability ratios referenced to the median ($X_{0.50}$):

$$C_{pu}^* = \frac{USL - X_{0.50}}{X_{0.99865} - X_{0.50}}, \qquad C_{pl}^* = \frac{X_{0.50} - LSL}{X_{0.50} - X_{0.00135}}$$

$$C_{pk}^* = \min(C_{pu}^*, C_{pl}^*)$$

Clements published extensive lookup tables parameterized by the sample skewness $\sqrt{b_1}$ and kurtosis $b_2$, allowing practitioners to determine standardized percentile multipliers without complex numerical integration. Alternatively, modern practitioners apply the Box-Cox or Johnson transformations to normalize the empirical data before evaluating $C_{pk}$ on the transformed scale.

## 2.8 Multivariate Process Capability Indices ($MC_p, MC_{pk}$)

Modern precision assemblies frequently require simultaneous compliance across $p$ correlated geometric or mechanical characteristics $\mathbf{X} = (X_1, X_2, \dots, X_p)^T \sim \mathcal{N}_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. Evaluating unilateral capability indices $C_{pk, j}$ for each dimension independently commits the independence fallacy: even if each individual dimension satisfies $C_{pk} \ge 1.33$, the joint probability that all $p$ dimensions simultaneously fall within their specification region may be unacceptably low due to covariance.

Let the allowable engineering tolerance region be a $p$-dimensional hyper-rectangle:
$$\Omega = \{\mathbf{x} \in \mathbb{R}^p : LSL_j \le x_j \le USL_j, \; j = 1, \dots, p\}$$

Taam, Subbaiah, and Liddy (1993) introduced the **Multivariate Capability Index ($MC_p$)**, defined as the ratio of the volume of the modified tolerance region to the volume of the $99.73\%$ process tolerance ellipse:

$$MC_p = \frac{\text{Vol}(\Omega^*)}{\text{Vol}(\text{Process Ellipse})} = \frac{\prod_{j=1}^p (USL_j - LSL_j)}{|\boldsymbol{\Sigma}|^{1/2} (\pi \chi^2_{p, 0.9973})^{p/2} / \Gamma(p/2 + 1)}$$

To incorporate centering, Taam et al. formulated the **$MC_{pm}$ index**:

$$MC_{pm} = \frac{MC_p}{\sqrt{1 + (\boldsymbol{\mu} - \mathbf{T})^T \boldsymbol{\Sigma}^{-1} (\boldsymbol{\mu} - \mathbf{T})}}$$

where $(\boldsymbol{\mu} - \mathbf{T})^T \boldsymbol{\Sigma}^{-1} (\boldsymbol{\mu} - \mathbf{T})$ is the squared Mahalanobis distance between the operating mean vector $\boldsymbol{\mu}$ and the engineering target vector $\mathbf{T}$. If the process drifts off-target in multivariate space, $MC_{pm}$ declines rapidly, warning engineers of compound assembly interference.

## 2.9 Linearity and Bias Studies in Measurement Systems Evaluation

In addition to repeatability and reproducibility, a complete measurement system evaluation requires evaluating two fundamental properties: **Bias** and **Linearity**.

### Measurement Bias
Bias is the difference between the observed average of measurements and a certified reference standard master value $X_{\text{master}}$:

$$\text{Bias} = \bar{Y} - X_{\text{master}}$$

To statistically verify whether bias is significant, an operator measures the reference standard $m$ times ($m \ge 15$). A one-sample Student $t$-test is performed:

$$t_{\text{stat}} = \frac{|\text{Bias}|}{S / \sqrt{m}}$$

Under the null hypothesis $H_0: \text{Bias} = 0$, $t_{\text{stat}}$ follows a $t$-distribution with $m - 1$ degrees of freedom. If $p < 0.05$, the measurement gage has statistically significant bias, requiring physical recalibration or electronic zero-offset adjustment.

### Measurement Linearity
A measurement device may exhibit zero bias at the midpoint of its operating range, yet display negative bias at the lower end and positive bias at the upper end. **Linearity** assesses whether the measurement bias remains constant across the entire intended operating range of the instrument.

To perform a linearity study:
1. Select $g$ reference parts ($g \ge 5$) whose master values $X_{m, 1} < X_{m, 2} < \dots < X_{m, g}$ span the full operating range of the gage.
2. Measure each part $m$ times ($m \ge 10$), computing the sample mean $\bar{Y}_i$ and observed bias $b_i = \bar{Y}_i - X_{m, i}$ for each reference part.
3. Fit a simple linear regression of bias on master reference value:
   $$b_i = a_0 + a_1 X_{m, i} + \varepsilon_i$$
4. Test the null hypothesis $H_0: a_1 = 0$ (constant bias across operating range). If the slope $a_1$ is statistically significant ($p < 0.05$), the gage exhibits non-linearity.
5. The **Percentage Linearity** is defined as:
   $$\%\text{Linearity} = \frac{|a_1| \times \text{Process Variation}}{\text{Tolerance Band}} \times 100\%$$
   Acceptable industrial metrology standards require $\%\text{Linearity} \le 5\%$.
"""

idx1 = u1_text.find("## Fully worked question 1:")
u1_new = u1_text[:idx1] + u1_addon.strip() + "\n\n" + u1_text[idx1:]
(DRAFT_DIR / "unit-1.md").write_text(u1_new, encoding="utf-8")

idx2 = u2_text.find("## Fully worked question 1:")
u2_new = u2_text[:idx2] + u2_addon.strip() + "\n\n" + u2_text[idx2:]
(DRAFT_DIR / "unit-2.md").write_text(u2_new, encoding="utf-8")

print("Units 1 and 2 expanded successfully.")
