# Unit 1: Simple Linear Regression: OLS Estimation, Gauss-Markov Theorem, Normal Equations & ANOVA Decomposition

Simple linear regression forms the mathematical cornerstone of statistical modeling, econometric inference, and experimental calibration. Rather than treating two observable variables symmetrically as in bivariate correlation analysis, regression analysis establishes a directed functional architecture in which a continuous response variable $Y$ is modeled conditionally on a predictor or explanatory variable $X$. In this opening unit of the University of Dhaka Honours curriculum for Courses Stat H-303 and Stat H-312, we develop the complete theoretical apparatus of simple linear regression from first principles: conditional expectation functions, the classical Gauss–Markov assumptions, Ordinary Least Squares (OLS) optimization, exact algebraic orthogonality identities, finite-sample sampling distributions, the Gauss–Markov optimality proof, analysis of variance (ANOVA) partitioning, and simultaneous versus pointwise interval estimation.

## 1.1 Conditional Expectation Functions, Population Regression Lines, and Classical Gauss-Markov Assumptions

In scientific inquiry, deterministic physical laws postulate exact functional relationships between variables, such as Hooke's law relating spring elongation to applied force or Ohm's law relating electrical current to voltage. In statistical and observational sciences—ranging from agronomy and biostatistics to macroeconomics and industrial quality engineering—observable responses never adhere to a deterministic curve without variation. Even when the explanatory covariate $X$ is held fixed at a precise level $x$, repeated measurements of the response variable $Y$ exhibit stochastic dispersion driven by unmeasured biological heterogeneity, ambient environmental fluctuations, micro-level behavioral idiosyncrasies, and instrumentation measurement error.

To formalize this stochastic relationship on a rigorous probability space $(\Omega, \mathcal{F}, \mathbb{P})$, consider a pair of jointly distributed random variables $(X, Y)$ possessing a finite first conditional moment $\mathbb{E}[|Y| \mid X = x] < \infty$. The fundamental mathematical object governing regression theory is the **Conditional Expectation Function (CEF)**, denoted by $\mu(x)$:

$$\mu(x) = \mathbb{E}[Y \mid X = x] = \int_{-\infty}^{\infty} y \, f_{Y \mid X}(y \mid x) \, dy$$

for continuous random variables, with the integral replaced by a summation over the conditional probability mass function when $Y$ is discrete. The conditional expectation function $\mu(x)$ represents the systematic, predictable locus of the average response across subpopulations stratified by the covariate level $X = x$. A foundational justification for centering statistical regression around $\mu(x)$ arises from Hilbert space approximation theory: among all Borel-measurable functions $g(X)$ with finite second moment, the conditional expectation $\mu(X) = \mathbb{E}[Y \mid X]$ uniquely minimizes the expected squared prediction error:

$$\mathbb{E}\left[ (Y - g(X))^2 \right] = \mathbb{E}\left[ (Y - \mu(X) + \mu(X) - g(X))^2 \right] = \mathbb{E}\left[ (Y - \mu(X))^2 \right] + \mathbb{E}\left[ (\mu(X) - g(X))^2 \right]$$

where the cross-product term vanishes identically by the Law of Iterated Expectations, since $\mathbb{E}[(Y - \mu(X))(\mu(X) - g(X)) \mid X] = (\mu(X) - g(X)) \mathbb{E}[Y - \mu(X) \mid X] = 0$. Because the second term $\mathbb{E}[(\mu(X) - g(X))^2]$ is non-negative and equals zero if and only if $g(X) = \mu(X)$ almost surely, the CEF is the globally optimal mean-squared-error predictor of $Y$ given $X$.

In the **Simple Linear Regression Model (SLRM)**, we postulate that the population conditional expectation function is an affine linear function of the single covariate $x$:

$$\mathbb{E}[Y \mid X = x] = \beta_0 + \beta_1 x$$

Here, $\beta_0 \in \mathbb{R}$ is the **population intercept**, representing the expected response when the predictor equals zero ($x = 0$), and $\beta_1 \in \mathbb{R}$ is the **population slope**, measuring the marginal change in the expected response per unit increase in $x$:

$$\beta_1 = \frac{d}{dx} \mathbb{E}[Y \mid X = x] = \mathbb{E}[Y \mid X = x + 1] - \mathbb{E}[Y \mid X = x]$$

Notice that the word "linear" in linear regression refers strictly to **linearity in the unknown parameters** $(\beta_0, \beta_1)$, rather than linearity in the raw underlying physical measurement. For example, a relationship $Y_i = \beta_0 + \beta_1 \ln(U_i) + \varepsilon_i$ or $Y_i = \beta_0 + \beta_1 \cos(\omega t_i) + \varepsilon_i$ remains a simple linear regression model upon defining the transformed regressor $x_i = \ln(U_i)$ or $x_i = \cos(\omega t_i)$, whereas $Y_i = \beta_0 \exp(\beta_1 x_i) + \varepsilon_i$ is intrinsically nonlinear in the parameters.

For an observed sample of $n$ experimental units $(x_1, Y_1), (x_2, Y_2), \dots, (x_n, Y_n)$, we decompose each individual observation $Y_i$ into its deterministic systematic component $\mathbb{E}[Y_i \mid x_i]$ and an unobservable stochastic disturbance or random error term $\varepsilon_i = Y_i - \mathbb{E}[Y_i \mid x_i]$:

$$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad i = 1, 2, \dots, n$$

To establish exact finite-sample properties of estimators without initially imposing a specific parametric distribution (such as Gaussianity) on the errors, classical regression theory relies on the **Classical Gauss–Markov Assumptions**:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Assumption Code</th><th>Mathematical Formulation</th><th>Statistical &amp; Physical Interpretation</th></tr>
</thead>
<tbody>
<tr><td><strong>A1: Linearity in Parameters</strong></td><td>$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ for $i=1,\dots,n$</td><td>The true data-generating process is additive in the linear systematic signal $\beta_0 + \beta_1 x_i$ and the stochastic disturbance $\varepsilon_i$.</td></tr>
<tr><td><strong>A2: Non-Degenerate Design Variation</strong></td><td>$S_{xx} = \sum_{i=1}^n (x_i - \bar{x})^2 > 0$ ($n \ge 2$)</td><td>The predictor values $x_1, \dots, x_n$ are treated as fixed constants (or conditioned upon) and are not all identical; at least two $x_i$ values differ.</td></tr>
<tr><td><strong>A3: Zero Conditional Mean (Exogeneity)</strong></td><td>$\mathbb{E}[\varepsilon_i \mid x_1, \dots, x_n] = 0$ for all $i$</td><td>The disturbances have zero mean at every covariate configuration, ensuring $\mathbb{E}[Y_i \mid x_i] = \beta_0 + \beta_1 x_i$ without omitted-variable bias.</td></tr>
<tr><td><strong>A4: Homoscedasticity (Constant Variance)</strong></td><td>$\text{Var}(\varepsilon_i \mid x_1, \dots, x_n) = \sigma^2 \in (0, \infty)$</td><td>The dispersion of the stochastic error around the population regression line remains constant across all levels of the predictor $x_i$.</td></tr>
<tr><td><strong>A5: Non-Autocorrelation (Uncorrelated Errors)</strong></td><td>$\text{Cov}(\varepsilon_i, \varepsilon_j \mid x_1, \dots, x_n) = 0$ for $i \neq j$</td><td>Disturbances across distinct experimental units or time points are pairwise linearly uncorrelated, implying $\text{Cov}(Y_i, Y_j) = 0$ for $i \neq j$.</td></tr>
<tr><td><strong>A6: Gaussianity (Optional for Exact Inference)</strong></td><td>$\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$</td><td>Errors are independent and identically distributed normal variables, enabling exact finite-sample $t$-tests, $F$-tests, and confidence intervals.</td></tr>
</tbody>
</table></div>

When the regressors $X_i$ are random variables drawn from a bivariate population rather than pre-selected experimental levels, conditioning on the observed vector $\mathbf{x} = (x_1, \dots, x_n)^T$ allows all expectations and variances to be evaluated conditionally. So long as strict exogeneity $\mathbb{E}[\varepsilon_i \mid \mathbf{X}] = 0$ and conditional spherical variance $\text{Cov}(\boldsymbol{\varepsilon} \mid \mathbf{X}) = \sigma^2 \mathbf{I}_n$ hold, any estimator that is conditionally unbiased given $\mathbf{X}$ is also unconditionally unbiased by the Law of Iterated Expectations.

### Historical Genesis and Epistemological Distinction Between Regression and Correlation
The term "regression" entered statistical science through Sir Francis Galton's nineteenth-century biometric investigations of hereditary stature, in which he observed that the adult heights of offspring of extraordinarily tall or short parents tended to revert or "regress" toward the population mean height. While Galton and Karl Pearson initially framed this phenomenon within symmetric bivariate normal populations, modern statistical theory—crystallized by Ronald Fisher, Jerzy Neyman, and Trygve Haavelmo—strictly separates symmetric correlation analysis from asymmetric regression modeling. In correlation analysis, both variables are treated on an equal footing as random realizations from a joint distribution, and the sample correlation coefficient is invariant to interchanging the roles of the two variables. In regression analysis, by contrast, the explanatory variable is treated as an exogenous or conditioning input—either fixed by experimental protocol in a laboratory setting or observed prior to the realization of the outcome in an observational study—while the response variable carries the stochastic disturbance. This asymmetry explains why regressing response on predictor yields a line that minimizes vertical squared deviations, whereas regressing predictor on response minimizes horizontal squared deviations and produces a distinct geometric locus whenever the variables are imperfectly correlated.

## 1.2 Ordinary Least Squares (OLS) Derivation, Normal Equations, and Algebraic Orthogonality Properties

Given a realized sample of $n$ pairs $(x_1, y_1), \dots, (x_n, y_n)$, the true parameters $(\beta_0, \beta_1)$ and the true disturbances $\varepsilon_i$ are unobservable. If we propose candidate parameter values $(b_0, b_1) \in \mathbb{R}^2$, the resulting candidate fitted value for the $i$-th unit is $\hat{y}_i(b_0, b_1) = b_0 + b_1 x_i$, and the corresponding vertical deviation between the observed datum and the candidate line is $e_i(b_0, b_1) = y_i - (b_0 + b_1 x_i)$.

Proposed independently by Adrien-Marie Legendre (1805) and Carl Friedrich Gauss (1809) in the context of celestial mechanics and geodetic triangulation, the **Principle of Ordinary Least Squares (OLS)** selects the parameter estimators $(\hat{\beta}_0, \hat{\beta}_1)$ that minimize the sum of squared vertical deviations, denoted as the objective function $Q(b_0, b_1)$:

$$Q(b_0, b_1) = \sum_{i=1}^n \left[ y_i - (b_0 + b_1 x_i) \right]^2$$

Because $Q(b_0, b_1)$ is a continuously differentiable, non-negative quadratic form in $(b_0, b_1)$, we obtain its stationary points by setting the first-order partial derivatives with respect to $b_0$ and $b_1$ equal to zero:

$$\frac{\partial Q}{\partial b_0} = -2 \sum_{i=1}^n (y_i - b_0 - b_1 x_i) = 0$$

$$\frac{\partial Q}{\partial b_1} = -2 \sum_{i=1}^n x_i (y_i - b_0 - b_1 x_i) = 0$$

Dividing both equations by $-2$, rearranging terms, and replacing $(b_0, b_1)$ by the minimizers $(\hat{\beta}_0, \hat{\beta}_1)$ yields the celebrated **OLS Normal Equations**:

$$\begin{aligned}
n \hat{\beta}_0 + \left(\sum_{i=1}^n x_i\right) \hat{\beta}_1 &= \sum_{i=1}^n y_i \\
\left(\sum_{i=1}^n x_i\right) \hat{\beta}_0 + \left(\sum_{i=1}^n x_i^2\right) \hat{\beta}_1 &= \sum_{i=1}^n x_i y_i
\end{aligned}$$

Dividing the first normal equation by $n$ gives $\hat{\beta}_0 + \hat{\beta}_1 \bar{x} = \bar{y}$, where $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ and $\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ are the sample means. Consequently, the intercept estimator is explicitly linked to the slope estimator via:

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

Substituting $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$ into the second normal equation yields:

$$\sum_{i=1}^n x_i (\bar{y} - \hat{\beta}_1 \bar{x} + \hat{\beta}_1 x_i) = \sum_{i=1}^n x_i y_i \implies \bar{y} \sum_{i=1}^n x_i + \hat{\beta}_1 \sum_{i=1}^n x_i (x_i - \bar{x}) = \sum_{i=1}^n x_i y_i$$

To simplify these sums, we introduce the standard **corrected sums of squares and cross-products** notation:

$$S_{xx} = \sum_{i=1}^n (x_i - \bar{x})^2 = \sum_{i=1}^n x_i^2 - n \bar{x}^2 = \sum_{i=1}^n x_i(x_i - \bar{x})$$

$$S_{yy} = \sum_{i=1}^n (y_i - \bar{y})^2 = \sum_{i=1}^n y_i^2 - n \bar{y}^2, \qquad S_{xy} = \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) = \sum_{i=1}^n x_i y_i - n \bar{x}\bar{y} = \sum_{i=1}^n (x_i - \bar{x}) y_i$$

where the identities $\sum (x_i - \bar{x}) \bar{x} = \bar{x} \sum (x_i - \bar{x}) = 0$ and $\sum (x_i - \bar{x}) \bar{y} = \bar{y} \sum (x_i - \bar{x}) = 0$ follow because deviations from the sample mean sum identically to zero. Under Assumption A2 ($S_{xx} > 0$), solving for $\hat{\beta}_1$ produces the closed-form **OLS Slope Estimator**:

$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = r_{xy} \frac{s_y}{s_x}$$

where $r_{xy} = S_{xy} / \sqrt{S_{xx} S_{yy}}$ is the Pearson product-moment correlation coefficient and $s_x, s_y$ are the sample standard deviations. To confirm rigorously that $(\hat{\beta}_0, \hat{\beta}_1)$ corresponds to a strict global minimum rather than a saddle point, we inspect the $2 \times 2$ Hessian matrix of second partial derivatives of $Q(b_0, b_1)$:

$$\mathbf{H}_Q = \begin{pmatrix} \dfrac{\partial^2 Q}{\partial b_0^2} & \dfrac{\partial^2 Q}{\partial b_0 \partial b_1} \\[8pt] \dfrac{\partial^2 Q}{\partial b_1 \partial b_0} & \dfrac{\partial^2 Q}{\partial b_1^2} \end{pmatrix} = 2 \begin{pmatrix} n & \sum_{i=1}^n x_i \\[6pt] \sum_{i=1}^n x_i & \sum_{i=1}^n x_i^2 \end{pmatrix}$$

The leading principal minor is $2n > 0$, and the determinant of $\mathbf{H}_Q$ is:

$$\det(\mathbf{H}_Q) = 4 \left[ n \sum_{i=1}^n x_i^2 - \left(\sum_{i=1}^n x_i\right)^2 \right] = 4 n \left( \sum_{i=1}^n x_i^2 - n \bar{x}^2 \right) = 4 n S_{xx} > 0$$

By Sylvester's criterion, $\mathbf{H}_Q$ is strictly positive definite everywhere on $\mathbb{R}^2$, proving that $(\hat{\beta}_0, \hat{\beta}_1)$ is the unique global minimizer of $Q(b_0, b_1)$.

Once $(\hat{\beta}_0, \hat{\beta}_1)$ are computed, we define the **fitted values** $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ and the **OLS residuals** $e_i = y_i - \hat{y}_i$. Crucially, the normal equations impose six exact, distribution-free **algebraic orthogonality identities** on the residuals that hold for every dataset whenever an intercept is included:
1. **Zero Sum of Residuals**: $\sum_{i=1}^n e_i = 0$ (directly from the first normal equation).
2. **Equality of Observed and Fitted Means**: $\sum_{i=1}^n y_i = \sum_{i=1}^n \hat{y}_i \implies \bar{\hat{y}} = \bar{y}$.
3. **Centroid Passage Property**: Setting $x = \bar{x}$ in the fitted line gives $\hat{y}(\bar{x}) = \hat{\beta}_0 + \hat{\beta}_1 \bar{x} = (\bar{y} - \hat{\beta}_1 \bar{x}) + \hat{\beta}_1 \bar{x} = \bar{y}$, so the fitted regression line always passes exactly through the sample centroid $(\bar{x}, \bar{y})$.
4. **Orthogonality to the Predictor**: $\sum_{i=1}^n x_i e_i = 0$ (directly from the second normal equation), and consequently $\sum_{i=1}^n (x_i - \bar{x}) e_i = \sum x_i e_i - \bar{x} \sum e_i = 0$.
5. **Orthogonality to the Fitted Values**: $\sum_{i=1}^n \hat{y}_i e_i = \sum_{i=1}^n (\hat{\beta}_0 + \hat{\beta}_1 x_i) e_i = \hat{\beta}_0 \sum_{i=1}^n e_i + \hat{\beta}_1 \sum_{i=1}^n x_i e_i = 0$. In $n$-dimensional Euclidean space $\mathbb{R}^n$, the residual vector $\mathbf{e}$ is strictly orthogonal to the fitted response vector $\hat{\mathbf{y}}$.
6. **Non-Zero Sum of Squares in Intercept-Free Regression**: If a regression through the origin $Y_i = \beta_1 x_i + \varepsilon_i$ is fitted without an intercept $\beta_0$, the first normal equation is absent; only $\sum x_i e_i = 0$ holds, and $\sum_{i=1}^n e_i$ is generally non-zero.

### Numerical Stability of Centered Computations and Geometric Orthogonality in Hilbert Space
From the standpoint of statistical computing (Course Stat H-312), the textbook algebraic formula for the corrected sum of squares, which subtracts the product of the sample size and the squared sample mean from the raw sum of squares, is notoriously susceptible to catastrophic floating-point cancellation when the sample standard deviation is small relative to the magnitude of the sample mean. Modern statistical software packages therefore evaluate the centered deviations first—or employ Welford's one-pass updating recursion and Householder QR orthogonal triangularization—before accumulating squared deviations and cross-products. Geometrically, the six orthogonality properties derived from the normal equations reflect the decomposition of Euclidean space into a two-dimensional estimation subspace spanned by the constant vector and the regressor vector, together with an orthogonal residual subspace of dimension two less than the sample size. Because the constant vector of ones lies inside the estimation plane, projecting the response vector onto that plane guarantees that the residual vector is perpendicular to the vector of ones, which is the geometric reason why the ordinary least squares residuals sum identically to zero.

## 1.3 Sampling Distributions, Unbiasedness, Variances, Covariance, and Estimation of Error Variance

To evaluate the statistical precision of the Ordinary Least Squares estimators across repeated samples, we examine $\hat{\beta}_1$ and $\hat{\beta}_0$ as random variables generated by the stochastic vector $\mathbf{Y} = (Y_1, \dots, Y_n)^T$. A pivotal algebraic step is to express $\hat{\beta}_1$ and $\hat{\beta}_0$ as explicit **linear combinations** of the observations $Y_1, \dots, Y_n$. Define the deterministic regression weights $k_i$ by:

$$k_i = \frac{x_i - \bar{x}}{S_{xx}}, \quad i = 1, 2, \dots, n$$

Because $\sum_{i=1}^n (x_i - \bar{x}) = 0$, the numerator of $\hat{\beta}_1$ simplifies to $S_{xy} = \sum_{i=1}^n (x_i - \bar{x})(Y_i - \bar{Y}) = \sum_{i=1}^n (x_i - \bar{x}) Y_i - \bar{Y} \sum_{i=1}^n (x_i - \bar{x}) = \sum_{i=1}^n (x_i - \bar{x}) Y_i$. Thus:

$$\hat{\beta}_1 = \sum_{i=1}^n k_i Y_i$$

Before taking expectations and variances, we verify three fundamental algebraic identities satisfied by the weights $k_i$:

$$\sum_{i=1}^n k_i = \frac{\sum_{i=1}^n (x_i - \bar{x})}{S_{xx}} = 0, \qquad \sum_{i=1}^n k_i x_i = \frac{\sum_{i=1}^n (x_i - \bar{x}) x_i}{S_{xx}} = \frac{S_{xx}}{S_{xx}} = 1, \qquad \sum_{i=1}^n k_i^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{S_{xx}^2} = \frac{S_{xx}}{S_{xx}^2} = \frac{1}{S_{xx}}$$

Substituting the structural model $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ into $\hat{\beta}_1 = \sum_{i=1}^n k_i Y_i$ yields the representation of $\hat{\beta}_1$ in terms of the true parameters and random errors:

$$\hat{\beta}_1 = \sum_{i=1}^n k_i (\beta_0 + \beta_1 x_i + \varepsilon_i) = \beta_0 \sum_{i=1}^n k_i + \beta_1 \sum_{i=1}^n k_i x_i + \sum_{i=1}^n k_i \varepsilon_i = \beta_1 + \sum_{i=1}^n k_i \varepsilon_i$$

Similarly, the intercept estimator $\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{x}$ can be written as a linear combination of $Y_1, \dots, Y_n$ with weights $w_i = \frac{1}{n} - k_i \bar{x}$:

$$\hat{\beta}_0 = \sum_{i=1}^n \left(\frac{1}{n} - k_i \bar{x}\right) Y_i = (\beta_0 + \beta_1 \bar{x} + \bar{\varepsilon}) - \left(\beta_1 + \sum_{i=1}^n k_i \varepsilon_i\right) \bar{x} = \beta_0 + \sum_{i=1}^n \left(\frac{1}{n} - k_i \bar{x}\right) \varepsilon_i$$

Using Assumptions A3 ($\mathbb{E}[\varepsilon_i] = 0$), A4 ($\text{Var}(\varepsilon_i) = \sigma^2$), and A5 ($\text{Cov}(\varepsilon_i, \varepsilon_j) = 0$ for $i \neq j$), we immediately obtain the exact finite-sample expectations, variances, and covariance of the OLS estimators:

1. **Unbiasedness of Slope and Intercept**:
   $$\mathbb{E}[\hat{\beta}_1] = \beta_1 + \sum_{i=1}^n k_i \mathbb{E}[\varepsilon_i] = \beta_1, \qquad \mathbb{E}[\hat{\beta}_0] = \beta_0 + \sum_{i=1}^n \left(\frac{1}{n} - k_i \bar{x}\right) \mathbb{E}[\varepsilon_i] = \beta_0$$

2. **Sampling Variance of the Slope Estimator**:
   $$\text{Var}(\hat{\beta}_1) = \text{Var}\left(\sum_{i=1}^n k_i \varepsilon_i\right) = \sum_{i=1}^n k_i^2 \text{Var}(\varepsilon_i) = \sigma^2 \sum_{i=1}^n k_i^2 = \frac{\sigma^2}{S_{xx}}$$
   Notice the profound experimental design implication: $\text{Var}(\hat{\beta}_1)$ decreases when the error variance $\sigma^2$ is small and when the predictor values are widely dispersed around their mean (making $S_{xx}$ large).

3. **Sampling Variance of the Intercept Estimator**:
   $$\text{Var}(\hat{\beta}_0) = \sigma^2 \sum_{i=1}^n \left(\frac{1}{n} - k_i \bar{x}\right)^2 = \sigma^2 \left( \frac{n}{n^2} - \frac{2\bar{x}}{n}\sum_{i=1}^n k_i + \bar{x}^2 \sum_{i=1}^n k_i^2 \right) = \sigma^2 \left( \frac{1}{n} + \frac{\bar{x}^2}{S_{xx}} \right) = \frac{\sigma^2 \sum_{i=1}^n x_i^2}{n S_{xx}}$$
   When $\bar{x}$ lies far from the origin $x = 0$, extrapolating the fitted line back to the vertical axis amplifies slope uncertainty by $\bar{x}^2$, inflating $\text{Var}(\hat{\beta}_0)$.

4. **Covariance Between Intercept and Slope Estimators**:
   $$\text{Cov}(\hat{\beta}_0, \hat{\beta}_1) = \text{Cov}(\bar{Y} - \hat{\beta}_1 \bar{x}, \hat{\beta}_1) = \text{Cov}(\bar{Y}, \hat{\beta}_1) - \bar{x} \text{Var}(\hat{\beta}_1)$$
   Because $\text{Cov}(\bar{Y}, \hat{\beta}_1) = \text{Cov}(\frac{1}{n}\sum Y_i, \sum k_j Y_j) = \frac{\sigma^2}{n} \sum_{i=1}^n k_i = 0$, the sample mean $\bar{Y}$ and the OLS slope $\hat{\beta}_1$ are strictly **uncorrelated**! Consequently:
   $$\text{Cov}(\hat{\beta}_0, \hat{\beta}_1) = -\frac{\bar{x} \sigma^2}{S_{xx}}$$
   If $\bar{x} > 0$, a random sample fluctuation that overestimates the slope ($\hat{\beta}_1 > \beta_1$) must pivot the line around the centroid $(\bar{x}, \bar{Y})$, tilting the left end downward and causing the intercept to be underestimated ($\hat{\beta}_0 < \beta_0$). Centering the predictor at $\tilde{x}_i = x_i - \bar{x}$ makes $\text{Cov}(\hat{\beta}_0^*, \hat{\beta}_1) = 0$.

In virtually all empirical applications, the disturbance variance $\sigma^2$ is unknown and must be estimated from the **Error (or Residual) Sum of Squares**, $\text{SSE} = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n (Y_i - \hat{Y}_i)^2$. To find $\mathbb{E}[\text{SSE}]$, write each residual in centered form:

$$e_i = Y_i - (\bar{Y} + \hat{\beta}_1 (x_i - \bar{x})) = (Y_i - \bar{Y}) - \hat{\beta}_1 (x_i - \bar{x})$$

Squaring and summing over $i = 1, \dots, n$ yields the key computational identity:

$$\text{SSE} = \sum_{i=1}^n (Y_i - \bar{Y})^2 - 2 \hat{\beta}_1 \sum_{i=1}^n (x_i - \bar{x})(Y_i - \bar{Y}) + \hat{\beta}_1^2 \sum_{i=1}^n (x_i - \bar{x})^2 = S_{yy} - 2 \hat{\beta}_1 S_{xy} + \hat{\beta}_1^2 S_{xx} = S_{yy} - \hat{\beta}_1^2 S_{xx}$$

Alternatively, substituting $Y_i - \bar{Y} = \beta_1(x_i - \bar{x}) + (\varepsilon_i - \bar{\varepsilon})$ and $\hat{\beta}_1 - \beta_1 = \sum k_i \varepsilon_i$ into $e_i = (\varepsilon_i - \bar{\varepsilon}) - (\hat{\beta}_1 - \beta_1)(x_i - \bar{x})$ gives:

$$\text{SSE} = \sum_{i=1}^n (\varepsilon_i - \bar{\varepsilon})^2 - (\hat{\beta}_1 - \beta_1)^2 S_{xx}$$

Taking expectations, since $\mathbb{E}[\sum_{i=1}^n (\varepsilon_i - \bar{\varepsilon})^2] = (n - 1)\sigma^2$ and $\mathbb{E}[(\hat{\beta}_1 - \beta_1)^2] = \text{Var}(\hat{\beta}_1) = \sigma^2 / S_{xx}$:

$$\mathbb{E}[\text{SSE}] = (n - 1)\sigma^2 - \left(\frac{\sigma^2}{S_{xx}}\right) S_{xx} = (n - 1)\sigma^2 - \sigma^2 = (n - 2)\sigma^2$$

Therefore, dividing $\text{SSE}$ by $n - 2$ degrees of freedom (accounting for the two estimated parameters $\hat{\beta}_0$ and $\hat{\beta}_1$) defines the **unbiased estimator of error variance** (also called Mean Square Error, $\text{MSE}$):

$$s^2 = \text{MSE} = \frac{\text{SSE}}{n - 2} = \frac{1}{n - 2} \sum_{i=1}^n e_i^2, \qquad \mathbb{E}[s^2] = \sigma^2$$

### Experimental Design Principles for Maximizing Slope Precision
The analytical formulas for the sampling variances of the Ordinary Least Squares slope and intercept estimators provide immediate, actionable guidance for optimal experimental design before any physical measurements are collected. Because the variance of the slope estimator is inversely proportional to the corrected sum of squares of the predictor, an experimenter who is free to choose the operating levels of the explanatory variable within a bounded safe operating interval can minimize the variance of the estimated slope by placing half of the experimental runs at the lower boundary of the interval and the other half at the upper boundary. While such a two-point boundary design maximizes the spread of the predictor and thereby achieves the smallest possible standard error for the linear slope, it leaves no interior points to check whether the true conditional expectation function deviates from a straight line. Consequently, practical engineering and biometric calibration designs allocate the majority of runs toward the extremes of the predictor range to secure high precision for the slope while placing replicated center points near the sample mean to reduce intercept uncertainty and enable formal diagnostic testing for quadratic curvature.

## 1.4 Proof of the Gauss-Markov Theorem (BLUE Property) and Maximum Likelihood Equivalence

Why should a statistician prefer the Ordinary Least Squares estimators $(\hat{\beta}_0, \hat{\beta}_1)$ over alternative linear combinations of the data, such as connecting the first and last observations or grouping observations into upper and lower halves (Wald's method of averages)? The definitive theoretical answer under Assumptions A1–A5 is provided by the **Gauss–Markov Theorem**.

#### Theorem 1.1 (The Gauss–Markov Theorem for Simple Linear Regression)
Under the classical Gauss–Markov assumptions A1–A5 ($\mathbb{E}[\varepsilon_i] = 0$, $\text{Var}(\varepsilon_i) = \sigma^2$, $\text{Cov}(\varepsilon_i, \varepsilon_j) = 0$ for $i \neq j$, and $S_{xx} > 0$), the Ordinary Least Squares estimators $\hat{\beta}_1$ and $\hat{\beta}_0$ are the unique **Best Linear Unbiased Estimators (BLUE)** of $\beta_1$ and $\beta_0$, respectively. That is, among all estimators that are both linear functions of $Y_1, \dots, Y_n$ and unbiased for the target parameter, the OLS estimators possess the strictly smallest variance.

#### Complete Mathematical Proof for $\hat{\beta}_1$:
Let $\tilde{\beta}_1$ be any arbitrary linear estimator of the slope $\beta_1$:

$$\tilde{\beta}_1 = \sum_{i=1}^n c_i Y_i$$

where $c_1, c_2, \dots, c_n$ are deterministic constants depending only on the fixed predictor values $x_1, \dots, x_n$. Taking the mathematical expectation of $\tilde{\beta}_1$ under Assumption A1 and A3:

$$\mathbb{E}[\tilde{\beta}_1] = \sum_{i=1}^n c_i \mathbb{E}[Y_i] = \sum_{i=1}^n c_i (\beta_0 + \beta_1 x_i) = \beta_0 \left(\sum_{i=1}^n c_i\right) + \beta_1 \left(\sum_{i=1}^n c_i x_i\right)$$

For $\tilde{\beta}_1$ to be an unbiased estimator of $\beta_1$ identically for all $(\beta_0, \beta_1) \in \mathbb{R}^2$, the coefficients $c_i$ must satisfy the two linear unbiasedness constraints:

$$\sum_{i=1}^n c_i = 0 \qquad \text{and} \qquad \sum_{i=1}^n c_i x_i = 1$$

Now decompose each arbitrary weight $c_i$ by writing it as the sum of the OLS weight $k_i = (x_i - \bar{x})/S_{xx}$ and a discrepancy term $d_i$:

$$c_i = k_i + d_i \implies d_i = c_i - k_i, \quad i = 1, 2, \dots, n$$

Because both $c_i$ and $k_i$ satisfy the unbiasedness constraints, the discrepancy weights $d_i$ automatically satisfy two orthogonality conditions:

$$\sum_{i=1}^n d_i = \sum_{i=1}^n c_i - \sum_{i=1}^n k_i = 0 - 0 = 0, \qquad \sum_{i=1}^n d_i x_i = \sum_{i=1}^n c_i x_i - \sum_{i=1}^n k_i x_i = 1 - 1 = 0$$

Using these two identities, we evaluate the inner product between the OLS weights $k_i$ and the discrepancy weights $d_i$:

$$\sum_{i=1}^n k_i d_i = \sum_{i=1}^n \left(\frac{x_i - \bar{x}}{S_{xx}}\right) d_i = \frac{1}{S_{xx}} \left( \sum_{i=1}^n d_i x_i - \bar{x} \sum_{i=1}^n d_i \right) = \frac{1}{S_{xx}} (0 - \bar{x} \cdot 0) = 0$$

Now compute the sampling variance of the competing linear unbiased estimator $\tilde{\beta}_1$ under Assumptions A4 and A5:

$$\text{Var}(\tilde{\beta}_1) = \text{Var}\left(\sum_{i=1}^n c_i Y_i\right) = \sigma^2 \sum_{i=1}^n c_i^2 = \sigma^2 \sum_{i=1}^n (k_i + d_i)^2 = \sigma^2 \left( \sum_{i=1}^n k_i^2 + 2 \sum_{i=1}^n k_i d_i + \sum_{i=1}^n d_i^2 \right)$$

Since the cross-product sum $\sum_{i=1}^n k_i d_i = 0$ vanishes identically and $\sigma^2 \sum_{i=1}^n k_i^2 = \text{Var}(\hat{\beta}_1)$, this simplifies to:

$$\text{Var}(\tilde{\beta}_1) = \text{Var}(\hat{\beta}_1) + \sigma^2 \sum_{i=1}^n d_i^2$$

Because $\sigma^2 > 0$ and $\sum_{i=1}^n d_i^2 \ge 0$ is a sum of squares of real numbers, we have $\text{Var}(\tilde{\beta}_1) \ge \text{Var}(\hat{\beta}_1)$, with equality holding if and only if $d_i = 0$ for every $i = 1, \dots, n$, which means $c_i = k_i$ and $\tilde{\beta}_1 = \hat{\beta}_1$. An identical argument with $w_i = \frac{1}{n} - k_i \bar{x}$ and unbiasedness constraints $\sum c_i = 1, \sum c_i x_i = 0$ proves that $\hat{\beta}_0$ is the unique BLUE of $\beta_0$. More generally, for any scalar linear combination $\theta = a_0 \beta_0 + a_1 \beta_1$, the plug-in estimator $\hat{\theta} = a_0 \hat{\beta}_0 + a_1 \hat{\beta}_1$ is the unique BLUE of $\theta$.

### Equivalence with Maximum Likelihood Estimation (MLE) and UMVUE under Normal Errors
Note that the Gauss–Markov Theorem requires **no distributional assumption** beyond finite second moments; however, its optimality is restricted to the class of *linear* unbiased estimators. When we add Assumption A6—that $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$—then $Y_i \sim \mathcal{N}(\beta_0 + \beta_1 x_i, \sigma^2)$ independently, and the joint log-likelihood function for $\boldsymbol{\theta} = (\beta_0, \beta_1, \sigma^2)$ is:

$$\ell(\beta_0, \beta_1, \sigma^2) = -\frac{n}{2} \ln(2\pi) - \frac{n}{2} \ln(\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$$

For any fixed $\sigma^2 > 0$, maximizing $\ell(\beta_0, \beta_1, \sigma^2)$ with respect to $(\beta_0, \beta_1)$ is mathematically identical to minimizing the least-squares criterion $Q(\beta_0, \beta_1) = \sum (y_i - \beta_0 - \beta_1 x_i)^2$. Consequently:

$$\hat{\beta}_{0, \text{MLE}} = \hat{\beta}_{0, \text{OLS}}, \qquad \hat{\beta}_{1, \text{MLE}} = \hat{\beta}_{1, \text{OLS}}$$

Differentiating $\ell(\hat{\beta}_0, \hat{\beta}_1, \sigma^2)$ with respect to $\sigma^2$ yields $-\frac{n}{2\sigma^2} + \frac{\text{SSE}}{2(\sigma^2)^2} = 0$, giving the Maximum Likelihood Estimator of the error variance:

$$\hat{\sigma}_{\text{MLE}}^2 = \frac{\text{SSE}}{n} = \left(\frac{n - 2}{n}\right) s^2$$

Thus, $\hat{\sigma}_{\text{MLE}}^2$ is biased downward in finite samples ($\mathbb{E}[\hat{\sigma}_{\text{MLE}}^2] = \frac{n-2}{n}\sigma^2$), though it is asymptotically unbiased and consistent as $n \to \infty$. Furthermore, under normal errors, the joint density belongs to a regular 3-parameter full-rank exponential family with complete sufficient statistic $\mathbf{T} = (\sum Y_i, \sum x_i Y_i, \sum Y_i^2)$. By the **Lehmann–Scheffé Theorem**, because $\hat{\beta}_0$, $\hat{\beta}_1$, and $s^2 = \text{SSE}/(n-2)$ are unbiased estimators that are functions solely of the complete sufficient statistic $\mathbf{T}$, they are the unique **Uniformly Minimum Variance Unbiased Estimators (UMVUE)** among *all* unbiased estimators—both linear and nonlinear!

### Scope and Limitations of the Gauss-Markov Optimality Guarantee
Students of theoretical statistics must appreciate both the remarkable generality and the precise boundaries of the Gauss–Markov Theorem. On the one hand, the theorem is entirely non-parametric with respect to the shape of the error distribution: whether the disturbances follow a symmetric Gaussian bell curve, a skewed gamma distribution, or a discrete two-point distribution, the Ordinary Least Squares estimator achieves the minimum possible variance among all unbiased estimators that are linear combinations of the response observations. On the other hand, the restriction to linear and unbiased estimators is critical. When the error distribution possesses heavy tails—such as a Cauchy, Laplace, or contaminated normal distribution—nonlinear estimators such as the Least Absolute Deviations median regression estimator or Huber's M-estimator are no longer constrained by the Gauss–Markov bound and can achieve dramatically smaller asymptotic variance than Ordinary Least Squares. Similarly, in high-dimensional or collinear settings, biased linear estimators such as ridge regression deliberately sacrifice exact unbiasedness in order to achieve a smaller total Mean Squared Error than the Gauss–Markov Best Linear Unbiased Estimator.

## 1.5 ANOVA Decomposition, Coefficient of Determination, and Exact Hypothesis Tests

To assess how effectively the fitted regression line accounts for the observed variation in $Y$, we partition the deviation of each observation $y_i$ from the overall sample mean $\bar{y}$ into two additive components by adding and subtracting the fitted value $\hat{y}_i$:

$$y_i - \bar{y} = (\hat{y}_i - \bar{y}) + (y_i - \hat{y}_i) = (\hat{y}_i - \bar{y}) + e_i$$

Here, $(y_i - \bar{y})$ is the **total deviation**, $(\hat{y}_i - \bar{y})$ is the **explained (regression) deviation**, and $e_i = (y_i - \hat{y}_i)$ is the **unexplained (residual) deviation**. Squaring both sides and summing over all $n$ observations yields:

$$\sum_{i=1}^n (y_i - \bar{y})^2 = \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 + \sum_{i=1}^n e_i^2 + 2 \sum_{i=1}^n (\hat{y}_i - \bar{y}) e_i$$

Let us evaluate the cross-product term using the algebraic orthogonality identities of Section 1.2:

$$\sum_{i=1}^n (\hat{y}_i - \bar{y}) e_i = \sum_{i=1}^n \hat{y}_i e_i - \bar{y} \sum_{i=1}^n e_i = 0 - \bar{y}(0) = 0$$

Because the cross-product vanishes identically, we obtain the fundamental **Analysis of Variance (ANOVA) Sum-of-Squares Decomposition** (a Pythagorean identity in $\mathbb{R}^n$):

$$\text{SST} = \text{SSR} + \text{SSE}$$

where:
- **Total Sum of Squares ($\text{SST}$)**: $\text{SST} = S_{yy} = \sum_{i=1}^n (y_i - \bar{y})^2$, with $n - 1$ degrees of freedom.
- **Regression (Model) Sum of Squares ($\text{SSR}$)**: $\text{SSR} = \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 = \hat{\beta}_1^2 \sum_{i=1}^n (x_i - \bar{x})^2 = \hat{\beta}_1^2 S_{xx} = \hat{\beta}_1 S_{xy} = \frac{S_{xy}^2}{S_{xx}}$, with $1$ degree of freedom.
- **Error (Residual) Sum of Squares ($\text{SSE}$)**: $\text{SSE} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = S_{yy} - \hat{\beta}_1^2 S_{xx}$, with $n - 2$ degrees of freedom.

The proportion of total sample variation in $Y$ explained by the linear regression on $X$ is defined as the **Coefficient of Determination**, $R^2$:

$$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}} = \frac{S_{xy}^2}{S_{xx} S_{yy}} = r_{xy}^2 \in [0, 1]$$

In simple linear regression with an intercept, $R^2$ is identically the square of the sample Pearson correlation coefficient $r_{xy}$ between $x$ and $y$ (as well as the square of the correlation between observed $y_i$ and fitted $\hat{y}_i$). When $R^2 = 1$, all data points lie strictly on the fitted line ($\text{SSE} = 0$); when $R^2 = 0$, $\hat{\beta}_1 = 0$ and $\hat{y}_i = \bar{y}$ for all $i$.

Under the Gaussian assumption $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$, Cochran's Theorem establishes that:
1. $\hat{\beta}_1 \sim \mathcal{N}\!\left(\beta_1, \frac{\sigma^2}{S_{xx}}\right)$ and $\hat{\beta}_0 \sim \mathcal{N}\!\left(\beta_0, \sigma^2\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)\right)$.
2. $\frac{\text{SSE}}{\sigma^2} = \frac{(n-2)s^2}{\sigma^2} \sim \chi_{n-2}^2$, and $\text{SSE}$ is statistically **independent** of $(\hat{\beta}_0, \hat{\beta}_1)$.
3. Under the null hypothesis $H_0: \beta_1 = 0$, $\frac{\text{SSR}}{\sigma^2} = \frac{\hat{\beta}_1^2 S_{xx}}{\sigma^2} \sim \chi_1^2$ independently of $\text{SSE}$.

Consequently, to test $H_0: \beta_1 = \beta_{1,0}$ against $H_1: \beta_1 \neq \beta_{1,0}$, we use the exact Student $t$-statistic with $n - 2$ degrees of freedom:

$$t = \frac{\hat{\beta}_1 - \beta_{1,0}}{\text{SE}(\hat{\beta}_1)} = \frac{\hat{\beta}_1 - \beta_{1,0}}{s / \sqrt{S_{xx}}} \sim t_{n-2} \quad \text{under } H_0$$

For the overall regression test $H_0: \beta_1 = 0$ vs. $H_1: \beta_1 \neq 0$, the ANOVA $F$-statistic is the ratio of the Mean Square for Regression ($\text{MSR} = \text{SSR}/1$) to the Mean Square Error ($\text{MSE} = \text{SSE}/(n-2)$):

$$F = \frac{\text{MSR}}{\text{MSE}} = \frac{\text{SSR} / 1}{\text{SSE} / (n - 2)} = \frac{\hat{\beta}_1^2 S_{xx}}{s^2} = t^2 = \frac{R^2 / 1}{(1 - R^2) / (n - 2)} \sim F_{1, n-2} \quad \text{under } H_0: \beta_1 = 0$$

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Source of Variation</th><th>Degrees of Freedom (df)</th><th>Sum of Squares (SS)</th><th>Mean Square (MS)</th><th>Expected Mean Square $\mathbb{E}[\text{MS}]$</th><th>$F$-Statistic</th></tr>
</thead>
<tbody>
<tr><td><strong>Regression (Model)</strong></td><td>$1$</td><td>$\text{SSR} = \hat{\beta}_1^2 S_{xx}$</td><td>$\text{MSR} = \text{SSR} / 1$</td><td>$\sigma^2 + \beta_1^2 S_{xx}$</td><td>$F = \dfrac{\text{MSR}}{\text{MSE}} \sim F_{1, n-2}$</td></tr>
<tr><td><strong>Residual (Error)</strong></td><td>$n - 2$</td><td>$\text{SSE} = S_{yy} - \hat{\beta}_1^2 S_{xx}$</td><td>$\text{MSE} = s^2 = \dfrac{\text{SSE}}{n - 2}$</td><td>$\sigma^2$</td><td>—</td></tr>
<tr><td><strong>Total (Corrected)</strong></td><td>$n - 1$</td><td>$\text{SST} = S_{yy}$</td><td>—</td><td>—</td><td>—</td></tr>
</tbody>
</table></div>

Notice from the column of Expected Mean Squares that $\mathbb{E}[\text{MSR}] = \sigma^2 + \beta_1^2 S_{xx}$. When $H_0: \beta_1 = 0$ is true, both $\text{MSR}$ and $\text{MSE}$ estimate $\sigma^2$, so $F \approx 1$; when $\beta_1 \neq 0$, $\text{MSR}$ is systematically inflated by $\beta_1^2 S_{xx} > 0$, justifying an upper-tail rejection region $F > F_{\alpha, 1, n-2}$.

### Interpretation Pitfalls and Scale Properties of the Coefficient of Determination
Although the coefficient of determination is the most widely cited summary measure of goodness of fit in applied regression reporting, statistical methodology emphasizes several critical caveats regarding its scientific interpretation. First, a large coefficient of determination near unity does not establish that the linear functional form is correctly specified; a strongly curved exponential or parabolic trajectory often yields a coefficient of determination exceeding ninety percent when fitted by a straight line, even though residual plots immediately expose systematic specification error. Second, the coefficient of determination is highly sensitive to the design dispersion of the regressor: if an investigator restricts sampling to a narrow range of the explanatory variable, the regression sum of squares shrinks relative to the error sum of squares, causing the coefficient of determination to drop sharply even though the true structural slope and the error variance remain completely unchanged. For this reason, the residual standard error provides a stable, scale-invariant measure of predictive accuracy in the physical units of the response variable, whereas the coefficient of determination measures relative variance explanation within the specific sample range.

## 1.6 Mean Response Confidence Intervals, Prediction Intervals, and Working-Hotelling Simultaneous Bands

A core objective of regression modeling is inference at a specified covariate value $x_0$. Statisticians must carefully distinguish between two fundamentally different inferential targets at $x = x_0$:
1. **Estimating the Conditional Mean Response** $\mu_{Y \mid x_0} = \mathbb{E}[Y \mid X = x_0] = \beta_0 + \beta_1 x_0$ (a deterministic population parameter representing the average outcome across all units with $X = x_0$).
2. **Predicting an Individual Future Observation** $Y_{\text{new}} = \beta_0 + \beta_1 x_0 + \varepsilon_{\text{new}}$ (a random variable representing a single new realization at $X = x_0$, where $\varepsilon_{\text{new}} \sim \mathcal{N}(0, \sigma^2)$ is independent of the training sample).

For both targets, the natural point estimator/predictor is the fitted value on the OLS line:

$$\hat{Y}_0 = \hat{\mu}_{Y \mid x_0} = \hat{\beta}_0 + \hat{\beta}_1 x_0 = \bar{Y} + \hat{\beta}_1 (x_0 - \bar{x})$$

Because $\bar{Y}$ and $\hat{\beta}_1$ are uncorrelated ($\text{Cov}(\bar{Y}, \hat{\beta}_1) = 0$), the sampling variance of $\hat{Y}_0$ as an estimator of the conditional mean $\mu_{Y \mid x_0}$ is:

$$\text{Var}(\hat{Y}_0) = \text{Var}(\bar{Y}) + (x_0 - \bar{x})^2 \text{Var}(\hat{\beta}_1) = \frac{\sigma^2}{n} + \frac{(x_0 - \bar{x})^2 \sigma^2}{S_{xx}} = \sigma^2 \left[ \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}} \right]$$

Therefore, replacing $\sigma$ by $s = \sqrt{\text{MSE}}$ yields the exact $100(1 - \alpha)\%$ **Pointwise Confidence Interval for the Mean Response** $\mathbb{E}[Y \mid X = x_0]$:

$$\hat{y}_0 \pm t_{\alpha/2, \, n-2} \, s \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}$$

In contrast, when predicting a single new outcome $Y_{\text{new}} = \beta_0 + \beta_1 x_0 + \varepsilon_{\text{new}}$, the **prediction error** is the random variable $\psi = Y_{\text{new}} - \hat{Y}_0 = (\beta_0 + \beta_1 x_0 - \hat{Y}_0) + \varepsilon_{\text{new}}$. Its expectation is $\mathbb{E}[Y_{\text{new}} - \hat{Y}_0] = 0$, and because the future observation $Y_{\text{new}}$ is independent of the historical sample used to compute $\hat{Y}_0$, the variance of the prediction error is the sum of two variances:

$$\text{Var}(Y_{\text{new}} - \hat{Y}_0) = \text{Var}(Y_{\text{new}}) + \text{Var}(\hat{Y}_0) = \sigma^2 + \sigma^2 \left[ \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}} \right] = \sigma^2 \left[ 1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}} \right]$$

Notice the extra $+1$ inside the bracket: it accounts for the irreducible stochastic variance $\sigma^2$ of the individual disturbance $\varepsilon_{\text{new}}$ around the true regression line! Even if the sample size $n \to \infty$ so that the regression line is known with absolute certainty ($\frac{1}{n} \to 0$ and $\frac{(x_0-\bar{x})^2}{S_{xx}} \to 0$), the prediction interval retains a positive asymptotic half-width $z_{\alpha/2} \sigma$, whereas the confidence interval for the mean collapses to zero width. The exact $100(1 - \alpha)\%$ **Prediction Interval for a Single New Observation** $Y_{\text{new}}$ at $x_0$ is:

$$\hat{y}_0 \pm t_{\alpha/2, \, n-2} \, s \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}$$

If instead we predict the mean $\bar{Y}_{\text{new}, m}$ of $m$ independent future observations at $x_0$, the factor $1$ is replaced by $\frac{1}{m}$, yielding standard error $s\sqrt{\frac{1}{m} + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}$. Both the mean confidence interval and the prediction interval achieve their minimum width at the sample mean $x_0 = \bar{x}$ and flare outward along symmetric **hyperbolic boundaries** as $|x_0 - \bar{x}|$ increases, reflecting the growing danger of extrapolation away from the data center.

### Working–Hotelling Simultaneous Confidence Band for the Entire Regression Line
A pointwise $95\%$ confidence interval covers $\mu_{Y \mid x_0}$ at a *single* pre-selected value $x_0$ with probability $0.95$, but if an analyst demands a simultaneous confidence band that encloses the entire true regression line $\beta_0 + \beta_1 x$ across **all** real numbers $x \in (-\infty, \infty)$ simultaneously with familywise confidence $1 - \alpha$, the critical multiplier $t_{\alpha/2, n-2}$ must be widened. Working and Hotelling (1929) proved that because a straight line in $\mathbb{R}^2$ is completely determined by the two parameters $(\beta_0, \beta_1)$, the supremum over all $x \in \mathbb{R}$ of the squared standardized deviation equals a quadratic form distributed as $2 F_{2, n-2}$:

$$\mathbb{P}\left( \hat{\beta}_0 + \hat{\beta}_1 x - W s \sqrt{\frac{1}{n} + \frac{(x - \bar{x})^2}{S_{xx}}} \le \beta_0 + \beta_1 x \le \hat{\beta}_0 + \hat{\beta}_1 x + W s \sqrt{\frac{1}{n} + \frac{(x - \bar{x})^2}{S_{xx}}} \quad \forall x \in \mathbb{R} \right) = 1 - \alpha$$

where the **Working–Hotelling multiplier** is $W = \sqrt{2 F_{\alpha, \, 2, \, n-2}}$. Because $W = \sqrt{2 F_{\alpha, 2, n-2}} > \sqrt{F_{\alpha, 1, n-2}} = t_{\alpha/2, n-2}$, the simultaneous band is moderately wider than the pointwise confidence interval everywhere, guaranteeing simultaneous coverage across the entire domain of $x$.

### Practical Calibration of Pointwise Intervals Versus Simultaneous Confidence Bands
Choosing appropriately between a pointwise confidence interval for the conditional mean, a Working–Hotelling simultaneous confidence band, and an individual prediction interval is essential in applied decision-making. When a regulatory agency or manufacturing engineer evaluates the expected long-run average yield at a single, pre-specified target operating condition, the pointwise Student-$t$ confidence interval provides exact nominal coverage. When a calibration curve is published as a reference chart to be consulted repeatedly across many different predictor values by future laboratories, the Working–Hotelling hyperbolic band must be employed so that the entire calibration line is contained within the envelope at the stated familywise confidence level. Finally, when certifying whether an individual patient's clinical biomarker or a single future industrial batch will fall within safety specifications, neither confidence band is sufficient; the analyst must use the wider prediction interval, which incorporates both the estimation uncertainty of the regression line and the irreducible random variation of the individual future realization.

## Fully worked question 1: Complete Simple Linear Regression Analysis: OLS Estimation, ANOVA Table, Confidence Intervals & Prediction Intervals

### Question
A chemical process engineering laboratory at the University of Dhaka investigates the linear relationship between reactor operating temperature $x$ (in units of $10^\circ\text{C}$ above $100^\circ\text{C}$) and the percentage yield $Y$ of a purified catalytic polymer across $n = 10$ experimental runs. The summary statistics computed from the $n = 10$ runs are:

$$\sum_{i=1}^{10} x_i = 50, \quad \sum_{i=1}^{10} y_i = 650, \quad \sum_{i=1}^{10} x_i^2 = 330, \quad \sum_{i=1}^{10} y_i^2 = 42910, \quad \sum_{i=1}^{10} x_i y_i = 3450$$

1. Compute the corrected sums of squares and cross-products $S_{xx}, S_{yy}, S_{xy}$, and determine the Ordinary Least Squares estimates $\hat{\beta}_1$ and $\hat{\beta}_0$. Write down the fitted regression equation.
2. Partition the Total Sum of Squares into $\text{SSR}$ and $\text{SSE}$, calculate the unbiased error variance estimate $s^2 = \text{MSE}$, the coefficient of determination $R^2$, and construct the complete ANOVA table. Test $H_0: \beta_1 = 0$ at significance level $\alpha = 0.05$ using both the $t$-test and the ANOVA $F$-test (note: $t_{0.025, 8} = 2.306$, $F_{0.05, 1, 8} = 5.318$).
3. At a target operating temperature $x_0 = 8$, calculate the point prediction $\hat{y}_0$, the $95\%$ pointwise confidence interval for the mean yield $\mathbb{E}[Y \mid x_0 = 8]$, the $95\%$ Working–Hotelling simultaneous confidence band interval at $x_0 = 8$ (given $F_{0.05, 2, 8} = 4.459$), and the $95\%$ prediction interval for a single new reactor batch $Y_{\text{new}}$ at $x_0 = 8$.

### Solution, step 1: Compute sample means, corrected sums of squares, and OLS parameter estimates
With $n = 10$ observations, we first compute the sample means $\bar{x}$ and $\bar{y}$:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{10} x_i = \frac{50}{10} = 5.0, \qquad \bar{y} = \frac{1}{n} \sum_{i=1}^{10} y_i = \frac{650}{10} = 65.0$$

Next, we evaluate the corrected sums of squares and cross-products $S_{xx}, S_{yy},$ and $S_{xy}$:

$$S_{xx} = \sum_{i=1}^{10} x_i^2 - n \bar{x}^2 = 330 - 10(5.0)^2 = 330 - 250 = 80.0$$

$$S_{yy} = \sum_{i=1}^{10} y_i^2 - n \bar{y}^2 = 42910 - 10(65.0)^2 = 42910 - 42250 = 660.0$$

$$S_{xy} = \sum_{i=1}^{10} x_i y_i - n \bar{x} \bar{y} = 3450 - 10(5.0)(65.0) = 3450 - 3250 = 200.0$$

Applying the closed-form Ordinary Least Squares formulas from Section 1.2 gives the slope and intercept estimates:

$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{200.0}{80.0} = 2.50$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} = 65.0 - (2.50)(5.0) = 65.0 - 12.50 = 52.50$$

Therefore, the fitted linear regression equation is:

$$\hat{y} = 52.50 + 2.50 x$$

Each unit increase in $x$ ($10^\circ\text{C}$ increase in reactor temperature) increases the expected polymer yield by $2.50$ percentage points.

### Solution, step 2: ANOVA partitioning, error variance s^2, R^2, and hypothesis testing
We partition the Total Sum of Squares $\text{SST} = S_{yy} = 660.0$ into the Regression Sum of Squares ($\text{SSR}$) and Error Sum of Squares ($\text{SSE}$):

$$\text{SSR} = \hat{\beta}_1 S_{xy} = \hat{\beta}_1^2 S_{xx} = (2.50)(200.0) = 500.0$$

$$\text{SSE} = \text{SST} - \text{SSR} = 660.0 - 500.0 = 160.0$$

With $n - 2 = 10 - 2 = 8$ error degrees of freedom, the unbiased estimate of the disturbance variance $\sigma^2$ and residual standard error $s$ are:

$$s^2 = \text{MSE} = \frac{\text{SSE}}{n - 2} = \frac{160.0}{8} = 20.0, \qquad s = \sqrt{20.0} \approx 4.4721$$

The coefficient of determination $R^2$ and sample correlation $r_{xy}$ are:

$$R^2 = \frac{\text{SSR}}{\text{SST}} = \frac{500.0}{660.0} = \frac{25}{33} \approx 0.7576 \quad (75.76\%), \qquad r_{xy} = +\sqrt{0.7576} \approx +0.8704$$

Thus, $75.76\%$ of the total variation in polymer yield is explained by the linear regression on reactor temperature. The standard errors of $\hat{\beta}_1$ and $\hat{\beta}_0$ are:

$$\text{SE}(\hat{\beta}_1) = \frac{s}{\sqrt{S_{xx}}} = \sqrt{\frac{20.0}{80.0}} = \sqrt{0.25} = 0.50$$

$$\text{SE}(\hat{\beta}_0) = s \sqrt{\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}} = \sqrt{20.0 \left(\frac{1}{10} + \frac{25.0}{80.0}\right)} = \sqrt{2.0 + 6.25} = \sqrt{8.25} \approx 2.8723$$

To test $H_0: \beta_1 = 0$ vs. $H_1: \beta_1 \neq 0$ at $\alpha = 0.05$:
- **$t$-Test**: $t = \frac{\hat{\beta}_1 - 0}{\text{SE}(\hat{\beta}_1)} = \frac{2.50}{0.50} = 5.00$. Since $|t| = 5.00 > t_{0.025, 8} = 2.306$, we reject $H_0$.
- **ANOVA $F$-Test**: $F = \frac{\text{MSR}}{\text{MSE}} = \frac{500.0 / 1}{160.0 / 8} = \frac{500.0}{20.0} = 25.00 = t^2$. Since $F = 25.00 > F_{0.05, 1, 8} = 5.318$, both tests identically confirm a highly statistically significant linear relationship.

### Solution, step 3: Pointwise confidence interval, Working-Hotelling band, and prediction interval at x_0 = 8
At the target covariate level $x_0 = 8$, the fitted point prediction is:

$$\hat{y}_0 = 52.50 + 2.50(8) = 52.50 + 20.00 = 72.50$$

Notice that $x_0 - \bar{x} = 8.0 - 5.0 = 3.0$, so $(x_0 - \bar{x})^2 / S_{xx} = 9.0 / 80.0 = 0.1125$.
1. **Standard Error and $95\%$ Pointwise Confidence Interval for $\mathbb{E}[Y \mid x_0 = 8]$**:
   $$\text{SE}(\hat{\mu}_{Y \mid 8}) = s \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}} = \sqrt{20.0 (0.10 + 0.1125)} = \sqrt{20.0 (0.2125)} = \sqrt{4.25} \approx 2.0616$$
   $$\text{95\% Mean CI}: \quad 72.50 \pm (2.306)(2.0616) = 72.50 \pm 4.754 = [67.746, \, 77.254]$$

2. **$95\%$ Working–Hotelling Simultaneous Confidence Band at $x_0 = 8$**:
   The Working–Hotelling critical multiplier is $W = \sqrt{2 F_{0.05, 2, 8}} = \sqrt{2(4.459)} = \sqrt{8.918} \approx 2.9863$.
   $$\text{95\% Simultaneous Band}: \quad 72.50 \pm (2.9863)(2.0616) = 72.50 \pm 6.157 = [66.343, \, 78.657]$$

3. **$95\%$ Prediction Interval for a Single Future Batch $Y_{\text{new}}$ at $x_0 = 8$**:
   $$\text{SE}(Y_{\text{new}} - \hat{Y}_0) = s \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}} = \sqrt{20.0 (1 + 0.2125)} = \sqrt{24.25} \approx 4.9244$$
   $$\text{95\% Prediction Interval}: \quad 72.50 \pm (2.306)(4.9244) = 72.50 \pm 11.356 = [61.144, \, 83.856]$$

Comparing the three half-widths ($\pm 4.754$ for the pointwise mean CI, $\pm 6.157$ for the simultaneous Working–Hotelling band, and $\pm 11.356$ for the individual prediction interval) illustrates how individual batch variability $\sigma^2 = 20.0$ dominates single-observation prediction uncertainty.

## Fully worked question 2: Regression Through the Origin (Zero-Intercept Model): BLUE Derivation, Residual Properties, and Efficiency Comparison

### Question
In certain physical and biometric calibration settings (such as spectrophotometric absorbance obeying the Beer–Lambert law where zero concentration implies zero absorbance), theory dictates that the population regression line passes strictly through the origin ($\beta_0 = 0$), yielding the **Regression Through the Origin (RTO)** model:

$$Y_i = \beta_1 x_i + \varepsilon_i, \quad i = 1, 2, \dots, n$$

where $\mathbb{E}[\varepsilon_i] = 0$, $\text{Var}(\varepsilon_i) = \sigma^2$, $\text{Cov}(\varepsilon_i, \varepsilon_j) = 0$ ($i \neq j$), and $\sum_{i=1}^n x_i^2 > 0$.

1. Derive the Ordinary Least Squares estimator $\tilde{\beta}_1$ of $\beta_1$ under the zero-intercept model, prove that $\tilde{\beta}_1$ is unbiased for $\beta_1$ when $\beta_0 = 0$, and derive its exact variance $\text{Var}(\tilde{\beta}_1)$.
2. Prove via the Gauss–Markov method that $\tilde{\beta}_1$ is the unique Best Linear Unbiased Estimator (BLUE) of $\beta_1$ when $\beta_0 = 0$, and compare $\text{Var}(\tilde{\beta}_1)$ against the variance $\text{Var}(\hat{\beta}_1) = \sigma^2 / S_{xx}$ of the full intercept-included OLS slope estimator.
3. Show that for the RTO residuals $\tilde{e}_i = Y_i - \tilde{\beta}_1 x_i$, the weighted orthogonality $\sum_{i=1}^n x_i \tilde{e}_i = 0$ holds, but $\sum_{i=1}^n \tilde{e}_i \neq 0$ in general. Finally, derive the bias and Mean Squared Error of $\tilde{\beta}_1$ if the true data-generating process actually has a non-zero intercept $\beta_0 \neq 0$.

### Solution, step 1: OLS derivation, unbiasedness, and variance of the RTO estimator
To estimate $\beta_1$ in the zero-intercept model $Y_i = \beta_1 x_i + \varepsilon_i$, we minimize the single-parameter sum of squares objective function:

$$Q_0(b_1) = \sum_{i=1}^n (Y_i - b_1 x_i)^2$$

Differentiating with respect to $b_1$ and setting the derivative equal to zero gives the single normal equation:

$$\frac{d Q_0}{d b_1} = -2 \sum_{i=1}^n x_i (Y_i - \tilde{\beta}_1 x_i) = 0 \implies \left(\sum_{i=1}^n x_i^2\right) \tilde{\beta}_1 = \sum_{i=1}^n x_i Y_i$$

Since $\sum_{i=1}^n x_i^2 > 0$ (and $d^2 Q_0 / d b_1^2 = 2 \sum x_i^2 > 0$), the unique global minimizer is:

$$\tilde{\beta}_1 = \frac{\sum_{i=1}^n x_i Y_i}{\sum_{i=1}^n x_i^2}$$

Substituting $Y_i = \beta_1 x_i + \varepsilon_i$ into this expression yields:

$$\tilde{\beta}_1 = \frac{\sum_{i=1}^n x_i (\beta_1 x_i + \varepsilon_i)}{\sum_{i=1}^n x_i^2} = \beta_1 + \frac{\sum_{i=1}^n x_i \varepsilon_i}{\sum_{i=1}^n x_i^2}$$

Taking expectations and variances under $\mathbb{E}[\varepsilon_i] = 0$ and $\text{Cov}(\varepsilon_i, \varepsilon_j) = \sigma^2 \delta_{ij}$:

$$\mathbb{E}[\tilde{\beta}_1] = \beta_1 + \frac{\sum_{i=1}^n x_i \mathbb{E}[\varepsilon_i]}{\sum_{i=1}^n x_i^2} = \beta_1$$

$$\text{Var}(\tilde{\beta}_1) = \frac{\sum_{i=1}^n x_i^2 \text{Var}(\varepsilon_i)}{\left(\sum_{i=1}^n x_i^2\right)^2} = \frac{\sigma^2 \sum_{i=1}^n x_i^2}{\left(\sum_{i=1}^n x_i^2\right)^2} = \frac{\sigma^2}{\sum_{i=1}^n x_i^2}$$

### Solution, step 2: BLUE optimality proof and variance comparison against the full OLS estimator
Let $\beta_1^* = \sum_{i=1}^n a_i Y_i$ be any linear estimator of $\beta_1$. Under the true model $Y_i = \beta_1 x_i + \varepsilon_i$, its expectation is $\mathbb{E}[\beta_1^*] = \beta_1 \sum_{i=1}^n a_i x_i$, so unbiasedness requires the single constraint $\sum_{i=1}^n a_i x_i = 1$. Let $a_i^* = x_i / \sum_{j=1}^n x_j^2$ be the RTO weights and define $d_i = a_i - a_i^*$. Then $\sum_{i=1}^n d_i x_i = 1 - 1 = 0$, which implies $\sum_{i=1}^n a_i^* d_i = (\sum d_i x_i)/(\sum x_j^2) = 0$. Consequently:

$$\text{Var}(\beta_1^*) = \sigma^2 \sum_{i=1}^n (a_i^* + d_i)^2 = \sigma^2 \sum_{i=1}^n (a_i^*)^2 + \sigma^2 \sum_{i=1}^n d_i^2 = \text{Var}(\tilde{\beta}_1) + \sigma^2 \sum_{i=1}^n d_i^2 \ge \text{Var}(\tilde{\beta}_1)$$

proving that $\tilde{\beta}_1$ is the unique BLUE when $\beta_0 = 0$. Comparing $\text{Var}(\tilde{\beta}_1)$ to the variance $\text{Var}(\hat{\beta}_1) = \sigma^2 / S_{xx}$ of the intercept-included estimator, since $\sum_{i=1}^n x_i^2 = S_{xx} + n \bar{x}^2 \ge S_{xx}$:

$$\text{Var}(\tilde{\beta}_1) = \frac{\sigma^2}{S_{xx} + n \bar{x}^2} \le \frac{\sigma^2}{S_{xx}} = \text{Var}(\hat{\beta}_1)$$

The relative efficiency ratio is $\frac{\text{Var}(\tilde{\beta}_1)}{\text{Var}(\hat{\beta}_1)} = \frac{S_{xx}}{S_{xx} + n \bar{x}^2} < 1$ whenever $\bar{x} \neq 0$, because knowing $\beta_0 = 0$ anchors the line at $(0,0)$ rather than estimating a second parameter.

### Solution, step 3: Residual properties and MSE under intercept misspecification
For the RTO residuals $\tilde{e}_i = Y_i - \tilde{\beta}_1 x_i$, the normal equation directly implies:

$$\sum_{i=1}^n x_i \tilde{e}_i = \sum_{i=1}^n x_i Y_i - \tilde{\beta}_1 \sum_{i=1}^n x_i^2 = 0$$

so $\tilde{\mathbf{e}}$ is orthogonal to $\mathbf{x}$ and $\tilde{\hat{\mathbf{y}}} = \tilde{\beta}_1 \mathbf{x}$, and $\mathbb{E}[\sum \tilde{e}_i^2] = (n - 1)\sigma^2$. However, summing the raw residuals gives:

$$\sum_{i=1}^n \tilde{e}_i = \sum_{i=1}^n (Y_i - \tilde{\beta}_1 x_i) = n(\bar{Y} - \tilde{\beta}_1 \bar{x})$$

which is non-zero unless $(\bar{x}, \bar{Y})$ happens to lie on the line through the origin. Because $\sum \tilde{e}_i \neq 0$, the uncentered decomposition $\sum (Y_i - \bar{Y})^2$ does not partition cleanly into $\sum (\tilde{\hat{Y}}_i - \bar{Y})^2 + \sum \tilde{e}_i^2$ (instead, $\sum Y_i^2 = \sum \tilde{\hat{Y}}_i^2 + \sum \tilde{e}_i^2$).

Finally, suppose the true data-generating process actually has a non-zero intercept $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ with $\beta_0 \neq 0$. Then:

$$\mathbb{E}[\tilde{\beta}_1] = \frac{\sum_{i=1}^n x_i (\beta_0 + \beta_1 x_i)}{\sum_{i=1}^n x_i^2} = \beta_1 + \beta_0 \frac{n \bar{x}}{\sum_{i=1}^n x_i^2} \implies \text{Bias}(\tilde{\beta}_1) = \frac{n \bar{x} \beta_0}{S_{xx} + n \bar{x}^2}$$

The Mean Squared Error of the misspecified zero-intercept estimator is therefore:

$$\text{MSE}(\tilde{\beta}_1) = \text{Var}(\tilde{\beta}_1) + \left[\text{Bias}(\tilde{\beta}_1)\right]^2 = \frac{\sigma^2}{S_{xx} + n \bar{x}^2} + \frac{n^2 \bar{x}^2 \beta_0^2}{(S_{xx} + n \bar{x}^2)^2}$$

Whenever $|\beta_0|$ is large relative to $\sigma$, the squared specification bias $\text{Bias}(\tilde{\beta}_1)^2$ overwhelms the variance reduction, explaining why statisticians retain the intercept $\beta_0$ unless physical theory guarantees $\beta_0 = 0$ with certainty.

## Fully worked question 3: Orthogonality of Sample Mean and OLS Slope, Joint Distribution of Estimators, and Inverse Calibration (Fieller's Theorem)

### Question
Consider the normal simple linear regression model $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ ($i = 1, \dots, n$) where $\varepsilon_i \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$ and $S_{xx} > 0$.

1. Prove analytically that the sample mean $\bar{Y}$ and the OLS slope estimator $\hat{\beta}_1$ are statistically independent random variables, and derive the exact $2 \times 2$ variance-covariance matrix $\text{Cov}\!\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{pmatrix}$ by writing $\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{pmatrix}$ as a linear transformation of $\begin{pmatrix} \bar{Y} \\ \hat{\beta}_1 \end{pmatrix}$.
2. Derive the correlation coefficient $\rho(\hat{\beta}_0, \hat{\beta}_1)$ between the OLS intercept and slope estimators as an explicit function of $\bar{x}$, $n$, and $S_{xx}$.
3. **Inverse Regression (Calibration Problem)**: Suppose an analytical chemist observes a known benchmark response $y^*$ (or wishes to find the horizontal intercept $x^* = -\beta_0 / \beta_1$ where $\mathbb{E}[Y \mid x^*] = 0$). Using the pivotal quantity $W(x^*) = \hat{\beta}_0 + \hat{\beta}_1 x^* - y^*$, derive **Fieller's exact $100(1-\alpha)\%$ confidence set** for the unknown true covariate $x^* = (y^* - \beta_0)/\beta_1$.

### Solution, step 1: Prove independence of Y-bar and beta_1_hat and derive the 2x2 covariance matrix
Write $\bar{Y} = \sum_{i=1}^n a_i Y_i$ with $a_i = \frac{1}{n}$ and $\hat{\beta}_1 = \sum_{i=1}^n k_i Y_i$ with $k_i = \frac{x_i - \bar{x}}{S_{xx}}$. Because $Y_1, \dots, Y_n$ are independent normal random variables, any pair of linear combinations $(\bar{Y}, \hat{\beta}_1)$ follows a bivariate normal distribution. Their covariance is:

$$\text{Cov}(\bar{Y}, \hat{\beta}_1) = \text{Cov}\left(\sum_{i=1}^n \frac{1}{n} Y_i, \, \sum_{j=1}^n k_j Y_j\right) = \frac{\sigma^2}{n} \sum_{i=1}^n k_i = \frac{\sigma^2}{n S_{xx}} \sum_{i=1}^n (x_i - \bar{x}) = 0$$

Because jointly normal random variables with zero covariance are statistically independent, $\bar{Y}$ and $\hat{\beta}_1$ are independent:

$$\begin{pmatrix} \bar{Y} \\ \hat{\beta}_1 \end{pmatrix} \sim \mathcal{N}_2 \left( \begin{pmatrix} \beta_0 + \beta_1 \bar{x} \\ \beta_1 \end{pmatrix}, \, \sigma^2 \begin{pmatrix} 1/n & 0 \\ 0 & 1/S_{xx} \end{pmatrix} \right)$$

Now express $\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{pmatrix}$ as a linear transformation of $\begin{pmatrix} \bar{Y} \\ \hat{\beta}_1 \end{pmatrix}$:

$$\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{pmatrix} = \begin{pmatrix} \bar{Y} - \bar{x} \hat{\beta}_1 \\ \hat{\beta}_1 \end{pmatrix} = \underbrace{\begin{pmatrix} 1 & -\bar{x} \\ 0 & 1 \end{pmatrix}}_{\mathbf{A}} \begin{pmatrix} \bar{Y} \\ \hat{\beta}_1 \end{pmatrix}$$

By standard multivariate normal covariance propagation, $\text{Cov}\!\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{pmatrix} = \mathbf{A} \text{Cov}\!\begin{pmatrix} \bar{Y} \\ \hat{\beta}_1 \end{pmatrix} \mathbf{A}^T$:

$$\text{Cov}\begin{pmatrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{pmatrix} = \sigma^2 \begin{pmatrix} 1 & -\bar{x} \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1/n & 0 \\ 0 & 1/S_{xx} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -\bar{x} & 1 \end{pmatrix} = \sigma^2 \begin{pmatrix} \dfrac{1}{n} + \dfrac{\bar{x}^2}{S_{xx}} & -\dfrac{\bar{x}}{S_{xx}} \\[10pt] -\dfrac{\bar{x}}{S_{xx}} & \dfrac{1}{S_{xx}} \end{pmatrix}$$

### Solution, step 2: Derive the correlation coefficient between intercept and slope estimators
From the $2 \times 2$ covariance matrix derived in Step 1, we divide the off-diagonal covariance $\text{Cov}(\hat{\beta}_0, \hat{\beta}_1)$ by the square root of the product of the diagonal variances:

$$\rho(\hat{\beta}_0, \hat{\beta}_1) = \frac{\text{Cov}(\hat{\beta}_0, \hat{\beta}_1)}{\sqrt{\text{Var}(\hat{\beta}_0) \text{Var}(\hat{\beta}_1)}} = \frac{-\sigma^2 \bar{x} / S_{xx}}{\sqrt{\sigma^2 \left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right) \left(\frac{\sigma^2}{S_{xx}}\right)}} = \frac{-\bar{x}}{\sqrt{\frac{S_{xx}}{n} + \bar{x}^2}} = \frac{-\bar{x}}{\sqrt{\frac{1}{n} \sum_{i=1}^n x_i^2}}$$

Notice that $\rho(\hat{\beta}_0, \hat{\beta}_1)$ always has the opposite sign of $\bar{x}$, approaches $-1$ as $\bar{x} / s_x \to +\infty$, and equals zero if and only if the predictor is centered so that $\bar{x} = 0$.

### Solution, step 3: Derive Fieller's exact confidence set for inverse calibration x*
Let $y^* = \beta_0 + \beta_1 x^*$ be the target expected response at the unknown true covariate value $x^* = (y^* - \beta_0)/\beta_1$. While the natural point estimator is $\hat{x}^* = (y^* - \hat{\beta}_0)/\hat{\beta}_1 = \bar{x} + (y^* - \bar{Y})/\hat{\beta}_1$, this is a ratio of two normal random variables whose exact distribution is heavy-tailed (Cauchy-like). Instead of relying on an approximate delta-method expansion, **Fieller's method** constructs an exact linear normal pivot:

$$W(x^*) = \hat{\beta}_0 + \hat{\beta}_1 x^* - y^* = (\bar{Y} - y^*) + \hat{\beta}_1 (x^* - \bar{x})$$

Because $y^* = \beta_0 + \beta_1 x^*$, we have $\mathbb{E}[W(x^*)] = \beta_0 + \beta_1 x^* - y^* = 0$, and by the independence of $\bar{Y}$ and $\hat{\beta}_1$:

$$\text{Var}(W(x^*)) = \sigma^2 \left[ \frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}} \right]$$

Since $W(x^*)$ is normal and independent of $s^2 = \text{MSE}$, the standardized ratio follows an exact Student $t_{n-2}$ distribution:

$$T(x^*) = \frac{(\bar{Y} - y^*) + \hat{\beta}_1 (x^* - \bar{x})}{s \sqrt{\frac{1}{n} + \frac{(x^* - \bar{x})^2}{S_{xx}}}} \sim t_{n-2}$$

Setting $T(x^*)^2 \le t_{\alpha/2, n-2}^2$ and letting $u = x^* - \bar{x}$ and $d = y^* - \bar{Y}$ yields the quadratic inequality in $u$:

$$(\hat{\beta}_1 u - d)^2 \le t_{\alpha/2, n-2}^2 s^2 \left( \frac{1}{n} + \frac{u^2}{S_{xx}} \right)$$

Define the slope significance ratio $g = \frac{t_{\alpha/2, n-2}^2 s^2}{\hat{\beta}_1^2 S_{xx}} = \frac{t_{\alpha/2, n-2}^2}{t_{\text{slope}}^2}$. Notice that $g < 1$ if and only if $H_0: \beta_1 = 0$ is rejected at level $\alpha$. Rearranging the inequality into standard quadratic form in $u = x^* - \bar{x}$:

$$\hat{\beta}_1^2 (1 - g) u^2 - 2 \hat{\beta}_1 d u + \left( d^2 - \frac{t_{\alpha/2, n-2}^2 s^2}{n} \right) \le 0$$

When $g < 1$ (so the slope is significantly non-zero), solving this quadratic equation gives **Fieller's exact $100(1-\alpha)\%$ confidence interval** for $x^*$:

$$x^* \in \bar{x} + \frac{1}{1 - g} \left[ \frac{y^* - \bar{Y}}{\hat{\beta}_1} \pm \frac{t_{\alpha/2, n-2} \, s}{\hat{\beta}_1} \sqrt{ \frac{1 - g}{n} + \frac{(y^* - \bar{Y})^2}{\hat{\beta}_1^2 S_{xx}} } \right]$$

When $g \to 0$ (high slope precision), Fieller's interval reduces smoothly to the delta-method approximation; when $g \ge 1$ ($\beta_1$ is not statistically distinguishable from zero), the confidence set becomes the complement of a finite interval or the entire real line $(-\infty, \infty)$, reflecting the physical fact that a horizontal line cannot be inverted uniquely.
