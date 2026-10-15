# tooling/expand-unit-6.py
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "r", encoding="utf-8") as f:
    text = f.read()

addition = r"""

---

## 6.6 Specialized Bootstrap Methodologies: Parametric, Residual, Wild, and Block Bootstrapping

While Efron's classical non-parametric bootstrap assumes that observations are independent and identically distributed (i.i.d.), complex empirical models frequently violate pure exchangeability. In econometric regressions, error variances vary across observation clusters (heteroscedasticity); in financial and macroeconomic data, observations exhibit persistent serial autocorrelation across time. To handle these non-standard data structures, mathematical statisticians developed specialized bootstrap variants.

### 1. The Parametric Bootstrap

In settings where a specific parametric family $F_{\boldsymbol{\theta}}$ is theoretically justified (e.g. Poisson count models, Extreme Value distributions, or Gaussian processes), but the finite-sample distribution of an estimator $\hat{\psi} = g(\hat{\boldsymbol{\theta}})$ is analytically intractable:
1. Estimate parameters via Maximum Likelihood Estimation (MLE): $\hat{\boldsymbol{\theta}} = \arg\max_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta} \mid \mathbf{x})$.
2. For $b = 1, \dots, B$, draw synthetic bootstrap samples directly from the fitted parametric density:
   $$\mathbf{x}^{*b} \sim F_{\hat{\boldsymbol{\theta}}}$$
3. Re-estimate the parameter on each synthetic sample: $\hat{\boldsymbol{\theta}}^{*b}$.
The parametric bootstrap yields higher statistical efficiency (smaller variance) than the non-parametric bootstrap whenever the parametric model is correctly specified, but is sensitive to model misspecification.

### 2. Regression Resampling: Pairs Bootstrap vs Residual Bootstrap

In multiple linear regression $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$, there are two distinct ways to execute the non-parametric bootstrap:

#### A. Pairs (Case) Resampling:
Resamples whole observational tuples $(y_i, \mathbf{x}_i)$ with replacement:
$$(\mathbf{y}^*, \mathbf{X}^*) \sim \text{ResampleWithReplacement}(\{ (y_1, \mathbf{x}_1), \dots, (y_n, \mathbf{x}_n) \})$$
- **Properties**: Treats the regressors $\mathbf{X}$ as stochastic (random design). It is completely robust against heteroscedasticity ($\text{Var}(\epsilon_i \mid \mathbf{x}_i) = \sigma^2(\mathbf{x}_i)$) because the joint relationship between $\mathbf{x}_i$ and the residual magnitude is preserved in the sampled pairs.
- **Risk**: In small samples with collinear features, some bootstrap matrices $\mathbf{X}^*$ may fail to have full column rank, triggering singular matrix inversion errors.

#### B. Residual (Model-Based) Resampling:
Treats the regressors $\mathbf{X}$ as fixed (fixed design):
1. Fit the full OLS model to obtain coefficients $\hat{\boldsymbol{\beta}}$ and residuals $e_i = y_i - \mathbf{x}_i \hat{\boldsymbol{\beta}}$.
2. Center the residuals: $\tilde{e}_i = e_i - \bar{e}$.
3. Resample the centered residuals with replacement: $e_1^*, \dots, e_n^*$.
4. Construct synthetic responses: $y_i^* = \mathbf{x}_i \hat{\boldsymbol{\beta}} + e_i^*$.
5. Regress $\mathbf{y}^*$ on the fixed design matrix $\mathbf{X}$.
- **Virtue**: Because $\mathbf{X}$ is fixed, $(\mathbf{X}^\top \mathbf{X})^{-1}$ is factored only **once**, making residual bootstrapping exceptionally fast ($\mathcal{O}(n p)$ per resample).
- **Flaw**: Strictly assumes homoscedasticity ($\text{Var}(\epsilon_i) = \sigma^2$). If the true errors are heteroscedastic, residual resampling produces invalid standard errors.

### 3. The Wild Bootstrap for Heteroscedastic Regressions

To combine the computational speed of residual resampling with robustness against arbitrary unknown heteroscedasticity, C. F. J. Wu (1986) and Enno Mammen (1993) formulated the **Wild Bootstrap**.

Instead of resampling residuals across different observations, the Wild Bootstrap modifies each observation's residual in-place by multiplying it by an independent scalar random weight $v_i^*$:

$$y_i^* = \mathbf{x}_i \hat{\boldsymbol{\beta}} + e_i \cdot v_i^*$$

where the random variables $v_1^*, \dots, v_n^*$ are drawn independently from an external auxiliary distribution satisfying the moment conditions:

$$\mathbb{E}[v_i^*] = 0, \quad \mathbb{E}[(v_i^*)^2] = 1, \quad \mathbb{E}[(v_i^*)^3] = 1$$

#### Mammen's Two-Point Auxiliary Distribution:
Mammen demonstrated that the unique two-point distribution satisfying all three moment conditions is:

$$v_i^* = \begin{cases} \frac{1 - \sqrt{5}}{2} \approx -0.618034 & \text{with probability } p = \frac{\sqrt{5} + 1}{2\sqrt{5}} \approx 0.723607 \\ \frac{1 + \sqrt{5}}{2} \approx +1.618034 & \text{with probability } 1 - p = \frac{\sqrt{5} - 1}{2\sqrt{5}} \approx 0.276393 \end{cases}$$

Alternatively, the **Rademacher Distribution** draws $v_i^* \in \{-1, +1\}$ with equal probability $1/2$, satisfying $\mathbb{E}[v_i^*] = 0$ and $\mathbb{E}[(v_i^*)^2] = 1$ (ideal for symmetric error distributions).

Because $\mathbb{E}[(e_i v_i^*)^2 \mid \mathbf{x}_i] = e_i^2 \mathbb{E}[(v_i^*)^2] = e_i^2$, the Wild Bootstrap preserves the exact conditional variance $\sigma_i^2$ at each distinct observation $\mathbf{x}_i$ while generating a valid stochastic resample, delivering second-order asymptotic accuracy even under severe heteroscedasticity.

### 4. Block Bootstrapping for Dependent Time Series

In time series econometrics ($X_1, X_2, \dots, X_n$), observations are sequentially autocorrelated: $\text{Cov}(X_t, X_{t+k}) \ne 0$. Classical i.i.d. resampling completely destroys the temporal sequence, treating dependent records as independent and producing severely underestimated standard errors.

To preserve temporal dependence, Hans Künsch (1989) introduced the **Moving Block Bootstrap (MBB)**.

#### The Moving Block Bootstrap Protocol:
1. Select a block length $\ell \in \mathbb{N}$ such that $\ell \to \infty$ as $n \to \infty$, but $\ell / n \to 0$ (typically $\ell \propto n^{1/3}$).
2. Form all $n - \ell + 1$ overlapping contiguous temporal blocks of length $\ell$:
   $$\mathcal{B}_j = (X_j, X_{j+1}, \dots, X_{j+\ell-1}), \quad j = 1, \dots, n - \ell + 1$$
3. To construct a bootstrap series of length $n$, draw $k = \lceil n / \ell \rceil$ blocks uniformly at random with replacement from $\{\mathcal{B}_1, \dots, \mathcal{B}_{n-\ell+1}\}$ and concatenate them.
4. Truncate the concatenated series to length $n$.

Because observations *within* each block retain their exact temporal ordering and spacing, the Moving Block Bootstrap captures autocorrelation up to lag $\ell - 1$.

#### The Stationary Bootstrap (Politis and Romano, 1994):
A theoretical drawback of the Moving Block Bootstrap is that the resampled series is not strictly stationary: the covariance between observations spanning a block boundary differs from the covariance within a block.
Dimitris Politis and Joseph Romano resolved this by introducing the **Stationary Bootstrap**, where the block length $L$ is itself a stochastic random variable drawn from a **Geometric Distribution**:
$$\mathbb{P}(L = k) = (1 - p)^{k-1} p, \quad k = 1, 2, \dots$$
with mean block length $\mathbb{E}[L] = 1/p$. The resulting bootstrap resample is proven to be strictly stationary conditional on the observed data.

---

## 6.7 Model Selection, the One-Standard-Error Rule, and Out-of-Bag (OOB) Ensemble Validation

Cross-validation is the central engine for hyperparameter tuning in machine learning and regularized statistics (such as choosing the penalty $\lambda$ in Lasso regression or tuning tree depth in gradient boosting).

### The Bias-Variance Trade-Off in K-Fold Cross-Validation

The choice of the number of folds $K$ in $K$-fold cross-validation involves a delicate balance between computational cost, statistical bias, and estimator variance:
- **$K = 2$ (50/50 Split)**: Each model is trained on only half the data ($N/2$). Because statistical models perform worse on smaller sample sizes, $K = 2$ exhibits **high pessimistic bias**: it systematically overestimates the generalization error of a model trained on the full sample $N$.
- **$K = N$ (Leave-One-Out CV)**: Each model is trained on $N - 1$ observations, virtually eliminating training-size bias. However, the $N$ training sets are nearly identical, sharing $N - 2$ data points. Consequently, the $N$ error estimates are **strongly positively correlated**, which inflates the variance of the overall cross-validation error estimate.
- **Optimal Compromise ($K = 5$ or $K = 10$)**: Empirical research by Breiman and Spector (1992) and Kohavi (1995) demonstrated that $K = 10$ provides minimal mean squared error, maintaining negligible bias while achieving low variance.

### The One-Standard-Error Rule (1-SE Rule)

When plotting cross-validation error against a model complexity parameter (e.g. the regularization penalty $\lambda$ in Lasso or Ridge regression), the empirical CV curve $\text{CV}(\lambda)$ typically displays a shallow, flat valley around the global minimum $\hat{\lambda}_{min}$.

Because $\text{CV}(\lambda)$ is estimated from random folds, the exact location of the minimum $\hat{\lambda}_{min}$ is subject to sampling noise. Selecting $\hat{\lambda}_{min}$ directly often yields an overly complex model that includes spurious, non-informative variables.

To enforce scientific parsimony, Trevor Hastie, Robert Tibshirani, and Jerome Friedman formulated the **One-Standard-Error Rule (1-SE Rule)**:

```text
The One-Standard-Error Rule in Regularization Paths:
  CV Error ^
           |       .---.
           |      /     \               Threshold: CV_min + SE(CV_min)
           | ----+-------+-------------x------------------------
           |    /         \           /
           |   /           '---.     /
           |  /                 '---'  <-- Global Minimum CV_min
       0.0 +-+--------------------+----+-------------------> \lambda
                                \lambda_min  \lambda_{1SE} (More Parsimonious / Simpler)
```

#### Protocol for the 1-SE Rule:
1. Compute the cross-validation error curve across the candidate parameter grid: $\text{CV}(\lambda_1), \dots, \text{CV}(\lambda_M)$.
2. Identify the global minimum:
   $$\text{CV}_{min} = \min_{\lambda} \text{CV}(\lambda) = \text{CV}(\hat{\lambda}_{min})$$
3. Compute the standard error of the cross-validation estimate at the minimum:
   $$\text{SE}(\text{CV}_{min}) = \frac{\text{SD}(\text{Fold Errors})}{\sqrt{K}}$$
4. Select the **most regularized (simplest / most parsimonious) model** whose cross-validation error is within one standard error of the minimum:
   $$\hat{\lambda}_{1SE} = \max \{ \lambda : \text{CV}(\lambda) \le \text{CV}_{min} + \text{SE}(\text{CV}_{min}) \}$$

In Lasso regression, $\hat{\lambda}_{1SE}$ shrinks more coefficients to exactly zero, eliminating false-positive predictors and yielding a more interpretable, robust model that generalizes better to unseen populations.

### Out-of-Bag (OOB) Error Estimation in Bagging and Random Forests

In 1996, Leo Breiman invented **Bootstrap Aggregation (Bagging)** and subsequently **Random Forests** (2001).
Bagging constructs an ensemble of $B$ decision trees $\{T_1, \dots, T_B\}$, where each tree $T_b$ is trained on an independent bootstrap resample $\mathbf{x}^{*b}$ of size $N$ drawn with replacement from the training set.

Recall from Section 6.2 that the probability an observation $i$ is omitted from any given bootstrap sample is:

$$\mathbb{P}(\text{Omitted}) = \left( 1 - \frac{1}{N} \right)^N \approx e^{-1} \approx 36.8\%$$

These unselected observations are termed **Out-of-Bag (OOB) observations** for tree $T_b$.
Across an ensemble of $B = 500$ trees, each observation $i$ is out-of-bag for approximately $0.368 \times 500 \approx 184$ trees!

#### The OOB Prediction and Error Metric:
For each observation $i \in \{1, \dots, N\}$:
1. Identify the sub-ensemble of trees $\mathcal{T}_i^{OOB} = \{ b \in \{1, \dots, B\} : i \notin \mathbf{x}^{*b} \}$ for which observation $i$ was omitted during training.
2. Aggregate predictions only across this out-of-bag sub-ensemble:
   - For regression: $\hat{y}_i^{OOB} = \frac{1}{|\mathcal{T}_i^{OOB}|} \sum_{b \in \mathcal{T}_i^{OOB}} T_b(\mathbf{x}_i)$.
   - For classification: majority vote across $\mathcal{T}_i^{OOB}$.
3. Compute the **Out-of-Bag Mean Squared Error**:

$$\text{MSE}_{OOB} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i^{OOB})^2$$

#### Computational Virtues of OOB Validation:
- Because $\hat{y}_i^{OOB}$ is evaluated exclusively by trees that **never saw observation $i$ during training**, OOB error is an entirely honest, unbiased estimate of out-of-sample generalization error.
- Breiman proved that OOB error is asymptotically equivalent to Leave-One-Out Cross-Validation (LOOCV).
- Crucially, OOB error is computed **in a single training pass** alongside ensemble construction, completely eliminating the need to execute separate $K$-fold cross-validation loops!
"""

marker = "## Fully worked question 1:"
idx = text.find(marker)
new_text = text[:idx] + addition.strip() + "\n\n" + text[idx:]

with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated Unit 6 successfully!")
