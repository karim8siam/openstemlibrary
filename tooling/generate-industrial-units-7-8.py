#!/usr/bin/env python3
"""
Generate Units 7 and 8 for Industrial and Official Statistics.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

unit_7 = r"""# Unit 7: National Statistical Systems, SNA Framework & Macroeconomic Output Measurement

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
"""

unit_8 = r"""# Unit 8: Social, Labor, Poverty & Sustainable Development Statistics in Official Governance

## 8.1 Modern Labor Force Statistics and the ILO 19th ICLS Resolution

Labor force statistics measure the mobilization of human resources in economic production, the standard of living of households, and the structural dynamics of employment, unemployment, and labor underutilization. 

In 2013, the 19th International Conference of Labour Statisticians (ICLS), convened by the International Labour Organization (ILO), adopted a revolutionary resolution fundamentally reforming the statistical definition of work. The 19th ICLS framework established that **work** encompasses any human activity producing goods or services for consumption by others or for own use. It partitioned work into five mutually exclusive forms:
1. **Own-Use Production Work**: Producing goods or services for own final household consumption (e.g., subsistence farming, collecting firewood, fetching water, home cooking, childcare).
2. **Employment Work**: Work performed in exchange for pay, profit, or family gain.
3. **Unpaid Trainee Work**: Apprenticeships, internships, and clinical residencies performed without financial compensation.
4. **Volunteer Work**: Non-compulsory work performed without pay for charitable organizations or other households.
5. **Other Work Activities**: Unpaid community service, mandatory work by prisoners.

Crucially, **only Employment Work enters the official Labor Force**. The other four forms of work are recognized as productive human activity but are tracked via separate satellite accounts, preventing the dilution of economic employment metrics.

### Decomposition of the Working-Age Population
The national statistical system defines the **Working-Age Population ($WAP$)** (typically individuals aged 15 years and older residing in private households, excluding institutional populations in prisons or military barracks). The working-age population is divided into two mutually exclusive categories:

$$WAP = \text{Labor Force } (LF) + \text{Outside the Labor Force } (OLF)$$

The **Labor Force ($LF$)** comprises all persons who supply labor for the production of goods and services for pay or profit:

$$LF = \text{Employed } (E) + \text{Unemployed } (U)$$

### Operational Definitions
1. **Employed ($E$)**: All persons of working age who, during a short reference period of seven days (the reference week), engaged in any activity to produce goods or provide services for pay or profit for **at least one hour**. The one-hour criterion ensures that all forms of precarious, casual, part-time, and informal work are captured. The employed category also includes persons temporarily absent from a job (due to illness, annual leave, maternity leave, or strike).
2. **Unemployed ($U$)**: All persons of working age who simultaneously satisfy three strict criteria during the reference period:
   - **Without Work**: Not employed (did not work even one hour for pay or profit).
   - **Currently Available**: Available to start work within a specified short period (typically within the reference week or following two weeks).
   - **Actively Seeking Work**: Took specific, verifiable steps in a specified recent period (past four weeks) to seek paid employment or self-employment (e.g., applying to job postings, submitting CVs, registering at employment exchanges, placing advertisements, applying for business loans).
3. **Outside the Labor Force ($OLF$)**: All working-age individuals who are neither employed nor unemployed (full-time students, retired persons, homemakers engaged exclusively in unpaid domestic duties, persons with severe disabilities, and discouraged job-seekers).

### Core Headline Indicators
1. **Labor Force Participation Rate ($LFPR$)**:
   $$LFPR = \frac{LF}{WAP} \times 100\% = \frac{E + U}{WAP} \times 100\%$$
2. **Employment-to-Population Ratio ($EPR$)**:
   $$EPR = \frac{E}{WAP} \times 100\%$$
3. **Unemployment Rate ($UR$)**:
   $$UR = \frac{U}{LF} \times 100\% = \frac{U}{E + U} \times 100\%$$

Notice that the Unemployment Rate is calculated as a percentage of the **Labor Force**, *not* of the total population!

## 8.2 Labor Underutilization and Decent Work Deficits

In developing and low-income economies (such as Bangladesh, India, or Kenya), the headline Unemployment Rate is frequently surprisingly low (e.g., $3\%$ to $5\%$). This paradox occurs because in the absence of comprehensive universal unemployment insurance, impoverished individuals cannot afford to remain idle while actively searching for formal jobs. They must survive by engaging in precarious informal activities—selling tea, rickshaw pulling, day labor—which classifies them as "employed" under the one-hour rule.

To provide an honest, multidimensional diagnostic of labor distress, the ILO 19th ICLS resolution formulated four composite **Measures of Labor Underutilization (LU1 to LU4)**:

### 1. Time-Related Underemployment ($TRU$)
Persons in employment who wanted to work additional hours, whose working hours were below a designated threshold (typically 35 or 40 hours per week), and who were available to work additional hours.

### 2. The Potential Labor Force ($PLF$)
Working-age individuals outside the labor force who exhibit an attachment to the labor market, consisting of:
- **Unavailable Jobseekers**: Persons who actively searched for work but were not immediately available to start.
- **Available Potential Jobseekers (Discouraged Workers)**: Persons who want to work and are immediately available, but did not actively seek work during the past four weeks because they believe no suitable jobs exist, they lack skills, or they gave up searching.

### The Four Underutilization Rates
- **$LU_1$ (Unemployment Rate)**:
  $$LU_1 = \frac{U}{LF} \times 100\%$$
- **$LU_2$ (Combined Rate of Time-Related Underemployment and Unemployment)**:
  $$LU_2 = \frac{U + TRU}{LF} \times 100\%$$
- **$LU_3$ (Combined Rate of Unemployment and Potential Labor Force)**:
  $$LU_3 = \frac{U + PLF}{LF + PLF} \times 100\%$$
- **$LU_4$ (Composite Measure of Labor Underutilization)**:
  $$LU_4 = \frac{U + TRU + PLF}{LF + PLF} \times 100\%$$

$LU_4$ represents the total unmet need for employment in the national economy, capturing the full magnitude of idle and underemployed human potential.

### Informal Employment and Decent Work
The ILO defines **Informal Employment** as jobs lacking basic social protections, written employment contracts, paid annual leave, or severance pay, occurring in either:
- **The Informal Sector**: Unincorporated household enterprises not registered with national authorities.
- **Formal Enterprises**: Formal corporations employing informal workers off the books to evade labor taxes.

Official systems track the **Decent Work Agenda** through indicators including the Gender Wage Gap, the Fatal Occupational Injury Rate, and the **NEET Rate** (the proportion of youth aged 15–24 Not in Education, Employment, or Training).

## 8.3 Poverty Measurement Methodologies and Poverty Lines

Poverty measurement evaluates whether an individual or household possesses sufficient economic resources to attain an acceptable minimum standard of living.

### 1. Absolute Versus Relative Poverty Lines
- **Absolute Poverty Line**: Fixed in terms of the purchasing power required to command a defined physical basket of essential goods and services (food, clothing, shelter). The real value of an absolute poverty line remains constant over time, updating only for inflation. Standard in developing countries and for international monitoring (e.g., the World Bank global absolute poverty line of \$2.15 per day at 2017 Purchasing Power Parity).
- **Relative Poverty Line**: Defined relative to the prevailing economic standard of the society, typically set at $50\%$ or $60\%$ of national median equivalized disposable household income. Standard in the European Union and OECD countries. As society gets richer, the relative poverty line rises automatically.

### 2. The Cost of Basic Needs (CBN) Method
The **Cost of Basic Needs (CBN)** approach, widely deployed by NSOs across Asia and Africa, constructs the poverty line in two sequential stages:

#### Step 1: The Food Poverty Line ($Z_F$)
1. Nutritional experts establish a minimum recommended daily dietary energy intake per capita (typically $2,122\text{ kcal}$ per day, including minimum protein standards).
2. Economists define a normative food basket representing the consumption patterns of the bottom three deciles of the population (rice, pulses, vegetables, oil, fish, milk).
3. The quantities in this food basket are priced using local retail market prices to compute the **Food Poverty Line ($Z_F$)**: the exact monetary cost required to purchase the minimum nutritional basket.

#### Step 2: The Non-Food Allowance and Overall Poverty Lines
Because even the poorest households must purchase clothing, shelter, and medical care, a non-food allowance must be added to $Z_F$:
- **Lower Poverty Line ($Z_{\text{lower}}$)**: Evaluates the non-food expenditure of households whose *total* consumption expenditure is approximately equal to the food poverty line ($Y_i \approx Z_F$). Because these households sacrifice necessary food to afford shelter and clothing, their non-food spending ($NF_{\text{minimal}}$) represents an absolute minimal survival allowance:
  $$Z_{\text{lower}} = Z_F + NF_{\text{minimal}}$$
  Households below $Z_{\text{lower}}$ are classified as living in **extreme poverty**.
- **Upper Poverty Line ($Z_{\text{upper}}$)**: Evaluates the non-food expenditure of households whose *food* consumption expenditure equals the food poverty line ($F_i \approx Z_F$). Their non-food spending ($NF_{\text{typical}}$) represents a broader social allowance:
  $$Z_{\text{upper}} = Z_F + NF_{\text{typical}}$$
  Households below $Z_{\text{upper}}$ are classified as living in **moderate poverty**.

## 8.4 The Foster-Greer-Thorbecke (FGT) Class of Poverty Metrics

In 1984, Erik Foster, Joel Greer, and Erik Thorbecke formulated an axiomatic family of poverty metrics that unified the entire mathematical theory of poverty analysis.

Let a population consist of $N$ individuals with welfare metrics (income or consumption expenditure) sorted in ascending order:
$$y_1 \le y_2 \le \dots \le y_q < z \le y_{q+1} \le \dots \le y_N$$
where $z$ is the official poverty line, and $q$ is the total number of individuals whose income falls strictly below the poverty line ($y_i < z$).

The **Foster-Greer-Thorbecke ($P_\alpha$) Metric** is defined as:

$$P_\alpha = \frac{1}{N} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^\alpha, \qquad \alpha \ge 0$$

where $\alpha$ is a poverty aversion parameter governing the ethical sensitivity of the metric to the depth and severity of poverty.

### Special Cases of the FGT Metric
1. **$\alpha = 0$: The Headcount Ratio ($P_0$ / $H$)**:
   $$P_0 = \frac{1}{N} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^0 = \frac{q}{N}$$
   The Headcount Ratio measures the **incidence (prevalence)** of poverty: the proportion of the national population living below the poverty line.
   *Axiomatic Limitation*: $P_0$ violates Sen’s Monotonicity Axiom (if a poor person becomes poorer, $P_0$ does not change) and Transfer Axiom (if income is transferred from a poor person to a richer person, $P_0$ remains unchanged).

2. **$\alpha = 1$: The Poverty Gap Index ($P_1$ / $PG$)**:
   $$P_1 = \frac{1}{N} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^1 = H \times I$$
   where $I = \frac{1}{q} \sum_{i=1}^q \frac{z - y_i}{z}$ is the **Income Gap Ratio** (the average shortfall among the poor expressed as a fraction of the poverty line).
   $P_1$ measures the **depth** of poverty. It satisfies the Monotonicity Axiom. Multiplying $P_1 \times z \times N$ calculates the exact total monetary transfer required to bring every poor citizen precisely up to the poverty line under perfect targeting!

3. **$\alpha = 2$: The Squared Poverty Gap (Poverty Severity Index, $P_2$)**:
   $$P_2 = \frac{1}{N} \sum_{i=1}^q \left( \frac{z - y_i}{z} \right)^2$$
   By squaring the normalized poverty gap, $P_2$ assigns progressively higher mathematical weight to the poorest of the poor. $P_2$ satisfies both the Monotonicity Axiom and Sen’s Transfer Axiom (a transfer from a poor person to a less-poor person strictly increases $P_2$).

### Subgroup Decomposability
A decisive advantage of the FGT family is **additive subgroup decomposability**. If a population of size $N$ is partitioned into $M$ mutually exclusive demographic or geographic subgroups (e.g., urban vs rural, or 8 administrative divisions) with sizes $N_j$ and poverty metrics $P_{\alpha, j}$:

$$P_\alpha = \sum_{j=1}^M \frac{N_j}{N} P_{\alpha, j}$$

The percentage contribution of subgroup $j$ to national poverty is $C_j = \frac{N_j P_{\alpha, j}}{N P_\alpha} \times 100\%$, providing policymakers with an indispensable tool for spatial poverty targeting.

## 8.5 Income and Consumption Inequality: Lorenz Curves and the Gini Coefficient

While poverty focuses exclusively on the segment of the population falling below an absolute threshold $z$, inequality evaluates the relative dispersion of economic resources across the entire national distribution.

### The Lorenz Curve
Max O. Lorenz (1905) formulated the **Lorenz Curve** $L(p)$, which plots the cumulative proportion of total national income or consumption expenditure received by the bottom $p$ proportion of the population ($p \in [0, 1]$).

Let income $Y$ have cumulative distribution function $F(y)$ with mean $\mu = \mathbb{E}[Y]$. The Lorenz curve is defined as:

$$L(p) = \frac{\int_0^p F^{-1}(u)\,du}{\int_0^1 F^{-1}(u)\,du} = \frac{1}{\mu} \int_0^p F^{-1}(u)\,du$$

#### Mathematical Properties of the Lorenz Curve
1. $L(0) = 0$ (the bottom $0\%$ owns $0\%$ of income).
2. $L(1) = 1$ (the bottom $100\%$ owns $100\%$ of income).
3. $L(p) \le p$ for all $p \in [0, 1]$: the curve lies entirely below the 45-degree diagonal line of perfect equality ($L_{\text{equality}}(p) = p$).
4. The slope of the Lorenz curve is non-negative and monotonically increasing:
   $$L'(p) = \frac{F^{-1}(p)}{\mu} \ge 0, \qquad L''(p) = \frac{1}{\mu f(F^{-1}(p))} \ge 0$$
   The Lorenz curve is strictly convex to the horizontal axis.

### The Gini Coefficient ($G$)
Corrado Gini (1912) defined the **Gini Coefficient** as the ratio of the area between the 45-degree line of perfect equality and the Lorenz curve (Area $A$) to the total triangular area beneath the equality line (Area $A + B = 0.5$):

$$G = \frac{\text{Area } A}{\text{Area } A + B} = \frac{\text{Area } A}{0.5} = 2 \text{ Area } A = 2 \int_0^1 (p - L(p))\,dp = 1 - 2 \int_0^1 L(p)\,dp$$

#### Discrete Formulation for Sample Data
For a sample of $n$ individuals with sorted incomes $y_1 \le y_2 \le \dots \le y_n$ and sample mean $\bar{y} = \frac{1}{n} \sum y_i$, the Gini coefficient equals half the relative mean absolute difference:

$$G = \frac{\sum_{i=1}^n \sum_{j=1}^n |y_i - y_j|}{2 n^2 \bar{y}} = \frac{2 \sum_{i=1}^n i \cdot y_i}{n \sum_{i=1}^n y_i} - \frac{n + 1}{n}$$

The Gini coefficient ranges from $0.0$ (perfect equality, every person has identical income) to $1.0$ (perfect inequality, one single person possesses all national wealth while everyone else has zero). In empirical national economies, consumption Gini coefficients typically range from $0.25$ to $0.35$ (low inequality) to $0.45$ to $0.65$ (severe inequality).

### Supplementary Inequality Metrics
1. **The Palma Ratio**: The ratio of the richest $10\%$ of the population's share of gross national income to the poorest $40\%$'s share:
   $$\text{Palma} = \frac{\text{Income Share of Top } 10\%}{\text{Income Share of Bottom } 40\%}$$
   Gabriel Palma observed that middle-income classes ($50\%$ of the population between deciles 5 and 9) consistently capture approximately $50\%$ of national income across all countries; inequality is overwhelmingly driven by the structural tug-of-war between the richest $10\%$ and the bottom $40\%$.
2. **Theil’s Entropy Index ($T$)**: An information-theoretic entropy measure of inequality:
   $$T = \frac{1}{n} \sum_{i=1}^n \frac{y_i}{\bar{y}} \ln\left( \frac{y_i}{\bar{y}} \right)$$
   Theil's index decomposes perfectly into within-group inequality and between-group inequality without residual interaction terms.

## 8.6 Multidimensional Poverty Index (MPI) and the SDG 2030 Framework

Human deprivation extends far beyond income or consumption poverty. A household with cash income above the monetary poverty line may still suffer from chronic malnutrition, lack clean drinking water, live in an unpaved mud hut without electricity, and have children out of school.

### The Alkire-Foster Multidimensional Poverty Index (MPI)
Sabina Alkire and James Foster (2011) formulated the **Multidimensional Poverty Index (MPI)**, officially adopted by the United Nations Development Programme (UNDP) for global human development monitoring.

The Global MPI evaluates deprivation across three equally weighted core dimensions comprising ten indicators:
1. **Health** (weight $1/3$): Nutrition ($1/6$), Child Mortality ($1/6$).
2. **Education** (weight $1/3$): Years of Schooling ($1/6$), Child School Attendance ($1/6$).
3. **Standard of Living** (weight $1/3$): Cooking Fuel ($1/18$), Sanitation ($1/18$), Drinking Water ($1/18$), Electricity ($1/18$), Housing ($1/18$), Assets ($1/18$).

#### The Dual-Cutoff Methodology
- **Deprivation Cutoff ($z_j$)**: For each indicator $j$, an individual is defined as deprived ($I_{ij} = 1$) if their achievement falls below $z_j$ (e.g., lacking electricity, or having a malnourished child).
- **Deprivation Score ($c_i$)**: The weighted sum of deprivations suffered by individual $i$:
  $$c_i = \sum_{j=1}^d w_j I_{ij}, \qquad \sum_{j=1}^d w_j = 1.0$$
- **Poverty Cutoff ($k$)**: A person is defined as **multidimensionally poor** if their deprivation score equals or exceeds a designated threshold $k$ (globally standardized at $k = 1/3 = 33.3\%$):
  $$\text{Person } i \text{ is poor if } c_i \ge k$$

The **Adjusted Headcount Ratio ($M_0$)** is the product of two intuitive numbers:

$$M_0 = H \times A$$

where:
- $H = \frac{q}{N}$: The multidimensional headcount ratio (percentage of the population that is multidimensionally poor).
- $A = \frac{\sum_{i=1}^q c_i(k)}{q}$: The **intensity of poverty** (the average percentage of weighted indicators in which poor persons are deprived).

$M_0$ satisfies dimensional monotonicity: if a poor person becomes deprived in an additional indicator, $A$ increases, driving up $M_0$.

### The UN Sustainable Development Goals (SDG 2030) Monitoring Architecture
The Sustainable Development Goals (2015–2030) comprise 17 Goals, 169 Targets, and 231 unique Statistical Indicators. The global statistical system categorizes SDG indicators into three tiers:
- **Tier I**: Internationally established methodology exists and data are regularly produced by at least $50\%$ of countries.
- **Tier II**: Internationally established methodology exists, but data are not regularly produced by countries.
- **Tier III**: No internationally agreed methodology or standards yet exist (actively developed by custodian agencies).

National Statistical Offices serve as the official national reporting focal points, integrating administrative tax registers, civil registration and vital statistics (CRVS), geospatial satellite imagery, and high-frequency digital mobile surveys into national SDG reporting platforms.

## Fully worked question 1: Comprehensive Labor Force and Underutilization Diagnostics (LU1 to LU4)

### Question
The national statistical office of a developing nation conducts a nationwide Labor Force Survey (LFS) adhering to the ILO 19th ICLS resolution. The survey sample represents a total non-institutional Working-Age Population ($WAP$) of $80,000,000$ persons aged 15 years and older.

The survey categorizes the working-age population into the following mutually exclusive groups:
- Employed working full-time ($35+\text{ hours/week}$): $42,000,000$
- Employed working part-time who do *not* want additional hours: $6,000,000$
- Employed working part-time who want and are available to work additional hours (Time-Related Underemployed, $TRU$): $4,000,000$
- Persons without work, currently available, and actively seeking work (Unemployed, $U$): $2,400,000$
- Persons wanting work and available, but not actively seeking due to discouragement ($PLF_1$): $1,600,000$
- Persons seeking work but not immediately available within the next two weeks ($PLF_2$): $400,000$
- Full-time students, homemakers, and retirees with zero desire or availability for work ($OLF_{\text{inactive}}$): $23,600,000$

Perform the following calculations:
1. Compute the total number of Employed persons ($E$).
2. Compute the total Labor Force ($LF$) and the Labor Force Participation Rate ($LFPR$).
3. Compute the Employment-to-Population Ratio ($EPR$).
4. Compute the standard Unemployment Rate ($LU_1$).
5. Compute the Potential Labor Force ($PLF$).
6. Compute the composite labor underutilization indicators $LU_2, LU_3,$ and $LU_4$.
7. Provide a comparative policy interpretation of $LU_1$ versus $LU_4$.

### Solution, step 1: Compute total employed ($E$)
The employed population includes all persons working at least one hour for pay or profit:
$$E = E_{\text{full-time}} + E_{\text{part-time, voluntary}} + TRU = 42,000,000 + 6,000,000 + 4,000,000 = 52,000,000\text{ persons}$$

### Solution, step 2: Compute Labor Force ($LF$) and $LFPR$
The labor force comprises the employed and the unemployed:
$$LF = E + U = 52,000,000 + 2,400,000 = 54,400,000\text{ persons}$$

The Labor Force Participation Rate is:
$$LFPR = \frac{LF}{WAP} \times 100\% = \frac{54,400,000}{80,000,000} \times 100\% = 68.00\%$$

### Solution, step 3: Compute Employment-to-Population Ratio ($EPR$)
$$EPR = \frac{E}{WAP} \times 100\% = \frac{52,000,000}{80,000,000} \times 100\% = 65.00\%$$

### Solution, step 4: Compute standard Unemployment Rate ($LU_1$)
$$LU_1 = \frac{U}{LF} \times 100\% = \frac{2,400,000}{54,400,000} \times 100\% \approx 4.4118\% \approx 4.41\%$$
The headline official unemployment rate is **$4.41\%$**.

### Solution, step 5: Compute Potential Labor Force ($PLF$)
The Potential Labor Force comprises unavailable jobseekers and discouraged workers:
$$PLF = PLF_1 + PLF_2 = 1,600,000 + 400,000 = 2,000,000\text{ persons}$$
The Extended Labor Force is:
$$LF + PLF = 54,400,000 + 2,000,000 = 56,400,000\text{ persons}$$

### Solution, step 6: Compute composite underutilization rates ($LU_2, LU_3, LU_4$)
1. **$LU_2$ (Underemployment + Unemployment)**:
   $$LU_2 = \frac{U + TRU}{LF} \times 100\% = \frac{2,400,000 + 4,000,000}{54,400,000} \times 100\% = \frac{6,400,000}{54,400,000} \times 100\% \approx 11.7647\% \approx 11.76\%$$

2. **$LU_3$ (Unemployment + Potential Labor Force)**:
   $$LU_3 = \frac{U + PLF}{LF + PLF} \times 100\% = \frac{2,400,000 + 2,000,000}{56,400,000} \times 100\% = \frac{4,400,000}{56,400,000} \times 100\% \approx 7.8014\% \approx 7.80\%$$

3. **$LU_4$ (Composite Measure of Labor Underutilization)**:
   $$LU_4 = \frac{U + TRU + PLF}{LF + PLF} \times 100\% = \frac{2,400,000 + 4,000,000 + 2,000,000}{56,400,000} \times 100\% = \frac{8,400,000}{56,400,000} \times 100\% \approx 14.8936\% \approx 14.89\%$$

### Solution, step 7: Comparative policy interpretation
- The headline unemployment rate ($LU_1 = 4.41\%$) gives the superficial political impression of near-full employment.
- However, the composite labor underutilization indicator ($LU_4 = 14.89\%$) reveals that nearly **$15\%$ of the total productive human capacity** ($8.4\text{ million citizens}$) is economically sidelined or underemployed: $4.0\text{ million}$ workers are involuntarily working fewer hours than they need, and $2.0\text{ million}$ discouraged individuals have dropped out of active search.
- Reliance on $LU_1$ alone would cause finance ministries to drastically under-invest in vocational training and job creation initiatives.

## Fully worked question 2: Foster-Greer-Thorbecke Poverty Analysis and Spatial Decomposition

### Question
A regional development bank evaluates poverty dynamics across two administrative districts (District A and District B) using the Foster-Greer-Thorbecke (FGT) framework. The official national poverty line is established at $z = 3,000\text{ BDT}$ per capita per month.

The income distributions for sampled representative households (each household normalized to 1 individual) in the two districts are:
- **District A (Urban/Industrial)**: Total population $N_A = 6$. Monthly per capita incomes:
  $$y_A = [1,500, \; 2,100, \; 2,700, \; 3,500, \; 4,200, \; 6,000]$$
- **District B (Rural/Agrarian)**: Total population $N_B = 4$. Monthly per capita incomes:
  $$y_B = [900, \; 1,200, \; 1,800, \; 4,500]$$

Total regional population is $N = N_A + N_B = 10$.

Perform the following calculations:
1. For District A, identify the poor individuals and compute the normalized poverty gaps $g_i = (z - y_i)/z$.
2. Compute the FGT metrics for District A: Headcount Ratio ($P_{0, A}$), Poverty Gap Index ($P_{1, A}$), and Squared Poverty Gap ($P_{2, A}$).
3. For District B, identify the poor individuals and compute $P_{0, B}, P_{1, B},$ and $P_{2, B}$.
4. Compute the combined total regional poverty metrics $P_0, P_1,$ and $P_2$ using the FGT subgroup decomposition formula.
5. Determine the percentage contribution of District B to total regional poverty severity ($P_2$).
6. Calculate the minimum total financial transfer (in BDT) required to eliminate poverty in the combined region under perfect targeting.

### Solution, step 1: Evaluate District A
Poverty line $z = 3,000\text{ BDT}$.
In District A ($N_A = 6$), the incomes strictly below $z$ are:
- Person 1: $y_1 = 1,500 \implies g_1 = (3,000 - 1,500)/3,000 = 1,500 / 3,000 = 0.50$
- Person 2: $y_2 = 2,100 \implies g_2 = (3,000 - 2,100)/3,000 = 900 / 3,000 = 0.30$
- Person 3: $y_3 = 2,700 \implies g_3 = (3,000 - 2,700)/3,000 = 300 / 3,000 = 0.10$
- Persons 4, 5, 6 have incomes $\ge 3,000$ (not poor).

Number of poor in District A: $q_A = 3$.

Computing FGT metrics for District A:
1. **Headcount Ratio ($P_{0, A}$)**:
   $$P_{0, A} = \frac{q_A}{N_A} = \frac{3}{6} = 0.5000 = 50.0\%$$
2. **Poverty Gap Index ($P_{1, A}$)**:
   $$P_{1, A} = \frac{1}{N_A} \sum_{i=1}^{q_A} g_i = \frac{0.50 + 0.30 + 0.10}{6} = \frac{0.90}{6} = 0.1500 = 15.0\%$$
3. **Squared Poverty Gap ($P_{2, A}$)**:
   $$g_1^2 = 0.50^2 = 0.2500, \quad g_2^2 = 0.30^2 = 0.0900, \quad g_3^2 = 0.10^2 = 0.0100$$
   $$\sum g_i^2 = 0.2500 + 0.0900 + 0.0100 = 0.3500$$
   $$P_{2, A} = \frac{0.3500}{6} \approx 0.05833 = 5.833\%$$

### Solution, step 2: Evaluate District B
In District B ($N_B = 4$), incomes strictly below $z = 3,000$ are:
- Person 1: $y_1 = 900 \implies g_1 = (3,000 - 900)/3,000 = 2,100 / 3,000 = 0.70$
- Person 2: $y_2 = 1,200 \implies g_2 = (3,000 - 1,200)/3,000 = 1,800 / 3,000 = 0.60$
- Person 3: $y_3 = 1,800 \implies g_3 = (3,000 - 1,800)/3,000 = 1,200 / 3,000 = 0.40$
- Person 4: $y_4 = 4,500 \ge 3,000$ (not poor).

Number of poor in District B: $q_B = 3$.

Computing FGT metrics for District B:
1. **Headcount Ratio ($P_{0, B}$)**:
   $$P_{0, B} = \frac{q_B}{N_B} = \frac{3}{4} = 0.7500 = 75.0\%$$
2. **Poverty Gap Index ($P_{1, B}$)**:
   $$P_{1, B} = \frac{1}{N_B} \sum g_i = \frac{0.70 + 0.60 + 0.40}{4} = \frac{1.70}{4} = 0.4250 = 42.5\%$$
3. **Squared Poverty Gap ($P_{2, B}$)**:
   $$g_1^2 = 0.70^2 = 0.4900, \quad g_2^2 = 0.60^2 = 0.3600, \quad g_3^2 = 0.40^2 = 0.1600$$
   $$\sum g_i^2 = 0.4900 + 0.3600 + 0.1600 = 1.0100$$
   $$P_{2, B} = \frac{1.0100}{4} = 0.2525 = 25.25\%$$

### Solution, step 3: Subgroup decomposition for total region
Population weights:
$$w_A = \frac{N_A}{N} = \frac{6}{10} = 0.60, \qquad w_B = \frac{N_B}{N} = \frac{4}{10} = 0.40$$

Using $P_\alpha = w_A P_{\alpha, A} + w_B P_{\alpha, B}$:
1. **Total Headcount Ratio ($P_0$)**:
   $$P_0 = (0.60 \times 0.5000) + (0.40 \times 0.7500) = 0.3000 + 0.3000 = 0.6000 = 60.0\%$$
2. **Total Poverty Gap Index ($P_1$)**:
   $$P_1 = (0.60 \times 0.1500) + (0.40 \times 0.4250) = 0.0900 + 0.1700 = 0.2600 = 26.0\%$$
3. **Total Squared Poverty Gap ($P_2$)**:
   $$P_2 = (0.60 \times 0.05833) + (0.40 \times 0.2525) = 0.0350 + 0.1010 = 0.1360 = 13.60\%$$

### Solution, step 4: Spatial contribution of District B to poverty severity
The percentage contribution of District B to total regional poverty severity $P_2$ is:
$$\text{Contribution}_B = \frac{w_B P_{2, B}}{P_2} \times 100\% = \frac{0.1010}{0.1360} \times 100\% \approx 74.26\%$$
Even though District B accounts for only $40\%$ of the population, it generates **$74.26\%$ of total poverty severity** due to acute rural poverty depth!

### Solution, step 5: Minimum total financial transfer to eliminate poverty
Under perfect targeting, the minimum financial resources required to eliminate poverty equals the sum of income shortfalls:
$$\text{Total Shortfall} = P_1 \times z \times N = 0.2600 \times 3,000 \times 10 = 780 \times 10 = 7,800\text{ BDT}$$
Checking by direct summing:
- District A shortfalls: $(3,000 - 1,500) + (3,000 - 2,100) + (3,000 - 2,700) = 1,500 + 900 + 300 = 2,700\text{ BDT}$.
- District B shortfalls: $(3,000 - 900) + (3,000 - 1,200) + (3,000 - 1,800) = 2,100 + 1,800 + 1,200 = 5,100\text{ BDT}$.
- Total $= 2,700 + 5,100 = 7,800\text{ BDT}$.
A targeted lump-sum cash transfer budget of **$7,800\text{ BDT}$** is the absolute theoretical minimum required to eliminate poverty.

## Fully worked question 3: Gini Coefficient Derivation, Lorenz Curve, and Alkire-Foster MPI

### Question
An economic development research council analyzes inequality and multidimensional poverty in a developing municipal ward. 

**Part I: Inequality Analysis**
A survey of $n = 5$ households yields sorted monthly income values:
$$\mathbf{y} = [2,000, \; 4,000, \; 6,000, \; 10,000, \; 18,000]\text{ BDT}$$

1. Compute the cumulative population shares $p_i$ and cumulative income shares $L_i$.
2. Calculate the Gini Coefficient ($G$) using the relative mean difference formula.
3. Calculate the Palma Ratio.

**Part II: Multidimensional Poverty Analysis (Alkire-Foster)**
The same 5 households are evaluated across $d = 4$ equally weighted indicators ($w_j = 0.25$ each):
- Indicator 1: Nutrition (1 if malnourished, 0 if adequate)
- Indicator 2: Clean Drinking Water (1 if unimproved, 0 if clean piped)
- Indicator 3: Electricity (1 if lacking grid/solar, 0 if electrified)
- Indicator 4: School Attendance (1 if any school-aged child out of school, 0 if enrolled)

The observed binary deprivation matrix $\mathbf{I} = [I_{ij}]$ for Households 1 to 5 across Indicators 1 to 4 is:
- Household 1: $[1, 1, 1, 0]$
- Household 2: $[1, 1, 0, 0]$
- Household 3: $[1, 0, 1, 1]$
- Household 4: $[0, 0, 1, 0]$
- Household 5: $[0, 0, 0, 0]$

The multidimensional poverty cutoff is set at $k = 0.50$ (a household is poor if deprived in at least $50\%$ of weighted indicators).

4. Compute the deprivation score $c_i$ for each household.
5. Identify which households are multidimensionally poor.
6. Compute the Multidimensional Headcount Ratio ($H$), the Intensity of Poverty ($A$), and the Adjusted Headcount Ratio ($M_0$).

### Solution, step 1: Part I - Lorenz Curve coordinates
Total income:
$$\sum_{i=1}^5 y_i = 2,000 + 4,000 + 6,000 + 10,000 + 18,000 = 40,000\text{ BDT}$$
Mean income $\bar{y} = 40,000 / 5 = 8,000\text{ BDT}$.

Compute cumulative shares:
- $i=1$: $p_1 = 1/5 = 0.20$, $\quad L_1 = 2,000 / 40,000 = 0.0500$ ($5.0\%$)
- $i=2$: $p_2 = 2/5 = 0.40$, $\quad L_2 = (2,000 + 4,000)/40,000 = 6,000 / 40,000 = 0.1500$ ($15.0\%$)
- $i=3$: $p_3 = 3/5 = 0.60$, $\quad L_3 = (6,000 + 6,000)/40,000 = 12,000 / 40,000 = 0.3000$ ($30.0\%$)
- $i=4$: $p_4 = 4/5 = 0.80$, $\quad L_4 = (12,000 + 10,000)/40,000 = 22,000 / 40,000 = 0.5500$ ($55.0\%$)
- $i=5$: $p_5 = 5/5 = 1.00$, $\quad L_5 = 40,000 / 40,000 = 1.0000$ ($100.0\%$)

### Solution, step 2: Part I - Calculate the Gini Coefficient
Using the ranked sum formula:
$$G = \frac{2 \sum_{i=1}^n i \cdot y_i}{n \sum_{i=1}^n y_i} - \frac{n + 1}{n}$$
Here $n = 5$, $\sum y_i = 40,000$:
$$\sum_{i=1}^5 i \cdot y_i = 1(2,000) + 2(4,000) + 3(6,000) + 4(10,000) + 5(18,000)$$
$$= 2,000 + 8,000 + 18,000 + 40,000 + 90,000 = 158,000$$

Evaluating $G$:
$$G = \frac{2 \times 158,000}{5 \times 40,000} - \frac{5 + 1}{5} = \frac{316,000}{200,000} - \frac{6}{5} = 1.580 - 1.200 = 0.380$$
The Gini coefficient is **$0.380$** (reflecting moderate-to-high income inequality).

### Solution, step 3: Part I - Calculate the Palma Ratio
- Share of top $10\%$ (here represented by top $20\%$, Household 5):
  $$\text{Top Share} = \frac{18,000}{40,000} = 0.4500 = 45.0\%$$
- Share of bottom $40\%$ (Households 1 and 2):
  $$\text{Bottom Share} = \frac{2,000 + 4,000}{40,000} = \frac{6,000}{40,000} = 0.1500 = 15.0\%$$

The Palma Ratio is:
$$\text{Palma} = \frac{0.4500}{0.1500} = 3.00$$
The richest group captures exactly $3.0\times$ as much income as the bottom $40\%$.

### Solution, step 4: Part II - Alkire-Foster Deprivation Scores
With $w_j = 0.25$ for each of the $4$ indicators, $c_i = 0.25 \sum_{j=1}^4 I_{ij}$:
- Household 1: $[1, 1, 1, 0] \implies c_1 = 3 \times 0.25 = 0.75$ ($75\%$)
- Household 2: $[1, 1, 0, 0] \implies c_2 = 2 \times 0.25 = 0.50$ ($50\%$)
- Household 3: $[1, 0, 1, 1] \implies c_3 = 3 \times 0.25 = 0.75$ ($75\%$)
- Household 4: $[0, 0, 1, 0] \implies c_4 = 1 \times 0.25 = 0.25$ ($25\%$)
- Household 5: $[0, 0, 0, 0] \implies c_5 = 0 \times 0.25 = 0.00$ ($0\%$)

### Solution, step 5: Part II - Identification of Multidimensionally Poor
With poverty cutoff $k = 0.50$:
- Household 1: $c_1 = 0.75 \ge 0.50 \implies \mathbf{Poor}$
- Household 2: $c_2 = 0.50 \ge 0.50 \implies \mathbf{Poor}$
- Household 3: $c_3 = 0.75 \ge 0.50 \implies \mathbf{Poor}$
- Household 4: $c_4 = 0.25 < 0.50 \implies \text{Not Poor}$
- Household 5: $c_5 = 0.00 < 0.50 \implies \text{Not Poor}$

Total multidimensionally poor households: $q = 3$ (Households 1, 2, and 3).

### Solution, step 6: Part II - Compute $H, A,$ and $M_0$
1. **Multidimensional Headcount Ratio ($H$)**:
   $$H = \frac{q}{N} = \frac{3}{5} = 0.6000 = 60.0\%$$
   $60\%$ of households in the ward are multidimensionally poor.

2. **Intensity of Poverty ($A$)**:
   The average deprivation score among the poor:
   $$A = \frac{\sum_{i \in \text{Poor}} c_i}{q} = \frac{c_1 + c_2 + c_3}{3} = \frac{0.75 + 0.50 + 0.75}{3} = \frac{2.00}{3} \approx 0.6667 = 66.67\%$$
   Poor households are deprived in an average of two-thirds ($66.67\%$) of the indicators.

3. **Adjusted Headcount Ratio ($M_0$)**:
   $$M_0 = H \times A = 0.6000 \times 0.6667 = 0.4000$$
   The municipal ward’s Multidimensional Poverty Index is **$M_0 = 0.400$**.
"""

(DRAFT_DIR / "unit-7.md").write_text(unit_7.strip() + "\n", encoding="utf-8")
print("Unit 7 written.")

(DRAFT_DIR / "unit-8.md").write_text(unit_8.strip() + "\n", encoding="utf-8")
print("Unit 8 written.")
