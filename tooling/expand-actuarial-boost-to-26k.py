#!/usr/bin/env python3
"""
Booster script for Actuarial Statistics and Mathematical Demography
to bring the book draft over 26,000 substantive prose words across all 8 units.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"

# --- UNIT 1 BOOSTER ---
u1_path = DRAFT_DIR / "unit-1.md"
u1_text = u1_path.read_text(encoding="utf-8")
u1_add = r"""
## 1.14 Absolute Cash Flow Dedication vs Duration Immunization

When managing institutional balance sheets, actuaries protect multi-billion dollar liability commitments against financial market volatility using two competing asset-liability management paradigms: **Absolute Cash Flow Dedication (Cash Flow Matching)** and **Duration Immunization**.

### 1. Mathematical Formulation of Cash Flow Dedication
Absolute cash flow dedication completely eliminates interest rate and term structure risk by selecting a portfolio of default-free bonds whose contractual coupon and principal cash inflows match the liability cash outflows in both timing and amount.

Let an insurer face known liability cash outflows $L_t$ at calendar periods $t \in \{1, 2, \dots, T\}$. Let $J$ distinct default-free bonds be available in capital markets, where bond $j \in \{1, \dots, J\}$ has market price $P_j$ per unit face amount and produces cash inflow $C_{j, t}$ at period $t$.

Let $x_j \ge 0$ denote the face amount of bond $j$ purchased by the insurer. The dedication problem is formulated as a linear programming optimization:

$$\min_{x_1, \dots, x_J} \sum_{j=1}^J P_j x_j$$
subject to the exact solvency matching constraints:
$$\sum_{j=1}^J C_{j, t} x_j \ge L_t \quad \text{for each } t = 1, 2, \dots, T$$
$$x_j \ge 0 \quad \text{for all } j = 1, \dots, J$$

If reinvestment of excess cash is permitted at a conservative short-term reinvestment rate $r_{\text{safe}}$, let $R_t$ denote cash carried forward from period $t-1$ to period $t$:
$$\sum_{j=1}^J C_{j, t} x_j + R_{t-1} (1 + r_{\text{safe}}) - R_t = L_t$$
where $R_0 = 0$ and $R_t \ge 0$ for all $t$.

### 2. Dedication versus Duration Immunization: Comparative Trade-Offs
While dedication guarantees complete immunity against arbitrary yield curve twists, inversions, and macroeconomic volatility without requiring periodic portfolio rebalancing, it carries practical challenges:
1. **Capital Inefficiency**: Dedication requires purchasing specific bonds at designated maturities, demanding significantly greater initial investment capital than duration immunization.
2. **Bond Illiquidity and Availability**: For long-dated liabilities maturing in 30 to 50 years, traded sovereign or investment-grade bonds with matching cash flows may simply not exist in public capital markets.
3. **Rebalancing Overhead**: In contrast, duration immunization allows the insurer to invest in highly liquid benchmark instruments, but requires dynamic, continuous rebalancing as time elapses and interest rates fluctuate.

## 1.15 Corporate Credit Spreads and Merton's Structural Default Model

In life insurer asset portfolios, corporate bonds offer yields exceeding sovereign debt benchmarks. The difference between the yield to maturity of a corporate bond $y_{\text{corp}}$ and a default-free sovereign bond $y_{\text{gov}}$ of identical maturity is the **Credit Spread** $s$:
$$s = y_{\text{corp}} - y_{\text{gov}}$$

The credit spread compensates the insurer for expected default loss, credit migration risk, and liquidity risk. In 1974, Nobel laureate Robert C. Merton formulated the foundational structural model of corporate default using Black-Scholes option pricing theory.

### Mathematical Formulation of Merton's Model
Consider a corporate firm whose total enterprise value $V(t)$ follows a geometric Brownian motion under the risk-neutral measure $\mathbb{Q}$:
$$dV(t) = r V(t)\,dt + \sigma_V V(t)\,dW(t)$$
where $r$ is the risk-free rate and $\sigma_V$ is the asset volatility.

The firm's capital structure consists of:
- Equity with market value $E(t)$.
- A single zero-coupon corporate bond with face value $D$ maturing at time $T$.

At maturity $T$:
- If firm asset value exceeds the debt obligation ($V(T) \ge D$), the firm repays bondholders in full ($D$), and equity holders receive the residual surplus $V(T) - D$.
- If firm value falls below debt face value ($V(T) < D$), the firm defaults. Bondholders seize all available firm assets $V(T)$, and equity holders receive zero.

Thus, the terminal payoff to equity is:
$$E(T) = \max(0, V(T) - D)$$
Equity is mathematically equivalent to a **European Call Option** on the firm's total assets with strike price equal to debt face value $D$!

By the Black-Scholes formula, current equity value is:
$$E(0) = V(0) \Phi(d_1) - D e^{-r T} \Phi(d_2)$$
where:
$$d_1 = \frac{\ln(V(0)/D) + (r + \frac{1}{2}\sigma_V^2)T}{\sigma_V \sqrt{T}}, \quad d_2 = d_1 - \sigma_V \sqrt{T}$$

By balance sheet conservation of value, the corporate debt value $B(0)$ is:
$$B(0) = V(0) - E(0) = D e^{-r T} \Phi(d_2) + V(0)[1 - \Phi(d_1)]$$

The risk-neutral probability of default before maturity $T$ is given by:
$$P(\text{Default}) = \Phi(-d_2)$$
The quantity $d_2$ is known as the **Distance to Default**. The corporate bond yield $y$ satisfies $B(0) = D e^{-y T}$, enabling exact analytical extraction of the theoretical credit spread:
$$s = y - r = -\frac{1}{T} \ln\left( \frac{B(0)}{D e^{-r T}} \right) = -\frac{1}{T} \ln\left( \Phi(d_2) + \frac{V(0)}{D e^{-r T}} \Phi(-d_1) \right)$$
Actuaries apply Merton's model to calculate default risk charges under Solvency II and Risk-Based Capital (RBC) frameworks.
"""

# --- UNIT 2 BOOSTER ---
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")
u2_add = r"""
## 2.14 Continuous Annuities Under Time-Varying Force of Interest

In financial mathematics, interest rates do not remain static across multi-decade accumulation periods. When the force of interest $\delta(t)$ varies continuously as a deterministic function of calendar time $t$, the discount factor from time $t$ back to time 0 is the exponential integral:

$$v(t) = \exp\left( -\int_0^t \delta(u)\,du \right)$$

The present value of a continuous payment stream paid at rate $\rho(t)$ over the interval $[0, n]$ is:

$$PV = \int_0^n \rho(t) v(t)\,dt = \int_0^n \rho(t) \exp\left( -\int_0^t \delta(u)\,du \right)\,dt$$

### 1. Linear Force of Interest: $\delta(t) = a + bt$
Suppose the force of interest rises or falls linearly with time ($b \ne 0$). The discount factor is:
$$\int_0^t (a + bu)\,du = at + \frac{1}{2} bt^2 \implies v(t) = e^{-(at + \frac{1}{2} bt^2)}$$

For a level continuous annuity ($\rho(t) = 1$):
$$\bar{a}_{\overline{n}|} = \int_0^n e^{-(at + \frac{1}{2} bt^2)}\,dt$$
Completing the square in the exponent:
$$at + \frac{1}{2}bt^2 = \frac{b}{2} \left( t^2 + \frac{2a}{b}t \right) = \frac{b}{2} \left[ \left( t + \frac{a}{b} \right)^2 - \frac{a^2}{b^2} \right] = \frac{1}{2} \left( \sqrt{b} t + \frac{a}{\sqrt{b}} \right)^2 - \frac{a^2}{2b}$$
Let $z = \sqrt{b} t + \frac{a}{\sqrt{b}}$, with $dz = \sqrt{b} dt$. The present value evaluates directly in terms of the standard Gaussian cumulative distribution function $\Phi(\cdot)$:

$$\bar{a}_{\overline{n}|} = \sqrt{\frac{2\pi}{b}} \exp\left( \frac{a^2}{2b} \right) \left[ \Phi\left( \sqrt{b} n + \frac{a}{\sqrt{b}} \right) - \Phi\left( \frac{a}{\sqrt{b}} \right) \right]$$

This closed-form Gaussian solution enables rapid valuation of variable-rate life contingencies without numerical quadratures.

### 2. Exponential Force of Interest: $\delta(t) = a e^{bt}$
If the force of interest accelerates exponentially (as observed during extreme currency debasement or hyperinflation):
$$\int_0^t a e^{bu}\,du = \frac{a}{b} (e^{bt} - 1) \implies v(t) = \exp\left( -\frac{a}{b} (e^{bt} - 1) \right) = e^{a/b} \exp\left( -\frac{a}{b} e^{bt} \right)$$
The present value integral transforms into an Incomplete Gamma function, providing analytical bounds for runaway inflation regimes.

## 2.15 Structured Debt Amortization: Prepayment Benchmarks and CMO Tranches

In residential mortgage-backed securities (RMBS) and Collateralized Mortgage Obligations (CMOs), underlying homeowners hold an embedded prepayment option: they may prepay all or part of their remaining mortgage balance at any time without penalty (typically to refinance when market rates decline).

### 1. Prepayment Mathematical Metrics: SMM and CPR
Prepayment behavior is quantified via two interconnected rates:
- **Single Monthly Mortality ($SMM$)**: The percentage of the beginning-of-month outstanding principal balance prepaid during month $t$:
  $$SMM_t = \frac{\text{Prepayments during month } t}{\text{Beginning Principal Balance}_t - \text{Scheduled Principal Repayment}_t}$$
- **Constant Prepayment Rate ($CPR$)**: The annualized equivalent prepayment rate:
  $$CPR = 1 - (1 - SMM)^{12} \iff SMM = 1 - (1 - CPR)^{1/12}$$

### 2. The PSA Standard Prepayment Benchmark
The Public Securities Association (PSA) benchmark establishes an industry-standard curve reflecting empirical homeowner behavior:
- A new mortgage experiences low prepayments initially while homeowners settle in.
- Prepayment rates ramp up linearly over the first 30 months by $0.2\%$ CPR per month, reaching $6\%$ CPR at month 30.
- For all months $t \ge 30$, the prepayment rate remains constant at $6\%$ CPR:

$$\text{CPR}(t) = \begin{cases}
6\% \times \left( \frac{t}{30} \right) = 0.2\% \times t & \text{for } 1 \le t \le 30 \\
6\% & \text{for } t > 30
\end{cases}$$

Prepayment speeds are expressed as multiples of the standard benchmark (e.g., $150\%$ PSA or $50\%$ PSA).

### 3. Sequential-Pay Tranches and Prepayment Risk Allocation
A CMO pools thousands of mortgages and restructures their cash flows into sequential-pay bond classes (Tranche A, Tranche B, Tranche C, and Tranche Z / Accrual):
- Tranches A, B, and C receive periodic interest concurrently.
- All principal payments (both scheduled amortization and prepayments) are directed exclusively to Tranche A until Tranche A is completely retired.
- Principal then cascades sequentially to Tranche B, then to Tranche C.
- Tranche Z receives neither interest nor principal until all earlier tranches are retired; its interest is capitalized, growing its principal balance.

By concentrating prepayment uncertainty, sequential structuring provides short-duration investors (such as commercial banks) with stable, protected cash flows via Tranche A, while long-duration institutional investors (life insurers and pension funds) acquire Tranche C and Z to match long-term liabilities.
"""

# --- UNIT 3 BOOSTER ---
u3_path = DRAFT_DIR / "unit-3.md"
u3_text = u3_path.read_text(encoding="utf-8")
u3_add = r"""
## 3.11 Analytical Expectation of Life: Euler-Maclaurin Expansion

A central theoretical distinction in demographic and actuarial science lies between:
1. **The Complete Expectation of Life ($e_x^\circ$)**: The expected total future lifetime from age $x$ in continuous time:
   $$e_x^\circ = \mathbb{E}[T_x] = \int_0^\infty {}_t p_x\,dt$$
2. **The Curtate Expectation of Life ($e_x$)**: The expected number of complete future years lived:
   $$e_x = \mathbb{E}[K_x] = \sum_{k=1}^\infty {}_k p_x$$

### 1. Derivation via the Euler-Maclaurin Summation Formula
To derive the exact relationship between the continuous integral and discrete summation, we deploy the **Euler-Maclaurin Summation Formula**.

For a smooth function $f(t)$ defined on $[0, \infty)$ with $\lim_{t \to \infty} f(t) = 0$:
$$\int_0^\infty f(t)\,dt = \sum_{k=1}^\infty f(k) + \frac{1}{2} f(0) - \frac{1}{12} f'(0) + \frac{1}{720} f'''(0) - \dots$$

Setting $f(t) = {}_t p_x$:
- At $t = 0$: $f(0) = {}_0 p_x = 1$.
- First derivative: $f'(t) = \frac{d}{dt} {}_t p_x = -{}_t p_x \mu_{x+t}$. At $t = 0$:
  $$f'(0) = -{}_0 p_x \mu_{x} = -\mu_x$$
- Substituting into the Euler-Maclaurin expansion:

$$e_x^\circ = e_x + \frac{1}{2} (1) - \frac{1}{12} (-\mu_x) + \mathcal{O}(f'''(0))$$

$$e_x^\circ \approx e_x + \frac{1}{2} + \frac{1}{12} \mu_x$$

### 2. Demographic and Practical Interpretation
The primary term $\frac{1}{2}$ reflects the standard assumption that deaths are distributed uniformly across each integer year of age, meaning that deceased individuals survive on average half a year ($0.5$) in their final year of life:
$$e_x^\circ \approx e_x + 0.5$$

The secondary correction term $+\frac{1}{12} \mu_x$ accounts for the curvature of the survival curve. At advanced ages ($x > 80$), where the force of mortality $\mu_x$ becomes substantial ($\mu_{85} \approx 0.10 - 0.15$), the correction term adds a measurable increment of $0.01$ to $0.015$ years.

### 3. Woolhouse's Formula for Fractional Curtate Expectations
If life expectancy is evaluated in discrete intervals of length $1/m$ (e.g., monthly intervals where $m = 12$):
$$e_x^{(m)} = \frac{1}{m} \sum_{k=1}^\infty {}_{k/m} p_x \approx e_x^\circ - \frac{1}{2m} - \frac{1}{12m^2} \mu_x$$
Substituting $e_x^\circ \approx e_x + \frac{1}{2}$:
$$e_x^{(m)} \approx e_x + \frac{m - 1}{2m}$$
For monthly evaluation ($m = 12$):
$$e_x^{(12)} \approx e_x + \frac{11}{24} \approx e_x + 0.4583$$
This relationship enables life annuity administrators to reconcile monthly pension benefit obligations with annual life table data.

## 3.12 Maximum Likelihood Estimation of Parametric Mortality Laws

To calibrate parametric mortality models (such as Gompertz $\mu_x = B c^x$ or Makeham $\mu_x = A + B c^x$) to insured lives, actuaries maximize the likelihood function of observed individual life histories.

### Mathematical Formulation of Likelihood for Censored Lifetime Data
Consider an actuarial study of $n$ insured individuals observed over an observation window. For individual $i \in \{1, 2, \dots, n\}$:
- The individual enters observation at age $x_i$.
- The individual exits observation at age $x_i + t_i$.
- Let $\delta_i \in \{0, 1\}$ be the censoring indicator: $\delta_i = 1$ if the individual died at age $x_i + t_i$, and $\delta_i = 0$ if the individual survived to the study end date or withdrew alive (right-censored).

The likelihood contribution of individual $i$ is:
$$L_i = \left( {}_{t_i} p_{x_i} \cdot \mu_{x_i + t_i} \right)^{\delta_i} \cdot \left( {}_{t_i} p_{x_i} \right)^{1 - \delta_i} = {}_{t_i} p_{x_i} \cdot [\mu_{x_i + t_i}]^{\delta_i}$$

Since ${}_{t_i} p_{x_i} = \exp\left( -\int_0^{t_i} \mu_{x_i + s}\,ds \right)$, the total log-likelihood for the cohort is:

$$\ln L = \sum_{i=1}^n \left[ \delta_i \ln \mu(x_i + t_i) - \int_0^{t_i} \mu(x_i + s)\,ds \right]$$

### Maximum Likelihood Estimation for the Gompertz Law
Under the Gompertz law, $\mu(x) = B c^x = e^{\alpha + \beta x}$ where $\alpha = \ln B$ and $\beta = \ln c > 0$.
The cumulative hazard integral is:
$$\int_0^{t_i} e^{\alpha + \beta (x_i + s)}\,ds = \frac{e^{\alpha + \beta x_i}}{\beta} (e^{\beta t_i} - 1)$$

The log-likelihood simplifies to:
$$\ln L(\alpha, \beta) = \sum_{i=1}^n \left[ \delta_i (\alpha + \beta (x_i + t_i)) - \frac{e^{\alpha + \beta x_i}}{\beta} (e^{\beta t_i} - 1) \right]$$

The score equations are obtained by taking partial derivatives:
$$\frac{\partial \ln L}{\partial \alpha} = \sum_{i=1}^n \left[ \delta_i - \frac{e^{\alpha + \beta x_i}}{\beta} (e^{\beta t_i} - 1) \right] = 0$$
$$\frac{\partial \ln L}{\partial \beta} = \sum_{i=1}^n \left[ \delta_i (x_i + t_i) - \frac{e^{\alpha + \beta x_i}}{\beta} \left( t_i e^{\beta t_i} - \frac{e^{\beta t_i} - 1}{\beta} \right) \right] = 0$$

Solving these non-linear equations via Newton-Raphson iteration yields the maximum likelihood estimates $(\hat{\alpha}, \hat{\beta})$. Inverting the observed Fisher Information Matrix provides the asymptotic variance-covariance matrix:
$$\mathbf{\Sigma} = \begin{pmatrix} -\frac{\partial^2 \ln L}{\partial \alpha^2} & -\frac{\partial^2 \ln L}{\partial \alpha \partial \beta} \\ -\frac{\partial^2 \ln L}{\partial \alpha \partial \beta} & -\frac{\partial^2 \ln L}{\partial \beta^2} \end{pmatrix}^{-1}$$
enabling the actuary to construct Wald confidence intervals for projected mortality rates.
"""

# --- UNIT 4 BOOSTER ---
u4_path = DRAFT_DIR / "unit-4.md"
u4_text = u4_path.read_text(encoding="utf-8")
u4_add = r"""
## 4.10 Multi-State Actuarial Cash Flow Valuation: Active-Disabled-Death Continuum

To price complex health contingencies (such as long-term care policies, critical illness insurance, and permanent disability income riders), actuaries combine the transition probabilities $p_{x}^{ij}(s, t)$ derived from Kolmogorov forward equations with continuous financial discounting.

### 1. Actuarial Present Value of Benefit Cash Flows
Consider an active life aged $x$ at time $t = 0$ in State 0 (Active). The policy provides:
1. An annuity benefit paid continuously at rate $b(t)$ while the policyholder is in State 1 (Disabled).
2. A lump sum death benefit $S(t)$ paid immediately upon transition from any live state to State 2 (Dead).

The **Actuarial Present Value (APV)** of the disability annuity benefit is:

$$\bar{a}_{x}^{01} = \int_0^\infty v^t \cdot p_{x}^{01}(0, t) \cdot b(t)\,dt = \int_0^\infty e^{-\delta t} \cdot p_{x}^{01}(0, t) \cdot b(t)\,dt$$

The Actuarial Present Value of the death benefit is:

$$\bar{A}_{x}^{02} = \int_0^\infty e^{-\delta t} \left[ p_{x}^{00}(0, t) \mu_{x+t}^{02} + p_{x}^{01}(0, t) \mu_{x+t}^{12} \right] S(t)\,dt$$

The term inside the brackets represents the total probability density of entering the absorbing death state at duration $t$, decomposing into deaths occurring directly from the active state ($p_{x}^{00} \mu^{02}$) and deaths occurring from the disabled state ($p_{x}^{01} \mu^{12}$).

### 2. Premium Equivalence in Multi-State Models
Let the policyholder pay a level annual premium continuously at rate $\bar{P}$ while active (State 0). Premium payments cease immediately upon disability or death (a built-in **Waiver of Premium Benefit**).

The Actuarial Present Value of premium inflows is:
$$\text{APV}(\text{Premiums}) = \bar{P} \cdot \bar{a}_{x}^{00} = \bar{P} \int_0^\infty e^{-\delta t} p_{x}^{00}(0, t)\,dt$$

By the Equivalence Principle, equating expected premium inflows to expected benefit outflows:
$$\bar{P} \cdot \bar{a}_{x}^{00} = \bar{a}_{x}^{01} + \bar{A}_{x}^{02} \implies \bar{P} = \frac{\bar{a}_{x}^{01} + \bar{A}_{x}^{02}}{\bar{a}_{x}^{00}}$$

This general formulation provides the mathematical foundation for modern health insurance reserving across all international regulatory jurisdictions.

## 4.11 Reversionary Annuities and Contingent Insurance Valuation

Actuaries frequently design contracts whose benefit payouts depend on the specific order in which two or more lives die.

### 1. The Reversionary Annuity ($\bar{a}_{x|y}$)
A **Reversionary Annuity** is issued to two lives $(x)$ and $(y)$. It pays a continuous annuity at rate 1 per year to $(y)$ following the death of $(x)$, provided $(y)$ is still alive. The payments cease upon the subsequent death of $(y)$.

Let $I_y(t)$ be the indicator that $(y)$ is alive at time $t$, and let $I_x(t)$ be the indicator that $(x)$ is alive at time $t$. Payment occurs at time $t$ if and only if $(y)$ is alive and $(x)$ is dead:
$$\text{Payment at time } t = I_y(t) \cdot (1 - I_x(t)) = I_y(t) - I_y(t) I_x(t)$$

Taking expectations discounted by $e^{-\delta t}$:
$$\mathbb{E}[e^{-\delta t} I_y(t)] = e^{-\delta t} {}_t p_y$$
$$\mathbb{E}[e^{-\delta t} I_y(t) I_x(t)] = e^{-\delta t} {}_t p_{xy}$$

Integrating over all future durations $t \in [0, \infty)$:

$$\bar{a}_{x|y} = \int_0^\infty e^{-\delta t} \left( {}_t p_y - {}_t p_{xy} \right) dt = \int_0^\infty e^{-\delta t} {}_t p_y\,dt - \int_0^\infty e^{-\delta t} {}_t p_{xy}\,dt$$

$$\bar{a}_{x|y} = \bar{a}_y - \bar{a}_{xy}$$

This identity proves that a reversionary annuity can be synthesized as a long position in a single life annuity on $(y)$ combined with a short position in a joint life annuity on $(xy)$.

### 2. Contingent Life Assurances ($\bar{A}_{xy}^1$ and $\bar{A}_{xy}^2$)
A **Contingent Life Assurance** pays a benefit upon the death of one life, conditional upon the survival status of the other life:
- $\bar{A}_{xy}^1$: Pays 1 at the moment of death of $(x)$, provided that $(x)$ dies before $(y)$.
- $\bar{A}_{xy}^2$: Pays 1 at the moment of death of $(x)$, provided that $(x)$ dies after $(y)$.

The net single premium for $\bar{A}_{xy}^1$ is:
$$\bar{A}_{xy}^1 = \int_0^\infty e^{-\delta t} {}_t p_{xy} \mu_{x+t}\,dt$$

For $\bar{A}_{xy}^2$:
$$\bar{A}_{xy}^2 = \int_0^\infty e^{-\delta t} {}_t p_x (1 - {}_t p_y) \mu_{x+t}\,dt = \int_0^\infty e^{-\delta t} {}_t p_x \mu_{x+t}\,dt - \int_0^\infty e^{-\delta t} {}_t p_{xy} \mu_{x+t}\,dt$$

$$\bar{A}_{xy}^2 = \bar{A}_x - \bar{A}_{xy}^1$$

Summing the two contingent assurances:
$$\bar{A}_{xy}^1 + \bar{A}_{xy}^2 = \bar{A}_x$$
Because $(x)$ must either die before $(y)$ or die after $(y)$, the sum of the two mutually exclusive contingent assurances reconstitutes the unconstrained single life whole life assurance on $(x)$.
"""

# --- UNIT 5 BOOSTER ---
u5_path = DRAFT_DIR / "unit-5.md"
u5_text = u5_path.read_text(encoding="utf-8")
u5_add = r"""
## 5.10 Multiregional Demographic Projections: Andrei Rogers' Matrix Framework

In national demographic planning, human populations do not reside in isolated closed environments. Instead, populations are distributed across geographic regions, provinces, or metropolitan areas, interconnected by continuous inter-regional internal migration.

To model spatial demographic dynamics simultaneously, Andrei Rogers (1975) formulated the **Multiregional Demographic Accounting Framework**.

### 1. The Multiregional Life Table
Let a nation be partitioned into $R$ distinct geographic regions ($i, j \in \{1, 2, \dots, R\}$).
Let $\mathbf{l}(x)$ denote the $R \times R$ multiregional survival matrix, where element $l_{ij}(x)$ represents the probability that an individual born in region $i$ is alive and residing in region $j$ at age $x$.

The survival matrix differential system satisfies:
$$\frac{d}{dx} \mathbf{l}(x) = -\mathbf{l}(x) \mathbf{\mu}(x)$$
where $\mathbf{\mu}(x)$ is the $R \times R$ mobility and mortality hazard rate matrix:
$$\mathbf{\mu}(x) = \begin{pmatrix}
\mu_{1\bullet}(x) & -\mu_{12}(x) & \dots & -\mu_{1R}(x) \\
-\mu_{21}(x) & \mu_{2\bullet}(x) & \dots & -\mu_{2R}(x) \\
\vdots & \vdots & \ddots & \vdots \\
-\mu_{R1}(x) & -\mu_{R2}(x) & \dots & \mu_{R\bullet}(x)
\end{pmatrix}$$
with off-diagonal entries $-\mu_{ij}(x)$ representing instantaneous migration intensities from region $i$ to region $j$, and diagonal entries representing total exit intensity:
$$\mu_{i\bullet}(x) = \mu_{id}(x) + \sum_{j \ne i} \mu_{ij}(x)$$
where $\mu_{id}(x)$ is the death rate in region $i$.

### 2. Discrete Transition Matrix Estimation
In discrete empirical analysis with age interval $h$ (typically $h = 5$ years), the multiregional transition probability matrix $\mathbf{P}(x)$ from age $x$ to $x + h$ is approximated via the central rate matrix $\mathbf{M}(x)$:

$$\mathbf{P}(x) = \left[ \mathbf{I} + \frac{h}{2} \mathbf{M}(x) \right]^{-1} \left[ \mathbf{I} - \frac{h}{2} \mathbf{M}(x) \right]$$

This bilinear transformation guarantees that all transition probabilities remain strictly positive and rows sum to the appropriate regional survival totals.

### 3. Spatial Population Projection
Let $\mathbf{K}_t$ be the multiregional population vector at time $t$, organized by region and age class. The population evolves according to the generalized multiregional growth operator:
$$\mathbf{K}_{t+1} = \mathbf{G} \mathbf{K}_t$$
where $\mathbf{G}$ is the block multiregional projection matrix. Spectral analysis of $\mathbf{G}$ yields the long-run spatial distribution of the national population, revealing regional urbanization trends and internal depopulation trajectories.

## 5.11 Weak vs Strong Ergodicity in Demographic Theory

A profound foundational question in mathematical demography is: **to what extent does the current age structure of a human population reflect its initial historical conditions versus its ongoing vital rates?**

This inquiry is resolved by the **Ergodic Theorems of Demography**.

### 1. Strong Ergodicity (Constant Vital Rates)
Formulated by Alfred Lotka and F. R. Sharpe:
*Theorem*: If a closed population is subjected to constant age-specific mortality rates $\ell(x)$ and constant fertility rates $m(x)$ over time, the age distribution of the population converges asymptotically to a unique stable age profile $c(x) = b e^{-rx} \ell(x)$, completely independent of the initial age distribution $\mathbf{n}_0$.
Mathematically:
$$\lim_{t \to \infty} \frac{\mathbf{n}_t}{\sum_j n_{j, t}} = \mathbf{u}$$
where $\mathbf{u}$ is the normalized dominant right eigenvector of the projection operator.

### 2. Weak Ergodicity (Time-Varying Vital Rates)
In real human history, vital rates are never constant: fertility fluctuates across baby booms and busts, and mortality shifts with medical breakthroughs and pandemics. Alvaro Lopez (1961) proved the remarkable **Weak Ergodic Theorem**:

*Theorem*: Consider two populations with arbitrary, completely different initial age vectors $\mathbf{x}_0$ and $\mathbf{y}_0$. If both populations are subjected from time $t = 0$ onward to the *exact same sequence* of time-varying fertility and mortality projection matrices $\{\mathbf{L}_1, \mathbf{L}_2, \mathbf{L}_3, \dots\}$, then the relative age distributions of the two populations will become asymptotically identical as $t \to \infty$:

$$\lim_{t \to \infty} \left\| \frac{\mathbf{x}_t}{\mathbf{1}^T \mathbf{x}_t} - \frac{\mathbf{y}_t}{\mathbf{1}^T \mathbf{y}_t} \right\| = 0$$

*Proof Intuition via Hilbert's Projective Metric*:
Lopez's proof utilizes the **Birkhoff-Hilbert Projective Metric** $d_H(\mathbf{x}, \mathbf{y})$ on the positive cone $\mathbb{R}_+^K$:
$$d_H(\mathbf{x}, \mathbf{y}) = \ln\left( \max_{i, j} \frac{x_i y_j}{x_j y_i} \right)$$
Each non-negative projection matrix $\mathbf{L}_t$ acts as a strict contraction mapping under the Hilbert metric:
$$d_H(\mathbf{L}_t \mathbf{x}, \mathbf{L}_t \mathbf{y}) \le \tau(\mathbf{L}_t) \cdot d_H(\mathbf{x}, \mathbf{y})$$
where the Birkhoff contraction coefficient satisfies $\tau(\mathbf{L}_t) < 1$.

As time progresses, repeated multiplication contracts the distance exponentially:
$$d_H(\mathbf{x}_t, \mathbf{y}_t) \le \left( \prod_{s=1}^t \tau(\mathbf{L}_s) \right) d_H(\mathbf{x}_0, \mathbf{y}_0) \to 0 \quad \text{as } t \to \infty$$

Weak ergodicity establishes that the demographic past is completely forgotten: after 70 to 100 years, the age structure of a nation is entirely determined by its recent vital rates, bearing zero statistical trace of its historical origins.
"""

# --- UNIT 6 BOOSTER ---
u6_path = DRAFT_DIR / "unit-6.md"
u6_text = u6_path.read_text(encoding="utf-8")
u6_add = r"""
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
"""

# --- UNIT 7 BOOSTER ---
u7_path = DRAFT_DIR / "unit-7.md"
u7_text = u7_path.read_text(encoding="utf-8")
u7_add = r"""
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
"""

# --- UNIT 8 BOOSTER ---
u8_path = DRAFT_DIR / "unit-8.md"
u8_text = u8_path.read_text(encoding="utf-8")
u8_add = r"""
## 8.10 Numerical Inversion of Aggregate Claims: The Fast Fourier Transform (FFT)

While Panjer's recursion provides an exact method for computing aggregate claims distributions when claim frequency belongs to the $(a, b, 0)$ or $(a, b, 1)$ classes, many empirical insurance portfolios feature claim frequency distributions outside these families (e.g., Delaporte distributions, zero-modified Poisson-inverse Gaussian mixtures).

To compute the aggregate claims distribution $g_k = P(S = k)$ for arbitrary frequency and continuous severity distributions, modern actuarial science utilizes **Characteristic Function Inversion via the Fast Fourier Transform (FFT)**.

### 1. The Characteristic Function of Aggregate Claims
Recall that the aggregate claims random variable is $S = \sum_{j=1}^N X_j$.
Let $\phi_X(t) = \mathbb{E}[e^{itX}]$ denote the characteristic function of individual claim severity $X$, and let $P_N(z) = \mathbb{E}[z^N]$ denote the probability generating function of claim count $N$.

By the tower property of conditional expectation:

$$\phi_S(t) = \mathbb{E}\left[ e^{itS} \right] = \mathbb{E}\left[ \mathbb{E}\left[ \exp\left( it \sum_{j=1}^N X_j \right) \Bigg| N \right] \right] = \mathbb{E}\left[ (\phi_X(t))^N \right] = P_N(\phi_X(t))$$

For a Compound Poisson process with frequency parameter $\lambda$:
$$\phi_S(t) = \exp\left( \lambda (\phi_X(t) - 1) \right)$$
For a Compound Negative Binomial process with parameters $(r, p)$:
$$\phi_S(t) = \left( \frac{p}{1 - (1 - p)\phi_X(t)} \right)^r$$

### 2. Discretization and Discrete Fourier Transform (DFT)
Let claim severity be discretized on a regular grid of size $h > 0$ with $M = 2^m$ points ($M \in \{1024, 2048, 4096, 8192\}$):
$$\mathbf{f} = [f_0, f_1, f_2, \dots, f_{M-1}]^T, \quad f_k = P(X = k \cdot h)$$

The Discrete Fourier Transform of the severity vector $\mathbf{f}$ is:
$$\hat{f}_k = \sum_{j=0}^{M-1} f_j \exp\left( \frac{2\pi i \cdot j \cdot k}{M} \right) \quad \text{for } k = 0, 1, \dots, M-1$$
This is computed in $\mathcal{O}(M \log M)$ operations using the Cooley-Tukey FFT algorithm.

Next, the aggregate characteristic values $\hat{g}_k$ are evaluated directly through the theoretical generating relation:
$$\hat{g}_k = P_N(\hat{f}_k) = \exp\left( \lambda (\hat{f}_k - 1) \right)$$

Finally, the probability mass function of aggregate claims $\mathbf{g} = [g_0, g_1, \dots, g_{M-1}]^T$ is recovered via the Inverse Fast Fourier Transform (IFFT):

$$g_j = \frac{1}{M} \sum_{k=0}^{M-1} \hat{g}_k \exp\left( -\frac{2\pi i \cdot j \cdot k}{M} \right)$$

### 3. Mitigating Aliasing and Wrapping Errors: Exponential Tilting
Because the discrete Fourier transform implicitly assumes periodic boundary conditions with period $M$, aggregate claim probabilities beyond $M$ wrap around and contaminate early probabilities $g_0, g_1$, creating **Aliasing / Wrapping Error**.

To eliminate aliasing, actuaries deploy **Exponential Tilting (Esscher Transform)**:
1. Define the tilted severity distribution:
   $$\tilde{f}_j = e^{-\theta j} f_j$$
   where $\theta > 0$ is a damping parameter.
2. Run the FFT and IFFT on the tilted distribution to obtain the tilted aggregate probabilities $\tilde{g}_j$.
3. Untilt the resulting aggregate distribution:
   $$g_j = e^{\theta j} \tilde{g}_j$$
Exponential damping suppresses tail values prior to periodicity wrapping, reducing aliasing error below machine precision ($10^{-14}$) and ensuring pristine aggregate stop-loss reinsurance pricing.

## 8.11 Liability-Driven Investment (LDI) and Dynamic Pension Solvency

In defined benefit pension management, traditional asset allocation models that focus purely on maximizing asset returns (e.g., $60\%$ equities / $40\%$ bonds) expose pension plans to catastrophic funding ratio collapses when interest rates drop.

To guarantee solvency, pension funds deploy **Liability-Driven Investment (LDI)**.

### 1. The Pension Funding Ratio and Surplus Volatility
Let $A$ be the market value of pension plan assets, and let $L$ be the Present Value of Defined Benefit Liabilities ($PVFB$ or $AAL$).
The **Funding Ratio** is:
$$FR = \frac{A}{L}$$
The pension **Surplus** is:
$$S = A - L$$

The variance of changes in pension surplus $\Delta S = \Delta A - \Delta L$ is:

$$\sigma_S^2 = \sigma_A^2 + \sigma_L^2 - 2 \rho_{AL} \sigma_A \sigma_L$$

where $\sigma_A$ is asset volatility, $\sigma_L$ is liability volatility, and $\rho_{AL}$ is the asset-liability correlation.

If assets are invested in equities while liabilities consist of long-duration guaranteed bonds, the asset-liability correlation $\rho_{AL}$ is close to zero or negative. Consequently, surplus volatility is massive ($\sigma_S^2 \approx \sigma_A^2 + \sigma_L^2$). If interest rates drop by 100 basis points, liabilities surge by $20\%$, causing the funding ratio to collapse into deep deficit.

### 2. The LDI Portfolio Bifurcation
LDI decomposes the pension portfolio into two dedicated structural allocations:
1. **The Liability Hedging Portfolio (LHP)**: Designed strictly to achieve $\rho_{AL} \approx 1.0$ and match the key rate duration and inflation sensitivity of liabilities:
   - Physical long-dated sovereign bonds and index-linked gilts.
   - Derivative overlays: **Interest Rate Swaps**, **Inflation Swaps**, and **Swaptions**. In a receiver swap, the pension fund receives fixed interest and pays floating, synthesizing long bond duration with minimal cash capital outlay.
2. **The Return-Seeking Portfolio (RSP)**: Invested in high-expected-return growth assets (global equities, private infrastructure, private credit, and real estate) to systematically eliminate any existing unfunded actuarial liability ($UAL$).

By matching liability duration via synthetic swaps in the LHP, $\rho_{AL} \to 1.0$ and $\sigma_L \approx \sigma_A^{\text{hedging}}$, surplus volatility $\sigma_S^2 \to 0$. This stabilizes employer pension contribution rates, insulates corporate sponsors from balance sheet volatility, and secures the retirement pensions of millions of workers.
"""

booster_expansions = [
    (1, u1_path, u1_text, u1_add),
    (2, u2_path, u2_text, u2_add),
    (3, u3_path, u3_text, u3_add),
    (4, u4_path, u4_text, u4_add),
    (5, u5_path, u5_text, u5_add),
    (6, u6_path, u6_text, u6_add),
    (7, u7_path, u7_text, u7_add),
    (8, u8_path, u8_text, u8_add),
]

for unit_num, path, text, add in booster_expansions:
    marker = "## Fully worked question 1:"
    idx = text.find(marker)
    if idx == -1:
        print(f"Warning: Marker not found in unit {unit_num}!")
        continue
    new_text = text[:idx] + add.strip() + "\n\n" + text[idx:]
    path.write_text(new_text, encoding="utf-8")
    print(f"Unit {unit_num} boosted successfully.")

print("All units boosted.")
