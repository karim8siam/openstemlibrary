#!/usr/bin/env python3
"""
Final precision booster to drive Economic Statistics past 30,500 pure prose words.
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
# UNIT 2
# ----------------------------------------------------
u2_cross = """
---

## The Lloyd-Moulton Constant Elasticity of Substitution Price Index

While superlative index numbers (such as Fisher and Törnqvist) eliminate upper-level substitution bias by using expenditure weights from both the base and current periods, they suffer from an operational drawback for national statistical agencies: they can only be computed retrospectively after current-period expenditure surveys or national accounts data become available (often with a lag of one to two years).

To provide a real-time index that accommodates consumer substitution without requiring contemporaneous expenditure weights, P. J. Lloyd (1975) and Brent Moulton (1996) formulated the **Lloyd-Moulton CES Price Index**:

$$P_{\\text{LM}}(p_0, p_t, w_0; \\sigma) = \\left[ \\sum_{i=1}^{n} w_{i0} \\left( \\frac{p_{it}}{p_{i0}} \\right)^{1-\\sigma} \\right]^{\\frac{1}{1-\\sigma}}, \\quad \\sigma \\ne 1$$

where:
- $w_{i0}$ denotes the expenditure share of commodity $i$ in the base period ($w_{i0} = p_{i0} q_{i0} / \\sum p_{j0} q_{j0}$).
- $\\sigma \\ge 0$ is the constant elasticity of substitution across commodities within the consumer preference aggregator.

### Mathematical Limiting Properties:
1. **Zero Substitution ($\\sigma = 0$)**:
   When consumers exhibit zero willingness to substitute (Leontief fixed-coefficient preferences):
   $$P_{\\text{LM}}(p_0, p_t, w_0; 0) = \\sum_{i=1}^{n} w_{i0} \\left( \\frac{p_{it}}{p_{i0}} \\right) = P_{\\text{Laspeyres}}$$
   The Lloyd-Moulton index collapses exactly to the standard fixed-basket Laspeyres price index.
2. **Unitary Elasticity of Substitution ($\\sigma \\to 1$)**:
   By l'Hôpital's rule, as $\\sigma \\to 1$ (Cobb-Douglas preferences where expenditure shares remain invariant):
   $$\\lim_{\\sigma \\to 1} P_{\\text{LM}} = \\prod_{i=1}^{n} \\left( \\frac{p_{it}}{p_{i0}} \\right)^{w_{i0}} = P_{\\text{Geometric Laspeyres}}$$
3. **General Substitution ($0 < \\sigma < 1$)**:
   In empirical consumer expenditure systems, the aggregate upper-level elasticity of substitution typically falls in the range of $\\sigma \\approx 0.6$ to $0.8$. By estimating $\\sigma$ econometrically from historical panel data, statistical agencies can compute the Lloyd-Moulton index concurrently using only base weights $w_0$ and current prices $p_t$, producing an inflation metric that tracks the superlative Fisher index within hundredths of a percentage point in real time.
"""

# ----------------------------------------------------
# UNIT 4
# ----------------------------------------------------
u4_cross = """
---

## The Bry-Boschan Business Cycle Dating Algorithm

While parametric and econometric filters smooth time series, national statistical committees—most notably the NBER Business Cycle Dating Committee in the United States and the CEPR Business Cycle Dating Committee in Europe—formally date the peaks and troughs of economic business cycles using objective, non-parametric turning point algorithms. The international benchmark for programmatic cycle dating is the **Bry-Boschan Algorithm** (Gerhard Bry and Charlotte Boschan, 1971).

### 1. Algorithmic Architecture
Operating on seasonally adjusted monthly or quarterly time series (such as real personal income, industrial production, and payroll employment), the algorithm identifies local extrema through a hierarchical screening sequence:

1. **Step 1: Outlier Replacement and Extreme Value Smoothing**:
   Spurious spikes attributable to severe weather strikes or statistical anomalies are identified via a Spencer moving average and replaced with modified values.
2. **Step 2: Initial Turning Point Identification on 12-Month Moving Average**:
   Potential peaks and troughs are identified on a smooth 12-month moving average of the series. A month $t$ is identified as a candidate peak if its value exceeds all values within a 5-month symmetric neighborhood:
   $$Y_t > Y_{t \\pm k}, \\quad k = 1, 2, \\dots, 5$$
   Similarly, a candidate trough is identified if $Y_t < Y_{t \\pm k}$.
3. **Step 3: Refinement on Intermediate Henderson Curves**:
   The candidate turning points are mapped onto a shorter Henderson moving average filter (e.g., 7-term or 9-term), searching within $\\pm 4$ months of the Step 2 dates to ensure that the turning point reflects the genuine turning apex rather than filter distortion.
4. **Step 4: Final Pinpointing on the Deseasonalized Series**:
   The turning point date is transferred to the unsmoothed deseasonalized economic series, selecting the absolute local maximum or minimum within a neighborhood of the Henderson turning point.

### 2. Censoring and Duration Constraints
To ensure economic credibility and conformity with classical business cycle theory, the algorithm enforces strict duration and alternation rules:
- **Alternation Constraint**: Peaks and troughs must strictly alternate. If two consecutive peaks occur without an intervening trough, the lower peak is eliminated.
- **Phase Duration Constraint**: The minimum duration of an economic phase (from peak to trough, or from trough to peak) must be at least **5 months (or 2 quarters)**. Shorter dips are classified as pause corrections rather than full recessions.
- **Full Cycle Duration Constraint**: The minimum duration of a complete cycle (from peak to peak, or from trough to trough) must be at least **15 months (or 5 quarters)**.
- **Boundary Censoring**: No turning point can be placed within the first 6 months or last 6 months of a time series, preventing unstable nowcast revisions at sample boundaries.
"""

# ----------------------------------------------------
# UNIT 6
# ----------------------------------------------------
u6_cross = """
---

## Capital Services and the Perpetual Inventory Method (PIM)

In the System of National Accounts, physical capital assets (commercial factories, computer servers, transport vehicles, industrial robotics) enter production not as current consumable expenses, but as durable productive stocks that provide a continuous flow of productive services over multiple calendar years. To measure total capital inputs and depreciation rigorously, national statistical institutes deploy the **Perpetual Inventory Method (PIM)** codified in the OECD Manual on Measuring Capital (2009).

### 1. The Perpetual Inventory Method Formulation
The gross capital stock of an asset category is estimated by accumulating historical gross fixed capital investments over time, subtracting retired assets as they reach the end of their economic service lives:

$$K_t = \\sum_{\\tau=0}^{T_{\\max}} I_{t-\\tau} g(\\tau)$$

where:
- $I_{t-\\tau}$ is the constant-price gross investment incurred $\\tau$ years in the past.
- $g(\\tau)$ is the **Survival Function**, representing the probability that an asset installed $\\tau$ years ago remains physically active in production (typically modeled using a log-normal or Weibull retirement distribution centered on average asset lifespan $T_{\\text{mean}}$).

### 2. Depreciation Profiles: Geometric vs Hyperbolic
The decline in an asset's economic market value as it ages is governed by its **Depreciation Profile**:
- **Geometric (Declining Balance) Depreciation**:
  Assumes that an asset's efficiency and market price decline at a constant percentage rate $\\delta$ per year:
  $$P_{\\tau} = P_0 (1 - \\delta)^\\tau$$
  Under geometric depreciation, the rate of physical deterioration and the rate of monetary depreciation coincide, simplifying national accounting equations.
- **Hyperbolic Age-Efficiency Profile**:
  Reflects the engineering reality that many machines maintain high, near-constant productive output for most of their working lives, experiencing rapid breakdown only near the end of their lifespan:
  $$d(\\tau) = \\frac{T - \\tau}{T - \\beta \\tau}, \\quad 0 \\le \\beta < 1$$

### 3. Capital Services vs Net Capital Wealth
National accountants distinguish sharply between:
1. **Net Capital Stock (Wealth Capital)**: The sum of the written-down market values of all past investments, measuring the net monetary wealth stored in capital goods.
2. **Capital Services (Productive Capital)**: The physical flow of productive inputs rendered by capital assets into current production.
In calculating Total Factor Productivity (TFP / Solow Residual), economists must deploy Capital Services rather than Net Capital Wealth: a fast-depreciating computer server provides high productive computing power per dollar of asset value compared to a long-lived warehouse, requiring user-cost rental price weighting.
"""

# ----------------------------------------------------
# UNIT 7
# ----------------------------------------------------
u7_cross = """
---

## Sectoral Prioritization: The Hypothetical Extraction Method (HEM)

In national industrial strategy and regional development planning, economic planners seek to identify "key sectors" whose disruption or expansion would exert the greatest systemic impact on national output. While simple output multipliers (column sums of $(I-A)^{-1}$) provide a basic ranking, they do not account for the absolute scale of the industry within the economy.
To provide a rigorous systemic assessment, input-output economists employ the **Hypothetical Extraction Method (HEM)**.

### Mathematical Formulation
The Hypothetical Extraction Method simulates the complete hypothetical removal of sector $k$ from the economic matrix, evaluating how total national production would contract in its absence.

Partition the $n$-sector technology matrix $A$ into sector $k$ and all other remaining sectors (denoted $-k$):

$$A = \\begin{bmatrix}
a_{kk} & A_{k, -k} \\\\
A_{-k, k} & A_{-k, -k}
\\end{bmatrix}$$

1. **Extraction of Backward Linkages (Hypothetical Supplier Shutdown)**:
   Suppose sector $k$ stops purchasing intermediate inputs from the rest of the economy ($A_{-k, k} = 0$). The extracted technology matrix is:
   $$\\bar{A}_{(k)}^{\\text{back}} = \\begin{bmatrix}
   a_{kk} & A_{k, -k} \\\\
   0 & A_{-k, -k}
   \\end{bmatrix}$$
   The resulting hypothetical output vector is:
   $$\\bar{X}_{(k)}^{\\text{back}} = (I - \\bar{A}_{(k)}^{\\text{back}})^{-1} F$$
   The aggregate output loss caused by severing sector $k$'s upstream purchases is:
   $$\\Delta X_{\\text{back}} = \\sum_{i=1}^{n} X_i - \\sum_{i=1}^{n} \\bar{X}_{i, (k)}^{\\text{back}}$$

2. **Complete Hypothetical Extraction**:
   Extracting both upstream purchases and downstream sales of sector $k$ sets $A_{k, -k} = 0$, $A_{-k, k} = 0$, and $F_k = 0$.
   The percentage loss in total national output measures the total systemic integration index of sector $k$:
   $$\\text{Total Extraction Impact } \\% = \\frac{\\sum X_i - \\sum \\bar{X}_{i, (k)}}{\\sum X_i} \\times 100\\%$$

The Hypothetical Extraction Method identifies true structural bottlenecks: sectors whose failure triggers catastrophic cascading shutdowns across the entire national economy.

---

## Supply-Driven Input-Output Modeling: The Ghosh Model

While Leontief's classical model is **Demand-Driven** (allocating output from inputs based on fixed technical coefficients $a_{ij} = x_{ij} / X_j$), A. Ghosh (1958) formulated a mathematically dual **Supply-Driven Input-Output Model**.

In the Ghosh framework:
- Output allocations are assumed to depend on fixed **Allocation Coefficients** (output shares):
  $$b_{ij} = \\frac{x_{ij}}{X_i}$$
  where $b_{ij}$ represents the fraction of sector $i$'s gross output that is allocated to sector $j$ as an intermediate input.
- Compiling the $n \\times n$ **Allocation Matrix $B$**:
  $$B = \\begin{bmatrix}
  b_{11} & b_{12} & \\dots & b_{1n} \\\\
  b_{21} & b_{22} & \\dots & b_{2n} \\\\
  \\vdots & \\vdots & \\ddots & \\vdots \\\\
  b_{n1} & b_{n2} & \\dots & b_{nn}
  \\end{bmatrix}$$

The horizontal row balance equation across sectors is:
$$X_j = \\sum_{i=1}^{n} b_{ij} X_i + V_j$$
In matrix notation:
$$X^T = X^T B + V^T \\implies X^T (I - B) = V^T$$
where $V$ is the vector of primary value-added inputs (labor, capital, imports).

Inverting $(I - B)$ yields the **Ghosh Inverse Matrix**:

$$X^T = V^T (I - B)^{-1} = V^T G$$

The Ghosh model traces how an exogenous disruption or expansion in primary factor availability (such as a nationwide labor strike, an international petroleum embargo, or an agricultural drought) transmits forward through the supply chain, altering output levels across downstream industries.
"""

# ----------------------------------------------------
# UNIT 8
# ----------------------------------------------------
u8_cross = """
---

## Flexible Production Frontiers: The Transcendental Logarithmic (Translog) Function

In empirical microeconomics and production economics, researchers often reject the classical Cobb-Douglas production function ($Y = A K^\\alpha L^\\beta$) and Constant Elasticity of Substitution (CES) function because they impose restrictive a priori constraints: Cobb-Douglas forces the elasticity of substitution between capital and labor to equal unity ($\\sigma = 1$), while CES forces it to remain constant across all output levels.

To model unrestricted substitution dynamics, Laurits Christensen, Dale Jorgenson, and Lawrence Lau (1973) developed the **Transcendental Logarithmic (Translog) Production Frontier**.

### Mathematical Formulation
The translog production function represents a second-order Taylor series approximation to an arbitrary, twice continuously differentiable production function:

$$\\ln(Y) = \\alpha_0 + \\sum_{i=1}^{m} \\alpha_i \\ln(X_i) + \\frac{1}{2} \\sum_{i=1}^{m} \\sum_{j=1}^{m} \\beta_{ij} \\ln(X_i) \\ln(X_j)$$

where:
- $Y$ is total physical output.
- $X_i, X_j$ are input factors (e.g., Capital $K$, Labor $L$, Energy $E$, Materials $M$).
- By Young's theorem on the symmetry of cross-partial derivatives:
  $$\\beta_{ij} = \\beta_{ji} \\quad \\forall i \\ne j$$

### 1. Output Elasticities with Respect to Inputs
The output elasticity of factor $i$ is:

$$\\epsilon_i = \\frac{\\partial \\ln(Y)}{\\partial \\ln(X_i)} = \\alpha_i + \\sum_{j=1}^{m} \\beta_{ij} \\ln(X_j)$$

Notice that unlike Cobb-Douglas (where elasticity is the constant parameter $\\alpha_i$), the translog output elasticity varies continuously with the levels of all inputs deployed.
Under constant returns to scale:
$$\\sum_{i=1}^{m} \\alpha_i = 1 \\quad \\text{and} \\quad \\sum_{j=1}^{m} \\beta_{ij} = 0 \\quad \\forall i$$

### 2. Allen-Uzawa and Morishima Elasticities of Substitution
The elasticity of substitution between factor $i$ and factor $j$ in the translog cost dual function $C(w, Y)$ is given by the **Allen-Uzawa Partial Elasticity of Substitution (AES)**:

$$\\sigma_{ij}^{\\text{AES}} = \\frac{C \\cdot \\frac{\\partial^2 C}{\\partial w_i \\partial w_j}}{\\frac{\\partial C}{\\partial w_i} \\frac{\\partial C}{\\partial w_j}} = \\frac{\\gamma_{ij} + s_i s_j}{s_i s_j}, \\quad i \\ne j$$

where $s_i = w_i X_i / C$ is the cost share of input $i$.
Because the Allen-Uzawa elasticity can produce ambiguous signs in multi-factor settings, modern econometrics prefers the **Morishima Elasticity of Substitution (MES)**:

$$\\sigma_{ij}^{\\text{MES}} = \\frac{\\partial \\ln(X_i / X_j)}{\\partial \\ln(w_j)} = s_j (\\sigma_{ij}^{\\text{AES}} - \\sigma_{jj}^{\\text{AES}})$$

The Morishima elasticity measures the percentage change in the input ratio $(X_i / X_j)$ induced by a one-percent change in the price of factor $j$ ($w_j$). It is inherently asymmetric ($\\sigma_{ij}^{\\text{MES}} \\ne \\sigma_{ji}^{\\text{MES}}$), accurately capturing that adjusting capital equipment in response to a wage hike is structurally different from adjusting labor hiring in response to an interest rate shock.
"""

crossers = {
    2: u2_cross,
    4: u4_cross,
    6: u6_cross,
    7: u7_cross,
    8: u8_cross,
}

for unit_num, cross_text in crossers.items():
    file_path = OUT_DIR / f"unit-{unit_num}.md"
    content = file_path.read_text(encoding="utf-8")
    new_content = inject_before_worked_questions(content, cross_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Unit {unit_num} crossed: {prose_count(new_content)} words")
