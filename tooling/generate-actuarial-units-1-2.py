#!/usr/bin/env python3
"""
Generate Units 1 and 2 for Actuarial Statistics and Mathematical Demography.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_1 = r"""# Unit 1: Theory of Interest, Discount Rates & Financial Mathematics

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
"""

unit_2 = r"""# Unit 2: Annuities Certain, Varying Cash Flows & Loan Amortization Mechanics

## 2.1 Classical Annuities-Certain: Annuities-Immediate and Annuities-Due

An **annuity-certain** is a deterministic sequence of periodic payments made at specified regular intervals over a fixed, pre-determined time horizon of $n$ periods, where payment receipt is not contingent on any uncertain biological event (such as survival or death).

Annuities are classified into two structural payment timings:
- **Annuity-Immediate (Ordinary Annuity)**: Periodic payments of $1$ unit occur at the *end* of each of the $n$ consecutive periods (at times $t = 1, 2, \dots, n$).
- **Annuity-Due**: Periodic payments of $1$ unit occur at the *start* of each of the $n$ consecutive periods (at times $t = 0, 1, \dots, n - 1$).

### Mathematical Derivation of Present Values
Let $i$ denote the effective interest rate per period, and let $v = (1 + i)^{-1}$ be the periodic discount factor.

#### 1. The Present Value of an Annuity-Immediate ($a_{\overline{n}|}$)
The present value of an $n$-period annuity-immediate, denoted $a_{\overline{n}|}$, is the sum of the discounted present values of all $n$ payments:

$$a_{\overline{n}|} = v^1 + v^2 + v^3 + \dots + v^n = \sum_{t=1}^n v^t$$

This is a finite geometric series with initial term $v$ and common ratio $v$. Applying the summation formula:

$$a_{\overline{n}|} = v \frac{1 - v^n}{1 - v} = \frac{v}{1 - v} (1 - v^n)$$

Since $1 - v = d$ and $v / d = v / (i v) = 1 / i$:

$$a_{\overline{n}|} = \frac{1 - v^n}{i} = \frac{1 - (1 + i)^{-n}}{i}$$

#### 2. The Present Value of an Annuity-Due ($\ddot{a}_{\overline{n}|}$)
For an annuity-due, payments occur at $t = 0, 1, \dots, n - 1$:

$$\ddot{a}_{\overline{n}|} = v^0 + v^1 + v^2 + \dots + v^{n-1} = \sum_{t=0}^{n-1} v^t = \frac{1 - v^n}{1 - v}$$

Since $1 - v = d$:

$$\ddot{a}_{\overline{n}|} = \frac{1 - v^n}{d} = \frac{1 - (1 + i)^{-n}}{d}$$

#### Fundamental Relationship Between $a_{\overline{n}|}$ and $\ddot{a}_{\overline{n}|}$
Because each payment in an annuity-due occurs exactly one period earlier than in an annuity-immediate, its present value is scaled by $(1 + i)$:

$$\ddot{a}_{\overline{n}|} = (1 + i) a_{\overline{n}|}$$

Alternatively, separating the initial cash payment at $t = 0$:

$$\ddot{a}_{\overline{n}|} = 1 + a_{\overline{n-1}|}$$

### Accumulated Values at Maturity: $s_{\overline{n}|}$ and $\ddot{s}_{\overline{n}|}$
The accumulated value at the end of the term ($t = n$) is obtained by compounding the present value forward by $(1 + i)^n$:

$$s_{\overline{n}|} = a_{\overline{n}|} (1 + i)^n = \frac{1 - v^n}{i} (1 + i)^n = \frac{(1 + i)^n - 1}{i}$$

$$\ddot{s}_{\overline{n}|} = \ddot{a}_{\overline{n}|} (1 + i)^n = \frac{(1 + i)^n - 1}{d} = (1 + i) s_{\overline{n}|}$$

Inverting these equations gives the classical identity connecting present value and accumulated value:

$$\frac{1}{a_{\overline{n}|}} - \frac{1}{s_{\overline{n}|}} = \frac{i}{1 - v^n} - \frac{i}{(1 + i)^n - 1} = i$$

The periodic capital recovery payment exceeds the periodic sinking fund deposit by exactly the interest rate $i$!

## 2.2 Continuous Annuities and Sub-Period Payment Annuities ($a_{\overline{n}|}^{(m)}$)

### 1. Continuous Annuities ($\bar{a}_{\overline{n}|}$)
When capital is paid continuously at a uniform rate of $1$ unit per year over $n$ years (so that an infinitesimal amount $dt$ is paid during each interval $[t, t + dt]$):

$$\bar{a}_{\overline{n}|} = \int_0^n v^t\,dt = \int_0^n e^{-\delta t}\,dt = \left[ \frac{-e^{-\delta t}}{\delta} \right]_0^n = \frac{1 - e^{-\delta n}}{\delta} = \frac{1 - v^n}{\delta}$$

$$\bar{s}_{\overline{n}|} = \bar{a}_{\overline{n}|} (1 + i)^n = \frac{(1 + i)^n - 1}{\delta}$$

### 2. Annuities Payable $m$-thly ($a_{\overline{n}|}^{(m)}$)
When an annuity pays a total of $1$ unit per year in $m$ equal installments of $1/m$ at the end of each $m$-th of a year:

$$a_{\overline{n}|}^{(m)} = \frac{1}{m} \sum_{k=1}^{m \cdot n} v^{k/m} = \frac{1}{m} v^{1/m} \frac{1 - (v^{1/m})^{mn}}{1 - v^{1/m}} = \frac{1 - v^n}{m (1 - v^{1/m}) v^{-1/m}} = \frac{1 - v^n}{m ((1 + i)^{1/m} - 1)}$$

Since $m [(1 + i)^{1/m} - 1] = i^{(m)}$:

$$a_{\overline{n}|}^{(m)} = \frac{1 - v^n}{i^{(m)}}$$

Similarly, for payments made at the beginning of each $m$-th of a year:

$$\ddot{a}_{\overline{n}|}^{(m)} = \frac{1 - v^n}{d^{(m)}}$$

Notice that the numerator $1 - v^n$ remains invariant across all formulations; only the denominator shifts among $i, d, i^{(m)}, d^{(m)},$ and $\delta$.

## 2.3 Perpetuities and Deferred Annuities

### Perpetuities
A **perpetuity** is an annuity whose cash flows continue indefinitely ($n \to \infty$).
Because $\lim_{n \to \infty} v^n = 0$ for any positive interest rate $i > 0$:

$$a_{\overline{\infty}|} = \lim_{n \to \infty} \frac{1 - v^n}{i} = \frac{1}{i}$$

$$\ddot{a}_{\overline{\infty}|} = \lim_{n \to \infty} \frac{1 - v^n}{d} = \frac{1}{d} = 1 + \frac{1}{i}$$

$$\bar{a}_{\overline{\infty}|} = \lim_{n \to \infty} \frac{1 - v^n}{\delta} = \frac{1}{\delta}$$

Perpetuities provide the mathematical foundation for capitalizing common stock equity dividends under the Gordon Growth Model, valuing preferred shares, and establishing permanent university endowment funds.

### Deferred Annuities
An annuity deferred by $m$ periods, denoted ${}_{m|} a_{\overline{n}|}$, is an annuity of $n$ payments where the first payment commences after an initial deferral latency of $m$ periods (first payment at time $t = m + 1$):

$${}_{m|} a_{\overline{n}|} = v^m \cdot a_{\overline{n}|} = v^{m+1} + v^{m+2} + \dots + v^{m+n}$$

Equivalently, expressed as the difference between two immediate annuities:

$${}_{m|} a_{\overline{n}|} = a_{\overline{m+n}|} - a_{\overline{m}|}$$

Similarly, for deferred annuities-due:

$${}_{m|} \ddot{a}_{\overline{n}|} = v^m \cdot \ddot{a}_{\overline{n}|} = \ddot{a}_{\overline{m+n}|} - \ddot{a}_{\overline{m}|}$$

## 2.4 Arithmetically and Geometrically Varying Annuities

Real-world cash flows frequently increase or decrease over time to adjust for inflation or growing corporate revenues.

### 1. Arithmetically Increasing Annuity-Immediate ($(Ia)_{\overline{n}|}$)
An annuity where payments increase in an arithmetic progression: the payment at time $t = 1$ is $1$, at time $t = 2$ is $2$, and at time $t = n$ is $n$:

$$(Ia)_{\overline{n}|} = \sum_{t=1}^n t \cdot v^t = 1 v^1 + 2 v^2 + 3 v^3 + \dots + n v^n$$

To evaluate this arithmetico-geometric series, multiply by $(1 + i)$:
$$(1 + i) (Ia)_{\overline{n}|} = 1 + 2 v^1 + 3 v^2 + \dots + n v^{n-1}$$
Subtract $(Ia)_{\overline{n}|}$:
$$i (Ia)_{\overline{n}|} = 1 + v^1 + v^2 + \dots + v^{n-1} - n v^n = \ddot{a}_{\overline{n}|} - n v^n$$
Dividing by $i$:

$$(Ia)_{\overline{n}|} = \frac{\ddot{a}_{\overline{n}|} - n v^n}{i}$$

Similarly, for an increasing annuity-due where payments of $1, 2, \dots, n$ occur at times $t = 0, 1, \dots, n - 1$:

$$(I\ddot{a})_{\overline{n}|} = (1 + i) (Ia)_{\overline{n}|} = \frac{\ddot{a}_{\overline{n}|} - n v^n}{d}$$

### 2. Arithmetically Decreasing Annuity-Immediate ($(Da)_{\overline{n}|}$)
An annuity where payments start at $n$ and decrease by $1$ unit each period: payments are $n$ at $t = 1$, $n - 1$ at $t = 2$, down to $1$ at $t = n$:

$$(Da)_{\overline{n}|} = \sum_{t=1}^n (n - t + 1) v^t = \frac{n - a_{\overline{n}|}}{i}$$

Notice that for any $n$, the sum of the increasing and decreasing annuity satisfies:
$$(Ia)_{\overline{n}|} + (Da)_{\overline{n}|} = (n + 1) a_{\overline{n}|}$$

### 3. Geometrically Increasing Annuity
Suppose an annuity pays $1$ unit at $t = 1$, and subsequent payments grow at a geometric rate $g$ per period (so payment at time $t$ is $(1 + g)^{t-1}$):

$$PV = \sum_{t=1}^n (1 + g)^{t-1} v^t = \frac{v}{1 + g} \sum_{t=1}^n \left( \frac{1 + g}{1 + i} \right)^t$$

Define an adjusted interest rate $i^*$:
$$1 + i^* = \frac{1 + i}{1 + g} \implies i^* = \frac{i - g}{1 + g}$$
The present value collapses to an equivalent level annuity evaluated at rate $i^*$:

$$PV = \frac{a_{\overline{n}|i^*}}{1 + g}$$

If $g = i$, $i^* = 0$, and $PV = n \cdot v = \frac{n}{1 + i}$.

## 2.5 Loan Amortization Mechanics: Prospective and Retrospective Balances

When a loan of principal amount $L$ is repaid through $n$ periodic level payments of amount $P$ at interest rate $i$, the basic equation of value is:

$$L = P \cdot a_{\overline{n}|i} \implies P = \frac{L}{a_{\overline{n}|i}}$$

At any intermediate epoch $t \in \{1, 2, \dots, n\}$, the borrower has made $t$ payments, with $n - t$ payments remaining. Actuaries compute the **Outstanding Loan Balance** $B_t$ through two equivalent formulations:

### 1. The Prospective Method
The outstanding balance $B_t$ equals the actuarial present value at time $t$ of all remaining future loan payments:

$$B_t = P \cdot a_{\overline{n - t}|i}$$

### 2. The Retrospective Method
The outstanding balance $B_t$ equals the accumulated value of the original loan principal minus the accumulated value of all past payments already made:

$$B_t = L (1 + i)^t - P \cdot s_{\overline{t}|i}$$

#### Proof of Equivalence
Substitute $L = P a_{\overline{n}|}$:
$$B_t = P a_{\overline{n}|} (1 + i)^t - P s_{\overline{t}|} = P \left[ \frac{1 - v^n}{i} (1 + i)^t - \frac{(1 + i)^t - 1}{i} \right]$$
$$= P \left[ \frac{(1 + i)^t - v^{n-t} - (1 + i)^t + 1}{i} \right] = P \left[ \frac{1 - v^{n-t}}{i} \right] = P \cdot a_{\overline{n - t}|i}$$
The prospective and retrospective balances are algebraically identical.

### Decomposition into Principal and Interest
Each periodic installment $P$ is partitioned into two components: an interest charge on the outstanding balance and a principal reduction:
$$P = I_t + PR_t$$
1. **Interest Paid in Period $t$**:
   $$I_t = i \cdot B_{t-1} = i \cdot P a_{\overline{n - t + 1}|} = i \cdot P \frac{1 - v^{n - t + 1}}{i} = P (1 - v^{n - t + 1})$$
2. **Principal Repaid in Period $t$**:
   $$PR_t = P - I_t = P - P(1 - v^{n - t + 1}) = P \cdot v^{n - t + 1}$$

Notice that successive principal repayments form an expanding geometric progression:
$$PR_{t+1} = PR_t \cdot (1 + i)$$
In early years, payments are dominated by interest ($I_t$); in later years, payments are dominated by principal amortization ($PR_t$).

## Fully worked question 1: Constructing a Complete Loan Amortization Schedule and Balance Reconciliation

### Question
An industrial manufacturing firm secures a commercial bank term loan of $L = 500,000\text{ BDT}$ to install an automated packaging robot. The loan is amortized via $n = 5$ equal annual installments payable at the end of each year at an effective annual interest rate of $i = 9.00\%$ ($i = 0.09$).

Perform the following calculations:
1. Compute the level annual installment payment $P$.
2. Compute the outstanding balance at the end of Year 3 ($B_3$) using the **Prospective Method**.
3. Compute the outstanding balance at the end of Year 3 ($B_3$) using the **Retrospective Method**, verifying exact equality.
4. Construct the complete 5-year loan amortization schedule, showing for each year $t = 1, 2, 3, 4, 5$:
   - Beginning balance $B_{t-1}$
   - Total payment $P$
   - Interest paid $I_t$
   - Principal repaid $PR_t$
   - Ending balance $B_t$
5. Verify that the sum of all principal repayments equals the original loan principal ($L = 500,000\text{ BDT}$).

### Solution, step 1: Compute annual installment payment $P$
Given $L = 500,000$, $n = 5$, and $i = 0.09$:
$$v = (1.09)^{-1} \approx 0.917431$$
$$v^5 = (1.09)^{-5} \approx 0.649931$$
$$a_{\overline{5}|0.09} = \frac{1 - v^5}{i} = \frac{1 - 0.649931}{0.09} = \frac{0.350069}{0.09} \approx 3.889651$$

The annual installment payment is:
$$P = \frac{L}{a_{\overline{5}|0.09}} = \frac{500,000}{3.889651} \approx 128,546.21\text{ BDT}$$

### Solution, step 2: Outstanding balance at $t = 3$ via Prospective Method
At $t = 3$, $n - t = 5 - 3 = 2$ payments remain:
$$v^2 = (1.09)^{-2} \approx 0.841680$$
$$a_{\overline{2}|0.09} = \frac{1 - v^2}{0.09} = \frac{1 - 0.841680}{0.09} = \frac{0.158320}{0.09} \approx 1.759111$$
$$B_3 = P \cdot a_{\overline{2}|0.09} = 128,546.21 \times 1.759111 \approx 226,126.96\text{ BDT}$$

### Solution, step 3: Outstanding balance at $t = 3$ via Retrospective Method
Under the retrospective method:
$$(1.09)^3 \approx 1.295029$$
$$s_{\overline{3}|0.09} = \frac{(1.09)^3 - 1}{0.09} = \frac{0.295029}{0.09} \approx 3.278100$$
$$L (1.09)^3 = 500,000 \times 1.295029 = 647,514.50\text{ BDT}$$
$$P \cdot s_{\overline{3}|0.09} = 128,546.21 \times 3.278100 = 421,387.48\text{ BDT}$$
$$B_3 = 647,514.50 - 421,387.48 = 226,127.02\text{ BDT}$$
Within rounding precision of $0.06\text{ BDT}$, the prospective and retrospective methods match identically!

### Solution, step 4: Construct the complete 5-year amortization schedule
- **Year 1**:
  - $B_0 = 500,000.00$
  - $I_1 = 0.09 \times 500,000.00 = 45,000.00$
  - $PR_1 = 128,546.21 - 45,000.00 = 83,546.21$
  - $B_1 = 500,000.00 - 83,546.21 = 416,453.79$
- **Year 2**:
  - $B_1 = 416,453.79$
  - $I_2 = 0.09 \times 416,453.79 = 37,480.84$
  - $PR_2 = 128,546.21 - 37,480.84 = 91,065.37$
  - $B_2 = 416,453.79 - 91,065.37 = 325,388.42$
- **Year 3**:
  - $B_2 = 325,388.42$
  - $I_3 = 0.09 \times 325,388.42 = 29,284.96$
  - $PR_3 = 128,546.21 - 29,284.96 = 99,261.25$
  - $B_3 = 325,388.42 - 99,261.25 = 226,127.17$
- **Year 4**:
  - $B_3 = 226,127.17$
  - $I_4 = 0.09 \times 226,127.17 = 20,351.45$
  - $PR_4 = 128,546.21 - 20,351.45 = 108,194.76$
  - $B_4 = 226,127.17 - 108,194.76 = 117,932.41$
- **Year 5**:
  - $B_4 = 117,932.41$
  - $I_5 = 0.09 \times 117,932.41 = 10,613.92$
  - $PR_5 = 128,546.21 - 10,613.92 = 117,932.29 \approx 117,932.41$
  - $B_5 = 0.00$

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Year $t$</th>
<th>Beginning Balance $B_{t-1}$</th>
<th>Payment $P$</th>
<th>Interest $I_t$</th>
<th>Principal $PR_t$</th>
<th>Ending Balance $B_t$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>500,000.00</td>
<td>128,546.21</td>
<td>45,000.00</td>
<td>83,546.21</td>
<td>416,453.79</td>
</tr>
<tr>
<td>2</td>
<td>416,453.79</td>
<td>128,546.21</td>
<td>37,480.84</td>
<td>91,065.37</td>
<td>325,388.42</td>
</tr>
<tr>
<td>3</td>
<td>325,388.42</td>
<td>128,546.21</td>
<td>29,284.96</td>
<td>99,261.25</td>
<td>226,127.17</td>
</tr>
<tr>
<td>4</td>
<td>226,127.17</td>
<td>128,546.21</td>
<td>20,351.45</td>
<td>108,194.76</td>
<td>117,932.41</td>
</tr>
<tr>
<td>5</td>
<td>117,932.41</td>
<td>128,546.21</td>
<td>10,613.92</td>
<td>117,932.29</td>
<td>0.00</td>
</tr>
</tbody>
</table>
</div>

### Solution, step 5: Verify principal summation
$$\sum_{t=1}^5 PR_t = 83,546.21 + 91,065.37 + 99,261.25 + 108,194.76 + 117,932.29 = 499,999.88 \approx 500,000\text{ BDT}$$
The principal is completely amortized to zero over the 5-year loan term.

## Fully worked question 2: Valuation of Arithmetically and Geometrically Varying Cash Flows

### Question
An infrastructure concession consortium bids to finance a toll bridge under a Public-Private Partnership (PPP). The financial engineering model projects the following cash flow profiles over an operating concession of $n = 15\text{ years}$ at a constant discount rate of $i = 7.00\%$ ($i = 0.07$):

**Project Alpha (Arithmetic Expansion)**:
Toll revenues start at $10,000,000\text{ BDT}$ at $t = 1$ and increase by an arithmetic increment of $1,000,000\text{ BDT}$ in each subsequent year (i.e., $11\text{M}$ at $t=2$, $12\text{M}$ at $t=3$, up to $24\text{M}$ at $t=15$).

**Project Beta (Geometric Expansion)**:
Toll revenues start at $10,000,000\text{ BDT}$ at $t = 1$ and increase at a compound geometric growth rate of $g = 4.00\%$ per year (i.e., $10(1.04)^{t-1}\text{M}$ at year $t$).

Perform the following calculations:
1. Compute the present value of Project Alpha using the $(Ia)_{\overline{n}|}$ formulation.
2. Compute the present value of Project Beta using the adjusted interest rate $i^*$ formulation.
3. Determine which revenue model yields higher economic present value to the concessionaire.

### Solution, step 1: Value Project Alpha (Arithmetic Expansion)
Let $P_t = 10 + (t - 1) \times 1 = 9 + t$ (in millions of BDT).
Decompose Project Alpha into a level annuity of $9\text{M}$ and an increasing annuity $(Ia)_{\overline{15}|}$ of $1\text{M}$:
$$PV_\alpha = 9 \cdot a_{\overline{15}|0.07} + 1 \cdot (Ia)_{\overline{15}|0.07}$$

Compute basic actuarial values for $n = 15, i = 0.07$:
$$v = (1.07)^{-1} \approx 0.934579$$
$$v^{15} = (1.07)^{-15} \approx 0.362446$$
$$a_{\overline{15}|0.07} = \frac{1 - v^{15}}{0.07} = \frac{1 - 0.362446}{0.07} = \frac{0.637554}{0.07} \approx 9.107914$$
$$\ddot{a}_{\overline{15}|0.07} = (1.07) a_{\overline{15}|0.07} = 1.07 \times 9.107914 \approx 9.745468$$

Now evaluate $(Ia)_{\overline{15}|0.07}$:
$$(Ia)_{\overline{15}|0.07} = \frac{\ddot{a}_{\overline{15}|} - 15 v^{15}}{i} = \frac{9.745468 - 15(0.362446)}{0.07}$$
$$15 \times 0.362446 = 5.436690$$
$$\text{Numerator} = 9.745468 - 5.436690 = 4.308778$$
$$(Ia)_{\overline{15}|0.07} = \frac{4.308778}{0.07} \approx 61.553971$$

Aggregate Project Alpha present value:
$$PV_\alpha = 9(9.107914) + 1(61.553971) = 81.971226 + 61.553971 = 143.525197\text{ million BDT}$$
$$PV_\alpha \approx 143,525,197\text{ BDT}$$

### Solution, step 2: Value Project Beta (Geometric Expansion)
Project Beta pays $C_t = 10(1 + g)^{t-1}$ with $g = 0.04$ and $i = 0.07$:
$$i^* = \frac{i - g}{1 + g} = \frac{0.07 - 0.04}{1 + 0.04} = \frac{0.03}{1.04} \approx 0.02884615$$

Compute the present value:
$$PV_\beta = \frac{10}{1 + g} a_{\overline{15}|i^*} = \frac{10}{1.04} \left[ \frac{1 - (1 + i^*)^{-15}}{i^*} \right]$$
Calculate $(1 + i^*)^{-15}$:
$$1 + i^* = \frac{1.07}{1.04} \approx 1.02884615$$
$$(1 + i^*)^{-15} = \left(\frac{1.04}{1.07}\right)^{15} = (0.9719626)^{15} \approx 0.651759$$
$$1 - (1 + i^*)^{-15} = 1 - 0.651759 = 0.348241$$
$$a_{\overline{15}|i^*} = \frac{0.348241}{0.02884615} \approx 12.07235$$
Now multiply by $10 / 1.04$:
$$PV_\beta = \frac{10}{1.04} \times 12.07235 = 9.615385 \times 12.07235 \approx 116.0803\text{ million BDT}$$
$$PV_\beta \approx 116,080,288\text{ BDT}$$

### Solution, step 3: Comparison
- Project Alpha (Arithmetic increment): $PV = 143,525,197\text{ BDT}$
- Project Beta (Geometric growth): $PV = 116,080,288\text{ BDT}$
- **Conclusion**: Project Alpha delivers **$27,444,909\text{ BDT}$** higher present value ($+23.6\%$) because its absolute annual cash additions ($+1\text{M}$ each year, representing $10\%$ growth initially) expand cash flows significantly faster in early-to-mid years than the compound $4\%$ growth rate.

## Fully worked question 3: Multi-Frequency Annuity Valuations ($a_{\overline{n}|}^{(m)}$) and Continuous Approximation

### Question
A retiree purchases an immediate annuity that guarantees payments of $120,000\text{ BDT}$ per year for $n = 20\text{ years}$. The effective annual interest rate is $i = 6.00\%$ ($i = 0.06$).

Perform the following calculations:
1. Compute the present value of the annuity if payments are made:
   - Annually ($m = 1$)
   - Semi-annually in installments of $60,000\text{ BDT}$ ($m = 2$)
   - Monthly in installments of $10,000\text{ BDT}$ ($m = 12$)
   - Continuously at a uniform rate of $120,000\text{ BDT/year}$ ($m \to \infty$)
2. Compute the exact dollar premium required for monthly payment timing compared to annual payment timing.
3. Apply Woolhouse's three-term Euler-Maclaurin expansion formula:
   $$a_{\overline{n}|}^{(m)} \approx a_{\overline{n}|} + \frac{m - 1}{2m} (1 - v^n)$$
   and assess its approximation error relative to the exact monthly present value.

### Solution, step 1: Compute exact present values across payment frequencies
For $n = 20$ and $i = 0.06$:
$$v = (1.06)^{-1} \approx 0.943396$$
$$v^{20} = (1.06)^{-20} \approx 0.311805$$
$$1 - v^{20} = 1 - 0.311805 = 0.688195$$

1. **Annual Payment ($m = 1$)**:
   $$a_{\overline{20}|} = \frac{0.688195}{0.06} \approx 11.46992$$
   $$PV_{\text{annual}} = 120,000 \times 11.46992 \approx 1,376,390\text{ BDT}$$

2. **Semi-Annual Payment ($m = 2$)**:
   $$i^{(2)} = 2 [(1.06)^{0.5} - 1] = 2 [1.029563 - 1] = 0.059126$$
   $$a_{\overline{20}|}^{(2)} = \frac{0.688195}{0.059126} \approx 11.63946$$
   $$PV_{\text{semi}} = 120,000 \times 11.63946 \approx 1,396,735\text{ BDT}$$

3. **Monthly Payment ($m = 12$)**:
   $$i^{(12)} = 12 [(1.06)^{1/12} - 1] = 12 [1.00486755 - 1] = 0.0584106$$
   $$a_{\overline{20}|}^{(12)} = \frac{0.688195}{0.0584106} \approx 11.78202$$
   $$PV_{\text{monthly}} = 120,000 \times 11.78202 \approx 1,413,842\text{ BDT}$$

4. **Continuous Payment ($m \to \infty$)**:
   $$\delta = \ln(1.06) \approx 0.0582689$$
   $$\bar{a}_{\overline{20}|} = \frac{0.688195}{0.0582689} \approx 11.81067$$
   $$PV_{\text{continuous}} = 120,000 \times 11.81067 \approx 1,417,280\text{ BDT}$$

### Solution, step 2: Incremental cost of monthly payments
$$PV_{\text{monthly}} - PV_{\text{annual}} = 1,413,842 - 1,376,390 = 37,452\text{ BDT}$$
The insurer must charge an additional **$37,452\text{ BDT}$** ($+2.72\%$) to provide monthly payouts because the retiree receives funds earlier in each policy year, forfeiting intra-year interest to the company.

### Solution, step 3: Evaluate Woolhouse's Euler-Maclaurin expansion
Using Woolhouse's formula for $m = 12$:
$$\frac{m - 1}{2m} = \frac{11}{24} \approx 0.458333$$
$$a_{\overline{20}|}^{(12)} \approx a_{\overline{20}|} + \frac{11}{24}(1 - v^{20}) = 11.46992 + 0.458333(0.688195) = 11.46992 + 0.31542 = 11.78534$$
Multiply by annual benefit of $120,000$:
$$PV_{\text{Woolhouse}} = 120,000 \times 11.78534 \approx 1,414,241\text{ BDT}$$
Approximation error:
$$\text{Error} = 1,414,241 - 1,413,842 = +399\text{ BDT}$$
$$\% \text{Error} = \frac{399}{1,413,842} \times 100\% \approx 0.028\%$$
Woolhouse's formula achieves $99.97\%$ numerical accuracy without requiring nominal rate root extraction!
"""

(DRAFT_DIR / "unit-1.md").write_text(unit_1.strip() + "\n", encoding="utf-8")
print("Unit 1 written.")

(DRAFT_DIR / "unit-2.md").write_text(unit_2.strip() + "\n", encoding="utf-8")
print("Unit 2 written.")
