# tooling/expand-unit-3.py
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-3.md", "r", encoding="utf-8") as f:
    text = f.read()

addition = r"""

---

## 3.6 Non-Parametric Surface Smoothing, Spline Bases, and High-Dimensional Model Interpretability Visualizations

In modern data analysis, exploring non-linear bivariate and multivariate functional relationships between variables without imposing rigid parametric forms (such as straight lines or quadratic polynomials) is a central task. Statistical graphics engines integrate continuous non-parametric smoothers directly into their layered geometries (e.g. `geom_smooth(method = "loess")` or `geom_smooth(method = "gam")`). Understanding the underlying computational mechanics of local regression, penalized smoothing splines, and high-dimensional model interpretability plots is essential for sound exploratory visualization.

### Locally Estimated Scatterplot Smoothing (LOESS / LOWESS)

Developed by William S. Cleveland in 1979 and expanded with Susan Devlin in 1988, **LOESS (Locally Estimated Scatterplot Smoothing)** is a non-parametric method that fits localized low-degree polynomials across moving neighborhoods of the data.

#### Algorithmic Execution Protocol:
Let $(x_1, y_1), \dots, (x_n, y_n)$ denote $n$ bivariate observations. To estimate the smoothed curve $\hat{g}(x)$ at any focal evaluation point $x$:

1. **Neighborhood Delineation via Span ($\alpha$)**:
   The analyst selects a smoothing parameter or **span** $\alpha \in (0, 1)$, defining the proportion of total data points included in each local neighborhood:
   $$k = \lfloor \alpha \cdot n \rfloor$$
   The algorithm finds the $k$ nearest neighbors to $x$ based on Euclidean distance $|x_i - x|$. Let $\Delta(x)$ denote the distance to the $k$-th furthest neighbor:
   $$\Delta(x) = \max_{i \in \mathcal{N}_k(x)} |x_i - x|$$

2. **Tricube Weight Allocation**:
   Each neighbor $x_i \in \mathcal{N}_k(x)$ is assigned a neighborhood weight via the **Tricube Kernel**:
   $$w_i(x) = W\left( \frac{|x_i - x|}{\Delta(x)} \right)$$
   where the tricube function $W(u)$ is defined as:
   $$W(u) = (1 - |u|^3)^3 \cdot \mathbb{I}(0 \le |u| < 1)$$
   The tricube weight smoothly decays to zero at the boundary of the neighborhood, ensuring that observations near the center of the local window receive maximum weight while distant points exert negligible influence.

3. **Weighted Polynomial Fitting**:
   A polynomial of degree $d$ (typically linear $d = 1$ or quadratic $d = 2$) is fitted locally by solving the weighted least squares objective:
   $$\min_{\boldsymbol{\beta}} \sum_{i \in \mathcal{N}_k(x)} w_i(x) \left( y_i - \sum_{j=0}^d \beta_j (x_i - x)^j \right)^2$$
   The smoothed fitted value at point $x$ is simply the evaluated constant term:
   $$\hat{g}(x) = \hat{\beta}_0$$

4. **Robustness Iterations via Bisquare Weighting**:
   To prevent severe outliers from distorting the smoothed trend line, Cleveland introduced iterative **robustness reweighting**:
   - Compute initial residuals: $e_i = y_i - \hat{g}(x_i)$.
   - Compute the median absolute deviation (MAD) of the residuals:
     $$s = \text{median}(|e_i|)$$
   - Assign robustness weights $r_i$ using the **Tukey Bisquare Weight Function**:
     $$r_i = B\left( \frac{e_i}{6 s} \right)$$
     where $B(u) = (1 - u^2)^2 \cdot \mathbb{I}(|u| < 1)$.
   - Refit the local regressions using combined weights $\tilde{w}_i(x) = w_i(x) \cdot r_i$. Typically, 2 to 3 robustness iterations suffice to completely insulate the smoothed curve against extreme anomalies.

### Penalized B-Splines and Generalized Additive Models (GAMs)

While LOESS works effectively for 1D smoothing with moderate sample sizes, its computational complexity scales quadratically with sample size $\mathcal{O}(n^2)$ when evaluated across many points, and it suffers from the curse of dimensionality when extended to higher-dimensional surfaces.

For large datasets and multivariate smoothing, modern statistical systems deploy **Penalized Smoothing Splines** within Trevor Hastie and Robert Tibshirani's **Generalized Additive Models (GAM)** framework (implemented in Simon Wood's `mgcv` package in R and `pygam` / `statsmodels` in Python).

#### The Penalized Likelihood Objective:
A smooth univariate function $f(x)$ is represented as a linear combination of $K$ fixed basis functions $b_k(x)$ (typically cubic B-splines or thin plate regression splines):

$$f(x) = \sum_{k=1}^K \beta_k b_k(x) = \mathbf{b}(x)^\top \boldsymbol{\beta}$$

To prevent overfitting when $K$ is large, the optimization penalizes excessive curvature (roughness) via a regularization parameter $\lambda$:

$$\mathcal{L}_{pen}(\boldsymbol{\beta}) = \sum_{i=1}^n (y_i - f(x_i))^2 + \lambda \int [f''(x)]^2 \, dx$$

In matrix notation:
$$\mathcal{L}_{pen}(\boldsymbol{\beta}) = \|\mathbf{y} - \mathbf{B} \boldsymbol{\beta}\|_2^2 + \lambda \boldsymbol{\beta}^\top \mathbf{S} \boldsymbol{\beta}$$
where $\mathbf{B}_{n \times K}$ is the basis evaluation matrix ($B_{ik} = b_k(x_i)$) and $\mathbf{S}_{K \times K}$ is the known symmetric roughness penalty matrix with entries:
$$S_{jk} = \int b_j''(x) b_k''(x) \, dx$$

Setting the gradient to zero yields the exact penalized ridge-type solution:
$$\hat{\boldsymbol{\beta}} = (\mathbf{B}^\top \mathbf{B} + \lambda \mathbf{S})^{-1} \mathbf{B}^\top \mathbf{y}$$

#### Automatic Smoothing Parameter Selection via GCV:
The smoothing parameter $\lambda$ controls the trade-off between fidelity to the data and smoothness:
- As $\lambda \to 0$, $f(x)$ interpolates the data (wiggly, high variance).
- As $\lambda \to \infty$, the penalty dominates, forcing $f''(x) = 0$ everywhere, collapsing the smoother to a simple linear OLS fit.

The optimal $\lambda$ is chosen automatically by minimizing the **Generalized Cross-Validation (GCV)** criterion:

$$\text{GCV}(\lambda) = \frac{n \|\mathbf{y} - \hat{\mathbf{y}}\|_2^2}{(n - \text{tr}(\mathbf{A}_\lambda))^2}$$

where $\mathbf{A}_\lambda = \mathbf{B} (\mathbf{B}^\top \mathbf{B} + \lambda \mathbf{S})^{-1} \mathbf{B}^\top$ is the influence (hat) matrix, and $\text{tr}(\mathbf{A}_\lambda)$ represents the **effective degrees of freedom (EDF)** of the smooth term.

### Visualizing High-Dimensional Models: PDP, ICE, and ALE Plots

In high-dimensional machine learning and complex statistical models (random forests, gradient boosting, neural networks, generalized additive models), understanding how individual features influence the predicted outcome is obscured by the "black-box" nature of the predictive function $\hat{f}(\mathbf{x})$. To diagnose and interpret these models visually, statisticians use three foundational diagnostic visualizations:

#### 1. Partial Dependence Plots (PDP)
Introduced by Jerome Friedman (2001), the Partial Dependence Plot depicts the average marginal effect of a chosen subset of features $X_S$ (typically one or two variables) on the predicted response $\hat{f}(\mathbf{x})$, averaging out the effects of all other complementary features $X_C$:

$$\hat{f}_S(x_S) = \mathbb{E}_{X_C}[\hat{f}(x_S, X_C)] \approx \frac{1}{n} \sum_{i=1}^n \hat{f}(x_S, x_{i, C})$$

- **Limitation**: PDP assumes feature independence. If $X_S$ and $X_C$ are heavily correlated in the real world (e.g., engine displacement and vehicle weight), the PDP averages predictions over impossible synthetic data points (e.g., a 6.0-liter engine in a 900 kg subcompact car), creating misleading visual artifacts.

#### 2. Individual Conditional Expectation (ICE) Plots
Developed by Alex Goldstein and colleagues (2015), ICE plots disaggregate the average PDP curve. For each individual observation $i$ in the dataset, the algorithm plots a separate curve:
$$x_S \mapsto \hat{f}(x_S, x_{i, C})$$
By rendering $n$ individual lines on a single plot, ICE curves immediately reveal **heterogeneous treatment effects and interaction effects** that are completely invisible in the average PDP. If some lines slope upward while others slope downward, a strong interaction with a feature in $X_C$ is visually unmasked.

#### 3. Accumulated Local Effects (ALE) Plots
To resolve the feature correlation bias of PDPs without requiring heavy computational sampling, Daniel Apley and Jingyu Zhu (2020) formulated **Accumulated Local Effects (ALE)** plots.

Instead of marginalizing over the entire marginal distribution of $X_C$, ALE computes differences in predictions within **localized conditional windows** of $X_S$:

$$f_{ALE}(x_S) = \int_{z_0}^{x_S} \mathbb{E}_{X_C \mid X_S = z} \left[ \frac{\partial \hat{f}(z, X_C)}{\partial z} \right] dz$$

In practice, the variable $X_S$ is partitioned into $K$ intervals $[z_{k-1}, z_k]$. The uncentered ALE estimate accumulates the average finite differences of observations falling strictly inside each interval:

$$\hat{f}_{ALE}(x) = \sum_{k=1}^{k(x)} \frac{1}{|\mathcal{S}_k|} \sum_{i \in \mathcal{S}_k} \left[ \hat{f}(z_k, x_{i, C}) - \hat{f}(z_{k-1}, x_{i, C}) \right]$$

Because ALE only evaluates predictions at realistic, observed combinations of $(x_S, x_C)$, it is completely robust against feature collinearity and runs significantly faster than PDP, representing the modern gold standard for diagnostic interpretability graphics.
"""

marker = "## Fully worked question 1:"
idx = text.find(marker)
new_text = text[:idx] + addition.strip() + "\n\n" + text[idx:]

with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-3.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated Unit 3 successfully!")
