# Unit 1: Index Numbers: Foundations, Weighted Aggregates & Construction Methods

Economic statistics provides the quantitative architecture for observing, modeling, and regulating national economic performance. At the center of applied macroeconomic measurement stands the theory of **index numbers**. Often termed the "barometers of economic activity," index numbers summarize complex multidimensional changes in prices, physical quantities, industrial production, and trade volume across time and geographical space into clean, single-dimensional scalar trajectories. Because real-world economies produce millions of heterogeneous goods and services denominated in non-additive physical units—metric tons of steel, kilowatt-hours of electrical energy, bushels of wheat, and hours of surgical labor—measuring overall inflation or economic growth requires rigorous statistical aggregation formulas that weight commodities according to their true economic importance.

## 1.1 Nature, Purpose, and Foundations of Economic Index Numbers

An index number is a specialized statistical measure designed to quantify the relative change in the magnitude of a group of related variables across time, geographic space, or economic sectors.

### The Fundamental Index Problem
Let an economy encompass $N$ distinct commodities indexed by $i = 1, 2, \dots, N$.
In base period $0$, each commodity $i$ is transacted at unit price $p_{i0}$ and traded in quantity $q_{i0}$.
In current period $t$, the same commodity is transacted at unit price $p_{it}$ and quantity $q_{it}$.
The individual price relative for commodity $i$ is:

$$R_{it} = \frac{p_{it}}{p_{i0}}$$

Because individual price relatives diverge dramatically—some prices rise rapidly due to supply bottlenecks, others remain stable, and others fall due to technological automation—we cannot simply sum prices across commodities ($p_{\text{steel}} + p_{\text{wheat}}$ is meaningless). The foundational challenge of index number theory consists in finding a continuous aggregator function $I(p_t, q_t, p_0, q_0)$ that maps the $4N$-dimensional vector of prices and quantities into a meaningful scalar price index $P_{0t}$ and quantity index $Q_{0t}$.

### Key Economic Applications of Index Numbers
1. **Inflation Monitoring and Monetary Policy**: Central banks (such as the Federal Reserve, the European Central Bank, and Bangladesh Bank) monitor the Consumer Price Index (CPI) and Personal Consumption Expenditures (PCE) deflator to calibrate interest rate decisions, inflation-targeting mandates, and quantitative easing operations.
2. **Real Wage Indexation and Cost-of-Living Adjustments (COLA)**: Labor unions, public service pay commissions, and social security administrations index nominal wages, pensions, and minimum wage thresholds to price indices to protect workers' purchasing power from inflationary erosion.
3. **National Accounts Deflation**: Macroeconometricians divide nominal Gross Domestic Product (GDP) by the GDP deflator to isolate real physical output growth from pure monetary inflation.
4. **Terms of Trade (ToT) in International Commerce**: The net barter terms of trade, defined as the ratio of the export price index to the import price index ($P_X / P_M \times 100$), determines whether a sovereign nation's international purchasing power is appreciating or deteriorating.

## 1.2 Base Period Selection, Fixed-Base vs Chain-Base Systems, and Splicing

The numerical value of any index number depends fundamentally on the benchmark against which comparisons are executed: the **Base Period**.

### Criteria for Selecting a Valid Base Period
1. **Economic Normalcy**: The base period must be an economically normal year, free from severe macroeconomic dislocations, hyperinflation, wartime devastation, harvest failures, or global pandemics. Choosing an abnormal crisis year creates a distorted benchmark that skews subsequent comparisons.
2. **Temporal Proximity**: The base period should not be too distant in the past. Over time, consumer preferences evolve, new electronic products emerge, and older products become obsolete. If a base year is thirty years old, its fixed commodity basket no longer reflects modern consumption patterns.

### Fixed-Base vs Chain-Base Systems
In economic statistics, temporal comparisons are structured according to two distinct operational architectures:

1. **Fixed-Base Index System**:
   A single, designated historical period $0$ serves as the permanent denominator for all subsequent periods $t$:
   $$P_{01} = \frac{p_1}{p_0}, \quad P_{02} = \frac{p_2}{p_0}, \quad \dots, \quad P_{0t} = \frac{p_t}{p_0}$$
   - *Advantages*: Computationally straightforward and simple to explain to the public; comparisons between any two adjacent years are consistent with a fixed reference basket.
   - *Disadvantages*: As the baseline recedes into the past, new goods cannot be easily incorporated, and structural shifts in consumer spending are ignored.

2. **Chain-Base Index System**:
   The base period shifts continuously, with each period compared directly to its immediately preceding period, generating a sequence of **link relatives**:
   $$P_{0, 1} = \frac{p_1}{p_0}, \quad P_{1, 2} = \frac{p_2}{p_1}, \quad \dots, \quad P_{t-1, t} = \frac{p_t}{p_{t-1}}$$
   The cumulative chain index relative to the initial origin is obtained by successive multiplication (chaining) of the link relatives:
   $$P_{0t}^{\text{chain}} = P_{0, 1} \times P_{1, 2} \times P_{2, 3} \times \dots \times P_{t-1, t}$$
   - *Advantages*: Highly flexible; new technological commodities can be added and obsolete goods retired each year, and quantity weights reflect contemporary spending patterns.
   - *Disadvantages*: If prices oscillate cyclically without a secular trend, chain indices can suffer from **chain drift** (where the chained index fails to return to unity after prices and quantities return to their starting values).

### Shifting and Splicing of Index Series
When a statistical agency updates its fixed base year (e.g., rebasing a Consumer Price Index from 2010 = 100 to 2020 = 100), it creates two disjoint, non-comparable historical series: the old series terminating in 2020 and the new series beginning in 2020.
To establish a continuous, unbroken longitudinal historical series, demographers and econometricians perform **splicing**.

Let $P_{0t}^{\text{old}}$ denote the old series with base year $0$, and let $P_{1t}^{\text{new}}$ denote the new series with base year $1$. At the overlapping splicing year $k$, both indices are recorded: $P_{0k}^{\text{old}}$ and $P_{1k}^{\text{new}} = 100$.
To splice the old series onto the new base (converting historical pre-$k$ values into new-base equivalents):

$$P_{1t}^{\text{spliced}} = P_{0t}^{\text{old}} \times \left( \frac{100}{P_{0k}^{\text{old}}} \right) \quad \text{for } t < k$$

Conversely, to splice the new series onto the old base:

$$P_{0t}^{\text{spliced}} = P_{1t}^{\text{new}} \times \left( \frac{P_{0k}^{\text{old}}}{100} \right) \quad \text{for } t > k$$

This linear scaling factor ensures seamless mathematical continuity across the base-year transition.

## 1.3 Simple (Unweighted) Index Numbers and Their Mathematical Flaws

The earliest historical index formulations aggregated prices without incorporating commodity quantities or expenditure shares.

### 1. Simple Aggregative Price Index
The ratio of the unweighted sum of commodity prices in the current period to the unweighted sum in the base period:

$$P_{0t}^{\text{SA}} = \frac{\sum_{i=1}^N p_{it}}{\sum_{i=1}^N p_{i0}} \times 100$$

**Fatal Mathematical Flaw (The Unit Dependence Problem)**:
The simple aggregative index is extraordinarily sensitive to the arbitrary physical units in which prices are quoted. If the price of gold is quoted per metric ton instead of per gram, its numerical magnitude will completely dominate the sum, rendering price changes in all other commodities mathematically irrelevant. The simple aggregative index violates the fundamental Unit Test of index number theory.

### 2. Simple Average of Price Relatives
To eliminate unit dependence, one can compute individual dimensionless price relatives $R_i = p_{it} / p_{i0}$ and average them:
- **Arithmetic Mean of Relatives**:
  $$P_{0t}^{\text{AM}} = \frac{1}{N} \sum_{i=1}^N \left( \frac{p_{it}}{p_{i0}} \right) \times 100$$
- **Geometric Mean of Relatives (Jevons Index, 1865)**:
  $$P_{0t}^{\text{GM}} = \left( \prod_{i=1}^N \frac{p_{it}}{p_{i0}} \right)^{1/N} \times 100 = \exp\left( \frac{1}{N} \sum_{i=1}^N \ln\left( \frac{p_{it}}{p_{i0}} \right) \right) \times 100$$
- **Harmonic Mean of Relatives (Coggeshall Index, 1887)**:
  $$P_{0t}^{\text{HM}} = \frac{N}{\sum_{i=1}^N \left( \frac{p_{i0}}{p_{it}} \right)} \times 100$$

While the Jevons geometric index eliminates unit dependence and satisfies the time-reversal property, all unweighted averages suffer from a crippling economic defect: **they treat every commodity as equally important**. A hundred-percent price increase in table salt (which accounts for $0.05\%$ of household expenditure) exerts the identical statistical impact as a hundred-percent increase in residential rent (which accounts for $35\%$ of expenditure). To reflect true cost-of-living impacts, commodities must be weighted by their economic expenditure.

## 1.4 Weighted Aggregative Price Index Numbers: Laspeyres, Paasche, and Fisher

In modern economic statistics, weighted aggregative index numbers weight each commodity price by physical quantities transacted in either the base period, the current period, or a composite combination.

### 1. The Laspeyres Price Index (Étienne Laspeyres, 1871)
The **Laspeyres Price Index** ($P_L$) weights prices by the **base-period quantities** ($q_{i0}$):

$$P_L = \frac{\sum_{i=1}^N p_{it} q_{i0}}{\sum_{i=1}^N p_{i0} q_{i0}} \times 100$$

The numerator represents the cost of purchasing the original base-period consumption basket at contemporary current-period prices. The denominator represents the actual expenditure incurred to purchase that same basket in the base period.

#### Expression as a Weighted Average of Relatives:
Multiply and divide each term in the numerator by $p_{i0}$:

$$P_L = \frac{\sum \left( \frac{p_{it}}{p_{i0}} \right) p_{i0} q_{i0}}{\sum p_{i0} q_{i0}} = \sum_{i=1}^N \left( \frac{p_{it}}{p_{i0}} \right) w_{i0}$$

where $w_{i0} = \frac{p_{i0} q_{i0}}{\sum p_{i0} q_{i0}}$ represents the **base-period expenditure share** of commodity $i$, satisfying $\sum w_{i0} = 1$.
Thus, the Laspeyres index is mathematically equivalent to the arithmetic mean of price relatives weighted by base-period budget shares.

#### The Laspeyres Upward Substitution Bias:
Microeconomic consumer theory proves that when prices rise unevenly, rational consumers do not consume a rigid, fixed physical basket; instead, they substitute away from commodities whose relative prices have escalated toward goods that have become relatively cheaper. Because the Laspeyres index assumes a completely frozen physical basket ($q_{i0}$), it completely ignores consumer substitution. Consequently, the Laspeyres index **systematically overstates the true cost-of-living inflation** experienced by households.

### 2. The Paasche Price Index (Hermann Paasche, 1874)
The **Paasche Price Index** ($P_P$) weights prices by the **current-period quantities** ($q_{it}$):

$$P_P = \frac{\sum_{i=1}^N p_{it} q_{it}}{\sum_{i=1}^N p_{i0} q_{it}} \times 100$$

The numerator represents the actual contemporary expenditure incurred in period $t$. The denominator represents what that exact same contemporary basket would have cost if purchased at base-period prices.

#### Expression as a Weighted Harmonic Mean of Relatives:
The Paasche index is mathematically equivalent to the **harmonic mean of price relatives weighted by current-period expenditure shares**:

$$P_P = \frac{\sum p_{it} q_{it}}{\sum \left( \frac{p_{i0}}{p_{it}} \right) p_{it} q_{it}} = \frac{1}{\sum_{i=1}^N \left( \frac{p_{i0}}{p_{it}} \right) w_{it}}$$

where $w_{it} = \frac{p_{it} q_{it}}{\sum p_{it} q_{it}}$.

#### The Paasche Downward Substitution Bias:
Because the current basket $q_{it}$ reflects consumer substitution toward cheaper alternatives, evaluating that basket at base prices ($p_{i0}$) overstates base-period expenditure. Consequently, the Paasche index **systematically understates true cost-of-living inflation**.

In almost all empirical economies, the fundamental Laspeyres-Paasche inequality holds:

$$P_P \le P_L$$

### 3. Fisher's Ideal Index (Irving Fisher, 1922)
Recognizing that Laspeyres overstates inflation while Paasche understates it, the Yale economist Irving Fisher proposed the geometric mean of the two indices as the **Fisher Ideal Index** ($P_F$):

$$P_F = \sqrt{P_L \times P_P} = \sqrt{ \left( \frac{\sum p_{it} q_{i0}}{\sum p_{i0} q_{i0}} \right) \times \left( \frac{\sum p_{it} q_{it}}{\sum p_{i0} q_{it}} \right) } \times 100$$

Fisher designated this formula "ideal" because, as proven in Unit 2, it satisfies both the Time Reversal Test and the Factor Reversal Test—a rigorous mathematical achievement that neither Laspeyres nor Paasche can attain.

## 1.5 Alternative Weighted Aggregative Formulations

In addition to Laspeyres, Paasche, and Fisher, economic statisticians developed several compromise formulas designed to balance base-period and current-period baskets without requiring geometric square roots.

### 1. The Marshall–Edgeworth Index (Alfred Marshall, 1887; Francis Y. Edgeworth, 1925)
The Marshall–Edgeworth index ($P_{ME}$) weights prices by the **arithmetic average of base-period and current-period quantities**:

$$q_{i}^{ME} = \frac{q_{i0} + q_{it}}{2}$$

$$P_{ME} = \frac{\sum p_{it} \left( \frac{q_{i0} + q_{it}}{2} \right)}{\sum p_{i0} \left( \frac{q_{i0} + q_{it}}{2} \right)} \times 100 = \frac{\sum p_{it} q_{i0} + \sum p_{it} q_{it}}{\sum p_{i0} q_{i0} + \sum p_{i0} q_{it}} \times 100$$

The Marshall–Edgeworth index provides an exceptional numerical approximation to Fisher's Ideal Index without requiring non-linear root evaluations. Furthermore, it satisfies the Time Reversal Test.

### 2. The Dorbish–Bowley Index (F. L. Dorbish, 1899; Arthur L. Bowley, 1901)
The Dorbish–Bowley index ($P_{DB}$) is the **arithmetic mean of the Laspeyres and Paasche indices**:

$$P_{DB} = \frac{P_L + P_P}{2}$$

Because the arithmetic mean of two positive numbers always exceeds or equals their geometric mean ($AM \ge GM$), the Dorbish–Bowley index is always slightly larger than Fisher's Ideal Index:

$$P_{DB} \ge P_F$$

### 3. The Walsh Price Index (Correa Moylan Walsh, 1901)
The Walsh index ($P_W$) weights prices by the **geometric mean of base and current quantities**:

$$q_i^W = \sqrt{q_{i0} \cdot q_{it}}$$

$$P_W = \frac{\sum p_{it} \sqrt{q_{i0} q_{it}}}{\sum p_{i0} \sqrt{q_{i0} q_{it}}} \times 100$$

The Walsh index belongs to the class of **superlative index numbers** (in the sense of Erwin Diewert), providing an exact second-order Taylor approximation to arbitrary consumer expenditure functions.


### The Economic Theory of Index Numbers: Konüs True Cost-of-Living Index
While mathematical statisticians approach index numbers through axiomatic properties and aggregative formulas, economic theorists ground index numbers in microeconomic consumer optimization. In 1924, the Russian mathematical economist Alexander A. Konüs formulated the **True Cost-of-Living Index (COLI)**.

Let u = U(q) represent a consumer's continuous, quasi-concave utility function over consumption bundles q.
The minimum expenditure required to attain utility level u at price vector p is given by the consumer's **Expenditure Function** (or cost function):

$$E(p, u) = \min_{q} \{ p^T q : U(q) \ge u \}$$

Konüs defined the True Cost-of-Living Index as the ratio of minimum expenditures required to attain a specified base reference utility level u_0 under current prices p_t versus base prices p_0:

$$P_K(p_t, p_0; u_0) = rac{E(p_t, u_0)}{E(p_0, u_0)}$$

#### The Fundamental Konüs Bounds:
Konüs established that the observable Laspeyres and Paasche index numbers provide rigorous upper and lower empirical bounds for the unobservable true cost of living:
1. **The Laspeyres Upper Bound**:
   Because the base-period bundle q_0 was chosen by the consumer under base prices p_0, it achieves utility U(q_0) = u_0. At current prices p_t, the consumer could choose to purchase the same bundle q_0, incurring cost p_t^T q_0. However, by substituting away from relatively expensive goods, the consumer can attain utility u_0 at a cost strictly less than or equal to p_t^T q_0:
   $$E(p_t, u_0) \le p_t^T q_0$$
   Dividing both sides by base expenditure E(p_0, u_0) = p_0^T q_0 yields the celebrated **Konüs Theorem**:
   $$P_K(p_t, p_0; u_0) \le rac{p_t^T q_0}{p_0^T q_0} = P_L$$
   The Laspeyres index is a strict mathematical upper bound to the true cost-of-living index!
2. **The Paasche Lower Bound**:
   Similarly, evaluating the true cost of living relative to current-period utility u_t yields:
   $$P_K(p_t, p_0; u_t) \ge rac{p_t^T q_t}{p_0^T q_t} = P_P$$
   The Paasche index is a strict mathematical lower bound!

Combining the two bounds establishes that the true economic cost-of-living index is bounded between Paasche and Laspeyres:
$$P_P \le P_K \le P_L$$
Because Fisher's Ideal Index P_F is the geometric mean of Laspeyres and Paasche, it falls squarely inside this theoretical band, serving as an exceptional empirical approximation to the true cost of living.

### Superlative Index Numbers and Diewert's Exact Quadratic Approximation
In 1976, W. Erwin Diewert revolutionized index number theory by formulating the concept of **Superlative Index Numbers**. An index number formula is defined as superlative if it is exact for a flexible consumer expenditure function—a function capable of providing a second-order Taylor series approximation to an arbitrary, twice-continuously differentiable utility function.

Diewert established two foundational theorems:
1. **The Fisher Ideal Index is Superlative**: Fisher's index P_F is exact for the flexible quadratic mean-of-order-r expenditure function when r = 2.
2. **The Törnqvist Index is Superlative (Leo Törnqvist, 1936)**:
   The Törnqvist index P_T weights logarithmic price changes by the arithmetic mean of base-period and current-period expenditure shares:
   $$\ln P_T = \sum_{i=1}^N rac{w_{i0} + w_{it}}{2} \ln\left( rac{p_{it}}{p_{i0}} 
ight)$$
   $$P_T = \prod_{i=1}^N \left( rac{p_{it}}{p_{i0}} 
ight)^{rac{w_{i0} + w_{it}}{2}}$$
   Diewert proved that the Törnqvist index is exact for the transcendental logarithmic (translog) expenditure function.

Because both Fisher and Törnqvist indices allow consumer expenditure weights to adapt smoothly to price changes, they virtually eliminate the substitution bias that plagues the fixed-basket Laspeyres Consumer Price Index.

### Hedonic Quality Adjustment and Scanner Data Innovations
In modern digital economies, goods undergo rapid technological improvement: a modern personal computer or smartphone may cost the same nominal price as a model sold five years ago, but it features ten times the processing speed, memory, and photographic resolution. If statistical agencies simply record the nominal price, they drastically overstate true inflation because they ignore the colossal expansion in product quality.

To resolve this challenge, Zvi Griliches (1961, 1971) formalized **Hedonic Price Regression**:

$$\ln p_i = eta_0 + \sum_{k=1}^K eta_k z_{ik} + arepsilon_i$$

where z_{ik} denotes the k-th physical characteristic of good i (e.g., processor speed, RAM, screen resolution, vehicle horsepower). The regression coefficient beta_k represents the marginal implicit shadow price of characteristic k. Statistical agencies use hedonic regressions to decompose observed price changes into a pure quality change component and a residual pure inflation component, ensuring that consumer price indices track true utility costs rather than technological upgrading.


### The Economic Theory of Index Numbers: Konüs True Cost-of-Living Index
While mathematical statisticians approach index numbers through axiomatic properties and aggregative formulas, economic theorists ground index numbers in microeconomic consumer optimization. In 1924, the Russian mathematical economist Alexander A. Konüs formulated the **True Cost-of-Living Index (COLI)**.

Let u = U(q) represent a consumer's continuous, quasi-concave utility function over consumption bundles q.
The minimum expenditure required to attain utility level u at price vector p is given by the consumer's **Expenditure Function** (or cost function):

$$E(p, u) = \min_{q} \{ p^T q : U(q) \ge u \}$$

Konüs defined the True Cost-of-Living Index as the ratio of minimum expenditures required to attain a specified base reference utility level u_0 under current prices p_t versus base prices p_0:

$$P_K(p_t, p_0; u_0) = rac{E(p_t, u_0)}{E(p_0, u_0)}$$

#### The Fundamental Konüs Bounds:
Konüs established that the observable Laspeyres and Paasche index numbers provide rigorous upper and lower empirical bounds for the unobservable true cost of living:
1. **The Laspeyres Upper Bound**:
   Because the base-period bundle q_0 was chosen by the consumer under base prices p_0, it achieves utility U(q_0) = u_0. At current prices p_t, the consumer could choose to purchase the same bundle q_0, incurring cost p_t^T q_0. However, by substituting away from relatively expensive goods, the consumer can attain utility u_0 at a cost strictly less than or equal to p_t^T q_0:
   $$E(p_t, u_0) \le p_t^T q_0$$
   Dividing both sides by base expenditure E(p_0, u_0) = p_0^T q_0 yields the celebrated **Konüs Theorem**:
   $$P_K(p_t, p_0; u_0) \le rac{p_t^T q_0}{p_0^T q_0} = P_L$$
   The Laspeyres index is a strict mathematical upper bound to the true cost-of-living index!
2. **The Paasche Lower Bound**:
   Similarly, evaluating the true cost of living relative to current-period utility u_t yields:
   $$P_K(p_t, p_0; u_t) \ge rac{p_t^T q_t}{p_0^T q_t} = P_P$$
   The Paasche index is a strict mathematical lower bound!

Combining the two bounds establishes that the true economic cost-of-living index is bounded between Paasche and Laspeyres:
$$P_P \le P_K \le P_L$$
Because Fisher's Ideal Index P_F is the geometric mean of Laspeyres and Paasche, it falls squarely inside this theoretical band, serving as an exceptional empirical approximation to the true cost of living.

### Superlative Index Numbers and Diewert's Exact Quadratic Approximation
In 1976, W. Erwin Diewert revolutionized index number theory by formulating the concept of **Superlative Index Numbers**. An index number formula is defined as superlative if it is exact for a flexible consumer expenditure function—a function capable of providing a second-order Taylor series approximation to an arbitrary, twice-continuously differentiable utility function.

Diewert established two foundational theorems:
1. **The Fisher Ideal Index is Superlative**: Fisher's index P_F is exact for the flexible quadratic mean-of-order-r expenditure function when r = 2.
2. **The Törnqvist Index is Superlative (Leo Törnqvist, 1936)**:
   The Törnqvist index P_T weights logarithmic price changes by the arithmetic mean of base-period and current-period expenditure shares:
   $$\ln P_T = \sum_{i=1}^N rac{w_{i0} + w_{it}}{2} \ln\left( rac{p_{it}}{p_{i0}} 
ight)$$
   $$P_T = \prod_{i=1}^N \left( rac{p_{it}}{p_{i0}} 
ight)^{rac{w_{i0} + w_{it}}{2}}$$
   Diewert proved that the Törnqvist index is exact for the transcendental logarithmic (translog) expenditure function.

Because both Fisher and Törnqvist indices allow consumer expenditure weights to adapt smoothly to price changes, they virtually eliminate the substitution bias that plagues the fixed-basket Laspeyres Consumer Price Index.

### Hedonic Quality Adjustment and Scanner Data Innovations
In modern digital economies, goods undergo rapid technological improvement: a modern personal computer or smartphone may cost the same nominal price as a model sold five years ago, but it features ten times the processing speed, memory, and photographic resolution. If statistical agencies simply record the nominal price, they drastically overstate true inflation because they ignore the colossal expansion in product quality.

To resolve this challenge, Zvi Griliches (1961, 1971) formalized **Hedonic Price Regression**:

$$\ln p_i = eta_0 + \sum_{k=1}^K eta_k z_{ik} + arepsilon_i$$

where z_{ik} denotes the k-th physical characteristic of good i (e.g., processor speed, RAM, screen resolution, vehicle horsepower). The regression coefficient beta_k represents the marginal implicit shadow price of characteristic k. Statistical agencies use hedonic regressions to decompose observed price changes into a pure quality change component and a residual pure inflation component, ensuring that consumer price indices track true utility costs rather than technological upgrading.

## Fully worked question 1: Comprehensive Computation of Weighted Aggregative Price Indices

### Question
A national statistical office tracks retail price inflation across four core consumer commodity groups: Food ($A$), Housing/Energy ($B$), Clothing ($C$), and Transport ($D$). The observed retail prices (in currency units per physical unit) and consumption quantities across the base year ($0$) and current year ($t$) are recorded below:

| Commodity | Base Price ($p_0$) | Base Quantity ($q_0$) | Current Price ($p_t$) | Current Quantity ($q_t$) |
| :---: | :---: | :---: | :---: | :---: |
| **A (Food)** | $20.00$ | $100$ | $25.00$ | $120$ |
| **B (Energy)** | $50.00$ | $40$ | $60.00$ | $35$ |
| **C (Clothing)** | $40.00$ | $25$ | $44.00$ | $30$ |
| **D (Transport)** | $10.00$ | $80$ | $15.00$ | $70$ |

1. Calculate the four fundamental expenditure cross-products: $\sum p_0 q_0, \sum p_t q_0, \sum p_0 q_t,$ and $\sum p_t q_t$.
2. Calculate the Laspeyres Price Index ($P_L$) and Paasche Price Index ($P_P$). Verify the classical inequality $P_P \le P_L$.
3. Compute Fisher's Ideal Price Index ($P_F$), the Marshall–Edgeworth Price Index ($P_{ME}$), and the Dorbish–Bowley Price Index ($P_{DB}$). Compare the numerical results.

### Solution, step 1: Calculate Expenditure Cross-Products
We evaluate the four products commodity by commodity:
1. **Base-Period Expenditure ($\sum p_0 q_0$)**:
   - $A$: $20.00 \times 100 = 2{,}000.00$
   - $B$: $50.00 \times 40 = 2{,}000.00$
   - $C$: $40.00 \times 25 = 1{,}000.00$
   - $D$: $10.00 \times 80 = 800.00$
   $$\sum p_0 q_0 = 2{,}000 + 2{,}000 + 1{,}000 + 800 = 5{,}800.00$$

2. **Cost of Base Basket at Current Prices ($\sum p_t q_0$)**:
   - $A$: $25.00 \times 100 = 2{,}500.00$
   - $B$: $60.00 \times 40 = 2{,}400.00$
   - $C$: $44.00 \times 25 = 1{,}100.00$
   - $D$: $15.00 \times 80 = 1{,}200.00$
   $$\sum p_t q_0 = 2{,}500 + 2{,}400 + 1{,}100 + 1{,}200 = 7{,}200.00$$

3. **Cost of Current Basket at Base Prices ($\sum p_0 q_t$)**:
   - $A$: $20.00 \times 120 = 2{,}400.00$
   - $B$: $50.00 \times 35 = 1{,}750.00$
   - $C$: $40.00 \times 30 = 1{,}200.00$
   - $D$: $10.00 \times 70 = 700.00$
   $$\sum p_0 q_t = 2{,}400 + 1{,}750 + 1{,}200 + 700 = 6{,}050.00$$

4. **Current-Period Actual Expenditure ($\sum p_t q_t$)**:
   - $A$: $25.00 \times 120 = 3{,}000.00$
   - $B$: $60.00 \times 35 = 2{,}100.00$
   - $C$: $44.00 \times 30 = 1{,}320.00$
   - $D$: $15.00 \times 70 = 1{,}050.00$
   $$\sum p_t q_t = 3{,}000 + 2{,}100 + 1{,}320 + 1{,}050 = 7{,}470.00$$

### Solution, step 2: Compute Laspeyres and Paasche Indices
1. **Laspeyres Price Index ($P_L$)**:
   $$P_L = \frac{\sum p_t q_0}{\sum p_0 q_0} \times 100 = \frac{7{,}200.00}{5{,}800.00} \times 100 \approx 1.241379 \times 100 = 124.14$$
   The Laspeyres index indicates inflation of $24.14\%$.

2. **Paasche Price Index ($P_P$)**:
   $$P_P = \frac{\sum p_t q_t}{\sum p_0 q_t} \times 100 = \frac{7{,}470.00}{6{,}050.00} \times 100 \approx 1.234711 \times 100 = 123.47$$
   The Paasche index indicates inflation of $23.47\%$.

**Inequality Verification**:
$$P_P (123.47) \le P_L (124.14)$$
The classical inequality holds. The Laspeyres index exceeds the Paasche index by $0.67$ percentage points due to upward substitution bias.

### Solution, step 3: Compute Fisher, Marshall–Edgeworth, and Dorbish–Bowley
1. **Fisher's Ideal Index ($P_F$)**:
   $$P_F = \sqrt{P_L \times P_P} = \sqrt{124.1379 \times 123.4711} = \sqrt{15327.44} \approx 123.8040 \implies 123.80$$

2. **Marshall–Edgeworth Index ($P_{ME}$)**:
   $$P_{ME} = \frac{\sum p_t q_0 + \sum p_t q_t}{\sum p_0 q_0 + \sum p_0 q_t} \times 100 = \frac{7{,}200.00 + 7{,}470.00}{5{,}800.00 + 6{,}050.00} \times 100 = \frac{14{,}670.00}{11{,}850.00} \times 100 \approx 1.237975 \times 100 = 123.80$$
   Notice that $P_{ME}$ matches $P_F$ to within two decimal places ($123.80$ vs $123.80$)!

3. **Dorbish–Bowley Index ($P_{DB}$)**:
   $$P_{DB} = \frac{P_L + P_P}{2} = \frac{124.1379 + 123.4711}{2} = \frac{247.6090}{2} = 123.8045 \implies 123.80$$

Notice the exact ordering:
$$P_F (123.8040) \le P_{DB} (123.8045)$$
The arithmetic mean $P_{DB}$ slightly exceeds the geometric mean $P_F$, verifying the fundamental $AM \ge GM$ inequality.

## Fully worked question 2: Splicing Overlapping Price Index Series

### Question
A Ministry of Planning and Economic Development updates its national Consumer Price Index series, shifting the base year from 2010 ($2010 = 100$) to 2020 ($2020 = 100$). The recorded index numbers across the transition decade are given below:

| Year | Old Series ($2010 = 100$) | New Series ($2020 = 100$) |
| :---: | :---: | :---: |
| **2016** | $145.0$ | — |
| **2017** | $152.0$ | — |
| **2018** | $160.0$ | — |
| **2019** | $168.0$ | — |
| **2020** | $180.0$ | $100.0$ |
| **2021** | — | $106.0$ |
| **2022** | — | $114.0$ |
| **2023** | — | $122.0$ |
| **2024** | — | $130.0$ |

1. Splice the Old Series onto the New Base ($2020 = 100$) to obtain a backward-spliced continuous index from 2016 to 2024.
2. Splice the New Series onto the Old Base ($2010 = 100$) to obtain a forward-spliced continuous index from 2016 to 2024.
3. Compute the overall cumulative inflation rate between 2016 and 2024 using both spliced series and verify that both spliced systems yield identical economic growth rates.

### Solution, step 1: Splice Old Series onto New Base ($2020 = 100$)
At the overlapping splicing year 2020:
- Old series value: $P_{2010, 2020} = 180.0$
- New series value: $P_{2020, 2020} = 100.0$

The backward conversion factor is:

$$k_{\text{backward}} = \frac{100.0}{180.0} = \frac{1}{1.80} = 0.5555556$$

We multiply each historical value of the Old Series by $k_{\text{backward}}$:
- **Year 2016**: $145.0 \times \frac{100}{180} = 145.0 \times 0.5555556 \approx 80.56$
- **Year 2017**: $152.0 \times \frac{100}{180} = 152.0 \times 0.5555556 \approx 84.44$
- **Year 2018**: $160.0 \times \frac{100}{180} = 160.0 \times 0.5555556 \approx 88.89$
- **Year 2019**: $168.0 \times \frac{100}{180} = 168.0 \times 0.5555556 \approx 93.33$
- **Year 2020**: $180.0 \times \frac{100}{180} = 100.00$

The complete continuous series on the **New Base ($2020 = 100$)** is:
- 2016: $80.56$
- 2017: $84.44$
- 2018: $88.89$
- 2019: $93.33$
- 2020: $100.00$
- 2021: $106.00$
- 2022: $114.00$
- 2023: $122.00$
- 2024: $130.00$

### Solution, step 2: Splice New Series onto Old Base ($2010 = 100$)
The forward conversion factor is:

$$k_{\text{forward}} = \frac{180.0}{100.0} = 1.800$$

We multiply each value of the New Series by $k_{\text{forward}}$:
- **Year 2020**: $100.0 \times 1.80 = 180.00$
- **Year 2021**: $106.0 \times 1.80 = 190.80$
- **Year 2022**: $114.0 \times 1.80 = 205.20$
- **Year 2023**: $122.0 \times 1.80 = 219.60$
- **Year 2024**: $130.0 \times 1.80 = 234.00$

The complete continuous series on the **Old Base ($2010 = 100$)** is:
- 2016: $145.00$
- 2017: $152.00$
- 2018: $160.00$
- 2019: $168.00$
- 2020: $180.00$
- 2021: $190.80$
- 2022: $205.20$
- 2023: $219.60$
- 2024: $234.00$

### Solution, step 3: Compute Cumulative Inflation and Verify Equivalence
We calculate the percentage increase in the price level between 2016 and 2024:

1. **Using the New-Base Spliced Series ($2020 = 100$)**:
   $$\Delta P_{\text{new}} = \left( \frac{P_{2024}}{P_{2016}} - 1 \right) \times 100 = \left( \frac{130.00}{80.55556} - 1 \right) \times 100 = (1.613793 - 1) \times 100 = 61.38\%$$

2. **Using the Old-Base Spliced Series ($2010 = 100$)**:
   $$\Delta P_{\text{old}} = \left( \frac{P_{2024}}{P_{2016}} - 1 \right) \times 100 = \left( \frac{234.00}{145.00} - 1 \right) \times 100 = (1.613793 - 1) \times 100 = 61.38\%$$

Both spliced series yield the **identical cumulative price inflation of $61.38\%$** over the eight-year period, proving that linear splicing strictly preserves the underlying economic rate of price expansion.

## Fully worked question 3: Chain-Base Index Number Construction and Chain Drift Analysis

### Question
An economic research foundation evaluates the retail prices of a volatile seasonal fruit basket across five consecutive quarters:

| Quarter | Price ($p_t$) | Quantity ($q_t$) |
| :---: | :---: | :---: |
| **Q1 (Spring)** | $10.00$ | $100$ |
| **Q2 (Summer)** | $15.00$ | $80$ |
| **Q3 (Autumn)** | $12.00$ | $90$ |
| **Q4 (Winter)** | $20.00$ | $60$ |
| **Q5 (Spring Revisit)** | $10.00$ | $100$ |

1. Calculate the Fixed-Base Price Index ($P_{1t}^{\text{fixed}}$) taking Quarter 1 as the fixed base ($Q1 = 100$).
2. Compute the quarterly Link Relatives ($L_t = \frac{p_t}{p_{t-1}} \times 100$) and construct the Chain-Base Price Index ($P_{1t}^{\text{chain}}$).
3. Evaluate the price index at Quarter 5 where prices returned to their starting value ($p_5 = p_1 = 10.00$). Analyze whether chain drift occurred.

### Solution, step 1: Fixed-Base Price Index
The fixed base is Quarter 1 ($p_1 = 10.00$):
The formula is $P_{1t}^{\text{fixed}} = \frac{p_t}{p_1} \times 100 = \frac{p_t}{10.00} \times 100$:
- **Q1**: $\frac{10.00}{10.00} \times 100 = 100.00$
- **Q2**: $\frac{15.00}{10.00} \times 100 = 150.00$
- **Q3**: $\frac{12.00}{10.00} \times 100 = 120.00$
- **Q4**: $\frac{20.00}{10.00} \times 100 = 200.00$
- **Q5**: $\frac{10.00}{10.00} \times 100 = 100.00$

At Quarter 5, the fixed-base index returns to exactly $100.00$.

### Solution, step 2: Compute Link Relatives and Chain Index
The Link Relative is the percentage ratio of current price to preceding price:

$$L_t = \frac{p_t}{p_{t-1}} \times 100$$

1. **Q1**: Baseline = $100.00$
2. **Q2**: $L_2 = \frac{15.00}{10.00} \times 100 = 150.00$
3. **Q3**: $L_3 = \frac{12.00}{15.00} \times 100 = 80.00$
4. **Q4**: $L_4 = \frac{20.00}{12.00} \times 100 = 166.6667$
5. **Q5**: $L_5 = \frac{10.00}{20.00} \times 100 = 50.00$

Now construct the Chain-Base Index:

$$P_{1t}^{\text{chain}} = \frac{P_{1, t-1}^{\text{chain}} \times L_t}{100}$$

- **Q1**: $P_1^{\text{chain}} = 100.00$
- **Q2**: $P_2^{\text{chain}} = \frac{100.00 \times 150.00}{100} = 150.00$
- **Q3**: $P_3^{\text{chain}} = \frac{150.00 \times 80.00}{100} = 120.00$
- **Q4**: $P_4^{\text{chain}} = \frac{120.00 \times 166.6667}{100} = 200.00$
- **Q5**: $P_5^{\text{chain}} = \frac{200.00 \times 50.00}{100} = 100.00$

### Solution, step 3: Chain Drift Evaluation
In this single-commodity price relative case, the chained product is:

$$P_{15}^{\text{chain}} = \frac{p_2}{p_1} \times \frac{p_3}{p_2} \times \frac{p_4}{p_3} \times \frac{p_5}{p_4} \times 100 = \frac{p_5}{p_1} \times 100 = \frac{10.00}{10.00} \times 100 = 100.00$$

Because the intermediate prices cancel out telescopically, no chain drift occurs in the single-good setting.
However, in multi-commodity weighted aggregative systems (such as a chained Laspeyres index), changing quantity weights from quarter to quarter prevent exact telescopic cancellation. If consumers buy large quantities when goods are discounted and small quantities when prices spike (seasonal cycling), a chained Laspeyres index will systematically drift upward, failing to return to 100 even when all individual prices return to their baseline levels. To avoid chain drift in empirical macroeconomic accounting, statistical agencies chain indices annually rather than monthly or quarterly.


---

## Modern Economic Index Number Theory: Divisia, Törnqvist, and Superlative Indices

While classical index number theory focused predominantly on fixed-basket aggregative formulations (Laspeyres and Paasche), twentieth-century mathematical economics established rigorous microeconomic and axiomatic foundations through the work of François Divisia (1925), Erwin Diewert (1976), and Leo Törnqvist (1936).

### 1. The Continuous Divisia Index
In 1925, the French mathematical economist François Divisia proposed a continuous-time formulation of price and quantity indices. Let $p_i(t)$ and $q_i(t)$ represent the continuous price and quantity trajectories of commodity $i$ at time $t$. The aggregate expenditure at time $t$ is:

$$E(t) = \sum_{i=1}^{n} p_i(t) q_i(t)$$

Differentiating both sides with respect to continuous time $t$:

$$\frac{dE(t)}{dt} = \sum_{i=1}^{n} \frac{dp_i(t)}{dt} q_i(t) + \sum_{i=1}^{n} p_i(t) \frac{dq_i(t)}{dt}$$

Dividing by total expenditure $E(t)$:

$$\frac{1}{E(t)} \frac{dE(t)}{dt} = \sum_{i=1}^{n} \left( \frac{p_i(t) q_i(t)}{E(t)} \right) \frac{1}{p_i(t)} \frac{dp_i(t)}{dt} + \sum_{i=1}^{n} \left( \frac{p_i(t) q_i(t)}{E(t)} \right) \frac{1}{q_i(t)} \frac{dq_i(t)}{dt}$$

Defining $w_i(t) = \frac{p_i(t) q_i(t)}{E(t)}$ as the instantaneous expenditure share of commodity $i$, and noting that $\frac{1}{x} \frac{dx}{dt} = \frac{d \ln(x)}{dt}$, the proportional growth rate of nominal expenditure decomposes into the sum of the instantaneous growth rates of the aggregate price index $P(t)$ and quantity index $Q(t)$:

$$\frac{d \ln[E(t)]}{dt} = \frac{d \ln[P(t)]}{dt} + \frac{d \ln[Q(t)]}{dt}$$

where the continuous growth rate of the **Divisia Price Index** is defined as:

$$\frac{d \ln[P(t)]}{dt} = \sum_{i=1}^{n} w_i(t) \frac{d \ln[p_i(t)]}{dt}$$

Integrating over a discrete calendar interval $[0, 1]$:

$$\ln[P(1)] - \ln[P(0)] = \int_{0}^{1} \sum_{i=1}^{n} w_i(t) \frac{d \ln[p_i(t)]}{dt} dt$$

The Divisia index possesses remarkable theoretical properties: it satisfies both the Time Reversal Test and the Factor Reversal Test continuously. However, because economic data are collected at discrete intervals rather than continuously, the line integral cannot be evaluated without discrete approximation.

### 2. The Törnqvist Discrete Approximation
To approximate the continuous Divisia line integral using discrete data, Finnish statistician Leo Törnqvist (1936) replaced the continuous expenditure shares with the arithmetic mean of the base and current period expenditure shares:

$$\bar{w}_i = \frac{w_{i,0} + w_{i,t}}{2}$$

Taking the exponential of the weighted sum of log price relatives yields the **Törnqvist Price Index**:

$$\ln(P_T) = \sum_{i=1}^{n} \bar{w}_i \ln\left( \frac{p_{i,t}}{p_{i,0}} \right) = \sum_{i=1}^{n} \left( \frac{w_{i,0} + w_{i,t}}{2} \right) \ln\left( \frac{p_{i,t}}{p_{i,0}} \right)$$

$$P_T = \prod_{i=1}^{n} \left( \frac{p_{i,t}}{p_{i,0}} \right)^{\frac{w_{i,0} + w_{i,t}}{2}}$$

The Törnqvist index is symmetric with respect to time, treats both periods symmetrically, and accommodates smooth consumer substitution between goods.

### 3. Diewert's Theory of Superlative Index Numbers
In a landmark 1976 paper, Canadian econometrician W. Erwin Diewert introduced the concept of **Superlative Index Numbers**. A price index formula is defined as superlative if it is exact for a flexible unit cost function—meaning a cost function that provides a second-order Taylor series approximation to an arbitrary, twice continuously differentiable aggregator function.

Diewert established two foundational theorems:
1. **Fisher's Ideal Index is Superlative**: Fisher's index $P_F = \sqrt{P_L \times P_P}$ is exact for the flexible Quadratic Mean of Order $r = 2$ unit cost function:
   $$C(p) = \left( \sum_{i=1}^{n} \sum_{j=1}^{n} b_{ij} p_i^{1/2} p_j^{1/2} \right)^{2}$$
2. **The Törnqvist Index is Superlative**: The Törnqvist index $P_T$ is exact for the flexible Translog (transcendental logarithmic) unit cost function:
   $$\ln[C(p)] = \alpha_0 + \sum_{i=1}^{n} \alpha_i \ln(p_i) + \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} \gamma_{ij} \ln(p_i) \ln(p_j)$$

Because both Fisher's Ideal Index and the Törnqvist Index are superlative, they accommodate flexible substitution behavior among consumers as relative prices shift, eliminating upper-level substitution bias. In practical empirical applications, numerical values of $P_F$ and $P_T$ rarely differ by more than a fraction of a percent.

---

## Elementary Aggregate Indices and Chain Drift Dynamics

Before statistical agencies can compute weighted aggregative indices (like Laspeyres or Fisher), they must first compile thousands of price quotations for individual items within detailed product categories where quantity weights are unavailable. These initial aggregations are termed **Elementary Price Indices**.

### 1. Classical Elementary Formulations
Let $p_{i,0}$ and $p_{i,t}$ denote the price of item $i$ ($i = 1, \dots, k$) in the base and current period within an unweighted elementary stratum.
- **The Dutot Index (Ratio of Arithmetic Averages)**:
  $$P_{\text{Dutot}} = \frac{\frac{1}{k} \sum_{i=1}^{k} p_{i,t}}{\frac{1}{k} \sum_{i=1}^{k} p_{i,0}} = \frac{\sum_{i=1}^{k} p_{i,t}}{\sum_{i=1}^{k} p_{i,0}}$$
  The Dutot index is sensitive to units of measurement unless all items within the stratum are homogenous in physical specification.
- **The Carli Index (Arithmetic Average of Price Relatives)**:
  $$P_{\text{Carli}} = \frac{1}{k} \sum_{i=1}^{k} \left( \frac{p_{i,t}}{p_{i,0}} \right)$$
  The Carli index fails the Time Reversal Test: by Jensen's inequality for convex functions, the arithmetic mean of relatives and the arithmetic mean of inverted relatives satisfy:
  $$P_{\text{Carli}}(0, t) \times P_{\text{Carli}}(t, 0) > 1$$
  The Carli index is systematically biased upward and has been largely banished from international statistical guidelines.
- **The Jevons Index (Geometric Mean of Price Relatives)**:
  $$P_{\text{Jevons}} = \left[ \prod_{i=1}^{k} \left( \frac{p_{i,t}}{p_{i,0}} \right) \right]^{1/k} = \frac{\left[ \prod_{i=1}^{k} p_{i,t} \right]^{1/k}}{\left[ \prod_{i=1}^{k} p_{i,0} \right]^{1/k}}$$
  The Jevons index satisfies both the Unit Test and the Time Reversal Test. Furthermore, it implicitly assumes that consumers maintain constant expenditure shares within the item category (unitary elasticity of substitution, $\sigma = 1$). For these reasons, the Jevons index is recommended by the international Consumer Price Index Manual as the preferred elementary aggregator.

### 2. High-Frequency Scanner Data and Chain Drift
In modern digital statistical systems, statistical offices increasingly ingest massive scanner barcode datasets and web-scraped daily transactions. To maintain timely product coverage, analysts frequently chain high-frequency monthly or weekly indices.

However, chaining indices under high-frequency sales promotions and seasonal restocking produces the phenomenon of **Chain Drift**. If retail prices fluctuate cyclically due to weekend promotions (dropping by 20% on sale and rebounding by 25% on Monday), while consumers purchase heavily at the discount price and abstain at regular price, chaining standard formulas generates a cumulative index that drifts systematically away from the true fixed-base price level. Resolving chain drift requires deploying multilateral index number methods, such as the **GEKS (Gini-Eltetö-Köves-Szulc)** or **Rolling Year GEKS** algorithms.
