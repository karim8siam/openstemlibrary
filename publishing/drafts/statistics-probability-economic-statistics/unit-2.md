# Unit 2: Axiomatic Tests of Index Numbers & Cost-of-Living Metrics

The construction of price and quantity index numbers has inspired intense mathematical debates regarding what logical properties a reliable index formula must satisfy. In his monumental 1922 treatise *The Making of Index Numbers*, Irving Fisher examined over one hundred and eighty distinct mathematical index formulas, subjecting each to a rigorous battery of axiomatic tests. Fisher demonstrated that almost all classical index numbers fail elementary consistency tests, and identified the unique mathematical properties that elevate the Fisher Ideal Index above its competitors. In this unit, we formalize Fisher's axiomatic tests, prove Wald's impossibility theorem, and analyze practical macroeconomic cost-of-living metrics, consumer price indices, purchasing power deflators, and real wage dynamics.

## 2.1 Irving Fisher's Axiomatic Criteria for Index Numbers

Fisher's axiomatic (test) approach treats an index number formula $P(p_0, q_0, p_t, q_t)$ as a mathematical operator, evaluating whether it satisfies fundamental geometric, dimensional, and temporal consistency axioms.

### 1. The Identity Test (Commodity Monotonicity)
If prices in the current period remain identical to prices in the base period for every single commodity ($p_{it} = p_{i0}$ for all $i$), the price index must equal unity (or 100):

$$P(p_0, q_0, p_0, q_t) = 1.000$$

All standard index formulas (Laspeyres, Paasche, Fisher, Marshall-Edgeworth, Törnqvist) trivially satisfy the Identity Test.

### 2. The Proportionality Test
If all commodity prices in the current period change by a constant scalar multiple $\lambda > 0$ relative to the base period ($p_{it} = \lambda \cdot p_{i0}$ for all $i$), the price index must equal that exact scalar multiple:

$$P(p_0, q_0, \lambda p_0, q_t) = \lambda$$

All standard weighted aggregative indices satisfy the Proportionality Test.

### 3. The Dimensionality (Unit) Test
The numerical value of the price index must be completely invariant to changes in the physical units of measurement used for commodities (e.g., quoting wheat in kilograms versus metric tons, or petroleum in liters versus barrels) and changes in the monetary currency units (e.g., dollars versus cents).

Let $\alpha_i > 0$ denote physical scale factors and $\beta > 0$ denote monetary scale factors. The Unit Test requires:

$$P(\beta p_0 \mathbf{D}_\alpha, \mathbf{D}_\alpha^{-1} q_0, \beta p_t \mathbf{D}_\alpha, \mathbf{D}_\alpha^{-1} q_t) = P(p_0, q_0, p_t, q_t)$$

where $\mathbf{D}_\alpha = \text{diag}(\alpha_1, \dots, \alpha_N)$.
As established in Unit 1, simple unweighted aggregative indices fail the Unit Test, whereas all weighted aggregative indices (Laspeyres, Paasche, Fisher, Marshall-Edgeworth) satisfy the Unit Test.

### 4. The Time Reversal Test (TRT)
The Time Reversal Test is among the most celebrated axiomatic criteria in economic statistics. It requires that the index number formula possess temporal symmetry: if the temporal direction of the comparison is reversed (treating current period $t$ as the base and base period $0$ as the current period), the resulting backward index must be the exact mathematical reciprocal of the forward index.

Let $P_{0t}$ denote the price index measuring price change from base period $0$ to current period $t$.
Let $P_{t0}$ denote the index computed using the exact same mathematical formula, but interchanging the roles of periods $0$ and $t$ (replacing $p_0$ with $p_t$, $p_t$ with $p_0$, $q_0$ with $q_t$, and $q_t$ with $q_0$).
The **Time Reversal Test** requires:

$$P_{0t} \times P_{t0} = 1.000 \iff P_{t0} = \frac{1}{P_{0t}}$$

If an index indicates that prices doubled ($P_{0t} = 2.0$) from period 0 to period $t$, then evaluating price change backward from period $t$ to period 0 must indicate that prices were halved ($P_{t0} = 0.5$). An index that fails this test exhibits temporal asymmetry, systematically introducing an artificial directional drift.

### 5. The Factor Reversal Test (FRT)
The Factor Reversal Test requires that the product of a price index formula and its corresponding quantity index formula must equal the true **Value Relative Ratio** of total consumer expenditure between the two periods.

Let $V_{0t} = \frac{\sum_{i=1}^N p_{it} q_{it}}{\sum_{i=1}^N p_{i0} q_{i0}}$ denote the true expenditure value ratio.
Let $Q_{0t}$ denote the quantity index obtained by interchanging the symbols $p$ and $q$ in the price index formula (replacing prices with quantities and quantities with prices).
The **Factor Reversal Test** requires:

$$P_{0t} \times Q_{0t} = \frac{\sum p_t q_t}{\sum p_0 q_0} = V_{0t}$$

Just as Price multiplied by Quantity equals Total Expenditure for an individual commodity ($p \cdot q = v$), the macroeconomic Price Index multiplied by the Quantity Index must completely exhaust total expenditure change, leaving zero unexplained residual.

### 6. The Circular Test (Transitivity Test)
The Circular Test generalizes the Time Reversal Test across three or more time periods. It requires that direct comparison between period $0$ and period $2$ must equal the chained product of the intermediate comparisons:

$$P_{01} \times P_{12} \times P_{20} = 1.000 \iff P_{02} = P_{01} \times P_{12}$$

The Circular Test guarantees that a multi-period comparison is independent of the intermediate geographic or temporal routing.

## 2.2 Mathematical Proofs of Axiomatic Reversal Tests

We now present the formal mathematical proofs establishing which classical index numbers satisfy or fail Fisher's reversal tests.

### Proof: The Laspeyres Index Fails the Time Reversal Test
Recall the forward Laspeyres price index:
$$P_{0t}^L = \frac{\sum p_t q_0}{\sum p_0 q_0}$$
Interchange periods $0$ and $t$ to obtain the backward Laspeyres index $P_{t0}^L$:
$$P_{t0}^L = \frac{\sum p_0 q_t}{\sum p_t q_t}$$
Multiply the forward and backward indices:
$$P_{0t}^L \times P_{t0}^L = \left( \frac{\sum p_t q_0}{\sum p_0 q_0} \right) \times \left( \frac{\sum p_0 q_t}{\sum p_t q_t} \right) = \frac{(\sum p_t q_0) (\sum p_0 q_t)}{(\sum p_0 q_0) (\sum p_t q_t)}$$
In general, $(\sum p_t q_0) (\sum p_0 q_t) \ne (\sum p_0 q_0) (\sum p_t q_t)$.
Therefore:
$$P_{0t}^L \times P_{t0}^L \ne 1$$
The Laspeyres price index **fails the Time Reversal Test**.

### Proof: The Paasche Index Fails the Time Reversal Test
Recall the forward Paasche index:
$$P_{0t}^P = \frac{\sum p_t q_t}{\sum p_0 q_t}$$
Interchange periods $0$ and $t$:
$$P_{t0}^P = \frac{\sum p_0 q_0}{\sum p_t q_0}$$
Multiply the two indices:
$$P_{0t}^P \times P_{t0}^P = \left( \frac{\sum p_t q_t}{\sum p_0 q_t} \right) \times \left( \frac{\sum p_0 q_0}{\sum p_t q_0} \right) = \frac{(\sum p_t q_t) (\sum p_0 q_0)}{(\sum p_0 q_t) (\sum p_t q_0)} \ne 1$$
The Paasche price index **fails the Time Reversal Test**.
Notice that:
$$P_{0t}^L \times P_{t0}^P = \left( \frac{\sum p_t q_0}{\sum p_0 q_0} \right) \times \left( \frac{\sum p_0 q_0}{\sum p_t q_0} \right) = 1.000$$
The reciprocal of the forward Laspeyres index is the backward Paasche index!

### Formal Proof: Fisher's Ideal Index Satisfies the Time Reversal Test
Recall Fisher's Ideal Index:
$$P_{0t}^F = \sqrt{ \left( \frac{\sum p_t q_0}{\sum p_0 q_0} \right) \left( \frac{\sum p_t q_t}{\sum p_0 q_t} \right) }$$
Interchange periods $0$ and $t$ to obtain the backward Fisher index:
$$P_{t0}^F = \sqrt{ \left( \frac{\sum p_0 q_t}{\sum p_t q_t} \right) \left( \frac{\sum p_0 q_0}{\sum p_t q_0} \right) }$$
Multiply the forward and backward Fisher indices:
$$P_{0t}^F \times P_{t0}^F = \sqrt{ \left( \frac{\sum p_t q_0}{\sum p_0 q_0} \right) \left( \frac{\sum p_t q_t}{\sum p_0 q_t} \right) \times \left( \frac{\sum p_0 q_t}{\sum p_t q_t} \right) \left( \frac{\sum p_0 q_0}{\sum p_t q_0} \right) }$$
Rearrange the terms inside the square root:
$$P_{0t}^F \times P_{t0}^F = \sqrt{ \left( \frac{\sum p_t q_0}{\sum p_t q_0} \right) \times \left( \frac{\sum p_0 q_0}{\sum p_0 q_0} \right) \times \left( \frac{\sum p_t q_t}{\sum p_t q_t} \right) \times \left( \frac{\sum p_0 q_t}{\sum p_0 q_t} \right) } = \sqrt{1 \times 1 \times 1 \times 1} = 1.000$$
Therefore:
$$P_{0t}^F \times P_{t0}^F = 1.000 \iff P_{t0}^F = \frac{1}{P_{0t}^F}$$
Fisher's Ideal Index **strictly satisfies the Time Reversal Test**. $\blacksquare$

### Proof: The Laspeyres and Paasche Indices Fail the Factor Reversal Test
For the Laspeyres index, interchanging $p$ and $q$ gives the Laspeyres quantity index:
$$Q_{0t}^L = \frac{\sum q_t p_0}{\sum q_0 p_0} = \frac{\sum p_0 q_t}{\sum p_0 q_0}$$
Multiply price index by quantity index:
$$P_{0t}^L \times Q_{0t}^L = \left( \frac{\sum p_t q_0}{\sum p_0 q_0} \right) \times \left( \frac{\sum p_0 q_t}{\sum p_0 q_0} \right) = \frac{(\sum p_t q_0) (\sum p_0 q_t)}{(\sum p_0 q_0)^2} \ne \frac{\sum p_t q_t}{\sum p_0 q_0}$$
Laspeyres **fails the Factor Reversal Test**.

Similarly, for the Paasche index:
$$Q_{0t}^P = \frac{\sum q_t p_t}{\sum q_0 p_t} = \frac{\sum p_t q_t}{\sum p_t q_0}$$
$$P_{0t}^P \times Q_{0t}^P = \left( \frac{\sum p_t q_t}{\sum p_0 q_t} \right) \times \left( \frac{\sum p_t q_t}{\sum p_t q_0} \right) = \frac{(\sum p_t q_t)^2}{(\sum p_0 q_t) (\sum p_t q_0)} \ne \frac{\sum p_t q_t}{\sum p_0 q_0}$$
Paasche **fails the Factor Reversal Test**.

### Formal Proof: Fisher's Ideal Index Satisfies the Factor Reversal Test
Recall Fisher's price index:
$$P_{0t}^F = \sqrt{ \frac{\sum p_t q_0}{\sum p_0 q_0} \times \frac{\sum p_t q_t}{\sum p_0 q_t} }$$
Interchanging the symbols $p$ and $q$ yields Fisher's quantity index:
$$Q_{0t}^F = \sqrt{ \frac{\sum q_t p_0}{\sum q_0 p_0} \times \frac{\sum q_t p_t}{\sum q_0 p_t} } = \sqrt{ \frac{\sum p_0 q_t}{\sum p_0 q_0} \times \frac{\sum p_t q_t}{\sum p_t q_0} }$$
Multiply the price index and quantity index:
$$P_{0t}^F \times Q_{0t}^F = \sqrt{ \left( \frac{\sum p_t q_0}{\sum p_0 q_0} \times \frac{\sum p_t q_t}{\sum p_0 q_t} \right) \times \left( \frac{\sum p_0 q_t}{\sum p_0 q_0} \times \frac{\sum p_t q_t}{\sum p_t q_0} \right) }$$
Notice the remarkable cross-cancellations:
- The term $\sum p_t q_0$ in the first numerator cancels with $\sum p_t q_0$ in the second denominator.
- The term $\sum p_0 q_t$ in the second numerator cancels with $\sum p_0 q_t$ in the first denominator.
The product simplifies to:
$$P_{0t}^F \times Q_{0t}^F = \sqrt{ \frac{(\sum p_t q_t)^2}{(\sum p_0 q_0)^2} } = \frac{\sum p_t q_t}{\sum p_0 q_0} = V_{0t}$$
Fisher's Ideal Index **strictly satisfies the Factor Reversal Test**. $\blacksquare$

### Proof: The Marshall–Edgeworth Index Satisfies TRT but Fails FRT
Recall the Marshall–Edgeworth index:
$$P_{0t}^{ME} = \frac{\sum p_t (q_0 + q_t)}{\sum p_0 (q_0 + q_t)} = \frac{\sum p_t q_0 + \sum p_t q_t}{\sum p_0 q_0 + \sum p_0 q_t}$$
Interchanging periods $0$ and $t$:
$$P_{t0}^{ME} = \frac{\sum p_0 (q_t + q_0)}{\sum p_t (q_t + q_0)} = \frac{\sum p_0 q_t + \sum p_0 q_0}{\sum p_t q_t + \sum p_t q_0}$$
Notice that the numerator of $P_{t0}^{ME}$ is identically the denominator of $P_{0t}^{ME}$, and the denominator of $P_{t0}^{ME}$ is identically the numerator of $P_{0t}^{ME}$!
$$P_{0t}^{ME} \times P_{t0}^{ME} = \left( \frac{\sum p_t q_0 + \sum p_t q_t}{\sum p_0 q_0 + \sum p_0 q_t} \right) \times \left( \frac{\sum p_0 q_0 + \sum p_0 q_t}{\sum p_t q_0 + \sum p_t q_t} \right) = 1.000$$
Marshall–Edgeworth **satisfies the Time Reversal Test**. However, it fails the Factor Reversal Test.

## 2.3 Wald's Impossibility Theorem for Index Numbers

A natural question arises: **Can an analyst construct an index number formula that simultaneously satisfies all desirable axiomatic tests—including the Time Reversal Test, the Factor Reversal Test, and the Circular Test?**

In 1937, the mathematical statistician Abraham Wald formulated and proved the **Wald Impossibility Theorem** for index numbers.

### Theorem (Abraham Wald, 1937):
There does not exist any bilateral aggregative price index formula $P(p_0, q_0, p_t, q_t)$ that simultaneously satisfies:
1. The Proportionality Test.
2. The Circular (Transitivity) Test.
3. The Factor Reversal Test.
unless the index degenerates into an unweighted geometric mean (like the Jevons index), which treats all commodities as equally important and fails to reflect economic expenditure shares.

Wald proved that Fisher's Ideal Index, while satisfying both Time and Factor Reversal Tests, **fails the Circular Test**. Conversely, simple geometric indices that satisfy the Circular Test fail the Factor Reversal Test. This mathematical impossibility establishes that every practical index number formula represents a deliberate analytical compromise between competing axiomatic desiderata.

## 2.4 Consumer Price Index (CPI) and Cost-of-Living Metrics

The **Consumer Price Index ($CPI$)** is the most widely cited macroeconomic statistic in the world. It measures the average change over time in the prices paid by urban consumers for a representative market basket of consumer goods and services.

### Methods of Constructing the CPI
Statistical agencies construct the CPI using two alternative operational methods:

1. **The Aggregate Expenditure Method**:
   Identical in formulation to the Laspeyres weighted aggregative index:
   $$CPI = \frac{\sum p_t q_0}{\sum p_0 q_0} \times 100$$
   where $q_0$ represents the quantities consumed in a benchmark Household Income and Expenditure Survey (HIES).

2. **The Family Budget Method (Weighted Average of Price Relatives)**:
   $$CPI = \frac{\sum W_i R_i}{\sum W_i} = \frac{\sum (p_0 q_0) \left( \frac{p_t}{p_0} \right)}{\sum p_0 q_0} \times 100$$
   where $R_i = \frac{p_{it}}{p_{i0}} \times 100$ is the price relative for commodity $i$, and $W_i = p_{i0} q_{i0}$ is the base-period expenditure incurred by the average family on commodity $i$.
   The Aggregate Expenditure Method and Family Budget Method yield **identical numerical results**.

## 2.5 Macroeconomic Applications: Deflating, Real Wages, and Purchasing Power

Index numbers provide the indispensable mathematical tools for converting nominal monetary statistics into real, inflation-adjusted purchasing power metrics.

### 1. Deflating Nominal Economic Series
To evaluate whether an economic magnitude (such as national retail sales, manufacturing shipments, or government tax revenues) has grown in genuine physical volume or merely through price inflation, analysts **deflate** the series:

$$\text{Real Value} = \frac{\text{Nominal Value}}{\text{Price Index}} \times 100$$

### 2. Purchasing Power of Money (PPM)
The purchasing power of a currency unit (e.g., dollar or taka) measures the quantity of goods and services that one unit of currency can buy. It is the exact reciprocal of the price index:

$$PPM = \frac{1}{CPI} \times 100$$

If the Consumer Price Index rises from $100$ to $125$ (a $25\%$ inflation rate), the purchasing power of money becomes:

$$PPM = \frac{1}{125} \times 100 = 0.80 \implies 80.0\%$$

The currency has lost $20\%$ of its real purchasing power.

### 3. Real Wages and the Real Wage Index
Let $W_{\text{nom}}$ denote the nominal monetary wage earned by an industrial worker, and let $CPI$ denote the consumer price index.
The **Real Wage** is:

$$W_{\text{real}} = \frac{W_{\text{nom}}}{CPI} \times 100$$

The **Real Wage Index ($RWI$)** measures relative changes in workers' standard of living:

$$RWI = \frac{\text{Money Wage Index}}{CPI} \times 100$$

If nominal wages increase by $10\%$ while the $CPI$ surges by $15\%$:
$$RWI = \frac{110}{115} \times 100 \approx 95.65$$
Although the worker takes home $10\%$ more paper currency, their real standard of living has fallen by $4.35\%$.

## Fully worked question 1: Mathematical Verification of Fisher's Time and Factor Reversal Tests

### Question
An econometric auditing bureau evaluates price and quantity indices across three industrial raw materials: Copper ($A$), Aluminum ($B$), and Nickel ($C$). The recorded prices per metric ton and transaction volumes across base year ($0$) and current year ($t$) are:

| Material | Base Price ($p_0$) | Base Quantity ($q_0$) | Current Price ($p_t$) | Current Quantity ($q_t$) |
| :---: | :---: | :---: | :---: | :---: |
| **A (Copper)** | $8{,}000$ | $50$ | $10{,}000$ | $60$ |
| **B (Aluminum)** | $2{,}000$ | $120$ | $2{,}500$ | $100$ |
| **C (Nickel)** | $15{,}000$ | $20$ | $18{,}000$ | $25$ |

1. Calculate the four primary expenditure cross-products: $\sum p_0 q_0, \sum p_t q_0, \sum p_0 q_t,$ and $\sum p_t q_t$.
2. Compute the forward Laspeyres, Paasche, and Fisher price indices ($P_{0t}^L, P_{0t}^P, P_{0t}^F$).
3. Test whether the Laspeyres index and Fisher's Ideal Index satisfy the Time Reversal Test ($P_{0t} \times P_{t0} = 1$).
4. Compute the Fisher quantity index ($Q_{0t}^F$) and verify that Fisher's Ideal Index satisfies the Factor Reversal Test ($P_{0t}^F \times Q_{0t}^F = V_{0t}$).

### Solution, step 1: Compute Expenditure Cross-Products
1. **Base-Period Total Expenditure ($\sum p_0 q_0$)**:
   - Copper: $8{,}000 \times 50 = 400{,}000$
   - Aluminum: $2{,}000 \times 120 = 240{,}000$
   - Nickel: $15{,}000 \times 20 = 300{,}000$
   $$\sum p_0 q_0 = 400{,}000 + 240{,}000 + 300{,}000 = 940{,}000$$

2. **Cost of Base Basket at Current Prices ($\sum p_t q_0$)**:
   - Copper: $10{,}000 \times 50 = 500{,}000$
   - Aluminum: $2{,}500 \times 120 = 300{,}000$
   - Nickel: $18{,}000 \times 20 = 360{,}000$
   $$\sum p_t q_0 = 500{,}000 + 300{,}000 + 360{,}000 = 1{,}160{,}000$$

3. **Cost of Current Basket at Base Prices ($\sum p_0 q_t$)**:
   - Copper: $8{,}000 \times 60 = 480{,}000$
   - Aluminum: $2{,}000 \times 100 = 200{,}000$
   - Nickel: $15{,}000 \times 25 = 375{,}000$
   $$\sum p_0 q_t = 480{,}000 + 200{,}000 + 375{,}000 = 1{,}055{,}000$$

4. **Current-Period Actual Expenditure ($\sum p_t q_t$)**:
   - Copper: $10{,}000 \times 60 = 600{,}000$
   - Aluminum: $2{,}500 \times 100 = 250{,}000$
   - Nickel: $18{,}000 \times 25 = 450{,}000$
   $$\sum p_t q_t = 600{,}000 + 250{,}000 + 450{,}000 = 1{,}300{,}000$$

### Solution, step 2: Compute Price Indices
1. **Laspeyres Price Index ($P_{0t}^L$)**:
   $$P_{0t}^L = \frac{\sum p_t q_0}{\sum p_0 q_0} = \frac{1{,}160{,}000}{940{,}000} \approx 1.234043 \implies 123.40$$

2. **Paasche Price Index ($P_{0t}^P$)**:
   $$P_{0t}^P = \frac{\sum p_t q_t}{\sum p_0 q_t} = \frac{1{,}300{,}000}{1{,}055{,}000} \approx 1.232227 \implies 123.22$$

3. **Fisher's Ideal Price Index ($P_{0t}^F$)**:
   $$P_{0t}^F = \sqrt{P_{0t}^L \times P_{0t}^P} = \sqrt{1.234043 \times 1.232227} = \sqrt{1.520621} \approx 1.233135 \implies 123.31$$

### Solution, step 3: Execution of the Time Reversal Test
1. **Test for Laspeyres Index**:
   The backward Laspeyres index is:
   $$P_{t0}^L = \frac{\sum p_0 q_t}{\sum p_t q_t} = \frac{1{,}055{,}000}{1{,}300{,}000} \approx 0.811538$$
   Multiply forward and backward:
   $$P_{0t}^L \times P_{t0}^L = 1.234043 \times 0.811538 \approx 1.001476 \ne 1.000$$
   Because $1.001476 \ne 1$, the Laspeyres index **fails the Time Reversal Test**.

2. **Test for Fisher's Ideal Index**:
   The backward Fisher index is:
   $$P_{t0}^F = \sqrt{ \left( \frac{\sum p_0 q_t}{\sum p_t q_t} \right) \left( \frac{\sum p_0 q_0}{\sum p_t q_0} \right) } = \sqrt{ \frac{1{,}055{,}000}{1{,}300{,}000} \times \frac{940{,}000}{1{,}160{,}000} } = \sqrt{0.811538 \times 0.810345} = \sqrt{0.657626} \approx 0.810941$$
   Multiply forward and backward:
   $$P_{0t}^F \times P_{t0}^F = 1.233135 \times 0.810941 = 0.999999 \approx 1.000$$
   Fisher's Ideal Index **satisfies the Time Reversal Test** with exact precision.

### Solution, step 4: Execution of the Factor Reversal Test
The true Expenditure Value Ratio is:

$$V_{0t} = \frac{\sum p_t q_t}{\sum p_0 q_0} = \frac{1{,}300{,}000}{940{,}000} \approx 1.382979$$

Fisher's Quantity Index ($Q_{0t}^F$) is obtained by interchanging prices and quantities:

$$Q_{0t}^F = \sqrt{ \left( \frac{\sum q_t p_0}{\sum q_0 p_0} \right) \left( \frac{\sum q_t p_t}{\sum q_0 p_t} \right) } = \sqrt{ \left( \frac{\sum p_0 q_t}{\sum p_0 q_0} \right) \left( \frac{\sum p_t q_t}{\sum p_t q_0} \right) }$$

Substitute the numerical values:

$$Q_{0t}^F = \sqrt{ \frac{1{,}055{,}000}{940{,}000} \times \frac{1{,}300{,}000}{1{,}160{,}000} } = \sqrt{1.122340 \times 1.120690} = \sqrt{1.257795} \approx 1.121515 \implies 112.15$$

Physical raw material transaction volume increased by $12.15\%$.

Now multiply Fisher's Price Index by Fisher's Quantity Index:

$$P_{0t}^F \times Q_{0t}^F = 1.233135 \times 1.121515 \approx 1.382979$$

Notice that:

$$P_{0t}^F \times Q_{0t}^F = 1.382979 = V_{0t}$$

The product matches the true expenditure value ratio $V_{0t}$ to the sixth decimal place! Fisher's Ideal Index **strictly satisfies the Factor Reversal Test**.

## Fully worked question 2: Real Wage Deflation and Purchasing Power Dynamics

### Question
A labor economics research institute analyzes wages and retail price inflation for an industrial manufacturing workforce across a six-year period:

| Year | Monthly Nominal Wage ($W$) | Consumer Price Index ($CPI$) |
| :---: | :---: | :---: |
| **2019** | $\$2{,}500$ | $100.0$ |
| **2020** | $\$2{,}700$ | $105.0$ |
| **2021** | $\$2{,}900$ | $112.0$ |
| **2022** | $\$3{,}150$ | $126.0$ |
| **2023** | $\$3{,}400$ | $140.0$ |
| **2024** | $\$3{,}600$ | $150.0$ |

1. Calculate the Purchasing Power of the Dollar ($PPM$) in each year relative to the 2019 baseline.
2. Deflate the nominal monthly wages to compute the Real Monthly Wage ($W_{\text{real}}$) at constant 2019 purchasing power for each year.
3. Construct the Nominal Money Wage Index ($MWI$) and the Real Wage Index ($RWI$) with $2019 = 100$. Evaluate whether workers experienced an improvement or deterioration in real material welfare between 2019 and 2024.

### Solution, step 1: Calculate Purchasing Power of Money (PPM)
The formula is $PPM = \frac{100}{CPI}$:
- **2019**: $\frac{100}{100.0} = 1.000 \implies 100.0\%$
- **2020**: $\frac{100}{105.0} \approx 0.9524 \implies 95.24\%$
- **2021**: $\frac{100}{112.0} \approx 0.8929 \implies 89.29\%$
- **2022**: $\frac{100}{126.0} \approx 0.7937 \implies 79.37\%$
- **2023**: $\frac{100}{140.0} \approx 0.7143 \implies 71.43\%$
- **2024**: $\frac{100}{150.0} \approx 0.6667 \implies 66.67\%$

By 2024, the currency lost one-third ($33.33\%$) of its purchasing power due to price inflation.

### Solution, step 2: Calculate Real Wages at Constant 2019 Prices
The formula is $W_{\text{real}} = \frac{W_{\text{nominal}}}{CPI} \times 100$:
- **2019**: $\frac{2{,}500}{100.0} \times 100 = \$2{,}500.00$
- **2020**: $\frac{2{,}700}{105.0} \times 100 = \$2{,}571.43$
- **2021**: $\frac{2{,}900}{112.0} \times 100 = \$2{,}589.29$
- **2022**: $\frac{3{,}150}{126.0} \times 100 = \$2{,}500.00$
- **2023**: $\frac{3{,}400}{140.0} \times 100 = \$2{,}428.57$
- **2024**: $\frac{3{,}600}{150.0} \times 100 = \$2{,}400.00$

### Solution, step 3: Construct Indices and Synthesize Welfare Trajectory
1. **Nominal Money Wage Index ($MWI = \frac{W_t}{W_{2019}} \times 100$)**:
   - 2019: $\frac{2{,}500}{2{,}500} \times 100 = 100.00$
   - 2020: $\frac{2{,}700}{2{,}500} \times 100 = 108.00$
   - 2021: $\frac{2{,}900}{2{,}500} \times 100 = 116.00$
   - 2022: $\frac{3{,}150}{2{,}500} \times 100 = 126.00$
   - 2023: $\frac{3{,}400}{2{,}500} \times 100 = 136.00$
   - 2024: $\frac{3{,}600}{2{,}500} \times 100 = 144.00$

2. **Real Wage Index ($RWI = \frac{W_{\text{real}, t}}{W_{\text{real}, 2019}} \times 100 = \frac{MWI}{CPI} \times 100$)**:
   - 2019: $\frac{2{,}500.00}{2{,}500.00} \times 100 = 100.00$
   - 2020: $\frac{2{,}571.43}{2{,}500.00} \times 100 = 102.86$
   - 2021: $\frac{2{,}589.29}{2{,}500.00} \times 100 = 103.57$
   - 2022: $\frac{2{,}500.00}{2{,}500.00} \times 100 = 100.00$
   - 2023: $\frac{2{,}428.57}{2{,}500.00} \times 100 = 97.14$
   - 2024: $\frac{2{,}400.00}{2{,}500.00} \times 100 = 96.00$

**Economic Welfare Diagnosis**:
1. Between 2019 and 2021, nominal wage gains ($+16\%$) outpaced inflation ($+12\%$), expanding real wages to a peak of $\$2{,}589.29$ ($RWI = 103.57$).
2. Between 2022 and 2024, inflation accelerated dramatically ($CPI$ surging from $112$ to $150$, a $33.9\%$ jump), outstripping wage increases ($MWI$ rising from $116$ to $144$, a $24.1\%$ jump).
3. By 2024, despite receiving $\$3{,}600$ per month (a substantial $44.0\%$ increase in paper currency), workers' real purchasing power had collapsed to $\$2{,}400$ in 2019 purchasing power—a net **$4.0\%$ decline in real material living standards** ($RWI = 96.00$). This exemplifies the classic **money illusion** in macroeconomics.

## Fully worked question 3: Consumer Price Index via Family Budget Method and Wage Compensation

### Question
A tripartite national labor conciliation board investigates cost-of-living adjustments for low-income industrial workers. A representative Household Expenditure Survey establishes the consumption weights and commodity price relatives between base year $2018$ and current year $2024$:

| Expenditure Category | Base Expenditure Weight ($W_i = p_0 q_0$) | 2018 Price ($p_0$) | 2024 Price ($p_t$) |
| :---: | :---: | :---: | :---: |
| **1. Cereals & Food** | $\$4{,}000$ | $\$20.00$ | $\$32.00$ |
| **2. Housing Rent** | $\$2{,}500$ | $\$500.00$ | $\$700.00$ |
| **3. Fuel & Lighting** | $\$1{,}000$ | $\$50.00$ | $\$80.00$ |
| **4. Clothing** | $\$1{,}500$ | $\$100.00$ | $\$125.00$ |
| **5. Miscellaneous Services** | $\$1{,}000$ | $\$40.00$ | $\$60.00$ |

1. Calculate the price relatives ($R_i = rac{p_t}{p_0} 	imes 100$) for each expenditure category.
2. Calculate the Consumer Price Index ($CPI$) for 2024 ($2018 = 100$) using the Family Budget Method: $CPI = rac{\sum W_i R_i}{\sum W_i}$.
3. If an industrial worker earned a monthly wage of $\$500.00$ in 2018, determine the minimum nominal wage that must be paid in 2024 to fully insulate the worker from cost-of-living increases, and compute the required Dearness Allowance (DA).

### Solution, step 1: Calculate Price Relatives ($R_i$)
The price relative formula is $R_i = rac{p_t}{p_0} 	imes 100$:
1. **Cereals & Food**:
   $$R_1 = rac{32.00}{20.00} 	imes 100 = 160.00$$
2. **Housing Rent**:
   $$R_2 = rac{700.00}{500.00} 	imes 100 = 140.00$$
3. **Fuel & Lighting**:
   $$R_3 = rac{80.00}{50.00} 	imes 100 = 160.00$$
4. **Clothing**:
   $$R_4 = rac{125.00}{100.00} 	imes 100 = 125.00$$
5. **Miscellaneous**:
   $$R_5 = rac{60.00}{40.00} 	imes 100 = 150.00$$

### Solution, step 2: Compute CPI via Family Budget Method
We evaluate the weighted products $W_i 	imes R_i$:
- Food: $4{,}000 	imes 160.00 = 640{,}000$
- Rent: $2{,}500 	imes 140.00 = 350{,}000$
- Fuel: $1{,}000 	imes 160.00 = 160{,}000$
- Clothing: $1{,}500 	imes 125.00 = 187{,}500$
- Misc: $1{,}000 	imes 150.00 = 150{,}000$

Summing the weights:
$$\sum W_i = 4{,}000 + 2{,}500 + 1{,}000 + 1{,}500 + 1{,}000 = 10{,}000$$

Summing the weighted products:
$$\sum (W_i R_i) = 640{,}000 + 350{,}000 + 160{,}000 + 187{,}500 + 150{,}000 = 1{,}487{,}500$$

The Consumer Price Index is:

$$CPI = rac{\sum (W_i R_i)}{\sum W_i} = rac{1{,}487{,}500}{10{,}000} = 148.75$$

The cost of living for industrial workers rose by **$48.75\%$** between 2018 and 2024.

### Solution, step 3: Wage Indexation and Dearness Allowance Calculation
The baseline wage in 2018 was $W_0 = \$500.00$.
To maintain real purchasing power, the compensated 2024 wage $W_t$ must satisfy:

$$W_t = W_0 	imes \left( rac{CPI}{100} 
ight) = \$500.00 	imes \left( rac{148.75}{100} 
ight) = \$500.00 	imes 1.4875 = \$743.75$$

The required monthly nominal wage in 2024 is **$\$743.75$**.

The required **Dearness Allowance (DA)**—the compensatory cash supplement added to basic pay—is:

$$	ext{DA} = W_t - W_0 = \$743.75 - \$500.00 = \$243.75 	ext{ per month}$$

Expressed as a percentage of basic wage:
$$	ext{DA Rate} = rac{\$243.75}{\$500.00} 	imes 100 = 48.75\%$$

Paying a monthly Dearness Allowance of $\$243.75$ exactly neutralizes the $48.75\%$ rise in the consumer price index, fully preserving the worker's real standard of living.


---

## Axiomatic Incompatibility: Wald's Impossibility Theorem

A central preoccupation of mathematical index number theory throughout the twentieth century was the pursuit of an index formula satisfying all desirable axiomatic criteria simultaneously. Irving Fisher famously tested dozens of formulas against his battery of tests. However, in 1937, the mathematical statistician Abraham Wald established a foundational negative result: **Wald's Inconsistency Theorem**.

### Statement and Proof of Wald's Incompatibility Theorem
Wald demonstrated that no single index number formula $P(p_0, p_t, q_0, q_t)$ can simultaneously satisfy:
1. **The Time Reversal Test**: $P(p_0, p_t, q_0, q_t) \times P(p_t, p_0, q_t, q_0) = 1$.
2. **The Factor Reversal Test**: $P(p_0, p_t, q_0, q_t) \times Q(p_0, p_t, q_0, q_t) = \frac{p_t^T q_t}{p_0^T q_0}$.
3. **The Circular (Transitivity) Test**: $P(p_0, p_r, q_0, q_r) \times P(p_r, p_t, q_r, q_t) = P(p_0, p_t, q_0, q_t)$ for any intermediate period $r$.

The proof proceeds by examining the functional dependence of the index on quantities. To satisfy the Circular Test across all possible price paths, the weights attached to prices in period $r$ must not depend on the specific baseline period $0$ or current period $t$. Consequently, an index satisfying circularity must take the general form of a ratio of fixed-weight linear combinations:
$$P(0, t) = \frac{\sum c_i p_{i,t}}{\sum c_i p_{i,0}}$$
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

Let $p_i$ be the market price of a complex durable good (such as a laptop computer or motor vehicle), and let $z_i = [z_{i1}, z_{i2}, \dots, z_{ik}]$ represent a vector of $k$ objectively measurable technical attributes (processor speed, RAM capacity, battery life, weight, screen resolution). The **Hedonic Price Function** relates market price to attributes:

$$\ln(p_i) = \beta_0 + \sum_{j=1}^{k} \beta_j z_{ij} + \epsilon_i$$

where:
- $\beta_j = \frac{\partial \ln(p)}{\partial z_j}$ represents the marginal implicit shadow price of characteristic $j$, indicating the percentage premium consumers are willing to pay for an additional unit of that attribute.

When an obsolete model $A$ (with attributes $z_A$ and price $p_{A,0}$) is replaced in the market by an upgraded model $B$ (with attributes $z_B$ and price $p_{B,t}$), the pure quality-adjusted price relative is:

$$\text{Pure Price Relative} = \frac{p_{B,t}}{p_{A,0} \times \exp\left( \sum_{j=1}^{k} \hat{\beta}_j (z_{Bj} - z_{Aj}) \right)}$$

The denominator adjusts the baseline price upward by the exact monetary value of the quality improvement, ensuring that only genuine price inflation enters the Consumer Price Index.


---

## The Stochastic Approach to Index Numbers

In contrast to the axiomatic approach of Fisher or the microeconomic approach of Konüs, the **Stochastic Approach to Index Numbers** treats observed price relatives as independent sample realizations of a underlying general inflation signal contaminated by idiosyncratic, item-specific relative price shocks. Pioneered by William Stanley Jevons (1863) and Francis Ysidro Edgeworth (1887), and modernized by E. A. Selvanathan and D. S. Prasada Rao (1994), this framework casts index construction as a formal problem of statistical estimation.

### 1. The Classical Unweighted Stochastic Model
Let $R_{it} = p_{it} / p_{i0}$ denote the observed price relative for commodity $i$ ($i = 1, \dots, k$) between base period $0$ and current period $t$.
The stochastic model posits:

$$R_{it} = \Pi_t \epsilon_{it}$$

where:
- $\Pi_t$ represents the common systematic macroeconomic price change parameter (the true underlying price level ratio).
- $\epsilon_{it}$ is a multiplicative random disturbance representing commodity-specific supply or demand shocks, satisfying $E[\epsilon_{it}] = 1$ and $\text{Var}(\epsilon_{it}) = \sigma^2$.

Taking natural logarithms linearizes the estimation equation:

$$\ln(R_{it}) = \pi_t + u_{it}$$

where $\pi_t = \ln(\Pi_t)$ and $u_{it} = \ln(\epsilon_{it})$ is an additive zero-mean disturbance with constant variance $\sigma_u^2$.
The Ordinary Least Squares (OLS) estimator of $\pi_t$ is the unweighted sample mean of the log price relatives:

$$\hat{\pi}_t = \frac{1}{k} \sum_{i=1}^{k} \ln(R_{it})$$

Exponentiating $\hat{\pi}_t$ yields the estimated price index:

$$\hat{\Pi}_t = \exp(\hat{\pi}_t) = \left[ \prod_{i=1}^{k} \left( \frac{p_{it}}{p_{i0}} \right) \right]^{1/k} = P_{\text{Jevons}}$$

The stochastic approach provides an explicit econometric justification for the **Jevons Index**: it is the Best Linear Unbiased Estimator (BLUE) of underlying general inflation when relative price shocks are identically and independently distributed across commodities.

### 2. Weighted Stochastic Regression Models
Because commodities vary widely in economic importance, the assumption of homoskedastic disturbances is unrealistic: expenditure-heavy staple commodities generally exhibit more stable relative prices than minor luxury goods.
To incorporate economic weights, Edgeworth proposed minimizing a weighted sum of squared residuals:

$$\min_{\pi_t} \sum_{i=1}^{k} w_i [\ln(R_{it}) - \pi_t]^2$$

where $w_i = \frac{1}{2}(w_{i0} + w_{it})$ is the average expenditure share of good $i$.
Setting the first derivative to zero yields:

$$\hat{\pi}_t = \sum_{i=1}^{k} w_i \ln(R_{it})$$

Exponentiating this weighted regression coefficient yields:

$$\hat{\Pi}_t = \exp\left( \sum_{i=1}^{k} w_i \ln\left( \frac{p_{it}}{p_{i0}} \right) \right) = P_{\text{Törnqvist}}$$

Under the stochastic framework, the **Törnqvist Superlative Index** emerges as the Weighted Least Squares econometric estimator of inflation. Furthermore, the regression framework yields standard errors and confidence intervals for the rate of inflation, allowing statisticians to conduct formal hypothesis tests regarding price stability.

---

## Plutocratic vs Democratic Price Indices and Distributional Inflation

The Consumer Price Index published by national statistical offices is constructed using national aggregate expenditure weights:

$$w_i = \frac{\sum_{h=1}^{H} E_{ih}}{\sum_{h=1}^{H} \sum_{j=1}^{n} E_{jh}}$$

where $E_{ih}$ represents expenditure on good $i$ by household $h$ across all $H$ households in the economy.

### 1. The Plutocratic Bias of the Aggregate CPI
In 1958, S. J. Prais demonstrated that the national aggregate expenditure weights represent an income-weighted average of individual household expenditure shares:

$$w_i = \sum_{h=1}^{H} \left( \frac{E_h}{E_{\text{total}}} \right) s_{ih}$$

where $s_{ih} = E_{ih} / E_h$ is the budget share of good $i$ in household $h$, and $E_h / E_{\text{total}}$ is household $h$'s share of aggregate national consumer spending.

Because affluent households spend vastly more money than impoverished households, their budget shares dominate national aggregate weights:
- A wealthy household spending $\$200{,}000$ annually receives **twenty times greater mathematical weight** in the national CPI than a low-income household spending $\$10{,}000$ annually.
- The official CPI is therefore fundamentally **Plutocratic**: it reflects the purchasing patterns of households near the 75th or 80th percentile of the income distribution.

### 2. The Democratic Price Index
To reflect democratic social welfare principles ("one household, one vote"), Prais formulated the **Democratic Price Index**:

$$w_i^{\text{dem}} = \frac{1}{H} \sum_{h=1}^{H} s_{ih}$$

The Democratic CPI assigns equal mathematical weight to every household's budget allocation regardless of wealth.

#### Policy Implications:
During periods when essential necessities (food, household heating, electricity, basic rent) inflate faster than luxury discretionary services (air travel, electronics, fine dining), the inflation rate experienced by the bottom two deciles of society is substantially higher than the official plutocratic CPI. Indexing state welfare benefits and minimum wages strictly to the plutocratic CPI leads to silent erosion of real living standards among the most vulnerable citizens.


---

## Multilateral Index Systems: Geary-Khamis and EKS Methods

When comparing price levels and real purchasing power across three or more countries simultaneously, standard bilateral index numbers (such as Fisher or Törnqvist) fail because they violate the **Transitivity (Circular) Property**: $P_{A/B} \times P_{B/C} \ne P_{A/C}$.
To produce consistent, transitively closed international comparisons without base-country dependency, the United Nations International Comparison Program (ICP) deploys multilateral index number systems.

### 1. The Eltetö-Köves-Szulc (EKS) Method
Formulated independently by Ödön Éltető and Péter Köves (1964) and Bohdan Szulc (1964), the **EKS Method** constructs a transitive multilateral price index matrix from an underlying system of non-transitive bilateral Fisher ideal indices $F_{j/k}$.

The EKS index between country $j$ and country $k$ is defined as the geometric mean of all indirect Fisher comparisons routed through every participating country $r$ ($r = 1, \dots, M$):

$$P_{j/k}^{\text{EKS}} = \left[ \prod_{r=1}^{M} \left( F_{j/r} \times F_{r/k} \right) \right]^{1/M} = \left[ \prod_{r=1}^{M} \left( \frac{F_{j/r}}{F_{k/r}} \right) \right]^{1/M}$$

The EKS method minimizes the logarithmic distance between the transitive multilateral indices and the underlying bilateral Fisher indices:
$$\min \sum_{j=1}^{M} \sum_{k=1}^{M} \left( \ln(P_{j/k}^{\text{EKS}}) - \ln(F_{j/k}) \right)^2$$
The EKS index satisfies transitivity, base-country invariance, and characteristicity, making it the preferred metric for international poverty comparisons and GDP per capita rankings across OECD and Eurostat member nations.

### 2. The Geary-Khamis (GK) System
Pioneered by R. C. Geary (1958) and Salem Khamis (1970), the **Geary-Khamis System** determines an international set of average commodity prices $\pi_i$ and country purchasing power parities $\text{PPP}_j$ simultaneously through a coupled system of linear equations:

1. **International Price of Commodity $i$**:
   $$\pi_i = \sum_{j=1}^{M} \left( \frac{p_{ij}}{\text{PPP}_j} \right) \left( \frac{q_{ij}}{\sum_{k=1}^{M} q_{ik}} \right)$$
   The international price $\pi_i$ is a quantity-weighted average of the purchasing-power-adjusted national prices of commodity $i$ across all countries.
2. **Purchasing Power Parity of Country $j$**:
   $$\text{PPP}_j = \frac{\sum_{i=1}^{n} p_{ij} q_{ij}}{\sum_{i=1}^{n} \pi_i q_{ij}}$$
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


---

## The Lloyd-Moulton Constant Elasticity of Substitution Price Index

While superlative index numbers (such as Fisher and Törnqvist) eliminate upper-level substitution bias by using expenditure weights from both the base and current periods, they suffer from an operational drawback for national statistical agencies: they can only be computed retrospectively after current-period expenditure surveys or national accounts data become available (often with a lag of one to two years).

To provide a real-time index that accommodates consumer substitution without requiring contemporaneous expenditure weights, P. J. Lloyd (1975) and Brent Moulton (1996) formulated the **Lloyd-Moulton CES Price Index**:

$$P_{\text{LM}}(p_0, p_t, w_0; \sigma) = \left[ \sum_{i=1}^{n} w_{i0} \left( \frac{p_{it}}{p_{i0}} \right)^{1-\sigma} \right]^{\frac{1}{1-\sigma}}, \quad \sigma \ne 1$$

where:
- $w_{i0}$ denotes the expenditure share of commodity $i$ in the base period ($w_{i0} = p_{i0} q_{i0} / \sum p_{j0} q_{j0}$).
- $\sigma \ge 0$ is the constant elasticity of substitution across commodities within the consumer preference aggregator.

### Mathematical Limiting Properties:
1. **Zero Substitution ($\sigma = 0$)**:
   When consumers exhibit zero willingness to substitute (Leontief fixed-coefficient preferences):
   $$P_{\text{LM}}(p_0, p_t, w_0; 0) = \sum_{i=1}^{n} w_{i0} \left( \frac{p_{it}}{p_{i0}} \right) = P_{\text{Laspeyres}}$$
   The Lloyd-Moulton index collapses exactly to the standard fixed-basket Laspeyres price index.
2. **Unitary Elasticity of Substitution ($\sigma \to 1$)**:
   By l'Hôpital's rule, as $\sigma \to 1$ (Cobb-Douglas preferences where expenditure shares remain invariant):
   $$\lim_{\sigma \to 1} P_{\text{LM}} = \prod_{i=1}^{n} \left( \frac{p_{it}}{p_{i0}} \right)^{w_{i0}} = P_{\text{Geometric Laspeyres}}$$
3. **General Substitution ($0 < \sigma < 1$)**:
   In empirical consumer expenditure systems, the aggregate upper-level elasticity of substitution typically falls in the range of $\sigma \approx 0.6$ to $0.8$. By estimating $\sigma$ econometrically from historical panel data, statistical agencies can compute the Lloyd-Moulton index concurrently using only base weights $w_0$ and current prices $p_t$, producing an inflation metric that tracks the superlative Fisher index within hundredths of a percentage point in real time.
