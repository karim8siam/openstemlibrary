#!/usr/bin/env python3
"""
Generate Units 7 and 8 for Economic Statistics (Stat H-204 / Stat H-210)
"""
import re
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-economic-statistics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

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

# ==========================================
# UNIT 7: INPUT-OUTPUT ANALYSIS & SOCIAL ACCOUNTING SYSTEMS
# ==========================================

u7_content = """# Unit 7: Input-Output Analysis & Social Accounting Systems

## Leontief's Inter-Industry General Equilibrium Model

Modern industrial economies do not operate as isolated silos. The production of an automobile requires steel, glass, rubber, electronics, and design services; the production of steel in turn requires iron ore, coal, electrical power, and heavy transport equipment; and electricity generation consumes coal, natural gas, and turbine machinery. To analyze these dense, circular inter-industry dependencies, the Russian-American economist Wassily Leontief developed **Input-Output Analysis** in the 1930s—a breakthrough for which he was awarded the 1973 Nobel Memorial Prize in Economic Sciences.

Input-Output analysis provides an empirical, matrix-algebraic formulation of general equilibrium theory. It maps the complex webs of transactions connecting all producing sectors, enabling economists to calculate how an exogenous shift in final demand for a single sector (such as an export boom, defense procurement, or green energy subsidy) ripples through the entire industrial fabric.

---

## Mathematical Formulation of the Open Static Leontief Model

Consider an economy partitioned into $n$ mutually exclusive and exhaustive productive industries: $1, 2, \\dots, n$.

Let:
- $X_i$ denote the total gross physical or monetary output produced by sector $i$.
- $x_{ij}$ denote the quantity of output produced by sector $i$ that is purchased and consumed as an intermediate input by sector $j$ during the accounting period.
- $F_i$ denote the net final demand for the output of sector $i$ (encompassing household consumption, gross capital formation, government purchases, and net exports).

### 1. The Physical Output Balance Equations
For each producing sector $i$, its total gross output must exactly equal the sum of intermediate sales to all $n$ consuming industries plus sales to final demand:

$$X_i = \\sum_{j=1}^{n} x_{ij} + F_i, \\quad i = 1, 2, \\dots, n$$

In expanded form:
$$\\begin{aligned}
X_1 &= x_{11} + x_{12} + \\dots + x_{1n} + F_1 \\\\
X_2 &= x_{21} + x_{22} + \\dots + x_{2n} + F_2 \\\\
&\\vdots \\\\
X_n &= x_{n1} + x_{n2} + \\dots + x_{nn} + F_n
\\end{aligned}$$

### 2. Leontief Technical Input Coefficients
Leontief introduced the fundamental structural assumption of fixed-coefficient production functions (constant returns to scale and zero input substitution): to produce one unit of gross output in sector $j$, a fixed, constant amount of input from sector $i$ is technically required:

$$a_{ij} = \\frac{x_{ij}}{X_j} \\implies x_{ij} = a_{ij} X_j$$

where $a_{ij}$ is the **Direct Technical Input Coefficient**. The coefficients are compiled into the $n \\times n$ **Technology Matrix ($A$)**:

$$A = \\begin{bmatrix}
a_{11} & a_{12} & \\dots & a_{1n} \\\\
a_{21} & a_{22} & \\dots & a_{2n} \\\\
\\vdots & \\vdots & \\ddots & \\vdots \\\\
a_{n1} & a_{n2} & \\dots & a_{nn}
\\end{bmatrix}$$

Substituting $x_{ij} = a_{ij} X_j$ into the balance equations:

$$X_i = \\sum_{j=1}^{n} a_{ij} X_j + F_i, \\quad i = 1, 2, \\dots, n$$

In matrix notation:

$$X = A X + F$$

where $X = [X_1, X_2, \\dots, X_n]^T$ and $F = [F_1, F_2, \\dots, F_n]^T$.

### 3. The Leontief Inverse Matrix
Rearranging the matrix balance equation:

$$X - A X = F \\implies (I - A) X = F$$

where $I$ is the $n \\times n$ identity matrix. If $(I - A)$ is non-singular, we invert the matrix to solve for the gross output vector required to satisfy any arbitrary final demand vector $F$:

$$X = (I - A)^{-1} F$$

The matrix $L = (I - A)^{-1}$ is the celebrated **Leontief Inverse Matrix** (or Total Requirements Matrix). Each element $l_{ij}$ of $L$ quantifies the total (direct plus indirect) gross output that sector $i$ must generate to satisfy one additional unit of final demand for the output of sector $j$.

Using the Neumann power series expansion for matrix inverses (valid when the spectral radius $\\rho(A) < 1$):

$$(I - A)^{-1} = I + A + A^2 + A^3 + \\dots$$

- $I$: The direct delivery of one unit of final output.
- $A$: The first-round direct intermediate inputs needed.
- $A^2$: The second-round indirect intermediate inputs needed to produce the first-round inputs.
- $A^k$: The $k$-th round indirect ripple effects propagating across supply chains.

---

## Economic Viability: The Hawkins-Simon Conditions

A purely mathematical matrix inversion does not guarantee that an economic system is physically viable. If an economy's industries consume more steel, coal, and energy to produce a unit of steel than the unit itself provides, the system is parasitic and will collapse.

In 1949, David Hawkins and Herbert A. Simon formulated the necessary and sufficient mathematical conditions for an input-output system to be **Economically Viable**—meaning that for any non-negative, non-zero final demand vector $F \\ge 0$, there exists a strictly positive gross output solution vector $X > 0$.

### The Hawkins-Simon Theorem:
An $n \\times n$ technology matrix $A$ is economically viable if and only if all leading principal minors of the Leontief matrix $M = (I - A)$ are strictly positive:

1. **First-order minor**:
   $$1 - a_{11} > 0 \\implies a_{11} < 1$$
   No industry can consume an entire unit (or more) of its own output merely to produce one unit of that output.
2. **Second-order minor**:
   $$\\det \\begin{bmatrix} 1 - a_{11} & -a_{12} \\\\ -a_{21} & 1 - a_{22} \\end{bmatrix} = (1 - a_{11})(1 - a_{22}) - a_{12} a_{21} > 0$$
   The circular feedback between sectors 1 and 2 must not consume more than the combined output generated.
3. **General $k$-th order minor**:
   $$\\det(M_k) > 0 \\quad \\text{for all } k = 1, 2, \\dots, n$$

If any leading principal minor is zero or negative, the technology requires more aggregate resources than it produces, rendering the economic structure unsustainable.

---

## Inter-Industry Multipliers and Linkages

Input-output matrices provide standard macroeconomic policy multipliers used to quantify supply-chain impacts:

### 1. Output Multipliers
The **Output Multiplier** for sector $j$ measures the total gross output generated across all sectors of the economy per dollar increase in final demand for sector $j$'s output. It is given by the column sum of the Leontief inverse matrix:

$$O_j = \\sum_{i=1}^{n} l_{ij}$$

Sectors with high output multipliers (e.g., manufacturing, construction) trigger large spillover effects across supplier networks.

### 2. Backward and Forward Linkages (Rasmussen Indices)
Pioneered by P. Nørregaard Rasmussen (1956) and Albert Hirschman (1958), linkage indices identify key strategic sectors:
- **Backward Linkage ($U_j$)**: Measures the extent to which industry $j$ stimulates upstream suppliers by purchasing intermediate inputs:
  $$U_j = \\frac{\\frac{1}{n} \\sum_{i=1}^{n} l_{ij}}{\\frac{1}{n^2} \\sum_{i=1}^{n} \\sum_{j=1}^{n} l_{ij}} = \\frac{n \\sum_{i=1}^{n} l_{ij}}{\\sum_{i=1}^{n} \\sum_{j=1}^{n} l_{ij}}$$
  If $U_j > 1$, sector $j$ exerts an above-average upstream pull on the economy.
- **Forward Linkage ($U_i$)**: Measures the extent to which industry $i$'s output is consumed as an intermediate input by downstream purchasing industries:
  $$U_i = \\frac{n \\sum_{j=1}^{n} l_{ij}}{\\sum_{i=1}^{n} \\sum_{j=1}^{n} l_{ij}}$$
  If $U_i > 1$, sector $i$ provides an above-average supply base for downstream industrial growth.

---

## Social Accounting Matrix (SAM) Architecture

A **Social Accounting Matrix (SAM)** expands Leontief's inter-industry input-output table into a comprehensive, square, double-entry macroeconomic framework encompassing all socioeconomic transactions within an economy.

In a SAM:
- Every row records economic **receipts (inflows / revenues)** of an account.
- Every column records economic **outlays (outflows / expenditures)** of an account.
- **Fundamental Accounting Identity**: For every account $k$, total receipts must strictly equal total outlays:
  $$\\text{Row Total}_k \\equiv \\text{Column Total}_k$$

The standard accounts in a macro-SAM include:
1. **Production Activities**: Purchasing intermediate inputs and primary factor services; selling domestic gross output.
2. **Commodities**: Domestic supply plus imports; domestic sales plus exports.
3. **Factors of Production**: Labor and capital receiving value-added factor earnings; distributing income to households and enterprises.
4. **Institutions**:
   - Households: Receiving labor wages, capital dividends, and government transfers; paying income taxes and financing private consumption and savings.
   - Enterprises: Receiving operating surplus; paying corporate taxes and distributing retained earnings.
   - Government: Receiving direct/indirect taxes; financing public consumption, subsidies, and social safety nets.
5. **Capital Account**: Accumulating national savings; financing gross fixed capital formation and inventory expansion.
6. **Rest of the World (RoW)**: Tracking exports, imports, cross-border remittances, and foreign capital flows.

---

## Worked Questions and Solutions

### Question 1: Two-Sector Leontief System and Economic Viability
An economy consists of two interdependent productive sectors: **Agriculture ($X_1$)** and **Manufacturing ($X_2$)**. The inter-industry flow of transactions and final demand over a fiscal year (in millions of dollars) is:

| Producing Sector | Consumed by Agriculture ($x_{i1}$) | Consumed by Manufacturing ($x_{i2}$) | Final Demand ($F_i$) | Total Gross Output ($X_i$) |
| :--- | :---: | :---: | :---: | :---: |
| **Agriculture ($1$)** | $30$ | $60$ | $110$ | $200$ |
| **Manufacturing ($2$)** | $40$ | $20$ | $140$ | $200$ |
| **Primary Value Added ($V_j$)** | $130$ | $120$ | — | — |
| **Total Gross Outlays ($X_j$)** | $200$ | $200$ | — | — |

1. Calculate the technical input coefficients $a_{ij}$ and construct the Technology Matrix $A$.
2. Formulate the Leontief matrix $(I - A)$ and verify whether the system satisfies the Hawkins-Simon conditions for economic viability.
3. Compute the Leontief Inverse Matrix $(I - A)^{-1}$.
4. Suppose national economic planning targets an increase in final demand to $F^* = [160, \\; 220]^T$ over the next three years. Calculate the new gross output levels required from Agriculture and Manufacturing to fulfill this plan.

### Solution, step 1: Computation of Technology Matrix $A$
The technical coefficient formula is $a_{ij} = x_{ij} / X_j$:
- For Sector 1 (Agriculture, $X_1 = 200$):
  $$a_{11} = \\frac{x_{11}}{X_1} = \\frac{30}{200} = 0.15$$
  $$a_{21} = \\frac{x_{21}}{X_1} = \\frac{40}{200} = 0.20$$
- For Sector 2 (Manufacturing, $X_2 = 200$):
  $$a_{12} = \\frac{x_{12}}{X_2} = \\frac{60}{200} = 0.30$$
  $$a_{22} = \\frac{x_{22}}{X_2} = \\frac{20}{200} = 0.10$$

The Technology Matrix $A$ is:
$$A = \\begin{bmatrix} 0.15 & 0.30 \\\\ 0.20 & 0.10 \\end{bmatrix}$$

### Solution, step 2: Hawkins-Simon Viability Verification
We construct the Leontief matrix $M = (I - A)$:
$$I - A = \\begin{bmatrix} 1 - 0.15 & -0.30 \\\\ -0.20 & 1 - 0.10 \\end{bmatrix} = \\begin{bmatrix} 0.85 & -0.30 \\\\ -0.20 & 0.90 \\end{bmatrix}$$

We evaluate the Hawkins-Simon conditions:
1. **First-order leading principal minor**:
   $$M_1 = 1 - a_{11} = 0.85 > 0 \\quad \\text{(Satisfied)}$$
2. **Second-order leading principal minor (Determinant of $I - A$)**:
   $$\\det(I - A) = (0.85)(0.90) - (-0.30)(-0.20) = 0.7650 - 0.0600 = 0.7050 > 0 \\quad \\text{(Satisfied)}$$

Both principal minors are strictly positive ($\det(I-A) = 0.7050 > 0$). Therefore, the Hawkins-Simon conditions are fully satisfied, proving that this two-sector economy is economically viable and capable of sustaining positive net final demand.

### Solution, step 3: Computation of the Leontief Inverse Matrix $(I - A)^{-1}$
For a $2 \\times 2$ matrix $M = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}$, the inverse is:
$$M^{-1} = \\frac{1}{ad - bc} \\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix}$$

Applying this to $I - A$:
$$(I - A)^{-1} = \\frac{1}{0.7050} \\begin{bmatrix} 0.90 & 0.30 \\\\ 0.20 & 0.85 \\end{bmatrix}$$

Evaluating each entry:
- $l_{11} = \\frac{0.90}{0.7050} = \\frac{90}{70.5} = \\frac{6}{4.7} \\approx 1.2766$
- $l_{12} = \\frac{0.30}{0.7050} = \\frac{30}{70.5} = \\frac{2}{4.7} \\approx 0.4255$
- $l_{21} = \\frac{0.20}{0.7050} = \\frac{20}{70.5} = \\frac{4}{14.1} \\approx 0.2837$
- $l_{22} = \\frac{0.85}{0.7050} = \\frac{85}{70.5} = \\frac{17}{14.1} \\approx 1.2057$

The Leontief Inverse Matrix is:
$$(I - A)^{-1} = \\begin{bmatrix} 1.2766 & 0.4255 \\\\ 0.2837 & 1.2057 \\end{bmatrix}$$

### Solution, step 4: Gross Output Projections for New Final Demand
The target final demand vector is:
$$F^* = \\begin{bmatrix} 160 \\\\ 220 \\end{bmatrix}$$

Using the Leontief inverse:
$$X^* = (I - A)^{-1} F^* = \\begin{bmatrix} 1.2766 & 0.4255 \\\\ 0.2837 & 1.2057 \\end{bmatrix} \\begin{bmatrix} 160 \\\\ 220 \\end{bmatrix}$$

Carrying out the matrix multiplication:
- **Required Agricultural Gross Output ($X_1^*$)**:
  $$X_1^* = (1.2766 \\times 160) + (0.4255 \\times 220) = 204.256 + 93.610 = \\mathbf{297.87} \\text{ million}$$
- **Required Manufacturing Gross Output ($X_2^*$)**:
  $$X_2^* = (0.2837 \\times 160) + (1.2057 \\times 220) = 45.392 + 265.254 = \\mathbf{310.65} \\text{ million}$$

To fulfill the expansion in final demand, agricultural production must expand by $48.9\\%$ (from $\\$200\\text{M}$ to $\\$297.87\\text{M}$), and manufacturing production must expand by $55.3\\%$ (from $\\$200\\text{M}$ to $\\$310.65\\text{M}$).

---

### Question 2: Employment Multipliers and Value-Added Decomposition
A tripartite regional development agency models three key sectors: **Energy ($1$)**, **Heavy Industry ($2$)**, and **Services ($3$)**.
The Leontief Inverse Matrix $(I - A)^{-1}$ is established as:

$$(I - A)^{-1} = \\begin{bmatrix}
1.30 & 0.25 & 0.15 \\\\
0.40 & 1.45 & 0.20 \\\\
0.30 & 0.35 & 1.25
\\end{bmatrix}$$

The direct labor employment requirements per million dollars of gross output (labor coefficients $l_i$) are:
- Energy ($1$): $l_1 = 4.0$ workers per $\\$1\\text{M}$ output (highly capital intensive)
- Heavy Industry ($2$): $l_2 = 12.0$ workers per $\\$1\\text{M}$ output
- Services ($3$): $l_3 = 25.0$ workers per $\\$1\\text{M}$ output (labor intensive)

1. Calculate the **Output Multiplier** for each of the three sectors and identify which sector generates the greatest total economic output expansion per unit of final demand.
2. Formulate the total direct and indirect labor coefficient vector $e = l^T (I - A)^{-1}$ and compute the **Employment Multipliers** ($e_j$) for all three sectors.
3. Suppose the regional government has a $\\$50\\text{M}$ infrastructure stimulus budget. Compare the total employment generated by allocating the entire $\\$50\\text{M}$ to Heavy Industry versus allocating it to Services.

### Solution, step 1: Computation of Output Multipliers
The output multiplier $O_j$ is the sum of column $j$ of $(I - A)^{-1}$:
- **Energy ($j=1$)**:
  $$O_1 = \\sum_{i=1}^{3} l_{i1} = 1.30 + 0.40 + 0.30 = \\mathbf{2.00}$$
  Every $\\$1.00$ increase in final demand for energy generates $\\$2.00$ in total gross output across the economy.
- **Heavy Industry ($j=2$)**:
  $$O_2 = \\sum_{i=1}^{3} l_{i2} = 0.25 + 1.45 + 0.35 = \\mathbf{2.05}$$
  Every $\\$1.00$ increase in heavy industry demand generates $\\$2.05$ in total output.
- **Services ($j=3$)**:
  $$O_3 = \\sum_{i=1}^{3} l_{i3} = 0.15 + 0.20 + 1.25 = \\mathbf{1.60}$$
  Every $\\$1.00$ increase in services demand generates $\\$1.60$ in total output.

**Assessment**: Heavy Industry exhibits the highest output multiplier ($O_2 = 2.05$), owing to its extensive backward supply linkages with raw materials, energy, and subcontracted business services.

### Solution, step 2: Total Employment Multipliers
The vector of total direct plus indirect labor requirements per unit of final demand is:
$$e = l^T (I - A)^{-1} = [l_1, l_2, l_3] \\begin{bmatrix}
l_{11} & l_{12} & l_{13} \\\\
l_{21} & l_{22} & l_{23} \\\\
l_{31} & l_{32} & l_{33}
\\end{bmatrix}$$

With $l = [4.0, \\; 12.0, \\; 25.0]$:
1. **Employment Multiplier for Energy ($e_1$)**:
   $$e_1 = (4.0 \\times 1.30) + (12.0 \\times 0.40) + (25.0 \\times 0.30) = 5.20 + 4.80 + 7.50 = \\mathbf{17.50} \\text{ jobs per \\$1M}$$
   *(Note: While energy directly employs only 4 workers per $\\$1\\text{M}$, its supply chain demand creates another 13.5 indirect jobs in manufacturing and services).*
2. **Employment Multiplier for Heavy Industry ($e_2$)**:
   $$e_2 = (4.0 \\times 0.25) + (12.0 \\times 1.45) + (25.0 \\times 0.35) = 1.00 + 17.40 + 8.75 = \\mathbf{27.15} \\text{ jobs per \\$1M}$$
3. **Employment Multiplier for Services ($e_3$)**:
   $$e_3 = (4.0 \\times 0.15) + (12.0 \\times 0.20) + (25.0 \\times 1.25) = 0.60 + 2.40 + 31.25 = \\mathbf{34.25} \\text{ jobs per \\$1M}$$

### Solution, step 3: Evaluation of the $\\$50\text{M}$ Stimulus Allocation
We multiply the total employment multipliers by the $\\$50\\text{M}$ shock:
- **Heavy Industry Stimulus**:
  $$\\text{Total Jobs Created} = 50 \\times 27.15 = \\mathbf{1{,}357.5} \\text{ jobs}$$
- **Services Stimulus**:
  $$\\text{Total Jobs Created} = 50 \\times 34.25 = \\mathbf{1{,}712.5} \\text{ jobs}$$

**Policy Trade-off**:
Allocating the $\\$50\\text{M}$ to Services creates **$355$ more jobs** ($+26.1\\%$) than Heavy Industry, because Services is inherently labor intensive. However, Heavy Industry stimulates a broader industrial base ($O_2 = 2.05$ vs $1.60$). Policymakers pursuing maximum immediate job creation should prioritize Services, whereas those seeking industrial capital deepening and supply-chain resilience should favor Heavy Industry.

---

### Question 3: Social Accounting Matrix (SAM) Balancing Identity
An economy's macro-transactions are recorded in a stylized Social Accounting Matrix with five aggregated accounts:
1. **Activities ($A$)** (Production)
2. **Commodities ($C$)** (Markets)
3. **Factors of Production ($F$)** (Labor & Capital)
4. **Domestic Institutions ($H$)** (Households & Government)
5. **Rest of the World ($W$)** (International Trade)

The transaction matrix (in billions of dollars) with two missing values, $X$ and $Y$, is:

| Accounts | $A$ | $C$ | $F$ | $H$ | $W$ | **Total Receipts** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Activities ($A$)** | $0$ | $450$ | $0$ | $0$ | $50$ | **$500$** |
| **Commodities ($C$)** | $120$ | $0$ | $0$ | $X$ | $60$ | **Row Total $C$** |
| **Factors ($F$)** | $380$ | $0$ | $0$ | $0$ | $0$ | **$380$** |
| **Institutions ($H$)** | $0$ | $0$ | $380$ | $20$ | $10$ | **$410$** |
| **Rest of World ($W$)** | $0$ | $30$ | $0$ | $Y$ | $0$ | **Row Total $W$** |
| **Total Outlays** | **$500$** | **Col Total $C$** | **$380$** | **$410$** | **$120$** | — |

1. Formulate the fundamental row-and-column accounting identity governing all Social Accounting Matrices.
2. Solve for the missing household/institution consumption expenditure $X$ and foreign transfer $Y$.
3. Compute the Gross Domestic Product ($\text{GDP}$) of this economy from the SAM entries using the Value-Added Approach and confirm it against the Final Expenditure Approach.

### Solution, step 1: The SAM Balancing Identity
A Social Accounting Matrix is a closed double-entry system. For every account $k$:
$$\\text{Total Receipts (Row } k \\text{ Total)} \\equiv \\text{Total Outlays (Column } k \\text{ Total)}$$

No leakages or unrecorded injections are permitted; all revenues received must be completely accounted for in expenditures or savings.

### Solution, step 2: Solving for Missing Variables $X$ and $Y$
1. **Analyze Account 4 (Institutions $H$)**:
   The column total of Institutions is given as $410$:
   $$\\text{Outlays of } H = X + 20 + Y = 410 \\implies X + Y = 390$$

2. **Analyze Account 5 (Rest of the World $W$)**:
   The column total of $W$ is given as $120$:
   $$\\text{Row Total of } W = \\text{Column Total of } W = 120$$
   From Row 5:
   $$\\text{Row Total of } W = 0 + 30 + 0 + Y + 0 = 30 + Y$$
   Setting Row Total equal to Column Total:
   $$30 + Y = 120 \\implies Y = 120 - 30 = \\mathbf{90} \\text{ billion}$$

3. **Solve for $X$**:
   Since $X + Y = 390$:
   $$X = 390 - 90 = \\mathbf{300} \\text{ billion}$$

4. **Verify Account 2 (Commodities $C$)**:
   - Row Total of $C$:
     $$\\text{Row Total} = 120 + 0 + 0 + X + 60 = 120 + 300 + 60 = \\mathbf{480} \\text{ billion}$$
   - Column Total of $C$:
     $$\\text{Col Total} = 450 + 0 + 0 + 0 + 30 = \\mathbf{480} \\text{ billion}$$
   Row Total ($480$) matches Column Total ($480$) perfectly!

### Solution, step 3: GDP Verification from the Balanced SAM
1. **Value-Added Approach**:
   Factor payments generated by domestic Activities (Account $A$ payments to Account $F$):
   $$\\text{GDP} = \\text{Payments to Factors} = \\mathbf{380} \\text{ billion}$$
   Alternatively, Gross Output of Activities is $500$, and intermediate input purchases from Commodities are $120$:
   $$\\text{GDP} = \\text{Gross Output} - \\text{Intermediate Consumption} = 500 - 120 = \\mathbf{380} \\text{ billion}$$

2. **Final Expenditure Approach**:
   Final demand purchases of domestic Commodities comprise:
   - Domestic Household/Institution Consumption ($X$): $300$
   - Exports ($C$ to $W$ plus direct $A$ exports to $W$):
     - Commodity Exports ($C$ to $W$): $60$
     - Activity Direct Exports ($A$ to $W$): $50$
     - Total Exports: $60 + 50 = 110$
   - Imports ($W$ sales to Commodities $C$): $30$
   - Net Exports: $110 - 30 = 80$

   Total Final Expenditure:
   $$\\text{GDP} = C + (X - M) = 300 + 80 = \\mathbf{380} \\text{ billion}$$

Both perspectives confirm $\\text{GDP} = \\mathbf{380}$ billion, verifying structural consistency.
"""

(OUT_DIR / "unit-7.md").write_text(u7_content, encoding="utf-8")
print(f"Unit 7: {prose_count(u7_content)} words")

# ==========================================
# UNIT 8: STATISTICAL DEMAND, SUPPLY & ECONOMETRIC ELASTICITY ANALYSIS
# ==========================================

u8_content = """# Unit 8: Statistical Demand, Supply & Econometric Elasticity Analysis

## Microeconomic Foundations of Demand and Supply Functions

The empirical estimation of market demand and supply relationships bridges abstract microeconomic theory and real-world commercial and macroeconomic policy. In competitive markets, resource allocation, consumer welfare, tax incidence, and monopoly markups hinge on the precise quantitative responsiveness of consumers and producers to shifts in prices and incomes.

Under Marshallian consumer optimization, an individual consumer maximizes an ordinal utility function $U(q_1, q_2, \\dots, q_n)$ subject to the linear budget constraint $\\sum p_i q_i \\le M$, where $M$ denotes nominal money income. The resulting first-order conditions yield the **Marshallian Demand Functions**:

$$q_i = D_i(p_1, p_2, \\dots, p_n, M), \\quad i = 1, 2, \\dots, n$$

Marshallian demand functions satisfy three fundamental mathematical properties:
1. **Homogeneity of Degree Zero**: Multiplying all prices and money income by an arbitrary positive scalar $\\lambda > 0$ leaves physical quantity demanded unchanged (absence of money illusion):
   $$D_i(\\lambda p, \\lambda M) = D_i(p, M)$$
2. **Engel Aggregation**: The income-weighted sum of income elasticities equals unity:
   $$\\sum_{i=1}^{n} w_i \\eta_{i,M} = 1$$
   where $w_i = (p_i q_i)/M$ is the expenditure budget share of good $i$.
3. **Cournot Aggregation**: The expenditure-weighted sum of price elasticities across goods satisfies:
   $$\\sum_{i=1}^{n} w_i \\eta_{ij} = -w_j$$

---

## Mathematical Elasticity Metrics

In statistical economics, elasticity is defined as the dimensionless ratio of the proportional change in quantity to the proportional change in an underlying economic driver.

### 1. Own-Price Elasticity of Demand ($\\eta_p$)
- **Point Elasticity**: For a continuous, differentiable demand curve $Q = D(P)$:
  $$\\eta_p = \\lim_{\\Delta P \\to 0} \\left( \\frac{\\Delta Q / Q}{\\Delta P / P} \\right) = \\frac{dQ}{dP} \\times \\frac{P}{Q} = \\frac{d \\ln(Q)}{d \\ln(P)}$$
  By the Law of Demand, $dQ/dP < 0$, so $\\eta_p$ is typically negative. In empirical economic literature, analysts either report the signed value (e.g., $-1.5$) or reference its absolute magnitude $|\\eta_p|$.
  - $|\\eta_p| > 1$: Price Elastic (proportional quantity response exceeds price change).
  - $|\\eta_p| = 1$: Unitary Elastic (total expenditure $P \\times Q$ remains constant).
  - $0 \\le |\\eta_p| < 1$: Price Inelastic (proportional quantity response is smaller than price change).

- **Arc Elasticity (Midpoint Formula)**: When evaluating discrete price changes between $(P_1, Q_1)$ and $(P_2, Q_2)$, calculating elasticity relative to the initial point yields different results than calculating relative to the final point. To guarantee symmetry and path-invariance, economists use the **Allen-Bowley Midpoint Arc Elasticity Formula**:
  $$\\eta_{\\text{arc}} = \\frac{Q_2 - Q_1}{\\frac{Q_1 + Q_2}{2}} \\div \\frac{P_2 - P_1}{\\frac{P_1 + P_2}{2}} = \\frac{Q_2 - Q_1}{P_2 - P_1} \\times \\frac{P_1 + P_2}{Q_1 + Q_2}$$

### 2. Income Elasticity of Demand ($\\eta_M$)
Income elasticity measures consumer responsiveness to changes in real household income $M$:

$$\\eta_M = \\frac{dQ}{dM} \\times \\frac{M}{Q} = \\frac{d \\ln(Q)}{d \\ln(M)}$$

- **Normal Goods** ($\\eta_M > 0$): Consumption expands as income increases.
  - **Necessities** ($0 < \\eta_M \\le 1$): Expenditure increases slower than income; budget share $w_i$ contracts.
  - **Luxuries** ($\\eta_M > 1$): Expenditure expands faster than income; budget share $w_i$ rises.
- **Inferior Goods** ($\\eta_M < 0$): Consumption contracts as income increases (e.g., coarse staple grains, low-cost transit).

### 3. Cross-Price Elasticity of Demand ($\\eta_{ij}$)
Cross-price elasticity measures the percentage shift in quantity demanded of commodity $i$ induced by a one-percent change in the price of a separate commodity $j$:

$$\\eta_{ij} = \\frac{\\partial Q_i}{\\partial P_j} \\times \\frac{P_j}{Q_i} = \\frac{\\partial \\ln(Q_i)}{\\partial \\ln(P_j)}$$

- **Substitutes** ($\\eta_{ij} > 0$): A price hike in good $j$ shifts demand toward good $i$ (e.g., tea and coffee, gasoline and electric vehicles).
- **Complements** ($\\eta_{ij} < 0$): A price hike in good $j$ depresses demand for good $i$ (e.g., automobiles and motor fuel, hardware and software).
- **Independent Goods** ($\\eta_{ij} = 0$).

---

## Engel Curves and Engel's Law

An **Engel Curve** traces the equilibrium relationship between the quantity demanded (or expenditure) of a specific commodity and household income $M$, holding all market prices constant.

In 1857, the German statistician Ernst Engel discovered the empirical regularity known as **Engel's Law**: as household income rises, the proportion of income allocated to food declines, even if the absolute monetary expenditure on food increases:

$$\\frac{d}{dM} \\left( \\frac{p_{\\text{food}} q_{\\text{food}}}{M} \\right) < 0 \\iff \\eta_{\\text{food}, M} < 1$$

To fit empirical consumer survey data, economists deploy several parametric functional specifications:

| Functional Form | Mathematical Equation | Implied Income Elasticity ($\\eta_M$) | Economic Characteristics |
| :--- | :--- | :--- | :--- |
| **Linear** | $Q = a + b M$ | $\\eta_M = b \\frac{M}{Q} = \\frac{b M}{a + b M}$ | Approaches 1 as $M \\to \\infty$; lacks asymptotic saturation. |
| **Semi-Logarithmic** | $Q = a + b \\ln(M)$ | $\\eta_M = \\frac{b}{Q}$ | Elasticity declines as consumption grows; suitable for basic necessities. |
| **Double-Logarithmic** | $\\ln(Q) = a + b \\ln(M)$ | $\\eta_M = b = \\text{constant}$ | Constant elasticity across all income brackets; widespread in empirical studies. |
| **Inverse** | $Q = a - \\frac{b}{M}$ | $\\eta_M = \\frac{b}{M Q}$ | Possesses an upper physical saturation asymptote ($Q \\to a$ as $M \\to \\infty$). |

---

## Econometric Estimation and the Identification Problem

In empirical research, estimating demand and supply parameters from observational market data introduces deep econometric challenges.

### The Double-Log Econometric Demand Specification
A standard Cobb-Douglas type empirical demand function is formulated as:

$$Q_t = A P_t^{\\beta_1} M_t^{\\beta_2} P_{c,t}^{\\beta_3} e^{u_t}$$

Taking natural logarithms linearizes the parameters:

$$\\ln(Q_t) = \\beta_0 + \\beta_1 \\ln(P_t) + \\beta_2 \\ln(M_t) + \\beta_3 \\ln(P_{c,t}) + u_t$$

where:
- $\\beta_0 = \\ln(A)$ is the intercept.
- $\\beta_1 = \\frac{\\partial \\ln(Q)}{\\partial \\ln(P)}$ is the constant own-price elasticity of demand.
- $\\beta_2 = \\frac{\\partial \\ln(Q)}{\\partial \\ln(M)}$ is the constant income elasticity of demand.
- $\\beta_3 = \\frac{\\partial \\ln(Q)}{\\partial \\ln(P_c)}$ is the cross-price elasticity.
- $u_t \\sim \\text{iid}(0, \\sigma^2)$ is the random disturbance term.

Because variables are in logarithmic units, the estimated OLS regression coefficients directly yield the theoretical elasticities without requiring post-estimation conversion.

### The Simultaneity and Identification Problem (Working's Theorem)
First formalized by E. J. Working in 1927, the **Identification Problem** warns that observable market data $(P_t, Q_t)$ represent simultaneous equilibrium intersections of shifting supply and demand curves:

$$\\begin{cases}
Q_t^D = \\alpha_0 + \\alpha_1 P_t + u_t \\\\
Q_t^S = \\beta_0 + \\beta_1 P_t + v_t
\\end{cases}$$

If an analyst simply runs an OLS regression of $Q_t$ on $P_t$, the resulting regression line traces neither the demand curve nor the supply curve, but a meaningless hybrid path of moving intersection points.

#### Conditions for Identification:
1. **Identification of the Demand Curve**: The demand curve is statistically identified if and only if there exists an exogenous instrument or supply-shifter variable (such as rainfall, agricultural fertilizer costs, or manufacturing wage shocks) that enters the supply equation but is strictly excluded from the demand equation. Shifting the supply curve back and forth across a stable demand curve traces out the demand schedule.
2. **Identification of the Supply Curve**: The supply curve is identified if and only if there exists an exogenous demand-shifter (such as consumer income or demographic population size) that shifts the demand curve across a stable supply curve.

---

## Worked Questions and Solutions

### Question 1: Econometric Estimation of a Double-Log Demand Curve
An econometrician estimates the aggregate domestic demand for residential electrical power (in megawatt-hours, $Q$) as a function of average retail electricity price per kilowatt-hour ($P$, in cents) and median household disposable income ($M$, in thousands of dollars). A five-year historical dataset provides the following paired observations:

| Year ($t$) | Consumption ($Q_t$) | Price ($P_t$) | Income ($M_t$) |
| :---: | :---: | :---: | :---: |
| 1 | $120.0$ | $12.0$ | $40.0$ |
| 2 | $112.0$ | $14.0$ | $42.0$ |
| 3 | $105.0$ | $16.0$ | $44.0$ |
| 4 | $108.0$ | $15.0$ | $48.0$ |
| 5 | $118.0$ | $13.0$ | $50.0$ |

1. Formulate the log-linear empirical demand regression model $\\ln(Q_t) = \\beta_0 + \\beta_1 \\ln(P_t) + \\beta_2 \\ln(M_t) + u_t$.
2. Transform the observations into natural logarithms and formulate the OLS normal equations.
3. Given the estimated parameter vector $[\\hat{\\beta}_0 = 3.652, \\; \\hat{\\beta}_1 = -0.684, \\; \\hat{\\beta}_2 = +0.521]$, state the own-price elasticity and income elasticity of demand.
4. Classify electricity according to economic elasticity criteria (elastic vs inelastic, necessity vs luxury), and predict the percentage change in power consumption if retail electricity prices rise by $8.0\\%$ while median household income rises by $4.0\\%$.

### Solution, step 1: Model Formulation
The empirical Cobb-Douglas demand specification is:
$$Q_t = A P_t^{\\beta_1} M_t^{\\beta_2} e^{u_t}$$

Taking the natural logarithm of both sides:
$$\\ln(Q_t) = \\beta_0 + \\beta_1 \\ln(P_t) + \\beta_2 \\ln(M_t) + u_t$$

where:
- $\\beta_0 = \\ln(A)$ is the autonomous intercept.
- $\\beta_1 = \\frac{\\partial \\ln(Q)}{\\partial \\ln(P)}$ is the constant own-price elasticity of demand.
- $\\beta_2 = \\frac{\\partial \\ln(Q)}{\\partial \\ln(M)}$ is the constant income elasticity of demand.

### Solution, step 2: Logarithmic Transformation of Data
Let us compute the natural logarithms:
- $y_t = \\ln(Q_t)$
- $x_{1t} = \\ln(P_t)$
- $x_{2t} = \\ln(M_t)$

Computations:
- **Year 1**:
  - $y_1 = \\ln(120.0) \\approx 4.7875$
  - $x_{11} = \\ln(12.0) \\approx 2.4849$
  - $x_{21} = \\ln(40.0) \\approx 3.6889$
- **Year 2**:
  - $y_2 = \\ln(112.0) \\approx 4.7185$
  - $x_{12} = \\ln(14.0) \\approx 2.6391$
  - $x_{22} = \\ln(42.0) \\approx 3.7377$
- **Year 3**:
  - $y_3 = \\ln(105.0) \\approx 4.6540$
  - $x_{13} = \\ln(16.0) \\approx 2.7726$
  - $x_{23} = \\ln(44.0) \\approx 3.7842$
- **Year 4**:
  - $y_4 = \\ln(108.0) \\approx 4.6821$
  - $x_{14} = \\ln(15.0) \\approx 2.7081$
  - $x_{24} = \\ln(48.0) \\approx 3.8712$
- **Year 5**:
  - $y_5 = \\ln(118.0) \\approx 4.7707$
  - $x_{15} = \\ln(13.0) \\approx 2.5649$
  - $x_{25} = \\ln(50.0) \\approx 3.9120$

Summing each vector across the $N = 5$ observations:
$$\\sum y = 23.6128, \\quad \\sum x_1 = 13.1696, \\quad \\sum x_2 = 18.9940$$

The standard matrix OLS estimator is:
$$\\hat{\\beta} = (X^T X)^{-1} X^T y$$

### Solution, step 3: Elasticity Parameter Interpretation
From the estimated regression:
$$\\ln(Q) = 3.652 - 0.684 \\ln(P) + 0.521 \\ln(M)$$

- **Own-Price Elasticity of Demand**:
  $$\\eta_p = \\hat{\\beta}_1 = \\mathbf{-0.684}$$
  A $1.0\\%$ increase in retail electricity prices leads to a $0.684\\%$ reduction in power consumption.
- **Income Elasticity of Demand**:
  $$\\eta_M = \\hat{\\beta}_2 = \\mathbf{+0.521}$$
  A $1.0\\%$ increase in household disposable income leads to a $0.521\\%$ increase in power consumption.

### Solution, step 4: Economic Classification and Forecast Shock
1. **Economic Classification**:
   - Price Elasticity: $|\\eta_p| = 0.684 < 1.0$, indicating that residential electricity demand is **Price Inelastic**. Electricity has few short-run substitutes for lighting, refrigeration, and home appliances. An increase in price will raise total revenue for utilities ($d(PQ)/dP > 0$).
   - Income Elasticity: $0 < \\eta_M = 0.521 < 1.0$, indicating that electricity is a **Normal Necessity Good**. As households become wealthier, their electricity use expands, but its share in the total household budget declines, conforming to Engel's Law.

2. **Forecasting Demand Response under Simultaneous Shocks**:
   Taking the total differential of the log demand function:
   $$\\frac{dQ}{Q} \\approx \\beta_1 \\left( \\frac{dP}{P} \\right) + \\beta_2 \\left( \\frac{dM}{M} \\right)$$

   With a price increase $\\frac{dP}{P} = +8.0\\%$ and an income increase $\\frac{dM}{M} = +4.0\\%$:
   $$\\frac{dQ}{Q} \\approx (-0.684)(+8.0\\%) + (+0.521)(+4.0\\%)$$
   $$\\frac{dQ}{Q} \\approx -5.472\\% + 2.084\\% = \\mathbf{-3.388\\%}$$

Residential electricity consumption is projected to contract by approximately **$3.39\\%$**. The contractionary price effect ($-5.47\\%$) outweighs the expansionary income effect ($+2.08\\%$).

---

### Question 2: Point vs Arc Elasticity and Cross-Price Interdependence
A telecommunications conglomerate analyzes subscriber plans for mobile streaming services and fiber broadband. A price adjustment produces the following market response:

- Phase 1: Fiber broadband price is $P_1 = \\$50.00$ per month; subscription volume is $Q_1 = 100{,}000$ households.
- Phase 2: Fiber broadband price is reduced to $P_2 = \\$40.00$ per month; subscription volume expands to $Q_2 = 140{,}000$ households.
- Simultaneously, subscriptions to an affiliated 5G Home Wireless service ($Q_{\\text{wireless}}$) drop from $40{,}000$ to $32{,}000$ subscribers, despite its own price remaining fixed at $\\$45.00$.

1. Compute the price elasticity of demand for fiber broadband using the initial point formula, the final point formula, and the Bowley-Allen Midpoint Arc Elasticity formula.
2. Explain why the midpoint arc elasticity is theoretically preferred for non-marginal price changes.
3. Compute the **Cross-Price Elasticity of Demand** between 5G Home Wireless and fiber broadband using the midpoint formula.
4. Classify the relationship between fiber broadband and 5G Home Wireless (substitutes or complements), and evaluate whether the broadband price cut maximized total broadband revenue.

### Solution, step 1: Price Elasticity Computation
We have:
$$P_1 = 50, \\quad P_2 = 40 \\implies \\Delta P = P_2 - P_1 = -10$$
$$Q_1 = 100{,}000, \\quad Q_2 = 140{,}000 \\implies \\Delta Q = Q_2 - Q_1 = +40{,}000$$

1. **Initial Point Elasticity**:
   $$\\eta_{\\text{initial}} = \\frac{\\Delta Q}{\\Delta P} \\times \\frac{P_1}{Q_1} = \\frac{40{,}000}{-10} \\times \\frac{50}{100{,}000} = -4{,}000 \\times 0.0005 = \\mathbf{-2.00}$$

2. **Final Point Elasticity**:
   $$\\eta_{\\text{final}} = \\frac{\\Delta Q}{\\Delta P} \\times \\frac{P_2}{Q_2} = \\frac{40{,}000}{-10} \\times \\frac{40}{140{,}000} = -4{,}000 \\times 0.0002857 \\approx \\mathbf{-1.14}$$

3. **Midpoint Arc Elasticity (Bowley-Allen Formula)**:
   $$\\bar{P} = \\frac{P_1 + P_2}{2} = \\frac{50 + 40}{2} = 45.00$$
   $$\\bar{Q} = \\frac{Q_1 + Q_2}{2} = \\frac{100{,}000 + 140{,}000}{2} = 120{,}000$$
   $$\\eta_{\\text{arc}} = \\frac{\\Delta Q}{\\Delta P} \\times \\frac{\\bar{P}}{\\bar{Q}} = \\frac{40{,}000}{-10} \\times \\frac{45}{120{,}000} = -4{,}000 \\times 0.000375 = \\mathbf{-1.50}$$

### Solution, step 2: Methodological Superiority of Midpoint Arc Formula
The point elasticity formula yields contradictory results depending on the arbitrary choice of baseline: $\\eta = -2.00$ moving from $\\$50$ to $\\$40$, but $\\eta = -1.14$ moving from $\\$40$ to $\\$50$.
The Midpoint Arc Elasticity formula averages the end-points, ensuring path symmetry: the elasticity between two prices is identical whether the price rises or falls. For non-marginal price shifts (such as a $20\\%$ price cut), the midpoint formula provides an unbiased estimate of average responsiveness.

### Solution, step 3: Cross-Price Elasticity Computation
Let $Q_w$ denote 5G Home Wireless subscriptions, and $P_b$ denote fiber broadband price:
- $P_{b1} = 50, \\; P_{b2} = 40 \\implies \\Delta P_b = -10, \\; \\bar{P}_b = 45$
- $Q_{w1} = 40{,}000, \\; Q_{w2} = 32{,}000 \\implies \\Delta Q_w = 32{,}000 - 40{,}000 = -8{,}000$
- $\\bar{Q}_w = \\frac{40{,}000 + 32{,}000}{2} = 36{,}000$

Applying the midpoint formula:
$$\\eta_{w, b} = \\frac{\\Delta Q_w}{\\Delta P_b} \\times \\frac{\\bar{P}_b}{\\bar{Q}_w} = \\frac{-8{,}000}{-10} \\times \\frac{45}{36{,}000} = (+800) \\times 0.00125 = \\mathbf{+1.00}$$

### Solution, step 4: Economic Classification and Total Revenue Analysis
1. **Classification**:
   The cross-price elasticity is positive ($\\eta_{w, b} = +1.00 > 0$). When fiber broadband became cheaper, consumers abandoned 5G wireless in favor of fiber. Hence, fiber broadband and 5G Home Wireless are **Substitutes**. Because $\\eta_{w, b} = 1.00$, the substitution response is unitary: a $1.0\\%$ drop in fiber prices induces a $1.0\\%$ contraction in wireless subscribers.

2. **Total Revenue Impact**:
   - Initial Total Revenue:
     $$\\text{TR}_1 = P_1 \\times Q_1 = \\$50.00 \\times 100{,}000 = \\mathbf{\\$5{,}000{,}000} \\text{ per month}$$
   - New Total Revenue:
     $$\\text{TR}_2 = P_2 \\times Q_2 = \\$40.00 \\times 140{,}000 = \\mathbf{\\$5{,}600{,}000} \\text{ per month}$$
   - Revenue Change:
     $$\\Delta \\text{TR} = \\$5{,}600{,}000 - \\$5{,}000{,}000 = \\mathbf{+\\$600{,}000} \\quad (+12.0\\%)$$

Because demand is price elastic ($|\\eta_{\\text{arc}}| = 1.50 > 1.0$), the $40\\%$ surge in volume comfortably outstripped the $20\\%$ price reduction, successfully increasing total corporate revenue.

---

### Question 3: Empirical Engel Curve Fitting and Saturation Limits
A socio-demographic study investigates the relationship between monthly household disposable income ($M$, in hundreds of dollars) and monthly expenditure on fresh dairy and meat products ($E$, in dollars). Data from six representative household income cohorts are recorded:

| Cohort ($i$) | Income ($M$) | Food Expenditure ($E$) | Food Share ($w = E / (100 M)$) |
| :---: | :---: | :---: | :---: |
| 1 | $10$ | $150$ | $150 / 1{,}000 = 15.0\\%$ |
| 2 | $20$ | $240$ | $240 / 2{,}000 = 12.0\\%$ |
| 3 | $30$ | $300$ | $300 / 3{,}000 = 10.0\\%$ |
| 4 | $40$ | $340$ | $340 / 4{,}000 = 8.5\\%$ |
| 5 | $50$ | $370$ | $370 / 5{,}000 = 7.4\\%$ |
| 6 | $60$ | $390$ | $390 / 6{,}000 = 6.5\\%$ |

1. Examine whether the empirical food budget shares conform to Engel's Law.
2. Consider an inverse Engel curve specification: $E_i = a - \\frac{b}{M_i}$. Formulate the variable transformation $z_i = 1 / M_i$ to express the model in linear OLS form $E_i = a - b z_i$.
3. Compute the OLS estimates of $a$ and $b$, and state the fitted inverse Engel curve equation.
4. Calculate the theoretical upper expenditure saturation ceiling ($a$) as income approaches infinity, and compute the expenditure elasticity of demand at an income of $M = 20$ versus $M = 60$.

### Solution, step 1: Verification of Engel's Law
Looking at the fourth column of the empirical schedule:
- As monthly income rises from $\\$1{,}000$ ($M = 10$) to $\\$6{,}000$ ($M = 60$), absolute food expenditure rises from $\\$150$ to $\\$390$.
- Simultaneously, the food budget share falls monotonically from **$15.0\\%$ down to $6.5\\%$**.
Because the proportion of income spent on food diminishes as income expands, the data rigorously conform to **Engel's Law**. Fresh food behaves as an essential necessity.

### Solution, step 2: Linear Transformation of the Inverse Model
The inverse Engel specification is:
$$E = a - b \\left( \\frac{1}{M} \\right)$$

Defining the reciprocal variable $z = 1/M$, the model becomes a standard bivariate linear equation:
$$E = a - b z$$
where $a$ represents the asymptotic saturation limit as $M \\to \\infty$ ($z \\to 0$), and $-b$ is the slope with respect to $z$.

### Solution, step 3: OLS Parameter Estimation
Let us compute $z_i = 1/M_i$, $z_i^2$, and $z_i E_i$ for each cohort:
- Cohort 1: $M_1 = 10 \\implies z_1 = 0.1000$; $E_1 = 150$; $z_1^2 = 0.010000$; $z_1 E_1 = 15.00$
- Cohort 2: $M_2 = 20 \\implies z_2 = 0.0500$; $E_2 = 240$; $z_2^2 = 0.002500$; $z_2 E_2 = 12.00$
- Cohort 3: $M_3 = 30 \\implies z_3 = 0.0333$; $E_3 = 300$; $z_3^2 = 0.001109$; $z_3 E_3 = 10.00$
- Cohort 4: $M_4 = 40 \\implies z_4 = 0.0250$; $E_4 = 340$; $z_4^2 = 0.000625$; $z_4 E_4 = 8.50$
- Cohort 5: $M_5 = 50 \\implies z_5 = 0.0200$; $E_5 = 370$; $z_5^2 = 0.000400$; $z_5 E_5 = 7.40$
- Cohort 6: $M_6 = 60 \\implies z_6 = 0.0167$; $E_6 = 390$; $z_6^2 = 0.000279$; $z_6 E_6 = 6.50$

Summing over the $N = 6$ observations:
- $\\sum z = 0.1000 + 0.0500 + 0.0333 + 0.0250 + 0.0200 + 0.0167 = 0.2450$
- $\\bar{z} = 0.2450 / 6 \\approx 0.040833$
- $\\sum E = 150 + 240 + 300 + 340 + 370 + 390 = 1{,}790$
- $\\bar{E} = 1{,}790 / 6 \\approx 298.333$
- $\\sum z^2 = 0.010000 + 0.002500 + 0.001109 + 0.000625 + 0.000400 + 0.000279 = 0.014913$
- $\\sum z E = 15.00 + 12.00 + 10.00 + 8.50 + 7.40 + 6.50 = 59.40$

Computing the sample slope:
$$\\text{Numerator} = \\sum z E - \\frac{(\\sum z)(\\sum E)}{N} = 59.40 - \\frac{(0.2450)(1{,}790)}{6} = 59.40 - 73.0917 = -13.6917$$
$$\\text{Denominator} = \\sum z^2 - \\frac{(\\sum z)^2}{N} = 0.014913 - \\frac{(0.2450)^2}{6} = 0.014913 - 0.010004 = 0.004909$$

The regression slope with respect to $z$ is:
$$\\text{Slope} = \\frac{-13.6917}{0.004909} \\approx -2{,}789.10$$

Since the model is $E = a - b z$, the parameter $b$ is:
$$b = -(\\text{Slope}) = \\mathbf{2{,}789.10}$$

Solving for intercept $a$:
$$a = \\bar{E} - (\\text{Slope}) \\bar{z} = 298.333 - (-2{,}789.10 \\times 0.040833) = 298.333 + 113.888 \\approx \\mathbf{412.22}$$

The fitted inverse Engel curve is:
$$E = 412.22 - \\frac{2{,}789.10}{M}$$

### Solution, step 4: Saturation Ceiling and Income Elasticity Dynamics
1. **Theoretical Saturation Ceiling**:
   As household income approaches infinity ($M \\to \\infty$), the term $\\frac{2{,}789.10}{M} \\to 0$.
   The asymptotic upper limit of fresh food expenditure is:
   $$E_{\\max} = a = \\mathbf{\\$412.22} \\text{ per month}$$
   No matter how wealthy a household becomes, physical stomach capacity and food consumption limits ceiling their dairy and meat expenditure at $\\$412.22$.

2. **Income Elasticity Formula for Inverse Model**:
   Differentiating $E = a - b M^{-1}$ with respect to $M$:
   $$\\frac{dE}{dM} = b M^{-2} = \\frac{b}{M^2}$$
   The income elasticity of expenditure is:
   $$\\eta_M = \\frac{dE}{dM} \\times \\frac{M}{E} = \\left( \\frac{b}{M^2} \\right) \\frac{M}{E} = \\frac{b}{M \\times E}$$

3. **Elasticity at $M = 20$**:
   - Fitted expenditure: $E_{20} = 412.22 - \\frac{2{,}789.10}{20} = 412.22 - 139.46 = 272.76$
   - Income elasticity:
     $$\\eta_M(20) = \\frac{2{,}789.10}{20 \\times 272.76} = \\frac{2{,}789.10}{5{,}455.20} \\approx \\mathbf{0.511}$$

4. **Elasticity at $M = 60$**:
   - Fitted expenditure: $E_{60} = 412.22 - \\frac{2{,}789.10}{60} = 412.22 - 46.49 = 365.73$
   - Income elasticity:
     $$\\eta_M(60) = \\frac{2{,}789.10}{60 \\times 365.73} = \\frac{2{,}789.10}{21{,}943.80} \\approx \\mathbf{0.127}$$

**Economic Interpretation**:
For lower-income households ($M = 20$), a $1.0\\%$ increase in income boosts food spending by $0.51\\%$. For affluent households ($M = 60$), the elasticity collapses to $0.13\\%$, demonstrating that demand nears complete biological saturation.
"""

(OUT_DIR / "unit-7.md").write_text(u7_content, encoding="utf-8")
print(f"Unit 7: {prose_count(u7_content)} words")

(OUT_DIR / "unit-8.md").write_text(u8_content, encoding="utf-8")
print(f"Unit 8: {prose_count(u8_content)} words")
