# Unit 3: Control Charts for Attributes: Proportion, Nonconforming Units & Defect Count Models

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

## 3.9 Demerit Control Charts (Quality Score Rating Systems)

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

## 3.12 Operating Characteristic (OC) Functions for Attribute Control Charts

Just as variables control charts have Operating Characteristic (OC) curves, the statistical performance of attribute charts ($p$-charts and $c$-charts) is characterized by their ability to discriminate between in-control and out-of-control conditions.

### OC Curve for the $p$-Chart
For a $p$-chart with constant sample size $n$ and control limits $[LCL, UCL]$, suppose the true fraction nonconforming shifts from the baseline $p_0$ to an out-of-control state $p_1$.

The probability of Type II error $\beta$ (the probability that a sample proportion $\widehat{p}$ plots within the control limits despite the shift) is given by the cumulative binomial distribution:

$$\beta(p_1) = P(LCL \le \widehat{p} \le UCL \mid p_1) = P(n \cdot LCL \le D \le n \cdot UCL \mid p_1) = \sum_{d = \lceil n \cdot LCL \rceil}^{\lfloor n \cdot UCL \rfloor} \binom{n}{d} p_1^d (1 - p_1)^{n-d}$$

The statistical power to detect the shift on any given sample is $1 - \beta(p_1)$, and the Average Run Length is:

$$ARL_1 = \frac{1}{1 - \beta(p_1)}$$

Because the Binomial distribution is discrete, the in-control Type I error rate $\alpha = 1 - \beta(p_0)$ does not exactly equal the theoretical $0.0027$ of Gaussian charts, fluctuating significantly depending on whether $n \bar{p}$ is small or large.

### OC Curve for the $c$-Chart
For a $c$-chart monitoring defect counts with limits $[LCL, UCL]$ derived from in-control mean $\bar{c}$, suppose the true defect rate shifts to $c_1$. The probability of Type II error is:

$$\beta(c_1) = P(LCL \le C \le UCL \mid c_1) = \sum_{c = \lceil LCL \rceil}^{\lfloor UCL \rfloor} \frac{e^{-c_1} c_1^c}{c!}$$

Plotting $\beta(c_1)$ against $c_1$ produces the OC curve for the defect count chart. As with the $p$-chart, small values of $\bar{c}$ produce highly asymmetric OC curves with low power against downward shifts (quality improvements), reinforcing the necessity of using exact Poisson probability limits or switching to Time-Between-Events (TBE) charts in high-yield processes.

## 3.13 Conversion Between Defect Metrics: DPU, DPO, and DPMO

In Six Sigma enterprise quality frameworks, attribute defect data must be normalized to enable cross-departmental benchmarking across products of radically differing complexity. A printed circuit board with $2,000$ solder joints cannot be compared directly with a stamped bracket containing only $4$ holes using raw defect counts.

To normalize defect data across varying assembly complexity:
1. **Defects Per Unit ($DPU$)**: The average number of defects observed per finished product unit:
   $$DPU = \frac{\text{Total Defects Found}}{\text{Total Units Inspected}} = \frac{D}{N}$$
2. **Defects Per Opportunity ($DPO$)**: The ratio of observed defects to the total number of distinct opportunities for defect generation across the inspected units:
   $$DPO = \frac{\text{Total Defects Found}}{\text{Total Units Inspected} \times \text{Defect Opportunities per Unit}} = \frac{D}{N \times O}$$
   where $O$ is the number of opportunities for error per product unit.
3. **Defects Per Million Opportunities ($DPMO$)**: Normalizing $DPO$ to a standard scale of one million:
   $$DPMO = DPO \times 1,000,000$$

Converting $DPMO$ to the equivalent Six Sigma quality level via the inverse standard normal distribution:
$$\text{Sigma Level} = \Phi^{-1}(1 - DPMO / 1,000,000) + 1.5$$
This mathematical conversion bridges the gap between discrete attribute counts and continuous Six Sigma process capability metrics.

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
