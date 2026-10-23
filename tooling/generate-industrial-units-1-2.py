#!/usr/bin/env python3
"""
Generate Units 1 and 2 for Industrial and Official Statistics.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_1 = r"""# Unit 1: Foundations of Statistical Quality Control & Shewhart Control Charts for Variables

## 1.1 Philosophy and Evolution of Industrial Quality Engineering

The discipline of statistical quality control represents the application of probability theory, sampling distributions, and statistical hypothesis testing to manufacturing operations, service delivery, and supply chain processes. Historically, industrial production relied upon post-manufacturing inspection—a practice colloquially termed "inspecting quality in." In a purely inspectorial paradigm, finished goods are subjected to screening at the terminus of the assembly line, with nonconforming items discarded or routed to rework. As pioneered by Walter A. Shewhart at Bell Telephone Laboratories in the 1920s, and subsequently expanded by W. Edwards Deming and Joseph M. Juran, post-process screening is economically inefficient and fundamentally incapable of preventing defect generation. 

Shewhart recognized that industrial manufacturing is an ongoing, dynamic stochastic system. Every manufacturing process exhibits inherent variation. A stamping press stamping automotive panels, an automated milling machine fabricating titanium turbine blades, or a photolithographic stepper etching nanometer-scale semiconductor wafers does not produce identical outputs over time. Instead, successive parts fluctuate in dimensions, hardness, electrical resistivity, and surface finish. Quality engineering seeks to understand, monitor, and systematically reduce this variability.

W. Edwards Deming formalized this operational philosophy into his Fourteen Points for Management and the Plan-Do-Check-Act (PDCA) cycle, originally conceived by Shewhart. Deming argued that inspection ceases to be necessary when process variation is reduced to the degree where the probability of producing nonconforming output approaches zero. Deming emphasized that management must distinguish between common causes and assignable causes of variation. Confusing common-cause variability with assignable-cause disturbances leads to "tampering"—unjustified adjustments to a stable system that invariably inflate the variance of the output, a mathematical phenomenon demonstrated by Deming's famous Funnel Experiment.

Joseph Juran contributed the Quality Trilogy: quality planning, quality control, and quality improvement. Juran emphasized that quality control maintains a process at its planned level of performance through feedback loops and corrective action, whereas quality improvement achieves breakthrough performance by eliminating chronic sources of variation that had previously been accepted as inevitable operating background.

## 1.2 Common Causes Versus Assignable Causes of Process Variation

A manufacturing process operates under two fundamentally distinct categories of variability:

1. **Common Causes (Chance Causes)**: Common causes represent the inherent, background noise of a well-behaved production system. They arise from a multitude of small, individually unidentifiable disturbances: microscopic fluctuations in raw material composition, infinitesimal variations in machine vibration, ambient room temperature and humidity oscillations, and standard operator reaction times. Common causes are chronic and intrinsic to the machinery, tooling, and environment as currently designed. A process operating exclusively under common causes is said to be in a state of **statistical control** or **predictable stability**. Its output can be modeled as independent and identically distributed (i.i.d.) random variables following a stable probability distribution $F(x; \boldsymbol{\theta})$ over time.

2. **Assignable Causes (Special Causes)**: Assignable causes represent extrinsic, identifiable disruptions that introduce shifts, trends, cycles, or variance inflation into the process distribution. Examples include a broken cutting tool insert, a sudden change in raw material vendor batches, an untrained replacement machine operator, a loose pneumatic clamping fixture, or thermal drift caused by a failed cooling manifold. Assignable causes produce non-random patterns and parametric instability, altering the distribution from $F(x; \boldsymbol{\theta}_0)$ to $F(x; \boldsymbol{\theta}_1)$. 

The primary objective of Statistical Process Control (SPC) is the timely, reliable detection of assignable causes so that operating personnel can intervene, identify the root physical mechanism, and implement corrective measures before extensive volumes of nonconforming product are manufactured.

## 1.3 The Shewhart 3-Sigma Control Chart Principle

Walter Shewhart formulated the control chart as a statistical hypothesis testing mechanism executed sequentially over time. A control chart plots a sample statistic $W_t$ (such as the subgroup sample mean $\bar{X}$, range $R$, standard deviation $S$, or proportion nonconforming $p$) calculated from periodic rational subgroups taken at times $t = 1, 2, 3, \dots$.

A Shewhart control chart consists of three horizontal reference lines:
- **Center Line ($CL$)**: Represents the expected value of the monitored statistic under in-control conditions: $CL = \mathbb{E}[W \mid \text{in-control}]$.
- **Upper Control Limit ($UCL$)**: The threshold above which a sample statistic indicates an out-of-control condition: $UCL = \mathbb{E}[W] + 3 \sigma_W$.
- **Lower Control Limit ($LCL$)**: The threshold below which a sample statistic indicates an out-of-control condition: $LCL = \mathbb{E}[W] - 3 \sigma_W$.

where $\sigma_W$ denotes the standard error of the sample statistic $W$.

Shewhart selected $3\sigma$ limits based on an optimal economic balance between two competing statistical risks:
- **Type I Error ($\alpha$, False Alarm)**: Concluding the process has experienced an assignable cause when it is actually operating stably under common causes.
- **Type II Error ($\beta$, Missed Signal)**: Failing to detect an assignable cause that has shifted or degraded the process distribution.

Under Gaussian distribution assumptions, Chebychev's inequality guarantees that for any probability distribution with finite variance, the probability of exceeding $k$ standard deviations is bounded by $P(|W - \mu_W| \ge k\sigma_W) \le 1/k^2$. For $k = 3$, this upper bound is $1/9 \approx 0.1111$. When $W$ is normally distributed (which holds closely for subgroup means $\bar{X}$ via the Central Limit Theorem), the exact two-sided false alarm probability is:

$$\alpha = P(|Z| > 3) = 2(1 - \Phi(3)) \approx 2(1 - 0.99865) = 0.0027$$

Thus, in an in-control Gaussian process, approximately $2.7$ false alarms occur per $1,000$ plotted subgroups, yielding an in-control Average Run Length of:

$$ARL_0 = \frac{1}{\alpha} = \frac{1}{0.0027} \approx 370.4$$

This indicates that an unshifted process will trigger an erroneous out-of-control signal only once every $370$ inspection intervals on average.

## 1.4 Shewhart $\bar{X}$ and $R$ Control Charts for Rational Subgroups

When the quality characteristic of interest is a continuous variable $X \sim \mathcal{N}(\mu, \sigma^2)$, monitoring both the process location (mean $\mu$) and process dispersion (standard deviation $\sigma$) is mandatory. Rational subgrouping requires taking samples of size $n$ (typically $n = 4$ or $n = 5$) such that variability within a subgroup is driven purely by short-term common causes, while variability between subgroups captures potential assignable causes.

Let $X_{ij}$ denote the $j$-th observation in the $i$-th rational subgroup, where $i = 1, 2, \dots, m$ and $j = 1, 2, \dots, n$. For each subgroup, compute the sample mean $\bar{X}_i$ and sample range $R_i$:

$$\bar{X}_i = \frac{1}{n} \sum_{j=1}^n X_{ij}, \qquad R_i = \max_{1 \le j \le n}(X_{ij}) - \min_{1 \le j \le n}(X_{ij})$$

The overall grand mean $\bar{\bar{X}}$ and average range $\bar{R}$ across $m$ initial baseline subgroups (Phase I) are:

$$\bar{\bar{X}} = \frac{1}{m} \sum_{i=1}^m \bar{X}_i, \qquad \bar{R} = \frac{1}{m} \sum_{i=1}^m R_i$$

### Derivation of Control Factors $d_2$ and $d_3$
In order to estimate the unknown process standard deviation $\sigma$ from the sample ranges, quality theory utilizes the distribution of the relative range $W = R / \sigma$ for a sample of size $n$ from an independent standard normal population $Z_1, \dots, Z_n$.

Let $Z_{(1)} \le Z_{(2)} \le \dots \le Z_{(n)}$ be the order statistics of $n$ independent standard normal variates. The sample range in standardized units is $W = Z_{(n)} - Z_{(1)}$. The expected value of $W$ is defined as the constant $d_2$:

$$d_2(n) = \mathbb{E}[W] = \int_{-\infty}^{\infty} \left[ 1 - (1 - \Phi(w))^n - (\Phi(w))^n \right] dw$$

Similarly, the standard deviation of $W$ is denoted by the constant $d_3(n) = \sqrt{\text{Var}(W)}$. Because $\mathbb{E}[R] = d_2 \sigma$, an unbiased estimator of $\sigma$ is:

$$\widehat{\sigma} = \frac{\bar{R}}{d_2}$$

### Control Limits for the $R$ Chart
The standard error of the range is $\sigma_R = d_3 \sigma = d_3 (\bar{R} / d_2)$. Therefore, the $3\sigma$ control limits for the range chart are:

$$UCL_R = \bar{R} + 3 d_3 \frac{\bar{R}}{d_2} = \bar{R} \left(1 + 3 \frac{d_3}{d_2}\right) = D_4 \bar{R}$$

$$LCL_R = \max\left(0, \; \bar{R} - 3 d_3 \frac{\bar{R}}{d_2}\right) = \max\left(0, \; \bar{R} \left(1 - 3 \frac{d_3}{d_2}\right)\right) = D_3 \bar{R}$$

where the standard factor constants are defined as:
$$D_4 = 1 + 3 \frac{d_3}{d_2}, \qquad D_3 = \max\left(0, \; 1 - 3 \frac{d_3}{d_2}\right)$$
For subgroup sizes $n \le 6$, $D_3 = 0$, meaning the lower control limit on range is zero.

### Control Limits for the $\bar{X}$ Chart
The standard error of the sample mean is $\sigma_{\bar{X}} = \sigma / \sqrt{n} = \bar{R} / (d_2 \sqrt{n})$. Setting $A_2 = 3 / (d_2 \sqrt{n})$, the $3\sigma$ limits are:

$$UCL_{\bar{X}} = \bar{\bar{X}} + 3 \frac{\bar{R}}{d_2 \sqrt{n}} = \bar{\bar{X}} + A_2 \bar{R}$$

$$CL_{\bar{X}} = \bar{\bar{X}}$$

$$LCL_{\bar{X}} = \bar{\bar{X}} - 3 \frac{\bar{R}}{d_2 \sqrt{n}} = \bar{\bar{X}} - A_2 \bar{R}$$

In standard statistical quality engineering practice, the $R$ chart must always be analyzed first. If the process dispersion is out of control, the estimate $\widehat{\sigma} = \bar{R} / d_2$ is invalid, rendering the control limits on the $\bar{X}$ chart unreliable.

## 1.5 Shewhart $\bar{X}$ and $S$ Control Charts for Moderate to Large Subgroups

When subgroup sizes exceed $n = 5$ or $n = 6$, or when individual subgroup sample sizes vary, the sample standard deviation $S$ is mathematically superior to the range $R$. The sample range ignores all intermediate observations between the minimum and maximum, losing statistical efficiency as $n$ grows.

For subgroup $i$, the sample standard deviation is:

$$S_i = \sqrt{\frac{1}{n-1} \sum_{j=1}^n (X_{ij} - \bar{X}_i)^2}$$

Because $S$ is a biased estimator of $\sigma$, quality control introduces the unbiasing constant $c_4(n)$:

$$\mathbb{E}[S] = c_4 \sigma, \qquad c_4(n) = \sqrt{\frac{2}{n-1}} \frac{\Gamma(n/2)}{\Gamma((n-1)/2)}$$

The variance of $S$ is $\text{Var}(S) = \sigma^2 (1 - c_4^2)$. An unbiased pooled estimator of $\sigma$ across $m$ subgroups with average sample standard deviation $\bar{S} = \frac{1}{m} \sum_{i=1}^m S_i$ is $\widehat{\sigma} = \bar{S} / c_4$.

The $3\sigma$ control limits for the $S$ chart are:

$$UCL_S = \bar{S} + 3 \frac{\bar{S}}{c_4} \sqrt{1 - c_4^2} = B_4 \bar{S}$$

$$LCL_S = \max\left(0, \; \bar{S} - 3 \frac{\bar{S}}{c_4} \sqrt{1 - c_4^2}\right) = B_3 \bar{S}$$

where $B_4 = 1 + \frac{3}{c_4}\sqrt{1 - c_4^2}$ and $B_3 = \max\left(0, \; 1 - \frac{3}{c_4}\sqrt{1 - c_4^2}\right)$.

The corresponding limits for the $\bar{X}$ chart using $S$ are:

$$UCL_{\bar{X}} = \bar{\bar{X}} + A_3 \bar{S}, \qquad LCL_{\bar{X}} = \bar{\bar{X}} - A_3 \bar{S}$$

where $A_3 = 3 / (c_4 \sqrt{n})$.

## 1.6 Operating Characteristic (OC) Functions and Average Run Length (ARL)

The operational performance of a control chart is quantified by its **Operating Characteristic (OC)** curve and **Average Run Length (ARL)**. Suppose the process mean shifts from an in-control state $\mu_0$ to an out-of-control state $\mu_1 = \mu_0 + \delta \sigma$, where $\delta = (\mu_1 - \mu_0)/\sigma$ represents the standardized shift magnitude.

The probability of Type II error $\beta$ is the probability that a subgroup sample mean falls within the control limits despite the shift:

$$\beta = P(LCL_{\bar{X}} \le \bar{X} \le UCL_{\bar{X}} \mid \mu = \mu_0 + \delta \sigma)$$

Since $\bar{X} \sim \mathcal{N}\left(\mu_0 + \delta \sigma, \frac{\sigma^2}{n}\right)$, standardizing gives:

$$\beta = \Phi\left( 3 - \delta \sqrt{n} \right) - \Phi\left( -3 - \delta \sqrt{n} \right)$$

For moderate to large positive shifts ($\delta \sqrt{n} \ge 1$), the second term $\Phi(-3 - \delta \sqrt{n})$ is virtually zero, yielding the approximation $\beta \approx \Phi(3 - \delta \sqrt{n})$.

The probability that a subgroup triggers an alarm on a single sample is $p = 1 - \beta$. Assuming successive subgroups are statistically independent, the number of samples $Y$ until the first alarm occurs follows a Geometric distribution:

$$P(Y = y) = \beta^{y-1} (1 - \beta), \qquad y = 1, 2, 3, \dots$$

The expected number of subgroups required to detect the shift is the **Average Run Length ($ARL$)**:

$$ARL_1 = \mathbb{E}[Y] = \frac{1}{1 - \beta} = \frac{1}{p}$$

The **Average Time to Signal ($ATS$)** is given by $ATS = ARL \cdot h$, where $h$ is the sampling interval between successive subgroups in hours.

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Shift Magnitude ($\delta = \Delta\mu / \sigma$)</th>
<th>Subgroup Size $n=4$: $\beta$</th>
<th>Subgroup Size $n=4$: $ARL_1$</th>
<th>Subgroup Size $n=9$: $\beta$</th>
<th>Subgroup Size $n=9$: $ARL_1$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.0 (In-Control)</td>
<td>0.9973</td>
<td>370.4</td>
<td>0.9973</td>
<td>370.4</td>
</tr>
<tr>
<td>0.5</td>
<td>0.9772</td>
<td>43.9</td>
<td>0.9332</td>
<td>15.0</td>
</tr>
<tr>
<td>1.0</td>
<td>0.8413</td>
<td>6.3</td>
<td>0.5000</td>
<td>2.0</td>
</tr>
<tr>
<td>1.5</td>
<td>0.5000</td>
<td>2.0</td>
<td>0.0668</td>
<td>1.07</td>
</tr>
<tr>
<td>2.0</td>
<td>0.1587</td>
<td>1.19</td>
<td>0.00135</td>
<td>1.001</td>
</tr>
<tr>
<td>3.0</td>
<td>0.00135</td>
<td>1.001</td>
<td>0.00000</td>
<td>1.000</td>
</tr>
</tbody>
</table>
</div>

This table illustrates that standard Shewhart charts are exceptionally effective at detecting large shifts ($\delta \ge 2.0$), identifying them within 1 to 2 samples, but are sluggish when detecting small shifts ($\delta \le 1.0$), requiring dozens of samples unless augmented by sensitizing rules or advanced charting techniques like CUSUM and EWMA.

## 1.7 Sensitizing Rules: Western Electric and Nelson Criteria

To enhance the sensitivity of Shewhart charts to small shifts, drift, and systematic patterns without altering the basic chart layout, quality practitioners apply supplementary decision rules. The most renowned are the **Western Electric Rules (WECO)**, which divide each half of the control chart into three equal zones of width $1\sigma$:
- **Zone C**: Center line to $\pm 1\sigma$.
- **Zone B**: $\pm 1\sigma$ to $\pm 2\sigma$.
- **Zone A**: $\pm 2\sigma$ to $\pm 3\sigma$.

An out-of-control condition is declared if any of the following criteria occur:
1. **Rule 1 (Shewhart Rule)**: One point falls beyond Zone A (outside the $3\sigma$ control limits).
2. **Rule 2**: Two out of three consecutive points fall in Zone A or beyond on the same side of the center line.
3. **Rule 3**: Four out of five consecutive points fall in Zone B or beyond on the same side of the center line.
4. **Rule 4 (Run Rule)**: Eight consecutive points fall on the same side of the center line (in Zone C or beyond).

Lloyd Nelson (1984) generalized these into the **Nelson Rules**, adding checks for:
- Six consecutive points steadily increasing or decreasing (evidence of continuous tool wear or heating drift).
- Fourteen consecutive points alternating up and down (evidence of over-control or alternating between two different machines or operators).
- Fifteen consecutive points in Zone C on either side of the center line (evidence of stratification or overly wide control limits caused by mixture sampling).
- Eight consecutive points on both sides of the center line with none in Zone C (evidence of bimodal distributions caused by mixing two distinct tool streams).

While sensitizing rules drastically reduce $ARL_1$ for small shifts, they inevitably inflate the overall false alarm rate $\alpha$, dropping the in-control $ARL_0$ from $370$ down to approximately $91$ when all four Western Electric rules are used simultaneously.

## Fully worked question 1: Establishing Shewhart $\bar{X}$ and $R$ Limits and Phase I Cleanup

### Question
An aerospace precision engineering facility manufactures stainless steel hydraulic control valves. The critical quality dimension is the internal bore diameter, with a target nominal value of $25.000\text{ mm}$. During Phase I setup, an industrial quality engineer collects $m = 25$ rational subgroups of size $n = 5$ parts each from the computerized numerical control (CNC) boring center under normal operating conditions.

The aggregate statistics computed across all $25$ initial subgroups are:
$$\sum_{i=1}^{25} \bar{X}_i = 625.350\text{ mm}, \qquad \sum_{i=1}^{25} R_i = 0.525\text{ mm}$$

Upon reviewing the plotted Phase I control charts, subgroup 14 shows a range of $R_{14} = 0.048\text{ mm}$ and a mean of $\bar{X}_{14} = 25.045\text{ mm}$. An engineering investigation discovers that during subgroup 14, a pneumatic chuck pressure drop allowed workpiece slippage (an identifiable assignable cause).

Perform the following tasks:
1. Determine the factor constants $d_2, d_3, A_2, D_3, D_4$ for subgroup size $n = 5$.
2. Compute the trial control limits for both the $R$ chart and the $\bar{X}$ chart based on the full $25$ subgroups.
3. Confirm whether subgroup 14 falls outside the trial limits.
4. Eliminate subgroup 14 and calculate revised, clean control limits for ongoing Phase II process monitoring.
5. Estimate the underlying in-control process standard deviation $\sigma$ from the revised baseline.

### Solution, step 1: Retrieve factor constants and calculate initial grand averages
For rational subgroup size $n = 5$, the standard ASTM/ASQC control chart factor constants derived from the normal order statistics are:
$$d_2 = 2.326, \qquad d_3 = 0.864$$
$$A_2 = \frac{3}{d_2 \sqrt{n}} = \frac{3}{2.326 \times \sqrt{5}} = \frac{3}{5.2011} \approx 0.577$$
$$D_3 = \max\left(0, 1 - 3\frac{d_3}{d_2}\right) = \max\left(0, 1 - 3 \times \frac{0.864}{2.326}\right) = \max(0, 1 - 1.114) = 0$$
$$D_4 = 1 + 3\frac{d_3}{d_2} = 1 + 1.114 = 2.114$$

Now compute the trial grand mean and trial average range from the $m = 25$ subgroups:
$$\bar{\bar{X}}_{\text{trial}} = \frac{625.350}{25} = 25.0140\text{ mm}$$
$$\bar{R}_{\text{trial}} = \frac{0.525}{25} = 0.0210\text{ mm}$$

### Solution, step 2: Compute trial control limits and audit subgroup 14
First, evaluate the Range chart trial limits:
$$CL_R = \bar{R}_{\text{trial}} = 0.0210\text{ mm}$$
$$UCL_R = D_4 \bar{R}_{\text{trial}} = 2.114 \times 0.0210 = 0.0444\text{ mm}$$
$$LCL_R = D_3 \bar{R}_{\text{trial}} = 0\text{ mm}$$

Next, evaluate the Mean chart trial limits:
$$CL_{\bar{X}} = \bar{\bar{X}}_{\text{trial}} = 25.0140\text{ mm}$$
$$UCL_{\bar{X}} = \bar{\bar{X}}_{\text{trial}} + A_2 \bar{R}_{\text{trial}} = 25.0140 + (0.577 \times 0.0210) = 25.0140 + 0.0121 = 25.0261\text{ mm}$$
$$LCL_{\bar{X}} = \bar{\bar{X}}_{\text{trial}} - A_2 \bar{R}_{\text{trial}} = 25.0140 - 0.0121 = 25.0019\text{ mm}$$

Auditing Subgroup 14:
- The range for subgroup 14 is $R_{14} = 0.048\text{ mm}$. Since $0.048 > UCL_R (0.0444\text{ mm})$, subgroup 14 is out of control on dispersion.
- The mean for subgroup 14 is $\bar{X}_{14} = 25.045\text{ mm}$. Since $25.045 > UCL_{\bar{X}} (25.0261\text{ mm})$, subgroup 14 is also out of control on location.

Because an unambiguous assignable cause (pneumatic chuck pressure drop) was verified, subgroup 14 must be discarded from Phase I baseline calculations.

### Solution, step 3: Revise Phase I baseline and establish Phase II control limits
Recalculate totals across the remaining $m = 24$ subgroups:
$$\sum_{i \ne 14} \bar{X}_i = 625.350 - 25.045 = 600.305\text{ mm}$$
$$\sum_{i \ne 14} R_i = 0.525 - 0.048 = 0.477\text{ mm}$$

The revised baseline grand parameters are:
$$\bar{\bar{X}}_{\text{rev}} = \frac{600.305}{24} = 25.0127\text{ mm}$$
$$\bar{R}_{\text{rev}} = \frac{0.477}{24} = 0.019875\text{ mm} \approx 0.0199\text{ mm}$$

Compute the clean, final Phase II control limits:
- **Revised $R$ Chart**:
  $$CL_R = 0.0199\text{ mm}$$
  $$UCL_R = D_4 \bar{R}_{\text{rev}} = 2.114 \times 0.019875 = 0.0420\text{ mm}$$
  $$LCL_R = 0\text{ mm}$$

- **Revised $\bar{X}$ Chart**:
  $$CL_{\bar{X}} = 25.0127\text{ mm}$$
  $$UCL_{\bar{X}} = 25.0127 + (0.577 \times 0.019875) = 25.0127 + 0.0115 = 25.0242\text{ mm}$$
  $$LCL_{\bar{X}} = 25.0127 - 0.0115 = 25.0012\text{ mm}$$

Finally, estimate the inherent in-control process standard deviation $\sigma$:
$$\widehat{\sigma} = \frac{\bar{R}_{\text{rev}}}{d_2} = \frac{0.019875}{2.326} \approx 0.008545\text{ mm} = 8.545\ \mu\text{m}$$
These revised limits will govern real-time operational monitoring during Phase II production.

## Fully worked question 2: Power and Average Run Length Evaluation for Process Mean Shifts

### Question
A high-volume automated injection molding line produces polymer medical syringe barrels. The critical inner diameter is monitored using a Shewhart $\bar{X}$ chart with rational subgroups of size $n = 4$ inspected every $30\text{ minutes}$ ($h = 0.5\text{ hr}$). The in-control process parameters are $\mu_0 = 12.500\text{ mm}$ and $\sigma = 0.040\text{ mm}$.

Due to an abrupt heater band malfunction, the true process mean shifts upward to $\mu_1 = 12.540\text{ mm}$, while the process standard deviation remains unchanged at $\sigma = 0.040\text{ mm}$.

Calculate:
1. The standardized shift magnitude $\delta = (\mu_1 - \mu_0)/\sigma$.
2. The probability of Type II error $\beta$ on the first subgroup following the shift.
3. The statistical power ($1 - \beta$) of detecting the shift on any given sample.
4. The Average Run Length ($ARL_1$) to detect this shift.
5. The Average Time to Signal ($ATS$) in hours.
6. The probability that the shift is detected by the 3rd subgroup following its occurrence.

### Solution, step 1: Standardize the shift and establish control boundaries
The standardized mean shift $\delta$ is:
$$\delta = \frac{\mu_1 - \mu_0}{\sigma} = \frac{12.540 - 12.500}{0.040} = 1.0$$
The shift is exactly $1.0\sigma$.

The standard error of the subgroup sample mean $\bar{X}$ with $n = 4$ is:
$$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{0.040}{\sqrt{4}} = \frac{0.040}{2} = 0.020\text{ mm}$$

The $3\sigma$ Shewhart control limits are:
$$UCL = \mu_0 + 3 \sigma_{\bar{X}} = 12.500 + 3(0.020) = 12.560\text{ mm}$$
$$LCL = \mu_0 - 3 \sigma_{\bar{X}} = 12.500 - 3(0.020) = 12.440\text{ mm}$$

### Solution, step 2: Calculate Type II error probability $\beta$ and statistical power
Under the shifted process distribution, the sample mean follows $\bar{X} \sim \mathcal{N}\left(\mu_1 = 12.540, \sigma_{\bar{X}}^2 = 0.020^2\right)$.
The probability of failing to signal ($\beta$) is the probability that $\bar{X}$ falls within $[LCL, UCL]$:
$$\beta = P(12.440 \le \bar{X} \le 12.560 \mid \mu = 12.540)$$

Standardizing the endpoints:
$$Z_{\text{upper}} = \frac{UCL - \mu_1}{\sigma_{\bar{X}}} = \frac{12.560 - 12.540}{0.020} = \frac{0.020}{0.020} = +1.00$$
$$Z_{\text{lower}} = \frac{LCL - \mu_1}{\sigma_{\bar{X}}} = \frac{12.440 - 12.540}{0.020} = \frac{-0.100}{0.020} = -5.00$$

Evaluating the cumulative standard normal probabilities:
$$\beta = \Phi(1.00) - \Phi(-5.00) \approx 0.84134 - 0.00000 = 0.84134$$
The probability that a single subgroup fails to signal despite the $1.0\sigma$ shift is approximately $84.13\%$.

The statistical power $p$ (probability of detection on any single sample) is:
$$p = 1 - \beta = 1 - 0.84134 = 0.15866 \approx 15.87\%$$

### Solution, step 3: Determine $ARL_1$, $ATS$, and cumulative detection probability
The Average Run Length ($ARL_1$) under this shift is:
$$ARL_1 = \frac{1}{1 - \beta} = \frac{1}{0.15866} \approx 6.303\text{ subgroups}$$
On average, $6.3$ subgroups must be drawn to catch the shift.

Given a sampling frequency of $h = 0.5\text{ hours}$ (every 30 minutes), the Average Time to Signal is:
$$ATS = ARL_1 \times h = 6.303 \times 0.5 = 3.15\text{ hours}$$
It takes approximately $3$ hours and $9$ minutes of production to detect this $1\sigma$ shift using standard Shewhart limits without sensitizing rules.

Now, compute the probability that the shift is detected on or before the 3rd subgroup ($m \le 3$). 
The complementary probability that the chart fails to detect the shift across all of the first three consecutive subgroups is $\beta^3$:
$$P(\text{Detection by sample 3}) = 1 - \beta^3 = 1 - (0.84134)^3 = 1 - 0.59555 = 0.40445 \approx 40.45\%$$
Thus, there is only a $40.45\%$ chance of catching this shift within the first 90 minutes of production, reinforcing the need for CUSUM or EWMA charts when small shifts have serious financial consequences.

## Fully worked question 3: Constructing $\bar{X}$ and $S$ Control Charts with Variable Subgroup Sizes

### Question
An advanced semiconductor packaging line encapsulates silicon dies in ceramic substrate packages. Subgroup sizes vary from lot to lot due to differing tray capacities:
- Lot 1: $n_1 = 4$, $\bar{X}_1 = 45.2\text{ mil}$, $S_1 = 1.8\text{ mil}$
- Lot 2: $n_2 = 6$, $\bar{X}_2 = 46.1\text{ mil}$, $S_2 = 2.1\text{ mil}$
- Lot 3: $n_3 = 5$, $\bar{X}_3 = 44.8\text{ mil}$, $S_3 = 1.9\text{ mil}$
- Lot 4: $n_4 = 5$, $\bar{X}_4 = 45.6\text{ mil}$, $S_4 = 2.0\text{ mil}$

Perform the following calculations:
1. Calculate the weighted grand mean $\bar{\bar{X}}$ and the pooled sample standard deviation $S_{\text{pooled}}$.
2. Determine the unbiasing constant $c_4(n)$ for sample sizes $n = 4, 5, 6$.
3. Compute the unbiased estimate of the process standard deviation $\sigma$.
4. Calculate individual exact control limits for both the $S$ chart and the $\bar{X}$ chart for Lot 2 ($n_2 = 6$).
5. Assess whether Lot 2 is in statistical control.

### Solution, step 1: Compute weighted grand mean and pooled standard deviation
When subgroup sizes $n_i$ vary, the grand mean is the weighted average of subgroup means:
$$N = \sum_{i=1}^4 n_i = 4 + 6 + 5 + 5 = 20$$
$$\bar{\bar{X}} = \frac{\sum_{i=1}^4 n_i \bar{X}_i}{N} = \frac{4(45.2) + 6(46.1) + 5(44.8) + 5(45.6)}{20}$$
$$\sum n_i \bar{X}_i = 180.8 + 276.6 + 224.0 + 228.0 = 909.4\text{ mil}$$
$$\bar{\bar{X}} = \frac{909.4}{20} = 45.470\text{ mil}$$

The pooled variance weights each sample variance by its degrees of freedom $(n_i - 1)$:
$$S_{\text{pooled}}^2 = \frac{\sum_{i=1}^4 (n_i - 1) S_i^2}{\sum_{i=1}^4 (n_i - 1)} = \frac{(4-1)(1.8)^2 + (6-1)(2.1)^2 + (5-1)(1.9)^2 + (5-1)(2.0)^2}{(3 + 5 + 4 + 4)}$$
Degrees of freedom $= 3 + 5 + 4 + 4 = 16$.
$$\sum (n_i - 1) S_i^2 = 3(3.24) + 5(4.41) + 4(3.61) + 4(4.00) = 9.72 + 22.05 + 14.44 + 16.00 = 62.21$$
$$S_{\text{pooled}}^2 = \frac{62.21}{16} = 3.888125\text{ mil}^2$$
$$S_{\text{pooled}} = \sqrt{3.888125} \approx 1.9718\text{ mil}$$

### Solution, step 2: Determine $c_4$ constants and estimate $\sigma$
Using the formula $c_4(n) = \sqrt{\frac{2}{n-1}}\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}$:
- For $n = 4$: $c_4(4) = \sqrt{2/3} \frac{\Gamma(2)}{\Gamma(1.5)} = \sqrt{0.6667} \frac{1}{0.88623} \approx 0.9213$
- For $n = 5$: $c_4(5) = \sqrt{2/4} \frac{\Gamma(2.5)}{\Gamma(2)} = \sqrt{0.5} \times 1.3293 \approx 0.9400$
- For $n = 6$: $c_4(6) = \sqrt{2/5} \frac{\Gamma(3)}{\Gamma(2.5)} = \sqrt{0.4} \frac{2}{1.3293} \approx 0.9515$

For the pooled estimate with total degrees of freedom $df = 16$, the effective sample size is $n_{\text{eff}} = df + 1 = 17$:
$$c_4(17) \approx 1 - \frac{1}{4(16)} = 1 - \frac{1}{64} \approx 0.9844$$
The unbiased estimate of the process standard deviation is:
$$\widehat{\sigma} = \frac{S_{\text{pooled}}}{c_4(17)} = \frac{1.9718}{0.9844} \approx 2.003\text{ mil}$$

### Solution, step 3: Establish exact control limits for Lot 2 ($n_2 = 6$) and evaluate control status
For Lot 2 with $n_2 = 6$, $c_4(6) = 0.9515$:

1. **Exact $S$ Chart limits for $n_2 = 6$**:
   $$\mathbb{E}[S \mid n=6] = c_4(6) \widehat{\sigma} = 0.9515 \times 2.003 = 1.9059\text{ mil}$$
   $$\sigma_S(6) = \widehat{\sigma} \sqrt{1 - c_4(6)^2} = 2.003 \times \sqrt{1 - (0.9515)^2} = 2.003 \times \sqrt{1 - 0.90535} = 2.003 \times 0.30765 \approx 0.6162\text{ mil}$$
   $$UCL_S = \mathbb{E}[S] + 3 \sigma_S = 1.9059 + 3(0.6162) = 1.9059 + 1.8486 = 3.7545\text{ mil}$$
   $$LCL_S = \max(0, \mathbb{E}[S] - 3 \sigma_S) = \max(0, 1.9059 - 1.8486) = 0.0573\text{ mil}$$

2. **Exact $\bar{X}$ Chart limits for $n_2 = 6$**:
   $$\sigma_{\bar{X}}(6) = \frac{\widehat{\sigma}}{\sqrt{6}} = \frac{2.003}{2.4495} \approx 0.8177\text{ mil}$$
   $$CL = \bar{\bar{X}} = 45.470\text{ mil}$$
   $$UCL_{\bar{X}} = \bar{\bar{X}} + 3 \sigma_{\bar{X}} = 45.470 + 3(0.8177) = 45.470 + 2.453 = 47.923\text{ mil}$$
   $$LCL_{\bar{X}} = \bar{\bar{X}} - 3 \sigma_{\bar{X}} = 45.470 - 2.453 = 43.017\text{ mil}$$

3. **Audit Lot 2**:
   - Lot 2 observed standard deviation: $S_2 = 2.1\text{ mil}$. Since $0.0573 \le 2.1 \le 3.7545$, the dispersion is in control.
   - Lot 2 observed mean: $\bar{X}_2 = 46.1\text{ mil}$. Since $43.017 \le 46.1 \le 47.923$, the mean is in control.
   
Therefore, Lot 2 is fully in statistical control under exact individual sample size limits.
"""

unit_2 = r"""# Unit 2: Process Capability Analysis, Tolerance Synthesis & Measurement Systems Evaluation

## 2.1 Control Limits Versus Engineering Specification Tolerances

A foundational distinction in industrial quality engineering separates the statistical voice of the process from the engineering voice of the customer:
- **Control Limits ($LCL, UCL$)**: Derived exclusively from the inherent variability of the manufacturing process ($\mu \pm 3\sigma/\sqrt{n}$). They reflect what the process *is actually achieving* when operating stably under common causes.
- **Specification Limits ($LSL, USL$)**: Established by product designers, systems architects, and customer functional requirements. They reflect what the manufactured part *must achieve* to assemble properly, withstand operational stress, and prevent operational failure.

There is no necessary mathematical connection between control limits and specification tolerances. A process can be in perfect statistical control (highly stable and predictable) yet produce $100\%$ nonconforming scrap if its natural variation exceeds the allowable tolerance spread or if its operating mean is severely off-center. Conversely, an out-of-control process might temporarily produce parts that happen to fall within specifications, but its unpredictability poses severe long-term risk. **Process Capability Analysis** quantitatively bridges this gap, evaluating whether the natural distribution of a stable process fits comfortably within the engineering tolerance boundaries.

## 2.2 Potential Process Capability: The $C_p$ Index

Assume a continuous quality characteristic $X$ is generated by an in-control manufacturing process following a normal distribution $X \sim \mathcal{N}(\mu, \sigma^2)$, with Lower Specification Limit ($LSL$) and Upper Specification Limit ($USL$). 

The total allowable engineering tolerance width is:
$$\text{Tolerance Band} = USL - LSL$$

The natural process capability spread is defined by Shewhart's $6\sigma$ envelope (from $\mu - 3\sigma$ to $\mu + 3\sigma$), encompassing $99.73\%$ of output under normality. The **Potential Process Capability Index ($C_p$)** is defined as the ratio of allowable tolerance to natural process spread:

$$C_p = \frac{USL - LSL}{6\sigma}$$

### Interpretation of $C_p$
- **$C_p < 1.0$ (Incapable Process)**: The natural process spread is wider than the tolerance band ($6\sigma > USL - LSL$). Even if the process is centered perfectly at the nominal midpoint $M = (USL + LSL)/2$, a substantial fraction of parts will inevitably breach specification limits, generating defective product.
- **$C_p = 1.0$ (Barely Capable Process)**: The $6\sigma$ spread exactly equals the tolerance bandwidth. When perfectly centered, the expected nonconforming fraction is $0.27\%$ ($2,700$ parts per million, PPM). Any slight disturbance in process mean immediately produces scrap.
- **$C_p = 1.33$ (Capable Process, 4-Sigma Quality)**: The tolerance band spans $8\sigma$. When centered, the defect rate is $63\text{ PPM}$. This is the traditional industrial benchmark for established manufacturing processes.
- **$C_p \ge 1.67$ (Highly Capable, 5-Sigma Quality)**: The tolerance band spans $10\sigma$, with a centered defect rate of $0.57\text{ PPM}$. Required for critical safety components in aerospace and medical technology.
- **$C_p \ge 2.0$ (World-Class, Six Sigma Quality)**: The tolerance band spans $12\sigma$. Even under a sustained $1.5\sigma$ mean drift, the process produces no more than $3.4\text{ PPM}$ nonconforming output.

Notice that $C_p$ evaluates only the process *spread* relative to tolerance; it provides zero information regarding whether the process is actually *centered* between $LSL$ and $USL$.

## 2.3 Actual Process Capability: The $C_{pk}$ Index

To penalize process off-centering, quality engineering defines unilateral capability ratios for the upper and lower specification limits:

$$C_{pu} = \frac{USL - \mu}{3\sigma}, \qquad C_{pl} = \frac{\mu - LSL}{3\sigma}$$

The **Actual Process Capability Index ($C_{pk}$)** is the minimum of these two one-sided ratios:

$$C_{pk} = \min(C_{pu}, C_{pl}) = \min\left( \frac{USL - \mu}{3\sigma}, \; \frac{\mu - LSL}{3\sigma} \right)$$

Algebraically, $C_{pk}$ can be related directly to $C_p$ via the centering parameter $k$:

$$k = \frac{|\mu - M|}{(USL - LSL)/2}, \qquad M = \frac{USL + LSL}{2}$$

where $k \in [0, 1]$ represents the fractional deviation of the mean from nominal midpoint. Then:

$$C_{pk} = C_p (1 - k)$$

### Key Properties of $C_{pk}$
1. If the process is perfectly centered ($\mu = M$), then $k = 0$, and $C_{pk} = C_p$.
2. As the process mean shifts away from center, $k$ increases, causing $C_{pk}$ to decrease monotonically while $C_p$ remains constant.
3. If the process mean shifts exactly onto one of the specification limits ($\mu = USL$ or $\mu = LSL$), $C_{pk} = 0$, indicating that $50\%$ of production is defective.
4. If the process mean shifts outside the specification limits, $C_{pk} < 0$.
5. The actual fraction of nonconforming product produced by the process is given by:
   $$p = P(X < LSL) + P(X > USL) = \Phi\left( -\frac{\mu - LSL}{\sigma} \right) + \Phi\left( -\frac{USL - \mu}{\sigma} \right) = \Phi(-3 C_{pl}) + \Phi(-3 C_{pu})$$
   A common upper bound on the nonconforming fraction is $p \le 2\Phi(-3 C_{pk})$.

## 2.4 Taguchi Capability Index: $C_{pm}$ and Quadratic Quality Loss

Genichi Taguchi challenged the traditional "goal-post" mentality of specification limits. The goal-post philosophy assumes that a product dimension falling just inside specification ($USL - \epsilon$) incurs zero loss, whereas a dimension falling just outside ($USL + \epsilon$) incurs immediate catastrophic loss. Taguchi demonstrated that customer dissatisfaction and economic cost accumulate continuously as a quadratic function of deviation from the design target $T$:

$$L(X) = k_T (X - T)^2$$

where $k_T$ is a financial loss coefficient. The expected quality loss per unit manufactured is:

$$\mathbb{E}[L(X)] = k_T \mathbb{E}[(X - T)^2] = k_T \left[ \sigma^2 + (\mu - T)^2 \right]$$

Taguchi introduced the **$C_{pm}$ Index** (also known as the Taguchi Capability Index), which incorporates the mean square deviation from the design target $T$:

$$C_{pm} = \frac{USL - LSL}{6 \tau}, \qquad \tau = \sqrt{\mathbb{E}[(X - T)^2]} = \sqrt{\sigma^2 + (\mu - T)^2}$$

Notice that $\tau$ reflects both process variance $\sigma^2$ and off-target bias $(\mu - T)^2$. We can rewrite $C_{pm}$ in terms of $C_p$:

$$C_{pm} = \frac{C_p}{\sqrt{1 + \left(\frac{\mu - T}{\sigma}\right)^2}} = \frac{C_p}{\sqrt{1 + \xi^2}}$$

where $\xi = (\mu - T)/\sigma$ is the standardized target discrepancy. If the process mean is centered exactly on target ($\mu = T$), then $C_{pm} = C_p$. If the process mean drifts away from target, $C_{pm}$ drops rapidly, penalizing the departure even if the process remains comfortably within traditional specification tolerances.

## 2.5 Sampling Distributions and Confidence Intervals for Capability Indices

In empirical industrial practice, true parameters $\mu$ and $\sigma$ are unknown and must be estimated from a random sample of $N$ parts, yielding sample estimators:

$$\widehat{C}_p = \frac{USL - LSL}{6 S}, \qquad \widehat{C}_{pk} = \min\left( \frac{USL - \bar{X}}{3S}, \; \frac{\bar{X} - LSL}{3S} \right)$$

Because $\widehat{C}_p$ and $\widehat{C}_{pk}$ are sample statistics, they exhibit sampling variability. Making operational decisions based solely on point estimates without confidence intervals introduces substantial commercial risk.

### Sampling Distribution of $\widehat{C}_p$
Recall that for a normal sample of size $N$, $(N - 1)S^2 / \sigma^2 \sim \chi^2_{N-1}$. Therefore:

$$\frac{\widehat{C}_p}{C_p} = \frac{\sigma}{S} = \sqrt{\frac{N - 1}{(N - 1)S^2/\sigma^2}} \sim \sqrt{\frac{N - 1}{\chi^2_{N-1}}}$$

Thus, $(N - 1)(\widehat{C}_p / C_p)^2$ follows an inverted chi-square distribution. A $(1 - \alpha)100\%$ confidence interval for the true potential capability $C_p$ is:

$$\widehat{C}_p \sqrt{\frac{\chi^2_{\alpha/2, N-1}}{N - 1}} \le C_p \le \widehat{C}_p \sqrt{\frac{\chi^2_{1-\alpha/2, N-1}}{N - 1}}$$

### Asymptotic Distribution and Confidence Interval for $\widehat{C}_{pk}$
Zhang, Stenback, and Wardrop (1990) derived the large-sample asymptotic variance of $\widehat{C}_{pk}$:

$$\text{Var}(\widehat{C}_{pk}) \approx \frac{1}{9N} + \frac{\widehat{C}_{pk}^2}{2(N - 1)}$$

An approximate $(1 - \alpha)100\%$ confidence interval for $C_{pk}$ is:

$$\widehat{C}_{pk} \pm Z_{\alpha/2} \sqrt{\frac{1}{9N} + \frac{\widehat{C}_{pk}^2}{2(N - 1)}}$$

This formula reveals why small sample sizes (such as $N = 30$) yield excessively wide confidence intervals, frequently causing engineers to overestimate true process capability.

## 2.6 Measurement Systems Analysis: Gage Repeatability and Reproducibility (Gage R&R)

Before process capability can be meaningfully assessed, the measurement system itself must be validated. If the calipers, coordinate measuring machines (CMM), optical comparators, or sensors exhibit substantial measurement noise, the observed process variance will be artificially inflated:

$$\sigma^2_{\text{total}} = \sigma^2_{\text{part}} + \sigma^2_{\text{measurement}}$$

The variance of the measurement system $\sigma^2_{\text{measurement}}$ (commonly termed Gage R&R, $\sigma^2_{GRR}$) is partitioned into two orthogonal components:
1. **Repeatability ($\sigma^2_{\text{repeatability}}$, Equipment Variation, $EV$)**: The variability observed when one operator measures the exact same part multiple times using the identical measurement instrument.
2. **Reproducibility ($\sigma^2_{\text{reproducibility}}$, Appraiser Variation, $AV$)**: The variability observed when different operators measure the exact same part using the identical measurement instrument.

$$\sigma^2_{GRR} = \sigma^2_{\text{repeatability}} + \sigma^2_{\text{reproducibility}} = \sigma^2_{EV} + \sigma^2_{AV}$$

### ANOVA Method for Gage R&R
In a standard crossed Gage R&R study, $p$ parts are selected at random from the production process, $o$ operators are assigned, and each operator measures every part $r$ times (replicates). The total number of observations is $N = p \cdot o \cdot r$.

The two-factor crossed random effects model is:

$$Y_{ijk} = \mu + P_i + O_j + (PO)_{ij} + \varepsilon_{ijk}$$

where $P_i \sim \mathcal{N}(0, \sigma^2_P)$ is the random part effect, $O_j \sim \mathcal{N}(0, \sigma^2_O)$ is the random operator effect, $(PO)_{ij} \sim \mathcal{N}(0, \sigma^2_{PO})$ is the part-by-operator interaction, and $\varepsilon_{ijk} \sim \mathcal{N}(0, \sigma^2_{\varepsilon})$ is the experimental measurement error.

From the two-way ANOVA table:
- **Repeatability Variance**: $\widehat{\sigma}^2_{\text{repeatability}} = MS_E$
- **Part-by-Operator Interaction**: $\widehat{\sigma}^2_{PO} = \frac{MS_{PO} - MS_E}{r}$
- **Operator Reproducibility**: $\widehat{\sigma}^2_O = \frac{MS_O - MS_{PO}}{p \cdot r}$
- **Gage Reproducibility**: $\widehat{\sigma}^2_{\text{reproducibility}} = \widehat{\sigma}^2_O + \widehat{\sigma}^2_{PO}$
- **Total Measurement System Variance**: $\widehat{\sigma}^2_{GRR} = \widehat{\sigma}^2_{\text{repeatability}} + \widehat{\sigma}^2_{\text{reproducibility}}$
- **Part-to-Part Variance**: $\widehat{\sigma}^2_{\text{part}} = \frac{MS_P - MS_{PO}}{o \cdot r}$

### Measurement System Evaluation Metrics
The Automotive Industry Action Group (AIAG) defines three primary metrics:

1. **Precision-to-Tolerance Ratio ($P/T$)**:
   $$P/T = \frac{6 \sigma_{GRR}}{USL - LSL} \times 100\%$$
2. **Percentage of Total Process Variation ($\%GRR$)**:
   $$\%GRR = \frac{\sigma_{GRR}}{\sigma_{\text{total}}} \times 100\%$$
3. **Number of Distinct Categories ($ndc$)**:
   $$ndc = \left\lfloor 1.41 \frac{\sigma_{\text{part}}}{\sigma_{GRR}} \right\rfloor$$

### Acceptance Criteria
- $P/T$ or $\%GRR < 10\%$: Measurement system is excellent and universally acceptable.
- $10\% \le P/T \le 30\%$: Measurement system is conditionally acceptable depending on application criticality and replacement cost.
- $P/T > 30\%$: Measurement system is unacceptable; calibration, fixturing, or instrument replacement is mandatory.
- $ndc \ge 5$: The measurement system possesses adequate statistical resolution to discriminate between parts.

## Fully worked question 1: Comprehensive Process Capability Evaluation ($C_p, C_{pk}, C_{pm}$) and Defect Rate

### Question
A specialized microelectronics fabrication facility produces precision thin-film resistors. The technical specification for resistance is $100.0 \pm 6.0\ \Omega$ (thus $LSL = 94.0\ \Omega$, $USL = 106.0\ \Omega$, and nominal target $T = 100.0\ \Omega$).

A continuous monitoring audit of $N = 100$ resistors from a stable manufacturing line yields a sample mean of $\bar{X} = 101.5\ \Omega$ and a sample standard deviation of $S = 1.25\ \Omega$.

Perform the following analyses:
1. Calculate the point estimates for potential capability $\widehat{C}_p$ and actual capability $\widehat{C}_{pk}$.
2. Calculate the centering parameter $k$.
3. Calculate the Taguchi capability index $\widehat{C}_{pm}$.
4. Compute the expected nonconforming fraction (in PPM) under the current operating conditions.
5. If operating personnel retune the process centering so that $\bar{X} = 100.0\ \Omega$ with variance unchanged, determine the new $\widehat{C}_{pk}$, $\widehat{C}_{pm}$, and the revised PPM defect rate.

### Solution, step 1: Compute $\widehat{C}_p$ and $\widehat{C}_{pk}$
The specification bandwidth is $USL - LSL = 106.0 - 94.0 = 12.0\ \Omega$.
The nominal midpoint is $M = (94.0 + 106.0)/2 = 100.0\ \Omega$.

1. **Potential Capability Index $\widehat{C}_p$**:
   $$\widehat{C}_p = \frac{USL - LSL}{6S} = \frac{12.0}{6 \times 1.25} = \frac{12.0}{7.50} = 1.600$$

2. **Actual Capability Index $\widehat{C}_{pk}$**:
   $$\widehat{C}_{pu} = \frac{USL - \bar{X}}{3S} = \frac{106.0 - 101.5}{3 \times 1.25} = \frac{4.5}{3.75} = 1.200$$
   $$\widehat{C}_{pl} = \frac{\bar{X} - LSL}{3S} = \frac{101.5 - 94.0}{3 \times 1.25} = \frac{7.5}{3.75} = 2.000$$
   $$\widehat{C}_{pk} = \min(\widehat{C}_{pu}, \widehat{C}_{pl}) = \min(1.200, 2.000) = 1.200$$

### Solution, step 2: Calculate centering parameter $k$ and Taguchi capability $\widehat{C}_{pm}$
The centering coefficient $k$ is:
$$k = \frac{|\bar{X} - M|}{(USL - LSL)/2} = \frac{|101.5 - 100.0|}{6.0} = \frac{1.5}{6.0} = 0.250$$
Verifying relationship:
$$\widehat{C}_{pk} = \widehat{C}_p (1 - k) = 1.600 \times (1 - 0.250) = 1.600 \times 0.750 = 1.200$$

For the Taguchi index $\widehat{C}_{pm}$:
$$\widehat{\tau} = \sqrt{S^2 + (\bar{X} - T)^2} = \sqrt{1.25^2 + (101.5 - 100.0)^2} = \sqrt{1.5625 + 2.25} = \sqrt{3.8125} \approx 1.95256\ \Omega$$
$$\widehat{C}_{pm} = \frac{USL - LSL}{6 \widehat{\tau}} = \frac{12.0}{6 \times 1.95256} = \frac{12.0}{11.7154} \approx 1.024$$
Alternatively, via the discrepancy formula:
$$\xi = \frac{\bar{X} - T}{S} = \frac{1.5}{1.25} = 1.20$$
$$\widehat{C}_{pm} = \frac{\widehat{C}_p}{\sqrt{1 + \xi^2}} = \frac{1.600}{\sqrt{1 + 1.20^2}} = \frac{1.600}{\sqrt{1 + 1.44}} = \frac{1.600}{\sqrt{2.44}} = \frac{1.600}{1.56205} \approx 1.024$$

### Solution, step 3: Calculate defect rates and assess centering adjustment
1. **Current Defect Rate**:
   - Defective above $USL$:
     $$Z_{\text{upper}} = \frac{USL - \bar{X}}{S} = \frac{106.0 - 101.5}{1.25} = \frac{4.5}{1.25} = 3.60$$
     $$P(X > USL) = 1 - \Phi(3.60) \approx 0.0001591 = 159.1\text{ PPM}$$
   - Defective below $LSL$:
     $$Z_{\text{lower}} = \frac{LSL - \bar{X}}{S} = \frac{94.0 - 101.5}{1.25} = \frac{-7.5}{1.25} = -6.00$$
     $$P(X < LSL) = \Phi(-6.00) \approx 9.87 \times 10^{-10} \approx 0.000\text{ PPM}$$
   - Total current defect rate $= 159.1\text{ PPM}$.

2. **Adjusted Process ($\bar{X} = 100.0\ \Omega, S = 1.25\ \Omega$)**:
   Since $\bar{X} = M = T = 100.0\ \Omega$:
   $$k = 0 \implies \widehat{C}_{pk} = \widehat{C}_p = 1.600$$
   $$\xi = 0 \implies \widehat{C}_{pm} = \widehat{C}_p = 1.600$$
   The standard score for both limits is:
   $$Z = \frac{106.0 - 100.0}{1.25} = \frac{6.0}{1.25} = 4.80$$
   The two-sided defect rate is:
   $$p_{\text{new}} = 2 \times (1 - \Phi(4.80)) \approx 2 \times (7.93 \times 10^{-7}) = 1.586 \times 10^{-6} \approx 1.59\text{ PPM}$$

Recentering the process reduces the defect rate from $159.1\text{ PPM}$ down to $1.59\text{ PPM}$—a 100-fold quality improvement achieved purely by centering without requiring expensive machine upgrades!

## Fully worked question 2: Statistical Inference and Confidence Intervals for $C_p$ and $C_{pk}$

### Question
An automotive transmission component manufacturer must certify to an original equipment manufacturer (OEM) that a gear hobbing process satisfies $C_p \ge 1.33$ and $C_{pk} \ge 1.33$ at a $95\%$ confidence level. The engineering specifications for spline tooth thickness are $LSL = 15.20\text{ mm}$ and $USL = 15.80\text{ mm}$.

A validation sample of $N = 50$ gears is randomly sampled from a confirmed stable production run, yielding:
$$\bar{X} = 15.54\text{ mm}, \qquad S = 0.068\text{ mm}$$

Perform the following statistical evaluations:
1. Compute the point estimates $\widehat{C}_p$ and $\widehat{C}_{pk}$.
2. Construct an exact two-sided $95\%$ confidence interval for the true population capability $C_p$ (given $\chi^2_{0.025, 49} = 31.555$ and $\chi^2_{0.975, 49} = 70.222$).
3. Construct an approximate large-sample two-sided $95\%$ confidence interval for the true population capability $C_{pk}$.
4. State whether the manufacturer can legally certify with $95\%$ statistical confidence that the process meets the OEM standard ($C_{pk} \ge 1.33$).

### Solution, step 1: Calculate sample capability point estimates
The engineering tolerance bandwidth is $USL - LSL = 15.80 - 15.20 = 0.60\text{ mm}$.
The nominal midpoint is $M = (15.20 + 15.80)/2 = 15.50\text{ mm}$.

1. **Potential Capability $\widehat{C}_p$**:
   $$\widehat{C}_p = \frac{0.60}{6 \times 0.068} = \frac{0.60}{0.408} \approx 1.4706$$

2. **Actual Capability $\widehat{C}_{pk}$**:
   $$\widehat{C}_{pu} = \frac{USL - \bar{X}}{3S} = \frac{15.80 - 15.54}{3 \times 0.068} = \frac{0.26}{0.204} \approx 1.2745$$
   $$\widehat{C}_{pl} = \frac{\bar{X} - LSL}{3S} = \frac{15.54 - 15.20}{3 \times 0.068} = \frac{0.34}{0.204} \approx 1.6667$$
   $$\widehat{C}_{pk} = \min(1.2745, 1.6667) = 1.2745$$

### Solution, step 2: Construct exact $95\%$ confidence interval for $C_p$
For $N = 50$, degrees of freedom $df = 49$. The critical values are $\chi^2_{0.025, 49} = 31.555$ and $\chi^2_{0.975, 49} = 70.222$.
The exact confidence interval is:
$$\widehat{C}_p \sqrt{\frac{\chi^2_{0.025, 49}}{49}} \le C_p \le \widehat{C}_p \sqrt{\frac{\chi^2_{0.975, 49}}{49}}$$
Substitute $\widehat{C}_p = 1.4706$:
$$\text{Lower Limit} = 1.4706 \times \sqrt{\frac{31.555}{49}} = 1.4706 \times \sqrt{0.64398} = 1.4706 \times 0.80248 \approx 1.180$$
$$\text{Upper Limit} = 1.4706 \times \sqrt{\frac{70.222}{49}} = 1.4706 \times \sqrt{1.43310} = 1.4706 \times 1.19712 \approx 1.760$$
Thus, the $95\%$ confidence interval for $C_p$ is:
$$1.180 \le C_p \le 1.760$$

### Solution, step 3: Construct $95\%$ confidence interval for $C_{pk}$ and evaluate certification
Using the large-sample asymptotic standard error formula:
$$SE(\widehat{C}_{pk}) = \sqrt{\frac{1}{9N} + \frac{\widehat{C}_{pk}^2}{2(N - 1)}} = \sqrt{\frac{1}{9(50)} + \frac{(1.2745)^2}{2(49)}}$$
$$SE(\widehat{C}_{pk}) = \sqrt{\frac{1}{450} + \frac{1.62435}{98}} = \sqrt{0.002222 + 0.016575} = \sqrt{0.018797} \approx 0.1371$$

For a $95\%$ two-sided confidence interval, $Z_{0.025} = 1.960$:
$$\text{Margin of Error} = 1.960 \times 0.1371 \approx 0.2687$$
$$\text{Lower Limit} = 1.2745 - 0.2687 = 1.0058 \approx 1.006$$
$$\text{Upper Limit} = 1.2745 + 0.2687 = 1.5432 \approx 1.543$$
Thus, the $95\%$ confidence interval for $C_{pk}$ is:
$$1.006 \le C_{pk} \le 1.543$$

**Certification Decision**:
Even though the sample point estimate for potential capability exceeds the threshold ($\widehat{C}_p = 1.47 > 1.33$), the sample point estimate for actual capability is already below target ($\widehat{C}_{pk} = 1.27 < 1.33$). Furthermore, the lower bound of the $95\%$ confidence interval for $C_{pk}$ is $1.006$, substantially below the required benchmark of $1.33$. 
Therefore, the manufacturer cannot certify the process to the OEM. The process requires recentering towards $15.50\text{ mm}$ to raise $C_{pk}$, followed by re-sampling.

## Fully worked question 3: Analysis of Variance (ANOVA) Formulation for Crossed Gage R&R

### Question
An optical sensor manufacturing facility executes a crossed Gage R&R study to validate a vision inspection system measuring micro-lens focal length. The engineering tolerance bandwidth is $USL - LSL = 0.500\text{ mm}$.

The study employs:
- $p = 10$ randomly sampled micro-lenses
- $o = 3$ certified metrology technicians (operators)
- $r = 2$ trial replications per operator-part combination
Total number of measurement trials is $N = 10 \times 3 \times 2 = 60$.

The two-factor crossed ANOVA on the measurement data yields the following Sum of Squares:
- Total Sum of Squares: $SS_{\text{Total}} = 1.8450$
- Parts Sum of Squares: $SS_{\text{Parts}} = 1.6200$
- Operators Sum of Squares: $SS_{\text{Operators}} = 0.0540$
- Part $\times$ Operator Interaction Sum of Squares: $SS_{PO} = 0.0720$
- Equipment Measurement Error (Residual) Sum of Squares: $SS_E = 0.0990$

Calculate:
1. The degrees of freedom and Mean Squares ($MS$) for all ANOVA terms.
2. The variance components: $\widehat{\sigma}^2_{\text{repeatability}}$, $\widehat{\sigma}^2_{\text{reproducibility}}$, $\widehat{\sigma}^2_{GRR}$, and $\widehat{\sigma}^2_{\text{part}}$.
3. The total observed variation standard deviation $\widehat{\sigma}_{\text{total}}$.
4. The Precision-to-Tolerance ratio ($P/T\%$).
5. The percentage of total process variation attributable to Gage R&R ($\%GRR$).
6. The number of distinct categories ($ndc$).
7. Assess whether this measurement system is acceptable for production inspection.

### Solution, step 1: Construct the ANOVA table
The degrees of freedom are:
- $df_{\text{Parts}} = p - 1 = 10 - 1 = 9$
- $df_{\text{Operators}} = o - 1 = 3 - 1 = 2$
- $df_{PO} = (p - 1)(o - 1) = 9 \times 2 = 18$
- $df_E = p \cdot o \cdot (r - 1) = 10 \times 3 \times (2 - 1) = 30$
- $df_{\text{Total}} = N - 1 = 60 - 1 = 59$

Now compute Mean Squares ($MS = SS / df$):
- $MS_P = \frac{SS_{\text{Parts}}}{9} = \frac{1.6200}{9} = 0.18000$
- $MS_O = \frac{SS_{\text{Operators}}}{2} = \frac{0.0540}{2} = 0.02700$
- $MS_{PO} = \frac{SS_{PO}}{18} = \frac{0.0720}{18} = 0.00400$
- $MS_E = \frac{SS_E}{30} = \frac{0.0990}{30} = 0.00330$

### Solution, step 2: Extract variance components
1. **Repeatability (Equipment Variation)**:
   $$\widehat{\sigma}^2_{\text{repeatability}} = MS_E = 0.00330\text{ mm}^2$$

2. **Part $\times$ Operator Interaction**:
   $$\widehat{\sigma}^2_{PO} = \max\left(0, \; \frac{MS_{PO} - MS_E}{r}\right) = \frac{0.00400 - 0.00330}{2} = \frac{0.00070}{2} = 0.00035\text{ mm}^2$$

3. **Operator Variation (Appraiser Variation)**:
   $$\widehat{\sigma}^2_O = \max\left(0, \; \frac{MS_O - MS_{PO}}{p \cdot r}\right) = \frac{0.02700 - 0.00400}{10 \times 2} = \frac{0.02300}{20} = 0.00115\text{ mm}^2$$

4. **Total Reproducibility**:
   $$\widehat{\sigma}^2_{\text{reproducibility}} = \widehat{\sigma}^2_O + \widehat{\sigma}^2_{PO} = 0.00115 + 0.00035 = 0.00150\text{ mm}^2$$

5. **Total Gage R&R Variance**:
   $$\widehat{\sigma}^2_{GRR} = \widehat{\sigma}^2_{\text{repeatability}} + \widehat{\sigma}^2_{\text{reproducibility}} = 0.00330 + 0.00150 = 0.00480\text{ mm}^2$$
   $$\widehat{\sigma}_{GRR} = \sqrt{0.00480} \approx 0.06928\text{ mm}$$

6. **Part-to-Part Variance**:
   $$\widehat{\sigma}^2_{\text{part}} = \frac{MS_P - MS_{PO}}{o \cdot r} = \frac{0.18000 - 0.00400}{3 \times 2} = \frac{0.17600}{6} \approx 0.029333\text{ mm}^2$$
   $$\widehat{\sigma}_{\text{part}} = \sqrt{0.029333} \approx 0.17127\text{ mm}$$

7. **Total Observed Variation**:
   $$\widehat{\sigma}^2_{\text{total}} = \widehat{\sigma}^2_{\text{part}} + \widehat{\sigma}^2_{GRR} = 0.029333 + 0.00480 = 0.034133\text{ mm}^2$$
   $$\widehat{\sigma}_{\text{total}} = \sqrt{0.034133} \approx 0.18475\text{ mm}$$

### Solution, step 3: Evaluate Gage R&R criteria and acceptability
1. **Precision-to-Tolerance Ratio ($P/T$)**:
   Tolerance $= USL - LSL = 0.500\text{ mm}$.
   $$P/T = \frac{6 \widehat{\sigma}_{GRR}}{USL - LSL} \times 100\% = \frac{6 \times 0.06928}{0.500} \times 100\% = \frac{0.41568}{0.500} \times 100\% = 83.14\%$$

2. **Percentage of Total Process Variation ($\%GRR$)**:
   $$\%GRR = \frac{\widehat{\sigma}_{GRR}}{\widehat{\sigma}_{\text{total}}} \times 100\% = \frac{0.06928}{0.18475} \times 100\% \approx 37.50\%$$

3. **Number of Distinct Categories ($ndc$)**:
   $$ndc = \left\lfloor 1.41 \frac{\widehat{\sigma}_{\text{part}}}{\widehat{\sigma}_{GRR}} \right\rfloor = \left\lfloor 1.41 \times \frac{0.17127}{0.06928} \right\rfloor = \lfloor 1.41 \times 2.4721 \rfloor = \lfloor 3.486 \rfloor = 3$$

**System Evaluation**:
- The $P/T$ ratio is $83.14\%$ (far exceeding the $30\%$ maximum allowable ceiling).
- The $\%GRR$ is $37.50\%$ (exceeding the $30\%$ limit).
- The $ndc = 3$ (strictly below the mandatory minimum of $5$ distinct categories).

**Conclusion**: The optical vision measurement system is completely unacceptable for production release. The Gage R&R consumes over $83\%$ of the customer's tolerance band. The measurement system requires immediate engineering intervention: the primary driver is repeatability ($EV = \sqrt{0.00330} \approx 0.0574\text{ mm}$, which is $68.8\%$ of total measurement variance), pointing to lens positioning vibrations, lighting variations, or autofocus camera resolution limitations.
"""

(DRAFT_DIR / "unit-1.md").write_text(unit_1.strip() + "\n", encoding="utf-8")
print("Unit 1 written.")

(DRAFT_DIR / "unit-2.md").write_text(unit_2.strip() + "\n", encoding="utf-8")
print("Unit 2 written.")
