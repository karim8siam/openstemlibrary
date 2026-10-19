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

# Read Unit 1 and add deep sections
u1 = (OUT_DIR / "unit-1.md").read_text(encoding="utf-8")
u1_extra = """
### The Economic Theory of Index Numbers: Konüs True Cost-of-Living Index
While mathematical statisticians approach index numbers through axiomatic properties and aggregative formulas, economic theorists ground index numbers in microeconomic consumer optimization. In 1924, the Russian mathematical economist Alexander A. Konüs formulated the **True Cost-of-Living Index (COLI)**.

Let u = U(q) represent a consumer's continuous, quasi-concave utility function over consumption bundles q.
The minimum expenditure required to attain utility level u at price vector p is given by the consumer's **Expenditure Function** (or cost function):

$$E(p, u) = \min_{q} \{ p^T q : U(q) \ge u \}$$

Konüs defined the True Cost-of-Living Index as the ratio of minimum expenditures required to attain a specified base reference utility level u_0 under current prices p_t versus base prices p_0:

$$P_K(p_t, p_0; u_0) = \frac{E(p_t, u_0)}{E(p_0, u_0)}$$

#### The Fundamental Konüs Bounds:
Konüs established that the observable Laspeyres and Paasche index numbers provide rigorous upper and lower empirical bounds for the unobservable true cost of living:
1. **The Laspeyres Upper Bound**:
   Because the base-period bundle q_0 was chosen by the consumer under base prices p_0, it achieves utility U(q_0) = u_0. At current prices p_t, the consumer could choose to purchase the same bundle q_0, incurring cost p_t^T q_0. However, by substituting away from relatively expensive goods, the consumer can attain utility u_0 at a cost strictly less than or equal to p_t^T q_0:
   $$E(p_t, u_0) \le p_t^T q_0$$
   Dividing both sides by base expenditure E(p_0, u_0) = p_0^T q_0 yields the celebrated **Konüs Theorem**:
   $$P_K(p_t, p_0; u_0) \le \frac{p_t^T q_0}{p_0^T q_0} = P_L$$
   The Laspeyres index is a strict mathematical upper bound to the true cost-of-living index!
2. **The Paasche Lower Bound**:
   Similarly, evaluating the true cost of living relative to current-period utility u_t yields:
   $$P_K(p_t, p_0; u_t) \ge \frac{p_t^T q_t}{p_0^T q_t} = P_P$$
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
   $$\ln P_T = \sum_{i=1}^N \frac{w_{i0} + w_{it}}{2} \ln\left( \frac{p_{it}}{p_{i0}} \right)$$
   $$P_T = \prod_{i=1}^N \left( \frac{p_{it}}{p_{i0}} \right)^{\frac{w_{i0} + w_{it}}{2}}$$
   Diewert proved that the Törnqvist index is exact for the transcendental logarithmic (translog) expenditure function.

Because both Fisher and Törnqvist indices allow consumer expenditure weights to adapt smoothly to price changes, they virtually eliminate the substitution bias that plagues the fixed-basket Laspeyres Consumer Price Index.

### Hedonic Quality Adjustment and Scanner Data Innovations
In modern digital economies, goods undergo rapid technological improvement: a modern personal computer or smartphone may cost the same nominal price as a model sold five years ago, but it features ten times the processing speed, memory, and photographic resolution. If statistical agencies simply record the nominal price, they drastically overstate true inflation because they ignore the colossal expansion in product quality.

To resolve this challenge, Zvi Griliches (1961, 1971) formalized **Hedonic Price Regression**:

$$\ln p_i = \beta_0 + \sum_{k=1}^K \beta_k z_{ik} + \varepsilon_i$$

where z_{ik} denotes the k-th physical characteristic of good i (e.g., processor speed, RAM, screen resolution, vehicle horsepower). The regression coefficient beta_k represents the marginal implicit shadow price of characteristic k. Statistical agencies use hedonic regressions to decompose observed price changes into a pure quality change component and a residual pure inflation component, ensuring that consumer price indices track true utility costs rather than technological upgrading.
"""

u1 = u1.replace("## Fully worked question 1", u1_extra + "\n## Fully worked question 1")
(OUT_DIR / "unit-1.md").write_text(u1, encoding="utf-8")
print(f"Updated Unit 1: {prose_count(u1)} words")

# ==============================================================================
# UNIT 2: Axiomatic Tests of Index Numbers & Cost-of-Living Metrics
# ==============================================================================
u2_content = """# Unit 2: Axiomatic Tests of Index Numbers & Cost-of-Living Metrics

The construction of price and quantity index numbers has inspired intense mathematical debates regarding what logical properties a reliable index formula must satisfy. In his monumental 1922 treatise *The Making of Index Numbers*, Irving Fisher examined over one hundred and eighty distinct mathematical index formulas, subjecting each to a rigorous battery of axiomatic tests. Fisher demonstrated that almost all classical index numbers fail elementary consistency tests, and identified the unique mathematical properties that elevate the Fisher Ideal Index above its competitors. In this unit, we formalize Fisher's axiomatic tests, prove Wald's impossibility theorem, and analyze practical macroeconomic cost-of-living metrics, consumer price indices, purchasing power deflators, and real wage dynamics.

## 2.1 Irving Fisher's Axiomatic Criteria for Index Numbers

Fisher's axiomatic (test) approach treats an index number formula $P(p_0, q_0, p_t, q_t)$ as a mathematical operator, evaluating whether it satisfies fundamental geometric, dimensional, and temporal consistency axioms.

### 1. The Identity Test (Commodity Monotonicity)
If prices in the current period remain identical to prices in the base period for every single commodity ($p_{it} = p_{i0}$ for all $i$), the price index must equal unity (or 100):

$$P(p_0, q_0, p_0, q_t) = 1.000$$

All standard index formulas (Laspeyres, Paasche, Fisher, Marshall-Edgeworth, Törnqvist) trivially satisfy the Identity Test.

### 2. The Proportionality Test
If all commodity prices in the current period change by a constant scalar multiple $\\lambda > 0$ relative to the base period ($p_{it} = \\lambda \\cdot p_{i0}$ for all $i$), the price index must equal that exact scalar multiple:

$$P(p_0, q_0, \\lambda p_0, q_t) = \\lambda$$

All standard weighted aggregative indices satisfy the Proportionality Test.

### 3. The Dimensionality (Unit) Test
The numerical value of the price index must be completely invariant to changes in the physical units of measurement used for commodities (e.g., quoting wheat in kilograms versus metric tons, or petroleum in liters versus barrels) and changes in the monetary currency units (e.g., dollars versus cents).

Let $\\alpha_i > 0$ denote physical scale factors and $\\beta > 0$ denote monetary scale factors. The Unit Test requires:

$$P(\\beta p_0 \\mathbf{D}_\\alpha, \\mathbf{D}_\\alpha^{-1} q_0, \\beta p_t \\mathbf{D}_\\alpha, \\mathbf{D}_\\alpha^{-1} q_t) = P(p_0, q_0, p_t, q_t)$$

where $\\mathbf{D}_\\alpha = \\text{diag}(\\alpha_1, \\dots, \\alpha_N)$.
As established in Unit 1, simple unweighted aggregative indices fail the Unit Test, whereas all weighted aggregative indices (Laspeyres, Paasche, Fisher, Marshall-Edgeworth) satisfy the Unit Test.

### 4. The Time Reversal Test (TRT)
The Time Reversal Test is among the most celebrated axiomatic criteria in economic statistics. It requires that the index number formula possess temporal symmetry: if the temporal direction of the comparison is reversed (treating current period $t$ as the base and base period $0$ as the current period), the resulting backward index must be the exact mathematical reciprocal of the forward index.

Let $P_{0t}$ denote the price index measuring price change from base period $0$ to current period $t$.
Let $P_{t0}$ denote the index computed using the exact same mathematical formula, but interchanging the roles of periods $0$ and $t$ (replacing $p_0$ with $p_t$, $p_t$ with $p_0$, $q_0$ with $q_t$, and $q_t$ with $q_0$).
The **Time Reversal Test** requires:

$$P_{0t} \\times P_{t0} = 1.000 \\iff P_{t0} = \\frac{1}{P_{0t}}$$

If an index indicates that prices doubled ($P_{0t} = 2.0$) from period 0 to period $t$, then evaluating price change backward from period $t$ to period 0 must indicate that prices were halved ($P_{t0} = 0.5$). An index that fails this test exhibits temporal asymmetry, systematically introducing an artificial directional drift.

### 5. The Factor Reversal Test (FRT)
The Factor Reversal Test requires that the product of a price index formula and its corresponding quantity index formula must equal the true **Value Relative Ratio** of total consumer expenditure between the two periods.

Let $V_{0t} = \\frac{\\sum_{i=1}^N p_{it} q_{it}}{\\sum_{i=1}^N p_{i0} q_{i0}}$ denote the true expenditure value ratio.
Let $Q_{0t}$ denote the quantity index obtained by interchanging the symbols $p$ and $q$ in the price index formula (replacing prices with quantities and quantities with prices).
The **Factor Reversal Test** requires:

$$P_{0t} \\times Q_{0t} = \\frac{\\sum p_t q_t}{\\sum p_0 q_0} = V_{0t}$$

Just as Price multiplied by Quantity equals Total Expenditure for an individual commodity ($p \\cdot q = v$), the macroeconomic Price Index multiplied by the Quantity Index must completely exhaust total expenditure change, leaving zero unexplained residual.

### 6. The Circular Test (Transitivity Test)
The Circular Test generalizes the Time Reversal Test across three or more time periods. It requires that direct comparison between period $0$ and period $2$ must equal the chained product of the intermediate comparisons:

$$P_{01} \\times P_{12} \\times P_{20} = 1.000 \\iff P_{02} = P_{01} \\times P_{12}$$

The Circular Test guarantees that a multi-period comparison is independent of the intermediate geographic or temporal routing.

## 2.2 Mathematical Proofs of Axiomatic Reversal Tests

We now present the formal mathematical proofs establishing which classical index numbers satisfy or fail Fisher's reversal tests.

### Proof: The Laspeyres Index Fails the Time Reversal Test
Recall the forward Laspeyres price index:
$$P_{0t}^L = \\frac{\\sum p_t q_0}{\\sum p_0 q_0}$$
Interchange periods $0$ and $t$ to obtain the backward Laspeyres index $P_{t0}^L$:
$$P_{t0}^L = \\frac{\\sum p_0 q_t}{\\sum p_t q_t}$$
Multiply the forward and backward indices:
$$P_{0t}^L \\times P_{t0}^L = \\left( \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\right) \\times \\left( \\frac{\\sum p_0 q_t}{\\sum p_t q_t} \\right) = \\frac{(\\sum p_t q_0) (\\sum p_0 q_t)}{(\\sum p_0 q_0) (\\sum p_t q_t)}$$
In general, $(\\sum p_t q_0) (\\sum p_0 q_t) \\ne (\\sum p_0 q_0) (\\sum p_t q_t)$.
Therefore:
$$P_{0t}^L \\times P_{t0}^L \\ne 1$$
The Laspeyres price index **fails the Time Reversal Test**.

### Proof: The Paasche Index Fails the Time Reversal Test
Recall the forward Paasche index:
$$P_{0t}^P = \\frac{\\sum p_t q_t}{\\sum p_0 q_t}$$
Interchange periods $0$ and $t$:
$$P_{t0}^P = \\frac{\\sum p_0 q_0}{\\sum p_t q_0}$$
Multiply the two indices:
$$P_{0t}^P \\times P_{t0}^P = \\left( \\frac{\\sum p_t q_t}{\\sum p_0 q_t} \\right) \\times \\left( \\frac{\\sum p_0 q_0}{\\sum p_t q_0} \\right) = \\frac{(\\sum p_t q_t) (\\sum p_0 q_0)}{(\\sum p_0 q_t) (\\sum p_t q_0)} \\ne 1$$
The Paasche price index **fails the Time Reversal Test**.
Notice that:
$$P_{0t}^L \\times P_{t0}^P = \\left( \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\right) \\times \\left( \\frac{\\sum p_0 q_0}{\\sum p_t q_0} \\right) = 1.000$$
The reciprocal of the forward Laspeyres index is the backward Paasche index!

### Formal Proof: Fisher's Ideal Index Satisfies the Time Reversal Test
Recall Fisher's Ideal Index:
$$P_{0t}^F = \\sqrt{ \\left( \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\right) \\left( \\frac{\\sum p_t q_t}{\\sum p_0 q_t} \\right) }$$
Interchange periods $0$ and $t$ to obtain the backward Fisher index:
$$P_{t0}^F = \\sqrt{ \\left( \\frac{\\sum p_0 q_t}{\\sum p_t q_t} \\right) \\left( \\frac{\\sum p_0 q_0}{\\sum p_t q_0} \\right) }$$
Multiply the forward and backward Fisher indices:
$$P_{0t}^F \\times P_{t0}^F = \\sqrt{ \\left( \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\right) \\left( \\frac{\\sum p_t q_t}{\\sum p_0 q_t} \\right) \\times \\left( \\frac{\\sum p_0 q_t}{\\sum p_t q_t} \\right) \\left( \\frac{\\sum p_0 q_0}{\\sum p_t q_0} \\right) }$$
Rearrange the terms inside the square root:
$$P_{0t}^F \\times P_{t0}^F = \\sqrt{ \\left( \\frac{\\sum p_t q_0}{\\sum p_t q_0} \\right) \\times \\left( \\frac{\\sum p_0 q_0}{\\sum p_0 q_0} \\right) \\times \\left( \\frac{\\sum p_t q_t}{\\sum p_t q_t} \\right) \\times \\left( \\frac{\\sum p_0 q_t}{\\sum p_0 q_t} \\right) } = \\sqrt{1 \\times 1 \\times 1 \\times 1} = 1.000$$
Therefore:
$$P_{0t}^F \\times P_{t0}^F = 1.000 \\iff P_{t0}^F = \\frac{1}{P_{0t}^F}$$
Fisher's Ideal Index **strictly satisfies the Time Reversal Test**. $\\blacksquare$

### Proof: The Laspeyres and Paasche Indices Fail the Factor Reversal Test
For the Laspeyres index, interchanging $p$ and $q$ gives the Laspeyres quantity index:
$$Q_{0t}^L = \\frac{\\sum q_t p_0}{\\sum q_0 p_0} = \\frac{\\sum p_0 q_t}{\\sum p_0 q_0}$$
Multiply price index by quantity index:
$$P_{0t}^L \\times Q_{0t}^L = \\left( \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\right) \\times \\left( \\frac{\\sum p_0 q_t}{\\sum p_0 q_0} \\right) = \\frac{(\\sum p_t q_0) (\\sum p_0 q_t)}{(\\sum p_0 q_0)^2} \\ne \\frac{\\sum p_t q_t}{\\sum p_0 q_0}$$
Laspeyres **fails the Factor Reversal Test**.

Similarly, for the Paasche index:
$$Q_{0t}^P = \\frac{\\sum q_t p_t}{\\sum q_0 p_t} = \\frac{\\sum p_t q_t}{\\sum p_t q_0}$$
$$P_{0t}^P \\times Q_{0t}^P = \\left( \\frac{\\sum p_t q_t}{\\sum p_0 q_t} \\right) \\times \\left( \\frac{\\sum p_t q_t}{\\sum p_t q_0} \\right) = \\frac{(\\sum p_t q_t)^2}{(\\sum p_0 q_t) (\\sum p_t q_0)} \\ne \\frac{\\sum p_t q_t}{\\sum p_0 q_0}$$
Paasche **fails the Factor Reversal Test**.

### Formal Proof: Fisher's Ideal Index Satisfies the Factor Reversal Test
Recall Fisher's price index:
$$P_{0t}^F = \\sqrt{ \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\times \\frac{\\sum p_t q_t}{\\sum p_0 q_t} }$$
Interchanging the symbols $p$ and $q$ yields Fisher's quantity index:
$$Q_{0t}^F = \\sqrt{ \\frac{\\sum q_t p_0}{\\sum q_0 p_0} \\times \\frac{\\sum q_t p_t}{\\sum q_0 p_t} } = \\sqrt{ \\frac{\\sum p_0 q_t}{\\sum p_0 q_0} \\times \\frac{\\sum p_t q_t}{\\sum p_t q_0} }$$
Multiply the price index and quantity index:
$$P_{0t}^F \\times Q_{0t}^F = \\sqrt{ \\left( \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\times \\frac{\\sum p_t q_t}{\\sum p_0 q_t} \\right) \\times \\left( \\frac{\\sum p_0 q_t}{\\sum p_0 q_0} \\times \\frac{\\sum p_t q_t}{\\sum p_t q_0} \\right) }$$
Notice the remarkable cross-cancellations:
- The term $\\sum p_t q_0$ in the first numerator cancels with $\\sum p_t q_0$ in the second denominator.
- The term $\\sum p_0 q_t$ in the second numerator cancels with $\\sum p_0 q_t$ in the first denominator.
The product simplifies to:
$$P_{0t}^F \\times Q_{0t}^F = \\sqrt{ \\frac{(\\sum p_t q_t)^2}{(\\sum p_0 q_0)^2} } = \\frac{\\sum p_t q_t}{\\sum p_0 q_0} = V_{0t}$$
Fisher's Ideal Index **strictly satisfies the Factor Reversal Test**. $\\blacksquare$

### Proof: The Marshall–Edgeworth Index Satisfies TRT but Fails FRT
Recall the Marshall–Edgeworth index:
$$P_{0t}^{ME} = \\frac{\\sum p_t (q_0 + q_t)}{\\sum p_0 (q_0 + q_t)} = \\frac{\\sum p_t q_0 + \\sum p_t q_t}{\\sum p_0 q_0 + \\sum p_0 q_t}$$
Interchanging periods $0$ and $t$:
$$P_{t0}^{ME} = \\frac{\\sum p_0 (q_t + q_0)}{\\sum p_t (q_t + q_0)} = \\frac{\\sum p_0 q_t + \\sum p_0 q_0}{\\sum p_t q_t + \\sum p_t q_0}$$
Notice that the numerator of $P_{t0}^{ME}$ is identically the denominator of $P_{0t}^{ME}$, and the denominator of $P_{t0}^{ME}$ is identically the numerator of $P_{0t}^{ME}$!
$$P_{0t}^{ME} \\times P_{t0}^{ME} = \\left( \\frac{\\sum p_t q_0 + \\sum p_t q_t}{\\sum p_0 q_0 + \\sum p_0 q_t} \\right) \\times \\left( \\frac{\\sum p_0 q_0 + \\sum p_0 q_t}{\\sum p_t q_0 + \\sum p_t q_t} \\right) = 1.000$$
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
   $$CPI = \\frac{\\sum p_t q_0}{\\sum p_0 q_0} \\times 100$$
   where $q_0$ represents the quantities consumed in a benchmark Household Income and Expenditure Survey (HIES).

2. **The Family Budget Method (Weighted Average of Price Relatives)**:
   $$CPI = \\frac{\\sum W_i R_i}{\\sum W_i} = \\frac{\\sum (p_0 q_0) \\left( \\frac{p_t}{p_0} \\right)}{\\sum p_0 q_0} \\times 100$$
   where $R_i = \\frac{p_{it}}{p_{i0}} \\times 100$ is the price relative for commodity $i$, and $W_i = p_{i0} q_{i0}$ is the base-period expenditure incurred by the average family on commodity $i$.
   The Aggregate Expenditure Method and Family Budget Method yield **identical numerical results**.

## 2.5 Macroeconomic Applications: Deflating, Real Wages, and Purchasing Power

Index numbers provide the indispensable mathematical tools for converting nominal monetary statistics into real, inflation-adjusted purchasing power metrics.

### 1. Deflating Nominal Economic Series
To evaluate whether an economic magnitude (such as national retail sales, manufacturing shipments, or government tax revenues) has grown in genuine physical volume or merely through price inflation, analysts **deflate** the series:

$$\\text{Real Value} = \\frac{\\text{Nominal Value}}{\\text{Price Index}} \\times 100$$

### 2. Purchasing Power of Money (PPM)
The purchasing power of a currency unit (e.g., dollar or taka) measures the quantity of goods and services that one unit of currency can buy. It is the exact reciprocal of the price index:

$$PPM = \\frac{1}{CPI} \\times 100$$

If the Consumer Price Index rises from $100$ to $125$ (a $25\\%$ inflation rate), the purchasing power of money becomes:

$$PPM = \\frac{1}{125} \\times 100 = 0.80 \\implies 80.0\\%$$

The currency has lost $20\\%$ of its real purchasing power.

### 3. Real Wages and the Real Wage Index
Let $W_{\\text{nom}}$ denote the nominal monetary wage earned by an industrial worker, and let $CPI$ denote the consumer price index.
The **Real Wage** is:

$$W_{\\text{real}} = \\frac{W_{\\text{nom}}}{CPI} \\times 100$$

The **Real Wage Index ($RWI$)** measures relative changes in workers' standard of living:

$$RWI = \\frac{\\text{Money Wage Index}}{CPI} \\times 100$$

If nominal wages increase by $10\\%$ while the $CPI$ surges by $15\\%$:
$$RWI = \\frac{110}{115} \\times 100 \\approx 95.65$$
Although the worker takes home $10\\%$ more paper currency, their real standard of living has fallen by $4.35\\%$.

## Fully worked question 1: Mathematical Verification of Fisher's Time and Factor Reversal Tests

### Question
An econometric auditing bureau evaluates price and quantity indices across three industrial raw materials: Copper ($A$), Aluminum ($B$), and Nickel ($C$). The recorded prices per metric ton and transaction volumes across base year ($0$) and current year ($t$) are:

| Material | Base Price ($p_0$) | Base Quantity ($q_0$) | Current Price ($p_t$) | Current Quantity ($q_t$) |
| :---: | :---: | :---: | :---: | :---: |
| **A (Copper)** | $8{,}000$ | $50$ | $10{,}000$ | $60$ |
| **B (Aluminum)** | $2{,}000$ | $120$ | $2{,}500$ | $100$ |
| **C (Nickel)** | $15{,}000$ | $20$ | $18{,}000$ | $25$ |

1. Calculate the four primary expenditure cross-products: $\\sum p_0 q_0, \\sum p_t q_0, \\sum p_0 q_t,$ and $\\sum p_t q_t$.
2. Compute the forward Laspeyres, Paasche, and Fisher price indices ($P_{0t}^L, P_{0t}^P, P_{0t}^F$).
3. Test whether the Laspeyres index and Fisher's Ideal Index satisfy the Time Reversal Test ($P_{0t} \\times P_{t0} = 1$).
4. Compute the Fisher quantity index ($Q_{0t}^F$) and verify that Fisher's Ideal Index satisfies the Factor Reversal Test ($P_{0t}^F \\times Q_{0t}^F = V_{0t}$).

### Solution, step 1: Compute Expenditure Cross-Products
1. **Base-Period Total Expenditure ($\\sum p_0 q_0$)**:
   - Copper: $8{,}000 \\times 50 = 400{,}000$
   - Aluminum: $2{,}000 \\times 120 = 240{,}000$
   - Nickel: $15{,}000 \\times 20 = 300{,}000$
   $$\\sum p_0 q_0 = 400{,}000 + 240{,}000 + 300{,}000 = 940{,}000$$

2. **Cost of Base Basket at Current Prices ($\\sum p_t q_0$)**:
   - Copper: $10{,}000 \\times 50 = 500{,}000$
   - Aluminum: $2{,}500 \\times 120 = 300{,}000$
   - Nickel: $18{,}000 \\times 20 = 360{,}000$
   $$\\sum p_t q_0 = 500{,}000 + 300{,}000 + 360{,}000 = 1{,}160{,}000$$

3. **Cost of Current Basket at Base Prices ($\\sum p_0 q_t$)**:
   - Copper: $8{,}000 \\times 60 = 480{,}000$
   - Aluminum: $2{,}000 \\times 100 = 200{,}000$
   - Nickel: $15{,}000 \\times 25 = 375{,}000$
   $$\\sum p_0 q_t = 480{,}000 + 200{,}000 + 375{,}000 = 1{,}055{,}000$$

4. **Current-Period Actual Expenditure ($\\sum p_t q_t$)**:
   - Copper: $10{,}000 \\times 60 = 600{,}000$
   - Aluminum: $2{,}500 \\times 100 = 250{,}000$
   - Nickel: $18{,}000 \\times 25 = 450{,}000$
   $$\\sum p_t q_t = 600{,}000 + 250{,}000 + 450{,}000 = 1{,}300{,}000$$

### Solution, step 2: Compute Price Indices
1. **Laspeyres Price Index ($P_{0t}^L$)**:
   $$P_{0t}^L = \\frac{\\sum p_t q_0}{\\sum p_0 q_0} = \\frac{1{,}160{,}000}{940{,}000} \\approx 1.234043 \\implies 123.40$$

2. **Paasche Price Index ($P_{0t}^P$)**:
   $$P_{0t}^P = \\frac{\\sum p_t q_t}{\\sum p_0 q_t} = \\frac{1{,}300{,}000}{1{,}055{,}000} \\approx 1.232227 \\implies 123.22$$

3. **Fisher's Ideal Price Index ($P_{0t}^F$)**:
   $$P_{0t}^F = \\sqrt{P_{0t}^L \\times P_{0t}^P} = \\sqrt{1.234043 \\times 1.232227} = \\sqrt{1.520621} \\approx 1.233135 \\implies 123.31$$

### Solution, step 3: Execution of the Time Reversal Test
1. **Test for Laspeyres Index**:
   The backward Laspeyres index is:
   $$P_{t0}^L = \\frac{\\sum p_0 q_t}{\\sum p_t q_t} = \\frac{1{,}055{,}000}{1{,}300{,}000} \\approx 0.811538$$
   Multiply forward and backward:
   $$P_{0t}^L \\times P_{t0}^L = 1.234043 \\times 0.811538 \\approx 1.001476 \\ne 1.000$$
   Because $1.001476 \\ne 1$, the Laspeyres index **fails the Time Reversal Test**.

2. **Test for Fisher's Ideal Index**:
   The backward Fisher index is:
   $$P_{t0}^F = \\sqrt{ \\left( \\frac{\\sum p_0 q_t}{\\sum p_t q_t} \\right) \\left( \\frac{\\sum p_0 q_0}{\\sum p_t q_0} \\right) } = \\sqrt{ \\frac{1{,}055{,}000}{1{,}300{,}000} \\times \\frac{940{,}000}{1{,}160{,}000} } = \\sqrt{0.811538 \\times 0.810345} = \\sqrt{0.657626} \\approx 0.810941$$
   Multiply forward and backward:
   $$P_{0t}^F \\times P_{t0}^F = 1.233135 \\times 0.810941 = 0.999999 \\approx 1.000$$
   Fisher's Ideal Index **satisfies the Time Reversal Test** with exact precision.

### Solution, step 4: Execution of the Factor Reversal Test
The true Expenditure Value Ratio is:

$$V_{0t} = \\frac{\\sum p_t q_t}{\\sum p_0 q_0} = \\frac{1{,}300{,}000}{940{,}000} \\approx 1.382979$$

Fisher's Quantity Index ($Q_{0t}^F$) is obtained by interchanging prices and quantities:

$$Q_{0t}^F = \\sqrt{ \\left( \\frac{\\sum q_t p_0}{\\sum q_0 p_0} \\right) \\left( \\frac{\\sum q_t p_t}{\\sum q_0 p_t} \\right) } = \\sqrt{ \\left( \\frac{\\sum p_0 q_t}{\\sum p_0 q_0} \\right) \\left( \\frac{\\sum p_t q_t}{\\sum p_t q_0} \\right) }$$

Substitute the numerical values:

$$Q_{0t}^F = \\sqrt{ \\frac{1{,}055{,}000}{940{,}000} \\times \\frac{1{,}300{,}000}{1{,}160{,}000} } = \\sqrt{1.122340 \\times 1.120690} = \\sqrt{1.257795} \\approx 1.121515 \\implies 112.15$$

Physical raw material transaction volume increased by $12.15\\%$.

Now multiply Fisher's Price Index by Fisher's Quantity Index:

$$P_{0t}^F \\times Q_{0t}^F = 1.233135 \\times 1.121515 \\approx 1.382979$$

Notice that:

$$P_{0t}^F \\times Q_{0t}^F = 1.382979 = V_{0t}$$

The product matches the true expenditure value ratio $V_{0t}$ to the sixth decimal place! Fisher's Ideal Index **strictly satisfies the Factor Reversal Test**.

## Fully worked question 2: Real Wage Deflation and Purchasing Power Dynamics

### Question
A labor economics research institute analyzes wages and retail price inflation for an industrial manufacturing workforce across a six-year period:

| Year | Monthly Nominal Wage ($W$) | Consumer Price Index ($CPI$) |
| :---: | :---: | :---: |
| **2019** | $\\$2{,}500$ | $100.0$ |
| **2020** | $\\$2{,}700$ | $105.0$ |
| **2021** | $\\$2{,}900$ | $112.0$ |
| **2022** | $\\$3{,}150$ | $126.0$ |
| **2023** | $\\$3{,}400$ | $140.0$ |
| **2024** | $\\$3{,}600$ | $150.0$ |

1. Calculate the Purchasing Power of the Dollar ($PPM$) in each year relative to the 2019 baseline.
2. Deflate the nominal monthly wages to compute the Real Monthly Wage ($W_{\\text{real}}$) at constant 2019 purchasing power for each year.
3. Construct the Nominal Money Wage Index ($MWI$) and the Real Wage Index ($RWI$) with $2019 = 100$. Evaluate whether workers experienced an improvement or deterioration in real material welfare between 2019 and 2024.

### Solution, step 1: Calculate Purchasing Power of Money (PPM)
The formula is $PPM = \\frac{100}{CPI}$:
- **2019**: $\\frac{100}{100.0} = 1.000 \\implies 100.0\\%$
- **2020**: $\\frac{100}{105.0} \\approx 0.9524 \\implies 95.24\\%$
- **2021**: $\\frac{100}{112.0} \\approx 0.8929 \\implies 89.29\\%$
- **2022**: $\\frac{100}{126.0} \\approx 0.7937 \\implies 79.37\\%$
- **2023**: $\\frac{100}{140.0} \\approx 0.7143 \\implies 71.43\\%$
- **2024**: $\\frac{100}{150.0} \\approx 0.6667 \\implies 66.67\\%$

By 2024, the currency lost one-third ($33.33\\%$) of its purchasing power due to price inflation.

### Solution, step 2: Calculate Real Wages at Constant 2019 Prices
The formula is $W_{\\text{real}} = \\frac{W_{\\text{nominal}}}{CPI} \\times 100$:
- **2019**: $\\frac{2{,}500}{100.0} \\times 100 = \\$2{,}500.00$
- **2020**: $\\frac{2{,}700}{105.0} \\times 100 = \\$2{,}571.43$
- **2021**: $\\frac{2{,}900}{112.0} \\times 100 = \\$2{,}589.29$
- **2022**: $\\frac{3{,}150}{126.0} \\times 100 = \\$2{,}500.00$
- **2023**: $\\frac{3{,}400}{140.0} \\times 100 = \\$2{,}428.57$
- **2024**: $\\frac{3{,}600}{150.0} \\times 100 = \\$2{,}400.00$

### Solution, step 3: Construct Indices and Synthesize Welfare Trajectory
1. **Nominal Money Wage Index ($MWI = \\frac{W_t}{W_{2019}} \\times 100$)**:
   - 2019: $\\frac{2{,}500}{2{,}500} \\times 100 = 100.00$
   - 2020: $\\frac{2{,}700}{2{,}500} \\times 100 = 108.00$
   - 2021: $\\frac{2{,}900}{2{,}500} \\times 100 = 116.00$
   - 2022: $\\frac{3{,}150}{2{,}500} \\times 100 = 126.00$
   - 2023: $\\frac{3{,}400}{2{,}500} \\times 100 = 136.00$
   - 2024: $\\frac{3{,}600}{2{,}500} \\times 100 = 144.00$

2. **Real Wage Index ($RWI = \\frac{W_{\\text{real}, t}}{W_{\\text{real}, 2019}} \\times 100 = \\frac{MWI}{CPI} \\times 100$)**:
   - 2019: $\\frac{2{,}500.00}{2{,}500.00} \\times 100 = 100.00$
   - 2020: $\\frac{2{,}571.43}{2{,}500.00} \\times 100 = 102.86$
   - 2021: $\\frac{2{,}589.29}{2{,}500.00} \\times 100 = 103.57$
   - 2022: $\\frac{2{,}500.00}{2{,}500.00} \\times 100 = 100.00$
   - 2023: $\\frac{2{,}428.57}{2{,}500.00} \\times 100 = 97.14$
   - 2024: $\\frac{2{,}400.00}{2{,}500.00} \\times 100 = 96.00$

**Economic Welfare Diagnosis**:
1. Between 2019 and 2021, nominal wage gains ($+16\\%$) outpaced inflation ($+12\\%$), expanding real wages to a peak of $\\$2{,}589.29$ ($RWI = 103.57$).
2. Between 2022 and 2024, inflation accelerated dramatically ($CPI$ surging from $112$ to $150$, a $33.9\\%$ jump), outstripping wage increases ($MWI$ rising from $116$ to $144$, a $24.1\\%$ jump).
3. By 2024, despite receiving $\\$3{,}600$ per month (a substantial $44.0\\%$ increase in paper currency), workers' real purchasing power had collapsed to $\\$2{,}400$ in 2019 purchasing power—a net **$4.0\\%$ decline in real material living standards** ($RWI = 96.00$). This exemplifies the classic **money illusion** in macroeconomics.

## Fully worked question 3: Consumer Price Index via Family Budget Method and Wage Compensation

### Question
A tripartite national labor conciliation board investigates cost-of-living adjustments for low-income industrial workers. A representative Household Expenditure Survey establishes the consumption weights and commodity price relatives between base year $2018$ and current year $2024$:

| Expenditure Category | Base Expenditure Weight ($W_i = p_0 q_0$) | 2018 Price ($p_0$) | 2024 Price ($p_t$) |
| :---: | :---: | :---: | :---: |
| **1. Cereals & Food** | $\\$4{,}000$ | $\\$20.00$ | $\\$32.00$ |
| **2. Housing Rent** | $\\$2{,}500$ | $\\$500.00$ | $\\$700.00$ |
| **3. Fuel & Lighting** | $\\$1{,}000$ | $\\$50.00$ | $\\$80.00$ |
| **4. Clothing** | $\\$1{,}500$ | $\\$100.00$ | $\\$125.00$ |
| **5. Miscellaneous Services** | $\\$1{,}000$ | $\\$40.00$ | $\\$60.00$ |

1. Calculate the price relatives ($R_i = \frac{p_t}{p_0} \times 100$) for each expenditure category.
2. Calculate the Consumer Price Index ($CPI$) for 2024 ($2018 = 100$) using the Family Budget Method: $CPI = \frac{\sum W_i R_i}{\sum W_i}$.
3. If an industrial worker earned a monthly wage of $\\$500.00$ in 2018, determine the minimum nominal wage that must be paid in 2024 to fully insulate the worker from cost-of-living increases, and compute the required Dearness Allowance (DA).

### Solution, step 1: Calculate Price Relatives ($R_i$)
The price relative formula is $R_i = \frac{p_t}{p_0} \times 100$:
1. **Cereals & Food**:
   $$R_1 = \frac{32.00}{20.00} \times 100 = 160.00$$
2. **Housing Rent**:
   $$R_2 = \frac{700.00}{500.00} \times 100 = 140.00$$
3. **Fuel & Lighting**:
   $$R_3 = \frac{80.00}{50.00} \times 100 = 160.00$$
4. **Clothing**:
   $$R_4 = \frac{125.00}{100.00} \times 100 = 125.00$$
5. **Miscellaneous**:
   $$R_5 = \frac{60.00}{40.00} \times 100 = 150.00$$

### Solution, step 2: Compute CPI via Family Budget Method
We evaluate the weighted products $W_i \times R_i$:
- Food: $4{,}000 \times 160.00 = 640{,}000$
- Rent: $2{,}500 \times 140.00 = 350{,}000$
- Fuel: $1{,}000 \times 160.00 = 160{,}000$
- Clothing: $1{,}500 \times 125.00 = 187{,}500$
- Misc: $1{,}000 \times 150.00 = 150{,}000$

Summing the weights:
$$\sum W_i = 4{,}000 + 2{,}500 + 1{,}000 + 1{,}500 + 1{,}000 = 10{,}000$$

Summing the weighted products:
$$\sum (W_i R_i) = 640{,}000 + 350{,}000 + 160{,}000 + 187{,}500 + 150{,}000 = 1{,}487{,}500$$

The Consumer Price Index is:

$$CPI = \frac{\sum (W_i R_i)}{\sum W_i} = \frac{1{,}487{,}500}{10{,}000} = 148.75$$

The cost of living for industrial workers rose by **$48.75\%$** between 2018 and 2024.

### Solution, step 3: Wage Indexation and Dearness Allowance Calculation
The baseline wage in 2018 was $W_0 = \$500.00$.
To maintain real purchasing power, the compensated 2024 wage $W_t$ must satisfy:

$$W_t = W_0 \times \left( \frac{CPI}{100} \right) = \$500.00 \times \left( \frac{148.75}{100} \right) = \$500.00 \times 1.4875 = \$743.75$$

The required monthly nominal wage in 2024 is **$\$743.75$**.

The required **Dearness Allowance (DA)**—the compensatory cash supplement added to basic pay—is:

$$\text{DA} = W_t - W_0 = \$743.75 - \$500.00 = \$243.75 \text{ per month}$$

Expressed as a percentage of basic wage:
$$\text{DA Rate} = \frac{\$243.75}{\$500.00} \times 100 = 48.75\%$$

Paying a monthly Dearness Allowance of $\$243.75$ exactly neutralizes the $48.75\%$ rise in the consumer price index, fully preserving the worker's real standard of living.
"""

(OUT_DIR / "unit-2.md").write_text(u2_content, encoding="utf-8")
print(f"Unit 2: {prose_count(u2_content)} words")
