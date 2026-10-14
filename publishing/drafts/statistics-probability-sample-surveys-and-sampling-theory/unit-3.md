# Unit 3: Stratified Random Sampling and Optimal Allocation

## Principles of Stratification and Population Heterogeneity

Simple random sampling treats the entire finite population as an undifferentiated, homogeneous collective. In the vast majority of real-world socioeconomic, ecological, industrial, and demographic investigations, however, populations exhibit pronounced internal structures. Establishments differ by industrial sector and revenue scale; agricultural holdings vary across ecological zones and irrigation regimes; and households diverge across urban, suburban, and rural administrative regions. When substantial variation exists between identifiable sub-collectives, simple random sampling expends unnecessary sample size absorbing between-group differences into the total variance.

Stratified sampling resolves this fundamental inefficiency by partitioning the population of $N$ units into $L$ non-overlapping, mutually exclusive, and exhaustive subpopulations called **strata**, denoted by $U_1, U_2, \dots, U_L$. The partition satisfies two fundamental set-theoretic conditions:
$$U = \bigcup_{h=1}^L U_h \quad \text{and} \quad U_h \cap U_k = \emptyset \quad \forall h \ne k$$
Let $N_h = |U_h|$ denote the number of population units in stratum $h$, such that:
$$N = \sum_{h=1}^L N_h$$
The relative size of stratum $h$ in the population is designated as the **stratum weight**:
$$W_h = \frac{N_h}{N}, \quad \text{where } \sum_{h=1}^L W_h = 1 \text{ and } W_h > 0 \quad \forall h$$

The operational protocol of **Stratified Random Sampling** requires that an independent probability sample $s_h$ of predetermined size $n_h \ge 2$ be drawn from each stratum $U_h$ using an independent simple random sampling without replacement (SRSWOR) design. The total sample size across all $L$ strata is:
$$n = \sum_{h=1}^L n_h$$
Because the samples are selected independently across strata, the random inclusion indicators $I_{hi}$ and $I_{kj}$ are statistically independent whenever $h \ne k$, drastically simplifying the joint probability space and variance calculations.

The core motivation for stratification rests upon three distinct scientific and administrative imperatives:
1. **Dramatic Precision Gains**: By grouping elements that are relatively homogeneous into the same stratum, the within-stratum variances $S_h^2$ are substantially smaller than the overall population variance $S^2$. Because sampling is conducted independently within each stratum, between-stratum differences $\sum W_h (\bar{Y}_h - \bar{Y})^2$ are completely eliminated from the sampling error of the estimator.
2. **Guaranteed Domain Representation**: In unstratified SRSWOR, small yet critically important subpopulations (such as rare specialized industrial firms or minority ethnic communities) risk being severely underrepresented or completely omitted from the realized sample purely by random chance. Stratification guarantees a pre-specified sample size $n_h$ for every domain of study, ensuring that all subpopulation estimates achieve acceptable margins of error.
3. **Operational and Administrative Convenience**: Fieldwork management, interviewer dispatching, language translation of questionnaires, and sampling frames are frequently organized by administrative geographic divisions. Stratification allows differing field procedures, sampling frames, and measurement modes to be tailored to each regional environment.

## Population Parameters and Stratified Estimators

Let $y_{hi}$ denote the value of the survey variable for the $i$-th element in the $h$-th stratum, where $h = 1, \dots, L$ and $i = 1, \dots, N_h$. The fundamental stratum-level parameters are defined as follows:

The **stratum total**:
$$Y_h = \sum_{i=1}^{N_h} y_{hi}$$
The **stratum population mean**:
$$\bar{Y}_h = \frac{1}{N_h} \sum_{i=1}^{N_h} y_{hi} = \frac{Y_h}{N_h}$$
The **stratum finite population variance** (defined with divisor $N_h - 1$):
$$S_h^2 = \frac{1}{N_h - 1} \sum_{i=1}^{N_h} (y_{hi} - \bar{Y}_h)^2$$

The overall population total is the aggregate across all $L$ strata:
$$Y = \sum_{h=1}^L Y_h = \sum_{h=1}^L N_h \bar{Y}_h$$
The overall population mean is the weighted average of the individual stratum means:
$$\bar{Y} = \frac{Y}{N} = \frac{1}{N} \sum_{h=1}^L N_h \bar{Y}_h = \sum_{h=1}^L W_h \bar{Y}_h$$

### The Stratified Sample Mean Estimator
Within each stratum $h$, let $\bar{y}_h$ denote the sample mean of the $n_h$ selected units:
$$\bar{y}_h = \frac{1}{n_h} \sum_{i \in s_h} y_{hi}$$
The standard estimator of the overall population mean $\bar{Y}$ under stratified sampling is the **stratified sample mean**, denoted $\bar{y}_{st}$:
$$\bar{y}_{st} = \sum_{h=1}^L W_h \bar{y}_h = \sum_{h=1}^L \frac{N_h}{N} \bar{y}_h$$
Similarly, the estimator of the population total $Y$ is:
$$\hat{Y}_{st} = N \bar{y}_{st} = \sum_{h=1}^L N_h \bar{y}_h$$

### Proof of Design Unbiasedness
We evaluate the mathematical expectation of $\bar{y}_{st}$ under the stratified random sampling design distribution. Because expectation is a linear operator and sampling is conducted independently within each stratum:
$$E[\bar{y}_{st}] = E\left[ \sum_{h=1}^L W_h \bar{y}_h \right] = \sum_{h=1}^L W_h E[\bar{y}_h]$$
Within stratum $h$, the sample is drawn via SRSWOR from $U_h$. By the fundamental theorem of SRSWOR proved in Unit 2, the sample mean $\bar{y}_h$ is strictly design-unbiased for the stratum mean $\bar{Y}_h$, so $E[\bar{y}_h] = \bar{Y}_h$. Therefore:
$$E[\bar{y}_{st}] = \sum_{h=1}^L W_h \bar{Y}_h = \bar{Y}$$
This proves that the stratified sample mean $\bar{y}_{st}$ is strictly **design-unbiased** for the population mean $\bar{Y}$. Likewise, $E[\hat{Y}_{st}] = N E[\bar{y}_{st}] = N \bar{Y} = Y$.

### Exact Variance of the Stratified Estimator
To derive the sampling variance of $\bar{y}_{st}$, we exploit the mutual independence of the sampling mechanisms across distinct strata:
$$V(\bar{y}_{st}) = V\left( \sum_{h=1}^L W_h \bar{y}_h \right) = \sum_{h=1}^L W_h^2 V(\bar{y}_h) + \sum_{h=1}^L \sum_{k \ne h}^L W_h W_k \text{Cov}(\bar{y}_h, \bar{y}_k)$$
Because the selection in stratum $h$ is entirely independent of the selection in stratum $k$ for all $h \ne k$, the design covariance is identically zero: $\text{Cov}(\bar{y}_h, \bar{y}_k) = 0$.

Applying the SRSWOR variance formula within each stratum:
$$V(\bar{y}_h) = \left( \frac{1 - f_h}{n_h} \right) S_h^2 = \left( \frac{N_h - n_h}{N_h} \right) \frac{S_h^2}{n_h}$$
where $f_h = n_h / N_h$ is the stratum sampling fraction. Substituting this into the variance summation yields the foundational variance formula for stratified random sampling:
$$V(\bar{y}_{st}) = \sum_{h=1}^L W_h^2 \left( \frac{1 - f_h}{n_h} \right) S_h^2 = \sum_{h=1}^L W_h^2 \left( \frac{N_h - n_h}{N_h} \right) \frac{S_h^2}{n_h}$$
For the estimated total $\hat{Y}_{st} = N \bar{y}_{st}$:
$$V(\hat{Y}_{st}) = N^2 V(\bar{y}_{st}) = \sum_{h=1}^L N_h^2 \left( \frac{1 - f_h}{n_h} \right) S_h^2 = \sum_{h=1}^L N_h(N_h - n_h) \frac{S_h^2}{n_h}$$

### Unbiased Estimation of Stratified Sampling Variance
In empirical applications, the stratum population variances $S_h^2$ are unknown. Let $s_h^2$ denote the sample variance computed from the $n_h$ observations in stratum $h$:
$$s_h^2 = \frac{1}{n_h - 1} \sum_{i \in s_h} (y_{hi} - \bar{y}_h)^2$$
Since $E[s_h^2] = S_h^2$ for every stratum $h$, an unbiased estimator of $V(\bar{y}_{st})$ is:
$$v(\bar{y}_{st}) = \sum_{h=1}^L W_h^2 \left( \frac{1 - f_h}{n_h} \right) s_h^2 = \sum_{h=1}^L W_h^2 \left( \frac{N_h - n_h}{N_h} \right) \frac{s_h^2}{n_h}$$
This estimator is strictly design-unbiased: $E[v(\bar{y}_{st})] = V(\bar{y}_{st})$, provided $n_h \ge 2$ for all $h = 1, \dots, L$.

## Allocation Schemes: Proportional, Neyman and Cost-Optimized Allocation

Once the total sample size $n$ and the strata boundaries are fixed, the statistician must decide how to partition $n$ into the individual stratum sample sizes $n_1, n_2, \dots, n_L$ subject to the constraint $\sum_{h=1}^L n_h = n$. The method of choosing $n_h$ is called the **sample allocation scheme**. Differing allocation schemes optimize different mathematical criteria.

### 1. Equal Allocation
Under **Equal Allocation**, an identical number of units is selected from each stratum, regardless of stratum size or variability:
$$n_h = \frac{n}{L} \quad \forall h = 1, \dots, L$$
Equal allocation is typically deployed when the primary research objective is to compare individual strata against one another with equal statistical power (e.g., comparing four geographic quadrants), rather than estimating the aggregate population mean $\bar{Y}$.

### 2. Proportional Allocation
Under **Proportional Allocation** (pioneered by Arthur Bowley in 1926), the stratum sample sizes are set strictly proportional to the stratum population sizes:
$$n_h \propto N_h \implies n_h = n \frac{N_h}{N} = n W_h$$
This allocation guarantees that the sampling fraction is completely uniform across all strata:
$$f_h = \frac{n_h}{N_h} = \frac{n W_h}{N W_h} = \frac{n}{N} = f \quad \forall h = 1, \dots, L$$
A sampling design with uniform inclusion probabilities ($\pi_{hi} = f$) is called a **self-weighting design**. In a self-weighting stratified sample, the design weights $d_{hi} = 1 / \pi_{hi} = N / n$ are identical for every sampled unit across the entire population. Consequently, the stratified sample mean $\bar{y}_{st}$ simplifies to the ordinary unweighted sample mean of all $n$ observations:
$$\bar{y}_{st} = \sum_{h=1}^L W_h \bar{y}_h = \sum_{h=1}^L \frac{N_h}{N} \left( \frac{1}{n_h} \sum_{i \in s_h} y_{hi} \right) = \sum_{h=1}^L \frac{N_h}{N} \left( \frac{N}{n N_h} \sum_{i \in s_h} y_{hi} \right) = \frac{1}{n} \sum_{h=1}^L \sum_{i \in s_h} y_{hi} = \bar{y}$$
This self-weighting property provides immense operational simplicity: no individual case weighting is required during tabulation.

Substituting $n_h = n W_h$ and $f_h = f$ into the general stratified variance formula gives the variance under proportional allocation:
$$V_{prop}(\bar{y}_{st}) = \sum_{h=1}^L W_h^2 \left( \frac{1 - f}{n W_h} \right) S_h^2 = \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h S_h^2$$
Notice that the variance is directly proportional to the weighted average of the internal stratum variances, $\bar{S}^2_{within} = \sum W_h S_h^2$.

### 3. Neyman Optimal Allocation
While proportional allocation accounts for stratum sizes, it ignores differences in stratum variability. If Stratum 1 is composed of highly volatile elements ($S_1 = 500$) while Stratum 2 is composed of nearly identical elements ($S_2 = 10$), allocating equal proportions of sample to both is highly suboptimal: observing a small number of units in Stratum 2 is sufficient to determine its mean with extreme precision, freeing up resources to sample Stratum 1 much more intensively.

Jerzy Neyman (1934) solved this optimization problem: finding the stratum sample sizes $n_1, \dots, n_L$ that minimize the variance $V(\bar{y}_{st})$ for a fixed total sample size $n = \sum n_h$.

Ignoring the finite population correction term $W_h^2 S_h^2 / N_h$ (which is independent of $n_h$), the objective is to minimize:
$$f(n_1, \dots, n_L) = \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} \quad \text{subject to} \quad g(n_1, \dots, n_L) = \sum_{h=1}^L n_h - n = 0$$

Formulate the Lagrangian function:
$$\Lambda(n_1, \dots, n_L, \lambda) = \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} + \lambda \left( \sum_{h=1}^L n_h - n \right)$$
Differentiating with respect to $n_h$ and setting the partial derivative to zero:
$$\frac{\partial \Lambda}{\partial n_h} = -\frac{W_h^2 S_h^2}{n_h^2} + \lambda = 0 \implies n_h^2 = \frac{W_h^2 S_h^2}{\lambda} \implies n_h = \frac{W_h S_h}{\sqrt{\lambda}}$$
Summing across all strata $h = 1, \dots, L$:
$$\sum_{h=1}^L n_h = \frac{1}{\sqrt{\lambda}} \sum_{h=1}^L W_h S_h = n \implies \frac{1}{\sqrt{\lambda}} = \frac{n}{\sum_{k=1}^L W_k S_k}$$
Substituting $1/\sqrt{\lambda}$ back into the expression for $n_h$ yields **Neyman’s Optimal Allocation Formula**:
$$n_h = n \left( \frac{W_h S_h}{\sum_{k=1}^L W_k S_k} \right) = n \left( \frac{N_h S_h}{\sum_{k=1}^L N_k S_k} \right)$$

Under Neyman allocation, the sample allocated to stratum $h$ is directly proportional to both its population size $N_h$ and its standard deviation $S_h$. Strata that are large and heterogeneous receive the largest allocations; strata that are small or uniform receive minimal allocations.

To obtain the variance under Neyman allocation, substitute $n_h = n \frac{W_h S_h}{\sum W_k S_k}$ into the variance formula:
$$V_{Neyman}(\bar{y}_{st}) = \sum_{h=1}^L \frac{W_h^2 S_h^2}{n \frac{W_h S_h}{\sum W_k S_k}} - \frac{1}{N} \sum_{h=1}^L W_h S_h^2 = \frac{1}{n} \left( \sum_{k=1}^L W_k S_k \right) \sum_{h=1}^L W_h S_h - \frac{1}{N} \sum_{h=1}^L W_h S_h^2$$
$$V_{Neyman}(\bar{y}_{st}) = \frac{1}{n} \left( \sum_{h=1}^L W_h S_h \right)^2 - \frac{1}{N} \sum_{h=1}^L W_h S_h^2$$

### 4. Optimum Allocation under a Linear Cost Function
In real-world field surveys, the cost of surveying an element varies substantially across strata. Surveying a rural household in an isolated mountainous district ($c_1 = 5,000$ BDT per interview) requires significant travel time and off-road transport, whereas surveying an urban apartment in Dhaka ($c_2 = 500$ BDT) is relatively inexpensive.

Let the total survey cost be modeled by a realistic **linear cost function**:
$$C = c_0 + \sum_{h=1}^L c_h n_h$$
where $c_0$ is fixed overhead cost (office headquarters, administrative management, software infrastructure) and $c_h$ is the unit cost of enumerating a single element in stratum $h$.

The optimization problem can be framed in two dual ways:
1. **Minimize Variance for a Fixed Total Budget $C$**.
2. **Minimize Total Cost $C$ for a Prescribed Variance Target $V^*$**.

Using the Cauchy–Schwarz inequality, consider the product of the variable variance $\sum \frac{W_h^2 S_h^2}{n_h}$ and the variable cost $\sum c_h n_h$:
$$\left( \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} \right) \left( \sum_{h=1}^L c_h n_h \right) \ge \left[ \sum_{h=1}^L \left( \frac{W_h S_h}{\sqrt{n_h}} \right) (\sqrt{c_h n_h}) \right]^2 = \left( \sum_{h=1}^L W_h S_h \sqrt{c_h} \right)^2$$
The Cauchy–Schwarz lower bound is attained if and only if the terms are strictly proportional:
$$\frac{W_h S_h / \sqrt{n_h}}{\sqrt{c_h n_h}} = \text{constant} \implies \frac{W_h S_h}{n_h \sqrt{c_h}} = \text{constant} \implies n_h \propto \frac{W_h S_h}{\sqrt{c_h}}$$
This establishes **Cochran's Optimum Cost Allocation Rule**:
$$n_h \propto \frac{N_h S_h}{\sqrt{c_h}}$$

If the total budget $C$ is fixed, the total sample size $n$ and the individual stratum allocations are given by:
$$n_h = (C - c_0) \frac{\frac{W_h S_h}{\sqrt{c_h}}}{\sum_{k=1}^L W_k S_k \sqrt{c_k}}$$
and the total sample size is:
$$n = \sum_{h=1}^L n_h = (C - c_0) \frac{\sum_{h=1}^L \frac{W_h S_h}{\sqrt{c_h}}}{\sum_{k=1}^L W_k S_k \sqrt{c_k}}$$

Notice the intuitive economic interpretation:
- A stratum receives a **larger sample size** if it contains more units ($N_h$ is large) or exhibits greater variability ($S_h$ is large).
- A stratum receives a **smaller sample size** if it is expensive to survey ($c_h$ is large), scaling inversely with the square root of unit cost $\sqrt{c_h}$.
- When unit costs are identical across all strata ($c_h = c$), the cost factors cancel, and optimum allocation collapses exactly to Neyman allocation.

## The Precision Hierarchy: Proof that V_opt <= V_prop <= V_ran

One of the most elegant and profound theorems in mathematical sampling theory is the definitive precision hierarchy connecting optimum allocation, proportional allocation, and unstratified simple random sampling.

### Total Sum of Squares Decomposition
To compare stratified sampling against simple random sampling, we must decompose the total finite population variance $S^2$. Recall:
$$(N - 1) S^2 = \sum_{h=1}^L \sum_{i=1}^{N_h} (y_{hi} - \bar{Y})^2$$
Add and subtract the stratum mean $\bar{Y}_h$ inside the squared term:
$$(N - 1) S^2 = \sum_{h=1}^L \sum_{i=1}^{N_h} [(y_{hi} - \bar{Y}_h) + (\bar{Y}_h - \bar{Y})]^2$$
Expanding the square:
$$(N - 1) S^2 = \sum_{h=1}^L \sum_{i=1}^{N_h} (y_{hi} - \bar{Y}_h)^2 + 2 \sum_{h=1}^L (\bar{Y}_h - \bar{Y}) \underbrace{\sum_{i=1}^{N_h} (y_{hi} - \bar{Y}_h)}_{= 0} + \sum_{h=1}^L N_h (\bar{Y}_h - \bar{Y})^2$$
$$(N - 1) S^2 = \sum_{h=1}^L (N_h - 1) S_h^2 + \sum_{h=1}^L N_h (\bar{Y}_h - \bar{Y})^2$$
For reasonably large stratum sizes ($N_h \approx N_h - 1$ and $N \approx N - 1$), dividing by $N$ yields the asymptotic variance decomposition:
$$S^2 \approx \sum_{h=1}^L W_h S_h^2 + \sum_{h=1}^L W_h (\bar{Y}_h - \bar{Y})^2$$
where:
- $\sum W_h S_h^2$ is the **average within-stratum variance** ($\bar{S}^2_{within}$).
- $\sum W_h (\bar{Y}_h - \bar{Y})^2$ is the **between-stratum variance** ($S^2_{between}$).

### Comparison 1: Proportional Allocation versus Unstratified SRS
The variance under unstratified simple random sampling (ignoring $1/N$ terms) is:
$$V_{ran}(\bar{y}) \approx \left( \frac{1 - f}{n} \right) S^2 \approx \left( \frac{1 - f}{n} \right) \left[ \sum_{h=1}^L W_h S_h^2 + \sum_{h=1}^L W_h (\bar{Y}_h - \bar{Y})^2 \right]$$
The variance under proportional stratified sampling is:
$$V_{prop}(\bar{y}_{st}) = \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h S_h^2$$
Subtracting $V_{prop}$ from $V_{ran}$:
$$V_{ran}(\bar{y}) - V_{prop}(\bar{y}_{st}) = \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h (\bar{Y}_h - \bar{Y})^2$$
Because $W_h > 0$ and $(\bar{Y}_h - \bar{Y})^2 \ge 0$, the right-hand side is strictly non-negative! Therefore:
$$V_{prop}(\bar{y}_{st}) \le V_{ran}(\bar{y})$$
Equality holds if and only if all stratum means are identical: $\bar{Y}_1 = \bar{Y}_2 = \dots = \bar{Y}_L = \bar{Y}$. Whenever the strata differ in their means, **proportional allocation is guaranteed to be strictly more precise than unstratified simple random sampling**. The variance reduction is directly proportional to the between-stratum heterogeneity.

### Comparison 2: Neyman Optimal Allocation versus Proportional Allocation
Now compare proportional allocation to Neyman optimal allocation for the same total sample size $n$.
Recall:
$$V_{prop}(\bar{y}_{st}) \approx \frac{1}{n} \sum_{h=1}^L W_h S_h^2$$
$$V_{opt}(\bar{y}_{st}) \approx \frac{1}{n} \left( \sum_{h=1}^L W_h S_h \right)^2$$
Subtracting $V_{opt}$ from $V_{prop}$:
$$V_{prop}(\bar{y}_{st}) - V_{opt}(\bar{y}_{st}) = \frac{1}{n} \left[ \sum_{h=1}^L W_h S_h^2 - \left( \sum_{h=1}^L W_h S_h \right)^2 \right]$$
Notice that $\sum_{h=1}^L W_h S_h = \bar{S}$ is the weighted mean of the stratum standard deviations, and $\sum W_h S_h^2$ is the weighted mean of their squares. By the definition of variance:
$$\sum_{h=1}^L W_h S_h^2 - \left( \sum_{h=1}^L W_h S_h \right)^2 = \sum_{h=1}^L W_h (S_h - \bar{S})^2$$
Therefore:
$$V_{prop}(\bar{y}_{st}) - V_{opt}(\bar{y}_{st}) = \frac{1}{n} \sum_{h=1}^L W_h (S_h - \bar{S})^2 \ge 0$$
Equality holds if and only if all stratum standard deviations are identical: $S_1 = S_2 = \dots = S_L = \bar{S}$.

Combining both inequalities yields the **Fundamental Theorem of Stratified Sampling Precision**:
$$V_{opt}(\bar{y}_{st}) \le V_{prop}(\bar{y}_{st}) \le V_{ran}(\bar{y})$$
This theorem proves that:
1. Proportional allocation reduces variance by eliminating **between-stratum mean differences**.
2. Neyman allocation further reduces variance by exploiting **within-stratum standard deviation differences**.

## Stratum Construction and Boundary Demarcation Algorithms

To maximize the efficiency of stratified sampling, the statistician must resolve two practical design problems:
1. How many strata $L$ should be formed?
2. Where should the boundary cut-points $y_0 < y_1 < \dots < y_L$ be placed along a continuous stratification variable?

### How Many Strata?
Empirical studies by Cochran (1977) demonstrate that for a given auxiliary stratification variable $X$ correlated with survey variable $Y$ with correlation $\rho$:
$$\frac{V(\bar{y}_{st})}{V(\bar{y}_{ran})} \approx 1 - \rho^2 \left( 1 - \frac{1}{L^2} \right)$$
As $L$ increases:
- Going from $L = 1$ (unstratified) to $L = 2$ achieves $75\%$ of the maximum possible variance reduction ($1 - 1/4 = 0.75$).
- Going from $L = 2$ to $L = 6$ achieves $97\%$ of the maximum variance reduction ($1 - 1/36 \approx 0.972$).
- Beyond $L = 6$, the marginal gain in precision is infinitesimal, while operational costs and sample management complexity increase substantially. Thus, modern official surveys rarely construct more than 4 to 6 strata along any single continuous dimension.

### The Dalenius–Hodges Cumulative Square Root of Frequency Rule
Tore Dalenius and Joseph Hodges (1959) derived the optimal boundaries for partitioning a continuous variable $Y$ into $L$ strata under Neyman allocation. They proved that the variance is minimized when the boundaries $y_1, y_2, \dots, y_{L-1}$ partition the cumulative distribution of the square root of the population density $\sqrt{f(y)}$ into $L$ equal intervals:
$$\int_{y_{h-1}}^{y_h} \sqrt{f(y)} \, dy = \text{constant} = \frac{1}{L} \int_{y_0}^{y_L} \sqrt{f(y)} \, dy$$

In empirical practice, the population density $f(y)$ is approximated by a finely binned frequency histogram. The **Dalenius–Hodges Protocol** executes as follows:
1. Divide the range of the auxiliary variable $X$ into $K$ fine classes ($K \ge 20$).
2. Calculate the class frequency $f_k$ for each class $k = 1, \dots, K$.
3. Compute the square root of frequency $\sqrt{f_k}$ for each class.
4. Construct the cumulative sum series: $G_k = \sum_{j=1}^k \sqrt{f_j}$, with total $G_{max} = G_K$.
5. Determine the target interval width: $\Delta = G_{max} / L$.
6. Establish the $L - 1$ stratum boundaries at the class cut-points where the cumulative sum $G_k$ equals $\Delta, 2\Delta, \dots, (L - 1)\Delta$.

### Skewed Populations and the Lavallée–Hidiroglou Algorithm
In business and enterprise surveys, economic distributions (such as annual revenue or employee count) are extremely right-skewed: a tiny fraction of massive corporate conglomerates accounts for $80\%$ of total national economic output, while hundreds of thousands of microenterprises account for the remainder.

Applying standard random sampling to such populations creates immense volatility: if a single corporate giant is randomly selected into the sample, its expansion weight $N/n$ multiplies its revenue to an astronomical level; if it is missed, the total is severely underestimated.

To solve this problem, Pierre Lavallée and Michael Hidiroglou (1988) formulated the **Take-All Stratum Framework**:
1. **Take-All (Certainty) Stratum**: All enterprises with size $x_i$ exceeding an optimal threshold $b_{cut}$ are grouped into a certainty stratum ($U_L$). Every unit in this stratum is sampled with probability $\pi_i = 1$ ($n_L = N_L$). Because $f_L = 1$, the finite population correction factor becomes $1 - f_L = 0$, completely **eliminating sampling variance from the largest, most volatile sector of the economy**!
2. **Take-Some Strata**: The remaining $N - N_L$ smaller enterprises are partitioned into $L - 1$ strata using the Dalenius–Hodges rule and sampled via standard Neyman allocation.

The Lavallée–Hidiroglou algorithm iteratively solves for the threshold $b_{cut}$ and the take-some sample sizes to minimize the total sample size $n$ required to achieve a target coefficient of variation $\text{CV}(\hat{Y})$. This architecture is universally deployed by national statistical agencies in annual industrial and commercial censuses.

---

## Fully worked question 1: Lagrange Multiplier Derivation of Cost-Constrained Optimum Allocation

**Question.** A survey research director must design a stratified survey across $L$ administrative strata. The total available variable budget for fieldwork is fixed at $C_{net} = C - c_0$, where $C$ is the total allocated funding and $c_0$ is fixed overhead. The unit cost of collecting data in stratum $h$ is $c_h > 0$.
The variance of the stratified estimator is modeled by:
$$V(\bar{y}_{st}) = \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} - \frac{1}{N} \sum_{h=1}^L W_h S_h^2$$

(a) Using the method of Lagrange multipliers, derive the exact formula for the optimal stratum sample sizes $n_h$ that minimize $V(\bar{y}_{st})$ subject to the budgetary constraint $\sum_{h=1}^L c_h n_h = C_{net}$.
(b) Derive the second-order sufficiency conditions to verify that this critical point is a global minimum.
(c) Derive the closed-form expression for the resulting minimum achievable variance $V_{min}(\bar{y}_{st})$.

**Solution, step 1: Formulate the objective function and Lagrangian.**
The term $\frac{1}{N} \sum_{h=1}^L W_h S_h^2$ in the variance formula is a fixed constant independent of the allocation vector $\mathbf{n} = (n_1, \dots, n_L)^\top$. Therefore, minimizing $V(\bar{y}_{st})$ is mathematically equivalent to minimizing the variable component:
$$f(n_1, \dots, n_L) = \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h}$$
subject to the linear budgetary constraint:
$$g(n_1, \dots, n_L) = \sum_{h=1}^L c_h n_h - C_{net} = 0$$

Define the Lagrangian function $\Lambda: \mathbb{R}^L \times \mathbb{R} \to \mathbb{R}$:
$$\Lambda(n_1, \dots, n_L, \lambda) = \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} + \lambda \left( \sum_{h=1}^L c_h n_h - C_{net} \right)$$
where $\lambda$ is the Lagrange multiplier.

To find the stationary points, set the first-order partial derivatives with respect to each $n_h$ to zero:
$$\frac{\partial \Lambda}{\partial n_h} = -\frac{W_h^2 S_h^2}{n_h^2} + \lambda c_h = 0 \quad \forall h = 1, 2, \dots, L$$
This yields:
$$\frac{W_h^2 S_h^2}{n_h^2} = \lambda c_h \implies n_h^2 = \frac{W_h^2 S_h^2}{\lambda c_h}$$
Taking the positive square root (since sample sizes must be strictly positive, $n_h > 0$):
$$n_h = \frac{W_h S_h}{\sqrt{\lambda} \sqrt{c_h}} = \frac{1}{\sqrt{\lambda}} \left( \frac{W_h S_h}{\sqrt{c_h}} \right)$$

**Solution, step 2: Solve for the Lagrange multiplier and establish the optimal allocation.**
Multiply both sides of the expression for $n_h$ by the unit cost $c_h$:
$$c_h n_h = \frac{1}{\sqrt{\lambda}} \left( \frac{W_h S_h}{\sqrt{c_h}} \right) c_h = \frac{1}{\sqrt{\lambda}} W_h S_h \sqrt{c_h}$$
Summing over all $L$ strata:
$$\sum_{h=1}^L c_h n_h = \frac{1}{\sqrt{\lambda}} \sum_{h=1}^L W_h S_h \sqrt{c_h}$$
Substitute the budget constraint $\sum_{h=1}^L c_h n_h = C_{net}$:
$$C_{net} = \frac{1}{\sqrt{\lambda}} \sum_{h=1}^L W_h S_h \sqrt{c_h} \implies \frac{1}{\sqrt{\lambda}} = \frac{C_{net}}{\sum_{k=1}^L W_k S_k \sqrt{c_k}}$$

Substituting this expression for $1/\sqrt{\lambda}$ back into the equation for $n_h$:
$$n_h = C_{net} \frac{\frac{W_h S_h}{\sqrt{c_h}}}{\sum_{k=1}^L W_k S_k \sqrt{c_k}}$$
Since $W_h = N_h / N$, multiplying numerator and denominator by $N$ produces the equivalent population-count form:
$$n_h = C_{net} \frac{\frac{N_h S_h}{\sqrt{c_h}}}{\sum_{k=1}^L N_k S_k \sqrt{c_k}}$$
This completes the derivation of the cost-optimized stratum sample sizes.

**Solution, step 3: Verify second-order sufficiency conditions and compute minimum variance.**
To prove that this stationary point represents a unique global minimum, evaluate the Hessian matrix $\mathbf{H}$ of the objective function $f(\mathbf{n})$.
Compute the second partial derivatives:
$$\frac{\partial^2 f}{\partial n_h^2} = \frac{2 W_h^2 S_h^2}{n_h^3} > 0 \quad \forall n_h > 0$$
$$\frac{\partial^2 f}{\partial n_h \partial n_k} = 0 \quad \forall h \ne k$$
The Hessian matrix $\mathbf{H} = \text{diag}\left( \frac{2 W_1^2 S_1^2}{n_1^3}, \dots, \frac{2 W_L^2 S_L^2}{n_L^3} \right)$ is a diagonal matrix with strictly positive diagonal entries for all $\mathbf{n} \in \mathbb{R}_{>0}^L$. Therefore, $\mathbf{H}$ is strictly positive definite everywhere on the feasible region, which confirms that $f(\mathbf{n})$ is strictly convex and the critical point is the unique global minimum.

Now evaluate the resulting minimum variance. Substitute the optimal $n_h$ into $\sum \frac{W_h^2 S_h^2}{n_h}$:
$$\sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} = \sum_{h=1}^L \frac{W_h^2 S_h^2}{C_{net} \frac{W_h S_h / \sqrt{c_h}}{\sum_k W_k S_k \sqrt{c_k}}} = \frac{\sum_{k=1}^L W_k S_k \sqrt{c_k}}{C_{net}} \sum_{h=1}^L W_h S_h \sqrt{c_h} = \frac{1}{C_{net}} \left( \sum_{h=1}^L W_h S_h \sqrt{c_h} \right)^2$$
Subtracting the finite population correction constant:
$$V_{min}(\bar{y}_{st}) = \frac{1}{C_{net}} \left( \sum_{h=1}^L W_h S_h \sqrt{c_h} \right)^2 - \frac{1}{N} \sum_{h=1}^L W_h S_h^2$$
This provides the theoretical lower bound on sampling variance achievable under budget $C_{net}$.

---

## Fully worked question 2: Numerical Allocation and Variance Comparison across Heterogeneous Strata

**Question.** An agricultural economics bureau conducts a crop production survey in a rural division containing $N = 10,000$ agricultural holdings partitioned into $L = 3$ distinct agro-ecological strata. The recorded variable $y$ is the commercial paddy rice yield in metric tons. 

The bureau's administrative census files provide the following baseline parameters:
- **Stratum 1 (Coastal Lowlands)**: $N_1 = 5,000$ holdings, standard deviation $S_1 = 4.0$ tons, unit data collection cost $c_1 = 100$ BDT.
- **Stratum 2 (River Basin Alluvial Plain)**: $N_2 = 3,500$ holdings, standard deviation $S_2 = 6.0$ tons, unit data collection cost $c_2 = 100$ BDT.
- **Stratum 3 (Highland Terrace/Plateau)**: $N_3 = 1,500$ holdings, standard deviation $S_3 = 12.0$ tons, unit data collection cost $c_3 = 100$ BDT.

The bureau has authorized a fixed total sample size of $n = 600$ holdings.
(a) Calculate the stratum weights $W_h$ and the overall average within-stratum variance $\bar{S}^2_{within} = \sum W_h S_h^2$.
(b) Determine the stratum sample sizes $(n_1, n_2, n_3)$ and calculate the variance of the stratified estimator $V(\bar{y}_{st})$ under:
    (i) Equal Allocation,
    (ii) Proportional Allocation,
    (iii) Neyman Optimal Allocation.
(c) Calculate the Relative Efficiency of Neyman allocation compared to Proportional allocation and Equal allocation.

**Solution, step 1: Compute stratum weights and variances.**
The total population is $N = 5,000 + 3,500 + 1,500 = 10,000$.
The stratum weights are:
$$W_1 = \frac{5,000}{10,000} = 0.50, \quad W_2 = \frac{3,500}{10,000} = 0.35, \quad W_3 = \frac{1,500}{10,000} = 0.15$$
Verify that $\sum W_h = 0.50 + 0.35 + 0.15 = 1.00$.

The stratum variances $S_h^2$ are:
$$S_1^2 = (4.0)^2 = 16.0, \quad S_2^2 = (6.0)^2 = 36.0, \quad S_3^2 = (12.0)^2 = 144.0$$
Compute the products:
$$W_1 S_1 = (0.50)(4.0) = 2.00$$
$$W_2 S_2 = (0.35)(6.0) = 2.10$$
$$W_3 S_3 = (0.15)(12.0) = 1.80$$
Sum of products:
$$\sum_{h=1}^3 W_h S_h = 2.00 + 2.10 + 1.80 = 5.90$$

Compute the weighted average of stratum variances:
$$\bar{S}^2_{within} = \sum_{h=1}^3 W_h S_h^2 = (0.50)(16.0) + (0.35)(36.0) + (0.15)(144.0)$$
$$\bar{S}^2_{within} = 8.00 + 12.60 + 21.60 = 42.20$$

The constant finite population correction term is:
$$\frac{1}{N} \sum_{h=1}^3 W_h S_h^2 = \frac{42.20}{10,000} = 0.00422$$

**Solution, step 2: Allocation schemes and variance computations.**

### (i) Equal Allocation ($n_h = n / L = 600 / 3 = 200$)
$$n_1 = 200, \quad n_2 = 200, \quad n_3 = 200$$
Evaluate the variance $V_{eq}(\bar{y}_{st}) = \sum_{h=1}^3 \frac{W_h^2 S_h^2}{n_h} - \frac{1}{N} \sum W_h S_h^2$:
$$\sum_{h=1}^3 \frac{W_h^2 S_h^2}{n_h} = \frac{W_1^2 S_1^2}{200} + \frac{W_2^2 S_2^2}{200} + \frac{W_3^2 S_3^2}{200}$$
$$W_1^2 S_1^2 = (0.50)^2 (16) = (0.25)(16) = 4.00$$
$$W_2^2 S_2^2 = (0.35)^2 (36) = (0.1225)(36) = 4.41$$
$$W_3^2 S_3^2 = (0.15)^2 (144) = (0.0225)(144) = 3.24$$
$$\sum_{h=1}^3 W_h^2 S_h^2 = 4.00 + 4.41 + 3.24 = 11.65$$
Thus:
$$\sum_{h=1}^3 \frac{W_h^2 S_h^2}{n_h} = \frac{11.65}{200} = 0.05825$$
Subtracting the FPC correction:
$$V_{eq}(\bar{y}_{st}) = 0.05825 - 0.00422 = 0.054030 \text{ tons}^2$$
Standard error: $\text{SE}_{eq} = \sqrt{0.054030} \approx 0.23244$ tons.

### (ii) Proportional Allocation ($n_h = n W_h$)
$$n_1 = 600 \times 0.50 = 300$$
$$n_2 = 600 \times 0.35 = 210$$
$$n_3 = 600 \times 0.15 = 90$$
Check: $n_1 + n_2 + n_3 = 300 + 210 + 90 = 600$.

The overall sampling fraction is $f = 600 / 10,000 = 0.06$.
The variance under proportional allocation is:
$$V_{prop}(\bar{y}_{st}) = \left( \frac{1 - f}{n} \right) \sum_{h=1}^3 W_h S_h^2 = \left( \frac{1 - 0.06}{600} \right) (42.20) = \left( \frac{0.94}{600} \right) (42.20) = \frac{39.668}{600} \approx 0.066113 \text{ tons}^2$$
Standard error: $\text{SE}_{prop} = \sqrt{0.066113} \approx 0.25712$ tons.

### (iii) Neyman Optimal Allocation ($n_h = n \frac{W_h S_h}{\sum W_k S_k}$)
Recall $\sum W_k S_k = 5.90$.
$$n_1 = 600 \times \frac{2.00}{5.90} = 600 \times 0.338983 \approx 203.39 \implies 203$$
$$n_2 = 600 \times \frac{2.10}{5.90} = 600 \times 0.355932 \approx 213.56 \implies 214$$
$$n_3 = 600 \times \frac{1.80}{5.90} = 600 \times 0.305085 \approx 183.05 \implies 183$$
Check: $203 + 214 + 183 = 600$.

Compute the theoretical variance under Neyman allocation:
$$V_{opt}(\bar{y}_{st}) = \frac{1}{n} \left( \sum_{h=1}^3 W_h S_h \right)^2 - \frac{1}{N} \sum_{h=1}^3 W_h S_h^2$$
$$\frac{1}{600} (5.90)^2 - 0.00422 = \frac{34.81}{600} - 0.00422 = 0.0580167 - 0.00422 = 0.053797 \text{ tons}^2$$
Standard error: $\text{SE}_{opt} = \sqrt{0.053797} \approx 0.23194$ tons.

**Solution, step 3: Evaluate Relative Efficiency.**
Compare Neyman optimal allocation against Proportional allocation:
$$\text{RE}(opt \text{ vs } prop) = \frac{V_{prop}(\bar{y}_{st})}{V_{opt}(\bar{y}_{st})} = \frac{0.066113}{0.053797} \approx 1.2289$$
Neyman allocation is **$22.89\%$ more efficient** than proportional allocation!
The percentage variance reduction achieved by switching from proportional to Neyman allocation is:
$$\text{Gain} = \frac{0.066113 - 0.053797}{0.066113} \times 100\% = \frac{0.012316}{0.066113} \times 100\% \approx 18.63\%$$

Compare Neyman optimal allocation against Equal allocation:
$$\text{RE}(opt \text{ vs } equal) = \frac{V_{eq}(\bar{y}_{st})}{V_{opt}(\bar{y}_{st})} = \frac{0.054030}{0.053797} \approx 1.0043$$

Notice why Proportional allocation performed poorly here: Stratum 3 has only $15\%$ of the population ($W_3 = 0.15$), but its variance is massive ($S_3 = 12$, nine times the variance of Stratum 1). Proportional allocation allocated only 90 units to this volatile stratum, allowing Stratum 3's high variance to inflate the overall error. Neyman allocation corrected this mistake by shifting sample size from Stratum 1 into Stratum 3 (increasing $n_3$ from 90 to 183), achieving substantial variance reduction.

---

## Fully worked question 3: Proof of the Variance Reduction Hierarchy and Gain in Precision

**Question.** A statistical theoretician analyzes the relative efficiency of stratified sampling against simple random sampling without replacement (SRSWOR). 
(a) For a population of $N$ units partitioned into $L$ strata, prove from the exact sum of squares identity that:
$$V_{prop}(\bar{y}_{st}) = V_{ran}(\bar{y}) - \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h (\bar{Y}_h - \bar{Y})^2 + O\left(\frac{1}{N}\right)$$
(b) Prove that the variance reduction of Neyman allocation over proportional allocation is given by:
$$V_{opt}(\bar{y}_{st}) = V_{prop}(\bar{y}_{st}) - \frac{1}{n} \sum_{h=1}^L W_h (S_h - \bar{S})^2$$
where $\bar{S} = \sum_{h=1}^L W_h S_h$.
(c) Suppose a socioeconomic survey of $N = 50,000$ households has overall variance $S^2 = 1,000$. The population is stratified into $L = 4$ income strata with weights $W = (0.40, 0.30, 0.20, 0.10)$ and stratum means $\bar{Y} = (20, 35, 60, 110)$. The stratum standard deviations are $S = (15, 20, 30, 50)$. A sample of $n = 1,000$ is drawn. Calculate the numerical variance under $V_{ran}$, $V_{prop}$, and $V_{opt}$, and compute the percentage gains in precision.

**Solution, step 1: Prove the exact relationship between $V_{ran}$ and $V_{prop}$.**
Recall the exact finite population sum of squares identity:
$$(N - 1) S^2 = \sum_{h=1}^L (N_h - 1) S_h^2 + \sum_{h=1}^L N_h (\bar{Y}_h - \bar{Y})^2$$
Divide both sides by $N - 1$:
$$S^2 = \sum_{h=1}^L \frac{N_h - 1}{N - 1} S_h^2 + \sum_{h=1}^L \frac{N_h}{N - 1} (\bar{Y}_h - \bar{Y})^2$$
Since $W_h = N_h / N$, we have $\frac{N_h}{N - 1} = W_h \frac{N}{N - 1} \approx W_h$.
Approximating to order $O(1/N)$:
$$S^2 = \sum_{h=1}^L W_h S_h^2 + \sum_{h=1}^L W_h (\bar{Y}_h - \bar{Y})^2$$

The variance of the sample mean under unstratified SRSWOR is:
$$V_{ran}(\bar{y}) = \left( \frac{1 - f}{n} \right) S^2$$
Substituting the expansion of $S^2$:
$$V_{ran}(\bar{y}) = \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h S_h^2 + \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h (\bar{Y}_h - \bar{Y})^2$$
Recall that under proportional stratified sampling, $V_{prop}(\bar{y}_{st}) = \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h S_h^2$.
Therefore:
$$V_{ran}(\bar{y}) - V_{prop}(\bar{y}_{st}) = \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h (\bar{Y}_h - \bar{Y})^2 \ge 0$$
This proves that $V_{prop}(\bar{y}_{st}) \le V_{ran}(\bar{y})$, with equality if and only if all stratum means are identical.

**Solution, step 2: Prove the variance difference between Proportional and Neyman allocation.**
Consider the variances ignoring $1/N$ terms:
$$V_{prop}(\bar{y}_{st}) \approx \frac{1}{n} \sum_{h=1}^L W_h S_h^2$$
$$V_{opt}(\bar{y}_{st}) \approx \frac{1}{n} \left( \sum_{h=1}^L W_h S_h \right)^2 = \frac{1}{n} \bar{S}^2$$
where $\bar{S} = \sum_{h=1}^L W_h S_h$.
Subtracting the two expressions:
$$V_{prop}(\bar{y}_{st}) - V_{opt}(\bar{y}_{st}) = \frac{1}{n} \left[ \sum_{h=1}^L W_h S_h^2 - \bar{S}^2 \right]$$
Now consider the algebraic identity for the weighted variance of the standard deviations:
$$\sum_{h=1}^L W_h (S_h - \bar{S})^2 = \sum_{h=1}^L W_h (S_h^2 - 2 \bar{S} S_h + \bar{S}^2) = \sum_{h=1}^L W_h S_h^2 - 2 \bar{S} \sum_{h=1}^L W_h S_h + \bar{S}^2 \sum_{h=1}^L W_h$$
$$= \sum_{h=1}^L W_h S_h^2 - 2 \bar{S}^2 + \bar{S}^2 = \sum_{h=1}^L W_h S_h^2 - \bar{S}^2$$
Substituting this back gives:
$$V_{prop}(\bar{y}_{st}) - V_{opt}(\bar{y}_{st}) = \frac{1}{n} \sum_{h=1}^L W_h (S_h - \bar{S})^2 \ge 0$$
This completes the mathematical proof that $V_{opt} \le V_{prop}$, with equality if and only if all stratum standard deviations are identical.

**Solution, step 3: Numerical evaluation for the socioeconomic survey.**
Given: $N = 50,000, n = 1,000 \implies f = 1,000 / 50,000 = 0.02$.
The FPC factor is $1 - f = 1 - 0.02 = 0.98$.
$S^2 = 1,000$.

1. Variance under unstratified simple random sampling:
   $$V_{ran}(\bar{y}) = \left( \frac{1 - f}{n} \right) S^2 = \left( \frac{0.98}{1,000} \right) (1,000) = 0.98000$$

2. Variance under proportional allocation:
   Compute the overall population mean $\bar{Y} = \sum W_h \bar{Y}_h$:
   $$\bar{Y} = (0.40)(20) + (0.30)(35) + (0.20)(60) + (0.10)(110) = 8.0 + 10.5 + 12.0 + 11.0 = 41.5$$
   Compute the between-stratum variance $\sum W_h (\bar{Y}_h - \bar{Y})^2$:
   $$(20 - 41.5)^2 = (-21.5)^2 = 462.25 \implies (0.40)(462.25) = 184.90$$
   $$(35 - 41.5)^2 = (-6.5)^2 = 42.25 \implies (0.30)(42.25) = 12.675$$
   $$(60 - 41.5)^2 = (18.5)^2 = 342.25 \implies (0.20)(342.25) = 68.45$$
   $$(110 - 41.5)^2 = (68.5)^2 = 4,692.25 \implies (0.10)(4,692.25) = 469.225$$
   Sum of between-stratum terms:
   $$S^2_{between} = 184.90 + 12.675 + 68.45 + 469.225 = 735.25$$

   By the variance decomposition, the within-stratum variance is:
   $$\bar{S}^2_{within} = S^2 - S^2_{between} = 1,000 - 735.25 = 264.75$$
   Alternatively, calculate $\sum W_h S_h^2$ directly:
   $$S_1^2 = 225 \implies (0.40)(225) = 90.0$$
   $$S_2^2 = 400 \implies (0.30)(400) = 120.0$$
   $$S_3^2 = 900 \implies (0.20)(900) = 180.0$$
   $$S_4^2 = 2,500 \implies (0.10)(2,500) = 250.0$$
   $$\sum W_h S_h^2 = 90 + 120 + 180 + 250 = 640.0$$
   (Note: When individual stratum variances are supplied as $S = (15, 20, 30, 50)$, $\sum W_h S_h^2 = 640.0$. The total $S^2 = 640.0 + 735.25 = 1,375.25$. We evaluate using the true exact parameters $S_h$ and $S^2 = 1,375.25$.)

   Recalculate exact $V_{ran}$ with $S^2 = 1,375.25$:
   $$V_{ran} = \frac{0.98}{1,000} (1,375.25) = 1.347745$$
   Variance under proportional allocation:
   $$V_{prop} = \frac{0.98}{1,000} \sum W_h S_h^2 = \frac{0.98}{1,000} (640.0) = 0.627200$$

3. Variance under Neyman optimal allocation:
   Compute $\bar{S} = \sum W_h S_h$:
   $$\bar{S} = (0.40)(15) + (0.30)(20) + (0.20)(30) + (0.10)(50) = 6.0 + 6.0 + 6.0 + 5.0 = 23.0$$
   $$\bar{S}^2 = (23.0)^2 = 529.0$$
   Neyman variance:
   $$V_{opt} = \frac{1}{1,000} (529.0) - \frac{640.0}{50,000} = 0.52900 - 0.01280 = 0.516200$$

### Precision Comparisons
1. **Gain of Proportional Allocation over SRSWOR**:
   $$\text{Reduction} = \frac{V_{ran} - V_{prop}}{V_{ran}} \times 100\% = \frac{1.347745 - 0.627200}{1.347745} \times 100\% = \frac{0.720545}{1.347745} \times 100\% \approx 53.46\%$$
   Proportional stratification eliminates the substantial between-income mean differences, cutting sampling variance by more than half ($53.46\%$ reduction).

2. **Gain of Neyman Allocation over Proportional Allocation**:
   $$\text{Reduction} = \frac{V_{prop} - V_{opt}}{V_{prop}} \times 100\% = \frac{0.627200 - 0.516200}{0.627200} \times 100\% = \frac{0.111000}{0.627200} \times 100\% \approx 17.70\%$$
   Neyman allocation extracts an additional $17.70\%$ variance reduction by tailoring sample size to the standard deviation gradient ($S_h$ ranging from 15 to 50).

3. **Total Gain of Neyman Allocation over SRSWOR**:
   $$\text{Total Relative Efficiency} = \frac{V_{ran}}{V_{opt}} = \frac{1.347745}{0.516200} \approx 2.6109$$
   Neyman allocation is **$2.61$ times more efficient** than unstratified simple random sampling. To achieve the same precision as this $n = 1,000$ Neyman stratified sample, an unstratified SRS would require $n = 2,611$ households!

---

## Stratum Boundary Determination: The Dalenius–Hodges Cumulative Square-Root Rule

In our theoretical analysis of stratified sampling, we assumed that the finite population was already partitioned into $L$ clearly defined strata. When strata are formed by qualitative administrative categories—such as provinces, hospital departments, or school districts—stratum boundaries are natural and fixed. However, when stratification is based on a continuous quantitative variable—such as annual household income, farm acreage, or enterprise employee count—the survey methodologist faces a critical design question: **Where should the numerical cut-points $y_0 < y_1 < y_2 < \dots < y_L$ be placed along the continuous distribution to maximize precision?**

### Mathematical Formulation of Optimal Stratification

Let $y$ be a continuous stratification variable governed by a probability density function $f(y)$ on the finite or semi-infinite interval $[a, b]$. We wish to partition $[a, b]$ into $L$ non-overlapping strata defined by boundary cut-points:
$$a = y_0 < y_1 < y_2 < \dots < y_{L-1} < y_L = b$$

For stratum $h$ defined by the interval $(y_{h-1}, y_h]$, the population proportion is:
$$W_h = \int_{y_{h-1}}^{y_h} f(y) \, dy$$
The stratum mean is:
$$\mu_h = \frac{1}{W_h} \int_{y_{h-1}}^{y_h} y f(y) \, dy$$
The stratum variance is:
$$\sigma_h^2 = \frac{1}{W_h} \int_{y_{h-1}}^{y_h} (y - \mu_h)^2 f(y) \, dy$$

Under Neyman optimal allocation with fixed total sample size $n$, the variance of the stratified sample mean is:
$$V(\bar{y}_{st}) = \frac{1}{n} \left( \sum_{h=1}^L W_h \sigma_h \right)^2 - \frac{1}{N} \sum_{h=1}^L W_h \sigma_h^2$$

Ignoring the negligible second term, minimizing $V(\bar{y}_{st})$ is mathematically equivalent to minimizing the sum of weighted stratum standard deviations:
$$\min_{y_1, \dots, y_{L-1}} \sum_{h=1}^L W_h \sigma_h$$

Differentiating this objective function with respect to boundary cut-point $y_h$ and setting the derivative to zero yields the exact theoretical condition for optimal boundaries (Dalenius, 1950):
$$\frac{\sigma_h^2 + (y_h - \mu_h)^2}{\sigma_h} = \frac{\sigma_{h+1}^2 + (y_h - \mu_{h+1})^2}{\sigma_{h+1}} \quad (h = 1, 2, \dots, L - 1)$$

Because this system of non-linear equations involves implicit integrals of $f(y)$, finding an exact analytical solution for general non-Gaussian distributions is intractable.

### Derivation of the Dalenius–Hodges $\text{cum} \sqrt{f}$ Approximation

In 1959, Tore Dalenius and Joseph L. Hodges Jr. discovered an extraordinary mathematical approximation that transforms this intractable optimization into a straightforward, universal algorithmic procedure.

Assume that the number of strata $L$ is moderately large, so that within any single stratum $h$, the interval width $k_h = y_h - y_{h-1}$ is relatively narrow. Over this narrow interval $(y_{h-1}, y_h]$, the density function $f(y)$ can be approximated as a uniform constant equal to its midpoint value $f(u_h)$, where $u_h = \frac{y_{h-1} + y_h}{2}$.

Under this local uniformity approximation:
1. The stratum weight is:
   $$W_h = \int_{y_{h-1}}^{y_h} f(y) \, dy \approx f(u_h) (y_h - y_{h-1}) = f(u_h) k_h$$
2. The stratum variance is approximately the variance of a continuous uniform distribution of width $k_h$:
   $$\sigma_h^2 \approx \frac{(y_h - y_{h-1})^2}{12} = \frac{k_h^2}{12} \implies \sigma_h \approx \frac{k_h}{\sqrt{12}} = \frac{y_h - y_{h-1}}{\sqrt{12}}$$

Now evaluate the product $W_h \sigma_h$:
$$W_h \sigma_h \approx \left[ f(u_h) (y_h - y_{h-1}) \right] \left[ \frac{y_h - y_{h-1}}{\sqrt{12}} \right] = \frac{1}{\sqrt{12}} f(u_h) (y_h - y_{h-1})^2$$

Notice that:
$$\int_{y_{h-1}}^{y_h} \sqrt{f(y)} \, dy \approx \sqrt{f(u_h)} (y_h - y_{h-1})$$
Squaring both sides:
$$\left( \int_{y_{h-1}}^{y_h} \sqrt{f(y)} \, dy \right)^2 \approx f(u_h) (y_h - y_{h-1})^2$$

Substituting this back into the expression for $W_h \sigma_h$:
$$W_h \sigma_h \approx \frac{1}{\sqrt{12}} \int_{y_{h-1}}^{y_h} \sqrt{f(y)} \, dy \cdot (y_h - y_{h-1})$$

To minimize the sum $\sum_{h=1}^L W_h \sigma_h$, Dalenius and Hodges proved that the integral of the square root of the density must be **equalized across all $L$ strata**:
$$\int_{y_0}^{y_1} \sqrt{f(y)} \, dy = \int_{y_1}^{y_2} \sqrt{f(y)} \, dy = \dots = \int_{y_{L-1}}^{y_L} \sqrt{f(y)} \, dy = \frac{1}{L} \int_{y_0}^{y_L} \sqrt{f(y)} \, dy$$

This celebrated result is known as the **Dalenius–Hodges Cumulative Square-Root Rule** ($\text{cum} \sqrt{f}$ rule).

### Operational Step-by-Step Algorithm for Empirical Data

To construct optimal stratum boundaries from an empirical frequency distribution:
1. **Histogram Construction**: Tabulate the continuous variable $y$ into $K$ fine, equal-width discrete bins ($K \ge 20$ or $30$). Let $f_i$ denote the frequency (or count) of observations falling into the $i$-th bin ($i = 1, \dots, K$).
2. **Square-Root Transformation**: Compute the square root of each bin frequency: $r_i = \sqrt{f_i}$.
3. **Cumulative Summation**: Calculate the running cumulative total:
   $$C_k = \sum_{i=1}^k \sqrt{f_i} \quad (k = 1, 2, \dots, K)$$
   Let $C_K$ denote the total aggregate cumulative sum.
4. **Equal-Interval Partitioning**: Divide the total cumulative sum into $L$ equal intervals:
   $$\Delta = \frac{C_K}{L}$$
   The target boundary values on the cumulative scale are:
   $$T_h = h \times \Delta = h \times \frac{C_K}{L} \quad (h = 1, 2, \dots, L - 1)$$
5. **Boundary Cut-Point Identification**: The empirical stratum boundary $y_h$ is the upper limit of the bin where the cumulative sum $C_k$ first reaches or crosses $T_h$.

The Dalenius–Hodges rule guarantees that under Neyman allocation, the resulting stratified design achieves near-optimal variance reduction without requiring complex numerical optimization.

---

## The Lavallée–Hidiroglou (L-H) Algorithm for Skewed Business Populations

In establishment, agricultural, and financial surveys, the distribution of economic variables (such as business revenues, bank deposits, or commercial farm acreages) exhibits extreme positive skewness. A massive fraction of the total population value is concentrated within a tiny handful of colossal enterprises, while thousands of small businesses contribute minuscule shares to the national total.

If standard equal-probability or proportional stratified sampling is applied to such highly skewed populations, the sampling variance is dominated by whether any mega-enterprises happen to enter the sample. To solve this structural problem, Pierre Lavallée and Michael Hidiroglou (1988) formulated an optimal stratification architecture tailored for business surveys.

### The Take-All / Take-Some Stratum Architecture

The population is partitioned into $L$ strata:
- **Take-Some Strata ($h = 1, 2, \dots, L - 1$)**: These strata contain small and medium enterprises. A probability sample of size $n_h < N_h$ is selected from stratum $h$.
- **Take-All (Certainty) Stratum ($h = L$)**: This stratum contains all mega-enterprises whose size exceeds a designated threshold $b$. Every single enterprise in this stratum is enumerated completely ($n_L = N_L$).

Because every unit in the take-all stratum is surveyed with certainty ($f_L = n_L / N_L = 1$), the sampling variance from the take-all stratum is **identically zero**:
$$V_L = \frac{1 - f_L}{n_L} S_L^2 = \frac{1 - 1}{N_L} S_L^2 = 0$$
The colossal enterprises are known without any sampling error, completely eliminating the primary source of variance in economic surveys!

### The Optimization Problem

The objective of the Lavallée–Hidiroglou algorithm is to determine the cut-off boundary $b$ between the take-some and take-all strata, alongside the boundaries $y_1 < \dots < y_{L-2}$ within the take-some strata, to:
$$\min n = n_L + \sum_{h=1}^{L-1} n_h = N_L + \sum_{h=1}^{L-1} n_h$$
subject to achieving a pre-specified target **Coefficient of Variation ($CV_{target}$)**:
$$CV(\hat{Y}) = \frac{\sqrt{V(\hat{Y})}}{Y} \le CV_{target}$$

where the total variance across the take-some strata under Neyman allocation is:
$$V(\hat{Y}) = \sum_{h=1}^{L-1} \frac{N_h^2 (1 - f_h)}{n_h} S_h^2 = \frac{\left( \sum_{h=1}^{L-1} N_h S_h \right)^2}{n - N_L} - \sum_{h=1}^{L-1} N_h S_h^2$$

### The Iterative L-H Algorithm

Lavallée and Hidiroglou established an iterative algorithm:
1. **Initial Cut-off Guess**: Choose an initial threshold $b^{(0)}$ (for example, isolating the top $5\%$ of enterprises into the take-all stratum).
2. **Take-Some Stratification**: Apply the Dalenius–Hodges $\text{cum} \sqrt{f}$ rule to partition the remaining take-some sub-population into $L - 1$ strata.
3. **Allocation Computation**: Calculate stratum standard deviations $S_h$ and compute required sample sizes $n_h$ to satisfy the $CV_{target}$ constraint.
4. **Cut-off Boundary Update**: Update the threshold $b$ by solving the gradient condition:
   $$b^{(t+1)} = \mu_{L-1} + \sqrt{\frac{S_{L-1}^2}{1 - \frac{N_{L-1}}{n_{L-1}} \left( \frac{CV^2 Y^2 + \sum N_h S_h^2}{\sum N_h S_h} \right)^{-1}}}$$
5. **Convergence**: Repeat steps 2 through 4 until the cut-off boundary $b$ stabilizes ($|b^{(t+1)} - b^{(t)}| < \epsilon$).

Modern survey packages in R (such as `stratification::strata.LH()`) implement the Lavallée–Hidiroglou algorithm, saving statistical agencies tens of millions of dollars annually in industrial census operations.

---

## Multi-Objective Stratified Allocation: Bethel's Algorithm

In our previous derivation of Neyman optimal allocation, the optimization problem assumed a single survey characteristic $y$. The sample size allocated to stratum $h$ was proportional to $W_h S_h$:
$$n_h \propto W_h S_h$$

In practical multi-purpose surveys, questionnaires measure dozens or hundreds of distinct indicators simultaneously:
- An agricultural survey measures wheat yield, livestock counts, fertilizer expenditures, and farm machinery assets.
- A labor force survey measures unemployment rates, weekly hours worked, informal sector earnings, and vocational training participation.

Each survey variable $y^{(p)}$ ($p = 1, 2, \dots, P$) exhibits a distinct variance pattern across strata. For variable 1, Stratum 1 may have the highest variance ($S_{1,1} \gg S_{2,1}$); for variable 2, Stratum 2 may have the highest variance ($S_{2,2} \gg S_{1,2}$). A Neyman allocation tailored exclusively to variable 1 will result in an unacceptably large standard error for variable 2!

### The Multi-Objective Optimization Problem

To achieve balanced precision across all $P$ survey variables simultaneously within a fixed total cost, J. W. Bethel (1989) formulated multi-objective allocation as a convex mathematical programming problem.

Let $C = c_0 + \sum_{h=1}^L c_h n_h$ denote the operational survey cost function, where $c_h$ is the marginal cost per interview in stratum $h$.
For each survey variable $p \in \{1, 2, \dots, P\}$, let $V_p$ denote the variance of the stratified estimator $\hat{Y}^{(p)}$, and let $V_{p,target}$ denote the maximum acceptable variance budget for that variable.

The optimization problem is:
$$\min_{\{n_1, \dots, n_L\}} \sum_{h=1}^L c_h n_h \quad \text{subject to} \quad V_p(\hat{Y}^{(p)}) \le V_{p,target} \quad (p = 1, 2, \dots, P) \quad \text{and} \quad 0 < n_h \le N_h$$

The variance of variable $p$ under stratified sampling is:
$$V_p = \sum_{h=1}^L \frac{N_h^2 (1 - f_h)}{n_h} S_{h,p}^2 = \sum_{h=1}^L \frac{N_h^2 S_{h,p}^2}{n_h} - \sum_{h=1}^L N_h S_{h,p}^2$$

Define the variance tolerance:
$$v_p = V_{p,target} + \sum_{h=1}^L N_h S_{h,p}^2$$
and define the normalized stratum dispersion constants:
$$a_{h,p} = \frac{N_h^2 S_{h,p}^2}{v_p}$$

The constraints can be written compactly as:
$$\sum_{h=1}^L \frac{a_{h,p}}{n_h} \le 1 \quad (p = 1, 2, \dots, P)$$

### Bethel's Kuhn–Tucker Solution

Bethel applied Kuhn–Tucker duality theory to solve this convex programming problem. Let $\boldsymbol{\alpha} = (\alpha_1, \dots, \alpha_P)^\top$ denote the vector of non-negative Lagrange multipliers associated with the $P$ precision constraints ($\alpha_p \ge 0, \sum \alpha_p = 1$).

Bethel proved that the optimal allocation $n_h^*$ is given by:
$$n_h^* = \frac{\sqrt{\frac{1}{c_h} \sum_{p=1}^P \alpha_p^* a_{h,p}}}{\sum_{k=1}^L \sqrt{c_k \sum_{p=1}^P \alpha_p^* a_{k,p}}}$$
where the optimal multiplier vector $\boldsymbol{\alpha}^*$ is found by maximizing the concave dual objective function:
$$\max_{\boldsymbol{\alpha} \ge \mathbf{0}, \sum \alpha_p = 1} \sum_{h=1}^L \sqrt{c_h \sum_{p=1}^P \alpha_p a_{h,p}}$$

#### Substantive Interpretation of Bethel's Multipliers:
The Lagrange multiplier $\alpha_p^*$ represents the **shadow price** (binding tightness) of the precision constraint for variable $p$:
- If $\alpha_p^* = 0$, the precision target for variable $p$ is easily satisfied as a byproduct of sampling for other variables; it exerts zero influence on sample allocation.
- If $\alpha_p^* > 0$, the precision target for variable $p$ is actively binding and constrains the design. The composite allocation blends the Neyman standard deviations weighted by their shadow prices $\alpha_p^*$.

Bethel's algorithm guarantees that every primary survey indicator achieves its specified precision threshold at the absolute minimum financial expenditure.

---

## Robustness of Neyman Allocation Against Misspecified Variances

A common logistical challenge in applying Neyman optimal allocation ($n_h \propto W_h S_h$) is that the true population stratum standard deviations $S_h$ are unknown prior to conducting the survey. Methodologists must approximate $S_h$ using pilot studies, historical census datasets, or administrative proxy records, yielding guessed standard deviations $S_h^*$.

The allocated sample sizes are based on these proxy values:
$$n_h^* = n \frac{W_h S_h^*}{\sum W_k S_k^*}$$

What happens to survey precision if the guessed standard deviations $S_h^*$ deviate from the true values $S_h$?

Let $V_{opt}$ denote the true minimum variance achieved if exact $S_h$ were known, and let $V(S^*)$ denote the actual variance achieved using the proxy values $S_h^*$.
Cochran (1977) derived the exact proportional loss in efficiency:
$$\frac{V(S^*) - V_{opt}}{V_{opt}} = \frac{\left( \sum W_h S_h^* \right) \left( \sum \frac{W_h S_h^2}{S_h^*} \right) - \left( \sum W_h S_h \right)^2}{\left( \sum W_h S_h \right)^2}$$

By the Cauchy–Schwarz inequality, this relative variance inflation is bounded by:
$$\frac{V(S^*) - V_{opt}}{V_{opt}} \approx \sum_{h=1}^L W_h \left( \frac{S_h^* - S_h}{S_h} \right)^2$$

#### Crucial Practical Insight:
The variance penalty is quadratic in the relative estimation error $\frac{S_h^* - S_h}{S_h}$.
- If the pilot estimates of $S_h$ have a $10\%$ relative error across strata, the variance inflation is approximately $(0.10)^2 = 0.01$, or only **$1\%$ above the theoretical minimum**!
- Even if $S_h$ estimates are corrupted by a substantial $20\%$ error, the variance increases by only $4\%$.
- In contrast, falling back to proportional allocation ($S_h^* = \bar{S}$) incurs a variance penalty equal to $\frac{V(S_h)}{(\sum W_h S_h)^2}$, which often exceeds $20\%$ to $50\%$.

**Rule of Thumb**: As long as the estimated standard deviations $S_h^*$ correctly identify which strata are highly variable and which are homogeneous, Neyman allocation remains vastly superior to proportional allocation. Moderate errors in the exact numeric values of $S_h$ exert negligible impact on survey precision.

---

## Post-Stratification: Theory, Random Sample Sizes and Asymptotic Efficiency

In classical stratified sampling (pre-stratification), the stratum membership of every unit in the finite population is known in advance on the sampling frame. Independent probability samples are then drawn separately within each stratum. In empirical survey practice, however, many vital demographic and socioeconomic characteristics—such as educational attainment, household income brackets, health insurance status, or voting preference—are **unobserved on the sampling frame** at the time the sample is selected. An agency cannot draw a pre-stratified sample on variables that do not exist in the frame registry.

Nonetheless, external administrative sources (such as a national decennial census or high-accuracy demographic register) frequently provide the exact population counts or proportions for these strata:
$$N_h \quad \text{and} \quad W_h = \frac{N_h}{N} \quad (h = 1, 2, \dots, L)$$
Under these conditions, the survey statistician draws an unstratified simple random sample without replacement (SRSWOR) of size $n$ from the entire population, measures both the survey variable $y_i$ and the stratum classification variable on all $n$ respondents, and classifies the sampled units into strata post hoc. This technique is known as **Post-Stratification**.

### The Post-Stratified Estimator

Let $s_h$ denote the set of sampled units that happen to fall into stratum $h$, and let:
$$n_h = \sum_{i \in s} I(i \in U_h)$$
denote the observed sample size in stratum $h$, where $\sum_{h=1}^L n_h = n$.

The sample mean within stratum $h$ is:
$$\bar{y}_h = \frac{1}{n_h} \sum_{i \in s_h} y_i \quad (\text{defined when } n_h > 0)$$

The **Post-Stratified Estimator of the Population Mean** is:
$$\bar{y}_{post} = \sum_{h=1}^L W_h \bar{y}_h = \sum_{h=1}^L \frac{N_h}{N} \bar{y}_h$$

The corresponding estimator of the population total is $\hat{Y}_{post} = N \bar{y}_{post} = \sum_{h=1}^L N_h \bar{y}_h$.

### Conditional and Unconditional Moments

Unlike pre-stratification where the sample sizes $n_h$ are fixed constants chosen by the statistician, in post-stratification **the sample sizes $n_h$ are random variables**. 
The vector of sample counts $\mathbf{n} = (n_1, n_2, \dots, n_L)^\top$ follows a multivariate Hypergeometric distribution:
$$E(n_h) = n W_h \quad \text{and} \quad V(n_h) = n W_h (1 - W_h) \left( \frac{N - n}{N - 1} \right)$$

#### Conditional Unbiasedness:
First, condition on the realized sample allocation vector $\mathbf{n} = (n_1, \dots, n_L)$, assuming $n_h \ge 1$ for all $h$:
Conditional on $n_h$, the $n_h$ units observed in stratum $h$ represent an exact SRSWOR of size $n_h$ from the $N_h$ units of stratum $h$. Therefore:
$$E(\bar{y}_h \mid n_h) = \bar{Y}_h \implies E(\bar{y}_{post} \mid \mathbf{n}) = \sum_{h=1}^L W_h E(\bar{y}_h \mid n_h) = \sum_{h=1}^L W_h \bar{Y}_h = \bar{Y}$$

Taking the unconditional expectation over all possible sample partitions $\mathbf{n}$:
$$E(\bar{y}_{post}) = E_{\mathbf{n}}\left[ E(\bar{y}_{post} \mid \mathbf{n}) \right] = E_{\mathbf{n}}(\bar{Y}) = \bar{Y}$$
Thus, conditional on non-empty strata ($n_h > 0$), the post-stratified estimator is strictly design-unbiased.

#### Derivation of the Exact Unconditional Variance:
Applying the Law of Total Variance:
$$V(\bar{y}_{post}) = V_{\mathbf{n}}\left( E(\bar{y}_{post} \mid \mathbf{n}) \right) + E_{\mathbf{n}}\left( V(\bar{y}_{post} \mid \mathbf{n}) \right)$$

Because $E(\bar{y}_{post} \mid \mathbf{n}) = \bar{Y}$ is a constant independent of $\mathbf{n}$:
$$V_{\mathbf{n}}\left( E(\bar{y}_{post} \mid \mathbf{n}) \right) = V_{\mathbf{n}}(\bar{Y}) = 0$$

Therefore, the entire unconditional variance is governed by the expected conditional variance:
$$V(\bar{y}_{post}) = E_{\mathbf{n}}\left( V(\bar{y}_{post} \mid \mathbf{n}) \right)$$

Conditional on $\mathbf{n}$, sampling within different strata is independent. The conditional variance within stratum $h$ under SRSWOR is:
$$V(\bar{y}_h \mid n_h) = \left( \frac{N_h - n_h}{N_h} \right) \frac{S_h^2}{n_h} = \left( \frac{1}{n_h} - \frac{1}{N_h} \right) S_h^2$$

Summing across all $L$ strata:
$$V(\bar{y}_{post} \mid \mathbf{n}) = \sum_{h=1}^L W_h^2 \left( \frac{1}{n_h} - \frac{1}{N_h} \right) S_h^2 = \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} - \frac{1}{N} \sum_{h=1}^L W_h S_h^2$$

Now take the expectation $E_{\mathbf{n}}$ over the distribution of $n_h$.
We require the expectation of the reciprocal $E(1 / n_h)$.
Using a second-order Taylor expansion around the expected value $E(n_h) = n W_h$:
$$\frac{1}{n_h} \approx \frac{1}{n W_h} - \frac{n_h - n W_h}{(n W_h)^2} + \frac{(n_h - n W_h)^2}{(n W_h)^3}$$
Taking expectations:
$$E\left( \frac{1}{n_h} \right) \approx \frac{1}{n W_h} - 0 + \frac{V(n_h)}{(n W_h)^3} = \frac{1}{n W_h} + \frac{n W_h (1 - W_h)}{(n W_h)^3} = \frac{1}{n W_h} + \frac{1 - W_h}{n^2 W_h^2}$$

Substitute this expectation back into the variance formula:
$$E_{\mathbf{n}}\left( \sum_{h=1}^L \frac{W_h^2 S_h^2}{n_h} \right) \approx \sum_{h=1}^L W_h^2 S_h^2 \left[ \frac{1}{n W_h} + \frac{1 - W_h}{n^2 W_h^2} \right] = \frac{1}{n} \sum_{h=1}^L W_h S_h^2 + \frac{1}{n^2} \sum_{h=1}^L (1 - W_h) S_h^2$$

Subtracting the finite-population term $\frac{1}{N} \sum W_h S_h^2$:
$$V(\bar{y}_{post}) \approx \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h S_h^2 + \frac{1}{n^2} \sum_{h=1}^L (1 - W_h) S_h^2$$

Recall that the variance of the sample mean under **pre-stratified proportional allocation** is:
$$V_{prop}(\bar{y}_{st}) = \left( \frac{1 - f}{n} \right) \sum_{h=1}^L W_h S_h^2$$

Therefore, we arrive at the celebrated **Post-Stratification Variance Theorem**:
$$V(\bar{y}_{post}) \approx V_{prop}(\bar{y}_{st}) + \frac{1}{n^2} \sum_{h=1}^L (1 - W_h) S_h^2$$

#### Profound Methodological Significance:
1. **The Order $O(1/n^2)$ Penalty**: The second term represents the variance penalty induced by the stochastic fluctuation in the realized sample sizes $n_h$. Notice that this penalty decays at rate $O(1/n^2)$, whereas the primary variance decays at rate $O(1/n)$.
2. **Asymptotic Equivalence**: As sample size $n$ grows, the $O(1/n^2)$ term becomes completely negligible. In a sample of $n = 1,000$ households across $L = 5$ post-strata, the penalty accounts for less than $0.2\%$ of the total variance. 
3. **Operational Power**: Post-stratification achieves virtually the **exact same variance reduction as proportional pre-stratification**, without requiring any pre-survey knowledge of stratum membership on the sampling frame!

---

## Controlled Selection: Deep Stratification Without Inflating Sample Size

In large-scale survey planning, investigators often wish to stratify by multiple categorical variables simultaneously:
- Geographic Region ($R = 8$ divisions)
- Urban/Rural Classification ($U = 3$ levels: metropolitan, peri-urban, rural)
- Ecological Agro-climatic Zone ($E = 5$ zones)
- Majority Economic Activity ($A = 4$ sectors)

Crossing all four categorical variables generates a multi-way stratification grid of:
$$L = R \times U \times E \times A = 8 \times 3 \times 5 \times 4 = 480 \text{ strata}$$

If classical stratified sampling is executed with the minimum requirement of $n_h \ge 2$ units per stratum to permit variance estimation, the survey would require a minimum sample of:
$$n_{min} = 2 \times 480 = 960 \text{ Primary Sampling Units}$$
If the total field budget allows visiting only $n = 40$ or $50$ PSUs, classical multi-way stratification collapses completely, as the number of strata ($480$) vastly exceeds the available sample size ($40$).

### The Goodman–Kish Controlled Selection Framework

In 1950, Roe Goodman and Leslie Kish developed **Controlled Selection**, a mathematical optimization methodology that achieves multi-way stratification when the sample size $n$ is smaller than the number of stratification cells.

Let the multi-way population be represented as a two-dimensional grid of $R$ rows and $C$ columns, with known population proportions $P_{rc}$ in cell $(r, c)$ such that $\sum_{r=1}^R \sum_{c=1}^C P_{rc} = 1$.
Given a total sample size of $n$ units, the expected sample size in cell $(r, c)$ under proportional allocation is:
$$e_{rc} = n P_{rc}$$
The marginal expected sample sizes for row $r$ and column $c$ are:
$$e_{r\cdot} = \sum_{c=1}^C e_{rc} = n P_{r\cdot} \quad \text{and} \quad e_{\cdot c} = \sum_{r=1}^R e_{rc} = n P_{\cdot c}$$

Because $e_{rc}$ is typically a fractional number (e.g., $e_{rc} = 0.35$ or $1.42$), an integer sample cannot allocate exactly $e_{rc}$ units to cell $(r, c)$.

#### The Controlled Selection Principle:
Controlled selection defines an integer sample pattern $\mathbf{n}_k = \{n_{rc}^{(k)}\}$ where every cell count $n_{rc}^{(k)}$ is restricted to one of the two integers adjacent to $e_{rc}$:
$$n_{rc}^{(k)} \in \{ \lfloor e_{rc} \rfloor, \; \lfloor e_{rc} \rfloor + 1 \}$$
and the marginal totals satisfy:
$$n_{r\cdot}^{(k)} \in \{ \lfloor e_{r\cdot} \rfloor, \; \lfloor e_{r\cdot} \rfloor + 1 \} \quad \text{and} \quad n_{\cdot c}^{(k)} \in \{ \lfloor e_{\cdot c} \rfloor, \; \lfloor e_{\cdot c} \rfloor + 1 \}$$

Goodman and Kish proved that any matrix of expected counts can be expressed as a convex linear combination of a small number of integer patterns $\mathbf{n}_1, \mathbf{n}_2, \dots, \mathbf{n}_K$ with selection probabilities $p_1, p_2, \dots, p_K$ ($\sum p_k = 1$):
$$\sum_{k=1}^K p_k n_{rc}^{(k)} = e_{rc} = n P_{rc} \quad \text{for all } r \text{ and } c$$

By drawing pattern $k$ with probability $p_k$, every individual cell and every marginal stratum achieves its exact required selection probability, providing deep multi-way stratification control without requiring sample size inflation.

---

## Variance Estimation with One Unit Per Stratum: The Collapsed Strata Method

In many national master samples (such as the Current Population Survey or the National Health Interview Survey), methodologists form very fine strata and allocate exactly **one Primary Sampling Unit per stratum** ($n_h = 1$ for all $h = 1, \dots, L$). Selecting $n_h = 1$ maximizes geographic stratification dispersion across the nation.

However, selecting $n_h = 1$ introduces a profound inferential dilemma: Because there is only one observation in stratum $h$, the sample variance:
$$s_h^2 = \frac{1}{1 - 1} (y_{h1} - \bar{y}_h)^2 = \frac{0}{0}$$
is mathematically undefined! An unbiased estimator of the sampling variance does not exist within the design-based framework when $n_h = 1$.

### The Method of Collapsed Strata

To construct valid, defensible standard errors from a single-unit-per-stratum design, Cochran (1977) and Hansen, Hurwitz, and Madow (1953) developed the **Method of Collapsed Strata**.

Suppose the $L$ strata are partitioned into $G = L / 2$ pairs of adjacent, substantively similar strata (assumed here that $L$ is even).
Let group $g \in \{1, 2, \dots, G\}$ consist of the two paired strata $g1$ and $g2$.
From stratum $g1$, we observe sample total $\hat{Y}_{g1}$; from stratum $g2$, we observe sample total $\hat{Y}_{g2}$.
Let $X_{g1}$ and $X_{g2}$ denote a known auxiliary measure of size (such as census population count) for the two strata.

The **Collapsed Strata Variance Estimator** of the estimated total $\hat{Y} = \sum_{g=1}^G (\hat{Y}_{g1} + \hat{Y}_{g2})$ is:
$$\hat{V}_{col}(\hat{Y}) = \sum_{g=1}^G \left( \hat{Y}_{g1} - \frac{X_{g1}}{X_{g2}} \hat{Y}_{g2} \right)^2 \left( \frac{X_{g1} + X_{g2}}{2 X_{g1}} \right)$$

When the two paired strata are approximately equal in size ($X_{g1} \approx X_{g2}$), this formula simplifies to the classical pairwise squared difference:
$$\hat{V}_{col}(\hat{Y}) = \sum_{g=1}^G (\hat{Y}_{g1} - \hat{Y}_{g2})^2$$

### Expectation and Positive Conservatism

Taking the design expectation of the collapsed variance estimator:
$$E\left[ (\hat{Y}_{g1} - \hat{Y}_{g2})^2 \right] = V(\hat{Y}_{g1}) + V(\hat{Y}_{g2}) + [E(\hat{Y}_{g1}) - E(\hat{Y}_{g2})]^2 = V(\hat{Y}_{g1}) + V(\hat{Y}_{g2}) + (Y_{g1} - Y_{g2})^2$$

Summing across all $G$ groups:
$$E[\hat{V}_{col}(\hat{Y})] = \sum_{g=1}^G [V(\hat{Y}_{g1}) + V(\hat{Y}_{g2})] + \sum_{g=1}^G (Y_{g1} - Y_{g2})^2 = V(\hat{Y}) + \sum_{g=1}^G (Y_{g1} - Y_{g2})^2$$

#### Crucial Theoretical Properties:
1. **Strict Positive Conservatism**: Notice that $\sum_{g=1}^G (Y_{g1} - Y_{g2})^2 \ge 0$ is a sum of squared differences between the true stratum totals. Therefore:
   $$E[\hat{V}_{col}(\hat{Y})] \ge V(\hat{Y})$$
   The collapsed strata variance estimator is **guaranteed to be conservative** (it never underestimates the true variance).
2. **Minimizing Overestimation**: To make the overestimation bias $\sum (Y_{g1} - Y_{g2})^2$ as small as possible, methodologists pair strata that are as nearly identical as possible in terms of population size, geographic proximity, and socioeconomic characteristics ($Y_{g1} \approx Y_{g2}$).
3. **Safety for Public Policy**: In official statistics and regulatory decisions, conservative standard errors are universally preferred over anti-conservative ones: reporting slightly wider confidence intervals protects scientific conclusions against false-positive claims.

---

## Practical Synthesis, Quality Diagnostics and Computational Verification

The practical execution of Stratified Random Sampling requires careful safeguards against common real-world failure modes.

### 1. Small Sample Allocations and Sample Size Constraints
When computing Neyman or cost-optimal allocations, the mathematical formula may yield a non-integer sample size or a value $n_h < 2$ for very small strata.
- **Minimum Stratum Size Rule**: Every stratum must have at least $n_h \ge 2$ sampled units to permit design-based variance estimation. If $n_h = 1$, the within-stratum sample variance $s_h^2$ has zero degrees of freedom, rendering unbiased variance estimation impossible.
- **Upper Bound Truncation (Over-Allocation)**: If $n_h \ge N_h$, the entire stratum must be converted into a certainty (take-all) stratum ($n_h = N_h$). The remaining sample size $n - N_h$ is then reallocated across the remaining take-some strata.

### 2. Post-Stratification
When stratum membership cannot be identified on the sampling frame prior to selection (e.g., educational attainment is not listed on a national population registry), units cannot be sampled independently by stratum. However, if the population stratum weights $W_h = N_h / N$ are known from a recent census, the researcher can draw an unstratified simple random sample and classify the sampled units into strata post hoc.

The **post-stratified estimator** of the population mean is:
$$\bar{y}_{post} = \sum_{h=1}^L W_h \bar{y}_h$$
where $\bar{y}_h$ is the mean of the $n_h$ units that randomly fell into stratum $h$. When $n$ is sufficiently large such that $P(n_h = 0) \approx 0$, the post-stratified estimator is conditionally design-unbiased, and its unconditional variance satisfies:
$$V(\bar{y}_{post}) \approx V_{prop}(\bar{y}_{st}) + \frac{1}{n^2} \sum_{h=1}^L (1 - W_h) S_h^2$$
For large $n$, the penalty term is of order $O(1/n^2)$, meaning that post-stratification achieves nearly the exact same precision as true proportional stratified sampling!

In Unit 4, we examine environments where units are geographically dispersed and independent element listing is prohibitively expensive, requiring the theory of **Cluster Sampling and Multistage Sampling**.
