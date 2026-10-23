#!/usr/bin/env python3
"""
Generate Units 3 and 4 for Actuarial Statistics and Mathematical Demography.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-actuarial-statistics-and-mathematical-demography"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_3 = r"""# Unit 3: Survival Models, Life Tables & Parametric Mortality Laws

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
"""

unit_4 = r"""# Unit 4: Life Insurance Contracts & Actuarial Present Value Valuations

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
"""

(DRAFT_DIR / "unit-3.md").write_text(unit_3.strip() + "\n", encoding="utf-8")
print("Unit 3 written.")

(DRAFT_DIR / "unit-4.md").write_text(unit_4.strip() + "\n", encoding="utf-8")
print("Unit 4 written.")
