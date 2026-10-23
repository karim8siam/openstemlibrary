# Unit 5: Acceptance Sampling Quality Assurance: Attributes & Variables Inspection Systems

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

## 5.8 Dodge-Romig Sampling Systems: AOQL and LTPD Optimization

In the late 1920s and 1930s, Harold F. Dodge and Harry G. Romig developed the **Dodge-Romig Sampling Systems** at Bell Telephone Laboratories. Unlike military standards which are indexed by AQL, Dodge-Romig plans are specifically engineered for **rectifying inspection** environments where every rejected lot is 100% sorted.

Dodge-Romig tables provide sampling plans categorized into two fundamental classes:
1. **Lot Tolerance Percent Defective (LTPD) Plans**: Designed to provide a guaranteed consumer's risk of $\beta = 0.10$ at a designated limiting quality $p_2 = LTPD$, while mathematically minimizing the Average Total Inspection ($ATI$) at the supplier's process average defect rate $\bar{p}$.
2. **Average Outgoing Quality Limit (AOQL) Plans**: Designed to guarantee that outgoing defectiveness never exceeds a pre-set ceiling ($AOQL$) under rectifying inspection, while mathematically minimizing the Average Total Inspection ($ATI$) at the process average $\bar{p}$.

### Mathematical Optimization Criterion
For a given lot size $N$ and historical process average $\bar{p}$, Dodge and Romig sought the pair $(n, c)$ that minimizes the objective function:

$$\min_{n, c} ATI(\bar{p}) = n + (1 - P_a(\bar{p}; n, c))(N - n)$$

subject to either:
$$P_a(p_2; n, c) = 0.10 \quad (\text{for LTPD plans})$$
or
$$\max_{0 \le p \le 1} AOQ(p; n, c, N) = AOQL \quad (\text{for AOQL plans})$$

By tabulating optimal combinations across standard lot size brackets ($N = 1-50, 51-100, \dots, 50,001-100,000$) and process averages $\bar{p}$, Dodge and Romig created the most cost-efficient rectifying inspection systems in manufacturing history.

## 5.9 Continuous Sampling Plans for Automated Production: CSP-1, CSP-2, and CSP-3

Traditional lot-by-lot acceptance sampling requires segregating parts into identifiable physical containers or batches. In high-speed automated continuous flow lines (e.g., continuous conveyor belt assembly of canned beverages, automotive engine blocks, or consumer electronics), halting the line to form artificial lots is logistically impossible. 

To govern continuous production flows, Harold Dodge (1943) invented **Continuous Sampling Plans (CSP)**:

### The CSP-1 Operational Protocol
CSP-1 operates as an adaptive two-mode finite state machine:
1. **Screening Mode (100% Inspection)**: At production startup, inspect $100\%$ of units consecutively in order of manufacture. Continue screening until a pre-determined **clearing clearance number** $i$ of consecutive units are found to be completely defect-free ($i$ consecutive conforming units).
2. **Sampling Mode**: Once $i$ consecutive defect-free units are observed, discontinue 100% screening. Inspect only a small fraction $f$ of units (e.g., $f = 1/5$ or $f = 1/10$), selecting units at random or systematically along the line.
3. **Reversion Trigger**: As long as sampled units are conforming, sampling continues indefinitely. The instant *a single nonconforming unit* is discovered during sampling, the line immediately reverts to **Screening Mode (100% Inspection)**, and the cycle repeats.

Dodge proved that for any specified fraction $f$ and clearing interval $i$, the outgoing quality is guaranteed never to exceed a mathematical ceiling:

$$AOQL_{\text{CSP-1}} = \frac{k_{\text{CSP}}}{i}$$

Subsequent variants (CSP-2 and CSP-3) introduce delay buffers before reverting to 100% screening, preventing line disruptions from isolated, accidental defects while preserving strict AOQL protection.

## 5.10 Mathematical Analysis of MIL-STD-105E Switching Rules via Markov Chains

The military sampling standard MIL-STD-105E (and its civilian equivalent ANSI/ASQ Z1.4) does not operate as an isolated sampling plan, but as an adaptive dynamic inspection system with three operational states: **Normal Inspection (State N)**, **Tightened Inspection (State T)**, and **Reduced Inspection (State R)**, plus an absorbing state of **Discontinued Inspection (State D)**.

The operational switching rules are defined as follows:
1. **Normal to Tightened**: When 2 out of 5 (or fewer) consecutive lots are rejected on original normal inspection.
2. **Tightened to Normal**: When 5 consecutive lots are accepted on original tightened inspection.
3. **Tightened to Discontinue**: When 5 lots remain on tightened inspection without reverting to normal inspection; contractual procurement is formally halted.
4. **Normal to Reduced**: When 10 consecutive lots are accepted under normal inspection, the total number of nonconforming units is below a specified limit number, production is steady, and reduced inspection is approved by the responsible authority.
5. **Reduced to Normal**: If a single lot is rejected, or if lot production becomes irregular.

### Markov Chain Formulation
Let $P_N(p)$, $P_T(p)$, and $P_R(p)$ denote the probability of lot acceptance under normal, tightened, and reduced inspection plans at incoming defect rate $p$. The entire system can be modeled as a discrete-time Markov chain with transition matrix $\mathbf{P}$.

W. R. Pabst and H. F. Dodge derived the stationary equilibrium probabilities $(\pi_N, \pi_T, \pi_R)$ of the operating system:

$$\boldsymbol{\pi} = \boldsymbol{\pi} \mathbf{P}, \qquad \pi_N + \pi_T + \pi_R = 1.0$$

The **Composite Operating Characteristic Curve ($P_{a, \text{system}}$)** of the complete MIL-STD-105E system is:

$$P_{a, \text{system}}(p) = \pi_N(p) P_N(p) + \pi_T(p) P_T(p) + \pi_R(p) P_R(p)$$

The switching mechanism dramatically steepens the overall OC curve:
- When incoming supplier quality is high ($p \le AQL$), $\pi_N + \pi_R \approx 1.0$, allowing the supplier to enjoy low inspection costs and near $100\%$ acceptance.
- As soon as incoming quality degrades beyond AQL ($p > AQL$), the system transitions with high probability into Tightened Inspection ($\pi_T \to 1.0$). If quality does not improve immediately, the probability of reaching Discontinuation approaches $1.0$, creating massive economic pressure on the vendor to maintain manufacturing discipline.

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
