# Unit 8: Mathematical Demography, Multiple Decrement Models & Population Dynamics

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

## 8.10 Numerical Inversion of Aggregate Claims: The Fast Fourier Transform (FFT)

While Panjer's recursion provides an exact method for computing aggregate claims distributions when claim frequency belongs to the $(a, b, 0)$ or $(a, b, 1)$ classes, many empirical insurance portfolios feature claim frequency distributions outside these families (e.g., Delaporte distributions, zero-modified Poisson-inverse Gaussian mixtures).

To compute the aggregate claims distribution $g_k = P(S = k)$ for arbitrary frequency and continuous severity distributions, modern actuarial science utilizes **Characteristic Function Inversion via the Fast Fourier Transform (FFT)**.

### 1. The Characteristic Function of Aggregate Claims
Recall that the aggregate claims random variable is $S = \sum_{j=1}^N X_j$.
Let $\phi_X(t) = \mathbb{E}[e^{itX}]$ denote the characteristic function of individual claim severity $X$, and let $P_N(z) = \mathbb{E}[z^N]$ denote the probability generating function of claim count $N$.

By the tower property of conditional expectation:

$$\phi_S(t) = \mathbb{E}\left[ e^{itS} \right] = \mathbb{E}\left[ \mathbb{E}\left[ \exp\left( it \sum_{j=1}^N X_j \right) \Bigg| N \right] \right] = \mathbb{E}\left[ (\phi_X(t))^N \right] = P_N(\phi_X(t))$$

For a Compound Poisson process with frequency parameter $\lambda$:
$$\phi_S(t) = \exp\left( \lambda (\phi_X(t) - 1) \right)$$
For a Compound Negative Binomial process with parameters $(r, p)$:
$$\phi_S(t) = \left( \frac{p}{1 - (1 - p)\phi_X(t)} \right)^r$$

### 2. Discretization and Discrete Fourier Transform (DFT)
Let claim severity be discretized on a regular grid of size $h > 0$ with $M = 2^m$ points ($M \in \{1024, 2048, 4096, 8192\}$):
$$\mathbf{f} = [f_0, f_1, f_2, \dots, f_{M-1}]^T, \quad f_k = P(X = k \cdot h)$$

The Discrete Fourier Transform of the severity vector $\mathbf{f}$ is:
$$\hat{f}_k = \sum_{j=0}^{M-1} f_j \exp\left( \frac{2\pi i \cdot j \cdot k}{M} \right) \quad \text{for } k = 0, 1, \dots, M-1$$
This is computed in $\mathcal{O}(M \log M)$ operations using the Cooley-Tukey FFT algorithm.

Next, the aggregate characteristic values $\hat{g}_k$ are evaluated directly through the theoretical generating relation:
$$\hat{g}_k = P_N(\hat{f}_k) = \exp\left( \lambda (\hat{f}_k - 1) \right)$$

Finally, the probability mass function of aggregate claims $\mathbf{g} = [g_0, g_1, \dots, g_{M-1}]^T$ is recovered via the Inverse Fast Fourier Transform (IFFT):

$$g_j = \frac{1}{M} \sum_{k=0}^{M-1} \hat{g}_k \exp\left( -\frac{2\pi i \cdot j \cdot k}{M} \right)$$

### 3. Mitigating Aliasing and Wrapping Errors: Exponential Tilting
Because the discrete Fourier transform implicitly assumes periodic boundary conditions with period $M$, aggregate claim probabilities beyond $M$ wrap around and contaminate early probabilities $g_0, g_1$, creating **Aliasing / Wrapping Error**.

To eliminate aliasing, actuaries deploy **Exponential Tilting (Esscher Transform)**:
1. Define the tilted severity distribution:
   $$\tilde{f}_j = e^{-\theta j} f_j$$
   where $\theta > 0$ is a damping parameter.
2. Run the FFT and IFFT on the tilted distribution to obtain the tilted aggregate probabilities $\tilde{g}_j$.
3. Untilt the resulting aggregate distribution:
   $$g_j = e^{\theta j} \tilde{g}_j$$
Exponential damping suppresses tail values prior to periodicity wrapping, reducing aliasing error below machine precision ($10^{-14}$) and ensuring pristine aggregate stop-loss reinsurance pricing.

## 8.11 Liability-Driven Investment (LDI) and Dynamic Pension Solvency

In defined benefit pension management, traditional asset allocation models that focus purely on maximizing asset returns (e.g., $60\%$ equities / $40\%$ bonds) expose pension plans to catastrophic funding ratio collapses when interest rates drop.

To guarantee solvency, pension funds deploy **Liability-Driven Investment (LDI)**.

### 1. The Pension Funding Ratio and Surplus Volatility
Let $A$ be the market value of pension plan assets, and let $L$ be the Present Value of Defined Benefit Liabilities ($PVFB$ or $AAL$).
The **Funding Ratio** is:
$$FR = \frac{A}{L}$$
The pension **Surplus** is:
$$S = A - L$$

The variance of changes in pension surplus $\Delta S = \Delta A - \Delta L$ is:

$$\sigma_S^2 = \sigma_A^2 + \sigma_L^2 - 2 \rho_{AL} \sigma_A \sigma_L$$

where $\sigma_A$ is asset volatility, $\sigma_L$ is liability volatility, and $\rho_{AL}$ is the asset-liability correlation.

If assets are invested in equities while liabilities consist of long-duration guaranteed bonds, the asset-liability correlation $\rho_{AL}$ is close to zero or negative. Consequently, surplus volatility is massive ($\sigma_S^2 \approx \sigma_A^2 + \sigma_L^2$). If interest rates drop by 100 basis points, liabilities surge by $20\%$, causing the funding ratio to collapse into deep deficit.

### 2. The LDI Portfolio Bifurcation
LDI decomposes the pension portfolio into two dedicated structural allocations:
1. **The Liability Hedging Portfolio (LHP)**: Designed strictly to achieve $\rho_{AL} \approx 1.0$ and match the key rate duration and inflation sensitivity of liabilities:
   - Physical long-dated sovereign bonds and index-linked gilts.
   - Derivative overlays: **Interest Rate Swaps**, **Inflation Swaps**, and **Swaptions**. In a receiver swap, the pension fund receives fixed interest and pays floating, synthesizing long bond duration with minimal cash capital outlay.
2. **The Return-Seeking Portfolio (RSP)**: Invested in high-expected-return growth assets (global equities, private infrastructure, private credit, and real estate) to systematically eliminate any existing unfunded actuarial liability ($UAL$).

By matching liability duration via synthetic swaps in the LHP, $\rho_{AL} \to 1.0$ and $\sigma_L \approx \sigma_A^{\text{hedging}}$, surplus volatility $\sigma_S^2 \to 0$. This stabilizes employer pension contribution rates, insulates corporate sponsors from balance sheet volatility, and secures the retirement pensions of millions of workers.

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
