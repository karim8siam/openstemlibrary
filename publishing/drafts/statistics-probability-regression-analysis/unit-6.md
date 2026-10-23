# Unit 6: Multicollinearity, Variance Inflation, Regularized Shrinkage (Ridge & LASSO) & Dimension Reduction

In the classical multiple linear regression model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $\mathbb{E}[\boldsymbol{\varepsilon} \mid \mathbf{X}] = \mathbf{0}$ and $\operatorname{Var}(\boldsymbol{\varepsilon} \mid \mathbf{X}) = \sigma^2 \mathbf{I}_n$, the Gauss–Markov assumption that the $n \times p$ design matrix $\mathbf{X}$ has full column rank ($\operatorname{rank}(\mathbf{X}) = p$) is technically a binary mathematical condition: either the columns of $\mathbf{X}$ are linearly independent, in which case the Gram matrix $\mathbf{X}^\top \mathbf{X}$ is strictly positive definite and the unique Ordinary Least Squares estimator $\hat{\boldsymbol{\beta}}_{\text{OLS}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{Y}$ exists, or they are linearly dependent, in which case $\mathbf{X}^\top \mathbf{X}$ is singular and $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ is non-unique. In computational statistics and applied econometrics, however, conditioning is a continuous spectrum rather than a binary dichotomy. When explanatory variables exhibit strong—though imperfect—linear dependencies across observations, the regression model suffers from **near multicollinearity** (or **ill-conditioning**). Under severe multicollinearity, the Gram matrix $\mathbf{X}^\top \mathbf{X}$ lies perilously close to the boundary of singularity: its smallest eigenvalues approach zero, its determinant collapses, and the elements of $(\mathbf{X}^\top \mathbf{X})^{-1}$ explode in magnitude.

Although near multicollinearity violates none of the Gauss–Markov assumptions—leaving $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ unbiased and formally BLUE—it renders the unbiased estimator practically unusable when $p$ is moderate or large or when predictors move together. Because the trace of the covariance matrix $\operatorname{tr}(\operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}})) = \sigma^2 \sum_{j=1}^p \lambda_j^{-1}$ is dominated by the reciprocal of the smallest eigenvalue $\lambda_{\min}(\mathbf{X}^\top \mathbf{X})$, the expected squared Euclidean distance between $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ and the true vector $\boldsymbol{\beta}$ becomes enormous. Individual regression coefficients become acutely sensitive to tiny perturbations in the data, display counterintuitive algebraic signs, and exhibit inflated standard errors that mask genuine structural relationships (producing a high overall ANOVA $F$-statistic alongside individually insignificant $t$-statistics). Overcoming this pathology requires stepping outside the restrictive class of unbiased linear estimators. By introducing a controlled, deliberate shrinkage bias—either via quadratic $\ell_2$ penalization (**Hoerl–Kennard Ridge Regression**), sparsity-inducing $\ell_1$ penalization (**Tibshirani's LASSO**), hybrid $\ell_1/\ell_2$ penalization (**Elastic Net**), or spectral subspace projection (**Principal Component Regression** and **Partial Least Squares**)—we can dramatically reduce estimation variance and achieve substantially lower Mean Squared Error (MSE) than OLS.

---

## 6.1 Exact Versus Near Multicollinearity: Geometry of Ill-Conditioned Gram Matrices, Determinant Collapse, and Parameter Instability

Let $\mathbf{X} = [\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_p] \in \mathbb{R}^{n \times p}$ denote the design matrix of $p$ predictors (or let $\mathbf{X}$ denote the $n \times k$ matrix of centered and standardized non-constant predictors after sweeping out the intercept via the Frisch–Waugh–Lovell theorem, so that $\mathbf{X}^\top \mathbf{X} = \mathbf{R}_{XX}$ is the $k \times k$ sample correlation matrix of the explanatory variables).

### Exact (Perfect) Multicollinearity and Non-Identifiability

**Exact multicollinearity** occurs when there exists a non-zero vector $\mathbf{c} = (c_1, c_2, \dots, c_p)^\top \neq \mathbf{0}$ such that an exact linear combination of the columns of $\mathbf{X}$ vanishes across all $n$ observations in the sample:

$$\sum_{j=1}^p c_j \mathbf{x}_j = \mathbf{X}\mathbf{c} = \mathbf{0}_{n \times 1}$$

Equivalently, $\operatorname{rank}(\mathbf{X}) < p$, which implies $\operatorname{rank}(\mathbf{X}^\top \mathbf{X}) < p$ and $\det(\mathbf{X}^\top \mathbf{X}) = 0$. What happens to the normal equations $(\mathbf{X}^\top \mathbf{X})\hat{\boldsymbol{\beta}} = \mathbf{X}^\top \mathbf{Y}$ when $\mathbf{X}\mathbf{c} = \mathbf{0}$?
1. **Uniqueness of the Fitted Projection $\hat{\mathbf{Y}}$**: Because the column space $\mathcal{C}(\mathbf{X}) \subset \mathbb{R}^n$ is a well-defined linear subspace of dimension $r = \operatorname{rank}(\mathbf{X}) < p$, the orthogonal projection $\hat{\mathbf{Y}} = \mathbf{P}_{\mathcal{C}(\mathbf{X})}\mathbf{Y}$ of $\mathbf{Y}$ onto $\mathcal{C}(\mathbf{X})$ (and hence the residual vector $\mathbf{e} = \mathbf{Y} - \hat{\mathbf{Y}}$ and $\text{SSE} = \mathbf{e}^\top \mathbf{e}$) remains **completely unique**! Specifically, for any generalized inverse $(\mathbf{X}^\top \mathbf{X})^-$ satisfying $(\mathbf{X}^\top \mathbf{X})(\mathbf{X}^\top \mathbf{X})^-(\mathbf{X}^\top \mathbf{X}) = \mathbf{X}^\top \mathbf{X}$, the projection matrix $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top \mathbf{X})^-\mathbf{X}^\top$ is invariant to the choice of generalized inverse.
2. **Non-Identifiability of the Parameter Vector $\boldsymbol{\beta}$**: If $\hat{\boldsymbol{\beta}}_0 = (\mathbf{X}^\top \mathbf{X})^-\mathbf{X}^\top \mathbf{Y}$ is any particular solution to the normal equations, then for every scalar $\alpha \in \mathbb{R}$, the shifted vector $\hat{\boldsymbol{\beta}}(\alpha) = \hat{\boldsymbol{\beta}}_0 + \alpha \mathbf{c}$ generates the exact same fitted values:

$$\mathbf{X}\hat{\boldsymbol{\beta}}(\alpha) = \mathbf{X}\hat{\boldsymbol{\beta}}_0 + \alpha (\mathbf{X}\mathbf{c}) = \mathbf{X}\hat{\boldsymbol{\beta}}_0 + \mathbf{0} = \hat{\mathbf{Y}}$$

Thus, there exists an infinite affine subspace of solutions $\hat{\boldsymbol{\beta}}_0 + \operatorname{Null}(\mathbf{X})$ that achieve the exact same minimum sum of squared residuals $\text{SSE}$. Individual parameters $\beta_j$ associated with nonzero entries of $\mathbf{c}$ are **statistically unidentifiable**: the data cannot distinguish the separate partial effect of $X_j$ holding other variables constant because $X_j$ cannot vary independently of the other predictors in the sample. (Only linear functions $\boldsymbol{\ell}^\top \boldsymbol{\beta}$ where $\boldsymbol{\ell} \in \mathcal{R}(\mathbf{X}^\top \mathbf{X}) = \operatorname{Null}(\mathbf{X})^\perp$ are **estimable**).

### Near (Approximate) Multicollinearity and Geometric Instability

In practice, exact linear dependence usually arises from deterministic specification errors—such as including all $m$ dummy variables for an $m$-category factor alongside an intercept (the **Dummy Variable Trap**), including both nominal income, real income, and the price deflator in logarithmic form ($\ln Y_{\text{real}} = \ln Y_{\text{nom}} - \ln P$), or having fewer observations than parameters ($n < p$). Far more pervasive is **near multicollinearity**, where no exact vector $\mathbf{c} \neq \mathbf{0}$ satisfies $\mathbf{X}\mathbf{c} = \mathbf{0}$, but there exists a unit vector $\mathbf{c}$ ($\|\mathbf{c}\|_2 = 1$) such that:

$$\|\mathbf{X}\mathbf{c}\|_2^2 = \mathbf{c}^\top (\mathbf{X}^\top \mathbf{X})\mathbf{c} = \varepsilon \ll 1$$

Geometrically, in $n$-dimensional observation space $\mathbb{R}^n$, the column vectors $\mathbf{x}_1, \dots, \mathbf{x}_p$ span a $p$-dimensional hyperplane $\mathcal{C}(\mathbf{X})$, but two or more vectors point in nearly identical (or nearly opposite) directions, separated by a tiny acute angle $\theta \approx 0$. Just as attempting to balance a flat tabletop on two support legs placed only a millimeter apart results in wild tilting along the perpendicular axis whenever a speck of dust lands on the surface, projecting $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ onto two nearly collinear vectors $\mathbf{x}_1$ and $\mathbf{x}_2$ requires huge, oppositely signed coordinates $\hat{\beta}_1 \gg 0$ and $\hat{\beta}_2 \ll 0$ to represent small orthogonal components of the noise vector $\boldsymbol{\varepsilon}$.

### Practical Symptoms of Severe Multicollinearity in Empirical Regression

When near multicollinearity is present, standard OLS output exhibits a characteristic syndrome of diagnostic anomalies:
1. **The High-$R^2$ / Few-Significant-$t$-Ratios Paradox**: The overall regression achieves a very high coefficient of determination $R^2$ and a highly significant omnibus ANOVA $F$-test (rejecting $H_0: \beta_1 = \dots = \beta_k = 0$ with a tiny $p$-value), yet the individual partial $t$-statistics $t_j = \hat{\beta}_j / \operatorname{SE}(\hat{\beta}_j)$ for the collinear predictors are statistically insignificant! Because the predictors move together, the data confirm with high certainty that the *group* of variables jointly predicts $\mathbf{Y}$, but cannot apportion credit among individual members of the group.
2. **Strong Negative Correlation Between Estimated Coefficients**: If two standardized predictors $X_1$ and $X_2$ have a strong positive correlation $r_{12} > 0$, their OLS slope estimators $\hat{\beta}_1$ and $\hat{\beta}_2$ exhibit a strong **negative** sampling correlation $\operatorname{Corr}(\hat{\beta}_1, \hat{\beta}_2) = -r_{12} < 0$. An overestimate of $\beta_1$ in a given sample is automatically compensated by a corresponding underestimate of $\beta_2$ so that the sum $\hat{\beta}_1 X_{i1} + \hat{\beta}_2 X_{i2}$ remains close to $Y_i$.
3. **Extreme Sensitivity to Sample Perturbations**: Deleting or adding a single observation, or perturbing $Y_i$ in the third decimal place, can cause $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ to swing dramatically in magnitude and even flip algebraic sign.

---

## 6.2 Variance Inflation Factors ($\text{VIF}_j = \frac{1}{1 - R_j^2}$), Tolerance, and Partitioned Matrix Derivation

To quantify the exact factor by which multicollinearity inflates the sampling variance of the $j$-th regression coefficient $\hat{\beta}_j$, let us center all variables around their sample means and standardize each predictor so that $\mathbf{z}_j = \frac{\mathbf{x}_j - \bar{x}_j \mathbf{1}_n}{\sqrt{S_{x_j x_j}}}$ has unit length ($\mathbf{z}_j^\top \mathbf{z}_j = 1$). Let $\mathbf{Z} = [\mathbf{z}_1, \dots, \mathbf{z}_k] \in \mathbb{R}^{n \times k}$ be the standardized design matrix, so that $\mathbf{Z}^\top \mathbf{Z} = \mathbf{R}_{XX}$ is the $k \times k$ correlation matrix of the explanatory variables.

### Exact Derivation via the Frisch–Waugh–Lovell Theorem and Block Matrix Inversion

Without loss of generality, focus on the $j$-th original predictor $\mathbf{x}_j$ and partition the centered design matrix as $\tilde{\mathbf{X}} = [\tilde{\mathbf{x}}_j, \; \tilde{\mathbf{X}}_{-j}]$, where $\tilde{\mathbf{x}}_j = \mathbf{x}_j - \bar{x}_j \mathbf{1}_n$ is the centered $j$-th predictor (with sum of squares $S_{jj} = \tilde{\mathbf{x}}_j^\top \tilde{\mathbf{x}}_j = \sum_{i=1}^n (X_{ij} - \bar{X}_j)^2$) and $\tilde{\mathbf{X}}_{-j} \in \mathbb{R}^{n \times (k-1)}$ contains the remaining $k - 1$ centered predictors. The centered Gram matrix is partitioned into a $2 \times 2$ block matrix:

$$\tilde{\mathbf{X}}^\top \tilde{\mathbf{X}} = \begin{pmatrix} \tilde{\mathbf{x}}_j^\top \tilde{\mathbf{x}}_j & \tilde{\mathbf{x}}_j^\top \tilde{\mathbf{X}}_{-j} \\ \tilde{\mathbf{X}}_{-j}^\top \tilde{\mathbf{x}}_j & \tilde{\mathbf{X}}_{-j}^\top \tilde{\mathbf{X}}_{-j} \end{pmatrix}$$

By the Schur complement formula for the $(1, 1)$ entry of the inverse of a partitioned symmetric matrix (or equivalently by the Frisch–Waugh–Lovell theorem), the $(j, j)$ diagonal element of $(\tilde{\mathbf{X}}^\top \tilde{\mathbf{X}})^{-1}$ is the reciprocal of the Schur complement of $\tilde{\mathbf{X}}_{-j}^\top \tilde{\mathbf{X}}_{-j}$:

$$\left[ (\tilde{\mathbf{X}}^\top \tilde{\mathbf{X}})^{-1} \right]_{jj} = \left( \tilde{\mathbf{x}}_j^\top \tilde{\mathbf{x}}_j - \tilde{\mathbf{x}}_j^\top \tilde{\mathbf{X}}_{-j} (\tilde{\mathbf{X}}_{-j}^\top \tilde{\mathbf{X}}_{-j})^{-1} \tilde{\mathbf{X}}_{-j}^\top \tilde{\mathbf{x}}_j \right)^{-1} = \frac{1}{\tilde{\mathbf{x}}_j^\top (\mathbf{I}_n - \mathbf{H}_{-j}) \tilde{\mathbf{x}}_j}$$

where $\mathbf{H}_{-j} = \tilde{\mathbf{X}}_{-j} (\tilde{\mathbf{X}}_{-j}^\top \tilde{\mathbf{X}}_{-j})^{-1} \tilde{\mathbf{X}}_{-j}^\top$ is the orthogonal projection matrix onto the column space of the other $k - 1$ centered predictors! Now recognize what the quadratic form in the denominator represents:
- In an auxiliary OLS regression of $X_j$ on an intercept and all other $k - 1$ explanatory variables $X_1, \dots, X_{j-1}, X_{j+1}, \dots, X_k$:

$$X_{ij} = \alpha_0 + \sum_{\ell \neq j} \alpha_\ell X_{i\ell} + u_{ij}$$

  the total sum of squares of $X_j$ is $\text{SST}_j = \tilde{\mathbf{x}}_j^\top \tilde{\mathbf{x}}_j = S_{jj}$, the explained sum of squares is $\text{SSR}_j = \tilde{\mathbf{x}}_j^\top \mathbf{H}_{-j} \tilde{\mathbf{x}}_j$, and the residual sum of squares is $\text{SSE}_j = \tilde{\mathbf{x}}_j^\top (\mathbf{I}_n - \mathbf{H}_{-j}) \tilde{\mathbf{x}}_j$.
- Dividing $\text{SSE}_j$ by $\text{SST}_j = S_{jj}$ invokes the coefficient of determination $R_j^2 = \frac{\text{SSR}_j}{\text{SST}_j} = 1 - \frac{\text{SSE}_j}{\text{SST}_j}$ from regressing $X_j$ on the remaining $k - 1$ predictors:

$$\text{SSE}_j = \tilde{\mathbf{x}}_j^\top (\mathbf{I}_n - \mathbf{H}_{-j}) \tilde{\mathbf{x}}_j = S_{jj}\left(1 - R_j^2\right)$$

Substituting this exact identity into $\operatorname{Var}(\hat{\beta}_j) = \sigma^2 \left[(\tilde{\mathbf{X}}^\top \tilde{\mathbf{X}})^{-1}\right]_{jj}$ yields the fundamental variance decomposition of multiple regression:

$$\operatorname{Var}(\hat{\beta}_j) = \frac{\sigma^2}{S_{jj}\left(1 - R_j^2\right)} = \underbrace{\left(\frac{\sigma^2}{\sum_{i=1}^n (X_{ij} - \bar{X}_j)^2}\right)}_{\text{Orthogonal Benchmark Variance}} \times \underbrace{\left(\frac{1}{1 - R_j^2}\right)}_{\text{VIF}_j}$$

### Definition and Interpretation of $\text{VIF}_j$ and Tolerance

The multiplier that inflates $\operatorname{Var}(\hat{\beta}_j)$ relative to an ideal orthogonal design (where $X_j$ is uncorrelated with all other predictors, so $R_j^2 = 0$) is defined by Donald Marquardt (1970) as the **Variance Inflation Factor ($\text{VIF}_j$)**:

$$\text{VIF}_j = \frac{1}{1 - R_j^2} = \left(\mathbf{R}_{XX}^{-1}\right)_{jj}, \qquad \text{Tolerance}_j = \text{TOL}_j = \frac{1}{\text{VIF}_j} = 1 - R_j^2$$

Notice two critical mathematical facts:
1. **Diagonal of the Inverse Correlation Matrix**: $\text{VIF}_j$ is identically equal to the $j$-th diagonal element of the inverse of the $k \times k$ predictor correlation matrix $\mathbf{R}_{XX}^{-1}$.
2. **Standard Error Magnification**: Because standard errors are square roots of variances, $\operatorname{SE}(\hat{\beta}_j)$ and the width of the $100(1-\alpha)\%$ confidence interval for $\beta_j$ are multiplied by $\sqrt{\text{VIF}_j}$:
   - If $R_j^2 = 0.00$ (complete orthogonality): $\text{TOL}_j = 1.00$, $\text{VIF}_j = 1.0$, and $\sqrt{\text{VIF}_j} = 1.00$.
   - If $R_j^2 = 0.75$: $\text{TOL}_j = 0.25$, $\text{VIF}_j = 4.0$, and standard errors are doubled ($\sqrt{\text{VIF}_j} = 2.00$).
   - If $R_j^2 = 0.80$: $\text{TOL}_j = 0.20$, $\text{VIF}_j = 5.0$, and standard errors are inflated by $\sqrt{5} \approx 2.236$ (a common moderate-collinearity warning threshold).
   - If $R_j^2 = 0.90$: $\text{TOL}_j = 0.10$, $\text{VIF}_j = 10.0$, and standard errors are inflated by $\sqrt{10} \approx 3.162$ (the standard severe-collinearity cutoff).
   - If $R_j^2 = 0.99$: $\text{TOL}_j = 0.01$, $\text{VIF}_j = 100.0$, and standard errors explode $10$-fold!

---

## 6.3 Spectral Diagnostics: Singular Value Decomposition, Condition Indices, and Belsley–Kuh–Welsch Variance Decomposition Proportions

While Variance Inflation Factors clearly indicate *which* variables have inflated variances, $\text{VIF}_j$ suffers from two diagnostic limitations: first, it cannot distinguish whether a single near-linear dependency or several distinct coexisting linear dependencies are operating among the predictors; second, if a near-dependency involves the **intercept column** (for instance, when a continuous predictor such as absolute Kelvin temperature has a tiny coefficient of variation across observations, $\operatorname{SD}(X_j) / \bar{X}_j \ll 1$), centered correlation-based $\text{VIF}_j$ values completely miss the ill-conditioning of the uncentered matrix $\mathbf{X}$.

To resolve both limitations, David Belsley, Edwin Kuh, and Roy Welsch (1980) developed a comprehensive spectral diagnostic framework based on the **Singular Value Decomposition (SVD)** of the column-equilibrated $n \times p$ design matrix $\mathbf{X}$ (where each column, including the intercept, is scaled to have unit Euclidean norm $\|\mathbf{x}_j\|_2 = 1$).

### Singular Value Decomposition and the Spectral Condition Number

Any $n \times p$ matrix $\mathbf{X}$ ($n \ge p$) admits the thin Singular Value Decomposition:

$$\mathbf{X} = \mathbf{U} \mathbf{D} \mathbf{V}^\top = \sum_{\ell=1}^p \mu_\ell \mathbf{u}_\ell \mathbf{v}_\ell^\top$$

where:
- $\mathbf{U} = [\mathbf{u}_1, \dots, \mathbf{u}_p] \in \mathbb{R}^{n \times p}$ has orthonormal columns ($\mathbf{U}^\top \mathbf{U} = \mathbf{I}_p$) spanning $\mathcal{C}(\mathbf{X})$.
- $\mathbf{V} = [\mathbf{v}_1, \dots, \mathbf{v}_p] \in \mathbb{R}^{p \times p}$ is an orthogonal matrix ($\mathbf{V}^\top \mathbf{V} = \mathbf{V}\mathbf{V}^\top = \mathbf{I}_p$) whose columns $\mathbf{v}_\ell$ are the orthonormal right singular vectors (principal axes / eigenvectors of $\mathbf{X}^\top \mathbf{X}$).
- $\mathbf{D} = \operatorname{diag}(\mu_1, \mu_2, \dots, \mu_p)$ contains the ordered non-negative **singular values** $\mu_1 \ge \mu_2 \ge \dots \ge \mu_p \ge 0$.

Cross-multiplying $\mathbf{X}^\top \mathbf{X}$ immediately yields its orthogonal eigendecomposition:

$$\mathbf{X}^\top \mathbf{X} = \mathbf{V} \mathbf{D}^2 \mathbf{V}^\top = \mathbf{V} \boldsymbol{\Lambda} \mathbf{V}^\top = \sum_{\ell=1}^p \lambda_\ell \mathbf{v}_\ell \mathbf{v}_\ell^\top, \qquad \text{where } \lambda_\ell = \mu_\ell^2$$

Thus, the eigenvalues of $\mathbf{X}^\top \mathbf{X}$ are the squares of the singular values of $\mathbf{X}$ ($\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p > 0$), and the determinant is $\det(\mathbf{X}^\top \mathbf{X}) = \prod_{\ell=1}^p \lambda_\ell = \prod_{\ell=1}^p \mu_\ell^2$. Whenever one or more singular values $\mu_\ell$ approach zero, the corresponding eigenvectors $\mathbf{v}_\ell$ identify the exact linear combinations of columns that are nearly collinear ($\|\mathbf{X}\mathbf{v}_\ell\|_2 = \mu_\ell \approx 0$).

We define the **$\ell$-th Condition Index ($\eta_\ell$)** and the overall **Spectral Condition Number ($\kappa(\mathbf{X})$)** as:

$$\eta_\ell = \frac{\mu_{\max}}{\mu_\ell} = \frac{\mu_1}{\mu_\ell} = \sqrt{\frac{\lambda_1}{\lambda_\ell}} \quad (\ell = 1, \dots, p), \qquad \kappa(\mathbf{X}) = \eta_p = \frac{\mu_1}{\mu_p} = \sqrt{\frac{\lambda_{\max}(\mathbf{X}^\top \mathbf{X})}{\lambda_{\min}(\mathbf{X}^\top \mathbf{X})}}$$

By construction, $\eta_\ell \ge 1$, with $\eta_1 = 1$. If the columns of $\mathbf{X}$ are mutually orthonormal, all singular values equal $1$ and $\kappa(\mathbf{X}) = 1$. As collinearity intensifies, $\mu_p \to 0$ and $\kappa(\mathbf{X}) \to \infty$:
- **$10 \le \eta_\ell < 30$**: Indicates moderate to strong linear dependence associated with the $\ell$-th singular value.
- **$\eta_\ell \ge 30$** (equivalently $\lambda_1 / \lambda_\ell \ge 900$): Signals **severe multicollinearity**; the number of condition indices exceeding $30$ reveals the exact number of distinct near-linear dependencies present in $\mathbf{X}$.

### Belsley–Kuh–Welsch Variance Decomposition Proportions ($\pi_{\ell j}$)

Crucially, because $(\mathbf{X}^\top \mathbf{X})^{-1} = \mathbf{V} \mathbf{D}^{-2} \mathbf{V}^\top = \sum_{\ell=1}^p \frac{1}{\mu_\ell^2} \mathbf{v}_\ell \mathbf{v}_\ell^\top$, the sampling variance of the $j$-th regression coefficient $\hat{\beta}_j$ decomposes additively across the $p$ orthogonal principal components:

$$\operatorname{Var}(\hat{\beta}_j) = \sigma^2 \left[(\mathbf{X}^\top \mathbf{X})^{-1}\right]_{jj} = \sigma^2 \sum_{\ell=1}^p \frac{v_{j\ell}^2}{\mu_\ell^2} = \sigma^2 \sum_{\ell=1}^p \frac{v_{j\ell}^2}{\lambda_\ell}$$

where $v_{j\ell}$ is the $(j, \ell)$ entry of $\mathbf{V}$. Define $\phi_{j\ell} = \frac{v_{j\ell}^2}{\mu_\ell^2}$ and $\phi_j = \sum_{\ell=1}^p \phi_{j\ell}$. The **Variance Decomposition Proportion ($\pi_{\ell j}$)** is the fraction of the sampling variance of $\hat{\beta}_j$ attributable to the $\ell$-th singular value $\mu_\ell$:

$$\pi_{\ell j} = \frac{\phi_{j\ell}}{\phi_j} = \frac{v_{j\ell}^2 / \mu_\ell^2}{\sum_{m=1}^p \left(v_{jm}^2 / \mu_m^2\right)}, \qquad \sum_{\ell=1}^p \pi_{\ell j} = 1 \quad \text{for each } j = 1, \dots, p$$

**The Belsley–Kuh–Welsch Diagnostic Rule**: A degrading collinearity relation is diagnosed whenever **(i)** a singular value has a high condition index ($\eta_\ell \ge 30$) **and (ii)** two or more regression coefficients $\hat{\beta}_j, \hat{\beta}_m$ simultaneously have high variance decomposition proportions ($\pi_{\ell j} > 0.50$ and $\pi_{\ell m} > 0.50$) associated with that same singular value $\mu_\ell$.

---

## 6.4 Tikhonov Regularization and Hoerl–Kennard Ridge Regression: Spectral Shrinkage, Bias–Variance Trade-Off, and the Existence Theorem

When the eigenvalues $\lambda_\ell$ of $\mathbf{X}^\top \mathbf{X}$ are near zero, the total mean squared error (expected squared Euclidean distance) of the OLS estimator explodes:

$$\operatorname{MSE}(\hat{\boldsymbol{\beta}}_{\text{OLS}}) = \mathbb{E}\left[\|\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta}\|_2^2\right] = \operatorname{tr}\left(\operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}})\right) = \sigma^2 \operatorname{tr}\left((\mathbf{X}^\top \mathbf{X})^{-1}\right) = \sigma^2 \sum_{\ell=1}^p \frac{1}{\lambda_\ell}$$

If $\lambda_p = 10^{-4}$, then $1/\lambda_p = 10{,}000$, causing $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ to lie on average very far from the true parameter vector $\boldsymbol{\beta}$, with an inflated squared Euclidean norm $\mathbb{E}[\|\hat{\boldsymbol{\beta}}_{\text{OLS}}\|_2^2] = \|\boldsymbol{\beta}\|_2^2 + \sigma^2 \sum_{\ell=1}^p \frac{1}{\lambda_\ell} \gg \|\boldsymbol{\beta}\|_2^2$.

### Formulation of Hoerl–Kennard Ridge Regression (1970)

Drawing on Andrey Tikhonov's (1943) regularization theory for ill-posed inverse problems, Arthur Hoerl and Robert Kennard (1970) proposed adding a strictly positive scalar multiple $\lambda \mathbf{I}_p$ ($\lambda > 0$, often denoted $k > 0$) to the ill-conditioned Gram matrix $\mathbf{X}^\top \mathbf{X}$ before inversion. Equivalently, after centering $\mathbf{Y}$ and standardizing the $p$ predictors so that the intercept $\hat{\beta}_0 = \bar{Y}$ is estimated separately without penalization, **Ridge Regression** minimizes the $\ell_2$-penalized residual sum of squares:

$$\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) = \arg\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \left\{ \|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda \|\boldsymbol{\beta}\|_2^2 \right\} = \arg\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \left\{ (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) + \lambda \boldsymbol{\beta}^\top \boldsymbol{\beta} \right\}$$

By Lagrangian duality, this penalized unconstrained optimization is mathematically equivalent to the constrained optimization problem $\min_{\boldsymbol{\beta}} \|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2$ subject to the spherical Euclidean ball constraint $\|\boldsymbol{\beta}\|_2^2 \le t$ (where $t > 0$ has a one-to-one inverse correspondence with $\lambda > 0$). It also admits a **Bayesian Conjugate Normal Interpretation**: if the prior distribution on $\boldsymbol{\beta}$ is isotropic Gaussian $\boldsymbol{\beta} \sim \mathcal{N}_p(\mathbf{0}, \tau^2 \mathbf{I}_p)$ and the likelihood is $\mathbf{Y} \mid \boldsymbol{\beta} \sim \mathcal{N}_n(\mathbf{X}\boldsymbol{\beta}, \sigma^2 \mathbf{I}_n)$, then the posterior distribution $\boldsymbol{\beta} \mid \mathbf{Y}$ is Gaussian with posterior mean (and MAP mode) equal to $\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda)$ for $\lambda = \sigma^2 / \tau^2$.

Differentiating the Ridge objective $Q_\lambda(\boldsymbol{\beta}) = (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) + \lambda \boldsymbol{\beta}^\top \boldsymbol{\beta}$ with respect to $\boldsymbol{\beta}$ and setting the gradient to zero yields the **Ridge Normal Equations**:

$$\frac{\partial Q_\lambda(\boldsymbol{\beta})}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^\top \mathbf{Y} + 2(\mathbf{X}^\top \mathbf{X})\boldsymbol{\beta} + 2\lambda \mathbf{I}_p \boldsymbol{\beta} = \mathbf{0} \quad \Longrightarrow \quad \left(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p\right) \hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) = \mathbf{X}^\top \mathbf{Y}$$

Because the eigenvalues of $\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p$ are $\lambda_\ell + \lambda \ge \lambda > 0$, the matrix $\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p$ is **always strictly positive definite and invertible for every $\lambda > 0$**, even if $\operatorname{rank}(\mathbf{X}) < p$ or $p > n$! Its spectral condition number is stabilized to $\kappa\left(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p\right) = \frac{\lambda_1 + \lambda}{\lambda_p + \lambda} \ll \frac{\lambda_1}{\lambda_p}$. Solving for $\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda)$ gives:

$$\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) = \left(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p\right)^{-1} \mathbf{X}^\top \mathbf{Y} = \mathbf{W}_\lambda \hat{\boldsymbol{\beta}}_{\text{OLS}}$$

where $\mathbf{W}_\lambda = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p)^{-1}(\mathbf{X}^\top \mathbf{X}) = \left(\mathbf{I}_p + \lambda (\mathbf{X}^\top \mathbf{X})^{-1}\right)^{-1}$ is the linear shrinkage matrix.

### Spectral Filter Representation, Bias Vector, and Covariance Matrix

Substituting the Singular Value Decomposition $\mathbf{X} = \mathbf{U}\mathbf{D}\mathbf{V}^\top$ (with $\lambda_\ell = \mu_\ell^2$) into the Ridge estimator reveals how Ridge operates along each principal axis $\mathbf{v}_\ell$:

$$\mathbf{X}\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) = \mathbf{X}(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p)^{-1}\mathbf{X}^\top \mathbf{Y} = \sum_{\ell=1}^p \left(\frac{\lambda_\ell}{\lambda_\ell + \lambda}\right) \mathbf{u}_\ell \mathbf{u}_\ell^\top \mathbf{Y}, \qquad \hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) = \sum_{\ell=1}^p \left(\frac{\lambda_\ell}{\lambda_\ell + \lambda}\right) \frac{\mathbf{u}_\ell^\top \mathbf{Y}}{\mu_\ell} \mathbf{v}_\ell$$

Compared to OLS, which weights each principal direction by $1$, Ridge multiplies the $\ell$-th canonical component by the **spectral shrinkage factor** $f_\ell(\lambda) = \frac{\lambda_\ell}{\lambda_\ell + \lambda} \in (0, 1)$. Directions with large eigenvalues ($\lambda_\ell \gg \lambda$, high information) experience negligible shrinkage ($f_\ell(\lambda) \approx 1$), whereas collinear directions with tiny eigenvalues ($\lambda_\ell \ll \lambda$, high noise) are heavily damped toward zero! The **Effective Degrees of Freedom** of the Ridge fit is the trace of the Ridge hat matrix $\mathbf{H}_\lambda = \mathbf{X}(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p)^{-1}\mathbf{X}^\top$:

$$\operatorname{df}(\lambda) = \operatorname{tr}(\mathbf{H}_\lambda) = \sum_{\ell=1}^p \frac{\lambda_\ell}{\lambda_\ell + \lambda} \in (0, p]$$

Now let us compute the exact **Bias Vector** and **Covariance Matrix** of $\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) = \mathbf{W}_\lambda \hat{\boldsymbol{\beta}}_{\text{OLS}}$:
1. **Expectation and Bias**:

$$\mathbb{E}\left[\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda)\right] = \mathbf{W}_\lambda \boldsymbol{\beta} = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p)^{-1}(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p - \lambda \mathbf{I}_p)\boldsymbol{\beta} = \boldsymbol{\beta} - \lambda(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p)^{-1}\boldsymbol{\beta}$$

$$\operatorname{Bias}\left(\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda)\right) = -\lambda \left(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p\right)^{-1} \boldsymbol{\beta}$$

2. **Variance-Covariance Matrix**:

$$\operatorname{Var}\left(\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda)\right) = \mathbf{W}_\lambda \operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}}) \mathbf{W}_\lambda^\top = \sigma^2 \left(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p\right)^{-1} (\mathbf{X}^\top \mathbf{X}) \left(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I}_p\right)^{-1}$$

3. **Total Mean Squared Error Decomposition**: Transforming to canonical coordinates $\boldsymbol{\alpha} = \mathbf{V}^\top \boldsymbol{\beta}$ (where $\|\boldsymbol{\alpha}\|_2^2 = \|\boldsymbol{\beta}\|_2^2$), the total scalar MSE is the sum of the trace of the covariance matrix and the squared Euclidean norm of the bias vector:

$$\operatorname{MSE}(\lambda) = \mathbb{E}\left[\|\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) - \boldsymbol{\beta}\|_2^2\right] = \underbrace{\sigma^2 \sum_{\ell=1}^p \frac{\lambda_\ell}{(\lambda_\ell + \lambda)^2}}_{\text{Total Variance } V(\lambda)} + \underbrace{\lambda^2 \sum_{\ell=1}^p \frac{\alpha_\ell^2}{(\lambda_\ell + \lambda)^2}}_{\text{Squared Bias } B^2(\lambda)}$$

### Theorem and Proof: The Hoerl–Kennard Existence Theorem

> [!IMPORTANT]
> **Theorem (Hoerl and Kennard, 1970)**: For any full-rank linear regression model with $\sigma^2 > 0$ and bounded true parameter vector $\|\boldsymbol{\beta}\|_2 < \infty$, there always exists a strictly positive regularization parameter $\lambda^* > 0$ such that for all $\lambda \in \left(0, \, \frac{2\sigma^2}{\max_\ell \alpha_\ell^2}\right)$ (and specifically for all $\lambda \in \left(0, \, \frac{\sigma^2}{\max_\ell \alpha_\ell^2}\right)$ in the matrix Loewner ordering), the Ridge estimator achieves a **strictly smaller total Mean Squared Error than the OLS estimator**:
> $$\operatorname{MSE}\left(\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda)\right) < \operatorname{MSE}\left(\hat{\boldsymbol{\beta}}_{\text{OLS}}\right)$$

**Proof**: Differentiate the variance term $V(\lambda)$ and the squared bias term $B^2(\lambda)$ with respect to $\lambda$ for $\lambda \ge 0$:

$$V'(\lambda) = \frac{d}{d\lambda}\left[ \sigma^2 \sum_{\ell=1}^p \lambda_\ell (\lambda_\ell + \lambda)^{-2} \right] = -2\sigma^2 \sum_{\ell=1}^p \frac{\lambda_\ell}{(\lambda_\ell + \lambda)^3}$$

$$\left[B^2(\lambda)\right]' = \frac{d}{d\lambda}\left[ \sum_{\ell=1}^p \alpha_\ell^2 \lambda^2 (\lambda_\ell + \lambda)^{-2} \right] = 2\lambda \sum_{\ell=1}^p \frac{\alpha_\ell^2 \lambda_\ell}{(\lambda_\ell + \lambda)^3}$$

Now evaluate both derivatives at the OLS boundary $\lambda = 0^+$:

$$V'(0^+) = -2\sigma^2 \sum_{\ell=1}^p \frac{1}{\lambda_\ell^2} < 0, \qquad \left[B^2\right]'(0^+) = 0$$

Adding the two derivatives yields the initial slope of $\operatorname{MSE}(\lambda)$ at $\lambda = 0^+$:

$$\left.\frac{d\,\operatorname{MSE}(\lambda)}{d\lambda}\right|_{\lambda = 0^+} = V'(0^+) + \left[B^2\right]'(0^+) = -2\sigma^2 \sum_{\ell=1}^p \frac{1}{\lambda_\ell^2} < 0$$

Why does this happen? At $\lambda = 0$, the squared bias $B^2(\lambda) = O(\lambda^2)$ has a **zero first derivative** (horizontal tangent), whereas the variance $V(\lambda)$ drops with a **strictly negative linear slope** proportional to $\sum \lambda_\ell^{-2}$! Consequently, moving $\lambda$ slightly above zero trades a second-order $O(\lambda^2)$ increase in squared bias for a first-order $O(\lambda)$ reduction in variance. More specifically, $\operatorname{MSE}'(\lambda) = 2\sum_{\ell=1}^p \frac{\lambda_\ell (\lambda \alpha_\ell^2 - \sigma^2)}{(\lambda_\ell + \lambda)^3} < 0$ is guaranteed for every $\lambda \in \left(0, \, \frac{\sigma^2}{\max_{1 \le \ell \le p} \alpha_\ell^2}\right)$. $\blacksquare$

In empirical practice, visual selection of $\lambda$ is aided by the **Ridge Trace Plot**, which graphs the $p$ coordinates of $\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda)$ against $\lambda \ge 0$: as $\lambda$ increases from $0$, wild oscillations and sign reversals among collinear coefficients rapidly stabilize at a modest value of $\lambda$.

---

## 6.5 Tibshirani's LASSO ($\ell_1$ Penalty), Subgradient KKT Optimality, Soft-Thresholding, and Zou–Hastie Elastic Net

Although Ridge Regression dramatically improves estimation accuracy under multicollinearity, the smooth quadratic penalty $\|\boldsymbol{\beta}\|_2^2 = \sum_{j=1}^p \beta_j^2$ shrinks coefficients asymptotically toward zero without ever setting any coefficient **exactly equal to zero** for finite $\lambda > 0$. Consequently, Ridge retains all $p$ variables in the model and does not perform automatic subset selection.

### Formulation of the LASSO and Subgradient KKT Optimality

To achieve simultaneous continuous shrinkage and exact variable selection (sparsity), Robert Tibshirani (1996) introduced the **Least Absolute Shrinkage and Selection Operator (LASSO)**, which replaces the $\ell_2$ penalty with the $\ell_1$ norm $\|\boldsymbol{\beta}\|_1 = \sum_{j=1}^p |\beta_j|$:

$$\hat{\boldsymbol{\beta}}_{\text{LASSO}}(\lambda) = \arg\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \left\{ \frac{1}{2}\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda \sum_{j=1}^p |\beta_j| \right\}$$

Equivalently, LASSO minimizes $\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2$ subject to the $\ell_1$ diamond/polytope constraint $\sum_{j=1}^p |\beta_j| \le t$. From a Bayesian standpoint, the $\ell_1$ penalty corresponds to an independent **Laplace (Double Exponential) prior** $p(\beta_j) = \frac{\lambda}{2\sigma^2}\exp\left(-\frac{\lambda}{\sigma^2}|\beta_j|\right)$, whose sharp cusp at the origin concentrates posterior mode mass directly on sparse coordinate axes.

Geometrically, why does LASSO produce exact zeros while Ridge does not? The residual sum of squares $\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2$ has elliptical level contours centered at the unconstrained OLS estimate $\hat{\boldsymbol{\beta}}_{\text{OLS}}$.
- In **Ridge Regression**, the feasible region $\|\boldsymbol{\beta}\|_2^2 \le t$ is a smooth hypersphere with no corners; the expanding RSS ellipses almost surely touch the sphere at an interior point where all coordinates $\hat{\beta}_j \neq 0$.
- In **LASSO**, the feasible region $\|\boldsymbol{\beta}\|_1 \le t$ is a cross-polytope (a diamond in $\mathbb{R}^2$, an octahedron in $\mathbb{R}^3$) with sharp **vertices and edges lying directly on the coordinate axes** where one or more $\beta_j = 0$. Expanding elliptical contours frequently intersect a corner of the diamond first, setting the corresponding coordinate(s) identically to zero!

### Closed-Form Derivation of the Soft-Thresholding Operator via Subgradient Calculus

Because the absolute value function $|\beta_j|$ is non-differentiable at $\beta_j = 0$, standard derivative calculus is replaced by convex **subdifferential calculus**. The subdifferential $\partial |\beta_j|$ of $|\beta_j|$ is the set-valued mapping:

$$\partial |\beta_j| = \begin{cases} \{+1\} & \text{if } \beta_j > 0 \\ \{-1\} & \text{if } \beta_j < 0 \\ [-1, +1] & \text{if } \beta_j = 0 \end{cases}$$

By the Karush–Kuhn–Tucker (KKT) optimality conditions for convex programs, $\hat{\boldsymbol{\beta}}$ minimizes $\frac{1}{2}\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda \|\boldsymbol{\beta}\|_1$ if and only if $\mathbf{0} \in -\mathbf{X}^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) + \lambda \partial \|\hat{\boldsymbol{\beta}}\|_1$, which states coordinate-wise for each $j = 1, \dots, p$:

$$\mathbf{x}_j^\top (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) = \lambda s_j, \qquad \text{where } s_j = \operatorname{sgn}(\hat{\beta}_j) \text{ if } \hat{\beta}_j \neq 0, \text{ and } s_j \in [-1, +1] \text{ if } \hat{\beta}_j = 0$$

Suppose the columns of $\mathbf{X}$ are orthonormal ($\mathbf{X}^\top \mathbf{X} = \mathbf{I}_p$), so that the unconstrained OLS estimate is $\hat{\beta}_{j,\text{OLS}} = \mathbf{x}_j^\top \mathbf{Y}$. Then $\mathbf{x}_j^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) = \hat{\beta}_{j,\text{OLS}} - \hat{\beta}_j$, and the KKT stationarity condition becomes:

$$\hat{\beta}_{j,\text{OLS}} - \hat{\beta}_j = \lambda s_j \quad \Longleftrightarrow \quad \hat{\beta}_j = \hat{\beta}_{j,\text{OLS}} - \lambda s_j$$

We analyze the three exhaustive cases:
1. **Case 1 ($\hat{\beta}_j > 0 \implies s_j = +1$)**: Then $\hat{\beta}_j = \hat{\beta}_{j,\text{OLS}} - \lambda > 0$, which holds if and only if $\hat{\beta}_{j,\text{OLS}} > \lambda$.
2. **Case 2 ($\hat{\beta}_j < 0 \implies s_j = -1$)**: Then $\hat{\beta}_j = \hat{\beta}_{j,\text{OLS}} + \lambda < 0$, which holds if and only if $\hat{\beta}_{j,\text{OLS}} < -\lambda$.
3. **Case 3 ($\hat{\beta}_j = 0 \implies s_j \in [-1, +1]$)**: Then $\hat{\beta}_{j,\text{OLS}} = \lambda s_j \in [-\lambda, +\lambda]$, which holds if and only if $|\hat{\beta}_{j,\text{OLS}}| \le \lambda$.

Combining all three cases yields Donoho and Johnstone's **Soft-Thresholding Operator $S_\lambda(\cdot)$**:

$$\hat{\beta}_{j,\text{LASSO}}(\lambda) = S_\lambda\left(\hat{\beta}_{j,\text{OLS}}\right) = \operatorname{sgn}\left(\hat{\beta}_{j,\text{OLS}}\right) \max\left( \left|\hat{\beta}_{j,\text{OLS}}\right| - \lambda, \; 0 \right) = \begin{cases} \hat{\beta}_{j,\text{OLS}} - \lambda & \text{if } \hat{\beta}_{j,\text{OLS}} > \lambda \\ 0 & \text{if } |\hat{\beta}_{j,\text{OLS}}| \le \lambda \\ \hat{\beta}_{j,\text{OLS}} + \lambda & \text{if } \hat{\beta}_{j,\text{OLS}} < -\lambda \end{cases}$$

For general non-orthogonal designs $\mathbf{X}$, **Cyclic Coordinate Descent** (Friedman, Hastie, and Tibshirani, 2010) updates each coordinate $\hat{\beta}_j$ iteratively by computing the partial residual $\mathbf{r}^{(-j)} = \mathbf{Y} - \sum_{\ell \neq j} \mathbf{x}_\ell \hat{\beta}_\ell$ and applying soft-thresholding: $\hat{\beta}_j \leftarrow \frac{1}{\mathbf{x}_j^\top \mathbf{x}_j} S_\lambda\left(\mathbf{x}_j^\top \mathbf{r}^{(-j)}\right)$. Furthermore, Bradley Efron, Trevor Hastie, Iain Johnstone, and Robert Tibshirani (2004) proved that the entire continuous LASSO regularization path $\{\hat{\boldsymbol{\beta}}_{\text{LASSO}}(\lambda) : \lambda \ge 0\}$ is **piecewise linear** as a function of $\lambda$! Their **Least Angle Regression (LARS)** algorithm computes the exact entire LASSO solution path with the same order of computational complexity as a single Ordinary Least Squares fit ($O(np^2)$ operations) by moving along equiangular directions that maintain equal absolute correlation with all currently active predictors until a new variable enters the active set or an existing coefficient crosses zero.

Despite its remarkable geometric elegance, standard LASSO applies the exact same penalty rate $\lambda$ to every coefficient, which introduces a constant shrinkage bias $\pm \lambda$ even for large, genuinely non-zero true parameters $\beta_j$. Moreover, Zhao and Yu (2006) demonstrated that standard LASSO achieves consistent model selection (recovering the exact true support $S_0 = \{j : \beta_j \neq 0\}$ with probability approaching one) if and only if the design matrix satisfies the stringent **Irrepresentable Condition**, which bounds the regression coefficients of irrelevant predictors on relevant predictors strictly below unity in $\ell_1$ norm—a condition frequently violated under strong multicollinearity. To overcome this limitation and eliminate the constant bias on large coefficients, Hui Zou (2006) introduced the **Adaptive LASSO**, which assigns data-dependent inverse weights $w_j = 1 / |\hat{\beta}_{j,\text{init}}|^\gamma$ ($\gamma > 0$, where $\hat{\boldsymbol{\beta}}_{\text{init}}$ is a root-$n$ consistent initial estimator such as OLS or Ridge) to the $\ell_1$ penalty $\lambda \sum_{j=1}^p w_j |\beta_j|$. Adaptive LASSO enjoys the celebrated **Oracle Property**: asymptotically, it selects the exact true subset of non-zero variables with probability tending to one while estimating their non-zero coefficients with the exact same asymptotic normal covariance matrix as if the true sparse model had been known in advance.

### Zou and Hastie's Elastic Net (2005)

While LASSO excels at sparse selection, it exhibits three limitations under severe multicollinearity: (a) when $p > n$, LASSO can select at most $n$ variables before saturating; (b) if a group of predictors exhibits very high pairwise correlation, LASSO tends to arbitrarily select one variable from the group and drop the others; and (c) when $n > p$ and correlations are high, Ridge empirically outperforms LASSO in prediction accuracy.

Hui Zou and Trevor Hastie (2005) resolved these issues via the **Elastic Net**, which combines the $\ell_1$ LASSO penalty and the $\ell_2$ Ridge penalty:

$$\hat{\boldsymbol{\beta}}_{\text{EN}}(\lambda_1, \lambda_2) = \arg\min_{\boldsymbol{\beta} \in \mathbb{R}^p} \left\{ \frac{1}{2}\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda_1 \|\boldsymbol{\beta}\|_1 + \frac{\lambda_2}{2} \|\boldsymbol{\beta}\|_2^2 \right\}$$

Often parameterized with $\lambda > 0$ and mixing parameter $\alpha \in [0, 1]$ as $\lambda\left[\alpha \|\boldsymbol{\beta}\|_1 + \frac{1-\alpha}{2}\|\boldsymbol{\beta}\|_2^2\right]$, the strictly convex $\ell_2$ term $(\lambda_2/2)\|\boldsymbol{\beta}\|_2^2$ induces a **grouping effect**: any two standardized predictors with sample correlation $r_{j\ell} \to 1$ are guaranteed to receive nearly identical estimated coefficients, bounded explicitly by the inequality $|\hat{\beta}_j - \hat{\beta}_\ell| \le \frac{\|\mathbf{Y}\|_2}{\lambda_2}\sqrt{2(1 - r_{j\ell})}$, while the sharp corners of the $\ell_1$ term $\lambda_1 \|\boldsymbol{\beta}\|_1$ preserve exact sparsity. Under orthonormal columns ($\mathbf{X}^\top \mathbf{X} = \mathbf{I}_p$), the Elastic Net solution combines soft-thresholding with Ridge scaling:

$$\hat{\beta}_{j,\text{EN}}(\lambda_1, \lambda_2) = \frac{S_{\lambda_1}\left(\hat{\beta}_{j,\text{OLS}}\right)}{1 + \lambda_2} = \frac{\operatorname{sgn}(\hat{\beta}_{j,\text{OLS}})\max\left(|\hat{\beta}_{j,\text{OLS}}| - \lambda_1, \, 0\right)}{1 + \lambda_2}$$

---

## 6.6 Dimension Reduction and Regularization Tuning: Principal Component Regression (PCR), Partial Least Squares (PLS), and Generalized Cross-Validation (GCV)

An alternative to continuous penalty shrinkage is **discrete spectral dimension reduction**, which projects the $p$ correlated predictors onto an $m$-dimensional orthogonal subspace ($m < p$) before applying OLS.

### 1. Principal Component Regression (PCR)

Using the Singular Value Decomposition $\mathbf{X} = \mathbf{U}\mathbf{D}\mathbf{V}^\top$ of the centered and standardized design matrix (so $\mathbf{X}^\top \mathbf{X} = \mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^\top$ with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p$), define the $n \times p$ matrix of **Principal Component Scores**:

$$\mathbf{Z} = \mathbf{X}\mathbf{V} = [\mathbf{z}_1, \mathbf{z}_2, \dots, \mathbf{z}_p], \qquad \text{where } \mathbf{z}_\ell = \mathbf{X}\mathbf{v}_\ell = \mu_\ell \mathbf{u}_\ell$$

Notice that the principal components $\mathbf{z}_1, \dots, \mathbf{z}_p$ are **mutually orthogonal**, with sums of squares equal to the eigenvalues of $\mathbf{X}^\top \mathbf{X}$:

$$\mathbf{Z}^\top \mathbf{Z} = \mathbf{V}^\top (\mathbf{X}^\top \mathbf{X}) \mathbf{V} = \boldsymbol{\Lambda} = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_p)$$

Rewriting the linear model in terms of the orthogonal scores gives $\mathbf{Y} = \mathbf{X}\mathbf{V}\mathbf{V}^\top \boldsymbol{\beta} + \boldsymbol{\varepsilon} = \mathbf{Z}\boldsymbol{\alpha} + \boldsymbol{\varepsilon}$, where $\boldsymbol{\alpha} = \mathbf{V}^\top \boldsymbol{\beta}$. Because $\mathbf{Z}^\top \mathbf{Z}$ is diagonal, the OLS estimator of the $\ell$-th canonical parameter $\alpha_\ell$ is simply $\hat{\alpha}_\ell = \frac{\mathbf{z}_\ell^\top \mathbf{Y}}{\mathbf{z}_\ell^\top \mathbf{z}_\ell} = \frac{\mathbf{v}_\ell^\top \mathbf{X}^\top \mathbf{Y}}{\lambda_\ell}$ with variance $\operatorname{Var}(\hat{\alpha}_\ell) = \frac{\sigma^2}{\lambda_\ell}$.

In **Principal Component Regression (PCR)**, we retain only the first $m < p$ principal components $\mathbf{Z}_m = [\mathbf{z}_1, \dots, \mathbf{z}_m]$ corresponding to the $m$ largest eigenvalues $\lambda_1 \ge \dots \ge \lambda_m$, and hard-threshold the remaining $p - m$ high-variance, low-eigenvalue components to zero ($\hat{\alpha}_{m+1} = \dots = \hat{\alpha}_p = 0$). Transforming back to the original coordinate basis via $\mathbf{V}_m = [\mathbf{v}_1, \dots, \mathbf{v}_m]$ yields the **PCR Estimator**:

$$\hat{\boldsymbol{\beta}}_{\text{PCR}}(m) = \mathbf{V}_m \hat{\boldsymbol{\alpha}}_m = \sum_{\ell=1}^m \left(\frac{\mathbf{u}_\ell^\top \mathbf{Y}}{\mu_\ell}\right) \mathbf{v}_\ell = \sum_{\ell=1}^m \frac{1}{\lambda_\ell} \mathbf{v}_\ell \mathbf{v}_\ell^\top \mathbf{X}^\top \mathbf{Y}$$

with covariance matrix $\operatorname{Var}\left(\hat{\boldsymbol{\beta}}_{\text{PCR}}(m)\right) = \sigma^2 \sum_{\ell=1}^m \frac{1}{\lambda_\ell} \mathbf{v}_\ell \mathbf{v}_\ell^\top$ and bias $\operatorname{Bias}\left(\hat{\boldsymbol{\beta}}_{\text{PCR}}(m)\right) = -\sum_{\ell=m+1}^p \alpha_\ell \mathbf{v}_\ell$. While Ridge applies smooth weights $\frac{\lambda_\ell}{\lambda_\ell + \lambda} \in (0, 1)$, PCR applies a discrete step-function filter ($1$ for $\ell \le m$, $0$ for $\ell > m$). Because orthogonal vectors $\mathbf{v}_\ell$ preserve Euclidean norms, the total Mean Squared Error of the $m$-component PCR estimator decomposes cleanly into retained variance plus omitted signal squared:

$$\operatorname{MSE}\left(\hat{\boldsymbol{\beta}}_{\text{PCR}}(m)\right) = \sigma^2 \sum_{\ell=1}^m \frac{1}{\lambda_\ell} + \sum_{\ell=m+1}^p \alpha_\ell^2$$

Consequently, discarding the $\ell$-th principal component strictly reduces total Mean Squared Error whenever its omitted signal squared $\alpha_\ell^2$ is smaller than its estimation noise variance $\sigma^2 / \lambda_\ell$.

### 2. Partial Least Squares (PLS) Regression

A potential vulnerability of PCR is that the principal directions $\mathbf{v}_1, \dots, \mathbf{v}_m$ are chosen in an **unsupervised** manner solely to maximize predictor variance $\operatorname{Var}(\mathbf{X}\mathbf{v}_\ell) = \lambda_\ell$, without consulting the response $\mathbf{Y}$. As pointed out by Ian Jolliffe (1982), there is no theoretical guarantee that the high-variance directions of $\mathbf{X}$ are the directions most strongly correlated with $\mathbf{Y}$; occasionally, a low-eigenvalue principal component carries substantial predictive power for $\mathbf{Y}$.

Herman Wold (1966) developed **Partial Least Squares (PLS)** to construct orthogonal latent components $\mathbf{t}_1, \dots, \mathbf{t}_m$ in a **supervised** manner that balances large predictor variance with high predictor-response correlation. Specifically, at step $\ell$, PLS seeks a unit weight vector $\mathbf{w}_\ell$ maximizing the squared sample covariance between the linear combination $\mathbf{X}^{(\ell-1)}\mathbf{w}_\ell$ and $\mathbf{Y}$, where $\operatorname{Cov}^2(\mathbf{X}\mathbf{w}, \mathbf{Y}) = \operatorname{Var}(\mathbf{X}\mathbf{w}) \cdot \operatorname{Var}(\mathbf{Y}) \cdot \operatorname{Corr}^2(\mathbf{X}\mathbf{w}, \mathbf{Y})$:
- For the first PLS direction $\mathbf{w}_1$, solve:

$$\mathbf{w}_1 = \arg\max_{\|\mathbf{w}\|_2 = 1} \operatorname{Cov}^2(\mathbf{X}\mathbf{w}, \mathbf{Y}) \quad \Longrightarrow \quad \mathbf{w}_1 = \frac{\mathbf{X}^\top \mathbf{Y}}{\|\mathbf{X}^\top \mathbf{Y}\|_2}$$

- Compute the first score vector $\mathbf{t}_1 = \mathbf{X}\mathbf{w}_1$, regress $\mathbf{Y}$ on $\mathbf{t}_1$ to obtain coefficient $\hat{\theta}_1 = \frac{\mathbf{t}_1^\top \mathbf{Y}}{\mathbf{t}_1^\top \mathbf{t}_1}$, orthogonalize (deflate) each column of $\mathbf{X}$ with respect to $\mathbf{t}_1$ via $\mathbf{X}^{(1)} = \mathbf{X} - \mathbf{t}_1 (\mathbf{t}_1^\top \mathbf{t}_1)^{-1}\mathbf{t}_1^\top \mathbf{X}$, and iterate to extract $m$ mutually orthogonal supervised components spanning the $m$-dimensional **Krylov subspace** $\mathcal{K}_m(\mathbf{X}^\top \mathbf{X}, \mathbf{X}^\top \mathbf{Y}) = \operatorname{span}\left\{\mathbf{X}^\top \mathbf{Y}, \, (\mathbf{X}^\top \mathbf{X})\mathbf{X}^\top \mathbf{Y}, \, \dots, \, (\mathbf{X}^\top \mathbf{X})^{m-1}\mathbf{X}^\top \mathbf{Y}\right\}$. Because PLS explicitly targets $\mathbf{X}^\top \mathbf{Y}$, it typically achieves comparable in-sample fit to PCR using fewer components ($m_{\text{PLS}} \le m_{\text{PCR}}$), though its non-linear dependence on $\mathbf{Y}$ can slightly increase variance relative to PCR.

### 3. Selecting the Regularization Parameter: $K$-Fold CV, Exact LOO Shortcut, and GCV

Because $\text{SSE}$ on the training data is minimized at $\lambda = 0$ (OLS), the regularization parameter $\lambda$ (or $m$) must be tuned using out-of-sample predictive error criteria:
- **$K$-Fold Cross-Validation**: Partition the $n$ observations into $K$ disjoint folds $F_1, \dots, F_K$ (typically $K = 5$ or $10$), fit the regularized model on the remaining $n - |F_k|$ observations for a grid of $\lambda$ values, and minimize $\operatorname{CV}(\lambda) = \frac{1}{n}\sum_{k=1}^K \sum_{i \in F_k} \left(Y_i - \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}^{(-k)}(\lambda)\right)^2$.
- **Exact Leave-One-Out (PRESS) Shortcut for Ridge**: For any linear smoother $\hat{\mathbf{Y}}(\lambda) = \mathbf{H}_\lambda \mathbf{Y}$, the $n$-fold Leave-One-Out cross-validation error can be computed from a **single** fit without refitting the model $n$ times:

$$\operatorname{LOOCV}(\lambda) = \frac{1}{n}\sum_{i=1}^n \left( Y_i - \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}^{(-i)}(\lambda) \right)^2 = \frac{1}{n}\sum_{i=1}^n \left( \frac{Y_i - \hat{Y}_i(\lambda)}{1 - (\mathbf{H}_\lambda)_{ii}} \right)^2$$

- **Golub–Heath–Wahba (1979) Generalized Cross-Validation (GCV)**: Replaces the individual leverage diagonals $(\mathbf{H}_\lambda)_{ii}$ with their rotation-invariant average $\frac{1}{n}\operatorname{tr}(\mathbf{H}_\lambda) = \frac{1}{n}\operatorname{df}(\lambda)$:

$$\operatorname{GCV}(\lambda) = \frac{\frac{1}{n}\left\|\mathbf{Y} - \mathbf{H}_\lambda \mathbf{Y}\right\|_2^2}{\left(1 - \frac{1}{n}\operatorname{tr}(\mathbf{H}_\lambda)\right)^2} = \frac{n \cdot \text{SSE}(\lambda)}{\left(n - \sum_{\ell=1}^p \frac{\lambda_\ell}{\lambda_\ell + \lambda}\right)^2}$$

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Method</th>
<th>Objective / Spectral Filter $f_\ell$</th>
<th>Sparsity (Feature Selection)</th>
<th>Key Strength &amp; Primary Limitation</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ordinary Least Squares (OLS)</strong></td>
<td>$\min \|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2$; $f_\ell = 1$</td>
<td>No ($\hat{\beta}_j \neq 0$ for all $j$)</td>
<td>Unbiased (BLUE), but variance $\sigma^2 \sum \lambda_\ell^{-1}$ explodes when $\lambda_p \to 0$</td>
</tr>
<tr>
<td><strong>Ridge Regression ($\ell_2$)</strong></td>
<td>$\min \|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda\|\boldsymbol{\beta}\|_2^2$; $f_\ell = \frac{\lambda_\ell}{\lambda_\ell + \lambda}$</td>
<td>No (continuous proportional shrinkage)</td>
<td>Closed-form $(\mathbf{X}^\top \mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top \mathbf{Y}$; strictly beats OLS MSE for small $\lambda > 0$</td>
</tr>
<tr>
<td><strong>LASSO ($\ell_1$)</strong></td>
<td>$\min \frac{1}{2}\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda\|\boldsymbol{\beta}\|_1$</td>
<td>Yes (sets weak predictors exactly to $0$)</td>
<td>Produces interpretable sparse models; struggles with tightly grouped collinear sets</td>
</tr>
<tr>
<td><strong>Elastic Net ($\ell_1 + \ell_2$)</strong></td>
<td>$\min \frac{1}{2}\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda_1\|\boldsymbol{\beta}\|_1 + \frac{\lambda_2}{2}\|\boldsymbol{\beta}\|_2^2$</td>
<td>Yes (sparse + grouped selection)</td>
<td>Handles $p > n$ and groups correlated predictors together; requires tuning $(\lambda_1, \lambda_2)$</td>
</tr>
<tr>
<td><strong>Principal Component Regression (PCR)</strong></td>
<td>Retains top $m$ eigenvectors of $\mathbf{X}^\top \mathbf{X}$; $f_\ell = \mathbf{1}_{\{\ell \le m\}}$</td>
<td>No (uses all $p$ original variables in $\mathbf{v}_\ell$)</td>
<td>Eliminates tiny-eigenvalue variance completely; unsupervised choice of $\mathbf{v}_\ell$</td>
</tr>
</tbody>
</table></div>

---

## Worked Questions and Solutions

### Question 1: Variance Inflation Factors, Spectral Condition Number, and Belsley–Kuh–Welsch Proportions

Consider a multiple regression model with $k = 3$ standardized predictors $(X_1, X_2, X_3)$ and standardized response $Y$ across $n = 104$ observations, yielding the sample correlation matrix $\mathbf{R}_{XX} = \mathbf{X}^\top \mathbf{X}$ and predictor-response vector $\mathbf{r}_{XY} = \mathbf{X}^\top \mathbf{Y}$:

$$\mathbf{R}_{XX} = \begin{pmatrix} 1.00 & 0.90 & 0.00 \\ 0.90 & 1.00 & 0.00 \\ 0.00 & 0.00 & 1.00 \end{pmatrix}, \qquad \mathbf{r}_{XY} = \begin{pmatrix} 0.57 \\ 0.57 \\ 0.40 \end{pmatrix}$$

1. Compute the determinant $\det(\mathbf{R}_{XX})$, the exact inverse matrix $\mathbf{R}_{XX}^{-1}$, the Variance Inflation Factors ($\text{VIF}_1, \text{VIF}_2, \text{VIF}_3$), the tolerances ($\text{TOL}_j$), and the OLS parameter vector $\hat{\boldsymbol{\beta}}_{\text{OLS}} = \mathbf{R}_{XX}^{-1}\mathbf{r}_{XY}$.
2. Find all eigenvalues $\lambda_1 \ge \lambda_2 \ge \lambda_3$ and orthonormal eigenvectors $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ of $\mathbf{R}_{XX}$, and compute the singular values $\mu_\ell$, the condition indices $\eta_1, \eta_2, \eta_3$, and the spectral condition number $\kappa(\mathbf{X})$.
3. Construct the complete $3 \times 3$ Belsley–Kuh–Welsch table of Variance Decomposition Proportions $\pi_{\ell j}$ and interpret which predictors are involved in the collinear dependency.

### Solution, step 1: Inverse Correlation Matrix, VIFs, Tolerances, and OLS Estimates

Because $\mathbf{R}_{XX}$ is block-diagonal with a $2 \times 2$ upper-left block $\mathbf{A} = \begin{pmatrix} 1.00 & 0.90 \\ 0.90 & 1.00 \end{pmatrix}$ and a $1 \times 1$ lower-right block $(1.00)$, its determinant is:

$$\det(\mathbf{R}_{XX}) = \det(\mathbf{A}) \times 1.00 = (1.00)(1.00) - (0.90)^2 = 1.00 - 0.81 = 0.1900$$

Inverting the upper-left $2 \times 2$ block via $\mathbf{A}^{-1} = \frac{1}{0.19}\begin{pmatrix} 1.00 & -0.90 \\ -0.90 & 1.00 \end{pmatrix}$ gives the exact inverse correlation matrix:

$$\mathbf{R}_{XX}^{-1} = \begin{pmatrix} 1/0.19 & -0.90/0.19 & 0 \\ -0.90/0.19 & 1/0.19 & 0 \\ 0 & 0 & 1 \end{pmatrix} \approx \begin{pmatrix} 5.2632 & -4.7368 & 0.0000 \\ -4.7368 & 5.2632 & 0.0000 \\ 0.0000 & 0.0000 & 1.0000 \end{pmatrix}$$

Reading the diagonal elements of $\mathbf{R}_{XX}^{-1}$ yields the Variance Inflation Factors and Tolerances:
- Predictor $X_1$: $\text{VIF}_1 = \left(\mathbf{R}_{XX}^{-1}\right)_{11} = \frac{1}{1 - 0.90^2} = \frac{1}{0.19} \approx 5.2632$, $\text{TOL}_1 = 1 - R_1^2 = 0.1900$.
- Predictor $X_2$: $\text{VIF}_2 = \left(\mathbf{R}_{XX}^{-1}\right)_{22} = \frac{1}{1 - 0.90^2} = \frac{1}{0.19} \approx 5.2632$, $\text{TOL}_2 = 1 - R_2^2 = 0.1900$.
- Predictor $X_3$: $\text{VIF}_3 = \left(\mathbf{R}_{XX}^{-1}\right)_{33} = \frac{1}{1 - 0.00^2} = 1.0000$, $\text{TOL}_3 = 1.0000$.

Notice also the large negative off-diagonal covariance entry $\left(\mathbf{R}_{XX}^{-1}\right)_{12} = -4.7368$, which implies that the sampling correlation between $\hat{\beta}_1$ and $\hat{\beta}_2$ is $\operatorname{Corr}(\hat{\beta}_1, \hat{\beta}_2) = \frac{-4.7368}{5.2632} = -0.9000$. Now compute $\hat{\boldsymbol{\beta}}_{\text{OLS}} = \mathbf{R}_{XX}^{-1}\mathbf{r}_{XY}$:

$$\hat{\boldsymbol{\beta}}_{\text{OLS}} = \begin{pmatrix} \frac{1.00(0.57) - 0.90(0.57)}{0.19} \\ \frac{-0.90(0.57) + 1.00(0.57)}{0.19} \\ 1.00(0.40) \end{pmatrix} = \begin{pmatrix} \frac{0.10 \times 0.57}{0.19} \\ \frac{0.10 \times 0.57}{0.19} \\ 0.40 \end{pmatrix} = \begin{pmatrix} 0.3000 \\ 0.3000 \\ 0.4000 \end{pmatrix}$$

### Solution, step 2: Eigenvalues, Orthonormal Eigenvectors, Singular Values, and Condition Indices

For the symmetric $2 \times 2$ block $\begin{pmatrix} 1 & r \\ r & 1 \end{pmatrix}$ with $r = 0.90$, the eigenvalues are $1 + r = 1.90$ and $1 - r = 0.10$, while the $(3, 3)$ block contributes eigenvalue $1.00$. Ordering the eigenvalues in descending sequence $\lambda_1 \ge \lambda_2 \ge \lambda_3$ gives:
- $\lambda_1 = 1 + 0.90 = 1.9000$, with orthonormal eigenvector $\mathbf{v}_1 = \left(\frac{1}{\sqrt{2}}, \, \frac{1}{\sqrt{2}}, \, 0\right)^\top \approx (0.7071, 0.7071, 0)^\top$.
- $\lambda_2 = 1.0000$, with orthonormal eigenvector $\mathbf{v}_2 = (0, \, 0, \, 1)^\top$.
- $\lambda_3 = 1 - 0.90 = 0.1000$, with orthonormal eigenvector $\mathbf{v}_3 = \left(\frac{1}{\sqrt{2}}, \, -\frac{1}{\sqrt{2}}, \, 0\right)^\top \approx (0.7071, -0.7071, 0)^\top$.

(Verify that $\lambda_1 \lambda_2 \lambda_3 = (1.90)(1.00)(0.10) = 0.1900 = \det(\mathbf{R}_{XX})$ and $\lambda_1 + \lambda_2 + \lambda_3 = 3.00 = \operatorname{tr}(\mathbf{R}_{XX})$). Taking square roots yields the singular values $\mu_\ell = \sqrt{\lambda_\ell}$ and condition indices $\eta_\ell = \mu_1 / \mu_\ell = \sqrt{\lambda_1 / \lambda_\ell}$:
- Component $\ell = 1$: $\mu_1 = \sqrt{1.90} \approx 1.3784$, $\eta_1 = 1.0000$.
- Component $\ell = 2$: $\mu_2 = \sqrt{1.00} = 1.0000$, $\eta_2 = \sqrt{1.90 / 1.00} \approx 1.3784$.
- Component $\ell = 3$: $\mu_3 = \sqrt{0.10} \approx 0.3162$, $\eta_3 = \kappa(\mathbf{X}) = \sqrt{1.90 / 0.10} = \sqrt{19} \approx 4.3589$.

### Solution, step 3: Belsley–Kuh–Welsch Variance Decomposition Proportions ($\pi_{\ell j}$)

We compute $\phi_{j\ell} = \frac{v_{j\ell}^2}{\lambda_\ell}$ for each predictor $j \in \{1, 2, 3\}$ and each principal component $\ell \in \{1, 2, 3\}$:
- **For $j = 1$ ($X_1$)**: $v_{11}^2 = 0.50$, $v_{12}^2 = 0$, $v_{13}^2 = 0.50$. Thus:
  - $\phi_{11} = \frac{0.50}{1.90} = 0.2632$, $\phi_{12} = \frac{0}{1.00} = 0$, $\phi_{13} = \frac{0.50}{0.10} = 5.0000$.
  - Sum $\phi_1 = 0.2632 + 0 + 5.0000 = 5.2632 = \text{VIF}_1$.
  - Proportions: $\pi_{11} = \frac{0.2632}{5.2632} = 0.0500$ ($5.0\%$), $\pi_{21} = 0.0000$ ($0.0\%$), $\pi_{31} = \frac{5.0000}{5.2632} = 0.9500$ ($95.0\%$).
- **For $j = 2$ ($X_2$)**: By symmetry ($v_{21}^2 = 0.50$, $v_{22}^2 = 0$, $v_{23}^2 = 0.50$), we obtain identical proportions:
  - $\pi_{12} = 0.0500$ ($5.0\%$), $\pi_{22} = 0.0000$ ($0.0\%$), $\pi_{32} = 0.9500$ ($95.0\%$).
- **For $j = 3$ ($X_3$)**: $v_{31}^2 = 0$, $v_{32}^2 = 1.00$, $v_{33}^2 = 0$. Thus:
  - $\phi_{31} = 0$, $\phi_{32} = \frac{1.00}{1.00} = 1.0000$, $\phi_{33} = 0$, $\phi_3 = 1.0000 = \text{VIF}_3$.
  - Proportions: $\pi_{13} = 0.0000$, $\pi_{23} = 1.0000$ ($100.0\%$), $\pi_{33} = 0.0000$.

The complete Belsley–Kuh–Welsch diagnostic table is:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Component $\ell$</th>
<th>Eigenvalue $\lambda_\ell$</th>
<th>Singular Value $\mu_\ell$</th>
<th>Condition Index $\eta_\ell$</th>
<th>$\pi_{\ell 1}$ ($X_1$)</th>
<th>$\pi_{\ell 2}$ ($X_2$)</th>
<th>$\pi_{\ell 3}$ ($X_3$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$1$</td>
<td>$1.9000$</td>
<td>$1.3784$</td>
<td>$1.0000$</td>
<td>$0.0500$</td>
<td>$0.0500$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td>$2$</td>
<td>$1.0000$</td>
<td>$1.0000$</td>
<td>$1.3784$</td>
<td>$0.0000$</td>
<td>$0.0000$</td>
<td>$1.0000$</td>
</tr>
<tr>
<td>$3$</td>
<td>$0.1000$</td>
<td>$0.3162$</td>
<td>$4.3589$</td>
<td><strong>$0.9500$</strong></td>
<td><strong>$0.9500$</strong></td>
<td>$0.0000$</td>
</tr>
</tbody>
</table></div>

**Diagnostic Interpretation**: Fully $95\%$ of the variance of $\hat{\beta}_1$ ($\pi_{31} = 0.95$) and $95\%$ of the variance of $\hat{\beta}_2$ ($\pi_{32} = 0.95$) are concentrated on the single smallest eigenvalue $\lambda_3 = 0.10$, while $X_3$ is completely orthogonal ($\pi_{33} = 0$).

---

### Question 2: Hoerl–Kennard Ridge Regression MSE Optimization vs. Principal Component Regression

Consider a two-predictor standardized linear model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ where $\mathbf{X}^\top \mathbf{X}$ has already been rotated into canonical principal coordinates $\mathbf{Z} = \mathbf{X}\mathbf{V}$ with eigenvalues $\lambda_1 = 10.0$ and $\lambda_2 = 0.10$. Suppose the true canonical parameter vector is $\boldsymbol{\alpha} = (\alpha_1, \alpha_2)^\top = (2.0, 0.20)^\top$, the error variance is $\sigma^2 = 1.0$, and for a realized sample the canonical projections are $\mathbf{Z}^\top \mathbf{Y} = (21.0, -0.15)^\top$.
1. Compute the unconstrained OLS estimate $\hat{\boldsymbol{\alpha}}_{\text{OLS}}$ and its exact theoretical total Mean Squared Error $\operatorname{MSE}(\hat{\boldsymbol{\alpha}}_{\text{OLS}})$.
2. For Ridge Regression with penalty parameter $\lambda = 0.10$, compute the Ridge estimate $\hat{\boldsymbol{\alpha}}_{\text{ridge}}(0.10)$, the effective degrees of freedom $\operatorname{df}(0.10)$, the exact theoretical variance $V(0.10)$, the squared bias $B^2(0.10)$, and the total $\operatorname{MSE}(0.10)$.
3. Compute the theoretical total $\operatorname{MSE}$ of the $1$-component Principal Component Regression estimator $\hat{\boldsymbol{\alpha}}_{\text{PCR}}(m = 1)$ (which sets $\hat{\alpha}_2 = 0$), and compare $\operatorname{MSE}(\text{OLS})$, $\operatorname{MSE}(\text{Ridge}, \lambda = 0.10)$, and $\operatorname{MSE}(\text{PCR}, m = 1)$.

### Solution, step 1: Unconstrained OLS Estimator and Exact Total MSE

In canonical coordinates where $\mathbf{Z}^\top \mathbf{Z} = \operatorname{diag}(\lambda_1, \lambda_2) = \operatorname{diag}(10.0, 0.10)$ and $\mathbf{Z}^\top \mathbf{Y} = (21.0, -0.15)^\top$, the OLS estimator is:

$$\hat{\boldsymbol{\alpha}}_{\text{OLS}} = (\mathbf{Z}^\top \mathbf{Z})^{-1}\mathbf{Z}^\top \mathbf{Y} = \begin{pmatrix} 21.0 / 10.0 \\ -0.15 / 0.10 \end{pmatrix} = \begin{pmatrix} 2.1000 \\ -1.5000 \end{pmatrix}$$

Notice how severely the tiny second eigenvalue $\lambda_2 = 0.10$ distorts the second coordinate: whereas $\hat{\alpha}_{1,\text{OLS}} = 2.10$ is very close to the true $\alpha_1 = 2.0$, the second coordinate $\hat{\alpha}_{2,\text{OLS}} = -1.50$ has the wrong sign and is far from the true $\alpha_2 = +0.20$! Because OLS is unbiased ($B^2(0) = 0$), its theoretical total Mean Squared Error equals the sum of its canonical variances:

$$\operatorname{MSE}\left(\hat{\boldsymbol{\alpha}}_{\text{OLS}}\right) = \sigma^2 \left( \frac{1}{\lambda_1} + \frac{1}{\lambda_2} \right) = 1.0 \left( \frac{1}{10.0} + \frac{1}{0.10} \right) = 0.1000 + 10.0000 = 10.1000$$

Fully $99.01\%$ of the total estimation error of OLS ($10.00 / 10.10$) arises from the noisy second principal component $\lambda_2 = 0.10$.

### Solution, step 2: Ridge Regression Estimate, Effective Degrees of Freedom, and Exact MSE at $\lambda = 0.10$

For $\lambda = 0.10$, the Ridge shrinkage factors $f_\ell(\lambda) = \frac{\lambda_\ell}{\lambda_\ell + \lambda}$ are:
- Component $\ell = 1$: $f_1(0.10) = \frac{10.0}{10.0 + 0.10} = \frac{10.0}{10.10} \approx 0.9901$
- Component $\ell = 2$: $f_2(0.10) = \frac{0.10}{0.10 + 0.10} = \frac{0.10}{0.20} = 0.5000$

Thus, the effective degrees of freedom of the Ridge fit is $\operatorname{df}(0.10) = f_1(0.10) + f_2(0.10) = 0.9901 + 0.5000 = 1.4901$, and the realized Ridge point estimate is:

$$\hat{\boldsymbol{\alpha}}_{\text{ridge}}(0.10) = \begin{pmatrix} \frac{21.0}{10.0 + 0.10} \\ \frac{-0.15}{0.10 + 0.10} \end{pmatrix} = \begin{pmatrix} 2.0792 \\ -0.7500 \end{pmatrix}$$

Now let us evaluate the exact theoretical variance $V(0.10)$ and squared bias $B^2(0.10)$ under $\sigma^2 = 1.0$ and $\boldsymbol{\alpha} = (2.0, 0.20)^\top$:
1. **Total Variance $V(0.10)$**:

$$V(0.10) = \sigma^2 \left[ \frac{\lambda_1}{(\lambda_1 + \lambda)^2} + \frac{\lambda_2}{(\lambda_2 + \lambda)^2} \right] = 1.0 \left[ \frac{10.0}{(10.10)^2} + \frac{0.10}{(0.20)^2} \right] = \frac{10.0}{102.01} + \frac{0.10}{0.04} = 0.09803 + 2.50000 = 2.59803$$

2. **Squared Bias $B^2(0.10)$**:

$$B^2(0.10) = \lambda^2 \left[ \frac{\alpha_1^2}{(\lambda_1 + \lambda)^2} + \frac{\alpha_2^2}{(\lambda_2 + \lambda)^2} \right] = (0.01) \left[ \frac{4.0}{(10.10)^2} + \frac{0.04}{(0.20)^2} \right] = 0.00039 + 0.01000 = 0.01039$$

3. **Total Ridge Mean Squared Error**:

$$\operatorname{MSE}_{\text{ridge}}(0.10) = V(0.10) + B^2(0.10) = 2.59803 + 0.01039 = 2.60842$$

By accepting a tiny squared bias of $0.01039$, Ridge Regression with $\lambda = 0.10$ slashes the total variance from $10.1000$ down to $2.59803$, cutting total Mean Squared Error by **$74.17\%$**!

### Solution, step 3: Principal Component Regression ($m = 1$) MSE and Comparison

The $1$-component Principal Component Regression estimator $\hat{\boldsymbol{\alpha}}_{\text{PCR}}(1)$ retains $\hat{\alpha}_1 = \hat{\alpha}_{1,\text{OLS}} = 2.10$ and sets $\hat{\alpha}_2 = 0$:
- **Variance of $\hat{\boldsymbol{\alpha}}_{\text{PCR}}(1)$**: Because $\hat{\alpha}_2 = 0$ is a deterministic constant with zero variance, the total variance is solely the variance of $\hat{\alpha}_1$:

$$V_{\text{PCR}}(1) = \frac{\sigma^2}{\lambda_1} + 0 = \frac{1.0}{10.0} = 0.1000$$

- **Squared Bias of $\hat{\boldsymbol{\alpha}}_{\text{PCR}}(1)$**: Since $\hat{\alpha}_1$ is unbiased for $\alpha_1$ and $\hat{\alpha}_2 = 0$ has bias $-\alpha_2 = -0.20$:

$$B_{\text{PCR}}^2(1) = 0^2 + (-\alpha_2)^2 = (-0.20)^2 = 0.0400$$

- **Total PCR Mean Squared Error**:

$$\operatorname{MSE}_{\text{PCR}}(1) = V_{\text{PCR}}(1) + B_{\text{PCR}}^2(1) = 0.1000 + 0.0400 = 0.1400$$

Comparing all three estimators:

$$\operatorname{MSE}_{\text{PCR}}(1) = 0.1400 \;<\; \operatorname{MSE}_{\text{ridge}}(0.10) = 2.6084 \;<\; \operatorname{MSE}_{\text{OLS}} = 10.1000$$

Because the true signal in the collinear direction is small ($\alpha_2^2 = 0.04 \ll \sigma^2 / \lambda_2 = 10.0$), dropping the second principal component via PCR (or setting a larger Ridge penalty $\lambda = \sigma^2 / \alpha_2^2 = 1.0 / 0.04 = 25.0$) reduces total MSE by more than $98\%$ relative to OLS!

---

### Question 3: LASSO Soft-Thresholding, Active Set Selection, and Elastic Net Solution Paths

Consider a linear regression model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $p = 4$ orthonormal predictors ($\mathbf{X}^\top \mathbf{X} = \mathbf{I}_4$) where the unconstrained Ordinary Least Squares coefficient vector is:

$$\hat{\boldsymbol{\beta}}_{\text{OLS}} = \mathbf{X}^\top \mathbf{Y} = \begin{pmatrix} 3.50 \\ -2.20 \\ 0.85 \\ -0.40 \end{pmatrix}$$

1. Using the LASSO objective $\min_{\boldsymbol{\beta}} \left\{\frac{1}{2}\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \lambda \|\boldsymbol{\beta}\|_1\right\}$, determine the exact critical penalty thresholds $\lambda_{(1)} > \lambda_{(2)} > \lambda_{(3)} > \lambda_{(4)} > 0$ at which each predictor enters the active non-zero set $\mathcal{A}(\lambda) = \{j : \hat{\beta}_{j,\text{LASSO}}(\lambda) \neq 0\}$ as $\lambda$ decreases from $\infty$ to $0$.
2. Compute the exact numerical coefficient vectors for **(a)** LASSO at $\lambda = 1.00$, **(b)** Ridge Regression at $\lambda = 1.00$ (under $\frac{1}{2}\|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 + \frac{\lambda}{2}\|\boldsymbol{\beta}\|_2^2$), and **(c)** Elastic Net at $\lambda_1 = 1.00, \lambda_2 = 0.25$.
3. Verify directly that the KKT subgradient stationarity conditions $-\mathbf{x}_j^\top(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) + \lambda s_j = 0$ are satisfied for all $j = 1, 2, 3, 4$ at the LASSO solution for $\lambda = 1.00$, explicitly finding the subgradient value $s_j \in [-1, +1]$ for each variable.

### Solution, step 1: Critical LASSO Knots and Active Set Entry Thresholds

Under an orthonormal design ($\mathbf{X}^\top \mathbf{X} = \mathbf{I}_4$), the LASSO coordinate solution is given by the soft-thresholding operator $\hat{\beta}_{j,\text{LASSO}}(\lambda) = \operatorname{sgn}(\hat{\beta}_{j,\text{OLS}})\max\left(|\hat{\beta}_{j,\text{OLS}}| - \lambda, \, 0\right)$. Consequently, the $j$-th predictor is non-zero if and only if $\lambda < |\hat{\beta}_{j,\text{OLS}}|$. Sorting the absolute OLS coefficients $|\hat{\beta}_{j,\text{OLS}}|$ in descending order yields the exact knot sequence:
- **For $\lambda \ge \lambda_{(1)} = |\hat{\beta}_{1,\text{OLS}}| = 3.50$**: All coefficients are zero, $\mathcal{A}(\lambda) = \emptyset$.
- **At $\lambda_{(1)} = 3.50$**: $X_1$ enters the active set; for $\lambda \in [2.20, 3.50)$, $\mathcal{A}(\lambda) = \{1\}$.
- **At $\lambda_{(2)} = |\hat{\beta}_{2,\text{OLS}}| = 2.20$**: $X_2$ enters the active set; for $\lambda \in [0.85, 2.20)$, $\mathcal{A}(\lambda) = \{1, 2\}$.
- **At $\lambda_{(3)} = |\hat{\beta}_{3,\text{OLS}}| = 0.85$**: $X_3$ enters the active set; for $\lambda \in [0.40, 0.85)$, $\mathcal{A}(\lambda) = \{1, 2, 3\}$.
- **At $\lambda_{(4)} = |\hat{\beta}_{4,\text{OLS}}| = 0.40$**: $X_4$ enters the active set; for $\lambda \in [0, 0.40)$, $\mathcal{A}(\lambda) = \{1, 2, 3, 4\}$.

### Solution, step 2: Exact Numerical Estimates for LASSO, Ridge, and Elastic Net

1. **LASSO Estimator at $\lambda = 1.00$**: Applying $S_{1.00}(\hat{\beta}_{j,\text{OLS}})$ to each coordinate of $(3.50, -2.20, 0.85, -0.40)^\top$:
   - $\hat{\beta}_{1,\text{LASSO}}(1.00) = +1 \times \max(3.50 - 1.00, \, 0) = +2.5000$
   - $\hat{\beta}_{2,\text{LASSO}}(1.00) = -1 \times \max(2.20 - 1.00, \, 0) = -1.2000$
   - $\hat{\beta}_{3,\text{LASSO}}(1.00) = +1 \times \max(0.85 - 1.00, \, 0) = 0.0000$
   - $\hat{\beta}_{4,\text{LASSO}}(1.00) = -1 \times \max(0.40 - 1.00, \, 0) = 0.0000$

   Thus, $\hat{\boldsymbol{\beta}}_{\text{LASSO}}(1.00) = (2.5000, \, -1.2000, \, 0.0000, \, 0.0000)^\top$, producing a sparse model with active set $\mathcal{A}(1.00) = \{1, 2\}$.

2. **Ridge Estimator at $\lambda = 1.00$**: Under $\mathbf{X}^\top \mathbf{X} = \mathbf{I}_4$, $\hat{\boldsymbol{\beta}}_{\text{ridge}}(\lambda) = (\mathbf{I}_4 + \lambda \mathbf{I}_4)^{-1}\hat{\boldsymbol{\beta}}_{\text{OLS}} = \frac{1}{1 + 1.00}\hat{\boldsymbol{\beta}}_{\text{OLS}} = 0.50\,\hat{\boldsymbol{\beta}}_{\text{OLS}}$:

$$\hat{\boldsymbol{\beta}}_{\text{ridge}}(1.00) = \begin{pmatrix} 1.7500 \\ -1.1000 \\ 0.4250 \\ -0.2000 \end{pmatrix}$$

   Every coefficient is shrunk by $50\%$, and none are zero.

3. **Elastic Net Estimator at $\lambda_1 = 1.00, \lambda_2 = 0.25$**: Dividing the LASSO soft-thresholded vector by $1 + \lambda_2 = 1.25$:

$$\hat{\boldsymbol{\beta}}_{\text{EN}}(1.00, 0.25) = \frac{1}{1.25}\hat{\boldsymbol{\beta}}_{\text{LASSO}}(1.00) = 0.80 \begin{pmatrix} 2.5000 \\ -1.2000 \\ 0.0000 \\ 0.0000 \end{pmatrix} = \begin{pmatrix} 2.0000 \\ -0.9600 \\ 0.0000 \\ 0.0000 \end{pmatrix}$$

### Solution, step 3: Direct Verification of Subgradient KKT Optimality Conditions

For an orthonormal design, the KKT condition $-\left(\hat{\beta}_{j,\text{OLS}} - \hat{\beta}_j\right) + \lambda s_j = 0$ with $\lambda = 1.00$ gives $s_j = \frac{\hat{\beta}_{j,\text{OLS}} - \hat{\beta}_j}{1.00}$:
- **$j = 1$ ($\hat{\beta}_1 = 2.50 > 0$)**: $s_1 = \frac{3.50 - 2.50}{1.00} = +1.00 = \operatorname{sgn}(\hat{\beta}_1)$ (valid).
- **$j = 2$ ($\hat{\beta}_2 = -1.20 < 0$)**: $s_2 = \frac{-2.20 - (-1.20)}{1.00} = -1.00 = \operatorname{sgn}(\hat{\beta}_2)$ (valid).
- **$j = 3$ ($\hat{\beta}_3 = 0.00$)**: $s_3 = \frac{0.85 - 0.00}{1.00} = +0.85 \in [-1, +1]$ (strictly inside the subdifferential interval $[-1, +1]$, confirming $\hat{\beta}_3 = 0$ is uniquely optimal).
- **$j = 4$ ($\hat{\beta}_4 = 0.00$)**: $s_4 = \frac{-0.40 - 0.00}{1.00} = -0.40 \in [-1, +1]$ (strictly inside $[-1, +1]$, confirming $\hat{\beta}_4 = 0$ is uniquely optimal).
