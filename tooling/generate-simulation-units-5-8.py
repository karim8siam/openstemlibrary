#!/usr/bin/env python3
"""
Generate Units 5 to 8 for Statistical Simulation and Monte Carlo Methods.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
u5 = r"""# Unit 5: Variance Reduction Techniques

In Unit 4, we established that the estimation error of Crude Monte Carlo integration decays at the universal asymptotic rate $\text{SE}(\hat{\theta}_n) = \sigma / \sqrt{n}$. To achieve an order-of-magnitude improvement in estimation accuracy (reducing standard error by a factor of 10), a naive brute-force approach requires multiplying the computational sample size $n$ by a factor of 100 ($10^2$). In high-dimensional quantitative risk modeling, climate projection, and particle physics, generating millions of independent draws is computationally prohibitive.

**Variance Reduction Techniques (VRTs)** are sophisticated statistical transformation methods that modify the simulation design to substantially suppress the numerator $\sigma^2 = \mathrm{Var}(h(\mathbf{X}))$ without altering the expected value $\mathbb{E}[\hat{\theta}] = \theta$. By exploiting known analytical symmetries, auxiliary variables, or importance weighting, variance reduction yields identical or superior precision with orders-of-magnitude fewer computational evaluations.

## 5.1 The Antithetic Variates Method

The **Antithetic Variates Method**, introduced by J. M. Hammersley and K. W. Morton in 1956, reduces variance by deliberately inducing negative covariance between pairs of simulation draws.

### 1. Mathematical Formulation
Suppose we desire to estimate $\theta = \mathbb{E}[h(U)]$, where $U \sim \mathcal{U}(0, 1)$.
Because the standard uniform distribution is symmetric about $0.5$, if $U \sim \mathcal{U}(0, 1)$, its complement $1 - U$ is also identically distributed as $\mathcal{U}(0, 1)$.

Instead of drawing $2n$ independent uniform variates, the antithetic approach generates $n$ independent pairs $(U_i, 1 - U_i)$ and evaluates:
$$\hat{\theta}_{\text{anti}} = \frac{1}{2n} \sum_{i=1}^n \left[ h(U_i) + h(1 - U_i) \right] = \frac{1}{n} \sum_{i=1}^n \left( \frac{h(U_i) + h(1 - U_i)}{2} \right)$$

Let $W_i = \frac{1}{2} [h(U_i) + h(1 - U_i)]$. By linearity of expectation:
$$\mathbb{E}[\hat{\theta}_{\text{anti}}] = \mathbb{E}[W_i] = \frac{1}{2} (\mathbb{E}[h(U)] + \mathbb{E}[h(1 - U)]) = \frac{1}{2} (\theta + \theta) = \theta$$
The estimator is strictly unbiased.

### 2. Variance Analysis and Monotonicity
The variance of the antithetic average is:
$$\mathrm{Var}(W_i) = \mathrm{Var}\left( \frac{h(U) + h(1 - U)}{2} \right) = \frac{1}{4} \left[ \mathrm{Var}(h(U)) + \mathrm{Var}(h(1 - U)) + 2\,\mathrm{Cov}(h(U), h(1 - U)) \right]$$
Since $1 - U \stackrel{d}{=} U$, $\mathrm{Var}(h(1 - U)) = \mathrm{Var}(h(U)) = \sigma^2$. Therefore:

$$\mathrm{Var}(W_i) = \frac{\sigma^2}{2} + \frac{1}{2} \mathrm{Cov}(h(U), h(1 - U))$$

Comparing $\hat{\theta}_{\text{anti}}$ (which uses $2n$ function evaluations across $n$ pairs) with a Crude Monte Carlo estimator $\hat{\theta}_{\text{crude}}$ based on $2n$ independent draws:
$$\mathrm{Var}(\hat{\theta}_{\text{crude}}) = \frac{\sigma^2}{2n}$$
$$\mathrm{Var}(\hat{\theta}_{\text{anti}}) = \frac{\mathrm{Var}(W_i)}{n} = \frac{\sigma^2}{2n} + \frac{\mathrm{Cov}(h(U), h(1 - U))}{2n}$$

The antithetic estimator achieves strict variance reduction ($\mathrm{Var}(\hat{\theta}_{\text{anti}}) < \mathrm{Var}(\hat{\theta}_{\text{crude}})$) if and only if the covariance between paired evaluations is strictly negative:

$$\mathrm{Cov}(h(U), h(1 - U)) < 0$$

*Theorem (Monotonic Functions Guarantee Variance Reduction)*: If $h(u)$ is a monotonically increasing (or monotonically decreasing) function on $[0, 1]$, then:
$$\mathrm{Cov}(h(U), h(1 - U)) \le 0$$
with strict inequality unless $h(u)$ is a constant almost everywhere.

*Proof Intuition*: If $h$ is monotonic increasing, when $U$ is larger than $0.5$, $h(U)$ is above average, while $1 - U$ is smaller than $0.5$, forcing $h(1 - U)$ below average. Deviations from the mean systematically cancel out, producing substantial variance suppression.

## 5.2 The Control Variates Method

The **Control Variates Method** reduces variance by incorporating an auxiliary random variable $Y$ whose expectation $\mu_Y = \mathbb{E}[Y]$ is analytically known.

### 1. The Controlled Estimator
Suppose we want to estimate $\theta = \mathbb{E}[X]$, where $X = h(\mathbf{U})$.
Let $Y = g(\mathbf{U})$ be an auxiliary variable simulated simultaneously with $X$, where $\mu_Y = \mathbb{E}[Y]$ is known exactly in closed form.

For any real scalar coefficient $c \in \mathbb{R}$, define the controlled estimator:

$$\hat{\theta}_c = X - c (Y - \mu_Y)$$

We evaluate its properties:
1. **Unbiasedness**:
   $$\mathbb{E}[\hat{\theta}_c] = \mathbb{E}[X] - c (\mathbb{E}[Y] - \mu_Y) = \theta - c(0) = \theta$$
   The controlled estimator is unconditionally unbiased for *any arbitrary value* of $c \in \mathbb{R}$!
2. **Variance**:
   $$\mathrm{Var}(\hat{\theta}_c) = \mathrm{Var}(X - c Y) = \mathrm{Var}(X) - 2 c\,\mathrm{Cov}(X, Y) + c^2\,\mathrm{Var}(Y)$$

### 2. Derivation of the Optimal Control Coefficient $c^*$
To minimize $\mathrm{Var}(\hat{\theta}_c)$ with respect to $c$, differentiate and set to zero:
$$\frac{d}{dc} \mathrm{Var}(\hat{\theta}_c) = -2\,\mathrm{Cov}(X, Y) + 2 c\,\mathrm{Var}(Y) = 0$$

Solving for the optimal coefficient $c^*$:

$$c^* = \frac{\mathrm{Cov}(X, Y)}{\mathrm{Var}(Y)} = \rho_{XY} \frac{\sigma_X}{\sigma_Y}$$

Notice that $c^*$ is mathematically identical to the population regression slope of $X$ on $Y$ in ordinary least squares regression!

Substituting $c^*$ into the variance equation:
$$\mathrm{Var}(\hat{\theta}_{c^*}) = \sigma_X^2 - 2 \left( \frac{\mathrm{Cov}(X, Y)}{\sigma_Y^2} \right) \mathrm{Cov}(X, Y) + \left( \frac{\mathrm{Cov}(X, Y)}{\sigma_Y^2} \right)^2 \sigma_Y^2$$
$$\mathrm{Var}(\hat{\theta}_{c^*}) = \sigma_X^2 - \frac{[\mathrm{Cov}(X, Y)]^2}{\sigma_Y^2} = \sigma_X^2 \left( 1 - \frac{[\mathrm{Cov}(X, Y)]^2}{\sigma_X^2 \sigma_Y^2} \right)$$

$$\mathrm{Var}(\hat{\theta}_{c^*}) = \mathrm{Var}(X) \cdot (1 - \rho_{XY}^2)$$

where $\rho_{XY} = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}$ is the Pearson correlation coefficient between target $X$ and control $Y$.

The percentage variance reduction is exactly equal to the squared correlation coefficient:

$$\text{Percentage Variance Reduction} = \rho_{XY}^2 = R^2$$

- If $|\rho_{XY}| = 0.90$, variance is reduced by $81\%$ (a 5.26-fold increase in efficiency).
- If $|\rho_{XY}| = 0.99$, variance is reduced by $98\%$ (a 50-fold efficiency gain).
In practice, $c^*$ is estimated from the simulated sample using sample covariance and sample variance without inducing asymptotic bias.

## 5.3 Importance Sampling: Change of Measure and Optimal Proposal

When simulating rare events (e.g., probability of default in financial stress testing $\theta < 10^{-5}$ or nuclear reactor breach probabilities), Crude Monte Carlo is useless because virtually all simulated paths fall in the uninformative normal operating region. **Importance Sampling** deliberately alters the sampling distribution to force frequent visitations to the critical rare-event region, adjusting each draw by a likelihood ratio weight to preserve strict unbiasedness.

### 1. Mathematical Formulation: The Radon-Nikodym Derivative
Let $\theta = \mathbb{E}_f[h(\mathbf{X})] = \int_{\mathcal{X}} h(\mathbf{x}) f(\mathbf{x})\,d\mathbf{x}$.
Let $g(\mathbf{x})$ be an alternative probability density function (the **importance proposal density**) satisfying the absolute continuity condition:
$$h(\mathbf{x}) f(\mathbf{x}) \ne 0 \implies g(\mathbf{x}) > 0$$

We rewrite the integral by multiplying and dividing by $g(\mathbf{x})$:

$$\theta = \int_{\mathcal{X}} h(\mathbf{x}) \frac{f(\mathbf{x})}{g(\mathbf{x})} g(\mathbf{x})\,d\mathbf{x} = \int_{\mathcal{X}} \left[ h(\mathbf{x}) w(\mathbf{x}) \right] g(\mathbf{x})\,d\mathbf{x} = \mathbb{E}_g\left[ h(\mathbf{X}) w(\mathbf{X}) \right]$$

where:

$$w(\mathbf{x}) = \frac{f(\mathbf{x})}{g(\mathbf{x})}$$

is the **likelihood ratio** or **importance weight** (the Radon-Nikodym derivative $df / dg$).

The **Importance Sampling Estimator** based on $n$ independent draws $\mathbf{Y}_1, \dots, \mathbf{Y}_n \sim g(\mathbf{y})$ is:

$$\hat{\theta}_{\text{IS}} = \frac{1}{n} \sum_{i=1}^n h(\mathbf{Y}_i) w(\mathbf{Y}_i) = \frac{1}{n} \sum_{i=1}^n h(\mathbf{Y}_i) \frac{f(\mathbf{Y}_i)}{g(\mathbf{Y}_i)}$$

By construction, $\mathbb{E}_g[\hat{\theta}_{\text{IS}}] = \theta$, guaranteeing strict unbiasedness.

### 2. The Zero-Variance Optimal Proposal Density
The variance of the importance sampling estimator is:
$$\mathrm{Var}_g(\hat{\theta}_{\text{IS}}) = \frac{1}{n} \mathrm{Var}_g(h(\mathbf{Y}) w(\mathbf{Y})) = \frac{1}{n} \left[ \mathbb{E}_g\left( h(\mathbf{Y})^2 w(\mathbf{Y})^2 \right) - \theta^2 \right] = \frac{1}{n} \left[ \int_{\mathcal{X}} \frac{h(\mathbf{x})^2 f(\mathbf{x})^2}{g(\mathbf{x})}\,d\mathbf{x} - \theta^2 \right]$$

*Theorem (Optimal Zero-Variance Importance Density)*: If $h(\mathbf{x}) \ge 0$, the importance proposal density $g^*(\mathbf{x})$ that minimizes the variance satisfies:

$$g^*(\mathbf{x}) = \frac{h(\mathbf{x}) f(\mathbf{x})}{\int_{\mathcal{X}} h(\mathbf{u}) f(\mathbf{u})\,d\mathbf{u}} = \frac{h(\mathbf{x}) f(\mathbf{x})}{\theta}$$

Under this optimal density, the variance is **identically zero**:

$$\mathrm{Var}_{g^*}(\hat{\theta}_{\text{IS}}) \equiv 0$$

*Proof*:
Under $g^*(\mathbf{x})$, the importance weight is $w(\mathbf{x}) = \frac{f(\mathbf{x})}{g^*(\mathbf{x})} = \frac{\theta}{h(\mathbf{x})}$.
Therefore, for every single candidate draw $\mathbf{Y}_i$:
$$h(\mathbf{Y}_i) w(\mathbf{Y}_i) = h(\mathbf{Y}_i) \cdot \frac{\theta}{h(\mathbf{Y}_i)} = \theta$$
Every simulated summand evaluates identically to the true integral $\theta$! A single draw ($n = 1$) yields the exact answer without any random variation.

*Practical Reality*: Because $g^*(\mathbf{x})$ requires knowing the normalizing constant $\theta$ (the very integral we wish to compute), $g^*$ cannot be implemented directly. However, the theorem provides the guiding principle: **choose an importance density $g(\mathbf{x})$ that is shaped proportionally to $|h(\mathbf{x})| f(\mathbf{x})$**, concentrating samples where the integrand is largest.

*Cautionary Principle on Heavy Tails*: The proposal $g(\mathbf{x})$ must have **heavier tails** than $f(\mathbf{x})$. If $g(\mathbf{x})$ decays faster than $f(\mathbf{x})$ in the tails, the likelihood ratio $w(\mathbf{x}) = f(\mathbf{x})/g(\mathbf{x}) \to \infty$, causing the variance $\mathbb{E}_g[h^2 w^2]$ to become infinite!

## 5.4 Stratified Sampling and Latin Hypercube Sampling (LHS)

### 1. Stratified Sampling
Stratified sampling partitions the integration domain $\mathcal{D}$ into $K$ mutually disjoint strata $\mathcal{D}_1, \dots, \mathcal{D}_K$ such that $\bigcup_{k=1}^K \mathcal{D}_k = \mathcal{D}$ and $\mathcal{D}_j \cap \mathcal{D}_k = \emptyset$.
Let $p_k = P(\mathbf{X} \in \mathcal{D}_k) = \int_{\mathcal{D}_k} f(\mathbf{x})\,d\mathbf{x}$ be the stratum probability weight, and let $\theta_k = \mathbb{E}[h(\mathbf{X}) \mid \mathbf{X} \in \mathcal{D}_k]$ be the conditional expectation.

The overall expectation decomposes as:
$$\theta = \sum_{k=1}^K p_k \theta_k$$

In each stratum $k$, draw $n_k$ independent samples from the conditional density $f(\mathbf{x} \mid \mathbf{X} \in \mathcal{D}_k)$, and compute the stratified estimator:
$$\hat{\theta}_{\text{strat}} = \sum_{k=1}^K p_k \hat{\theta}_k, \quad \text{where } \hat{\theta}_k = \frac{1}{n_k} \sum_{i=1}^{n_k} h(\mathbf{X}_{ki})$$

The total variance decomposes via the **Law of Total Variance**:
$$\mathrm{Var}(\hat{\theta}_{\text{strat}}) = \sum_{k=1}^K \frac{p_k^2 \sigma_k^2}{n_k}$$
where $\sigma_k^2 = \mathrm{Var}(h(\mathbf{X}) \mid \mathbf{X} \in \mathcal{D}_k)$ is the within-stratum variance.
Stratified sampling completely eliminates the between-stratum variance $\sum p_k (\theta_k - \theta)^2$ from the estimation error!

Under **Neyman Optimal Allocation**, the sample allocation per stratum that minimizes total variance for fixed total sample size $n = \sum n_k$ is:
$$n_k^* = n \frac{p_k \sigma_k}{\sum_{j=1}^K p_j \sigma_j}$$

### 2. Latin Hypercube Sampling (LHS)
Developed by McKay, Beckman, and Conover (1979), **Latin Hypercube Sampling** extends stratification to $d$-dimensional hypercubes.
For $n$ simulation runs in $d$ dimensions:
- The range of each coordinate variable $j \in \{1, \dots, d\}$ is partitioned into $n$ equiprobable intervals: $[0, 1/n), [1/n, 2/n), \dots, [(n-1)/n, 1]$.
- In each interval along each dimension, exactly one point is placed.
- The coordinates are matched across dimensions using random independent permutations $\pi_j \in S_n$:
  $$\mathbf{U}_i = \left( \frac{\pi_1(i) - 1 + V_{1i}}{n}, \; \frac{\pi_2(i) - 1 + V_{2i}}{n}, \; \dots, \; \frac{\pi_d(i) - 1 + V_{di}}{n} \right)$$
  where $V_{ji} \sim \mathcal{U}(0, 1)$.
LHS guarantees that the marginal projections onto every single one-dimensional coordinate axis are completely uniform and non-overlapping, eliminating clustering and significantly reducing variance for additive integrands.

## Fully worked question 1: Antithetic Variates for Exponential Decay Integration

### Question
An actuary computes the expected discounted payout of a continuous perpetuity:
$$\theta = \int_0^1 e^{-2x}\,dx$$
1. Evaluate the exact analytical value of $\theta$.
2. Compute the theoretical variance of the Crude Monte Carlo estimator $\hat{\theta}_{\text{crude}}$ based on $2n$ independent uniform draws from $\mathcal{U}(0, 1)$.
3. Compute the theoretical variance of the Antithetic Variates estimator $\hat{\theta}_{\text{anti}}$ based on $n$ antithetic pairs $(U_i, 1 - U_i)$, and calculate the percentage variance reduction and efficiency gain.

### Solution, step 1: Exact Analytical Integration
The integrand is $h(x) = e^{-2x}$ on $[0, 1]$:
$$\theta = \int_0^1 e^{-2x}\,dx = \left[ -\frac{1}{2} e^{-2x} \right]_0^1 = -\frac{1}{2} e^{-2} - \left(-\frac{1}{2}\right) = \frac{1 - e^{-2}}{2}$$
Evaluating numerically:
$$e^{-2} = \frac{1}{e^2} \approx \frac{1}{7.389056} \approx 0.1353353$$
$$\theta = \frac{1 - 0.1353353}{2} = \frac{0.8646647}{2} \approx 0.432332$$

### Solution, step 2: Variance of Crude Monte Carlo
Let $U \sim \mathcal{U}(0, 1)$. The second moment is:
$$\mathbb{E}[h(U)^2] = \int_0^1 (e^{-2u})^2 du = \int_0^1 e^{-4u}\,du = \left[ -\frac{1}{4} e^{-4u} \right]_0^1 = \frac{1 - e^{-4}}{4}$$
$$e^{-4} \approx 0.0183156 \implies \mathbb{E}[h(U)^2] = \frac{1 - 0.0183156}{4} = \frac{0.9816844}{4} \approx 0.2454211$$
The population variance is:
$$\sigma^2 = \mathrm{Var}(h(U)) = \mathbb{E}[h(U)^2] - \theta^2 = 0.2454211 - (0.432332)^2$$
$$0.432332^2 \approx 0.186911 \implies \sigma^2 = 0.2454211 - 0.1869110 = 0.058510$$
For $2n$ independent evaluations, the Crude Monte Carlo variance is:
$$\mathrm{Var}(\hat{\theta}_{\text{crude}}) = \frac{\sigma^2}{2n} = \frac{0.058510}{2n} = \frac{0.029255}{n}$$

### Solution, step 3: Variance of Antithetic Estimator and Efficiency Gain
For an antithetic pair $(U, 1 - U)$, the cross-product expectation is:
$$\mathbb{E}[h(U) h(1 - U)] = \int_0^1 e^{-2u} e^{-2(1 - u)}\,du = \int_0^1 e^{-2u - 2 + 2u}\,du = \int_0^1 e^{-2}\,du = e^{-2} \approx 0.1353353$$
The covariance between antithetic evaluations is:
$$\mathrm{Cov}(h(U), h(1 - U)) = \mathbb{E}[h(U) h(1 - U)] - \theta^2 = 0.1353353 - 0.1869110 = -0.0515757$$
Notice that the covariance is strongly negative!

The variance of the antithetic pair average $W = \frac{1}{2}[h(U) + h(1 - U)]$ is:
$$\mathrm{Var}(W) = \frac{\sigma^2}{2} + \frac{1}{2} \mathrm{Cov}(h(U), h(1 - U)) = \frac{0.058510}{2} + \frac{-0.0515757}{2} = 0.029255 - 0.025788 = 0.003467$$
The variance of the antithetic estimator based on $n$ pairs ($2n$ total evaluations) is:
$$\mathrm{Var}(\hat{\theta}_{\text{anti}}) = \frac{\mathrm{Var}(W)}{n} = \frac{0.003467}{n}$$

Comparing the variances for the exact same computational cost ($2n$ evaluations):
$$\text{Variance Ratio} = \frac{\mathrm{Var}(\hat{\theta}_{\text{anti}})}{\mathrm{Var}(\hat{\theta}_{\text{crude}})} = \frac{0.003467 / n}{0.029255 / n} = \frac{0.003467}{0.029255} \approx 0.1185$$
$$\text{Percentage Variance Reduction} = (1 - 0.1185) \times 100\% = 88.15\%$$
$$\text{Efficiency Gain} = \frac{\mathrm{Var}(\hat{\theta}_{\text{crude}})}{\mathrm{Var}(\hat{\theta}_{\text{anti}})} = \frac{0.029255}{0.003467} \approx 8.44$$
*Conclusion*: The antithetic estimator achieves an **8.44-fold computational speedup**, delivering the same precision with less than $12\%$ of the computational evaluations.

## Fully worked question 2: Control Variates for Non-Linear Function Integration

### Question
A financial engineer estimates the integral:
$$\theta = \int_0^1 \frac{1}{1 + x}\,dx = \ln(2) \approx 0.693147$$
using Monte Carlo simulation with $U \sim \mathcal{U}(0, 1)$.
To reduce variance, the engineer chooses the linear Taylor control variate:
$$Y = 1 - \frac{1}{2} U$$
whose expectation is $\mu_Y = \mathbb{E}[Y] = 1 - \frac{1}{2}(0.5) = 0.750$.
1. Compute the analytical variance of the target variable $X = \frac{1}{1 + U}$.
2. Compute the covariance $\mathrm{Cov}(X, Y)$ and variance $\mathrm{Var}(Y)$.
3. Determine the optimal control coefficient $c^*$, the resulting variance of the controlled estimator, and the percentage variance reduction.

### Solution, step 1: Variance of Target Variable $X$
The target is $X = h(U) = \frac{1}{1 + U}$ for $U \sim \mathcal{U}(0, 1)$:
$$\theta = \mathbb{E}[X] = \int_0^1 \frac{1}{1 + u}\,du = [\ln(1 + u)]_0^1 = \ln(2) \approx 0.693147$$
The second moment is:
$$\mathbb{E}[X^2] = \int_0^1 \left(\frac{1}{1 + u}\right)^2 du = \left[ -\frac{1}{1 + u} \right]_0^1 = -\frac{1}{2} - (-1) = \frac{1}{2} = 0.500$$
The variance is:
$$\mathrm{Var}(X) = \mathbb{E}[X^2] - \theta^2 = 0.500 - (0.693147)^2 = 0.500 - 0.480453 = 0.019547$$

### Solution, step 2: Covariance and Control Variance
The control variate is $Y = 1 - \frac{1}{2}U$:
$$\mathrm{Var}(Y) = \mathrm{Var}\left( 1 - \frac{1}{2}U \right) = \left(-\frac{1}{2}\right)^2 \mathrm{Var}(U) = \frac{1}{4} \times \frac{1}{12} = \frac{1}{48} \approx 0.020833$$

Now compute $\mathbb{E}[X Y]$:
$$X Y = \left(\frac{1}{1 + U}\right) \left( 1 - \frac{1}{2}U \right)$$
Notice that:
$$\frac{1 - \frac{1}{2}u}{1 + u} = \frac{\frac{3}{2} - \frac{1}{2}(1 + u)}{1 + u} = \frac{3/2}{1 + u} - \frac{1}{2}$$
Integrating over $[0, 1]$:
$$\mathbb{E}[X Y] = \int_0^1 \left( \frac{3/2}{1 + u} - \frac{1}{2} \right) du = \frac{3}{2} \ln(2) - \frac{1}{2} = 1.5 \times 0.693147 - 0.500 = 1.039721 - 0.500 = 0.539721$$
The covariance is:
$$\mathrm{Cov}(X, Y) = \mathbb{E}[X Y] - \mathbb{E}[X] \mathbb{E}[Y] = 0.539721 - (0.693147 \times 0.750) = 0.539721 - 0.519860 = 0.019861$$

### Solution, step 3: Optimal Coefficient $c^*$ and Variance Reduction
The optimal coefficient is:
$$c^* = \frac{\mathrm{Cov}(X, Y)}{\mathrm{Var}(Y)} = \frac{0.019861}{1 / 48} = 0.019861 \times 48 \approx 0.953328$$

The squared correlation coefficient is:
$$\rho_{XY}^2 = \frac{[\mathrm{Cov}(X, Y)]^2}{\mathrm{Var}(X) \mathrm{Var}(Y)} = \frac{(0.019861)^2}{0.019547 \times 0.020833} = \frac{0.00039446}{0.00040722} \approx 0.96866 \quad (96.87\%)$$

The variance of the controlled estimator is:
$$\mathrm{Var}(\hat{\theta}_{c^*}) = \mathrm{Var}(X) \cdot (1 - \rho_{XY}^2) = 0.019547 \times (1 - 0.96866) = 0.019547 \times 0.03134 \approx 0.0006126$$

Comparing with the original variance $\mathrm{Var}(X) = 0.019547$:
$$\text{Efficiency Gain} = \frac{0.019547}{0.0006126} \approx 31.9$$
*Conclusion*: The control variate achieves an astounding **96.87% variance reduction**, delivering a **31.9-fold computational efficiency gain** using a simple linear approximation!

## Fully worked question 3: Importance Sampling for Extreme Gaussian Tail Estimation

### Question
An extreme value analyst estimates the deep tail probability $\theta = P(Z > 4.5)$ for $Z \sim \mathcal{N}(0, 1)$, whose true value is approximately $3.39767 \times 10^{-6}$.
1. Explain why Crude Monte Carlo with $n = 10^5$ draws will fail to provide any meaningful estimate.
2. Formulate an Importance Sampling estimator using a shifted Exponential distribution proposal:
   $$g(y) = \lambda e^{-\lambda (y - 4.5)} \quad \text{for } y \ge 4.5$$
3. Determine the optimal parameter $\lambda^*$ and compute the variance of the resulting importance sampling estimator.

### Solution, step 1: Failure of Crude Monte Carlo
Under Crude Monte Carlo:
$$\hat{\theta}_{\text{crude}} = \frac{1}{n} \sum_{i=1}^n I(Z_i > 4.5)$$
The probability of observing a single success in $n = 100,000$ draws is:
$$\mathbb{E}[\text{Number of successes}] = n \theta = 100,000 \times 3.39767 \times 10^{-6} \approx 0.34$$
In roughly $71\%$ of all simulation runs, **zero** points will fall in the target region ($P(\text{Binomial}(10^5, \theta) = 0) = (1 - \theta)^{10^5} \approx e^{-0.34} \approx 0.712$). The Crude Monte Carlo estimator will output $\hat{\theta} = 0$, reporting that the probability is zero!

### Solution, step 2: Formulation of the Importance Sampling Estimator
The target probability is:
$$\theta = \int_{4.5}^\infty \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\,dx$$
We choose a shifted exponential proposal starting at $x_0 = 4.5$:
$$g(x) = \lambda e^{-\lambda(x - 4.5)} \quad \text{for } x \ge 4.5$$
To sample $X \sim g(x)$: draw $U \sim \mathcal{U}(0, 1)$ and set $X = 4.5 - \frac{\ln U}{\lambda}$.
The importance weight is:
$$w(x) = \frac{f(x)}{g(x)} = \frac{\frac{1}{\sqrt{2\pi}} e^{-x^2/2}}{\lambda e^{-\lambda(x - 4.5)}} = \frac{1}{\lambda \sqrt{2\pi}} \exp\left( -\frac{x^2}{2} + \lambda(x - 4.5) \right)$$
The Importance Sampling estimator is:
$$\hat{\theta}_{\text{IS}} = \frac{1}{n} \sum_{i=1}^n w(X_i)$$
Because all generated draws $X_i \ge 4.5$ automatically satisfy the condition, every single draw contributes a non-zero, informative weight!

### Solution, step 3: Optimal Parameter $\lambda^*$ and Variance
To make the importance weight $w(x)$ as close to constant as possible, we choose $\lambda$ to match the rate of decay of the normal density at the threshold $x_0 = 4.5$:
$$\frac{d}{dx} \left( -\frac{x^2}{2} \right) \Bigg|_{x = 4.5} = -4.5 \implies \lambda^* = 4.5$$
Substituting $\lambda = 4.5$:
$$w(x) = \frac{1}{4.5 \sqrt{2\pi}} \exp\left( -\frac{x^2}{2} + 4.5 x - 4.5^2 \right) = \frac{1}{4.5 \sqrt{2\pi}} \exp\left( -\frac{(x - 4.5)^2}{2} - \frac{4.5^2}{2} \right)$$
$$w(x) = \frac{e^{-4.5^2 / 2}}{4.5 \sqrt{2\pi}} \exp\left( -\frac{(x - 4.5)^2}{2} \right)$$
Notice that for all $x \ge 4.5$, the term $-\frac{(x - 4.5)^2}{2} \le 0$, which guarantees that the weight is bounded above by:
$$w(x) \le \frac{e^{-10.125}}{4.5 \sqrt{2\pi}} \approx \frac{3.996 \times 10^{-5}}{11.2798} \approx 3.54 \times 10^{-6}$$
Evaluating the second moment:
$$\mathbb{E}_g[w(X)^2] \le (3.54 \times 10^{-6}) \times \theta \approx (3.54 \times 10^{-6}) \times (3.398 \times 10^{-6}) \approx 1.20 \times 10^{-11}$$
$$\mathrm{Var}_g(w(X)) = \mathbb{E}_g[w(X)^2] - \theta^2 \approx 1.20 \times 10^{-11} - (3.398 \times 10^{-6})^2 \approx 1.20 \times 10^{-11} - 1.15 \times 10^{-11} = 5.0 \times 10^{-13}$$
For $n = 10,000$ draws, the standard error of the Importance Sampling estimate is:
$$\text{SE}(\hat{\theta}_{\text{IS}}) = \sqrt{\frac{5.0 \times 10^{-13}}{10,000}} = \sqrt{5.0 \times 10^{-17}} \approx 7.07 \times 10^{-9}$$
The relative error is:
$$\frac{\text{SE}}{\theta} \approx \frac{7.07 \times 10^{-9}}{3.398 \times 10^{-6}} \approx 0.00208 \quad (0.21\%)$$
*Conclusion*: Importance Sampling achieves an astonishing **0.21% relative error** with just 10,000 draws on a $10^{-6}$ rare event where Crude Monte Carlo failed completely!
"""

(DRAFT_DIR / "unit-5.md").write_text(u5.strip() + "\n", encoding="utf-8")
print("Unit 5 generated.")
# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
u6 = r"""# Unit 6: Markov Chain Monte Carlo (MCMC): Metropolis-Hastings Algorithms

In Bayesian statistics, statistical physics, and spatial econometrics, posterior probability distributions often involve high-dimensional parameter spaces ($\mathbf{\theta} \in \mathbb{R}^p$ where $p \ge 10$) with intractable normalizing constants:
$$\pi(\mathbf{\theta} \mid \mathbf{y}) = \frac{p(\mathbf{y} \mid \mathbf{\theta}) p(\mathbf{\theta})}{\int_{\Theta} p(\mathbf{y} \mid \mathbf{\theta}) p(\mathbf{\theta})\,d\mathbf{\theta}}$$
In high dimensions, standard rejection sampling and importance sampling fail catastrophically because the volume of the proposal density's support dwarfs the region of high target posterior density, causing acceptance rates and effective sample sizes to drop to zero.

**Markov Chain Monte Carlo (MCMC)** overcomes this limitation by constructing an ergodic Markov chain whose stationary invariant distribution is *identically equal* to the target distribution $\pi(\mathbf{\theta} \mid \mathbf{y})$. Instead of generating independent draws, MCMC produces a dependent sequence of states that explores the high-probability contours of the parameter space.

## 6.1 Markov Chain Foundations: Ergodicity and Detailed Balance

Let $\{\mathbf{X}_0, \mathbf{X}_1, \mathbf{X}_2, \dots\}$ be a discrete-time, continuous-state Markov chain defined on state space $\mathcal{X} \subseteq \mathbb{R}^p$.
The chain is governed by a **transition kernel** $P(\mathbf{x}, \mathcal{A}) = P(\mathbf{X}_{t+1} \in \mathcal{A} \mid \mathbf{X}_t = \mathbf{x})$. When the transition kernel admits a transition density $K(\mathbf{x}, \mathbf{y})$:
$$P(\mathbf{x}, d\mathbf{y}) = K(\mathbf{x}, \mathbf{y})\,d\mathbf{y} + r(\mathbf{x}) \delta_{\mathbf{x}}(d\mathbf{y})$$
where $r(\mathbf{x}) = 1 - \int K(\mathbf{x}, \mathbf{y})\,d\mathbf{y}$ is the probability of remaining at $\mathbf{x}$.

### 1. Invariance and Detailed Balance
A probability density $\pi(\mathbf{x})$ is a **stationary (invariant) distribution** for the Markov chain if:
$$\pi(\mathbf{y}) = \int_{\mathcal{X}} \pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y})\,d\mathbf{x} \quad \text{for all } \mathbf{y} \in \mathcal{X}$$

A sufficient (though not strictly necessary) condition for $\pi(\mathbf{x})$ to be stationary is the **Detailed Balance (Reversibility)** condition:

$$\pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x}) \quad \text{for all } \mathbf{x}, \mathbf{y} \in \mathcal{X}$$

*Proof that Detailed Balance Implies Invariance*:
Integrating both sides of detailed balance with respect to $\mathbf{x}$:
$$\int_{\mathcal{X}} \pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y})\,d\mathbf{x} = \int_{\mathcal{X}} \pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x})\,d\mathbf{x} = \pi(\mathbf{y}) \int_{\mathcal{X}} K(\mathbf{y}, \mathbf{x})\,d\mathbf{x}$$
Since $K(\mathbf{y}, \mathbf{x})$ is a probability density integrating to 1 over $\mathcal{X}$:
$$\int_{\mathcal{X}} \pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y})\,d\mathbf{x} = \pi(\mathbf{y}) \cdot 1 = \pi(\mathbf{y})$$
Thus, detailed balance guarantees that $\pi(\mathbf{x})$ is the stationary distribution of the chain.

### 2. Ergodicity and the Ergodic Theorem
A Markov chain is **ergodic** if it is:
1. **$\pi$-irreducible**: Every Borel set $\mathcal{A}$ with $\pi(\mathcal{A}) > 0$ can be reached from any starting state in a finite number of steps.
2. **Aperiodic**: The chain does not cycle deterministically between disjoint partitions.
3. **Harris recurrent**: The chain revisits every non-negligible region infinitely often with probability 1.

*Theorem (The Ergodic Theorem / Strong Law for MCMC)*: If a Markov chain $\{\mathbf{X}_t\}$ is ergodic with stationary distribution $\pi$, then for any integrable function $h: \mathcal{X} \to \mathbb{R}$ ($\mathbb{E}_\pi[|h|] < \infty$), the empirical trajectory average converges almost surely to the true expectation:

$$\lim_{N \to \infty} \frac{1}{N} \sum_{t=1}^N h(\mathbf{X}_t) = \mathbb{E}_\pi[h(\mathbf{X})] \quad \text{almost surely}$$
regardless of the initial starting state $\mathbf{X}_0$.

## 6.2 The Metropolis-Hastings Algorithm

In 1953, Nicholas Metropolis, Arianna Rosenbluth, Marshall Rosenbluth, Augusta Teller, and Edward Teller published the seminal Metropolis algorithm for symmetric proposals. In 1970, W. K. Hastings generalized the algorithm to arbitrary, non-symmetric proposal distributions.

### The Metropolis-Hastings Algorithm Mechanics
Let $\pi(\mathbf{x}) = \frac{\tilde{\pi}(\mathbf{x})}{Z}$ be the target probability density, where the normalizing constant $Z$ is unknown.
Let $q(\mathbf{y} \mid \mathbf{x})$ be a candidate **proposal distribution** specifying the probability density of proposing a move from current state $\mathbf{x}$ to candidate state $\mathbf{y}$.

Given current state $\mathbf{X}_t = \mathbf{x}$:
1. **Propose Candidate**: Draw a candidate state $\mathbf{Y} \sim q(\mathbf{y} \mid \mathbf{x})$.
2. **Compute Acceptance Probability**:
   $$\alpha(\mathbf{x}, \mathbf{Y}) = \min\left( 1, \; \frac{\pi(\mathbf{Y}) q(\mathbf{x} \mid \mathbf{Y})}{\pi(\mathbf{x}) q(\mathbf{Y} \mid \mathbf{x})} \right) = \min\left( 1, \; \frac{\tilde{\pi}(\mathbf{Y}) q(\mathbf{x} \mid \mathbf{Y})}{\tilde{\pi}(\mathbf{x}) q(\mathbf{Y} \mid \mathbf{x})} \right)$$
   Notice that the intractable normalizing constant $Z$ cancels out identically in the ratio $\frac{\tilde{\pi}(\mathbf{Y})/Z}{\tilde{\pi}(\mathbf{x})/Z}$!
3. **Acceptance Step**:
   - Draw $U \sim \mathcal{U}(0, 1)$.
   - If $U \le \alpha(\mathbf{x}, \mathbf{Y})$, **accept** the proposal: $\mathbf{X}_{t+1} = \mathbf{Y}$.
   - Otherwise, **reject** the proposal: $\mathbf{X}_{t+1} = \mathbf{x}$ (the chain remains at the current state).

### Proof of Detailed Balance
The effective transition density for a move from $\mathbf{x} \ne \mathbf{y}$ is:
$$K(\mathbf{x}, \mathbf{y}) = q(\mathbf{y} \mid \mathbf{x}) \alpha(\mathbf{x}, \mathbf{y})$$
Assume without loss of generality that $\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \le \pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})$.
Then:
$$\alpha(\mathbf{x}, \mathbf{y}) = \frac{\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})}{\pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})}, \quad \text{while} \quad \alpha(\mathbf{y}, \mathbf{x}) = 1$$
We evaluate the forward probability flow:
$$\pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x}) \left( \frac{\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})}{\pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})} \right) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})$$
We evaluate the reverse probability flow:
$$\pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x}) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \alpha(\mathbf{y}, \mathbf{x}) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \cdot 1 = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})$$
Both flows are strictly equal:
$$\pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y}) \equiv \pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x})$$
Detailed balance holds exactly.

## 6.3 Proposal Mechanisms and the 0.234 Optimal Tuning Rule

The statistical performance and mixing speed of Metropolis-Hastings depends critically on the proposal density $q(\mathbf{y} \mid \mathbf{x})$.

### 1. Random-Walk Metropolis-Hastings
The candidate is generated by adding a zero-mean random perturbation $\mathbf{\epsilon}$ to the current state:
$$\mathbf{Y} = \mathbf{x} + \mathbf{\epsilon}, \quad \mathbf{\epsilon} \sim g(\mathbf{\epsilon})$$
where $g(\mathbf{\epsilon})$ is symmetric ($g(\mathbf{\epsilon}) = g(-\mathbf{\epsilon})$), such as a Gaussian $\mathcal{N}(\mathbf{0}, \sigma_{\text{prop}}^2 \mathbf{I})$.
Because $q(\mathbf{y} \mid \mathbf{x}) = g(\mathbf{y} - \mathbf{x}) = g(\mathbf{x} - \mathbf{y}) = q(\mathbf{x} \mid \mathbf{y})$, the proposal ratio cancels to 1:
$$\alpha(\mathbf{x}, \mathbf{y}) = \min\left( 1, \; \frac{\pi(\mathbf{y})}{\pi(\mathbf{x})} \right)$$
This recovers the original **Metropolis Algorithm**.

**The Proposal Scale Dilemma**:
- If proposal scale $\sigma_{\text{prop}}$ is **too small**: Candidates $\mathbf{y}$ are close to $\mathbf{x}$, resulting in very high acceptance ($\alpha \approx 100\%$), but the chain moves via minuscule Brownian diffusion, taking millions of iterations to traverse the target distribution (high autocorrelation, poor mixing).
- If proposal scale $\sigma_{\text{prop}}$ is **too large**: Candidates land in low-probability tail regions where $\pi(\mathbf{y}) \ll \pi(\mathbf{x})$, resulting in near-zero acceptance ($\alpha \approx 0\%$). The chain gets stuck at the same state for thousands of iterations.

### 2. The Roberts-Gelman-Gilks Optimal Scaling Rule (0.234)
In 1997, Gareth Roberts, Andrew Gelman, and Walter Gilks published a foundational asymptotic theorem:
*Theorem (Roberts, Gelman, & Gilks, 1997)*: For an i.i.d. target distribution in $d$-dimensional Euclidean space $\mathbb{R}^d$ as $d \to \infty$, the optimal proposal standard deviation that maximizes the speed of diffusion of the Markov chain scales as:
$$\sigma_{\text{prop}}^* \approx \frac{2.38}{\sqrt{d}} \sigma_{\text{target}}$$
Under this optimal scaling, the asymptotic average acceptance rate converges to:

$$\alpha^* \approx 0.234 \quad (23.4\%)$$

For 1-dimensional targets, the optimal acceptance rate is approximately $44\%$; for $d \ge 5$ dimensions, tuning the proposal variance to maintain an acceptance rate between **$20\%$ and $25\%$** provides optimal mixing.

## 6.4 MCMC Convergence Diagnostics

Because MCMC samples are auto-correlated and depend on the initial arbitrary starting state $\mathbf{X}_0$, analysts must determine when the chain has reached stationarity (the **burn-in period**) and assess the precision of trajectory estimates.

### 1. Burn-In and Trace Plots
- **Burn-In Period ($B$)**: Early iterations ($t = 1, \dots, B$) generated while the chain travels from the starting point $\mathbf{X}_0$ toward the mode of $\pi$ are discarded:
  $$\hat{\theta} = \frac{1}{N - B} \sum_{t=B+1}^N h(\mathbf{X}_t)$$
- **Trace Plots**: Plotting state values $X_t$ against iteration number $t$. A healthy chain exhibits a "hairy caterpillar" appearance, oscillating rapidly without secular drift.

### 2. Autocorrelation and Effective Sample Size (ESS)
Due to positive serial correlation $\rho_k = \mathrm{Corr}(X_t, X_{t+k})$, the variance of the sample mean is inflated by the **Integrated Autocorrelation Time (IACT)**:
$$\tau = 1 + 2 \sum_{k=1}^\infty \rho_k$$
$$\mathrm{Var}(\hat{\theta}) \approx \frac{\sigma^2}{N} \tau$$
The **Effective Sample Size (ESS)** represents the number of equivalent independent draws:

$$\text{ESS} = \frac{N}{\tau} = \frac{N}{1 + 2 \sum_{k=1}^\infty \rho_k}$$

If $N = 10,000$ and $\tau = 20$, the chain contains only $\text{ESS} = 500$ independent pieces of statistical information.

### 3. The Gelman-Rubin Diagnostic ($\hat{R}$)
Andrew Gelman and Donald Rubin (1992) introduced the standard multi-chain convergence metric:
- Run $M \ge 3$ parallel chains with overdispersed initial values for $N$ iterations.
- Compute the **Between-Chain Variance** $B / N$ and **Within-Chain Variance** $W$.
- The estimated marginal posterior variance is:
  $$\hat{V} = \frac{N - 1}{N} W + \frac{M + 1}{M \cdot N} B$$
- The **Potential Scale Reduction Factor (PSRF)** is:
  $$\hat{R} = \sqrt{\frac{\hat{V}}{W}}$$
At convergence, between-chain variance vanishes, and $\hat{R} \to 1.0$. As a regulatory and scientific convention, convergence is diagnosed when:
$$\hat{R} < 1.05 \quad (\text{or } \hat{R} < 1.01 \text{ for rigorous clinical trials})$$

## Fully worked question 1: Random-Walk Metropolis on an Unnormalized Mixture

### Question
An astronomer models stellar brightness using an unnormalized bimodal Gaussian mixture density:
$$\tilde{\pi}(x) = 0.40 \exp\left( -\frac{(x + 2)^2}{2} \right) + 0.60 \exp\left( -\frac{(x - 3)^2}{4} \right) \quad \text{for } x \in \mathbb{R}$$
The astronomer runs a Random-Walk Metropolis algorithm with Gaussian proposal:
$$Y \sim \mathcal{N}(x_t, \sigma_{\text{prop}}^2 = 1.0)$$
The chain is currently at state $x_0 = 1.0$.
1. Compute the unnormalized target density at current state $\tilde{\pi}(1.0)$.
2. A random draw from the proposal distribution yields candidate $Y = 2.20$.
   - Compute the unnormalized target density $\tilde{\pi}(2.20)$.
   - Calculate the exact Metropolis acceptance probability $\alpha(1.0, 2.20)$.
3. Given a uniform draw $u = 0.750$, determine whether the candidate is accepted or rejected, and specify state $x_1$.

### Solution, step 1: Evaluation of Current State Density $\tilde{\pi}(1.0)$
The target function is:
$$\tilde{\pi}(x) = 0.40 e^{-(x + 2)^2 / 2} + 0.60 e^{-(x - 3)^2 / 4}$$
Evaluating at $x_0 = 1.0$:
- Term 1:
  $$(x + 2)^2 = (1.0 + 2)^2 = 3^2 = 9 \implies -\frac{9}{2} = -4.5$$
  $$e^{-4.5} \approx 0.011109 \implies 0.40 \times 0.011109 \approx 0.004444$$
- Term 2:
  $$(x - 3)^2 = (1.0 - 3)^2 = (-2)^2 = 4 \implies -\frac{4}{4} = -1.0$$
  $$e^{-1.0} \approx 0.367879 \implies 0.60 \times 0.367879 \approx 0.220728$$

Summing the terms:
$$\tilde{\pi}(1.0) = 0.004444 + 0.220728 = 0.225172$$

### Solution, step 2: Candidate Density $\tilde{\pi}(2.20)$ and Acceptance Probability
Evaluating at candidate $Y = 2.20$:
- Term 1:
  $$(x + 2)^2 = (2.20 + 2)^2 = 4.20^2 = 17.64 \implies -\frac{17.64}{2} = -8.82$$
  $$e^{-8.82} \approx 0.0001477 \implies 0.40 \times 0.0001477 \approx 0.000059$$
- Term 2:
  $$(x - 3)^2 = (2.20 - 3)^2 = (-0.80)^2 = 0.64 \implies -\frac{0.64}{4} = -0.16$$
  $$e^{-0.16} \approx 0.852144 \implies 0.60 \times 0.852144 \approx 0.511286$$

Summing the terms:
$$\tilde{\pi}(2.20) = 0.000059 + 0.511286 = 0.511345$$

Because the proposal is symmetric (Gaussian random walk, $q(y|x) = q(x|y)$):
$$\alpha(1.0, 2.20) = \min\left( 1, \; \frac{\tilde{\pi}(2.20)}{\tilde{\pi}(1.0)} \right) = \min\left( 1, \; \frac{0.511345}{0.225172} \right)$$
$$\frac{0.511345}{0.225172} \approx 2.2709$$
Since the ratio exceeds 1.0:
$$\alpha(1.0, 2.20) = 1.0000 \quad (100\%)$$
The proposed move is toward a state of higher probability density, so it is accepted deterministically.

### Solution, step 3: Evaluation of Acceptance Step
The uniform filter draw is $u = 0.750$.
Comparing $u \le \alpha$:
$$u = 0.750 \le 1.0000$$
The move is **accepted**!
The new state of the Markov chain is:
$$x_1 = 2.20$$

## Fully worked question 2: Independence Metropolis-Hastings with Asymmetric Proposal

### Question
A Bayesian statistician samples an unnormalized target posterior density:
$$\tilde{\pi}(x) = x^3 e^{-x} \quad \text{for } x > 0 \quad (\text{a Gamma}(4, 1) \text{ distribution})$$
using an **Independence Metropolis-Hastings sampler** with exponential proposal:
$$q(y \mid x) = g(y) = \frac{1}{3} e^{-y / 3} \quad \text{for } y > 0 \quad (\text{an Exp}(\lambda = 1/3) \text{ distribution})$$
The chain is currently at state $x_t = 3.0$.
1. A candidate is drawn from the proposal distribution: $Y = 6.0$.
   Formulate the exact Metropolis-Hastings acceptance ratio:
   $$\rho(x, y) = \frac{\tilde{\pi}(y) q(x \mid y)}{\tilde{\pi}(x) q(y \mid x)}$$
2. Calculate the acceptance probability $\alpha(3.0, 6.0)$ to 4 decimal places.
3. If the candidate had been $Y = 0.50$, compute the corresponding acceptance probability $\alpha(3.0, 0.50)$.

### Solution, step 1: Algebraic Formulation of the Acceptance Ratio
For an independence sampler, $q(y \mid x) = g(y)$ and $q(x \mid y) = g(x)$.
The ratio is:
$$\rho(x, y) = \frac{\tilde{\pi}(y) g(x)}{\tilde{\pi}(x) g(y)} = \frac{y^3 e^{-y} \cdot \frac{1}{3} e^{-x/3}}{x^3 e^{-x} \cdot \frac{1}{3} e^{-y/3}} = \left( \frac{y}{x} \right)^3 \frac{e^{-y + x/3}}{e^{-x + y/3}} = \left( \frac{y}{x} \right)^3 \exp\left( -(y - x) + \frac{1}{3}(x - y) \right)$$
$$\rho(x, y) = \left( \frac{y}{x} \right)^3 \exp\left( -\frac{4}{3}(y - x) \right)$$

### Solution, step 2: Calculation for $x = 3.0$ and $Y = 6.0$
Given $x = 3.0$ and $y = 6.0$:
- Coordinate ratio:
  $$\frac{y}{x} = \frac{6.0}{3.0} = 2.0 \implies \left( \frac{y}{x} \right)^3 = 2.0^3 = 8.0$$
- Coordinate difference:
  $$y - x = 6.0 - 3.0 = +3.0$$
  $$-\frac{4}{3}(y - x) = -\frac{4}{3} \times 3.0 = -4.0$$
- Exponential factor:
  $$e^{-4.0} \approx 0.0183156$$

The acceptance ratio is:
$$\rho(3.0, 6.0) = 8.0 \times 0.0183156 \approx 0.146525$$
The acceptance probability is:
$$\alpha(3.0, 6.0) = \min(1, \; 0.146525) \approx 0.1465 \quad (14.65\%)$$

### Solution, step 3: Calculation for $x = 3.0$ and $Y = 0.50$
Given $x = 3.0$ and $y = 0.50$:
- Coordinate ratio:
  $$\frac{y}{x} = \frac{0.50}{3.0} = \frac{1}{6} \implies \left( \frac{y}{x} \right)^3 = \frac{1}{216} \approx 0.0046296$$
- Coordinate difference:
  $$y - x = 0.50 - 3.0 = -2.50$$
  $$-\frac{4}{3}(y - x) = -\frac{4}{3} \times (-2.50) = +\frac{10}{3} \approx +3.33333$$
- Exponential factor:
  $$e^{10/3} \approx e^{3.33333} \approx 28.0316$$

The acceptance ratio is:
$$\rho(3.0, 0.50) = \frac{1}{216} \times 28.0316 \approx 0.129776$$
The acceptance probability is:
$$\alpha(3.0, 0.50) = \min(1, \; 0.129776) \approx 0.1298 \quad (12.98\%)$$

*Insight*: The independence sampler penalizes candidate proposals in both tails because the proposal density $g(y) = \frac{1}{3} e^{-y/3}$ fails to match the Gamma shape ($y^3 e^{-y}$), demonstrating why proposal matching is vital.

## Fully worked question 3: Effective Sample Size and Gelman-Rubin Convergence Diagnostic

### Question
Two parallel MCMC chains ($M = 2$) are run to estimate a posterior parameter $\theta$.
Each chain is run for $N = 1,000$ iterations after discarding burn-in:
- **Chain 1**: Sample mean $\bar{X}_1 = 10.40$, sample variance $s_1^2 = 4.20$.
- **Chain 2**: Sample mean $\bar{X}_2 = 10.80$, sample variance $s_2^2 = 4.60$.
- The estimated lag-1 autocorrelation within chains is $\hat{\rho}_1 = 0.70$, with negligible higher-order autocorrelations ($\hat{\rho}_k \approx 0$ for $k \ge 2$).

1. Compute the Within-Chain Variance $W$, Between-Chain Variance $B$, and the Gelman-Rubin diagnostic $\hat{R}$.
2. Determine whether the chains have successfully achieved convergence according to the standard threshold $\hat{R} < 1.05$.
3. Compute the Effective Sample Size (ESS) for a combined sample of $2,000$ draws.

### Solution, step 1: Computation of Within and Between Variances and $\hat{R}$
Let $M = 2$ chains of length $N = 1,000$.
1. **Within-Chain Variance ($W$)**:
   $$W = \frac{1}{M} \sum_{m=1}^M s_m^2 = \frac{s_1^2 + s_2^2}{2} = \frac{4.20 + 4.60}{2} = \frac{8.80}{2} = 4.40$$

2. **Overall Mean**:
   $$\bar{X} = \frac{\bar{X}_1 + \bar{X}_2}{2} = \frac{10.40 + 10.80}{2} = 10.60$$

3. **Between-Chain Variance ($B$)**:
   $$\frac{B}{N} = \frac{1}{M - 1} \sum_{m=1}^M (\bar{X}_m - \bar{X})^2 = (10.40 - 10.60)^2 + (10.80 - 10.60)^2 = (-0.20)^2 + (0.20)^2 = 0.04 + 0.04 = 0.08$$
   $$B = N \times 0.08 = 1,000 \times 0.08 = 80.0$$

4. **Pooled Marginal Posterior Variance ($\hat{V}$)**:
   $$\hat{V} = \frac{N - 1}{N} W + \frac{M + 1}{M \cdot N} B = \frac{999}{1000} (4.40) + \frac{3}{2 \times 1000} (80.0)$$
   $$\hat{V} = (0.999 \times 4.40) + (0.0015 \times 80.0) = 4.3956 + 0.1200 = 4.5156$$

5. **Gelman-Rubin Statistic ($\hat{R}$)**:
   $$\hat{R} = \sqrt{\frac{\hat{V}}{W}} = \sqrt{\frac{4.5156}{4.40}} = \sqrt{1.02627} \approx 1.01305 \approx 1.013$$

### Solution, step 2: Convergence Assessment
The calculated potential scale reduction factor is:
$$\hat{R} = 1.013$$
Since $\hat{R} = 1.013 < 1.05$ (and even satisfies the ultra-strict threshold $\hat{R} < 1.02$), between-chain variation is negligible compared to within-chain variation. The chains have successfully converged to a common stationary posterior distribution.

### Solution, step 3: Calculation of Effective Sample Size (ESS)
Given lag-1 autocorrelation $\hat{\rho}_1 = 0.70$ and $\hat{\rho}_k \approx 0$ for $k \ge 2$:
The integrated autocorrelation time is:
$$\tau \approx 1 + 2 \hat{\rho}_1 = 1 + 2(0.70) = 1 + 1.40 = 2.40$$

For the combined simulation sample of $N_{\text{total}} = M \times N = 2 \times 1,000 = 2,000$ draws:
$$\text{ESS} = \frac{N_{\text{total}}}{\tau} = \frac{2,000}{2.40} = \frac{2,000}{2.4} \approx 833.3 \approx 833 \text{ independent draws}$$
Even though $2,000$ correlated iterations were executed, the statistical precision of the posterior mean estimate is equivalent to only $833$ independent Monte Carlo draws.
"""

(DRAFT_DIR / "unit-6.md").write_text(u6.strip() + "\n", encoding="utf-8")
print("Unit 6 generated.")
# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
u7 = r"""# Unit 7: The Gibbs Sampler & Bayesian Computational Inference

In multi-parameter Bayesian inference, designing a joint proposal distribution $q(\mathbf{\theta}^* \mid \mathbf{\theta})$ that explores a complex, correlated high-dimensional parameter space efficiently via standard Metropolis-Hastings can be extraordinarily difficult. In 1984, Stuart and Donald Geman introduced the **Gibbs Sampler** in the context of spatial image processing (named after physicist Josiah Willard Gibbs). In 1990, Alan Gelfand and Adrian Smith demonstrated that the Gibbs sampler provides a universal computational engine for estimating complex Bayesian models.

Instead of proposing simultaneous moves for all $p$ parameters at once, the Gibbs sampler updates the parameters **one variable at a time** (or one block at a time) by sampling directly from the **full conditional posterior distribution** of each parameter given the current values of all other parameters and the observed data.

## 7.1 Mechanics of the Gibbs Sampler: Systematic and Random Scan

Let $\mathbf{\theta} = (\theta_1, \theta_2, \dots, \theta_p)^T \in \Theta$ be a parameter vector with joint posterior distribution $\pi(\mathbf{\theta} \mid \mathbf{y})$.
Let $\mathbf{\theta}_{-j} = (\theta_1, \dots, \theta_{j-1}, \theta_{j+1}, \dots, \theta_p)^T$ denote the subvector of all parameters excluding $\theta_j$.

The **Full Conditional Distribution** of parameter $\theta_j$ is the conditional distribution of $\theta_j$ given all remaining parameters and the data:
$$\pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) = \frac{\pi(\theta_1, \dots, \theta_p \mid \mathbf{y})}{\int \pi(\theta_1, \dots, \theta_j^*, \dots, \theta_p \mid \mathbf{y})\,d\theta_j^*} \propto \pi(\mathbf{\theta} \mid \mathbf{y})$$

### 1. The Systematic Scan Gibbs Sampler
Given an initial state $\mathbf{\theta}^{(0)} = (\theta_1^{(0)}, \dots, \theta_p^{(0)})^T$, iteration $t+1$ executes a deterministic sweep through all $p$ coordinates:
1. Sample $\theta_1^{(t+1)} \sim \pi(\theta_1 \mid \theta_2^{(t)}, \theta_3^{(t)}, \dots, \theta_p^{(t)}, \mathbf{y})$.
2. Sample $\theta_2^{(t+1)} \sim \pi(\theta_2 \mid \theta_1^{(t+1)}, \theta_3^{(t)}, \dots, \theta_p^{(t)}, \mathbf{y})$.
   $\dots$
$j$. Sample $\theta_j^{(t+1)} \sim \pi(\theta_j \mid \theta_1^{(t+1)}, \dots, \theta_{j-1}^{(t+1)}, \theta_{j+1}^{(t)}, \dots, \theta_p^{(t)}, \mathbf{y})$.
   $\dots$
$p$. Sample $\theta_p^{(t+1)} \sim \pi(\theta_p \mid \theta_1^{(t+1)}, \dots, \theta_{p-1}^{(t+1)}, \mathbf{y})$.

Notice that as each new parameter $\theta_j^{(t+1)}$ is drawn, it is immediately used in the conditioning sets of all subsequent updates within the same iteration.

### 2. The Gibbs Sampler as Metropolis-Hastings with Acceptance $\alpha \equiv 1$
A profound theoretical insight is that the Gibbs sampler is mathematically equivalent to a multi-stage Metropolis-Hastings algorithm where the acceptance probability is **identically 100%**:

*Theorem*: Consider updating coordinate $j$ using candidate proposal $q(\mathbf{\theta}^* \mid \mathbf{\theta}) = \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \cdot I(\mathbf{\theta}_{-j}^* = \mathbf{\theta}_{-j})$.
The Metropolis-Hastings acceptance ratio is:
$$\alpha(\mathbf{\theta}, \mathbf{\theta}^*) = \min\left( 1, \; \frac{\pi(\mathbf{\theta}^* \mid \mathbf{y}) q(\mathbf{\theta} \mid \mathbf{\theta}^*)}{\pi(\mathbf{\theta} \mid \mathbf{y}) q(\mathbf{\theta}^* \mid \mathbf{\theta})} \right)$$
By definition of conditional probability:
$$\pi(\mathbf{\theta}^* \mid \mathbf{y}) = \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y})$$
$$\pi(\mathbf{\theta} \mid \mathbf{y}) = \pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y})$$
Substituting into the acceptance ratio:
$$\frac{\pi(\mathbf{\theta}^* \mid \mathbf{y}) q(\mathbf{\theta} \mid \mathbf{\theta}^*)}{\pi(\mathbf{\theta} \mid \mathbf{y}) q(\mathbf{\theta}^* \mid \mathbf{\theta})} = \frac{\left[ \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y}) \right] \left[ \pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) \right]}{\left[ \pi(\theta_j \mid \mathbf{\theta}_{-j}, \mathbf{y}) \pi(\mathbf{\theta}_{-j} \mid \mathbf{y}) \right] \left[ \pi(\theta_j^* \mid \mathbf{\theta}_{-j}, \mathbf{y}) \right]} \equiv 1$$
Every single candidate draw is accepted with probability $\alpha \equiv 1.0$! Zero proposals are rejected.

## 7.2 Data Augmentation and Latent Variable Models

In many statistical models, the observed data likelihood $p(\mathbf{y} \mid \mathbf{\theta})$ is analytically intractable, but the complete data likelihood $p(\mathbf{y}, \mathbf{z} \mid \mathbf{\theta})$ involving unobserved **latent variables** $\mathbf{z}$ is simple and conjugate. In 1987, Martin Tanner and Wing Hung Wong formulated the **Data Augmentation Framework**.

### The Tanner-Wong Two-Step Iteration
1. **Imputation Step (I-Step)**: Sample the missing latent variables from their predictive distribution given current parameters:
   $$\mathbf{z}^{(t+1)} \sim p(\mathbf{z} \mid \mathbf{y}, \mathbf{\theta}^{(t)})$$
2. **Posterior Step (P-Step)**: Sample the parameters from their complete-data posterior distribution given augmented data:
   $$\mathbf{\theta}^{(t+1)} \sim p(\mathbf{\theta} \mid \mathbf{y}, \mathbf{z}^{(t+1)})$$
As $t \to \infty$, the marginal sequence $\{\mathbf{\theta}^{(t)}\}$ converges in distribution to the exact observed posterior $\pi(\mathbf{\theta} \mid \mathbf{y})$.

### The Albert-Chib Algorithm for Bayesian Probit Regression
Consider a binary probit regression model where observed responses $y_i \in \{0, 1\}$ follow:
$$P(y_i = 1 \mid \mathbf{x}_i, \mathbf{\beta}) = \Phi(\mathbf{x}_i^T \mathbf{\beta})$$
The likelihood function $\prod_{i=1}^n \Phi(\mathbf{x}_i^T \mathbf{\beta})^{y_i} [1 - \Phi(\mathbf{x}_i^T \mathbf{\beta})]^{1 - y_i}$ is non-conjugate with respect to a Gaussian prior $\mathbf{\beta} \sim \mathcal{N}(\mathbf{\beta}_0, \mathbf{\Sigma}_0)$.

In 1993, James Albert and Siddhartha Chib introduced continuous latent variables $Z_i \sim \mathcal{N}(\mathbf{x}_i^T \mathbf{\beta}, 1)$ such that:
$$y_i = \begin{cases} 1 & \text{if } Z_i > 0 \\ 0 & \text{if } Z_i \le 0 \end{cases}$$

Under this formulation, the full conditionals are analytically tractable standard distributions:
1. **Update Latent Variables**: For each $i = 1, \dots, n$:
   - If $y_i = 1$, sample $Z_i \sim \mathcal{N}(\mathbf{x}_i^T \mathbf{\beta}, 1)$ truncated to the positive interval $(0, \infty)$.
   - If $y_i = 0$, sample $Z_i \sim \mathcal{N}(\mathbf{x}_i^T \mathbf{\beta}, 1)$ truncated to the negative interval $(-\infty, 0]$.
2. **Update Regression Coefficients**: Conditional on continuous vector $\mathbf{Z} = (Z_1, \dots, Z_n)^T$, the model is standard linear regression $\mathbf{Z} = \mathbf{X}\mathbf{\beta} + \mathbf{\epsilon}$ with $\mathbf{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$. With prior $\mathbf{\beta} \sim \mathcal{N}(\mathbf{\beta}_0, \mathbf{\Sigma}_0)$:
   $$\mathbf{\beta} \mid \mathbf{Z}, \mathbf{y} \sim \mathcal{N}\left( (\mathbf{\Sigma}_0^{-1} + \mathbf{X}^T\mathbf{X})^{-1} (\mathbf{\Sigma}_0^{-1}\mathbf{\beta}_0 + \mathbf{X}^T\mathbf{Z}), \; (\mathbf{\Sigma}_0^{-1} + \mathbf{X}^T\mathbf{X})^{-1} \right)$$
The Albert-Chib sampler transforms non-linear categorical inference into linear Gaussian updates.

## 7.3 Gibbs Sampling for Bayesian Multiple Linear Regression

Consider the classical multiple linear regression model:
$$\mathbf{y} = \mathbf{X}\mathbf{\beta} + \mathbf{\epsilon}, \quad \mathbf{\epsilon} \sim \mathcal{N}_n(\mathbf{0}, \sigma^2 \mathbf{I}_n)$$
where $\mathbf{y} \in \mathbb{R}^n$ is the response vector, $\mathbf{X} \in \mathbb{R}^{n \times p}$ is the design matrix, $\mathbf{\beta} \in \mathbb{R}^p$ is the regression coefficient vector, and $\sigma^2 > 0$ is the residual variance.

We place independent semi-conjugate priors on $\mathbf{\beta}$ and $\sigma^2$:
- $\mathbf{\beta} \sim \mathcal{N}_p(\mathbf{\beta}_0, \mathbf{\Sigma}_0)$ (Gaussian prior).
- $\sigma^2 \sim \text{Inverse-Gamma}(a_0, b_0)$ with density $p(\sigma^2) \propto (\sigma^2)^{-(a_0 + 1)} \exp(-b_0 / \sigma^2)$.

### The Full Conditional Posterior Distributions
1. **Full Conditional of $\mathbf{\beta}$ given $\sigma^2$ and $\mathbf{y}$**:
   $$\mathbf{\beta} \mid \sigma^2, \mathbf{y} \sim \mathcal{N}_p(\mathbf{\beta}_n, \mathbf{\Sigma}_n)$$
   where:
   $$\mathbf{\Sigma}_n = \left( \mathbf{\Sigma}_0^{-1} + \frac{1}{\sigma^2} \mathbf{X}^T \mathbf{X} \right)^{-1}$$
   $$\mathbf{\beta}_n = \mathbf{\Sigma}_n \left( \mathbf{\Sigma}_0^{-1} \mathbf{\beta}_0 + \frac{1}{\sigma^2} \mathbf{X}^T \mathbf{y} \right)$$
2. **Full Conditional of $\sigma^2$ given $\mathbf{\beta}$ and $\mathbf{y}$**:
   $$\sigma^2 \mid \mathbf{\beta}, \mathbf{y} \sim \text{Inverse-Gamma}(a_n, b_n)$$
   where:
   $$a_n = a_0 + \frac{n}{2}$$
   $$b_n = b_0 + \frac{1}{2} (\mathbf{y} - \mathbf{X}\mathbf{\beta})^T (\mathbf{y} - \mathbf{X}\mathbf{\beta}) = b_0 + \frac{1}{2} \sum_{i=1}^n (y_i - \mathbf{x}_i^T\mathbf{\beta})^2$$

The Gibbs sampler alternates between drawing $\mathbf{\beta}^{(t+1)} \sim \mathcal{N}_p(\mathbf{\beta}_n, \mathbf{\Sigma}_n)$ using Cholesky factorization and drawing $\sigma^{2(t+1)} \sim \text{Inverse-Gamma}(a_n, b_n)$ via inverted Gamma sampling.

## Fully worked question 1: Gibbs Sampling for a Bivariate Gaussian Distribution

### Question
A bivariate target distribution is a zero-mean Gaussian vector $(X, Y)^T \sim \mathcal{N}_2(\mathbf{0}, \mathbf{\Sigma})$ with unit variances $\sigma_X^2 = \sigma_Y^2 = 1.0$ and correlation coefficient $\rho = 0.80$:
$$\mathbf{\Sigma} = \begin{pmatrix} 1.0 & 0.80 \\ 0.80 & 1.0 \end{pmatrix}$$
1. Derive the full conditional distributions $X \mid Y = y$ and $Y \mid X = x$.
2. Starting from initial state $(x_0, y_0) = (2.0, 2.0)$, execute two complete iterations of the systematic scan Gibbs sampler using the following standard normal draws:
   - For $x_1$: $z_{x1} = -0.50$.
   - For $y_1$: $z_{y1} = +0.25$.
   - For $x_2$: $z_{x2} = +1.10$.
   - For $y_2$: $z_{y2} = -0.40$.
3. Compute the lag-1 autocorrelation between successive states of $X$ in the Gibbs sequence.

### Solution, step 1: Derivation of the Full Conditional Distributions
For a bivariate normal vector with means 0, unit variances, and correlation $\rho$:
- The conditional distribution of $X$ given $Y = y$ is univariate Gaussian:
  $$X \mid Y = y \sim \mathcal{N}\left( \rho y, \; 1 - \rho^2 \right)$$
- Symmetrically:
  $$Y \mid X = x \sim \mathcal{N}\left( \rho x, \; 1 - \rho^2 \right)$$
Given $\rho = 0.80$:
$$\rho^2 = 0.80^2 = 0.64 \implies 1 - \rho^2 = 1 - 0.64 = 0.36$$
$$\sigma_{\text{cond}} = \sqrt{1 - \rho^2} = \sqrt{0.36} = 0.60$$
Thus, the sampling rules are:
$$X \mid Y = y \sim \mathcal{N}(0.80 y, \; 0.60^2) \implies X = 0.80 y + 0.60 Z_X$$
$$Y \mid X = x \sim \mathcal{N}(0.80 x, \; 0.60^2) \implies Y = 0.80 x + 0.60 Z_Y$$

### Solution, step 2: Execution of Two Gibbs Iterations
Starting state: $x_0 = 2.0, y_0 = 2.0$.

- **Iteration 1**:
  1. Sample $x_1 \sim \mathcal{N}(0.80 y_0, 0.60^2)$ using $z_{x1} = -0.50$:
     $$\mu_{x1} = 0.80 \times 2.0 = 1.60$$
     $$x_1 = 1.60 + 0.60 \times (-0.50) = 1.60 - 0.30 = 1.30$$
  2. Sample $y_1 \sim \mathcal{N}(0.80 x_1, 0.60^2)$ using new $x_1 = 1.30$ and $z_{y1} = +0.25$:
     $$\mu_{y1} = 0.80 \times 1.30 = 1.04$$
     $$y_1 = 1.04 + 0.60 \times (+0.25) = 1.04 + 0.15 = 1.19$$
  *State after Iteration 1*: $(x_1, y_1) = (1.30, 1.19)$.

- **Iteration 2**:
  1. Sample $x_2 \sim \mathcal{N}(0.80 y_1, 0.60^2)$ using $y_1 = 1.19$ and $z_{x2} = +1.10$:
     $$\mu_{x2} = 0.80 \times 1.19 = 0.952$$
     $$x_2 = 0.952 + 0.60 \times (+1.10) = 0.952 + 0.660 = 1.612$$
  2. Sample $y_2 \sim \mathcal{N}(0.80 x_2, 0.60^2)$ using new $x_2 = 1.612$ and $z_{y2} = -0.40$:
     $$\mu_{y2} = 0.80 \times 1.612 = 1.2896$$
     $$y_2 = 1.2896 + 0.60 \times (-0.40) = 1.2896 - 0.2400 = 1.0496$$
  *State after Iteration 2*: $(x_2, y_2) = (1.612, 1.050)$.

### Solution, step 3: Lag-1 Autocorrelation of the Sequence
Notice the recurrence relation for the $X$ sequence across full iterations:
$$X_{t+1} = \rho Y_t + \sigma_{\text{cond}} Z_{X, t+1} = \rho (\rho X_t + \sigma_{\text{cond}} Z_{Y, t}) + \sigma_{\text{cond}} Z_{X, t+1}$$
$$X_{t+1} = \rho^2 X_t + \rho \sigma_{\text{cond}} Z_{Y, t} + \sigma_{\text{cond}} Z_{X, t+1}$$
This is an autoregressive process of order 1 ($\text{AR}(1)$) with autoregressive coefficient $\phi = \rho^2$!
Therefore, the lag-1 autocorrelation between successive Gibbs iterations is:
$$\mathrm{Corr}(X_t, X_{t+1}) = \rho^2 = 0.80^2 = 0.64$$
Notice that if $\rho \to 1.0$ (extreme correlation), $\rho^2 \to 1.0$, and the Gibbs sampler moves in tiny orthogonal steps along coordinate axes, suffering extreme slow mixing.

## Fully worked question 2: Conjugate Normal-Inverse-Gamma Gibbs Sampling

### Question
A pharmaceutical quality assurance lab measures tablet dissolution time. An observed sample of $n = 10$ measurements yields:
$$\sum_{i=1}^{10} y_i = 120.0 \implies \bar{y} = 12.0, \quad \sum_{i=1}^{10} (y_i - \bar{y})^2 = 18.0$$
The data are modeled as $y_i \mid \mu, \sigma^2 \sim \mathcal{N}(\mu, \sigma^2)$.
Priors are:
- $\mu \sim \mathcal{N}(\mu_0 = 10.0, \sigma_0^2 = 4.0)$.
- $\sigma^2 \sim \text{Inverse-Gamma}(a_0 = 2.0, b_0 = 5.0)$.

1. Derive the full conditional posterior distribution formulas for $\mu \mid \sigma^2, \mathbf{y}$ and $\sigma^2 \mid \mu, \mathbf{y}$.
2. In a Gibbs sampler step, the current variance is $\sigma^{2(t)} = 2.0$. Compute the numerical mean and variance of the full conditional distribution for $\mu$.
3. If the newly sampled mean is $\mu^{(t+1)} = 11.50$, compute the updated shape $a_n$ and scale $b_n$ for the full conditional distribution of $\sigma^2$.

### Solution, step 1: Full Conditional Formulations
1. **Full Conditional of $\mu \mid \sigma^2, \mathbf{y}$**:
   Since the prior is Gaussian and likelihood is Gaussian:
   $$\mu \mid \sigma^2, \mathbf{y} \sim \mathcal{N}\left( \mu_n, \; \sigma_n^2 \right)$$
   where:
   $$\frac{1}{\sigma_n^2} = \frac{1}{\sigma_0^2} + \frac{n}{\sigma^2} \implies \sigma_n^2 = \left( \frac{1}{\sigma_0^2} + \frac{n}{\sigma^2} \right)^{-1}$$
   $$\mu_n = \sigma_n^2 \left( \frac{\mu_0}{\sigma_0^2} + \frac{n \bar{y}}{\sigma^2} \right)$$

2. **Full Conditional of $\sigma^2 \mid \mu, \mathbf{y}$**:
   Since the prior is Inverse-Gamma and likelihood is Gaussian:
   $$\sigma^2 \mid \mu, \mathbf{y} \sim \text{Inverse-Gamma}(a_n, b_n)$$
   where:
   $$a_n = a_0 + \frac{n}{2}$$
   $$b_n = b_0 + \frac{1}{2} \sum_{i=1}^n (y_i - \mu)^2$$

### Solution, step 2: Numerical Update of $\mu$ for $\sigma^2 = 2.0$
Given $n = 10, \bar{y} = 12.0, \mu_0 = 10.0, \sigma_0^2 = 4.0$, and $\sigma^2 = 2.0$:
- Posterior precision:
  $$\frac{1}{\sigma_n^2} = \frac{1}{4.0} + \frac{10}{2.0} = 0.25 + 5.00 = 5.25$$
  $$\sigma_n^2 = \frac{1}{5.25} \approx 0.190476$$
- Posterior mean:
  $$\frac{\mu_0}{\sigma_0^2} = \frac{10.0}{4.0} = 2.50$$
  $$\frac{n \bar{y}}{\sigma^2} = \frac{10 \times 12.0}{2.0} = \frac{120.0}{2.0} = 60.0$$
  $$\mu_n = 0.190476 \times (2.50 + 60.0) = 0.190476 \times 62.50 \approx 11.9048$$
*Conditional Distribution*: $\mu \mid \sigma^2 = 2.0, \mathbf{y} \sim \mathcal{N}(11.905, \; 0.1905)$.

### Solution, step 3: Numerical Update of $\sigma^2$ for $\mu = 11.50$
Given $a_0 = 2.0, b_0 = 5.0, n = 10$, and $\mu = 11.50$:
1. Updated shape parameter:
   $$a_n = a_0 + \frac{n}{2} = 2.0 + \frac{10}{2} = 2.0 + 5.0 = 7.0$$
2. Sum of squared deviations:
   $$\sum_{i=1}^{10} (y_i - \mu)^2 = \sum_{i=1}^{10} (y_i - \bar{y})^2 + n (\bar{y} - \mu)^2$$
   Given $\sum (y_i - \bar{y})^2 = 18.0$, $\bar{y} = 12.0$, and $\mu = 11.50$:
   $$n (\bar{y} - \mu)^2 = 10 \times (12.0 - 11.50)^2 = 10 \times (0.50)^2 = 10 \times 0.25 = 2.50$$
   $$\sum_{i=1}^{10} (y_i - \mu)^2 = 18.0 + 2.50 = 20.50$$
3. Updated scale parameter:
   $$b_n = b_0 + \frac{1}{2} \sum_{i=1}^{10} (y_i - \mu)^2 = 5.0 + \frac{1}{2}(20.50) = 5.0 + 10.25 = 15.25$$

*Conditional Distribution*: $\sigma^2 \mid \mu = 11.50, \mathbf{y} \sim \text{Inverse-Gamma}(a_n = 7.0, \; b_n = 15.25)$.

## Fully worked question 3: Albert-Chib Data Augmentation for Probit Regression

### Question
Consider an Albert-Chib Bayesian probit regression model with a single predictor $x$ and no intercept:
$$P(y_i = 1 \mid x_i, \beta) = \Phi(x_i \beta)$$
Prior is $\beta \sim \mathcal{N}(0, \sigma_0^2 = 10)$.
Two observations are recorded:
- Observation 1: $x_1 = 1.0, y_1 = 1$.
- Observation 2: $x_2 = 2.0, y_2 = 0$.

The Gibbs sampler is at state $\beta = 0.50$.
1. Specify the exact conditional distributions of the latent variables $Z_1$ and $Z_2$ given $\beta = 0.50$.
2. In the imputation step, pseudorandom uniform draws yield:
   - For $Z_1$: draw $U_1 = 0.400$.
   - For $Z_2$: draw $U_2 = 0.600$.
   Compute the sampled values $Z_1$ and $Z_2$ using truncated normal inversion.
3. Compute the parameters of the updated full conditional distribution $\beta \mid Z_1, Z_2$.

### Solution, step 1: Conditional Distributions of Latent Variables $Z_1, Z_2$
Under the Albert-Chib model, the latent variable is $Z_i \sim \mathcal{N}(x_i \beta, 1)$:
- For $i = 1$ ($y_1 = 1$): $Z_1 > 0$.
  Mean: $\mu_{Z1} = x_1 \beta = 1.0 \times 0.50 = 0.50$.
  $Z_1 \sim \mathcal{N}(0.50, 1)$ truncated to $(0, \infty)$.
- For $i = 2$ ($y_2 = 0$): $Z_2 \le 0$.
  Mean: $\mu_{Z2} = x_2 \beta = 2.0 \times 0.50 = 1.00$.
  $Z_2 \sim \mathcal{N}(1.00, 1)$ truncated to $(-\infty, 0]$.

### Solution, step 2: Truncated Normal Sampling via Uniform Inversion
To sample $Z \sim \mathcal{N}(\mu, 1)$ truncated to $(a, b)$:
$$Z = \mu + \Phi^{-1}\left( \Phi(a - \mu) + U \cdot [\Phi(b - \mu) - \Phi(a - \mu)] \right)$$

1. **Sampling $Z_1$ on $(0, \infty)$ with $\mu = 0.50, U_1 = 0.400$**:
   - $a = 0, b = \infty$.
   - $a - \mu = 0 - 0.50 = -0.50$.
   - $\Phi(-0.50) = 1 - \Phi(0.50) \approx 1 - 0.69146 = 0.30854$.
   - $\Phi(\infty) = 1.0$.
   - Interpolated probability:
     $$P_1 = 0.30854 + 0.400 \times (1.0 - 0.30854) = 0.30854 + 0.400 \times 0.69146 = 0.30854 + 0.27658 = 0.58512$$
   - Invert: $\Phi^{-1}(0.58512) \approx +0.2150$.
   - Sampled value:
     $$Z_1 = \mu + \Phi^{-1}(P_1) = 0.50 + 0.2150 = 0.7150$$

2. **Sampling $Z_2$ on $(-\infty, 0]$ with $\mu = 1.00, U_2 = 0.600$**:
   - $a = -\infty, b = 0$.
   - $\Phi(-\infty) = 0.0$.
   - $b - \mu = 0 - 1.00 = -1.00$.
   - $\Phi(-1.00) = 1 - \Phi(1.00) \approx 1 - 0.84134 = 0.15866$.
   - Interpolated probability:
     $$P_2 = 0.0 + 0.600 \times 0.15866 = 0.095196$$
   - Invert: $\Phi^{-1}(0.095196) \approx -1.3094$.
   - Sampled value:
     $$Z_2 = \mu + \Phi^{-1}(P_2) = 1.00 - 1.3094 = -0.3094$$

### Solution, step 3: Update of $\beta$ Conditional on $\mathbf{Z} = (0.7150, -0.3094)^T$
Conditional on $\mathbf{Z}$, the model is standard linear regression:
$$\mathbf{Z} = \mathbf{X}\beta + \mathbf{\epsilon}, \quad \mathbf{\epsilon} \sim \mathcal{N}_2(\mathbf{0}, \mathbf{I})$$
where $\mathbf{X} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 1.0 \\ 2.0 \end{pmatrix}$, and prior $\beta \sim \mathcal{N}(0, \sigma_0^2 = 10)$:
- $\mathbf{X}^T \mathbf{X} = 1.0^2 + 2.0^2 = 1.0 + 4.0 = 5.0$.
- Posterior variance:
  $$\sigma_\beta^2 = \left( \frac{1}{\sigma_0^2} + \mathbf{X}^T \mathbf{X} \right)^{-1} = \left( \frac{1}{10} + 5.0 \right)^{-1} = (0.10 + 5.0)^{-1} = \frac{1}{5.10} \approx 0.19608$$
- Cross product:
  $$\mathbf{X}^T \mathbf{Z} = x_1 Z_1 + x_2 Z_2 = 1.0 \times (0.7150) + 2.0 \times (-0.3094) = 0.7150 - 0.6188 = +0.0962$$
- Posterior mean:
  $$\mu_\beta = \sigma_\beta^2 \left( \frac{\mu_0}{\sigma_0^2} + \mathbf{X}^T \mathbf{Z} \right) = 0.19608 \times (0 + 0.0962) = 0.19608 \times 0.0962 \approx +0.01886$$

*Full Conditional*: $\beta \mid \mathbf{Z}, \mathbf{y} \sim \mathcal{N}(\mu_\beta = 0.0189, \; \sigma_\beta^2 = 0.1961)$.
The step transforms non-linear categorical inference into elementary linear Gaussian regression.
"""

(DRAFT_DIR / "unit-7.md").write_text(u7.strip() + "\n", encoding="utf-8")
print("Unit 7 generated.")

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
u8 = r"""# Unit 8: Resampling & Permutation Methods: Bootstrap and Jackknife

In classical mathematical statistics, constructing confidence intervals, assessing estimator bias, and testing statistical hypotheses traditionally require making restrictive distributional assumptions (such as normality of observations) or relying upon asymptotic large-sample approximations whose finite-sample adequacy may be questionable. When estimating complex parameters—such as the ratio of trimmed medians, eigenvalues of sample correlation matrices, or non-linear econometric elasticities—analytical sampling distributions are typically impossible to derive in closed form.

In 1979, Bradley Efron published a revolutionary paper in *The Annals of Statistics* introducing the **Bootstrap**. Resampling methods replace intractable mathematical derivations with massive computer simulation, using the empirical data sample itself as an empirical proxy for the unknown population distribution. Alongside Maurice Quenouille's and John Tukey's **Jackknife** and Fisher's **Permutation Tests**, resampling constitutes an indispensable pillar of modern computational statistical inference.

## 8.1 The Plug-In Principle and Bradley Efron's Empirical Bootstrap

Let $\mathbf{X} = (X_1, X_2, \dots, X_n)$ be an independent and identically distributed (i.i.d.) random sample drawn from an unknown cumulative distribution function $F$:
$$X_i \sim F \quad \text{i.i.d. for } i = 1, \dots, n$$
We desire to estimate an unknown population parameter $\theta = t(F)$, such as the population mean $\mu = \int x\,dF(x)$, population median $F^{-1}(0.5)$, or variance $\sigma^2$.

Let $\hat{\theta} = s(\mathbf{X})$ be a sample estimator of $\theta$. To quantify the statistical uncertainty of $\hat{\theta}$, we need its sampling distribution $F_{\hat{\theta}}$, standard error $\text{se}_F(\hat{\theta})$, and bias $\text{bias}_F(\hat{\theta}) = \mathbb{E}_F[\hat{\theta}] - \theta$.

### 1. The Empirical Distribution Function (EDF)
The sample data $\mathbf{X}$ define the **Empirical Distribution Function (EDF)** $\hat{F}_n$:

$$\hat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n I(X_i \le x)$$

The EDF assigns discrete probability mass $1/n$ to each of the $n$ observed data points:
$$P_{\hat{F}_n}(X^* = X_i) = \frac{1}{n} \quad \text{for } i = 1, 2, \dots, n$$

By the **Glivenko-Cantelli Theorem (The Fundamental Theorem of Statistics)**:
$$\lim_{n \to \infty} \sup_{x \in \mathbb{R}} |\hat{F}_n(x) - F(x)| = 0 \quad \text{almost surely}$$
As $n \to \infty$, the empirical distribution $\hat{F}_n$ converges uniformly to the true population distribution $F$.

### 2. The Plug-In Principle
The **Plug-In Principle** dictates that any unknown population characteristic $\theta = t(F)$ is estimated by the corresponding characteristic of the empirical distribution:
$$\hat{\theta} = t(\hat{F}_n)$$
Similarly, the unknown standard error $\text{se}_F(\hat{\theta})$ is estimated by the plug-in estimate:
$$\widehat{\text{se}}(\hat{\theta}) = \text{se}_{\hat{F}_n}(\hat{\theta}^*)$$

### 3. The Non-Parametric Bootstrap Algorithm
Because calculating $\text{se}_{\hat{F}_n}(\hat{\theta}^*)$ analytically is intractable for complex estimators, Efron approximated it via Monte Carlo simulation:
1. For $b = 1, 2, \dots, B$ (where $B \ge 1,000$ bootstrap replicates):
   - Draw a **bootstrap sample** $\mathbf{X}^{*b} = (X_1^{*b}, X_2^{*b}, \dots, X_n^{*b})$ by sampling $n$ observations **uniformly at random with replacement** from the original dataset $\mathbf{X}$.
   - Compute the bootstrap replicate of the statistic:
     $$\hat{\theta}^{*b} = s(\mathbf{X}^{*b})$$
2. The **Bootstrap Standard Error** is the sample standard deviation of the $B$ bootstrap replications:
   $$\widehat{\text{se}}_B(\hat{\theta}) = \sqrt{\frac{1}{B - 1} \sum_{b=1}^B \left( \hat{\theta}^{*b} - \bar{\theta}^* \right)^2}$$
   where $\bar{\theta}^* = \frac{1}{B} \sum_{b=1}^B \hat{\theta}^{*b}$.
3. The **Bootstrap Bias Estimate** is:
   $$\widehat{\text{bias}}_B(\hat{\theta}) = \bar{\theta}^* - \hat{\theta}$$
   The bias-corrected point estimate is $\hat{\theta}_{\text{bc}} = \hat{\theta} - \widehat{\text{bias}}_B = 2\hat{\theta} - \bar{\theta}^*$.

## 8.2 Bootstrap Confidence Intervals: Normal, Percentile, Basic, and BCa

Constructing confidence intervals for parameter $\theta$ via bootstrapping admits several formulations:

### 1. The Standard Normal Bootstrap Interval
Assuming the sampling distribution of $\hat{\theta}$ is approximately Gaussian:
$$\mathcal{CI}_{\text{norm}} = \left[ \hat{\theta} - z_{1 - \alpha/2} \widehat{\text{se}}_B, \; \hat{\theta} + z_{1 - \alpha/2} \widehat{\text{se}}_B \right]$$
*Limitation*: Fails when the sampling distribution is skewed, heavy-tailed, or bounded.

### 2. The Percentile Bootstrap Interval
Sort the $B$ bootstrap estimates in ascending order:
$$\hat{\theta}^{*(1)} \le \hat{\theta}^{*(2)} \le \dots \le \hat{\theta}^{*(B)}$$
The $(1 - \alpha) \times 100\%$ **Percentile Interval** uses the empirical quantiles of the bootstrap distribution:

$$\mathcal{CI}_{\text{perc}} = \left[ \hat{\theta}^{*(\lfloor B \cdot \alpha/2 \rfloor)}, \; \hat{\theta}^{*(\lfloor B \cdot (1 - \alpha/2) \rfloor)} \right]$$

For a $95\%$ confidence interval with $B = 2,000$:
$$\mathcal{CI}_{0.95} = \left[ \hat{\theta}^{*(50)}, \; \hat{\theta}^{*(1950)} \right]$$
*Key Property (Transformation Invariance)*: If $g(\cdot)$ is any strictly monotonic transformation, the percentile interval for $g(\theta)$ is exactly $[g(\hat{\theta}_{\text{low}}), g(\hat{\theta}_{\text{high}})]$.
*Accuracy*: First-order accurate: coverage error $= \mathcal{O}(n^{-1/2})$.

### 3. The Basic (Empirical) Bootstrap Interval
Let the estimation error be $\delta = \hat{\theta} - \theta$. The basic bootstrap approximates the distribution of $\delta$ by the bootstrap errors $\delta^* = \hat{\theta}^* - \hat{\theta}$:
$$\mathcal{CI}_{\text{basic}} = \left[ 2\hat{\theta} - \hat{\theta}^{*(1 - \alpha/2)}, \; 2\hat{\theta} - \hat{\theta}^{*(\alpha/2)} \right]$$

### 4. Bias-Corrected and Accelerated (BCa) Intervals
Formulated by Efron in 1987, the **BCa Interval** corrects for both median bias and variance stabilization through two parameters:
- **$z_0$ (Bias-Correction Factor)**: Measures the median bias of $\hat{\theta}^*$:
  $$z_0 = \Phi^{-1}\left( \frac{\#\{\hat{\theta}^{*b} < \hat{\theta}\}}{B} \right)$$
- **$a$ (Acceleration Parameter)**: Measures the rate of change of the standard error of $\hat{\theta}$ with respect to the true parameter $\theta$, computed via jackknife influence values:
  $$a = \frac{\sum_{i=1}^n (\bar{U} - U_i)^3}{6 \left[ \sum_{i=1}^n (\bar{U} - U_i)^2 \right]^{3/2}}$$

The adjusted quantile points $\alpha_1, \alpha_2$ are:
$$\alpha_1 = \Phi\left( z_0 + \frac{z_0 + z_{\alpha/2}}{1 - a(z_0 + z_{\alpha/2})} \right), \quad \alpha_2 = \Phi\left( z_0 + \frac{z_0 + z_{1 - \alpha/2}}{1 - a(z_0 + z_{1 - \alpha/2})} \right)$$
$$\mathcal{CI}_{\text{BCa}} = \left[ \hat{\theta}^{*(\alpha_1)}, \; \hat{\theta}^{*(\alpha_2)} \right]$$
The BCa interval is **second-order accurate**: coverage error $= \mathcal{O}(n^{-1})$ and is transformation-invariant.

## 8.3 The Quenouille-Tukey Jackknife

Developed by Maurice Quenouille (1949) for bias reduction and extended by John Tukey (1958) for variance estimation, the **Jackknife** is a deterministic leave-one-out resampling method that requires no random number generation.

### 1. Leave-One-Out Estimators and Pseudovalues
Let $\mathbf{X} = (X_1, \dots, X_n)$ be a sample of size $n$, with point estimate $\hat{\theta} = s(\mathbf{X})$.
For each observation $i \in \{1, 2, \dots, n\}$, define the **leave-one-out subsample** $\mathbf{X}_{(i)}$ omitting the $i$-th data point:
$$\mathbf{X}_{(i)} = (X_1, \dots, X_{i-1}, X_{i+1}, \dots, X_n)$$
Let $\hat{\theta}_{(i)} = s(\mathbf{X}_{(i)})$ be the statistic evaluated on this $(n-1)$-sized subsample.

The mean of the leave-one-out estimates is:
$$\hat{\theta}_{(\bullet)} = \frac{1}{n} \sum_{i=1}^n \hat{\theta}_{(i)}$$

### 2. Jackknife Bias and Variance Formulas
- **Jackknife Bias Estimator**:
  $$\widehat{\text{bias}}_{\text{jack}} = (n - 1) (\hat{\theta}_{(\bullet)} - \hat{\theta})$$
- **Bias-Corrected Jackknife Estimator**:
  $$\hat{\theta}_{\text{jack}} = \hat{\theta} - \widehat{\text{bias}}_{\text{jack}} = n \hat{\theta} - (n - 1) \hat{\theta}_{(\bullet)}$$
- **Jackknife Variance Estimator**:
  $$\widehat{\text{var}}_{\text{jack}}(\hat{\theta}) = \frac{n - 1}{n} \sum_{i=1}^n \left( \hat{\theta}_{(i)} - \hat{\theta}_{(\bullet)} \right)^2$$
- **Jackknife Standard Error**:
  $$\widehat{\text{se}}_{\text{jack}} = \sqrt{\widehat{\text{var}}_{\text{jack}}}$$

*Theoretical Limitation*: The jackknife is non-smooth: it fails completely for non-differentiable statistics such as the sample median or sample quantiles, where $\widehat{\text{var}}_{\text{jack}}$ is inconsistent. The bootstrap, by contrast, handles non-smooth statistics seamlessly.

## 8.4 Permutation Tests: Fisher's Exact Hypothesis Testing

When testing the null hypothesis $H_0$ that two samples come from identical distributions, Ronald Fisher formulated the **Permutation Test (Randomization Test)**.

### The Two-Sample Permutation Algorithm
Consider sample $\mathbf{X} = (X_1, \dots, X_{n_1})$ from group 1 and sample $\mathbf{Y} = (Y_1, \dots, Y_{n_2})$ from group 2.
- Null hypothesis: $H_0: F_X = F_Y$.
- Compute the observed test statistic (e.g., difference in sample means):
  $$T_{\text{obs}} = \bar{X} - \bar{Y}$$
- Under $H_0$, group membership labels are completely exchangeable. Pool the $N = n_1 + n_2$ observations into a single dataset $\mathbf{Z} = (\mathbf{X}, \mathbf{Y})$.
- The total number of possible partitions of $N$ items into groups of size $n_1$ and $n_2$ is:
  $$M = \binom{N}{n_1} = \frac{N!}{n_1! n_2!}$$

For each of the $M$ partitions $\pi$:
- Assign $n_1$ items to group 1 and $n_2$ items to group 2, and compute $T_\pi = \bar{X}_\pi - \bar{Y}_\pi$.

The **Exact Permutation p-value** (for a two-tailed test) is:

$$p_{\text{exact}} = \frac{1}{M} \sum_{\pi=1}^M I(|T_\pi| \ge |T_{\text{obs}}|)$$

When $M$ is astronomically large (e.g., $n_1 = n_2 = 50 \implies \binom{100}{50} \approx 10^{29}$), exact enumeration is impossible. Statisticians draw a random sample of $B = 10,000$ random permutations to compute the **Monte Carlo Permutation p-value**:

$$\hat{p}_{\text{MC}} = \frac{1 + \sum_{b=1}^B I(|T_b^*| \ge |T_{\text{obs}}|)}{B + 1}$$
Permutation tests are completely distribution-free, valid for any sample size, and require zero parametric assumptions.

## Fully worked question 1: Non-Parametric Bootstrap Standard Error and Confidence Intervals

### Question
A biomedical researcher observes $n = 5$ patient recovery durations (in days) following a clinical therapy:
$$\mathbf{x} = (12, 15, 18, 22, 33)$$
The sample mean is $\bar{x} = 20.0$ days.
1. Compute the analytical standard error of the sample mean $\text{se}(\bar{x}) = s / \sqrt{n}$.
2. In a small Monte Carlo bootstrap study, $B = 6$ bootstrap samples are drawn with replacement from $\mathbf{x}$:
   - Sample 1: $(15, 15, 18, 22, 33) \implies \bar{x}^{*1} = 20.6$
   - Sample 2: $(12, 18, 18, 18, 22) \implies \bar{x}^{*2} = 17.6$
   - Sample 3: $(12, 12, 15, 22, 33) \implies \bar{x}^{*3} = 18.8$
   - Sample 4: $(15, 18, 22, 33, 33) \implies \bar{x}^{*4} = 24.2$
   - Sample 5: $(12, 15, 15, 18, 22) \implies \bar{x}^{*5} = 16.4$
   - Sample 6: $(18, 22, 22, 33, 33) \implies \bar{x}^{*6} = 25.6$
   Compute the bootstrap mean $\bar{x}^*$, the bootstrap standard error $\widehat{\text{se}}_B$, and the bootstrap bias estimate.
3. Construct the $90\%$ percentile bootstrap confidence interval using the sorted bootstrap replicates.

### Solution, step 1: Analytical Sample Standard Error
Given data $\mathbf{x} = (12, 15, 18, 22, 33)$ with $n = 5$:
- Sample mean:
  $$\bar{x} = \frac{12 + 15 + 18 + 22 + 33}{5} = \frac{100}{5} = 20.0$$
- Deviations from mean:
  $$(12 - 20) = -8 \implies (-8)^2 = 64$$
  $$(15 - 20) = -5 \implies (-5)^2 = 25$$
  $$(18 - 20) = -2 \implies (-2)^2 = 4$$
  $$(22 - 20) = +2 \implies 2^2 = 4$$
  $$(33 - 20) = +13 \implies 13^2 = 169$$
- Sum of squared deviations:
  $$\sum (x_i - \bar{x})^2 = 64 + 25 + 4 + 4 + 169 = 266$$
- Sample variance and standard deviation:
  $$s^2 = \frac{266}{n - 1} = \frac{266}{4} = 66.50 \implies s = \sqrt{66.50} \approx 8.1548$$
- Analytical standard error:
  $$\text{se}(\bar{x}) = \frac{s}{\sqrt{n}} = \frac{8.1548}{\sqrt{5}} = \frac{8.1548}{2.2361} \approx 3.6469 \approx 3.65 \text{ days}$$

### Solution, step 2: Bootstrap Estimates
The $B = 6$ bootstrap means are:
$$\bar{\mathbf{x}}^* = (20.6, 17.6, 18.8, 24.2, 16.4, 25.6)$$
1. **Bootstrap Mean**:
   $$\bar{x}^* = \frac{20.6 + 17.6 + 18.8 + 24.2 + 16.4 + 25.6}{6} = \frac{123.2}{6} \approx 20.533$$
2. **Bootstrap Bias Estimate**:
   $$\widehat{\text{bias}}_B = \bar{x}^* - \bar{x} = 20.533 - 20.000 = +0.533 \text{ days}$$
3. **Bootstrap Standard Error**:
   Deviations from $\bar{x}^* = 20.533$:
   - $(20.6 - 20.533)^2 = 0.067^2 \approx 0.0045$
   - $(17.6 - 20.533)^2 = (-2.933)^2 \approx 8.6025$
   - $(18.8 - 20.533)^2 = (-1.733)^2 \approx 3.0033$
   - $(24.2 - 20.533)^2 = (3.667)^2 \approx 13.4469$
   - $(16.4 - 20.533)^2 = (-4.133)^2 \approx 17.0817$
   - $(25.6 - 20.533)^2 = (5.067)^2 \approx 25.6745$
   Sum of squares:
   $$\sum (\bar{x}^{*b} - \bar{x}^*)^2 = 0.0045 + 8.6025 + 3.0033 + 13.4469 + 17.0817 + 25.6745 = 67.8134$$
   $$\widehat{\text{se}}_B = \sqrt{\frac{67.8134}{6 - 1}} = \sqrt{\frac{67.8134}{5}} = \sqrt{13.5627} \approx 3.6828 \approx 3.68 \text{ days}$$
Notice how closely the bootstrap standard error ($3.68$) approximates the true analytical standard error ($3.65$) even with only 6 bootstrap replicates!

### Solution, step 3: Percentile Bootstrap Confidence Interval
Sort the $B = 6$ bootstrap replicates in ascending order:
$$\bar{\mathbf{x}}^{*(sorted)} = [16.4, 17.6, 18.8, 20.6, 24.2, 25.6]$$
For a $90\%$ confidence interval ($\alpha = 0.10$), the lower quantile is $\alpha/2 = 0.05$ and upper quantile is $1 - \alpha/2 = 0.95$.
With $B = 6$, taking the lowest and highest values:
$$\mathcal{CI}_{0.90} = [16.4, \; 25.6] \text{ days}$$

## Fully worked question 2: Jackknife Bias and Variance for Ratio Estimation

### Question
An economist estimates the population debt-to-income ratio $R = \mu_Y / \mu_X$ using sample ratio estimator:
$$\hat{R} = \frac{\bar{Y}}{\bar{X}}$$
from a sample of $n = 4$ household pairs $(X_i, Y_i)$ where $X$ is income and $Y$ is debt (in thousands of dollars):
- Household 1: $(X_1 = 50, Y_1 = 20)$
- Household 2: $(X_2 = 60, Y_2 = 30)$
- Household 3: $(X_3 = 80, Y_3 = 40)$
- Household 4: $(X_4 = 110, Y_4 = 70)$

1. Compute the full-sample totals and the plug-in ratio estimate $\hat{R}$.
2. Evaluate the four leave-one-out ratio estimates $\hat{R}_{(1)}, \dots, \hat{R}_{(4)}$.
3. Compute the Jackknife bias estimate $\widehat{\text{bias}}_{\text{jack}}$ and the Jackknife standard error $\widehat{\text{se}}_{\text{jack}}$.

### Solution, step 1: Full-Sample Ratio Estimate
Total income:
$$\sum_{i=1}^4 X_i = 50 + 60 + 80 + 110 = 300$$
Total debt:
$$\sum_{i=1}^4 Y_i = 20 + 30 + 40 + 70 = 160$$
The sample ratio estimate is:
$$\hat{R} = \frac{\bar{Y}}{\bar{X}} = \frac{160 / 4}{300 / 4} = \frac{160}{300} = \frac{8}{15} \approx 0.533333$$

### Solution, step 2: Computation of Leave-One-Out Estimates
For each $i \in \{1, 2, 3, 4\}$, the leave-one-out ratio is $\hat{R}_{(i)} = \frac{\sum_{j \ne i} Y_j}{\sum_{j \ne i} X_j}$:
- **Omitting Household 1 ($X_1 = 50, Y_1 = 20$)**:
  $$\sum X_{(1)} = 300 - 50 = 250, \quad \sum Y_{(1)} = 160 - 20 = 140$$
  $$\hat{R}_{(1)} = \frac{140}{250} = 0.560000$$
- **Omitting Household 2 ($X_2 = 60, Y_2 = 30$)**:
  $$\sum X_{(2)} = 300 - 60 = 240, \quad \sum Y_{(2)} = 160 - 30 = 130$$
  $$\hat{R}_{(2)} = \frac{130}{240} \approx 0.541667$$
- **Omitting Household 3 ($X_3 = 80, Y_3 = 40$)**:
  $$\sum X_{(3)} = 300 - 80 = 220, \quad \sum Y_{(3)} = 160 - 40 = 120$$
  $$\hat{R}_{(3)} = \frac{120}{220} = \frac{6}{11} \approx 0.545455$$
- **Omitting Household 4 ($X_4 = 110, Y_4 = 70$)**:
  $$\sum X_{(4)} = 300 - 110 = 190, \quad \sum Y_{(4)} = 160 - 70 = 90$$
  $$\hat{R}_{(4)} = \frac{90}{190} = \frac{9}{19} \approx 0.473684$$

Mean of leave-one-out estimates:
$$\hat{R}_{(\bullet)} = \frac{0.560000 + 0.541667 + 0.545455 + 0.473684}{4} = \frac{2.120806}{4} \approx 0.530202$$

### Solution, step 3: Jackknife Bias and Standard Error
1. **Jackknife Bias Estimate**:
   $$\widehat{\text{bias}}_{\text{jack}} = (n - 1) (\hat{R}_{(\bullet)} - \hat{R}) = (4 - 1) (0.530202 - 0.533333) = 3 \times (-0.003131) \approx -0.009393$$
   The bias-corrected estimate is:
   $$\hat{R}_{\text{jack}} = \hat{R} - \widehat{\text{bias}}_{\text{jack}} = 0.533333 - (-0.009393) \approx 0.542726$$

2. **Jackknife Variance and Standard Error**:
   Deviations from $\hat{R}_{(\bullet)} = 0.530202$:
   - $(0.560000 - 0.530202)^2 = 0.029798^2 \approx 0.0008879$
   - $(0.541667 - 0.530202)^2 = 0.011465^2 \approx 0.0001314$
   - $(0.545455 - 0.530202)^2 = 0.015253^2 \approx 0.0002327$
   - $(0.473684 - 0.530202)^2 = (-0.056518)^2 \approx 0.0031943$
   Sum of squared deviations:
   $$\sum_{i=1}^4 (\hat{R}_{(i)} - \hat{R}_{(\bullet)})^2 = 0.0008879 + 0.0001314 + 0.0002327 + 0.0031943 = 0.0044463$$
   $$\widehat{\text{var}}_{\text{jack}}(\hat{R}) = \frac{n - 1}{n} \sum_{i=1}^n (\hat{R}_{(i)} - \hat{R}_{(\bullet)})^2 = \frac{3}{4} \times 0.0044463 \approx 0.0033347$$
   $$\widehat{\text{se}}_{\text{jack}} = \sqrt{0.0033347} \approx 0.057747 \approx 0.0577$$

*Conclusion*: The estimated debt-to-income ratio is $0.533 \pm 0.058$, with a small negative finite-sample bias of $-0.009$.

## Fully worked question 3: Exact Two-Sample Permutation Test

### Question
A randomized clinical trial compares a new drug (Group A, $n_A = 3$) against a standard placebo (Group B, $n_B = 3$) on blood pressure reduction (mm Hg):
- Group A: $(8, 11, 14) \implies \bar{X}_A = 11.0$
- Group B: $(3, 5, 7) \implies \bar{X}_B = 5.0$

The observed test statistic is the difference in group means:
$$T_{\text{obs}} = \bar{X}_A - \bar{X}_B = 11.0 - 5.0 = +6.0$$

1. Calculate the total number of distinct permutations $M = \binom{n_A + n_B}{n_A}$.
2. Enumerate all distinct permutations and compute the test statistic $T$ for each partition.
3. Determine the exact one-tailed and two-tailed permutation p-values, and state the statistical conclusion at significance level $\alpha = 0.05$.

### Solution, step 1: Total Number of Partitions
The pooled dataset of $N = 3 + 3 = 6$ observations is:
$$\mathbf{Z} = (3, 5, 7, 8, 11, 14)$$
The sum of all six observations is:
$$\sum Z_i = 3 + 5 + 7 + 8 + 11 + 14 = 48$$
The overall mean is $\bar{Z} = 48 / 6 = 8.0$.
Notice that:
$$\bar{X}_A - \bar{X}_B = \frac{\sum_{i \in A} Z_i}{3} - \frac{48 - \sum_{i \in A} Z_i}{3} = \frac{2 \sum_{i \in A} Z_i - 48}{3}$$
The test statistic is completely determined by the sum of elements assigned to Group A: $S_A = \sum_{i \in A} Z_i$!

The total number of equiprobable permutations under $H_0$ is:
$$M = \binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20 \text{ distinct permutations}$$

### Solution, step 2: Enumeration of All 20 Permutations and Test Statistics
We list all 20 possible subsets of size 3 from $\{3, 5, 7, 8, 11, 14\}$ and compute $S_A$ and $T = \frac{2 S_A - 48}{3}$:
1. $\{3, 5, 7\} \implies S_A = 15 \implies T = \frac{30 - 48}{3} = -6.0$
2. $\{3, 5, 8\} \implies S_A = 16 \implies T = \frac{32 - 48}{3} = -5.33$
3. $\{3, 5, 11\} \implies S_A = 19 \implies T = \frac{38 - 48}{3} = -3.33$
4. $\{3, 5, 14\} \implies S_A = 22 \implies T = \frac{44 - 48}{3} = -1.33$
5. $\{3, 7, 8\} \implies S_A = 18 \implies T = \frac{36 - 48}{3} = -4.0$
6. $\{3, 7, 11\} \implies S_A = 21 \implies T = \frac{42 - 48}{3} = -2.0$
7. $\{3, 7, 14\} \implies S_A = 24 \implies T = \frac{48 - 48}{3} = 0.0$
8. $\{3, 8, 11\} \implies S_A = 22 \implies T = -1.33$
9. $\{3, 8, 14\} \implies S_A = 25 \implies T = +0.67$
10. $\{3, 11, 14\} \implies S_A = 28 \implies T = +2.67$
11. $\{5, 7, 8\} \implies S_A = 20 \implies T = \frac{40 - 48}{3} = -2.67$
12. $\{5, 7, 11\} \implies S_A = 23 \implies T = -0.67$
13. $\{5, 7, 14\} \implies S_A = 26 \implies T = +1.33$
14. $\{5, 8, 11\} \implies S_A = 24 \implies T = 0.0$
15. $\{5, 8, 14\} \implies S_A = 27 \implies T = +2.0$
16. $\{5, 11, 14\} \implies S_A = 30 \implies T = +4.0$
17. $\{7, 8, 11\} \implies S_A = 26 \implies T = +1.33$
18. $\{7, 8, 14\} \implies S_A = 29 \implies T = +3.33$
19. $\{7, 11, 14\} \implies S_A = 32 \implies T = +5.33$
20. $\{8, 11, 14\} \implies S_A = 33 \implies T = \frac{66 - 48}{3} = +6.0$ (Observed data!)

The observed statistic is $T_{\text{obs}} = +6.0$.

### Solution, step 3: Exact p-Value Determination
1. **One-Tailed Test ($H_1: \mu_A > \mu_B$)**:
   We count the number of permutations where $T \ge T_{\text{obs}} = +6.0$:
   Only permutation 20 satisfies $T \ge +6.0$ ($T = +6.0$).
   $$p_{\text{one-tailed}} = \frac{\#\{T \ge 6.0\}}{20} = \frac{1}{20} = 0.0500$$

2. **Two-Tailed Test ($H_1: \mu_A \ne \mu_B$)**:
   We count permutations where $|T| \ge |T_{\text{obs}}| = 6.0$:
   - Permutation 1: $T = -6.0$ ($|-6.0| = 6.0$).
   - Permutation 20: $T = +6.0$ ($|+6.0| = 6.0$).
   Exactly 2 permutations satisfy $|T| \ge 6.0$:
   $$p_{\text{two-tailed}} = \frac{\#\{|T| \ge 6.0\}}{20} = \frac{2}{20} = 0.1000$$

*Statistical Conclusion*:
At significance level $\alpha = 0.05$, the two-tailed p-value is $p = 0.1000 > 0.05$. Therefore, we fail to reject the null hypothesis of equal efficacy. Because sample sizes are tiny ($n_A = n_B = 3$), even with completely separated samples (every observation in A exceeds every observation in B), the smallest possible two-tailed p-value is $2/20 = 0.10$, mathematically preventing rejection at the $5\%$ level without larger sample sizes.
"""

(DRAFT_DIR / "unit-8.md").write_text(u8.strip() + "\n", encoding="utf-8")
print("Unit 8 generated.")
