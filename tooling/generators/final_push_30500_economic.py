#!/usr/bin/env python3
"""
Final push to cross 30,500 pure prose words for Economic Statistics.
"""
import re
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-economic-statistics")

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

def inject_before_worked_questions(content, addition):
    marker = "## Worked Questions and Solutions"
    if marker in content:
        parts = content.split(marker)
        return parts[0] + addition + "\n" + marker + parts[1]
    else:
        return content + "\n" + addition

u3_add = """
---

## Fourier Flexible Form Detrending in Nonlinear Series

When long-term economic time series exhibit smooth, non-linear structural transitions that cannot be adequately captured by low-degree polynomials or rigid break dates, econometricians employ the **Fourier Flexible Form Detrending Approach** (A. Ronald Gallant, 1981; Walter Enders and Junsoo Lee, 2012).

### Mathematical Specification
The secular trend is specified as a linear combination of a deterministic polynomial drift and a finite trigonometric Fourier series:

$$T_t = \\alpha_0 + \\beta t + \\sum_{k=1}^{F} \\left[ \\gamma_k \\sin\\left( \\frac{2\\pi k t}{N} \\right) + \\delta_k \\cos\\left( \\frac{2\\pi k t}{N} \\right) \\right]$$

where:
- $N$ is the total sample size.
- $k$ represents the integer frequency of the oscillation ($k = 1, 2, \\dots$).
- $F$ is the maximum number of cumulative harmonic frequencies.

### Theoretical Advantages:
1. **Universal Approximation**: By the Stone-Weierstrass theorem, a Fourier series can approximate any arbitrary, smooth, continuous non-linear function to any desired degree of precision.
2. **Smooth Break Modeling**: Instead of imposing discontinuous, knife-edge dummy variable break dates (which often cause severe pre-test bias), low-frequency Fourier terms ($k = 1$ or $k = 2$) trace out smooth, gradual structural regime transitions across decades (such as post-war industrial reconstruction or gradual digital automation).
3. **Model Selection**: Econometricians select the optimal harmonic frequency $k^*$ by minimizing the Bayesian Information Criterion (BIC) or Akaike Information Criterion (AIC), providing a data-driven, non-parametric secular trend line that preserves degrees of freedom.
"""

u4_add = """
---

## The Beveridge-Nelson Trend-Cycle Decomposition

In macroeconomic time series analysis, Stephen Beveridge and Charles Nelson (1981) introduced a fundamental model-based decomposition that defines the secular trend of an integrated time series strictly in terms of long-horizon conditional expectations.

### 1. Conceptual Definition of the Beveridge-Nelson Trend
Consider a time series $Y_t$ that is stationary in first differences: $\\Delta Y_t = \\mu + \\epsilon_t + \\theta_1 \\epsilon_{t-1} + \\dots = \\mu + C(L) \\epsilon_t$, where $C(L) = \\sum_{j=0}^{\\infty} c_j L^j$ is an invertible moving-average lag polynomial with $c_0 = 1$.

Beveridge and Nelson defined the **Secular Trend ($T_t$)** at time $t$ as the long-horizon forecast of the level of the series, adjusted for the deterministic drift rate $\\mu$:

$$T_t = \\lim_{k \\to \\infty} \\left[ E_t(Y_{t+k}) - k \\mu \\right]$$

The trend represents the level the economic series would reach once all transient, self-reversing cyclical shocks have completely dissipated.

### 2. Derivation of the Trend and Cyclical Components
Decomposing the lag polynomial via the algebraic polynomial identity:
$$C(L) = C(1) + (1 - L) C^*(L)$$
where $C(1) = \\sum_{j=0}^{\\infty} c_j$ is the sum of moving average coefficients, and $c_j^* = -\\sum_{i=j+1}^{\\infty} c_i$.

Substituting into the first-differenced equation:
$$\\Delta Y_t = \\mu + C(1) \\epsilon_t + \\Delta C^*(L) \\epsilon_t$$

Integrating both sides:
$$Y_t = T_t + C_t$$
where:
- **The Beveridge-Nelson Trend**:
  $$T_t = T_{t-1} + \\mu + C(1) \\epsilon_t$$
  The secular trend evolves as a pure random walk with constant drift $\\mu$ and innovation shock variance $[C(1)]^2 \\sigma_\\epsilon^2$.
- **The Beveridge-Nelson Cycle**:
  $$C_t = C^*(L) \\epsilon_t = -\\sum_{j=0}^{\\infty} \\left( \\sum_{i=j+1}^{\\infty} c_i \\right) \\epsilon_{t-j}$$
  The cyclical component is a strictly covariance-stationary process.

A vital insight of the Beveridge-Nelson decomposition is that the trend innovation and the cyclical innovation are driven by the **exact same random shock $\\epsilon_t$**, meaning that economic shocks alter both the long-run permanent trend and the short-run business cycle simultaneously.
"""

u5_add = """
---

## Alternative Rank-Dependent Inequality Metrics: Mehran and Piesch Indices

While Corrado Gini's concentration coefficient weights the vertical distance between the 45-degree line and the Lorenz curve uniformly across the population, welfare economists often wish to place greater ethical sensitivity on disparities at specific locations along the income spectrum.
Farhad Mehran (1976) and Walter Piesch (1975) formulated alternative linear rank-dependent inequality metrics.

### 1. The Mehran Inequality Index ($M$)
The Mehran Index assigns declining linear weights to individuals based on their population rank, placing greater mathematical emphasis on income inequality among the poorest citizens:

$$M = 3 \\int_{0}^{1} (1 - p) [p - L(p)] dp$$

- In discrete population samples:
  $$M = 1 - \\frac{3}{n^2 \\mu} \\sum_{i=1}^{n} (n - i + 1)^2 y_{(i)}$$
- The Mehran index is particularly sensitive to changes in income at the bottom of the distribution: a transfer from an impoverished citizen to a middle-class citizen produces a larger numerical increase in $M$ than in the Gini coefficient.

### 2. The Piesch Inequality Index ($P$)
Conversely, the Piesch Index assigns increasing linear weights to population rank, focusing sensitivity on concentration at the top of the income distribution:

$$P = \\frac{3}{2} \\int_{0}^{1} p [p - L(p)] dp$$

- In discrete population samples:
  $$P = \\frac{3}{2 n^2 \\mu} \\sum_{i=1}^{n} i^2 y_{(i)} - \\frac{3n + 1}{4n}$$
- The Piesch index is sensitive to oligarchic wealth concentration and windfall executive earnings among the top percentiles.

By examining the triad of Gini, Mehran, and Piesch indices simultaneously, national statistical offices can ascertain whether rising national inequality is being driven primarily by falling wages at the bottom ($M$ rising fastest) or accelerating wealth accumulation at the top ($P$ rising fastest).
"""

u7_add = """
---

## Waste Input-Output (WIO) Modeling and the Circular Economy

In contemporary industrial ecology and environmental planning, the linear economic model of "take, make, dispose" is being replaced by the **Circular Economy**. To model the physical transformation of manufactured goods into post-consumer scrap, recycling, and secondary raw materials, Shinichiro Nakamura and Yasushi Kondo (2002) developed the **Waste Input-Output (WIO) Model**.

### Mathematical Architecture of the WIO System
The WIO table expands Leontief's economic matrix by appending physical waste treatment and recycling sectors:

$$\\begin{bmatrix}
X_I \\\\ X_W
\\end{bmatrix} = \\begin{bmatrix}
A_{I, I} & A_{I, W} \\\\
W_{W, I} & W_{W, W}
\\end{bmatrix} \\begin{bmatrix}
X_I \\\\ X_W
\\end{bmatrix} + \\begin{bmatrix}
F_I \\\\ W_F
\\end{bmatrix}$$

where:
- $X_I$ is the monetary output vector of standard industrial producing sectors ($n \\times 1$).
- $X_W$ is the physical output vector of waste management and recycling treatment facilities (e.g., metric tons of incinerated, shredded, or recycled plastics, metals, paper).
- $A_{I, I}$ is the conventional inter-industry technical coefficient matrix.
- $A_{I, W}$ represents the purchases of industrial goods and energy required by waste treatment plants per unit of waste processed.
- $W_{W, I}$ is the **Waste Generation Matrix**: each element $w_{kj}$ represents the physical mass of waste type $k$ generated per unit of gross industrial output in sector $j$.
- $W_F$ is the physical vector of municipal solid waste discarded directly by final household consumers.

Inverting the augmented block matrix enables environmental planners to calculate how changes in recycling mandates, consumer packaging taxes, or landfill disposal bans affect total industrial output, energy consumption, and circular resource recovery across national supply chains.
"""

u8_add = """
---

## Hedonic Property Pricing and Environmental Amenity Valuation

In environmental and urban economics, public goods such as clean atmospheric air, urban green canopy, quiet residential neighborhoods, and high-performing public schools do not trade in separate private markets. To quantify consumer valuation and willingness to pay for these non-market amenities, Sherwin Rosen (1974) formulated the **Hedonic Property Pricing Method**.

### 1. The Hedonic Price Function
Let $P_i$ denote the market sale price of residential property $i$. A house is viewed as a heterogeneous bundle of structural attributes $S_i$ (square footage, bedrooms, bathrooms, lot size), neighborhood socioeconomic characteristics $N_i$ (crime rates, school test scores), and environmental amenities $Z_i$ (ambient particulate pollution $\\text{PM}_{2.5}$, proximity to parks, highway traffic noise):

$$\\ln(P_i) = \\alpha_0 + \\sum_{j=1}^{s} \\beta_j S_{ij} + \\sum_{k=1}^{m} \\gamma_k N_{ik} + \\theta Z_i + u_i$$

The parameter $\\theta = \\frac{\\partial \\ln(P)}{\\partial Z}$ represents the percentage change in property value resulting from a one-unit change in environmental quality.
The **Marginal Implicit Price (Marginal Willingness to Pay, MWTP)** for amenity $Z$ is:

$$\\text{MWTP}_Z = \\frac{\\partial P}{\\partial Z} = \\theta \\times P_i$$

### 2. Capitalization and Welfare Evaluation
When a public infrastructure project or clean air regulation reduces local air pollution from $Z_0$ to $Z_1$:
- Housing values in the affected zone appreciate, a phenomenon known as **Amenity Capitalization**.
- Under the first-stage Rosen hedonic equilibrium, the aggregate capitalized property value increase across all $H$ affected homes provides an empirical measure of the societal welfare benefit:
  $$\\Delta W \\approx \\sum_{i=1}^{H} \\text{MWTP}_{Z, i} \\times \\Delta Z_i$$

By analyzing thousands of real estate mortgage and title transfer records via hedonic regression, economic statisticians supply court-tested cost-benefit valuations for environmental policy mandates and public infrastructure projects.
"""

final_additions = {
    3: u3_add,
    4: u4_add,
    5: u5_add,
    7: u7_add,
    8: u8_add,
}

for unit_num, add_text in final_additions.items():
    file_path = OUT_DIR / f"unit-{unit_num}.md"
    content = file_path.read_text(encoding="utf-8")
    new_content = inject_before_worked_questions(content, add_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Unit {unit_num} pushed: {prose_count(new_content)} words")
