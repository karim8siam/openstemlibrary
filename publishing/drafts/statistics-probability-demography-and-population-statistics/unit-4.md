# Unit 4: Life Tables: Mathematical Construction, Complete & Abridged Models

The life table (actuarial mortality table) is the crown jewel of mathematical demography and actuarial science. First conceptualized by John Graunt in 1662 and formalized mathematically by the astronomer Edmond Halley in 1693, the life table tracks the hypothetical survival and attrition of a synthetic birth cohort (radix $l_0$, conventionally set to $100{,}000$) subjected from birth to extinction to a fixed, unchanging schedule of age-specific mortality rates. By isolating mortality from the confounding effects of initial population size and age structure, the life table provides the ultimate benchmark of longevity: the life expectancy at birth ($e_0$).

## 4.1 Anatomy of the Life Table: The Fundamental Columns and Their Interrelations

A standard demographic life table consists of seven interconnected mathematical columns. In an **abridged life table**, the life course is partitioned into five-year age intervals $[x, x+n)$, with specialized narrow intervals for infancy ($[0, 1)$) and early childhood ($[1, 5)$). In a **complete life table**, the interval width is strictly one single year ($n = 1$) across all ages from $0$ to the terminal open-ended bracket $\omega$.

### The Seven Canonical Life Table Columns
1. **Age Interval $[x, x+n)$**:
   The exact chronological age bracket, where $x$ is the exact attained age and $n$ is the width of the interval.
2. **Mortality Probability ($_n q_x$)**:
   The conditional probability that a person who has survived to exact age $x$ will die before reaching exact age $x+n$:
   $$_n q_x = \mathbb{P}(\text{Death in } [x, x+n) \mid \text{Alive at } x)$$
   The complement is the conditional survival probability:
   $$_n p_x = 1 - {_n q_x} = \mathbb{P}(\text{Survives to } x+n \mid \text{Alive at } x)$$
3. **Number of Cohort Survivors ($l_x$)**:
   The number of individuals from the initial synthetic cohort of size $l_0$ who survive to celebrate exact attained birthday $x$. By definition, $l_0$ is the **radix** (typically $100{,}000$). For subsequent ages:
   $$l_{x+n} = l_x \cdot (1 - {_n q_x}) = l_x \cdot {_n p_x}$$
4. **Number of Cohort Deaths ($_n d_x$)**:
   The number of individuals from the synthetic cohort who die within the age interval $[x, x+n)$:
   $$_n d_x = l_x - l_{x+n} = l_x \cdot {_n q_x}$$
   The sum of all deaths across the entire table equals the initial radix: $\sum_{x=0}^{\omega} {_n d_x} = l_0$.
5. **Person-Years Lived within the Interval ($_n L_x$)**:
   The total person-years lived by the cohort between exact ages $x$ and $x+n$. In continuous calculus:
   $$_n L_x = \int_x^{x+n} l(t) \, dt$$
   In discrete demographic practice, $_n L_x$ is computed using the average fraction of the interval lived by those who die:
   $$_n L_x = n \cdot l_{x+n} + {_n a_x} \cdot {_n d_x}$$
   where $_n a_x$ is the average person-years lived in $[x, x+n)$ by individuals dying within that interval.
6. **Total Person-Years Remaining Above Age $x$ ($T_x$)**:
   The cumulative person-years lived by the cohort from exact age $x$ until all members have died:
   $$T_x = \int_x^{\infty} l(t) \, dt = \sum_{y \ge x} {_n L_y}$$
   Notice that $T_x = T_{x+n} + {_n L_x}$.
7. **Expectation of Life ($e_x$)**:
   The average number of additional years of life remaining for an individual who has survived to exact age $x$:
   $$e_x = \frac{T_x}{l_x}$$
   At birth ($x = 0$), $e_0 = \frac{T_0}{l_0}$ represents the **Life Expectancy at Birth**.

## 4.2 The Conversion of Central Death Rates ($m_x$) to Mortality Probabilities ($q_x$)

A central operational challenge in empirical demography is converting observed **central death rates** ($_n M_x$ or $_n m_x$), which are empirical ratios of deaths to mid-year person-years in an actual living population, into **life table probabilities** ($_n q_x$).

### Mathematical Derivation of the Conversion Formula
Consider the cohort experience in age interval $[x, x+n)$.
By definition, the central death rate in the life table cohort is:

$$_n m_x = \frac{_n d_x}{_n L_x}$$

Recall the expression for $_n L_x$:

$$_n L_x = n \cdot l_{x+n} + {_n a_x} \cdot {_n d_x}$$

Substitute $l_{x+n} = l_x - {_n d_x}$:

$$_n L_x = n (l_x - {_n d_x}) + {_n a_x} \cdot {_n d_x} = n \cdot l_x - (n - {_n a_x}) {_n d_x}$$

Now, substitute this into the central death rate equation:

$$_n m_x = \frac{_n d_x}{n \cdot l_x - (n - {_n a_x}) {_n d_x}}$$

Divide the numerator and denominator by $l_x$, recalling that $\frac{_n d_x}{l_x} = {_n q_x}$:

$$_n m_x = \frac{_n q_x}{n - (n - {_n a_x}) {_n q_x}}$$

To express $_n q_x$ explicitly as a function of $_n m_x$, cross-multiply:

$$_n m_x \left[ n - (n - {_n a_x}) {_n q_x} \right] = {_n q_x}$$

$$n \cdot {_n m_x} - (n - {_n a_x}) {_n m_x} \cdot {_n q_x} = {_n q_x}$$

$$n \cdot {_n m_x} = {_n q_x} \left[ 1 + (n - {_n a_x}) {_n m_x} \right]$$

Dividing through yields the fundamental **Greville–Chiang Conversion Identity**:

$$_n q_x = \frac{n \cdot {_n m_x}}{1 + (n - {_n a_x}) {_n m_x}}$$

### The Linear Assumption (Midpoint Approximation)
For adult ages between age 5 and age 65, mortality is relatively moderate and deaths are distributed approximately uniformly across the five-year interval. Under this uniform distribution of deaths (UDD) assumption, the average age at death within the interval is exactly at the midpoint:

$$_n a_x = \frac{n}{2}$$

Substituting $_n a_x = \frac{n}{2}$ into the conversion formula yields the classical formula:

$$_n q_x = \frac{n \cdot {_n m_x}}{1 + \frac{n}{2} {_n m_x}}$$

For a five-year interval ($n = 5$):

$$_5 q_x = \frac{5 \cdot {_5 m_x}}{1 + 2.5 \cdot {_5 m_x}}$$

This simple equation provides an exceptionally accurate transformation for mature adult age groups.

## 4.3 Separation Factors and Chiang's Formulas for Infant and Child Mortality

The midpoint assumption ($_n a_x = n/2$) fails completely in infancy ($[0, 1)$) and early childhood ($[1, 5)$).
During the first year of life, biological mortality is heavily concentrated in the early neonatal period (days 0–6). An infant dying before age 1 does not live an average of $0.5$ years; instead, infant deaths occur on average at $0.1$ to $0.3$ years of life!
Similarly, between ages 1 and 4, deaths are concentrated in the second year of life ($x = 1$) rather than spread evenly across the four-year span.

### Keyfitz and Flieger Empirical Calibration for Infant Separation ($a_0$)
Nathan Keyfitz and Wilhelm Flieger established empirical regression equations for the infant separation factor $a_0$ based on the level of the infant central death rate $m_0$:
- For males:
  $$a_0 = \begin{cases} 0.045 + 2.684 \cdot m_0 & \text{if } m_0 < 0.107 \\ 0.330 & \text{if } m_0 \ge 0.107 \end{cases}$$
- For females:
  $$a_0 = \begin{cases} 0.053 + 2.800 \cdot m_0 & \text{if } m_0 < 0.107 \\ 0.350 & \text{if } m_0 \ge 0.107 \end{cases}$$

### Chiang's Abridged Life Table Methodology
C. L. Chiang (1968, 1984) formulated standard analytical estimators for the infant and child separation parameters:
1. For age 0 ($n = 1$):
   $$q_0 = \frac{m_0}{1 + (1 - a_0) m_0}$$
   $$L_0 = l_1 + a_0 \cdot d_0 = l_0 - (1 - a_0) d_0$$
2. For age 1–4 ($n = 4$):
   $$_4 a_1 = 1.50$$ (in low mortality settings, deaths occur around age 2.5).
   $$_4 q_1 = \frac{4 \cdot {_4 m_1}}{1 + (4 - {_4 a_1}) {_4 m_1}} = \frac{4 \cdot {_4 m_1}}{1 + 2.5 \cdot {_4 m_1}}$$
   $$_4 L_1 = 4 \cdot l_5 + {_4 a_1} \cdot {_4 d_1} = 4 \cdot l_5 + 1.50 \cdot {_4 d_1}$$

### The Terminal Open-Ended Age Group ($\omega+$)
For the oldest open-ended age bracket (e.g., ages $85+$ or $90+$), all individuals who enter the interval will eventually die within it:

$$q_{\omega} = 1.0000$$

$$d_{\omega} = l_{\omega}$$

Because $e_{\omega} = \frac{T_{\omega}}{l_{\omega}}$ and $m_{\omega} = \frac{d_{\omega}}{L_{\omega}} = \frac{l_{\omega}}{T_{\omega}}$:

$$L_{\omega} = T_{\omega} = \frac{l_{\omega}}{m_{\omega}}$$

$$e_{\omega} = \frac{1}{m_{\omega}}$$

This simple reciprocal identity closes the life table mathematically.

## 4.4 Continuous Formulation of Life Tables and Actuarial Functions

In mathematical demography and continuous actuarial science, the life table is formulated as a continuous probability model.

Let $X$ denote the random variable representing age at death (lifespan) of an individual from the synthetic cohort.
- The **Cumulative Distribution Function** is $F(x) = \mathbb{P}(X \le x) = 1 - S(x) = 1 - \frac{l(x)}{l_0}$.
- The **Probability Density Function** of age at death is:
  $$f(x) = \frac{d F(x)}{dx} = -\frac{1}{l_0} \frac{d l(x)}{dx} = \frac{l(x)}{l_0} \mu(x)$$
- The conditional probability density of dying at age $x+t$ given survival to age $x$ is:
  $$_t p_x \cdot \mu(x+t)$$
- The complete expectation of life is the expected value of remaining lifetime:
  $$e_x = \mathbb{E}[X - x \mid X > x] = \int_0^{\infty} t \left( _t p_x \mu(x+t) \right) dt$$
  Integrating by parts:
  $$e_x = \int_0^{\infty} {_t p_x} \, dt = \frac{1}{l(x)} \int_x^{\infty} l(t) \, dt = \frac{T(x)}{l(x)}$$

This establishes that the area under the curve of $l(t)$ from $x$ to $\infty$ divided by $l(x)$ equals the exact mathematical expectation of remaining life.

## 4.5 Applications in Actuarial Mathematics: Annuities and Life Assurances

Life tables provide the indispensable foundation for pricing private pensions, life insurances, and government social security programs.

### Life Assurances (Continuous Net Single Premium)
Let $\delta = \ln(1 + i)$ denote the force of interest corresponding to annual discount rate $i$. A continuous whole life assurance paying \$1 upon the death of an individual aged $x$ has an actuarial present value denoted by $\bar{A}_x$:

$$\bar{A}_x = \int_0^{\infty} e^{-\delta t} \, {_t p_x} \mu(x+t) \, dt$$

### Life Annuities
A continuous whole life annuity paying \$1 per annum continuously while an individual aged $x$ remains alive has an actuarial present value denoted by $\bar{a}_x$:

$$\bar{a}_x = \int_0^{\infty} e^{-\delta t} \, {_t p_x} \, dt$$

The fundamental actuarial identity connecting assurances and annuities is:

$$\bar{A}_x = 1 - \delta \cdot \bar{a}_x$$

This allows actuaries to price lifetime retirement annuities directly from demographic life tables.


### Comparative Mathematical Evaluation of Abridged Life Table Construction Methods
When transforming empirical central death rates into life table probabilities, demographers can deploy several alternative mathematical graduation paradigms. Understanding the subtle analytical differences between these classical methods is essential for choosing the appropriate technique in national statistical offices.

#### 1. The Chiang Formulation (1968, 1984)
Chin Long Chiang established the standard modern formulation based on the exact separation factor a(x), which represents the mean duration of life lived within the age interval by those who die. Chiang's method assumes that within each adult age group (from age five up to the penultimate age group), the distribution of deaths can be modeled linearly, leading to an average separation factor of exactly half the interval width. Chiang's primary methodological contribution was deriving closed-form mathematical expressions for the variance and covariance of all life table columns, establishing the first rigorous sampling theory for life tables. In Chiang's framework, cohort attrition is treated as a sequence of conditional binomial trials, allowing researchers to compute asymptotic confidence intervals for life expectancy at any age.

#### 2. The Reed–Merrell Formulation (1939)
Lowell J. Reed and Margaret Merrell developed their method at Johns Hopkins University by fitting an empirical exponential relationship between observed central death rates and life table mortality probabilities across a large corpus of historical life tables. Rather than assuming a linear distribution of deaths within the age interval, Reed and Merrell recognized that biological senescence causes the force of mortality to accelerate exponentially within five-year intervals at older ages. Their formula introduces a cubic correction factor that captures this second-order upward curvature. For five-year age intervals, the Reed-Merrell formula provides an exceptionally robust conversion that slightly elevates mortality probabilities at ages sixty and older compared to linear formulas, accurately reflecting accelerated physiological decline.

#### 3. The Greville Formulation (1943)
Thomas N. E. Greville formulated an analytical conversion that directly incorporates the slope of the central death rate curve itself. Greville assumed that the central death rate m(x) follows an exponential trajectory across adjacent age intervals, such that the force of mortality can be expressed as a Gompertz curve. Greville proved that the separation factor a(x) can be computed endogenously from the data by evaluating the difference between the logarithmic death rates of the preceding and succeeding age intervals. Consequently, Greville's method does not require an arbitrary external choice of separation factors; the data themselves determine the degree of curvature within each interval.

#### 4. Keyfitz–Frauenthal Non-Parametric Graduation (1975)
Nathan Keyfitz and James Frauenthal developed a refined numerical quadrature method that estimates the separation factor a(x) by fitting a second-degree polynomial (parabola) through three adjacent values of the living population and death counts. By using numerical integration across the three cohorts, Keyfitz and Frauenthal demonstrated that the separation factor can be expressed as a linear combination of adjacent population counts. This technique eliminates boundary artifacts and provides the highest degree of mathematical fidelity in populations undergoing rapid epidemiological transitions where mortality schedules depart from standard Gompertz models.


### Survival Analysis Connections: Kaplan–Meier, Nelson–Aalen, and Cox Models
In modern mathematical statistics, demography converges intimately with biostatistics and clinical epidemiology through the unified framework of **survival analysis** (time-to-event modeling). The fundamental life table functions developed by actuaries over three centuries map directly onto continuous stochastic processes.

#### The Kaplan–Meier Non-Parametric Product-Limit Estimator
In clinical trials and observational cohort studies, individuals are monitored over time, but many subjects are lost to follow-up, emigrate, or remain alive at the study termination date. In 1958, Edward L. Kaplan and Paul Meier formulated the non-parametric product-limit estimator for the survival function S(t) in the presence of right-censored data.

Let distinct death times be ordered chronologically: t_1 < t_2 < ... < t_k.
At death time t_i, let d_i denote the number of recorded deaths, and let r_i denote the number of individuals at risk (alive and under observation immediately prior to t_i). The Kaplan-Meier estimator is:

$$\hat{S}(t) = \prod_{t_i \le t} \left( 1 - \frac{d_i}{r_i} 
\right)$$

Notice that this is identically the life table product of conditional survival probabilities: S(x) = product of (1 - q_i). When there is no right-censoring, the Kaplan-Meier product-limit formula simplifies exactly to the empirical life table cohort proportion l(x) / l_0! Greenwood's formula provides the asymptotic variance of the Kaplan-Meier estimator:

$$\widehat{\text{Var}}(\hat{S}(t)) = [\hat{S}(t)]^2 \sum_{t_i \le t} \frac{d_i}{r_i (r_i - d_i)}$$

#### The Cox Proportional Hazards Model
In 1972, the British statistician David R. Cox revolutionized survival modeling by formulating the semiparametric **Proportional Hazards Model**. Cox expressed the hazard function (force of mortality mu(t; z)) for an individual with covariate vector z (such as blood pressure, smoking status, socioeconomic status, and genetic markers) as:

$$\mu(t; \mathbf{z}) = \mu_0(t) \exp(\boldsymbol{\beta}^T \mathbf{z})$$

where mu_0(t) is an unspecified, arbitrary baseline hazard function (analogous to the standard life table force of mortality), and beta is a vector of regression coefficients. Cox developed the method of **partial likelihood**, demonstrating that the parameter vector beta can be estimated with full asymptotic efficiency without estimating the baseline hazard function mu_0(t). This monumental breakthrough established the standard statistical framework used worldwide for evaluating medical treatments and demographic survival determinants.


### Classical Actuarial Commutation Functions: D_x, N_x, C_x, and M_x
Before modern electronic supercomputers revolutionized financial calculations, actuaries in life insurance companies and state pension systems relied upon pre-calculated **commutation columns** to price complex life contingencies and retirement annuities in seconds using simple arithmetic.

Let i denote the annual effective interest rate, and let v = 1 / (1 + i) denote the annual discount factor. Commutation functions blend the life table columns l_x and d_x directly with compound interest powers v^x:

1. **The D_x Column**:
   $$D_x = v^x \cdot l_x$$
   Represents the discounted cohort survival volume evaluated at age x.
2. **The N_x Column**:
   $$N_x = \sum_{y=x}^{\omega} D_y = D_x + D_{x+1} + D_{x+2} + \dots$$
   Represents the cumulative sum of D_x from age x to the end of the life table. The actuarial present value of an immediate whole life annuity of one dollar per year paying at the start of each year (annuity-due) is computed as:
   $$\ddot{a}_x = \frac{N_x}{D_x}$$
   A deferred life annuity paying starting at age 65 for a current 30-year-old is computed as the simple ratio:
   $${}_{35|}\ddot{a}_{30} = \frac{N_{65}}{D_{30}}$$
3. **The C_x Column**:
   $$C_x = v^{x+1} \cdot d_x$$
   Represents the discounted value of death benefits payable at the end of the year of death for individuals dying between ages x and x+1.
4. **The M_x Column**:
   $$M_x = \sum_{y=x}^{\omega} C_y = C_x + C_{x+1} + C_{x+2} + \dots$$
   Represents the cumulative sum of discounted death claims. The net single premium for a whole life assurance paying one dollar upon the death of an individual aged x is:
   $$A_x = \frac{M_x}{D_x}$$

By organizing life tables into commutation columns, eighteenth- and nineteenth-century actuaries transformed complex continuous integrals into simple table lookups, establishing the mathematical infrastructure of the modern global life insurance industry.

## Fully worked question 1: Complete Life Table Construction from Empirical Age-Specific Death Rates

### Question
An actuarial bureau constructs an abridged life table from registered deaths and census counts for a national population. The radix is $l_0 = 100{,}000$. The empirical central death rates ($_n m_x$) and calibrated separation factors ($_n a_x$) across seven key life intervals are given below:

| Age Interval $[x, x+n)$ | Interval Width ($n$) | Central Death Rate ($_n m_x$) | Separation Factor ($_n a_x$) |
| :---: | :---: | :---: | :---: |
| **0–1** | $1$ | $0.02500$ | $0.150$ |
| **1–5** | $4$ | $0.00250$ | $1.500$ |
| **5–15** | $10$ | $0.00060$ | $5.000$ |
| **15–30** | $15$ | $0.00120$ | $7.500$ |
| **30–50** | $20$ | $0.00350$ | $10.000$ |
| **50–70** | $20$ | $0.01500$ | $10.000$ |
| **70+** | $\infty$ | $0.08000$ | $e_{70} = 1/m_{70}$ |

1. Calculate the conditional mortality probability ($_n q_x$) and survival probability ($_n p_x$) for every age interval using the exact Greville-Chiang conversion formula.
2. Construct the survivor column ($l_x$) and death column ($_n d_x$) starting from radix $l_0 = 100{,}000$.
3. Compute the person-years lived in each interval ($_n L_x$), the cumulative person-years ($T_x$), and the expectation of life ($e_x$) at each attained age. Verify that $e_0$ accurately reflects life expectancy at birth.

### Solution, step 1: Calculate Mortality Probabilities ($_n q_x$)
The conversion formula is:

$$_n q_x = \frac{n \cdot {_n m_x}}{1 + (n - {_n a_x}) {_n m_x}}$$

1. **Age 0–1 ($n = 1, m_0 = 0.025, a_0 = 0.15$)**:
   $$n - a_0 = 1 - 0.15 = 0.85$$
   $$q_0 = \frac{1 \times 0.02500}{1 + 0.85 \times 0.02500} = \frac{0.02500}{1 + 0.02125} = \frac{0.02500}{1.02125} \approx 0.024480$$
   $$p_0 = 1 - 0.024480 = 0.975520$$

2. **Age 1–5 ($n = 4, _4 m_1 = 0.00250, _4 a_1 = 1.50$)**:
   $$n - {_4 a_1} = 4 - 1.50 = 2.50$$
   $$_4 q_1 = \frac{4 \times 0.00250}{1 + 2.50 \times 0.00250} = \frac{0.01000}{1 + 0.00625} = \frac{0.01000}{1.00625} \approx 0.009938$$
   $$_4 p_1 = 1 - 0.009938 = 0.990062$$

3. **Age 5–15 ($n = 10, _{10} m_5 = 0.00060, _{10} a_5 = 5.0$)**:
   $$n - a = 10 - 5.0 = 5.0$$
   $$_{10} q_5 = \frac{10 \times 0.00060}{1 + 5.0 \times 0.00060} = \frac{0.00600}{1 + 0.00300} = \frac{0.00600}{1.00300} \approx 0.005982$$
   $$_{10} p_5 = 1 - 0.005982 = 0.994018$$

4. **Age 15–30 ($n = 15, _{15} m_{15} = 0.00120, _{15} a_{15} = 7.5$)**:
   $$n - a = 15 - 7.5 = 7.5$$
   $$_{15} q_{15} = \frac{15 \times 0.00120}{1 + 7.5 \times 0.00120} = \frac{0.01800}{1 + 0.00900} = \frac{0.01800}{1.00900} \approx 0.017840$$
   $$_{15} p_{15} = 1 - 0.017840 = 0.982160$$

5. **Age 30–50 ($n = 20, _{20} m_{30} = 0.00350, _{20} a_{30} = 10.0$)**:
   $$n - a = 20 - 10.0 = 10.0$$
   $$_{20} q_{30} = \frac{20 \times 0.00350}{1 + 10.0 \times 0.00350} = \frac{0.07000}{1 + 0.03500} = \frac{0.07000}{1.03500} \approx 0.067633$$
   $$_{20} p_{30} = 1 - 0.067633 = 0.932367$$

6. **Age 50–70 ($n = 20, _{20} m_{50} = 0.01500, _{20} a_{50} = 10.0$)**:
   $$n - a = 20 - 10.0 = 10.0$$
   $$_{20} q_{50} = \frac{20 \times 0.01500}{1 + 10.0 \times 0.01500} = \frac{0.30000}{1 + 0.15000} = \frac{0.30000}{1.15000} \approx 0.260870$$
   $$_{20} p_{50} = 1 - 0.260870 = 0.739130$$

7. **Age 70+ (Terminal open-ended)**:
   $$q_{70} = 1.000000$$

### Solution, step 2: Compute Cohort Survivors ($l_x$) and Deaths ($_n d_x$)
Starting with radix $l_0 = 100{,}000$:

1. **Age 0**:
   $$d_0 = l_0 \cdot q_0 = 100{,}000 \times 0.024480 = 2{,}448$$
   $$l_1 = l_0 - d_0 = 100{,}000 - 2{,}448 = 97{,}552$$

2. **Age 1**:
   $$_4 d_1 = l_1 \cdot {_4 q_1} = 97{,}552 \times 0.009938 \approx 970$$
   $$l_5 = l_1 - {_4 d_1} = 97{,}552 - 970 = 96{,}582$$

3. **Age 5**:
   $$_{10} d_5 = l_5 \cdot {_{10} q_5} = 96{,}582 \times 0.005982 \approx 578$$
   $$l_{15} = l_5 - {_{10} d_5} = 96{,}582 - 578 = 96{,}004$$

4. **Age 15**:
   $$_{15} d_{15} = l_{15} \cdot {_{15} q_{15}} = 96{,}004 \times 0.017840 \approx 1{,}713$$
   $$l_{30} = l_{15} - {_{15} d_{15}} = 96{,}004 - 1{,}713 = 94{,}291$$

5. **Age 30**:
   $$_{20} d_{30} = l_{30} \cdot {_{20} q_{30}} = 94{,}291 \times 0.067633 \approx 6{,}377$$
   $$l_{50} = l_{30} - {_{20} d_{30}} = 94{,}291 - 6{,}377 = 87{,}914$$

6. **Age 50**:
   $$_{20} d_{50} = l_{50} \cdot {_{20} q_{50}} = 87{,}914 \times 0.260870 \approx 22{,}934$$
   $$l_{70} = l_{50} - {_{20} d_{50}} = 87{,}914 - 22{,}934 = 64{,}980$$

7. **Age 70+**:
   $$d_{70+} = l_{70} = 64{,}980$$
   Check sum: $2{,}448 + 970 + 578 + 1{,}713 + 6{,}377 + 22{,}934 + 64{,}980 = 100{,}000 = l_0$.

### Solution, step 3: Compute Person-Years Lived ($_n L_x$), Cumulative $T_x$, and Life Expectancy ($e_x$)
Using $_n L_x = n \cdot l_{x+n} + {_n a_x} \cdot {_n d_x}$:

1. **Age 0–1 ($n = 1, a_0 = 0.15$)**:
   $$L_0 = 1 \times l_1 + 0.15 \times d_0 = 97{,}552 + 0.15 \times 2{,}448 = 97{,}552 + 367.2 = 97{,}919$$

2. **Age 1–5 ($n = 4, _4 a_1 = 1.50$)**:
   $$_4 L_1 = 4 \times l_5 + 1.50 \times {_4 d_1} = 4 \times 96{,}582 + 1.50 \times 970 = 386{,}328 + 1{,}455 = 387{,}783$$

3. **Age 5–15 ($n = 10, _{10} a_5 = 5.0$)**:
   $$_{10} L_5 = 10 \times l_{15} + 5.0 \times {_{10} d_5} = 10 \times 96{,}004 + 5.0 \times 578 = 960{,}040 + 2{,}890 = 962{,}930$$

4. **Age 15–30 ($n = 15, _{15} a_{15} = 7.5$)**:
   $$_{15} L_{15} = 15 \times l_{30} + 7.5 \times {_{15} d_{15}} = 15 \times 94{,}291 + 7.5 \times 1{,}713 = 1{,}414{,}365 + 12{,}847.5 = 1{,}427{,}213$$

5. **Age 30–50 ($n = 20, _{20} a_{30} = 10.0$)**:
   $$_{20} L_{30} = 20 \times l_{50} + 10.0 \times {_{20} d_{30}} = 20 \times 87{,}914 + 10.0 \times 6{,}377 = 1{,}758{,}280 + 63{,}770 = 1{,}822{,}050$$

6. **Age 50–70 ($n = 20, _{20} a_{50} = 10.0$)**:
   $$_{20} L_{50} = 20 \times l_{70} + 10.0 \times {_{20} d_{50}} = 20 \times 64{,}980 + 10.0 \times 22{,}934 = 1{,}299{,}600 + 229{,}340 = 1{,}528{,}940$$

7. **Age 70+ (Terminal)**:
   $$L_{70+} = \frac{l_{70}}{m_{70}} = \frac{64{,}980}{0.08000} = 812{,}250$$

Now compute $T_x$ by backward accumulation from the terminal age:
- $T_{70} = L_{70+} = 812{,}250$
- $T_{50} = T_{70} + {_{20} L_{50}} = 812{,}250 + 1{,}528{,}940 = 2{,}341{,}190$
- $T_{30} = T_{50} + {_{20} L_{30}} = 2{,}341{,}190 + 1{,}822{,}050 = 4{,}163{,}240$
- $T_{15} = T_{30} + {_{15} L_{15}} = 4{,}163{,}240 + 1{,}427{,}213 = 5{,}590{,}453$
- $T_5 = T_{15} + {_{10} L_5} = 5{,}590{,}453 + 962{,}930 = 6{,}553{,}383$
- $T_1 = T_5 + {_4 L_1} = 6{,}553{,}383 + 387{,}783 = 6{,}941{,}166$
- $T_0 = T_1 + L_0 = 6{,}941{,}166 + 97{,}919 = 7{,}039{,}085$

Finally, compute the life expectancy $e_x = \frac{T_x}{l_x}$:
- **At Birth ($x = 0$)**:
  $$e_0 = \frac{T_0}{l_0} = \frac{7{,}039{,}085}{100{,}000} = 70.39 \text{ years}$$
- **At Age 1 ($x = 1$)**:
  $$e_1 = \frac{T_1}{l_1} = \frac{6{,}941{,}166}{97{,}552} = 71.15 \text{ years}$$
  *(Notice that $e_1 > e_0$ because surviving the high-mortality infant hurdle adds $0.76$ years to expected longevity!)*
- **At Age 5 ($x = 5$)**:
  $$e_5 = \frac{T_5}{l_5} = \frac{6{,}553{,}383}{96{,}582} = 67.85 \text{ years}$$
- **At Age 15 ($x = 15$)**:
  $$e_{15} = \frac{T_{15}}{l_{15}} = \frac{5{,}590{,}453}{96{,}004} = 58.23 \text{ years}$$
- **At Age 30 ($x = 30$)**:
  $$e_{30} = \frac{T_{30}}{l_{30}} = \frac{4{,}163{,}240}{94{,}291} = 44.15 \text{ years}$$
- **At Age 50 ($x = 50$)**:
  $$e_{50} = \frac{T_{50}}{l_{50}} = \frac{2{,}341{,}190}{87{,}914} = 26.63 \text{ years}$$
- **At Age 70 ($x = 70$)**:
  $$e_{70} = \frac{T_{70}}{l_{70}} = \frac{812{,}250}{64{,}980} = 12.50 \text{ years}$$

The complete mathematical life table is constructed with exact consistency.


### Analytical Properties of the Life Table: Rectangularization and Compression of Morbidity
A foundational topic in theoretical demography is the mathematical shape of the survival curve $l(x)$ and its evolution over the past two centuries. When demographers plot the cohort survivor column $l(x)$ against age $x$ across successive historical epochs, a striking geometric metamorphosis becomes apparent: the survival curve transforms from a gentle, steeply descending convex slope into an increasingly high, flat plateau that plunges almost vertically at advanced ages. This phenomenon is known as the **Rectangularization of the Survival Curve** (or the compression of mortality).

#### Mathematical Measurement of Rectangularization
To quantify the degree of rectangularization rigorously, mathematical demographers deploy several analytic metrics:
1. **The Interquartile Range of Age at Death ($IQR$)**: Let $x_{75}, x_{50}, x_{25}$ denote the ages at which the synthetic cohort survivor function $l(x)$ equals $75{,}000, 50{,}000,$ and $25{,}000$ respectively (corresponding to the 25th percentile, median, and 75th percentile of the life table distribution of deaths). The interquartile range is defined as:
   $$IQR = x_{25} - x_{75}$$
   In historical high-mortality populations, deaths were dispersed widely across the entire life span, resulting in an $IQR$ exceeding fifty or sixty years. In modern post-industrial societies with highly rectangularized survival curves, deaths are heavily concentrated into a narrow chronological band between ages 75 and 92, compressing the $IQR$ down to twelve or fourteen years.
2. **The Keyfitz Entropy Parameter ($H$)**: Nathan Keyfitz formulated a dimensionless measure of mortality entropy that characterizes the convexity of the survival curve:
   $$H = \frac{\int_0^{\infty} e(x) l(x) \mu(x) \, dx}{e_0 \cdot l_0} = -\frac{\int_0^{\infty} l(x) \ln l(x) \, dx}{\int_0^{\infty} l(x) \, dx}$$
   The entropy parameter $H$ possesses a profound biological interpretation: it represents the percentage increase in life expectancy at birth that would result from a uniform one percent proportional reduction in the force of mortality at all ages:
   $$\frac{d e_0 / e_0}{-d \mu / \mu} = H$$
   - For an idealized completely rectangular survival schedule where everyone lives to exact age $\omega$ and dies simultaneously, $H = 0$. In this limit, reducing mortality yields zero gain in life expectancy because lifespan is already maximal.
   - For a population subject to constant force of mortality $\mu(x) = \mu$ across all ages (an exponential survival curve $l(x) = l_0 e^{-\mu x}$), $H = 1$.
   - In modern developed countries, $H$ has declined steadily from approximately $0.80$ in the nineteenth century down to $0.15$ or $0.18$ today, demonstrating that human survival curves are approaching a highly rectangular state.

#### The Compression of Morbidity Hypothesis
In 1980, James F. Fries proposed the influential **Compression of Morbidity** hypothesis in medicine and actuarial science. Fries asserted that because maximum human biological lifespan is genetically bounded by teleomeric attrition, cellular oxidative damage, and physiological senescence, life expectancy cannot expand indefinitely. However, if the onset of chronic debilitating diseases (osteoarthritis, vascular dementia, cardiovascular impairment) can be delayed more rapidly than the modest gains in maximum life expectancy, the average duration of lifetime disability will be compressed into a very brief period immediately preceding death.

Testing Fries's hypothesis requires constructing **Health-Adjusted Life Tables (HALEs)** and **Disability-Free Life Tables (Sullivan Method)**, which partition total life table person-years $_n L_x$ into years lived in good functional health versus years lived with moderate or severe functional limitations. Actuaries and health economists use Sullivan's method to calculate the proportion of total life expectancy spent free of disability, providing vital empirical data for long-term care insurance and state pension sustainability.


### Model Life Tables: The Coale–Demeny and United Nations Empirical Systems
When vital registration systems in developing territories are severely defective or incomplete, actuaries and mathematical demographers cannot construct empirical life tables directly from observed death counts. Under such circumstances, demographers utilize **Model Life Tables**—standardized families of life tables derived from historical mortality patterns observed across dozens of populations with accurate vital records.

#### 1. The Coale–Demeny Regional Model Life Tables (1966, 1983)
Ansley J. Coale and Paul Demeny analyzed 326 historical life tables spanning Europe, North America, and Australasia. They discovered that while the overall level of mortality varies continuously, human mortality schedules cluster into four distinct regional families characterized by distinctive age-pattern ratios:
- **West Family**: Represents the general mortality pattern of modern human populations where causes of death are diversified. The West family is universally used as the default baseline when specific cause-of-death epidemiological information is lacking.
- **North Family**: Characterized by very low infant and childhood mortality relative to adult mortality, with elevated mortality among adults aged 45 to 65. Historically observed in Scandinavian countries (Norway, Sweden, Iceland) where maternal breastfeeding practices protected infants from waterborne pathogens, while adult cardiovascular disease and tuberculosis were common.
- **South Family**: Characterized by exceptionally high mortality at ages one through four relative to infant mortality under age one, accompanied by high mortality among adults aged 40 to 60. Historically observed in Southern Europe (Italy, Spain, Portugal) and parts of Latin America, reflecting infectious diarrheal weaning diseases in toddlerhood.
- **East Family**: Characterized by extremely high infant mortality and very high mortality at older adult ages (over age 50), with relatively favorable survival during late childhood and young adulthood. Historically observed in Central and Eastern Europe (Austria, Poland, Hungary, Russia) due to intense winter respiratory infections.

Coale and Demeny tabulated twenty-four distinct levels of mortality for each of the four families, indexing life expectancy at birth e_0 from 20.0 years (Level 1) to 80.0 years (Level 24) in increments of 2.5 years.

#### 2. The United Nations Model Life Tables for Developing Countries (1982)
Recognizing that 20th-century developing nations experienced modern antibiotic therapies and malaria eradication that altered the relationship between childhood and adult mortality differently from historical European patterns, the United Nations Population Division constructed five new empirical model families based on developing-country data:
- **Latin American Pattern**: High infant and child mortality relative to adult mortality, with favorable survival in late adulthood.
- **Chilean Pattern**: High infant mortality combined with low child mortality, driven by high prevalence of respiratory illnesses in infants.
- **South Asian Pattern**: Characterized by excessive mortality among female children and young women, reflecting socio-cultural discrimination and high maternal mortality risks.
- **Far Eastern Pattern**: Characterized by very high male adult mortality relative to female mortality, driven by high rates of tuberculosis and liver diseases (hepatitis B).
- **General Pattern**: An intermediate, composite developing-country schedule.

By matching observed child mortality from census birth histories to a specific model life table family, demographers can reconstruct complete adult survival curves and life expectancy with high statistical reliability.

## Fully worked question 2: Reed–Merrell Logarithmic Life Table Graduation

### Question
In 1939, Lowell J. Reed and Margaret Merrell developed a celebrated empirical equation relating the life table mortality probability $_n q_x$ to the central death rate $_n m_x$ through an exponential hazard function:

$$_n q_x = 1 - \exp\left( -n \cdot {_n m_x} - a \cdot n^3 \cdot {_n m_x}^2 \right)$$

where $a = 0.008$ is a universal empirical constant calibrated across global human populations.

An epidemiologist evaluates mortality in a high-risk adult demographic with the following observed central death rates:
- Five-year central death rate at age 45: $_5 m_{45} = 0.00850$
- Five-year central death rate at age 60: $_5 m_{60} = 0.02400$

1. Compute $_5 q_{45}$ and $_5 q_{60}$ using the Reed–Merrell formula ($n = 5, a = 0.008$).
2. Compare the Reed–Merrell results with the standard linear midpoint Chiang formula $_5 q_x^{\text{Chiang}} = \frac{5 \cdot {_5 m_x}}{1 + 2.5 \cdot {_5 m_x}}$.
3. Explain why the Reed–Merrell formula provides superior curvature correction in age intervals with rapidly accelerating mortality.

### Solution, step 1: Compute Probabilities Using Reed–Merrell
The Reed–Merrell formula with $n = 5$ is:
$n^3 = 5^3 = 125$.
$$a \cdot n^3 = 0.008 \times 125 = 1.000$$

Therefore, for $n = 5$, the Reed–Merrell exponent simplifies elegantly to:

$$_5 q_x = 1 - \exp\left( -5 \cdot {_5 m_x} - 1.0 \cdot {_5 m_x}^2 \right) = 1 - \exp\left( -[5 \cdot {_5 m_x} + {_5 m_x}^2] \right)$$

**Calculation for Age 45 ($_5 m_{45} = 0.00850$):**
- Linear term: $5 \times 0.00850 = 0.04250$
- Quadratic term: $(0.00850)^2 = 0.00007225$
- Exponent sum: $0.04250 + 0.00007225 = 0.04257225$
- Exponential value:
  $$\exp(-0.04257225) \approx 0.958319$$
- Mortality probability:
  $$_5 q_{45}^{\text{RM}} = 1 - 0.958319 = 0.041681$$

**Calculation for Age 60 ($_5 m_{60} = 0.02400$):**
- Linear term: $5 \times 0.02400 = 0.12000$
- Quadratic term: $(0.02400)^2 = 0.000576$
- Exponent sum: $0.12000 + 0.000576 = 0.120576$
- Exponential value:
  $$\exp(-0.120576) \approx 0.886409$$
- Mortality probability:
  $$_5 q_{60}^{\text{RM}} = 1 - 0.886409 = 0.113591$$

### Solution, step 2: Compare with the Linear Chiang Formula
Now evaluate the standard Chiang formula:

$$_5 q_x^{\text{Chiang}} = \frac{5 \cdot {_5 m_x}}{1 + 2.5 \cdot {_5 m_x}}$$

**For Age 45:**
$$_5 q_{45}^{\text{Chiang}} = \frac{5 \times 0.00850}{1 + 2.5 \times 0.00850} = \frac{0.04250}{1 + 0.02125} = \frac{0.04250}{1.02125} \approx 0.041616$$

Comparison at age 45:
- Reed–Merrell: $0.041681$
- Chiang: $0.041616$
- Discrepancy: $|0.041681 - 0.041616| = 0.000065$ (a negligible difference of $0.15\%$, confirming excellent concordance at moderate mortality levels).

**For Age 60:**
$$_5 q_{60}^{\text{Chiang}} = \frac{5 \times 0.02400}{1 + 2.5 \times 0.02400} = \frac{0.12000}{1 + 0.06000} = \frac{0.12000}{1.06000} \approx 0.113208$$

Comparison at age 60:
- Reed–Merrell: $0.113591$
- Chiang: $0.113208$
- Discrepancy: $0.113591 - 0.113208 = 0.000383$ (Reed–Merrell estimates a slightly higher probability).

### Solution, step 3: Analytical Rationale for the Reed–Merrell Quadratic Term
In human populations, the force of mortality $\mu(x)$ does not remain constant across a five-year interval; according to Gompertz's law, $\mu(x)$ accelerates exponentially.
If $\mu(t) = \mu_0 e^{\alpha t}$, the integral of the force of mortality is:

$$\int_0^n \mu(t) dt = \mu_0 \left( \frac{e^{\alpha n} - 1}{\alpha} \right)$$

Expanding $e^{\alpha n}$ via Taylor series:

$$\frac{e^{\alpha n} - 1}{\alpha} = n + \frac{1}{2} \alpha n^2 + \frac{1}{6} \alpha^2 n^3 + \dots$$

The linear formula assumes that $\int_0^n \mu(t) dt \approx n \cdot m_x$, which truncates the Taylor series at the first term. The Reed–Merrell term $-a n^3 m_x^2$ precisely captures the positive second-order curvature of the exponential Gompertz hazard. At older ages where $m_x > 0.02$, this quadratic curvature term prevents the underestimation of mortality probabilities inherent in simple linear approximations.


### Variance of Life Table Functions and Chiang's Large-Sample Variance of Life Expectancy
In applied demographic and public health research, life table functions are estimated from empirical samples of deaths and living populations, making them subject to random stochastic fluctuations. In 1960 and 1984, C. L. Chiang developed the classical large-sample variance formulas that allow mathematical demographers to attach standard errors and confidence intervals to life expectancy at birth $e_0$ and remaining life expectancy $e_x$.

#### The Binomial Sampling Model for Cohort Deaths
Consider the cohort in age interval $[x, x+n)$. Conditional on $l_x$ survivors entering the interval, the number of deaths $_n d_x$ follows a binomial distribution with sample size $l_x$ and probability parameter $_n q_x$:

$$_n d_x \sim \text{Binomial}(l_x, {_n q_x})$$

The variance of the sample mortality probability $_n q_x$ is given by:

$$\text{Var}(_n q_x) = \frac{_n q_x (1 - {_n q_x})}{l_x}$$

When converting from empirical central death rates $_n m_x = {_n D_x} / {_n P_x}$, Chiang showed that using the Taylor series delta method, the variance of the life table mortality probability is:

$$\text{Var}(_n q_x) = \frac{n^2 \cdot {_n m_x} (1 - {_n a_x} \cdot {_n m_x})}{_n P_x \cdot \left[ 1 + (n - {_n a_x}) {_n m_x} \right]^3}$$

#### Chiang's Variance Formula for Life Expectancy ($e_x$)
To derive the variance of the remaining life expectancy $e_x = T_x / l_x$, Chiang expressed $e_x$ as a linear combination of the conditional survival probabilities across all subsequent age intervals. By assuming that mortality probabilities in disjoint age intervals are stochastically independent, Chiang established that:

$$\text{Var}(e_x) = \sum_{y \ge x} \left( _n p_x \right)^2 \cdot \left[ (1 - {_n a_y}) \cdot n + e_{y+n} \right]^2 \cdot \text{Var}(_n q_y)$$

For life expectancy at birth ($x = 0$), this simplifies to:

$$\text{Var}(e_0) = \sum_{y=0}^{\omega} \left( \frac{l_y}{l_0} \right)^2 \cdot \left[ (1 - {_n a_y}) \cdot n + e_{y+n} \right]^2 \cdot \text{Var}(_n q_y)$$

The standard error is $\text{SE}(e_0) = \sqrt{\text{Var}(e_0)}$, allowing the construction of asymptotic ninety-five percent Wald confidence intervals:

$$\text{CI}_{95\%}(e_0) = \left[ \hat{e}_0 - 1.96 \cdot \text{SE}(\hat{e}_0), \; \hat{e}_0 + 1.96 \cdot \text{SE}(\hat{e}_0) \right]$$

In municipal health departments and small island nations where population counts are modest (e.g., populations under 100,000), Chiang's variance formulas provide the indispensable statistical foundation for determining whether observed gains in life expectancy represent genuine epidemiological improvements or mere random sampling noise.

### Sullivan's Method for Health-Adjusted and Disability-Free Life Expectancy
In modern health economics, demographers go beyond measuring mere length of life to quantify the qualitative health status of person-years lived. In 1971, D. F. Sullivan formulated an elegant mathematical extension of the life table that integrates prevalence data on chronic disability with standard life table person-years.

#### Mathematical Formulation of Sullivan's Health Table
Let $_n L_x$ denote the standard life table person-years lived between ages $x$ and $x+n$.
Let $_n \pi_x$ denote the age-specific prevalence of chronic illness, severe functional limitation, or cognitive disability in the living population, typically measured through representative national health interview surveys (such as the National Health and Nutrition Examination Survey or European Health Interview Survey):

$$_n \pi_x = \frac{\text{Number of Persons with Disability in Age Interval } [x, x+n)}{_n P_x}$$

Sullivan partitions the total person-years $_n L_x$ into two mutually exclusive components:
1. **Person-Years Lived with Disability**:
   $$_n L_x^D = {_n \pi_x} \cdot {_n L_x}$$
2. **Person-Years Lived Free of Disability**:
   $$_n L_x^{DF} = (1 - {_n \pi_x}) \cdot {_n L_x}$$

The total cumulative disability-free person-years remaining above age $x$ is:

$$T_x^{DF} = \sum_{y \ge x} {_n L_y^{DF}} = \sum_{y \ge x} (1 - {_n \pi_y}) \cdot {_n L_y}$$

The **Disability-Free Life Expectancy ($DFLE_x$)** (also termed healthy life years) is:

$$DFLE_x = \frac{T_x^{DF}}{l_x}$$

The **Proportion of Remaining Life Spent Free of Disability** is:

$$P_{DF}(x) = \frac{DFLE_x}{e_x} \times 100 = \frac{T_x^{DF}}{T_x} \times 100$$

Sullivan's method reveals striking public health realities: while biological life expectancy at birth $e_0$ in Western nations often reaches eighty-two years, disability-free life expectancy $DFLE_0$ is frequently between sixty-eight and seventy-two years, indicating that individuals spend an average of ten to fourteen years living with chronic functional impairments. Comparing $DFLE$ across cohorts over time provides the decisive empirical test of the Fries compression of morbidity hypothesis.

## Fully worked question 3: Actuarial Present Value of Retirement Pensions from Life Table Functions

### Question
An actuary designs a defined-benefit pension annuity for an employee retiring at exact age 65. The demographic survival schedule of the company's pension fund is characterized by the following abridged life table parameters starting at age 65:

| Age ($x$) | Survivors ($l_x$) | Person-Years ($L_x$) |
| :---: | :---: | :---: |
| **65** | $80{,}000$ | $375{,}000$ (Ages 65–70) |
| **70** | $70{,}000$ | $315{,}000$ (Ages 70–75) |
| **75** | $56{,}000$ | $230{,}000$ (Ages 75–80) |
| **80** | $36{,}000$ | $130{,}000$ (Ages 80–85) |
| **85** | $16{,}000$ | $64{,}000$ (Ages 85+) |

The pension plan provides an annual lifetime annuity payment of $B = \$30{,}000$ per year, paid continuously until death. The fund assumes a conservative risk-free interest rate of $i = 4.0\%$ per annum, corresponding to a force of interest $\delta = \ln(1 + 0.04) \approx 0.039221$.

1. Calculate the undiscounted Life Expectancy at age 65 ($e_{65}$) and the total expected undiscounted payout over the retiree's remaining lifespan.
2. Approximate the actuarial present value of the lifetime continuous annuity $\bar{a}_{65}$ by discounting the person-years lived in each five-year age interval to age 65 using the interval midpoint discount factor $v^{t + n/2} = e^{-\delta(t + 2.5)}$.
3. Determine the required initial capital reserve that must be deposited into the retiree's individual pension account at age 65 to fully fund the annuity.

### Solution, step 1: Compute Undiscounted Life Expectancy and Payout
Total person-years remaining above age 65 ($T_{65}$) is the sum of person-years in all intervals from age 65 onwards:

$$T_{65} = \sum_{x \ge 65} L_x = 375{,}000 + 315{,}000 + 230{,}000 + 130{,}000 + 64{,}000 = 1{,}114{,}000 \text{ person-years}$$

The undiscounted life expectancy at age 65 is:

$$e_{65} = \frac{T_{65}}{l_{65}} = \frac{1{,}114{,}000}{80{,}000} = 13.925 \text{ years}$$

A typical retiree at age 65 is expected to live an additional $13.925$ years (surviving to approximately age 78.9).

The total undiscounted expected cash payout is:

$$\text{Total Expected Payout} = B \times e_{65} = \$30{,}000 \times 13.925 = \$417{,}750$$

### Solution, step 2: Actuarial Discounting of Annuity Person-Years
The continuous actuarial present value of an annuity of \$1 per year is:

$$\bar{a}_{65} = \frac{1}{l_{65}} \int_0^{\infty} e^{-\delta t} l(65 + t) \, dt$$

We evaluate this integral numerically by discounting each five-year cohort $L_x$ using its midpoint distance $t_{\text{mid}}$ from retirement age 65:

1. **Ages 65–70 ($t \in [0, 5)$, $t_{\text{mid}} = 2.5$, $L_{65} = 375{,}000$)**:
   $$\delta \times 2.5 = 0.039221 \times 2.5 = 0.098053$$
   $$v^{2.5} = e^{-0.098053} \approx 0.906602$$
   $$\text{Discounted PY}_1 = 375{,}000 \times 0.906602 = 339{,}976$$

2. **Ages 70–75 ($t \in [5, 10)$, $t_{\text{mid}} = 7.5$, $L_{70} = 315{,}000$)**:
   $$\delta \times 7.5 = 0.039221 \times 7.5 = 0.294158$$
   $$v^{7.5} = e^{-0.294158} \approx 0.745156$$
   $$\text{Discounted PY}_2 = 315{,}000 \times 0.745156 = 234{,}724$$

3. **Ages 75–80 ($t \in [10, 15)$, $t_{\text{mid}} = 12.5$, $L_{75} = 230{,}000$)**:
   $$\delta \times 12.5 = 0.039221 \times 12.5 = 0.490263$$
   $$v^{12.5} = e^{-0.490263} \approx 0.612465$$
   $$\text{Discounted PY}_3 = 230{,}000 \times 0.612465 = 140{,}867$$

4. **Ages 80–85 ($t \in [15, 20)$, $t_{\text{mid}} = 17.5$, $L_{80} = 130{,}000$)**:
   $$\delta \times 17.5 = 0.039221 \times 17.5 = 0.686368$$
   $$v^{17.5} = e^{-0.686368} \approx 0.503399$$
   $$\text{Discounted PY}_4 = 130{,}000 \times 0.503399 = 65{,}442$$

5. **Ages 85+ ($t \ge 20$, average remaining life in open interval $\approx 4.0$ years, $t_{\text{eff}} \approx 24.0$, $L_{85} = 64{,}000$)**:
   $$\delta \times 24.0 = 0.039221 \times 24.0 = 0.941304$$
   $$v^{24.0} = e^{-0.941304} \approx 0.390117$$
   $$\text{Discounted PY}_5 = 64{,}000 \times 0.390117 = 24{,}967$$

**Total Actuarially Discounted Person-Years**:

$$T_{65}^{\text{disc}} = 339{,}976 + 234{,}724 + 140{,}867 + 65{,}442 + 24{,}967 = 805{,}976$$

The actuarial annuity value per dollar of annual benefit is:

$$\bar{a}_{65} = \frac{T_{65}^{\text{disc}}}{l_{65}} = \frac{805{,}976}{80{,}000} \approx 10.0747$$

### Solution, step 3: Calculate Required Capital Reserve
The capital reserve required at retirement is the product of the annual benefit $B$ and the actuarial annuity value $\bar{a}_{65}$:

$$\text{Required Reserve} = B \times \bar{a}_{65} = \$30{,}000 \times 10.0747 = \$302{,}241$$

**Actuarial Risk and Finance Synthesis**:
1. Without interest discounting, funding $13.925$ years of retirement requires $\$417{,}750$.
2. Because invested funds earn a $4.0\%$ compound return while the pensioner ages, the pension fund requires only $\$302{,}241$ at age 65 to guarantee all future payments. The difference of $\$115{,}509$ ($27.6\%$) is generated entirely by compound investment interest.
3. If an individual pensioner dies earlier than average (e.g., at age 68), the unspent capital reserve remains in the fund, exactly subsidizing individuals who live past age 90. This fundamental actuarial pooling mechanism is known as **mortality cross-subsidization** (or survival credits).
