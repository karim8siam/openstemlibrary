# Unit 4: Numerical Linear Algebra, Floating-Point Arithmetic, QR/SVD Decompositions, and Matrix Computations

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

---

## 4.8 Spectral Graph Theory, Graph Laplacians, and Spectral Clustering

In modern spatial statistics, network analytics, and manifold learning, data relationships are naturally modeled as graphs $\mathcal{G} = (\mathcal{V}, \mathcal{E})$. Spectral graph theory investigates the structural properties of graphs through the eigenvalues and eigenvectors of associated matrices, providing the foundation for **Spectral Clustering** and Laplacian Eigenmaps.

### The Graph Adjacency, Degree, and Laplacian Matrices

Let $\mathcal{G}$ be an undirected, weighted graph with $n$ vertices.
1. **Adjacency (Affinity) Matrix $\mathbf{W} \in \mathbb{R}^{n \times n}$**:
   For continuous spatial data, weights are typically constructed via a Gaussian radial basis function (RBF) kernel:
   $$W_{ij} = \exp\left( -\frac{\|\mathbf{x}_i - \mathbf{x}_j\|_2^2}{2 \sigma^2} \right) \quad \text{for } i \ne j, \quad W_{ii} = 0$$
2. **Degree Matrix $\mathbf{D} \in \mathbb{R}^{n \times n}$**:
   A diagonal matrix containing the degree (total connectivity weight) of each vertex:
   $$D_{ii} = d_i = \sum_{j=1}^n W_{ij}$$
3. **Unnormalized Graph Laplacian $\mathbf{L} \in \mathbb{R}^{n \times n}$**:
   $$\mathbf{L} = \mathbf{D} - \mathbf{W}$$

#### Fundamental Mathematical Properties of the Graph Laplacian:
1. **Quadratic Energy Form**:
   For any vector $\mathbf{f} \in \mathbb{R}^n$:
   $$\mathbf{f}^\top \mathbf{L} \mathbf{f} = \mathbf{f}^\top \mathbf{D} \mathbf{f} - \mathbf{f}^\top \mathbf{W} \mathbf{f} = \sum_{i=1}^n d_i f_i^2 - \sum_{i, j=1}^n f_i f_j W_{ij}$$
   $$= \frac{1}{2} \left[ \sum_{i=1}^n \left( \sum_{j=1}^n W_{ij} \right) f_i^2 - 2 \sum_{i, j=1}^n f_i f_j W_{ij} + \sum_{j=1}^n \left( \sum_{i=1}^n W_{ij} \right) f_j^2 \right]$$
   $$= \frac{1}{2} \sum_{i, j=1}^n W_{ij} (f_i - f_j)^2 \ge 0$$
   Because $W_{ij} \ge 0$, the quadratic form is strictly non-negative, proving that $\mathbf{L}$ is **symmetric positive semi-definite (PSD)**.

2. **Trivial Eigenvalue and Multiplicity**:
   Notice that $\mathbf{L} \mathbf{1}_n = \mathbf{D} \mathbf{1}_n - \mathbf{W} \mathbf{1}_n = \mathbf{d} - \mathbf{d} = \mathbf{0}$.
   Therefore, $\lambda_1 = 0$ is always an eigenvalue of $\mathbf{L}$ with corresponding eigenvector $\mathbf{v}_1 = \mathbf{1}_n$.
   **Connected Components Theorem**: The multiplicity $k$ of the eigenvalue $\lambda = 0$ equals the exact number of connected components in the graph $\mathcal{G}$.

### Normalized Graph Laplacians and Normalized Cuts

In graph partitioning, dividing a graph into disjoint subsets $A$ and $B$ by minimizing the cross-cluster edge weights $\text{cut}(A, B) = \sum_{i \in A, j \in B} W_{ij}$ suffers from a severe size bias: it frequently isolates a single outlier vertex.
To enforce balanced clusters, Jianbo Shi and Jitendra Malik (2000) formulated the **Normalized Cut (NCut)** problem, which relaxes to finding the eigenvectors of the **Symmetric Normalized Laplacian**:

$$\mathbf{L}_{sym} = \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{W} \mathbf{D}^{-1/2}$$

#### The Ng–Jordan–Weiss (NJW) Spectral Clustering Algorithm:
1. Form affinity matrix $\mathbf{W}$ and degree matrix $\mathbf{D}$.
2. Compute the normalized Laplacian $\mathbf{L}_{sym} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{W} \mathbf{D}^{-1/2}$.
3. Compute the $k$ smallest eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_k$ of $\mathbf{L}_{sym}$.
4. Construct matrix $\mathbf{U} \in \mathbb{R}^{n \times k}$ and normalize its rows to unit Euclidean length: $Y_{ij} = U_{ij} / \|\mathbf{U}_{i, :}\|_2$.
5. Cluster the rows of $\mathbf{Y}$ into $k$ groups using standard $k$-means.

Spectral clustering maps complex, non-linearly separable manifold structures (e.g. concentric circles or intertwining spirals) into linearly separable orthogonal coordinates, demonstrating the immense power of numerical linear algebra in exploratory data science.

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

---

## 4.10 Randomized Linear Algebra: Fast Matrix Multiplication and Leverage Score Sampling

When massive datasets contain billions of rows ($n = 10^9$), even $\mathcal{O}(n p)$ algorithms strain disk I/O and CPU memory bus bandwidth. The field of **Randomized Numerical Linear Algebra (RandNLA)**, pioneered by Petros Drineas and Michael Mahoney (2006), uses non-uniform probability sampling to approximate matrix multiplication and linear regression with provable theoretical error bounds.

### Randomized Matrix Multiplication via Importance Sampling

Suppose we wish to compute the matrix product $\mathbf{C} = \mathbf{A} \mathbf{B}$, where $\mathbf{A} \in \mathbb{R}^{m \times n}$ and $\mathbf{B} \in \mathbb{R}^{n \times p}$.
The exact matrix product is the sum of $n$ outer products of columns of $\mathbf{A}$ and rows of $\mathbf{B}$:
$$\mathbf{A} \mathbf{B} = \sum_{k=1}^n \mathbf{A}_{*, k} \mathbf{B}_{k, *}$$
Evaluating this exact sum requires $2 m n p$ FLOPs.

RandNLA approximates $\mathbf{A} \mathbf{B}$ by sampling a small subset of $c \ll n$ column-row pairs according to non-uniform sampling probabilities $p_k$:

$$p_k = \frac{\|\mathbf{A}_{*, k}\|_2 \|\mathbf{B}_{k, *}\|_2}{\sum_{j=1}^n \|\mathbf{A}_{*, j}\|_2 \|\mathbf{B}_{j, *}\|_2}, \quad \sum_{k=1}^n p_k = 1$$

The randomized estimator constructs sampled matrices $\mathbf{S} \in \mathbb{R}^{m \times c}$ and $\mathbf{R} \in \mathbb{R}^{c \times p}$, scaling each sampled pair by $\frac{1}{\sqrt{c \cdot p_{i_t}}}$:

$$\mathbf{C}_{approx} = \mathbf{S} \mathbf{R} = \frac{1}{c} \sum_{t=1}^c \frac{\mathbf{A}_{*, i_t} \mathbf{B}_{i_t, *}}{p_{i_t}}$$

#### Mathematical Properties:
1. **Strict Unbiasedness**:
   $$\mathbb{E}[\mathbf{C}_{approx}] = \frac{1}{c} \sum_{t=1}^c \sum_{k=1}^n p_k \left( \frac{\mathbf{A}_{*, k} \mathbf{B}_{k, *}}{p_k} \right) = \sum_{k=1}^n \mathbf{A}_{*, k} \mathbf{B}_{k, *} = \mathbf{A} \mathbf{B}$$
2. **Minimal Variance Optimality**:
   Drineas and Mahoney proved that sampling probabilities $p_k \propto \|\mathbf{A}_{*, k}\|_2 \|\mathbf{B}_{k, *}\|_2$ **minimize the Frobenius norm variance $\mathbb{E}[\|\mathbf{A}\mathbf{B} - \mathbf{S}\mathbf{R}\|_F^2]$**.
   The expected approximation error satisfies:
   $$\mathbb{E}[\|\mathbf{A} \mathbf{B} - \mathbf{S} \mathbf{R}\|_F] \le \frac{1}{\sqrt{c}} \|\mathbf{A}\|_F \|\mathbf{B}\|_F$$

### Statistical Leverage Score Sampling for Terabyte Regression

In massive linear regression $\min_{\boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2$ where $\mathbf{X} \in \mathbb{R}^{n \times p}$ has $n = 10^8$ rows, standard OLS is too slow.

Uniform random downsampling of rows introduces severe bias if high-leverage outliers are missed. RandNLA solves this using **Statistical Leverage Score Sampling**:
- Let $\mathbf{X} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top$ be the thin SVD of $\mathbf{X}$.
- The leverage score of row $i$ is the squared Euclidean norm of the $i$-th row of the left singular matrix $\mathbf{U}$:
  $$h_i = \|\mathbf{U}_{i, :}\|_2^2 = \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top, \quad \sum_{i=1}^n h_i = p$$
- Sample $r = \mathcal{O}(p \log p / \epsilon^2)$ rows from $(\mathbf{X}, \mathbf{y})$ with non-uniform probabilities:
  $$\pi_i = \frac{h_i}{p}$$
- Solve the weighted least squares regression on the tiny $r \times p$ sample:
  $$\hat{\boldsymbol{\beta}}_{sub} = (\tilde{\mathbf{X}}^\top \tilde{\mathbf{X}})^{-1} \tilde{\mathbf{X}}^\top \tilde{\mathbf{y}}$$

Drineas, Mahoney, and Muthukrishnan (2006) proved that the subsampled solution satisfies the **Relative-Error Guarantee**:

$$\|\mathbf{y} - \mathbf{X} \hat{\boldsymbol{\beta}}_{sub}\|_2 \le (1 + \epsilon) \|\mathbf{y} - \mathbf{X} \hat{\boldsymbol{\beta}}_{OLS}\|_2$$

with probability at least $0.99$, reducing the computational workload from hours to fractions of a second while guaranteeing near-optimal prediction accuracy.

---

## 4.11 Multiway Data Analysis: Tensor Decompositions (CP and Tucker)

In contemporary statistical applications—including neuroimaging (electroencephalogram and fMRI arrays: subjects $\times$ time points $\times$ electrode channels), multi-omic single-cell genomics, and chemometric multi-way fluorescence spectroscopy—observations are naturally structured as higher-order multidimensional arrays: **Tensors**.

A tensor $\boldsymbol{\mathcal{X}} \in \mathbb{R}^{I_1 \times I_2 \times \dots \times I_N}$ is an $N$-way array, where $N$ denotes the order (number of modes). Classical 2D matrix factorizations (SVD, PCA) flatten higher-order structures into 2D matrices, destroying multidimensional spatio-temporal correlations. Multiway data analysis generalizes matrix decompositions to tensors via two canonical frameworks: **CANDECOMP/PARAFAC (CP)** and the **Tucker Decomposition**.

### The CANDECOMP/PARAFAC (CP) Decomposition

Introduced by J. Douglas Carroll and Jih-Jie Chang (1970) as CANDECOMP, and independently by Richard Harshman (1970) as PARAFAC (Parallel Factor Analysis), the **CP Decomposition** factorizes an $N$-way tensor into a sum of $R$ rank-one component tensors.

For a 3rd-order tensor $\boldsymbol{\mathcal{X}} \in \mathbb{R}^{I \times J \times K}$:

$$\boldsymbol{\mathcal{X}} \approx \sum_{r=1}^R \lambda_r (\mathbf{a}_r \circ \mathbf{b}_r \circ \mathbf{c}_r)$$

where:
- $\circ$ denotes the vector outer product: $(\mathbf{a}_r \circ \mathbf{b}_r \circ \mathbf{c}_r)_{ijk} = a_{ir} b_{jr} c_{kr}$.
- $\mathbf{A} = [\mathbf{a}_1, \dots, \mathbf{a}_R] \in \mathbb{R}^{I \times R}$, $\mathbf{B} = [\mathbf{b}_1, \dots, \mathbf{b}_R] \in \mathbb{R}^{J \times R}$, and $\mathbf{C} = [\mathbf{c}_1, \dots, \mathbf{c}_R] \in \mathbb{R}^{K \times R}$ are the **factor loading matrices** for modes 1, 2, and 3.
- $R$ is the **tensor rank**.

#### The Uniqueness Theorem (Kruskal, 1977):
A foundational mathematical virtue of the CP decomposition is its **essential uniqueness**. In standard 2D matrix SVD, factor matrices can be arbitrarily rotated ($\mathbf{X} = (\mathbf{U} \mathbf{Q}) (\mathbf{Q}^\top \mathbf{V}^\top)$). 
In stark contrast, Joseph Kruskal proved that if the sum of the $k$-ranks (Kruskal ranks) of the factor matrices satisfies:
$$k_{\mathbf{A}} + k_{\mathbf{B}} + k_{\mathbf{C}} \ge 2 R + 2$$
then the CP decomposition is **strictly unique up to trivial permutation and scaling of components**! Zero rotational ambiguity. Components extracted from a CP decomposition represent genuine, unmixed physical signals.

#### Optimization via Alternating Least Squares (ALS):
The CP model is fitted by minimizing the squared Frobenius norm error $\|\boldsymbol{\mathcal{X}} - \sum \lambda_r \mathbf{a}_r \circ \mathbf{b}_r \circ \mathbf{c}_r\|_F^2$. The algorithm alternates between updating $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{C}$ via regularized least squares using the Khatri–Rao column-wise Kronecker product:
$$\mathbf{A} \leftarrow \mathbf{X}_{(1)} (\mathbf{C} \odot \mathbf{B}) [(\mathbf{C}^\top \mathbf{C}) * (\mathbf{B}^\top \mathbf{B})]^{-1}$$
where $\odot$ denotes the Khatri–Rao product and $*$ denotes the Hadamard element-wise product.

### The Tucker Decomposition (Higher-Order SVD)

Formulated by Ledyard Tucker (1966), the **Tucker Decomposition** is a higher-order form of Principal Component Analysis. It decomposes a tensor into a small **core tensor** multiplied by orthogonal factor matrices along each mode:

$$\boldsymbol{\mathcal{X}} \approx \boldsymbol{\mathcal{G}} \times_1 \mathbf{A} \times_2 \mathbf{B} \times_3 \mathbf{C}$$

where:
- $\boldsymbol{\mathcal{G}} \in \mathbb{R}^{P \times Q \times R}$ is the **core tensor**, capturing interactions between latent factors across the modes.
- $\mathbf{A} \in \mathbb{R}^{I \times P}$, $\mathbf{B} \in \mathbb{R}^{J \times Q}$, and $\mathbf{C} \in \mathbb{R}^{K \times R}$ are orthogonal factor matrices ($\mathbf{A}^\top \mathbf{A} = \mathbf{I}_P$).
- $\times_n$ denotes the mode-$n$ tensor-matrix multiplication.

The **Higher-Order SVD (HOSVD)**, formalized by Lieven De Lathauwer and colleagues (2000), computes factor matrices $\mathbf{A}, \mathbf{B}, \mathbf{C}$ directly as the leading left singular vectors of the mode-$n$ unfolded matrices $\mathbf{X}_{(1)}, \mathbf{X}_{(2)}, \mathbf{X}_{(3)}$, providing optimal multilinear dimensionality reduction for massive scientific datasets.

---

## 4.12 Circulant and Toeplitz Systems: Fast Fourier Transform Matrix Inversion

In time series analysis, spatial statistics, and Gaussian Process modeling, covariance matrices $\mathbf{\Sigma} \in \mathbb{R}^{n \times n}$ exhibit translation-invariant stationarity: the covariance between observation $i$ and observation $j$ depends solely on their spatial or temporal lag $|i - j|$:

$$\Sigma_{ij} = \gamma(|i - j|)$$

A matrix with constant entries along each descending diagonal is a **Toeplitz Matrix**:

$$\mathbf{T} = \begin{bmatrix} t_0 & t_1 & t_2 & \dots & t_{n-1} \\ t_{-1} & t_0 & t_1 & \dots & t_{n-2} \\ t_{-2} & t_{-1} & t_0 & \dots & t_{n-3} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ t_{-(n-1)} & t_{-(n-2)} & t_{-(n-3)} & \dots & t_0 \end{bmatrix}$$

Solving a generic linear system $\mathbf{A} \mathbf{x} = \mathbf{b}$ via standard Cholesky or LU decomposition requires $\mathcal{O}(n^3)$ operations. For Toeplitz systems, specialized fast algorithms exploit structural symmetry to achieve dramatic computational speedups:
- **Levinson–Durbin Algorithm**: Solves Toeplitz systems in $\mathcal{O}(n^2)$ operations.
- **Superfast Toeplitz Inversion**: Divides and conquers in $\mathcal{O}(n \log^2 n)$ operations.

### Circulant Matrices and Spectral Diagonalization via FFT

A special subclass of Toeplitz matrices is the **Circulant Matrix** $\mathbf{C} \in \mathbb{R}^{n \times n}$, where each row is a cyclic right shift of the preceding row:

$$\mathbf{C} = \begin{bmatrix} c_0 & c_1 & c_2 & \dots & c_{n-1} \\ c_{n-1} & c_0 & c_1 & \dots & c_{n-2} \\ c_{n-2} & c_{n-1} & c_0 & \dots & c_{n-3} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ c_1 & c_2 & c_3 & \dots & c_0 \end{bmatrix}$$

#### The Fundamental Spectral Theorem of Circulant Matrices:
Circulant matrices possess an extraordinary mathematical property: **every circulant matrix of size $n$ is diagonalized by the identical, universal Discrete Fourier Transform (DFT) Matrix $\mathbf{F}_n$**!

The entries of the normalized DFT matrix $\mathbf{F} \in \mathbb{C}^{n \times n}$ are:
$$F_{jk} = \frac{1}{\sqrt{n}} \omega^{j k}, \quad \omega = e^{-2\pi i / n}$$
where $i = \sqrt{-1}$.
The matrix $\mathbf{F}$ is unitary ($\mathbf{F}^H \mathbf{F} = \mathbf{I}$, where $H$ denotes conjugate transpose).

Any circulant matrix $\mathbf{C}$ admits the exact spectral decomposition:

$$\mathbf{C} = \mathbf{F}^H \boldsymbol{\Lambda} \mathbf{F}$$

where the diagonal eigenvalue matrix $\boldsymbol{\Lambda} = \text{diag}(\lambda_0, \dots, \lambda_{n-1})$ is computed by taking the **Fast Fourier Transform (FFT)** of the first column $\mathbf{c}_0$:

$$\boldsymbol{\lambda} = \sqrt{n} \, \mathbf{F} \mathbf{c}_0 = \text{FFT}(\mathbf{c}_0)$$

#### Ultra-Fast Circulant Inversion and Matrix-Vector Multiplication:
1. **Matrix-Vector Multiplication ($\mathbf{y} = \mathbf{C} \mathbf{x}$)**:
   $$\mathbf{y} = \mathbf{F}^H \boldsymbol{\Lambda} \mathbf{F} \mathbf{x} = \text{IFFT}(\text{FFT}(\mathbf{c}_0) \odot \text{FFT}(\mathbf{x}))$$
   where $\odot$ denotes element-wise product.
   This executes in **strictly $\mathcal{O}(n \log n)$ time** via the Fast Fourier Transform, rather than $\mathcal{O}(n^2)$!
2. **System Inversion ($\mathbf{C} \mathbf{x} = \mathbf{b}$)**:
   $$\mathbf{x} = \mathbf{C}^{-1} \mathbf{b} = \mathbf{F}^H \boldsymbol{\Lambda}^{-1} \mathbf{F} \mathbf{b} = \text{IFFT}\left( \frac{\text{FFT}(\mathbf{b})}{\text{FFT}(\mathbf{c}_0)} \right)$$
   Inverting a circulant system requires only two FFT calls, executing in **$\mathcal{O}(n \log n)$ operations**!

### Embedding Toeplitz Matrices into Circulant Structures
To solve an arbitrary Toeplitz system $\mathbf{T} \mathbf{x} = \mathbf{b}$ using the ultra-fast $\mathcal{O}(n \log n)$ FFT machinery, Wood and Chan (1994) developed the **Circulant Embedding Technique**:
- Embed the $n \times n$ Toeplitz matrix $\mathbf{T}$ as the upper-left block of an augmented $2n \times 2n$ circulant matrix $\tilde{\mathbf{C}}$:
  $$\tilde{\mathbf{C}} = \begin{bmatrix} \mathbf{T} & \mathbf{B} \\ \mathbf{B} & \mathbf{T} \end{bmatrix}$$
Evaluating Gaussian process likelihoods and simulating stationary spatial fields across $n = 1,000,000$ points executes in seconds using FFT circulant embedding, representing one of the greatest triumphs of numerical algorithms in spatial statistics.



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
