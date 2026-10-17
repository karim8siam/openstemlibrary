# Unit 3: Normal-Sample Theory, Quadratic Forms, and Exact Sampling Distributions

## 3.1 The Multivariate Normal Distribution: Definitions, Characteristic Functions, and Affine Invariance

The multivariate normal (Gaussian) distribution occupies a preeminent position in mathematical statistics. It serves not only as the exact sampling model for many physical measurements, but also as the universal limiting distribution for properly normalized sample sums and linear estimators via the multidimensional Central Limit Theorem.

Let $\mathbf{X} = (X_1, X_2, \dots, X_n)^T$ be an $n$-dimensional random vector defined on a probability space $(\Omega, \mathcal{F}, P)$. There are several mathematically equivalent ways to define the multivariate normal distribution:

1. **Affine Transformation Definition (Constructive Definition)**: The random vector $\mathbf{X}$ is said to follow a multivariate normal distribution if there exists a $k$-dimensional vector of independent standard normal random variables $\mathbf{Z} = (Z_1, \dots, Z_k)^T \sim \mathcal{N}_k(\mathbf{0}, \mathbf{I}_k)$, an $n \times k$ deterministic real matrix $\mathbf{A}$, and an $n$-dimensional deterministic vector $\boldsymbol{\mu} \in \mathbb{R}^n$, such that:
   $$\mathbf{X} = \mathbf{A} \mathbf{Z} + \boldsymbol{\mu}$$
   Under this representation, the mean vector is $\mathbb{E}[\mathbf{X}] = \boldsymbol{\mu}$, and the covariance matrix is:
   $$\boldsymbol{\Sigma} = \text{Cov}(\mathbf{X}) = \mathbb{E}\left[ (\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T \right] = \mathbf{A} \mathbb{E}[\mathbf{Z} \mathbf{Z}^T] \mathbf{A}^T = \mathbf{A} \mathbf{I}_k \mathbf{A}^T = \mathbf{A} \mathbf{A}^T$$
   The resulting covariance matrix $\boldsymbol{\Sigma}$ is symmetric and positive semi-definite of rank at most $\min(n, k)$.
2. **Linear Combination Definition (Cramér-Wold Device)**: The random vector $\mathbf{X}$ is multivariate normal if and only if for every deterministic constant vector $\mathbf{c} = (c_1, \dots, c_n)^T \in \mathbb{R}^n$, the scalar linear combination:
   $$Y = \mathbf{c}^T \mathbf{X} = \sum_{i=1}^n c_i X_i$$
   follows a univariate normal distribution:
   $$Y \sim \mathcal{N}(\mathbf{c}^T \boldsymbol{\mu}, \; \mathbf{c}^T \boldsymbol{\Sigma} \mathbf{c})$$
   (where a normal distribution with variance zero is understood as a degenerate point mass at its mean). This definition provides an immediate criterion for testing multivariate normality.
3. **Characteristic Function Definition**: The random vector $\mathbf{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ has joint characteristic function defined for all $\mathbf{t} \in \mathbb{R}^n$ by:
   $$\phi_{\mathbf{X}}(\mathbf{t}) = \mathbb{E}\left[ e^{i \mathbf{t}^T \mathbf{X}} \right] = \exp\left( i \mathbf{t}^T \boldsymbol{\mu} - \frac{1}{2} \mathbf{t}^T \boldsymbol{\Sigma} \mathbf{t} \right)$$
   This characteristic function exists universally, regardless of whether $\boldsymbol{\Sigma}$ is non-singular or singular (degenerate).

### The Non-Singular Probability Density Function
When the covariance matrix $\boldsymbol{\Sigma}$ is strictly positive-definite (denoted $\boldsymbol{\Sigma} \succ 0$), its determinant $\det(\boldsymbol{\Sigma}) > 0$ is strictly positive, and its matrix inverse $\boldsymbol{\Sigma}^{-1}$ exists. In this case, the multivariate normal distribution is absolutely continuous with respect to the $n$-dimensional Lebesgue measure, possessing the joint probability density function:

$$f_{\mathbf{X}}(\mathbf{x}; \boldsymbol{\mu}, \boldsymbol{\Sigma}) = \frac{1}{(2\pi)^{n/2} \det(\boldsymbol{\Sigma})^{1/2}} \exp\left( -\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)$$

for all $\mathbf{x} \in \mathbb{R}^n$. The contours of constant probability density correspond to ellipsoids defined by the quadratic form $(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) = c^2$, known as Mahalanobis ellipsoids. The principal axes of these ellipsoids align precisely with the eigenvectors of $\boldsymbol{\Sigma}$, and their semi-axis lengths are proportional to the square roots of the corresponding eigenvalues.

### Affine Invariance Property
A cornerstone property of the Gaussian family is its closure under affine transformations.

**Theorem (Affine Invariance)**: Let $\mathbf{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, and let $\mathbf{B}$ be an $m \times n$ real matrix and $\mathbf{d} \in \mathbb{R}^m$ a constant vector. Then the transformed vector $\mathbf{Y} = \mathbf{B} \mathbf{X} + \mathbf{d}$ follows an $m$-dimensional multivariate normal distribution:

$$\mathbf{Y} \sim \mathcal{N}_m(\mathbf{B} \boldsymbol{\mu} + \mathbf{d}, \; \mathbf{B} \boldsymbol{\Sigma} \mathbf{B}^T)$$

**Proof**:
Using the characteristic function definition, for any $\mathbf{s} \in \mathbb{R}^m$:
$$\phi_{\mathbf{Y}}(\mathbf{s}) = \mathbb{E}\left[ e^{i \mathbf{s}^T (\mathbf{B} \mathbf{X} + \mathbf{d})} \right] = e^{i \mathbf{s}^T \mathbf{d}} \mathbb{E}\left[ e^{i (\mathbf{B}^T \mathbf{s})^T \mathbf{X}} \right] = e^{i \mathbf{s}^T \mathbf{d}} \phi_{\mathbf{X}}(\mathbf{B}^T \mathbf{s})$$
Substituting the known characteristic function of $\mathbf{X}$:
$$\phi_{\mathbf{Y}}(\mathbf{s}) = e^{i \mathbf{s}^T \mathbf{d}} \exp\left( i (\mathbf{B}^T \mathbf{s})^T \boldsymbol{\mu} - \frac{1}{2} (\mathbf{B}^T \mathbf{s})^T \boldsymbol{\Sigma} (\mathbf{B}^T \mathbf{s}) \right) = \exp\left( i \mathbf{s}^T (\mathbf{B} \boldsymbol{\mu} + \mathbf{d}) - \frac{1}{2} \mathbf{s}^T (\mathbf{B} \boldsymbol{\Sigma} \mathbf{B}^T) \mathbf{s} \right)$$
By the uniqueness theorem for characteristic functions, $\mathbf{Y}$ is uniquely identified as an $m$-variate normal vector with mean vector $\mathbf{B} \boldsymbol{\mu} + \mathbf{d}$ and covariance matrix $\mathbf{B} \boldsymbol{\Sigma} \mathbf{B}^T$. $\blacksquare$

## 3.2 Uncorrelatedness and Independence in Gaussian Vectors

In general probability theory, two random variables being uncorrelated ($\text{Cov}(X, Y) = 0$) does not imply that they are stochastically independent. A standard counterexample is $X \sim \mathcal{N}(0, 1)$ and $Y = X^2$: since the third moment of a standard normal is zero, $\text{Cov}(X, Y) = \mathbb{E}[X^3] - \mathbb{E}[X]\mathbb{E}[X^2] = 0$, yet $Y$ is a deterministic function of $X$ and thus completely dependent.

However, when random variables are **jointly** multivariate normal, the situation simplifies completely.

**Theorem (Independence via Zero Covariance)**: Let $\mathbf{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$. Partition $\mathbf{X}$ into two sub-vectors $\mathbf{X}_1 \in \mathbb{R}^{n_1}$ and $\mathbf{X}_2 \in \mathbb{R}^{n_2}$ (with $n_1 + n_2 = n$), with corresponding partitioned mean vector and covariance matrix:

$$\mathbf{X} = \begin{pmatrix} \mathbf{X}_1 \\ \mathbf{X}_2 \end{pmatrix}, \quad \boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \quad \boldsymbol{\Sigma} = \begin{pmatrix} \boldsymbol{\Sigma}_{11} & \boldsymbol{\Sigma}_{12} \\ \boldsymbol{\Sigma}_{21} & \boldsymbol{\Sigma}_{22} \end{pmatrix}$$

Then $\mathbf{X}_1$ and $\mathbf{X}_2$ are statistically independent if and only if their cross-covariance matrix vanishes identically:

$$\boldsymbol{\Sigma}_{12} = \text{Cov}(\mathbf{X}_1, \mathbf{X}_2) = \mathbf{0}$$

**Proof**:
If $\mathbf{X}_1$ and $\mathbf{X}_2$ are independent, then by definition $\text{Cov}(\mathbf{X}_1, \mathbf{X}_2) = \mathbf{0}$, establishing necessity.
To prove sufficiency, suppose $\boldsymbol{\Sigma}_{12} = \mathbf{0}$ (which also implies $\boldsymbol{\Sigma}_{21} = \boldsymbol{\Sigma}_{12}^T = \mathbf{0}$). Then the covariance matrix is block-diagonal:
$$\boldsymbol{\Sigma} = \begin{pmatrix} \boldsymbol{\Sigma}_{11} & \mathbf{0} \\ \mathbf{0} & \boldsymbol{\Sigma}_{22} \end{pmatrix}$$
Let $\mathbf{t} = (\mathbf{t}_1^T, \mathbf{t}_2^T)^T \in \mathbb{R}^n$, where $\mathbf{t}_1 \in \mathbb{R}^{n_1}$ and $\mathbf{t}_2 \in \mathbb{R}^{n_2}$. The joint characteristic function of $\mathbf{X}$ is:
$$\phi_{\mathbf{X}}(\mathbf{t}) = \exp\left( i \mathbf{t}^T \boldsymbol{\mu} - \frac{1}{2} \mathbf{t}^T \boldsymbol{\Sigma} \mathbf{t} \right) = \exp\left( i \mathbf{t}_1^T \boldsymbol{\mu}_1 + i \mathbf{t}_2^T \boldsymbol{\mu}_2 - \frac{1}{2} (\mathbf{t}_1^T \boldsymbol{\Sigma}_{11} \mathbf{t}_1 + \mathbf{t}_2^T \boldsymbol{\Sigma}_{22} \mathbf{t}_2) \right)$$
Using the exponential addition law $\exp(a + b) = \exp(a) \exp(b)$, the characteristic function factorizes:
$$\phi_{\mathbf{X}}(\mathbf{t}_1, \mathbf{t}_2) = \exp\left( i \mathbf{t}_1^T \boldsymbol{\mu}_1 - \frac{1}{2} \mathbf{t}_1^T \boldsymbol{\Sigma}_{11} \mathbf{t}_1 \right) \cdot \exp\left( i \mathbf{t}_2^T \boldsymbol{\mu}_2 - \frac{1}{2} \mathbf{t}_2^T \boldsymbol{\Sigma}_{22} \mathbf{t}_2 \right) = \phi_{\mathbf{X}_1}(\mathbf{t}_1) \cdot \phi_{\mathbf{X}_2}(\mathbf{t}_2)$$
Because the joint characteristic function factorizes into the product of the marginal characteristic functions for all $\mathbf{t}_1$ and $\mathbf{t}_2$, the random vectors $\mathbf{X}_1$ and $\mathbf{X}_2$ are strictly independent. $\blacksquare$

This theorem has immense practical significance: to prove that two linear combinations or projections of a Gaussian random vector are statistically independent, it is necessary and sufficient to demonstrate that their covariance is zero.

## 3.3 Quadratic Forms in Normal Vectors: Matrix Algebra and Spectral Representations

In linear models, regression diagnostics, and analysis of variance, test statistics (such as sums of squared residuals, explained sums of squares, and Wald statistics) take the mathematical form of **quadratic forms**.

Let $\mathbf{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ be a Gaussian random vector, and let $\mathbf{A}$ be an $n \times n$ real symmetric matrix ($\mathbf{A} = \mathbf{A}^T$). A **quadratic form** in $\mathbf{X}$ is a scalar random variable defined by:

$$Q = \mathbf{X}^T \mathbf{A} \mathbf{X} = \sum_{i=1}^n \sum_{j=1}^n a_{ij} X_i X_j$$

If $\mathbf{A}$ were not initially symmetric, we could replace it without changing the value of $Q$ by its symmetric part $\frac{1}{2}(\mathbf{A} + \mathbf{A}^T)$, since $\mathbf{X}^T \mathbf{A} \mathbf{X} = \mathbf{X}^T \left(\frac{\mathbf{A} + \mathbf{A}^T}{2}\right) \mathbf{X}$. Thus, symmetry of $\mathbf{A}$ is assumed throughout without loss of generality.

### First and Second Moments of Quadratic Forms
To compute the expectation of $Q = \mathbf{X}^T \mathbf{A} \mathbf{X}$, we utilize the trace operator $\text{tr}(\cdot)$, which satisfies cyclic commutativity: $\text{tr}(\mathbf{B} \mathbf{C}) = \text{tr}(\mathbf{C} \mathbf{B})$ for any matrices of compatible dimensions. Because $Q$ is a scalar ($1 \times 1$ matrix), it equals its own trace:

$$\mathbb{E}[Q] = \mathbb{E}\left[ \text{tr}(\mathbf{X}^T \mathbf{A} \mathbf{X}) \right] = \mathbb{E}\left[ \text{tr}(\mathbf{A} \mathbf{X} \mathbf{X}^T) \right] = \text{tr}\left( \mathbf{A} \mathbb{E}[\mathbf{X} \mathbf{X}^T] \right)$$

Recalling that the second moment matrix is $\mathbb{E}[\mathbf{X} \mathbf{X}^T] = \boldsymbol{\Sigma} + \boldsymbol{\mu} \boldsymbol{\mu}^T$:

$$\mathbb{E}[\mathbf{X}^T \mathbf{A} \mathbf{X}] = \text{tr}\left( \mathbf{A} (\boldsymbol{\Sigma} + \boldsymbol{\mu} \boldsymbol{\mu}^T) \right) = \text{tr}(\mathbf{A} \boldsymbol{\Sigma}) + \text{tr}(\mathbf{A} \boldsymbol{\mu} \boldsymbol{\mu}^T) = \text{tr}(\mathbf{A} \boldsymbol{\Sigma}) + \boldsymbol{\mu}^T \mathbf{A} \boldsymbol{\mu}$$

This moment formula holds universally for any random vector $\mathbf{X}$ with mean $\boldsymbol{\mu}$ and covariance $\boldsymbol{\Sigma}$, regardless of normality.

When $\mathbf{X}$ is Gaussian, higher-order moments can also be evaluated. The exact variance of the quadratic form is:

$$\text{Var}(\mathbf{X}^T \mathbf{A} \mathbf{X}) = 2 \text{tr}(\mathbf{A} \boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\Sigma}) + 4 \boldsymbol{\mu}^T \mathbf{A} \boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\mu}$$

Furthermore, if $\mathbf{B}$ is another $n \times n$ symmetric matrix defining a second quadratic form $\mathbf{X}^T \mathbf{B} \mathbf{X}$, their covariance is:

$$\text{Cov}(\mathbf{X}^T \mathbf{A} \mathbf{X}, \; \mathbf{X}^T \mathbf{B} \mathbf{X}) = 2 \text{tr}(\mathbf{A} \boldsymbol{\Sigma} \mathbf{B} \boldsymbol{\Sigma}) + 4 \boldsymbol{\mu}^T \mathbf{A} \boldsymbol{\Sigma} \mathbf{B} \boldsymbol{\mu}$$

## 3.4 The Chi-Square Distribution: Derivation, Reproductive Properties, and MGF

The most foundational sampling distribution for quadratic forms is the **Chi-Square distribution** ($\chi^2$).

### Derivation from the Standard Normal Distribution
Let $Z \sim \mathcal{N}(0, 1)$ be a standard univariate normal random variable. Define $Y = Z^2$. The cumulative distribution function of $Y$ for $y > 0$ is:

$$F_Y(y) = P(Y \le y) = P(Z^2 \le y) = P(-\sqrt{y} \le Z \le \sqrt{y}) = 2 \Phi(\sqrt{y}) - 1$$

where $\Phi(z) = \int_{-\infty}^z \frac{1}{\sqrt{2\pi}} e^{-u^2/2} \, du$ is the standard normal CDF. Differentiating with respect to $y$ via the Leibniz rule:

$$f_Y(y) = \frac{d}{dy} [2 \Phi(\sqrt{y}) - 1] = 2 \phi(\sqrt{y}) \cdot \frac{d}{dy}(\sqrt{y}) = 2 \left( \frac{1}{\sqrt{2\pi}} e^{-y/2} \right) \left( \frac{1}{2\sqrt{y}} \right) = \frac{1}{\sqrt{2\pi}} y^{-1/2} e^{-y/2}$$

Recalling that $\Gamma(1/2) = \sqrt{\pi}$, we can rewrite the normalizing constant:

$$f_Y(y) = \frac{1}{2^{1/2} \Gamma(1/2)} y^{\frac{1}{2} - 1} e^{-y/2}, \quad y > 0$$

This is precisely the probability density function of a Gamma distribution with shape parameter $\alpha = 1/2$ and rate parameter $\beta = 1/2$. This distribution is designated as the **Chi-Square distribution with 1 degree of freedom**, denoted $\chi_1^2$:

$$Z^2 \sim \chi_1^2 \equiv \text{Gamma}\left(\frac{1}{2}, \frac{1}{2}\right)$$

### Sum of Independent Squared Standard Normal Variates
Now, let $Z_1, Z_2, \dots, Z_k$ be mutually independent standard normal random variables: $\mathbf{Z} \sim \mathcal{N}_k(\mathbf{0}, \mathbf{I}_k)$. Define the sum of their squares:

$$U = \sum_{i=1}^k Z_i^2 = \mathbf{Z}^T \mathbf{Z} = \|\mathbf{Z}\|^2$$

The moment generating function of $Z_i^2 \sim \chi_1^2$ is:

$$M_{Z_i^2}(t) = \mathbb{E}\left[ e^{t Z_i^2} \right] = (1 - 2t)^{-1/2} \quad \text{for } t < 1/2$$

By mutual independence, the MGF of the sum $U = \sum_{i=1}^k Z_i^2$ is the product of the individual MGFs:

$$M_U(t) = \prod_{i=1}^k M_{Z_i^2}(t) = \prod_{i=1}^k (1 - 2t)^{-1/2} = (1 - 2t)^{-k/2}, \quad t < 1/2$$

By the MGF Uniqueness Theorem, $U$ follows a Gamma distribution with shape $\alpha = k/2$ and rate $\beta = 1/2$. This distribution is the **Chi-Square distribution with $k$ degrees of freedom**, denoted $\chi_k^2$. Its probability density function is:

$$f_U(u; k) = \frac{1}{2^{k/2} \Gamma(k/2)} u^{\frac{k}{2} - 1} e^{-u/2}, \quad u > 0$$

and zero for $u \le 0$.

### Fundamental Properties of the $\chi_k^2$ Distribution
1. **Mean and Variance**:
   $$\mathbb{E}[U] = k, \quad \text{Var}(U) = 2k$$
2. **Reproductive Property**: If $U_1 \sim \chi_{k_1}^2$ and $U_2 \sim \chi_{k_2}^2$ are independent, then:
   $$U_1 + U_2 \sim \chi_{k_1 + k_2}^2$$
3. **Asymptotic Normality**: By the classical Central Limit Theorem, as the degrees of freedom $k \to \infty$:
   $$\frac{\chi_k^2 - k}{\sqrt{2k}} \xrightarrow{d} \mathcal{N}(0, 1)$$

## 3.5 Distribution of Quadratic Forms: Idempotent Matrices and Craig's Theorem

We now establish the central theorem connecting quadratic forms in Gaussian vectors to the Chi-Square distribution.

Let $\mathbf{Z} \sim \mathcal{N}_n(\mathbf{0}, \mathbf{I}_n)$ be a vector of standard normal random variables, and let $\mathbf{A}$ be an $n \times n$ real symmetric matrix. When does the quadratic form $Q = \mathbf{Z}^T \mathbf{A} \mathbf{Z}$ follow an exact Chi-Square distribution?

**Theorem (Chi-Square Distribution of Quadratic Forms)**: The quadratic form $Q = \mathbf{Z}^T \mathbf{A} \mathbf{Z}$ follows a central Chi-Square distribution with $r$ degrees of freedom ($Q \sim \chi_r^2$) if and only if the matrix $\mathbf{A}$ is **idempotent** of rank $r$:

$$\mathbf{A}^2 = \mathbf{A} \quad \text{and} \quad \text{rank}(\mathbf{A}) = r$$

**Proof**:
Since $\mathbf{A}$ is a real symmetric matrix, the Spectral Theorem of linear algebra guarantees the existence of an orthogonal matrix $\mathbf{P}$ ($\mathbf{P}^T \mathbf{P} = \mathbf{I}_n$) such that:
$$\mathbf{A} = \mathbf{P} \boldsymbol{\Lambda} \mathbf{P}^T$$
where $\boldsymbol{\Lambda} = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$ is the diagonal matrix of real eigenvalues of $\mathbf{A}$.
Substitute this spectral decomposition into the quadratic form:
$$Q = \mathbf{Z}^T (\mathbf{P} \boldsymbol{\Lambda} \mathbf{P}^T) \mathbf{Z} = (\mathbf{P}^T \mathbf{Z})^T \boldsymbol{\Lambda} (\mathbf{P}^T \mathbf{Z})$$
Define the transformed random vector $\mathbf{W} = \mathbf{P}^T \mathbf{Z}$. Because $\mathbf{P}$ is orthogonal ($\mathbf{P}^T \mathbf{P} = \mathbf{I}_n$), the vector $\mathbf{W}$ is an orthogonal transformation of standard normals. Its distribution is:
$$\mathbf{W} \sim \mathcal{N}_n(\mathbf{0}, \; \mathbf{P}^T \mathbf{I}_n \mathbf{P}) = \mathcal{N}_n(\mathbf{0}, \mathbf{I}_n)$$
Thus, the components $W_1, W_2, \dots, W_n$ are themselves mutually independent standard normal random variables!
Expanding the quadratic form in terms of $\mathbf{W}$:
$$Q = \mathbf{W}^T \boldsymbol{\Lambda} \mathbf{W} = \sum_{i=1}^n \lambda_i W_i^2$$
Because $W_1^2, \dots, W_n^2$ are independent $\chi_1^2$ random variables, the moment generating function of $Q$ is:
$$M_Q(t) = \mathbb{E}\left[ \exp\left( t \sum_{i=1}^n \lambda_i W_i^2 \right) \right] = \prod_{i=1}^n \mathbb{E}\left[ e^{(t \lambda_i) W_i^2} \right] = \prod_{i=1}^n (1 - 2 \lambda_i t)^{-1/2}$$
For $Q$ to follow a $\chi_r^2$ distribution, its MGF must equal $(1 - 2t)^{-r/2}$. Equating the two expressions:
$$\prod_{i=1}^n (1 - 2 \lambda_i t)^{-1/2} = (1 - 2t)^{-r/2}$$
Squaring both sides and taking reciprocal squares:
$$\prod_{i=1}^n (1 - 2 \lambda_i t) = (1 - 2t)^r$$
This equality of polynomials in $t$ holds for all $t$ in a neighborhood of zero if and only if exactly $r$ of the eigenvalues $\lambda_i$ are equal to 1, and the remaining $n - r$ eigenvalues are equal to 0:
$$\lambda_i \in \{0, 1\} \quad \text{for all } i, \quad \text{with } \sum_{i=1}^n \lambda_i = r$$
A symmetric matrix whose eigenvalues are exclusively 0 and 1 is, by definition, an **orthogonal projection matrix** (symmetric idempotent matrix), satisfying $\mathbf{A}^2 = \mathbf{A}$. The number of non-zero eigenvalues equals the rank: $\text{rank}(\mathbf{A}) = \text{tr}(\mathbf{A}) = r$. This completes the proof in both directions. $\blacksquare$

### Independence of Quadratic Forms: Craig's Theorem
A companion question concerns when two quadratic forms $\mathbf{Z}^T \mathbf{A} \mathbf{Z}$ and $\mathbf{Z}^T \mathbf{B} \mathbf{Z}$ are statistically independent.

**Theorem (Craig's Theorem)**: Let $\mathbf{Z} \sim \mathcal{N}_n(\mathbf{0}, \mathbf{I}_n)$, and let $\mathbf{A}$ and $\mathbf{B}$ be $n \times n$ real symmetric matrices. The quadratic forms $Q_1 = \mathbf{Z}^T \mathbf{A} \mathbf{Z}$ and $Q_2 = \mathbf{Z}^T \mathbf{B} \mathbf{Z}$ are statistically independent if and only if the matrix product vanishes:

$$\mathbf{A} \mathbf{B} = \mathbf{0}$$

(or equivalently, $\mathbf{B} \mathbf{A} = \mathbf{0}$, since $(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T \mathbf{A}^T = \mathbf{B}\mathbf{A}$).

The condition $\mathbf{A} \mathbf{B} = \mathbf{0}$ means that the column space of $\mathbf{B}$ is contained within the null space of $\mathbf{A}$. The two projection matrices project the data vector onto mutually orthogonal subspaces of $\mathbb{R}^n$, ensuring complete stochastic independence between the resulting energy allocations.

## 3.6 Cochran's Theorem on the Decomposition of Sums of Squares

In analysis of variance (ANOVA) and linear regression, the total sum of squares $\sum_{i=1}^n X_i^2 = \mathbf{X}^T \mathbf{X}$ is partitioned into several component sums of squares:

$$\mathbf{X}^T \mathbf{X} = \mathbf{X}^T \mathbf{A}_1 \mathbf{X} + \mathbf{X}^T \mathbf{A}_2 \mathbf{X} + \dots + \mathbf{X}^T \mathbf{A}_k \mathbf{X}$$

where each $\mathbf{A}_j$ is a symmetric matrix representing a specific experimental factor or residual sum of squares. **Cochran's Theorem** provides the definitive conditions under which these component quadratic forms are mutually independent Chi-Square variates.

**Theorem (Cochran's Theorem)**: Let $\mathbf{Z} \sim \mathcal{N}_n(\mathbf{0}, \mathbf{I}_n)$, and suppose the identity matrix can be decomposed into a sum of $k$ real symmetric matrices:

$$\mathbf{I}_n = \sum_{j=1}^k \mathbf{A}_j$$

where $\text{rank}(\mathbf{A}_j) = r_j$. Then the following conditions are mathematically equivalent:
1. $\sum_{j=1}^k r_j = n$ (the sum of ranks equals the ambient dimension $n$).
2. Each matrix $\mathbf{A}_j$ is idempotent: $\mathbf{A}_j^2 = \mathbf{A}_j$ for all $j \in \{1, \dots, k\}$.
3. The matrices are pairwise orthogonal: $\mathbf{A}_j \mathbf{A}_m = \mathbf{0}$ for all $j \ne m$.
4. The quadratic forms $Q_j = \mathbf{Z}^T \mathbf{A}_j \mathbf{Z}$ are mutually independent Chi-Square random variables:
   $$Q_j \sim \chi_{r_j}^2 \quad \text{for each } j \in \{1, \dots, k\}$$

Cochran's Theorem guarantees that when the degrees of freedom partition cleanly ($\sum r_j = n$), the resulting ANOVA sums of squares are automatically independent Chi-Square variables, providing the exact theoretical justification for $F$-tests in the analysis of variance.

## 3.7 Exact Independence of Sample Mean and Sample Variance in Gaussian Samples

We are now equipped to deliver the definitive proof of the celebrated property of Gaussian samples: the sample mean $\bar{X}$ and the sample variance $S^2$ are completely independent.

Let $X_1, X_2, \dots, X_n$ be an i.i.d. random sample from $\mathcal{N}(\mu, \sigma^2)$. In vector notation, $\mathbf{X} \sim \mathcal{N}_n(\mu \mathbf{1}_n, \sigma^2 \mathbf{I}_n)$.

Define the projection matrix onto the 1-dimensional subspace spanned by $\mathbf{1}_n$:

$$\mathbf{P} = \frac{1}{n} \mathbf{1}_n \mathbf{1}_n^T$$

and define the centering projection matrix:

$$\mathbf{M} = \mathbf{I}_n - \mathbf{P} = \mathbf{I}_n - \frac{1}{n} \mathbf{1}_n \mathbf{1}_n^T$$

Observe that:
1. $\bar{X} = \frac{1}{n} \mathbf{1}_n^T \mathbf{X}$ is a linear transformation of $\mathbf{X}$.
2. The residual vector is $\mathbf{X} - \bar{X}\mathbf{1}_n = \mathbf{M} \mathbf{X}$.
3. The sample variance is $S^2 = \frac{1}{n-1} \mathbf{X}^T \mathbf{M} \mathbf{X} = \frac{1}{n-1} \|\mathbf{M}\mathbf{X}\|^2$.

Now, compute the covariance between the linear vector $\bar{X}\mathbf{1}_n = \mathbf{P}\mathbf{X}$ and the residual vector $\mathbf{M}\mathbf{X}$:

$$\text{Cov}(\mathbf{P}\mathbf{X}, \; \mathbf{M}\mathbf{X}) = \mathbf{P} \text{Cov}(\mathbf{X}) \mathbf{M}^T = \mathbf{P} (\sigma^2 \mathbf{I}_n) \mathbf{M} = \sigma^2 \mathbf{P} \mathbf{M}$$

Evaluating the matrix product $\mathbf{P} \mathbf{M}$:

$$\mathbf{P} \mathbf{M} = \mathbf{P} (\mathbf{I}_n - \mathbf{P}) = \mathbf{P} - \mathbf{P}^2 = \mathbf{P} - \mathbf{P} = \mathbf{0}$$

Since $\mathbf{X}$ is multivariate normal, and the linear transformations $\mathbf{P}\mathbf{X}$ and $\mathbf{M}\mathbf{X}$ have zero cross-covariance, they are **stochastically independent random vectors**!

Because $\bar{X}$ is a measurable function of $\mathbf{P}\mathbf{X}$ (specifically, $\bar{X} = \frac{1}{n}\mathbf{1}_n^T (\mathbf{P}\mathbf{X})$), and $S^2$ is a measurable function of $\mathbf{M}\mathbf{X}$ (specifically, $S^2 = \frac{1}{n-1} \|\mathbf{M}\mathbf{X}\|^2$), any functions of independent random vectors are themselves independent. Therefore:

$$\bar{X} \quad \text{and} \quad S^2 \quad \text{are strictly independent random variables!}$$

Furthermore, since $\mathbf{M}$ is idempotent ($\mathbf{M}^2 = \mathbf{M}$) of rank $\text{tr}(\mathbf{M}) = n - 1$:

$$\frac{(n - 1)S^2}{\sigma^2} = \left(\frac{\mathbf{X} - \mu\mathbf{1}_n}{\sigma}\right)^T \mathbf{M} \left(\frac{\mathbf{X} - \mu\mathbf{1}_n}{\sigma}\right) \sim \chi_{n-1}^2$$

Thus, in a normal sample of size $n$:
1. $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$.
2. $\frac{(n-1)S^2}{\sigma^2} \sim \chi_{n-1}^2$.
3. $\bar{X}$ and $S^2$ are statistically independent.

## 3.8 Student's t Distribution: Definition, Derivation, and Moments

In practical scientific inference, the true population variance $\sigma^2$ is rarely known. When an investigator replaces the unknown standard deviation $\sigma$ in the standardized mean $Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$ with the sample standard deviation $S$, the resulting ratio is the **Student's $t$-statistic**:

$$T = \frac{\bar{X} - \mu}{S / \sqrt{n}}$$

### General Definition of the $t$ Distribution
Let $Z \sim \mathcal{N}(0, 1)$ be a standard normal random variable, and let $V \sim \chi_\nu^2$ be a Chi-Square random variable with $\nu > 0$ degrees of freedom. Assume that $Z$ and $V$ are **independent**. The random variable:

$$T = \frac{Z}{\sqrt{V / \nu}}$$

is said to follow **Student's $t$ distribution with $\nu$ degrees of freedom**, denoted $T \sim t_\nu$.

Since in a Gaussian sample $Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0, 1)$ and $V = \frac{(n-1)S^2}{\sigma^2} \sim \chi_{n-1}^2$ are independent, the ratio:

$$\frac{Z}{\sqrt{V / (n - 1)}} = \frac{\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}}{\sqrt{\frac{(n-1)S^2}{\sigma^2 (n-1)}}} = \frac{\bar{X} - \mu}{S / \sqrt{n}}$$

follows an exact $t_{n-1}$ distribution.

### Analytical Derivation of the Probability Density Function
Because $Z$ and $V$ are independent, their joint density is the product of standard normal and Chi-Square densities:

$$f_{Z, V}(z, v) = \left( \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \right) \left( \frac{1}{2^{\nu/2} \Gamma(\nu/2)} v^{\frac{\nu}{2} - 1} e^{-v/2} \right), \quad z \in \mathbb{R}, \; v > 0$$

Define the transformation:

$$T = \frac{Z}{\sqrt{V / \nu}}, \quad W = V$$

The inverse transformation is:

$$Z = T \sqrt{\frac{W}{\nu}}, \quad V = W$$

The Jacobian matrix of the inverse mapping is:

$$J = \begin{pmatrix} \frac{\partial z}{\partial t} & \frac{\partial z}{\partial w} \\ \frac{\partial v}{\partial t} & \frac{\partial v}{\partial w} \end{pmatrix} = \begin{pmatrix} \sqrt{\frac{w}{\nu}} & \frac{t}{2\sqrt{\nu w}} \\ 0 & 1 \end{pmatrix}$$

The determinant of the Jacobian is:

$$\det(J) = \sqrt{\frac{w}{\nu}} = \frac{w^{1/2}}{\sqrt{\nu}}$$

Since $w > 0$, $|\det(J)| = w^{1/2} / \sqrt{\nu}$. The joint density of $(T, W)$ is:

$$f_{T, W}(t, w) = f_{Z, V}\left( t \sqrt{\frac{w}{\nu}}, w \right) \cdot \frac{w^{1/2}}{\sqrt{\nu}} = \frac{1}{\sqrt{2\pi \nu} 2^{\nu/2} \Gamma(\nu/2)} w^{\frac{\nu}{2} - 1 + \frac{1}{2}} \exp\left( -\frac{1}{2} w \left( 1 + \frac{t^2}{\nu} \right) \right)$$

To obtain the marginal density $f_T(t)$, integrate out $w$ over $(0, \infty)$:

$$f_T(t) = \frac{1}{\sqrt{2\pi \nu} 2^{\nu/2} \Gamma(\nu/2)} \int_0^\infty w^{\frac{\nu + 1}{2} - 1} \exp\left( -\frac{w}{2} \left( 1 + \frac{t^2}{\nu} \right) \right) \, dw$$

Make the substitution $u = \frac{w}{2}\left(1 + \frac{t^2}{\nu}\right)$, so $w = \frac{2u}{1 + t^2/\nu}$ and $dw = \frac{2 \, du}{1 + t^2/\nu}$:

$$\int_0^\infty w^{\frac{\nu + 1}{2} - 1} e^{-u} \frac{2 \, du}{1 + t^2/\nu} = \left( \frac{2}{1 + t^2/\nu} \right)^{\frac{\nu + 1}{2}} \int_0^\infty u^{\frac{\nu + 1}{2} - 1} e^{-u} \, du = \left( \frac{2}{1 + t^2/\nu} \right)^{\frac{\nu + 1}{2}} \Gamma\left( \frac{\nu + 1}{2} \right)$$

Substituting this back into $f_T(t)$ and canceling powers of 2:

$$f_T(t; \nu) = \frac{\Gamma\left( \frac{\nu + 1}{2} \right)}{\sqrt{\nu \pi} \, \Gamma\left( \frac{\nu}{2} \right)} \left( 1 + \frac{t^2}{\nu} \right)^{-\frac{\nu + 1}{2}}, \quad t \in \mathbb{R}$$

This is the exact probability density function of Student's $t$ distribution with $\nu$ degrees of freedom.

### Moments and Tail Decay
The $t$ distribution is symmetric about zero: $f_T(-t) = f_T(t)$. Therefore, all odd moments that exist are zero: $\mathbb{E}[T^k] = 0$ for odd $k < \nu$.
1. **Mean**: $\mathbb{E}[T] = 0$ if $\nu > 1$ (undefined for $\nu \le 1$).
2. **Variance**: $\text{Var}(T) = \frac{\nu}{\nu - 2}$ if $\nu > 2$ (infinite for $1 < \nu \le 2$).
3. **Heavy Tails**: As $|t| \to \infty$, $f_T(t) \sim C |t|^{-(\nu + 1)}$. The tails decay as a polynomial power law rather than exponentially, making the $t$ distribution much more prone to extreme values than the Gaussian distribution.
4. **Gaussian Limit**: Using Stirling's approximation, as $\nu \to \infty$:
   $$\lim_{\nu \to \infty} \left( 1 + \frac{t^2}{\nu} \right)^{-\frac{\nu + 1}{2}} = e^{-t^2/2}, \quad \lim_{\nu \to \infty} \frac{\Gamma((\nu+1)/2)}{\sqrt{\nu \pi}\Gamma(\nu/2)} = \frac{1}{\sqrt{2\pi}}$$
   recovering the standard normal density $\mathcal{N}(0, 1)$.

## 3.9 Snedecor-Fisher F Distribution: Definition, Derivation, and Reciprocal Symmetry

When comparing the variances of two independent Gaussian populations or evaluating the overall significance of a linear regression model, inference relies on the **Snedecor-Fisher $F$ distribution**.

### General Definition of the $F$ Distribution
Let $U_1 \sim \chi_{\nu_1}^2$ and $U_2 \sim \chi_{\nu_2}^2$ be two **independent** Chi-Square random variables with $\nu_1$ and $\nu_2$ degrees of freedom, respectively. The random variable defined by the ratio of these variables scaled by their degrees of freedom:

$$F = \frac{U_1 / \nu_1}{U_2 / \nu_2}$$

is said to follow the **$F$ distribution with $\nu_1$ and $\nu_2$ degrees of freedom**, denoted $F \sim F_{\nu_1, \nu_2}$.

### Analytical Derivation of the Density Function
Because $U_1$ and $U_2$ are independent, their joint density is:

$$f_{U_1, U_2}(u_1, u_2) = \frac{1}{2^{(\nu_1 + \nu_2)/2} \Gamma(\nu_1/2) \Gamma(\nu_2/2)} u_1^{\frac{\nu_1}{2} - 1} u_2^{\frac{\nu_2}{2} - 1} e^{-(u_1 + u_2)/2}, \quad u_1 > 0, \; u_2 > 0$$

Define the transformation:

$$F = \frac{U_1 / \nu_1}{U_2 / \nu_2} = \frac{\nu_2 U_1}{\nu_1 U_2}, \quad W = U_2$$

The inverse transformation is:

$$U_1 = \frac{\nu_1}{\nu_2} F W, \quad U_2 = W$$

The Jacobian determinant is:

$$\det(J) = \det \begin{pmatrix} \frac{\nu_1}{\nu_2} w & \frac{\nu_1}{\nu_2} f \\ 0 & 1 \end{pmatrix} = \frac{\nu_1}{\nu_2} w$$

The joint density of $(F, W)$ is:

$$f_{F, W}(f, w) = \frac{1}{2^{(\nu_1+\nu_2)/2}\Gamma(\nu_1/2)\Gamma(\nu_2/2)} \left( \frac{\nu_1}{\nu_2} f w \right)^{\frac{\nu_1}{2} - 1} w^{\frac{\nu_2}{2} - 1} \exp\left( -\frac{w}{2}\left(1 + \frac{\nu_1}{\nu_2} f\right) \right) \cdot \frac{\nu_1}{\nu_2} w$$

Integrating out $w$ over $(0, \infty)$ using the Gamma integral yields the probability density function of $F$:

$$f_F(f; \nu_1, \nu_2) = \frac{\Gamma\left( \frac{\nu_1 + \nu_2}{2} \right)}{\Gamma\left( \frac{\nu_1}{2} \right) \Gamma\left( \frac{\nu_2}{2} \right)} \left( \frac{\nu_1}{\nu_2} \right)^{\frac{\nu_1}{2}} \frac{f^{\frac{\nu_1}{2} - 1}}{\left( 1 + \frac{\nu_1}{\nu_2} f \right)^{\frac{\nu_1 + \nu_2}{2}}}, \quad f > 0$$

and zero for $f \le 0$.

### Core Structural Properties of the $F$ Distribution
1. **Reciprocal Property**: If $F \sim F_{\nu_1, \nu_2}$, then its reciprocal satisfies:
   $$\frac{1}{F} = \frac{U_2 / \nu_2}{U_1 / \nu_1} \sim F_{\nu_2, \nu_1}$$
   This property allows critical values in the lower tail to be computed directly from upper-tail critical values:
   $$F_{1 - \alpha, \nu_1, \nu_2} = \frac{1}{F_{\alpha, \nu_2, \nu_1}}$$
2. **Relation to Student's $t$**: If $T \sim t_\nu$, then $T = \frac{Z}{\sqrt{V/\nu}}$, so:
   $$T^2 = \frac{Z^2 / 1}{V / \nu} \sim F_{1, \nu}$$
   The square of a Student's $t$ variate with $\nu$ degrees of freedom is an $F$ variate with $(1, \nu)$ degrees of freedom.
3. **Moments**:
   $$\mathbb{E}[F] = \frac{\nu_2}{\nu_2 - 2} \quad \text{for } \nu_2 > 2$$
   $$\text{Var}(F) = \frac{2 \nu_2^2 (\nu_1 + \nu_2 - 2)}{\nu_1 (\nu_2 - 2)^2 (\nu_2 - 4)} \quad \text{for } \nu_2 > 4$$
   Notice that the mean depends exclusively on the denominator degrees of freedom $\nu_2$.

## 3.10 Non-Central Sampling Distributions: Non-Central $\chi^2$, $t$, and $F$

When evaluating the power of statistical hypothesis tests under specific alternative hypotheses ($H_1$), test statistics no longer follow central sampling distributions. Instead, non-zero population effects induce **non-central distributions**.

### The Non-Central Chi-Square Distribution
Let $X_1, X_2, \dots, X_k$ be independent normal random variables with unit variances but non-zero means: $X_i \sim \mathcal{N}(\mu_i, 1)$. Define the sum of their squares:

$$Y = \sum_{i=1}^k X_i^2 = \mathbf{X}^T \mathbf{X}$$

The random variable $Y$ follows a **non-central Chi-Square distribution** with $k$ degrees of freedom and **non-centrality parameter** $\lambda$, denoted $Y \sim \chi_k^2(\lambda)$, where:

$$\lambda = \sum_{i=1}^k \mu_i^2 = \|\boldsymbol{\mu}\|^2$$

The moment generating function of $Y$ is:

$$M_Y(t) = (1 - 2t)^{-k/2} \exp\left( \frac{\lambda t}{1 - 2t} \right), \quad t < 1/2$$

Expanding the exponential term via power series reveals that the non-central $\chi_k^2(\lambda)$ distribution is an exact **Poisson mixture of central Chi-Square distributions**:

$$f_Y(y; k, \lambda) = \sum_{j=0}^\infty \frac{e^{-\lambda/2} (\lambda/2)^j}{j!} f_{\chi_{k + 2j}^2}(y)$$

where the mixing weights are Poisson probabilities with mean $\lambda / 2$, and the conditional components are central Chi-Square densities with degrees of freedom $k + 2j$.
The mean and variance of $Y \sim \chi_k^2(\lambda)$ are:

$$\mathbb{E}[Y] = k + \lambda, \quad \text{Var}(Y) = 2k + 4\lambda$$

### The Non-Central Student's $t$ Distribution
Let $Z \sim \mathcal{N}(\delta, 1)$ have non-zero mean $\delta$, and let $V \sim \chi_\nu^2$ be independent of $Z$. The ratio:

$$T = \frac{Z}{\sqrt{V / \nu}}$$

follows a **non-central Student's $t$ distribution** with $\nu$ degrees of freedom and non-centrality parameter $\delta$, denoted $t_\nu(\delta)$. This distribution is essential for computing the statistical power of one-sample and two-sample Student's $t$-tests.

### The Non-Central $F$ Distribution
Let $U_1 \sim \chi_{\nu_1}^2(\lambda)$ be a non-central Chi-Square variable, and let $U_2 \sim \chi_{\nu_2}^2$ be an independent central Chi-Square variable. The ratio:

$$F = \frac{U_1 / \nu_1}{U_2 / \nu_2}$$

follows a **non-central $F$ distribution**, denoted $F_{\nu_1, \nu_2}(\lambda)$. The non-central $F$ distribution governs the power calculations in ANOVA and general linear hypothesis testing.

### Geometric Interpretation and Statistical Applications of Non-Central Distributions

In statistical testing, non-central distributions are the indispensable engine of **power analysis and sample size determination**. When the null hypothesis $H_0$ is false, the test statistic no longer follows a central distribution centered at zero or unity, but shifts toward the non-central distribution whose shape depends monotonically upon the non-centrality parameter $\lambda$.

For instance, in the classic analysis of variance (ANOVA) comparing $k$ experimental treatments with $n_i$ observations in the $i$-th group, the test statistic is the ratio of treatment mean square to error mean square:

$$F = \frac{\text{MST}}{\text{MSE}} = \frac{\sum_{i=1}^k n_i (\bar{X}_{i\cdot} - \bar{X}_{\cdot\cdot})^2 / (k-1)}{\sum_{i=1}^k \sum_{j=1}^{n_i} (X_{ij} - \bar{X}_{i\cdot})^2 / (N-k)}$$

Under the null hypothesis $H_0: \mu_1 = \mu_2 = \dots = \mu_k$, the numerator and denominator quadratic forms are central chi-squares, yielding the central $F(k-1, N-k)$ distribution. Under an alternative hypothesis $H_1$, the expected treatment means deviate from the grand mean, so the numerator becomes a non-central chi-square with non-centrality parameter:

$$\lambda = \frac{1}{\sigma^2} \sum_{i=1}^k n_i (\mu_i - \bar{\mu})^2$$

where $\bar{\mu} = \frac{1}{N}\sum n_i \mu_i$. The test statistic follows an exact non-central $F$-distribution $F(k-1, N-k, \lambda)$.
The statistical power of the test at significance level $\alpha$ is:

$$\text{Power}(\lambda) = P\left( F(k-1, N-k, \lambda) \ge F_{1-\alpha, k-1, N-k} \right)$$

Because the cumulative distribution function of the non-central $F$ distribution is strictly decreasing in $\lambda$ for every fixed critical value, the power function $\text{Power}(\lambda)$ is strictly increasing in $\lambda$. This formalizes the mathematical intuition that power improves when:
1. The effect size $\sum n_i(\mu_i - \bar{\mu})^2$ is large;
2. The experimental error variance $\sigma^2$ is small;
3. The overall sample size $N$ is increased.

By inverting the non-central $F$ power function, researchers in clinical trials, agricultural science, and psychometrics can accurately calculate the required sample size to guarantee a target power (typically $80\%$ or $90\%$) prior to data collection.


## 3.11 The Wishart Distribution: Matrix Generalization of Chi-Square

In univariate normal sampling, the sum of squared deviations $\sum_{i=1}^n (X_i - \bar{X})^2$ follows a scaled Chi-Square distribution. In multivariate normal sampling, where each observation $\mathbf{X}_i$ is a $p$-dimensional random vector, the natural matrix analogue of the sum of squares is the scatter matrix $\sum_{i=1}^n (\mathbf{X}_i - \bar{\mathbf{X}})(\mathbf{X}_i - \bar{\mathbf{X}})^T$. The sampling distribution of this random matrix is the **Wishart distribution**, first derived by John Wishart in 1928.

### Formal Definition of the Wishart Matrix
Let $\mathbf{Z}_1, \mathbf{Z}_2, \dots, \mathbf{Z}_m$ be an independent collection of $p$-dimensional multivariate normal vectors with zero mean vector and common $p \times p$ positive-definite covariance matrix $\boldsymbol{\Sigma}$:

$$\mathbf{Z}_i \sim \mathcal{N}_p(\mathbf{0}, \boldsymbol{\Sigma}) \quad \text{for each } i \in \{1, 2, \dots, m\}$$

The $p \times p$ random matrix formed by the sum of outer products:

$$\mathbf{W} = \sum_{i=1}^m \mathbf{Z}_i \mathbf{Z}_i^T$$

is said to follow a **central Wishart distribution** with $m$ degrees of freedom and scale matrix $\boldsymbol{\Sigma}$, denoted:

$$\mathbf{W} \sim \mathcal{W}_p(m, \boldsymbol{\Sigma})$$

Notice that when $p = 1$, the matrix collapses to a scalar $W = \sum_{i=1}^m Z_i^2$, where $Z_i \sim \mathcal{N}(0, \sigma^2)$, so $W / \sigma^2 \sim \chi_m^2$. Thus, the Wishart distribution represents a direct multidimensional tensor generalization of the Chi-Square law.

When the degrees of freedom satisfy $m \ge p$, the matrix $\mathbf{W}$ is non-singular and strictly positive-definite with probability 1. In that regular case, $\mathbf{W}$ possesses a matrix probability density function with respect to the Lebesgue measure on the cone of $p \times p$ symmetric positive-definite matrices:

$$f_{\mathbf{W}}(\mathbf{W}; m, \boldsymbol{\Sigma}) = \frac{1}{2^{m p / 2} \det(\boldsymbol{\Sigma})^{m/2} \Gamma_p(m/2)} \det(\mathbf{W})^{\frac{m - p - 1}{2}} \exp\left( -\frac{1}{2} \text{tr}(\boldsymbol{\Sigma}^{-1} \mathbf{W}) \right)$$

where $\Gamma_p(a)$ is the **multivariate Gamma function**, defined as:

$$\Gamma_p(a) = \pi^{p(p - 1)/4} \prod_{j=1}^p \Gamma\left( a - \frac{j - 1}{2} \right)$$

### Properties and Bartlett's Decomposition
The Wishart distribution exhibits fundamental structural properties that parallel the univariate Chi-Square distribution:
1. **Mean Matrix**: The mathematical expectation of the random matrix is:
   $$\mathbb{E}[\mathbf{W}] = m \boldsymbol{\Sigma}$$
2. **Reproductive Property**: If $\mathbf{W}_1 \sim \mathcal{W}_p(m_1, \boldsymbol{\Sigma})$ and $\mathbf{W}_2 \sim \mathcal{W}_p(m_2, \boldsymbol{\Sigma})$ are independent, then:
   $$\mathbf{W}_1 + \mathbf{W}_2 \sim \mathcal{W}_p(m_1 + m_2, \boldsymbol{\Sigma})$$
3. **Linear Invariance**: If $\mathbf{C}$ is a non-singular $q \times p$ matrix, then:
   $$\mathbf{C} \mathbf{W} \mathbf{C}^T \sim \mathcal{W}_q(m, \; \mathbf{C} \boldsymbol{\Sigma} \mathbf{C}^T)$$
4. **Bartlett's Decomposition**: If $\mathbf{W} \sim \mathcal{W}_p(m, \mathbf{I}_p)$ with $m \ge p$, then $\mathbf{W}$ can be factored uniquely as $\mathbf{W} = \mathbf{T} \mathbf{T}^T$, where $\mathbf{T}$ is a lower-triangular matrix with positive diagonal elements. Bartlett proved that all non-zero entries of $\mathbf{T}$ are mutually independent random variables, with squared diagonal elements following independent Chi-Square distributions ($T_{jj}^2 \sim \chi_{m - j + 1}^2$) and off-diagonal elements following independent standard normal distributions ($T_{jk} \sim \mathcal{N}(0, 1)$ for $j > k$). This decomposition provides an ultra-fast algorithm for simulating Wishart matrices in computational statistics.

## 3.12 Hotelling's $T^2$ Distribution: The Multivariate Generalization of Student's $t$

In univariate analysis, Student's $t$-statistic tests hypotheses concerning a population mean when the variance is unknown. In $p$-dimensional multivariate settings, Harold Hotelling introduced the **Hotelling's $T^2$ statistic** to test hypotheses about the multivariate mean vector $\boldsymbol{\mu} \in \mathbb{R}^p$.

Let $\mathbf{X}_1, \dots, \mathbf{X}_n$ be an i.i.d. random sample of $p$-dimensional vectors from $\mathcal{N}_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, with $n > p$. The sample mean vector and sample covariance matrix are:

$$\bar{\mathbf{X}} = \frac{1}{n} \sum_{i=1}^n \mathbf{X}_i, \quad \mathbf{S} = \frac{1}{n-1} \sum_{i=1}^n (\mathbf{X}_i - \bar{\mathbf{X}})(\mathbf{X}_i - \bar{\mathbf{X}})^T$$

Hotelling's $T^2$ statistic for testing the null hypothesis $H_0: \boldsymbol{\mu} = \boldsymbol{\mu}_0$ is defined as the squared Mahalanobis distance between the sample mean and the hypothesized mean, scaled by the sample size:

$$T^2 = n (\bar{\mathbf{X}} - \boldsymbol{\mu}_0)^T \mathbf{S}^{-1} (\bar{\mathbf{X}} - \boldsymbol{\mu}_0)$$

### Exact Transformation to the Snedecor-Fisher $F$ Distribution
Under the null hypothesis $H_0: \boldsymbol{\mu} = \boldsymbol{\mu}_0$, the exact sampling distribution of Hotelling's $T^2$ can be transformed into an exact Snedecor-Fisher $F$ distribution.

**Theorem (Hotelling's $T^2$ Representation)**: If $\mathbf{X}_1, \dots, \mathbf{X}_n \sim \mathcal{N}_p(\boldsymbol{\mu}_0, \boldsymbol{\Sigma})$ with $n > p$, then:

$$\frac{n - p}{p (n - 1)} T^2 \sim F_{p, n - p}$$

**Proof Outline**:
From normal sampling theory, $\sqrt{n}(\bar{\mathbf{X}} - \boldsymbol{\mu}_0) \sim \mathcal{N}_p(\mathbf{0}, \boldsymbol{\Sigma})$, and $(n - 1)\mathbf{S} \sim \mathcal{W}_p(n - 1, \boldsymbol{\Sigma})$, with $\bar{\mathbf{X}}$ and $\mathbf{S}$ being completely independent.
Standardizing by $\boldsymbol{\Sigma}^{-1/2}$, define $\mathbf{Z} = \sqrt{n}\boldsymbol{\Sigma}^{-1/2}(\bar{\mathbf{X}} - \boldsymbol{\mu}_0) \sim \mathcal{N}_p(\mathbf{0}, \mathbf{I}_p)$ and $\mathbf{W} = (n - 1)\boldsymbol{\Sigma}^{-1/2} \mathbf{S} \boldsymbol{\Sigma}^{-1/2} \sim \mathcal{W}_p(n - 1, \mathbf{I}_p)$.
Then $T^2 = (n - 1) \mathbf{Z}^T \mathbf{W}^{-1} \mathbf{Z}$.
Conditioning on $\mathbf{Z} = \mathbf{z}$, choose an orthogonal matrix $\mathbf{P}$ whose first row is $\mathbf{z}^T / \|\mathbf{z}\|$. By the invariance of the Wishart distribution under orthogonal rotations, the scalar quantity $\frac{\mathbf{z}^T \mathbf{W}^{-1} \mathbf{z}}{\|\mathbf{z}\|^2}$ is equal to the $(1, 1)$ entry of $(\mathbf{P} \mathbf{W} \mathbf{P}^T)^{-1}$.
Using the block matrix inversion formula, the reciprocal of the $(1, 1)$ entry of an inverted standard Wishart matrix follows an independent Chi-Square distribution:
$$\frac{\|\mathbf{z}\|^2}{\mathbf{z}^T \mathbf{W}^{-1} \mathbf{z}} \sim \chi_{(n - 1) - p + 1}^2 = \chi_{n - p}^2$$
Therefore, conditional on $\mathbf{Z}$:
$$\frac{\mathbf{z}^T \mathbf{W}^{-1} \mathbf{z}}{\|\mathbf{z}\|^2} = \frac{1}{V}, \quad \text{where } V \sim \chi_{n - p}^2$$
Multiplying by $\|\mathbf{Z}\|^2 \sim \chi_p^2$ (which is independent of $V$):
$$T^2 = (n - 1) \frac{\|\mathbf{Z}\|^2}{V} = (n - 1) \frac{\chi_p^2}{\chi_{n - p}^2}$$
Dividing the numerator and denominator by their degrees of freedom:
$$\frac{T^2}{n - 1} \cdot \frac{n - p}{p} = \frac{\chi_p^2 / p}{\chi_{n - p}^2 / (n - p)} \sim F_{p, n - p}$$
This establishes the exact correspondence between Hotelling's $T^2$ and the $F$ distribution, enabling exact multivariate hypothesis testing across all dimensions. $\blacksquare$

## 3.13 The Generalized Sample Variance and Wilks' Lambda

In univariate statistics, the sample variance $S^2$ measures scalar dispersion. In multivariate analysis, dispersion must capture both the individual coordinate variances and their mutual correlations. A foundational scalar measure of multidimensional dispersion is the **generalized sample variance**, introduced by Samuel S. Wilks.

The generalized sample variance is defined as the determinant of the sample covariance matrix:

$$|\mathbf{S}| = \det(\mathbf{S})$$

### Geometric Interpretation as Hypervolume
The determinant $|\mathbf{S}|$ has an intuitive geometric meaning. Consider the sample vectors centered by the sample mean: $\mathbf{r}_i = \mathbf{X}_i - \bar{\mathbf{X}} \in \mathbb{R}^p$. These vectors span a $p$-dimensional parallelotope in Euclidean space. The volume of this parallelotope is directly proportional to $\sqrt{\det(\mathbf{S})}$.
- If the variables are completely uncorrelated and standardized, $\mathbf{S} = \mathbf{I}_p$, so $|\mathbf{S}| = 1$, representing maximal multidimensional spread.
- If one variable is a perfect linear combination of the other variables, the data points collapse onto a $(p - 1)$-dimensional hyperplane, the matrix $\mathbf{S}$ becomes singular, and $|\mathbf{S}| = 0$.

### Exact Sampling Distribution of the Generalized Variance
Because $(n - 1)\mathbf{S} \sim \mathcal{W}_p(n - 1, \boldsymbol{\Sigma})$, the distribution of $|\mathbf{S}|$ is determined by the determinant of a Wishart matrix. Using Bartlett's decomposition, the determinant of $\mathbf{W} \sim \mathcal{W}_p(m, \mathbf{I}_p)$ decomposes into the product of the squared diagonal elements of the Cholesky factor $\mathbf{T}$:

$$\det(\mathbf{W}) = \prod_{j=1}^p T_{jj}^2$$

Because the entries $T_{jj}$ are mutually independent with $T_{jj}^2 \sim \chi_{m - j + 1}^2$, the determinant of a Wishart matrix is distributed as the **product of $p$ independent Chi-Square random variables**:

$$\det(\mathbf{W}) \sim \prod_{j=1}^p \chi_{m - j + 1}^2$$

Consequently, the generalized sample variance satisfies:

$$\det(\mathbf{S}) \sim \frac{\det(\boldsymbol{\Sigma})}{(n - 1)^p} \prod_{j=1}^p \chi_{n - j}^2$$

Taking natural logarithms transforms the product into a sum of independent log-Chi-Square random variables, which converges rapidly to a Gaussian distribution via the classical Central Limit Theorem as the sample size $n \to \infty$.

## 3.14 Quadratic Forms in Singular Normal Vectors and the Moore-Penrose Pseudoinverse

In many modern statistical applications—such as overparameterized regression models, spline smoothing, and spatial Markov random fields—the covariance matrix $\boldsymbol{\Sigma}$ of a normal vector $\mathbf{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is **singular** ($\text{rank}(\boldsymbol{\Sigma}) = r < n$). In such degenerate settings, the classical inverse $\boldsymbol{\Sigma}^{-1}$ does not exist, and the probability distribution is concentrated entirely on an $r$-dimensional affine hyperplane within $\mathbb{R}^n$.

To construct quadratic forms and test statistics under singular covariance matrices, mathematical statistics deploys the **Moore-Penrose pseudoinverse** (or more generally, a generalized inverse $\boldsymbol{\Sigma}^-$).

A matrix $\boldsymbol{\Sigma}^-$ is a **generalized inverse** (or $g$-inverse) of $\boldsymbol{\Sigma}$ if it satisfies the fundamental Penrose condition:

$$\boldsymbol{\Sigma} \boldsymbol{\Sigma}^- \boldsymbol{\Sigma} = \boldsymbol{\Sigma}$$

The Moore-Penrose pseudoinverse, denoted $\boldsymbol{\Sigma}^+$, satisfies three additional conditions: $\boldsymbol{\Sigma}^+ \boldsymbol{\Sigma} \boldsymbol{\Sigma}^+ = \boldsymbol{\Sigma}^+$, $(\boldsymbol{\Sigma} \boldsymbol{\Sigma}^+)^T = \boldsymbol{\Sigma} \boldsymbol{\Sigma}^+$, and $(\boldsymbol{\Sigma}^+ \boldsymbol{\Sigma})^T = \boldsymbol{\Sigma}^+ \boldsymbol{\Sigma}$, making it unique.

### Khatri's Theorem on Quadratic Forms in Singular Normal Vectors
The classical theorem on Chi-Square distributions of quadratic forms (Section 3.5) was generalized to singular normal vectors by C. G. Khatri in 1968.

**Theorem (Khatri's Theorem)**: Let $\mathbf{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where $\boldsymbol{\Sigma}$ may be singular. Let $\mathbf{A}$ be an $n \times n$ real symmetric matrix. Then the quadratic form:

$$Q = \mathbf{X}^T \mathbf{A} \mathbf{X}$$

follows a non-central Chi-Square distribution $Q \sim \chi_r^2(\lambda)$ if and only if:

$$\boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\Sigma} = \boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\Sigma}$$

with degrees of freedom $r = \text{tr}(\mathbf{A} \boldsymbol{\Sigma})$ and non-centrality parameter $\lambda = \boldsymbol{\mu}^T \mathbf{A} \boldsymbol{\mu}$.

Furthermore, if $\boldsymbol{\mu} = \mathbf{0}$, the condition reduces to $\boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\Sigma} = \boldsymbol{\Sigma} \mathbf{A} \boldsymbol{\Sigma}$, which simplifies in the non-singular case ($\boldsymbol{\Sigma} \succ 0$) to $\mathbf{A} \boldsymbol{\Sigma} \mathbf{A} = \mathbf{A}$, recovering the classical idempotency criterion. This theorem provides the complete mathematical foundation for testing linear hypotheses in rank-deficient design models.

## 3.15 Spherically and Elliptically Symmetric Distributions: Invariance Beyond Gaussian Normality

Many elegant geometric and invariance properties of the multivariate normal distribution—such as the rotational symmetry of standard normal vectors and the quadratic structure of Mahalanobis contours—extend naturally to a broader, highly flexible class of probability distributions known as **elliptically contoured (or elliptical) distributions**.

### Spherical Random Vectors
A continuous random vector $\mathbf{Z} \in \mathbb{R}^n$ is said to follow a **spherical distribution** if its probability distribution is invariant under all orthogonal transformations (rotations and reflections). That is, for every orthogonal matrix $\mathbf{P} \in \mathbb{R}^{n \times n}$ satisfying $\mathbf{P}^T \mathbf{P} = \mathbf{I}_n$:

$$\mathbf{P} \mathbf{Z} \stackrel{d}{=} \mathbf{Z}$$

When $\mathbf{Z}$ possesses a probability density function with respect to the Lebesgue measure, rotational invariance implies that the density $f_{\mathbf{Z}}(\mathbf{z})$ depends on the coordinate vector $\mathbf{z}$ solely through its squared Euclidean norm $\|\mathbf{z}\|^2 = \mathbf{z}^T \mathbf{z}$:

$$f_{\mathbf{Z}}(\mathbf{z}) = g(\mathbf{z}^T \mathbf{z}) = g(z_1^2 + z_2^2 + \dots + z_n^2)$$

for some non-negative scalar function $g: [0, \infty) \to [0, \infty)$, termed the density generator.

A profound geometric decomposition characterizes all spherical distributions. Any spherical random vector $\mathbf{Z}$ can be uniquely represented in polar-coordinate form as:

$$\mathbf{Z} \stackrel{d}{=} R \, \mathbf{U}$$

where:
1. $R = \|\mathbf{Z}\| = \sqrt{\mathbf{Z}^T \mathbf{Z}} \ge 0$ is a non-negative scalar random variable representing the radial distance from the origin.
2. $\mathbf{U} = \mathbf{Z} / \|\mathbf{Z}\|$ is a random unit vector uniformly distributed over the $(n - 1)$-dimensional unit sphere $\mathbb{S}^{n-1} = \{\mathbf{u} \in \mathbb{R}^n : \|\mathbf{u}\| = 1\}$.
3. The radial distance $R$ and the spherical directional vector $\mathbf{U}$ are **statistically independent**!

This stochastic representation reveals that the direction $\mathbf{U}$ is purely geometric and completely universal across all spherical distributions, while the specific distribution within the spherical family is governed entirely by the choice of radial distribution for $R$.

### Elliptical Random Vectors
The family of **elliptical distributions** is obtained by applying general affine transformations to spherical vectors. Let $\mathbf{Z} \in \mathbb{R}^k$ be a spherical random vector. Define:

$$\mathbf{X} = \boldsymbol{\mu} + \mathbf{A} \mathbf{Z}$$

where $\boldsymbol{\mu} \in \mathbb{R}^n$ is a location vector and $\mathbf{A} \in \mathbb{R}^{n \times k}$ is a dispersion matrix. Letting $\boldsymbol{\Sigma} = \mathbf{A} \mathbf{A}^T$, the random vector $\mathbf{X}$ is said to follow an elliptical distribution, denoted $\mathbf{X} \sim \mathcal{E}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma}, g)$.

When $\boldsymbol{\Sigma}$ is positive-definite, the probability density function of $\mathbf{X}$ is given by:

$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{\det(\boldsymbol{\Sigma})^{1/2}} g\left( (\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)$$

Prominent examples of elliptical distributions include:
1. **The Multivariate Normal Distribution**: Generated by $g(u) = (2\pi)^{-n/2} e^{-u/2}$. In this special case, the radial variable squared $R^2 = \|\mathbf{Z}\|^2$ follows a Chi-Square distribution $\chi_n^2$. The normal distribution is the unique member of the spherical family whose components $Z_1, \dots, Z_n$ are mutually independent; for all other spherical distributions, rotational invariance forces coordinate dependence through the shared radial factor $R$.
2. **The Multivariate Student's $t$ Distribution**: Generated by $g(u) \propto (1 + u/\nu)^{-(\nu + n)/2}$. Here, the vector can be represented as $\mathbf{X} = \boldsymbol{\mu} + \frac{\mathbf{Z}}{\sqrt{V/\nu}}$, where $\mathbf{Z} \sim \mathcal{N}_n(\mathbf{0}, \boldsymbol{\Sigma})$ and $V \sim \chi_\nu^2$ is an independent scalar Chi-Square variable.
3. **The Multivariate Cauchy Distribution**: The special case of the multivariate $t$ distribution with $\nu = 1$.
4. **The Multivariate Logistic and Laplace Distributions**: Providing alternative symmetric heavy-tailed and double-exponential models.

### Invariance of $F$ and $t$ Ratios under Spherical Distributions
A remarkable result in mathematical statistics, established by E. S. Andersen (1958) and K. T. Fang, is that many classical test statistics derived under normality remain **exact invariants under any continuous spherical distribution**!

Consider a statistic that takes the form of a scale-invariant ratio of homogeneous quadratic forms:

$$T(\mathbf{Z}) = \frac{\mathbf{Z}^T \mathbf{A} \mathbf{Z}}{\mathbf{Z}^T \mathbf{B} \mathbf{Z}}$$

Substitute the stochastic polar representation $\mathbf{Z} = R \mathbf{U}$:

$$T(\mathbf{Z}) = \frac{(R \mathbf{U})^T \mathbf{A} (R \mathbf{U})}{(R \mathbf{U})^T \mathbf{B} (R \mathbf{U})} = \frac{R^2 (\mathbf{U}^T \mathbf{A} \mathbf{U})}{R^2 (\mathbf{U}^T \mathbf{B} \mathbf{U})} = \frac{\mathbf{U}^T \mathbf{A} \mathbf{U}}{\mathbf{U}^T \mathbf{B} \mathbf{U}}$$

Notice that the radial random variable $R^2$ cancels completely from the numerator and denominator!
Because $\mathbf{U}$ is uniformly distributed on the unit sphere for *any* spherical distribution, the sampling distribution of the ratio $T(\mathbf{Z})$ depends strictly on the uniform spherical measure of $\mathbf{U}$, completely independent of the radial distribution $R$.

Consequently:
- The standard one-sample Student's $t$-statistic $T = \frac{\bar{X} \sqrt{n}}{S}$ has an exact $t_{n-1}$ distribution under the null hypothesis $\mu = 0$ not only for Gaussian samples, but for **any spherical population distribution**!
- The ANOVA $F$-statistic has an exact $F$ distribution under the null hypothesis for all spherical distributions!

This invariance provides deep mathematical insight into the extraordinary empirical robustness of Student's $t$-tests and $F$-tests against departures from normality: whenever the data-generating mechanism preserves spherical symmetry, the exact null distribution of the test statistic is completely unchanged.

## Fully worked question 1: Full Rigorous Proof of Cochran's Theorem using Matrix Spectral Decomposition and Moment Generating Functions

### Question
Let $\mathbf{Z} \sim \mathcal{N}_n(\mathbf{0}, \mathbf{I}_n)$ be an $n$-dimensional standard normal random vector. Suppose that the $n \times n$ identity matrix is decomposed into a sum of $k$ real symmetric matrices:

$$\mathbf{I}_n = \sum_{j=1}^k \mathbf{A}_j$$

where $\text{rank}(\mathbf{A}_j) = r_j$ for each $j \in \{1, 2, \dots, k\}$.
1. State the rank equality condition: $\sum_{j=1}^k r_j = n$.
2. Prove that the rank condition implies that every matrix $\mathbf{A}_j$ is idempotent: $\mathbf{A}_j^2 = \mathbf{A}_j$ for all $j$.
3. Prove that the rank condition implies pairwise orthogonality: $\mathbf{A}_j \mathbf{A}_m = \mathbf{0}$ for all $j \ne m$.
4. Derive the joint moment generating function of the quadratic forms $Q_j = \mathbf{Z}^T \mathbf{A}_j \mathbf{Z}$ ($j = 1, \dots, k$) and deduce that $Q_1, \dots, Q_k$ are mutually independent Chi-Square random variables: $Q_j \sim \chi_{r_j}^2$.

### Solution, step 1: Spectral Properties and Rank Analysis
Let $\mathbf{I}_n = \sum_{j=1}^k \mathbf{A}_j$, where each $\mathbf{A}_j$ is real and symmetric with $\text{rank}(\mathbf{A}_j) = r_j$, and assume $\sum_{j=1}^k r_j = n$.
Because each $\mathbf{A}_j$ is real symmetric, its non-zero eigenvalues $\lambda_{ji}$ are real. Let $p_j$ denote the number of non-zero eigenvalues of $\mathbf{A}_j$. Since the rank of a symmetric matrix equals the number of its non-zero eigenvalues, $p_j = r_j$.

Let $\lambda_{\max}(\mathbf{A}_j)$ denote the largest eigenvalue of $\mathbf{A}_j$. We first prove that all eigenvalues of every $\mathbf{A}_j$ satisfy $\lambda \le 1$.
Suppose for contradiction that some $\mathbf{A}_m$ has an eigenvalue $\lambda > 1$ with associated unit eigenvector $\mathbf{v}$ ($\|\mathbf{v}\| = 1$). Then:
$$\mathbf{v}^T \mathbf{A}_m \mathbf{v} = \lambda > 1$$
However, multiplying the identity decomposition by $\mathbf{v}$ on both sides:
$$1 = \mathbf{v}^T \mathbf{I}_n \mathbf{v} = \sum_{j=1}^k \mathbf{v}^T \mathbf{A}_j \mathbf{v} = \mathbf{v}^T \mathbf{A}_m \mathbf{v} + \sum_{j \ne m} \mathbf{v}^T \mathbf{A}_j \mathbf{v} > 1 + \sum_{j \ne m} \mathbf{v}^T \mathbf{A}_j \mathbf{v}$$
Since $\sum_{j=1}^k r_j = n$, the column spaces of $\mathbf{A}_1, \dots, \mathbf{A}_k$ form a direct sum decomposition of $\mathbb{R}^n$:
$$\mathbb{R}^n = \text{Col}(\mathbf{A}_1) \oplus \text{Col}(\mathbf{A}_2) \oplus \dots \oplus \text{Col}(\mathbf{A}_k)$$
Because the sum of dimensions of the column spaces equals $n$, their intersections are trivial: $\text{Col}(\mathbf{A}_j) \cap \sum_{m \ne j} \text{Col}(\mathbf{A}_m) = \{\mathbf{0}\}$.

### Solution, step 2: Proof of Idempotency
For any vector $\mathbf{x} \in \text{Col}(\mathbf{A}_j)$, there exists $\mathbf{u} \in \mathbb{R}^n$ such that $\mathbf{x} = \mathbf{A}_j \mathbf{u}$. Multiply both sides of the identity decomposition by $\mathbf{x}$:
$$\mathbf{x} = \mathbf{I}_n \mathbf{x} = \sum_{m=1}^k \mathbf{A}_m \mathbf{x} = \mathbf{A}_j \mathbf{x} + \sum_{m \ne j} \mathbf{A}_m \mathbf{x}$$
Rearranging terms:
$$\mathbf{x} - \mathbf{A}_j \mathbf{x} = \sum_{m \ne j} \mathbf{A}_m \mathbf{x}$$
The left side resides in $\text{Col}(\mathbf{A}_j)$, while the right side resides in the sum of the remaining column spaces $\sum_{m \ne j} \text{Col}(\mathbf{A}_m)$.
Because the decomposition is a direct sum, the intersection of these two linear subspaces contains only the zero vector $\mathbf{0}$. Therefore, both sides must vanish identically:
$$\mathbf{x} - \mathbf{A}_j \mathbf{x} = \mathbf{0} \implies \mathbf{A}_j \mathbf{x} = \mathbf{x}$$
Since this holds for every vector $\mathbf{x} \in \text{Col}(\mathbf{A}_j)$, substitute $\mathbf{x} = \mathbf{A}_j \mathbf{u}$ for any arbitrary $\mathbf{u} \in \mathbb{R}^n$:
$$\mathbf{A}_j (\mathbf{A}_j \mathbf{u}) = \mathbf{A}_j \mathbf{u} \implies \mathbf{A}_j^2 \mathbf{u} = \mathbf{A}_j \mathbf{u} \quad \text{for all } \mathbf{u} \in \mathbb{R}^n$$
Consequently:
$$\mathbf{A}_j^2 = \mathbf{A}_j \quad \text{for all } j \in \{1, 2, \dots, k\}$$
Each matrix $\mathbf{A}_j$ is an orthogonal projection matrix (symmetric idempotent matrix).

### Solution, step 3: Proof of Pairwise Orthogonality
From the direct sum argument in Step 2, we also established that:
$$\sum_{m \ne j} \mathbf{A}_m \mathbf{x} = \mathbf{0} \quad \text{for every } \mathbf{x} \in \text{Col}(\mathbf{A}_j)$$
Specifically, for any distinct pair $j \ne m$, multiplying $\mathbf{A}_m \mathbf{x} = \mathbf{0}$ with $\mathbf{x} = \mathbf{A}_j \mathbf{u}$ yields:
$$\mathbf{A}_m \mathbf{A}_j \mathbf{u} = \mathbf{0} \quad \text{for all } \mathbf{u} \in \mathbb{R}^n$$
Therefore:
$$\mathbf{A}_m \mathbf{A}_j = \mathbf{0} \quad \text{for all } m \ne j$$
The projection matrices are mutually pairwise orthogonal.

### Solution, step 4: Joint MGF Derivation and Chi-Square Independence
Consider the joint moment generating function of the $k$ quadratic forms $Q_j = \mathbf{Z}^T \mathbf{A}_j \mathbf{Z}$ for parameters $t_1, \dots, t_k$:
$$M(t_1, \dots, t_k) = \mathbb{E}\left[ \exp\left( \sum_{j=1}^k t_j Q_j \right) \right] = \mathbb{E}\left[ \exp\left( \mathbf{Z}^T \left( \sum_{j=1}^k t_j \mathbf{A}_j \right) \mathbf{Z} \right) \right]$$
Because the matrices $\mathbf{A}_1, \dots, \mathbf{A}_k$ are symmetric and pairwise orthogonal ($\mathbf{A}_j \mathbf{A}_m = \mathbf{0}$ for $j \ne m$), they commute pairwise and can be **simultaneously diagonalized** by a common orthogonal matrix $\mathbf{P}$ ($\mathbf{P}^T \mathbf{P} = \mathbf{I}_n$).
Under this basis, $\mathbf{P}^T \mathbf{A}_j \mathbf{P} = \boldsymbol{\Lambda}_j$, where $\boldsymbol{\Lambda}_j$ is a diagonal matrix containing $r_j$ ones and $n - r_j$ zeros.
Since $\sum_{j=1}^k \mathbf{A}_j = \mathbf{I}_n$, the diagonal positions of the ones in $\boldsymbol{\Lambda}_1, \dots, \boldsymbol{\Lambda}_k$ are completely mutually disjoint!
Let $\mathbf{W} = \mathbf{P}^T \mathbf{Z} \sim \mathcal{N}_n(\mathbf{0}, \mathbf{I}_n)$. The quadratic forms separate cleanly across disjoint coordinate subsets:
$$Q_j = \mathbf{Z}^T \mathbf{A}_j \mathbf{Z} = \mathbf{W}^T \boldsymbol{\Lambda}_j \mathbf{W} = \sum_{i \in I_j} W_i^2$$
where $I_1, I_2, \dots, I_k$ form a partition of the index set $\{1, 2, \dots, n\}$ with $|I_j| = r_j$.
Because the coordinate sub-vectors $(W_i)_{i \in I_j}$ are disjoint collections of independent standard normal random variables, the quadratic forms $Q_1, Q_2, \dots, Q_k$ depend on completely disjoint subsets of independent random variables.
Consequently, $Q_1, \dots, Q_k$ are **mutually stochastically independent**, and each follows an exact central Chi-Square distribution:
$$Q_j = \sum_{i \in I_j} W_i^2 \sim \chi_{r_j}^2 \quad \text{for each } j \in \{1, 2, \dots, k\}$$
This completes the full rigorous proof of Cochran's Theorem. $\blacksquare$

## Fully worked question 2: Derivation of the Exact Probability Density Function of Student's t Distribution with $\nu$ Degrees of Freedom

### Question
Let $Z \sim \mathcal{N}(0, 1)$ and $V \sim \chi_\nu^2$ be independent random variables, where $\nu > 0$. The Student's $t$ statistic is defined by:

$$T = \frac{Z}{\sqrt{V / \nu}}$$

1. Write out the joint probability density function $f_{Z, V}(z, v)$ of $(Z, V)$.
2. Apply the bivariate transformation method to define $(T, W)$, where $W = V$, and compute the Jacobian determinant of the inverse transformation.
3. Formulate the marginal integral for $f_T(t)$ and evaluate it in closed form using the properties of the Euler Gamma function.
4. Verify that as $\nu \to \infty$, the probability density function $f_T(t)$ converges pointwise to the standard normal density $\phi(t) = \frac{1}{\sqrt{2\pi}} e^{-t^2/2}$.

### Solution, step 1: Joint Density of Independent Components
The probability density function of $Z \sim \mathcal{N}(0, 1)$ is:

$$f_Z(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}, \quad -\infty < z < \infty$$

The probability density function of $V \sim \chi_\nu^2$ is:

$$f_V(v) = \frac{1}{2^{\nu/2} \Gamma(\nu/2)} v^{\frac{\nu}{2} - 1} e^{-v/2}, \quad v > 0$$

Because $Z$ and $V$ are independent random variables, their joint probability density function is the product of their marginal densities:

$$f_{Z, V}(z, v) = f_Z(z) f_V(v) = \frac{1}{\sqrt{2\pi} 2^{\nu/2} \Gamma(\nu/2)} v^{\frac{\nu}{2} - 1} \exp\left( -\frac{1}{2}(z^2 + v) \right)$$

defined on the support domain $\mathcal{S} = \{(z, v) \in \mathbb{R}^2 : -\infty < z < \infty, \; v > 0\}$.

### Solution, step 2: Coordinate Transformation and Jacobian Computation
Define the forward bivariate mapping:

$$T = \frac{Z}{\sqrt{V / \nu}}, \quad W = V$$

The image set is $\mathcal{T} = \{(t, w) \in \mathbb{R}^2 : -\infty < t < \infty, \; w > 0\}$.
The inverse transformation is obtained by expressing $z$ and $v$ in terms of $t$ and $w$:

$$v = w, \quad z = t \sqrt{\frac{w}{\nu}} = \frac{t w^{1/2}}{\sqrt{\nu}}$$

The partial derivatives of the inverse transformation are:

$$\frac{\partial z}{\partial t} = \frac{w^{1/2}}{\sqrt{\nu}}, \quad \frac{\partial z}{\partial w} = \frac{t}{2\sqrt{\nu} w^{1/2}}$$

$$\frac{\partial v}{\partial t} = 0, \quad \frac{\partial v}{\partial w} = 1$$

The Jacobian matrix of the inverse mapping is:

$$J = \begin{pmatrix} \frac{\partial z}{\partial t} & \frac{\partial z}{\partial w} \\ \frac{\partial v}{\partial t} & \frac{\partial v}{\partial w} \end{pmatrix} = \begin{pmatrix} \frac{w^{1/2}}{\sqrt{\nu}} & \frac{t}{2\sqrt{\nu} w^{1/2}} \\ 0 & 1 \end{pmatrix}$$

The Jacobian determinant is:

$$\det(J) = \left( \frac{w^{1/2}}{\sqrt{\nu}} \right)(1) - (0)\left( \frac{t}{2\sqrt{\nu} w^{1/2}} \right) = \frac{w^{1/2}}{\sqrt{\nu}}$$

Because $w > 0$, the absolute value of the Jacobian determinant is $|\det(J)| = \frac{w^{1/2}}{\sqrt{\nu}}$.

### Solution, step 3: Evaluation of the Marginal Density Integral
Substitute the inverse transformation into the joint density:

$$f_{T, W}(t, w) = f_{Z, V}\left( \frac{t w^{1/2}}{\sqrt{\nu}}, w \right) |\det(J)|$$

Notice that $z^2 = \frac{t^2 w}{\nu}$, so the exponential argument becomes:

$$-\frac{1}{2}(z^2 + v) = -\frac{1}{2}\left( \frac{t^2 w}{\nu} + w \right) = -\frac{w}{2}\left( 1 + \frac{t^2}{\nu} \right)$$

The power of $w$ in the joint density is $w^{\frac{\nu}{2} - 1} \cdot w^{1/2} = w^{\frac{\nu + 1}{2} - 1}$. Thus:

$$f_{T, W}(t, w) = \frac{1}{\sqrt{2\pi \nu} 2^{\nu/2} \Gamma(\nu/2)} w^{\frac{\nu + 1}{2} - 1} \exp\left( -\frac{w}{2}\left( 1 + \frac{t^2}{\nu} \right) \right)$$

To obtain the marginal density $f_T(t)$, integrate out $w$ from $0$ to $\infty$:

$$f_T(t) = \frac{1}{\sqrt{2\pi \nu} 2^{\nu/2} \Gamma(\nu/2)} \int_0^\infty w^{\frac{\nu + 1}{2} - 1} \exp\left( -\frac{w}{2}\left( 1 + \frac{t^2}{\nu} \right) \right) dw$$

Recall the standard Gamma integral identity: for any constants $a > 0$ and $b > 0$, $\int_0^\infty w^{a - 1} e^{-b w} \, dw = \frac{\Gamma(a)}{b^a}$.
Here, set $a = \frac{\nu + 1}{2}$ and $b = \frac{1}{2}\left( 1 + \frac{t^2}{\nu} \right)$:

$$\int_0^\infty w^{\frac{\nu + 1}{2} - 1} \exp\left( -\frac{w}{2}\left( 1 + \frac{t^2}{\nu} \right) \right) dw = \frac{\Gamma\left( \frac{\nu + 1}{2} \right)}{\left[ \frac{1}{2}\left( 1 + \frac{t^2}{\nu} \right) \right]^{\frac{\nu + 1}{2}}} = 2^{\frac{\nu + 1}{2}} \Gamma\left( \frac{\nu + 1}{2} \right) \left( 1 + \frac{t^2}{\nu} \right)^{-\frac{\nu + 1}{2}}$$

Substitute this into the expression for $f_T(t)$:

$$f_T(t) = \frac{1}{\sqrt{2\pi \nu} 2^{\nu/2} \Gamma(\nu/2)} \cdot 2^{\frac{\nu + 1}{2}} \Gamma\left( \frac{\nu + 1}{2} \right) \left( 1 + \frac{t^2}{\nu} \right)^{-\frac{\nu + 1}{2}}$$

Simplify the powers of 2: $\frac{2^{(\nu + 1)/2}}{\sqrt{2} \cdot 2^{\nu/2}} = \frac{2^{\nu/2 + 1/2}}{2^{1/2 + \nu/2}} = 1$. The expression simplifies to:

$$f_T(t; \nu) = \frac{\Gamma\left( \frac{\nu + 1}{2} \right)}{\sqrt{\nu \pi} \, \Gamma\left( \frac{\nu}{2} \right)} \left( 1 + \frac{t^2}{\nu} \right)^{-\frac{\nu + 1}{2}} \quad \text{for all } t \in \mathbb{R}$$

This completes the closed-form analytical derivation of Student's $t$ probability density function.

### Solution, step 4: Pointwise Convergence to the Normal Density
We now examine the limiting behavior of $f_T(t; \nu)$ as the degrees of freedom $\nu \to \infty$.
First, consider the polynomial kernel factor:

$$\lim_{\nu \to \infty} \left( 1 + \frac{t^2}{\nu} \right)^{-\frac{\nu + 1}{2}} = \lim_{\nu \to \infty} \left[ \left( 1 + \frac{t^2}{\nu} \right)^\nu \right]^{-1/2} \cdot \left( 1 + \frac{t^2}{\nu} \right)^{-1/2}$$

Using the classical exponential limit $\lim_{m \to \infty} (1 + x/m)^m = e^x$ with $x = t^2$:

$$\lim_{\nu \to \infty} \left( 1 + \frac{t^2}{\nu} \right)^{-\frac{\nu + 1}{2}} = (e^{t^2})^{-1/2} \cdot 1 = e^{-t^2/2}$$

Second, consider the normalizing ratio:

$$C_\nu = \frac{\Gamma\left( \frac{\nu + 1}{2} \right)}{\sqrt{\nu \pi} \, \Gamma\left( \frac{\nu}{2} \right)}$$

By Stirling's asymptotic formula for the Gamma function, $\Gamma(z) \sim \sqrt{2\pi} z^{z - 1/2} e^{-z}$ as $z \to \infty$.
For any fixed real constant $c$, Wendel's asymptotic limit gives:

$$\lim_{z \to \infty} \frac{\Gamma(z + c)}{\Gamma(z) z^c} = 1$$

Setting $z = \nu / 2$ and $c = 1/2$:

$$\lim_{\nu \to \infty} \frac{\Gamma\left( \frac{\nu}{2} + \frac{1}{2} \right)}{\Gamma\left( \frac{\nu}{2} \right)} = \left( \frac{\nu}{2} \right)^{1/2} = \sqrt{\frac{\nu}{2}}$$

Substitute this asymptotic limit into $C_\nu$:

$$\lim_{\nu \to \infty} C_\nu = \lim_{\nu \to \infty} \frac{1}{\sqrt{\nu \pi}} \cdot \sqrt{\frac{\nu}{2}} = \frac{1}{\sqrt{\pi}} \cdot \frac{1}{\sqrt{2}} = \frac{1}{\sqrt{2\pi}}$$

Multiplying the two limits together:

$$\lim_{\nu \to \infty} f_T(t; \nu) = \frac{1}{\sqrt{2\pi}} e^{-t^2/2} = \phi(t)$$

This proves that Student's $t$ probability density function converges pointwise to the standard normal density across the entire real line.

## Fully worked question 3: Distribution of the Ratio of Quadratic Forms in Gaussian Vectors and Properties of Fisher-Snedecor F

### Question
Let $X_1, \dots, X_n$ be an i.i.d. sample from $\mathcal{N}(\mu_X, \sigma_X^2)$ and let $Y_1, \dots, Y_m$ be an i.i.d. sample from $\mathcal{N}(\mu_Y, \sigma_Y^2)$, with the two samples being mutually independent. Let $S_X^2$ and $S_Y^2$ denote their respective sample variances.
1. Formulate the ratio of sample variances scaled by population variances and identify its exact distribution.
2. Under the null hypothesis $H_0: \sigma_X^2 = \sigma_Y^2$, derive the distribution of the sample variance ratio $F = S_X^2 / S_Y^2$.
3. Prove that the expected value of $F \sim F_{\nu_1, \nu_2}$ is $\frac{\nu_2}{\nu_2 - 2}$ for $\nu_2 > 2$, and explain why this expectation is strictly greater than 1 even when both population variances are identical.
4. Derive the critical value reciprocal relationship $F_{1 - \alpha, \nu_1, \nu_2} = 1 / F_{\alpha, \nu_2, \nu_1}$ and demonstrate how it allows two-tailed hypothesis testing using only upper-tail statistical tables.

### Solution, step 1: Scaling Ratio Formulation
From Section 3.7, the sample variances of independent Gaussian samples follow scaled Chi-Square distributions:

$$U_1 = \frac{(n - 1) S_X^2}{\sigma_X^2} \sim \chi_{n-1}^2 = \chi_{\nu_1}^2, \quad \text{where } \nu_1 = n - 1$$

$$U_2 = \frac{(m - 1) S_Y^2}{\sigma_Y^2} \sim \chi_{m-1}^2 = \chi_{\nu_2}^2, \quad \text{where } \nu_2 = m - 1$$

Because the two samples are mutually independent, the random variables $U_1$ and $U_2$ are statistically independent.
Consider the ratio of each Chi-Square variate divided by its respective degrees of freedom:

$$\frac{U_1 / \nu_1}{U_2 / \nu_2} = \frac{\frac{(n-1)S_X^2}{\sigma_X^2 (n-1)}}{\frac{(m-1)S_Y^2}{\sigma_Y^2 (m-1)}} = \frac{S_X^2 / \sigma_X^2}{S_Y^2 / \sigma_Y^2} = \left( \frac{S_X^2}{S_Y^2} \right) \left( \frac{\sigma_Y^2}{\sigma_X^2} \right)$$

By definition of the Fisher-Snedecor $F$ distribution (Section 3.9), the ratio of two independent Chi-Square variables divided by their degrees of freedom follows an exact $F$ distribution:

$$\left( \frac{S_X^2}{S_Y^2} \right) \left( \frac{\sigma_Y^2}{\sigma_X^2} \right) \sim F_{\nu_1, \nu_2}$$

### Solution, step 2: Null Hypothesis Distribution
Under the null hypothesis of equal population variances $H_0: \sigma_X^2 = \sigma_Y^2$, the variance ratio $\sigma_Y^2 / \sigma_X^2 = 1$. The test statistic simplifies to the raw ratio of sample variances:

$$F = \frac{S_X^2}{S_Y^2}$$

Therefore, under $H_0$:

$$F = \frac{S_X^2}{S_Y^2} \sim F_{\nu_1, \nu_2} = F_{n-1, m-1}$$

This exact result enables exact finite-sample two-sample tests of variance equality.

### Solution, step 3: Expected Value Derivation and Jensen's Inequality Paradox
To compute $\mathbb{E}[F]$, express $F$ as:

$$F = \frac{U_1 / \nu_1}{U_2 / \nu_2} = \left( \frac{U_1}{\nu_1} \right) \cdot \left( \frac{\nu_2}{U_2} \right)$$

Because $U_1$ and $U_2$ are independent, the expectation of their product factorizes:

$$\mathbb{E}[F] = \mathbb{E}\left[ \frac{U_1}{\nu_1} \right] \cdot \mathbb{E}\left[ \frac{\nu_2}{U_2} \right] = \frac{1}{\nu_1} \mathbb{E}[U_1] \cdot \nu_2 \mathbb{E}\left[ \frac{1}{U_2} \right]$$

Since $U_1 \sim \chi_{\nu_1}^2$, its expected value is $\mathbb{E}[U_1] = \nu_1$. Thus, $\frac{1}{\nu_1}\mathbb{E}[U_1] = 1$.
Now evaluate $\mathbb{E}[1/U_2]$, where $U_2 \sim \chi_{\nu_2}^2$ with density $f_{U_2}(u) = \frac{1}{2^{\nu_2/2}\Gamma(\nu_2/2)} u^{\nu_2/2 - 1} e^{-u/2}$:

$$\mathbb{E}\left[ \frac{1}{U_2} \right] = \int_0^\infty \frac{1}{u} \frac{1}{2^{\nu_2/2}\Gamma(\nu_2/2)} u^{\frac{\nu_2}{2} - 1} e^{-u/2} \, du = \frac{1}{2^{\nu_2/2}\Gamma(\nu_2/2)} \int_0^\infty u^{\frac{\nu_2}{2} - 2} e^{-u/2} \, du$$

The integral converges if and only if $\frac{\nu_2}{2} - 1 > 0$, which requires $\nu_2 > 2$.
Using the Gamma identity $\int_0^\infty u^{a - 1} e^{-u/2} \, du = 2^a \Gamma(a)$ with $a = \frac{\nu_2}{2} - 1$:

$$\int_0^\infty u^{\frac{\nu_2}{2} - 2} e^{-u/2} \, du = 2^{\frac{\nu_2}{2} - 1} \Gamma\left( \frac{\nu_2}{2} - 1 \right)$$

Substitute this back into the expectation:

$$\mathbb{E}\left[ \frac{1}{U_2} \right] = \frac{2^{\frac{\nu_2}{2} - 1} \Gamma\left( \frac{\nu_2}{2} - 1 \right)}{2^{\frac{\nu_2}{2}} \Gamma\left( \frac{\nu_2}{2} \right)} = \frac{1}{2} \frac{\Gamma\left( \frac{\nu_2}{2} - 1 \right)}{\left( \frac{\nu_2}{2} - 1 \right) \Gamma\left( \frac{\nu_2}{2} - 1 \right)} = \frac{1}{2\left( \frac{\nu_2 - 2}{2} \right)} = \frac{1}{\nu_2 - 2}$$

Multiplying by $\nu_2$:

$$\mathbb{E}[F] = 1 \cdot \nu_2 \left( \frac{1}{\nu_2 - 2} \right) = \frac{\nu_2}{\nu_2 - 2} \quad \text{for } \nu_2 > 2$$

Notice that for any finite $\nu_2 > 2$:

$$\frac{\nu_2}{\nu_2 - 2} = 1 + \frac{2}{\nu_2 - 2} > 1$$

Even when both populations possess identical variances ($\sigma_X^2 = \sigma_Y^2$), the expected value of the sample variance ratio $S_X^2 / S_Y^2$ is strictly greater than 1!
This apparent paradox is a direct consequence of **Jensen's Inequality**: because the function $g(u) = 1/u$ is strictly convex for $u > 0$, $\mathbb{E}[1/U_2] > 1/\mathbb{E}[U_2] = 1/\nu_2$. The reciprocal of the sample variance places disproportionate upward probability mass when $S_Y^2$ is close to zero, pulling the expected value above 1. As $\nu_2 \to \infty$, $\frac{\nu_2}{\nu_2 - 2} \to 1$, vanishing in large samples.

### Solution, step 4: Reciprocal Quantile Relationship for Upper and Lower Tails
Let $F \sim F_{\nu_1, \nu_2}$. By definition of the critical value $F_{\alpha, \nu_1, \nu_2}$, the upper-tail probability is:

$$P\left( F \ge F_{\alpha, \nu_1, \nu_2} \right) = \alpha$$

Equivalently, the lower-tail probability is:

$$P\left( F \le F_{1 - \alpha, \nu_1, \nu_2} \right) = \alpha$$

Now invert the inequality inside the probability:

$$P\left( F \le F_{1 - \alpha, \nu_1, \nu_2} \right) = P\left( \frac{1}{F} \ge \frac{1}{F_{1 - \alpha, \nu_1, \nu_2}} \right) = \alpha$$

From Section 3.9, the reciprocal variable follows an inverted degrees-of-freedom distribution:

$$\frac{1}{F} \sim F_{\nu_2, \nu_1}$$

By definition of the upper-tail quantile for $F_{\nu_2, \nu_1}$:

$$P\left( F_{\nu_2, \nu_1} \ge F_{\alpha, \nu_2, \nu_1} \right) = \alpha$$

Comparing the two statements:

$$\frac{1}{F_{1 - \alpha, \nu_1, \nu_2}} = F_{\alpha, \nu_2, \nu_1} \implies F_{1 - \alpha, \nu_1, \nu_2} = \frac{1}{F_{\alpha, \nu_2, \nu_1}}$$

This identity is of great practical utility: standard published statistical tables tabulate only upper-tail critical values (e.g., $\alpha = 0.05, 0.01$). To find a lower-tail critical value for $F_{\nu_1, \nu_2}$, an analyst simply takes the reciprocal of the upper-tail critical value with the degrees of freedom swapped ($F_{\alpha, \nu_2, \nu_1}$).
