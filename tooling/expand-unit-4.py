# tooling/expand-unit-4.py
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "r", encoding="utf-8") as f:
    text = f.read()

addition = r"""

---

## 4.6 Recursive Matrix Updates: Givens Rotations, Cholesky Rank-One Modifiers, and Non-Negative Matrix Factorization

In statistical data streaming, sequential clinical trials, and recursive Bayesian filtering (Kalman filtering), observations arrive sequentially over time: $\mathbf{x}_{n+1}, \mathbf{x}_{n+2}, \dots$. If a statistical model must incorporate each newly arrived observation into an existing Ordinary Least Squares (OLS) fit, recomputing the QR decomposition or Cholesky factorization from scratch requires $\mathcal{O}(n p^2)$ operations per observation. For continuous data streams, this recalculation is computationally prohibitive.

To maintain real-time throughput, numerical statisticians deploy **rank-one updating and downdating algorithms**, which modify existing matrix factorizations in $\mathcal{O}(p^2)$ operations.

### Givens Plane Rotations and Recursive QR Updating

A **Givens Rotation** is an orthogonal matrix transformation $\mathbf{G}(i, k, \theta) \in \mathbb{R}^{m \times m}$ that rotates two coordinate axes in the $(i, k)$ coordinate plane by an angle $\theta$, selectively introducing a zero at position $(k, i)$ without disturbing any other rows or columns.

The matrix $\mathbf{G}(i, k, \theta)$ differs from the identity matrix $\mathbf{I}_m$ only at four intersection entries:
$$G_{ii} = c = \cos\theta, \quad G_{ik} = s = \sin\theta$$
$$G_{ki} = -s = -\sin\theta, \quad G_{kk} = c = \cos\theta$$

```text
Givens Rotation Matrix Structure:
            Row i       Row k
Row i [ ...   c   ...    s   ... ]
      [          ...             ]
Row k [ ...  -s   ...    c   ... ]
```

To eliminate the element $b$ in a 2-vector $\begin{bmatrix} a \\ b \end{bmatrix}$ such that:
$$\begin{bmatrix} c & s \\ -s & c \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} r \\ 0 \end{bmatrix}$$
the rotation coefficients are computed via the numerically stable formulas (avoiding intermediate overflow or underflow):
$$r = \text{sign}(a) \sqrt{a^2 + b^2}, \quad c = \frac{a}{r}, \quad s = \frac{b}{r}$$

#### Adding an Observation Row to QR:
Suppose an existing design matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ has factored QR form $\mathbf{X} = \mathbf{Q} \mathbf{R}$.
When a new observation vector $\mathbf{x}_{new} \in \mathbb{R}^p$ arrives, the augmented system is:
$$\tilde{\mathbf{X}} = \begin{bmatrix} \mathbf{R} \\ \mathbf{x}_{new}^\top \end{bmatrix} \in \mathbb{R}^{(p+1) \times p}$$
Notice that $\tilde{\mathbf{X}}$ is upper triangular except for the bottom row $\mathbf{x}_{new}^\top$.
By applying a sequence of $p$ successive Givens rotations $\mathbf{G}_1, \dots, \mathbf{G}_p$ between row $p+1$ and rows $1, \dots, p$:
- Rotation $\mathbf{G}_1$ eliminates the first element $x_{new, 1}$ using diagonal element $R_{11}$.
- Rotation $\mathbf{G}_2$ eliminates $x_{new, 2}$ using diagonal element $R_{22}$.
- In general, rotation $\mathbf{G}_k$ eliminates $x_{new, k}$ in $\mathcal{O}(p - k)$ FLOPs.

The total operation count to update the entire factorization is:
$$\text{FLOPs}_{update} = \sum_{k=1}^p 6 (p - k) \approx 3 p^2 \text{ FLOPs}$$
For $p = 50$, updating requires $\sim 7,500$ operations, compared to $2 n p^2 \approx 500,000,000$ operations for full re-factorization—a **speedup exceeding $60,000\times$**!

### Cholesky Rank-One Updating and Downdating

Let $\mathbf{C} = \mathbf{X}^\top \mathbf{X} = \mathbf{L} \mathbf{L}^\top$ be an existing Cholesky factorization.
When a new observation $\mathbf{x}$ arrives, the updated cross-product matrix is:
$$\mathbf{C}^* = \mathbf{C} + \mathbf{x} \mathbf{x}^\top = \mathbf{L} \mathbf{L}^\top + \mathbf{x} \mathbf{x}^\top$$
We seek an updated lower-triangular matrix $\mathbf{L}^*$ such that $\mathbf{C}^* = \mathbf{L}^* (\mathbf{L}^*)^\top$.

#### The Updating Recurrence (Gill, Murray, Saunders, 1974):
The update is computed by expressing the system in block matrix form:
$$\begin{bmatrix} \mathbf{L} & \mathbf{x} \end{bmatrix} \begin{bmatrix} \mathbf{L}^\top \\ \mathbf{x}^\top \end{bmatrix} = \mathbf{L} \mathbf{L}^\top + \mathbf{x} \mathbf{x}^\top$$
Applying a sequence of $p$ plane rotations eliminates the trailing vector $\mathbf{x}$, restoring triangular form in $\mathcal{O}(p^2)$ operations.

#### Cholesky Downdating:
Conversely, deleting an outlier or out-of-window observation requires **Cholesky Downdating**:
$$\mathbf{C}_{down} = \mathbf{L} \mathbf{L}^\top - \mathbf{x} \mathbf{x}^\top$$
Unlike updating (which is unconditionally stable because adding $\mathbf{x}\mathbf{x}^\top$ preserves positive definiteness), downdating is **numerically perilous**: if $\mathbf{x}$ is collinear with the existing basis, $\mathbf{C}_{down}$ can cease to be positive definite due to roundoff errors. Modern algorithms deploy hyperbolic rotations to monitor the remaining margin of positive definiteness.

### Non-Negative Matrix Factorization (NMF)

In many empirical disciplines—such as chemometrics, topic modeling, and gene expression profiling—data matrices $\mathbf{V} \in \mathbb{R}^{n \times p}$ represent strictly non-negative physical quantities (light intensities, word counts, chemical concentrations: $V_{ij} \ge 0$).

Standard SVD allows singular vectors to take arbitrary negative values, which lack biological or physical interpretability. To enforce physical realism, Daniel Lee and H. Sebastian Seung (1999) formulated **Non-Negative Matrix Factorization (NMF)**:

$$\mathbf{V} \approx \mathbf{W} \mathbf{H}, \quad \text{subject to } W_{ik} \ge 0, \, H_{kj} \ge 0$$

where $\mathbf{W} \in \mathbb{R}^{n \times k}$ represents the **basis matrix** (parts dictionary) and $\mathbf{H} \in \mathbb{R}^{k \times p}$ represents the **coefficient activation matrix** ($k \ll \min(n, p)$).

#### Objective Functions and Multiplicative Update Rules:
1. **Frobenius Divergence Objective**:
   $$\min_{\mathbf{W} \ge 0, \, \mathbf{H} \ge 0} \frac{1}{2} \|\mathbf{V} - \mathbf{W} \mathbf{H}\|_F^2 = \frac{1}{2} \sum_{i, j} (V_{ij} - (\mathbf{W}\mathbf{H})_{ij})^2$$
   Lee and Seung derived the elegant **multiplicative update rules**:
   $$H_{kj} \leftarrow H_{kj} \frac{(\mathbf{W}^\top \mathbf{V})_{kj}}{(\mathbf{W}^\top \mathbf{W} \mathbf{H})_{kj}}$$
   $$W_{ik} \leftarrow W_{ik} \frac{(\mathbf{V} \mathbf{H}^\top)_{ik}}{(\mathbf{W} \mathbf{H} \mathbf{H}^\top)_{ik}}$$

2. **Kullback–Leibler (I-Divergence) Objective**:
   $$\mathcal{D}_{KL}(\mathbf{V} \,\|\, \mathbf{W} \mathbf{H}) = \sum_{i, j} \left( V_{ij} \ln \frac{V_{ij}}{(\mathbf{W}\mathbf{H})_{ij}} - V_{ij} + (\mathbf{W}\mathbf{H})_{ij} \right)$$
   with multiplicative updates:
   $$H_{kj} \leftarrow H_{kj} \frac{\sum_i W_{ik} V_{ij} / (\mathbf{W}\mathbf{H})_{ij}}{\sum_i W_{ik}}$$
   $$W_{ik} \leftarrow W_{ik} \frac{\sum_j H_{kj} V_{ij} / (\mathbf{W}\mathbf{H})_{ij}}{\sum_j H_{kj}}$$

Because these multiplicative rules scale existing non-negative entries by non-negative quotients, non-negativity is preserved automatically without requiring constrained Lagrange multipliers or projection operators. NMF produces sparse, part-based representations where features combine purely additively.

---

## 4.7 Iterative Solvers and Randomized Linear Algebra: Conjugate Gradients and Randomized SVD

As datasets expand into millions of observations and tens of thousands of features, classical direct solvers ($\mathcal{O}(n p^2)$ or $\mathcal{O}(p^3)$) become computational bottlenecks. Modern statistical computing bridges numerical linear algebra and probability theory via **iterative Krylov subspace solvers** and **randomized matrix approximations**.

### The Method of Conjugate Gradients (CG)

For massive, sparse symmetric positive-definite (SPD) linear systems $\mathbf{A} \mathbf{x} = \mathbf{b}$ (such as penalized spline smoothing matrices or Gaussian Markov random field precision matrices), Magnus Hestenes and Eduard Stiefel (1952) developed the **Conjugate Gradient (CG)** method.

#### Theoretical Formulation:
Solving $\mathbf{A} \mathbf{x} = \mathbf{b}$ is mathematically equivalent to finding the global minimum of the strictly convex quadratic energy functional:

$$\phi(\mathbf{x}) = \frac{1}{2} \mathbf{x}^\top \mathbf{A} \mathbf{x} - \mathbf{b}^\top \mathbf{x}$$

Instead of searching along the steepest descent gradient directions (which oscillate in narrow ill-conditioned valleys), the CG algorithm searches along mutually **$\mathbf{A}$-conjugate (orthogonal)** search directions:

$$\mathbf{p}_i^\top \mathbf{A} \mathbf{p}_j = 0 \quad \text{for all } i \ne j$$

#### Algorithmic Recurrence:
Starting from initial guess $\mathbf{x}_0$ (typically $\mathbf{x}_0 = \mathbf{0}$):
- Initial residual: $\mathbf{r}_0 = \mathbf{b} - \mathbf{A} \mathbf{x}_0$. Initial direction: $\mathbf{p}_0 = \mathbf{r}_0$.
- At step $k$:
  $$\alpha_k = \frac{\mathbf{r}_k^\top \mathbf{r}_k}{\mathbf{p}_k^\top \mathbf{A} \mathbf{p}_k}$$
  $$\mathbf{x}_{k+1} = \mathbf{x}_k + \alpha_k \mathbf{p}_k$$
  $$\mathbf{r}_{k+1} = \mathbf{r}_k - \alpha_k \mathbf{A} \mathbf{p}_k$$
  $$\beta_k = \frac{\mathbf{r}_{k+1}^\top \mathbf{r}_{k+1}}{\mathbf{r}_k^\top \mathbf{r}_k}$$
  $$\mathbf{p}_{k+1} = \mathbf{r}_{k+1} + \beta_k \mathbf{p}_k$$

#### Convergence Rate and Preconditioning:
In exact arithmetic, CG terminates in at most $p$ iterations. In floating-point arithmetic, the error after $k$ iterations is bounded by the condition number $\kappa = \kappa_2(\mathbf{A})$:

$$\|\mathbf{x}_k - \mathbf{x}^*\|_{\mathbf{A}} \le 2 \left( \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1} \right)^k \|\mathbf{x}_0 - \mathbf{x}^*\|_{\mathbf{A}}$$

To accelerate convergence, **Preconditioned Conjugate Gradient (PCG)** applies an invertible preconditioner $\mathbf{M} \approx \mathbf{A}$ such that $\mathbf{M}^{-1} \mathbf{A} \approx \mathbf{I}$, collapsing the condition number to near 1. Common statistical preconditioners include Jacobi diagonal scaling and Incomplete Cholesky factorizations.

### Randomized Singular Value Decomposition (Randomized SVD)

In 2011, Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp synthesized randomized sketching theory into the **Randomized SVD** algorithm. For massive matrices where $p$ is large but the effective statistical rank $k$ is small ($k \ll p$), randomized SVD computes near-optimal low-rank factorizations in $\mathcal{O}(n p \log k)$ operations instead of $\mathcal{O}(n p^2)$ deterministic operations.

```text
Randomized SVD Pipeline:
  [ High-Dim Matrix X (n x p) ] x [ Gaussian Sketch Omega (p x (k+s)) ]
                                |
                                v
               [ Sample Matrix Y = X Omega (n x (k+s)) ]
                                |
                   (Orthonormalize via QR: Y = Q R)
                                v
                [ Orthonormal Basis Q (n x (k+s)) ]
                                |
                   (Project: B = Q^T X ((k+s) x p))
                                v
                [ Small Matrix B ((k+s) x p) ]
                                |
                   (Small Deterministic SVD: B = \tilde{U} \Sigma V^T)
                                v
               [ Final SVD: U = Q \tilde{U}, \Sigma, V^T ]
```

#### The Two-Stage Algorithmic Protocol:
1. **Stage A: Randomized Subspace Identification**:
   - Draw an independent Gaussian random test matrix $\boldsymbol{\Omega} \in \mathbb{R}^{p \times (k + s)}$, where $s$ is a small oversampling parameter (typically $s = 5$ or $10$). Each entry $\Omega_{ij} \sim \mathcal{N}(0, 1)$.
   - Form the sketch sample matrix:
     $$\mathbf{Y} = \mathbf{X} \boldsymbol{\Omega} \in \mathbb{R}^{n \times (k + s)}$$
   - Orthonormalize the columns of $\mathbf{Y}$ via QR decomposition to construct an orthonormal basis $\mathbf{Q} \in \mathbb{R}^{n \times (k + s)}$:
     $$\mathbf{Y} = \mathbf{Q} \mathbf{R}$$
   - The subspace spanned by the columns of $\mathbf{Q}$ captures the dominant action of $\mathbf{X}$ with probability exceeding $1 - 10^{-s}$.

2. **Stage B: Low-Dimensional Deterministic Decomposition**:
   - Project $\mathbf{X}$ onto the low-dimensional subspace:
     $$\mathbf{B} = \mathbf{Q}^\top \mathbf{X} \in \mathbb{R}^{(k + s) \times p}$$
   - Compute the classical deterministic SVD of the small matrix $\mathbf{B}$:
     $$\mathbf{B} = \tilde{\mathbf{U}} \boldsymbol{\Sigma} \mathbf{V}^\top$$
   - Reconstruct the left singular vectors of $\mathbf{X}$:
     $$\mathbf{U} = \mathbf{Q} \tilde{\mathbf{U}}$$
   - Truncate to the top $k$ components.

Randomized SVD operates by making only **two passes over the massive data matrix $\mathbf{X}$**, making it the premier algorithm for streaming data, out-of-core memory-mapped arrays, and distributed cloud computing engines (Apache Spark).
"""

marker = "## Fully worked question 1:"
idx = text.find(marker)
new_text = text[:idx] + addition.strip() + "\n\n" + text[idx:]

with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated Unit 4 successfully!")
