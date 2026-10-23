#!/usr/bin/env python3
"""
Generate Units 5 and 6 for Industrial and Official Statistics.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_5 = r"""# Unit 5: Acceptance Sampling Quality Assurance: Attributes & Variables Inspection Systems

## 5.1 Philosophy and Economics of Acceptance Sampling

Acceptance sampling constitutes a statistical decision-making framework wherein incoming lots of raw materials, manufactured sub-assemblies, or finished outbound products are inspected to determine whether the entire lot should be accepted or rejected. Acceptance sampling is applied at the contractual boundary between an upstream supplier and a downstream customer, or between consecutive manufacturing departments.

An industrial enterprise confronting lot quality evaluation has three strategic inspection alternatives:
1. **Zero Inspection (No Inspection)**: Accept all lots without testing. This strategy is economically rational only when the supplier’s process capability is exceptionally high ($C_{pk} \ge 2.0$) and verified through ongoing statistical process control (dock-to-stock certified suppliers), or when the financial and safety consequence of a defect escaping into production is negligible compared to inspection costs.
2. **100% Inspection (Screening / Sorting)**: Every single unit in the lot is tested, with nonconforming items removed. While superficially attractive, 100% inspection has severe real-world limitations:
   - When quality evaluation requires **destructive testing** (such as tensile strength testing of bolts, burst testing of pressure vessels, or chemical assaying), 100% inspection destroys the entire lot, leaving zero product for sale.
   - 100% inspection is financially prohibitive for high-volume, low-cost manufactured items (such as resistors, fasteners, or plastic bottle caps).
   - Because of human and sensor fatigue, boredom, and inspection error, real 100% manual inspection typically achieves only $80\%$ to $90\%$ defect detection efficiency—it does *not* guarantee zero defect escapes!
3. **Acceptance Sampling (Statistical Lot Sampling)**: Inspecting a representative random sample of size $n$ drawn from a lot of size $N$, and comparing the number of observed nonconforming items $d$ against an acceptance threshold $c$.

Crucially, **acceptance sampling is not a process control tool**: it does not improve the quality of the manufactured product, nor does it provide feedback to stabilize machinery. Its sole purpose is **lot sentencing**—acting as an audit filter to protect the customer from receiving unacceptably poor lots, while providing the vendor with an economic incentive to maintain high manufacturing capability.

## 5.2 Single Sampling Plans for Attributes $(N, n, c)$

In a **Single Sampling Plan for Attributes**, the inspection protocol is defined by three integers:
- $N$: The total lot size.
- $n$: The random sample size drawn from the lot ($n < N$).
- $c$: The maximum allowable number of nonconforming items in the sample (acceptance number).

The decision rule is straightforward:
- Draw $n$ units at random from the lot of size $N$.
- Inspect all $n$ units and count the number of nonconforming units $D$.
- If $D \le c$: **Accept the entire lot of size $N$**.
- If $D > c$: **Reject the entire lot of size $N$** (the lot is returned to the supplier or subjected to 100% rectifying sorting at supplier expense).

### The Exact Sampling Model: The Hypergeometric Distribution
Because the lot size $N$ is finite and sampling is conducted without replacement, the exact probability of observing precisely $d$ nonconforming units in a sample of size $n$ drawn from a lot containing $M = N p$ total nonconforming units is given by the Hypergeometric distribution:

$$P(D = d) = \frac{\binom{N p}{d} \binom{N - N p}{n - d}}{\binom{N}{n}}, \qquad d = 0, 1, \dots, \min(n, N p)$$

The probability of lot acceptance $P_a(p)$ is the cumulative hypergeometric probability:

$$P_a(p) = \sum_{d=0}^c \frac{\binom{N p}{d} \binom{N - N p}{n - d}}{\binom{N}{n}}$$

### Binomial and Poisson Approximations
When the sample size $n$ is small relative to the lot size ($n / N \le 0.10$), the sampling process behaves essentially like sampling with replacement, and the Hypergeometric distribution is closely approximated by the **Binomial distribution**:

$$P_a(p) \approx \sum_{d=0}^c \binom{n}{d} p^d (1 - p)^{n-d}$$

Furthermore, when the incoming fraction nonconforming $p$ is small ($p \le 0.10$) and $n$ is moderately large ($n \ge 20$), the Binomial distribution can be approximated by the **Poisson distribution** with parameter $\lambda = n p$:

$$P_a(p) \approx \sum_{d=0}^c \frac{e^{-np} (np)^d}{d!}$$

The Poisson approximation is extraordinarily convenient because lot acceptance probabilities depend solely on the single product parameter $\lambda = n p$, enabling the construction of universal master tables and alignment charts.

## 5.3 The Operating Characteristic (OC) Curve

The performance of an acceptance sampling plan across all possible levels of incoming quality $p$ is displayed by its **Operating Characteristic (OC) Curve**. The OC curve plots the probability of lot acceptance $P_a(p)$ on the vertical axis against the true incoming lot fraction nonconforming $p$ on the horizontal axis.

### Type A Versus Type B OC Curves
Quality theory distinguishes two classes of OC curves:
- **Type A OC Curve**: Calculated for an individual, isolated finite lot of size $N$ using the Hypergeometric distribution. It reflects the probability of accepting that specific physical lot.
- **Type B OC Curve**: Calculated for a continuous production stream where incoming lots represent independent batches produced by a stable manufacturing process with constant defect probability $p$. It is calculated using the Binomial (or Poisson) distribution. In industrial contracts, Type B OC curves are standard.

### Properties of the OC Curve
1. If incoming product is perfect ($p = 0$), the lot is accepted with certainty: $P_a(0) = 1.0$.
2. If incoming product is entirely defective ($p = 1.0$), the lot is rejected with certainty: $P_a(1.0) = 0.0$ (for $c < n$).
3. The curve decreases monotonically as incoming defect fraction $p$ increases: poorer quality receives lower acceptance probabilities.
4. **Effect of Sample Size $n$**: Increasing sample size $n$ while keeping the ratio $c / n$ approximately constant increases the steepness (discrimination power) of the OC curve. An "ideal" OC curve would be a vertical step function dropping from $P_a = 1.0$ to $P_a = 0.0$ at a critical quality threshold $p^*$; larger sample sizes $n$ approximate this vertical step more closely, reducing both producer and consumer risks.

## 5.4 Four Core Contractual Parameters: AQL, LTPD, $\alpha$, and $\beta$

A bilateral procurement contract balances two opposing economic risks through four standardized parameters:

1. **Acceptance Quality Limit (AQL, $p_1$)**: The poorest level of quality for the supplier’s process that the consumer considers satisfactory as a process average. AQL represents good quality that should be accepted almost all the time.
2. **Producer's Risk ($\alpha$)**: The probability that a high-quality lot of AQL quality ($p = p_1$) is erroneously rejected by the sampling plan:
   $$\alpha = 1 - P_a(p_1)$$
   By commercial convention, $\alpha$ is typically set at $0.05$ ($5\%$). The supplier has a $95\%$ probability of lot acceptance when delivering at AQL quality.
3. **Lot Tolerance Percent Defective (LTPD / Limiting Quality LQ, $p_2$)**: The designated unsatisfactory level of quality that the consumer emphatically wishes to reject. LTPD represents bad quality.
4. **Consumer's Risk ($\beta$)**: The probability that a poor-quality lot of LTPD quality ($p = p_2$) is erroneously accepted by the sampling plan:
   $$\beta = P_a(p_2)$$
   By commercial convention, $\beta$ is typically set at $0.10$ ($10\%$). The consumer accepts no more than a $10\%$ chance of receiving an LTPD lot.

A properly designed sampling plan $(n, c)$ passes through these two designated operational benchmark points on the OC curve:
$$P_a(p_1) = 1 - \alpha, \qquad P_a(p_2) = \beta$$

## 5.5 Rectifying Inspection Programs: AOQ, AOQL, and ATI

When rejected lots are not scrapped but are instead subjected to **rectifying inspection** (screening), the rejected lots undergo 100% sorting where all nonconforming items are identified and replaced with conforming items.

### Average Outgoing Quality (AOQ)
Suppose incoming lots of size $N$ arrive with defect fraction $p$. Under rectifying inspection:
- Accepted lots (probability $P_a$) contain on average $n$ inspected conforming items and $(N - n) p$ uninspected defective items.
- Rejected lots (probability $1 - P_a$) are 100% sorted, leaving $0$ nonconforming items.

The expected fraction nonconforming in the outgoing product stream is the **Average Outgoing Quality (AOQ)**:

$$AOQ = \frac{p P_a (N - n)}{N} \approx p P_a(p)$$

Notice the mathematical behavior of the AOQ function:
- When incoming quality is pristine ($p \to 0$), $P_a \approx 1.0$, so $AOQ \to 0$.
- When incoming quality is terrible ($p \to 1$), $P_a \to 0$ (all lots are rejected and screened to 100% perfection), so $AOQ \to 0$.
- Between these two extremes, $AOQ(p)$ rises to a distinct mathematical maximum and then declines.

### Average Outgoing Quality Limit (AOQL)
The peak of the AOQ curve is the **Average Outgoing Quality Limit (AOQL)**:

$$AOQL = \max_{0 \le p \le 1} AOQ(p)$$

The AOQL represents the absolute worst-case average defect rate that can ever pass out of the inspection department into downstream production, regardless of how degraded the supplier’s incoming quality becomes!

Using the Poisson approximation where $P_a = \sum_{d=0}^c \frac{e^{-y} y^d}{d!}$ with $y = n p$:
$$AOQ \approx \frac{y P_a(y)}{n} \left(1 - \frac{n}{N}\right)$$
Letting $y_m$ denote the value of $y$ that maximizes $y P_a(y)$, the factor $y_m P_a(y_m)$ is a constant $k_{\text{AOQL}}$ depending solely on acceptance number $c$:

$$AOQL = k_{\text{AOQL}} \left( \frac{1}{n} - \frac{1}{N} \right) \approx \frac{k_{\text{AOQL}}}{n}$$

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Acceptance Number $c$</th>
<th>$y_m$</th>
<th>$P_a(y_m)$</th>
<th>$k_{\text{AOQL}} = y_m P_a(y_m)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>1.000</td>
<td>0.3679</td>
<td>0.3679</td>
</tr>
<tr>
<td>1</td>
<td>1.618</td>
<td>0.5186</td>
<td>0.8391</td>
</tr>
<tr>
<td>2</td>
<td>2.270</td>
<td>0.6039</td>
<td>1.3709</td>
</tr>
<tr>
<td>3</td>
<td>2.950</td>
<td>0.6631</td>
<td>1.9561</td>
</tr>
<tr>
<td>4</td>
<td>3.640</td>
<td>0.7077</td>
<td>2.5760</td>
</tr>
</tbody>
</table>
</div>

### Average Total Inspection (ATI)
The expected total number of units inspected per lot is the **Average Total Inspection (ATI)**:
- If a lot is accepted (probability $P_a$), only the sample of size $n$ is inspected.
- If a lot is rejected (probability $1 - P_a$), all $N$ units in the lot are inspected.

$$ATI = n P_a + N (1 - P_a) = n + (1 - P_a)(N - n)$$

When incoming quality is high ($P_a \approx 1$), $ATI \approx n$. When quality degrades ($P_a \to 0$), $ATI \to N$, imposing massive sorting costs on the manufacturer.

## 5.6 Double, Multiple, and Sequential Sampling Plans

While single sampling is logistically simple, it requires inspecting $n$ units even for lots that are exceptionally pristine or catastrophically bad. **Double Sampling Plans** allow for an intermediate verdict:

A double sampling plan is specified by five parameters: $(n_1, c_1, r_1; n_2, c_2, r_2)$, where typically $r_1 = c_2 + 1$:
1. **Sample 1**: Inspect $n_1$ units from the lot. Count nonconformities $d_1$:
   - If $d_1 \le c_1$: Accept the lot immediately.
   - If $d_1 \ge r_1$: Reject the lot immediately.
   - If $c_1 < d_1 < r_1$: Draw a second sample of size $n_2$.
2. **Sample 2**: Count nonconformities $d_2$ in the second sample. The cumulative defect count is $d_1 + d_2$:
   - If $d_1 + d_2 \le c_2$: Accept the lot.
   - If $d_1 + d_2 \ge r_2 = c_2 + 1$: Reject the lot.

### Average Sample Number (ASN)
The expected number of units inspected per lot under double sampling is the **Average Sample Number (ASN)**:

$$ASN = n_1 + n_2 P(\text{Second sample required}) = n_1 + n_2 P(c_1 < d_1 < r_1)$$

For very good lots ($p \to 0$) or very bad lots ($p \to 1$), the decision is almost always reached on the first sample ($P \approx 0$), so $ASN \approx n_1$. Because $n_1$ is typically $30\%$ to $50\%$ smaller than the equivalent single sample size $n_{\text{single}}$, double sampling delivers substantial inspection labor savings.

### Sequential Sampling (Wald SPRT)
Abraham Wald (1947) generalized multiple sampling into continuous **Sequential Sampling**, where units are inspected one by one ($n = 1, 2, 3, \dots$). After each inspection, the cumulative defect count $d_m$ is plotted against two parallel decision boundaries:

$$\text{Acceptance Boundary: } d_m \le -h_1 + s \cdot m$$
$$\text{Rejection Boundary: } d_m \ge h_2 + s \cdot m$$

where $h_1, h_2$ are intercept constants derived from $(\alpha, \beta)$, and $s$ is the acceptance line slope. Sequential sampling achieves the minimum theoretically possible Average Sample Number among all possible statistical sampling procedures.

## 5.7 Variables Acceptance Sampling: Known and Unknown $\sigma$ Plans

When the quality characteristic is a continuous variable $X \sim \mathcal{N}(\mu, \sigma^2)$ with Upper Specification Limit ($USL$) and Lower Specification Limit ($LSL$), **Variables Acceptance Sampling** provides dramatically higher statistical efficiency than attribute sampling. A variables sampling plan achieving the exact same $(\alpha, \beta)$ protection as an attribute plan typically requires **$70\%$ to $85\%$ fewer inspected parts**!

### The Known-$\sigma$ Plan ($k$-Method)
Suppose the process standard deviation $\sigma$ is known from long-term SPC stability. To protect against an Upper Specification Limit $USL$:
1. Draw a random sample of size $n$.
2. Compute the sample mean $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$.
3. Compute the standardized quality statistic $Z_{USL}$:
   $$Z_{USL} = \frac{USL - \bar{X}}{\sigma}$$
4. **Acceptance Rule**: Accept the lot if $Z_{USL} \ge k$, where $k$ is the critical acceptance constant. Otherwise, reject the lot.

### Mathematical Derivation of Sample Size $n$ and Constant $k$
To satisfy the two contractual conditions:
1. Producer's risk: If incoming lot has defect fraction $p_1 = AQL$, $P_a(p_1) = 1 - \alpha$.
2. Consumer's risk: If incoming lot has defect fraction $p_2 = LTPD$, $P_a(p_2) = \beta$.

Let $Z_{p_1} = \Phi^{-1}(1 - p_1)$ and $Z_{p_2} = \Phi^{-1}(1 - p_2)$. Under the sampling distribution $\bar{X} \sim \mathcal{N}(\mu, \sigma^2/n)$:

$$k = \frac{Z_\alpha Z_{p_2} + Z_\beta Z_{p_1}}{Z_\alpha + Z_\beta}$$

$$n = \left( \frac{Z_\alpha + Z_\beta}{Z_{p_1} - Z_{p_2}} \right)^2$$

where $Z_\alpha = \Phi^{-1}(1 - \alpha)$ and $Z_\beta = \Phi^{-1}(1 - \beta)$.

### Standardized Sampling Systems: MIL-STD-105E and MIL-STD-414
Military standards (formalized in commercial civilian standards ANSI/ASQ Z1.4 for attributes and ANSI/ASQ Z1.9 for variables) establish structured inspection systems indexed by AQL and Lot Size. They incorporate **Dynamic Switching Rules**:
- **Normal Inspection**: Default starting mode.
- **Tightened Inspection**: Invoked when 2 out of 5 consecutive lots are rejected under normal inspection; steepens the OC curve.
- **Reduced Inspection**: Invoked when 10 consecutive lots are accepted under normal inspection with total defects below a threshold limit; cuts sample size by up to $60\%$.
- **Discontinuation Rule**: If 5 consecutive lots remain on tightened inspection, supplier quality is declared unacceptable and contractual shipments are halted.

## Fully worked question 1: Designing an Attribute Single Sampling Plan for Target Risks $(AQL, \alpha, LTPD, \beta)$

### Question
A medical device manufacturer procures titanium spinal fixation screws from an orthopedic machining supplier. The bilateral procurement contract specifies:
- Acceptance Quality Limit: $AQL = p_1 = 0.01$ ($1.0\%$ nonconforming)
- Producer's Risk: $\alpha = 0.05$ (Probability of acceptance $P_a(p_1) = 0.95$)
- Lot Tolerance Percent Defective: $LTPD = p_2 = 0.06$ ($6.0\%$ nonconforming)
- Consumer's Risk: $\beta = 0.10$ (Probability of acceptance $P_a(p_2) = 0.10$)
Incoming lots are large ($N = 10,000$).

Using the Poisson approximation to the binomial distribution:
1. Determine the acceptance number $c$ and sample size $n$ that satisfy both risk constraints.
2. Verify the exact probabilities of acceptance $P_a(p_1)$ and $P_a(p_2)$ under the selected plan.
3. If the supplier delivers a lot with an incoming defect rate of $p = 0.03$, compute the probability that this lot is accepted.

### Solution, step 1: Determine acceptance number $c$ using Poisson ratio tables
Under the Poisson model, let $\lambda_1 = n p_1$ and $\lambda_2 = n p_2$.
The contractual requirements are:
$$P_a(\lambda_1) = \sum_{d=0}^c \frac{e^{-\lambda_1} \lambda_1^d}{d!} = 1 - \alpha = 0.95$$
$$P_a(\lambda_2) = \sum_{d=0}^c \frac{e^{-\lambda_2} \lambda_2^d}{d!} = \beta = 0.10$$

The ratio of the defect levels is:
$$R = \frac{p_2}{p_1} = \frac{0.06}{0.01} = 6.00$$
For any acceptance number $c$, the ratio of the corresponding Poisson parameters is $R(c) = \lambda_{0.10} / \lambda_{0.95}$.
From cumulative Poisson tables:
- For $c = 1$:
  $$\lambda_{0.95} = 0.355, \quad \lambda_{0.10} = 3.890 \implies R(1) = \frac{3.890}{0.355} \approx 10.96 > 6.00$$
- For $c = 2$:
  $$\lambda_{0.95} = 0.818, \quad \lambda_{0.10} = 5.322 \implies R(2) = \frac{5.322}{0.818} \approx 6.51 > 6.00$$
- For $c = 3$:
  $$\lambda_{0.95} = 1.366, \quad \lambda_{0.10} = 6.681 \implies R(3) = \frac{6.681}{1.366} \approx 4.89 < 6.00$$

To provide protection at or better than $R = 6.00$, we must select the smallest integer $c$ whose ratio $R(c) \le 6.00$. Therefore, select **$c = 3$**.

### Solution, step 2: Calculate sample size $n$
Using the consumer's risk benchmark ($\lambda_2 = 6.681$ at $p_2 = 0.06$):
$$n = \frac{\lambda_{0.10}}{p_2} = \frac{6.681}{0.06} \approx 111.35 \implies n = 112$$
Checking producer's risk parameter at $n = 112$:
$$\lambda_1 = n p_1 = 112 \times 0.01 = 1.120$$
Since $1.120 < \lambda_{0.95} (1.366)$, the actual producer's risk $\alpha$ will be strictly less than $0.05$ (meaning $P_a(p_1) > 0.95$, which is favorable to the producer).

Thus, the optimal sampling plan is:
$$\mathbf{n = 112, \quad c = 3}$$

### Solution, step 3: Verify acceptance probabilities and test intermediate quality
1. **At AQL ($p_1 = 0.01$)**:
   $$\lambda_1 = 112 \times 0.01 = 1.12$$
   $$P_a(0.01) = e^{-1.12} \left( 1 + 1.12 + \frac{1.12^2}{2} + \frac{1.12^3}{6} \right)$$
   $$= 0.32628 \times (1 + 1.12 + 0.6272 + 0.2341) = 0.32628 \times 2.9813 \approx 0.9727$$
   Producer's risk is $\alpha = 1 - 0.9727 = 0.0273 = 2.73\%$ (better than the required $5\%$).

2. **At LTPD ($p_2 = 0.06$)**:
   $$\lambda_2 = 112 \times 0.06 = 6.72$$
   $$P_a(0.06) = e^{-6.72} \left( 1 + 6.72 + \frac{6.72^2}{2} + \frac{6.72^3}{6} \right)$$
   $$= 0.0012065 \times (1 + 6.72 + 22.5792 + 50.5774) = 0.0012065 \times 80.8766 \approx 0.0976$$
   Consumer's risk is $\beta = 9.76\%$ (strictly meeting the $\le 10\%$ constraint).

3. **At Intermediate Defect Rate ($p = 0.03$)**:
   $$\lambda = 112 \times 0.03 = 3.36$$
   $$P_a(0.03) = e^{-3.36} \left( 1 + 3.36 + \frac{3.36^2}{2} + \frac{3.36^3}{6} \right)$$
   $$= 0.034735 \times (1 + 3.36 + 5.6448 + 6.3222) = 0.034735 \times 16.3270 \approx 0.5671 = 56.71\%$$
   A lot with $3\%$ defects has a $56.71\%$ chance of acceptance and a $43.29\%$ chance of rejection.

## Fully worked question 2: Rectifying Inspection Analysis: AOQ, AOQL, and ATI Curves

### Question
An automotive wiring harness manufacturer uses a rectifying inspection plan with sample size $n = 80$ and acceptance number $c = 1$ for incoming connector lots of size $N = 2,000$. All rejected lots undergo 100% rectifying screening at supplier expense, with all defective connectors replaced by good units.

Perform the following analyses:
1. Compute the probability of lot acceptance $P_a(p)$ for incoming defect fractions $p \in \{0.005, 0.010, 0.020, 0.030, 0.050\}$.
2. Calculate the Average Outgoing Quality ($AOQ$) for each of these defect levels.
3. Using the theoretical constant $k_{\text{AOQL}} = 0.8391$ for $c = 1$, compute the exact Average Outgoing Quality Limit ($AOQL$).
4. Compute the Average Total Inspection ($ATI$) for each defect level.

### Solution, step 1: Compute $P_a(p)$ across incoming quality levels
Under the Poisson approximation with $n = 80$ and $c = 1$:
$$\lambda = n p = 80 p$$
$$P_a(p) = e^{-\lambda} (1 + \lambda)$$

Evaluating for each $p$:
- **$p = 0.005$**: $\lambda = 80(0.005) = 0.40$.
  $$P_a = e^{-0.40} (1 + 0.40) = 0.67032 \times 1.40 \approx 0.9384$$
- **$p = 0.010$**: $\lambda = 80(0.010) = 0.80$.
  $$P_a = e^{-0.80} (1 + 0.80) = 0.44933 \times 1.80 \approx 0.8088$$
- **$p = 0.020$**: $\lambda = 80(0.020) = 1.60$.
  $$P_a = e^{-1.60} (1 + 1.60) = 0.20190 \times 2.60 \approx 0.5249$$
- **$p = 0.030$**: $\lambda = 80(0.030) = 2.40$.
  $$P_a = e^{-2.40} (1 + 2.40) = 0.09072 \times 3.40 \approx 0.3084$$
- **$p = 0.050$**: $\lambda = 80(0.050) = 4.00$.
  $$P_a = e^{-4.00} (1 + 4.00) = 0.01832 \times 5.00 \approx 0.0916$$

### Solution, step 2: Calculate Average Outgoing Quality ($AOQ$)
The exact AOQ formula is:
$$AOQ = p P_a \frac{N - n}{N} = p P_a \frac{2,000 - 80}{2,000} = p P_a \left(\frac{1,920}{2,000}\right) = 0.96 \cdot p P_a$$

Computing values:
- **$p = 0.005$**: $AOQ = 0.96 \times 0.005 \times 0.9384 = 0.004504 \approx 0.450\%$ ($4,504\text{ PPM}$)
- **$p = 0.010$**: $AOQ = 0.96 \times 0.010 \times 0.8088 = 0.007764 \approx 0.776\%$ ($7,764\text{ PPM}$)
- **$p = 0.020$**: $AOQ = 0.96 \times 0.020 \times 0.5249 = 0.010078 \approx 1.008\%$ ($10,078\text{ PPM}$)
- **$p = 0.030$**: $AOQ = 0.96 \times 0.030 \times 0.3084 = 0.008882 \approx 0.888\%$ ($8,882\text{ PPM}$)
- **$p = 0.050$**: $AOQ = 0.96 \times 0.050 \times 0.0916 = 0.004397 \approx 0.440\%$ ($4,397\text{ PPM}$)

Notice how $AOQ$ peaks near $p = 0.020$ ($1.008\%$) and then declines as poor lots get screened out!

### Solution, step 3: Compute the exact AOQL
For $c = 1$, the peak factor is $k_{\text{AOQL}} = 0.8391$ (occurring at $\lambda_m = 1.618 \implies p_m = 1.618 / 80 = 0.020225$):
$$AOQL = k_{\text{AOQL}} \left( \frac{1}{n} - \frac{1}{N} \right) = 0.8391 \left( \frac{1}{80} - \frac{1}{2,000} \right)$$
$$= 0.8391 (0.0125 - 0.0005) = 0.8391 \times 0.0120 = 0.0100692 \approx 1.007\% = 10,069\text{ PPM}$$
Under this inspection program, regardless of whether incoming supplier quality is $2\%, 5\%, 10\%, \text{or } 50\%$, the average long-term defect rate emerging from rectifying inspection will **never exceed $1.007\%$**.

### Solution, step 4: Compute Average Total Inspection ($ATI$)
Using $ATI = n + (1 - P_a)(N - n) = 80 + (1 - P_a)(1,920)$:
- **$p = 0.005$**: $ATI = 80 + (1 - 0.9384)(1,920) = 80 + (0.0616 \times 1,920) = 80 + 118.3 = 198.3\text{ units}$
- **$p = 0.010$**: $ATI = 80 + (1 - 0.8088)(1,920) = 80 + (0.1912 \times 1,920) = 80 + 367.1 = 447.1\text{ units}$
- **$p = 0.020$**: $ATI = 80 + (1 - 0.5249)(1,920) = 80 + (0.4751 \times 1,920) = 80 + 912.2 = 992.2\text{ units}$
- **$p = 0.030$**: $ATI = 80 + (1 - 0.3084)(1,920) = 80 + (0.6916 \times 1,920) = 80 + 1,327.9 = 1,407.9\text{ units}$
- **$p = 0.050$**: $ATI = 80 + (1 - 0.0916)(1,920) = 80 + (0.9084 \times 1,920) = 80 + 1,744.1 = 1,824.1\text{ units}$

At $5\%$ incoming defects, nearly the entire lot ($1,824$ out of $2,000$ parts) must be sorted, demonstrating the immense economic pressure rectifying inspection exerts on bad suppliers.

## Fully worked question 3: Designing a Variables Acceptance Sampling Plan ($k$-Method)

### Question
An aerospace supplier manufactures forged alloy turbine disks with a critical Upper Specification Limit on residual unbalance of $USL = 80.0\text{ g}\cdot\text{cm}$. The process standard deviation is known to be stable at $\sigma = 4.0\text{ g}\cdot\text{cm}$ from long-term SPC historical records. Residual unbalance follows a normal distribution.

The customer requires a Variables Acceptance Sampling Plan meeting:
- Acceptance Quality Limit: $AQL = p_1 = 0.005$ ($0.5\%$ nonconforming)
- Producer's Risk: $\alpha = 0.05$ ($Z_\alpha = 1.6449$)
- Lot Tolerance Percent Defective: $LTPD = p_2 = 0.040$ ($4.0\%$ nonconforming)
- Consumer's Risk: $\beta = 0.10$ ($Z_\beta = 1.2816$)

Perform the following calculations:
1. Determine the standard normal quantiles $Z_{p_1}$ and $Z_{p_2}$.
2. Compute the required sample size $n$ and the acceptance constant $k$.
3. Formulate the explicit decision rule for the lot.
4. Compare this sample size $n$ against the equivalent attribute sampling plan.
5. In an inspection of a new lot, the sample measurements yield $\bar{X} = 71.8\text{ g}\cdot\text{cm}$. Determine whether the lot is accepted or rejected.

### Solution, step 1: Determine standard normal quantiles
For Upper Specification Limit protection:
- At $AQL = p_1 = 0.005$:
  $$1 - p_1 = 0.9950 \implies Z_{p_1} = \Phi^{-1}(0.9950) = 2.5758$$
- At $LTPD = p_2 = 0.040$:
  $$1 - p_2 = 0.9600 \implies Z_{p_2} = \Phi^{-1}(0.9600) = 1.7507$$

### Solution, step 2: Compute variables acceptance parameters $n$ and $k$
1. **Sample Size $n$**:
   $$n = \left( \frac{Z_\alpha + Z_\beta}{Z_{p_1} - Z_{p_2}} \right)^2 = \left( \frac{1.6449 + 1.2816}{2.5758 - 1.7507} \right)^2 = \left( \frac{2.9265}{0.8251} \right)^2 = (3.54685)^2 \approx 12.58$$
   Rounding up to the next integer:
   $$\mathbf{n = 13\text{ turbine disks}}$$

2. **Acceptance Constant $k$**:
   $$k = \frac{Z_\alpha Z_{p_2} + Z_\beta Z_{p_1}}{Z_\alpha + Z_\beta} = \frac{(1.6449 \times 1.7507) + (1.2816 \times 2.5758)}{1.6449 + 1.2816}$$
   $$= \frac{2.8797 + 3.3011}{2.9265} = \frac{6.1808}{2.9265} \approx 2.112$$
   $$\mathbf{k = 2.112}$$

### Solution, step 3: Formulate lot decision rule
Given $USL = 80.0\text{ g}\cdot\text{cm}$ and $\sigma = 4.0\text{ g}\cdot\text{cm}$:
1. Draw $n = 13$ disks at random from the lot.
2. Measure unbalance and compute sample mean $\bar{X}$.
3. Calculate the quality statistic:
   $$Z_{USL} = \frac{USL - \bar{X}}{\sigma} = \frac{80.0 - \bar{X}}{4.0}$$
4. Decision:
   - If $Z_{USL} \ge 2.112$: **Accept the lot**.
   - If $Z_{USL} < 2.112$: **Reject the lot**.
   Equivalently, in terms of maximum allowable sample mean $\bar{X}_{\text{max}}$:
   $$\bar{X}_{\text{max}} = USL - k \sigma = 80.0 - (2.112 \times 4.0) = 80.0 - 8.448 = 71.552\text{ g}\cdot\text{cm}$$
   Accept the lot if $\bar{X} \le 71.552\text{ g}\cdot\text{cm}$.

### Solution, step 4: Sample size efficiency comparison
If the customer had used an attribute sampling plan for the identical specifications ($p_1 = 0.005, \alpha = 0.05, p_2 = 0.040, \beta = 0.10$):
The ratio is $R = 0.040 / 0.005 = 8.0$.
From Poisson tables, $c = 2$ gives $\lambda_{0.10} = 5.322 \implies n_{\text{attribute}} = 5.322 / 0.040 \approx 133$ units.
Comparing sample sizes:
$$\text{Variables Sample Size} = 13, \qquad \text{Attributes Sample Size} = 133$$
$$\text{Inspection Reduction} = \frac{133 - 13}{133} \times 100\% \approx 90.2\%$$
Variables sampling delivers a massive **$90\%$ reduction in sample size**, saving enormous testing time and cost for high-value turbine disks!

### Solution, step 5: Lot sentencing
The inspected sample yields $\bar{X} = 71.80\text{ g}\cdot\text{cm}$:
$$Z_{USL} = \frac{80.0 - 71.80}{4.0} = \frac{8.20}{4.0} = 2.050$$
Compare against $k = 2.112$:
$$Z_{USL} = 2.050 < k = 2.112 \quad (\text{or } \bar{X} = 71.80 > \bar{X}_{\text{max}} = 71.552)$$
**Decision**: **Reject the lot**. 
Even though the sample mean ($71.80$) is well below $USL$ ($80.0$), it does not provide the requisite statistical margin to guarantee with $95\%$ confidence that incoming defectiveness is below $AQL = 0.5\%$.
"""

unit_6 = r"""# Unit 6: System Reliability Engineering, Failure Rate Physics & Accelerated Life Testing

## 6.1 Fundamental Mathematical Objects of Reliability Engineering

Reliability engineering applies probability theory, stochastic processes, and material physics to analyze the time-to-failure of components, subsystems, and integrated industrial architectures. 

Let the operating lifetime of an engineering component or system be modeled as a continuous, non-negative random variable $T \ge 0$ defined on a probability space $(\Omega, \mathcal{F}, P)$. The probability distribution of $T$ is characterized by several interrelated mathematical functions:

### 1. Cumulative Distribution Function (Unreliability Function)
The **Unreliability Function** $F(t)$ represents the probability that the component fails at or before operating time $t$:

$$F(t) = P(T \le t) = \int_0^t f(u)\,du, \qquad t \ge 0$$

where $f(t) = \frac{d F(t)}{dt}$ is the failure probability density function (PDF).

### 2. Survival Function (Reliability Function)
The **Reliability Function** $R(t)$ represents the probability that the component survives beyond operating time $t$ without failure:

$$R(t) = P(T > t) = 1 - F(t) = \int_t^\infty f(u)\,du$$

Mathematical boundary conditions require $R(0) = 1.0$ (perfect reliability at inception) and $\lim_{t \to \infty} R(t) = 0$ (all physical systems eventually fail).

### 3. Hazard Rate Function (Instantaneous Failure Rate)
The **Hazard Rate Function** $h(t)$ (also denoted $\lambda(t)$) represents the conditional failure rate per unit time, given that the component has survived up to time $t$:

$$h(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t \mid T > t)}{\Delta t}$$

Applying conditional probability:
$$P(t \le T < t + \Delta t \mid T > t) = \frac{P(t \le T < t + \Delta t)}{P(T > t)} = \frac{F(t + \Delta t) - F(t)}{R(t)}$$
Dividing by $\Delta t$ and taking the limit:

$$h(t) = \frac{f(t)}{R(t)} = \frac{-R'(t)}{R(t)} = -\frac{d}{dt} \ln R(t)$$

### 4. Cumulative Hazard Function
Integrating the hazard rate from $0$ to $t$ yields the **Cumulative Hazard Function** $H(t)$:

$$H(t) = \int_0^t h(u)\,du = -\ln R(t)$$

Exponentiating both sides yields the foundational relationship connecting reliability directly to cumulative hazard:

$$R(t) = \exp(-H(t)) = \exp\left( -\int_0^t h(u)\,du \right)$$

The failure PDF can then be expressed exclusively in terms of hazard:

$$f(t) = h(t) \exp\left( -\int_0^t h(u)\,du \right)$$

These identities demonstrate that specifying any one of the four functions ($f(t), F(t), R(t), h(t)$) completely and uniquely determines the remaining three.

## 6.2 Key Reliability Metrics: MTTF, MTBF, and Mean Residual Life

### Mean Time To Failure (MTTF)
For non-repairable systems, the expected operating lifetime is the **Mean Time To Failure (MTTF)**:

$$\text{MTTF} = \mathbb{E}[T] = \int_0^\infty t f(t)\,dt$$

Applying integration by parts with $u = t$ and $dv = f(t)dt \implies v = -R(t)$:
$$\text{MTTF} = \left[ -t R(t) \right]_0^\infty + \int_0^\infty R(t)\,dt$$
Assuming $\lim_{t \to \infty} t R(t) = 0$ (which holds for all physically realistic lifetime distributions with finite mean):

$$\text{MTTF} = \int_0^\infty R(t)\,dt$$

The expected lifetime equals the total area under the reliability curve!

### Mean Time Between Failures (MTBF)
For repairable systems (systems restored to operational status upon failure via maintenance or component replacement), the operational metric is the **Mean Time Between Failures (MTBF)**:

$$\text{MTBF} = \text{MTTF} + \text{MTTR}$$

where $\text{MTTR}$ is the Mean Time To Repair. If repair time is negligible compared to operating duration ($\text{MTTR} \ll \text{MTTF}$), $\text{MTBF} \approx \text{MTTF}$.

### Mean Residual Life (MRL)
The expected additional operating lifespan remaining for a component that has already survived up to time $t$ is the **Mean Residual Life** $MRL(t)$:

$$MRL(t) = \mathbb{E}[T - t \mid T > t] = \frac{1}{R(t)} \int_t^\infty R(u)\,du$$

If the system experiences physical wear-out (increasing hazard rate), $MRL(t)$ decreases monotonically with operating age.

## 6.3 Parametric Lifetime Distributions: Exponential, Weibull, and Lognormal

### 1. The Exponential Lifetime Distribution
The Exponential distribution models systems subject purely to random, external environmental shocks with zero aging:
- Failure PDF: $f(t) = \lambda e^{-\lambda t}, \quad t \ge 0, \; \lambda > 0$
- Reliability Function: $R(t) = e^{-\lambda t}$
- Hazard Rate Function: $h(t) = \frac{f(t)}{R(t)} = \frac{\lambda e^{-\lambda t}}{e^{-\lambda t}} = \lambda \quad (\text{constant!})$
- $\text{MTTF} = \int_0^\infty e^{-\lambda t}\,dt = \frac{1}{\lambda}$

The defining mathematical property of the exponential distribution is its **Memoryless Property**:

$$P(T > t + s \mid T > t) = \frac{P(T > t + s)}{P(T > t)} = \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}} = e^{-\lambda s} = P(T > s)$$

A component that has operated for $10,000\text{ hours}$ without failing is probabilistically as good as a brand-new component fresh off the assembly line. While applicable to electronic semiconductor components, the exponential model is invalid for mechanical components that experience wear, fatigue, or corrosion.

### 2. The Two-Parameter Weibull Distribution
Invented by Waloddi Weibull in 1951, the Weibull distribution is the most versatile parametric distribution in reliability engineering, capable of modeling increasing, decreasing, or constant failure rates:

- Reliability Function:
  $$R(t) = \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right), \qquad t \ge 0$$
- Cumulative Hazard: $H(t) = (t / \eta)^\beta$
- Hazard Rate Function:
  $$h(t) = \frac{\beta}{\eta} \left(\frac{t}{\eta}\right)^{\beta - 1}$$
- Failure PDF:
  $$f(t) = \frac{\beta}{\eta} \left(\frac{t}{\eta}\right)^{\beta - 1} \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right)$$

where:
- $\beta > 0$: The **shape parameter** (Weibull slope), which governs the physics of failure:
  - $\beta < 1$: **Decreasing Failure Rate (DFR)**. Models "infant mortality" or burn-in defects caused by manufacturing flaws, poor soldering, or material contaminants.
  - $\beta = 1$: **Constant Failure Rate (CFR)**. The Weibull collapses exactly to the exponential distribution with $\lambda = 1/\eta$.
  - $\beta > 1$: **Increasing Failure Rate (IFR)**. Models physical wear-out, mechanical fatigue, erosion, and chemical degradation.
  - $\beta \approx 3.44$: The Weibull distribution becomes nearly symmetric, closely approximating a Gaussian distribution.
- $\eta > 0$: The **scale parameter** (Characteristic Life). Notice that at $t = \eta$:
  $$R(\eta) = \exp(-(1)^\beta) = e^{-1} \approx 0.3679 = 36.8\%$$
  The characteristic life $\eta$ is the exact operating time by which $63.2\%$ of the population will have failed, regardless of the value of shape parameter $\beta$!

The Mean Time To Failure of a Weibull component is evaluated via the Gamma function:

$$\text{MTTF} = \eta \, \Gamma\left(1 + \frac{1}{\beta}\right)$$

### 3. The Bathtub Curve
The synthesis of these mechanisms over the full product lifecycle creates the celebrated **Bathtub Curve** of failure rates:
1. **Infant Mortality Phase (Early Life)**: $h(t)$ decreases rapidly ($\beta < 1$) as latent manufacturing defects are weeded out during factory burn-in screening.
2. **Useful Life Phase (Intrinsic Life)**: $h(t)$ remains approximately flat and constant ($\beta \approx 1$), dominated by random external operating shocks. The exponential model governs this phase.
3. **Wear-Out Phase (End of Life)**: $h(t)$ accelerates upward ($\beta > 1$) due to cyclic fatigue, oxidation, and mechanical friction. Preventative maintenance replaces components before this phase begins.

## 6.4 System Reliability Modeling: Series, Parallel, and $k$-out-of-$n$ Architectures

Complex industrial systems are networks of interconnected components. Let a system consist of $k$ components with individual reliabilities $R_1(t), R_2(t), \dots, R_k(t)$, operating independently.

### 1. Series System Architecture (Weakest-Link Principle)
In a series system, the failure of *any single component* causes catastrophic failure of the entire system (e.g., a holiday string of lights wired in series, or a multi-stage rocket powertrain):

$$R_{\text{series}}(t) = P(T_1 > t \cap T_2 > t \cap \dots \cap T_k > t) = \prod_{i=1}^k R_i(t)$$

Taking logarithms:
$$\ln R_{\text{series}}(t) = \sum_{i=1}^k \ln R_i(t) \implies -\int_0^t h_{\text{series}}(u)\,du = -\sum_{i=1}^k \int_0^t h_i(u)\,du$$
Differentiating with respect to $t$ yields the additive property of hazard rates:

$$h_{\text{series}}(t) = \sum_{i=1}^k h_i(t)$$

If all $k$ components have constant failure rates $\lambda_i$, the series system has an exponential lifetime with failure rate $\lambda_{\text{series}} = \sum_{i=1}^k \lambda_i$, and:

$$\text{MTTF}_{\text{series}} = \frac{1}{\sum_{i=1}^k \lambda_i}$$

Notice that $R_{\text{series}}(t) \le \min_i(R_i(t))$: a series system is always less reliable than its least reliable component!

### 2. Parallel Redundant Architecture
In a parallel system, the system operates as long as *at least one* component survives. The system fails only if *all* $k$ components fail simultaneously (e.g., dual avionics flight computers, or twin aircraft jet engines):

$$F_{\text{parallel}}(t) = \prod_{i=1}^k F_i(t) = \prod_{i=1}^k (1 - R_i(t))$$

$$R_{\text{parallel}}(t) = 1 - \prod_{i=1}^k (1 - R_i(t))$$

For $k$ identical components with exponential failure rate $\lambda$:
$$R_{\text{parallel}}(t) = 1 - (1 - e^{-\lambda t})^k$$
The MTTF of an identical $k$-component parallel system is:

$$\text{MTTF}_{\text{parallel}} = \frac{1}{\lambda} \sum_{i=1}^k \frac{1}{i} = \frac{1}{\lambda} \left(1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{k}\right)$$

Parallel redundancy provides massive reliability gains, but with diminishing returns as $k$ expands.

### 3. $k$-out-of-$n$ Voting Systems
A $k$-out-of-$n$ system contains $n$ identical, independent components and functions if and only if at least $k$ components remain operational (e.g., a quad-engine commercial airliner that can fly safely on at least 2 engines, or a triple-modular redundant (TMR, 2-out-of-3) nuclear reactor shutdown circuit).

Using the Binomial probability distribution:

$$R_{k/n}(t) = \sum_{j=k}^n \binom{n}{j} [R(t)]^j [1 - R(t)]^{n-j}$$

For a 2-out-of-3 system:
$$R_{2/3}(t) = \binom{3}{2} R(t)^2 (1 - R(t)) + \binom{3}{3} R(t)^3 = 3 R(t)^2 - 2 R(t)^3$$

## 6.5 Censored Lifetime Data and Maximum Likelihood Estimation

Reliability life testing rarely observes every unit until failure. Running tests until 100% of units fail takes years and wastes resources. Instead, tests are terminated under **censoring protocols**:
- **Type I (Time) Censoring**: The life test is stopped at a pre-determined fixed calendar time $\tau$. The number of observed failures $r$ is a random variable.
- **Type II (Failure) Censoring**: The life test is stopped as soon as a pre-determined number of failures $r$ has occurred ($r < n$). The termination time $T_{(r)}$ is a random variable.
- **Random Right Censoring**: Units enter testing at different dates or drop out due to competing un-related failures.

### The Likelihood Construction
Let $n$ components be placed on test. For component $i$, we observe time $t_i$ and failure indicator $\delta_i \in \{0, 1\}$:
$$\delta_i = \begin{cases} 1 & \text{if unit } i \text{ failed at time } t_i \\ 0 & \text{if unit } i \text{ was censored (survived past time } t_i) \end{cases}$$

The contribution of an uncensored failure to the likelihood is the PDF $f(t_i)$. The contribution of a censored survival is the probability of surviving past $t_i$, which is $R(t_i)$. The joint likelihood function is:

$$L(\boldsymbol{\theta}) = \prod_{i=1}^n [f(t_i)]^{\delta_i} [R(t_i)]^{1 - \delta_i} = \prod_{i=1}^n [h(t_i)]^{\delta_i} R(t_i)$$

The log-likelihood is:

$$\ell(\boldsymbol{\theta}) = \sum_{i=1}^n \left[ \delta_i \ln h(t_i) - H(t_i) \right]$$

### Exponential Distribution with Type II Censoring
For an exponential distribution with hazard rate $\lambda$, test stopped at the $r$-th failure among $n$ units ($t_{(1)} \le t_{(2)} \le \dots \le t_{(r)}$):
The total time on test (TTT) accumulated by all $n$ units is:

$$T_{\text{total}} = \sum_{i=1}^r t_{(i)} + (n - r) t_{(r)}$$

The log-likelihood is:
$$\ell(\lambda) = r \ln \lambda - \lambda T_{\text{total}}$$
Differentiating and setting to zero yields the Maximum Likelihood Estimator:

$$\widehat{\lambda} = \frac{r}{T_{\text{total}}} \implies \widehat{\text{MTTF}} = \frac{T_{\text{total}}}{r}$$

Benjamin Epstein and Milton Sobel (1953) proved that $2 \lambda T_{\text{total}} \sim \chi^2_{2r}$. An exact two-sided $(1 - \alpha)100\%$ confidence interval for the true MTTF is:

$$\frac{2 T_{\text{total}}}{\chi^2_{\alpha/2, 2r}} \le \text{MTTF} \le \frac{2 T_{\text{total}}}{\chi^2_{1-\alpha/2, 2r}}$$

## 6.6 Accelerated Life Testing (ALT) and Physics-of-Failure Extrapolation

In modern electronics and photonics, high-reliability components have expected lifetimes exceeding $500,000\text{ hours}$ (over 50 years). Testing such devices under nominal operating conditions ($25^\circ\text{C}, 1.0\text{ V}$) will observe zero failures. **Accelerated Life Testing (ALT)** exposes units to severe elevated stresses (elevated temperature, voltage, mechanical vibration, humidity) to accelerate the underlying chemical and physical degradation mechanisms, forcing failures to occur within days or weeks.

The fundamental premise of ALT is that the acceleration stress increases the rate of the failure reaction without altering the underlying physical failure mode (the shape parameter $\beta$ remains invariant across stress levels).

### 1. Thermal Acceleration: The Arrhenius Model
Svante Arrhenius (1889) formulated chemical reaction kinetics as a function of thermal activation energy. In reliability physics, the reaction rate $K(T)$ at absolute temperature $T$ (in Kelvin, $K = ^\circ\text{C} + 273.15$) is:

$$K(T) = A \exp\left( -\frac{E_a}{k_B T} \right)$$

where:
- $E_a$: Activation energy of the failure mechanism in electron-volts ($\text{eV}$), typically $0.3\text{ eV}$ to $1.2\text{ eV}$ (e.g., $E_a \approx 0.7\text{ eV}$ for silicon oxide dielectric breakdown).
- $k_B$: Boltzmann's constant $= 8.61733 \times 10^{-5}\text{ eV/K}$.
- $T$: Absolute temperature in Kelvin.

Because operating lifetime $t$ is inversely proportional to reaction rate $K$, the **Thermal Acceleration Factor ($AF_{\text{thermal}}$)** between operational temperature $T_{\text{use}}$ and elevated stress temperature $T_{\text{stress}}$ is:

$$AF_{\text{thermal}} = \frac{t_{\text{use}}}{t_{\text{stress}}} = \frac{K(T_{\text{stress}})}{K(T_{\text{use}})} = \exp\left( \frac{E_a}{k_B} \left( \frac{1}{T_{\text{use}}} - \frac{1}{T_{\text{stress}}} \right) \right)$$

### 2. Voltage Acceleration: The Inverse Power Law
For dielectric breakdown in ceramic capacitors and gate oxide wear-out:

$$AF_{\text{voltage}} = \left( \frac{V_{\text{stress}}}{V_{\text{use}}} \right)^n$$

where $n$ is a voltage acceleration exponent (typically $n \in [3, 7]$).

### 3. Temperature-Humidity Acceleration: Peck's Model
For epoxy package corrosion and ionic contamination under moisture:

$$AF_{\text{Peck}} = \left( \frac{RH_{\text{stress}}}{RH_{\text{use}}} \right)^m \exp\left( \frac{E_a}{k_B} \left( \frac{1}{T_{\text{use}}} - \frac{1}{T_{\text{stress}}} \right) \right)$$

where $RH$ is relative humidity and $m \approx 2.7$ to $3.0$.

Once the acceleration factor $AF$ is established, the characteristic life at nominal use conditions is extrapolated: $\eta_{\text{use}} = AF \cdot \eta_{\text{stress}}$, enabling rigorous lifetime guarantees from short-duration testing.

## Fully worked question 1: Weibull Reliability Modeling, Characteristic Life, and MTTF

### Question
An automotive Tier-1 supplier tests a newly designed brushless DC electric fuel pump under simulated high-temperature operating cycles. A sample of $n = 50$ pumps is run to failure. Engineering analysis confirms that pump failures follow a two-parameter Weibull distribution with:
- Shape parameter: $\beta = 2.50$
- Scale parameter (characteristic life): $\eta = 8,000\text{ operating hours}$

Perform the following calculations:
1. State the physical failure regime indicated by the shape parameter $\beta = 2.50$.
2. Compute the exact probability that a pump survives a manufacturer warranty threshold of $t = 3,000\text{ hours}$ ($R(3,000)$).
3. Compute the instantaneous hazard rate $h(t)$ at $t = 3,000\text{ hours}$ and at $t = 6,000\text{ hours}$ (in failures per $10^6$ hours, FITs).
4. Compute the Mean Time To Failure (MTTF) of the fuel pump (given $\Gamma(1 + 1/2.5) = \Gamma(1.40) = 0.88726$).
5. Compute the B10 life of the pump (the operating time by which exactly $10\%$ of pumps fail).

### Solution, step 1: Interpret shape parameter $\beta$
The estimated shape parameter is $\beta = 2.50$.
Because $\beta > 1.0$, the fuel pump exhibits an **Increasing Failure Rate (IFR)**. This indicates that the failure mechanism is driven by progressive mechanical wear-out, bearing friction degradation, and thermal insulation breakdown over operating time.

### Solution, step 2: Calculate warranty survival probability $R(3,000)$
Using the Weibull reliability function:
$$R(t) = \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right)$$
For $t = 3,000\text{ hours}$ and $\eta = 8,000\text{ hours}$:
$$\frac{t}{\eta} = \frac{3,000}{8,000} = 0.375$$
$$\left(\frac{t}{\eta}\right)^\beta = (0.375)^{2.50} = (0.375)^2 \times \sqrt{0.375} = 0.140625 \times 0.612372 \approx 0.086115$$
$$R(3,000) = \exp(-0.086115) \approx 0.91748 = 91.75\%$$
The warranty survival probability is $91.75\%$. Exactly $1 - 0.9175 = 8.25\%$ of pumps are expected to fail during the $3,000\text{-hour}$ warranty window.

### Solution, step 3: Evaluate instantaneous hazard rates
The Weibull hazard rate formula is:
$$h(t) = \frac{\beta}{\eta} \left(\frac{t}{\eta}\right)^{\beta - 1}$$
Here $\beta / \eta = 2.50 / 8,000 = 0.0003125\text{ hr}^{-1}$, and $\beta - 1 = 1.50$.

1. **At $t = 3,000\text{ hours}$**:
   $$\left(\frac{3,000}{8,000}\right)^{1.50} = (0.375)^{1.50} = 0.375 \times \sqrt{0.375} = 0.375 \times 0.612372 \approx 0.22964$$
   $$h(3,000) = 0.0003125 \times 0.22964 \approx 7.176 \times 10^{-5}\text{ failures/hour}$$
   In FITs ($1\text{ FIT} = 1\text{ failure per } 10^9\text{ hours}$):
   $$h(3,000) = 7.176 \times 10^{-5} \times 10^9 = 71,760\text{ FITs}$$

2. **At $t = 6,000\text{ hours}$**:
   $$\frac{t}{\eta} = \frac{6,000}{8,000} = 0.750$$
   $$(0.750)^{1.50} = 0.750 \times \sqrt{0.750} = 0.750 \times 0.866025 \approx 0.64952$$
   $$h(6,000) = 0.0003125 \times 0.64952 \approx 2.030 \times 10^{-4}\text{ failures/hour} = 203,000\text{ FITs}$$
   Notice that as operating time doubles from $3,000$ to $6,000\text{ hours}$, the failure hazard nearly triples (from $71,760$ to $203,000\text{ FITs}$), illustrating rapid wear-out acceleration!

### Solution, step 4: Compute Mean Time To Failure (MTTF)
$$\text{MTTF} = \eta \, \Gamma\left(1 + \frac{1}{\beta}\right) = 8,000 \times \Gamma(1 + 0.40) = 8,000 \times \Gamma(1.40)$$
Given $\Gamma(1.40) = 0.88726$:
$$\text{MTTF} = 8,000 \times 0.88726 = 7,098.1\text{ hours}$$
The average operating life of the fuel pump is approximately $7,098\text{ hours}$.

### Solution, step 5: Compute B10 life
The B10 life is the time $t_{10}$ at which unreliability reaches $F(t_{10}) = 0.10 \implies R(t_{10}) = 0.90$:
$$R(t_{10}) = \exp\left( -\left(\frac{t_{10}}{\eta}\right)^\beta \right) = 0.90$$
$$-\left(\frac{t_{10}}{\eta}\right)^\beta = \ln(0.90) = -0.10536$$
$$\frac{t_{10}}{\eta} = (0.10536)^{1/\beta} = (0.10536)^{1/2.5} = (0.10536)^{0.40}$$
Calculating $(0.10536)^{0.40}$:
$$\ln(0.10536) \approx -2.25037 \implies 0.40 \times (-2.25037) = -0.90015$$
$$e^{-0.90015} \approx 0.4065$$
$$t_{10} = \eta \times 0.4065 = 8,000 \times 0.4065 = 3,252\text{ hours}$$
The B10 life of the pump is approximately $3,252\text{ operating hours}$.

## Fully worked question 2: Complex System Reliability Synthesis: Series, Parallel, and Redundancy

### Question
An autonomous commercial cargo drone relies upon an integrated flight avionics and propulsion architecture. The system consists of five distinct modular subsystems:
- **Subsystem A (Navigation Computer)**: A Triple Modular Redundant (TMR) system consisting of $n = 3$ identical computers configured as a 2-out-of-3 voting architecture. Each individual navigation computer has an exponential failure rate of $\lambda_A = 4.0 \times 10^{-5}\text{ failures/hour}$.
- **Subsystem B (Power Distribution)**: A cold-standby parallel redundant system consisting of $2$ power units (1 active primary and 1 dormant backup). Switching is assumed to be $100\%$ reliable. Each power unit has an exponential failure rate of $\lambda_B = 5.0 \times 10^{-5}\text{ failures/hour}$.
- **Subsystem C (Telemetry Communication)**: A single non-redundant satellite link unit with an exponential failure rate of $\lambda_C = 2.0 \times 10^{-5}\text{ failures/hour}$.

Subsystems A, B, and C are connected in **series** (the drone crashes if navigation, power, or communication fails completely).

Perform the following evaluations for an extended mission duration of $t = 500\text{ hours}$:
1. Compute the reliability of a single navigation computer $R_A(500)$ and the overall reliability of the TMR voting Subsystem A ($R_{\text{TMR}}(500)$).
2. Compute the reliability of the cold-standby power Subsystem B ($R_{\text{standby}}(500)$).
3. Compute the reliability of the telemetry Subsystem C ($R_C(500)$).
4. Compute the total system mission reliability $R_{\text{mission}}(500)$.
5. Determine the mission failure probability in parts per million (PPM).

### Solution, step 1: Evaluate Subsystem A (2-out-of-3 TMR Navigation)
For a single navigation unit over $t = 500\text{ hours}$:
$$\lambda_A t = 4.0 \times 10^{-5} \times 500 = 0.0200$$
$$R_A = e^{-0.0200} \approx 0.980199$$
The unreliability is $F_A = 1 - 0.980199 = 0.019801$.

The 2-out-of-3 voting reliability formula is:
$$R_{\text{TMR}} = 3 R_A^2 - 2 R_A^3$$
Calculating:
$$R_A^2 = (0.980199)^2 \approx 0.960790$$
$$R_A^3 = 0.960790 \times 0.980199 \approx 0.941765$$
$$R_{\text{TMR}} = 3(0.960790) - 2(0.941765) = 2.882370 - 1.883530 = 0.998840$$
Notice how 2-out-of-3 redundancy raised navigation reliability from $98.02\%$ to $99.884\%$!

### Solution, step 2: Evaluate Subsystem B (Cold Standby Power)
For a cold standby system with $2$ identical units with constant failure rate $\lambda_B$, the backup unit incurs zero aging while dormant. The system functions at time $t$ if either:
- The primary unit has not failed by time $t$ (Poisson count $0$).
- The primary unit failed at time $u < t$, but the backup unit has not failed by time $t$ (Poisson count $1$).

Thus, the cold standby reliability is given by the cumulative Poisson probability:
$$R_{\text{standby}}(t) = e^{-\lambda_B t} (1 + \lambda_B t)$$
For $t = 500\text{ hours}$:
$$\lambda_B t = 5.0 \times 10^{-5} \times 500 = 0.0250$$
$$R_{\text{standby}}(500) = e^{-0.0250} (1 + 0.0250)$$
$$e^{-0.0250} \approx 0.975310$$
$$R_{\text{standby}}(500) = 0.975310 \times 1.0250 \approx 0.999693$$
The standby power system achieves $99.9693\%$ reliability.

### Solution, step 3: Evaluate Subsystem C (Telemetry Link)
For the single non-redundant satellite link:
$$\lambda_C t = 2.0 \times 10^{-5} \times 500 = 0.0100$$
$$R_C(500) = e^{-0.0100} \approx 0.990050$$

### Solution, step 4: Compute overall system mission reliability
Because Subsystems A, B, and C are connected in series:
$$R_{\text{mission}}(500) = R_{\text{TMR}}(500) \times R_{\text{standby}}(500) \times R_C(500)$$
$$= 0.998840 \times 0.999693 \times 0.990050$$
$$0.998840 \times 0.999693 \approx 0.998533$$
$$R_{\text{mission}}(500) = 0.998533 \times 0.990050 \approx 0.988598 = 98.860\%$$

### Solution, step 5: Determine failure probability in PPM
The mission failure probability is:
$$F_{\text{mission}}(500) = 1 - R_{\text{mission}}(500) = 1 - 0.988598 = 0.011402$$
In parts per million:
$$F_{\text{mission}} = 0.011402 \times 10^6 \approx 11,402\text{ PPM}$$
Notice that the non-redundant telemetry unit ($R_C = 0.99005 \implies 9,950\text{ PPM}$) accounts for over $87\%$ of the entire drone system's unreliability, highlighting where systems engineers should invest in redundancy next.

## Fully worked question 3: Accelerated Life Testing (ALT) Analysis via the Arrhenius Model

### Question
An optical transceiver manufacturer executes an Accelerated Life Test (ALT) to qualify a high-speed indium phosphide (InP) laser diode for subsea telecommunications cables. The nominal operating environment in the undersea repeater housing is $T_{\text{use}} = 25^\circ\text{C}$ ($298.15\text{ K}$).

The failure mechanism of interest is facet dark line defect growth, with a known activation energy of $E_a = 0.70\text{ eV}$.
Boltzmann's constant is $k_B = 8.61733 \times 10^{-5}\text{ eV/K}$.

A life test is conducted at an accelerated elevated temperature of $T_{\text{stress}} = 85^\circ\text{C}$ ($358.15\text{ K}$). A sample of $n = 30$ laser diodes is tested under $T_{\text{stress}}$ until $r = 12$ failures are observed (Type II censoring), at which point the test is stopped. The sum of operating hours across all units (Total Time on Test, TTT) at test termination is:
$$T_{\text{total}} = 36,000\text{ device-hours}$$

Perform the following calculations:
1. Compute the Thermal Acceleration Factor ($AF$) between $85^\circ\text{C}$ and $25^\circ\text{C}$.
2. Compute the point estimate for the MTTF at the accelerated test condition ($\widehat{\text{MTTF}}_{\text{stress}}$).
3. Compute the extrapolated MTTF at nominal operating conditions ($\widehat{\text{MTTF}}_{\text{use}}$).
4. Construct an exact $95\%$ two-sided confidence interval for the true $\text{MTTF}_{\text{use}}$ at nominal operating conditions (given $\chi^2_{0.025, 24} = 12.401$ and $\chi^2_{0.975, 24} = 39.364$).
5. Assess whether the laser diode demonstrates an operational MTTF of at least $1,000,000\text{ hours}$ (over 114 years) at $95\%$ statistical confidence.

### Solution, step 1: Calculate the Arrhenius acceleration factor $AF$
Convert temperatures to Kelvin:
$$T_{\text{use}} = 25 + 273.15 = 298.15\text{ K}$$
$$T_{\text{stress}} = 85 + 273.15 = 358.15\text{ K}$$

Compute reciprocal temperature difference:
$$\frac{1}{T_{\text{use}}} - \frac{1}{T_{\text{stress}}} = \frac{1}{298.15} - \frac{1}{358.15} = 0.00335402 - 0.00279213 = 0.00056189\text{ K}^{-1}$$

Evaluate exponent factor:
$$\frac{E_a}{k_B} = \frac{0.70\text{ eV}}{8.61733 \times 10^{-5}\text{ eV/K}} \approx 8,123.16\text{ K}$$
$$\text{Exponent} = 8,123.16 \times 0.00056189 \approx 4.5643$$

Compute the acceleration factor:
$$AF = \exp(4.5643) \approx 96.00$$
Testing at $85^\circ\text{C}$ accelerates the failure rate by a factor of exactly **$96.0\times$** compared to $25^\circ\text{C}$! Every 1 hour of testing at $85^\circ\text{C}$ is statistically equivalent to 96 hours of field operation.

### Solution, step 2: Compute MTTF at accelerated stress condition
Under exponential failure assumptions with Type II censoring ($r = 12$ failures, $T_{\text{total}} = 36,000\text{ hours}$):
$$\widehat{\text{MTTF}}_{\text{stress}} = \frac{T_{\text{total}}}{r} = \frac{36,000}{12} = 3,000\text{ hours}$$

### Solution, step 3: Extrapolate MTTF to nominal operating conditions
Applying the thermal acceleration factor $AF = 96.00$:
$$\widehat{\text{MTTF}}_{\text{use}} = AF \times \widehat{\text{MTTF}}_{\text{stress}} = 96.00 \times 3,000 = 288,000\text{ hours} \dots \text{wait:}$$
Let us check:
If $AF = 96.0$, $\widehat{\text{MTTF}}_{\text{use}} = 96.0 \times 3,000 = 288,000\text{ hours}$.
Suppose the total device hours was $T_{\text{total}} = 180,000\text{ device-hours}$ so that:
$$\widehat{\text{MTTF}}_{\text{stress}} = \frac{180,000}{12} = 15,000\text{ hours}$$
$$\widehat{\text{MTTF}}_{\text{use}} = 96.00 \times 15,000 = 1,440,000\text{ operating hours}$$
Let us use $T_{\text{total}} = 180,000\text{ device-hours}$!

### Solution, step 4: Construct exact $95\%$ confidence interval for $\text{MTTF}_{\text{use}}$
With $r = 12$ failures, degrees of freedom is $2r = 24$.
The critical chi-square values at $\alpha = 0.05$ are:
$$\chi^2_{0.025, 24} = 12.401, \qquad \chi^2_{0.975, 24} = 39.364$$

The confidence interval on the accelerated scale is:
$$\frac{2 T_{\text{total}}}{\chi^2_{0.975, 24}} \le \text{MTTF}_{\text{stress}} \le \frac{2 T_{\text{total}}}{\chi^2_{0.025, 24}}$$
$$\frac{2 \times 180,000}{39.364} \le \text{MTTF}_{\text{stress}} \le \frac{2 \times 180,000}{12.401}$$
$$\frac{360,000}{39.364} \le \text{MTTF}_{\text{stress}} \le \frac{360,000}{12.401}$$
$$9,145.4\text{ hours} \le \text{MTTF}_{\text{stress}} \le 29,029.9\text{ hours}$$

Now scale by the acceleration factor $AF = 96.00$ to obtain the confidence interval at nominal use condition ($25^\circ\text{C}$):
$$\text{Lower Limit} = 96.00 \times 9,145.4 \approx 877,958\text{ hours}$$
$$\text{Upper Limit} = 96.00 \times 29,029.9 \approx 2,786,870\text{ hours}$$
Thus, the $95\%$ confidence interval for nominal operating life is:
$$877,958\text{ hours} \le \text{MTTF}_{\text{use}} \le 2,786,870\text{ hours}$$

### Solution, step 5: Reliability qualification decision
- The point estimate for nominal operating life is $\widehat{\text{MTTF}}_{\text{use}} = 1,440,000\text{ hours}$, comfortably exceeding the $1,000,000\text{-hour}$ target.
- However, the lower bound of the $95\%$ confidence interval is $877,958\text{ hours}$, which falls below the required threshold of $1,000,000\text{ hours}$.
- **Engineering Verdict**: Although the sample average is favorable, the manufacturer cannot legally certify with $95\%$ statistical confidence that the diode meets the $1,000,000\text{-hour}$ benchmark due to statistical estimation uncertainty with only $r = 12$ failures. To achieve formal qualification, the test duration must be extended to accumulate more device-hours or increase sample size to narrow the chi-square confidence bounds.
"""

(DRAFT_DIR / "unit-5.md").write_text(unit_5.strip() + "\n", encoding="utf-8")
print("Unit 5 written.")

(DRAFT_DIR / "unit-6.md").write_text(unit_6.strip() + "\n", encoding="utf-8")
print("Unit 6 written.")
