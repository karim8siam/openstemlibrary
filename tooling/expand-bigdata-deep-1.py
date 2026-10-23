#!/usr/bin/env python3
"""
Deep Expansion Pass 1 for Big Data Methods for Statistics (Book 16).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 1 applied.")

# -------------------------------------------------------------
# UNIT 1 DEEP
# -------------------------------------------------------------
u1_deep = r"""
## 1.10 Metric Entropy, Covering Numbers, and Dudley's Chaining

In empirical process theory and high-dimensional non-parametric statistics, bounding the uniform deviations of stochastic processes $\sup_{f \in \mathcal{F}} |\mathbb{E}_n[f] - \mathbb{E}[f]|$ requires quantifying the "size" or intrinsic complexity of function classes $\mathcal{F}$ in metric spaces. 

### 1. Covering and Packing Numbers
Let $(T, d)$ be a pseudo-metric space.
- An **$\epsilon$-Covering** of $T$ is a set of points $\{t_1, \dots, t_N\} \subset T$ such that for every $t \in T$, there exists some $t_j$ with $d(t, t_j) \le \epsilon$. The **Covering Number** $N(T, d, \epsilon)$ is the minimal cardinality of such an $\epsilon$-cover.
- An **$\epsilon$-Packing** of $T$ is a set of points $\{s_1, \dots, s_M\} \subset T$ such that for all $i \ne j$, $d(s_i, s_j) > \epsilon$. The **Packing Number** $D(T, d, \epsilon)$ is the maximal cardinality of an $\epsilon$-packing.

The duality theorem of Kolmogorov and Tikhomirov (1959) connects covering and packing:
$$N(T, d, \epsilon) \le D(T, d, \epsilon) \le N(T, d, \epsilon/2)$$
The quantity $\mathcal{H}(T, d, \epsilon) = \ln N(T, d, \epsilon)$ is known as the **Metric Entropy** (Kolmogorov entropy) of the space.

### 2. Dudley's Chaining Integral
Consider a zero-mean sub-Gaussian random process $\{X_t\}_{t \in T}$ indexed by metric space $(T, d)$, satisfying $\mathbb{E}[e^{\lambda(X_s - X_t)}] \le e^{\lambda^2 d^2(s, t) / 2}$.
A naive union bound over an $\epsilon$-net yields an error bound that diverges if $\epsilon \to 0$. Richard M. Dudley (1967) invented the technique of **Chaining**, forming an infinite sequence of nested approximations at geometrically decreasing scales $\epsilon_k = 2^{-k}$.

*Theorem (Dudley's Chaining Bound)*: Let $D = \mathrm{diam}(T) = \sup_{s, t \in T} d(s, t)$. Then the expected supremum is bounded by:

$$\mathbb{E}\left[ \sup_{t \in T} X_t \right] \le 8 \sqrt{2} \int_0^D \sqrt{\ln N(T, d, \epsilon)}\,d\epsilon$$

Dudley's integral provides the universal tool for deriving non-asymptotic risk bounds for high-dimensional LASSO, kernel regression, and deep neural network generalization errors.

## 1.11 Slepian's Inequality and Gordon's Min-Max Comparison

Comparing the suprema of high-dimensional Gaussian processes is made possible by David Slepian's (1962) lemma and its powerful generalization by Yehoram Gordon (1985).

*Theorem (Slepian's Comparison Inequality)*: Let $\mathbf{X} = (X_1, \dots, X_p)^T$ and $\mathbf{Y} = (Y_1, \dots, Y_p)^T$ be centered Gaussian random vectors in $\mathbb{R}^p$ such that:
1. $\mathbb{E}[X_i^2] = \mathbb{E}[Y_i^2]$ for all $i = 1, \dots, p$.
2. $\mathbb{E}[X_i X_j] \le \mathbb{E}[Y_i Y_j]$ for all $i \ne j$.
Then for any threshold $c \in \mathbb{R}$:
$$P\left( \max_{1 \le i \le p} X_i \le c \right) \le P\left( \max_{1 \le i \le p} Y_i \le c \right) \implies \mathbb{E}\left[ \max_{1 \le i \le p} X_i \right] \ge \mathbb{E}\left[ \max_{1 \le i \le p} Y_i \right]$$

*Intuition*: Decreasing the correlations between Gaussian variables pushes them further apart, driving the maximum higher. Gordon's Gaussian Min-Max Theorem (GMT) extends this to bilinear forms $\max_{\mathbf{u}} \min_{\mathbf{v}} \mathbf{u}^T \mathbf{G} \mathbf{v}$, forming the mathematical engine used by Sur and Candès (2019) to prove exact asymptotic phase transitions in high-dimensional logistic regression.
"""

# -------------------------------------------------------------
# UNIT 2 DEEP
# -------------------------------------------------------------
u2_deep = r"""
## 2.9 Random Fourier Features for Scalable Kernel Approximations

In non-linear dimension reduction and kernel learning, evaluating the full $n \times n$ Gram matrix $\mathbf{K}$ requires $O(n^2)$ computation and memory. In Unit 2.3, we examined the Nyström approximation. An alternative paradigm developed by Ali Rahimi and Benjamin Recht (2007) avoids computing kernel matrices altogether by mapping data into explicit randomized Euclidean feature spaces.

### 1. Bochner's Theorem on Shift-Invariant Kernels
A continuous shift-invariant kernel $k(\mathbf{x}, \mathbf{y}) = k(\mathbf{x} - \mathbf{y})$ on $\mathbb{R}^p$ is positive definite if and only if $k(\boldsymbol{\Delta})$ is the Fourier transform of a non-negative bounded Borel measure $p(\boldsymbol{\omega})$:

$$k(\mathbf{x} - \mathbf{y}) = \int_{\mathbb{R}^p} p(\boldsymbol{\omega}) e^{i \boldsymbol{\omega}^T (\mathbf{x} - \mathbf{y})}\,d\boldsymbol{\omega} = \mathbb{E}_{\boldsymbol{\omega} \sim p}\left[ \cos(\boldsymbol{\omega}^T (\mathbf{x} - \mathbf{y})) \right]$$
For the standard Gaussian RBF kernel $k(\mathbf{x}, \mathbf{y}) = \exp(-\gamma \|\mathbf{x} - \mathbf{y}\|_2^2)$, the spectral distribution $p(\boldsymbol{\omega})$ is a multivariate Gaussian $\mathcal{N}(\mathbf{0}, 2\gamma \mathbf{I}_p)$.

### 2. The Random Fourier Feature Mapping
Rahimi and Recht constructed a randomized low-dimensional feature map $\mathbf{z}: \mathbb{R}^p \to \mathbb{R}^{2D}$:
1. Sample $D$ independent frequency vectors $\boldsymbol{\omega}_1, \dots, \boldsymbol{\omega}_D \sim p(\boldsymbol{\omega}) = \mathcal{N}(\mathbf{0}, 2\gamma \mathbf{I}_p)$.
2. For any input vector $\mathbf{x} \in \mathbb{R}^p$, define the randomized feature vector:
$$\mathbf{z}(\mathbf{x}) = \frac{1}{\sqrt{D}} \left[ \cos(\boldsymbol{\omega}_1^T \mathbf{x}), \dots, \cos(\boldsymbol{\omega}_D^T \mathbf{x}), \sin(\boldsymbol{\omega}_1^T \mathbf{x}), \dots, \sin(\boldsymbol{\omega}_D^T \mathbf{x}) \right]^T$$

By trigonometric addition formulas:
$$\langle \mathbf{z}(\mathbf{x}), \mathbf{z}(\mathbf{y}) \rangle = \frac{1}{D} \sum_{j=1}^D \left[ \cos(\boldsymbol{\omega}_j^T \mathbf{x}) \cos(\boldsymbol{\omega}_j^T \mathbf{y}) + \sin(\boldsymbol{\omega}_j^T \mathbf{x}) \sin(\boldsymbol{\omega}_j^T \mathbf{y}) \right] = \frac{1}{D} \sum_{j=1}^D \cos(\boldsymbol{\omega}_j^T (\mathbf{x} - \mathbf{y}))$$
By the Law of Large Numbers, $\langle \mathbf{z}(\mathbf{x}), \mathbf{z}(\mathbf{y}) \rangle \to k(\mathbf{x}, \mathbf{y})$.

*Computational Revolution*: Any non-linear kernel regression or PCA problem on $n = 10^7$ observations can be solved by transforming data into explicit $2D$-dimensional vectors $\mathbf{z}(\mathbf{x})$ and fitting standard linear OLS or linear PCA in $O(n D)$ time, transforming non-linear kernel estimation from an $O(n^2)$ impossible task into a streaming linear regression problem.

## 2.10 Diffusion Maps and Spectral Geometry

Ronald Coifman and Stéphane Lafon (2006) introduced **Diffusion Maps**, discovering low-dimensional manifold coordinates by modeling heat diffusion and random walks on data graphs.

### 1. The Normalized Graph Laplacian
Let $\mathbf{W} \in \mathbb{R}^{n \times n}$ be an affinity matrix with Gaussian weights $W_{ij} = \exp(-\|\mathbf{x}_i - \mathbf{x}_j\|_2^2 / \epsilon)$. Let $\mathbf{D} = \mathrm{diag}(\sum_j W_{ij})$ be the degree matrix.
The Markov transition matrix governing random walk diffusion across the data manifold is:
$$\mathbf{P} = \mathbf{D}^{-1} \mathbf{W}$$
where $P_{ij} = P(\mathbf{x}_{t+1} = \mathbf{x}_j \mid \mathbf{x}_t = \mathbf{x}_i)$. Running the random walk for $t$ discrete timesteps yields transition probabilities $P_{ij}^{(t)} = (\mathbf{P}^t)_{ij}$.

### 2. Diffusion Distance and Spectral Coordinate Mapping
The **Diffusion Distance** $D_t^2(\mathbf{x}_i, \mathbf{x}_j)$ measures geometric proximity by comparing the conditional path distributions of random walks emanating from points $i$ and $j$:
$$D_t^2(\mathbf{x}_i, \mathbf{x}_j) = \|P_{i \cdot}^{(t)} - P_{j \cdot}^{(t)}\|_{L^2(1/\pi)}^2 = \sum_{k=1}^n \frac{(P_{ik}^{(t)} - P_{jk}^{(t)})^2}{\pi_k}$$
where $\pi_k = D_{kk} / \sum D_{jj}$ is the stationary distribution of the random walk.

*Spectral Embedding Theorem*: Let $\lambda_0 = 1 > \lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_{n-1}$ be the eigenvalues of $\mathbf{P}$ with right eigenvectors $\boldsymbol{\psi}_k$. The diffusion map $\boldsymbol{\Psi}_t: \mathbf{x}_i \mapsto (\lambda_1^t \psi_{1, i}, \lambda_2^t \psi_{2, i}, \dots, \lambda_d^t \psi_{d, i})^T$ embeds the manifold into $\mathbb{R}^d$ such that **Euclidean distance in the embedding space equals diffusion distance on the original manifold**:
$$\|\boldsymbol{\Psi}_t(\mathbf{x}_i) - \boldsymbol{\Psi}_t(\mathbf{x}_j)\|_2 = D_t(\mathbf{x}_i, \mathbf{x}_j) + O\left( \left(\frac{\lambda_{d+1}}{\lambda_1}\right)^t \right)$$
Diffusion maps eliminate noise and reveal intrinsic non-linear coordinates (such as developmental trajectories in single-cell genomics) with rigorous spectral guarantees.
"""

# -------------------------------------------------------------
# UNIT 3 DEEP
# -------------------------------------------------------------
u3_deep = r"""
## 3.9 Least Angle Regression (LARS) and the Full Lasso Path

In Unit 3.3, we used coordinate descent to solve the Lasso for a fixed tuning parameter $\lambda$. But in practical statistical modeling, how does one select the optimal $\lambda$, and how do the parameter estimates evolve as $\lambda$ sweeps continuously from $\infty$ down to $0$?

Bradley Efron, Trevor Hastie, Iain Johnstone, and Robert Tibshirani (2004) developed **Least Angle Regression (LARS)**, discovering that the Lasso coefficient path $\hat{\boldsymbol{\beta}}(\lambda)$ is a continuous, **piecewise linear** function of $\lambda$.

### 1. The Equiangular Path Geometry
Instead of taking tiny gradient steps, LARS exploits the geometry of least squares correlations:
1. Start with all coefficients $\boldsymbol{\beta} = \mathbf{0}$. Set current residual $\mathbf{r} = \mathbf{y}$.
2. Find the feature $\mathbf{x}_{j_1}$ most correlated with current residual $\mathbf{r}$: $j_1 = \arg\max_j |\mathbf{x}_j^T \mathbf{r}|$.
3. Move $\beta_{j_1}$ in the direction of its sign until another predictor $\mathbf{x}_{j_2}$ has as much correlation with the current residual as $\mathbf{x}_{j_1}$.
4. Instead of continuing along $\mathbf{x}_{j_1}$, LARS moves $\boldsymbol{\beta}$ along the **Equiangular Vector** $\mathbf{u}_A$ that makes an equal angle with both $\mathbf{x}_{j_1}$ and $\mathbf{x}_{j_2}$.
5. Continue along this joint equiangular ray until a third variable $\mathbf{x}_{j_3}$ catches up in correlation, and update the active set $A = \{j_1, j_2, j_3\}$.

### 2. The Lasso Modification to LARS
LARS is converted into exact Lasso by adding one simple rule:
*If a non-zero coefficient hits zero ($\beta_j \to 0$), drop variable $j$ from the active set $A$ and recompute the equiangular direction.*

Because the path between transition events is strictly linear, LARS computes the **entire continuous regularization path for all $\lambda \in [0, \infty)$** in the exact same computational time required for a single Ordinary Least Squares regression: $O(n p \min(n, p))$ operations.

## 3.10 High-Dimensional Logistic Regression: The Candès-Sur Phase Transition

In high-dimensional classification, statisticians fit logistic regression models $\log \frac{P(Y_i = 1)}{1 - P(Y_i = 1)} = \mathbf{x}_i^T \boldsymbol{\beta}$ with $n$ binary observations and $p$ features.
In classical statistics ($p$ fixed, $n \to \infty$), the Maximum Likelihood Estimator (MLE) always exists uniquely, is asymptotically unbiased, and its variance matches the inverse Fisher information $\mathbf{I}^{-1}(\boldsymbol{\beta})$.

Emmanuel Candès and Pragya Sur (2019) proved that in the high-dimensional regime where $p/n \to \kappa \in (0, 1)$, **classical logistic regression theory is completely false**.

### 1. The Separation Phase Transition
By Albert and Anderson's (1984) theorem, the logistic MLE exists if and only if the data points cannot be linearly separated by a hyperplane. 

*Theorem (Candès-Sur 2019)*: Let $\mathbf{x}_i \sim \mathcal{N}(\mathbf{0}, \mathbf{\Sigma})$ be independent Gaussian covariates. There exists a universal deterministic curve $h(\gamma_0)$ such that as $n, p \to \infty$ with $p/n \to \kappa$:
- If $\kappa < h(\gamma_0)$, the data are not linearly separable, and the MLE exists with probability approaching 1.0.
- If $\kappa > h(\gamma_0)$, the data are **linearly separable**, and the MLE **fails to exist** with probability approaching 1.0 (coefficients diverge to $\pm \infty$).
For symmetric labels ($P(Y=1) = 0.5$) with null features, the critical threshold is exactly $\kappa^* = 0.50$. In high dimensions, if $p > n/2$, unregularized logistic regression collapses due to separation!

### 2. Asymptotic Bias and Inflated Variance
Furthermore, Candès and Sur proved that even when the MLE exists ($\kappa < h(\gamma_0)$), the MLE is **asymptotically biased**:
$$\hat{\boldsymbol{\beta}}_{\text{MLE}} \approx \alpha_* \boldsymbol{\beta}^*$$
where the bias factor $\alpha_* > 1$ systematically inflates the true effect sizes, and the empirical standard error is significantly larger than predicted by the classical inverse Fisher information matrix. Unregularized logistic regression cannot be trusted in high dimensions; penalization via Lasso or Ridge is mandatory.
"""

# -------------------------------------------------------------
# UNIT 4 DEEP
# -------------------------------------------------------------
u4_deep = r"""
## 4.8 Alternating Direction Method of Multipliers (ADMM) for Distributed Optimization

In distributed statistical estimation, data are partitioned across $K$ worker nodes. Stephen Boyd et al. (2011) popularized the **Alternating Direction Method of Multipliers (ADMM)**, providing a mathematically robust framework for solving distributed convex optimization problems with consensus constraints.

### 1. The Global Consensus Problem
Consider solving the distributed empirical risk minimization problem across $K$ nodes:
$$\min_{\mathbf{w} \in \mathbb{R}^d} \sum_{k=1}^K f_k(\mathbf{w}) + g(\mathbf{w})$$
where $f_k(\mathbf{w})$ is the local loss function on worker $k$, and $g(\mathbf{w})$ is a global regularization term (such as the $L_1$ penalty $g(\mathbf{w}) = \lambda \|\mathbf{w}\|_1$).

We introduce local worker copies $\mathbf{w}_1, \dots, \mathbf{w}_K \in \mathbb{R}^d$ and an auxiliary master consensus variable $\mathbf{z} \in \mathbb{R}^d$, reformulating the objective as:
$$\min_{\{\mathbf{w}_k\}, \mathbf{z}} \sum_{k=1}^K f_k(\mathbf{w}_k) + g(\mathbf{z}) \quad \text{subject to} \quad \mathbf{w}_k - \mathbf{z} = \mathbf{0}, \quad k = 1, \dots, K$$

### 2. The Augmented Lagrangian and ADMM Updates
The augmented Lagrangian with penalty parameter $\rho > 0$ and dual multipliers $\mathbf{u}_k \in \mathbb{R}^d$ is:
$$\mathcal{L}_\rho(\{\mathbf{w}_k\}, \mathbf{z}, \{\mathbf{u}_k\}) = \sum_{k=1}^K \left[ f_k(\mathbf{w}_k) + \frac{\rho}{2} \|\mathbf{w}_k - \mathbf{z} + \mathbf{u}_k\|_2^2 \right] + g(\mathbf{z})$$

ADMM updates execute in three distributed stages:
1. **Parallel Worker Step**: Each worker $k \in \{1, \dots, K\}$ minimizes its local augmented loss independently:
$$\mathbf{w}_k^{(t+1)} = \arg\min_{\mathbf{w}} \left\{ f_k(\mathbf{w}) + \frac{\rho}{2} \|\mathbf{w} - \mathbf{z}^{(t)} + \mathbf{u}_k^{(t)}\|_2^2 \right\}$$
Worker updates require zero network communication and execute in parallel across nodes.
2. **Master Consensus Step**: The central coordinator gathers local vectors $\mathbf{w}_k^{(t+1)}$, computes the sample average $\bar{\mathbf{w}}^{(t+1)} = \frac{1}{K} \sum \mathbf{w}_k^{(t+1)}$, and solves the proximal step:
$$\mathbf{z}^{(t+1)} = \arg\min_{\mathbf{z}} \left\{ g(\mathbf{z}) + \frac{K \rho}{2} \|\mathbf{z} - \bar{\mathbf{w}}^{(t+1)} - \bar{\mathbf{u}}^{(t)}\|_2^2 \right\}$$
When $g(\mathbf{z}) = \lambda \|\mathbf{z}\|_1$, this update is computed in closed form using the soft-thresholding operator $\mathcal{S}(\cdot, \lambda / (K \rho))$.
3. **Dual Multiplier Update**: Each worker updates its dual variable:
$$\mathbf{u}_k^{(t+1)} = \mathbf{u}_k^{(t)} + \mathbf{w}_k^{(t+1)} - \mathbf{z}^{(t+1)}$$

ADMM converges to the exact global optimum under arbitrary data partitioning, handling non-smooth regularizers and ill-conditioned losses with guaranteed primal and dual residual decay.

## 4.9 The Parameter Server Architecture for Massive Sparse Models

When fitting modern deep recommendation systems, natural language embeddings, or massive search click-through-rate models, the parameter vector $\mathbf{w}$ contains billions of weights (e.g., $d \ge 10^{11}$, requiring terabytes of storage for parameters alone). In this regime, the parameter vector cannot fit into the memory of any single master coordinator node.

Mu Li et al. (2014) introduced the **Parameter Server** architecture:
- Nodes are partitioned into two groups: **Worker Nodes** (which store data shards and compute gradients) and **Server Nodes** (which partition and maintain the global parameter vector $\mathbf{w}$).
- The global parameter space is partitioned across server nodes using distributed consistent hashing.
- Workers transmit and receive parameters asynchronously using two primitives:
  - `Push(keys, gradients)`: Worker sends sparse gradients for the specific features present in its mini-batch to the designated server node.
  - `Pull(keys)`: Worker fetches the current parameter weights for its active mini-batch features.

By decoupling model storage from data processing and supporting bounded asynchronous updates (Stale Synchronous Parallelism - SSP), parameter servers scale statistical learning models to hundreds of billions of parameters across clusters of thousands of machines.
"""

def main():
    append_to_unit(1, u1_deep)
    append_to_unit(2, u2_deep)
    append_to_unit(3, u3_deep)
    append_to_unit(4, u4_deep)
    print("Units 1-4 deep pass 1 applied.")

if __name__ == "__main__":
    main()
