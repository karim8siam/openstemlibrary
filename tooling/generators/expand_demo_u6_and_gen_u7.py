import re
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-demography-and-population-statistics")

def prose_count(text):
    text = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    text = re.sub(r"\$[^$\n]+\$", " ", text)
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    return len(words)

# Expand Unit 6
u6 = (OUT_DIR / "unit-6.md").read_text(encoding="utf-8")
u6_add = """
### Non-Linear Generalizations: The Gompertz and von Bertalanffy Growth Models
While the Verhulst–Pearl logistic model assumes exact point-symmetry about its inflection point $K/2$, empirical demographic growth trajectories often exhibit marked asymmetry: human and economic expansions frequently accelerate rapidly during early phases and experience prolonged, gradual deceleration as carrying capacities are approached, or vice versa. To model asymmetric growth, mathematical demographers deploy generalized growth curves.

#### 1. The Gompertz Growth Model
Originally formulated by Benjamin Gompertz in 1825 for actuarial mortality, the Gompertz curve was adapted by demographers and econometricians to model population growth where the proportional growth rate declines exponentially over time:

$$\\frac{d \\ln P}{dt} = r \\, e^{-\\alpha t}$$

Integrating this differential relationship yields the double-exponential **Gompertz Growth Function**:

$$P(t) = K \\, \\exp\\left( -b \\, e^{-\\alpha t} \\right) = K \\, a^{b^t}$$

where:
- $K$ is the asymptotic carrying capacity.
- $\\alpha > 0$ governs the rate of growth deceleration.
- $b > 0$ is a positioning parameter related to the initial population $P_0 = K e^{-b}$.

The Gompertz curve possesses a fundamentally asymmetric inflection point:
$$\\frac{d^2 P}{dt^2} = 0 \\implies P^* = \\frac{K}{e} \\approx 0.3679 \\, K$$
Unlike the symmetric logistic curve whose inflection point occurs at fifty percent of carrying capacity ($0.50 K$), the Gompertz inflection point occurs earlier, at approximately thirty-seven percent ($1/e$) of the asymptote. This makes the Gompertz model exceptionally well-suited for modeling the adoption of modern family planning techniques, urban population surges, and life expectancy expansions.

#### 2. The von Bertalanffy Growth Curve
In bio-demography and ecological population dynamics, Ludwig von Bertalanffy (1938) derived a growth model based on the physiological balance between anabolic processes (mass synthesis proportional to surface area or metabolic rate $P^m$) and catabolic breakdown (tissue loss proportional to total body mass $P$):

$$\\frac{dP}{dt} = \\eta P^m - \\gamma P$$

When $m = 2/3$ (representing surface-area scaling in organismal biology), the analytical solution is:

$$P(t) = K \\left( 1 - \\beta \\, e^{-k t} \\right)^3$$

In spatial human demography, this model captures the growth of enclosed municipal systems where physical infrastructure development scales with municipal area while maintenance costs scale with total population.

### Rhodes' Differential Method of Logistic Fitting
In 1940, E. C. Rhodes developed an alternative technique to fit the logistic curve that utilizes all available historical census points rather than relying upon three arbitrary equidistant points.

Recall the logistic differential equation $\\frac{1}{P} \\frac{dP}{dt} = r - \\frac{r}{K} P$. Rhodes noted that this can be expressed as a simple linear regression model:

$$y = A - B \\cdot x$$

where $y = \\frac{1}{P} \\frac{dP}{dt}$ is the instantaneous relative growth rate, $x = P$ is the population size, the intercept is $A = r$, and the slope is $B = r / K$.

In empirical census data, the continuous derivative $\\frac{dP}{dt}$ is approximated by the central difference quotient between consecutive censuses:

$$\\left( \\frac{dP}{dt} \\right)_t \\approx \\frac{P_{t+1} - P_{t-1}}{t_{t+1} - t_{t-1}}$$

and the corresponding population $P$ is the mid-interval value $P_t$. By running ordinary least squares (OLS) regression of the empirical relative growth rates on population sizes across ten or more historical censuses, demographers obtain robust, noise-dampened estimates of both $r$ and $K = A / B$. This regression-based approach avoids the sensitivity to outlier years inherent in the classical three-point method.
"""

u6 = u6.replace("## Fully worked question 2", u6_add + "\n## Fully worked question 2")
(OUT_DIR / "unit-6.md").write_text(u6, encoding="utf-8")
print(f"Deeply Expanded Unit 6: {prose_count((OUT_DIR / 'unit-6.md').read_text(encoding='utf-8'))} words")

# ==============================================================================
# UNIT 7: Stable and Stationary Population Theory (Lotka System)
# ==============================================================================
u7_content = """# Unit 7: Stable and Stationary Population Theory (Lotka System)

Stable population theory is the theoretical pinnacle of mathematical demography. Formulated between 1907 and 1939 by the physical chemist and statistician Alfred J. Lotka (in collaboration with F. R. Sharpe), stable population theory investigates the long-term mathematical consequences of subjecting a closed human population to fixed, unchanging schedules of age-specific fertility and mortality. Lotka proved that regardless of its initial, arbitrary age distribution, any closed population subjected to constant vital rates will eventually converge toward a unique, time-invariant relative age distribution, expanding or contracting at a constant intrinsic rate of natural increase $r$. This profound asymptotic convergence forms the foundation for indirect demographic estimation in developing nations lacking complete vital statistics.

## 7.1 The Stationary Population as an Actuarial Limiting Case

Before examining the general stable model where populations grow or shrink, we examine the foundational baseline of zero growth: the **Stationary Population**.

### Definition of a Stationary Population
A **Stationary Population** is a special demographic state characterized by two defining conditions:
1. The total population size remains strictly constant over time: $\\frac{dN}{dt} = 0$, meaning the annual rate of natural increase is identically zero ($r = 0$).
2. The age-sex distribution is completely unchanging over time, and annual births exactly equal annual deaths: $B(t) = D(t) = B_0 = \\text{constant}$.
3. Net international migration is zero (closed population).
4. The Net Reproduction Rate is exactly unity: $NRR = 1.000$.

### The Equivalence Between Life Table Functions and the Stationary Population
A remarkable mathematical isomorphism exists between the life table of Unit 4 and a stationary population: **the life table columns describe the exact physical composition of a living stationary population**.

Let a stationary population be generated by a continuous stream of $l_0$ annual births ($B = l_0$) evenly distributed across each calendar year, subjected to unchanging life table survival schedule $l(x)$:
- The number of individuals surviving to celebrate exact birthday $x$ in any calendar year is $l_x$.
- The number of deaths occurring between ages $x$ and $x+n$ during any calendar year is $_n d_x$.
- The enumerated population living in age group $[x, x+n)$ at any given moment is exactly equal to the life table person-years column:
  $$_n P_x = {_n L_x}$$
- The total population of the stationary state is the cumulative person-years column at birth:
  $$N_{\\text{stat}} = T_0 = \\int_0^{\\infty} l(t) \\, dt = l_0 \\cdot e_0$$

### Fundamental Demographic Identities in a Stationary Population
From the relationship $N_{\\text{stat}} = l_0 \\cdot e_0$:
1. The **Birth Rate** of a stationary population is:
   $$b = \\frac{B}{N_{\\text{stat}}} = \\frac{l_0}{l_0 \\cdot e_0} = \\frac{1}{e_0}$$
2. The **Death Rate** of a stationary population is:
   $$d = \\frac{D}{N_{\\text{stat}}} = \\frac{l_0}{l_0 \\cdot e_0} = \\frac{1}{e_0}$$
3. The Rate of Natural Increase is:
   $$r = b - d = \\frac{1}{e_0} - \\frac{1}{e_0} = 0$$

In a stationary population, **the crude birth rate and the crude death rate are identically equal to the mathematical reciprocal of life expectancy at birth**:

$$b = d = \\frac{1}{e_0}$$

For example, in a stationary population with a life expectancy of $e_0 = 80$ years:
$$b = d = \\frac{1}{80} = 0.0125 \\implies 12.5 \\text{ per 1,000}$$
If life expectancy is $e_0 = 50$ years, the birth and death rates must both equal $20.0$ per $1{,}000$.

## 7.2 Lotka's Continuous Stable Population Model

In 1907, Alfred J. Lotka generalized the stationary model to populations undergoing continuous exponential growth or decline ($r \\ne 0$).

### Core Postulates of the Stable Population Model
1. The population is **closed to migration** ($M = 0$).
2. The force of mortality $\\mu(x)$ (and hence survival function $p(x) = l(x)/l_0$) is fixed and invariant over time.
3. The force of fertility $m(x)$ (age-specific birth rate for female births) is fixed and invariant over time.

### The Integral Equation of Birth Trajectories
Let $B(t)$ denote the continuous number of births occurring in the population at time $t$. Any birth occurring at time $t$ must be born to a mother aged $x \\in [\\alpha, \\beta]$ (where $\\alpha = 15$ and $\\beta = 50$ are the physiological boundaries of reproduction).
A mother who is aged $x$ at time $t$ was herself born at time $t - x$.
The number of surviving women aged $x$ at time $t$ is:
$$W(x, t) = B(t - x) \\cdot p(x)$$
Multiplying by the age-specific fertility rate $m(x)$ and integrating across all reproductive ages yields **Lotka's Renewal Equation**:

$$B(t) = \\int_0^{\\infty} B(t - x) \\, p(x) \\, m(x) \\, dx$$

### The Stable Exponential Solution
Lotka postulated that as time $t \\to \\infty$, the birth trajectory converges to an exponential curve:
$$B(t) = B_0 \\, e^{r t}$$
where $r$ is the constant intrinsic rate of natural increase.
Substitute this trial solution into the renewal equation:

$$B_0 \\, e^{r t} = \\int_0^{\\infty} B_0 \\, e^{r (t - x)} \\, p(x) \\, m(x) \\, dx$$

Divide both sides by $B_0 e^{rt}$:

$$1 = \\int_0^{\\infty} e^{-r x} \\, p(x) \\, m(x) \\, dx$$

This is the celebrated **Lotka Characteristic Equation** (Euler–Lotka equation). It defines an implicit non-linear relationship between the biological vital rate schedules $\\{p(x), m(x)\\}$ and the intrinsic rate of growth $r$.

## 7.3 Derivation of the Stable Age Distribution $c(x)$

In a stable population, what proportion of the population is aged $x$?

Let $N(t)$ denote total population size at time $t$. Under continuous exponential growth:
$$N(t) = N_0 \\, e^{r t}$$
The number of individuals alive at exact age $x$ at time $t$ is the survivors of those born $x$ years ago:
$$N(x, t) = B(t - x) \\, p(x) = B_0 \\, e^{r (t - x)} \\, p(x) = B(t) \\, e^{-r x} \\, p(x)$$

The proportion of the population at exact age $x$, denoted by $c(x) = \\frac{N(x, t)}{N(t)}$, is:

$$c(x) = \\frac{B(t)}{N(t)} \\, e^{-r x} \\, p(x) = b \\, e^{-r x} \\, p(x)$$

where $b = \\frac{B(t)}{N(t)}$ is the constant **Intrinsic Birth Rate**.

### Normalization and the Intrinsic Birth Rate
Because $c(x)$ is a probability density function across all ages $[0, \\infty)$, it must integrate to unity:

$$\\int_0^{\\infty} c(x) \\, dx = 1$$

Substitute $c(x) = b \\, e^{-rx} p(x)$:

$$b \\int_0^{\\infty} e^{-r x} \\, p(x) \\, dx = 1$$

Solving for the Intrinsic Birth Rate:

$$b = \\frac{1}{\\int_0^{\\infty} e^{-r x} \\, p(x) \\, dx}$$

The **Intrinsic Death Rate ($d$)** follows from demographic accounting:

$$d = b - r$$

### Comparison of Age Distributions:
- **If $r = 0$ (Stationary)**: $c(x) = b \\cdot p(x) = \\frac{l(x)}{T_0}$. The age distribution is shaped entirely by biological mortality $p(x)$.
- **If $r > 0$ (Growing Stable Population)**: The factor $e^{-rx}$ acts as an exponential discount factor with age. The age distribution is tilted toward younger ages, expanding the base of children and young adults (young age structure).
- **If $r < 0$ (Declining Stable Population)**: The factor $e^{-rx} = e^{|r|x}$ expands with age, tilting the age distribution toward older cohorts and accelerating population aging.

## 7.4 Solving the Characteristic Equation via Euler–Lotka Polynomials

The characteristic equation $\\int_0^{\\infty} e^{-rx} p(x) m(x) dx = 1$ cannot be solved in closed elementary form. To solve for $r$ numerically, Lotka expanded the exponential $e^{-rx}$ using Taylor series around $r = 0$.

Define the **Net Maternity Function** $\\phi(x) = p(x) m(x)$.
The $k$-th moment of the net maternity function about age zero is:

$$R_k = \\int_0^{\\infty} x^k \\, \\phi(x) \\, dx = \\int_0^{\\infty} x^k \\, p(x) \\, m(x) \\, dx$$

Notice that:
- $R_0 = \\int_0^{\\infty} \\phi(x) \\, dx = NRR$ (The Net Reproduction Rate!).
- $R_1 = \\int_0^{\\infty} x \\, \\phi(x) \\, dx$ is the first moment of childbearing age.
- $\\mu = \\frac{R_1}{R_0} = T$ is the **Mean Age of Childbearing in the Stationary Population** (mean generation length).
- $\\sigma^2 = \\frac{R_2}{R_0} - \\mu^2$ is the variance of age at childbearing.

### Taylor Series Expansion of the Characteristic Equation
Expanding $e^{-rx} = 1 - rx + \\frac{1}{2} r^2 x^2 - \\dots$:

$$1 = \\int_0^{\\infty} \\left( 1 - r x + \\frac{1}{2} r^2 x^2 - \\dots \\right) \\phi(x) \\, dx$$

$$1 = R_0 - r R_1 + \\frac{1}{2} r^2 R_2 - \\dots$$

Divide by $R_0 = NRR$:

$$\\frac{1}{R_0} = 1 - r \\left( \\frac{R_1}{R_0} \\right) + \\frac{1}{2} r^2 \\left( \\frac{R_2}{R_0} \\right) - \\dots$$

Taking the natural logarithm of both sides and using $\\ln(1 - z) \\approx -z - \\frac{z^2}{2}$:

$$-\\ln(R_0) \\approx -r \\mu + \\frac{1}{2} r^2 \\sigma^2$$

$$\\ln(NRR) \\approx r T - \\frac{1}{2} r^2 \\sigma^2$$

### Lotka's Second-Order Approximation for $r$:
Neglecting the variance term $\\frac{1}{2} r^2 \\sigma^2$ yields the first-order approximation:

$$r_1 = \\frac{\\ln(NRR)}{T}$$

Substituting $r_1$ into the quadratic term yields Lotka's celebrated second-order formula:

$$r \\approx \\frac{\\ln(NRR)}{T - \\frac{1}{2} \\sigma^2 \\frac{\\ln(NRR)}{T}}$$

This quadratic correction provides exceptional numerical accuracy, matching iterative numerical root-finding algorithms to within four decimal places.

## 7.5 Coale's Regional Model Stable Populations and Indirect Demographic Estimation

In developing countries lacking reliable vital registration, Ansley J. Coale and Paul Demeny (1966, 1983) utilized stable population theory to create the **Coale–Demeny Regional Model Life Tables and Stable Populations**.

Coale and Demeny assembled thousands of empirical mortality schedules and identified four distinct mortality families based on historical European patterns:
1. **North Family**: High infant mortality and low old-age mortality.
2. **South Family**: Elevated adult mortality and high cardiovascular burden.
3. **East Family**: High tuberculosis and infectious respiratory mortality.
4. **West Family**: The general, balanced mortality pattern representing standard global mortality.

By crossing each mortality family across twenty-four levels of life expectancy ($e_0$ from 20 to 80 years) and thirteen intrinsic growth rates ($r$ from $-1\\%$ to $+4\\%$), Coale and Demeny tabulated complete sets of model stable age distributions. When an analyst conducts a census in a developing nation and observes only the proportion of children under age 15 ($P_{0-14}$) and the intercensal growth rate $r$, the analyst can look up the corresponding model stable table to deduce the unobserved life expectancy at birth $e_0$, crude birth rate $b$, and infant mortality rate $q_0$ without vital registration!

## Fully worked question 1: Numerical Solution of the Lotka Characteristic Equation and Intrinsic Growth Rate

### Question
A mathematical demographer estimates the net maternity schedule $\\phi(x) = p(x) m(x)$ for a female population in quinquennial reproductive intervals:

| Age Interval ($x$ to $x+5$) | Interval Midpoint ($x_m$) | Net Maternity Value ($_5 \\phi_x$) |
| :---: | :---: | :---: |
| **15–19** | $17.5$ | $0.0300$ |
| **20–24** | $22.5$ | $0.1100$ |
| **25–29** | $27.5$ | $0.1400$ |
| **30–34** | $32.5$ | $0.1000$ |
| **35–39** | $37.5$ | $0.0500$ |
| **40–44** | $42.5$ | $0.0150$ |
| **45–49** | $47.5$ | $0.0020$ |

1. Calculate the zero-th moment $R_0$ (the Net Reproduction Rate, $NRR$), the first moment $R_1$, the second moment $R_2$, the mean length of generation $T$, and the variance of age at childbearing $\\sigma^2$.
2. Compute the first-order approximation of the intrinsic rate of natural increase ($r_1 = \\frac{\\ln NRR}{T}$) and the refined second-order Lotka correction ($r_2$).
3. Perform two iterations of the Newton–Raphson algorithm on the discrete characteristic function $f(r) = \\sum_{i=1}^7 e^{-r x_m} \\cdot (5 \\cdot {_5 \\phi_x}) - 1 = 0$ to determine the exact intrinsic growth rate $r^*$.

### Solution, step 1: Calculate Moments of the Net Maternity Function
The discrete moments of the distribution are:
$$R_0 = 5 \\times \\sum {_5 \\phi_x}$$
$$R_1 = 5 \\times \\sum (x_m \\cdot {_5 \\phi_x})$$
$$R_2 = 5 \\times \\sum (x_m^2 \\cdot {_5 \\phi_x})$$

We compute the products for each age interval:
- **Ages 15–19 ($x_m = 17.5, \\phi = 0.0300$)**:
  $$x_m \\phi = 17.5 \\times 0.0300 = 0.5250$$
  $$x_m^2 \\phi = (17.5)^2 \\times 0.0300 = 306.25 \\times 0.0300 = 9.1875$$
- **Ages 20–24 ($x_m = 22.5, \\phi = 0.1100$)**:
  $$x_m \\phi = 22.5 \\times 0.1100 = 2.4750$$
  $$x_m^2 \\phi = 506.25 \\times 0.1100 = 55.6875$$
- **Ages 25–29 ($x_m = 27.5, \\phi = 0.1400$)**:
  $$x_m \\phi = 27.5 \\times 0.1400 = 3.8500$$
  $$x_m^2 \\phi = 756.25 \\times 0.1400 = 105.8750$$
- **Ages 30–34 ($x_m = 32.5, \\phi = 0.1000$)**:
  $$x_m \\phi = 32.5 \\times 0.1000 = 3.2500$$
  $$x_m^2 \\phi = 1056.25 \\times 0.1000 = 105.6250$$
- **Ages 35–39 ($x_m = 37.5, \\phi = 0.0500$)**:
  $$x_m \\phi = 37.5 \\times 0.0500 = 1.8750$$
  $$x_m^2 \\phi = 1406.25 \\times 0.0500 = 70.3125$$
- **Ages 40–44 ($x_m = 42.5, \\phi = 0.0150$)**:
  $$x_m \\phi = 42.5 \\times 0.0150 = 0.6375$$
  $$x_m^2 \\phi = 1806.25 \\times 0.0150 = 27.09375$$
- **Ages 45–49 ($x_m = 47.5, \\phi = 0.0020$)**:
  $$x_m \\phi = 47.5 \\times 0.0020 = 0.0950$$
  $$x_m^2 \\phi = 2256.25 \\times 0.0020 = 4.5125$$

Summing the columns:
$$\\sum \\phi = 0.0300 + 0.1100 + 0.1400 + 0.1000 + 0.0500 + 0.0150 + 0.0020 = 0.4470$$
$$\\sum x_m \\phi = 0.5250 + 2.4750 + 3.8500 + 3.2500 + 1.8750 + 0.6375 + 0.0950 = 12.7075$$
$$\\sum x_m^2 \\phi = 9.1875 + 55.6875 + 105.8750 + 105.6250 + 70.3125 + 27.09375 + 4.5125 = 378.29375$$

Now multiply by interval width $n = 5$:
- **Zero-th Moment ($NRR$)**:
  $$R_0 = 5 \\times 0.4470 = 2.2350$$
  *(The Net Reproduction Rate is $2.235$ daughters per woman).*
- **First Moment ($R_1$)**:
  $$R_1 = 5 \\times 12.7075 = 63.5375$$
- **Second Moment ($R_2$)**:
  $$R_2 = 5 \\times 378.29375 = 1{,}891.46875$$

Now compute the mean and variance:
- **Mean Generation Length ($T$)**:
  $$T = \\frac{R_1}{R_0} = \\frac{63.5375}{2.2350} \\approx 28.4284 \\text{ years}$$
- **Variance of Age at Childbearing ($\\sigma^2$)**:
  $$\\sigma^2 = \\frac{R_2}{R_0} - T^2 = \\frac{1{,}891.46875}{2.2350} - (28.4284)^2 = 846.2947 - 808.1740 = 38.1207 \\text{ years}^2$$
  The standard deviation is $\\sigma = \\sqrt{38.1207} \\approx 6.17$ years.

### Solution, step 2: Lotka Analytical Approximations for $r$
1. **First-Order Approximation ($r_1$)**:
   $$\\ln(NRR) = \\ln(2.2350) = 0.804234$$
   $$r_1 = \\frac{\\ln(NRR)}{T} = \\frac{0.804234}{28.4284} \\approx 0.028290 \\implies 2.829\\% \\text{ per annum}$$

2. **Second-Order Lotka Correction ($r_2$)**:
   Recall: $\\ln(NRR) = r T - \\frac{1}{2} r^2 \\sigma^2$.
   $$0.804234 = 28.4284 \\, r - \\frac{1}{2} (38.1207) \\, r^2$$
   $$19.06035 \\, r^2 - 28.4284 \\, r + 0.804234 = 0$$
   Applying the quadratic formula:
   $$r = \\frac{28.4284 - \\sqrt{(28.4284)^2 - 4 \\times 19.06035 \\times 0.804234}}{2 \\times 19.06035}$$
   $$(28.4284)^2 = 808.1740$$
   $$4 \\times 19.06035 \\times 0.804234 = 61.3160$$
   $$\\text{Discriminant} = 808.1740 - 61.3160 = 746.8580$$
   $$\\sqrt{746.8580} \\approx 27.3287$$
   $$r_2 = \\frac{28.4284 - 27.3287}{38.1207} = \\frac{1.0997}{38.1207} \\approx 0.028848 \\implies 2.885\\% \\text{ per annum}$$

### Solution, step 3: Newton–Raphson Numerical Root Finding
The exact discrete characteristic function is:
$$f(r) = 5 \\sum_{i=1}^7 e^{-r x_m} {_5 \\phi_x} - 1 = 0$$
The derivative with respect to $r$ is:
$$f'(r) = -5 \\sum_{i=1}^7 x_m \\, e^{-r x_m} {_5 \\phi_x}$$

Let initial seed be $r^{(0)} = 0.0288$.
We evaluate $f(0.0288)$ and $f'(0.0288)$ across all intervals:
- $i=1 (17.5)$: $e^{-0.0288 \\times 17.5} = e^{-0.504} = 0.60411$. Term: $5 \\times 0.03 \\times 0.60411 = 0.09062$. Deriv: $-17.5 \\times 0.09062 = -1.5858$
- $i=2 (22.5)$: $e^{-0.0288 \\times 22.5} = e^{-0.648} = 0.52309$. Term: $5 \\times 0.11 \\times 0.52309 = 0.28770$. Deriv: $-22.5 \\times 0.28770 = -6.4732$
- $i=3 (27.5)$: $e^{-0.0288 \\times 27.5} = e^{-0.792} = 0.45294$. Term: $5 \\times 0.14 \\times 0.45294 = 0.31706$. Deriv: $-27.5 \\times 0.31706 = -8.7191$
- $i=4 (32.5)$: $e^{-0.0288 \\times 32.5} = e^{-0.936} = 0.39219$. Term: $5 \\times 0.10 \\times 0.39219 = 0.19609$. Deriv: $-32.5 \\times 0.19609 = -6.3731$
- $i=5 (37.5)$: $e^{-0.0288 \\times 37.5} = e^{-1.080} = 0.33960$. Term: $5 \\times 0.05 \\times 0.33960 = 0.08490$. Deriv: $-37.5 \\times 0.08490 = -3.1837$
- $i=6 (42.5)$: $e^{-0.0288 \\times 42.5} = e^{-1.224} = 0.29405$. Term: $5 \\times 0.015 \\times 0.29405 = 0.02205$. Deriv: $-42.5 \\times 0.02205 = -0.9373$
- $i=7 (47.5)$: $e^{-0.0288 \\times 47.5} = e^{-1.368} = 0.25462$. Term: $5 \\times 0.002 \\times 0.25462 = 0.00255$. Deriv: $-47.5 \\times 0.00255 = -0.1210$

Summing terms:
$$\\sum = 0.09062 + 0.28770 + 0.31706 + 0.19609 + 0.08490 + 0.02205 + 0.00255 = 1.00097$$
$$f(0.0288) = 1.00097 - 1 = +0.00097$$

Summing derivative terms:
$$f'(0.0288) = -(1.5858 + 6.4732 + 8.7191 + 6.3731 + 3.1837 + 0.9373 + 0.1210) = -27.3932$$

Newton–Raphson step:
$$r^{(1)} = r^{(0)} - \\frac{f(r^{(0)})}{f'(r^{(0)})} = 0.0288 - \\frac{0.00097}{-27.3932} = 0.0288 + 0.0000354 = 0.028835$$

The exact intrinsic rate of natural increase is:

$$r^* = 0.028835 \\implies 2.884\\% \\text{ per annum}$$

Notice how the second-order Lotka approximation ($r_2 = 0.028848$) matched the exact numerical root to within $0.001\\%$, while the simple first-order rate ($r_1 = 0.028290$) was biased downward by over half a percentage point due to ignoring the dispersion of childbearing ages.

## Fully worked question 2: Stable Age Distribution and Intrinsic Birth Rate Computation

### Question
A mathematical demographer models a growing stable population with intrinsic rate of natural increase $r = 0.020$ ($2.0\\%$ per year). The survival schedule $p(x) = l(x)/l_0$ across ten-year life spans is evaluated as follows:

| Age Interval $[x, x+10)$ | Interval Midpoint ($x_m$) | Survival Probability to Midpoint ($p(x_m)$) |
| :---: | :---: | :---: |
| **0–10** | $5.0$ | $0.9600$ |
| **10–20** | $15.0$ | $0.9400$ |
| **20–30** | $25.0$ | $0.9100$ |
| **30–40** | $35.0$ | $0.8700$ |
| **40–50** | $45.0$ | $0.8100$ |
| **50–60** | $55.0$ | $0.7200$ |
| **60–70** | $65.0$ | $0.5800$ |
| **70+** | $75.0$ (effective) | $0.3200$ |

1. Compute the discounted survival weight $w(x_m) = e^{-r x_m} \\cdot p(x_m)$ for each age interval.
2. Calculate the Intrinsic Birth Rate $b$ and the Intrinsic Death Rate $d$ per $1{,}000$ population.
3. Determine the percentage age distribution $c(x)$ of the stable population and compare it with the stationary age distribution ($r = 0$).

### Solution, step 1: Calculate Discounted Survival Weights
With $r = 0.020$, the discounting factor is $e^{-0.020 x_m}$:

1. **Ages 0–10 ($x_m = 5.0$)**:
   $$e^{-0.020 \\times 5.0} = e^{-0.100} = 0.904837$$
   $$w_1 = 0.904837 \\times 0.9600 = 0.868644$$
2. **Ages 10–20 ($x_m = 15.0$)**:
   $$e^{-0.020 \\times 15.0} = e^{-0.300} = 0.740818$$
   $$w_2 = 0.740818 \\times 0.9400 = 0.696369$$
3. **Ages 20–30 ($x_m = 25.0$)**:
   $$e^{-0.020 \\times 25.0} = e^{-0.500} = 0.606531$$
   $$w_3 = 0.606531 \\times 0.9100 = 0.551943$$
4. **Ages 30–40 ($x_m = 35.0$)**:
   $$e^{-0.020 \\times 35.0} = e^{-0.700} = 0.496585$$
   $$w_4 = 0.496585 \\times 0.8700 = 0.432029$$
5. **Ages 40–50 ($x_m = 45.0$)**:
   $$e^{-0.020 \\times 45.0} = e^{-0.900} = 0.406570$$
   $$w_5 = 0.406570 \\times 0.8100 = 0.329321$$
6. **Ages 50–60 ($x_m = 55.0$)**:
   $$e^{-0.020 \\times 55.0} = e^{-1.100} = 0.332871$$
   $$w_6 = 0.332871 \\times 0.7200 = 0.239667$$
7. **Ages 60–70 ($x_m = 65.0$)**:
   $$e^{-0.020 \\times 65.0} = e^{-1.300} = 0.272532$$
   $$w_7 = 0.272532 \\times 0.5800 = 0.158068$$
8. **Ages 70+ ($x_m = 75.0$)**:
   $$e^{-0.020 \\times 75.0} = e^{-1.500} = 0.223130$$
   $$w_8 = 0.223130 \\times 0.3200 = 0.071402$$

Sum of weights across all intervals:
$$\\sum w = 0.868644 + 0.696369 + 0.551943 + 0.432029 + 0.329321 + 0.239667 + 0.158068 + 0.071402 = 3.347443$$

Each interval spans $n = 10$ years. The integral approximation is:
$$\\int_0^{\\infty} e^{-r x} p(x) \\, dx = 10 \\times \\sum w = 10 \\times 3.347443 = 33.47443$$

### Solution, step 2: Calculate Intrinsic Birth and Death Rates
The Intrinsic Birth Rate is:

$$b = \\frac{1}{\\int_0^{\\infty} e^{-r x} p(x) \\, dx} = \\frac{1}{33.47443} \\approx 0.029874 \\implies 29.87 \\text{ per 1,000}$$

The Intrinsic Death Rate is:

$$d = b - r = 0.029874 - 0.020000 = 0.009874 \\implies 9.87 \\text{ per 1,000}$$

Notice the consistency: $b - d = 29.87 - 9.87 = 20.00 \\text{ per 1,000} = 2.0\\% = r$.

### Solution, step 3: Determine Stable Age Distribution and Compare with Stationary
The percentage in each ten-year interval is:
$$c_i = \\frac{w_i}{\\sum w} \\times 100$$
For comparison, the stationary percentage ($r = 0$) is based on unweighted survival $p(x_m)$:
$$\\sum p = 0.96 + 0.94 + 0.91 + 0.87 + 0.81 + 0.72 + 0.58 + 0.32 = 6.11$$
$$c_i^{\\text{stat}} = \\frac{p(x_m)}{\\sum p} \\times 100$$

Comparing the two distributions:
- **Ages 0–10**:
  - Stable ($r = 2\\%$): $\\frac{0.868644}{3.347443} \\times 100 = 25.95\\%$
  - Stationary ($r = 0$): $\\frac{0.96}{6.11} \\times 100 = 15.71\\%$
  *(Children under 10 constitute $26\\%$ of the growing stable population compared to only $16\\%$ in the stationary state!)*
- **Ages 10–20**:
  - Stable: $\\frac{0.696369}{3.347443} \\times 100 = 20.80\\%$
  - Stationary: $\\frac{0.94}{6.11} \\times 100 = 15.38\\%$
- **Ages 20–30**:
  - Stable: $\\frac{0.551943}{3.347443} \\times 100 = 16.49\\%$
  - Stationary: $\\frac{0.91}{6.11} \\times 100 = 14.89\\%$
- **Ages 30–40**:
  - Stable: $\\frac{0.432029}{3.347443} \\times 100 = 12.91\\%$
  - Stationary: $\\frac{0.87}{6.11} \\times 100 = 14.24\\%$
- **Ages 40–50**:
  - Stable: $\\frac{0.329321}{3.347443} \\times 100 = 9.84\\%$
  - Stationary: $\\frac{0.81}{6.11} \\times 100 = 13.26\\%$
- **Ages 50–60**:
  - Stable: $\\frac{0.239667}{3.347443} \\times 100 = 7.16\\%$
  - Stationary: $\\frac{0.72}{6.11} \\times 100 = 11.78\\%$
- **Ages 60–70**:
  - Stable: $\\frac{0.158068}{3.347443} \\times 100 = 4.72\\%$
  - Stationary: $\\frac{0.58}{6.11} \\times 100 = 9.49\\%$
- **Ages 70+**:
  - Stable: $\\frac{0.071402}{3.347443} \\times 100 = 2.13\\%$
  - Stationary: $\\frac{0.32}{6.11} \\times 100 = 5.24\\%$

**Demographic Insight**:
Exponential growth ($r = 2\\%$) drastically rejuvenates the age distribution: youth under age 20 comprise $46.75\\%$ of the growing stable population, compared to only $31.09\\%$ in the stationary population. Senior citizens aged 60 and over comprise only $6.85\\%$ of the growing population, compared to $14.73\\%$ in the stationary state. Rapid growth dilutes the elderly proportion.

## Fully worked question 3: Keyfitz Demographic Momentum Formulation and Post-Replacement Equilibrium

### Question
A high-fertility developing country with an expanding stable population experiences an abrupt, instantaneous fertility drop to exact replacement level ($NRR = 1.000$). Nathan Keyfitz (1971) derived the celebrated formula for the resulting **Demographic Momentum factor ($M$)**—the ratio of the ultimate stationary population size $N_{\\infty}$ to the population size at the moment fertility drops $N(0)$:

$$M = \\frac{b \\cdot e_0}{r \\cdot T} \\left( \\frac{NRR - 1}{NRR} \\right)$$

where:
- Intrinsic Birth Rate prior to fertility drop: $b = 0.0350$ (35.0 per 1,000)
- Intrinsic Rate of Natural Increase prior to drop: $r = 0.0250$ (2.5% per year)
- Life Expectancy at Birth: $e_0 = 65.0 \\text{ years}$
- Mean Length of Generation: $T = 28.0 \\text{ years}$
- Pre-drop Net Reproduction Rate: $NRR = 2.0138$
- Population size at the instant fertility drops: $N(0) = 100{,}000{,}000$ inhabitants

1. Compute the Keyfitz momentum factor $M$.
2. Calculate the ultimate stationary population size $N_{\\infty}$ and the absolute population growth that will occur solely due to age-structural inertia.
3. Explain why the population continues to expand substantially for fifty years after individual women reduce their fertility to the two-child replacement level.

### Solution, step 1: Compute the Keyfitz Momentum Factor
Using Keyfitz's analytical formula:

$$M = \\frac{b \\cdot e_0}{r \\cdot T} \\left( \\frac{NRR - 1}{NRR} \\right)$$

We evaluate each component term:
1. Numerator product:
   $$b \\cdot e_0 = 0.0350 \\times 65.0 = 2.2750$$
2. Denominator product:
   $$r \\cdot T = 0.0250 \\times 28.0 = 0.7000$$
3. First ratio:
   $$\\frac{b \\cdot e_0}{r \\cdot T} = \\frac{2.2750}{0.7000} = 3.2500$$
4. Replacement factor:
   $$\\frac{NRR - 1}{NRR} = \\frac{2.0138 - 1}{2.0138} = \\frac{1.0138}{2.0138} \\approx 0.503426$$

Multiplying the two terms:

$$M = 3.2500 \\times 0.503426 \\approx 1.636136 \\implies 1.6361$$

The Keyfitz demographic momentum factor is $M = 1.6361$.

### Solution, step 2: Calculate Ultimate Population and Absolute Growth
The baseline population when replacement fertility is attained is $N(0) = 100{,}000{,}000$.
The ultimate stationary population size is:

$$N_{\\infty} = M \\times N(0) = 1.636136 \\times 100{,}000{,}000 = 163{,}613{,}600 \\approx 163.61 \\text{ million}$$

The absolute expansion resulting strictly from demographic momentum is:

$$\\Delta N_{\\text{momentum}} = N_{\\infty} - N(0) = 163{,}613{,}600 - 100{,}000{,}000 = 63{,}613{,}600$$

The population will expand by an additional **$63.61$ million people** ($+63.6\\%$) after replacement fertility is achieved!

### Solution, step 3: Demographic Mechanism of Population Momentum
Why does a population grow by $63.6\\%$ after every mother reduces her family size to replacement level ($NRR = 1$)?

The phenomenon of demographic momentum is driven entirely by **age-structural memory**:
1. Prior to the fertility drop, the high growth rate ($r = 2.5\\%$) produced massive successive birth cohorts, creating an extraordinarily wide base in the population pyramid (over $45\\%$ of the population is under age 15).
2. Even when the fertility rate drops immediately to two children per woman, these massive childhood cohorts continue to march upward through the age pyramid into their prime childbearing years ($20-35$).
3. Although each individual woman bears only replacement-level offspring, the sheer **number of women in reproductive age** is so immense that total annual births continue to heavily outnumber annual deaths for several decades ($B(t) > D(t)$).
4. Only when these large transitional cohorts pass completely through their reproductive years and into old age (approximately 50 to 70 years after the initial fertility drop) does the age structure settle into the stationary profile where annual births finally balance annual deaths.
5. This profound result demonstrates why population policies must act decades in advance: halting population growth cannot be achieved instantly even through the most radical fertility reductions.
"""

(OUT_DIR / "unit-7.md").write_text(u7_content, encoding="utf-8")
print(f"Unit 7: {prose_count(u7_content)} words")
