# tooling/generate-unit-6.py
import os

out_path = "publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

unit6_text = r"""# Unit 6: Resampling Methods: Nonparametric Bootstrap, Jackknife, Permutation Tests, and Cross-Validation

## 6.1 The Empirical Distribution Function, Dvoretzky–Kiefer–Wolfowitz Bounds, and the Plug-In Principle

Classical parametric inference relies upon rigid distributional assumptions (e.g., assuming observations follow a Gaussian, Poisson, or Weibull family). In modern empirical science, complex data distributions exhibit skewness, multi-modality, bounded supports, and heavy tails that violate parametric assumptions. 

Resampling methods—including the **Nonparametric Bootstrap**, the **Jackknife**, and **Permutation Tests**—revolutionized mathematical statistics in the late 20th century by substituting computational power for untestable parametric assumptions. The theoretical foundation of all non-parametric resampling methods is the **Empirical Distribution Function (EDF)** and Bradley Efron's **Plug-In Principle**.

### The Empirical Distribution Function (EDF)

Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed (i.i.d.) random sample drawn from an unknown continuous cumulative distribution function $F(x) = \mathbb{P}(X \le x)$ on the real line $\mathbb{R}$.

The **Empirical Distribution Function (EDF)** $\hat{F}_n(x)$ is the discrete step function assigning equal probability mass $1/n$ to each observed data point:

$$\hat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}(X_i \le x)$$

where $\mathbb{I}(\cdot)$ is the indicator function taking value 1 if the condition is satisfied and 0 otherwise.

```text
Empirical Distribution Function Step Pattern:
  1.0 +                                       .---
      |                                  .----'
      |                             .----'
      |                        .----'
      |                   .----'
      |              .----'
  0.0 +---------+----+----+----+----+----+----+---> x
               X(1) X(2) X(3) X(4) X(5) X(6)
```

#### Pointwise Statistical Properties:
For any fixed evaluation point $x \in \mathbb{R}$:
1. **Binomial Representation**: The sum $n \hat{F}_n(x) = \sum_{i=1}^n \mathbb{I}(X_i \le x)$ is a sum of $n$ independent Bernoulli trials with success probability $p = F(x)$. Therefore:
   $$n \hat{F}_n(x) \sim \text{Binomial}(n, F(x))$$
2. **Unbiasedness**:
   $$\mathbb{E}[\hat{F}_n(x)] = \frac{1}{n} \mathbb{E}[n \hat{F}_n(x)] = \frac{n F(x)}{n} = F(x)$$
3. **Variance**:
   $$\text{Var}(\hat{F}_n(x)) = \frac{F(x)(1 - F(x))}{n} \to 0 \quad \text{as } n \to \infty$$
4. **Strong Consistency (Pointwise)**: By the Strong Law of Large Numbers:
   $$\hat{F}_n(x) \xrightarrow{a.s.} F(x)$$

### Uniform Convergence: The Glivenko–Cantelli Theorem

While pointwise convergence guarantees that $\hat{F}_n(x)$ converges to $F(x)$ at any specific point $x$, mathematical statistics requires uniform convergence over the entire continuum $\mathbb{R}$.

The foundational result, proved by Valery Glivenko and Francesco Cantelli in 1933, is the **Glivenko–Cantelli Theorem (The Fundamental Theorem of Statistics)**:

$$\| \hat{F}_n - F \|_\infty = \sup_{x \in \mathbb{R}} |\hat{F}_n(x) - F(x)| \xrightarrow{a.s.} 0 \quad \text{as } n \to \infty$$

The empirical distribution function converges uniformly and almost surely to the true data-generating distribution across the entire real line.

### Finite-Sample Non-Asymptotic Confidence Bands: The DKW Inequality

In 1956, Aryeh Dvoretzky, Jack Kiefer, and Jacob Wolfowitz established an exponential bound on the supremum deviation. In 1990, Pascal Massart determined the sharp leading constant, producing the celebrated **Dvoretzky–Kiefer–Wolfowitz (DKW) Inequality**:

$$\mathbb{P}\left( \sup_{x \in \mathbb{R}} |\hat{F}_n(x) - F(x)| > \epsilon \right) \le 2 \exp(-2 n \epsilon^2) \quad \text{for any } \epsilon > 0$$

#### Construction of Exact Non-Parametric Confidence Bands:
Setting the right-hand tail probability to $\alpha$ (e.g. $\alpha = 0.05$ for a $95\%$ confidence band):
$$2 \exp(-2 n \epsilon^2) = \alpha \implies -2 n \epsilon^2 = \ln\left( \frac{\alpha}{2} \right) \implies \epsilon_n = \sqrt{\frac{\ln(2 / \alpha)}{2 n}}$$

This yields an exact, distribution-free, finite-sample $100(1 - \alpha)\%$ **simultaneous confidence band** for the unknown distribution function $F(x)$:

$$L(x) = \max(0, \, \hat{F}_n(x) - \epsilon_n) \le F(x) \le \min(1, \, \hat{F}_n(x) + \epsilon_n) = U(x)$$

This confidence band holds for **all** $x \in \mathbb{R}$ simultaneously, regardless of whether $F(x)$ is normal, exponential, multimodal, or pathological!

### The Plug-In Principle (Bradley Efron)

A population statistical parameter $\theta$ can generally be expressed as a mathematical functional of the underlying distribution function $F$:

$$\theta = T(F)$$

#### Examples of Statistical Functionals:
- **Population Mean**: $\mu = T(F) = \int x \, dF(x)$
- **Population Variance**: $\sigma^2 = T(F) = \int (x - \int u \, dF(u))^2 dF(x)$
- **Population Median**: $m = T(F) = F^{-1}(1/2)$
- **Correlation**: $\rho = T(F)$ evaluated over bivariate CDF $F(x, y)$.

The **Plug-In Principle** states that the natural non-parametric estimator of any parameter $\theta = T(F)$ is obtained by substituting the empirical distribution function $\hat{F}_n$ in place of the unknown distribution $F$:

$$\hat{\theta} = T(\hat{F}_n)$$

- For the mean: $T(\hat{F}_n) = \int x \, d\hat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n X_i = \bar{X}$.
- For the variance: $T(\hat{F}_n) = \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2$.
- For the median: $T(\hat{F}_n) = \hat{F}_n^{-1}(1/2) = \text{Sample Median}$.

Because $\hat{F}_n$ converges uniformly to $F$ by the Glivenko–Cantelli theorem, plug-in estimators inherit strong consistency $T(\hat{F}_n) \to T(F)$ under mild continuity conditions on the functional $T$.

---

## 6.2 The Nonparametric Bootstrap: Resampling Mechanics and Bootstrap Confidence Intervals

While the plug-in principle provides point estimators $\hat{\theta} = T(\hat{F}_n)$, calculating the standard error, bias, or confidence intervals for complex estimators (such as the ratio of two medians, eigenvalues of a covariance matrix, or Gini coefficients) is analytically intractable under classical mathematics.

In 1979, Bradley Efron introduced the **Nonparametric Bootstrap**. The central insight of the bootstrap is to treat the observed sample $\hat{F}_n$ as a surrogate for the true population $F$.

```text
The Bootstrap Analogy:
  Real World:        Population F  ----(draw size n)---->  Sample X  ---->  \hat{\theta} = T(X)
                          ^                                     |
                          |                                     | (Plug-in Analogy)
                          |                                     v
  Bootstrap World:   Sample \hat{F}_n --(resample with replacement)--> Bootstrap Sample X* ----> \hat{\theta}* = T(X*)
```

### The Bootstrap Resampling Protocol

1. Given an observed sample $\mathbf{x} = (x_1, \dots, x_n)$, calculate the point estimate $\hat{\theta} = T(\mathbf{x})$.
2. For $b = 1, 2, \dots, B$ (where $B \in [1,000, 10,000]$):
   - Draw a **bootstrap resample** $\mathbf{x}^{*b} = (x_1^{*b}, \dots, x_n^{*b})$ by sampling $n$ observations from $\mathbf{x}$ **uniformly at random with replacement**.
   - Compute the bootstrap replication of the estimator:
     $$\hat{\theta}^{*b} = T(\mathbf{x}^{*b})$$
3. Use the empirical distribution of the $B$ bootstrap replications $\{\hat{\theta}^{*1}, \dots, \hat{\theta}^{*B}\}$ to estimate standard errors, bias, and confidence intervals.

#### Multinomial Representation of Bootstrap Resamples:
Sampling $n$ observations with replacement from $\{x_1, \dots, x_n\}$ is algebraically equivalent to assigning random integer resampling weights $(w_1^*, \dots, w_n^*)$ drawn from a multinomial distribution:

$$\mathbf{w}^* = (w_1^*, \dots, w_n^*) \sim \text{Multinomial}\left( n, \, \left(\frac{1}{n}, \dots, \frac{1}{n}\right) \right)$$

where $w_i^*$ denotes the number of times original observation $x_i$ appears in the bootstrap sample. The probability that any specific observation $x_i$ is omitted entirely from a bootstrap resample is:

$$\mathbb{P}(w_i^* = 0) = \left( 1 - \frac{1}{n} \right)^n \to e^{-1} \approx 0.367879 \approx 36.8\%$$

Consequently, each bootstrap sample contains on average only $(1 - e^{-1}) \approx 63.2\%$ distinct original data points, with the remaining $36.8\%$ consisting of duplicates.

### Bootstrap Standard Error and Bias Estimation

1. **Bootstrap Standard Error**:
   The bootstrap standard error is the empirical sample standard deviation of the $B$ bootstrap replications:

   $$\widehat{\text{SE}}_{boot}(\hat{\theta}) = \sqrt{\frac{1}{B - 1} \sum_{b=1}^B (\hat{\theta}^{*b} - \bar{\theta}^*)^2}$$

   where $\bar{\theta}^* = \frac{1}{B} \sum_{b=1}^B \hat{\theta}^{*b}$.

2. **Bootstrap Bias Estimation**:
   The bias of an estimator is defined as $\text{Bias}(\hat{\theta}) = \mathbb{E}[\hat{\theta}] - \theta$. In the bootstrap world, the true parameter $\theta$ is replaced by $\hat{\theta}$, and the expectation $\mathbb{E}[\hat{\theta}]$ is replaced by $\bar{\theta}^*$:

   $$\widehat{\text{Bias}}_{boot}(\hat{\theta}) = \bar{\theta}^* - \hat{\theta}$$

   The **bias-corrected point estimator** is:
   $$\hat{\theta}_{bc} = \hat{\theta} - \widehat{\text{Bias}}_{boot} = 2 \hat{\theta} - \bar{\theta}^*$$

### Typology of Bootstrap Confidence Intervals

Statisticians employ four primary frameworks to construct $100(1 - \alpha)\%$ bootstrap confidence intervals:

#### 1. Standard Normal (Wald) Interval
Assumes the bootstrap distribution is approximately Gaussian:
$$\text{CI}_{norm} = \left[ \hat{\theta} - z_{1 - \alpha/2} \widehat{\text{SE}}_{boot}, \; \hat{\theta} + z_{1 - \alpha/2} \widehat{\text{SE}}_{boot} \right]$$
- **Flaw**: Performs poorly if the sampling distribution is skewed, asymmetric, or bounded.

#### 2. Basic (Empirical / Pivot) Interval
Based on the pivotal quantity $R = \hat{\theta} - \theta$. By approximating the distribution of $\hat{\theta} - \theta$ with the distribution of $\hat{\theta}^* - \hat{\theta}$:
$$\text{CI}_{basic} = \left[ 2\hat{\theta} - \hat{\theta}^*_{(1 - \alpha/2)}, \; 2\hat{\theta} - \hat{\theta}^*_{(\alpha/2)} \right]$$
where $\hat{\theta}^*_{(\alpha)}$ denotes the $\alpha$-quantile of the sorted bootstrap replications.

#### 3. Percentile Interval (Efron, 1981)
Directly takes the empirical quantiles of the bootstrap distribution:
$$\text{CI}_{perc} = \left[ \hat{\theta}^*_{(\alpha/2)}, \; \hat{\theta}^*_{(1 - \alpha/2)} \right]$$
- **Virtue**: Strictly **transformation-respecting**. If $g(\cdot)$ is any strictly monotonic transformation, the percentile interval for $g(\theta)$ is simply $[g(\hat{\theta}^*_{(\alpha/2)}), g(\hat{\theta}^*_{(1 - \alpha/2)})]$.
- **Limitation**: Suffers from coverage errors of order $\mathcal{O}(n^{-1/2})$ when the estimator has underlying bias or non-constant variance (heteroscedasticity).

#### 4. Bias-Corrected and Accelerated (BCa) Interval (Efron, 1987)
The gold standard non-parametric interval. The BCa interval adjusts the quantile endpoints to correct for both **median bias** ($z_0$) and **variance skewness (acceleration $a$)**:

$$\text{CI}_{BCa} = \left[ \hat{\theta}^*_{(\alpha_1)}, \; \hat{\theta}^*_{(\alpha_2)} \right]$$

where the adjusted percentile levels $\alpha_1, \alpha_2$ are given by:
$$\alpha_1 = \Phi\left( z_0 + \frac{z_0 + z_{\alpha/2}}{1 - a (z_0 + z_{\alpha/2})} \right)$$
$$\alpha_2 = \Phi\left( z_0 + \frac{z_0 + z_{1 - \alpha/2}}{1 - a (z_0 + z_{1 - \alpha/2})} \right)$$
- The **bias-correction parameter $z_0$** is estimated from the proportion of bootstrap replications falling below the original estimate:
  $$z_0 = \Phi^{-1}\left( \frac{1}{B} \sum_{b=1}^B \mathbb{I}(\hat{\theta}^{*b} < \hat{\theta}) \right)$$
- The **acceleration parameter $a$** measures the rate of change of the standard error of $\hat{\theta}$ with respect to the true parameter, estimated using jackknife influence values:
  $$a = \frac{\sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^3}{6 \left[ \sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^2 \right]^{3/2}}$$
BCa intervals achieve second-order accuracy ($\mathcal{O}(n^{-1})$ coverage error), preserving exact nominal coverage even for skewed non-normal statistics.

---

## 6.3 The Jackknife: Leave-One-Out Estimators, Bias Reduction, and Breakdown Modes

Preceding the bootstrap by three decades, the **Jackknife** was invented by Maurice Quenouille in 1949 as a tool for non-parametric bias reduction, and extended by John Tukey in 1958 to estimate sampling variance.

Unlike the bootstrap (which requires stochastic Monte Carlo simulation), the classical jackknife is **strictly deterministic**, systematically evaluating the statistic over all $n$ leave-one-out sub-samples.

### The Jackknife Pseudovalues and Bias Reduction

Let $\mathbf{x} = (x_1, \dots, x_n)$ be a sample of size $n$, and let $\hat{\theta} = T(\mathbf{x})$ be an estimator.
Let $\mathbf{x}_{(-i)}$ denote the sub-sample of size $n - 1$ obtained by deleting the $i$-th observation $x_i$:

$$\mathbf{x}_{(-i)} = (x_1, \dots, x_{i-1}, x_{i+1}, \dots, x_n)$$

The $i$-th **leave-one-out replication** is:
$$\hat{\theta}_{(-i)} = T(\mathbf{x}_{(-i)})$$
The average of the leave-one-out replications is:
$$\bar{\theta}_{(\cdot)} = \frac{1}{n} \sum_{i=1}^n \hat{\theta}_{(-i)}$$

#### Quenouille's Bias Elimination Theorem:
Suppose an estimator $\hat{\theta}$ has bias whose asymptotic expansion in powers of $1/n$ is:
$$\mathbb{E}[\hat{\theta}] = \theta + \frac{a_1}{n} + \frac{a_2}{n^2} + \mathcal{O}(n^{-3})$$
For the leave-one-out estimator based on $n - 1$ observations:
$$\mathbb{E}[\hat{\theta}_{(-i)}] = \theta + \frac{a_1}{n - 1} + \frac{a_2}{(n - 1)^2} + \mathcal{O}(n^{-3})$$

Taking the expectation of $\bar{\theta}_{(\cdot)}$:
$$\mathbb{E}[\bar{\theta}_{(\cdot)}] = \theta + \frac{a_1}{n - 1} + \mathcal{O}(n^{-2})$$

Quenouille constructed the **Jackknife Bias-Reduced Estimator**:

$$\hat{\theta}_{jack} = n \hat{\theta} - (n - 1) \bar{\theta}_{(\cdot)}$$

Evaluating its expectation:
$$\mathbb{E}[\hat{\theta}_{jack}] = n \mathbb{E}[\hat{\theta}] - (n - 1) \mathbb{E}[\bar{\theta}_{(\cdot)}]$$
$$= n \left( \theta + \frac{a_1}{n} + \mathcal{O}(n^{-2}) \right) - (n - 1) \left( \theta + \frac{a_1}{n - 1} + \mathcal{O}(n^{-2}) \right)$$
$$= n\theta + a_1 - (n - 1)\theta - a_1 + \mathcal{O}(n^{-1}) = \theta + \mathcal{O}(n^{-2})$$

The leading $\mathcal{O}(n^{-1})$ bias term **cancels out completely**! The jackknife automatically reduces the bias from order $n^{-1}$ to order $n^{-2}$ without requiring any analytical derivations of the sampling distribution.

#### Tukey's Pseudovalues:
Tukey defined the $i$-th **Jackknife Pseudovalue** as:
$$J_i = n \hat{\theta} - (n - 1) \hat{\theta}_{(-i)}$$
Notice that the jackknife estimator is simply the arithmetic mean of the pseudovalues:
$$\hat{\theta}_{jack} = \frac{1}{n} \sum_{i=1}^n J_i$$

### Tukey's Jackknife Variance Estimator

Tukey proposed treating the pseudovalues $J_1, \dots, J_n$ as approximately independent observations, leading to the **Jackknife Variance Estimator**:

$$v_{jack} = \frac{1}{n (n - 1)} \sum_{i=1}^n (J_i - \hat{\theta}_{jack})^2 = \frac{n - 1}{n} \sum_{i=1}^n (\hat{\theta}_{(-i)} - \bar{\theta}_{(\cdot)})^2$$

Notice the multiplier $\frac{n - 1}{n}$, which is drastically different from the usual $\frac{1}{n - 1}$. 
- Because the leave-one-out sub-samples $\mathbf{x}_{(-i)}$ and $\mathbf{x}_{(-j)}$ share $n - 2$ identical observations, the replications $\hat{\theta}_{(-i)}$ are extremely close to one another. The factor $(n - 1)$ magnifies their tiny variance to properly reconstruct the sample variance of the original estimator $\hat{\theta}$.

### Breakdown Modes: The Non-Smoothness Trap (Failure on Sample Median)

While the jackknife works brilliantly for **smooth statistics** (sample mean, variance, correlation, regression coefficients), it suffers from a catastrophic failure mode when applied to **non-smooth statistics**, most notably the **sample median**.

#### Why the Jackknife Fails on the Median:
Consider a sorted sample of even size $n = 2m$:
$$x_{(1)} < x_{(2)} < \dots < x_{(2m)}$$
The sample median is:
$$\hat{\theta} = \frac{x_{(m)} + x_{(m+1)}}{2}$$
When we delete observation $x_i$:
- If $i \le m$, the $(2m-1)$-element sub-sample has median $\hat{\theta}_{(-i)} = x_{(m+1)}$.
- If $i > m$, the sub-sample has median $\hat{\theta}_{(-i)} = x_{(m)}$.
Notice that the leave-one-out median takes only **two discrete values**, regardless of how large $n$ is!
As $n \to \infty$, the jackknife variance estimator $v_{jack}$ does **not** converge to the true asymptotic variance of the median. In fact, $v_{jack}$ remains stochastic and does not even converge to a deterministic limit!

**The Solution: Delete-$d$ Jackknife or Bootstrap**:
To estimate the variance of non-smooth statistics like quantiles, statisticians must use either the **Nonparametric Bootstrap** (which resamples with replacement and is smooth in distribution) or the **Delete-$d$ Jackknife** (Shao and Wu, 1989), where $d$ observations are removed at a time such that $\sqrt{n} \ll d \ll n$.

---

## 6.4 Permutation Tests: Exact Combinatorial Inference and Monte Carlo Approximations

In classical two-sample hypothesis testing (e.g. Student's $t$-test), testing whether a treatment produces a significant effect requires assuming that the underlying populations are Gaussian with equal variances.

In 1935, Ronald A. Fisher introduced **Permutation Tests (Randomization Tests)**, demonstrating that valid exact hypothesis tests can be constructed using purely combinatorial mechanics under the **sharp null hypothesis of exchangeability**.

### The Sharp Null Hypothesis of Exchangeability

Consider an experiment comparing two treatment groups:
- Control group: $\mathbf{X} = (X_1, \dots, X_{n_1})$
- Treatment group: $\mathbf{Y} = (Y_1, \dots, Y_{n_2})$
Total sample size: $N = n_1 + n_2$.

The **Sharp Null Hypothesis ($H_0$)** posits that the treatment has **zero effect on every individual**:
$$H_0: F_X(z) = F_Y(z) = F(z) \quad \text{for all } z \in \mathbb{R}$$

Under $H_0$, the labels "Control" and "Treatment" are arbitrary semantic tags assigned by the experimenter. Every observation in the pooled sample:
$$\mathbf{Z} = (X_1, \dots, X_{n_1}, Y_1, \dots, Y_{n_2}) = (Z_1, \dots, Z_N)$$
was drawn from the identical underlying distribution $F$.

#### The Principle of Exchangeability:
Under $H_0$, the joint distribution of $(Z_1, \dots, Z_N)$ is invariant under any permutation of the indices:
$$(Z_{\pi(1)}, \dots, Z_{\pi(N)}) \stackrel{d}{=} (Z_1, \dots, Z_N)$$
for every permutation $\pi \in \mathcal{S}_N$.

### Exact Combinatorial Enumeration

Let $T(\mathbf{Z})$ denote a chosen test statistic measuring the difference between groups (e.g., difference in sample means $T = \bar{Y} - \bar{X}$, difference in medians, or two-sample Wilcoxon rank sum).
Let $T_{obs} = T(\mathbf{Z}_{obs})$ denote the test statistic computed on the observed data.

Under $H_0$, every possible partition of the $N$ observations into a group of size $n_1$ and a group of size $n_2$ is **equally likely**.
The total number of possible partitions is given by the binomial coefficient:

$$M = \binom{N}{n_1} = \frac{N!}{n_1! n_2!}$$

For each of the $M$ partitions $\mathbf{Z}^{(m)}$, compute the test statistic $T^{(m)}$.
The **Exact Permutation $p$-value** (for a one-sided upper-tail test) is the exact proportion of partitions whose test statistic is greater than or equal to $T_{obs}$:

$$p_{exact} = \frac{1}{M} \sum_{m=1}^M \mathbb{I}(T^{(m)} \ge T_{obs})$$

#### Properties of Exact Permutation Tests:
1. **Exact Size Guarantee**: The test achieves exact nominal Type I error rate $\alpha$:
   $$\mathbb{P}(p_{exact} \le \alpha \mid H_0) \le \alpha$$
   Zero asymptotic approximations. The test is exact for any sample size, even $n_1 = 3, n_2 = 3$.
2. **Distribution-Free**: Requires zero assumptions about normality, homoscedasticity, or linearity.

### Monte Carlo Permutation Approximation

As sample sizes grow, the total number of partitions $M = \binom{N}{n_1}$ explodes combinatorially:
- For $n_1 = 20, n_2 = 20$:
  $$M = \binom{40}{20} = 137,846,528,820 \approx 1.38 \times 10^{11} \text{ partitions!}$$
Evaluating all 137 billion partitions is computationally prohibitive.

To evaluate $p$-values on large datasets, statisticians draw an independent random sample of $B$ permutations $\pi_1, \dots, \pi_B$ uniformly from the permutation space (typically $B \in [1,000, 100,000]$).

#### The Valid Pseudo-Count $p$-value Formula:
In computing the Monte Carlo permutation $p$-value, novice programmers often compute:
$$\tilde{p} = \frac{1}{B} \sum_{b=1}^B \mathbb{I}(T^{*b} \ge T_{obs})$$
This naive formula is **technically invalid** because if none of the simulated permutations exceed $T_{obs}$, it reports $\tilde{p} = 0$, implying an impossible zero-probability event.

The mathematically rigorous, strictly valid Monte Carlo $p$-value (North et al., 2002) includes the observed data itself as the $(B + 1)$-th permutation:

$$p_{MC} = \frac{1 + \sum_{b=1}^B \mathbb{I}(T^{*b} \ge T_{obs})}{B + 1}$$

Under $H_0$, $p_{MC}$ is guaranteed to be strictly super-uniform ($\mathbb{P}(p_{MC} \le \alpha) \le \alpha$), preserving the exact size of the hypothesis test.

---

## 6.5 Cross-Validation: K-Fold, Leave-One-Out, and Fast Analytical Leverage Shortcuts

In predictive modeling and model selection (e.g. tuning regularization parameter $\lambda$ in Lasso/Ridge, selecting polynomial degree, or pruning decision trees), evaluating a model on the same training data used to fit it produces **optimism bias**: the training error systematically underestimates the true out-of-sample generalization error:

$$\mathbb{E}[\text{Error}_{train}] < \mathbb{E}[\text{Error}_{test}]$$

**Cross-Validation (CV)** provides an empirical, non-parametric methodology for estimating out-of-sample prediction error.

### Typology of Cross-Validation Frameworks

#### 1. $K$-Fold Cross-Validation
1. Randomly partition the dataset of $N$ observations into $K$ mutually disjoint, roughly equal-sized folds $\mathcal{C}_1, \dots, \mathcal{C}_K$:
   $$\bigcup_{k=1}^K \mathcal{C}_k = \{1, \dots, N\}, \quad \mathcal{C}_j \cap \mathcal{C}_k = \emptyset \quad (j \ne k)$$
2. For each fold $k \in \{1, \dots, K\}$:
   - Train the model using the remaining $K - 1$ folds: $\mathcal{D}_{(-k)} = \{1, \dots, N\} \setminus \mathcal{C}_k$.
   - Predict responses for observations in the held-out fold $\mathcal{C}_k$: $\hat{y}_i^{(-k)}$.
   - Compute the fold prediction error:
     $$\text{MSE}_k = \frac{1}{|\mathcal{C}_k|} \sum_{i \in \mathcal{C}_k} L(y_i, \, \hat{y}_i^{(-k)})$$
3. The overall $K$-fold cross-validation error is the average across all $K$ folds:

$$\text{CV}_{(K)} = \frac{1}{N} \sum_{i=1}^N L(y_i, \, \hat{y}_i^{(-k(i))})$$

Standard practice adopts $K = 5$ or $K = 10$, balancing computational cost and the bias-variance trade-off of the error estimator.

#### 2. Leave-One-Out Cross-Validation (LOOCV)
LOOCV is the extreme case where $K = N$: each fold contains exactly one observation ($|\mathcal{C}_k| = 1$).
The model is trained $N$ separate times on $N - 1$ observations, predicting the held-out observation:

$$\text{LOOCV} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_{(-i)})^2$$

- **Virtue**: Almost completely unbiased for generalization error because each training subset has size $N - 1 \approx N$.
- **Historical Drawback**: Fitting a complex model $N$ separate times requires prohibitive computation.

### The Fast Analytical LOOCV Leverage Identity in Linear Models

For Ordinary Least Squares (OLS) linear regression $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$, fitting $N$ models from scratch is **completely unnecessary**. 

Through an extraordinary algebraic cancellation involving the Sherman–Morrison–Woodbury matrix inverse formula, the leave-one-out prediction error $y_i - \hat{y}_{(-i)}$ can be computed directly from the single model fitted to the **entire dataset**!

#### The Fast LOOCV Identity:
Let $\hat{y}_i = \mathbf{x}_i \hat{\boldsymbol{\beta}}$ denote the fitted value from the full model, and let $e_i = y_i - \hat{y}_i$ denote the standard OLS residual.
Let $\mathbf{H} = \mathbf{X} (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top$ denote the projection (hat) matrix, with diagonal leverage values $h_{ii} = H_{ii}$.

The leave-one-out prediction error satisfies the exact mathematical identity:

$$e_{[i]} = y_i - \hat{y}_{(-i)} = \frac{e_i}{1 - h_{ii}}$$

#### The LOOCV Master Equation:
The total Leave-One-Out Cross-Validation error is computed in a single vectorized pass:

$$\text{LOOCV} = \frac{1}{N} \sum_{i=1}^N \left( \frac{e_i}{1 - h_{ii}} \right)^2 = \frac{1}{N} \sum_{i=1}^N \left( \frac{y_i - \hat{y}_i}{1 - h_{ii}} \right)^2$$

This identity reduces the computational complexity of LOOCV from $\mathcal{O}(N^2 p^2)$ down to **$\mathcal{O}(N p^2)$—the exact same cost as fitting a single regression model**!

---

## Fully worked question 1: Analytical Derivation of the Fast LOOCV Leverage Identity in Linear Regression

### Question
In multiple linear regression, an analyst fits an Ordinary Least Squares (OLS) model:

$$\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\epsilon}$$

where $\mathbf{X} \in \mathbb{R}^{n \times p}$ has full column rank $p$, $\mathbf{y} \in \mathbb{R}^n$, and the full-sample parameter estimator is:
$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$$

Let $\mathbf{H} = \mathbf{X} (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \in \mathbb{R}^{n \times n}$ be the hat matrix, with diagonal leverage elements $h_{ii} = \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top$, where $\mathbf{x}_i$ is the $i$-th row of $\mathbf{X}$ written as a row vector ($1 \times p$).

Let $\mathbf{X}_{(-i)} \in \mathbb{R}^{(n-1) \times p}$ and $\mathbf{y}_{(-i)} \in \mathbb{R}^{n-1}$ denote the design matrix and response vector with the $i$-th observation removed.
The leave-one-out parameter estimate is:
$$\hat{\boldsymbol{\beta}}_{(-i)} = (\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)})^{-1} \mathbf{X}_{(-i)}^\top \mathbf{y}_{(-i)}$$

The leave-one-out predicted value for observation $i$ is $\hat{y}_{(-i)} = \mathbf{x}_i \hat{\boldsymbol{\beta}}_{(-i)}$, and the leave-one-out prediction error is $e_{[i]} = y_i - \hat{y}_{(-i)}$.

1. Express $\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)}$ and $\mathbf{X}_{(-i)}^\top \mathbf{y}_{(-i)}$ as rank-one updates of the full-sample cross-products $\mathbf{X}^\top \mathbf{X}$ and $\mathbf{X}^\top \mathbf{y}$.
2. State the **Sherman–Morrison Formula** for the inverse of an invertible matrix perturbed by a rank-one outer product:
   $$(\mathbf{A} - \mathbf{u} \mathbf{v}^\top)^{-1} = \mathbf{A}^{-1} + \frac{\mathbf{A}^{-1} \mathbf{u} \mathbf{v}^\top \mathbf{A}^{-1}}{1 - \mathbf{v}^\top \mathbf{A}^{-1} \mathbf{u}}$$
   Apply this formula to derive an exact algebraic expression for $(\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)})^{-1}$.
3. Prove rigorously that the parameter difference satisfies:
   $$\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(-i)} = \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top e_i}{1 - h_{ii}}$$
   where $e_i = y_i - \mathbf{x}_i \hat{\boldsymbol{\beta}}$ is the ordinary full-sample residual.
4. Using this parameter difference, prove the **Fast LOOCV Identity**:
   $$e_{[i]} = y_i - \hat{y}_{(-i)} = \frac{e_i}{1 - h_{ii}}$$
5. In a sample of $n = 5$ observations, the full-sample residuals are $\mathbf{e} = [-1.2, \, 0.8, \, -0.4, \, 1.5, \, -0.7]$ and the diagonal leverage values are $\mathbf{h} = [0.20, \, 0.36, \, 0.15, \, 0.50, \, 0.25]$. Compute the five leave-one-out prediction errors $e_{[1]}, \dots, e_{[5]}$ and the exact LOOCV mean squared error.

---

### Solution, step 1: Express leave-one-out cross products as rank-one modifications

**Solution, step 1: Express leave-one-out cross products as rank-one modifications.**

The full cross-product matrix is the sum of outer products of the individual rows:
$$\mathbf{X}^\top \mathbf{X} = \sum_{j=1}^n \mathbf{x}_j^\top \mathbf{x}_j$$
Removing the $i$-th row $\mathbf{x}_i$ subtracts its individual outer product:

$$\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)} = \sum_{j \ne i} \mathbf{x}_j^\top \mathbf{x}_j = \mathbf{X}^\top \mathbf{X} - \mathbf{x}_i^\top \mathbf{x}_i$$

Similarly, for the cross-product with the response vector:
$$\mathbf{X}^\top \mathbf{y} = \sum_{j=1}^n \mathbf{x}_j^\top y_j$$
Removing the $i$-th observation yields:

$$\mathbf{X}_{(-i)}^\top \mathbf{y}_{(-i)} = \mathbf{X}^\top \mathbf{y} - \mathbf{x}_i^\top y_i$$

---

### Solution, step 2: Apply Sherman–Morrison formula to invert the perturbed matrix

**Solution, step 2: Apply Sherman–Morrison formula to invert the perturbed matrix.**

Let $\mathbf{A} = \mathbf{X}^\top \mathbf{X}$. The perturbed matrix is:
$$\mathbf{A} - \mathbf{u} \mathbf{v}^\top = \mathbf{X}^\top \mathbf{X} - \mathbf{x}_i^\top \mathbf{x}_i$$
where $\mathbf{u} = \mathbf{x}_i^\top$ (a $p \times 1$ column vector) and $\mathbf{v}^\top = \mathbf{x}_i$ (a $1 \times p$ row vector).

Applying the Sherman–Morrison formula:
$$(\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)})^{-1} = (\mathbf{X}^\top \mathbf{X} - \mathbf{x}_i^\top \mathbf{x}_i)^{-1}$$
$$= (\mathbf{X}^\top \mathbf{X})^{-1} + \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1}}{1 - \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top}$$

Recall the definition of the leverage $h_{ii}$:
$$h_{ii} = \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top$$

Substituting $h_{ii}$ into the denominator:

$$(\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)})^{-1} = (\mathbf{X}^\top \mathbf{X})^{-1} + \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1}}{1 - h_{ii}}$$

---

### Solution, step 3: Derive the parameter vector difference

**Solution, step 3: Derive the parameter vector difference.**

The leave-one-out parameter estimator is:
$$\hat{\boldsymbol{\beta}}_{(-i)} = (\mathbf{X}_{(-i)}^\top \mathbf{X}_{(-i)})^{-1} \mathbf{X}_{(-i)}^\top \mathbf{y}_{(-i)}$$
Substitute our rank-one expressions:
$$\hat{\boldsymbol{\beta}}_{(-i)} = \left[ (\mathbf{X}^\top \mathbf{X})^{-1} + \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1}}{1 - h_{ii}} \right] (\mathbf{X}^\top \mathbf{y} - \mathbf{x}_i^\top y_i)$$

Expand the product into four terms:
$$\hat{\boldsymbol{\beta}}_{(-i)} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y} - (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top y_i + \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}}{1 - h_{ii}} - \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top y_i}{1 - h_{ii}}$$

Notice that:
- $(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y} = \hat{\boldsymbol{\beta}}$ (the full-sample estimator).
- $\mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y} = \mathbf{x}_i \hat{\boldsymbol{\beta}} = \hat{y}_i$ (the full-sample fitted value).
- $\mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top = h_{ii}$ (the leverage).

Substitute these terms:
$$\hat{\boldsymbol{\beta}}_{(-i)} = \hat{\boldsymbol{\beta}} - (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top y_i + \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top \hat{y}_i}{1 - h_{ii}} - \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top h_{ii} y_i}{1 - h_{ii}}$$

Group the terms containing $(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top$:
$$\hat{\boldsymbol{\beta}}_{(-i)} = \hat{\boldsymbol{\beta}} + (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top \left[ -y_i + \frac{\hat{y}_i}{1 - h_{ii}} - \frac{h_{ii} y_i}{1 - h_{ii}} \right]$$

Combine the bracketed terms over the common denominator $(1 - h_{ii})$:
$$-y_i + \frac{\hat{y}_i - h_{ii} y_i}{1 - h_{ii}} = \frac{-y_i (1 - h_{ii}) + \hat{y}_i - h_{ii} y_i}{1 - h_{ii}} = \frac{-y_i + h_{ii} y_i + \hat{y}_i - h_{ii} y_i}{1 - h_{ii}}$$
$$= \frac{-y_i + \hat{y}_i}{1 - h_{ii}} = -\frac{y_i - \hat{y}_i}{1 - h_{ii}} = -\frac{e_i}{1 - h_{ii}}$$

Therefore:
$$\hat{\boldsymbol{\beta}}_{(-i)} = \hat{\boldsymbol{\beta}} - \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top e_i}{1 - h_{ii}}$$

Rearranging gives the parameter update formula:

$$\hat{\boldsymbol{\beta}} - \hat{\boldsymbol{\beta}}_{(-i)} = \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top e_i}{1 - h_{ii}}$$

---

### Solution, step 4: Prove the Fast LOOCV Identity

**Solution, step 4: Prove the Fast LOOCV Identity.**

Now evaluate the leave-one-out fitted value $\hat{y}_{(-i)}$:
$$\hat{y}_{(-i)} = \mathbf{x}_i \hat{\boldsymbol{\beta}}_{(-i)} = \mathbf{x}_i \left[ \hat{\boldsymbol{\beta}} - \frac{(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top e_i}{1 - h_{ii}} \right]$$
$$= \mathbf{x}_i \hat{\boldsymbol{\beta}} - \frac{\mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top e_i}{1 - h_{ii}} = \hat{y}_i - \frac{h_{ii} e_i}{1 - h_{ii}}$$

Now compute the leave-one-out prediction error $e_{[i]} = y_i - \hat{y}_{(-i)}$:
$$e_{[i]} = y_i - \left( \hat{y}_i - \frac{h_{ii} e_i}{1 - h_{ii}} \right) = (y_i - \hat{y}_i) + \frac{h_{ii} e_i}{1 - h_{ii}}$$
Since $y_i - \hat{y}_i = e_i$:
$$e_{[i]} = e_i + \frac{h_{ii} e_i}{1 - h_{ii}} = e_i \left( 1 + \frac{h_{ii}}{1 - h_{ii}} \right) = e_i \left( \frac{1 - h_{ii} + h_{ii}}{1 - h_{ii}} \right) = \frac{e_i}{1 - h_{ii}}$$

This completes the rigorous mathematical proof of the **Fast LOOCV Identity**:

$$e_{[i]} = \frac{e_i}{1 - h_{ii}}$$

---

### Solution, step 5: Numerical computation of LOOCV errors

**Solution, step 5: Numerical computation of LOOCV errors.**

We are given $n = 5$ observations with:
- Residuals: $\mathbf{e} = [-1.2, \, 0.8, \, -0.4, \, 1.5, \, -0.7]$
- Leverages: $\mathbf{h} = [0.20, \, 0.36, \, 0.15, \, 0.50, \, 0.25]$

Compute $e_{[i]} = e_i / (1 - h_{ii})$ for each observation:

1. **Observation 1**:
   $$e_{[1]} = \frac{-1.2}{1 - 0.20} = \frac{-1.2}{0.80} = \mathbf{-1.5000}$$
   $$e_{[1]}^2 = (-1.5)^2 = 2.25$$

2. **Observation 2**:
   $$e_{[2]} = \frac{0.8}{1 - 0.36} = \frac{0.8}{0.64} = \mathbf{1.2500}$$
   $$e_{[2]}^2 = (1.25)^2 = 1.5625$$

3. **Observation 3**:
   $$e_{[3]} = \frac{-0.4}{1 - 0.15} = \frac{-0.4}{0.85} \approx \mathbf{-0.470588}$$
   $$e_{[3]}^2 \approx (-0.470588)^2 \approx 0.221453$$

4. **Observation 4**:
   $$e_{[4]} = \frac{1.5}{1 - 0.50} = \frac{1.5}{0.50} = \mathbf{3.0000}$$
   $$e_{[4]}^2 = (3.0)^2 = 9.00$$

5. **Observation 5**:
   $$e_{[5]} = \frac{-0.7}{1 - 0.25} = \frac{-0.7}{0.75} \approx \mathbf{-0.933333}$$
   $$e_{[5]}^2 \approx (-0.933333)^2 \approx 0.871111$$

#### Overall LOOCV Mean Squared Error:
$$\sum_{i=1}^5 e_{[i]}^2 = 2.25 + 1.5625 + 0.221453 + 9.00 + 0.871111 = 13.905064$$

$$\text{LOOCV} = \frac{1}{5} \sum_{i=1}^5 e_{[i]}^2 = \frac{13.905064}{5} \approx \mathbf{2.7810}$$

Notice that the high-leverage observation 4 ($h_{44} = 0.50$) doubles its prediction error from $1.5$ to $3.0$, properly penalizing the model for overfitting high-leverage data points.

---

## Fully worked question 2: Exact Combinatorial Enumeration and Monte Carlo Approximation of a Two-Sample Permutation Test

### Question
An agronomist evaluates the efficacy of a bio-organic fertilizer on wheat crop yield (in metric tons per hectare) in an arid agricultural district:
- **Control Plot ($X$)**: $n_1 = 4$ observations: $\mathbf{x} = [3.2, \, 3.6, \, 4.0, \, 4.4]$
- **Treated Plot ($Y$)**: $n_2 = 4$ observations: $\mathbf{y} = [4.8, \, 5.2, \, 5.6, \, 6.0]$

The researcher tests the sharp null hypothesis $H_0$ that the bio-fertilizer has zero effect on wheat yield, against the one-sided alternative $H_1$ that the fertilizer increases yield. The chosen test statistic is the difference between group sample means:

$$T = \bar{Y} - \bar{X}$$

1. Calculate the observed test statistic $T_{obs} = \bar{y}_{obs} - \bar{x}_{obs}$.
2. Determine the total number of distinct partitions $M$ of the pooled sample into two groups of size 4.
3. Determine how many partitions yield a test statistic greater than or equal to $T_{obs}$, and compute the exact one-sided permutation $p$-value $p_{exact}$.
4. Suppose a computing system estimates the $p$-value using a Monte Carlo permutation test with $B = 1,000$ independent random permutations.
   - What is the probability that a randomly drawn permutation achieves $T^* \ge T_{obs}$?
   - What is the expected value of the Monte Carlo $p$-value $p_{MC} = \frac{1 + K}{B + 1}$?
   - Calculate the standard deviation (standard error) of the Monte Carlo $p$-value estimate.

---

### Solution, step 1: Calculate the observed test statistic T_obs

**Solution, step 1: Calculate the observed test statistic T_obs.**

1. **Mean of Control Group $\bar{x}_{obs}$**:
   $$\sum_{i=1}^4 x_i = 3.2 + 3.6 + 4.0 + 4.4 = 15.2$$
   $$\bar{x}_{obs} = \frac{15.2}{4} = 3.80 \text{ tons/ha}$$

2. **Mean of Treated Group $\bar{y}_{obs}$**:
   $$\sum_{j=1}^4 y_j = 4.8 + 5.2 + 5.6 + 6.0 = 21.6$$
   $$\bar{y}_{obs} = \frac{21.6}{4} = 5.40 \text{ tons/ha}$$

3. **Observed Difference in Means**:
   $$T_{obs} = \bar{y}_{obs} - \bar{x}_{obs} = 5.40 - 3.80 = \mathbf{1.60 \text{ tons/ha}}$$

---

### Solution, step 2: Total number of distinct partitions

**Solution, step 2: Total number of distinct partitions.**

Total sample size: $N = n_1 + n_2 = 4 + 4 = 8$.
The number of distinct ways to choose $n_2 = 4$ elements from $N = 8$ elements is given by the binomial coefficient:

$$M = \binom{N}{n_2} = \binom{8}{4} = \frac{8!}{4! \cdot 4!} = \frac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1} = \frac{1,680}{24} = \mathbf{70 \text{ partitions}}$$

There are exactly $70$ equally likely combinatorial partitions under $H_0$.

---

### Solution, step 3: Exact permutation p-value derivation

**Solution, step 3: Exact permutation p-value derivation.**

Notice the values in the pooled sample:
$$\mathbf{z} = [3.2, \, 3.6, \, 4.0, \, 4.4, \, 4.8, \, 5.2, \, 5.6, \, 6.0]$$
The elements are strictly sorted with a constant step size of $0.4$.

Every element of the treated group in the observed data is **strictly greater** than every element of the control group:
$$\min(\mathbf{y}_{obs}) = 4.8 > \max(\mathbf{x}_{obs}) = 4.4$$

Therefore, the observed treated group $\{4.8, 5.2, 5.6, 6.0\}$ consists of the **four largest elements** in the entire pooled sample!

1. To achieve a group sum $\sum y_j^* \ge \sum y_{j, obs} = 21.6$, the partition must choose elements from $\{z_1, \dots, z_8\}$ whose sum is at least $21.6$.
2. Since $21.6$ is the sum of the four largest numbers in the entire set, **no other combination of four numbers can achieve a larger or equal sum**!
3. Therefore, the partition achieving $\bar{Y}^* \ge 5.40$ is **unique**; it occurs only for the observed partition itself.
   $$\#\{m : T^{(m)} \ge T_{obs}\} = 1$$

The exact permutation $p$-value is:

$$p_{exact} = \frac{1}{M} = \frac{1}{70} \approx \mathbf{0.014286} \approx 1.43\%$$

Because $p_{exact} = 0.0143 < 0.05$, the researcher rejects the null hypothesis at the $5\%$ significance level, concluding that the bio-fertilizer produces a statistically significant yield increase.

---

### Solution, step 4: Monte Carlo permutation test properties

**Solution, step 4: Monte Carlo permutation test properties.**

In the Monte Carlo test, $B = 1,000$ permutations are sampled independently with replacement from the $M = 70$ possibilities.

1. **Probability of Success $p$**:
   For any single random permutation draw, the probability that it equals the unique maximal partition is:
   $$p = \frac{1}{70} \approx 0.0142857$$

2. **Distribution of Exceedance Count $K$**:
   The count of permutations exceeding $T_{obs}$, denoted $K = \sum_{b=1}^B \mathbb{I}(T^{*b} \ge T_{obs})$, follows a Binomial distribution:
   $$K \sim \text{Binomial}(B = 1000, \, p = 1/70)$$
   $$\mathbb{E}[K] = B \cdot p = 1000 \times \frac{1}{70} = \frac{100}{7} \approx 14.2857$$
   $$\text{Var}(K) = B \cdot p (1 - p) = 1000 \times \frac{1}{70} \times \frac{69}{70} \approx 14.2857 \times 0.985714 \approx 14.0816$$

3. **Expected Value of the Monte Carlo $p$-value**:
   The Monte Carlo $p$-value is:
   $$p_{MC} = \frac{1 + K}{B + 1} = \frac{1 + K}{1001}$$
   $$\mathbb{E}[p_{MC}] = \frac{1 + \mathbb{E}[K]}{B + 1} = \frac{1 + 14.2857}{1001} = \frac{15.2857}{1001} \approx \mathbf{0.015270}$$

4. **Standard Error of the Estimate**:
   $$\text{Var}(p_{MC}) = \text{Var}\left( \frac{1 + K}{B + 1} \right) = \frac{\text{Var}(K)}{(B + 1)^2} = \frac{14.0816}{(1001)^2} = \frac{14.0816}{1,002,001} \approx 1.40535 \times 10^{-5}$$
   $$\text{SE}(p_{MC}) = \sqrt{1.40535 \times 10^{-5}} \approx \mathbf{0.003749}$$

A $95\%$ confidence interval for the Monte Carlo estimated $p$-value with $B = 1,000$ draws is:
$$0.0153 \pm 1.96 \times 0.00375 = 0.0153 \pm 0.0073 = [0.0080, \, 0.0226]$$
Since the entire interval lies comfortably below $\alpha = 0.05$, $B = 1,000$ permutations provides decisive power to reject $H_0$.

---

## Fully worked question 3: Jackknife Bias-Reduction Proof and Derivation of the Jackknife Variance Estimator for Sample Quantiles

### Question
An actuary analyzes insurance claim severities using the sample coefficient of variation (CV):

$$\theta = \frac{\sigma}{\mu}, \quad \hat{\theta} = \frac{s}{\bar{x}}$$

where $\bar{x} = \frac{1}{n} \sum x_i$ and $s = \sqrt{\frac{1}{n-1} \sum (x_i - \bar{x})^2}$.

1. Under standard asymptotic expansions for ratio estimators, the expected value of the sample coefficient of variation satisfies:
   $$\mathbb{E}[\hat{\theta}] = \theta + \frac{a_1}{n} + \mathcal{O}(n^{-2})$$
   Prove that the Jackknife estimator:
   $$\hat{\theta}_{jack} = n \hat{\theta} - (n - 1) \bar{\theta}_{(\cdot)}$$
   strictly eliminates the $\mathcal{O}(n^{-1})$ bias term.
2. In a small loss audit of $n = 4$ claims:
   $$\mathbf{x} = [10, \, 20, \, 30, \, 60]$$
   Compute:
   - The sample mean $\bar{x}$, sample standard deviation $s$, and naive sample CV $\hat{\theta}$.
   - The four leave-one-out estimates $\hat{\theta}_{(-1)}, \dots, \hat{\theta}_{(-4)}$ and their mean $\bar{\theta}_{(\cdot)}$.
   - The Jackknife bias-corrected estimate $\hat{\theta}_{jack}$.
3. Compute Tukey's Jackknife variance estimate $v_{jack}$ and estimated standard error for $\hat{\theta}$.
4. Explain why applying the classical delete-1 jackknife to estimate the variance of the sample median $\hat{m} = \text{median}(\mathbf{x})$ fails to be statistically consistent as $n \to \infty$, and state the mathematical conditions required for jackknife consistency.

---

### Solution, step 1: Mathematical proof of bias cancellation

**Solution, step 1: Mathematical proof of bias cancellation.**

Let $\hat{\theta} = T(\mathbf{x})$ based on a sample of size $n$, with expectation:
$$\mathbb{E}[\hat{\theta}] = \theta + \frac{a_1}{n} + \frac{a_2}{n^2} + \mathcal{O}(n^{-3})$$
where $a_1, a_2$ are constants depending on population central moments.

Each leave-one-out sub-sample $\mathbf{x}_{(-i)}$ has sample size $n - 1$.
Therefore:
$$\mathbb{E}[\hat{\theta}_{(-i)}] = \theta + \frac{a_1}{n - 1} + \frac{a_2}{(n - 1)^2} + \mathcal{O}(n^{-3})$$

Taking the expectation of the average $\bar{\theta}_{(\cdot)} = \frac{1}{n} \sum_{i=1}^n \hat{\theta}_{(-i)}$:
$$\mathbb{E}[\bar{\theta}_{(\cdot)}] = \theta + \frac{a_1}{n - 1} + \frac{a_2}{(n - 1)^2} + \mathcal{O}(n^{-3})$$

Now evaluate the expectation of the Jackknife estimator $\hat{\theta}_{jack} = n \hat{\theta} - (n - 1) \bar{\theta}_{(\cdot)}$:
$$\mathbb{E}[\hat{\theta}_{jack}] = n \mathbb{E}[\hat{\theta}] - (n - 1) \mathbb{E}[\bar{\theta}_{(\cdot)}]$$
$$= n \left[ \theta + \frac{a_1}{n} + \frac{a_2}{n^2} + \mathcal{O}(n^{-3}) \right] - (n - 1) \left[ \theta + \frac{a_1}{n - 1} + \frac{a_2}{(n - 1)^2} + \mathcal{O}(n^{-3}) \right]$$
$$= \left( n \theta + a_1 + \frac{a_2}{n} \right) - \left( (n - 1)\theta + a_1 + \frac{a_2}{n - 1} \right) + \mathcal{O}(n^{-2})$$
$$= (n - (n - 1))\theta + (a_1 - a_1) + a_2 \left( \frac{1}{n} - \frac{1}{n - 1} \right) + \mathcal{O}(n^{-2})$$
$$= \theta + 0 + a_2 \left( \frac{n - 1 - n}{n (n - 1)} \right) + \mathcal{O}(n^{-2})$$
$$= \theta - \frac{a_2}{n (n - 1)} + \mathcal{O}(n^{-2}) = \theta + \mathcal{O}(n^{-2})$$

The $\mathcal{O}(n^{-1})$ term $a_1$ cancels out **identically to zero**.
This proves that the Jackknife estimator reduces the asymptotic bias from $\mathcal{O}(n^{-1})$ to $\mathcal{O}(n^{-2})$.

---

### Solution, step 2: Numerical computation of full-sample and leave-one-out CV estimates

**Solution, step 2: Numerical computation of full-sample and leave-one-out CV estimates.**

Given $\mathbf{x} = [10, \, 20, \, 30, \, 60]$ with $n = 4$:

1. **Full Sample Estimates**:
   $$\sum x_i = 10 + 20 + 30 + 60 = 120 \implies \bar{x} = \frac{120}{4} = 30.0$$
   $$\sum (x_i - \bar{x})^2 = (10 - 30)^2 + (20 - 30)^2 + (30 - 30)^2 + (60 - 30)^2$$
   $$= (-20)^2 + (-10)^2 + 0^2 + 30^2 = 400 + 100 + 0 + 900 = 1,400$$
   $$s^2 = \frac{1,400}{4 - 1} = \frac{1,400}{3} \approx 466.6667 \implies s = \sqrt{466.6667} \approx 21.6025$$
   $$\hat{\theta} = \frac{s}{\bar{x}} = \frac{21.6025}{30.0} \approx \mathbf{0.720082}$$

2. **Leave-One-Out Computations ($n - 1 = 3$)**:
   - **Delete $x_1 = 10$**: $\mathbf{x}_{(-1)} = [20, 30, 60]$.
     $$\sum = 110 \implies \bar{x}_{(-1)} = \frac{110}{3} \approx 36.6667$$
     $$\sum (x_i - \bar{x})^2 = (20 - 36.6667)^2 + (30 - 36.6667)^2 + (60 - 36.6667)^2 = 277.78 + 44.44 + 544.44 = 866.6667$$
     $$s_{(-1)}^2 = \frac{866.6667}{2} = 433.3333 \implies s_{(-1)} = 20.8167$$
     $$\hat{\theta}_{(-1)} = \frac{20.8167}{36.6667} \approx \mathbf{0.567727}$$

   - **Delete $x_2 = 20$**: $\mathbf{x}_{(-2)} = [10, 30, 60]$.
     $$\sum = 100 \implies \bar{x}_{(-2)} = \frac{100}{3} \approx 33.3333$$
     $$\sum (x_i - \bar{x})^2 = (10 - 33.3333)^2 + (30 - 33.3333)^2 + (60 - 33.3333)^2 = 544.44 + 11.11 + 711.11 = 1,266.6667$$
     $$s_{(-2)}^2 = \frac{1,266.6667}{2} = 633.3333 \implies s_{(-2)} = 25.1661$$
     $$\hat{\theta}_{(-2)} = \frac{25.1661}{33.3333} \approx \mathbf{0.754983}$$

   - **Delete $x_3 = 30$**: $\mathbf{x}_{(-3)} = [10, 20, 60]$.
     $$\sum = 90 \implies \bar{x}_{(-3)} = \frac{90}{3} = 30.0$$
     $$\sum (x_i - \bar{x})^2 = (10 - 30)^2 + (20 - 30)^2 + (60 - 30)^2 = 400 + 100 + 900 = 1,400$$
     $$s_{(-3)}^2 = \frac{1,400}{2} = 700.0 \implies s_{(-3)} = \sqrt{700} \approx 26.4575$$
     $$\hat{\theta}_{(-3)} = \frac{26.4575}{30.0} \approx \mathbf{0.881917}$$

   - **Delete $x_4 = 60$**: $\mathbf{x}_{(-4)} = [10, 20, 30]$.
     $$\sum = 60 \implies \bar{x}_{(-4)} = \frac{60}{3} = 20.0$$
     $$\sum (x_i - \bar{x})^2 = (10 - 20)^2 + (20 - 20)^2 + (30 - 20)^2 = 100 + 0 + 100 = 200$$
     $$s_{(-4)}^2 = \frac{200}{2} = 100.0 \implies s_{(-4)} = 10.0$$
     $$\hat{\theta}_{(-4)} = \frac{10.0}{20.0} = \mathbf{0.500000}$$

3. **Average of Leave-One-Out Replications $\bar{\theta}_{(\cdot)}$**:
   $$\sum_{i=1}^4 \hat{\theta}_{(-i)} = 0.567727 + 0.754983 + 0.881917 + 0.500000 = 2.704627$$
   $$\bar{\theta}_{(\cdot)} = \frac{2.704627}{4} \approx \mathbf{0.676157}$$

4. **Jackknife Bias-Corrected Point Estimate**:
   $$\hat{\theta}_{jack} = 4 \hat{\theta} - 3 \bar{\theta}_{(\cdot)} = 4(0.720082) - 3(0.676157) = 2.880328 - 2.028471 = \mathbf{0.851857}$$

---

### Solution, step 3: Tukey's Jackknife variance and standard error

**Solution, step 3: Tukey's Jackknife variance and standard error.**

Tukey's variance formula is:
$$v_{jack} = \frac{n - 1}{n} \sum_{i=1}^n (\hat{\theta}_{(-i)} - \bar{\theta}_{(\cdot)})^2 = \frac{3}{4} \sum_{i=1}^4 (\hat{\theta}_{(-i)} - 0.676157)^2$$

Compute the squared deviations around $\bar{\theta}_{(\cdot)} = 0.676157$:
- $(\hat{\theta}_{(-1)} - \bar{\theta}_{(\cdot)})^2 = (0.567727 - 0.676157)^2 = (-0.108430)^2 \approx 0.011757$
- $(\hat{\theta}_{(-2)} - \bar{\theta}_{(\cdot)})^2 = (0.754983 - 0.676157)^2 = (0.078826)^2 \approx 0.006214$
- $(\hat{\theta}_{(-3)} - \bar{\theta}_{(\cdot)})^2 = (0.881917 - 0.676157)^2 = (0.205760)^2 \approx 0.042337$
- $(\hat{\theta}_{(-4)} - \bar{\theta}_{(\cdot)})^2 = (0.500000 - 0.676157)^2 = (-0.176157)^2 \approx 0.031031$

Sum of squared deviations:
$$\sum_{i=1}^4 (\hat{\theta}_{(-i)} - \bar{\theta}_{(\cdot)})^2 = 0.011757 + 0.006214 + 0.042337 + 0.031031 = 0.091339$$

Now multiply by $\frac{n - 1}{n} = \frac{3}{4} = 0.75$:

$$v_{jack} = 0.75 \times 0.091339 = \mathbf{0.068504}$$

Estimated Jackknife Standard Error:
$$\text{SE}_{jack}(\hat{\theta}) = \sqrt{0.068504} \approx \mathbf{0.2617}$$

---

### Solution, step 4: Theoretical explanation of Jackknife breakdown on the sample median

**Solution, step 4: Theoretical explanation of Jackknife breakdown on the sample median.**

#### The Non-Smoothness Pathology:
The mathematical foundation of the Jackknife relies on **Fréchet differentiability** (or Hadamard differentiability) of the statistical functional $T(F)$. 
- For smooth functionals (means, variances, regression parameters), a small perturbation in data weights produces a smooth, linear change in the estimator. The influence function $L(x) = \lim_{\epsilon \to 0} \frac{T((1-\epsilon)F + \epsilon \delta_x) - T(F)}{\epsilon}$ is well-behaved, and deleting one observation perturbs the estimate by $\mathcal{O}(n^{-1})$.

For the **sample median**, however:
$$T(F) = F^{-1}(1/2)$$
The median functional is **non-smooth and step-discontinuous**.
- Deleting an observation shifts the median index by at most half a step. In a sample of size $n$, the leave-one-out median $\hat{\theta}_{(-i)}$ takes only two discrete values ($x_{(m)}$ and $x_{(m+1)}$).
- The difference $\hat{\theta}_{(-i)} - \bar{\theta}_{(\cdot)}$ is governed entirely by the single gap between the two central order statistics: $x_{(m+1)} - x_{(m)}$.
- In probability theory, the spacing between adjacent order statistics $n (X_{(m+1)} - X_{(m)})$ converges in distribution to an **Exponential random variable**, rather than concentrating around zero.
- Consequently, Tukey's jackknife variance estimator $v_{jack}$ remains random and stochastic as $n \to \infty$; it does **not** converge to the true asymptotic variance $\frac{1}{4 n f(m)^2}$.

#### Mathematical Conditions for Jackknife Consistency:
For the delete-1 Jackknife variance estimator to be consistent ($v_{jack} \xrightarrow{P} \text{Var}(\hat{\theta})$), the functional $T(F)$ must be **locally linear with a square-integrable influence function**:
$$\int [L_F(x)]^2 dF(x) < \infty$$
When this condition is violated (as with quantiles, extreme value statistics, and support boundaries), statisticians must deploy the **Bootstrap** or the **Delete-$d$ Jackknife** where $d / n \to 0$ but $d \to \infty$.
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(unit6_text)

print("Successfully written deep Unit 6!")
