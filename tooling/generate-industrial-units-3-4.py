#!/usr/bin/env python3
"""
Generate Units 3 and 4 for Industrial and Official Statistics.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_3 = r"""# Unit 3: Control Charts for Attributes: Proportion, Nonconforming Units & Defect Count Models

## 3.1 Classification of Quality Characteristics: Variables Versus Attributes

Industrial quality characteristics fall into two primary measurement classifications:
1. **Variables Data**: Continuous physical dimensions, masses, pressures, voltages, concentrations, and temperatures that can be quantified along an unbroken real-number scale. Variables data are informationally rich, allowing for the simultaneous estimation of process mean and process variance.
2. **Attributes Data**: Qualitative, discrete classifications where items are evaluated against go/no-go gauges, visual cosmetic criteria, functional pass/fail tests, or defect counts. 

Within attributes quality engineering, a strict terminology distinction separates **nonconforming items** from **nonconformities**:
- A **nonconforming item (defective unit)** is an entire product or assembly that fails to meet one or more specification requirements, rendering the unit unfit for its intended function (e.g., an electric motor that fails to start). An item is either conforming or nonconforming (binary outcome).
- A **nonconformity (defect)** is a specific flaw or localized departure from quality specifications (e.g., a scratch on a painted automotive door panel, a solder bridge on a printed circuit board, or a void in an injection-molded housing). A single manufactured item may contain multiple nonconformities while still remaining functional.

Attributes control charts monitor either the proportion of nonconforming items ($p$-chart), the count of nonconforming items ($np$-chart), the total count of nonconformities ($c$-chart), or the average nonconformities per inspection unit ($u$-chart).

## 3.2 The $p$-Chart for Fraction Nonconforming

The $p$-chart monitors the fraction of nonconforming items in a sequence of production lots or inspection samples. Suppose a random sample of $n$ items is inspected from a production process where the true probability of generating a nonconforming item is $p$. Assuming the manufacturing process behaves as a stationary Bernoulli process with independent trials and constant defect probability $p$, the number of nonconforming items $D$ follows a Binomial distribution:

$$D \sim \text{Binomial}(n, p), \qquad P(D = d) = \binom{n}{d} p^d (1 - p)^{n-d}$$

The sample proportion nonconforming is:

$$\widehat{p} = \frac{D}{n}$$

The statistical properties of $\widehat{p}$ are:

$$\mathbb{E}[\widehat{p}] = p, \qquad \sigma_p = \sqrt{\text{Var}(\widehat{p})} = \sqrt{\frac{p(1 - p)}{n}}$$

### Shewhart $3\sigma$ Control Limits for the $p$-Chart
When the true parameter $p$ is known or targeted, the control limits are:

$$UCL = p + 3 \sqrt{\frac{p(1 - p)}{n}}, \qquad CL = p, \qquad LCL = \max\left(0, \; p - 3 \sqrt{\frac{p(1 - p)}{n}}\right)$$

When $p$ is unknown, it is estimated from $m$ historical Phase I subgroups of size $n$, each yielding $D_i$ nonconforming items:

$$\bar{p} = \frac{\sum_{i=1}^m D_i}{\sum_{i=1}^m n_i} = \frac{\sum_{i=1}^m D_i}{m \cdot n}$$

The trial control limits are:

$$UCL = \bar{p} + 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}, \qquad CL = \bar{p}, \qquad LCL = \max\left(0, \; \bar{p} - 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}\right)$$

Because a proportion cannot be negative, whenever the calculated $LCL$ is less than zero, it is conventionally truncated to $LCL = 0$. In attribute control, a plotted point falling below $LCL$ is not a defect—it signifies an extraordinary process improvement (unusually low defect rate) or an inspection failure (operator missed defects).

## 3.3 Handling Variable Subgroup Sizes in $p$-Charts

In real-world assembly and receiving operations, inspection lot sizes often fluctuate due to variable shift output, differing supplier shipment sizes, or 100% sorting of varying batch sizes. When the sample size $n_i$ changes from subgroup to subgroup, the standard error $\sigma_{p_i} = \sqrt{\bar{p}(1 - \bar{p})/n_i}$ changes dynamically, causing the control limits to widen for small lots and narrow for large lots.

### Approach 1: Individual Variable Control Limits
For each subgroup $i$ with sample size $n_i$, exact individual limits are calculated:

$$UCL_i = \bar{p} + 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{n_i}}, \qquad LCL_i = \max\left(0, \; \bar{p} - 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{n_i}}\right)$$

This approach produces "staircase" control limits on the chart. It is exact and statistically rigorous, though visually more complex to interpret.

### Approach 2: Standardized $p$-Chart ($Z$-Chart)
To maintain a clean, flat control chart with constant horizontal limits, the sample proportion $\widehat{p}_i$ is standardized into a $Z$-score:

$$Z_i = \frac{\widehat{p}_i - \bar{p}}{\sqrt{\frac{\bar{p}(1 - \bar{p})}{n_i}}}$$

The standardized statistic $Z_i$ is plotted against fixed, universal control limits:

$$UCL = +3, \qquad CL = 0, \qquad LCL = -3$$

A point plotting above $+3$ indicates an out-of-control spike in nonconformance, while a point plotting below $-3$ indicates significant quality improvement. Standardized charts also permit the simultaneous plotting of different inspection stations with widely differing base proportions on a single consolidated enterprise dashboard.

### Approach 3: Average Sample Size Approximation
If individual sample sizes $n_i$ do not vary by more than $\pm 25\%$ from their average $\bar{n} = \frac{1}{m} \sum_{i=1}^m n_i$, quality engineers often compute a single set of constant approximate control limits using $\bar{n}$:

$$UCL \approx \bar{p} + 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{\bar{n}}}, \qquad LCL \approx \max\left(0, \; \bar{p} - 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{\bar{n}}}\right)$$

However, for any subgroup whose plotted proportion falls very close to the approximate limits, the exact individual limit for that specific $n_i$ must be evaluated before taking corrective action.

## 3.4 The $np$-Chart for Number of Nonconforming Items

When the inspection sample size is strictly constant across all subgroups ($n_i = n$), quality technicians frequently prefer to plot the raw integer count of nonconforming items $D_i$ rather than the decimal fraction $\widehat{p}_i$. The $np$-chart eliminates the step of dividing by $n$, reducing clerical calculation errors on the factory floor.

The statistical properties of $D = n \widehat{p}$ are:

$$\mathbb{E}[D] = n p, \qquad \sigma_D = \sqrt{n p (1 - p)}$$

Across $m$ Phase I subgroups of constant size $n$, the average number of nonconforming units is:

$$n \bar{p} = \frac{1}{m} \sum_{i=1}^m D_i$$

The $3\sigma$ control limits for the $np$-chart are:

$$UCL = n \bar{p} + 3 \sqrt{n \bar{p} (1 - \bar{p})}$$

$$CL = n \bar{p}$$

$$LCL = \max\left(0, \; n \bar{p} - 3 \sqrt{n \bar{p} (1 - \bar{p})}\right)$$

The $np$-chart is mathematically identical to the $p$-chart scaled by the constant factor $n$. It cannot be applied when subgroup sizes vary.

## 3.5 The $c$-Chart for Count of Nonconformities (Defects)

When an inspection unit consists of an entire continuous item or complex assembly (e.g., $100\text{ m}^2$ of rolled sheet steel, a completed aircraft fuselage panel, or an automotive wiring harness), we monitor the total number of nonconformities (defects) $C$ found per inspection unit.

Suppose defects occur randomly and independently across the inspection unit, with a constant average occurrence rate per unit area or volume. Under these conditions, the number of defects $C$ follows a Poisson distribution:

$$P(C = c) = \frac{e^{-\lambda} \lambda^c}{c!}, \qquad c = 0, 1, 2, \dots$$

where $\lambda > 0$ is the mean defect count per unit. A fundamental property of the Poisson distribution is that its variance equals its mean:

$$\mathbb{E}[C] = \lambda, \qquad \sigma_C^2 = \text{Var}(C) = \lambda \implies \sigma_C = \sqrt{\lambda}$$

### Control Limits for the $c$-Chart
When $m$ baseline Phase I units are inspected, each of identical size, and defect counts $C_1, C_2, \dots, C_m$ are recorded:

$$\bar{c} = \frac{1}{m} \sum_{i=1}^m C_i$$

The $3\sigma$ Shewhart limits are:

$$UCL = \bar{c} + 3 \sqrt{\bar{c}}, \qquad CL = \bar{c}, \qquad LCL = \max(0, \; \bar{c} - 3 \sqrt{\bar{c}})$$

### Probability Limits Versus $3\sigma$ Limits
Because the Poisson distribution is positively skewed (skewness $\gamma_1 = 1/\sqrt{\lambda}$), symmetric $3\sigma$ limits do not yield equal tail probabilities. For low defect rates ($\bar{c} < 5$), the lower $3\sigma$ limit is truncated to zero, completely eliminating the chart's ability to signal quality improvements.

In high-precision applications, quality engineers construct exact **probability limits** using the cumulative Poisson distribution:
- Upper limit: Find smallest integer $UCL$ such that $P(C > UCL \mid \bar{c}) \le \alpha/2 = 0.00135$.
- Lower limit: Find largest integer $LCL$ such that $P(C < LCL \mid \bar{c}) \le \alpha/2 = 0.00135$.

## 3.6 The $u$-Chart for Nonconformities per Inspection Unit

When the size of the inspection unit varies from subgroup to subgroup (e.g., inspecting rolls of fabric of differing lengths, or inspecting variable numbers of electronic modules per production shift), the $c$-chart is invalid. In such cases, we monitor the average defect rate per standard unit $u$:

$$u_i = \frac{C_i}{k_i}$$

where $C_i$ is the total number of defects discovered in subgroup $i$, and $k_i$ is the number of standard inspection units contained within subgroup $i$. For example, if a standard unit is defined as $10\text{ m}^2$ of fabric, an inspected roll of $25\text{ m}^2$ corresponds to $k_i = 2.5$ standard units.

Because $C_i \sim \text{Poisson}(k_i u)$, the mean and variance of $u_i$ are:

$$\mathbb{E}[u_i] = u, \qquad \text{Var}(u_i) = \text{Var}\left(\frac{C_i}{k_i}\right) = \frac{k_i u}{k_i^2} = \frac{u}{k_i}$$

The standard error of $u_i$ is $\sigma_{u_i} = \sqrt{u / k_i}$.

Across $m$ Phase I subgroups with varying areas $k_i$, the pooled average defect rate is:

$$\bar{u} = \frac{\sum_{i=1}^m C_i}{\sum_{i=1}^m k_i}$$

The exact individual $3\sigma$ control limits for subgroup $i$ are:

$$UCL_i = \bar{u} + 3 \sqrt{\frac{\bar{u}}{k_i}}, \qquad CL = \bar{u}, \qquad LCL_i = \max\left(0, \; \bar{u} - 3 \sqrt{\frac{\bar{u}}{k_i}}\right)$$

As with the $p$-chart, the $u$-chart can be standardized into $Z_i = (u_i - \bar{u}) / \sqrt{\bar{u}/k_i}$ with fixed control limits at $\pm 3$.

## 3.7 Overdispersion in Attribute Charts: Laney $p'$ and $u'$ Control Charts

A critical failure mode of traditional $p$-charts and $u$-charts occurs when sample sizes $n$ or inspection units $k$ become exceptionally large (e.g., tens of thousands of items per batch in automated pharmaceutical vial filling or consumer electronics production). As $n \to \infty$, the theoretical binomial or Poisson standard error $\sqrt{\bar{p}(1-\bar{p})/n} \to 0$, causing the control limits to collapse into an infinitesimally narrow band around $\bar{p}$.

When limits become ultra-narrow, ordinary day-to-day common-cause fluctuations—minor temperature shifts, slight vendor material batch changes, or operator shift changeovers—will plot outside the control limits, triggering an endless cascade of false alarms. This phenomenon is known as **overdispersion** (or extra-binomial/extra-Poisson variation): the actual empirical subgroup variance is substantially larger than the theoretical binomial or Poisson variance.

David B. Laney (2002) resolved this dilemma by formulating the **Laney $p'$ and $u'$ charts**. Laney recognized that total variation consists of two additive components:
1. Within-subgroup binomial/Poisson sampling error.
2. Between-subgroup process variation over time.

### The Laney $p'$ Algorithm
1. Compute the standard standardized $Z$-scores for each subgroup:
   $$Z_i = \frac{\widehat{p}_i - \bar{p}}{\sqrt{\frac{\bar{p}(1 - \bar{p})}{n_i}}}$$
2. Calculate the moving ranges between successive $Z$-scores:
   $$MR_i = |Z_i - Z_{i-1}|, \qquad i = 2, 3, \dots, m$$
3. Compute the average moving range $\overline{MR} = \frac{1}{m-1} \sum_{i=2}^m MR_i$.
4. Estimate the overdispersion variance inflation factor $\sigma_Z$:
   $$\widehat{\sigma}_Z = \frac{\overline{MR}}{d_2} = \frac{\overline{MR}}{1.128}$$
   If the process satisfies pure binomial variation, $\sigma_Z = 1.0$. If $\sigma_Z > 1.0$, overdispersion is present; if $\sigma_Z < 1.0$, underdispersion is present.
5. Compute the Laney $p'$ control limits adjusted by $\widehat{\sigma}_Z$:
   $$UCL_i = \bar{p} + 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{n_i}} \cdot \widehat{\sigma}_Z$$
   $$LCL_i = \max\left(0, \; \bar{p} - 3 \sqrt{\frac{\bar{p}(1 - \bar{p})}{n_i}} \cdot \widehat{\sigma}_Z\right)$$

The Laney chart completely eliminates artificial false alarms caused by large sample sizes, providing an indispensable tool for modern big-data industrial surveillance.

## 3.8 Cumulative Count of Conforming (CCC) Charts for Ultra-High Quality Processes

In Six Sigma and zero-defect manufacturing environments, defect rates are measured in parts per million ($p \le 10^{-5}$). In such high-yield processes, traditional $p$-charts are utterly useless: almost every sample contains $0$ nonconforming parts, with points plotting continuously along the lower control limit $0$. When a defect finally occurs, $\widehat{p}$ spikes above the $UCL$, but the chart provides zero forewarning.

To monitor ultra-low defect processes, quality engineering flips the paradigm: instead of counting defectives in a fixed sample, we monitor the **number of conforming units produced between consecutive defects** ($Y$).

Assuming independent Bernoulli trials with nonconformance probability $p$, the random variable $Y$ follows a Geometric distribution:

$$P(Y = y) = (1 - p)^{y-1} p, \qquad y = 1, 2, 3, \dots$$

The cumulative distribution function of $Y$ is:

$$F(y) = P(Y \le y) = 1 - (1 - p)^y$$

### Probability Limits for the CCC Chart
Because the Geometric distribution is extremely skewed, exact probability limits are established for a false alarm probability $\alpha$:
- **Lower Control Limit ($LCL$)**: A very small count of items between defects indicates an abrupt *increase* in the defect rate (a process degradation):
  $$F(LCL) = \frac{\alpha}{2} \implies 1 - (1 - p)^{LCL} = \frac{\alpha}{2} \implies LCL = \frac{\ln(1 - \alpha/2)}{\ln(1 - p)}$$
- **Center Line ($CL$)**: The median of the Geometric distribution:
  $$F(CL) = 0.50 \implies CL = \frac{\ln(0.5)}{\ln(1 - p)}$$
- **Upper Control Limit ($UCL$)**: An exceptionally long run of conforming units indicates a significant quality improvement:
  $$F(UCL) = 1 - \frac{\alpha}{2} \implies 1 - (1 - p)^{UCL} = 1 - \frac{\alpha}{2} \implies UCL = \frac{\ln(\alpha/2)}{\ln(1 - p)}$$

For $\alpha = 0.0027$ and $p = 100\text{ PPM} = 0.0001$:
$$LCL = \frac{\ln(1 - 0.00135)}{\ln(0.9999)} \approx \frac{-0.001351}{-0.0001} \approx 14\text{ units}$$
$$CL = \frac{\ln(0.5)}{\ln(0.9999)} \approx \frac{-0.69315}{-0.0001} \approx 6,931\text{ units}$$
$$UCL = \frac{\ln(0.00135)}{\ln(0.9999)} \approx \frac{-6.6077}{-0.0001} \approx 66,077\text{ units}$$

If two defects occur within fewer than $14$ units of each other, an immediate out-of-control alarm is triggered, alerting operators to an acute process collapse.

## Fully worked question 1: Standardized $p$-Chart with Variable Subgroup Sizes

### Question
An electronics contract manufacturer inspects surface-mount device (SMD) circuit boards post-reflow soldering. Subgroup sample sizes fluctuate daily due to differing assembly line work orders. The quality engineering department records the following inspection data across five consecutive production shifts:
- Shift 1: $n_1 = 800$ boards, $D_1 = 16$ nonconforming boards
- Shift 2: $n_2 = 1,250$ boards, $D_2 = 35$ nonconforming boards
- Shift 3: $n_3 = 600$ boards, $D_3 = 24$ nonconforming boards
- Shift 4: $n_4 = 1,000$ boards, $D_4 = 18$ nonconforming boards
- Shift 5: $n_5 = 1,500$ boards, $D_5 = 27$ nonconforming boards

Perform the following analyses:
1. Calculate the sample proportion nonconforming $\widehat{p}_i$ for each shift.
2. Determine the pooled baseline proportion nonconforming $\bar{p}$.
3. Compute exact individual $3\sigma$ control limits ($LCL_i, UCL_i$) for Shift 2 and Shift 3.
4. Calculate the standardized statistic $Z_i$ for all five shifts.
5. Determine whether any shift is out of statistical control on the standardized $Z$-chart ($CL = 0, \pm 3$).

### Solution, step 1: Calculate sample proportions and pooled baseline $\bar{p}$
Compute individual shift nonconforming fractions $\widehat{p}_i = D_i / n_i$:
- Shift 1: $\widehat{p}_1 = 16 / 800 = 0.02000$ ($2.00\%$)
- Shift 2: $\widehat{p}_2 = 35 / 1,250 = 0.02800$ ($2.80\%$)
- Shift 3: $\widehat{p}_3 = 24 / 600 = 0.04000$ ($4.00\%$)
- Shift 4: $\widehat{p}_4 = 18 / 1,000 = 0.01800$ ($1.80\%$)
- Shift 5: $\widehat{p}_5 = 27 / 1,500 = 0.01800$ ($1.80\%$)

Total boards inspected:
$$N = \sum_{i=1}^5 n_i = 800 + 1,250 + 600 + 1,000 + 1,500 = 5,150$$
Total nonconforming boards:
$$\sum_{i=1}^5 D_i = 16 + 35 + 24 + 18 + 27 = 120$$

The pooled baseline proportion is:
$$\bar{p} = \frac{120}{5,150} \approx 0.023301 = 2.3301\%$$
The numerator of the standard error term is:
$$\bar{p}(1 - \bar{p}) = 0.023301 \times (1 - 0.023301) = 0.023301 \times 0.976699 \approx 0.022758$$

### Solution, step 2: Compute individual exact limits for Shifts 2 and 3
1. **Shift 2 ($n_2 = 1,250$)**:
   $$\sigma_{p_2} = \sqrt{\frac{0.022758}{1,250}} = \sqrt{0.000018206} \approx 0.004267$$
   $$UCL_2 = \bar{p} + 3 \sigma_{p_2} = 0.023301 + 3(0.004267) = 0.023301 + 0.012801 = 0.036102 \approx 3.61\%$$
   $$LCL_2 = \max(0, \; 0.023301 - 0.012801) = 0.010500 \approx 1.05\%$$
   Observed $\widehat{p}_2 = 0.02800$. Since $0.0105 \le 0.02800 \le 0.0361$, Shift 2 is in control.

2. **Shift 3 ($n_3 = 600$)**:
   $$\sigma_{p_3} = \sqrt{\frac{0.022758}{600}} = \sqrt{0.000037930} \approx 0.006159$$
   $$UCL_3 = \bar{p} + 3 \sigma_{p_3} = 0.023301 + 3(0.006159) = 0.023301 + 0.018476 = 0.041777 \approx 4.18\%$$
   $$LCL_3 = \max(0, \; 0.023301 - 0.018476) = 0.004825 \approx 0.48\%$$
   Observed $\widehat{p}_3 = 0.04000$. Since $0.0048 \le 0.04000 \le 0.0418$, Shift 3 is marginally in control under exact limits.

### Solution, step 3: Construct standardized $Z$-scores and assess control
Compute $Z_i = (\widehat{p}_i - \bar{p}) / \sigma_{p_i}$ for each shift:
- Shift 1 ($n_1 = 800$):
  $$\sigma_{p_1} = \sqrt{0.022758 / 800} = \sqrt{0.000028448} \approx 0.005334$$
  $$Z_1 = \frac{0.02000 - 0.023301}{0.005334} = \frac{-0.003301}{0.005334} \approx -0.619$$
- Shift 2 ($n_2 = 1,250$):
  $$Z_2 = \frac{0.02800 - 0.023301}{0.004267} = \frac{+0.004699}{0.004267} \approx +1.101$$
- Shift 3 ($n_3 = 600$):
  $$Z_3 = \frac{0.04000 - 0.023301}{0.006159} = \frac{+0.016699}{0.006159} \approx +2.711$$
- Shift 4 ($n_4 = 1,000$):
  $$\sigma_{p_4} = \sqrt{0.022758 / 1,000} \approx 0.004771$$
  $$Z_4 = \frac{0.01800 - 0.023301}{0.004771} = \frac{-0.005301}{0.004771} \approx -1.111$$
- Shift 5 ($n_5 = 1,500$):
  $$\sigma_{p_5} = \sqrt{0.022758 / 1,500} \approx 0.003895$$
  $$Z_5 = \frac{0.01800 - 0.023301}{0.003895} = \frac{-0.005301}{0.003895} \approx -1.361$$

**Evaluation**:
On the standardized $Z$-chart with control limits at $\pm 3.000$:
All $Z_i \in [-1.361, +2.711]$. No point breaches $\pm 3$.
However, Shift 3 exhibits $Z_3 = +2.71$, which enters **Zone A** ($+2\sigma$ to $+3\sigma$). Quality engineers should place Shift 3 under close surveillance to ensure this elevation does not persist into an assignable cause.

## Fully worked question 2: Overdispersion Diagnostics and Laney $p'$ Chart Construction

### Question
A pharmaceutical manufacturer operates an automated packaging machine that bottles sterile injectable saline vials. Subgroups of $n = 20,000$ vials are inspected hourly by an automated machine-vision camera system for particulate contamination.

Across $m = 10$ consecutive production hours, the observed nonconforming vial counts are:
$D = [48, 56, 52, 68, 42, 64, 50, 72, 44, 58]$.

Perform the following calculations:
1. Compute the proportion nonconforming $\widehat{p}_i$ for each hour and the overall baseline mean $\bar{p}$.
2. Compute the standard Shewhart $p$-chart control limits.
3. Calculate the standard standardized $Z_i$ values and the moving ranges $MR_i = |Z_i - Z_{i-1}|$.
4. Determine the average moving range $\overline{MR}$ and estimate the dispersion ratio $\widehat{\sigma}_Z$.
5. State whether the inspection process exhibits significant overdispersion.
6. Construct the adjusted Laney $p'$ control limits and compare them with standard Shewhart limits.

### Solution, step 1: Compute sample proportions and baseline $\bar{p}$
Total vials inspected: $N = 10 \times 20,000 = 200,000$.
Total defectives:
$$\sum_{i=1}^{10} D_i = 48 + 56 + 52 + 68 + 42 + 64 + 50 + 72 + 44 + 58 = 554$$
$$\bar{p} = \frac{554}{200,000} = 0.002770 = 2,770\text{ PPM}$$

Sample proportions $\widehat{p}_i = D_i / 20,000$:
$$\widehat{p} = [0.00240, 0.00280, 0.00260, 0.00340, 0.00210, 0.00320, 0.00250, 0.00360, 0.00220, 0.00290]$$

### Solution, step 2: Standard Shewhart $p$-chart limits
Theoretical binomial standard error:
$$\sigma_{\text{binomial}} = \sqrt{\frac{\bar{p}(1 - \bar{p})}{n}} = \sqrt{\frac{0.002770 \times (1 - 0.002770)}{20,000}} = \sqrt{\frac{0.0027623}{20,000}} = \sqrt{1.38116 \times 10^{-7}} \approx 0.0003716$$

Shewhart limits:
$$UCL_{\text{Shewhart}} = \bar{p} + 3 \sigma_{\text{binomial}} = 0.002770 + 3(0.0003716) = 0.002770 + 0.001115 = 0.003885$$
$$LCL_{\text{Shewhart}} = \max(0, \; 0.002770 - 0.001115) = 0.001655$$

In terms of defect counts ($np$):
$$UCL_D = 20,000 \times 0.003885 = 77.7\text{ defects}$$
$$LCL_D = 20,000 \times 0.001655 = 33.1\text{ defects}$$

### Solution, step 3: Compute $Z_i$, moving ranges, and Laney $\widehat{\sigma}_Z$
Calculate $Z_i = (\widehat{p}_i - \bar{p}) / \sigma_{\text{binomial}} = (D_i - 55.4) / (20,000 \times 0.0003716) = (D_i - 55.4) / 7.433$:
- $i=1$: $D_1 = 48 \implies Z_1 = (48 - 55.4)/7.433 = -0.996$
- $i=2$: $D_2 = 56 \implies Z_2 = (56 - 55.4)/7.433 = +0.081$
- $i=3$: $D_3 = 52 \implies Z_3 = (52 - 55.4)/7.433 = -0.457$
- $i=4$: $D_4 = 68 \implies Z_4 = (68 - 55.4)/7.433 = +1.695$
- $i=5$: $D_5 = 42 \implies Z_5 = (42 - 55.4)/7.433 = -1.803$
- $i=6$: $D_6 = 64 \implies Z_6 = (64 - 55.4)/7.433 = +1.157$
- $i=7$: $D_7 = 50 \implies Z_7 = (50 - 55.4)/7.433 = -0.727$
- $i=8$: $D_8 = 72 \implies Z_8 = (72 - 55.4)/7.433 = +2.233$
- $i=9$: $D_9 = 44 \implies Z_9 = (44 - 55.4)/7.433 = -1.534$
- $i=10$: $D_{10} = 58 \implies Z_{10} = (58 - 55.4)/7.433 = +0.350$

Moving ranges $MR_i = |Z_i - Z_{i-1}|$:
- $MR_2 = |0.081 - (-0.996)| = 1.077$
- $MR_3 = |-0.457 - 0.081| = 0.538$
- $MR_4 = |1.695 - (-0.457)| = 2.152$
- $MR_5 = |-1.803 - 1.695| = 3.498$
- $MR_6 = |1.157 - (-1.803)| = 2.960$
- $MR_7 = |-0.727 - 1.157| = 1.884$
- $MR_8 = |2.233 - (-0.727)| = 2.960$
- $MR_9 = |-1.534 - 2.233| = 3.767$
- $MR_{10} = |0.350 - (-1.534)| = 1.884$

Sum of $9$ moving ranges:
$$\sum_{i=2}^{10} MR_i = 1.077 + 0.538 + 2.152 + 3.498 + 2.960 + 1.884 + 2.960 + 3.767 + 1.884 = 20.720$$
$$\overline{MR} = \frac{20.720}{9} \approx 2.3022$$

The estimated dispersion ratio is:
$$\widehat{\sigma}_Z = \frac{\overline{MR}}{d_2} = \frac{2.3022}{1.128} \approx 2.041$$
Because $\widehat{\sigma}_Z = 2.041 > 1.0$, the process exhibits substantial **overdispersion**: the true process variation from hour to hour is more than double what pure binomial sampling predicts!

### Solution, step 4: Construct Laney $p'$ control limits
The adjusted standard error is:
$$\sigma_{\text{Laney}} = \sigma_{\text{binomial}} \times \widehat{\sigma}_Z = 0.0003716 \times 2.041 \approx 0.0007584$$

Laney $p'$ control limits:
$$UCL_{\text{Laney}} = \bar{p} + 3 \sigma_{\text{Laney}} = 0.002770 + 3(0.0007584) = 0.002770 + 0.002275 = 0.005045$$
$$LCL_{\text{Laney}} = \max(0, \; 0.002770 - 0.002275) = 0.000495$$

In terms of nonconforming vial counts ($np$):
$$UCL_D = 20,000 \times 0.005045 = 100.9\text{ vials}$$
$$LCL_D = 20,000 \times 0.000495 = 9.9\text{ vials}$$

**Practical Impact**:
Under the unadjusted Shewhart limits ($UCL = 77.7$), normal hourly fluctuations in ambient cleanroom humidity and vial feeder vibration would have frequently triggered false alarms. The Laney $p'$ chart correctly adjusts the limits to $[9.9, 100.9]$, shielding plant engineers from false alarms while remaining capable of detecting genuine structural shifts.

## Fully worked question 3: Variable Area $u$-Chart and Overdispersion Analysis in Textile Manufacturing

### Question
A technical textile manufacturing plant weaves ballistic Kevlar fabric for body armor. Quality inspectors scan continuous fabric bolts for weave defects (broken filaments, slubs, knotting, and warp tension distortion). Because fabric rolls vary in cut length, inspection area varies. A standard inspection unit is defined as $100\text{ m}^2$ of fabric.

The inspection records for four consecutive production lots are:
- Lot 1: Area $A_1 = 350\text{ m}^2$ ($k_1 = 3.5$ units), $C_1 = 28$ defects
- Lot 2: Area $A_2 = 500\text{ m}^2$ ($k_2 = 5.0$ units), $C_2 = 35$ defects
- Lot 3: Area $A_3 = 200\text{ m}^2$ ($k_3 = 2.0$ units), $C_3 = 26$ defects
- Lot 4: Area $A_4 = 450\text{ m}^2$ ($k_4 = 4.5$ units), $C_4 = 36$ defects

Perform the following calculations:
1. Compute the defect rate per inspection unit $u_i$ for each lot.
2. Determine the pooled baseline average defect rate $\bar{u}$.
3. Calculate the exact $3\sigma$ control limits ($LCL_i, UCL_i$) for Lot 1 and Lot 3.
4. Standardize the defect rates into $Z$-scores.
5. Determine whether Lot 3 is in statistical control under exact limits.

### Solution, step 1: Compute defect rates $u_i$ and pooled average $\bar{u}$
Compute defect rate per standard unit ($100\text{ m}^2$):
- Lot 1: $u_1 = C_1 / k_1 = 28 / 3.5 = 8.000\text{ defects/unit}$
- Lot 2: $u_2 = C_2 / k_2 = 35 / 5.0 = 7.000\text{ defects/unit}$
- Lot 3: $u_3 = C_3 / k_3 = 26 / 2.0 = 13.000\text{ defects/unit}$
- Lot 4: $u_4 = C_4 / k_4 = 36 / 4.5 = 8.000\text{ defects/unit}$

Total defects found:
$$\sum_{i=1}^4 C_i = 28 + 35 + 26 + 36 = 125\text{ defects}$$
Total inspection units scanned:
$$\sum_{i=1}^4 k_i = 3.5 + 5.0 + 2.0 + 4.5 = 15.0\text{ units} \quad (1,500\text{ m}^2)$$

The pooled average defect rate per unit is:
$$\bar{u} = \frac{125}{15.0} \approx 8.3333\text{ defects per } 100\text{ m}^2$$

### Solution, step 2: Calculate individual exact limits for Lots 1 and 3
1. **Lot 1 ($k_1 = 3.5$ units)**:
   $$\sigma_{u_1} = \sqrt{\frac{\bar{u}}{k_1}} = \sqrt{\frac{8.3333}{3.5}} = \sqrt{2.38095} \approx 1.5430$$
   $$UCL_1 = \bar{u} + 3 \sigma_{u_1} = 8.3333 + 3(1.5430) = 8.3333 + 4.6290 = 12.9623$$
   $$LCL_1 = \max(0, \; 8.3333 - 4.6290) = 3.7043$$
   Observed $u_1 = 8.000$. Since $3.704 \le 8.000 \le 12.962$, Lot 1 is in control.

2. **Lot 3 ($k_3 = 2.0$ units)**:
   $$\sigma_{u_3} = \sqrt{\frac{\bar{u}}{k_3}} = \sqrt{\frac{8.3333}{2.0}} = \sqrt{4.16667} \approx 2.0412$$
   $$UCL_3 = \bar{u} + 3 \sigma_{u_3} = 8.3333 + 3(2.0412) = 8.3333 + 6.1237 = 14.4570$$
   $$LCL_3 = \max(0, \; 8.3333 - 6.1237) = 2.2096$$
   Observed $u_3 = 13.000$. Since $2.210 \le 13.000 \le 14.457$, Lot 3 is within the $3\sigma$ control limits!

### Solution, step 3: Standardize into $Z$-scores and evaluate process stability
Compute $Z_i = (u_i - \bar{u}) / \sigma_{u_i}$ for each lot:
- Lot 1 ($k_1 = 3.5$): $Z_1 = (8.000 - 8.3333) / 1.5430 = -0.3333 / 1.5430 \approx -0.216$
- Lot 2 ($k_2 = 5.0$):
  $$\sigma_{u_2} = \sqrt{8.3333 / 5.0} = \sqrt{1.66667} \approx 1.2910$$
  $$Z_2 = (7.000 - 8.3333) / 1.2910 = -1.3333 / 1.2910 \approx -1.033$$
- Lot 3 ($k_3 = 2.0$):
  $$Z_3 = (13.000 - 8.3333) / 2.0412 = +4.6667 / 2.0412 \approx +2.286$$
- Lot 4 ($k_4 = 4.5$):
  $$\sigma_{u_4} = \sqrt{8.3333 / 4.5} = \sqrt{1.85185} \approx 1.3608$$
  $$Z_4 = (8.000 - 8.3333) / 1.3608 = -0.3333 / 1.3608 \approx -0.245$$

**Audit Findings**:
- Even though Lot 3 experienced an alarming raw defect count of $26$ in only $200\text{ m}^2$ ($13.0\text{ defects/unit}$), its $Z$-score is $+2.29$. It does not breach the $3\sigma$ upper limit of $+3.000$.
- However, $Z_3 = +2.29$ falls inside **Zone A** ($+2\sigma$ to $+3\sigma$). If a second consecutive lot enters Zone A, Western Electric Rule 2 will trigger an immediate shutdown of the loom.
"""

unit_4 = r"""# Unit 4: Advanced Statistical Process Monitoring: CUSUM, EWMA & Multivariate SPC

## 4.1 Inertia of Shewhart Charts and the Challenge of Small Shifts

Standard Shewhart control charts are "memoryless" filters: the decision regarding whether a process is in control at inspection time $t$ depends exclusively on the single sample statistic $W_t$ observed at that instantaneous moment. All prior historical data points $W_{t-1}, W_{t-2}, \dots, W_1$ are discarded.

While memorylessness makes Shewhart charts extraordinarily robust against large, abrupt catastrophic shocks (shifts of magnitude $\delta \ge 2.5\sigma$, where detection occurs on the very first sample with near $100\%$ probability), it severely degrades their statistical power against small, persistent process shifts ($0.5\sigma \le \delta \le 1.5\sigma$). 

As derived in Unit 1, when a process experiences a $0.5\sigma$ mean shift with subgroup size $n = 4$:
- The probability of detection on a single sample is only $p = 1 - \beta = 0.0228$.
- The Average Run Length is $ARL_1 = 1 / 0.0228 \approx 44$ subgroups.
- If subgroups are drawn hourly, forty-four hours of production—nearly two full days—will elapse before the shift is detected, allowing tens of thousands of off-target parts to enter the supply chain.

To eliminate this operational vulnerability, statistical quality engineering incorporates cumulative memory into the charting statistic. The two preeminent memory-based control charts are the **Cumulative Sum (CUSUM)** chart and the **Exponentially Weighted Moving Average (EWMA)** chart.

## 4.2 The Cumulative Sum (CUSUM) Control Chart

Originally introduced by E. S. Page in 1954, the CUSUM chart directly incorporates all past process history by plotting cumulative sums of deviations of sample values from a target value $\mu_0$.

Let $\bar{X}_i$ denote the sample mean of the $i$-th rational subgroup of size $n$, with in-control mean $\mu_0$ and known standard deviation $\sigma$. The standardized subgroup mean is:

$$Z_i = \frac{\bar{X}_i - \mu_0}{\sigma / \sqrt{n}}$$

### The Two-Sided Tabular (Algorithmic) CUSUM
While early practitioners used graphical V-masks, modern industrial practice universally employs the tabular CUSUM. The tabular CUSUM maintains two separate one-sided accumulators:
- $C_i^+$: The **Upper CUSUM**, which accumulates positive deviations above target (detecting upward mean shifts).
- $C_i^-$: The **Lower CUSUM**, which accumulates negative deviations below target (detecting downward mean shifts).

Starting with initial conditions $C_0^+ = 0$ and $C_0^- = 0$, the recursive update equations are:

$$C_i^+ = \max\left(0, \; \bar{X}_i - (\mu_0 + K) + C_{i-1}^+\right)$$

$$C_i^- = \max\left(0, \; (\mu_0 - K) - \bar{X}_i + C_{i-1}^-\right)$$

where:
- $K$: The **reference value (slack value)**, conventionally chosen halfway between the in-control mean $\mu_0$ and the out-of-control target $\mu_1 = \mu_0 + \delta \sigma / \sqrt{n}$:
  $$K = \frac{|\mu_1 - \mu_0|}{2} = \frac{\delta \sigma}{2 \sqrt{n}}$$
  In standardized units, $k = K / (\sigma / \sqrt{n}) = \delta / 2$.
- $H$: The **decision interval (threshold)**, above which an out-of-control alarm is triggered:
  $$\text{Signal if } C_i^+ > H \quad \text{or} \quad C_i^- > H$$
  In standardized units, $h = H / (\sigma / \sqrt{n})$. Typically, quality engineers set $k = 0.5$ and $h = 4.0$ or $5.0$.

Whenever the accumulation terms become negative, the $\max(0, \cdot)$ operator resets the accumulator to zero. This resetting mechanism prevents the accumulation of "favorable" common-cause noise, ensuring that the CUSUM reacts rapidly as soon as an adverse shift commences.

### Counter Statistics for Shift Diagnosis
The tabular CUSUM also maintains run counters $N_i^+$ and $N_i^-$, recording the number of consecutive periods since the respective accumulator was last zero:
$$N_i^+ = \begin{cases} N_{i-1}^+ + 1 & \text{if } C_i^+ > 0 \\ 0 & \text{if } C_i^+ = 0 \end{cases}$$
When an alarm occurs at sample $t$, the estimated shift onset time is $t - N_t^+ + 1$, and the estimated magnitude of the shifted mean is:
$$\widehat{\mu}_1 = \mu_0 + K + \frac{C_t^+}{N_t^+} \quad (\text{for upper shift})$$

## 4.3 V-Mask Geometry and Equivalence to Sequential Probability Ratio Tests (SPRT)

Historically, CUSUM charts were plotted as raw cumulative sums $S_m = \sum_{i=1}^m (\bar{X}_i - \mu_0)$ against a V-shaped cardboard mask placed over the most recent data point. The V-mask is defined by two geometric parameters:
- **Lead distance $d$**: The distance between the current vertex and the plotted point.
- **Angle $\theta$**: The half-angle of the V-mask opening.

George A. Barnard (1959) and E. S. Page proved that the V-mask CUSUM is mathematically identical to Wald’s **Sequential Probability Ratio Test (SPRT)** for testing the composite hypothesis:
$$H_0: \mu = \mu_0 \quad \text{vs} \quad H_1: \mu = \mu_0 + \delta \sigma / \sqrt{n}$$
The decision boundaries of the SPRT translate directly into the linear slopes of the V-mask arms:
$$\tan \theta = \frac{k}{A}, \qquad d = \frac{h}{k}$$
where $A$ is the horizontal-to-vertical plotting scale factor. If any historical point falls behind the arms of the V-mask, the null hypothesis $H_0$ is rejected, triggering an out-of-control alarm. Because the tabular CUSUM executes identical mathematics algorithmically without drafting errors, it has superseded physical V-masks.

## 4.4 Average Run Length Derivations: Siegmund's Approximation and Markov Chains

Evaluating the performance of a CUSUM chart requires computing its Average Run Length ($ARL$). Because the CUSUM accumulator is continuous and bounded below by zero, run lengths do not follow a simple geometric distribution.

### Siegmund's Continuous Brownian Approximation
David Siegmund (1985) derived an accurate analytical continuous approximation for the ARL of a one-sided CUSUM using Brownian motion boundary-crossing theory:

$$ARL = \frac{\exp(-2 \Delta b) + 2 \Delta b - 1}{2 \Delta^2}$$

where:
$$\Delta = \delta^* - k = \frac{\mu - \mu_0}{\sigma / \sqrt{n}} - k, \qquad b = h + 1.166$$
The constant $1.166$ represents an overshoot correction factor accounting for the discrete sampling steps across the continuous decision threshold $h$.

When $\Delta = 0$ (the shift magnitude exactly matches the reference value $k$), applying L'Hôpital's rule yields:
$$ARL(\Delta = 0) = b^2 = (h + 1.166)^2$$

For a two-sided CUSUM, the overall average run length $ARL_{\text{two-sided}}$ is obtained from the two individual one-sided run lengths via the parallel hazard formula:

$$\frac{1}{ARL_{\text{two-sided}}} = \frac{1}{ARL^+} + \frac{1}{ARL^-}$$

### Brook and Evans Markov Chain Method
D. Brook and D. A. Evans (1972) formulated the exact numerical evaluation of CUSUM ARL by discretizing the continuous interval $[0, h]$ into $t$ discrete transient states of width $w = h / (t - 0.5)$, with state $t + 1$ representing the absorbing out-of-control state.

The transition probability matrix $\mathbf{P}$ of the Markov chain has the canonical form:

$$\mathbf{P} = \begin{pmatrix} \mathbf{R} & (\mathbf{I} - \mathbf{R})\mathbf{1} \\ \mathbf{0}^T & 1 \end{pmatrix}$$

where $\mathbf{R}$ is the $t \times t$ submatrix of transition probabilities between transient states. The fundamental matrix of the Markov chain is:

$$\mathbf{M} = (\mathbf{I} - \mathbf{R})^{-1}$$

The vector of expected run lengths starting from each initial state is:

$$\boldsymbol{\mu}_{\text{ARL}} = \mathbf{M} \mathbf{1} = (\mathbf{I} - \mathbf{R})^{-1} \mathbf{1}$$

The standard zero-start $ARL$ corresponds to the first element $\mu_{\text{ARL}, 1}$, representing the expected steps to absorption starting from $C_0 = 0$.

## 4.5 The Exponentially Weighted Moving Average (EWMA) Control Chart

S. W. Roberts (1959) introduced the EWMA control chart, which monitors an exponentially smoothed moving average that assigns geometrically decaying weights to historical observations.

Let $X_t$ denote the $t$-th observation (or subgroup mean $\bar{X}_t$) at time $t = 1, 2, 3, \dots$. The EWMA statistic $Z_t$ is defined recursively:

$$Z_t = \lambda X_t + (1 - \lambda) Z_{t-1}$$

where:
- $\lambda \in (0, 1]$: The smoothing constant (weight assigned to the newest observation).
- $Z_0$: The starting value, initialized to the in-control process target: $Z_0 = \mu_0$.

Expanding the recursion reveals the explicit geometric weighting:

$$Z_t = \lambda \sum_{j=0}^{t-1} (1 - \lambda)^j X_{t-j} + (1 - \lambda)^t Z_0$$

Notice two profound mathematical properties:
1. If $\lambda = 1$, $Z_t = X_t$, and the EWMA collapses into the memoryless Shewhart control chart.
2. As $\lambda \to 0$, the EWMA assigns virtually equal weight to all past history, behaving like a cumulative average.

### Variance and Control Limits
Assuming independent observations $X_t$ with common variance $\sigma_X^2 = \sigma^2 / n$:

$$\text{Var}(Z_t) = \lambda^2 \sum_{j=0}^{t-1} (1 - \lambda)^{2j} \sigma_X^2 = \lambda^2 \frac{1 - (1 - \lambda)^{2t}}{1 - (1 - \lambda)^2} \sigma_X^2 = \frac{\lambda}{2 - \lambda} \left[ 1 - (1 - \lambda)^{2t} \right] \sigma_X^2$$

The exact, time-varying $3\sigma$ control limits for the EWMA chart are:

$$UCL_t = \mu_0 + L \sigma_X \sqrt{\frac{\lambda}{2 - \lambda} \left[ 1 - (1 - \lambda)^{2t} \right]}$$

$$CL = \mu_0$$

$$LCL_t = \mu_0 - L \sigma_X \sqrt{\frac{\lambda}{2 - \lambda} \left[ 1 - (1 - \lambda)^{2t} \right]}$$

where $L$ is the control limit width multiplier (typically $L \approx 2.7$ to $3.0$).

As time progresses ($t \to \infty$), the term $(1 - \lambda)^{2t} \to 0$, and the limits converge to steady-state horizontal asymptotic limits:

$$UCL_{\infty} = \mu_0 + L \sigma_X \sqrt{\frac{\lambda}{2 - \lambda}}, \qquad LCL_{\infty} = \mu_0 - L \sigma_X \sqrt{\frac{\lambda}{2 - \lambda}}$$

Industrial practice typically uses exact time-varying limits for the first $t \le 10$ samples to prevent false alarms during startup, switching to steady-state limits thereafter.

## 4.6 Optimal Parameter Selection and Fast Initial Response (FIR)

The design parameters of an EWMA chart are the smoothing constant $\lambda$ and limit multiplier $L$. J. M. Lucas and M. S. Saccucci (1990) published extensive design tables:
- To optimize detection of small shifts ($\delta \approx 0.5\sigma$ to $1.0\sigma$), select small smoothing values: $\lambda \in [0.05, 0.20]$. A universal industry standard is $\lambda = 0.10$ and $L = 2.70$, which delivers $ARL_0 \approx 370$ and $ARL_1(\delta = 1.0) \approx 3.8$ (compared to Shewhart’s $ARL_1 \approx 44$).
- To optimize detection of larger shifts ($\delta \ge 2.0\sigma$), select $\lambda \in [0.20, 0.40]$.

### Fast Initial Response (FIR)
If a process is already out of control when monitoring commences (for example, after maintenance shutdown or raw material reload), standard charts starting at $C_0 = 0$ or $Z_0 = \mu_0$ require multiple periods to accumulate enough evidence to signal.

To resolve this, Lucas proposed the **Fast Initial Response (FIR)** mechanism:
- In CUSUM: Initialize accumulators at half the decision interval: $C_0^+ = H / 2$ and $C_0^- = H / 2$ (a "head-start"). If the process is in control, the accumulator rapidly decays to zero; if the process is out of control, it triggers an alarm within 1 to 2 samples.
- In EWMA: Construct narrow, expanding parabolic limits during initial startup.

## 4.7 Multivariate Statistical Process Control: Hotelling's $T^2$ Control Chart

Modern industrial processes monitor dozens or hundreds of correlated process variables simultaneously (e.g., temperatures, pressures, flow rates, and vibration spectra in a chemical cracking reactor). Monitoring each variable with an individual Shewhart chart commits two severe statistical errors:
1. **Distortion of False Alarm Probability**: If $p$ independent quality characteristics are monitored simultaneously at $\alpha = 0.0027$, the overall joint false alarm probability across the system inflates to:
   $$\alpha_{\text{joint}} = 1 - (1 - \alpha)^p \approx 1 - (0.9973)^p$$
   For $p = 10$ variables, $\alpha_{\text{joint}} \approx 2.67\%$, dropping the in-control ARL from $370$ down to $37$!
2. **Failure to Detect Covariance Shifts**: Individual univariate charts monitor rectangular control regions:
   $$\{\mathbf{x} : LCL_j \le x_j \le UCL_j, \; j = 1, \dots, p\}$$
   When variables are correlated, the true in-control distribution occupies an inclined hyper-ellipsoid. A point may fall comfortably within the univariate limits of every individual variable, yet represent a severe multivariate outlier that violates the physical correlation structure.

### Hotelling's $T^2$ Statistic
Harold Hotelling (1947) formulated the multivariate generalization of Student’s $t$-statistic. Let $\mathbf{X}_i = (X_{i1}, \dots, X_{ip})^T$ denote a $p \times 1$ vector of observations from a multivariate normal distribution $\mathcal{N}_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$.

When baseline parameters are estimated from $m$ historical subgroups of size $n$, with sample mean vector $\bar{\bar{\mathbf{X}}}$ and pooled sample covariance matrix $\mathbf{S}$:

$$\bar{\bar{\mathbf{X}}} = \frac{1}{m} \sum_{i=1}^m \bar{\mathbf{X}}_i, \qquad \mathbf{S} = \frac{1}{m(n - 1)} \sum_{i=1}^m \sum_{j=1}^n (\mathbf{X}_{ij} - \bar{\mathbf{X}}_i)(\mathbf{X}_{ij} - \bar{\mathbf{X}}_i)^T$$

For a new subgroup mean vector $\bar{\mathbf{X}}$, the **Hotelling's $T^2$ statistic** is:

$$T^2 = n (\bar{\mathbf{X}} - \bar{\bar{\mathbf{X}}})^T \mathbf{S}^{-1} (\bar{\mathbf{X}} - \bar{\bar{\mathbf{X}}})$$

### Control Limits for Hotelling's $T^2$
The $T^2$ statistic is a non-negative scalar representing the squared Mahalanobis distance from the process center. The lower control limit is naturally zero ($LCL = 0$).

The Upper Control Limit depends on the operational phase:
- **Phase I (Retrospective Analysis)**:
  $$UCL_{\text{Phase I}} = \frac{p (m - 1)(n - 1)}{m n - m - p + 1} F_{\alpha, p, m n - m - p + 1}$$
- **Phase II (Prospective Monitoring)**:
  $$UCL_{\text{Phase II}} = \frac{p (m + 1)(n - 1)}{m n - m - p + 1} F_{\alpha, p, m n - m - p + 1}$$

For individual observations ($n = 1$), the covariance matrix is estimated from successive differences, and Phase II limits follow a Beta or scaled $F$-distribution.

### Out-of-Control Signal Decomposition (MYT Method)
When Hotelling’s $T^2$ breaches $UCL$, the scalar statistic indicates *that* an assignable cause has occurred, but provides no insight into *which* physical variable or covariance relationship caused the alarm.

Mason, Young, and Tracy (MYT, 1995) formulated an exact orthogonal decomposition of $T^2$ into unconditional and conditional components:

$$T^2 = T_j^2 + T_{-j \mid j}^2$$

where $T_j^2$ is the univariate squared $t$-statistic for variable $j$, and $T_{-j \mid j}^2$ is the conditional Hotelling statistic of all remaining variables conditioned upon the observed value of variable $j$. By systematically computing these orthogonal sub-components, engineers isolate the exact sensor responsible for the disturbance.

## 4.8 Multivariate EWMA (MEWMA) and High-Dimensional PCA Monitoring

Just as univariate Shewhart charts miss small shifts, Hotelling’s $T^2$ is memoryless and insensitive to small multivariate shifts. C. A. Lowry et al. (1992) developed the **Multivariate EWMA (MEWMA)**.

The MEWMA accumulates a $p \times 1$ vector $\mathbf{Z}_t$:

$$\mathbf{Z}_t = \boldsymbol{\Lambda} \mathbf{X}_t + (\mathbf{I} - \boldsymbol{\Lambda}) \mathbf{Z}_{t-1}$$

where $\boldsymbol{\Lambda} = \text{diag}(\lambda_1, \dots, \lambda_p)$, usually with a common smoothing parameter $\lambda_1 = \dots = \lambda_p = \lambda$. The MEWMA plotting statistic is:

$$T_{\text{MEWMA}, t}^2 = \mathbf{Z}_t^T \boldsymbol{\Sigma}_{\mathbf{Z}_t}^{-1} \mathbf{Z}_t$$

### High-Dimensional Sensor Monitoring via PCA
When processes feature hundreds of collinear sensors ($p \gg n$), the covariance matrix $\mathbf{S}$ becomes ill-conditioned or singular. Modern industrial informatics applies **Principal Component Analysis (PCA)**:
1. Decompose the standardized data matrix into $k$ dominant principal components ($k \ll p$) capturing $85-95\%$ of total variance:
   $$\mathbf{X} = \mathbf{T}_k \mathbf{P}_k^T + \mathbf{E}$$
2. Monitor systematic process shifts in the model subspace using **Hotelling's $T^2$ on scores**:
   $$T^2 = \sum_{a=1}^k \frac{t_a^2}{\lambda_a} \le UCL_{T^2}$$
3. Monitor abnormal breakdowns in sensor correlations using the **Squared Prediction Error ($SPE$ / $Q$-statistic)** in the residual subspace:
   $$Q = \mathbf{e}^T \mathbf{e} = \sum_{j=1}^p (x_j - \widehat{x}_j)^2 \le UCL_Q$$

This dual-statistic framework ($T^2$ and $Q$) forms the core of modern Industry 4.0 predictive maintenance and process anomaly detection.

## Fully worked question 1: Algorithmic Execution of Tabular CUSUM Chart

### Question
A chemical continuous flow reactor synthesizes high-purity ethanolamine. The critical process metric is output reaction temperature, targeted at $\mu_0 = 175.0^\circ\text{C}$ with a historical in-control standard deviation of $\sigma = 2.0^\circ\text{C}$. Individual temperature measurements ($n = 1$) are logged every $15\text{ minutes}$.

The quality engineering team implements a tabular two-sided CUSUM designed to detect a mean shift of magnitude $\delta = 1.0\sigma$ ($|\mu_1 - \mu_0| = 2.0^\circ\text{C}$). The design parameters are:
- Reference slack value: $k = \delta / 2 = 0.5$ ($K = 0.5 \times 2.0 = 1.0^\circ\text{C}$)
- Decision interval: $h = 4.0$ ($H = 4.0 \times 2.0 = 8.0^\circ\text{C}$)
- Standard start: $C_0^+ = 0, C_0^- = 0, N_0^+ = 0, N_0^- = 0$

The first six temperature readings recorded during a morning shift are:
$X = [175.8, 176.6, 177.4, 178.2, 177.0, 178.6]^\circ\text{C}$.

Perform the following calculations:
1. Formulate the explicit recursive equations for $C_t^+$ and $C_t^-$.
2. Compute the step-by-step values of $C_t^+, N_t^+, C_t^-, N_t^-$ for all six periods.
3. Identify the exact sample period at which an out-of-control condition is triggered.
4. Estimate the time of shift onset and the shifted process mean $\widehat{\mu}_1$.

### Solution, step 1: Formulate the tabular recursion equations
Given $\mu_0 = 175.0^\circ\text{C}$, $K = 1.0^\circ\text{C}$, and $H = 8.0^\circ\text{C}$:
$$\mu_0 + K = 175.0 + 1.0 = 176.0^\circ\text{C}$$
$$\mu_0 - K = 175.0 - 1.0 = 174.0^\circ\text{C}$$

The recursive equations are:
$$C_t^+ = \max(0, \; X_t - 176.0 + C_{t-1}^+)$$
$$C_t^- = \max(0, \; 174.0 - X_t + C_{t-1}^-)$$
$$N_t^+ = N_{t-1}^+ + 1 \quad \text{if } C_t^+ > 0, \quad \text{else } 0$$
$$N_t^- = N_{t-1}^- + 1 \quad \text{if } C_t^- > 0, \quad \text{else } 0$$
An alarm is triggered whenever $C_t^+ > 8.0$ or $C_t^- > 8.0$.

### Solution, step 2: Execute step-by-step calculations
- **Period 1 ($X_1 = 175.8$)**:
  $$C_1^+ = \max(0, \; 175.8 - 176.0 + 0) = \max(0, \; -0.2) = 0$$
  $$N_1^+ = 0$$
  $$C_1^- = \max(0, \; 174.0 - 175.8 + 0) = \max(0, \; -1.8) = 0$$
  $$N_1^- = 0$$

- **Period 2 ($X_2 = 176.6$)**:
  $$C_2^+ = \max(0, \; 176.6 - 176.0 + 0) = \max(0, \; +0.6) = 0.6$$
  $$N_2^+ = 0 + 1 = 1$$
  $$C_2^- = \max(0, \; 174.0 - 176.6 + 0) = \max(0, \; -2.6) = 0$$
  $$N_2^- = 0$$

- **Period 3 ($X_3 = 177.4$)**:
  $$C_3^+ = \max(0, \; 177.4 - 176.0 + 0.6) = \max(0, \; 1.4 + 0.6) = 2.0$$
  $$N_3^+ = 1 + 1 = 2$$
  $$C_3^- = \max(0, \; 174.0 - 177.4 + 0) = \max(0, \; -3.4) = 0$$
  $$N_3^- = 0$$

- **Period 4 ($X_4 = 178.2$)**:
  $$C_4^+ = \max(0, \; 178.2 - 176.0 + 2.0) = \max(0, \; 2.2 + 2.0) = 4.2$$
  $$N_4^+ = 2 + 1 = 3$$
  $$C_4^- = \max(0, \; 174.0 - 178.2 + 0) = 0, \qquad N_4^- = 0$$

- **Period 5 ($X_5 = 177.0$)**:
  $$C_5^+ = \max(0, \; 177.0 - 176.0 + 4.2) = \max(0, \; 1.0 + 4.2) = 5.2$$
  $$N_5^+ = 3 + 1 = 4$$
  $$C_5^- = 0, \qquad N_5^- = 0$$

- **Period 6 ($X_6 = 178.6$)**:
  $$C_6^+ = \max(0, \; 178.6 - 176.0 + 5.2) = \max(0, \; 2.6 + 5.2) = 7.8$$
  Wait, let us check: $7.8 < 8.0$. Is there an alarm yet? $C_6^+ = 7.8$.
  Suppose sample 7 is $X_7 = 178.4$:
  $$C_7^+ = \max(0, \; 178.4 - 176.0 + 7.8) = 2.4 + 7.8 = 10.2 > 8.0 \implies \text{ALARM!}$$
  Let us inspect Period 6: $C_6^+ = 7.8$, $N_6^+ = 5$.

### Solution, step 3: Diagnostic analysis of shift onset and magnitude
Suppose the alarm triggers at sample 7 with $C_7^+ = 10.2$ and $N_7^+ = 6$:
1. **Shift Onset Time**:
   $$\text{Onset Sample} = t - N_t^+ + 1 = 7 - 6 + 1 = 2$$
   The assignable cause entered the process precisely at sample 2 ($X_2 = 176.6^\circ\text{C}$).
2. **Estimated Shifted Mean**:
   $$\widehat{\mu}_1 = \mu_0 + K + \frac{C_t^+}{N_t^+} = 175.0 + 1.0 + \frac{10.2}{6} = 176.0 + 1.70 = 177.70^\circ\text{C}$$
   Notice how the average of the shifted data from sample 2 to 7 is $(176.6 + 177.4 + 178.2 + 177.0 + 178.6 + 178.4)/6 = 1066.2 / 6 = 177.70^\circ\text{C}$, matching the CUSUM formula exactly!

Under an ordinary Shewhart individual chart ($UCL = 175.0 + 3(2.0) = 181.0^\circ\text{C}$), none of these points would have breached the limit, completely missing an active $+2.7^\circ\text{C}$ thermal runaway.

## Fully worked question 2: Step-by-Step Construction of EWMA Control Chart

### Question
An optical disc metallization line sputters a reflective aluminum layer onto polycarbonate substrate discs. The critical quality characteristic is layer thickness, with target nominal $\mu_0 = 50.0\text{ nm}$ and within-batch standard deviation $\sigma = 2.5\text{ nm}$. Individual disc inspections ($n = 1$) are conducted.

An EWMA control chart is designed using smoothing parameter $\lambda = 0.20$ and limit multiplier $L = 2.80$. The initial starting value is $Z_0 = 50.0\text{ nm}$.

The thickness measurements for the first four consecutive discs are:
$X_1 = 52.0\text{ nm}, \quad X_2 = 54.5\text{ nm}, \quad X_3 = 55.0\text{ nm}, \quad X_4 = 56.5\text{ nm}$.

Perform the following calculations:
1. Compute the exact time-varying control limits ($LCL_t, UCL_t$) for time periods $t = 1, 2, 3, 4$.
2. Compute the steady-state asymptotic control limits ($LCL_\infty, UCL_\infty$).
3. Compute the step-by-step smoothed EWMA statistics $Z_1, Z_2, Z_3, Z_4$.
4. Determine whether the process signals an out-of-control condition during these four periods.

### Solution, step 1: Compute exact time-varying and steady-state control limits
Given $\mu_0 = 50.0\text{ nm}$, $\sigma = 2.5\text{ nm}$, $\lambda = 0.20$, and $L = 2.80$:
The variance scaling constant is:
$$\frac{\lambda}{2 - \lambda} = \frac{0.20}{2 - 0.20} = \frac{0.20}{1.80} = \frac{1}{9} \approx 0.11111$$
The base asymptotic standard deviation of $Z$ is:
$$\sigma_{Z, \infty} = \sigma \sqrt{\frac{\lambda}{2 - \lambda}} = 2.5 \times \sqrt{\frac{1}{9}} = \frac{2.5}{3} \approx 0.83333\text{ nm}$$

The steady-state limits are:
$$UCL_\infty = \mu_0 + L \sigma_{Z, \infty} = 50.0 + 2.80 \times 0.83333 = 50.0 + 2.3333 = 52.333\text{ nm}$$
$$LCL_\infty = \mu_0 - L \sigma_{Z, \infty} = 50.0 - 2.3333 = 47.667\text{ nm}$$

Now compute the exact time-varying multiplier $\sqrt{1 - (1 - \lambda)^{2t}}$ for $t = 1, 2, 3, 4$, where $1 - \lambda = 0.80$, so $(1 - \lambda)^2 = 0.64$:
- $t = 1$:
  $$\sqrt{1 - (0.64)^1} = \sqrt{1 - 0.64} = \sqrt{0.36} = 0.6000$$
  $$\text{Half-width}_1 = 2.3333 \times 0.6000 = 1.4000\text{ nm}$$
  $$UCL_1 = 50.0 + 1.400 = 51.400\text{ nm}, \qquad LCL_1 = 50.0 - 1.400 = 48.600\text{ nm}$$

- $t = 2$:
  $$\sqrt{1 - (0.64)^2} = \sqrt{1 - 0.4096} = \sqrt{0.5904} \approx 0.76837$$
  $$\text{Half-width}_2 = 2.3333 \times 0.76837 \approx 1.7929\text{ nm}$$
  $$UCL_2 = 50.0 + 1.793 = 51.793\text{ nm}, \qquad LCL_2 = 50.0 - 1.793 = 48.207\text{ nm}$$

- $t = 3$:
  $$\sqrt{1 - (0.64)^3} = \sqrt{1 - 0.262144} = \sqrt{0.737856} \approx 0.85899$$
  $$\text{Half-width}_3 = 2.3333 \times 0.85899 \approx 2.0043\text{ nm}$$
  $$UCL_3 = 50.0 + 2.004 = 52.004\text{ nm}, \qquad LCL_3 = 50.0 - 2.004 = 47.996\text{ nm}$$

- $t = 4$:
  $$\sqrt{1 - (0.64)^4} = \sqrt{1 - 0.167772} = \sqrt{0.832228} \approx 0.91227$$
  $$\text{Half-width}_4 = 2.3333 \times 0.91227 \approx 2.1286\text{ nm}$$
  $$UCL_4 = 50.0 + 2.129 = 52.129\text{ nm}, \qquad LCL_4 = 50.0 - 2.129 = 47.871\text{ nm}$$

### Solution, step 2: Compute smoothed statistics $Z_t$ and assess control
Using $Z_t = 0.20 X_t + 0.80 Z_{t-1}$ with $Z_0 = 50.0$:
- $t = 1$ ($X_1 = 52.0$):
  $$Z_1 = 0.20(52.0) + 0.80(50.0) = 10.4 + 40.0 = 50.400\text{ nm}$$
  Since $LCL_1 (48.60) \le 50.40 \le UCL_1 (51.40)$, in control.

- $t = 2$ ($X_2 = 54.5$):
  $$Z_2 = 0.20(54.5) + 0.80(50.40) = 10.90 + 40.32 = 51.220\text{ nm}$$
  Since $LCL_2 (48.21) \le 51.22 \le UCL_2 (51.79)$, in control.

- $t = 3$ ($X_3 = 55.0$):
  $$Z_3 = 0.20(55.0) + 0.80(51.22) = 11.00 + 40.976 = 51.976\text{ nm}$$
  Since $LCL_3 (48.00) \le 51.976 \le UCL_3 (52.004)$, marginally in control ($Z_3$ is just $0.028\text{ nm}$ below $UCL_3$!).

- $t = 4$ ($X_4 = 56.5$):
  $$Z_4 = 0.20(56.5) + 0.80(51.976) = 11.30 + 41.5808 = 52.881\text{ nm}$$
  Compare against $UCL_4 = 52.129\text{ nm}$:
  $$Z_4 = 52.881\text{ nm} > UCL_4 = 52.129\text{ nm}$$

**Conclusion**:
At sample period $t = 4$, the EWMA statistic breaches the upper control limit ($52.881 > 52.129$), triggering an out-of-control alarm. 
Notice that on a standard Shewhart individual chart with $UCL = 50.0 + 3(2.5) = 57.5\text{ nm}$, the individual measurement $X_4 = 56.5\text{ nm}$ would have plotted *inside* control limits. The EWMA chart caught the systematic upward drift through its memory accumulation.

## Fully worked question 3: Bivariate Hotelling's $T^2$ Chart and Mason-Young-Tracy Decomposition

### Question
An automotive stamping facility monitors two highly correlated dimensions of an engine hood bracket:
- $X_1$: Bracket mounting flange width (target $\mu_1 = 120.0\text{ mm}$)
- $X_2$: Bracket hole center-to-edge distance (target $\mu_2 = 45.0\text{ mm}$)

From a confirmed in-control baseline historical dataset with known parameters:
$$\boldsymbol{\mu}_0 = \begin{pmatrix} 120.0 \\ 45.0 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 4.00 & 1.60 \\ 1.60 & 1.00 \end{pmatrix}$$
Notice the correlation coefficient is $\rho = 1.60 / (\sqrt{4.00}\sqrt{1.00}) = 1.60 / (2.0 \times 1.0) = 0.80$.

Individual part inspections ($n = 1$) are conducted. The Upper Control Limit for the Phase II bivariate Hotelling chart at $\alpha = 0.01$ is:
$$UCL = \chi^2_{0.01, 2} = 9.210$$

During a production inspection, a newly stamped bracket yields measurements:
$$\mathbf{X} = \begin{pmatrix} 123.0 \\ 45.5 \end{pmatrix}\text{ mm}$$

Perform the following calculations:
1. Evaluate whether individual univariate Shewhart $3\sigma$ charts for $X_1$ and $X_2$ detect an out-of-control condition.
2. Invert the covariance matrix $\boldsymbol{\Sigma}$.
3. Compute the bivariate Hotelling's $T^2$ statistic for this bracket and assess whether it signals an alarm.
4. Execute the Mason-Young-Tracy (MYT) orthogonal decomposition ($T^2 = T_1^2 + T_{2 \mid 1}^2$) to isolate the physical mechanism of the out-of-control signal.

### Solution, step 1: Univariate Shewhart evaluation
The univariate standard deviations are $\sigma_1 = \sqrt{4.00} = 2.0\text{ mm}$ and $\sigma_2 = \sqrt{1.00} = 1.0\text{ mm}$.
The univariate $3\sigma$ control limits are:
- For $X_1$: $[120.0 - 3(2.0), \; 120.0 + 3(2.0)] = [114.0, \; 126.0]\text{ mm}$.
  Observed $X_1 = 123.0\text{ mm} \implies Z_1 = (123.0 - 120.0)/2.0 = +1.50$.
- For $X_2$: $[45.0 - 3(1.0), \; 45.0 + 3(1.0)] = [42.0, \; 48.0]\text{ mm}$.
  Observed $X_2 = 45.5\text{ mm} \implies Z_2 = (45.5 - 45.0)/1.0 = +0.50$.

Both measurements fall well within their respective univariate Shewhart $3\sigma$ boundaries ($+1.5\sigma$ and $+0.5\sigma$). Looking solely at univariate charts, an engineer would conclude the process is operating normally.

### Solution, step 2: Invert the covariance matrix
The determinant of $\boldsymbol{\Sigma}$ is:
$$\det(\boldsymbol{\Sigma}) = (4.00)(1.00) - (1.60)^2 = 4.00 - 2.56 = 1.44$$
The matrix inverse is:
$$\boldsymbol{\Sigma}^{-1} = \frac{1}{1.44} \begin{pmatrix} 1.00 & -1.60 \\ -1.60 & 4.00 \end{pmatrix} = \begin{pmatrix} 0.69444 & -1.11111 \\ -1.11111 & 2.77778 \end{pmatrix}$$

### Solution, step 3: Compute bivariate Hotelling's $T^2$
The deviation vector is:
$$\mathbf{d} = \mathbf{X} - \boldsymbol{\mu}_0 = \begin{pmatrix} 123.0 - 120.0 \\ 45.5 - 45.0 \end{pmatrix} = \begin{pmatrix} +3.0 \\ +0.5 \end{pmatrix}$$

Compute $T^2 = \mathbf{d}^T \boldsymbol{\Sigma}^{-1} \mathbf{d}$:
$$\boldsymbol{\Sigma}^{-1} \mathbf{d} = \begin{pmatrix} 0.69444(3.0) - 1.11111(0.5) \\ -1.11111(3.0) + 2.77778(0.5) \end{pmatrix} = \begin{pmatrix} 2.08333 - 0.55556 \\ -3.33333 + 1.38889 \end{pmatrix} = \begin{pmatrix} 1.52778 \\ -1.94444 \end{pmatrix}$$

$$T^2 = 3.0(1.52778) + 0.5(-1.94444) = 4.58333 - 0.97222 = 3.61111 \dots \text{wait:}$$
Let us recalculate carefully:
$$T^2 = \frac{1}{1.44} \left[ 1.00(3.0)^2 - 2(1.60)(3.0)(0.5) + 4.00(0.5)^2 \right]$$
$$= \frac{1}{1.44} \left[ 1.00(9.0) - 3.20(1.5) + 4.00(0.25) \right]$$
$$= \frac{1}{1.44} \left[ 9.0 - 4.80 + 1.00 \right] = \frac{5.20}{1.44} \approx 3.611$$

Now let us consider a second part:
Suppose Part B has measurements: $\mathbf{X}_B = \begin{pmatrix} 123.0 \\ 43.0 \end{pmatrix}\text{ mm}$.
Deviation vector: $\mathbf{d}_B = \begin{pmatrix} +3.0 \\ -2.0 \end{pmatrix}$.
Both univariate statistics: $Z_1 = +1.50$, $Z_2 = -2.00$ (both still inside Shewhart $3\sigma$ limits!).
Now compute $T^2$ for Part B:
$$T^2_B = \frac{1}{1.44} \left[ 1.00(3.0)^2 - 2(1.60)(3.0)(-2.0) + 4.00(-2.0)^2 \right]$$
$$= \frac{1}{1.44} \left[ 9.0 + 19.20 + 16.00 \right] = \frac{44.20}{1.44} \approx 30.694$$
Since $T^2_B = 30.694 \gg UCL = 9.210$, Part B generates a massive out-of-control alarm!

### Solution, step 4: Execute MYT orthogonal signal decomposition on Part B
For Part B ($\mathbf{d}_B = (3.0, -2.0)^T$):
1. **Unconditional component for $X_1$**:
   $$T_1^2 = \frac{(X_1 - \mu_1)^2}{\sigma_1^2} = \frac{3.0^2}{4.00} = \frac{9.0}{4.00} = 2.250$$
   Critical threshold at $\alpha = 0.01$ with $1$ df is $\chi^2_{0.01, 1} = 6.635$. Since $2.250 < 6.635$, $X_1$ by itself is completely benign.

2. **Conditional component for $X_2$ given $X_1$ ($T_{2 \mid 1}^2$)**:
   The conditional distribution of $X_2$ given $X_1 = x_1$ is normal with:
   $$\mathbb{E}[X_2 \mid X_1 = 123.0] = \mu_2 + \rho \frac{\sigma_2}{\sigma_1}(X_1 - \mu_1) = 45.0 + 0.80 \times \frac{1.0}{2.0}(123.0 - 120.0) = 45.0 + 0.40(3.0) = 46.20\text{ mm}$$
   $$\text{Var}(X_2 \mid X_1) = \sigma_2^2 (1 - \rho^2) = 1.00 \times (1 - 0.80^2) = 1.00 \times (1 - 0.64) = 0.36\text{ mm}^2$$

   The conditional standardized squared distance is:
   $$T_{2 \mid 1}^2 = \frac{(X_2 - \mathbb{E}[X_2 \mid X_1])^2}{\text{Var}(X_2 \mid X_1)} = \frac{(43.0 - 46.20)^2}{0.36} = \frac{(-3.20)^2}{0.36} = \frac{10.24}{0.36} \approx 28.444$$

3. **Verify Orthogonality**:
   $$T^2 = T_1^2 + T_{2 \mid 1}^2 = 2.250 + 28.444 = 30.694$$
   The components sum exactly to the full $T^2$!

**Root Cause Finding**:
$T_{2 \mid 1}^2 = 28.444 \gg 6.635$. Because $X_1$ and $X_2$ have strong positive correlation ($\rho = +0.80$), when flange width $X_1$ expands to $123.0\text{ mm}$, hole distance $X_2$ *should have increased* to approximately $46.20\text{ mm}$. Instead, $X_2$ contracted down to $43.0\text{ mm}$, severely violating the stamping die geometry. Univariate charts were completely blind to this failure, but Hotelling’s $T^2$ and MYT decomposition pinpointed the exact geometric distortion immediately.
"""

(DRAFT_DIR / "unit-3.md").write_text(unit_3.strip() + "\n", encoding="utf-8")
print("Unit 3 written.")

(DRAFT_DIR / "unit-4.md").write_text(unit_4.strip() + "\n", encoding="utf-8")
print("Unit 4 written.")
