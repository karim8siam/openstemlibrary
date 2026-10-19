#!/usr/bin/env python3
"""
Push Economic Statistics past 30,500 pure prose words by adding deep academic content to Units 4, 5, 6, 7, and 8.
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
# UNIT 4 PUSH
# ----------------------------------------------------
u4_push = """
---

## Band-Pass Frequency Filtering: Baxter-King and Christiano-Fitzgerald Filters

In modern empirical macroeconomics, the classical Burns and Mitchell definition of a business cycle corresponds to fluctuations in economic activity with periodicities ranging between **6 quarters (1.5 years)** and **32 quarters (8 years)**. Fluctuations with periodicities shorter than 6 quarters are classified as high-frequency irregular noise or seasonal remnants, while fluctuations lasting longer than 8 years reflect low-frequency secular trends.

To isolate this precise economic frequency band without distorting phase timing, econometricians employ **Band-Pass Frequency Filters**.

### 1. The Ideal Band-Pass Filter
In the frequency domain, an ideal band-pass filter possesses a frequency response function that equals 1 inside the pass-band $[\\omega_L, \\omega_U]$ and 0 outside:

$$\\alpha(\\omega) = \\begin{cases} 1, & \\omega_L \\le |\\omega| \\le \\omega_U \\\\ 0, & \\text{otherwise} \\end{cases}$$

where $\\omega_L = \\frac{2\\pi}{32} \\approx 0.1963$ radians and $\\omega_U = \\frac{2\\pi}{6} \\approx 1.0472$ radians.

The inverse Fourier transform yields the theoretical infinite-order symmetric time-domain filter weights:

$$a_j = \\begin{cases} \\frac{\\omega_U - \\omega_L}{\\pi}, & j = 0 \\\\ \\frac{\\sin(\\omega_U j) - \\sin(\\omega_L j)}{\\pi j}, & j = \\pm 1, \\pm 2, \\dots \\end{cases}$$

Applying the ideal filter requires infinite historical and future data: $y_t^* = \\sum_{j=-\\infty}^{\\infty} a_j y_{t-j}$. Because finite samples cannot implement an infinite filter, finite approximations must be constructed.

### 2. The Baxter-King (BK) Filter
Marianne Baxter and Robert King (1999) proposed an optimal finite approximation by truncating the infinite filter at a symmetric lag lead length $K$ (typically $K = 12$ quarters for quarterly data):

$$\\min_{\\{\\hat{a}_j\\}} \\int_{-\\pi}^{\\pi} |\\alpha(\\omega) - \\hat{\\alpha}(\\omega)|^2 d\\omega \\quad \\text{subject to } \\hat{\\alpha}(0) = \\sum_{j=-K}^{K} \\hat{a}_j = 0$$

The zero-frequency constraint $\\sum \\hat{a}_j = 0$ guarantees that the BK filter completely eliminates any linear or deterministic trend from the series, rendering non-stationary $I(1)$ series stationary without introducing phase shift distortions.
However, because the filter is symmetric, it results in the loss of $K$ observations at the beginning and $K$ observations at the end of the sample (a loss of 3 years of data at each boundary).

### 3. The Christiano-Fitzgerald (CF) Full-Sample Asymmetric Filter
To prevent data loss at sample boundaries, Lawrence Christiano and Terry Fitzgerald (2003) developed an asymmetric filter that computes cyclical estimates across the entire sample period $t = 1, \\dots, T$.
Under the assumption that the time series follows a random walk with drift ($y_t = \\mu + y_{t-1} + \\epsilon_t$), the CF filter computes time-varying weights $\\hat{b}_{j,t}$ that minimize the mean squared approximation error conditional on all available observations:

$$y_t^{\\text{CF}} = \\sum_{j=-(T-t)}^{t-1} \\hat{b}_{j,t} y_{t+j}$$

At the center of a long series, the CF filter approaches the symmetric Baxter-King weights; at the sample boundaries (such as the most recent quarter), the filter uses asymmetric weights, eliminating endpoint data loss and enabling real-time business cycle monitoring for central banks.
"""

# ----------------------------------------------------
# UNIT 5 PUSH
# ----------------------------------------------------
u5_push = """
---

## Vulnerability to Poverty and Dynamic Risk Analysis

Standard static poverty metrics measure whether a household's income falls below the subsistence threshold $z$ at a single survey instant. However, households constantly transition into and out of poverty due to agricultural droughts, macro-financial crises, illness, unemployment, or seasonal price spikes.
To incorporate future uncertainty into social policy, economists analyze **Vulnerability to Poverty**.

### Mathematical Formulation of Vulnerability as Expected Poverty
Pioneered by Stefan Dercon and Shubham Chaudhuri (2002), vulnerability $V_{it}$ is defined as the ex-ante probability that a household will experience poverty in the future period $t+1$:

$$V_{it} = P(y_{i, t+1} < z) = \\int_{-\\infty}^{z} f_{it}(y_{i, t+1}) dy_{i, t+1}$$

where $f_{it}(y_{i, t+1})$ is the conditional subjective probability density function of future household consumption, dependent on observable household asset endowments $X_{it}$ and covariate community shock variables $S_t$.

Econometrically, log household consumption is modeled as:

$$\\ln(y_{it}) = X_{it} \\beta + e_{it}$$

where disturbances exhibit heteroskedasticity capturing risk exposure:
$$e_{it} \\sim N(0, \\sigma_{e, i}^2), \\quad \\sigma_{e, i}^2 = X_{it} \\theta$$

Assuming log-normality, the estimated vulnerability probability is:

$$\\hat{V}_{it} = \\Phi\\left( \\frac{\\ln(z) - X_{it} \\hat{\\beta}}{\\hat{\\sigma}_{e, i}} \\right)$$

where $\\Phi(\\cdot)$ is the standard normal cumulative distribution function.

### Policy Taxonomy: Chronic vs Transient Poverty
A household is classified as vulnerable if its vulnerability probability exceeds a critical risk threshold (typically $V^* = 0.50$):
1. **The Chronically Poor**: Households whose expected long-run consumption is strictly below the poverty line ($E[y_i] < z$). They lack productive capital, arable land, and marketable education. Their poverty requires permanent structural interventions (asset transfers, education, land reform).
2. **The Transiency Vulnerable**: Households whose expected mean consumption is above the poverty line ($E[y_i] > z$), but whose exposure to uninsured environmental, macroeconomic, or health volatility frequently plunges them into poverty. Their vulnerability requires counter-cyclical safety nets (crop insurance, subsidized health coverage, emergency credit lines).

---

## The Sen Poverty Index and Axiomatic Revisions

In 1976, Amartya Sen demonstrated that the classical Headcount Ratio ($H$) and Poverty Gap Index ($I$) violated two fundamental ethical criteria:
1. **The Monotonicity Axiom**: A reduction in the income of any poor household, holding all other incomes constant, must strictly increase the poverty index. (Violated by $H$).
2. **The Transfer Axiom**: A pure regressive transfer of income from a poor household to any richer household (even if both remain poor) must strictly increase the poverty index. (Violated by both $H$ and $I$).

### The Sen Normalized Poverty Index ($S$)
Sen formulated an index explicitly integrating incidence ($H$), depth ($I$), and inequality among the poor ($G_p$):

$$S = H \\left[ I + (1 - I) G_p \\right]$$

where:
- $H = Q / N$ is the Headcount Ratio.
- $I = (z - \\bar{y}_p) / z$ is the Income Gap Ratio.
- $G_p$ is the Gini coefficient calculated exclusively among the poor population.

#### Axiomatic Interpretation:
If all poor individuals have identical incomes ($G_p = 0$), Sen's index reduces to $S = H \\times I = P_1$ (the standard Poverty Gap Index). As inequality among the destitute widens ($G_p > 0$), the index increases, satisfying both the Monotonicity Axiom and the Transfer Axiom by penalizing severe internal deprivation among the poorest of the poor.
"""

# ----------------------------------------------------
# UNIT 6 PUSH
# ----------------------------------------------------
u6_push = """
---

## Flow of Funds Accounts and the Integrated Financial Balance Sheet

National income accounting in the real economy tracks the production of goods, generation of income, and expenditure on capital goods. However, modern economies operate via complex financial intermediation: savings generated by surplus economic units (households) must be channeled through financial markets and commercial banks to finance the deficits of investing units (corporations, general government).
To track these capital movements, national accounts include the **Flow of Funds Accounts (FFA)** and the **Integrated Balance Sheet**.

### 1. The Inter-Sectoral Net Lending/Borrowing Identity
For every institutional sector $k$ in the economy (Households, Non-Financial Corporations, Financial Corporations, General Government, Rest of the World), gross savings ($S_k$) plus net capital transfers ($TK_k$) minus gross capital accumulation ($I_k$) defines the sector's **Net Lending ($+)$ or Net Borrowing ($-$)**:

$$\\text{NL/NB}_k = (S_k + TK_k) - I_k$$

Across all institutional sectors and the Rest of the World, the sum of net lending and borrowing is identically zero:

$$\\sum_{k} \\text{NL/NB}_k \\equiv 0$$

- If General Government runs a fiscal deficit (Net Borrowing, $\\text{NL/NB}_{\\text{gov}} < 0$), it must be financed by domestic household net savings ($\\text{NL/NB}_{\\text{hh}} > 0$), corporate retained savings, or foreign capital inflows from the Rest of the World ($\\text{NL/NB}_{\\text{RoW}} > 0$, equivalent to a current account deficit).

### 2. Financial Assets and Liability Tracking
In the Flow of Funds matrix:
- Every acquisition of a financial asset by one sector (e.g., a household purchasing a corporate bond or bank deposit) is matched by the issuance of a financial liability by another sector (the corporate borrowing or bank deposit liability).
- Net lending equals the net acquisition of financial assets minus the net incurrence of financial liabilities:
  $$\\text{NL/NB}_k = \\Delta \\text{FA}_k - \\Delta \\text{FL}_k$$

The Flow of Funds matrix provides central banks and macroprudential regulators with an early warning system for systemic risk, identifying excessive corporate debt leverage, real estate mortgage bubbles, and dangerous liquidity mismatches before they trigger systemic banking crises.
"""

# ----------------------------------------------------
# UNIT 7 PUSH
# ----------------------------------------------------
u7_push = """
---

## Multi-Regional Input-Output (MRIO) Modeling and Global Value Chains

In the era of economic globalization, international trade no longer consists primarily of completed finished goods traded between two nations. Modern manufacturing is characterized by **Global Value Chains (GVCs)**: raw mineral ores extracted in Australia are shipped to China for refining, manufactured into electronic components in Taiwan, assembled into consumer smartphones in Vietnam, and marketed by retail corporations in the United States and Europe.

To analyze international trade and carbon emissions without distortion, national statistical organizations compile **Multi-Regional Input-Output (MRIO)** tables (such as the OECD Inter-Country Input-Output ICIO database and the World Input-Output Database WIOD).

### 1. Mathematical Architecture of the MRIO Model
Consider a world economy comprising $M$ sovereign nations ($r, s = 1, \\dots, M$), where each nation has $n$ industrial sectors.
The global MRIO system is formulated as:

$$\\begin{bmatrix}
X^1 \\\\ X^2 \\\\ \\vdots \\\\ X^M
\\end{bmatrix} = \\begin{bmatrix}
A^{11} & A^{12} & \\dots & A^{1M} \\\\
A^{21} & A^{22} & \\dots & A^{2M} \\\\
\\vdots & \\vdots & \\ddots & \\vdots \\\\
A^{M1} & A^{M2} & \\dots & A^{MM}
\\end{bmatrix} \\begin{bmatrix}
X^1 \\\\ X^2 \\\\ \\vdots \\\\ X^M
\\end{bmatrix} + \\begin{bmatrix}
\\sum_{s} F^{1s} \\\\ \\sum_{s} F^{2s} \\\\ \\vdots \\\\ \\sum_{s} F^{Ms}
\\end{bmatrix}$$

where:
- $X^r$ is the $n \\times 1$ gross output vector of country $r$.
- $A^{rr}$ is the domestic technology matrix of country $r$.
- $A^{rs}$ is the inter-country trade intermediate coefficient matrix: each element $a_{ij}^{rs} = x_{ij}^{rs} / X_j^s$ denotes the intermediate inputs exported from industry $i$ in country $r$ consumed by industry $j$ in country $s$.
- $F^{rs}$ is the final demand vector of goods produced in country $r$ and consumed in country $s$.

Defining the global technology matrix as $\\mathbb{A}$ and global output as $\\mathbb{X}$:

$$\\mathbb{X} = (\\mathbb{I} - \\mathbb{A})^{-1} \\mathbb{F}$$

### 2. Trade in Value Added (TiVA) and Gross Export Decomposition
Pioneered by Robert Koopman, Zhi Wang, and Shang-Jin Wei (2014), the **KWW Gross Export Decomposition** breaks a nation's gross bilateral exports ($E^{rs}$) into distinct value-added components:

1. **Domestic Value Added ($DVA$) Absorbed Abroad**: The true net income generated by domestic workers and capital embodied in exports that is ultimately consumed by foreign residents.
2. **Domestic Value Added Returning Home**: Domestic inputs exported abroad for intermediate processing that are subsequently re-imported as finished goods.
3. **Foreign Value Added ($FVA$)**: The value of imported foreign intermediate components incorporated into domestic exports.
4. **Pure Double-Counting**: Goods and intermediate parts that cross international borders multiple times before final assembly.

In electronics and automobile manufacturing, Foreign Value Added often accounts for 40% to 60% of gross export value, confirming that gross customs trade statistics severely distort actual economic contributions and bilateral trade balances.
"""

# ----------------------------------------------------
# UNIT 8 PUSH
# ----------------------------------------------------
u8_push = """
---

## Econometric Identification of Market Power: The Bresnahan-Lau Model

In applied microeconomics and antitrust regulatory proceedings, competition authorities must assess whether firms in concentrated industries (such as commercial banking, telecommunications, or airline transport) behave competitively or exploit market power to extract monopoly rents. Because proprietary marginal cost data are rarely disclosed to econometricians, Timothy Bresnahan (1982) and Lawrence Lau (1982) developed an econometric methodology to identify market conduct directly from observable aggregate market price and quantity data.

### 1. Structural Formulation
Consider an oligopolistic market with aggregate demand:

$$Q_t = \\alpha_0 + \\alpha_1 P_t + \\alpha_2 Y_t + \\alpha_3 (P_t \\cdot Z_t) + u_t$$

where $Y_t$ is consumer income, and $Z_t$ is an exogenous demand rotator (such as the price of a complementary service) that alters the slope of the demand curve.

The industry marginal revenue perceived by a representative firm is:

$$MR_t(\\theta) = P_t + \\theta \\left( \\frac{\\partial P}{\\partial Q} \\right) Q_t = P_t + \\frac{\\theta}{\\alpha_1 + \\alpha_3 Z_t} Q_t$$

where $\\theta \\in [0, 1]$ is the unobserved **Conduct Parameter**:
- $\\theta = 0$: Perfect Competition (Price equals Marginal Cost, $P = MC$).
- $\\theta = 1/N$: Symmetric Cournot-Nash Oligopoly with $N$ firms.
- $\\theta = 1$: Perfect Collusion / Joint Monopoly Profit Maximization.

Assuming a linear marginal cost curve:
$$MC_t = \\beta_0 + \\beta_1 Q_t + \\beta_2 W_t + v_t$$
where $W_t$ is an exogenous input cost (e.g., labor wages, energy prices).

In profit-maximizing supply equilibrium ($MR_t = MC_t$):

$$P_t = -\\theta Q_t^* + \\beta_0 + \\beta_1 Q_t + \\beta_2 W_t + v_t$$

where $Q_t^* = \\frac{Q_t}{\\alpha_1 + \\alpha_3 Z_t}$ is the rotated effective quantity variable.

### 2. Simultaneous Estimation and Hypothesis Testing
By estimating the demand equation and the supply relation simultaneously via Two-Stage Least Squares or Full Information Maximum Likelihood (FIML), the econometrician identifies $\\alpha_1, \\alpha_3$ from the demand curve, which allows the construction of $Q_t^*$.
The regression coefficient on $Q_t^*$ in the supply relation directly identifies the conduct parameter $\\theta$.
Statistical agencies can then formally test the null hypothesis of perfect competition ($H_0: \\theta = 0$) against the alternative of oligopolistic collusion ($H_1: \\theta > 0$), providing court-admissible empirical evidence of market anti-competitive conduct.
"""

pushes = {
    4: u4_push,
    5: u5_push,
    6: u6_push,
    7: u7_push,
    8: u8_push,
}

for unit_num, push_text in pushes.items():
    file_path = OUT_DIR / f"unit-{unit_num}.md"
    content = file_path.read_text(encoding="utf-8")
    new_content = inject_before_worked_questions(content, push_text)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"Unit {unit_num} pushed: {prose_count(new_content)} words")
