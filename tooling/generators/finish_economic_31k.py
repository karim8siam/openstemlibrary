#!/usr/bin/env python3
"""
Final push to bring Economic Statistics (Units 1 through 8) to >= 30,500 pure prose words.
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
# UNIT 2 FINAL EXPANSION
# ----------------------------------------------------
u2_final = """
---

## Multilateral Index Systems: Geary-Khamis and EKS Methods

When comparing price levels and real purchasing power across three or more countries simultaneously, standard bilateral index numbers (such as Fisher or Törnqvist) fail because they violate the **Transitivity (Circular) Property**: $P_{A/B} \\times P_{B/C} \\ne P_{A/C}$.
To produce consistent, transitively closed international comparisons without base-country dependency, the United Nations International Comparison Program (ICP) deploys multilateral index number systems.

### 1. The Eltetö-Köves-Szulc (EKS) Method
Formulated independently by Ödön Éltető and Péter Köves (1964) and Bohdan Szulc (1964), the **EKS Method** constructs a transitive multilateral price index matrix from an underlying system of non-transitive bilateral Fisher ideal indices $F_{j/k}$.

The EKS index between country $j$ and country $k$ is defined as the geometric mean of all indirect Fisher comparisons routed through every participating country $r$ ($r = 1, \\dots, M$):

$$P_{j/k}^{\\text{EKS}} = \\left[ \\prod_{r=1}^{M} \\left( F_{j/r} \\times F_{r/k} \\right) \\right]^{1/M} = \\left[ \\prod_{r=1}^{M} \\left( \\frac{F_{j/r}}{F_{k/r}} \\right) \\right]^{1/M}$$

The EKS method minimizes the logarithmic distance between the transitive multilateral indices and the underlying bilateral Fisher indices:
$$\\min \\sum_{j=1}^{M} \\sum_{k=1}^{M} \\left( \\ln(P_{j/k}^{\\text{EKS}}) - \\ln(F_{j/k}) \\right)^2$$
The EKS index satisfies transitivity, base-country invariance, and characteristicity, making it the preferred metric for international poverty comparisons and GDP per capita rankings across OECD and Eurostat member nations.

### 2. The Geary-Khamis (GK) System
Pioneered by R. C. Geary (1958) and Salem Khamis (1970), the **Geary-Khamis System** determines an international set of average commodity prices $\\pi_i$ and country purchasing power parities $\\text{PPP}_j$ simultaneously through a coupled system of linear equations:

1. **International Price of Commodity $i$**:
   $$\\pi_i = \\sum_{j=1}^{M} \\left( \\frac{p_{ij}}{\\text{PPP}_j} \\right) \\left( \\frac{q_{ij}}{\\sum_{k=1}^{M} q_{ik}} \\right)$$
   The international price $\\pi_i$ is a quantity-weighted average of the purchasing-power-adjusted national prices of commodity $i$ across all countries.
2. **Purchasing Power Parity of Country $j$**:
   $$\\text{PPP}_j = \\frac{\\sum_{i=1}^{n} p_{ij} q_{ij}}{\\sum_{i=1}^{n} \\pi_i q_{ij}}$$
   The PPP of country $j$ is the ratio of its domestic expenditure evaluated at local prices to its expenditure evaluated at international prices.

The GK system guarantees **Additive Consistency**: the sum of real expenditures on individual goods equals total real GDP. However, it imparts an upward Gerschenkron substitution bias to lower-income economies, because international prices reflect the consumption structures of rich nations.

---

## Owner-Occupied Housing in Consumer Price Indices

A persistent source of international divergence in CPI methodology is the statistical treatment of **Owner-Occupied Housing (OOH)**. A residential dwelling is simultaneously a physical capital asset providing long-term investment returns and a provider of flow consumer shelter services.

Statistical agencies resolve this dual nature using three alternative conceptual models:
1. **The Rental Equivalence (Implicit Rent) Approach**:
   Adopted by the United States Bureau of Labor Statistics, this approach imputes the consumption value of shelter by measuring what owner-occupants would pay to rent an equivalent market home in their neighborhood. It relies on representative rental housing surveys.
2. **The User Cost Approach**:
   Measures the net cost of owning and occupying a home, comprising mortgage interest, property taxes, homeowner insurance, maintenance, and capital depreciation, minus expected capital appreciation. While theoretically grounded in neoclassical capital theory, it introduces high volatility during real estate price swings.
3. **The Net Acquisition Approach**:
   Adopted by Eurostat for the Harmonized Index of Consumer Prices (HICP), this approach treats housing as a durable good, measuring the net purchase price of newly constructed residential dwellings, architectural fees, and major renovations, excluding purchases of existing land.
"""

# ----------------------------------------------------
# UNIT 3 FINAL EXPANSION
# ----------------------------------------------------
u3_final = """
---

## State-Space Representation and Kalman Filtering in Trend Estimation

While classical moving averages and polynomial trends operate as static descriptive smoothers, modern macroeconomic forecasting relies on **State-Space Models** and the **Kalman Filter** (Rudolf E. Kálmán, 1960). State-space models treat secular trend and seasonality as unobserved dynamic state variables that evolve stochastically over time, updating parameter estimates recursively as new real-time economic data arrive.

### 1. The Local Linear Trend Model
In Andrew Harvey's structural time series framework, a univariate economic series $Y_t$ is decomposed into an unobserved stochastic level $\\mu_t$ and a stochastic slope $\\beta_t$:

- **Measurement (Observation) Equation**:
  $$Y_t = \\mu_t + \\epsilon_t, \\quad \\epsilon_t \\sim \\text{NID}(0, \\sigma_\\epsilon^2)$$
  The observed economic variable $Y_t$ reflects the true underlying trend level $\\mu_t$ plus irregular white-noise measurement error $\\epsilon_t$.
- **State Transition Equations**:
  $$\\mu_{t+1} = \\mu_t + \\beta_t + \\eta_t, \\quad \\eta_t \\sim \\text{NID}(0, \\sigma_\\eta^2)$$
  $$\\beta_{t+1} = \\beta_t + \\zeta_t, \\quad \\zeta_t \\sim \\text{NID}(0, \\sigma_\\zeta^2)$$
  The trend level advances by the slope increment $\\beta_t$ plus an unexpected level shock $\\eta_t$. The slope parameter itself evolves as a random walk driven by slope disturbances $\\zeta_t$.

### 2. Recursive Kalman Filter Algorithm
The Kalman filter estimates the optimal conditional expectation of the unobserved state vector $\\alpha_t = [\\mu_t, \\beta_t]^T$ given information available up to time $t-1$ (prediction step) and updates it once $Y_t$ is observed (correction step):

1. **Prediction Step**:
   $$\\alpha_{t|t-1} = T \\alpha_{t-1|t-1}$$
   $$P_{t|t-1} = T P_{t-1|t-1} T^T + Q$$
   where $T = \\begin{bmatrix} 1 & 1 \\\\ 0 & 1 \\end{bmatrix}$, $P$ is the state error covariance matrix, and $Q = \\text{diag}(\\sigma_\\eta^2, \\sigma_\\zeta^2)$ is the disturbance covariance matrix.
2. **Measurement Prediction Error (Innovation)**:
   $$v_t = Y_t - Z \\alpha_{t|t-1}, \\quad F_t = Z P_{t|t-1} Z^T + \\sigma_\\epsilon^2$$
   where $Z = [1, \\; 0]$.
3. **Updating Step (Kalman Gain Correction)**:
   $$K_t = P_{t|t-1} Z^T F_t^{-1}$$
   $$\\alpha_{t|t} = \\alpha_{t|t-1} + K_t v_t$$
   $$P_{t|t} = (I - K_t Z) P_{t|t-1}$$

The **Kalman Gain ($K_t$)** dictates how heavily the filter adjusts the estimated secular trend in response to real-time surprise innovations $v_t$. If measurement noise is high ($\\sigma_\\epsilon^2$ large), $K_t$ is small, and the filter smooths through the shock. If trend volatility is high, $K_t$ is large, allowing the trend line to bend quickly to structural economic transitions.
"""

# ----------------------------------------------------
# UNIT 4 FINAL EXPANSION
# ----------------------------------------------------
u4_final = """
---

## Real-Time Macroeconomic Nowcasting with Mixed-Frequency Data

Central banks and economic ministries face a persistent informational timing mismatch: while key macroeconomic aggregates like Gross Domestic Product (GDP) are published with a lag of several months and only at quarterly frequencies, financial markets, industrial sensors, and consumer transaction systems generate daily, weekly, and monthly data in real time.
To bridge this gap, modern economic statistics deploys **Macroeconomic Nowcasting**.

### 1. Mixed Data Sampling (MIDAS) Regressions
Introduced by Eric Ghysels (2004), **MIDAS Regressions** allow researchers to regress a low-frequency dependent variable (quarterly GDP growth, $Y_t$) directly on high-frequency explanatory variables (monthly industrial production, weekly unemployment claims, daily bond yields, $X_t^{(m)}$) without first aggregating the high-frequency series into arbitrary quarterly averages.

A standard MIDAS model is formulated as:

$$Y_t = \\beta_0 + \\beta_1 B(L^{1/m}; \\theta) X_t^{(m)} + \\epsilon_t$$

where:
- $L^{1/m}$ is a fractional lag operator such that $L^{j/m} X_t^{(m)} = X_{t - j/m}^{(m)}$.
- $B(L^{1/m}; \\theta) = \\sum_{j=0}^{K} w(j; \\theta) L^{j/m}$ is a distributed lag polynomial governed by a parsimonious parameter vector $\\theta$.
- Common weighting functions include the **Exponential Almon Polynomial**:
  $$w(j; \\theta_1, \\theta_2) = \\frac{\\exp(\\theta_1 j + \\theta_2 j^2)}{\\sum_{k=0}^{K} \\exp(\\theta_1 k + \\theta_2 k^2)}$$
  and the **Beta Density Lag Function**.

By estimating smooth non-linear lag weights, MIDAS extracts predictive signals from the most recent high-frequency intra-quarter data points, updating the nowcast of current-quarter GDP as new high-frequency data arrive.

### 2. Dynamic Factor Models (DFM)
Formalized by Domenico Giannone, Lucrezia Reichlin, and David Small (2008), the **Dynamic Factor Model (DFM)** extracts a small number of unobserved common macroeconomic latent factors $f_t$ from hundreds of heterogeneous economic time series:

$$X_{i,t} = \\lambda_i^T f_t + e_{i,t}$$
$$f_t = A f_{t-1} + u_t$$

where $\\lambda_i$ is the factor loading vector and $e_{i,t}$ is idiosyncratic series-specific noise.
Using state-space Kalman filtering under missing data patterns ("ragged edges"), the DFM processes incoming monthly and weekly economic news releases, continuously computing the news contribution of each statistical release to the updated GDP estimate.
"""

# ----------------------------------------------------
# UNIT 5 FINAL EXPANSION
# ----------------------------------------------------
u5_final = """
---

## Inequality of Opportunity and the Roemer Analytical Framework

In modern welfare economics and social justice theory, economists distinguish between inequality of outcomes (disparities in observed income or wealth) and **Inequality of Opportunity**. Pioneered by John Roemer (1998) and operationalized by François Bourguignon, Francisco Ferreira, and Vito Peragine, this framework partitions the determinants of an individual's economic success into two distinct categories:

1. **Circumstance Variables ($C$)**: Factors entirely outside an individual's personal control, determined at birth or during childhood. These encompass parental educational attainment, parental socioeconomic status, geographic birth region, race, gender, and inherited wealth.
2. **Effort Variables ($E$)**: Factors that are within the realm of individual agency, personal choices, and voluntary decisions—such as hours worked, educational investment, career occupational choice, and willingness to assume entrepreneurial risk.

### Mathematical Formulation
Let an individual's income $y$ be determined by circumstances $C$, efforts $E$, and unobserved luck $u$:

$$y = g(C, E, u)$$

To measure inequality of opportunity:
- Society is partitioned into $M$ mutually exclusive **Types**, where all individuals within type $m$ share the exact same circumstance profile $C_m$.
- Under the principle of **Equality of Opportunity**, disparities in income between types (attributable to circumstances) are ethically objectionable and represent social injustice, whereas disparities within a type (attributable to varying effort) are ethically legitimate.

### Measuring the Opportunity Share
Using the Mean Log Deviation ($GE(0) = MLD$), which is perfectly sub-group decomposable:

$$MLD(y) = MLD_{\\text{within}} + MLD_{\\text{between}}$$

The between-type inequality $MLD_{\\text{between}}$ is computed by replacing each individual's observed income with the average income of their circumstance type $\\bar{y}_m$:

$$MLD_{\\text{between}} = \\sum_{m=1}^{M} \\left( \\frac{N_m}{N} \\right) \\ln\\left( \\frac{\\mu}{\\bar{y}_m} \\right)$$

The **Inequality of Opportunity Ratio ($IOp$)** is defined as:

$$IOp = \\frac{MLD_{\\text{between}}}{MLD(y)} \\times 100\\%$$

In empirical studies across developing economies, between 30% and 60% of total national income inequality is directly attributable to circumstance variables determined at birth, demonstrating that high headline inequality largely reflects structural inequality of opportunity rather than differential effort.

---

## Intergenerational Income Mobility and the Great Gatsby Curve

Complementing static inequality metrics, **Intergenerational Income Mobility** measures the degree to which an individual's economic status is determined by the economic position of their parents.

### 1. The Intergenerational Income Elasticity (IGE)
The standard empirical model of intergenerational mobility regresses the log of child's adult permanent income ($y_{\\text{child}}$) on the log of parental income ($y_{\\text{parent}}$):

$$\\ln(y_{\\text{child}}) = \\alpha + \\beta \\ln(y_{\\text{parent}}) + \\epsilon$$

The parameter $\\beta$ is the **Intergenerational Income Elasticity (IGE)**:
- $\\beta = 0$: Complete intergenerational mobility (a child's expected adult income is entirely independent of parental wealth; complete equality of opportunity).
- $\\beta = 1$: Complete intergenerational immobility (a child's income reproduces their parents' position with zero social fluidity).
- Intergenerational Mobility is measured as $1 - \\beta$. In egalitarian societies (Denmark, Norway), $\\beta \\approx 0.15$ to $0.20$. In highly immobile societies (United States, United Kingdom, Brazil), $\\beta \\approx 0.45$ to $0.60$.

### 2. The Great Gatsby Curve
Named by Alan Krueger in 2012, the **Great Gatsby Curve** maps the empirical cross-national relationship between static income inequality (measured by the Gini coefficient) on the horizontal axis and intergenerational income persistence (measured by IGE, $\\beta$) on the vertical axis.
The curve reveals a strong, positive empirical correlation: nations with higher static income inequality systematically exhibit lower intergenerational social mobility. When income gaps between social strata widen, wealthy families invest vastly greater resources in private schooling, elite tutoring, social networks, and bequest capital, cementing advantage across generations and locking disadvantaged children into persistent poverty traps.
"""

# ----------------------------------------------------
# UNIT 6 FINAL EXPANSION
# ----------------------------------------------------
u6_final = """
---

## Comprehensive Wealth Accounting: The Inclusive Wealth Framework

While Gross Domestic Product measures current annual flows of production and income, it provides zero direct indication of an economy's long-term sustainability or capital accumulation. An economy can post high annual GDP growth by exhausting finite mineral wealth, depleting groundwater tables, and degrading ecological biomes—generating transient consumption at the cost of catastrophic future impoverishment.

To establish a comprehensive balance sheet of national prosperity, the United Nations Environment Programme (UNEP) and leading economists (Kenneth Arrow, Partha Dasgupta) developed the **Inclusive Wealth Index (IWI)**.

### The Four Pillars of Comprehensive Capital Stock
Comprehensive Wealth ($W$) is defined as the total social value of all capital assets owned by a nation:

$$W = K_{\\text{produced}} + K_{\\text{human}} + K_{\\text{natural}} + K_{\\text{social}}$$

1. **Produced (Manufactured) Capital ($K_{\\text{produced}}$)**:
   Physical infrastructure, machinery, commercial and residential buildings, transport logistics, and telecommunications hardware. Valued via the perpetual inventory method (PIM) at replacement cost.
2. **Human Capital ($K_{\\text{human}}$)**:
   The economic value embodied in the population's knowledge, skills, educational attainment, health, and productive working life. Formally estimated using the **Jorgenson-Fraumeni Lifetime Income Approach**, calculating the discounted present value of expected future lifetime labor market earnings:
   $$K_{\\text{human}} = \\sum_{a=0}^{A} N_a \\sum_{t=a}^{T} \\frac{w_t \\cdot P(t \\mid a)}{(1 + r)^{t-a}}$$
   where $w_t$ is the expected wage at age $t$, $P(t \\mid a)$ is the survival probability, and $r$ is the social discount rate.
3. **Natural Capital ($K_{\\text{natural}}$)**:
   The discounted monetary value of non-renewable fossil energy reserves, subsoil mineral ores, renewable timber stocks, agricultural soil productivity, freshwater aquifers, and critical ecosystem services (carbon sequestration, pollination, flood attenuation).
4. **Social and Institutional Capital ($K_{\\text{social}}$)**:
   The efficiency of legal systems, rule of law, anti-corruption governance, contract enforcement, and civic trust that enable economic factors to operate productively.

---

## Quarterly National Accounts Benchmarking: The Denton Technique

National statistical offices face an unavoidable reconciliation dilemma in GDP measurement:
- **Quarterly GDP Series ($y_t$)**: Available rapidly, tracking timely business cycle turning points, but constructed from incomplete, preliminary sub-annual surveys and indicators.
- **Annual GDP Accounts ($Y_T$)**: Published with significant lag, but derived from comprehensive, audited enterprise censuses, administrative tax returns, and complete supply-use tables.

Inevitably, summing the preliminary quarterly estimates across four quarters diverges from the definitive annual census benchmark: $\\sum_{t=1}^{4} y_{T, t} \\ne Y_T$.
Simply scaling each quarter by a constant annual factor ($Y_T / \\sum y_t$) creates artificial, sharp discontinuities between the fourth quarter of one year and the first quarter of the subsequent year—a distortion known as the **Step Problem**.

### The Denton Proportional Benchmarking Formulation
To eliminate the step problem while preserving intra-annual cyclical movements, Canadian statistician Frank Denton (1971) formulated a constrained quadratic optimization algorithm.
Let $x_t$ represent the final reconciled quarterly benchmarked series, and let $y_t$ represent the preliminary quarterly indicator series. Denton's method minimizes the squared relative period-to-period differences in the adjustment ratios:

$$\\min_{\\{x_t\\}} \\sum_{t=2}^{4M} \\left[ \\frac{x_t}{y_t} - \\frac{x_{t-1}}{y_{t-1}} \\right]^2$$

subject to the strict annual aggregation constraints for every year $T = 1, \\dots, M$:

$$\\sum_{t=4T-3}^{4T} x_t = Y_T$$

By minimizing the curvature of the benchmark-to-indicator ratio ($x_t / y_t$), Denton's algorithm smoothly blends annual benchmark levels into the quarterly trajectory without distorting quarterly growth rates or introducing spurious jump discontinuities at calendar boundaries.
"""

# ----------------------------------------------------
# UNIT 7 FINAL EXPANSION
# ----------------------------------------------------
u7_final = """
---

## Structural Decomposition Analysis (SDA) in Input-Output Systems

To understand the fundamental driving forces behind historical changes in macroeconomic output, employment, carbon emissions, or water use over decades, economists deploy **Structural Decomposition Analysis (SDA)**.
In an input-output framework, total gross output in year $t$ is:

$$X_t = L_t F_t = (I - A_t)^{-1} F_t$$

Over an elapsed interval from base year $0$ to target year $t$, the total observed change in output is $\\Delta X = X_t - X_0$.

### Polar Structural Decomposition
Because both the technology matrix ($A$) and final demand ($F$) change simultaneously, the total differential decomposes into:

$$\\Delta X = X_t - X_0 = L_t F_t - L_0 F_0$$

Adding and subtracting the cross-product terms $L_t F_0$ or $L_0 F_t$ yields two alternative "polar" decompositions:

1. **First Polar Decomposition**:
   $$\\Delta X = (\\Delta L) F_0 + L_t (\\Delta F)$$
2. **Second Polar Decomposition**:
   $$\\Delta X = (\\Delta L) F_t + L_0 (\\Delta F)$$

To eliminate arbitrary path dependence, economists take the unweighted arithmetic mean of both polar formulations:

$$\\Delta X = \\frac{1}{2} (\\Delta L) (F_0 + F_t) + \\frac{1}{2} (L_0 + L_t) (\\Delta F)$$

where:
- $\\frac{1}{2} (\\Delta L) (F_0 + F_t)$ is the **Technological Change Effect**: Output expansion driven by structural shifts in inter-industry input efficiency, supply-chain restructuring, and material substitution.
- $\\frac{1}{2} (L_0 + L_t) (\\Delta F)$ is the **Final Demand Effect**: Output expansion driven by changes in consumer tastes, government investment programs, and export demand.

### Further Decomposition of the Final Demand Effect:
The final demand shift $\\Delta F$ can be further partitioned into:
- **Level Effect**: Growth in the aggregate volume of final demand (holding product composition constant).
- **Structure (Mix) Effect**: Reallocation of final consumption shares across sectors (e.g., shifts from fossil fuels to renewable energy).

Applied to national carbon inventories, Structural Decomposition Analysis allows policymakers to quantify whether rising emissions are driven by aggregate GDP expansion, consumer preference shifts, or changing industrial supply-chain carbon intensities.
"""

# ----------------------------------------------------
# UNIT 8 FINAL EXPANSION
# ----------------------------------------------------
u8_final = """
---

## Discrete Choice Demand Analysis: The McFadden Random Utility Model

In modern industrial economics, marketing science, and transportation planning, consumers do not choose continuous quantities of homogeneous goods along a smooth marginal utility curve. Instead, they choose a single, indivisible discrete alternative from a finite choice set (e.g., choosing whether to commute by personal automobile, subway, bus, or bicycle; or choosing which brand of smartphone to purchase).

To model these decisions, Nobel laureate Daniel McFadden (1974) developed the **Random Utility Maximization (RUM) Framework**.

### 1. Mathematical Formulation
Let consumer $n$ face a choice set of $J$ discrete alternatives: $\\mathcal{C} = \\{1, 2, \\dots, J\\}$.
The utility consumer $n$ derives from choosing alternative $i$ is decomposed into a deterministic systematic component $V_{ni}$ and a random idiosyncratic stochastic component $\\epsilon_{ni}$:

$$U_{ni} = V_{ni} + \\epsilon_{ni}$$

The systematic utility $V_{ni}$ is a linear function of observable attributes of the alternative (price $P_i$, travel time $T_i$, comfort quality $Q_i$) and socioeconomic characteristics of the consumer (income $M_n$, age, household size):

$$V_{ni} = \\beta^T X_{ni}$$

Consumer $n$ chooses alternative $i$ if and only if it provides the highest utility among all available options:

$$P_{ni} = P(U_{ni} > U_{nj} \\quad \\forall j \\ne i) = P(\\epsilon_{nj} - \\epsilon_{ni} < V_{ni} - V_{nj} \\quad \\forall j \\ne i)$$

### 2. The Multinomial Logit (MNL) Model
McFadden proved that if the random disturbances $\\epsilon_{ni}$ are independently and identically distributed according to the **Type I Extreme Value (Gumbel) Distribution**:
$$F(\\epsilon) = \\exp(-\\exp(-\\epsilon))$$

the choice probability takes the celebrated closed-form **Multinomial Logit (MNL)** formula:

$$P_{ni} = \\frac{\\exp(V_{ni})}{\\sum_{j=1}^{J} \\exp(V_{nj})} = \\frac{\\exp(\\beta^T X_{ni})}{\\sum_{j=1}^{J} \\exp(\\beta^T X_{nj})}$$

### 3. The Independence of Irrelevant Alternatives (IIA) Property
A fundamental mathematical property of the standard multinomial logit model is the **Independence of Irrelevant Alternatives (IIA)**: the ratio of the choice probabilities between any two alternatives $i$ and $k$ depends strictly on the attributes of those two options and is completely independent of the presence, absence, or attributes of any other alternative $j$:

$$\\frac{P_{ni}}{P_{nk}} = \\frac{\\frac{\\exp(V_{ni})}{\\sum \\exp(V_j)}}{\\frac{\\exp(V_{nk})}{\\sum \\exp(V_j)}} = \\frac{\\exp(V_{ni})}{\\exp(V_{nk})} = \\exp(V_{ni} - V_{nk})$$

#### The Red Bus / Blue Bus Paradox:
While computationally elegant, IIA imposes rigid, unrealistic cross-price substitution patterns. In McFadden's famous thought experiment, if commuters choose between driving a car ($P_{\\text{car}} = 0.50$) and taking a blue bus ($P_{\\text{blue}} = 0.50$), introducing a red bus that is identical to the blue bus in every respect should split the bus ridership equally, leaving car ridership at 50%. Under IIA, however, the model forces all three alternatives to equal 33.3%, erroneously predicting that the introduction of a red bus causes half of all drivers to abandon their cars.

To resolve IIA distortions, modern econometrics deploys the **Nested Logit Model** (grouping close substitutes into hierarchical branches) and the **Random Coefficients Mixed Logit Model (BLP: Berry, Levinsohn, and Pakes 1995)**, which allows consumer preference parameters $\\beta$ to vary continuously across the population, accommodating realistic, flexible cross-price elasticity matrices across differentiated product markets.
"""

finals = {
    2: u2_final,
    3: u3_final,
    4: u4_final,
    5: u5_final,
    6: u6_final,
    7: u7_final,
    8: u8_final,
}

for unit_num, final_text in finals.items():
    file_path = OUT_DIR / f"unit-{unit_num}.md"
    content = file_path.read_text(encoding="utf-8")
    new_content = inject_before_worked_questions(content, final_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Unit {unit_num} finalized: {prose_count(new_content)} words")
