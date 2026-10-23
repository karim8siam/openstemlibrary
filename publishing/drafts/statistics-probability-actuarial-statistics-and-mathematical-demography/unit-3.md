# Unit 3: Survival Models, Life Tables & Parametric Mortality Laws

## 3.1 The Future Lifetime Random Variable and Survival Probabilities

The mathematical foundation of actuarial life contingencies centers on the continuous random variable governing human mortality. Let a newborn infant (age $0$) have total lifetime modeled by a non-negative continuous random variable $X \ge 0$, defined on a probability space $(\Omega, \mathcal{F}, P)$ with cumulative distribution function $F_0(x) = P(X \le x)$ and survival function:

$$S_0(x) = P(X > x) = 1 - F_0(x), \qquad x \ge 0$$

Now consider a life who has successfully survived to attain exact age $x \ge 0$ (denoted in classical actuarial notation as $(x)$). The future remaining lifetime of $(x)$ before death is modeled by the continuous random variable $T_x$:

$$T_x = X - x \mid X > x$$

The condition $X > x$ implies that $T_x$ takes values on $[0, \infty)$. The conditional survival function of $(x)$, denoted in international actuarial notation as ${}_t p_x$, is the probability that a life aged $x$ will survive for at least $t$ additional years:

$${}_t p_x = P(T_x > t) = P(X > x + t \mid X > x) = \frac{P(X > x + t)}{P(X > x)} = \frac{S_0(x + t)}{S_0(x)}$$

When $t = 1$, the subscript $1$ is omitted by convention: $p_x = {}_1 p_x = S_0(x + 1)/S_0(x)$ represents the one-year survival probability at age $x$.

### The Mortality Function: ${}_t q_x$
The cumulative distribution function of $T_x$, denoted ${}_t q_x$, represents the probability that a life aged $x$ will die within $t$ years:

$${}_t q_x = P(T_x \le t) = 1 - {}_t p_x = 1 - \frac{S_0(x + t)}{S_0(x)} = \frac{S_0(x) - S_0(x + t)}{S_0(x)}$$

When $t = 1$, $q_x = {}_1 q_x$ is the celebrated **one-year mortality rate** at age $x$.

### Deferred Probabilities of Death: ${}_{u|t} q_x$
The deferred probability ${}_{u|t} q_x$ represents the probability that $(x)$ survives for $u$ years and subsequently dies within the following $t$ years (between age $x + u$ and $x + u + t$):

$${}_{u|t} q_x = P(u < T_x \le u + t) = {}_u p_x - {}_{u+t} p_x = {}_u p_x \cdot {}_t q_{x+u}$$

When $t = 1$, the deferred term is written simply as ${}_{u|} q_x = {}_u p_x \cdot q_{x+u}$, representing the probability that a person aged $x$ survives $u$ full years and dies during the $(u+1)$-th year.

### Multiplicative Chain Rule
For arbitrary non-negative durations $t$ and $s$:

$${}_{t+s} p_x = {}_t p_x \cdot {}_s p_{x+t}$$

Survival from age $x$ to age $x + t + s$ is the product of surviving from $x$ to $x + t$, and then surviving from $x + t$ to $x + t + s$.

## 3.2 The Force of Mortality: $\mu_{x+t}$

The **force of mortality** (denoted $\mu_{x+t}$ or $\mu(x + t)$) represents the instantaneous hazard rate of death for a life aged $x + t$:

$$\mu_{x+t} = \lim_{\Delta t \to 0} \frac{P(t \le T_x < t + \Delta t \mid T_x > t)}{\Delta t}$$

Using conditional probability:
$$P(t \le T_x < t + \Delta t \mid T_x > t) = \frac{{}_t p_x - {}_{t+\Delta t} p_x}{{}_t p_x}$$
Dividing by $\Delta t$ and taking the limit:

$$\mu_{x+t} = -\frac{1}{{}_t p_x} \frac{d}{dt} ({}_t p_x) = -\frac{d}{dt} \ln({}_t p_x)$$

Since ${}_t p_x = S_0(x + t) / S_0(x)$:

$$\mu_{x+t} = -\frac{S_0'(x + t)}{S_0(x + t)} = -\frac{d}{dx} \ln S_0(x + t) = \mu(x + t)$$

The force of mortality depends purely on attained biological age $x + t$, completely independent of the starting baseline age $x$.

### Integrating the Force of Mortality
Integrating $-\mu_{x+s}$ from $s = 0$ to $s = t$:

$$\int_0^t \mu_{x+s}\,ds = -\ln({}_t p_x) + \ln({}_0 p_x) = -\ln({}_t p_x) \quad (\text{since } {}_0 p_x = 1)$$

Exponentiating both sides yields the foundational relationship connecting survival probability to the force of mortality:

$${}_t p_x = \exp\left( -\int_0^t \mu_{x+s}\,ds \right)$$

The probability density function of $T_x$, denoted $f_x(t)$, is the negative derivative of survival:

$$f_x(t) = -\frac{d}{dt} ({}_t p_x) = {}_t p_x \cdot \mu_{x+t}$$

The probability of dying at infinitesimal instant $t$ is the probability of surviving to time $t$ (${}_t p_x$) multiplied by the instantaneous hazard of dying at that moment ($\mu_{x+t}$).

## 3.3 Curtate Future Lifetime and Expectations of Life

### The Curtate Future Lifetime ($K_x$)
In financial contracts where benefits or annuities are paid annually, actuaries define the **curtate future lifetime** $K_x$ as the greatest integer less than or equal to $T_x$:

$$K_x = \lfloor T_x \rfloor$$

$K_x$ represents the number of complete future years lived by $(x)$ prior to death. It is a discrete random variable taking non-negative integer values $k \in \{0, 1, 2, \dots\}$.

The probability mass function of $K_x$ is:

$$P(K_x = k) = P(k \le T_x < k + 1) = {}_k p_x - {}_{k+1} p_x = {}_k p_x \cdot q_{x+k} = {}_k| q_x$$

### Complete Expectation of Life ($\mathring{e}_x$)
The **complete expectation of life** $\mathring{e}_x$ is the expected total future lifetime of $(x)$:

$$\mathring{e}_x = \mathbb{E}[T_x] = \int_0^\infty t f_x(t)\,dt = \int_0^\infty t ({}_t p_x \mu_{x+t})\,dt$$

Applying integration by parts with $u = t$ and $dv = -d({}_t p_x)$:
$$\mathring{e}_x = \left[ -t {}_t p_x \right]_0^\infty + \int_0^\infty {}_t p_x\,dt$$
Assuming $\lim_{t \to \infty} t {}_t p_x = 0$:

$$\mathring{e}_x = \int_0^\infty {}_t p_x\,dt$$

The complete life expectancy equals the total area under the survival curve from age $x$ onward!

### Curtate Expectation of Life ($e_x$)
The **curtate expectation of life** $e_x$ is the expected number of completed future years lived:

$$e_x = \mathbb{E}[K_x] = \sum_{k=0}^\infty k \cdot P(K_x = k) = \sum_{k=0}^\infty k ({}_k p_x - {}_{k+1} p_x)$$

Expanding the telescoping series:
$$e_x = 0(1 - p_x) + 1(p_x - {}_2 p_x) + 2({}_2 p_x - {}_3 p_x) + 3({}_3 p_x - {}_4 p_x) + \dots$$
$$e_x = \sum_{k=1}^\infty {}_k p_x$$

### Relationship Between $\mathring{e}_x$ and $e_x$
Assuming deaths distribute uniformly over each single year of age ($T_x \approx K_x + 0.5$):

$$\mathring{e}_x \approx e_x + \frac{1}{2}$$

## 3.4 Classical Parametric Laws of Mortality

Throughout demographic history, mathematicians formulated parametric laws to model human senescence:

### 1. Abraham de Moivre's Law (1725)
De Moivre postulated that human mortality operates under a uniform distribution of deaths up to a limiting terminal age $\omega$ (typically $\omega = 100$ or $105$):

$$S_0(x) = 1 - \frac{x}{\omega}, \qquad 0 \le x \le \omega$$

$${}_t p_x = \frac{\omega - (x + t)}{\omega - x} = 1 - \frac{t}{\omega - x}$$

The force of mortality is:
$$\mu_{x+t} = -\frac{d}{dt} \ln\left(1 - \frac{t}{\omega - x}\right) = \frac{1}{\omega - (x + t)}$$
The force of mortality increases hyperbolically, approaching infinity as age approaches $\omega$. The complete expectation of life is:
$$\mathring{e}_x = \frac{\omega - x}{2}$$

### 2. Benjamin Gompertz's Law (1825)
Benjamin Gompertz observed that after sexual maturity, human mortality increases in a geometric progression—a mathematical law of physiological senescence:

$$\mu_x = B \cdot c^x, \qquad B > 0, \; c > 1$$

where $B$ is a baseline biological vulnerability parameter, and $c$ is the annual mortality acceleration factor (empirically $c \approx 1.08$ to $1.10$, meaning the hazard of death doubles approximately every $7$ to $9$ years of adult life).

The survival probability is:
$${}_t p_x = \exp\left( -\int_0^t B c^{x+s}\,ds \right) = \exp\left( -B c^x \int_0^t c^s\,ds \right) = \exp\left( -\frac{B c^x}{\ln c} (c^t - 1) \right)$$
Letting $g = \exp(-B / \ln c)$:
$${}_t p_x = g^{c^x (c^t - 1)}$$

### 3. William Makeham's Law (1860)
William Makeham refined Gompertz's law by recognizing that total mortality consists of two distinct components: an age-independent background hazard (accidents, homicides, infectious epidemics) plus age-dependent physiological senescence:

$$\mu_x = A + B \cdot c^x, \qquad A \ge -B, \; B > 0, \; c > 1$$

The survival probability is:

$${}_t p_x = \exp\left( -\int_0^t (A + B c^{x+s})\,ds \right) = \exp(-A t) \cdot \exp\left( -\frac{B c^x}{\ln c} (c^t - 1) \right) = s^t \cdot g^{c^x (c^t - 1)}$$

where $s = e^{-A}$ and $g = \exp(-B / \ln c)$. Makeham’s law provided the mathematical engine for commercial life insurance actuarial tables worldwide for over a century.

### 4. The Weibull Mortality Law
Waloddi Weibull modeled aging as power-law wear-out:
$$\mu_x = k \cdot x^n, \qquad k > 0, \; n > 0$$
$${}_t p_x = \exp\left( -\frac{k}{n + 1} \left[ (x + t)^{n+1} - x^{n+1} \right] \right)$$

## 3.5 Life Table Structure and Construction

An actuarial **life table** translates continuous survival distributions into discrete tabular columns representing a hypothetical closed cohort of $\ell_0$ newborn infants (the **radix**, conventionally $\ell_0 = 100,000$ or $1,000,000$) followed over time until all members have died.

### Standard Life Table Columns
1. **$x$**: Exact attained age ($x = 0, 1, 2, \dots, \omega$).
2. **$\ell_x$**: The number of survivors reaching exact age $x$ out of the initial radix $\ell_0$:
   $$\ell_x = \ell_0 \cdot {}_x p_0 = \ell_0 \cdot S_0(x)$$
3. **$d_x$**: The number of deaths occurring between exact age $x$ and $x + 1$:
   $$d_x = \ell_x - \ell_{x+1}$$
4. **$q_x$**: The mortality rate (probability of dying within one year given survival to age $x$):
   $$q_x = \frac{d_x}{\ell_x} = 1 - \frac{\ell_{x+1}}{\ell_x}$$
5. **$p_x$**: The survival rate:
   $$p_x = \frac{\ell_{x+1}}{\ell_x} = 1 - q_x$$
6. **$L_x$**: The total person-years lived by the cohort between age $x$ and $x + 1$:
   $$L_x = \int_0^1 \ell_{x+t}\,dt$$
7. **$T_x$**: The total person-years lived by the cohort from age $x$ until terminal extinction $\omega$:
   $$T_x = \int_0^\infty \ell_{x+t}\,dt = \sum_{y=x}^{\omega - 1} L_y$$
8. **$\mathring{e}_x$**: Complete life expectancy:
   $$\mathring{e}_x = \frac{T_x}{\ell_x}$$
9. **$m_x$**: The central death rate:
   $$m_x = \frac{d_x}{L_x}$$

General multi-year probabilities are retrieved directly from the $\ell_x$ column:

$${}_t p_x = \frac{\ell_{x+t}}{\ell_x}, \qquad {}_t q_x = \frac{\ell_x - \ell_{x+t}}{\ell_x} = \frac{{}_t d_x}{\ell_x}, \qquad {}_{u|t} q_x = \frac{\ell_{x+u} - \ell_{x+u+t}}{\ell_x}$$

## 3.6 Fractional Age Assumptions (Inter-Age Interpolation)

Life tables tabulate values exclusively at integer ages $x = 0, 1, 2, \dots$. When an actuarial calculation requires probabilities at fractional ages (such as calculating the probability that a life aged $45.25$ survives to $45.75$), actuaries apply one of three standardized mathematical interpolation assumptions for $0 \le t \le 1$:

### 1. Uniform Distribution of Deaths (UDD)
Assumes that deaths occurring between age $x$ and $x + 1$ distribute uniformly across the calendar year. This is equivalent to linear interpolation of the survival function $\ell_{x+t}$:

$$\ell_{x+t} = (1 - t) \ell_x + t \ell_{x+1} = \ell_x - t \cdot d_x$$

Dividing by $\ell_x$:

$${}_t p_x = 1 - t \cdot q_x \implies {}_t q_x = t \cdot q_x$$

The force of mortality under UDD is:

$$\mu_{x+t} = \frac{q_x}{1 - t \cdot q_x}$$

Under UDD, the average person-years lived is:
$$L_x = \int_0^1 (\ell_x - t d_x)\,dt = \ell_x - \frac{1}{2} d_x = \frac{\ell_x + \ell_{x+1}}{2}$$
UDD is the most widely applied interpolation convention in life contingencies.

### 2. Constant Force of Mortality (CFM)
Assumes that the force of mortality remains strictly constant throughout the single year of age: $\mu_{x+t} = \mu$ for $0 \le t < 1$.

Since $p_x = \exp(-\mu) \implies \mu = -\ln p_x$:

$${}_t p_x = \exp(-\mu t) = (p_x)^t = (1 - q_x)^t$$

$$\mu_{x+t} = -\ln p_x = \text{constant}$$

### 3. The Balducci (Hyperbolic) Assumption
Assumes that the reciprocal of the survival curve is linear:
$$\frac{1}{\ell_{x+t}} = \frac{1 - t}{\ell_x} + \frac{t}{\ell_{x+1}}$$
which implies:
$${}_{1 - t} q_{x+t} = (1 - t) q_x$$
While mathematically convenient in the pre-computer era, Balducci implies a decreasing force of mortality within each year of age, making it biologically unrealistic.

## 3.7 Select and Ultimate Life Tables

When an individual applies for life insurance, they must undergo medical underwriting (physical examinations, blood panels, medical history review). Individuals approved for standard insurance coverage exhibit substantially lower mortality in early policy years than individuals of the identical age in the general population. Over time, this initial medical selection effect gradually wears off.

To capture this duration-dependent phenomenon, actuaries construct **Select and Ultimate Life Tables**:
- $[x]$: Age at initial policy underwriting selection.
- $t$: Duration (years elapsed since selection).
- $[x] + t$: Current attained age.

A select table tabulates mortality as a two-dimensional function $q_{[x]+t}$ for durations $t = 0, 1, \dots, r - 1$, where $r$ is the **select period** (typically $r = 2, 3,\text{ or } 5\text{ years}$). After $r$ years, the selection effect has completely dissipated, and mortality depends solely on attained age $x + r$, transitioning into the single-column **Ultimate Life Table**:

$$q_{[x]+t} = q_{x+t} \quad \text{for all } t \ge r$$

For example, with a 3-year select period ($r = 3$):
$$q_{[40]} < q_{[39]+1} < q_{[38]+2} < q_{40}$$
All four groups are currently aged 40, but a person freshly underwritten at age 40 has lower expected mortality than someone underwritten at age 37 three years ago!

## 3.7 Fractional Age Assumptions: Exact Mathematical Derivations

Life tables report survival numbers $l_x$ and mortality probabilities $q_x$ exclusively at integer ages $x \in \{0, 1, 2, \dots, \omega\}$. However, actuarial events such as policy death claims, annuity commencements, and premium surrender adjustments occur continuously at arbitrary fractional ages $x + t$, where $x$ is an integer age and $0 < t < 1$.

To evaluate probabilities involving fractional durations, actuaries invoke one of three standard mathematical assumptions regarding the distribution of deaths within the integer year of age $[x, x + 1)$.

### 1. Uniform Distribution of Deaths (UDD)
The **Uniform Distribution of Deaths** hypothesis assumes that the future lifetime random variable $T_x$ is uniformly distributed over the unit interval $[0, 1)$. Equivalently, the survival function $l_{x+t}$ interpolates linearly between $l_x$ and $l_{x+1}$:

$$l_{x+t} = (1 - t) l_x + t l_{x+1} = l_x - t \cdot d_x \quad \text{for } 0 \le t \le 1$$

From this linear specification, the fractional death probability is directly proportional to duration $t$:
$${}_t q_x = \frac{l_x - l_{x+t}}{l_x} = \frac{t \cdot d_x}{l_x} = t \cdot q_x$$

For any sub-interval $[t, t + s]$ such that $0 \le t < t + s \le 1$, the conditional probability of survival is:
$${}_s p_{x+t} = \frac{l_{x+t+s}}{l_{x+t}} = \frac{l_x - (t + s) d_x}{l_x - t \cdot d_x} = \frac{1 - (t + s) q_x}{1 - t \cdot q_x} = 1 - \frac{s \cdot q_x}{1 - t \cdot q_x}$$

The instantaneous force of mortality under UDD is:
$$\mu_{x+t} = -\frac{1}{l_{x+t}} \frac{d}{dt} l_{x+t} = -\frac{1}{l_x - t \cdot d_x} (-d_x) = \frac{d_x}{l_x - t \cdot d_x} = \frac{q_x}{1 - t \cdot q_x}$$
Under UDD, $\mu_{x+t}$ is a strictly increasing function of $t \in [0, 1)$, accelerating toward the end of the year of age.

### 2. Constant Force of Mortality (CFM)
The **Constant Force of Mortality** assumption posits that the hazard rate remains strictly invariant throughout the integer age interval:
$$\mu_{x+t} = \mu \quad \text{for all } t \in [0, 1)$$

Since $p_x = \exp\left( -\int_0^1 \mu_{x+u}\,du \right) = e^{-\mu}$, we immediately obtain:
$$\mu = -\ln(p_x)$$
The fractional survival probability is:
$${}_t p_x = e^{-\mu t} = (e^{-\mu})^t = (p_x)^t$$
The fractional mortality probability is:
$${}_t q_x = 1 - (p_x)^t = 1 - (1 - q_x)^t$$
For any sub-interval, conditional survival depends only on elapsed duration $s$, exhibiting the memoryless property within the year:
$${}_s p_{x+t} = (p_x)^s$$
The constant force assumption provides exceptional computational convenience in continuous-time Markov multi-state modeling.

### 3. The Balducci Assumption (Hyperbolic Survival)
Historically formulated by Gaetano Balducci, this hypothesis assumes that the reciprocal of the survival function is linear in $t$:
$$\frac{1}{l_{x+t}} = \frac{1 - t}{l_x} + \frac{t}{l_{x+1}} \quad \text{for } 0 \le t \le 1$$
This yields the foundational operational identity:
$${}_{1 - t} q_{x+t} = (1 - t) q_x$$
The instantaneous force of mortality under the Balducci assumption is:
$$\mu_{x+t} = \frac{q_x}{1 - (1 - t) q_x}$$
Under Balducci, $\mu_{x+t}$ is a decreasing function of $t$, which is biologically counterintuitive for adult human populations but provided substantial algebraic simplifications in manual actuarial calculations prior to digital computing.

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Metric / Property</th>
<th>Uniform Distribution of Deaths (UDD)</th>
<th>Constant Force of Mortality (CFM)</th>
<th>Balducci Assumption</th>
</tr>
</thead>
<tbody>
<tr>
<td>Survival Curve $l_{x+t}$</td>
<td>Linear: $l_x - t \cdot d_x$</td>
<td>Exponential: $l_x (p_x)^t$</td>
<td>Hyperbolic: $[(1-t)/l_x + t/l_{x+1}]^{-1}$</td>
</tr>
<tr>
<td>Fractional Mortality ${}_t q_x$</td>
<td>$t \cdot q_x$</td>
<td>$1 - (p_x)^t$</td>
<td>$\frac{t \cdot q_x}{1 - (1-t)q_x}$</td>
</tr>
<tr>
<td>Force of Mortality $\mu_{x+t}$</td>
<td>$\frac{q_x}{1 - t \cdot q_x}$ (increasing)</td>
<td>$-\ln(p_x)$ (constant)</td>
<td>$\frac{q_x}{1 - (1-t)q_x}$ (decreasing)</td>
</tr>
<tr>
<td>Primary Application</td>
<td>Statutory life insurance reserving</td>
<td>Multi-state stochastic continuous models</td>
<td>Historical life table graduation</td>
</tr>
</tbody>
</table>
</div>

## 3.8 Stochastic Mortality Modeling: The Lee-Carter Framework

Classical life table construction assumes that age-specific mortality rates are static in time. However, the twentieth and twenty-first centuries have witnessed continuous secular declines in mortality rates across nearly all human populations—a phenomenon termed **longevity improvement**.

Annuity providers, pension sponsors, and social security programs face substantial **longevity risk**: the systematic financial risk that retirees survive significantly longer than anticipated by static baseline life tables. To quantify longevity risk, actuaries deploy stochastic mortality models.

### The Lee-Carter Formulation
In 1992, Ronald Lee and Lawrence Carter formulated the foundational stochastic model for forecasting age-specific central death rates $m_{x, t}$ at age $x$ in calendar year $t$:

$$\ln(m_{x, t}) = \alpha_x + \beta_x \kappa_t + \epsilon_{x, t}$$

where:
- $\alpha_x$: The baseline age-specific log-mortality profile, representing the long-term empirical average of $\ln(m_{x, t})$ across all observed years.
- $\kappa_t$: The time-varying latent mortality index, capturing overall macroeconomic and public health improvements over calendar years.
- $\beta_x$: The age-specific sensitivity coefficient, measuring the relative speed of mortality decline at age $x$ in response to unit changes in $\kappa_t$.
- $\epsilon_{x, t} \sim \mathcal{N}(0, \sigma_\epsilon^2)$: A Gaussian error disturbance reflecting idiosyncratic demographic fluctuations.

### Identification Constraints and Model Estimation
To ensure unique mathematical identification of the parameters, two normalization constraints are imposed:
$$\sum_{t=1}^T \kappa_t = 0 \quad \text{and} \quad \sum_{x=x_{\min}}^{x_{\max}} \beta_x = 1$$

Under these constraints:
$$\alpha_x = \frac{1}{T} \sum_{t=1}^T \ln(m_{x, t})$$
The parameters $\beta_x$ and $\kappa_t$ are obtained via **Singular Value Decomposition (SVD)** of the mean-centered log-mortality matrix $Z_{x, t} = \ln(m_{x, t}) - \alpha_x$:
$$Z = U \Sigma V^T$$
The first principal component yields $\beta_x$ from the first left singular vector $u_1$ and $\kappa_t$ from the first right singular vector $v_1$ scaled by singular value $\sigma_1$.

### Forecasting and Random Walk with Drift
Once $\kappa_t$ is estimated historically, it is modeled as an autoregressive integrated moving average process, specifically a **Random Walk with Drift**:
$$\kappa_t = \kappa_{t-1} + d + e_t, \quad e_t \sim \mathcal{N}(0, \sigma_e^2)$$
where $d = \frac{\kappa_T - \kappa_1}{T - 1} < 0$ is the empirical downward drift.

Extrapolating $\kappa_{t+h} = \kappa_t + h \cdot d$ into the future enables probabilistic forecasting of life expectancy, prospective annuity liability valuations, and stress-testing of defined benefit pension solvency under Solvency II.

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

## 3.11 Analytical Expectation of Life: Euler-Maclaurin Expansion

A central theoretical distinction in demographic and actuarial science lies between:
1. **The Complete Expectation of Life ($e_x^\circ$)**: The expected total future lifetime from age $x$ in continuous time:
   $$e_x^\circ = \mathbb{E}[T_x] = \int_0^\infty {}_t p_x\,dt$$
2. **The Curtate Expectation of Life ($e_x$)**: The expected number of complete future years lived:
   $$e_x = \mathbb{E}[K_x] = \sum_{k=1}^\infty {}_k p_x$$

### 1. Derivation via the Euler-Maclaurin Summation Formula
To derive the exact relationship between the continuous integral and discrete summation, we deploy the **Euler-Maclaurin Summation Formula**.

For a smooth function $f(t)$ defined on $[0, \infty)$ with $\lim_{t \to \infty} f(t) = 0$:
$$\int_0^\infty f(t)\,dt = \sum_{k=1}^\infty f(k) + \frac{1}{2} f(0) - \frac{1}{12} f'(0) + \frac{1}{720} f'''(0) - \dots$$

Setting $f(t) = {}_t p_x$:
- At $t = 0$: $f(0) = {}_0 p_x = 1$.
- First derivative: $f'(t) = \frac{d}{dt} {}_t p_x = -{}_t p_x \mu_{x+t}$. At $t = 0$:
  $$f'(0) = -{}_0 p_x \mu_{x} = -\mu_x$$
- Substituting into the Euler-Maclaurin expansion:

$$e_x^\circ = e_x + \frac{1}{2} (1) - \frac{1}{12} (-\mu_x) + \mathcal{O}(f'''(0))$$

$$e_x^\circ \approx e_x + \frac{1}{2} + \frac{1}{12} \mu_x$$

### 2. Demographic and Practical Interpretation
The primary term $\frac{1}{2}$ reflects the standard assumption that deaths are distributed uniformly across each integer year of age, meaning that deceased individuals survive on average half a year ($0.5$) in their final year of life:
$$e_x^\circ \approx e_x + 0.5$$

The secondary correction term $+\frac{1}{12} \mu_x$ accounts for the curvature of the survival curve. At advanced ages ($x > 80$), where the force of mortality $\mu_x$ becomes substantial ($\mu_{85} \approx 0.10 - 0.15$), the correction term adds a measurable increment of $0.01$ to $0.015$ years.

### 3. Woolhouse's Formula for Fractional Curtate Expectations
If life expectancy is evaluated in discrete intervals of length $1/m$ (e.g., monthly intervals where $m = 12$):
$$e_x^{(m)} = \frac{1}{m} \sum_{k=1}^\infty {}_{k/m} p_x \approx e_x^\circ - \frac{1}{2m} - \frac{1}{12m^2} \mu_x$$
Substituting $e_x^\circ \approx e_x + \frac{1}{2}$:
$$e_x^{(m)} \approx e_x + \frac{m - 1}{2m}$$
For monthly evaluation ($m = 12$):
$$e_x^{(12)} \approx e_x + \frac{11}{24} \approx e_x + 0.4583$$
This relationship enables life annuity administrators to reconcile monthly pension benefit obligations with annual life table data.

## 3.12 Maximum Likelihood Estimation of Parametric Mortality Laws

To calibrate parametric mortality models (such as Gompertz $\mu_x = B c^x$ or Makeham $\mu_x = A + B c^x$) to insured lives, actuaries maximize the likelihood function of observed individual life histories.

### Mathematical Formulation of Likelihood for Censored Lifetime Data
Consider an actuarial study of $n$ insured individuals observed over an observation window. For individual $i \in \{1, 2, \dots, n\}$:
- The individual enters observation at age $x_i$.
- The individual exits observation at age $x_i + t_i$.
- Let $\delta_i \in \{0, 1\}$ be the censoring indicator: $\delta_i = 1$ if the individual died at age $x_i + t_i$, and $\delta_i = 0$ if the individual survived to the study end date or withdrew alive (right-censored).

The likelihood contribution of individual $i$ is:
$$L_i = \left( {}_{t_i} p_{x_i} \cdot \mu_{x_i + t_i} \right)^{\delta_i} \cdot \left( {}_{t_i} p_{x_i} \right)^{1 - \delta_i} = {}_{t_i} p_{x_i} \cdot [\mu_{x_i + t_i}]^{\delta_i}$$

Since ${}_{t_i} p_{x_i} = \exp\left( -\int_0^{t_i} \mu_{x_i + s}\,ds \right)$, the total log-likelihood for the cohort is:

$$\ln L = \sum_{i=1}^n \left[ \delta_i \ln \mu(x_i + t_i) - \int_0^{t_i} \mu(x_i + s)\,ds \right]$$

### Maximum Likelihood Estimation for the Gompertz Law
Under the Gompertz law, $\mu(x) = B c^x = e^{\alpha + \beta x}$ where $\alpha = \ln B$ and $\beta = \ln c > 0$.
The cumulative hazard integral is:
$$\int_0^{t_i} e^{\alpha + \beta (x_i + s)}\,ds = \frac{e^{\alpha + \beta x_i}}{\beta} (e^{\beta t_i} - 1)$$

The log-likelihood simplifies to:
$$\ln L(\alpha, \beta) = \sum_{i=1}^n \left[ \delta_i (\alpha + \beta (x_i + t_i)) - \frac{e^{\alpha + \beta x_i}}{\beta} (e^{\beta t_i} - 1) \right]$$

The score equations are obtained by taking partial derivatives:
$$\frac{\partial \ln L}{\partial \alpha} = \sum_{i=1}^n \left[ \delta_i - \frac{e^{\alpha + \beta x_i}}{\beta} (e^{\beta t_i} - 1) \right] = 0$$
$$\frac{\partial \ln L}{\partial \beta} = \sum_{i=1}^n \left[ \delta_i (x_i + t_i) - \frac{e^{\alpha + \beta x_i}}{\beta} \left( t_i e^{\beta t_i} - \frac{e^{\beta t_i} - 1}{\beta} \right) \right] = 0$$

Solving these non-linear equations via Newton-Raphson iteration yields the maximum likelihood estimates $(\hat{\alpha}, \hat{\beta})$. Inverting the observed Fisher Information Matrix provides the asymptotic variance-covariance matrix:
$$\mathbf{\Sigma} = \begin{pmatrix} -\frac{\partial^2 \ln L}{\partial \alpha^2} & -\frac{\partial^2 \ln L}{\partial \alpha \partial \beta} \\ -\frac{\partial^2 \ln L}{\partial \alpha \partial \beta} & -\frac{\partial^2 \ln L}{\partial \beta^2} \end{pmatrix}^{-1}$$
enabling the actuary to construct Wald confidence intervals for projected mortality rates.

## 3.13 Select and Ultimate Mortality in Life Insurance Underwriting

When an applicant applies for individual life insurance, the insurer conducts rigorous medical and financial underwriting, including blood tests, cardiovascular examinations, family medical history reviews, and lifestyle questionnaires.

Applicants with severe pre-existing chronic conditions are declined or rated with substandard extra mortality, while applicants issued standard policies are confirmed to be in superior physical health.

### 1. The Selection Effect and Select Duration
Because unhealthy lives are screened out, newly insured individuals experience mortality rates far below those of the general population of the same age. This mortality reduction is known as the **Selection Effect**.

Over elapsed calendar time $t$, this initial health screening advantage gradually dissipates:
- Insured individuals develop new illnesses, encounter accidents, and experience biological aging.
- After a duration of $r$ years (the **Select Period**, typically $r = 5$ to $25$ years depending on underwriting rigor), the mortality rate of the insured cohort approaches the mortality rate of the general insured pool of the same attained age.

### 2. Mathematical Notation of Select and Ultimate Life Tables
Actuaries denote select mortality using brackets:
- $[x]$: The age at which the life was underwritten and selected.
- $[x] + t$: The attained age of the life after $t$ elapsed years since underwriting ($t \ge 0$).
- $q_{[x] + t}$: The mortality rate at attained age $x + t$ for a life selected at age $x$.
- $q_{x + t}$: The **Ultimate Mortality Rate** at attained age $x + t$, applying to lives selected at least $r$ years earlier ($t \ge r$).

For any select duration $t < r$:
$$q_{[x] + t} < q_{[x - 1] + t + 1} < \dots < q_{x + t}$$

For duration $t \ge r$, the brackets are removed:
$$q_{[x] + t} = q_{x + t}$$

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Issue Age $[x]$</th>
<th>$q_{[x]}$ (Duration 0)</th>
<th>$q_{[x]+1}$ (Duration 1)</th>
<th>$q_{[x]+2}$ (Duration 2)</th>
<th>$q_{x+3}$ (Ultimate Rate)</th>
<th>Attained Age $x+3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$[50]$</td>
<td>0.00142</td>
<td>0.00215</td>
<td>0.00298</td>
<td>0.00392</td>
<td>53</td>
</tr>
<tr>
<td>$[51]$</td>
<td>0.00158</td>
<td>0.00238</td>
<td>0.00331</td>
<td>0.00435</td>
<td>54</td>
</tr>
<tr>
<td>$[52]$</td>
<td>0.00176</td>
<td>0.00264</td>
<td>0.00368</td>
<td>0.00482</td>
<td>55</td>
</tr>
</tbody>
</table>
</div>

Ignoring the select period and pricing life insurance policies using ultimate mortality rates would lead to severe uncompetitive overpricing, while underestimating reserves in early policy durations.

## 3.14 The Lexis Diagram and Period vs Cohort Observation

In demographic surveillance and actuarial survival analysis, vital events (births, deaths, migrations) occur across two simultaneous continuous dimensions: chronological calendar time $t$ and attained individual age $x$. To represent demographic data visually and track population cohorts without ambiguity, actuaries employ the **Lexis Diagram** (devised by Wilhelm Lexis in 1875).

### 1. Geometric Structure of the Lexis Diagram
A Lexis diagram plots calendar time $t$ on the horizontal axis and age $x$ on the vertical axis:
- **Lifelines**: Every individual life is represented as a straight line starting at the point of birth $(t_{\text{birth}}, 0)$ and advancing upward and to the right at a fixed $45^\circ$ angle ($dx/dt = 1$).
- **Points of Death**: An individual death is plotted as a point $(t_{\text{death}}, x_{\text{death}})$ terminating that life line.
- **Cohorts**: All individuals born during a given calendar year $[t_0, t_0 + 1)$ form a **Birth Cohort**, bounded by the diagonal strip extending from the base interval at age zero.

### 2. Period vs Cohort Perspectives and Geometric Elementary Sets
Demographers partition the Lexis plane into elementary geometric regions:
1. **Vertical Rectangles / Squares**: Represents a **Period-Age Observation** $[t, t+1) \times [x, x+1)$. All deaths occurring within calendar year $t$ to individuals between exact ages $x$ and $x+1$, regardless of birth year. This forms the standard basis for national census vital statistics.
2. **Horizontal Strips**: Represents life table experiences over age interval $[x, x+1)$ across all historical time.
3. **Parallelograms along the $45^\circ$ Diagonal**: Represents a **Cohort-Age Observation**, capturing all deaths occurring to a specific birth cohort as it advances through age interval $[x, x+1)$.
4. **Triangles**: A period-age square $[t, t+1) \times [x, x+1)$ is divided into two triangles by the $45^\circ$ diagonal lifeline:
   - The *Lower Triangle*: Deaths to individuals born in calendar year $t - x - 1$.
   - The *Upper Triangle*: Deaths to individuals born in calendar year $t - x$.

Distinguishing between these triangles allows actuaries to convert raw period vital registration records into pure cohort survival probabilities ${}_t p_x$ free from observational truncation bias.

## Fully worked question 1: Evaluating Survival Probabilities and Expectations Under Makeham's Law

### Question
An actuarial mortality study models adult mortality in an industrial workforce using Makeham’s Law:
$$\mu_x = A + B \cdot c^x$$
The fitted parametric constants are:
- $A = 0.00100$
- $B = 0.00005$
- $c = 1.10000$ (so $\ln c = \ln(1.10) \approx 0.095310$)

Perform the following calculations:
1. Compute the exact force of mortality at age $x = 40$ ($\mu_{40}$) and age $x = 70$ ($\mu_{70}$).
2. Compute the exact probability that a life aged $40$ survives to age $60$ (${}_{20} p_{40}$).
3. Compute the deferred mortality probability that a life aged $40$ survives to age $60$ and subsequently dies before reaching age $65$ (${}_{20|5} q_{40}$).
4. Calculate the doubling time of the senescent component of the force of mortality.

### Solution, step 1: Evaluate force of mortality $\mu_x$
Given $A = 0.00100$, $B = 0.00005$, and $c = 1.10$:
1. **At age $x = 40$**:
   $$c^{40} = (1.10)^{40} \approx 45.25926$$
   $$\mu_{40} = 0.00100 + (0.00005 \times 45.25926) = 0.00100 + 0.002263 = 0.003263$$
   The instantaneous hazard of death at age 40 is $0.3263\%$ per year. Notice that the background hazard ($0.00100$) accounts for $30.6\%$ of total mortality at age 40.

2. **At age $x = 70$**:
   $$c^{70} = (1.10)^{70} = (1.10)^{40} \times (1.10)^{30} \approx 45.25926 \times 17.44940 \approx 789.747$$
   $$\mu_{70} = 0.00100 + (0.00005 \times 789.747) = 0.00100 + 0.039487 = 0.040487$$
   The hazard of death at age 70 is $4.0487\%$ per year—over $12\times$ higher than at age 40!

### Solution, step 2: Compute survival probability ${}_{20} p_{40}$
Under Makeham’s Law:
$${}_{20} p_{40} = \exp\left( -20 A - \frac{B c^{40}}{\ln c} (c^{20} - 1) \right)$$
Evaluate each component:
- Background component:
  $$-20 A = -20 \times 0.00100 = -0.020000$$
- Senescent component:
  $$c^{20} = (1.10)^{20} \approx 6.727500 \implies c^{20} - 1 = 5.727500$$
  $$\frac{B c^{40}}{\ln c} = \frac{0.00005 \times 45.25926}{0.095310} = \frac{0.00226296}{0.095310} \approx 0.023743$$
  $$\text{Senescent Term} = 0.023743 \times 5.727500 \approx 0.135988$$
- Total integrated hazard:
  $$\int_0^{20} \mu_{40+s}\,ds = 0.020000 + 0.135988 = 0.155988$$
$${}_{20} p_{40} = \exp(-0.155988) \approx 0.855570 = 85.56\%$$
A 40-year-old worker has an $85.56\%$ probability of surviving to age 60.

### Solution, step 3: Compute deferred mortality probability ${}_{20|5} q_{40}$
$${}_{20|5} q_{40} = {}_{20} p_{40} - {}_{25} p_{40} = {}_{20} p_{40} (1 - {}_5 p_{60})$$
First compute ${}_5 p_{60}$:
$${}_5 p_{60} = \exp\left( -5 A - \frac{B c^{60}}{\ln c} (c^5 - 1) \right)$$
- $c^{60} = c^{40} \times c^{20} = 45.25926 \times 6.727500 \approx 304.4816$
- $c^5 = (1.10)^5 = 1.61051 \implies c^5 - 1 = 0.61051$
- $-5 A = -5 \times 0.00100 = -0.005000$
- Senescent term:
  $$\frac{0.00005 \times 304.4816}{0.095310} \times 0.61051 = \frac{0.015224}{0.095310} \times 0.61051 = 0.159732 \times 0.61051 \approx 0.097518$$
- Total integrated hazard: $0.005000 + 0.097518 = 0.102518$.
$${}_5 p_{60} = \exp(-0.102518) \approx 0.902562$$
$${}_5 q_{60} = 1 - 0.902562 = 0.097438$$

Now compute deferred probability:
$${}_{20|5} q_{40} = {}_{20} p_{40} \times {}_5 q_{60} = 0.855570 \times 0.097438 \approx 0.083365 = 8.34\%$$
There is an $8.34\%$ chance that a 40-year-old will survive to age 60 and die between age 60 and 65.

### Solution, step 4: Doubling time of the senescent mortality rate
The senescent component is $\mu_{\text{sen}}(x) = B c^x$.
Let $T_{\text{double}}$ denote the time required for $\mu_{\text{sen}}$ to double:
$$B c^{x + T_{\text{double}}} = 2 B c^x \implies c^{T_{\text{double}}} = 2$$
$$T_{\text{double}} \ln c = \ln 2 \implies T_{\text{double}} = \frac{\ln 2}{\ln(1.10)} = \frac{0.693147}{0.095310} \approx 7.27\text{ years}$$
Senescent mortality doubles every **$7.27\text{ years}$**.

## Fully worked question 2: Fractional Age Interpolation Under UDD and Constant Force Assumptions

### Question
An extract from an official actuarial life table reports the following cohort survivor counts:
- $\ell_{50} = 90,000$
- $\ell_{51} = 88,200$
- $\ell_{52} = 86,100$

Perform the following calculations:
1. Compute the one-year mortality rates $q_{50}$ and $q_{51}$.
2. Under the **Uniform Distribution of Deaths (UDD)** assumption:
   - Compute the survival probability ${}_{0.6} p_{50}$.
   - Compute the fractional probability that a life aged $50.4$ survives to age $51.8$ (${}_{1.4} p_{50.4}$).
   - Compute the instantaneous force of mortality at exact age $50.5$ ($\mu_{50.5}$).
3. Under the **Constant Force of Mortality (CFM)** assumption:
   - Compute the constant force of mortality $\mu$ over the interval $[50, 51)$.
   - Compute ${}_{1.4} p_{50.4}$ under CFM and compare with the UDD result.

### Solution, step 1: Compute $q_{50}$ and $q_{51}$
$$d_{50} = \ell_{50} - \ell_{51} = 90,000 - 88,200 = 1,800$$
$$q_{50} = \frac{d_{50}}{\ell_{50}} = \frac{1,800}{90,000} = 0.02000 \implies p_{50} = 0.98000$$
$$d_{51} = \ell_{51} - \ell_{52} = 88,200 - 86,100 = 2,100$$
$$q_{51} = \frac{d_{51}}{\ell_{51}} = \frac{2,100}{88,200} \approx 0.02381 \implies p_{51} \approx 0.97619$$

### Solution, step 2: Calculations under UDD
1. **${}_{0.6} p_{50}$**:
   Under UDD, ${}_t q_x = t \cdot q_x$:
   $${}_{0.6} q_{50} = 0.6 \times q_{50} = 0.6 \times 0.02000 = 0.01200$$
   $${}_{0.6} p_{50} = 1 - 0.01200 = 0.98800$$

2. **${}_{1.4} p_{50.4}$**:
   Decompose the path from age $50.4$ to $51.8$ into two segments:
   $${}_{1.4} p_{50.4} = {}_{0.6} p_{50.4} \cdot {}_{0.8} p_{51}$$
   - For the first segment (surviving from $50.4$ to $51.0$):
     $${}_{0.6} p_{50.4} = \frac{{}_1 p_{50}}{{}_{0.4} p_{50}} = \frac{1 - q_{50}}{1 - 0.4 q_{50}} = \frac{1 - 0.02000}{1 - (0.4 \times 0.02000)} = \frac{0.98000}{1 - 0.00800} = \frac{0.98000}{0.99200} \approx 0.987903$$
   - For the second segment (surviving from $51.0$ to $51.8$):
     $${}_{0.8} p_{51} = 1 - 0.8 q_{51} = 1 - (0.8 \times 0.023810) = 1 - 0.019048 = 0.980952$$
   - Multiply the two segments:
     $${}_{1.4} p_{50.4} = 0.987903 \times 0.980952 \approx 0.969085$$

3. **Force of mortality $\mu_{50.5}$ under UDD**:
   $$\mu_{50.5} = \frac{q_{50}}{1 - 0.5 q_{50}} = \frac{0.02000}{1 - (0.5 \times 0.02000)} = \frac{0.02000}{1 - 0.01000} = \frac{0.02000}{0.99000} \approx 0.020202$$

### Solution, step 3: Calculations under Constant Force of Mortality (CFM)
1. **Constant force $\mu$ on $[50, 51)$**:
   $$\mu = -\ln p_{50} = -\ln(0.98000) \approx 0.020203$$
   Notice that $\mu_{50.5}^{\text{UDD}} (0.020202) \approx \mu^{\text{CFM}} (0.020203)$ at the midpoint!

2. **${}_{1.4} p_{50.4}$ under CFM**:
   - For $[50, 51)$, constant force is $\mu_1 = 0.020203$.
     Duration lived is $1.0 - 0.4 = 0.6$ years:
     $${}_{0.6} p_{50.4} = \exp(-0.6 \mu_1) = \exp(-0.6 \times 0.020203) = \exp(-0.012122) \approx 0.987951$$
   - For $[51, 52)$, constant force is $\mu_2 = -\ln p_{51} = -\ln(0.976190) \approx 0.024098$.
     Duration lived is $0.8$ years:
     $${}_{0.8} p_{51} = \exp(-0.8 \mu_2) = \exp(-0.8 \times 0.024098) = \exp(-0.019278) \approx 0.980905$$
   - Multiply the two segments:
     $${}_{1.4} p_{50.4}^{\text{CFM}} = 0.987951 \times 0.980905 \approx 0.969086$$

**Comparison**:
- UDD Result: $0.969085$
- CFM Result: $0.969086$
The two assumptions agree to within 1 part per million, confirming that for single-year intervals, both interpolation methods are virtually indistinguishable.

## Fully worked question 3: Multi-Year Select and Ultimate Mortality Table Construction

### Question
A life reinsurance company constructs a select-and-ultimate life table with a 2-year select period ($r = 2$). The mortality rates for underwriting select ages $[60]$ and $[61]$ are:
- $q_{[60]} = 0.00800$
- $q_{[60]+1} = 0.01200$
- $q_{[61]} = 0.00900$
- $q_{[61]+1} = 0.01350$
- Ultimate rate at age 62: $q_{62} = 0.01600$
- Ultimate rate at age 63: $q_{63} = 0.01900$

Suppose a cohort of $100,000$ insured lives is underwritten at select age $[60]$ ($\ell_{[60]} = 100,000$).

Perform the following calculations:
1. Compute the expected survivors $\ell_{[60]+1}$, $\ell_{62}$, and $\ell_{63}$.
2. Compute the 3-year survival probability of a life selected at age 60 (${}_3 p_{[60]}$).
3. Compute the 3-year survival probability of a non-selected life aged 60 from the ultimate table if the ultimate rate at age 60 is $q_{60} = 0.01300$ and at age 61 is $q_{61} = 0.01450$.
4. Calculate the percentage mortality reduction gained over the 3-year horizon from medical underwriting selection.

### Solution, step 1: Trace the select cohort $\ell_{[60]+t}$
Starting with $\ell_{[60]} = 100,000$:
1. **At duration $t = 1$ (Attained age 61)**:
   $$d_{[60]} = \ell_{[60]} \times q_{[60]} = 100,000 \times 0.00800 = 800\text{ deaths}$$
   $$\ell_{[60]+1} = 100,000 - 800 = 99,200\text{ survivors}$$

2. **At duration $t = 2$ (Attained age 62 - transitions to Ultimate)**:
   $$d_{[60]+1} = \ell_{[60]+1} \times q_{[60]+1} = 99,200 \times 0.01200 = 1,190.4 \approx 1,190\text{ deaths}$$
   $$\ell_{62} = 99,200 - 1,190.4 = 98,009.6\text{ survivors}$$

3. **At duration $t = 3$ (Attained age 63 - Ultimate rate applies)**:
   $$d_{62} = \ell_{62} \times q_{62} = 98,009.6 \times 0.01600 = 1,568.15\text{ deaths}$$
   $$\ell_{63} = 98,009.6 - 1,568.15 = 96,441.45\text{ survivors}$$

### Solution, step 2: 3-year survival probability for select life (${}_3 p_{[60]}$)
$${}_3 p_{[60]} = \frac{\ell_{63}}{\ell_{[60]}} = \frac{96,441.45}{100,000} \approx 0.964415 = 96.44\%$$
Equivalently, via product of annual survival rates:
$${}_3 p_{[60]} = (1 - q_{[60]})(1 - q_{[60]+1})(1 - q_{62}) = (1 - 0.00800)(1 - 0.01200)(1 - 0.01600)$$
$$= 0.99200 \times 0.98800 \times 0.98400 = 0.980096 \times 0.98400 \approx 0.964414$$

The 3-year mortality probability is:
$${}_3 q_{[60]} = 1 - 0.964414 = 0.035586 = 3.559\%$$

### Solution, step 3: 3-year survival probability for ultimate (unselected) life
For an unselected life aged 60:
$${}_3 p_{60}^{\text{ultimate}} = (1 - q_{60})(1 - q_{61})(1 - q_{62}) = (1 - 0.01300)(1 - 0.01450)(1 - 0.01600)$$
$$= 0.98700 \times 0.98550 \times 0.98400$$
$$0.98700 \times 0.98550 \approx 0.9726885$$
$${}_3 p_{60}^{\text{ultimate}} = 0.9726885 \times 0.98400 \approx 0.957125 = 95.71\%$$

The 3-year unselected mortality probability is:
$${}_3 q_{60}^{\text{ultimate}} = 1 - 0.957125 = 0.042875 = 4.288\%$$

### Solution, step 4: Mortality reduction from underwriting selection
Compare cumulative 3-year death rates:
$$\text{Relative Mortality Reduction} = \frac{{}_3 q_{60}^{\text{ultimate}} - {}_3 q_{[60]}}{{}_3 q_{60}^{\text{ultimate}}} \times 100\% = \frac{0.042875 - 0.035586}{0.042875} \times 100\% = \frac{0.007289}{0.042875} \times 100\% \approx 17.00\%$$
Medical underwriting selection reduces the 3-year mortality rate by **$17.00\%$**, demonstrating why life insurance companies can offer substantial premium discounts to medically underwritten applicants.
