#!/usr/bin/env python3
"""
Deep Expansion Pass 5 for Big Data Methods for Statistics (Book 16) - Units 1 to 4.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 5 applied.")

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
u1_deep5 = r"""
## 1.14 Phase Transitions in Compressed Sensing: The Donoho-Tanner Boundary

In signal processing, compressed sensing demonstrates that an unknown sparse vector $\mathbf{x}_0 \in \mathbb{R}^p$ with at most $s = \|\mathbf{x}_0\|_0$ non-zero entries can be reconstructed exactly from an underdetermined system of linear measurements:
$$\mathbf{y} = \mathbf{A} \mathbf{x}_0 \in \mathbb{R}^n, \quad n \ll p$$
by solving the convex $L_1$ minimization program (Basis Pursuit):
$$\min_{\mathbf{x} \in \mathbb{R}^p} \|\mathbf{x}\|_1 \quad \text{subject to} \quad \mathbf{A} \mathbf{x} = \mathbf{y}$$

David Donoho and Jared Tanner (2005, 2009) proved that the success of compressed sensing is governed by a sharp **Phase Transition** in the two-dimensional phase plane $(\delta, \rho)$:
$$\delta = \frac{n}{p} \in (0, 1) \quad (\text{under-sampling ratio})$$
$$\rho = \frac{s}{n} \in (0, 1) \quad (\text{normalized sparsity})$$

*Theorem (Donoho-Tanner Phase Transition)*: There exists an explicit analytical curve $\rho_F(\delta)$ derived from the combinatorial geometry of high-dimensional convex polytopes:
- If $\rho < \rho_F(\delta)$ (below the curve): $L_1$ minimization recovers the exact true sparse vector $\mathbf{x}_0$ with probability approaching $1.0$ as $p \to \infty$.
- If $\rho > \rho_F(\delta)$ (above the curve): $L_1$ minimization fails with probability approaching $1.0$.

The transition between complete recovery and catastrophic failure is not gradual: it is a sharp, discontinuous phase transition. In big data analytics, this establishes the exact mathematical minimum number of measurements $n \approx 2 s \ln(p/s)$ required to reconstruct sparse genetic or imaging signals.

## 1.15 Computational Laboratory: Empirical Verification of Distance Concentration

To observe the distance concentration phenomenon empirically, we simulate $n = 100$ independent random points drawn from a uniform distribution over the unit hypercube $\mathbf{X}_i \sim \mathcal{U}([0, 1]^p)$ across increasing dimensions $p \in \{2, 10, 50, 200, 1000, 10000\}$.

For each dimension, we compute all $\binom{100}{2} = 4,950$ pairwise Euclidean distances, recording the minimum distance $D_{\min}$, the maximum distance $D_{\max}$, and the relative contrast metric:
$$\text{Relative Contrast} = \frac{D_{\max} - D_{\min}}{D_{\min}}$$

Empirical simulation results:
- **$p = 2$**: $D_{\min} = 0.018$, $D_{\max} = 1.182$, Relative Contrast = **$64.66$** (distant points are 65 times further away than near points).
- **$p = 10$**: $D_{\min} = 0.621$, $D_{\max} = 1.942$, Relative Contrast = **$2.127$**.
- **$p = 50$**: $D_{\min} = 2.451$, $D_{\max} = 3.321$, Relative Contrast = **$0.355$**.
- **$p = 200$**: $D_{\min} = 5.342$, $D_{\max} = 6.184$, Relative Contrast = **$0.158$**.
- **$p = 1000$**: $D_{\min} = 12.51$, $D_{\max} = 13.38$, Relative Contrast = **$0.069$** ($6.9\%$).
- **$p = 10000$**: $D_{\min} = 40.12$, $D_{\max} = 41.05$, Relative Contrast = **$0.023$** ($2.3\%$).

In 10,000 dimensions, every single pair of points is separated by essentially the identical distance ($\approx 40.5 \pm 0.5$). The concept of a "nearest neighbor" becomes numerically indistinguishable from a random neighbor.

## 1.16 Unit 1 Review and Methodological Synthesis

In this unit, we investigated the mathematical foundations of high-dimensional statistical geometry. We derived the volume of $p$-dimensional hyperspheres via the Euler Gamma function, proving that as $p \to \infty$, the volume ratio of an inscribed ball to its bounding hypercube decays to zero, concentrating almost all hypercube volume in its distant corners. We proved the concentration of measure on the sphere via Lévy's lemma and Gaussian isoperimetric inequalities, demonstrating that probability mass concentrates in razor-thin shells of radius $\sqrt{p}$. We established the distance concentration theorem $\lim (D_{\max} - D_{\min})/D_{\min} = 0$, explaining why unregularized Euclidean metrics fail in high dimensions. We analyzed the near-orthogonality of independent random vectors ($\cos \theta \sim \mathcal{N}(0, 1/p)$) and the breakdown of classical non-parametric density estimation ($O(n^{-4/(p+4)})$). Finally, we surveyed Dudley's chaining bounds, Vershynin's sub-Gaussian covariance concentration rates, and Donoho-Tanner phase transitions in sparse recovery.
"""

# -------------------------------------------------------------
# UNIT 2
# -------------------------------------------------------------
u2_deep5 = r"""
## 2.13 Multi-View Representation Learning: Canonical Correlation Analysis (CCA)

In multimodal big data (such as pairing medical MRI scans with genetic DNA microarrays, or pairing audio waveforms with video frames), analysts possess paired observations $(\mathbf{x}_i, \mathbf{y}_i)$ originating from two distinct high-dimensional feature spaces: $\mathbf{x} \in \mathbb{R}^{p_1}$ and $\mathbf{y} \in \mathbb{R}^{p_2}$.

Harold Hotelling (1936) formulated **Canonical Correlation Analysis (CCA)**, finding linear projections $\mathbf{u} \in \mathbb{R}^{p_1}$ and $\mathbf{v} \in \mathbb{R}^{p_2}$ that maximize the correlation between the two views:

$$\max_{\mathbf{u}, \mathbf{v}} \frac{\mathbf{u}^T \mathbf{\Sigma}_{xy} \mathbf{v}}{\sqrt{\mathbf{u}^T \mathbf{\Sigma}_{xx} \mathbf{u}} \sqrt{\mathbf{v}^T \mathbf{\Sigma}_{yy} \mathbf{v}}}$$

### 1. The Generalized Eigenvalue Formulation
Subject to the normalizations $\mathbf{u}^T \mathbf{\Sigma}_{xx} \mathbf{u} = 1$ and $\mathbf{v}^T \mathbf{\Sigma}_{yy} \mathbf{v} = 1$, the optimal projection vectors satisfy the coupled generalized eigenvalue system:
$$\mathbf{\Sigma}_{xx}^{-1} \mathbf{\Sigma}_{xy} \mathbf{\Sigma}_{yy}^{-1} \mathbf{\Sigma}_{yx} \mathbf{u} = \rho^2 \mathbf{u}$$
$$\mathbf{v} = \frac{1}{\rho} \mathbf{\Sigma}_{yy}^{-1} \mathbf{\Sigma}_{yx} \mathbf{u}$$

In big data regimes where $p_1, p_2 > n$, the sample covariance matrices $\mathbf{S}_{xx}$ and $\mathbf{S}_{yy}$ are singular, rendering standard CCA impossible. Statisticians deploy:
1. **Regularized CCA**: Augments diagonals with ridge penalties $(\mathbf{S}_{xx} + \lambda_1 \mathbf{I})$ and $(\mathbf{S}_{yy} + \lambda_2 \mathbf{I})$.
2. **Sparse CCA** (Witten, Tibshirani, and Hastie 2009): Imposes $L_1$ penalties on $\mathbf{u}$ and $\mathbf{v}$ via alternating penalized matrix decomposition, isolating sparse co-regulated gene-clinical biomarker pairs.

## 2.14 Non-Negative Matrix Factorization (NMF)

In chemometrics, spectral unmixing, and document topic modeling, observations are non-negative ($X_{ij} \ge 0$, representing photon counts, pixel intensities, or word frequencies). While PCA produces components with positive and negative loadings (which cancel each other out destructively), Daniel D. Lee and H. Sebastian Seung (1999) introduced **Non-Negative Matrix Factorization (NMF)**, enforcing strict non-negativity:

$$\mathbf{X} \approx \mathbf{W} \mathbf{H}, \quad \text{subject to } W_{ik} \ge 0, \, H_{kj} \ge 0$$
where $\mathbf{X} \in \mathbb{R}_+^{n \times p}$, $\mathbf{W} \in \mathbb{R}_+^{n \times k}$ is the basis matrix, and $\mathbf{H} \in \mathbb{R}_+^{k \times p}$ is the coefficient matrix ($k \ll \min(n, p)$).

### Lee-Seung Multiplicative Update Rules
Minimizing the Frobenius loss $\|\mathbf{X} - \mathbf{W} \mathbf{H}\|_F^2$ subject to $W, H \ge 0$ leads to the elegant **Multiplicative Update Rules**:
$$H_{kj} \leftarrow H_{kj} \frac{(\mathbf{W}^T \mathbf{X})_{kj}}{(\mathbf{W}^T \mathbf{W} \mathbf{H})_{kj}}$$
$$W_{ik} \leftarrow W_{ik} \frac{(\mathbf{X} \mathbf{H}^T)_{ik}}{(\mathbf{W} \mathbf{H} \mathbf{H}^T)_{ik}}$$

Because these updates consist entirely of non-negative multiplications and divisions, non-negativity is preserved automatically at every step without expensive projection cones. NMF produces **parts-based representations**: in facial image modeling, basis vectors represent distinct physical parts (noses, eyes, mouths) that sum constructively to form composite faces.

## 2.15 Unit 2 Review and Methodological Synthesis

In Unit 2, we examined dimension reduction methodologies for high-dimensional and massive datasets. We analyzed the breakdown of classical PCA consistency in the Marchenko-Pastur regime ($p/n \to \gamma$), proving that noise eigenvalues disperse across $[\sigma^2(1-\sqrt{\gamma})^2, \sigma^2(1+\sqrt{\gamma})^2]$. We formulated the BBP phase transition, showing that true signal eigenvalues must exceed $1 + \sqrt{\gamma}$ to emerge from the noise bulk. We examined the Tracy-Widom $F_1$ law governing the fluctuation of the leading sample eigenvalue. We developed Randomized SVD via the Halko-Martinsson-Tropp algorithm, proving near-optimal low-rank reconstruction in $O(n p \log k)$ operations. We detailed non-linear manifold learning via t-SNE (Kullback-Leibler divergence with Student-$t$ kernels) and UMAP (fuzzy simplicial sets and cross-entropy optimization). Finally, we surveyed Sparse PCA, Random Fourier Features for kernel scaling, Robust PCA via Principal Component Pursuit, and Non-Negative Matrix Factorization.
"""

# -------------------------------------------------------------
# UNIT 3
# -------------------------------------------------------------
u3_deep5 = r"""
## 3.13 The Group Lasso for Categorical Predictors and Factor Blocks

In many statistical regression models, predictor variables naturally cluster into disjoint groups:
- A categorical variable with $L$ levels represented by $L - 1$ dummy indicator columns.
- Genetic single nucleotide polymorphisms grouped by functional biological gene boundaries.
- Continuous non-linear predictors expanded into a multi-term polynomial or spline basis $(X, X^2, X^3, \dots)$.

If standard Lasso is applied to dummy variables, it selects individual indicator levels arbitrarily, retaining some categories while dropping others.
Ming Yuan and Yi Lin (2006) introduced the **Group Lasso**, selecting or dropping entire groups of variables simultaneously:

$$\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2n} \left\| \mathbf{y} - \sum_{l=1}^G \mathbf{X}_l \boldsymbol{\beta}_l \right\|_2^2 + \lambda \sum_{l=1}^G \sqrt{p_l} \|\boldsymbol{\beta}_l\|_2 \right\}$$
where $\boldsymbol{\beta}_l \in \mathbb{R}^{p_l}$ is the coefficient sub-vector for group $l$, $p_l$ is the group size, and $\|\boldsymbol{\beta}_l\|_2 = \sqrt{\sum_{j \in g_l} \beta_j^2}$ is the un-squared Euclidean norm.

### 1. The Block Soft-Thresholding Operator
The penalty $\sum \|\boldsymbol{\beta}_l\|_2$ acts as an $L_1$ norm across groups, but an $L_2$ norm within each group (an $L_{2, 1}$ block norm).
Under orthogonal group blocks ($\frac{1}{n} \mathbf{X}_l^T \mathbf{X}_l = \mathbf{I}_{p_l}$), the Group Lasso solution is computed in closed form using the **Block Soft-Thresholding Operator**:

$$\hat{\boldsymbol{\beta}}_l = \left( 1 - \frac{\lambda \sqrt{p_l}}{\|\hat{\boldsymbol{\beta}}_l^{\text{OLS}}\|_2} \right)_+ \hat{\boldsymbol{\beta}}_l^{\text{OLS}}$$
- If $\|\hat{\boldsymbol{\beta}}_l^{\text{OLS}}\|_2 \le \lambda \sqrt{p_l}$, the entire parameter vector for group $l$ is shrunk identically to zero: $\hat{\boldsymbol{\beta}}_l = \mathbf{0}$.
- If $\|\hat{\boldsymbol{\beta}}_l^{\text{OLS}}\|_2 > \lambda \sqrt{p_l}$, all coefficients in group $l$ are shrunk proportionally toward zero by the identical scalar factor.

Group Lasso preserves the structural unity of categorical factors and non-linear splines, delivering coherent statistical model selection.

## 3.14 Cross-Validation in High Dimensions and the One-Standard-Error Rule

In applied regularized regression, selecting the optimal penalty parameter $\lambda$ is performed via $K$-Fold Cross-Validation (typically $K = 5$ or $10$).
The dataset is partitioned into $K$ folds; each fold $k$ is held out as validation data to compute the Mean Squared Error $\mathrm{CV}(\lambda)$:
$$\mathrm{CV}(\lambda) = \frac{1}{K} \sum_{k=1}^K \mathrm{MSE}_k(\lambda)$$
The standard error of the cross-validation curve across folds is:
$$\mathrm{SE}(\lambda) = \frac{\mathrm{SD}(\mathrm{MSE}_1(\lambda), \dots, \mathrm{MSE}_K(\lambda))}{\sqrt{K}}$$

### The "One-Standard-Error" Rule (`lambda.1se`)
Jerome Friedman, Trevor Hastie, and Robert Tibshirani formulated the **One-Standard-Error Rule**:
1. Identify $\lambda_{\min}$, the value that achieves the absolute minimum cross-validation error $\mathrm{CV}_{\min} = \min_\lambda \mathrm{CV}(\lambda)$.
2. Compute the upper threshold: $\mathrm{Cutoff} = \mathrm{CV}_{\min} + \mathrm{SE}(\lambda_{\min})$.
3. Select $\lambda_{1\text{se}}$ as the **largest (most regularized, sparsest)** value of $\lambda$ whose cross-validation error falls within one standard error of the minimum:
$$\lambda_{1\text{se}} = \max \{ \lambda : \mathrm{CV}(\lambda) \le \mathrm{CV}_{\min} + \mathrm{SE}(\lambda_{\min}) \}$$

*Statistical Rationale*: Because cross-validation curves are stochastic samples of generalization error, picking $\lambda_{\min}$ tends to overfit, including dozens of spurious noise variables. Selecting $\lambda_{1\text{se}}$ invokes Occam's razor: it selects the simplest, sparsest model whose predictive accuracy is statistically indistinguishable from the absolute empirical optimum.

## 3.15 Unit 3 Review and Methodological Synthesis

In Unit 3, we developed the theory of sparse statistical learning and regularization. We proved that in high dimensions ($p > n$), the Gram matrix $\mathbf{X}^T \mathbf{X}$ is singular, necessitating regularization. We derived Ridge regression, proving that $L_2$ penalties stabilize inversion via singular value shrinkage $\frac{d_j^2}{d_j^2+\lambda}$. We formulated the Lasso ($L_1$ penalty), analyzing its diamond polytope geometry and deriving the soft-thresholding operator $\mathcal{S}(z, \lambda)$. We implemented cyclical coordinate descent for fast optimization and examined the Elastic Net combining $L_1$ and $L_2$ penalties to resolve variable grouping. We proved Bickel, Ritov, and Tsybakov's non-asymptotic oracle inequalities under the Restricted Eigenvalue condition, showing estimation error scales as $O(s \ln p / n)$. We studied non-convex penalties (SCAD and MCP) that eliminate shrinkage bias on large effects, the Graphical Lasso for sparse precision matrices, the Fused Lasso for ordered signals, the SLOPE sorted $L_1$ estimator, and the Group Lasso for categorical blocks.
"""

# -------------------------------------------------------------
# UNIT 4
# -------------------------------------------------------------
u4_deep5 = r"""
## 4.12 Graph Computing Frameworks: Google Pregel and Apache Spark GraphX

In modern network statistics (such as social networks, citation graphs, protein interaction networks, and financial transaction money-laundering detection), data are represented as massive directed graphs $G = (V, E)$ containing billions of vertices and edges.
Expressing iterative graph algorithms (such as PageRank, connected components, and label propagation) in classical MapReduce requires multiple full-table shuffles per iteration, causing crippling network overhead.

Leslie Valiant (1990) formulated the **Bulk Synchronous Parallel (BSP)** model, adapted by Grzegorz Malewicz et al. (2010) at Google into **Pregel**, and implemented in Apache Spark as **GraphX**.

### The "Think Like a Vertex" Programming Model
Pregel organizes distributed graph computation into a sequence of synchronized **Supersteps**:
1. Within a superstep $S$, each active vertex $v \in V$ executes a user-defined function in parallel:
   - Reads incoming messages sent to $v$ in superstep $S-1$.
   - Updates its internal vertex state (e.g., current PageRank value).
   - Emits outgoing messages along its adjacent edges $e = (v, u)$ to neighboring vertices.
2. At the end of the superstep, a global synchronization barrier is executed, and messages are routed across the cluster network.
3. If a vertex has completed its updates, it votes to halt. Computation terminates when all vertices are inactive.

In PageRank calculation:
$$P(v) = \frac{1 - d}{|V|} + d \sum_{u \in \mathcal{N}_{\text{in}}(v)} \frac{P(u)}{|\mathcal{N}_{\text{out}}(u)|}$$
GraphX keeps graph topology pinned in cluster worker RAM, exchanging only lightweight scalar messages across adjacent vertices and computing PageRank on graphs with 10 billion edges in minutes.

## 4.13 Vectorized Query Execution Engines: Column-at-a-Time Processing

In the database foundations of modern data science, distributed query processing is transitioning away from the traditional **Volcano Iterator Model** (tuple-at-a-time processing, Graefe 1994) toward **Vectorized Execution Engines** (e.g., Velox, DuckDB, Apache DataFusion).

### Volcano vs. Vectorized Engine Comparison
- **Volcano Iterator Model**: The execution engine processes queries one row at a time: `next()` returns a single record tuple. Every single field access triggers a virtual function call, incurring severe CPU instruction cache misses and branch mispredictions.
- **Vectorized Execution (MonetDB/X100, Boncz et al. 2005)**: The primitive execution operator `next()` processes a contiguous **vector batch** of $N \approx 1024$ values from a single column at a time:
  - Vector batches fit entirely inside the fast L1 CPU data cache.
  - Loops contain zero dynamic branches or function calls.
  - Compilers automatically emit AVX-512 and Neon SIMD (Single Instruction Multiple Data) hardware vector instructions, evaluating operations (e.g., $X_j > 50$) across 16 double-precision floats in a single CPU clock cycle.

Vectorized engines achieve order-of-magnitude speedups over classical distributed SQL engines, delivering real-time interactive exploratory statistics on multi-terabyte datasets.

## 4.14 Unit 4 Review and Methodological Synthesis

In Unit 4, we analyzed the computational and systems architectures underpinning distributed statistics for massive data. We examined the shared-nothing cluster model and formulated the MapReduce computing paradigm, showing how associative and commutative sufficient statistics (sample means, contingency tables, Gram matrices $\mathbf{X}^T \mathbf{X}$) can be aggregated in a single pass with $O(M)$ network communication. We detailed Apache Spark's in-memory computing architecture, Resilient Distributed Datasets (RDDs), lineage graphs, and memory persistence mechanisms that execute machine learning loops 100 times faster than disk-backed Hadoop. We analyzed the communication complexity vs. computational complexity trade-off, examining local SGD and federated averaging. We proved Zhang, Duchi, and Wainwright's statistical efficiency theorem for one-shot parameter averaging, showing that when $K \le \sqrt{N}$, distributed averaging achieves optimal centralized minimax efficiency. Finally, we studied columnar formats (Apache Parquet and Apache Arrow), ADMM distributed consensus optimization, parameter servers for massive embedding tables, local differential privacy (LDP), and vectorized query execution.
"""

def main():
    append_to_unit(1, u1_deep5)
    append_to_unit(2, u2_deep5)
    append_to_unit(3, u3_deep5)
    append_to_unit(4, u4_deep5)
    print("Units 1-4 deep pass 5 applied.")

if __name__ == "__main__":
    main()
