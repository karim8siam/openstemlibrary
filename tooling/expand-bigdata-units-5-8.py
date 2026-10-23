#!/usr/bin/env python3
"""
Expansion script for Units 5 to 8 of Big Data Methods for Statistics (Book 16).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} expanded.")

# -------------------------------------------------------------
# UNIT 5 EXPANSION
# -------------------------------------------------------------
u5_exp = r"""
## 5.5 Variance-Reduced Stochastic Gradient Descent: SVRG and SAGA

In Section 5.1, we noted that standard SGD with a fixed learning rate cannot converge to the exact minimum: because the variance of the stochastic gradient $\mathbb{E}[\|\nabla f_i(\mathbf{w}) - \nabla F(\mathbf{w})\|_2^2] = \sigma^2$ remains strictly positive even at the optimum $\mathbf{w}^*$ (where $\nabla F(\mathbf{w}^*) = \mathbf{0}$, but individual gradients $\nabla f_i(\mathbf{w}^*) \ne \mathbf{0}$), SGD requires a decaying learning rate $\eta_t \propto 1/t$, slowing convergence to a sublinear rate $O(1/t)$.

Rie Johnson and Tong Zhang (2013) developed **Stochastic Variance Reduced Gradient (SVRG)**, while Aaron Defazio et al. (2014) introduced **SAGA**, achieving **linear convergence rates** ($O(\rho^k)$ with $\rho < 1$) on strongly convex finite-sum problems.

### 1. The SVRG Algorithm
SVRG operates in two nested loops: an outer epoch loop and an inner stochastic loop:
1. **Outer Loop (Epoch)**: At epoch $s$, evaluate and store the exact full gradient at snapshot point $\tilde{\mathbf{w}}_{s-1}$:
$$\tilde{\boldsymbol{\mu}} = \nabla F(\tilde{\mathbf{w}}_{s-1}) = \frac{1}{n} \sum_{i=1}^n \nabla f_i(\tilde{\mathbf{w}}_{s-1})$$
2. **Inner Loop (Stochastic Steps)**: Initialize $\mathbf{w}_0 = \tilde{\mathbf{w}}_{s-1}$. For $t = 1, \dots, m$ (typically $m = 2n$):
   - Sample index $i_t \in \{1, \dots, n\}$ uniformly at random.
   - Construct the **variance-reduced stochastic gradient**:
$$\mathbf{v}_t = \nabla f_{i_t}(\mathbf{w}_{t-1}) - \nabla f_{i_t}(\tilde{\mathbf{w}}_{s-1}) + \tilde{\boldsymbol{\mu}}$$
   - Update parameters: $\mathbf{w}_t = \mathbf{w}_{t-1} - \eta \mathbf{v}_t$.
3. Set snapshot $\tilde{\mathbf{w}}_s = \mathbf{w}_m$ (or the average of inner iterates).

### 2. The Variance Reduction Mechanism
Verify the expectation of $\mathbf{v}_t$:
$$\mathbb{E}[\mathbf{v}_t \mid \mathbf{w}_{t-1}] = \frac{1}{n} \sum_{i=1}^n \nabla f_i(\mathbf{w}_{t-1}) - \frac{1}{n} \sum_{i=1}^n \nabla f_i(\tilde{\mathbf{w}}_{s-1}) + \tilde{\boldsymbol{\mu}} = \nabla F(\mathbf{w}_{t-1}) - \tilde{\boldsymbol{\mu}} + \tilde{\boldsymbol{\mu}} = \nabla F(\mathbf{w}_{t-1})$$
The estimator is strictly unbiased.

Now consider the variance: as the algorithm approaches the optimum ($\mathbf{w}_{t-1} \to \mathbf{w}^*$ and $\tilde{\mathbf{w}} \to \mathbf{w}^*$):
$$\lim_{\mathbf{w}_{t-1}, \tilde{\mathbf{w}} \to \mathbf{w}^*} \|\nabla f_{i_t}(\mathbf{w}_{t-1}) - \nabla f_{i_t}(\tilde{\mathbf{w}})\| = 0$$
Unlike standard SGD, **the variance of the stochastic gradient decays automatically to zero** as iterates approach the optimum! Consequently, SVRG can use a large, fixed learning rate $\eta$, achieving geometric linear convergence $\mathcal{O}(e^{-c t})$ with the per-step cost of SGD.

## 5.6 Asynchronous Lock-Free Optimization: The Hogwild! Algorithm

When scaling stochastic optimization across multi-core CPUs with shared memory, classical concurrent programming requires thread synchronization: when thread $A$ updates weight vector $\mathbf{w}$, it acquires a memory lock (mutex), forcing all other threads to stall. In massive models, lock contention consumes $95\%$ of CPU cycles.

Feng Niu, Benjamin Recht, Christopher Ré, and Stephen J. Wright (2011) introduced **Hogwild!**, proving that threads can read and write shared memory asynchronously **without locks or memory fences**.

### Theoretical Foundation of Hogwild!
In many high-dimensional problems (such as text classification, sparse collaborative filtering, and large graph embeddings), each training instance $\mathbf{x}_i$ is extremely sparse: out of $d = 10^7$ features, instance $i$ has non-zero entries in only a tiny subset of coordinates $\mathcal{V}_i \subset \{1, \dots, d\}$, where $|\mathcal{V}_i| \ll d$.

*Theorem (Niu et al. 2011)*: Let $\Omega = \max_{j} |\{ i : j \in \mathcal{V}_i \}|$ measure the sparsity conflict graph (the maximum degree of feature overlap). If $\Omega \ll d$, then almost all concurrent thread updates touch disjoint coordinates of the parameter vector $\mathbf{w}$.

Even when two threads occasionally overwrite the same memory word simultaneously (causing an atomic memory race condition), the perturbation acts as a small, zero-mean noise term that is absorbed by the intrinsic stochasticity of SGD. Hogwild! achieves near-linear speedups ($k$-fold speedup across $k$ CPU cores) with zero synchronization overhead.
"""

# -------------------------------------------------------------
# UNIT 6 EXPANSION
# -------------------------------------------------------------
u6_exp = r"""
## 6.5 The Nyström Method for Large-Scale Kernel Machines

In non-parametric regression and support vector machines (SVMs), non-linear relationships are captured via positive semi-definite kernel matrices:
$$\mathbf{K} \in \mathbb{R}^{n \times n}, \quad K_{ij} = k(\mathbf{x}_i, \mathbf{x}_j)$$
where $k(\cdot, \cdot)$ is a Mercer kernel (such as the Gaussian Radial Basis Function $k(\mathbf{x}, \mathbf{y}) = \exp(-\gamma \|\mathbf{x} - \mathbf{y}\|_2^2)$).

Kernel ridge regression requires inverting the $n \times n$ kernel matrix:
$$\hat{\boldsymbol{\alpha}} = (\mathbf{K} + \lambda \mathbf{I}_n)^{-1} \mathbf{y}$$
When $n = 100,000$, storing the $n \times n$ matrix requires $80$ Gigabytes of memory, and inverting it takes $O(n^3) \approx 10^{15}$ operations (days of computation).

E. J. Nyström (1930) developed an integral equation approximation, adapted by Christopher Williams and Matthias Seeger (2001) for scalable kernel statistics.

### Algorithmic Mechanics of the Nyström Method
Instead of computing all $n^2$ entries of $\mathbf{K}$, the Nyström method samples a small subset of $m \ll n$ landmark columns (typically $m \approx 500$ to $2,000$):
1. Partition the rows and columns of $\mathbf{K}$ into the $m$ sampled landmarks and the $n - m$ remaining points:
$$\mathbf{K} = \begin{pmatrix} \mathbf{K}_{mm} & \mathbf{K}_{nm - m}^T \\ \mathbf{K}_{nm - m} & \mathbf{K}_{nn - m} \end{pmatrix} = \begin{pmatrix} \mathbf{W} & \mathbf{K}_{21}^T \\ \mathbf{K}_{21} & \mathbf{K}_{22} \end{pmatrix}$$
where $\mathbf{W} \in \mathbb{R}^{m \times m}$ is the kernel matrix between landmarks, and $\mathbf{C} = \begin{pmatrix} \mathbf{W} \\ \mathbf{K}_{21} \end{pmatrix} \in \mathbb{R}^{n \times m}$ is the column sub-matrix.
2. The Nyström low-rank approximation of the entire $n \times n$ kernel matrix is:
$$\tilde{\mathbf{K}} = \mathbf{C} \mathbf{W}^\dagger \mathbf{C}^T$$
where $\mathbf{W}^\dagger$ is the Moore-Penrose pseudoinverse.

### Computational and Memory Savings
- **Memory**: We only store $\mathbf{C} \in \mathbb{R}^{n \times m}$, reducing memory from $O(n^2)$ to $O(n m)$. For $n = 100,000$ and $m = 1,000$, memory drops from $80$ GB to $800$ MB!
- **Inversion via Woodbury Identity**: Applying the Sherman-Morrison-Woodbury formula:
$$(\tilde{\mathbf{K}} + \lambda \mathbf{I}_n)^{-1} = \frac{1}{\lambda} \left[ \mathbf{I}_n - \mathbf{C} (\lambda \mathbf{W} + \mathbf{C}^T \mathbf{C})^{-1} \mathbf{C}^T \right]$$
The matrix to invert is $(\lambda \mathbf{W} + \mathbf{C}^T \mathbf{C})$, which is of dimension $m \times m$.
Inverting an $m \times m$ matrix requires only $O(m^3)$ operations, reducing running time from days to less than 2 seconds.

## 6.6 Fast Randomized Least Squares: Blendenpik and LSRN

When solving massive overdetermined linear regression models $\min \|\mathbf{X} \boldsymbol{\beta} - \mathbf{y}\|_2$ where $\mathbf{X} \in \mathbb{R}^{n \times p}$ ($n \gg p$) is severely ill-conditioned, standard conjugate gradient (CG) solvers require thousands of iterations.

Avron, Maymounkov, and Toledo (2010) created **Blendenpik**, while Meng, Saunders, and Mahoney (2014) developed **LSRN**, using random projections as optimal pre-conditioners.

### The Blendenpik Preconditioning Workflow
1. **Sketching**: Generate a Subsampled Randomized Hadamard Transform (SRHT) matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times n}$ with sketch size $k \approx 4 p$.
2. **Sketched QR Factorization**: Compute the sketched matrix $\tilde{\mathbf{X}} = \mathbf{\Pi} \mathbf{X} \in \mathbb{R}^{k \times p}$ in $O(n p \log k)$ time, and perform standard QR factorization:
$$\tilde{\mathbf{X}} = \mathbf{Q}_1 \mathbf{R}$$
where $\mathbf{R} \in \mathbb{R}^{p \times p}$ is upper-triangular.
3. **Preconditioned Iterative Solve**: Use $\mathbf{R}^{-1}$ as a right-preconditioner:
$$\min_{\boldsymbol{\gamma}} \|(\mathbf{X} \mathbf{R}^{-1}) \boldsymbol{\gamma} - \mathbf{y}\|_2, \quad \text{where } \boldsymbol{\beta} = \mathbf{R}^{-1} \boldsymbol{\gamma}$$

*Theorem (Avron et al. 2010)*: The condition number of the preconditioned matrix satisfies:
$$\kappa(\mathbf{X} \mathbf{R}^{-1}) \le \sqrt{\frac{1 + \epsilon}{1 - \epsilon}} \approx 1.0$$
Regardless of how horribly ill-conditioned the original matrix was ($\kappa(\mathbf{X}) \ge 10^{12}$), the preconditioned matrix has condition number near $1.0$. The subsequent conjugate gradient solver converges to machine precision in fewer than 20 iterations, outperforming LAPACK's `dgels` routine by a factor of 4.
"""

# -------------------------------------------------------------
# UNIT 7 EXPANSION
# -------------------------------------------------------------
u7_exp = r"""
## 7.6 Frequency Moment Estimation: The Alon-Matias-Szegedy (AMS) Sketch

In network traffic analysis and database query optimization, streaming algorithms must estimate the frequency moments of a data stream:
$$F_k = \sum_{i=1}^m f_i^k$$
where $f_i$ is the total frequency of item $i$:
- $F_0$: the number of distinct elements (cardinality).
- $F_1$: the total stream length $\sum f_i = N$.
- $F_2 = \sum f_i^2$: the **Second Frequency Moment** (also called the **Gini-Simpson diversity index** or **self-join size**). $F_2$ measures the degree of data skewness and collision concentration.

Noga Alon, Yossi Matias, and Mario Szegedy (1996) formulated the **AMS Sketch**, which won the Gödel Prize for proving that $F_2$ can be estimated in $O(\log(1/\delta) / \epsilon^2)$ space.

### Algorithmic Construction of the AMS Sketch
1. Construct a hash function $h: \mathcal{U} \to \{-1, +1\}$ chosen uniformly from a family of 4-wise independent hash functions.
2. Maintain a single scalar accumulator $X$, initialized to $0$.
3. When stream element $a_t$ arrives:
$$X \leftarrow X + h(a_t)$$
4. Compute the basic estimator:
$$Y = X^2$$

### Proof of Unbiasedness and Variance
Notice that after observing the entire stream:
$$X = \sum_{i=1}^m f_i h(i)$$
Evaluate the expectation of $Y = X^2$:
$$\mathbb{E}[Y] = \mathbb{E}[X^2] = \mathbb{E}\left[ \left( \sum_{i=1}^m f_i h(i) \right)^2 \right] = \sum_{i=1}^m f_i^2 \mathbb{E}[h(i)^2] + \sum_{i \ne j} f_i f_j \mathbb{E}[h(i) h(j)]$$
Because $h(i) \in \{-1, +1\}$, $h(i)^2 = 1.0$. By 2-wise independence, $\mathbb{E}[h(i) h(j)] = \mathbb{E}[h(i)] \mathbb{E}[h(j)] = 0$. Therefore:
$$\mathbb{E}[Y] = \sum_{i=1}^m f_i^2 = F_2$$
The basic AMS sketch is strictly unbiased!

Using 4-wise independence, the variance satisfies $\mathrm{Var}(Y) \le 2 F_2^2$. By averaging $k = O(1/\epsilon^2)$ independent copies and taking the median of medians, the AMS sketch guarantees that $\hat{F}_2 \in (1 \pm \epsilon) F_2$ with probability $1 - \delta$ using logarithmic memory.

## 7.7 Streaming Quantiles: The $t$-Digest Algorithm

While the mean and variance can be maintained in $O(1)$ space using Welford's algorithm, maintaining accurate extreme quantiles (such as the 99th, 99.9th, or 99.99th percentiles for server latency Service Level Agreements - SLAs) in a streaming environment is notoriously difficult.

Ted Dunning and Otmar Ertl (2019) introduced the **$t$-Digest**, a compact probabilistic data structure that provides sub-percentile accuracy for extreme tail percentiles while supporting real-time streaming updates and distributed merging.

### Structural Mechanics of $t$-Digest
A $t$-digest clusters incoming continuous observations into a collection of $K$ variable-sized centroids $C_j = (m_j, w_j)$, where $m_j$ is the centroid mean and $w_j$ is the centroid weight (the number of observations assigned to it).

Crucially, the maximum allowed weight of centroid $j$ is governed by a non-linear scale function $q \mapsto k(q, \delta)$:
$$w_j \le 4 N \frac{\sqrt{q(1 - q)}}{\delta}$$
where $q \in [0, 1]$ is the empirical quantile rank of centroid $j$, and $\delta$ is the compression parameter (typically $\delta \approx 100$ to $500$).

- Near the median ($q \approx 0.5$): $\sqrt{q(1 - q)} = 0.5$ is large, allowing centroids to merge and accumulate large weights.
- Near the extreme tails ($q \to 0$ or $q \to 1$): $\sqrt{q(1 - q)} \to 0$, forcing centroid weights to be tiny ($w_j \approx 1$).
Centroids near the tails are razor-sharp individual points, guaranteeing that the 99.9th percentile is estimated with relative error below $0.01\%$ using less than 10 Kilobytes of memory.
"""

# -------------------------------------------------------------
# UNIT 8 EXPANSION
# -------------------------------------------------------------
u8_exp = r"""
## 8.6 Exact High-Dimensional FDR Control: The Knockoffs Framework

In high-dimensional sparse regression $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$, the Benjamini-Hochberg procedure cannot be applied directly to individual regression $p$-values: the columns of $\mathbf{X}$ are mutually correlated, which causes the single-feature $p$-values to be intensely dependent, violating independence assumptions.

Rina Foygel Barber and Emmanuel Candès (2015), along with Candès et al. (2018), revolutionized high-dimensional variable selection by inventing the **Knockoffs Framework**. Knockoffs control the False Discovery Rate **exactly in finite samples** without relying on asymptotic approximations or making any assumptions about the sparsity of the true coefficients.

### 1. Model-X Knockoffs Construction
Let $\mathbf{x} = (X_1, \dots, X_p)^T$ be the random vector of covariates.
A knockoff vector $\tilde{\mathbf{x}} = (\tilde{X}_1, \dots, \tilde{X}_p)^T$ is an artificially generated synthetic feature vector satisfying two conditions:
1. **Swap Invariance**: For any subset of indices $S \subseteq \{1, \dots, p\}$, swapping the true features $X_j$ with their knockoffs $\tilde{X}_j$ for all $j \in S$ leaves the joint distribution unchanged:
$$[\mathbf{x}, \tilde{\mathbf{x}}]_{\text{swap}(S)} \stackrel{d}{=} [\mathbf{x}, \tilde{\mathbf{x}}]$$
2. **Conditional Independence from Response**: Knockoffs are generated without ever looking at the response variable $\mathbf{y}$:
$$\tilde{\mathbf{x}} \perp \mathbf{y} \mid \mathbf{x}$$

For Gaussian covariates $\mathbf{x} \sim \mathcal{N}(\mathbf{0}, \mathbf{\Sigma})$, knockoffs are generated as:
$$\tilde{\mathbf{x}} \mid \mathbf{x} \sim \mathcal{N}\left( \mathbf{x} - \mathbf{D} \mathbf{\Sigma}^{-1} \mathbf{x}, 2 \mathbf{D} - \mathbf{D} \mathbf{\Sigma}^{-1} \mathbf{D} \right)$$
where $\mathbf{D}$ is a positive diagonal matrix chosen such that $2 \mathbf{\Sigma} - \mathbf{D} \succeq \mathbf{0}$.

### 2. Feature Statistics and the Knockoff Filter
Fit a sparse learning algorithm (such as cross-validated Lasso) on the augmented feature matrix $[\mathbf{X}, \tilde{\mathbf{X}}]$ of dimension $n \times 2p$.
For each variable $j \in \{1, \dots, p\}$, define a **Feature Statistic** $W_j$ comparing the strength of original variable $j$ against its synthetic knockoff $\tilde{j}$:
$$W_j = f(Z_j, \tilde{Z}_j)$$
where $W_j > 0$ indicates that the real feature entered the model before its knockoff, while $W_j < 0$ indicates that the knockoff appeared stronger.
A canonical example is the Lasso signed maximum lambda:
$$W_j = \max(Z_j, \tilde{Z}_j) \times \mathrm{sign}(Z_j - \tilde{Z}_j)$$

By the swap invariance property, if variable $j$ is a true null ($\beta_j^* = 0$), the sign of $W_j$ is an independent, fair coin flip:
$$P(W_j > 0) = P(W_j < 0) = 0.5$$

### 3. The Knockoff+ Threshold
Sort the absolute values $|W_j|$. The data-dependent selection threshold is:
$$T = \min \left\{ t > 0 : \frac{1 + \#\{ j : W_j \le -t \}}{\max(1, \#\{ j : W_j \ge t \})} \le q^* \right\}$$
The selected set of discoveries is $\hat{S} = \{ j : W_j \ge T \}$.

*Theorem (Barber and Candès 2015)*: For any linear or non-linear regression model with arbitrary unknown signal magnitude, the Knockoff+ procedure guarantees exact finite-sample FDR control:
$$\mathbb{E}\left[ \frac{|\hat{S} \cap \{j : \beta_j^* = 0\}|}{\max(1, |\hat{S}|)} \right] \le q^*$$
Knockoffs eliminate the reliance on heuristic variable selection thresholds, providing a mathematically airtight shield against false scientific discoveries in high dimensions.
"""

def main():
    append_to_unit(5, u5_exp)
    append_to_unit(6, u6_exp)
    append_to_unit(7, u7_exp)
    append_to_unit(8, u8_exp)
    print("Units 5-8 expanded.")

if __name__ == "__main__":
    main()
