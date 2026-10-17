#!/usr/bin/env python3
"""
Author Unit 4 for Mathematical Statistics.
Focuses on Order Statistics, Joint Densities, Extremes, Spacings, and Sample Quantiles.
Generates >= 5,300 substantive prose words with zero KaTeX errors.
"""
from pathlib import Path

DEST = Path("publishing/drafts/statistics-probability-mathematical-statistics/unit-4.md")

content = r"""# Unit 4: Order Statistics, Joint Densities, Extremes, Spacings, and Sample Quantiles

## 4.1 Foundations of Order Statistics and Permutation Symmetries

In classical sampling theory, an observed sample vector $\mathbf{X} = (X_1, X_2, \dots, X_n)$ records observations in the chronological or sequential order in which they were collected. In many inferential contexts, however, the temporal indexing of the data points contains zero physical relevance. Instead, the structural information is organized by sorting the observations in ascending numerical order of magnitude.

Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed (i.i.d.) random sample from a continuous cumulative distribution function $F(x) = P(X \le x)$ with probability density function $f(x) = F'(x)$. Arranging the sample realizations in strictly non-decreasing order:

$$X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$$

defines the collection of **order statistics**. Specifically:
- $X_{(1)} = \min(X_1, X_2, \dots, X_n)$ is the **first order statistic** (the sample minimum).
- $X_{(n)} = \max(X_1, X_2, \dots, X_n)$ is the **$n$-th order statistic** (the sample maximum).
- For any integer $k \in \{1, 2, \dots, n\}$, $X_{(k)}$ is the **$k$-th order statistic**, representing the value that exceeds exactly $k - 1$ other sample values and is exceeded by the remaining $n - k$ observations.

Because the underlying distribution function $F(x)$ is continuous, the probability of any two coordinates coinciding vanishes identically: $P(X_i = X_j) = 0$ for all $i \ne j$. Consequently, with probability 1, the order statistics form a strictly ascending chain of inequalities:

$$P\left( X_{(1)} < X_{(2)} < \dots < X_{(n)} \right) = 1$$

Ties occur with probability zero, allowing us to treat the sorted values as strictly distinct real numbers.

### Permutation Symmetry and the Invariance Principle
To understand the probabilistic structure of order statistics, consider the sample space $\mathbb{R}^n$. The set of points where coordinates are pairwise distinct, $\mathbb{R}^n \setminus \bigcup_{i < j} \{\mathbf{x} : x_i = x_j\}$, is partitioned into $n!$ mutually disjoint open cones (wedges), each corresponding to one specific permutation $\pi$ of the indices $\{1, 2, \dots, n\}$ such that $x_{\pi(1)} < x_{\pi(2)} < \dots < x_{\pi(n)}$.

Because the original random variables $X_1, \dots, X_n$ are independent and identically distributed, their joint probability density function is completely symmetric under all coordinate permutations:

$$f_{\mathbf{X}}(x_1, \dots, x_n) = \prod_{i=1}^n f(x_i) = \prod_{i=1}^n f(x_{\pi(i)}) = f_{\mathbf{X}}(x_{\pi(1)}, \dots, x_{\pi(n)})$$

By this permutation symmetry, the probability measure of each of the $n!$ cones is identical, equal to $1/n!$.
The transformation from the unordered sample vector $\mathbf{X} = (X_1, \dots, X_n)$ to the sorted vector of order statistics $\mathbf{X}_{(\cdot)} = (X_{(1)}, \dots, X_{(n)})$ is an $n!$-to-1 mapping: every point in the sorted cone $\mathcal{T} = \{\mathbf{y} \in \mathbb{R}^n : y_1 < y_2 < \dots < y_n\}$ has exactly $n!$ pre-images under the sorting operation, one in each permutation wedge.
Because the Jacobian determinant of every coordinate permutation matrix is $\pm 1$ (with absolute value $|\det(\mathbf{P}_\pi)| = 1$), the multivariable change of variables theorem implies that the **joint probability density function of all $n$ order statistics** on the cone $\mathcal{T}$ is given by summing over all $n!$ permutations:

$$f_{X_{(1)}, X_{(2)}, \dots, X_{(n)}}(y_1, y_2, \dots, y_n) = n! \prod_{i=1}^n f(y_i) \quad \text{for } -\infty < y_1 < y_2 < \dots < y_n < \infty$$

and zero elsewhere. This joint density encapsulates all distribution theory for order statistics.

## 4.2 Marginal Distribution of the $k$-th Order Statistic

We now derive the marginal cumulative distribution function and probability density function of the $k$-th order statistic $X_{(k)}$ for an arbitrary continuous distribution $F(x)$.

### Cumulative Distribution Function via the Binomial Argument
Consider the event $\{X_{(k)} \le x\}$ for some fixed real threshold $x \in \mathbb{R}$. The $k$-th smallest observation is less than or equal to $x$ if and only if **at least $k$ of the $n$ observations** fall in the interval $(-\infty, x]$.

Let $Y = \sum_{i=1}^n \mathbf{1}_{(-\infty, x]}(X_i)$ denote the random number of sample observations that satisfy $X_i \le x$. Because $X_1, \dots, X_n$ are independent Bernoulli trials with success probability $p = P(X_i \le x) = F(x)$, the count $Y$ follows an exact Binomial distribution:

$$Y \sim \text{Binomial}(n, F(x))$$

Therefore, the event $\{X_{(k)} \le x\}$ is identical to the event $\{Y \ge k\}$:

$$F_{X_{(k)}}(x) = P(X_{(k)} \le x) = P(Y \ge k) = \sum_{j=k}^n \binom{n}{j} [F(x)]^j [1 - F(x)]^{n - j}$$

This formula expresses the CDF of the $k$-th order statistic as an exact finite sum of binomial probabilities.

### Probability Density Function Derivation
To obtain the probability density function $f_{X_{(k)}}(x)$, we differentiate $F_{X_{(k)}}(x)$ with respect to $x$ using the product and chain rules:

$$f_{X_{(k)}}(x) = \frac{d}{dx} \sum_{j=k}^n \binom{n}{j} [F(x)]^j [1 - F(x)]^{n - j}$$

Evaluating the derivative term by term produces a telescoping sum where adjacent terms cancel. Alternatively, we can deploy an intuitive infinitesimal combinatorial argument.
Consider the probability that $X_{(k)}$ falls in an infinitesimal interval $[x, x + dx]$:
1. Exactly one observation must fall within $[x, x + dx]$; the probability of this is $f(x) \, dx$.
2. Exactly $k - 1$ observations must fall strictly to the left of $x$, in $(-\infty, x)$; the probability of this configuration for a specific subset is $[F(x)]^{k - 1}$.
3. The remaining $n - k$ observations must fall strictly to the right of $x + dx$, in $(x, \infty)$; the probability of this configuration is $[1 - F(x)]^{n - k}$.
4. The number of ways to partition $n$ distinct observations into these three categories (left, inside, right) is given by the multinomial coefficient:
   $$\frac{n!}{(k - 1)! \, 1! \, (n - k)!}$$

Multiplying these independent components yields the exact marginal probability density function of $X_{(k)}$:

$$f_{X_{(k)}}(x) = \frac{n!}{(k - 1)! (n - k)!} [F(x)]^{k - 1} [1 - F(x)]^{n - k} f(x), \quad -\infty < x < \infty$$

This formula can also be written in terms of the Beta function $B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)} = \frac{(a - 1)!(b - 1)!}{(a + b - 1)!}$:

$$f_{X_{(k)}}(x) = \frac{1}{B(k, n - k + 1)} [F(x)]^{k - 1} [1 - F(x)]^{n - k} f(x)$$

### Special Cases: Extremes
Setting $k = 1$ yields the probability density function of the **sample minimum** $X_{(1)}$:

$$f_{X_{(1)}}(x) = n [1 - F(x)]^{n - 1} f(x)$$

with survival function:

$$P(X_{(1)} > x) = P(X_1 > x, \dots, X_n > x) = \prod_{i=1}^n P(X_i > x) = [1 - F(x)]^n$$

Setting $k = n$ yields the probability density function of the **sample maximum** $X_{(n)}$:

$$f_{X_{(n)}}(x) = n [F(x)]^{n - 1} f(x)$$

with cumulative distribution function:

$$F_{X_{(n)}}(x) = P(X_{(n)} \le x) = P(X_1 \le x, \dots, X_n \le x) = [F(x)]^n$$

## 4.3 Joint Probability Density Function of Two Order Statistics

In many statistical problems, one needs to analyze pairs of order statistics simultaneously (for instance, the minimum and maximum to study the sample range, or adjacent order statistics to study spacings).

Let $1 \le j < k \le n$. We seek the joint probability density function of $(X_{(j)}, X_{(k)})$ for arguments $u < v$.
Using the infinitesimal multinomial method, consider the joint probability that $X_{(j)} \in [u, u + du]$ and $X_{(k)} \in [v, v + dv]$ with $u < v$:
1. Exactly $j - 1$ observations fall in $(-\infty, u)$, each with probability $F(u)$.
2. Exactly one observation falls in $[u, u + du]$, with probability $f(u) \, du$.
3. Exactly $k - 1 - j$ observations fall in $(u, v)$, each with probability $F(v) - F(u)$.
4. Exactly one observation falls in $[v, v + dv]$, with probability $f(v) \, dv$.
5. The remaining $n - k$ observations fall in $(v, \infty)$, each with probability $1 - F(v)$.

The number of ways to assign $n$ distinct observations to these five disjoint intervals is given by the multinomial coefficient:

$$\frac{n!}{(j - 1)! \, 1! \, (k - 1 - j)! \, 1! \, (n - k)!}$$

Multiplying the multinomial coefficient by the probabilities of the respective configurations yields the exact **joint probability density function of $X_{(j)}$ and $X_{(k)}$**:

$$f_{X_{(j)}, X_{(k)}}(u, v) = \frac{n!}{(j - 1)! (k - 1 - j)! (n - k)!} [F(u)]^{j - 1} [F(v) - F(u)]^{k - 1 - j} [1 - F(v)]^{n - k} f(u) f(v)$$

valid for all $-\infty < u < v < \infty$, and zero whenever $u \ge v$.

### Joint Density of the Sample Minimum and Sample Maximum
Setting $j = 1$ and $k = n$ specializes the formula to the joint density of the extremes $(X_{(1)}, X_{(n)})$:

$$f_{X_{(1)}, X_{(n)}}(u, v) = n(n - 1) [F(v) - F(u)]^{n - 2} f(u) f(v), \quad -\infty < u < v < \infty$$

Notice that $X_{(1)}$ and $X_{(n)}$ are **never stochastically independent**: the term $[F(v) - F(u)]^{n - 2}$ couples $u$ and $v$ non-linearly, and the triangular support domain $u < v$ prevents any factorized independence.

## 4.4 The Sample Range and Midrange: Exact Distribution Theory

From the joint distribution of the extremes $(X_{(1)}, X_{(n)})$, two fundamental summary statistics of dispersion and location are constructed:
1. The **sample range**: $R = X_{(n)} - X_{(1)}$, which measures the total span or dispersion of the sample.
2. The **sample midrange**: $M = \frac{X_{(1)} + X_{(n)}}{2}$, which provides an alternative measure of central tendency based entirely on the sample extremes.

To find the joint and marginal distributions of $R$ and $M$, define the bivariate transformation:

$$R = X_{(n)} - X_{(1)}, \quad M = \frac{X_{(1)} + X_{(n)}}{2}$$

The inverse transformation is:

$$X_{(1)} = M - \frac{R}{2}, \quad X_{(n)} = M + \frac{R}{2}$$

The Jacobian matrix of the inverse mapping is:

$$J = \begin{pmatrix} \frac{\partial x_{(1)}}{\partial r} & \frac{\partial x_{(1)}}{\partial m} \\ \frac{\partial x_{(n)}}{\partial r} & \frac{\partial x_{(n)}}{\partial m} \end{pmatrix} = \begin{pmatrix} -1/2 & 1 \\ 1/2 & 1 \end{pmatrix}$$

The Jacobian determinant is:

$$\det(J) = (-1/2)(1) - (1/2)(1) = -1 \implies |\det(J)| = 1$$

Therefore, the joint probability density function of $(R, M)$ is:

$$f_{R, M}(r, m) = f_{X_{(1)}, X_{(n)}}\left( m - \frac{r}{2}, \; m + \frac{r}{2} \right) \cdot 1$$

Substituting the joint density of the extremes:

$$f_{R, M}(r, m) = n(n - 1) \left[ F\left(m + \frac{r}{2}\right) - F\left(m - \frac{r}{2}\right) \right]^{n - 2} f\left(m - \frac{r}{2}\right) f\left(m + \frac{r}{2}\right)$$

for $r > 0$ and $m \in \mathbb{R}$ such that $m - r/2 < m + r/2$ falls within the support of the distribution.

To obtain the marginal probability density function of the sample range $R$, integrate out the midrange $m$:

$$f_R(r) = n(n - 1) \int_{-\infty}^\infty \left[ F\left(m + \frac{r}{2}\right) - F\left(m - \frac{r}{2}\right) \right]^{n - 2} f\left(m - \frac{r}{2}\right) f\left(m + \frac{r}{2}\right) \, dm, \quad r > 0$$

Equivalently, performing the change of variable $u = m - r/2$ (so $m + r/2 = u + r$ and $dm = du$):

$$f_R(r) = n(n - 1) \int_{-\infty}^\infty [F(u + r) - F(u)]^{n - 2} f(u) f(u + r) \, du, \quad r > 0$$

This integral formula provides the exact probability density function of the sample range for any continuous parent distribution.

## 4.5 Uniform Order Statistics: Connections to Beta and Dirichlet Distributions

The distribution theory of order statistics simplifies remarkably when sampling from the standard uniform distribution $\text{Uniform}(0, 1)$, where $F(u) = u$ and $f(u) = 1$ on $(0, 1)$. By the Probability Integral Transform ($U = F(X)$), results for uniform order statistics translate directly to any continuous distribution.

Let $U_1, U_2, \dots, U_n \sim \text{Uniform}(0, 1)$ be an i.i.d. sample, and let $U_{(1)} < U_{(2)} < \dots < U_{(n)}$ denote their order statistics.

### Marginal Distribution as a Beta Law
Substituting $F(u) = u$ and $f(u) = 1$ into the marginal density formula for the $k$-th order statistic:

$$f_{U_{(k)}}(u) = \frac{n!}{(k - 1)! (n - k)!} u^{k - 1} (1 - u)^{n - k}, \quad 0 < u < 1$$

This is precisely the probability density function of a **Beta distribution** with parameters $\alpha = k$ and $\beta = n - k + 1$:

$$U_{(k)} \sim \text{Beta}(k, \; n - k + 1)$$

From the standard properties of the Beta distribution, the moments of $U_{(k)}$ can be evaluated in closed form:
1. **Expected Value**:
   $$\mathbb{E}[U_{(k)}] = \frac{\alpha}{\alpha + \beta} = \frac{k}{k + (n - k + 1)} = \frac{k}{n + 1}$$
   Notice that the expected values of the uniform order statistics divide the unit interval $[0, 1]$ into $n + 1$ segments of equal expected length $\frac{1}{n + 1}$:
   $$\mathbb{E}[U_{(1)}] = \frac{1}{n + 1}, \quad \mathbb{E}[U_{(2)}] = \frac{2}{n + 1}, \quad \dots, \quad \mathbb{E}[U_{(n)}] = \frac{n}{n + 1}$$
2. **Variance**:
   $$\text{Var}(U_{(k)}) = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)} = \frac{k(n - k + 1)}{(n + 1)^2 (n + 2)}$$
3. **Covariance**: For $1 \le j < k \le n$, the covariance between two uniform order statistics is:
   $$\text{Cov}(U_{(j)}, U_{(k)}) = \frac{j(n - k + 1)}{(n + 1)^2 (n + 2)}$$

### Joint Distribution of Uniform Spacings as a Dirichlet Law
Define the **sample spacings** of the uniform order statistics:

$$D_1 = U_{(1)}, \quad D_2 = U_{(2)} - U_{(1)}, \quad \dots, \quad D_k = U_{(k)} - U_{(k - 1)}, \quad \dots, \quad D_{n + 1} = 1 - U_{(n)}$$

The spacings $D_1, D_2, \dots, D_{n + 1}$ represent the lengths of the $n + 1$ sub-intervals created by placing $n$ random points on the unit interval $[0, 1]$. By construction, these spacings are non-negative and sum identically to 1:

$$\sum_{i=1}^{n + 1} D_i = U_{(1)} + (U_{(2)} - U_{(1)}) + \dots + (1 - U_{(n)}) = 1$$

The joint distribution of the first $n$ spacings $(D_1, \dots, D_n)$ is uniform over the standard $n$-dimensional simplex:

$$\Delta_n = \left\{ (d_1, \dots, d_n) \in \mathbb{R}^n : d_i > 0, \; \sum_{i=1}^n d_i < 1 \right\}$$

with constant joint density:

$$f_{D_1, \dots, D_n}(d_1, \dots, d_n) = n!$$

Consequently, the complete vector of $n + 1$ spacings follows a **symmetric Dirichlet distribution**:

$$(D_1, D_2, \dots, D_{n + 1}) \sim \text{Dirichlet}(1, 1, \dots, 1)$$

By the symmetry of the Dirichlet distribution, the spacings $D_1, D_2, \dots, D_{n + 1}$ are **exchangeable random variables**. Each individual spacing $D_i$ has the exact same marginal distribution:

$$D_i \sim \text{Beta}(1, n)$$

with expected value $\mathbb{E}[D_i] = \frac{1}{n + 1}$ and variance $\text{Var}(D_i) = \frac{n}{(n + 1)^2 (n + 2)}$.

## 4.6 Exponential Spacings and Sukhatme's Transformation

While uniform spacings are constrained to sum to 1, spacings from an **Exponential distribution** exhibit a miraculous property: they are completely mutually independent!

Let $X_1, X_2, \dots, X_n \sim \text{Exp}(\lambda)$ be an i.i.d. sample from an exponential distribution with rate parameter $\lambda > 0$, having density $f(x) = \lambda e^{-\lambda x}$ for $x > 0$. Let $X_{(1)} < X_{(2)} < \dots < X_{(n)}$ denote the order statistics.

Define the raw spacings between consecutive order statistics (setting $X_{(0)} = 0$):

$$W_1 = X_{(1)} - X_{(0)} = X_{(1)}$$

$$W_2 = X_{(2)} - X_{(1)}$$

$$W_k = X_{(k)} - X_{(k - 1)} \quad \text{for } k = 1, 2, \dots, n$$

### Sukhatme's Transformation and Memoryless Invariance
By the memoryless property of the Exponential distribution ($P(X > t + s \mid X > s) = P(X > t)$):
- The sample minimum $X_{(1)} = \min(X_1, \dots, X_n)$ is the minimum of $n$ independent $\text{Exp}(\lambda)$ variables, which is distributed as an exponential variable with rate $n\lambda$:
  $$W_1 = X_{(1)} \sim \text{Exp}(n\lambda)$$
- At time $X_{(1)}$, one item has failed. By memorylessness, the remaining $n - 1$ items each have an independent, fresh $\text{Exp}(\lambda)$ remaining lifetime. The additional time until the next failure, $W_2 = X_{(2)} - X_{(1)}$, is the minimum of $n - 1$ independent $\text{Exp}(\lambda)$ variables:
  $$W_2 \sim \text{Exp}((n - 1)\lambda)$$
- Inductively, at time $X_{(k - 1)}$, $n - k + 1$ items remain alive, so the waiting time until the $k$-th failure is:
  $$W_k = X_{(k)} - X_{(k - 1)} \sim \text{Exp}((n - k + 1)\lambda)$$

Crucially, because the Exponential distribution is memoryless, these consecutive waiting times are **mutually stochastically independent**!

Now define the **normalized spacings**:

$$Z_k = (n - k + 1) W_k = (n - k + 1) (X_{(k)} - X_{(k - 1)}) \quad \text{for } k = 1, 2, \dots, n$$

Because scaling an $\text{Exp}((n - k + 1)\lambda)$ random variable by $(n - k + 1)$ scales its rate parameter by $1 / (n - k + 1)$, each normalized spacing $Z_k$ follows a standard exponential distribution with rate $\lambda$:

$$Z_k \sim \text{Exp}(\lambda) \quad \text{for each } k \in \{1, 2, \dots, n\}$$

Furthermore, the normalized spacings $Z_1, Z_2, \dots, Z_n$ are **mutually independent and identically distributed**!

### Representation of Order Statistics as Partial Sums
Inverting Sukhatme's transformation allows any order statistic $X_{(k)}$ to be expressed as a linear combination of independent exponential variates:

$$X_{(k)} = \sum_{j=1}^k W_j = \sum_{j=1}^k \frac{Z_j}{n - j + 1}$$

This representation simplifies moment computations:
1. **Expected Value**:
   $$\mathbb{E}[X_{(k)}] = \sum_{j=1}^k \frac{\mathbb{E}[Z_j]}{n - j + 1} = \frac{1}{\lambda} \sum_{j=1}^k \frac{1}{n - j + 1}$$
2. **Variance**: By mutual independence of the $Z_j$:
   $$\text{Var}(X_{(k)}) = \sum_{j=1}^k \frac{\text{Var}(Z_j)}{(n - j + 1)^2} = \frac{1}{\lambda^2} \sum_{j=1}^k \frac{1}{(n - j + 1)^2}$$
3. **Covariance**: For $j < k$, since $X_{(k)} = X_{(j)} + \sum_{m=j+1}^k W_m$ where the sum is independent of $X_{(j)}$:
   $$\text{Cov}(X_{(j)}, X_{(k)}) = \text{Var}(X_{(j)}) = \frac{1}{\lambda^2} \sum_{m=1}^j \frac{1}{(n - m + 1)^2}$$

Sukhatme's transformation demonstrates that order statistics from an exponential population behave exactly like the jump times of a pure birth-death Markov process.

## 4.7 Limiting Distributions of Sample Extremes and the Fisher-Tippett-Gnedenko Theorem

In engineering reliability, climatology, hydrology, and financial risk management, interest focuses on the behavior of extreme events—the maximum flood level, the maximum wind speed, or the largest financial loss over a given epoch. This motivates the study of the asymptotic distribution of the sample maximum $X_{(n)}$ as the sample size $n \to \infty$.

Just as the Central Limit Theorem establishes that sums of random variables converge to a Gaussian limit under broad conditions, **Extreme Value Theory (EVT)** establishes that the sample maximum, when appropriately centered and scaled, can converge to only one of three possible non-degenerate limiting distribution types.

### The Fisher-Tippett-Gnedenko Theorem
Let $X_1, X_2, \dots, X_n$ be an i.i.d. sequence from cumulative distribution function $F(x)$, and let $M_n = X_{(n)} = \max(X_1, \dots, X_n)$. Suppose there exist sequences of real normalizing constants $a_n > 0$ and $b_n \in \mathbb{R}$ such that the normalized maximum:

$$\frac{M_n - b_n}{a_n} \xrightarrow{d} G$$

converges in distribution to a non-degenerate distribution function $G(z)$.

**Theorem (Fisher-Tippett-Gnedenko Theorem, 1928, 1943)**: The limiting cumulative distribution function $G(z)$ must belong to one of the following three parametric families (the three extreme value types):

1. **Type I: Gumbel Distribution (Light Tails)**:
   $$G_I(z) = \exp\left( -e^{-z} \right), \quad -\infty < z < \infty$$
   The Gumbel domain of attraction encompasses distributions whose tails decay exponentially fast, including the Gaussian, Exponential, Gamma, Lognormal, and Logistic distributions.
2. **Type II: Fréchet Distribution (Heavy, Power-Law Tails)**:
   $$G_{II}(z) = \begin{cases} 0 & z \le 0 \\ \exp\left( -z^{-\alpha} \right) & z > 0 \end{cases} \quad \text{for some } \alpha > 0$$
   The Fréchet domain of attraction encompasses heavy-tailed distributions with polynomial tail decay $1 - F(x) \sim x^{-\alpha}$, including the Pareto, Student's $t$, and Cauchy distributions.
3. **Type III: Weibull Distribution (Bounded Support Tails)**:
   $$G_{III}(z) = \begin{cases} \exp\left( -(-z)^\alpha \right) & z \le 0 \\ 1 & z > 0 \end{cases} \quad \text{for some } \alpha > 0$$
   The Weibull domain of attraction encompasses distributions with a finite right endpoint $\omega(F) < \infty$, including the Uniform and Beta distributions.

### The Generalized Extreme Value (GEV) Distribution
In 1955, C. B. Jenkinson unified these three distinct limiting families into a single, continuous, one-parameter formulation known as the **Generalized Extreme Value (GEV) distribution**:

$$G(z; \mu, \sigma, \xi) = \exp\left( -\left[ 1 + \xi \left( \frac{z - \mu}{\sigma} \right) \right]^{-1/\xi} \right)$$

defined on the support $\{z : 1 + \xi(z - \mu)/\sigma > 0\}$, where $\mu \in \mathbb{R}$ is the location parameter, $\sigma > 0$ is the scale parameter, and $\xi \in \mathbb{R}$ is the **shape parameter (extreme value index)**:
- $\xi = 0$ corresponds to the Gumbel distribution (taking the limit as $\xi \to 0$ recovers $\exp(-e^{-(z - \mu)/\sigma})$).
- $\xi > 0$ corresponds to the heavy-tailed Fréchet distribution (with tail index $\alpha = 1/\xi$).
- $\xi < 0$ corresponds to the bounded-support Weibull distribution.

This unified formulation allows practitioners to estimate the shape parameter $\xi$ directly from data, enabling the data to determine the appropriate tail behavior without imposing an a priori parametric classification.

## 4.8 Asymptotic Distribution of Sample Quantiles and the Bahadur Representation

While sample extremes investigate the outer boundaries $k = 1$ or $k = n$, intermediate order statistics where $k / n \to p \in (0, 1)$ estimate the population quantiles.

Let $p \in (0, 1)$ be a fixed probability fraction. The **population $p$-th quantile** $\xi_p$ of a continuous distribution $F$ is defined as the root of the equation:

$$F(\xi_p) = p \iff \xi_p = F^{-1}(p)$$

For a sample of size $n$, the **sample $p$-th quantile** is defined as the order statistic $X_{(k_n)}$, where the index $k_n = \lceil n p \rceil$ satisfies:

$$\lim_{n \to \infty} \frac{k_n}{n} = p$$

### Asymptotic Normality of Sample Quantiles
Suppose that $F$ is continuously differentiable in an open neighborhood of $\xi_p$ with strictly positive density $f(\xi_p) > 0$.

**Theorem (Asymptotic Normality of Sample Quantiles)**: As the sample size $n \to \infty$, the sample quantile $X_{(k_n)}$ is asymptotically normally distributed:

$$\sqrt{n}\left( X_{(k_n)} - \xi_p \right) \xrightarrow{d} \mathcal{N}\left( 0, \; \frac{p(1 - p)}{[f(\xi_p)]^2} \right)$$

**Proof Intuition via Probability Integral Transform**:
First consider standard uniform order statistics $U_{(k_n)}$. From Section 4.5, $U_{(k_n)} \sim \text{Beta}(k_n, n - k_n + 1)$, which has mean $k_n / (n + 1) \approx p$ and variance $\frac{p(1 - p)}{n}$. By the Central Limit Theorem for Beta distributions:
$$\sqrt{n}(U_{(k_n)} - p) \xrightarrow{d} \mathcal{N}(0, p(1 - p))$$
Now, apply the quantile transformation $X_{(k_n)} = F^{-1}(U_{(k_n)})$. Using the Delta Method (developed in Unit 8) with transformation $g(u) = F^{-1}(u)$, the derivative is:
$$g'(p) = \left. \frac{d}{du} F^{-1}(u) \right|_{u=p} = \frac{1}{f(F^{-1}(p))} = \frac{1}{f(\xi_p)}$$
Therefore, the asymptotic variance of $X_{(k_n)}$ is:
$$\text{AsyVar}\left(\sqrt{n}(X_{(k_n)} - \xi_p)\right) = [g'(p)]^2 \text{AsyVar}\left(\sqrt{n}(U_{(k_n)} - p)\right) = \left(\frac{1}{f(\xi_p)}\right)^2 p(1 - p) = \frac{p(1 - p)}{[f(\xi_p)]^2}$$
establishing the theorem. $\blacksquare$

### Special Case: The Sample Median
For the sample median $\tilde{X}$, set $p = 1/2$. The population median is $\xi_{1/2} = m$, satisfying $F(m) = 1/2$. The numerator of the asymptotic variance is $p(1 - p) = (1/2)(1/2) = 1/4$.
Consequently, the sample median satisfies:

$$\sqrt{n}(\tilde{X} - m) \xrightarrow{d} \mathcal{N}\left( 0, \; \frac{1}{4 [f(m)]^2} \right)$$

This formula demonstrates that the asymptotic precision of the sample median is governed entirely by the height of the probability density at the median, $f(m)$:
- If the population is standard Gaussian $\mathcal{N}(0, 1)$, then $m = 0$ and $f(0) = \frac{1}{\sqrt{2\pi}}$. The asymptotic variance is:
  $$\text{AsyVar}(\sqrt{n}\tilde{X}) = \frac{1}{4 (1/\sqrt{2\pi})^2} = \frac{2\pi}{4} = \frac{\pi}{2} \approx 1.5708$$
  Comparing this to the asymptotic variance of the sample mean $\bar{X}$ (which is $\sigma^2 = 1$), the asymptotic relative efficiency of the median relative to the mean is:
  $$\text{ARE}(\tilde{X}, \bar{X}) = \frac{1}{\pi / 2} = \frac{2}{\pi} \approx 0.6366$$
  In a normal population, the sample median requires approximately $1 / 0.6366 \approx 1.57$ times as many observations as the sample mean to achieve equivalent precision.
- If the population is standard Laplace (Double Exponential) with density $f(x) = \frac{1}{2} e^{-|x|}$, then $m = 0$ and $f(0) = 1/2$. The asymptotic variance of the median is:
  $$\text{AsyVar}(\sqrt{n}\tilde{X}) = \frac{1}{4 (1/2)^2} = \frac{1}{4(1/4)} = 1$$
  The variance of the sample mean for Laplace data is $\sigma^2 = 2$. Therefore:
  $$\text{ARE}(\tilde{X}, \bar{X}) = \frac{2}{1} = 2.0$$
  For Laplace data, the sample median is **twice as efficient** as the sample mean! Because the Laplace distribution has heavy tails and a sharp central peak, the median provides a far superior location estimator than the arithmetic average.

### The Bahadur Representation
In 1966, Raghu Raj Bahadur established a profound almost sure representation that linearizes sample quantiles into an average of independent indicator variables plus a higher-order remainder term:

$$X_{(k_n)} = \xi_p + \frac{p - F_n(\xi_p)}{f(\xi_p)} + R_n$$

where $F_n(x) = \frac{1}{n}\sum_{i=1}^n \mathbf{1}_{(-\infty, x]}(X_i)$ is the empirical cumulative distribution function, and the remainder term satisfies:

$$R_n = \mathcal{O}\left( n^{-3/4} (\ln n)^{1/2} (\ln \ln n)^{1/4} \right) \quad \text{almost surely as } n \to \infty$$

The Bahadur representation reveals that sample quantiles, which appear to be highly non-linear sorting operators, are asymptotically equivalent to sample averages of the indicator variables $\mathbf{1}_{(-\infty, \xi_p]}(X_i)$, enabling the direct application of standard Laws of Large Numbers, Central Limit Theorems, and Laws of the Iterated Logarithm.

## 4.9 Concomitants of Order Statistics in Bivariate Samples

In multivariate data, sorting a sample on one coordinate induces a corresponding ordering on the paired coordinates. These paired values are termed **concomitants** (or induced order statistics).

Let $(X_1, Y_1), (X_2, Y_2), \dots, (X_n, Y_n)$ be an i.i.d. bivariate random sample. If the observations are sorted according to the $X$-coordinates:

$$X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$$

the $Y$-value paired with the $k$-th order statistic $X_{(k)}$ is designated as the **concomitant of $X_{(k)}$**, denoted $Y_{[k]}$.

Notice that while $X_{(1)} < X_{(2)} < \dots < X_{(n)}$ are strictly ordered, their concomitants $Y_{[1]}, Y_{[2]}, \dots, Y_{[n]}$ are **not necessarily sorted**! If $X$ and $Y$ are positively correlated, $Y_{[k]}$ will tend to increase with $k$, but with random stochastic fluctuations.

### Conditional Distribution of Concomitants
The distribution of concomitants is governed by the regression relationship between $Y$ and $X$. Specifically, conditional on the order statistics of $X$:

$$P\left( Y_{[k]} \le y \mid X_{(1)} = x_1, \dots, X_{(n)} = x_n \right) = P\left( Y \le y \mid X = x_k \right) = F_{Y \mid X}(y \mid x_k)$$

The concomitant $Y_{[k]}$ depends on the entire vector of $X$-order statistics solely through its own paired coordinate $X_{(k)}$. Furthermore, conditional on $\mathbf{X}_{(\cdot)}$, the concomitants $Y_{[1]}, Y_{[2]}, \dots, Y_{[n]}$ are **conditionally mutually independent**!

If $(X, Y)$ is bivariate normal with correlation $\rho$, then:

$$Y_{[k]} \mid X_{(k)} = x_k \sim \mathcal{N}\left( \mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x_k - \mu_X), \; \sigma_Y^2(1 - \rho^2) \right)$$

Concomitants play an indispensable role in selection theory (such as predicting offspring traits from selected parents in genetics) and double sampling schemes.

## 4.10 Linear Combinations of Order Statistics: $L$-Estimators and the Trimmed Mean

Order statistics provide the mathematical ingredients for constructing robust estimators of location and scale that are impervious to extreme outliers and heavy-tailed contamination. Such statistics are called **$L$-estimators** (linear combinations of order statistics).

An $L$-estimator of location has the general mathematical form:

$$T_n = \sum_{i=1}^n c_{ni} X_{(i)}$$

where the weights $c_{ni}$ typically sum to 1 ($\sum_{i=1}^n c_{ni} = 1$) and are symmetric: $c_{n, i} = c_{n, n - i + 1}$.

### The $\alpha$-Trimmed Mean
The most prominent $L$-estimator is the **$\alpha$-trimmed mean** $\bar{X}_\alpha$. Let $\alpha \in [0, 1/2)$ be the trimming fraction (typically $\alpha = 0.05$ or $0.10$). The $\alpha$-trimmed mean discards the $k = \lfloor n\alpha \rfloor$ smallest observations and the $k$ largest observations, computing the arithmetic mean of the remaining $n - 2k$ central values:

$$\bar{X}_\alpha = \frac{1}{n - 2k} \sum_{i=k + 1}^{n - k} X_{(i)}$$

- When $\alpha = 0$, $k = 0$, recovering the ordinary sample mean $\bar{X}$.
- As $\alpha \to 1/2$, the trimmed mean converges to the sample median $\tilde{X}$.

The $\alpha$-trimmed mean combines the high efficiency of the sample mean on Gaussian data with the robust protection of the median against wild outliers, possessing a breakdown point equal to the trimming fraction $\alpha$.

## 4.11 Distribution-Free Confidence Intervals for Population Quantiles

A remarkable property of order statistics is that they allow the construction of **exact, distribution-free confidence intervals** for population quantiles without requiring any parametric assumptions about the underlying distribution $F$.

Let $p \in (0, 1)$, and let $\xi_p = F^{-1}(p)$ denote the true population $p$-th quantile. Consider an interval formed by two order statistics: $[X_{(r)}, X_{(s)}]$, where $1 \le r < s \le n$. We wish to determine the exact coverage probability:

$$P\left( X_{(r)} \le \xi_p \le X_{(s)} \right)$$

Observe that the event $\{X_{(r)} \le \xi_p \le X_{(s)}\}$ can be decomposed as:

$$\{X_{(r)} \le \xi_p\} \setminus \{X_{(s)} < \xi_p\}$$

Since $\{X_{(s)} < \xi_p\} \subset \{X_{(r)} \le \xi_p\}$, the probability is:

$$P\left( X_{(r)} \le \xi_p \le X_{(s)} \right) = P\left( X_{(r)} \le \xi_p \right) - P\left( X_{(s)} < \xi_p \right)$$

From Section 4.2, the event $\{X_{(k)} \le \xi_p\}$ is identical to the event that at least $k$ observations fall in $(-\infty, \xi_p]$. Let $Y = \sum_{i=1}^n \mathbf{1}_{(-\infty, \xi_p]}(X_i)$. Because $P(X_i \le \xi_p) = F(\xi_p) = p$, the count $Y$ follows an exact Binomial distribution:

$$Y \sim \text{Binomial}(n, p)$$

Therefore:

$$P(X_{(r)} \le \xi_p) = P(Y \ge r) = \sum_{j=r}^n \binom{n}{j} p^j (1 - p)^{n - j}$$

$$P(X_{(s)} < \xi_p) = P(Y \ge s) = \sum_{j=s}^n \binom{n}{j} p^j (1 - p)^{n - j}$$

Subtracting the two sums:

$$P\left( X_{(r)} \le \xi_p \le X_{(s)} \right) = \sum_{j=r}^{s - 1} \binom{n}{j} p^j (1 - p)^{n - j}$$

Notice that this coverage probability depends **strictly on the known Binomial distribution with parameters $n$ and $p$**! It contains zero unknown parameters and does not depend in any way on the functional form of $F$. By choosing integers $r$ and $s$ such that the binomial sum equals or exceeds $1 - \alpha$, an investigator obtains an exact, distribution-free $100(1 - \alpha)\%$ confidence interval for the population quantile.

## 4.12 Record Values and the Theory of Records: The Rényi Representation

Closely intertwined with order statistics is the theory of **record values**, which models sequential extremes occurring in an evolving time series (such as successive record temperatures in climate tracking, athletic sports records, or successive catastrophic structural stresses).

Let $X_1, X_2, \dots, X_n, \dots$ be an infinite sequence of independent and identically distributed continuous random variables. An observation $X_k$ is termed an **upper record value** (or simply a record) if its magnitude strictly exceeds all preceding observations in the chronological sequence:

$$X_k > \max(X_1, X_2, \dots, X_{k - 1})$$

By convention, the initial observation $X_1$ is always a record.

### Record Indicators and Rényi's Theorem
For each time index $k \ge 1$, define the binary record indicator variable:

$$I_k = \begin{cases} 1 & \text{if } X_k > \max(X_1, \dots, X_{k - 1}) \\ 0 & \text{otherwise} \end{cases}$$

Alfréd Rényi (1962) established a celebrated probabilistic invariance theorem regarding record indicators.

**Theorem (Rényi's Record Invariance Theorem)**: In an i.i.d. sequence from any continuous distribution:
1. The record indicators $I_1, I_2, I_3, \dots$ are **mutually independent random variables**!
2. The probability that the $k$-th observation is a record is inversely proportional to its chronological position:
   $$P(I_k = 1) = \frac{1}{k} \quad \text{for every } k \ge 1$$

**Proof**:
Consider the first $k$ observations $(X_1, X_2, \dots, X_k)$. Because the observations are i.i.d. and continuous, all $k!$ possible orderings of these $k$ variables are equally likely, each occurring with probability $1/k!$.
The event $\{I_k = 1\}$ occurs if and only if $X_k$ is the largest among the first $k$ variables: $X_k = \max(X_1, \dots, X_k)$. By permutation symmetry, any of the $k$ variables has an identical chance of being the maximum. Therefore:
$$P(I_k = 1) = \frac{(k - 1)!}{k!} = \frac{1}{k}$$
To prove mutual independence, let $\pi_k$ denote the rank of $X_k$ among the first $k$ observations. By the properties of relative ranks under uniform permutations, the rank $\pi_k$ is uniformly distributed over $\{1, 2, \dots, k\}$ and is strictly independent of the earlier relative ranks $(\pi_1, \dots, \pi_{k - 1})$. Since $I_k = \mathbf{1}_{\{\pi_k = k\}}$, the indicator $I_k$ is independent of the $\sigma$-algebra $\sigma(I_1, \dots, I_{k - 1})$, proving that $I_1, I_2, \dots$ are mutually independent Bernoulli variables. $\blacksquare$

### Expected Number of Records in a Sample of Size $n$
Let $N_n = \sum_{k=1}^n I_k$ denote the total number of records observed among the first $n$ trials. By linearity of expectation:

$$\mathbb{E}[N_n] = \sum_{k=1}^n \mathbb{E}[I_k] = \sum_{k=1}^n \frac{1}{k} = H_n$$

where $H_n = \sum_{k=1}^n \frac{1}{k}$ is the $n$-th harmonic number. Using the Euler-Mascheroni asymptotic expansion:

$$\mathbb{E}[N_n] = \ln n + \gamma + \mathcal{O}\left(\frac{1}{n}\right)$$

where $\gamma \approx 0.5772$ is the Euler-Mascheroni constant.
Because the indicators $I_k$ are mutually independent, the variance of $N_n$ is:

$$\text{Var}(N_n) = \sum_{k=1}^n \text{Var}(I_k) = \sum_{k=1}^n \left( \frac{1}{k} - \frac{1}{k^2} \right) = \sum_{k=1}^n \frac{1}{k} - \sum_{k=1}^n \frac{1}{k^2}$$

Recalling that $\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$:

$$\text{Var}(N_n) = \ln n + \gamma - \frac{\pi^2}{6} + o(1)$$

Applying the Lindeberg-Feller Central Limit Theorem to the sum of independent indicators:

$$\frac{N_n - \ln n}{\sqrt{\ln n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

This explains why records become extraordinarily rare as time progresses: in a sequence of $n = 1,000,000$ independent trials, the expected number of records is only $\ln(10^6) + 0.58 \approx 13.8 + 0.58 \approx 14.4$!

## 4.13 Order Statistics in Reliability Engineering: Coherent Systems and $k$-out-of-$n$ Architectures

In reliability theory and industrial engineering, systems are constructed from multiple physical components subject to stochastic wear, degradation, and random failure. The operational lifetime of the overall system is governed by order statistics of the component lifetimes.

Let $T_1, T_2, \dots, T_n$ be independent non-negative random variables representing the operational failure times of $n$ identical components, each with cumulative distribution function $F(t) = P(T_i \le t)$ and reliability (survival) function $R_0(t) = P(T_i > t) = 1 - F(t)$.

### Series and Parallel System Architectures
1. **Series System**: A series system functions if and only if **all $n$ components** are functioning. The system fails upon the earliest component failure. The lifetime of a series system is therefore the **first order statistic**:
   $$T_{\text{series}} = \min(T_1, T_2, \dots, T_n) = T_{(1)}$$
   The system reliability function is:
   $$R_{\text{series}}(t) = P(T_{(1)} > t) = \prod_{i=1}^n P(T_i > t) = [R_0(t)]^n = [1 - F(t)]^n$$
   If each component has hazard rate $h_0(t) = f(t) / R_0(t)$, the series system has hazard rate:
   $$h_{\text{series}}(t) = -\frac{d}{dt} \ln R_{\text{series}}(t) = -\frac{d}{dt} [n \ln R_0(t)] = n h_0(t)$$
   A series system is $n$ times more prone to failure than an individual component.
2. **Parallel System**: A parallel system functions as long as **at least one component** remains operational. The system fails only when every component has failed. The lifetime of a parallel system is the **$n$-th order statistic**:
   $$T_{\text{parallel}} = \max(T_1, T_2, \dots, T_n) = T_{(n)}$$
   The system failure probability is:
   $$F_{\text{parallel}}(t) = P(T_{(n)} \le t) = \prod_{i=1}^n P(T_i \le t) = [F(t)]^n = [1 - R_0(t)]^n$$
   The system reliability is:
   $$R_{\text{parallel}}(t) = 1 - [1 - R_0(t)]^n$$

### The $k$-out-of-$n$ Redundant System
A critical engineering generalization is the **$k$-out-of-$n$ system** (such as a multi-engine aircraft that requires at least $k = 2$ of its $n = 4$ engines to maintain flight, or a Byzantine fault-tolerant distributed consensus protocol requiring agreement among at least $k$ nodes).

A $k$-out-of-$n$ system functions if and only if **at least $k$ of the $n$ components remain operational**.
Equivalently, the system fails when $n - k + 1$ components have failed. Therefore, the lifetime of a $k$-out-of-$n$ system is precisely the $(n - k + 1)$-th order statistic:

$$T_{k\text{-out-of-}n} = T_{(n - k + 1)}$$

The system reliability function is obtained directly from the binomial survival formula for order statistics:

$$R_{k\text{-out-of-}n}(t) = P\left( T_{(n - k + 1)} > t \right) = \sum_{j=k}^n \binom{n}{j} [R_0(t)]^j [1 - R_0(t)]^{n - j}$$

This formula allows reliability engineers to optimize redundancy allocations and trade off physical component costs against system mean time between failures (MTBF).

## 4.14 Asymptotic Joint Distribution of Multiple Quantiles and Quantile Processes

In Section 4.8, we established the univariate asymptotic normality of a single sample quantile. In exploratory data analysis and non-parametric curve fitting, analysts routinely examine multiple quantiles simultaneously (such as the quartiles $Q_1 = \xi_{0.25}$, $Q_2 = \xi_{0.50}$, and $Q_3 = \xi_{0.75}$ to construct box plots and interquartile ranges).

Let $0 < p_1 < p_2 < \dots < p_m < 1$ be $m$ distinct probability fractions, with corresponding population quantiles $\xi_{p_r} = F^{-1}(p_r)$. Let $X_{(k_{n, 1})}, \dots, X_{(k_{n, m})}$ denote the corresponding sample quantiles, where $k_{n, r} = \lceil n p_r \rceil$.

**Theorem (Multivariate Quantile Asymptotic Normality)**: Assume that $F$ is continuously differentiable in open neighborhoods of $\xi_{p_1}, \dots, \xi_{p_m}$ with strictly positive densities $f(\xi_{p_r}) > 0$. Then the normalized $m$-dimensional vector of sample quantiles:

$$\sqrt{n} \begin{pmatrix} X_{(k_{n, 1})} - \xi_{p_1} \\ X_{(k_{n, 2})} - \xi_{p_2} \\ \vdots \\ X_{(k_{n, m})} - \xi_{p_m} \end{pmatrix} \xrightarrow{d} \mathcal{N}_m(\mathbf{0}, \boldsymbol{\Omega})$$

converges in distribution to an $m$-dimensional Gaussian distribution with zero mean vector and covariance matrix $\boldsymbol{\Omega} = (\omega_{rs})_{1 \le r, s \le m}$, whose entries are given for $r \le s$ by:

$$\omega_{rs} = \frac{p_r (1 - p_s)}{f(\xi_{p_r}) f(\xi_{p_s})}$$

and $\omega_{sr} = \omega_{rs}$ by symmetry.

### Asymptotic Distribution of the Interquartile Range
The sample **Interquartile Range (IQR)** is defined as:

$$\text{IQR}_n = X_{(\lceil 0.75 n \rceil)} - X_{(\lceil 0.25 n \rceil)}$$

estimating the population interquartile range $\Delta = \xi_{0.75} - \xi_{0.25}$.
Applying the bivariate quantile theorem with $p_1 = 0.25$ and $p_2 = 0.75$:
1. $p_1(1 - p_1) = (0.25)(0.75) = 3/16$.
2. $p_2(1 - p_2) = (0.75)(0.25) = 3/16$.
3. $p_1(1 - p_2) = (0.25)(0.25) = 1/16$.

The asymptotic covariance matrix of $(\hat{\xi}_{0.25}, \hat{\xi}_{0.75})$ is:

$$\boldsymbol{\Omega} = \begin{pmatrix} \frac{3}{16 [f(\xi_{0.25})]^2} & \frac{1}{16 f(\xi_{0.25}) f(\xi_{0.75})} \\ \frac{1}{16 f(\xi_{0.25}) f(\xi_{0.75})} & \frac{3}{16 [f(\xi_{0.75})]^2} \end{pmatrix}$$

By the linear transformation property of normal vectors, the difference $\text{IQR}_n = \hat{\xi}_{0.75} - \hat{\xi}_{0.25}$ has asymptotic variance:

$$\text{AsyVar}\left(\sqrt{n}(\text{IQR}_n - \Delta)\right) = \frac{3}{16 [f(\xi_{0.25})]^2} - \frac{2}{16 f(\xi_{0.25}) f(\xi_{0.75})} + \frac{3}{16 [f(\xi_{0.75})]^2}$$

For a symmetric population where $f(\xi_{0.25}) = f(\xi_{0.75}) = f_Q$:

$$\text{AsyVar}\left(\sqrt{n}(\text{IQR}_n - \Delta)\right) = \frac{3 - 2 + 3}{16 f_Q^2} = \frac{4}{16 f_Q^2} = \frac{1}{4 f_Q^2}$$

This provides the exact asymptotic variance formula for the non-parametric interquartile range across arbitrary symmetric continuous distributions.

## 4.15 Goodness-of-Fit Tests Based on Order Statistics: Kolmogorov-Smirnov and EDF Statistics

Order statistics provide the direct computational mechanism for evaluating whether an observed random sample $X_1, \dots, X_n$ is compatible with a hypothesized continuous cumulative distribution function $F_0(x)$. Such procedures are known as **Empirical Distribution Function (EDF) goodness-of-fit tests**.

The empirical distribution function $F_n(x) = \frac{1}{n}\sum_{i=1}^n \mathbf{1}_{(-\infty, x]}(X_i)$ is a step function with jump discontinuities of height $1/n$ located at each order statistic $X_{(i)}$.

### The Kolmogorov-Smirnov Statistic
The **Kolmogorov-Smirnov statistic** $D_n$ measures the maximum vertical supremum discrepancy between the empirical distribution function and the hypothesized theoretical distribution:

$$D_n = \sup_{x \in \mathbb{R}} |F_n(x) - F_0(x)|$$

Because $F_n(x)$ is constant between consecutive order statistics and jumps only at $X_{(i)}$, the continuous supremum reduces to a finite maximum over the sample order statistics:

$$D_n = \max_{1 \le i \le n} \left\{ \max\left( \left| \frac{i}{n} - F_0(X_{(i)}) \right|, \; \left| F_0(X_{(i)}) - \frac{i - 1}{n} \right| \right) \right\}$$

By the Probability Integral Transform, $U_{(i)} = F_0(X_{(i)})$ are standard uniform order statistics under the null hypothesis $H_0: F = F_0$. Therefore, the distribution of $D_n$ under $H_0$ is **strictly distribution-free**: it is completely independent of the hypothesized distribution function $F_0$.

In 1933, Andrey Kolmogorov proved that when properly scaled by $\sqrt{n}$, $D_n$ converges asymptotically to the Kolmogorov distribution:

$$\lim_{n \to \infty} P\left( \sqrt{n} D_n \le z \right) = K(z) = 1 - 2 \sum_{k=1}^\infty (-1)^{k - 1} e^{-2 k^2 z^2}, \quad z > 0$$

### Quadratic EDF Statistics: Cramér-von Mises and Anderson-Darling
Alternative goodness-of-fit statistics integrate squared discrepancies over the real line:
1. **Cramér-von Mises Statistic**:
   $$W_n^2 = n \int_{-\infty}^\infty [F_n(x) - F_0(x)]^2 dF_0(x) = \sum_{i=1}^n \left( F_0(X_{(i)}) - \frac{2i - 1}{2n} \right)^2 + \frac{1}{12n}$$
2. **Anderson-Darling Statistic**:
   $$A_n^2 = n \int_{-\infty}^\infty \frac{[F_n(x) - F_0(x)]^2}{F_0(x)(1 - F_0(x))} dF_0(x)$$
   The Anderson-Darling statistic weights the squared differences by the reciprocal of the variance function $F_0(x)(1 - F_0(x))$, placing severe penalties on discrepancies occurring in the tails of the distribution. It can be computed in closed form using order statistics:
   $$A_n^2 = -n - \frac{1}{n} \sum_{i=1}^n (2i - 1) \left[ \ln F_0(X_{(i)}) + \ln(1 - F_0(X_{(n - i + 1)})) \right]$$

These formulations underscore how order statistics transform complicated infinite-dimensional function comparisons into exact, highly tractable algebraic computations.

## 4.16 Nonparametric Tolerance Intervals and Wilks' Sample Size Determination

In quality control, manufacturing specifications, and safety certification, engineers must guarantee that a designated proportion $\gamma \in (0, 1)$ of future manufactured parts will fall within guaranteed dimensional tolerances with high statistical confidence $1 - \alpha$. Such boundaries are termed **tolerance intervals**.

Let $X_1, X_2, \dots, X_n$ be an i.i.d. sample from a continuous distribution $F$. Consider the random interval bounded by the sample minimum and sample maximum:

$$[L, U] = [X_{(1)}, X_{(n)}]$$

The proportion of the population covered by this interval is the random variable:

$$C = F(X_{(n)}) - F(X_{(1)})$$

We wish to determine the minimum sample size $n$ such that the interval contains at least a fraction $\gamma$ of the population with confidence at least $1 - \alpha$:

$$P(C \ge \gamma) = P\left( F(X_{(n)}) - F(X_{(1)}) \ge \gamma \right) \ge 1 - \alpha$$

### Derivation of the Exact Coverage Distribution
By the Probability Integral Transform, $U_{(1)} = F(X_{(1)})$ and $U_{(n)} = F(X_{(n)})$ are the minimum and maximum order statistics from a standard uniform distribution.
From Section 4.5, the coverage $C = U_{(n)} - U_{(1)}$ is the sum of $n - 1$ uniform spacings. By the properties of Dirichlet spacings:

$$C \sim \text{Beta}(n - 1, \; 2)$$

The cumulative distribution function of $C$ for $\gamma \in (0, 1)$ is:

$$P(C \le \gamma) = \int_0^\gamma \frac{\Gamma(n + 1)}{\Gamma(n - 1)\Gamma(2)} u^{n - 2} (1 - u)^{2 - 1} \, du = n(n - 1) \int_0^\gamma (u^{n - 2} - u^{n - 1}) \, du$$

Evaluating the elementary integral:

$$P(C \le \gamma) = n(n - 1) \left[ \frac{\gamma^{n - 1}}{n - 1} - \frac{\gamma^n}{n} \right] = n \gamma^{n - 1} - (n - 1) \gamma^n$$

Therefore, the survival probability (confidence level) is:

$$P(C \ge \gamma) = 1 - P(C \le \gamma) = 1 - n \gamma^{n - 1} + (n - 1) \gamma^n$$

Setting this equal to the desired confidence level $1 - \alpha$ yields **Wilks' Tolerance Equation (1941)**:

$$1 - n \gamma^{n - 1} + (n - 1) \gamma^n \ge 1 - \alpha \iff n \gamma^{n - 1} - (n - 1) \gamma^n \le \alpha$$

Remarkably, this equation is **completely distribution-free**: it holds identically for Gaussian, Cauchy, exponential, or multimodal populations without any knowledge of parameters!
For example, to guarantee that the interval $[X_{(1)}, X_{(n)}]$ covers at least $\gamma = 90\%$ of the population with $1 - \alpha = 95\%$ confidence ($\alpha = 0.05$):
- For $n = 45$: $45(0.9)^{44} - 44(0.9)^{45} \approx 0.054 > 0.05$.
- For $n = 47$: $47(0.9)^{46} - 46(0.9)^{47} \approx 0.047 \le 0.05$.

Thus, an engineer needs exactly $n = 47$ observations to guarantee $90\%$ population coverage with $95\%$ confidence, illustrating the immense practical power of exact distribution-free order statistics theory.

## 4.17 Order Statistics from Discrete Populations and the Combinatorics of Ties

While continuous distributions yield strictly ascending chains of order statistics with zero probability of ties ($X_{(1)} < X_{(2)} < \dots < X_{(n)}$), many empirical domains generate discrete integer measurements (such as customer counts, defect numbers, or survey Likert scores). When sampling from a discrete distribution, the probability of ties is strictly positive:

$$P(X_i = X_j) = \sum_{k} [P(X = k)]^2 > 0 \quad \text{for } i \ne j$$

Consequently, discrete order statistics satisfy weak inequalities:

$$X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$$

with multiple coordinates frequently sharing identical values.

### Exact Cumulative Distribution Function in the Discrete Setting
Let $X_1, \dots, X_n$ be an i.i.d. sample from a discrete distribution with probability mass function $p(x) = P(X = x)$ supported on integers $\mathbb{Z}$, and cumulative distribution function $F(x) = \sum_{t \le x} p(t)$.
The binomial connection established in Section 4.2 remains valid: the event $\{X_{(k)} \le x\}$ occurs if and only if at least $k$ observations fall in the interval $(-\infty, x]$:

$$F_{X_{(k)}}(x) = P(X_{(k)} \le x) = \sum_{j=k}^n \binom{n}{j} [F(x)]^j [1 - F(x)]^{n - j}$$

However, because $F(x)$ is a step function with jump discontinuities at each support integer, differentiation is no longer permissible. Instead, the exact probability mass function of the discrete $k$-th order statistic is obtained by finite differencing:

$$P(X_{(k)} = x) = F_{X_{(k)}}(x) - F_{X_{(k)}}(x - 1)$$

Expanding the binomial sums and applying algebraic identities yields the exact discrete probability mass function:

$$P(X_{(k)} = x) = \sum_{j=0}^{k - 1} \sum_{m=0}^{n - k} \frac{n!}{j! (k - 1 - j + 1 + m)! (n - j - (k - j + m))!} [F(x - 1)]^j [p(x)]^{n - j - m} [1 - F(x)]^m$$

Alternatively, by direct trinomial combinatorial partitioning, $X_{(k)} = x$ if and only if:
1. $j$ observations are strictly strictly smaller than $x$ (falling in $(-\infty, x - 1]$), with $0 \le j \le k - 1$.
2. $m$ observations are strictly strictly larger than $x$ (falling in $[x + 1, \infty)$), with $0 \le m \le n - k$.
3. The remaining $n - j - m \ge 1$ observations are tied exactly at $x$.

The probability of this joint trinomial event is:

$$P(X_{(k)} = x) = \sum_{j=0}^{k - 1} \sum_{m=0}^{n - k} \frac{n!}{j! m! (n - j - m)!} [F(x - 1)]^j [1 - F(x)]^m [p(x)]^{n - j - m}$$

### The Method of Continuous Jittering
In computational statistics and non-parametric data processing, analysts frequently convert discrete tied data into continuous variables using the **method of jittering (randomization)**. Let $U_1, \dots, U_n$ be independent $\text{Uniform}(-\epsilon, \epsilon)$ random perturbations, where $\epsilon < 1/2$. Define the jittered variables:

$$X_i^* = X_i + U_i$$

Because $U_i$ is continuous, the jittered variables $X_1^*, \dots, X_n^*$ are strictly continuous with probability 1, completely breaking all ties while strictly preserving the relative ordering among distinct discrete integer values: $X_i < X_j \iff X_i^* < X_j^*$. This allows continuous order statistic algorithms and rank transformations to operate seamlessly on discrete datasets.

## 4.18 Rank Vectors, Permutation Tests, and Linear Rank Statistics

Order statistics record the *values* of sorted observations. In contrast, the **rank vector** records the *positions* occupied by each original observation within the sorted sequence.

Let $X_1, X_2, \dots, X_n$ be an i.i.d. continuous random sample. The **rank** of the $i$-th observation $X_i$, denoted $R_i = \text{Rank}(X_i)$, is defined as the number of sample observations less than or equal to $X_i$:

$$R_i = \sum_{j=1}^n \mathbf{1}_{(-\infty, X_i]}(X_j) = 1 + \sum_{j \ne i} \mathbf{1}_{\{X_j < X_i\}}$$

The vector of all $n$ ranks:

$$\mathbf{R} = (R_1, R_2, \dots, R_n)^T$$

is a random permutation of the first $n$ positive integers $\{1, 2, \dots, n\}$.
Notice that by definition:

$$X_i = X_{(R_i)} \quad \text{and} \quad X_{(k)} = X_{\pi^{-1}(k)}$$

The rank vector $\mathbf{R}$ and the order statistics vector $\mathbf{X}_{(\cdot)} = (X_{(1)}, \dots, X_{(n)})$ decompose the original sample vector $\mathbf{X}$ into two orthogonal components:
1. $\mathbf{X}_{(\cdot)}$ captures all scale, location, and distributional shape information.
2. $\mathbf{R}$ captures purely non-parametric ordinal positioning.

### Distribution-Free Property of the Rank Vector
A cornerstone theorem of non-parametric statistics is that the rank vector is completely **distribution-free**.

**Theorem (Uniform Rank Distribution)**: If $X_1, \dots, X_n$ are i.i.d. from any arbitrary continuous distribution $F$, then the rank vector $\mathbf{R}$ is uniformly distributed over the set of all $n!$ permutations of $\{1, 2, \dots, n\}$:

$$P(\mathbf{R} = \mathbf{r}) = \frac{1}{n!} \quad \text{for every permutation } \mathbf{r} \in \mathcal{S}_n$$

Furthermore, the rank vector $\mathbf{R}$ and the order statistics vector $\mathbf{X}_{(\cdot)}$ are **completely stochastically independent**!

**Proof**:
Let $B$ be any Borel set in $\mathbb{R}^n$, and let $\mathbf{r} = (r_1, \dots, r_n)$ be a specific permutation. The joint event $\{\mathbf{X}_{(\cdot)} \in B, \; \mathbf{R} = \mathbf{r}\}$ corresponds to the original sample vector falling into the specific permutation wedge $\mathbf{X} \in B_{\mathbf{r}}$, where $x_i = y_{r_i}$ for $\mathbf{y} \in B \cap \{y_1 < \dots < y_n\}$.
Because the joint density of $\mathbf{X}$ is permutation-symmetric ($f_{\mathbf{X}}(\mathbf{x}) = \prod f(x_i)$):
$$P(\mathbf{X}_{(\cdot)} \in B, \; \mathbf{R} = \mathbf{r}) = \int_{B \cap \{y_1 < \dots < y_n\}} \prod_{i=1}^n f(y_{r_i}) \, dy_1 \dots dy_n = \int_{B \cap \{y_1 < \dots < y_n\}} \prod_{j=1}^n f(y_j) \, dy_1 \dots dy_n$$
Notice that this integral does not depend on the permutation $\mathbf{r}$. Summing over all $n!$ permutations:
$$P(\mathbf{X}_{(\cdot)} \in B) = n! \int_{B \cap \{y_1 < \dots < y_n\}} \prod_{j=1}^n f(y_j) \, dy_1 \dots dy_n$$
Therefore:
$$P(\mathbf{X}_{(\cdot)} \in B, \; \mathbf{R} = \mathbf{r}) = \frac{1}{n!} P(\mathbf{X}_{(\cdot)} \in B)$$
Summing over all Borel sets $B$ gives $P(\mathbf{R} = \mathbf{r}) = \frac{1}{n!}$, and dividing shows $P(\mathbf{X}_{(\cdot)} \in B, \mathbf{R} = \mathbf{r}) = P(\mathbf{X}_{(\cdot)} \in B) P(\mathbf{R} = \mathbf{r})$, establishing independence. $\blacksquare$

### Linear Rank Statistics
Most classic non-parametric test statistics—such as the Wilcoxon signed-rank statistic, the Mann-Whitney-Wilcoxon two-sample rank sum, and the Spearman rank correlation—are **linear rank statistics**, defined by:

$$L_n = \sum_{i=1}^n c_i a(R_i)$$

where $c_1, \dots, c_n$ are regression or treatment group scores, and $a(1), \dots, a(n)$ are score functions generated by a continuous function $\phi: (0, 1) \to \mathbb{R}$ via $a(k) = \phi(k / (n + 1))$.

Under the null hypothesis of exchangeability, the moments of $L_n$ can be evaluated explicitly using combinatorial averages:
1. **Expectation**:
   $$\mathbb{E}[L_n] = \left( \sum_{i=1}^n c_i \right) \bar{a}, \quad \text{where } \bar{a} = \frac{1}{n}\sum_{k=1}^n a(k)$$
2. **Variance**:
   $$\text{Var}(L_n) = \frac{1}{n - 1} \left( \sum_{i=1}^n (c_i - \bar{c})^2 \right) \left( \sum_{k=1}^n (a(k) - \bar{a})^2 \right)$$

By the celebrated **Hájek Projection Theorem (1961)**, linear rank statistics are asymptotically normally distributed as $n \to \infty$, providing distribution-free hypothesis tests with exceptional Pitman asymptotic relative efficiency across both Gaussian and heavy-tailed non-Gaussian populations.

## 4.19 Quantile-Quantile (Q-Q) Plots, Plotting Positions, and the Shapiro-Wilk Test

A powerful visual and analytical method for diagnosing parametric distributional assumptions is the **Quantile-Quantile (Q-Q) plot**. Rather than comparing histograms or kernel density estimates, which are sensitive to binning widths and bandwidth choices, a Q-Q plot directly compares empirical sample order statistics against theoretical population quantiles.

### Mathematical Formulation of the Q-Q Plot
Let $X_1, X_2, \dots, X_n$ be an observed random sample with order statistics $X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}$. Suppose we hypothesize that the data originate from a location-scale family with distribution function:

$$F(x; \mu, \sigma) = F_0\left( \frac{x - \mu}{\sigma} \right)$$

where $F_0$ is a completely specified standard reference distribution (such as the standard normal $\Phi(z)$), and $\mu \in \mathbb{R}$ and $\sigma > 0$ are unknown location and scale parameters.

Inverting the distribution function, the theoretical $p$-th quantile is:

$$\xi_p = F^{-1}(p; \mu, \sigma) = \mu + \sigma F_0^{-1}(p)$$

From Section 4.5, the expected value of the $i$-th uniform order statistic is $\mathbb{E}[U_{(i)}] = \frac{i}{n + 1}$. Therefore, setting $p_i = \mathbb{E}[U_{(i)}] = \frac{i}{n + 1}$, the expected value of $X_{(i)}$ is approximately:

$$\mathbb{E}[X_{(i)}] \approx F^{-1}(p_i) = \mu + \sigma F_0^{-1}(p_i)$$

A Q-Q plot graphs the bivariate points:

$$\left( q_i, \; X_{(i)} \right) \quad \text{for } i = 1, 2, \dots, n$$

where $q_i = F_0^{-1}(p_i)$ are the **theoretical standard quantiles**, and $X_{(i)}$ are the observed sample order statistics.

If the hypothesized parametric family is correct, the plotted points $(q_i, X_{(i)})$ will fall approximately along a straight line:

$$X_{(i)} \approx \mu + \sigma q_i$$

with intercept equal to the location parameter $\mu$ and slope equal to the scale parameter $\sigma$.
- **Heavier Tails than Reference**: The plot exhibits an $S$-shaped curve, bending downwards in the left tail ($X_{(i)} < \mu + \sigma q_i$) and upwards in the right tail ($X_{(i)} > \mu + \sigma q_i$).
- **Lighter Tails than Reference**: The curve bends upwards in the left tail and downwards in the right tail.
- **Positive Skewness (Right-Skewed)**: The plot shows upward convex curvature throughout.
- **Negative Skewness (Left-Skewed)**: The plot shows downward concave curvature.

### Continuous Plotting Positions: Blom, Hazen, and Weibull
While the naive choice $p_i = \frac{i}{n + 1}$ is common, it produces slight biases in the extreme tails. Mathematical statisticians deploy generalized plotting positions of the form:

$$p_i = \frac{i - a}{n + 1 - 2a}$$

where $a \in [0, 1/2)$ is an adjustment constant:
1. **Weibull Plotting Position ($a = 0$)**: $p_i = \frac{i}{n + 1}$. This matches the exact mean of uniform order statistics $\mathbb{E}[U_{(i)}]$.
2. **Hazen Plotting Position ($a = 0.5$)**: $p_i = \frac{i - 0.5}{n}$. This represents the midpoint of the empirical distribution interval.
3. **Blom Plotting Position ($a = 3/8 = 0.375$)**: $p_i = \frac{i - 3/8}{n + 1/4}$. Gunnar Blom (1958) proved that this choice provides nearly unbiased estimates of theoretical Gaussian quantiles: $\mathbb{E}[X_{(i)}] \approx \mu + \sigma \Phi^{-1}(p_i)$ with error $\mathcal{O}(n^{-2})$.

### The Shapiro-Wilk Test for Normality
The linearity of a Gaussian Q-Q plot serves as the foundation for the **Shapiro-Wilk $W$-statistic (1965)**, universally recognized as the most powerful omnibus test of normality.

Let $\mathbf{m} = (m_1, \dots, m_n)^T$ denote the vector of expected values of standard normal order statistics: $m_i = \mathbb{E}[Z_{(i)}]$, and let $\mathbf{V}$ denote their $n \times n$ covariance matrix: $V_{ij} = \text{Cov}(Z_{(i)}, Z_{(j)})$.
The generalized least squares estimator of the slope $\sigma$ in the Q-Q regression $X_{(i)} \approx \mu + \sigma m_i$ is proportional to:

$$b = \frac{\mathbf{m}^T \mathbf{V}^{-1} \mathbf{X}_{(\cdot)}}{\sqrt{\mathbf{m}^T \mathbf{V}^{-1} \mathbf{V}^{-1} \mathbf{m}}} = \sum_{i=1}^n a_i X_{(i)}$$

where the weight vector $\mathbf{a} = (a_1, \dots, a_n)^T = \frac{\mathbf{m}^T \mathbf{V}^{-1}}{\|\mathbf{m}^T \mathbf{V}^{-1}\|}$ satisfies $\mathbf{a}^T \mathbf{a} = 1$.
The Shapiro-Wilk test statistic is the ratio of the squared optimal slope estimator to the sample sum of squares:

$$W = \frac{b^2}{\sum_{i=1}^n (X_i - \bar{X})^2} = \frac{\left( \sum_{i=1}^n a_i X_{(i)} \right)^2}{\sum_{i=1}^n (X_i - \bar{X})^2}$$

Notice that $W$ is precisely the **squared Pearson correlation coefficient** between the observed order statistics $X_{(i)}$ and the optimal Gaussian weights $a_i$!
By Cauchy-Schwarz, $0 < W \le 1$. If the sample is truly Gaussian, the points are strictly collinear, driving $W$ close to 1. Departures from normality (skewness, heavy tails, bimodality) introduce non-linear curvature, substantially depressing the value of $W$ below 1 and triggering rejection of the Gaussian null hypothesis.

## Fully worked question 1: Joint Distribution of Extremes and Exact Density of the Sample Range for the Uniform Distribution

### Question
Let $X_1, X_2, \dots, X_n$ ($n \ge 2$) be an i.i.d. random sample from a Uniform distribution on the interval $(0, \theta)$, where $\theta > 0$, with probability density function:

$$f(x) = \frac{1}{\theta}, \quad 0 < x < \theta$$

and cumulative distribution function $F(x) = x / \theta$ for $0 < x < \theta$.
1. Derive the joint probability density function $f_{X_{(1)}, X_{(n)}}(u, v)$ of the sample minimum $X_{(1)}$ and sample maximum $X_{(n)}$.
2. Apply the bivariate transformation to derive the joint probability density function of the sample range $R = X_{(n)} - X_{(1)}$ and the sample midrange $M = \frac{X_{(1)} + X_{(n)}}{2}$.
3. Determine the exact support region in the $(r, m)$-plane and integrate out $m$ to find the marginal probability density function $f_R(r)$ of the sample range.
4. Calculate the expected value $\mathbb{E}[R]$ and variance $\text{Var}(R)$ of the sample range.

### Solution, step 1: Joint Density of the Extremes
For $X \sim \text{Uniform}(0, \theta)$, $F(x) = x / \theta$ and $f(x) = 1 / \theta$ for $x \in (0, \theta)$.
From Section 4.3, the joint probability density function of the minimum $X_{(1)}$ and maximum $X_{(n)}$ is given for $0 < u < v < \theta$ by:

$$f_{X_{(1)}, X_{(n)}}(u, v) = n(n - 1) [F(v) - F(u)]^{n - 2} f(u) f(v)$$

Substitute $F(v) - F(u) = \frac{v - u}{\theta}$ and $f(u) = f(v) = \frac{1}{\theta}$:

$$f_{X_{(1)}, X_{(n)}}(u, v) = n(n - 1) \left( \frac{v - u}{\theta} \right)^{n - 2} \left(\frac{1}{\theta}\right) \left(\frac{1}{\theta}\right) = \frac{n(n - 1)}{\theta^n} (v - u)^{n - 2}$$

valid on the triangular support domain $\mathcal{S} = \{(u, v) : 0 < u < v < \theta\}$, and zero elsewhere.

### Solution, step 2: Bivariate Transformation to Range and Midrange
Define the transformation:

$$R = X_{(n)} - X_{(1)}, \quad M = \frac{X_{(1)} + X_{(n)}}{2}$$

The inverse transformation is:

$$X_{(1)} = M - \frac{R}{2}, \quad X_{(n)} = M + \frac{R}{2}$$

As computed in Section 4.4, the Jacobian determinant is $|\det(J)| = 1$.
Substitute the inverse transformation into $v - u$:

$$v - u = \left( m + \frac{r}{2} \right) - \left( m - \frac{r}{2} \right) = r$$

Therefore, the joint probability density function of $(R, M)$ is:

$$f_{R, M}(r, m) = \frac{n(n - 1)}{\theta^n} r^{n - 2} \cdot 1 = \frac{n(n - 1)}{\theta^n} r^{n - 2}$$

### Solution, step 3: Determination of the Support Region and Marginal Integration
To find the limits of integration for $m$, map the original support constraints $0 < u < v < \theta$ into $(r, m)$ coordinates:
1. $u > 0 \implies m - \frac{r}{2} > 0 \implies m > \frac{r}{2}$.
2. $v < \theta \implies m + \frac{r}{2} < \theta \implies m < \theta - \frac{r}{2}$.
3. $u < v \implies m - \frac{r}{2} < m + \frac{r}{2} \implies r > 0$.

Combining these inequalities, the range $r$ can vary from $0$ to $\theta$. For any fixed $r \in (0, \theta)$, the midrange $m$ is constrained to the interval:

$$\frac{r}{2} < m < \theta - \frac{r}{2}$$

The length of this $m$-interval is:

$$\left(\theta - \frac{r}{2}\right) - \frac{r}{2} = \theta - r$$

To obtain the marginal probability density function $f_R(r)$, integrate $f_{R, M}(r, m)$ over this valid $m$-interval:

$$f_R(r) = \int_{r/2}^{\theta - r/2} \frac{n(n - 1)}{\theta^n} r^{n - 2} \, dm = \frac{n(n - 1)}{\theta^n} r^{n - 2} \int_{r/2}^{\theta - r/2} dm$$

Evaluating the elementary integral:

$$f_R(r) = \frac{n(n - 1)}{\theta^n} r^{n - 2} (\theta - r) = \frac{n(n - 1)}{\theta^n} \left( \theta r^{n - 2} - r^{n - 1} \right), \quad 0 < r < \theta$$

and zero elsewhere. Notice that when standardized by $W = R / \theta$, $W \sim \text{Beta}(n - 1, 2)$.

### Solution, step 4: Moments of the Sample Range
To evaluate the expected value $\mathbb{E}[R]$, compute the integral:

$$\mathbb{E}[R] = \int_0^\theta r f_R(r) \, dr = \frac{n(n - 1)}{\theta^n} \int_0^\theta \left( \theta r^{n - 1} - r^n \right) dr$$

Evaluate each term:

$$\int_0^\theta \theta r^{n - 1} dr = \theta \left[ \frac{r^n}{n} \right]_0^\theta = \frac{\theta^{n + 1}}{n}$$

$$\int_0^\theta r^n dr = \frac{\theta^{n + 1}}{n + 1}$$

Subtracting the two terms:

$$\frac{\theta^{n + 1}}{n} - \frac{\theta^{n + 1}}{n + 1} = \theta^{n + 1} \left( \frac{n + 1 - n}{n(n + 1)} \right) = \frac{\theta^{n + 1}}{n(n + 1)}$$

Multiplying by the pre-factor:

$$\mathbb{E}[R] = \frac{n(n - 1)}{\theta^n} \cdot \frac{\theta^{n + 1}}{n(n + 1)} = \frac{n - 1}{n + 1} \theta$$

To compute the variance, we first evaluate the second moment $\mathbb{E}[R^2]$:

$$\mathbb{E}[R^2] = \frac{n(n - 1)}{\theta^n} \int_0^\theta \left( \theta r^n - r^{n + 1} \right) dr = \frac{n(n - 1)}{\theta^n} \left[ \frac{\theta^{n + 2}}{n + 1} - \frac{\theta^{n + 2}}{n + 2} \right]$$

$$\frac{1}{n + 1} - \frac{1}{n + 2} = \frac{1}{(n + 1)(n + 2)}$$

$$\mathbb{E}[R^2] = \frac{n(n - 1)}{\theta^n} \cdot \frac{\theta^{n + 2}}{(n + 1)(n + 2)} = \frac{n(n - 1)}{(n + 1)(n + 2)} \theta^2$$

Now compute the variance:

$$\text{Var}(R) = \mathbb{E}[R^2] - (\mathbb{E}[R])^2 = \theta^2 \left[ \frac{n(n - 1)}{(n + 1)(n + 2)} - \frac{(n - 1)^2}{(n + 1)^2} \right] = \theta^2 \frac{n - 1}{n + 1} \left[ \frac{n}{n + 2} - \frac{n - 1}{n + 1} \right]$$

Simplify the bracketed difference:

$$\frac{n(n + 1) - (n - 1)(n + 2)}{(n + 2)(n + 1)} = \frac{(n^2 + n) - (n^2 + n - 2)}{(n + 1)(n + 2)} = \frac{2}{(n + 1)(n + 2)}$$

Therefore, the exact variance of the sample range is:

$$\text{Var}(R) = \frac{2(n - 1)}{(n + 1)^2 (n + 2)} \theta^2$$

As $n \to \infty$, $\mathbb{E}[R] \to \theta$ and $\text{Var}(R) = \mathcal{O}(n^{-2}) \to 0$, showing that the sample range converges in mean square to the true population support width $\theta$.

## Fully worked question 2: Proof of Independence and Exponential Distribution of Normalized Spacings via Sukhatme's Transformation

### Question
Let $X_1, X_2, \dots, X_n$ be an i.i.d. sample from an Exponential distribution with rate parameter $\lambda > 0$, with joint density of order statistics:

$$f_{X_{(1)}, \dots, X_{(n)}}(x_1, \dots, x_n) = n! \lambda^n \exp\left( -\lambda \sum_{i=1}^n x_i \right), \quad 0 < x_1 < x_2 < \dots < x_n < \infty$$

Define Sukhatme's normalized spacings:

$$Z_1 = n X_{(1)}$$

$$Z_2 = (n - 1)(X_{(2)} - X_{(1)})$$

$$Z_k = (n - k + 1)(X_{(k)} - X_{(k - 1)}) \quad \text{for } k = 1, 2, \dots, n$$

1. Express each order statistic $X_{(k)}$ as a linear combination of $Z_1, \dots, Z_k$.
2. Formulate the multivariate transformation mapping $(X_{(1)}, \dots, X_{(n)}) \mapsto (Z_1, \dots, Z_n)$ and compute its Jacobian matrix and determinant.
3. Express the exponent $\sum_{i=1}^n x_i$ in terms of $z_1, \dots, z_n$.
4. Derive the joint probability density function $f_{Z_1, \dots, Z_n}(z_1, \dots, z_n)$ and prove that $Z_1, \dots, Z_n$ are mutually independent, identically distributed Exponential random variables with common rate parameter $\lambda$.

### Solution, step 1: Inverse Linear Representation of Order Statistics
From the definition of the normalized spacings:

$$X_{(1)} = \frac{Z_1}{n}$$

$$X_{(2)} - X_{(1)} = \frac{Z_2}{n - 1} \implies X_{(2)} = X_{(1)} + \frac{Z_2}{n - 1} = \frac{Z_1}{n} + \frac{Z_2}{n - 1}$$

Inductively, for any index $k \in \{1, 2, \dots, n\}$:

$$X_{(k)} = \sum_{j=1}^k \frac{Z_j}{n - j + 1}$$

This expresses each original order statistic $x_k$ as a lower-triangular linear combination of the normalized spacings $z_1, \dots, z_k$.

### Solution, step 2: Jacobian Matrix and Determinant Evaluation
The mapping from $\mathbf{z} = (z_1, \dots, z_n)^T$ to $\mathbf{x} = (x_1, \dots, x_n)^T$ is linear: $\mathbf{x} = \mathbf{T} \mathbf{z}$, where $\mathbf{T}$ is a lower-triangular matrix with entries:

$$T_{kj} = \begin{cases} \frac{1}{n - j + 1} & \text{if } j \le k \\ 0 & \text{if } j > k \end{cases}$$

The Jacobian matrix of the inverse transformation is precisely $\mathbf{T}$:

$$J = \begin{pmatrix}
1/n & 0 & 0 & \dots & 0 \\
1/n & 1/(n - 1) & 0 & \dots & 0 \\
1/n & 1/(n - 1) & 1/(n - 2) & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1/n & 1/(n - 1) & 1/(n - 2) & \dots & 1/1
\end{pmatrix}$$

Because $\mathbf{T}$ is lower-triangular, its determinant is simply the product of its diagonal elements:

$$\det(J) = \prod_{j=1}^n T_{jj} = \prod_{j=1}^n \frac{1}{n - j + 1} = \frac{1}{n} \cdot \frac{1}{n - 1} \cdot \dots \cdot \frac{1}{1} = \frac{1}{n!}$$

Because all diagonal elements are strictly positive, $|\det(J)| = \frac{1}{n!}$.
Furthermore, the ordering constraint $0 < x_1 < x_2 < \dots < x_n < \infty$ translates directly to:

$$z_k = (n - k + 1)(x_k - x_{k - 1}) > 0 \quad \text{for all } k \in \{1, \dots, n\}$$

The image space is the entire positive orthant $\mathbb{R}_+^n = \{(z_1, \dots, z_n) : z_k > 0 \text{ for all } k\}$.

### Solution, step 3: Algebraic Rearrangement of the Exponent
We now express the sum of order statistics $\sum_{k=1}^n x_k$ in terms of the $z_j$:

$$\sum_{k=1}^n x_k = \sum_{k=1}^n \sum_{j=1}^k \frac{z_j}{n - j + 1}$$

Interchange the order of summation. The double sum ranges over the index pairs $1 \le j \le k \le n$:

$$\sum_{k=1}^n \sum_{j=1}^k \frac{z_j}{n - j + 1} = \sum_{j=1}^n \frac{z_j}{n - j + 1} \left( \sum_{k=j}^n 1 \right)$$

Notice that the inner sum counts the number of integers from $j$ to $n$, which is exactly $n - j + 1$:

$$\sum_{k=j}^n 1 = n - j + 1$$

Therefore, the factors cancel completely:

$$\sum_{j=1}^n \frac{z_j}{n - j + 1} (n - j + 1) = \sum_{j=1}^n z_j$$

This yields the algebraic identity:

$$\sum_{k=1}^n x_k = \sum_{j=1}^n z_j$$

### Solution, step 4: Joint Density Construction and Independence Proof
Applying the multivariate change of variables formula:

$$f_{Z_1, \dots, Z_n}(z_1, \dots, z_n) = f_{X_{(1)}, \dots, X_{(n)}}(\mathbf{x}(\mathbf{z})) \cdot |\det(J)|$$

Substitute the joint density of the order statistics and the Jacobian determinant:

$$f_{Z_1, \dots, Z_n}(z_1, \dots, z_n) = \left[ n! \lambda^n \exp\left( -\lambda \sum_{j=1}^n z_j \right) \right] \cdot \frac{1}{n!}$$

The factorial $n!$ cancels out completely:

$$f_{Z_1, \dots, Z_n}(z_1, \dots, z_n) = \lambda^n \exp\left( -\lambda \sum_{j=1}^n z_j \right) = \prod_{j=1}^n \lambda e^{-\lambda z_j}$$

valid for all $z_1 > 0, z_2 > 0, \dots, z_n > 0$.
Because the joint probability density function factorizes completely into the product of $n$ univariate functions:

$$f_{Z_1, \dots, Z_n}(z_1, \dots, z_n) = \prod_{j=1}^n f_{Z_j}(z_j), \quad \text{where } f_{Z_j}(z_j) = \lambda e^{-\lambda z_j} \mathbf{1}_{(0, \infty)}(z_j)$$

the random variables $Z_1, Z_2, \dots, Z_n$ are **mutually stochastically independent**, and each follows an exact **Exponential distribution with rate parameter $\lambda$**:

$$Z_j \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\lambda) \quad \text{for } j = 1, 2, \dots, n$$

This completes the full rigorous proof of Sukhatme's theorem. $\blacksquare$

## Fully worked question 3: Asymptotic Normality Proof of the Sample Quantile via the Bahadur Representation

### Question
Let $X_1, X_2, \dots, X_n$ be an i.i.d. sample from a continuous distribution $F$ with density $f$. Let $p \in (0, 1)$ be fixed, and let $\xi_p = F^{-1}(p)$ denote the true population $p$-th quantile. Assume that $F$ is twice differentiable at $\xi_p$ with $f(\xi_p) > 0$.
1. State the empirical distribution function $F_n(x)$ and derive its exact mean and variance at $x = \xi_p$.
2. Prove that $\sqrt{n}(F_n(\xi_p) - p) \xrightarrow{d} \mathcal{N}(0, p(1 - p))$.
3. Formulate the inversion equivalence between the sample quantile $X_{(k_n)}$ (where $k_n = \lceil n p \rceil$) and $F_n(x)$.
4. Use the Taylor expansion of $F$ around $\xi_p$ to establish that:
   $$\sqrt{n}\left( X_{(k_n)} - \xi_p \right) \xrightarrow{d} \mathcal{N}\left( 0, \; \frac{p(1 - p)}{[f(\xi_p)]^2} \right)$$

### Solution, step 1: Mean and Variance of the Empirical Distribution Function
The empirical distribution function $F_n(x)$ is defined as:

$$F_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{(-\infty, x]}(X_i)$$

For $x = \xi_p$, define the indicator random variables $I_i = \mathbf{1}_{(-\infty, \xi_p]}(X_i)$.
Since $X_1, \dots, X_n$ are i.i.d., the indicators $I_1, \dots, I_n$ are independent Bernoulli random variables with success probability:

$$P(X_i \le \xi_p) = F(\xi_p) = p$$

The expectation of $F_n(\xi_p)$ is:

$$\mathbb{E}[F_n(\xi_p)] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[I_i] = \frac{1}{n} (n p) = p$$

The variance of each indicator is $\text{Var}(I_i) = p(1 - p)$. Because the observations are independent:

$$\text{Var}(F_n(\xi_p)) = \text{Var}\left( \frac{1}{n} \sum_{i=1}^n I_i \right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(I_i) = \frac{1}{n^2} (n p(1 - p)) = \frac{p(1 - p)}{n}$$

### Solution, step 2: Asymptotic Normality of the Empirical Proportion
The normalized difference can be written as a standardized sum of i.i.d. zero-mean random variables:

$$\sqrt{n}(F_n(\xi_p) - p) = \frac{1}{\sqrt{n}} \sum_{i=1}^n (I_i - p)$$

Each term $I_i - p$ has mean $\mathbb{E}[I_i - p] = 0$ and finite variance $\sigma_I^2 = p(1 - p)$.
By the classical Lindeberg-Lévy Central Limit Theorem:

$$\sqrt{n}(F_n(\xi_p) - p) \xrightarrow{d} \mathcal{N}(0, p(1 - p))$$

### Solution, step 3: The Inversion Equivalence
Let $k_n = \lceil n p \rceil$, and let $\hat{\xi}_{n, p} = X_{(k_n)}$ denote the sample $p$-th quantile.
For any real number $t \in \mathbb{R}$, consider the probability event:

$$P\left( \sqrt{n}(\hat{\xi}_{n, p} - \xi_p) \le t \right) = P\left( \hat{\xi}_{n, p} \le \xi_p + \frac{t}{\sqrt{n}} \right)$$

Recall the fundamental identity between order statistics and the empirical distribution:
The $k_n$-th order statistic satisfies $X_{(k_n)} \le x$ if and only if the empirical distribution satisfies $F_n(x) \ge \frac{k_n}{n}$.
Setting $x_n = \xi_p + \frac{t}{\sqrt{n}}$:

$$P\left( \hat{\xi}_{n, p} \le x_n \right) = P\left( F_n(x_n) \ge \frac{k_n}{n} \right) = P\left( \sqrt{n}(F_n(x_n) - F(x_n)) \ge \sqrt{n}\left( \frac{k_n}{n} - F(x_n) \right) \right)$$

Equivalently, multiplying by $-1$:

$$P\left( \sqrt{n}(\hat{\xi}_{n, p} - \xi_p) \le t \right) = P\left( \sqrt{n}(F(x_n) - F_n(x_n)) \le \sqrt{n}\left( F(x_n) - \frac{k_n}{n} \right) \right)$$

### Solution, step 4: Taylor Expansion and Asymptotic Limit
Now expand $F(x_n) = F\left(\xi_p + \frac{t}{\sqrt{n}}\right)$ in a first-order Taylor series around $\xi_p$:

$$F\left(\xi_p + \frac{t}{\sqrt{n}}\right) = F(\xi_p) + F'(\xi_p) \frac{t}{\sqrt{n}} + o\left(\frac{1}{\sqrt{n}}\right) = p + f(\xi_p) \frac{t}{\sqrt{n}} + o\left(\frac{1}{\sqrt{n}}\right)$$

Since $k_n = \lceil n p \rceil$, $k_n / n = p + \mathcal{O}(1/n)$. Therefore:

$$\sqrt{n}\left( F(x_n) - \frac{k_n}{n} \right) = \sqrt{n}\left( p + f(\xi_p) \frac{t}{\sqrt{n}} - p + \mathcal{O}\left(\frac{1}{n}\right) \right) = f(\xi_p) t + o(1)$$

Next, consider the random variable $\sqrt{n}(F(x_n) - F_n(x_n))$.
By the continuity of the empirical process (or the Glivenko-Cantelli and Donsker theorems):

$$\sqrt{n}(F(x_n) - F_n(x_n)) = \sqrt{n}(p - F_n(\xi_p)) + o_p(1)$$

From Step 2, $W_n = \sqrt{n}(p - F_n(\xi_p)) \xrightarrow{d} \mathcal{N}(0, p(1 - p))$.
Therefore, taking the limit as $n \to \infty$:

$$\lim_{n \to \infty} P\left( \sqrt{n}(\hat{\xi}_{n, p} - \xi_p) \le t \right) = \lim_{n \to \infty} P\left( W_n \le f(\xi_p) t \right) = \Phi\left( \frac{f(\xi_p) t}{\sqrt{p(1 - p)}} \right)$$

Notice that this is the cumulative distribution function of a Gaussian random variable:

$$\Phi\left( \frac{t}{\frac{\sqrt{p(1 - p)}}{f(\xi_p)}} \right)$$

By the Portmanteau Theorem, convergence of the cumulative distribution functions at all continuity points implies convergence in distribution:

$$\sqrt{n}\left( \hat{\xi}_{n, p} - \xi_p \right) \xrightarrow{d} \mathcal{N}\left( 0, \; \frac{p(1 - p)}{[f(\xi_p)]^2} \right)$$

This completes the rigorous proof of asymptotic normality of the sample quantile. $\blacksquare$
"""

DEST.write_text(content.strip() + "\n", encoding="utf-8")
print(f"Unit 4 authored successfully at {DEST} ({len(content)} chars)")
