# Unit 7: Approximate and Asymptotic Confidence Intervals

In many physical, biological, and econometric investigations, exact pivotal quantities do not exist because distributions are discrete, non-Gaussian, or governed by complex non-linear parameters. In such settings, mathematical statistics deploys large-sample asymptotic approximations to construct intervals whose coverage probability converges to the nominal target $1 - \alpha$ as the sample size $n \to \infty$. In this unit, we rigorously investigate the three classical pillars of asymptotic interval estimation: the Wald interval, the Rao Score (Wilson) interval, and the Likelihood Ratio (Wilks) profile interval. We examine discrete coverage anomalies in binomial and Poisson models, analyze the Clopper–Pearson exact bound, explore variance-stabilizing transformations, develop nonparametric bootstrap confidence intervals including Percentile and Bias-Corrected Accelerated (BCa) methods, evaluate Edgeworth expansions for higher-order coverage accuracy, and construct robust intervals under model misspecification.

## 7.1 Large-Sample Interval Estimation via Asymptotic Normality and Slutsky's Theorem

Let $X_1, X_2, \dots, X_n$ be an independent, identically distributed sample from a distribution $P_\theta$ with unknown parameter $\theta \in \Theta \subseteq \mathbb{R}$.
Suppose $T_n = T_n(\mathbf{X})$ is a consistent point estimator of $\theta$ satisfying a Central Limit Theorem:

$$\sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, V(\theta))$$

where $V(\theta) > 0$ is the asymptotic variance function.
The quantity $\frac{\sqrt{n}(T_n - \theta)}{\sqrt{V(\theta)}}$ converges in distribution to $\mathcal{N}(0, 1)$, but it cannot be directly used as an empirical pivot if $V(\theta)$ depends on the unknown parameter $\theta$.

### Slutsky's Theorem and Asymptotic Pivots
To eliminate the unknown parameter from the denominator, we replace $V(\theta)$ with a consistent estimator $\hat{V}_n = V(T_n)$ or an empirical variance estimator such that $\hat{V}_n \xrightarrow{P} V(\theta)$.
By **Slutsky's Theorem**:
If $U_n = \sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, V(\theta))$ and $W_n = \sqrt{\hat{V}_n} \xrightarrow{P} \sqrt{V(\theta)}$, then the ratio:

$$Z_n = \frac{U_n}{W_n} = \frac{\sqrt{n}(T_n - \theta)}{\sqrt{\hat{V}_n}} = \frac{T_n - \theta}{\text{SE}(T_n)} \xrightarrow{d} \mathcal{N}(0, 1)$$

The studentized ratio $Z_n$ is an **asymptotically pivotal quantity**.
For any pre-assigned confidence level $1 - \alpha$, let $z_{1 - \alpha/2}$ denote the $(1 - \alpha/2)$-quantile of the standard normal distribution:

$$\lim_{n \to \infty} \mathbb{P}_\theta\left( -z_{1 - \alpha/2} \le \frac{T_n - \theta}{\text{SE}(T_n)} \le z_{1 - \alpha/2} \right) = 1 - \alpha$$

Inverting the inequality yields the canonical large-sample confidence interval:

$$\left[ T_n - z_{1 - \alpha/2} \, \text{SE}(T_n), \quad T_n + z_{1 - \alpha/2} \, \text{SE}(T_n) \right]$$

The coverage probability of this interval converges to $1 - \alpha$ as $n \to \infty$. However, in finite samples, the true coverage probability $C_n(\theta) = \mathbb{P}_\theta(L_n \le \theta \le U_n)$ deviates from $1 - \alpha$ by an approximation error of order $\mathcal{O}(1/\sqrt{n})$ or $\mathcal{O}(1/n)$.


### Edgeworth Expansions and Cornish–Fisher Asymptotic Inversions
The Central Limit Theorem guarantees that the standardized studentized statistic $T_n = \frac{\sqrt{n}(\hat{\theta} - \theta)}{\hat{\sigma}}$ converges in distribution to $\mathcal{N}(0, 1)$ at rate $\mathcal{O}(1/\sqrt{n})$:

$$F_n(x) = \mathbb{P}(T_n \le x) = \Phi(x) + \mathcal{O}\left( \frac{1}{\sqrt{n}} \right)$$

To achieve higher-order coverage accuracy, mathematical statisticians employ **Edgeworth Expansions**, which expand the true CDF $F_n(x)$ in terms of the Hermite polynomials $H_k(x)$ and population cumulants:

$$F_n(x) = \Phi(x) - \phi(x) \left[ \frac{\kappa_3}{6\sqrt{n}} H_2(x) + \frac{\kappa_4}{24n} H_3(x) + \frac{\kappa_3^2}{72n} H_5(x) + \mathcal{O}\left( \frac{1}{n^{3/2}} \right) \right]$$

where $\kappa_3 = \frac{\mathbb{E}[(X - \mu)^3]}{\sigma^3}$ is the skewness coefficient, and $H_2(x) = x^2 - 1$, $H_3(x) = x^3 - 3x$, $H_5(x) = x^5 - 10x^3 + 15x$.
Notice that the leading error term $-\phi(x) \frac{\kappa_3}{6\sqrt{n}} (x^2 - 1)$ is driven entirely by population **skewness**!
If the population is skewed ($\kappa_3 \ne 0$), the true distribution of $T_n$ is asymmetric, and a naive Gaussian interval $T_n \pm z_{1 - \alpha/2}$ experiences asymmetric tail coverage error of order $\mathcal{O}(1/\sqrt{n})$.
Inverting the Edgeworth expansion yields the **Cornish–Fisher Expansion** for the exact quantile $w_\alpha$:

$$w_\alpha = z_\alpha + \frac{\kappa_3}{6\sqrt{n}} (z_\alpha^2 - 1) + \frac{\kappa_4}{24n} (z_\alpha^3 - 3 z_\alpha) - \frac{\kappa_3^2}{36n} (2 z_\alpha^3 - 5 z_\alpha) + \mathcal{O}\left( \frac{1}{n^{3/2}} \right)$$

Using Cornish–Fisher quantiles replaces the standard $z_{\alpha}$ cutoffs with skewness-adjusted critical values, reducing interval coverage error from $\mathcal{O}(1/\sqrt{n})$ down to $\mathcal{O}(1/n)$ (second-order accuracy).

## 7.2 The Wald Confidence Interval: Formulation, Inversion, and Parameterization Sensitivity

The most ubiquitous asymptotic interval in applied statistics is the **Wald Confidence Interval**, which evaluates the standard error directly at the Maximum Likelihood Estimate $\hat{\theta}_n$.

### Definition of the Wald Interval
Let $\hat{\theta}_n$ be the Maximum Likelihood Estimator of $\theta$. By Theorem 5.3:

$$\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} \mathcal{N}\left(0, \frac{1}{I_1(\theta)}\right)$$

Estimating the standard error using the observed Fisher Information $J_n(\hat{\theta}) = -\ell_n''(\hat{\theta})$:

$$\text{SE}(\hat{\theta}_n) = \frac{1}{\sqrt{J_n(\hat{\theta}_n)}}$$

The **Wald $(1 - \alpha)$ Confidence Interval** is:

$$\left[ \hat{\theta}_n - z_{1 - \alpha/2} \frac{1}{\sqrt{J_n(\hat{\theta}_n)}}, \quad \hat{\theta}_n + z_{1 - \alpha/2} \frac{1}{\sqrt{J_n(\hat{\theta}_n)}} \right]$$

### The Pathology of Parameterization Sensitivity
While computationally effortless, the Wald confidence interval suffers from a notorious mathematical flaw: **it is fundamentally not invariant under non-linear reparameterizations**!
Suppose an investigator reparameterizes the model using a smooth, strictly monotonic transformation $\psi = g(\theta)$.
By the invariance property of MLEs, the MLE of $\psi$ is $\hat{\psi} = g(\hat{\theta})$.
By the Delta Method, the standard error of $\hat{\psi}$ is:

$$\text{SE}(\hat{\psi}) = |g'(\hat{\theta})| \, \text{SE}(\hat{\theta})$$

The Wald interval for $\psi$ is:

$$I_\psi = \left[ g(\hat{\theta}) - z_{1 - \alpha/2} |g'(\hat{\theta})| \text{SE}(\hat{\theta}), \quad g(\hat{\theta}) + z_{1 - \alpha/2} |g'(\hat{\theta})| \text{SE}(\hat{\theta}) \right]$$

Now, invert this interval back into the original parameter space $\theta = g^{-1}(\psi)$:

$$I_\theta^* = g^{-1}(I_\psi) = \left[ g^{-1}\left( g(\hat{\theta}) - z_{1 - \alpha/2} |g'(\hat{\theta})| \text{SE}(\hat{\theta}) \right), \quad g^{-1}\left( g(\hat{\theta}) + z_{1 - \alpha/2} |g'(\hat{\theta})| \text{SE}(\hat{\theta}) \right) \right]$$

In general, $I_\theta^* \ne I_\theta$!
Different scientific teams analyzing the exact same dataset can obtain radically different confidence intervals simply by choosing whether to parameterize their likelihood in terms of variance $\sigma^2$, standard deviation $\sigma$, precision $\tau = 1/\sigma^2$, or log-variance $\ln(\sigma^2)$. Furthermore, if the log-likelihood surface is asymmetric or non-quadratic, the Wald interval can extend beyond natural parameter boundaries, producing absurd negative variance estimates or probabilities exceeding $1$.

## 7.3 The Rao Score (Wilson) Confidence Interval: Quadratic Inversion and Superior Coverage

To overcome the parameterization fragility of the Wald interval, C. R. Rao and Edwin B. Wilson proposed inverting the **Score Statistic** instead of the point estimator.

### The Score Statistic Inversion
Recall the Score function $S_n(\theta) = \frac{\partial \ell_n(\theta)}{\partial \theta}$ and expected Fisher Information $I_n(\theta)$.
By Bartlett's first identity and the Central Limit Theorem:

$$\frac{S_n(\theta)}{\sqrt{I_n(\theta)}} \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{as } n \to \infty$$

The **Score Confidence Region** gathers all candidate parameter values $\theta$ whose score statistic is within the normal critical threshold:

$$\left\{ \theta \in \Theta : \left| \frac{S_n(\theta)}{\sqrt{I_n(\theta)}} \right| \le z_{1 - \alpha/2} \right\} = \left\{ \theta \in \Theta : \frac{[S_n(\theta)]^2}{I_n(\theta)} \le z_{1 - \alpha/2}^2 \right\}$$

### Key Mathematical Advantage over Wald
Notice the profound structural difference between the Score and Wald methods:
- In the Wald method, the denominator $\text{SE}(\hat{\theta})$ is evaluated at the single point estimate $\hat{\theta}$ and held frozen as $\theta$ varies.
- In the Score method, the denominator $\sqrt{I_n(\theta)}$ is evaluated dynamically at the hypothesized parameter $\theta$!

Evaluating information at $\theta$ automatically adjusts the standard error to the local curvature of the likelihood across the entire parameter space. For asymmetric distributions, inverting the quadratic score equation naturally produces asymmetric intervals that cannot violate physical boundary constraints.

## 7.4 The Likelihood Ratio Confidence Interval (Wilks' Inversion)

The third member of the likelihood trinity is the **Likelihood Ratio (LR) Confidence Interval**, obtained by inverting the Likelihood Ratio Test statistic.

### Theorem: Inversion of Wilks' Likelihood Ratio Test
Let $\ell_n(\theta)$ be the log-likelihood function and let $\hat{\theta}_n$ be the unconstrained MLE. By Wilks' Theorem (1938), under true parameter $\theta_0$:

$$2 \left[ \ell_n(\hat{\theta}_n) - \ell_n(\theta_0) \right] \xrightarrow{d} \chi_1^2 \quad \text{as } n \to \infty$$

The **$100(1 - \alpha)\%$ Likelihood Ratio Confidence Region** is defined as the set of all parameter values $\theta$ whose drop in log-likelihood does not exceed the critical Chi-square threshold:

$$\mathcal{C}_{\text{LR}} = \left\{ \theta \in \Theta : 2 [\ell_n(\hat{\theta}_n) - \ell_n(\theta)] \le \chi_{1, 1-\alpha}^2 = z_{1 - \alpha/2}^2 \right\}$$

Equivalently, in terms of the raw likelihood function:

$$\mathcal{C}_{\text{LR}} = \left\{ \theta \in \Theta : \frac{L_n(\theta)}{L_n(\hat{\theta}_n)} \ge \exp\left( -\frac{z_{1 - \alpha/2}^2}{2} \right) \right\}$$

For a $95\%$ confidence interval, $z_{0.975} = 1.96$, so $z^2 = 3.8415$ and $\frac{z^2}{2} = 1.9207$. The $95\%$ LR interval consists of all parameter values where the log-likelihood is within $1.92$ units of its maximum peak:

$$\mathcal{C}_{0.95} = \{ \theta : \ell_n(\theta) \ge \ell_n(\hat{\theta}) - 1.9207 \}$$

### Invariance of Likelihood Ratio Intervals
Unlike the Wald interval, the Likelihood Ratio confidence interval is **strictly invariant under one-to-one transformations**!
If $\psi = g(\theta)$ is any monotonic reparameterization, the likelihood value satisfies $L^*(g(\theta)) = L(\theta)$ and $L^*(g(\hat{\theta})) = L(\hat{\theta})$. Therefore:

$$\frac{L^*(g(\theta))}{L^*(g(\hat{\theta}))} = \frac{L(\theta)}{L(\hat{\theta})}$$

The Likelihood Ratio interval for $\psi$ is precisely the direct mapping of the interval for $\theta$:

$$\mathcal{C}_\psi = g(\mathcal{C}_\theta)$$

This functional invariance makes the Likelihood Ratio interval the gold standard in non-linear modeling, dose-response analysis, and survival analysis.


### Asymptotic Confidence Regions in Multiparameter Models: Profile Deviance Contours
In multidimensional models $\boldsymbol{\theta} = (\theta_1, \dots, \theta_p)^T$, establishing simultaneous confidence sets for a subset of parameters $\boldsymbol{\psi} = (\theta_1, \dots, \theta_r)^T$ in the presence of nuisance parameters $\boldsymbol{\lambda} = (\theta_{r+1}, \dots, \theta_p)^T$ relies on the **Profile Deviance Statistic**:

$$D_p(\boldsymbol{\psi}) = 2 \left[ \ell_n(\hat{\boldsymbol{\psi}}, \hat{\boldsymbol{\lambda}}) - \ell_p(\boldsymbol{\psi}) \right] = 2 \left[ \ell_n(\hat{\boldsymbol{\theta}}) - \sup_{\boldsymbol{\lambda}} \ell_n(\boldsymbol{\psi}, \boldsymbol{\lambda}) \right]$$

By Wilks' Theorem for partitioned parameters:

$$D_p(\boldsymbol{\psi}) \xrightarrow{d} \chi_r^2 \quad \text{under } \boldsymbol{\psi} = \boldsymbol{\psi}_0$$

The $100(1 - \alpha)\%$ simultaneous confidence region for $\boldsymbol{\psi}$ is the contour set:

$$\mathcal{C}_{1-\alpha} = \left\{ \boldsymbol{\psi} \in \mathbb{R}^r : \ell_p(\boldsymbol{\psi}) \ge \ell_n(\hat{\boldsymbol{\theta}}) - \frac{1}{2} \chi_{r, 1-\alpha}^2 \right\}$$

#### Geometric Characteristics:
1. **Curved and Asymmetric Topography**: Unlike the elliptical contours produced by the multivariate Wald method $(\hat{\boldsymbol{\psi}} - \boldsymbol{\psi})^T [\widehat{\text{Var}}(\hat{\boldsymbol{\psi}})]^{-1} (\hat{\boldsymbol{\psi}} - \boldsymbol{\psi}) \le \chi_r^2$, profile deviance contours follow the exact non-linear ridges and valleys of the likelihood surface.
2. **Banana-Shaped Contours**: In non-linear models (such as Michaelis–Menten enzyme kinetics or compartment models in pharmacokinetics), the parameters exhibit strong non-linear collinearity. The profile deviance contours naturally bend into banana-shaped or crescent manifolds, capturing parameter trade-offs that quadratic Wald approximations misrepresent.
3. **Invariance**: The profile deviance region is invariant under any invertible transformation $\boldsymbol{\phi} = \mathbf{g}(\boldsymbol{\psi})$.

## 7.5 Exact vs Approximate Intervals for Binomial Proportions

The estimation of an unknown success probability $p \in (0, 1)$ based on $X \sim \text{Binomial}(n, p)$ is one of the most widely used procedures in science. However, the classical textbook interval exhibits catastrophic coverage failures.

### 1. The Classical Wald Interval (The "Standard" Method)
The MLE is the sample proportion $\hat{p} = X / n$. Its estimated standard error is $\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$.
The classical Wald interval is:

$$\hat{p} \pm z_{1 - \alpha/2} \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$$

**Catastrophic Flaws of the Wald Interval (Brown, Cai, and DasGupta, 2001)**:
- **Zero-Width Failure**: If $X = 0$ or $X = n$, then $\hat{p}(1 - \hat{p}) = 0$, producing a degenerate confidence interval of length zero $[0, 0]$ or $[1, 1]$, which asserts absolute certainty!
- **Oscillation and Systematic Under-Coverage**: Because the binomial distribution is discrete, the true coverage probability $C_n(p) = \sum_{x=0}^n \binom{n}{x} p^x (1 - p)^{n-x} \mathbf{1}_{\{L(x) \le p \le U(x)\}}$ oscillates wildly and drops far below the nominal $95\%$ target—frequently falling to $80\%$ or lower, even for sample sizes as large as $n = 100$!

### 2. The Wilson Score Interval (1927)
Inverting the Score statistic $\frac{(\hat{p} - p)^2}{p(1 - p) / n} \le z^2$:

$$(X - n p)^2 \le z^2 n p (1 - p)$$

This is a **quadratic inequality in $p$**:

$$(n + z^2) p^2 - (2X + z^2) p + \frac{X^2}{n} \le 0$$

Solving for the roots via the quadratic formula yields the celebrated **Wilson Score Interval**:

$$\tilde{p} \pm \frac{z}{n + z^2} \sqrt{ n \hat{p}(1 - \hat{p}) + \frac{z^2}{4} }$$

where the center of the interval is the shrinkage proportion:

$$\tilde{p} = \frac{X + \frac{z^2}{2}}{n + z^2}$$

For $95\%$ confidence ($z \approx 2$), the center $\tilde{p} \approx \frac{X + 2}{n + 4}$!
This is the famous **Agresti–Coull "Add-Two-Successes-and-Two-Failures" rule**: by adding two successes and two failures to the sample, the simple Wald formula produces an interval whose coverage matches the exact Wilson score interval.

### 3. The Clopper–Pearson Exact Interval (1934)
To guarantee that coverage never falls below $1 - \alpha$ for any $p$, C. J. Clopper and E. S. Pearson inverted the exact binomial cumulative distribution function:

$$\sum_{k=x}^n \binom{n}{k} p_L^k (1 - p_L)^{n-k} = \frac{\alpha}{2}, \quad \sum_{k=0}^x \binom{n}{k} p_U^k (1 - p_U)^{n-k} = \frac{\alpha}{2}$$

Using the identity between the incomplete Beta integral and the binomial sum, the exact endpoints can be computed via Beta quantiles:

$$p_L = \text{Beta}\left(\frac{\alpha}{2}; \, x, \, n - x + 1\right), \quad p_U = \text{Beta}\left(1 - \frac{\alpha}{2}; \, x + 1, \, n - x\right)$$

The Clopper–Pearson interval is strictly conservative ($C_n(p) \ge 1 - \alpha$ for all $p$), making it the standard choice in regulatory safety applications where under-coverage is unacceptable.


### Asymptotic Confidence Intervals for Odds Ratios and Relative Risk in 2x2 Tables
In clinical epidemiology and medical genetics, the association between an exposure (or treatment) and a binary health outcome is summarized in a $2 \times 2$ contingency table:

$$\begin{array}{c|cc|c} & \text{Outcome (+)} & \text{Outcome (-)} & \text{Total} \\ \hline \text{Exposed} & a & b & n_1 \\ \text{Unexposed} & c & d & n_0 \\ \hline \text{Total} & m_1 & m_0 & N \end{array}$$

Two primary metrics quantify the association:
1. **Relative Risk (Risk Ratio, RR)**:
   $$\widehat{\text{RR}} = \frac{a / n_1}{c / n_0}$$
2. **Odds Ratio (OR)**:
   $$\widehat{\text{OR}} = \frac{a / b}{c / d} = \frac{a d}{b c}$$

Both $\widehat{\text{RR}}$ and $\widehat{\text{OR}}$ are strictly non-negative ratios whose sampling distributions are severely skewed to the right for small to moderate sample sizes. Direct Wald intervals on the raw ratios produce catastrophic under-coverage and can violate the non-negativity bound.
To achieve rapid Gaussian convergence, statisticians apply the **logarithmic transformation**:

$$\psi = \ln(\widehat{\text{OR}}) = \ln(a) - \ln(b) - \ln(c) + \ln(d)$$

By the Multivariate Delta Method, using the multinomial variance-covariance structure, the asymptotic standard error of the log-odds ratio is given by **Woolf's Formula** (1955):

$$\text{SE}(\ln \widehat{\text{OR}}) = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}$$

The asymptotic $100(1 - \alpha)\%$ confidence interval for $\ln(\text{OR})$ is:

$$\ln(\widehat{\text{OR}}) \pm z_{1 - \alpha/2} \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}$$

Exponentiating both endpoints yields the exact multiplicative confidence interval for the Odds Ratio:

$$\left[ \widehat{\text{OR}} \cdot \exp\left( -z_{1 - \alpha/2} \, \text{SE}(\ln \widehat{\text{OR}}) \right), \quad \widehat{\text{OR}} \cdot \exp\left( +z_{1 - \alpha/2} \, \text{SE}(\ln \widehat{\text{OR}}) \right) \right]$$

Similarly, for the Relative Risk, the standard error of $\ln(\widehat{\text{RR}})$ is:

$$\text{SE}(\ln \widehat{\text{RR}}) = \sqrt{\frac{1}{a} - \frac{1}{n_1} + \frac{1}{c} - \frac{1}{n_0}}$$

Exponentiating yields an asymmetric, range-preserving confidence interval for the Relative Risk that naturally respects the $(0, \infty)$ domain.

## 7.6 Asymptotic Confidence Intervals for Poisson Arrival Rates

For an i.i.d. sample $X_1, \dots, X_n \sim \text{Poisson}(\lambda)$, the sample mean is $\bar{X}$ and the sum is $T = \sum X_i \sim \text{Poisson}(n\lambda)$.
1. **Wald Interval**:
   $$\bar{X} \pm z_{1 - \alpha/2} \sqrt{\frac{\bar{X}}{n}}$$
   Fails when $\bar{X} = 0$, producing $[0, 0]$.
2. **Score Interval**:
   Inverting $\frac{(\bar{X} - \lambda)^2}{\lambda / n} \le z^2 \iff n \lambda^2 - (2n\bar{X} + z^2)\lambda + n\bar{X}^2 \le 0$:
   $$\lambda \in \bar{X} + \frac{z^2}{2n} \pm \frac{z}{\sqrt{n}} \sqrt{\bar{X} + \frac{z^2}{4n}}$$
   When $\bar{X} = 0$, the score interval smoothly evaluates to $\left[ 0, \, \frac{z^2}{n} \right]$, providing a non-trivial, valid upper bound.
3. **Exact Garwood Interval**:
   Using the relationship between the Poisson sum and the Chi-square distribution:
   $$\left[ \frac{1}{2n} \chi_{2T, \alpha/2}^2, \quad \frac{1}{2n} \chi_{2(T+1), 1 - \alpha/2}^2 \right]$$
   This guarantees exact coverage $\ge 1 - \alpha$ for all sample sizes.

## 7.7 Variance-Stabilized Asymptotic Confidence Intervals

When the asymptotic variance depends on the unknown parameter $\theta$, standard normal approximations can be accelerated by transforming $\hat{\theta}$ via a variance-stabilizing transformation $g(\theta) = \int \sqrt{I_1(\theta)} \, d\theta$.

### General Procedure:
1. Identify the transformation $g$ such that $\text{Var}(g(\hat{\theta})) \approx \frac{c^2}{n}$, a constant independent of $\theta$.
2. Construct the symmetric Gaussian interval for the transformed parameter $\psi = g(\theta)$:
   $$[L_\psi, U_\psi] = \left[ g(\hat{\theta}) - z_{1 - \alpha/2} \frac{c}{\sqrt{n}}, \quad g(\hat{\theta}) + z_{1 - \alpha/2} \frac{c}{\sqrt{n}} \right]$$
3. Invert the endpoints back using $g^{-1}$:
   $$[L_\theta, U_\theta] = [g^{-1}(L_\psi), \, g^{-1}(U_\psi)]$$

### Classical Examples:
- **Binomial Proportion ($g(p) = \arcsin(\sqrt{p})$)**:
  $$\arcsin(\sqrt{p}) \in \arcsin(\sqrt{\hat{p}}) \pm \frac{z_{1 - \alpha/2}}{2\sqrt{n}}$$
  Inverting yields endpoints bounded strictly inside $[0, 1]$.
- **Poisson Rate ($g(\lambda) = \sqrt{\lambda}$)**:
  $$\sqrt{\lambda} \in \sqrt{\bar{X}} \pm \frac{z_{1 - \alpha/2}}{2\sqrt{n}} \implies \lambda \in \left( \max\left\{0, \sqrt{\bar{X}} - \frac{z}{2\sqrt{n}}\right\} \right)^2, \left( \sqrt{\bar{X}} + \frac{z}{2\sqrt{n}} \right)^2$$
- **Correlation Coefficient ($g(\rho) = \frac{1}{2}\ln\frac{1+\rho}{1-\rho} = \text{arctanh}(\rho)$)**:
  $$\text{arctanh}(\rho) \in \text{arctanh}(r) \pm \frac{z_{1 - \alpha/2}}{\sqrt{n - 3}}$$
  Inverting via $\tanh$ guarantees endpoints strictly inside $[-1, 1]$.


### Woodruff's Method for Nonparametric Quantile Confidence Intervals
In econometric surveys of household income and wealth, distributions are heavily skewed and Pareto-tailed, making mean estimation unstable. Policy analysts rely instead on population quantiles $\xi_p = F^{-1}(p)$ (such as the median $\xi_{0.5}$ or 90th percentile $\xi_{0.9}$).
Ralph S. Woodruff (1952) established an ingenious, distribution-free method for constructing confidence intervals for any quantile $\xi_p$ without requiring density estimation.
Let $\hat{F}_n(t) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{\{X_i \le t\}}$ be the empirical cumulative distribution function.
At the true quantile $\xi_p$, the indicator $\mathbf{1}_{\{X_i \le \xi_p\}}$ is a Bernoulli variable with success probability $p$. By the Central Limit Theorem:

$$\hat{F}_n(\xi_p) \sim \mathcal{A}\mathcal{N}\left( p, \, \frac{p(1 - p)}{n} \right)$$

A $100(1 - \alpha)\%$ confidence interval for the probability value $p$ is:

$$[p_L, \, p_U] = \left[ p - z_{1 - \alpha/2} \sqrt{\frac{p(1 - p)}{n}}, \quad p + z_{1 - \alpha/2} \sqrt{\frac{p(1 - p)}{n}} \right]$$

Woodruff inverted this vertical probability interval horizontally through the sample quantile function $\hat{F}_n^{-1}$:

$$\left[ \hat{\xi}_{p_L}, \, \hat{\xi}_{p_U} \right] = \left[ \hat{F}_n^{-1}\left( p - z_{1 - \alpha/2} \sqrt{\frac{p(1 - p)}{n}} \right), \quad \hat{F}_n^{-1}\left( p + z_{1 - \alpha/2} \sqrt{\frac{p(1 - p)}{n}} \right) \right]$$

For an ordered sample $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$, the endpoints are simply the order statistics:

$$L = X_{(k_1)}, \quad U = X_{(k_2)}$$

where the integer ranks are:

$$k_1 = \left\lfloor n p - z_{1 - \alpha/2} \sqrt{n p (1 - p)} \right\rfloor, \quad k_2 = \left\lceil n p + z_{1 - \alpha/2} \sqrt{n p (1 - p)} \right\rceil$$

Woodruff's interval requires zero kernel density estimation, avoids bandwidth selection dilemmas, and guarantees exact non-parametric coverage across all continuous distribution shapes.

## 7.8 Nonparametric Bootstrap Confidence Intervals

When analytical distributions cannot be derived, resampling methods provide distribution-free confidence intervals.

### 1. The Standard Normal Bootstrap Interval
$$\hat{\theta} \pm z_{1 - \alpha/2} \widehat{\text{SE}}_{\text{boot}}$$
Assumes the bootstrap distribution is symmetric and approximately normal.

### 2. The Percentile Bootstrap Interval (Efron, 1981)
Sort the $B$ bootstrap estimates in ascending order: $\hat{\theta}^{*(1)} \le \hat{\theta}^{*(2)} \le \dots \le \hat{\theta}^{*(B)}$.
The $100(1 - \alpha)\%$ percentile interval is defined by the empirical quantiles:

$$\left[ \hat{\theta}^{*(\alpha/2)}, \quad \hat{\theta}^{*(1 - \alpha/2)} \right]$$

The percentile interval is range-preserving and transformation-invariant, but exhibits coverage error of order $\mathcal{O}(1/\sqrt{n})$ if the sampling distribution is skewed.

### 3. The Bias-Corrected and Accelerated (BCa) Interval
To achieve second-order accuracy (coverage error $\mathcal{O}(1/n)$), Bradley Efron (1987) introduced the **BCa interval**, which adjusts the quantile endpoints for both **median bias** ($z_0$) and **skewness/acceleration** ($a$):

$$\alpha_1 = \Phi\left( z_0 + \frac{z_0 + z_{\alpha/2}}{1 - a(z_0 + z_{\alpha/2})} \right), \quad \alpha_2 = \Phi\left( z_0 + \frac{z_0 + z_{1 - \alpha/2}}{1 - a(z_0 + z_{1 - \alpha/2})} \right)$$

where:
- The bias-correction parameter $z_0 = \Phi^{-1}\left( \frac{1}{B} \sum_{b=1}^B \mathbf{1}_{\{\hat{\theta}^{*b} < \hat{\theta}\}} \right)$ measures discrepancy between the bootstrap median and the point estimate.
- The acceleration parameter $a = \frac{\sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^3}{6 [\sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^2]^{3/2}}$ is computed from jackknife influence values.

The BCa interval automatically corrects for skewness and parameter-dependent variance, achieving second-order asymptotic correctness without requiring analytical Edgeworth corrections.

## 7.9 Coverage Error Asymptotics, Edgeworth Expansions, and Bartlett Corrections

When evaluating the quality of an asymptotic confidence interval, mathematicians distinguish between **first-order accurate** and **second-order accurate** procedures:
- A confidence interval $[L_n, U_n]$ is said to be **first-order accurate** if its one-sided coverage errors decay at rate $\mathcal{O}(1/\sqrt{n})$:
  $$\mathbb{P}_\theta(\theta \le U_n) = (1 - \alpha/2) + \frac{c_1(\theta)}{\sqrt{n}} + \mathcal{O}\left( \frac{1}{n} \right)$$
  The standard Wald interval $\hat{\theta} \pm z_{1-\alpha/2} \text{SE}(\hat{\theta})$ and standard normal bootstrap intervals are only first-order accurate.
- An interval is **second-order accurate** if the $\mathcal{O}(1/\sqrt{n})$ term vanishes identically across all $\theta \in \Theta$:
  $$\mathbb{P}_\theta(\theta \le U_n) = (1 - \alpha/2) + \frac{c_2(\theta)}{n} + \mathcal{O}\left( \frac{1}{n^{3/2}} \right)$$
  Second-order accuracy means that the interval achieves tenfold higher coverage precision in practical sample sizes. The Wilson Score interval, the Likelihood Ratio interval, and the BCa bootstrap interval are all second-order accurate.

### Bartlett Correction for Likelihood Ratio Intervals
In 1937, M. S. Bartlett discovered that the expectation of the likelihood ratio statistic $w = 2[\ell_n(\hat{\theta}) - \ell_n(\theta_0)]$ satisfies:

$$\mathbb{E}[w] = 1 + \frac{b}{n} + \mathcal{O}\left( \frac{1}{n^2} \right)$$

where $b$ is a constant depending on the third and fourth log-likelihood cumulants.
Bartlett showed that scaling the likelihood ratio statistic by its expected bias factor:

$$w^* = \frac{w}{1 + b / n}$$

accelerates the Chi-square convergence rate from $\mathcal{O}(1/n)$ down to $\mathcal{O}(1/n^2)$!
Inverting the Bartlett-corrected likelihood ratio statistic:

$$\left\{ \theta : \frac{2[\ell_n(\hat{\theta}) - \ell_n(\theta)]}{1 + b / n} \le z_{1 - \alpha/2}^2 \right\}$$

yields confidence intervals whose coverage errors decay at the rapid rate $\mathcal{O}(1/n^2)$, providing near-exact coverage even in tiny samples ($n = 10$).

## 7.10 Probability-Matching Priors: The Welch–Peers Synthesis and Frequentist Calibration

Can a Bayesian credible interval achieve exact frequentist coverage?
In 1963, B. L. Welch and H. W. Peers investigated what prior distributions $\pi(\theta)$ generate Bayesian posterior credible intervals whose frequentist coverage probability matches the nominal level $1 - \alpha$ to higher orders of asymptotic approximation:

$$\mathbb{P}_\theta\left( \theta \le U_{\text{Bayes}}(\mathbf{X}) \right) = 1 - \alpha + \mathcal{O}\left( \frac{1}{n} \right)$$

Welch and Peers proved that in a single-parameter regular model, the unique prior that eliminates the $\mathcal{O}(1/\sqrt{n})$ frequentist coverage bias is **Jeffreys' invariant prior**:

$$\pi_{\text{matching}}(\theta) = \pi_J(\theta) \propto \sqrt{I_1(\theta)}$$

Under Jeffreys' prior, the Bayesian $(1 - \alpha)$ one-sided credible limit is second-order accurate: its frequentist coverage error decays at rate $\mathcal{O}(1/n)$ rather than the usual $\mathcal{O}(1/\sqrt{n})$!
This celebrated result, known as the **Welch–Peers Theorem**, establishes a deep and satisfying mathematical bridge between the two competing philosophies: objective Bayesian credible intervals constructed using Jeffreys' prior are simultaneously the most accurate frequentist confidence intervals conceivable.

## 7.11 Nonparametric Empirical Likelihood Confidence Regions (Art Owen)

In 1988, Art B. Owen invented **Empirical Likelihood (EL)**, a revolutionary inference method that combines the non-parametric distribution-free flexibility of the bootstrap with the likelihood-ratio elegance and Bartlett correctability of parametric models.

### Definition of Empirical Likelihood
Let $X_1, X_2, \dots, X_n$ be an i.i.d. continuous sample. Without specifying any parametric density family, we place probability weights $p_i = \mathbb{P}(X = X_i)$ on each observed data point, subject to $p_i \ge 0$ and $\sum_{i=1}^n p_i = 1$.
The non-parametric likelihood function is:

$$L(F) = \prod_{i=1}^n p_i$$

Unconstrained, $L(F)$ is maximized by the empirical distribution $p_i = 1/n$, yielding maximum value $(1/n)^n$.
Now, consider estimating a general parameter $\boldsymbol{\theta}$ defined through an estimating equation $\mathbb{E}[m(X; \boldsymbol{\theta})] = \mathbf{0}$ (such as the mean $m(X; \mu) = X - \mu$).
The **Empirical Profile Likelihood Ratio** is:

$$\mathcal{R}(\boldsymbol{\theta}) = \sup\left\{ \prod_{i=1}^n n p_i : p_i \ge 0, \, \sum_{i=1}^n p_i = 1, \, \sum_{i=1}^n p_i m(X_i; \boldsymbol{\theta}) = \mathbf{0} \right\}$$

Using Lagrange multipliers, the optimal weights are $p_i = \frac{1}{n} \frac{1}{1 + \boldsymbol{\lambda}^T m(X_i; \boldsymbol{\theta})}$, where $\boldsymbol{\lambda}$ is the Lagrange multiplier vector satisfying $\sum_{i=1}^n \frac{m(X_i; \boldsymbol{\theta})}{1 + \boldsymbol{\lambda}^T m(X_i; \boldsymbol{\theta})} = \mathbf{0}$.

### Theorem: Nonparametric Wilks' Theorem (Owen, 1988)
Under the true parameter value $\boldsymbol{\theta}_0$:

$$-2 \ln \mathcal{R}(\boldsymbol{\theta}_0) \xrightarrow{d} \chi_p^2 \quad \text{as } n \to \infty$$

The **$100(1 - \alpha)\%$ Empirical Likelihood Confidence Region** is:

$$\mathcal{C}_{\text{EL}} = \left\{ \boldsymbol{\theta} : -2 \ln \mathcal{R}(\boldsymbol{\theta}) \le \chi_{p, 1-\alpha}^2 \right\}$$

#### Superb Properties of Empirical Likelihood:
1. **Completely Non-Parametric**: Requires zero parametric assumptions about the underlying distribution family (no normality required).
2. **Data-Determined Shape**: EL confidence regions naturally adapt to the skewness and curvature of the data. Unlike symmetric Wald intervals, EL contours naturally deform into asymmetric, data-driven shapes.
3. **Range Preserving**: EL intervals for bounded parameters (e.g. positive variances) automatically respect physical boundaries without ad-hoc truncation.
4. **Bartlett Correctable**: Peter Hall (1990) proved that Owen's empirical likelihood is Bartlett-correctable, reducing coverage error from $\mathcal{O}(1/n)$ to $\mathcal{O}(1/n^2)$.

---


### Higher-Order Tail Calibrations and Higher-Order Asymptotics of Confidence Intervals
While standard first-order asymptotic confidence intervals rely upon the normal approximation $Z = \frac{\hat{\theta} - \theta}{\text{SE}(\hat{\theta})} \approx \mathcal{N}(0, 1)$, empirical coverage probabilities in moderate samples ($n \in [20, 100]$) frequently exhibit substantial coverage errors of order $\mathcal{O}(1/\sqrt{n})$ due to skewness in the underlying distribution.

To eliminate these asymmetric tail coverage errors, higher-order asymptotic theory develops Cornish–Fisher inversions and Edgeworth expansions of the standardized pivotal distribution:

$$\mathbb{P}\left( \frac{\hat{\theta} - \theta}{\text{SE}(\hat{\theta})} \le z \right) = \Phi(z) - \phi(z) \left[ \frac{\kappa_3}{6\sqrt{n}} (z^2 - 1) + \frac{\kappa_4}{24n} (z^3 - 3z) + \frac{\kappa_3^2}{72n} (z^5 - 10z^3 + 15z) \right] + \mathcal{O}\left( \frac{1}{n^{3/2}} \right)$$

where $\kappa_3$ and $\kappa_4$ denote the standardized skewness and kurtosis of the score function increments. Inverting this expansion analytically gives rise to skewness-corrected confidence bounds, where the upper and lower critical values are modified by asymmetric perturbation terms proportional to $\hat{\kappa}_3 / (6\sqrt{n})$.

Furthermore, Bartlett corrections apply directly to the likelihood ratio statistic $w(\theta) = 2(\ell(\hat{\theta}) - \ell(\theta))$. By dividing $w(\theta)$ by its expected value scale factor $1 + b/n$, where $b$ is computed from joint moments of the log-likelihood derivatives:

$$w^*(\theta) = \frac{w(\theta)}{1 + b/n} \sim \chi^2_1 + \mathcal{O}\left( \frac{1}{n^2} \right)$$

The resulting Bartlett-corrected likelihood ratio confidence interval achieves an exceptional coverage error rate of order $\mathcal{O}(1/n^2)$, outperforming ordinary Wald intervals by two entire orders of magnitude. This remarkable error reduction is achieved without requiring any computer-intensive resampling.

## Fully worked question 1: Rigorous Inversion and Coverage Comparison of Wald, Wilson Score, and Clopper-Pearson Binomial Intervals

### Question
An autonomous vehicle sensor validation lab tests the reliability of an object-detection radar system. In a test run of $n = 40$ pedestrian detection trials, the radar successfully detects pedestrians $X = 38$ times (an observed success rate $\hat{p} = 38/40 = 0.95$).

1. Compute the classical $95\%$ Wald confidence interval for the detection probability $p$. Check whether the upper confidence limit exceeds the physical bound of $1.0$.
2. Formulate the quadratic score inequality and derive the exact numerical endpoints of the $95\%$ Wilson Score confidence interval.
3. Compute the Agresti–Coull adjusted proportion $\tilde{p}$ and evaluate the Agresti–Coull $95\%$ confidence interval.
4. Using the Beta quantile formulation, calculate the exact $95\%$ Clopper–Pearson conservative confidence interval using:
   - $p_L = \text{Beta}(0.025; \, 38, \, 3) = 0.8308$
   - $p_U = \text{Beta}(0.975; \, 39, \, 2) = 0.9939$
   Compare all four intervals and discuss why the Wald interval is scientifically misleading in this high-reliability regime.

### Solution, step 1: Classical Wald interval
Sample size $n = 40$, successes $X = 38$.
Sample proportion:

$$\hat{p} = \frac{38}{40} = 0.95$$

Estimated standard error:

$$\text{SE}_{\text{Wald}} = \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}} = \sqrt{\frac{0.95 \times 0.05}{40}} = \sqrt{\frac{0.0475}{40}} = \sqrt{0.0011875} \approx 0.03446$$

For $95\%$ confidence, $z_{0.975} = 1.95996 \approx 1.960$.
Margin of error:

$$E = 1.960 \times 0.03446 \approx 0.06754$$

Endpoints:
- Lower limit: $0.95 - 0.06754 = 0.8825$
- Upper limit: $0.95 + 0.06754 = 1.0175$

The classical Wald $95\%$ confidence interval is:

$$[0.8825, \, 1.0175]$$

**Pathology:** The upper confidence limit $1.0175 > 1.0$, which violates the fundamental axiom of probability theory! A probability cannot exceed unity. Truncating at $1.0$ yields $[0.8825, 1.0000]$, which distorts the nominal confidence coefficient.

### Solution, step 2: Wilson Score interval
The Wilson score inequality is:

$$\frac{(\hat{p} - p)^2}{\frac{p(1 - p)}{n}} \le z^2$$

Substitute $\hat{p} = 0.95$, $n = 40$, and $z = 1.960$ ($z^2 = 3.8416$):

$$(0.95 - p)^2 \le \frac{3.8416}{40} p(1 - p) = 0.09604 p(1 - p)$$

Expand both sides:

$$0.9025 - 1.90 p + p^2 \le 0.09604 p - 0.09604 p^2$$

Collect all terms on the left:

$$(1 + 0.09604) p^2 - (1.90 + 0.09604) p + 0.9025 \le 0$$

$$1.09604 p^2 - 1.99604 p + 0.9025 \le 0$$

Solve using the quadratic formula $p = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$:
- $a = 1.09604$
- $b = -1.99604$
- $c = 0.9025$

Discriminant:

$$b^2 - 4ac = (-1.99604)^2 - 4(1.09604)(0.9025) = 3.984176 - 3.956704 = 0.027472$$

$$\sqrt{b^2 - 4ac} = \sqrt{0.027472} \approx 0.165747$$

Compute roots:
- Lower limit:
  $$p_L = \frac{1.99604 - 0.165747}{2(1.09604)} = \frac{1.830293}{2.19208} \approx 0.83495$$
- Upper limit:
  $$p_U = \frac{1.99604 + 0.165747}{2(1.09604)} = \frac{2.161787}{2.19208} \approx 0.98618$$

The exact $95\%$ Wilson Score interval is:

$$[0.8350, \, 0.9862]$$

Notice that:
- The interval is strictly contained inside $(0, 1)$.
- It is appropriately asymmetric: the lower margin ($0.95 - 0.835 = 0.115$) is much wider than the upper margin ($0.986 - 0.95 = 0.036$), reflecting the natural boundary barrier at $1.0$.

### Solution, step 3: Agresti–Coull interval
For $95\%$ confidence ($z \approx 2$), add $z^2 / 2 = 2$ successes and $z^2 = 4$ trials:
- $\tilde{n} = n + 4 = 40 + 4 = 44$
- $\tilde{X} = X + 2 = 38 + 2 = 40$
- $\tilde{p} = \frac{40}{44} = \frac{10}{11} \approx 0.90909$

Standard error:

$$\text{SE}_{\text{AC}} = \sqrt{\frac{\tilde{p}(1 - \tilde{p})}{\tilde{n}}} = \sqrt{\frac{0.90909 \times 0.09091}{44}} = \sqrt{\frac{0.082645}{44}} = \sqrt{0.001878} \approx 0.04334$$

Margin of error:

$$E = 1.960 \times 0.04334 \approx 0.08495$$

Endpoints:
- Lower: $0.90909 - 0.08495 = 0.8241$
- Upper: $0.90909 + 0.08495 = 0.9940$

The Agresti–Coull $95\%$ confidence interval is:

$$[0.8241, \, 0.9940]$$

This simple formula closely approximates the Wilson score interval without requiring any quadratic equations.

### Solution, step 4: Clopper–Pearson exact interval and comparison
The Clopper–Pearson exact interval is:

$$[0.8308, \, 0.9939]$$

**Comparison Table:**
- Classical Wald: $[0.8825, 1.0175]$ (Invalid: upper bound $> 1.0$, severely anticonservative lower bound)
- Wilson Score: $[0.8350, 0.9862]$ (Optimal: exact nominal coverage, strictly bounded)
- Agresti–Coull: $[0.8241, 0.9940]$ (Excellent approximation, slightly conservative)
- Clopper–Pearson: $[0.8308, 0.9939]$ (Strictly conservative, guaranteed coverage $\ge 95\%$)

In high-reliability engineering where $p \approx 1$ or $p \approx 0$, the Wald interval should never be used. The Wilson Score interval or Clopper–Pearson interval must be deployed.

---

## Fully worked question 2: BCa Bootstrap Confidence Interval Construction for the Correlation Coefficient with Skewness Correction

### Question
An ergonomic design team evaluates the relationship between operator cognitive reaction time $X$ (in milliseconds) and operational error rate $Y$ (errors per hour) in an air traffic control simulator. A sample of $n = 15$ operators is tested, yielding a sample Pearson correlation coefficient $r = 0.72$.

1. Construct the naive standard normal bootstrap interval assuming $B = 2,000$ bootstrap replications yield an empirical standard deviation $\widehat{\text{SE}}_{\text{boot}} = 0.125$.
2. In the bootstrap simulation, exactly $1,340$ out of the $2,000$ bootstrap estimates satisfy $r^{*b} < 0.72$. Compute the median bias-correction parameter $z_0 = \Phi^{-1}(1340 / 2000)$.
3. Jackknife influence values evaluate to an acceleration parameter $a = 0.045$. Calculate the adjusted BCa percentile probabilities $\alpha_1$ and $\alpha_2$ for a nominal $95\%$ confidence interval ($z_{0.025} = -1.960$ and $z_{0.975} = +1.960$).
4. Given that the empirical bootstrap quantiles corresponding to $\alpha_1$ and $\alpha_2$ are $r^{*(\alpha_1)} = 0.385$ and $r^{*(\alpha_2)} = 0.885$, compare the BCa interval to Fisher's variance-stabilized $z$-transformation interval:
   $$\text{arctanh}(\rho) \in \text{arctanh}(r) \pm \frac{1.960}{\sqrt{n - 3}}$$

### Solution, step 1: Naive standard normal bootstrap interval
Given $r = 0.72$, $n = 15$, and $\widehat{\text{SE}}_{\text{boot}} = 0.125$.
For $95\%$ confidence, $z_{0.975} = 1.960$.
Margin of error:

$$E = 1.960 \times 0.125 = 0.2450$$

The standard normal bootstrap interval is:

$$0.72 \pm 0.2450 = [0.4750, \, 0.9650]$$

This interval naively assumes that the sampling distribution of $r$ is symmetric and Gaussian. However, because $r = 0.72$ is close to the upper boundary $1.0$, the sampling distribution of $r$ is severely skewed to the left.

### Solution, step 2: Bias-correction parameter $z_0$
The proportion of bootstrap replications falling below the original point estimate $r = 0.72$ is:

$$p_0 = \frac{1,340}{2,000} = 0.6700$$

Since $p_0 = 0.67 > 0.50$, the bootstrap distribution has a median smaller than the point estimate, indicating positive skewness of estimation error.
Compute $z_0 = \Phi^{-1}(0.6700)$:
From standard normal CDF tables, $\Phi(0.440) \approx 0.6700$.
Thus:

$$z_0 = 0.440$$

### Solution, step 3: BCa adjusted percentile probabilities
Given $z_0 = 0.440$, acceleration $a = 0.045$, and $z_{0.025} = -1.960$, $z_{0.975} = 1.960$.
Compute the adjusted quantile arguments:

**1. Lower tail adjustment $\alpha_1$**:

$$w_1 = z_0 + \frac{z_0 + z_{0.025}}{1 - a(z_0 + z_{0.025})} = 0.440 + \frac{0.440 - 1.960}{1 - 0.045(0.440 - 1.960)}$$

$$w_1 = 0.440 + \frac{-1.520}{1 - 0.045(-1.520)} = 0.440 + \frac{-1.520}{1 + 0.0684} = 0.440 + \frac{-1.520}{1.0684} = 0.440 - 1.4227 = -0.9827$$

Now compute $\alpha_1 = \Phi(-0.9827)$:
From normal tables, $\Phi(-0.9827) \approx 0.1629$.
Instead of the naive $2.5\%$ lower quantile, the BCa adjustment samples at the **$16.29\%$ percentile**!

**2. Upper tail adjustment $\alpha_2$**:

$$w_2 = z_0 + \frac{z_0 + z_{0.975}}{1 - a(z_0 + z_{0.975})} = 0.440 + \frac{0.440 + 1.960}{1 - 0.045(0.440 + 1.960)}$$

$$w_2 = 0.440 + \frac{2.400}{1 - 0.045(2.400)} = 0.440 + \frac{2.400}{1 - 0.1080} = 0.440 + \frac{2.400}{0.8920} = 0.440 + 2.6906 = 3.1306$$

Now compute $\alpha_2 = \Phi(3.1306)$:
From normal tables, $\Phi(3.1306) \approx 0.9991$.
Instead of the naive $97.5\%$ upper quantile, the BCa adjustment samples at the **$99.91\%$ percentile**!

### Solution, step 4: BCa interval and comparison with Fisher's $z$
The resulting $95\%$ BCa bootstrap interval is:

$$[r^{*(0.1629)}, \, r^{*(0.9991)}] = [0.3850, \, 0.8850]$$

Now compare with Fisher's variance-stabilized $z$-transformation:
For $r = 0.72$:

$$z_r = \text{arctanh}(0.72) = \frac{1}{2} \ln\left( \frac{1 + 0.72}{1 - 0.72} \right) = \frac{1}{2} \ln\left( \frac{1.72}{0.28} \right) = \frac{1}{2} \ln(6.14286) = \frac{1}{2} (1.8153) \approx 0.9076$$

Standard error for $n = 15$:

$$\text{SE} = \frac{1}{\sqrt{n - 3}} = \frac{1}{\sqrt{12}} = \frac{1}{3.4641} \approx 0.2887$$

The $95\%$ confidence interval on the $z$-scale is:

$$0.9076 \pm 1.960 \times 0.2887 = 0.9076 \pm 0.5658 = [0.3418, \, 1.4734]$$

Now invert back to the correlation scale using $\rho = \tanh(z) = \frac{e^{2z} - 1}{e^{2z} + 1}$:
- Lower limit: $\tanh(0.3418) \approx 0.3289$
- Upper limit: $\tanh(1.4734) \approx 0.9002$

Fisher's exact $95\%$ interval is:

$$[0.3289, \, 0.9002]$$

Notice how closely the non-parametric BCa bootstrap interval $[0.385, 0.885]$ tracks Fisher's theoretical interval, successfully correcting for the severe left-skewness of $r$ without requiring any assumption of bivariate normality.

---

## Fully worked question 3: Profile Likelihood Ratio Confidence Interval for Non-Linear Hazard Ratios in Proportional Hazards Models

### Question
An oncology clinical research trial investigates survival times $T$ of patients with advanced non-small cell lung carcinoma receiving either an immunotherapy combination ($x_i = 1$) or standard chemotherapy ($x_i = 0$).
Failure times follow an exponential proportional hazards model with baseline hazard $\lambda > 0$ and treatment effect $\beta \in \mathbb{R}$:

$$h(t; x_i) = \lambda e^{\beta x_i}$$

The primary parameter of clinical interest is the **Hazard Ratio (HR)**:

$$\theta = e^\beta$$

In a trial of $n = 50$ patients, $n_1 = 25$ received immunotherapy and $n_0 = 25$ received chemotherapy. Over the trial duration:
- In the chemotherapy group ($x = 0$): $d_0 = 18$ deaths were observed with total person-time at risk $Y_0 = 120.0$ person-months.
- In the immunotherapy group ($x = 1$): $d_1 = 10$ deaths were observed with total person-time at risk $Y_1 = 150.0$ person-months.

1. Write down the full log-likelihood function $\ell(\lambda, \beta)$ and express it in terms of the hazard ratio $\theta = e^\beta$.
2. For any fixed candidate value of $\theta > 0$, derive the analytical expression for the constrained maximum likelihood estimate of the baseline hazard $\hat{\lambda}(\theta)$.
3. Substitute $\hat{\lambda}(\theta)$ to construct the explicit profile log-likelihood function $\ell_p(\theta)$.
4. Compute the Maximum Likelihood Estimate $\hat{\theta}_{\text{MLE}}$ and evaluate the $95\%$ Profile Likelihood Ratio confidence interval for the Hazard Ratio $\theta$ using the chi-square threshold $\ell_p(\hat{\theta}) - \ell_p(\theta) \le \frac{3.8415}{2} = 1.9208$. Compare this with the Wald interval for $\theta$.

### Solution, step 1: Log-likelihood in terms of Hazard Ratio $\theta$
For an exponential survival model, the log-likelihood is:

$$\ell(\lambda, \beta) = \sum_{i=1}^n [d_i \ln h(t_i; x_i) - H(t_i; x_i)] = \sum_{i=1}^n [d_i (\ln(\lambda) + \beta x_i) - \lambda e^{\beta x_i} y_i]$$

where $d_i$ is the event indicator and $y_i$ is observed time at risk.
Grouping by treatment arm ($x = 0$ and $x = 1$):

$$\ell(\lambda, \beta) = d_0 \ln(\lambda) - \lambda Y_0 + d_1 [\ln(\lambda) + \beta] - \lambda e^\beta Y_1$$

Substitute $\theta = e^\beta$ (so $\beta = \ln(\theta)$):

$$\ell(\lambda, \theta) = (d_0 + d_1) \ln(\lambda) + d_1 \ln(\theta) - \lambda (Y_0 + \theta Y_1)$$

Substitute observed values: $d_0 = 18$, $d_1 = 10$, $d = d_0 + d_1 = 28$, $Y_0 = 120.0$, $Y_1 = 150.0$:

$$\ell(\lambda, \theta) = 28 \ln(\lambda) + 10 \ln(\theta) - \lambda (120 + 150 \theta)$$

### Solution, step 2: Constrained MLE of baseline hazard $\hat{\lambda}(\theta)$
For any fixed value of $\theta > 0$, differentiate $\ell(\lambda, \theta)$ with respect to the nuisance parameter $\lambda$:

$$\frac{\partial \ell}{\partial \lambda} = \frac{28}{\lambda} - (120 + 150 \theta) = 0$$

Solving for $\lambda$:

$$\hat{\lambda}(\theta) = \frac{28}{120 + 150 \theta}$$

### Solution, step 3: Profile log-likelihood $\ell_p(\theta)$
Substitute $\hat{\lambda}(\theta)$ back into the log-likelihood:

$$\ell_p(\theta) = \ell(\hat{\lambda}(\theta), \theta) = 28 \ln\left( \frac{28}{120 + 150 \theta} \right) + 10 \ln(\theta) - \left( \frac{28}{120 + 150 \theta} \right) (120 + 150 \theta)$$

$$= 28 \ln(28) - 28 \ln(120 + 150 \theta) + 10 \ln(\theta) - 28$$

Notice that $28 \ln(28) - 28$ is a constant independent of $\theta$.
The kernel of the profile log-likelihood is:

$$\ell_p(\theta) = 10 \ln(\theta) - 28 \ln(120 + 150 \theta) + C$$

### Solution, step 4: Global MLE and Profile Likelihood Ratio Interval
To find the unconstrained MLE $\hat{\theta}$, maximize $\ell_p(\theta)$:

$$\frac{d\ell_p}{d\theta} = \frac{10}{\theta} - \frac{28 \times 150}{120 + 150 \theta} = 0$$

$$10(120 + 150 \theta) = 4,200 \theta$$

$$1,200 + 1,500 \theta = 4,200 \theta \implies 2,700 \theta = 1,200$$

$$\hat{\theta} = \frac{1,200}{2,700} = \frac{4}{9} \approx 0.4444$$

The immunotherapy combination reduces the hazard of death by approximately $55.6\%$ ($	ext{HR} = 0.444$).
Now evaluate the profile log-likelihood at the peak:
- At $\hat{\theta} = 0.4444$:
  $$120 + 150(0.4444) = 120 + 66.6667 = 186.6667$$
  $$\ell_p(\hat{\theta}) = 10 \ln(0.44444) - 28 \ln(186.6667) = 10(-0.81093) - 28(5.22933) = -8.1093 - 146.4212 = -154.5305$$

The $95\%$ Profile Likelihood Ratio interval consists of all $\theta > 0$ satisfying:

$$\ell_p(\theta) \ge \ell_p(\hat{\theta}) - 1.9208 = -154.5305 - 1.9208 = -156.4513$$

Solving $10 \ln(\theta) - 28 \ln(120 + 150 \theta) = -156.4513$ numerically via Newton's method yields the roots:
- Lower root: $\theta_L = 0.2085$
- Upper root: $\theta_U = 0.9124$

The $95\%$ Profile Likelihood Ratio confidence interval for the Hazard Ratio is:

$$\text{HR} \in [0.2085, \, 0.9124]$$

Because the entire interval lies strictly below $1.0$, the trial conclusively demonstrates that immunotherapy significantly prolongs survival relative to chemotherapy ($p < 0.05$). Furthermore, unlike a naive Wald interval $\hat{\theta} \pm 1.96 \text{SE}(\hat{\theta})$ which is symmetric on the linear HR scale and can generate negative lower limits, the Profile Likelihood interval is naturally asymmetric ($0.444 - 0.209 = 0.235$ vs $0.912 - 0.444 = 0.468$), respecting the multiplicative geometry of hazard ratios.
