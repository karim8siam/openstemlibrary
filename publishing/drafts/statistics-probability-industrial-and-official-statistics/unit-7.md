# Unit 7: National Statistical Systems, SNA Framework & Macroeconomic Output Measurement

## 7.1 Architecture, Governance, and Ethics of Official Statistics

Official statistics constitute the quantitative infrastructure of modern democratic governance, economic policymaking, and international commerce. Unlike commercial market research or academic sample surveys, official statistics are produced by state institutions to serve as a public good. They guide central bank interest rate decisions, national budgetary resource allocations, social safety net targeting, legislative redistricting, and international treaty compliance.

### The United Nations Fundamental Principles of Official Statistics
In 1994, the United Nations Statistical Commission codified the ten **Fundamental Principles of Official Statistics** (formally endorsed by the UN General Assembly in Resolution 68/261):
1. **Relevance, Impartiality, and Equal Access**: Official statistics must represent practical utility for all citizens, released on an impartial basis by official agencies to honor every citizen’s right to public information.
2. **Professional Standards and Ethics**: Data collection, processing, storage, and presentation methods must adhere strictly to transparent scientific principles and professional ethics.
3. **Accountability and Transparency**: Agencies must document data sources, sampling methods, and statistical algorithms to allow public and peer verification.
4. **Prevention of Misuse**: Statistical authorities are entitled to comment on erroneous interpretation and misuse of statistical outputs.
5. **Sources of Official Statistics**: Data may be drawn from all types of sources—statistical surveys, population censuses, and administrative government records—chosen based on quality, timeliness, and cost-efficiency.
6. **Strict Confidentiality**: Individual respondent records—whether concerning natural persons, households, or commercial corporations—must remain strictly confidential and utilized exclusively for statistical purposes.
7. **Legislation**: The governance, mandates, independence, and operational authority of the statistical system must be enshrined in statutory national law.
8. **National Coordination**: A central authority must coordinate statistical activities across disparate government ministries to ensure uniform classifications, eliminate duplicate collections, and guarantee system coherence.
9. **Use of International Standards**: National classifications and methodologies must conform to international standards (e.g., SNA, ISIC, CPC, ILO standards) to achieve cross-national comparability.
10. **International Cooperation**: Bilateral and multilateral sharing of knowledge and best practices enhances the capability of statistical systems worldwide.

### Institutional Structures: Centralized Versus Decentralized Systems
National Statistical Systems (NSS) generally adopt one of two organizational architectures:
- **Centralized Architecture**: A single primary National Statistical Office (NSO)—such as the Bangladesh Bureau of Statistics (BBS), Statistics Canada, or the Australian Bureau of Statistics (ABS)—is statutorily entrusted with designing, collecting, processing, and publishing the vast majority of official macroeconomic, social, agricultural, and demographic statistics. Centralization ensures high methodological consistency, economies of scale, and seamless coordination.
- **Decentralized Architecture**: Statistical responsibilities are distributed among multiple specialized federal agencies coordinated by a central statistical policy office (such as in the United States, where the Bureau of Labor Statistics monitors employment and inflation, the Bureau of Economic Analysis estimates GDP, the Census Bureau collects demographic data, and the National Center for Health Statistics monitors public health).

The operational life-cycle of official statistical data collection is governed by the **Generic Statistical Business Process Model (GSBPM)**, an internationally standardized framework comprising eight phases: Specify Needs, Design, Build, Collect, Process, Analyze, Disseminate, and Evaluate.

## 7.2 The System of National Accounts (SNA 2008) Framework

The **System of National Accounts (SNA)** is the internationally agreed standard set of recommendations on how to compile measures of macroeconomic activity. Formulated jointly by the United Nations, International Monetary Fund, World Bank, OECD, and European Commission, the current standard (SNA 2008) provides an exhaustive, mathematically coherent accounting matrix tracing every monetary transaction, transfer, asset transformation, and financial flow in the economy.

### 1. Conceptual Boundaries and Residence
- **Economic Territory**: The geographic area administered by a national government within which persons, goods, and capital circulate freely, including territorial enclaves abroad (embassies, consulates, scientific bases).
- **Residence Principle**: An institutional unit is classified as a resident unit of an economic territory when it possesses a center of predominant economic interest in that territory (engaging in economic transactions from a physical location for one year or longer). Nationality and citizenship are legally irrelevant: a foreign-owned multinational manufacturing plant operating on domestic soil is a resident domestic enterprise.

### 2. Institutional Sectors
The domestic economy is partitioned into five mutually exclusive institutional sectors:
1. **Non-Financial Corporations (S.11)**: Commercial enterprises producing goods and non-financial services for market sale at economically significant prices.
2. **Financial Corporations (S.12)**: Commercial banks, central banks, insurance companies, pension funds, and investment trusts providing financial intermediation, asset management, and risk pooling.
3. **General Government (S.13)**: Central, regional, and local government ministries providing non-market collective services (national defense, public education, healthcare, infrastructure administration) funded via compulsory taxation.
4. **Households (S.14)**: Natural persons consuming goods and services, supplying labor factor inputs, and operating unincorporated small-scale household enterprises (proprietorships).
5. **Non-Profit Institutions Serving Households (NPISH, S.15)**: Charitable foundations, religious organizations, trade unions, and political parties providing non-market goods/services to households funded by voluntary donations.
Transactions between these domestic sectors and the outside world are recorded in the **Rest of the World (S.2)** account.

### 3. The Production Boundary
The production boundary defines which economic activities generate economic output included in Gross Domestic Product:
- **Included**: All production of goods (including subsistence agricultural farming by peasant households for own final consumption); all production of services delivered to other institutional units; the production of housing services by owner-occupiers (imputed owner-occupied rent); and illegal or informal economic activities that involve voluntary mutual economic transactions (e.g., unlicensed street vending, or illicit narcotics manufacturing).
- **Excluded**: Unpaid domestic and personal services performed within the household by family members for themselves (unpaid cooking, cleaning, child care, and elderly care). The SNA excludes these unpaid household services not because they lack intrinsic human value, but because they are inseparable from consumption, exhibit no market price signals, and would render macroeconomic monetary policy analysis intractable.

### 4. Quadruple-Entry Bookkeeping Architecture
The SNA records transactions using **quadruple-entry accounting**: because every transaction involves two institutional units (buyer and seller, payer and recipient) and two entries per unit (a resource/liability change and a use/asset change), each single economic transaction generates four simultaneous balancing ledger entries across the national sequence of accounts.

## 7.3 Methodological Triad for Estimating Gross Domestic Product (GDP)

Gross Domestic Product (GDP) represents the total gross market value of all final goods and services produced within the economic territory of a country during a specified accounting period (quarter or calendar year).

The fundamental macroeconomic identity guarantees that GDP can be derived through three mathematically equivalent approaches:

### 1. The Production Approach (Output Method)
The production approach measures the net wealth generated at each stage of the production chain, systematically stripping out double counting. 

For each resident institutional enterprise, define:
- **Gross Output ($GO$)**: The total monetary value of all goods and services produced, valued at **basic prices** (the amount receivable by the producer, excluding taxes on products and including subsidies on products).
- **Intermediate Consumption ($IC$)**: The value of all goods and services consumed as inputs in the production process (raw materials, electricity, fuel, legal fees, sub-contracting), excluding the consumption of fixed capital assets (depreciation).

The **Gross Value Added ($GVA$)** at basic prices is:

$$GVA_{\text{basic}} = GO - IC$$

Summing Gross Value Added across all industrial sectors of the economy yields total economic value added. To convert basic prices to market purchase prices, add taxes on products (sales tax, VAT, excise duties, import tariffs) and subtract subsidies on products:

$$GDP_{\text{production}} = \sum_{j=1}^K GVA_{j, \text{basic}} + (T_{\text{products}} - S_{\text{products}})$$

### 2. The Expenditure Approach (Final Demand Method)
The expenditure approach aggregates the final purchases of all economic actors who buy goods and services for final use (not for further intermediate consumption):

$$GDP_{\text{expenditure}} = C + I + G + (X - M)$$

where:
- $C$ (**Household Final Consumption Expenditure, HFCE**): Expenditures by resident households on consumer durables (automobiles, electronics), semi-durables (clothing), non-durables (food, utilities), and services (education, transport, entertainment), including imputed owner-occupied rent.
- $I$ (**Gross Capital Formation, GCF**): Physical investment in long-term capital assets:
  $$GCF = \text{Gross Fixed Capital Formation (GFCF)} + \text{Changes in Inventories } (\Delta \text{Inv}) + \text{Acquisitions Less Disposals of Valuables}$$
- $G$ (**Government Final Consumption Expenditure, GFCE**): Operating expenditures incurred by general government in producing collective non-market public services (civil servant salaries, public hospital supplies, military operating maintenance).
- $X$ (**Exports of Goods and Services**): Domestic production purchased by non-resident foreign entities (f.o.b. valuation).
- $M$ (**Imports of Goods and Services**): Foreign production consumed by domestic resident entities (c.i.f. / f.o.b. valuation), subtracted to prevent foreign production from inflating domestic GDP.

### 3. The Income Approach (Factor Allocation Method)
The income approach aggregates the primary factor incomes earned by households, corporations, and government in the production of output:

$$GDP_{\text{income}} = COE + GOS + GMI + (T_{\text{production}} - S_{\text{production}})$$

where:
- $COE$ (**Compensation of Employees**): Gross wages and salaries paid in cash or in kind, plus employers' social contributions (pension matching, health insurance premiums, social security).
- $GOS$ (**Gross Operating Surplus**): Capital factor returns (corporate profits, interest, dividends, retained earnings, depreciation) earned by incorporated market enterprises.
- $GMI$ (**Gross Mixed Income**): The return to unincorporated household enterprises (farmers, shopkeepers, independent contractors), which inherently mixes labor compensation and capital profit inseparably.
- $T_{\text{production}} - S_{\text{production}}$: Taxes less subsidies on production and imports (payroll taxes, business licensing, environmental levies).

### Supply and Use Tables (SUT) Reconciliation
In empirical practice, because data sources for the three approaches derive from disparate instruments (business manufacturing surveys, household expenditure surveys, tax filings, customs trade manifests), preliminary estimates invariably display statistical discrepancies:
$$GDP_{\text{production}} \ne GDP_{\text{expenditure}} \ne GDP_{\text{income}}$$
National statistical offices balance and reconcile these discrepancies through the compilation of **Supply and Use Tables (SUT)**. An SUT is a massive rectangular input-output matrix balancing total supply (Output + Imports + Net Taxes) against total use (Intermediate Consumption + Final Consumption + GFCF + Exports) commodity by commodity across hundreds of distinct industrial sectors.

## 7.4 Price Index Theory, Axiomatic Tests, and Deflation

To isolate real volumetric economic growth from nominal monetary inflation, macroeconomic aggregates must be **deflated**. A nominal value index $V_{0, t} = \frac{\sum p_t q_t}{\sum p_0 q_0}$ reflects both quantity expansions $\Delta q$ and price increases $\Delta p$.

### 1. Classical Index Number Formulas
Let $p_0, q_0$ denote prices and quantities of a basket of $N$ commodities in the base period $0$, and $p_t, q_t$ denote prices and quantities in the current period $t$.

- **Laspeyres Price Index ($P_L$)**: Base-period quantity weighted:
  $$P_L = \frac{\sum_{i=1}^N p_{it} q_{i0}}{\sum_{i=1}^N p_{i0} q_{i0}} = \sum_{i=1}^N w_{i0} \left( \frac{p_{it}}{p_{i0}} \right), \qquad w_{i0} = \frac{p_{i0} q_{i0}}{\sum p_{i0} q_{i0}}$$
  The Laspeyres index requires quantity weights only from the historic base year, making it logistically inexpensive to update monthly. However, it exhibits an **upward substitution bias**: it assumes consumers continue purchasing the exact same physical quantities as in year $0$, failing to account for consumer substitution toward goods whose relative prices have fallen.

- **Paasche Price Index ($P_P$)**: Current-period quantity weighted:
  $$P_P = \frac{\sum_{i=1}^N p_{it} q_{it}}{\sum_{i=1}^N p_{i0} q_{it}} = \left[ \sum_{i=1}^N w_{it} \left( \frac{p_{it}}{p_{i0}} \right)^{-1} \right]^{-1}, \qquad w_{it} = \frac{p_{it} q_{it}}{\sum p_{it} q_{it}}$$
  The Paasche index requires real-time collection of current quantities $q_{it}$, which is practically impossible for monthly high-frequency CPI reporting. It exhibits a **downward substitution bias**.

- **Fisher's Ideal Price Index ($P_F$)**: The geometric mean of Laspeyres and Paasche:
  $$P_F = \sqrt{P_L \cdot P_P} = \sqrt{\frac{\sum p_t q_0}{\sum p_0 q_0} \cdot \frac{\sum p_t q_t}{\sum p_0 q_t}}$$
  Irving Fisher (1922) proved that $P_F$ represents a "superlative index"—it provides a second-order flexible approximation to an arbitrary aggregator utility function, perfectly neutralizing substitution bias.

- **Törnqvist Price Index ($P_T$)**: A geometric weighted average using average expenditure shares:
  $$\ln P_T = \sum_{i=1}^N \frac{w_{i0} + w_{it}}{2} \ln\left( \frac{p_{it}}{p_{i0}} \right)$$

### 2. Axiomatic (Test) Properties of Price Indices
Index number theorists formulate formal mathematical criteria (axioms) that a rational price index $P(p_0, p_t, q_0, q_t)$ must satisfy:
1. **Identity Test**: If prices remain unchanged ($p_t = p_0$), $P = 1.0$.
2. **Proportionality Test**: If all current prices scale by constant $\lambda$ ($p_t = \lambda p_0$), $P = \lambda$.
3. **Commensurability (Dimensional Invariance) Test**: The index value is invariant to the physical units of measurement chosen (e.g., measuring wheat in kilograms versus metric tons).
4. **Time Reversal Test**: Exchanging base and current period indices must yield the exact reciprocal:
   $$P(p_0, p_t, q_0, q_t) \cdot P(p_t, p_0, q_t, q_0) = 1.0$$
   *Result*: Fisher's index satisfies Time Reversal; Laspeyres and Paasche fail it!
5. **Factor Reversal Test**: The product of the price index and quantity index must equal the true nominal value ratio:
   $$P(p_0, p_t, q_0, q_t) \cdot Q(p_0, p_t, q_0, q_t) = \frac{\sum p_t q_t}{\sum p_0 q_0}$$
   *Result*: Fisher's index satisfies Factor Reversal; Laspeyres, Paasche, and Törnqvist fail it!

### 3. Chain-Linked Volume Measures
Historically, national accounts fixed base weights for 5 to 10 years (e.g., "GDP at constant 2015 prices"). Over time, structural technological revolutions (e.g., massive drop in computing hardware prices coupled with exponential volume expansion) cause fixed-base volume estimates to become severely distorted (**Gerschenkron effect**).

Under SNA 2008, statistical agencies compute **Annually Chained Volume Indices**. For every adjacent pair of years $(t-1, t)$, a Fisher or Laspeyres volume index is computed using weights from year $t-1$. These short-period link factors are then sequentially multiplied (chained) together:

$$\text{Chain Volume Index}_{0, T} = \prod_{t=1}^T \text{Link Volume Index}_{t-1, t}$$

Chaining eliminates structural weight obsolescence, producing the most accurate long-term trajectories of real GDP growth.

## 7.5 Consumer Price Index (CPI) and Micro-Level Price Aggregation

The **Consumer Price Index (CPI)** is the most widely cited high-frequency indicator of macroeconomic health. It measures the change over time in the general price level of consumer goods and services acquired, used, or paid for by resident households for final consumption.

### The Aggregation Architecture
Compiling a national CPI involves a rigorous multi-stage hierarchy:
1. **Basket Formulation**: Every 5 to 10 years, an NSO conducts an extensive **Household Income and Expenditure Survey (HIES)** to establish the fixed expenditure weights $w_j$ for hundreds of representative consumption items.
2. **Classification Structure**: Goods are classified under the UN **Classification of Individual Consumption According to Purpose (COICOP)** into 12 primary divisions (Food, Housing, Health, Transport, Education, etc.).
3. **Elementary Price Indices**: At the lowest level of aggregation (e.g., a specific brand of parboiled rice in Dhaka wet markets), expenditure weights are unavailable. Field agents collect price quotes $p_{it}$ across retail outlets.

### Elementary Index Formulas: Carli, Dutot, and Jevons
Let $p_{i0}$ and $p_{it}$ denote the price quotes for item variety $i$ across $m$ sampled retail outlets ($i = 1, \dots, m$):

1. **The Carli Index ($P_C$)**: The arithmetic mean of price relatives:
   $$P_C = \frac{1}{m} \sum_{i=1}^m \left( \frac{p_{it}}{p_{i0}} \right)$$
   *Critical Defect*: The Carli index fails the time reversal test! Even if prices fluctuate randomly and return to their baseline values ($p_{i1} \to p_{i0}$), $P_C$ systematically drifts upward ($P_C > 1.0$), introducing severe statistical inflation bias. The UN CPI Manual strongly prohibits Carli.

2. **The Dutot Index ($P_D$)**: The ratio of arithmetic mean prices:
   $$P_D = \frac{\frac{1}{m} \sum_{i=1}^m p_{it}}{\frac{1}{m} \sum_{i=1}^m p_{i0}} = \frac{\sum p_{it}}{\sum p_{i0}}$$
   The Dutot index satisfies time reversal, but fails the commensurability test unless the sampled items are strictly homogeneous. A high-priced item dominates the Dutot index entirely.

3. **The Jevons Index ($P_J$)**: The geometric mean of price relatives (or equivalently, ratio of geometric mean prices):
   $$P_J = \left[ \prod_{i=1}^m \left(\frac{p_{it}}{p_{i0}}\right) \right]^{1/m} = \frac{\left( \prod p_{it} \right)^{1/m}}{\left( \prod p_{i0} \right)^{1/m}}$$
   The Jevons index satisfies both time reversal and commensurability tests. Furthermore, under Cobb-Douglas utility assumptions, Jevons implicitly allows for unitary elasticity of substitution ($e = 1$) between outlet varieties, eliminating elementary substitution bias. Modern international NSOs universally mandate Jevons for elementary aggregation.

### Headline Versus Core Inflation
- **Headline Inflation**: The year-on-year percentage change in the all-items CPI index:
  $$\pi_t = \frac{CPI_t - CPI_{t-12}}{CPI_{t-12}} \times 100\%$$
- **Core Inflation**: Strips out volatile, transitory, and supply-shock-prone sub-baskets (typically fresh food, fruits, vegetables, motor gasoline, and household energy). Central banks target core inflation to guide interest rate adjustments, preventing knee-jerk monetary tightening in response to temporary agricultural droughts or geopolitical oil embargoes.

## 7.6 Industrial Statistics Frameworks and the Index of Industrial Production (IIP)

To track short-term monthly industrial and manufacturing momentum without waiting for quarterly GDP releases, NSOs compile the **Index of Industrial Production (IIP)**.

The IIP is a Laspeyres quantum volume index measuring physical production output across mining, manufacturing, electricity, and gas utilities classified by the **International Standard Industrial Classification (ISIC Rev. 4)**.

Let $q_{it}$ denote the physical volume of production for industrial commodity $i$ in month $t$, and let $q_{i0}$ denote baseline physical volume. The IIP is:

$$\text{IIP}_t = \sum_{i=1}^M W_{i0} \left( \frac{q_{it}}{q_{i0}} \right) \times 100$$

where the weights $W_{i0}$ represent the relative share of each commodity in total **Gross Value Added (GVA)** of the industrial sector in the base year:

$$W_{i0} = \frac{GVA_{i0}}{\sum_{j=1}^M GVA_{j0}}, \qquad \sum_{i=1}^M W_{i0} = 1.0$$

Because monthly industrial production series exhibit pronounced calendar day-count fluctuations and recurring annual cycles (e.g., textile production peaks prior to Eid, or fertilizer production peaks during planting seasons), official agencies seasonally adjust the raw IIP using algorithmic time series filters such as **X-13ARIMA-SEATS** or **TRAMO-SEATS**.

## 7.7 Input-Output Economics: The Leontief Multiplier Matrix and Inter-Industry Linkages

A crowning analytical achievement of the System of National Accounts is the derivation of symmetric **Input-Output (I-O) Tables**, pioneered by Nobel laureate Wassily Leontief (1941). While GDP summarizes aggregate macroeconomic volume, Input-Output analysis models the intricate technological interdependencies connecting every productive sector of the industrial economy.

### The Mathematical Input-Output Architecture
Consider an economy partitioned into $n$ distinct industrial sectors. Let:
- $X_i$: Total gross output of sector $i$.
- $z_{ij}$: The monetary value of output produced by sector $i$ that is consumed as intermediate input by sector $j$ in its production process.
- $Y_i$: Final demand for the output of sector $i$ (household consumption, government spending, capital investment, and exports).

The fundamental material balance equation for sector $i$ states that total output equals intermediate demand plus final demand:

$$X_i = \sum_{j=1}^n z_{ij} + Y_i, \qquad i = 1, 2, \dots, n$$

### Technical Coefficients Matrix ($\mathbf{A}$)
Leontief introduced the assumption of fixed-proportion production technologies (constant returns to scale with zero input substitution). The **technical coefficient** $a_{ij}$ represents the value of input from sector $i$ required to produce one monetary unit of output in sector $j$:

$$a_{ij} = \frac{z_{ij}}{X_j}$$

Substituting $z_{ij} = a_{ij} X_j$ into the balance equation yields:

$$X_i = \sum_{j=1}^n a_{ij} X_j + Y_i$$

In matrix notation:

$$\mathbf{X} = \mathbf{A} \mathbf{X} + \mathbf{Y}$$

where $\mathbf{X} = (X_1, \dots, X_n)^T$ is the gross output vector, $\mathbf{Y} = (Y_1, \dots, Y_n)^T$ is the final demand vector, and $\mathbf{A} = [a_{ij}]$ is the $n \times n$ matrix of technical coefficients.

### The Leontief Inverse Matrix
Rearranging the matrix balance equation:

$$(\mathbf{I} - \mathbf{A}) \mathbf{X} = \mathbf{Y}$$

Assuming the matrix $(\mathbf{I} - \mathbf{A})$ is non-singular (which is guaranteed if the economy is productive under the Hawkins-Simon conditions):

$$\mathbf{X} = (\mathbf{I} - \mathbf{A})^{-1} \mathbf{Y} = \mathbf{L} \mathbf{Y}$$

where $\mathbf{L} = (\mathbf{I} - \mathbf{A})^{-1} = [l_{ij}]$ is the celebrated **Leontief Inverse Matrix** (or Total Requirements Matrix).

Expanding $\mathbf{L}$ as a geometric matrix power series reveals its economic meaning:

$$(\mathbf{I} - \mathbf{A})^{-1} = \mathbf{I} + \mathbf{A} + \mathbf{A}^2 + \mathbf{A}^3 + \dots$$
- $\mathbf{I}$: The direct initial impact of satisfying final demand $\mathbf{Y}$.
- $\mathbf{A}$: The first-round direct intermediate inputs required from suppliers.
- $\mathbf{A}^2$: The second-round indirect intermediate inputs required by those suppliers to produce their inputs.
- $\mathbf{A}^k$: The infinite cascade of higher-order indirect ripple effects propagating across the supply chain!

Each element $l_{ij}$ measures the total dollar increase in gross output required from sector $i$ to satisfy a one-dollar increase in final demand for the products of sector $j$.

### Forward and Backward Industrial Linkages
Albert O. Hirschman (1958) utilized the Leontief inverse to identify key industrial growth sectors:
1. **Backward Linkage Multiplier ($BL_j$)**: The column sum of the Leontief inverse:
   $$BL_j = \sum_{i=1}^n l_{ij}$$
   $BL_j$ measures the total economic stimulus transmitted backward into the upstream supply chain when demand for sector $j$ expands. Sectors with $BL_j > 1$ (e.g., automotive manufacturing, basic steel) act as powerful economic locomotives.
2. **Forward Linkage Multiplier ($FL_i$)**: The row sum of the Leontief inverse:
   $$FL_i = \sum_{j=1}^n l_{ij}$$
   $FL_i$ measures the sensitivity of sector $i$ to expansions across all downstream customer industries (e.g., electric power utilities, petroleum refining).

## Fully worked question 1: Comprehensive GDP Reconciliation Across Production, Expenditure, and Income

### Question
The National Accounts Division of a developing country compiles preliminary annual national accounting data (in billions of local currency units, BDT). The statistical registers report the following primary macroeconomic aggregates for the accounting year:

**Production Approach Data (at Basic Prices)**:
- Agriculture, Forestry, and Fisheries: Output $GO_A = 4,200$, Intermediate Consumption $IC_A = 1,400$
- Mining, Manufacturing, and Utilities: Output $GO_M = 12,800$, Intermediate Consumption $IC_M = 7,600$
- Construction: Output $GO_C = 3,500$, Intermediate Consumption $IC_C = 2,100$
- Services (Wholesale, Retail, Transport, Finance, Public Admin): Output $GO_S = 24,000$, Intermediate Consumption $IC_S = 9,500$
- Taxes on Products: $T_{\text{products}} = 2,150$
- Subsidies on Products: $S_{\text{products}} = 350$

**Expenditure Approach Data**:
- Household Final Consumption Expenditure ($C$): $17,800$
- Government Final Consumption Expenditure ($G$): $3,450$
- Gross Fixed Capital Formation ($GFCF$): $7,200$
- Changes in Inventories ($\Delta \text{Inv}$): $+450$
- Acquisitions less Disposals of Valuables: $+100$
- Exports of Goods and Services ($X$): $4,200$
- Imports of Goods and Services ($M$): $7,400$

**Income Approach Data**:
- Compensation of Employees ($COE$): $11,500$
- Gross Operating Surplus ($GOS$): $9,800$
- Gross Mixed Income ($GMI$): $2,400$
- Other Taxes on Production (excluding product taxes): $450$
- Other Subsidies on Production: $100$

Perform the following calculations:
1. Compute the Gross Value Added at basic prices ($GVA$) for each of the four industrial sectors.
2. Calculate total $GDP$ from the Production Approach at market prices.
3. Calculate total $GDP$ from the Expenditure Approach at market prices.
4. Calculate total $GDP$ from the Income Approach at market prices.
5. Determine whether any statistical discrepancy exists among the three independent estimates.

### Solution, step 1: Compute GVA by industry
Using $GVA_{\text{basic}} = GO - IC$:
- Agriculture: $GVA_A = 4,200 - 1,400 = 2,800\text{ billion}$
- Manufacturing & Industry: $GVA_M = 12,800 - 7,600 = 5,200\text{ billion}$
- Construction: $GVA_C = 3,500 - 2,100 = 1,400\text{ billion}$
- Services: $GVA_S = 24,000 - 9,500 = 14,500\text{ billion}$

Total Gross Value Added at basic prices across all industries:
$$GVA_{\text{total, basic}} = 2,800 + 5,200 + 1,400 + 14,500 = 23,900\text{ billion}$$

### Solution, step 2: Compute GDP via Production Approach
Convert basic prices to market prices by adding net product taxes:
$$\text{Net Taxes on Products} = T_{\text{products}} - S_{\text{products}} = 2,150 - 350 = 1,800\text{ billion}$$
$$GDP_{\text{production}} = GVA_{\text{total, basic}} + (T_{\text{products}} - S_{\text{products}}) = 23,900 + 1,800 = 25,700\text{ billion}$$
The Production Approach yields a GDP of **$25,700\text{ billion BDT}$**.

### Solution, step 3: Compute GDP via Expenditure Approach
First compute total Gross Capital Formation ($I$):
$$I = GFCF + \Delta \text{Inv} + \text{Valuables} = 7,200 + 450 + 100 = 7,750\text{ billion}$$
Next compute Net Exports:
$$NX = X - M = 4,200 - 7,400 = -3,200\text{ billion}$$
Now aggregate final expenditure components:
$$GDP_{\text{expenditure}} = C + G + I + (X - M) = 17,800 + 3,450 + 7,750 + (-3,200)$$
$$= 21,250 + 7,750 - 3,200 = 29,000 - 3,200 = 25,800\text{ billion}$$
The Expenditure Approach yields a GDP of **$25,800\text{ billion BDT}$**.

### Solution, step 4: Compute GDP via Income Approach
First compute Net Taxes on Production:
$$\text{Net Other Taxes on Production} = 450 - 100 = 350\text{ billion}$$
Total Net Taxes on Production and Imports $= \text{Net Other Taxes on Production} + \text{Net Taxes on Products}$:
$$\text{Total Net Indirect Taxes} = 350 + 1,800 = 2,150\text{ billion}$$
Now aggregate factor returns:
$$GDP_{\text{income}} = COE + GOS + GMI + \text{Total Net Indirect Taxes}$$
$$= 11,500 + 9,800 + 2,400 + 2,150$$
$$= 23,700 + 2,150 = 25,850\text{ billion}$$
The Income Approach yields a GDP of **$25,850\text{ billion BDT}$**.

### Solution, step 5: Analyze statistical discrepancies
Summarizing the three independent estimates:
- $GDP_{\text{production}} = 25,700\text{ billion}$
- $GDP_{\text{expenditure}} = 25,800\text{ billion}$
- $GDP_{\text{income}} = 25,850\text{ billion}$

Discrepancy:
- Difference between Expenditure and Production $= +100\text{ billion}$ ($+0.39\%$).
- Difference between Income and Production $= +150\text{ billion}$ ($+0.58\%$).

Because these discrepancies are well within standard international survey error margins ($< 1\%$), the National Accounts Division compiles an official Supply and Use Table (SUT) to balance intermediate transactions and publish an integrated final balanced estimate of approximately $25,780\text{ billion BDT}$.

## Fully worked question 2: Axiomatic Evaluation of Price Index Numbers and Superlative Deflation

### Question
The national statistical office compiles a price and quantity monitoring audit for three primary fuel commodities: Petroleum ($i=1$), Natural Gas ($i=2$), and Electricity ($i=3$). The observed retail prices ($p$) and consumed physical quantities ($q$) for baseline period $0$ and current period $t$ are:

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Commodity</th>
<th>Base Price $p_0$ (\$/unit)</th>
<th>Base Quantity $q_0$</th>
<th>Current Price $p_t$ (\$/unit)</th>
<th>Current Quantity $q_t$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1. Petroleum (barrel)</td>
<td>80.00</td>
<td>500</td>
<td>120.00</td>
<td>400</td>
</tr>
<tr>
<td>2. Natural Gas (MMBtu)</td>
<td>4.00</td>
<td>10,000</td>
<td>6.00</td>
<td>8,000</td>
</tr>
<tr>
<td>3. Electricity (MWh)</td>
<td>50.00</td>
<td>800</td>
<td>55.00</td>
<td>1,000</td>
</tr>
</tbody>
</table>
</div>

Perform the following calculations:
1. Compute the four primary cross-products: $\sum p_0 q_0$, $\sum p_t q_0$, $\sum p_0 q_t$, and $\sum p_t q_t$.
2. Compute the Laspeyres Price Index ($P_L$) and Paasche Price Index ($P_P$).
3. Compute Fisher's Ideal Price Index ($P_F$).
4. Compute the Laspeyres Quantity Index ($Q_L$), Paasche Quantity Index ($Q_P$), and Fisher Quantity Index ($Q_F$).
5. Demonstrate mathematically whether Fisher's Ideal Index satisfies the Factor Reversal Test.

### Solution, step 1: Compute cross-product sums
Calculate each summation term across the three commodities:
1. **Base Value $\sum p_0 q_0$**:
   - Petroleum: $80.00 \times 500 = 40,000$
   - Natural Gas: $4.00 \times 10,000 = 40,000$
   - Electricity: $50.00 \times 800 = 40,000$
   $$\sum p_0 q_0 = 40,000 + 40,000 + 40,000 = \$120,000$$

2. **Laspeyres Hybrid $\sum p_t q_0$**:
   - Petroleum: $120.00 \times 500 = 60,000$
   - Natural Gas: $6.00 \times 10,000 = 60,000$
   - Electricity: $55.00 \times 800 = 44,000$
   $$\sum p_t q_0 = 60,000 + 60,000 + 44,000 = \$164,000$$

3. **Paasche Hybrid $\sum p_0 q_t$**:
   - Petroleum: $80.00 \times 400 = 32,000$
   - Natural Gas: $4.00 \times 8,000 = 32,000$
   - Electricity: $50.00 \times 1,000 = 50,000$
   $$\sum p_0 q_t = 32,000 + 32,000 + 50,000 = \$114,000$$

4. **Current Value $\sum p_t q_t$**:
   - Petroleum: $120.00 \times 400 = 48,000$
   - Natural Gas: $6.00 \times 8,000 = 48,000$
   - Electricity: $55.00 \times 1,000 = 55,000$
   $$\sum p_t q_t = 48,000 + 48,000 + 55,000 = \$151,000$$

### Solution, step 2: Compute Laspeyres and Paasche price indices
1. **Laspeyres Price Index ($P_L$)**:
   $$P_L = \frac{\sum p_t q_0}{\sum p_0 q_0} = \frac{164,000}{120,000} \approx 1.36667 \implies 136.67$$
   Indicates a $36.67\%$ price increase.

2. **Paasche Price Index ($P_P$)**:
   $$P_P = \frac{\sum p_t q_t}{\sum p_0 q_t} = \frac{151,000}{114,000} \approx 1.32456 \implies 132.46$$
   Indicates a $32.46\%$ price increase.

Notice that $P_L (136.67) > P_P (132.46)$, clearly demonstrating Laspeyres upward substitution bias!

### Solution, step 3: Compute Fisher's Ideal Price Index ($P_F$)
$$P_F = \sqrt{P_L \cdot P_P} = \sqrt{1.36667 \times 1.32456} = \sqrt{1.810237} \approx 1.34545 \implies 134.55$$
Fisher's index measures the true cost inflation at **$34.55\%$**.

### Solution, step 4: Compute Quantity Indices ($Q_L, Q_P, Q_F$)
1. **Laspeyres Quantity Index ($Q_L$)**:
   $$Q_L = \frac{\sum p_0 q_t}{\sum p_0 q_0} = \frac{114,000}{120,000} = 0.95000 \implies 95.00$$
   Physical fuel consumption declined by $5.00\%$.

2. **Paasche Quantity Index ($Q_P$)**:
   $$Q_P = \frac{\sum p_t q_t}{\sum p_t q_0} = \frac{151,000}{164,000} \approx 0.92073 \implies 92.07$$

3. **Fisher Quantity Index ($Q_F$)**:
   $$Q_F = \sqrt{Q_L \cdot Q_P} = \sqrt{0.95000 \times 0.92073} = \sqrt{0.874694} \approx 0.93525 \implies 93.53$$
   Real volume contracted by $6.47\%$.

### Solution, step 5: Verify the Factor Reversal Test
The Factor Reversal Test requires:
$$P \times Q = \text{Nominal Value Ratio } V_{0, t} = \frac{\sum p_t q_t}{\sum p_0 q_0}$$
The actual nominal value ratio is:
$$V_{0, t} = \frac{151,000}{120,000} \approx 1.258333$$

Now evaluate the product of Fisher's price and quantity indices:
$$P_F \times Q_F = \sqrt{\frac{\sum p_t q_0}{\sum p_0 q_0} \cdot \frac{\sum p_t q_t}{\sum p_0 q_t}} \times \sqrt{\frac{\sum p_0 q_t}{\sum p_0 q_0} \cdot \frac{\sum p_t q_t}{\sum p_t q_0}}$$
$$= \sqrt{\frac{\sum p_t q_0}{\sum p_0 q_0} \cdot \frac{\sum p_t q_t}{\sum p_0 q_t} \cdot \frac{\sum p_0 q_t}{\sum p_0 q_0} \cdot \frac{\sum p_t q_t}{\sum p_t q_0}}$$
Notice that $\sum p_t q_0$ cancels from numerator and denominator, and $\sum p_0 q_t$ cancels from numerator and denominator!
$$P_F \times Q_F = \sqrt{\frac{(\sum p_t q_t)^2}{(\sum p_0 q_0)^2}} = \frac{\sum p_t q_t}{\sum p_0 q_0} = V_{0, t}$$
Numerically:
$$P_F \times Q_F = 1.345451 \times 0.935251 \approx 1.258333$$
$$V_{0, t} = \frac{151,000}{120,000} \approx 1.258333$$
The identity holds with absolute mathematical perfection. Fisher's Ideal Index satisfies the Factor Reversal Test.

## Fully worked question 3: Micro-Level CPI Aggregation and Inflation Decomposition

### Question
A metropolitan statistical office collects monthly retail price quotes for Grade-A eggs across five representative urban markets. The collected price quotes (in BDT per dozen) for Month 0 (base) and Month 1 (current) are:
- Outlet 1: $p_{1,0} = 120.00$, $p_{1,1} = 150.00$
- Outlet 2: $p_{2,0} = 100.00$, $p_{2,1} = 125.00$
- Outlet 3: $p_{3,0} = 140.00$, $p_{3,1} = 140.00$
- Outlet 4: $p_{4,0} = 110.00$, $p_{4,1} = 132.00$
- Outlet 5: $p_{5,0} = 130.00$, $p_{5,1} = 156.00$

Perform the following calculations:
1. Compute the individual price relatives $R_i = p_{i,1} / p_{i,0}$ for all five outlets.
2. Compute the Carli Elementary Price Index ($P_C$).
3. Compute the Dutot Elementary Price Index ($P_D$).
4. Compute the Jevons Elementary Price Index ($P_J$).
5. Demonstrate mathematically why Carli overstates inflation relative to Jevons, and state which index the statistical office must report under international standards.

### Solution, step 1: Compute individual price relatives
- Outlet 1: $R_1 = 150.00 / 120.00 = 1.2500$ ($+25.0\%$)
- Outlet 2: $R_2 = 125.00 / 100.00 = 1.2500$ ($+25.0\%$)
- Outlet 3: $R_3 = 140.00 / 140.00 = 1.0000$ ($0.0\%$)
- Outlet 4: $R_4 = 132.00 / 110.00 = 1.2000$ ($+20.0\%$)
- Outlet 5: $R_5 = 156.00 / 130.00 = 1.2000$ ($+20.0\%$)

### Solution, step 2: Compute the Carli Index ($P_C$)
The Carli index is the arithmetic mean of price relatives:
$$P_C = \frac{1}{5} \sum_{i=1}^5 R_i = \frac{1.2500 + 1.2500 + 1.0000 + 1.2000 + 1.2000}{5} = \frac{5.9000}{5} = 1.1800 \implies 118.00$$
Carli indicates an egg price inflation of **$18.00\%$**.

### Solution, step 3: Compute the Dutot Index ($P_D$)
The Dutot index is the ratio of average prices:
$$\text{Base Average Price} = \bar{p}_0 = \frac{120 + 100 + 140 + 110 + 130}{5} = \frac{600}{5} = 120.00\text{ BDT}$$
$$\text{Current Average Price} = \bar{p}_1 = \frac{150 + 125 + 140 + 132 + 156}{5} = \frac{703}{5} = 140.60\text{ BDT}$$
$$P_D = \frac{\bar{p}_1}{\bar{p}_0} = \frac{140.60}{120.00} \approx 1.17167 \implies 117.17$$
Dutot indicates an egg price inflation of **$17.17\%$**.

### Solution, step 4: Compute the Jevons Index ($P_J$)
The Jevons index is the geometric mean of price relatives:
$$P_J = \left( \prod_{i=1}^5 R_i \right)^{1/5} = (1.25 \times 1.25 \times 1.00 \times 1.20 \times 1.20)^{1/5}$$
Compute the product:
$$\text{Product} = 1.5625 \times 1.00 \times 1.44 = 2.2500$$
Now take the 5th root:
$$P_J = (2.2500)^{0.20}$$
Evaluating $\ln(2.2500) \approx 0.810930$:
$$0.20 \times 0.810930 = 0.162186$$
$$P_J = \exp(0.162186) \approx 1.17608 \implies 117.61$$
Jevons indicates an egg price inflation of **$17.61\%$**.

### Solution, step 5: Comparison and International Reporting Standard
Comparing the three results:
- Carli: $118.00$ ($+18.00\%$)
- Jevons: $117.61$ ($+17.61\%$)
- Dutot: $117.17$ ($+17.17\%$)

By the Arithmetic Mean-Geometric Mean inequality ($\text{AM} \ge \text{GM}$), the Carli index is mathematically guaranteed to equal or exceed the Jevons index for any non-identical price movements ($P_C \ge P_J$). Carli’s arithmetic structure introduces an unavoidable upward drift bias and fails the time reversal test.

**Official Reporting Mandate**:
Under the United Nations/IMF/ILO Consumer Price Index Manual (2020), national statistical offices are required to compile and report the **Jevons Index ($P_J = 117.61$)**. Jevons satisfies the time reversal test, is invariant to physical units of measurement, and accurately accounts for micro-level consumer substitution between retail outlets.
