#!/usr/bin/env python3
"""
Expand Units 1 and 2 of Actuarial Statistics and Mathematical Demography.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"

u1_path = DRAFT_DIR / "unit-1.md"
u1_text = u1_path.read_text(encoding="utf-8")

u1_add = r"""
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
"""

idx1 = u1_text.find("## Fully worked question 1:")
u1_text = u1_text[:idx1] + u1_add.strip() + "\n\n" + u1_text[idx1:]
u1_path.write_text(u1_text, encoding="utf-8")
print("Unit 1 expanded.")

u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")

u2_add = r"""
## 2.6 Sinking Fund Mechanics and Two-Rate Investment Yields

In institutional project finance and corporate bond indentures, a borrower who borrows principal $L$ for $n$ years may be contractually prohibited from amortizing the loan directly through installment payments to the creditor. Instead, the creditor requires the borrower to pay annual interest $i \cdot L$ at the end of each year, and repay the entire principal $L$ as a single bullet lump sum at maturity $t = n$.

To accumulate the principal $L$ by time $n$, the borrower establishes a separate **Sinking Fund** with a third-party depository trust, making $n$ annual end-of-year deposits of amount $D$ that accumulate at a sinking fund interest rate $j$.

### The Sinking Fund Equation of Value
The sinking fund deposits must accumulate to $L$ at time $n$:

$$D \cdot s_{\overline{n}|j} = L \implies D = \frac{L}{s_{\overline{n}|j}} = \frac{L \cdot j}{(1 + j)^n - 1}$$

The borrower's total annual financial outlay $E$ consists of two distinct components:
1. The annual interest payment to the lender: $i \cdot L$.
2. The annual deposit into the sinking fund: $D = L / s_{\overline{n}|j}$.

$$E = i \cdot L + \frac{L}{s_{\overline{n}|j}} = L \left( i + \frac{1}{s_{\overline{n}|j}} \right)$$

### The Sinking Fund General Yield Rate ($i^*$)
Recall that under standard loan amortization at rate $j$:
$$\frac{1}{a_{\overline{n}|j}} = j + \frac{1}{s_{\overline{n}|j}} \implies \frac{1}{s_{\overline{n}|j}} = \frac{1}{a_{\overline{n}|j}} - j$$
Substituting into the total annual outlay:

$$E = L \left( i - j + \frac{1}{a_{\overline{n}|j}} \right)$$

If the sinking fund earns the exact same interest rate as the loan ($j = i$):
$$E = L \left( i + \frac{1}{a_{\overline{n}|i}} - i \right) = \frac{L}{a_{\overline{n}|i}}$$
The annual outlay collapses identically to the standard level amortization payment!

However, in real commercial markets, the borrowing rate exceeds the safe reinvestment rate ($i > j$). The overall effective annual borrowing cost $i^*$ to the borrower satisfies:
$$L = E \cdot a_{\overline{n}|i^*} \implies a_{\overline{n}|i^*} = \frac{L}{E} = \frac{1}{i + \frac{1}{s_{\overline{n}|j}}}$$
Because $j < i$, the sinking fund deposit $D$ is larger than under equal rates, raising the borrower's effective cost of capital $i^*$ strictly above the nominal loan rate $i$.

## 2.7 Continuous Varying Annuities and General Polynomial Payment Streams

When cash flows are paid continuously at a time-varying rate $\rho(t)$ over a time horizon $[0, n]$, the present value is given by the continuous integral:

$$PV = \int_0^n \rho(t) v^t\,dt = \int_0^n \rho(t) e^{-\delta t}\,dt$$

### 1. Continuously Increasing Continuous Annuity ($(\bar{I}\bar{a})_{\overline{n}|}$)
When the payment rate increases continuously at a unit rate per year ($\rho(t) = t$):

$$(\bar{I}\bar{a})_{\overline{n}|} = \int_0^n t e^{-\delta t}\,dt$$

Applying integration by parts with $u = t$ and $dv = e^{-\delta t}dt$:
$$(\bar{I}\bar{a})_{\overline{n}|} = \left[ -\frac{t e^{-\delta t}}{\delta} \right]_0^n + \frac{1}{\delta} \int_0^n e^{-\delta t}\,dt = -\frac{n e^{-\delta n}}{\delta} + \frac{1 - e^{-\delta n}}{\delta^2}$$
Since $\bar{a}_{\overline{n}|} = \frac{1 - e^{-\delta n}}{\delta}$ and $v^n = e^{-\delta n}$:

$$(\bar{I}\bar{a})_{\overline{n}|} = \frac{\bar{a}_{\overline{n}|} - n v^n}{\delta}$$

The accumulated value at time $n$ is:

$$(\bar{I}\bar{s})_{\overline{n}|} = (\bar{I}\bar{a})_{\overline{n}|} e^{\delta n} = \frac{\bar{s}_{\overline{n}|} - n}{\delta}$$

### 2. General Polynomial Cash Flows ($\rho(t) = t^k$)
For arbitrary integer powers $k \ge 1$:
$$I_k(n) = \int_0^n t^k e^{-\delta t}\,dt = \frac{k!}{\delta^{k+1}} \left[ 1 - e^{-\delta n} \sum_{r=0}^k \frac{(\delta n)^r}{r!} \right]$$
This analytical expression enables exact closed-form valuations for complex industrial manufacturing ramp-up cash flows and oil reservoir depletion production profiles.

## 2.8 Consumer Credit Financing: The Rule of 78 and Truth in Lending

In consumer retail installment finance (e.g., automobile loans and personal electronics financing), lenders historically computed interest using the **Add-On Interest Method** rather than compound interest amortization.

### The Add-On Interest Formulation
Let principal $L$ be borrowed for $n$ months at an annual add-on interest rate $r_{\text{add}}$.
Total finance charge (interest):
$$I_{\text{total}} = L \cdot r_{\text{add}} \cdot \left(\frac{n}{12}\right)$$
Total amount to be repaid:
$$M = L + I_{\text{total}}$$
The flat monthly payment is:
$$P = \frac{M}{n} = \frac{L + I_{\text{total}}}{n}$$

The true Annual Percentage Rate ($APR$) of an add-on loan is substantially higher than the stated add-on rate $r_{\text{add}}$:

$$APR \approx \frac{2 n}{n + 1} r_{\text{add}}$$

For a 12-month loan, $APR \approx \frac{24}{13} r_{\text{add}} \approx 1.85 \times r_{\text{add}}$. A stated $10\%$ add-on loan carries an actual compound interest cost of over $18.5\%$!

### The Rule of 78 (Sum-of-the-Digits Method)
If a consumer prepays an installment loan before maturity (e.g., pays off a 12-month loan after $k$ months), the lender must compute an interest rebate. The **Rule of 78** allocates total interest across months proportionally to the number of remaining monthly installments.

For a 12-month loan, the sum of the digits from $1$ to $12$ is:
$$\sum_{j=1}^{12} j = \frac{12 \times 13}{2} = 78$$
- Month 1 receives $12/78$ of total interest.
- Month 2 receives $11/78$ of total interest.
- Month $k$ receives $(n - k + 1)/78$ of total interest.

If the loan is prepaid after $k$ months, the fraction of total interest earned by the lender is:

$$\text{Fraction Earned} = \frac{\sum_{j=1}^k (n - j + 1)}{\frac{n(n + 1)}{2}} = \frac{k [2n - k + 1]}{n(n + 1)}$$

The unearned interest rebate credited to the consumer is:

$$\text{Rebate} = I_{\text{total}} \times \frac{(n - k)(n - k + 1)}{n(n + 1)}$$

The Rule of 78 heavily front-loads interest charges into early months, penalizing early prepayment relative to true actuarial amortization.

## 2.9 Makeham's Formula for Bond Valuation and Amortization of Premium/Discount

A standard fixed-income bond promises $n$ coupon payments of amount $C \cdot g$ at regular intervals, plus redemption of par/redemption value $C$ at maturity $t = n$, where $g$ is the coupon rate per period and $i$ is the yield rate per period.

The standard bond price formula is:
$$P = C \cdot g \cdot a_{\overline{n}|i} + C \cdot v^n$$

### Derivation of Makeham's Formula
Let $K = C \cdot v^n$ denote the present value of the redemption payment.
Since $a_{\overline{n}|} = \frac{1 - v^n}{i} = \frac{1 - K/C}{i}$, substitute into the bond price equation:

$$P = C \cdot g \left( \frac{1 - K/C}{i} \right) + K = \frac{g}{i} (C - K) + K$$

$$P = K + \frac{g}{i} (C - K)$$

This is **Makeham's Formula** (formulated by William Makeham in 1874). Makeham’s formula has profound elegance:
- If the coupon rate equals the yield rate ($g = i$): $P = K + (C - K) = C$ (the bond sells at par).
- If the coupon rate exceeds the yield rate ($g > i$): $P > C$ (the bond sells at a **premium**).
- If the coupon rate is below the yield rate ($g < i$): $P < C$ (the bond sells at a **discount**).

The premium amount $P - C = (C \cdot g - C \cdot i) a_{\overline{n}|i}$ is amortized systematically across the bond’s life, mirroring loan amortization schedules.
"""

idx2 = u2_text.find("## Fully worked question 1:")
u2_text = u2_text[:idx2] + u2_add.strip() + "\n\n" + u2_text[idx2:]
u2_path.write_text(u2_text, encoding="utf-8")
print("Unit 2 expanded.")
