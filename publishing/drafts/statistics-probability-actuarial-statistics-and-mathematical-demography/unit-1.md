# Unit 1: Theory of Interest, Discount Rates & Financial Mathematics

## 1.1 The Economic Principle of the Time Value of Money and Accumulation Functions

Actuarial science and quantitative financial mathematics rest fundamentally upon the axiom of the **Time Value of Money**: a monetary unit (such as \$1 or 1 BDT) received immediately in the present possesses greater economic utility than the contractual promise of the identical monetary unit received at some future epoch $t > 0$. This disparity arises from three compounding economic phenomena:
1. **Investment Productivity (Opportunity Cost of Capital)**: Capital deployed in productive industrial enterprise generates surplus economic value over time through capital appreciation and operational profits.
2. **Systemic Price Inflation**: General increases in the consumer price level systematically erode the physical purchasing power of currency over time.
3. **Default and Uncertainty Risk**: An unfulfilled future cash flow carries counterparty default risk and systemic liquidity hazards.

To formalize this mathematically, let $t \ge 0$ denote continuous time measured in calendar years from an initial origin $t = 0$. An investment of principal capital $K$ made at time $t = 0$ grows into an accumulated value $A(t)$ at time $t$. The dimensionless transformation function governing this growth is the **Accumulation Function** $a(t)$:

$$a(t) = \frac{A(t)}{K}, \qquad t \ge 0$$

Mathematical consistency requires:
- Initial condition: $a(0) = 1.0$.
- Monotonicity: For non-negative interest environments, $a(t)$ is monotonically non-decreasing ($\frac{d a(t)}{dt} \ge 0$).
- Convexity: Under compound interest, $a(t)$ is strictly convex.

### Simple Interest Versus Compound Interest
1. **Simple Interest**: Interest is earned exclusively on the original principal capital $K$, with accrued interest never added to principal:
   $$a(t) = 1 + i \cdot t, \qquad t \ge 0$$
   where $i > 0$ is the constant annual simple interest rate. Simple interest violates the principle of financial time-consistency: splitting an investment horizon into sub-periods $[0, t_1]$ and $[t_1, t_2]$ yields $a(t_1) a(t_2 - t_1) \ne a(t_2)$. Simple interest is mathematically confined to short-term commercial money-market loans ($t < 1\text{ year}$).
2. **Compound Interest**: Interest earned during any infinitesimal or discrete interval is instantly capitalized into principal, itself earning interest in all subsequent intervals:
   $$a(t) = (1 + i)^t, \qquad t \ge 0$$
   Compound interest satisfies the multiplicative semi-group property:
   $$a(t_1 + t_2) = a(t_1) \cdot a(t_2)$$
   ensuring that transaction timing, intermediate refinancing, and cash flow pooling remain invariant to calendar origin.

## 1.2 Effective Rates of Interest and Discount

Let an investment horizon be partitioned into discrete annual periods $[t - 1, t]$ for $t = 1, 2, 3, \dots$.

### The Effective Annual Rate of Interest ($i$)
The **effective rate of interest** $i_t$ for the $t$-th operating year is the ratio of the amount of interest earned during that period to the capital invested at the start of the period:

$$i_t = \frac{A(t) - A(t - 1)}{A(t - 1)} = \frac{a(t) - a(t - 1)}{a(t - 1)}$$

Under stationary compound interest, $i_t$ is strictly invariant over time: $i_t = i$ for all $t \ge 1$.

### The Discount Factor ($v$)
To determine the present capital value $P$ required today to accumulate to a future sum of $1$ unit at time $t = 1$, we invert the accumulation operator:

$$v = \frac{1}{1 + i} = (1 + i)^{-1}$$

The term $v$ is the **Present Value Discount Factor** (or discount factor). Discounting a future cash flow $C_t$ due at time $t$ to its present value at time $0$ requires scaling by $v^t$:

$$PV(C_t) = C_t \cdot v^t = C_t (1 + i)^{-t}$$

### The Effective Rate of Discount ($d$)
While interest $i$ is paid at the *end* of an annual period as a percentage of the *initial* principal, commercial transactions frequently charge interest in advance at the *start* of the period as a percentage of the *final maturity value*. This defines the **effective rate of discount** $d$:

$$d_t = \frac{A(t) - A(t - 1)}{A(t)} = \frac{a(t) - a(t - 1)}{a(t)}$$

Under stationary compound conditions:

$$d = \frac{i}{1 + i} = i \cdot v = 1 - v$$

Algebraic manipulation yields the fundamental triad of actuarial financial equivalences:

$$i - d = i \cdot d$$

$$v = 1 - d = (1 + i)^{-1}$$

$$1 + i = \frac{1}{1 - d} = (1 - d)^{-1}$$

The quantity $i - d$ represents the interest earned on the interest paid in advance: if a borrower pays discount $d$ at the start of the year, that amount $d$ could itself be invested at interest rate $i$ for the remainder of the year to yield $i \cdot d$.

## 1.3 Nominal Rates of Interest and Discount Compounded $m$-thly

In practical commercial banking and bond markets, interest is rarely credited solely once per annum. Mortgages, savings accounts, and corporate bonds credit interest semi-annually ($m = 2$), quarterly ($m = 4$), monthly ($m = 12$), or daily ($m = 365$).

### Nominal Rate of Interest $i^{(m)}$
A **nominal rate of interest payable $m$ times a year** is denoted $i^{(m)}$. The interest credited during each $m$-th of a year is the sub-period rate:

$$i_{\text{sub}} = \frac{i^{(m)}}{m}$$

Compounding this sub-period rate across $m$ sub-periods over one complete calendar year must reproduce the effective annual rate of interest $i$:

$$\left( 1 + \frac{i^{(m)}}{m} \right)^m = 1 + i$$

Inverting yields the exact relationship:

$$i^{(m)} = m \left[ (1 + i)^{1/m} - 1 \right]$$

### Nominal Rate of Discount $d^{(m)}$
Similarly, a **nominal rate of discount convertible $m$ times a year** $d^{(m)}$ charges a discount fraction $d^{(m)} / m$ at the start of each $m$-th of a year:

$$\left( 1 - \frac{d^{(m)}}{m} \right)^m = 1 - d = v = (1 + i)^{-1}$$

$$d^{(m)} = m \left[ 1 - v^{1/m} \right] = m \left[ 1 - (1 + i)^{-1/m} \right]$$

### Asymptotic Ordering of Nominal Rates
Expanding $(1 + i)^{1/m}$ via the binomial series for small $i$:
$$i^{(m)} = m \left[ 1 + \frac{1}{m}i + \frac{1/m(1/m - 1)}{2} i^2 + \dots - 1 \right] = i - \frac{m - 1}{2m} i^2 + \dots$$
As the compounding frequency $m$ increases, less compounding delay occurs, so a lower nominal rate is required to produce the same effective annual yield. This establishes the universal actuarial inequality chain:

$$d < d^{(2)} < d^{(4)} < d^{(12)} < \dots < \delta < \dots < i^{(12)} < i^{(4)} < i^{(2)} < i$$

Every nominal interest rate exceeds the continuous force of interest $\delta$, which in turn exceeds every nominal discount rate!

## 1.4 The Instantaneous Force of Interest ($\delta(t)$)

As compounding frequency approaches infinity ($m \to \infty$), compounding occurs continuously at every infinitesimal instant of time $dt$.

### Continuous Force of Interest Definition
For an arbitrary accumulation function $a(t)$, the **force of interest** $\delta(t)$ is defined as the instantaneous proportional growth rate of capital:

$$\delta(t) = \lim_{\Delta t \to 0} \frac{a(t + \Delta t) - a(t)}{\Delta t \cdot a(t)} = \frac{a'(t)}{a(t)} = \frac{d}{dt} \ln a(t)$$

Integrating both sides from $0$ to $t$:

$$\int_0^t \delta(u)\,du = \ln a(t) - \ln a(0) = \ln a(t) \quad (\text{since } a(0) = 1)$$

Exponentiating yields the general accumulation operator under continuous varying interest:

$$a(t) = \exp\left( \int_0^t \delta(u)\,du \right)$$

The corresponding discount factor from time $t_2$ back to time $t_1$ is:

$$v(t_1, t_2) = \exp\left( -\int_{t_1}^{t_2} \delta(u)\,du \right)$$

### Constant Force of Interest
When the force of interest is constant over time ($\delta(t) = \delta$):

$$a(t) = e^{\delta t}$$

Setting $t = 1$, we relate the continuous force of interest directly to the discrete effective rate of interest $i$:

$$e^\delta = 1 + i \implies \delta = \ln(1 + i) = -\ln(1 - d) = -\ln v$$

Taking the limit of nominal rates as $m \to \infty$:

$$\lim_{m \to \infty} i^{(m)} = \lim_{m \to \infty} m \left( (1 + i)^{1/m} - 1 \right) = \lim_{h \to 0} \frac{(1 + i)^h - 1}{h} = \ln(1 + i) = \delta$$

$$\lim_{m \to \infty} d^{(m)} = \lim_{m \to \infty} m \left( 1 - (1 + i)^{-1/m} \right) = \ln(1 + i) = \delta$$

The continuous force of interest $\delta$ represents the singular mathematical nexus where the nominal interest rate and nominal discount rate converge.

## 1.5 Equations of Value, Net Present Value, and Internal Rate of Return

A financial transaction or actuarial insurance contract is modeled as a stream of deterministic cash flows:
$$\mathbf{C} = \{(c_k, t_k) : k = 0, 1, 2, \dots, n\}$$
where $c_k$ is the net cash flow (inflow if $c_k > 0$, outflow if $c_k < 0$) occurring at calendar time $t_k \ge 0$.

### The Equation of Value
The fundamental operational equation of financial mathematics is the **Equation of Value**, which states that at any chosen comparison date $T$ (focal date), the accumulated value of all past cash flows must equal the discounted present value of all future cash flows:

$$\sum_{k=0}^n c_k (1 + i)^{T - t_k} = 0$$

Choosing focal date $T = 0$, the Equation of Value expresses the **Net Present Value (NPV)**:

$$NPV(i) = \sum_{k=0}^n c_k v^{t_k} = \sum_{k=0}^n c_k (1 + i)^{-t_k} = 0$$

### The Internal Rate of Return (IRR)
The **Internal Rate of Return (IRR)**, or yield rate $i^*$, is the interest rate that satisfies the Equation of Value: $NPV(i^*) = 0$.

Letting $x = 1 + i$, the equation $NPV(i) = 0$ is a polynomial in $x^{-1}$. By the Fundamental Theorem of Algebra, a polynomial of degree $n$ has $n$ complex roots. For financial viability, there must exist a **unique positive real root** $i^* > -1$.

### Descartes' Rule of Signs and Project Uniqueness
Descartes' Rule of Signs establishes that the number of positive real roots of a polynomial cannot exceed the number of sign changes in its sequence of coefficients $(c_0, c_1, \dots, c_n)$:
- **Standard Conventional Project**: A single sign change occurs: an initial capital investment outflow ($c_0 < 0$) followed by purely positive inflows ($c_k > 0$ for $k \ge 1$). Here, the number of sign changes is exactly $1$, guaranteeing a **unique real yield rate $i^*$**.
- **Non-Conventional Cash Flows**: If the cash flow stream changes sign multiple times (e.g., subsequent environmental clean-up costs or decommissioning outflows $c_n < 0$), multiple real internal rates of return can exist ($i_1^* \ne i_2^*$), rendering IRR mathematically ambiguous. In such cases, financial actuaries rely on the **Net Present Value rule** evaluated at a market hurdle rate $r$.

## 1.6 Real Versus Nominal Rates of Interest and Fisher's Equation

When future cash flows span decades (such as in life insurance policies, defined-benefit pension schemes, and long-term infrastructure bonds), general macroeconomic price inflation degrades purchasing power.

Let $i$ denote the **nominal annual interest rate** (the monetary growth rate of capital).
Let $r$ denote the **inflation rate** (the annual growth rate of the Consumer Price Index).
Let $i'$ denote the **real annual interest rate** (the physical purchasing power growth rate of capital).

Over one annual period:
$$1 + i = (1 + i')(1 + r) = 1 + i' + r + i' r$$

Rearranging yields the exact **Fisher Equation**:

$$i' = \frac{1 + i}{1 + r} - 1 = \frac{i - r}{1 + r}$$

When inflation rates are modest ($r \ll 1$), the denominator $1 + r \approx 1$, yielding the standard linear approximation:
$$i' \approx i - r$$
However, in high-inflation environments, the full non-linear Fisher formulation must be employed. If an asset pays cash flows indexed to inflation, actuarial present values are computed by discounting real cash flows at the real interest rate $i'$.

## 1.7 Fixed-Income Asset Duration and Convexity

To protect pension funds and life insurance companies against interest rate volatility, actuaries measure the sensitivity of present values to fluctuations in the yield rate $i$.

Let a fixed-income bond promise cash flows $c_t$ at times $t = 1, 2, \dots, n$, with current market price:
$$P(i) = \sum_{t=1}^n c_t (1 + i)^{-t}$$

### Macaulay Duration ($D_{\text{mac}}$)
Frederick Macaulay (1938) defined the **Macaulay Duration** as the weighted average maturity of cash flows, where each time $t$ is weighted by the present value of that cash flow as a proportion of the total price:

$$D_{\text{mac}} = \frac{\sum_{t=1}^n t \cdot c_t (1 + i)^{-t}}{\sum_{t=1}^n c_t (1 + i)^{-t}} = \frac{1}{P(i)} \sum_{t=1}^n t \cdot c_t v^t$$

### Modified Duration ($D_{\text{mod}}$)
The **Modified Duration** measures the exact percentage change in bond price per unit change in yield $i$:

$$D_{\text{mod}} = -\frac{1}{P(i)} \frac{d P(i)}{di} = -\frac{1}{P(i)} \sum_{t=1}^n (-t) c_t (1 + i)^{-t-1} = \frac{D_{\text{mac}}}{1 + i}$$

The first-order linear Taylor series price approximation is:
$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta i$$

### Convexity ($C$)
Because the price-yield relationship $P(i)$ is strictly convex ($d^2 P / di^2 > 0$), modified duration underestimates price gains when rates fall and overestimates price losses when rates rise. **Convexity** provides the second-order curvature correction:

$$C = \frac{1}{P(i)} \frac{d^2 P(i)}{di^2} = \frac{1}{P(i)} \sum_{t=1}^n t (t + 1) c_t (1 + i)^{-t-2} = \frac{v^2}{P(i)} \sum_{t=1}^n t(t+1) c_t v^t$$

The second-order Taylor series approximation is:

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta i + \frac{1}{2} C \cdot (\Delta i)^2$$

**Redington's Immunization**: In 1952, F. M. Redington proved that an insurance company's surplus is immunized against infinitesimal interest rate shifts if:
1. $PV(\text{Assets}) = PV(\text{Liabilities})$
2. $D_{\text{Assets}} = D_{\text{Liabilities}}$ (duration matching)
3. $C_{\text{Assets}} > C_{\text{Liabilities}}$ (convexity of assets exceeds liabilities)

## 1.8 Stochastic Term Structure Models: Vasicek and Cox-Ingersoll-Ross

While classical financial mathematics treats the force of interest $\delta(t)$ as a deterministic function of calendar time, real fixed-income capital markets experience continuous stochastic fluctuations driven by macroeconomic shocks, central bank liquidity operations, and inflation expectations.

In modern quantitative financial actuarial theory, the instantaneous short rate $r(t) = \delta(t)$ is modeled as a continuous-time stochastic diffusion process satisfying a stochastic differential equation (SDE):

$$dr(t) = \mu(r(t), t)\,dt + \sigma(r(t), t)\,dW(t)$$

where $W(t)$ is a standard Brownian motion (Wiener process) defined on a filtered probability space.

### 1. The Vasicek Model (Ornstein-Uhlenbeck Process)
Oldrich Vasicek (1977) formulated the seminal mean-reverting interest rate model:

$$dr(t) = \kappa (\theta - r(t))\,dt + \sigma\,dW(t)$$

where:
- $\theta > 0$: The long-term mean reversion level.
- $\kappa > 0$: The speed of mean reversion.
- $\sigma > 0$: The instantaneous volatility coefficient.

Under the Vasicek model, conditional on $r(s)$ for $s < t$, the short rate $r(t)$ follows a Gaussian distribution:

$$r(t) \mid r(s) \sim \mathcal{N}\left( \theta + (r(s) - \theta) e^{-\kappa(t - s)}, \; \frac{\sigma^2}{2\kappa} (1 - e^{-2\kappa(t - s)}) \right)$$

The zero-coupon bond price $P(t, T)$ maturing at time $T$ admits an exact analytical affine term structure representation:

$$P(t, T) = \mathbb{E}^{\mathbb{Q}}\left[ \exp\left( -\int_t^T r(u)\,du \right) \Big| r(t) \right] = A(t, T) \exp(-B(t, T) r(t))$$

where $B(t, T) = \frac{1 - e^{-\kappa(T - t)}}{\kappa}$, and $A(t, T)$ is an explicit deterministic function.
*Theoretical Limitation*: Because $r(t)$ is Gaussian, the Vasicek model assigns positive probability to negative nominal interest rates ($P(r(t) < 0) > 0$).

### 2. The Cox-Ingersoll-Ross (CIR) Model
John Cox, Jonathan Ingersoll, and Stephen Ross (1985) eliminated negative interest rates by introducing a square-root diffusion coefficient:

$$dr(t) = \kappa (\theta - r(t))\,dt + \sigma \sqrt{r(t)}\,dW(t)$$

When the interest rate approaches zero, the volatility term $\sigma \sqrt{r(t)} \to 0$, while the drift term $\kappa \theta > 0$ pushes the rate back toward positive territory. Under the Feller condition:

$$2 \kappa \theta \ge \sigma^2$$

the boundary at $r = 0$ is strictly inaccessible, guaranteeing that the force of interest remains strictly positive for all $t > 0$. The conditional distribution of $r(t)$ follows a scaled non-central chi-square distribution, providing an indispensable foundation for pricing interest rate derivatives, guaranteed minimum withdrawal benefits (GMWB), and variable annuities.

## 1.9 Capital Budgeting Criteria: Net Present Value Profile and Fisher's Intersection

In actuarial corporate finance, choosing between competing capital investment projects requires comparing cash flow streams across multiple evaluation metrics:
1. **Net Present Value (NPV)**:
   $$NPV(i) = \sum_{t=0}^n c_t (1 + i)^{-t}$$
2. **Profitability Index ($PI$)**: The ratio of the present value of future cash inflows to the initial capital outlay:
   $$PI = \frac{\sum_{t=1}^n c_t (1 + i)^{-t}}{-c_0}$$
   A project is acceptable if $PI > 1.0$.
3. **Payback Period**: The earliest time $T_{\text{pb}}$ at which cumulative undiscounted cash inflows equal the initial investment:
   $$\min T_{\text{pb}} \quad \text{such that} \quad \sum_{t=1}^{T_{\text{pb}}} c_t \ge -c_0$$
   The discounted payback period replaces raw cash flows with discounted cash flows $c_t v^t$.

### The Net Present Value Profile and Fisher's Rate of Return
Plotting $NPV(i)$ as a continuous function of the discount rate $i$ produces the **NPV Profile**. For a conventional project, $NPV(i)$ is a monotonically decreasing convex function of $i$. The horizontal axis intercept ($NPV(i) = 0$) defines the Internal Rate of Return ($IRR$).

When two mutually exclusive investment projects (Project A and Project B) are compared:
- If their NPV profiles cross, the discount rate at the intersection point is **Fisher's Rate of Intersection ($i_{\text{Fisher}}$)**:
  $$NPV_A(i_{\text{Fisher}}) = NPV_B(i_{\text{Fisher}}) \iff NPV_{A - B}(i_{\text{Fisher}}) = 0$$
  Fisher's rate is the internal rate of return on the incremental cash flow stream $(c_t^A - c_t^B)$.
- If the company's cost of capital is less than Fisher's rate ($i < i_{\text{Fisher}}$), Project A may have higher NPV while Project B has higher IRR, producing an **NPV-IRR conflict**. Actuarial financial theory establishes that the **NPV criterion is universally superior**: maximizing NPV directly maximizes the total terminal monetary surplus of the firm's shareholders.

## 1.10 Full Immunization: Shiu's Generalization and Multi-Period Liability Matching

While Redington's classical immunization guarantees surplus protection against infinitesimal parallel yield curve shifts ($\Delta i \to 0$), it does not guarantee protection against large, non-infinitesimal interest rate shocks ($\Delta i \gg 0$).

### Elias Shiu's Theorem on Full Immunization
In 1987, Elias S. M. Shiu formulated the exact necessary and sufficient conditions for **Full Immunization**. 

Consider an insurer facing a single liability cash outflow $L$ due at calendar time $t_L$, funded by an asset portfolio of cash inflows $A_t$ at times $t_1 < t_2 < \dots < t_m$. The net surplus at yield $i$ is:

$$S(i) = \sum_{j=1}^m A_{t_j} (1 + i)^{-t_j} - L (1 + i)^{-t_L}$$

Shiu proved that the surplus is guaranteed to be strictly non-negative ($S(i) \ge 0$) for *any arbitrary change in interest rate* $\Delta i \in (-1, \infty)$ if and only if:
1. $PV(\text{Assets}) = PV(\text{Liabilities})$ at the current market rate $i_0$.
2. The asset portfolio duration matches the liability date:
   $$D_{\text{mac}}(\text{Assets}) = t_L$$
3. **Cash Flow Straddling**: There must exist at least one asset cash inflow strictly before the liability date and at least one asset cash inflow strictly after the liability date:
   $$t_1 < t_L < t_m$$

When asset inflows straddle the liability outflow, the surplus function $S(i)$ achieves a global minimum of zero at $i = i_0$, so that $S(i) > 0$ for all $i \ne i_0$. Full immunization completely eliminates interest rate risk for single-liability matching.

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

## Fully worked question 1: Exact Equivalence Across Nominal Rates and Force of Interest

### Question
An institutional investment portfolio earns a constant effective annual rate of interest of $i = 8.00\%$ ($i = 0.08$).

Perform the following calculations:
1. Compute the exact discount factor $v$ and the effective annual rate of discount $d$.
2. Compute the nominal rate of interest compounded semi-annually ($i^{(2)}$), quarterly ($i^{(4)}$), and monthly ($i^{(12)}$).
3. Compute the nominal rate of discount compounded semi-annually ($d^{(2)}$), quarterly ($d^{(4)}$), and monthly ($d^{(12)}$).
4. Compute the continuous force of interest $\delta$.
5. Verify numerically the universal inequality chain:
   $$d < d^{(2)} < d^{(4)} < d^{(12)} < \delta < i^{(12)} < i^{(4)} < i^{(2)} < i$$

### Solution, step 1: Compute discount factor $v$ and effective discount rate $d$
Given $i = 0.080000$:
$$v = \frac{1}{1 + i} = \frac{1}{1.08} \approx 0.925926$$
$$d = \frac{i}{1 + i} = 1 - v = 1 - 0.925926 = 0.074074 \implies 7.4074\%$$
Verifying $i - d = i \cdot d$:
$$i - d = 0.080000 - 0.074074 = 0.005926$$
$$i \cdot d = 0.080000 \times 0.074074 = 0.005926$$
The identity holds.

### Solution, step 2: Compute nominal interest rates $i^{(m)}$
Using $i^{(m)} = m \left[ (1 + i)^{1/m} - 1 \right]$:
- For $m = 2$ (semi-annual):
  $$i^{(2)} = 2 \left[ (1.08)^{0.5} - 1 \right] = 2 [1.0392305 - 1] = 2 \times 0.0392305 = 0.078461 \implies 7.8461\%$$
- For $m = 4$ (quarterly):
  $$i^{(4)} = 4 \left[ (1.08)^{0.25} - 1 \right] = 4 [1.0194265 - 1] = 4 \times 0.0194265 = 0.077706 \implies 7.7706\%$$
- For $m = 12$ (monthly):
  $$i^{(12)} = 12 \left[ (1.08)^{1/12} - 1 \right] = 12 [1.0064340 - 1] = 12 \times 0.0064340 = 0.077208 \implies 7.7208\%$$

### Solution, step 3: Compute nominal discount rates $d^{(m)}$
Using $d^{(m)} = m \left[ 1 - v^{1/m} \right] = m \left[ 1 - (1.08)^{-1/m} \right]$:
- For $m = 2$:
  $$d^{(2)} = 2 \left[ 1 - (1.08)^{-0.5} \right] = 2 [1 - 0.9622504] = 2 \times 0.0377496 = 0.075499 \implies 7.5499\%$$
- For $m = 4$:
  $$d^{(4)} = 4 \left[ 1 - (1.08)^{-0.25} \right] = 4 [1 - 0.9809437] = 4 \times 0.0190563 = 0.076225 \implies 7.6225\%$$
- For $m = 12$:
  $$d^{(12)} = 12 \left[ 1 - (1.08)^{-1/12} \right] = 12 [1 - 0.9936071] = 12 \times 0.0063929 = 0.076715 \implies 7.6715\%$$

### Solution, step 4: Compute continuous force of interest $\delta$
$$\delta = \ln(1 + i) = \ln(1.08) \approx 0.076961 \implies 7.6961\%$$

### Solution, step 5: Verify the universal inequality chain
Collating all values in percentage form:
- $d = 7.4074\%$
- $d^{(2)} = 7.5499\%$
- $d^{(4)} = 7.6225\%$
- $d^{(12)} = 7.6715\%$
- $\delta = 7.6961\%$
- $i^{(12)} = 7.7208\%$
- $i^{(4)} = 7.7706\%$
- $i^{(2)} = 7.8461\%$
- $i = 8.0000\%$

Checking ordering:
$$7.4074\% < 7.5499\% < 7.6225\% < 7.6715\% < 7.6961\% < 7.7208\% < 7.7706\% < 7.8461\% < 8.0000\%$$
The universal inequality chain holds with complete mathematical rigor.

## Fully worked question 2: Time-Varying Force of Interest and Continuous Present Value

### Question
An environmental reclamation trust fund guarantees a payment of $C = 1,000,000\text{ BDT}$ at time $t = 10\text{ years}$ to restore a retired open-pit bauxite mine. Because macroeconomic market conditions are transitioning, the instantaneous force of interest is not constant, but varies continuously according to the deterministic quadratic function:

$$\delta(t) = 0.03 + 0.008 t - 0.0004 t^2, \qquad 0 \le t \le 10$$

Perform the following calculations:
1. Determine the accumulation function $a(t)$ for $0 \le t \le 10$.
2. Compute the exact value of $a(10)$.
3. Determine the equivalent level constant force of interest $\bar{\delta}$ over the 10-year horizon.
4. Compute the present value $PV$ that must be deposited into the trust fund today at $t = 0$ to fund the $1,000,000\text{ BDT}$ liability.
5. If the trust fund earns an additional continuous cash inflow of $R(t) = 50,000\text{ BDT/year}$ streaming continuously over the first 5 years ($0 \le t \le 5$), write the integral for the present value of this continuous annuity and compute its exact numerical value.

### Solution, step 1: Derive the accumulation function $a(t)$
Using $a(t) = \exp\left( \int_0^t \delta(u)\,du \right)$:
$$\int_0^t \delta(u)\,du = \int_0^t (0.03 + 0.008 u - 0.0004 u^2)\,du$$
Evaluating the antiderivative:
$$\int_0^t \delta(u)\,du = \left[ 0.03 u + 0.008 \frac{u^2}{2} - 0.0004 \frac{u^3}{3} \right]_0^t = 0.03 t + 0.004 t^2 - \frac{0.0004}{3} t^3$$

Thus, the accumulation function is:
$$a(t) = \exp\left( 0.03 t + 0.004 t^2 - \frac{0.0004}{3} t^3 \right)$$

### Solution, step 2: Compute $a(10)$
For $t = 10$:
$$\text{Exponent} = 0.03(10) + 0.004(10^2) - \frac{0.0004}{3}(10^3) = 0.30 + 0.004(100) - \frac{0.40}{3}$$
$$= 0.30 + 0.40 - 0.133333 = 0.70 - 0.133333 = 0.566667$$
$$a(10) = \exp(0.566667) \approx 1.76238$$
One unit invested at $t = 0$ accumulates to approximately $1.76238$ units at $t = 10$.

### Solution, step 3: Determine equivalent level constant force of interest $\bar{\delta}$
An equivalent level force of interest $\bar{\delta}$ satisfies:
$$\exp(10 \bar{\delta}) = a(10) = \exp(0.566667)$$
$$10 \bar{\delta} = 0.566667 \implies \bar{\delta} = \frac{0.566667}{10} = 0.056667 \implies 5.6667\%$$
The equivalent constant annual force of interest is **$5.6667\%$** (effective annual rate $i = e^{\bar{\delta}} - 1 = e^{0.056667} - 1 \approx 5.830\%$).

### Solution, step 4: Compute the present value of the reclamation liability
Discounting $1,000,000\text{ BDT}$ back to $t = 0$:
$$PV = \frac{C}{a(10)} = C \cdot \exp(-0.566667) = \frac{1,000,000}{1.76238} \approx 567,415\text{ BDT}$$
The trust fund must deposit **$567,415\text{ BDT}$** today to guarantee the future reclamation obligations.

### Solution, step 5: Value of continuous streaming cash inflows
The present value of a continuous payment stream $R(t)$ from $t = 0$ to $t = 5$ is:
$$PV_{\text{annuity}} = \int_0^5 R(t) [a(t)]^{-1} \, dt = 50,000 \int_0^5 \exp\left( -\left(0.03 t + 0.004 t^2 - \frac{0.0004}{3} t^3\right) \right) dt$$
To evaluate this integral accurately, compute the exponent values at discrete midpoints or use Simpson's rule across 5 sub-intervals ($h = 1$):
- $t = 0$: $\exp(0) = 1.00000$
- $t = 1$: $0.03(1) + 0.004(1) - 0.000133 = 0.033867 \implies e^{-0.033867} = 0.96669$
- $t = 2$: $0.03(2) + 0.004(4) - 0.001067 = 0.074933 \implies e^{-0.074933} = 0.92781$
- $t = 3$: $0.03(3) + 0.004(9) - 0.003600 = 0.122400 \implies e^{-0.122400} = 0.88479$
- $t = 4$: $0.03(4) + 0.004(16) - 0.008533 = 0.175467 \implies e^{-0.175467} = 0.83906$
- $t = 5$: $0.03(5) + 0.004(25) - 0.016667 = 0.233333 \implies e^{-0.233333} = 0.79189$

Using Simpson's composite rule with $h = 1$:
$$\text{Integral} \approx \frac{1}{3} \left[ y_0 + 4(y_1 + y_3) + 2(y_2 + y_4) + y_5 \right]$$
$$y_1 + y_3 = 0.96669 + 0.88479 = 1.85148 \implies 4 \times 1.85148 = 7.40592$$
$$y_2 + y_4 = 0.92781 + 0.83906 = 1.76687 \implies 2 \times 1.76687 = 3.53374$$
$$y_0 + y_5 = 1.00000 + 0.79189 = 1.79189$$
$$\text{Sum} = 1.79189 + 7.40592 + 3.53374 = 12.73155$$
$$\text{Integral} = \frac{12.73155}{3} \approx 4.24385$$
Multiply by annual stream $50,000$:
$$PV_{\text{annuity}} = 50,000 \times 4.24385 \approx 212,193\text{ BDT}$$
The continuous cash inflow provides **$212,193\text{ BDT}$** in present value.

## Fully worked question 3: Bond Duration, Convexity, and Redington Immunization

### Question
A life insurance company issues a guaranteed structured settlement liability that requires paying a single lump-sum payout of $L = 5,000,000\text{ BDT}$ at time $t = 8\text{ years}$. The current prevailing market yield across all maturities is flat at $i = 6.00\%$ ($i = 0.06$).

To immunize this liability, the company's chief investment officer constructs an asset portfolio consisting of two zero-coupon government bonds:
- Bond 1: Matures at time $t_1 = 5\text{ years}$ (market price $P_1$)
- Bond 2: Matures at time $t_2 = 12\text{ years}$ (market price $P_2$)

Perform the following actuarial calculations:
1. Compute the present value ($PV_L$), Macaulay duration ($D_L$), and convexity ($C_L$) of the liability.
2. Determine the exact amounts (in BDT of present value) that must be allocated to Bond 1 ($A_1$) and Bond 2 ($A_2$) to satisfy the first two Redington immunization conditions ($PV_A = PV_L$ and $D_A = D_L$).
3. Compute the convexity of the resulting asset portfolio ($C_A$).
4. Verify whether the third Redington condition ($C_A > C_L$) is satisfied.
5. If the market yield shifts immediately upward by $100\text{ basis points}$ ($\Delta i = +0.01$, from $6\%$ to $7\%$), compute the exact change in asset value $\Delta A$, liability value $\Delta L$, and the change in the company's surplus $\Delta S = \Delta A - \Delta L$.

### Solution, step 1: Liability present value, duration, and convexity
Discount factor at $i = 0.06$: $v = (1.06)^{-1} \approx 0.943396$.
For a single cash flow of $5,000,000\text{ BDT}$ at $t = 8$:
1. **Present Value**:
   $$PV_L = 5,000,000 \times (1.06)^{-8} = \frac{5,000,000}{1.593848} \approx 3,137,062\text{ BDT}$$
2. **Macaulay Duration**:
   For any single cash flow, Macaulay duration is identically equal to its maturity:
   $$D_L = 8.000\text{ years}$$
   Modified duration:
   $$D_{\text{mod}, L} = \frac{8.000}{1.06} \approx 7.54717\text{ years}$$
3. **Convexity**:
   $$C_L = \frac{t(t + 1)}{(1 + i)^2} = \frac{8 \times 9}{(1.06)^2} = \frac{72}{1.1236} \approx 64.0797\text{ years}^2$$

### Solution, step 2: Asset allocation via duration matching
Let $A_1$ and $A_2$ denote the present value allocated to Bond 1 ($t_1 = 5$) and Bond 2 ($t_2 = 12$).
The two immunization equations are:
1. **Present Value Matching**:
   $$A_1 + A_2 = PV_L = 3,137,062$$
2. **Duration Matching**:
   The Macaulay duration of an asset portfolio is the weighted average of individual durations:
   $$\frac{5 A_1 + 12 A_2}{A_1 + A_2} = D_L = 8$$
   $$5 A_1 + 12 A_2 = 8(A_1 + A_2) = 8 A_1 + 8 A_2$$
   $$4 A_2 = 3 A_1 \implies A_1 = \frac{4}{3} A_2$$

Substitute into the present value equation:
$$\frac{4}{3} A_2 + A_2 = \frac{7}{3} A_2 = 3,137,062$$
$$A_2 = \frac{3}{7} \times 3,137,062 \approx 1,344,455\text{ BDT}$$
$$A_1 = \frac{4}{7} \times 3,137,062 \approx 1,792,607\text{ BDT}$$

The portfolio allocates **$1,792,607\text{ BDT}$** ($57.14\%$) to the 5-year bond and **$1,344,455\text{ BDT}$** ($42.86\%$) to the 12-year bond.

### Solution, step 3: Compute asset portfolio convexity
For each zero-coupon bond:
$$C_1 = \frac{5 \times 6}{(1.06)^2} = \frac{30}{1.1236} \approx 26.6999\text{ years}^2$$
$$C_2 = \frac{12 \times 13}{(1.06)^2} = \frac{156}{1.1236} \approx 138.8394\text{ years}^2$$

The asset portfolio convexity is the weighted average:
$$C_A = \frac{A_1 C_1 + A_2 C_2}{A_1 + A_2} = \frac{4}{7}(26.6999) + \frac{3}{7}(138.8394)$$
$$= 15.2571 + 59.5026 = 74.7597\text{ years}^2$$

### Solution, step 4: Verify Redington's third condition
Compare asset and liability convexities:
$$C_A = 74.7597\text{ years}^2 > C_L = 64.0797\text{ years}^2$$
Because $C_A > C_L$, the asset portfolio has greater curvature than the liability. Redington's third condition is satisfied, guaranteeing that any small interest rate movement (up or down) will increase the insurer's net surplus!

### Solution, step 5: Exact surplus impact under $\Delta i = +0.01$ (Yield increases to $7\%$)
At $i = 0.07$:
1. **New Liability Value**:
   $$L_{\text{new}} = 5,000,000 \times (1.07)^{-8} = \frac{5,000,000}{1.718186} \approx 2,909,929\text{ BDT}$$
   $$\Delta L = 2,909,929 - 3,137,062 = -227,133\text{ BDT}$$

2. **New Asset Value**:
   - Nominal face value of Bond 1: $F_1 = 1,792,607 \times (1.06)^5 = 1,792,607 \times 1.338226 = 2,398,913\text{ BDT}$.
     New value at $7\%$: $A_{1, \text{new}} = 2,398,913 \times (1.07)^{-5} = 2,398,913 / 1.402552 \approx 1,710,392\text{ BDT}$.
   - Nominal face value of Bond 2: $F_2 = 1,344,455 \times (1.06)^{12} = 1,344,455 \times 2.012196 = 2,705,307\text{ BDT}$.
     New value at $7\%$: $A_{2, \text{new}} = 2,705,307 \times (1.07)^{-12} = 2,705,307 / 2.252192 \approx 1,201,188\text{ BDT}$.
   - Total new asset value:
     $$A_{\text{new}} = 1,710,392 + 1,201,188 = 2,911,580\text{ BDT}$$
     $$\Delta A = 2,911,580 - 3,137,062 = -225,482\text{ BDT}$$

3. **Surplus Change ($\Delta S$)**:
   $$\Delta S = \Delta A - \Delta L = -225,482 - (-227,133) = +1,651\text{ BDT}$$
   Even though the yield spiked by a full percentage point, the company's surplus expanded by **$+1,651\text{ BDT}$**, proving the power of Redington immunization!
