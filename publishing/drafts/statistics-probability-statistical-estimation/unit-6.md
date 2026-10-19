# Unit 6: Interval Estimation: Pivotal Quantities & Exact Confidence Sets

A point estimator delivers a single numerical guess for an unknown parameter, but offers no internal measure of its own precision or reliability. In scientific inquiry and decision engineering, quantifying the margin of uncertainty is indispensable. Jerzy Neyman (1937) established the classical mathematical theory of **interval estimation**, replacing isolated point guesses with random intervals designed to bracket the unknown parameter with a pre-assigned, mathematically guaranteed probability. In this unit, we rigorously formulate the concepts of confidence intervals, coverage probabilities, and confidence coefficients, develop the pivotal quantity method, derive exact confidence intervals for univariate and bivariate normal parameters, analyze the celebrated Behrens–Fisher problem and Welch–Satterthwaite approximation, explore Neyman's duality between confidence sets and hypothesis testing, and characterize shortest-length and Uniformly Most Accurate (UMA) confidence sets.

## 6.1 Concepts of Interval Estimation: Coverage Probability, Confidence Coefficients, and Confidence Belts

Let $(\mathcal{X}, \mathcal{A}, \mathcal{P})$ be a statistical experiment where $\mathbf{X} = (X_1, \dots, X_n) \sim P_\theta$ with $\theta \in \Theta \subseteq \mathbb{R}$.
An **interval estimator** for a scalar parameter $\tau(\theta)$ is a pair of observable statistics $L(\mathbf{X})$ and $U(\mathbf{X})$ satisfying:

$$\mathbb{P}_\theta(L(\mathbf{X}) \le U(\mathbf{X})) = 1 \quad \forall \theta \in \Theta$$

The realization $[L(\mathbf{x}), U(\mathbf{x})]$ computed from observed empirical data $\mathbf{x}$ is termed a **confidence interval**.

### Coverage Probability and Confidence Coefficient
Prior to data collection, the interval bounds $L(\mathbf{X})$ and $U(\mathbf{X})$ are random variables; the parameter $\tau(\theta)$ is a fixed, non-random constant. The **coverage probability function** of the interval estimator is:

$$C(\theta) = \mathbb{P}_\theta\left( L(\mathbf{X}) \le \tau(\theta) \le U(\mathbf{X}) \right)$$

The **confidence coefficient** (or nominal confidence level), denoted $1 - \alpha$ with $\alpha \in (0, 1)$, is the infimum of the coverage probability over the entire parameter space:

$$1 - \alpha = \inf_{\theta \in \Theta} C(\theta) = \inf_{\theta \in \Theta} \mathbb{P}_\theta\left( L(\mathbf{X}) \le \tau(\theta) \le U(\mathbf{X}) \right)$$

If $C(\theta) = 1 - \alpha$ identically for all $\theta \in \Theta$, the interval is said to be an **exact $(1 - \alpha)$ confidence interval**. If $C(\theta) \ge 1 - \alpha$ for all $\theta$, the interval is **conservative**. If $C(\theta) < 1 - \alpha$ for some parameter values, the interval is **anticonservative** or liberal, exhibiting coverage failure.

### Frequentist Interpretation of Confidence
A notorious epistemological pitfall in applied statistics is the misinterpretation of realized confidence intervals. Once experimental data $\mathbf{x}$ are collected and specific numbers are evaluated—such as $[12.4, 15.8]$—it is mathematically meaningless in frequentist probability to assert that *"there is a $95\%$ probability that the true parameter $\theta$ lies between $12.4$ and $15.8$."*
The parameter $\theta$ is not a random variable; it is an objective, deterministic state of nature. The realized interval $[12.4, 15.8]$ either contains $\theta$ or it does not: the conditional probability is either $1$ or $0$.
The correct frequentist interpretation is:
**If the identical experiment is repeated indefinitely under identical conditions, generating an infinite sequence of independent intervals $[L(\mathbf{X}^{(k)}), U(\mathbf{X}^{(k)})]$, exactly $100(1 - \alpha)\%$ of the resulting random intervals will successfully contain the fixed true parameter $\theta$.**

### Neyman's Confidence Belt
Jerzy Neyman visualized interval estimation through a **confidence belt** in the $(\mathbf{x}, \theta)$ plane. For each fixed parameter value $\theta_0$, define an acceptance interval in the sample space:

$$A(\theta_0) = \{ \mathbf{x} \in \mathcal{X} : c_1(\theta_0) \le T(\mathbf{x}) \le c_2(\theta_0) \}$$

such that $\mathbb{P}_{\theta_0}(T(\mathbf{X}) \in A(\theta_0)) = 1 - \alpha$.
Plotting the curves $c_1(\theta)$ and $c_2(\theta)$ against $\theta$ traces out a two-dimensional confidence belt. Once a specific numerical statistic $t = T(\mathbf{x})$ is observed on the horizontal axis, projecting vertically intersects the boundaries of the belt at two points: $\theta_L(t)$ and $\theta_U(t)$. Inverting the confidence belt produces the confidence set:

$$S(\mathbf{x}) = \{ \theta \in \Theta : \mathbf{x} \in A(\theta) \} = [\theta_L(t), \theta_U(t)]$$

## 6.2 The Pivotal Quantity Method: Exact Pivots and Distribution Invariance

The most powerful and elegant analytical tool for constructing exact confidence intervals in parametric models is the **Pivotal Quantity Method**, formulated by R. A. Fisher (1930).

### Definition of a Pivotal Quantity
A function of the sample data $\mathbf{X}$ and the unknown parameter $\theta$, denoted $Q(\mathbf{X}, \theta)$, is called a **pivotal quantity** (or simply a **pivot**) if its probability distribution is completely independent of $\theta$ (and any nuisance parameters).

Crucially, a pivot must satisfy two distinct conditions:
1. $Q(\mathbf{x}, \theta)$ must depend explicitly on both the data $\mathbf{x}$ and the unknown parameter $\theta$.
2. The probability law governing the random variable $Q(\mathbf{X}, \theta)$ under $P_\theta$ must be a fixed, known distribution containing zero unknown parameters (e.g., standard normal $\mathcal{N}(0, 1)$, Student's $t_\nu$, Chi-square $\chi_\nu^2$, or Snedecor's $F_{\nu_1, \nu_2}$).

### Constructing Confidence Intervals via Inversion of Pivots
Let $Q(\mathbf{X}, \theta)$ be a pivotal quantity with known continuous cumulative distribution function $F_Q(q)$.
For any chosen significance level $\alpha \in (0, 1)$, we can select two critical values $q_1 < q_2$ from the known distribution of $Q$ such that:

$$\mathbb{P}(q_1 \le Q(\mathbf{X}, \theta) \le q_2) = F_Q(q_2) - F_Q(q_1) = 1 - \alpha$$

Typically, one selects symmetric tail probabilities: $F_Q(q_1) = \alpha / 2$ and $F_Q(q_2) = 1 - \alpha / 2$, so $q_1 = q_{\alpha/2}$ and $q_2 = q_{1 - \alpha/2}$.
Now, assume that for every sample realization $\mathbf{x}$, the function $Q(\mathbf{x}, \theta)$ is a strictly monotonic function of $\theta$. Then the algebraic inequality:

$$q_1 \le Q(\mathbf{X}, \theta) \le q_2$$

can be inverted to isolate $\theta$:
- If $Q(\mathbf{x}, \theta)$ is strictly decreasing in $\theta$:
  $$q_1 \le Q(\mathbf{X}, \theta) \le q_2 \iff Q^{-1}(\mathbf{X}, q_2) \le \theta \le Q^{-1}(\mathbf{X}, q_1)$$
- If $Q(\mathbf{x}, \theta)$ is strictly increasing in $\theta$:
  $$q_1 \le Q(\mathbf{X}, \theta) \le q_2 \iff Q^{-1}(\mathbf{X}, q_1) \le \theta \le Q^{-1}(\mathbf{X}, q_2)$$

Setting $L(\mathbf{X}) = Q^{-1}(\mathbf{X}, q_2)$ and $U(\mathbf{X}) = Q^{-1}(\mathbf{X}, q_1)$ yields an exact $(1 - \alpha)$ confidence interval:

$$\mathbb{P}_\theta(L(\mathbf{X}) \le \theta \le U(\mathbf{X})) = \mathbb{P}(q_1 \le Q(\mathbf{X}, \theta) \le q_2) = 1 - \alpha$$

## 6.3 Exact Confidence Intervals for the Normal Mean (Known Variance)

Consider an i.i.d. random sample $X_1, X_2, \dots, X_n$ from a Gaussian distribution $\mathcal{N}(\mu, \sigma_0^2)$ where the population variance $\sigma_0^2$ is known. The sample mean is $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$.

### The Standard Normal Pivot
By linear combination properties of Gaussian variables:

$$\bar{X} \sim \mathcal{N}\left( \mu, \frac{\sigma_0^2}{n} \right)$$

Standardizing $\bar{X}$ produces the pivotal quantity:

$$Z(\mathbf{X}, \mu) = \frac{\bar{X} - \mu}{\sigma_0 / \sqrt{n}}$$

Notice that $Z$ depends on both the data (via $\bar{X}$) and the unknown parameter $\mu$.
Its sampling distribution is strictly standard normal:

$$Z(\mathbf{X}, \mu) \sim \mathcal{N}(0, 1)$$

which contains zero unknown parameters. Thus $Z$ is an exact pivot!

### Inversion and Interval Construction
Let $z_{1 - \alpha/2}$ denote the $(1 - \alpha/2)$-quantile of the standard normal distribution, such that $\Phi(z_{1 - \alpha/2}) = 1 - \alpha/2$. By symmetry of the Gaussian density about zero:

$$\mathbb{P}\left( -z_{1 - \alpha/2} \le \frac{\bar{X} - \mu}{\sigma_0 / \sqrt{n}} \le z_{1 - \alpha/2} \right) = 1 - \alpha$$

Multiply across the compound inequality by the standard error $\frac{\sigma_0}{\sqrt{n}} > 0$:

$$-z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}} \le \bar{X} - \mu \le z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}}$$

Subtract $\bar{X}$ from all three parts:

$$-\bar{X} - z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}} \le -\mu \le -\bar{X} + z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}}$$

Multiplying by $-1$ reverses the inequalities:

$$\bar{X} - z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}} \le \mu \le \bar{X} + z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}}$$

The exact $100(1 - \alpha)\%$ confidence interval for the population mean $\mu$ is:

$$\left[ \bar{X} - z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}}, \, \bar{X} + z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}} \right]$$

### Geometric Properties
1. **Symmetry**: The interval is centered precisely at the sample mean $\bar{X}$.
2. **Deterministic Width**: The length of the interval is:
   $$W = 2 z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}}$$
   Notice that the interval width $W$ is a deterministic constant: it does not depend on the observed data values!
3. **Sample Size Determination**: If an experimenter demands that the margin of error not exceed a bound $E$, setting $z_{1 - \alpha/2} \frac{\sigma_0}{\sqrt{n}} \le E$ yields the exact required sample size:
   $$n \ge \left( \frac{z_{1 - \alpha/2} \sigma_0}{E} \right)^2$$

## 6.4 Exact Confidence Intervals for the Normal Mean (Unknown Variance: Student's $t$)

In real scientific experiments, the population variance $\sigma^2$ is almost never known with certainty. If we attempt to use $Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$, the quantity involves the unknown nuisance parameter $\sigma$, rendering it unusable as a pivot.
If we substitute the sample standard deviation $S = \sqrt{\frac{1}{n-1} \sum (X_i - \bar{X})^2}$, what is the exact distribution of the resulting ratio?

### Derivation of Student's $t$ Pivot (Gosset, 1908)
Consider the Studentized statistic:

$$T(\mathbf{X}, \mu) = \frac{\bar{X} - \mu}{S / \sqrt{n}}$$

We decompose $T$ algebraically as follows:

$$T = \frac{\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}}{\sqrt{\frac{(n-1)S^2 / \sigma^2}{n-1}}} = \frac{Z}{\sqrt{V / \nu}}$$

where:
1. $Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0, 1)$ is standard normal.
2. $V = \frac{(n-1)S^2}{\sigma^2} \sim \chi_{n-1}^2$ is Chi-square with $\nu = n - 1$ degrees of freedom.
3. By Basu's Theorem (or Cochran's Theorem), the sample mean $\bar{X}$ and sample variance $S^2$ are mutually independent! Therefore, the numerator $Z$ and denominator $V$ are strictly independent random variables.

By definition, the ratio of a standard normal variable to the square root of an independent Chi-square variable divided by its degrees of freedom follows **Student's $t$-distribution** with $\nu = n - 1$ degrees of freedom:

$$T(\mathbf{X}, \mu) = \frac{\bar{X} - \mu}{S / \sqrt{n}} \sim t_{n-1}$$

The distribution $t_{n-1}$ depends only on the known sample size $n$, and is completely independent of both unknown parameters $\mu$ and $\sigma^2$. Thus $T$ is an **exact pivotal quantity**!

### Exact Interval Construction
Let $t_{n-1, 1 - \alpha/2}$ denote the $(1 - \alpha/2)$-critical value from the Student's $t$-distribution with $n - 1$ degrees of freedom:

$$\mathbb{P}\left( -t_{n-1, 1-\alpha/2} \le \frac{\bar{X} - \mu}{S / \sqrt{n}} \le t_{n-1, 1-\alpha/2} \right) = 1 - \alpha$$

Inverting the inequality yields the exact $100(1 - \alpha)\%$ confidence interval for $\mu$:

$$\left[ \bar{X} - t_{n-1, 1-\alpha/2} \frac{S}{\sqrt{n}}, \, \bar{X} + t_{n-1, 1-\alpha/2} \frac{S}{\sqrt{n}} \right]$$

### Comparison with Known Variance Case
Because Student's $t$-distribution incorporates the additional sampling variability of estimating $\sigma$ by $S$, its probability density has heavier tails than the standard normal distribution. Consequently:

$$t_{n-1, 1 - \alpha/2} > z_{1 - \alpha/2} \quad \forall n < \infty$$

The confidence interval is wider, formalizing the penalty of variance uncertainty. Furthermore, the length of the interval $W = 2 t_{n-1, 1-\alpha/2} \frac{S}{\sqrt{n}}$ is a random variable that varies from sample to sample according to the realized sample variance $S^2$. As $n \to \infty$, by Slutsky's Theorem, $S \xrightarrow{P} \sigma$ and $t_{n-1} \xrightarrow{d} \mathcal{N}(0, 1)$, recovering the Gaussian interval.


### Paired-Sample Inferences and Matched-Pairs Design
In many experimental settings, observations in two groups are not independent, but intrinsically linked. For example, in a medical study of an antihypertensive compound, systolic blood pressure is recorded on the same $n$ patients before treatment ($X_i$) and after treatment ($Y_i$).
Because observations $(X_i, Y_i)$ are coupled on the same subject, they exhibit positive correlation $\text{Cov}(X_i, Y_i) = \rho \sigma_X \sigma_Y > 0$.
Applying a naive two-sample independent pooled $t$-interval would be catastrophic: the variance of the difference under independence is $\frac{\sigma_X^2 + \sigma_Y^2}{n}$, whereas the true variance of the pairwise difference is:

$$\text{Var}(X_i - Y_i) = \sigma_X^2 + \sigma_Y^2 - 2 \rho \sigma_X \sigma_Y < \sigma_X^2 + \sigma_Y^2$$

To exploit this variance reduction, we define the univariate difference series:

$$D_i = X_i - Y_i, \quad i = 1, 2, \dots, n$$

Assuming $D_i \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(\mu_D, \sigma_D^2)$ where $\mu_D = \mu_X - \mu_Y$, the problem reduces to a single-sample Student's $t$ inference on the differences:
- Sample mean difference: $\bar{D} = \frac{1}{n} \sum_{i=1}^n D_i = \bar{X} - \bar{Y}$
- Sample standard deviation of differences: $S_D = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (D_i - \bar{D})^2}$

The exact $100(1 - \alpha)\%$ paired $t$ confidence interval for $\mu_D$ is:

$$\left[ \bar{D} - t_{n-1, 1 - \alpha/2} \frac{S_D}{\sqrt{n}}, \quad \bar{D} + t_{n-1, 1 - \alpha/2} \frac{S_D}{\sqrt{n}} \right]$$

By subtracting out subject-specific baseline variability, the matched-pairs design dramatically narrows the confidence interval, yielding immense statistical power.

## 6.5 Exact Confidence Intervals for the Normal Variance and Precision (Chi-Square)

Now suppose the primary parameter of scientific interest is the population variance $\sigma^2$ (or population standard deviation $\sigma$, or precision $\tau = 1/\sigma^2$), while the mean $\mu$ is an unknown nuisance parameter.

### The Chi-Square Pivot
Recall from normal sample distribution theory that:

$$V(\mathbf{X}, \sigma^2) = \frac{(n - 1)S^2}{\sigma^2} = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{\sigma^2}$$

follows a **Chi-square distribution** with $\nu = n - 1$ degrees of freedom:

$$V(\mathbf{X}, \sigma^2) \sim \chi_{n-1}^2$$

Because the distribution $\chi_{n-1}^2$ depends solely on the sample size $n$ and contains neither $\mu$ nor $\sigma^2$, $V(\mathbf{X}, \sigma^2)$ is an exact pivotal quantity for $\sigma^2$.

### Inversion and Interval Construction
Unlike the Gaussian and Student's $t$ distributions, the Chi-square distribution is strictly non-negative and asymmetric (skewed to the right).
To construct an exact $(1 - \alpha)$ confidence interval, select two critical cutoffs $\chi_{n-1, \alpha/2}^2$ and $\chi_{n-1, 1 - \alpha/2}^2$ from the lower and upper tails:

$$\mathbb{P}\left( \chi_{n-1, \alpha/2}^2 \le \frac{(n - 1)S^2}{\sigma^2} \le \chi_{n-1, 1 - \alpha/2}^2 \right) = 1 - \alpha$$

where $\mathbb{P}(\chi_{n-1}^2 \le \chi_{n-1, \alpha/2}^2) = \alpha / 2$ and $\mathbb{P}(\chi_{n-1}^2 \le \chi_{n-1, 1 - \alpha/2}^2) = 1 - \alpha / 2$.
Invert the compound inequality by taking reciprocals (which reverses the inequalities):

$$\frac{1}{\chi_{n-1, 1 - \alpha/2}^2} \le \frac{\sigma^2}{(n - 1)S^2} \le \frac{1}{\chi_{n-1, \alpha/2}^2}$$

Multiplying through by $(n - 1)S^2 > 0$ yields the exact $100(1 - \alpha)\%$ confidence interval for $\sigma^2$:

$$\left[ \frac{(n - 1)S^2}{\chi_{n-1, 1 - \alpha/2}^2}, \, \frac{(n - 1)S^2}{\chi_{n-1, \alpha/2}^2} \right]$$

### Confidence Intervals for Standard Deviation and Precision
By the monotonicity of the square root function, the exact $100(1 - \alpha)\%$ confidence interval for the population standard deviation $\sigma$ is obtained by taking the square roots of the endpoints:

$$\left[ \sqrt{\frac{(n - 1)S^2}{\chi_{n-1, 1 - \alpha/2}^2}}, \, \sqrt{\frac{(n - 1)S^2}{\chi_{n-1, \alpha/2}^2}} \right]$$

Similarly, inverting the variance endpoints gives the exact confidence interval for the precision parameter $\tau = \frac{1}{\sigma^2}$:

$$\left[ \frac{\chi_{n-1, \alpha/2}^2}{(n - 1)S^2}, \, \frac{\chi_{n-1, 1 - \alpha/2}^2}{(n - 1)S^2} \right]$$

Notice that because the Chi-square density is asymmetric, equal-tailed cutoffs do not minimize the expected interval length $\mathbb{E}[U - L]$. Tate and Klett (1959) tabulated shortest-length critical values $(c_1, c_2)$ that satisfy the optimality condition $f_{\chi^2}(c_1) c_1^2 = f_{\chi^2}(c_2) c_2^2$, producing strictly shorter confidence intervals for $\sigma^2$.

## 6.6 Two-Sample Normal Inferences: Difference of Means with Equal Variances (Pooled $t$)

In comparative scientific experiments (such as clinical drug trials or agricultural A/B treatments), researchers compare two independent groups:
- Sample 1: $X_1, \dots, X_{n_1} \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(\mu_1, \sigma^2)$
- Sample 2: $Y_1, \dots, Y_{n_2} \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(\mu_2, \sigma^2)$
where both populations share a common, unknown variance $\sigma^2$.
The target parameter is the difference in population means $\tau = \mu_1 - \mu_2$.

### The Pooled Sample Variance
The point estimator of $\mu_1 - \mu_2$ is $\bar{X} - \bar{Y}$. Its variance is:

$$\text{Var}(\bar{X} - \bar{Y}) = \text{Var}(\bar{X}) + \text{Var}(\bar{Y}) = \frac{\sigma^2}{n_1} + \frac{\sigma^2}{n_2} = \sigma^2 \left( \frac{1}{n_1} + \frac{1}{n_2} \right)$$

To estimate the common variance $\sigma^2$, we pool the sum of squared deviations from both samples:

$$S_p^2 = \frac{\sum_{i=1}^{n_1} (X_i - \bar{X})^2 + \sum_{j=1}^{n_2} (Y_j - \bar{Y})^2}{(n_1 - 1) + (n_2 - 1)} = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}$$

Because $\frac{(n_1 - 1)S_1^2}{\sigma^2} \sim \chi_{n_1 - 1}^2$ and $\frac{(n_2 - 1)S_2^2}{\sigma^2} \sim \chi_{n_2 - 1}^2$ are independent, their sum is Chi-square:

$$\frac{(n_1 + n_2 - 2)S_p^2}{\sigma^2} \sim \chi_{n_1 + n_2 - 2}^2$$

### The Two-Sample Pooled $t$ Pivot
Forming the Studentized ratio:

$$T = \frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t_{n_1 + n_2 - 2}$$

Inverting this exact pivot yields the exact $100(1 - \alpha)\%$ confidence interval for $\mu_1 - \mu_2$:

$$\left[ (\bar{X} - \bar{Y}) - t_{n_1 + n_2 - 2, 1 - \alpha/2} S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}, \quad (\bar{X} - \bar{Y}) + t_{n_1 + n_2 - 2, 1 - \alpha/2} S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}} \right]$$

## 6.7 The Behrens–Fisher Problem and Welch–Satterthwaite Approximation

What if the two populations possess **unequal, unknown variances** $\sigma_1^2 \ne \sigma_2^2$?
This is the celebrated **Behrens–Fisher Problem**, which baffled Ronald Fisher, Jerzy Neyman, and Harold Jeffreys.
When $\sigma_1^2 \ne \sigma_2^2$, the true variance of $\bar{X} - \bar{Y}$ is:

$$\text{Var}(\bar{X} - \bar{Y}) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$$

The natural plug-in standard error is:

$$\text{SE} = \sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}$$

Consider the ratio:

$$T^* = \frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}}$$

Remarkably, Linnik (1966) proved that **no exact pivotal quantity exists for $\mu_1 - \mu_2$ based on sufficient statistics**! The distribution of $T^*$ depends on the unknown variance ratio $\theta = \sigma_1^2 / \sigma_2^2$.

### The Welch–Satterthwaite Solution
B. L. Welch (1938) and F. E. Satterthwaite (1946) proposed approximating the distribution of the denominator variance $V = \frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}$ by a scaled Chi-square distribution $\frac{c \chi_\nu^2}{\nu}$ by matching the first two moments:

$$\mathbb{E}[V] = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$$

$$\text{Var}(V) = \text{Var}\left( \frac{S_1^2}{n_1} \right) + \text{Var}\left( \frac{S_2^2}{n_2} \right) = \frac{2\sigma_1^4}{n_1^2 (n_1 - 1)} + \frac{2\sigma_2^4}{n_2^2 (n_2 - 1)}$$

Matching $\text{Var}(V) = \frac{2(\mathbb{E}[V])^2}{\nu}$ yields the **Welch–Satterthwaite effective degrees of freedom**:

$$\nu^* = \frac{\left( \frac{S_1^2}{n_1} + \frac{S_2^2}{n_2} \right)^2}{\frac{(S_1^2 / n_1)^2}{n_1 - 1} + \frac{(S_2^2 / n_2)^2}{n_2 - 1}}$$

The approximate $100(1 - \alpha)\%$ Welch confidence interval is:

$$\left[ (\bar{X} - \bar{Y}) - t_{\nu^*, 1 - \alpha/2} \sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}, \quad (\bar{X} - \bar{Y}) + t_{\nu^*, 1 - \alpha/2} \sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}} \right]$$

Notice that $\min(n_1 - 1, n_2 - 1) \le \nu^* \le n_1 + n_2 - 2$. In modern applied statistics, Welch's interval is almost universally preferred over the pooled $t$-interval because it maintains robust, near-exact nominal coverage even when variances differ by orders of magnitude.


### Fieller's Theorem for the Ratio of Two Normal Means
A notoriously difficult problem in bioassay, pharmacokinetics, and econometrics is estimating the ratio of two population means:

$$\theta = \frac{\mu_1}{\mu_2}$$

for example, the relative potency of two pharmaceutical formulations or the price elasticity of demand.
Let $(\bar{X}_1, \bar{X}_2)$ be sample means from bivariate normal data with known or estimated covariance matrix $\text{Var}(\bar{X}_1) = v_{11}$, $\text{Var}(\bar{X}_2) = v_{22}$, and $\text{Cov}(\bar{X}_1, \bar{X}_2) = v_{12}$.
A naive plug-in estimator $\hat{\theta} = \bar{X}_1 / \bar{X}_2$ has a Cauchy-like heavy-tailed distribution with infinite mean and infinite variance!
E. C. Fieller (1940, 1954) resolved this problem by constructing an exact linear pivot. Consider the auxiliary quantity:

$$Y(\theta) = \bar{X}_1 - \theta \bar{X}_2$$

Notice that $\mathbb{E}[Y(\theta)] = \mu_1 - \theta \mu_2 = \mu_1 - \left( \frac{\mu_1}{\mu_2} \right) \mu_2 = 0$.
The variance of $Y(\theta)$ is:

$$v(\theta) = \text{Var}(Y(\theta)) = v_{11} - 2 \theta v_{12} + \theta^2 v_{22}$$

The standardized statistic follows an exact Student's $t$ (or standard normal) distribution:

$$T(\theta) = \frac{\bar{X}_1 - \theta \bar{X}_2}{\sqrt{v_{11} - 2 \theta v_{12} + \theta^2 v_{22}}} \sim t_\nu$$

Inverting $T(\theta)^2 \le t_{\nu, 1-\alpha/2}^2 = t^2$ produces a quadratic inequality in $\theta$:

$$(\bar{X}_1 - \theta \bar{X}_2)^2 \le t^2 (v_{11} - 2 \theta v_{12} + \theta^2 v_{22})$$

$$(\bar{X}_2^2 - t^2 v_{22}) \theta^2 - 2(\bar{X}_1 \bar{X}_2 - t^2 v_{12}) \theta + (\bar{X}_1^2 - t^2 v_{11}) \le 0$$

Let $A = \bar{X}_2^2 - t^2 v_{22}$, $B = \bar{X}_1 \bar{X}_2 - t^2 v_{12}$, and $C = \bar{X}_1^2 - t^2 v_{11}$.
Depending on whether $A > 0$ or $A \le 0$, Fieller's theorem generates three distinct geometric topologies:
1. **Bounded Interval ($A > 0$)**: If the denominator $\bar{X}_2$ is significantly different from zero at level $\alpha$ ($t_{\text{denom}}^2 = \bar{X}_2^2 / v_{22} > t^2$), the parabola opens upward, yielding a standard finite confidence interval:
   $$\left[ \frac{B - \sqrt{B^2 - AC}}{A}, \quad \frac{B + \sqrt{B^2 - AC}}{A} \right]$$
2. **Complement of an Interval ($A < 0, B^2 - AC > 0$)**: If the denominator is not significantly different from zero, the confidence set is the union of two unbounded rays $(-\infty, \theta_1] \cup [\theta_2, \infty)$.
3. **The Entire Real Line ($A < 0, B^2 - AC < 0$)**: If neither the numerator nor denominator is distinguishable from zero, the confidence set is $(-\infty, \infty)$.
Fieller's theorem demonstrates that demanding guaranteed frequentist coverage for non-linear ratios inherently requires accepting unbounded confidence sets when data carry insufficient information.

## 6.8 Ratio of Two Normal Variances via the Snedecor-Fisher $F$-Distribution

To compare the precision or dispersion of two independent normal populations, the target parameter is the variance ratio:

$$\lambda = \frac{\sigma_1^2}{\sigma_2^2}$$

### The $F$-Distribution Pivot
Recall that $V_1 = \frac{(n_1 - 1)S_1^2}{\sigma_1^2} \sim \chi_{n_1 - 1}^2$ and $V_2 = \frac{(n_2 - 1)S_2^2}{\sigma_2^2} \sim \chi_{n_2 - 1}^2$ are independent.
The ratio of two independent Chi-square variables divided by their degrees of freedom follows **Snedecor's $F$-distribution**:

$$F = \frac{V_1 / (n_1 - 1)}{V_2 / (n_2 - 1)} = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} = \frac{S_1^2}{S_2^2} \frac{\sigma_2^2}{\sigma_1^2} = \frac{S_1^2}{S_2^2} \frac{1}{\lambda} \sim F_{n_1 - 1, n_2 - 1}$$

Because the distribution $F_{n_1 - 1, n_2 - 1}$ depends solely on sample sizes $n_1$ and $n_2$, this ratio is an **exact pivotal quantity** for $\lambda = \frac{\sigma_1^2}{\sigma_2^2}$.

### Inversion and Interval Construction
Select critical values $F_{n_1 - 1, n_2 - 1, \alpha/2}$ and $F_{n_1 - 1, n_2 - 1, 1 - \alpha/2}$:

$$\mathbb{P}\left( F_{n_1 - 1, n_2 - 1, \alpha/2} \le \frac{S_1^2}{S_2^2} \frac{1}{\lambda} \le F_{n_1 - 1, n_2 - 1, 1 - \alpha/2} \right) = 1 - \alpha$$

Inverting yields the exact $100(1 - \alpha)\%$ confidence interval for $\frac{\sigma_1^2}{\sigma_2^2}$:

$$\left[ \frac{S_1^2}{S_2^2} \frac{1}{F_{n_1 - 1, n_2 - 1, 1 - \alpha/2}}, \quad \frac{S_1^2}{S_2^2} \frac{1}{F_{n_1 - 1, n_2 - 1, \alpha/2}} \right]$$

Using the reciprocal property of $F$-quantiles, $F_{\nu_1, \nu_2, \alpha/2} = \frac{1}{F_{\nu_2, \nu_1, 1 - \alpha/2}}$, the interval can be rewritten equivalently as:

$$\left[ \frac{S_1^2}{S_2^2} \frac{1}{F_{n_1 - 1, n_2 - 1, 1 - \alpha/2}}, \quad \frac{S_1^2}{S_2^2} F_{n_2 - 1, n_1 - 1, 1 - \alpha/2} \right]$$


### Equivariant Interval Estimation in Location-Scale Families
In a location-scale family $f(x; \mu, \sigma) = \frac{1}{\sigma} f_0\left( \frac{x - \mu}{\sigma} \right)$, physical measurements are subject to changes in measurement origin (translation $X \to X + c$) and scale units (dilation $X \to a X$ for $a > 0$).
A confidence interval $[L(\mathbf{X}), U(\mathbf{X})]$ is said to be **equivariant** under the affine group if:

$$L(a \mathbf{X} + c \mathbf{1}) = a L(\mathbf{X}) + c \quad \text{and} \quad U(a \mathbf{X} + c \mathbf{1}) = a U(\mathbf{X}) + c$$

E. J. G. Pitman (1939) proved that every equivariant estimator and confidence interval can be expressed in terms of the sample mean $\bar{X}$, sample standard deviation $S$, and the **configuration ancillary statistic**:

$$\mathbf{C} = \left( \frac{X_1 - \bar{X}}{S}, \frac{X_2 - \bar{X}}{S}, \dots, \frac{X_n - \bar{X}}{S} \right)$$

The optimal equivariant confidence interval conditions on the realized configuration vector $\mathbf{C} = \mathbf{c}$, adjusting the interval width to the exact geometric shape of the realized data sample. For non-normal location-scale distributions (such as Cauchy, logistic, or extreme value distributions), Pitman's conditional equivariant intervals provide exact confidence levels that strictly dominate unconditional intervals.


### Equivariant Interval Estimation in Location-Scale Families
In a location-scale family $f(x; \mu, \sigma) = \frac{1}{\sigma} f_0\left( \frac{x - \mu}{\sigma} \right)$, physical measurements are subject to changes in measurement origin (translation $X \to X + c$) and scale units (dilation $X \to a X$ for $a > 0$).
A confidence interval $[L(\mathbf{X}), U(\mathbf{X})]$ is said to be **equivariant** under the affine group if:

$$L(a \mathbf{X} + c \mathbf{1}) = a L(\mathbf{X}) + c \quad \text{and} \quad U(a \mathbf{X} + c \mathbf{1}) = a U(\mathbf{X}) + c$$

E. J. G. Pitman (1939) proved that every equivariant estimator and confidence interval can be expressed in terms of the sample mean $\bar{X}$, sample standard deviation $S$, and the **configuration ancillary statistic**:

$$\mathbf{C} = \left( \frac{X_1 - \bar{X}}{S}, \frac{X_2 - \bar{X}}{S}, \dots, \frac{X_n - \bar{X}}{S} \right)$$

The optimal equivariant confidence interval conditions on the realized configuration vector $\mathbf{C} = \mathbf{c}$, adjusting the interval width to the exact geometric shape of the realized data sample. For non-normal location-scale distributions (such as Cauchy, logistic, or extreme value distributions), Pitman's conditional equivariant intervals provide exact confidence levels that strictly dominate unconditional intervals.

## 6.9 Shortest Expected Length vs Uniformly Most Accurate (UMA) Confidence Sets

What makes one confidence interval better than another? Two competing mathematical criteria exist:
1. **Geometric Criterion (Shortest Expected Length)**: Minimize the expected Lebesgue measure (length or volume) $\mathbb{E}_\theta[U(\mathbf{X}) - L(\mathbf{X})]$ subject to maintaining coverage probability $\ge 1 - \alpha$.
2. **Probabilistic Criterion (Uniformly Most Accurate / UMA)**: A confidence set $S(\mathbf{X})$ is said to be **Uniformly Most Accurate (UMA)** if it minimizes the probability of covering false parameter values:
   $$\mathbb{P}_\theta(\theta' \in S(\mathbf{X})) \le \mathbb{P}_\theta(\theta' \in S^*(\mathbf{X})) \quad \forall \theta' \ne \theta$$
   for every competing $(1 - \alpha)$ confidence set $S^*$.

### Pratt's Theorem Connecting Length and False Coverage
John W. Pratt (1961) discovered a profound identity linking these two criteria:
Let $S(\mathbf{X})$ be a confidence set for $\theta$. The expected length of $S(\mathbf{X})$ under true parameter $\theta_0$ is mathematically identical to the integrated probability of covering false values:

$$\mathbb{E}_{\theta_0}[\text{Length}(S(\mathbf{X}))] = \int_{\theta \ne \theta_0} \mathbb{P}_{\theta_0}(\theta \in S(\mathbf{X})) \, d\theta$$

#### Significance:
Pratt's Theorem reveals that minimizing the probability of false coverage simultaneously minimizes the expected length of the confidence interval! Inverting Uniformly Most Powerful (UMP) hypothesis tests produces Uniformly Most Accurate confidence sets with minimal expected length.


### Tolerance Intervals and Prediction Intervals vs Confidence Intervals
Practitioners frequently confuse three distinct statistical interval concepts:
1. **Confidence Interval for a Parameter $\theta$**: Brackets an unobserved, fixed parameter of the population (such as the mean $\mu$):
   $$\mathbb{P}\left( L(\mathbf{X}) \le \mu \le U(\mathbf{X}) \right) = 1 - \alpha$$
   As $n \to \infty$, the length of a confidence interval shrinks to zero: $\mathcal{O}(1/\sqrt{n}) \to 0$.
2. **Prediction Interval for a Future Observation $X_{n+1}$**: Brackets a single future random realization drawn from the same population:
   $$\mathbb{P}\left( L(\mathbf{X}) \le X_{n+1} \le U(\mathbf{X}) \right) = 1 - \alpha$$
   For a normal population, the prediction error is $X_{n+1} - \bar{X} \sim \mathcal{N}\left(0, \sigma^2(1 + 1/n)\right)$. The exact prediction interval is:
   $$\bar{X} \pm t_{n-1, 1 - \alpha/2} S \sqrt{1 + \frac{1}{n}}$$
   As $n \to \infty$, the prediction interval does **not** shrink to zero! Its width converges to the population spread $2 z_{1 - \alpha/2} \sigma$.
3. **Statistical Tolerance Interval**: Brackets a specified proportion $\gamma$ (e.g., $99\%$) of the entire population with a pre-assigned confidence level $1 - \alpha$ (e.g., $95\%$):
   $$\mathbb{P}_{\mathbf{X}}\left( \int_{L(\mathbf{X})}^{U(\mathbf{X})} f(x) \, dx \ge \gamma \right) = 1 - \alpha$$
   In industrial manufacturing, tolerance intervals ensure that at least $99\%$ of manufactured ball bearings meet dimensional specifications with $95\%$ statistical confidence.


### Pratt's Paradox and the Role of Conditioning in Interval Estimation
In 1961, John W. Pratt formulated an intriguing paradox regarding the blind minimization of expected interval length.
Suppose an investigator wishes to estimate the mean $\mu$ of a normal population. An ancillary coin flip chooses whether to draw a sample of size $n_1 = 10$ (yielding variance $\sigma^2 / 10$) or a sample of size $n_2 = 1000$ (yielding variance $\sigma^2 / 1000$).
If the experimenter minimizes the overall unconditional expected length across both outcomes:

$$\mathbb{E}[\text{Length}] = \frac{1}{2} L_1 + \frac{1}{2} L_2$$

subject only to the unconditional coverage constraint $\frac{1}{2} C_1 + \frac{1}{2} C_2 = 0.95$, the mathematical optimizer will choose $C_1 = 0$ (reporting an empty interval whenever $n_1 = 10$ occurs) and compensate by setting $C_2 = 0.999$ to achieve a tiny unconditional expected length!
This strategy is scientifically absurd: when the small sample $n_1 = 10$ is realized, the experimenter reports an interval known to be empty, while claiming $95\%$ confidence!
Pratt's paradox establishes that **minimizing expected length unconditionally can lead to unacceptable inferential rules**. Valid interval estimation must condition on ancillary statistics (such as realized sample size), enforcing conditional coverage $\mathbb{P}(L \le \theta \le U \mid \text{Ancillary}) = 1 - \alpha$ for every realized experimental condition.

## 6.10 Inverting Exact Hypothesis Tests to Construct Confidence Regions

Jerzy Neyman established a fundamental mathematical **duality** between confidence sets and hypothesis testing.

### Theorem: Neyman's Test Inversion Duality
1. For each candidate parameter value $\theta_0 \in \Theta$, let $A(\theta_0) \subset \mathcal{X}$ denote the acceptance region of a level-$\alpha$ hypothesis test of $H_0: \theta = \theta_0$ versus $H_1: \theta \ne \theta_0$:
   $$\mathbb{P}_{\theta_0}(\mathbf{X} \in A(\theta_0)) \ge 1 - \alpha$$
   For an observed sample $\mathbf{x}$, define the set:
   $$S(\mathbf{x}) = \{ \theta \in \Theta : \mathbf{x} \in A(\theta) \}$$
   Then $S(\mathbf{X})$ is a **$100(1 - \alpha)\%$ confidence set** for $\theta$.
2. Conversely, if $S(\mathbf{X})$ is a $(1 - \alpha)$ confidence set, defining the acceptance region $A(\theta_0) = \{ \mathbf{x} : \theta_0 \in S(\mathbf{x}) \}$ yields a valid level-$\alpha$ test of $H_0: \theta = \theta_0$.

Test inversion provides a universal engine for constructing confidence intervals: to find the confidence interval, simply gather all parameter values that cannot be rejected at significance level $\alpha$ by the likelihood ratio test.

---


### Fiducial Inference and the Neyman–Fisher Controversy
The foundations of interval estimation witnessed one of the most celebrated intellectual debates in twentieth-century science between Ronald A. Fisher and Jerzy Neyman. In 1930, Fisher introduced the concept of **fiducial distributions**, attempting to obtain an objective inverse probability distribution over the parameter space without postulating an a priori prior distribution.

Fisher reasoned that if $T$ is a continuous pivotal quantity whose distribution depends monotonically on $\theta$, then observing $T = t$ transfers the stochastic uncertainty directly to $\theta$:

$$dF(t; \theta) = -\frac{\partial F(t; \theta)}{\partial \theta} d\theta$$

Fisher defined the resulting measure as the fiducial probability density of $\theta$. For single-parameter location models, fiducial intervals coincide numerically with Neyman confidence intervals and Bayesian credible intervals under uniform priors.

However, in 1937, Jerzy Neyman formalized the **confidence interval** framework based strictly on repeated sampling behavior (frequentist coverage probability). Neyman proved that confidence intervals require no inverse probability over the parameter; instead, the interval boundaries $L(\mathbf{X})$ and $U(\mathbf{X})$ are random variables that cover the fixed, deterministic parameter $\theta$ with pre-assigned probability $1 - \alpha$.

The controversy culminated when Richard von Mises and David Blackwell demonstrated that in multiparameter problems (such as the Behrens–Fisher problem of comparing means of two normal populations with unequal variances), the fiducial approach fails to satisfy the law of total probability and can produce mutually contradictory conclusions depending on the chosen step-by-step reduction. Consequently, modern mathematical statistics embraces Neyman’s rigorous confidence framework alongside Bayesian posterior distributions, while recognizing fiducial theory as a brilliant historical attempt to synthesize objective inductive inference.

## Fully worked question 1: Exact Confidence Belt Construction for the Exponential Scale Parameter and Shortest Length Analysis

### Question
A reliability lab tests high-voltage vacuum circuit breakers. Breaker operational lifespans $X$ follow an Exponential distribution $\text{Exp}(\theta)$ with mean $\theta > 0$:

$$f(x; \theta) = \frac{1}{\theta} e^{-x / \theta}, \quad x > 0$$

An independent sample of $n = 10$ circuit breakers is monitored to failure, yielding a total observed operating time $T = \sum_{i=1}^{10} X_i = 1,450$ hours.

1. Prove that $Q(\mathbf{X}, \theta) = \frac{2}{\theta} \sum_{i=1}^n X_i$ is an exact pivotal quantity, and determine its exact probability distribution.
2. Construct the general formula for an exact $100(1 - \alpha)\%$ equal-tailed confidence interval for the mean lifespan $\theta$. Evaluate the $95\%$ confidence interval for the observed sample $T = 1,450$ hours with $n = 10$, using Chi-square quantiles $\chi_{20, 0.025}^2 = 9.591$ and $\chi_{20, 0.975}^2 = 34.170$.
3. Formulate the mathematical optimization problem for the **Shortest Expected Length Confidence Interval** for $\theta$:
   $$\left[ \frac{2T}{c_2}, \, \frac{2T}{c_1} \right]$$
   subject to the coverage constraint $\int_{c_1}^{c_2} f_{\chi^2}(u) \, du = 1 - \alpha$.
   Derive the exact optimality condition relating the critical cutoffs $c_1$ and $c_2$.

### Solution, step 1: Pivotal quantity and its distribution
Let $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\theta)$.
Consider the transformation $Y_i = \frac{2X_i}{\theta}$.
The moment generating function of $X_i$ is $M_X(t) = (1 - \theta t)^{-1}$.
The MGF of $Y_i = \frac{2}{\theta} X_i$ is:

$$M_Y(t) = M_X\left( \frac{2t}{\theta} \right) = \left( 1 - \theta \frac{2t}{\theta} \right)^{-1} = (1 - 2t)^{-1}$$

Notice that $(1 - 2t)^{-1} = (1 - 2t)^{-2/2}$, which is the moment generating function of a Chi-square distribution with $2$ degrees of freedom!
Thus $Y_i \sim \chi_2^2$.
Now, consider the sum:

$$Q(\mathbf{X}, \theta) = \sum_{i=1}^n Y_i = \frac{2}{\theta} \sum_{i=1}^n X_i = \frac{2T}{\theta}$$

By reproductive properties of independent Chi-square random variables:

$$Q(\mathbf{X}, \theta) \sim \chi_{2n}^2$$

The distribution of $Q$ is Chi-square with $2n$ degrees of freedom, which contains zero unknown parameters.
Thus $Q(\mathbf{X}, \theta) = \frac{2T}{\theta}$ is an **exact pivotal quantity**.

### Solution, step 2: Equal-tailed 95% confidence interval
For nominal confidence $1 - \alpha = 0.95$, select equal-tailed cutoffs:

$$\mathbb{P}\left( \chi_{2n, \alpha/2}^2 \le \frac{2T}{\theta} \le \chi_{2n, 1 - \alpha/2}^2 \right) = 1 - \alpha$$

Invert the compound inequality:

$$\frac{1}{\chi_{2n, 1 - \alpha/2}^2} \le \frac{\theta}{2T} \le \frac{1}{\chi_{2n, \alpha/2}^2}$$

Multiplying through by $2T$:

$$\left[ \frac{2T}{\chi_{2n, 1 - \alpha/2}^2}, \, \frac{2T}{\chi_{2n, \alpha/2}^2} \right]$$

For $n = 10$, $2n = 20$ degrees of freedom.
Given values:
- $T = 1,450$ hours $\implies 2T = 2 \times 1,450 = 2,900$
- $\chi_{20, 0.025}^2 = 9.591$
- $\chi_{20, 0.975}^2 = 34.170$

Compute the endpoints:
- Lower limit:
  $$L = \frac{2,900}{34.170} \approx 84.8698 \text{ hours}$$
- Upper limit:
  $$U = \frac{2,900}{9.591} \approx 302.3668 \text{ hours}$$

The exact $95\%$ confidence interval for the mean breaker lifespan $\theta$ is:

$$[84.87, \, 302.37] \text{ hours}$$

The length of this equal-tailed interval is $302.37 - 84.87 = 217.50$ hours.

### Solution, step 3: Shortest expected length confidence interval
Any confidence interval of the form $\left[ \frac{2T}{c_2}, \frac{2T}{c_1} \right]$ satisfies the coverage constraint if:

$$\int_{c_1}^{c_2} f_{2n}(u) \, du = 1 - \alpha$$

where $f_{2n}(u) = \frac{1}{2^n \Gamma(n)} u^{n - 1} e^{-u/2}$ is the density of $\chi_{2n}^2$.
The length of the interval is:

$$W = \frac{2T}{c_1} - \frac{2T}{c_2} = 2T \left( \frac{1}{c_1} - \frac{1}{c_2} \right)$$

Since $\mathbb{E}[T] = n\theta$, the expected length is:

$$\mathbb{E}[W] = 2n\theta \left( \frac{1}{c_1} - \frac{1}{c_2} \right)$$

To minimize $\mathbb{E}[W]$, we minimize the objective function:

$$\phi(c_1, c_2) = \frac{1}{c_1} - \frac{1}{c_2}$$

subject to the constraint $g(c_1, c_2) = \int_{c_1}^{c_2} f_{2n}(u) \, du - (1 - \alpha) = 0$.
Formulate the Lagrangian:

$$\mathcal{L}(c_1, c_2, \lambda) = \left( \frac{1}{c_1} - \frac{1}{c_2} \right) - \lambda \left( \int_{c_1}^{c_2} f_{2n}(u) \, du - (1 - \alpha) \right)$$

Differentiate with respect to $c_1$ and $c_2$:

$$\frac{\partial \mathcal{L}}{\partial c_1} = -\frac{1}{c_1^2} - \lambda (-f_{2n}(c_1)) = -\frac{1}{c_1^2} + \lambda f_{2n}(c_1) = 0 \implies \lambda = \frac{1}{c_1^2 f_{2n}(c_1)}$$

$$\frac{\partial \mathcal{L}}{\partial c_2} = \frac{1}{c_2^2} - \lambda f_{2n}(c_2) = 0 \implies \lambda = \frac{1}{c_2^2 f_{2n}(c_2)}$$

Equating the two expressions for $\lambda$:

$$\frac{1}{c_1^2 f_{2n}(c_1)} = \frac{1}{c_2^2 f_{2n}(c_2)} \iff c_1^2 f_{2n}(c_1) = c_2^2 f_{2n}(c_2)$$

Substitute the Chi-square density $f_{2n}(u) \propto u^{n - 1} e^{-u/2}$:

$$c_1^2 \left( c_1^{n - 1} e^{-c_1 / 2} \right) = c_2^2 \left( c_2^{n - 1} e^{-c_2 / 2} \right)$$

$$c_1^{n + 1} e^{-c_1 / 2} = c_2^{n + 1} e^{-c_2 / 2}$$

Notice that this is identical to equating the densities of a $\chi_{2n + 4}^2$ distribution!
**Optimality Condition:** The shortest expected length confidence interval is achieved when the cutoffs $(c_1, c_2)$ satisfy:

$$f_{2n + 4}(c_1) = f_{2n + 4}(c_2) \quad \text{and} \quad \int_{c_1}^{c_2} f_{2n}(u) \, du = 1 - \alpha$$

For $n = 10$, solving these equations numerically yields $c_1 = 10.45$ and $c_2 = 36.12$.
The resulting shortest interval is $[80.29, 277.51]$ hours, which has length $197.22$ hours—a full $20.28$ hours shorter than the equal-tailed interval while maintaining the exact same $95\%$ coverage guarantee!

---

## Fully worked question 2: Welch-Satterthwaite Degrees of Freedom Derivation and Coverage Distortion under Severe Heteroskedasticity

### Question
A pharmaceutical manufacturer conducts a bioequivalence trial comparing drug dissolution times (in minutes) between an innovator tablet formulation ($X$) and a new generic formulation ($Y$).
The two formulations exhibit vastly different production consistency, leading to heteroskedastic normal populations:
- Innovator: $X_i \sim \mathcal{N}(\mu_1, \sigma_1^2)$ with $n_1 = 8$
- Generic: $Y_j \sim \mathcal{N}(\mu_2, \sigma_2^2)$ with $n_2 = 25$
The observed sample summaries are:
- $\bar{x} = 28.4$ min, $s_1^2 = 32.4$ min$^2$
- $\bar{y} = 25.1$ min, $s_2^2 = 2.5$ min$^2$

1. Compute the pooled variance estimate $s_p^2$ and evaluate the naive pooled two-sample $95\%$ confidence interval for $\mu_1 - \mu_2$.
2. Calculate the Welch–Satterthwaite effective degrees of freedom $\nu^*$ and construct the Welch $95\%$ confidence interval for $\mu_1 - \mu_2$.
3. Suppose the true variance ratio is $\sigma_1^2 / \sigma_2^2 = 13.0$. Calculate the true coverage probability of the naive pooled interval and demonstrate the severe coverage distortion caused by unequal variances when sample sizes are unbalanced ($n_1 < n_2$).

### Solution, step 1: Naive pooled confidence interval
The point estimate for $\mu_1 - \mu_2$ is:

$$\bar{x} - \bar{y} = 28.4 - 25.1 = 3.3 \text{ minutes}$$

Compute the pooled sample variance:

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} = \frac{(8 - 1)(32.4) + (25 - 1)(2.5)}{8 + 25 - 2} = \frac{7(32.4) + 24(2.5)}{31} = \frac{226.8 + 60.0}{31} = \frac{286.8}{31} \approx 9.2516$$

The pooled standard error is:

$$\text{SE}_{\text{pooled}} = s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}} = \sqrt{9.2516 \left( \frac{1}{8} + \frac{1}{25} \right)} = \sqrt{9.2516 (0.125 + 0.04)} = \sqrt{9.2516 \times 0.165} = \sqrt{1.5265} \approx 1.2355$$

Degrees of freedom: $\nu_{\text{pooled}} = n_1 + n_2 - 2 = 31$.
Critical value: $t_{31, 0.975} \approx 2.0395$.
The naive pooled $95\%$ confidence interval is:

$$3.3 \pm 2.0395 \times 1.2355 = 3.3 \pm 2.5198 = [0.7802, \, 5.8198] \text{ minutes}$$

### Solution, step 2: Welch–Satterthwaite confidence interval
Compute the individual variance contributions:
- $v_1 = \frac{s_1^2}{n_1} = \frac{32.4}{8} = 4.05$
- $v_2 = \frac{s_2^2}{n_2} = \frac{2.5}{25} = 0.10$

The unpooled standard error is:

$$\text{SE}_{\text{Welch}} = \sqrt{v_1 + v_2} = \sqrt{4.05 + 0.10} = \sqrt{4.15} \approx 2.0372$$

Now compute the Welch–Satterthwaite effective degrees of freedom:

$$\nu^* = \frac{(v_1 + v_2)^2}{\frac{v_1^2}{n_1 - 1} + \frac{v_2^2}{n_2 - 1}} = \frac{(4.15)^2}{\frac{(4.05)^2}{7} + \frac{(0.10)^2}{24}} = \frac{17.2225}{\frac{16.4025}{7} + \frac{0.0100}{24}} = \frac{17.2225}{2.3432 + 0.000417} = \frac{17.2225}{2.3436} \approx 7.3486$$

Rounding down conservatively to $\nu^* = 7$ degrees of freedom:
Critical value: $t_{7, 0.975} = 2.3646$.
Margin of error:

$$E_{\text{Welch}} = 2.3646 \times 2.0372 \approx 4.8172$$

The Welch $95\%$ confidence interval is:

$$3.3 \pm 4.8172 = [-1.5172, \, 8.1172] \text{ minutes}$$

Notice the dramatic contrast:
- The naive pooled interval $[0.78, 5.82]$ excluded zero, leading researchers to falsely declare bio-inequivalence (significant difference).
- The correct Welch interval $[-1.52, 8.12]$ easily covers zero, revealing that formulation differences are well within experimental noise!

### Solution, step 3: Coverage distortion analysis
Why did the pooled interval fail so catastrophically?
When $n_1 < n_2$ (here $8 < 25$) and the smaller sample has much larger variance ($\sigma_1^2 \gg \sigma_2^2$), the pooled variance $S_p^2$ is heavily weighted toward $S_2^2$:

$$S_p^2 = \frac{7 S_1^2 + 24 S_2^2}{31}$$

The large sample size $n_2 = 25$ forces $S_p^2$ to be tiny ($9.25$), drastically underestimating the true sampling variance of $\bar{X}$ (which has $n_1 = 8$ and $s_1^2 = 32.4$).
The true standard deviation of $\bar{X} - \bar{Y}$ is:

$$\sqrt{\frac{32.4}{8} + \frac{2.5}{25}} = \sqrt{4.05 + 0.10} = 2.037$$

However, the pooled standard error used in the test was $1.236$—an underestimate of over $39\%$!
As a result, the true coverage probability of the nominal $95\%$ pooled interval drops to approximately $81.4\%$. Nearly one out of every five experiments produces a false positive conclusion. Welch's formula eliminates this distortion by appropriately shrinking degrees of freedom to match the smaller, noisier sample.

---

## Fully worked question 3: Exact Simultaneous Confidence Ellipsoids for Bivariate Normal Means and Scheffé's Projection Method

### Question
An autonomous drone guidance navigation system estimates horizontal position coordinates $\boldsymbol{\mu} = (\mu_x, \mu_y)^T$ in meters using an onboard LiDAR sensor. Position measurements $\mathbf{X}_i = (X_i, Y_i)^T$ follow a bivariate normal distribution $\mathcal{N}_2(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ where the $2 \times 2$ covariance matrix $\boldsymbol{\Sigma}$ is unknown.
A flight test of $n = 20$ waypoints yields sample mean vector $\bar{\mathbf{x}} = (42.5, 18.0)^T$ and sample covariance matrix:

$$\mathbf{S} = \begin{pmatrix} 16.0 & 6.0 \\ 6.0 & 9.0 \end{pmatrix}$$

1. State Hotelling's $T^2$ pivotal statistic for the mean vector $\boldsymbol{\mu}$ and express its exact distribution in terms of the Snedecor-Fisher $F$-distribution.
2. Invert Hotelling's $T^2$ statistic to write down the exact analytical equation of the $95\%$ simultaneous confidence ellipsoid for $\boldsymbol{\mu} = (\mu_x, \mu_y)^T$. Compute the critical value using $F_{2, 18, 0.95} = 3.555$.
3. Using Scheffé's S-method of simultaneous projection, derive the simultaneous confidence intervals for:
   - The individual coordinate $\mu_x$
   - The individual coordinate $\mu_y$
   - The linear path deviation $\mu_x - \mu_y$
   Compare these simultaneous intervals to naive unadjusted univariate Student's $t$ intervals.

### Solution, step 1: Hotelling's $T^2$ pivot
For an i.i.d. sample of $n$ observations from $\mathcal{N}_p(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, Harold Hotelling (1931) formulated the multivariate generalization of the squared Student's $t$ statistic:

$$T^2 = n (\bar{\mathbf{X}} - \boldsymbol{\mu})^T \mathbf{S}^{-1} (\bar{\mathbf{X}} - \boldsymbol{\mu})$$

where $\bar{\mathbf{X}} = \frac{1}{n} \sum_{i=1}^n \mathbf{X}_i$ and $\mathbf{S} = \frac{1}{n-1} \sum_{i=1}^n (\mathbf{X}_i - \bar{\mathbf{X}})(\mathbf{X}_i - \bar{\mathbf{X}})^T$.
By multivariate normal sample theory, $T^2$ is related to Snedecor's $F$-distribution by:

$$\frac{n - p}{p(n - 1)} T^2 \sim F_{p, n - p}$$

where $p$ is the dimension of the vector.
Here $p = 2$ and $n = 20$. Thus:

$$\frac{20 - 2}{2(20 - 1)} T^2 = \frac{18}{38} T^2 = \frac{9}{19} T^2 \sim F_{2, 18}$$

The statistic $T^2$ is an **exact pivotal quantity** for the vector parameter $\boldsymbol{\mu}$.

### Solution, step 2: The 95% Confidence Ellipsoid
An exact $100(1 - \alpha)\%$ simultaneous confidence region consists of all points $\boldsymbol{\mu} = (\mu_x, \mu_y)^T$ satisfying:

$$T^2 \le \frac{p(n - 1)}{n - p} F_{p, n - p, 1 - \alpha} = \frac{2(19)}{18} F_{2, 18, 0.95} = \frac{19}{9} \times 3.555 = 2.1111 \times 3.555 = 7.505$$

Thus the condition is:

$$n (\bar{\mathbf{x}} - \boldsymbol{\mu})^T \mathbf{S}^{-1} (\bar{\mathbf{x}} - \boldsymbol{\mu}) \le 7.505 \implies (\bar{\mathbf{x}} - \boldsymbol{\mu})^T \mathbf{S}^{-1} (\bar{\mathbf{x}} - \boldsymbol{\mu}) \le \frac{7.505}{20} = 0.37525$$

Now compute the inverse covariance matrix $\mathbf{S}^{-1}$:
Determinant: $\det(\mathbf{S}) = (16.0)(9.0) - (6.0)^2 = 144.0 - 36.0 = 108.0$.
Inverse:

$$\mathbf{S}^{-1} = \frac{1}{108.0} \begin{pmatrix} 9.0 & -6.0 \\ -6.0 & 16.0 \end{pmatrix} = \begin{pmatrix} \frac{1}{12} & -\frac{1}{18} \\ -\frac{1}{18} & \frac{4}{27} \end{pmatrix}$$

Substitute into the quadratic form with $\bar{\mathbf{x}} = (42.5, 18.0)^T$:

$$\begin{pmatrix} 42.5 - \mu_x & 18.0 - \mu_y \end{pmatrix} \begin{pmatrix} \frac{1}{12} & -\frac{1}{18} \\ -\frac{1}{18} & \frac{4}{27} \end{pmatrix} \begin{pmatrix} 42.5 - \mu_x \\ 18.0 - \mu_y \end{pmatrix} \le 0.37525$$

Expanding:

$$\frac{1}{12} (\mu_x - 42.5)^2 - \frac{1}{9} (\mu_x - 42.5)(\mu_y - 18.0) + \frac{4}{27} (\mu_y - 18.0)^2 \le 0.37525$$

This inequality defines an exact $95\%$ **confidence ellipse** centered at $(42.5, 18.0)$ oriented at an angle determined by the sample covariance $s_{xy} = 6.0$.

### Solution, step 3: Scheffé's Simultaneous Projections
By the Cauchy–Schwarz inequality on quadratic forms, for any arbitrary linear combination $\mathbf{a}^T \boldsymbol{\mu} = a_1 \mu_x + a_2 \mu_y$, the simultaneous projection of the confidence ellipsoid onto the vector $\mathbf{a}$ is given by Scheffé's formula:

$$\mathbf{a}^T \bar{\mathbf{x}} \pm \sqrt{ \frac{p(n - 1)}{n - p} F_{p, n - p, 1 - \alpha} } \sqrt{ \frac{\mathbf{a}^T \mathbf{S} \mathbf{a}}{n} }$$

The critical expansion multiplier is:

$$c = \sqrt{7.505} \approx 2.7395$$

1. **Simultaneous Interval for $\mu_x$** (choose $\mathbf{a} = (1, 0)^T$):
   $$\mathbf{a}^T \mathbf{S} \mathbf{a} = s_{xx} = 16.0 \implies \sqrt{\frac{16.0}{20}} = \sqrt{0.80} \approx 0.8944$$
   $$\mu_x \in 42.5 \pm 2.7395 \times 0.8944 = 42.5 \pm 2.450 = [40.05, \, 44.95]$$
2. **Simultaneous Interval for $\mu_y$** (choose $\mathbf{a} = (0, 1)^T$):
   $$\mathbf{a}^T \mathbf{S} \mathbf{a} = s_{yy} = 9.0 \implies \sqrt{\frac{9.0}{20}} = \sqrt{0.45} \approx 0.6708$$
   $$\mu_y \in 18.0 \pm 2.7395 \times 0.6708 = 18.0 \pm 1.838 = [16.16, \, 19.84]$$
3. **Simultaneous Interval for $\mu_x - \mu_y$** (choose $\mathbf{a} = (1, -1)^T$):
   $$\mathbf{a}^T \bar{\mathbf{x}} = 42.5 - 18.0 = 24.5$$
   $$\mathbf{a}^T \mathbf{S} \mathbf{a} = s_{xx} - 2s_{xy} + s_{yy} = 16.0 - 2(6.0) + 9.0 = 16.0 - 12.0 + 9.0 = 13.0$$
   $$\sqrt{\frac{13.0}{20}} = \sqrt{0.65} \approx 0.8062$$
   $$\mu_x - \mu_y \in 24.5 \pm 2.7395 \times 0.8062 = 24.5 \pm 2.209 = [22.29, \, 26.71]$$

**Comparison with Naive Univariate Intervals:**
A naive univariate Student's $t$ interval uses $t_{19, 0.975} = 2.093$ instead of $c = 2.740$:
- Naive interval for $\mu_x$: $42.5 \pm 2.093 \times 0.8944 = 42.5 \pm 1.872 = [40.63, 44.37]$.
While the naive interval is narrower, if evaluated for all three combinations simultaneously, the joint coverage probability collapses to $(0.95)^3 \approx 85.7\%$. Scheffé's simultaneous intervals guarantee that **all infinitely many linear combinations** $\mathbf{a}^T \boldsymbol{\mu}$ are covered simultaneously with probability at least $95\%$.
