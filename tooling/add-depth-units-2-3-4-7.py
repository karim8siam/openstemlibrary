#!/usr/bin/env python3
"""
Adds substantive prose depth to Units 2, 3, 4, and 7 to cross 50,000 words in COURSE_DATA.
"""
from pathlib import Path

BASE = Path("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r")

def expand_unit_2():
    path = BASE / "unit-2.md"
    content = path.read_text(encoding="utf-8")
    addition = r"""

## 2.12 Streaming Tabular Wrangling, Chunked Iteration, and Out-of-Core Processing: Polars LazyFrames and Apache Arrow

In modern statistical analytics, empirical datasets frequently exceed available physical random access memory (RAM). When an applied researcher attempts to load an $80\text{ GB}$ administrative health record or longitudinal financial transaction log into a standard in-memory pandas or base R session on a machine equipped with $32\text{ GB}$ of RAM, the operating system triggers aggressive virtual memory swap thrashing, culminating in an inevitable `MemoryError` or Out-of-Memory (OOM) kernel termination. To process massive datasets without requiring expensive distributed supercomputing clusters, computational statisticians rely on out-of-core streaming pipelines and declarative lazy execution frameworks.

### The Chunked Iteration Paradigm

The simplest architectural strategy for handling out-of-core data is chunked sequential streaming. Instead of materializing the entire tabular dataset in memory simultaneously, the computational engine reads a fixed batch of rows (for example, $b = 100,000$ records per chunk), applies transformations, updates running statistical accumulators, and immediately releases the chunk buffer back to the memory allocator:

```python
import pandas as pd
import numpy as np

# Sequential chunked processing of massive CSV files
chunk_size = 100_000
running_count = 0
running_sum = 0.0
running_sum_sq = 0.0

for chunk in pd.read_csv("massive_sensor_log.csv", chunksize=chunk_size, usecols=["temperature"]):
    clean_vals = chunk["temperature"].dropna().to_numpy(dtype=np.float64)
    running_count += clean_vals.size
    running_sum += np.sum(clean_vals)
    running_sum_sq += np.sum(clean_vals ** 2)

sample_mean = running_sum / running_count
sample_var = (running_sum_sq - (running_sum ** 2) / running_count) / (running_count - 1)
```

While chunked sequential streaming successfully prevents memory exhaustion, it imposes significant algorithmic constraints:
1. **Accumulator Limitations**: Only "embarrassingly decomposable" statistics—such as counts, sums, extrema, and certain linear moments—can be updated incrementally across disjoint batches. Non-local operations, such as global medians, quantiles, and sorting, cannot be evaluated without multi-pass external merge sorts.
2. **Interpreter Overhead**: In Python, executing an explicit `for` loop over thousands of chunks incurs repeated bytecode dispatch and object boxing penalties.

### Lazy Evaluation and Expression Pushdown in Polars

The modern frontier of high-performance out-of-core data wrangling is embodied by **Polars**, an open-source query engine implemented in Rust and built upon the Apache Arrow columnar memory model. Unlike pandas and R data.table, which evaluate data manipulation operations eagerly (immediately computing and materializing every intermediate dataframe), Polars supports a **LazyFrame** execution mode:

```python
import polars as pl

# Construct declarative query plan without loading data into memory
q = (
    pl.scan_parquet("records_*.parquet")
    .filter(pl.col("patient_age") >= 65)
    .with_columns(
        (pl.col("systolic_bp") / pl.col("diastolic_bp")).alias("bp_ratio")
    )
    .group_by("diagnosis_category")
    .agg([
        pl.len().alias("patient_count"),
        pl.col("bp_ratio").mean().alias("mean_bp_ratio"),
        pl.col("bp_ratio").std().alias("std_bp_ratio")
    ])
)

# Execute streaming query plan across disk partitions
result = q.collect(streaming=True)
```

When an analyst invokes operations on a `LazyFrame`, Polars does not execute computations. Instead, it constructs a **Logical Query Plan**—a directed graph of mathematical expressions and relational transformations. Prior to physical execution, the query optimizer analyzes the logical graph and executes several high-level compiler optimizations:
- **Predicate Pushdown**: If a filter operation ($\sigma_{\text{age} \ge 65}$) appears downstream, the optimizer moves the filter to the earliest possible stage—directly into the Parquet reader. Rows failing the predicate are never loaded into RAM.
- **Projection Pushdown**: If only three columns (`patient_age`, `systolic_bp`, `diagnosis_category`) are referenced out of $150$ columns present in the Parquet schema, the reader skips reading the remaining $147$ column byte streams completely.
- **Common Subexpression Elimination**: Identical mathematical expressions computed across multiple aggregated columns are evaluated exactly once, caching intermediate SIMD registers.

When `collect(streaming=True)` is called, the Polars streaming engine splits the workload into vector batches (typically $65,536$ records) and executes them across all available CPU threads in parallel via work-stealing thread pools, achieving memory consumption that remains strictly flat regardless of whether the dataset contains $100,000$ or $1,000,000,000$ rows.
"""
    parts = content.split("## Fully worked question 1:")
    path.write_text(parts[0] + addition + "\n## Fully worked question 1:" + parts[1], encoding="utf-8")
    print("Unit 2 expanded successfully!")

def expand_unit_3():
    path = BASE / "unit-3.md"
    content = path.read_text(encoding="utf-8")
    addition = r"""

## 3.12 High-Dimensional Exploratory Visualizations: t-SNE, UMAP, and Parallel Coordinate Geometry

While univariate histograms, kernel densities, and bivariate scatter plots suffice for examining low-dimensional relationships, modern empirical research routinely involves high-dimensional feature spaces $\mathbf{X} \in \mathbb{R}^{n \times p}$ with dozens or hundreds of continuous covariates ($p \gg 3$). Projecting high-dimensional data onto two-dimensional visual displays without losing critical clustering structure, geometric manifolds, and multivariate correlations is a fundamental challenge in exploratory data analysis.

### The Limitations of Linear Projections: Principal Component Analysis (PCA)

Classical linear dimensionality reduction via Principal Component Analysis seeks an orthogonal projection matrix $\mathbf{W} \in \mathbb{R}^{p \times 2}$ that maximizes projected variance:

$$\max_{\mathbf{W}^T \mathbf{W} = \mathbf{I}_2} \text{Tr}(\mathbf{W}^T \boldsymbol{\Sigma} \mathbf{W})$$

While PCA guarantees optimal preservation of global Euclidean distances in a least-squares sense, it fails catastrophically when the underlying data reside on nonlinear curved manifolds—such as concentric spheres, Swiss rolls, or complex biological differentiation trajectories. Under linear PCA projections, points that are vastly distant along the geodesic manifold surface are artificially collapsed onto identical regions in the 2D display, concealing natural cluster boundaries.

### t-Distributed Stochastic Neighbor Embedding (t-SNE)

To visualize nonlinear cluster structures, Laurens van der Maaten and Geoffrey Hinton (2008) introduced **t-SNE**. Rather than preserving global Euclidean distances, t-SNE converts high-dimensional Euclidean distances into conditional probabilities that represent pairwise neighborhood similarities:

$$p_{j|i} = \frac{\exp(-\|\mathbf{x}_i - \mathbf{x}_j\|^2 / 2\sigma_i^2)}{\sum_{k \ne i} \exp(-\|\mathbf{x}_i - \mathbf{x}_k\|^2 / 2\sigma_i^2)}, \quad p_{ij} = \frac{p_{j|i} + p_{i|j}}{2n}$$

where the bandwidth variance $\sigma_i^2$ is determined adaptively to match a user-specified **perplexity** parameter $\text{Perp}(P_i) = 2^{H(P_i)}$, representing the effective number of local neighbors.

In the low-dimensional embedding space $\mathbf{y}_i \in \mathbb{R}^2$, pairwise similarities are defined using a heavy-tailed Student-t distribution with one degree of freedom (the standard Cauchy distribution):

$$q_{ij} = \frac{(1 + \|\mathbf{y}_i - \mathbf{y}_j\|^2)^{-1}}{\sum_{k} \sum_{l \ne k} (1 + \|\mathbf{y}_k - \mathbf{y}_l\|^2)^{-1}}$$

The optimization objective minimizes the Kullback–Leibler divergence between high-dimensional distribution $P$ and low-dimensional distribution $Q$:

$$\mathcal{L}_{t\text{-SNE}} = \text{KL}(P \| Q) = \sum_{i \ne j} p_{ij} \ln\left( \frac{p_{ij}}{q_{ij}} \right)$$

The heavy-tailed Cauchy density solves the infamous **crowding problem**: because the volume of a sphere in $\mathbb{R}^p$ scales exponentially with $p$, points that are moderately distant in high-dimensional space would be forced to crowd together in 2D Euclidean space under a Gaussian mapping. The heavy tails of the Student-t distribution allow moderately distant points to be positioned far apart in the 2D plane without inflating the Kullback–Leibler penalty.

### Uniform Manifold Approximation and Projection (UMAP)

While t-SNE excels at separating discrete clusters, it suffers from two major limitations: it does not preserve global topology (the relative distances between distant clusters are largely arbitrary), and its $O(n^2)$ computational complexity scales poorly to massive datasets ($n > 100,000$).

**UMAP** (McInnes, Healy, & Melville, 2018) resolves these challenges through Riemannian geometry and algebraic topology:
1. It models the data as a fuzzy simplicial complex on a local Riemannian manifold where Riemannian metric distances are locally scaled.
2. It constructs a low-dimensional fuzzy simplicial set and minimizes the fuzzy set cross-entropy:
   $$C(P, Q) = \sum_{i \ne j} \left[ p_{ij} \ln\left( \frac{p_{ij}}{q_{ij}} \right) + (1 - p_{ij}) \ln\left( \frac{1 - p_{ij}}{1 - q_{ij}} \right) \right]$$
3. By including the second term $(1 - p_{ij}) \ln(1 - q_{ij})$, UMAP penalizes dissimilarity mismatches, preserving both local neighborhood structures and global inter-cluster geometries.
4. Using nearest-neighbor descent graphs and stochastic gradient descent (SGD), UMAP executes orders of magnitude faster than standard t-SNE, enabling interactive exploration of millions of points.

### Parallel Coordinates for High-Dimensional Correlation Auditing

When dimensionality reduction embeddings obscure individual feature scales, **Parallel Coordinates** (Inselberg, 1985) display high-dimensional vectors directly without loss of information:
- The $p$ orthogonal axes of Cartesian space are mapped into $p$ parallel vertical axes evenly spaced along a horizontal baseline.
- A single observation vector $\mathbf{x}_i = (x_{i1}, x_{i2}, \dots, x_{ip})$ is represented as a continuous polyline connecting the points $(j, x_{ij})$ across all vertical axes.
- A positive correlation between variables $X_j$ and $X_{j+1}$ appears visually as a bundle of parallel lines between the two axes. A negative correlation manifests as an hourglass pencil of crossing lines intersecting at a focal point.
- Non-linear interactions, multivariate outliers, and multi-modal clustering become immediately apparent as distinct, coherent ribbon trajectories flowing through the coordinate grid.
"""
    parts = content.split("## Fully worked question 1:")
    path.write_text(parts[0] + addition + "\n## Fully worked question 1:" + parts[1], encoding="utf-8")
    print("Unit 3 expanded successfully!")

def expand_unit_4():
    path = BASE / "unit-4.md"
    content = path.read_text(encoding="utf-8")
    addition = r"""

## 4.13 Matrix Completion, Nuclear Norm Regularization, and Low-Rank Tensor Networks

In high-dimensional statistical computing, observational matrices frequently suffer from extensive missingness. In recommendation engines, epidemiological surveillance panels, and spatial environmental sensor networks, an observation matrix $\mathbf{M} \in \mathbb{R}^{m \times n}$ is observed only on a small subset of index coordinates $\Omega \subset \{1, \dots, m\} \times \{1, \dots, n\}$, with $|\Omega| \ll m \cdot n$. The mathematical goal of **matrix completion** is to recover the unobserved matrix entries by exploiting the prior knowledge that the underlying data-generating matrix possesses low rank: $\text{rank}(\mathbf{M}) = r \ll \min(m, n)$.

### The Nuclear Norm Convex Relaxation

Direct rank minimization under sampling constraints is formulated as:

$$\min_{\mathbf{X} \in \mathbb{R}^{m \times n}} \text{rank}(\mathbf{X}) \quad \text{subject to } P_\Omega(\mathbf{X}) = P_\Omega(\mathbf{M})$$

where $P_\Omega(\mathbf{X})_{ij} = X_{ij}$ if $(i, j) \in \Omega$ and $0$ otherwise. Because the rank function $\text{rank}(\mathbf{X})$ is non-convex and discontinuous, exact rank minimization is an NP-hard combinatorial problem requiring exhaustive search over combinatorial subspaces.

In a landmark theoretical breakthrough, Emmanuel Candès and Benjamin Recht (2009) demonstrated that the non-convex rank objective can be replaced by its convex envelope: the **nuclear norm** (or trace norm) $\|\mathbf{X}\|_*$, defined as the sum of the singular values:

$$\|\mathbf{X}\|_* = \sum_{i=1}^{\min(m, n)} \sigma_i(\mathbf{X})$$

The convex relaxation problem becomes:

$$\min_{\mathbf{X} \in \mathbb{R}^{m \times n}} \|\mathbf{X}\|_* \quad \text{subject to } P_\Omega(\mathbf{X}) = P_\Omega(\mathbf{M})$$

Under mild incoherence conditions on the singular vectors of $\mathbf{M}$, Candès and Recht proved that solving this convex optimization problem recovers the missing entries of $\mathbf{M}$ **exactly** with high probability, provided the number of observed entries satisfies:

$$|\Omega| \ge C \cdot n^{1.2} r \ln(n)$$

for some universal constant $C$. This remarkable result parallels the Shannon–Nyquist sampling theorem for compressed sensing, establishing that low-rank structured matrices can be perfectly reconstructed from minimal random samples.

### The Singular Value Thresholding (SVT) Algorithm

To solve the nuclear norm minimization problem computationally for large matrices where interior-point semidefinite programming is prohibitively expensive, Cai, Candès, and Shen (2010) formulated the **Singular Value Thresholding (SVT)** algorithm.

Let $\mathcal{D}_\tau(\mathbf{Y})$ denote the soft-thresholding operator applied to the singular values of matrix $\mathbf{Y}$. If the SVD of $\mathbf{Y}$ is given by $\mathbf{Y} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^T$ with singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_{\min(m, n)}$, the operator shrinks singular values toward zero by threshold $\tau > 0$:

$$\mathcal{D}_\tau(\mathbf{Y}) = \mathbf{U} \mathcal{D}_\tau(\boldsymbol{\Sigma}) \mathbf{V}^T, \quad \mathcal{D}_\tau(\boldsymbol{\Sigma}) = \text{diag}(\max(0, \sigma_i - \tau))$$

The SVT algorithm executes linearized Bregman iterations:
1. Initialize $\mathbf{Y}_0 = \mathbf{0} \in \mathbb{R}^{m \times n}$.
2. At iteration $k = 1, 2, \dots$:
   $$\mathbf{X}_k = \mathcal{D}_\tau(\mathbf{Y}_{k-1})$$
   $$\mathbf{Y}_k = \mathbf{Y}_{k-1} + \delta P_\Omega(\mathbf{M} - \mathbf{X}_k)$$
   where $\delta$ is a step size satisfying $0 < \delta < 2$.
3. Terminate when relative reconstruction error $\|P_\Omega(\mathbf{X}_k - \mathbf{M})\|_F / \|P_\Omega(\mathbf{M})\|_F$ falls below numerical tolerance $\epsilon$.

Because the singular value thresholding operator $\mathcal{D}_\tau(\mathbf{Y})$ zeroes out all singular values smaller than $\tau$, each iterate $\mathbf{X}_k$ retains low rank throughout execution. Consequently, the SVD at each step can be evaluated extremely efficiently using iterative Lanczos or randomized truncated SVD algorithms that compute only the top $k \ll \min(m, n)$ singular triplets, scaling comfortably to matrices with millions of rows and columns.

### Tensor Networks and the Tensor-Train (TT) Decomposition

When empirical data extend beyond two-dimensional matrices into $D$-way multidimensional tensors $\boldsymbol{\mathcal{X}} \in \mathbb{R}^{n_1 \times n_2 \times \dots \times n_D}$ (such as spatio-temporal demographic tensors or neuroimaging fMRI arrays), standard matrix completion faces the **curse of dimensionality**: the raw tensor requires storing $\prod_{d=1}^D n_d = n^D$ floating-point entries.

The **Tensor-Train (TT) Decomposition** (Oseledets, 2011) expresses each scalar element of the $D$-way tensor as a contracted sequence of matrix multiplications across low-dimensional 3-way core tensors $\mathbf{G}_d \in \mathbb{R}^{r_{d-1} \times n_d \times r_d}$:

$$\mathcal{X}(i_1, i_2, \dots, i_D) = \mathbf{G}_1(i_1) \mathbf{G}_2(i_2) \dots \mathbf{G}_D(i_D)$$

where $r_0 = r_D = 1$ and the dimensions $r_d$ are the **TT-ranks**. The storage footprint collapses from exponential $\mathcal{O}(n^D)$ to linear in dimension: $\mathcal{O}(D \cdot n \cdot r^2)$. Alternating Least Squares (ALS) and cross-approximation algorithms over tensor-train representations enable the estimation, regression, and completion of massive multi-way statistical data structures that would otherwise be impossible to instantiate in physical hardware.
"""
    parts = content.split("## Fully worked question 1:")
    path.write_text(parts[0] + addition + "\n## Fully worked question 1:" + parts[1], encoding="utf-8")
    print("Unit 4 expanded successfully!")

def expand_unit_7():
    path = BASE / "unit-7.md"
    content = path.read_text(encoding="utf-8")
    addition = r"""

## 7.13 Coordinate Descent, Proximal Gradients, and High-Dimensional Sparse Regression

In contemporary genomic, econometric, and biostatistical modeling, researchers frequently confront high-dimensional regression regimes where the number of candidate covariates $p$ vastly exceeds the available sample size $n$ ($p \gg n$). In such ill-posed settings, the ordinary least squares Gram matrix $\mathbf{X}^T \mathbf{X} \in \mathbb{R}^{p \times p}$ has rank at most $n$, making it singular and non-invertible. To perform consistent parameter estimation and feature selection simultaneously, statisticians introduce sparsity-inducing penalties.

### The Lasso and Elastic Net Regularization Objectives

The **Least Absolute Shrinkage and Selection Operator (Lasso)** (Tibshirani, 1996) regularizes the residual sum of squares by the $\ell_1$ norm of the parameter vector:

$$\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \left\{ \frac{1}{2n} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \lambda \|\boldsymbol{\beta}\|_1 \right\} = \min_{\boldsymbol{\beta} \in \mathbb{R}^p} \left\{ \frac{1}{2n} \sum_{i=1}^n \left( y_i - \sum_{j=1}^p X_{ij} \beta_j \right)^2 + \lambda \sum_{j=1}^p |\beta_j| \right\}$$

where $\lambda \ge 0$ is a tuning parameter controlling the degree of sparsity. When collinearity among predictors is severe, the **Elastic Net** (Zou & Hastie, 2005) combines $\ell_1$ and $\ell_2$ penalties:

$$\mathcal{L}_{\text{enet}}(\boldsymbol{\beta}) = \frac{1}{2n} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \lambda \left[ \alpha \|\boldsymbol{\beta}\|_1 + \frac{1 - \alpha}{2} \|\boldsymbol{\beta}\|_2^2 \right]$$

with mixing parameter $\alpha \in [0, 1]$. Because the $\ell_1$ norm $|\beta_j|$ has a sharp non-differentiable singularity (kink) at $\beta_j = 0$, classical smooth gradient descent and Newton–Raphson algorithms cannot be applied directly.

### Cyclic Coordinate Descent and the Soft-Thresholding Operator

Friedman, Hastie, and Tibshirani (2007, 2010) demonstrated that **Cyclic Coordinate Descent** provides an astonishingly fast, numerically stable solver for Lasso and Elastic Net problems (implemented in the celebrated `glmnet` R package and `scikit-learn`'s `Lasso` and `ElasticNet`).

Suppose all predictors are standardized so that $\frac{1}{n} \sum_{i=1}^n X_{ij}^2 = 1$. When optimizing with respect to a single coordinate $\beta_j$ while holding all other $p - 1$ coefficients $\boldsymbol{\beta}_{-j}$ fixed, the partial residual vector is:

$$\mathbf{r}_{-j} = \mathbf{y} - \sum_{k \ne j} \mathbf{x}_k \beta_k$$

The univariate objective for coordinate $j$ reduces to:

$$g(\beta_j) = \frac{1}{2n} \|\mathbf{r}_{-j} - \mathbf{x}_j \beta_j\|_2^2 + \lambda |\beta_j| = \frac{1}{2} \beta_j^2 - \left( \frac{1}{n} \mathbf{x}_j^T \mathbf{r}_{-j} \right) \beta_j + \lambda |\beta_j| + \text{constant}$$

Let $z_j = \frac{1}{n} \mathbf{x}_j^T \mathbf{r}_{-j}$ represent the simple OLS regression coefficient of the partial residuals on feature $j$. The global unconstrained minimizer of $g(\beta_j)$ is given in closed form by the **Soft-Thresholding Operator** $\mathcal{S}_\lambda(z)$:

$$\hat{\beta}_j = \mathcal{S}_\lambda(z_j) = \text{sign}(z_j) \max(0, |z_j| - \lambda) = \begin{cases} z_j - \lambda & \text{if } z_j > \lambda \\ 0 & \text{if } |z_j| \le \lambda \\ z_j + \lambda & \text{if } z_j < -\lambda \end{cases}$$

The coordinate descent algorithm repeatedly cycles through coordinates $j = 1, 2, \dots, p$:
1. Compute partial correlation $z_j = \frac{1}{n} \mathbf{x}_j^T \mathbf{r} + \beta_j$.
2. Update $\beta_j \leftarrow \mathcal{S}_\lambda(z_j)$.
3. Update residual vector $\mathbf{r} \leftarrow \mathbf{r} - \mathbf{x}_j (\beta_j^{\text{new}} - \beta_j^{\text{old}})$.

Each univariate scalar step requires only $\mathcal{O}(n)$ operations! Because the objective function decomposes into a smooth convex loss plus a separable non-smooth penalty $\sum g_j(\beta_j)$, Tseng (2001) proved that coordinate descent is **guaranteed to converge to the exact global minimum**.

### Active-Set Convergence and Pathwise Warm Starts

In production statistical software, coordinate descent achieves supercomputer-level efficiency through two algorithmic innovations:
1. **Warm Starts along a Regularization Path**: Models are solved over a descending grid of $K \approx 100$ penalty values $\lambda_{\max} > \lambda_1 > \dots > \lambda_K$. At $\lambda_{\max} = \max_j \frac{1}{n} |\mathbf{x}_j^T \mathbf{y}|$, all coefficients are identically zero ($\boldsymbol{\beta} = \mathbf{0}$). For each subsequent $\lambda_k$, the algorithm initializes search from the optimal solution $\hat{\boldsymbol{\beta}}(\lambda_{k-1})$ of the preceding problem, requiring only a handful of coordinate cycles to reach machine precision.
2. **Active-Set Strategies**: The algorithm maintains an active set $\mathcal{A} = \{j : \beta_j \ne 0\}$. Coordinate descent iterates exclusively over features in $\mathcal{A}$ until convergence. A single full cycle across all $p$ features is then executed to verify optimality via Karush–Kuhn–Tucker (KKT) conditions ($|z_k| \le \lambda$ for all $k \notin \mathcal{A}$). If any feature violates KKT, it is appended to $\mathcal{A}$ and active cycling resumes. In regimes where $p = 100,000$ and only $50$ features are active, this reduces computational effort by more than $99.9\%$.
"""
    parts = content.split("## Fully worked question 1:")
    path.write_text(parts[0] + addition + "\n## Fully worked question 1:" + parts[1], encoding="utf-8")
    print("Unit 7 expanded successfully!")

if __name__ == "__main__":
    expand_unit_2()
    expand_unit_3()
    expand_unit_4()
    expand_unit_7()
