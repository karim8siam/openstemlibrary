# Unit 6: Benefit Premiums, the Equivalence Principle & Loss-at-Issue Variance

## 6.1 The Equivalence Principle and the Future Loss-at-Issue Random Variable

In a commercial life insurance policy, policyholders rarely pay the entire cost of insurance as a single upfront lump sum (Net Single Premium). Instead, premiums are funded through periodic level annual installments paid throughout the duration of the policy.

Determining the actuarially fair level premium requires balancing two stochastic cash flow streams:
1. The **benefit payments** promised by the insurer to the policyholder's beneficiaries upon death.
2. The **premium payments** paid by the policyholder to the insurer while alive.

### The Future Loss-at-Issue Random Variable: ${}_0 L$
At policy issue ($t = 0$), the financial outcome of the contract from the insurer’s perspective is modeled by the **Future Loss-at-Issue Random Variable** ${}_0 L$:

$${}_0 L = \text{Present Value of Future Benefits} - \text{Present Value of Future Net Premiums}$$

Because both death benefit timing and the number of premiums paid depend on the stochastic future lifetime $T_x$, ${}_0 L$ is a continuous or discrete random variable:
- If the policyholder dies early, the insurer collects few premiums but pays the full death claim: ${}_0 L > 0$ (a financial loss to the insurer).
- If the policyholder survives for many decades, the insurer collects numerous premiums and compounds them over time: ${}_0 L < 0$ (a financial gain to the insurer).

### The Equivalence Principle
The **Equivalence Principle** (also known as the Net Premium Principle) mandates that the net level annual premium $P$ must be set such that the expected value of the future loss-at-issue is exactly zero:

$$\mathbb{E}[{}_0 L] = 0$$

$$\mathbb{E}[\text{Present Value of Future Benefits}] = \mathbb{E}[\text{Present Value of Future Net Premiums}]$$

$$\text{Actuarial Present Value of Benefits} = \text{Actuarial Present Value of Net Premiums}$$

The Equivalence Principle ensures that across a large portfolio of independent policies, the insurer’s expected underwriting profit is zero, providing a pure mathematical benchmark before administrative expenses and profit margins are added.

## 6.2 Mathematical Derivations of Net Level Premiums

Let $P$ denote the net level annual premium payable at the beginning of each year while $(x)$ is alive.

### 1. Discrete Whole Life Insurance: $P_x$
For a unit whole life insurance of $1$ payable at the end of the year of death, with premiums payable annually for life:
- Benefit APV: $A_x$
- Premium APV: $P_x \cdot \ddot{a}_x$

Applying the Equivalence Principle:
$$P_x \cdot \ddot{a}_x = A_x \implies P_x = \frac{A_x}{\ddot{a}_x}$$

Using commutation functions:
$$P_x = \frac{M_x / D_x}{N_x / D_x} = \frac{M_x}{N_x}$$

Using the identity $A_x = 1 - d \ddot{a}_x$:
$$P_x = \frac{1 - d \ddot{a}_x}{\ddot{a}_x} = \frac{1}{\ddot{a}_x} - d$$

### 2. $n$-Year Term Insurance: $P_{x:\overline{n}|}^1$
Premiums are paid annually for at most $n$ years (an $n$-year temporary annuity-due $\ddot{a}_{x:\overline{n}|}$), and benefits are paid only if death occurs within $n$ years:

$$P_{x:\overline{n}|}^1 \cdot \ddot{a}_{x:\overline{n}|} = A_{x:\overline{n}|}^1 \implies P_{x:\overline{n}|}^1 = \frac{A_{x:\overline{n}|}^1}{\ddot{a}_{x:\overline{n}|}} = \frac{M_x - M_{x+n}}{N_x - N_{x+n}}$$

### 3. $n$-Year Pure Endowment: $P_{x:\overline{n}|}^{\;\;1}$
Premiums are paid annually for at most $n$ years, and $1$ unit is paid at time $n$ if $(x)$ survives:

$$P_{x:\overline{n}|}^{\;\;1} \cdot \ddot{a}_{x:\overline{n}|} = {}_n E_x \implies P_{x:\overline{n}|}^{\;\;1} = \frac{{}_n E_x}{\ddot{a}_{x:\overline{n}|}} = \frac{D_{x+n}}{N_x - N_{x+n}}$$

### 4. $n$-Year Endowment Insurance: $P_{x:\overline{n}|}$
Combines term insurance and pure endowment:

$$P_{x:\overline{n}|} = \frac{A_{x:\overline{n}|}}{\ddot{a}_{x:\overline{n}|}} = \frac{A_{x:\overline{n}|}^1 + {}_n E_x}{\ddot{a}_{x:\overline{n}|}} = \frac{M_x - M_{x+n} + D_{x+n}}{N_x - N_{x+n}} = \frac{1}{\ddot{a}_{x:\overline{n}|}} - d$$

Notice that $P_{x:\overline{n}|} = P_{x:\overline{n}|}^1 + P_{x:\overline{n}|}^{\;\;1}$.

### 5. Limited-Payment Whole Life Insurance: ${}_h P_x$
Premiums are paid for at most $h$ years ($h < \omega - x$), but insurance coverage continues for the entire remaining lifetime:

$${}_h P_x \cdot \ddot{a}_{x:\overline{h}|} = A_x \implies {}_h P_x = \frac{A_x}{\ddot{a}_{x:\overline{h}|}} = \frac{M_x}{N_x - N_{x+h}}$$

## 6.3 Continuous Benefit Premiums: $\bar{P}(\bar{A}_x)$

In continuous insurance models, death benefits are paid at the moment of death, and premiums are collected continuously at a constant annual rate $\bar{P}$:

$$\text{Benefit APV} = \bar{A}_x, \qquad \text{Premium APV} = \bar{P} \cdot \bar{a}_x$$

Applying the Equivalence Principle:

$$\bar{P}(\bar{A}_x) = \frac{\bar{A}_x}{\bar{a}_x} = \frac{1 - \delta \bar{a}_x}{\bar{a}_x} = \frac{1}{\bar{a}_x} - \delta$$

Under constant force of mortality $\mu$ and constant force of interest $\delta$:
$$\bar{A}_x = \frac{\mu}{\delta + \mu}, \qquad \bar{a}_x = \frac{1}{\delta + \mu}$$
$$\bar{P}(\bar{A}_x) = \frac{\mu / (\delta + \mu)}{1 / (\delta + \mu)} = \mu$$
When mortality and interest forces are constant, the continuous net premium equals the instantaneous hazard of death $\mu$, completely independent of the interest rate $\delta$!

## 6.4 Variance of the Future Loss-at-Issue: $\text{Var}({}_0 L)$

While the Equivalence Principle guarantees $\mathbb{E}[{}_0 L] = 0$, the insurer incurs underwriting risk because the variance $\text{Var}({}_0 L) > 0$.

### Discrete Whole Life Insurance
For a discrete whole life policy with sum insured $b = 1$ and net annual premium $P_x$:
$${}_0 L = v^{K_x + 1} - P_x \ddot{a}_{\overline{K_x + 1}|}$$
Substitute $\ddot{a}_{\overline{K_x + 1}|} = \frac{1 - v^{K_x + 1}}{d}$:
$${}_0 L = v^{K_x + 1} - P_x \left( \frac{1 - v^{K_x + 1}}{d} \right) = v^{K_x + 1} \left( 1 + \frac{P_x}{d} \right) - \frac{P_x}{d}$$

Notice that ${}_0 L$ is a linear transformation of the single random variable $Z = v^{K_x + 1}$!
Taking the variance:

$$\text{Var}({}_0 L) = \left( 1 + \frac{P_x}{d} \right)^2 \text{Var}(v^{K_x + 1}) = \left( 1 + \frac{P_x}{d} \right)^2 \left[ {}^2 A_x - (A_x)^2 \right]$$

Since $1 + \frac{P_x}{d} = 1 + \frac{A_x / \ddot{a}_x}{d} = \frac{d \ddot{a}_x + A_x}{d \ddot{a}_x} = \frac{1}{d \ddot{a}_x} = \frac{1}{1 - A_x}$:

$$\text{Var}({}_0 L) = \frac{{}^2 A_x - (A_x)^2}{(1 - A_x)^2}$$

### Continuous Whole Life Insurance
In continuous time:
$${}_0 \bar{L} = v^{T_x} \left( 1 + \frac{\bar{P}}{\delta} \right) - \frac{\bar{P}}{\delta}$$

$$\text{Var}({}_0 \bar{L}) = \left( 1 + \frac{\bar{P}}{\delta} \right)^2 \left[ {}^2\bar{A}_x - (\bar{A}_x)^2 \right] = \frac{{}^2\bar{A}_x - (\bar{A}_x)^2}{(1 - \bar{A}_x)^2}$$

This formula reveals why life insurance policies on elderly lives carry higher variance: both the level premium $P_x$ and mortality rates increase rapidly with age, inflating the loss multiplier $(1 + P/d)^2$.

## 6.5 The Percentile Premium Principle and Ruin Bounds

An insurer managing a portfolio of $N$ policies cannot rely solely on the Equivalence Principle if capital reserves are constrained. If premiums are set strictly at $\mathbb{E}[{}_0 L] = 0$, by the Central Limit Theorem there is an approximate $50\%$ probability that aggregate claims will exceed aggregate premiums!

Under the **Percentile Premium Principle**, the premium $P^*$ is determined such that the probability of the insurer incurring a net financial loss on the contract is capped at an acceptable risk ceiling $\alpha$ (e.g., $\alpha = 0.05$ or $0.01$):

$$P({}_0 L > 0) \le \alpha$$

For a whole life policy:
$${}_0 L > 0 \iff v^{K_x + 1} \left( 1 + \frac{P^*}{d} \right) - \frac{P^*}{d} > 0 \iff v^{K_x + 1} > \frac{P^*}{P^* + d} \iff K_x + 1 < \frac{\ln\left(\frac{P^*}{P^* + d}\right)}{\ln v}$$

Let $k^*$ be the critical duration threshold such that $P(K_x \le k^*) = {}_{k^* + 1} q_x \le \alpha$. The percentile premium is:

$$P^* = \frac{d \cdot v^{k^* + 1}}{1 - v^{k^* + 1}}$$

The percentile premium guarantees that the contract produces an underwriting profit with probability at least $1 - \alpha$.

## 6.6 Gross Premiums: Incorporating Expenses and Loadings

Net level premiums consider only death benefit disbursements. In commercial operations, an insurance company incurs substantial operational expenses:
1. **Acquisition Expenses**: Medical underwriting examinations, agent sales commissions, advertising, and policy setup costs incurred in Year 1.
2. **Renewal Expenses**: Premium collection fees, customer service, IT system maintenance, and accounting audits incurred in Years $2, 3, \dots, n$.
3. **Claim Settlement Expenses**: Legal verification of death certificates, claims investigation, and disbursements.
4. **Profit and Contingency Loadings**: Shareholder return on regulatory solvency capital and safety margins against epidemic spikes.

Let $G$ denote the **Gross Annual Premium** payable at the start of each year.
Expenses are categorized as:
- Fraction of gross premium in Year 1: $c_0 \cdot G$ (e.g., $50\%$ agent commission).
- Fraction of gross premium in Renewal Years ($t \ge 2$): $c_1 \cdot G$ (e.g., $5\%$ administrative commission).
- Fixed dollar cost per policy in Year 1: $e_0$ (e.g., $500\text{ BDT}$ policy setup fee).
- Fixed dollar cost per policy in Renewal Years ($t \ge 2$): $e_1$ (e.g., $50\text{ BDT}$ maintenance fee).
- Claim settlement expense per unit death benefit: $e_c$ (e.g., $1\%$ of sum insured $b$).

### The Gross Premium Equation of Value
$$\mathbb{E}[\text{PV of Gross Premiums}] = \mathbb{E}[\text{PV of Benefits}] + \mathbb{E}[\text{PV of All Expenses}]$$

$$G \cdot \ddot{a}_{x:\overline{n}|} = b(1 + e_c) A_{x:\overline{n}|}^1 + \left[ c_0 G + c_1 G a_{x:\overline{n-1}|} \right] + \left[ e_0 + e_1 a_{x:\overline{n-1}|} \right]$$

Since $a_{x:\overline{n-1}|} = \ddot{a}_{x:\overline{n}|} - 1$, gathering all terms involving $G$ on the left side:

$$G \left[ \ddot{a}_{x:\overline{n}|} - c_0 - c_1 (\ddot{a}_{x:\overline{n}|} - 1) \right] = b(1 + e_c) A_{x:\overline{n}|}^1 + e_0 + e_1 (\ddot{a}_{x:\overline{n}|} - 1)$$

$$G = \frac{b(1 + e_c) A_{x:\overline{n}|}^1 + (e_0 - e_1) + e_1 \ddot{a}_{x:\overline{n}|}}{(1 - c_1) \ddot{a}_{x:\overline{n}|} - (c_0 - c_1)}$$

This formulation enables actuarial pricing departments to calculate commercially viable consumer premiums that ensure company solvency and profitability.

## 6.7 Second Moments and Variance of Present Value Random Variables

Actuarial pricing based strictly on the Equivalence Principle (where the premium $P$ satisfies $\mathbb{E}[L] = 0$) guarantees expected solvency only over an infinite pool of independent policyholders by the Weak Law of Large Numbers. In commercial reality, an insurer holds a finite portfolio of policies and must hold regulatory surplus capital to protect against stochastic mortality fluctuations.

To quantify solvency margins and calculate the probability of underwriting ruin, actuaries derive the variance of the present value of benefit payment random variables.

### 1. Whole Life Insurance Benefit Present Value ($Z$)
Let $Z = v^{T_x} = e^{-\delta T_x}$ denote the continuous present value random variable for a unit whole life insurance benefit issued to $(x)$, payable at the moment of death.

The expected value (Net Single Premium) is:
$$\mathbb{E}[Z] = \bar{A}_x = \int_0^\infty e^{-\delta t} {}_t p_x \mu_{x+t}\,dt$$

The second raw moment of $Z$ is:
$$\mathbb{E}[Z^2] = \mathbb{E}\left[ (e^{-\delta T_x})^2 \right] = \mathbb{E}\left[ e^{-2\delta T_x} \right] = \int_0^\infty e^{-2\delta t} {}_t p_x \mu_{x+t}\,dt$$

Notice that this integral is identical to the net single premium formula, but evaluated at twice the force of interest ($2\delta$). In standard international actuarial notation, an insurance symbol with a superscript 2 on the upper left denotes evaluation at twice the force of interest:
$$\mathbb{E}[Z^2] = {}^2\bar{A}_x \quad \text{evaluated at force } \delta^* = 2\delta \text{ (or interest rate } i^* = (1 + i)^2 - 1 = 2i + i^2)$$

The variance of the benefit present value is:
$$\mathrm{Var}(Z) = \mathbb{E}[Z^2] - (\mathbb{E}[Z])^2 = {}^2\bar{A}_x - (\bar{A}_x)^2$$

### 2. Discrete Whole Life Insurance
For a policy paying 1 at the end of the year of death, $Z_{\text{disc}} = v^{K_x + 1}$:
$$\mathbb{E}[Z_{\text{disc}}] = A_x = \sum_{k=0}^\infty v^{k+1} {}_k p_x q_{x+k}$$
$$\mathbb{E}[Z_{\text{disc}}^2] = \sum_{k=0}^\infty (v^{k+1})^2 {}_k p_x q_{x+k} = {}^2A_x$$
$$\mathrm{Var}(Z_{\text{disc}}) = {}^2A_x - (A_x)^2$$

### 3. Portfolio Percentile Premium Principle
Consider an insurer issuing $N$ independent, identically distributed life insurance policies to individuals aged $x$, each with benefit face amount $S$. The aggregate claims present value is:
$$S_N = \sum_{j=1}^N S \cdot Z_j$$
By independence:
$$\mathbb{E}[S_N] = N \cdot S \cdot A_x, \quad \mathrm{Var}(S_N) = N \cdot S^2 \cdot \mathrm{Var}(Z) = N \cdot S^2 \left( {}^2A_x - (A_x)^2 \right)$$

By the Central Limit Theorem, for large $N$, $S_N$ is approximately Gaussian:
$$S_N \sim \mathcal{N}\left( N S A_x, \; N S^2 [{}^2A_x - (A_x)^2] \right)$$

If the insurer collects a total single premium $\Pi_{\text{total}}$ and requires a $99\%$ solvency probability that aggregate claims do not exceed available premium capital ($P(S_N \le \Pi_{\text{total}}) = 0.99$):
$$\Pi_{\text{total}} = \mathbb{E}[S_N] + z_{0.99} \sqrt{\mathrm{Var}(S_N)} = N S A_x + 2.326 \cdot S \sqrt{N [{}^2A_x - (A_x)^2]}$$

The required premium per policy $\pi = \Pi_{\text{total}} / N$ is:
$$\pi = S A_x + 2.326 \frac{S \sqrt{{}^2A_x - (A_x)^2}}{\sqrt{N}}$$
As portfolio size $N \to \infty$, the risk margin per policy shrinks at rate $\mathcal{O}(1/\sqrt{N})$, mathematically demonstrating the fundamental economic principle of insurance pooling and risk diversification.

## 6.8 Expense-Loaded Gross Premiums and Profit Testing

The net premium $P_x$ covers strictly the expected cost of mortality benefits. In corporate actuarial practice, life insurance products must bear substantial administrative, underwriting, distribution, and capital costs. The actual premium charged to the consumer is the **Gross Premium** $G$.

### 1. Classification of Actuarial Expenses
Expenses are categorized into three structural types:
1. **Percentage of Premium Expenses ($c_t$)**: Commissions paid to sales agents and brokers, premium collection taxes, and licensing fees. These are expressed as a fraction of gross premium $G$:
   - First-year commission rate $c_1$ (frequently $50\% - 90\%$ of first-year premium).
   - Renewal commission rates $c_t$ for $t \ge 2$ (typically $3\% - 7\%$).
2. **Per-Policy Expenses ($e_t$)**: Policy establishment charges, underwriting medical examinations, policy issuance fees, and ongoing customer billing overhead:
   - First-year initial overhead $e_1$ (e.g., $\$150$ per policy).
   - Renewal administrative maintenance $e_t$ for $t \ge 2$ (e.g., $\$25$ per policy per year).
3. **Per-Face-Amount Expenses ($f_t$)**: Claim settlement investigation fees, death benefit legal processing, and reinsurance reporting costs (e.g., $\$1.50$ per $\$1,000$ of death benefit).

### 2. The Gross Premium Equation of Value
For a fully discrete whole life insurance policy with face amount $S$ issued to $(x)$, the Equivalence Principle states that at policy inception:
$$PV(\text{Gross Premiums}) = PV(\text{Death Benefits}) + PV(\text{Expenses})$$

Let $G$ be the level annual gross premium payable at the beginning of each year. The present value of gross premiums is $G \cdot \ddot{a}_x$.
The present value of death benefits is $S \cdot A_x$.
The present value of expenses is:
$$PV(\text{Expenses}) = (c_1 G + e_1 + f_1 S) + \sum_{k=1}^\infty v^k {}_k p_x (c_r G + e_r + f_r S)$$
where $c_r, e_r, f_r$ are the renewal expense rates.

Since $\sum_{k=1}^\infty v^k {}_k p_x = \ddot{a}_x - 1$, we can group the expense terms:
$$PV(\text{Expenses}) = G \left[ c_r \ddot{a}_x + (c_1 - c_r) \right] + \left[ e_r \ddot{a}_x + (e_1 - e_r) \right] + S \left[ f_r A_x + (f_1 - f_r) \right]$$

Equating $PV(\text{Gross Premiums}) = PV(\text{Benefits}) + PV(\text{Expenses})$ and isolating $G$:

$$G = \frac{S (A_x + f_r A_x + f_1 - f_r) + e_r \ddot{a}_x + (e_1 - e_r)}{\ddot{a}_x (1 - c_r) - (c_1 - c_r)}$$

This analytical expression demonstrates that heavily front-loaded initial commissions ($c_1 \gg c_r$) and issuance fees ($e_1 \gg e_r$) reduce the net denominator, forcing gross premiums significantly above the pure risk rate.

## 6.9 Continuous vs Discrete Benefit Conversions: The Claims Acceleration Factor

In statutory life insurance contracts, death benefits are legally payable immediately upon receipt of proof of death—essentially at the moment of death $T_x$. However, classical actuarial life tables evaluate discrete end-of-year death benefits $A_x = \sum_{k=0}^\infty v^{k+1} {}_k p_x q_{x+k}$.

Actuaries establish rigorous mathematical links between continuous insurances $\bar{A}_x$ and discrete insurances $A_x$ using fractional age mortality assumptions.

### 1. Exact Derivation under Uniform Distribution of Deaths (UDD)
Under UDD, deaths in each year of age $[k, k+1)$ occur uniformly throughout the year. The future lifetime random variable can be decomposed as:
$$T_x = K_x + S$$
where $K_x = \lfloor T_x \rfloor$ is the curtate future lifetime (an integer), and $S = T_x - K_x$ is the fractional year of death, uniformly distributed on $[0, 1)$ and statistically independent of $K_x$.

The present value of a unit benefit payable at the moment of death is:
$$\bar{Z} = v^{T_x} = v^{K_x + S} = v^{K_x + 1} \cdot v^{S - 1}$$

Taking the mathematical expectation:
$$\bar{A}_x = \mathbb{E}[\bar{Z}] = \mathbb{E}[v^{K_x + 1} \cdot v^{S - 1}] = \mathbb{E}[v^{K_x + 1}] \cdot \mathbb{E}[v^{S - 1}]$$
Since $\mathbb{E}[v^{K_x + 1}] = A_x$, we evaluate the expectation of $v^{S - 1} = (1 + i)^{1 - S}$:
$$\mathbb{E}[(1 + i)^{1 - S}] = \int_0^1 (1 + i)^{1 - s} \cdot 1\,ds = (1 + i) \int_0^1 e^{-\delta s}\,ds = (1 + i) \left[ \frac{1 - e^{-\delta}}{\delta} \right]$$
Since $1 - e^{-\delta} = 1 - v = d$, and $(1 + i) d = i$:

$$\mathbb{E}[(1 + i)^{1 - S}] = \frac{(1 + i) d}{\delta} = \frac{i}{\delta}$$

Therefore, under UDD, the exact continuous whole life net single premium is:

$$\bar{A}_x = \frac{i}{\delta} A_x$$

The conversion factor $\frac{i}{\delta}$ is known as the **Claims Acceleration Factor**.

### 2. Numerical Series Expansion and Claims Acceleration Intuition
Expanding $i/\delta$ in powers of interest rate $i$:
$$\frac{i}{\delta} = \frac{i}{\ln(1 + i)} = \frac{i}{i - \frac{1}{2}i^2 + \frac{1}{3}i^3 - \dots} \approx \frac{1}{1 - \frac{1}{2}i} \approx 1 + \frac{i}{2}$$

Substituting this approximation yields:
$$\bar{A}_x \approx \left( 1 + \frac{i}{2} \right) A_x = (1 + i)^{1/2} A_x$$
*Actuarial Intuition*: Because deaths are uniformly distributed, death claims occur on average at the midpoint of the year of death ($t = k + 0.5$). An insurer paying claims at midpoint earns only half a year of interest compared to end-of-year settlement ($t = k + 1$). Thus, the net single premium must be increased by approximately half a year's interest ($1 + i/2$) to compensate for lost investment earnings.

For an interest rate of $i = 6\%$, $\delta = \ln(1.06) \approx 0.0582689$. The claims acceleration factor is:
$$\frac{0.06}{0.0582689} \approx 1.02971$$
Paying claims immediately upon death increases the required insurance premium by nearly $3\%$.

## 6.10 Joint Life and Last Survivor Insurance: Foundational Identities

When life insurance benefits or annuity cash flows protect couples, families, or business partners, actuaries price contracts defined on multi-life statuses.

### 1. Definitions of Multi-Life Statuses
Let $(x)$ and $(y)$ be two lives with future lifetimes $T_x$ and $T_y$.
1. **The Joint Life Status ($(xy)$)**: Survives as long as *both* lives survive, and fails at the moment of the first death:
   $$T_{xy} = \min(T_x, T_y)$$
   Survival probability under independence:
   $${}_t p_{xy} = P(T_x > t, T_y > t) = {}_t p_x \cdot {}_t p_y$$
2. **The Last Survivor Status ($(\overline{xy})$)**: Survives as long as *at least one* life survives, and fails at the moment of the second (last) death:
   $$T_{\overline{xy}} = \max(T_x, T_y)$$
   Survival probability:
   $${}_t p_{\overline{xy}} = P(T_{\overline{xy}} > t) = 1 - P(T_x \le t, T_y \le t) = 1 - (1 - {}_t p_x)(1 - {}_t p_y) = {}_t p_x + {}_t p_y - {}_t p_{xy}$$

### 2. The Fundamental Algebraic Valuation Identities
From the elementary arithmetic property of real numbers:
$$\min(u, v) + \max(u, v) = u + v$$
Applying this to the survival random variables:
$$T_{xy} + T_{\overline{xy}} = T_x + T_y$$

For any linear discounted present value cash flow functional $\mathcal{L}(\cdot)$, this identity extends to insurance and annuity valuation:
1. **Life Annuities**:
   $$\bar{a}_{xy} + \bar{a}_{\overline{xy}} = \bar{a}_x + \bar{a}_y \implies \bar{a}_{\overline{xy}} = \bar{a}_x + \bar{a}_y - \bar{a}_{xy}$$
   Similarly for discrete annuities:
   $$\ddot{a}_{\overline{xy}} = \ddot{a}_x + \ddot{a}_y - \ddot{a}_{xy}$$
2. **Life Assurances**:
   $$\bar{A}_{xy} + \bar{A}_{\overline{xy}} = \bar{A}_x + \bar{A}_y \implies \bar{A}_{\overline{xy}} = \bar{A}_x + \bar{A}_y - \bar{A}_{xy}$$

*Actuarial Pricing Application*: An insurer offering a "last-to-die" survivor life insurance policy (which pays benefit $S$ upon the second death to fund estate taxes) computes the net single premium simply by evaluating the two single-life premiums and subtracting the joint-life premium:
$$\bar{A}_{\overline{xy}} = \bar{A}_x + \bar{A}_y - \bar{A}_{xy}$$
Because $\bar{A}_{xy} > \max(\bar{A}_x, \bar{A}_y)$, the last survivor insurance premium is significantly lower than either single life premium, reflecting the substantially longer expected waiting time until both lives perish.

## 6.11 Market-Consistent Embedded Value (MCEV) and Profit Signatures

In life insurance financial reporting and mergers and acquisitions (M&A), accounting standards based on historical book value fail to capture the true economic value of long-term insurance policies in force. The global insurance industry utilizes **Market-Consistent Embedded Value (MCEV)**.

### 1. Components of Market-Consistent Embedded Value
MCEV measures the consolidated economic value of the shareholders' interest in the life insurance enterprise, decomposed into two primary pillars:

$$\text{MCEV} = \text{Adjusted Net Worth (ANW)} + \text{Value of Business in Force (VIF)}$$

1. **Adjusted Net Worth (ANW)**: The market value of free shareholder capital backing the business:
   $$\text{ANW} = \text{Free Surplus} + \text{Required Capital}$$
   - *Free Surplus*: Unencumbered shareholder capital immediately available for distribution.
   - *Required Capital*: Capital earmarked to meet statutory solvency margins (such as Solvency II Solvency Capital Requirement - SCR).
2. **Value of Business in Force (VIF)**: The present value of future profits emerging from in-force policies, adjusted for frictional capital costs and non-hedgeable risks:
   $$\text{VIF} = \text{PVFP} - \text{FOG} - \text{CoC} - \text{CRNHR}$$
   - **PVFP (Present Value of Future Profits)**: Discounted projected cash flows generated by the policy block under certainty-equivalent risk-neutral interest rates.
   - **FOG (Time Value of Financial Options and Guarantees)**: The market value of stochastic interest rate options embedded in policies (such as minimum guaranteed surrender rates or annuity conversion options).
   - **CoC (Frictional Cost of Required Capital)**: The drag from corporate taxation and investment management fees on capital locked in the company to meet regulatory requirements.
   - **CRNHR (Cost of Residual Non-Hedgeable Risks)**: A risk margin compensating shareholders for non-financial underwriting risks that cannot be dynamically hedged in capital markets (such as pandemic mortality spikes or operational failures).

### 2. Profit Signatures and Internal Rate of Return (IRR)
To model the PVFP, the actuary constructs the annual **Profit Vector** $\mathbf{Pr}_t$, defining the projected net cash flow per policy surviving to duration $t$.

Multiplying $\mathbf{Pr}_t$ by the probability that a policy is still in force at duration $t-1$ (${}_{t-1} p_x^{(\tau)}$) yields the **Profit Signature** $\mathbf{\Pi}_t$:
$$\mathbf{\Pi}_t = \mathbf{Pr}_t \cdot {}_{t-1} p_x^{(\tau)}$$

- At $t = 0$: $\mathbf{\Pi}_0 = -(\text{Initial Acquisition and Underwriting Strain}) < 0$.
- At $t \ge 1$: $\mathbf{\Pi}_t = \text{Surplus emerging from premium margins and investment gains} > 0$.

The **Net Present Value of Profits (NPV)** discounted at the shareholder hurdle rate $r_{\text{hurdle}}$ is:
$$NPV = \sum_{t=0}^n \frac{\mathbf{\Pi}_t}{(1 + r_{\text{hurdle}})^t}$$

The **Internal Rate of Return (IRR)** is the discount rate $i^*$ satisfying:
$$\sum_{t=0}^n \frac{\mathbf{\Pi}_t}{(1 + i^*)^t} = 0$$
A new insurance product is approved for commercial launch only if $IRR > r_{\text{hurdle}}$, guaranteeing shareholder value creation.

## 6.12 Modern Unbundled Life Contracts: Universal Life Insurance Mechanics

Traditional whole life contracts bundle investment returns, mortality costs, and expense loadings into an indivisible level premium. In contrast, **Universal Life (UL)** insurance unbundles these components into an explicit, transparent cash accumulation fund:

$$\text{Account Value}_{t+1} = \left[ \text{Account Value}_t + \text{Premium}_t - \text{Expense Charges}_t - \text{COI}_t \right] \times (1 + i_t^{\text{credited}})$$

where:
- $\text{Premium}_t$: Flexible premium payments chosen by the policyholder.
- $\text{Expense Charges}_t$: Explicit policy administration fees and premium taxes.
- $\text{COI}_t$: The **Cost of Insurance** charge deducted monthly to cover pure mortality risk.
- $i_t^{\text{credited}}$: The credited interest rate declared by the insurer (subject to a contractual minimum guarantee, e.g., $2.0\%$).

### 1. Cost of Insurance (COI) Mechanics
The Cost of Insurance deducted at month $t$ is calculated as:
$$\text{COI}_t = q_{x+t / 12}^{\text{COI}} \times \text{Net Amount at Risk}_t$$
where $q_{x+t/12}^{\text{COI}}$ is the insurer's monthly mortality charge per unit of risk.

### 2. Death Benefit Structures: Option A vs Option B
Universal life policies offer two distinct death benefit designs:
1. **Option A (Level Death Benefit)**: The total death benefit remains constant at face amount $F$.
   - The Net Amount at Risk (NAR) decreases as the account value accumulates:
     $$\text{NAR}_t = F - \text{Account Value}_t$$
   - Because NAR shrinks, COI charges decline, allowing cash value to grow faster in later years.
2. **Option B (Increasing Death Benefit)**: The total death benefit equals the face amount $F$ plus the entire cash account value:
   $$\text{Total Death Benefit}_t = F + \text{Account Value}_t$$
   - The Net Amount at Risk remains constant at $F$ for all durations:
     $$\text{NAR}_t = F$$
   - COI charges increase steadily with age as the mortality rate $q_{x+t}$ escalates, demanding higher ongoing premium contributions to prevent policy lapse.

Universal life flexibility enables policyholders to adjust premium contributions and face amounts over their lifecycles, establishing UL as the dominant life insurance architecture in North American financial markets.

## Fully worked question 1: Net Level Premium Derivation and Commutation Calculations

### Question
An actuarial life table extract at an effective annual interest rate of $i = 6.00\%$ ($i = 0.06$, $d = 0.06/1.06 \approx 0.0566038$) provides the following commutation values:
- $D_{35} = 22,000$
- $D_{55} = 6,600$
- $D_{65} = 3,300$
- $M_{35} = 5,500$
- $M_{55} = 3,850$
- $M_{65} = 2,640$
- $N_{35} = 330,000$
- $N_{55} = 88,000$
- $N_{65} = 36,300$

A life aged $35$ purchases a policy with a sum insured of $b = 500,000\text{ BDT}$. Compute the net level annual premium payable annually in advance for:
1. A Whole Life Insurance policy ($500,000 P_{35}$).
2. A 20-Year Term Insurance policy ($500,000 P_{35:\overline{20}|}^1$).
3. A 20-Year Endowment Insurance policy ($500,000 P_{35:\overline{20}|}$).
4. A 20-Year Limited-Payment Whole Life Insurance policy ($500,000 {}_{20} P_{35}$).
5. Verify numerically that $P_{35:\overline{20}|} > P_{35} > {}_{20} P_{35} > P_{35:\overline{20}|}^1$.

### Solution, step 1: Whole life net annual premium $P_{35}$
Using $P_x = M_x / N_x$:
$$P_{35} = \frac{M_{35}}{N_{35}} = \frac{5,500}{330,000} = \frac{1}{60} \approx 0.016667$$
For a sum insured of $500,000\text{ BDT}$:
$$\text{Premium}_{\text{whole life}} = 500,000 \times 0.016667 = 8,333.33\text{ BDT/year}$$

### Solution, step 2: 20-Year term insurance net annual premium $P_{35:\overline{20}|}^1$
For a 20-year term from age 35, terminal age is $35 + 20 = 55$:
$$P_{35:\overline{20}|}^1 = \frac{M_{35} - M_{55}}{N_{35} - N_{55}} = \frac{5,500 - 3,850}{330,000 - 88,000} = \frac{1,650}{242,000} \approx 0.00681818$$
For a sum insured of $500,000\text{ BDT}$:
$$\text{Premium}_{\text{term}} = 500,000 \times 0.00681818 = 3,409.09\text{ BDT/year}$$

### Solution, step 3: 20-Year endowment insurance net annual premium $P_{35:\overline{20}|}$
$$P_{35:\overline{20}|} = \frac{M_{35} - M_{55} + D_{55}}{N_{35} - N_{55}} = \frac{5,500 - 3,850 + 6,600}{242,000} = \frac{1,650 + 6,600}{242,000} = \frac{8,250}{242,000} \approx 0.03409091$$
For a sum insured of $500,000\text{ BDT}$:
$$\text{Premium}_{\text{endowment}} = 500,000 \times 0.03409091 = 17,045.45\text{ BDT/year}$$

### Solution, step 4: 20-Year limited-payment whole life net annual premium ${}_{20} P_{35}$
Coverage is for whole life ($M_{35}$), but premiums are paid for at most 20 years ($N_{35} - N_{55}$):
$${}_{20} P_{35} = \frac{M_{35}}{N_{35} - N_{55}} = \frac{5,500}{242,000} \approx 0.02272727$$
For a sum insured of $500,000\text{ BDT}$:
$$\text{Premium}_{\text{limited}} = 500,000 \times 0.02272727 = 11,363.64\text{ BDT/year}$$

### Solution, step 5: Comparison of net annual premiums
Collating annual premiums for $500,000\text{ BDT}$ coverage:
- 20-Year Endowment: $17,045.45\text{ BDT/year}$
- 20-Pay Whole Life: $11,363.64\text{ BDT/year}$
- Ordinary Whole Life: $8,333.33\text{ BDT/year}$
- 20-Year Term: $3,409.09\text{ BDT/year}$

Checking ordering:
$$17,045.45 > 11,363.64 > 8,333.33 > 3,409.09$$
$$P_{35:\overline{20}|} > {}_{20} P_{35} > P_{35} > P_{35:\overline{20}|}^1$$
The economic ordering holds: Endowment is highest because it guarantees a payout whether $(x)$ lives or dies; Term is lowest because it pays only if $(x)$ dies within 20 years.

## Fully worked question 2: Loss-at-Issue Variance and Policyholder Risk Profiles

### Question
An insurance company issues a discrete whole life policy of $b = 100,000\text{ BDT}$ to a life aged $x = 45$. Net level annual premiums $P = 100,000 P_{45}$ are payable at the start of each year for life.

The actuarial parameters at effective interest rate $i = 5.00\%$ ($i = 0.05, d = 0.05/1.05 \approx 0.047619$) are:
- $A_{45} = 0.20120$
- ${}^2 A_{45} = 0.06850$

Perform the following calculations:
1. Compute the net level annual premium $P$.
2. Compute the variance of the present value of the death benefit $\text{Var}(b v^{K_{45} + 1})$.
3. Compute the variance $\text{Var}({}_0 L)$ and standard deviation $\sigma({}_0 L)$ of the future loss-at-issue random variable.
4. Calculate the financial loss ${}_0 L$ incurred by the insurer if the policyholder dies:
   - In Policy Year 1 ($K_{45} = 0$)
   - In Policy Year 5 ($K_{45} = 4$)
   - In Policy Year 30 ($K_{45} = 29$)

### Solution, step 1: Net level annual premium $P$
Using the duality relation $\ddot{a}_{45} = (1 - A_{45}) / d$:
$$\ddot{a}_{45} = \frac{1 - 0.20120}{0.047619} = \frac{0.79880}{0.047619} \approx 16.7748$$
$$P_{45} = \frac{A_{45}}{\ddot{a}_{45}} = \frac{0.20120}{16.7748} \approx 0.011994$$
For a sum insured of $100,000\text{ BDT}$:
$$P = 100,000 \times 0.011994 = 1,199.40\text{ BDT/year}$$

### Solution, step 2: Variance of death benefit present value
$$\text{Var}(Z) = b^2 [{}^2 A_{45} - (A_{45})^2] = (100,000)^2 [0.06850 - (0.20120)^2]$$
$$(0.20120)^2 \approx 0.040481$$
$${}^2 A_{45} - (A_{45})^2 = 0.06850 - 0.040481 = 0.028019$$
$$\text{Var}(Z) = 10^{10} \times 0.028019 = 280,190,000\text{ BDT}^2$$

### Solution, step 3: Variance and standard deviation of loss-at-issue ${}_0 L$
The loss multiplier is:
$$1 + \frac{P_{45}}{d} = 1 + \frac{0.011994}{0.047619} = 1 + 0.251874 = 1.251874$$
$$\left( 1 + \frac{P_{45}}{d} \right)^2 = (1.251874)^2 \approx 1.567189$$
The variance of ${}_0 L$ is:
$$\text{Var}({}_0 L) = \left( 1 + \frac{P_{45}}{d} \right)^2 \text{Var}(Z) = 1.567189 \times 280,190,000 \approx 439,110,686\text{ BDT}^2$$
The standard deviation is:
$$\sigma({}_0 L) = \sqrt{439,110,686} \approx 20,955\text{ BDT}$$

### Solution, step 4: Realized loss ${}_0 L$ across different death years
Formula for realized loss given death in year $K + 1$:
$${}_0 L = 100,000 v^{K+1} - P \ddot{a}_{\overline{K+1}|}$$
1. **Death in Year 1 ($K = 0$)**:
   $v^1 = (1.05)^{-1} \approx 0.952381$. Only $1$ premium is paid ($P = 1,199.40\text{ BDT}$).
   $${}_0 L = 100,000(0.952381) - 1,199.40 = 95,238.10 - 1,199.40 = +94,038.70\text{ BDT}$$
   The insurer suffers a catastrophic loss of **$+94,039\text{ BDT}$** on this single policy!

2. **Death in Year 5 ($K = 4$)**:
   $v^5 = (1.05)^{-5} \approx 0.783526$.
   $$\ddot{a}_{\overline{5}|} = \frac{1 - v^5}{d} = \frac{1 - 0.783526}{0.047619} \approx 4.54595$$
   $${}_0 L = 100,000(0.783526) - 1,199.40(4.54595) = 78,352.60 - 5,452.41 = +72,900.19\text{ BDT}$$
   The insurer suffers a loss of **$+72,900\text{ BDT}$**.

3. **Death in Year 30 ($K = 29$)**:
   $v^{30} = (1.05)^{-30} \approx 0.231377$.
   $$\ddot{a}_{\overline{30}|} = \frac{1 - 0.231377}{0.047619} = \frac{0.768623}{0.047619} \approx 16.14048$$
   $${}_0 L = 100,000(0.231377) - 1,199.40(16.14048) = 23,137.70 - 19,358.90 = +3,778.80\text{ BDT}$$
   Even after 30 years, ${}_0 L > 0$ because the net annual premium was calculated for an expected future lifetime of nearly 35 years!

## Fully worked question 3: Gross Premium Pricing with Acquisition and Renewal Expenses

### Question
A commercial life insurer designs a 20-Year Endowment Insurance policy with sum insured $b = 1,000,000\text{ BDT}$ for a life aged $40$. The policy pays $1,000,000\text{ BDT}$ upon death within 20 years or upon survival to age 60.

The actuarial net values at an effective interest rate of $i = 6.00\%$ ($i = 0.06$) are:
- $A_{40:\overline{20}|}^1 = 0.08500$
- ${}_{20} E_{40} = 0.26500$
- $\ddot{a}_{40:\overline{20}|} = 11.5000$

The company's cost accounting and underwriting departments establish the following expense structure:
- Initial sales commission (Year 1): $40\%$ of first-year gross premium ($c_0 = 0.40$)
- Renewal sales commission (Years 2–20): $5\%$ of renewal gross premium ($c_1 = 0.05$)
- Initial policy setup and medical examination expense: $e_0 = 1,500\text{ BDT}$ (fixed)
- Renewal annual administrative fee: $e_1 = 200\text{ BDT/year}$ (fixed)
- Claim settlement expense: $e_c = 0.50\%$ of the face value paid upon death or maturity

Perform the following calculations:
1. Compute the net level annual premium $P_{40:\overline{20}|}$ under the Equivalence Principle.
2. Formulate the gross premium equation of value and solve for the Gross Annual Premium $G$.
3. Compute the expense loading amount ($G - P$) in BDT and as a percentage of the gross premium.
4. Calculate the total dollar expenses projected to be consumed by the policy over its full 20-year term if the policyholder survives to maturity.

### Solution, step 1: Net level annual premium $P$
Total net endowment insurance APV:
$$A_{40:\overline{20}|} = A_{40:\overline{20}|}^1 + {}_{20} E_{40} = 0.08500 + 0.26500 = 0.35000$$
The net annual premium is:
$$P = b \times \frac{A_{40:\overline{20}|}}{\ddot{a}_{40:\overline{20}|}} = 1,000,000 \times \frac{0.35000}{11.5000} \approx 30,434.78\text{ BDT/year}$$

### Solution, step 2: Gross annual premium $G$
Let $G$ denote the gross annual premium.
1. **Present Value of Gross Premiums**:
   $$PV(\text{Premiums}) = G \cdot \ddot{a}_{40:\overline{20}|} = 11.5000 G$$

2. **Present Value of Benefits plus Claim Expenses**:
   Total benefit with $0.50\%$ claim expense $= 1,000,000 \times 1.005 = 1,005,000\text{ BDT}$.
   $$PV(\text{Benefits}) = 1,005,000 \times A_{40:\overline{20}|} = 1,005,000 \times 0.35000 = 351,750\text{ BDT}$$

3. **Present Value of Percentage Premium Expenses**:
   - Year 1: $c_0 G = 0.40 G$
   - Years 2–20: $c_1 G a_{40:\overline{19}|} = 0.05 G (\ddot{a}_{40:\overline{20}|} - 1) = 0.05 G (11.5000 - 1) = 0.05 G (10.5000) = 0.5250 G$
   - Total Percentage Expenses $= 0.40 G + 0.5250 G = 0.9250 G$

4. **Present Value of Fixed Policy Expenses**:
   - Year 1: $e_0 = 1,500\text{ BDT}$
   - Years 2–20: $e_1 (\ddot{a}_{40:\overline{20}|} - 1) = 200 \times 10.5000 = 2,100\text{ BDT}$
   - Total Fixed Expenses $= 1,500 + 2,100 = 3,600\text{ BDT}$

Equating total inflows and outflows:
$$11.5000 G = 351,750 + 0.9250 G + 3,600$$
$$11.5000 G - 0.9250 G = 351,750 + 3,600$$
$$10.5750 G = 355,350$$
$$G = \frac{355,350}{10.5750} \approx 33,602.84\text{ BDT/year}$$
The Gross Annual Premium charged to the policyholder is **$33,603\text{ BDT/year}$**.

### Solution, step 3: Expense loading analysis
$$\text{Expense Loading} = G - P = 33,602.84 - 30,434.78 = 3,168.06\text{ BDT/year}$$
As a percentage of gross premium:
$$\% \text{Loading} = \frac{3,168.06}{33,602.84} \times 100\% \approx 9.43\%$$
The expense loading comprises $9.43\%$ of each gross premium installment.

### Solution, step 4: Undiscounted expenses if policy survives to maturity
If the policyholder survives the full 20 years:
- Agent commissions:
  - Year 1: $0.40 \times 33,602.84 = 13,441.14\text{ BDT}$
  - Years 2–20 (19 years): $19 \times (0.05 \times 33,602.84) = 19 \times 1,680.14 = 31,922.66\text{ BDT}$
  - Total commissions $= 13,441.14 + 31,922.66 = 45,363.80\text{ BDT}$
- Fixed administrative fees:
  - Year 1: $1,500\text{ BDT}$
  - Years 2–20: $19 \times 200 = 3,800\text{ BDT}$
  - Total fixed fees $= 1,500 + 3,800 = 5,300\text{ BDT}$
- Maturity claim settlement fee:
  - $0.005 \times 1,000,000 = 5,000\text{ BDT}$
- **Total Lifetime Expenses Paid**:
  $$\text{Total Expenses} = 45,363.80 + 5,300.00 + 5,000.00 = 55,663.80\text{ BDT}$$
The insurer expends **$55,664\text{ BDT}$** over the 20-year policy lifecycle to service the contract.
