# Unit 6: Ratio, Regression and Calibration Estimation

## The Role of Auxiliary Information in Estimation

In survey sampling theory, auxiliary information consists of data regarding one or more supplementary characteristics $\mathbf{x} = (x_1, x_2, \dots, x_p)^\top$ available for the elements of the population. In Units 3, 4, and 5, we investigated how auxiliary information is deployed at the **design stage** prior to data collection—using auxiliary variables to partition the universe into homogeneous strata, to delineate compact clusters, or to assign unequal selection probabilities proportional to size (PPS).

However, in many practical survey investigations, auxiliary information cannot be utilized during sample selection:
1. **Absence of Unit-Level Frame Records**: Detailed auxiliary values $x_i$ for every single individual unit in the frame may not be recorded or accessible when the sample is drawn. For example, a national statistical office may know the exact aggregate population counts of males and females across five-year age brackets from a recent national census, but the operational sampling frame of telephone numbers or residential addresses does not record the age or sex of the occupants.
2. **Multi-Dimensional Auxiliary Vectors**: When multiple auxiliary characteristics are available simultaneously (such as age, sex, educational attainment, and regional geography), constructing a multidimensional stratified or PPS design that accommodates all variables simultaneously leads to extreme stratum fragmentation, empty sampling cells, and operational paralysis.
3. **Multi-Purpose Surveys**: Large-scale national surveys gather data on hundreds of distinct substantive variables (e.g., employment, health expenditures, nutrition, energy consumption). An optimal design for one survey variable may be disastrously inefficient for another.

To overcome these structural constraints, modern survey theory leverages auxiliary information at the **estimation stage**, after the sample has been gathered. By benchmarking sample totals against known, reliable population totals derived from censuses or pristine administrative registers, the statistician can adjust the estimation formula or calibrate the survey weights. This post-survey adjustment achieves two goals:
- **Substantial Variance Reduction**: Correlated auxiliary variables absorb large fractions of sampling variability, producing estimators whose standard errors are significantly smaller than the unadjusted Horvitz–Thompson estimator.
- **Consistent Benchmarking**: Calibration guarantees that when the survey weights are applied to the auxiliary variables, the resulting survey estimates reproduce the external demographic benchmarks exactly, eliminating discrepancies between national statistical publications.

---

## The Ratio Estimator: Foundations, Linearization and Mean Squared Error

The ratio estimator is one of the oldest, most elegant, and most widely applied techniques in survey practice. It is particularly effective when the survey variable $y$ is approximately proportional to a single positive auxiliary variable $x$, such that the relationship between $y$ and $x$ passes approximately through the origin.

### Formulation of the Estimator

Let $U = \{1, 2, \dots, N\}$ denote a finite population of $N$ units. Associated with each unit $i$ is the target variable $y_i$ and a strictly positive auxiliary variable $x_i > 0$. Suppose the population total of the auxiliary variable is known with certainty from an independent source:
$$X = \sum_{i=1}^N x_i \quad \text{and} \quad \bar{X} = \frac{X}{N}$$

A simple random sample without replacement (SRSWOR) of size $n$ is selected. Let $\bar{y} = \frac{1}{n} \sum_{i \in s} y_i$ and $\bar{x} = \frac{1}{n} \sum_{i \in s} x_i$ denote the unweighted sample means.

The finite-population ratio of the two characteristics is:
$$R = \frac{Y}{X} = \frac{\bar{Y}}{\bar{X}}$$

The sample estimate of the population ratio is:
$$\hat{R} = \frac{\bar{y}}{\bar{x}} = \frac{\sum_{i \in s} y_i}{\sum_{i \in s} x_i}$$

The **Ratio Estimator of the Population Mean $\bar{Y}$** is defined as:
$$\hat{\bar{Y}}_R = \hat{R} \bar{X} = \frac{\bar{y}}{\bar{x}} \bar{X}$$

Similarly, the **Ratio Estimator of the Population Total $Y$** is:
$$\hat{Y}_R = \hat{R} X = \frac{\bar{y}}{\bar{x}} X$$

### Superpopulation Model Interpretation

Under the model-based superpopulation perspective (Brewer, 1963; Royall, 1970), the ratio estimator arises naturally as the best linear unbiased predictor under the following regression model:
$$y_i = \beta x_i + \varepsilon_i$$
where:
$$E_\xi(\varepsilon_i \mid x_i) = 0, \quad V_\xi(\varepsilon_i \mid x_i) = \sigma^2 x_i, \quad \text{Cov}_\xi(\varepsilon_i, \varepsilon_j \mid x_i, x_j) = 0 \quad (i \ne j)$$
Under this model, the conditional expectation of $y$ is a straight line through the origin, and the residual variance is proportional to $x_i$ (heteroscedasticity). The weighted least-squares estimator of $\beta$ under this model is precisely $\hat{\beta} = \frac{\sum y_i}{\sum x_i} = \hat{R}$.

### Finite-Sample Bias of the Ratio Estimator

Because the ratio estimator is a non-linear function of two random variables ($\bar{y}$ and $\bar{x}$), it is technically biased in finite samples. To quantify this bias, we deploy a Taylor series expansion.

Define the relative sample deviations:
$$e_0 = \frac{\bar{y} - \bar{Y}}{\bar{Y}} \implies \bar{y} = \bar{Y}(1 + e_0)$$
$$e_1 = \frac{\bar{x} - \bar{X}}{\bar{X}} \implies \bar{x} = \bar{X}(1 + e_1)$$

Under SRSWOR, the expectations of these relative deviations are zero:
$$E(e_0) = 0, \quad E(e_1) = 0$$

Their variances and covariance under the randomization distribution are:
$$E(e_0^2) = \frac{V(\bar{y})}{\bar{Y}^2} = \frac{1 - f}{n} \frac{S_y^2}{\bar{Y}^2} = \frac{1 - f}{n} C_y^2$$
$$E(e_1^2) = \frac{V(\bar{x})}{\bar{X}^2} = \frac{1 - f}{n} \frac{S_x^2}{\bar{X}^2} = \frac{1 - f}{n} C_x^2$$
$$E(e_0 e_1) = \frac{\text{Cov}(\bar{y}, \bar{x})}{\bar{Y} \bar{X}} = \frac{1 - f}{n} \frac{S_{xy}}{\bar{Y} \bar{X}} = \frac{1 - f}{n} \rho C_y C_x$$
where $C_y = S_y / \bar{Y}$ and $C_x = S_x / \bar{X}$ are the population coefficients of variation, $\rho = \frac{S_{xy}}{S_y S_x}$ is the finite-population Pearson correlation coefficient, and $S_{xy} = \frac{1}{N - 1} \sum_{i=1}^N (y_i - \bar{Y})(x_i - \bar{X})$ is the population covariance.

Now express the sample ratio $\hat{R}$ in terms of $e_0$ and $e_1$:
$$\hat{R} = \frac{\bar{Y}(1 + e_0)}{\bar{X}(1 + e_1)} = R (1 + e_0)(1 + e_1)^{-1}$$

Assuming $|e_1| < 1$, we expand $(1 + e_1)^{-1}$ using a second-order Taylor series:
$$(1 + e_1)^{-1} = 1 - e_1 + e_1^2 - e_1^3 + \dots$$
Multiplying through:
$$\hat{R} = R (1 + e_0)(1 - e_1 + e_1^2 - \dots) \approx R (1 + e_0 - e_1 - e_0 e_1 + e_1^2)$$

Taking expectations:
$$E(\hat{R}) \approx R \left[ 1 + E(e_0) - E(e_1) - E(e_0 e_1) + E(e_1^2) \right] = R \left[ 1 - E(e_0 e_1) + E(e_1^2) \right]$$

Substituting the expectations:
$$E(\hat{R}) - R \approx R \left[ \frac{1 - f}{n} C_x^2 - \frac{1 - f}{n} \rho C_y C_x \right] = R \frac{1 - f}{n} C_x (C_x - \rho C_y)$$

Therefore, the approximate finite-sample bias of the ratio estimator of the mean $\hat{\bar{Y}}_R = \hat{R} \bar{X}$ is:
$$\text{Bias}(\hat{\bar{Y}}_R) \approx \bar{Y} \frac{1 - f}{n} C_x (C_x - \rho C_y)$$

#### Properties of the Bias:
1. **Order of Magnitude $O(1/n)$**: The bias is proportional to $1/n$. As sample size increases, the bias decays to zero much faster than the standard error (which decays at rate $O(1/\sqrt{n})$).
2. **Zero Bias Condition**: The bias is identically zero if $\rho = C_x / C_y$.
3. **Practical Negligibility**: In empirical practice with sample sizes $n \ge 30$ and coefficients of variation $C_x \le 0.10$, the ratio of the bias to the standard error ($\text{Bias} / \text{SE}$) is typically well below $0.10$. Cochran (1977) established that whenever $\text{Bias} / \text{SE} < 0.10$, the bias exerts a negligible effect on nominal confidence interval coverage rates.

### Mean Squared Error and Asymptotic Variance

To derive the Mean Squared Error ($\text{MSE}$) of the ratio estimator, we use the first-order linear approximation:
$$\hat{\bar{Y}}_R - \bar{Y} = \hat{R}\bar{X} - R\bar{X} \approx \bar{X} R (e_0 - e_1) = \bar{Y} (e_0 - e_1)$$

Squaring both sides:
$$(\hat{\bar{Y}}_R - \bar{Y})^2 \approx \bar{Y}^2 (e_0^2 + e_1^2 - 2 e_0 e_1)$$

Taking the design expectation:
$$\text{MSE}(\hat{\bar{Y}}_R) = E[(\hat{\bar{Y}}_R - \bar{Y})^2] \approx \bar{Y}^2 \left[ E(e_0^2) + E(e_1^2) - 2 E(e_0 e_1) \right]$$

Substitute the variance and covariance expressions:
$$\text{MSE}(\hat{\bar{Y}}_R) \approx \bar{Y}^2 \frac{1 - f}{n} \left[ C_y^2 + C_x^2 - 2 \rho C_y C_x \right]$$

Translating coefficients of variation back to population variances:
$$\bar{Y}^2 C_y^2 = S_y^2, \quad \bar{Y}^2 C_x^2 = \bar{Y}^2 \frac{S_x^2}{\bar{X}^2} = R^2 S_x^2, \quad \bar{Y}^2 \rho C_y C_x = R S_{xy}$$

This yields the fundamental **Mean Squared Error Formula for the Ratio Estimator**:
$$\text{MSE}(\hat{\bar{Y}}_R) \approx \frac{1 - f}{n} \left[ S_y^2 + R^2 S_x^2 - 2 R S_{xy} \right] = \frac{1 - f}{n} \left[ S_y^2 + R^2 S_x^2 - 2 R \rho S_y S_x \right]$$

We can write this compactly in terms of the population residuals $E_i = y_i - R x_i$:
$$\frac{1}{N - 1} \sum_{i=1}^N (y_i - R x_i)^2 = \frac{1}{N - 1} \sum_{i=1}^N \left[ (y_i - \bar{Y}) - R(x_i - \bar{X}) \right]^2 = S_y^2 + R^2 S_x^2 - 2 R S_{xy}$$
Therefore:
$$\text{MSE}(\hat{\bar{Y}}_R) \approx \frac{1 - f}{n} S_d^2$$
where $S_d^2 = \frac{1}{N - 1} \sum_{i=1}^N (y_i - R x_i)^2$ is the finite-population variance of the residuals from the line $y = Rx$.

### Sample Variance Estimator

From sample data, the residual variance $S_d^2$ is estimated using the sample residuals $e_i = y_i - \hat{R} x_i$:
$$s_d^2 = \frac{1}{n - 1} \sum_{i \in s} (y_i - \hat{R} x_i)^2 = s_y^2 + \hat{R}^2 s_x^2 - 2 \hat{R} s_{xy}$$

The standard approximately unbiased estimator of the variance of the ratio estimator is:
$$\hat{V}(\hat{\bar{Y}}_R) = \frac{1 - f}{n} s_d^2 = \frac{1 - f}{n(n - 1)} \sum_{i \in s} (y_i - \hat{R} x_i)^2$$

### The Fundamental Efficiency Condition: When Does Ratio Estimation Beat Simple Random Sampling?

A practitioner must determine whether applying the ratio estimator improves precision over the unadjusted sample mean $\bar{y}$.
The variance of the simple sample mean under SRSWOR is:
$$V(\bar{y}) = \frac{1 - f}{n} S_y^2$$

The ratio estimator is more efficient than the simple sample mean if and only if:
$$\text{MSE}(\hat{\bar{Y}}_R) < V(\bar{y})$$
$$\frac{1 - f}{n} \left[ S_y^2 + R^2 S_x^2 - 2 R \rho S_y S_x \right] < \frac{1 - f}{n} S_y^2$$

Subtracting $S_y^2$ from both sides:
$$R^2 S_x^2 - 2 R \rho S_y S_x < 0$$
Dividing by $R S_x > 0$:
$$R S_x - 2 \rho S_y < 0 \implies 2 \rho S_y > R S_x$$
Substituting $R = \bar{Y} / \bar{X}$:
$$2 \rho S_y > \frac{\bar{Y}}{\bar{X}} S_x \implies \rho > \frac{1}{2} \frac{S_x / \bar{X}}{S_y / \bar{Y}} = \frac{1}{2} \frac{C_x}{C_y}$$

This delivers the celebrated **Efficiency Criterion for the Ratio Estimator**:
$$\rho > \frac{C_x}{2 C_y}$$

#### Critical Implications of the Efficiency Threshold:
1. **Positive Correlation is Insufficient**: It is not enough for $\rho$ to be positive ($\rho > 0$). If $C_x$ is substantially larger than $C_y$ (the auxiliary variable is much more dispersed than the target variable), the threshold $\frac{C_x}{2 C_y}$ can be large (e.g., $0.60$ or $0.75$). If $\rho = 0.40$, applying the ratio estimator will **increase the variance** rather than decrease it!
2. **Equal Variances**: When the coefficients of variation are equal ($C_x \approx C_y$), the condition becomes simply $\rho > 0.50$. The correlation between $y$ and $x$ must exceed $0.50$ for the ratio estimator to outperform simple random sampling.
3. **Diagnostic Rule**: A survey statistician should never blindly apply ratio estimation without first verifying that the sample correlation satisfies $r > \frac{c_x}{2 c_y}$.

---

## The Linear Regression Estimator: Derivation and Optimal Variance

While the ratio estimator is highly effective when the relationship between $y$ and $x$ is linear and passes through the origin, it loses efficiency when the relationship has a non-zero intercept. The **linear regression estimator** relaxes this constraint, accommodating any linear relationship $y = \alpha + \beta x + \varepsilon$ with an arbitrary intercept.

### The Difference Estimator as a Theoretical Precursor

To understand the regression estimator, we first examine the **difference estimator**. Suppose $k$ is a pre-determined mathematical constant chosen before observing the sample. The difference estimator of the population mean is:
$$\bar{y}_d = \bar{y} - k(\bar{x} - \bar{X})$$

#### Properties:
1. **Strict Design Unbiasedness**:
   $$E(\bar{y}_d) = E(\bar{y}) - k[E(\bar{x}) - \bar{X}] = \bar{Y} - k[\bar{X} - \bar{X}] = \bar{Y}$$
   The difference estimator is strictly unbiased for any constant $k$.
2. **Exact Sampling Variance**:
   $$V(\bar{y}_d) = V(\bar{y}) + k^2 V(\bar{x}) - 2 k \text{Cov}(\bar{y}, \bar{x}) = \frac{1 - f}{n} \left[ S_y^2 + k^2 S_x^2 - 2 k S_{xy} \right]$$
3. **Optimal Multiplier**:
   Differentiating $V(\bar{y}_d)$ with respect to $k$ and setting to zero:
   $$2 k S_x^2 - 2 S_{xy} = 0 \implies k_{opt} = \frac{S_{xy}}{S_x^2} = B$$
   where $B$ is the population linear regression slope of $y$ on $x$.
   Substituting $k = B$ into the variance formula:
   $$V(\bar{y}_d \mid k = B) = \frac{1 - f}{n} \left[ S_y^2 + \frac{S_{xy}^2}{S_x^4} S_x^2 - 2 \frac{S_{xy}}{S_x^2} S_{xy} \right] = \frac{1 - f}{n} \left[ S_y^2 - \frac{S_{xy}^2}{S_x^2} \right]$$
   Since $\rho^2 = \frac{S_{xy}^2}{S_y^2 S_x^2}$, we have:
   $$V_{opt}(\bar{y}_d) = \frac{1 - f}{n} S_y^2 (1 - \rho^2)$$

### The Linear Regression Estimator

In practice, the true population regression slope $B = S_{xy} / S_x^2$ is unknown. We estimate it from the sample using the ordinary least squares slope:
$$b = \frac{s_{xy}}{s_x^2} = \frac{\sum_{i \in s} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i \in s} (x_i - \bar{x})^2}$$

The **Linear Regression Estimator** of the population mean is:
$$\bar{y}_{lr} = \bar{y} + b(\bar{X} - \bar{x})$$

The corresponding estimator of the population total is:
$$\hat{Y}_{lr} = N \bar{y}_{lr} = N \bar{y} + b(X - N \bar{x})$$

### Finite-Sample Bias and Asymptotic Variance

Because $b$ is a stochastic random variable that covaries with $\bar{x}$, $\bar{y}_{lr}$ has a slight finite-sample bias:
$$\text{Bias}(\bar{y}_{lr}) = - \text{Cov}(b, \bar{x})$$
Under bivariate normality, $\text{Cov}(b, \bar{x}) = 0$, making $\bar{y}_{lr}$ strictly unbiased. In general finite populations, the bias is of order $O(1/n)$ and vanishes rapidly as $n$ grows.

To first order of approximation, the variance of the linear regression estimator is equal to the optimal difference variance:
$$V(\bar{y}_{lr}) \approx \frac{1 - f}{n} S_y^2 (1 - \rho^2)$$

An approximately unbiased sample estimator of this variance is:
$$\hat{V}(\bar{y}_{lr}) = \frac{1 - f}{n} s_y^2 (1 - r^2) = \frac{1 - f}{n(n - 2)} \sum_{i \in s} (y_i - \bar{y} - b(x_i - \bar{x}))^2$$
where $r = \frac{s_{xy}}{s_y s_x}$ is the sample correlation coefficient.

### Universal Superiority of the Regression Estimator

Comparing the asymptotic variance of the regression estimator with the simple random sampling mean:
$$V(\bar{y}_{lr}) \approx \frac{1 - f}{n} S_y^2 (1 - \rho^2) \le \frac{1 - f}{n} S_y^2 = V(\bar{y})$$
Because $\rho^2 \ge 0$, the regression estimator **never increases variance** relative to simple random sampling (to order $O(1/n)$). Even if the correlation is weak (e.g., $\rho = 0.20$), the regression estimator reduces variance by $1 - 0.20^2 = 4\%$. If the correlation is strong (e.g., $\rho = 0.90$), it reduces variance by $1 - 0.90^2 = 81\%$.

Now compare the regression estimator with the ratio estimator:
$$\text{MSE}(\hat{\bar{Y}}_R) - V(\bar{y}_{lr}) \approx \frac{1 - f}{n} \left[ (S_y^2 + R^2 S_x^2 - 2 R S_{xy}) - (S_y^2 - \frac{S_{xy}^2}{S_x^2}) \right]$$
$$= \frac{1 - f}{n} \left[ R^2 S_x^2 - 2 R S_{xy} + \frac{S_{xy}^2}{S_x^2} \right] = \frac{1 - f}{n} \left[ R S_x - \frac{S_{xy}}{S_x} \right]^2 = \frac{1 - f}{n} S_x^2 (R - B)^2 \ge 0$$

This yields an essential mathematical theorem:
$$V(\bar{y}_{lr}) \le \text{MSE}(\hat{\bar{Y}}_R)$$
The linear regression estimator is **always more precise than or equal to the ratio estimator**. The two estimators achieve identical precision if and only if $R = B$, which occurs when the population regression line passes strictly through the origin ($\alpha = \bar{Y} - B \bar{X} = 0$).

---

## Separate versus Combined Estimation in Stratified Sampling

When the population is partitioned into $L$ strata and auxiliary totals $X_h$ are known for each stratum $h$, two distinct approaches exist for constructing ratio and regression estimators:

### 1. The Combined Estimator
In combined estimation, a single overall ratio or regression slope is computed across all strata:
$$\hat{\bar{Y}}_{RC} = \frac{\bar{y}_{st}}{\bar{x}_{st}} \bar{X}$$
$$\bar{y}_{lrc} = \bar{y}_{st} + b_c(\bar{X} - \bar{x}_{st})$$
where $\bar{y}_{st} = \sum_{h=1}^L W_h \bar{y}_h$ and $\bar{x}_{st} = \sum_{h=1}^L W_h \bar{x}_h$.

The bias of the combined estimator is of order $O(1/n)$, where $n = \sum n_h$ is the total sample size across the entire survey.

### 2. The Separate Estimator
In separate estimation, independent ratio or regression estimators are computed within each individual stratum $h$, and then aggregated:
$$\hat{\bar{Y}}_{RS} = \sum_{h=1}^L W_h \hat{R}_h \bar{X}_h = \sum_{h=1}^L W_h \frac{\bar{y}_h}{\bar{x}_h} \bar{X}_h$$
$$\bar{y}_{lrs} = \sum_{h=1}^L W_h \left[ \bar{y}_h + b_h(\bar{X}_h - \bar{x}_h) \right]$$

#### The Bias vs. Precision Trade-off:
- **Precision Gain**: If the true regression slopes $B_h$ differ markedly across strata, the separate estimator captures these stratum-specific slopes, achieving a lower variance than the combined estimator:
  $$V(\bar{y}_{lrs}) \le V(\bar{y}_{lrc})$$
- **Cumulative Bias Hazard**: The separate estimator incurs a bias in every single stratum of order $O(1/n_h)$. Summing across $L$ strata, the total bias can accumulate to $L \times O(1/n_h)$. If the within-stratum sample sizes $n_h$ are small (e.g., $n_h = 10$ or $15$), this cumulative bias can become severe.

**Standard Survey Rule**: 
- If sample sizes within strata are large ($n_h \ge 30$ or $50$ for all $h$), use the **separate estimator**.
- If sample sizes within strata are small ($n_h < 20$) or if slopes $B_h$ are relatively homogeneous across strata, use the **combined estimator** to protect against cumulative bias.

---

## Calibration Weighting and the Deville–Särndal Framework

In modern official statistics, surveys collect data on dozens of demographic, geographic, and economic variables simultaneously. The classical univariate ratio and regression estimators cannot readily accommodate multi-dimensional benchmark constraints across dozens of overlapping margins.

In 1992, Jean-Claude Deville and Carl-Erik Särndal formulated a universal optimization framework known as **Calibration Weighting**. Calibration transforms survey weighting into a constrained mathematical optimization problem.

### Formal Formulation of the Calibration Problem

Let $s \subset U$ denote a probability sample drawn with design weights:
$$d_k = \frac{1}{\pi_k} \quad (k \in s)$$
Associated with each sampled unit $k$ is an auxiliary vector of $p$ characteristics:
$$\mathbf{x}_k = (x_{k1}, x_{k2}, \dots, x_{kp})^\top$$
The population totals of these auxiliary variables are known from external censuses or administrative registers:
$$\mathbf{X} = \sum_{k \in U} \mathbf{x}_k = (X_1, X_2, \dots, X_p)^\top$$

The objective of calibration is to find a set of new, calibrated weights $\{w_k : k \in s\}$ that:
1. Are as close as possible to the original design weights $d_k$, according to a pre-specified distance metric $G(w_k / d_k)$.
2. Satisfy the **Calibration Equations** (benchmarking constraints) exactly:
   $$\sum_{k \in s} w_k \mathbf{x}_k = \mathbf{X}$$

### The Optimization Problem

Mathematically, calibration solves the constrained minimization problem:
$$\min_{\{w_k\}_{k \in s}} \sum_{k \in s} \frac{d_k}{q_k} G\left( \frac{w_k}{d_k} \right) \quad \text{subject to} \quad \sum_{k \in s} w_k \mathbf{x}_k = \mathbf{X}$$
where:
- $G(u)$ is a strictly convex distance function satisfying $G(1) = 0$, $G'(1) = 0$, and $G''(1) = 1$.
- $q_k > 0$ are known scaling factors (typically $q_k = 1$).

### Classical Distance Functions

The choice of distance function $G(u)$ determines the operational behavior and range of the calibrated weights:

1. **Linear (Chi-Square) Distance**:
   $$G(u) = \frac{1}{2}(u - 1)^2$$
   This leads directly to the **Generalized Regression Estimator (GREG)**. It admits an exact closed-form analytical solution. However, linear calibration can occasionally produce negative weights ($w_k < 0$), which are physically impossible in survey estimation.

2. **Exponential (Raking / Entropy) Distance**:
   $$G(u) = u \log u - u + 1$$
   This leads to **Iterative Proportional Fitting (Multiplicative Raking)**. Because $u \log u$ is defined only for $u > 0$, the calibrated weights are **guaranteed to be strictly positive** ($w_k > 0$ for all $k$).

3. **Logit (Bounded) Distance**:
   $$G(u) = (u - L) \log\left( \frac{u - L}{1 - L} \right) + (U - u) \log\left( \frac{U - u}{U - 1} \right)$$
   This restricts the weight adjustment factor to a pre-specified bounded interval:
   $$L < \frac{w_k}{d_k} < U \quad \text{where } L < 1 < U$$
   Bounded calibration prevents extreme weight inflation, protecting estimators against excessive variance while maintaining exact benchmarking.

### The Generalized Regression Estimator (GREG)

Under the linear distance function $G(u) = \frac{1}{2}(u - 1)^2$, the optimization problem is solved using Lagrange multipliers.
The Lagrangian is:
$$\mathcal{L} = \frac{1}{2} \sum_{k \in s} d_k \left( \frac{w_k}{d_k} - 1 \right)^2 - \boldsymbol{\lambda}^\top \left( \sum_{k \in s} w_k \mathbf{x}_k - \mathbf{X} \right)$$

Differentiating with respect to $w_k$ and setting to zero:
$$\frac{\partial \mathcal{L}}{\partial w_k} = \frac{w_k}{d_k} - 1 - \boldsymbol{\lambda}^\top \mathbf{x}_k = 0 \implies w_k = d_k (1 + \boldsymbol{\lambda}^\top \mathbf{x}_k)$$

Substitute $w_k$ into the calibration equations:
$$\sum_{k \in s} d_k (1 + \boldsymbol{\lambda}^\top \mathbf{x}_k) \mathbf{x}_k = \mathbf{X}$$
$$\sum_{k \in s} d_k \mathbf{x}_k + \left( \sum_{k \in s} d_k \mathbf{x}_k \mathbf{x}_k^\top \right) \boldsymbol{\lambda} = \mathbf{X}$$

Let $\hat{\mathbf{X}}_\pi = \sum_{k \in s} d_k \mathbf{x}_k$ denote the uncalibrated Horvitz–Thompson estimator of the auxiliary totals. Then:
$$\left( \sum_{k \in s} d_k \mathbf{x}_k \mathbf{x}_k^\top \right) \boldsymbol{\lambda} = \mathbf{X} - \hat{\mathbf{X}}_\pi$$

Assuming the sample covariance matrix $\hat{\mathbf{T}}_{xx} = \sum_{k \in s} d_k \mathbf{x}_k \mathbf{x}_k^\top$ is invertible:
$$\boldsymbol{\lambda} = \left( \sum_{k \in s} d_k \mathbf{x}_k \mathbf{x}_k^\top \right)^{-1} (\mathbf{X} - \hat{\mathbf{X}}_\pi)$$

Substituting $\boldsymbol{\lambda}$ back into the weight formula yields the **Exact GREG Weight Formula**:
$$w_k = d_k \left[ 1 + (\mathbf{X} - \hat{\mathbf{X}}_\pi)^\top \left( \sum_{j \in s} d_j \mathbf{x}_j \mathbf{x}_j^\top \right)^{-1} \mathbf{x}_k \right]$$

The calibrated GREG estimator of the population total of any survey variable $y$ is:
$$\hat{Y}_{GREG} = \sum_{k \in s} w_k y_k = \hat{Y}_\pi + (\mathbf{X} - \hat{\mathbf{X}}_\pi)^\top \hat{\mathbf{B}}$$
where $\hat{\mathbf{B}} = \left( \sum_{j \in s} d_j \mathbf{x}_j \mathbf{x}_j^\top \right)^{-1} \sum_{j \in s} d_j \mathbf{x}_j y_j$ is the weighted least-squares regression coefficient vector.

### Asymptotic Equivalence Theorem
Deville and Särndal (1992) proved a remarkable theoretical result: For any valid distance function $G(u)$, the resulting calibrated estimator $\hat{Y}_{cal} = \sum_{k \in s} w_k y_k$ is **asymptotically equivalent to the Generalized Regression Estimator (GREG)** to first order of approximation:
$$\frac{1}{N} \hat{Y}_{cal} = \frac{1}{N} \hat{Y}_{GREG} + O_p(n^{-1})$$
Consequently, all calibration estimators (whether linear, raking, or logit) share the exact same asymptotic variance:
$$V(\hat{Y}_{cal}) \approx \sum_{i=1}^N \sum_{j=1}^N (\pi_{ij} - \pi_i \pi_j) \frac{E_i}{\pi_i} \frac{E_j}{\pi_j}$$
where $E_i = y_i - \mathbf{x}_i^\top \mathbf{B}$ are the population regression residuals.

---

## Fully worked question 1: First-Order Taylor Expansion Derivation of Ratio Estimator MSE and Verification of the Correlation Threshold

**Question.** An agricultural census authority conducts an objective survey to estimate the total production of organic soybeans across an agricultural valley. The valley comprises $N = 600$ commercial farms. The survey variable $y_i$ is soybean production (in metric tons), and the auxiliary variable $x_i$ is cultivated soybean area (in hectares) recorded in cadastral tax records.

The known total cultivated area across all 600 farms is:
$$X = 12,000 \text{ hectares} \implies \bar{X} = 20.0 \text{ ha/farm}$$

A simple random sample without replacement (SRSWOR) of $n = 50$ farms is selected. From a comprehensive historic baseline, the population parameters are known to be:
- Mean production: $\bar{Y} = 48.0 \text{ metric tons/farm}$ (so total production is $Y = 28,800 \text{ tons}$)
- Variance of production: $S_y^2 = 576.0 \text{ (tons)}^2 \implies S_y = 24.0 \text{ tons}$
- Variance of area: $S_x^2 = 64.0 \text{ (ha)}^2 \implies S_x = 8.0 \text{ ha}$
- Covariance: $S_{xy} = 144.0 \text{ ton}\cdot\text{ha}$

1. Compute the coefficients of variation $C_y$, $C_x$, the Pearson correlation coefficient $\rho$, and the population ratio $R$.
2. State and evaluate the exact efficiency criterion condition $\rho > \frac{C_x}{2 C_y}$. Does the ratio estimator outperform the simple sample mean in this population?
3. Calculate:
   - The finite-sample bias of the ratio estimator of the mean $\hat{\bar{Y}}_R$.
   - The approximate Mean Squared Error $\text{MSE}(\hat{\bar{Y}}_R)$ and standard error $\text{SE}(\hat{\bar{Y}}_R)$.
   - The variance of the unadjusted sample mean $V(\bar{y})$ and standard error $\text{SE}(\bar{y})$.
   - The Relative Efficiency of the ratio estimator compared to the unadjusted sample mean.

**Solution, step 1: Computing coefficients of variation, correlation, and population ratio.**
Given:
- $N = 600$, $n = 50$, sampling fraction $f = n/N = 50/600 = 1/12 \approx 0.083333$
- Finite population correction: $1 - f = 1 - 0.083333 = 11/12 \approx 0.916667$
- $\bar{Y} = 48.0$, $S_y = 24.0$
- $\bar{X} = 20.0$, $S_x = 8.0$
- $S_{xy} = 144.0$

1. **Coefficients of Variation**:
   $$C_y = \frac{S_y}{\bar{Y}} = \frac{24.0}{48.0} = 0.500$$
   $$C_x = \frac{S_x}{\bar{X}} = \frac{8.0}{20.0} = 0.400$$

2. **Pearson Correlation Coefficient**:
   $$\rho = \frac{S_{xy}}{S_y S_x} = \frac{144.0}{24.0 \times 8.0} = \frac{144.0}{192.0} = 0.750$$

3. **Population Ratio**:
   $$R = \frac{\bar{Y}}{\bar{X}} = \frac{48.0}{20.0} = 2.40 \text{ tons per hectare}$$

**Solution, step 2: Evaluating the efficiency threshold condition.**
The ratio estimator is more efficient than the simple sample mean if and only if:
$$\rho > \frac{C_x}{2 C_y}$$

Compute the threshold value:
$$\text{Threshold} = \frac{C_x}{2 C_y} = \frac{0.400}{2 \times 0.500} = \frac{0.400}{1.000} = 0.400$$

Comparing the observed correlation with the threshold:
$$\rho = 0.750 > 0.400$$
The correlation coefficient ($\rho = 0.75$) substantially exceeds the critical threshold ($0.40$). Therefore, the ratio estimator is mathematically guaranteed to achieve superior precision over the simple sample mean.

**Solution, step 3: Calculating bias, MSE, variance, and relative efficiency.**

1. **Finite-Sample Bias of $\hat{\bar{Y}}_R$**:
   $$\text{Bias}(\hat{\bar{Y}}_R) \approx \bar{Y} \frac{1 - f}{n} C_x (C_x - \rho C_y)$$
   Substitute the parameters:
   $$C_x - \rho C_y = 0.400 - 0.750 \times 0.500 = 0.400 - 0.375 = 0.025$$
   $$\frac{1 - f}{n} = \frac{0.916667}{50} = 0.0183333$$
   $$\text{Bias}(\hat{\bar{Y}}_R) \approx 48.0 \times 0.0183333 \times 0.400 \times 0.025 = 48.0 \times 0.0183333 \times 0.010 = 0.00880 \text{ metric tons}$$
   Notice how tiny this bias is: $0.0088$ tons relative to the mean of $48.0$ tons is a relative bias of just $+0.018\%$, completely negligible in practice.

2. **Mean Squared Error of $\hat{\bar{Y}}_R$**:
   $$\text{MSE}(\hat{\bar{Y}}_R) \approx \frac{1 - f}{n} \left[ S_y^2 + R^2 S_x^2 - 2 R S_{xy} \right]$$
   Compute each component:
   - $S_y^2 = 576.0$
   - $R^2 S_x^2 = (2.40)^2 \times 64.0 = 5.76 \times 64.0 = 368.64$
   - $2 R S_{xy} = 2 \times 2.40 \times 144.0 = 4.80 \times 144.0 = 691.20$

   Summing inside the bracket:
   $$S_d^2 = 576.0 + 368.64 - 691.20 = 253.44$$
   Multiplying by $\frac{1 - f}{n} = 0.0183333$:
   $$\text{MSE}(\hat{\bar{Y}}_R) \approx 0.0183333 \times 253.44 = 4.6464 \text{ (tons)}^2$$
   The standard error of the ratio estimator is:
   $$\text{SE}(\hat{\bar{Y}}_R) = \sqrt{4.6464} = 2.1555 \text{ metric tons}$$

   Checking the bias-to-standard-error ratio:
   $$\frac{\text{Bias}}{\text{SE}} = \frac{0.00880}{2.1555} \approx 0.0041 < 0.10$$
   This formally verifies Cochran's criterion: the bias accounts for less than $0.5\%$ of the standard error and has zero impact on confidence intervals.

3. **Variance of the Unadjusted Sample Mean $V(\bar{y})$**:
   $$V(\bar{y}) = \frac{1 - f}{n} S_y^2 = 0.0183333 \times 576.0 = 10.5600 \text{ (tons)}^2$$
   The standard error of the unadjusted sample mean is:
   $$\text{SE}(\bar{y}) = \sqrt{10.5600} \approx 3.2496 \text{ metric tons}$$

4. **Relative Efficiency**:
   $$\text{RE} = \frac{V(\bar{y})}{\text{MSE}(\hat{\bar{Y}}_R)} = \frac{10.5600}{4.6464} = 2.2727$$
   The ratio estimator is **$2.27$ times more efficient** than the unadjusted sample mean, slashing sampling variance by $56.0\%$. To achieve the same precision with the unadjusted sample mean, the agency would have had to survey $n = 50 \times 2.2727 \approx 114$ farms instead of 50.

---

## Fully worked question 2: Linear Regression Estimator Derivation, Optimal Slope and Variance Comparison with Ratio Estimator

**Question.** An urban planning agency investigates residential electrical energy consumption across $N = 1,000$ apartment units in a metropolitan district. The survey variable $y_i$ is monthly electricity consumption (in kilowatt-hours, kWh), and the auxiliary variable $x_i$ is apartment interior floor area (in square meters, $\text{m}^2$).

The known total floor area of all 1,000 apartments is:
$$X = 85,000 \text{ m}^2 \implies \bar{X} = 85.0 \text{ m}^2$$

A sample of $n = 40$ apartments is selected via SRSWOR. The true population characteristics are:
- Mean electricity consumption: $\bar{Y} = 420.0 \text{ kWh}$
- Variance of electricity consumption: $S_y^2 = 14,400.0 \text{ (kWh)}^2 \implies S_y = 120.0 \text{ kWh}$
- Variance of floor area: $S_x^2 = 400.0 \text{ (m}^2)^2 \implies S_x = 20.0 \text{ m}^2$
- Correlation coefficient: $\rho = 0.850$

1. Compute the population linear regression slope $B = S_{xy} / S_x^2$ and the regression intercept $A = \bar{Y} - B \bar{X}$. Interpret the physical meaning of the non-zero intercept.
2. Compute the exact asymptotic variance of the Linear Regression Estimator $V(\bar{y}_{lr})$ and its standard error.
3. Compute the approximate Mean Squared Error of the Ratio Estimator $\text{MSE}(\hat{\bar{Y}}_R)$ for this same population.
4. Calculate the variance difference $\text{MSE}(\hat{\bar{Y}}_R) - V(\bar{y}_{lr})$ and verify that it matches the theoretical identity $\frac{1-f}{n} S_x^2 (R - B)^2$.

**Solution, step 1: Computing regression parameters and interpreting the intercept.**
Given:
- $N = 1,000$, $n = 40$, sampling fraction $f = 40 / 1,000 = 0.040$
- Finite population correction: $1 - f = 0.960$
- $\frac{1 - f}{n} = \frac{0.960}{40} = 0.0240$
- $\bar{X} = 85.0$, $S_x = 20.0$, $S_x^2 = 400.0$
- $\bar{Y} = 420.0$, $S_y = 120.0$, $S_y^2 = 14,400.0$
- $\rho = 0.850$

Compute population covariance:
$$S_{xy} = \rho S_y S_x = 0.850 \times 120.0 \times 20.0 = 0.850 \times 2,400.0 = 2,040.0 \text{ kWh}\cdot\text{m}^2$$

1. **Population Regression Slope**:
   $$B = \frac{S_{xy}}{S_x^2} = \frac{2,040.0}{400.0} = 5.10 \text{ kWh per m}^2$$
   Each additional square meter of apartment area is associated with an average increase of $5.10$ kWh in monthly electrical consumption.

2. **Population Regression Intercept**:
   $$A = \bar{Y} - B \bar{X} = 420.0 - 5.10 \times 85.0 = 420.0 - 433.5 = -13.50 \text{ kWh}$$

3. **Physical Interpretation**:
   The population regression line is $y = -13.50 + 5.10 x$. Because the intercept $A = -13.50 \ne 0$, the relationship between energy consumption and floor area does not pass through the origin. While the slope is strongly positive, small baseline baseload fixtures behave differently from space heating. Because $A \ne 0$, the ratio estimator will be sub-optimal compared to the linear regression estimator.

**Solution, step 2: Computing variance and standard error of the linear regression estimator.**
The asymptotic variance of the linear regression estimator is:
$$V(\bar{y}_{lr}) \approx \frac{1 - f}{n} S_y^2 (1 - \rho^2)$$

Evaluate the variance reduction factor:
$$1 - \rho^2 = 1 - (0.850)^2 = 1 - 0.7225 = 0.2775$$

Compute the variance:
$$V(\bar{y}_{lr}) \approx 0.0240 \times 14,400.0 \times 0.2775 = 345.60 \times 0.2775 = 95.904 \text{ (kWh)}^2$$

The standard error is:
$$\text{SE}(\bar{y}_{lr}) = \sqrt{95.904} \approx 9.793 \text{ kWh}$$

Notice the massive precision gain relative to simple random sampling:
$$V(\bar{y}) = \frac{1 - f}{n} S_y^2 = 0.0240 \times 14,400.0 = 345.60 \text{ (kWh)}^2$$
$$\text{SE}(\bar{y}) = \sqrt{345.60} \approx 18.590 \text{ kWh}$$
The regression estimator reduces sampling variance by $72.25\%$, cutting the standard error nearly in half.

**Solution, step 3: Computing Mean Squared Error of the ratio estimator.**
First, compute the population ratio:
$$R = \frac{\bar{Y}}{\bar{X}} = \frac{420.0}{85.0} \approx 4.941176 \text{ kWh/m}^2$$

Recall the MSE formula for the ratio estimator:
$$\text{MSE}(\hat{\bar{Y}}_R) \approx \frac{1 - f}{n} \left[ S_y^2 + R^2 S_x^2 - 2 R S_{xy} \right]$$

Compute each term inside the bracket:
- $S_y^2 = 14,400.0$
- $R^2 S_x^2 = (4.941176)^2 \times 400.0 \approx 24.415225 \times 400.0 = 9,766.090$
- $2 R S_{xy} = 2 \times 4.941176 \times 2,040.0 \approx 9.882353 \times 2,040.0 = 20,160.000$

Summing the terms:
$$S_d^2 = 14,400.0 + 9,766.090 - 20,160.000 = 4,006.090$$

Multiplying by $\frac{1 - f}{n} = 0.0240$:
$$\text{MSE}(\hat{\bar{Y}}_R) \approx 0.0240 \times 4,006.090 = 96.146 \text{ (kWh)}^2$$
The standard error of the ratio estimator is:
$$\text{SE}(\hat{\bar{Y}}_R) = \sqrt{96.146} \approx 9.805 \text{ kWh}$$

**Solution, step 4: Verifying the theoretical variance difference identity.**
Subtract the regression variance from the ratio MSE:
$$\Delta = \text{MSE}(\hat{\bar{Y}}_R) - V(\bar{y}_{lr}) = 96.14616 - 95.90400 = 0.24216 \text{ (kWh)}^2$$

Now evaluate the theoretical identity:
$$\Delta_{theory} = \frac{1 - f}{n} S_x^2 (R - B)^2$$
Substitute:
$$R - B = 4.941176 - 5.100000 = -0.158824$$
$$(R - B)^2 = (-0.158824)^2 \approx 0.0252250$$
$$\Delta_{theory} = 0.0240 \times 400.0 \times 0.0252250 = 9.60 \times 0.0252250 = 0.24216 \text{ (kWh)}^2$$

The two values match perfectly to five decimal places! This confirms that:
1. $V(\bar{y}_{lr}) \le \text{MSE}(\hat{\bar{Y}}_R)$ holds strictly.
2. The slight efficiency penalty of the ratio estimator is directly proportional to the squared divergence $(R - B)^2$, driven by the non-zero regression intercept $A = -13.50$.

---

## Fully worked question 3: Constructing Calibrated GREG Weights Under Multi-Dimensional Marginal Constraints

**Question.** A municipal labor force survey gathers data across a metropolitan workforce of $N = 10,000$ individuals. A simple random sample of $n = 5$ workers is drawn with initial design weights:
$$d_k = \frac{N}{n} = \frac{10,000}{5} = 2,000 \quad \text{for all } k = 1, \dots, 5$$

The survey measures monthly wages $y_k$ (in dollars), and two auxiliary demographic variables:
- $x_{k1} = 1$: Constant intercept term (representing total population headcount).
- $x_{k2}$: Age in years.

From official municipal civil registry records, the true population totals are known exactly:
- Total population headcount: $X_1 = N = 10,000$
- Total aggregate age: $X_2 = 400,000 \text{ person-years}$ (meaning true average population age is $\bar{X}_2 = 40.0 \text{ years}$)

The sample data gathered from the 5 individuals are:

$$\begin{array}{c|ccc}
\text{Sampled Individual } k & x_{k1} \text{ (Headcount)} & x_{k2} \text{ (Age, yrs)} & y_k \text{ (Wage, dollars)} \\
\hline
1 & 1 & 25 & 2,800 \\
2 & 1 & 35 & 3,600 \\
3 & 1 & 40 & 4,200 \\
4 & 1 & 45 & 5,000 \\
5 & 1 & 55 & 6,400 \\
\hline
\text{Sample Mean } \bar{\mathbf{x}} & 1.0 & 40.0 & 4,400
\end{array}$$

1. Compute the uncalibrated Horvitz–Thompson estimates of the auxiliary totals $\hat{X}_{1,\pi}$ and $\hat{X}_{2,\pi}$, and compute the uncalibrated estimate of total monthly wages $\hat{Y}_\pi$.
2. Formulate the Generalized Regression (GREG) calibration equations. Compute the sample matrix $\hat{\mathbf{T}}_{xx} = \sum_{k=1}^5 d_k \mathbf{x}_k \mathbf{x}_k^\top$, invert it, and calculate the Lagrange multiplier vector $\boldsymbol{\lambda}$.
3. Compute the calibrated weights $w_k$ for all 5 sampled individuals. Verify that:
   - The calibrated weights satisfy the two benchmarking equations exactly.
   - Compute the calibrated estimate of total wages $\hat{Y}_{GREG} = \sum_{k=1}^5 w_k y_k$.

**Solution, step 1: Computing uncalibrated Horvitz–Thompson estimates.**
With uniform design weights $d_k = 2,000$:
1. **Auxiliary Total 1 (Headcount)**:
   $$\hat{X}_{1,\pi} = \sum_{k=1}^5 d_k x_{k1} = 2,000 \times (1 + 1 + 1 + 1 + 1) = 2,000 \times 5 = 10,000$$
   Notice $\hat{X}_{1,\pi} = 10,000 = X_1$, so there is zero discrepancy on headcount.

2. **Auxiliary Total 2 (Aggregate Age)**:
   $$\hat{X}_{2,\pi} = \sum_{k=1}^5 d_k x_{k2} = 2,000 \times (25 + 35 + 40 + 45 + 55) = 2,000 \times 200 = 400,000$$
   Notice that the sample mean age is $\bar{x}_2 = 200 / 5 = 40.0$, which happens to match the true population mean $\bar{X}_2 = 40.0$!
   $$\mathbf{X} - \hat{\mathbf{X}}_\pi = \begin{pmatrix} 10,000 \\ 400,000 \end{pmatrix} - \begin{pmatrix} 10,000 \\ 400,000 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

To make this calibration problem instructive and demonstrate non-zero weight adjustments under unequal sample margins, let us consider a sample where the sample mean age diverges from the population mean!
Suppose Individual 5 had Age $x_{5,2} = 65$ (instead of 55), while individuals 1 to 4 remain as:
- $k = 1$: $x_{1,2} = 25$, $y_1 = 2,800$
- $k = 2$: $x_{2,2} = 35$, $y_2 = 3,600$
- $k = 3$: $x_{3,2} = 40$, $y_3 = 4,200$
- $k = 4$: $x_{4,2} = 45$, $y_4 = 5,000$
- $k = 5$: $x_{5,2} = 65$, $y_5 = 7,400$

Now recompute the sample values:
- Sample sum of age: $\sum_{k=1}^5 x_{k2} = 25 + 35 + 40 + 45 + 65 = 210$
- Sample mean age: $\bar{x}_2 = 210 / 5 = 42.0 \text{ years}$ (diverging from true population mean $40.0$)
- Estimated total age: $\hat{X}_{2,\pi} = 2,000 \times 210 = 420,000 \text{ person-years}$
- The discrepancy vector is:
  $$\mathbf{X} - \hat{\mathbf{X}}_\pi = \begin{pmatrix} 10,000 \\ 400,000 \end{pmatrix} - \begin{pmatrix} 10,000 \\ 420,000 \end{pmatrix} = \begin{pmatrix} 0 \\ -20,000 \end{pmatrix}$$
- Uncalibrated estimate of total wages:
  $$\sum y_k = 2,800 + 3,600 + 4,200 + 5,000 + 7,400 = 23,000$$
  $$\hat{Y}_\pi = 2,000 \times 23,000 = 46,000,000 \text{ dollars}$$

**Solution, step 2: Computing sample matrix $\hat{\mathbf{T}}_{xx}$, its inverse, and Lagrange multiplier $\boldsymbol{\lambda}$.**
Each observation has vector $\mathbf{x}_k = (1, x_{k2})^\top$.
The outer product matrix is:
$$\mathbf{x}_k \mathbf{x}_k^\top = \begin{pmatrix} 1 & x_{k2} \\ x_{k2} & x_{k2}^2 \end{pmatrix}$$

Compute the sums across the 5 sampled individuals:
- $\sum_{k=1}^5 1 = 5$
- $\sum_{k=1}^5 x_{k2} = 210$
- $\sum_{k=1}^5 x_{k2}^2 = 25^2 + 35^2 + 40^2 + 45^2 + 65^2 = 625 + 1,225 + 1,600 + 2,025 + 4,225 = 9,700$

Multiplying by uniform design weight $d = 2,000$:
$$\hat{\mathbf{T}}_{xx} = \sum_{k=1}^5 d_k \mathbf{x}_k \mathbf{x}_k^\top = 2,000 \times \begin{pmatrix} 5 & 210 \\ 210 & 9,700 \end{pmatrix} = \begin{pmatrix} 10,000 & 420,000 \\ 420,000 & 19,400,000 \end{pmatrix}$$

Compute the determinant:
$$\det\left(\begin{pmatrix} 5 & 210 \\ 210 & 9,700 \end{pmatrix}\right) = 5(9,700) - (210)^2 = 48,500 - 44,100 = 4,400$$
Notice that $4,400 = 5 \times \sum (x_{k2} - \bar{x}_2)^2 = 5 \times 880 = 4,400$.

The inverse of the unscaled matrix is:
$$\begin{pmatrix} 5 & 210 \\ 210 & 9,700 \end{pmatrix}^{-1} = \frac{1}{4,400} \begin{pmatrix} 9,700 & -210 \\ -210 & 5 \end{pmatrix}$$

Therefore, the inverse of $\hat{\mathbf{T}}_{xx}$ is:
$$\hat{\mathbf{T}}_{xx}^{-1} = \frac{1}{2,000 \times 4,400} \begin{pmatrix} 9,700 & -210 \\ -210 & 5 \end{pmatrix} = \frac{1}{8,800,000} \begin{pmatrix} 9,700 & -210 \\ -210 & 5 \end{pmatrix}$$

Now compute the Lagrange multiplier vector $\boldsymbol{\lambda} = \hat{\mathbf{T}}_{xx}^{-1} (\mathbf{X} - \hat{\mathbf{X}}_\pi)$:
$$\boldsymbol{\lambda} = \frac{1}{8,800,000} \begin{pmatrix} 9,700 & -210 \\ -210 & 5 \end{pmatrix} \begin{pmatrix} 0 \\ -20,000 \end{pmatrix}$$

Multiplying the matrix by the vector:
$$\begin{pmatrix} 9,700(0) + (-210)(-20,000) \\ -210(0) + 5(-20,000) \end{pmatrix} = \begin{pmatrix} 4,200,000 \\ -100,000 \end{pmatrix}$$

Dividing by $8,800,000$:
$$\lambda_1 = \frac{4,200,000}{8,800,000} = \frac{42}{88} = \frac{21}{44} \approx 0.477273$$
$$\lambda_2 = \frac{-100,000}{8,800,000} = \frac{-1}{88} \approx -0.0113636$$

Thus:
$$\boldsymbol{\lambda} = \begin{pmatrix} 21/44 \\ -1/88 \end{pmatrix}$$

**Solution, step 3: Computing calibrated weights and verifying constraints.**
The GREG weight formula is:
$$w_k = d_k (1 + \boldsymbol{\lambda}^\top \mathbf{x}_k) = 2,000 \left[ 1 + \lambda_1 (1) + \lambda_2 x_{k2} \right] = 2,000 \left[ 1 + \frac{21}{44} - \frac{1}{88} x_{k2} \right]$$
$$w_k = 2,000 \left[ \frac{65}{44} - \frac{x_{k2}}{88} \right] = 2,000 \left[ \frac{130 - x_{k2}}{88} \right] = \frac{2,000}{88} (130 - x_{k2}) = \frac{250}{11} (130 - x_{k2})$$

Now compute the exact calibrated weight for each individual:
1. Individual 1 ($x_{1,2} = 25$):
   $$w_1 = \frac{250}{11} (130 - 25) = \frac{250 \times 105}{11} = \frac{26,250}{11} \approx 2,386.3636$$
2. Individual 2 ($x_{2,2} = 35$):
   $$w_2 = \frac{250}{11} (130 - 35) = \frac{250 \times 95}{11} = \frac{23,750}{11} \approx 2,159.0909$$
3. Individual 3 ($x_{3,2} = 40$):
   $$w_3 = \frac{250}{11} (130 - 40) = \frac{250 \times 90}{11} = \frac{22,500}{11} \approx 2,045.4545$$
4. Individual 4 ($x_{4,2} = 45$):
   $$w_4 = \frac{250}{11} (130 - 45) = \frac{250 \times 85}{11} = \frac{21,250}{11} \approx 1,931.8182$$
5. Individual 5 ($x_{5,2} = 65$):
   $$w_5 = \frac{250}{11} (130 - 65) = \frac{250 \times 65}{11} = \frac{16,250}{11} \approx 1,477.2727$$

Notice the intuitive behavior of the calibrated weights: because the sample was over-represented by older individuals (mean age 42 vs true age 40), calibration **downweights** the older individuals ($w_5 = 1,477 < 2,000$) and **upweights** the younger individuals ($w_1 = 2,386 > 2,000$) to balance the distribution! All weights remain strictly positive.

Now verify the calibration benchmarking equations:
1. **Constraint 1 (Headcount Total = 10,000)**:
   $$\sum_{k=1}^5 w_k = \frac{26,250 + 23,750 + 22,500 + 21,250 + 16,250}{11} = \frac{110,000}{11} = 10,000.000$$
   Exact match!

2. **Constraint 2 (Total Person-Years = 400,000)**:
   $$\sum_{k=1}^5 w_k x_{k2} = \frac{26,250(25) + 23,750(35) + 22,500(40) + 21,250(45) + 16,250(65)}{11}$$
   - $26,250 \times 25 = 656,250$
   - $23,750 \times 35 = 831,250$
   - $22,500 \times 40 = 900,000$
   - $21,250 \times 45 = 956,250$
   - $16,250 \times 65 = 1,056,250$
   Summing the products:
   $$656,250 + 831,250 + 900,000 + 956,250 + 1,056,250 = 4,400,000$$
   Dividing by 11:
   $$\sum_{k=1}^5 w_k x_{k2} = \frac{4,400,000}{11} = 400,000.000$$
   Exact match! The calibrated weights satisfy both population benchmarks to the exact integer.

Finally, compute the calibrated GREG estimate of total monthly wages:
$$\hat{Y}_{GREG} = \sum_{k=1}^5 w_k y_k = \frac{26,250(2,800) + 23,750(3,600) + 22,500(4,200) + 21,250(5,000) + 16,250(7,400)}{11}$$
Compute each term:
- $26,250 \times 2,800 = 73,500,000$
- $23,750 \times 3,600 = 85,500,000$
- $22,500 \times 4,200 = 94,500,000$
- $21,250 \times 5,000 = 106,250,000$
- $16,250 \times 7,400 = 120,250,000$

Summing all 5 terms:
$$\text{Numerator} = 73,500,000 + 85,500,000 + 94,500,000 + 106,250,000 + 120,250,000 = 480,000,000$$
Dividing by 11:
$$\hat{Y}_{GREG} = \frac{480,000,000}{11} \approx 43,636,363.64 \text{ dollars}$$

Compare this with the uncalibrated estimate:
$$\hat{Y}_\pi = 46,000,000 \text{ dollars}$$
Because the sample was artificially skewed toward higher-earning older individuals, the uncalibrated estimator substantially overestimated municipal payroll. Calibration automatically corrected this demographic imbalance, adjusting the estimate downward by 2,363,636 dollars to reflect the true age distribution of the city.

---

## Practical Synthesis and Implementation Guidelines

In modern survey software suites (such as R's `survey` package or Python's `samplics`), calibration weighting is the standard production step connecting raw field data to published official estimates.

### Best-Practice Calibration Workflow:
1. **Formulate Auxiliary Vector $\mathbf{x}_k$**: Include an intercept term $1$ to preserve the population size $N$, followed by indicator dummy variables for categorical margins (age categories, sex, educational levels, geographic districts). To prevent collinearity, drop one redundant category per marginal partition.
2. **Execute Linear Calibration (GREG)**: Compute initial weights. Inspect the resulting weight distribution:
   - Check the minimum weight $\min w_k$. If any $w_k < 0$, linear calibration is discarded.
   - Check the ratio of maximum to minimum weight $\max w_k / \min w_k$. If the ratio exceeds $10.0$ or $15.0$, variance inflation will occur.
3. **Switch to Logit or Raking Calibration if Needed**: If linear weights are negative or extreme, rerun calibration using the **Logit distance function** with bounds $[L, U] = [0.4, 2.5]$, ensuring that no weight is reduced below $40\%$ or inflated above $250\%$ of its design weight.
4. **Variance Estimation via Linearized Residuals**: To estimate standard errors of calibrated estimators, compute the survey residuals $e_k = y_k - \mathbf{x}_k^\top \hat{\mathbf{B}}$. Apply the complex survey design variance formula (incorporating strata and clusters) directly to the weighted residuals $w_k e_k$, guaranteeing honest standard errors.

In the next unit, we address what happens when sampled units cannot be observed—examining Survey Nonresponse, Imputation, and the Total Survey Error paradigm.
