# Unit 5: Violations of Classical Assumptions: Heteroscedasticity, Weighted Least Squares, GLS & Autocorrelation

In the classical linear regression model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, the Gauss–Markov theorem establishes that the Ordinary Least Squares (OLS) estimator $\hat{\boldsymbol{\beta}}_{\text{OLS}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{Y}$ achieves minimum variance within the class of all linear unbiased estimators, provided that the stochastic disturbance vector satisfies the spherical covariance assumption $\operatorname{Var}(\boldsymbol{\varepsilon} \mid \mathbf{X}) = \sigma^2 \mathbf{I}_n$. This assumption encompasses two distinct structural requirements: **homoscedasticity**, meaning that every disturbance exhibits an identical conditional variance $\operatorname{Var}(\varepsilon_i \mid \mathbf{X}) = \sigma^2$ across all observations $i = 1, \dots, n$, and **non-autocorrelation**, meaning that distinct disturbances are conditionally uncorrelated such that $\operatorname{Cov}(\varepsilon_i, \varepsilon_j \mid \mathbf{X}) = 0$ for all $i \neq j$. In empirical econometric, biometric, and physical datasets, however, the spherical assumption is routinely violated. Cross-sectional microeconomic surveys of household consumption, corporate capital expenditure, and regional mortality rates typically exhibit dispersion that scales systematically with household wealth, firm size, or population count, generating **heteroscedasticity**. Conversely, macroeconomic, financial, and geophysical time series sampled sequentially over time exhibit inertia, cyclical persistence, and shock propagation across adjacent periods, generating **serial correlation** (or **autocorrelation**).

When the error covariance matrix departs from a scalar multiple of the identity matrix and takes the general nonspherical form $\operatorname{Var}(\boldsymbol{\varepsilon} \mid \mathbf{X}) = \sigma^2 \boldsymbol{\Omega}$, where $\boldsymbol{\Omega}$ is a symmetric positive definite $n \times n$ matrix, the classical regression apparatus suffers two fundamental breakdowns. First, although OLS remains unbiased and consistent under strict exogeneity, it forfeits the Gauss–Markov optimality property: alternative linear unbiased estimators exist that weight observations inversely to their error precision and correlation structure, achieving strictly smaller sampling variance. Second, and far more perilously for applied scientific inference, the conventional OLS variance-covariance estimator $s^2(\mathbf{X}^\top \mathbf{X})^{-1}$ becomes a systematically biased and inconsistent estimator of the true sampling variance of $\hat{\boldsymbol{\beta}}_{\text{OLS}}$. Consequently, standard $t$-ratios, $F$-statistics, confidence intervals, and prediction bands computed under classical formulas lose their nominal Student-$t$ and Snedecor-$F$ distributions, frequently inflating Type I error rates and producing spurious findings of statistical significance. In this unit, we rigorously develop the mathematical theory of nonspherical linear models, prove Aitken's Generalized Least Squares (GLS) optimality theorem, formulate Weighted Least Squares (WLS) and Feasible GLS (FGLS), derive classical and asymptotic score/Lagrange Multiplier tests for heteroscedasticity and autocorrelation, construct Huber–Eicker–White heteroscedasticity-consistent (HC0–HC4) sandwich standard errors, and analyze Prais–Winsten and Cochrane–Orcutt estimation under autoregressive disturbances.

---

## 5.1 Nonspherical Disturbances in the General Linear Model: Consequences for OLS Unbiasedness, Efficiency, and Inference

Consider the generalized linear regression model in matrix notation for $n$ observations and $p$ parameters (consisting of an intercept and $k = p - 1$ explanatory variables):

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$$

where $\mathbf{Y} \in \mathbb{R}^{n \times 1}$ is the vector of observed response variables, $\mathbf{X} \in \mathbb{R}^{n \times p}$ is a full-column-rank design matrix ($\operatorname{rank}(\mathbf{X}) = p < n$), $\boldsymbol{\beta} \in \mathbb{R}^{p \times 1}$ is the vector of unknown population regression parameters, and $\boldsymbol{\varepsilon} \in \mathbb{R}^{n \times 1}$ is the unobserved random disturbance vector. We maintain the strict exogeneity assumption $\mathbb{E}[\boldsymbol{\varepsilon} \mid \mathbf{X}] = \mathbf{0}$, which guarantees that the linear predictor $\mathbf{X}\boldsymbol{\beta}$ correctly specifies the conditional expectation function $\mathbb{E}[\mathbf{Y} \mid \mathbf{X}] = \mathbf{X}\boldsymbol{\beta}$. However, we relax the spherical error assumption and specify a general positive definite conditional covariance structure:

$$\operatorname{Var}(\boldsymbol{\varepsilon} \mid \mathbf{X}) = \mathbb{E}[\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^\top \mid \mathbf{X}] = \boldsymbol{\Sigma} = \sigma^2 \boldsymbol{\Omega}$$

Here, $\sigma^2 > 0$ is a positive scaling constant (often normalized so that $\operatorname{tr}(\boldsymbol{\Omega}) = n$), and $\boldsymbol{\Omega}$ is a symmetric, positive definite $n \times n$ matrix ($\boldsymbol{\Omega}^\top = \boldsymbol{\Omega}$ and $\mathbf{a}^\top \boldsymbol{\Omega} \mathbf{a} > 0$ for all non-zero $\mathbf{a} \in \mathbb{R}^n$). This general parameterization encompasses three primary empirical regimes:

1. **Classical Spherical Disturbances**: $\boldsymbol{\Omega} = \mathbf{I}_n$, so $\boldsymbol{\Sigma} = \sigma^2 \mathbf{I}_n$. All disturbances have constant variance $\sigma^2$ and zero pairwise covariance.
2. **Pure Heteroscedasticity**: $\boldsymbol{\Omega} = \operatorname{diag}(\omega_1, \omega_2, \dots, \omega_n)$ with $\omega_i > 0$ not all equal. The disturbances are mutually uncorrelated ($\operatorname{Cov}(\varepsilon_i, \varepsilon_j \mid \mathbf{X}) = 0$ for $i \neq j$), but the conditional variance varies across observations as $\operatorname{Var}(\varepsilon_i \mid \mathbf{X}) = \sigma_i^2 = \sigma^2 \omega_i$.
3. **Serial Correlation / Autocorrelation and Spatial Dependence**: $\boldsymbol{\Omega}$ contains non-zero off-diagonal entries $\omega_{ij} \neq 0$ for $i \neq j$, reflecting temporal correlation across time-series observations or spatial correlation across geographic units.

### Unbiasedness and Consistency of OLS Under Nonspherical Errors

Suppose an investigator applies Ordinary Least Squares to estimate $\boldsymbol{\beta}$ without accounting for the non-identity structure of $\boldsymbol{\Omega}$:

$$\hat{\boldsymbol{\beta}}_{\text{OLS}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{Y} = \boldsymbol{\beta} + (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\varepsilon}$$

Taking the conditional expectation given $\mathbf{X}$, we observe that unbiasedness depends exclusively on the first-moment condition $\mathbb{E}[\boldsymbol{\varepsilon} \mid \mathbf{X}] = \mathbf{0}$ and requires no assumptions regarding the second-moment matrix $\boldsymbol{\Omega}$:

$$\mathbb{E}[\hat{\boldsymbol{\beta}}_{\text{OLS}} \mid \mathbf{X}] = \boldsymbol{\beta} + (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbb{E}[\boldsymbol{\varepsilon} \mid \mathbf{X}] = \boldsymbol{\beta}$$

Thus, **OLS remains unconditionally and conditionally unbiased under arbitrary heteroscedasticity and autocorrelation**, provided that the regressors are exogenous. Furthermore, if the sample size grows ($n \to \infty$) such that the empirical Gram matrix converges in probability to a finite positive definite matrix, $\operatorname{plim}_{n \to \infty} \left(\frac{1}{n}\mathbf{X}^\top \mathbf{X}\right) = \mathbf{Q}_{XX}$, and the scaled error covariance satisfies $\lim_{n \to \infty} \frac{1}{n^2} \mathbf{X}^\top (\sigma^2 \boldsymbol{\Omega}) \mathbf{X} = \mathbf{0}$, then $\operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}} \mid \mathbf{X}) \to \mathbf{0}$ in matrix norm. By Chebyshev's inequality, $\hat{\boldsymbol{\beta}}_{\text{OLS}} \xrightarrow{P} \boldsymbol{\beta}$, confirming that OLS remains weakly consistent in large samples under mild regularity conditions on the growth of $\boldsymbol{\Omega}$.

### True Sampling Variance of OLS Versus the Naive Covariance Matrix

Despite preserving unbiasedness, the sampling precision of $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ is profoundly altered by $\boldsymbol{\Omega}$. We derive the exact conditional variance-covariance matrix of the OLS estimator by evaluating the outer product of the estimation error $\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\varepsilon}$:

$$\operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}} \mid \mathbf{X}) = \mathbb{E}\left[ (\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta})(\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta})^\top \;\middle|\; \mathbf{X} \right] = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbb{E}[\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^\top \mid \mathbf{X}] \mathbf{X}(\mathbf{X}^\top \mathbf{X})^{-1}$$

Substituting $\mathbb{E}[\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^\top \mid \mathbf{X}] = \sigma^2 \boldsymbol{\Omega} = \boldsymbol{\Sigma}$, we obtain the **true sandwich variance-covariance matrix of OLS**:

$$\operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}} \mid \mathbf{X}) = \sigma^2 (\mathbf{X}^\top \mathbf{X})^{-1} (\mathbf{X}^\top \boldsymbol{\Omega} \mathbf{X}) (\mathbf{X}^\top \mathbf{X})^{-1} = (\mathbf{X}^\top \mathbf{X})^{-1} (\mathbf{X}^\top \boldsymbol{\Sigma} \mathbf{X}) (\mathbf{X}^\top \mathbf{X})^{-1}$$

Notice that the outer factors $(\mathbf{X}^\top \mathbf{X})^{-1}$ form the "bread" of the sandwich, while the middle matrix $\mathbf{X}^\top \boldsymbol{\Sigma} \mathbf{X}$ forms the "meat." Under the classical spherical assumption ($\boldsymbol{\Omega} = \mathbf{I}_n$), the middle factor collapses to $\mathbf{X}^\top \mathbf{I}_n \mathbf{X} = \mathbf{X}^\top \mathbf{X}$, cancelling one inverse factor and reducing to the familiar formula $\sigma^2 (\mathbf{X}^\top \mathbf{X})^{-1}$. When $\boldsymbol{\Omega} \neq \mathbf{I}_n$, no such cancellation occurs, and the true variance $(\mathbf{X}^\top \mathbf{X})^{-1}(\mathbf{X}^\top \boldsymbol{\Sigma} \mathbf{X})(\mathbf{X}^\top \mathbf{X})^{-1}$ differs structurally from $\sigma^2(\mathbf{X}^\top \mathbf{X})^{-1}$.

### Mathematical Proof of the Bias of the Classical Residual Variance Estimator $s^2$

Even more subtle is the behavior of the classical residual variance estimator $s^2 = \frac{\mathbf{e}^\top \mathbf{e}}{n - p}$, where $\mathbf{e} = \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}_{\text{OLS}} = (\mathbf{I}_n - \mathbf{H})\boldsymbol{\varepsilon}$ is the OLS residual vector and $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top$ is the orthogonal projection (hat) matrix. Taking the expectation of the Residual Sum of Squares ($\text{SSE} = \mathbf{e}^\top \mathbf{e}$) using the cyclic permutation invariance of the matrix trace operator $\operatorname{tr}(\mathbf{A}\mathbf{B}) = \operatorname{tr}(\mathbf{B}\mathbf{A})$, we obtain:

$$\mathbb{E}[\mathbf{e}^\top \mathbf{e} \mid \mathbf{X}] = \mathbb{E}\left[ \boldsymbol{\varepsilon}^\top (\mathbf{I}_n - \mathbf{H})^\top (\mathbf{I}_n - \mathbf{H}) \boldsymbol{\varepsilon} \;\middle|\; \mathbf{X} \right] = \mathbb{E}\left[ \operatorname{tr}\left( (\mathbf{I}_n - \mathbf{H}) \boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^\top \right) \;\middle|\; \mathbf{X} \right] = \sigma^2 \operatorname{tr}\left( (\mathbf{I}_n - \mathbf{H})\boldsymbol{\Omega} \right)$$

Expanding the trace yields:

$$\mathbb{E}[s^2 \mid \mathbf{X}] = \frac{\sigma^2}{n - p} \left[ \operatorname{tr}(\boldsymbol{\Omega}) - \operatorname{tr}(\mathbf{H}\boldsymbol{\Omega}) \right] = \frac{\sigma^2}{n - p} \left[ \operatorname{tr}(\boldsymbol{\Omega}) - \operatorname{tr}\left( (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\Omega} \mathbf{X} \right) \right]$$

Consequently, the naive OLS covariance matrix estimator $\widehat{\operatorname{Var}}_{\text{naive}}(\hat{\boldsymbol{\beta}}_{\text{OLS}}) = s^2 (\mathbf{X}^\top \mathbf{X})^{-1}$ has expected value:

$$\mathbb{E}\left[ s^2 (\mathbf{X}^\top \mathbf{X})^{-1} \;\middle|\; \mathbf{X} \right] = \frac{\sigma^2}{n - p} \left[ \operatorname{tr}(\boldsymbol{\Omega}) - \operatorname{tr}(\mathbf{H}\boldsymbol{\Omega}) \right] (\mathbf{X}^\top \mathbf{X})^{-1} \neq \sigma^2 (\mathbf{X}^\top \mathbf{X})^{-1} (\mathbf{X}^\top \boldsymbol{\Omega} \mathbf{X}) (\mathbf{X}^\top \mathbf{X})^{-1}$$

To appreciate the practical direction of this bias, consider simple linear regression $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ under pure heteroscedasticity ($\operatorname{Var}(\varepsilon_i) = \sigma_i^2$, $\operatorname{Cov}(\varepsilon_i, \varepsilon_j) = 0$). The true sampling variance of the OLS slope estimator $\hat{\beta}_{1,\text{OLS}} = \frac{\sum_{i=1}^n (x_i - \bar{x})Y_i}{S_{xx}}$ (where $S_{xx} = \sum_{i=1}^n (x_i - \bar{x})^2$) is:

$$\operatorname{Var}(\hat{\beta}_{1,\text{OLS}}) = \frac{\sum_{i=1}^n (x_i - \bar{x})^2 \sigma_i^2}{S_{xx}^2}$$

Meanwhile, in large samples, the naive estimator $s^2 / S_{xx}$ converges approximately to $\frac{\bar{\sigma}^2}{S_{xx}}$, where $\bar{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n \sigma_i^2$ is the average error variance. Subtracting the approximate naive variance from the true variance reveals a covariance relationship between squared predictor deviations and error variances:

$$\operatorname{Var}(\hat{\beta}_{1,\text{OLS}}) - \frac{\bar{\sigma}^2}{S_{xx}} = \frac{\sum_{i=1}^n \left[ (x_i - \bar{x})^2 - \frac{S_{xx}}{n} \right] (\sigma_i^2 - \bar{\sigma}^2)}{S_{xx}^2}$$

Whenever observations with extreme predictor values (large $(x_i - \bar{x})^2$, i.e., high leverage $h_{ii}$) also exhibit high error variance $\sigma_i^2$—the standard empirical case when variance increases with $x_i$—the numerator is strictly positive. In this prevalent scenario, **the naive OLS standard error systematically underestimates the true standard error of $\hat{\beta}_{1,\text{OLS}}$**, producing artificially inflated $t$-statistics and confidence intervals whose actual coverage probability falls substantially below $1 - \alpha$.

---

## 5.2 Aitken's Generalized Least Squares (GLS), Cholesky Whitening Transformations, and the Aitken–Gauss–Markov Theorem

When the positive definite error covariance structure $\boldsymbol{\Omega}$ is known, Alexander Aitken (1935) demonstrated that optimal estimation can be fully restored by transforming the regression system into an equivalent homoscedastic, uncorrelated representation—a procedure known in signal processing and econometrics as **pre-whitening**.

### Matrix Spectral and Cholesky Factorization of $\boldsymbol{\Omega}$

Because $\boldsymbol{\Omega} \in \mathbb{R}^{n \times n}$ is symmetric and strictly positive definite, all of its eigenvalues $\lambda_1, \dots, \lambda_n$ are real and strictly positive, and its inverse $\boldsymbol{\Omega}^{-1}$ is likewise symmetric and positive definite. By the spectral decomposition theorem (or via Cholesky factorization), there exists a non-singular $n \times n$ matrix $\mathbf{P}$ (often called the **whitening matrix** or symmetric square root $\boldsymbol{\Omega}^{-1/2}$) such that:

$$\boldsymbol{\Omega}^{-1} = \mathbf{P}^\top \mathbf{P} \quad \Longleftrightarrow \quad \mathbf{P} \boldsymbol{\Omega} \mathbf{P}^\top = \mathbf{I}_n \quad \Longleftrightarrow \quad \boldsymbol{\Omega} = \mathbf{P}^{-1} (\mathbf{P}^\top)^{-1}$$

Pre-multiplying the structural regression equation $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ on the left by $\mathbf{P}$ yields the transformed linear model:

$$\mathbf{P}\mathbf{Y} = \mathbf{P}\mathbf{X}\boldsymbol{\beta} + \mathbf{P}\boldsymbol{\varepsilon} \quad \Longleftrightarrow \quad \mathbf{Y}^* = \mathbf{X}^*\boldsymbol{\beta} + \boldsymbol{\varepsilon}^*$$

where $\mathbf{Y}^* = \mathbf{P}\mathbf{Y}$, $\mathbf{X}^* = \mathbf{P}\mathbf{X}$, and $\boldsymbol{\varepsilon}^* = \mathbf{P}\boldsymbol{\varepsilon}$. Let us verify that the transformed model satisfies all classical Gauss–Markov assumptions:
1. **Full Column Rank**: Since $\mathbf{P}$ is non-singular ($\operatorname{rank}(\mathbf{P}) = n$) and $\operatorname{rank}(\mathbf{X}) = p$, Sylvester's rank inequality guarantees $\operatorname{rank}(\mathbf{X}^*) = \operatorname{rank}(\mathbf{P}\mathbf{X}) = p$.
2. **Zero Conditional Mean**: $\mathbb{E}[\boldsymbol{\varepsilon}^* \mid \mathbf{X}] = \mathbf{P}\mathbb{E}[\boldsymbol{\varepsilon} \mid \mathbf{X}] = \mathbf{P}\mathbf{0} = \mathbf{0}$.
3. **Spherical Transformed Error Covariance**: Evaluating the conditional covariance matrix of $\boldsymbol{\varepsilon}^*$ gives:

$$\operatorname{Var}(\boldsymbol{\varepsilon}^* \mid \mathbf{X}) = \mathbb{E}\left[ \boldsymbol{\varepsilon}^* (\boldsymbol{\varepsilon}^*)^\top \;\middle|\; \mathbf{X} \right] = \mathbf{P} \mathbb{E}[\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^\top \mid \mathbf{X}] \mathbf{P}^\top = \mathbf{P} (\sigma^2 \boldsymbol{\Omega}) \mathbf{P}^\top = \sigma^2 (\mathbf{P} \boldsymbol{\Omega} \mathbf{P}^\top) = \sigma^2 \mathbf{I}_n$$

### Derivation of the Generalized Least Squares (GLS) Estimator

Because the transformed model $\mathbf{Y}^* = \mathbf{X}^*\boldsymbol{\beta} + \boldsymbol{\varepsilon}^*$ satisfies the classical spherical assumptions, we obtain the optimal estimator of $\boldsymbol{\beta}$ by applying Ordinary Least Squares to the transformed quantities $(\mathbf{Y}^*, \mathbf{X}^*)$. Minimizing the transformed sum of squared residuals corresponds to minimizing the generalized quadratic form in the Mahalanobis metric induced by $\boldsymbol{\Omega}^{-1}$:

$$S_{\text{GLS}}(\boldsymbol{\beta}) = (\mathbf{Y}^* - \mathbf{X}^*\boldsymbol{\beta})^\top (\mathbf{Y}^* - \mathbf{X}^*\boldsymbol{\beta}) = (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top \mathbf{P}^\top \mathbf{P} (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}) = (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top \boldsymbol{\Omega}^{-1} (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})$$

Differentiating $S_{\text{GLS}}(\boldsymbol{\beta})$ with respect to $\boldsymbol{\beta}$ and setting the gradient vector to zero yields the **Generalized Normal Equations**:

$$\frac{\partial S_{\text{GLS}}(\boldsymbol{\beta})}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{Y} + 2(\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})\hat{\boldsymbol{\beta}}_{\text{GLS}} = \mathbf{0}$$

Since $\mathbf{X}$ has full column rank $p$ and $\boldsymbol{\Omega}^{-1}$ is strictly positive definite, for any non-zero vector $\mathbf{c} \in \mathbb{R}^p$ the vector $\mathbf{z} = \mathbf{X}\mathbf{c}$ is non-zero, so $\mathbf{c}^\top (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})\mathbf{c} = \mathbf{z}^\top \boldsymbol{\Omega}^{-1}\mathbf{z} > 0$. Thus $\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X}$ is positive definite and invertible. Solving for $\hat{\boldsymbol{\beta}}_{\text{GLS}}$ gives **Aitken's Generalized Least Squares (GLS) Estimator**:

$$\hat{\boldsymbol{\beta}}_{\text{GLS}} = (\mathbf{X}^*\top \mathbf{X}^*)^{-1}\mathbf{X}^*\top \mathbf{Y}^* = \left(\mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{X}\right)^{-1} \mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{Y}$$

The variance-covariance matrix of $\hat{\boldsymbol{\beta}}_{\text{GLS}}$ follows directly from substituting $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$:

$$\hat{\boldsymbol{\beta}}_{\text{GLS}} - \boldsymbol{\beta} = \left(\mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{X}\right)^{-1} \mathbf{X}^\top \boldsymbol{\Omega}^{-1} \boldsymbol{\varepsilon}$$

$$\operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{GLS}} \mid \mathbf{X}) = \left(\mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{X}\right)^{-1} \mathbf{X}^\top \boldsymbol{\Omega}^{-1} (\sigma^2 \boldsymbol{\Omega}) \boldsymbol{\Omega}^{-1} \mathbf{X} \left(\mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{X}\right)^{-1} = \sigma^2 \left(\mathbf{X}^\top \boldsymbol{\Omega}^{-1} \mathbf{X}\right)^{-1}$$

Moreover, the unbiased estimator of the scalar scale parameter $\sigma^2$ is the normalized generalized residual sum of squares:

$$\hat{\sigma}_{\text{GLS}}^2 = \frac{(\mathbf{Y}^* - \mathbf{X}^*\hat{\boldsymbol{\beta}}_{\text{GLS}})^\top (\mathbf{Y}^* - \mathbf{X}^*\hat{\boldsymbol{\beta}}_{\text{GLS}})}{n - p} = \frac{(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}_{\text{GLS}})^\top \boldsymbol{\Omega}^{-1} (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}_{\text{GLS}})}{n - p}$$

### Theorem and Proof: The Aitken–Gauss–Markov Theorem

> [!IMPORTANT]
> **Theorem (Aitken, 1935)**: In the generalized linear model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $\mathbb{E}[\boldsymbol{\varepsilon} \mid \mathbf{X}] = \mathbf{0}$ and $\operatorname{Var}(\boldsymbol{\varepsilon} \mid \mathbf{X}) = \sigma^2 \boldsymbol{\Omega}$ where $\boldsymbol{\Omega}$ is a known positive definite matrix and $\operatorname{rank}(\mathbf{X}) = p$, the GLS estimator $\hat{\boldsymbol{\beta}}_{\text{GLS}} = (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{Y}$ is the unique **Best Linear Unbiased Estimator (BLUE)** of $\boldsymbol{\beta}$. That is, for any other linear unbiased estimator $\tilde{\boldsymbol{\beta}} = \mathbf{C}\mathbf{Y}$, the covariance matrix difference $\operatorname{Var}(\tilde{\boldsymbol{\beta}} \mid \mathbf{X}) - \operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{GLS}} \mid \mathbf{X})$ is positive semi-definite.

**Proof**: Let $\tilde{\boldsymbol{\beta}} = \mathbf{C}\mathbf{Y}$ be an arbitrary linear estimator of $\boldsymbol{\beta}$, where $\mathbf{C} \in \mathbb{R}^{p \times n}$ is a non-stochastic matrix (or measurable with respect to $\mathbf{X}$). Define the discrepancy matrix $\mathbf{D} = \mathbf{C} - (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\Omega}^{-1}$, so that $\mathbf{C} = (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\Omega}^{-1} + \mathbf{D}$. Taking the conditional expectation of $\tilde{\boldsymbol{\beta}}$ gives:

$$\mathbb{E}[\tilde{\boldsymbol{\beta}} \mid \mathbf{X}] = \mathbf{C}\mathbf{X}\boldsymbol{\beta} = \left[ (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X} + \mathbf{D}\mathbf{X} \right]\boldsymbol{\beta} = \boldsymbol{\beta} + \mathbf{D}\mathbf{X}\boldsymbol{\beta}$$

For $\tilde{\boldsymbol{\beta}}$ to be unbiased for all parameter vectors $\boldsymbol{\beta} \in \mathbb{R}^p$, it is necessary and sufficient that $\mathbf{D}\mathbf{X} = \mathbf{0}_{p \times p}$. Now compute the variance-covariance matrix of $\tilde{\boldsymbol{\beta}}$:

$$\operatorname{Var}(\tilde{\boldsymbol{\beta}} \mid \mathbf{X}) = \sigma^2 \mathbf{C} \boldsymbol{\Omega} \mathbf{C}^\top = \sigma^2 \left[ (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\Omega}^{-1} + \mathbf{D} \right] \boldsymbol{\Omega} \left[ \boldsymbol{\Omega}^{-1}\mathbf{X}(\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1} + \mathbf{D}^\top \right]$$

Expanding the quadratic product yields four terms:

$$\operatorname{Var}(\tilde{\boldsymbol{\beta}} \mid \mathbf{X}) = \sigma^2 (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1} + \sigma^2 (\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1}\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\boldsymbol{\Omega}\mathbf{D}^\top + \sigma^2 \mathbf{D}\boldsymbol{\Omega}\boldsymbol{\Omega}^{-1}\mathbf{X}(\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X})^{-1} + \sigma^2 \mathbf{D}\boldsymbol{\Omega}\mathbf{D}^\top$$

Observe that the two cross-product terms simplify via $\boldsymbol{\Omega}^{-1}\boldsymbol{\Omega} = \mathbf{I}_n$ and vanish identically by the unbiasedness orthogonality condition $\mathbf{D}\mathbf{X} = \mathbf{0}$ (and $\mathbf{X}^\top \mathbf{D}^\top = (\mathbf{D}\mathbf{X})^\top = \mathbf{0}$):

$$\operatorname{Var}(\tilde{\boldsymbol{\beta}} \mid \mathbf{X}) = \operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{GLS}} \mid \mathbf{X}) + \sigma^2 \mathbf{D}\boldsymbol{\Omega}\mathbf{D}^\top$$

Because $\boldsymbol{\Omega}$ is positive definite, for any vector $\mathbf{a} \in \mathbb{R}^p$, the quadratic form $\mathbf{a}^\top (\sigma^2 \mathbf{D}\boldsymbol{\Omega}\mathbf{D}^\top)\mathbf{a} = \sigma^2 (\mathbf{D}^\top \mathbf{a})^\top \boldsymbol{\Omega} (\mathbf{D}^\top \mathbf{a}) \ge 0$, proving that $\operatorname{Var}(\tilde{\boldsymbol{\beta}} \mid \mathbf{X}) - \operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{GLS}} \mid \mathbf{X}) = \sigma^2 \mathbf{D}\boldsymbol{\Omega}\mathbf{D}^\top$ is positive semi-definite. In particular, selecting $\tilde{\boldsymbol{\beta}} = \hat{\boldsymbol{\beta}}_{\text{OLS}}$ reveals that $\operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{OLS}} \mid \mathbf{X}) - \operatorname{Var}(\hat{\boldsymbol{\beta}}_{\text{GLS}} \mid \mathbf{X})$ is positive semi-definite (and strictly positive definite unless the column space of $\boldsymbol{\Omega}\mathbf{X}$ coincides with the column space of $\mathbf{X}$, known as **Zyskind's condition** or **Kruskal's theorem**). $\blacksquare$

---

## 5.3 Weighted Least Squares (WLS) Under Heteroscedasticity and Feasible Generalized Least Squares (FGLS)

An important specialization of Generalized Least Squares arises when the disturbances are mutually uncorrelated across observations ($\operatorname{Cov}(\varepsilon_i, \varepsilon_j \mid \mathbf{X}) = 0$ for $i \neq j$), but exhibit non-constant conditional variance $\operatorname{Var}(\varepsilon_i \mid \mathbf{X}) = \sigma_i^2 = \sigma^2 \omega_i$. In this pure heteroscedasticity regime, the covariance matrix $\boldsymbol{\Omega}$ and its inverse $\boldsymbol{\Omega}^{-1}$ are diagonal matrices:

$$\boldsymbol{\Omega} = \operatorname{diag}(\omega_1, \omega_2, \dots, \omega_n), \qquad \boldsymbol{\Omega}^{-1} = \mathbf{W} = \operatorname{diag}(w_1, w_2, \dots, w_n) \quad \text{where } w_i = \frac{1}{\omega_i} = \frac{\sigma^2}{\sigma_i^2}$$

The symmetric whitening matrix is simply the diagonal matrix of inverse standard deviations, $\mathbf{P} = \mathbf{W}^{1/2} = \operatorname{diag}(\sqrt{w_1}, \sqrt{w_2}, \dots, \sqrt{w_n})$. Applying $\mathbf{P}$ to the $i$-th row of the regression system $Y_i = \beta_0 + \beta_1 X_{i1} + \dots + \beta_{p-1} X_{i,p-1} + \varepsilon_i$ divides every term in the $i$-th observation (including the intercept column of ones!) by $\sqrt{\omega_i}$:

$$\frac{Y_i}{\sqrt{\omega_i}} = \beta_0 \left(\frac{1}{\sqrt{\omega_i}}\right) + \beta_1 \left(\frac{X_{i1}}{\sqrt{\omega_i}}\right) + \dots + \beta_{p-1} \left(\frac{X_{i,p-1}}{\sqrt{\omega_i}}\right) + \frac{\varepsilon_i}{\sqrt{\omega_i}}$$

Each transformed error $\varepsilon_i^* = \varepsilon_i / \sqrt{\omega_i}$ now has constant variance $\operatorname{Var}(\varepsilon_i^* \mid \mathbf{X}) = \frac{1}{\omega_i}\operatorname{Var}(\varepsilon_i \mid \mathbf{X}) = \frac{\sigma^2 \omega_i}{\omega_i} = \sigma^2$. Notice that the transformed equation has **no constant intercept column** unless one of the original regressors was already proportional to $\sqrt{\omega_i}$; instead, $\beta_0$ is the slope coefficient attached to the reciprocal square-root weight variable $1/\sqrt{\omega_i}$.

### The WLS Objective Function and Normal Equations

The GLS criterion under diagonal $\boldsymbol{\Omega}$ reduces to minimizing the **weighted sum of squared residuals**, where each squared residual is weighted by $w_i = 1/\omega_i \propto 1/\sigma_i^2$:

$$S_{\text{WLS}}(\boldsymbol{\beta}) = \sum_{i=1}^n w_i \left( Y_i - \mathbf{x}_i^\top \boldsymbol{\beta} \right)^2 = (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^\top \mathbf{W} (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})$$

This yields the **Weighted Least Squares (WLS) Estimator**:

$$\hat{\boldsymbol{\beta}}_{\text{WLS}} = \left(\mathbf{X}^\top \mathbf{W} \mathbf{X}\right)^{-1} \mathbf{X}^\top \mathbf{W} \mathbf{Y} = \left( \sum_{i=1}^n w_i \mathbf{x}_i \mathbf{x}_i^\top \right)^{-1} \left( \sum_{i=1}^n w_i \mathbf{x}_i Y_i \right)$$

Intuitively, WLS assigns high analytical weight $w_i$ to observations drawn from low-variance, high-precision sub-populations (small $\sigma_i^2$), forcing the fitted hyperplane to pass closely through reliable data points, while down-weighting noisy, volatile observations (large $\sigma_i^2$) so that erratic outliers do not pull the regression surface off course.

In the special case of **Simple Linear Regression** $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ with weights $w_i > 0$, minimizing $\sum_{i=1}^n w_i (Y_i - \beta_0 - \beta_1 x_i)^2$ yields closed-form expressions that parallel classical OLS except that unweighted sample means are replaced by weighted sample means $\bar{x}_w = \frac{\sum_{i=1}^n w_i x_i}{\sum_{i=1}^n w_i}$ and $\bar{Y}_w = \frac{\sum_{i=1}^n w_i Y_i}{\sum_{i=1}^n w_i}$:

$$\hat{\beta}_{1,\text{WLS}} = \frac{\sum_{i=1}^n w_i (x_i - \bar{x}_w)(Y_i - \bar{Y}_w)}{\sum_{i=1}^n w_i (x_i - \bar{x}_w)^2}, \qquad \hat{\beta}_{0,\text{WLS}} = \bar{Y}_w - \hat{\beta}_{1,\text{WLS}} \bar{x}_w$$

with exact sampling variance $\operatorname{Var}(\hat{\beta}_{1,\text{WLS}}) = \frac{\sigma^2}{\sum_{i=1}^n w_i (x_i - \bar{x}_w)^2}$. By the Cauchy–Schwarz inequality, for any positive sequence $\omega_i$:

$$\left( \sum_{i=1}^n (x_i - \bar{x})^2 \omega_i \right) \left( \sum_{i=1}^n \frac{(x_i - \bar{x}_w)^2}{\omega_i} \right) \ge \left( \sum_{i=1}^n (x_i - \bar{x})(x_i - \bar{x}_w) \right)^2 = \left( \sum_{i=1}^n (x_i - \bar{x})^2 \right)^2$$

which immediately implies $\operatorname{Var}(\hat{\beta}_{1,\text{WLS}}) \le \operatorname{Var}(\hat{\beta}_{1,\text{OLS}})$, with strict inequality whenever $\omega_i$ varies across observations with $x_i \neq \bar{x}$.

### Common Empirical Sources of Known vs. Unknown Weights

1. **Grouped / Cell-Mean Aggregated Data**: Suppose micro-level observations $Y_{ij} = \mathbf{x}_i^\top \boldsymbol{\beta} + \varepsilon_{ij}$ ($j = 1, \dots, n_i$) within region or demographic cell $i$ satisfy homoscedastic individual variance $\operatorname{Var}(\varepsilon_{ij}) = \sigma^2$, but the investigator only observes cell averages $\bar{Y}_i = \frac{1}{n_i}\sum_{j=1}^{n_i} Y_{ij}$ based on group sizes $n_i$. Then $\bar{Y}_i = \mathbf{x}_i^\top \boldsymbol{\beta} + \bar{\varepsilon}_i$, where the averaged error has variance $\operatorname{Var}(\bar{\varepsilon}_i) = \frac{\sigma^2}{n_i}$. Here $\omega_i = 1/n_i$ is known exactly from the sample sizes, so WLS uses weights $w_i = n_i$, multiplying each cell-mean equation by $\sqrt{n_i}$.
2. **Proportional Variance Models**: In cross-sectional expenditure models, standard deviation often scales proportionally with a size variable $Z_i$ (e.g., firm assets or household income): $\operatorname{SD}(\varepsilon_i \mid Z_i) = \sigma Z_i$, so $\operatorname{Var}(\varepsilon_i \mid Z_i) = \sigma^2 Z_i^2$. Here $\omega_i = Z_i^2$ and WLS weights are $w_i = 1/Z_i^2$, dividing the regression equation through by $Z_i$.

### Feasible Generalized Least Squares (FGLS / Two-Step Estimation)

In most econometric applications, the covariance matrix $\boldsymbol{\Omega}$ is not known *a priori*. If $\boldsymbol{\Omega}$ contained $n(n+1)/2$ unrestricted unknown parameters, total parameters would exceed the sample size $n$, rendering estimation impossible (an incidental parameters problem). Instead, **Feasible Generalized Least Squares (FGLS)** specifies $\boldsymbol{\Omega} = \boldsymbol{\Omega}(\boldsymbol{\gamma})$ as a smooth parametric function of a low-dimensional parameter vector $\boldsymbol{\gamma} \in \mathbb{R}^m$ ($m \ll n$). A standard specification for heteroscedasticity is the **multiplicative exponential skedastic function** (Harvey, 1976):

$$\sigma_i^2 = \exp\left( \alpha_0 + \mathbf{z}_i^\top \boldsymbol{\gamma} \right) = \sigma^2 \exp\left(\mathbf{z}_i^\top \boldsymbol{\gamma}\right)$$

where $\mathbf{z}_i \in \mathbb{R}^m$ is a vector of exogenous variance-driving variables (often a subset of $\mathbf{x}_i$), and $\sigma^2 = e^{\alpha_0}$. The exponential form guarantees strictly positive predicted variances $\hat{\sigma}_i^2 > 0$ for any parameter vector $\hat{\boldsymbol{\gamma}}$. The two-step FGLS procedure proceeds as follows:

- **Step 1 (Consistent Initial OLS and Residual Extraction)**: Estimate $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ by OLS to obtain consistent residuals $e_i = Y_i - \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}_{\text{OLS}}$.
- **Step 2 (Auxiliary Skedastic Regression)**: Take the natural logarithm of the squared OLS residuals $\ln(e_i^2) = \alpha_0 + \mathbf{z}_i^\top \boldsymbol{\gamma} + v_i$, where $v_i = \ln(e_i^2 / \sigma_i^2)$, and estimate $(\hat{\alpha}_0, \hat{\boldsymbol{\gamma}})$ via OLS. Compute fitted variance weights $\hat{\omega}_i = \exp(\mathbf{z}_i^\top \hat{\boldsymbol{\gamma}})$ and form $\hat{\boldsymbol{\Omega}} = \operatorname{diag}(\hat{\omega}_1, \dots, \hat{\omega}_n)$.
- **Step 3 (Feasible WLS Update)**: Compute the FGLS estimator by replacing $\boldsymbol{\Omega}$ with its consistent plug-in estimate $\hat{\boldsymbol{\Omega}}$:

$$\hat{\boldsymbol{\beta}}_{\text{FGLS}} = \left(\mathbf{X}^\top \hat{\boldsymbol{\Omega}}^{-1} \mathbf{X}\right)^{-1} \mathbf{X}^\top \hat{\boldsymbol{\Omega}}^{-1} \mathbf{Y}$$

Under standard regularity conditions—specifically, if $\hat{\boldsymbol{\gamma}} \xrightarrow{P} \boldsymbol{\gamma}$ such that $\operatorname{plim}_{n \to \infty} \frac{1}{n}\mathbf{X}^\top (\hat{\boldsymbol{\Omega}}^{-1} - \boldsymbol{\Omega}^{-1})\mathbf{X} = \mathbf{0}$ and $\operatorname{plim}_{n \to \infty} \frac{1}{\sqrt{n}}\mathbf{X}^\top (\hat{\boldsymbol{\Omega}}^{-1} - \boldsymbol{\Omega}^{-1})\boldsymbol{\varepsilon} = \mathbf{0}$—the estimation error in $\hat{\boldsymbol{\Omega}}$ vanishes asymptotically at a faster rate than the $\sqrt{n}$-scaled regression score. Consequently, $\hat{\boldsymbol{\beta}}_{\text{FGLS}}$ is **asymptotically equivalent** to the infeasible exact GLS estimator:

$$\sqrt{n}\left( \hat{\boldsymbol{\beta}}_{\text{FGLS}} - \hat{\boldsymbol{\beta}}_{\text{GLS}} \right) \xrightarrow{P} \mathbf{0} \quad \Longrightarrow \quad \sqrt{n}\left(\hat{\boldsymbol{\beta}}_{\text{FGLS}} - \boldsymbol{\beta}\right) \xrightarrow{d} \mathcal{N}_p\left( \mathbf{0}, \; \sigma^2 \operatorname{plim}_{n \to \infty} \left(\frac{1}{n}\mathbf{X}^\top \boldsymbol{\Omega}^{-1}\mathbf{X}\right)^{-1} \right)$$

> [!WARNING]
> **Finite-Sample Caveat of FGLS**: Although $\hat{\boldsymbol{\beta}}_{\text{FGLS}}$ is asymptotically efficient when the skedastic function $\sigma_i^2 = \sigma^2 \omega(\mathbf{z}_i; \boldsymbol{\gamma})$ is correctly specified, $\hat{\boldsymbol{\beta}}_{\text{FGLS}}$ is a non-linear function of $\mathbf{Y}$ (because $\hat{\boldsymbol{\Omega}}$ depends on the data $\mathbf{Y}$ via the first-stage OLS residuals). Consequently, in finite samples, FGLS is generally neither exactly unbiased nor guaranteed to have smaller variance than OLS if $\hat{\boldsymbol{\gamma}}$ is noisily estimated.

---

## 5.4 Diagnostic Testing for Heteroscedasticity: Goldfeld–Quandt, Breusch–Pagan–Godfrey, Glejser, and White's General Specification Test

Before abandoning classical OLS inference or specifying an FGLS variance model, an empirical researcher must test the null hypothesis of homoscedasticity $H_0: \sigma_1^2 = \sigma_2^2 = \dots = \sigma_n^2 = \sigma^2$ against structured or unstructured heteroscedastic alternatives. Because the true disturbances $\varepsilon_i$ are unobserved, all diagnostic tests use the OLS residuals $e_i = Y_i - \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}_{\text{OLS}}$ as empirical proxies for $\varepsilon_i$.

### 1. The Goldfeld–Quandt Exact Finite-Sample $F$-Test (1965)

When error variance is suspected to be a monotonic function of a single known continuous explanatory variable $X_j$ (e.g., $\sigma_i^2 = \sigma^2 X_{ij}^2$) and the disturbances are normally distributed ($\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma})$), Stephen Goldfeld and Richard Quandt constructed an exact finite-sample $F$-test by partitioning the sample into low-variance and high-variance regimes:

1. **Order Observations**: Sort the $n$ observations in ascending order of the suspect variable $X_{ij}$.
2. **Omit Central Observations**: Discard $c$ central observations (typically $c \approx n/5$ to $n/4$) to sharpen the variance contrast between the lower and upper extremes, leaving two subsamples of size $n_1 = \frac{n - c}{2}$ (low $X_j$) and $n_2 = \frac{n - c}{2}$ (high $X_j$), requiring $n_1 > p$.
3. **Separate OLS Regressions**: Fit the linear regression model separately to the first $n_1$ observations and the last $n_2$ observations, obtaining residual sums of squares $\text{SSE}_1$ (with $n_1 - p$ degrees of freedom) and $\text{SSE}_2$ (with $n_2 - p$ degrees of freedom).
4. **Test Statistic**: Under $H_0: \sigma_i^2 = \sigma^2$ and normal independent errors, the two subsamples are completely independent, so $\frac{\text{SSE}_1}{\sigma^2} \sim \chi^2_{n_1 - p}$ and $\frac{\text{SSE}_2}{\sigma^2} \sim \chi^2_{n_2 - p}$ independently. The Goldfeld–Quandt statistic follows an exact Snedecor $F$-distribution under $H_0$:

$$F_{\text{GQ}} = \frac{\text{SSE}_2 / (n_2 - p)}{\text{SSE}_1 / (n_1 - p)} = \frac{s_2^2}{s_1^2} \;\underset{H_0}{\sim}\; F_{n_2 - p, \, n_1 - p}$$

If error variance increases with $X_j$, $s_2^2$ will systematically exceed $s_1^2$, and we reject $H_0$ at significance level $\alpha$ if $F_{\text{GQ}} > F_{\alpha, \, n_2 - p, \, n_1 - p}$.

### 2. The Breusch–Pagan–Godfrey Lagrange Multiplier Test and Koenker–Bassett Studentization

To test whether error variance depends on a vector of $m$ explanatory variables $\mathbf{z}_i = (z_{i1}, \dots, z_{im})^\top$ via any twice-differentiable skedastic function $\sigma_i^2 = h(\alpha_0 + \mathbf{z}_i^\top \boldsymbol{\gamma})$ where $h(\cdot) > 0$ and $h'(\cdot) \neq 0$, Trevor Breusch and Adrian Pagan (1979) and Leslie Godfrey (1978) derived the Lagrange Multiplier (Score) test of $H_0: \boldsymbol{\gamma} = \mathbf{0}$ (since $\boldsymbol{\gamma} = \mathbf{0} \implies \sigma_i^2 = h(\alpha_0) = \sigma^2$).

- **Original Gaussian Breusch–Pagan Test**: Under normal errors $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$, the fourth central moment is $\mathbb{E}[\varepsilon_i^4] = 3\sigma^4$, so the variance of the squared error is $\operatorname{Var}(\varepsilon_i^2) = \mathbb{E}[\varepsilon_i^4] - (\mathbb{E}[\varepsilon_i^2])^2 = 3\sigma^4 - \sigma^4 = 2\sigma^4$, which implies $\operatorname{Var}(\varepsilon_i^2 / \sigma^2) = 2$. Defining the maximum likelihood variance estimate $\hat{\sigma}_{\text{MLE}}^2 = \frac{1}{n}\sum_{i=1}^n e_i^2$ and standardized squared residuals $g_i = e_i^2 / \hat{\sigma}_{\text{MLE}}^2$, the Gaussian score statistic equals one-half the Explained Sum of Squares ($\text{SSR}_{\text{aux}}$) from regressing $g_i$ on $(1, \mathbf{z}_i^\top)$:

$$\text{LM}_{\text{BP-Gaussian}} = \frac{1}{2} \text{SSR}_{\text{aux}} \;\underset{H_0}{\xrightarrow{d}}\; \chi^2_m$$

- **Koenker–Bassett (1982) Studentized Breusch–Pagan Test**: Roger Koenker observed that the divisor $2\sigma^4$ relies critically on Gaussian kurtosis ($\kappa = 3$). If the true errors are heavy-tailed (leptokurtic, $\kappa > 3$), $\operatorname{Var}(\varepsilon_i^2) = (\kappa - 1)\sigma^4 > 2\sigma^4$, causing the original Breusch–Pagan test to reject homoscedasticity far too frequently merely because of non-normality! Replacing the theoretical Gaussian variance $2\sigma^4$ with the consistent empirical variance of the squared residuals $\hat{V} = \frac{1}{n}\sum_{i=1}^n (e_i^2 - \hat{\sigma}_{\text{MLE}}^2)^2$ yields the **Koenker–Bassett studentized LM statistic**, which equals the sample size $n$ multiplied by the unadjusted coefficient of determination $R_{\text{aux}}^2$ from the auxiliary OLS regression of $e_i^2$ on an intercept and $z_{i1}, \dots, z_{im}$:

$$e_i^2 = \delta_0 + \delta_1 z_{i1} + \dots + \delta_m z_{im} + u_i \quad \Longrightarrow \quad \text{LM}_{\text{BP}} = n R_{\text{aux}}^2 \;\underset{H_0}{\xrightarrow{d}}\; \chi^2_m$$

This $n R_{\text{aux}}^2$ formulation is completely robust to non-normal kurtosis and is the standard version implemented in modern statistical software.

### 3. Park (1966) and Glejser (1969) Auxiliary Residual Tests

Two classical precursor tests estimate functional forms directly:
- **Park Test**: Regresses $\ln(e_i^2) = \alpha_0 + \gamma \ln(X_i) + v_i$ and performs a $t$-test on $\hat{\gamma}$.
- **Glejser Test**: Regresses the absolute residuals $|e_i|$ on candidate functional forms of $X_i$, such as $|e_i| = \delta_0 + \delta_1 X_i + u_i$, $|e_i| = \delta_0 + \delta_1 \sqrt{X_i} + u_i$, or $|e_i| = \delta_0 + \delta_1 (1/X_i) + u_i$. This helps identify the specific power-law relationship needed to construct FGLS weights.

### 4. White's General Heteroscedasticity and Specification Test (1980)

Halbert White (1980) recognized that heteroscedasticity compromises OLS inference **only** insofar as the middle matrix $\frac{1}{n}\mathbf{X}^\top \boldsymbol{\Sigma} \mathbf{X} = \frac{1}{n}\sum_{i=1}^n \sigma_i^2 \mathbf{x}_i \mathbf{x}_i^\top$ diverges from $\sigma^2 \left(\frac{1}{n}\sum_{i=1}^n \mathbf{x}_i \mathbf{x}_i^\top\right)$. For the difference between these two $p \times p$ matrices to vanish, $\sigma_i^2$ must be uncorrelated with every unique element of the outer product matrix $\mathbf{x}_i \mathbf{x}_i^\top$—namely, all linear terms $X_{ij}$, all pure quadratic terms $X_{ij}^2$, and all cross-product interaction terms $X_{ij} X_{i\ell}$ ($1 \le j < \ell \le k$).

Accordingly, **White's Test** requires no prior knowledge of which variables drive the variance:
1. Estimate the primary regression by OLS and compute the squared residuals $e_i^2$.
2. Run an auxiliary OLS regression of $e_i^2$ on an intercept, all $k$ original regressors, all $k$ squared regressors, and all $\binom{k}{2} = \frac{k(k-1)}{2}$ pairwise cross-products (omitting any redundant columns, such as the square of a binary $0/1$ dummy variable since $D_i^2 = D_i$):

$$e_i^2 = \delta_0 + \sum_{j=1}^k \delta_j X_{ij} + \sum_{j=1}^k \gamma_{jj} X_{ij}^2 + \sum_{j=1}^{k-1}\sum_{\ell=j+1}^k \gamma_{j\ell} X_{ij} X_{i\ell} + u_i$$

3. With $q$ non-redundant auxiliary regressors (where $q = 2k + \frac{k(k-1)}{2} = \frac{k(k+3)}{2}$ if all $k$ predictors are continuous), compute the White test statistic:

$$W = n R_{\text{White}}^2 \;\underset{H_0}{\xrightarrow{d}}\; \chi^2_q$$

Reject $H_0$ if $W > \chi^2_{\alpha, \, q}$. Note that because $e_i^2$ also captures omitted non-linear terms in $\mathbb{E}[Y_i \mid \mathbf{x}_i]$, a significant White statistic can signal either pure heteroscedasticity or functional form misspecification (omitted quadratic/interaction terms in the mean equation).

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Diagnostic Test</th>
<th>Auxiliary Dependent Variable</th>
<th>Auxiliary Regressors &amp; Degrees of Freedom</th>
<th>Null Distribution &amp; Key Properties</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Goldfeld–Quandt (1965)</strong></td>
<td>Subsample OLS regressions on sorted low/high groups</td>
<td>Original $p$ regressors in each group; omits $c$ middle cases</td>
<td>Exact $F_{n_2 - p, \, n_1 - p}$ under normal errors; requires knowing single monotonic ordering variable $X_j$</td>
</tr>
<tr>
<td><strong>Breusch–Pagan / Koenker (1979, 1982)</strong></td>
<td>Squared OLS residuals $e_i^2$</td>
<td>$m$ suspected variance drivers $\mathbf{z}_i = (z_{i1}, \dots, z_{im})^\top$</td>
<td>Asymptotic $\text{LM} = n R_{\text{aux}}^2 \sim \chi^2_m$; high power against parametric variance models $\sigma_i^2 = h(\alpha_0 + \mathbf{z}_i^\top \boldsymbol{\gamma})$</td>
</tr>
<tr>
<td><strong>Glejser (1969)</strong></td>
<td>Absolute OLS residuals $|e_i|$</td>
<td>Functional transformations $X_i^r$ ($r \in \{1, 1/2, -1\}$)</td>
<td>Asymptotic $t$ or $F$ / $\chi^2$ test; directly guides choice of FGLS power weights</td>
</tr>
<tr>
<td><strong>White's General Test (1980)</strong></td>
<td>Squared OLS residuals $e_i^2$</td>
<td>All linear, squared, and cross-product terms ($q = \frac{k(k+3)}{2}$ for continuous $\mathbf{X}$)</td>
<td>Asymptotic $W = n R_{\text{White}}^2 \sim \chi^2_q$; assumption-free omnibus test, but consumes degrees of freedom rapidly as $k$ grows</td>
</tr>
</tbody>
</table></div>

---

## 5.5 Heteroscedasticity-Consistent (HC0–HC4) Huber–Eicker–White Sandwich Covariance Matrix Estimation

Suppose diagnostic tests reject homoscedasticity, or theoretical considerations dictate that $\sigma_i^2$ varies across observations, yet the true functional form of $\sigma_i^2$ is unknown. Rather than guessing a parametric skedastic model for FGLS (which risks misspecification), we can retain the unbiased and consistent OLS point estimator $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ and construct a **consistent estimator of its true sampling variance** under arbitrary, unknown heteroscedasticity.

Recall the true variance of the scaled OLS estimation error $\sqrt{n}(\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta})$:

$$\operatorname{Var}\left( \sqrt{n}(\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta}) \;\middle|\; \mathbf{X} \right) = \left(\frac{1}{n}\mathbf{X}^\top \mathbf{X}\right)^{-1} \left( \frac{1}{n}\mathbf{X}^\top \boldsymbol{\Sigma} \mathbf{X} \right) \left(\frac{1}{n}\mathbf{X}^\top \mathbf{X}\right)^{-1}$$

Under pure heteroscedasticity, $\boldsymbol{\Sigma} = \operatorname{diag}(\sigma_1^2, \sigma_2^2, \dots, \sigma_n^2)$, so the middle $p \times p$ meat matrix expands as a weighted sum of outer products of the regressor rows $\mathbf{x}_i \in \mathbb{R}^{p \times 1}$:

$$\boldsymbol{\Psi}_n = \frac{1}{n}\mathbf{X}^\top \boldsymbol{\Sigma} \mathbf{X} = \frac{1}{n}\sum_{i=1}^n \sigma_i^2 \mathbf{x}_i \mathbf{x}_i^\top$$

Wait: can we estimate the $n$ unknown individual variances $\sigma_1^2, \dots, \sigma_n^2$ consistently? **No**, because there is only one observation per $\sigma_i^2$. However, the fundamental insight of Friedhelm Eicker (1963), Peter Huber (1967), and Halbert White (1980) is that **we do not need consistent estimates of each individual $\sigma_i^2$; we only need a consistent estimator of the $p \times p$ average matrix $\boldsymbol{\Psi}_n = \frac{1}{n}\sum_{i=1}^n \sigma_i^2 \mathbf{x}_i \mathbf{x}_i^\top$!**

Replacing each unobserved $\sigma_i^2 = \mathbb{E}[\varepsilon_i^2 \mid \mathbf{X}]$ with its empirical counterpart—the squared OLS residual $e_i^2 = (Y_i - \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}_{\text{OLS}})^2$—yields the empirical meat matrix $\hat{\boldsymbol{\Psi}}_n = \frac{1}{n}\sum_{i=1}^n e_i^2 \mathbf{x}_i \mathbf{x}_i^\top$. Because $e_i = \varepsilon_i - \mathbf{x}_i^\top (\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta})$ and $\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta} = O_p(n^{-1/2})$, expanding $e_i^2 = \varepsilon_i^2 - 2\varepsilon_i \mathbf{x}_i^\top (\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta}) + \left[\mathbf{x}_i^\top (\hat{\boldsymbol{\beta}}_{\text{OLS}} - \boldsymbol{\beta})\right]^2$ and applying Markov's Weak Law of Large Numbers for independent non-identically distributed random variables (under bounded fourth moments $\sup_i \mathbb{E}[\varepsilon_i^4] < \infty$ and $\sup_i \|\mathbf{x}_i\|^4 < \infty$) proves that the error averages out across the $n$ summands:

$$\hat{\boldsymbol{\Psi}}_n - \boldsymbol{\Psi}_n = \frac{1}{n}\sum_{i=1}^n \left(e_i^2 - \sigma_i^2\right) \mathbf{x}_i \mathbf{x}_i^\top = \frac{1}{n}\sum_{i=1}^n \left(\varepsilon_i^2 - \sigma_i^2\right) \mathbf{x}_i \mathbf{x}_i^\top + O_p\left(n^{-1/2}\right) \xrightarrow{P} \mathbf{0}_{p \times p}$$

### Finite-Sample Bias Corrections: The HC0, HC1, HC2, HC3, and HC4 Hierarchy

Although White's baseline estimator (**HC0**) is asymptotically consistent, in finite samples the squared OLS residual $e_i^2$ systematically underestimates $\sigma_i^2$ due to leverage shrinkage. Specifically, since $\mathbf{e} = (\mathbf{I}_n - \mathbf{H})\boldsymbol{\varepsilon}$, under homoscedasticity $\mathbb{E}[e_i^2 \mid \mathbf{X}] = (1 - h_{ii})\sigma^2 < \sigma^2$, where $h_{ii} = \mathbf{x}_i^\top (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{x}_i \in [1/n, 1]$ is the $i$-th diagonal of the hat matrix. When an observation has high leverage ($h_{ii}$ close to $1$), the OLS regression line is pulled toward $Y_i$, shrinking $e_i^2$ toward zero and biasing HC0 standard errors downward in small samples. James MacKinnon and Halbert White (1985), Russell Davidson and James MacKinnon (1993), and Francisco Cribari-Neto (2004) developed a hierarchy of leverage-adjusted sandwich estimators of the form:

$$\widehat{\operatorname{Var}}_{\text{HC}k}(\hat{\boldsymbol{\beta}}_{\text{OLS}}) = (\mathbf{X}^\top \mathbf{X})^{-1} \left( \sum_{i=1}^n \hat{v}_i^{(k)} \mathbf{x}_i \mathbf{x}_i^\top \right) (\mathbf{X}^\top \mathbf{X})^{-1} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \hat{\boldsymbol{\Sigma}}_{\text{HC}k} \mathbf{X}(\mathbf{X}^\top \mathbf{X})^{-1}$$

where the diagonal elements $\hat{v}_i^{(k)}$ of $\hat{\boldsymbol{\Sigma}}_{\text{HC}k} = \operatorname{diag}(\hat{v}_1^{(k)}, \dots, \hat{v}_n^{(k)})$ are defined as follows:

1. **HC0 (Baseline White, 1980)**: $\hat{v}_i^{(0)} = e_i^2$. Asymptotically valid, but downwardly biased in finite samples ($n < 250$), especially when high-leverage observations exist.
2. **HC1 (Hinkley, 1977; Default in Stata `robust`)**: $\hat{v}_i^{(1)} = \frac{n}{n - p} e_i^2$. Applies a uniform degrees-of-freedom inflation factor $\frac{n}{n-p}$ (matching $\bar{h} = p/n$), but does not account for heterogeneous individual leverages $h_{ii}$.
3. **HC2 (Horn, Horn, and Duncan, 1975)**: $\hat{v}_i^{(2)} = \frac{e_i^2}{1 - h_{ii}}$. Exactly unbiased for $\sigma^2$ under homoscedasticity since $\mathbb{E}\left[\frac{e_i^2}{1 - h_{ii}}\right] = \frac{(1 - h_{ii})\sigma^2}{1 - h_{ii}} = \sigma^2$.
4. **HC3 (MacKinnon and White, 1985; Jackknife Approximation, Default in R `sandwich`)**: $\hat{v}_i^{(3)} = \frac{e_i^2}{(1 - h_{ii})^2} = e_{(i)}^2$, where $e_{(i)} = \frac{e_i}{1 - h_{ii}}$ is the leave-one-out deletion (PRESS) residual! By squaring the leverage penalty $(1 - h_{ii})^{-2}$, HC3 heavily penalizes high-leverage points and provides superior finite-sample Type I error control.
5. **HC4 (Cribari-Neto, 2004)**: $\hat{v}_i^{(4)} = \frac{e_i^2}{(1 - h_{ii})^{\delta_i}}$, where $\delta_i = \min\left(4, \, \frac{n h_{ii}}{p}\right) = \min\left(4, \, \frac{h_{ii}}{\bar{h}}\right)$ scales the exponent up to $4$ for extreme leverage outliers ($h_{ii} > 2\bar{h}$).

---

## 5.6 Serial Correlation and Autoregressive Disturbances: AR(1) Dynamics, Durbin–Watson $d$-Test, Breusch–Godfrey LM Test, Prais–Winsten, and Cochrane–Orcutt

When regression data are collected sequentially over time ($t = 1, 2, \dots, T$), the disturbance $\varepsilon_t$ represents the cumulative influence of omitted macroeconomic shocks, supply-chain bottlenecks, consumer habit persistence, and measurement conventions that persist across multiple periods. The canonical benchmark model for temporal correlation is the stationary **First-Order Autoregressive Process, AR(1)**:

$$\varepsilon_t = \rho \varepsilon_{t-1} + u_t, \qquad |\rho| < 1, \qquad u_t \;\overset{\text{i.i.d.}}{\sim}\; \left(0, \sigma_u^2\right)$$

where $\rho \in (-1, 1)$ is the first-order autocorrelation coefficient and $u_t$ is a white-noise innovation sequence satisfying $\mathbb{E}[u_t \mid \mathbf{X}] = 0$, $\operatorname{Var}(u_t \mid \mathbf{X}) = \sigma_u^2$, and $\operatorname{Cov}(u_t, u_s \mid \mathbf{X}) = 0$ for $t \neq s$.

### Derivation of the Stationary AR(1) Covariance Matrix $\boldsymbol{\Omega}$ and Its Analytical Inverse $\boldsymbol{\Omega}^{-1}$

By recursive backward substitution under the stationarity condition $|\rho| < 1$, we express $\varepsilon_t$ as an infinite moving-average representation of past white-noise shocks:

$$\varepsilon_t = u_t + \rho u_{t-1} + \rho^2 u_{t-2} + \rho^3 u_{t-3} + \dots = \sum_{j=0}^\infty \rho^j u_{t-j}$$

From this causal expansion, we compute the unconditional mean, variance, and lag-$s$ autocovariance ($s \ge 0$):
- **Mean**: $\mathbb{E}[\varepsilon_t] = \sum_{j=0}^\infty \rho^j \mathbb{E}[u_{t-j}] = 0$.
- **Stationary Variance**: Because the innovations $u_{t-j}$ are mutually uncorrelated, the variance is a convergent geometric series with ratio $\rho^2 < 1$:

$$\sigma_\varepsilon^2 = \operatorname{Var}(\varepsilon_t) = \sum_{j=0}^\infty \left(\rho^j\right)^2 \operatorname{Var}(u_{t-j}) = \sigma_u^2 \sum_{j=0}^\infty \rho^{2j} = \frac{\sigma_u^2}{1 - \rho^2}$$

- **Lag-$s$ Autocovariance and Autocorrelation ($s \ge 1$)**: Multiplying $\varepsilon_t = \rho \varepsilon_{t-1} + u_t = \rho^s \varepsilon_{t-s} + \sum_{j=0}^{s-1} \rho^j u_{t-j}$ by $\varepsilon_{t-s}$ and taking expectations (noting that future innovations $u_{t-j}$ for $j < s$ are uncorrelated with $\varepsilon_{t-s}$) yields:

$$\gamma_s = \operatorname{Cov}(\varepsilon_t, \varepsilon_{t-s}) = \rho^s \operatorname{Var}(\varepsilon_{t-s}) = \sigma_u^2 \frac{\rho^s}{1 - \rho^2} \quad \Longrightarrow \quad \operatorname{Corr}(\varepsilon_t, \varepsilon_{t-s}) = \frac{\gamma_s}{\gamma_0} = \rho^s$$

Setting the scale factor $\sigma^2 = \sigma_u^2$, the $T \times T$ covariance matrix $\operatorname{Var}(\boldsymbol{\varepsilon}) = \sigma_u^2 \boldsymbol{\Omega}$ has Toeplitz autocorrelation structure:

$$\boldsymbol{\Omega} = \frac{1}{1 - \rho^2} \begin{pmatrix} 1 & \rho & \rho^2 & \cdots & \rho^{T-1} \\ \rho & 1 & \rho & \cdots & \rho^{T-2} \\ \rho^2 & \rho & 1 & \cdots & \rho^{T-3} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ \rho^{T-1} & \rho^{T-2} & \rho^{T-3} & \cdots & 1 \end{pmatrix}$$

Remarkably, the inverse of this dense $T \times T$ matrix is an sparse, symmetric **tridiagonal matrix** $\boldsymbol{\Omega}^{-1} = \mathbf{P}^\top \mathbf{P}$, factored via the lower-bidiagonal **Prais–Winsten transformation matrix** $\mathbf{P} \in \mathbb{R}^{T \times T}$:

$$\mathbf{P} = \begin{pmatrix} \sqrt{1 - \rho^2} & 0 & 0 & \cdots & 0 & 0 \\ -\rho & 1 & 0 & \cdots & 0 & 0 \\ 0 & -\rho & 1 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & -\rho & 1 \end{pmatrix}, \qquad \boldsymbol{\Omega}^{-1} = \mathbf{P}^\top \mathbf{P} = \begin{pmatrix} 1 & -\rho & 0 & \cdots & 0 & 0 \\ -\rho & 1+\rho^2 & -\rho & \cdots & 0 & 0 \\ 0 & -\rho & 1+\rho^2 & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 1+\rho^2 & -\rho \\ 0 & 0 & 0 & \cdots & -\rho & 1 \end{pmatrix}$$

Let us verify why $\mathbf{P}\boldsymbol{\varepsilon}$ whitens the disturbance vector:
- For $t = 2, 3, \dots, T$, the $t$-th row of $\mathbf{P}\boldsymbol{\varepsilon}$ computes the quasi-difference $\varepsilon_t^* = \varepsilon_t - \rho \varepsilon_{t-1} = u_t$, which has variance $\sigma_u^2$ and is independent of all other rows!
- For the initial observation $t = 1$, there is no $\varepsilon_0$ in the sample. However, multiplying $\varepsilon_1$ by $\sqrt{1 - \rho^2}$ produces $\varepsilon_1^* = \sqrt{1 - \rho^2}\,\varepsilon_1$, whose variance is $(1 - \rho^2) \operatorname{Var}(\varepsilon_1) = (1 - \rho^2)\frac{\sigma_u^2}{1 - \rho^2} = \sigma_u^2$, and since $u_2, \dots, u_T$ are future innovations independent of $\varepsilon_1$, $\operatorname{Cov}(\varepsilon_1^*, \varepsilon_t^*) = 0$ for all $t \ge 2$!

### Consequences of Positive Autocorrelation ($\rho > 0$) for Naive OLS Standard Errors

In economic time series, both the regressors $X_t$ and the disturbances $\varepsilon_t$ typically display positive autocorrelation ($\rho > 0$ and $\rho_X = \operatorname{Corr}(X_t, X_{t-1}) > 0$). In simple regression $Y_t = \beta_0 + \beta_1 x_t + \varepsilon_t$, the true asymptotic variance of $\hat{\beta}_{1,\text{OLS}}$ is inflated relative to the naive formula $\sigma_\varepsilon^2 / S_{xx}$ by the autocorrelation factor:

$$\operatorname{Var}(\hat{\beta}_{1,\text{OLS}}) = \frac{\sigma_\varepsilon^2}{S_{xx}} \left[ 1 + \frac{2}{S_{xx}} \sum_{t=1}^{T-1}\sum_{s=1}^{T-t} \rho^s (x_t - \bar{x})(x_{t+s} - \bar{x}) \right] \approx \frac{\sigma_\varepsilon^2}{S_{xx}} \left( \frac{1 + \rho \rho_X}{1 - \rho \rho_X} \right)$$

Simultaneously, positive autocorrelation causes successive disturbances to cluster on the same side of the true regression line, allowing the OLS fitted line to track the correlated error drift and artificially depressing the residual variance estimator:

$$\mathbb{E}[s^2] \approx \sigma_\varepsilon^2 \left[ 1 - \frac{2}{T - 2}\left(\frac{1 + \rho \rho_X}{1 - \rho \rho_X}\right) \right] < \sigma_\varepsilon^2$$

Thus, when $\rho > 0$ and $\rho_X > 0$, **naive OLS suffers a double downward bias**: $s^2$ underestimates $\sigma_\varepsilon^2$, while $\sigma_\varepsilon^2 / S_{xx}$ omits the positive multiplier $\frac{1 + \rho \rho_X}{1 - \rho \rho_X} > 1$. For instance, if $\rho = 0.8$ and $\rho_X = 0.8$, the inflation factor is $\frac{1 + 0.64}{1 - 0.64} = \frac{1.64}{0.36} = 4.56$, meaning the true variance is more than $4.5$ times larger than the naive variance, and naive $t$-statistics are exaggerated by more than $\sqrt{4.56} \approx 2.13$-fold!

### Diagnostic Tests for Serial Correlation

1. **The Durbin–Watson $d$-Test (1950, 1951)**: To test $H_0: \rho = 0$ in an AR(1) model with strictly exogenous regressors and an intercept, James Durbin and Geoffrey Watson defined the ratio of the sum of squared first-differences of OLS residuals to the Residual Sum of Squares:

$$d = \frac{\sum_{t=2}^T (e_t - e_{t-1})^2}{\sum_{t=1}^T e_t^2} = \frac{\sum_{t=2}^T e_t^2 + \sum_{t=2}^T e_{t-1}^2 - 2\sum_{t=2}^T e_t e_{t-1}}{\sum_{t=1}^T e_t^2} \approx 2(1 - \hat{\rho})$$

where $\hat{\rho} = \frac{\sum_{t=2}^T e_t e_{t-1}}{\sum_{t=1}^T e_t^2}$ is the sample first-order residual autocorrelation, and the approximation holds because the endpoint terms $(e_1^2 + e_T^2) / \sum_{t=1}^T e_t^2 \to 0$ as $T \to \infty$. Because $-1 \le \hat{\rho} \le 1$, the statistic satisfies $0 \le d \le 4$:
- **Zero autocorrelation ($\hat{\rho} \approx 0$)**: $d \approx 2$.
- **Strong positive autocorrelation ($\hat{\rho} \to +1$)**: $d \to 0$.
- **Strong negative autocorrelation ($\hat{\rho} \to -1$)**: $d \to 4$.

Because $\mathbf{e} = (\mathbf{I}_T - \mathbf{H})\boldsymbol{\varepsilon}$, the exact finite-sample distribution of $d = \frac{\boldsymbol{\varepsilon}^\top (\mathbf{I}_T - \mathbf{H})\mathbf{A}(\mathbf{I}_T - \mathbf{H})\boldsymbol{\varepsilon}}{\boldsymbol{\varepsilon}^\top (\mathbf{I}_T - \mathbf{H})\boldsymbol{\varepsilon}}$ depends on the specific configuration of the design matrix $\mathbf{X}$. However, Durbin and Watson proved that for any design matrix $\mathbf{X}$ with $k$ regressors and an intercept, the exact critical value $d_\alpha$ is bounded between two tabulated universal values $d_L$ (lower bound) and $d_U$ (upper bound):
- If $d < d_L$: Reject $H_0: \rho = 0$ in favor of positive autocorrelation ($H_1: \rho > 0$).
- If $d_L \le d \le d_U$: The test falls in the **Zone of Indecision (Inconclusive Region)**.
- If $d_U < d < 4 - d_U$: Fail to reject $H_0: \rho = 0$ (no evidence of AR(1) autocorrelation).
- If $4 - d_U \le d \le 4 - d_L$: Zone of Indecision for negative autocorrelation.
- If $d > 4 - d_L$: Reject $H_0$ in favor of negative autocorrelation ($H_1: \rho < 0$).

> [!CAUTION]
> **Invalidity of $d$ with Lagged Dependent Variables (Durbin's $h$-Test)**: When $\mathbf{X}$ contains a lagged dependent variable $Y_{t-1}$ (dynamic model $Y_t = \beta_0 + \gamma Y_{t-1} + \mathbf{x}_t^\top \boldsymbol{\beta} + \varepsilon_t$), $Y_{t-1}$ is correlated with $\varepsilon_{t-1}$, biasing $\hat{\rho}$ toward zero and biasing $d$ toward $2$. In this setting, Durbin (1970) proposed **Durbin's $h$-statistic**:
> $$h = \hat{\rho} \sqrt{\frac{T}{1 - T \cdot \widehat{\operatorname{Var}}(\hat{\gamma})}} \;\underset{H_0}{\xrightarrow{d}}\; \mathcal{N}(0, 1)$$
> which is valid provided $T \cdot \widehat{\operatorname{Var}}(\hat{\gamma}) < 1$. Even more generally, the **Breusch–Godfrey test** remains valid regardless of whether $T \cdot \widehat{\operatorname{Var}}(\hat{\gamma}) < 1$.

2. **The Breusch–Godfrey (BG) Lagrange Multiplier Test for $\text{AR}(q)$ or $\text{MA}(q)$ Errors (1978)**: To test $H_0: \rho_1 = \rho_2 = \dots = \rho_q = 0$ in the higher-order autoregressive process $\varepsilon_t = \rho_1 \varepsilon_{t-1} + \dots + \rho_q \varepsilon_{t-q} + u_t$ (even in the presence of lagged dependent variables $Y_{t-1}$), regress the OLS residuals $e_t$ on **both** the original regressors $\mathbf{x}_t$ and the $q$ lagged residuals $e_{t-1}, \dots, e_{t-q}$ (setting initial pre-sample residuals $e_0 = e_{-1} = \dots = 0$):

$$e_t = \mathbf{x}_t^\top \boldsymbol{\delta} + \alpha_1 e_{t-1} + \alpha_2 e_{t-2} + \dots + \alpha_q e_{t-q} + v_t$$

Including the original regressors $\mathbf{x}_t$ in this auxiliary regression accounts for the non-orthogonality between $\mathbf{x}_t$ and the lagged residuals (which is essential when $\mathbf{x}_t$ includes $Y_{t-1}$). The Breusch–Godfrey LM statistic is:

$$\text{LM}_{\text{BG}} = (T - q) R_{\text{aux}}^2 \;\underset{H_0}{\xrightarrow{d}}\; \chi^2_q$$

### Corrective Estimation: Cochrane–Orcutt vs. Prais–Winsten FGLS and Newey–West HAC

When AR(1) serial correlation is confirmed, two classical FGLS procedures transform the model using $\hat{\rho} = \frac{\sum_{t=2}^T e_t e_{t-1}}{\sum_{t=1}^{T-1} e_t^2}$:
1. **Cochrane–Orcutt (1949) Two-Step / Iterative Procedure**: Drops the initial observation $t = 1$ and applies OLS to the $T - 1$ quasi-differenced observations ($t = 2, \dots, T$):

$$Y_t - \hat{\rho} Y_{t-1} = \beta_0(1 - \hat{\rho}) + \beta_1(X_{t1} - \hat{\rho} X_{t-1,1}) + \dots + \beta_k(X_{tk} - \hat{\rho} X_{t-1,k}) + u_t$$

Note that the intercept estimated in the quasi-differenced regression is $\hat{\beta}_0^* = \widehat{\beta_0(1 - \rho)}$, so the original intercept is recovered via $\hat{\beta}_0 = \hat{\beta}_0^* / (1 - \hat{\rho})$. In iterative Cochrane–Orcutt, the updated parameter vector $\hat{\boldsymbol{\beta}}$ is used to recompute structural residuals $\tilde{e}_t = Y_t - \mathbf{x}_t^\top \hat{\boldsymbol{\beta}}$, update $\hat{\rho}$, and re-estimate until convergence.
2. **Prais–Winsten (1954) Full-Sample FGLS**: Retaining only $T - 1$ observations in Cochrane–Orcutt discards the initial state $t = 1$, which causes severe finite-sample efficiency loss when $T$ is small or when $X_t$ exhibits a strong trend. Prais and Winsten retain $t = 1$ by applying the first row of $\mathbf{P}$:

$$\sqrt{1 - \hat{\rho}^2}\,Y_1 = \beta_0 \sqrt{1 - \hat{\rho}^2} + \beta_1 \sqrt{1 - \hat{\rho}^2}\,X_{11} + \dots + \beta_k \sqrt{1 - \hat{\rho}^2}\,X_{1k} + \varepsilon_1^*$$

Combining this scaled $t = 1$ equation with the $T - 1$ quasi-differenced equations ($t = 2, \dots, T$) executes exact FGLS across all $T$ observations.
3. **Newey–West (1987) Heteroscedasticity and Autocorrelation Consistent (HAC) Standard Errors**: When the exact ARMA order is unknown, Whitney Newey and Kenneth West generalized White's sandwich estimator to time series by including Bartlett-weighted sample autocovariance matrices up to truncation lag $L$ (typically $L = \lfloor 4(T/100)^{2/9} \rfloor$):

$$\hat{\boldsymbol{\Psi}}_{\text{NW}} = \frac{1}{T}\sum_{t=1}^T e_t^2 \mathbf{x}_t \mathbf{x}_t^\top + \frac{1}{T}\sum_{\ell=1}^L \left(1 - \frac{\ell}{L + 1}\right) \sum_{t=\ell+1}^T e_t e_{t-\ell} \left(\mathbf{x}_t \mathbf{x}_{t-\ell}^\top + \mathbf{x}_{t-\ell}\mathbf{x}_t^\top\right)$$

The linear Bartlett kernel weights $w(\ell, L) = 1 - \frac{\ell}{L+1}$ guarantee that $\hat{\boldsymbol{\Psi}}_{\text{NW}}$ is strictly positive semi-definite in every finite sample while converging in probability to $\lim_{T \to \infty} \frac{1}{T}\mathbf{X}^\top \boldsymbol{\Sigma} \mathbf{X}$.

---

## Worked Questions and Solutions

### Question 1: Exact Efficiency Loss of OLS Relative to WLS and HC0 vs. Naive Standard Errors Under Power-Law Heteroscedasticity

Consider a regression through the origin $Y_i = \beta x_i + \varepsilon_i$ for $n = 4$ independent observations with fixed non-stochastic design points $x_1 = 1$, $x_2 = 2$, $x_3 = 3$, and $x_4 = 4$. The observed response values are $Y_1 = 2.5$, $Y_2 = 3.8$, $Y_3 = 7.2$, and $Y_4 = 7.5$. Suppose the disturbances satisfy $\mathbb{E}[\varepsilon_i] = 0$ and $\operatorname{Cov}(\varepsilon_i, \varepsilon_j) = 0$ for $i \neq j$, but exhibit proportional power-law heteroscedasticity $\operatorname{Var}(\varepsilon_i) = \sigma^2 x_i^2$, so that $\omega_i = x_i^2$.
1. Derive the symbolic formulas and compute the numerical estimates for both the Ordinary Least Squares estimator $\hat{\beta}_{\text{OLS}}$ and the Weighted Least Squares estimator $\hat{\beta}_{\text{WLS}}$.
2. Calculate the exact theoretical variances $\operatorname{Var}(\hat{\beta}_{\text{OLS}})$ and $\operatorname{Var}(\hat{\beta}_{\text{WLS}})$ as multiples of $\sigma^2$, and determine the exact finite-sample relative efficiency $\operatorname{Eff}(\hat{\beta}_{\text{OLS}}) = \operatorname{Var}(\hat{\beta}_{\text{WLS}}) / \operatorname{Var}(\hat{\beta}_{\text{OLS}})$.
3. Using the OLS residuals $e_i = Y_i - \hat{\beta}_{\text{OLS}} x_i$, compute the naive OLS variance estimate $\widehat{\operatorname{Var}}_{\text{naive}}(\hat{\beta}_{\text{OLS}})$, the White HC0 variance estimate $\widehat{\operatorname{Var}}_{\text{HC0}}(\hat{\beta}_{\text{OLS}})$, and the leverage-adjusted HC2 and HC3 variance estimates.

### Solution, step 1: Derivation and Numerical Computation of $\hat{\beta}_{\text{OLS}}$ and $\hat{\beta}_{\text{WLS}}$

In the one-parameter regression through the origin $\mathbf{Y} = \mathbf{x}\beta + \boldsymbol{\varepsilon}$ with $\mathbf{x} = (1, 2, 3, 4)^\top$ and $\mathbf{Y} = (2.5, 3.8, 7.2, 7.5)^\top$, the Ordinary Least Squares estimator minimizes $\sum_{i=1}^4 (Y_i - \beta x_i)^2$, yielding:

$$\hat{\beta}_{\text{OLS}} = \frac{\sum_{i=1}^4 x_i Y_i}{\sum_{i=1}^4 x_i^2}$$

Evaluating the required sample sums from the four observations:
- $\sum_{i=1}^4 x_i^2 = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30$
- $\sum_{i=1}^4 x_i Y_i = (1)(2.5) + (2)(3.8) + (3)(7.2) + (4)(7.5) = 2.5 + 7.6 + 21.6 + 30.0 = 61.7$

Thus, the OLS point estimate is:

$$\hat{\beta}_{\text{OLS}} = \frac{61.7}{30} \approx 2.0567$$

For Weighted Least Squares under $\operatorname{Var}(\varepsilon_i) = \sigma^2 \omega_i = \sigma^2 x_i^2$, the optimal weights are inversely proportional to the error variances: $w_i = \frac{1}{\omega_i} = \frac{1}{x_i^2}$. Equivalently, dividing the structural equation $Y_i = \beta x_i + \varepsilon_i$ by $\sqrt{\omega_i} = x_i$ yields the homoscedastic transformed equation:

$$\frac{Y_i}{x_i} = \beta(1) + \frac{\varepsilon_i}{x_i}, \qquad \operatorname{Var}\left(\frac{\varepsilon_i}{x_i}\right) = \frac{\sigma^2 x_i^2}{x_i^2} = \sigma^2$$

Minimizing $\sum_{i=1}^4 w_i (Y_i - \beta x_i)^2 = \sum_{i=1}^4 \frac{1}{x_i^2}(Y_i - \beta x_i)^2$ produces the WLS estimator, which is simply the sample mean of the individual ratios $Y_i / x_i$:

$$\hat{\beta}_{\text{WLS}} = \frac{\sum_{i=1}^4 w_i x_i Y_i}{\sum_{i=1}^4 w_i x_i^2} = \frac{\sum_{i=1}^4 \frac{1}{x_i^2} x_i Y_i}{\sum_{i=1}^4 \frac{1}{x_i^2} x_i^2} = \frac{\sum_{i=1}^4 (Y_i / x_i)}{\sum_{i=1}^4 1} = \frac{1}{n}\sum_{i=1}^n \frac{Y_i}{x_i}$$

Computing the four individual ratios $Y_i / x_i$:
- $Y_1 / x_1 = 2.5 / 1 = 2.50$
- $Y_2 / x_2 = 3.8 / 2 = 1.90$
- $Y_3 / x_3 = 7.2 / 3 = 2.40$
- $Y_4 / x_4 = 7.5 / 4 = 1.875$

Summing these ratios gives $\sum_{i=1}^4 (Y_i / x_i) = 2.50 + 1.90 + 2.40 + 1.875 = 8.675$, so:

$$\hat{\beta}_{\text{WLS}} = \frac{8.675}{4} = 2.16875 \approx 2.1688$$

Notice how OLS ($\hat{\beta}_{\text{OLS}} = 2.0567$) is pulled downward toward the fourth observation ($Y_4 / x_4 = 1.875$) because OLS weights the $i$-th ratio $Y_i / x_i$ by $x_i^2 / \sum x_j^2 = 16/30 = 53.3\%$, placing over half of its total weight on the single most volatile observation ($x_4 = 4$, where $\operatorname{Var}(\varepsilon_4) = 16\sigma^2$)!

### Solution, step 2: Exact Theoretical Variances and Relative Efficiency of OLS vs. WLS

We evaluate the exact true sampling variance of $\hat{\beta}_{\text{OLS}} = \frac{\sum_{i=1}^4 x_i Y_i}{\sum_{i=1}^4 x_i^2}$ under $\operatorname{Var}(Y_i) = \sigma^2 x_i^2$:

$$\operatorname{Var}(\hat{\beta}_{\text{OLS}}) = \frac{\sum_{i=1}^4 x_i^2 \operatorname{Var}(\varepsilon_i)}{\left(\sum_{i=1}^4 x_i^2\right)^2} = \frac{\sum_{i=1}^4 x_i^2 (\sigma^2 x_i^2)}{\left(\sum_{i=1}^4 x_i^2\right)^2} = \sigma^2 \frac{\sum_{i=1}^4 x_i^4}{\left(\sum_{i=1}^4 x_i^2\right)^2}$$

Computing the fourth-power sum $\sum_{i=1}^4 x_i^4 = 1^4 + 2^4 + 3^4 + 4^4 = 1 + 16 + 81 + 256 = 354$, we obtain:

$$\operatorname{Var}(\hat{\beta}_{\text{OLS}}) = \sigma^2 \frac{354}{30^2} = \sigma^2 \frac{354}{900} = \frac{59}{150}\sigma^2 \approx 0.3933\,\sigma^2$$

In contrast, the exact variance of the BLUE estimator $\hat{\beta}_{\text{WLS}} = \frac{1}{4}\sum_{i=1}^4 \frac{Y_i}{x_i}$ is:

$$\operatorname{Var}(\hat{\beta}_{\text{WLS}}) = \frac{\sigma^2}{\sum_{i=1}^4 w_i x_i^2} = \frac{\sigma^2}{4} = 0.2500\,\sigma^2$$

Therefore, the finite-sample relative efficiency of Ordinary Least Squares compared to Weighted Least Squares is:

$$\operatorname{Eff}(\hat{\beta}_{\text{OLS}}) = \frac{\operatorname{Var}(\hat{\beta}_{\text{WLS}})}{\operatorname{Var}(\hat{\beta}_{\text{OLS}})} = \frac{0.2500\,\sigma^2}{(59/150)\sigma^2} = \frac{37.5}{59} = \frac{75}{118} \approx 0.6356 \quad (63.56\%)$$

Even with only $n = 4$ observations, OLS loses $36.44\%$ of the precision achieved by WLS, because its variance is inflated by a factor of $118/75 \approx 1.5733$.

### Solution, step 3: Naive, HC0, HC2, and HC3 Covariance and Standard Error Calculations

Let us compute the fitted values $\hat{Y}_i = \hat{\beta}_{\text{OLS}} x_i = \frac{61.7}{30} x_i$, the OLS residuals $e_i = Y_i - \hat{Y}_i$, and the hat matrix diagonals $h_{ii} = \frac{x_i^2}{\sum_{j=1}^4 x_j^2} = \frac{x_i^2}{30}$ (noting that $\sum_{i=1}^4 h_{ii} = p = 1$):
- $i = 1$ ($x_1 = 1$): $\hat{Y}_1 = 2.0567$, $e_1 = 2.5 - 2.0567 = +0.4433$, $e_1^2 = 0.1965$, $h_{11} = 1/30 = 0.0333$, $1 - h_{11} = 29/30 = 0.9667$.
- $i = 2$ ($x_2 = 2$): $\hat{Y}_2 = 4.1133$, $e_2 = 3.8 - 4.1133 = -0.3133$, $e_2^2 = 0.0982$, $h_{22} = 4/30 = 0.1333$, $1 - h_{22} = 26/30 = 0.8667$.
- $i = 3$ ($x_3 = 3$): $\hat{Y}_3 = 6.1700$, $e_3 = 7.2 - 6.1700 = +1.0300$, $e_3^2 = 1.0609$, $h_{33} = 9/30 = 0.3000$, $1 - h_{33} = 21/30 = 0.7000$.
- $i = 4$ ($x_4 = 4$): $\hat{Y}_4 = 8.2267$, $e_4 = 7.5 - 8.2267 = -0.7267$, $e_4^2 = 0.5280$, $h_{44} = 16/30 = 0.5333$, $1 - h_{44} = 14/30 = 0.4667$.

Now we evaluate the four variance estimators of $\hat{\beta}_{\text{OLS}}$, all of which share the outer "bread" factor $(\mathbf{X}^\top \mathbf{X})^{-1} = \frac{1}{\sum x_i^2} = \frac{1}{30}$:
1. **Naive OLS Variance Estimator** ($n - p = 4 - 1 = 3$ degrees of freedom):

$$\text{SSE} = \sum_{i=1}^4 e_i^2 = 0.1965 + 0.0982 + 1.0609 + 0.5280 = 1.8837, \qquad s^2 = \frac{1.8837}{3} = 0.6279$$

$$\widehat{\operatorname{Var}}_{\text{naive}}(\hat{\beta}_{\text{OLS}}) = \frac{s^2}{\sum_{i=1}^4 x_i^2} = \frac{0.6279}{30} = 0.02093 \quad \Longrightarrow \quad \operatorname{SE}_{\text{naive}}(\hat{\beta}_{\text{OLS}}) = \sqrt{0.02093} = 0.1447$$

2. **HC0 (Baseline White Sandwich Estimator)**:

$$\sum_{i=1}^4 x_i^2 e_i^2 = (1)(0.1965) + (4)(0.0982) + (9)(1.0609) + (16)(0.5280) = 0.1965 + 0.3927 + 9.5481 + 8.4487 = 18.5860$$

$$\widehat{\operatorname{Var}}_{\text{HC0}}(\hat{\beta}_{\text{OLS}}) = \frac{\sum_{i=1}^4 x_i^2 e_i^2}{\left(\sum_{i=1}^4 x_i^2\right)^2} = \frac{18.5860}{900} = 0.02065 \quad \Longrightarrow \quad \operatorname{SE}_{\text{HC0}}(\hat{\beta}_{\text{OLS}}) = 0.1437$$

Notice why HC0 is slightly smaller than the naive variance here: observation $i = 4$ has an enormous leverage of $h_{44} = 0.5333$, which shrinks $e_4^2$ by a factor of $(1 - h_{44}) = 0.4667$!
3. **HC2 (Leverage-Unbiased Sandwich Estimator)**: Dividing each $x_i^2 e_i^2$ by $1 - h_{ii}$:

$$\sum_{i=1}^4 \frac{x_i^2 e_i^2}{1 - h_{ii}} = \frac{0.1965}{0.9667} + \frac{0.3927}{0.8667} + \frac{9.5481}{0.7000} + \frac{8.4487}{0.4667} = 0.2033 + 0.4531 + 13.6401 + 18.1044 = 32.4009$$

$$\widehat{\operatorname{Var}}_{\text{HC2}}(\hat{\beta}_{\text{OLS}}) = \frac{32.4009}{900} = 0.03600 \quad \Longrightarrow \quad \operatorname{SE}_{\text{HC2}}(\hat{\beta}_{\text{OLS}}) = \sqrt{0.03600} = 0.1897$$

4. **HC3 (Jackknife / PRESS Sandwich Estimator)**: Dividing each $x_i^2 e_i^2$ by $(1 - h_{ii})^2$:

$$\sum_{i=1}^4 \frac{x_i^2 e_i^2}{(1 - h_{ii})^2} = \frac{0.1965}{0.9667^2} + \frac{0.3927}{0.8667^2} + \frac{9.5481}{0.7000^2} + \frac{8.4487}{0.4667^2} = 0.2103 + 0.5228 + 19.4859 + 38.7951 = 59.0141$$

$$\widehat{\operatorname{Var}}_{\text{HC3}}(\hat{\beta}_{\text{OLS}}) = \frac{59.0141}{900} = 0.06557 \quad \Longrightarrow \quad \operatorname{SE}_{\text{HC3}}(\hat{\beta}_{\text{OLS}}) = \sqrt{0.06557} = 0.2561$$

Comparing $\operatorname{SE}_{\text{HC3}} = 0.2561$ and $\operatorname{SE}_{\text{HC2}} = 0.1897$ against $\operatorname{SE}_{\text{naive}} = 0.1447$ and $\operatorname{SE}_{\text{HC0}} = 0.1437$ vividly demonstrates why HC2 and HC3 are essential when high-leverage points ($h_{44} = 0.5333$) coincide with high error variance.

---

### Question 2: Breusch–Pagan LM Test, White's General Test, and Log-Linear Variance Function FGLS Estimation

An econometrician estimates a cross-sectional household food expenditure equation $Y_i = \beta_0 + \beta_1 X_{i1} + \beta_2 X_{i2} + \varepsilon_i$ across $n = 120$ households, where $Y_i$ is weekly food expenditure, $X_{i1}$ is disposable household income, and $X_{i2}$ is household family size.
- From the primary OLS regression, the residual sum of squares is $\text{SSE} = 480.0$.
- To test for heteroscedasticity, the econometrician runs three auxiliary regressions on the $n = 120$ observations:
  - **Auxiliary Regression A (Koenker–Bassett Breusch–Pagan)**: Regressing $e_i^2$ on $(1, X_{i1}, X_{i2})$ yields a total sum of squares $\text{SST}_{\text{aux}} = 2{,}400.0$ and an explained regression sum of squares $\text{SSR}_{\text{aux}, A} = 312.0$.
  - **Auxiliary Regression B (White's General Test)**: Regressing $e_i^2$ on $(1, X_{i1}, X_{i2}, X_{i1}^2, X_{i2}^2, X_{i1}X_{i2})$ yields $\text{SSR}_{\text{aux}, B} = 444.0$ (with the same $\text{SST}_{\text{aux}} = 2{,}400.0$).
  - **Auxiliary Regression C (Multiplicative Exponential Skedastic Model)**: Regressing $\ln(e_i^2)$ on $(1, \ln X_{i1}, \ln X_{i2})$ yields $\widehat{\ln(e_i^2)} = -1.20 + 1.60 \ln(X_{i1}) + 0.50 \ln(X_{i2})$.

1. Perform the Koenker–Bassett studentized Breusch–Pagan LM test at the $\alpha = 0.05$ significance level ($\chi^2_{0.05, 2} = 5.991$, $\chi^2_{0.01, 2} = 9.210$). Also compute the classical Gaussian Breusch–Pagan statistic and compare them.
2. Perform White's general heteroscedasticity test at $\alpha = 0.05$ ($\chi^2_{0.05, 5} = 11.070$, $\chi^2_{0.01, 5} = 15.086$).
3. Using Auxiliary Regression C, formulate the exact transformation of $(Y_i, 1, X_{i1}, X_{i2})$ required to compute the two-step Feasible Generalized Least Squares (FGLS) estimator $\hat{\boldsymbol{\beta}}_{\text{FGLS}}$, and evaluate the exact transformed row for a household with $Y_i = 90$, $X_{i1} = 16$, and $X_{i2} = 4$.

### Solution, step 1: Studentized vs. Gaussian Breusch–Pagan Lagrange Multiplier Test

In Auxiliary Regression A, the squared OLS residual $e_i^2$ is regressed on $m = 2$ explanatory variables ($X_{i1}$ and $X_{i2}$) plus an intercept across $n = 120$ observations. The auxiliary coefficient of determination is:

$$R_{\text{aux}, A}^2 = \frac{\text{SSR}_{\text{aux}, A}}{\text{SST}_{\text{aux}}} = \frac{312.0}{2{,}400.0} = 0.1300$$

Under $H_0: \gamma_1 = \gamma_2 = 0$ (homoscedasticity), the Koenker–Bassett studentized Breusch–Pagan statistic is:

$$\text{LM}_{\text{BP}} = n R_{\text{aux}, A}^2 = 120 \times 0.1300 = 15.60$$

Since $15.60 > \chi^2_{0.05, 2} = 5.991$ (and indeed $15.60 > \chi^2_{0.01, 2} = 9.210$, with $p\text{-value} = e^{-15.60/2} = e^{-7.80} \approx 0.00041$), we strongly reject the null hypothesis of homoscedasticity at both the $5\%$ and $1\%$ levels.

To compare with the classical Gaussian Breusch–Pagan statistic, note that the maximum likelihood error variance estimate is $\hat{\sigma}_{\text{MLE}}^2 = \frac{\text{SSE}}{n} = \frac{480.0}{120} = 4.0$. Because the Gaussian test scales $e_i^2$ by $\hat{\sigma}_{\text{MLE}}^2 = 4.0$, the explained sum of squares of $g_i = e_i^2 / \hat{\sigma}_{\text{MLE}}^2$ is $\text{SSR}_g = \frac{\text{SSR}_{\text{aux}, A}}{(\hat{\sigma}_{\text{MLE}}^2)^2} = \frac{312.0}{4.0^2} = \frac{312.0}{16.0} = 19.50$. Thus:

$$\text{LM}_{\text{BP-Gaussian}} = \frac{1}{2}\text{SSR}_g = \frac{19.50}{2} = 9.75$$

Notice why the two statistics differ: the empirical variance of $e_i^2$ is $\frac{\text{SST}_{\text{aux}}}{n} = \frac{2{,}400.0}{120} = 20.0$, whereas the Gaussian formula assumes $\operatorname{Var}(e_i^2) = 2\hat{\sigma}_{\text{MLE}}^4 = 2(16.0) = 32.0$. Both versions reject $H_0$ at the $1\%$ level, confirming substantial heteroscedasticity driven by income and family size.

### Solution, step 2: White's General Heteroscedasticity Test

In Auxiliary Regression B, the $q = 5$ auxiliary regressors are the two linear terms ($X_{i1}, X_{i2}$), the two pure quadratic terms ($X_{i1}^2, X_{i2}^2$), and the interaction term ($X_{i1}X_{i2}$), matching $q = \frac{k(k+3)}{2} = \frac{2(5)}{2} = 5$ degrees of freedom. The auxiliary $R^2$ is:

$$R_{\text{White}}^2 = \frac{\text{SSR}_{\text{aux}, B}}{\text{SST}_{\text{aux}}} = \frac{444.0}{2{,}400.0} = 0.1850$$

Computing White's omnibus statistic for $n = 120$:

$$W = n R_{\text{White}}^2 = 120 \times 0.1850 = 22.20$$

Comparing $W = 22.20$ to the critical values $\chi^2_{0.05, 5} = 11.070$ and $\chi^2_{0.01, 5} = 15.086$, we find $22.20 > 15.086$ ($p\text{-value} \approx 0.00048$). We decisively reject homoscedasticity. Moreover, the incremental increase in auxiliary $R^2$ from $0.1300$ to $0.1850$ across the $3$ quadratic/interaction terms yields an incremental LM statistic of $120(0.1850 - 0.1300) = 6.60$, indicating non-linear variance scaling.

### Solution, step 3: FGLS Skedastic Weighting and Numerical Row Transformation

Auxiliary Regression C estimates the log-linear skedastic relationship:

$$\widehat{\ln(\sigma_i^2)} = -1.20 + 1.60 \ln(X_{i1}) + 0.50 \ln(X_{i2})$$

Exponentiating both sides yields the multiplicative power-law variance function:

$$\hat{\sigma}_i^2 = e^{-1.20} X_{i1}^{1.60} X_{i2}^{0.50} = \hat{\sigma}^2 \hat{\omega}_i, \qquad \text{where } \hat{\omega}_i = X_{i1}^{1.60} X_{i2}^{0.50}$$

Taking the square root gives the estimated relative error standard deviation $\sqrt{\hat{\omega}_i}$ and the FGLS weight $w_i = 1/\hat{\omega}_i$:

$$\sqrt{\hat{\omega}_i} = X_{i1}^{0.80} X_{i2}^{0.25}, \qquad w_i = \frac{1}{\hat{\omega}_i} = X_{i1}^{-1.60} X_{i2}^{-0.50}$$

To obtain $\hat{\boldsymbol{\beta}}_{\text{FGLS}} = (\mathbf{X}^\top \hat{\boldsymbol{\Omega}}^{-1}\mathbf{X})^{-1}\mathbf{X}^\top \hat{\boldsymbol{\Omega}}^{-1}\mathbf{Y}$ via Ordinary Least Squares on transformed variables, we divide every element of the $i$-th equation by $\sqrt{\hat{\omega}_i} = X_{i1}^{0.80} X_{i2}^{0.25}$:

$$Y_i^* = \frac{Y_i}{X_{i1}^{0.80} X_{i2}^{0.25}} = \beta_0 \left(\frac{1}{X_{i1}^{0.80} X_{i2}^{0.25}}\right) + \beta_1 \left(\frac{X_{i1}^{0.20}}{X_{i2}^{0.25}}\right) + \beta_2 \left(\frac{X_{i2}^{0.75}}{X_{i1}^{0.80}}\right) + \varepsilon_i^*$$

For the specific household with $Y_i = 90$, $X_{i1} = 16$, and $X_{i2} = 4$, note that $16 = 2^4$ and $4 = 2^2$:
- $\sqrt{\hat{\omega}_i} = 16^{0.80} \times 4^{0.25} = (2^4)^{0.80} \times (2^2)^{0.25} = 2^{3.2} \times 2^{0.5} = 2^{3.7} \approx 12.9960$
- Transformed response: $Y_i^* = 90 / 12.9960 \approx 6.9252$
- Transformed intercept column: $X_{i0}^* = 1 / 12.9960 \approx 0.07695$
- Transformed income regressor: $X_{i1}^* = 16 / 12.9960 \approx 1.2311$
- Transformed family size regressor: $X_{i2}^* = 4 / 12.9960 \approx 0.3078$

---

### Question 3: First-Order Autoregressive Disturbances, Durbin–Watson Bounds Test, and Prais–Winsten vs. Cochrane–Orcutt Transformation

A macroeconomic time-series regression $Y_t = \beta_0 + \beta_1 X_t + \varepsilon_t$ with $\varepsilon_t = \rho \varepsilon_{t-1} + u_t$ is estimated by OLS over $T = 25$ quarterly observations ($k = 1$ explanatory variable plus an intercept).
- The OLS residuals satisfy $\sum_{t=1}^{25} e_t^2 = 50.0$, $\sum_{t=2}^{25} (e_t - e_{t-1})^2 = 24.0$, and $\sum_{t=2}^{25} e_t e_{t-1} = 25.0$ (with $e_1^2 = 1.2$ and $e_{25}^2 = 0.8$).
- The first three observations of the dataset are $(X_1, Y_1) = (10, 22)$, $(X_2, Y_2) = (12, 26)$, and $(X_3, Y_3) = (15, 31)$.

1. Compute the Durbin–Watson $d$-statistic and the sample first-order autocorrelation coefficient $\hat{\rho} = \frac{\sum_{t=2}^{25} e_t e_{t-1}}{\sum_{t=1}^{25} e_t^2}$, verify the exact algebraic relationship linking $d$, $\hat{\rho}$, $e_1^2$, and $e_{25}^2$, and test $H_0: \rho = 0$ against $H_1: \rho > 0$ at $\alpha = 0.05$ given tabulated Durbin–Watson bounds $d_L = 1.29$ and $d_U = 1.45$ for $(T = 25, k = 1)$.
2. Using $\hat{\rho}$, construct the exact transformed regression rows $(Y_t^*, X_{t0}^*, X_{t1}^*)$ for $t = 1, 2, 3$ under both the **Cochrane–Orcutt** transformation and the **Prais–Winsten** transformation.
3. Calculate the theoretical percentage efficiency loss of OLS relative to exact GLS in estimating the slope $\beta_1$ when $X_t$ itself follows an AR(1) process with $\rho_X = 0.6$ and the error autocorrelation is $\rho = 0.5$, using the asymptotic variance formula $\operatorname{AVar}(\hat{\beta}_{1,\text{OLS}}) = \frac{\sigma_\varepsilon^2}{S_{xx}}\left(\frac{1 + \rho\rho_X}{1 - \rho\rho_X}\right)$ and $\operatorname{AVar}(\hat{\beta}_{1,\text{GLS}}) = \frac{\sigma_u^2}{S_{xx}(1 + \rho^2 - 2\rho\rho_X)}$.

### Solution, step 1: Durbin–Watson $d$-Statistic, Exact End-Point Identity, and Hypothesis Test

Directly applying the definition of the Durbin–Watson statistic and the sample autocorrelation coefficient:

$$d = \frac{\sum_{t=2}^{25} (e_t - e_{t-1})^2}{\sum_{t=1}^{25} e_t^2} = \frac{24.0}{50.0} = 0.4800, \qquad \hat{\rho} = \frac{\sum_{t=2}^{25} e_t e_{t-1}}{\sum_{t=1}^{25} e_t^2} = \frac{25.0}{50.0} = 0.5000$$

To verify the exact algebraic identity between $d$ and $\hat{\rho}$, expand the numerator of $d$:

$$\sum_{t=2}^T (e_t - e_{t-1})^2 = \sum_{t=2}^T e_t^2 + \sum_{t=1}^{T-1} e_t^2 - 2\sum_{t=2}^T e_t e_{t-1} = 2\sum_{t=1}^T e_t^2 - (e_1^2 + e_T^2) - 2\sum_{t=2}^T e_t e_{t-1}$$

Dividing through by $\sum_{t=1}^T e_t^2 = 50.0$ gives:

$$d = 2(1 - \hat{\rho}) - \frac{e_1^2 + e_{25}^2}{\sum_{t=1}^{25} e_t^2} = 2(1 - 0.5000) - \frac{1.2 + 0.8}{50.0} = 1.0000 - \frac{2.0}{50.0} = 1.0000 - 0.0400 = 0.9600 \quad \text{(if } \sum_{t=2}^{25}(e_t - e_{t-1})^2 = 48.0\text{)}$$

Wait: let us check why the problem statement reported $\sum_{t=2}^{25}(e_t - e_{t-1})^2 = 24.0$ while $\sum_{t=2}^{25} e_t e_{t-1} = 25.0$: if $\sum_{t=2}^{25}(e_t - e_{t-1})^2 = 24.0$ and $e_1^2 + e_{25}^2 = 2.0$, then $\sum_{t=2}^{25} e_t e_{t-1} = \frac{2(50.0) - 2.0 - 24.0}{2} = \frac{74.0}{2} = 37.0$ (so $\hat{\rho}_{\text{exact}} = 37.0/50.0 = 0.74$), whereas using the given value $\hat{\rho} = 0.50$ corresponds to $d \approx 2(1 - 0.50) = 1.00$. Under either $d = 0.48$ or $d = 0.96$, the test statistic lies strictly below the lower critical bound $d_L = 1.29$:

$$d < d_L = 1.29$$

Therefore, we **reject the null hypothesis $H_0: \rho = 0$** at the $\alpha = 0.05$ level and conclude that the disturbances exhibit statistically significant positive first-order autocorrelation.

### Solution, step 2: Cochrane–Orcutt vs. Prais–Winsten Transformed Rows for $t = 1, 2, 3$

Using $\hat{\rho} = 0.50$, we construct the transformed response $Y_t^*$, transformed intercept regressor $X_{t0}^*$, and transformed slope regressor $X_{t1}^*$:

- **Under Cochrane–Orcutt**: Observation $t = 1$ is discarded entirely. For $t \ge 2$, $Y_t^* = Y_t - \hat{\rho} Y_{t-1}$, $X_{t0}^* = 1 - \hat{\rho} = 0.50$, and $X_{t1}^* = X_t - \hat{\rho} X_{t-1}$:
  - $t = 1$: **Omitted**
  - $t = 2$: $Y_2^* = 26 - 0.50(22) = 15.0$, $X_{20}^* = 1 - 0.50 = 0.50$, $X_{21}^* = 12 - 0.50(10) = 7.0$
  - $t = 3$: $Y_3^* = 31 - 0.50(26) = 18.0$, $X_{30}^* = 1 - 0.50 = 0.50$, $X_{31}^* = 15 - 0.50(12) = 9.0$

- **Under Prais–Winsten**: Observation $t = 1$ is retained and scaled by $\sqrt{1 - \hat{\rho}^2} = \sqrt{1 - 0.25} = \sqrt{0.75} = \frac{\sqrt{3}}{2} \approx 0.8660$, while $t \ge 2$ are identical to Cochrane–Orcutt:
  - $t = 1$: $Y_1^* = 0.8660(22) = 19.0526$, $X_{10}^* = 0.8660(1) = 0.8660$, $X_{11}^* = 0.8660(10) = 8.6603$
  - $t = 2$: $Y_2^* = 15.0000$, $X_{20}^* = 0.5000$, $X_{21}^* = 7.0000$
  - $t = 3$: $Y_3^* = 18.0000$, $X_{30}^* = 0.5000$, $X_{31}^* = 9.0000$

### Solution, step 3: Asymptotic Efficiency Loss of OLS Relative to GLS Under AR(1) Errors

Given $\rho = 0.50$ and $\rho_X = 0.60$, note that $\sigma_\varepsilon^2 = \frac{\sigma_u^2}{1 - \rho^2} = \frac{\sigma_u^2}{1 - 0.25} = \frac{4}{3}\sigma_u^2 \approx 1.3333\,\sigma_u^2$ and $\rho \rho_X = (0.50)(0.60) = 0.30$.
1. **Asymptotic Variance of OLS**:

$$\operatorname{AVar}(\hat{\beta}_{1,\text{OLS}}) = \frac{\sigma_u^2}{(1 - \rho^2)S_{xx}}\left(\frac{1 + \rho\rho_X}{1 - \rho\rho_X}\right) = \frac{\sigma_u^2}{0.75\,S_{xx}}\left(\frac{1 + 0.30}{1 - 0.30}\right) = \frac{\sigma_u^2}{S_{xx}}\left(\frac{4}{3} \times \frac{1.30}{0.70}\right) = \frac{5.20}{2.10}\frac{\sigma_u^2}{S_{xx}} = \frac{52}{21}\frac{\sigma_u^2}{S_{xx}} \approx 2.4762\,\frac{\sigma_u^2}{S_{xx}}$$

2. **Asymptotic Variance of GLS**: Because the quasi-differenced predictor $x_t^* = (x_t - \bar{x}) - \rho(x_{t-1} - \bar{x})$ has sum of squares $\sum (x_t^*)^2 \approx S_{xx}(1 + \rho^2 - 2\rho\rho_X) = S_{xx}(1 + 0.25 - 0.60) = 0.65\,S_{xx}$, the GLS variance is:

$$\operatorname{AVar}(\hat{\beta}_{1,\text{GLS}}) = \frac{\sigma_u^2}{0.65\,S_{xx}} = \frac{20}{13}\frac{\sigma_u^2}{S_{xx}} \approx 1.5385\,\frac{\sigma_u^2}{S_{xx}}$$

3. **Relative Efficiency and Percentage Efficiency Loss**:

$$\operatorname{Eff}(\hat{\beta}_{1,\text{OLS}}) = \frac{\operatorname{AVar}(\hat{\beta}_{1,\text{GLS}})}{\operatorname{AVar}(\hat{\beta}_{1,\text{OLS}})} = \frac{20/13}{52/21} = \frac{20 \times 21}{13 \times 52} = \frac{420}{676} = \frac{105}{169} \approx 0.6213 \quad (62.13\%)$$

Thus, ignoring moderate AR(1) serial correlation ($\rho = 0.50$) when the predictor has moderate persistence ($\rho_X = 0.60$) causes OLS to suffer a **$37.87\%$ loss in asymptotic efficiency** relative to GLS.
