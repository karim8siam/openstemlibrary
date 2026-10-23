#!/usr/bin/env python3
"""
Final expansion script for Actuarial Statistics and Mathematical Demography
to bring the book draft well beyond 25,000 substantive prose words across all 8 units.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"

# --- UNIT 1 FINAL ADDITION ---
u1_path = DRAFT_DIR / "unit-1.md"
u1_text = u1_path.read_text(encoding="utf-8")
u1_add = r"""
## 1.13 Inflation-Adjusted Returns and the Fisher Hypothesis

In long-term actuarial financial engineering—particularly in defined benefit pension valuation, long-tail casualty reserving, and index-linked lifetime annuities—cash flow projections spanning several decades are heavily exposed to purchasing power erosion caused by monetary inflation.

### 1. The Classical and Continuous Fisher Relation
Irving Fisher formulated the fundamental relationship between the nominal interest rate $i$, the real interest rate $r$, and the expected rate of inflation $\pi$.

Over a discrete annual horizon, one monetary unit invested at nominal rate $i$ accumulates to $1 + i$. Deflating this terminal nominal amount by the general price index inflation factor $(1 + \pi)$ yields the real purchasing power accumulation:

$$1 + r = \frac{1 + i}{1 + \pi} \iff 1 + i = (1 + r)(1 + \pi) = 1 + r + \pi + r \pi$$

Solving for the nominal interest rate:

$$i = r + \pi + r \pi$$

In introductory economic theory, the cross-product term $r \pi$ is frequently omitted as negligible for small rates, yielding the familiar linear approximation:
$$i \approx r + \pi$$
However, in institutional actuarial reserving and high-inflation regimes, the interaction term $r \pi$ represents a substantial compounding effect that cannot be discarded.

Under continuous compounding, where $\delta$ is the nominal continuous force of interest, $\delta_r$ is the real continuous force of interest, and $\delta_\pi$ is the continuous force of inflation:
$$e^\delta = e^{\delta_r} \cdot e^{\delta_\pi} = e^{\delta_r + \delta_\pi}$$
Taking the natural logarithm:

$$\delta = \delta_r + \delta_\pi$$
In continuous time, the Fisher relation holds with exact linear additivity without any approximation error.

### 2. Treasury Inflation-Protected Securities (TIPS) and Break-Even Inflation
Sovereign governments issue inflation-indexed bonds, such as United States Treasury Inflation-Protected Securities (TIPS) and United Kingdom Index-Linked Gilts.

In a TIPS bond:
- The principal (par value) of the bond adjusts continuously in direct proportion to the Consumer Price Index (CPI):
  $$C(t) = C_0 \cdot \frac{\text{CPI}(t)}{\text{CPI}(0)}$$
- The periodic coupon payments are calculated by multiplying the fixed real coupon rate $g_{\text{real}}$ by the inflation-adjusted principal:
  $$\text{Coupon}(t) = g_{\text{real}} \cdot C(t)$$
- At maturity, the investor receives the maximum of the inflation-adjusted principal or the original par value ($\max(C(n), C_0)$), providing an asymmetric deflation floor.

The **Break-Even Inflation Rate (BEIR)** is defined as the difference between the nominal yield on a standard conventional sovereign bond $y_{\text{nom}}(t)$ and the real yield on an inflation-indexed bond $y_{\text{real}}(t)$ of identical maturity $t$:

$$\text{BEIR}(t) = y_{\text{nom}}(t) - y_{\text{real}}(t)$$

The break-even inflation rate decomposes into expected future inflation plus an inflation risk premium demanded by risk-averse investors to bear inflation uncertainty:
$$\text{BEIR}(t) = \mathbb{E}[\pi(t)] + \text{RP}_\pi(t)$$
Actuaries extract break-even inflation curves directly from market quotes to price inflation-indexed annuities and calibrate cost-of-living adjustments (COLA) for corporate retirement plans.
"""

# --- UNIT 2 FINAL ADDITION ---
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")
u2_add = r"""
## 2.12 Continuous Escalation and Geometric Perpetuities in Corporate Valuation

In corporate valuation, equity research, and actuarial appraisal of insurance companies, analysts must project and discount cash flow streams that expand indefinitely at a compound growth rate $g$.

### 1. Discrete Geometrically Growing Annuity and Perpetuity
Let an annuity pay cash flows at the end of each year for $n$ years, where the first payment is $C$, and each subsequent payment increases at constant growth rate $g$. The cash flows are:
- Year 1: $C$
- Year 2: $C(1 + g)$
- Year $k$: $C(1 + g)^{k-1}$

The present value at effective discount rate $i$ (with $i \ne g$) is:

$$PV = \sum_{k=1}^n C(1 + g)^{k-1} (1 + i)^{-k} = \frac{C}{1 + g} \sum_{k=1}^n \left( \frac{1 + g}{1 + i} \right)^k$$

Define an adjusted interest rate $j$ satisfying:
$$\frac{1}{1 + j} = \frac{1 + g}{1 + i} \implies 1 + j = \frac{1 + i}{1 + g} \implies j = \frac{i - g}{1 + g}$$

Substituting $j$ into the summation reduces the geometrically growing annuity to a standard level annuity evaluated at rate $j$:

$$PV = \frac{C}{1 + g} \cdot a_{\overline{n}|j} = C \left[ \frac{1 - \left( \frac{1 + g}{1 + i} \right)^n}{i - g} \right]$$

When $n \to \infty$ and $i > g$, the growth factor $\left( \frac{1 + g}{1 + i} \right)^n \to 0$. The present value converges to the celebrated **Gordon Growth Model Perpetuity**:

$$PV_\infty = \frac{C}{i - g}$$

If $i \le g$, the series diverges to infinity, demonstrating that no finite asset can sustain a risk-free perpetual growth rate exceeding the market discount rate.

### 2. Continuous Cash Flows with Continuous Exponential Growth
Consider a continuous payment stream paid at the instantaneous rate $\rho(t) = \rho_0 e^{\gamma t}$ over the time interval $[0, n]$, discounted at continuous force of interest $\delta$:

$$PV = \int_0^n \rho_0 e^{\gamma t} e^{-\delta t}\,dt = \rho_0 \int_0^n e^{-(\delta - \gamma)t}\,dt$$

For $\delta \ne \gamma$:
$$PV = \rho_0 \left[ -\frac{e^{-(\delta - \gamma)t}}{\delta - \gamma} \right]_0^n = \rho_0 \left( \frac{1 - e^{-(\delta - \gamma)n}}{\delta - \gamma} \right) = \rho_0 \cdot \bar{a}_{\overline{n}|(\delta - \gamma)}$$

If the continuous payment flows perpetually ($n \to \infty$) and $\delta > \gamma$:
$$PV_\infty = \frac{\rho_0}{\delta - \gamma}$$
This continuous formulation serves as the mathematical engine for valuing royalties, mineral rights extraction leases, and continuous life reinsurance expense allowances.
"""

# --- UNIT 3 FINAL ADDITION ---
u3_path = DRAFT_DIR / "unit-3.md"
u3_text = u3_path.read_text(encoding="utf-8")
u3_add = r"""
## 3.9 Analytical Life Table Graduation: Whittaker-Henderson Smoothing

Raw demographic data collected from national censuses or life insurer claim files generate crude mortality rates $\hat{q}_x = d_x / l_x$. Because of finite sample sizes, these crude rates exhibit random sampling noise, violating the biological expectation that adult human mortality rates must form a smooth, monotonically accelerating progression with age.

The process of converting irregular empirical rates into a smooth, coherent mathematical progression suitable for statutory life insurance pricing is termed **Graduation**.

### 1. The Whittaker-Henderson Type B Framework
Formulated by E. T. Whittaker in 1923 and extended by Robert Henderson, Whittaker-Henderson graduation treats smoothing as an explicit optimization problem balancing two competing objectives:
1. **Fit (Fidelity to Data)**: The graduated rates $u_x$ should adhere closely to the observed crude rates $v_x = \hat{q}_x$, weighted by sample exposure $w_x$:
   $$F = \sum_{x=1}^m w_x (u_x - v_x)^2$$
2. **Smoothness**: The $z$-th order differences $\Delta^z u_x$ of the graduated sequence should be minimized to suppress erratic oscillations:
   $$S = \sum_{x=1}^{m - z} (\Delta^z u_x)^2$$
   Typically, actuaries select $z = 3$, enforcing smoothness in the third differences ($\Delta^3 u_x \approx 0$), which aligns with quadratic polynomials.

The graduated sequence $\mathbf{u} = [u_1, u_2, \dots, u_m]^T$ is determined by minimizing the penalized loss function:

$$M(\mathbf{u}) = F + h \cdot S = \sum_{x=1}^m w_x (u_x - v_x)^2 + h \sum_{x=1}^{m - z} (\Delta^z u_x)^2$$

where $h > 0$ is the smoothing parameter:
- As $h \to 0$, $M \to F$, and the graduated rates collapse to the raw, unsmoothed crude rates ($u_x = v_x$).
- As $h \to \infty$, $S \to 0$, forcing the graduated sequence into a pure polynomial of degree $z - 1$ regardless of the underlying data.

### 2. Matrix Formulation and System Solution
In matrix notation, let $\mathbf{W} = \text{diag}(w_1, w_2, \dots, w_m)$ be the diagonal weight matrix, and let $\mathbf{K}$ be the $(m - z) \times m$ difference operator matrix representing $\Delta^z$. The loss function is:

$$M(\mathbf{u}) = (\mathbf{u} - \mathbf{v})^T \mathbf{W} (\mathbf{u} - \mathbf{v}) + h \cdot \mathbf{u}^T \mathbf{K}^T \mathbf{K} \mathbf{u}$$

Taking the gradient with respect to vector $\mathbf{u}$ and setting it to zero:
$$\nabla_\mathbf{u} M = 2 \mathbf{W} (\mathbf{u} - \mathbf{v}) + 2 h \mathbf{K}^T \mathbf{K} \mathbf{u} = \mathbf{0}$$
$$(\mathbf{W} + h \mathbf{K}^T \mathbf{K}) \mathbf{u} = \mathbf{W} \mathbf{v}$$

The optimal graduated mortality rates are given by the linear system:

$$\mathbf{u} = (\mathbf{W} + h \mathbf{K}^T \mathbf{K})^{-1} \mathbf{W} \mathbf{v}$$

Because $\mathbf{K}^T \mathbf{K}$ is banded with bandwidth $2z + 1$ (septadiagonal for $z = 3$), the system can be solved efficiently via Cholesky decomposition in $\mathcal{O}(m)$ operations without inverting dense matrices.
"""

# --- UNIT 4 FINAL ADDITION ---
u4_path = DRAFT_DIR / "unit-4.md"
u4_text = u4_path.read_text(encoding="utf-8")
u4_add = r"""
## 4.9 Joint Life Modeling with Copulas and Common Shock Models

Classical joint life actuarial mathematics assumes that the future lifetime random variables $T_x$ and $T_y$ of two spouses are mutually independent:
$$P(T_x > t, T_y > s) = P(T_x > t) \cdot P(T_y > s) = {}_t p_x \cdot {}_s p_y$$

In empirical demographic reality, spouses share common socioeconomic environments, dietary habits, infectious disease exposures, and psychological distress. Empirical studies document two pronounced phenomena:
1. **Positive Lifetime Association**: Long-term married couples exhibit significant positive correlation in life expectancy ($\rho(T_x, T_y) > 0$).
2. **The Broken-Heart Phenomenon (Bereavement Effect)**: Upon the death of one spouse, the surviving spouse experiences an acute spike in mortality hazard rate $\mu$, particularly during the first six to twelve months of widowhood.

### 1. Common Shock Models
The simplest structural method to introduce positive mortality dependence is the **Marshall-Olkin Common Shock Model**.

Let each individual's death be driven by independent idiosyncratic fatal shocks plus a simultaneous common shock:
- Individual $(x)$ is subject to an idiosyncratic Poisson shock process with hazard intensity $\lambda_1$.
- Individual $(y)$ is subject to an idiosyncratic Poisson shock process with hazard intensity $\lambda_2$.
- Both individuals are jointly exposed to an environmental common shock process (e.g., motor vehicle crash, natural catastrophe, toxic exposure) with hazard intensity $\lambda_{12}$.

The individual total mortality forces are:
$$\mu_x = \lambda_1 + \lambda_{12}, \quad \mu_y = \lambda_2 + \lambda_{12}$$

The joint survival function is:

$$S(t, s) = P(T_x > t, T_y > s) = \exp\left( -\lambda_1 t - \lambda_2 s - \lambda_{12} \max(t, s) \right)$$

For equal durations ($t = s$):
$$S(t, t) = \exp\left( -(\lambda_1 + \lambda_2 + \lambda_{12}) t \right) = \exp\left( -(\mu_x + \mu_y - \lambda_{12}) t \right)$$

Under independence ($\lambda_{12} = 0$), $S(t, t) = e^{-(\mu_x + \mu_y)t}$. Because $\lambda_{12} > 0$, the probability that both spouses survive simultaneously is strictly higher than predicted by the independence model!

### 2. Archimedean Copula Framework
By **Sklar's Theorem**, any multivariate joint survival function $S(t, s)$ can be uniquely decomposed into its marginal survival functions $S_X(t) = {}_t p_x$ and $S_Y(s) = {}_s p_y$ via a survival copula $C(u, v)$:

$$S(t, s) = C(S_X(t), S_Y(s))$$

A widely utilized parametric copula in actuarial science is the **Clayton Copula**:
$$C_\theta(u, v) = \left( u^{-\theta} + v^{-\theta} - 1 \right)^{-1/\theta}, \quad \theta > 0$$
where $\theta$ measures the degree of lower tail dependence. As $\theta \to 0$, $C_\theta(u, v) \to u \cdot v$ (independence).

Another primary family is the **Frank Copula**:
$$C_\alpha(u, v) = -\frac{1}{\alpha} \ln\left( 1 + \frac{(e^{-\alpha u} - 1)(e^{-\alpha v} - 1)}{e^{-\alpha} - 1} \right), \quad \alpha \ne 0$$
which exhibits symmetric dependence and captures married couple survival patterns with exceptional empirical fidelity. Incorporating copula dependence prevents life insurers from mispricing joint life and last survivor annuities.
"""

# --- UNIT 5 FINAL ADDITION ---
u5_path = DRAFT_DIR / "unit-5.md"
u5_text = u5_path.read_text(encoding="utf-8")
u5_add = r"""
## 5.9 Demographic Momentum and Age-Structural Inertia

A fundamental paradox of twentieth-century population dynamics is **Demographic Momentum**: even if the fertility rate of a developing nation immediately drops to the exact replacement level ($NRR = 1.0$) overnight, the total population size continues to expand substantially for several decades before eventually stabilizing.

This structural inertia occurs because past periods of high fertility generate a disproportionately young age structure with massive cohorts of children and adolescents. As these large youth cohorts advance into their prime reproductive years, the sheer volume of potential parents produces a large annual number of total births, even when each woman bears only replacement-level offspring.

### 1. Nathan Keyfitz's Momentum Formula
In 1971, Nathan Keyfitz derived an analytical expression for the **Demographic Momentum Factor** $M$, defined as the ratio of the ultimate stationary population size $P_\infty$ to the population size at the moment fertility drops to replacement level $P_0$:

$$M = \frac{P_\infty}{P_0} = \frac{b}{r \cdot e_0^\circ} \left( \frac{R_0 - 1}{R_0} \right) \left( \frac{1}{\mu_1 - \frac{1}{2} r \sigma^2} \right)$$

where:
- $b$: The crude birth rate at the moment of intervention ($t = 0$).
- $r$: The intrinsic rate of natural increase prior to intervention ($r > 0$).
- $e_0^\circ$: The life expectancy at birth in the stationary mortality regime.
- $R_0$: The pre-intervention Net Reproduction Rate ($R_0 > 1$).
- $\mu_1$: The mean age of childbearing in the stationary population ($\approx 27 - 29$ years).

In simplified empirical demography, Keyfitz's formula is commonly approximated as:

$$M \approx \frac{b \cdot e_0^\circ}{\sqrt{R_0}}$$

*Illustrative Interpretation*: Consider a high-growth population where the crude birth rate is $b = 35$ per $1,000$ ($0.035$), life expectancy at birth is $e_0^\circ = 70$ years, and $R_0 = 2.0$ (each mother averages two surviving daughters). Substituting these values yields:
$$M \approx \frac{0.035 \times 70}{\sqrt{2.0}} = \frac{2.45}{1.414} \approx 1.73$$
Even though fertility instantly drops to replacement, demographic momentum guarantees that the population will inevitably expand by an additional $73\%$ before stabilization!

### 2. Demographic Dependency Ratios and the Demographic Dividend
Demographic age structures are conventionally divided into three broad functional categories:
1. Youth population (ages $0 - 14$): $P_{0-14}$
2. Working-age population (ages $15 - 64$): $P_{15-64}$
3. Senior population (ages $65+$): $P_{65+}$

The economic burden placed on the productive workforce is measured by three **Dependency Ratios**:
- **Child Dependency Ratio ($CDR$)**: $CDR = \frac{P_{0-14}}{P_{15-64}}$
- **Old-Age Dependency Ratio ($ODR$)**: $ODR = \frac{P_{65+}}{P_{15-64}}$
- **Total Dependency Ratio ($TDR$)**: $TDR = \frac{P_{0-14} + P_{65+}}{P_{15-64}} = CDR + ODR$

When fertility declines rapidly, child dependency plunges while old-age dependency remains temporarily modest. This creates a multi-decade window where the total dependency ratio reaches a historical minimum ($TDR < 0.50$), producing the **Demographic Dividend**—a powerful economic growth catalyst where workforce expansion outpaces overall population growth.
"""

# --- UNIT 6 FINAL ADDITION ---
u6_path = DRAFT_DIR / "unit-6.md"
u6_text = u6_path.read_text(encoding="utf-8")
u6_add = r"""
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
"""

# --- UNIT 7 FINAL ADDITION ---
u7_path = DRAFT_DIR / "unit-7.md"
u7_text = u7_path.read_text(encoding="utf-8")
u7_add = r"""
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
"""

# --- UNIT 8 FINAL ADDITION ---
u8_path = DRAFT_DIR / "unit-8.md"
u8_text = u8_path.read_text(encoding="utf-8")
u8_add = r"""
## 8.9 Actuarial Pension Valuation Methods: Projected Unit Credit vs Entry Age Normal

Defined benefit (DB) pension plans promise retirement annuities defined by a benefit formula:
$$\text{Annual Pension} = k \cdot n \cdot S_{\text{final}}$$
where $k$ is the annual accrual rate (e.g., $1.5\% - 2.0\%$), $n$ is years of credited service, and $S_{\text{final}}$ is the final average salary (e.g., average of the final three years).

To determine annual employer contributions, consulting actuaries utilize cost allocation methods governed by the International Accounting Standard (IAS 19) and the US Financial Accounting Standards Board (ASC 715).

### 1. The Projected Unit Credit (PUC) Method
The **Projected Unit Credit** method allocates total projected retirement benefits across years of service accrued to date:
- At attained age $x$ with entry age $e$, elapsed service is $y = x - e$, and total service at normal retirement age $r$ is $n = r - e$.
- The **Actuarial Accrued Liability (AAL)** is the present value of the projected retirement benefit earned for service rendered prior to the valuation date:
  $$\text{AAL}_x^{\text{PUC}} = \left( \frac{x - e}{r - e} \right) \cdot PVFB_x$$
  where $PVFB_x$ is the Present Value of Future Benefits at age $x$, incorporating salary growth projections $s_r / s_x$.
- The **Normal Cost (NC)** is the present value of the additional benefit unit allocated to the current year:
  $$\text{NC}_x^{\text{PUC}} = \frac{1}{r - e} \cdot PVFB_x = \frac{\text{AAL}_x^{\text{PUC}}}{x - e}$$
*Characteristic Behavior*: Because $PVFB_x$ increases exponentially with age as the employee nears retirement (due to fewer years of interest discounting and higher survival probabilities), the PUC normal cost per employee rises rapidly with age.

### 2. The Entry Age Normal (EAN) Method
The **Entry Age Normal** method treats the pension funding cost as a level percentage of employee salary $C$ payable from initial employment age $e$ to retirement age $r$:
- The contribution rate $C$ is determined at entry age $e$ to equate the present value of future normal costs to the present value of future benefits:
  $$C \cdot \ddot{a}_{e:\overline{r-e}|}^{s} = PVFB_e \implies C = \frac{PVFB_e}{\ddot{a}_{e:\overline{r-e}|}^{s}}$$
  where $\ddot{a}_{e:\overline{r-e}|}^{s}$ is a salary-weighted annuity factor.
- At attained age $x$, the **Normal Cost** is simply:
  $$\text{NC}_x^{\text{EAN}} = C \cdot s_x$$
- The **Actuarial Accrued Liability** under EAN is computed prospectively:
  $$\text{AAL}_x^{\text{EAN}} = PVFB_x - C \cdot s_x \cdot \ddot{a}_{x:\overline{r-x}|}^{s}$$
  or retrospectively:
  $$\text{AAL}_x^{\text{EAN}} = C \sum_{j=e}^{x-1} s_j \frac{{}_j p_e (1 + i)^{x-j}}{{}_{x-e} p_e}$$

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Valuation Metric</th>
<th>Projected Unit Credit (PUC)</th>
<th>Entry Age Normal (EAN)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Accounting Standard</td>
<td>Mandated under IFRS (IAS 19) and US GAAP</td>
<td>Preferred for statutory funding and US public pensions</td>
</tr>
<tr>
<td>Normal Cost Trajectory</td>
<td>Increases steadily with participant age</td>
<td>Level percentage of employee payroll over career</td>
</tr>
<tr>
<td>Accrued Liability ($AAL$)</td>
<td>Lower in early career, accelerates later</td>
<td>Higher in early career, smoother progression</td>
</tr>
<tr>
<td>Budget Predictability</td>
<td>Vulnerable to demographic aging of workforce</td>
<td>Highly stable budgeting as a constant payroll fraction</td>
</tr>
</tbody>
</table>
</div>

The difference between the Actuarial Accrued Liability and the market value of plan assets ($AAL - \text{Assets}$) represents the **Unfunded Actuarial Liability (UAL)**, which employers amortize over statutory periods (typically 15 to 30 years).
"""

final_expansions = [
    (1, u1_path, u1_text, u1_add),
    (2, u2_path, u2_text, u2_add),
    (3, u3_path, u3_text, u3_add),
    (4, u4_path, u4_text, u4_add),
    (5, u5_path, u5_text, u5_add),
    (6, u6_path, u6_text, u6_add),
    (7, u7_path, u7_text, u7_add),
    (8, u8_path, u8_text, u8_add),
]

for unit_num, path, text, add in final_expansions:
    marker = "## Fully worked question 1:"
    idx = text.find(marker)
    if idx == -1:
        print(f"Warning: Marker not found in unit {unit_num}!")
        continue
    new_text = text[:idx] + add.strip() + "\n\n" + text[idx:]
    path.write_text(new_text, encoding="utf-8")
    print(f"Unit {unit_num} expanded successfully.")

print("All units expanded with final additions.")
