# Unit 4: Life Insurance Contracts & Actuarial Present Value Valuations

## 4.1 The Stochastic Present Value Loss Variable for Life Insurance

A life insurance policy is a legally binding contract under which an insurer promises to pay a designated capital sum (the death benefit or sum insured $b_t$) upon the death of the insured life $(x)$, contingent upon death occurring within an agreed policy horizon.

Because human mortality is a stochastic biological phenomenon, both the **timing of the claim payment** and the **number of years over which the insurer can invest premiums** are random variables.

Let $T_x$ denote the future lifetime of $(x)$. In a continuous insurance contract paying a unit benefit of $\$1$ at the exact moment of death $T_x$, the present value of the benefit payment is a continuous random variable $Z$:

$$Z = v^{T_x} = (1 + i)^{-T_x} = e^{-\delta T_x}$$

The expected value of $Z$, denoted $\mathbb{E}[Z]$, is the **Actuarial Present Value (APV)**—classically termed the **Net Single Premium (NSP)**. The net single premium represents the exact capital lump sum the insurer must collect at policy inception to fund the promised death benefit, ignoring administrative expenses and profit loadings.

In discrete insurance contracts where claims are aggregated and paid at the **end of the policy year of death**, death occurs in year $K_x + 1$, where $K_x = \lfloor T_x \rfloor$ is the curtate future lifetime. The discrete present value random variable is:

$$Z = v^{K_x + 1} = (1 + i)^{-(K_x + 1)}$$

## 4.2 Continuous Whole Life Insurance: $\bar{A}_x$

A **Continuous Whole Life Insurance** pays a benefit of $1$ unit at the exact moment of death of $(x)$, whenever death occurs ($0 < T_x < \infty$).

### Actuarial Present Value ($\bar{A}_x$)
The APV is the expected value of $Z = e^{-\delta T_x}$:

$$\bar{A}_x = \mathbb{E}[e^{-\delta T_x}] = \int_0^\infty e^{-\delta t} f_x(t)\,dt = \int_0^\infty e^{-\delta t} {}_t p_x \mu_{x+t}\,dt = \int_0^\infty v^t {}_t p_x \mu_{x+t}\,dt$$

### Second Moment and Variance of $Z$
To quantify the financial underwriting risk of the contract, the insurer must compute the variance of the present value random variable $\text{Var}(Z)$:

$$\text{Var}(Z) = \mathbb{E}[Z^2] - (\mathbb{E}[Z])^2 = \mathbb{E}[(e^{-\delta T_x})^2] - (\bar{A}_x)^2 = \mathbb{E}[e^{-2\delta T_x}] - (\bar{A}_x)^2$$

Notice that $\mathbb{E}[e^{-2\delta T_x}]$ has the exact same mathematical form as $\bar{A}_x$, but evaluated at a force of interest equal to twice the original force ($2\delta$). In actuarial notation, this second moment is denoted ${}^2\bar{A}_x$:

$${}^2\bar{A}_x = \int_0^\infty e^{-2\delta t} {}_t p_x \mu_{x+t}\,dt = \int_0^\infty (v^2)^t {}_t p_x \mu_{x+t}\,dt$$

Therefore:

$$\text{Var}(Z) = {}^2\bar{A}_x - (\bar{A}_x)^2$$

Under constant force of mortality $\mu$ and constant force of interest $\delta$:
$${}_t p_x \mu_{x+t} = e^{-\mu t} \mu$$
$$\bar{A}_x = \int_0^\infty e^{-\delta t} e^{-\mu t} \mu\,dt = \mu \int_0^\infty e^{-(\delta + \mu) t}\,dt = \frac{\mu}{\delta + \mu}$$
$${}^2\bar{A}_x = \frac{\mu}{2\delta + \mu}$$
$$\text{Var}(Z) = \frac{\mu}{2\delta + \mu} - \left( \frac{\mu}{\delta + \mu} \right)^2$$

## 4.3 Discrete Whole Life Insurance: $A_x$ and Commutation Functions

In a **Discrete Whole Life Insurance**, a unit benefit of $1$ is paid at the end of the year of death: $Z = v^{K_x + 1}$.

### Actuarial Present Value ($A_x$)
Summing over all possible discrete integer death years $k = 0, 1, 2, \dots$:

$$A_x = \mathbb{E}[v^{K_x + 1}] = \sum_{k=0}^\infty v^{k+1} P(K_x = k) = \sum_{k=0}^\infty v^{k+1} {}_k| q_x = \sum_{k=0}^\infty v^{k+1} {}_k p_x q_{x+k}$$

The second moment is:
$${}^2 A_x = \sum_{k=0}^\infty (v^2)^{k+1} {}_k| q_x$$
$$\text{Var}(Z) = {}^2 A_x - (A_x)^2$$

### Classical Commutation Functions: $D_x, C_x, M_x$
Before digital computers, evaluating summations across life table columns was labor-intensive. Actuaries streamlined calculations by pre-computing **Commutation Functions** combining interest discounting and cohort survival numbers:

1. **Discounted Cohort Survivors ($D_x$)**:
   $$D_x = v^x \ell_x$$
2. **Discounted Cohort Deaths ($C_x$)**:
   $$C_x = v^{x+1} d_x$$
3. **Accumulated Discounted Deaths ($M_x$)**:
   $$M_x = \sum_{y=x}^{\omega - 1} C_y = \sum_{y=x}^{\omega - 1} v^{y+1} d_y$$

Multiplying $A_x$ by $v^x \ell_x / (v^x \ell_x) = 1$:
$$A_x = \sum_{k=0}^\infty v^{k+1} \frac{d_{x+k}}{\ell_x} = \frac{1}{v^x \ell_x} \sum_{k=0}^\infty v^{x+k+1} d_{x+k} = \frac{\sum_{y=x}^\infty C_y}{D_x}$$

$$A_x = \frac{M_x}{D_x}$$

The entire infinite summation collapses into the ratio of two single numbers looked up from a commutation table!

## 4.4 Term Insurance, Pure Endowment, and Endowment Insurance

Not all life insurance policies cover the entire lifespan. Commercial insurance packages combine term coverage with survival endowments:

### 1. Term Life Insurance ($A_{x:\overline{n}|}^1$ and $\bar{A}_{x:\overline{n}|}^1$)
A **Term Life Insurance** pays a benefit of $1$ unit if and only if $(x)$ dies within a fixed policy term of $n$ years. If the insured survives past $n$ years, the policy expires with zero payout.

- Continuous:
  $$\bar{A}_{x:\overline{n}|}^1 = \int_0^n v^t {}_t p_x \mu_{x+t}\,dt$$
- Discrete:
  $$A_{x:\overline{n}|}^1 = \sum_{k=0}^{n-1} v^{k+1} {}_k| q_x = \frac{\sum_{k=0}^{n-1} C_{x+k}}{D_x} = \frac{M_x - M_{x+n}}{D_x}$$

### 2. Pure Endowment ($A_{x:\overline{n}|}^{\;\;1}$ or ${}_n E_x$)
A **Pure Endowment** contract pays a benefit of $1$ unit at time $n$ if and only if $(x)$ survives to attained age $x + n$. If $(x)$ dies prior to time $n$, zero benefit is paid.

The present value random variable is:
$$Z = \begin{cases} v^n & \text{if } T_x > n \\ 0 & \text{if } T_x \le n \end{cases}$$

The Actuarial Present Value is denoted ${}_n E_x$:

$${}_n E_x = v^n P(T_x > n) = v^n {}_n p_x = \frac{v^{x+n} \ell_{x+n}}{v^x \ell_x} = \frac{D_{x+n}}{D_x}$$

The second moment is:
$${}^2({}_n E_x) = (v^{2n}) {}_n p_x = v^n {}_n E_x$$
$$\text{Var}(Z) = (v^{2n}) {}_n p_x - (v^n {}_n p_x)^2 = v^{2n} {}_n p_x (1 - {}_n p_x) = v^{2n} {}_n p_x {}_n q_x$$

### 3. Endowment Insurance ($A_{x:\overline{n}|}$ and $\bar{A}_{x:\overline{n}|}$)
An **Endowment Insurance** combines term insurance and pure endowment: it pays $1$ unit at the time of death if death occurs before $n$, OR pays $1$ unit at maturity $n$ if $(x)$ survives to time $n$:

$$A_{x:\overline{n}|} = A_{x:\overline{n}|}^1 + {}_n E_x = \frac{M_x - M_{x+n} + D_{x+n}}{D_x}$$

$$\bar{A}_{x:\overline{n}|} = \bar{A}_{x:\overline{n}|}^1 + {}_n E_x$$

## 4.5 Deferred and Varying Life Insurance Contracts

### 1. Deferred Life Insurance (${}_{m|} A_x$)
A deferred insurance contract provides whole life protection commencing only after an initial deferral period of $m$ years. If $(x)$ dies during the first $m$ years, no benefit is paid.

$${}_{m|} A_x = \sum_{k=m}^\infty v^{k+1} {}_k| q_x = v^m {}_m p_x A_{x+m} = {}_m E_x \cdot A_{x+m} = \frac{M_{x+m}}{D_x}$$

### 2. Arithmetically Increasing Whole Life Insurance ($(IA)_x$)
An increasing insurance contract pays a death benefit of $k + 1$ units if death occurs in policy year $k + 1$ (benefit is $\$1$ in year 1, $\$2$ in year 2, $\$3$ in year 3, etc.):

$$(IA)_x = \sum_{k=0}^\infty (k + 1) v^{k+1} {}_k| q_x = \frac{\sum_{k=0}^\infty (k + 1) C_{x+k}}{D_x}$$

Defining the second-order commutation function $R_x = \sum_{y=x}^\infty M_y$:

$$(IA)_x = \frac{R_x}{D_x}$$

## 4.6 Approximating Claims Payable at the Moment of Death

In real life insurance practice, death benefits are paid immediately upon receipt of proof of death (typically within a few weeks of mortality), rather than delayed until the end of the policy anniversary year. 

To approximate continuous claims $\bar{A}$ from discrete life table values $A$, actuaries assume the **Uniform Distribution of Deaths (UDD)** over each single year of age:

$$\bar{A}_x \approx \frac{i}{\delta} A_x$$

$$\bar{A}_{x:\overline{n}|}^1 \approx \frac{i}{\delta} A_{x:\overline{n}|}^1$$

Since $\frac{i}{\delta} = \frac{e^\delta - 1}{\delta} \approx 1 + \frac{\delta}{2} \approx 1 + \frac{i}{2}$, paying benefits immediately at death rather than at year-end increases the net single premium by approximately half a year's interest ($\sim 2\%$ to $4\%$).

For an endowment insurance:
$$\bar{A}_{x:\overline{n}|} = \bar{A}_{x:\overline{n}|}^1 + {}_n E_x \approx \frac{i}{\delta} A_{x:\overline{n}|}^1 + {}_n E_x$$
Notice that the factor $i/\delta$ applies *only* to the term insurance death component, never to the pure endowment maturity component ${}_n E_x$ (which is always paid exactly at integer time $n$).

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

## 4.12 Joint-and-Survivor Annuity Reductions and Cash Refund Guarantees

In defined benefit pension schemes and individual commercial retirement planning, retiring couples rarely select a joint life annuity that terminates on the first death, because the surviving spouse would be left without income. Nor do they typically select an unreduced 100% joint-and-survivor annuity, which carries high premium costs.

Instead, the vast majority of retirement plans provide **Joint-and-Survivor Annuities with Benefit Reductions**.

### 1. The Joint-and-Survivor Reduction Model
Consider a retirement annuity issued to $(x)$ (the primary retiree) and $(y)$ (the contingent spouse).
The contract pays:
- Benefit rate 1 per year while both $(x)$ and $(y)$ are alive.
- Benefit rate $\theta_1$ per year to $(x)$ if $(y)$ dies first ($0 < \theta_1 \le 1$).
- Benefit rate $\theta_2$ per year to $(y)$ if $(x)$ dies first ($0 < \theta_2 \le 1$).
- Zero payments after both lives have died.

In standard pension design, commonly selected reduction factors are $\theta_1 = 1.0$ (no reduction to the primary worker) and $\theta_2 = 0.50$ ($50\%$ joint-and-survivor) or $\theta_2 = 0.667$ ($66.7\%$ joint-and-survivor).

Let $I_x(t)$ and $I_y(t)$ be the survival indicators. The payment rate at duration $t$ is:
$$\rho(t) = I_x(t) I_y(t) + \theta_1 I_x(t)(1 - I_y(t)) + \theta_2 I_y(t)(1 - I_x(t))$$
Rearranging terms:
$$\rho(t) = \theta_1 I_x(t) + \theta_2 I_y(t) + (1 - \theta_1 - \theta_2) I_x(t) I_y(t)$$

Taking expectations and discounting:

$$\bar{a} = \theta_1 \bar{a}_x + \theta_2 \bar{a}_y + (1 - \theta_1 - \theta_2) \bar{a}_{xy}$$

For the symmetric case where the benefit reduces to fraction $\theta$ upon either spouse's death ($\theta_1 = \theta_2 = \theta$):
$$\bar{a} = \theta \bar{a}_x + \theta \bar{a}_y + (1 - 2\theta) \bar{a}_{xy}$$

If $\theta = 1/2$ (a $50\%$ reduction upon the first death):
$$\bar{a} = \frac{1}{2} \bar{a}_x + \frac{1}{2} \bar{a}_y$$
Remarkably, the joint life status $\bar{a}_{xy}$ cancels out completely, and the annuity value is simply the arithmetic average of the two single life annuities!

### 2. Cash Refund and Installment Refund Annuities
Retirees are often reluctant to purchase life annuities because of the perceived risk that if they die shortly after retirement, the insurer retains the remaining capital. Insurers resolve this behavioral friction by offering **Refund Annuities**:
- **Cash Refund Annuity**: If the annuitant dies before cumulative annuity payments equal the initial purchase premium $P$, the remaining balance $P - \sum \text{Payments}$ is refunded immediately as a lump sum death benefit.
- **Installment Refund Annuity**: If total payments are less than $P$, the periodic annuity payments continue to the designated beneficiary until cumulative payments equal $P$.
Actuarial valuation splits the refund annuity into a life annuity plus a decreasing term insurance benefit on $(x)$, providing capital certainty to risk-averse pensioners.

## Fully worked question 1: Discrete Whole Life and Endowment Insurance Valuation via Commutation Functions

### Question
An extract from an actuarial valuation table compiled at an effective annual interest rate of $i = 5.00\%$ ($i = 0.05$, $v = 1/1.05 \approx 0.952381$) reports the following commutation values:
- $D_{40} = 15,000$
- $D_{50} = 8,800$
- $D_{60} = 4,800$
- $M_{40} = 4,200$
- $M_{50} = 3,300$
- $M_{60} = 2,400$
- $R_{40} = 84,000$

A life aged $40$ purchases various life insurance policies. Compute:
1. The Net Single Premium for a Whole Life Insurance of $100,000\text{ BDT}$ payable at the end of the year of death ($100,000 A_{40}$).
2. The Net Single Premium for a 20-Year Term Insurance of $100,000\text{ BDT}$ ($100,000 A_{40:\overline{20}|}^1$).
3. The Net Single Premium for a 20-Year Pure Endowment of $100,000\text{ BDT}$ ($100,000 {}_{20} E_{40}$).
4. The Net Single Premium for a 20-Year Endowment Insurance of $100,000\text{ BDT}$ ($100,000 A_{40:\overline{20}|}$).
5. The Net Single Premium for an Increasing Whole Life Insurance paying $10,000\text{ BDT}$ in Year 1, $20,000\text{ BDT}$ in Year 2, increasing by $10,000\text{ BDT}$ each year thereafter ($10,000 (IA)_{40}$).

### Solution, step 1: Whole life insurance valuation
Using $A_x = M_x / D_x$:
$$A_{40} = \frac{M_{40}}{D_{40}} = \frac{4,200}{15,000} = 0.28000$$
For a sum insured of $100,000\text{ BDT}$:
$$\text{NSP}_{\text{whole life}} = 100,000 \times 0.28000 = 28,000\text{ BDT}$$

### Solution, step 2: 20-Year term insurance valuation
For a 20-year term from age 40, terminal age is $40 + 20 = 60$:
$$A_{40:\overline{20}|}^1 = \frac{M_{40} - M_{60}}{D_{40}} = \frac{4,200 - 2,400}{15,000} = \frac{1,800}{15,000} = 0.12000$$
For a sum insured of $100,000\text{ BDT}$:
$$\text{NSP}_{\text{term}} = 100,000 \times 0.12000 = 12,000\text{ BDT}$$

### Solution, step 3: 20-Year pure endowment valuation
$${}_{20} E_{40} = \frac{D_{60}}{D_{40}} = \frac{4,800}{15,000} = 0.32000$$
For a maturity benefit of $100,000\text{ BDT}$:
$$\text{NSP}_{\text{pure endowment}} = 100,000 \times 0.32000 = 32,000\text{ BDT}$$

### Solution, step 4: 20-Year endowment insurance valuation
An endowment insurance is the sum of term insurance and pure endowment:
$$A_{40:\overline{20}|} = A_{40:\overline{20}|}^1 + {}_{20} E_{40} = 0.12000 + 0.32000 = 0.44000$$
Equivalently, via commutation functions:
$$A_{40:\overline{20}|} = \frac{M_{40} - M_{60} + D_{60}}{D_{40}} = \frac{4,200 - 2,400 + 4,800}{15,000} = \frac{6,600}{15,000} = 0.44000$$
For a sum insured of $100,000\text{ BDT}$:
$$\text{NSP}_{\text{endowment}} = 100,000 \times 0.44000 = 44,000\text{ BDT}$$

### Solution, step 5: Increasing whole life insurance valuation
Using $(IA)_x = R_x / D_x$:
$$(IA)_{40} = \frac{R_{40}}{D_{40}} = \frac{84,000}{15,000} = 5.60000$$
For a scale benefit of $10,000\text{ BDT}$ per step:
$$\text{NSP}_{\text{increasing}} = 10,000 \times 5.60000 = 56,000\text{ BDT}$$

## Fully worked question 2: Stochastic Variance of Present Value Loss Variable and Risk Pools

### Question
An insurance company sells identical independent 10-year term insurance policies to a portfolio of $N = 100$ lives, each aged $x = 50$. Each policy pays a lump-sum death benefit of $B = 250,000\text{ BDT}$ at the end of the year of death if the insured dies within 10 years.

The actuarial life table and interest rate parameters are:
- Effective annual interest rate: $i = 6.00\%$ ($i = 0.06$)
- Single policy term actuarial values:
  $$A_{50:\overline{10}|}^1 = 0.06500, \qquad {}^2 A_{50:\overline{10}|}^1 = 0.02450$$

Let $S = \sum_{j=1}^{100} Z_j$ denote the aggregate present value of claims across the entire portfolio, where $Z_j = B \cdot v^{K_{50, j} + 1} \mathbb{I}(K_{50, j} < 10)$.

Perform the following calculations:
1. Compute the expected value $\mathbb{E}[Z]$ and standard deviation $\sigma_Z$ for a single policy.
2. Compute the expected aggregate claims $\mathbb{E}[S]$ and standard deviation $\sigma_S$ for the portfolio of 100 policies.
3. Compute the coefficient of variation ($CV = \sigma / \mathbb{E}$) for a single policy and for the 100-policy portfolio.
4. Using the Central Limit Theorem, calculate the total capital reserve $C$ the insurer must establish at policy inception so that the probability of aggregate claims exceeding reserves is no more than $1.0\%$ ($P(S > C) \le 0.01$, with $Z_{0.01} = 2.326$).
5. Compute the required contingency risk loading as a percentage of expected claims.

### Solution, step 1: Single policy mean and standard deviation
For a single policy with benefit $B = 250,000\text{ BDT}$:
$$\mathbb{E}[Z] = B \cdot A_{50:\overline{10}|}^1 = 250,000 \times 0.06500 = 16,250\text{ BDT}$$

The variance of a single policy loss variable is:
$$\text{Var}(Z) = B^2 \left[ {}^2 A_{50:\overline{10}|}^1 - (A_{50:\overline{10}|}^1)^2 \right]$$
$$(A_{50:\overline{10}|}^1)^2 = (0.06500)^2 = 0.004225$$
$${}^2 A_{50:\overline{10}|}^1 - (A_{50:\overline{10}|}^1)^2 = 0.02450 - 0.004225 = 0.020275$$
$$\text{Var}(Z) = (250,000)^2 \times 0.020275 = 6.25 \times 10^{10} \times 0.020275 = 1,267,187,500\text{ BDT}^2$$
$$\sigma_Z = \sqrt{1,267,187,500} \approx 35,597.58\text{ BDT}$$

### Solution, step 2: Aggregate portfolio mean and standard deviation
For $N = 100$ independent, identically distributed policies:
$$\mathbb{E}[S] = N \cdot \mathbb{E}[Z] = 100 \times 16,250 = 1,625,000\text{ BDT}$$
$$\text{Var}(S) = N \cdot \text{Var}(Z) = 100 \times 1,267,187,500 = 126,718,750,000\text{ BDT}^2$$
$$\sigma_S = \sqrt{N} \cdot \sigma_Z = \sqrt{100} \times 35,597.58 = 10 \times 35,597.58 = 355,975.80\text{ BDT}$$

### Solution, step 3: Evaluate Coefficient of Variation ($CV$)
- Single policy:
  $$CV_Z = \frac{\sigma_Z}{\mathbb{E}[Z]} = \frac{35,597.58}{16,250} \approx 2.1906 = 219.06\%$$
- 100-policy portfolio:
  $$CV_S = \frac{\sigma_S}{\mathbb{E}[S]} = \frac{355,975.80}{1,625,000} = \frac{CV_Z}{\sqrt{N}} = \frac{2.1906}{10} \approx 0.2191 = 21.91\%$$
Pooling 100 independent risks reduces relative volatility by a factor of $\sqrt{100} = 10\times$, illustrating the foundational economic law of insurance risk pooling!

### Solution, step 4: Compute $99\%$ confidence solvency reserve $C$
By the Central Limit Theorem, aggregate claims $S$ asymptotically follow a normal distribution $S \sim \mathcal{N}(\mathbb{E}[S], \sigma_S^2)$:
$$P(S \le C) = 0.99 \implies \frac{C - \mathbb{E}[S]}{\sigma_S} = Z_{0.01} = 2.326$$
$$C = \mathbb{E}[S] + 2.326 \cdot \sigma_S = 1,625,000 + (2.326 \times 355,975.80)$$
$$= 1,625,000 + 828,000 = 2,453,000\text{ BDT}$$
The insurer must maintain **$2,453,000\text{ BDT}$** in reserves to ensure solvency at a $99\%$ confidence level.

### Solution, step 5: Determine contingency risk loading
$$\text{Risk Loading} = C - \mathbb{E}[S] = 2,453,000 - 1,625,000 = 828,000\text{ BDT}$$
$$\% \text{Risk Loading} = \frac{828,000}{1,625,000} \times 100\% \approx 50.95\%$$
The insurer must collect a $50.95\%$ safety buffer over expected claims to protect against extreme statistical mortality clusters in a small portfolio of 100 lives.

## Fully worked question 3: Continuous Versus Discrete Insurance Under UDD and De Moivre's Law

### Question
A continuous whole life insurance policy pays $100,000\text{ BDT}$ at the moment of death of a life aged $x = 60$. Mortality follows De Moivre's Law with terminal age $\omega = 100$. The effective annual interest rate is $i = 6.00\%$ ($i = 0.06$).

Perform the following calculations:
1. Determine the force of interest $\delta$ and the discount factor $v$.
2. Compute the exact Actuarial Present Value $\bar{A}_{60}$ using the continuous integral definition under De Moivre's Law.
3. Compute the discrete Actuarial Present Value $A_{60}$ assuming payments at the end of the year of death.
4. Compute the UDD approximation $\bar{A}_{60} \approx \frac{i}{\delta} A_{60}$ and determine the approximation error relative to the exact integral.
5. Compute the second moment ${}^2\bar{A}_{60}$ and the standard deviation of the present value loss variable.

### Solution, step 1: Parameters under De Moivre's Law
For $x = 60$ and $\omega = 100$:
$$\omega - x = 100 - 60 = 40\text{ years}$$
Under De Moivre's Law, the future lifetime $T_{60}$ is uniformly distributed on $[0, 40]$:
$$f_{60}(t) = \frac{1}{40}, \qquad 0 \le t \le 40$$
The financial interest parameters are:
$$i = 0.06 \implies \delta = \ln(1.06) \approx 0.0582689$$
$$v = (1.06)^{-1} \approx 0.943396$$

### Solution, step 2: Exact continuous APV $\bar{A}_{60}$
$$\bar{A}_{60} = \int_0^{40} e^{-\delta t} f_{60}(t)\,dt = \frac{1}{40} \int_0^{40} e^{-\delta t}\,dt = \frac{1}{40} \left[ \frac{1 - e^{-40 \delta}}{\delta} \right] = \frac{\bar{a}_{\overline{40}|}}{40}$$
Calculate $e^{-40 \delta}$:
$$e^{-40 \delta} = (1.06)^{-40} \approx 0.097222$$
$$1 - e^{-40 \delta} = 1 - 0.097222 = 0.902778$$
$$\bar{a}_{\overline{40}|} = \frac{0.902778}{0.0582689} \approx 15.49331$$
$$\bar{A}_{60} = \frac{15.49331}{40} \approx 0.387333$$
For a $100,000\text{ BDT}$ benefit:
$$\text{APV}_{\text{continuous}} = 100,000 \times 0.387333 = 38,733.30\text{ BDT}$$

### Solution, step 3: Discrete APV $A_{60}$
Under De Moivre's Law, $q_{60+k} = \frac{1}{40 - k}$, and ${}_k| q_{60} = \frac{1}{40}$ for each integer year $k = 0, 1, \dots, 39$:
$$A_{60} = \sum_{k=0}^{39} v^{k+1} \cdot \frac{1}{40} = \frac{1}{40} \sum_{k=0}^{39} v^{k+1} = \frac{a_{\overline{40}|}}{40}$$
Calculate $a_{\overline{40}|0.06}$:
$$a_{\overline{40}|} = \frac{1 - (1.06)^{-40}}{0.06} = \frac{1 - 0.097222}{0.06} = \frac{0.902778}{0.06} \approx 15.04630$$
$$A_{60} = \frac{15.04630}{40} \approx 0.376158$$
$$\text{APV}_{\text{discrete}} = 100,000 \times 0.376158 = 37,615.80\text{ BDT}$$

### Solution, step 4: UDD approximation and error assessment
The UDD multiplier is:
$$\frac{i}{\delta} = \frac{0.06}{0.0582689} \approx 1.029709$$
Approximating $\bar{A}_{60}$:
$$\bar{A}_{60}^{\text{UDD}} \approx \frac{i}{\delta} A_{60} = 1.029709 \times 0.376158 \approx 0.387333$$
Notice that because De Moivre’s Law has a constant death density $f(t) = 1/40$, deaths are *exactly* uniformly distributed over each single year of age! 
Consequently, the UDD approximation is not merely an approximation—it is **mathematically exact to 6 decimal places**!
$$\text{Exact } \bar{A}_{60} = 0.387333, \qquad \text{UDD } \bar{A}_{60} = 0.387333$$

### Solution, step 5: Second moment and standard deviation
Evaluate at $2\delta = 2 \times 0.0582689 = 0.1165378$:
$$e^{-40(2\delta)} = (e^{-40\delta})^2 = (0.097222)^2 \approx 0.009452$$
$${}^2\bar{A}_{60} = \frac{1 - e^{-40(2\delta)}}{40(2\delta)} = \frac{1 - 0.009452}{40 \times 0.1165378} = \frac{0.990548}{4.661512} \approx 0.212495$$
The variance is:
$$\text{Var}(Z) = B^2 [{}^2\bar{A}_{60} - (\bar{A}_{60})^2]$$
$$(\bar{A}_{60})^2 = (0.387333)^2 \approx 0.150027$$
$${}^2\bar{A}_{60} - (\bar{A}_{60})^2 = 0.212495 - 0.150027 = 0.062468$$
$$\sigma_Z = 100,000 \times \sqrt{0.062468} = 100,000 \times 0.249936 \approx 24,994\text{ BDT}$$
The standard deviation of the present value of the death claim is **$24,994\text{ BDT}$**.
