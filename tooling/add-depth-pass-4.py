# tooling/add-depth-pass-4.py

# 1. Expand Unit 8
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "r", encoding="utf-8") as f:
    u8 = f.read()

u8_addition = r"""

---

## 8.11 Linear Mixed-Effects Models: Crossed vs Nested Random Effects and REML Estimation

In hierarchical, longitudinal, and grouped observational studies (e.g. repeated student test scores nested within classrooms, or multi-center clinical trials), observations within the same group share unobserved cluster-specific latent variables.

To model intra-cluster correlation without consuming excessive degrees of freedom, statisticians deploy **Linear Mixed-Effects Models (LMMs)**, formalized by Nan Laird and James Ware (1982) and implemented in R's `lme4` (`lmer`) and Python's `statsmodels.mixedlm`:

$$\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \mathbf{Z} \mathbf{u} + \boldsymbol{\epsilon}$$

where:
- $\mathbf{X} \in \mathbb{R}^{n \times p}$ is the fixed-effects design matrix, with population parameters $\boldsymbol{\beta} \in \mathbb{R}^p$.
- $\mathbf{Z} \in \mathbb{R}^{n \times q}$ is the random-effects design matrix, with cluster random effects $\mathbf{u} \sim \mathcal{N}(\mathbf{0}, \mathbf{G})$.
- $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I}_n)$ is the residual error vector, independent of $\mathbf{u}$.

The marginal distribution of the response is Gaussian with block-compound covariance:
$$\mathbf{y} \sim \mathcal{N}(\mathbf{X} \boldsymbol{\beta}, \, \mathbf{V}), \quad \mathbf{V} = \mathbf{Z} \mathbf{G} \mathbf{Z}^\top + \sigma^2 \mathbf{I}_n$$

### Extended Formula Syntax in `lme4`: Random Intercepts and Slopes

The Wilkinson–Rogers formula is extended by adding grouping conditioning bars `(... | group)`:

1. **Random Intercepts Model**:
   ```r
   y ~ x + (1 | school)
   ```
   Specifies that each school has its own baseline intercept $u_{0i}$, shifting the regression line vertically while keeping the slope $\beta_1$ constant across all schools.

2. **Correlated Random Intercepts and Slopes**:
   ```r
   y ~ x + (x | school)   # Equivalent to (1 + x | school)
   ```
   Allows both the baseline intercept $u_{0i}$ and the treatment slope $u_{1i}$ to vary across schools, estimating their joint $2 \times 2$ covariance matrix:
   $$\mathbf{G} = \begin{bmatrix} \sigma_{u0}^2 & \rho \sigma_{u0} \sigma_{u1} \\ \rho \sigma_{u0} \sigma_{u1} & \sigma_{u1}^2 \end{bmatrix}$$

3. **Uncorrelated Random Intercepts and Slopes**:
   ```r
   y ~ x + (1 | school) + (0 + x | school)
   ```
   Forces the correlation parameter $\rho = 0$, reducing parameters to two independent variances.

4. **Crossed vs Nested Groupings**:
   - **Nested Grouping (`(1 | district / school)`)**: Schools are unique to specific districts (school 1 in district A is completely distinct from school 1 in district B). Expands to: `(1 | district) + (1 | district:school)`.
   - **Crossed Grouping (`(1 | subject) + (1 | item)`)**: In psychometrics or consumer testing, every subject evaluates multiple items, and every item is evaluated by multiple subjects. Neither factor is nested within the other. `lme4` solves crossed random effects using sparse Cholesky algorithms (`CHOLMOD`), factorizing sparse matrices with hundreds of thousands of random effects in seconds.

### Restricted Maximum Likelihood (REML) vs Standard Maximum Likelihood (ML)

When estimating the variance components $\mathbf{G}$ and $\sigma^2$:
- **Standard Maximum Likelihood (ML)**: Jointly maximizes $L(\boldsymbol{\beta}, \mathbf{V} \mid \mathbf{y})$. However, ML treats the fixed-effects $\boldsymbol{\beta}$ as known without penalizing for the $p$ degrees of freedom consumed in estimating $\boldsymbol{\beta}$. Consequently, ML variance estimates $\hat{\sigma}^2$ and $\hat{\mathbf{G}}$ are **negatively biased** (underestimated by a factor of $(n - p)/n$), exactly like dividing by $n$ instead of $n - 1$ in sample variance.
- **Restricted Maximum Likelihood (REML)** (Patterson and Thompson, 1971):
  REML transforms the data via an orthogonal linear projection $\mathbf{A} \in \mathbb{R}^{(n - p) \times n}$ such that $\mathbf{A} \mathbf{X} = \mathbf{0}$.
  The transformed vector $\mathbf{w} = \mathbf{A} \mathbf{y}$ satisfies:
  $$\mathbf{w} \sim \mathcal{N}(\mathbf{0}, \, \mathbf{A} \mathbf{V} \mathbf{A}^\top)$$
  The fixed effects $\boldsymbol{\beta}$ **vanish completely from the likelihood**! REML maximizes the likelihood of the error contrasts, producing strictly **unbiased, design-consistent estimates of all variance and covariance components**.
"""

marker = "## Fully worked question 1:"
idx = u8.find(marker)
u8_new = u8[:idx] + u8_addition.strip() + "\n\n" + u8[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "w", encoding="utf-8") as f:
    f.write(u8_new)
print("Expanded Unit 8 pass 4!")

# 2. Expand Unit 7
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "r", encoding="utf-8") as f:
    u7 = f.read()

u7_addition = r"""

---

## 7.11 Profile Likelihoods and the Backfitting Algorithm in Additive Modeling

In semiparametric statistics and high-dimensional regression, optimization criteria often partition naturally into primary parameters of scientific interest $\boldsymbol{\theta} \in \mathbb{R}^p$ (e.g. treatment effect) and high-dimensional nuisance parameters $\boldsymbol{\eta} \in \mathbb{R}^q$ (e.g. baseline hazards, non-parametric smoothers, or nuisance intercepts).

### The Profile Likelihood Method

Let $\ell(\boldsymbol{\theta}, \boldsymbol{\eta})$ be the joint log-likelihood. To eliminate the $q$ nuisance parameters without integrating them out (as in Bayesian marginalization), classical likelihood theory defines the **Profile Log-Likelihood**:

$$\ell_{prof}(\boldsymbol{\theta}) = \max_{\boldsymbol{\eta}} \ell(\boldsymbol{\theta}, \boldsymbol{\eta}) = \ell(\boldsymbol{\theta}, \, \hat{\boldsymbol{\eta}}(\boldsymbol{\theta}))$$

where $\hat{\boldsymbol{\eta}}(\boldsymbol{\theta}) = \arg\max_{\boldsymbol{\eta}} \ell(\boldsymbol{\theta}, \boldsymbol{\eta})$ is the restricted maximum likelihood estimate of the nuisance parameters for any fixed $\boldsymbol{\theta}$.

#### Theoretical Properties of the Profile Likelihood:
1. **Identical Point Estimates**: The global maximum of the profile likelihood matches the joint MLE:
   $$\hat{\boldsymbol{\theta}}_{MLE} = \arg\max_{\boldsymbol{\theta}} \ell_{prof}(\boldsymbol{\theta})$$
2. **Profile Score Function**: By the chain rule:
   $$\frac{d \ell_{prof}}{d\boldsymbol{\theta}} = \left. \frac{\partial \ell}{\partial \boldsymbol{\theta}} \right|_{\boldsymbol{\eta} = \hat{\boldsymbol{\eta}}} + \left. \frac{\partial \ell}{\partial \boldsymbol{\eta}} \right|_{\boldsymbol{\eta} = \hat{\boldsymbol{\eta}}} \frac{d\hat{\boldsymbol{\eta}}}{d\boldsymbol{\theta}}$$
   Because $\hat{\boldsymbol{\eta}}$ maximizes $\ell$ with respect to $\boldsymbol{\eta}$, the stationary condition requires $\left. \frac{\partial \ell}{\partial \boldsymbol{\eta}} \right|_{\boldsymbol{\eta} = \hat{\boldsymbol{\eta}}} = \mathbf{0}$.
   The second term vanishes! The profile score is simply the ordinary score evaluated at the constrained MLE:
   $$\nabla_{\boldsymbol{\theta}} \ell_{prof}(\boldsymbol{\theta}) = \nabla_{\boldsymbol{\theta}} \ell(\boldsymbol{\theta}, \, \hat{\boldsymbol{\eta}}(\boldsymbol{\theta}))$$
3. **Profile Likelihood Confidence Intervals**:
   Inverting the likelihood ratio test on the profile curve produces Wilks confidence intervals:
   $$\text{CI}_{1-\alpha} = \{ \boldsymbol{\theta} : 2 [\ell_{prof}(\hat{\boldsymbol{\theta}}) - \ell_{prof}(\boldsymbol{\theta})] \le \chi_{p, 1-\alpha}^2 \}$$
   These profile intervals properly reflect the statistical uncertainty of estimating the nuisance parameters $\boldsymbol{\eta}$, providing far superior coverage over standard Wald intervals when nuisance parameters are non-linearly constrained.

### The Backfitting Algorithm for Generalized Additive Models

In Generalized Additive Models (GAMs), the additive predictor is a sum of $p$ smooth univariate functions:

$$\mathbb{E}[Y \mid \mathbf{X}] = \alpha + \sum_{j=1}^p f_j(X_j)$$

where each $f_j$ is an unknown smooth curve constrained to have zero mean ($\sum_{i=1}^n f_j(x_{ij}) = 0$).
Fitting all $p$ functions simultaneously via a single high-dimensional spline matrix can be memory-intensive.

Trevor Hastie and Robert Tibshirani (1990) formulated the **Backfitting Algorithm**, which decouples the multivariate problem into a sequence of simple 1D smoothing operations.

#### Algorithmic Recurrence:
1. Initialize $\alpha = \frac{1}{n} \sum y_i$, and $f_1^{(0)} = f_2^{(0)} = \dots = f_p^{(0)} = \mathbf{0}$.
2. In a cyclic loop $j = 1, 2, \dots, p$:
   - Form the **partial residual vector** by subtracting the current fitted effects of all other $p - 1$ predictors:
     $$\mathbf{r}_j = \mathbf{y} - \alpha \mathbf{1} - \sum_{k \ne j} \mathbf{f}_k$$
   - Apply a univariate smoother $\mathcal{S}_j$ (such as LOESS, smoothing spline, or local linear regression) to predict the partial residual from predictor $X_j$:
     $$\mathbf{f}_j \leftarrow \mathcal{S}_j(\mathbf{r}_j \mid \mathbf{X}_j)$$
   - Center the updated curve: $\mathbf{f}_j \leftarrow \mathbf{f}_j - \text{mean}(\mathbf{f}_j)$.
3. Repeat step 2 until the relative change in all function estimates falls below convergence threshold $\epsilon$.

#### Gauss–Seidel Convergence:
Hastie and Tibshirani proved that if the individual smoothers $\mathcal{S}_j$ are linear operators ($\mathbf{f}_j = \mathbf{S}_j \mathbf{r}_j$) and self-adjoint (symmetric) with eigenvalues bounded in $[0, 1]$, the Backfitting algorithm is mathematically equivalent to the **Gauss–Seidel iterative solver** for the linear operator equation $(\mathbf{I} - \mathbf{M}) \mathbf{f} = \mathbf{d}$, guaranteeing global convergence to a unique stationary smooth surface.
"""

marker = "## Fully worked question 1:"
idx = u7.find(marker)
u7_new = u7[:idx] + u7_addition.strip() + "\n\n" + u7[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "w", encoding="utf-8") as f:
    f.write(u7_new)
print("Expanded Unit 7 pass 4!")

# 3. Expand Unit 5
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "r", encoding="utf-8") as f:
    u5 = f.read()

u5_addition = r"""

---

## 5.11 Multi-Level Monte Carlo (MLMC) and Variational Inference (VI)

In advanced computational mathematics and high-dimensional Bayesian statistics, researchers bridge stochastic simulation with analytical optimization using **Multi-Level Monte Carlo (MLMC)** and **Variational Inference (VI)**.

### Multi-Level Monte Carlo (Michael Giles, 2008)

In stochastic differential equations (SDEs) and continuous-time finance, evaluating expected payoffs $\mathbb{E}[P]$ requires discretizing continuous time using numerical Euler–Maruyama schemes with time step $h$.
- Small step size $h$ reduces discretization bias, but makes each path simulation computationally expensive.
- Standard Monte Carlo requires $N = \mathcal{O}(\epsilon^{-2})$ paths at fine step $h = \mathcal{O}(\epsilon)$, requiring total computational cost $\mathcal{O}(\epsilon^{-3})$.

Michael Giles formulated **Multi-Level Monte Carlo (MLMC)**, which deploys a geometric hierarchy of discretization levels $\ell = 0, 1, \dots, L$ with step sizes $h_\ell = M^{-\ell} h_0$ (e.g. $M = 2$ or $4$).

By the telescoping sum identity:

$$\mathbb{E}[P_L] = \mathbb{E}[P_0] + \sum_{\ell=1}^L \mathbb{E}[P_\ell - P_{\ell-1}]$$

Instead of simulating millions of paths at the ultra-fine level $L$, MLMC:
1. Simulates a large number of independent paths at the cheap coarse level $\ell = 0$ to estimate $\mathbb{E}[P_0]$.
2. Simulates a small number of coupled path pairs $(P_\ell, P_{\ell-1})$ using the **exact same Brownian motion path** at each level $\ell \ge 1$ to estimate the correction differences $\mathbb{E}[P_\ell - P_{\ell-1}]$.

Because the coupled paths share identical Brownian increments, the variance of the difference decays exponentially with level:
$$\text{Var}(P_\ell - P_{\ell-1}) = \mathcal{O}(h_\ell^\beta)$$
MLMC slashes the total computational complexity from $\mathcal{O}(\epsilon^{-3})$ down to **$\mathcal{O}(\epsilon^{-2})$—the exact theoretical minimum possible for independent Monte Carlo integration**!

### Variational Inference: Transforming Integration into Optimization

In massive Bayesian inference where MCMC sampling is too slow, **Variational Inference (VI)** (David Blei, Alp Kucukelbir, Jon McAuliffe, 2017) reframes posterior integration as a deterministic optimization problem.

Instead of generating stochastic Markov chain samples from the true posterior $p(\boldsymbol{\theta} \mid \mathbf{y})$, VI posits a tractable parametric family of distributions $q(\boldsymbol{\theta} \mid \boldsymbol{\phi})$ (the **variational family**) and optimizes the variational parameters $\boldsymbol{\phi}$ to minimize the Kullback–Leibler divergence to the true posterior:

$$\boldsymbol{\phi}^* = \arg\min_{\boldsymbol{\phi}} \mathcal{D}_{KL}(q(\boldsymbol{\theta} \mid \boldsymbol{\phi}) \,\|\, p(\boldsymbol{\theta} \mid \mathbf{y}))$$

As derived in Section 7.5, minimizing KL divergence is mathematically equivalent to maximizing the **Evidence Lower Bound (ELBO)**:

$$\text{ELBO}(\boldsymbol{\phi}) = \mathbb{E}_{q}[\ln p(\mathbf{y}, \boldsymbol{\theta})] - \mathbb{E}_{q}[\ln q(\boldsymbol{\theta} \mid \boldsymbol{\phi})]$$

#### The Mean-Field Variational Family:
The classic mean-field approximation assumes the parameters factorize completely into independent univariate marginals:
$$q(\boldsymbol{\theta}) = \prod_{j=1}^p q_j(\theta_j)$$
Under mean-field assumptions, the optimal coordinate updates satisfy:
$$\ln q_j^*(\theta_j) = \mathbb{E}_{-j}[\ln p(\mathbf{y}, \boldsymbol{\theta})] + \text{constant}$$
Coordinate Ascent Variational Inference (CAVI) updates each variational factor in turn. For complex non-conjugate models, **Black-Box Variational Inference (BBVI)** uses stochastic gradient ascent on the ELBO with score function estimators (REINFORCE) or the pathwise reparameterization trick ($\boldsymbol{\theta} = g(\boldsymbol{\epsilon}, \boldsymbol{\phi})$ with $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$), bringing Bayesian inference to datasets containing hundreds of millions of observations.
"""

marker = "## Fully worked question 1:"
idx = u5.find(marker)
u5_new = u5[:idx] + u5_addition.strip() + "\n\n" + u5[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "w", encoding="utf-8") as f:
    f.write(u5_new)
print("Expanded Unit 5 pass 4!")

# 4. Expand Unit 4
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "r", encoding="utf-8") as f:
    u4 = f.read()

u4_addition = r"""

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
"""

marker = "## Fully worked question 1:"
idx = u4.find(marker)
u4_new = u4[:idx] + u4_addition.strip() + "\n\n" + u4[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "w", encoding="utf-8") as f:
    f.write(u4_new)
print("Expanded Unit 4 pass 4!")
