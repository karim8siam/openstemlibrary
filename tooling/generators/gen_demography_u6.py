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

# Expand Unit 5 first
u5 = (OUT_DIR / "unit-5.md").read_text(encoding="utf-8")
u5_extra = """
### Tempo vs Quantum of Fertility and the Bongaarts–Feeney Adjustment
A profound methodological challenge in modern fertility analysis is the distinction between the **quantum** of fertility (the total number of children a woman bears over her lifetime) and the **tempo** of fertility (the chronological timing and age distribution of childbearing).

In the 1960s, Norman B. Ryder demonstrated that period fertility measures such as the annual Total Fertility Rate ($TFR$) are subject to severe **tempo distortions**. When successive cohorts of women postpone childbearing to older ages (e.g., due to rising female university enrollment and labor force participation), the mean age of childbearing shifts upward ($d\\mu / dt > 0$). During the transitional period of postponement, annual births are delayed into future calendar years, causing the observed period $TFR$ to temporarily plunge far below the actual completed lifetime family size of the women! Conversely, if women accelerate childbearing to younger ages (as occurred during the 1950s post-war baby boom), annual births from multiple cohorts are compressed into the same calendar years, artificially inflating the period $TFR$.

In 1998, John Bongaarts and Griffith Feeney formulated an elegant mathematical adjustment to remove tempo distortions from period fertility. Let $TFR(t)$ be the observed period Total Fertility Rate in calendar year $t$. Let $\\mu_i(t)$ denote the mean age of mothers at the birth of order $i$ (first births, second births, etc.), and let $r_i(t) = \\frac{d\\mu_i(t)}{dt}$ denote the annual rate of change in the mean age of childbearing for birth order $i$.

Bongaarts and Feeney proved that the tempo-free, quantum-adjusted Total Fertility Rate for birth order $i$, denoted by $TFR_i^*(t)$, is:

$$TFR_i^*(t) = \\frac{TFR_i(t)}{1 - r_i(t)}$$

Summing across all birth orders yields the total adjusted fertility:

$$TFR^*(t) = \\sum_{i} \\frac{TFR_i(t)}{1 - r_i(t)}$$

If the mean age of childbearing increases by $0.10$ years annually ($r_i = 0.10$), the observed period rate captures only $1 - 0.10 = 90\\%$ of the cohort's true quantum. An observed $TFR$ of $1.50$ actually corresponds to a tempo-adjusted rate of:

$$TFR^* = \\frac{1.50}{1 - 0.10} = \\frac{1.50}{0.90} \\approx 1.67$$

Understanding the Bongaarts-Feeney tempo adjustment prevents policymakers from confusing temporary postponement of motherhood with permanent childlessness.

### Parity Progression Ratios (PPR) and Life Table Parity Analysis
While the Total Fertility Rate sums birth rates across maternal ages, it treats every childbearing event independently of how many children the woman has previously borne. In parity-specific demographic analysis, demographers model childbearing as a sequential stochastic process through **Parity Progression Ratios ($PPR$)**.

Let $p_i$ denote the Parity Progression Ratio from parity $i$ to parity $i+1$. It represents the conditional probability that a woman who has already given birth to $i$ live children will eventually advance to bear at least one more child ($i+1$):

$$p_i = \\mathbb{P}(\\text{Gives birth to child } i+1 \\mid \\text{Has already borne } i \\text{ children})$$

By convention:
- $p_0$ is the probability that a childless woman has at least one child (the complement $1 - p_0$ represents permanent childlessness).
- $p_1$ is the probability that a mother of one child progresses to have a second child.
- $p_2$ is the probability that a two-child family expands to three children (the critical two-child stop-rule threshold).

The Total Fertility Rate can be expressed directly as a geometric series of parity progression ratios:

$$TFR = p_0 + p_0 p_1 + p_0 p_1 p_2 + p_0 p_1 p_2 p_3 + \\dots = \\sum_{k=0}^{\\infty} \\prod_{j=0}^k p_j$$

In societies where $p_0$ and $p_1$ remain high ($>0.85$) while $p_2$ collapses ($<0.25$), fertility decline is driven strictly by stopping behavior at the two-child norm rather than generalized childlessness.
"""

u5 = u5.replace("## Fully worked question 2", u5_extra + "\n## Fully worked question 2")
(OUT_DIR / "unit-5.md").write_text(u5, encoding="utf-8")
print(f"Updated Unit 5: {prose_count(u5)} words")

# ==============================================================================
# UNIT 6: Mathematical Models of Population Growth
# ==============================================================================
u6_content = """# Unit 6: Mathematical Models of Population Growth

Mathematical modeling of population growth is among the oldest and most intellectually rich branches of applied mathematics, dating back to Leonardo of Pisa (Fibonacci) in 1202, Thomas Robert Malthus in 1798, and Pierre-François Verhulst in 1838. In demography, mathematical growth models serve two distinct purposes: **deductive analytical modeling** (deriving the logical trajectory of population size and structural composition under explicit biological postulates) and **empirical graduation** (fitting functional curves to historical census series to enable intercensal interpolation and medium-term demographic forecasting). In this unit, we formalize the mathematics of discrete arithmetic, geometric, continuous exponential, and Verhulst-Pearl logistic growth models.

## 6.1 Discrete Linear and Arithmetic Growth Models

The simplest mathematical formulation of population growth assumes that a population expands by a constant, absolute number of individuals in each successive temporal unit.

### Mathematical Formulation
Let $P(t)$ denote the population size at time $t$, and let $P(0) = P_0$ denote the baseline population at time $t = 0$. The **Arithmetic (Linear) Growth Model** postulates a constant absolute annual increment $b$:

$$\\frac{dP(t)}{dt} = b = \\text{constant}$$

Integrating from $0$ to $t$:

$$P(t) = P_0 + b \\cdot t$$

Given two census enumerations at times $t_1$ and $t_2$ ($t_2 > t_1$) with counts $P(t_1)$ and $P(t_2)$, the average annual absolute increment is:

$$b = \\frac{P(t_2) - P(t_1)}{t_2 - t_1}$$

The arithmetic growth rate expressed as a percentage of the baseline population is:

$$r_{\\text{arithmetic}} = \\frac{b}{P_0} = \\frac{P(t_2) - P(t_1)}{P(t_1) \\cdot (t_2 - t_1)}$$

### Demographic Limitations of the Arithmetic Model
While arithmetic models are mathematically trivial and computationally convenient for short-term linear interpolation between closely spaced censuses (e.g., estimating population on July 1 of an intercensal year), they are demographically unrealistic for long-term modeling:
1. **Biological Implausibility**: Population growth is inherently biological: people produce offspring in proportion to their numbers. A constant absolute increment $b$ implies that as the population grows larger, each individual's average contribution to growth declines continuously ($b / P(t) \\to 0$).
2. **Failure of Compounding**: The arithmetic model ignores the fundamental demographic reality that newborn individuals mature into parents who produce further offspring (the demographic multiplier effect).

## 6.2 Geometric Compounding Growth Models

Recognizing the multiplicative nature of biological reproduction, the geometric growth model incorporates discrete annual compounding, analogous to compound interest in financial mathematics.

### Mathematical Formulation
Assume that the population expands at a constant proportional rate $r_g$ per calendar year, compounded once at the conclusion of each annual cycle:

$$P(t) = P_0 (1 + r_g)^t$$

Given two historical censuses separated by $t$ years:

$$(1 + r_g)^t = \\frac{P(t)}{P_0}$$

Taking the $t$-th root:

$$1 + r_g = \\left( \\frac{P(t)}{P_0} \\right)^{1/t}$$

Solving for the **Geometric Annual Growth Rate ($r_g$)**:

$$r_g = \\left( \\frac{P(t)}{P_0} \\right)^{1/t} - 1$$

Expressed as a percentage:

$$r_g(\\%) = \\left[ \\left( \\frac{P(t)}{P_0} \\right)^{1/t} - 1 \\right] \\times 100$$

### Intercensal Interpolation under Geometric Growth
For any fractional time $t^* \\in (t_1, t_2)$, the intercensal population is interpolated via:

$$P(t^*) = P(t_1) \\left( \\frac{P(t_2)}{P(t_1)} \\right)^{\\frac{t^* - t_1}{t_2 - t_1}}$$

Geometric compounding is widely utilized by national statistical bureaus for decennial census interpolation when vital events are published at discrete annual intervals.

## 6.3 Continuous Exponential Growth Models and Doubling Time

In biological reality, human births and deaths occur continuously around the clock every second of the day, rather than in discrete annual bursts. The continuous exponential growth model formalizes this continuous instantaneous compounding.

### The Differential Equation of Exponential Growth
Let the rate of change of population size be directly proportional to the current population size:

$$\\frac{dP(t)}{dt} = r \\cdot P(t)$$

where $r$ represents the **intrinsic instantaneous rate of natural increase** (the Malthusian parameter).
Separating variables:

$$\\frac{1}{P(t)} \\, dP = r \\, dt$$

Integrating both sides from $t = 0$ (where $P(0) = P_0$) to time $t$:

$$\\int_{P_0}^{P(t)} \\frac{1}{P} \\, dP = \\int_0^t r \\, dt$$

$$\\ln\\left( \\frac{P(t)}{P_0} \\right) = r \\cdot t$$

Exponentiating both sides yields the classical **Continuous Exponential Growth Model**:

$$P(t) = P_0 \\, e^{r t}$$

### Derivation of the Continuous Growth Rate
Given two census observations $P(t_1)$ and $P(t_2)$ separated by elapsed time $\\Delta t = t_2 - t_1$:

$$e^{r \\Delta t} = \\frac{P(t_2)}{P(t_1)}$$

Taking the natural logarithm:

$$r \\Delta t = \\ln\\left( \\frac{P(t_2)}{P(t_1)} \\right)$$

$$r = \\frac{\\ln[P(t_2) / P(t_1)]}{t_2 - t_1} = \\frac{\\ln P(t_2) - \\ln P(t_1)}{\\Delta t}$$

### Mathematical Derivation of Doubling Time ($T_d$)
The **Doubling Time ($T_d$)** is the precise time required for a population growing at constant exponential rate $r$ to double its initial size:

$$P(T_d) = 2 \\cdot P_0$$

Substitute this into the exponential equation:

$$P_0 \\, e^{r T_d} = 2 \\cdot P_0$$

Divide both sides by $P_0$:

$$e^{r T_d} = 2$$

Taking the natural logarithm:

$$r \\cdot T_d = \\ln(2) \\approx 0.693147$$

Solving for $T_d$:

$$T_d = \\frac{\\ln(2)}{r} = \\frac{0.693147}{r}$$

If the growth rate is expressed as an annual percentage $r(\\%) = 100 \\cdot r$:

$$T_d = \\frac{100 \\cdot \\ln(2)}{r(\\%)} = \\frac{69.31}{r(\\%)} \\approx \\frac{70}{r(\\%)}$$

This celebrated demographic approximation is known worldwide as the **Rule of 70**:
- A population growing at $r = 1.0\\%$ per annum doubles in approximately $70 / 1 = 70$ years.
- A population expanding at $r = 2.0\\%$ per annum doubles in $70 / 2 = 35$ years.
- At an explosive rate of $r = 3.5\\%$ per annum (frequently observed in mid-20th-century developing nations), the population doubles in just $70 / 3.5 = 20$ years!

## 6.4 The Verhulst–Pearl Logistic Growth Model

Unconstrained exponential growth cannot continue indefinitely in a finite physical environment. As Thomas Malthus recognized, human populations eventually encounter resource, ecological, and environmental constraints. In 1838, the Belgian mathematician Pierre-François Verhulst introduced the **Logistic Model**, which Raymond Pearl and Lowell J. Reed rediscovered and popularized in 1920.

### Differential Formulation of Logistic Growth
Verhulst postulated that the per capita growth rate is not constant, but declines linearly as population size $P(t)$ approaches an asymptotic ceiling—the **Carrying Capacity ($K$)**:

$$\\frac{1}{P} \\frac{dP}{dt} = r \\left( 1 - \\frac{P}{K} \\right)$$

Rearranging:

$$\\frac{dP}{dt} = r P \\left( \\frac{K - P}{K} \\right) = \\frac{r}{K} P (K - P)$$

where:
- $r > 0$ is the intrinsic rate of growth in the absence of density-dependent competition.
- $K > 0$ is the environmental carrying capacity (asymptote of the population).
- The term $\\left( 1 - \\frac{P}{K} \\right)$ represents the environmental resistance factor. When $P \\ll K$, environmental resistance is near zero, and the population grows quasi-exponentially. As $P \\to K$, environmental resistance approaches unity, halting growth.

### Analytical Solution of the Logistic Differential Equation
We solve the autonomous non-linear differential equation via separation of variables:

$$\\frac{dP}{P(K - P)} = \\frac{r}{K} \\, dt$$

Using partial fraction decomposition:

$$\\frac{1}{P(K - P)} = \\frac{1}{K} \\left[ \\frac{1}{P} + \\frac{1}{K - P} \\right]$$

Substitute this into the equation:

$$\\frac{1}{K} \\left[ \\frac{1}{P} + \\frac{1}{K - P} \\right] dP = \\frac{r}{K} \\, dt$$

Multiply both sides by $K$:

$$\\left[ \\frac{1}{P} + \\frac{1}{K - P} \\right] dP = r \\, dt$$

Integrate both sides:

$$\\int \\left( \\frac{1}{P} + \\frac{1}{K - P} \\right) dP = \\int r \\, dt$$

$$\\ln(P) - \\ln(K - P) = r t + C_0$$

$$\\ln\\left( \\frac{P}{K - P} \\right) = r t + C_0$$

Exponentiate both sides:

$$\\frac{P(t)}{K - P(t)} = C \\, e^{r t} \\quad \\text{where } C = e^{C_0}$$

At initial time $t = 0$:

$$\\frac{P_0}{K - P_0} = C$$

Let $\\beta = \\frac{1}{C} = \\frac{K - P_0}{P_0} = \\frac{K}{P_0} - 1$. Then:

$$\\frac{K - P(t)}{P(t)} = \\beta \\, e^{-r t}$$

$$\\frac{K}{P(t)} - 1 = \\beta \\, e^{-r t}$$

$$\\frac{K}{P(t)} = 1 + \\beta \\, e^{-r t}$$

Inverting yields the canonical **Verhulst–Pearl Logistic Growth Function**:

$$P(t) = \\frac{K}{1 + \\beta \\, e^{-r t}}$$

### Mathematical Properties of the Logistic S-Curve
1. **Asymptotes**:
   - As $t \\to -\\infty$: $P(t) \\to 0$.
   - As $t \\to +\\infty$: $P(t) \\to K$.
2. **Point of Inflection ($P^*$)**:
   The point of maximum absolute growth rate ($\frac{d^2 P}{dt^2} = 0$) is found by differentiating $\\frac{dP}{dt} = \\frac{r}{K} (K P - P^2)$:
   $$\\frac{d^2 P}{dt^2} = \\frac{r}{K} (K - 2P) \\frac{dP}{dt} = 0$$
   Since $\\frac{dP}{dt} > 0$, the inflection point occurs strictly when:
   $$K - 2P = 0 \\implies P^* = \\frac{K}{2}$$
   The population grows most rapidly in absolute numbers when it reaches **exactly half of its carrying capacity**.
3. **Time of Inflection ($t^*$)**:
   Setting $P(t^*) = K/2$:
   $$\\frac{K}{1 + \\beta e^{-r t^*}} = \\frac{K}{2} \\implies 1 + \\beta e^{-r t^*} = 2 \\implies \\beta e^{-r t^*} = 1$$
   $$e^{r t^*} = \\beta \\implies t^* = \\frac{\\ln \\beta}{r}$$
4. **Symmetry**: The logistic curve is strictly symmetric about its inflection point $(t^*, K/2)$.

## 6.5 Fitting the Logistic Curve: The Pearl–Reed Three-Point Method

To calibrate the three parameters of the logistic curve ($K, \\beta, r$) to historical census data, Raymond Pearl and Lowell Reed formulated the **Three-Point Method**.

### Mathematical Derivation of the Three-Point Formula
Select three equidistant census observations along the historical timeline:
- $P_0$ at time $t = 0$
- $P_1$ at time $t = h$
- $P_2$ at time $t = 2h$
where $h$ is the constant time interval between chosen censuses (e.g., $h = 20$ years).

The logistic equations at the three points are:
$$P_0 = \\frac{K}{1 + \\beta}$$
$$P_1 = \\frac{K}{1 + \\beta e^{-r h}}$$
$$P_2 = \\frac{K}{1 + \\beta e^{-2 r h}}$$

Invert each equation to isolate $\\frac{1}{P}$:
$$\\frac{1}{P_0} = \\frac{1 + \\beta}{K}$$
$$\\frac{1}{P_1} = \\frac{1 + \\beta e^{-r h}}{K}$$
$$\\frac{1}{P_2} = \\frac{1 + \\beta e^{-2 r h}}{K}$$

Let $u = e^{-r h}$. Taking differences between adjacent reciprocals:
$$\\Delta_1 = \\frac{1}{P_0} - \\frac{1}{P_1} = \\frac{\\beta (1 - u)}{K}$$
$$\\Delta_2 = \\frac{1}{P_1} - \\frac{1}{P_2} = \\frac{\\beta u (1 - u)}{K}$$

Dividing $\\Delta_2$ by $\\Delta_1$:
$$\\frac{\\Delta_2}{\\Delta_1} = \\frac{\\frac{1}{P_1} - \\frac{1}{P_2}}{\\frac{1}{P_0} - \\frac{1}{P_1}} = u = e^{-r h}$$

Since $u = e^{-r h}$, we solve directly for the growth parameter $r$:
$$r = -\\frac{1}{h} \\ln(u) = -\\frac{1}{h} \\ln\\left( \\frac{\\frac{1}{P_1} - \\frac{1}{P_2}}{\\frac{1}{P_0} - \\frac{1}{P_1}} \\right)$$

Once $u$ is known, Pearl and Reed established that the carrying capacity $K$ is given by:

$$K = \\frac{2 P_0 P_1 P_2 - P_1^2 (P_0 + P_2)}{P_0 P_2 - P_1^2}$$

Once $K$ is determined, $\\beta$ is computed directly from the initial condition:

$$\\beta = \\frac{K - P_0}{P_0}$$

This three-point algorithm provides an analytical solution that passes through all three benchmark census counts.

## Fully worked question 1: Comparative Growth Modeling: Arithmetic, Geometric, and Continuous Exponential

### Question
A national statistical bureau evaluates demographic expansion across a developing nation based on two decennial censuses:
- Census 1 (April 1, 2010): $P_{2010} = 40{,}000{,}000$ inhabitants
- Census 2 (April 1, 2020): $P_{2020} = 50{,}000{,}000$ inhabitants
The elapsed time between the two enumerations is exactly $\\Delta t = 10.0$ years.

1. Calculate the annual arithmetic absolute increment $b$ and the annual arithmetic growth rate $r_{\\text{arith}}$.
2. Calculate the discrete geometric annual compounding rate $r_{\\text{geom}}$ and the continuous exponential instantaneous rate $r_{\\text{cont}}$.
3. Project the national population to April 1, 2035 ($t = 25$ years from 2010) under all three growth regimes, and compute the continuous doubling time $T_d$.

### Solution, step 1: Arithmetic Growth Parameters
The elapsed time is $\\Delta t = 10.0$ years.
The absolute population increase over the decade is:
$$\\Delta P = P_{2020} - P_{2010} = 50{,}000{,}000 - 40{,}000{,}000 = 10{,}000{,}000$$

The average annual arithmetic increment is:
$$b = \\frac{\\Delta P}{\\Delta t} = \\frac{10{,}000{,}000}{10.0} = 1{,}000{,}000 \\text{ persons per year}$$

The arithmetic growth rate relative to the 2010 baseline is:
$$r_{\\text{arith}} = \\frac{b}{P_{2010}} \\times 100 = \\frac{1{,}000{,}000}{40{,}000{,}000} \\times 100 = 2.500\\% \\text{ per annum}$$

### Solution, step 2: Geometric and Continuous Growth Rates
1. **Geometric Compounding Rate ($r_{\\text{geom}}$)**:
   $$r_{\\text{geom}} = \\left( \\frac{P_{2020}}{P_{2010}} \\right)^{1/10} - 1 = \\left( \\frac{50{,}000{,}000}{40{,}000{,}000} \\right)^{0.10} - 1 = (1.25)^{0.10} - 1$$
   Computing $(1.25)^{0.10}$:
   $$\\ln(1.25) = 0.22314355$$
   $$0.10 \\times 0.22314355 = 0.022314355$$
   $$e^{0.022314355} \\approx 1.022565$$
   $$r_{\\text{geom}} = 1.022565 - 1 = 0.022565 \\implies 2.2565\\% \\text{ per annum}$$

2. **Continuous Exponential Rate ($r_{\\text{cont}}$)**:
   $$r_{\\text{cont}} = \\frac{\\ln(P_{2020} / P_{2010})}{\\Delta t} = \\frac{\\ln(1.25)}{10.0} = \\frac{0.22314355}{10.0} = 0.02231436 \\implies 2.2314\\% \\text{ per annum}$$

Notice the mathematical hierarchy of rates:
$$r_{\\text{cont}} (2.2314\\%) < r_{\\text{geom}} (2.2565\\%) < r_{\\text{arith}} (2.500\\%)$$
This hierarchy universally holds because continuous compounding generates the greatest compounding efficiency, requiring the smallest nominal rate to achieve the same decennial expansion.

### Solution, step 3: Demographic Projections to 2035 ($t = 25$ years) and Doubling Time
The elapsed time from the 2010 baseline to 2035 is $t = 25$ years.

1. **Under Arithmetic Growth**:
   $$P_{\\text{arith}}(25) = P_{2010} + 25 \\times b = 40{,}000{,}000 + 25 \\times 1{,}000{,}000 = 65{,}000{,}000$$

2. **Under Geometric Compounding Growth**:
   $$P_{\\text{geom}}(25) = P_{2010} (1 + r_{\\text{geom}})^{25} = 40{,}000{,}000 \\times (1.022565)^{25}$$
   $$(1.022565)^{25} = (1.25)^{2.5} = (1.25)^2 \\times \\sqrt{1.25} = 1.5625 \\times 1.118034 = 1.746928$$
   $$P_{\\text{geom}}(25) = 40{,}000{,}000 \\times 1.746928 = 69{,}877{,}123$$

3. **Under Continuous Exponential Growth**:
   $$P_{\\text{cont}}(25) = P_{2010} \\, e^{25 \\times 0.02231436} = 40{,}000{,}000 \\, e^{0.5578589} = 40{,}000{,}000 \\times 1.746928 = 69{,}877{,}123$$
   *(Geometric and continuous exponential compounding yield identical projections when evaluated from the same empirical endpoints).*

4. **Continuous Doubling Time ($T_d$)**:
   $$T_d = \\frac{\\ln(2)}{r_{\\text{cont}}} = \\frac{0.69314718}{0.02231436} \\approx 31.06 \\text{ years}$$

At the prevailing continuous growth rate of $2.23\\%$, the national population will double from $40$ million to $80$ million in approximately $31.1$ years (around the year 2041).

## Fully worked question 2: Pearl–Reed Three-Point Calibration of the Logistic Growth Function

### Question
An ecological demographer fits a Verhulst-Pearl logistic growth model to a municipal population series enumerated across three equidistant census intervals spaced $h = 20$ years apart:
- Year 1980 ($t = 0$): $P_0 = 100{,}000$ inhabitants
- Year 2000 ($t = 20$): $P_1 = 160{,}000$ inhabitants
- Year 2020 ($t = 40$): $P_2 = 220{,}000$ inhabitants

1. Apply the Pearl-Reed three-point algorithm to calculate the environmental carrying capacity $K$ of the municipality.
2. Determine the initial scaling parameter $\\beta$ and the intrinsic growth rate parameter $r$.
3. Formulate the complete mathematical logistic equation $P(t)$, determine the population and calendar year at the inflection point, and forecast the municipal population for Year 2040 ($t = 60$).

### Solution, step 1: Calculate the Carrying Capacity ($K$)
The Pearl-Reed formula for carrying capacity is:

$$K = \\frac{2 P_0 P_1 P_2 - P_1^2 (P_0 + P_2)}{P_0 P_2 - P_1^2}$$

We evaluate each term systematically:
1. First numerator term:
   $$2 P_0 P_1 P_2 = 2 \\times 100{,}000 \\times 160{,}000 \\times 220{,}000 = 7.04 \\times 10^{15}$$
2. Second numerator term:
   $$P_1^2 = (160{,}000)^2 = 2.56 \\times 10^{10}$$
   $$P_0 + P_2 = 100{,}000 + 220{,}000 = 320{,}000$$
   $$P_1^2 (P_0 + P_2) = 2.56 \\times 10^{10} \\times 320{,}000 = 8.192 \\times 10^{15}$$
3. Total numerator:
   $$\\text{Num} = 7.04 \\times 10^{15} - 8.192 \\times 10^{15} = -1.152 \\times 10^{15}$$
4. Denominator:
   $$P_0 P_2 = 100{,}000 \\times 220{,}000 = 2.20 \\times 10^{10}$$
   $$P_1^2 = (160{,}000)^2 = 2.56 \\times 10^{10}$$
   $$\\text{Denom} = P_0 P_2 - P_1^2 = 2.20 \\times 10^{10} - 2.56 \\times 10^{10} = -0.36 \\times 10^{10} = -3.60 \\times 10^9$$

Dividing numerator by denominator:

$$K = \\frac{-1.152 \\times 10^{15}}{-3.60 \\times 10^9} = \\frac{1.152 \\times 10^{15}}{3.60 \\times 10^9} = 320{,}000$$

The carrying capacity of the municipality is $K = 320{,}000$ inhabitants.

### Solution, step 2: Calculate Parameters $\\beta$ and $r$
1. **The Parameter $\\beta$**:
   $$\\beta = \\frac{K - P_0}{P_0} = \\frac{320{,}000 - 100{,}000}{100{,}000} = \\frac{220{,}000}{100{,}000} = 2.200$$

2. **The Intrinsic Growth Rate $r$**:
   We evaluate the reciprocal ratio $u = e^{-r h}$:
   $$\\frac{1}{P_0} = \\frac{1}{100{,}000} = 1.000 \\times 10^{-5}$$
   $$\\frac{1}{P_1} = \\frac{1}{160{,}000} = 0.625 \\times 10^{-5}$$
   $$\\frac{1}{P_2} = \\frac{1}{220{,}000} \\approx 0.454545 \\times 10^{-5}$$

   $$\\Delta_1 = \\frac{1}{P_0} - \\frac{1}{P_1} = (1.000 - 0.625) \\times 10^{-5} = 0.375 \\times 10^{-5}$$
   $$\\Delta_2 = \\frac{1}{P_1} - \\frac{1}{P_2} = (0.625 - 0.454545) \\times 10^{-5} = 0.170455 \\times 10^{-5}$$

   $$u = e^{-20 r} = \\frac{\\Delta_2}{\\Delta_1} = \\frac{0.170455 \\times 10^{-5}}{0.375 \\times 10^{-5}} \\approx 0.454547$$

   Taking the natural logarithm:
   $$\\ln(u) = \\ln(0.454547) = -0.788454$$
   $$-20 r = -0.788454 \\implies r = \\frac{0.788454}{20} = 0.039423 \\implies 3.942\\% \\text{ per annum}$$

### Solution, step 3: Complete Logistic Equation, Inflection Point, and 2040 Projection
1. **The Calibrated Logistic Model**:
   $$P(t) = \\frac{320{,}000}{1 + 2.200 \\, e^{-0.039423 \\, t}}$$
   where $t$ is years elapsed since 1980 ($t = \\text{Year} - 1980$).

2. **The Inflection Point**:
   - The population at the inflection point is exactly half the carrying capacity:
     $$P^* = \\frac{K}{2} = \\frac{320{,}000}{2} = 160{,}000 \\text{ inhabitants}$$
   - Notice that $P_1 = 160{,}000$ at Year 2000! Therefore, the inflection point occurred **exactly in the Year 2000** ($t^* = 20$).
   - Check via formula: $t^* = \\frac{\\ln \\beta}{r} = \\frac{\\ln(2.200)}{0.039423} = \\frac{0.788457}{0.039423} = 20.00 \\text{ years}$.
   At Year 2000, municipal growth reached its maximum velocity of:
   $$\\left( \\frac{dP}{dt} \\right)_{\\text{max}} = \\frac{r K}{4} = \\frac{0.039423 \\times 320{,}000}{4} = 3{,}153.8 \\text{ persons per year}$$

3. **Forecast for Year 2040 ($t = 60$)**:
   $$-0.039423 \\times 60 = -2.36538$$
   $$e^{-2.36538} = 0.093913$$
   $$1 + \\beta e^{-r t} = 1 + 2.200 \\times 0.093913 = 1 + 0.206609 = 1.206609$$
   $$P(60) = \\frac{320{,}000}{1.206609} \\approx 265{,}206 \\text{ inhabitants}$$

**Demographic Synthesis**:
Between 1980 and 2000, the municipal population expanded by $60{,}000$ inhabitants ($100k \\to 160k$). Between 2000 and 2020, growth slowed to $60{,}000$ ($160k \\to 220k$). Between 2020 and 2040, as density-dependent constraints intensify, growth decelerates further to $45{,}206$ ($220k \\to 265{,}206$), approaching the ultimate ceiling of $320{,}000$.

## Fully worked question 3: Carrying Capacity Sensitivity and Velocity Analysis in Logistic Growth

### Question
A regional planning authority models the growth of an industrial metropolis under ecological zoning limits. The urban population dynamics satisfy the differential logistic law:

$$\\frac{dP}{dt} = 0.05 \\, P \\left( 1 - \\frac{P}{2{,}000{,}000} \\right)$$

where $P(t)$ is population size and $t$ is measured in years. The metropolis currently has an enumerated population of $P(0) = 500{,}000$ inhabitants.

1. Identify the intrinsic growth rate $r$ and carrying capacity $K$. Calculate the current instantaneous rate of population growth in persons per year ($\frac{dP}{dt}$ at $P = 500{,}000$).
2. Determine the population size and calendar time at which the metropolis will experience its absolute peak growth velocity. Compute this maximum growth velocity.
3. Solve for the exact time $T_{90}$ required for the metropolitan population to reach $90\\%$ of its carrying capacity ($P = 1{,}800{,}000$).

### Solution, step 1: Model Identification and Current Growth Velocity
From the differential equation $\\frac{dP}{dt} = 0.05 P \\left( 1 - \\frac{P}{2{,}000{,}000} \\right)$:
- Intrinsic growth rate: $r = 0.05$ ($5.0\\%$ per annum)
- Environmental carrying capacity: $K = 2{,}000{,}000$ inhabitants

At current population $P(0) = 500{,}000$:
$$\\frac{dP}{dt} = 0.05 \\times 500{,}000 \\times \\left( 1 - \\frac{500{,}000}{2{,}000{,}000} \\right) = 25{,}000 \\times (1 - 0.25) = 25{,}000 \\times 0.75 = 18{,}750 \\text{ persons per year}$$

The current growth velocity is $18{,}750$ additional residents per year.

### Solution, step 2: Maximum Growth Velocity and Inflection Dynamics
By the fundamental theorem of logistic growth, the growth rate $\\frac{dP}{dt}$ is a quadratic function of $P$:
$$g(P) = r P - \\frac{r}{K} P^2$$
The vertex of this downward-opening parabola occurs at:
$$P^* = \\frac{K}{2} = \\frac{2{,}000{,}000}{2} = 1{,}000{,}000 \\text{ inhabitants}$$

The maximum growth velocity is:
$$\\left( \\frac{dP}{dt} \\right)_{\\text{max}} = \\frac{r K}{4} = \\frac{0.05 \\times 2{,}000{,}000}{4} = \\frac{100{,}000}{4} = 25{,}000 \\text{ persons per year}$$

To find the time $t^*$ when this maximum velocity is reached, we evaluate the logistic solution:
$$\\beta = \\frac{K - P_0}{P_0} = \\frac{2{,}000{,}000 - 500{,}000}{500{,}000} = \\frac{1{,}500{,}000}{500{,}000} = 3.0$$

Setting $P(t^*) = K/2 = 1{,}000{,}000$:
$$t^* = \\frac{\\ln \\beta}{r} = \\frac{\\ln(3.0)}{0.05} = \\frac{1.098612}{0.05} = 21.972 \\approx 21.97 \\text{ years}$$

The metropolis will experience its peak growth velocity in approximately $22.0$ years, expanding by $25{,}000$ residents annually.

### Solution, step 3: Time Required to Reach 90% of Carrying Capacity
We set $P(T_{90}) = 0.90 \\times K = 1{,}800{,}000$.
From the linear logit form of the logistic solution:
$$\\frac{K - P(t)}{P(t)} = \\beta \\, e^{-r t}$$

Substitute $P = 0.90 K$:
$$\\frac{K - 0.90 K}{0.90 K} = \\frac{0.10 K}{0.90 K} = \\frac{1}{9} = \\beta \\, e^{-r T_{90}}$$

Substitute $\\beta = 3.0$ and $r = 0.05$:
$$\\frac{1}{9} = 3.0 \\, e^{-0.05 T_{90}}$$
$$e^{-0.05 T_{90}} = \\frac{1}{27}$$
$$e^{0.05 T_{90}} = 27$$

Taking the natural logarithm:
$$0.05 \\, T_{90} = \\ln(27) = \\ln(3^3) = 3 \\cdot \\ln(3) = 3 \\times 1.098612 = 3.295837$$

Solving for $T_{90}$:
$$T_{90} = \\frac{3.295837}{0.05} = 65.9167 \\approx 65.92 \\text{ years}$$

**Planning Synthesis**:
The metropolis will reach $90\\%$ of its carrying capacity ($1.8$ million residents) in approximately $65.9$ years. Growth proceeds in three distinct phases:
1. Years 0 to 22: Accelerating growth, with annual increments expanding from $18{,}750$ to the peak of $25{,}000$.
2. Years 22 to 66: Decelerating growth, as land scarcity, traffic congestion, and zoning restrictions dampen per capita expansion.
3. Post Year 66: Asymptotic plateauing toward the carrying capacity limit of $2{,}000{,}000$.
"""

(OUT_DIR / "unit-6.md").write_text(u6_content, encoding="utf-8")
print(f"Unit 6: {prose_count(u6_content)} words")
