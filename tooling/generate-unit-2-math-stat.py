#!/usr/bin/env python3
"""
Author Unit 2 for Mathematical Statistics.
Focuses on Random Samples, Joint Distributions, Sampling Statistics, and Moment Generating Techniques.
Generates >= 5,300 substantive prose words with zero KaTeX errors.
"""
from pathlib import Path

DEST = Path("publishing/drafts/statistics-probability-mathematical-statistics/unit-2.md")

content = r"""# Unit 2: Random Samples, Joint Distributions, Sampling Statistics, and Moment Generating Techniques

## 2.1 The Concept of Random Sampling, Exchangeability, and Joint Density Factorization

At the core of statistical inference lies the mathematical formulation of a random sample. In empirical science, data collection generates a sequence of observed numerical values resulting from some physical, biological, or social mechanism. In the language of probability theory, these observations are modeled as random variables defined on an underlying probability space $(\Omega, \mathcal{F}, P)$, where $\Omega$ is the sample space, $\mathcal{F}$ is the associated $\sigma$-algebra of events, and $P$ is a probability measure.

Let $X_1, X_2, \dots, X_n$ be random variables mapping the sample space $\Omega$ into the real line $\mathbb{R}$. We state that the collection of random variables $\mathbf{X} = (X_1, X_2, \dots, X_n)$ constitutes a **random sample of size $n$** from a population characterized by the cumulative distribution function $F(x; \boldsymbol{\theta})$ if two fundamental probabilistic conditions are simultaneously satisfied:
1. **Identical Distribution**: Each individual random variable $X_i$ possesses the exact same marginal probability distribution governed by the distribution function $F(x; \boldsymbol{\theta})$:
   $$P(X_i \le x) = F(x; \boldsymbol{\theta}) \quad \text{for all } x \in \mathbb{R} \text{ and for each } i \in \{1, 2, \dots, n\}$$
2. **Mutual Stochastic Independence**: The random variables $X_1, X_2, \dots, X_n$ are mutually independent, meaning that for any arbitrary sequence of Borel measurable sets $B_1, B_2, \dots, B_n \in \mathcal{B}(\mathbb{R})$, the joint probability factorizes as the product of the marginal probabilities:
   $$P(X_1 \in B_1, X_2 \in B_2, \dots, X_n \in B_n) = \prod_{i=1}^n P(X_i \in B_i)$$

This paired property is universally denoted by the acronym **i.i.d.** (independent and identically distributed). The statistical consequence of mutual independence is profound: the realization of any sub-collection of observations imparts zero probabilistic information regarding the behavior or values of the remaining observations, conditional on the true parameter $\boldsymbol{\theta}$.

To understand the scope of independence, it is illuminating to contrast it with the weaker condition of **exchangeability**. A sequence of random variables $X_1, \dots, X_n$ is said to be exchangeable if for every permutation $\pi$ of the indices $\{1, 2, \dots, n\}$, the joint probability distribution of the permuted vector $(X_{\pi(1)}, \dots, X_{\pi(n)})$ is identical to that of the original vector $(X_1, \dots, X_n)$. While every i.i.d. sequence is necessarily exchangeable due to the commutativity of real multiplication in product measures, exchangeable sequences need not be independent. A classic example is sampling without replacement from a finite population, where knowing that an earlier draw yielded a particular category slightly depletes that category, inducing negative covariance among draws while preserving permutation invariance. By de Finetti's Representation Theorem, any infinitely exchangeable sequence of random variables can be represented as a mixture of i.i.d. sequences with respect to some latent prior distribution, thereby anchoring the i.i.d. paradigm as the foundational mathematical building block of both frequentist and Bayesian statistical mechanics.

When the marginal distribution function $F(x; \boldsymbol{\theta})$ is dominated by a $\sigma$-finite reference measure $\mu$ on the measurable space $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ (such as the standard Lebesgue measure $\lambda$ in the continuous domain, or the discrete counting measure over a countable lattice), the Radon–Nikodym Theorem guarantees the existence of a marginal probability density function (or probability mass function) $f(x; \boldsymbol{\theta}) = \frac{dF}{d\mu}(x; \boldsymbol{\theta})$. Applying Tonelli's and Fubini's theorems to the product measure space, the joint distribution of the sample vector $\mathbf{X} = (X_1, \dots, X_n)$ is dominated by the product measure $\mu^n = \mu \times \dots \times \mu$ on $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$, and its joint density function decomposes completely into the product:

$$f_{\mathbf{X}}(\mathbf{x}; \boldsymbol{\theta}) = f(x_1, x_2, \dots, x_n; \boldsymbol{\theta}) = \prod_{i=1}^n f(x_i; \boldsymbol{\theta})$$

This product decomposition serves as the mathematical engine for constructing likelihood functions, computing sampling moments, and establishing finite-sample as well as asymptotic properties of estimators.

## 2.2 Sample Statistics, Induced $\sigma$-Algebras, and Data Reduction

Upon observing a realization $\mathbf{x} = (x_1, \dots, x_n)$ of the random sample $\mathbf{X}$, the raw data vector resides in an $n$-dimensional Euclidean space $\mathbb{R}^n$. In practical inference, an investigator rarely operates directly on the high-dimensional raw coordinates. Instead, the data vector is mapped into a lower-dimensional space through a function known as a **statistic**.

Formally, a statistic $T = T(\mathbf{X})$ is defined as a Borel measurable mapping:

$$T: (\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n)) \to (\mathbb{R}^m, \mathcal{B}(\mathbb{R}^m))$$

where the functional form of $T$ contains no unknown parameters. The requirement that $T$ be free of unknown parameters distinguishes statistics from general random functions; for instance, the sample average $\frac{1}{n}\sum_{i=1}^n X_i$ is a legitimate statistic, whereas the quantity $\frac{1}{n}\sum_{i=1}^n (X_i - \mu)$ is a pivot or structural function, but not a statistic when the population mean $\mu$ is unknown.

From a measure-theoretic standpoint, the transformation $T$ induces a sub-$\sigma$-algebra $\sigma(T) \subseteq \mathcal{B}(\mathbb{R}^n)$, defined by the collection of inverse images:

$$\sigma(T) = \{ T^{-1}(B) : B \in \mathcal{B}(\mathbb{R}^m) \}$$

The sub-$\sigma$-algebra $\sigma(T)$ represents the specific information concerning the underlying sample vector that can be discriminated by observing the value of $T$. Every statistic $T$ induces a partition of the sample space $\mathbb{R}^n$, where two sample vectors $\mathbf{x}$ and $\mathbf{y}$ belong to the same partition cell (equivalence class) if and only if $T(\mathbf{x}) = T(\mathbf{y})$. Data reduction consists precisely in collapsing each equivalence class into a single summary point, discarding within-cell variations while attempting to preserve between-cell variations that contain information about the unknown parameter $\boldsymbol{\theta}$.

Because the original sample vector $\mathbf{X}$ is a random vector governed by the probability measure $P_{\boldsymbol{\theta}}$, the statistic $T = T(\mathbf{X})$ is itself a random variable (or random vector if $m > 1$). The induced probability distribution of $T$, denoted $P_{\boldsymbol{\theta}}^T$ and defined on $(\mathbb{R}^m, \mathcal{B}(\mathbb{R}^m))$ by:

$$P_{\boldsymbol{\theta}}^T(B) = P_{\boldsymbol{\theta}}(\mathbf{X} \in T^{-1}(B)) = P_{\boldsymbol{\theta}}(T(\mathbf{X}) \in B) \quad \text{for all } B \in \mathcal{B}(\mathbb{R}^m)$$

is termed the **sampling distribution** of the statistic $T$. The determination of exact sampling distributions is crucial for constructing exact confidence intervals, computing exact $p$-values in hypothesis testing, and evaluating risk functions in decision theory.

## 2.3 The Sample Mean: Finite-Sample Properties, Linearity, and Variance Decay

The most ubiquitous summary statistic for location is the **sample mean**, denoted $\bar{X}$ and defined as the arithmetic average of the sample coordinates:

$$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$$

The sample mean represents an affine projection of the $n$-dimensional sample vector onto the one-dimensional equicoordinate subspace spanned by the all-ones vector $\mathbf{1}_n = (1, 1, \dots, 1)^T \in \mathbb{R}^n$.

### First Moment: Universality of Unbiasedness
Suppose that the population distribution possesses a finite first moment, meaning that $\mathbb{E}[|X_i|] < \infty$. Let $\mu = \mathbb{E}[X_i]$ denote the population mean. By the linearity of the mathematical expectation operator, the expectation of $\bar{X}$ is:

$$\mathbb{E}[\bar{X}] = \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^n X_i \right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i] = \frac{1}{n} (n \mu) = \mu$$

Notice that this derivation requires only the existence of the first moment $\mathbb{E}[|X_i|] < \infty$ and identical marginal expectations; it does not even require stochastic independence among the observations. Thus, the sample mean $\bar{X}$ is an **unbiased estimator** of the population mean $\mu$ across all probability distributions with finite mean.

### Second Moment: Standard Error Decay under Independence
Suppose further that the population distribution possesses a finite second moment, so that $\text{Var}(X_i) = \sigma^2 < \infty$. Using the properties of the variance operator on sums of random variables:

$$\text{Var}(\bar{X}) = \text{Var}\left( \frac{1}{n} \sum_{i=1}^n X_i \right) = \frac{1}{n^2} \text{Var}\left( \sum_{i=1}^n X_i \right) = \frac{1}{n^2} \left[ \sum_{i=1}^n \text{Var}(X_i) + 2 \sum_{1 \le i < j \le n} \text{Cov}(X_i, X_j) \right]$$

Because the random variables $X_1, \dots, X_n$ are mutually independent, every pairwise covariance vanishes identically: $\text{Cov}(X_i, X_j) = 0$ for all $i \ne j$. Consequently, the double summation vanishes, leaving:

$$\text{Var}(\bar{X}) = \frac{1}{n^2} \sum_{i=1}^n \sigma^2 = \frac{1}{n^2} (n \sigma^2) = \frac{\sigma^2}{n}$$

The positive square root of the sampling variance of $\bar{X}$ is the **standard error of the mean**:

$$\text{SE}(\bar{X}) = \sqrt{\text{Var}(\bar{X})} = \frac{\sigma}{\sqrt{n}}$$

This formula encapsulates the fundamental law of statistical precision: the variability of the sample mean diminishes inversely with the square root of the sample size, $\mathcal{O}(n^{-1/2})$. To halve the uncertainty surrounding the sample mean, an investigator must quadruple the sample size.

By Chebyshev's inequality, for any arbitrary positive tolerance $\epsilon > 0$:

$$P(|\bar{X} - \mu| \ge \epsilon) \le \frac{\text{Var}(\bar{X})}{\epsilon^2} = \frac{\sigma^2}{n \epsilon^2}$$

Taking the limit as the sample size $n \to \infty$, the upper bound converges to zero:

$$\lim_{n \to \infty} P(|\bar{X} - \mu| \ge \epsilon) = 0$$

This establishes that $\bar{X}$ converges in probability to the population mean $\mu$, proving the Weak Law of Large Numbers for any distribution with finite variance.

## 2.4 The Sample Variance: Bessel's Correction and Exact Derivation of Unbiasedness

To quantify the dispersion or variability of the observed data around their empirical center, statistics relies on the **sample variance**, denoted $S^2$. The sample variance is defined with divisor $n - 1$:

$$S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$$

The use of the denominator $n - 1$ instead of the sample size $n$ is known as **Bessel's correction**. To understand why this correction is necessary, consider the naive variance estimator using divisor $n$:

$$S_n^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2$$

Let us derive the expectation of $\sum_{i=1}^n (X_i - \bar{X})^2$ by decomposing the deviation of each observation $X_i$ from the sample mean into two orthogonal components: the deviation of $X_i$ from the true population mean $\mu$, and the deviation of the sample mean $\bar{X}$ from $\mu$:

$$X_i - \bar{X} = (X_i - \mu) - (\bar{X} - \mu)$$

Squaring both sides of this identity yields:

$$(X_i - \bar{X})^2 = \left[ (X_i - \mu) - (\bar{X} - \mu) \right]^2 = (X_i - \mu)^2 - 2 (X_i - \mu)(\bar{X} - \mu) + (\bar{X} - \mu)^2$$

Now, sum this equation across all observations $i = 1, 2, \dots, n$:

$$\sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i - \mu)^2 - 2 (\bar{X} - \mu) \sum_{i=1}^n (X_i - \mu) + \sum_{i=1}^n (\bar{X} - \mu)^2$$

Notice that $\sum_{i=1}^n (X_i - \mu) = \sum_{i=1}^n X_i - n\mu = n\bar{X} - n\mu = n(\bar{X} - \mu)$. Substituting this into the cross-product term:

$$-2 (\bar{X} - \mu) \left[ n (\bar{X} - \mu) \right] = -2n (\bar{X} - \mu)^2$$

The third term is a constant summed $n$ times: $\sum_{i=1}^n (\bar{X} - \mu)^2 = n (\bar{X} - \mu)^2$. Combining these expressions yields the celebrated algebraic identity for the sum of squared deviations:

$$\sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i - \mu)^2 - n (\bar{X} - \mu)^2$$

Now, take mathematical expectations across this identity:

$$\mathbb{E}\left[ \sum_{i=1}^n (X_i - \bar{X})^2 \right] = \sum_{i=1}^n \mathbb{E}\left[ (X_i - \mu)^2 \right] - n \mathbb{E}\left[ (\bar{X} - \mu)^2 \right]$$

By definition, $\mathbb{E}[(X_i - \mu)^2] = \text{Var}(X_i) = \sigma^2$ for every observation, so the first sum equals $n \sigma^2$. Furthermore, since $\bar{X}$ is an unbiased estimator of $\mu$, $\mathbb{E}[(\bar{X} - \mu)^2] = \text{Var}(\bar{X}) = \frac{\sigma^2}{n}$. Therefore:

$$\mathbb{E}\left[ \sum_{i=1}^n (X_i - \bar{X})^2 \right] = n \sigma^2 - n \left( \frac{\sigma^2}{n} \right) = n \sigma^2 - \sigma^2 = (n - 1) \sigma^2$$

This reveals that the naive estimator $S_n^2$ has expectation:

$$\mathbb{E}[S_n^2] = \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2 \right] = \frac{n - 1}{n} \sigma^2 = \sigma^2 - \frac{\sigma^2}{n}$$

The naive estimator is systematically biased downwards; on average, it underestimates the true population variance by the exact amount $\frac{\sigma^2}{n}$. The geometric reason for this bias is intuitive: the deviations are measured from the sample mean $\bar{X}$, which is the unique center of gravity that minimizes the sum of squared distances $\sum_{i=1}^n (X_i - c)^2$ over all real choices $c$. Since $\bar{X}$ adapts to the specific sample, the sum of squared deviations from $\bar{X}$ is always strictly smaller than the sum of squared deviations from the true population mean $\mu$ (unless $\bar{X}$ happens to coincide exactly with $\mu$).

Dividing the sum of squared deviations by $n - 1$ instead of $n$ neutralizes this bias completely:

$$\mathbb{E}[S^2] = \mathbb{E}\left[ \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2 \right] = \frac{(n-1)\sigma^2}{n-1} = \sigma^2$$

Thus, Bessel's correction guarantees that $S^2$ is an **unbiased estimator** of the population variance $\sigma^2$ for any arbitrary probability distribution possessing finite variance.

## 2.5 Linear Combinations of Random Variables and Geometry of Orthogonal Projections

Linear combinations of random variables form the theoretical infrastructure of analysis of variance, linear regression, time series filtering, and multivariate analysis. Let $X_1, X_2, \dots, X_n$ be random variables with mean vector $\boldsymbol{\mu} = (\mu_1, \dots, \mu_n)^T$ and covariance matrix $\boldsymbol{\Sigma}$, where the $(i, j)$-th entry of $\boldsymbol{\Sigma}$ is $\sigma_{ij} = \text{Cov}(X_i, X_j)$. 

Consider an arbitrary linear combination:

$$Y = \sum_{i=1}^n a_i X_i = \mathbf{a}^T \mathbf{X}$$

where $\mathbf{a} = (a_1, \dots, a_n)^T \in \mathbb{R}^n$ is a deterministic coefficient vector. By the linearity of the mathematical expectation:

$$\mathbb{E}[Y] = \mathbb{E}\left[ \mathbf{a}^T \mathbf{X} \right] = \mathbf{a}^T \mathbb{E}[\mathbf{X}] = \mathbf{a}^T \boldsymbol{\mu} = \sum_{i=1}^n a_i \mu_i$$

To compute the variance of $Y$, we express the variance operator in quadratic form:

$$\text{Var}(Y) = \mathbb{E}\left[ (Y - \mathbb{E}[Y])^2 \right] = \mathbb{E}\left[ (\mathbf{a}^T \mathbf{X} - \mathbf{a}^T \boldsymbol{\mu})^2 \right] = \mathbb{E}\left[ \left(\mathbf{a}^T (\mathbf{X} - \boldsymbol{\mu})\right) \left(\mathbf{a}^T (\mathbf{X} - \boldsymbol{\mu})\right)^T \right]$$

Since the inner product is a scalar, we can write:

$$\text{Var}(Y) = \mathbb{E}\left[ \mathbf{a}^T (\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T \mathbf{a} \right] = \mathbf{a}^T \mathbb{E}\left[ (\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T \right] \mathbf{a} = \mathbf{a}^T \boldsymbol{\Sigma} \mathbf{a}$$

Writing this quadratic form in scalar notation:

$$\text{Var}(Y) = \sum_{i=1}^n \sum_{j=1}^n a_i a_j \text{Cov}(X_i, X_j) = \sum_{i=1}^n a_i^2 \sigma_i^2 + 2 \sum_{1 \le i < j \le n} a_i a_j \sigma_{ij}$$

When the variables $X_1, \dots, X_n$ are mutually independent, the off-diagonal covariances vanish ($\sigma_{ij} = 0$ for all $i \ne j$), simplifying the quadratic form to a single diagonal sum:

$$\text{Var}\left( \sum_{i=1}^n a_i X_i \right) = \sum_{i=1}^n a_i^2 \sigma_i^2$$

Now, consider two distinct linear combinations:

$$Y_1 = \sum_{i=1}^n a_i X_i = \mathbf{a}^T \mathbf{X} \quad \text{and} \quad Y_2 = \sum_{j=1}^n b_j X_j = \mathbf{b}^T \mathbf{X}$$

The covariance between $Y_1$ and $Y_2$ is computed via bilinearity:

$$\text{Cov}(Y_1, Y_2) = \mathbb{E}\left[ (\mathbf{a}^T (\mathbf{X} - \boldsymbol{\mu})) (\mathbf{b}^T (\mathbf{X} - \boldsymbol{\mu})) \right] = \mathbf{a}^T \mathbb{E}\left[ (\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T \right] \mathbf{b} = \mathbf{a}^T \boldsymbol{\Sigma} \mathbf{b}$$

If the random variables $X_1, \dots, X_n$ are independent and identically distributed with common variance $\sigma^2$, then $\boldsymbol{\Sigma} = \sigma^2 \mathbf{I}_n$, where $\mathbf{I}_n$ is the $n \times n$ identity matrix. The covariance collapses to:

$$\text{Cov}(Y_1, Y_2) = \sigma^2 (\mathbf{a}^T \mathbf{b}) = \sigma^2 \sum_{i=1}^n a_i b_i$$

This provides a profound geometric connection between probability theory and Euclidean geometry: two linear combinations of i.i.d. variables are **uncorrelated** if and only if their coefficient vectors $\mathbf{a}$ and $\mathbf{b}$ are **orthogonal** in $\mathbb{R}^n$ with respect to the standard Euclidean inner product ($\mathbf{a}^T \mathbf{b} = 0$).

### Orthogonal Decomposition of the Sample Space
To see this geometry in action, consider the decomposition of the sample vector $\mathbf{X} \in \mathbb{R}^n$ into the sample mean vector and the residual vector. Define the vector of sample means $\mathbf{\bar{X}} = \bar{X} \mathbf{1}_n = (\bar{X}, \bar{X}, \dots, \bar{X})^T$. The sample mean vector lies in the 1-dimensional subspace $L = \text{span}(\mathbf{1}_n)$. The residual vector is:

$$\mathbf{R} = \mathbf{X} - \mathbf{\bar{X}} = (X_1 - \bar{X}, X_2 - \bar{X}, \dots, X_n - \bar{X})^T$$

Notice that the sum of the components of $\mathbf{R}$ is identically zero: $\sum_{i=1}^n (X_i - \bar{X}) = 0$. In vector notation, this means:

$$\mathbf{1}_n^T \mathbf{R} = \mathbf{1}_n^T (\mathbf{X} - \bar{X} \mathbf{1}_n) = \sum_{i=1}^n X_i - \bar{X} (\mathbf{1}_n^T \mathbf{1}_n) = n\bar{X} - n\bar{X} = 0$$

Thus, the residual vector $\mathbf{R}$ is strictly orthogonal to the equicoordinate vector $\mathbf{1}_n$. It resides in the $(n - 1)$-dimensional orthogonal complement subspace $L^\perp$. The projection matrix that projects any vector $\mathbf{X}$ onto $L$ is:

$$\mathbf{P} = \frac{1}{n} \mathbf{1}_n \mathbf{1}_n^T = \begin{pmatrix} 1/n & \dots & 1/n \\ \vdots & \ddots & \vdots \\ 1/n & \dots & 1/n \end{pmatrix}$$

The projection matrix that projects $\mathbf{X}$ onto $L^\perp$ is the centering matrix:

$$\mathbf{M} = \mathbf{I}_n - \mathbf{P} = \mathbf{I}_n - \frac{1}{n} \mathbf{1}_n \mathbf{1}_n^T$$

Both $\mathbf{P}$ and $\mathbf{M}$ are **symmetric idempotent matrices**: $\mathbf{P}^T = \mathbf{P}$, $\mathbf{P}^2 = \mathbf{P}$, $\mathbf{M}^T = \mathbf{M}$, and $\mathbf{M}^2 = \mathbf{M}$. Furthermore, they are mutually orthogonal: $\mathbf{P} \mathbf{M} = \mathbf{0}$. The sum of squared deviations can be written compactly as the squared Euclidean norm of the projected residual vector:

$$\sum_{i=1}^n (X_i - \bar{X})^2 = \|\mathbf{R}\|^2 = \|\mathbf{M} \mathbf{X}\|^2 = \mathbf{X}^T \mathbf{M}^T \mathbf{M} \mathbf{X} = \mathbf{X}^T \mathbf{M} \mathbf{X}$$

Because the rank of an idempotent matrix equals its trace, the dimension of the subspace $L^\perp$ where the residuals live is:

$$\text{rank}(\mathbf{M}) = \text{tr}(\mathbf{M}) = \text{tr}(\mathbf{I}_n) - \frac{1}{n} \text{tr}(\mathbf{1}_n \mathbf{1}_n^T) = n - \frac{1}{n}(n) = n - 1$$

This geometric fact is the origin of the term "degrees of freedom": the $n$ original random variables are constrained to lie in an $(n - 1)$-dimensional hyperplane because their sum around the sample mean must equal zero.

## 2.6 Moment Generating Functions: Analytical Foundations, Series Expansions, and Uniqueness

While the direct calculation of sampling distributions via multivariate integrals can become intractable, transform methods provide an elegant algebraic machinery. Among these, the **moment generating function (MGF)** is the primary tool for analyzing sums and linear combinations.

### Formal Definition and Convergence
Let $X$ be a random variable defined on $(\Omega, \mathcal{F}, P)$. The moment generating function of $X$, denoted $M_X(t)$, is defined as the mathematical expectation:

$$M_X(t) = \mathbb{E}\left[ e^{tX} \right]$$

for all real numbers $t \in \mathbb{R}$ for which the expectation exists and is finite. We say that the moment generating function of $X$ **exists** if there exists a strictly positive constant $h > 0$ such that $M_X(t) < \infty$ for all $t \in (-h, h)$.

If $X$ is a continuous random variable with probability density function $f(x)$, the MGF is given by the integral:

$$M_X(t) = \int_{-\infty}^\infty e^{tx} f(x) \, dx$$

If $X$ is a discrete random variable with probability mass function $p(x)$ supported on a countable set, the MGF is:

$$M_X(t) = \sum_{x} e^{tx} p(x)$$

The condition that $M_X(t)$ is finite in an open interval around the origin $(-h, h)$ imposes a strong constraint on the decay rate of the distribution's tails. Specifically, for $t \in (0, h)$, the integral $\int_0^\infty e^{tx} f(x) \, dx$ converges only if the right tail of $f(x)$ decays faster than $e^{-tx}$ as $x \to +\infty$. Similarly, for $t \in (-h, 0)$, convergence requires the left tail to decay faster than $e^{-|t||x|}$ as $x \to -\infty$. Distributions with "heavy tails"—such as the Student's $t$, Pareto, and Cauchy distributions—fail this requirement, and their moment generating functions do not exist for any $t \ne 0$.

### Differentiation and Moment Extraction
When $M_X(t)$ converges on an open interval $(-h, h)$, the function is infinitely differentiable (real analytic) on that domain. By the Dominated Convergence Theorem, we can interchange differentiation and expectation to any arbitrary order $k \in \mathbb{N}$:

$$\frac{d^k}{dt^k} M_X(t) = \frac{d^k}{dt^k} \mathbb{E}\left[ e^{tX} \right] = \mathbb{E}\left[ \frac{d^k}{dt^k} e^{tX} \right] = \mathbb{E}\left[ X^k e^{tX} \right]$$

Setting $t = 0$ collapses the exponential term to $e^0 = 1$, yielding the $k$-th raw moment $\mu_k' = \mathbb{E}[X^k]$:

$$\left. \frac{d^k}{dt^k} M_X(t) \right|_{t=0} = \mathbb{E}\left[ X^k \right] = \mu_k'$$

Expanding $M_X(t)$ in a Maclaurin series reveals that the raw moments are directly encoded as the series coefficients:

$$M_X(t) = \sum_{k=0}^\infty \frac{\mathbb{E}[X^k]}{k!} t^k = 1 + \mu_1' t + \frac{\mu_2'}{2!} t^2 + \frac{\mu_3'}{3!} t^3 + \dots$$

### The Uniqueness Theorem
The fundamental power of the MGF in distribution theory resides in its uniqueness.

**Theorem (MGF Uniqueness Theorem)**: Let $X$ and $Y$ be two random variables with cumulative distribution functions $F_X$ and $F_Y$. If their moment generating functions $M_X(t)$ and $M_Y(t)$ both exist and satisfy:

$$M_X(t) = M_Y(t) \quad \text{for all } t \in (-h, h) \text{ for some } h > 0$$

then $F_X(u) = F_Y(u)$ at all continuity points $u \in \mathbb{R}$. That is, $X$ and $Y$ have identical probability distributions.

This theorem establishes an injective relationship between probability distributions and moment generating functions. If the MGF of an unknown statistic can be algebraically derived and shown to match the MGF of a known parametric distribution, the statistic must follow that exact distribution.

### Algebraic Properties under Linear Operations
The MGF satisfies elementary algebraic properties under linear operations:
1. **Affine Transformation**: If $Y = aX + b$ for constants $a, b \in \mathbb{R}$, then:
   $$M_Y(t) = \mathbb{E}\left[ e^{t(aX + b)} \right] = e^{bt} \mathbb{E}\left[ e^{(at)X} \right] = e^{bt} M_X(at)$$
2. **Sums of Independent Random Variables**: If $X_1, X_2, \dots, X_n$ are mutually independent random variables with respective MGFs $M_{X_1}(t), \dots, M_{X_n}(t)$, then the MGF of their sum $Y = \sum_{i=1}^n X_i$ is the product of their individual MGFs:
   $$M_Y(t) = \mathbb{E}\left[ e^{t \sum_{i=1}^n X_i} \right] = \mathbb{E}\left[ \prod_{i=1}^n e^{t X_i} \right] = \prod_{i=1}^n \mathbb{E}\left[ e^{t X_i} \right] = \prod_{i=1}^n M_{X_i}(t)$$
3. **Sample Mean of i.i.d. Variates**: For the sample mean $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$ of an i.i.d. sample:
   $$M_{\bar{X}}(t) = M_{\sum X_i}\left( \frac{t}{n} \right) = \left[ M_X\left( \frac{t}{n} \right) \right]^n$$

## 2.7 Characteristic Functions: Universal Existence and Lévy's Inversion Theorem

While the moment generating function provides a convenient tool when it exists, its failure to converge for heavy-tailed distributions limits its mathematical generality. To overcome this restriction, mathematical statistics deploys the **characteristic function**, which extends the real parameter $t$ into the complex plane by defining the argument along the imaginary axis.

The characteristic function of a random variable $X$ is defined for all real $t \in \mathbb{R}$ by:

$$\phi_X(t) = \mathbb{E}\left[ e^{itX} \right] = \int_{-\infty}^\infty e^{itx} \, dF(x) = \mathbb{E}[\cos(tX)] + i \mathbb{E}[\sin(tX)]$$

where $i = \sqrt{-1}$ is the imaginary unit.

Because the integrand satisfies $|e^{itX}| = |\cos(tX) + i\sin(tX)| = \sqrt{\cos^2(tX) + \sin^2(tX)} = 1$, the integrand is universally bounded by 1 for all real numbers $t$ and $x$. Consequently:

$$|\phi_X(t)| = \left| \mathbb{E}[e^{itX}] \right| \le \mathbb{E}\left[ |e^{itX}| \right] = \mathbb{E}[1] = 1$$

Therefore, the characteristic function $\phi_X(t)$ **exists for every probability distribution without exception**, regardless of whether moments exist. The characteristic function possesses several universal structural properties:
1. $\phi_X(0) = \mathbb{E}[e^0] = 1$.
2. $\phi_X(-t) = \mathbb{E}[e^{-itX}] = \overline{\phi_X(t)}$, exhibiting Hermitian symmetry.
3. $\phi_X(t)$ is uniformly continuous on the entire real line $\mathbb{R}$.
4. If $Y = aX + b$, then $\phi_Y(t) = e^{itb} \phi_X(at)$.
5. If $X_1, \dots, X_n$ are independent, $\phi_{\sum X_i}(t) = \prod_{i=1}^n \phi_{X_i}(t)$.

### Lévy's Inversion Formula
The characteristic function uniquely determines the underlying probability distribution, as established by Paul Lévy.

**Theorem (Lévy's Inversion Theorem)**: Let $F(x)$ be the cumulative distribution function of $X$, and let $\phi(t)$ be its characteristic function. For any two real numbers $a < b$ that are continuity points of $F$:

$$F(b) - F(a) = \lim_{T \to \infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{-ita} - e^{-itb}}{it} \phi(t) \, dt$$

Furthermore, if the characteristic function is absolutely integrable over the real line, $\int_{-\infty}^\infty |\phi(t)| \, dt < \infty$, then the distribution of $X$ is absolutely continuous with respect to Lebesgue measure, and its probability density function $f(x)$ is continuous, bounded, and given by the inverse Fourier transform:

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^\infty e^{-itx} \phi(t) \, dt$$

This explicit inversion formula allows probability densities to be directly computed from characteristic functions, bridging distribution theory with harmonic analysis.

## 2.8 Cumulant Generating Functions, Invariants, and Marcinkiewicz's Theorem

While moments provide intuitive polynomial expectations, their algebra under summation is complicated by binomial and multinomial coefficients. A vastly more natural algebraic representation is provided by **cumulants**, which are defined via the logarithm of the moment generating function.

The **cumulant generating function (CGF)** of a random variable $X$, denoted $K_X(t)$, is defined as:

$$K_X(t) = \ln M_X(t) = \ln \mathbb{E}\left[ e^{tX} \right]$$

assuming $M_X(t)$ exists in an open interval $(-h, h)$ around zero. The cumulants $\kappa_1, \kappa_2, \kappa_3, \dots$ are the coefficients of the Maclaurin series expansion of $K_X(t)$:

$$K_X(t) = \sum_{r=1}^\infty \kappa_r \frac{t^r}{r!} = \kappa_1 t + \kappa_2 \frac{t^2}{2!} + \kappa_3 \frac{t^3}{3!} + \kappa_4 \frac{t^4}{4!} + \dots$$

Equivalently, the $r$-th cumulant is given by the $r$-th derivative of the CGF evaluated at $t = 0$:

$$\kappa_r = \left. \frac{d^r}{dt^r} K_X(t) \right|_{t=0}$$

### Mapping Between Cumulants and Central Moments
To derive the relationships between cumulants and moments, we expand $K_X(t) = \ln(1 + [M_X(t) - 1])$ using the Taylor series $\ln(1 + u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \frac{u^4}{4} + \dots$, where $M_X(t) - 1 = \mu_1' t + \frac{\mu_2'}{2} t^2 + \frac{\mu_3'}{6} t^3 + \dots$:

1. **First Cumulant ($\kappa_1$)**:
   $$\kappa_1 = \left. \frac{d}{dt} \ln M_X(t) \right|_{t=0} = \left. \frac{M_X'(t)}{M_X(t)} \right|_{t=0} = \frac{\mu_1'}{1} = \mu$$
   The first cumulant is the population mean.
2. **Second Cumulant ($\kappa_2$)**:
   $$\kappa_2 = \left. \frac{d^2}{dt^2} \ln M_X(t) \right|_{t=0} = \left. \frac{M_X''(t)M_X(t) - [M_X'(t)]^2}{[M_X(t)]^2} \right|_{t=0} = \mu_2' - (\mu_1')^2 = \sigma^2$$
   The second cumulant is the population variance $\mu_2$.
3. **Third Cumulant ($\kappa_3$)**:
   Differentiating once more yields:
   $$\kappa_3 = \mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3 = \mu_3 = \mathbb{E}[(X - \mu)^3]$$
   The third cumulant is the third central moment, capturing population skewness.
4. **Fourth Cumulant ($\kappa_4$)**:
   Computing the fourth derivative yields:
   $$\kappa_4 = \mu_4 - 3\mu_2^2 = \mu_4 - 3\sigma^4$$
   The fourth cumulant measures excess kurtosis. While the fourth central moment $\mu_4$ depends on variance, the fourth cumulant isolates the non-Gaussian tail behavior directly.

### The Fundamental Property: Strict Additivity under Independence
The supreme advantage of cumulants is their behavior under independent summation. Let $X_1, \dots, X_n$ be mutually independent random variables, and let $Y = \sum_{i=1}^n X_i$. Taking the logarithm of the product of MGFs:

$$K_Y(t) = \ln M_Y(t) = \ln\left( \prod_{i=1}^n M_{X_i}(t) \right) = \sum_{i=1}^n \ln M_{X_i}(t) = \sum_{i=1}^n K_{X_i}(t)$$

Equating coefficients of $\frac{t^r}{r!}$ on both sides demonstrates that for every integer order $r \ge 1$:

$$\kappa_r(Y) = \sum_{i=1}^n \kappa_r(X_i)$$

Cumulants are **strictly additive** under independent addition. There are no cross-terms or combinatorial expansions. To compute the $r$-th cumulant of a sum of independent random variables, one simply sums the individual $r$-th cumulants.

### Marcinkiewicz's Theorem
For a Gaussian distribution $\mathcal{N}(\mu, \sigma^2)$, the MGF is $M(t) = \exp(\mu t + \frac{1}{2}\sigma^2 t^2)$, so the CGF is an exact quadratic polynomial:

$$K(t) = \mu t + \frac{1}{2}\sigma^2 t^2$$

Consequently, for any normal distribution, $\kappa_1 = \mu$, $\kappa_2 = \sigma^2$, and **all higher-order cumulants vanish identically**: $\kappa_r = 0$ for all $r \ge 3$. 

A famous result by Józef Marcinkiewicz establishes that this is not an accident.

**Theorem (Marcinkiewicz's Theorem)**: If the cumulant generating function $K(t)$ of a random variable is a polynomial in $t$, then the degree of that polynomial cannot exceed 2. That is, the polynomial must either be of degree 1 (a degenerate point-mass distribution) or of degree 2 (a Gaussian distribution).

Marcinkiewicz's Theorem reveals that no non-degenerate probability distribution can have its cumulants vanish beyond order 3, 4, or any higher finite order: either an infinite number of cumulants are non-zero, or only the first two are non-zero. This provides a deep mathematical characterization of the Gaussian distribution as the unique distribution having finite cumulant complexity.

## 2.9 Convolution Integrals, Bivariate Transformations, and Jacobian Coordinate Changes

When moment generating functions are inaccessible or when one requires the exact joint distribution of dependent variables, transformation of variables via Jacobian matrices and convolution integrals provides the fundamental constructive pathway.

### The Multidimensional Change of Variables Theorem
Let $\mathbf{X} = (X_1, X_2)^T$ be a continuous bivariate random vector with joint probability density function $f_{\mathbf{X}}(x_1, x_2)$ supported on an open set $\mathcal{S} \subseteq \mathbb{R}^2$. Consider a transformation:

$$Y_1 = g_1(X_1, X_2) \quad \text{and} \quad Y_2 = g_2(X_1, X_2)$$

Assume that this mapping $\mathbf{g}: \mathcal{S} \to \mathcal{T} \subseteq \mathbb{R}^2$ is a bijective, continuously differentiable function with inverse mapping:

$$X_1 = h_1(Y_1, Y_2) \quad \text{and} \quad X_2 = h_2(Y_1, Y_2)$$

The **Jacobian matrix** of the inverse transformation is the $2 \times 2$ matrix of partial derivatives:

$$J = \begin{pmatrix} \frac{\partial h_1}{\partial y_1} & \frac{\partial h_1}{\partial y_2} \\ \frac{\partial h_2}{\partial y_1} & \frac{\partial h_2}{\partial y_2} \end{pmatrix}$$

The Jacobian determinant, denoted $\det(J)$, captures the local area deformation factor under the coordinate change. By the multivariable change of variables theorem for Lebesgue integrals, the joint probability density function of $\mathbf{Y} = (Y_1, Y_2)^T$ on $\mathcal{T}$ is given by:

$$f_{\mathbf{Y}}(y_1, y_2) = f_{\mathbf{X}}\left( h_1(y_1, y_2), h_2(y_1, y_2) \right) \cdot \left| \det(J) \right|$$

and zero elsewhere.

### The Convolution Formula for Sums
To determine the probability density function of the sum $Y = X_1 + X_2$ of two continuous random variables, we introduce an auxiliary variable $Z = X_2$. The forward transformation is:

$$Y = X_1 + X_2, \quad Z = X_2$$

The inverse transformation is:

$$X_1 = Y - Z, \quad X_2 = Z$$

The Jacobian matrix of the inverse mapping is:

$$J = \begin{pmatrix} \frac{\partial x_1}{\partial y} & \frac{\partial x_1}{\partial z} \\ \frac{\partial x_2}{\partial y} & \frac{\partial x_2}{\partial z} \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

The determinant is $\det(J) = (1)(1) - (-1)(0) = 1$, so $|\det(J)| = 1$. The joint density of $(Y, Z)$ is therefore:

$$f_{Y, Z}(y, z) = f_{X_1, X_2}(y - z, z)$$

To obtain the marginal density of the sum $Y$, we integrate out the auxiliary variable $z$ over $\mathbb{R}$:

$$f_Y(y) = \int_{-\infty}^\infty f_{X_1, X_2}(y - z, z) \, dz$$

When $X_1$ and $X_2$ are independent, the joint density factorizes as $f_{X_1, X_2}(x_1, x_2) = f_{X_1}(x_1) f_{X_2}(x_2)$, yielding the classical **convolution integral**:

$$f_{X_1 + X_2}(y) = (f_{X_1} * f_{X_2})(y) = \int_{-\infty}^\infty f_{X_1}(y - z) f_{X_2}(z) \, dz = \int_{-\infty}^\infty f_{X_1}(z) f_{X_2}(y - z) \, dz$$

When both variables are non-negative ($X_1 \ge 0, X_2 \ge 0$), the integrand is non-zero only when $z \ge 0$ and $y - z \ge 0$, which restricts the integration limits to $z \in [0, y]$:

$$f_{X_1 + X_2}(y) = \int_0^y f_{X_1}(y - z) f_{X_2}(z) \, dz \quad \text{for } y \ge 0$$

### Quotient and Product Formulas
Similar Jacobian transformations yield standard formulas for ratios and products:
1. **Ratio Transformation**: Let $U = X_1 / X_2$ and $V = X_2$. The inverse is $X_1 = U V$ and $X_2 = V$. The Jacobian determinant is $|\det(J)| = |v|$. Integrating out $v$ yields the ratio density:
   $$f_{X_1 / X_2}(u) = \int_{-\infty}^\infty |v| f_{X_1, X_2}(u v, v) \, dv$$
2. **Product Transformation**: Let $W = X_1 X_2$ and $V = X_2$. The inverse is $X_1 = W / V$ and $X_2 = V$. The Jacobian determinant is $|\det(J)| = 1/|v|$. Integrating out $v$ yields the product density:
   $$f_{X_1 X_2}(w) = \int_{-\infty}^\infty \frac{1}{|v|} f_{X_1, X_2}\left( \frac{w}{v}, v \right) \, dv$$

## 2.10 The Probability Integral Transform and Universal Sampling

A fundamental result connecting arbitrary continuous distributions with the standard uniform distribution is the **Probability Integral Transform**.

**Theorem (Probability Integral Transform)**: Let $X$ be a continuous random variable whose cumulative distribution function $F_X(x) = P(X \le x)$ is strictly increasing and continuous on its support. Define the transformed random variable:

$$U = F_X(X)$$

Then $U$ is distributed uniformly on the open unit interval $(0, 1)$:

$$U \sim \text{Uniform}(0, 1)$$

**Proof**:
Since $F_X$ is strictly increasing and continuous, its inverse function $F_X^{-1}: (0, 1) \to \mathbb{R}$ is strictly increasing and uniquely defined. For any $u \in (0, 1)$, the cumulative distribution function of $U$ is:

$$F_U(u) = P(U \le u) = P(F_X(X) \le u)$$

Applying the strictly increasing function $F_X^{-1}$ to both sides of the inequality preserves the inequality direction:

$$F_U(u) = P\left( X \le F_X^{-1}(u) \right) = F_X\left( F_X^{-1}(u) \right) = u$$

For $u \le 0$, $F_U(u) = 0$, and for $u \ge 1$, $F_U(u) = 1$. The CDF $F_U(u) = u$ on $(0, 1)$ is the exact CDF of a $\text{Uniform}(0, 1)$ random variable. Differentiating with respect to $u$ yields the constant density $f_U(u) = 1$ on $(0, 1)$. $\blacksquare$

### The Inverse Transform Method for Simulation
The converse of the Probability Integral Transform provides the theoretical foundation for generating pseudo-random variates from any arbitrary target distribution.

**Theorem (Inverse Transform Generation)**: Let $U \sim \text{Uniform}(0, 1)$, and let $F$ be any cumulative distribution function (continuous or discrete). Define the generalized inverse (quantile function):

$$F^{-1}(u) = \inf\{ x \in \mathbb{R} : F(x) \ge u \}, \quad u \in (0, 1)$$

Then the random variable $X = F^{-1}(U)$ has exact cumulative distribution function $F$.

This theorem guarantees that given a uniform random number generator, evaluating the inverse CDF $F^{-1}(U)$ generates exact, independent samples from any target distribution, anchoring computational Monte Carlo sampling in rigorous distribution theory.

## 2.11 Covariance Between Sample Moments and Geary's Characterization

In non-Gaussian parent populations, sample statistics frequently exhibit intricate statistical dependencies. While the sample mean $\bar{X}$ and sample variance $S^2$ are independent under normal sampling (as proved in Unit 3), they are generally correlated when sampling from skewed populations.

To derive the exact covariance between $\bar{X}$ and $S^2$, let $X_1, \dots, X_n$ be an i.i.d. random sample from a population with mean $\mu$, variance $\sigma^2$, and third central moment $\mu_3 = \mathbb{E}[(X - \mu)^3]$. We wish to evaluate:

$$\text{Cov}(\bar{X}, S^2) = \mathbb{E}\left[(\bar{X} - \mu)(S^2 - \sigma^2)\right] = \mathbb{E}[(\bar{X} - \mu) S^2] - \sigma^2 \mathbb{E}[\bar{X} - \mu]$$

Since $\mathbb{E}[\bar{X} - \mu] = 0$, the covariance simplifies to:

$$\text{Cov}(\bar{X}, S^2) = \mathbb{E}[(\bar{X} - \mu) S^2]$$

Recall the algebraic identity:

$$S^2 = \frac{1}{n-1} \left( \sum_{i=1}^n (X_i - \mu)^2 - n(\bar{X} - \mu)^2 \right)$$

Multiplying by $\bar{X} - \mu = \frac{1}{n} \sum_{j=1}^n (X_j - \mu)$ yields:

$$\mathbb{E}[(\bar{X} - \mu) S^2] = \frac{1}{n-1} \mathbb{E}\left[ (\bar{X} - \mu) \sum_{i=1}^n (X_i - \mu)^2 - n(\bar{X} - \mu)^3 \right]$$

Now, expand the first term:

$$\mathbb{E}\left[ (\bar{X} - \mu) \sum_{i=1}^n (X_i - \mu)^2 \right] = \frac{1}{n} \sum_{j=1}^n \sum_{i=1}^n \mathbb{E}\left[ (X_j - \mu)(X_i - \mu)^2 \right]$$

When $j \ne i$, by independence:

$$\mathbb{E}\left[ (X_j - \mu)(X_i - \mu)^2 \right] = \mathbb{E}[X_j - \mu] \cdot \mathbb{E}[(X_i - \mu)^2] = 0 \cdot \sigma^2 = 0$$

When $j = i$, the expectation is the third central moment:

$$\mathbb{E}[(X_i - \mu)^3] = \mu_3$$

There are exactly $n$ such diagonal terms ($i = j \in \{1, \dots, n\}$). Therefore:

$$\mathbb{E}\left[ (\bar{X} - \mu) \sum_{i=1}^n (X_i - \mu)^2 \right] = \frac{1}{n} (n \mu_3) = \mu_3$$

Next, we evaluate $\mathbb{E}[(\bar{X} - \mu)^3]$:

$$\mathbb{E}[(\bar{X} - \mu)^3] = \mathbb{E}\left[ \left(\frac{1}{n}\sum_{i=1}^n (X_i - \mu)\right)^3 \right] = \frac{1}{n^3} \sum_{i=1}^n \sum_{j=1}^n \sum_{k=1}^n \mathbb{E}[(X_i - \mu)(X_j - \mu)(X_k - \mu)]$$

By mutual independence, any expectation where an index appears with power 1 vanishes because $\mathbb{E}[X_i - \mu] = 0$. The only terms that survive are those where all three indices coincide: $i = j = k$. There are $n$ such terms, each evaluating to $\mu_3$. Thus:

$$\mathbb{E}[(\bar{X} - \mu)^3] = \frac{1}{n^3} (n \mu_3) = \frac{\mu_3}{n^2}$$

Substituting both expressions back into our covariance formula:

$$\text{Cov}(\bar{X}, S^2) = \frac{1}{n-1} \left( \mu_3 - n \left(\frac{\mu_3}{n^2}\right) \right) = \frac{1}{n-1} \left( \mu_3 - \frac{\mu_3}{n} \right) = \frac{1}{n-1} \mu_3 \left( \frac{n-1}{n} \right) = \frac{\mu_3}{n}$$

This is an exact, finite-sample result of fundamental importance:

$$\text{Cov}(\bar{X}, S^2) = \frac{\mu_3}{n}$$

We observe the following key implications:
1. If the population distribution is symmetric about its mean ($\mu_3 = 0$), such as in the Gaussian, Student's $t$, Uniform, or Laplace distributions, then $\text{Cov}(\bar{X}, S^2) = 0$. The sample mean and sample variance are completely uncorrelated.
2. If the population distribution is positively skewed ($\mu_3 > 0$), such as in the Exponential, Gamma, Lognormal, or Poisson distributions, then $\text{Cov}(\bar{X}, S^2) > 0$. When the sample mean is unusually large, the sample variance also tends to be unusually large.
3. If the population distribution is negatively skewed ($\mu_3 < 0$), such as in left-skewed Beta distributions, then $\text{Cov}(\bar{X}, S^2) < 0$.

This result underscores that zero correlation between $\bar{X}$ and $S^2$ is a universal feature of symmetric populations, but full stochastic independence between them is a unique signature reserved exclusively for Gaussian populations, as established by Geary's Theorem.

## 2.12 Sampling from Finite Populations, Combinatorial Hypergeometric Models, and the Finite Population Correction

While the classical statistical framework presumes an infinite superpopulation or continuous data-generating mechanism yielding strictly independent observations, real-world survey methodology, ecological census tracking, and auditing procedures frequently sample from a finite, enumerated collection of $N$ identifiable population units. Let the population values be denoted by the finite sequence $\{y_1, y_2, \dots, y_N\}$, with fixed finite population mean $\mu_N = \frac{1}{N}\sum_{i=1}^N y_i$ and finite population variance $\sigma_N^2 = \frac{1}{N}\sum_{i=1}^N (y_i - \mu_N)^2$.

When drawing a sample of size $n < N$ **without replacement** (Simple Random Sampling Without Replacement, or SRSWOR), every possible subset of size $n$ has an identical probability of selection, equal to $1/\binom{N}{n}$. The resulting sample sequence $X_1, X_2, \dots, X_n$ is identically distributed: each $X_i$ has marginal probability distribution $P(X_i = y_k) = 1/N$ for all $k \in \{1, \dots, N\}$. Consequently, the marginal expectation and variance are identical across all draw indices:

$$\mathbb{E}[X_i] = \mu_N, \quad \text{Var}(X_i) = \sigma_N^2$$

However, because the sampling is executed without replacement, the observations are **not mutually independent**. Selecting a specific value $y_k$ on an earlier draw physically removes that value from the available urn, preventing its re-selection and thereby inducing a negative statistical dependency across all distinct coordinates. Specifically, for any pair $i \ne j$, the joint probability is:

$$P(X_i = y_k, X_j = y_m) = \frac{1}{N(N-1)} \quad \text{for } k \ne m$$

with the probability vanishing when $k = m$. The joint expectation is:

$$\mathbb{E}[X_i X_j] = \sum_{k=1}^N \sum_{m \ne k}^N y_k y_m \frac{1}{N(N-1)} = \frac{1}{N(N-1)} \left[ \left(\sum_{k=1}^N y_k\right)^2 - \sum_{k=1}^N y_k^2 \right]$$

Recognizing that $\sum_{k=1}^N y_k = N\mu_N$ and $\sum_{k=1}^N y_k^2 = N(\sigma_N^2 + \mu_N^2)$, the cross-product simplifies to:

$$\mathbb{E}[X_i X_j] = \frac{1}{N(N-1)} \left[ N^2 \mu_N^2 - N(\sigma_N^2 + \mu_N^2) \right] = \mu_N^2 - \frac{\sigma_N^2}{N - 1}$$

Subtracting $\mathbb{E}[X_i]\mathbb{E}[X_j] = \mu_N^2$, we obtain the exact pairwise covariance between any two distinct draws:

$$\text{Cov}(X_i, X_j) = -\frac{\sigma_N^2}{N - 1} < 0$$

This negative covariance reflects the physical conservation of units: observing an unusually large value depletes the remaining pool, making subsequent draws marginally smaller on average.

To determine the sampling variance of the sample mean $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ under SRSWOR, we sum the variances and covariances:

$$\text{Var}(\bar{X}) = \frac{1}{n^2} \left[ \sum_{i=1}^n \text{Var}(X_i) + \sum_{i=1}^n \sum_{j \ne i}^n \text{Cov}(X_i, X_j) \right] = \frac{1}{n^2} \left[ n \sigma_N^2 + n(n-1)\left(-\frac{\sigma_N^2}{N-1}\right) \right]$$

Factoring out $\frac{\sigma_N^2}{n}$:

$$\text{Var}(\bar{X}) = \frac{\sigma_N^2}{n} \left[ 1 - \frac{n - 1}{N - 1} \right] = \frac{\sigma_N^2}{n} \left( \frac{N - n}{N - 1} \right)$$

Defining the population-adjusted variance $S_N^2 = \frac{N}{N-1}\sigma_N^2 = \frac{1}{N-1}\sum_{i=1}^N (y_i - \mu_N)^2$, this takes the classical form:

$$\text{Var}(\bar{X}) = \frac{S_N^2}{n} \left( 1 - \frac{n}{N} \right) = \frac{S_N^2}{n} (1 - f)$$

where $f = \frac{n}{N}$ is the **sampling fraction**, and the dimensionless factor:

$$\text{FPC} = 1 - f = \frac{N - n}{N}$$

is the **Finite Population Correction (FPC)**. The FPC quantifies the exact reduction in sampling variability achieved when a substantial proportion of the entire population has been observed. When the population size $N \to \infty$ while the sample size $n$ remains fixed, the sampling fraction $f \to 0$, causing the FPC to converge to 1, gracefully recovering the standard infinite-population variance formula $\sigma^2 / n$. In the extreme limit where the entire population is sampled ($n = N$), the FPC collapses to zero, reflecting the deterministic fact that an exhaustive census possesses zero sampling error.

## 2.13 Exact Distribution of Linear Contrasts, Orthogonal Matrices, and the Helmert Transformation

In experimental design, comparative clinical trials, and analysis of variance (ANOVA), researchers frequently investigate hypotheses concerning differences or weighted comparisons among group means. Such mathematical objects are termed **linear contrasts**.

Let $X_1, X_2, \dots, X_n$ be independent random variables with means $\mu_1, \dots, \mu_n$ and common variance $\sigma^2$. A linear combination:

$$C = \sum_{i=1}^n c_i X_i = \mathbf{c}^T \mathbf{X}$$

is defined as a **contrast** if the scalar coefficients sum identically to zero:

$$\sum_{i=1}^n c_i = \mathbf{c}^T \mathbf{1}_n = 0$$

Contrasts represent differences between subsets of variables. For instance, the simple pairwise difference $X_1 - X_2$ corresponds to $\mathbf{c} = (1, -1, 0, \dots, 0)^T$, and comparing the average of two treatment groups to a control group corresponds to $\mathbf{c} = (1/2, 1/2, -1, 0, \dots, 0)^T$.

The expectation of a contrast is the contrast of expectations:

$$\mathbb{E}[C] = \sum_{i=1}^n c_i \mu_i$$

If all group means are identical ($\mu_1 = \dots = \mu_n = \mu$), then $\mathbb{E}[C] = \mu \sum_{i=1}^n c_i = \mu(0) = 0$, regardless of the magnitude of $\mu$. The variance of the contrast is:

$$\text{Var}(C) = \sum_{i=1}^n c_i^2 \sigma^2 = \sigma^2 \|\mathbf{c}\|^2$$

Now consider two distinct contrasts $C_1 = \mathbf{c}_1^T \mathbf{X}$ and $C_2 = \mathbf{c}_2^T \mathbf{X}$, where $\sum_{i=1}^n c_{1i} = 0$ and $\sum_{i=1}^n c_{2i} = 0$. The covariance between these two contrasts is:

$$\text{Cov}(C_1, C_2) = \sigma^2 (\mathbf{c}_1^T \mathbf{c}_2) = \sigma^2 \sum_{i=1}^n c_{1i} c_{2i}$$

Two contrasts are said to be **orthogonal contrasts** if their coefficient vectors are orthogonal in $\mathbb{R}^n$:

$$\mathbf{c}_1^T \mathbf{c}_2 = \sum_{i=1}^n c_{1i} c_{2i} = 0$$

When contrasts are orthogonal, their covariance is zero. In a collection of $n$ observations, one can construct at most $n - 1$ mutually orthogonal contrasts that are simultaneously orthogonal to the equicoordinate vector $\mathbf{1}_n$. This geometric structure is operationalized through the **Helmert Transformation**.

### The Helmert Transformation Matrix
The Helmert transformation is an explicit, constructive $n \times n$ orthogonal matrix $\mathbf{H}$ whose first row is proportional to $\mathbf{1}_n^T$, and whose remaining $n - 1$ rows constitute mutually orthogonal contrasts of normalized length 1:

$$\mathbf{H} = \begin{pmatrix}
\frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \frac{1}{\sqrt{n}} & \dots & \frac{1}{\sqrt{n}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} & 0 & \dots & 0 \\
\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{6}} & -\frac{2}{\sqrt{6}} & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{1}{\sqrt{k(k-1)}} & \dots & \frac{1}{\sqrt{k(k-1)}} & -\frac{k-1}{\sqrt{k(k-1)}} & \dots \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{1}{\sqrt{n(n-1)}} & \frac{1}{\sqrt{n(n-1)}} & \dots & \dots & -\frac{n-1}{\sqrt{n(n-1)}}
\end{pmatrix}$$

By construction, $\mathbf{H}$ satisfies the orthogonality condition:

$$\mathbf{H} \mathbf{H}^T = \mathbf{H}^T \mathbf{H} = \mathbf{I}_n$$

Let $\mathbf{Y} = \mathbf{H} \mathbf{X}$ denote the transformed random vector. Let us examine the individual components of $\mathbf{Y} = (Y_1, Y_2, \dots, Y_n)^T$:
1. The first component is:
   $$Y_1 = \sum_{i=1}^n \frac{1}{\sqrt{n}} X_i = \sqrt{n} \left( \frac{1}{n} \sum_{i=1}^n X_i \right) = \sqrt{n} \bar{X}$$
   The first transformed variable is an exact scalar multiple of the sample mean.
2. The remaining components $Y_2, Y_3, \dots, Y_n$ are mutually orthogonal contrasts that depend exclusively on pairwise and progressive differences among the observations, containing zero contribution from the grand sample mean.

Because $\mathbf{H}$ is an orthogonal transformation, it preserves the Euclidean inner product and Euclidean norm:

$$\|\mathbf{Y}\|^2 = \mathbf{Y}^T \mathbf{Y} = (\mathbf{H}\mathbf{X})^T (\mathbf{H}\mathbf{X}) = \mathbf{X}^T (\mathbf{H}^T \mathbf{H}) \mathbf{X} = \mathbf{X}^T \mathbf{I}_n \mathbf{X} = \mathbf{X}^T \mathbf{X} = \sum_{i=1}^n X_i^2$$

Now, expand the left side as the sum of squared transformed components:

$$\sum_{i=1}^n Y_i^2 = Y_1^2 + \sum_{j=2}^n Y_j^2 = (\sqrt{n}\bar{X})^2 + \sum_{j=2}^n Y_j^2 = n\bar{X}^2 + \sum_{j=2}^n Y_j^2$$

Equating this to $\sum_{i=1}^n X_i^2$ yields the fundamental identity:

$$\sum_{j=2}^n Y_j^2 = \sum_{i=1}^n X_i^2 - n\bar{X}^2 = \sum_{i=1}^n (X_i - \bar{X})^2 = (n - 1) S^2$$

This establishes that the sum of squared deviations $(n - 1) S^2$ is **identically equal to the sum of squares of the last $n - 1$ Helmert variables**:

$$(n - 1) S^2 = \sum_{j=2}^n Y_j^2$$

This algebraic decomposition provides the exact geometric foundation for proving the independence of the sample mean and sample variance in Gaussian populations, because the transformation maps the sample mean exclusively into $Y_1$, while mapping the sample variance exclusively into the remaining orthogonal coordinates $Y_2, \dots, Y_n$.

## 2.14 The Bivariate Normal Distribution, Conditional Gaussian Laws, and the Correlation Coefficient

When sampling pairs of measurements $(X_{1i}, X_{2i})$ from a shared physical or biological subject (such as height and weight, parental and offspring trait values, or pre-test and post-test scores), the univariate framework generalizes to bivariate and multivariate distributions. The canonical baseline for joint continuous modeling is the **bivariate normal distribution**.

A bivariate random vector $\mathbf{X} = (X_1, X_2)^T$ follows a bivariate normal distribution, denoted $\mathbf{X} \sim \mathcal{N}_2(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, with mean vector $\boldsymbol{\mu} = (\mu_1, \mu_2)^T$ and positive-definite covariance matrix:

$$\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{pmatrix}$$

where $\sigma_1 > 0$, $\sigma_2 > 0$, and the Pearson correlation coefficient $\rho \in (-1, 1)$ measures the degree of linear association between the two components. The determinant of the covariance matrix is:

$$\det(\boldsymbol{\Sigma}) = \sigma_1^2 \sigma_2^2 - (\rho \sigma_1 \sigma_2)^2 = \sigma_1^2 \sigma_2^2 (1 - \rho^2)$$

The inverse covariance matrix (the precision matrix) is computed explicitly:

$$\boldsymbol{\Sigma}^{-1} = \frac{1}{\sigma_1^2 \sigma_2^2 (1 - \rho^2)} \begin{pmatrix} \sigma_2^2 & -\rho \sigma_1 \sigma_2 \\ -\rho \sigma_1 \sigma_2 & \sigma_1^2 \end{pmatrix} = \frac{1}{1 - \rho^2} \begin{pmatrix} 1/\sigma_1^2 & -\rho/(\sigma_1 \sigma_2) \\ -\rho/(\sigma_1 \sigma_2) & 1/\sigma_2^2 \end{pmatrix}$$

The quadratic form appearing in the exponent is:

$$Q(x_1, x_2) = (\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) = \frac{1}{1 - \rho^2} \left[ \left(\frac{x_1 - \mu_1}{\sigma_1}\right)^2 - 2\rho \left(\frac{x_1 - \mu_1}{\sigma_1}\right)\left(\frac{x_2 - \mu_2}{\sigma_2}\right) + \left(\frac{x_2 - \mu_2}{\sigma_2}\right)^2 \right]$$

Thus, the joint probability density function of $(X_1, X_2)$ is given for all $(x_1, x_2) \in \mathbb{R}^2$ by:

$$f_{X_1, X_2}(x_1, x_2) = \frac{1}{2\pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \exp\left( -\frac{1}{2(1 - \rho^2)} \left[ \left(\frac{x_1 - \mu_1}{\sigma_1}\right)^2 - 2\rho \left(\frac{x_1 - \mu_1}{\sigma_1}\right)\left(\frac{x_2 - \mu_2}{\sigma_2}\right) + \left(\frac{x_2 - \mu_2}{\sigma_2}\right)^2 \right] \right)$$

### Conditional Distributions and Linear Regression
A celebrated structural property of the bivariate normal distribution is that its conditional distributions are strictly univariate normal. By completing the square in the exponent with respect to $x_2$, the joint density factorizes as $f_{X_1, X_2}(x_1, x_2) = f_{X_1}(x_1) f_{X_2 \mid X_1}(x_2 \mid x_1)$, where the marginal density is $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ and the conditional density is:

$$X_2 \mid X_1 = x_1 \sim \mathcal{N}\left( \mu_2 + \rho \frac{\sigma_2}{\sigma_1}(x_1 - \mu_1), \; \sigma_2^2 (1 - \rho^2) \right)$$

This conditional law reveals two foundational mathematical properties:
1. **Linearity of the Regression Function**: The conditional expectation $\mathbb{E}[X_2 \mid X_1 = x_1] = \mu_2 + \beta (x_1 - \mu_1)$ is a strictly linear function of the conditioning value $x_1$, where the regression slope $\beta = \rho \frac{\sigma_2}{\sigma_1}$ represents the rate of change in $X_2$ per unit change in $X_1$. This provides the rigorous probabilistic justification for linear regression models.
2. **Homoskedasticity**: The conditional variance $\text{Var}(X_2 \mid X_1 = x_1) = \sigma_2^2 (1 - \rho^2)$ is completely constant; it does not depend in any way on the conditioning realization $x_1$. The variance of $X_2$ is reduced from its marginal value $\sigma_2^2$ by the factor $1 - \rho^2$, quantifying the exact proportion of variance explained by knowing $X_1$ ($R^2 = \rho^2$).

### Sampling Distribution of the Sample Correlation Coefficient
In empirical investigations, the population correlation $\rho$ is unknown and must be estimated from a bivariate random sample $(X_{11}, X_{21}), \dots, (X_{1n}, X_{2n})$ via the Pearson sample correlation coefficient:

$$R = \frac{\sum_{i=1}^n (X_{1i} - \bar{X}_1)(X_{2i} - \bar{X}_2)}{\sqrt{\sum_{i=1}^n (X_{1i} - \bar{X}_1)^2 \sum_{i=1}^n (X_{2i} - \bar{X}_2)^2}}$$

When the true population correlation is zero ($\rho = 0$), the exact sampling distribution of $R$ was established by Student (William Sealy Gosset). The transformed statistic:

$$T = \frac{R \sqrt{n - 2}}{\sqrt{1 - R^2}}$$

follows an exact Student's $t$ distribution with $n - 2$ degrees of freedom:

$$T \sim t_{n-2}$$

However, when $\rho \ne 0$, the exact probability density function of $R$ (first derived by R. A. Fisher in 1915) is notoriously complicated, involving Gaussian hypergeometric functions ${}_2F_1$. Furthermore, the distribution of $R$ becomes highly skewed as $|\rho|$ approaches 1, converging to normality very slowly.

To resolve this inferential challenge, Fisher devised the famous **Fisher $z$-transformation**:

$$Z = \frac{1}{2} \ln\left( \frac{1 + R}{1 - R} \right) = \text{arctanh}(R)$$

Fisher proved via Taylor expansion that the transformed statistic $Z$ stabilizes the asymptotic variance and converges rapidly to a Gaussian distribution:

$$Z \sim \mathcal{A}\mathcal{N}\left( \frac{1}{2}\ln\left(\frac{1 + \rho}{1 - \rho}\right) + \frac{\rho}{2(n - 1)}, \; \frac{1}{n - 3} \right)$$

Notice that the asymptotic variance $\frac{1}{n - 3}$ is completely independent of the unknown parameter $\rho$. This variance-stabilizing transformation allows analysts to construct robust, high-accuracy confidence intervals and hypothesis tests for correlation coefficients across arbitrary sample sizes.

## Fully worked question 1: Exact Sampling Distribution of the Sum of Independent Gamma Variates with Unequal Scale Parameters via MGF Inversion

### Question
Let $X_1$ and $X_2$ be two independent random variables following Gamma distributions with integer shape parameters $\alpha_1 = 1$ and $\alpha_2 = 1$ (i.e., independent Exponential random variables), but with distinct rate parameters $\beta_1$ and $\beta_2$, where $\beta_1 \ne \beta_2 > 0$. 
1. Determine the moment generating function of the sum $Y = X_1 + X_2$.
2. Decompose $M_Y(t)$ into partial fractions.
3. Invert the transform analytically to obtain the exact probability density function $f_Y(y)$ for all $y > 0$.
4. Verify by direct integration that $\int_0^\infty f_Y(y) \, dy = 1$ and evaluate the exact expected value $\mathbb{E}[Y]$.

### Solution, step 1: Derivation and Product of Individual MGFs
For an exponential random variable $X_i \sim \text{Exp}(\beta_i) = \text{Gamma}(1, \beta_i)$ with probability density function $f_{X_i}(x) = \beta_i e^{-\beta_i x}$ for $x > 0$, the moment generating function is given for all $t < \beta_i$ by:

$$M_{X_i}(t) = \int_0^\infty e^{tx} \beta_i e^{-\beta_i x} \, dx = \beta_i \int_0^\infty e^{-(\beta_i - t)x} \, dx = \frac{\beta_i}{\beta_i - t} = \left( 1 - \frac{t}{\beta_i} \right)^{-1}$$

Because $X_1$ and $X_2$ are independent random variables, the moment generating function of their sum $Y = X_1 + X_2$ factorizes as the algebraic product of their individual MGFs:

$$M_Y(t) = M_{X_1}(t) \cdot M_{X_2}(t) = \left( \frac{\beta_1}{\beta_1 - t} \right) \left( \frac{\beta_2}{\beta_2 - t} \right) = \frac{\beta_1 \beta_2}{(\beta_1 - t)(\beta_2 - t)}$$

valid on the open domain $t < \min(\beta_1, \beta_2)$.

### Solution, step 2: Partial Fraction Decomposition of the MGF
Because the rate parameters are distinct ($\beta_1 \ne \beta_2$), the denominator polynomial has two distinct real roots at $t = \beta_1$ and $t = \beta_2$. We can decompose the rational function into partial fractions:

$$\frac{\beta_1 \beta_2}{(\beta_1 - t)(\beta_2 - t)} = \frac{A}{\beta_1 - t} + \frac{B}{\beta_2 - t}$$

Multiplying both sides by the common denominator $(\beta_1 - t)(\beta_2 - t)$ yields the identity:

$$\beta_1 \beta_2 = A(\beta_2 - t) + B(\beta_1 - t)$$

To find $A$, evaluate this identity at $t = \beta_1$:

$$\beta_1 \beta_2 = A(\beta_2 - \beta_1) + B(0) \implies A = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1}$$

To find $B$, evaluate the identity at $t = \beta_2$:

$$\beta_1 \beta_2 = A(0) + B(\beta_1 - \beta_2) \implies B = \frac{\beta_1 \beta_2}{\beta_1 - \beta_2} = -\frac{\beta_1 \beta_2}{\beta_2 - \beta_1}$$

We can factor out the common constant and express each term in standard MGF form:

$$M_Y(t) = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1} \left[ \frac{1}{\beta_1 - t} - \frac{1}{\beta_2 - t} \right] = \frac{\beta_2}{\beta_2 - \beta_1} \left( \frac{\beta_1}{\beta_1 - t} \right) + \frac{\beta_1}{\beta_1 - \beta_2} \left( \frac{\beta_2}{\beta_2 - t} \right)$$

Notice that $\frac{\beta_1}{\beta_1 - t}$ is precisely the MGF of an $\text{Exp}(\beta_1)$ distribution, and $\frac{\beta_2}{\beta_2 - t}$ is the MGF of an $\text{Exp}(\beta_2)$ distribution. Thus, $M_Y(t)$ is expressed as a linear combination of exponential MGFs with coefficients:

$$c_1 = \frac{\beta_2}{\beta_2 - \beta_1}, \quad c_2 = \frac{\beta_1}{\beta_1 - \beta_2}$$

Observe that $c_1 + c_2 = \frac{\beta_2 - \beta_1}{\beta_2 - \beta_1} = 1$.

### Solution, step 3: Transform Inversion and Construction of the Probability Density Function
By the uniqueness theorem of the moment generating function, the inverse Laplace-Stieltjes transform operates linearly. Inverting term by term:

$$\mathcal{L}^{-1}\left\{ \frac{\beta_1}{\beta_1 - t} \right\} = \beta_1 e^{-\beta_1 y}, \quad \mathcal{L}^{-1}\left\{ \frac{\beta_2}{\beta_2 - t} \right\} = \beta_2 e^{-\beta_2 y}$$

Consequently, the exact probability density function $f_Y(y)$ for $y > 0$ is:

$$f_Y(y) = c_1 \beta_1 e^{-\beta_1 y} + c_2 \beta_2 e^{-\beta_2 y} = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1} e^{-\beta_1 y} + \frac{\beta_1 \beta_2}{\beta_1 - \beta_2} e^{-\beta_2 y}$$

Factoring out the term $\frac{\beta_1 \beta_2}{\beta_2 - \beta_1}$:

$$f_Y(y) = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1} \left( e^{-\beta_1 y} - e^{-\beta_2 y} \right), \quad y > 0$$

For $y \le 0$, $f_Y(y) = 0$. This distribution is recognized in queueing theory and stochastic processes as the **hypoexponential distribution** of order 2.

### Solution, step 4: Normalization Verification and Moment Computation
To verify normalization, integrate $f_Y(y)$ over the positive half-line:

$$\int_0^\infty f_Y(y) \, dy = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1} \left[ \int_0^\infty e^{-\beta_1 y} \, dy - \int_0^\infty e^{-\beta_2 y} \, dy \right]$$

Evaluating each elementary integral:

$$\int_0^\infty e^{-\beta_1 y} \, dy = \frac{1}{\beta_1}, \quad \int_0^\infty e^{-\beta_2 y} \, dy = \frac{1}{\beta_2}$$

Substituting these values:

$$\int_0^\infty f_Y(y) \, dy = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1} \left( \frac{1}{\beta_1} - \frac{1}{\beta_2} \right) = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1} \left( \frac{\beta_2 - \beta_1}{\beta_1 \beta_2} \right) = 1$$

The density integrates to 1. To compute the expected value $\mathbb{E}[Y]$, we evaluate the first derivative of $M_Y(t)$ at $t = 0$:

$$K_Y(t) = \ln M_Y(t) = \ln \beta_1 - \ln(\beta_1 - t) + \ln \beta_2 - \ln(\beta_2 - t)$$

$$\mathbb{E}[Y] = K_Y'(0) = \left. \left( \frac{1}{\beta_1 - t} + \frac{1}{\beta_2 - t} \right) \right|_{t=0} = \frac{1}{\beta_1} + \frac{1}{\beta_2}$$

This matches the expected value from linearity of expectation: $\mathbb{E}[X_1 + X_2] = \mathbb{E}[X_1] + \mathbb{E}[X_2] = \frac{1}{\beta_1} + \frac{1}{\beta_2}$.

## Fully worked question 2: Joint Distribution and Sample Moment Properties for Non-Gaussian Parent Populations

### Question
Let $X_1, X_2, \dots, X_n$ ($n \ge 3$) be an i.i.d. random sample from a continuous distribution with mean $\mu$, variance $\sigma^2$, third central moment $\mu_3$, and fourth central moment $\mu_4$. 
1. Derive the exact finite-sample variance of the sample variance: $\text{Var}(S^2)$.
2. Prove that the standardized sample variance $\sqrt{n}(S^2 - \sigma^2)$ has asymptotic variance $\mu_4 - \sigma^4$.
3. Under what exact condition on the population kurtosis is $\text{Var}(S^2)$ minimal for a fixed variance $\sigma^2$?

### Solution, step 1: Representation of the Sample Variance via U-Statistics
The sample variance $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ can be rewritten in symmetric pairwise difference form:

$$\sum_{i=1}^n (X_i - \bar{X})^2 = \frac{1}{2n} \sum_{i=1}^n \sum_{j=1}^n (X_i - X_j)^2 = \frac{1}{n} \sum_{1 \le i < j \le n} (X_i - X_j)^2$$

Therefore:

$$S^2 = \frac{1}{\binom{n}{2}} \sum_{1 \le i < j \le n} \frac{1}{2}(X_i - X_j)^2$$

This reveals that $S^2$ is an unbiased $U$-statistic of degree 2 with symmetric kernel:

$$h(X_i, X_j) = \frac{1}{2}(X_i - X_j)^2$$

Without loss of generality, let $\mu = 0$ (since variance and central moments are translation-invariant). Then $\mathbb{E}[X_i] = 0$, $\mathbb{E}[X_i^2] = \sigma^2$, $\mathbb{E}[X_i^3] = \mu_3$, and $\mathbb{E}[X_i^4] = \mu_4$. The expectation of the kernel is:

$$\mathbb{E}[h(X_1, X_2)] = \frac{1}{2}\mathbb{E}[(X_1 - X_2)^2] = \frac{1}{2}\left(\mathbb{E}[X_1^2] - 2\mathbb{E}[X_1]\mathbb{E}[X_2] + \mathbb{E}[X_2^2]\right) = \frac{1}{2}(\sigma^2 - 0 + \sigma^2) = \sigma^2$$

### Solution, step 2: Kernel Variance and Projection Analysis
To compute the exact variance of $S^2$ via $U$-statistic theory, we define the one-variable projection:

$$h_1(x) = \mathbb{E}[h(x, X_2)] = \frac{1}{2}\mathbb{E}[(x - X_2)^2] = \frac{1}{2}\left(x^2 - 2x\mathbb{E}[X_2] + \mathbb{E}[X_2^2]\right) = \frac{1}{2}(x^2 + \sigma^2)$$

The variance of this first-order projection is:

$$\zeta_1 = \text{Var}(h_1(X_1)) = \text{Var}\left(\frac{1}{2}X_1^2 + \frac{1}{2}\sigma^2\right) = \frac{1}{4}\text{Var}(X_1^2) = \frac{1}{4}\left(\mathbb{E}[X_1^4] - (\mathbb{E}[X_1^2])^2\right) = \frac{1}{4}(\mu_4 - \sigma^4)$$

Next, we evaluate the variance of the complete two-variable kernel:

$$\zeta_2 = \text{Var}(h(X_1, X_2)) = \mathbb{E}[h^2(X_1, X_2)] - \sigma^4$$

Compute $\mathbb{E}[h^2(X_1, X_2)]$:

$$h^2(X_1, X_2) = \frac{1}{4}(X_1 - X_2)^4 = \frac{1}{4}\left(X_1^4 - 4X_1^3 X_2 + 6X_1^2 X_2^2 - 4X_1 X_2^3 + X_2^4\right)$$

Taking expectations of independent zero-mean terms:

$$\mathbb{E}[h^2(X_1, X_2)] = \frac{1}{4}\left(\mu_4 - 0 + 6\sigma^2 \sigma^2 - 0 + \mu_4\right) = \frac{1}{4}(2\mu_4 + 6\sigma^4) = \frac{1}{2}\mu_4 + \frac{3}{2}\sigma^4$$

Subtracting $\sigma^4$:

$$\zeta_2 = \left(\frac{1}{2}\mu_4 + \frac{3}{2}\sigma^4\right) - \sigma^4 = \frac{1}{2}(\mu_4 + \sigma^4)$$

### Solution, step 3: Exact Finite-Sample Variance of $S^2$
By the classical Hoeffding formula for the variance of a $U$-statistic of degree 2:

$$\text{Var}(S^2) = \frac{1}{\binom{n}{2}} \sum_{c=1}^2 \binom{2}{c}\binom{n-2}{2-c}\zeta_c = \frac{4(n-2)}{n(n-1)}\zeta_1 + \frac{2}{n(n-1)}\zeta_2$$

Substitute $\zeta_1 = \frac{1}{4}(\mu_4 - \sigma^4)$ and $\zeta_2 = \frac{1}{2}(\mu_4 + \sigma^4)$:

$$\text{Var}(S^2) = \frac{4(n-2)}{n(n-1)}\left[\frac{1}{4}(\mu_4 - \sigma^4)\right] + \frac{2}{n(n-1)}\left[\frac{1}{2}(\mu_4 + \sigma^4)\right]$$

Simplify the algebraic expression:

$$\text{Var}(S^2) = \frac{(n-2)(\mu_4 - \sigma^4) + (\mu_4 + \sigma^4)}{n(n-1)} = \frac{(n-1)\mu_4 - (n-3)\sigma^4}{n(n-1)}$$

Equivalently, writing in terms of $n$:

$$\text{Var}(S^2) = \frac{1}{n}\left( \mu_4 - \frac{n-3}{n-1}\sigma^4 \right)$$

This is the exact finite-sample variance of $S^2$ for any distribution with finite fourth moments.

### Solution, step 4: Asymptotic Variance and Kurtosis Bounds
Multiplying by $n$ and taking the limit as $n \to \infty$:

$$\lim_{n \to \infty} n \text{Var}(S^2) = \lim_{n \to \infty} \left( \mu_4 - \frac{n-3}{n-1}\sigma^4 \right) = \mu_4 - \sigma^4$$

Hence, the asymptotic variance of $\sqrt{n}(S^2 - \sigma^2)$ is:

$$\text{AsyVar}\left(\sqrt{n}(S^2 - \sigma^2)\right) = \mu_4 - \sigma^4$$

For a normal distribution, $\mu_4 = 3\sigma^4$. Substituting this yields the familiar Gaussian variance:

$$\text{Var}_{\text{normal}}(S^2) = \frac{1}{n}\left(3\sigma^4 - \frac{n-3}{n-1}\sigma^4\right) = \frac{1}{n}\sigma^4\left(\frac{3(n-1) - (n-3)}{n-1}\right) = \frac{2\sigma^4}{n-1}$$

Now, recall the fundamental moment inequality: for any random variable $X$, Jensen's inequality implies $\mathbb{E}[(X - \mu)^4] \ge (\mathbb{E}[(X - \mu)^2])^2$, meaning:

$$\mu_4 \ge \sigma^4$$

with equality if and only if $(X - \mu)^2$ is constant almost surely (a two-point symmetric distribution $P(X = \mu \pm \sigma) = 1/2$, such as a Rademacher distribution). In that minimal case, $\mu_4 = \sigma^4$, so the excess kurtosis is $\gamma_2 = \frac{\mu_4}{\sigma^4} - 3 = -2$. For such distributions:

$$\text{Var}(S^2) = \frac{1}{n}\left(\sigma^4 - \frac{n-3}{n-1}\sigma^4\right) = \frac{2\sigma^4}{n(n-1)}$$

which achieves the absolute theoretical lower bound for the variance of the sample variance.

## Fully worked question 3: Convolution Integral Derivation for the Ratio and Product of Independent Cauchy and Uniform Random Variables

### Question
Let $X$ and $Y$ be two independent continuous random variables. $X$ follows a standard Cauchy distribution with probability density function:

$$f_X(x) = \frac{1}{\pi(1 + x^2)}, \quad x \in \mathbb{R}$$

and $Y$ follows a standard Uniform distribution on the interval $(0, 1)$ with probability density function:

$$f_Y(y) = 1, \quad 0 < y < 1$$

1. Set up the bivariate transformation to find the probability density function of the product $W = X Y$.
2. Formulate the exact convolution integral and determine the integration bounds.
3. Evaluate the integral analytically to find the closed-form density $f_W(w)$ for all $w \in \mathbb{R}$.
4. Show that $W$ possesses heavy tails and examine its asymptotic decay rate as $|w| \to \infty$.

### Solution, step 1: Bivariate Transformation Setup
We wish to determine the probability density function of $W = X Y$. To apply the Jacobian method, define an auxiliary random variable $V = Y$. The forward transformation is:

$$W = X Y, \quad V = Y$$

Since $Y \in (0, 1)$ and $X \in \mathbb{R}$, the image space is $\mathcal{T} = \{(w, v) \in \mathbb{R}^2 : w \in \mathbb{R}, 0 < v < 1\}$. The inverse transformation is uniquely given by:

$$X = \frac{W}{V}, \quad Y = V$$

The Jacobian matrix of the inverse mapping is:

$$J = \begin{pmatrix} \frac{\partial x}{\partial w} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial w} & \frac{\partial y}{\partial v} \end{pmatrix} = \begin{pmatrix} \frac{1}{v} & -\frac{w}{v^2} \\ 0 & 1 \end{pmatrix}$$

The determinant of the Jacobian is:

$$\det(J) = \left(\frac{1}{v}\right)(1) - \left(-\frac{w}{v^2}\right)(0) = \frac{1}{v}$$

Since $v \in (0, 1)$, $|\det(J)| = \frac{1}{v}$.

### Solution, step 2: Formulation of the Joint and Marginal Densities
Because $X$ and $Y$ are independent, their joint density is:

$$f_{X, Y}(x, y) = f_X(x) f_Y(y) = \frac{1}{\pi(1 + x^2)} \cdot \mathbf{1}_{(0, 1)}(y)$$

Applying the change of variables formula, the joint density of $(W, V)$ on $\mathcal{T}$ is:

$$f_{W, V}(w, v) = f_X\left(\frac{w}{v}\right) f_Y(v) |\det(J)| = \frac{1}{\pi\left(1 + \frac{w^2}{v^2}\right)} \cdot 1 \cdot \frac{1}{v}$$

Simplify the algebraic expression:

$$f_{W, V}(w, v) = \frac{1}{\pi \frac{v^2 + w^2}{v^2}} \cdot \frac{1}{v} = \frac{v}{\pi(v^2 + w^2)}, \quad w \in \mathbb{R}, \; 0 < v < 1$$

To find the marginal density $f_W(w)$, integrate out the auxiliary variable $v$ across its support $(0, 1)$:

$$f_W(w) = \int_0^1 \frac{v}{\pi(v^2 + w^2)} \, dv$$

### Solution, step 3: Analytical Evaluation of the Integral
The integrand has the form $\frac{v}{v^2 + w^2}$. For any fixed $w \ne 0$, make the substitution $u = v^2 + w^2$, so that $du = 2v \, dv$, or $v \, dv = \frac{1}{2} du$. When $v = 0$, $u = w^2$; when $v = 1$, $u = 1 + w^2$. The integral becomes:

$$f_W(w) = \frac{1}{\pi} \int_{w^2}^{1 + w^2} \frac{1}{2u} \, du = \frac{1}{2\pi} \left[ \ln u \right]_{w^2}^{1 + w^2} = \frac{1}{2\pi} \left[ \ln(1 + w^2) - \ln(w^2) \right]$$

Using logarithmic properties:

$$f_W(w) = \frac{1}{2\pi} \ln\left( \frac{1 + w^2}{w^2} \right) = \frac{1}{2\pi} \ln\left( 1 + \frac{1}{w^2} \right), \quad w \ne 0$$

Now, consider the behavior at $w = 0$. As $w \to 0$:

$$\lim_{w \to 0} f_W(w) = \lim_{w \to 0} \frac{1}{2\pi} \ln\left( 1 + \frac{1}{w^2} \right) = +\infty$$

The density possesses a logarithmic singularity at the origin $w = 0$. However, this singularity is integrable:

$$\int_{-1}^1 \ln\left(1 + \frac{1}{w^2}\right) dw < \infty$$

Thus, the exact closed-form probability density function of $W$ is:

$$f_W(w) = \frac{1}{2\pi} \ln\left( 1 + \frac{1}{w^2} \right) \quad \text{for all } w \in \mathbb{R} \setminus \{0\}$$

### Solution, step 4: Verification of Integrability and Asymptotic Tail Behavior
To verify that $f_W(w)$ integrates to 1 over $\mathbb{R}$, exploit the symmetry $f_W(-w) = f_W(w)$:

$$\int_{-\infty}^\infty f_W(w) \, dw = 2 \int_0^\infty \frac{1}{2\pi} \ln\left(1 + \frac{1}{w^2}\right) dw = \frac{1}{\pi} \int_0^\infty \ln\left(\frac{w^2 + 1}{w^2}\right) dw$$

Use integration by parts: let $u = \ln(w^2 + 1) - \ln(w^2)$ and $dv = dw$, so $v = w$. The derivative is:

$$u' = \frac{2w}{w^2 + 1} - \frac{2}{w} = \frac{2w^2 - 2(w^2 + 1)}{w(w^2 + 1)} = -\frac{2}{w(w^2 + 1)}$$

Applying integration by parts:

$$\int_0^\infty u \, dw = \left[ w \ln\left(1 + \frac{1}{w^2}\right) \right]_0^\infty - \int_0^\infty w \left( -\frac{2}{w(w^2 + 1)} \right) dw$$

For the boundary term:
- As $w \to \infty$, $w \ln(1 + 1/w^2) \sim w(1/w^2) = 1/w \to 0$.
- As $w \to 0^+$, let $y = 1/w \to \infty$; then $\frac{1}{y} \ln(1 + y^2) \to 0$.
Thus, the boundary term vanishes completely at both limits. The remaining integral is:

$$\int_0^\infty \frac{2}{w^2 + 1} \, dw = 2 \left[ \arctan(w) \right]_0^\infty = 2 \left( \frac{\pi}{2} - 0 \right) = \pi$$

Multiplying by the pre-factor $1/\pi$:

$$\int_{-\infty}^\infty f_W(w) \, dw = \frac{1}{\pi} \cdot \pi = 1$$

To analyze the tail decay as $|w| \to \infty$, use the Taylor expansion $\ln(1 + z) = z - \frac{z^2}{2} + \mathcal{O}(z^3)$ with $z = 1/w^2$:

$$f_W(w) = \frac{1}{2\pi} \left( \frac{1}{w^2} - \frac{1}{2w^4} + \mathcal{O}\left(\frac{1}{w^6}\right) \right) \sim \frac{1}{2\pi w^2} \quad \text{as } |w| \to \infty$$

Comparing this to the standard Cauchy density $f_X(x) \sim \frac{1}{\pi x^2}$, we observe that multiplying the Cauchy variable by an independent $\text{Uniform}(0, 1)$ variable preserves the exact same inverse-square heavy tail decay $\mathcal{O}(|w|^{-2})$, with the asymptotic tail constant halved from $1/\pi$ to $1/(2\pi)$. Consequently, like the parent Cauchy distribution, $W$ has an undefined expectation and infinite variance.
"""

DEST.write_text(content.strip() + "\n", encoding="utf-8")
print(f"Unit 2 authored successfully at {DEST} ({len(content)} chars)")
