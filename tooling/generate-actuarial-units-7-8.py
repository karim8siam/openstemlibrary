#!/usr/bin/env python3
"""
Generate Units 7 and 8 for Actuarial Statistics and Mathematical Demography.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_7 = r"""# Unit 7: Benefit Reserves, Thiele's Differential Equation & Expense Loadings

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
"""

unit_8 = r"""# Unit 8: Mathematical Demography, Multiple Decrement Models & Population Dynamics

## 8.1 Multiple Decrement Theory: Competing Risks in Actuarial Science

In the single-decrement survival models analyzed in Unit 3, death was the sole terminating event. In real-world actuarial environments—such as defined-benefit corporate pension funds, health insurance schemes, and life insurance portfolios—an individual may exit the active insured population due to one of several mutually exclusive competing causes:
- Cause 1: Normal Age Retirement
- Cause 2: Ill-Health Total Disability
- Cause 3: Death in Active Service
- Cause 4: Voluntary Withdrawal (Resignation / Policy Surrender)

The mathematical theory governing these competing pathways is **Multiple Decrement Theory**.

### The Continuous Multiple Decrement Model
Let $(x)$ be an active life aged $x$. The time until exit is modeled by a continuous random variable $T \ge 0$, and the cause of exit is modeled by a discrete random variable $J \in \{1, 2, \dots, m\}$.

The **Cause-Specific Force of Decrement** for cause $j$ at attained age $x + t$ is:

$$\mu_x^{(j)}(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t, \; J = j \mid T > t)}{\Delta t}$$

The **Total Force of Decrement** across all operating causes is the direct sum of cause-specific hazards:

$$\mu_x^{(\tau)}(t) = \sum_{j=1}^m \mu_x^{(j)}(t)$$

The probability that a life aged $x$ survives all $m$ decrements for at least $t$ years is:

$${}_t p_x^{(\tau)} = \exp\left( -\int_0^t \mu_x^{(\tau)}(s)\,ds \right) = \exp\left( -\sum_{j=1}^m \int_0^t \mu_x^{(j)}(s)\,ds \right) = \prod_{j=1}^m \exp\left( -\int_0^t \mu_x^{(j)}(s)\,ds \right)$$

### Crude Decrement Probabilities: ${}_t q_x^{(j)}$
The marginal probability that $(x)$ leaves the active cohort before duration $t$ specifically due to cause $j$ in the presence of all other competing decrements is the **Crude Decrement Probability**:

$${}_t q_x^{(j)} = P(T \le t, \; J = j) = \int_0^t {}_s p_x^{(\tau)} \cdot \mu_x^{(j)}(s)\,ds$$

Summing across all $m$ causes reproduces the total decrement probability:

$${}_t q_x^{(\tau)} = \sum_{j=1}^m {}_t q_x^{(j)} = 1 - {}_t p_x^{(\tau)}$$

When $t = 1$, the annual crude decrement rate is written simply as $q_x^{(j)}$.

## 8.2 Associated Single Decrement Tables and Net Probabilities

Actuaries frequently confront counterfactual policy questions: *What would the mortality rate of factory workers be if industrial toxic exposures were completely eradicated?* Or: *What would the pension fund retirement rate be if early disability exits were eliminated?*

Answering these questions requires isolating cause $j$ from all other competing risks.

### The Associated Single Decrement Table
For each cause $j$, actuaries construct a theoretical **Associated Single Decrement Table (ASDT)**, representing an imaginary universe where cause $j$ is the *only* operating hazard.

The **Net Decrement Probability** $q_x^{\prime (j)}$ represents the probability that a life aged $x$ exits within one year due to cause $j$ assuming all other decrements are inoperative:

$$p_x^{\prime (j)} = 1 - q_x^{\prime (j)} = \exp\left( -\int_0^1 \mu_x^{(j)}(s)\,ds \right)$$

Because an individual cannot be saved from death by withdrawing from a pension scheme, net probabilities satisfy:

$$q_x^{\prime (j)} > q_x^{(j)}$$

The crude probability $q_x^{(j)}$ is strictly smaller than the net probability $q_x^{\prime (j)}$ because competing causes remove lives who would otherwise have exited via cause $j$ later in the year!

### Mathematical Conversion Relationships
To translate between crude rates $q_x^{(j)}$ and net rates $q_x^{\prime (j)}$, actuaries apply one of two fractional assumptions:

#### 1. Constant Force of Decrement (CFD)
Assuming the ratio of each cause-specific hazard to total hazard remains constant over the year:
$$\frac{\mu_x^{(j)}(t)}{\mu_x^{(\tau)}(t)} = c_j = \frac{q_x^{(j)}}{q_x^{(\tau)}}, \qquad 0 \le t \le 1$$
Integrating yields the celebrated exponential conversion:

$$p_x^{\prime (j)} = \left( p_x^{(\tau)} \right)^{\frac{q_x^{(j)}}{q_x^{(\tau)}}}$$

$$q_x^{\prime (j)} = 1 - \left( 1 - q_x^{(\tau)} \right)^{\frac{q_x^{(j)}}{q_x^{(\tau)}}}$$

#### 2. Uniform Distribution of Decrements (UDD in Multiple Decrement Table)
Assuming each crude decrement distributes uniformly over the year (${}_t q_x^{(j)} = t \cdot q_x^{(j)}$), for a two-decrement model ($m = 2$):

$$q_x^{\prime (1)} = \frac{q_x^{(1)}}{1 - \frac{1}{2} q_x^{(2)}}$$

$$q_x^{\prime (2)} = \frac{q_x^{(2)}}{1 - \frac{1}{2} q_x^{(1)}}$$

The denominator $1 - \frac{1}{2} q_x^{(2)}$ adjusts for the fact that lives exiting via cause 2 on average exit at mid-year ($t = 0.5$), exposing them to cause 1 for only half the year.

## 8.3 Joint Life and Last Survivor Statuses (Multi-Life Contingencies)

Many actuarial contracts involve multiple lives simultaneously (e.g., joint life annuities for married couples, or survivor pensions for widows).

Let $(x)$ and $(y)$ be two lives with remaining future lifetimes $T_x$ and $T_y$.

### 1. The Joint Life Status: $(xy)$
The **Joint Life Status** (denoted $(xy)$) is a status that functions as long as *both* lives survive, failing upon the *first death*:

$$T_{xy} = \min(T_x, T_y)$$

Assuming $T_x$ and $T_y$ are statistically independent:

$${}_t p_{xy} = P(T_x > t \cap T_y > t) = {}_t p_x \cdot {}_t p_y$$

The force of mortality of the joint status is additive:

$$\mu_{xy}(t) = -\frac{d}{dt} \ln({}_t p_{xy}) = -\frac{d}{dt} \ln({}_t p_x) - \frac{d}{dt} \ln({}_t p_y) = \mu_{x+t} + \mu_{y+t}$$

The joint life annuity-due is:

$$\ddot{a}_{xy} = \sum_{t=0}^\infty v^t {}_t p_{xy} = \sum_{t=0}^\infty v^t {}_t p_x {}_t p_y$$

### 2. The Last Survivor Status: $(\overline{xy})$
The **Last Survivor Status** (denoted $(\overline{xy})$) functions as long as *at least one* life survives, failing only upon the *second death*:

$$T_{\overline{xy}} = \max(T_x, T_y)$$

The probability of surviving past $t$ is:

$${}_t p_{\overline{xy}} = P(T_x > t \cup T_y > t) = {}_t p_x + {}_t p_y - {}_t p_{xy}$$

### Duality Identities for Multi-Life Contracts
Taking discounted integrals and sums yields the universal multi-life addition theorems:

$$\ddot{a}_{\overline{xy}} = \ddot{a}_x + \ddot{a}_y - \ddot{a}_{xy}$$

$$A_{\overline{xy}} = A_x + A_y - A_{xy}$$

$$\mathring{e}_{\overline{xy}} = \mathring{e}_x + \mathring{e}_y - \mathring{e}_{xy}$$

These identities permit the immediate pricing of complex joint-and-survivor annuity options from single-life and joint-life tables.

## 8.4 Mathematical Demography: Alfred Lotka's Stable Population Theory

In 1907–1939, Alfred J. Lotka revolutionized mathematical demography by formulating the continuous renewal theory of human population dynamics.

Let $B(t)$ denote the continuous birth rate (births per unit time) in a closed female population at calendar time $t$.
Let $p(a) = {}_a p_0$ denote the probability that a female newborn survives to exact age $a$.
Let $m(a)$ denote the age-specific fertility rate (the annual rate of female childbearing for women aged $a$, restricted to reproductive ages $[\alpha, \beta] \approx [15, 49]$).

### The Lotka Renewal Integral Equation
Females born at time $t - a$ who survive to time $t$ are aged $a$. Their number is $B(t - a) p(a)$. Each woman of age $a$ gives birth at rate $m(a)$. 

Summing births across all maternal ages:

$$B(t) = G(t) + \int_\alpha^\beta B(t - a) p(a) m(a)\,da$$

where $G(t)$ represents births contributed by females who were already alive at initial time $t = 0$. For $t > \beta \approx 50\text{ years}$, the initial population has aged past reproduction ($G(t) = 0$), and the renewal equation becomes purely endogenous:

$$B(t) = \int_\alpha^\beta B(t - a) p(a) m(a)\,da$$

### The Characteristic Equation for the Intrinsic Growth Rate ($r$)
Lotka sought trial exponential solutions of the form $B(t) = C e^{r t}$. Substituting into the renewal equation:

$$C e^{r t} = \int_\alpha^\beta C e^{r(t - a)} p(a) m(a)\,da$$

Dividing both sides by $C e^{r t}$ yields **Lotka's Characteristic Equation**:

$$\int_\alpha^\beta e^{-r a} p(a) m(a)\,da = 1.0$$

The unique real root $r$ of this equation is the **Intrinsic Rate of Natural Increase** (Lotka's $r$).
- If $\int_\alpha^\beta p(a) m(a)\,da > 1.0$: $r > 0$ (the population expands exponentially).
- If $\int_\alpha^\beta p(a) m(a)\,da = 1.0$: $r = 0$ (the population reaches stationary equilibrium).
- If $\int_\alpha^\beta p(a) m(a)\,da < 1.0$: $r < 0$ (the population declines exponentially).

### Net and Gross Reproduction Rates
1. **Gross Reproduction Rate ($GRR$)**: The average number of female daughters a woman would bear if she survived to the end of her reproductive years ($\beta$):
   $$GRR = \int_\alpha^\beta m(a)\,da$$
2. **Net Reproduction Rate ($NRR$, $R_0$)**: The average number of female daughters a newborn girl will bear, accounting for cohort mortality:
   $$R_0 = NRR = \int_\alpha^\beta p(a) m(a)\,da$$
   Notice that $R_0$ is the characteristic equation evaluated at $r = 0$.

### The Asymptotic Stable Age Distribution
Lotka proved that **regardless of the initial age distribution of a population**, if age-specific fertility $m(a)$ and survival $p(a)$ remain constant over time, the population will inexorably converge to a fixed, time-invariant **Stable Age Distribution** $c(a)$:

$$c(a) = b \cdot e^{-r a} p(a)$$

where $b = \left[ \int_0^\omega e^{-r a} p(a)\,da \right]^{-1}$ is the stable crude birth rate. This result—the **Strong Ergodic Theorem of Demography**—establishes that a population completely forgets its historical demographic shocks!

## 8.5 Discrete Population Projections: The Leslie Matrix Model

In 1945, P. H. Leslie discretized Lotka’s continuous renewal theory into an elegant matrix algebra formulation widely applied in official national demographic forecasting.

Divide the female population into $k$ equal age groups of width $h$ years (typically $h = 5\text{ years}$, giving age brackets $0-4, 5-9, \dots, 80-84, 85+$).
Let the state vector at time step $t$ be:

$$\mathbf{n}_t = (n_{1, t}, n_{2, t}, \dots, n_{k, t})^T$$

where $n_{i, t}$ is the female population count in age group $i$ at time $t$.

### The Leslie Projection Matrix ($\mathbf{L}$)
The population evolves from time step $t$ to $t + 1$ (after $h$ years) via the linear matrix system:

$$\mathbf{n}_{t+1} = \mathbf{L} \cdot \mathbf{n}_t$$

The **Leslie Matrix** $\mathbf{L}$ is a $k \times k$ square matrix with a canonical sparse structure:

$$\mathbf{L} = \begin{pmatrix} F_1 & F_2 & F_3 & \dots & F_{k-1} & F_k \\ P_1 & 0 & 0 & \dots & 0 & 0 \\ 0 & P_2 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \dots & \vdots & \vdots \\ 0 & 0 & \dots & P_{k-1} & 0 & 0 \end{pmatrix}$$

where:
- **Top Row ($F_i$)**: The net effective reproduction coefficient for age group $i$, measuring daughters born during the 5-year interval who survive to enter age group 1 ($0-4$):
  $$F_i = \sqrt{P_0} \cdot \frac{m_i + m_{i+1} P_i}{2}$$
- **Sub-Diagonal ($P_i$)**: The cohort survival probability from age group $i$ to age group $i + 1$:
  $$P_i = \frac{L_{i+1}}{L_i}$$
- All other matrix entries are zero.

### Spectral Analysis and Dominant Eigenvalue
Because $\mathbf{L}$ is a non-negative, irreducible matrix, the **Perron-Frobenius Theorem** guarantees:
1. $\mathbf{L}$ has a unique, positive real eigenvalue $\lambda_1 > 0$ that strictly exceeds the modulus of all other complex eigenvalues ($|\lambda_j| < \lambda_1$ for $j \ge 2$).
2. The long-term asymptotic growth rate is governed entirely by $\lambda_1$:
   $$\lim_{t \to \infty} \mathbf{n}_t = c \cdot \lambda_1^t \cdot \mathbf{v}_1$$
   where $\lambda_1 = e^{r h}$ is directly related to Lotka's intrinsic rate of natural increase $r$.
3. The right eigenvector $\mathbf{v}_1$ corresponding to $\lambda_1$ defines the asymptotic stable age structure.
4. The left eigenvector $\mathbf{u}_1^T$ defines Fisher's **Reproductive Value** across age brackets.

## Fully worked question 1: Multiple Decrement Table Construction and Net Probability Conversion

### Question
A defined-benefit corporate pension fund tracks active white-collar employees aged $x = 60$. During the year of age from 60 to 61, employees face three competing decrements:
- Decrement 1: Normal and Early Retirement ($j = 1$)
- Decrement 2: Total Permanent Disability ($j = 2$)
- Decrement 3: Death in Active Service ($j = 3$)

A multiple decrement study across an initial active cohort of $\ell_{60}^{(\tau)} = 10,000$ employees observes the following decrement counts during the year:
- Retirements: $d_{60}^{(1)} = 1,200$
- Disabilities: $d_{60}^{(2)} = 300$
- Deaths: $d_{60}^{(3)} = 100$

Total decrements: $d_{60}^{(\tau)} = 1,200 + 300 + 100 = 1,600$.

Perform the following calculations:
1. Compute the crude annual decrement rates $q_{60}^{(1)}, q_{60}^{(2)}, q_{60}^{(3)}$, and the overall survival rate $p_{60}^{(\tau)}$.
2. Under the **Constant Force of Decrement (CFD)** assumption, compute the net decrement probabilities $q_{60}^{\prime (1)}, q_{60}^{\prime (2)},$ and $q_{60}^{\prime (3)}$ in the associated single decrement tables.
3. Under the **Uniform Distribution of Decrements (UDD)** assumption in the multiple decrement table, compute the net decrement probabilities and compare with the CFD results.
4. If a corporate policy change raises the mandatory retirement age to 65 (completely eliminating retirement at age 60, so $q_{60}^{\prime (1)} = 0$), compute the revised number of deaths expected to occur among the 10,000 employees.

### Solution, step 1: Compute crude rates and total survival
$$\ell_{60}^{(\tau)} = 10,000$$
$$d_{60}^{(\tau)} = 1,600 \implies q_{60}^{(\tau)} = \frac{1,600}{10,000} = 0.16000$$
$$p_{60}^{(\tau)} = 1 - 0.16000 = 0.84000$$

Crude rates:
- Retirement: $q_{60}^{(1)} = 1,200 / 10,000 = 0.12000$
- Disability: $q_{60}^{(2)} = 300 / 10,000 = 0.03000$
- Death: $q_{60}^{(3)} = 100 / 10,000 = 0.01000$
Check: $0.12000 + 0.03000 + 0.01000 = 0.16000$.

### Solution, step 2: Net rates under Constant Force of Decrement (CFD)
Formula: $p_{60}^{\prime (j)} = [p_{60}^{(\tau)}]^{q_{60}^{(j)} / q_{60}^{(\tau)}} = [0.84000]^{q_{60}^{(j)} / 0.16000}$:
1. **Net Retirement Rate ($q_{60}^{\prime (1)}$)**:
   $$\text{Power} = \frac{0.12000}{0.16000} = 0.750$$
   $$p_{60}^{\prime (1)} = (0.84000)^{0.750} = \exp(0.750 \times \ln 0.84000) = \exp(0.750 \times (-0.174353)) = \exp(-0.130765) \approx 0.877421$$
   $$q_{60}^{\prime (1)} = 1 - 0.877421 = 0.12258 = 12.26\%$$

2. **Net Disability Rate ($q_{60}^{\prime (2)}$)**:
   $$\text{Power} = \frac{0.03000}{0.16000} = 0.1875$$
   $$p_{60}^{\prime (2)} = (0.84000)^{0.1875} = \exp(0.1875 \times (-0.174353)) = \exp(-0.032691) \approx 0.967838$$
   $$q_{60}^{\prime (2)} = 1 - 0.967838 = 0.03216 = 3.22\%$$

3. **Net Death Rate ($q_{60}^{\prime (3)}$)**:
   $$\text{Power} = \frac{0.01000}{0.16000} = 0.0625$$
   $$p_{60}^{\prime (3)} = (0.84000)^{0.0625} = \exp(0.0625 \times (-0.174353)) = \exp(-0.010897) \approx 0.989162$$
   $$q_{60}^{\prime (3)} = 1 - 0.989162 = 0.01084 = 1.084\%$$

Notice that for every cause, the net rate exceeds the crude rate ($q^{\prime (j)} > q^{(j)}$)! For deaths, the net rate is $1.084\%$ versus crude $1.000\%$.

### Solution, step 3: Net rates under UDD in Multiple Decrement Table
Under UDD for three decrements:
$$q_{60}^{\prime (j)} = \frac{q_{60}^{(j)}}{1 - \frac{1}{2} \sum_{k \ne j} q_{60}^{(k)} + \frac{1}{3} \prod_{k \ne j} q_{60}^{(k)}}$$
For death ($j = 3$):
$$\sum_{k \ne 3} q_{60}^{(k)} = q_{60}^{(1)} + q_{60}^{(2)} = 0.12000 + 0.03000 = 0.15000$$
$$1 - \frac{1}{2}(0.15000) = 1 - 0.07500 = 0.92500$$
$$q_{60}^{\prime (3)} \approx \frac{0.01000}{0.92500} \approx 0.01081 = 1.081\%$$
Both CFD ($1.084\%$) and UDD ($1.081\%$) agree closely.

### Solution, step 4: Revised death counts if retirement is eliminated
If retirement is eliminated ($q^{\prime (1)} = 0$), only disability and death operate.
Under the CFD independence model:
$$p_{60}^{(\tau) \text{ new}} = p_{60}^{\prime (2)} \times p_{60}^{\prime (3)} = 0.967838 \times 0.989162 \approx 0.957348$$
$$q_{60}^{(\tau) \text{ new}} = 1 - 0.957348 = 0.042652$$

The revised total forces of decrement are:
$$\mu_2 = -\ln p_{60}^{\prime (2)} = 0.032691, \qquad \mu_3 = -\ln p_{60}^{\prime (3)} = 0.010897$$
$$\mu_{\text{new}} = 0.032691 + 0.010897 = 0.043588$$
The revised crude death rate is:
$$q_{60}^{(3) \text{ new}} = \frac{\mu_3}{\mu_{\text{new}}} q_{60}^{(\tau) \text{ new}} = \frac{0.010897}{0.043588} \times 0.042652 = 0.25000 \times 0.042652 \approx 0.010663$$

Expected deaths among $10,000$ employees:
$$\text{Expected Deaths} = 10,000 \times 0.010663 \approx 106.6 \approx 107\text{ deaths}$$
Eliminating early retirement increases active workforce deaths from $100$ to **$107$** because the 1,200 employees who previously retired now remain on the payroll and exposed to workplace mortality!

## Fully worked question 2: Joint Life and Last Survivor Annuity Pricing

### Question
An actuarial consulting firm prices retirement options for a married couple consisting of a husband aged $x = 65$ and a wife aged $y = 62$. 

The single-life and joint-life annuity-due values compiled at an effective annual interest rate of $i = 5.00\%$ ($i = 0.05$) are:
- $\ddot{a}_{65} = 11.2000$
- $\ddot{a}_{62} = 12.5000$
- $\ddot{a}_{65:62} = 9.8000$ (Joint Life Annuity, paying while both are alive)

The couple has accumulated a retirement fund of $1,500,000\text{ BDT}$.

Perform the following calculations:
1. Compute the Actuarial Present Value of the Last Survivor Annuity-Due ($\ddot{a}_{\overline{65:62}}$).
2. Compute the annual pension $P_1$ payable under an ordinary Joint Life Annuity (payments cease upon the first death).
3. Compute the annual pension $P_2$ payable under a $100\%$ Joint-and-Survivor Annuity (payments continue unchanged until the second death).
4. Compute the annual pension $P_3$ payable under a **Two-Thirds ($66.7\%$) Joint-and-Survivor Annuity**, which pays $P_3$ while both are alive, and reduces to $\frac{2}{3} P_3$ to the surviving spouse upon the first death.

### Solution, step 1: Compute Last Survivor Annuity $\ddot{a}_{\overline{65:62}}$
Using the multi-life addition theorem:
$$\ddot{a}_{\overline{xy}} = \ddot{a}_x + \ddot{a}_y - \ddot{a}_{xy}$$
Substitute the given values:
$$\ddot{a}_{\overline{65:62}} = 11.2000 + 12.5000 - 9.8000 = 23.7000 - 9.8000 = 13.9000$$

### Solution, step 2: Option 1 - Ordinary Joint Life Annuity
Payments occur only while both spouses are alive. The equation of value is:
$$P_1 \cdot \ddot{a}_{65:62} = 1,500,000\text{ BDT}$$
$$P_1 = \frac{1,500,000}{9.8000} \approx 153,061.22\text{ BDT/year}$$
The couple receives **$153,061\text{ BDT/year}$**, but payments terminate completely the instant either spouse dies.

### Solution, step 3: Option 2 - 100% Joint-and-Survivor Annuity
Payments continue at $100\%$ until the second death:
$$P_2 \cdot \ddot{a}_{\overline{65:62}} = 1,500,000\text{ BDT}$$
$$P_2 = \frac{1,500,000}{13.9000} \approx 107,913.67\text{ BDT/year}$$
The couple receives **$107,914\text{ BDT/year}$** ($29.5\%$ lower than Option 1), but with complete lifelong security for the surviving spouse.

### Solution, step 4: Option 3 - Two-Thirds (66.7%) Joint-and-Survivor Annuity
The payment structure is:
- While both are alive: Pays $P_3$.
- If husband dies first: Wife receives $\frac{2}{3} P_3$.
- If wife dies first: Husband receives $\frac{2}{3} P_3$.

We express this cash flow structure using joint and single annuities:
$$\text{APV} = \frac{2}{3} P_3 \ddot{a}_x + \frac{2}{3} P_3 \ddot{a}_y - \frac{1}{3} P_3 \ddot{a}_{xy}$$
Alternatively:
$$\text{APV} = \frac{2}{3} P_3 \ddot{a}_{\overline{xy}} + \frac{1}{3} P_3 \ddot{a}_{xy}$$
Check consistency:
$$\frac{2}{3}(\ddot{a}_x + \ddot{a}_y - \ddot{a}_{xy}) + \frac{1}{3} \ddot{a}_{xy} = \frac{2}{3}\ddot{a}_x + \frac{2}{3}\ddot{a}_y - \frac{1}{3}\ddot{a}_{xy}$$
Both formulations are algebraically identical!

Evaluate the unit multiplier:
$$\text{Multiplier} = \frac{2}{3}(13.9000) + \frac{1}{3}(9.8000) = \frac{27.8000 + 9.8000}{3} = \frac{37.6000}{3} \approx 12.533333$$

Now solve for $P_3$:
$$P_3 \times 12.533333 = 1,500,000\text{ BDT}$$
$$P_3 = \frac{1,500,000}{12.533333} \approx 119,680.85\text{ BDT/year}$$

**Payout Summary for Option 3**:
- While both spouses are alive: **$119,681\text{ BDT/year}$** ($9,973\text{ BDT/month}$).
- Upon first death, surviving spouse receives $\frac{2}{3} \times 119,681 = \mathbf{79,787\text{ BDT/year}}$ ($6,649\text{ BDT/month}$) for life.
This represents the most popular pension option among retirees, balancing adequate dual income with surviving spouse protection.

## Fully worked question 3: The Leslie Matrix Population Projection and Eigenvalue Growth

### Question
A mathematical demographer models an animal wildlife population (or human female population) partitioned into $k = 3$ distinct age classes of equal width:
- Class 1: Juveniles (Age $0-1$)
- Class 2: Sub-Adults (Age $1-2$)
- Class 3: Mature Adults (Age $2-3$)

The demographic vital rates parameterized in the Leslie Matrix $\mathbf{L}$ are:
- Age-specific reproduction coefficients: $F_1 = 0.0, \; F_2 = 1.6, \; F_3 = 1.2$
- Survival probabilities: $P_1 = 0.50$ (survival from Class 1 to 2), $P_2 = 0.25$ (survival from Class 2 to 3)

The Leslie matrix is:
$$\mathbf{L} = \begin{pmatrix} 0.0 & 1.6 & 1.2 \\ 0.50 & 0.0 & 0.0 \\ 0.0 & 0.25 & 0.0 \end{pmatrix}$$

The initial population census vector at year $t = 0$ is $\mathbf{n}_0 = (100, \; 40, \; 20)^T$.

Perform the following calculations:
1. Compute the population vectors at year $t = 1$ ($\mathbf{n}_1$) and year $t = 2$ ($\mathbf{n}_2$).
2. Formulate the characteristic polynomial $\det(\mathbf{L} - \lambda \mathbf{I}) = 0$.
3. Compute the dominant eigenvalue $\lambda_1$.
4. Determine the intrinsic rate of natural increase $r$.
5. Determine the stable age distribution eigenvector $\mathbf{v}_1$.
6. Calculate the Net Reproduction Rate ($R_0$) from the matrix parameters.

### Solution, step 1: Project population vectors $\mathbf{n}_1$ and $\mathbf{n}_2$
1. **At year $t = 1$**:
   $$\mathbf{n}_1 = \mathbf{L} \cdot \mathbf{n}_0 = \begin{pmatrix} 0.0 & 1.6 & 1.2 \\ 0.50 & 0.0 & 0.0 \\ 0.0 & 0.25 & 0.0 \end{pmatrix} \begin{pmatrix} 100 \\ 40 \\ 20 \end{pmatrix}$$
   - $n_{1, 1} = (0.0 \times 100) + (1.6 \times 40) + (1.2 \times 20) = 0 + 64 + 24 = 88$
   - $n_{2, 1} = 0.50 \times 100 = 50$
   - $n_{3, 1} = 0.25 \times 40 = 10$
   $$\mathbf{n}_1 = \begin{pmatrix} 88 \\ 50 \\ 10 \end{pmatrix}, \qquad \text{Total Population } N_1 = 88 + 50 + 10 = 148$$
   Initial total population was $N_0 = 100 + 40 + 20 = 160$. Total population temporarily dipped to $148$ due to age structure imbalances.

2. **At year $t = 2$**:
   $$\mathbf{n}_2 = \mathbf{L} \cdot \mathbf{n}_1 = \begin{pmatrix} 0.0 & 1.6 & 1.2 \\ 0.50 & 0.0 & 0.0 \\ 0.0 & 0.25 & 0.0 \end{pmatrix} \begin{pmatrix} 88 \\ 50 \\ 10 \end{pmatrix}$$
   - $n_{1, 2} = (1.6 \times 50) + (1.2 \times 10) = 80 + 12 = 92$
   - $n_{2, 2} = 0.50 \times 88 = 44$
   - $n_{3, 2} = 0.25 \times 50 = 12.5 \approx 13$
   $$\mathbf{n}_2 = \begin{pmatrix} 92 \\ 44 \\ 12.5 \end{pmatrix}, \qquad \text{Total Population } N_2 \approx 148.5$$

### Solution, step 2: Characteristic polynomial of $\mathbf{L}$
$$\det(\mathbf{L} - \lambda \mathbf{I}) = \det \begin{pmatrix} -\lambda & 1.6 & 1.2 \\ 0.50 & -\lambda & 0 \\ 0 & 0.25 & -\lambda \end{pmatrix} = 0$$
Expanding along the first row:
$$\det = -\lambda \begin{vmatrix} -\lambda & 0 \\ 0.25 & -\lambda \end{vmatrix} - 1.6 \begin{vmatrix} 0.50 & 0 \\ 0 & -\lambda \end{vmatrix} + 1.2 \begin{vmatrix} 0.50 & -\lambda \\ 0 & 0.25 \end{vmatrix}$$
$$= -\lambda(\lambda^2) - 1.6(-0.50 \lambda) + 1.2(0.50 \times 0.25)$$
$$= -\lambda^3 + 0.80 \lambda + 0.15 = 0$$
Multiplying by $-1$:

$$\lambda^3 - 0.80 \lambda - 0.15 = 0$$

### Solution, step 3: Solve for the dominant eigenvalue $\lambda_1$
Let $f(\lambda) = \lambda^3 - 0.80 \lambda - 0.15$:
- At $\lambda = 1.0$: $f(1.0) = 1.0 - 0.80 - 0.15 = +0.05 > 0$.
- At $\lambda = 0.9$: $f(0.9) = (0.9)^3 - 0.80(0.9) - 0.15 = 0.729 - 0.720 - 0.15 = -0.141 < 0$.
By the intermediate value theorem, a root lies between $0.9$ and $1.0$.

Applying Newton-Raphson iteration starting at $\lambda_0 = 1.0$:
$$f'( \lambda ) = 3 \lambda^2 - 0.80$$
- $f(1.0) = 0.05$
- $f'(1.0) = 3(1.0) - 0.80 = 2.20$
$$\lambda_1 = 1.0 - \frac{0.05}{2.20} = 1.0 - 0.022727 \approx 0.97727$$

Second iteration:
- $f(0.97727) = (0.97727)^3 - 0.80(0.97727) - 0.15 = 0.93335 - 0.78182 - 0.15 = +0.00153$
- $f'(0.97727) = 3(0.97727)^2 - 0.80 = 3(0.95506) - 0.80 = 2.86518 - 0.80 = 2.06518$
$$\lambda_1 = 0.97727 - \frac{0.00153}{2.06518} \approx 0.97727 - 0.00074 = 0.97653$$
$$\lambda_1 \approx 0.9765$$
The dominant eigenvalue is **$\lambda_1 \approx 0.9765$**.

### Solution, step 4: Compute intrinsic rate of natural increase $r$
Since $\lambda_1 = e^r$ (with time step $h = 1\text{ year}$):
$$r = \ln(\lambda_1) = \ln(0.9765) \approx -0.0238 \implies -2.38\%\text{ per year}$$
Because $\lambda_1 < 1.0$ ($r < 0$), the population will contract asymptotically by $2.38\%$ per year.

### Solution, step 5: Determine the stable age distribution eigenvector $\mathbf{v}_1$
The eigenvector satisfies $\mathbf{L} \mathbf{v}_1 = \lambda_1 \mathbf{v}_1$:
$$\begin{pmatrix} 0.0 & 1.6 & 1.2 \\ 0.50 & 0.0 & 0.0 \\ 0.0 & 0.25 & 0.0 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = 0.9765 \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}$$
From row 2:
$$0.50 v_1 = 0.9765 v_2 \implies v_2 = \frac{0.50}{0.9765} v_1 \approx 0.51203 v_1$$
From row 3:
$$0.25 v_2 = 0.9765 v_3 \implies v_3 = \frac{0.25}{0.9765} v_2 = \frac{0.25 \times 0.51203}{0.9765} v_1 = \frac{0.12801}{0.9765} v_1 \approx 0.13109 v_1$$

Setting $v_1 = 1.0$:
$$\mathbf{v}_1 = \begin{pmatrix} 1.00000 \\ 0.51203 \\ 0.13109 \end{pmatrix}$$
Sum of elements $= 1.00000 + 0.51203 + 0.13109 = 1.64312$.
Normalizing to percentages:
- Class 1 (Juveniles): $\frac{1.00000}{1.64312} \times 100\% = 60.86\%$
- Class 2 (Sub-Adults): $\frac{0.51203}{1.64312} \times 100\% = 31.16\%$
- Class 3 (Mature Adults): $\frac{0.13109}{1.64312} \times 100\% = 7.98\%$

The asymptotic stable age distribution is **$60.86\%$ Juveniles, $31.16\%$ Sub-Adults, and $7.98\%$ Adults**.

### Solution, step 6: Compute the Net Reproduction Rate ($R_0$)
The Net Reproduction Rate is the expected lifetime female offspring produced per newborn:
$$R_0 = F_1 + P_1 F_2 + P_1 P_2 F_3 = 0.0 + (0.50 \times 1.6) + (0.50 \times 0.25 \times 1.2)$$
$$R_0 = 0 + 0.80 + 0.15 = 0.9500$$
Because $R_0 = 0.9500 < 1.0$, a female newborn replaces only $0.95$ female offspring over her lifecycle, mathematically proving that the population is below replacement level and will decline.
"""

(DRAFT_DIR / "unit-7.md").write_text(unit_7.strip() + "\n", encoding="utf-8")
print("Unit 7 written.")

(DRAFT_DIR / "unit-8.md").write_text(unit_8.strip() + "\n", encoding="utf-8")
print("Unit 8 written.")
