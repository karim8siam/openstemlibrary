#!/usr/bin/env python3
"""
Cross 25,500 substantive prose words for Big Data Methods for Statistics (Book 16).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} boosted.")

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
u1_cross = r"""
## 1.20 Kolmogorov $n$-Widths and Linear Approximation Complexity

In theoretical non-parametric functional data analysis, the intrinsic complexity of estimating unknown smooth regression functions $f \in \mathcal{F}$ is quantified by **Kolmogorov $n$-Widths**, formulated by Andrey Kolmogorov in 1936.

Let $\mathcal{F}$ be a subset of a normed linear space $(X, \|\cdot\|)$ (such as a Sobolev ball $W^{s, 2}$ of functions with $s$ square-integrable derivatives). The Kolmogorov $n$-width $d_n(\mathcal{F}, X)$ measures the minimal worst-case distance between $\mathcal{F}$ and the best possible $n$-dimensional linear subspace $X_n \subset X$:

$$d_n(\mathcal{F}, X) = \inf_{X_n \subset X, \dim(X_n) \le n} \sup_{f \in \mathcal{F}} \inf_{g \in X_n} \|f - g\|$$

*Theorem (Kolmogorov Width Decay for Sobolev Classes)*: For Sobolev functions on a $p$-dimensional domain $[0, 1]^p$ with smoothness parameter $s$:
$$d_n(W^{s, 2}([0, 1]^p), L^2) \asymptotically \Theta\left( n^{-\frac{s}{p}} \right)$$

Notice the catastrophic exponent $-s/p$: to reduce approximation error by a factor of 10 in $p = 100$ dimensions with smoothness $s = 2$, the required linear subspace dimension must scale by:
$$n_{\text{req}} = 10^{p/s} = 10^{100/2} = 10^{50} \text{ dimensions}$$
This fundamental functional analysis theorem proves that linear approximation schemes (such as Fourier series or polynomial expansions) are physically incapable of overcoming the curse of dimensionality in high dimensions without structural sparsity or low-rank manifold constraints.
"""

# -------------------------------------------------------------
# UNIT 2
# -------------------------------------------------------------
u2_cross = r"""
## 2.19 The Continuous Fokker-Planck Limit of Graph Laplacians

In spectral dimension reduction and diffusion maps (Unit 2.10), data points $\mathbf{x}_1, \dots, \mathbf{x}_n$ are assumed to be sampled from an underlying probability density $p(\mathbf{x})$ supported on a smooth, compact Riemannian manifold $\mathcal{M} \subset \mathbb{R}^p$.
A fundamental theoretical question is: *what does the discrete normalized graph Laplacian matrix $\mathbf{L} = \mathbf{D}^{-1} \mathbf{W} - \mathbf{I}$ converge to as the sample size $n \to \infty$ and neighborhood bandwidth $\epsilon \to 0$?*

Ronald Coifman and Stéphane Lafon (2006) proved that under the $\alpha$-normalization:
$$W_{ij}^{(\alpha)} = \frac{W_{ij}}{p(\mathbf{x}_i)^\alpha p(\mathbf{x}_j)^\alpha}$$
the discrete graph transition operator converges to a continuous differential operator:

$$\lim_{n \to \infty, \epsilon \to 0} \frac{\mathbf{P}_\alpha - \mathbf{I}}{\epsilon} f(\mathbf{x}) = \Delta_{\mathcal{M}} f(\mathbf{x}) + (2 - 2\alpha) \frac{\nabla p(\mathbf{x})}{p(\mathbf{x})} \cdot \nabla f(\mathbf{x})$$
where $\Delta_{\mathcal{M}}$ is the intrinsic Laplace-Beltrami operator on the manifold.
- When $\alpha = 0$ (standard normalized cuts), the diffusion includes a drift term along the gradient of the data density $\nabla p / p$.
- When $\alpha = 1$ (the Laplace-Beltrami normalization), the density drift term drops out completely ($(2 - 2(1)) = 0$), leaving strictly $\Delta_{\mathcal{M}} f(\mathbf{x})$.

*Profound Methodological Consequence*: Setting $\alpha = 1$ in diffusion maps allows the statistician to **recover the pure intrinsic Riemannian geometry of the manifold**, completely decoupled from the non-uniform sampling density of the data points!
"""

# -------------------------------------------------------------
# UNIT 3
# -------------------------------------------------------------
u3_cross = r"""
## 3.19 The Dantzig Selector of Candès and Tao

In 2007, Emmanuel Candès and Terence Tao introduced the **Dantzig Selector**, an elegant alternative to the Lasso that casts sparse high-dimensional regression as a convex **Linear Program (LP)**:

$$\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \|\boldsymbol{\beta}\|_1 \quad \text{subject to} \quad \left\| \frac{1}{n} \mathbf{X}^T (\mathbf{y} - \mathbf{X} \boldsymbol{\beta}) \right\|_\infty \le \lambda$$
where $\|\mathbf{v}\|_\infty = \max_{1 \le j \le p} |v_j|$ is the maximum absolute coordinate.

### Equivalence and Linear Programming Solvers
The constraint $\| \frac{1}{n} \mathbf{X}^T (\mathbf{y} - \mathbf{X} \boldsymbol{\beta}) \|_\infty \le \lambda$ enforces that the residual vector $\mathbf{r} = \mathbf{y} - \mathbf{X} \boldsymbol{\beta}$ cannot have correlation larger than $\lambda$ with any predictor column in $\mathbf{X}$.
Setting $\boldsymbol{\beta} = \mathbf{u} - \mathbf{v}$ with $\mathbf{u}, \mathbf{v} \ge \mathbf{0}$, the Dantzig Selector is expressed as a canonical linear program:
$$\min_{\mathbf{u}, \mathbf{v}} \sum_{j=1}^p (u_j + v_j) \quad \text{subject to} \quad -\lambda \mathbf{1} \le \frac{1}{n} \mathbf{X}^T (\mathbf{y} - \mathbf{X}(\mathbf{u} - \mathbf{v})) \le \lambda \mathbf{1}, \quad \mathbf{u}, \mathbf{v} \ge \mathbf{0}$$

Candès and Tao proved that under the Restricted Isometry Property with $\delta_{2s} < \sqrt{2} - 1 \approx 0.414$, the Dantzig Selector achieves the exact same optimal oracle estimation bound as the Lasso:
$$\|\hat{\boldsymbol{\beta}}_{\text{DS}} - \boldsymbol{\beta}^*\|_2^2 \le C \sigma^2 \frac{s \ln p}{n}$$
Because it is a linear program, the Dantzig Selector can be solved via standard interior-point and simplex solvers, providing a crucial bridge between compressed sensing and sparse statistics.
"""

# -------------------------------------------------------------
# UNIT 4
# -------------------------------------------------------------
u4_cross = r"""
## 4.17 Distributed Fault Tolerance and Straggler Mitigation

In large-scale distributed computing clusters comprising thousands of commodity servers, hardware failure is not an exceptional anomaly; it is a routine, continuous certainty. If each server has a Mean Time Between Failures (MTBF) of 3 years ($1,095$ days), a cluster containing 10,000 servers experiences an average of **nine server crashes every single day**.

### 1. Lineage Graphs vs. Periodic Checkpointing
Classical distributed systems relied on global coordinated checkpointing: pausing computation every 30 minutes to serialize all memory state to distributed disks (HDFS). In statistical learning, checkpointing consumes up to $50\%$ of cluster compute capacity.
Apache Spark eliminates checkpointing through **Deterministic Lineage Graphs**: because transformations (e.g., `map`, `filter`) are pure mathematical functions, if worker node 42 fails, Spark re-schedules only the specific lost partition on an idle worker, recomputing it from the original input blocks in seconds.

### 2. Straggler Mitigation via Speculative Execution
In large distributed matrix operations, algorithmic progress is bounded by the slowest machine in the cluster (**The Straggler Problem**). Slower execution can be caused by localized network congestion, failing hard drive sectors, or background operating system garbage collection pauses.
Modern big data engines deploy **Speculative Execution**: the master driver monitors task progress across all nodes. If a task runs significantly slower than the median task completion time, the driver launches an identical speculative copy of the task on a different idle node. The node that completes first writes the result, while the redundant straggler task is killed. Speculative execution reduces long-tail latency by $70\%$.
"""

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
u5_cross = r"""
## 5.15 Stochastic Mirror Descent and Bregman Divergences

In standard Euclidean stochastic gradient descent, updates are restricted to the $L_2$ norm. However, in many statistical learning problems, parameters reside on non-Euclidean geometries:
- In probability estimation and multi-class classification, the parameter vector is a probability distribution residing on the unit simplex $\Delta^{d-1} = \{ \mathbf{w} \in \mathbb{R}^d : w_j \ge 0, \sum w_j = 1 \}$.
- In quantum state estimation and metric learning, parameters are positive semi-definite density matrices on the spectraplex $\mathcal{S}_+^d$.

Arkadi Nemirovski and David B. Yudin (1983) developed **Mirror Descent**, generalizing gradient descent to arbitrary Banach spaces using **Bregman Divergences**.

### 1. Bregman Divergence Formulation
Let $\psi: \Omega \to \mathbb{R}$ be a strictly convex, continuously differentiable distance-generating function. The Bregman divergence associated with $\psi$ is:
$$D_\psi(\mathbf{x}, \mathbf{y}) = \psi(\mathbf{x}) - \psi(\mathbf{y}) - \langle \nabla \psi(\mathbf{y}), \mathbf{x} - \mathbf{y} \rangle$$
- If $\psi(\mathbf{x}) = \frac{1}{2} \|\mathbf{x}\|_2^2$, then $D_\psi(\mathbf{x}, \mathbf{y}) = \frac{1}{2} \|\mathbf{x} - \mathbf{y}\|_2^2$ (standard Euclidean distance).
- If $\psi(\mathbf{x}) = \sum_{j=1}^d x_j \ln x_j$ (negative entropy on the simplex), then $D_\psi(\mathbf{x}, \mathbf{y}) = \sum x_j \ln(x_j / y_j) = \mathcal{D}_{\text{KL}}(\mathbf{x} \parallel \mathbf{y})$ (Kullback-Leibler divergence).

### 2. The Stochastic Mirror Descent Update
At step $t$, Mirror Descent updates parameters by solving:
$$\mathbf{w}_{t+1} = \arg\min_{\mathbf{w} \in \Omega} \left\{ \langle \mathbf{g}_t, \mathbf{w} \rangle + \frac{1}{\eta_t} D_\psi(\mathbf{w}, \mathbf{w}_t) \right\}$$
When using the entropic regularizer on the probability simplex, this update yields the famous **Exponentiated Gradient (Softmax) Update**:
$$w_{t+1, j} = \frac{w_{t, j} \exp(-\eta_t g_{t, j})}{\sum_{k=1}^d w_{t, k} \exp(-\eta_t g_{t, k})}$$

*Theoretical Advantage*: On a $d$-dimensional unit simplex, standard Euclidean SGD has convergence rate scaling as $O(\sqrt{d / T})$, degrading rapidly with dimension. Entropic Mirror Descent achieves a convergence rate scaling as:
$$O\left( \sqrt{\frac{\ln d}{T}} \right)$$
The dependence on dimension is **logarithmic**! In probability spaces with $d = 1,000,000$ categories, Mirror Descent converges hundreds of times faster than standard SGD.
"""

# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
u6_cross = r"""
## 6.14 Oblivious Subspace Embeddings for $L_1$ Robust Regression

In classical least squares regression, sketching matrices target the $L_2$ Euclidean norm. However, Ordinary Least Squares is highly sensitive to heavy-tailed noise and gross response outliers. **$L_1$ Regression** (Least Absolute Deviations) provides robust parameter estimation:
$$\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_1 = \sum_{i=1}^n |y_i - \mathbf{x}_i^T \boldsymbol{\beta}|$$

Kenneth L. Clarkson et al. (2013) proved that Gaussian and Rademacher sketches fail for $L_1$ norms because the $L_1$ norm does not concentrate under Gaussian projections.

### Cauchy Random Projections
Clarkson et al. introduced **Cauchy Random Projections**:
Construct a sketch matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times n}$ where each entry $\Pi_{ij}$ is drawn independently from a standard **Cauchy distribution**:
$$f(x) = \frac{1}{\pi (1 + x^2)}$$
By the 1-stability of the Cauchy distribution: for any vector $\mathbf{v} \in \mathbb{R}^n$, the inner product $\sum_{j=1}^n \Pi_{ij} v_j$ is distributed as $\|\mathbf{v}\|_1 \cdot Z$, where $Z$ is a standard Cauchy scalar!

Because the Cauchy distribution has infinite mean and infinite variance, the sketched $L_1$ norm is estimated via the sample **median** rather than the sample mean:
$$\hat{\|\mathbf{v}\|}_1 = \mathrm{median}\left( |\Pi_{1} \mathbf{v}|, \dots, |\Pi_{k} \mathbf{v}| \right)$$
This **Oblivious Subspace Embedding (OSE)** embeds the $n$-dimensional $L_1$ column space of $\mathbf{X}$ into a lower-dimensional space $k = O(p \ln p)$ in $O(n p \log p)$ time, allowing massive robust $L_1$ regression models to be solved with linear programming interior-point solvers in seconds.
"""

# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
u7_cross = r"""
## 7.16 The Misra-Gries Streaming Summarization Algorithm

In Unit 7.10, we examined the Space-Saving algorithm for identifying frequent items. Jayadev Misra and David Gries (1982) formulated the original **Misra-Gries Algorithm**, providing a deterministic streaming summary that guarantees bounded frequency estimation errors.

### Algorithmic Mechanics
Given parameter $k$, maintain at most $k - 1$ distinct items and their non-negative integer counters.
When stream item $x$ arrives:
1. If $x$ is currently monitored, increment its counter: $c_x \leftarrow c_x + 1$.
2. If $x$ is not monitored and fewer than $k - 1$ items are stored, insert $x$ with count $c_x = 1$.
3. If $x$ is not monitored and the table is full ($k - 1$ items present):
   - **Simultaneously decrement all $k - 1$ stored counters by 1**:
$$c_j \leftarrow c_j - 1 \quad \forall j$$
   - Remove any items whose counters drop to $0$.

*Theorem (Misra-Gries Guarantee)*: Let $N$ be the total length of the data stream. For any item $x$, the estimated count $\hat{f}_x$ satisfies:
$$f_x - \frac{N}{k} \le \hat{f}_x \le f_x$$
The maximum underestimation error is bounded strictly by $N/k$.
To guarantee that any item appearing more than $1\%$ of the time ($\phi = 0.01$) is detected, setting $k = 100$ monitors only 99 counters! Misra-Gries requires zero hash functions, executes with zero random numbers, and provides deterministic worst-case frequency bounds.
"""

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
u8_cross = r"""
## 8.15 Multiple Testing under Positive Dependence: Proof of the PRDS Condition

In Section 8.2, we stated that the Benjamini-Hochberg (BH) procedure controls the False Discovery Rate under the **Positive Regression Dependency on a Subset (PRDS)** property. Here, we present the mathematical definition and theoretical proof sketch.

### Definition of PRDS
A vector of test statistics $\mathbf{X} = (X_1, \dots, X_m)$ is said to satisfy **Positive Regression Dependency on a Subset $I_0$** (where $I_0$ is the set of true null hypotheses) if for any increasing set $D \subseteq \mathbb{R}^m$ and for any index $i \in I_0$:
$$P(\mathbf{X} \in D \mid X_i = x) \text{ is a non-decreasing function of } x$$
PRDS is satisfied by:
- Multivariate normal test statistics with non-negative correlation matrix ($\Sigma_{jk} \ge 0$).
- Absolute Student-$t$ statistics sharing a common denominator variance estimate.
- One-sided tests comparing treatment groups against a common control group (Dunnett's test).

### The Benjamini-Yekutieli Proof of FDR Control under PRDS
Let $V$ be the number of false discoveries and $R$ the total discoveries.
$$\mathrm{FDR} = \mathbb{E}\left[ \frac{V}{\max(R, 1)} \right] = \sum_{i \in I_0} \mathbb{E}\left[ \frac{\mathbb{I}(H_i \text{ is rejected})}{\max(R, 1)} \right]$$
Condition on the $p$-value of true null hypothesis $i$: $P_i = p$.
Under the BH step-up rule, $H_i$ is rejected if and only if $P_i \le \frac{R}{m} q^*$, which is equivalent to $R \ge \frac{m P_i}{q^*}$.
$$\mathbb{E}\left[ \frac{\mathbb{I}(H_i \text{ rejected})}{\max(R, 1)} \,\middle|\, P_i = p \right] = \sum_{r=1}^m \frac{1}{r} P\left( R = r, \, p \le \frac{r}{m} q^* \,\middle|\, P_i = p \right)$$
Summing over $p$ and using the PRDS property to bound the conditional probabilities yields:
$$\mathrm{FDR} \le \sum_{i \in I_0} \frac{q^*}{m} = \frac{m_0}{m} q^* \le q^*$$
This rigorous proof guarantees that in genetic association studies with non-negative linkage disequilibrium (LD) blocks, the Benjamini-Hochberg procedure strictly controls FDR.
"""

def main():
    append_to_unit(1, u1_cross)
    append_to_unit(2, u2_cross)
    append_to_unit(3, u3_cross)
    append_to_unit(4, u4_cross)
    append_to_unit(5, u5_cross)
    append_to_unit(6, u6_cross)
    append_to_unit(7, u7_cross)
    append_to_unit(8, u8_cross)
    print("All 8 units cross 25k applied.")

if __name__ == "__main__":
    main()
