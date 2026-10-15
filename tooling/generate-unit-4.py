# tooling/generate-unit-4.py
import os

out_path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

unit4_text = r"""# Unit 4: Numerical Linear Algebra, Floating-Point Arithmetic, QR/SVD Decompositions, and Matrix Computations

## 4.1 IEEE 754 Floating-Point Arithmetic, Machine Precision, and Condition Numbers

In theoretical statistics, algebraic equations are formulated under the assumption of exact real arithmetic over the continuum of real numbers $\mathbb{R}$. In statistical computing, however, calculations are executed on digital computers with finite memory and finite register widths. Every continuous real number is mapped into a discrete, finite set of binary representations governed by the **IEEE 754 Floating-Point Standard**.

Failure to appreciate the discrete topology of floating-point arithmetic can introduce catastrophic truncation errors, loss of mathematical significance, and algorithm divergence into otherwise sound statistical estimators.

### The IEEE 754 Binary Representation Architecture

Under the IEEE 754 standard (revised in 2008 and 2019), a binary floating-point number $x$ is partitioned into three discrete bitfields:
1. A **Sign bit ($s \in \{0, 1\}$)**: Encodes positive ($s = 0$) or negative ($s = 1$).
2. A **Biased Exponent ($e$)**: An unsigned integer stored with a fixed bias $B$.
3. A **Significand / Mantissa ($m$)**: A fractional binary sequence representing the precision bits.

The numerical value represented by the bit pattern is given by:

$$x = (-1)^s \times 2^{e - B} \times \left( 1 + \sum_{j=1}^p b_j 2^{-j} \right) = (-1)^s \times 2^{e - B} \times (1.m)_2$$

where the leading $1$ is an implicit (hidden) bit not physically stored in memory, granting an additional bit of precision for normalized numbers.

```text
IEEE 754 64-Bit Double-Precision Layout:
+---+----------------------+----------------------------------------------------+
| s | Exponent e (11 bits) | Fraction / Significand m (52 bits)                 |
+---+----------------------+----------------------------------------------------+
  1           11                                     52
```

#### Binary Layout Parameters Across Standard Precisions:
- **Single Precision (`binary32` / `float32`)**:
  - Total bits: 32 (1 sign bit, 8 exponent bits, 23 fraction bits).
  - Exponent bias: $B = 2^{8-1} - 1 = 127$.
  - Precision: $p = 23 + 1 = 24$ bits of significand ($\approx 7.22$ decimal digits).
  - Dynamic range: $\approx 1.18 \times 10^{-38}$ to $3.40 \times 10^{38}$.
- **Double Precision (`binary64` / `float64`)**:
  - Total bits: 64 (1 sign bit, 11 exponent bits, 52 fraction bits).
  - Exponent bias: $B = 2^{11-1} - 1 = 1023$.
  - Precision: $p = 52 + 1 = 53$ bits of significand ($\approx 15.95$ decimal digits).
  - Dynamic range: $\approx 2.23 \times 10^{-308}$ to $1.80 \times 10^{308}$.

### Machine Epsilon and the Unit in the Last Place (ULP)

The discrete nature of floating-point numbers implies that the real line is represented as a non-uniform lattice. The spacing between consecutive representable numbers is quantified by the **Unit in the Last Place (ULP)**:

$$\text{ulp}(x) = 2^{e - B - p + 1}$$

Between $1.0$ and $2.0$, the exponent is $e - B = 0$. The gap between $1.0$ and the very next representable floating-point number is defined as the **Machine Epsilon ($\epsilon_{mach}$)**:

$$\epsilon_{mach} = \text{ulp}(1.0) = 2^{-(p - 1)}$$

- In IEEE 754 double precision ($p = 53$):
  $$\epsilon_{mach} = 2^{-52} \approx 2.220446 \times 10^{-16}$$
- In single precision ($p = 24$):
  $$\epsilon_{mach} = 2^{-23} \approx 1.192093 \times 10^{-7}$$

The standard rounding rule (Round to Nearest, Ties to Even) guarantees that for any real number $x$ within the normalized range, its floating-point representation $\text{fl}(x)$ satisfies:

$$\text{fl}(x) = x (1 + \delta), \quad |\delta| \le u = \frac{1}{2} \epsilon_{mach} = 2^{-p}$$

where $u = 2^{-53} \approx 1.11 \times 10^{-16}$ is the **unit roundoff**.

### Special Encodings: Subnormals, Infinities, and NaNs

The IEEE 754 standard reserves specific exponent bit patterns to handle boundary conditions gracefully without crashing the hardware:
1. **Subnormal (Denormalized) Numbers ($e = 0, m \ne 0$)**:
   When the biased exponent is all zeros ($e = 0$), the implicit leading bit becomes $0$ instead of $1$:
   $$x = (-1)^s \times 2^{1 - B} \times (0.m)_2$$
   Subnormals provide **gradual underflow**, allowing computations to continue below $2^{-1022} \approx 2.23 \times 10^{-308}$ down to $2^{-1074} \approx 4.94 \times 10^{-324}$ at the expense of reduced significant bits.
2. **Signed Zeros ($e = 0, m = 0$)**:
   Distinguishes $+0.0$ and $-0.0$, preserving branch cut directions in complex analysis and directional limits (e.g. $1 / (+0.0) = +\infty$ while $1 / (-0.0) = -\infty$).
3. **Infinities ($e = \text{all 1s}, m = 0$)**:
   Represent mathematical overflow ($+\infty$ and $-\infty$).
4. **Not-a-Number (NaN) ($e = \text{all 1s}, m \ne 0$)**:
   Represents mathematically invalid operations (such as $0 / 0$, $\infty - \infty$, or $\sqrt{-1}$ over reals). 
   - **Quiet NaN ($qNaN$)**: Propagates through arithmetic expressions without triggering hardware interrupts.
   - **Signaling NaN ($sNaN$)**: Triggers an immediate floating-point exception trap when accessed.

### Condition Numbers of Linear Systems and Operations

In numerical analysis, it is essential to distinguish between the **stability of an algorithm** and the **conditioning of a mathematical problem**.
- A problem is **ill-conditioned** if a tiny perturbation in the input data produces a massive perturbation in the exact mathematical solution.
- An algorithm is **numerically unstable** if it introduces roundoff errors that amplify during execution, producing an inaccurate solution even on a well-conditioned problem.

#### The Condition Number of a Matrix
Consider solving the linear system $\mathbf{A} \mathbf{x} = \mathbf{b}$, where $\mathbf{A} \in \mathbb{R}^{n \times n}$ is non-singular. Perturbing the right-hand side vector by $\delta \mathbf{b}$ induces a perturbation $\delta \mathbf{x}$ in the solution:

$$\mathbf{A} (\mathbf{x} + \delta \mathbf{x}) = \mathbf{b} + \delta \mathbf{b} \implies \mathbf{A} \, \delta \mathbf{x} = \delta \mathbf{b} \implies \delta \mathbf{x} = \mathbf{A}^{-1} \, \delta \mathbf{b}$$

Taking matrix and vector norms:
$$\|\delta \mathbf{x}\| \le \|\mathbf{A}^{-1}\| \|\delta \mathbf{b}\|$$
$$\|\mathbf{b}\| = \|\mathbf{A} \mathbf{x}\| \le \|\mathbf{A}\| \|\mathbf{x}\| \implies \frac{1}{\|\mathbf{x}\|} \le \frac{\|\mathbf{A}\|}{\|\mathbf{b}\|}$$

Multiplying the inequalities yields the relative error bound:

$$\frac{\|\delta \mathbf{x}\|}{\|\mathbf{x}\|} \le \|\mathbf{A}\| \|\mathbf{A}^{-1}\| \frac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|}$$

The quantity $\kappa(\mathbf{A}) = \|\mathbf{A}\| \|\mathbf{A}^{-1}\|$ is the **Condition Number** of matrix $\mathbf{A}$.
In the standard Euclidean 2-norm ($L_2$ norm), the condition number is the ratio of the largest to smallest singular values of $\mathbf{A}$:

$$\kappa_2(\mathbf{A}) = \frac{\sigma_{max}(\mathbf{A})}{\sigma_{min}(\mathbf{A})}$$

**Rule of Thumb for Numerical Precision**:
If $\kappa_{10}(\mathbf{A}) \approx 10^k$, solving the linear system $\mathbf{A} \mathbf{x} = \mathbf{b}$ in 64-bit double precision (which provides $\sim 16$ decimal digits) can lose up to $k$ digits of accuracy. If $\kappa(\mathbf{A}) \ge 10^{16}$, the matrix is numerically singular, and the computed solution contains zero significant digits!

---

## 4.2 Catastrophic Cancellation in Sample Variance: Naive Two-Pass vs Welford's Algorithm

One of the most consequential examples of numerical instability in statistical computing arises in the calculation of the elementary sample variance:

$$s^2 = \frac{1}{n - 1} \sum_{i=1}^n (x_i - \bar{x})^2$$

### The Mechanism of Catastrophic Cancellation

In algebraic arithmetic, the condition number of subtracting two nearly equal numbers $x$ and $y$ ($x \approx y$) approaches infinity:

$$\text{Cond}(x - y) = \left| \frac{x}{x - y} \right| \to \infty \quad \text{as } y \to x$$

When two numbers that agree in their first $k$ most significant bits are subtracted in floating-point hardware:
$$\text{fl}(x - y) = \text{fl}(x) - \text{fl}(y)$$
the identical leading bits cancel out to zero. The result is shifted left into the significand register, pulling uninitialized or garbage low-order rounding bits into the significant digits. This phenomenon is termed **catastrophic cancellation**.

### The Naive "Textbook" One-Pass Formula

Many introductory statistics textbooks present the algebraic shortcut:

$$\sum_{i=1}^n (x_i - \bar{x})^2 = \sum_{i=1}^n x_i^2 - n \bar{x}^2 = \sum_{i=1}^n x_i^2 - \frac{1}{n} \left( \sum_{i=1}^n x_i \right)^2$$

Software developers frequently implement this formula because it requires only a **single pass** over the data, accumulating $S_1 = \sum x_i$ and $S_2 = \sum x_i^2$ simultaneously:

```python
# CATASTROPHIC ONE-PASS VARIANCE
def naive_variance(x):
    n = len(x)
    s1 = sum(x)
    s2 = sum(val**2 for val in x)
    return (s2 - (s1**2) / n) / (n - 1)
```

#### Why the Naive Formula Fails:
Suppose a dataset has a very large mean $\mu = 10^9$ and a small variance $\sigma^2 = 1.0$:
$$x = [10^9 + 1, \, 10^9 + 2, \, 10^9 + 3]$$
- $\sum x_i \approx 3 \times 10^9$, so $(\sum x_i)^2 / n \approx 3 \times 10^{18}$.
- $\sum x_i^2 \approx 3 \times 10^{18} + 14$.
In 64-bit double precision, the significand holds 53 bits ($\approx 15.95$ decimal digits). The number $3 \times 10^{18}$ requires 62 bits of integer precision!
Consequently, the low-order digits ($14$) fall completely beyond the 53-bit register limit and are discarded during rounding.
When the subtraction executes:
$$\text{fl}\left( \sum x_i^2 - \frac{(\sum x_i)^2}{n} \right) = 0.0 \quad \text{(or even negative!)}$$
The computed variance evaluates to zero or returns a negative number, violating the fundamental non-negativity axiom of variance!

### The Two-Pass Algorithm

The standard textbook two-pass algorithm computes the sample mean in the first pass, and then accumulates squared deviations in a second pass:

```python
# TWO-PASS ALGORITHM
def two_pass_variance(x):
    n = len(x)
    xbar = sum(x) / n
    return sum((val - xbar)**2 for val in x) / (n - 1)
```

The two-pass algorithm is numerically stable because subtracting the mean $\bar{x}$ from each observation shifts the data origin to zero. The squared deviations $(x_i - \bar{x})^2$ are small numbers computed without cancellation. However, the two-pass algorithm requires reading the entire dataset from RAM or disk twice, doubling I/O bandwidth.

### Welford's Numerically Stable One-Pass Algorithm

In 1962, B. P. Welford published an ingenious recurrence relation that computes the exact sample mean and sample variance in a **single pass** with optimal numerical stability.

#### Mathematical Formulation of Welford's Recurrence:
Let $\bar{x}_k$ denote the sample mean of the first $k$ observations, and let $M_{2, k} = \sum_{i=1}^k (x_i - \bar{x}_k)^2$ denote the sum of squared deviations of the first $k$ observations.

When the $(k+1)$-th observation $x_{k+1}$ arrives, the updated mean and sum of squared deviations are computed via the recurrence:

$$\bar{x}_{k+1} = \bar{x}_k + \frac{x_{k+1} - \bar{x}_k}{k + 1}$$

$$M_{2, k+1} = M_{2, k} + (x_{k+1} - \bar{x}_k)(x_{k+1} - \bar{x}_{k+1})$$

The sample variance after $n$ observations is given by:

$$s^2 = \frac{M_{2, n}}{n - 1}$$

```text
Welford Single-Pass State Flow:
  (x_{k+1}) ---> [ Delta1 = x_{k+1} - xbar_k ]
                         |
                         +---> [ xbar_{k+1} = xbar_k + Delta1 / (k+1) ]
                         |            |
                         v            v
                 [ Delta2 = x_{k+1} - xbar_{k+1} ]
                         |
                         v
                 [ M_{2, k+1} = M_{2, k} + Delta1 * Delta2 ]
```

Notice that the update for $M_2$ multiplies two distinct differences:
- $\Delta_1 = x_{k+1} - \bar{x}_k$ (deviation from the old mean).
- $\Delta_2 = x_{k+1} - \bar{x}_{k+1}$ (deviation from the updated new mean).

Because both $\Delta_1$ and $\Delta_2$ have the same sign, their product $\Delta_1 \Delta_2$ is **strictly non-negative**. Therefore, $M_{2, k+1} \ge M_{2, k}$ monotonically, making it mathematically impossible for Welford's algorithm to produce a negative variance!

---

## 4.3 Linear Regression Solvers: Normal Equations vs Cholesky vs Householder QR

In statistical computing, fitting an Ordinary Least Squares (OLS) linear regression model represents the single most frequently executed linear algebra task:

$$\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$$

where $\mathbf{X} \in \mathbb{R}^{n \times p}$ is the design matrix ($n \ge p$ with full column rank $\text{rank}(\mathbf{X}) = p$), $\mathbf{y} \in \mathbb{R}^n$ is the response vector, and $\boldsymbol{\beta} \in \mathbb{R}^p$ is the unknown parameter vector.

The OLS estimator minimizes the sum of squared residuals:

$$\min_{\boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2$$

Setting the gradient to zero yields the celebrated **Normal Equations**:

$$\mathbf{X}^\top \mathbf{X} \boldsymbol{\beta} = \mathbf{X}^\top \mathbf{y}$$

### The Three Fundamental Solution Pathways

How should a statistical computing engine solve for $\hat{\boldsymbol{\beta}}$ in software? There are three primary pathways:

#### Pathway 1: Normal Equations via Cholesky Decomposition
1. Explicitly compute the cross-product matrix $\mathbf{C} = \mathbf{X}^\top \mathbf{X} \in \mathbb{R}^{p \times p}$ and the right-hand vector $\mathbf{d} = \mathbf{X}^\top \mathbf{y} \in \mathbb{R}^p$.
2. Because $\mathbf{C}$ is symmetric positive definite (SPD), compute its **Cholesky factorization**:
   $$\mathbf{C} = \mathbf{L} \mathbf{L}^\top$$
   where $\mathbf{L}$ is a lower-triangular matrix with strictly positive diagonal entries.
3. Solve two triangular systems via forward and back substitution:
   $$\mathbf{L} \mathbf{z} = \mathbf{d} \quad (\text{forward solve for } \mathbf{z})$$
   $$\mathbf{L}^\top \boldsymbol{\beta} = \mathbf{z} \quad (\text{back solve for } \boldsymbol{\beta})$$

- **Computational Complexity (FLOPs)**:
  - Forming $\mathbf{X}^\top \mathbf{X}$: $n p^2$ FLOPs.
  - Cholesky factorization $\mathbf{L} \mathbf{L}^\top$: $\frac{1}{3} p^3$ FLOPs.
  - Forward and back substitution: $2 p^2$ FLOPs.
  - Total FLOP count: $\approx n p^2 + \frac{1}{3} p^3$.
- **Virtue**: Extremely fast. Requires only $p \times p$ working memory.

#### Pathway 2: Householder QR Decomposition
Instead of forming the cross-product $\mathbf{X}^\top \mathbf{X}$, factor the design matrix $\mathbf{X}$ directly into an orthogonal matrix $\mathbf{Q} \in \mathbb{R}^{n \times n}$ and an upper-triangular matrix $\mathbf{R} \in \mathbb{R}^{n \times p}$:

$$\mathbf{X} = \mathbf{Q} \mathbf{R} = \begin{bmatrix} \mathbf{Q}_1 & \mathbf{Q}_2 \end{bmatrix} \begin{bmatrix} \mathbf{R}_1 \\ \mathbf{0} \end{bmatrix} = \mathbf{Q}_1 \mathbf{R}_1$$

where $\mathbf{Q}_1 \in \mathbb{R}^{n \times p}$ has orthonormal columns ($\mathbf{Q}_1^\top \mathbf{Q}_1 = \mathbf{I}_p$) and $\mathbf{R}_1 \in \mathbb{R}^{p \times p}$ is upper triangular.

Substitute $\mathbf{X} = \mathbf{Q}_1 \mathbf{R}_1$ into the normal equations:
$$(\mathbf{Q}_1 \mathbf{R}_1)^\top (\mathbf{Q}_1 \mathbf{R}_1) \boldsymbol{\beta} = (\mathbf{Q}_1 \mathbf{R}_1)^\top \mathbf{y}$$
$$\mathbf{R}_1^\top (\mathbf{Q}_1^\top \mathbf{Q}_1) \mathbf{R}_1 \boldsymbol{\beta} = \mathbf{R}_1^\top \mathbf{Q}_1^\top \mathbf{y}$$
Because $\mathbf{Q}_1^\top \mathbf{Q}_1 = \mathbf{I}_p$:
$$\mathbf{R}_1^\top \mathbf{R}_1 \boldsymbol{\beta} = \mathbf{R}_1^\top \mathbf{Q}_1^\top \mathbf{y}$$
Since $\mathbf{R}_1$ has full rank, $\mathbf{R}_1^\top$ is invertible:

$$\mathbf{R}_1 \boldsymbol{\beta} = \mathbf{Q}_1^\top \mathbf{y}$$

The solution is obtained by forming the vector $\mathbf{c} = \mathbf{Q}_1^\top \mathbf{y}$ and solving the upper-triangular system $\mathbf{R}_1 \boldsymbol{\beta} = \mathbf{c}$ via back substitution!

- **Computational Complexity (FLOPs)**:
  - Householder QR factorization: $2 n p^2 - \frac{2}{3} p^3$ FLOPs.
  - Applying $\mathbf{Q}_1^\top$ to $\mathbf{y}$: $2 n p$ FLOPs.
  - Back substitution: $p^2$ FLOPs.
  - Total FLOP count: $\approx 2 n p^2 - \frac{2}{3} p^3$.
- Notice that QR requires approximately **twice as many FLOPs** as Cholesky when $n \gg p$.

### The Numerical Stability Paradox: The Squaring of the Condition Number

Why do standard statistical packages (`lm()` in R, `np.linalg.lstsq` in NumPy) default to QR decomposition despite it requiring twice as many operations?

The answer lies in **matrix conditioning**:

$$\kappa_2(\mathbf{X}^\top \mathbf{X}) = [\kappa_2(\mathbf{X})]^2$$

#### The Condition Number Squaring Theorem:
Let the singular values of $\mathbf{X}$ be $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p > 0$.
The condition number of $\mathbf{X}$ is:
$$\kappa_2(\mathbf{X}) = \frac{\sigma_1}{\sigma_p}$$
The eigenvalues of $\mathbf{X}^\top \mathbf{X}$ are $\lambda_j = \sigma_j^2$.
The condition number of $\mathbf{X}^\top \mathbf{X}$ is:
$$\kappa_2(\mathbf{X}^\top \mathbf{X}) = \frac{\lambda_1}{\lambda_p} = \frac{\sigma_1^2}{\sigma_p^2} = [\kappa_2(\mathbf{X})]^2$$

Consider an empirical design matrix with condition number $\kappa_2(\mathbf{X}) = 10^9$:
- In 64-bit IEEE double precision ($\sim 16$ decimal digits of precision):
- If we solve via **Householder QR**, the algorithm works directly with $\mathbf{X}$. The effective condition number is $10^9$. The computed solution retains:
  $$16 - 9 = 7 \text{ decimal digits of accuracy}$$
  The regression coefficients are accurate and reliable.
- If we solve via **Normal Equations (Cholesky)**, we must form $\mathbf{X}^\top \mathbf{X}$ in memory. The condition number is squared:
  $$\kappa_2(\mathbf{X}^\top \mathbf{X}) = (10^9)^2 = 10^{18}$$
  Because $10^{18} > 10^{16} = 1/\epsilon_{mach}$, the matrix $\mathbf{X}^\top \mathbf{X}$ is **completely singular to machine precision**! Roundoff errors swamp all significant digits, and Cholesky decomposition either aborts with a non-positive-definite error or returns completely bogus, explosive coefficients.

This fundamental theorem establishes that **Householder QR is vastly superior to the Normal Equations for collinear or poorly conditioned statistical data**.

---

## 4.4 Singular Value Decomposition, Principal Component Analysis, and Low-Rank Approximations

The **Singular Value Decomposition (SVD)** is widely regarded as the pinnacle of numerical linear algebra. In statistical computing, SVD provides the unifying engine for Principal Component Analysis (PCA), canonical correlation analysis, factor analysis, Ridge regression, and latent semantic indexing.

### The Singular Value Decomposition Theorem

Let $\mathbf{X} \in \mathbb{R}^{n \times p}$ be an arbitrary real matrix with $n \ge p$. There exist orthogonal matrices $\mathbf{U} \in \mathbb{R}^{n \times n}$ and $\mathbf{V} \in \mathbb{R}^{p \times p}$ and a diagonal matrix $\boldsymbol{\Sigma} \in \mathbb{R}^{n \times p}$ such that:

$$\mathbf{X} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top$$

where:
- $\mathbf{U}^\top \mathbf{U} = \mathbf{I}_n$ (the columns $\mathbf{u}_1, \dots, \mathbf{u}_n$ are the **left singular vectors**, forming an orthonormal basis for $\mathbb{R}^n$).
- $\mathbf{V}^\top \mathbf{V} = \mathbf{I}_p$ (the columns $\mathbf{v}_1, \dots, \mathbf{v}_p$ are the **right singular vectors**, forming an orthonormal basis for $\mathbb{R}^p$).
- $\boldsymbol{\Sigma} = \begin{bmatrix} \text{diag}(\sigma_1, \dots, \sigma_p) \\ \mathbf{0}_{(n-p) \times p} \end{bmatrix}$ contains the non-negative **singular values** arranged in non-increasing order:
  $$\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p \ge 0$$

In compact (thin / economy) SVD:

$$\mathbf{X} = \mathbf{U}_p \boldsymbol{\Sigma}_p \mathbf{V}^\top = \sum_{j=1}^p \sigma_j \mathbf{u}_j \mathbf{v}_j^\top$$

where $\mathbf{U}_p \in \mathbb{R}^{n \times p}$ contains the first $p$ orthonormal columns.

### Equivalence of SVD and Principal Component Analysis (PCA)

Let $\mathbf{X} \in \mathbb{R}^{n \times p}$ represent a multivariate dataset of $n$ observations across $p$ continuous variables. Assume the columns of $\mathbf{X}$ are centered to have zero mean ($\sum_{i=1}^n x_{ij} = 0$).

The sample covariance matrix is:

$$\mathbf{S} = \frac{1}{n - 1} \mathbf{X}^\top \mathbf{X}$$

#### Spectral Decomposition of the Covariance Matrix:
Substitute the thin SVD $\mathbf{X} = \mathbf{U}_p \boldsymbol{\Sigma}_p \mathbf{V}^\top$ into the covariance matrix:

$$\mathbf{S} = \frac{1}{n - 1} (\mathbf{U}_p \boldsymbol{\Sigma}_p \mathbf{V}^\top)^\top (\mathbf{U}_p \boldsymbol{\Sigma}_p \mathbf{V}^\top) = \frac{1}{n - 1} \mathbf{V} \boldsymbol{\Sigma}_p \mathbf{U}_p^\top \mathbf{U}_p \boldsymbol{\Sigma}_p \mathbf{V}^\top$$

Because $\mathbf{U}_p^\top \mathbf{U}_p = \mathbf{I}_p$:

$$\mathbf{S} = \mathbf{V} \left( \frac{\boldsymbol{\Sigma}_p^2}{n - 1} \right) \mathbf{V}^\top$$

This is the exact **eigenvalue decomposition** of the symmetric covariance matrix $\mathbf{S} = \mathbf{V} \boldsymbol{\Lambda} \mathbf{V}^\top$:
1. The **Principal Component Loadings** (eigenvectors of $\mathbf{S}$) are identical to the **right singular vectors $\mathbf{V}$** of the centered data matrix!
2. The **Sample Variances** of the principal components are directly related to the singular values:
   $$\lambda_j = \frac{\sigma_j^2}{n - 1}$$
3. The **Principal Component Scores** (projections of the observations onto the orthogonal principal axes) are given by:
   $$\mathbf{Z} = \mathbf{X} \mathbf{V} = (\mathbf{U}_p \boldsymbol{\Sigma}_p \mathbf{V}^\top) \mathbf{V} = \mathbf{U}_p \boldsymbol{\Sigma}_p$$

**Algorithmic Insight**:
Computing PCA via SVD on the centered matrix $\mathbf{X} / \sqrt{n - 1}$ avoids explicitly computing the sample covariance matrix $\mathbf{X}^\top \mathbf{X}$, preserving condition number stability and avoiding roundoff errors!

### The Eckart–Young–Mirsky Optimal Low-Rank Approximation Theorem

In statistical dimension reduction, image compression, and collaborative filtering (recommender systems), we seek a low-rank matrix $\hat{\mathbf{X}}_k$ of rank $k < p$ that approximates the high-dimensional matrix $\mathbf{X}$ as closely as possible.

In 1936, Carl Eckart and Gale Young (extended to general unitarily invariant norms by A. S. Mirsky in 1960) proved that the optimal rank-$k$ approximation is obtained by **truncating the SVD**:

$$\mathbf{X}_k = \sum_{j=1}^k \sigma_j \mathbf{u}_j \mathbf{v}_j^\top$$

#### The Theorem:
For any rank constraint $k \le \text{rank}(\mathbf{X})$:

$$\min_{\text{rank}(\mathbf{B}) \le k} \|\mathbf{X} - \mathbf{B}\|_F = \|\mathbf{X} - \mathbf{X}_k\|_F = \sqrt{\sum_{j=k+1}^p \sigma_j^2}$$

and for the spectral 2-norm:

$$\min_{\text{rank}(\mathbf{B}) \le k} \|\mathbf{X} - \mathbf{B}\|_2 = \|\mathbf{X} - \mathbf{X}_k\|_2 = \sigma_{k+1}$$

No other rank-$k$ matrix can achieve a smaller approximation error in either the Frobenius or spectral norm.

---

## 4.5 Sparse Matrix Representations: CSR, CSC, and Sparse BLAS

In modern statistical applications—such as natural language processing (term-document matrices), genomic sparse linkage, spatial autoregressions, and graph analytics—matrices can be massive ($N = 1,000,000$) yet contain $99.9\%$ zero entries.

Storing a $10^6 \times 10^6$ matrix in dense double precision requires:
$$\text{Memory} = 10^{12} \times 8 \text{ bytes} = 8 \text{ Terabytes of RAM!}$$
However, if only $0.01\%$ of entries are non-zero ($10^8$ non-zeros), storing only the non-zero elements requires less than 1.5 GB of RAM.

### Compressed Sparse Row (CSR) and Compressed Sparse Column (CSC) Formats

The two primary standard formats for sparse matrix computations are CSR and CSC:

#### 1. Compressed Sparse Row (CSR) Format
CSR compresses row offsets while storing column indices and values explicitly. It uses three 1D contiguous arrays:
- `data`: A floating-point array of length $N_{nz}$ containing all non-zero values in row-major order.
- `indices`: An integer array of length $N_{nz}$ containing the column indices ($0 \le j < C$) for each corresponding entry in `data`.
- `indptr` (Index Pointers): An integer array of length $R + 1$, where `indptr[i]` denotes the starting index in `data` and `indices` for row $i$. The number of non-zero elements in row $i$ is simply `indptr[i+1] - indptr[i]`.

```text
CSR Layout Example for Matrix:
  [ 0.0  5.2  0.0 ]
  [ 1.8  0.0  0.0 ]
  [ 0.0  3.4  9.1 ]

data    : [ 5.2,  1.8,  3.4,  9.1 ] (Length = 4)
indices : [  1,    0,    1,    2  ] (Length = 4)
indptr  : [  0,    1,    2,    4  ] (Length = 3 + 1 = 4)
```

- **Strengths**: Extremely efficient for row slicing (`A[i, :]`), row-wise matrix additions, and **Sparse Matrix-Vector Multiplication (SpMV)** $\mathbf{y} = \mathbf{A} \mathbf{x}$.
- In SpMV, the inner product for row $i$ is evaluated by sweeping over the slice `data[indptr[i]:indptr[i+1]]`, executing in $O(N_{nz})$ time without touching any zero elements.

#### 2. Compressed Sparse Column (CSC) Format
CSC is the column-major analogue of CSR:
- `data`: Non-zero values stored in column-major order.
- `indices`: Row indices for each non-zero entry.
- `indptr`: Column index pointers of length $C + 1$.
- **Strengths**: Extremely efficient for column slicing (`A[:, j]`) and sparse matrix-matrix multiplication (`SpGEMM`). CSC is the standard format used by compiled sparse solvers such as SuperLU and SuiteSparse (CHOLMOD).

---

## Fully worked question 1: Error Analysis of Catastrophic Cancellation in Naive Sample Variance and Mathematical Proof of Welford's Recurrence

### Question
A physical sensor array records atmospheric pressure deviations over a high-altitude observation post. A calibration dataset of $n = 5$ measurements is collected:

$$\mathbf{x} = [1000000.2, \, 1000000.4, \, 1000000.6, \, 1000000.8, \, 1000001.0]$$

1. Compute the exact theoretical sample mean $\bar{x}$ and exact sample variance $s^2$ using exact real arithmetic.
2. Suppose an engineer implements the textbook one-pass variance formula:
   $$s^2 = \frac{1}{n - 1} \left( \sum_{i=1}^n x_i^2 - \frac{1}{n} \left( \sum_{i=1}^n x_i \right)^2 \right)$$
   on a hypothetical floating-point system that maintains 8 decimal digits of significand precision. Demonstrate step-by-step how catastrophic cancellation causes the computed variance to completely lose significance.
3. Provide a complete, rigorous mathematical proof of **Welford's recurrence relations**:
   $$\bar{x}_k = \bar{x}_{k-1} + \frac{x_k - \bar{x}_{k-1}}{k}$$
   $$M_{2, k} = M_{2, k-1} + (x_k - \bar{x}_{k-1})(x_k - \bar{x}_k)$$
   where $M_{2, k} = \sum_{i=1}^k (x_i - \bar{x}_k)^2$.
4. Trace Welford's algorithm numerically on the sensor dataset, showing the state variables $(\bar{x}_k, M_{2, k})$ at each step $k = 1, \dots, 5$.

---

### Solution, step 1: Exact theoretical mean and variance

**Solution, step 1: Exact theoretical mean and variance.**

Let us decompose each observation into a baseline constant $c = 1,000,000$ and a small perturbation $u_i = x_i - c$:
$$\mathbf{u} = [0.2, \, 0.4, \, 0.6, \, 0.8, \, 1.0]$$

1. **Exact Sample Mean**:
   $$\sum_{i=1}^5 u_i = 0.2 + 0.4 + 0.6 + 0.8 + 1.0 = 3.0$$
   $$\bar{u} = \frac{3.0}{5} = 0.6$$
   $$\bar{x} = c + \bar{u} = 1,000,000 + 0.6 = 1,000,000.6$$

2. **Exact Sample Variance**:
   Because adding a constant does not alter variance, $\text{Var}(\mathbf{x}) = \text{Var}(\mathbf{u})$:
   $$\sum_{i=1}^5 (u_i - \bar{u})^2 = (0.2 - 0.6)^2 + (0.4 - 0.6)^2 + (0.6 - 0.6)^2 + (0.8 - 0.6)^2 + (1.0 - 0.6)^2$$
   $$= (-0.4)^2 + (-0.2)^2 + (0.0)^2 + (0.2)^2 + (0.4)^2 = 0.16 + 0.04 + 0.00 + 0.04 + 0.16 = 0.40$$

   The exact sample variance is:
   $$s^2 = \frac{0.40}{5 - 1} = \frac{0.40}{4} = 0.10$$

---

### Solution, step 2: Catastrophic cancellation simulation with 8-digit precision

**Solution, step 2: Catastrophic cancellation simulation with 8-digit precision.**

Consider an arithmetic environment that rounds all intermediate operations to 8 significant decimal digits.

1. **Sum of Observations $\sum x_i$**:
   $$\sum x_i = 1000000.2 + 1000000.4 + 1000000.6 + 1000000.8 + 1000001.0 = 5000003.0$$
   This has 8 significant digits: $5.0000030 \times 10^6$. Stored exactly.

2. **Evaluation of $(\sum x_i)^2 / 5$**:
   $$(5000003.0)^2 = 25,000,030,000,009.0 \approx 2.5000030000009 \times 10^{13}$$
   Rounded to 8 decimal digits:
   $$\text{fl}\left( (\sum x_i)^2 \right) = 2.5000030 \times 10^{13}$$
   Dividing by 5:
   $$\text{fl}\left( \frac{(\sum x_i)^2}{5} \right) = \frac{2.5000030 \times 10^{13}}{5} = 5.0000060 \times 10^{12}$$

3. **Sum of Squares $\sum x_i^2$**:
   Let us compute each square:
   - $(1000000.2)^2 = 1,000,000,400,000.04 \to \text{rounded: } 1.0000004 \times 10^{12}$
   - $(1000000.4)^2 = 1,000,000,800,000.16 \to \text{rounded: } 1.0000008 \times 10^{12}$
   - $(1000000.6)^2 = 1,000,001,200,000.36 \to \text{rounded: } 1.0000012 \times 10^{12}$
   - $(1000000.8)^2 = 1,000,001,600,000.64 \to \text{rounded: } 1.0000016 \times 10^{12}$
   - $(1000001.0)^2 = 1,000,002,000,001.00 \to \text{rounded: } 1.0000020 \times 10^{12}$
   Summing the five values:
   $$\sum x_i^2 \approx 5.0000060 \times 10^{12}$$

4. **The Subtraction**:
   Now evaluate the numerator:
   $$\sum x_i^2 - \frac{(\sum x_i)^2}{5} = 5.0000060 \times 10^{12} - 5.0000060 \times 10^{12} = \mathbf{0.0}$$

   $$\hat{s}^2_{naive} = \frac{0.0}{4} = \mathbf{0.0}$$

The true variance is $0.10$, but the naive formula reports **$0.0$**! All significant digits were completely obliterated by catastrophic cancellation during the subtraction of the two massive numbers.

---

### Solution, step 3: Mathematical proof of Welford's recurrence relations

**Solution, step 3: Mathematical proof of Welford's recurrence relations.**

#### 1. Proof of Mean Recurrence:
By definition:
$$\bar{x}_k = \frac{1}{k} \sum_{i=1}^k x_i = \frac{1}{k} \left( \sum_{i=1}^{k-1} x_i + x_k \right) = \frac{1}{k} \left( (k - 1) \bar{x}_{k-1} + x_k \right)$$
$$= \frac{k \bar{x}_{k-1} - \bar{x}_{k-1} + x_k}{k} = \bar{x}_{k-1} + \frac{x_k - \bar{x}_{k-1}}{k}$$
This proves the mean recurrence equation.

#### 2. Proof of Sum of Squared Deviations Recurrence:
By definition:
$$M_{2, k} = \sum_{i=1}^k (x_i - \bar{x}_k)^2$$
Split the sum into the first $k-1$ terms and the $k$-th term:
$$M_{2, k} = \sum_{i=1}^{k-1} (x_i - \bar{x}_k)^2 + (x_k - \bar{x}_k)^2$$

Notice that:
$$x_i - \bar{x}_k = x_i - \left( \bar{x}_{k-1} + \frac{x_k - \bar{x}_{k-1}}{k} \right) = (x_i - \bar{x}_{k-1}) - \frac{x_k - \bar{x}_{k-1}}{k}$$

Square both sides:
$$(x_i - \bar{x}_k)^2 = (x_i - \bar{x}_{k-1})^2 - \frac{2 (x_k - \bar{x}_{k-1})}{k} (x_i - \bar{x}_{k-1}) + \frac{(x_k - \bar{x}_{k-1})^2}{k^2}$$

Sum across $i = 1, \dots, k-1$:
$$\sum_{i=1}^{k-1} (x_i - \bar{x}_k)^2 = \sum_{i=1}^{k-1} (x_i - \bar{x}_{k-1})^2 - \frac{2 (x_k - \bar{x}_{k-1})}{k} \sum_{i=1}^{k-1} (x_i - \bar{x}_{k-1}) + (k - 1) \frac{(x_k - \bar{x}_{k-1})^2}{k^2}$$

Recall that by definition of the sample mean, the sum of deviations around $\bar{x}_{k-1}$ is identically zero:
$$\sum_{i=1}^{k-1} (x_i - \bar{x}_{k-1}) = 0$$

Therefore, the middle cross-product term vanishes!
$$\sum_{i=1}^{k-1} (x_i - \bar{x}_k)^2 = M_{2, k-1} + \frac{k - 1}{k^2} (x_k - \bar{x}_{k-1})^2$$

Now add the $k$-th term $(x_k - \bar{x}_k)^2$:
Using $\bar{x}_k = \bar{x}_{k-1} + \frac{x_k - \bar{x}_{k-1}}{k}$:
$$x_k - \bar{x}_k = x_k - \bar{x}_{k-1} - \frac{x_k - \bar{x}_{k-1}}{k} = \left( 1 - \frac{1}{k} \right) (x_k - \bar{x}_{k-1}) = \left( \frac{k - 1}{k} \right) (x_k - \bar{x}_{k-1})$$
Squaring this gives:
$$(x_k - \bar{x}_k)^2 = \frac{(k - 1)^2}{k^2} (x_k - \bar{x}_{k-1})^2$$

Combine the two parts into $M_{2, k}$:
$$M_{2, k} = M_{2, k-1} + \left[ \frac{k - 1}{k^2} + \frac{(k - 1)^2}{k^2} \right] (x_k - \bar{x}_{k-1})^2$$

Simplify the bracketed factor:
$$\frac{(k - 1) + (k - 1)^2}{k^2} = \frac{(k - 1)(1 + k - 1)}{k^2} = \frac{(k - 1) k}{k^2} = \frac{k - 1}{k}$$

Thus:
$$M_{2, k} = M_{2, k-1} + \frac{k - 1}{k} (x_k - \bar{x}_{k-1})^2$$

Finally, rewrite $\frac{k - 1}{k} (x_k - \bar{x}_{k-1})$ using our earlier identity:
$$\left( \frac{k - 1}{k} \right) (x_k - \bar{x}_{k-1}) = x_k - \bar{x}_k$$

Substituting this yields:

$$M_{2, k} = M_{2, k-1} + (x_k - \bar{x}_{k-1})(x_k - \bar{x}_k)$$

This proves Welford's recurrence relation.

---

### Solution, step 4: Numerical trace of Welford's algorithm

**Solution, step 4: Numerical trace of Welford's algorithm.**

Let us trace the algorithm on $\mathbf{x} = [1000000.2, \, 1000000.4, \, 1000000.6, \, 1000000.8, \, 1000001.0]$:

- **Initialization ($k = 1, x_1 = 1000000.2$)**:
  $$\bar{x}_1 = 1000000.2, \quad M_{2, 1} = 0.0$$

- **Step $k = 2, x_2 = 1000000.4$**:
  $$\Delta_1 = x_2 - \bar{x}_1 = 1000000.4 - 1000000.2 = 0.2$$
  $$\bar{x}_2 = \bar{x}_1 + \frac{\Delta_1}{2} = 1000000.2 + 0.1 = 1000000.3$$
  $$\Delta_2 = x_2 - \bar{x}_2 = 1000000.4 - 1000000.3 = 0.1$$
  $$M_{2, 2} = M_{2, 1} + \Delta_1 \Delta_2 = 0.0 + (0.2 \times 0.1) = 0.02$$

- **Step $k = 3, x_3 = 1000000.6$**:
  $$\Delta_1 = x_3 - \bar{x}_2 = 1000000.6 - 1000000.3 = 0.3$$
  $$\bar{x}_3 = \bar{x}_2 + \frac{\Delta_1}{3} = 1000000.3 + 0.1 = 1000000.4$$
  $$\Delta_2 = x_3 - \bar{x}_3 = 1000000.6 - 1000000.4 = 0.2$$
  $$M_{2, 3} = M_{2, 2} + \Delta_1 \Delta_2 = 0.02 + (0.3 \times 0.2) = 0.02 + 0.06 = 0.08$$

- **Step $k = 4, x_4 = 1000000.8$**:
  $$\Delta_1 = x_4 - \bar{x}_3 = 1000000.8 - 1000000.4 = 0.4$$
  $$\bar{x}_4 = \bar{x}_3 + \frac{\Delta_1}{4} = 1000000.4 + 0.1 = 1000000.5$$
  $$\Delta_2 = x_4 - \bar{x}_4 = 1000000.8 - 1000000.5 = 0.3$$
  $$M_{2, 4} = M_{2, 3} + \Delta_1 \Delta_2 = 0.08 + (0.4 \times 0.3) = 0.08 + 0.12 = 0.20$$

- **Step $k = 5, x_5 = 1000001.0$**:
  $$\Delta_1 = x_5 - \bar{x}_4 = 1000001.0 - 1000000.5 = 0.5$$
  $$\bar{x}_5 = \bar{x}_4 + \frac{\Delta_1}{5} = 1000000.5 + 0.1 = 1000000.6$$
  $$\Delta_2 = x_5 - \bar{x}_5 = 1000001.0 - 1000000.6 = 0.4$$
  $$M_{2, 5} = M_{2, 4} + \Delta_1 \Delta_2 = 0.20 + (0.5 \times 0.4) = 0.20 + 0.20 = 0.40$$

Finally, compute the sample variance:
$$s^2 = \frac{M_{2, 5}}{n - 1} = \frac{0.40}{4} = \mathbf{0.10}$$

Welford's algorithm computes the **exact theoretical variance $0.10$** flawlessly in a single pass without suffering from catastrophic cancellation!

---

## Fully worked question 2: Computational Stability and FLOP Count Comparison: Cholesky Decomposition vs Householder QR Decomposition for OLS Estimation

### Question
An econometrician models macroeconomic investment trends using an Ordinary Least Squares (OLS) multiple regression model:

$$\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$$

with $n = 100,000$ observational quarterly records and $p = 50$ macroeconomic indicators.
The design matrix $\mathbf{X}$ has full column rank, but exhibits moderate multicollinearity with condition number:

$$\kappa_2(\mathbf{X}) = 10^7$$

1. Calculate the exact floating-point operation count (FLOPs) required to compute $\hat{\boldsymbol{\beta}}$ via:
   - **Method A (Normal Equations with Cholesky Decomposition)**
   - **Method B (Householder QR Decomposition)**
   Quantify the FLOP ratio $\text{FLOPs}_{QR} / \text{FLOPs}_{Cholesky}$.
2. Under 64-bit IEEE double-precision arithmetic ($\epsilon_{mach} \approx 2.22 \times 10^{-16}$), analyze the condition number of the system solved under Method A versus Method B.
3. Compute the theoretical bound on the relative error of the estimated coefficient vector $\|\delta \hat{\boldsymbol{\beta}}\| / \|\hat{\boldsymbol{\beta}}\|$ under both methods.
4. Conclude why numerical software libraries recommend QR decomposition for general statistical regression modeling despite its higher operation count.

---

### Solution, step 1: FLOP count derivation and ratio

**Solution, step 1: FLOP count derivation and ratio.**

We are given $n = 100,000 = 10^5$ and $p = 50$. Notice that $n \gg p$.

#### Method A: Normal Equations with Cholesky Decomposition
1. **Forming Cross-Product Matrix $\mathbf{X}^\top \mathbf{X}$**:
   Since $\mathbf{X}^\top \mathbf{X}$ is symmetric, only the upper triangle ($p(p+1)/2$ entries) needs to be computed. Each entry is an inner product of two length-$n$ vectors, requiring $n$ multiplications and $n-1$ additions ($\approx 2n$ FLOPs):
   $$\text{FLOPs}(\mathbf{X}^\top \mathbf{X}) \approx 2n \times \frac{p^2}{2} = n p^2$$
   For $n = 10^5, p = 50$:
   $$\text{FLOPs}(\mathbf{X}^\top \mathbf{X}) = 10^5 \times 50^2 = 10^5 \times 2,500 = 250,000,000 \text{ FLOPs} = 2.5 \times 10^8 \text{ FLOPs}$$

2. **Forming Right-Hand Vector $\mathbf{X}^\top \mathbf{y}$**:
   Multiplying a $p \times n$ matrix by a length-$n$ vector requires:
   $$\text{FLOPs}(\mathbf{X}^\top \mathbf{y}) \approx 2 n p = 2 \times 10^5 \times 50 = 10,000,000 \text{ FLOPs} = 1.0 \times 10^7 \text{ FLOPs}$$

3. **Cholesky Factorization $\mathbf{L} \mathbf{L}^\top$**:
   Factoring a $p \times p$ SPD matrix requires:
   $$\text{FLOPs}(\text{Cholesky}) \approx \frac{1}{3} p^3 = \frac{1}{3} (50)^3 = \frac{125,000}{3} \approx 41,667 \text{ FLOPs}$$

4. **Triangular Solves (Forward and Back Substitution)**:
   $$\text{FLOPs}(\text{Solves}) \approx 2 p^2 = 2 \times 2,500 = 5,000 \text{ FLOPs}$$

Total FLOPs for Method A:
$$\text{FLOPs}_{Cholesky} \approx n p^2 + 2 n p + \frac{1}{3} p^3 \approx 250,000,000 + 10,000,000 + 41,667 \approx 260,041,667 \text{ FLOPs}$$
$$\text{FLOPs}_{Cholesky} \approx 2.60 \times 10^8 \text{ FLOPs}$$

---

#### Method B: Householder QR Decomposition
1. **Householder Factorization $\mathbf{X} = \mathbf{Q} \mathbf{R}$**:
   Factoring an $n \times p$ matrix using Householder reflections requires:
   $$\text{FLOPs}(\text{Householder}) \approx 2 n p^2 - \frac{2}{3} p^3$$
   For $n = 10^5, p = 50$:
   $$\text{FLOPs}(\text{Householder}) \approx 2 \times 10^5 \times 2,500 - \frac{2}{3} (125,000) = 500,000,000 - 83,333 \approx 499,916,667 \text{ FLOPs}$$

2. **Forming $\mathbf{c} = \mathbf{Q}_1^\top \mathbf{y}$**:
   Applying the $p$ stored Householder vectors to $\mathbf{y}$ requires:
   $$\text{FLOPs}(\mathbf{Q}^\top \mathbf{y}) \approx 2 n p = 2 \times 10^5 \times 50 = 10,000,000 \text{ FLOPs}$$

3. **Back Substitution $\mathbf{R}_1 \boldsymbol{\beta} = \mathbf{c}$**:
   Solving the $p \times p$ upper triangular system requires:
   $$\text{FLOPs}(\text{BackSolve}) \approx p^2 = 2,500 \text{ FLOPs}$$

Total FLOPs for Method B:
$$\text{FLOPs}_{QR} \approx 2 n p^2 + 2 n p - \frac{2}{3} p^3 \approx 500,000,000 + 10,000,000 - 83,333 \approx 509,916,667 \text{ FLOPs}$$
$$\text{FLOPs}_{QR} \approx 5.10 \times 10^8 \text{ FLOPs}$$

---

#### FLOP Ratio:
$$\frac{\text{FLOPs}_{QR}}{\text{FLOPs}_{Cholesky}} \approx \frac{5.10 \times 10^8}{2.60 \times 10^8} \approx 1.961 \approx 2.0$$

Householder QR requires almost **exactly twice as many operations** as Cholesky.

---

### Solution, step 2: Condition number analysis

**Solution, step 2: Condition number analysis.**

We are given $\kappa_2(\mathbf{X}) = 10^7$.

1. **Condition Number under Method B (QR Decomposition)**:
   Householder QR operates directly on $\mathbf{X}$. Because orthogonal transformations preserve Euclidean 2-norms ($\|\mathbf{Q} \mathbf{z}\|_2 = \|\mathbf{z}\|_2$):
   $$\kappa_2(\mathbf{R}_1) = \kappa_2(\mathbf{Q}_1 \mathbf{R}_1) = \kappa_2(\mathbf{X}) = 10^7$$
   The condition number of the triangular system solved in back substitution is:
   $$\kappa_{QR} = 10^7$$

2. **Condition Number under Method A (Normal Equations / Cholesky)**:
   Method A must solve the system with matrix $\mathbf{C} = \mathbf{X}^\top \mathbf{X}$.
   By the Condition Number Squaring Theorem:
   $$\kappa_2(\mathbf{X}^\top \mathbf{X}) = [\kappa_2(\mathbf{X})]^2 = (10^7)^2 = 10^{14}$$
   The condition number of the system solved under Cholesky is:
   $$\kappa_{Cholesky} = 10^{14}$$

---

### Solution, step 3: Relative error bounds and precision loss

**Solution, step 3: Relative error bounds and precision loss.**

In IEEE 754 double-precision arithmetic, machine epsilon is:
$$\epsilon_{mach} \approx 2.22 \times 10^{-16} \implies u \approx 1.11 \times 10^{-16}$$

The theoretical relative error bound on the computed solution $\hat{\boldsymbol{\beta}}$ satisfies:
$$\frac{\|\delta \hat{\boldsymbol{\beta}}\|}{\|\hat{\boldsymbol{\beta}}\|} \le \mathcal{O}(\kappa \cdot \epsilon_{mach})$$

1. **Under Method B (QR Decomposition)**:
   $$\frac{\|\delta \hat{\boldsymbol{\beta}}\|}{\|\hat{\boldsymbol{\beta}}\|} \le 10^7 \times 2.22 \times 10^{-16} \approx 2.22 \times 10^{-9}$$
   The computed solution loses at most 7 decimal digits of precision.
   Since double precision provides 16 digits, the coefficients retain:
   $$16 - 7 = \mathbf{9 \text{ reliable, significant decimal digits!}}$$

2. **Under Method A (Normal Equations / Cholesky)**:
   $$\frac{\|\delta \hat{\boldsymbol{\beta}}\|}{\|\hat{\boldsymbol{\beta}}\|} \le 10^{14} \times 2.22 \times 10^{-16} \approx 2.22 \times 10^{-2} = 0.0222$$
   The relative error is bounded only by $\sim 2.2\%$. The solution loses 14 decimal digits of precision:
   $$16 - 14 = \mathbf{2 \text{ significant decimal digits!}}$$
   The estimated coefficients are corrupted by roundoff noise, with only 1 or 2 trustworthy digits remaining.

---

### Solution, step 4: Synthesis and engineering recommendation

**Solution, step 4: Synthesis and engineering recommendation.**

#### Conclusion:
While Method A (Cholesky) executes in roughly half the wall-clock time, it exposes the user to severe numerical vulnerability whenever explanatory variables exhibit collinearity. Squaring the condition number from $10^7$ to $10^{14}$ virtually exhausts the 16-digit precision of double-precision hardware.

In contrast, **Householder QR maintains the original condition number $\kappa_2(\mathbf{X}) = 10^7$**, delivering 9 robust digits of precision. Because modern CPUs execute hundreds of millions of FLOPs in milliseconds, paying a $2\times$ FLOP penalty to guarantee mathematical accuracy is overwhelmingly the correct engineering trade-off for statistical software.

---

## Fully worked question 3: Derivation of Principal Components via SVD and Proof of the Eckart–Young–Mirsky Optimal Low-Rank Matrix Approximation

### Question
A chemometrics laboratory analyzes spectroscopic absorption curves across $n = 100$ compound samples and $p = 6$ optical wavelengths. After column-centering, the $100 \times 6$ data matrix $\mathbf{X}_c$ yields the following singular values:

$$\boldsymbol{\sigma} = [\sigma_1 = 120.0, \, \sigma_2 = 45.0, \, \sigma_3 = 18.0, \, \sigma_4 = 6.0, \, \sigma_5 = 2.0, \, \sigma_6 = 0.5]$$

1. Derive the total empirical variance of the dataset, and calculate the percentage of total variance explained by the first two principal components ($k = 2$).
2. Formulate the rank-2 optimal low-rank approximation $\hat{\mathbf{X}}_2$ in terms of the singular vectors and singular values.
3. State and prove the **Eckart–Young–Mirsky Theorem** for the Frobenius norm:
   $$\min_{\text{rank}(\mathbf{B}) \le k} \|\mathbf{X} - \mathbf{B}\|_F = \|\mathbf{X} - \mathbf{X}_k\|_F = \sqrt{\sum_{j=k+1}^p \sigma_j^2}$$
4. Compute the exact approximation errors in both the **Frobenius norm** $\|\mathbf{X}_c - \hat{\mathbf{X}}_2\|_F$ and the **spectral 2-norm** $\|\mathbf{X}_c - \hat{\mathbf{X}}_2\|_2$ for the chemometrics dataset.

---

### Solution, step 1: Total empirical variance and variance explained by top 2 PCs

**Solution, step 1: Total empirical variance and variance explained by top 2 PCs.**

Let $\mathbf{S} = \frac{1}{n - 1} \mathbf{X}_c^\top \mathbf{X}_c$ denote the sample covariance matrix.
The total variance of the dataset is the trace of the covariance matrix:

$$\text{Total Variance} = \text{tr}(\mathbf{S}) = \sum_{j=1}^p \text{Var}(X_j) = \sum_{j=1}^p \lambda_j$$

Recall from SVD theory that the eigenvalues of $\mathbf{S}$ are related to the singular values of $\mathbf{X}_c$ by:
$$\lambda_j = \frac{\sigma_j^2}{n - 1}$$

With $n = 100$, the divisor is $n - 1 = 99$.
Let us compute $\sigma_j^2$ for each component:
- $\sigma_1^2 = (120.0)^2 = 14,400$
- $\sigma_2^2 = (45.0)^2 = 2,025$
- $\sigma_3^2 = (18.0)^2 = 324$
- $\sigma_4^2 = (6.0)^2 = 36$
- $\sigma_5^2 = (2.0)^2 = 4$
- $\sigma_6^2 = (0.5)^2 = 0.25$

Sum of squared singular values:
$$\sum_{j=1}^6 \sigma_j^2 = 14,400 + 2,025 + 324 + 36 + 4 + 0.25 = 16,789.25$$

Total empirical variance:
$$\text{Total Variance} = \frac{16,789.25}{99} \approx 169.5884$$

#### Proportion of Variance Explained by Top 2 PCs ($k = 2$):
$$\text{PVE}_2 = \frac{\lambda_1 + \lambda_2}{\sum_{j=1}^6 \lambda_j} = \frac{\sigma_1^2 + \sigma_2^2}{\sum_{j=1}^6 \sigma_j^2}$$

$$\sigma_1^2 + \sigma_2^2 = 14,400 + 2,025 = 16,425.0$$

$$\text{PVE}_2 = \frac{16,425.0}{16,789.25} \approx 0.978304 \approx 97.83\%$$

The first two principal components explain **$97.83\%$ of the total variation** in the spectroscopic dataset.

---

### Solution, step 2: Rank-2 optimal low-rank approximation formulation

**Solution, step 2: Rank-2 optimal low-rank approximation formulation.**

The rank-2 truncated SVD is formulated as:

$$\hat{\mathbf{X}}_2 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^\top + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^\top = 120.0 \, \mathbf{u}_1 \mathbf{v}_1^\top + 45.0 \, \mathbf{u}_2 \mathbf{v}_2^\top$$

where:
- $\mathbf{u}_1, \mathbf{u}_2 \in \mathbb{R}^{100}$ are the first two orthonormal left singular vectors (normalized PC score directions).
- $\mathbf{v}_1, \mathbf{v}_2 \in \mathbb{R}^6$ are the first two orthonormal right singular vectors (wavelength loading vectors).

---

### Solution, step 3: Proof of the Eckart–Young–Mirsky Theorem (Frobenius Norm)

**Solution, step 3: Proof of the Eckart–Young–Mirsky Theorem (Frobenius Norm).**

Let $\mathbf{X} \in \mathbb{R}^{n \times p}$ have SVD $\mathbf{X} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top$, with singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_p \ge 0$.
We seek to minimize $\|\mathbf{X} - \mathbf{B}\|_F^2$ subject to $\text{rank}(\mathbf{B}) \le k$.

1. **Unitary Invariance of the Frobenius Norm**:
   For any orthogonal matrices $\mathbf{U}$ and $\mathbf{V}$:
   $$\|\mathbf{X} - \mathbf{B}\|_F^2 = \|\mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top - \mathbf{B}\|_F^2 = \|\mathbf{U}^\top (\mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top - \mathbf{B}) \mathbf{V}\|_F^2 = \|\boldsymbol{\Sigma} - \mathbf{U}^\top \mathbf{B} \mathbf{V}\|_F^2$$

   Let $\mathbf{Y} = \mathbf{U}^\top \mathbf{B} \mathbf{V}$. Since $\mathbf{U}$ and $\mathbf{V}$ are non-singular, $\text{rank}(\mathbf{Y}) = \text{rank}(\mathbf{B}) \le k$.
   Thus, the problem is equivalent to:
   $$\min_{\text{rank}(\mathbf{Y}) \le k} \|\boldsymbol{\Sigma} - \mathbf{Y}\|_F^2$$

2. **Decomposition of the Squared Frobenius Norm**:
   $$\|\boldsymbol{\Sigma} - \mathbf{Y}\|_F^2 = \sum_{i=1}^p (\sigma_i - Y_{ii})^2 + \sum_{i \ne j} Y_{ij}^2$$
   To minimize this quantity, we must set all off-diagonal entries $Y_{ij} = 0$ for $i \ne j$.
   Thus, $\mathbf{Y}$ must be a diagonal matrix.

3. **Diagonal Rank Constraint**:
   Since $\text{rank}(\mathbf{Y}) \le k$ and $\mathbf{Y}$ is diagonal, $\mathbf{Y}$ can have at most $k$ non-zero diagonal entries.
   To minimize:
   $$\sum_{i=1}^p (\sigma_i - Y_{ii})^2$$
   for each non-zero diagonal entry, we set $Y_{ii} = \sigma_i$ (giving $(\sigma_i - \sigma_i)^2 = 0$).
   For the $p - k$ zero entries, $Y_{ii} = 0$, giving penalty $\sigma_i^2$.
   To minimize the sum of discarded squared singular values:
   $$\min_{\{i_1, \dots, i_k\}} \sum_{i \notin \{i_1, \dots, i_k\}} \sigma_i^2$$
   we must retain the **$k$ largest singular values** $\sigma_1, \dots, \sigma_k$ and set the remaining $p - k$ values to zero!

4. **Reconstructing $\mathbf{B}_{opt}$**:
   The optimal matrix $\mathbf{Y}_{opt}$ has diagonal entries $[\sigma_1, \dots, \sigma_k, 0, \dots, 0]$.
   Transforming back:
   $$\mathbf{B}_{opt} = \mathbf{U} \mathbf{Y}_{opt} \mathbf{V}^\top = \sum_{j=1}^k \sigma_j \mathbf{u}_j \mathbf{v}_j^\top = \mathbf{X}_k$$

The minimal approximation error in Frobenius norm is:

$$\|\mathbf{X} - \mathbf{X}_k\|_F = \sqrt{\sum_{j=k+1}^p \sigma_j^2}$$

This completes the proof of the Eckart–Young–Mirsky Theorem.

---

### Solution, step 4: Exact approximation errors for the chemometrics dataset

**Solution, step 4: Exact approximation errors for the chemometrics dataset.**

We evaluate the errors for $k = 2$:

1. **Frobenius Norm Approximation Error**:
   The discarded singular values are $\sigma_3, \sigma_4, \sigma_5, \sigma_6$:
   $$\|\mathbf{X}_c - \hat{\mathbf{X}}_2\|_F = \sqrt{\sigma_3^2 + \sigma_4^2 + \sigma_5^2 + \sigma_6^2}$$
   $$\sum_{j=3}^6 \sigma_j^2 = 324 + 36 + 4 + 0.25 = 364.25$$
   $$\|\mathbf{X}_c - \hat{\mathbf{X}}_2\|_F = \sqrt{364.25} \approx 19.0853$$

2. **Spectral 2-Norm Approximation Error**:
   By the spectral norm formulation of the Eckart–Young–Mirsky Theorem:
   $$\|\mathbf{X}_c - \hat{\mathbf{X}}_2\|_2 = \sigma_{k+1} = \sigma_3 = 18.0$$

#### Summary:
The rank-2 truncated SVD achieves an optimal Frobenius error of $19.09$ and an optimal spectral operator error of exactly $18.0$, capturing nearly $98\%$ of the structural variance with a six-fold reduction in data rank.
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(unit4_text)

print("Successfully written deep Unit 4!")
