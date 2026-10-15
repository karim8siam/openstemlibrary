# tooling/add-depth-final.py

# 1. Expand Unit 3
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-3.md", "r", encoding="utf-8") as f:
    u3 = f.read()

u3_addition = r"""

---

## 3.7 Seriation, Matrix Permutation Graphics, and Cleveland's Trellis Banking Theory

Beyond Cartesian plots and scatter displays, exploratory multivariate data analysis requires structured tabular and matrix visualizations capable of revealing latent cluster blocks, permutation hierarchies, and perceptual slope calibrations.

### Jacques Bertin's Matrix Seriation and Permutation Graphics

In *Sémiologie Graphique* (1967), Jacques Bertin demonstrated that tabular data matrices can be transformed into powerful visual exploratory engines through **Seriation (Matrix Permutation)**.

Given an empirical matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ of $n$ observations and $p$ categorical or continuous variables, raw rows and columns typically appear in arbitrary data-collection order. Bertin recognized that by simultaneously permuting the row ordering $\pi_{row}$ and column ordering $\pi_{col}$:

$$\tilde{\mathbf{X}} = \mathbf{P}_{row} \mathbf{X} \mathbf{P}_{col}^\top$$

the matrix can be reordered such that similar rows and similar columns are positioned adjacent to one another.

#### Seriation Algorithms:
1. **Hierarchical Clustering Reordering (Optimal Leaf Ordering)**:
   Rows and columns are independently clustered via agglomerative hierarchical clustering with distance metric $d(x_i, x_j) = 1 - r_{ij}$. Bar-Joseph and colleagues (2001) formulated the **Optimal Leaf Ordering (OLO)** algorithm, which traverses the dendrogram tree, rotating internal nodes in $\mathcal{O}(n^3)$ time to minimize the sum of distances between adjacent tree leaves:
   $$\min_{\pi} \sum_{i=1}^{n-1} d(x_{\pi(i)}, x_{\pi(i+1)})$$
2. **Spectral Seriation**:
   Constructs the unnormalized graph Laplacian $\mathbf{L} = \mathbf{D} - \mathbf{W}$ of the row affinity graph. By the properties of spectral graph theory, the second smallest eigenvector (the **Fiedler Vector**) provides the continuous 1D ordering that minimizes squared distance penalties between connected entities. Sorting rows by the elements of the Fiedler vector groups correlated observations into contiguous visual blocks along the diagonal.

Seriation heatmaps reveal block-diagonal correlation clusters, banded anti-diagonal gradients (simplex structures), and isolated anomaly rows that are completely imperceptible in unpermuted tables.

### Cleveland's Trellis Displays and Banking to 45 Degrees

In 1988, William S. Cleveland, Marylyn McGill, and Robert McGill published their foundational psychophysical research on **Banking to 45 Degrees**.

When human viewers examine a 2D line plot depicting a continuous functional relationship $y = f(x)$, the primary perceptual task is decoding the **rate of change (derivative / slope)** of the curve.

#### The Psychophysics of Orientation Discrimination:
Cleveland and colleagues conducted controlled visual experiments demonstrating that human visual discrimination between orientations is **maximally sensitive when line segment angles are near $45^\circ$ or $-45^\circ$**, and degrades severely when angles approach horizontal ($0^\circ$) or vertical ($90^\circ$).

#### The Aspect Ratio Banking Equation:
The **aspect ratio** of a plot is defined as the physical display height divided by the physical display width:
$$\alpha = \frac{\text{Height}}{\text{Width}}$$
Let $\Delta x_k = x_{k+1} - x_k$ and $\Delta y_k = y_{k+1} - y_k$ denote the coordinates of the line segments in data units.
The physical visual angle $\theta_k$ of segment $k$ on the display canvas is:
$$\theta_k(\alpha) = \arctan\left( \alpha \frac{\Delta y_k}{\Delta x_k} \right)$$

Cleveland formulated the **Average Absolute Aspect Banking Rule**: choose the aspect ratio $\alpha$ such that the average absolute orientation of the line segments equals $45^\circ$ (or $\pi / 4$ radians):

$$\frac{1}{\sum_{k=1}^{n-1} \|\Delta \mathbf{x}_k\|_2} \sum_{k=1}^{n-1} \|\Delta \mathbf{x}_k\|_2 |\theta_k(\alpha)| = 45^\circ$$

By banking to $45^\circ$, subtle oscillations, sudden inflection points, and cyclic seasonal patterns in economic and physical time series (such as sunspot cycles or quarterly GDP growth rates) become instantly visible to the human eye. Modern ggplot2 and lattice engines implement automatic aspect ratio banking via `coord_fixed(ratio = ...)` and specialized banking algorithms.
"""

marker = "## Fully worked question 1:"
idx = u3.find(marker)
u3_new = u3[:idx] + u3_addition.strip() + "\n\n" + u3[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-3.md", "w", encoding="utf-8") as f:
    f.write(u3_new)
print("Expanded Unit 3!")

# 2. Expand Unit 4
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "r", encoding="utf-8") as f:
    u4 = f.read()

u4_addition = r"""

---

## 4.9 Pivoting Strategies, Generalized Eigenproblems, and Ridge Condition Analysis

In advanced computational statistics and econometrics, matrix factorizations encounter structural rank-deficiencies and collinearity that require pivoting strategies, generalized eigenvalue solutions, and $L_2$ regularization.

### Pivoting Strategies in Matrix Decompositions

In numerical Gaussian elimination and LU factorization of matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$, the algorithm divides by diagonal pivot elements $A_{kk}$. If a diagonal entry is zero or extraordinarily small ($|A_{kk}| \ll \epsilon_{mach}$), direct division triggers division-by-zero or massive roundoff amplification.

#### 1. Partial (Row) Pivoting:
At step $k$, scan the current column $k$ from row $k$ to row $n$. Find the row $i^* \ge k$ that maximizes the absolute value:
$$i^* = \arg\max_{i \ge k} |A_{ik}|$$
Swap row $k$ with row $i^*$. This is encoded via permutation matrix $\mathbf{P}$:
$$\mathbf{P} \mathbf{A} = \mathbf{L} \mathbf{U}$$
Row pivoting guarantees that all multipliers in $\mathbf{L}$ satisfy $|L_{ij}| \le 1.0$, bounding error growth by $2^{n-1}$ (which in practice is essentially $\mathcal{O}(n)$).

#### 2. Complete Pivoting:
Scans the entire remaining sub-matrix $(n - k + 1) \times (n - k + 1)$ for the maximal element:
$$(i^*, j^*) = \arg\max_{i \ge k, j \ge k} |A_{ij}|$$
Swaps both rows and columns:
$$\mathbf{P} \mathbf{A} \mathbf{Q} = \mathbf{L} \mathbf{U}$$
Complete pivoting provides absolute numerical stability, but searching the 2D submatrix requires $\mathcal{O}(n^3)$ comparison overhead.

#### 3. Rank-Revealing QR (RRQR) with Column Pivoting:
In statistical regression when design matrix $\mathbf{X}$ is collinear, standard QR fails to identify which columns are redundant. Gene Golub (1965) formulated **QR with Column Pivoting (RRQR)**:
$$\mathbf{X} \mathbf{P} = \mathbf{Q} \mathbf{R} = \mathbf{Q} \begin{bmatrix} \mathbf{R}_{11} & \mathbf{R}_{12} \\ \mathbf{0} & \mathbf{R}_{22} \end{bmatrix}$$
where permutation matrix $\mathbf{P}$ reorders columns so that diagonal elements $|R_{kk}|$ are strictly non-increasing. If $\mathbf{X}$ has numerical rank $r < p$, the sub-block $\|\mathbf{R}_{22}\|_2 \le \epsilon$, allowing the statistical software to detect and drop collinear columns automatically (the engine of R's `lm()`).

### Generalized Eigenvalue Problems in Discriminant and Canonical Analysis

In multivariate statistics, many classic techniques—including Fisher's **Linear Discriminant Analysis (LDA)** and Hotelling's **Canonical Correlation Analysis (CCA)**—do not solve standard eigenvalue problems $\mathbf{A} \mathbf{v} = \lambda \mathbf{v}$. Instead, they solve the **Generalized Eigenvalue Problem**:

$$\mathbf{A} \mathbf{v} = \lambda \mathbf{B} \mathbf{v}$$

where $\mathbf{A}$ is symmetric (e.g. between-group covariance $\mathbf{S}_B$) and $\mathbf{B}$ is symmetric positive-definite (e.g. within-group covariance $\mathbf{S}_W$).

#### Numerical Solution via Cholesky Factorization:
A naive approach inverts $\mathbf{B}$ and solves the standard problem for $\mathbf{B}^{-1} \mathbf{A}$. However, the product $\mathbf{B}^{-1} \mathbf{A}$ is generally **asymmetric**, destroying symmetry and requiring complex arithmetic.
The numerically stable algorithm:
1. Compute the Cholesky factorization of $\mathbf{B}$:
   $$\mathbf{B} = \mathbf{L} \mathbf{L}^\top$$
2. Substitute into the generalized system:
   $$\mathbf{A} \mathbf{v} = \lambda \mathbf{L} \mathbf{L}^\top \mathbf{v}$$
3. Multiply on the left by $\mathbf{L}^{-1}$ and insert $\mathbf{I} = (\mathbf{L}^\top)^{-1} \mathbf{L}^\top$:
   $$\mathbf{L}^{-1} \mathbf{A} (\mathbf{L}^\top)^{-1} (\mathbf{L}^\top \mathbf{v}) = \lambda (\mathbf{L}^\top \mathbf{v})$$
4. Define transformed symmetric matrix $\mathbf{C} = \mathbf{L}^{-1} \mathbf{A} (\mathbf{L}^{-1})^\top$ and transformed vector $\mathbf{w} = \mathbf{L}^\top \mathbf{v}$.
5. Solve the standard symmetric eigenvalue problem $\mathbf{C} \mathbf{w} = \lambda \mathbf{w}$.
6. Retrieve the true generalized eigenvectors by back-solving the triangular system:
   $$\mathbf{L}^\top \mathbf{v} = \mathbf{w}$$
This preserves symmetry, guarantees real orthogonal eigenvectors, and operates near machine precision.

### Condition Number Conditioning via Ridge Regularization

When design matrix $\mathbf{X}$ exhibits severe multicollinearity, the cross-product matrix $\mathbf{X}^\top \mathbf{X}$ has tiny eigenvalues $\lambda_{min} \approx 0$, driving the condition number $\kappa(\mathbf{X}^\top \mathbf{X}) \to \infty$.

Arthur Hoerl and Robert Kennard (1970) formulated **Ridge Regression ($L_2$ Regularization)**:

$$\hat{\boldsymbol{\beta}}_{ridge} = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p)^{-1} \mathbf{X}^\top \mathbf{y}, \quad \lambda > 0$$

#### Spectral Condition Number Regularization:
Let the eigenvalues of $\mathbf{X}^\top \mathbf{X}$ be $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p \ge 0$.
The eigenvalues of the regularized matrix $\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p$ are shifted:
$$\lambda_j(\text{Ridge}) = \lambda_j + \lambda$$

The condition number of the regularized linear system is:

$$\kappa(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p) = \frac{\lambda_1 + \lambda}{\lambda_p + \lambda}$$

As $\lambda$ increases from 0:
- If $\lambda_p = 10^{-6}$ and $\lambda_1 = 10^2$, the original condition number is $\kappa = 10^8$.
- Adding a modest ridge penalty $\lambda = 1.0$:
  $$\kappa_{ridge} = \frac{100 + 1}{10^{-6} + 1} \approx 101$$
The condition number collapses from **one hundred million down to 101**! This massive reduction in condition number stabilizes matrix inversion, drastically suppresses coefficient sampling variance, and prevents floating-point catastrophic errors.
"""

marker = "## Fully worked question 1:"
idx = u4.find(marker)
u4_new = u4[:idx] + u4_addition.strip() + "\n\n" + u4[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "w", encoding="utf-8") as f:
    f.write(u4_new)
print("Expanded Unit 4!")

# 3. Expand Unit 5
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "r", encoding="utf-8") as f:
    u5 = f.read()

u5_addition = r"""

---

## 5.9 Simulation of Continuous-Time Stochastic Processes and Particle Filtering

In quantitative finance, ecological epidemiology, and physical modeling, statistical computing requires generating full trajectories of continuous-time stochastic processes and filtering hidden dynamic states.

### Exact Simulation of Brownian Motion and Diffusion Paths

The foundational building block of continuous-time stochastic calculus is the standard **Brownian Motion (Wiener Process)** $W(t)$ on $t \in [0, T]$, characterized by three axiomatic properties:
1. $W(0) = 0$.
2. Independent increments: For any $0 \le t_1 < t_2 \le t_3 < t_4$, the increment $W(t_4) - W(t_3)$ is independent of $W(t_2) - W(t_1)$.
3. Gaussian increments: For any $s < t$:
   $$W(t) - W(s) \sim \mathcal{N}(0, \, t - s)$$

#### Algorithmic Path Generation:
To simulate a discrete sample path across $M$ uniform time intervals $\Delta t = T / M$:
1. Generate an i.i.d. vector of standard normal variates $Z_1, \dots, Z_M \sim \mathcal{N}(0, 1)$.
2. Compute the discrete increments: $\Delta W_m = \sqrt{\Delta t} \, Z_m$.
3. Compute the trajectory via cumulative summation:
   $$W(t_m) = \sum_{j=1}^m \Delta W_j = \text{cumsum}(\Delta \mathbf{W})$$

#### The Brownian Bridge:
A **Brownian Bridge** $B(t)$ is a standard Brownian motion conditioned to return to zero at terminal time $T$: $B(0) = 0$ and $B(T) = 0$.
Given an unconstrained Brownian path $W(t)$, the Brownian bridge is constructed directly via the linear projection:

$$B(t) = W(t) - \frac{t}{T} W(T), \quad t \in [0, T]$$

Brownian bridges are central to empirical process theory and evaluating the exact distribution of the Kolmogorov–Smirnov test statistic.

### The Lewis–Shedler Thinning Algorithm for Inhomogeneous Poisson Processes

A homogeneous Poisson process has a constant arrival rate $\lambda$. In real-world systems (such as emergency room arrivals or financial trade transactions), the arrival rate varies continuously over time: $\lambda(t) \ge 0$.

In 1979, P. A. W. Lewis and Gerald Shedler developed the **Thinning Algorithm**, applying acceptance-rejection principles to point processes.

#### Thinning Protocol:
1. Determine an upper bound constant $\lambda^* < \infty$ that majorizes the rate function:
   $$\lambda(t) \le \lambda^* \quad \text{for all } t \in [0, T]$$
2. Simulate potential arrival times from a fast homogeneous Poisson process with constant rate $\lambda^*$:
   - Draw inter-arrival times $\Delta t_k \sim \text{Exponential}(\lambda^*)$ via inversion: $\Delta t_k = -\frac{1}{\lambda^*} \ln U_k$.
   - Potential arrival times: $t_k = t_{k-1} + \Delta t_k$.
3. For each candidate arrival time $t_k \le T$:
   - Draw $U \sim \text{Uniform}(0, 1)$.
   - Evaluate the acceptance test:
     $$\text{If } U \le \frac{\lambda(t_k)}{\lambda^*}, \quad \text{ACCEPT and record } t_k \text{ as an event.}$$
     $$\text{Otherwise, REJECT and discard } t_k.$$

The accepted event times follow the exact **Inhomogeneous Poisson Process with intensity $\lambda(t)$** without requiring numerical integration of $\Lambda(t) = \int_0^t \lambda(s) ds$.

### Sequential Monte Carlo (SMC) and Particle Filtering

For non-linear, non-Gaussian state-space hidden Markov models:
- State equation: $\mathbf{x}_t \sim p(\mathbf{x}_t \mid \mathbf{x}_{t-1})$
- Observation equation: $\mathbf{y}_t \sim p(\mathbf{y}_t \mid \mathbf{x}_t)$

Classical Kalman filters fail. **Particle Filters (Sequential Importance Resampling, SIR)** represent the continuous filtering distribution $p(\mathbf{x}_t \mid \mathbf{y}_{1:t})$ using a cloud of $P$ weighted particles $\{ \mathbf{x}_t^{(p)}, w_t^{(p)} \}_{p=1}^P$:

1. **Propagation**: Sample new states from transition density:
   $$\tilde{\mathbf{x}}_t^{(p)} \sim p(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(p)})$$
2. **Weighting**: Update importance weights using observation likelihood:
   $$w_t^{(p)} \propto w_{t-1}^{(p)} \cdot p(\mathbf{y}_t \mid \tilde{\mathbf{x}}_t^{(p)})$$
3. **Resampling**: When effective sample size $\text{ESS} = 1 / \sum (\tilde{w}_t^{(p)})^2 < P / 2$, resample $P$ particles with replacement proportional to weights $w_t^{(p)}$, eliminating low-probability trajectories and cloning promising paths.
"""

marker = "## Fully worked question 1:"
idx = u5.find(marker)
u5_new = u5[:idx] + u5_addition.strip() + "\n\n" + u5[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "w", encoding="utf-8") as f:
    f.write(u5_new)
print("Expanded Unit 5!")

# 4. Expand Unit 6
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "r", encoding="utf-8") as f:
    u6 = f.read()

u6_addition = r"""

---

## 6.8 The Double Bootstrap, Prepivoting, and Non-Parametric Tolerance Intervals

While standard bootstrap confidence intervals achieve first-order accuracy ($\mathcal{O}(n^{-1/2})$ coverage error) or second-order accuracy ($\mathcal{O}(n^{-1})$ for BCa), high-stakes applications (such as aerospace component certification and clinical bioequivalence) require higher-order asymptotic corrections and distribution-free tolerance bounds.

### The Double Bootstrap (Iterated Bootstrap) and Prepivoting

In 1987, Rudolf Beran introduced the theory of **Prepivoting**, realized computationally via the **Double (Iterated) Bootstrap**.

#### The Coverage Calibration Problem:
Suppose we construct a nominal $90\%$ bootstrap confidence interval for parameter $\theta$. Due to finite-sample skewness, the true realized coverage probability of the interval may be only $86\%$:
$$\mathbb{P}(\theta \in \text{CI}_{0.90}) = 0.86 \ne 0.90$$
The nominal level $\alpha = 0.10$ suffers from a coverage error of $0.04$.

The Double Bootstrap uses a **nested bootstrap loop** to estimate and eliminate this coverage error:

```text
The Double Bootstrap Nested Hierarchy:
  Sample X (Size n)
     |
     v Outer Bootstrap Loop (B1 = 1,000 resamples X*)
  Bootstrap Sample X*
     |
     v Inner Bootstrap Loop (B2 = 250 resamples X**)
  Double Bootstrap Sample X**
```

#### The Double Bootstrap Execution Protocol:
1. For each outer bootstrap resample $\mathbf{x}^{*b}$ ($b = 1, \dots, B_1$):
   - Compute outer estimate $\hat{\theta}^{*b}$.
   - For each inner resample $k = 1, \dots, B_2$:
     - Draw $\mathbf{x}^{**k}$ by resampling with replacement from $\mathbf{x}^{*b}$.
     - Compute inner estimate $\hat{\theta}^{**k}$.
   - Compute the inner empirical coverage rate $\hat{C}_b(\alpha)$.
2. Adjust the nominal quantile level $\alpha^* = \arg\min_\alpha |\bar{C}(\alpha) - (1 - \alpha_{nominal})|$.
3. Construct the final interval using the calibrated percentile $\alpha^*$.

Beran proved that each iteration of the bootstrap **removes one additional order of asymptotic error**:
- Standard percentile interval: Coverage error $\mathcal{O}(n^{-1/2})$.
- Double bootstrap interval: Coverage error **$\mathcal{O}(n^{-2})$**!
For $n = 100$, an error of $\mathcal{O}(n^{-2}) \approx 10^{-4}$ achieves near-perfect nominal coverage, completely eliminating coverage bias at the cost of $B_1 \times B_2$ computational operations.

### Non-Parametric Tolerance Intervals via Order Statistics

A standard confidence interval provides bounds for an unknown scalar population parameter $\theta$ (such as the mean $\mu$). In industrial reliability and regulatory compliance, engineers require **Tolerance Intervals**: bounds that cover at least a specified proportion $\beta \in (0, 1)$ of the entire population with a specified high confidence level $1 - \alpha$.

Wilks (1941) proved that exact, distribution-free tolerance intervals can be constructed directly from sample **order statistics** $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$.

#### Wilks' Exact Distribution-Free Equation:
Let the interval be $[X_{(r)}, X_{(s)}]$ where $1 \le r < s \le n$.
The proportion of the population covered by the interval is the random variable:
$$C = F(X_{(s)}) - F(X_{(r)})$$

By standard order statistic probability theory, the coverage $C$ follows a **Beta Distribution**:

$$C \sim \text{Beta}(s - r, \, n - (s - r) + 1)$$

We require that $\mathbb{P}(C \ge \beta) \ge 1 - \alpha$:

$$\sum_{k=s-r}^n \binom{n}{k} \beta^k (1 - \beta)^{n - k} \ge 1 - \alpha$$

For the extreme two-sided tolerance interval spanning the sample minimum and maximum $[X_{(1)}, X_{(n)}]$ ($r = 1, s = n$, so $s - r = n - 1$):

$$\mathbb{P}(C \ge \beta) = 1 - n \beta^{n - 1} + (n - 1) \beta^n \ge 1 - \alpha$$

#### Sample Size Determination:
To guarantee with $95\%$ confidence ($1 - \alpha = 0.95$) that the interval $[X_{(1)}, X_{(n)}]$ encompasses at least $90\%$ of the population ($\beta = 0.90$):
$$1 - n (0.90)^{n-1} + (n - 1)(0.90)^n \ge 0.95$$
Solving numerically yields the minimum required sample size:
$$n = 46 \text{ observations}$$
This extraordinary mathematical result holds for **any continuous distribution**, providing rigorous statistical guarantees without parametric assumptions.
"""

marker = "## Fully worked question 1:"
idx = u6.find(marker)
u6_new = u6[:idx] + u6_addition.strip() + "\n\n" + u6[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "w", encoding="utf-8") as f:
    f.write(u6_new)
print("Expanded Unit 6!")

# 5. Expand Unit 8
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "r", encoding="utf-8") as f:
    u8 = f.read()

u8_addition_extra = r"""

---

## 8.8 High-Performance Tabular Storage: Apache Parquet, Snappy, and Predicate Pushdown

In modern large-scale statistical pipelines, analytical data frames are rarely stored as uncompressed plain-text CSV files. Plain text files are bloated, lack data type metadata, and force computing engines to parse every single byte sequentially from disk into memory.

To optimize persistent storage and I/O throughput, the open-source community established **Apache Parquet**, a standardized columnar on-disk storage format.

### The Physical Architecture of Apache Parquet

Unlike row-based storage models (CSV, SQLite) that store data tuple-by-tuple:
$$\text{Row 1: } [id_1, age_1, income_1] \quad \text{Row 2: } [id_2, age_2, income_2]$$
Apache Parquet groups records into **Row Groups** (typically 100,000 to 1,000,000 rows each) and stores data strictly **column-by-column within each row group**:

```text
Apache Parquet File Structure:
+-----------------------------------------------------------+
| File Header                                               |
+-----------------------------------------------------------+
| Row Group 1:                                              |
|   Column 1 (id):     [ Compressed Data Chunk + Stats ]    |
|   Column 2 (age):    [ Compressed Data Chunk + Stats ]    |
|   Column 3 (income): [ Compressed Data Chunk + Stats ]    |
+-----------------------------------------------------------+
| Row Group 2:                                              |
|   Column 1 (id):     [ Compressed Data Chunk + Stats ]    |
|   Column 2 (age):    [ Compressed Data Chunk + Stats ]    |
|   Column 3 (income): [ Compressed Data Chunk + Stats ]    |
+-----------------------------------------------------------+
| File Footer (Metadata: Schema, Row Counts, Block Offsets) |
+-----------------------------------------------------------+
```

### Compression and Encoding Techniques
Because a single column holds homogeneous values of the identical data type, Parquet achieves extraordinary compression ratios:
1. **Dictionary Encoding**: Replaces repetitive categorical strings with small 1-byte integer keys.
2. **Run-Length Encoding (RLE) and Bit-Packing**: Replaces repeated sequences of identical integers (e.g. `[1, 1, 1, 1, 1]`) with count pairs (`(5, 1)`), storing values using the minimum necessary bit-width.
3. **Block-Level Compression Algorithms**:
   - **Snappy**: Engineered by Google for high-speed decompression (over $500 \text{ MB/sec}$ per CPU core) with modest compression ratios.
   - **ZSTD (Zstandard)**: Developed by Yann Collet at Facebook, delivering state-of-the-art compression ratios with rapid decompression speed.

### Two Transformative Query Optimizations:
1. **Column Projection (Column Pruning)**:
   If a statistical regression requires only 3 variables out of a 100-column table, Parquet reads **only the byte chunks for those 3 columns**, completely skipping the remaining 97 columns on disk! Disk I/O drops by $97\%$.
2. **Predicate Pushdown (Min/Max Statistics Pruning)**:
   Parquet embeds metadata summary statistics (`min_value`, `max_value`, `null_count`) into the footer of every row group.
   When an analytical query evaluates:
   ```python
   df = pd.read_parquet("census.parquet", filters=[("age", ">", 65)])
   ```
   The query engine reads the footer metadata before touching the data. If a row group has `max_value = 62`, the engine knows that zero records in that row group satisfy the filter. The entire 50 MB row group is **skipped without reading a single byte from disk**!

By combining column pruning and predicate pushdown, reading datasets from Apache Parquet into pandas or R `arrow::read_parquet()` executes between **$10\times$ and $100\times$ faster** than reading raw CSV files, representing the foundational storage pillar of modern computational statistics.
"""

marker = "## Fully worked question 1:"
idx = u8.find(marker)
u8_new = u8[:idx] + u8_addition_extra.strip() + "\n\n" + u8[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "w", encoding="utf-8") as f:
    f.write(u8_new)
print("Expanded Unit 8 extra!")
