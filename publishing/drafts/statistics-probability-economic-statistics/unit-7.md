# Unit 7: Input-Output Analysis & Social Accounting Systems

## Leontief's Inter-Industry General Equilibrium Model

Modern industrial economies do not operate as isolated silos. The production of an automobile requires steel, glass, rubber, electronics, and design services; the production of steel in turn requires iron ore, coal, electrical power, and heavy transport equipment; and electricity generation consumes coal, natural gas, and turbine machinery. To analyze these dense, circular inter-industry dependencies, the Russian-American economist Wassily Leontief developed **Input-Output Analysis** in the 1930s—a breakthrough for which he was awarded the 1973 Nobel Memorial Prize in Economic Sciences.

Input-Output analysis provides an empirical, matrix-algebraic formulation of general equilibrium theory. It maps the complex webs of transactions connecting all producing sectors, enabling economists to calculate how an exogenous shift in final demand for a single sector (such as an export boom, defense procurement, or green energy subsidy) ripples through the entire industrial fabric.

---

## Mathematical Formulation of the Open Static Leontief Model

Consider an economy partitioned into $n$ mutually exclusive and exhaustive productive industries: $1, 2, \dots, n$.

Let:
- $X_i$ denote the total gross physical or monetary output produced by sector $i$.
- $x_{ij}$ denote the quantity of output produced by sector $i$ that is purchased and consumed as an intermediate input by sector $j$ during the accounting period.
- $F_i$ denote the net final demand for the output of sector $i$ (encompassing household consumption, gross capital formation, government purchases, and net exports).

### 1. The Physical Output Balance Equations
For each producing sector $i$, its total gross output must exactly equal the sum of intermediate sales to all $n$ consuming industries plus sales to final demand:

$$X_i = \sum_{j=1}^{n} x_{ij} + F_i, \quad i = 1, 2, \dots, n$$

In expanded form:
$$\begin{aligned}
X_1 &= x_{11} + x_{12} + \dots + x_{1n} + F_1 \\
X_2 &= x_{21} + x_{22} + \dots + x_{2n} + F_2 \\
&\vdots \\
X_n &= x_{n1} + x_{n2} + \dots + x_{nn} + F_n
\end{aligned}$$

### 2. Leontief Technical Input Coefficients
Leontief introduced the fundamental structural assumption of fixed-coefficient production functions (constant returns to scale and zero input substitution): to produce one unit of gross output in sector $j$, a fixed, constant amount of input from sector $i$ is technically required:

$$a_{ij} = \frac{x_{ij}}{X_j} \implies x_{ij} = a_{ij} X_j$$

where $a_{ij}$ is the **Direct Technical Input Coefficient**. The coefficients are compiled into the $n \times n$ **Technology Matrix ($A$)**:

$$A = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn}
\end{bmatrix}$$

Substituting $x_{ij} = a_{ij} X_j$ into the balance equations:

$$X_i = \sum_{j=1}^{n} a_{ij} X_j + F_i, \quad i = 1, 2, \dots, n$$

In matrix notation:

$$X = A X + F$$

where $X = [X_1, X_2, \dots, X_n]^T$ and $F = [F_1, F_2, \dots, F_n]^T$.

### 3. The Leontief Inverse Matrix
Rearranging the matrix balance equation:

$$X - A X = F \implies (I - A) X = F$$

where $I$ is the $n \times n$ identity matrix. If $(I - A)$ is non-singular, we invert the matrix to solve for the gross output vector required to satisfy any arbitrary final demand vector $F$:

$$X = (I - A)^{-1} F$$

The matrix $L = (I - A)^{-1}$ is the celebrated **Leontief Inverse Matrix** (or Total Requirements Matrix). Each element $l_{ij}$ of $L$ quantifies the total (direct plus indirect) gross output that sector $i$ must generate to satisfy one additional unit of final demand for the output of sector $j$.

Using the Neumann power series expansion for matrix inverses (valid when the spectral radius $\rho(A) < 1$):

$$(I - A)^{-1} = I + A + A^2 + A^3 + \dots$$

- $I$: The direct delivery of one unit of final output.
- $A$: The first-round direct intermediate inputs needed.
- $A^2$: The second-round indirect intermediate inputs needed to produce the first-round inputs.
- $A^k$: The $k$-th round indirect ripple effects propagating across supply chains.

---

## Economic Viability: The Hawkins-Simon Conditions

A purely mathematical matrix inversion does not guarantee that an economic system is physically viable. If an economy's industries consume more steel, coal, and energy to produce a unit of steel than the unit itself provides, the system is parasitic and will collapse.

In 1949, David Hawkins and Herbert A. Simon formulated the necessary and sufficient mathematical conditions for an input-output system to be **Economically Viable**—meaning that for any non-negative, non-zero final demand vector $F \ge 0$, there exists a strictly positive gross output solution vector $X > 0$.

### The Hawkins-Simon Theorem:
An $n \times n$ technology matrix $A$ is economically viable if and only if all leading principal minors of the Leontief matrix $M = (I - A)$ are strictly positive:

1. **First-order minor**:
   $$1 - a_{11} > 0 \implies a_{11} < 1$$
   No industry can consume an entire unit (or more) of its own output merely to produce one unit of that output.
2. **Second-order minor**:
   $$\det \begin{bmatrix} 1 - a_{11} & -a_{12} \\ -a_{21} & 1 - a_{22} \end{bmatrix} = (1 - a_{11})(1 - a_{22}) - a_{12} a_{21} > 0$$
   The circular feedback between sectors 1 and 2 must not consume more than the combined output generated.
3. **General $k$-th order minor**:
   $$\det(M_k) > 0 \quad \text{for all } k = 1, 2, \dots, n$$

If any leading principal minor is zero or negative, the technology requires more aggregate resources than it produces, rendering the economic structure unsustainable.

---

## Inter-Industry Multipliers and Linkages

Input-output matrices provide standard macroeconomic policy multipliers used to quantify supply-chain impacts:

### 1. Output Multipliers
The **Output Multiplier** for sector $j$ measures the total gross output generated across all sectors of the economy per dollar increase in final demand for sector $j$'s output. It is given by the column sum of the Leontief inverse matrix:

$$O_j = \sum_{i=1}^{n} l_{ij}$$

Sectors with high output multipliers (e.g., manufacturing, construction) trigger large spillover effects across supplier networks.

### 2. Backward and Forward Linkages (Rasmussen Indices)
Pioneered by P. Nørregaard Rasmussen (1956) and Albert Hirschman (1958), linkage indices identify key strategic sectors:
- **Backward Linkage ($U_j$)**: Measures the extent to which industry $j$ stimulates upstream suppliers by purchasing intermediate inputs:
  $$U_j = \frac{\frac{1}{n} \sum_{i=1}^{n} l_{ij}}{\frac{1}{n^2} \sum_{i=1}^{n} \sum_{j=1}^{n} l_{ij}} = \frac{n \sum_{i=1}^{n} l_{ij}}{\sum_{i=1}^{n} \sum_{j=1}^{n} l_{ij}}$$
  If $U_j > 1$, sector $j$ exerts an above-average upstream pull on the economy.
- **Forward Linkage ($U_i$)**: Measures the extent to which industry $i$'s output is consumed as an intermediate input by downstream purchasing industries:
  $$U_i = \frac{n \sum_{j=1}^{n} l_{ij}}{\sum_{i=1}^{n} \sum_{j=1}^{n} l_{ij}}$$
  If $U_i > 1$, sector $i$ provides an above-average supply base for downstream industrial growth.

---

## Social Accounting Matrix (SAM) Architecture

A **Social Accounting Matrix (SAM)** expands Leontief's inter-industry input-output table into a comprehensive, square, double-entry macroeconomic framework encompassing all socioeconomic transactions within an economy.

In a SAM:
- Every row records economic **receipts (inflows / revenues)** of an account.
- Every column records economic **outlays (outflows / expenditures)** of an account.
- **Fundamental Accounting Identity**: For every account $k$, total receipts must strictly equal total outlays:
  $$\text{Row Total}_k \equiv \text{Column Total}_k$$

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


---

## Advanced Input-Output Systems: The Price Dual and Closed Models

While the primal Leontief model solves for gross physical output given final demand, input-output theory possesses a mathematically symmetrical **Price Dual Model** governing how input costs, wages, and profit markups determine industry product prices.

### 1. The Price Dual Leontief Model
Let $p = [p_1, p_2, \dots, p_n]^T$ represent the vector of unit prices charged by the $n$ producing industries.
For each sector $j$, its unit price must cover the cost of intermediate inputs purchased from all sectors plus primary value-added costs per unit of gross output (labor wages, depreciation, indirect taxes, and normal profits):

$$p_j = \sum_{i=1}^{n} p_i a_{ij} + v_j, \quad j = 1, 2, \dots, n$$

where $v_j = V_j / X_j$ is the **Value-Added Coefficient** of sector $j$.
In matrix notation:

$$p = A^T p + v$$

where $A^T$ is the transpose of the technology matrix $A$, and $v = [v_1, v_2, \dots, v_n]^T$.
Rearranging:

$$(I - A^T) p = v \implies p = (I - A^T)^{-1} v = \left[ (I - A)^{-1} \right]^T v$$

The price dual shows that each industry's equilibrium price is a linear combination of primary value-added inputs across all upstream sectors, weighted by the transposed Leontief inverse.

#### Practical Policy Application: Cost-Push Inflation Modeling:
The price dual is the standard tool used by ministries of finance and central banks to trace the economy-wide transmission of cost shocks. If a carbon tax is levied on the energy sector ($v_{\text{energy}}$ increases by $\Delta v_1$), the price vector response is:
$$\Delta p = (I - A^T)^{-1} \Delta v$$
The model calculates the exact cascading inflationary impact on steel, manufacturing, freight logistics, and consumer retail prices.

### 2. The Closed Leontief Model and Induced Multipliers
In the open static Leontief model, final demand $F$ is treated as strictly exogenous. However, in reality, household consumption is endogenously driven by the labor income earned in production: expanding industrial output creates jobs, paying wages to workers who subsequently spend their earnings on consumer goods.

The **Closed Leontief Model** endogenizes households by treating them as the $(n+1)$-th industry:
- **Household Row (Inputs to Production)**: Sector $n+1$ provides labor services; row coefficients represent labor input per unit output: $a_{n+1, j} = L_j / X_j$.
- **Household Column (Consumption Demand)**: Column coefficients represent household consumption shares per dollar of labor income: $a_{i, n+1} = C_i / E_{\text{total}}$.

The augmented $(n+1) \times (n+1)$ coefficient matrix $\tilde{A}$ is:
$$\tilde{A} = \begin{bmatrix} A & c \\ l^T & 0 \end{bmatrix}$$

Inverting $(I - \tilde{A})$ yields the **Type II (Induced) Multipliers**:

$$\text{Type II Multiplier} = \text{Direct Impact} + \text{Indirect Supply-Chain Impact} + \text{Induced Household Spending Impact}$$

Type II multipliers are systematically larger than Type I (direct + indirect) multipliers, capturing the full Keynesian circular flow of income and expenditure.


---

## Environmentally Extended Input-Output (EEIO) Analysis

In environmental economics and climate policy, **Environmentally Extended Input-Output (EEIO) Analysis** integrates macroeconomic input-output tables with physical environmental satellite accounts. This allows researchers to trace greenhouse gas emissions, water withdrawals, and energy footprints through inter-industry supply chains from primary extraction to final retail consumption.

### 1. Mathematical Formulation of the EEIO Model
Let $e = [e_1, e_2, \dots, e_n]^T$ denote the vector of **Direct Environmental Intensity Coefficients**, where $e_j$ represents direct physical emissions (e.g., metric tons of $\text{CO}_2$ equivalent) released per unit of gross monetary output in sector $j$:

$$e_j = \frac{E_j}{X_j}$$

where $E_j$ is the total physical emissions generated directly by industry $j$.

In the Leontief system, gross output is determined by final demand: $X = (I - A)^{-1} F$.
The total physical emissions $T_E$ generated across the entire economy to satisfy final demand vector $F$ is:

$$T_E = e^T X = e^T (I - A)^{-1} F$$

Defining the **Embodied Emissions Multiplier Vector** as:

$$\epsilon^T = e^T (I - A)^{-1}$$

Each element $\epsilon_j$ represents the total direct plus upstream indirect greenhouse gas emissions generated across all supplier industries per dollar of final demand for the output of sector $j$.

### 2. Production-Based vs Consumption-Based Accounting
The EEIO framework provides the mathematical foundation for distinguishing between:
- **Production-Based Emissions (Territorial Emissions)**:
  Emissions physically released within domestic sovereign boundaries:
  $$\text{Emissions}_{\text{prod}} = \sum_{j=1}^{n} E_j = e^T X$$
- **Consumption-Based Emissions (Carbon Footprint)**:
  Emissions embodied in the final goods and services consumed by domestic residents, regardless of where in the world the physical emissions occurred:
  $$\text{Emissions}_{\text{cons}} = e^T (I - A)^{-1} F_{\text{domestic}} + \epsilon_{\text{imported}}^T M_{\text{final}}$$

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
- $B$ is the $n \times n$ **Capital Coefficients Matrix**, where $b_{ij}$ denotes the quantity of capital good $i$ required per unit expansion in the productive capacity of sector $j$:
  $$b_{ij} = \frac{K_{ij}}{\Delta X_j}$$

Rearranging into a matrix difference equation:

$$(I - A + B) X_t - B X_{t+1} = C_t$$

Solving this system of second-order matrix difference equations reveals the economy's optimal multi-sector investment trajectory and validates the **Turnpike Theorems** of dynamic general equilibrium: to achieve maximum long-run growth, the economy must converge to a balanced expansion path determined by the dominant eigenvalue of the capital-technology system.


---

## Structural Decomposition Analysis (SDA) in Input-Output Systems

To understand the fundamental driving forces behind historical changes in macroeconomic output, employment, carbon emissions, or water use over decades, economists deploy **Structural Decomposition Analysis (SDA)**.
In an input-output framework, total gross output in year $t$ is:

$$X_t = L_t F_t = (I - A_t)^{-1} F_t$$

Over an elapsed interval from base year $0$ to target year $t$, the total observed change in output is $\Delta X = X_t - X_0$.

### Polar Structural Decomposition
Because both the technology matrix ($A$) and final demand ($F$) change simultaneously, the total differential decomposes into:

$$\Delta X = X_t - X_0 = L_t F_t - L_0 F_0$$

Adding and subtracting the cross-product terms $L_t F_0$ or $L_0 F_t$ yields two alternative "polar" decompositions:

1. **First Polar Decomposition**:
   $$\Delta X = (\Delta L) F_0 + L_t (\Delta F)$$
2. **Second Polar Decomposition**:
   $$\Delta X = (\Delta L) F_t + L_0 (\Delta F)$$

To eliminate arbitrary path dependence, economists take the unweighted arithmetic mean of both polar formulations:

$$\Delta X = \frac{1}{2} (\Delta L) (F_0 + F_t) + \frac{1}{2} (L_0 + L_t) (\Delta F)$$

where:
- $\frac{1}{2} (\Delta L) (F_0 + F_t)$ is the **Technological Change Effect**: Output expansion driven by structural shifts in inter-industry input efficiency, supply-chain restructuring, and material substitution.
- $\frac{1}{2} (L_0 + L_t) (\Delta F)$ is the **Final Demand Effect**: Output expansion driven by changes in consumer tastes, government investment programs, and export demand.

### Further Decomposition of the Final Demand Effect:
The final demand shift $\Delta F$ can be further partitioned into:
- **Level Effect**: Growth in the aggregate volume of final demand (holding product composition constant).
- **Structure (Mix) Effect**: Reallocation of final consumption shares across sectors (e.g., shifts from fossil fuels to renewable energy).

Applied to national carbon inventories, Structural Decomposition Analysis allows policymakers to quantify whether rising emissions are driven by aggregate GDP expansion, consumer preference shifts, or changing industrial supply-chain carbon intensities.


---

## Multi-Regional Input-Output (MRIO) Modeling and Global Value Chains

In the era of economic globalization, international trade no longer consists primarily of completed finished goods traded between two nations. Modern manufacturing is characterized by **Global Value Chains (GVCs)**: raw mineral ores extracted in Australia are shipped to China for refining, manufactured into electronic components in Taiwan, assembled into consumer smartphones in Vietnam, and marketed by retail corporations in the United States and Europe.

To analyze international trade and carbon emissions without distortion, national statistical organizations compile **Multi-Regional Input-Output (MRIO)** tables (such as the OECD Inter-Country Input-Output ICIO database and the World Input-Output Database WIOD).

### 1. Mathematical Architecture of the MRIO Model
Consider a world economy comprising $M$ sovereign nations ($r, s = 1, \dots, M$), where each nation has $n$ industrial sectors.
The global MRIO system is formulated as:

$$\begin{bmatrix}
X^1 \\ X^2 \\ \vdots \\ X^M
\end{bmatrix} = \begin{bmatrix}
A^{11} & A^{12} & \dots & A^{1M} \\
A^{21} & A^{22} & \dots & A^{2M} \\
\vdots & \vdots & \ddots & \vdots \\
A^{M1} & A^{M2} & \dots & A^{MM}
\end{bmatrix} \begin{bmatrix}
X^1 \\ X^2 \\ \vdots \\ X^M
\end{bmatrix} + \begin{bmatrix}
\sum_{s} F^{1s} \\ \sum_{s} F^{2s} \\ \vdots \\ \sum_{s} F^{Ms}
\end{bmatrix}$$

where:
- $X^r$ is the $n \times 1$ gross output vector of country $r$.
- $A^{rr}$ is the domestic technology matrix of country $r$.
- $A^{rs}$ is the inter-country trade intermediate coefficient matrix: each element $a_{ij}^{rs} = x_{ij}^{rs} / X_j^s$ denotes the intermediate inputs exported from industry $i$ in country $r$ consumed by industry $j$ in country $s$.
- $F^{rs}$ is the final demand vector of goods produced in country $r$ and consumed in country $s$.

Defining the global technology matrix as $\mathbb{A}$ and global output as $\mathbb{X}$:

$$\mathbb{X} = (\mathbb{I} - \mathbb{A})^{-1} \mathbb{F}$$

### 2. Trade in Value Added (TiVA) and Gross Export Decomposition
Pioneered by Robert Koopman, Zhi Wang, and Shang-Jin Wei (2014), the **KWW Gross Export Decomposition** breaks a nation's gross bilateral exports ($E^{rs}$) into distinct value-added components:

1. **Domestic Value Added ($DVA$) Absorbed Abroad**: The true net income generated by domestic workers and capital embodied in exports that is ultimately consumed by foreign residents.
2. **Domestic Value Added Returning Home**: Domestic inputs exported abroad for intermediate processing that are subsequently re-imported as finished goods.
3. **Foreign Value Added ($FVA$)**: The value of imported foreign intermediate components incorporated into domestic exports.
4. **Pure Double-Counting**: Goods and intermediate parts that cross international borders multiple times before final assembly.

In electronics and automobile manufacturing, Foreign Value Added often accounts for 40% to 60% of gross export value, confirming that gross customs trade statistics severely distort actual economic contributions and bilateral trade balances.


---

## Sectoral Prioritization: The Hypothetical Extraction Method (HEM)

In national industrial strategy and regional development planning, economic planners seek to identify "key sectors" whose disruption or expansion would exert the greatest systemic impact on national output. While simple output multipliers (column sums of $(I-A)^{-1}$) provide a basic ranking, they do not account for the absolute scale of the industry within the economy.
To provide a rigorous systemic assessment, input-output economists employ the **Hypothetical Extraction Method (HEM)**.

### Mathematical Formulation
The Hypothetical Extraction Method simulates the complete hypothetical removal of sector $k$ from the economic matrix, evaluating how total national production would contract in its absence.

Partition the $n$-sector technology matrix $A$ into sector $k$ and all other remaining sectors (denoted $-k$):

$$A = \begin{bmatrix}
a_{kk} & A_{k, -k} \\
A_{-k, k} & A_{-k, -k}
\end{bmatrix}$$

1. **Extraction of Backward Linkages (Hypothetical Supplier Shutdown)**:
   Suppose sector $k$ stops purchasing intermediate inputs from the rest of the economy ($A_{-k, k} = 0$). The extracted technology matrix is:
   $$\bar{A}_{(k)}^{\text{back}} = \begin{bmatrix}
   a_{kk} & A_{k, -k} \\
   0 & A_{-k, -k}
   \end{bmatrix}$$
   The resulting hypothetical output vector is:
   $$\bar{X}_{(k)}^{\text{back}} = (I - \bar{A}_{(k)}^{\text{back}})^{-1} F$$
   The aggregate output loss caused by severing sector $k$'s upstream purchases is:
   $$\Delta X_{\text{back}} = \sum_{i=1}^{n} X_i - \sum_{i=1}^{n} \bar{X}_{i, (k)}^{\text{back}}$$

2. **Complete Hypothetical Extraction**:
   Extracting both upstream purchases and downstream sales of sector $k$ sets $A_{k, -k} = 0$, $A_{-k, k} = 0$, and $F_k = 0$.
   The percentage loss in total national output measures the total systemic integration index of sector $k$:
   $$\text{Total Extraction Impact } \% = \frac{\sum X_i - \sum \bar{X}_{i, (k)}}{\sum X_i} \times 100\%$$

The Hypothetical Extraction Method identifies true structural bottlenecks: sectors whose failure triggers catastrophic cascading shutdowns across the entire national economy.

---

## Supply-Driven Input-Output Modeling: The Ghosh Model

While Leontief's classical model is **Demand-Driven** (allocating output from inputs based on fixed technical coefficients $a_{ij} = x_{ij} / X_j$), A. Ghosh (1958) formulated a mathematically dual **Supply-Driven Input-Output Model**.

In the Ghosh framework:
- Output allocations are assumed to depend on fixed **Allocation Coefficients** (output shares):
  $$b_{ij} = \frac{x_{ij}}{X_i}$$
  where $b_{ij}$ represents the fraction of sector $i$'s gross output that is allocated to sector $j$ as an intermediate input.
- Compiling the $n \times n$ **Allocation Matrix $B$**:
  $$B = \begin{bmatrix}
  b_{11} & b_{12} & \dots & b_{1n} \\
  b_{21} & b_{22} & \dots & b_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  b_{n1} & b_{n2} & \dots & b_{nn}
  \end{bmatrix}$$

The horizontal row balance equation across sectors is:
$$X_j = \sum_{i=1}^{n} b_{ij} X_i + V_j$$
In matrix notation:
$$X^T = X^T B + V^T \implies X^T (I - B) = V^T$$
where $V$ is the vector of primary value-added inputs (labor, capital, imports).

Inverting $(I - B)$ yields the **Ghosh Inverse Matrix**:

$$X^T = V^T (I - B)^{-1} = V^T G$$

The Ghosh model traces how an exogenous disruption or expansion in primary factor availability (such as a nationwide labor strike, an international petroleum embargo, or an agricultural drought) transmits forward through the supply chain, altering output levels across downstream industries.


---

## Waste Input-Output (WIO) Modeling and the Circular Economy

In contemporary industrial ecology and environmental planning, the linear economic model of "take, make, dispose" is being replaced by the **Circular Economy**. To model the physical transformation of manufactured goods into post-consumer scrap, recycling, and secondary raw materials, Shinichiro Nakamura and Yasushi Kondo (2002) developed the **Waste Input-Output (WIO) Model**.

### Mathematical Architecture of the WIO System
The WIO table expands Leontief's economic matrix by appending physical waste treatment and recycling sectors:

$$\begin{bmatrix}
X_I \\ X_W
\end{bmatrix} = \begin{bmatrix}
A_{I, I} & A_{I, W} \\
W_{W, I} & W_{W, W}
\end{bmatrix} \begin{bmatrix}
X_I \\ X_W
\end{bmatrix} + \begin{bmatrix}
F_I \\ W_F
\end{bmatrix}$$

where:
- $X_I$ is the monetary output vector of standard industrial producing sectors ($n \times 1$).
- $X_W$ is the physical output vector of waste management and recycling treatment facilities (e.g., metric tons of incinerated, shredded, or recycled plastics, metals, paper).
- $A_{I, I}$ is the conventional inter-industry technical coefficient matrix.
- $A_{I, W}$ represents the purchases of industrial goods and energy required by waste treatment plants per unit of waste processed.
- $W_{W, I}$ is the **Waste Generation Matrix**: each element $w_{kj}$ represents the physical mass of waste type $k$ generated per unit of gross industrial output in sector $j$.
- $W_F$ is the physical vector of municipal solid waste discarded directly by final household consumers.

Inverting the augmented block matrix enables environmental planners to calculate how changes in recycling mandates, consumer packaging taxes, or landfill disposal bans affect total industrial output, energy consumption, and circular resource recovery across national supply chains.


---

## Updating Input-Output Matrices: The RAS Biproportional Method

Because comprehensive national input-output tables require extensive nationwide enterprise censuses, national statistical bureaus typically compile full benchmark tables only once every five or ten years. In the intervening years, macroeconomic planners possess updated aggregate sectoral gross outputs ($X_i$), total intermediate deliveries ($u_i = \sum_{j} x_{ij}$), and total intermediate purchases ($v_j = \sum_{i} x_{ij}$), but lack the detailed interior cell transactions $x_{ij}$.

To update an existing baseline technology matrix $A^0$ to a target year without conducting a full census, mathematical statisticians employ the **RAS Biproportional Adjustment Method** (Richard Stone, 1961).

### 1. The Biproportional Model Formulation
The RAS algorithm assumes that changes in technical coefficients over time reflect two distinct, independent economic forces:
1. **The Substitution Effect ($r_i$)**: A row multiplier reflecting secular substitution across all consuming industries toward or away from input $i$ (e.g., universal substitution of digital telecommunications for paper, or plastics for steel).
2. **The Fabrication Effect ($s_j$)**: A column multiplier reflecting technological changes in the fabrication depth or degree of processing in industry $j$ (e.g., automation reducing total intermediate materials relative to gross output).

The updated technical coefficient matrix $A^1$ is formulated as the biproportional product:

$$A^1 = \hat{r} A^0 \hat{s}$$

where $\hat{r} = \text{diag}(r_1, r_2, \dots, r_n)$ is a diagonal matrix of row scaling factors, and $\hat{s} = \text{diag}(s_1, s_2, \dots, s_n)$ is a diagonal matrix of column scaling factors.

In element-wise terms:
$$a_{ij}^1 = r_i a_{ij}^0 s_j$$

### 2. The Iterative Balancing Algorithm
The vectors $r$ and $s$ are determined iteratively to satisfy two simultaneous marginal constraints:
- **Row Sum Constraint**: $\sum_{j=1}^{n} a_{ij}^1 X_j^1 = u_i^1$ (Total intermediate deliveries match observed target rows).
- **Column Sum Constraint**: $\sum_{i=1}^{n} a_{ij}^1 X_j^1 = v_j^1$ (Total intermediate purchases match observed target columns).

The algorithm alternates between:
- Step 1: Scaling rows to match intermediate deliveries $u^1$.
- Step 2: Scaling columns of the resulting matrix to match intermediate purchases $v^1$.

Michael Bacharach (1970) proved that if the baseline matrix $A^0$ is non-negative and connected, the iterative RAS algorithm converges uniquely to the global minimum of the Kullback-Leibler information divergence:
$$\min \sum_{i=1}^{n} \sum_{j=1}^{n} x_{ij}^1 \ln\left( \frac{x_{ij}^1}{x_{ij}^0} \right)$$
The updated matrix preserves all structural zero entries, guarantees strictly non-negative technical coefficients, and satisfies all macro-accounting identities.

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
4. Suppose national economic planning targets an increase in final demand to $F^* = [160, \; 220]^T$ over the next three years. Calculate the new gross output levels required from Agriculture and Manufacturing to fulfill this plan.

### Solution, step 1: Computation of Technology Matrix $A$
The technical coefficient formula is $a_{ij} = x_{ij} / X_j$:
- For Sector 1 (Agriculture, $X_1 = 200$):
  $$a_{11} = \frac{x_{11}}{X_1} = \frac{30}{200} = 0.15$$
  $$a_{21} = \frac{x_{21}}{X_1} = \frac{40}{200} = 0.20$$
- For Sector 2 (Manufacturing, $X_2 = 200$):
  $$a_{12} = \frac{x_{12}}{X_2} = \frac{60}{200} = 0.30$$
  $$a_{22} = \frac{x_{22}}{X_2} = \frac{20}{200} = 0.10$$

The Technology Matrix $A$ is:
$$A = \begin{bmatrix} 0.15 & 0.30 \\ 0.20 & 0.10 \end{bmatrix}$$

### Solution, step 2: Hawkins-Simon Viability Verification
We construct the Leontief matrix $M = (I - A)$:
$$I - A = \begin{bmatrix} 1 - 0.15 & -0.30 \\ -0.20 & 1 - 0.10 \end{bmatrix} = \begin{bmatrix} 0.85 & -0.30 \\ -0.20 & 0.90 \end{bmatrix}$$

We evaluate the Hawkins-Simon conditions:
1. **First-order leading principal minor**:
   $$M_1 = 1 - a_{11} = 0.85 > 0 \quad \text{(Satisfied)}$$
2. **Second-order leading principal minor (Determinant of $I - A$)**:
   $$\det(I - A) = (0.85)(0.90) - (-0.30)(-0.20) = 0.7650 - 0.0600 = 0.7050 > 0 \quad \text{(Satisfied)}$$

Both principal minors are strictly positive ($\det(I-A) = 0.7050 > 0$). Therefore, the Hawkins-Simon conditions are fully satisfied, proving that this two-sector economy is economically viable and capable of sustaining positive net final demand.

### Solution, step 3: Computation of the Leontief Inverse Matrix $(I - A)^{-1}$
For a $2 \times 2$ matrix $M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the inverse is:
$$M^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

Applying this to $I - A$:
$$(I - A)^{-1} = \frac{1}{0.7050} \begin{bmatrix} 0.90 & 0.30 \\ 0.20 & 0.85 \end{bmatrix}$$

Evaluating each entry:
- $l_{11} = \frac{0.90}{0.7050} = \frac{90}{70.5} = \frac{6}{4.7} \approx 1.2766$
- $l_{12} = \frac{0.30}{0.7050} = \frac{30}{70.5} = \frac{2}{4.7} \approx 0.4255$
- $l_{21} = \frac{0.20}{0.7050} = \frac{20}{70.5} = \frac{4}{14.1} \approx 0.2837$
- $l_{22} = \frac{0.85}{0.7050} = \frac{85}{70.5} = \frac{17}{14.1} \approx 1.2057$

The Leontief Inverse Matrix is:
$$(I - A)^{-1} = \begin{bmatrix} 1.2766 & 0.4255 \\ 0.2837 & 1.2057 \end{bmatrix}$$

### Solution, step 4: Gross Output Projections for New Final Demand
The target final demand vector is:
$$F^* = \begin{bmatrix} 160 \\ 220 \end{bmatrix}$$

Using the Leontief inverse:
$$X^* = (I - A)^{-1} F^* = \begin{bmatrix} 1.2766 & 0.4255 \\ 0.2837 & 1.2057 \end{bmatrix} \begin{bmatrix} 160 \\ 220 \end{bmatrix}$$

Carrying out the matrix multiplication:
- **Required Agricultural Gross Output ($X_1^*$)**:
  $$X_1^* = (1.2766 \times 160) + (0.4255 \times 220) = 204.256 + 93.610 = \mathbf{297.87} \text{ million}$$
- **Required Manufacturing Gross Output ($X_2^*$)**:
  $$X_2^* = (0.2837 \times 160) + (1.2057 \times 220) = 45.392 + 265.254 = \mathbf{310.65} \text{ million}$$

To fulfill the expansion in final demand, agricultural production must expand by $48.9\%$ (from $\$200\text{M}$ to $\$297.87\text{M}$), and manufacturing production must expand by $55.3\%$ (from $\$200\text{M}$ to $\$310.65\text{M}$).

---

### Question 2: Employment Multipliers and Value-Added Decomposition
A tripartite regional development agency models three key sectors: **Energy ($1$)**, **Heavy Industry ($2$)**, and **Services ($3$)**.
The Leontief Inverse Matrix $(I - A)^{-1}$ is established as:

$$(I - A)^{-1} = \begin{bmatrix}
1.30 & 0.25 & 0.15 \\
0.40 & 1.45 & 0.20 \\
0.30 & 0.35 & 1.25
\end{bmatrix}$$

The direct labor employment requirements per million dollars of gross output (labor coefficients $l_i$) are:
- Energy ($1$): $l_1 = 4.0$ workers per $\$1\text{M}$ output (highly capital intensive)
- Heavy Industry ($2$): $l_2 = 12.0$ workers per $\$1\text{M}$ output
- Services ($3$): $l_3 = 25.0$ workers per $\$1\text{M}$ output (labor intensive)

1. Calculate the **Output Multiplier** for each of the three sectors and identify which sector generates the greatest total economic output expansion per unit of final demand.
2. Formulate the total direct and indirect labor coefficient vector $e = l^T (I - A)^{-1}$ and compute the **Employment Multipliers** ($e_j$) for all three sectors.
3. Suppose the regional government has a $\$50\text{M}$ infrastructure stimulus budget. Compare the total employment generated by allocating the entire $\$50\text{M}$ to Heavy Industry versus allocating it to Services.

### Solution, step 1: Computation of Output Multipliers
The output multiplier $O_j$ is the sum of column $j$ of $(I - A)^{-1}$:
- **Energy ($j=1$)**:
  $$O_1 = \sum_{i=1}^{3} l_{i1} = 1.30 + 0.40 + 0.30 = \mathbf{2.00}$$
  Every $\$1.00$ increase in final demand for energy generates $\$2.00$ in total gross output across the economy.
- **Heavy Industry ($j=2$)**:
  $$O_2 = \sum_{i=1}^{3} l_{i2} = 0.25 + 1.45 + 0.35 = \mathbf{2.05}$$
  Every $\$1.00$ increase in heavy industry demand generates $\$2.05$ in total output.
- **Services ($j=3$)**:
  $$O_3 = \sum_{i=1}^{3} l_{i3} = 0.15 + 0.20 + 1.25 = \mathbf{1.60}$$
  Every $\$1.00$ increase in services demand generates $\$1.60$ in total output.

**Assessment**: Heavy Industry exhibits the highest output multiplier ($O_2 = 2.05$), owing to its extensive backward supply linkages with raw materials, energy, and subcontracted business services.

### Solution, step 2: Total Employment Multipliers
The vector of total direct plus indirect labor requirements per unit of final demand is:
$$e = l^T (I - A)^{-1} = [l_1, l_2, l_3] \begin{bmatrix}
l_{11} & l_{12} & l_{13} \\
l_{21} & l_{22} & l_{23} \\
l_{31} & l_{32} & l_{33}
\end{bmatrix}$$

With $l = [4.0, \; 12.0, \; 25.0]$:
1. **Employment Multiplier for Energy ($e_1$)**:
   $$e_1 = (4.0 \times 1.30) + (12.0 \times 0.40) + (25.0 \times 0.30) = 5.20 + 4.80 + 7.50 = \mathbf{17.50} \text{ jobs per \$1M}$$
   *(Note: While energy directly employs only 4 workers per $\$1\text{M}$, its supply chain demand creates another 13.5 indirect jobs in manufacturing and services).*
2. **Employment Multiplier for Heavy Industry ($e_2$)**:
   $$e_2 = (4.0 \times 0.25) + (12.0 \times 1.45) + (25.0 \times 0.35) = 1.00 + 17.40 + 8.75 = \mathbf{27.15} \text{ jobs per \$1M}$$
3. **Employment Multiplier for Services ($e_3$)**:
   $$e_3 = (4.0 \times 0.15) + (12.0 \times 0.20) + (25.0 \times 1.25) = 0.60 + 2.40 + 31.25 = \mathbf{34.25} \text{ jobs per \$1M}$$

### Solution, step 3: Evaluation of the $\$50\text{M}$ Stimulus Allocation
We multiply the total employment multipliers by the $\$50\text{M}$ shock:
- **Heavy Industry Stimulus**:
  $$\text{Total Jobs Created} = 50 \times 27.15 = \mathbf{1{,}357.5} \text{ jobs}$$
- **Services Stimulus**:
  $$\text{Total Jobs Created} = 50 \times 34.25 = \mathbf{1{,}712.5} \text{ jobs}$$

**Policy Trade-off**:
Allocating the $\$50\text{M}$ to Services creates **$355$ more jobs** ($+26.1\%$) than Heavy Industry, because Services is inherently labor intensive. However, Heavy Industry stimulates a broader industrial base ($O_2 = 2.05$ vs $1.60$). Policymakers pursuing maximum immediate job creation should prioritize Services, whereas those seeking industrial capital deepening and supply-chain resilience should favor Heavy Industry.

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
$$\text{Total Receipts (Row } k \text{ Total)} \equiv \text{Total Outlays (Column } k \text{ Total)}$$

No leakages or unrecorded injections are permitted; all revenues received must be completely accounted for in expenditures or savings.

### Solution, step 2: Solving for Missing Variables $X$ and $Y$
1. **Analyze Account 4 (Institutions $H$)**:
   The column total of Institutions is given as $410$:
   $$\text{Outlays of } H = X + 20 + Y = 410 \implies X + Y = 390$$

2. **Analyze Account 5 (Rest of the World $W$)**:
   The column total of $W$ is given as $120$:
   $$\text{Row Total of } W = \text{Column Total of } W = 120$$
   From Row 5:
   $$\text{Row Total of } W = 0 + 30 + 0 + Y + 0 = 30 + Y$$
   Setting Row Total equal to Column Total:
   $$30 + Y = 120 \implies Y = 120 - 30 = \mathbf{90} \text{ billion}$$

3. **Solve for $X$**:
   Since $X + Y = 390$:
   $$X = 390 - 90 = \mathbf{300} \text{ billion}$$

4. **Verify Account 2 (Commodities $C$)**:
   - Row Total of $C$:
     $$\text{Row Total} = 120 + 0 + 0 + X + 60 = 120 + 300 + 60 = \mathbf{480} \text{ billion}$$
   - Column Total of $C$:
     $$\text{Col Total} = 450 + 0 + 0 + 0 + 30 = \mathbf{480} \text{ billion}$$
   Row Total ($480$) matches Column Total ($480$) perfectly!

### Solution, step 3: GDP Verification from the Balanced SAM
1. **Value-Added Approach**:
   Factor payments generated by domestic Activities (Account $A$ payments to Account $F$):
   $$\text{GDP} = \text{Payments to Factors} = \mathbf{380} \text{ billion}$$
   Alternatively, Gross Output of Activities is $500$, and intermediate input purchases from Commodities are $120$:
   $$\text{GDP} = \text{Gross Output} - \text{Intermediate Consumption} = 500 - 120 = \mathbf{380} \text{ billion}$$

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
   $$\text{GDP} = C + (X - M) = 300 + 80 = \mathbf{380} \text{ billion}$$

Both perspectives confirm $\text{GDP} = \mathbf{380}$ billion, verifying structural consistency.
