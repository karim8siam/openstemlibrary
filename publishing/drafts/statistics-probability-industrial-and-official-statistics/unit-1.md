# Unit 1: Foundations of Statistical Quality Control & Shewhart Control Charts for Variables

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

## 1.8 Phase I Retrospective Setup Versus Phase II Operational Monitoring

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

## 1.11 Short-Run Statistical Process Control and Deviation from Nominal Charts

Traditional Shewhart control charts were formulated for high-volume mass production lines manufacturing thousands of identical parts across months of continuous operation. In modern flexible manufacturing systems, aerospace machine shops, and job-shop environments, production runs are short—often consisting of only 20 to 50 parts before the machine is retooled for a completely different part geometry or customer contract. In such low-volume, high-mix environments, waiting for 25 subgroups of identical parts to establish Phase I control limits is impossible.

To monitor short production runs across diverse part families on a single machine tool, quality statisticians utilize **Short-Run SPC** methodologies:

### 1. Deviation from Nominal (DNOM) Charts
When a single CNC machining center mills different parts that have different nominal design targets $T_i$ but share similar process variability $\sigma$, the raw measurement $X$ is replaced with the **Deviation from Nominal**:

$$Y_{ij} = X_{ij} - T_i$$

Because the nominal target is subtracted, the transformed variable $Y$ has an expected value of zero ($\mathbb{E}[Y] = 0$) regardless of which specific part is currently being machined. Subgroup averages of deviations $\bar{Y}$ and ranges $R_Y$ are plotted on a single unified control chart across consecutive production runs of completely different parts.

### 2. Standardized Short-Run $\bar{X}$ and $R$ Charts
When consecutive parts differ not only in nominal targets $T_i$ but also in process variability $\sigma_i$ (due to differing tolerances, material hardness, or tool diameters), DNOM is insufficient. Quality engineering applies **Standardized Short-Run Charts**:

For part family $i$ with target $T_i$ and expected average range $\bar{R}_i$, compute the standardized statistics for subgroup $k$:

$$Z_{\bar{X}, k} = \frac{\bar{X}_k - T_i}{\bar{R}_i / (d_2 \sqrt{n})} = \frac{\bar{X}_k - T_i}{A_2 \bar{R}_i / 3}$$

$$W_{R, k} = \frac{R_k}{\bar{R}_i}$$

The standardized mean statistic $Z_{\bar{X}}$ is plotted against fixed universal control limits at $CL = 0, \pm 3$. The standardized range statistic $W_R$ is plotted against center line $CL = 1.0$ with limits at $D_3$ and $D_4$. 

Standardized short-run charting enables a single machine operator to maintain continuous real-time statistical process control across dozens of different part orders on a single control chart, eliminating the traditional barrier to SPC in high-mix manufacturing.

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
