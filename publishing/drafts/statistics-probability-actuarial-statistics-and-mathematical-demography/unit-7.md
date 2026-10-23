# Unit 7: Benefit Reserves, Thiele's Differential Equation & Expense Loadings

## 7.1 The Operational Necessity of Policy Benefit Reserves

A fundamental structural challenge in life insurance pricing arises from the profound tension between the consumer's demand for a constant, predictable annual premium and the biological reality of human senescence.

As established in Unit 3, the human force of mortality $\mu_x$ increases exponentially after adulthood (doubling approximately every 7 to 9 years under Gompertz's law). If an insurance company charged an annual renewable term premium that matched the actual expected cost of mortality in each individual policy year:
- At age 25, the annual premium for a $\$100,000$ policy would be negligible ($\approx \$150/\text{year}$).
- By age 65, the annual premium would climb to over $\$2,000/\text{year}$.
- By age 80, the annual premium would exceed $\$10,000/\text{year}$.

Under an escalating natural premium schedule, healthy elderly policyholders voluntarily surrender or lapse their coverage because they cannot afford the exorbitant rates, while unhealthy individuals make every financial sacrifice to maintain their coverage. This dynamic produces severe **adverse selection**, triggering a death spiral that destroys the insurance risk pool.

To prevent adverse selection and satisfy consumer preferences, life insurance companies offer **Level Premium Policies**, where the annual premium $P$ remains strictly constant throughout the multi-decade life of the contract.

### The Accumulation of Policy Reserves
Under a level premium structure:
1. **Early Policy Years**: The net level annual premium $P$ substantially exceeds the instantaneous expected mortality cost ($P > b \cdot q_{x+t}$). The insurer accumulates a substantial annual operating surplus.
2. **Later Policy Years**: The instantaneous expected mortality cost substantially exceeds the level premium ($P < b \cdot q_{x+t}$). The annual premium collected is completely inadequate to pay current death claims.

The insurer must not treat the early operating surplus as distributed corporate profit! The surplus must be retained, invested at interest, and held in trust as a liability on the insurer's balance sheet. This liability is the **Benefit Reserve** (or Policy Value, denoted ${}_t V$ at policy duration $t$). The reserve bridges the gap between rising future claim costs and flat future premium inflows.

## 7.2 Prospective Benefit Reserves: ${}_t V$

At any policy duration $t \ge 0$, the **Prospective Benefit Reserve** ${}_t V$ is defined as the actuarial present value of future benefits minus the actuarial present value of future net premiums, conditional on the insured life $(x)$ being alive at duration $t$:

$${}_t V = \mathbb{E}[\text{PV of Future Benefits at duration } t \mid T_x > t] - \mathbb{E}[\text{PV of Future Net Premiums at duration } t \mid T_x > t]$$

### 1. Discrete Whole Life Insurance Reserve: ${}_t V_x$
For a unit whole life policy issued at age $x$ with net annual premium $P_x = A_x / \ddot{a}_x$:
At duration $t$, the insured is aged $x + t$.
- The APV of future death benefits is $A_{x+t}$.
- The APV of future net premiums is $P_x \cdot \ddot{a}_{x+t}$.

$${}_t V_x = A_{x+t} - P_x \cdot \ddot{a}_{x+t}$$

### Alternative Mathematical Formulations
Using the duality relation $A_{x+t} = 1 - d \ddot{a}_{x+t}$ and $P_x = 1/\ddot{a}_x - d$:
$${}_t V_x = (1 - d \ddot{a}_{x+t}) - \left( \frac{1}{\ddot{a}_x} - d \right) \ddot{a}_{x+t} = 1 - d \ddot{a}_{x+t} - \frac{\ddot{a}_{x+t}}{\ddot{a}_x} + d \ddot{a}_{x+t} = 1 - \frac{\ddot{a}_{x+t}}{\ddot{a}_x}$$

Using $\ddot{a}_y = (1 - A_y)/d$:
$${}_t V_x = 1 - \frac{(1 - A_{x+t})/d}{(1 - A_x)/d} = 1 - \frac{1 - A_{x+t}}{1 - A_x} = \frac{A_{x+t} - A_x}{1 - A_x}$$

Notice the boundary conditions:
- At policy inception ($t = 0$): ${}_0 V_x = 1 - \ddot{a}_x / \ddot{a}_x = 0$ (the initial net reserve is zero by the Equivalence Principle).
- As attained age approaches the terminal age ($x + t \to \omega$): $A_{x+t} \to 1$ and $\ddot{a}_{x+t} \to 1$, so ${}_t V_x \to 1$ (the reserve converges to the full sum insured).

### 2. $n$-Year Term Insurance Reserve: ${}_t V_{x:\overline{n}|}^1$
At duration $t < n$, remaining term coverage is $n - t$ years:

$${}_t V_{x:\overline{n}|}^1 = A_{x+t:\overline{n-t}|}^1 - P_{x:\overline{n}|}^1 \cdot \ddot{a}_{x+t:\overline{n-t}|}$$

Boundary conditions:
- At inception: ${}_0 V_{x:\overline{n}|}^1 = 0$.
- At expiration: ${}_n V_{x:\overline{n}|}^1 = 0$ (all coverage ceases with zero remaining value).

### 3. $n$-Year Endowment Insurance Reserve: ${}_t V_{x:\overline{n}|}$
$${}_t V_{x:\overline{n}|} = A_{x+t:\overline{n-t}|} - P_{x:\overline{n}|} \cdot \ddot{a}_{x+t:\overline{n-t}|} = 1 - \frac{\ddot{a}_{x+t:\overline{n-t}|}}{\ddot{a}_{x:\overline{n}|}}$$

Boundary conditions:
- At inception: ${}_0 V_{x:\overline{n}|} = 0$.
- At maturity ($t = n$): ${}_n V_{x:\overline{n}|} = 1.0$ (the reserve must equal exactly $100\%$ of the face value to pay the maturing endowment).

## 7.3 Retrospective Benefit Reserves and Equivalence Proof

While the prospective reserve looks forward into the uncertain future, the **Retrospective Benefit Reserve** looks backward into past history. It represents the accumulated value of all past net premiums collected from the cohort minus the accumulated value of all past death claims paid to deceased cohort members.

### Mathematical Formulation
Across the initial $t$ policy years, the insured was alive to pay $t$ premiums at ages $x, x + 1, \dots, x + t - 1$.
The accumulated value of past net premiums per survivor at duration $t$ is:
$$\text{Accumulated Premiums} = P \cdot \frac{N_x - N_{x+t}}{D_{x+t}}$$

The accumulated value of past death claims paid at ages $x, x + 1, \dots, x + t - 1$ per survivor at duration $t$ is:
$$\text{Accumulated Claims} = \frac{M_x - M_{x+t}}{D_{x+t}}$$

The retrospective reserve is:

$${}_t V^{\text{retro}} = P \cdot \frac{N_x - N_{x+t}}{D_{x+t}} - \frac{M_x - M_{x+t}}{D_{x+t}}$$

### Proof of Mathematical Equivalence
By the Equivalence Principle, the net annual premium satisfies $P N_x = M_x$.
Substitute $M_x = P N_x$ into the retrospective formula:
$${}_t V^{\text{retro}} = \frac{P N_x - P N_{x+t} - P N_x + M_{x+t}}{D_{x+t}} = \frac{M_{x+t} - P N_{x+t}}{D_{x+t}} = \frac{M_{x+t}}{D_{x+t}} - P \frac{N_{x+t}}{D_{x+t}}$$
Since $M_{x+t} / D_{x+t} = A_{x+t}$ and $N_{x+t} / D_{x+t} = \ddot{a}_{x+t}$:

$${}_t V^{\text{retro}} = A_{x+t} - P \ddot{a}_{x+t} = {}_t V^{\text{prospective}}$$

The prospective and retrospective benefit reserves are identical mathematical objects viewed through opposite ends of the time horizon!

## 7.4 Recursive Reserve Accumulation: Fackler's Equation and Death Strain at Risk

Consider a single policyholder alive at duration $t$ with reserve ${}_t V$. At the start of year $t + 1$, the policyholder pays the net annual premium $P$. The total fund available to the insurer at the start of the year is:

$$\text{Initial Fund} = {}_t V + P$$

Over the policy year, this fund earns interest at effective rate $i$, growing by year-end to:
$$\text{Accumulated Fund at Year-End} = ({}_t V + P)(1 + i)$$

During policy year $t + 1$, the life $(x + t)$ faces probability of death $q_{x+t}$ and probability of survival $p_{x+t} = 1 - q_{x+t}$:
- If the life dies (probability $q_{x+t}$), the insurer pays the death benefit $b$.
- If the life survives (probability $p_{x+t}$), the insurer must establish the next year-end reserve ${}_{t+1} V$.

By the law of total expectation across the cohort, the accumulated fund must exactly balance the expected year-end obligations:

$$({}_t V + P)(1 + i) = q_{x+t} \cdot b + p_{x+t} \cdot {}_{t+1} V$$

This is **Fackler's Recursive Reserve Equation** (formulated by David Parks Fackler in 1868).

### Net Amount at Risk (Death Strain at Risk)
Substitute $p_{x+t} = 1 - q_{x+t}$ into Fackler's equation:
$$({}_t V + P)(1 + i) = q_{x+t} b + (1 - q_{x+t}) {}_{t+1} V = {}_{t+1} V + q_{x+t} (b - {}_{t+1} V)$$

The term $(b - {}_{t+1} V)$ is the **Net Amount at Risk (Death Strain at Risk, $DSAR$)**:
$$DSAR_{t+1} = b - {}_{t+1} V$$

The financial significance is profound:
- When a policyholder dies, the insurer does not suffer a cash loss of the entire face value $b$.
- The insurer already possesses the policyholder’s accumulated reserve ${}_{t+1} V$!
- The insurer’s net out-of-pocket loss is only the difference $b - {}_{t+1} V$.

Dividing by $(1 + i)$:

$${}_t V + P = v \cdot {}_{t+1} V + v \cdot q_{x+t} (b - {}_{t+1} V)$$

Each annual premium $P$ contributes to two distinct financial accounts:
1. An **investment savings deposit** ($v \cdot {}_{t+1} V - {}_t V$), which builds the policyholder's cash value.
2. A **pure term insurance premium** ($v \cdot q_{x+t} DSAR_{t+1}$), which purchases 1-year term coverage for the net amount at risk!

## 7.5 Continuous Reserves and Thiele's Differential Equation

Thorvald N. Thiele (1875) formulated the continuous-time ordinary differential equation governing benefit reserve accumulation.

Consider a continuous policy paying sum insured $b$ at the moment of death, with continuous premium collection rate $\bar{P}$ and continuous reserves ${}_t \bar{V}$.

Consider the infinitesimal interval $[t, t + \Delta t]$. Applying Fackler's logic over $dt$:
The fund at time $t$ is ${}_t \bar{V}$. During $\Delta t$:
- Premiums collected: $\bar{P} \Delta t$.
- Interest earned: $\delta \cdot {}_t \bar{V} \Delta t$.
- Probability of death: $\mu_{x+t} \Delta t$.
- Net payment upon death: $(b - {}_t \bar{V})$.

The change in reserve $\Delta {}_t \bar{V}$ is:

$$\Delta {}_t \bar{V} = \delta {}_t \bar{V} \Delta t + \bar{P} \Delta t - \mu_{x+t} (b - {}_t \bar{V}) \Delta t + o(\Delta t)$$

Dividing by $\Delta t$ and taking the limit as $\Delta t \to 0$ yields **Thiele's Differential Equation**:

$$\frac{d}{dt} {}_t \bar{V} = \delta \cdot {}_t \bar{V} + \bar{P} - \mu_{x+t} (b - {}_t \bar{V})$$

### Economic Interpretation of Thiele's Equation
The instantaneous rate of reserve growth $\frac{d}{dt} {}_t \bar{V}$ is driven by three physical forces:
1. $+\delta {}_t \bar{V}$: Compound interest accumulation on the existing asset reserve.
2. $+\bar{P}$: Premium revenue inflow from the living policyholder.
3. $-\mu_{x+t}(b - {}_t \bar{V})$: Expected mortality claim outflow for the net amount at risk.

Thiele's differential equation represents the actuarial counterpart to the Black-Scholes partial differential equation in financial engineering. It forms the foundational numerical engine used in modern actuarial modeling software to value multi-state pension and disability contracts via Runge-Kutta integration.

## 7.6 Expense Reserves, Full Preliminary Term (FPT) and Surrender Values

### The Initial New Business Strain
Under classical **Net Level Premium (NLP)** reserve valuation, statutory accounting rules require the insurer to establish the full theoretical net reserve ${}_1 V$ at the end of Year 1. However, as derived in Unit 6, an insurer expends $40\%$ to $60\%$ of the first-year gross premium on sales commissions and medical underwriting ($c_0$). 

Because expenses are heavily front-loaded while gross premiums are collected in flat level increments, an insurer writing high volumes of new life insurance policies suffers severe statutory accounting losses in Year 1—a phenomenon termed **New Business Strain**. If uncorrected, rapid commercial growth will drive a solvent insurance company into technical bankruptcy!

### The Full Preliminary Term (FPT) Valuation System
To relieve new business strain without compromising solvency, actuarial standards developed **Modified Reserve Systems**, the most prominent of which is the **Full Preliminary Term (FPT)** method.

Under FPT:
- **Year 1**: The policy is treated mathematically as a 1-year pure term insurance. The first-year net premium is set to the 1-year term cost:
  $$P_1^{\text{FPT}} = c_{x} = b \cdot v q_x$$
  Because all remaining first-year premium revenue is freed to absorb initial sales commissions and underwriting costs, the reserve at the end of Year 1 is set to zero:
  $${}_1 V^{\text{FPT}} = 0$$
- **Years $2$ to $n$**: The policy is treated as if it were originally issued at age $x + 1$ with $(n - 1)$ premium payments. The renewal net premium $P_{\text{renewal}}^{\text{FPT}}$ is:
  $$P_{\text{renewal}}^{\text{FPT}} = \frac{A_{x+1}}{\ddot{a}_{x+1:\overline{n-1}|}} > P_x$$
- **Terminal Convergence**: As duration $t$ approaches maturity, the FPT reserve catches up with the Net Level Premium reserve, converging to exact equality at policy termination:
  $${}_n V^{\text{FPT}} = {}_n V^{\text{NLP}} = b$$

### Surrender Values and Non-Forfeiture Options
If a policyholder cancels (surrenders) their policy prior to maturity, they are contractually entitled to a **Cash Surrender Value ($CSV$)**. 
The surrender value is derived from the asset reserve, minus a **surrender charge** in early years to recoup unamortized acquisition expenses:
$$CSV_t = {}_t V - SC_t$$
Alternatively, the policyholder may convert their cash value into non-forfeiture options:
1. **Reduced Paid-Up Insurance**: Using $CSV_t$ as a net single premium to purchase a reduced whole life policy ($b_{\text{paid-up}} = CSV_t / A_{x+t}$) with zero future premium obligations.
2. **Extended Term Insurance**: Using $CSV_t$ to purchase term insurance for the full original sum insured $b$ for as many years and days as the cash value can fund.

## 7.8 Hattendorff's Theorem on the Variance of Benefit Reserves

In life insurance mathematics, the prospective net loss random variable at time $t$ for a policy issued at $t = 0$ is defined as:
$${}_t L = v^{T_{x+t}} - P \cdot \ddot{a}_{\overline{K_{x+t} + 1}|}$$
The benefit reserve at duration $t$ is the mathematical expectation of this loss:
$${}_t V = \mathbb{E}[{}_t L]$$

A central theoretical problem formulated in the nineteenth century was computing the variance of ${}_0 L$, the net loss at policy issue. In 1868, the German actuary Karl Hattendorff proved a landmark theorem that revolutionized actuarial risk theory: **the annual losses in successive policy years are mutually uncorrelated random variables**.

### Statement and Proof of Hattendorff's Theorem
Let the total policy lifetime be discretized into yearly intervals $[k, k+1)$ for $k = 0, 1, 2, \dots$.
Define the **one-year net loss random variable** $J_k$ allocated to policy year $k+1$, evaluated at duration $k+1$:

$$J_k = \begin{cases}
1 - {}_{k+1} V & \text{if $(x)$ dies during year } k+1 \text{ (probability } q_{x+k}) \\
{}_k V (1 + i) - P(1 + i) - {}_{k+1} V = 0 & \text{if $(x)$ survives to year } k+1 \text{ (probability } p_{x+k})
\end{cases}$$
under the recursive reserve relation ${}_k V + P = v q_{x+k} + v p_{x+k} {}_{k+1} V$.

The actual mortality loss random variable in year $k+1$, discounted to duration $k$, has conditional expectation:
$$\mathbb{E}[J_k \mid K_x \ge k] = (1 - {}_{k+1} V) q_{x+k} + (-{}_{k+1} V) p_{x+k} + ({}_k V + P)(1 + i) = 0$$
The conditional expected loss in every individual policy year is identically zero!

The conditional variance of the one-year loss is:
$$\mathrm{Var}(J_k \mid K_x \ge k) = (1 - {}_{k+1} V)^2 q_{x+k} p_{x+k}$$
The quantity $1 - {}_{k+1} V$ is the **Net Amount at Risk (NAR)** in policy year $k+1$.

Hattendorff demonstrated that the aggregate prospective loss at issue ${}_0 L$ can be expressed as a linear combination of these single-year loss variables:
$${}_0 L = \sum_{k=0}^\infty v^{k+1} I(K_x \ge k) J_k$$
where $I(K_x \ge k)$ is the indicator that the policyholder is alive at the beginning of year $k+1$.

Because the conditional expectation of $J_k$ given past history is zero, the sequence of discounted losses forms a **martingale difference sequence**. Therefore:
$$\mathrm{Cov}(J_k, J_m) = 0 \quad \text{for all } k \ne m$$

Taking the variance of the sum:

$$\mathrm{Var}({}_0 L) = \sum_{k=0}^\infty v^{2(k+1)} {}_k p_x \cdot q_{x+k} \cdot p_{x+k} \cdot (1 - {}_{k+1} V)^2$$

### Profound Practical Implications of Hattendorff's Theorem
1. **Total Reserve Risk Decomposition**: The variance of the insurer's lifetime financial loss on a policy equals the sum of the discounted annual variances of the mortality risk, weighted by the survival probability ${}_k p_x$.
2. **Role of the Net Amount at Risk**: The variance in year $k+1$ is directly proportional to the square of the Net Amount at Risk $(1 - {}_{k+1} V)^2$. As the policy matures and the reserve ${}_{k+1} V$ accumulates toward the face amount of $1.0$, the net amount at risk contracts toward zero, drastically dampening the insurer's annual underwriting volatility in later policy years.
3. **Reinsurance Optimization**: Insurers structure excess-of-loss and quota-share reinsurance treaties specifically to cap the Net Amount at Risk $(1 - {}_{k+1} V)$, systematically suppressing portfolio variance.

## 7.9 Modified Reserve Systems: Full Preliminary Term and Zillmerisation

Under net level premium reserving, the net premium $P_x$ is assumed constant across all policy durations $t = 1, 2, \dots, n$. However, as established in Section 6.8, an insurance company incurs massive acquisition expenses in year 1 ($e_1$ and $c_1$) to underwrite, issue, and distribute the policy.

If the insurer is legally mandated to post a full net level reserve ${}_1 V$ at the end of Year 1, it must finance both the acquisition expenses and the reserve out of surplus capital, creating severe **surrender drain** and **new business strain** that can threaten the solvency of rapidly growing insurance companies.

To eliminate new business strain while preserving long-term solvency, statutory insurance regulators authorize **Modified Reserve Systems**.

### 1. The Full Preliminary Term (FPT) Method
The Full Preliminary Term method treats the first policy year as pure one-year term insurance, deferring the accumulation of savings reserves until Year 2.

Under FPT:
- **Year 1 Net Premium ($\beta_1^{\text{FPT}}$)**: Exactly covers one-year mortality risk:
  $$\beta_1^{\text{FPT}} = c_{x} = v q_x$$
- **Renewal Net Premium ($\beta^{\text{FPT}}$)**: Amortizes the policy benefit over the remaining $n - 1$ years for an individual aged $x + 1$:
  $$\beta^{\text{FPT}} = P_{x+1:\overline{n-1}|} = \frac{A_{x+1:\overline{n-1}|}}{\ddot{a}_{x+1:\overline{n-1}|}}$$
Since $\beta_1^{\text{FPT}} \ll P$ and $\beta^{\text{FPT}} > P$, the company frees up the entire difference $P - \beta_1^{\text{FPT}}$ in the first year to fund acquisition expenses!

The FPT benefit reserves satisfy:
- At $t = 1$: ${}_1 V^{\text{FPT}} = 0$. (No reserve is held at the end of the first year).
- At duration $t \ge 2$:
  $${}_t V^{\text{FPT}} = {}_{t-1} V_{x+1:\overline{n-1}|}$$
The reserve held at duration $t$ equals the standard net level reserve for a policy issued at age $x+1$ at duration $t-1$.

### 2. Zillmer's Reserving Method
In continental Europe and the United Kingdom, August Zillmer generalized modified reserving by explicitly incorporating an acquisition expense amortization factor $\alpha_{\text{zillmer}}$ (commonly $3.5\%$ of sum assured) into the prospective reserve:

$${}_t V^{\text{Zillmer}} = A_{x+t} - P_x^{\text{Zillmer}} \ddot{a}_{x+t}$$
where the Zillmerized premium is:
$$P_x^{\text{Zillmer}} = P_x + \frac{\alpha_{\text{zillmer}}}{\ddot{a}_x}$$

At policy inception ($t = 0$):
$${}_0 V^{\text{Zillmer}} = A_x - \left( P_x + \frac{\alpha_{\text{zillmer}}}{\ddot{a}_x} \right) \ddot{a}_x = (A_x - P_x \ddot{a}_x) - \alpha_{\text{zillmer}} = -\alpha_{\text{zillmer}}$$
The negative initial reserve reflects the unamortized acquisition debt. Over the policy tenure, ${}_t V^{\text{Zillmer}}$ rises steadily and converges identically to the full contractual benefit at maturity.

## 7.10 Asset Shares and Surrender Value Equity

While statutory benefit reserves ${}_t V$ represent theoretical liability allocations mandated by insurance regulators, the actual capital accumulated by a cohort of identical policies is governed by the **Asset Share** $AS_t$.

The asset share tracks the real-world retrospective accumulation of all cash inflows and outflows per surviving policyholder, incorporating actual investment earnings, real operating expenses, policy lapses, and surrender penalties.

### 1. The Recursive Asset Share Formula
Let $N_t$ be the number of policies in force at duration $t$. Over policy year $t+1$:
- The insurer collects gross premium $G$ from each surviving policyholder at time $t$.
- The insurer incurs per-policy expenses $e_{t+1}$ and percentage expenses $c_{t+1} G$.
- The net investable funds earn actual earned investment yield rate $i'$.
- At the end of year $t+1$, mortality claims of amount $S$ are paid to deceased policyholders ($q_{x+t}'$).
- Surrendering policyholders exit the pool, receiving cash surrender value $CV_{t+1}$ ($w_{t+1}'$).
- The remaining asset pool is divided equally among the $p_{x+t}' (1 - w_{t+1}')$ surviving, persistent policyholders.

The recursive equation for the asset share per surviving policy at duration $t+1$ is:

$$AS_{t+1} = \frac{[AS_t + G(1 - c_{t+1}) - e_{t+1}](1 + i') - S \cdot q_{x+t}' - CV_{t+1} \cdot w_{t+1}'}{1 - q_{x+t}' - w_{t+1}'}$$

where $q_{x+t}'$ is the actual experienced mortality rate and $w_{t+1}'$ is the actual experienced voluntary lapse/surrender rate.

### 2. Determination of Cash Surrender Values
When a policyholder terminates an insurance contract prior to maturity, the insurer pays a **Cash Surrender Value (CSV)**.

Actuaries design surrender value schedules to satisfy three fundamental equitable principles:
1. **Solvency Protection**: The cash surrender value must never exceed the available asset share:
   $$CV_t \le AS_t$$
   If $CV_t > AS_t$, departing policyholders extract more capital than they contributed, inflicting financial injury on remaining persistent policyholders.
2. **Surrender Charges**: In early policy years ($t \le 5$), heavy initial acquisition expenses cause the asset share to be negative ($AS_t < 0$) or significantly below the statutory reserve (${}_t V$). Insurers apply a **Surrender Charge** $SC_t$:
   $$CV_t = \max\left( 0, \; {}_t V - SC_t \right)$$
   Surrender charges amortize unrecovered acquisition debt and vanish by year 10.
3. **Non-Forfeiture Options**: Instead of taking cash, the surrendering policyholder may elect:
   - **Reduced Paid-Up Insurance (RPU)**: Using $CV_t$ as a single premium to purchase a reduced face amount $S' < S$ of fully paid whole life insurance without future premiums.
   - **Extended Term Insurance (ETI)**: Using $CV_t$ to purchase term insurance with the original face amount $S$ for a temporary term of $m$ years.

## 7.12 Continuous Multi-State Reserving: The General Thiele Differential System

In modern actuarial software, life and health reserves are computed using continuous differential equations rather than discrete recursive tables. In Section 7.5, we introduced Thiele's differential equation for a standard whole life policy. We now generalize Thiele's equation to an arbitrary finite-state Markov model with $J + 1$ states $\{0, 1, \dots, J\}$.

### 1. General Continuous Cash Flow Specifications
For an individual in state $i \in \{0, 1, \dots, J\}$ at duration $t$:
- $P_i(t)$: Continuous gross premium inflow rate received while in state $i$.
- $b_i(t)$: Continuous annuity benefit payout rate paid while in state $i$.
- $e_i(t)$: Continuous administrative expense rate incurred while in state $i$.
- $S_{ij}(t)$: Lump sum benefit paid immediately upon transition from state $i$ to state $j$ ($i \ne j$).
- $\mu_{x+t}^{ij}$: Instantaneous transition intensity from state $i$ to state $j$.
- $\delta(t)$: Instantaneous force of interest.

Let $V_i(t)$ denote the prospective policy reserve at time $t$, conditional on the insured occupying state $i$ at duration $t$.

### 2. Derivation of the General Thiele Differential Equation
Consider an infinitesimal time step $dt$. During the interval $[t, t + dt]$:
- Net cash inflow earned while in state $i$: $[P_i(t) - b_i(t) - e_i(t)] dt$.
- Interest earned on current reserve: $\delta(t) V_i(t) dt$.
- Probability of transitioning to state $j \ne i$: $\mu_{x+t}^{ij} dt$.
  Upon transition to state $j$, the insurer pays the lump sum benefit $S_{ij}(t)$ and must hold the new state reserve $V_j(t + dt)$. Thus, the expected payout and liability change on transition is:
  $$\sum_{j \ne i} \mu_{x+t}^{ij} [S_{ij}(t) + V_j(t)] dt$$
- Probability of remaining in state $i$: $1 - \sum_{j \ne i} \mu_{x+t}^{ij} dt$.

The equation of equilibrium equates the present reserve to discounted future liabilities:
$$V_i(t) = [P_i(t) - b_i(t) - e_i(t)] dt + e^{-\delta(t) dt} \left[ \left(1 - \sum_{j \ne i} \mu_{x+t}^{ij} dt \right) V_i(t + dt) + \sum_{j \ne i} \mu_{x+t}^{ij} [S_{ij}(t) + V_j(t)] dt \right]$$

Approximating $e^{-\delta(t) dt} \approx 1 - \delta(t) dt$, expanding $V_i(t + dt) = V_i(t) + \frac{d}{dt} V_i(t) dt$, collecting terms of order $dt$, and dividing by $dt$ produces the **General Thiele System of Differential Equations**:

$$\frac{d}{dt} V_i(t) = \delta(t) V_i(t) - [P_i(t) - b_i(t) - e_i(t)] - \sum_{j \ne i} \mu_{x+t}^{ij} \left[ S_{ij}(t) + V_j(t) - V_i(t) \right]$$

### 3. Economic Interpretation of the Equation
Every term in Thiele's equation has a transparent financial meaning:
1. $\delta(t) V_i(t)$: The continuous investment yield earned on the existing reserve.
2. $-[P_i(t) - b_i(t) - e_i(t)]$: The net operating cash outflow rate.
3. $-\sum_{j \ne i} \mu_{x+t}^{ij} [S_{ij}(t) + V_j(t) - V_i(t)]$: The expected mortality or morbidity strain.
   The quantity $R_{ij}(t) = S_{ij}(t) + V_j(t) - V_i(t)$ represents the **Net Sum at Risk for Transition $i \to j$**: the total capital drain experienced by the insurer if the policyholder jumps from state $i$ to state $j$.

The Thiele system is solved backwards in time starting from the boundary conditions at policy expiration $t = n$:
$$V_i(n) = \text{Contractual Maturity Endowment in State } i$$
Using fourth-order Runge-Kutta numerical integration, this single system computes exact technical provisions for life insurance, critical illness, disability, and long-term care contracts.

## 7.13 Reserving for Equity-Indexed and Variable Annuity Guarantees (GMxB)

Modern variable annuities provide policyholders with investment exposure to equity mutual funds while incorporating embedded actuarial downside guarantees, known collectively as **GMxB Guarantees**:
1. **Guaranteed Minimum Death Benefit (GMDB)**: Guarantees that upon death, the beneficiary receives at least the original premium deposit, regardless of stock market declines:
   $$\text{Benefit} = \max(W_t, G_0)$$
   where $W_t$ is the separate account fund value and $G_0$ is the guaranteed minimum base.
2. **Guaranteed Minimum Accumulation Benefit (GMAB)**: Guarantees that at policy maturity $T$, the account value will not be less than the guaranteed base:
   $$\text{Payoff} = \max(0, G_0 - W_T)$$
   This payoff is mathematically identical to an embedded **European Put Option** on the separate account fund with strike price $G_0$.
3. **Guaranteed Minimum Withdrawal Benefit (GMWB)**: Allows the policyholder to withdraw a fixed percentage (e.g., $5\%$) of the guaranteed benefit base annually for life, even if the actual account balance drops to zero.

### Stochastic Reserving Under VM-21 and Principle-Based Reserving (PBR)
Because GMxB guarantees involve financial market risk intertwined with policyholder behavior (lapses, dynamic surrenders, and elective utilization), deterministic life tables are completely incapable of measuring liability risk.

Under United States Principle-Based Reserving (Valuation Manual VM-21), insurers must compute technical reserves stochastically:
1. **Stochastic Scenario Generation**: The insurer simulates $M = 10,000$ correlated economic paths of interest rates, equity returns, and inflation over a 30-year horizon.
2. **Dynamic Policyholder Behavior**: On each path $k$, policyholder lapse rates $\lambda_t^{(k)}$ adjust dynamically: when equity markets crash and the embedded put guarantee is deep in-the-money, policyholder surrender rates plummet to near zero (the "sticky money" phenomenon).
3. **Greatest Present Value of Accumulated Deficiency (GPVAD)**: On each path $k$, the actuary calculates the maximum capital deficiency:
   $$\text{GPVAD}_k = \max_{1 \le t \le T} \left[ -\sum_{s=1}^t \frac{\text{Net Cash Flow}_s^{(k)}}{(1 + r_s^{(k)})^s} \right]$$
4. **Conditional Tail Expectation (CTE 70)**: The statutory reserve is set equal to the average of the worst $30\%$ of simulated deficiencies:
   $$\text{Reserve} = \text{CTE}_{70} = \mathbb{E}\left[ \text{GPVAD} \mid \text{GPVAD} \ge \text{Quantile}_{0.70}(\text{GPVAD}) \right]$$
Stochastic PBR ensures that insurers hold sufficient reserves to survive extreme market contractions combined with severe longevity extensions.

## Fully worked question 1: Prospective and Retrospective Reserve Reconciliation

### Question
An extract from an actuarial valuation table compiled at an effective annual interest rate of $i = 5.00\%$ ($i = 0.05$, $d = 0.05/1.05 \approx 0.047619$) provides the following commutation values:
- $D_{30} = 25,000$
- $D_{40} = 15,000$
- $D_{50} = 8,800$
- $M_{30} = 6,250$
- $M_{40} = 4,200$
- $M_{50} = 3,300$
- $N_{30} = 400,000$
- $N_{40} = 200,000$
- $N_{50} = 88,000$

A life aged $30$ purchases a 20-Year Endowment Insurance policy with sum insured $b = 100,000\text{ BDT}$. Net annual premiums $P = 100,000 P_{30:\overline{20}|}$ are payable at the start of each year for 20 years.

Perform the following calculations:
1. Compute the net level annual premium $P$.
2. Compute the benefit reserve at duration $t = 10$ (attained age $40$) using the **Prospective Method** (${}_{10} V$).
3. Compute the benefit reserve at duration $t = 10$ using the **Retrospective Method** (${}_{10} V^{\text{retro}}$), demonstrating exact mathematical equality.
4. Compute the reserve at policy inception (${}_0 V$) and at maturity (${}_{20} V$).

### Solution, step 1: Net level annual premium $P$
For a 20-year endowment issued at age 30, maturity is at age $30 + 20 = 50$:
$$P_{30:\overline{20}|} = \frac{M_{30} - M_{50} + D_{50}}{N_{30} - N_{50}} = \frac{6,250 - 3,300 + 8,800}{400,000 - 88,000} = \frac{2,950 + 8,800}{312,000} = \frac{11,750}{312,000} \approx 0.03766026$$
For a sum insured of $100,000\text{ BDT}$:
$$P = 100,000 \times 0.03766026 = 3,766.03\text{ BDT/year}$$

### Solution, step 2: Prospective reserve at $t = 10$ (${}_{10} V$)
At $t = 10$, the insured is aged $40$, with $20 - 10 = 10$ years remaining to maturity (age 50):
1. **APV of Remaining Benefits**:
   $$A_{40:\overline{10}|} = \frac{M_{40} - M_{50} + D_{50}}{D_{40}} = \frac{4,200 - 3,300 + 8,800}{15,000} = \frac{900 + 8,800}{15,000} = \frac{9,700}{15,000} \approx 0.646667$$
   For $100,000\text{ BDT}$ face value:
   $$\text{APV}_{\text{benefits}} = 100,000 \times 0.646667 = 64,666.67\text{ BDT}$$

2. **APV of Remaining Net Premiums**:
   $$\ddot{a}_{40:\overline{10}|} = \frac{N_{40} - N_{50}}{D_{40}} = \frac{200,000 - 88,000}{15,000} = \frac{112,000}{15,000} \approx 7.466667$$
   $$\text{APV}_{\text{premiums}} = P \cdot \ddot{a}_{40:\overline{10}|} = 3,766.03 \times 7.466667 \approx 28,119.67\text{ BDT}$$

3. **Prospective Reserve**:
   $${}_{10} V = \text{APV}_{\text{benefits}} - \text{APV}_{\text{premiums}} = 64,666.67 - 28,119.67 = 36,547.00\text{ BDT}$$

### Solution, step 3: Retrospective reserve at $t = 10$ (${}_{10} V^{\text{retro}}$)
Under the retrospective method:
$${}_{10} V^{\text{retro}} = 100,000 \left[ P_{30:\overline{20}|} \frac{N_{30} - N_{40}}{D_{40}} - \frac{M_{30} - M_{40}}{D_{40}} \right]$$
Calculate components:
- Accumulated past premiums:
  $$\frac{N_{30} - N_{40}}{D_{40}} = \frac{400,000 - 200,000}{15,000} = \frac{200,000}{15,000} \approx 13.333333$$
  $$P \times 13.333333 = 3,766.03 \times 13.333333 \approx 50,213.73\text{ BDT}$$
- Accumulated past claims:
  $$\frac{M_{30} - M_{40}}{D_{40}} = \frac{6,250 - 4,200}{15,000} = \frac{2,050}{15,000} \approx 0.136667$$
  $$100,000 \times 0.136667 = 13,666.67\text{ BDT}$$
- Net Retrospective Reserve:
  $${}_{10} V^{\text{retro}} = 50,213.73 - 13,666.67 = 36,547.06\text{ BDT}$$
Within $0.06\text{ BDT}$ rounding tolerance, prospective and retrospective reserves are identical!

### Solution, step 4: Boundary reserve values
- At $t = 0$: ${}_0 V = 0\text{ BDT}$ (by Equivalence Principle).
- At $t = 20$: ${}_{20} V = 100,000\text{ BDT}$ (exact maturity endowment obligation).

## Fully worked question 2: Fackler's Recursive Accumulation and Death Strain Accounting

### Question
An insurance company tracks an individual whole life insurance policy with sum insured $b = 200,000\text{ BDT}$ issued to $(x)$. The net annual premium is $P = 4,200\text{ BDT}$. The effective interest rate is $i = 6.00\%$ ($i = 0.06$).

At policy duration $t = 15$, the terminal reserve is ${}_{15} V = 48,000\text{ BDT}$.
The mortality rate at attained age $x + 15$ is $q_{x+15} = 0.01500$ (survival rate $p_{x+15} = 0.98500$).

Perform the following calculations:
1. Compute the fund available at the beginning of policy year 16 after collecting premium $P$.
2. Compute the fund accumulated with interest at the end of policy year 16.
3. Using Fackler's recursive equation, compute the terminal reserve at the end of year 16 (${}_{16} V$).
4. Compute the Net Amount at Risk (Death Strain at Risk, $DSAR$) during year 16.
5. In a cohort of $1,000$ identical policyholders alive at duration 15:
   - Compute the expected death claim payouts.
   - If exactly $18$ policyholders die during year 16 (compared to expected deaths of $15$), compute the **Mortality Loss (Strain Loss)** incurred by the company.

### Solution, step 1: Initial fund at beginning of year 16
$$\text{Fund}_{\text{start}} = {}_{15} V + P = 48,000 + 4,200 = 52,200\text{ BDT}$$

### Solution, step 2: Accumulated fund at end of year 16
$$\text{Fund}_{\text{end}} = 52,200 \times (1 + i) = 52,200 \times 1.06 = 55,332\text{ BDT}$$

### Solution, step 3: Fackler's recursive reserve ${}_{16} V$
Fackler's equation states:
$$({}_{15} V + P)(1 + i) = q_{x+15} \cdot b + p_{x+15} \cdot {}_{16} V$$
Substitute known values:
$$55,332 = (0.01500 \times 200,000) + 0.98500 \cdot {}_{16} V$$
$$55,332 = 3,000 + 0.98500 \cdot {}_{16} V$$
$$0.98500 \cdot {}_{16} V = 55,332 - 3,000 = 52,332$$
$${}_{16} V = \frac{52,332}{0.98500} \approx 53,128.93\text{ BDT}$$
The reserve at the end of year 16 is **$53,129\text{ BDT}$**.

### Solution, step 4: Net Amount at Risk ($DSAR$)
$$DSAR_{16} = b - {}_{16} V = 200,000 - 53,128.93 = 146,871.07\text{ BDT}$$
The insurer’s net exposure upon death is approximately $146,871\text{ BDT}$, not the full $200,000\text{ BDT}$.

### Solution, step 5: Cohort mortality strain accounting
For $1,000$ policyholders alive at duration 15:
- Expected deaths: $\mathbb{E}[\text{Deaths}] = 1,000 \times q_{x+15} = 1,000 \times 0.01500 = 15\text{ deaths}$.
- Expected claim disbursements: $15 \times 200,000 = 3,000,000\text{ BDT}$.
- Expected death strain:
  $$\text{Expected Strain} = 15 \times DSAR_{16} = 15 \times 146,871.07 = 2,203,066.05\text{ BDT}$$
- Actual deaths: $18\text{ deaths}$ ($3$ excess deaths).
- Actual death strain:
  $$\text{Actual Strain} = 18 \times DSAR_{16} = 18 \times 146,871.07 = 2,643,679.26\text{ BDT}$$
- **Mortality Loss (Strain Loss)**:
  $$\text{Mortality Loss} = \text{Actual Strain} - \text{Expected Strain} = (18 - 15) \times DSAR_{16} = 3 \times 146,871.07 = 440,613.21\text{ BDT}$$
The insurer suffers an underwriting mortality loss of **$440,613\text{ BDT}$** due to the 3 excess deaths.

## Fully worked question 3: Thiele's Differential Equation and Numerical Reserve Trajectory

### Question
A continuous whole life insurance policy pays a death benefit of $b = 100,000\text{ BDT}$ at the moment of death of a life aged $x = 50$. Continuous net level premiums are collected at rate $\bar{P} = 1,800\text{ BDT/year}$. 

The financial force of interest is constant at $\delta = 0.0400$.
The force of mortality follows Gompertz's law:
$$\mu_{50+t} = 0.0008 \times (1.08)^{50+t}$$

Perform the following calculations:
1. Write down the explicit form of Thiele’s Differential Equation for the reserve trajectory ${}_t \bar{V}$.
2. At duration $t = 10$ (attained age 60), the accumulated reserve is ${}_{10} \bar{V} = 18,500\text{ BDT}$. Compute the exact value of $\mu_{60}$ and the net amount at risk ($b - {}_{10} \bar{V}$).
3. Compute the instantaneous derivative $\frac{d}{dt} {}_t \bar{V}$ at $t = 10$.
4. Using Euler’s forward numerical integration method with step size $\Delta t = 0.5\text{ years}$, approximate the reserve at duration $t = 10.5$ (${}_{10.5} \bar{V}$).

### Solution, step 1: Formulate Thiele's Differential Equation
Thiele's ODE states:
$$\frac{d}{dt} {}_t \bar{V} = \delta \cdot {}_t \bar{V} + \bar{P} - \mu_{50+t} (b - {}_t \bar{V})$$
Substitute $b = 100,000$, $\bar{P} = 1,800$, $\delta = 0.04$:
$$\frac{d}{dt} {}_t \bar{V} = 0.04 \cdot {}_t \bar{V} + 1,800 - \mu_{50+t} (100,000 - {}_t \bar{V})$$

### Solution, step 2: Evaluate parameters at duration $t = 10$ (Age 60)
At $t = 10$, attained age is $50 + 10 = 60$:
$$\mu_{60} = 0.0008 \times (1.08)^{60}$$
Calculate $(1.08)^{60}$:
$$(1.08)^{60} = \exp(60 \times \ln 1.08) = \exp(60 \times 0.076961) = \exp(4.61766) \approx 101.257$$
$$\mu_{60} = 0.0008 \times 101.257 \approx 0.081006$$
The hazard rate at age 60 is $8.1006\%$ per year.

The Net Amount at Risk at $t = 10$ is:
$$b - {}_{10} \bar{V} = 100,000 - 18,500 = 81,500\text{ BDT}$$

### Solution, step 3: Compute instantaneous derivative at $t = 10$
Substitute values into Thiele's equation:
1. Interest earned on reserve:
   $$\delta \cdot {}_{10} \bar{V} = 0.04 \times 18,500 = +740.00\text{ BDT/year}$$
2. Premium inflow:
   $$\bar{P} = +1,800.00\text{ BDT/year}$$
3. Expected claim outflow on net risk:
   $$\mu_{60} (b - {}_{10} \bar{V}) = 0.081006 \times 81,500 \approx 6,601.99\text{ BDT/year}$$

Summing terms:
$$\frac{d}{dt} {}_{10} \bar{V} = 740.00 + 1,800.00 - 6,601.99 = 2,540.00 - 6,601.99 = -4,061.99\text{ BDT/year}$$

**Critical Finding**:
The derivative is **negative** ($\frac{d}{dt} {}_t \bar{V} < 0$)!
At age 60, mortality costs ($6,602\text{ BDT/year}$) have overtaken combined premium inflow and interest earnings ($2,540\text{ BDT/year}$). The policy reserve has passed its peak and is now actively unwinding to fund escalating claims, exactly as actuarial theory dictates!

### Solution, step 4: Euler numerical integration for ${}_{10.5} \bar{V}$
Using Euler's step formula with $\Delta t = 0.5\text{ years}$:
$${}_{10.5} \bar{V} \approx {}_{10} \bar{V} + \Delta t \left( \frac{d}{dt} {}_{10} \bar{V} \right)$$
$${}_{10.5} \bar{V} \approx 18,500 + 0.5 \times (-4,061.99) = 18,500 - 2,031.00 = 16,469.00\text{ BDT}$$
The estimated reserve at duration $10.5$ is **$16,469\text{ BDT}$**.
