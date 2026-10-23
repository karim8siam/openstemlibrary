#!/usr/bin/env python3
"""
Generate Units 5 and 6 for Actuarial Statistics and Mathematical Demography.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_5 = r"""# Unit 5: Life Annuities: Continuous, Discrete, Varying & Guaranteed Contracts

## 5.1 The Stochastic Present Value Random Variable for Life Annuities

A **life annuity** is a financial contract that guarantees a sequence of periodic payments made to a designated beneficiary (the annuitant $(x)$) for as long as the annuitant remains alive. Life annuities serve as the preeminent institutional instrument for converting accumulated retirement wealth into guaranteed, lifelong income, eliminating the risk of outliving one’s financial capital (**longevity risk**).

Unlike an annuity-certain (Unit 2), where the number of payments $n$ is fixed deterministically by contract, the duration of a life annuity is governed by the stochastic biological lifetime of the individual.

### Continuous Whole Life Annuity: $\bar{a}_x$
In a continuous whole life annuity, payments are made continuously at a constant rate of $1$ unit per year until the exact moment of death $T_x$. The present value of the payment stream is a continuous random variable denoted $Y$:

$$Y = \bar{a}_{\overline{T_x}|} = \int_0^{T_x} v^t\,dt = \frac{1 - v^{T_x}}{\delta} = \frac{1 - e^{-\delta T_x}}{\delta}$$

The **Actuarial Present Value (APV)** of this contract, denoted $\bar{a}_x$, is the expected value of $Y$:

$$\bar{a}_x = \mathbb{E}[Y] = \mathbb{E}\left[ \frac{1 - e^{-\delta T_x}}{\delta} \right] = \int_0^\infty \bar{a}_{\overline{t}|} f_x(t)\,dt = \int_0^\infty \left( \int_0^t v^s\,ds \right) {}_t p_x \mu_{x+t}\,dt$$

Reversing the order of integration yields the standard operational integral:

$$\bar{a}_x = \int_0^\infty v^t {}_t p_x\,dt = \int_0^\infty e^{-\delta t} {}_t p_x\,dt$$

The actuarial present value is simply the discounted sum of the probabilities of being alive to receive each infinitesimal payment!

### Discrete Whole Life Annuity-Due: $\ddot{a}_x$
In practical private pension schemes and life insurance premium payment schedules, cash flows occur in discrete annual installments. In a **Whole Life Annuity-Due**, payments of $1$ unit occur at the start of each year that the annuitant survives (at times $t = 0, 1, 2, \dots, K_x$, where $K_x = \lfloor T_x \rfloor$ is the curtate future lifetime).

The present value random variable $Y$ is:

$$Y = \ddot{a}_{\overline{K_x + 1}|} = \frac{1 - v^{K_x + 1}}{d}$$

The Actuarial Present Value, denoted $\ddot{a}_x$, is the expected value of $Y$:

$$\ddot{a}_x = \mathbb{E}[Y] = \sum_{k=0}^\infty \ddot{a}_{\overline{k+1}|} P(K_x = k) = \sum_{k=0}^\infty \left( \sum_{t=0}^k v^t \right) {}_k| q_x$$

Interchanging the order of summation yields the celebrated summation formula:

$$\ddot{a}_x = \sum_{t=0}^\infty v^t {}_t p_x = 1 + v p_x + v^2 {}_2 p_x + v^3 {}_3 p_x + \dots$$

### Discrete Whole Life Annuity-Immediate: $a_x$
If payments occur at the *end* of each year survived by $(x)$ (at times $t = 1, 2, \dots, K_x$):

$$a_x = \sum_{t=1}^\infty v^t {}_t p_x = v p_x + v^2 {}_2 p_x + v^3 {}_3 p_x + \dots$$

Because the annuity-due includes an immediate upfront payment of $1$ unit at time $0$, the fundamental relationship connecting immediate and due annuities is:

$$\ddot{a}_x = 1 + a_x$$

## 5.2 Fundamental Equivalence Theorems Between Insurances and Annuities

In financial economics, a risk-free bond can be decomposed into coupon streams and principal redemption. In actuarial life contingencies, a profound structural duality connects life insurance contracts and life annuity contracts.

### Discrete Equivalence Theorem: $A_x = 1 - d \ddot{a}_x$
Consider the random variable $Y = \ddot{a}_{\overline{K_x + 1}|} = \frac{1 - v^{K_x + 1}}{d}$.
Recall from Unit 4 that the present value random variable for a discrete whole life insurance is $Z = v^{K_x + 1}$.
Rearranging algebraically:

$$d \cdot Y = 1 - Z \implies Z = 1 - d \cdot Y$$

Taking expectations on both sides:

$$\mathbb{E}[Z] = 1 - d \cdot \mathbb{E}[Y]$$

$$A_x = 1 - d \cdot \ddot{a}_x \iff \ddot{a}_x = \frac{1 - A_x}{d}$$

#### Financial Economic Intuition
If an investor deposits $1$ unit of capital into an account earning interest at effective discount rate $d$:
- The account generates an annual interest dividend of $d$ units paid in advance at the start of each year for life, which is precisely an annuity-due of $d \ddot{a}_x$.
- Upon the death of the investor, the principal of $1$ unit is returned to the estate, which has present value $1 \cdot A_x$.
- By the conservation of financial value, the initial $1$ unit of capital must equal the sum of the dividend stream and the death benefit: $1 = d \ddot{a}_x + A_x$.

### Continuous Equivalence Theorem: $\bar{A}_x = 1 - \delta \bar{a}_x$
Similarly, in continuous time:
$$Y = \bar{a}_{\overline{T_x}|} = \frac{1 - e^{-\delta T_x}}{\delta} = \frac{1 - Z}{\delta} \implies Z = 1 - \delta \cdot Y$$
Taking expectations:

$$\bar{A}_x = 1 - \delta \cdot \bar{a}_x \iff \bar{a}_x = \frac{1 - \bar{A}_x}{\delta}$$

### Variance Relationships Between Annuities and Insurances
Because $Y = \frac{1 - Z}{d}$, the variance of the life annuity present value random variable is directly proportional to the variance of the life insurance random variable:

$$\text{Var}(Y) = \text{Var}\left( \frac{1 - Z}{d} \right) = \frac{1}{d^2} \text{Var}(Z) = \frac{{}^2 A_x - (A_x)^2}{d^2}$$

In continuous time:

$$\text{Var}(\bar{Y}) = \frac{\text{Var}(\bar{Z})}{\delta^2} = \frac{{}^2\bar{A}_x - (\bar{A}_x)^2}{\delta^2}$$

These identities permit the immediate derivation of annuity variances without performing separate second-moment integrations.

## 5.3 Temporary Life Annuities and Commutation Column $N_x$

A **Temporary Life Annuity** restricts payments to a maximum horizon of $n$ years, terminating upon the earlier of the death of $(x)$ or the expiration of $n$ years.

### 1. Temporary Life Annuity-Due: $\ddot{a}_{x:\overline{n}|}$
Payments of $1$ unit occur at times $t = 0, 1, \dots, n - 1$ provided $(x)$ is alive:

$$\ddot{a}_{x:\overline{n}|} = \sum_{t=0}^{n-1} v^t {}_t p_x = 1 + v p_x + v^2 {}_2 p_x + \dots + v^{n-1} {}_{n-1} p_x$$

### 2. Commutation Function Formulation: $N_x$
Recall that $D_x = v^x \ell_x$. Multiplying $\ddot{a}_{x:\overline{n}|}$ by $D_x / D_x$:
$$\ddot{a}_{x:\overline{n}|} = \frac{1}{D_x} \sum_{t=0}^{n-1} v^{x+t} \ell_{x+t} = \frac{D_x + D_{x+1} + \dots + D_{x+n-1}}{D_x}$$

Actuaries define the third-order commutation function $N_x$ as the accumulated sum of $D_y$ values from age $x$ to the terminal age of the table $\omega$:

$$N_x = \sum_{y=x}^{\omega - 1} D_y = \sum_{y=x}^{\omega - 1} v^y \ell_y$$

Using $N_x$, the whole life and temporary annuity values simplify to elegant algebraic ratios:

$$\ddot{a}_x = \frac{N_x}{D_x}$$

$$\ddot{a}_{x:\overline{n}|} = \frac{N_x - N_{x+n}}{D_x}$$

$$a_x = \frac{N_{x+1}}{D_x}$$

$$a_{x:\overline{n}|} = \frac{N_{x+1} - N_{x+n+1}}{D_x}$$

### 3. Equivalence with Endowment Insurance
The finite-term insurance-annuity duality relation is:

$$A_{x:\overline{n}|} = 1 - d \cdot \ddot{a}_{x:\overline{n}|}$$

$$\bar{A}_{x:\overline{n}|} = 1 - \delta \cdot \bar{a}_{x:\overline{n}|}$$

## 5.4 Deferred and Guaranteed Life Annuities

### 1. Deferred Life Annuities: ${}_{u|} \ddot{a}_x$
A deferred life annuity postpones benefit payments until after an initial waiting period of $u$ years. Payments commence at age $x + u$ and continue for life, provided $(x)$ survives the deferral window:

$${}_{u|} \ddot{a}_x = \sum_{t=u}^\infty v^t {}_t p_x = v^u {}_u p_x \ddot{a}_{x+u} = {}_u E_x \cdot \ddot{a}_{x+u} = \frac{N_{x+u}}{D_x}$$

Equivalently, expressed as the difference between a whole life annuity and a temporary annuity:
$${}_{u|} \ddot{a}_x = \ddot{a}_x - \ddot{a}_{x:\overline{u}|} = \frac{N_x}{D_x} - \frac{N_x - N_{x+u}}{D_x} = \frac{N_{x+u}}{D_x}$$

### 2. Guaranteed (Certain-and-Life) Annuities: $\ddot{a}_{\overline{x:\overline{n}|}}$
A primary customer objection to standard life annuities is the risk of dying shortly after policy inception (e.g., dying in year 1 after paying a huge purchase premium). To eliminate this risk, insurers offer **Guaranteed Annuities** (annuities with a guaranteed term certain).

An $n$-year guaranteed life annuity-due pays benefits for $n$ years *regardless of whether $(x)$ lives or dies*, and continues payments thereafter for life if $(x)$ survives past $n$ years:

$$\ddot{a}_{\overline{x:\overline{n}|}} = \ddot{a}_{\overline{n}|} + {}_{n|} \ddot{a}_x = \ddot{a}_{\overline{n}|} + {}_n E_x \cdot \ddot{a}_{x+n}$$

Using commutation functions:

$$\ddot{a}_{\overline{x:\overline{n}|}} = \ddot{a}_{\overline{n}|} + \frac{N_{x+n}}{D_x}$$

The contract guarantees minimum total payments of $n$, shielding the annuitant's beneficiaries from early forfeiture.

## 5.5 Multi-Frequency Annuities ($\ddot{a}_x^{(m)}$) and Woolhouse's Formula

In contemporary retirement practice, pension benefits are paid monthly ($m = 12$) or quarterly ($m = 4$) rather than in single annual installments.

Let $\ddot{a}_x^{(m)}$ denote an annuity paying a total of $1$ unit per year in $m$ equal installments of $1/m$ at the beginning of each $m$-th of a year:

$$\ddot{a}_x^{(m)} = \frac{1}{m} \sum_{k=0}^\infty v^{k/m} {}_{k/m} p_x$$

Because standard life tables do not tabulate fractional survival probabilities ${}_{k/m} p_x$, actuaries apply **Woolhouse’s Formula**, derived via Euler-Maclaurin summation:

$$\ddot{a}_x^{(m)} \approx \ddot{a}_x - \frac{m - 1}{2m} - \frac{m^2 - 1}{12 m^2} (\mu_x + \delta)$$

For monthly payments ($m = 12$), the constant $(m - 1)/(2m) = 11/24 \approx 0.45833$. The second-order term involving $(\mu_x + \delta)$ is typically negligible ($\approx 0.001$), yielding the universal practical approximation:

$$\ddot{a}_x^{(12)} \approx \ddot{a}_x - \frac{11}{24} = \ddot{a}_x - 0.45833$$

Similarly, for an immediate annuity payable monthly:

$$a_x^{(12)} \approx a_x + \frac{11}{24}$$

## 5.6 Varying Life Annuities: $(I\ddot{a})_x$ and Commutation Column $S_x$

An **Arithmetically Increasing Whole Life Annuity-Due** pays $1$ unit at time $0$, $2$ units at time $1$, $3$ units at time $2$, and $k + 1$ units at time $k$:

$$(I\ddot{a})_x = \sum_{k=0}^\infty (k + 1) v^k {}_k p_x = \frac{\sum_{k=0}^\infty (k + 1) D_{x+k}}{D_x} = \frac{\sum_{k=0}^\infty N_{x+k}}{D_x}$$

Actuaries define the fourth-order commutation column $S_x$ as:

$$S_x = \sum_{y=x}^{\omega - 1} N_y$$

The increasing annuity-due evaluates directly as:

$$(I\ddot{a})_x = \frac{S_x}{D_x}$$

For an increasing annuity-immediate:
$$(Ia)_x = \frac{S_{x+1}}{D_x}$$

## Fully worked question 1: Evaluating Life Annuities and Commutation Relationships

### Question
An extract from an actuarial valuation table compiled at an effective annual interest rate of $i = 6.00\%$ ($i = 0.06$, $d = 0.06/1.06 \approx 0.0566038$) provides the following commutation values:
- $D_{65} = 5,000$
- $D_{70} = 3,600$
- $D_{75} = 2,400$
- $N_{65} = 55,000$
- $N_{70} = 33,500$
- $N_{75} = 18,500$
- $S_{65} = 420,000$

A retiree aged $65$ purchases various retirement income policies. Compute:
1. The Actuarial Present Value of a Whole Life Annuity-Due of $120,000\text{ BDT}$ per year ($120,000 \ddot{a}_{65}$).
2. The Actuarial Present Value of a Whole Life Insurance on $(65)$ using the duality theorem ($A_{65} = 1 - d \ddot{a}_{65}$).
3. The Actuarial Present Value of a 10-Year Temporary Life Annuity-Due of $120,000\text{ BDT}$ per year ($120,000 \ddot{a}_{65:\overline{10}|}$).
4. The Actuarial Present Value of a Life Annuity-Due of $120,000\text{ BDT}$ deferred by 5 years (${}_{5|} \ddot{a}_{65}$).
5. The Actuarial Present Value of a 5-Year Guaranteed Life Annuity-Due of $120,000\text{ BDT}$ per year ($\ddot{a}_{\overline{65:\overline{5}|}}$).
6. The Actuarial Present Value of an Increasing Life Annuity-Due paying $10,000\text{ BDT}$ in Year 1, $20,000\text{ BDT}$ in Year 2, increasing by $10,000\text{ BDT}$ per year for life ($10,000 (I\ddot{a})_{65}$).

### Solution, step 1: Whole life annuity-due $\ddot{a}_{65}$
Using $\ddot{a}_x = N_x / D_x$:
$$\ddot{a}_{65} = \frac{N_{65}}{D_{65}} = \frac{55,000}{5,000} = 11.0000$$
For an annual pension of $120,000\text{ BDT}$:
$$\text{APV}_{\text{whole life}} = 120,000 \times 11.0000 = 1,320,000\text{ BDT}$$

### Solution, step 2: Whole life insurance $A_{65}$ via duality
Using $A_{65} = 1 - d \ddot{a}_{65}$:
$$d = \frac{i}{1 + i} = \frac{0.06}{1.06} \approx 0.05660377$$
$$A_{65} = 1 - (0.05660377 \times 11.0000) = 1 - 0.6226415 = 0.377358$$
A whole life insurance of $100,000\text{ BDT}$ on $(65)$ has a net single premium of:
$$100,000 \times 0.377358 \approx 37,736\text{ BDT}$$

### Solution, step 3: 10-Year temporary life annuity-due $\ddot{a}_{65:\overline{10}|}$
For a 10-year term from age 65, terminal age is $65 + 10 = 75$:
$$\ddot{a}_{65:\overline{10}|} = \frac{N_{65} - N_{75}}{D_{65}} = \frac{55,000 - 18,500}{5,000} = \frac{36,500}{5,000} = 7.3000$$
For an annual pension of $120,000\text{ BDT}$:
$$\text{APV}_{\text{temporary}} = 120,000 \times 7.3000 = 876,000\text{ BDT}$$

### Solution, step 4: 5-Year deferred life annuity-due ${}_{5|} \ddot{a}_{65}$
$${}_{5|} \ddot{a}_{65} = \frac{N_{70}}{D_{65}} = \frac{33,500}{5,000} = 6.7000$$
For an annual pension of $120,000\text{ BDT}$:
$$\text{APV}_{\text{deferred}} = 120,000 \times 6.7000 = 804,000\text{ BDT}$$
Check consistency:
$$\ddot{a}_{65:\overline{5}|} = \frac{N_{65} - N_{70}}{D_{65}} = \frac{55,000 - 33,500}{5,000} = \frac{21,500}{5,000} = 4.3000$$
$$\ddot{a}_{65:\overline{5}|} + {}_{5|} \ddot{a}_{65} = 4.3000 + 6.7000 = 11.0000 = \ddot{a}_{65}$$
The sum matches the whole life annuity perfectly.

### Solution, step 5: 5-Year guaranteed life annuity-due $\ddot{a}_{\overline{65:\overline{5}|}}$
Annuity-due certain for 5 years at $i = 0.06$:
$$\ddot{a}_{\overline{5}|} = (1.06) a_{\overline{5}|0.06} = 1.06 \times \left[ \frac{1 - (1.06)^{-5}}{0.06} \right] = 1.06 \times 4.212364 \approx 4.465106$$
Adding the deferred life annuity component:
$$\ddot{a}_{\overline{65:\overline{5}|}} = \ddot{a}_{\overline{5}|} + {}_{5|} \ddot{a}_{65} = 4.465106 + 6.7000 = 11.165106$$
For an annual pension of $120,000\text{ BDT}$:
$$\text{APV}_{\text{guaranteed}} = 120,000 \times 11.165106 \approx 1,339,813\text{ BDT}$$
Adding a 5-year guarantee costs an additional $1,339,813 - 1,320,000 = 19,813\text{ BDT}$ ($+1.5\%$).

### Solution, step 6: Increasing life annuity-due $(I\ddot{a})_{65}$
Using $(I\ddot{a})_x = S_x / D_x$:
$$(I\ddot{a})_{65} = \frac{S_{65}}{D_{65}} = \frac{420,000}{5,000} = 84.0000$$
For a scale step of $10,000\text{ BDT}$:
$$\text{APV}_{\text{increasing}} = 10,000 \times 84.0000 = 840,000\text{ BDT}$$

## Fully worked question 2: Variance Analysis of Life Annuity Present Value

### Question
A life insurance company issues a single-premium continuous whole life annuity of $B = 50,000\text{ BDT}$ per year to a life aged $x = 55$. 

Mortality is governed by a constant force of mortality $\mu = 0.0200$, and interest is governed by a constant force of interest $\delta = 0.0500$.

Perform the following calculations:
1. Compute the exact Actuarial Present Value $\bar{a}_{55}$.
2. Compute the Net Single Premium charged for the $50,000\text{ BDT/year}$ annuity.
3. Compute the continuous whole life insurance values $\bar{A}_{55}$ and ${}^2\bar{A}_{55}$.
4. Compute the variance $\text{Var}(\bar{Z})$ of the whole life insurance loss variable.
5. Using the equivalence relation $\text{Var}(\bar{Y}) = \text{Var}(\bar{Z}) / \delta^2$, compute the variance and standard deviation of the annuity present value random variable.
6. Compute the probability that the actual present value payout to the annuitant exceeds the premium collected ($P(Y > \bar{a}_{55})$).

### Solution, step 1: Compute $\bar{a}_{55}$ under constant forces
Under constant force of mortality $\mu = 0.02$ and constant force of interest $\delta = 0.05$:
$${}_t p_{55} = e^{-\mu t} = e^{-0.02 t}$$
$$\bar{a}_{55} = \int_0^\infty e^{-\delta t} e^{-\mu t}\,dt = \int_0^\infty e^{-(\delta + \mu) t}\,dt = \frac{1}{\delta + \mu} = \frac{1}{0.05 + 0.02} = \frac{1}{0.07} \approx 14.285714$$

### Solution, step 2: Net Single Premium
For an annual benefit rate of $50,000\text{ BDT/year}$:
$$\text{NSP} = 50,000 \times \bar{a}_{55} = 50,000 \times \frac{1}{0.07} \approx 714,286\text{ BDT}$$

### Solution, step 3: Life insurance values $\bar{A}_{55}$ and ${}^2\bar{A}_{55}$
$$\bar{A}_{55} = \frac{\mu}{\delta + \mu} = \frac{0.02}{0.07} \approx 0.285714$$
Verifying duality:
$$\bar{a}_{55} = \frac{1 - \bar{A}_{55}}{\delta} = \frac{1 - 0.285714}{0.05} = \frac{0.714286}{0.05} = 14.285714$$
For the second moment, evaluate at $2\delta = 2 \times 0.05 = 0.10$:
$${}^2\bar{A}_{55} = \frac{\mu}{2\delta + \mu} = \frac{0.02}{0.10 + 0.02} = \frac{0.02}{0.12} = \frac{1}{6} \approx 0.166667$$

### Solution, step 4: Variance of insurance random variable $\bar{Z}$
$$\text{Var}(\bar{Z}) = {}^2\bar{A}_{55} - (\bar{A}_{55})^2 = \frac{1}{6} - \left( \frac{2}{7} \right)^2 = \frac{1}{6} - \frac{4}{49} = \frac{49 - 24}{294} = \frac{25}{294} \approx 0.085034$$

### Solution, step 5: Variance and standard deviation of annuity random variable $\bar{Y}$
For a unit annuity:
$$\text{Var}(\bar{Y}) = \frac{\text{Var}(\bar{Z})}{\delta^2} = \frac{25 / 294}{(0.05)^2} = \frac{0.085034}{0.0025} \approx 34.0136$$
For the $50,000\text{ BDT/year}$ policy ($Y_{\text{policy}} = 50,000 \bar{Y}$):
$$\text{Var}(Y_{\text{policy}}) = (50,000)^2 \times 34.0136 = 2.5 \times 10^9 \times 34.0136 = 8.5034 \times 10^{10}\text{ BDT}^2$$
$$\sigma(Y_{\text{policy}}) = 50,000 \times \sqrt{34.0136} = 50,000 \times 5.8321 \approx 291,606\text{ BDT}$$
The standard deviation of the payout present value is **$291,606\text{ BDT}$** ($40.8\%$ of the expected premium!).

### Solution, step 6: Probability that actual payout exceeds the premium
We seek $P(Y > \mathbb{E}[Y]) = P\left( \frac{1 - e^{-\delta T_{55}}}{\delta} > \bar{a}_{55} \right)$:
$$\frac{1 - e^{-\delta T_{55}}}{\delta} > 14.285714$$
$$1 - e^{-\delta T_{55}} > 0.05 \times 14.285714 = 0.714286$$
$$e^{-\delta T_{55}} < 1 - 0.714286 = 0.285714$$
$$-\delta T_{55} < \ln(0.285714) = -1.252763$$
$$T_{55} > \frac{1.252763}{\delta} = \frac{1.252763}{0.05} = 25.055\text{ years}$$
Thus, the actual payout exceeds the collected premium if and only if the annuitant survives for more than $25.055$ years (attains age $80.055$).

Under exponential survival with $\mu = 0.02$:
$$P(T_{55} > 25.055) = e^{-\mu(25.055)} = e^{-0.02 \times 25.055} = e^{-0.5011} \approx 0.60586 = 60.59\%$$
Remarkably, because the exponential distribution is right-skewed, there is a **$60.59\%$ probability** that the annuitant receives more than the expected present value of benefits!

## Fully worked question 3: Monthly Pension Valuation via Woolhouse's Formula

### Question
A university professor aged $60$ retires with an accumulated defined-contribution pension balance of $2,000,000\text{ BDT}$. The professor wishes to purchase a single-premium life annuity payable in equal monthly installments of $M$ at the beginning of each month for life.

The actuarial life table compiled at an effective annual interest rate of $i = 5.00\%$ ($i = 0.05$) reports:
- $\ddot{a}_{60} = 12.8450$
- Force of mortality at age 60: $\mu_{60} = 0.0125$

Perform the following calculations:
1. Compute the nominal discount rate $d^{(12)}$ and the continuous force of interest $\delta$.
2. Compute the monthly annuity-due value $\ddot{a}_{60}^{(12)}$ using:
   - Woolhouse's two-term formula ($\ddot{a}_x^{(12)} \approx \ddot{a}_x - 11/24$)
   - Woolhouse's three-term formula ($\ddot{a}_x^{(12)} \approx \ddot{a}_x - 11/24 - \frac{143}{1728}(\mu_x + \delta)$)
3. Calculate the monthly pension installment $M$ that can be purchased with the $2,000,000\text{ BDT}$ retirement balance under the three-term Woolhouse value.
4. If the contract is structured as a **10-Year Guaranteed Monthly Life Annuity** ($\ddot{a}_{\overline{60:\overline{10}|}}^{(12)}$) with ${}_{10} E_{60} = 0.5420$ and $\ddot{a}_{70}^{(12)} = 9.4250$, compute the revised monthly pension payment and assess the cost of the guarantee.

### Solution, step 1: Compute interest parameters
Given $i = 0.05$:
$$\delta = \ln(1.05) \approx 0.048790$$
$$d = \frac{0.05}{1.05} \approx 0.047619$$
$$d^{(12)} = 12 [1 - (1.05)^{-1/12}] \approx 0.048691$$

### Solution, step 2: Evaluate $\ddot{a}_{60}^{(12)}$ via Woolhouse's formula
1. **Two-term formula**:
   $$\frac{m - 1}{2m} = \frac{11}{24} \approx 0.458333$$
   $$\ddot{a}_{60}^{(12)} \approx 12.8450 - 0.458333 = 12.386667 \approx 12.3867$$

2. **Three-term formula**:
   $$\frac{m^2 - 1}{12 m^2} = \frac{144 - 1}{12(144)} = \frac{143}{1728} \approx 0.082755$$
   $$\mu_{60} + \delta = 0.0125 + 0.048790 = 0.061290$$
   $$\text{Correction} = 0.082755 \times 0.061290 \approx 0.005072$$
   $$\ddot{a}_{60}^{(12)} = 12.386667 - 0.005072 = 12.381595 \approx 12.3816$$

### Solution, step 3: Determine monthly pension payout $M$
The total annual pension is $12 M$. The equation of value is:
$$12 M \cdot \ddot{a}_{60}^{(12)} = 2,000,000\text{ BDT}$$
$$12 M = \frac{2,000,000}{12.381595} \approx 161,529.98\text{ BDT/year}$$
The monthly installment is:
$$M = \frac{161,529.98}{12} \approx 13,460.83\text{ BDT/month}$$
The retiree receives a guaranteed lifelong income of **$13,461\text{ BDT}$** at the start of every month.

### Solution, step 4: Guaranteed 10-Year monthly annuity evaluation
For an annuity with a 10-year term certain payable monthly:
$$\ddot{a}_{\overline{60:\overline{10}|}}^{(12)} = \ddot{a}_{\overline{10}|}^{(12)} + {}_{10} E_{60} \cdot \ddot{a}_{70}^{(12)}$$
Calculate the 10-year annuity-certain due payable monthly:
$$\ddot{a}_{\overline{10}|}^{(12)} = \frac{1 - (1.05)^{-10}}{d^{(12)}} = \frac{1 - 0.613913}{0.048691} = \frac{0.386087}{0.048691} \approx 7.92933$$
Adding the deferred life annuity:
$${}_{10} E_{60} \cdot \ddot{a}_{70}^{(12)} = 0.5420 \times 9.4250 = 5.10835$$
$$\ddot{a}_{\overline{60:\overline{10}|}}^{(12)} = 7.92933 + 5.10835 = 13.03768$$

Compute the revised monthly pension:
$$12 M_{\text{guaranteed}} = \frac{2,000,000}{13.03768} \approx 153,401.52\text{ BDT/year}$$
$$M_{\text{guaranteed}} = \frac{153,401.52}{12} \approx 12,783.46\text{ BDT/month}$$

**Cost of Guarantee**:
- Non-guaranteed pension: $13,461\text{ BDT/month}$
- 10-Year guaranteed pension: $12,783\text{ BDT/month}$
The retiree forfeits $13,461 - 12,783 = 678\text{ BDT/month}$ (a $5.04\%$ reduction in monthly income) in exchange for ensuring that if death occurs during the next 10 years, their heirs will continue receiving the monthly pension until the 10-year milestone.
"""

unit_6 = r"""# Unit 6: Benefit Premiums, the Equivalence Principle & Loss-at-Issue Variance

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
"""

(DRAFT_DIR / "unit-5.md").write_text(unit_5.strip() + "\n", encoding="utf-8")
print("Unit 5 written.")

(DRAFT_DIR / "unit-6.md").write_text(unit_6.strip() + "\n", encoding="utf-8")
print("Unit 6 written.")
