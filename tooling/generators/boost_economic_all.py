#!/usr/bin/env python3
"""
Boost word counts across Units 1 through 8 of Economic Statistics to guarantee >= 30,000 pure prose words.
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

# ----------------------------------------------------
# UNIT 1 EXPANSIONS
# ----------------------------------------------------
u1_boost = """
---

## Modern Economic Index Number Theory: Divisia, Törnqvist, and Superlative Indices

While classical index number theory focused predominantly on fixed-basket aggregative formulations (Laspeyres and Paasche), twentieth-century mathematical economics established rigorous microeconomic and axiomatic foundations through the work of François Divisia (1925), Erwin Diewert (1976), and Leo Törnqvist (1936).

### 1. The Continuous Divisia Index
In 1925, the French mathematical economist François Divisia proposed a continuous-time formulation of price and quantity indices. Let $p_i(t)$ and $q_i(t)$ represent the continuous price and quantity trajectories of commodity $i$ at time $t$. The aggregate expenditure at time $t$ is:

$$E(t) = \\sum_{i=1}^{n} p_i(t) q_i(t)$$

Differentiating both sides with respect to continuous time $t$:

$$\\frac{dE(t)}{dt} = \\sum_{i=1}^{n} \\frac{dp_i(t)}{dt} q_i(t) + \\sum_{i=1}^{n} p_i(t) \\frac{dq_i(t)}{dt}$$

Dividing by total expenditure $E(t)$:

$$\\frac{1}{E(t)} \\frac{dE(t)}{dt} = \\sum_{i=1}^{n} \\left( \\frac{p_i(t) q_i(t)}{E(t)} \\right) \\frac{1}{p_i(t)} \\frac{dp_i(t)}{dt} + \\sum_{i=1}^{n} \\left( \\frac{p_i(t) q_i(t)}{E(t)} \\right) \\frac{1}{q_i(t)} \\frac{dq_i(t)}{dt}$$

Defining $w_i(t) = \\frac{p_i(t) q_i(t)}{E(t)}$ as the instantaneous expenditure share of commodity $i$, and noting that $\\frac{1}{x} \\frac{dx}{dt} = \\frac{d \\ln(x)}{dt}$, the proportional growth rate of nominal expenditure decomposes into the sum of the instantaneous growth rates of the aggregate price index $P(t)$ and quantity index $Q(t)$:

$$\\frac{d \\ln[E(t)]}{dt} = \\frac{d \\ln[P(t)]}{dt} + \\frac{d \\ln[Q(t)]}{dt}$$

where the continuous growth rate of the **Divisia Price Index** is defined as:

$$\\frac{d \\ln[P(t)]}{dt} = \\sum_{i=1}^{n} w_i(t) \\frac{d \\ln[p_i(t)]}{dt}$$

Integrating over a discrete calendar interval $[0, 1]$:

$$\\ln[P(1)] - \\ln[P(0)] = \\int_{0}^{1} \\sum_{i=1}^{n} w_i(t) \\frac{d \\ln[p_i(t)]}{dt} dt$$

The Divisia index possesses remarkable theoretical properties: it satisfies both the Time Reversal Test and the Factor Reversal Test continuously. However, because economic data are collected at discrete intervals rather than continuously, the line integral cannot be evaluated without discrete approximation.

### 2. The Törnqvist Discrete Approximation
To approximate the continuous Divisia line integral using discrete data, Finnish statistician Leo Törnqvist (1936) replaced the continuous expenditure shares with the arithmetic mean of the base and current period expenditure shares:

$$\\bar{w}_i = \\frac{w_{i,0} + w_{i,t}}{2}$$

Taking the exponential of the weighted sum of log price relatives yields the **Törnqvist Price Index**:

$$\\ln(P_T) = \\sum_{i=1}^{n} \\bar{w}_i \\ln\\left( \\frac{p_{i,t}}{p_{i,0}} \\right) = \\sum_{i=1}^{n} \\left( \\frac{w_{i,0} + w_{i,t}}{2} \\right) \\ln\\left( \\frac{p_{i,t}}{p_{i,0}} \\right)$$

$$P_T = \\prod_{i=1}^{n} \\left( \\frac{p_{i,t}}{p_{i,0}} \\right)^{\\frac{w_{i,0} + w_{i,t}}{2}}$$

The Törnqvist index is symmetric with respect to time, treats both periods symmetrically, and accommodates smooth consumer substitution between goods.

### 3. Diewert's Theory of Superlative Index Numbers
In a landmark 1976 paper, Canadian econometrician W. Erwin Diewert introduced the concept of **Superlative Index Numbers**. A price index formula is defined as superlative if it is exact for a flexible unit cost function—meaning a cost function that provides a second-order Taylor series approximation to an arbitrary, twice continuously differentiable aggregator function.

Diewert established two foundational theorems:
1. **Fisher's Ideal Index is Superlative**: Fisher's index $P_F = \\sqrt{P_L \\times P_P}$ is exact for the flexible Quadratic Mean of Order $r = 2$ unit cost function:
   $$C(p) = \\left( \\sum_{i=1}^{n} \\sum_{j=1}^{n} b_{ij} p_i^{1/2} p_j^{1/2} \\right)^{2}$$
2. **The Törnqvist Index is Superlative**: The Törnqvist index $P_T$ is exact for the flexible Translog (transcendental logarithmic) unit cost function:
   $$\\ln[C(p)] = \\alpha_0 + \\sum_{i=1}^{n} \\alpha_i \\ln(p_i) + \\frac{1}{2} \\sum_{i=1}^{n} \\sum_{j=1}^{n} \\gamma_{ij} \\ln(p_i) \\ln(p_j)$$

Because both Fisher's Ideal Index and the Törnqvist Index are superlative, they accommodate flexible substitution behavior among consumers as relative prices shift, eliminating upper-level substitution bias. In practical empirical applications, numerical values of $P_F$ and $P_T$ rarely differ by more than a fraction of a percent.

---

## Elementary Aggregate Indices and Chain Drift Dynamics

Before statistical agencies can compute weighted aggregative indices (like Laspeyres or Fisher), they must first compile thousands of price quotations for individual items within detailed product categories where quantity weights are unavailable. These initial aggregations are termed **Elementary Price Indices**.

### 1. Classical Elementary Formulations
Let $p_{i,0}$ and $p_{i,t}$ denote the price of item $i$ ($i = 1, \\dots, k$) in the base and current period within an unweighted elementary stratum.
- **The Dutot Index (Ratio of Arithmetic Averages)**:
  $$P_{\\text{Dutot}} = \\frac{\\frac{1}{k} \\sum_{i=1}^{k} p_{i,t}}{\\frac{1}{k} \\sum_{i=1}^{k} p_{i,0}} = \\frac{\\sum_{i=1}^{k} p_{i,t}}{\\sum_{i=1}^{k} p_{i,0}}$$
  The Dutot index is sensitive to units of measurement unless all items within the stratum are homogenous in physical specification.
- **The Carli Index (Arithmetic Average of Price Relatives)**:
  $$P_{\\text{Carli}} = \\frac{1}{k} \\sum_{i=1}^{k} \\left( \\frac{p_{i,t}}{p_{i,0}} \\right)$$
  The Carli index fails the Time Reversal Test: by Jensen's inequality for convex functions, the arithmetic mean of relatives and the arithmetic mean of inverted relatives satisfy:
  $$P_{\\text{Carli}}(0, t) \\times P_{\\text{Carli}}(t, 0) > 1$$
  The Carli index is systematically biased upward and has been largely banished from international statistical guidelines.
- **The Jevons Index (Geometric Mean of Price Relatives)**:
  $$P_{\\text{Jevons}} = \\left[ \\prod_{i=1}^{k} \\left( \\frac{p_{i,t}}{p_{i,0}} \\right) \\right]^{1/k} = \\frac{\\left[ \\prod_{i=1}^{k} p_{i,t} \\right]^{1/k}}{\\left[ \\prod_{i=1}^{k} p_{i,0} \\right]^{1/k}}$$
  The Jevons index satisfies both the Unit Test and the Time Reversal Test. Furthermore, it implicitly assumes that consumers maintain constant expenditure shares within the item category (unitary elasticity of substitution, $\\sigma = 1$). For these reasons, the Jevons index is recommended by the international Consumer Price Index Manual as the preferred elementary aggregator.

### 2. High-Frequency Scanner Data and Chain Drift
In modern digital statistical systems, statistical offices increasingly ingest massive scanner barcode datasets and web-scraped daily transactions. To maintain timely product coverage, analysts frequently chain high-frequency monthly or weekly indices.

However, chaining indices under high-frequency sales promotions and seasonal restocking produces the phenomenon of **Chain Drift**. If retail prices fluctuate cyclically due to weekend promotions (dropping by 20% on sale and rebounding by 25% on Monday), while consumers purchase heavily at the discount price and abstain at regular price, chaining standard formulas generates a cumulative index that drifts systematically away from the true fixed-base price level. Resolving chain drift requires deploying multilateral index number methods, such as the **GEKS (Gini-Eltetö-Köves-Szulc)** or **Rolling Year GEKS** algorithms.
"""

# ----------------------------------------------------
# UNIT 2 EXPANSIONS
# ----------------------------------------------------
u2_boost = """
---

## Axiomatic Incompatibility: Wald's Impossibility Theorem

A central preoccupation of mathematical index number theory throughout the twentieth century was the pursuit of an index formula satisfying all desirable axiomatic criteria simultaneously. Irving Fisher famously tested dozens of formulas against his battery of tests. However, in 1937, the mathematical statistician Abraham Wald established a foundational negative result: **Wald's Inconsistency Theorem**.

### Statement and Proof of Wald's Incompatibility Theorem
Wald demonstrated that no single index number formula $P(p_0, p_t, q_0, q_t)$ can simultaneously satisfy:
1. **The Time Reversal Test**: $P(p_0, p_t, q_0, q_t) \\times P(p_t, p_0, q_t, q_0) = 1$.
2. **The Factor Reversal Test**: $P(p_0, p_t, q_0, q_t) \\times Q(p_0, p_t, q_0, q_t) = \\frac{p_t^T q_t}{p_0^T q_0}$.
3. **The Circular (Transitivity) Test**: $P(p_0, p_r, q_0, q_r) \\times P(p_r, p_t, q_r, q_t) = P(p_0, p_t, q_0, q_t)$ for any intermediate period $r$.

The proof proceeds by examining the functional dependence of the index on quantities. To satisfy the Circular Test across all possible price paths, the weights attached to prices in period $r$ must not depend on the specific baseline period $0$ or current period $t$. Consequently, an index satisfying circularity must take the general form of a ratio of fixed-weight linear combinations:
$$P(0, t) = \\frac{\\sum c_i p_{i,t}}{\\sum c_i p_{i,0}}$$
for some invariant weight vector $c$.
However, if $c$ is fixed and independent of $q_0$ and $q_t$, the resulting quantity index derived from factor reversal fails to accommodate shifting consumption shares, violating either factor reversal or proportionality.

This impossibility theorem implies that statistical offices cannot construct a universally perfect index. Agencies must make explicit trade-offs based on the primary analytical objective: Fisher's index satisfies time and factor reversal but fails circularity, while chain-linked series satisfy transitivity at the cost of slight path dependency.

---

## Consumer Price Index Biases: The Boskin Commission Findings

In 1996, the United States Senate commissioned a committee of distinguished economists, chaired by Michael Boskin, to investigate whether the Consumer Price Index systematically overstated the true cost of living. The **Boskin Commission Report** concluded that the official CPI overstated inflation by approximately **1.1 percentage points per annum**.

The report categorized the sources of CPI bias into four distinct structural mechanisms:

1. **Upper-Level Substitution Bias (approx. 0.3% per annum)**:
   The classical Laspeyres CPI uses fixed expenditure basket weights from a historical base survey. When the relative price of beef rises while chicken becomes cheaper, rational consumers substitute toward chicken. A fixed-weight Laspeyres index ignores this substitution, assuming consumers continue purchasing the same expensive bundle, thereby overstating the true cost of attaining the baseline utility level.

2. **Lower-Level Substitution Bias (approx. 0.1% per annum)**:
   Occurs within elementary item categories (e.g., across different brands of canned tomatoes or apples) when arithmetic aggregation (the Carli index) is deployed instead of geometric averaging (the Jevons index).

3. **New Goods Bias (approx. 0.6% combined with Quality Change)**:
   New technological innovations (such as smartphones, personal computers, or life-saving pharmaceuticals) enter commercial markets at high initial prices, followed by rapid price drops as production scales. Fixed-basket indices typically add new goods to the basket years after their introduction, missing the initial phase of dramatic consumer surplus gains and price declines.

4. **Quality Change Bias**:
   When a product's price increases alongside a substantial improvement in performance, durability, fuel efficiency, or safety (e.g., an automobile incorporating anti-lock brakes and advanced airbags), attributing the entire price hike to inflation overstates cost-of-living growth. The portion of the price hike reflecting higher quality represents real output, not inflation.

5. **Outlet Substitution Bias (approx. 0.1% per annum)**:
   Occurs when consumers migrate from traditional high-cost brick-and-mortar department stores to discount warehouse clubs, supercenters, and online e-commerce platforms offering identical goods at lower price levels. Traditional CPI sampling treated discount outlets as entirely separate items, failing to capture the cost reduction experienced by migrating households.

### Fiscal and Policy Consequences of Measurement Bias
An upward bias of 1.1 percentage points in the CPI exerts massive cumulative fiscal effects:
- Government transfer programs (Social Security, veteran pensions) indexed to the CPI over-compensate recipients, compounding annual budgetary outlays by hundreds of billions of dollars over a decade.
- Income tax brackets indexed to the CPI expand too rapidly, leading to unlegislated revenue reductions.
- Real wage growth and historical economic productivity gains are systematically understated.

---

## Hedonic Pricing Models for Quality Adjustment

To eliminate quality change bias, national statistical institutes deploy **Hedonic Regression Analysis**, based on Kelvin Lancaster's consumer theory (which posits that goods are valued for the utility-bearing characteristics they embody) and Sherwin Rosen's hedonic pricing equilibrium.

Let $p_i$ be the market price of a complex durable good (such as a laptop computer or motor vehicle), and let $z_i = [z_{i1}, z_{i2}, \\dots, z_{ik}]$ represent a vector of $k$ objectively measurable technical attributes (processor speed, RAM capacity, battery life, weight, screen resolution). The **Hedonic Price Function** relates market price to attributes:

$$\\ln(p_i) = \\beta_0 + \\sum_{j=1}^{k} \\beta_j z_{ij} + \\epsilon_i$$

where:
- $\\beta_j = \\frac{\\partial \\ln(p)}{\\partial z_j}$ represents the marginal implicit shadow price of characteristic $j$, indicating the percentage premium consumers are willing to pay for an additional unit of that attribute.

When an obsolete model $A$ (with attributes $z_A$ and price $p_{A,0}$) is replaced in the market by an upgraded model $B$ (with attributes $z_B$ and price $p_{B,t}$), the pure quality-adjusted price relative is:

$$\\text{Pure Price Relative} = \\frac{p_{B,t}}{p_{A,0} \\times \\exp\\left( \\sum_{j=1}^{k} \\hat{\\beta}_j (z_{Bj} - z_{Aj}) \\right)}$$

The denominator adjusts the baseline price upward by the exact monetary value of the quality improvement, ensuring that only genuine price inflation enters the Consumer Price Index.
"""

# ----------------------------------------------------
# UNIT 3 EXPANSIONS
# ----------------------------------------------------
u3_boost = """
---

## Advanced Trend Extraction: Orthogonal Polynomials and Modern Filtering

While standard Ordinary Least Squares polynomial fitting provides intuitive trend equations, fitting higher-degree polynomials via normal equations encounters severe numerical instability due to multicollinearity between powers of time ($t, t^2, t^3$). To overcome this, mathematical statisticians employ **Orthogonal Polynomials**, while macroeconomic policy relies on frequency-domain filters.

### 1. Orthogonal Polynomials (Chebyshev-Gram Polynomials)
A set of polynomials $\\{\\phi_0(t), \\phi_1(t), \\dots, \\phi_p(t)\\}$ defined on discrete observation points $t = 1, 2, \\dots, N$ is mutually orthogonal if:

$$\\sum_{t=1}^{N} \\phi_r(t) \\phi_s(t) = 0 \\quad \\text{for all } r \\ne s$$

Expressing the polynomial trend as a linear combination of orthogonal basis functions:

$$T_t = c_0 \\phi_0(t) + c_1 \\phi_1(t) + c_2 \\phi_2(t) + \\dots + c_p \\phi_p(t)$$

Because all cross-product terms vanish ($\\sum \\phi_r \\phi_s = 0$), the normal equations decouple completely. Each parameter $c_r$ can be estimated independently without inverting a matrix:

$$c_r = \\frac{\\sum_{t=1}^{N} Y_t \\phi_r(t)}{\\sum_{t=1}^{N} [\\phi_r(t)]^2}$$

The standardized Chebyshev-Gram polynomials for centered coordinates $x = t - \\bar{t}$ are:
- $\\phi_0(x) = 1$
- $\\phi_1(x) = x$
- $\\phi_2(x) = x^2 - \\frac{N^2 - 1}{12}$
- $\\phi_3(x) = x^3 - \\left( \\frac{3N^2 - 7}{20} \\right) x$

**Practical Advantage**: Adding a higher-order term (e.g., expanding from a quadratic to a cubic trend) does not alter the numerical values of previously estimated lower-order coefficients ($c_0, c_1, c_2$), enabling sequential hypothesis testing of polynomial degree.

### 2. The Hodrick-Prescott (HP) Filter
In modern business cycle analysis and central banking, parametric polynomial trends are largely replaced by the **Hodrick-Prescott (HP) Filter** (Robert Hodrick and Edward Prescott, 1980). The HP filter decomposes an economic time series $y_t$ into a smooth trend component $\\tau_t$ and a cyclical component $c_t = y_t - \\tau_t$ by solving an explicit penalized optimization problem:

$$\\min_{\\{\\tau_t\\}_{t=1}^{T}} \\left\\{ \\sum_{t=1}^{T} (y_t - \\tau_t)^2 + \\lambda \\sum_{t=2}^{T-1} [(\\tau_{t+1} - \\tau_t) - (\\tau_t - \\tau_{t-1})]^2 \\right\\}$$

The objective function balances two competing goals:
1. **Goodness of Fit**: Minimizing the sum of squared cyclical deviations $\\sum (y_t - \\tau_t)^2$.
2. **Smoothness of Trend**: Penalizing second differences (acceleration or curvature) of the trend line via the regularization parameter $\\lambda$.

#### The Smoothing Parameter $\\lambda$:
- As $\\lambda \\to 0$, curvature is unconstrained, and the trend matches the data identically ($\\tau_t = y_t$).
- As $\\lambda \\to \\infty$, second differences are penalized to zero, forcing the trend to become a strictly linear OLS regression line.

By matching the filter's frequency response to standard business cycle durations (cycles between 2 and 8 years), economists adopt canonical values for $\\lambda$:
- **Quarterly Data**: $\\lambda = 1{,}600$
- **Monthly Data**: $\\lambda = 14{,}400$
- **Annual Data**: $\\lambda = 100$ (or $\\lambda = 6.25$ in modern literature)

#### The End-Point Bias Problem:
At the sample boundaries ($t=1$ and $t=T$), the second-difference penalty operates with fewer adjacent points. Consequently, the HP trend is heavily drawn toward the most recent data observations. Central banks must exercise caution when interpreting the HP trend at the current edge of the business cycle.
"""

# ----------------------------------------------------
# UNIT 4 EXPANSIONS
# ----------------------------------------------------
u4_boost = """
---

## Advanced Seasonal Adjustment: The Census X-13ARIMA-SEATS Architecture

While the classical Ratio-to-Moving Average method established the conceptual foundation of seasonal decomposition, contemporary national statistical offices rely on sophisticated algorithmic suites, primarily the U.S. Census Bureau's **X-13ARIMA-SEATS** program (combining the empirical X-11/X-12 moving average filters with the European SEATS model-based ARIMA signal extraction).

### 1. The Multi-Stage X-11 Filtering Pipeline
The X-11 algorithm operates through an iterative, cascading sequence of moving average filters designed to separate trend-cycle, seasonal, and irregular components while isolating extreme outliers:

1. **Step 1: Preliminary Trend-Cycle Estimation**:
   A 12-month (or 4-quarter) centered moving average is fitted to raw data $Y_t$ to produce a preliminary trend-cycle estimate $T_t^{(1)}$.
2. **Step 2: Preliminary Seasonal-Irregular Ratios**:
   In a multiplicative model, ratios $SI_t^{(1)} = Y_t / T_t^{(1)}$ are computed.
3. **Step 3: Preliminary Seasonal Filtering via $3 \\times 3$ Moving Average**:
   To isolate preliminary seasonal factors from $SI_t^{(1)}$, a weighted 5-term moving average (a 3-term average of a 3-term average, denoted $3 \\times 3$) is computed separately for each calendar month across years:
   $$S_t^{(1)} = \\frac{1}{9} SI_{t-24} + \\frac{2}{9} SI_{t-12} + \\frac{3}{9} SI_t + \\frac{2}{9} SI_{t+12} + \\frac{1}{9} SI_{t+24}$$
4. **Step 4: Preliminary Deseasonalization**:
   The raw series is divided by the normalized seasonal factor: $D_t^{(1)} = Y_t / S_t^{(1)}$.
5. **Step 5: Refined Trend Extraction via the Henderson Filter**:
   The Henderson moving average filter (typically 13 terms for monthly data, with specialized symmetric cubic-preserving weights) is applied to $D_t^{(1)}$ to generate an improved trend-cycle estimate $T_t^{(2)}$.
6. **Step 6: Iterative Convergence and Outlier Downweighting**:
   Ratios $SI_t^{(2)} = Y_t / T_t^{(2)}$ are scrutinized for extreme outliers exceeding $2.5\\sigma$. Outliers are replaced with modified values, and a wider $3 \\times 5$ or $3 \\times 9$ seasonal filter is deployed, yielding final seasonal indices $S_t^*$ and deseasonalized series $D_t^*$.

### 2. Calendar and Working-Day Adjustments
Raw macroeconomic figures are distorted not only by seasonal weather, but by calendar mechanics:
- **Trading Day / Working Day Variations**: Different months contain varying numbers of Mondays, Fridays, or weekend days. If a month contains five Saturdays and five Sundays, retail sales or construction activity will diverge sharply from a month with five working weekdays.
- **Moving Holiday Effects**: Major religious and cultural holidays (such as Easter, Chinese New Year, Passover, and Eid) shift across calendar months from year to year. X-13ARIMA models these events using regression variables with ARIMA errors (RegARIMA), estimating holiday coefficients prior to seasonal decomposition.

---

## Frequency-Domain Spectral Analysis of Seasonality

In mathematical statistics, seasonality can be analyzed in the frequency domain via **Spectral Density Analysis**. A covariance-stationary time series $Y_t$ possesses an autocovariance function $\\gamma(k) = \\text{Cov}(Y_t, Y_{t-k})$.
The **Spectral Density Function** $f(\\omega)$ is the Fourier transform of the autocovariance sequence:

$$f(\\omega) = \\frac{1}{2\\pi} \\left[ \\gamma(0) + 2 \\sum_{k=1}^{\\infty} \\gamma(k) \\cos(\\omega k) \\right], \\quad \\omega \\in [0, \\pi]$$

where $\\omega$ denotes angular frequency in radians per unit time. The area under the spectral density function over any frequency band represents the proportion of total series variance generated by oscillations in that frequency band.

### Detecting Seasonal Harmonics
For monthly time series, annual seasonality corresponds to a fundamental cycle of period 12 months, corresponding to angular frequency:
$$\\omega_1 = \\frac{2\\pi}{12} = \\frac{\\pi}{6} \\approx 0.5236 \\text{ radians}$$

Non-sinusoidal seasonal patterns also generate sharp spectral spikes at the harmonic frequencies:
- $\\omega_2 = 2 \\times \\frac{2\\pi}{12} = \\frac{2\\pi}{6}$ (6-month semi-annual harmonic)
- $\\omega_3 = 3 \\times \\frac{2\\pi}{12} = \\frac{\\pi}{2}$ (4-month quarterly harmonic)
- $\\omega_4 = 4 \\times \\frac{2\\pi}{12} = \\frac{2\\pi}{3}$ (3-month harmonic)
- $\\omega_5 = 5 \\times \\frac{2\\pi}{12} = \\frac{5\\pi}{6}$ (2.4-month harmonic)
- $\\omega_6 = \\pi$ (2-month bi-monthly harmonic)

A properly deseasonalized economic time series must display a smooth spectral density function devoid of prominent peaks at these six canonical seasonal harmonic frequencies.
"""

# ----------------------------------------------------
# UNIT 5 EXPANSIONS
# ----------------------------------------------------
u5_boost = """
---

## Entropy-Based Inequality Metrics: The Generalized Entropy Family

While the Gini coefficient provides an intuitive geometric measure of inequality, it suffers from a major mathematical limitation: it is not strictly **sub-group decomposable**. If a population is divided into distinct geographic regions or ethnic subgroups, national Gini inequality cannot be cleanly partitioned into the sum of within-group inequality and between-group inequality without generating an intractable overlapping residual term.

To overcome this, mathematical economists deploy the **Generalized Entropy (GE) Family of Inequality Measures**, rooted in Claude Shannon's information theory.

### Mathematical Formulation
For a discrete population of $n$ individuals with incomes $y = [y_1, y_2, \\dots, y_n]$ and arithmetic mean $\\mu = \\frac{1}{n} \\sum y_i$, the Generalized Entropy Index $GE(\\alpha)$ is defined as:

$$GE(\\alpha) = \\begin{cases}
\\frac{1}{\\alpha(\\alpha - 1)} \\left[ \\frac{1}{n} \\sum_{i=1}^{n} \\left( \\frac{y_i}{\\mu} \\right)^\\alpha - 1 \\right], & \\alpha \\ne 0, 1 \\\\
\\frac{1}{n} \\sum_{i=1}^{n} \\ln\\left( \\frac{\\mu}{y_i} \\right), & \\alpha = 0 \\\\
\\frac{1}{n} \\sum_{i=1}^{n} \\left( \\frac{y_i}{\\mu} \\right) \\ln\\left( \\frac{y_i}{\\mu} \\right), & \\alpha = 1
\\end{cases}$$

The parameter $\\alpha \\in (-\\infty, \\infty)$ represents sensitivity to income disparities at differing parts of the distribution:
- For large positive $\\alpha$ (e.g., $\\alpha = 2$), the index is sensitive to income concentration at the very top of the distribution.
- For $\\alpha = 1$, the index is the celebrated **Theil's $T$ Index**.
- For $\\alpha = 0$, the index is **Theil's $L$ Index** (also known as the **Mean Log Deviation, MLD**), which is particularly sensitive to distress in the lower tail.
- For $\\alpha = 2$, $GE(2) = \\frac{1}{2} \\left( \\frac{\\sigma}{\\mu} \\right)^2 = \\frac{1}{2} CV^2$, which is half the squared coefficient of variation.

### Perfect Sub-Group Decomposability
Suppose a nation's population is partitioned into $K$ mutually exclusive subgroups ($k = 1, \\dots, K$), where subgroup $k$ has population $n_k$, mean income $\\mu_k$, population share $v_k = n_k / n$, and aggregate income share $s_k = (n_k \\mu_k) / (n \\mu)$.
Every Generalized Entropy index decomposes into:

$$GE(\\alpha) = GE_{\\text{within}}(\\alpha) + GE_{\\text{between}}(\\alpha)$$

where:
$$GE_{\\text{within}}(\\alpha) = \\sum_{k=1}^{K} v_k^{1-\\alpha} s_k^\\alpha GE_k(\\alpha)$$
$$GE_{\\text{between}}(\\alpha) = \\frac{1}{\\alpha(\\alpha - 1)} \\left[ \\sum_{k=1}^{K} v_k \\left( \\frac{\\mu_k}{\\mu} \\right)^\\alpha - 1 \\right]$$

For the Mean Log Deviation ($\\alpha = 0$), the weights simplify to population shares:
$$MLD = \\sum_{k=1}^{K} v_k MLD_k + \\sum_{k=1}^{K} v_k \\ln\\left( \\frac{\\mu}{\\mu_k} \\right)$$

This property enables policymakers to evaluate what percentage of national inequality stems from disparities within provinces versus average income gaps between provinces.

---

## Normative Inequality Measurement: The Atkinson Index

In 1970, British economist Anthony B. Atkinson formulated an explicit welfare-theoretic approach to inequality measurement. Atkinson argued that every statistical inequality metric embodies an implicit ethical value judgment regarding social welfare.

### 1. Equally Distributed Equivalent Income ($y_{\\text{ede}}$)
Let society possess an additive, utilitarian Social Welfare Function over individual incomes:
$$W = \\frac{1}{n} \\sum_{i=1}^{n} U(y_i)$$
where $U(y)$ exhibits constant relative inequality aversion $\\epsilon \\ge 0$:
$$U(y) = \\begin{cases} \\frac{y^{1-\\epsilon}}{1-\\epsilon}, & \\epsilon \\ne 1 \\\\ \\ln(y), & \\epsilon = 1 \\end{cases}$$

Atkinson defined the **Equally Distributed Equivalent Income ($y_{\\text{ede}}$)** as that hypothetical level of uniform per-capita income which, if enjoyed by every single individual in society, would generate the exact same level of total social welfare as the currently observed unequal income distribution:

$$U(y_{\\text{ede}}) = \\frac{1}{n} \\sum_{i=1}^{n} U(y_i)$$

Solving for $y_{\\text{ede}}$:
$$y_{\\text{ede}} = \\begin{cases} \\left[ \\frac{1}{n} \\sum_{i=1}^{n} y_i^{1-\\epsilon} \\right]^{\\frac{1}{1-\\epsilon}}, & \\epsilon \\ne 1 \\\\ \\exp\\left( \\frac{1}{n} \\sum_{i=1}^{n} \\ln(y_i) \\right), & \\epsilon = 1 \\end{cases}$$

Because $U(y)$ is strictly concave for $\\epsilon > 0$, by Jensen's inequality $y_{\\text{ede}} < \\mu$, where $\\mu$ is the actual arithmetic mean income.

### 2. The Atkinson Inequality Index ($A_\\epsilon$)
The Atkinson Index is defined as the proportional welfare loss attributable to unequal income distribution:

$$A_\\epsilon = 1 - \\frac{y_{\\text{ede}}}{\\mu} = 1 - \\left[ \\frac{1}{n} \\sum_{i=1}^{n} \\left( \\frac{y_i}{\\mu} \\right)^{1-\\epsilon} \\right]^{\\frac{1}{1-\\epsilon}}$$

- **Interpretation**: An Atkinson index of $A_\\epsilon = 0.20$ means that if income were distributed completely equally, society could achieve the same level of aggregate social welfare with only $80\\%$ of its current total income. The remaining $20\\%$ of national income is effectively "wasted" on inequality.
- **The Inequality Aversion Parameter $\\epsilon$**:
  - $\\epsilon = 0$: Society is indifferent to inequality ($y_{\\text{ede}} = \\mu \\implies A_0 = 0$).
  - $\\epsilon \\to \\infty$: Society adopts a Rawlsian maximin criterion, focusing exclusively on the welfare of the poorest citizen.
"""

# ----------------------------------------------------
# UNIT 6 EXPANSIONS
# ----------------------------------------------------
u6_boost = """
---

## Modern National Accounting: Chain-Linked Volume Measures in SNA 2008

For decades, statistical agencies computed real macroeconomic output using a fixed-base Laspeyres volume index: holding relative commodity prices constant at a fixed base year (e.g., 2010 prices) for ten or fifteen years. However, in modern dynamic economies characterized by rapid technological innovation and shifting relative prices, fixed-base series suffer from severe **Base Year Aging (Substitution Bias)**.

### The Breakdown of Fixed-Base Volume Series
As information technology and electronics drop exponentially in price while expanding in physical output (e.g., semiconductor chips, cloud computing), evaluating contemporary computer hardware at 2010 prices assigns exorbitant, obsolete weights to high-growth tech sectors. This causes fixed-base real GDP to artificially overstate economic growth in post-base years—a distortion known as the **Gerschenkron Effect**.

### Annual Chain-Linking Methodology
To eliminate base year aging, the United Nations System of National Accounts (SNA 2008) mandates the adoption of **Annual Chain-Linked Volume Measures**.

Under annual chain-linking:
1. Economic volume growth between year $t-1$ and year $t$ is calculated using the actual prices of the immediately preceding year ($t-1$):
   $$L_{V}^{t-1 \\to t} = \\frac{\\sum_{i=1}^{M} P_{i, t-1} Q_{i, t}}{\\sum_{i=1}^{M} P_{i, t-1} Q_{i, t-1}}$$
2. The consecutive annual volume growth factors are chained (multiplied) together relative to an arbitrary reference year $T_0$:
   $$\\text{Chained Volume Index}_t = \\prod_{\\tau=1}^{t} L_{V}^{\\tau-1 \\to \\tau}$$
3. The chained index is scaled to the nominal currency value of the reference year to produce **Chained Dollars** or **Chained Euros**.

#### The Loss of Additive Consistency:
While annual chain-linking eliminates substitution bias, it introduces a major structural trade-off: **Non-Additivity of Chained Aggregates**. In any year other than the reference year and the year immediately following it, the sum of chain-linked components (e.g., chain-linked consumption + chain-linked investment + chain-linked net exports) does not mathematically equal chain-linked real GDP. National accountants must explicitly publish a balancing discrepancy term to account for non-additivity.

---

## Measuring the Non-Observed and Informal Economy (NOE)

In many developing and emerging economies, a substantial fraction of economic activity occurs outside official regulatory, tax, and social security registries. To prevent Gross Domestic Product from drastically understating total national production, national statistical institutes apply specialized econometric and survey methodologies to estimate the **Non-Observed Economy (NOE)**.

The OECD and SNA categorize the non-observed economy into five structural components:
1. **Underground Production**: Activities that are productive and legal in principle, but deliberately concealed from public authorities to evade income taxes, social security charges, minimum wage laws, or administrative regulations.
2. **Illegal Production**: Production of goods and services whose sale, distribution, or possession is prohibited by criminal law (e.g., narcotics trafficking, illicit arms trade, smuggling, unlicensed gambling).
3. **Informal Sector Production**: Small-scale, unincorporated market enterprises owned by households (street vendors, unregistered artisanal workshops, informal subsistence transport) with low organization and zero formal accounting records.
4. **Household Production for Own Final Use**: Subsistence agriculture, owner-occupied housing maintenance, and domestic water/firewood collection.
5. **Deficiencies in Basic Data Collection Systems**: Formal enterprises omitted from business registers due to rapid enterprise churn or non-response.

### Statistical Estimation Techniques:
- **The Labor Input Method (Italian ISTAT Methodology)**:
  Compares total labor supply estimated from comprehensive household Population Census / Labor Force Surveys with the labor demand officially reported by registered enterprises. The surplus of employed individuals over registered employees reveals the volume of informal labor, which is multiplied by sector-specific productivity benchmarks to impute unrecorded output.
- **The Currency Demand Approach (Tanzi Model)**:
  Estimates an econometric money demand equation. Excess cash holding beyond that explained by real income and interest rates is attributed to tax evasion, estimating the volume of hidden market transactions.
"""

# ----------------------------------------------------
# UNIT 7 EXPANSIONS
# ----------------------------------------------------
u7_boost = """
---

## Advanced Input-Output Systems: The Price Dual and Closed Models

While the primal Leontief model solves for gross physical output given final demand, input-output theory possesses a mathematically symmetrical **Price Dual Model** governing how input costs, wages, and profit markups determine industry product prices.

### 1. The Price Dual Leontief Model
Let $p = [p_1, p_2, \\dots, p_n]^T$ represent the vector of unit prices charged by the $n$ producing industries.
For each sector $j$, its unit price must cover the cost of intermediate inputs purchased from all sectors plus primary value-added costs per unit of gross output (labor wages, depreciation, indirect taxes, and normal profits):

$$p_j = \\sum_{i=1}^{n} p_i a_{ij} + v_j, \\quad j = 1, 2, \\dots, n$$

where $v_j = V_j / X_j$ is the **Value-Added Coefficient** of sector $j$.
In matrix notation:

$$p = A^T p + v$$

where $A^T$ is the transpose of the technology matrix $A$, and $v = [v_1, v_2, \\dots, v_n]^T$.
Rearranging:

$$(I - A^T) p = v \\implies p = (I - A^T)^{-1} v = \\left[ (I - A)^{-1} \\right]^T v$$

The price dual shows that each industry's equilibrium price is a linear combination of primary value-added inputs across all upstream sectors, weighted by the transposed Leontief inverse.

#### Practical Policy Application: Cost-Push Inflation Modeling:
The price dual is the standard tool used by ministries of finance and central banks to trace the economy-wide transmission of cost shocks. If a carbon tax is levied on the energy sector ($v_{\\text{energy}}$ increases by $\\Delta v_1$), the price vector response is:
$$\\Delta p = (I - A^T)^{-1} \\Delta v$$
The model calculates the exact cascading inflationary impact on steel, manufacturing, freight logistics, and consumer retail prices.

### 2. The Closed Leontief Model and Induced Multipliers
In the open static Leontief model, final demand $F$ is treated as strictly exogenous. However, in reality, household consumption is endogenously driven by the labor income earned in production: expanding industrial output creates jobs, paying wages to workers who subsequently spend their earnings on consumer goods.

The **Closed Leontief Model** endogenizes households by treating them as the $(n+1)$-th industry:
- **Household Row (Inputs to Production)**: Sector $n+1$ provides labor services; row coefficients represent labor input per unit output: $a_{n+1, j} = L_j / X_j$.
- **Household Column (Consumption Demand)**: Column coefficients represent household consumption shares per dollar of labor income: $a_{i, n+1} = C_i / E_{\\text{total}}$.

The augmented $(n+1) \\times (n+1)$ coefficient matrix $\\tilde{A}$ is:
$$\\tilde{A} = \\begin{bmatrix} A & c \\\\ l^T & 0 \\end{bmatrix}$$

Inverting $(I - \\tilde{A})$ yields the **Type II (Induced) Multipliers**:

$$\\text{Type II Multiplier} = \\text{Direct Impact} + \\text{Indirect Supply-Chain Impact} + \\text{Induced Household Spending Impact}$$

Type II multipliers are systematically larger than Type I (direct + indirect) multipliers, capturing the full Keynesian circular flow of income and expenditure.
"""

# ----------------------------------------------------
# UNIT 8 EXPANSIONS
# ----------------------------------------------------
u8_boost = """
---

## Advanced Demand Systems: The Almost Ideal Demand System (AIDS)

While single-equation log-log demand models provide convenient elasticity estimates, microeconomic theory dictates that multi-commodity demand functions must satisfy system-wide consumer optimization restrictions: Slutsky symmetry, homogeneity of degree zero, and budget exhaustion. In 1980, Angus Deaton and John Muellbauer revolutionized applied consumer economics by introducing the **Almost Ideal Demand System (AIDS)**.

### Mathematical Specification of the AIDS Model
Derived from the Price-Independent Generalized Logarithmic (PIGLOG) expenditure function, the AIDS model expresses the expenditure budget share $w_i = (p_i q_i) / M$ of good $i$ as a linear function of the logarithms of individual commodity prices and real household expenditure:

$$w_i = \\alpha_i + \\sum_{j=1}^{n} \\gamma_{ij} \\ln(p_j) + \\beta_i \\ln\\left( \\frac{M}{P^*} \\right) + u_i, \\quad i = 1, 2, \\dots, n$$

where:
- $w_i$ is the budget share of good $i$ ($\\sum w_i = 1$).
- $p_j$ is the price of commodity $j$.
- $M$ is total nominal household expenditure.
- $P^*$ is an aggregate translog price index, commonly approximated in empirical research by the **Stone Price Index**:
  $$\\ln(P^*) \\approx \\sum_{k=1}^{n} w_k \\ln(p_k)$$

### Theoretical Restrictions on AIDS Parameters:
To conform to neoclassical utility maximization, the parameter matrices must satisfy three sets of linear restrictions:
1. **Adding-Up (Budget Exhaustion)**:
   $$\\sum_{i=1}^{n} \\alpha_i = 1, \\quad \\sum_{i=1}^{n} \\gamma_{ij} = 0, \\quad \\sum_{i=1}^{n} \\beta_i = 0$$
2. **Homogeneity of Degree Zero in Prices and Income**:
   $$\\sum_{j=1}^{n} \\gamma_{ij} = 0 \\quad \\text{for each good } i$$
3. **Slutsky Symmetry**:
   $$\\gamma_{ij} = \\gamma_{ji} \\quad \\text{for all } i \\ne j$$

### Elasticity Formulas in the AIDS Model:
- **Expenditure (Income) Elasticity**:
  $$\\eta_{i, M} = 1 + \\frac{\\beta_i}{w_i}$$
  - If $\\beta_i > 0$, good $i$ is a **Luxury** ($\\eta_{i,M} > 1$); its budget share expands as total expenditure rises.
  - If $\\beta_i < 0$, good $i$ is a **Necessity** ($\\eta_{i,M} < 1$); its budget share contracts as total expenditure rises, conforming to Engel's Law.
- **Uncompensated (Marshallian) Own-Price Elasticity**:
  $$\\eta_{ii} = -1 + \\frac{\\gamma_{ii}}{w_i} - \\beta_i$$
- **Cross-Price Elasticity**:
  $$\\eta_{ij} = \\frac{\\gamma_{ij}}{w_i} - \\beta_i \\left( \\frac{w_j}{w_i} \\right)$$

The AIDS framework allows econometricians to test whether empirical consumer choices conform to utility theory while estimating rich price and income substitution matrices across large consumer baskets.

---

## Consumer Welfare and Deadweight Loss Quantification

When governments introduce excise taxes, import tariffs, or environmental carbon fees, consumer prices rise and equilibrium consumption contracts. Econometric demand equations enable precise mathematical quantification of the resulting welfare impacts.

### Compensating and Equivalent Variation
Let $v(p, M)$ denote the indirect utility function, and let $e(p, u)$ denote the expenditure function.
When prices rise from $p^0$ to $p^1$:
1. **Compensating Variation ($CV$)**: The additional monetary compensation a consumer requires at the new prices $p^1$ to restore their original baseline utility level $u^0$:
   $$CV = e(p^1, u^0) - e(p^0, u^0) = e(p^1, u^0) - M^0$$
2. **Equivalent Variation ($EV$)**: The monetary reduction in base income at initial prices $p^0$ that would reduce the consumer's welfare by the same amount as the price hike:
   $$EV = e(p^1, u^1) - e(p^0, u^1) = M^0 - e(p^0, u^1)$$

### Marshallian Consumer Surplus and Harberger Deadweight Loss
For moderate price changes where income effects are small, consumer welfare loss is approximated by the change in **Marshallian Consumer Surplus ($\\Delta CS$)**:

$$\\Delta CS = -\\int_{P^0}^{P^1} Q(P) dP$$

When an ad valorem tax rate $t$ is levied on a competitive commodity with initial price $P_0$ and quantity $Q_0$:
- Price paid by buyers: $P_1 = P_0 (1 + t)$
- New quantity demanded: $Q_1 = Q_0 [1 - |\\eta_p| t]$
- Government Tax Revenue:
  $$TR = t P_0 Q_1 = t P_0 Q_0 (1 - |\\eta_p| t)$$
- **Deadweight Loss (Harberger Excess Burden)**:
  $$DWL = -\\Delta CS - TR = \\frac{1}{2} \\Delta P \\Delta Q = \\frac{1}{2} (t P_0) (|\\eta_p| t Q_0) = \\frac{1}{2} |\\eta_p| P_0 Q_0 t^2$$

The deadweight loss of taxation increases with the **square of the tax rate ($t^2$)** and proportionally with the **price elasticity of demand ($|\\eta_p|$)**. This foundational statistical theorem underpins optimal tax policy: to minimize societal welfare loss, governments should levy higher tax rates on highly price-inelastic necessities and lower rates on highly elastic goods (the Ramsey Tax Rule).
"""

boosters = {
    1: u1_boost,
    2: u2_boost,
    3: u3_boost,
    4: u4_boost,
    5: u5_boost,
    6: u6_boost,
    7: u7_boost,
    8: u8_boost,
}

for unit_num, boost_text in boosters.items():
    file_path = OUT_DIR / f"unit-{unit_num}.md"
    content = file_path.read_text(encoding="utf-8")
    new_content = inject_before_worked_questions(content, boost_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Unit {unit_num} boosted: {prose_count(new_content)} words")
