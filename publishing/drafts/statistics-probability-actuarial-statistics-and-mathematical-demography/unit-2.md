# Unit 2: Annuities Certain, Varying Cash Flows & Loan Amortization Mechanics

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

## 2.16 Mortgage Refinancing Rationality, Refinancing Thresholds, and Burnout

In residential and commercial real estate finance, fixed-rate mortgage borrowers possess an embedded financial call option to prepay and refinance their debt whenever prevailing market mortgage interest rates $i_{\text{market}}$ drop below their contract interest rate $i_{\text{contract}}$.

### 1. The Rational Refinancing Threshold Equation
Refinancing is not costless: the borrower must pay upfront transaction costs $F$ (closing fees, title insurance, legal appraisal, and origination points).
Let $B$ be the outstanding principal balance, and let $n$ be the remaining amortization tenure in months.

The borrower saves monthly payments:
$$\Delta P = P(B, n, i_{\text{contract}}) - P(B, n, i_{\text{market}})$$
The present value of these monthly savings over the expected tenure $T \le n$ (discounted at rate $i_{\text{market}}$) is $\Delta P \cdot a_{\overline{T}|i_{\text{market}}}$.

A naive borrower refinances whenever:
$$\Delta P \cdot a_{\overline{T}|i_{\text{market}}} > F$$

However, because refinancing extinguishes the borrower's option to refinance at even lower interest rates in the future, the decision represents the exercise of an **American-style call option**. Richard Stanton (1995) showed that the optimal refinancing threshold requires an interest rate spread $\Delta i = i_{\text{contract}} - i_{\text{market}}$ substantially higher than the naive breakeven rate:

$$\Delta i^* \approx \sqrt{\frac{2 F \sigma_i \sqrt{2\ln(1/\sigma_i)}}{B}} + \dots$$

Borrowers demand an interest rate incentive of 100 to 200 basis points before initiating refinancing.

### 2. Refinancing Burnout and Media Hysteresis
Mortgage pools exhibit **Burnout**: after a prolonged period of low interest rates, all financially sophisticated and credit-eligible borrowers refinance and exit the pool. The remaining pool of borrowers consists disproportionately of:
- Low financial literacy borrowers who ignore refinancing opportunities.
- Borrowers whose home equity has declined (high LTV), disqualifying them from new underwriting.
- Borrowers with damaged credit scores.

Consequently, when market interest rates drop again to the same or even lower levels, the refinancing speed of the pool fails to match previous levels. Prepayment modelers represent burnout by tracking the cumulative refinancing incentive through path-dependent state variables in mortgage cash flow simulations.

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
