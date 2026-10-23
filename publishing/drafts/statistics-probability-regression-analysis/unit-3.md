# Unit 3: Exact & Asymptotic Inference in Linear Models: General Linear Hypotheses, Confidence Ellipsoids & Simultaneous Intervals

Once the parameters of a multiple linear regression model have been estimated via Ordinary Least Squares, scientific inquiry turns from point estimation to formal statistical inference: testing structural economic or physical hypotheses, constructing joint confidence regions for correlated parameters, controlling familywise error rates across simultaneous inferences, and forecasting future observations. In this third unit, we unify all parametric hypothesis tests in linear models under the General Linear Hypothesis framework $H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d}$, prove the equivalence of the Wald quadratic form and the Full-versus-Reduced Model Extra Sum-of-Squares $F$-statistic, derive Restricted Least Squares (RLS) estimators via Lagrange multipliers, analyze the geometry of joint confidence ellipsoids relative to marginal intervals, and establish Bonferroni, Scheffé, and Working–Hotelling simultaneous inference procedures.

## 3.1 The General Linear Hypothesis Framework and Full-Row-Rank Contrast Matrices

In empirical research, statistical hypotheses rarely take the elementary form of testing whether a single isolated parameter vanishes in a vacuum. Econometricians testing constant returns to scale in a Cobb–Douglas production function $\ln(Y_i) = \beta_0 + \beta_1 \ln(K_i) + \beta_2 \ln(L_i) + \varepsilon_i$ must test whether the capital and labor elasticities sum to unity ($\beta_1 + \beta_2 = 1$). Biostatisticians comparing four clinical treatment regimens must test whether three differential treatment effects are simultaneously zero ($\beta_1 = \beta_2 = \beta_3 = 0$). Agricultural scientists evaluating fertilizer formulations must test whether nitrogen and phosphorus have identical marginal yields ($\beta_1 - \beta_2 = 0$) while simultaneously testing whether a potassium interaction vanishes ($\beta_3 = 0$).

Every one of these diverse scientific questions is a special case of the **General Linear Hypothesis (GLH)** on the $p \times 1$ parameter vector $\boldsymbol{\beta}$ of the classical normal linear model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ with $\boldsymbol{\varepsilon} \sim \mathcal{N}_n(\mathbf{0}_n, \sigma^2 \mathbf{I}_n)$ and $\text{rank}(\mathbf{X}) = p$:

$$H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d} \qquad \text{versus} \qquad H_1: \mathbf{C}\boldsymbol{\beta} \neq \mathbf{d}$$

Here, $\mathbf{C} \in \mathbb{R}^{q \times p}$ is a known, deterministic **hypothesis (or coefficient) matrix** specifying $q$ linear combinations of the parameters, and $\mathbf{d} \in \mathbb{R}^{q \times 1}$ is a known vector of hypothesized constants. When $\mathbf{d} = \mathbf{0}_q$, the null hypothesis is termed a **homogeneous linear hypothesis**. To ensure that the $q$ scalar equations inside $\mathbf{C}\boldsymbol{\beta} = \mathbf{d}$ are algebraically consistent and contain no redundant linear dependencies, we require that $\mathbf{C}$ possess **full row rank**:

$$\text{rank}(\mathbf{C}) = q \le p$$

If a researcher initially writes down a set of linear equations where one equation is a linear combination of the others, redundant rows are simply eliminated until the remaining $q$ rows are linearly independent in $\mathbb{R}^p$. Geometrically, imposing the $q$ linearly independent restrictions $\mathbf{C}\boldsymbol{\beta} = \mathbf{d}$ constrains the parameter vector $\boldsymbol{\beta}$ to lie within an affine subspace (flat manifold) of dimension $p - q$ embedded inside $\mathbb{R}^p$.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Scientific Hypothesis</th><th>Null Hypothesis Statement</th><th>Dimension $q$</th><th>Matrix $\mathbf{C} \in \mathbb{R}^{q \times p}$ and Vector $\mathbf{d} \in \mathbb{R}^{q \times 1}$ (for $p = 4$)</th></tr>
</thead>
<tbody>
<tr><td><strong>Overall Model Significance (ANOVA)</strong></td><td>$H_0: \beta_1 = \beta_2 = \beta_3 = 0$</td><td>$q = 3$</td><td>$\mathbf{C} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \quad \mathbf{d} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$</td></tr>
<tr><td><strong>Single Partial Slope Test</strong></td><td>$H_0: \beta_2 = \beta_{2,0}$</td><td>$q = 1$</td><td>$\mathbf{C} = \begin{pmatrix} 0 & 0 & 1 & 0 \end{pmatrix}, \quad \mathbf{d} = (\beta_{2,0})$</td></tr>
<tr><td><strong>Subset Omission Test</strong></td><td>$H_0: \beta_2 = 0 \text{ and } \beta_3 = 0$</td><td>$q = 2$</td><td>$\mathbf{C} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}, \quad \mathbf{d} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$</td></tr>
<tr><td><strong>Equality of Two Slopes</strong></td><td>$H_0: \beta_1 = \beta_2 \iff \beta_1 - \beta_2 = 0$</td><td>$q = 1$</td><td>$\mathbf{C} = \begin{pmatrix} 0 & 1 & -1 & 0 \end{pmatrix}, \quad \mathbf{d} = (0)$</td></tr>
<tr><td><strong>Constant Returns to Scale</strong></td><td>$H_0: \beta_1 + \beta_2 + \beta_3 = 1$</td><td>$q = 1$</td><td>$\mathbf{C} = \begin{pmatrix} 0 & 1 & 1 & 1 \end{pmatrix}, \quad \mathbf{d} = (1)$</td></tr>
<tr><td><strong>Simultaneous Equality of Three Slopes</strong></td><td>$H_0: \beta_1 = \beta_2 = \beta_3$</td><td>$q = 2$</td><td>$\mathbf{C} = \begin{pmatrix} 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 \end{pmatrix}, \quad \mathbf{d} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$</td></tr>
</tbody>
</table></div>

To construct an exact test statistic from the unrestricted Ordinary Least Squares estimator $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$, we examine the **discrepancy vector** $\mathbf{w} = \mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d} \in \mathbb{R}^{q \times 1}$. Because $\hat{\boldsymbol{\beta}} \sim \mathcal{N}_p(\boldsymbol{\beta}, \sigma^2(\mathbf{X}^T\mathbf{X})^{-1})$, any affine transformation of $\hat{\boldsymbol{\beta}}$ follows a multivariate normal distribution:

$$\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d} \sim \mathcal{N}_q \left( \mathbf{C}\boldsymbol{\beta} - \mathbf{d}, \; \sigma^2 \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right)$$

Because $\text{rank}(\mathbf{C}) = q$ and $(\mathbf{X}^T\mathbf{X})^{-1}$ is strictly positive definite, the $q \times q$ symmetric matrix $\mathbf{G} = \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T$ is strictly positive definite and invertible. Consequently, standardizing the discrepancy vector by its inverse covariance matrix yields a quadratic form that follows a non-central chi-square distribution with $q$ degrees of freedom and non-centrality parameter $\lambda = (\mathbf{C}\boldsymbol{\beta} - \mathbf{d})^T [\sigma^2 \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T]^{-1} (\mathbf{C}\boldsymbol{\beta} - \mathbf{d})$:

$$\frac{Q_H}{\sigma^2} = \frac{(\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})}{\sigma^2} \sim \chi_q^2(\lambda)$$

Under the null hypothesis $H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d}$, the non-centrality parameter vanishes ($\lambda = 0$), so $Q_H / \sigma^2 \sim \chi_q^2$ follows a central chi-square distribution with $q$ degrees of freedom. Because $\hat{\boldsymbol{\beta}}$ (and hence $Q_H$) is statistically independent of the residual sum of squares $\text{SSE} = (n - p)s^2$ where $\text{SSE}/\sigma^2 \sim \chi_{n-p}^2$, dividing the mean square $(Q_H / q)$ by $s^2 = \text{SSE}/(n - p)$ cancels the unknown scale parameter $\sigma^2$ and produces the exact **General Linear Hypothesis $F$-Statistic**:

$$F = \frac{(\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d}) / q}{\text{SSE} / (n - p)} = \frac{Q_H / q}{s^2} \sim F_{q, \, n-p} \quad \text{under } H_0$$

When $H_0$ is false ($\mathbf{C}\boldsymbol{\beta} \neq \mathbf{d}$), $F$ follows a non-central $F_{q, n-p}(\lambda)$ distribution whose expectation exceeds unity, so we reject $H_0$ at significance level $\alpha$ whenever $F > F_{\alpha, \, q, \, n-p}$.

### Algebraic Invariance of the General Linear Hypothesis F-Statistic Under Equivalent Contrast Matrices
A crucial theoretical property of the General Linear Hypothesis test is that the value of the $F$-statistic depends only on the linear subspace (or affine restriction manifold) defined by the null hypothesis, and not on the particular algebraic basis chosen to write the contrast matrix. Suppose two statisticians formulate the same structural hypothesis—for instance, the simultaneous equality of three slope coefficients—using two different full-row-rank contrast matrices that are related to one another by premultiplication by an invertible $q \times q$ transformation matrix. When the transformed contrast matrix and transformed right-hand-side vector are substituted into the Wald quadratic form, the invertible transformation matrix and its transpose factor out of the middle inverse matrix and cancel identically with the outer factors. Thus, any two algebraically equivalent formulations of a linear restriction yield the exact same numerator sum of squares, degrees of freedom, and $p$-value.

## 3.2 Restricted Least Squares (RLS), Lagrange Multipliers, and Full vs Reduced Model Equivalence

A profound theorem of linear model theory states that the Wald-type quadratic form $Q_H = (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})^T [\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})$ derived in Section 3.1 is **identically equal** to the drop in the Residual Sum of Squares between the constrained (Reduced) model where $H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d}$ is enforced and the unconstrained (Full) model! To prove this equivalence, we derive the **Restricted Least Squares (RLS)** estimator $\hat{\boldsymbol{\beta}}_R$, which minimizes $\|\mathbf{Y} - \mathbf{X}\mathbf{b}\|_2^2$ subject to the exact linear equality constraint $\mathbf{C}\mathbf{b} = \mathbf{d}$.

Formulate the Lagrangian objective function with a $q \times 1$ vector of Lagrange multipliers $2\boldsymbol{\lambda} \in \mathbb{R}^q$:

$$\mathcal{L}(\mathbf{b}, \boldsymbol{\lambda}) = (\mathbf{Y} - \mathbf{X}\mathbf{b})^T (\mathbf{Y} - \mathbf{X}\mathbf{b}) + 2\boldsymbol{\lambda}^T (\mathbf{C}\mathbf{b} - \mathbf{d})$$

Setting the partial derivatives with respect to $\mathbf{b}$ and $\boldsymbol{\lambda}$ equal to zero at the constrained minimizer $(\hat{\boldsymbol{\beta}}_R, \hat{\boldsymbol{\lambda}})$ gives the first-order Karush–Kuhn–Tucker (KKT) optimality system:

$$\begin{aligned}
\frac{1}{2} \nabla_{\mathbf{b}} \mathcal{L} &= -\mathbf{X}^T \mathbf{Y} + (\mathbf{X}^T \mathbf{X})\hat{\boldsymbol{\beta}}_R + \mathbf{C}^T \hat{\boldsymbol{\lambda}} = \mathbf{0}_p \\
\frac{1}{2} \nabla_{\boldsymbol{\lambda}} \mathcal{L} &= \mathbf{C}\hat{\boldsymbol{\beta}}_R - \mathbf{d} = \mathbf{0}_q
\end{aligned}$$

Premultiplying the first equation by $(\mathbf{X}^T\mathbf{X})^{-1}$ and recognizing the unrestricted OLS estimator $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ yields:

$$\hat{\boldsymbol{\beta}}_R = \hat{\boldsymbol{\beta}} - (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{C}^T \hat{\boldsymbol{\lambda}}$$

To solve for the Lagrange multiplier vector $\hat{\boldsymbol{\lambda}}$, premultiply both sides of this expression by $\mathbf{C}$ and invoke the second KKT constraint $\mathbf{C}\hat{\boldsymbol{\beta}}_R = \mathbf{d}$:

$$\mathbf{C}\hat{\boldsymbol{\beta}}_R = \mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \hat{\boldsymbol{\lambda}} = \mathbf{d} \implies \hat{\boldsymbol{\lambda}} = \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})$$

Substituting $\hat{\boldsymbol{\lambda}}$ back into the equation for $\hat{\boldsymbol{\beta}}_R$ provides the closed-form **Restricted Least Squares (RLS) Estimator**:

$$\hat{\boldsymbol{\beta}}_R = \hat{\boldsymbol{\beta}} - (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})$$

Notice how transparent this formula is: if the unrestricted OLS estimator already satisfies the null hypothesis ($\mathbf{C}\hat{\boldsymbol{\beta}} = \mathbf{d}$), the correction term vanishes and $\hat{\boldsymbol{\beta}}_R = \hat{\boldsymbol{\beta}}$. Otherwise, $\hat{\boldsymbol{\beta}}_R$ projects $\hat{\boldsymbol{\beta}}$ obliquely onto the constraint manifold $\{\mathbf{b} : \mathbf{C}\mathbf{b} = \mathbf{d}\}$ in the metric of $(\mathbf{X}^T\mathbf{X})$. Under $H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d}$, $\hat{\boldsymbol{\beta}}_R$ is strictly unbiased ($\mathbb{E}[\hat{\boldsymbol{\beta}}_R] = \boldsymbol{\beta}$) and has a smaller covariance matrix than $\hat{\boldsymbol{\beta}}$ in the Loewner sense:

$$\text{Cov}(\hat{\boldsymbol{\beta}}_R) = \sigma^2 (\mathbf{X}^T\mathbf{X})^{-1} - \sigma^2 (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1} \preceq \text{Cov}(\hat{\boldsymbol{\beta}})$$

Now let us decompose the residual vector of the Restricted (Reduced) model, $\mathbf{e}_R = \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}_R$, by adding and subtracting the unrestricted fitted vector $\hat{\mathbf{Y}} = \mathbf{X}\hat{\boldsymbol{\beta}}$:

$$\mathbf{e}_R = \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}_R = (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}) + \mathbf{X}(\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_R) = \mathbf{e}_F + \mathbf{X}(\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_R)$$

where $\mathbf{e}_F = \mathbf{Y} - \mathbf{X}\hat{\boldsymbol{\beta}}$ is the residual vector of the unrestricted Full model. Because $\mathbf{X}^T \mathbf{e}_F = \mathbf{0}_p$ by the normal equations of the full model, the two vectors $\mathbf{e}_F \in \mathcal{C}(\mathbf{X})^\perp$ and $\mathbf{X}(\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_R) \in \mathcal{C}(\mathbf{X})$ are strictly **orthogonal**! Taking squared Euclidean norms yields the Pythagorean identity:

$$\text{SSE}_R = \|\mathbf{e}_R\|_2^2 = \|\mathbf{e}_F\|_2^2 + \|\mathbf{X}(\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_R)\|_2^2 = \text{SSE}_F + (\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_R)^T (\mathbf{X}^T\mathbf{X}) (\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_R)$$

Substituting $\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_R = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T [\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})$ into the quadratic term simplifies immediately to:

$$\text{SSE}_R - \text{SSE}_F = (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d})^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d}) = Q_H$$

This establishes the celebrated **Full-versus-Reduced Model General Linear $F$-Test**:

$$F = \frac{(\text{SSE}_R - \text{SSE}_F) / (\text{df}_R - \text{df}_F)}{\text{SSE}_F / \text{df}_F} = \frac{(\text{SSE}_R - \text{SSE}_F) / q}{\text{SSE}_F / (n - p)} = \frac{(R_F^2 - R_R^2) / q}{(1 - R_F^2) / (n - p)} \sim F_{q, \, n-p} \quad \text{under } H_0$$

where the last equality holds whenever both the Full and Reduced models share the same dependent variable $Y$ and include an intercept so they share the same Total Sum of Squares $\text{SST}$. Moreover, under Gaussian errors, the Gaussian likelihood ratio statistic $\Lambda = \sup_{H_0} L(\boldsymbol{\beta}, \sigma^2) / \sup_{\Theta} L(\boldsymbol{\beta}, \sigma^2)$ equals $(\text{SSE}_F / \text{SSE}_R)^{n/2} = (1 + \frac{q}{n-p} F)^{-n/2}$, which is a strictly decreasing function of $F$, proving that the General Linear $F$-test is identically the exact **Likelihood Ratio Test (LRT)**!

### Bias-Variance Trade-Off and Gauss-Markov Optimality of Restricted Least Squares
The Restricted Least Squares estimator derived via Lagrange multipliers illuminates the fundamental interplay between structural prior information and sampling precision. When the linear restriction imposed by the null hypothesis holds exactly in the underlying population, the Restricted Least Squares estimator is unbiased and achieves a strictly smaller variance-covariance matrix (in the Loewner positive semi-definite ordering) than the unrestricted Ordinary Least Squares estimator, because projecting the estimate onto the lower-dimensional constraint manifold eliminates $q$ dimensions of orthogonal estimation noise. However, if the imposed restriction is false in the population, the Restricted Least Squares estimator incurs a systematic specification bias proportional to the violation of the constraint, and the numerator of the General Linear $F$-statistic compares the squared magnitude of this restriction violation against the baseline error variance.

## 3.3 Individual Coefficient t-Tests, Linear Combinations, and Structural Parameter Restrictions

Let us specialize the General Linear Hypothesis to the most frequently encountered single-degree-of-freedom ($q = 1$) and multi-degree-of-freedom hypotheses in applied regression analysis.

### 1. Testing a Single Linear Combination $H_0: \mathbf{c}^T \boldsymbol{\beta} = d$ ($q = 1$)
Let $\mathbf{c} = (c_0, c_1, \dots, c_k)^T \in \mathbb{R}^p \setminus \{\mathbf{0}\}$ be a single column vector defining a scalar parametric target $\theta = \mathbf{c}^T \boldsymbol{\beta} = \sum_{j=0}^k c_j \beta_j$. By the Matrix Gauss–Markov Theorem, its unique BLUE is $\hat{\theta} = \mathbf{c}^T \hat{\boldsymbol{\beta}}$, which under normal errors follows:

$$\mathbf{c}^T \hat{\boldsymbol{\beta}} \sim \mathcal{N}\left( \mathbf{c}^T \boldsymbol{\beta}, \; \sigma^2 \mathbf{c}^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{c} \right)$$

Replacing $\sigma^2$ by $s^2 = \text{MSE} = \text{SSE}/(n - p)$ gives the estimated standard error of $\mathbf{c}^T \hat{\boldsymbol{\beta}}$:

$$\text{SE}(\mathbf{c}^T \hat{\boldsymbol{\beta}}) = s \sqrt{\mathbf{c}^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{c}}$$

To test $H_0: \mathbf{c}^T \boldsymbol{\beta} = d$ (against a two-sided alternative $H_1: \mathbf{c}^T \boldsymbol{\beta} \neq d$, or a one-sided alternative $H_1: \mathbf{c}^T \boldsymbol{\beta} > d$ or $< d$), we use the exact Student $t$-statistic with $n - p$ degrees of freedom:

$$t = \frac{\mathbf{c}^T \hat{\boldsymbol{\beta}} - d}{s \sqrt{\mathbf{c}^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{c}}} \sim t_{n-p} \quad \text{under } H_0$$

Notice that squaring $t$ reproduces the $q = 1$ General Linear $F$-statistic: $t^2 = \frac{(\mathbf{c}^T\hat{\boldsymbol{\beta}} - d)^2}{s^2 \mathbf{c}^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{c}} = F \sim F_{1, n-p}$. The corresponding exact $100(1 - \alpha)\%$ confidence interval for $\mathbf{c}^T \boldsymbol{\beta}$ is $\mathbf{c}^T \hat{\boldsymbol{\beta}} \pm t_{\alpha/2, n-p} \, s \sqrt{\mathbf{c}^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{c}}$.

### 2. Individual Partial $t$-Tests $H_0: \beta_j = \beta_{j,0}$
Choosing $\mathbf{c} = \mathbf{e}_j$ (the $j$-th standard basis vector with $1$ in position $j$ and $0$ elsewhere) selects a single regression coefficient $\beta_j$. Then $\mathbf{c}^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{c} = c_{jj}$, the $j$-th diagonal entry of $(\mathbf{X}^T\mathbf{X})^{-1}$, so $\text{SE}(\hat{\beta}_j) = s \sqrt{c_{jj}}$ and:

$$t_j = \frac{\hat{\beta}_j - \beta_{j,0}}{s \sqrt{c_{jj}}} \sim t_{n-p} \quad \text{under } H_0: \beta_j = \beta_{j,0}$$

When $\beta_{j,0} = 0$, $t_j^2 = F_j = \frac{\text{SSR}(X_j \mid \mathbf{X}_{(-j)})}{\text{MSE}}$ is the marginal (Type III) partial $F$-test for removing predictor $X_j$ from the full model.

### 3. Testing Equality of Two Slope Parameters $H_0: \beta_j = \beta_m$
To test whether two predictors $X_j$ and $X_m$ (measured in commensurate units) exert identical marginal effects on $Y$, we rewrite $H_0: \beta_j - \beta_m = 0$ by setting $\mathbf{c} = \mathbf{e}_j - \mathbf{e}_m$. Evaluating the quadratic form $\mathbf{c}^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{c} = c_{jj} + c_{mm} - 2 c_{jm}$ yields the standard error of the difference between two estimated slopes:

$$\text{SE}(\hat{\beta}_j - \hat{\beta}_m) = \sqrt{ \widehat{\text{Var}}(\hat{\beta}_j) + \widehat{\text{Var}}(\hat{\beta}_m) - 2 \widehat{\text{Cov}}(\hat{\beta}_j, \hat{\beta}_m) } = s \sqrt{ c_{jj} + c_{mm} - 2 c_{jm} }$$

Alternatively, we can form the Reduced model directly by substituting $\beta_j = \beta_m$ into the regression equation:

$$Y_i = \beta_0 + \dots + \beta_j (x_{ij} + x_{im}) + \dots + \varepsilon_i$$

which collapses the two separate predictors $x_{ij}$ and $x_{im}$ into a single composite sum variable $z_i = x_{ij} + x_{im}$, reducing the number of parameters by $q = 1$, and then compute $F = (\text{SSE}_R - \text{SSE}_F) / \text{MSE}_F = t^2$.

### 4. Testing Linear Structural Restrictions via Reparameterization
Similarly, to test $H_0: \beta_1 + \beta_2 = 1$ in $Y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \varepsilon_i$ via the Reduced-model method, substitute $\beta_2 = 1 - \beta_1$ into the model:

$$Y_i = \beta_0 + \beta_1 x_{i1} + (1 - \beta_1) x_{i2} + \varepsilon_i \iff (Y_i - x_{i2}) = \beta_0 + \beta_1 (x_{i1} - x_{i2}) + \varepsilon_i$$

Thus, regressing the transformed response $Y_i^* = Y_i - x_{i2}$ on the single transformed regressor $x_i^* = x_{i1} - x_{i2}$ yields the exact Restricted Least Squares sum of squares $\text{SSE}_R$ with $n - 2$ degrees of freedom!

### Commensurability of Units When Testing Equality or Sums of Regression Coefficients
When formulating linear combinations and equality tests across multiple regression slopes, applied statisticians must verify that the underlying variables are measured in commensurate physical or economic units. Testing whether a single partial regression coefficient equals zero is invariant to rescaling the predictor: multiplying a predictor by a thousand divides its estimated slope and its standard error by a thousand, leaving the individual $t$-statistic unchanged. In sharp contrast, testing whether two slope coefficients are equal to one another ($H_0: \beta_1 - \beta_2 = 0$) is meaningful only when both predictors share a common scale—such as dollars of expenditure on two advertising channels, percentage shares, or dimensionless logarithmic elasticities in a Cobb–Douglas function. If two predictors are measured in incompatible physical units, testing equality of their raw slopes is arbitrary unless the variables are first standardized to dimensionless z-scores.

## 3.4 Joint Confidence Ellipsoids vs Marginal Confidence Intervals

When an investigator wishes to make a joint probability statement about the entire $p \times 1$ parameter vector $\boldsymbol{\beta}$ (or a $q \times 1$ subvector $\boldsymbol{\beta}_S = \mathbf{C}\boldsymbol{\beta}$), substituting $\mathbf{C} = \mathbf{I}_p$ and $\mathbf{d} = \boldsymbol{\beta}$ into the General Linear Hypothesis pivotal quantity shows that:

$$\frac{(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})^T (\mathbf{X}^T\mathbf{X}) (\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})}{p s^2} \sim F_{p, \, n-p}$$

Inverting this pivotal quantity defines the exact $100(1 - \alpha)\%$ **Joint Confidence Region for $\boldsymbol{\beta}$**:

$$\mathcal{E}_{1-\alpha}(\boldsymbol{\beta}) = \left\{ \boldsymbol{\beta} \in \mathbb{R}^p : (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}})^T (\mathbf{X}^T\mathbf{X}) (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}) \le p \, s^2 \, F_{\alpha, \, p, \, n-p} \right\}$$

Because $\mathbf{X}^T\mathbf{X}$ is symmetric and strictly positive definite, the inequality $(\boldsymbol{\beta} - \hat{\boldsymbol{\beta}})^T (\mathbf{X}^T\mathbf{X}) (\boldsymbol{\beta} - \hat{\boldsymbol{\beta}}) \le c^2$ describes the interior and boundary of a solid **$p$-dimensional hyper-ellipsoid** centered at the OLS estimate $\hat{\boldsymbol{\beta}}$. More generally, for any $q \times 1$ parameter subvector $\boldsymbol{\theta} = \mathbf{C}\boldsymbol{\beta}$ (such as the two slopes $(\beta_1, \beta_2)^T$ with $q = 2$), the exact $100(1 - \alpha)\%$ joint confidence ellipsoid is:

$$\mathcal{E}_{1-\alpha}(\boldsymbol{\theta}) = \left\{ \boldsymbol{\theta} \in \mathbb{R}^q : (\boldsymbol{\theta} - \hat{\boldsymbol{\theta}})^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\boldsymbol{\theta} - \hat{\boldsymbol{\theta}}) \le q \, s^2 \, F_{\alpha, \, q, \, n-p} \right\}$$

### Geometric Orientation of the Confidence Ellipsoid vs the Marginal Rectangle
Why is a joint confidence ellipsoid essential when predictors $X_1$ and $X_2$ are correlated? Suppose we construct separate $100(1 - \alpha)\%$ marginal $t$-intervals $\hat{\beta}_1 \pm t_{\alpha/2, n-p} \text{SE}(\hat{\beta}_1)$ and $\hat{\beta}_2 \pm t_{\alpha/2, n-p} \text{SE}(\hat{\beta}_2)$. Taking their Cartesian product forms an axis-aligned **rectangular box** in the $(\beta_1, \beta_2)$-plane. This naive rectangle fails in two ways:
1. **Distorted Joint Coverage Probability**: Even if $\hat{\beta}_1$ and $\hat{\beta}_2$ were independent, the probability that both independent $95\%$ intervals simultaneously cover their targets would be $(0.95)^2 = 0.9025 < 0.95$.
2. **Tilt Induced by Predictor Collinearity**: Recall from Problem 2.3 that when $X_1$ and $X_2$ have positive sample correlation $r_{12} > 0$, the off-diagonal element of $(\mathbf{X}_c^T\mathbf{X}_c)^{-1}$ is negative, meaning $\text{Cov}(\hat{\beta}_1, \hat{\beta}_2) < 0$ (and $\rho(\hat{\beta}_1, \hat{\beta}_2) = -r_{12}$). Intuitively, if $X_1$ and $X_2$ move together in the sample, overestimating $\beta_1$ can be compensated by underestimating $\beta_2$ while keeping the fitted predictions $\hat{\beta}_1 x_{i1} + \hat{\beta}_2 x_{i2}$ nearly unchanged! Conversely, the quadratic form matrix $\mathbf{X}_c^T\mathbf{X}_c$ has positive off-diagonal entry $S_{12} > 0$, so the confidence ellipse:

$$S_{11}(\beta_1 - \hat{\beta}_1)^2 + 2 S_{12}(\beta_1 - \hat{\beta}_1)(\beta_2 - \hat{\beta}_2) + S_{22}(\beta_2 - \hat{\beta}_2)^2 \le 2 s^2 F_{\alpha, 2, n-p}$$

is **tilted along a negative $45^\circ$-like principal axis** (running from top-left to bottom-right). The eigenvalues $\lambda_{\min}, \lambda_{\max}$ of $\mathbf{X}_c^T\mathbf{X}_c$ govern the semi-axis lengths of the ellipse: the major (longest) semi-axis has length $\sqrt{2 s^2 F_{\alpha, 2, n-p} / \lambda_{\min}}$ along the direction of near-collinearity, while the minor (shortest) semi-axis has length $\sqrt{2 s^2 F_{\alpha, 2, n-p} / \lambda_{\max}}$. Consequently, a parameter pair $(\beta_1, \beta_2)$ (such as $(0, 0)$) can lie **well outside** the tilted joint confidence ellipse—so the joint $F$-test rejects $H_0: \beta_1 = \beta_2 = 0$—even when $0$ lies **inside** both individual marginal $t$-intervals! Conversely, corners of the marginal rectangle where $\beta_1$ and $\beta_2$ deviate in the same direction lie far outside the tilted ellipse.

### Resolving Apparent Contradictions Between the Overall ANOVA F-Test and Individual t-Tests
In empirical regression modeling with correlated predictors, analysts frequently encounter the puzzling situation in which the overall Analysis of Variance $F$-test rejects the global null hypothesis with an extremely small $p$-value, yet every single individual partial $t$-test fails to reach statistical significance. The geometric analysis of joint confidence ellipsoids completely resolves this apparent paradox. Each individual $t$-test projects the multidimensional confidence ellipsoid orthogonally onto a single coordinate axis, measuring only what a predictor contributes uniquely after all other correlated predictors have already been accounted for. When two predictors are strongly correlated, neither variable possesses much unique variation orthogonal to its partner, so the axis projections of the tilted confidence ellipsoid are wide and span zero on each individual axis, even though the narrow tilted ellipsoid itself misses the origin by a wide margin along the diagonal direction of joint variation.

This geometric divergence between the joint confidence ellipsoid and the axis-aligned marginal confidence box underscores a cardinal rule of multiple regression modeling: an analyst must never drop two or more correlated predictors simultaneously from a regression equation simply because their individual partial $t$-statistics are both smaller than the critical threshold! Deleting both variables at once corresponds to testing the joint null hypothesis that both parameters equal zero, which requires evaluating whether the origin lies inside the joint two-dimensional confidence ellipse via the partial $F$-test. Frequently, dropping one of the two collinear predictors immediately causes the remaining predictor's standard error to collapse and its $t$-statistic to become highly significant.

## 3.5 Simultaneous Inference: Bonferroni, Scheffe's S-Method, and Maximum Modulus Intervals

Whenever an analyst constructs $m \ge 2$ confidence intervals or conducts $m$ hypothesis tests from the same regression dataset, the **Familywise Error Rate (FWER)**—defined as the probability that at least one confidence interval in the family fails to cover its true parameter—exceeds the nominal pointwise level $\alpha$. Let $E_j$ denote the error event that the $j$-th confidence interval $I_j$ fails to cover its true target $\theta_j = \mathbf{c}_j^T \boldsymbol{\beta}$ ($j = 1, \dots, m$). The joint (simultaneous) confidence level of the family $\{I_1, \dots, I_m\}$ is:

$$\mathbb{P}\left( \bigcap_{j=1}^m \{\theta_j \in I_j\} \right) = 1 - \mathbb{P}\left( \bigcup_{j=1}^m E_j \right)$$

Three classical simultaneous inference procedures control the familywise error rate $\mathbb{P}(\bigcup_{j=1}^m E_j) \le \alpha$:

### 1. The Bonferroni Simultaneous Intervals (Finite Pre-Specified Family of Size $m$)
By **Boole's Inequality** (the finite union bound), for any events $E_1, \dots, E_m$ regardless of their dependence structure:

$$\mathbb{P}\left( \bigcup_{j=1}^m E_j \right) \le \sum_{j=1}^m \mathbb{P}(E_j)$$

Therefore, if we construct each of the $m$ pre-selected confidence intervals at individual error rate $\alpha / m$ (so $\mathbb{P}(E_j) = \alpha / m$), the familywise error rate is guaranteed not to exceed $\sum_{j=1}^m (\alpha/m) = \alpha$:

$$\mathbf{c}_j^T \hat{\boldsymbol{\beta}} \pm t_{\alpha / (2m), \, n-p} \, \text{SE}(\mathbf{c}_j^T \hat{\boldsymbol{\beta}}), \quad j = 1, 2, \dots, m$$

A slightly sharper bound for normal linear models is the **Šidák inequality** (valid for multivariate Student-$t$ distributions with product-type correlations), which replaces $\alpha/(2m)$ by $\frac{1}{2}[1 - (1 - \alpha)^{1/m}]$, or the exact multivariate-$t$ **Studentized Maximum Modulus** distribution.

### 2. Scheffé's $S$-Method (All Infinitely Many Linear Combinations in a $q$-Dimensional Subspace)
What if the investigator does not fix a small finite number $m$ of contrasts in advance, or wishes to engage in post-hoc data snooping across *all possible* linear combinations $\mathbf{c}^T \boldsymbol{\beta}$ belonging to a $q$-dimensional subspace spanned by the rows of $\mathbf{C} \in \mathbb{R}^{q \times p}$? Henry Scheffé (1953) solved this problem by projecting the $q$-dimensional joint confidence ellipsoid $\mathcal{E}_{1-\alpha}(\mathbf{C}\boldsymbol{\beta})$ onto every one-dimensional line! By the **Cauchy–Schwarz Inequality** (in the metric of $\mathbf{G} = \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T$), for any vector $\mathbf{a} \in \mathbb{R}^q \setminus \{\mathbf{0}\}$:

$$\sup_{\mathbf{a} \in \mathbb{R}^q \setminus \{\mathbf{0}\}} \frac{\left[ \mathbf{a}^T (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{C}\boldsymbol{\beta}) \right]^2}{s^2 \, \mathbf{a}^T \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \mathbf{a}} = \frac{(\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{C}\boldsymbol{\beta})^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{C}\boldsymbol{\beta})}{s^2} = q F \sim q F_{q, \, n-p}$$

Taking square roots proves that with exact probability $1 - \alpha$, **simultaneously for every $\mathbf{a} \in \mathbb{R}^q$** (where $\mathbf{c}^T = \mathbf{a}^T \mathbf{C}$):

$$\mathbf{c}^T \hat{\boldsymbol{\beta}} \pm S_\alpha \, \text{SE}(\mathbf{c}^T \hat{\boldsymbol{\beta}}), \qquad \text{where } S_\alpha = \sqrt{q \, F_{\alpha, \, q, \, n-p}}$$

When $\mathbf{C} = \mathbf{I}_p$ ($q = p$), $S_\alpha = \sqrt{p F_{\alpha, p, n-p}}$ provides simultaneous intervals for all $\mathbf{x}_0^T \boldsymbol{\beta}$ across the entire predictor space $\mathbf{x}_0 \in \mathbb{R}^p$ (the multiple-regression generalization of the Working–Hotelling band!). Moreover, Scheffé's method enjoys exact **coherence with the $F$-test**: the $F$-test rejects $H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d}$ at level $\alpha$ *if and only if* there exists at least one linear combination $\mathbf{a}^T \mathbf{C}\boldsymbol{\beta}$ whose Scheffé interval excludes $\mathbf{a}^T \mathbf{d}$.

### Strategic Choice Between Bonferroni and Scheffé:
Because both methods use the identical standard error $\text{SE}(\mathbf{c}_j^T\hat{\boldsymbol{\beta}})$, the analyst simply compares the two critical multipliers $B_\alpha = t_{\alpha/(2m), n-p}$ and $S_\alpha = \sqrt{q F_{\alpha, q, n-p}}$ **before examining the data** and selects whichever multiplier is smaller! For a small number of pre-planned comparisons ($m \approx q$ or $m$ slightly larger than $q$), the Bonferroni multiplier $t_{\alpha/(2m), n-p}$ is strictly smaller than $\sqrt{q F_{\alpha, q, n-p}}$, yielding narrower intervals; for large $m \gg q$ or post-hoc exploration, Scheffé's multiplier remains bounded at $\sqrt{q F_{\alpha, q, n-p}}$ whereas $t_{\alpha/(2m), n-p} \to \infty$.

### Controlling Familywise Error Rates in Confirmatory Versus Exploratory Regression Studies
Modern reproducible science places heavy emphasis on controlling false-positive discovery rates when multiple inferences are drawn from a single regression model. In a confirmatory clinical trial or engineering validation study where a small number of specific linear contrasts are pre-registered in the study protocol prior to data inspection, the Bonferroni (or Holm–Bonferroni step-down) procedure provides sharp, easily computed simultaneous intervals with minimal loss of statistical power. Conversely, in exploratory observational studies where researchers examine numerous post-hoc subgroup comparisons, pairwise treatment differences, and multi-parameter contrasts suggested by the observed data themselves, pre-planned multiplicity adjustments are invalid because the effective number of implicit comparisons is unbounded. In such post-hoc settings, Scheffé's $S$-method provides an ironclad mathematical guarantee that the familywise error rate across all infinitely many linear combinations in the contrast subspace will never exceed the nominal significance level.

## 3.6 Mean Response Estimation, Prediction Intervals, Hidden Extrapolation & Asymptotic Inference

Extending Section 1.6 to the general $p$-parameter multiple regression model, suppose we specify a target covariate vector $\mathbf{x}_0 = (1, x_{01}, x_{02}, \dots, x_{0k})^T \in \mathbb{R}^p$. We distinguish once again between estimating the deterministic conditional mean response $\mu_{Y \mid \mathbf{x}_0} = \mathbb{E}[Y \mid \mathbf{x}_0] = \mathbf{x}_0^T \boldsymbol{\beta}$ and predicting a future random realization $Y_{\text{new}} = \mathbf{x}_0^T \boldsymbol{\beta} + \varepsilon_{\text{new}}$, where $\varepsilon_{\text{new}} \sim \mathcal{N}(0, \sigma^2)$ is independent of the historical training sample $\mathbf{Y}$.

The BLUE point estimator of $\mu_{Y \mid \mathbf{x}_0}$ (and minimum-MSE linear unbiased predictor of $Y_{\text{new}}$) is:

$$\hat{Y}_0 = \mathbf{x}_0^T \hat{\boldsymbol{\beta}}$$

Define the **out-of-sample leverage** at $\mathbf{x}_0$ as the quadratic form $h_{00} = \mathbf{x}_0^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_0$. The sampling variance of $\hat{Y}_0$ and the variance of the prediction error $Y_{\text{new}} - \hat{Y}_0$ are:

$$\text{Var}(\hat{Y}_0) = \sigma^2 \mathbf{x}_0^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_0 = \sigma^2 h_{00}, \qquad \text{Var}(Y_{\text{new}} - \hat{Y}_0) = \sigma^2 + \sigma^2 \mathbf{x}_0^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_0 = \sigma^2 (1 + h_{00})$$

Consequently, the exact $100(1 - \alpha)\%$ **Confidence Interval for $\mathbb{E}[Y \mid \mathbf{x}_0]$** and **Prediction Interval for $Y_{\text{new}}$** are:

$$\text{Mean CI}: \quad \mathbf{x}_0^T \hat{\boldsymbol{\beta}} \pm t_{\alpha/2, \, n-p} \, s \sqrt{\mathbf{x}_0^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_0}, \qquad \text{Prediction Interval}: \quad \mathbf{x}_0^T \hat{\boldsymbol{\beta}} \pm t_{\alpha/2, \, n-p} \, s \sqrt{1 + \mathbf{x}_0^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_0}$$

If we wish to construct simultaneous prediction intervals for $m$ independent future observations at $\mathbf{x}_{0(1)}, \dots, \mathbf{x}_{0(m)}$, we apply either the Bonferroni multiplier $t_{\alpha/(2m), n-p}$ or the Scheffé simultaneous prediction multiplier $\sqrt{m F_{\alpha, m, n-p}}$ to $s\sqrt{1 + \mathbf{x}_{0(j)}^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_{0(j)}}$.

### The Geometry of Hidden Extrapolation and the Minimum-Volume Regressor Ellipsoid
In simple linear regression ($k = 1$), detecting whether a target point $x_0$ represents an dangerous extrapolation is trivial: one simply checks whether $x_0$ lies outside the sample range $[x_{\min}, x_{\max}]$. In multiple linear regression ($k \ge 2$), checking whether each individual coordinate $x_{0j}$ falls inside its marginal interval $[x_{j, \min}, x_{j, \max}]$ is **grossly insufficient**! When predictors $X_1, \dots, X_k$ are correlated, the historical sample points occupy a narrow, tilted cigar-shaped region inside the $k$-dimensional hyper-rectangle $\prod_{j=1}^k [x_{j, \min}, x_{j, \max}]$. A target point $\mathbf{x}_0$ can have every coordinate well within its individual marginal range and yet lie completely outside the joint multidimensional cloud of observed data—a perilous phenomenon called **hidden extrapolation**.

To detect hidden extrapolation rigorously without relying on two-dimensional scatterplots, Weisberg and Montgomery define the **Regressor Variable Hull (RVH)** as the smallest convex hull or minimum-volume ellipsoid enclosing the $n$ observed sample points $\mathbf{x}_1, \dots, \mathbf{x}_n$. Because the diagonal elements of the Hat matrix are $h_{ii} = \mathbf{x}_i^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_i$, let $h_{\max} = \max_{1 \le i \le n} h_{ii}$ be the maximum leverage observed in the training sample. The **Regressor Variable Ellipsoid** is defined as the set of all covariate vectors $\mathbf{x}_0$ whose leverage does not exceed $h_{\max}$:

$$\mathcal{R}_{\text{RVH}} = \left\{ \mathbf{x}_0 \in \mathbb{R}^p : h_{00} = \mathbf{x}_0^T (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{x}_0 \le h_{\max} \right\}$$

Whenever a proposed forecast point $\mathbf{x}_0$ yields $h_{00} > h_{\max}$, $\mathbf{x}_0$ lies further from the multivariate sample centroid (in Mahalanobis distance) than any observation in the training dataset, signaling hidden extrapolation.

### Asymptotic Inference Under Non-Normal Errors and Likelihood Ratio, Wald & Lagrange Multiplier Trinity

What happens to the $t$-tests, $F$-tests, and confidence intervals of Sections 3.1–3.6 when the classical Gauss–Markov assumptions A1–A5 hold ($\mathbb{E}[\boldsymbol{\varepsilon}] = \mathbf{0}_n$, $\text{Cov}(\boldsymbol{\varepsilon}) = \sigma^2 \mathbf{I}_n$), but Assumption A6 fails—meaning the error terms $\varepsilon_i$ are **non-normal** (for example, skewed exponential, heavy-tailed Student-$t$, or bounded uniform disturbances)?

In finite samples without normality, $\hat{\boldsymbol{\beta}}$ remains unbiased and BLUE by the Gauss–Markov Theorem, and $s^2 = \text{SSE}/(n-p)$ remains exactly unbiased for $\sigma^2$, but $\hat{\boldsymbol{\beta}}$ is no longer exactly multivariate normal and $\text{SSE}/\sigma^2$ is no longer exactly chi-square. However, as the sample size $n \to \infty$, large-sample **asymptotic distribution theory** rescues classical regression inference under mild regularity conditions on the sequence of design matrices $\mathbf{X}_n \in \mathbb{R}^{n \times p}$, known as the **Grenander–Noether Conditions**:
1. **Asymptotic Stability of the Gram Matrix**: As $n \to \infty$, the average cross-product matrix converges to a finite, symmetric, strictly positive definite $p \times p$ limit matrix $\mathbf{Q}$:
   $$\lim_{n \to \infty} \frac{1}{n} \mathbf{X}_n^T \mathbf{X}_n = \mathbf{Q} \succ \mathbf{0}_{p \times p}$$
   Note that this condition implies $(\mathbf{X}_n^T \mathbf{X}_n)^{-1} = \frac{1}{n} \mathbf{Q}_n^{-1} \to \mathbf{0}_{p \times p}$, so $\text{Cov}(\hat{\boldsymbol{\beta}}_n) = \sigma^2(\mathbf{X}_n^T\mathbf{X}_n)^{-1} \to \mathbf{0}_{p \times p}$. By Chebyshev's inequality, vanishing variance plus zero bias immediately guarantees that $\hat{\boldsymbol{\beta}}_n$ is **weakly consistent**: $\hat{\boldsymbol{\beta}}_n \xrightarrow{P} \boldsymbol{\beta}$.
2. **Vanishing Maximum Leverage (Lindeberg Condition)**: No single observation dominates the sample asymptotically, meaning the maximum diagonal element of the Hat matrix converges to zero:
   $$\lim_{n \to \infty} \max_{1 \le i \le n} h_{ii}^{(n)} = \lim_{n \to \infty} \max_{1 \le i \le n} \frac{1}{n} \mathbf{x}_i^T \left(\frac{1}{n}\mathbf{X}_n^T\mathbf{X}_n\right)^{-1} \mathbf{x}_i = 0$$

Under these conditions, if $\varepsilon_1, \dots, \varepsilon_n$ are i.i.d. with mean $0$ and finite variance $\sigma^2 \in (0, \infty)$, the **Lindeberg–Feller Multivariate Central Limit Theorem** applies to the scaled sum $\frac{1}{\sqrt{n}} \mathbf{X}_n^T \boldsymbol{\varepsilon} = \frac{1}{\sqrt{n}} \sum_{i=1}^n \mathbf{x}_i \varepsilon_i$, establishing **asymptotic normality** of the OLS estimator:

$$\sqrt{n} \left( \hat{\boldsymbol{\beta}}_n - \boldsymbol{\beta} \right) = \left( \frac{1}{n} \mathbf{X}_n^T \mathbf{X}_n \right)^{-1} \left( \frac{1}{\sqrt{n}} \mathbf{X}_n^T \boldsymbol{\varepsilon} \right) \xrightarrow{d} \mathcal{N}_p \left( \mathbf{0}_p, \; \sigma^2 \mathbf{Q}^{-1} \right)$$

Simultaneously, by the Weak Law of Large Numbers, $s_n^2 = \frac{1}{n-p}\boldsymbol{\varepsilon}^T(\mathbf{I}_n - \mathbf{H}_n)\boldsymbol{\varepsilon} = \frac{n}{n-p}\left(\frac{1}{n}\boldsymbol{\varepsilon}^T\boldsymbol{\varepsilon} - \frac{1}{n}\boldsymbol{\varepsilon}^T\mathbf{H}_n\boldsymbol{\varepsilon}\right) \xrightarrow{P} \sigma^2$ is a consistent estimator of $\sigma^2$. By **Slutsky's Theorem** and the **Continuous Mapping Theorem**, under $H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d}$:

$$W_n = q F_n = \frac{(\mathbf{C}\hat{\boldsymbol{\beta}}_n - \mathbf{d})^T \left[ \mathbf{C}(\mathbf{X}_n^T\mathbf{X}_n)^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}}_n - \mathbf{d})}{s_n^2} \xrightarrow{d} \chi_q^2$$

and $F_n = W_n / q \xrightarrow{d} \chi_q^2 / q$. Notice that as the denominator degrees of freedom $n - p \to \infty$, the random variable $F_{q, n-p}$ converges in distribution to $\chi_q^2 / q$! Therefore, the classical $t$-tests and $F$-tests are **asymptotically valid** for arbitrary non-normal error distributions with finite variance. (Caution: single-observation *prediction intervals* $\hat{y}_0 \pm t_{\alpha/2} s \sqrt{1 + h_{00}}$ still rely on the normality of the individual future error $\varepsilon_{\text{new}}$, because a single error $\varepsilon_{\text{new}}$ is not averaged by a Central Limit Theorem!).

Finally, in large-sample econometrics, testing $H_0: \mathbf{C}\boldsymbol{\beta} = \mathbf{d}$ can be conducted via any of the **Asymptotic Trinity of Tests**:
1. **Wald Statistic ($W$)**: Computed solely from the unrestricted model: $W = n (\text{SSE}_R - \text{SSE}_F) / \text{SSE}_F = \frac{n}{n-p} q F$.
2. **Likelihood Ratio Statistic ($LR$)**: $LR = n \ln(\text{SSE}_R / \text{SSE}_F) = n \ln\!\left(1 + \frac{W}{n}\right)$.
3. **Lagrange Multiplier / Score Statistic ($LM$)**: Computed solely from the restricted model: $LM = n (\text{SSE}_R - \text{SSE}_F) / \text{SSE}_R = \frac{W}{1 + W/n} = n R_{\text{aux}}^2$, where $R_{\text{aux}}^2$ is the uncentered $R^2$ from regressing the restricted residuals $\mathbf{e}_R$ on $\mathbf{X}$.

In every linear regression model of sample size $n$, these three statistics obey the exact deterministic algebraic inequality:

$$W \ge LR \ge LM$$

while all three converge in distribution to the identical $\chi_q^2$ limit under $H_0$ as $n \to \infty$, since $W - LR = O_p(n^{-1})$ and $LR - LM = O_p(n^{-1})$.

### Asymptotic Robustness and the Role of Heteroscedasticity-Consistent Inference
The asymptotic convergence results grounded in the Grenander–Noether conditions and the Lindeberg–Feller Central Limit Theorem explain why classical regression inference remains the workhorse of applied econometrics and social science even when disturbances depart from exact Gaussianity. Provided the sample size is moderately large and no single observation exercises asymptotically dominant leverage, the sampling distribution of the Ordinary Least Squares estimator is closely approximated by a multivariate normal distribution regardless of skewness or kurtosis in the error distribution. Crucially, however, asymptotic validity of the standard $t$-tests and $F$-tests still requires that the error variance be constant across observations (homoscedasticity); when error variance varies systematically with the predictors, the classical covariance formula remains inconsistent even in infinitely large samples, motivating the Generalized Least Squares and Huber–Eicker–White sandwich estimators developed in Unit 5.

## Fully worked question 1: General Linear Hypothesis F-Test, Restricted Least Squares Estimator, and Equivalence of Wald and Extra-SS Forms

### Question
An econometric study of $n = 24$ regional manufacturing sectors estimates a Cobb–Douglas production function $\ln(Y_i) = \beta_0 + \beta_1 \ln(K_i) + \beta_2 \ln(L_i) + \beta_3 \ln(E_i) + \varepsilon_i$ ($p = 4$), relating log output $\ln(Y)$ to log capital $\ln(K)$, log labor $\ln(L)$, and log energy $\ln(E)$. The unrestricted Ordinary Least Squares estimate $\hat{\boldsymbol{\beta}}$, the Residual Sum of Squares $\text{SSE}_F$, and the inverse Gram matrix $(\mathbf{X}^T\mathbf{X})^{-1}$ are:

$$\hat{\boldsymbol{\beta}} = \begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \\ \hat{\beta}_2 \\ \hat{\beta}_3 \end{pmatrix} = \begin{pmatrix} 2.00 \\ 0.45 \\ 0.55 \\ 0.20 \end{pmatrix}, \quad \text{SSE}_F = 4.00, \quad (\mathbf{X}^T\mathbf{X})^{-1} = \begin{pmatrix} 0.50 & -0.05 & -0.05 & 0.00 \\ -0.05 & 0.10 & -0.02 & 0.00 \\ -0.05 & -0.02 & 0.10 & 0.00 \\ 0.00 & 0.00 & 0.00 & 0.04 \end{pmatrix}$$

1. Test the **Constant Returns to Scale (CRS)** hypothesis $H_0: \beta_1 + \beta_2 + \beta_3 = 1$ against $H_1: \beta_1 + \beta_2 + \beta_3 \neq 1$ at $\alpha = 0.05$ using the General Linear Hypothesis $F$-test (and equivalent $t$-test), given $F_{0.05, 1, 20} = 4.351$ ($t_{0.025, 20} = 2.086$).
2. Compute the exact **Restricted Least Squares (RLS) estimator** $\hat{\boldsymbol{\beta}}_R$ under the constraint $\beta_1 + \beta_2 + \beta_3 = 1$, and determine the Restricted Residual Sum of Squares $\text{SSE}_R$.
3. Now test the joint two-degree-of-freedom structural hypothesis $H_0: \beta_1 = \beta_2 \text{ and } \beta_1 + \beta_2 + \beta_3 = 1$ at $\alpha = 0.05$ (given $F_{0.05, 2, 20} = 3.493$).

### Solution, step 1: Test Constant Returns to Scale H_0: beta_1 + beta_2 + beta_3 = 1
With $n = 24$ and $p = 4$, the error degrees of freedom are $n - p = 24 - 4 = 20$, and the unrestricted Mean Square Error is:

$$s^2 = \text{MSE}_F = \frac{\text{SSE}_F}{n - p} = \frac{4.00}{20} = 0.20$$

For $H_0: \beta_1 + \beta_2 + \beta_3 = 1$, we have $q = 1$, contrast row vector $\mathbf{C} = (0, 1, 1, 1)$, and target $d = 1$. The sample linear combination and its discrepancy from $d = 1$ are:

$$\mathbf{C}\hat{\boldsymbol{\beta}} = 0(2.00) + 1(0.45) + 1(0.55) + 1(0.20) = 1.20 \implies \mathbf{C}\hat{\boldsymbol{\beta}} - d = 1.20 - 1.00 = 0.20$$

Next, we compute the scalar quadratic form $\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T$, which is the sum of all entries in the lower-right $3 \times 3$ slope submatrix of $(\mathbf{X}^T\mathbf{X})^{-1}$:

$$\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T = (0.10 - 0.02 + 0.00) + (-0.02 + 0.10 + 0.00) + (0.00 + 0.00 + 0.04) = 0.08 + 0.08 + 0.04 = 0.20$$

Wait—let us also write out the full product $\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}$ as a $1 \times 4$ vector because we will need its transpose $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T$ in Step 2:

$$\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1} = \begin{pmatrix} 0 & 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 0.50 & -0.05 & -0.05 & 0.00 \\ -0.05 & 0.10 & -0.02 & 0.00 \\ -0.05 & -0.02 & 0.10 & 0.00 \\ 0.00 & 0.00 & 0.00 & 0.04 \end{pmatrix} = \begin{pmatrix} -0.10 & 0.08 & 0.08 & 0.04 \end{pmatrix}$$

Multiplying by $\mathbf{C}^T = (0, 1, 1, 1)^T$ confirms $\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T = 0.08 + 0.08 + 0.04 = 0.20$. Therefore, the numerator sum of squares $Q_H$ and the $F$-statistic are:

$$Q_H = \frac{(\mathbf{C}\hat{\boldsymbol{\beta}} - d)^2}{\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T} = \frac{(0.20)^2}{0.20} = \frac{0.04}{0.20} = 0.20, \qquad F = \frac{Q_H / 1}{s^2} = \frac{0.20}{0.20} = 1.00$$

Equivalently, $\text{SE}(\mathbf{C}\hat{\boldsymbol{\beta}}) = \sqrt{s^2 \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T} = \sqrt{(0.20)(0.20)} = 0.20$, so $t = \frac{1.20 - 1.00}{0.20} = 1.00$ and $F = t^2 = 1.00$. Since $F = 1.00 < F_{0.05, 1, 20} = 4.351$, we fail to reject $H_0$: the data are consistent with Constant Returns to Scale.

### Solution, step 2: Compute the Restricted Least Squares (RLS) estimator beta_hat_R and SSE_R
Applying the Restricted Least Squares formula from Section 3.2:

$$\hat{\boldsymbol{\beta}}_R = \hat{\boldsymbol{\beta}} - (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \left[ \mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T \right]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - d)$$

Since $[\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T]^{-1} (\mathbf{C}\hat{\boldsymbol{\beta}} - d) = (0.20)^{-1}(0.20) = 1.00$, and $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T = (-0.10, 0.08, 0.08, 0.04)^T$, we obtain:

$$\hat{\boldsymbol{\beta}}_R = \begin{pmatrix} 2.00 \\ 0.45 \\ 0.55 \\ 0.20 \end{pmatrix} - (1.00) \begin{pmatrix} -0.10 \\ 0.08 \\ 0.08 \\ 0.04 \end{pmatrix} = \begin{pmatrix} 2.10 \\ 0.37 \\ 0.47 \\ 0.16 \end{pmatrix}$$

Let us check the constraint on $\hat{\boldsymbol{\beta}}_R$: $\hat{\beta}_{1,R} + \hat{\beta}_{2,R} + \hat{\beta}_{3,R} = 0.37 + 0.47 + 0.16 = 1.00$, which satisfies the CRS restriction! And the Restricted Residual Sum of Squares is:

$$\text{SSE}_R = \text{SSE}_F + Q_H = 4.00 + 0.20 = 4.20$$

### Solution, step 3: Test the joint 2-df hypothesis H_0: beta_1 = beta_2 and beta_1 + beta_2 + beta_3 = 1
For the joint hypothesis $H_0: \beta_1 - \beta_2 = 0$ and $\beta_1 + \beta_2 + \beta_3 = 1$, we have $q = 2$ linearly independent rows:

$$\mathbf{C} = \begin{pmatrix} 0 & 1 & -1 & 0 \\ 0 & 1 & 1 & 1 \end{pmatrix}, \qquad \mathbf{d} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \qquad \mathbf{C}\hat{\boldsymbol{\beta}} - \mathbf{d} = \begin{pmatrix} 0.45 - 0.55 - 0 \\ 1.20 - 1.00 \end{pmatrix} = \begin{pmatrix} -0.10 \\ 0.20 \end{pmatrix}$$

We compute $\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}$:
- Row 1: $(0, 1, -1, 0)(\mathbf{X}^T\mathbf{X})^{-1} = (-0.05 - (-0.05), \; 0.10 - (-0.02), \; -0.02 - 0.10, \; 0) = (0.00, \; 0.12, \; -0.12, \; 0.00)$.
- Row 2: $(-0.10, \; 0.08, \; 0.08, \; 0.04)$ (from Step 1).

Multiplying by $\mathbf{C}^T$ gives the $2 \times 2$ matrix $\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T$:

$$\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T = \begin{pmatrix} 0.00 & 0.12 & -0.12 & 0.00 \\ -0.10 & 0.08 & 0.08 & 0.04 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 1 & 1 \\ -1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0.24 & 0.00 \\ 0.00 & 0.20 \end{pmatrix}$$

Because the two contrasts are mutually orthogonal in the metric of $(\mathbf{X}^T\mathbf{X})^{-1}$, $\mathbf{C}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{C}^T$ is diagonal! Thus $Q_H$ is simply the sum of the two separate quadratic forms:

$$Q_H = \begin{pmatrix} -0.10 & 0.20 \end{pmatrix} \begin{pmatrix} 1/0.24 & 0 \\ 0 & 1/0.20 \end{pmatrix} \begin{pmatrix} -0.10 \\ 0.20 \end{pmatrix} = \frac{(-0.10)^2}{0.24} + \frac{(0.20)^2}{0.20} = 0.04167 + 0.20000 = 0.24167$$

The $F$-statistic with $q = 2$ and $n - p = 20$ degrees of freedom is:

$$F = \frac{Q_H / 2}{s^2} = \frac{0.24167 / 2}{0.20} = \frac{0.12083}{0.20} = 0.6042$$

Since $F = 0.6042 < F_{0.05, 2, 20} = 3.493$, we fail to reject the joint hypothesis at the $5\%$ significance level.

## Fully worked question 2: Simultaneous Confidence Intervals: Comparing Pointwise t, Bonferroni, and Scheffe S-Method Multipliers

### Question
In a clinical pharmacology dose-response study with $n = 35$ patients and $p = 5$ parameters ($\beta_0, \beta_1, \beta_2, \beta_3, \beta_4$), the estimated slope vector for the $k = 4$ active biomarkers, the residual mean square $s^2 = \text{MSE}$, and the $4 \times 4$ slope submatrix of $(\mathbf{X}^T\mathbf{X})^{-1}$ are:

$$\begin{pmatrix} \hat{\beta}_1 \\ \hat{\beta}_2 \\ \hat{\beta}_3 \\ \hat{\beta}_4 \end{pmatrix} = \begin{pmatrix} 4.20 \\ 2.80 \\ -1.50 \\ 0.90 \end{pmatrix}, \quad s^2 = 4.00 \quad (\text{df} = 30), \quad \left[(\mathbf{X}^T\mathbf{X})^{-1}\right]_{1:4, 1:4} = \begin{pmatrix} 0.09 & 0.02 & 0.00 & 0.00 \\ 0.02 & 0.16 & 0.00 & 0.00 \\ 0.00 & 0.00 & 0.25 & -0.05 \\ 0.00 & 0.00 & -0.05 & 0.04 \end{pmatrix}$$

Suppose the research team pre-specifies a family of $m = 4$ linear parametric functions of interest:
$$\theta_1 = \beta_1, \qquad \theta_2 = \beta_2, \qquad \theta_3 = \beta_1 - \beta_2, \qquad \theta_4 = \beta_3 - \beta_4$$

1. Compute the point estimates $\hat{\theta}_1, \hat{\theta}_2, \hat{\theta}_3, \hat{\theta}_4$ and their exact standard errors $\text{SE}(\hat{\theta}_j)$ ($j = 1, 2, 3, 4$).
2. Compare the critical multipliers for $95\%$ confidence ($\alpha = 0.05$, $\text{df} = n - p = 30$) under (a) unadjusted pointwise Student-$t$ ($t_{0.025, 30} = 2.042$), (b) Bonferroni for $m = 4$ comparisons ($t_{0.05/8, 30} = t_{0.00625, 30} = 2.659$), and (c) Scheffé's $S$-method across the $q = 4$-dimensional slope subspace ($F_{0.05, 4, 30} = 2.690$). Construct the $95\%$ Bonferroni and Scheffé simultaneous intervals for all four parameters.
3. How many contrasts $m$ would the investigators have to test before Scheffé's $S$-method provides narrower simultaneous confidence intervals than the Bonferroni method?

### Solution, step 1: Calculate point estimates and exact standard errors for the four contrasts
With $s^2 = 4.00$, the residual standard deviation is $s = \sqrt{4.00} = 2.00$. Using $\text{SE}(\mathbf{c}^T\hat{\boldsymbol{\beta}}) = s \sqrt{\mathbf{c}^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{c}}$:
1. **$\theta_1 = \beta_1$**:
   $$\hat{\theta}_1 = 4.20, \qquad \text{SE}(\hat{\theta}_1) = 2.00 \sqrt{0.09} = 2.00(0.30) = 0.60$$
2. **$\theta_2 = \beta_2$**:
   $$\hat{\theta}_2 = 2.80, \qquad \text{SE}(\hat{\theta}_2) = 2.00 \sqrt{0.16} = 2.00(0.40) = 0.80$$
3. **$\theta_3 = \beta_1 - \beta_2$**:
   $$\hat{\theta}_3 = 4.20 - 2.80 = 1.40, \qquad \text{SE}(\hat{\theta}_3) = 2.00 \sqrt{c_{11} + c_{22} - 2 c_{12}} = 2.00 \sqrt{0.09 + 0.16 - 2(0.02)} = 2.00 \sqrt{0.21} \approx 0.9165$$
4. **$\theta_4 = \beta_3 - \beta_4$**:
   $$\hat{\theta}_4 = -1.50 - 0.90 = -2.40, \qquad \text{SE}(\hat{\theta}_4) = 2.00 \sqrt{c_{33} + c_{44} - 2 c_{34}} = 2.00 \sqrt{0.25 + 0.04 - 2(-0.05)} = 2.00 \sqrt{0.39} \approx 1.2490$$

### Solution, step 2: Compare critical multipliers and construct 95% Bonferroni and Scheffe intervals
We evaluate the three critical multipliers at $\alpha = 0.05$ with $\text{df} = 30$:
- **Unadjusted Pointwise $t$-Multiplier**: $t_{0.025, 30} = 2.042$ (does not control FWER; FWER can be up to $4 \times 0.05 = 0.20$).
- **Bonferroni Simultaneous Multiplier ($m = 4$)**: $B_{0.05} = t_{0.05/(2 \times 4), 30} = t_{0.00625, 30} = 2.659$.
- **Scheffé Simultaneous Multiplier ($q = 4$)**: $S_{0.05} = \sqrt{q F_{0.05, 4, 30}} = \sqrt{4(2.690)} = \sqrt{10.760} \approx 3.280$.

Because $B_{0.05} = 2.659 < S_{0.05} = 3.280$, the Bonferroni intervals are $(3.280 - 2.659)/3.280 = 18.9\%$ narrower than the Scheffé intervals while still guaranteeing at least $95\%$ simultaneous coverage for all four pre-planned contrasts:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Parameter $\theta_j$</th><th>Estimate $\hat{\theta}_j$</th><th>$\text{SE}(\hat{\theta}_j)$</th><th>95% Bonferroni Interval ($\pm 2.659 \, \text{SE}$)</th><th>95% Scheffé Interval ($\pm 3.280 \, \text{SE}$)</th></tr>
</thead>
<tbody>
<tr><td>$\theta_1 = \beta_1$</td><td>$4.20$</td><td>$0.6000$</td><td>$4.20 \pm 1.595 = [2.605, \; 5.795]$</td><td>$4.20 \pm 1.968 = [2.232, \; 6.168]$</td></tr>
<tr><td>$\theta_2 = \beta_2$</td><td>$2.80$</td><td>$0.8000$</td><td>$2.80 \pm 2.127 = [0.673, \; 4.927]$</td><td>$2.80 \pm 2.624 = [0.176, \; 5.424]$</td></tr>
<tr><td>$\theta_3 = \beta_1 - \beta_2$</td><td>$1.40$</td><td>$0.9165$</td><td>$1.40 \pm 2.437 = [-1.037, \; 3.837]$</td><td>$1.40 \pm 3.006 = [-1.606, \; 4.406]$</td></tr>
<tr><td>$\theta_4 = \beta_3 - \beta_4$</td><td>$-2.40$</td><td>$1.2490$</td><td>$-2.40 \pm 3.321 = [-5.721, \; 0.921]$</td><td>$-2.40 \pm 4.097 = [-6.497, \; 1.697]$</td></tr>
</tbody>
</table></div>

### Solution, step 3: Determine the crossover threshold m where Scheffe beats Bonferroni
Scheffé's multiplier $S_{0.05} = 3.280$ remains constant regardless of how many contrasts $m$ are examined inside the $q = 4$-dimensional slope subspace, whereas the Bonferroni multiplier $t_{0.05/(2m), 30}$ grows monotonically with $m$. We solve for $m$ such that:

$$t_{0.05/(2m), \, 30} > 3.280$$

In the Student $t_{30}$ distribution, the upper tail probability $\mathbb{P}(T_{30} > 3.280)$ equals $0.00131$. Setting $\frac{0.05}{2m} < 0.00131$:

$$m > \frac{0.05}{2(0.00131)} \approx 19.08 \implies m \ge 20$$

Thus, for any pre-planned family of $m \le 19$ contrasts, Bonferroni yields shorter intervals; if the researchers examine $m \ge 20$ contrasts (or perform unrestricted post-hoc exploration across the parameter space), Scheffé's $S$-method is strictly superior.

## Fully worked question 3: Joint Confidence Ellipsoid vs Marginal t-Intervals Paradox and Hidden Extrapolation Detection

### Question
Consider a two-predictor multiple linear regression model $Y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \varepsilon_i$ fitted to $n = 23$ observations ($\text{df} = 20$), where the predictors $x_{i1}$ and $x_{i2}$ are centered ($\bar{x}_1 = \bar{x}_2 = 0$) and strongly positively correlated ($r_{12} = 0.90$):

$$\mathbf{X}_c^T \mathbf{X}_c = \begin{pmatrix} 100 & 90 \\ 90 & 100 \end{pmatrix}, \quad \begin{pmatrix} \hat{\beta}_1 \\ \hat{\beta}_2 \end{pmatrix} = \begin{pmatrix} 0.40 \\ 0.40 \end{pmatrix}, \quad s^2 = \text{MSE} = 1.00$$

1. Compute the $2 \times 2$ inverse matrix $(\mathbf{X}_c^T \mathbf{X}_c)^{-1}$, find the individual standard errors $\text{SE}(\hat{\beta}_1)$ and $\text{SE}(\hat{\beta}_2)$, and test $H_0: \beta_1 = 0$ and $H_0: \beta_2 = 0$ separately at $\alpha = 0.05$ ($t_{0.025, 20} = 2.086$).
2. Now test the joint hypothesis $H_0: \beta_1 = \beta_2 = 0$ using the $2$-df $F$-test ($F_{0.05, 2, 20} = 3.493$) by evaluating whether $(\beta_1, \beta_2) = (0, 0)$ lies inside the $95\%$ joint confidence ellipse. Explain geometrically why $(0,0)$ is strongly rejected jointly even though neither $\beta_1$ nor $\beta_2$ is individually significant!
3. Suppose the maximum sample leverage is $h_{\max} = 0.35$. Determine whether predicting at two candidate centered covariate vectors $\mathbf{x}_{c, A} = (2.5, 2.5)^T$ and $\mathbf{x}_{c, B} = (2.5, -2.5)^T$ constitutes **hidden extrapolation** (note: don't forget the intercept term $1/n = 1/23 \approx 0.0435$ in $h_{00}$).

### Solution, step 1: Compute (X_c^T X_c)^(-1) and conduct the two individual marginal t-tests
The determinant of $\mathbf{X}_c^T \mathbf{X}_c$ is $(100)(100) - (90)^2 = 10000 - 8100 = 1900$. Therefore:

$$(\mathbf{X}_c^T \mathbf{X}_c)^{-1} = \frac{1}{1900} \begin{pmatrix} 100 & -90 \\ -90 & 100 \end{pmatrix} = \begin{pmatrix} 1/19 & -9/190 \\ -9/190 & 1/19 \end{pmatrix} \approx \begin{pmatrix} 0.05263 & -0.04737 \\ -0.04737 & 0.05263 \end{pmatrix}$$

With $s^2 = 1.00$, the individual standard errors of $\hat{\beta}_1$ and $\hat{\beta}_2$ are:

$$\text{SE}(\hat{\beta}_1) = \text{SE}(\hat{\beta}_2) = \sqrt{1.00 \times \frac{1}{19}} = \frac{1}{\sqrt{19}} \approx 0.2294$$

Testing $H_0: \beta_1 = 0$ and $H_0: \beta_2 = 0$ individually yields the marginal $t$-statistics:

$$t_1 = \frac{0.40}{0.2294} = 1.7436, \qquad t_2 = \frac{0.40}{0.2294} = 1.7436$$

Because $|t_1| = |t_2| = 1.7436 < t_{0.025, 20} = 2.086$, **neither $\beta_1$ nor $\beta_2$ is statistically significant** on its own ($95\%$ marginal confidence intervals are $0.40 \pm 2.086(0.2294) = [-0.0785, \, 0.8785]$, both of which contain $0$).

### Solution, step 2: Evaluate the joint confidence ellipse and explain the collinearity paradox
To test $H_0: (\beta_1, \beta_2)^T = (0, 0)^T$ jointly, we evaluate the quadratic form $(\hat{\boldsymbol{\beta}}_c - \mathbf{0})^T (\mathbf{X}_c^T \mathbf{X}_c) (\hat{\boldsymbol{\beta}}_c - \mathbf{0})$:

$$Q_H = \begin{pmatrix} 0.40 & 0.40 \end{pmatrix} \begin{pmatrix} 100 & 90 \\ 90 & 100 \end{pmatrix} \begin{pmatrix} 0.40 \\ 0.40 \end{pmatrix} = 100(0.16) + 2(90)(0.16) + 100(0.16) = 16.0 + 28.8 + 16.0 = 60.80$$

Dividing by $q s^2 = 2(1.00) = 2.00$ gives the exact $F$-statistic:

$$F = \frac{Q_H / 2}{s^2} = \frac{60.80}{2.00} = 30.40 \gg F_{0.05, 2, 20} = 3.493$$

The joint $F$-test is overwhelmingly significant ($p < 0.0001$), and $(0, 0)$ lies **far outside** the $95\%$ joint confidence ellipse (whose boundary is $Q_H \le 2(1.00)(3.493) = 6.986$)!

**Geometric Explanation**: Because $r_{12} = +0.90$, the correlation between $\hat{\beta}_1$ and $\hat{\beta}_2$ is $\rho(\hat{\beta}_1, \hat{\beta}_2) = -0.90$. The $95\%$ confidence ellipse is a narrow cigar tilted along the line $\beta_1 + \beta_2 = 0.80$. Along the direction $\beta_1 + \beta_2$, the variance is tiny: $\text{Var}(\hat{\beta}_1 + \hat{\beta}_2) = \frac{100 + 100 - 180}{1900} = \frac{20}{1900} \approx 0.0105$, so $\beta_1 + \beta_2 = 0.80$ is estimated with extreme precision ($\text{SE} = 0.1026$, $t = 7.80$), ruling out $(0,0)$. Along the orthogonal direction $\beta_1 - \beta_2$, the variance is $19$ times larger ($\frac{380}{1900} = 0.20$), inflating the marginal projections onto the individual axes.

### Solution, step 3: Detect hidden extrapolation at x_{c,A} and x_{c,B} via out-of-sample leverage
For a centered predictor model, the out-of-sample leverage at $\mathbf{x}_0 = (1, \mathbf{x}_{c,0}^T)^T$ is:

$$h_{00} = \frac{1}{n} + \mathbf{x}_{c,0}^T (\mathbf{X}_c^T \mathbf{X}_c)^{-1} \mathbf{x}_{c,0}$$

1. **Candidate Point A: $\mathbf{x}_{c, A} = (2.5, 2.5)^T$** (moving in the direction of positive correlation $x_1 = x_2$):
   $$h_{00, A} = \frac{1}{23} + \frac{1}{1900} \begin{pmatrix} 2.5 & 2.5 \end{pmatrix} \begin{pmatrix} 100 & -90 \\ -90 & 100 \end{pmatrix} \begin{pmatrix} 2.5 \\ 2.5 \end{pmatrix} = 0.0435 + \frac{6.25(100 - 90 - 90 + 100)}{1900} = 0.0435 + \frac{125}{1900} = 0.0435 + 0.0658 = 0.1093$$
   Since $h_{00, A} = 0.1093 \le h_{\max} = 0.35$, Point A lies **well inside** the Regressor Variable Ellipsoid (interpolation).

2. **Candidate Point B: $\mathbf{x}_{c, B} = (2.5, -2.5)^T$** (Notice that the marginal magnitudes $|x_{1}| = 2.5$ and $|x_{2}| = 2.5$ are identical to Point A, but move against the positive correlation $x_1 = -x_2$):
   $$h_{00, B} = \frac{1}{23} + \frac{1}{1900} \begin{pmatrix} 2.5 & -2.5 \end{pmatrix} \begin{pmatrix} 100 & -90 \\ -90 & 100 \end{pmatrix} \begin{pmatrix} 2.5 \\ -2.5 \end{pmatrix} = 0.0435 + \frac{6.25(100 + 90 + 90 + 100)}{1900} = 0.0435 + \frac{2375}{1900} = 0.0435 + 1.2500 = 1.2935$$
   Since $h_{00, B} = 1.2935 \gg h_{\max} = 0.35$, Point B is a **severe hidden extrapolation**! Its prediction variance $(1 + h_{00, B})\sigma^2 = 2.2935 \sigma^2$ is more than double that of Point A ($1.1093 \sigma^2$), even though both points have identical marginal coordinates $|x_j| = 2.5$.
