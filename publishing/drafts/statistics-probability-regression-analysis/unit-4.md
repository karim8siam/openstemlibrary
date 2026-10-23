# Unit 4: Regression Diagnostics, Leverage & Influence Analysis: Studentized Residuals, Cook's Distance & DFFITS

Ordinary Least Squares estimation rests on a quadratic objective function $\|\mathbf{Y} - \mathbf{X}\mathbf{b}\|_2^2$ that weights all observations quadratically. Consequently, a single anomalous observation—whether resulting from a data-entry transcription error, sensor malfunction, or an extreme covariate configuration—can severely distort parameter estimates, inflate or deflate standard errors, and invalidate hypothesis tests. In this fourth unit, we develop the mathematical machinery of modern regression diagnostics pioneered by Pregibon, Cook, Weisberg, and Belsley, Kuh, and Welsch: Hat-matrix leverages $h_{ii}$, internally and externally studentized residuals, Sherman–Morrison–Woodbury rank-one deletion algebra, PRESS residuals, Cook's Distance $D_i$, DFFITS, DFBETAS, COVRATIO, and graphical diagnostic plots.

## 4.1 Hat Matrix Diagonals (Leverage), Algebraic Bounds, and Mahalanobis Distance Geometry

In multiple linear regression, not all data points exert equal potential to pull the fitted hyperplane toward themselves. To quantify the structural position of the $i$-th observation in the $k$-dimensional predictor space, we examine the Hat matrix $\mathbf{H} = \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T$ introduced in Unit 2. Because $\hat{\mathbf{Y}} = \mathbf{H}\mathbf{Y}$, each fitted value $\hat{Y}_i$ is a linear combination of all $n$ observed responses:

$$\hat{Y}_i = \sum_{j=1}^n h_{ij} Y_j = h_{ii} Y_i + \sum_{j \neq i} h_{ij} Y_j$$

The $i$-th diagonal element $h_{ii} = \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i$ is called the **leverage** of observation $i$. Differentiating $\hat{Y}_i$ with respect to $Y_i$ reveals the direct physical meaning of $h_{ii}$:

$$h_{ii} = \frac{\partial \hat{Y}_i}{\partial Y_i}$$

That is, $h_{ii}$ measures the marginal rate at which a perturbation in the $i$-th observed response $Y_i$ pulls its own fitted value $\hat{Y}_i$! Moreover, because $\text{Cov}(\hat{\mathbf{Y}}) = \sigma^2 \mathbf{H}$ and $\text{Cov}(\mathbf{e}) = \sigma^2(\mathbf{I}_n - \mathbf{H})$, the leverage $h_{ii}$ simultaneously controls the variance of the $i$-th fitted value and the variance of the $i$-th raw residual:

$$\text{Var}(\hat{Y}_i) = \sigma^2 h_{ii}, \qquad \text{Var}(e_i) = \sigma^2 (1 - h_{ii}), \qquad \text{Cov}(\hat{Y}_i, Y_i) = \sigma^2 h_{ii}$$

Notice the striking implication: as $h_{ii} \to 1$, the residual variance $\text{Var}(e_i) = \sigma^2(1 - h_{ii}) \to 0$, forcing $\hat{Y}_i \to Y_i$ and $e_i \to 0$ regardless of the actual value of $Y_i$! Thus, a high-leverage observation masks its own vertical outlier status by pulling the regression hyperplane directly through $( \mathbf{x}_i^T, Y_i )$, leaving a deceptively small raw residual $e_i$.

### Exact Algebraic Properties and Bounds of $h_{ii}$
Using the symmetry ($\mathbf{H}^T = \mathbf{H}$) and idempotency ($\mathbf{H}^2 = \mathbf{H}$) of the Hat matrix, we establish four fundamental mathematical properties of the leverages $h_{ii}$:

1. **Idempotent Row-Sum-of-Squares Identity**: Equating the $(i, i)$-th diagonal entry of $\mathbf{H}$ and $\mathbf{H}^2$ gives:
   $$h_{ii} = (\mathbf{H}^2)_{ii} = \sum_{j=1}^n h_{ij} h_{ji} = \sum_{j=1}^n h_{ij}^2 = h_{ii}^2 + \sum_{j \neq i} h_{ij}^2$$
2. **Upper and Lower Bounds ($1/n \le h_{ii} \le 1$)**: Because $\sum_{j \neq i} h_{ij}^2 \ge 0$, the identity $h_{ii} = h_{ii}^2 + \sum_{j \neq i} h_{ij}^2$ implies $h_{ii} - h_{ii}^2 = h_{ii}(1 - h_{ii}) \ge 0$, which forces $0 \le h_{ii} \le 1$ (and if $h_{ii} = 1$, then $h_{ij} = 0$ for all $j \neq i$, meaning observation $i$ alone dedicates an entire degree of freedom to fitting itself). Furthermore, whenever the model includes an intercept ($\mathbf{1}_n \in \mathcal{C}(\mathbf{X})$), partitioning $\mathbf{X} = [\mathbf{1}_n, \mathbf{X}_c]$ where $\mathbf{X}_c$ is the $n \times k$ mean-centered predictor matrix gives:
   $$h_{ii} = \frac{1}{n} + (\mathbf{x}_{c,i})^T (\mathbf{X}_c^T \mathbf{X}_c)^{-1} \mathbf{x}_{c,i} \ge \frac{1}{n}$$
   with $h_{ii} = 1/n$ attained if and only if observation $i$ sits exactly at the sample centroid $\mathbf{x}_{c,i} = \mathbf{0}_k$ (i.e., $x_{ij} = \bar{x}_j$ for all $j = 1, \dots, k$). Finally, if the covariate row $\mathbf{x}_i$ is replicated $r$ times in the dataset ($h_{ii} = h_{jj}$ for $r$ identical rows), then $h_{ii} = \sum_{j=1}^n h_{ij}^2 \ge r h_{ii}^2 \implies h_{ii} \le \frac{1}{r}$.
3. **Connection to Squared Mahalanobis Distance $D_{M,i}^2$**: Let $\mathbf{S}_{XX} = \frac{1}{n - 1} \mathbf{X}_c^T \mathbf{X}_c$ denote the $k \times k$ sample covariance matrix of the $k$ predictors. The squared Mahalanobis distance of the $i$-th predictor vector from the sample centroid $\bar{\mathbf{x}}$ is $D_{M,i}^2 = (\mathbf{x}_{c,i})^T \mathbf{S}_{XX}^{-1} \mathbf{x}_{c,i} = (n - 1) (\mathbf{x}_{c,i})^T (\mathbf{X}_c^T \mathbf{X}_c)^{-1} \mathbf{x}_{c,i}$. Therefore:
   $$h_{ii} = \frac{1}{n} + \frac{D_{M,i}^2}{n - 1}$$
   This proves that leverage $h_{ii}$ depends **exclusively on the predictor matrix $\mathbf{X}$** (never on $\mathbf{Y}$) and is a direct affine function of the squared Mahalanobis distance of $\mathbf{x}_i$ from the center of the predictor cloud.
4. **Average Leverage and Diagnostic Cutoff Rules**: Because $\sum_{i=1}^n h_{ii} = \text{tr}(\mathbf{H}) = p$, the arithmetic mean of the leverages across all $n$ observations is strictly:
   $$\bar{h} = \frac{1}{n} \sum_{i=1}^n h_{ii} = \frac{p}{n}$$
   Hoaglin and Welsch (1978) and Belsley, Kuh, and Welsch (1980) classify an observation as a **high-leverage point** whenever $h_{ii} > \frac{2p}{n}$ (or $h_{ii} > \frac{3p}{n}$ in small samples where $2p/n > 0.5$).

### Geometric Distinction Between High Leverage, Outliers, and Actual Influence
A foundational lesson of regression diagnostics is that an observation's position in the predictor space and its discrepancy in the response space play complementary but distinct diagnostic roles. Leverage is purely a property of the design matrix: it quantifies how far an observation's covariate vector lies from the multivariate sample centroid in the metric of the sample covariance matrix of the predictors, without ever looking at the response values. Consequently, a high-leverage point is not necessarily an error or a bad observation; if the response at that extreme predictor configuration follows the true linear relationship faithfully, that observation acts as a valuable anchor that reduces the standard errors of the estimated slopes. However, because the variance of the raw residual shrinks proportionally to one minus the leverage, the Ordinary Least Squares hyperplane is forced to pass close to any high-leverage point, creating a severe vulnerability whenever a measurement or specification error occurs at an extreme covariate vector.

## 4.2 Raw, Standardized, Internally Studentized, and Leave-One-Out Deletion (PRESS) Residuals

While leverage $h_{ii}$ diagnoses whether an observation is unusual in the *horizontal* predictor space $\mathcal{C}(\mathbf{X})$, residuals diagnose whether an observation is an **outlier** in the *vertical* response direction. However, as established in Section 4.1, raw residuals $e_i = Y_i - \hat{Y}_i$ suffer from non-constant variance $\text{Var}(e_i) = \sigma^2(1 - h_{ii})$ that shrinks toward zero at high-leverage points. Consequently, raw residuals cannot be compared on a uniform scale across different observations. Statisticians construct a hierarchy of scaled and leave-one-out residuals to overcome this deficiency.

### 1. Standardized vs. Internally Studentized Residuals ($r_i$)
A naive first scaling—sometimes called the **standardized residual** $d_i = e_i / s$—divides every raw residual by the constant residual standard error $s = \sqrt{\text{MSE}}$, ignoring the leverage factor $\sqrt{1 - h_{ii}}$. To equalize the sampling variances across all $n$ observations regardless of their leverage, we divide each raw residual $e_i$ by its exact estimated standard error $\text{SE}(e_i) = s\sqrt{1 - h_{ii}}$, yielding the **Internally Studentized Residual**, $r_i$:

$$r_i = \frac{e_i}{s \sqrt{1 - h_{ii}}}, \quad i = 1, 2, \dots, n$$

Why is $r_i$ called *internally* studentized? Because the denominator $s = \sqrt{\sum_{j=1}^n e_j^2 / (n - p)}$ is computed *internally* using all $n$ residuals, **including $e_i$ itself**! Because $e_i^2$ appears in the numerator $e_i$ and also inside the denominator $(n - p)s^2 = \text{SSE}$, the numerator and denominator of $r_i$ are **not statistically independent**. In fact, since $e_i^2 / (1 - h_{ii}) \le \text{SSE}$ (as we prove below), the squared internally studentized residual is algebraically bounded above by $n - p$:

$$\frac{r_i^2}{n - p} = \frac{e_i^2}{(n - p) s^2 (1 - h_{ii})} = \frac{e_i^2}{\text{SSE} (1 - h_{ii})} \in [0, 1] \implies |r_i| \le \sqrt{n - p}$$

Under normal errors, $\frac{r_i^2}{n - p} \sim \text{Beta}\!\left(\frac{1}{2}, \frac{n - p - 1}{2}\right)$ (the Ellenberg distribution), so $r_i$ does not follow an exact Student $t$ distribution. Moreover, if observation $i$ is a gross vertical outlier ($|e_i| \to \infty$), its enormous squared residual inflates $s^2$ in the denominator, artificially depressing $r_i$ and masking the outlier!

### 2. Leave-One-Out Deletion (PRESS) Residuals $e_{(i)}$ and the Sherman–Morrison–Woodbury Identity
To prevent a suspected outlier from contaminating the regression fit and the variance estimate used to judge it, suppose we delete the $i$-th observation $(\mathbf{x}_i^T, Y_i)$ from the dataset, fit the OLS regression to the remaining $n - 1$ observations to obtain the **leave-one-out parameter vector** $\hat{\boldsymbol{\beta}}_{(i)} = (\mathbf{X}_{(i)}^T \mathbf{X}_{(i)})^{-1} \mathbf{X}_{(i)}^T \mathbf{Y}_{(i)}$, and compute the **deleted (or PRESS) residual**:

$$e_{(i)} = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)}$$

Remarkably, we do **not** have to re-estimate the regression $n$ separate times! Because deleting row $\mathbf{x}_i^T$ from $\mathbf{X}$ corresponds to a rank-one subtraction $\mathbf{X}_{(i)}^T \mathbf{X}_{(i)} = \mathbf{X}^T \mathbf{X} - \mathbf{x}_i \mathbf{x}_i^T$ and $\mathbf{X}_{(i)}^T \mathbf{Y}_{(i)} = \mathbf{X}^T \mathbf{Y} - \mathbf{x}_i Y_i$, we apply the **Sherman–Morrison–Woodbury Rank-One Matrix Inversion Identity**:

$$\left( \mathbf{X}_{(i)}^T \mathbf{X}_{(i)} \right)^{-1} = \left( \mathbf{X}^T \mathbf{X} - \mathbf{x}_i \mathbf{x}_i^T \right)^{-1} = (\mathbf{X}^T\mathbf{X})^{-1} + \frac{(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1}}{1 - \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i} = (\mathbf{X}^T\mathbf{X})^{-1} + \frac{(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1}}{1 - h_{ii}}$$

Multiplying this inverse by $\mathbf{X}_{(i)}^T \mathbf{Y}_{(i)} = \mathbf{X}^T \mathbf{Y} - \mathbf{x}_i Y_i$ and simplifying using $\mathbf{x}_i^T \hat{\boldsymbol{\beta}} = \hat{Y}_i$ and $h_{ii} = \mathbf{x}_i^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i$ yields the fundamental **Leave-One-Out Parameter Update Formula**:

$$\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)} = \frac{(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i \, e_i}{1 - h_{ii}}$$

Premultiplying both sides by $\mathbf{x}_i^T$ gives $\hat{Y}_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)} = \frac{h_{ii} e_i}{1 - h_{ii}}$. Substituting $\mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)} = \hat{Y}_i - \frac{h_{ii} e_i}{1 - h_{ii}}$ into $e_{(i)} = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)}$ produces the celebrated **Exact PRESS Residual Identity**:

$$e_{(i)} = Y_i - \hat{Y}_i + \frac{h_{ii} e_i}{1 - h_{ii}} = e_i + \frac{h_{ii} e_i}{1 - h_{ii}} = \frac{e_i}{1 - h_{ii}}$$

Look at the beauty of $e_{(i)} = \frac{e_i}{1 - h_{ii}}$: every leave-one-out prediction error $e_{(i)}$ is obtained instantaneously from the single full-sample OLS fit simply by dividing the ordinary residual $e_i$ by $1 - h_{ii}$! Summing the squares of all $n$ deleted residuals defines David Allen's (1974) **Prediction Sum of Squares ($\text{PRESS}$)** criterion for leave-one-out cross-validation:

$$\text{PRESS} = \sum_{i=1}^n e_{(i)}^2 = \sum_{i=1}^n \left( \frac{e_i}{1 - h_{ii}} \right)^2, \qquad R_{\text{pred}}^2 = 1 - \frac{\text{PRESS}}{\text{SST}}$$

### Computational Efficiency of Leave-One-Out Cross-Validation via the PRESS Statistic
In modern machine learning and predictive analytics, $K$-fold and leave-one-out cross-validation are standard benchmarks for assessing out-of-sample generalization error and preventing overfitting. For general nonlinear models or neural networks, leave-one-out cross-validation requires refitting the model $n$ separate times on subsets of size $n-1$, multiplying the computational cost by a factor of $n$. In linear regression models estimated by Ordinary Least Squares, the Sherman–Morrison–Woodbury rank-one matrix update eliminates this computational bottleneck completely: every single leave-one-out prediction residual is obtained exactly by dividing the ordinary full-sample residual by one minus its Hat-matrix leverage. Consequently, the Prediction Sum of Squares (PRESS) and the cross-validated coefficient of determination can be evaluated instantaneously from a single matrix factorization, providing an immediate guard against models that overfit high-leverage data points.

## 4.3 Externally Studentized (Jackknife / R-Student) Residuals and Bonferroni Outlier Tests

Armed with the exact leave-one-out deletion residual $e_{(i)} = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)} = \frac{e_i}{1 - h_{ii}}$, we can now construct an outlier test statistic whose numerator and denominator are **strictly statistically independent**!

First, what is the sampling variance of the deleted residual $e_{(i)}$? Because $\hat{\boldsymbol{\beta}}_{(i)}$ is computed exclusively from the $n - 1$ observations in $\mathbf{Y}_{(i)}$, it is completely independent of $Y_i$. Since $\text{Var}(\mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)}) = \sigma^2 \mathbf{x}_i^T (\mathbf{X}_{(i)}^T \mathbf{X}_{(i)})^{-1} \mathbf{x}_i = \sigma^2 \left(h_{ii} + \frac{h_{ii}^2}{1 - h_{ii}}\right) = \frac{\sigma^2 h_{ii}}{1 - h_{ii}}$, or directly from $e_{(i)} = \frac{e_i}{1 - h_{ii}}$ with $\text{Var}(e_i) = \sigma^2(1 - h_{ii})$:

$$\text{Var}(e_{(i)}) = \frac{\text{Var}(e_i)}{(1 - h_{ii})^2} = \frac{\sigma^2 (1 - h_{ii})}{(1 - h_{ii})^2} = \frac{\sigma^2}{1 - h_{ii}}$$

Second, let $s_{(i)}^2 = \frac{\text{SSE}_{(i)}}{n - p - 1}$ denote the **leave-one-out residual mean square** computed from the regression with observation $i$ deleted (which has $n - 1 - p$ error degrees of freedom). By rank-one deletion algebra, $\text{SSE}_{(i)}$ is related to the full-sample $\text{SSE}$ by the exact identity:

$$\text{SSE}_{(i)} = \text{SSE} - \frac{e_i^2}{1 - h_{ii}} = (n - p)s^2 - \frac{e_i^2}{1 - h_{ii}} = s^2 \left( n - p - r_i^2 \right)$$

Dividing by $n - p - 1$ degrees of freedom gives the explicit formula for $s_{(i)}^2$ in terms of $s^2$ and $r_i^2$:

$$s_{(i)}^2 = \frac{(n - p) s^2 - e_i^2 / (1 - h_{ii})}{n - p - 1} = s^2 \left( \frac{n - p - r_i^2}{n - p - 1} \right)$$

Notice that when $r_i^2 = 1$, $s_{(i)}^2 = s^2$; when $r_i^2 > 1$ (an outlying residual), $s_{(i)}^2 < s^2$ because deleting the outlier removes its disproportionate inflation of the error variance!

Standardizing the deleted residual $e_{(i)}$ by its external standard error $s_{(i)} / \sqrt{1 - h_{ii}}$ (or equivalently replacing $s$ by $s_{(i)}$ in the formula for $r_i$) defines the **Externally Studentized Residual** (also called the **Jackknife Residual**, **Deleted $t$-Residual**, or **R-Student**), denoted by $t_i$:

$$t_i = \frac{e_{(i)}}{s_{(i)} / \sqrt{1 - h_{ii}}} = \frac{e_i}{s_{(i)} \sqrt{1 - h_{ii}}} = r_i \sqrt{\frac{n - p - 1}{n - p - r_i^2}}$$

### Mean-Shift Outlier Model Equivalence and Exact $t_{n-p-1}$ Distribution
Because $s_{(i)}^2$ is computed solely from the residuals within the subspace orthogonal to $\mathbf{X}_{(i)}$ on the remaining $n - 1$ observations, $(n - p - 1)s_{(i)}^2 / \sigma^2 \sim \chi_{n-p-1}^2$ is **statistically independent** of $e_{(i)} = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)}$. Therefore, under the null hypothesis that observation $i$ follows the same normal linear model as the rest of the sample, $t_i$ follows an **exact Student $t$ distribution with $n - p - 1$ degrees of freedom**:

$$t_i \sim t_{n - p - 1}$$

Even more remarkably, $t_i$ is **identically equal** to the ordinary partial $t$-statistic for testing $H_0: \delta_i = 0$ in the **Mean-Shift Outlier Model**:

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \delta_i \mathbf{u}_i + \boldsymbol{\varepsilon}$$

where $\mathbf{u}_i = (0, \dots, 0, 1, 0, \dots, 0)^T \in \mathbb{R}^n$ is an indicator (dummy) variable that equals $1$ for the $i$-th observation and $0$ for all other $n - 1$ observations! By the Frisch–Waugh–Lovell Theorem, adding the dummy variable $\mathbf{u}_i$ absorbs the $i$-th observation completely, leaving $\hat{\boldsymbol{\beta}}_{(i)}$ as the slope vector, $\hat{\delta}_i = e_{(i)} = \frac{e_i}{1 - h_{ii}}$ as the mean-shift coefficient, and $s_{(i)}^2$ as the residual mean square with $n - p - 1$ degrees of freedom.

When scanning all $n$ observations without knowing in advance which observation might be an outlier, testing $\max_{1 \le i \le n} |t_i|$ requires a **Bonferroni multiple-testing correction** across the $n$ tests: we declare observation $i$ a statistically significant outlier at familywise level $\alpha$ if:

$$|t_i| > t_{\alpha / (2n), \, n - p - 1}$$

### Why External Studentization Prevents Outlier Masking in Small and Moderate Samples
The mathematical distinction between internally studentized residuals and externally studentized (jackknife) residuals is particularly consequential when a dataset of small or moderate size contains one or two severe vertical outliers. In an internally studentized residual, the numerator residual also contributes its square to the pooled residual sum of squares in the denominator. As a result, a single extreme outlier inflates the full-sample error variance estimate so substantially that its own internally studentized residual is compressed toward the bounded ceiling of the square root of the error degrees of freedom, while the internally studentized residuals of all other observations are artificially shrunk toward zero. External studentization breaks this algebraic coupling by computing the denominator scale estimate from the remaining $n-1$ observations with the suspect point omitted, restoring exact Student-$t$ distribution theory and ensuring high statistical power in Bonferroni outlier screening.

## 4.4 Global Influence Measures: Cook's Distance D_i and Calibration Thresholds

A critical principle of regression diagnostics is that **Vertical Outlier Status ($|r_i|$) $\times$ Horizontal Leverage ($h_{ii}$) $=$ Influence**:
- A vertical outlier near the centroid $\bar{\mathbf{x}}$ ($h_{ii} \approx 1/n$) shifts the intercept $\hat{\beta}_0$ by $e_i / n$ but barely tilts the regression slopes $\hat{\boldsymbol{\beta}}_{\text{slopes}}$.
- Conversely, a high-leverage point ($h_{ii}$ near $1$) that lies right on the true regression line ($e_i \approx 0$) reinforces the precision of the fit without distorting the parameter estimates (a "good leverage point").
- An observation becomes **highly influential** (a "bad leverage point") when it combines **both** moderate-to-high leverage $h_{ii}$ **and** a non-negligible studentized residual $r_i$.

In 1977, R. Dennis Cook introduced the canonical global measure of an observation's joint influence on all $p$ regression parameters (and equivalently on all $n$ fitted values): **Cook's Distance**, $D_i$. Recall from Section 3.4 that the $100(1 - \alpha)\%$ joint confidence ellipsoid for $\boldsymbol{\beta}$ is defined by the quadratic form $(\boldsymbol{\beta} - \hat{\boldsymbol{\beta}})^T (\mathbf{X}^T\mathbf{X}) (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}) / (p s^2) \le F_{\alpha, p, n-p}$. Cook's Distance $D_i$ measures the squared Mahalanobis distance from the full-sample OLS estimator $\hat{\boldsymbol{\beta}}$ to the leave-one-out estimator $\hat{\boldsymbol{\beta}}_{(i)}$ in the metric of the full-sample covariance matrix $p s^2 (\mathbf{X}^T\mathbf{X})^{-1}$:

$$D_i = \frac{\left( \hat{\boldsymbol{\beta}}_{(i)} - \hat{\boldsymbol{\beta}} \right)^T (\mathbf{X}^T\mathbf{X}) \left( \hat{\boldsymbol{\beta}}_{(i)} - \hat{\boldsymbol{\beta}} \right)}{p \, s^2} = \frac{\left\| \hat{\mathbf{Y}}_{(i)} - \hat{\mathbf{Y}} \right\|_2^2}{p \, s^2}$$

where $\hat{\mathbf{Y}}_{(i)} = \mathbf{X}\hat{\boldsymbol{\beta}}_{(i)}$ is the vector of all $n$ fitted values predicted when observation $i$ is omitted from the estimation! Thus, $D_i$ equals both the standardized shift in the parameter vector $\hat{\boldsymbol{\beta}}$ and the average squared standardized shift across all $n$ fitted predictions.

### Explicit Closed-Form Expression in Terms of $r_i$ and $h_{ii}$
Substituting the Sherman–Morrison–Woodbury update $\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)} = \frac{(\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i e_i}{1 - h_{ii}}$ into the quadratic form of $D_i$ yields a remarkably simple factorization that requires **no matrix re-inversion**:

$$D_i = \frac{1}{p s^2} \left( \frac{e_i}{1 - h_{ii}} \right)^2 \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1} (\mathbf{X}^T\mathbf{X}) (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i = \frac{e_i^2 \, h_{ii}}{p s^2 (1 - h_{ii})^2}$$

Grouping the internally studentized residual $r_i^2 = \frac{e_i^2}{s^2(1 - h_{ii})}$ separates $D_i$ into the product of the vertical outlier component $r_i^2 / p$ and the monotonically increasing horizontal leverage ratio $h_{ii} / (1 - h_{ii})$:

$$D_i = \left( \frac{r_i^2}{p} \right) \left( \frac{h_{ii}}{1 - h_{ii}} \right)$$

Notice how $D_i$ makes the interaction between vertical discrepancy and horizontal leverage mathematically explicit:
- If $h_{ii} = 0.50$, the leverage multiplier $\frac{h_{ii}}{1 - h_{ii}} = 1.0$; if $h_{ii} = 0.80$, the multiplier jumps to $\frac{0.80}{0.20} = 4.0$; if $h_{ii} = 0.90$, it jumps to $9.0$!
- **Calibration and Practical Cutoffs for $D_i$**: Although $D_i$ is not an exact $F$-distributed test statistic, Cook (1977) proposed calibrating $D_i$ against the median ($50\text{th}$ percentile) of the $F_{p, n-p}$ confidence ellipsoid distribution: if $D_i \approx F_{0.50, p, n-p} \approx 1.0$, then deleting observation $i$ moves the least-squares parameter vector $\hat{\boldsymbol{\beta}}$ all the way from the center of the joint confidence ellipsoid to the boundary of the **$50\%$ confidence region**! Consequently:
  1. **$D_i > 1.0$** (or $D_i > F_{0.50, p, n-p}$): Observation $i$ is globally influential and warrants immediate investigation.
  2. **$D_i > \frac{4}{n}$** (or $D_i > \frac{4}{n - p}$): Sample-size-adjusted screening cutoff used in automated diagnostic plots to flag moderately influential observations for closer inspection.

### Interpreting Cook's Distance Contours on the Leverage-Residual Plane
Because Cook's Distance factors cleanly into the product of the squared internally studentized residual (divided by $p$) and the leverage ratio $h_{ii} / (1 - h_{ii})$, modern statistical software displays influence diagnostics by plotting the studentized residuals on the vertical axis against the Hat-matrix leverages on the horizontal axis, superimposed with hyperbolic contour curves of constant Cook's Distance ($D_i = 0.5$ and $D_i = 1.0$). On this diagnostic plane, observations near the left boundary (low leverage) must have enormous vertical residuals to cross the $D_i = 0.5$ contour, whereas observations near the right boundary (high leverage) cross the $D_i = 1.0$ contour even with modest studentized residuals between $1$ and $2$. Inspecting this joint leverage-residual chart allows the analyst to immediately separate benign vertical outliers, benign high-leverage anchors, and genuinely influential observations that distort the fitted hyperplane.

## 4.5 Targeted Influence Diagnostics: DFFITS, DFBETAS, and COVRATIO

In their landmark 1980 monograph *Regression Diagnostics*, David Belsley, Edwin Kuh, and Roy Welsch introduced three targeted leave-one-out diagnostics—**DFFITS**, **DFBETAS**, and **COVRATIO**—that use the externally studentized variance $s_{(i)}^2$ and isolate the influence of observation $i$ on specific individual quantities.

### 1. $\text{DFFITS}_i$ (Standardized Difference in Fitted Value $\hat{Y}_i$)
$\text{DFFITS}_i$ measures how many standard errors the $i$-th fitted value $\hat{Y}_i = \mathbf{x}_i^T \hat{\boldsymbol{\beta}}$ changes when the $i$-th observation is deleted, scaled by the external standard error of $\hat{Y}_i$, namely $s_{(i)} \sqrt{h_{ii}}$:

$$\text{DFFITS}_i = \frac{\hat{Y}_i - \hat{Y}_{i(i)}}{s_{(i)} \sqrt{h_{ii}}}$$

Since $\hat{Y}_i - \hat{Y}_{i(i)} = \frac{h_{ii} e_i}{1 - h_{ii}}$ and $t_i = \frac{e_i}{s_{(i)}\sqrt{1 - h_{ii}}}$, $\text{DFFITS}_i$ simplifies immediately to:

$$\text{DFFITS}_i = \left( \frac{e_i}{s_{(i)} \sqrt{1 - h_{ii}}} \right) \sqrt{\frac{h_{ii}}{1 - h_{ii}}} = t_i \sqrt{\frac{h_{ii}}{1 - h_{ii}}}$$

Notice the exact structural bridge between $\text{DFFITS}_i$ and Cook's Distance $D_i$:

$$\text{DFFITS}_i^2 = p \, D_i \left( \frac{s^2}{s_{(i)}^2} \right)$$

Whereas $D_i$ is always non-negative and uses $s^2$, $\text{DFFITS}_i$ retains the sign of $e_i$ (indicating whether observation $i$ pulls $\hat{Y}_i$ upward or downward) and uses the outlier-resistant scale $s_{(i)}$. Belsley, Kuh, and Welsch recommend flagging observation $i$ as influential if:

$$|\text{DFFITS}_i| > 2 \sqrt{\frac{p}{n}} \quad (\text{for medium/large } n), \qquad \text{or} \qquad |\text{DFFITS}_i| > 1.0 \quad (\text{for small } n)$$

### 2. $\text{DFBETAS}_{j, (i)}$ (Standardized Difference in Individual Parameter $\hat{\beta}_j$)
While $D_i$ and $\text{DFFITS}_i$ measure aggregate influence on the fitted vector, a researcher often wants to know whether observation $i$ specifically distorts a *particular* regression coefficient of interest, $\hat{\beta}_j$ ($j = 0, 1, \dots, k$). $\text{DFBETAS}_{j, (i)}$ measures the change $\hat{\beta}_j - \hat{\beta}_{j(i)}$ scaled by the externally estimated standard error of $\hat{\beta}_j$, namely $s_{(i)} \sqrt{c_{jj}}$ where $c_{jj} = [(\mathbf{X}^T\mathbf{X})^{-1}]_{jj}$:

$$\text{DFBETAS}_{j, (i)} = \frac{\hat{\beta}_j - \hat{\beta}_{j(i)}}{s_{(i)} \sqrt{c_{jj}}} = \frac{\left[ (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i \right]_j e_i}{s_{(i)} \sqrt{c_{jj}} (1 - h_{ii})}$$

Let $\mathbf{R} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T \in \mathbb{R}^{p \times n}$ so that $\hat{\boldsymbol{\beta}} = \mathbf{R}\mathbf{Y}$. Then $\text{DFBETAS}_{j, (i)} = \frac{r_{ji}}{\sqrt{\sum_{m=1}^n r_{jm}^2}} \frac{t_i}{\sqrt{1 - h_{ii}}}$. Belsley, Kuh, and Welsch recommend the sample-size-adjusted cutoff:

$$|\text{DFBETAS}_{j, (i)}| > \frac{2}{\sqrt{n}} \quad (\text{for large } n), \qquad \text{or} \qquad |\text{DFBETAS}_{j, (i)}| > 1.0 \quad (\text{for small } n)$$

### 3. $\text{COVRATIO}_i$ (Determinant Ratio of Covariance Matrices / Generalized Variance Precision)
Recall that the volume of the joint confidence ellipsoid for $\boldsymbol{\beta}$ is proportional to the square root of the **generalized variance**, $\det(\widehat{\text{Cov}}(\hat{\boldsymbol{\beta}})) = \det(s^2 (\mathbf{X}^T\mathbf{X})^{-1}) = (s^2)^p \det((\mathbf{X}^T\mathbf{X})^{-1})$. $\text{COVRATIO}_i$ compares the determinant of the covariance matrix when observation $i$ is deleted against the full-sample determinant:

$$\text{COVRATIO}_i = \frac{\det\left( s_{(i)}^2 (\mathbf{X}_{(i)}^T \mathbf{X}_{(i)})^{-1} \right)}{\det\left( s^2 (\mathbf{X}^T \mathbf{X})^{-1} \right)} = \left( \frac{s_{(i)}^2}{s^2} \right)^p \frac{\det(\mathbf{X}^T\mathbf{X})}{\det(\mathbf{X}^T\mathbf{X} - \mathbf{x}_i \mathbf{x}_i^T)}$$

By the Matrix Determinant Lemma, $\det(\mathbf{X}^T\mathbf{X} - \mathbf{x}_i \mathbf{x}_i^T) = \det(\mathbf{X}^T\mathbf{X}) (1 - \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i) = \det(\mathbf{X}^T\mathbf{X})(1 - h_{ii})$! Substituting this and $s_{(i)}^2 / s^2 = \frac{n - p - r_i^2}{n - p - 1}$ yields the closed-form formula:

$$\text{COVRATIO}_i = \left( \frac{n - p - r_i^2}{n - p - 1} \right)^p \left( \frac{1}{1 - h_{ii}} \right) = \frac{1}{\left( \frac{n - p - 1 + t_i^2}{n - p} \right)^p (1 - h_{ii})}$$

Notice the two competing forces inside $\text{COVRATIO}_i$:
- A **high-leverage good point** ($h_{ii}$ large, $t_i \approx 0$) makes $\frac{1}{1 - h_{ii}} > 1$, so $\text{COVRATIO}_i > 1$: including observation $i$ *shrinks* the covariance determinant and improves estimation precision!
- A **vertical outlier** ($|t_i|$ large, $h_{ii}$ small) makes $s_{(i)}^2 \ll s^2$, so $\text{COVRATIO}_i < 1$: including observation $i$ inflates $s^2$ and *degrades* estimation precision!
Observations are flagged when $|\text{COVRATIO}_i - 1| > \frac{3p}{n}$.

### Synthesizing DFFITS, DFBETAS, and COVRATIO in Applied Regression Audits
Whereas Cook's Distance summarizes an observation's aggregate impact across the entire parameter vector in a single scalar, the Belsley–Kuh–Welsch triad of DFFITS, DFBETAS, and COVRATIO provides a granular diagnostic profile that pinpoints exactly which inferential conclusions are threatened by an anomalous case. In many observational studies with five or ten explanatory variables, only one primary policy or treatment coefficient is of substantive scientific interest while the remaining covariates serve purely as statistical controls. An observation may exhibit a moderately large Cook's Distance because it perturbs the estimated coefficients of two collinear control variables, yet its DFBETAS value for the primary treatment variable of interest may be negligible, reassuring the investigator that the main scientific finding is robust to that data point. Conversely, inspecting the COVRATIO statistic reveals whether deleting an observation expands or contracts the volume of the joint confidence ellipsoid, distinguishing between high-leverage points that stabilize the design matrix and vertical outliers that degrade estimation efficiency.

## 4.6 Graphical Diagnostics, Partial Plots, and Formal Lack-of-Fit F-Testing

Complementing numerical influence statistics, graphical residual diagnostics reveal structural violations of the Gauss–Markov assumptions—nonlinearity, heteroscedasticity, non-normality, omitted interactions, and masked leverage points—that summary statistics like $R^2$ and overall $F$-tests completely conceal (as famously demonstrated by **Anscombe's Quartet**, where four datasets with identical $\hat{\beta}_0, \hat{\beta}_1, s^2, R^2,$ and $F$-statistics exhibit radically different scatterplots).

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Diagnostic Plot</th><th>Vertical Axis vs Horizontal Axis</th><th>Primary Purpose &amp; Signature Pathologies</th></tr>
</thead>
<tbody>
<tr><td><strong>1. Residuals vs. Fitted Values</strong></td><td>$r_i$ (or $t_i$) vs. $\hat{Y}_i$</td><td>Plotted against $\hat{Y}_i$ (never against $Y_i$, because $\text{Cov}(e_i, Y_i) = \sigma^2(1 - h_{ii}) > 0$ induces a spurious upward slope of $1 - R^2$!). A <strong>U-shaped / parabolic curve</strong> indicates unmodeled nonlinearity; an <strong>outward megaphone / fan pattern</strong> indicates heteroscedasticity ($\text{Var}(\varepsilon_i)$ increasing with $\mu_i$).</td></tr>
<tr><td><strong>2. Scale-Location (Spread-Level) Plot</strong></td><td>$\sqrt{|r_i|}$ vs. $\hat{Y}_i$</td><td>Detects monotone heteroscedasticity more sensitively than signed residuals by folding negative residuals upward; a non-zero slope indicates non-constant variance.</td></tr>
<tr><td><strong>3. Normal Quantile-Quantile (Q-Q) Plot</strong></td><td>Ordered $t_{(1)} \le \dots \le t_{(n)}$ vs. $\Phi^{-1}\!\left(\frac{i - 0.375}{n + 0.25}\right)$</td><td>Checks Gaussianity (Assumption A6). An <strong>S-shaped curve</strong> indicates heavy tails (leptokurtosis) or light tails; a <strong>bowed / concave curve</strong> indicates positive or negative skewness.</td></tr>
<tr><td><strong>4. Residual Sequence / Lag Plot</strong></td><td>$r_t$ vs. time index $t$ (or $r_t$ vs. $r_{t-1}$)</td><td>Checks non-autocorrelation (Assumption A5). Long runs of positive/negative residuals or a positive slope in $r_t$ vs. $r_{t-1}$ indicate positive serial correlation ($\rho > 0$).</td></tr>
<tr><td><strong>5. Added-Variable (Partial Regression) Plot</strong></td><td>$\mathbf{e}_{Y \mid (-j)}$ vs. $\mathbf{e}_{j \mid (-j)}$</td><td>Visualizes the Frisch–Waugh–Lovell regression for predictor $X_j$ after sweeping out all other predictors $\mathbf{X}_{(-j)}$. Reveals high-leverage points in $X_j$ and observations driving $\hat{\beta}_j$.</td></tr>
<tr><td><strong>6. Component-Plus-Residual (Partial Residual) Plot</strong></td><td>$\mathbf{e}_F + \hat{\beta}_j \mathbf{x}_{(j)}$ vs. $\mathbf{x}_{(j)}$</td><td>Plots the partial residual $e_i + \hat{\beta}_j x_{ij}$ directly against the raw covariate $x_{ij}$. Superior to Added-Variable plots for diagnosing curvature $g_j(X_j)$ and suggesting power transformations.</td></tr>
</tbody>
</table></div>

### Mathematical Properties of Added-Variable vs. Component-Plus-Residual Plots
Let us compare the exact algebraic properties of the two partial plots for a target predictor $X_j$:
1. **Added-Variable (Partial Regression) Plot**: Plot the FWL response residuals $\mathbf{e}_{Y \mid (-j)} = \mathbf{M}_{(-j)} \mathbf{Y}$ on the vertical axis against the FWL predictor residuals $\mathbf{e}_{j \mid (-j)} = \mathbf{M}_{(-j)} \mathbf{x}_{(j)}$ on the horizontal axis. By the Frisch–Waugh–Lovell Theorem (Section 2.5):
   - The simple OLS line fitted to this scatterplot passes strictly through $(0, 0)$ with **exact slope $\hat{\beta}_j$** (the multiple regression coefficient of $X_j$ in the full model!).
   - The vertical residuals from this simple line are **identically the full-model residuals $\mathbf{e}_F$**.
   - The correlation of the points in this plot is the **partial correlation $r_{Y j \cdot (-j)}$**, and horizontal outliers identify observations with high partial leverage on $\hat{\beta}_j$.
2. **Component-Plus-Residual (Larsen–McCleary Partial Residual) Plot**: Define the partial residual vector $\mathbf{e}_j^* = \mathbf{e}_F + \hat{\beta}_j \mathbf{x}_{(j)}$ and plot $e_{ij}^*$ against the unresidualized predictor $x_{ij}$. The simple OLS regression of $\mathbf{e}_j^*$ on $\mathbf{x}_{(j)}$ (centered) also has **exact slope $\hat{\beta}_j$** (since $\frac{\mathbf{x}_{c(j)}^T (\mathbf{e}_F + \hat{\beta}_j \mathbf{x}_{c(j)})}{\mathbf{x}_{c(j)}^T \mathbf{x}_{c(j)}} = 0 + \hat{\beta}_j = \hat{\beta}_j$) and identical vertical residuals $\mathbf{e}_F$. However, because its horizontal axis is the true variable $x_{ij}$ rather than the linear residual $e_{i, j \mid (-j)}$, if the true model is $Y = \beta_0 + g_j(X_j) + \mathbf{X}_{(-j)}\boldsymbol{\beta}_{(-j)} + \varepsilon$, the Component-Plus-Residual plot directly displays the nonlinear curve $g_j(x_{ij})$ without distortion when $X_j$ is correlated with $\mathbf{X}_{(-j)}$.

### Formal Lack-of-Fit F-Test via Pure Error and Lack-of-Fit Partitioning

While residual plots provide visual evidence of functional misspecification, when an experimental dataset contains **replicated observations** (multiple experimental units observed at the exact same covariate vector), we can conduct an **exact, distribution-free (of the regression form) $F$-test for Lack of Fit**!

Suppose the $n$ total observations occur across $c < n$ distinct covariate levels (or distinct predictor vectors) $\mathbf{x}_{(1)}, \mathbf{x}_{(2)}, \dots, \mathbf{x}_{(c)}$. At the $j$-th distinct predictor level $\mathbf{x}_{(j)}$, suppose there are $n_j \ge 1$ replicate observations $Y_{j1}, Y_{j2}, \dots, Y_{j, n_j}$, where $\sum_{j=1}^c n_j = n$ and at least one level has $n_j \ge 2$ replicates (so $n > c > p$). Let $\bar{Y}_{j\cdot} = \frac{1}{n_j} \sum_{m=1}^{n_j} Y_{jm}$ denote the sample mean of the replicates at the $j$-th covariate level, and let $\hat{Y}_j = \mathbf{x}_{(j)}^T \hat{\boldsymbol{\beta}}$ denote the fitted regression value at level $j$.

We decompose each individual regression residual $e_{jm} = Y_{jm} - \hat{Y}_j$ by adding and subtracting the replicate group mean $\bar{Y}_{j\cdot}$:

$$Y_{jm} - \hat{Y}_j = \underbrace{(Y_{jm} - \bar{Y}_{j\cdot})}_{\text{Pure Error Deviation}} + \underbrace{(\bar{Y}_{j\cdot} - \hat{Y}_j)}_{\text{Lack-of-Fit Deviation}}$$

Squaring both sides and summing over $m = 1, \dots, n_j$ and $j = 1, \dots, c$, the cross-product term $2 \sum_{j=1}^c (\bar{Y}_{j\cdot} - \hat{Y}_j) \sum_{m=1}^{n_j} (Y_{jm} - \bar{Y}_{j\cdot}) = 0$ vanishes identically because deviations from each group mean sum to zero! This yields the exact **Pure Error vs. Lack-of-Fit Partition of $\text{SSE}$**:

$$\text{SSE} = \text{SSPE} + \text{SSLF}$$

where:
1. **Pure Error Sum of Squares ($\text{SSPE}$)** with $\text{df}_{\text{PE}} = \sum_{j=1}^c (n_j - 1) = n - c$ degrees of freedom:
   $$\text{SSPE} = \sum_{j=1}^c \sum_{m=1}^{n_j} (Y_{jm} - \bar{Y}_{j\cdot})^2, \qquad \text{MSPE} = \frac{\text{SSPE}}{n - c}$$
   Crucially, $\text{SSPE}$ depends **only** on the internal variation among replicates at identical $X$ values! Regardless of whether the postulated linear regression model $\mathbb{E}[Y \mid \mathbf{x}] = \mathbf{x}^T \boldsymbol{\beta}$ is true or completely misspecified, for fixed $\mathbf{x}_{(j)}$ the replicates $Y_{j1}, \dots, Y_{j, n_j}$ have identical mean $\mu(\mathbf{x}_{(j)})$ and variance $\sigma^2$, so $\mathbb{E}[\text{MSPE}] = \sigma^2$ is **always an unbiased estimator of $\sigma^2$**, and $\text{SSPE}/\sigma^2 \sim \chi_{n-c}^2$.
2. **Lack-of-Fit Sum of Squares ($\text{SSLF}$)** with $\text{df}_{\text{LF}} = (n - p) - (n - c) = c - p$ degrees of freedom:
   $$\text{SSLF} = \text{SSE} - \text{SSPE} = \sum_{j=1}^c n_j (\bar{Y}_{j\cdot} - \hat{Y}_j)^2, \qquad \text{MSLF} = \frac{\text{SSLF}}{c - p}$$
   Its expected value is $\mathbb{E}[\text{MSLF}] = \sigma^2 + \frac{1}{c - p} \sum_{j=1}^c n_j \left[ \mu(\mathbf{x}_{(j)}) - \mathbf{x}_{(j)}^T \boldsymbol{\beta}^* \right]^2$.

Because $\text{SSLF}$ and $\text{SSPE}$ are statistically independent by Cochran's Theorem, the **Exact Lack-of-Fit $F$-Statistic** for testing $H_0: \mathbb{E}[Y \mid \mathbf{x}] = \mathbf{x}^T \boldsymbol{\beta}$ against the general alternative $H_1: \mathbb{E}[Y \mid \mathbf{x}] = \mu(\mathbf{x}) \neq \mathbf{x}^T \boldsymbol{\beta}$ is:

$$F_{\text{LF}} = \frac{\text{MSLF}}{\text{MSPE}} = \frac{\text{SSLF} / (c - p)}{\text{SSPE} / (n - c)} \sim F_{c - p, \, n - c} \quad \text{under } H_0$$

Notice also that the one-way ANOVA model fitting a separate mean $\mu_j$ to each of the $c$ groups represents the **maximal (saturated) model** achievable by any function of $\mathbf{x}$, so $R_{\max}^2 = 1 - \frac{\text{SSPE}}{\text{SST}} < 1$ is the theoretical upper bound on $R^2$ for any regression curve fitted to this dataset!

### Diagnostic Workflow for Reconciling Graphical Residual Patterns and Formal Lack-of-Fit Tests
In contemporary statistical practice, visual residual diagnostics and formal hypothesis tests for functional specification operate hand in hand as a unified model-criticism workflow. When experimental replicates are available at identical covariate combinations, the formal Analysis of Variance Lack-of-Fit $F$-test provides an objective, assumption-light test of whether the linear model is adequate, because the pure error mean square estimates the disturbance variance without assuming any parametric form for the conditional mean function. However, when the Lack-of-Fit $F$-test rejects the linear specification—or in observational studies where exact covariate replicates do not exist—the test statistic alone does not tell the analyst how to repair the model. At that stage, comparing the Residuals-versus-Fitted plot, the Added-Variable plots, and the Component-Plus-Residual partial plots identifies which specific regressor exhibits curvature, whether a logarithmic or Box–Cox power transformation is warranted, or whether an omitted interaction term is responsible for the systematic lack of fit.

## Fully worked question 1: Complete Influence & Outlier Audit: Computing r_i, e_(i), t_i, Cook's Distance D_i, DFFITS_i, and COVRATIO_i

### Question
In a multiple linear regression model with $n = 25$ observations and $p = 5$ parameters ($\beta_0, \beta_1, \beta_2, \beta_3, \beta_4$), the full-sample Residual Sum of Squares is $\text{SSE} = 80.00$. Three suspect observations (Cases A, B, and C) exhibit the following raw residuals $e_i$ and Hat-matrix leverages $h_{ii}$:
- **Case A (Pure Vertical Outlier near Centroid)**: $e_A = 6.00$, $h_{AA} = 0.10$.
- **Case B (High-Leverage Good Point)**: $e_B = 0.80$, $h_{BB} = 0.75$.
- **Case C (High-Leverage Influential Point)**: $e_C = 4.00$, $h_{CC} = 0.60$.

1. For each of the three cases ($i \in \{A, B, C\}$), compute the leave-one-out PRESS residual $e_{(i)}$, the internally studentized residual $r_i$, the leave-one-out error variance $s_{(i)}^2$, and the externally studentized (jackknife) residual $t_i$. Test each case for outlier status at familywise significance level $\alpha = 0.05$ using the Bonferroni threshold $t_{0.05/(2 \times 25), \, 19} = t_{0.001, \, 19} = 3.579$.
2. For each of the three cases, compute **Cook's Distance $D_i$**, **$\text{DFFITS}_i$**, and **$\text{COVRATIO}_i$**.
3. Compare the diagnostic profiles of Cases A, B, and C against the standard Belsley–Kuh–Welsch and Cook thresholds ($h_{\text{cut}} = 2p/n$, $D_i > 1.0$, $|\text{DFFITS}_i| > 2\sqrt{p/n}$, $|\text{COVRATIO}_i - 1| > 3p/n$) and explain what action an analyst should take for each case.

### Solution, step 1: Compute PRESS residuals e_(i), internally studentized r_i, s_(i)^2, and jackknife t_i
With $n = 25$ and $p = 5$, the full-sample error degrees of freedom are $n - p = 20$, and the full-sample error variance estimate is:

$$s^2 = \text{MSE} = \frac{\text{SSE}}{n - p} = \frac{80.00}{20} = 4.00 \implies s = 2.00$$

Using $e_{(i)} = \frac{e_i}{1 - h_{ii}}$, $r_i = \frac{e_i}{s\sqrt{1 - h_{ii}}}$, $s_{(i)}^2 = s^2 \left(\frac{20 - r_i^2}{19}\right)$, and $t_i = r_i \sqrt{\frac{19}{20 - r_i^2}}$:

1. **Case A ($e_A = 6.00, \; h_{AA} = 0.10, \; 1 - h_{AA} = 0.90$)**:
   - $e_{(A)} = \frac{6.00}{0.90} = 6.6667$
   - $r_A = \frac{6.00}{2.00 \sqrt{0.90}} = \frac{3.00}{0.94868} = 3.1623 \implies r_A^2 = \frac{9.00}{0.90} = 10.00$
   - $s_{(A)}^2 = 4.00 \left(\frac{20 - 10.00}{19}\right) = \frac{40.00}{19} = 2.1053$ (deleting Outlier A cuts the error variance nearly in half!)
   - $t_A = 3.1623 \sqrt{\frac{19}{20 - 10.00}} = \sqrt{10.00 \times 1.90} = \sqrt{19.00} = 4.3589$
   Since $|t_A| = 4.3589 > t_{0.001, 19} = 3.579$, **Case A is a statistically significant vertical outlier** even after Bonferroni correction!

2. **Case B ($e_B = 0.80, \; h_{BB} = 0.75, \; 1 - h_{BB} = 0.25$)**:
   - $e_{(B)} = \frac{0.80}{0.25} = 3.2000$
   - $r_B = \frac{0.80}{2.00 \sqrt{0.25}} = \frac{0.80}{1.00} = 0.8000 \implies r_B^2 = 0.6400$
   - $s_{(B)}^2 = 4.00 \left(\frac{20 - 0.64}{19}\right) = 4.00 (1.01895) = 4.0758$
   - $t_B = 0.8000 \sqrt{\frac{19}{19.36}} = 0.7925 < 3.579$ (not a vertical outlier).

3. **Case C ($e_C = 4.00, \; h_{CC} = 0.60, \; 1 - h_{CC} = 0.40$)**:
   - $e_{(C)} = \frac{4.00}{0.40} = 10.0000$
   - $r_C = \frac{4.00}{2.00 \sqrt{0.40}} = \frac{2.00}{0.63246} = 3.1623 \implies r_C^2 = \frac{4.00}{0.40} = 10.00$
   - $s_{(C)}^2 = 4.00 \left(\frac{20 - 10.00}{19}\right) = 2.1053$
   - $t_C = 3.1623 \sqrt{\frac{19}{10.00}} = 4.3589 > 3.579$ (significant vertical outlier).

### Solution, step 2: Evaluate Cook's Distance D_i, DFFITS_i, and COVRATIO_i for all three cases
Using $D_i = \left(\frac{r_i^2}{p}\right)\left(\frac{h_{ii}}{1 - h_{ii}}\right)$, $\text{DFFITS}_i = t_i \sqrt{\frac{h_{ii}}{1 - h_{ii}}}$, and $\text{COVRATIO}_i = \left(\frac{s_{(i)}^2}{s^2}\right)^p \left(\frac{1}{1 - h_{ii}}\right)$ with $p = 5$:

1. **Case A ($r_A^2 = 10.00, \; t_A = 4.3589, \; h_{AA} = 0.10, \; \frac{h_{AA}}{1 - h_{AA}} = \frac{1}{9} \approx 0.1111$)**:
   - $D_A = \left(\frac{10.00}{5}\right) \left(\frac{0.10}{0.90}\right) = 2.00 \times \frac{1}{9} = 0.2222$
   - $\text{DFFITS}_A = 4.3589 \sqrt{\frac{1}{9}} = \frac{4.3589}{3} = 1.4530$
   - $\text{COVRATIO}_A = \left(\frac{10.00}{19}\right)^5 \left(\frac{1}{0.90}\right) = (0.52632)^5 (1.1111) = 0.04035 \times 1.1111 = 0.0448$

2. **Case B ($r_B^2 = 0.64, \; t_B = 0.7925, \; h_{BB} = 0.75, \; \frac{h_{BB}}{1 - h_{BB}} = \frac{0.75}{0.25} = 3.00$)**:
   - $D_B = \left(\frac{0.64}{5}\right) (3.00) = 0.128 \times 3.00 = 0.3840$
   - $\text{DFFITS}_B = 0.7925 \sqrt{3.00} = 0.7925 (1.73205) = 1.3727$
   - $\text{COVRATIO}_B = \left(\frac{19.36}{19}\right)^5 \left(\frac{1}{0.25}\right) = (1.01895)^5 (4.00) = 1.0984 \times 4.00 = 4.3935$

3. **Case C ($r_C^2 = 10.00, \; t_C = 4.3589, \; h_{CC} = 0.60, \; \frac{h_{CC}}{1 - h_{CC}} = \frac{0.60}{0.40} = 1.50$)**:
   - $D_C = \left(\frac{10.00}{5}\right) (1.50) = 2.00 \times 1.50 = 3.0000$
   - $\text{DFFITS}_C = 4.3589 \sqrt{1.50} = 4.3589 (1.22474) = 5.3385$
   - $\text{COVRATIO}_C = \left(\frac{10.00}{19}\right)^5 \left(\frac{1}{0.40}\right) = 0.04035 \times 2.50 = 0.1009$

### Solution, step 3: Diagnostic synthesis and comparative interpretation
With $n = 25$ and $p = 5$, the diagnostic cutoffs are $h_{\text{cut}} = \frac{2p}{n} = 0.40$, $D_{\text{cut}} = 1.00$ (or $4/n = 0.16$), $|\text{DFFITS}|_{\text{cut}} = 2\sqrt{p/n} = 2\sqrt{0.20} = 0.8944$, and $|\text{COVRATIO} - 1|_{\text{cut}} = \frac{3p}{n} = 0.60$ (i.e., outside $[0.40, 1.60]$):

- **Case A (Pure Vertical Outlier, Low Leverage)**: Because $h_{AA} = 0.10 \ll 0.40$, Case A sits near the center of the predictors. Even though it is a severe vertical outlier ($t_A = 4.3589$) that drastically inflates $s^2$ ($\text{COVRATIO}_A = 0.0448 \ll 0.40$), its Cook's Distance is modest ($D_A = 0.2222 < 1.0$) because it exerts almost no rotational torque on the slopes!
- **Case B (Good High-Leverage Point)**: Case B has very high leverage ($h_{BB} = 0.75 > 0.40$), but its studentized residual is small ($t_B = 0.7925$). Consequently, $D_B = 0.3840 < 1.0$, and $\text{COVRATIO}_B = 4.3935 \gg 1.60$ shows that Case B **substantially improves** parameter precision by expanding the predictor span!
- **Case C (Bad High-Leverage Influential Point)**: Notice that Case C has a smaller raw residual ($e_C = 4.00$) than Case A ($e_A = 6.00$) and identical studentized residuals ($r_C = r_A = 3.1623$, $t_C = t_A = 4.3589$), yet because Case C also has high leverage ($h_{CC} = 0.60 > 0.40$), its Cook's Distance is **13.5 times larger** ($D_C = 3.0000 \gg 1.0$, $\text{DFFITS}_C = 5.3385$). Case C severely distorts both $\hat{\boldsymbol{\beta}}$ and $s^2$ and must be audited for measurement error or modeled via robust regression.

## Fully worked question 2: Exact Algebraic Proofs of Deletion Identities: PRESS Residual e_(i), Leave-One-Out SSE_(i), and Bounds on Hat Diagonals

### Question
Let $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ be a full-rank linear regression model ($\text{rank}(\mathbf{X}) = p < n$) with Hat matrix $\mathbf{H} = \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T$ and leverages $h_{ii} = \mathbf{x}_i^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i < 1$.

1. Starting from the Sherman–Morrison–Woodbury formula $(\mathbf{X}_{(i)}^T\mathbf{X}_{(i)})^{-1} = (\mathbf{X}^T\mathbf{X})^{-1} + \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1}}{1 - h_{ii}}$, prove step-by-step that $\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)} = \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i e_i}{1 - h_{ii}}$ and $e_{(i)} = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)} = \frac{e_i}{1 - h_{ii}}$.
2. Prove the exact leave-one-out Residual Sum of Squares identity:
   $$\text{SSE} - \text{SSE}_{(i)} = \frac{e_i^2}{1 - h_{ii}}$$
3. Using the identity in Part 2, prove that the squared internally studentized residual satisfies $0 \le \frac{r_i^2}{n - p} \le 1$, and derive the algebraic relationship expressing $t_i$ as a monotonic function of $r_i$.

### Solution, step 1: Prove the leave-one-out parameter update and PRESS residual identity
By definition of the leave-one-out OLS estimator on the $n - 1$ observations with row $i$ removed, $\hat{\boldsymbol{\beta}}_{(i)} = (\mathbf{X}_{(i)}^T \mathbf{X}_{(i)})^{-1} \mathbf{X}_{(i)}^T \mathbf{Y}_{(i)}$, where $\mathbf{X}_{(i)}^T \mathbf{Y}_{(i)} = \mathbf{X}^T\mathbf{Y} - \mathbf{x}_i Y_i$. Substituting the Sherman–Morrison–Woodbury inverse gives:

$$\hat{\boldsymbol{\beta}}_{(i)} = \left[ (\mathbf{X}^T\mathbf{X})^{-1} + \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1}}{1 - h_{ii}} \right] (\mathbf{X}^T\mathbf{Y} - \mathbf{x}_i Y_i)$$

Expanding the product and using $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$, $\mathbf{x}_i^T \hat{\boldsymbol{\beta}} = \hat{Y}_i$, and $\mathbf{x}_i^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i = h_{ii}$:

$$\hat{\boldsymbol{\beta}}_{(i)} = \hat{\boldsymbol{\beta}} - (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i Y_i + \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i \hat{Y}_i}{1 - h_{ii}} - \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i h_{ii} Y_i}{1 - h_{ii}}$$

Factor out $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i$ from the last three terms over the common denominator $1 - h_{ii}$:

$$\hat{\boldsymbol{\beta}}_{(i)} = \hat{\boldsymbol{\beta}} - (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i \left[ \frac{(1 - h_{ii}) Y_i - \hat{Y}_i + h_{ii} Y_i}{1 - h_{ii}} \right] = \hat{\boldsymbol{\beta}} - \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i (Y_i - \hat{Y}_i)}{1 - h_{ii}} = \hat{\boldsymbol{\beta}} - \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i e_i}{1 - h_{ii}}$$

Rearranging gives $\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)} = \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i e_i}{1 - h_{ii}}$. Now premultiply by $\mathbf{x}_i^T$:

$$\hat{Y}_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)} = \frac{\mathbf{x}_i^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i e_i}{1 - h_{ii}} = \frac{h_{ii} e_i}{1 - h_{ii}}$$

Adding $e_i = Y_i - \hat{Y}_i$ to both sides yields the exact PRESS residual identity:

$$e_{(i)} = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}_{(i)} = e_i + \frac{h_{ii} e_i}{1 - h_{ii}} = \frac{e_i}{1 - h_{ii}}$$

### Solution, step 2: Prove the leave-one-out Residual Sum of Squares identity SSE - SSE_(i) = e_i^2 / (1 - h_ii)
Write out the leave-one-out Residual Sum of Squares $\text{SSE}_{(i)} = \sum_{j \neq i} (Y_j - \mathbf{x}_j^T \hat{\boldsymbol{\beta}}_{(i)})^2$ by summing over all $n$ observations and subtracting the $i$-th term $e_{(i)}^2$:

$$\text{SSE}_{(i)} = \left\| \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}_{(i)} \right\|_2^2 - e_{(i)}^2 = \left\| (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) + \mathbf{X}(\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)}) \right\|_2^2 - e_{(i)}^2$$

Because $\mathbf{e} = \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}$ is orthogonal to $\mathcal{C}(\mathbf{X})$ ($\mathbf{X}^T\mathbf{e} = \mathbf{0}_p$), the cross-term vanishes and Pythagoras gives:

$$\text{SSE}_{(i)} = \|\mathbf{e}\|_2^2 + (\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)})^T (\mathbf{X}^T\mathbf{X}) (\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)}) - e_{(i)}^2$$

Substitute $\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(i)} = \frac{(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i e_i}{1 - h_{ii}}$ and $e_{(i)} = \frac{e_i}{1 - h_{ii}}$:

$$\text{SSE}_{(i)} = \text{SSE} + \frac{e_i^2 \, \mathbf{x}_i^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_i}{(1 - h_{ii})^2} - \frac{e_i^2}{(1 - h_{ii})^2} = \text{SSE} + \frac{h_{ii} e_i^2 - e_i^2}{(1 - h_{ii})^2} = \text{SSE} - \frac{(1 - h_{ii}) e_i^2}{(1 - h_{ii})^2} = \text{SSE} - \frac{e_i^2}{1 - h_{ii}}$$

Therefore, $\text{SSE} - \text{SSE}_{(i)} = \frac{e_i^2}{1 - h_{ii}}$.

### Solution, step 3: Establish bounds on r_i^2 and the monotonic transformation to t_i
Because $\text{SSE}_{(i)} = \sum_{j \neq i} (Y_j - \mathbf{x}_j^T \hat{\boldsymbol{\beta}}_{(i)})^2 \ge 0$ is a sum of squares of real numbers, the identity $\text{SSE}_{(i)} = \text{SSE} - \frac{e_i^2}{1 - h_{ii}}$ immediately implies:

$$0 \le \frac{e_i^2}{1 - h_{ii}} \le \text{SSE} = (n - p) s^2$$

Dividing through by $(n - p)s^2 > 0$ gives:

$$0 \le \frac{e_i^2}{(n - p) s^2 (1 - h_{ii})} = \frac{r_i^2}{n - p} \le 1 \implies |r_i| \le \sqrt{n - p}$$

Furthermore, dividing $\text{SSE}_{(i)} = (n - p)s^2 - s^2 r_i^2 = s^2(n - p - r_i^2)$ by $n - p - 1$ gives $s_{(i)}^2 = s^2 \left(\frac{n - p - r_i^2}{n - p - 1}\right)$, and substituting $s_{(i)}$ into $t_i = \frac{e_i}{s_{(i)}\sqrt{1 - h_{ii}}} = r_i \left(\frac{s}{s_{(i)}}\right)$ yields:

$$t_i = r_i \sqrt{\frac{n - p - 1}{n - p - r_i^2}}, \qquad r_i^2 = \frac{(n - p) t_i^2}{n - p - 1 + t_i^2}$$

showing that $t_i$ is a strictly increasing one-to-one function of $r_i$ that maps the bounded interval $(-\sqrt{n-p}, +\sqrt{n-p})$ onto the entire real line $(-\infty, +\infty)$.

## Fully worked question 3: Formal ANOVA Lack-of-Fit F-Test with Replicated Observations & Theoretical Maximum R^2

### Question
A biochemical engineer fits a simple linear regression model $Y = \beta_0 + \beta_1 x + \varepsilon$ to $n = 10$ observations measured across $c = 4$ distinct substrate concentrations $x \in \{1, 2, 3, 4\}$:
- At $x_1 = 1$ ($n_1 = 2$): $y_{11} = 2.8, \; y_{12} = 3.2$
- At $x_2 = 2$ ($n_2 = 3$): $y_{21} = 6.7, \; y_{22} = 7.0, \; y_{23} = 7.3$
- At $x_3 = 3$ ($n_3 = 3$): $y_{31} = 8.8, \; y_{32} = 9.0, \; y_{33} = 9.2$
- At $x_4 = 4$ ($n_4 = 2$): $y_{41} = 8.7, \; y_{42} = 9.3$

1. Compute the group means $\bar{y}_{1\cdot}, \bar{y}_{2\cdot}, \bar{y}_{3\cdot}, \bar{y}_{4\cdot}$, the overall sample means $\bar{x}, \bar{y}$, the corrected sums $S_{xx}, S_{yy}, S_{xy}$, and the OLS linear regression fit $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$. Determine $\text{SST}$, $\text{SSR}$, and $\text{SSE}$.
2. Partition $\text{SSE}$ into the **Pure Error Sum of Squares ($\text{SSPE}$)** and the **Lack-of-Fit Sum of Squares ($\text{SSLF}$)**, determine their degrees of freedom, and carry out the exact **Lack-of-Fit $F$-Test** at $\alpha = 0.05$ ($F_{0.05, 2, 6} = 5.143$).
3. Calculate the ordinary $R^2$ of the linear model and compare it against the theoretical **maximum achievable $R_{\max}^2$** for any regression function on this dataset. What does the discrepancy between $R^2$ and $R_{\max}^2$ reveal?

### Solution, step 1: Compute replicate group means, OLS linear fit, and SST, SSR, SSE
First, we evaluate the replicate group means $\bar{y}_{j\cdot}$ at each of the $c = 4$ substrate levels:
- $x_1 = 1$ ($n_1 = 2$): $\bar{y}_{1\cdot} = \frac{2.8 + 3.2}{2} = 3.00$
- $x_2 = 2$ ($n_2 = 3$): $\bar{y}_{2\cdot} = \frac{6.7 + 7.0 + 7.3}{3} = 7.00$
- $x_3 = 3$ ($n_3 = 3$): $\bar{y}_{3\cdot} = \frac{8.8 + 9.0 + 9.2}{3} = 9.00$
- $x_4 = 4$ ($n_4 = 2$): $\bar{y}_{4\cdot} = \frac{8.7 + 9.3}{2} = 9.00$

Across all $n = 10$ observations:
- $\sum x_{jm} = 2(1) + 3(2) + 3(3) + 2(4) = 2 + 6 + 9 + 8 = 25 \implies \bar{x} = 2.50$
- $\sum y_{jm} = 2(3.0) + 3(7.0) + 3(9.0) + 2(9.0) = 6 + 21 + 27 + 18 = 72 \implies \bar{y} = 7.20$
- $S_{xx} = 2(1 - 2.5)^2 + 3(2 - 2.5)^2 + 3(3 - 2.5)^2 + 2(4 - 2.5)^2 = 2(2.25) + 3(0.25) + 3(0.25) + 2(2.25) = 10.50$
- $S_{xy} = \sum_{j=1}^4 n_j (x_j - \bar{x})(\bar{y}_{j\cdot} - \bar{y}) = 2(-1.5)(-4.2) + 3(-0.5)(-0.2) + 3(0.5)(1.8) + 2(1.5)(1.8) = 12.6 + 0.3 + 2.7 + 5.4 = 21.00$

Therefore, the OLS slope and intercept are:

$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{21.00}{10.50} = 2.00, \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} = 7.20 - 2.00(2.50) = 2.20$$

giving $\hat{y} = 2.20 + 2.00 x$, with fitted group values $\hat{y}_1 = 4.20, \; \hat{y}_2 = 6.20, \; \hat{y}_3 = 8.20, \; \hat{y}_4 = 10.20$.
Next, the Regression Sum of Squares is $\text{SSR} = \hat{\beta}_1 S_{xy} = 2.00(21.00) = 42.00$, and we compute $\text{SSE}$ and $\text{SST}$ in Step 2.

### Solution, step 2: Partition SSE into Pure Error (SSPE) and Lack of Fit (SSLF) and perform the F-test
We compute the **Pure Error Sum of Squares ($\text{SSPE}$)** from the internal deviations $(y_{jm} - \bar{y}_{j\cdot})$ within each of the $c = 4$ groups:
- Level $1$ ($\bar{y}_{1\cdot} = 3.0$): $(-0.2)^2 + (0.2)^2 = 0.08$
- Level $2$ ($\bar{y}_{2\cdot} = 7.0$): $(-0.3)^2 + (0.0)^2 + (0.3)^2 = 0.18$
- Level $3$ ($\bar{y}_{3\cdot} = 9.0$): $(-0.2)^2 + (0.0)^2 + (0.2)^2 = 0.08$
- Level $4$ ($\bar{y}_{4\cdot} = 9.0$): $(-0.3)^2 + (0.3)^2 = 0.18$

$$\text{SSPE} = 0.08 + 0.18 + 0.08 + 0.18 = 0.52, \qquad \text{df}_{\text{PE}} = n - c = 10 - 4 = 6$$

$$\text{MSPE} = \frac{\text{SSPE}}{n - c} = \frac{0.52}{6} \approx 0.08667$$

Next, we compute the **Lack-of-Fit Sum of Squares ($\text{SSLF}$)** from the weighted squared deviations of the group means $\bar{y}_{j\cdot}$ around the linear fitted values $\hat{y}_j = 2.20 + 2.00 x_j$:

$$\text{SSLF} = \sum_{j=1}^4 n_j (\bar{y}_{j\cdot} - \hat{y}_j)^2 = 2(3.0 - 4.2)^2 + 3(7.0 - 6.2)^2 + 3(9.0 - 8.2)^2 + 2(9.0 - 10.2)^2$$

$$\text{SSLF} = 2(1.44) + 3(0.64) + 3(0.64) + 2(1.44) = 2.88 + 1.92 + 1.92 + 2.88 = 9.60, \qquad \text{df}_{\text{LF}} = c - p = 4 - 2 = 2$$

$$\text{MSLF} = \frac{\text{SSLF}}{c - p} = \frac{9.60}{2} = 4.80$$

Thus, $\text{SSE} = \text{SSLF} + \text{SSPE} = 9.60 + 0.52 = 10.12$ ($\text{df} = 8$), and $\text{SST} = \text{SSR} + \text{SSE} = 42.00 + 10.12 = 52.12$ ($\text{df} = 9$). The **Lack-of-Fit $F$-Statistic** is:

$$F_{\text{LF}} = \frac{\text{MSLF}}{\text{MSPE}} = \frac{4.80}{0.52 / 6} = \frac{28.80}{0.52} \approx 55.385$$

Since $F_{\text{LF}} = 55.385 \gg F_{0.05, 2, 6} = 5.143$, we strongly **reject the linear model**: the group means $(3.0, 7.0, 9.0, 9.0)$ exhibit pronounced quadratic/Michaelis–Menten saturation that a straight line cannot capture!

### Solution, step 3: Compare linear R^2 against theoretical maximum R_max^2
For the fitted straight line, the ordinary Coefficient of Determination is:

$$R_{\text{linear}}^2 = \frac{\text{SSR}}{\text{SST}} = \frac{42.00}{52.12} \approx 0.8058 \quad (80.58\%)$$

A naive analyst looking only at $R_{\text{linear}}^2 = 80.58\%$ (and the overall linear $F$-statistic $F = \frac{42.00/1}{10.12/8} = 33.20$) might conclude that the straight line fits well! However, the theoretical **maximum achievable $R_{\max}^2$** for any model on this dataset is:

$$R_{\max}^2 = 1 - \frac{\text{SSPE}}{\text{SST}} = \frac{52.12 - 0.52}{52.12} = \frac{51.60}{52.12} \approx 0.9900 \quad (99.00\%)$$

In fact, notice that the group means $\bar{y}_{j\cdot} = (3.0, 7.0, 9.0, 9.0)$ lie *exactly* on the quadratic parabola $y = -3.0 + 7.0 x - 1.0 x^2$, which achieves $\text{SSLF}_{\text{quad}} = 0$ and $R_{\text{quad}}^2 = R_{\max}^2 = 99.00\%$! Nearly $95\%$ of the residual sum of squares of the linear model ($\text{SSLF}/\text{SSE} = 9.60 / 10.12 = 94.86\%$) was systematic lack of fit rather than random noise.
