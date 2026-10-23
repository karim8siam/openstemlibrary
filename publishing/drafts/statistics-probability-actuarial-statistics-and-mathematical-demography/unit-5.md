# Unit 5: Life Annuities: Continuous, Discrete, Varying & Guaranteed Contracts

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

## 5.12 Demographic Data Quality: Age-Heaping and Whipple's Index

In national census enumeration and demographic surveys in developing economies, reported age distributions frequently exhibit artificial spikes at specific terminal digits, most notably ages ending in 0 and 5 (such as ages 20, 25, 30, 35, 40, etc.). This distortion is termed **Age-Heaping** or **Digit Preference**.

Age-heaping arises because illiterate or innumerate respondents do not know their exact birth year and round their estimated age to the nearest multiple of 5 or 10. To assess the statistical accuracy and data integrity of census returns prior to life table construction, mathematical demographers calculate standardized quality indices.

### 1. Whipple's Index of Digit Preference
George C. Whipple formulated an index measuring the concentration of reported population at terminal digits 0 and 5 over the adult age span from 23 to 62:

$$W = \frac{\sum_{k=5}^{12} P_{5k}}{\frac{1}{5} \sum_{x=23}^{62} P_x} \times 100 = \frac{5 \sum_{k=5}^{12} P_{5k}}{\sum_{x=23}^{62} P_x} \times 100$$
where $P_{5k}$ denotes the population enumerated at ages $25, 30, 35, 40, 45, 50, 55, 60$.

*Interpretation Scale of Whipple's Index*:
- **$W < 105$**: Highly accurate demographic data (virtually no digit preference).
- **$105 \le W < 110$**: Fairly accurate data.
- **$110 \le W < 125$**: Approximate data with noticeable rounding.
- **$125 \le W < 175$**: Rough data with substantial distortion.
- **$W \ge 175$**: Very rough data; at the extreme $W = 500$, every single respondent reported an age ending in 0 or 5.

### 2. Myers' Blended Method
Whipple's index assumes that the true population in the age range $23 - 62$ is uniformly distributed, ignoring secular mortality declines across age. Robert J. Myers (1940) developed the **Myers' Blended Method**, which calculates the percentage deviation of reported ages for *every single terminal digit* $0, 1, 2, \dots, 9$ while mathematically neutralizing mortality attrition.

Myers' summary index equals half the sum of absolute deviations from $10\%$:
$$M = \frac{1}{2} \sum_{d=0}^9 |V_d - 10\%|$$
where $V_d$ is the blended percentage of population reporting terminal digit $d$. A Myers' score near 0 indicates pristine demographic record-keeping, whereas scores above 10 signal serious enumeration bias requiring mathematical graduation before life table compilation.

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
