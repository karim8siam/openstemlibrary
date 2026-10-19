# Unit 5: Income Distribution, Economic Inequality & Poverty Measurement

## Statistical Analysis of Income and Wealth Distribution

The mathematical study of personal income and wealth distribution forms a cornerstone of welfare economics and social policy. In an economy, aggregate production and national income may expand substantially, yet if gains accrue disproportionately to an elite minority, broad societal well-being and social cohesion may deteriorate. Statistical economics provides the formal analytical toolkit to quantify the size distribution of income, evaluate the degree of economic inequality, and measure the depth and severity of poverty.

In empirical microeconomics, the **Size Distribution of Income** arranges individual earners or households into ordered income brackets regardless of the institutional source of income (wages, profits, rents, or transfer payments). The resulting empirical income distributions invariably exhibit pronounced positive skewness (right-skewed): the vast majority of citizens cluster at low-to-moderate income levels, while an extended tail stretches into extremely high income brackets. Consequently, the arithmetic mean income $\bar{x}$ systematically exceeds the median income $x_{\text{med}}$, rendering standard symmetric Gaussian distributions inapplicable.

---

## Pareto's Law of Income Distribution

In 1897, the Italian mathematical economist and sociologist Vilfredo Pareto published his seminal empirical investigation into the upper tail of income distributions across European nations. Pareto discovered a striking empirical regularity: the number of individuals possessing an income greater than or equal to a specified threshold $x$ follows a power-law decay.

### Mathematical Formulation
Pareto's Law is formulated as:

$$N(x) = A x^{-\alpha}, \quad x \ge x_0 > 0$$

where:
- $x$ represents the level of income.
- $N(x)$ denotes the number of individuals earning an income of at least $x$.
- $x_0$ denotes the lower truncation threshold (the minimum subsistence income above which the power law holds).
- $A$ is a positive scale parameter proportional to total population size ($A = N x_0^\alpha$).
- $\alpha$ is the **Pareto Index** (or Pareto coefficient), a dimensionless shape parameter governing the speed of income decay.

Taking natural logarithms of both sides converts Pareto's equation into a linear specification:

$$\ln[N(x)] = \ln(A) - \alpha \ln(x)$$

When plotted on a double-logarithmic scale with $\ln(x)$ on the horizontal axis and $\ln[N(x)]$ on the vertical axis, Pareto's Law traces a downward-sloping straight line with constant slope $-\alpha$.

### Probability Density Function and Moments
Normalized as a continuous probability distribution for a continuous random income variable $X \in [x_0, \infty)$, the **Cumulative Distribution Function (CDF)** is:

$$F(x) = P(X \le x) = 1 - \left( \frac{x_0}{x} \right)^\alpha$$

The complementary CDF (survival function) is:
$$S(x) = 1 - F(x) = \left( \frac{x_0}{x} \right)^\alpha$$

Differentiating $F(x)$ with respect to $x$ yields the **Probability Density Function (PDF)**:

$$f(x) = \frac{dF(x)}{dx} = \frac{\alpha x_0^\alpha}{x^{\alpha + 1}}, \quad x \ge x_0$$

#### The Expected Value (Mean Income):
The theoretical arithmetic mean income $\bar{x} = E[X]$ is given by:

$$E[X] = \int_{x_0}^{\infty} x f(x) dx = \alpha x_0^\alpha \int_{x_0}^{\infty} x^{-\alpha} dx$$

Evaluating this improper integral:
$$\int_{x_0}^{\infty} x^{-\alpha} dx = \left[ \frac{x^{1-\alpha}}{1-\alpha} \right]_{x_0}^{\infty} = \frac{x_0^{1-\alpha}}{\alpha - 1} \quad \text{provided } \alpha > 1$$

Thus, the theoretical mean income is:

$$E[X] = \frac{\alpha}{\alpha - 1} x_0, \quad \alpha > 1$$

If $\alpha \le 1$, the integral diverges to infinity, indicating that the income distribution possesses an infinite mean—a condition reflecting hyper-concentrated aristocratic or plutocratic wealth. In empirical modern economies, $\alpha$ typically ranges between 1.5 and 2.5.

#### The Median Income:
The median income $x_{\text{med}}$ satisfies $F(x_{\text{med}}) = 0.50$:

$$1 - \left( \frac{x_0}{x_{\text{med}}} \right)^\alpha = 0.50 \implies \left( \frac{x_0}{x_{\text{med}}} \right)^\alpha = 0.50 \implies x_{\text{med}} = x_0 2^{1/\alpha}$$

Because $2^{1/\alpha} < \frac{\alpha}{\alpha - 1}$ for all $\alpha > 1$, the median is strictly less than the mean: $x_{\text{med}} < E[X]$, confirming the deep positive skewness of the Pareto distribution.

#### Economic Interpretation of $\alpha$:
The parameter $\alpha$ is an inverse measure of income inequality:
- A large $\alpha$ (e.g., $\alpha \ge 2.5$) signifies rapid decay in the upper tail, meaning very few individuals possess extreme fortunes, which corresponds to greater equality.
- A small $\alpha$ (e.g., $\alpha \to 1$) signifies a fat upper tail where vast wealth is concentrated among a tiny oligarchy, indicating severe inequality.

---

## The Lorenz Curve

Introduced by American statistician Max Otto Lorenz in 1905, the **Lorenz Curve** is the universal graphical and mathematical device used to visualize and analyze economic inequality.

### Continuous Mathematical Definition
Let $f(x)$ be the probability density function of income with finite positive mean $\mu = \int_0^\infty x f(x) dx$.
For any given income cutoff $x^*$:
1. The **Cumulative Proportion of Population** earning income up to $x^*$ is:
   $$p(x^*) = \int_0^{x^*} f(x) dx = F(x^*), \quad p \in [0, 1]$$
2. The **Cumulative Proportion of Total National Income** earned by those individuals is:
   $$q(x^*) = \frac{1}{\mu} \int_0^{x^*} x f(x) dx, \quad q \in [0, 1]$$

Eliminating the intermediate threshold parameter $x^*$ defines the Lorenz curve as the continuous functional relationship:

$$q = L(p), \quad p \in [0, 1]$$

### Fundamental Mathematical Properties of the Lorenz Curve:
1. **Boundary Conditions**:
   $$L(0) = 0 \quad \text{and} \quad L(1) = 1$$
   Zero percent of the population earns zero percent of income, and 100 percent of the population earns 100 percent of income.
2. **First Derivative (Monotonicity)**:
   By the chain rule of calculus:
   $$\frac{dL}{dp} = \frac{dq / dx^*}{dp / dx^*} = \frac{\frac{x^* f(x^*)}{\mu}}{f(x^*)} = \frac{x^*}{\mu} \ge 0$$
   The slope of the Lorenz curve at any point $p$ is equal to the ratio of the marginal individual's income $x^*$ to the national mean income $\mu$.
3. **Second Derivative (Convexity)**:
   $$\frac{d^2 L}{dp^2} = \frac{d}{dp} \left( \frac{x^*}{\mu} \right) = \frac{1}{\mu} \frac{dx^*}{dp} = \frac{1}{\mu f(x^*)} > 0$$
   Because $\mu > 0$ and $f(x^*) > 0$, the second derivative is strictly positive everywhere. Hence, the Lorenz curve is strictly convex (bowed downward toward the horizontal axis).
4. **The Line of Perfect Equality**:
   If every individual in society earned the exact same income ($x = \mu$), then $x^* / \mu = 1$ everywhere, yielding $L(p) = p$. The 45-degree diagonal connecting $(0,0)$ to $(1,1)$ represents the **Line of Absolute Equality**.
5. **The Line of Absolute Inequality**:
   If a single individual captured the entire national income while the remaining population earned zero, $L(p) = 0$ for all $p \in [0, 1)$ and $L(1) = 1$. The Lorenz curve coincides with the lower horizontal axis and the vertical boundary.

---

## The Gini Concentration Coefficient

Formulated by Italian statistician Corrado Gini in 1912, the **Gini Coefficient ($G$)** is the most widely cited scalar measure of income inequality.

### 1. Geometric Definition via the Lorenz Curve
In the unit square $[0, 1] \times [0, 1]$, the total area under the 45-degree line of perfect equality is:
$$\text{Area of Triangle } OAB = \frac{1}{2} \times 1 \times 1 = \frac{1}{2}$$

Let $B$ represent the area lying directly underneath the Lorenz curve:
$$B = \int_0^1 L(p) dp$$

Let $A$ represent the area of the concentration lens enclosed between the 45-degree line of equality and the Lorenz curve:
$$A = \frac{1}{2} - B = \int_0^1 [p - L(p)] dp$$

The Gini coefficient is defined as the ratio of area $A$ to the total area under the line of equality ($1/2$):

$$G = \frac{A}{A + B} = \frac{\frac{1}{2} - B}{\frac{1}{2}} = 1 - 2 B = 1 - 2 \int_0^1 L(p) dp$$

- **Boundedness**: $0 \le G \le 1$.
  - $G = 0$ indicates perfect equality ($L(p) = p$).
  - $G = 1$ indicates total inequality ($L(p) = 0$ for $p < 1$).
  - In national economies, Gini coefficients range from approximately 0.24 (egalitarian Nordic nations) to over 0.60 (highly unequal developing or transition economies).

### 2. Gini from the Pareto Distribution
If income follows a continuous Pareto distribution with parameter $\alpha > 1$, the continuous Lorenz curve takes the explicit closed functional form:
$$L(p) = 1 - (1 - p)^{(\alpha - 1) / \alpha}$$

Integrating $L(p)$ over $[0, 1]$:
$$\int_0^1 L(p) dp = \int_0^1 \left[ 1 - (1-p)^{1 - 1/\alpha} \right] dp = 1 - \frac{1}{2 - 1/\alpha} = 1 - \frac{\alpha}{2\alpha - 1}$$

Substituting into the Gini formula:
$$G = 1 - 2 \left( 1 - \frac{\alpha}{2\alpha - 1} \right) = \frac{2\alpha}{2\alpha - 1} - 1 = \frac{1}{2\alpha - 1}$$

This closed-form formula illustrates the inverse relationship: as $\alpha \to 1$, $G \to 1$ (complete inequality); as $\alpha \to \infty$, $G \to 0$ (complete equality).

### 3. Gini from Grouped Empirical Data (Trapezoidal Rule)
When analyzing census or household income surveys grouped into $K$ discrete fractiles (e.g., quintiles, deciles), the empirical Lorenz curve is a piecewise linear polygon connecting coordinates $(p_i, q_i)$ for $i = 0, 1, \dots, K$, with $(p_0, q_0) = (0, 0)$ and $(p_K, q_K) = (1, 1)$.

The area under the piecewise linear Lorenz curve is the sum of $K$ trapezoids:
$$B = \sum_{i=1}^{K} \frac{q_{i-1} + q_i}{2} (p_i - p_{i-1})$$

The Gini coefficient is computed via the **Brown Formula**:

$$G = 1 - \sum_{i=1}^{K} (p_i - p_{i-1})(q_{i-1} + q_i)$$

For equal decile groupings where each fractile represents an equal population share $p_i - p_{i-1} = 1/K$:
$$G = 1 - \frac{1}{K} \sum_{i=1}^{K} (q_{i-1} + q_i)$$

---

## Statistical Measurement of Poverty

While inequality measures dispersion across the entire income spectrum, **Poverty Measurement** focuses on the left tail—identifying individuals whose economic resources fall below a socially or biologically defined subsistence standard: the **Poverty Line ($z$)**.

### 1. The Headcount Ratio ($H$)
The Headcount Ratio is the simplest and most widespread metric. Let $N$ be the total population, and let $Q$ denote the number of poor individuals whose income or consumption expenditure $y_i$ falls strictly below the poverty line ($y_i < z$):

$$H = \frac{Q}{N}$$

**Limitation**: The Headcount Ratio captures only the incidence of poverty. It is completely insensitive to the depth of poverty: if a catastrophic shock halves the income of already destitute individuals, $H$ remains unchanged. Furthermore, it violates the Pigou-Dalton transfer principle: a regressive cash transfer from a destitute person to a marginally poor person that pushes the latter above $z$ paradoxically causes $H$ to decrease.

### 2. The Income Poverty Gap Ratio ($I$) and Poverty Gap Index ($\text{PGI}$)
To incorporate depth, the **Income Gap Ratio ($I$)** measures the average proportional shortfall of the poor from the poverty line:

$$I = \frac{1}{Q} \sum_{i=1}^{Q} \left( \frac{z - y_i}{z} \right) = 1 - \frac{\bar{y}_p}{z}$$

where $\bar{y}_p$ is the mean income of the poor.

The **Poverty Gap Index ($\text{PGI}$)**, also denoted as $P_1$, aggregates this shortfall across the entire national population:

$$\text{PGI} = \frac{1}{N} \sum_{i=1}^{Q} \left( \frac{z - y_i}{z} \right) = H \times I$$

$\text{PGI}$ measures the total financial resources per capita (expressed as a fraction of $z$) required to lift all poor individuals to the poverty line through perfectly targeted transfers.

### 3. The Foster-Greer-Thorbecke (FGT) Metric Family
In 1984, Erik Foster, Joel Greer, and Erik Thorbecke formulated the **FGT Family of Poverty Indices ($P_\alpha$)**:

$$P_\alpha = \frac{1}{N} \sum_{i=1}^{Q} \left( \frac{z - y_i}{z} \right)^\alpha, \quad \alpha \ge 0$$

The parameter $\alpha$ acts as an inequality aversion parameter:
- $\alpha = 0$: $P_0 = Q/N = H$ (Poverty Incidence / Headcount Ratio).
- $\alpha = 1$: $P_1 = \text{PGI}$ (Poverty Depth / Poverty Gap Index).
- $\alpha = 2$: $P_2 = \text{SPGI}$ (**Squared Poverty Gap Index** or **Poverty Severity Index**). By squaring the proportional shortfalls, $P_2$ places progressively higher mathematical weight on individuals living furthest below the subsistence threshold. Unlike $P_0$ and $P_1$, $P_2$ satisfies both the Monotonicity Axiom and the Pigou-Dalton Transfer Axiom.

---


---

## Entropy-Based Inequality Metrics: The Generalized Entropy Family

While the Gini coefficient provides an intuitive geometric measure of inequality, it suffers from a major mathematical limitation: it is not strictly **sub-group decomposable**. If a population is divided into distinct geographic regions or ethnic subgroups, national Gini inequality cannot be cleanly partitioned into the sum of within-group inequality and between-group inequality without generating an intractable overlapping residual term.

To overcome this, mathematical economists deploy the **Generalized Entropy (GE) Family of Inequality Measures**, rooted in Claude Shannon's information theory.

### Mathematical Formulation
For a discrete population of $n$ individuals with incomes $y = [y_1, y_2, \dots, y_n]$ and arithmetic mean $\mu = \frac{1}{n} \sum y_i$, the Generalized Entropy Index $GE(\alpha)$ is defined as:

$$GE(\alpha) = \begin{cases}
\frac{1}{\alpha(\alpha - 1)} \left[ \frac{1}{n} \sum_{i=1}^{n} \left( \frac{y_i}{\mu} \right)^\alpha - 1 \right], & \alpha \ne 0, 1 \\
\frac{1}{n} \sum_{i=1}^{n} \ln\left( \frac{\mu}{y_i} \right), & \alpha = 0 \\
\frac{1}{n} \sum_{i=1}^{n} \left( \frac{y_i}{\mu} \right) \ln\left( \frac{y_i}{\mu} \right), & \alpha = 1
\end{cases}$$

The parameter $\alpha \in (-\infty, \infty)$ represents sensitivity to income disparities at differing parts of the distribution:
- For large positive $\alpha$ (e.g., $\alpha = 2$), the index is sensitive to income concentration at the very top of the distribution.
- For $\alpha = 1$, the index is the celebrated **Theil's $T$ Index**.
- For $\alpha = 0$, the index is **Theil's $L$ Index** (also known as the **Mean Log Deviation, MLD**), which is particularly sensitive to distress in the lower tail.
- For $\alpha = 2$, $GE(2) = \frac{1}{2} \left( \frac{\sigma}{\mu} \right)^2 = \frac{1}{2} CV^2$, which is half the squared coefficient of variation.

### Perfect Sub-Group Decomposability
Suppose a nation's population is partitioned into $K$ mutually exclusive subgroups ($k = 1, \dots, K$), where subgroup $k$ has population $n_k$, mean income $\mu_k$, population share $v_k = n_k / n$, and aggregate income share $s_k = (n_k \mu_k) / (n \mu)$.
Every Generalized Entropy index decomposes into:

$$GE(\alpha) = GE_{\text{within}}(\alpha) + GE_{\text{between}}(\alpha)$$

where:
$$GE_{\text{within}}(\alpha) = \sum_{k=1}^{K} v_k^{1-\alpha} s_k^\alpha GE_k(\alpha)$$
$$GE_{\text{between}}(\alpha) = \frac{1}{\alpha(\alpha - 1)} \left[ \sum_{k=1}^{K} v_k \left( \frac{\mu_k}{\mu} \right)^\alpha - 1 \right]$$

For the Mean Log Deviation ($\alpha = 0$), the weights simplify to population shares:
$$MLD = \sum_{k=1}^{K} v_k MLD_k + \sum_{k=1}^{K} v_k \ln\left( \frac{\mu}{\mu_k} \right)$$

This property enables policymakers to evaluate what percentage of national inequality stems from disparities within provinces versus average income gaps between provinces.

---

## Normative Inequality Measurement: The Atkinson Index

In 1970, British economist Anthony B. Atkinson formulated an explicit welfare-theoretic approach to inequality measurement. Atkinson argued that every statistical inequality metric embodies an implicit ethical value judgment regarding social welfare.

### 1. Equally Distributed Equivalent Income ($y_{\text{ede}}$)
Let society possess an additive, utilitarian Social Welfare Function over individual incomes:
$$W = \frac{1}{n} \sum_{i=1}^{n} U(y_i)$$
where $U(y)$ exhibits constant relative inequality aversion $\epsilon \ge 0$:
$$U(y) = \begin{cases} \frac{y^{1-\epsilon}}{1-\epsilon}, & \epsilon \ne 1 \\ \ln(y), & \epsilon = 1 \end{cases}$$

Atkinson defined the **Equally Distributed Equivalent Income ($y_{\text{ede}}$)** as that hypothetical level of uniform per-capita income which, if enjoyed by every single individual in society, would generate the exact same level of total social welfare as the currently observed unequal income distribution:

$$U(y_{\text{ede}}) = \frac{1}{n} \sum_{i=1}^{n} U(y_i)$$

Solving for $y_{\text{ede}}$:
$$y_{\text{ede}} = \begin{cases} \left[ \frac{1}{n} \sum_{i=1}^{n} y_i^{1-\epsilon} \right]^{\frac{1}{1-\epsilon}}, & \epsilon \ne 1 \\ \exp\left( \frac{1}{n} \sum_{i=1}^{n} \ln(y_i) \right), & \epsilon = 1 \end{cases}$$

Because $U(y)$ is strictly concave for $\epsilon > 0$, by Jensen's inequality $y_{\text{ede}} < \mu$, where $\mu$ is the actual arithmetic mean income.

### 2. The Atkinson Inequality Index ($A_\epsilon$)
The Atkinson Index is defined as the proportional welfare loss attributable to unequal income distribution:

$$A_\epsilon = 1 - \frac{y_{\text{ede}}}{\mu} = 1 - \left[ \frac{1}{n} \sum_{i=1}^{n} \left( \frac{y_i}{\mu} \right)^{1-\epsilon} \right]^{\frac{1}{1-\epsilon}}$$

- **Interpretation**: An Atkinson index of $A_\epsilon = 0.20$ means that if income were distributed completely equally, society could achieve the same level of aggregate social welfare with only $80\%$ of its current total income. The remaining $20\%$ of national income is effectively "wasted" on inequality.
- **The Inequality Aversion Parameter $\epsilon$**:
  - $\epsilon = 0$: Society is indifferent to inequality ($y_{\text{ede}} = \mu \implies A_0 = 0$).
  - $\epsilon \to \infty$: Society adopts a Rawlsian maximin criterion, focusing exclusively on the welfare of the poorest citizen.


---

## Multidimensional Poverty Measurement: The Alkire-Foster Method

Traditional poverty measurement relied exclusively on unidimensional monetary indicators: whether a household's income or consumption expenditure falls below a monetary threshold $z$. However, as Nobel laureate Amartya Sen emphasized in his **Capabilities Approach**, poverty is inherently multidimensional: an individual may enjoy income above the subsistence line but suffer from severe deprivations in clean drinking water, basic healthcare, literacy, sanitation, and electrical energy.

To operationalize multidimensional poverty, Sabina Alkire and James Foster (2011) developed the **Alkire-Foster Method**, which underpins the United Nations Development Programme's global **Multidimensional Poverty Index (MPI)**.

### 1. The Dual-Cutoff Identification System
Consider an achievement matrix $X$ of size $N \times D$, where $x_{ij}$ denotes the achievement of individual $i$ in dimension $j$ ($j = 1, \dots, D$).
Each dimension has an explicit deprivation cutoff $z_j$ and an importance weight $w_j$ satisfying $\sum_{j=1}^{D} w_j = 1$.

- **First Cutoff (Within-Dimension Deprivation Cutoff $z_j$)**:
  Individual $i$ is deprived in dimension $j$ if $x_{ij} < z_j$.
  We construct the deprivation matrix $g^0$ where:
  $$g_{ij}^0 = \begin{cases} 1, & \text{if } x_{ij} < z_j \\ 0, & \text{if } x_{ij} \ge z_j \end{cases}$$
- **Deprivation Score ($c_i$)**:
  The weighted deprivation score for individual $i$ is:
  $$c_i = \sum_{j=1}^{D} w_j g_{ij}^0, \quad c_i \in [0, 1]$$
- **Second Cutoff (Cross-Dimensional Poverty Cutoff $k$)**:
  An individual is identified as **Multidimensionally Poor** if their total weighted deprivation score equals or exceeds the cross-dimensional threshold $k$ (e.g., $k = 0.33$ or $33\%$ of dimensions):
  $$i \in \text{Poor} \iff c_i \ge k$$

We construct the **Censored Deprivation Score** $c_i(k)$:
$$c_i(k) = \begin{cases} c_i, & \text{if } c_i \ge k \\ 0, & \text{if } c_i < k \end{cases}$$
Deprivations of non-poor individuals are censored to zero.

### 2. The Alkire-Foster Aggregation Metrics
1. **Multidimensional Headcount Ratio ($H$)**:
   The proportion of the population identified as multidimensionally poor:
   $$H = \frac{q_k}{N}$$
   where $q_k$ is the number of individuals with $c_i \ge k$.
2. **Average Intensity of Poverty ($A$)**:
   The average proportion of dimensions in which poor individuals are deprived:
   $$A = \frac{\sum_{i=1}^{N} c_i(k)}{q_k}$$
3. **Adjusted Headcount Ratio ($M_0$ / MPI)**:
   The foundational Alkire-Foster poverty index is the product of incidence ($H$) and intensity ($A$):
   $$M_0 = H \times A = \frac{1}{N} \sum_{i=1}^{N} c_i(k)$$

### 3. Dimensional Decomposition of $M_0$
A vital mathematical property of $M_0$ is that it is strictly decomposable by dimension.
The censored headcount ratio for dimension $j$, denoted $h_j$, is the proportion of the total population that is both multidimensionally poor and deprived in dimension $j$:

$$h_j = \frac{1}{N} \sum_{i=1}^{N} g_{ij}^0(k)$$

The overall index $M_0$ is an exact weighted sum of the dimensional censored headcounts:

$$M_0 = \sum_{j=1}^{D} w_j h_j$$

The percentage contribution of dimension $j$ to national multidimensional poverty is:

$$\text{Contribution}_j = \frac{w_j h_j}{M_0} \times 100\%$$

This allows planners to identify whether national poverty is primarily fueled by lack of educational schooling, child malnutrition, or lack of clean water infrastructure, directly informing targeted sectoral investments.


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

$$MLD(y) = MLD_{\text{within}} + MLD_{\text{between}}$$

The between-type inequality $MLD_{\text{between}}$ is computed by replacing each individual's observed income with the average income of their circumstance type $\bar{y}_m$:

$$MLD_{\text{between}} = \sum_{m=1}^{M} \left( \frac{N_m}{N} \right) \ln\left( \frac{\mu}{\bar{y}_m} \right)$$

The **Inequality of Opportunity Ratio ($IOp$)** is defined as:

$$IOp = \frac{MLD_{\text{between}}}{MLD(y)} \times 100\%$$

In empirical studies across developing economies, between 30% and 60% of total national income inequality is directly attributable to circumstance variables determined at birth, demonstrating that high headline inequality largely reflects structural inequality of opportunity rather than differential effort.

---

## Intergenerational Income Mobility and the Great Gatsby Curve

Complementing static inequality metrics, **Intergenerational Income Mobility** measures the degree to which an individual's economic status is determined by the economic position of their parents.

### 1. The Intergenerational Income Elasticity (IGE)
The standard empirical model of intergenerational mobility regresses the log of child's adult permanent income ($y_{\text{child}}$) on the log of parental income ($y_{\text{parent}}$):

$$\ln(y_{\text{child}}) = \alpha + \beta \ln(y_{\text{parent}}) + \epsilon$$

The parameter $\beta$ is the **Intergenerational Income Elasticity (IGE)**:
- $\beta = 0$: Complete intergenerational mobility (a child's expected adult income is entirely independent of parental wealth; complete equality of opportunity).
- $\beta = 1$: Complete intergenerational immobility (a child's income reproduces their parents' position with zero social fluidity).
- Intergenerational Mobility is measured as $1 - \beta$. In egalitarian societies (Denmark, Norway), $\beta \approx 0.15$ to $0.20$. In highly immobile societies (United States, United Kingdom, Brazil), $\beta \approx 0.45$ to $0.60$.

### 2. The Great Gatsby Curve
Named by Alan Krueger in 2012, the **Great Gatsby Curve** maps the empirical cross-national relationship between static income inequality (measured by the Gini coefficient) on the horizontal axis and intergenerational income persistence (measured by IGE, $\beta$) on the vertical axis.
The curve reveals a strong, positive empirical correlation: nations with higher static income inequality systematically exhibit lower intergenerational social mobility. When income gaps between social strata widen, wealthy families invest vastly greater resources in private schooling, elite tutoring, social networks, and bequest capital, cementing advantage across generations and locking disadvantaged children into persistent poverty traps.


---

## Vulnerability to Poverty and Dynamic Risk Analysis

Standard static poverty metrics measure whether a household's income falls below the subsistence threshold $z$ at a single survey instant. However, households constantly transition into and out of poverty due to agricultural droughts, macro-financial crises, illness, unemployment, or seasonal price spikes.
To incorporate future uncertainty into social policy, economists analyze **Vulnerability to Poverty**.

### Mathematical Formulation of Vulnerability as Expected Poverty
Pioneered by Stefan Dercon and Shubham Chaudhuri (2002), vulnerability $V_{it}$ is defined as the ex-ante probability that a household will experience poverty in the future period $t+1$:

$$V_{it} = P(y_{i, t+1} < z) = \int_{-\infty}^{z} f_{it}(y_{i, t+1}) dy_{i, t+1}$$

where $f_{it}(y_{i, t+1})$ is the conditional subjective probability density function of future household consumption, dependent on observable household asset endowments $X_{it}$ and covariate community shock variables $S_t$.

Econometrically, log household consumption is modeled as:

$$\ln(y_{it}) = X_{it} \beta + e_{it}$$

where disturbances exhibit heteroskedasticity capturing risk exposure:
$$e_{it} \sim N(0, \sigma_{e, i}^2), \quad \sigma_{e, i}^2 = X_{it} \theta$$

Assuming log-normality, the estimated vulnerability probability is:

$$\hat{V}_{it} = \Phi\left( \frac{\ln(z) - X_{it} \hat{\beta}}{\hat{\sigma}_{e, i}} \right)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function.

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

$$S = H \left[ I + (1 - I) G_p \right]$$

where:
- $H = Q / N$ is the Headcount Ratio.
- $I = (z - \bar{y}_p) / z$ is the Income Gap Ratio.
- $G_p$ is the Gini coefficient calculated exclusively among the poor population.

#### Axiomatic Interpretation:
If all poor individuals have identical incomes ($G_p = 0$), Sen's index reduces to $S = H \times I = P_1$ (the standard Poverty Gap Index). As inequality among the destitute widens ($G_p > 0$), the index increases, satisfying both the Monotonicity Axiom and the Transfer Axiom by penalizing severe internal deprivation among the poorest of the poor.


---

## Alternative Rank-Dependent Inequality Metrics: Mehran and Piesch Indices

While Corrado Gini's concentration coefficient weights the vertical distance between the 45-degree line and the Lorenz curve uniformly across the population, welfare economists often wish to place greater ethical sensitivity on disparities at specific locations along the income spectrum.
Farhad Mehran (1976) and Walter Piesch (1975) formulated alternative linear rank-dependent inequality metrics.

### 1. The Mehran Inequality Index ($M$)
The Mehran Index assigns declining linear weights to individuals based on their population rank, placing greater mathematical emphasis on income inequality among the poorest citizens:

$$M = 3 \int_{0}^{1} (1 - p) [p - L(p)] dp$$

- In discrete population samples:
  $$M = 1 - \frac{3}{n^2 \mu} \sum_{i=1}^{n} (n - i + 1)^2 y_{(i)}$$
- The Mehran index is particularly sensitive to changes in income at the bottom of the distribution: a transfer from an impoverished citizen to a middle-class citizen produces a larger numerical increase in $M$ than in the Gini coefficient.

### 2. The Piesch Inequality Index ($P$)
Conversely, the Piesch Index assigns increasing linear weights to population rank, focusing sensitivity on concentration at the top of the income distribution:

$$P = \frac{3}{2} \int_{0}^{1} p [p - L(p)] dp$$

- In discrete population samples:
  $$P = \frac{3}{2 n^2 \mu} \sum_{i=1}^{n} i^2 y_{(i)} - \frac{3n + 1}{4n}$$
- The Piesch index is sensitive to oligarchic wealth concentration and windfall executive earnings among the top percentiles.

By examining the triad of Gini, Mehran, and Piesch indices simultaneously, national statistical offices can ascertain whether rising national inequality is being driven primarily by falling wages at the bottom ($M$ rising fastest) or accelerating wealth accumulation at the top ($P$ rising fastest).

## Worked Questions and Solutions

### Question 1: Pareto Law Estimation and Distributional Analytics
A national revenue authority compiles annual corporate income tax returns. Corporate gross operating surpluses above a minimum threshold of $x_0 = \$100{,}000$ follow Pareto's distribution $N(x) = A x^{-\alpha}$. An audit of high-earning enterprises provides empirical counts:

| Income Threshold ($x$) | Number of Firms with Income $\ge x$ ($N$) |
| :---: | :---: |
| $\$100{,}000$ | $10{,}000$ |
| $\$200{,}000$ | $3{,}535$ |
| $\$400{,}000$ | $1{,}250$ |
| $\$800{,}000$ | $442$ |
| $\$1{,}600{,}000$ | $156$ |

1. Transform the empirical data into logarithmic coordinates and estimate the Pareto index $\alpha$ via Ordinary Least Squares regression of $\ln(N)$ on $\ln(x)$.
2. Calculate the theoretical arithmetic mean income $E[X]$ and median income $x_{\text{med}}$ of firms in this tax bracket.
3. Determine the theoretical Gini concentration coefficient implied by the estimated Pareto parameter $\alpha$.
4. Calculate the percentage of aggregate total corporate income captured by the top $10\%$ of corporations in this bracket.

### Solution, step 1: OLS Log-Linear Estimation of $\alpha$
We express income in units of $\$100{,}000$ (so $x_0 = 1.0$) or directly in dollars. Let $x$ be expressed in thousands of dollars:
- $x = [100, 200, 400, 800, 1600]$
- $N = [10000, 3535, 1250, 442, 156]$

Let us compute the natural logarithms $u_i = \ln(x_i)$ and $v_i = \ln(N_i)$:
- $i=1$: $x_1 = 100 \implies u_1 = \ln(100) \approx 4.6052$; $N_1 = 10000 \implies v_1 = \ln(10000) \approx 9.2103$
- $i=2$: $x_2 = 200 \implies u_2 = \ln(200) \approx 5.2983$; $N_2 = 3535 \implies v_2 = \ln(3535) \approx 8.1705$
- $i=3$: $x_3 = 400 \implies u_3 = \ln(400) \approx 5.9915$; $N_3 = 1250 \implies v_3 = \ln(1250) \approx 7.1309$
- $i=4$: $x_4 = 800 \implies u_4 = \ln(800) \approx 6.6846$; $N_4 = 442 \implies v_4 = \ln(442) \approx 6.0913$
- $i=5$: $x_5 = 1600 \implies u_5 = \ln(1600) \approx 7.3778$; $N_5 = 156 \implies v_5 = \ln(156) \approx 5.0500$

Let us evaluate the step differences in $u$ and $v$:
Notice that $x$ doubles at each step: $\Delta u = \ln(2) \approx 0.69315$.
The corresponding changes in $\ln(N)$ are:
- $v_2 - v_1 = 8.1705 - 9.2103 = -1.0398$
- $v_3 - v_2 = 7.1309 - 8.1705 = -1.0396$
- $v_4 - v_3 = 6.0913 - 7.1309 = -1.0396$
- $v_5 - v_4 = 5.0500 - 6.0913 = -1.0413$

The slope is remarkably constant across all intervals:
$$\text{Slope } (-\alpha) = \frac{\Delta v}{\Delta u} = \frac{-1.0398}{0.69315} = -1.5001 \approx -1.50$$

Thus, the Ordinary Least Squares estimate of the Pareto index is:
$$\alpha = 1.50$$

### Solution, step 2: Theoretical Mean and Median Income
With $\alpha = 1.50$ and minimum threshold $x_0 = \$100{,}000$:

1. **Theoretical Mean Corporate Income**:
   $$E[X] = \frac{\alpha}{\alpha - 1} x_0 = \frac{1.50}{1.50 - 1.00} \times \$100{,}000 = \frac{1.50}{0.50} \times \$100{,}000 = 3 \times \$100{,}000 = \mathbf{\$300{,}000}$$

2. **Theoretical Median Corporate Income**:
   $$x_{\text{med}} = x_0 2^{1/\alpha} = \$100{,}000 \times 2^{1/1.50} = \$100{,}000 \times 2^{2/3} = \$100{,}000 \times (4)^{1/3} \approx \$100{,}000 \times 1.5874 = \mathbf{\$158{,}740}$$

The mean income ($\$300{,}000$) is nearly double the median income ($\$158{,}740$), illustrating strong positive skewness.

### Solution, step 3: Pareto-Implied Gini Concentration Coefficient
For a Pareto distribution with $\alpha > 1$, the closed-form Gini coefficient formula is:

$$G = \frac{1}{2\alpha - 1}$$

Substituting $\alpha = 1.50$:
$$G = \frac{1}{2(1.50) - 1} = \frac{1}{3.0 - 1.0} = \frac{1}{2.0} = \mathbf{0.500}$$

The distribution exhibits a high Gini coefficient of 0.50, reflecting substantial inequality in corporate earnings.

### Solution, step 4: Income Captured by the Top 10% of Corporations
Let $p$ denote the cumulative proportion of firms from the bottom, so $p = 1 - 0.10 = 0.90$ marks the 90th percentile threshold.
The cumulative Lorenz curve for the Pareto distribution is:
$$L(p) = 1 - (1 - p)^{(\alpha - 1)/\alpha}$$

For $\alpha = 1.50$:
$$\frac{\alpha - 1}{\alpha} = \frac{1.50 - 1.00}{1.50} = \frac{0.50}{1.50} = \frac{1}{3}$$

Evaluating $L(0.90)$:
$$L(0.90) = 1 - (1 - 0.90)^{1/3} = 1 - (0.10)^{1/3}$$
Since $(0.10)^{1/3} \approx 0.46416$:
$$L(0.90) = 1 - 0.46416 = 0.53584 \approx 53.58\%$$

This indicates that the bottom $90\%$ of corporations earn only $53.58\%$ of aggregate corporate profits.
Consequently, the top $10\%$ of corporations capture:
$$\text{Top } 10\% \text{ Share} = 1 - L(0.90) = 1 - 0.53584 = 0.46416 = \mathbf{46.42\%}$$

Nearly half ($46.42\%$) of all corporate earnings are concentrated among the top decile of firms.

---

### Question 2: Lorenz Curve and Gini Coefficient from Grouped Household Survey Data
A national statistical bureau surveys $100{,}000$ households and groups them into equal population quintiles ($20\%$ each). The aggregate household disposable income (in millions of currency units) recorded for each quintile is:

| Quintile | Households ($f_i$) | Aggregate Income ($Y_i$) |
| :---: | :---: | :---: |
| **1st Quintile (Poorest 20%)** | $20{,}000$ | $60$ |
| **2nd Quintile** | $20{,}000$ | $120$ |
| **3rd Quintile** | $20{,}000$ | $180$ |
| **4th Quintile** | $20{,}000$ | $260$ |
| **5th Quintile (Richest 20%)** | $20{,}000$ | $380$ |

1. Construct the complete cumulative distribution schedule: population shares ($p_i$), cumulative income totals, and cumulative income shares ($q_i$).
2. Apply the Brown trapezoidal formula to compute the national Gini concentration coefficient.
3. Compute the Palma Ratio (ratio of the income share of the richest $10\%$ or top quintile to the poorest $40\%$).
4. Interpret the resulting metrics in terms of standard international welfare criteria.

### Solution, step 1: Construction of Cumulative Schedule
Total national income across all quintiles:
$$Y_{\text{total}} = 60 + 120 + 180 + 260 + 380 = 1{,}000 \text{ million}$$

Total population: $N = 100{,}000$.
Each quintile represents an equal population increment: $\Delta p_i = 0.20$.

We compute cumulative population shares $p_i$ and cumulative income shares $q_i$:

- **Base ($i=0$)**:
  $$p_0 = 0.00, \quad q_0 = 0.00$$
- **1st Quintile ($i=1$)**:
  - Cumulative population: $20{,}000 \implies p_1 = 0.20$
  - Income: $60 \implies q_1 = \frac{60}{1{,}000} = 0.060$
- **2nd Quintile ($i=2$)**:
  - Cumulative population: $40{,}000 \implies p_2 = 0.40$
  - Cumulative income: $60 + 120 = 180 \implies q_2 = \frac{180}{1{,}000} = 0.180$
- **3rd Quintile ($i=3$)**:
  - Cumulative population: $60{,}000 \implies p_3 = 0.60$
  - Cumulative income: $180 + 180 = 360 \implies q_3 = \frac{360}{1{,}000} = 0.360$
- **4th Quintile ($i=4$)**:
  - Cumulative population: $80{,}000 \implies p_4 = 0.80$
  - Cumulative income: $360 + 260 = 620 \implies q_4 = \frac{620}{1{,}000} = 0.620$
- **5th Quintile ($i=5$)**:
  - Cumulative population: $100{,}000 \implies p_5 = 1.00$
  - Cumulative income: $620 + 380 = 1{,}000 \implies q_5 = 1.000$

Tabular summary:

| $i$ | Quintile | $p_i$ | $\Delta p_i$ | $q_i$ | $q_{i-1} + q_i$ | $\Delta p_i \times (q_{i-1} + q_i)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | Origin | 0.00 | — | 0.000 | — | — |
| 1 | 1st Quintile | 0.20 | 0.20 | 0.060 | $0.000 + 0.060 = 0.060$ | $0.20 \times 0.060 = 0.0120$ |
| 2 | 2nd Quintile | 0.40 | 0.20 | 0.180 | $0.060 + 0.180 = 0.240$ | $0.20 \times 0.240 = 0.0480$ |
| 3 | 3rd Quintile | 0.60 | 0.20 | 0.360 | $0.180 + 0.360 = 0.540$ | $0.20 \times 0.540 = 0.1080$ |
| 4 | 4th Quintile | 0.80 | 0.20 | 0.620 | $0.360 + 0.620 = 0.980$ | $0.20 \times 0.980 = 0.1960$ |
| 5 | 5th Quintile | 1.00 | 0.20 | 1.000 | $0.620 + 1.000 = 1.620$ | $0.20 \times 1.620 = 0.3240$ |

### Solution, step 2: Computation of Gini Concentration Coefficient
The area under the empirical piecewise linear Lorenz curve is:
$$B = \frac{1}{2} \sum_{i=1}^{5} (p_i - p_{i-1})(q_{i-1} + q_i)$$

Sum of products:
$$\sum_{i=1}^{5} \Delta p_i (q_{i-1} + q_i) = 0.0120 + 0.0480 + 0.1080 + 0.1960 + 0.3240 = 0.6880$$

Applying the Brown Formula:
$$G = 1 - \sum_{i=1}^{5} (p_i - p_{i-1})(q_{i-1} + q_i) = 1 - 0.6880 = \mathbf{0.3120}$$

The national Gini coefficient is **$0.312$** (or $31.2\%$).

### Solution, step 3: Palma Ratio Computation
The Palma Ratio compares the income share of the top $10\%$ (or top quintile in quintile datasets) to the poorest $40\%$ of the population:
- Income share of top quintile (5th Quintile):
  $$S_{\text{top 20}} = \frac{380}{1{,}000} = 38.0\%$$
- Income share of bottom $40\%$ (1st + 2nd Quintiles):
  $$S_{\text{bottom 40}} = \frac{60 + 120}{1{,}000} = \frac{180}{1{,}000} = 18.0\%$$

The Palma-type ratio for this economy is:
$$\text{Palma Ratio} = \frac{S_{\text{top 20}}}{S_{\text{bottom 40}}} = \frac{38.0\%}{18.0\%} \approx \mathbf{2.111}$$

The richest $20\%$ of households command more than double the combined income of the entire bottom $40\%$ of society.

### Solution, step 4: Economic Assessment
A Gini coefficient of $0.312$ places this society in the moderate inequality bracket (comparable to countries like Germany, France, or Japan). While significantly more egalitarian than nations with Gini indices exceeding 0.45, the Palma ratio of 2.11 underscores that the poorest two quintiles capture only $18\%$ of national income, highlighting the necessity of progressive fiscal transfers and subsidized public services.

---

### Question 3: Poverty Measurement under the Foster-Greer-Thorbecke Framework
A socioeconomic survey evaluates consumption expenditures across ten representative households in an impoverished district ($N = 10$). The official absolute poverty line is established at:
$$z = \$150.00 \text{ per capita per month}$$

The recorded monthly per-capita expenditures (in dollars) of the ten households are:
$$\{ 60.0, \; 75.0, \; 90.0, \; 105.0, \; 120.0, \; 155.0, \; 180.0, \; 210.0, \; 250.0, \; 320.0 \}$$

1. Identify the number of poor households ($Q$) and compute the **Headcount Ratio ($P_0 = H$)**.
2. Compute the individual poverty shortfall gaps $(z - y_i)/z$ for all poor households, and calculate the **Poverty Gap Index ($P_1 = \text{PGI}$)**.
3. Compute the **Squared Poverty Gap Index ($P_2 = \text{SPGI}$)**.
4. Evaluate a proposed anti-poverty policy: a cash transfer of $\$30.00$ given to Household 1 (expenditure $\$60.00$) versus a cash transfer of $\$30.00$ given to Household 5 (expenditure $\$120.00$). Analyze the impact of each transfer on $P_0$, $P_1$, and $P_2$, and explain why $P_2$ satisfies the Pigou-Dalton transfer principle.

### Solution, step 1: Identification of the Poor and Headcount Ratio
We compare each household's expenditure $y_i$ against the poverty line $z = \$150.00$:
- Household 1: $y_1 = 60.0 < 150 \implies$ Poor
- Household 2: $y_2 = 75.0 < 150 \implies$ Poor
- Household 3: $y_3 = 90.0 < 150 \implies$ Poor
- Household 4: $y_4 = 105.0 < 150 \implies$ Poor
- Household 5: $y_5 = 120.0 < 150 \implies$ Poor
- Households 6 to 10: $y_i \ge 155.0 \ge 150 \implies$ Non-poor

The number of poor households is $Q = 5$.
Total households: $N = 10$.

The **Headcount Ratio ($P_0$)** is:
$$P_0 = H = \frac{Q}{N} = \frac{5}{10} = \mathbf{0.50} \quad (50.0\%)$$

### Solution, step 2: Computation of Poverty Gap Index ($P_1$)
For each poor household, we calculate the normalized poverty gap $g_i = \frac{z - y_i}{z} = \frac{150 - y_i}{150}$:
- $i=1$: $g_1 = \frac{150 - 60}{150} = \frac{90}{150} = 0.60$
- $i=2$: $g_2 = \frac{150 - 75}{150} = \frac{75}{150} = 0.50$
- $i=3$: $g_3 = \frac{150 - 90}{150} = \frac{60}{150} = 0.40$
- $i=4$: $g_4 = \frac{150 - 105}{150} = \frac{45}{150} = 0.30$
- $i=5$: $g_5 = \frac{150 - 120}{150} = \frac{30}{150} = 0.20$

Sum of normalized gaps across the poor:
$$\sum_{i=1}^{5} g_i = 0.60 + 0.50 + 0.40 + 0.30 + 0.20 = 2.00$$

The **Poverty Gap Index ($P_1$)** across the entire population ($N = 10$) is:
$$P_1 = \frac{1}{N} \sum_{i=1}^{Q} g_i = \frac{2.00}{10} = \mathbf{0.200} \quad (20.0\%)$$

The average depth of poverty represents $20.0\%$ of the poverty line per capita across the entire population. To eradicate poverty through perfect targeting, the government would need to disburse $0.20 \times \$150.00 = \$30.00$ per capita across all 10 households (a total fiscal outlay of $\$300.00$).

### Solution, step 3: Computation of Squared Poverty Gap Index ($P_2$)
We square the individual normalized gaps $g_i^2$:
- $i=1$: $g_1^2 = (0.60)^2 = 0.3600$
- $i=2$: $g_2^2 = (0.50)^2 = 0.2500$
- $i=3$: $g_3^2 = (0.40)^2 = 0.1600$
- $i=4$: $g_4^2 = (0.30)^2 = 0.0900$
- $i=5$: $g_5^2 = (0.20)^2 = 0.0400$

Sum of squared gaps:
$$\sum_{i=1}^{5} g_i^2 = 0.3600 + 0.2500 + 0.1600 + 0.0900 + 0.0400 = 0.9000$$

The **Squared Poverty Gap Index ($P_2$)** is:
$$P_2 = \frac{1}{N} \sum_{i=1}^{Q} g_i^2 = \frac{0.9000}{10} = \mathbf{0.0900} \quad (9.0\%)$$

### Solution, step 4: Policy Transfer Evaluation & Pigou-Dalton Axiom
Let us compare two alternative fiscal transfer interventions, each allocating $\$30.00$:

#### Policy A: Transfer $\$30.00$ to Household 5 ($y_5 = 120.00$)
- New expenditure: $y_5' = 120 + 30 = \$150.00$.
- Because $y_5' = z$, Household 5 crosses the poverty line and is no longer classified as poor.
- **Headcount Ratio ($P_0$)**: Falls from $0.50$ to $4/10 = \mathbf{0.40}$ (a 20% drop in headline poverty!).
- **Poverty Gap ($P_1$)**:
  New gap sum: $0.60 + 0.50 + 0.40 + 0.30 + 0.00 = 1.80$.
  $P_1' = 1.80 / 10 = \mathbf{0.180}$ (reduction of $\Delta P_1 = 0.020$).
- **Poverty Severity ($P_2$)**:
  New squared gap sum: $0.36 + 0.25 + 0.16 + 0.09 + 0.00 = 0.86$.
  $P_2' = 0.86 / 10 = \mathbf{0.0860}$ (reduction of $\Delta P_2 = 0.0040$).

#### Policy B: Transfer $\$30.00$ to Household 1 ($y_1 = 60.00$)
- New expenditure: $y_1' = 60 + 30 = \$90.00$.
- Because $y_1' = 90 < 150$, Household 1 remains poor.
- **Headcount Ratio ($P_0$)**: Remains completely unchanged at $5/10 = \mathbf{0.50}$.
- **Poverty Gap ($P_1$)**:
  New gap for Household 1: $g_1' = (150 - 90)/150 = 0.40$.
  New gap sum: $0.40 + 0.50 + 0.40 + 0.30 + 0.20 = 1.80$.
  $P_1' = 1.80 / 10 = \mathbf{0.180}$ (reduction of $\Delta P_1 = 0.020$, exactly identical to Policy A).
- **Poverty Severity ($P_2$)**:
  New squared gap for Household 1: $(0.40)^2 = 0.1600$.
  New squared gap sum: $0.16 + 0.25 + 0.16 + 0.09 + 0.04 = 0.70$.
  $P_2' = 0.70 / 10 = \mathbf{0.0700}$ (reduction of $\Delta P_2 = 0.0200$).

#### Methodological and Ethical Synthesis:
- If policymakers target the **Headcount Ratio ($P_0$)**, they face a perverse political incentive to favor Policy A: helping those closest to the poverty line ("skimming the cream") to artificially lower headline poverty, while neglecting the most destitute.
- If policymakers target the **Poverty Gap Index ($P_1$)**, both policies appear equally effective because $P_1$ measures total linear cash deficits.
- Only the **Squared Poverty Gap Index ($P_2$)** captures that helping the poorest household yields **five times greater poverty severity reduction** ($\Delta P_2 = 0.0200$ vs $0.0040$). By satisfying the **Pigou-Dalton Transfer Principle**, $P_2$ penalizes regressive distribution among the poor and rigorously guides social protection toward the most vulnerable.
