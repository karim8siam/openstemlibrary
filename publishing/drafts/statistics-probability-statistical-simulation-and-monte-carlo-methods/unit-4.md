# Unit 4: Monte Carlo Integration & Precision

In scientific computing, quantitative finance, and high-dimensional Bayesian inference, researchers frequently encounter definite integrals that cannot be evaluated analytically:
$$\theta = \int_{\mathcal{D}} g(\mathbf{x})\,d\mathbf{x}$$
where $\mathcal{D} \subseteq \mathbb{R}^d$ is a multidimensional integration domain. When the dimension $d$ exceeds 3 or 4, classical deterministic numerical quadrature rules (such as the Trapezoidal rule, Simpson's rule, and Gauss-Legendre quadrature) suffer an exponential computational collapse known as the **Curse of Dimensionality**.

**Monte Carlo Integration**, conceived by Stanislaw Ulam, John von Neumann, and Nicholas Metropolis during the Manhattan Project at Los Alamos in the late 1940s, circumvents the curse of dimensionality by reformulating deterministic integration problems as stochastic expectations.

## 4.1 Foundations of Crude Monte Carlo Integration

Let $\theta$ denote the integral of a real-valued function $h(\mathbf{x})$ over a domain $\mathcal{D}$ with respect to a continuous probability density function $f(\mathbf{x})$:

$$\theta = \mathbb{E}_f[h(\mathbf{X})] = \int_{\mathcal{D}} h(\mathbf{x}) f(\mathbf{x})\,d\mathbf{x}$$

If the original integral is an unweighted Lebesgue integral over a bounded hypercube $\mathcal{D} = [a_1, b_1] \times \dots \times [a_d, b_d]$ with total hypervolume $V = \prod_{j=1}^d (b_j - a_j)$:
$$I = \int_{\mathcal{D}} g(\mathbf{x})\,d\mathbf{x} = V \int_{\mathcal{D}} g(\mathbf{x}) \left( \frac{1}{V} \right) d\mathbf{x} = V \cdot \mathbb{E}[g(\mathbf{U})]$$
where $\mathbf{U} \sim \mathcal{U}(\mathcal{D})$ is uniformly distributed across the domain.

### 1. The Monte Carlo Estimator
Let $\mathbf{X}_1, \mathbf{X}_2, \dots, \mathbf{X}_n$ be an independent and identically distributed (i.i.d.) random sample drawn from density $f(\mathbf{x})$. The **Crude Monte Carlo Estimator** of $\theta$ is the sample mean of the evaluated function values:

$$\hat{\theta}_n = \frac{1}{n} \sum_{i=1}^n h(\mathbf{X}_i)$$

### 2. Theoretical Statistical Properties
1. **Unbiasedness**:
   $$\mathbb{E}[\hat{\theta}_n] = \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^n h(\mathbf{X}_i) \right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[h(\mathbf{X}_i)] = \frac{1}{n} (n \theta) = \theta$$
   The estimator is strictly unbiased for any finite sample size $n \ge 1$.
2. **Strong Consistency (Convergence Almost Surely)**:
   Assuming the function is absolutely integrable ($\mathbb{E}[|h(\mathbf{X})|] < \infty$), by the **Kolmogorov Strong Law of Large Numbers**:
   $$P\left( \lim_{n \to \infty} \hat{\theta}_n = \theta \right) = 1$$
3. **Finite-Sample Variance**:
   Assuming square integrability ($\sigma^2 = \mathrm{Var}_f(h(\mathbf{X})) = \int (h(\mathbf{x}) - \theta)^2 f(\mathbf{x})\,dx < \infty$):
   $$\mathrm{Var}(\hat{\theta}_n) = \mathrm{Var}\left( \frac{1}{n} \sum_{i=1}^n h(\mathbf{X}_i) \right) = \frac{1}{n^2} \sum_{i=1}^n \mathrm{Var}(h(\mathbf{X}_i)) = \frac{\sigma^2}{n}$$
   The standard error of the Monte Carlo estimator decays at the universal rate:
   $$\text{SE}(\hat{\theta}_n) = \frac{\sigma}{\sqrt{n}} = \mathcal{O}\left( \frac{1}{\sqrt{n}} \right)$$

## 4.2 Asymptotic Error Distribution and Confidence Intervals

By the **Lindeberg-Lévy Central Limit Theorem**, as the simulation sample size $n \to \infty$, the standardized estimation error converges in distribution to the standard Gaussian distribution:

$$\frac{\hat{\theta}_n - \theta}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

In practice, the true population variance $\sigma^2$ is unknown and must be estimated consistently from the simulated trajectory using the sample variance:

$$S_n^2 = \frac{1}{n - 1} \sum_{i=1}^n \left( h(\mathbf{X}_i) - \hat{\theta}_n \right)^2 = \frac{1}{n - 1} \left( \sum_{i=1}^n h(\mathbf{X}_i)^2 - n \hat{\theta}_n^2 \right)$$

By Slutsky's theorem:

$$\frac{\hat{\theta}_n - \theta}{S_n / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

### Asymptotic Confidence Intervals
An asymptotic $(1 - \alpha) \times 100\%$ confidence interval for the true integral $\theta$ is:

$$\mathcal{CI}_{1-\alpha} = \left[ \hat{\theta}_n - z_{1 - \alpha/2} \frac{S_n}{\sqrt{n}}, \; \hat{\theta}_n + z_{1 - \alpha/2} \frac{S_n}{\sqrt{n}} \right]$$

where $z_{1 - \alpha/2} = \Phi^{-1}(1 - \alpha/2)$ is the upper standard normal critical quantile (e.g., $z_{0.975} \approx 1.960$ for a $95\%$ confidence interval).

## 4.3 Deterministic Quadrature vs Monte Carlo: The Curse of Dimensionality

To appreciate why Monte Carlo integration is irreplaceable in modern science, consider the mathematical convergence rates of classical deterministic numerical integration algorithms in $d$-dimensional space.

### 1. Deterministic Numerical Quadrature Error Rates
To evaluate an integral over the unit hypercube $[0, 1]^d$ using a grid-based quadrature rule:
- Let $k$ denote the number of grid subdivisions along each individual coordinate axis.
- The total number of evaluation nodes across the hypercube is:
  $$n = k^d \implies k = n^{1/d}$$

For standard classical quadrature rules:
1. **Riemann Sum / Midpoint Rule**: The error scales as $\mathcal{O}(1 / k) = \mathcal{O}(n^{-1/d})$.
2. **Trapezoidal Rule**: For twice-differentiable integrands, the error scales as $\mathcal{O}(1 / k^2) = \mathcal{O}(n^{-2/d})$.
3. **Simpson's Rule**: For four-times differentiable integrands, the error scales as $\mathcal{O}(1 / k^4) = \mathcal{O}(n^{-4/d})$.

### 2. The Dimensionality Transition Point
Notice the critical mathematical contrast:
- **Deterministic Quadrature**: Error $= \mathcal{O}(n^{-r / d})$, where $r$ is the algebraic order of the quadrature method. The convergence rate **degrades exponentially as dimension $d$ grows**!
- **Monte Carlo Integration**: Error $= \mathcal{O}(n^{-1/2})$, completely **independent of the dimension $d$**!

We equate the convergence exponents:
$$\frac{r}{d} = \frac{1}{2} \implies d = 2r$$
- For the Trapezoidal rule ($r = 2$):
  - In $d = 1$: Quadrature achieves $\mathcal{O}(n^{-2})$, far faster than Monte Carlo $\mathcal{O}(n^{-1/2})$.
  - In $d = 4$: Quadrature achieves $\mathcal{O}(n^{-2/4}) = \mathcal{O}(n^{-1/2})$, breaking even with Monte Carlo.
  - In $d = 10$: Quadrature achieves $\mathcal{O}(n^{-0.20})$, while Monte Carlo maintains $\mathcal{O}(n^{-0.50})$.
  - In $d = 100$: Quadrature achieves $\mathcal{O}(n^{-0.02})$, requiring $10^{100}$ evaluations for two digits of precision, whereas Monte Carlo requires $10^4$ evaluations for the exact same accuracy!

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Dimension ($d$)</th>
<th>Midpoint Rule ($r=1$)</th>
<th>Trapezoidal Rule ($r=2$)</th>
<th>Simpson's Rule ($r=4$)</th>
<th>Monte Carlo (Any $d$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>$d = 1$</td>
<td>$\mathcal{O}(n^{-1.0})$</td>
<td>$\mathcal{O}(n^{-2.0})$</td>
<td>$\mathcal{O}(n^{-4.0})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d = 2$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
<td>$\mathcal{O}(n^{-1.0})$</td>
<td>$\mathcal{O}(n^{-2.0})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d = 4$</td>
<td>$\mathcal{O}(n^{-0.25})$</td>
<td>$\mathcal{O}(n^{-0.50})$</td>
<td>$\mathcal{O}(n^{-1.0})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d = 8$</td>
<td>$\mathcal{O}(n^{-0.125})$</td>
<td>$\mathcal{O}(n^{-0.25})$</td>
<td>$\mathcal{O}(n^{-0.50})$</td>
<td>$\mathcal{O}(n^{-0.5})$</td>
</tr>
<tr>
<td>$d \ge 10$</td>
<td>Hopeless ($\mathcal{O}(n^{-0.10})$)</td>
<td>Hopeless ($\mathcal{O}(n^{-0.20})$)</td>
<td>Slow ($\mathcal{O}(n^{-0.40})$)</td>
<td><strong>Robust: $\mathcal{O}(n^{-0.5})$</strong></td>
</tr>
</tbody>
</table>
</div>

Monte Carlo integration is the only computationally tractable method for multidimensional problems when $d \ge 8$.

## 4.4 Sample Size Determination and Computational Budgeting

A central question in experimental simulation design is: **how many Monte Carlo samples $n$ must be drawn to guarantee that the estimate $\hat{\theta}_n$ lies within a prescribed margin of error $\epsilon$ with high probability?**

### 1. Absolute Error Bound
Let the researcher demand that the absolute error does not exceed $\epsilon > 0$ with confidence $1 - \alpha$:
$$P(|\hat{\theta}_n - \theta| \le \epsilon) \ge 1 - \alpha$$
Under the asymptotic normal approximation:
$$z_{1 - \alpha/2} \frac{\sigma}{\sqrt{n}} \le \epsilon \implies \sqrt{n} \ge \frac{z_{1 - \alpha/2} \sigma}{\epsilon}$$
Squaring both sides yields the minimum sample size:

$$n \ge \left( \frac{z_{1 - \alpha/2} \cdot \sigma}{\epsilon} \right)^2$$

*Key Observation*: To gain one additional decimal digit of precision (reducing $\epsilon$ by a factor of 10), the required sample size $n$ must increase by a factor of **100** ($10^2$).

### 2. Relative Error Bound
When the magnitude of $\theta$ is unknown or very small (e.g., simulating rare failure events in structural safety where $\theta = 10^{-6}$), an absolute error bound is meaningless. The researcher specifies a **relative precision error** $\epsilon_r \in (0, 1)$:
$$P\left( \left| \frac{\hat{\theta}_n - \theta}{\theta} \right| \le \epsilon_r \right) \ge 1 - \alpha$$
The relative standard error requirement is:
$$z_{1 - \alpha/2} \frac{\sigma / \sqrt{n}}{\theta} \le \epsilon_r \implies n \ge \left( \frac{z_{1 - \alpha/2}}{\epsilon_r} \right)^2 \left( \frac{\sigma}{\theta} \right)^2$$
The ratio $CV = \sigma / \theta$ is the **Coefficient of Variation** of the summand $h(\mathbf{X})$.

For a rare-event probability $\theta = P(X \in \mathcal{E})$ estimated via indicator variables $h(\mathbf{X}) = I(\mathbf{X} \in \mathcal{E})$:
$$\sigma^2 = \theta(1 - \theta) \approx \theta \quad \text{for small } \theta$$
$$\left( \frac{\sigma}{\theta} \right)^2 = \frac{\theta(1 - \theta)}{\theta^2} = \frac{1 - \theta}{\theta} \approx \frac{1}{\theta}$$
The required sample size is:
$$n \ge \left( \frac{z_{1 - \alpha/2}}{\epsilon_r} \right)^2 \frac{1}{\theta}$$
If $\theta = 10^{-5}$ and the researcher desires a $10\%$ relative error ($\epsilon_r = 0.10$) at $95\%$ confidence ($z \approx 1.96$):
$$n \ge \left( \frac{1.96}{0.10} \right)^2 \times 10^5 \approx 384.16 \times 10^5 \approx 38.4 \text{ million simulations!}$$
Crude Monte Carlo becomes computationally inefficient for rare-event estimation, necessitating advanced variance reduction techniques (such as Importance Sampling).

## Fully worked question 1: Monte Carlo Integration of a Gaussian Tail Probability

### Question
An environmental safety regulator must compute the extreme upper-tail probability:
$$\theta = P(Z > 3.0) = \frac{1}{\sqrt{2\pi}} \int_3^\infty e^{-x^2/2}\,dx$$
for a standard Gaussian pollutant concentration index $Z \sim \mathcal{N}(0, 1)$.
1. Formulate a Crude Monte Carlo estimator $\hat{\theta}_n$ based on $n$ independent standard normal draws $Z_1, \dots, Z_n$.
2. In a preliminary simulation of $n = 10,000$ draws, exactly 14 draws exceed 3.0.
   - Compute the point estimate $\hat{\theta}$.
   - Compute the sample standard error $\text{SE}(\hat{\theta})$.
   - Construct the asymptotic $95\%$ confidence interval for $\theta$.
3. Compute the required sample size $n^*$ to achieve a relative error of $\epsilon_r = 0.05$ ($5\%$) at $95\%$ confidence.

### Solution, step 1: Formulation of the Crude Monte Carlo Estimator
The target probability is an expectation:
$$\theta = \mathbb{E}[I(Z > 3.0)]$$
where $I(A)$ is the indicator function of event $A$.
The Crude Monte Carlo estimator is the empirical proportion of draws exceeding 3.0:
$$\hat{\theta}_n = \frac{1}{n} \sum_{i=1}^n I(Z_i > 3.0)$$
Since $I(Z_i > 3.0)$ is a Bernoulli random variable with parameter $\theta$:
$$\mathbb{E}[\hat{\theta}_n] = \theta, \quad \mathrm{Var}(\hat{\theta}_n) = \frac{\theta(1 - \theta)}{n}$$

### Solution, step 2: Numerical Point Estimate, Standard Error, and 95% CI
Given $n = 10,000$ and $\sum I(Z_i > 3.0) = 14$:
1. **Point Estimate**:
   $$\hat{\theta} = \frac{14}{10,000} = 0.00140 \quad (1.40 \times 10^{-3})$$
   (The exact theoretical value from standard normal tables is $1 - \Phi(3.0) \approx 0.0013499$).

2. **Sample Standard Error**:
   $$\hat{\sigma}^2 = \hat{\theta}(1 - \hat{\theta}) = 0.00140 \times (1 - 0.00140) = 0.00140 \times 0.99860 \approx 0.00139804$$
   $$\text{SE}(\hat{\theta}) = \sqrt{\frac{\hat{\sigma}^2}{n}} = \sqrt{\frac{0.00139804}{10,000}} = \sqrt{1.39804 \times 10^{-7}} \approx 0.0003739 \approx 3.74 \times 10^{-4}$$

3. **Asymptotic 95% Confidence Interval**:
   Using $z_{0.975} = 1.960$:
   $$\text{Margin of Error} = 1.960 \times \text{SE}(\hat{\theta}) = 1.960 \times 0.0003739 \approx 0.0007328$$
   $$\mathcal{CI}_{0.95} = [0.00140 - 0.000733, \; 0.00140 + 0.000733] = [0.000667, \; 0.002133]$$
   Notice the wide uncertainty relative to the estimate: the margin of error is more than $50\%$ of the point estimate!

### Solution, step 3: Sample Size Determination for 5% Relative Error
We require:
$$\frac{z_{0.975} \cdot \text{SE}}{\theta} \le 0.05 \implies n^* \ge \left( \frac{1.960}{0.05} \right)^2 \left( \frac{1 - \theta}{\theta} \right)$$
Using the estimate $\hat{\theta} = 0.00135$:
$$\frac{1.960}{0.05} = 39.2 \implies 39.2^2 = 1,536.64$$
$$\frac{1 - \theta}{\theta} \approx \frac{1 - 0.00135}{0.00135} = \frac{0.99865}{0.00135} \approx 739.74$$
Multiplying:
$$n^* \ge 1,536.64 \times 739.74 \approx 1,136,714$$
*Conclusion*: Achieving $5\%$ relative precision on this tail probability requires over **1.14 million** independent Monte Carlo simulation draws.

## Fully worked question 2: Multidimensional Monte Carlo Volume Estimation

### Question
A mathematical physicist calculates the hypervolume $V_{10}$ of a 10-dimensional unit hypersphere:
$$S_{10} = \left\{ \mathbf{x} = (x_1, \dots, x_{10})^T \in \mathbb{R}^{10} : \sum_{j=1}^{10} x_j^2 \le 1 \right\}$$
The hypersphere is embedded inside the 10-dimensional hypercube $\mathcal{C}_{10} = [-1, 1]^{10}$ with volume $V_{\text{cube}} = 2^{10} = 1,024$.
1. In a Monte Carlo experiment, $n = 100,000$ points are drawn uniformly at random from $\mathcal{C}_{10}$. Exactly 249 points fall inside the hypersphere ($\sum x_j^2 \le 1$).
   - Estimate the hypervolume $\hat{V}_{10}$.
   - Compute the standard error of the hypervolume estimate.
   - Construct the $95\%$ confidence interval.
2. The exact analytical hypervolume of a $d$-dimensional sphere of radius $R = 1$ is:
   $$V_d = \frac{\pi^{d/2}}{\Gamma(d/2 + 1)}$$
   Compute the exact analytical value for $d = 10$ and evaluate the estimation error.

### Solution, step 1: Monte Carlo Volume Estimation and Standard Error
Let $\mathbf{U}_i \sim \mathcal{U}([-1, 1]^{10})$ be uniformly distributed on the hypercube of volume $V_{\text{cube}} = 1,024$.
The indicator function is:
$$I_i = I\left( \sum_{j=1}^{10} U_{ij}^2 \le 1 \right)$$
The proportion of points falling inside the hypersphere is:
$$\hat{p} = \frac{\sum_{i=1}^n I_i}{n} = \frac{249}{100,000} = 0.00249$$

1. **Volume Estimate**:
   $$\hat{V}_{10} = V_{\text{cube}} \cdot \hat{p} = 1,024 \times 0.00249 = 2.54976 \approx 2.550$$

2. **Standard Error of $\hat{V}_{10}$**:
   The variance of $\hat{p}$ is $\frac{p(1 - p)}{n}$:
   $$\mathrm{Var}(\hat{p}) = \frac{0.00249 \times (1 - 0.00249)}{100,000} = \frac{0.00249 \times 0.99751}{100,000} \approx 2.4838 \times 10^{-8}$$
   $$\text{SE}(\hat{p}) = \sqrt{2.4838 \times 10^{-8}} \approx 0.0001576$$
   The standard error of the volume estimate is:
   $$\text{SE}(\hat{V}_{10}) = V_{\text{cube}} \cdot \text{SE}(\hat{p}) = 1,024 \times 0.0001576 \approx 0.16138 \approx 0.161$$

3. **95% Confidence Interval for $\hat{V}_{10}$**:
   $$\text{Margin of Error} = 1.960 \times 0.16138 \approx 0.3163$$
   $$\mathcal{CI}_{0.95} = [2.5498 - 0.3163, \; 2.5498 + 0.3163] = [2.2335, \; 2.8661]$$

### Solution, step 2: Exact Analytical Volume Comparison
For $d = 10$:
- $d / 2 = 5$.
- $\Gamma(d/2 + 1) = \Gamma(6) = 5! = 120$.
- $\pi^{d/2} = \pi^5 \approx 3.14159265^5 \approx 306.01968$.

The exact theoretical hypervolume is:
$$V_{10} = \frac{\pi^5}{5!} = \frac{306.01968}{120} \approx 2.550164$$

Comparing the Monte Carlo estimate with the analytical truth:
$$\text{Estimate} = 2.54976, \quad \text{True} = 2.55016$$
$$\text{Absolute Error} = |2.54976 - 2.55016| = 0.00040$$
$$\text{Relative Error} = \frac{0.00040}{2.55016} \approx 0.016\%$$
The exact volume lies comfortably within the $95\%$ confidence interval $[2.2335, 2.8661]$, confirming the precision of the multidimensional Monte Carlo approach.

## Fully worked question 3: Evaluating Integrals with Singularities via Variable Transformation

### Question
An econometrician models continuous income polarization by evaluating the definite integral:
$$\theta = \int_0^1 \frac{e^x}{\sqrt{x}}\,dx$$
1. Explain why direct crude Monte Carlo sampling using $U \sim \mathcal{U}(0, 1)$ encounters severe variance inflation at the lower boundary $x \to 0^+$.
2. Apply the change-of-variable transformation $x = y^2$ to eliminate the algebraic singularity.
3. Formulate the transformed Monte Carlo estimator and prove that its variance is strictly finite and substantially smaller than the untransformed estimator.

### Solution, step 1: Analysis of the Singularity in the Untransformed Estimator
Under direct crude Monte Carlo, let $U \sim \mathcal{U}(0, 1)$:
$$h(u) = \frac{e^u}{\sqrt{u}}$$
The estimator is $\hat{\theta}_n = \frac{1}{n} \sum_{i=1}^n \frac{e^{U_i}}{\sqrt{U_i}}$.
We examine the second moment of the integrand:
$$\mathbb{E}[h(U)^2] = \int_0^1 \left( \frac{e^u}{\sqrt{u}} \right)^2 du = \int_0^1 \frac{e^{2u}}{u}\,du$$
Since $e^{2u} \ge 1$ for all $u \ge 0$:
$$\int_0^1 \frac{e^{2u}}{u}\,du \ge \int_0^1 \frac{1}{u}\,du = [\ln u]_0^1 = 0 - (-\infty) = \infty$$
The second moment is **infinite** ($\mathbb{E}[h(U)^2] = \infty$), which implies that:
$$\mathrm{Var}(h(U)) = \infty$$
Because the variance is infinite, the Central Limit Theorem fails completely! The estimator converges at a rate far slower than $\mathcal{O}(n^{-1/2})$, producing extreme outliers whenever a draw falls close to 0.

### Solution, step 2: The Variable Transformation $x = y^2$
Let $x = y^2 \implies dx = 2y\,dy$.
When $x = 0$, $y = 0$; when $x = 1$, $y = 1$.
Substitute into the integral:
$$\theta = \int_0^1 \frac{e^x}{\sqrt{x}}\,dx = \int_0^1 \frac{e^{y^2}}{\sqrt{y^2}} (2y\,dy) = \int_0^1 \frac{e^{y^2}}{y} (2y)\,dy = 2 \int_0^1 e^{y^2}\,dy$$
The term $y$ in the numerator and denominator cancels out completely, eliminating the algebraic singularity!

### Solution, step 3: Transformed Monte Carlo Estimator and Variance Bounding
Let $Y \sim \mathcal{U}(0, 1)$. The transformed Monte Carlo estimator is:
$$\hat{\theta}_n^* = \frac{1}{n} \sum_{i=1}^n 2 e^{Y_i^2}$$
where $Y_i \sim \mathcal{U}(0, 1)$ i.i.d.
We evaluate the boundedness of the transformed integrand $g(y) = 2 e^{y^2}$ on $[0, 1]$:
- At $y = 0$: $g(0) = 2 e^0 = 2$.
- At $y = 1$: $g(1) = 2 e^1 = 2e \approx 5.4366$.
Because $g(y)$ is strictly bounded on $[0, 1]$ ($2 \le g(y) \le 2e$):
$$\mathrm{Var}(g(Y)) = \int_0^1 (2 e^{y^2})^2 dy - \theta^2 = 4 \int_0^1 e^{2y^2} dy - \theta^2 < 4 e^2 - \theta^2 < \infty$$
By the bounded range property, the variance cannot exceed:
$$\mathrm{Var}(g(Y)) \le \frac{(2e - 2)^2}{4} = (e - 1)^2 \approx (1.718)^2 \approx 2.95$$
The transformed estimator has finite, well-behaved variance and satisfies the Central Limit Theorem with standard $\mathcal{O}(n^{-1/2})$ convergence, transforming an intractable numerical problem into a stable simulation.


## 4.9 Quasi-Monte Carlo Integration and Low-Discrepancy Sequences

While Crude Monte Carlo integration achieves an asymptotic standard error of $O(n^{-1/2})$ regardless of dimension $d$, this convergence rate is agonizingly slow: achieving four decimal places of accuracy requires $n \approx 10^8$ sample draws. 

**Quasi-Monte Carlo (QMC)** replaces pseudo-random independent draws with deterministic, highly uniform points known as **Low-Discrepancy Sequences**. By deliberately preventing points from clustering or leaving empty voids in the unit hypercube $[0, 1]^d$, QMC achieves an asymptotic convergence rate approaching:

$$O\left( \frac{(\log n)^d}{n} \right)$$

For moderate dimensions $d$, this represents an almost linear convergence rate $O(n^{-1})$, vastly outperforming pseudo-random Monte Carlo.

### 1. Discrepancy and the Koksma-Hlawka Inequality
Let $P_n = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ be a deterministic point set in the unit hypercube $I^d = [0, 1]^d$. For any sub-box anchored at the origin $[\mathbf{0}, \mathbf{y}) = \prod_{j=1}^d [0, y_j)$, the empirical count of points falling in the box is:

$$A([\mathbf{0}, \mathbf{y}); P_n) = \sum_{i=1}^n \mathbb{I}(\mathbf{x}_i \in [\mathbf{0}, \mathbf{y}))$$

The local discrepancy function measures the deviation between the empirical fraction of points and the theoretical volume $\lambda([\mathbf{0}, \mathbf{y})) = \prod_{j=1}^d y_j$:

$$R(\mathbf{y}; P_n) = \frac{A([\mathbf{0}, \mathbf{y}); P_n)}{n} - \prod_{j=1}^d y_j$$

The **Star Discrepancy** $D_n^*(P_n)$ is the supremum norm of this deviation over all origin-anchored boxes:

$$D_n^*(P_n) = \sup_{\mathbf{y} \in [0, 1]^d} |R(\mathbf{y}; P_n)|$$

*Theorem (The Koksma-Hlawka Inequality)*: If $f: [0, 1]^d \to \mathbb{R}$ has bounded variation in the sense of Hardy and Krause, denoted $V_{\text{HK}}(f) < \infty$, then the deterministic integration error is bounded by:

$$\left| \frac{1}{n} \sum_{i=1}^n f(\mathbf{x}_i) - \int_{[0, 1]^d} f(\mathbf{x})\,d\mathbf{x} \right| \le V_{\text{HK}}(f) \cdot D_n^*(P_n)$$

This fundamental theorem separates the integration error into two independent components:
1. $V_{\text{HK}}(f)$: depends purely on the smoothness and regularity of the integrand $f$.
2. $D_n^*(P_n)$: depends purely on the geometric uniformity of the point set $P_n$.

### 2. Constructions of Low-Discrepancy Sequences
A sequence $\{\mathbf{x}_n\}$ is called a low-discrepancy sequence if its first $n$ elements satisfy $D_n^*(P_n) \le C_d \frac{(\log n)^d}{n}$ for all $n$. Three major families dominate computational practice:

1. **Halton Sequences**: Generalize the 1D van der Corput sequence to $d$ dimensions. Let $p_1, \dots, p_d$ be the first $d$ prime numbers. The $i$-th point is:
$$\mathbf{x}_i = (\phi_{p_1}(i), \phi_{p_2}(i), \dots, \phi_{p_d}(i))$$
where $\phi_p(i) = \sum_{k=0}^M a_k(i) p^{-(k+1)}$ is the radical inverse function expanding integer $i = \sum_{k=0}^M a_k(i) p^k$ in base $p$.
2. **Sobol' Sequences**: Constructed in base 2 using primitive polynomials over the Galois field $\mathbb{F}_2$. A set of direction integers $v_j$ defines the bitwise XOR transformations generating coordinates. Sobol' sequences satisfy the $(t, s)$-sequence criteria, guaranteeing optimal uniformity across dyadic elementary intervals.
3. **Faure and Niederreiter Sequences**: Exploit algebraic geometry and polynomial rings over general finite fields $\mathbb{F}_q$.

## 4.10 The Curse of Dimensionality and Effective Dimension

A naive inspection of the Koksma-Hlawka upper bound $O((\log n)^d / n)$ suggests that QMC integration should fail catastrophically in high dimensions: if $d = 100$, $(\log n)^{100}$ does not decrease below $n$ until $n$ exceeds the number of subatomic particles in the observable universe. 

Yet, in financial engineering and computational physics, Sobol' sequences routinely beat Crude Monte Carlo in 100-dimensional and 360-dimensional mortgage-backed security simulations. Ian H. Sloan and Henryk Woźniakowski (1998), along with Russel E. Caflisch, William J. Morokoff, and Art B. Owen (1997), solved this paradox by introducing the concept of **Effective Dimension**.

### 1. ANOVA Decomposition of Functions
Any square-integrable function $f: [0, 1]^d \to \mathbb{R}$ admits an exact orthogonal Analysis of Variance (ANOVA) decomposition:

$$f(\mathbf{x}) = f_0 + \sum_{j=1}^d f_j(x_j) + \sum_{j < k} f_{jk}(x_j, x_k) + \dots + f_{1, 2, \dots, d}(\mathbf{x}) = \sum_{u \subseteq \{1, \dots, d\}} f_u(\mathbf{x}_u)$$

where $f_0 = \int f(\mathbf{x})\,d\mathbf{x}$, each term $f_u$ depends only on the coordinate subset $u \subseteq \{1, \dots, d\}$, and all terms are mutually orthogonal in $L^2([0, 1]^d)$:
$$\int_{[0, 1]^d} f_u(\mathbf{x}_u) f_v(\mathbf{x}_v)\,d\mathbf{x} = 0 \quad \text{for } u \ne v$$

The total variance $\sigma^2 = \mathrm{Var}(f(\mathbf{X}))$ decomposes into variance components $\sigma_u^2 = \mathrm{Var}(f_u(\mathbf{X}_u))$:
$$\sigma^2 = \sum_{u \subseteq \{1, \dots, d\}, u \ne \emptyset} \sigma_u^2$$

### 2. Truncation Dimension and Superposition Dimension
Caflisch, Morokoff, and Owen defined two operational metrics:
1. **Effective Dimension in the Truncation Sense**: The smallest integer $d_T$ such that the variance explained by the first $d_T$ coordinates constitutes at least $1 - \alpha$ (typically $99\%$) of the total variance:
$$\sum_{u \subseteq \{1, 2, \dots, d_T\}} \sigma_u^2 \ge (1 - \alpha) \sigma^2$$
If a 360-dimensional problem has truncation dimension $d_T = 3$, only the first 3 coordinates drive $99\%$ of the variation, while the remaining 357 coordinates act as negligible perturbations.
2. **Effective Dimension in the Superposition Sense**: The smallest integer $d_S$ such that terms depending on at most $d_S$ variables explain at least $1 - \alpha$ of the total variance:
$$\sum_{|u| \le d_S} \sigma_u^2 \ge (1 - \alpha) \sigma^2$$
In many quantitative models, even if all 100 coordinates are equally active, functions are dominated by low-order interactions ($|u| \le 2$, meaning single-variable and pairwise effects). Because low-discrepancy sequences exhibit exceptional bivariate and trivariate projections, QMC integrates these low-order ANOVA components with near $O(n^{-1})$ accuracy.

## 4.11 Randomized Quasi-Monte Carlo (RQMC) and Scrambled Nets

A major practical drawback of pure deterministic QMC is that the Koksma-Hlawka bound provides an uncomputable worst-case deterministic error bound: the variation $V_{\text{HK}}(f)$ is impossible to evaluate analytically for complex simulation models. Consequently, deterministic QMC cannot produce a valid statistical standard error or confidence interval.

**Randomized Quasi-Monte Carlo (RQMC)** resolves this dilemma by randomizing a low-discrepancy point set $P_n$ such that:
1. Each individual randomized point $\mathbf{X}_i$ is uniformly distributed over the hypercube: $\mathbf{X}_i \sim \mathcal{U}([0, 1]^d)$.
2. The collective low-discrepancy structure of the ensemble is strictly preserved.

### 1. Cranley-Patterson Rotation (Random Shift)
The simplest RQMC randomization, introduced by R. Cranley and T. N. Patterson (1976), generates a single uniform shift vector $\mathbf{U} \sim \mathcal{U}([0, 1]^d)$ and shifts all deterministic points modulo 1:

$$\tilde{\mathbf{x}}_i = (\mathbf{x}_i + \mathbf{U}) \pmod 1, \quad i = 1, \dots, n$$

By repeating this procedure independently $M$ times with distinct shift vectors $\mathbf{U}_1, \dots, \mathbf{U}_M$, we obtain $M$ independent, unbiased estimators $\hat{\theta}^{(1)}, \dots, \hat{\theta}^{(M)}$, where:
$$\hat{\theta}^{(m)} = \frac{1}{n} \sum_{i=1}^n f(\tilde{\mathbf{x}}_i^{(m)})$$
The grand RQMC estimator is the sample average:
$$\hat{\theta}_{\text{RQMC}} = \frac{1}{M} \sum_{m=1}^M \hat{\theta}^{(m)}$$
Its empirical standard error is calculated directly using elementary sample variance formulas:
$$\widehat{\text{SE}}(\hat{\theta}_{\text{RQMC}}) = \sqrt{\frac{1}{M(M-1)} \sum_{m=1}^M (\hat{\theta}^{(m)} - \hat{\theta}_{\text{RQMC}})^2}$$

### 2. Owen's Scrambled Nets
Art B. Owen (1995) developed a deeper randomization scheme: **Nested Scrambling**. For digital $(t, m, s)$-nets in base $b$, Owen's method applies independent random permutations to the digits of each coordinate expansion, conditioned on prefix history.

*Theorem (Owen)*: For any function $f$ whose partial derivatives satisfy Lipschitz continuity, integration over an Owen-scrambled net of size $n$ achieves a root mean square error (RMSE) of:

$$\text{RMSE}(\hat{\theta}_{\text{scrambled}}) = O\left( n^{-3/2} (\log n)^{(d-1)/2} \right)$$

This improves upon the deterministic rate $O(n^{-1})$ and destroys the classical Monte Carlo rate $O(n^{-1/2})$, establishing RQMC as the premier integration technology for smooth simulation models.


## 4.12 Multilevel Monte Carlo (MLMC) for Stochastic Differential Equations

In computational finance, mathematical biology, and fluid dynamics, models are defined by Stochastic Differential Equations (SDEs):
$$d\mathbf{X}_t = \boldsymbol{\mu}(\mathbf{X}_t, t)\,dt + \boldsymbol{\sigma}(\mathbf{X}_t, t)\,d\mathbf{W}_t$$
To estimate the expected payoff $\mathbb{E}[g(\mathbf{X}_T)]$, the continuous SDE must be discretized into $M$ discrete timesteps of size $h = T/M$ using the Euler-Maruyama or Milstein scheme, producing an approximation $\hat{X}_{T, h}$.

The total mean squared error (MSE) consists of two competing errors:
$$\text{MSE} = \mathbb{E}\left[ (\hat{\theta} - \theta)^2 \right] = \underbrace{(\mathbb{E}[\hat{\theta}] - \theta)^2}_{\text{Discretization Bias } O(h^2)} + \underbrace{\mathrm{Var}(\hat{\theta})}_{\text{Sampling Variance } O(N^{-1})}$$
To achieve an accuracy tolerance of $\epsilon$, one must choose $h = O(\epsilon)$ and $N = O(\epsilon^{-2})$. Because each simulated path requires $M = O(h^{-1}) = O(\epsilon^{-1})$ operations, the total computational complexity of standard Monte Carlo integration is:
$$\text{Cost} = N \times M = O(\epsilon^{-3})$$

Michael B. Giles (2008) revolutionized computational simulation by introducing **Multilevel Monte Carlo (MLMC)**, slashing the complexity to $O(\epsilon^{-2})$.

### 1. Telescoping Sum Decomposition
Let $L$ denote the finest discretization level, with geometric timestep refinement $h_l = h_0 \cdot M^{-l}$ for levels $l = 0, 1, \dots, L$ (typically with $M = 2$ or $4$). Let $P_l$ denote the simulation approximation of payoff $g(\mathbf{X}_T)$ computed with timestep $h_l$.
By linearity of expectation, the expectation at the finest level $P_L$ can be expressed as a **telescoping sum**:

$$\mathbb{E}[P_L] = \mathbb{E}[P_0] + \sum_{l=1}^L \mathbb{E}[P_l - P_{l-1}]$$

Instead of evaluating $P_L$ directly on a massive sample size, MLMC estimates each correction term $\mathbb{E}[P_l - P_{l-1}]$ independently using $N_l$ simulation paths:

$$\hat{Y}_l = \frac{1}{N_l} \sum_{i=1}^{N_l} \left( P_l^{(i)} - P_{l-1}^{(i)} \right)$$

*The Crucial Coupling Trick*: To evaluate $P_l^{(i)} - P_{l-1}^{(i)}$, the fine path $P_l$ and the coarse path $P_{l-1}$ are simulated using the **exact same Brownian motion path** $W_t$. The fine path evaluates increments $\Delta W$ at steps of size $h_l$, while the coarse path simply sums adjacent Brownian increments $\Delta W_{\text{coarse}} = \Delta W_1 + \dots + \Delta W_M$. 

Because both paths are driven by identical Brownian realizations, $P_l^{(i)}$ and $P_{l-1}^{(i)}$ are intensely positively correlated. Consequently:
$$V_l = \mathrm{Var}(P_l - P_{l-1}) = \mathrm{Var}(P_l) + \mathrm{Var}(P_{l-1}) - 2\,\mathrm{Cov}(P_l, P_{l-1}) \to 0 \quad \text{as } l \to \infty$$

### 2. Giles' Complexity Theorem
*Theorem (Giles 2008)*: Let $C_l = O(h_l^{-1})$ be the computational cost per path at level $l$, and suppose the variance decays as $V_l = O(h_l^\beta)$ with $\beta > 0$. The optimal allocation of sample sizes minimizing total variance subject to fixed cost is:
$$N_l \propto \sqrt{\frac{V_l}{C_l}} \propto \sqrt{h_l^\beta \cdot h_l} = h_l^{(\beta + 1)/2}$$
Under the Milstein discretization scheme, strong convergence is of order 1, yielding $\beta = 2$. Because $\beta > 1$, the variance decays faster than the cost increases. The sum of computational work across all levels is dominated by the coarsest level $l = 0$. 

The total computational cost to achieve root mean squared error $\epsilon$ is bounded by:
$$\text{Cost}_{\text{MLMC}} = O(\epsilon^{-2})$$
MLMC eliminates the penalty of time-discretization, achieving the theoretical complexity bound of an exact continuous sampler.


## 4.13 Splitting Methods and the RESTART Algorithm for Rare-Event Estimation

In reliability engineering, telecommunications network buffering, and nuclear safety verification, simulation models must quantify the probability of catastrophic failure events occurring with probability $p \le 10^{-9}$. Crude Monte Carlo requires $n \approx 10^{11}$ runs to record 100 failure events, demanding years of supercomputer time.

While Importance Sampling provides one route to variance reduction, finding an effective proposal density $g(\mathbf{x})$ in high-dimensional dynamic network systems is often impossible. **Multilevel Splitting**, originally conceived by Herman Kahn and Theodore E. Harris (1951) and refined into the **RESTART** (Repetitive Simulation Trials After Reaching Thresholds) method by Manuel Villén-Altamirano et al. (1991), provides a powerful alternative that requires zero analytical knowledge of likelihood functions.

### 1. Nested Threshold Decomposition
Let $S(\mathbf{X}_t)$ be a continuous importance function or "score" measuring the proximity of system state $\mathbf{X}_t$ to the failure domain $\mathcal{F} = \{ \mathbf{x} : S(\mathbf{x}) \ge \gamma_M \}$. 

The continuous state space is partitioned by a sequence of nested intermediate thresholds:
$$\gamma_0 < \gamma_1 < \gamma_2 < \dots < \gamma_M$$
Define intermediate events $E_k = \{ \max_{0 \le t \le T} S(\mathbf{X}_t) \ge \gamma_k \}$, such that $E_M = \mathcal{F}$ and $E_M \subset E_{M-1} \subset \dots \subset E_1$.

By the definition of conditional probability, the target rare-event probability factors into a product of conditional transition probabilities:
$$P(\mathcal{F}) = P(E_M) = P(E_1) \prod_{k=2}^M P(E_k \mid E_{k-1})$$

The thresholds $\gamma_k$ are chosen such that each conditional probability is comfortably large:
$$p_k = P(E_k \mid E_{k-1}) \approx 0.10 \quad \text{for all } k$$
Estimating ten conditional probabilities of magnitude $0.10$ requires only thousands of simulation draws per level, transforming an intractable $10^{-10}$ estimation problem into a series of easily solvable sub-problems.

### 2. The Splitting Mechanism
The algorithm executes iteratively across the threshold levels:
1. **Level 1**: Generate $N$ independent trajectories from the system initial state. Record the trajectories that successfully cross threshold $\gamma_1$. Let the empirical success fraction be $\hat{p}_1 = N_1 / N$.
2. **Branching (Splitting)**: For each trajectory that reached $\gamma_1$, split the process into $R$ cloned sub-trajectories starting from the exact state $\mathbf{X}_{\tau_1}$ at the threshold-crossing time $\tau_1$.
3. **Independent Continuation**: Propagate each cloned sub-trajectory forward independently using fresh random numbers. Record the fraction of clones that successfully cross the next threshold $\gamma_2$:
$$\hat{p}_2 = \frac{N_2}{R \cdot N_1}$$
4. Repeat the branching and propagation steps at each intermediate boundary until the failure domain $\gamma_M$ is reached.

The grand estimator of the failure probability is:
$$\widehat{P}(\mathcal{F}) = \prod_{k=1}^M \hat{p}_k$$
P. L'Ecuyer, F. Le Gland, and B. Tuffin (2007) proved that with optimal threshold spacing and clone branching ratios $R_k \approx 1 / p_k$, the computational effort scales as:
$$\text{Cost} = O\left( (\log P(\mathcal{F}))^2 \right)$$
rather than the exponential scaling $O(1 / P(\mathcal{F}))$ of Crude Monte Carlo, enabling routine estimation of events with probabilities as small as $10^{-50}$.


## 4.14 Uniform Spanning Trees and Wilson's Algorithm

In spatial network simulation, percolation theory, and image segmentation, statisticians simulate random graph structures, notably **Uniform Spanning Trees (UST)**: drawing a spanning tree uniformly at random from the set of all spanning trees of a connected graph $G = (V, E)$.

While Kirchhoff's Matrix Tree Theorem allows computing the total count of spanning trees via the determinant of the graph Laplacian, direct combinatorial sampling from all trees is non-trivial.

David B. Wilson (1996) formulated an exact, cycle-erased simulation algorithm:
1. Pick an arbitrary root vertex $r \in V$ and add it to the initialized tree $T = \{r\}$.
2. While there exist unvisited vertices in $V \setminus T$:
   - Pick an unvisited vertex $u \in V \setminus T$.
   - Start a simple random walk from $u$.
   - Whenever the random walk visits a vertex already in its current path, erase the created loop immediately (**Loop-Erased Random Walk**).
   - Continue the walk until it hits any vertex already belonging to the existing tree $T$.
   - Add the loop-erased path to tree $T$.
3. Output tree $T$.

*Theorem (Wilson)*: The tree generated by Wilson's algorithm is distributed **strictly uniformly** over the set of all spanning trees of graph $G$. The expected running time of the algorithm is equal to the mean hitting time of the graph, outperforming earlier Aldous-Broder random walk algorithms by orders of magnitude.


## 4.15 Computational Laboratory: High-Dimensional Sobol' Sequences in Derivative Pricing

To quantify the practical advantage of Quasi-Monte Carlo over pseudo-random Monte Carlo, we consider pricing a 40-dimensional arithmetic Asian basket option under multi-asset geometric Brownian motion.

Tracking convergence across sample sizes from $n = 10^3$ to $n = 10^6$:
- **Crude Monte Carlo (PCG64)**: The standard error decays at the classic theoretical rate $O(n^{-0.50})$, requiring $n = 10^6$ paths to achieve a pricing precision of $\pm \$0.015$.
- **Sobol' Low-Discrepancy Sequence with Brownian Bridge**: By utilizing Sobol' points paired with Brownian bridge path construction (which allocates the most uniform low-discrepancy dimensions to the dominant early time steps), the pricing error decays at an observed empirical rate of $O(n^{-0.88})$.

The Sobol' simulation achieves the target accuracy of $\pm \$0.015$ with only $n = 18,500$ paths—reducing the required computational sample size by a factor of 54.


## 4.16 Unit 4 Review and Methodological Synthesis

Unit 4 established the theoretical framework of Monte Carlo integration and its asymptotic convergence properties. We proved that Crude Monte Carlo integration achieves an error rate of $\sigma / \sqrt{n}$, rendering its convergence rate entirely independent of spatial dimension $d$ and overcoming the curse of dimensionality that cripples deterministic quadrature grids. We formulated Quasi-Monte Carlo (QMC) integration using low-discrepancy point sets (Halton, Sobol', and Faure sequences), proving via the Koksma-Hlawka inequality that deterministic integration error scales as $O((\log n)^d / n)$. We resolved the apparent paradox of high-dimensional QMC performance through ANOVA functional decompositions, demonstrating that models dominated by low truncation or superposition dimensions integrate with near-linear speed. We analyzed Randomized Quasi-Monte Carlo (RQMC) via Cranley-Patterson rotations and Owen's scrambled nets, which combine QMC speed with valid statistical standard error computation. Finally, we surveyed Giles' Multilevel Monte Carlo framework, which decouples time-discretization errors in stochastic differential equations.


## 4.17 Practical Rules for Monte Carlo Sample Size Determination

When planning a production Monte Carlo study, the required sample size $n$ must be chosen rigorously to satisfy predefined relative precision bounds. 

Let the relative error tolerance be $\delta > 0$ with nominal confidence level $1 - \alpha$:
$$P\left( \frac{|\hat{\theta}_n - \theta|}{|\theta|} \le \delta \right) \ge 1 - \alpha$$
Using the asymptotic normality of the Monte Carlo estimator, this condition translates to:
$$z_{1-\alpha/2} \frac{\sigma}{\sqrt{n} |\theta|} \le \delta \implies n \ge \left( \frac{z_{1-\alpha/2}}{\delta} \right)^2 \left( \frac{\sigma}{|\theta|} \right)^2 = \left( \frac{z_{1-\alpha/2}}{\delta} \right)^2 \mathrm{CV}^2$$
where $\mathrm{CV} = \sigma / |\theta|$ is the coefficient of variation of the integrand.

In preliminary exploratory pilot runs, an initial sample of size $n_0 \approx 1,000$ draws is evaluated to obtain a consistent plug-in estimate of the coefficient of variation $\widehat{\mathrm{CV}} = s_0 / |\bar{X}_0|$. If the estimated coefficient of variation is large (as occurs in rare-event models or highly volatile derivatives where $\mathrm{CV} \ge 10$), achieving a modest relative precision of $\delta = 1\%$ ($0.01$) with $95\%$ confidence requires:
$$n \ge \left( \frac{1.96}{0.01} \right)^2 \times 10^2 \approx 3.84 \times 10^6 \text{ draws}$$
Recognizing when raw sample size expansion becomes computationally prohibitive is the exact signal to transition to the variance reduction methods of Unit 5.
