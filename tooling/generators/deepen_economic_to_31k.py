#!/usr/bin/env python3
"""
Deepen Units 2 through 8 of Economic Statistics to ensure total pure prose exceeds 30,500 words.
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
# UNIT 2 DEEPENING
# ----------------------------------------------------
u2_deep = """
---

## The Stochastic Approach to Index Numbers

In contrast to the axiomatic approach of Fisher or the microeconomic approach of Konüs, the **Stochastic Approach to Index Numbers** treats observed price relatives as independent sample realizations of a underlying general inflation signal contaminated by idiosyncratic, item-specific relative price shocks. Pioneered by William Stanley Jevons (1863) and Francis Ysidro Edgeworth (1887), and modernized by E. A. Selvanathan and D. S. Prasada Rao (1994), this framework casts index construction as a formal problem of statistical estimation.

### 1. The Classical Unweighted Stochastic Model
Let $R_{it} = p_{it} / p_{i0}$ denote the observed price relative for commodity $i$ ($i = 1, \\dots, k$) between base period $0$ and current period $t$.
The stochastic model posits:

$$R_{it} = \\Pi_t \\epsilon_{it}$$

where:
- $\\Pi_t$ represents the common systematic macroeconomic price change parameter (the true underlying price level ratio).
- $\\epsilon_{it}$ is a multiplicative random disturbance representing commodity-specific supply or demand shocks, satisfying $E[\\epsilon_{it}] = 1$ and $\\text{Var}(\\epsilon_{it}) = \\sigma^2$.

Taking natural logarithms linearizes the estimation equation:

$$\\ln(R_{it}) = \\pi_t + u_{it}$$

where $\\pi_t = \\ln(\\Pi_t)$ and $u_{it} = \\ln(\\epsilon_{it})$ is an additive zero-mean disturbance with constant variance $\\sigma_u^2$.
The Ordinary Least Squares (OLS) estimator of $\\pi_t$ is the unweighted sample mean of the log price relatives:

$$\\hat{\\pi}_t = \\frac{1}{k} \\sum_{i=1}^{k} \\ln(R_{it})$$

Exponentiating $\\hat{\\pi}_t$ yields the estimated price index:

$$\\hat{\\Pi}_t = \\exp(\\hat{\\pi}_t) = \\left[ \\prod_{i=1}^{k} \\left( \\frac{p_{it}}{p_{i0}} \\right) \\right]^{1/k} = P_{\\text{Jevons}}$$

The stochastic approach provides an explicit econometric justification for the **Jevons Index**: it is the Best Linear Unbiased Estimator (BLUE) of underlying general inflation when relative price shocks are identically and independently distributed across commodities.

### 2. Weighted Stochastic Regression Models
Because commodities vary widely in economic importance, the assumption of homoskedastic disturbances is unrealistic: expenditure-heavy staple commodities generally exhibit more stable relative prices than minor luxury goods.
To incorporate economic weights, Edgeworth proposed minimizing a weighted sum of squared residuals:

$$\\min_{\\pi_t} \\sum_{i=1}^{k} w_i [\\ln(R_{it}) - \\pi_t]^2$$

where $w_i = \\frac{1}{2}(w_{i0} + w_{it})$ is the average expenditure share of good $i$.
Setting the first derivative to zero yields:

$$\\hat{\\pi}_t = \\sum_{i=1}^{k} w_i \\ln(R_{it})$$

Exponentiating this weighted regression coefficient yields:

$$\\hat{\\Pi}_t = \\exp\\left( \\sum_{i=1}^{k} w_i \\ln\\left( \\frac{p_{it}}{p_{i0}} \\right) \\right) = P_{\\text{Törnqvist}}$$

Under the stochastic framework, the **Törnqvist Superlative Index** emerges as the Weighted Least Squares econometric estimator of inflation. Furthermore, the regression framework yields standard errors and confidence intervals for the rate of inflation, allowing statisticians to conduct formal hypothesis tests regarding price stability.

---

## Plutocratic vs Democratic Price Indices and Distributional Inflation

The Consumer Price Index published by national statistical offices is constructed using national aggregate expenditure weights:

$$w_i = \\frac{\\sum_{h=1}^{H} E_{ih}}{\\sum_{h=1}^{H} \\sum_{j=1}^{n} E_{jh}}$$

where $E_{ih}$ represents expenditure on good $i$ by household $h$ across all $H$ households in the economy.

### 1. The Plutocratic Bias of the Aggregate CPI
In 1958, S. J. Prais demonstrated that the national aggregate expenditure weights represent an income-weighted average of individual household expenditure shares:

$$w_i = \\sum_{h=1}^{H} \\left( \\frac{E_h}{E_{\\text{total}}} \\right) s_{ih}$$

where $s_{ih} = E_{ih} / E_h$ is the budget share of good $i$ in household $h$, and $E_h / E_{\\text{total}}$ is household $h$'s share of aggregate national consumer spending.

Because affluent households spend vastly more money than impoverished households, their budget shares dominate national aggregate weights:
- A wealthy household spending $\\$200{,}000$ annually receives **twenty times greater mathematical weight** in the national CPI than a low-income household spending $\\$10{,}000$ annually.
- The official CPI is therefore fundamentally **Plutocratic**: it reflects the purchasing patterns of households near the 75th or 80th percentile of the income distribution.

### 2. The Democratic Price Index
To reflect democratic social welfare principles ("one household, one vote"), Prais formulated the **Democratic Price Index**:

$$w_i^{\\text{dem}} = \\frac{1}{H} \\sum_{h=1}^{H} s_{ih}$$

The Democratic CPI assigns equal mathematical weight to every household's budget allocation regardless of wealth.

#### Policy Implications:
During periods when essential necessities (food, household heating, electricity, basic rent) inflate faster than luxury discretionary services (air travel, electronics, fine dining), the inflation rate experienced by the bottom two deciles of society is substantially higher than the official plutocratic CPI. Indexing state welfare benefits and minimum wages strictly to the plutocratic CPI leads to silent erosion of real living standards among the most vulnerable citizens.
"""

# ----------------------------------------------------
# UNIT 3 DEEPENING
# ----------------------------------------------------
u3_deep = """
---

## Stochastic Trends, Unit Roots, and the Nelson-Plosser Revolution

For decades, econometricians treated macroeconomic time series as **Trend-Stationary Processes ($TSP$)**: deterministic linear or polynomial trends accompanied by stationary cyclical fluctuations:

$$Y_t = \\alpha + \\beta t + \\epsilon_t, \\quad \\epsilon_t \\sim I(0)$$

Under a trend-stationary specification, economic shocks are purely temporary: after a recession or supply disruption, the economy inevitably reverts back to its predetermined deterministic trend path.

### 1. Difference-Stationary Processes and Random Walks
In a landmark 1982 empirical paper, Charles Nelson and Charles Plosser tested historical macroeconomic series (real GNP, industrial production, employment, real wages) and overturned this classical paradigm. They demonstrated that most macroeconomic series are **Difference-Stationary Processes ($DSP$)** containing a **Stochastic Trend (Unit Root)**:

$$Y_t = \\mu + Y_{t-1} + u_t, \\quad u_t \\sim I(0)$$

Iterating backwards from an initial value $Y_0$:

$$Y_t = Y_0 + \\mu t + \\sum_{j=1}^{t} u_j$$

In a difference-stationary process:
- $\\mu t$ represents a deterministic drift rate.
- $\\sum_{j=1}^{t} u_j$ is a cumulative stochastic trend (a random walk with drift).

#### The Permanent Effect of Shocks:
In a unit root process, the variance expands linearly with time: $\\text{Var}(Y_t) = t \\sigma_u^2 \\to \\infty$ as $t \\to \\infty$. Every historical shock $u_t$ enters the summation with a coefficient of unity and permanently shifts the level of the time series forever. Recessions are not mere temporary dips below a deterministic trend; they permanently alter the long-run path of potential output.

### 2. Testing for Unit Roots: The Augmented Dickey-Fuller (ADF) Test
To test whether an economic series follows a deterministic trend or a stochastic unit root, David Dickey and Wayne Fuller (1979, 1981) formulated the **Dickey-Fuller Test**.
Consider the autoregressive model:

$$Y_t = \\alpha + \\beta t + \\rho Y_{t-1} + \\sum_{k=1}^{p} \\gamma_k \\Delta Y_{t-k} + e_t$$

Subtracting $Y_{t-1}$ from both sides:

$$\\Delta Y_t = \\alpha + \\beta t + \\delta Y_{t-1} + \\sum_{k=1}^{p} \\gamma_k \\Delta Y_{t-k} + e_t$$

where $\\delta = \\rho - 1$.
The hypotheses are:
- **Null Hypothesis ($H_0$)**: $\\delta = 0 \\iff \\rho = 1$ (The series contains a unit root / stochastic trend).
- **Alternative Hypothesis ($H_1$)**: $\\delta < 0 \\iff \\rho < 1$ (The series is trend-stationary).

Under the null hypothesis, the standard $t$-statistic $t_\\delta = \\hat{\\delta} / \\text{SE}(\\hat{\\delta})$ does not follow a Student's $t$-distribution, but rather the non-standard **Dickey-Fuller distribution** (characterized by Brownian motion integrals). If the test fails to reject $H_0$, detrending via simple OLS regression produces spurious results, and the series must be transformed via first-differencing: $\\Delta Y_t = Y_t - Y_{t-1}$.

---

## Structural Breaks in Trend: Perron's Breakthrough

In 1989, Pierre Perron demonstrated that standard Dickey-Fuller tests are dramatically biased toward erroneously finding a unit root if the true underlying data-generating process is a trend-stationary series with an unmodeled **Structural Break** (such as the 1929 Great Depression or the 1973 OPEC oil price shock).

Perron formulated models allowing for abrupt changes in trend parameters:
1. **Crash Model (Level Shift)**: An abrupt vertical jump in the trend intercept:
   $$Y_t = \\alpha_1 + (\\alpha_2 - \\alpha_1) D_U(t) + \\beta t + \\epsilon_t$$
   where $D_U(t) = 1$ if $t > T_B$ (break date) and $0$ otherwise.
2. **Changing Growth Model (Slope Break)**: A permanent shift in the trend slope:
   $$Y_t = \\alpha + \\beta_1 t + (\\beta_2 - \\beta_1) D_T(t) + \\epsilon_t$$
   where $D_T(t) = t - T_B$ if $t > T_B$ and $0$ otherwise.
3. **Combined Model (Simultaneous Jump and Slope Rotation)**.

Perron established that when major macroeconomic shocks are modeled as structural breaks, many aggregate economic time series revert to trend-stationarity, demonstrating that secular trends consist of long periods of steady growth punctuated by rare structural regime shifts.
"""

# ----------------------------------------------------
# UNIT 4 DEEPENING
# ----------------------------------------------------
u4_deep = """
---

## Seasonal Unit Roots: The HEGY Statistical Framework

Just as annual time series can exhibit non-stationary stochastic trends, seasonal quarterly or monthly series can exhibit **Stochastic Seasonality**—where the seasonal pattern itself evolves randomly over time rather than remaining fixed.

In 1990, Svend Hylleberg, Robert Engle, Clive Granger, and Byung Sam Yoo developed the celebrated **HEGY Test** for seasonal unit roots in quarterly time series.

### The Seasonal Lag Operator Polynomial
For a quarterly series, the annual seasonal differencing operator is:

$$\\Delta_4 Y_t = Y_t - Y_{t-4} = (1 - L^4) Y_t$$

Factoring the fourth-degree polynomial $(1 - L^4)$ into its roots:

$$1 - L^4 = (1 - L)(1 + L)(1 + L^2) = (1 - L)(1 + L)(1 - iL)(1 + iL)$$

This factorization reveals four distinct unit roots located on the complex unit circle, each corresponding to a specific frequency:
1. **Zero Frequency Root ($L = 1$)**: The standard non-seasonal long-run unit root (governing secular trend drift).
2. **Semi-Annual Frequency Root ($L = -1$)**: Cycles with period 2 quarters (6 months), angular frequency $\\omega = \\pi$.
3. **Annual Complex Roots ($L = \\pm i$)**: Cycles with period 4 quarters (12 months), angular frequency $\\omega = \\pm \\pi/2$.

The HEGY regression model filters the series into four orthogonal components:
$$\\Delta_4 Y_t = \\pi_1 y_{1, t-1} + \\pi_2 y_{2, t-1} + \\pi_3 y_{3, t-1} + \\pi_4 y_{3, t-2} + \\sum_{k=1}^{p} \\phi_k \\Delta_4 Y_{t-k} + \\epsilon_t$$

where:
- $y_{1t} = (1 + L + L^2 + L^3) Y_t$ (filters out all seasonal roots, preserving zero frequency).
- $y_{2t} = -(1 - L + L^2 - L^3) Y_t$ (preserves semi-annual frequency).
- $y_{3t} = -(1 - L^2) Y_t$ (preserves annual frequency).

Testing $\\pi_1 = 0$ tests for a zero-frequency unit root, $\\pi_2 = 0$ tests for a semi-annual unit root, and a joint $F$-test on $\\pi_3 = \\pi_4 = 0$ tests for annual seasonal unit roots. If seasonal unit roots exist, standard dummy variable seasonal adjustment is statistically invalid, and seasonal differencing must be performed.

---

## Early Warning Composite Leading Indicators and Turning Point Forecasting

To forecast macroeconomic business cycle turning points before they appear in lagging GDP data, economic institutions construct **Composite Leading Indicators (CLI)** based on the methodology pioneered by Wesley Mitchell and Arthur Burns at the NBER.

### 1. Classification of Macroeconomic Indicators
- **Leading Indicators**: Variables whose cyclical peaks and troughs consistently precede aggregate GDP turning points by 3 to 12 months. Key leading indicators include:
  - New manufacturing export orders.
  - Housing permits and residential building starts.
  - Stock market equity indices (e.g., S&P 500).
  - Yield curve term spread (10-year Treasury bond yield minus 3-month Treasury bill yield).
  - Consumer confidence and manufacturer sentiment surveys (PMI).
- **Coincident Indicators**: Variables that move in tandem with aggregate GDP (industrial production, real personal income less transfers, non-farm payroll employment, retail trade sales).
- **Lagging Indicators**: Variables that reach turning points several months after the economy has already turned (average duration of unemployment, prime lending rates, commercial loan balances, unit labor costs).

### 2. The Conference Board Aggregation Algorithm
The composite leading index is constructed through standardized steps:
1. Compute period-to-period percent changes $r_{it}$ for each component series.
2. Standardize each component by dividing by its long-run historical standard deviation $s_i$:
   $$v_{it} = \\frac{r_{it}}{s_i}$$
3. Compute the unweighted or weighted average of the standardized movements:
   $$R_t = \\sum_{i=1}^{m} w_i v_{it}$$
4. Standardize the composite sum $R_t$ and chain-link it to create the continuous Composite Leading Indicator index.

### 3. Hamilton's Markov-Switching Business Cycle Model
In 1989, James Hamilton formulated a non-linear regime-switching model capturing the asymmetric dynamics of expansions and contractions:

$$Y_t = \\mu_{S_t} + \\phi (Y_{t-1} - \\mu_{S_{t-1}}) + \\epsilon_t$$

where $S_t \\in \\{0, 1\\}$ is an unobserved discrete state variable:
- $S_t = 0$: Economic Contraction / Recession (with mean growth $\\mu_0 < 0$).
- $S_t = 1$: Economic Expansion / Boom (with mean growth $\\mu_1 > 0$).

The transition between regimes follows a first-order Markov chain governed by constant transition probabilities:
$$p_{00} = P(S_t = 0 \\mid S_{t-1} = 0), \\quad p_{11} = P(S_t = 1 \\mid S_{t-1} = 1)$$

Using maximum likelihood via the Hamilton filter, economists calculate the real-time probability that an economy has slipped into recession: $P(S_t = 0 \\mid \\Omega_t)$, providing policymakers with objective probabilistic recession nowcasts.
"""

# ----------------------------------------------------
# UNIT 5 DEEPENING
# ----------------------------------------------------
u5_deep = """
---

## Multidimensional Poverty Measurement: The Alkire-Foster Method

Traditional poverty measurement relied exclusively on unidimensional monetary indicators: whether a household's income or consumption expenditure falls below a monetary threshold $z$. However, as Nobel laureate Amartya Sen emphasized in his **Capabilities Approach**, poverty is inherently multidimensional: an individual may enjoy income above the subsistence line but suffer from severe deprivations in clean drinking water, basic healthcare, literacy, sanitation, and electrical energy.

To operationalize multidimensional poverty, Sabina Alkire and James Foster (2011) developed the **Alkire-Foster Method**, which underpins the United Nations Development Programme's global **Multidimensional Poverty Index (MPI)**.

### 1. The Dual-Cutoff Identification System
Consider an achievement matrix $X$ of size $N \\times D$, where $x_{ij}$ denotes the achievement of individual $i$ in dimension $j$ ($j = 1, \\dots, D$).
Each dimension has an explicit deprivation cutoff $z_j$ and an importance weight $w_j$ satisfying $\\sum_{j=1}^{D} w_j = 1$.

- **First Cutoff (Within-Dimension Deprivation Cutoff $z_j$)**:
  Individual $i$ is deprived in dimension $j$ if $x_{ij} < z_j$.
  We construct the deprivation matrix $g^0$ where:
  $$g_{ij}^0 = \\begin{cases} 1, & \\text{if } x_{ij} < z_j \\\\ 0, & \\text{if } x_{ij} \\ge z_j \\end{cases}$$
- **Deprivation Score ($c_i$)**:
  The weighted deprivation score for individual $i$ is:
  $$c_i = \\sum_{j=1}^{D} w_j g_{ij}^0, \\quad c_i \\in [0, 1]$$
- **Second Cutoff (Cross-Dimensional Poverty Cutoff $k$)**:
  An individual is identified as **Multidimensionally Poor** if their total weighted deprivation score equals or exceeds the cross-dimensional threshold $k$ (e.g., $k = 0.33$ or $33\\%$ of dimensions):
  $$i \\in \\text{Poor} \\iff c_i \\ge k$$

We construct the **Censored Deprivation Score** $c_i(k)$:
$$c_i(k) = \\begin{cases} c_i, & \\text{if } c_i \\ge k \\\\ 0, & \\text{if } c_i < k \\end{cases}$$
Deprivations of non-poor individuals are censored to zero.

### 2. The Alkire-Foster Aggregation Metrics
1. **Multidimensional Headcount Ratio ($H$)**:
   The proportion of the population identified as multidimensionally poor:
   $$H = \\frac{q_k}{N}$$
   where $q_k$ is the number of individuals with $c_i \\ge k$.
2. **Average Intensity of Poverty ($A$)**:
   The average proportion of dimensions in which poor individuals are deprived:
   $$A = \\frac{\\sum_{i=1}^{N} c_i(k)}{q_k}$$
3. **Adjusted Headcount Ratio ($M_0$ / MPI)**:
   The foundational Alkire-Foster poverty index is the product of incidence ($H$) and intensity ($A$):
   $$M_0 = H \\times A = \\frac{1}{N} \\sum_{i=1}^{N} c_i(k)$$

### 3. Dimensional Decomposition of $M_0$
A vital mathematical property of $M_0$ is that it is strictly decomposable by dimension.
The censored headcount ratio for dimension $j$, denoted $h_j$, is the proportion of the total population that is both multidimensionally poor and deprived in dimension $j$:

$$h_j = \\frac{1}{N} \\sum_{i=1}^{N} g_{ij}^0(k)$$

The overall index $M_0$ is an exact weighted sum of the dimensional censored headcounts:

$$M_0 = \\sum_{j=1}^{D} w_j h_j$$

The percentage contribution of dimension $j$ to national multidimensional poverty is:

$$\\text{Contribution}_j = \\frac{w_j h_j}{M_0} \\times 100\\%$$

This allows planners to identify whether national poverty is primarily fueled by lack of educational schooling, child malnutrition, or lack of clean water infrastructure, directly informing targeted sectoral investments.
"""

# ----------------------------------------------------
# UNIT 6 DEEPENING
# ----------------------------------------------------
u6_deep = """
---

## Environmental Accounting and Green GDP: The SEEA Framework

Conventional GDP measures aggregate economic output without subtracting the environmental degradation and natural capital depletion generated during the production process. If a nation clear-cuts its primary ancient forests, exhausts its subsoil petroleum reserves, and pollutes its river basins, conventional GDP registers substantial positive economic growth (from timber sales, oil extraction, and water filtration contracts), ignoring that the nation's underlying natural asset base has been depleted.

To rectify this flaw, the United Nations, European Commission, OECD, and World Bank developed the **System of Environmental-Economic Accounting (SEEA 2012)**.

### 1. Conceptual Framework of Green GDP
Green national accounting deducts the consumption of natural capital alongside the depreciation of man-made physical capital:

$$\\text{Environmentally Adjusted Domestic Product (EDP / Green GDP)} = \\text{GDP} - \\text{CFC} - \\text{DNC} - \\text{DEG}$$

where:
- $\\text{CFC}$: Consumption of Fixed Capital (physical depreciation of buildings, machinery).
- $\\text{DNC}$: Depletion of Natural Capital (the monetary value of extracted non-renewable resources such as minerals, oil, gas, and unsustainable extraction of timber and groundwater).
- $\\text{DEG}$: Environmental Degradation (the estimated monetary cost of residual emissions into air, soil, and water, encompassing carbon emissions, toxic effluents, and biodiversity loss).

### 2. Adjusted Net Savings (Genuine Savings)
Pioneered by the World Bank, **Adjusted Net Savings (ANS)**, also known as **Genuine Savings**, assesses whether an economy is pursuing sustainable development or consuming its long-term wealth:

$$\\text{ANS} = \\text{Gross National Savings} - \\text{CFC} + \\text{Education Expenditure} - \\text{Depletion of Energy} - \\text{Depletion of Minerals} - \\text{Net Forest Depletion} - \\text{Carbon Damage}$$

- **Education Expenditure** is added back as an investment in human capital rather than current consumption.
- If $\\text{ANS} > 0$, the economy's total wealth (physical + human + natural capital) is expanding, ensuring sustainable living standards for future generations.
- If $\\text{ANS} < 0$, the economy is liquidating its capital base to finance current consumption, heading toward long-run impoverishment.

---

## Measuring the Digital Economy and "Free" Digital Goods

A major challenge confronting contemporary national accounting is the **Digital Valuation Paradox**: consumers receive immense daily utility from free digital search engines, email, digital maps, open-source software, and video communication platforms, yet these services enter GDP only through advertising revenues or zero-value household consumption.

### The Limits of the SNA Production Boundary
In the System of National Accounts, GDP is restricted to market transactions with monetary prices or explicit barter exchanges. Non-market goods provided free of charge to households enter GDP only when produced by governments or non-profit institutions at cost.

When an internet platform provides free smartphone navigation services financed by digital advertising:
- The advertising expenditures paid by corporate sponsors are classified as **Intermediate Consumption** by the sponsor firms.
- Intermediate consumption is subtracted in the value-added calculation.
- Consequently, free digital consumer services do not directly enter final household consumption expenditure ($C$), creating an apparent wedge between measured real GDP growth and observed technological welfare gains.

### Proposed Valuation Methodologies:
1. **Welfare-Based Valuation (GDP-B)**:
   Erik Brynjolfsson and Avinash Collis (2019) proposed **GDP-B**, which uses massive online discrete choice willingness-to-accept experiments to quantify the direct consumer surplus generated by zero-price digital platforms (e.g., finding the median compensation consumers require to give up access to search engines for a month).
2. **Time-Use Valuation**:
   Imputing the monetary value of digital leisure time based on the opportunity cost of foregone wage labor.
"""

# ----------------------------------------------------
# UNIT 7 DEEPENING
# ----------------------------------------------------
u7_deep = """
---

## Environmentally Extended Input-Output (EEIO) Analysis

In environmental economics and climate policy, **Environmentally Extended Input-Output (EEIO) Analysis** integrates macroeconomic input-output tables with physical environmental satellite accounts. This allows researchers to trace greenhouse gas emissions, water withdrawals, and energy footprints through inter-industry supply chains from primary extraction to final retail consumption.

### 1. Mathematical Formulation of the EEIO Model
Let $e = [e_1, e_2, \\dots, e_n]^T$ denote the vector of **Direct Environmental Intensity Coefficients**, where $e_j$ represents direct physical emissions (e.g., metric tons of $\\text{CO}_2$ equivalent) released per unit of gross monetary output in sector $j$:

$$e_j = \\frac{E_j}{X_j}$$

where $E_j$ is the total physical emissions generated directly by industry $j$.

In the Leontief system, gross output is determined by final demand: $X = (I - A)^{-1} F$.
The total physical emissions $T_E$ generated across the entire economy to satisfy final demand vector $F$ is:

$$T_E = e^T X = e^T (I - A)^{-1} F$$

Defining the **Embodied Emissions Multiplier Vector** as:

$$\\epsilon^T = e^T (I - A)^{-1}$$

Each element $\\epsilon_j$ represents the total direct plus upstream indirect greenhouse gas emissions generated across all supplier industries per dollar of final demand for the output of sector $j$.

### 2. Production-Based vs Consumption-Based Accounting
The EEIO framework provides the mathematical foundation for distinguishing between:
- **Production-Based Emissions (Territorial Emissions)**:
  Emissions physically released within domestic sovereign boundaries:
  $$\\text{Emissions}_{\\text{prod}} = \\sum_{j=1}^{n} E_j = e^T X$$
- **Consumption-Based Emissions (Carbon Footprint)**:
  Emissions embodied in the final goods and services consumed by domestic residents, regardless of where in the world the physical emissions occurred:
  $$\\text{Emissions}_{\\text{cons}} = e^T (I - A)^{-1} F_{\\text{domestic}} + \\epsilon_{\\text{imported}}^T M_{\\text{final}}$$

#### Carbon Leakage and Policy Implications:
Developed economies often demonstrate declining domestic territorial emissions while their consumption-based carbon footprints continue to expand, due to the outsourcing of energy-intensive manufacturing to developing nations. Consumption-based EEIO modeling underpins modern trade instruments such as the European Union's **Carbon Border Adjustment Mechanism (CBAM)**, ensuring that imported steel, cement, and fertilizers bear the same carbon cost as domestic production.

---

## Dynamic Input-Output Modeling: The Leontief Dynamic System

The classical static Leontief model treats capital investment as an exogenous component of final demand. In reality, capital goods (machinery, factory buildings, transport equipment) are produced by industries within the economy to expand future productive capacity.

To endogenize investment, Wassily Leontief (1953) formulated the **Dynamic Input-Output Model**:

$$X_t = A X_t + B (X_{t+1} - X_t) + C_t$$

where:
- $X_t$ is gross output in year $t$.
- $A$ is the standard technical intermediate coefficients matrix.
- $C_t$ is non-capital final consumption demand.
- $B$ is the $n \\times n$ **Capital Coefficients Matrix**, where $b_{ij}$ denotes the quantity of capital good $i$ required per unit expansion in the productive capacity of sector $j$:
  $$b_{ij} = \\frac{K_{ij}}{\\Delta X_j}$$

Rearranging into a matrix difference equation:

$$(I - A + B) X_t - B X_{t+1} = C_t$$

Solving this system of second-order matrix difference equations reveals the economy's optimal multi-sector investment trajectory and validates the **Turnpike Theorems** of dynamic general equilibrium: to achieve maximum long-run growth, the economy must converge to a balanced expansion path determined by the dominant eigenvalue of the capital-technology system.
"""

# ----------------------------------------------------
# UNIT 8 DEEPENING
# ----------------------------------------------------
u8_deep = """
---

## Dynamic Market Equilibria: The Cobweb Model and Price Oscillations

In many agricultural and raw commodity markets, production decisions require an extended biological gestation period: farmers decide how many acres of crops to plant or livestock to breed based on current market prices, but the resulting harvest output cannot reach the market until the following season. This temporal production lag produces dynamic price-quantity oscillations formalized by the **Cobweb Theorem** (Mordecai Ezekiel, 1938).

### 1. Mathematical Formulation
Consider a market with an instantaneous linear demand curve and a lagged linear supply curve:

$$\\text{Demand}: \\quad Q_t^D = \\alpha - \\beta P_t, \\quad \\beta > 0$$
$$\\text{Supply}: \\quad Q_t^S = -\\gamma + \\delta P_{t-1}, \\quad \\delta > 0$$

In competitive market clearing at period $t$, quantity demanded must equal quantity supplied:

$$Q_t^D = Q_t^S \\implies \\alpha - \\beta P_t = -\\gamma + \\delta P_{t-1}$$

Rearranging yields a first-order linear difference equation in market price $P_t$:

$$P_t = -\\left( \\frac{\\delta}{\\beta} \\right) P_{t-1} + \\frac{\\alpha + \\gamma}{\\beta}$$

### 2. Long-Run Equilibrium and Stability Analysis
The long-run static equilibrium price $P^*$ satisfies $P_t = P_{t-1} = P^*$:

$$P^* = \\frac{\\alpha + \\gamma}{\\beta + \\delta}$$

Subtracting $P^*$ from the dynamic difference equation defines the deviation $p_t = P_t - P^*$:

$$p_t = -\\left( \\frac{\\delta}{\\beta} \\right) p_{t-1}$$

Iterating backwards from an initial price displacement $p_0$:

$$p_t = \\left( -\\frac{\\delta}{\\beta} \\right)^t p_0$$

Because the base ratio $(-\\delta / \\beta)$ is strictly negative, the price trajectory inevitably alternates signs from period to period, producing cyclical oscillations around the equilibrium.

#### Three Stability Regimes:
1. **Convergent (Damped) Cobweb**: $\\delta < \\beta \\iff |-\\delta/\\beta| < 1$.
   The supply curve is steeper than the demand curve ($|dQ^S/dP| < |dQ^D/dP|$). Price oscillations dampen over time, spiraling inward toward equilibrium $P^*$.
2. **Divergent (Explosive) Cobweb**: $\\delta > \\beta \\iff |-\\delta/\\beta| > 1$.
   The supply curve is flatter than the demand curve. Price fluctuations amplify progressively outward, destabilizing the market.
3. **Continuous (Perpetual) Cobweb**: $\\delta = \\beta \\iff |-\\delta/\\beta| = 1$.
   The system cycles indefinitely in a closed rectangular loop with constant amplitude.

---

## Simultaneous Equation Estimation: Two-Stage Least Squares (2SLS)

As established by Working's identification problem, estimating market demand and supply equations via Ordinary Least Squares yields biased and inconsistent estimates due to the simultaneity of price and quantity: price is endogenous ($E[P_t u_t] \\ne 0$).

To consistently estimate structural demand and supply parameters, econometricians deploy **Two-Stage Least Squares (2SLS)** with instrumental variables.

### The Structural Demand-Supply System
Consider an agricultural commodity market:

$$\\text{Demand}: \\quad Q_t = \\alpha_0 + \\alpha_1 P_t + \\alpha_2 Y_t + u_t$$
$$\\text{Supply}: \\quad Q_t = \\beta_0 + \\beta_1 P_t + \\beta_2 W_t + v_t$$

where:
- $Q_t$ (quantity) and $P_t$ (price) are endogenous variables.
- $Y_t$ (consumer income) is an exogenous demand-shifter.
- $W_t$ (weather rainfall index or fertilizer cost) is an exogenous supply-shifter.

### The Two-Stage Estimation Algorithm:
1. **Stage 1: Reduced-Form Regression**:
   Regress the endogenous price $P_t$ on all exogenous variables in the entire system ($Y_t$ and $W_t$) using OLS:
   $$P_t = \\pi_0 + \\pi_1 Y_t + \\pi_2 W_t + \\nu_t$$
   Compute the fitted (predicted) values:
   $$\\hat{P}_t = \\hat{\\pi}_0 + \\hat{\\pi}_1 Y_t + \\hat{\\pi}_2 W_t$$
   The predicted price $\\hat{P}_t$ captures only the exogenous variation in price driven by weather and income, purging the correlation with the structural demand disturbance $u_t$.
2. **Stage 2: Structural Estimation**:
   Replace the endogenous price $P_t$ with its fitted instrument $\\hat{P}_t$ in the structural demand equation and estimate via OLS:
   $$Q_t = \\alpha_0 + \\alpha_1 \\hat{P}_t + \\alpha_2 Y_t + u_t^*$$

The resulting 2SLS estimator $\\hat{\\alpha}_1$ is asymptotically consistent, providing unbiased estimates of true market demand price elasticity.
"""

deepeners = {
    2: u2_deep,
    3: u3_deep,
    4: u4_deep,
    5: u5_deep,
    6: u6_deep,
    7: u7_deep,
    8: u8_deep,
}

for unit_num, deep_text in deepeners.items():
    file_path = OUT_DIR / f"unit-{unit_num}.md"
    content = file_path.read_text(encoding="utf-8")
    new_content = inject_before_worked_questions(content, deep_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Unit {unit_num} deepened: {prose_count(new_content)} words")
