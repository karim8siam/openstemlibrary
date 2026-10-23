# Unit 7: Qualitative Predictors, Interaction Effects, Structural Breaks, Polynomial Splines & Model Selection

Dummy (indicator) variables for categorical factors, reference cell vs effects coding, and avoidance of the Dummy Variable Trap; Interaction terms between continuous and categorical predictors, Analysis of Covariance (ANCOVA), and Chow Test for structural stability across regimes; Polynomial regression, ill-conditioning of Vandermonde power bases, Forsythe orthogonal polynomials, piecewise linear segmented regression, and cubic B-splines; Variance-stabilizing and linearizing transformations: Box-Cox power family y^(lambda) and profile log-likelihood estimation of lambda; Variable selection and information criteria: Adjusted R^2, Mallows' C_p, PRESS statistic, Akaike Information Criterion (AIC), Bayesian Information Criterion (BIC), and stepwise/all-subsets algorithms.

## 7.1 Qualitative Predictors, Dummy Variable Encodings, Reference Cell vs Effects Coding, and the Dummy Variable Trap

In classical regression modeling, the columns of the design matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ must be numerical vectors, yet many important explanatory factors in economics, biostatistics, sociology, and quality engineering are **qualitative (categorical or nominal) variables** possessing $G \ge 2$ discrete, unordered categories or levels $\{C_1, C_2, \dots, C_G\}$. Assigning arbitrary consecutive integers $1, 2, \dots, G$ to a nominal variable inside a single regression column would impose a false metric assumption that the difference between category $1$ and category $2$ is identical in magnitude and direction to the difference between category $2$ and category $3$.

To incorporate a $G$-level qualitative factor into a linear regression model without imposing any artificial ordering or metric spacing among the categories, we construct **indicator (dummy) variables**. For a qualitative factor with $G$ mutually exclusive and exhaustive levels, we introduce $G - 1$ binary indicator variables $D_1, D_2, \dots, D_{G-1}$ alongside the model intercept $\beta_0$. Under the standard **Reference Cell (or Corner-Point) Coding** convention, one category—say $C_G$ (or $C_1$)—is designated as the **baseline reference group** and assigned zeros across all $G - 1$ indicators, while each remaining category $C_g$ ($g = 1, \dots, G - 1$) activates its corresponding indicator:

$$D_{ig} = \begin{cases} 1, & \text{if observation } i \text{ belongs to category } C_g \\ 0, & \text{otherwise} \end{cases} \qquad (g = 1, 2, \dots, G - 1)$$

When these $G - 1$ dummy variables are included alongside a continuous covariate $X_i$ in an additive multiple regression model:

$$Y_i = \beta_0 + \beta_1 x_i + \gamma_1 D_{i1} + \gamma_2 D_{i2} + \dots + \gamma_{G-1} D_{i, G-1} + \varepsilon_i$$

evaluating the conditional expectation function $\mathbb{E}[Y_i \mid x_i, \text{Group}]$ for each category reveals the exact structural interpretation of every parameter:
- **Reference Category $C_G$ ($D_{i1} = \dots = D_{i, G-1} = 0$)**: $\mathbb{E}[Y_i \mid x_i, C_G] = \beta_0 + \beta_1 x_i$. Thus, $\beta_0$ is the baseline intercept for the reference category $C_G$.
- **Category $C_g$ ($D_{ig} = 1$, all other $D_{im} = 0$)**: $\mathbb{E}[Y_i \mid x_i, C_g] = (\beta_0 + \gamma_g) + \beta_1 x_i$. Thus, $\gamma_g = \mathbb{E}[Y \mid x, C_g] - \mathbb{E}[Y \mid x, C_G]$ measures the **vertical parallel shift (differential intercept)** between category $C_g$ and the reference category $C_G$ holding the continuous predictor $x$ constant! Moreover, the contrast between any two non-reference categories $C_g$ and $C_m$ is simply $\gamma_g - \gamma_m$, with standard error $s\sqrt{c_{gg} + c_{mm} - 2c_{gm}}$.

### The Dummy Variable Trap (Exact Linear Collinearity)
Why must a model with an intercept $\beta_0$ include **at most $G - 1$** dummy variables for a $G$-level factor rather than all $G$ indicators $D_1, \dots, D_G$? Because the $G$ categories are mutually exclusive and exhaustive, every observation $i = 1, \dots, n$ belongs to exactly one category, which forces the pointwise algebraic identity:

$$\sum_{g=1}^G D_{ig} = D_{i1} + D_{i2} + \dots + D_{iG} = 1 = x_{i0} \quad \forall i = 1, 2, \dots, n$$

In vector notation, the sum of all $G$ indicator columns equals the intercept column of ones: $\sum_{g=1}^G \mathbf{d}_{(g)} = \mathbf{1}_n$. If an analyst includes both the intercept column $\mathbf{1}_n$ and all $G$ dummy columns in $\mathbf{X}$, the columns of $\mathbf{X}$ are linearly dependent ($\text{rank}(\mathbf{X}) = G < G + 1$), the Gram matrix $\mathbf{X}^T\mathbf{X}$ is strictly singular ($\det(\mathbf{X}^T\mathbf{X}) = 0$), and unique Ordinary Least Squares estimation collapses! This exact collinearity pathology is universally known in econometrics as the **Dummy Variable Trap**.

There are three mathematically equivalent ways to avoid the Dummy Variable Trap:
1. **Reference Cell Coding ($1$ Intercept $+$ $G - 1$ Dummies)**: Retain $\beta_0$ and omit one reference dummy $D_G$ (equivalent to imposing the corner-point constraint $\gamma_G = 0$).
2. **Cell-Means Coding (No Intercept $+$ All $G$ Dummies)**: Omit the intercept $\beta_0$ and include all $G$ indicator columns $D_1, \dots, D_G$:
   $$Y_i = \mu_1 D_{i1} + \mu_2 D_{i2} + \dots + \mu_G D_{iG} + \beta_1 x_i + \varepsilon_i$$
   Because the $G$ dummy columns are mutually orthogonal ($\mathbf{d}_{(g)}^T \mathbf{d}_{(m)} = 0$ for $g \neq m$ and $\mathbf{d}_{(g)}^T \mathbf{d}_{(g)} = n_g$), this parameterization is full rank and estimates each group's intercept $\mu_g = \beta_0 + \gamma_g$ directly.
3. **Effects (Sum-to-Zero / Deviation) Coding**: Retain the grand intercept $\mu_0$ and define $G - 1$ contrast variables $E_{ig} \in \{-1, 0, +1\}$ corresponding to the ANOVA zero-sum restriction $\sum_{g=1}^G \alpha_g = 0$ (so $\alpha_G = -\sum_{g=1}^{G-1} \alpha_g$):
   $$E_{ig} = D_{ig} - D_{iG} = \begin{cases} +1, & \text{if observation } i \in C_g \\ -1, & \text{if observation } i \in C_G \\ 0, & \text{otherwise} \end{cases} \qquad (g = 1, \dots, G - 1)$$
   Under effects coding, the intercept $\mu_0 = \frac{1}{G}\sum_{g=1}^G \mu_g$ represents the unweighted grand mean across all $G$ categories, and each coefficient $\alpha_g = \mu_g - \mu_0$ measures the deviation of category $C_g$ from the unweighted grand mean rather than from a single reference cell.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Coding Scheme</th><th>Design Columns Included</th><th>Intercept Meaning</th><th>Slope Coefficient $\gamma_g$ Meaning</th></tr>
</thead>
<tbody>
<tr><td><strong>Reference Cell Coding</strong></td><td>$\mathbf{1}_n$ and $D_1, \dots, D_{G-1}$ ($D_G$ omitted)</td><td>$\beta_0 = \mu_G$ (mean of baseline reference group $C_G$ at $x=0$)</td><td>$\gamma_g = \mu_g - \mu_G$ (contrast of group $g$ against baseline $G$)</td></tr>
<tr><td><strong>Cell-Means Coding</strong></td><td>$D_1, D_2, \dots, D_G$ (no $\mathbf{1}_n$ column)</td><td>None (replaced by $G$ group intercepts $\mu_1, \dots, \mu_G$)</td><td>$\mu_g$ (direct group-specific intercept for category $C_g$ at $x=0$)</td></tr>
<tr><td><strong>Effects (Sum-to-Zero) Coding</strong></td><td>$\mathbf{1}_n$ and $E_g = D_g - D_G$ ($g=1,\dots,G-1$)</td><td>$\mu_0 = \frac{1}{G}\sum_{g=1}^G \mu_g$ (unweighted grand mean across groups)</td><td>$\alpha_g = \mu_g - \mu_0$ (deviation of group $g$ from grand mean; $\alpha_G = -\sum_{g=1}^{G-1} \alpha_g$)</td></tr>
</tbody>
</table></div>

Crucially, because all three coding schemes span the exact same $G$-dimensional column space $\mathcal{C}(\mathbf{d}_{(1)}, \dots, \mathbf{d}_{(G)})$, the projection matrix $\mathbf{H}$, the fitted values $\hat{\mathbf{Y}}$, the residuals $\mathbf{e}$, and the $\text{SSE}$ are strictly identical across all three parameterizations!

## 7.2 Interaction Effects, Analysis of Covariance (ANCOVA), and the Chow Test for Structural Stability

The additive dummy-variable model of Section 7.1 assumes that the marginal effect $\beta_1 = \frac{\partial \mathbb{E}[Y \mid x, D]}{\partial x}$ of the continuous predictor $X$ is identical across all $G$ qualitative groups, producing $G$ **parallel regression lines** that differ only in their vertical intercepts. In statistical biometry and experimental design, this parallel-lines specification is the classical **Analysis of Covariance (ANCOVA)** model: by adjusting for a continuous baseline concomitant variable $X$ (such as pre-treatment blood pressure or initial plot fertility) that is unaffected by the treatment, ANCOVA removes within-group error variance, reduces $\text{MSE}$, and adjusts treatment group comparisons $\hat{\gamma}_g = (\bar{Y}_{g\cdot} - \bar{Y}_{G\cdot}) - \hat{\beta}_1 (\bar{x}_{g\cdot} - \bar{x}_{G\cdot})$ for baseline covariate imbalances.

However, in many scientific settings, the slope with respect to $X$ varies across qualitative categories—an effect known as a **qualitative-by-quantitative interaction** (or **moderation / non-parallelism**). Geometrically, an interaction means that the partial derivative of $\mathbb{E}[Y \mid X_1, X_2]$ with respect to one predictor depends on the level of another predictor. Forming the cross-product interaction terms $(D_{ig} x_i)$ for $g = 1, \dots, G - 1$ yields the **Unrestricted Separate-Regressions (Interaction) Model**:

$$Y_i = \beta_0 + \beta_1 x_i + \sum_{g=1}^{G-1} \gamma_g D_{ig} + \sum_{g=1}^{G-1} \delta_g (D_{ig} x_i) + \varepsilon_i$$

Evaluating the conditional expectation function within each category reveals how both the intercept and the slope shift across regimes:
- **Reference Group $C_G$**: $\mathbb{E}[Y_i \mid x_i, C_G] = \beta_0 + \beta_1 x_i$ (intercept $\beta_0$, slope $\beta_1$).
- **Group $C_g$ ($g = 1, \dots, G - 1$)**: $\mathbb{E}[Y_i \mid x_i, C_g] = (\beta_0 + \gamma_g) + (\beta_1 + \delta_g) x_i$ (intercept $\beta_0 + \gamma_g$, slope $\beta_1 + \delta_g$).

Here, $\gamma_g$ is the **differential intercept** and $\delta_g$ is the **differential slope** of group $g$ relative to the reference group $G$. This nested hierarchy enables three distinct General Linear Hypothesis $F$-tests:
1. **Test for Homogeneity of Slopes (Parallelism / No Interaction)**: $H_0: \delta_1 = \delta_2 = \dots = \delta_{G-1} = 0$ ($q = G - 1$ degrees of freedom), comparing the Full interaction model against the Reduced parallel-lines ANCOVA model.
2. **Test for Equal Group Intercepts Given Parallelism (ANCOVA Treatment Effect)**: Assuming parallelism holds, $H_0: \gamma_1 = \dots = \gamma_{G-1} = 0$ ($q = G - 1$ degrees of freedom).
3. **Test for Complete Coincidence of All $G$ Regression Lines**: $H_0: \gamma_1 = \dots = \gamma_{G-1} = \delta_1 = \dots = \delta_{G-1} = 0$ ($q = 2(G - 1)$ degrees of freedom), testing whether a single pooled regression line $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ holds across all $G$ groups.

### The Chow Test for Structural Stability Across Regimes ($p$ Parameters)
In macroeconomics, finance, and policy evaluation, an investigator often divides a sample of size $n = n_1 + n_2$ into two regimes—such as pre-policy vs. post-policy periods ($t = 1, \dots, n_1$ and $t = n_1 + 1, \dots, n$), or urban vs. rural households—and wishes to test whether the entire $p \times 1$ regression parameter vector remains structurally stable across the two regimes:

$$\begin{aligned}
\text{Regime 1 } (n_1 \text{ obs}): \quad \mathbf{Y}_1 &= \mathbf{X}_1 \boldsymbol{\beta}_{(1)} + \boldsymbol{\varepsilon}_1 \\
\text{Regime 2 } (n_2 \text{ obs}): \quad \mathbf{Y}_2 &= \mathbf{X}_2 \boldsymbol{\beta}_{(2)} + \boldsymbol{\varepsilon}_2
\end{aligned} \qquad H_0: \boldsymbol{\beta}_{(1)} = \boldsymbol{\beta}_{(2)} = \boldsymbol{\beta} \quad (\text{Structural Stability})$$

Assuming homoscedastic, independent normal disturbances $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$ across both regimes with $n_1 > p$ and $n_2 > p$, **Gregory Chow (1960)** showed that testing $H_0: \boldsymbol{\beta}_{(1)} = \boldsymbol{\beta}_{(2)}$ is a General Linear $F$-test with $q = p$ restrictions:
- **Reduced (Pooled) Model**: Fit a single regression to all $n = n_1 + n_2$ observations pooled together to obtain the pooled residual sum of squares $\text{SSE}_R = \text{SSE}_{\text{pooled}}$ with $\text{df}_R = n_1 + n_2 - p$ degrees of freedom.
- **Full (Unrestricted Separate Regimes) Model**: Fit the regression separately to Regime 1 (yielding $\text{SSE}_1$ with $n_1 - p$ df) and separately to Regime 2 (yielding $\text{SSE}_2$ with $n_2 - p$ df). Because the two regimes have zero overlapping parameters in the unrestricted block-diagonal model $\begin{pmatrix} \mathbf{Y}_1 \\ \mathbf{Y}_2 \end{pmatrix} = \begin{pmatrix} \mathbf{X}_1 & \mathbf{0} \\ \mathbf{0} & \mathbf{X}_2 \end{pmatrix} \begin{pmatrix} \boldsymbol{\beta}_{(1)} \\ \boldsymbol{\beta}_{(2)} \end{pmatrix} + \boldsymbol{\varepsilon}$, the unrestricted Full-model residual sum of squares is simply the sum $\text{SSE}_F = \text{SSE}_1 + \text{SSE}_2$ with $\text{df}_F = (n_1 - p) + (n_2 - p) = n - 2p$ degrees of freedom!

Notice that this block-diagonal model is **algebraically identical** to defining a regime dummy $D_i \in \{0, 1\}$ and interacting $D_i$ with the intercept and all $k = p - 1$ predictors in a single pooled equation! Therefore, the exact **Chow Structural Break $F$-Statistic** is:

$$F_{\text{Chow}} = \frac{\left[ \text{SSE}_{\text{pooled}} - (\text{SSE}_1 + \text{SSE}_2) \right] / p}{(\text{SSE}_1 + \text{SSE}_2) / (n_1 + n_2 - 2p)} \sim F_{p, \, n_1 + n_2 - 2p} \quad \text{under } H_0$$

*(Note: If the second regime has fewer observations than parameters, $n_2 \le p$, $\text{SSE}_2$ cannot be estimated separately; in that case, Chow's **Predictive Stability Test** compares $\text{SSE}_{\text{pooled}} - \text{SSE}_1$ against $\text{SSE}_1 / (n_1 - p)$ using an $F_{n_2, \, n_1 - p}$ distribution).*

## 7.3 Polynomial Regression, Vandermonde Ill-Conditioning, and Forsythe Orthogonal Polynomials

When theoretical considerations or residual plots indicate that the conditional expectation function $\mu(x) = \mathbb{E}[Y \mid X = x]$ is a smooth curve rather than a straight line, the classical Weierstrass Approximation Theorem motivates approximating $\mu(x)$ on a bounded interval by a **$d$-th degree Polynomial Regression Model**:

$$Y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \dots + \beta_d x_i^d + \varepsilon_i, \quad i = 1, 2, \dots, n$$

Even though $\mu(x)$ is a nonlinear curve in $x$, the polynomial regression model is **strictly linear in the unknown parameter vector** $\boldsymbol{\beta} = (\beta_0, \beta_1, \dots, \beta_d)^T \in \mathbb{R}^{d+1}$! Defining the $n \times (d + 1)$ **Vandermonde Design Matrix** $\mathbf{X}$ with entries $X_{ij} = x_i^j$ ($j = 0, 1, \dots, d$) casts polynomial regression directly into the standard multiple linear regression apparatus $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$.

### Two Critical Statistical and Numerical Principles in Polynomial Regression
1. **The Hierarchy (Marginalitya) Principle**: Because transforming the origin of $x$ via $x^* = x - c$ expands $(x^* + c)^2 = (x^*)^2 + 2c x^* + c^2$, a quadratic polynomial without a linear term ($\beta_1 = 0$) in one coordinate system acquires a non-zero linear term in every shifted coordinate system! To ensure that the fitted curve is invariant to linear shifts of scale and origin, polynomial models must respect the **hierarchical inclusion principle**: whenever a higher-order power $x^d$ is retained in the model, all lower-order powers $1, x, x^2, \dots, x^{d-1}$ should be retained even if one of their individual $t$-statistics is small, and model degree $d$ should be selected via sequential (Type I) sums of squares $\text{SSR}(x^d \mid x, \dots, x^{d-1})$.
2. **Severe Multicollinearity and Ill-Conditioning of the Raw Vandermonde Basis**: When $x_i > 0$ (for instance, years $x_i \in [2000, 2025]$ or temperatures $x_i \in [300, 400]$), the raw power columns $x_i, x_i^2, x_i^3$ are almost perfectly linearly correlated ($r(x, x^2) > 0.99$)! Even on $[0, 1]$, the continuous limit of $\frac{1}{n}\mathbf{X}^T\mathbf{X}$ as $n \to \infty$ is the notorious **Hilbert matrix** $H_{jk} = \int_0^1 x^{j+k} dx = \frac{1}{j + k + 1}$, whose condition number grows exponentially ($\kappa(\mathbf{H}_5) \approx 4.8 \times 10^5$), causing severe variance inflation and catastrophic numerical instability for $d \ge 4$.

### Centering and Forsythe–Gram–Schmidt Orthogonal Polynomials
A simple first remedy is **mean-centering** the predictor via $\tilde{x}_i = x_i - \bar{x}$ (or scaling to $[-1, 1]$) before raising to powers: $Y_i = \alpha_0 + \alpha_1 \tilde{x}_i + \alpha_2 \tilde{x}_i^2 + \dots + \alpha_d \tilde{x}_i^d + \varepsilon_i$. For any symmetric design around $\bar{x}$, odd and even powers of $\tilde{x}_i$ are strictly orthogonal ($\sum \tilde{x}_i^{2m-1} \tilde{x}_i^{2r} = 0$), immediately eliminating the correlation between $\tilde{x}_i$ and $\tilde{x}_i^2$!

To achieve **complete mutual orthogonality** across *all* degrees $j = 0, 1, \dots, d$ for any arbitrary spacing of sample points $x_1, \dots, x_n$, we replace the raw monomials $\{1, x, x^2, \dots, x^d\}$ by **Discrete Orthogonal Polynomials** $\{P_0(x), P_1(x), \dots, P_d(x)\}$, where $P_j(x)$ is a monic polynomial of exact degree $j$ satisfying the sample orthogonality condition:

$$\sum_{i=1}^n P_j(x_i) P_m(x_i) = 0 \quad \forall j \neq m$$

Using **Forsythe's (1957) Three-Term Recurrence Relation** (discrete Gram–Schmidt orthogonalization), the orthogonal polynomials are generated recursively without ever forming ill-conditioned moments:
- **Degree $0$**: $P_0(x_i) = 1$ for all $i = 1, \dots, n$.
- **Degree $1$**: $P_1(x_i) = x_i - \bar{x}$ (since $\sum P_0(x_i) P_1(x_i) = \sum (x_i - \bar{x}) = 0$).
- **Degree $j \ge 2$**:
  $$P_j(x_i) = (x_i - a_j) P_{j-1}(x_i) - b_j P_{j-2}(x_i)$$
  where the recurrence constants $a_j$ and $b_j$ are chosen so that $\sum_{i=1}^n P_j(x_i) P_{j-1}(x_i) = 0$ and $\sum_{i=1}^n P_j(x_i) P_{j-2}(x_i) = 0$ (and by induction $\sum P_j(x_i) P_m(x_i) = 0$ for all $m < j$):

$$a_j = \frac{\sum_{i=1}^n x_i \left[P_{j-1}(x_i)\right]^2}{\sum_{i=1}^n \left[P_{j-1}(x_i)\right]^2}, \qquad b_j = \frac{\sum_{i=1}^n x_i P_{j-1}(x_i) P_{j-2}(x_i)}{\sum_{i=1}^n \left[P_{j-2}(x_i)\right]^2} = \frac{\sum_{i=1}^n \left[P_{j-1}(x_i)\right]^2}{\sum_{i=1}^n \left[P_{j-2}(x_i)\right]^2}$$

In the orthogonal polynomial regression model $Y_i = \gamma_0 P_0(x_i) + \gamma_1 P_1(x_i) + \dots + \gamma_d P_d(x_i) + \varepsilon_i$, the Gram matrix $\mathbf{P}^T\mathbf{P} = \text{diag}(\sum P_0^2, \sum P_1^2, \dots, \sum P_d^2)$ is **strictly diagonal**! Consequently:

$$\hat{\gamma}_j = \frac{\sum_{i=1}^n P_j(x_i) Y_i}{\sum_{i=1}^n \left[P_j(x_i)\right]^2}, \qquad \text{Var}(\hat{\gamma}_j) = \frac{\sigma^2}{\sum_{i=1}^n \left[P_j(x_i)\right]^2}, \qquad \text{SSR}(P_j) = \hat{\gamma}_j^2 \sum_{i=1}^n \left[P_j(x_i)\right]^2$$

Because the columns are mutually orthogonal, adding a higher-degree polynomial $P_{d+1}(x)$ **never alters the previously computed estimates** $\hat{\gamma}_0, \hat{\gamma}_1, \dots, \hat{\gamma}_d$ or their sums of squares $\text{SSR}(P_j)$!

## 7.4 Piecewise Linear Segmented Regression, Truncated Power Bases, and Cubic Regression Splines

High-degree global polynomials ($d \ge 4$) suffer from a well-known analytical pathology known as **Runge's Phenomenon**: because a single global polynomial is infinitely rigid (analytic everywhere), a local perturbation or outlier near one end of the predictor domain induces wild, non-local oscillations across the entire interval, and polynomial tails diverge rapidly to $\pm\infty$ at the boundaries. When the underlying physical or biological mechanism changes slope smoothly or abruptly at interior threshold values, **piecewise polynomials and regression splines** provide flexible, locally adaptable curves within the exact linear regression framework.

### 1. Piecewise Linear (Broken-Stick / Segmented) Regression at a Known Knot $\xi$
Suppose the linear slope of $Y$ on $x$ changes at a known threshold (**knot** or **join point**) $x = \xi$ (for example, material yield above a critical stress $\xi$, or electricity demand above a comfort temperature $\xi = 22^\circ\text{C}$). If we fitted two completely separate regressions on $x \le \xi$ and $x > \xi$ using a step dummy $D_i = \mathbb{I}(x_i > \xi)$, the fitted function would suffer an unphysical vertical jump discontinuity at $x = \xi$ unless constrained. To guarantee **exact $C^0$ continuity** at the knot $x = \xi$ while allowing the slope to change from $\beta_1$ (for $x < \xi$) to $\beta_1 + \beta_2$ (for $x > \xi$), we define the **hinge function** (or degree-$1$ truncated power basis function, identical to the ReLU activation function in modern deep learning):

$$(x - \xi)_+ = \max(0, x - \xi) = \begin{cases} 0, & \text{if } x \le \xi \\ x - \xi, & \text{if } x > \xi \end{cases}$$

The **Continuous Piecewise Linear Regression Model** is then a standard two-predictor linear regression:

$$Y_i = \beta_0 + \beta_1 x_i + \beta_2 (x_i - \xi)_+ + \varepsilon_i$$

Let us verify continuity and slope interpretation on both sides of the knot $\xi$:
- **Left Regime ($x \le \xi$)**: $(x - \xi)_+ = 0 \implies \mathbb{E}[Y \mid x] = \beta_0 + \beta_1 x$ (slope is $\beta_1$). Approaching the knot from the left gives $\lim_{x \to \xi^-} \mathbb{E}[Y \mid x] = \beta_0 + \beta_1 \xi$.
- **Right Regime ($x > \xi$)**: $(x - \xi)_+ = x - \xi \implies \mathbb{E}[Y \mid x] = (\beta_0 - \beta_2 \xi) + (\beta_1 + \beta_2) x$ (slope is $\beta_1 + \beta_2$). Approaching the knot from the right gives $\lim_{x \to \xi^+} \mathbb{E}[Y \mid x] = \beta_0 + \beta_1 \xi + \beta_2(\xi - \xi) = \beta_0 + \beta_1 \xi$.
Both limits match at $x = \xi$, and testing $H_0: \beta_2 = 0$ via an ordinary $t$-test directly tests whether the slope changes at $\xi$!

### 2. Cubic Regression Splines and the Truncated Power Basis ($C^2$ Smoothness)
In general, a **degree-$d$ regression spline** with $K$ interior knots $\xi_1 < \xi_2 < \dots < \xi_K$ is a piecewise degree-$d$ polynomial on each subinterval $[\xi_k, \xi_{k+1}]$ that is constrained to be continuous together with its first $d - 1$ derivatives ($C^{d-1}$ smooth) at every knot $\xi_k$. The most widely used choice is the **Cubic Regression Spline ($d = 3$)**, which is continuous in value ($f(\xi_k^-) = f(\xi_k^+)$), first derivative/slope ($f'(\xi_k^-) = f'(\xi_k^+)$), and second derivative/curvature ($f''(\xi_k^-) = f''(\xi_k^+)$) at every knot, making the joins imperceptible to the human eye.

How many free linear parameters does a cubic spline with $K$ knots possess? In the **Truncated Power Basis**, we start with the global cubic polynomial $1, x, x^2, x^3$ ($4$ parameters) and add one cubic truncated power function $(x - \xi_k)_+^3 = [\max(0, x - \xi_k)]^3$ at each knot $k = 1, \dots, K$:

$$Y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \beta_3 x_i^3 + \sum_{k=1}^K \theta_k (x_i - \xi_k)_+^3 + \varepsilon_i$$

Why does adding $(x - \xi_k)_+^3$ automatically preserve continuity of $f, f',$ and $f''$ while allowing the third derivative $f'''$ to jump by $6\theta_k$ at $x = \xi_k$? Because the function $h_k(x) = (x - \xi_k)_+^3$ has $h_k(\xi_k) = 0$, first derivative $h_k'(x) = 3(x - \xi_k)_+^2 \implies h_k'(\xi_k) = 0$, and second derivative $h_k''(x) = 6(x - \xi_k)_+ \implies h_k''(\xi_k) = 0$, while $h_k'''(x) = 6 \mathbb{I}(x > \xi_k)$ jumps by $6$! Thus, a cubic spline with $K$ interior knots is a linear regression model with exact dimension:

$$p = (d + 1) + K = 4 + K \quad \text{degrees of freedom}$$

In computational practice (Course Stat H-312), the truncated power basis columns $(x - \xi_k)_+^3$ become collinear for large $x$, so software replaces them with **Curry–Schoenberg B-Splines (Basis Splines)**—an algebraically equivalent basis spanning the exact same $(K + 4)$-dimensional spline subspace, where each B-spline basis function $B_m(x)$ is non-zero only on a compact local support of at most $d + 2 = 5$ adjacent knots, yielding a well-conditioned banded Gram matrix! Furthermore, **Natural Cubic Splines** impose the boundary constraint that the curve is linear ($f''(x) = f'''(x) = 0$) beyond the boundary knots $\xi_1$ and $\xi_K$, saving $4$ degrees of freedom (reducing dimension from $K + 4$ to $K$) and eliminating erratic boundary tail variance.

## 7.5 Variance-Stabilizing Transformations and the Box-Cox Power Transformation Family

When diagnostic residual plots reveal that the response variable $Y > 0$ violates both linearity and homoscedasticity/normality simultaneously—such as positive skewness coupled with an outward megaphone fan where $\text{Var}(Y_i)$ increases with the conditional mean $\mu_i = \mathbb{E}[Y_i \mid \mathbf{x}_i]$—transforming the response variable $Y \mapsto g(Y)$ often rectifies non-normality, heteroscedasticity, and nonlinearity in a single stroke.

### 1. First-Order Delta-Method Derivation of Variance-Stabilizing Transformations
Suppose $\mathbb{E}[Y_i] = \mu_i$ and the error standard deviation is a known function of the mean: $\text{Var}(Y_i) = \sigma^2 [h(\mu_i)]^2$. By a first-order Taylor expansion of a smooth transformation $g(Y_i)$ around $\mu_i$, $g(Y_i) \approx g(\mu_i) + g'(\mu_i)(Y_i - \mu_i)$, so the approximate variance of the transformed response is:

$$\text{Var}(g(Y_i)) \approx \left[ g'(\mu_i) \right]^2 \text{Var}(Y_i) = \sigma^2 \left[ g'(\mu_i) \, h(\mu_i) \right]^2$$

To make $\text{Var}(g(Y_i))$ approximately **constant** (independent of $\mu_i$), we choose $g(\mu)$ so that $g'(\mu) h(\mu) = 1$, i.e., $g(\mu) = \int \frac{d\mu}{h(\mu)}$:
- **Poisson-Like Count Variance ($\text{Var}(Y_i) \propto \mu_i \implies h(\mu) = \mu^{1/2}$)**: $g(\mu) = \int \mu^{-1/2} d\mu = 2\sqrt{\mu} \implies$ **Square-Root Transformation** $Y^* = \sqrt{Y}$.
- **Constant Coefficient of Variation / Multiplicative Error ($\text{Var}(Y_i) \propto \mu_i^2 \implies h(\mu) = \mu$)**: $g(\mu) = \int \mu^{-1} d\mu = \ln(\mu) \implies$ **Logarithmic Transformation** $Y^* = \ln(Y)$.
- **Quadratic Variance ($\text{Var}(Y_i) \propto \mu_i^4 \implies h(\mu) = \mu^2$)**: $g(\mu) = \int \mu^{-2} d\mu = -\mu^{-1} \implies$ **Reciprocal Transformation** $Y^* = 1/Y$.

### 2. The Box–Cox Parametric Power Transformation Family (1964)
Rather than guessing a power transformation by trial and error, George Box and Sir David Cox (1964) embedded all power and logarithmic transformations of a strictly positive response $Y_i > 0$ into a single continuous parametric family indexed by $\lambda \in \mathbb{R}$:

$$y_i^{(\lambda)} = \begin{cases} \dfrac{y_i^\lambda - 1}{\lambda}, & \text{if } \lambda \neq 0 \\[10pt] \ln(y_i), & \text{if } \lambda = 0 \end{cases}$$

Notice why subtracting $1$ and dividing by $\lambda$ is essential: by L'Hôpital's rule, $\lim_{\lambda \to 0} \frac{y^\lambda - 1}{\lambda} = \lim_{\lambda \to 0} \frac{y^\lambda \ln(y)}{1} = \ln(y)$, making $y^{(\lambda)}$ a **continuous function of $\lambda$ at $\lambda = 0$**! Special cases include $\lambda = 1$ (linear $y - 1$), $\lambda = 0.5$ (square root $2(\sqrt{y} - 1)$), $\lambda = 0$ (natural log $\ln y$), $\lambda = -0.5$ (inverse square root), and $\lambda = -1$ (reciprocal $1 - y^{-1}$).

How is the optimal transformation parameter $\hat{\lambda}$ estimated by Maximum Likelihood? Box and Cox postulate that for the true parameter $\lambda$, the transformed vector $\mathbf{y}^{(\lambda)}$ satisfies the classical normal linear model $\mathbf{y}^{(\lambda)} \sim \mathcal{N}_n(\mathbf{X}\boldsymbol{\beta}, \sigma^2 \mathbf{I}_n)$. However, we cannot simply pick $\lambda$ to minimize $\text{SSE}(\lambda) = \|(\mathbf{I}_n - \mathbf{H})\mathbf{y}^{(\lambda)}\|_2^2$, because changing $\lambda$ changes the scale of $y_i^{(\lambda)}$ (for instance, shrinking $\lambda$ can change $\text{SSE}(\lambda)$ purely by compressing the numerical units of $y^{(\lambda)}$)! Instead, we must write the exact joint density of the **original untranformed data** $(Y_1, \dots, Y_n)$ by multiplying the normal density of $\mathbf{y}^{(\lambda)}$ by the **Jacobian determinant** of the transformation $y_i \mapsto y_i^{(\lambda)}$:

$$J(\lambda; \mathbf{y}) = \prod_{i=1}^n \left| \frac{d y_i^{(\lambda)}}{d y_i} \right| = \prod_{i=1}^n y_i^{\lambda - 1} \implies \ln J(\lambda; \mathbf{y}) = (\lambda - 1) \sum_{i=1}^n \ln(y_i)$$

Profiling out $\hat{\boldsymbol{\beta}}(\lambda) = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T \mathbf{y}^{(\lambda)}$ and $\hat{\sigma}_{\text{MLE}}^2(\lambda) = \frac{1}{n}\text{SSE}(\lambda)$ yields the **Box–Cox Profile Log-Likelihood**:

$$\ell_p(\lambda) = -\frac{n}{2} \ln\left( \frac{\text{SSE}(\lambda)}{n} \right) + (\lambda - 1) \sum_{i=1}^n \ln(y_i) + \text{const}$$

Even more conveniently, let $\dot{y} = \left(\prod_{i=1}^n y_i\right)^{1/n} = \exp\left(\frac{1}{n}\sum_{i=1}^n \ln y_i\right)$ denote the **geometric mean** of the original responses, and define the **Jacobian-normalized Box–Cox response** $z_i^{(\lambda)}$:

$$z_i^{(\lambda)} = \frac{y_i^{(\lambda)}}{\dot{y}^{\lambda - 1}} = \begin{cases} \dfrac{y_i^\lambda - 1}{\lambda \, \dot{y}^{\lambda - 1}}, & \lambda \neq 0 \\[10pt] \dot{y} \ln(y_i), & \lambda = 0 \end{cases}$$

Because the Jacobian of $y_i \mapsto z_i^{(\lambda)}$ is identically $1$ ($\prod_{i=1}^n (y_i / \dot{y})^{\lambda - 1} = 1$), maximizing $\ell_p(\lambda)$ is **algebraically equivalent to minimizing the Residual Sum of Squares $\text{SSE}_z(\lambda)$ of the normalized response $z_i^{(\lambda)}$**:

$$\ell_p(\lambda) = -\frac{n}{2} \ln\left( \frac{\text{SSE}_z(\lambda)}{n} \right) + \text{const}$$

An approximate $100(1 - \alpha)\%$ likelihood-ratio confidence interval for $\lambda$ consists of all values of $\lambda$ satisfying $2[\ell_p(\hat{\lambda}) - \ell_p(\lambda)] \le \chi_{\alpha, 1}^2$ (i.e., $\ell_p(\lambda) \ge \ell_p(\hat{\lambda}) - \frac{1}{2}\chi_{\alpha, 1}^2 = \ell_p(\hat{\lambda}) - 1.921$ for $95\%$ confidence), from which the analyst selects a nearby interpretable value such as $\lambda \in \{-1, -0.5, 0, 0.5, 1\}$.

## 7.6 Variable Selection and Model Comparison Criteria: Mallows' C_p, AIC, BIC, PRESS & Stepwise Algorithms

Suppose an analyst has collected a pool of $K$ candidate explanatory variables ($P = K + 1$ total parameters including the intercept), giving rise to $2^K$ possible subset regression models. Why not simply include all $K$ predictors in a single "kitchen-sink" model? As proved in Problem 2.2, while omitting relevant variables ($\beta_j \neq 0$) induces omitted-variable bias, including extraneous or redundant variables ($\beta_j = 0$) inflates the sampling variances $\text{Var}(\hat{\beta}_m)$ of the remaining coefficients, inflates the out-of-sample prediction variance $\text{Var}(\hat{Y}_0) = \sigma^2 \mathbf{x}_0^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_0$, and wastes error degrees of freedom.

To balance goodness of fit (low $\text{SSE}_p$) against model parsimony (small parameter count $p = k + 1 \le P$) across candidate subset models of dimension $p$, statistical theory employs five primary **Model Selection Criteria**:

### 1. Adjusted Coefficient of Determination ($R_{a,p}^2$) and Minimum $\text{MSE}_p$
As established in Section 2.6, maximizing $R_{a,p}^2 = 1 - \frac{\text{SSE}_p / (n - p)}{\text{SST} / (n - 1)}$ is strictly equivalent to **minimizing the residual mean square $\text{MSE}_p = \frac{\text{SSE}_p}{n - p}$**.

### 2. Colin Mallows' $C_p$ Criterion (1973)
Mallows designed $C_p$ to estimate the standardized **Total Scaled Mean Squared Prediction Error** $\Gamma_p$ of a $p$-parameter subset model across all $n$ sample design points:

$$\Gamma_p = \frac{1}{\sigma^2} \sum_{i=1}^n \mathbb{E}\left[ (\hat{Y}_{i(p)} - \mu_i)^2 \right] = \frac{1}{\sigma^2} \left( \sum_{i=1}^n \text{Var}(\hat{Y}_{i(p)}) + \sum_{i=1}^n \left[\text{Bias}(\hat{Y}_{i(p)})\right]^2 \right)$$

Because $\sum_{i=1}^n \text{Var}(\hat{Y}_{i(p)}) = \sigma^2 \text{tr}(\mathbf{H}_p) = p \sigma^2$, and $\mathbb{E}[\text{SSE}_p] = (n - p)\sigma^2 + \sum_{i=1}^n [\text{Bias}(\hat{Y}_{i(p)})]^2$, solving for the squared bias sum $\sum [\text{Bias}(\hat{Y}_{i(p)})]^2 = \mathbb{E}[\text{SSE}_p] - (n - p)\sigma^2$ and substituting into $\Gamma_p$ yields:

$$\Gamma_p = p + \frac{\mathbb{E}[\text{SSE}_p] - (n - p)\sigma^2}{\sigma^2} = \frac{\mathbb{E}[\text{SSE}_p]}{\sigma^2} - (n - 2p)$$

Replacing $\mathbb{E}[\text{SSE}_p]$ by the observed subset $\text{SSE}_p$ and replacing the unknown true variance $\sigma^2$ by the unbiased variance estimator $\hat{\sigma}_{\text{full}}^2 = \text{MSE}_P = \frac{\text{SSE}_P}{n - P}$ from the **full $P$-parameter model** defines **Mallows' $C_p$ Statistic**:

$$C_p = \frac{\text{SSE}_p}{\text{MSE}_P} - (n - 2p) = p + (P - p) \left( F_{P - p} - 1 \right)$$

where $F_{P-p} = \frac{(\text{SSE}_p - \text{SSE}_P)/(P - p)}{\text{MSE}_P}$ is the partial $F$-statistic for testing whether the $P - p$ omitted variables have zero coefficients! Consequently:
- If the $p$-parameter subset model has **zero specification bias** ($\mathbb{E}[\text{SSE}_p] = (n - p)\sigma^2$), then $\mathbb{E}[C_p] \approx p$.
- For the full model ($p = P$), $C_P = P$ identically by algebra.
- Good subset models exhibit **both small $p$ and $C_p \le p$** (sitting near or below the $45^\circ$ reference line $C_p = p$).

### 3. Akaike Information Criterion ($\text{AIC}$), Hurvich–Tsai $\text{AIC}_c$, and Schwarz Bayesian Information Criterion ($\text{BIC}$)
Information criteria penalize twice the negative maximized log-likelihood $-2 \ell(\hat{\boldsymbol{\beta}}_p, \hat{\sigma}_{p,\text{MLE}}^2) = n \ln(\text{SSE}_p / n) + n(1 + \ln 2\pi)$ by a complexity penalty proportional to $p$. Dropping additive constants that depend only on $n$, for a linear regression model of dimension $p$:

$$\text{AIC}(p) = n \ln\left(\frac{\text{SSE}_p}{n}\right) + 2p, \qquad \text{AIC}_c(p) = \text{AIC}(p) + \frac{2(p+1)(p+2)}{n - p - 2}, \qquad \text{BIC}(p) = n \ln\left(\frac{\text{SSE}_p}{n}\right) + p \ln(n)$$

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Criterion</th><th>Mathematical Formula (Minimize, except $R_{a,p}^2$)</th><th>Penalty per Parameter</th><th>Asymptotic Optimality Property</th></tr>
</thead>
<tbody>
<tr><td><strong>Adjusted $R_{a,p}^2$</strong></td><td>$1 - \dfrac{\text{SSE}_p / (n - p)}{\text{SST} / (n - 1)}$</td><td>Favorable if partial $F > 1$</td><td>Too permissive for model selection (retains noise variables with $\mathbb{P}(F_{1,\nu} > 1) \approx 0.32$).</td></tr>
<tr><td><strong>Mallows' $C_p$</strong></td><td>$\dfrac{\text{SSE}_p}{\text{MSE}_P} - (n - 2p)$</td><td>$2$ units per parameter ($F > 2$)</td><td>Asymptotically equivalent to $\text{AIC}$; minimax optimal for out-of-sample prediction error.</td></tr>
<tr><td><strong>Akaike ($\text{AIC}$)</strong></td><td>$n \ln(\text{SSE}_p / n) + 2p$</td><td>$2$ per parameter ($F \gtrsim 2$)</td><td>Minimizes Kullback–Leibler divergence; <strong>asymptotically efficient</strong> for prediction, but not selection-consistent.</td></tr>
<tr><td><strong>Schwarz ($\text{BIC}$)</strong></td><td>$n \ln(\text{SSE}_p / n) + p \ln(n)$</td><td>$\ln(n)$ per parameter ($> 2$ for $n \ge 8$)</td><td><strong>Selection-consistent</strong>: selects the true finite sparse model with probability $\to 1$ as $n \to \infty$.</td></tr>
<tr><td><strong>Allen's $\text{PRESS}_p$</strong></td><td>$\sum_{i=1}^n \left(\dfrac{e_{i(p)}}{1 - h_{ii(p)}}\right)^2$</td><td>Via leverage $1/(1 - h_{ii})^2$</td><td>Exact leave-one-out cross-validation error without requiring $\text{MSE}_P$.</td></tr>
</tbody>
</table></div>

When $K$ is too large for exhaustive **All-Possible-Regressions** ($2^K$ subsets, accelerated via the Furnival–Wilson leaps-and-bounds branch-and-bound algorithm), greedy heuristic searches—**Forward Selection**, **Backward Elimination**, and **Stepwise Regression** (which alternates forward additions with backward partial-$F$ deletions to remove variables rendered redundant by newly entered collinear predictors)—are employed, though analysts must remember that post-selection $p$-values from stepwise searches suffer from severe selection bias (Freedman's paradox) and should be validated on held-out test data or replaced by LASSO regularization.

## Worked Questions and Solutions

### Question 1: Chow Structural Break F-Test & Dummy-Interaction Equivalence Across Two Economic Regimes

An energy economist investigates whether the relationship between residential natural gas consumption $Y$ and two predictors—heating degree days $X_1$ and real household income $X_2$ ($p = 3$ parameters: $\beta_0, \beta_1, \beta_2$)—experienced a structural break following an energy-efficiency building code reform. The total sample of $n = 46$ observations is partitioned into Regime 1 (Pre-Reform, $n_1 = 22$) and Regime 2 (Post-Reform, $n_2 = 24$). Fitting the model $Y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \varepsilon_i$ yields:
- **Regime 1 Separate Fit ($n_1 = 22$)**: $\hat{\boldsymbol{\beta}}_{(1)} = (12.0, \; 0.85, \; 0.40)^T$, $\text{SSE}_1 = 54.0$
- **Regime 2 Separate Fit ($n_2 = 24$)**: $\hat{\boldsymbol{\beta}}_{(2)} = (8.5, \; 0.55, \; 0.35)^T$, $\text{SSE}_2 = 66.0$
- **Pooled Fit Across All $n = 46$ Observations**: $\text{SSE}_{\text{pooled}} = 165.0$
- **Parallel-Slopes (ANCOVA) Fit ($Y_i = \beta_0 + \gamma D_i + \beta_1 x_{i1} + \beta_2 x_{i2} + \varepsilon_i$)**: $\text{SSE}_{\text{ANCOVA}} = 148.0$

1. Write down the single pooled dummy-interaction regression equation using $D_i = \mathbb{I}(i \in \text{Regime 2})$ whose OLS estimates reproduce $\hat{\boldsymbol{\beta}}_{(1)}$ and $\hat{\boldsymbol{\beta}}_{(2)}$ identically, and determine the exact numerical values of all $6$ coefficients in that interaction equation.
2. Conduct the **Chow Structural Break $F$-Test** of $H_0: \boldsymbol{\beta}_{(1)} = \boldsymbol{\beta}_{(2)}$ at $\alpha = 0.05$ ($F_{0.05, 3, 40} = 2.839$).
3. Using the extra sum-of-squares principle, test specifically whether the **slopes** $(\beta_1, \beta_2)$ changed between the two regimes ($H_0: \delta_1 = \delta_2 = 0$, given $F_{0.05, 2, 40} = 3.232$).

### Solution, step 1: Formulate the pooled dummy-interaction model and determine its 6 coefficients
Define the post-reform binary indicator $D_i = 1$ if observation $i$ belongs to Regime 2 and $D_i = 0$ if observation $i$ belongs to Regime 1. The full unrestricted dummy-interaction model is:

$$Y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \gamma_0 D_i + \delta_1 (D_i x_{i1}) + \delta_2 (D_i x_{i2}) + \varepsilon_i$$

When $D_i = 0$ (Regime 1), $\mathbb{E}[Y_i \mid \mathbf{x}_i, D_i = 0] = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2}$, so $(\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2) = \hat{\boldsymbol{\beta}}_{(1)}^T = (12.0, \; 0.85, \; 0.40)$.
When $D_i = 1$ (Regime 2), $\mathbb{E}[Y_i \mid \mathbf{x}_i, D_i = 1] = (\beta_0 + \gamma_0) + (\beta_1 + \delta_1) x_{i1} + (\beta_2 + \delta_2) x_{i2}$, so the differential coefficients are $\hat{\boldsymbol{\delta}} = \hat{\boldsymbol{\beta}}_{(2)} - \hat{\boldsymbol{\beta}}_{(1)}$:
- $\hat{\gamma}_0 = \hat{\beta}_{0(2)} - \hat{\beta}_{0(1)} = 8.5 - 12.0 = -3.50$
- $\hat{\delta}_1 = \hat{\beta}_{1(2)} - \hat{\beta}_{1(1)} = 0.55 - 0.85 = -0.30$
- $\hat{\delta}_2 = \hat{\beta}_{2(2)} - \hat{\beta}_{2(1)} = 0.35 - 0.40 = -0.05$

And the Residual Sum of Squares of this $6$-parameter interaction model is $\text{SSE}_F = \text{SSE}_1 + \text{SSE}_2 = 54.0 + 66.0 = 120.0$ with $\text{df}_F = (22 - 3) + (24 - 3) = 19 + 21 = 40$ degrees of freedom.

### Solution, step 2: Execute the Chow Structural Break F-test for H_0: beta_(1) = beta_(2)
Under the null hypothesis of complete structural stability $H_0: \gamma_0 = \delta_1 = \delta_2 = 0$ ($q = p = 3$ restrictions), the Reduced model is the pooled regression with $\text{SSE}_{\text{pooled}} = 165.0$ and $\text{df}_R = 46 - 3 = 43$. Applying the Chow $F$-formula:

$$F_{\text{Chow}} = \frac{\left[ \text{SSE}_{\text{pooled}} - (\text{SSE}_1 + \text{SSE}_2) \right] / p}{(\text{SSE}_1 + \text{SSE}_2) / (n_1 + n_2 - 2p)} = \frac{(165.0 - 120.0) / 3}{120.0 / 40} = \frac{45.0 / 3}{3.00} = \frac{15.0}{3.00} = 5.00$$

Since $F_{\text{Chow}} = 5.00 > F_{0.05, 3, 40} = 2.839$, we **reject $H_0$** at the $5\%$ significance level and conclude that a statistically significant structural break occurred following the building code reform.

### Solution, step 3: Test homogeneity of slopes H_0: delta_1 = delta_2 = 0 against the ANCOVA model
To determine whether the structural break was merely a parallel downward shift in the intercept ($\gamma_0 \neq 0$ with $\delta_1 = \delta_2 = 0$) or also altered the marginal slopes $(\delta_1, \delta_2)$, we compare the Full $6$-parameter interaction model ($\text{SSE}_F = 120.0$, $\text{df}_F = 40$) against the $4$-parameter parallel-slopes ANCOVA model ($\text{SSE}_{\text{ANCOVA}} = 148.0$, $\text{df}_{\text{ANCOVA}} = 46 - 4 = 42$), which imposes $q = 2$ restrictions ($H_0: \delta_1 = \delta_2 = 0$):

$$F_{\text{slopes}} = \frac{(\text{SSE}_{\text{ANCOVA}} - \text{SSE}_F) / 2}{\text{SSE}_F / 40} = \frac{(148.0 - 120.0) / 2}{3.00} = \frac{28.0 / 2}{3.00} = \frac{14.0}{3.00} \approx 4.667$$

Since $F_{\text{slopes}} = 4.667 > F_{0.05, 2, 40} = 3.232$, we reject the parallel-slopes hypothesis: the building code reform significantly reduced the marginal sensitivity of gas consumption to heating degree days ($\hat{\delta}_1 = -0.30$).

### Question 2: Orthogonal Polynomial Regression vs Raw Vandermonde Basis & Continuous Piecewise Linear Spline

An agronomist measures grain yield $Y_i$ (in tons/ha) across $n = 5$ equally spaced nitrogen fertilizer levels $x_i \in \{1, 2, 3, 4, 5\}$:

$$\begin{array}{c|ccccc}
x_i & 1 & 2 & 3 & 4 & 5 \\ \hline
Y_i & 4.0 & 7.0 & 9.0 & 10.0 & 10.0
\end{array}$$

1. Construct the first three **Forsythe Orthogonal Polynomials** $P_0(x_i), P_1(x_i), P_2(x_i)$ evaluated at $x_i \in \{1, 2, 3, 4, 5\}$, and verify explicitly that $\sum_{i=1}^5 P_j(x_i) P_m(x_i) = 0$ for all $j \neq m$.
2. Estimate the orthogonal quadratic regression $Y_i = \gamma_0 P_0(x_i) + \gamma_1 P_1(x_i) + \gamma_2 P_2(x_i) + \varepsilon_i$, compute $\text{SSR}(P_1)$, $\text{SSR}(P_2)$, and $\text{SSE}$, and convert the fitted orthogonal polynomial into the raw power form $\hat{Y} = \hat{\beta}_0 + \hat{\beta}_1 x + \hat{\beta}_2 x^2$. Why did adding the quadratic term $P_2(x)$ leave $\hat{\gamma}_0$ and $\hat{\gamma}_1$ completely unchanged?
3. Now fit a **continuous piecewise linear spline** with a single knot at $\xi = 3$: $Y_i = \alpha_0 + \alpha_1 x_i + \alpha_2 (x_i - 3)_+ + \varepsilon_i$, and compare its $\text{SSE}$ against the quadratic polynomial.

### Solution, step 1: Construct the orthogonal polynomial basis vectors P_0, P_1, P_2 on x = {1, 2, 3, 4, 5}
With $n = 5$ symmetric, equally spaced points $x_i \in \{1, 2, 3, 4, 5\}$, the sample mean is $\bar{x} = 3.0$:
- **Degree $0$**: $P_0(x_i) = 1 \implies \mathbf{p}_0 = (1, \; 1, \; 1, \; 1, \; 1)^T$, with $\sum_{i=1}^5 P_0(x_i)^2 = 5$.
- **Degree $1$**: $P_1(x_i) = x_i - \bar{x} = x_i - 3 \implies \mathbf{p}_1 = (-2, \; -1, \; 0, \; 1, \; 2)^T$, with $\sum_{i=1}^5 P_1(x_i)^2 = 4 + 1 + 0 + 1 + 4 = 10$.
- **Degree $2$**: By Forsythe's recurrence $P_2(x_i) = (x_i - a_2) P_1(x_i) - b_2 P_0(x_i)$, symmetry gives $a_2 = \bar{x} = 3.0$ (since $\sum (x_i - 3)^3 = 0$) and $b_2 = \frac{\sum P_1(x_i)^2}{\sum P_0(x_i)^2} = \frac{10}{5} = 2.0$. Thus:

$$P_2(x_i) = (x_i - 3)^2 - 2 \implies \mathbf{p}_2 = (2, \; -1, \; -2, \; -1, \; 2)^T$$

Checking orthogonality and squared norm of $\mathbf{p}_2$:
- $\sum_{i=1}^5 P_0(x_i) P_2(x_i) = 2 - 1 - 2 - 1 + 2 = 0$
- $\sum_{i=1}^5 P_1(x_i) P_2(x_i) = (-2)(2) + (-1)(-1) + (0)(-2) + (1)(-1) + (2)(2) = -4 + 1 + 0 - 1 + 4 = 0$
- $\sum_{i=1}^5 P_2(x_i)^2 = 4 + 1 + 4 + 1 + 4 = 14$

### Solution, step 2: Estimate orthogonal quadratic parameters gamma_j, SSR components, and convert to raw powers
Given $\mathbf{Y} = (4, 7, 9, 10, 10)^T$, because the Gram matrix is strictly diagonal $\mathbf{P}^T\mathbf{P} = \text{diag}(5, 10, 14)$, each coefficient $\hat{\gamma}_j = (\mathbf{p}_j^T \mathbf{Y}) / (\mathbf{p}_j^T \mathbf{p}_j)$ is computed independently:
1. **Constant ($\hat{\gamma}_0$)**: $\mathbf{p}_0^T \mathbf{Y} = 4 + 7 + 9 + 10 + 10 = 40 \implies \hat{\gamma}_0 = \frac{40}{5} = 8.00$.
2. **Linear ($\hat{\gamma}_1$)**: $\mathbf{p}_1^T \mathbf{Y} = (-2)(4) + (-1)(7) + 0(9) + 1(10) + 2(10) = -8 - 7 + 0 + 10 + 20 = 15 \implies \hat{\gamma}_1 = \frac{15}{10} = 1.50$, and $\text{SSR}(P_1) = \hat{\gamma}_1^2 (10) = 2.25(10) = 22.50$.
3. **Quadratic ($\hat{\gamma}_2$)**: $\mathbf{p}_2^T \mathbf{Y} = (2)(4) + (-1)(7) + (-2)(9) + (-1)(10) + (2)(10) = 8 - 7 - 18 - 10 + 20 = -7 \implies \hat{\gamma}_2 = \frac{-7}{14} = -0.50$, and $\text{SSR}(P_2) = \hat{\gamma}_2^2 (14) = 0.25(14) = 3.50$.

Since $\text{SST} = \sum (Y_i - 8.0)^2 = 16 + 1 + 1 + 4 + 4 = 26.00$, we see that $\text{SSR}(P_1) + \text{SSR}(P_2) = 22.50 + 3.50 = 26.00 = \text{SST}$, so $\text{SSE}_{\text{quad}} = 0.00$ ($R^2 = 100\%$)! Expanding $\hat{Y} = 8.0 + 1.5(x - 3) - 0.5[(x - 3)^2 - 2]$ into raw powers of $x$ gives:

$$\hat{Y} = 8.0 + 1.5 x - 4.5 - 0.5(x^2 - 6x + 7) = 0.0 + 4.5 x - 0.5 x^2$$

Notice that in the raw power basis, the linear coefficient changed from $1.50$ (in simple regression) to $\hat{\beta}_1 = 4.50$ when $x^2$ was added because $x$ and $x^2$ are highly collinear ($r = 0.975$), whereas in the orthogonal basis $\hat{\gamma}_1 = 1.50$ remained completely invariant!

### Solution, step 3: Fit the continuous piecewise linear spline at knot xi = 3
For the piecewise linear spline $Y_i = \alpha_0 + \alpha_1 x_i + \alpha_2 (x_i - 3)_+ + \varepsilon_i$, the hinge basis vector is $\mathbf{h} = ((1-3)_+, (2-3)_+, (3-3)_+, (4-3)_+, (5-3)_+)^T = (0, 0, 0, 1, 2)^T$.
Using $\mathbf{X}_s = [\mathbf{1}, \mathbf{x}, \mathbf{h}]$:

$$\mathbf{X}_s^T \mathbf{X}_s = \begin{pmatrix} 5 & 15 & 3 \\ 15 & 55 & 14 \\ 3 & 14 & 5 \end{pmatrix}, \qquad \mathbf{X}_s^T \mathbf{Y} = \begin{pmatrix} 40 \\ 135 \\ 30 \end{pmatrix}$$

Solving $(\mathbf{X}_s^T \mathbf{X}_s) \hat{\boldsymbol{\alpha}} = \mathbf{X}_s^T \mathbf{Y}$ gives:

$$\hat{\alpha}_0 = 1.70, \qquad \hat{\alpha}_1 = 2.50, \qquad \hat{\alpha}_2 = -2.00 \implies \hat{Y}_s(x) = 1.70 + 2.50 x - 2.00(x - 3)_+$$

Below $x = 3$, the fitted slope is $+2.50$ tons/ha per unit of nitrogen; above $x = 3$, the slope drops by $-2.00$ to $2.50 - 2.00 = +0.50$ tons/ha. Evaluating $\hat{\mathbf{Y}}_s = (4.2, \; 6.7, \; 9.2, \; 9.7, \; 10.2)^T$ gives residuals $\mathbf{e}_s = (-0.2, \; +0.3, \; -0.2, \; +0.3, \; -0.2)^T$ and $\text{SSE}_s = 0.04 + 0.09 + 0.04 + 0.09 + 0.04 = 0.30$ ($R^2 = 25.70 / 26.00 = 98.85\%$).

### Question 3: Model Selection Audit: Evaluating Mallows' C_p, AIC, BIC, Adjusted R^2, and Box-Cox Likelihood Ratio Test

A biostatistician models patient recovery time $Y$ across $n = 40$ clinical subjects using a pool of $K = 4$ candidate predictors ($X_1, X_2, X_3, X_4$, so $P = K + 1 = 5$ parameters in the full model). The Total Sum of Squares is $\text{SST} = 500.0$. Five candidate nested/best-subset models yield the following Residual Sums of Squares $\text{SSE}_p$:
- **Model M1 ($p = 2$: $\beta_0, X_1$)**: $\text{SSE}_2 = 160.0$
- **Model M2 ($p = 3$: $\beta_0, X_1, X_2$)**: $\text{SSE}_3 = 90.0$
- **Model M3 ($p = 3$: $\beta_0, X_1, X_3$)**: $\text{SSE}_3^* = 135.0$
- **Model M4 ($p = 4$: $\beta_0, X_1, X_2, X_3$)**: $\text{SSE}_4 = 86.5$
- **Model M5 ($p = 5$: Full Model $\beta_0, X_1, X_2, X_3, X_4$)**: $\text{SSE}_5 = 84.0$

1. Compute the full-model error variance estimate $\text{MSE}_P = \text{MSE}_5$, and for each of the five candidate models evaluate: (a) $\text{MSE}_p$, (b) Adjusted $R_{a,p}^2$, (c) **Mallows' $C_p$**, (d) **$\text{AIC}(p)$**, and (e) **$\text{BIC}(p)$**.
2. Which subset model is selected by each criterion, and why do $\text{AIC}$, $\text{BIC}$, and $C_p$ all prefer Model M2 ($X_1, X_2$) over Model M4 ($X_1, X_2, X_3$) even though Adjusted $R_{a,p}^2$ is slightly higher for Model M4?
3. Suppose a Box–Cox transformation profile log-likelihood analysis on Model M2 yields $\ell_p(\hat{\lambda} = 0.05) = -42.10$, $\ell_p(\lambda = 0) = -42.35$, and $\ell_p(\lambda = 1) = -51.80$. Test $H_0: \lambda = 1$ (no transformation) and $H_0: \lambda = 0$ (log transformation) at $\alpha = 0.05$ ($\chi_{0.05, 1}^2 = 3.841$).

### Solution, step 1: Compute MSE_p, Adjusted R_a^2, Mallows' C_p, AIC, and BIC across all five models
For the full model M5 ($n = 40, P = 5$), the error degrees of freedom are $n - P = 35$, and the unbiased full-model error variance estimate is:

$$\text{MSE}_P = \text{MSE}_5 = \frac{\text{SSE}_5}{40 - 5} = \frac{84.0}{35} = 2.40$$

Note also that $\text{MST} = \frac{\text{SST}}{n - 1} = \frac{500.0}{39} \approx 12.8205$, and $\ln(n) = \ln(40) \approx 3.6889$. Using $C_p = \frac{\text{SSE}_p}{2.40} - (40 - 2p)$, $\text{AIC}(p) = 40 \ln(\text{SSE}_p / 40) + 2p$, and $\text{BIC}(p) = 40 \ln(\text{SSE}_p / 40) + 3.6889 p$:

1. **Model M1 ($p = 2, \; \text{SSE}_2 = 160.0, \; \text{df} = 38$)**:
   - $\text{MSE}_2 = \frac{160.0}{38} = 4.2105 \implies R_{a,2}^2 = 1 - \frac{4.2105}{12.8205} = 0.6716$
   - $C_2 = \frac{160.0}{2.40} - (40 - 4) = 66.67 - 36.00 = 30.67 \gg 2$ (severe omitted-variable bias!)
   - $\text{AIC}(2) = 40 \ln(4.000) + 4 = 55.452 + 4.000 = 59.452$, $\quad \text{BIC}(2) = 55.452 + 7.378 = 62.830$

2. **Model M2 ($p = 3$: $X_1, X_2$, $\text{SSE}_3 = 90.0, \; \text{df} = 37$)**:
   - $\text{MSE}_3 = \frac{90.0}{37} = 2.4324 \implies R_{a,3}^2 = 1 - \frac{2.4324}{12.8205} = 0.8103$
   - $C_3 = \frac{90.0}{2.40} - (40 - 6) = 37.50 - 34.00 = \mathbf{3.50} \approx p = 3$
   - $\text{AIC}(3) = 40 \ln(2.250) + 6 = 32.437 + 6.000 = \mathbf{38.437}$, $\quad \text{BIC}(3) = 32.437 + 11.067 = \mathbf{43.504}$

3. **Model M3 ($p = 3$: $X_1, X_3$, $\text{SSE}_3^* = 135.0, \; \text{df} = 37$)**:
   - $\text{MSE}_3^* = \frac{135.0}{37} = 3.6486 \implies R_{a,3}^{*2} = 0.7154$
   - $C_3^* = \frac{135.0}{2.40} - 34 = 56.25 - 34.00 = 22.25 \gg 3$
   - $\text{AIC}(3^*) = 40 \ln(3.375) + 6 = 48.656 + 6 = 54.656$, $\quad \text{BIC}(3^*) = 48.656 + 11.067 = 59.723$

4. **Model M4 ($p = 4$: $X_1, X_2, X_3$, $\text{SSE}_4 = 86.5, \; \text{df} = 36$)**:
   - $\text{MSE}_4 = \frac{86.5}{36} = \mathbf{2.4028} \implies R_{a,4}^2 = 1 - \frac{2.4028}{12.8205} = \mathbf{0.8126}$
   - $C_4 = \frac{86.5}{2.40} - (40 - 8) = 36.04 - 32.00 = 4.04$
   - $\text{AIC}(4) = 40 \ln(2.1625) + 8 = 30.851 + 8.000 = 38.851$, $\quad \text{BIC}(4) = 30.851 + 14.756 = 45.607$

5. **Model M5 ($p = 5$: Full Model, $\text{SSE}_5 = 84.0, \; \text{df} = 35$)**:
   - $\text{MSE}_5 = \frac{84.0}{35} = \mathbf{2.4000} \implies R_{a,5}^2 = 1 - \frac{2.4000}{12.8205} = \mathbf{0.8128}$
   - $C_5 = \frac{84.0}{2.40} - (40 - 10) = 35.00 - 30.00 = 5.00 = P$
   - $\text{AIC}(5) = 40 \ln(2.100) + 10 = 29.677 + 10.000 = 39.677$, $\quad \text{BIC}(5) = 29.677 + 18.444 = 48.121$

### Solution, step 2: Compare the selected models and explain the F > 1 vs F > 2 threshold
**Mallows' $C_p$** ($C_3 = 3.50$, lowest $C_p$ and $C_3 \approx 3$), **$\text{AIC}$** ($\text{AIC}(3) = 38.437$), and **$\text{BIC}$** ($\text{BIC}(3) = 43.504$) all unanimously select the parsimonious two-predictor **Model M2 ($X_1, X_2$)**!
Why did $R_{a,p}^2$ (and $\text{MSE}_p$) slightly favor M4 and M5? Because the partial $F$-statistic for adding $X_3$ to M2 is $F(X_3 \mid X_1, X_2) = \frac{90.0 - 86.5}{2.4028} = 1.457$, and adding $X_4$ to M4 gives $F(X_4 \mid X_1, X_2, X_3) = \frac{86.5 - 84.0}{2.400} = 1.042$. Since both partial $F$-statistics slightly exceed $1.0$, $\text{MSE}_p$ decreases slightly and $R_{a,p}^2$ ticks up from $0.8103 \to 0.8126 \to 0.8128$, even though neither $X_3$ nor $X_4$ is anywhere near statistically significant ($p > 0.23$). Because $C_p$ and $\text{AIC}$ require $F \gtrsim 2.0$ (and $\text{BIC}$ requires $F \gtrsim \ln(40) = 3.69$) to justify an extra parameter, they rightly screen out the noise predictors $X_3$ and $X_4$.

### Solution, step 3: Evaluate the Box-Cox profile log-likelihood ratio tests for lambda = 1 and lambda = 0
Using the asymptotic Likelihood Ratio statistic $LR(\lambda_0) = 2\left[\ell_p(\hat{\lambda}) - \ell_p(\lambda_0)\right] \sim \chi_1^2$ under $H_0: \lambda = \lambda_0$:
1. **Testing $H_0: \lambda = 1$ (No Transformation)**:
   $$LR(1) = 2 \left[ -42.10 - (-51.80) \right] = 2(9.70) = 19.40 > \chi_{0.05, 1}^2 = 3.841$$
   We strongly **reject $\lambda = 1$**: the untransformed scale exhibits statistically significant skewness/heteroscedasticity.
2. **Testing $H_0: \lambda = 0$ (Natural Logarithm Transformation $Y^* = \ln Y$)**:
   $$LR(0) = 2 \left[ -42.10 - (-42.35) \right] = 2(0.25) = 0.50 < \chi_{0.05, 1}^2 = 3.841$$
   Because $\lambda = 0$ lies well inside the $95\%$ Box–Cox confidence interval ($\ell_p(0) = -42.35 \ge -42.10 - 1.921 = -44.021$), the analyst should adopt the clean, scientifically interpretable **log transformation $\ln(Y)$** ($\lambda = 0$) rather than the awkward fractional power $\hat{\lambda} = 0.05$.
