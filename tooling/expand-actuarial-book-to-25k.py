#!/usr/bin/env python3
"""
Comprehensive expansion script for Actuarial Statistics and Mathematical Demography
to bring the book draft past 25,000 substantive prose words across all 8 units.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"

# --- UNIT 1 EXPANSION ---
u1_path = DRAFT_DIR / "unit-1.md"
u1_text = u1_path.read_text(encoding="utf-8")
u1_expansion = r"""
## 1.11 Continuous Term Structure Parametrization: Nelson-Siegel and Svensson Models

In institutional actuarial risk management and central banking, yield curves cannot be observed at every continuous maturity $t \in [0, \infty)$. Market observers only record discretely traded bond prices and sovereign debt yields at specific benchmark tenors such as 1 month, 3 months, 6 months, 1 year, 2 years, 5 years, 10 years, and 30 years. To determine the present value of arbitrary liability cash flows occurring at fractional intermediate maturities, actuaries must fit a smooth, continuous zero-coupon yield curve across the entire maturity spectrum.

The most widely adopted parametric yield curve estimation family in international insurance regulation and sovereign debt modeling is the model proposed by Charles Nelson and Andrew Siegel in 1987, alongside its four-parameter extension formulated by Lars Svensson in 1994.

### 1. The Nelson-Siegel Parametric Form
Nelson and Siegel hypothesized that the instantaneous forward rate curve $f(t)$ can be modeled as the solution to a second-order linear differential equation with repeated real roots. The instantaneous forward rate $f(t)$ for maturity $t$ is parametrized as:

$$f(t) = \beta_0 + \beta_1 e^{-t/\tau} + \beta_2 \frac{t}{\tau} e^{-t/\tau}$$

Integrating the instantaneous forward rate over the interval $[0, t]$ yields the spot zero-coupon yield curve $y(t)$:

$$y(t) = \frac{1}{t} \int_0^t f(u)\,du = \beta_0 + \beta_1 \left( \frac{1 - e^{-t/\tau}}{t/\tau} \right) + \beta_2 \left( \frac{1 - e^{-t/\tau}}{t/\tau} - e^{-t/\tau} \right)$$

Each parameter in the Nelson-Siegel formulation admits an intuitive economic and structural interpretation:
1. **$\beta_0$ (The Long-Term Factor or Level)**: As maturity approaches infinity ($t \to \infty$), the decay factors $\frac{1 - e^{-t/\tau}}{t/\tau} \to 0$ and $e^{-t/\tau} \to 0$. Consequently, $\lim_{t \to \infty} y(t) = \beta_0$. The parameter $\beta_0$ determines the asymptotic long-term discount rate, reflecting long-run equilibrium real interest rates and secular inflation expectations.
2. **$\beta_1$ (The Short-Term Factor or Slope)**: At zero maturity ($t \to 0$), $\lim_{t \to 0} y(t) = \beta_0 + \beta_1$. Therefore, $\beta_1 = y(0) - \beta_0$. Because $\beta_1$ represents the difference between the immediate overnight money-market rate and the infinite-horizon rate, negative values of $\beta_1$ correspond to normal, upward-sloping yield curves, while positive values indicate an inverted yield curve signaling impending macroeconomic contractions.
3. **$\beta_2$ (The Medium-Term Factor or Curvature / Hump)**: The weight assigned to $\beta_2$ is zero at $t = 0$, approaches zero as $t \to \infty$, and achieves a unique interior maximum at $t = \tau$. Hence, $\beta_2$ controls the magnitude and direction of the yield curve curvature or hump occurring around the characteristic maturity $\tau$.
4. **$\tau > 0$ (The Scale Parameter)**: The constant $\tau$ specifies the exact tenor at which the curvature loading reaches its maximum, governing the rate of exponential decay across the term structure.

### 2. The Svensson Extension
To accommodate complex yield curve geometries featuring two distinct humps or twisted inflection points (frequently observed during monetary policy transitions or quantitative easing episodes), Svensson added a second curvature component:

$$y(t) = \beta_0 + \beta_1 \left( \frac{1 - e^{-t/\tau_1}}{t/\tau_1} \right) + \beta_2 \left( \frac{1 - e^{-t/\tau_1}}{t/\tau_1} - e^{-t/\tau_1} \right) + \beta_3 \left( \frac{1 - e^{-t/\tau_2}}{t/\tau_2} - e^{-t/\tau_2} \right)$$

This six-parameter formulation ($\beta_0, \beta_1, \beta_2, \beta_3, \tau_1, \tau_2$) is the official standard employed by the European Central Bank (ECB) and the United States Federal Reserve for daily publication of continuous zero-coupon sovereign term structures. Actuaries discount multi-decade guaranteed pension and annuity obligations against these regulatory Svensson curves to establish technical solvency provisions.

## 1.12 Key Rate Duration and Non-Parallel Yield Curve Shifts

Classical Macaulay and modified durations rest on a restrictive mathematical assumption: that interest rate fluctuations consist exclusively of uniform, parallel translations across all maturities ($\Delta y(t) = \Delta y$ for all $t$). In empirical financial markets, however, yield curve movements are inherently non-parallel, dominated by steepening, flattening, twisting, and butterfly transformations.

To measure exposure to non-parallel shifts, Thomas Ho introduced **Key Rate Duration** in 1992.

### Mathematical Formulation of Key Rate Duration
Let the continuous term structure be divided into $K$ specified key maturities:
$$t_1 < t_2 < \dots < t_K$$
Commonly selected key maturities include $0.25, 1, 2, 5, 10, 20,$ and $30$ years.

A key rate shift of magnitude $\Delta y_k$ centered at key maturity $t_k$ represents a localized triangular perturbation of the yield curve:
- The yield change is exactly $\Delta y_k$ at $t = t_k$.
- The yield change declines linearly to zero at the adjacent key maturities $t_{k-1}$ and $t_{k+1}$.
- The yield change is strictly zero for all maturities $t \le t_{k-1}$ and $t \ge t_{k+1}$.

For an arbitrary maturity $t \in [t_{k-1}, t_k]$, the shift sensitivity weight is:
$$w_k(t) = \frac{t - t_{k-1}}{t_k - t_{k-1}}$$
For $t \in [t_k, t_{k+1}]$, the sensitivity weight is:
$$w_k(t) = \frac{t_{k+1} - t}{t_{k+1} - t_k}$$

The **Key Rate Duration** of an asset or liability portfolio with value $P$ with respect to key maturity $t_k$ is defined as the normalized partial derivative:

$$D_k = -\frac{1}{P} \frac{\partial P}{\partial y_k} \approx -\frac{P(y_k + \Delta y) - P(y_k - \Delta y)}{2\,P\,\Delta y}$$

### Fundamental Properties and Asset-Liability Matching
1. **Summation Property**: Because the piecewise linear triangular shift functions sum identically to unity across all maturities ($\sum_{k=1}^K w_k(t) = 1$ for all $t$), the sum of all key rate durations equals the aggregate effective duration of the portfolio:
   $$\sum_{k=1}^K D_k = D_{\text{eff}}$$
2. **Key Rate Immunization**: To immunize a life insurance company or pension fund against arbitrary yield curve twists, shifts, and butterfly bends, the asset portfolio $A$ and liability portfolio $L$ must satisfy key rate matching at every individual key maturity:
   $$D_k(A) \cdot PV(A) = D_k(L) \cdot PV(L) \quad \text{for each } k = 1, 2, \dots, K$$
When key rate durations are matched across all key points, the net asset-liability surplus is fully insulated against non-parallel yield curve rotations, providing vastly superior capital protection compared to traditional single-metric Redington duration matching.
"""

# --- UNIT 2 EXPANSION ---
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")
u2_expansion = r"""
## 2.10 Comprehensive Amortization Schedule Proofs and Fractional Duration Balances

A rigorous understanding of loan amortization requires proving the exact algebraic equivalence of the prospective and retrospective outstanding loan balances at any arbitrary integer payment period $k \in \{0, 1, \dots, n\}$, and extending these formulations to fractional evaluation dates $k + s$ where $0 < s < 1$.

### 1. Algebraic Equivalence of Prospective and Retrospective Balances
Consider a loan of principal $L$ issued at time $t = 0$, repaid through $n$ level annual end-of-year installments of amount $P$ at effective interest rate $i$. By the equation of value:
$$L = P \cdot a_{\overline{n}|i} = P \left( \frac{1 - v^n}{i} \right)$$

The **Prospective Outstanding Balance** $B_k^{\text{pro}}$ immediately following the $k$-th payment equals the present value of the remaining $n - k$ installments:
$$B_k^{\text{pro}} = P \cdot a_{\overline{n - k}|i} = P \left( \frac{1 - v^{n - k}}{i} \right)$$

The **Retrospective Outstanding Balance** $B_k^{\text{retro}}$ immediately following the $k$-th payment equals the accumulated value of the original loan principal minus the accumulated value of all $k$ past installments:
$$B_k^{\text{retro}} = L(1 + i)^k - P \cdot s_{\overline{k}|i} = L(1 + i)^k - P \left( \frac{(1 + i)^k - 1}{i} \right)$$

We now prove that $B_k^{\text{pro}} \equiv B_k^{\text{retro}}$ for all $k \in \{0, 1, \dots, n\}$:
Substitute $L = P \cdot a_{\overline{n}|i}$ into the retrospective expression:
$$\begin{aligned}
B_k^{\text{retro}} &= P \cdot a_{\overline{n}|i} (1 + i)^k - P \cdot s_{\overline{k}|i} \\
&= P \left[ \frac{1 - v^n}{i} (1 + i)^k - \frac{(1 + i)^k - 1}{i} \right] \\
&= \frac{P}{i} \left[ (1 + i)^k - v^n (1 + i)^k - (1 + i)^k + 1 \right] \\
&= \frac{P}{i} \left[ 1 - v^n v^{-k} \right] = \frac{P}{i} \left[ 1 - v^{n - k} \right] \\
&= P \cdot a_{\overline{n - k}|i} = B_k^{\text{pro}}
\end{aligned}$$
This establishes that both perspectives are mathematically identical under compound interest.

### 2. Outstanding Balance at Fractional Dates ($k + s$)
In commercial banking, an institutional borrower may refinance or prepay a loan at a fractional duration $k + s$, where $k$ is an integer number of elapsed periods and $s \in (0, 1)$ represents the fraction of the current period elapsed since payment $k$.

Two alternative valuation conventions exist in actuarial practice:
1. **Theoretical Compound Interest Method**: Under continuous compounding, the outstanding balance at time $k + s$ is the balance immediately following payment $k$ accumulated by the compound interest factor $(1 + i)^s$:
   $$B_{k + s}^{\text{theoretical}} = B_k (1 + i)^s = P \cdot a_{\overline{n - k}|i} (1 + i)^s$$
2. **Practical Linear Interpolation Method (Accrued Interest)**: Under banking regulations, interest is calculated using simple interest over the partial period. The total payoff amount equals the previous balance plus accrued simple interest:
   $$B_{k + s}^{\text{practical}} = B_k (1 + s \cdot i)$$
Since $(1 + i)^s < 1 + s \cdot i$ for all $s \in (0, 1)$ by Bernoulli's inequality, the practical simple interest convention generates a slightly higher payoff balance, providing a modest margin of conservatism to the lending institution.

## 2.11 Adjustable Rate Mortgages (ARMs) and Negative Amortization

While fixed-rate mortgages guarantee an invariant periodic payment $P$ throughout the entire loan tenure, modern financial markets feature extensive arrays of **Adjustable Rate Mortgages (ARMs)** where the interest rate adjusts periodically to reflect prevailing money-market benchmarks (such as SOFR or the Treasury Constant Maturity yield).

### Mathematical Mechanics of Rate Adjustments
Let a loan have initial principal $L_0$, amortization tenure of $n$ periods, and initial interest rate $i_1$. The initial payment is:
$$P_1 = \frac{L_0}{a_{\overline{n}|i_1}}$$
At the end of year $m_1$, the loan interest rate resets from $i_1$ to a new rate $i_2$. The outstanding principal balance immediately preceding the reset is $B_{m_1} = P_1 a_{\overline{n - m_1}|i_1}$.

To amortize the remaining balance over the residual $n - m_1$ periods, the mortgage servicer recomputes the periodic installment to $P_2$:
$$P_2 = \frac{B_{m_1}}{a_{\overline{n - m_1}|i_2}}$$
If market interest rates rise ($i_2 > i_1$), the required installment increases ($P_2 > P_1$), exposing the borrower to payment shock.

### Negative Amortization and Payment Caps
To shield consumers from sudden payment shocks, certain contracts establish **Payment Caps**, specifying that the periodic installment cannot increase by more than a contractual percentage $c_{\text{cap}}$ (for example, a $7.5\%$ annual cap: $P_{\text{capped}} = P_{\text{old}} \cdot (1 + c_{\text{cap}})$).

When interest rates surge dramatically, the capped payment $P_{\text{capped}}$ may be less than the periodic interest accrued on the outstanding loan balance:
$$P_{\text{capped}} < i_{\text{current}} \cdot B_{t-1}$$
Under these conditions:
1. The interest charge due for the period is $I_t = i_{\text{current}} \cdot B_{t-1}$.
2. The principal repayment portion is negative:
   $$R_t = P_{\text{capped}} - I_t < 0$$
3. The unpaid interest is capitalized into the loan principal, expanding the loan balance:
   $$B_t = B_{t-1} + (I_t - P_{\text{capped}}) > B_{t-1}$$
This phenomenon is known as **Negative Amortization**. If uncontrolled, negative amortization increases loan-to-value (LTV) ratios and amplifies default risk. Mortgage contracts typically impose a negative amortization cap (e.g., $115\%$ or $125\%$ of original principal), at which point payment caps are legally abrogated and payments are fully recast to amortize the enlarged debt.
"""

# --- UNIT 3 EXPANSION ---
u3_path = DRAFT_DIR / "unit-3.md"
u3_text = u3_path.read_text(encoding="utf-8")
u3_expansion = r"""
## 3.7 Fractional Age Assumptions: Exact Mathematical Derivations

Life tables report survival numbers $l_x$ and mortality probabilities $q_x$ exclusively at integer ages $x \in \{0, 1, 2, \dots, \omega\}$. However, actuarial events such as policy death claims, annuity commencements, and premium surrender adjustments occur continuously at arbitrary fractional ages $x + t$, where $x$ is an integer age and $0 < t < 1$.

To evaluate probabilities involving fractional durations, actuaries invoke one of three standard mathematical assumptions regarding the distribution of deaths within the integer year of age $[x, x + 1)$.

### 1. Uniform Distribution of Deaths (UDD)
The **Uniform Distribution of Deaths** hypothesis assumes that the future lifetime random variable $T_x$ is uniformly distributed over the unit interval $[0, 1)$. Equivalently, the survival function $l_{x+t}$ interpolates linearly between $l_x$ and $l_{x+1}$:

$$l_{x+t} = (1 - t) l_x + t l_{x+1} = l_x - t \cdot d_x \quad \text{for } 0 \le t \le 1$$

From this linear specification, the fractional death probability is directly proportional to duration $t$:
$${}_t q_x = \frac{l_x - l_{x+t}}{l_x} = \frac{t \cdot d_x}{l_x} = t \cdot q_x$$

For any sub-interval $[t, t + s]$ such that $0 \le t < t + s \le 1$, the conditional probability of survival is:
$${}_s p_{x+t} = \frac{l_{x+t+s}}{l_{x+t}} = \frac{l_x - (t + s) d_x}{l_x - t \cdot d_x} = \frac{1 - (t + s) q_x}{1 - t \cdot q_x} = 1 - \frac{s \cdot q_x}{1 - t \cdot q_x}$$

The instantaneous force of mortality under UDD is:
$$\mu_{x+t} = -\frac{1}{l_{x+t}} \frac{d}{dt} l_{x+t} = -\frac{1}{l_x - t \cdot d_x} (-d_x) = \frac{d_x}{l_x - t \cdot d_x} = \frac{q_x}{1 - t \cdot q_x}$$
Under UDD, $\mu_{x+t}$ is a strictly increasing function of $t \in [0, 1)$, accelerating toward the end of the year of age.

### 2. Constant Force of Mortality (CFM)
The **Constant Force of Mortality** assumption posits that the hazard rate remains strictly invariant throughout the integer age interval:
$$\mu_{x+t} = \mu \quad \text{for all } t \in [0, 1)$$

Since $p_x = \exp\left( -\int_0^1 \mu_{x+u}\,du \right) = e^{-\mu}$, we immediately obtain:
$$\mu = -\ln(p_x)$$
The fractional survival probability is:
$${}_t p_x = e^{-\mu t} = (e^{-\mu})^t = (p_x)^t$$
The fractional mortality probability is:
$${}_t q_x = 1 - (p_x)^t = 1 - (1 - q_x)^t$$
For any sub-interval, conditional survival depends only on elapsed duration $s$, exhibiting the memoryless property within the year:
$${}_s p_{x+t} = (p_x)^s$$
The constant force assumption provides exceptional computational convenience in continuous-time Markov multi-state modeling.

### 3. The Balducci Assumption (Hyperbolic Survival)
Historically formulated by Gaetano Balducci, this hypothesis assumes that the reciprocal of the survival function is linear in $t$:
$$\frac{1}{l_{x+t}} = \frac{1 - t}{l_x} + \frac{t}{l_{x+1}} \quad \text{for } 0 \le t \le 1$$
This yields the foundational operational identity:
$${}_{1 - t} q_{x+t} = (1 - t) q_x$$
The instantaneous force of mortality under the Balducci assumption is:
$$\mu_{x+t} = \frac{q_x}{1 - (1 - t) q_x}$$
Under Balducci, $\mu_{x+t}$ is a decreasing function of $t$, which is biologically counterintuitive for adult human populations but provided substantial algebraic simplifications in manual actuarial calculations prior to digital computing.

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Metric / Property</th>
<th>Uniform Distribution of Deaths (UDD)</th>
<th>Constant Force of Mortality (CFM)</th>
<th>Balducci Assumption</th>
</tr>
</thead>
<tbody>
<tr>
<td>Survival Curve $l_{x+t}$</td>
<td>Linear: $l_x - t \cdot d_x$</td>
<td>Exponential: $l_x (p_x)^t$</td>
<td>Hyperbolic: $[(1-t)/l_x + t/l_{x+1}]^{-1}$</td>
</tr>
<tr>
<td>Fractional Mortality ${}_t q_x$</td>
<td>$t \cdot q_x$</td>
<td>$1 - (p_x)^t$</td>
<td>$\frac{t \cdot q_x}{1 - (1-t)q_x}$</td>
</tr>
<tr>
<td>Force of Mortality $\mu_{x+t}$</td>
<td>$\frac{q_x}{1 - t \cdot q_x}$ (increasing)</td>
<td>$-\ln(p_x)$ (constant)</td>
<td>$\frac{q_x}{1 - (1-t)q_x}$ (decreasing)</td>
</tr>
<tr>
<td>Primary Application</td>
<td>Statutory life insurance reserving</td>
<td>Multi-state stochastic continuous models</td>
<td>Historical life table graduation</td>
</tr>
</tbody>
</table>
</div>

## 3.8 Stochastic Mortality Modeling: The Lee-Carter Framework

Classical life table construction assumes that age-specific mortality rates are static in time. However, the twentieth and twenty-first centuries have witnessed continuous secular declines in mortality rates across nearly all human populations—a phenomenon termed **longevity improvement**.

Annuity providers, pension sponsors, and social security programs face substantial **longevity risk**: the systematic financial risk that retirees survive significantly longer than anticipated by static baseline life tables. To quantify longevity risk, actuaries deploy stochastic mortality models.

### The Lee-Carter Formulation
In 1992, Ronald Lee and Lawrence Carter formulated the foundational stochastic model for forecasting age-specific central death rates $m_{x, t}$ at age $x$ in calendar year $t$:

$$\ln(m_{x, t}) = \alpha_x + \beta_x \kappa_t + \epsilon_{x, t}$$

where:
- $\alpha_x$: The baseline age-specific log-mortality profile, representing the long-term empirical average of $\ln(m_{x, t})$ across all observed years.
- $\kappa_t$: The time-varying latent mortality index, capturing overall macroeconomic and public health improvements over calendar years.
- $\beta_x$: The age-specific sensitivity coefficient, measuring the relative speed of mortality decline at age $x$ in response to unit changes in $\kappa_t$.
- $\epsilon_{x, t} \sim \mathcal{N}(0, \sigma_\epsilon^2)$: A Gaussian error disturbance reflecting idiosyncratic demographic fluctuations.

### Identification Constraints and Model Estimation
To ensure unique mathematical identification of the parameters, two normalization constraints are imposed:
$$\sum_{t=1}^T \kappa_t = 0 \quad \text{and} \quad \sum_{x=x_{\min}}^{x_{\max}} \beta_x = 1$$

Under these constraints:
$$\alpha_x = \frac{1}{T} \sum_{t=1}^T \ln(m_{x, t})$$
The parameters $\beta_x$ and $\kappa_t$ are obtained via **Singular Value Decomposition (SVD)** of the mean-centered log-mortality matrix $Z_{x, t} = \ln(m_{x, t}) - \alpha_x$:
$$Z = U \Sigma V^T$$
The first principal component yields $\beta_x$ from the first left singular vector $u_1$ and $\kappa_t$ from the first right singular vector $v_1$ scaled by singular value $\sigma_1$.

### Forecasting and Random Walk with Drift
Once $\kappa_t$ is estimated historically, it is modeled as an autoregressive integrated moving average process, specifically a **Random Walk with Drift**:
$$\kappa_t = \kappa_{t-1} + d + e_t, \quad e_t \sim \mathcal{N}(0, \sigma_e^2)$$
where $d = \frac{\kappa_T - \kappa_1}{T - 1} < 0$ is the empirical downward drift.

Extrapolating $\kappa_{t+h} = \kappa_t + h \cdot d$ into the future enables probabilistic forecasting of life expectancy, prospective annuity liability valuations, and stress-testing of defined benefit pension solvency under Solvency II.
"""

# --- UNIT 4 EXPANSION ---
u4_path = DRAFT_DIR / "unit-4.md"
u4_text = u4_path.read_text(encoding="utf-8")
u4_expansion = r"""
## 4.7 Continuous-Time Markov Multi-State Models and Kolmogorov Forward Equations

In modern life and health contingencies, individuals transition dynamically between multiple health states. Standard examples include:
1. **The Disability Income Model (Three States)**: State 0 (Active / Healthy), State 1 (Temporarily or Permanently Disabled), State 2 (Dead / Absorbing).
2. **Continuing Care Retirement Communities (CCRCs)**: Independent Living, Assisted Living, Skilled Nursing, and Death.

### 1. Transition Intensities and Chapman-Kolmogorov Equations
Let $S(t) \in \{0, 1, \dots, J\}$ denote the state occupied by a life aged $x$ at duration $t \ge 0$. The process is assumed to satisfy the continuous-time Markov property: the future transition probabilities depend solely on the current occupied state, independent of past state occupancy history.

The instantaneous **transition intensity** from state $i$ to state $j$ ($i \ne j$) at age $x + t$ is:
$$\mu_{x+t}^{ij} = \lim_{h \to 0^+} \frac{P(S(t + h) = j \mid S(t) = i)}{h}$$
The total exit intensity leaving state $i$ is:
$$\mu_{x+t}^{i \bullet} = \sum_{j \ne i} \mu_{x+t}^{ij}$$

Let $p_{x}^{ij}(s, t) = P(S(t) = j \mid S(s) = i)$ denote the transition probability from state $i$ at duration $s$ to state $j$ at duration $t$ ($s \le t$). By the law of total probability, the transition matrix satisfies the **Chapman-Kolmogorov Equation**:
$$p_{x}^{ik}(s, t) = \sum_{j=0}^J p_{x}^{ij}(s, u) \cdot p_{x}^{jk}(u, t) \quad \text{for any } u \in [s, t]$$

### 2. The Kolmogorov Forward Differential Equations
Differentiating $p_{x}^{ij}(s, t)$ with respect to terminal duration $t$ yields the system of **Kolmogorov Forward Differential Equations**:

$$\frac{\partial}{\partial t} p_{x}^{ij}(s, t) = \sum_{k \ne j} p_{x}^{ik}(s, t) \mu_{x+t}^{kj} - p_{x}^{ij}(s, t) \mu_{x+t}^{j \bullet}$$

In matrix notation, letting $\mathbf{P}(s, t) = [p_{x}^{ij}(s, t)]$ and defining the transition rate generator matrix $\mathbf{Q}(t)$ with off-diagonal entries $q_{ij}(t) = \mu_{x+t}^{ij}$ and diagonal entries $q_{ii}(t) = -\mu_{x+t}^{i \bullet}$:
$$\frac{\partial}{\partial t} \mathbf{P}(s, t) = \mathbf{P}(s, t) \mathbf{Q}(t)$$
Subject to the initial condition $\mathbf{P}(s, s) = \mathbf{I}$ (the identity matrix).

Solving this coupled system of linear ordinary differential equations numerically (using Runge-Kutta fourth-order integration) permits exact valuation of complex health insurance riders, disability waiver-of-premium benefits, and critical illness policies.

## 4.8 Dependent Decrement Mechanics and Uniform Distribution of Decrements

In multiple decrement theory, an individual aged $x$ can exit an active status due to $m$ competing causes of decrement (such as death, disability, voluntary withdrawal, or retirement). Actuaries must distinguish between:
1. **The Multiple Decrement Table (Dependent Rates)**: Where all causes operate simultaneously in the real insured population, yielding observed decrement probabilities $q_x^{(j)}$.
2. **Associated Single Decrement Tables (Independent Rates)**: Theoretical probabilities $q_x^{\prime (j)}$ reflecting the rate at which cause $j$ would operate if all other $m - 1$ competing causes were completely eliminated.

### 1. The Fundamental Integral Relations
The dependent probability of exiting due to cause $j$ over the unit age interval is:
$$q_x^{(j)} = \int_0^1 {}_t p_x^{(\tau)} \mu_{x+t}^{(j)}\,dt$$
where the total survival probability under all decrements combined is:
$${}_t p_x^{(\tau)} = \exp\left( -\int_0^t \sum_{k=1}^m \mu_{x+u}^{(k)}\,du \right) = \prod_{k=1}^m {}_t p_x^{\prime (k)}$$
assuming decrements act independently.

The independent single decrement probability is:
$$q_x^{\prime (j)} = 1 - p_x^{\prime (j)} = 1 - \exp\left( -\int_0^1 \mu_{x+t}^{(j)}\,dt \right)$$

### 2. Conversions under Uniform Distribution of Decrements
When converting between dependent probabilities $q_x^{(j)}$ and independent probabilities $q_x^{\prime (j)}$, actuaries invoke fractional distribution assumptions.

**Assumption A: Uniform Distribution of Decrements in the Multiple Decrement Table**:
Assume that in the combined table, exits from each cause $j$ occur uniformly across the year:
$${}_t q_x^{(j)} = t \cdot q_x^{(j)} \implies \frac{d}{dt} {}_t q_x^{(j)} = {}_t p_x^{(\tau)} \mu_{x+t}^{(j)} = q_x^{(j)}$$
Under this condition, the independent rate for cause 1 in a two-decrement model is given exactly by:
$$q_x^{\prime (1)} = 1 - (1 - q_x^{(\tau)})^{\frac{q_x^{(1)}}{q_x^{(\tau)}}}$$
if forces of decrement are proportional, or by the standard binomial approximation:
$$q_x^{\prime (1)} \approx \frac{q_x^{(1)}}{1 - \frac{1}{2} q_x^{(2)}}$$
*Actuarial Interpretation*: An individual who exits due to cause 2 is exposed to cause 1 for an average of half a year ($1/2$). Therefore, the effective exposure base for cause 1 is reduced by $\frac{1}{2} q_x^{(2)}$, requiring the dependent rate $q_x^{(1)}$ to be inflated by $1 / (1 - \frac{1}{2} q_x^{(2)})$ to recover the true net rate $q_x^{\prime (1)}$.

**Assumption B: Uniform Distribution of Decrements in Each Associated Single Decrement Table**:
If each independent decrement $j$ is uniformly distributed in its own single decrement table (${}_t q_x^{\prime (j)} = t \cdot q_x^{\prime (j)}$), the exact dependent rate in a two-decrement model is:
$$q_x^{(1)} = q_x^{\prime (1)} \left( 1 - \frac{1}{2} q_x^{\prime (2)} \right)$$
$$q_x^{(2)} = q_x^{\prime (2)} \left( 1 - \frac{1}{2} q_x^{\prime (1)} \right)$$
These conversion identities ensure mathematical consistency when building pension actuarial valuation software from separate mortality, disability, and employee turnover studies.
"""

# --- UNIT 5 EXPANSION ---
u5_path = DRAFT_DIR / "unit-5.md"
u5_text = u5_path.read_text(encoding="utf-8")
u5_expansion = r"""
## 5.7 Continuous Renewal Theory: Analytical Solution of Lotka's Equation

In Section 5.3, we presented Lotka's continuous renewal equation governing the total annual births $B(t)$ in a closed female population:
$$B(t) = G(t) + \int_0^t B(t - x) \ell(x) m(x)\,dx$$
where $G(t)$ represents births contributed by females already alive at time $t = 0$, $\ell(x) = {}_x p_0$ is the survival probability from birth to age $x$, and $m(x)$ is the maternity (fertility) function at age $x$.

For calendar times $t$ exceeding the maximum reproductive lifespan $\beta$ ($\approx 50$ years), all females born before $t = 0$ have completed childbearing, so $G(t) \equiv 0$. The renewal equation becomes the homogeneous Volterra integral equation of the second kind:
$$B(t) = \int_\alpha^\beta B(t - x) \phi(x)\,dx$$
where $\phi(x) = \ell(x) m(x)$ is the **net maternity function**, non-zero only over the reproductive age span $[\alpha, \beta]$.

### 1. The Characteristic Root Equation
We trial an exponential trial solution of the form $B(t) = C e^{rt}$. Substituting into the homogeneous integral equation yields:
$$C e^{rt} = \int_\alpha^\beta C e^{r(t - x)} \phi(x)\,dx = C e^{rt} \int_\alpha^\beta e^{-rx} \phi(x)\,dx$$
Dividing by $C e^{rt} \ne 0$ gives the celebrated **Lotka Characteristic Equation**:
$$\Psi(r) = \int_\alpha^\beta e^{-rx} \phi(x)\,dx = 1$$

Let $\Psi(r) = \int_\alpha^\beta e^{-rx} \ell(x) m(x)\,dx$. We evaluate its analytical properties:
1. Since $\phi(x) \ge 0$ for all $x \in [\alpha, \beta]$, $\Psi(r)$ is a strictly monotonically decreasing continuous function of real $r$:
   $$\frac{d\Psi}{dr} = -\int_\alpha^\beta x e^{-rx} \phi(x)\,dx < 0$$
2. As $r \to -\infty$, $\Psi(r) \to \infty$; as $r \to \infty$, $\Psi(r) \to 0$.
3. By the Intermediate Value Theorem, there exists **one and only one real root** $r_0 \in \mathbb{R}$ satisfying $\Psi(r_0) = 1$.
4. This unique real root $r_0$ is the **intrinsic rate of natural increase**. Furthermore, for any complex root $r_k = u_k + i v_k$ ($v_k \ne 0$), the real part satisfies:
   $$1 = \left| \int_\alpha^\beta e^{-(u_k + i v_k)x} \phi(x)\,dx \right| < \int_\alpha^\beta e^{-u_k x} \phi(x)\,dx = \Psi(u_k) \implies u_k < r_0$$
The unique real root $r_0$ strictly dominates the real parts of all complex conjugate roots ($u_k < r_0$). Consequently, as $t \to \infty$, all oscillatory complex terms $e^{u_k t} \cos(v_k t)$ decay exponentially relative to $e^{r_0 t}$, proving that the birth stream asymptotically converges to pure exponential growth:
$$B(t) \sim C_0 e^{r_0 t} \quad \text{as } t \to \infty$$

### 2. Cumulant Expansion of the Net Maternity Function
To compute $r_0$ analytically without numerical integration, Alfred Lotka expanded $e^{-rx}$ in a Taylor series about the mean length of a generation $T$:
$$\int_\alpha^\beta e^{-rx} \phi(x)\,dx \approx R_0 \exp\left( -r T + \frac{1}{2} r^2 \sigma^2 \right) = 1$$
Taking natural logarithms yields the quadratic approximation for the intrinsic rate $r_0$:
$$\ln(R_0) - r_0 T + \frac{1}{2} r_0^2 \sigma^2 = 0 \implies r_0 \approx \frac{\ln(R_0)}{T} + \frac{\sigma^2 [\ln(R_0)]^2}{2 T^3}$$
where:
- $R_0 = \int_\alpha^\beta \phi(x)\,dx$ is the Net Reproduction Rate.
- $T = \frac{1}{R_0} \int_\alpha^\beta x \phi(x)\,dx$ is the mean age of childbearing in the stationary population.
- $\sigma^2 = \frac{1}{R_0} \int_\alpha^\beta (x - T)^2 \phi(x)\,dx$ is the variance of the net maternity age distribution.
This elegant formula reveals that if $R_0 = 1$, $r_0 = 0$; if $R_0 > 1$, $r_0 > 0$; and if $R_0 < 1$, $r_0 < 0$.

## 5.8 Spectral Analysis of the Leslie Matrix and Fisher's Reproductive Value

In demographic projection, the discrete population vector $\mathbf{n}_t = [n_{0, t}, n_{1, t}, \dots, n_{k, t}]^T$ evolves according to the linear difference system:
$$\mathbf{n}_{t+1} = \mathbf{L} \mathbf{n}_t$$
where $\mathbf{L}$ is the $(k+1) \times (k+1)$ **Leslie Matrix**:
$$\mathbf{L} = \begin{pmatrix}
F_0 & F_1 & F_2 & \dots & F_{k-1} & F_k \\
P_0 & 0 & 0 & \dots & 0 & 0 \\
0 & P_1 & 0 & \dots & 0 & 0 \\
\vdots & \vdots & \ddots & \dots & \vdots & \vdots \\
0 & 0 & \dots & P_{k-1} & 0
\end{pmatrix}$$

### 1. The Perron-Frobenius Theorem in Demography
Because fertility rates $F_i \ge 0$ and survival probabilities $P_i \in (0, 1)$, $\mathbf{L}$ is a non-negative square matrix. If there are at least two consecutive reproductive age classes with non-zero fertility ($\gcd(\{i : F_i > 0\}) = 1$), the Leslie matrix $\mathbf{L}$ is **primitive** (irreducible and aperiodic).

By the celebrated **Perron-Frobenius Theorem**:
1. $\mathbf{L}$ possesses a unique, strictly positive, real dominant eigenvalue $\lambda_1 > 0$ such that for any other eigenvalue $\lambda_j$ ($j \ne 1$):
   $$\lambda_1 > |\lambda_j|$$
2. Associated with $\lambda_1$, there exists a unique right eigenvector $\mathbf{u} > \mathbf{0}$ satisfying:
   $$\mathbf{L} \mathbf{u} = \lambda_1 \mathbf{u}$$
   This eigenvector $\mathbf{u}$ defines the unique asymptotic **Stable Age Distribution**.
3. Associated with $\lambda_1$, there exists a unique left eigenvector $\mathbf{v}^T > \mathbf{0}$ satisfying:
   $$\mathbf{v}^T \mathbf{L} = \lambda_1 \mathbf{v}^T$$
   This left eigenvector $\mathbf{v}$ defines **Fisher's Reproductive Value**.

### 2. Fisher's Reproductive Value Formula
Sir Ronald Fisher defined the reproductive value $v_x$ of a female aged $x$ as her relative expected contribution to all future population births, discounted by the intrinsic growth rate $\lambda_1$:

$$v_x = \frac{\lambda_1^x}{\ell(x)} \sum_{y=x}^\beta \lambda_1^{-(y+1)} \ell(y) F_y$$
Normalizing $v_0 = 1$ (the reproductive value of a newborn):
- $v_x$ begins at $1$ at birth.
- $v_x$ rises steeply during pre-reproductive youth as the individual survives childhood mortality without expending reproductive capacity, reaching a global maximum at the peak of reproductive onset ($x \approx 18 - 22$).
- Beyond peak childbearing, $v_x$ declines monotonically, reaching identically zero at menopause ($x \ge \beta$).

The long-run asymptotic trajectory of the population under repeated projection is given explicitly by spectral decomposition:
$$\mathbf{n}_t = \mathbf{L}^t \mathbf{n}_0 = \lambda_1^t \frac{\mathbf{v}^T \mathbf{n}_0}{\mathbf{v}^T \mathbf{u}} \mathbf{u} + \mathcal{O}(|\lambda_2|^t)$$
The scalar quantity $\mathbf{v}^T \mathbf{n}_0$ represents the total reproductive capital of the initial population. This profound result guarantees that regardless of the initial age distribution $\mathbf{n}_0$, the population structure inevitably converges to the stable vector $\mathbf{u}$, confirming the **Strong Ergodic Theorem of Demography**.
"""

# --- UNIT 6 EXPANSION ---
u6_path = DRAFT_DIR / "unit-6.md"
u6_text = u6_path.read_text(encoding="utf-8")
u6_expansion = r"""
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
"""

# --- UNIT 7 EXPANSION ---
u7_path = DRAFT_DIR / "unit-7.md"
u7_text = u7_path.read_text(encoding="utf-8")
u7_expansion = r"""
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
"""

# --- UNIT 8 EXPANSION ---
u8_path = DRAFT_DIR / "unit-8.md"
u8_text = u8_path.read_text(encoding="utf-8")
u8_expansion = r"""
## 8.7 Recursive Aggregate Claims Computation: The Panjer Algorithm

In Section 8.1, the aggregate claims random variable was defined as the random sum:
$$S = \sum_{i=1}^N X_i$$
where $N$ is the annual claim frequency random variable and $\{X_i\}_{i=1}^\infty$ are independent, identically distributed positive claim severity random variables with probability distribution $f_X(x) = P(X = x)$ for discrete claim sizes $x \in \{1, 2, \dots, m\}$.

Calculating the probability mass function of aggregate claims $g_k = P(S = k)$ via direct multi-fold convolutions requires $\mathcal{O}(k^2)$ operations per fold, becoming computationally intractable when $N$ can assume hundreds or thousands of claims. In 1981, Harry Panjer introduced a revolutionary recursive formula that computes the exact distribution of $S$ in linear time $\mathcal{O}(k)$.

### 1. The Panjer $(a, b, 0)$ Class of Frequency Distributions
Panjer identified that the primary counting distributions in actuarial risk theory satisfy a common linear recursive relation:

$$p_n = P(N = n) = \left( a + \frac{b}{n} \right) p_{n-1} \quad \text{for } n = 1, 2, 3, \dots$$

The distributions satisfying this relation form the **Panjer $(a, b, 0)$ Class**:
1. **Poisson($\lambda$)**: $a = 0, \; b = \lambda, \; p_0 = e^{-\lambda}$.
2. **Binomial($m, p$)**: $a = -\frac{p}{1-p}, \; b = \frac{(m+1)p}{1-p}, \; p_0 = (1-p)^m$.
3. **Negative Binomial($r, p$)**: $a = 1 - p, \; b = (r-1)(1-p), \; p_0 = p^r$.
4. **Geometric($p$)**: Special case of Negative Binomial with $r = 1$: $a = 1 - p, \; b = 0$.

### 2. Statement and Proof of the Panjer Recursion
Let $N$ belong to the $(a, b, 0)$ class, and let severity $X$ take values on the positive integers $\{1, 2, \dots\}$ with $f_j = P(X = j)$. The aggregate claims distribution $g_k = P(S = k)$ satisfies:

$$g_0 = P(S = 0) = P(N = 0) = p_0$$
$$g_k = \frac{1}{1 - a f_0} \sum_{j=1}^k \left( a + \frac{b \cdot j}{k} \right) f_j \cdot g_{k - j} \quad \text{for } k = 1, 2, 3, \dots$$
When severity is strictly positive ($f_0 = P(X = 0) = 0$), the leading factor $1 - a f_0 = 1$.

*Mathematical Derivation*:
The probability generating function of $S$ is $G_S(z) = G_N(G_X(z))$.
From the definition of the $(a, b, 0)$ class:
$$G_N'(z) = \sum_{n=1}^\infty n p_n z^{n-1} = \sum_{n=1}^\infty (a n + b) p_{n-1} z^{n-1} = a z G_N'(z) + (a + b) G_N(z)$$
Differentiating $G_S(z) = G_N(G_X(z))$ with respect to $z$:
$$G_S'(z) = G_N'(G_X(z)) \cdot G_X'(z)$$
Substituting $G_N'(G_X(z)) = \frac{a + b}{1 - a G_X(z)} G_N(G_X(z))$ and equating coefficient series powers of $z^{k-1}$ produces the exact Panjer recursive identity.

Because each term $g_k$ depends only on previously computed values $\{g_0, g_1, \dots, g_{k-1}\}$, the entire probability distribution of aggregate claims can be generated in a single sequential sweep, enabling real-time pricing of aggregate stop-loss reinsurance contracts.

## 8.8 The Cramér-Lundberg Ruin Model: Exact Integro-Differential Equation

In classical continuous-time ruin theory, the insurer's surplus process $\{U(t)\}_{t \ge 0}$ evolves according to:
$$U(t) = u + c t - \sum_{i=1}^{N(t)} X_i$$
where:
- $u = U(0) \ge 0$ is the initial surplus capital.
- $c > 0$ is the continuous premium collection rate per unit time.
- $N(t)$ is a homogeneous Poisson process with claim arrival intensity $\lambda > 0$.
- $X_i$ are independent, identically distributed positive claim amounts with cumulative distribution function $F_X(x)$ and mean $\mu_X = \mathbb{E}[X] < \infty$.

The continuous premium collection rate includes a safety loading $\theta > 0$:
$$c = (1 + \theta) \lambda \mu_X$$
If $\theta \le 0$, ruin occurs with probability $1.0$ as $t \to \infty$ by the Strong Law of Large Numbers. Thus, the positive safety loading condition $\theta > 0$ is strictly required for long-term survival.

### 1. The Probability of Ruin
Let $T = \inf\{t > 0 : U(t) < 0\}$ denote the time of ruin (with $T = \infty$ if $U(t) \ge 0$ for all $t \ge 0$).
The ultimate ruin probability regarded as a function of initial capital $u$ is:
$$\psi(u) = P(T < \infty \mid U(0) = u)$$
The non-ruin (survival) probability is $\phi(u) = 1 - \psi(u)$.

### 2. Derivation of the Integro-Differential Equation
Consider a minuscule elapsed time interval $h > 0$. During $[0, h]$:
- With probability $1 - \lambda h + o(h)$, no claims occur, and the surplus grows deterministically to $u + c h$.
- With probability $\lambda h + o(h)$, exactly one claim of size $X$ occurs.
- The probability of two or more claims is $o(h)$.

By conditioning on the events occurring during $[0, h]$:
$$\psi(u) = (1 - \lambda h) \psi(u + c h) + \lambda h \left[ \int_0^u \psi(u + c h - x) dF_X(x) + \int_u^\infty 1 \cdot dF_X(x) \right] + o(h)$$
Rearranging terms, dividing by $c h$, and taking the limit as $h \to 0^+$:

$$\psi'(u) = \frac{\lambda}{c} \psi(u) - \frac{\lambda}{c} \int_0^u \psi(u - x) dF_X(x) - \frac{\lambda}{c} [1 - F_X(u)]$$

This is the celebrated **Integro-Differential Equation of Ruin Theory**.

### 3. Exact Solution for Exponential Claims
When individual claim severities are exponentially distributed with parameter $\alpha > 0$ ($f_X(x) = \alpha e^{-\alpha x}$ for $x > 0$), so that $\mu_X = 1/\alpha$, the integro-differential equation can be solved in closed analytical form.

Differentiating the equation and substituting the exponential density reduces the integro-differential equation to a second-order linear ordinary differential equation with constant coefficients:
$$\psi''(u) + \left( \alpha - \frac{\lambda}{c} \right) \psi'(u) = 0$$

Using the boundary conditions:
1. $\lim_{u \to \infty} \psi(u) = 0$ (infinite capital eliminates ruin).
2. Initial surplus condition at $u = 0$: $\psi(0) = \frac{\lambda}{c \alpha} = \frac{\lambda \mu_X}{(1 + \theta) \lambda \mu_X} = \frac{1}{1 + \theta}$.

The exact closed-form solution for the ultimate ruin probability is:

$$\psi(u) = \frac{1}{1 + \theta} \exp\left( -\frac{\theta \alpha}{1 + \theta} u \right)$$

This analytical result demonstrates that:
- Even with zero initial capital ($u = 0$), the insurer has a survival probability of $\phi(0) = 1 - \frac{1}{1 + \theta} = \frac{\theta}{1 + \theta} > 0$.
- The probability of ruin decays exponentially fast with respect to initial capital $u$, where the exponential decay parameter $R = \frac{\theta \alpha}{1 + \theta}$ is the exact Lundberg adjustment coefficient.
"""

expansions = [
    (1, u1_path, u1_text, u1_expansion),
    (2, u2_path, u2_text, u2_expansion),
    (3, u3_path, u3_text, u3_expansion),
    (4, u4_path, u4_text, u4_expansion),
    (5, u5_path, u5_text, u5_expansion),
    (6, u6_path, u6_text, u6_expansion),
    (7, u7_path, u7_text, u7_expansion),
    (8, u8_path, u8_text, u8_expansion),
]

for unit_num, path, text, add in expansions:
    marker = "## Fully worked question 1:"
    idx = text.find(marker)
    if idx == -1:
        print(f"Warning: Marker not found in unit {unit_num}!")
        continue
    new_text = text[:idx] + add.strip() + "\n\n" + text[idx:]
    path.write_text(new_text, encoding="utf-8")
    print(f"Unit {unit_num} expanded successfully.")

print("All units expanded.")
