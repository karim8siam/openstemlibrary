# Unit 8: Asymptotic Distribution Theory: Continuous Mapping, Slutsky's Theorem, and the Delta Method

## 8.1 The Philosophy and Role of Asymptotic Distribution Theory in Modern Inference

In mathematical statistics and scientific data analysis, exact finite-sample distributions for estimators $\hat{\theta}_n = T(X_1, \dots, X_n)$ can rarely be obtained in closed, analytically tractable form. While classical Gaussian sampling theory provides exact distributions—such as Student's $t$, Snedecor's $F$, and Fisher's $\chi^2$—these results rest upon the rigid and frequently unrealistic assumption that the parent population is strictly normal. In real-world scientific applications across physics, astronomy, biometrics, econometrics, genomics, and machine learning, empirical data almost invariably exhibit skewness, kurtosis, multi-modality, or heavy polynomial tails that deviate substantially from Gaussianity.

Furthermore, even if the parent distribution were known precisely, nonlinear transformations of sample statistics pose formidable analytical barriers. Consider calculating the exact finite-sample distribution of:
- The sample coefficient of variation $V_n = S_n / \bar{X}_n$;
- The sample Pearson correlation coefficient $r_n$;
- The empirical log-odds ratio $\ln(\hat{p}_1(1-\hat{p}_2) / [\hat{p}_2(1-\hat{p}_1)])$;
- Shannon entropy estimators $-\sum \hat{p}_i \ln \hat{p}_i$;
- Non-linear least squares parameters and Generalized Method of Moments (GMM) estimators.

The exact finite-sample distributions of these estimators depend upon complex multidimensional integrals or infinite hypergeometric series that offer limited intuitive insight and are cumbersome to use for hypothesis testing or confidence interval construction.

### The Asymptotic Paradigm

**Asymptotic distribution theory** overcomes these intractable obstacles by shifting focus from the exact finite-sample distribution $F_n(t) = P(\hat{\theta}_n \le t)$ to the limiting behavior of the sequence of distributions as the sample size $n$ approaches infinity ($n \to \infty$). Instead of attempting to calculate $F_n$ for every individual $n$, asymptotic theory identifies:
1. A deterministic centering sequence (the true parameter $\theta_0$ or population quantity);
2. A deterministic normalizing rate of convergence $a_n \uparrow \infty$ (most commonly the root-$n$ rate $a_n = \sqrt{n}$);
3. A stable, non-degenerate limiting probability distribution $G$ (predominantly the Gaussian distribution $\mathcal{N}(0, V)$).

Formally, we establish that:

$$a_n(\hat{\theta}_n - \theta_0) \xrightarrow{d} G$$

When $G \sim \mathcal{N}(0, V(\theta_0))$, the scalar or matrix $V(\theta_0)$ is designated as the **asymptotic variance** (or asymptotic covariance matrix) of the estimator. For large but finite sample sizes $n$, this asymptotic limit justifies the operational approximation:

$$\hat{\theta}_n \stackrel{a}{\sim} \mathcal{N}\left( \theta_0, \, \frac{V(\theta_0)}{n} \right)$$

This approximation enables researchers to construct asymptotically valid confidence intervals, formulate likelihood ratio, Wald, and score tests with well-calibrated type I error rates, and compare the statistical efficiency of competing estimators via **Asymptotic Relative Efficiency (ARE)**.

### Historical Evolution: From Laplace to Modern Empirical Process Theory

The conceptual roots of asymptotic theory trace back to Pierre-Simon Laplace and Carl Friedrich Gauss, who recognized that aggregate errors in astronomical observations tended toward a normal law. In the early twentieth century, Karl Pearson, Ronald A. Fisher, and Jerzy Neyman formalized the role of asymptotic normality in maximum likelihood estimation and hypothesis testing. However, the rigorous mathematical foundations that undergird modern asymptotic statistics were constructed between 1925 and 1970 by Evgeny Slutsky, Harald Cramér, Henry Mann, Abraham Wald, C. R. Rao, and Lucien Le Cam.

Le Cam's theory of **Local Asymptotic Normality (LAN)** and contemporary empirical process theory (developed by Richard Dudley, David Pollard, and Aad van der Vaart) revealed that asymptotic normality is not merely an algebraic curiosity of the Central Limit Theorem. Rather, it reflects a deep mathematical property of regular statistical experiments: in a localized $1/\sqrt{n}$ neighborhood of the true parameter, the statistical experiment converges weakly to a Gaussian shift experiment.

To operationalize asymptotic distribution theory, however, we require an analytical calculus that allows us to perform algebraic manipulations—such as addition, multiplication, division, and smooth functional transformations—on sequences of random variables that converge in distribution and in probability. This unit develops the four cornerstones of asymptotic theory:
1. **The Continuous Mapping Theorem (Mann-Wald Theorem)**;
2. **Slutsky's Theorem**;
3. **The Univariate and Multivariate Delta Methods**;
4. **Variance Stabilizing Transformations and Asymptotic Relative Efficiency**.


## 8.2 The Continuous Mapping Theorem (Mann-Wald Theorem)

In deterministic real analysis, a function $g: \mathbb{R} \to \mathbb{R}$ is continuous at a point $x$ if and only if for every deterministic sequence $x_n \to x$, we have $g(x_n) \to g(x)$. The **Continuous Mapping Theorem** (often called the Mann-Wald Theorem, after Henry Mann and Abraham Wald who popularized it in econometrics in 1943) asserts that this fundamental property extends to all four modes of stochastic convergence: almost sure convergence, convergence in probability, and convergence in distribution.

### Theorem 8.1: The Continuous Mapping Theorem (CMT)
Let $\{X_n\}_{n=1}^\infty$ be a sequence of random elements taking values in a metric space $(\mathcal{X}, d_{\mathcal{X}})$ (such as $\mathbb{R}^k$ with the standard Euclidean metric), and let $X$ be a random element in $\mathcal{X}$. Let $(\mathcal{Y}, d_{\mathcal{Y}})$ be another metric space (such as $\mathbb{R}^m$), and let $g: \mathcal{X} \to \mathcal{Y}$ be a measurable function. 

Let $C_g \subseteq \mathcal{X}$ denote the set of points at which the function $g$ is continuous. Suppose that the limiting random variable $X$ takes values in the continuity set $C_g$ with probability 1:

$$P(X \in C_g) = 1$$

Then the following stochastic implications hold:
1. **Almost Sure Convergence**: If $X_n \xrightarrow{\text{a.s.}} X$, then $g(X_n) \xrightarrow{\text{a.s.}} g(X)$.
2. **Convergence in Probability**: If $X_n \xrightarrow{P} X$, then $g(X_n) \xrightarrow{P} g(X)$.
3. **Convergence in Distribution**: If $X_n \xrightarrow{d} X$, then $g(X_n) \xrightarrow{d} g(X)$.

---

### Rigorous Proof for Convergence in Probability

Understanding why the Continuous Mapping Theorem holds for convergence in probability provides valuable pedagogical insight into $\epsilon$-$\delta$ arguments on probability spaces.

**Proof**:
Let $\epsilon > 0$ be given. We must demonstrate that:

$$\lim_{n \to \infty} P\left( d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \right) = 0$$

Let $x_0 \in C_g$ be an arbitrary continuity point of $g$. By the definition of metric continuity, there exists a strictly positive radius $\delta(x_0, \epsilon) > 0$ such that whenever $d_{\mathcal{X}}(x, x_0) < \delta(x_0, \epsilon)$, we have $d_{\mathcal{Y}}(g(x), g(x_0)) < \epsilon/2$.

Now, for any positive $\delta > 0$, decompose the event of interest:

$$\{ d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \} \subseteq \{ d_{\mathcal{X}}(X_n, X) \ge \delta \} \cup \{ d_{\mathcal{X}}(X_n, X) < \delta \text{ and } d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \}$$

Taking probabilities of both sides:

$$P\left( d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \right) \le P\left( d_{\mathcal{X}}(X_n, X) \ge \delta \right) + P\left( d_{\mathcal{X}}(X_n, X) < \delta \text{ and } d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \right)$$

Taking the limit superior as $n \to \infty$. By the hypothesis of convergence in probability, for any fixed $\delta > 0$, the first term vanishes: $\lim_{n \to \infty} P(d_{\mathcal{X}}(X_n, X) \ge \delta) = 0$.
Therefore:

$$\limsup_{n \to \infty} P\left( d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \right) \le \limsup_{n \to \infty} P\left( d_{\mathcal{X}}(X_n, X) < \delta \text{ and } d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \right)$$

Because $X \in C_g$ almost surely, by choosing $\delta$ sufficiently small, the second probability can be made arbitrarily small by the continuity of $g$ on the support of $X$. Taking the infimum over all $\delta > 0$:

$$\limsup_{n \to \infty} P\left( d_{\mathcal{Y}}(g(X_n), g(X)) \ge \epsilon \right) = 0$$

Since probabilities are non-negative, the limit exists and equals zero. Thus, $g(X_n) \xrightarrow{P} g(X)$. $\blacksquare$

---

### Rigorous Proof for Convergence in Distribution via the Portmanteau Theorem

**Proof**:
We utilize the topological characterization of weak convergence provided by Alexandrov's Portmanteau Theorem: a sequence $Y_n \xrightarrow{d} Y$ if and only if for every closed set $F \subseteq \mathcal{Y}$, we have:

$$\limsup_{n \to \infty} P(Y_n \in F) \le P(Y \in F)$$

Let $F \subseteq \mathcal{Y}$ be an arbitrary closed set. The event $\{g(X_n) \in F\}$ is identical to $\{X_n \in g^{-1}(F)\}$.
Let $\overline{g^{-1}(F)}$ denote the topological closure of the pre-image in $\mathcal{X}$.
We examine which points belong to this closure. Suppose $x \in \overline{g^{-1}(F)} \cap C_g$. 
Since $x$ is in the closure, there exists a sequence of points $\{x_k\}_{k=1}^\infty \subseteq g^{-1}(F)$ such that $x_k \to x$.
Because $x \in C_g$, the mapping $g$ is continuous at $x$, which ensures that:

$$\lim_{k \to \infty} g(x_k) = g(x)$$

Each point $g(x_k)$ belongs to $F$. Because $F$ is a closed set, it contains all of its limit points. Therefore, the limit $g(x)$ must belong to $F$:

$$g(x) \in F \iff x \in g^{-1}(F)$$

This establishes the critical set-theoretic inclusion:

$$\overline{g^{-1}(F)} \cap C_g \subseteq g^{-1}(F)$$

Now evaluate the probability of the closure under the limiting measure of $X$. Since $P(X \in C_g) = 1$:

$$P\left( X \in \overline{g^{-1}(F)} \right) = P\left( X \in \overline{g^{-1}(F)} \cap C_g \right) \le P(X \in g^{-1}(F)) = P(g(X) \in F)$$

Next, because $\overline{g^{-1}(F)}$ is by construction a closed set in $\mathcal{X}$, and because $X_n \xrightarrow{d} X$, the Portmanteau Theorem applies directly to the sequence $X_n$:

$$\limsup_{n \to \infty} P\left( X_n \in \overline{g^{-1}(F)} \right) \le P\left( X \in \overline{g^{-1}(F)} \right)$$

Finally, since the pre-image is contained within its closure ($g^{-1}(F) \subseteq \overline{g^{-1}(F)}$):

$$\limsup_{n \to \infty} P(g(X_n) \in F) = \limsup_{n \to \infty} P(X_n \in g^{-1}(F)) \le \limsup_{n \to \infty} P\left( X_n \in \overline{g^{-1}(F)} \right) \le P\left( X \in \overline{g^{-1}(F)} \right) \le P(g(X) \in F)$$

Since this inequality holds for every closed set $F \subseteq \mathcal{Y}$, the Portmanteau Theorem guarantees that:

$$g(X_n) \xrightarrow{d} g(X) \quad \blacksquare$$

---

### Crucial Practical Applications of the CMT
1. **Continuous Invariance of Consistency**: If an estimator sequence $\hat{\theta}_n$ is consistent for a parameter vector $\boldsymbol{\theta}$ ($\hat{\theta}_n \xrightarrow{P} \boldsymbol{\theta}$) and $g$ is continuous at $\boldsymbol{\theta}$, then the plug-in estimator $g(\hat{\theta}_n)$ is automatically consistent for $g(\boldsymbol{\theta})$:
   $$g(\hat{\theta}_n) \xrightarrow{P} g(\boldsymbol{\theta})$$
2. **Quadratic Forms and Chi-Square Distributions**: If a sequence of random vectors $\mathbf{Z}_n \xrightarrow{d} \mathcal{N}_k(\mathbf{0}, \mathbf{I}_k)$, consider the quadratic form mapping $g(\mathbf{z}) = \mathbf{z}^T \mathbf{z} = \sum_{j=1}^k z_j^2$. The function $g: \mathbb{R}^k \to \mathbb{R}$ is a continuous polynomial across the entirety of $\mathbb{R}^k$. By the Continuous Mapping Theorem:
   $$\mathbf{Z}_n^T \mathbf{Z}_n \xrightarrow{d} \chi_k^2$$
   This single result forms the theoretical bedrock for Pearson's goodness-of-fit test, Neyman-Pearson generalized likelihood ratio tests, and Wald confidence ellipsoids.


## 8.3 Slutsky's Theorem: Operations on Mixed Sequences

One of the most persistent misconceptions in probability theory is the assumption that convergence in distribution behaves like ordinary algebra. Specifically, if $X_n \xrightarrow{d} X$ and $Y_n \xrightarrow{d} Y$, it is **NOT** true in general that:
- $X_n + Y_n \xrightarrow{d} X + Y$;
- $X_n Y_n \xrightarrow{d} X Y$;
- $X_n / Y_n \xrightarrow{d} X / Y$.

### Why Does Algebraic Combination Fail for Convergence in Distribution?
The failure occurs because convergence in distribution is a marginal property: it asserts only that the marginal CDFs $F_{X_n}(t) \to F_X(t)$ and $F_{Y_n}(t) \to F_Y(t)$ converge pointwise at continuity points. It specifies **nothing whatsoever** about the joint probability distribution or copula connecting $X_n$ and $Y_n$ on the underlying probability space!

To see this clearly, let $X \sim \mathcal{N}(0, 1)$ be a standard Gaussian variable, and define for all $n \ge 1$:

$$X_n = X \quad \text{and} \quad Y_n = -X$$

Both sequences converge trivially in distribution: $X_n \xrightarrow{d} \mathcal{N}(0, 1)$ and $Y_n \xrightarrow{d} \mathcal{N}(0, 1)$ (by Gaussian symmetry).
Now consider their sum:

$$X_n + Y_n = X + (-X) = 0 \quad \text{almost surely for all } n$$

The sum is deterministically zero: it converges in distribution to a point mass at zero ($\delta_0$).
However, if $X$ and $Y$ were independent standard Gaussians, their sum $X + Y$ would follow a Gaussian distribution $\mathcal{N}(0, 2)$ with variance 2! 
Because the joint dependence between $X_n$ and $Y_n$ is unconstrained, the distribution of $X_n + Y_n$ cannot be determined solely from the marginal limits of $X_n$ and $Y_n$.

---

### Evgeny Slutsky's Discovery: Degeneracy Restores Algebra

In 1925, the Ukrainian statistician Evgeny Slutsky proved that algebraic operations are fully restored if **one of the sequences converges in probability to a non-random constant**. Because a constant possesses zero stochastic variability, its joint distribution with any other random variable is uniquely determined.

### Theorem 8.2: Slutsky's Theorem
Let $\{X_n\}_{n=1}^\infty$ and $\{Y_n\}_{n=1}^\infty$ be sequences of random variables defined on a common probability space $(\Omega, \mathcal{F}, P)$. Suppose that:

$$X_n \xrightarrow{d} X \quad \text{and} \quad Y_n \xrightarrow{P} c$$

where $X$ is a random variable and $c \in \mathbb{R}$ is a non-random real scalar. Then:
1. **Summation**:
   $$X_n + Y_n \xrightarrow{d} X + c$$
2. **Multiplication**:
   $$X_n Y_n \xrightarrow{d} c X$$
3. **Division** (provided $c \ne 0$ and $P(Y_n = 0) \to 0$):
   $$\frac{X_n}{Y_n} \xrightarrow{d} \frac{X}{c}$$

---

### The Joint Convergence Lemma
The underlying engine that drives Slutsky's theorem is the following lemma concerning joint convergence in distribution.

**Lemma 8.1 (Joint Convergence with a Constant)**:
If $X_n \xrightarrow{d} X$ and $Y_n \xrightarrow{P} c$, then the joint bivariate sequence converges in distribution to the independent vector $(X, c)$:

$$(X_n, Y_n) \xrightarrow{d} (X, c)$$

Once Lemma 8.1 is established, Slutsky's theorem is simply a direct corollary of the Continuous Mapping Theorem (Theorem 8.1) applied to the continuous bivariate coordinate maps:
- Addition: $g(x, y) = x + y \implies g(X_n, Y_n) = X_n + Y_n \xrightarrow{d} X + c$;
- Multiplication: $g(x, y) = x \cdot y \implies g(X_n, Y_n) = X_n Y_n \xrightarrow{d} c X$;
- Division: $g(x, y) = x / y$ on $\mathbb{R} \times (\mathbb{R} \setminus \{0\}) \implies X_n / Y_n \xrightarrow{d} X / c$.

---

### Cornerstone Application: Student's $t$ Ratio in Non-Gaussian Samples
In introductory statistics, students learn that the one-sample $t$-statistic:

$$T_n = \frac{\bar{X}_n - \mu}{S_n / \sqrt{n}}$$

follows Student's $t$-distribution with $n-1$ degrees of freedom when the population is normal. What happens when the population is non-normal (for instance, Exponential, Gamma, or Uniform)?

Rewrite the $t$-statistic algebraically:

$$T_n = \frac{\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma}}{\frac{S_n}{\sigma}} = \frac{Z_n}{W_n}$$

We analyze the numerator and denominator:
1. **Numerator**: By the classical Lindeberg-Lévy Central Limit Theorem, since the observations are i.i.d. with finite variance $\sigma^2$:
   $$Z_n = \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \xrightarrow{d} Z \sim \mathcal{N}(0, 1)$$
2. **Denominator**: By the Strong Law of Large Numbers, the sample variance converges almost surely to the population variance: $S_n^2 \xrightarrow{\text{a.s.}} \sigma^2$, which implies $S_n^2 \xrightarrow{P} \sigma^2$. By the Continuous Mapping Theorem applied to $g(u) = \sqrt{u}/\sigma$:
   $$W_n = \frac{S_n}{\sigma} \xrightarrow{P} \frac{\sigma}{\sigma} = 1$$

Here the denominator converges in probability to the non-zero constant $c = 1$. Applying Slutsky's Theorem (part 3):

$$T_n = \frac{Z_n}{W_n} \xrightarrow{d} \frac{Z}{1} = Z \sim \mathcal{N}(0, 1)$$

Slutsky's theorem provides the rigorous, distribution-free mathematical justification for the universal validity of Student's $t$-tests and $t$-confidence intervals in large samples, even when the parent population deviates severely from normality.


## 8.4 The Univariate Delta Method: Asymptotic Linearization

In practical statistical inference, we frequently possess an estimator $T_n$ that is asymptotically normally distributed for a parameter $\theta$, but our scientific interest centers upon a smooth nonlinear function:

$$\gamma = g(\theta)$$

For instance:
- In Bernoulli trials, we estimate the success probability $p$ with $\hat{p}$, but require inference on the log-odds (logit): $g(p) = \ln(p / (1-p))$.
- In Poisson rate estimation, we estimate $\lambda$ with $\bar{X}$, but wish to infer the probability of zero events: $g(\lambda) = e^{-\lambda}$.
- In industrial reliability, we estimate mean time to failure $\theta$, but require the instantaneous hazard rate: $g(\theta) = 1/\theta$.
- In exponential dispersion modeling, we estimate variance $\sigma^2$ with $S^2$, but require the standard deviation: $g(\sigma^2) = \sqrt{\sigma^2}$.

The **Delta Method** provides the analytical mechanism for transferring the asymptotic normality of $T_n$ onto the nonlinear transform $g(T_n)$ through local Taylor linearization.

### Theorem 8.3: The Univariate First-Order Delta Method
Let $\{T_n\}_{n=1}^\infty$ be a sequence of scalar random variables satisfying a Central Limit Theorem:

$$\sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$$

where $\theta \in \mathbb{R}$ is the target parameter and $\sigma^2 > 0$ is the asymptotic variance.
Let $g: \mathbb{R} \to \mathbb{R}$ be a function differentiable at the point $\theta$, such that its first derivative is non-zero:

$$g'(\theta) \ne 0$$

Then:

$$\sqrt{n}(g(T_n) - g(\theta)) \xrightarrow{d} \mathcal{N}\left( 0, \, \left[ g'(\theta) \right]^2 \sigma^2 \right)$$

---

### Complete Rigorous Proof

**Proof**:
Since the function $g$ is differentiable at $\theta$, Taylor's theorem with Peano's form of the remainder implies that for all real numbers $t$ in a neighborhood of $\theta$:

$$g(t) = g(\theta) + g'(\theta)(t - \theta) + R(t)(t - \theta)$$

where the remainder function $R(t)$ satisfies:

$$\lim_{t \to \theta} R(t) = 0$$

To ensure $R(t)$ is well-defined everywhere on $\mathbb{R}$, we set $R(\theta) = 0$.
Now substitute the random variable $T_n$ for $t$:

$$g(T_n) - g(\theta) = g'(\theta)(T_n - \theta) + R(T_n)(T_n - \theta)$$

Multiply both sides of the identity by the normalizing scaling factor $\sqrt{n}$:

$$\sqrt{n}(g(T_n) - g(\theta)) = g'(\theta) \sqrt{n}(T_n - \theta) + R(T_n) \sqrt{n}(T_n - \theta)$$

We analyze each term on the right-hand side separately:

1. **The Linear Main Effect**:
   By hypothesis, $\sqrt{n}(T_n - \theta) \xrightarrow{d} X \sim \mathcal{N}(0, \sigma^2)$.
   Since $g'(\theta)$ is a non-random scalar constant, scalar multiplication of a Gaussian random variable scales its variance by the square of the multiplier:
   $$g'(\theta) \sqrt{n}(T_n - \theta) \xrightarrow{d} g'(\theta) X \sim \mathcal{N}\left( 0, \, [g'(\theta)]^2 \sigma^2 \right)$$

2. **The Higher-Order Remainder**:
   First, establish consistency of $T_n$. By hypothesis, $\sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$.
   Dividing by $\sqrt{n}$:
   $$T_n - \theta = \frac{1}{\sqrt{n}} \left( \sqrt{n}(T_n - \theta) \right)$$
   Since $1/\sqrt{n} \to 0$ deterministically, Slutsky's theorem implies $T_n - \theta \xrightarrow{d} 0$, which is equivalent to $T_n \xrightarrow{P} \theta$.
   Next, examine the remainder function $R(t)$. By definition, $R(t)$ is continuous at $t = \theta$ with $R(\theta) = 0$.
   Applying the Continuous Mapping Theorem (Theorem 8.1):
   $$R(T_n) \xrightarrow{P} R(\theta) = 0$$
   Now examine the product remainder term:
   $$Q_n = R(T_n) \cdot \left( \sqrt{n}(T_n - \theta) \right)$$
   Notice that $R(T_n) \xrightarrow{P} 0$ and $\sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$.
   Applying Slutsky's Theorem (part 2, multiplication):
   $$Q_n \xrightarrow{d} 0 \cdot \mathcal{N}(0, \sigma^2) = 0$$
   Because convergence in distribution to the constant 0 is equivalent to convergence in probability to 0:
   $$Q_n = R(T_n) \sqrt{n}(T_n - \theta) \xrightarrow{P} 0$$

3. **Synthesis via Slutsky's Summation**:
   We have decomposed the scaled error into:
   $$\sqrt{n}(g(T_n) - g(\theta)) = \underbrace{g'(\theta) \sqrt{n}(T_n - \theta)}_{\xrightarrow{d} \mathcal{N}(0, [g'(\theta)]^2 \sigma^2)} + \underbrace{Q_n}_{\xrightarrow{P} 0}$$
   Applying Slutsky's Theorem (part 1, summation):
   $$\sqrt{n}(g(T_n) - g(\theta)) \xrightarrow{d} \mathcal{N}\left( 0, \, [g'(\theta)]^2 \sigma^2 \right) + 0 = \mathcal{N}\left( 0, \, [g'(\theta)]^2 \sigma^2 \right) \quad \blacksquare$$

---

### Worked Pedagogical Example: Asymptotic Distribution of Log-Odds
Let $X_1, \dots, X_n \sim \text{i.i.d. } \text{Bernoulli}(p)$ with $p \in (0, 1)$. The sample proportion $\hat{p}_n = \bar{X}_n$ satisfies:

$$\sqrt{n}(\hat{p}_n - p) \xrightarrow{d} \mathcal{N}(0, p(1-p))$$

We wish to derive the asymptotic distribution of the empirical log-odds (logit transformation):

$$g(p) = \ln\left( \frac{p}{1-p} \right) = \ln(p) - \ln(1-p)$$

1. Compute the first derivative:
   $$g'(p) = \frac{1}{p} - \frac{1}{1-p}(-1) = \frac{1}{p} + \frac{1}{1-p} = \frac{(1-p) + p}{p(1-p)} = \frac{1}{p(1-p)}$$
2. Notice that for all $p \in (0, 1)$, $g'(p) = \frac{1}{p(1-p)} > 0$, so the first derivative never vanishes.
3. Apply the Delta Method formula for the asymptotic variance:
   $$V(p) = [g'(p)]^2 \sigma^2(p) = \left( \frac{1}{p(1-p)} \right)^2 \left( p(1-p) \right) = \frac{1}{p(1-p)}$$
4. Conclude the limiting distribution:
   $$\sqrt{n}\left( \ln\left(\frac{\hat{p}_n}{1-\hat{p}_n}\right) - \ln\left(\frac{p}{1-p}\right) \right) \xrightarrow{d} \mathcal{N}\left( 0, \, \frac{1}{p(1-p)} \right)$$

This elegant result provides the foundational large-sample theory for logistic regression and epidemiological odds ratio analysis.


## 8.5 The Second-Order Delta Method: Vanishing First Derivatives

A vital condition in Theorem 8.3 is that the first derivative must not vanish: $g'(\theta) \ne 0$. What occurs if $g'(\theta) = 0$?

When the first derivative vanishes, the linear term in the Taylor expansion disappears completely. As a consequence:
1. The first-order variation is zero: the estimator does not fluctuate at the standard $\sqrt{n}$ scale;
2. The leading stochastic behavior is governed by the **second derivative** (the local curvature of $g$);
3. The rate of convergence accelerates from $\sqrt{n}$ to $n$;
4. The limiting distribution is no longer Gaussian: it becomes a scaled **chi-square distribution**!

### Theorem 8.4: The Second-Order Delta Method
Let $\{T_n\}_{n=1}^\infty$ be a sequence of random variables satisfying:

$$\sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$$

Suppose $g: \mathbb{R} \to \mathbb{R}$ is twice continuously differentiable in an open neighborhood of $\theta$, such that:

$$g'(\theta) = 0 \quad \text{and} \quad g''(\theta) \ne 0$$

Then:

$$n\left( g(T_n) - g(\theta) \right) \xrightarrow{d} \frac{1}{2} g''(\theta) \sigma^2 \cdot \chi_1^2$$

where $\chi_1^2$ denotes a central chi-square distribution with 1 degree of freedom.

---

### Rigorous Proof

**Proof**:
Expand $g(T_n)$ in a second-order Taylor series around the point $\theta$:

$$g(T_n) = g(\theta) + g'(\theta)(T_n - \theta) + \frac{1}{2} g''(\theta)(T_n - \theta)^2 + R_2(T_n)(T_n - \theta)^2$$

where the second-order remainder satisfies $\lim_{t \to \theta} R_2(t) = 0$, with $R_2(\theta) = 0$.
Since $g'(\theta) = 0$ by hypothesis, the linear term drops out completely:

$$g(T_n) - g(\theta) = \frac{1}{2} g''(\theta)(T_n - \theta)^2 + R_2(T_n)(T_n - \theta)^2$$

Multiply both sides of the identity by the quadratic normalizing factor $n = (\sqrt{n})^2$:

$$n\left( g(T_n) - g(\theta) \right) = \frac{1}{2} g''(\theta) \left[ \sqrt{n}(T_n - \theta) \right]^2 + R_2(T_n) \left[ \sqrt{n}(T_n - \theta) \right]^2$$

We analyze each component:
1. By hypothesis, $\sqrt{n}(T_n - \theta) \xrightarrow{d} Z \sim \mathcal{N}(0, \sigma^2)$. We can write $Z = \sigma U$, where $U \sim \mathcal{N}(0, 1)$ is a standard normal variable.
   Consider the squaring function $h(u) = u^2$. This mapping is continuous across the entire real line.
   Applying the Continuous Mapping Theorem (Theorem 8.1):
   $$\left[ \sqrt{n}(T_n - \theta) \right]^2 \xrightarrow{d} Z^2 = (\sigma U)^2 = \sigma^2 U^2 = \sigma^2 \chi_1^2$$
   Multiplying by the non-random constant $\frac{1}{2}g''(\theta)$:
   $$\frac{1}{2} g''(\theta) \left[ \sqrt{n}(T_n - \theta) \right]^2 \xrightarrow{d} \frac{1}{2} g''(\theta) \sigma^2 \chi_1^2$$

2. Since $T_n \xrightarrow{P} \theta$ and $R_2$ is continuous at $\theta$ with $R_2(\theta) = 0$, the Continuous Mapping Theorem ensures that $R_2(T_n) \xrightarrow{P} 0$.
   Because $[\sqrt{n}(T_n - \theta)]^2 \xrightarrow{d} \sigma^2 \chi_1^2$, Slutsky's Theorem (multiplication by a sequence converging in probability to zero) guarantees that:
   $$R_2(T_n) \left[ \sqrt{n}(T_n - \theta) \right]^2 \xrightarrow{P} 0$$

Applying Slutsky's Theorem (summation) to the two components yields:

$$n\left( g(T_n) - g(\theta) \right) \xrightarrow{d} \frac{1}{2} g''(\theta) \sigma^2 \chi_1^2 + 0 = \frac{1}{2} g''(\theta) \sigma^2 \chi_1^2 \quad \blacksquare$$

---

### Physical and Geometric Interpretation
The second-order delta method reveals an essential geometric principle:
- When $g'(\theta) \ne 0$, the graph of $g$ has a non-zero slope at $\theta$. Locally, the function acts as an affine transformation, preserving the Gaussian shape of the input fluctuations.
- When $g'(\theta) = 0$, $\theta$ is an extremum (local minimum or maximum) or an inflection point. For example, if $g$ has a local minimum, any fluctuation in $T_n$ (positive or negative) produces a strictly positive deviation in $g(T_n) - g(\theta) \ge 0$. Because negative deviations are impossible, the limiting distribution **cannot** be Gaussian; it must be one-sided, which is precisely why the non-negative $\chi_1^2$ distribution emerges.


## 8.6 The Multivariate Delta Method: Vectorial Transformations and Jacobians

In econometric modeling, biostatistics, and multivariate analysis, statistical inference rarely involves isolated univariate parameters. Instead, estimators typically form random vectors comprising sample means, variances, covariances, and regression coefficients. The **Multivariate Delta Method** generalizes Taylor linearization to smooth mappings from $\mathbb{R}^k$ to $\mathbb{R}^m$.

### Theorem 8.5: The Multivariate Delta Method
Let $\{\mathbf{T}_n\}_{n=1}^\infty$ be a sequence of $k$-dimensional random vectors:

$$\mathbf{T}_n = \begin{pmatrix} T_{n1} \\ T_{n2} \\ \vdots \\ T_{nk} \end{pmatrix}$$

satisfying a multivariate Central Limit Theorem:

$$\sqrt{n}(\mathbf{T}_n - \boldsymbol{\theta}) \xrightarrow{d} \mathcal{N}_k(\mathbf{0}, \boldsymbol{\Sigma})$$

where $\boldsymbol{\theta} \in \mathbb{R}^k$ is the parameter vector and $\boldsymbol{\Sigma} \in \mathbb{R}^{k \times k}$ is a positive semi-definite covariance matrix.

Let $\mathbf{g}: \mathbb{R}^k \to \mathbb{R}^m$ be a vector-valued function:

$$\mathbf{g}(\mathbf{t}) = \begin{pmatrix} g_1(\mathbf{t}) \\ g_2(\mathbf{t}) \\ \vdots \\ g_m(\mathbf{t}) \end{pmatrix}$$

Suppose that each coordinate function $g_j: \mathbb{R}^k \to \mathbb{R}$ is continuously differentiable in an open neighborhood of $\boldsymbol{\theta}$.
Define the $m \times k$ **Jacobian matrix** evaluated at $\boldsymbol{\theta}$:

$$\mathbf{D}_{\mathbf{g}}(\boldsymbol{\theta}) = \left. \begin{pmatrix}
\frac{\partial g_1}{\partial t_1} & \frac{\partial g_1}{\partial t_2} & \cdots & \frac{\partial g_1}{\partial t_k} \\
\frac{\partial g_2}{\partial t_1} & \frac{\partial g_2}{\partial t_2} & \cdots & \frac{\partial g_2}{\partial t_k} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial g_m}{\partial t_1} & \frac{\partial g_m}{\partial t_2} & \cdots & \frac{\partial g_m}{\partial t_k}
\end{pmatrix} \right|_{\mathbf{t} = \boldsymbol{\theta}}$$

Then:

$$\sqrt{n}\left( \mathbf{g}(\mathbf{T}_n) - \mathbf{g}(\boldsymbol{\theta}) \right) \xrightarrow{d} \mathcal{N}_m\left( \mathbf{0}, \, \mathbf{D}_{\mathbf{g}}(\boldsymbol{\theta}) \, \boldsymbol{\Sigma} \, \mathbf{D}_{\mathbf{g}}(\boldsymbol{\theta})^T \right)$$

---

### The Scalar Transformation Case ($m = 1$)
When $g: \mathbb{R}^k \to \mathbb{R}$ produces a single scalar output, the Jacobian matrix degenerates into the $1 \times k$ gradient row vector:

$$\nabla g(\boldsymbol{\theta})^T = \left( \frac{\partial g}{\partial \theta_1}, \frac{\partial g}{\partial \theta_2}, \dots, \frac{\partial g}{\partial \theta_k} \right)$$

The asymptotic covariance matrix collapses to a scalar quadratic form:

$$\sigma_g^2 = \nabla g(\boldsymbol{\theta})^T \boldsymbol{\Sigma} \nabla g(\boldsymbol{\theta}) = \sum_{i=1}^k \sum_{j=1}^k \frac{\partial g}{\partial \theta_i} \frac{\partial g}{\partial \theta_j} \Sigma_{ij}$$

And the limiting distribution is univariate normal:

$$\sqrt{n}(g(\mathbf{T}_n) - g(\boldsymbol{\theta})) \xrightarrow{d} \mathcal{N}\left( 0, \, \nabla g(\boldsymbol{\theta})^T \boldsymbol{\Sigma} \nabla g(\boldsymbol{\theta}) \right)$$

---

### In-Depth Application: The Odds Ratio in $2 \times 2$ Contingency Tables
In epidemiological case-control studies, researchers examine whether exposure to an environmental risk factor associates with disease occurrence. Consider independent binomial samples of disease cases ($n_1$ subjects, success probability $p_1$) and disease-free controls ($n_2$ subjects, success probability $p_2$). The population **odds ratio** is defined as:

$$\psi = \frac{p_1 / (1 - p_1)}{p_2 / (1 - p_2)} = \frac{p_1 (1 - p_2)}{p_2 (1 - p_1)}$$

Because the sample odds ratio $\hat{\psi} = \frac{\hat{p}_1(1 - \hat{p}_2)}{\hat{p}_2(1 - \hat{p}_1)}$ is highly skewed in finite samples, researchers work with the **log-odds ratio**:

$$g(p_1, p_2) = \ln \psi = \ln(p_1) - \ln(1 - p_1) - \ln(p_2) + \ln(1 - p_2)$$

Assume that as the total sample size $N = n_1 + n_2 \to \infty$, the sample proportions stabilize: $n_1 / N \to \lambda_1 \in (0, 1)$ and $n_2 / N \to \lambda_2 \in (0, 1)$.
The vector of sample proportions $\hat{\mathbf{p}} = (\hat{p}_1, \hat{p}_2)^T$ satisfies the bivariate CLT:

$$\sqrt{N}\left( \begin{pmatrix} \hat{p}_1 \\ \hat{p}_2 \end{pmatrix} - \begin{pmatrix} p_1 \\ p_2 \end{pmatrix} \right) \xrightarrow{d} \mathcal{N}_2\left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \, \begin{pmatrix} \frac{p_1(1-p_1)}{\lambda_1} & 0 \\ 0 & \frac{p_2(1-p_2)}{\lambda_2} \end{pmatrix} \right)$$

Compute the gradient of the log-odds ratio:

$$\nabla g(p_1, p_2) = \begin{pmatrix} \frac{\partial g}{\partial p_1} \\ \frac{\partial g}{\partial p_2} \end{pmatrix} = \begin{pmatrix} \frac{1}{p_1(1-p_1)} \\ -\frac{1}{p_2(1-p_2)} \end{pmatrix}$$

Apply the Multivariate Delta Method quadratic form:

$$\sigma_{\ln \psi}^2 = \nabla g^T \boldsymbol{\Sigma} \nabla g = \left( \frac{1}{p_1(1-p_1)} \right)^2 \frac{p_1(1-p_1)}{\lambda_1} + \left( -\frac{1}{p_2(1-p_2)} \right)^2 \frac{p_2(1-p_2)}{\lambda_2} = \frac{1}{\lambda_1 p_1(1-p_1)} + \frac{1}{\lambda_2 p_2(1-p_2)}$$

Expressing this back in terms of the finite sample sizes $n_1 = \lambda_1 N$ and $n_2 = \lambda_2 N$, the large-sample variance of $\ln \hat{\psi}$ is:

$$\text{Var}(\ln \hat{\psi}) \approx \frac{1}{n_1 \hat{p}_1(1 - \hat{p}_1)} + \frac{1}{n_2 \hat{p}_2(1 - \hat{p}_2)}$$

In terms of the cell counts $a, b, c, d$ of the contingency table (where $a = n_1 \hat{p}_1$, $b = n_1(1-\hat{p}_1)$, $c = n_2 \hat{p}_2$, and $d = n_2(1-\hat{p}_2)$):

$$\widehat{\text{Var}}(\ln \hat{\psi}) = \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}$$

This famous formula, known as **Woolf's formula** (1955), allows clinicians to construct reliable confidence intervals for odds ratios across all medical literature:

$$\text{CI}_{1-\alpha}(\psi) = \exp\left( \ln \hat{\psi} \pm z_{1-\alpha/2} \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}} \right)$$

---

### In-Depth Application: Asymptotic Distribution of Pearson Correlation
For an i.i.d. bivariate sample $(X_1, Y_1), \dots, (X_n, Y_n)$ with standardized variables ($\mu_X = \mu_Y = 0$, $\sigma_X^2 = \sigma_Y^2 = 1$, and correlation $\rho$), the vector of second moments $\mathbf{T}_n = (\frac{1}{n}\sum X_i^2, \frac{1}{n}\sum Y_i^2, \frac{1}{n}\sum X_i Y_i)^T$ converges in probability to $\boldsymbol{\theta} = (1, 1, \rho)^T$.
The correlation mapping is $g(u, v, w) = \frac{w}{\sqrt{uv}}$.
The gradient vector evaluated at $(1, 1, \rho)$ is:

$$\nabla g(1, 1, \rho) = \begin{pmatrix} -\frac{\rho}{2} \\ -\frac{\rho}{2} \\ 1 \end{pmatrix}$$

Under bivariate normality, the covariance matrix of the second moments is:

$$\boldsymbol{\Sigma} = \begin{pmatrix} 2 & 2\rho^2 & 2\rho \\ 2\rho^2 & 2 & 2\rho \\ 2\rho & 2\rho & 1 + \rho^2 \end{pmatrix}$$

Evaluating the quadratic form $\nabla g^T \boldsymbol{\Sigma} \nabla g$ yields:

$$\sigma_r^2 = (1 - \rho^2)^2$$

Thus, under bivariate Gaussianity:

$$\sqrt{n}(r_n - \rho) \xrightarrow{d} \mathcal{N}\left( 0, \, (1 - \rho^2)^2 \right)$$

This demonstrates the power of the Multivariate Delta Method in decomposing complex nonlinear dependencies into clean quadratic forms.


## 8.7 Variance Stabilizing Transformations (VST)

In many parametric families of distributions, the asymptotic variance of an estimator is not a constant, but depends functionally upon the unknown target parameter:

$$\text{Var}(\bar{X}_n) \approx \frac{\sigma^2(\mu)}{n}$$

This parameter dependence introduces practical complications in statistical inference:
1. **Wald Confidence Intervals**: Standard Wald intervals $\bar{X}_n \pm z_{1-\alpha/2} \frac{\sigma(\bar{X}_n)}{\sqrt{n}}$ exhibit poor empirical coverage in small or moderate samples because fluctuations in the denominator compound estimation errors in the numerator;
2. **Analysis of Variance (ANOVA)**: Classical linear models assume homoscedasticity (constant error variance across treatment groups). If group variances vary with group means, standard $F$-tests suffer severe size distortions;
3. **Hypothesis Testing**: Test statistic distributions depend on nuisance parameters under the null and alternative hypotheses.

A **Variance Stabilizing Transformation (VST)** is a smooth, invertible function $g: \mathbb{R} \to \mathbb{R}$ chosen so that the asymptotic variance of $g(\bar{X}_n)$ becomes a **universal constant**, completely independent of the unknown parameter $\mu$!

### Derivation of the Variance Stabilizing Differential Equation
By the univariate Delta Method (Theorem 8.3), for any differentiable function $g$:

$$\sqrt{n}(g(\bar{X}_n) - g(\mu)) \xrightarrow{d} \mathcal{N}\left( 0, \, [g'(\mu)]^2 \sigma^2(\mu) \right)$$

To achieve variance stabilization, we demand that the asymptotic variance be identically equal to a constant $c^2 > 0$ for all possible values of $\mu$ in the parameter space:

$$[g'(\mu)]^2 \sigma^2(\mu) = c^2$$

Taking the positive square root:

$$g'(\mu) = \frac{c}{\sigma(\mu)}$$

Integrating both sides with respect to $\mu$ yields the general formula for the Variance Stabilizing Transformation:

$$g(\mu) = c \int \frac{1}{\sigma(\mu)} \, d\mu$$

---

### The Canonical Transformations of Mathematical Statistics

#### 1. The Poisson Distribution (Square-Root Transform)
Let $X_1, \dots, X_n \sim \text{i.i.d. } \text{Poisson}(\lambda)$ with $\lambda > 0$.
The mean and variance are equal: $\mathbb{E}[X] = \lambda$ and $\text{Var}(X) = \lambda$, so $\sigma(\lambda) = \sqrt{\lambda}$.
Apply the VST integral with $c = 1$:

$$g(\lambda) = \int \frac{1}{\sqrt{\lambda}} \, d\lambda = 2\sqrt{\lambda}$$

Check the asymptotic distribution using the Delta Method:
$g'(\lambda) = 1/\sqrt{\lambda}$. The asymptotic variance is:

$$[g'(\lambda)]^2 \sigma^2(\lambda) = \left( \frac{1}{\sqrt{\lambda}} \right)^2 \lambda = \frac{1}{\lambda} \cdot \lambda = 1$$

Thus:

$$\sqrt{n}\left( 2\sqrt{\bar{X}_n} - 2\sqrt{\lambda} \right) \xrightarrow{d} \mathcal{N}(0, 1)$$

Or dividing by 2:

$$\sqrt{n}\left( \sqrt{\bar{X}_n} - \sqrt{\lambda} \right) \xrightarrow{d} \mathcal{N}\left( 0, \frac{1}{4} \right)$$

The asymptotic variance is strictly $1/4$, completely free of the unknown parameter $\lambda$!

---

#### 2. The Bernoulli / Binomial Distribution (Arcsine Square-Root Transform)
Let $X_1, \dots, X_n \sim \text{i.i.d. } \text{Bernoulli}(p)$ with $p \in (0, 1)$.
Here $\mathbb{E}[X] = p$ and $\sigma(p) = \sqrt{p(1-p)}$.
Apply the VST integral with $c = 1$:

$$g(p) = \int \frac{1}{\sqrt{p(1-p)}} \, dp$$

Make the trigonometric substitution $p = \sin^2(\theta)$, so $dp = 2\sin(\theta)\cos(\theta)\,d\theta$ and $\sqrt{p(1-p)} = \sin(\theta)\cos(\theta)$:

$$g(p) = \int \frac{2\sin(\theta)\cos(\theta)}{\sin(\theta)\cos(\theta)} \, d\theta = 2\theta = 2\arcsin(\sqrt{p})$$

Applying the Delta Method:

$$\sqrt{n}\left( 2\arcsin(\sqrt{\hat{p}_n}) - 2\arcsin(\sqrt{p}) \right) \xrightarrow{d} \mathcal{N}(0, 1)$$

Or setting $h(p) = \arcsin(\sqrt{p})$:

$$\sqrt{n}\left( \arcsin(\sqrt{\hat{p}_n}) - \arcsin(\sqrt{p}) \right) \xrightarrow{d} \mathcal{N}\left( 0, \frac{1}{4} \right)$$

This celebrated transformation, introduced by R. A. Fisher, is the standard tool used across meta-analysis and bioassay studies to stabilize variances of proportions near 0 or 1.

---

#### 3. Pearson Correlation: Fisher's $z$-Transformation
For bivariate Gaussian observations with population correlation $\rho \in (-1, 1)$, the sample correlation $r_n$ has asymptotic standard deviation $\sigma(\rho) = 1 - \rho^2$.
Apply the VST integral with $c = 1$:

$$g(\rho) = \int \frac{1}{1 - \rho^2} \, d\rho = \frac{1}{2}\ln\left( \frac{1+\rho}{1-\rho} \right) = \text{arctanh}(\rho)$$

Applying the Delta Method:

$$\sqrt{n}\left( \text{arctanh}(r_n) - \text{arctanh}(\rho) \right) \xrightarrow{d} \mathcal{N}(0, 1)$$

Fisher's $z$-transform eliminates the severe skewness of the sample correlation coefficient when $|\rho|$ is close to 1, rendering hypothesis tests on correlation coefficients robust and analytically tractable.

---

#### 4. The Negative Binomial Distribution (Inverse Hyperbolic Sine Transform)
In count models with overdispersion (such as RNA sequencing and ecology), counts follow a Negative Binomial distribution with mean $\mu$ and dispersion parameter $r > 0$, where $\text{Var}(X) = \mu + \frac{\mu^2}{r}$.
The variance function is $\sigma(\mu) = \sqrt{\mu(1 + \mu/r)}$.
Apply the VST integral:

$$g(\mu) = \int \frac{1}{\sqrt{\mu + \mu^2 / r}} \, d\mu = 2\sqrt{r} \ln\left( \sqrt{\frac{\mu}{r}} + \sqrt{1 + \frac{\mu}{r}} \right) = 2\sqrt{r} \, \text{arcsinh}\left( \sqrt{\frac{\mu}{r}} \right)$$

This transformation stabilizes the variance of overdispersed sequencing reads across varying library depths.

---

#### 5. Anscombe and Freeman-Tukey Second-Order Refinements
While standard first-order VSTs ensure asymptotic variance constancy at rate $O(1/\sqrt{n})$, finite-sample residual variance drift remains at rate $O(1/n)$.
To eliminate this second-order drift, Francis Anscombe (1948) and Murray Freeman and John Tukey (1950) introduced exact additive continuity adjustments:
- **Anscombe's Poisson Transform**: $A(X) = 2\sqrt{X + 3/8}$, which achieves $\text{Var}(A(X)) = 1 + O(1/\lambda^2)$ instead of $1 + O(1/\lambda)$;
- **Freeman-Tukey Binomial Transform**: $FT(X) = \arcsin\sqrt{\frac{X}{n+1}} + \arcsin\sqrt{\frac{X+1}{n+1}}$, which maintains nominal variance $1/(n+0.5)$ across extreme boundary probabilities $p \in (0.01, 0.99)$.


## 8.8 Asymptotic Relative Efficiency (ARE) and Pitman Efficiency

A central task of mathematical statistics is providing objective, mathematically rigorous criteria for selecting the best estimator among multiple competing alternatives. In finite samples, the Mean Squared Error (MSE) often depends sensitively upon the specific sample size $n$ and the true unknown parameter value $\theta$, precluding a globally optimal choice. **Asymptotic Relative Efficiency (ARE)** resolves this ambiguity by examining the comparative performance of estimators in large samples.

### Formal Definition of Pitman ARE
Let $T_{1, n}$ and $T_{2, n}$ be two consistent estimators of a parameter $\theta$, satisfying root-$n$ Central Limit Theorems:

$$\sqrt{n}(T_{1, n} - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma_1^2(\theta)) \quad \text{and} \quad \sqrt{n}(T_{2, n} - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma_2^2(\theta))$$

where $\sigma_1^2(\theta) > 0$ and $\sigma_2^2(\theta) > 0$ are the respective asymptotic variances.

The **Asymptotic Relative Efficiency** of $T_{1, n}$ relative to $T_{2, n}$ (in the sense of E. J. G. Pitman) is defined as the reciprocal ratio of their asymptotic variances:

$$\text{ARE}(T_1, T_2) = \frac{\sigma_2^2(\theta)}{\sigma_1^2(\theta)}$$

### Operational Sample-Size Interpretation
The operational power of Pitman ARE lies in its direct interpretation in terms of sample size economy:
Suppose an experimenter wishes to achieve a specified mean squared error tolerance $\text{MSE}_0$.
- Using estimator $T_1$, the sample size $n_1$ required satisfies $\sigma_1^2 / n_1 \approx \text{MSE}_0$;
- Using estimator $T_2$, the sample size $n_2$ required satisfies $\sigma_2^2 / n_2 \approx \text{MSE}_0$.

Equating the two expressions:

$$\frac{\sigma_1^2}{n_1} \approx \frac{\sigma_2^2}{n_2} \implies \lim_{\text{MSE}_0 \to 0} \frac{n_2}{n_1} = \frac{\sigma_2^2}{\sigma_1^2} = \text{ARE}(T_1, T_2)$$

- If $\text{ARE}(T_1, T_2) = 2.0$, estimator $T_1$ requires only **half as many data points** ($n_1 = 0.5 n_2$) as estimator $T_2$ to achieve the same estimation precision!
- If $\text{ARE}(T_1, T_2) = 0.80$, estimator $T_1$ requires $25\%$ more data points ($n_1 = 1.25 n_2$) than estimator $T_2$.

---

### Other Modes of Efficiency: Bahadur and Hodges-Lehmann
While Pitman ARE evaluates efficiency under local $1/\sqrt{n}$ neighborhoods, two other asymptotic efficiency frameworks exist:
1. **Bahadur Efficiency**: Evaluates the exponential decay rate of the $p$-value under a fixed alternative hypothesis as $n \to \infty$. It measures how rapidly the type II error probability collapses to zero.
2. **Hodges-Lehmann Efficiency**: Compares the exponential rate of decay of the power function for a fixed significance level.

Under standard regular models, these distinct efficiency criteria generally lead to the exact same preference ordering of estimators, demonstrating the foundational unity of asymptotic theory.

---

### Hodges' Superefficiency and Le Cam's Phenomenon
In 1951, Joseph Hodges constructed a famous counterexample to the conjecture that no estimator could have smaller asymptotic variance than the Cramér-Rao lower bound everywhere.
Let $X_1, \dots, X_n \sim \text{i.i.d. } \mathcal{N}(\theta, 1)$. The sample mean $\bar{X}_n$ has asymptotic variance 1.
Define Hodges' estimator:

$$T_n = \begin{cases} \bar{X}_n & \text{if } |\bar{X}_n| > n^{-1/4} \\ 0 & \text{if } |\bar{X}_n| \le n^{-1/4} \end{cases}$$

- If $\theta \ne 0$: by the Law of Large Numbers, $|\bar{X}_n| \to |\theta| > 0$. For large $n$, $|\bar{X}_n| > n^{-1/4}$ with probability tending to 1. Thus $\sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, 1)$, matching the MLE.
- If $\theta = 0$: $\sqrt{n} \bar{X}_n = O_P(1)$, so $|\bar{X}_n| = O_P(n^{-1/2}) \le n^{-1/4}$ with probability tending to 1. Thus $T_n = 0$ with probability 1, and $\sqrt{n}(T_n - 0) \xrightarrow{P} 0$. The asymptotic variance at $\theta = 0$ is **zero**!

Hodges' estimator appears to beat the Cramér-Rao bound! However, Lucien Le Cam (1953) resolved this apparent paradox:
1. Superefficiency can occur only on a subset of the parameter space of **Lebesgue measure zero** (here, the single point $\theta = 0$).
2. In a $1/\sqrt{n}$ neighborhood of the superefficient point (e.g. $\theta_n = h / \sqrt{n}$), the maximum risk of Hodges' estimator blows up, exceeding the minimax risk of the sample mean by an arbitrarily large factor!
This led to the **Hájek-Le Cam Asymptotic Minimax Theorem**, proving that regular estimators (whose distributions vary smoothly under $1/\sqrt{n}$ perturbations) cannot beat the Cramér-Rao bound anywhere.


## 8.9 Asymptotic Theory of Maximum Likelihood Estimators and the Trinity of Classical Tests

The asymptotic theorems developed throughout this unit reach their most powerful synthesis in the asymptotic theory of **Maximum Likelihood Estimation (MLE)** and the associated trinity of hypothesis tests. Under standard Cramér-Rao regularity conditions, the maximum likelihood estimator $\hat{\theta}_n$ possesses three extraordinary large-sample properties:

### 1. Strong Consistency ($\hat{\theta}_n \xrightarrow{\text{a.s.}} \theta_0$)
Let $X_1, \dots, X_n \sim \text{i.i.d. } f(x; \theta_0)$. The normalized log-likelihood is:

$$\frac{1}{n}\ell_n(\theta) = \frac{1}{n}\sum_{i=1}^n \ln f(X_i; \theta)$$

By the Strong Law of Large Numbers (Unit 7), for each fixed $\theta$:

$$\frac{1}{n}\ell_n(\theta) \xrightarrow{\text{a.s.}} \mathbb{E}_{\theta_0}[\ln f(X; \theta)]$$

Consider the difference between the expected log-likelihood at $\theta$ and at the true parameter $\theta_0$:

$$\mathbb{E}_{\theta_0}\left[ \ln\left( \frac{f(X; \theta)}{f(X; \theta_0)} \right) \right] = -D_{KL}(f_{\theta_0} \parallel f_\theta)$$

where $D_{KL}$ is the Kullback-Leibler divergence. By Jensen's inequality applied to the strictly concave logarithm function:

$$\mathbb{E}_{\theta_0}\left[ \ln\left( \frac{f(X; \theta)}{f(X; \theta_0)} \right) \right] \le \ln\left( \mathbb{E}_{\theta_0}\left[ \frac{f(X; \theta)}{f(X; \theta_0)} \right] \right) = \ln\left( \int f(x; \theta) \, dx \right) = \ln(1) = 0$$

Equality holds if and only if $f(x; \theta) = f(x; \theta_0)$ almost everywhere, which by parameter identifiability requires $\theta = \theta_0$. Thus, the population objective function possesses a unique global maximum at $\theta_0$. By uniform convergence of the log-likelihood over compact parameter spaces, the sample maximizer must converge almost surely to the population maximizer:

$$\hat{\theta}_n \xrightarrow{\text{a.s.}} \theta_0$$

---

### 2. Asymptotic Normality via Taylor Expansion
Because $\hat{\theta}_n$ maximizes the smooth log-likelihood function, it satisfies the score equation:

$$S_n(\hat{\theta}_n) = \ell_n'(\hat{\theta}_n) = 0$$

Expand the score function in a first-order Taylor series around the true parameter $\theta_0$:

$$0 = S_n(\hat{\theta}_n) = S_n(\theta_0) + S_n''(\theta^*)(\hat{\theta}_n - \theta_0)$$

where $\theta^*$ lies on the segment connecting $\hat{\theta}_n$ and $\theta_0$.
Rearranging:

$$\sqrt{n}(\hat{\theta}_n - \theta_0) = \frac{\frac{1}{\sqrt{n}} S_n(\theta_0)}{-\frac{1}{n} \ell_n''(\theta^*)}$$

We analyze the numerator and denominator:
- **Numerator**: The score at $\theta_0$ is a sum of i.i.d. zero-mean terms: $S_n(\theta_0) = \sum_{i=1}^n \frac{\partial}{\partial \theta}\ln f(X_i; \theta_0)$.
  The variance of each term is the Fisher Information $I_1(\theta_0) = \mathbb{E}[(\frac{\partial}{\partial \theta}\ln f(X; \theta_0))^2]$.
  By the Lindeberg-Lévy Central Limit Theorem:
  $$\frac{1}{\sqrt{n}} S_n(\theta_0) \xrightarrow{d} \mathcal{N}\left( 0, I_1(\theta_0) \right)$$

- **Denominator**: By the Law of Large Numbers and consistency of $\theta^* \xrightarrow{P} \theta_0$:
  $$-\frac{1}{n}\ell_n''(\theta^*) = -\frac{1}{n}\sum_{i=1}^n \frac{\partial^2}{\partial \theta^2}\ln f(X_i; \theta^*) \xrightarrow{P} \mathbb{E}_{\theta_0}\left[ -\frac{\partial^2}{\partial \theta^2}\ln f(X; \theta_0) \right] = I_1(\theta_0)$$

Applying Slutsky's Theorem (part 3, division):

$$\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} \frac{\mathcal{N}(0, I_1(\theta_0))}{I_1(\theta_0)} = \mathcal{N}\left( 0, \, \frac{I_1(\theta_0)}{[I_1(\theta_0)]^2} \right) = \mathcal{N}\left( 0, \, \frac{1}{I_1(\theta_0)} \right)$$

---

### 3. Asymptotic Efficiency and Attainment of the Cramér-Rao Bound
The Cramér-Rao Lower Bound asserts that for any unbiased estimator $T_n$, its variance satisfies $\text{Var}(T_n) \ge \frac{1}{n I_1(\theta_0)}$.
Because the asymptotic variance of $\sqrt{n}(\hat{\theta}_n - \theta_0)$ is identically equal to $1/I_1(\theta_0)$, the Maximum Likelihood Estimator achieves the lowest possible asymptotic variance among all regular estimators. It is **Best Asymptotically Normal (BAN)**.

---

### 4. The Classical Trinity of Hypothesis Tests
Consider testing the null hypothesis $H_0: \boldsymbol{\theta} = \boldsymbol{\theta}_0$ against $H_1: \boldsymbol{\theta} \ne \boldsymbol{\theta}_0$ for a $p$-dimensional parameter vector. Asymptotic theory provides three celebrated, asymptotically equivalent test statistics:
1. **The Likelihood Ratio Test (Wilks' Theorem)**:
   $$\Lambda_n = 2\left( \ell_n(\hat{\boldsymbol{\theta}}_n) - \ell_n(\boldsymbol{\theta}_0) \right) \xrightarrow{d} \chi_p^2$$
2. **The Wald Test**:
   $$W_n = (\hat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}_0)^T \left[ \mathbf{I}_n(\hat{\boldsymbol{\theta}}_n) \right] (\hat{\boldsymbol{\theta}}_n - \boldsymbol{\theta}_0) \xrightarrow{d} \chi_p^2$$
3. **The Score / Lagrange Multiplier Test (Rao's Score Test)**:
   $$R_n = \mathbf{S}_n(\boldsymbol{\theta}_0)^T \left[ \mathbf{I}_n(\boldsymbol{\theta}_0) \right]^{-1} \mathbf{S}_n(\boldsymbol{\theta}_0) \xrightarrow{d} \chi_p^2$$

Under local contiguous alternatives $\boldsymbol{\theta}_n = \boldsymbol{\theta}_0 + \mathbf{h}/\sqrt{n}$, all three test statistics converge in distribution to the same non-central chi-square distribution $\chi_p^2(\delta)$, where the non-centrality parameter is $\delta = \mathbf{h}^T \mathbf{I}_1(\boldsymbol{\theta}_0) \mathbf{h}$. Thus, they share identical asymptotic Pitman power!

### Higher-Order Asymptotics and Bartlett Adjustments

In finite samples of small or moderate size ($n \in [15, 50]$), the classical asymptotic $\chi_p^2$ approximation for the Likelihood Ratio Test statistic $\Lambda_n = 2(\ell_n(\hat{\boldsymbol{\theta}}_n) - \ell_n(\boldsymbol{\theta}_0))$ can suffer from noticeable size distortion (rejecting the null hypothesis more frequently than the nominal significance level $\alpha$).

In 1937, M. S. Bartlett discovered that the expectation of the likelihood ratio statistic under the null hypothesis deviates from $p$ by an order $O(n^{-1})$ term:

$$\mathbb{E}[\Lambda_n] = p \left( 1 + \frac{b}{n} + O(n^{-2}) \right)$$

where $b$ is a constant depending upon the first four derivatives of the log-likelihood function.
Bartlett showed that dividing the test statistic by its mean correction factor:

$$\Lambda_n^* = \frac{\Lambda_n}{1 + \frac{b}{n}}$$

removes the first-order error completely! The cumulative distribution function of the **Bartlett-corrected statistic** $\Lambda_n^*$ satisfies:

$$P(\Lambda_n^* \le x) = P(\chi_p^2 \le x) + O(n^{-2})$$

Notice that the error term drops from $O(n^{-1})$ all the way to $O(n^{-2})$! A sample of size $n = 20$ with Bartlett correction often attains the same distribution precision as an uncorrected sample of size $n = 400$. This remarkable result demonstrates how higher-order asymptotic theory bridges the gap between asymptotic elegance and small-sample empirical reality.



## Fully worked question 1: Detailed Step-by-Step Proof of Slutsky's Theorem

### Question
Let $\{X_n\}_{n=1}^\infty$ and $\{Y_n\}_{n=1}^\infty$ be sequences of real-valued random variables defined upon a common probability space $(\Omega, \mathcal{F}, P)$. Let $X$ be a random variable, and let $c \in \mathbb{R}$ be a fixed, non-random real constant.
Assume that:

$$X_n \xrightarrow{d} X \quad \text{and} \quad Y_n \xrightarrow{P} c$$

1. Rigorously prove that $X_n + Y_n \xrightarrow{d} X + c$ using distribution function bounds and $\epsilon$-decompositions.
2. Prove that if $Y_n \xrightarrow{P} 0$, then $X_n Y_n \xrightarrow{P} 0$ using stochastic boundedness (tightness) of $X_n$.
3. Using the results of parts 1 and 2, deduce that $X_n Y_n \xrightarrow{d} c X$, and that for $c \ne 0$, $X_n / Y_n \xrightarrow{d} X / c$.

---

### Solution, step 1: Proof of Summation ($X_n + Y_n \xrightarrow{d} X + c$)
Let $F_n(t) = P(X_n + Y_n \le t)$ denote the CDF of the sum, and let $F(t) = P(X + c \le t) = F_X(t - c)$ denote the target limiting CDF.
We must show that for every real number $t$ that is a point of continuity of $F$ (which is equivalent to $t - c$ being a continuity point of $F_X$):

$$\lim_{n \to \infty} P(X_n + Y_n \le t) = F_X(t - c)$$

Let $\epsilon > 0$ be an arbitrary positive constant.
Consider the event $\{X_n + Y_n \le t\}$. We partition this event based on whether the perturbation $|Y_n - c| \le \epsilon$ or $|Y_n - c| > \epsilon$:

$$\{X_n + Y_n \le t\} = (\{X_n + Y_n \le t\} \cap \{|Y_n - c| \le \epsilon\}) \cup (\{X_n + Y_n \le t\} \cap \{|Y_n - c| > \epsilon\})$$

If $X_n + Y_n \le t$ and $|Y_n - c| \le \epsilon$, then $Y_n \ge c - \epsilon$, which implies:

$$X_n \le t - Y_n \le t - (c - \epsilon) = t - c + \epsilon$$

Therefore, we have the set containment:

$$\{X_n + Y_n \le t\} \subseteq \{X_n \le t - c + \epsilon\} \cup \{|Y_n - c| > \epsilon\}$$

Taking probabilities and applying subadditivity:

$$P(X_n + Y_n \le t) \le P(X_n \le t - c + \epsilon) + P(|Y_n - c| > \epsilon)$$

Now take the limit superior as $n \to \infty$. By the hypothesis of convergence in probability, $\lim_{n \to \infty} P(|Y_n - c| > \epsilon) = 0$.
And by hypothesis, $X_n \xrightarrow{d} X$. If we select $\epsilon > 0$ such that $t - c + \epsilon$ is a continuity point of $F_X$:

$$\limsup_{n \to \infty} P(X_n + Y_n \le t) \le F_X(t - c + \epsilon)$$

Conversely, consider the event $\{X_n \le t - c - \epsilon\}$.
If $X_n \le t - c - \epsilon$ and $|Y_n - c| \le \epsilon$, then $Y_n \le c + \epsilon$, which implies:

$$X_n + Y_n \le (t - c - \epsilon) + (c + \epsilon) = t$$

Therefore:

$$\{X_n \le t - c - \epsilon\} \subseteq \{X_n + Y_n \le t\} \cup \{|Y_n - c| > \epsilon\}$$

Taking probabilities:

$$P(X_n \le t - c - \epsilon) \le P(X_n + Y_n \le t) + P(|Y_n - c| > \epsilon)$$

Subtracting $P(|Y_n - c| > \epsilon)$ and taking the limit inferior as $n \to \infty$:

$$F_X(t - c - \epsilon) \le \liminf_{n \to \infty} P(X_n + Y_n \le t)$$

Combining our lower and upper bounds:

$$F_X(t - c - \epsilon) \le \liminf_{n \to \infty} P(X_n + Y_n \le t) \le \limsup_{n \to \infty} P(X_n + Y_n \le t) \le F_X(t - c + \epsilon)$$

Because this holds for every sufficiently small $\epsilon > 0$ in the dense set of continuity points of $F_X$, we take the limit as $\epsilon \to 0^+$. Since $t - c$ is a point of continuity of $F_X$:

$$\lim_{\epsilon \to 0^+} F_X(t - c - \epsilon) = F_X(t - c) = \lim_{\epsilon \to 0^+} F_X(t - c + \epsilon)$$

By the squeeze theorem:

$$\lim_{n \to \infty} P(X_n + Y_n \le t) = F_X(t - c) = P(X + c \le t)$$

This establishes part 1: $X_n + Y_n \xrightarrow{d} X + c$. $\blacksquare$

---

### Solution, step 2: Proof that $Y_n \xrightarrow{P} 0 \implies X_n Y_n \xrightarrow{P} 0$
We must show that for any given error tolerance $\epsilon > 0$:

$$\lim_{n \to \infty} P(|X_n Y_n| \ge \epsilon) = 0$$

Choose an arbitrary positive cutoff threshold $M > 0$. We partition the sample space based on whether $|X_n| > M$ or $|X_n| \le M$:

$$\{|X_n Y_n| \ge \epsilon\} \subseteq \{|X_n| > M\} \cup \left\{ |Y_n| \ge \frac{\epsilon}{M} \right\}$$

To verify this inclusion, note that if $|X_n| \le M$ and $|Y_n| < \epsilon/M$, then the product satisfies $|X_n Y_n| \le |X_n| |Y_n| < M(\epsilon/M) = \epsilon$.
Taking probabilities:

$$P(|X_n Y_n| \ge \epsilon) \le P(|X_n| > M) + P\left( |Y_n| \ge \frac{\epsilon}{M} \right)$$

Now take the limit superior as $n \to \infty$. Since $Y_n \xrightarrow{P} 0$, for any fixed $M > 0$, the second term vanishes: $\lim_{n \to \infty} P(|Y_n| \ge \epsilon/M) = 0$.
Furthermore, because $X_n \xrightarrow{d} X$, the sequence $\{X_n\}$ is **tight** (stochastically bounded). Specifically, if we select $M$ from the continuity points of the distribution of $|X|$:

$$\limsup_{n \to \infty} P(|X_n| > M) = P(|X| > M)$$

Therefore, for every $M > 0$:

$$\limsup_{n \to \infty} P(|X_n Y_n| \ge \epsilon) \le P(|X| > M)$$

Since $X$ is a well-defined, proper random variable, its tail probabilities vanish at infinity:

$$\lim_{M \to \infty} P(|X| > M) = 0$$

Taking the infimum over all $M > 0$ yields:

$$\limsup_{n \to \infty} P(|X_n Y_n| \ge \epsilon) \le 0$$

Since probabilities cannot be negative, the limit exists and equals zero:

$$\lim_{n \to \infty} P(|X_n Y_n| \ge \epsilon) = 0$$

This proves that $X_n Y_n \xrightarrow{P} 0$. $\blacksquare$

---

### Solution, step 3: Proof of Multiplication and Division
Now consider $X_n Y_n$ when $Y_n \xrightarrow{P} c$.
Decompose the product algebraically:

$$X_n Y_n = X_n (c + (Y_n - c)) = c X_n + X_n (Y_n - c)$$

1. By the Continuous Mapping Theorem applied to scalar multiplication $g(x) = cx$:
   $$c X_n \xrightarrow{d} c X$$
2. Let $Z_n = Y_n - c$. By hypothesis, $Z_n \xrightarrow{P} 0$.
   Applying the result proved in step 2:
   $$X_n (Y_n - c) = X_n Z_n \xrightarrow{P} 0$$
3. Now apply the summation theorem proved in step 1 to the sum of $A_n = c X_n$ (which converges in distribution to $cX$) and $B_n = X_n(Y_n - c)$ (which converges in probability to 0):
   $$X_n Y_n = A_n + B_n \xrightarrow{d} c X + 0 = c X$$

Finally, for division when $c \ne 0$:
The reciprocal function $h(y) = 1/y$ is continuous on the punctured real line $\mathbb{R} \setminus \{0\}$.
Because $Y_n \xrightarrow{P} c$ with $c \ne 0$, the Continuous Mapping Theorem implies:

$$\frac{1}{Y_n} \xrightarrow{P} \frac{1}{c}$$

Now apply the multiplication result established above to $X_n$ and $1/Y_n$:

$$\frac{X_n}{Y_n} = X_n \cdot \left( \frac{1}{Y_n} \right) \xrightarrow{d} X \cdot \frac{1}{c} = \frac{X}{c}$$

This concludes the complete, rigorous proof of Slutsky's Theorem. $\blacksquare$


## Fully worked question 2: Deriving the Asymptotic Distribution of the Coefficient of Variation via Bivariate Delta Method

### Question
Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed (i.i.d.) random sample from a population with finite fourth moment $\mathbb{E}[X^4] < \infty$.
Let:
- $\mu = \mathbb{E}[X] \ne 0$ denote the population mean;
- $\sigma^2 = \text{Var}(X) > 0$ denote the population variance;
- $\mu_3 = \mathbb{E}[(X - \mu)^3]$ denote the third central moment;
- $\mu_4 = \mathbb{E}[(X - \mu)^4]$ denote the fourth central moment.

The population **coefficient of variation** is defined by:

$$V = \frac{\sigma}{\mu}$$

and is estimated by the sample coefficient of variation:

$$V_n = \frac{S_n}{\bar{X}_n}$$

where $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ and $S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X}_n)^2$.

1. Derive the joint asymptotic distribution of the vector $(\bar{X}_n, S_n^2)^T$ using the bivariate Central Limit Theorem.
2. Define the transformation $g(\bar{X}_n, S_n^2) = \frac{\sqrt{S_n^2}}{\bar{X}_n}$, compute its gradient vector $\nabla g(\mu, \sigma^2)$, and apply the Multivariate Delta Method to obtain the general asymptotic distribution of $\sqrt{n}(V_n - V)$.
3. Simplify the asymptotic variance when the underlying population is strictly Gaussian ($\mathcal{N}(\mu, \sigma^2)$).

---

### Solution, step 1: Joint Asymptotic Distribution of $(\bar{X}_n, S_n^2)^T$
First, replace $S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X}_n)^2$ with the asymptotically equivalent uncentered sample second moment around the true mean $\mu$.
Expand the sample variance:

$$\frac{1}{n}\sum_{i=1}^n (X_i - \bar{X}_n)^2 = \frac{1}{n}\sum_{i=1}^n (X_i - \mu)^2 - (\bar{X}_n - \mu)^2$$

Notice that $\sqrt{n}(\bar{X}_n - \mu)^2 = \frac{1}{\sqrt{n}}(\sqrt{n}(\bar{X}_n - \mu))^2 = O_P(n^{-1/2}) \xrightarrow{P} 0$.
Furthermore, the Bessel correction factor satisfies:

$$\frac{n}{n-1} = 1 + \frac{1}{n-1} = 1 + O(n^{-1})$$

Therefore, by Slutsky's theorem, the asymptotic distribution of $S_n^2$ is identical to the asymptotic distribution of the sample mean of the squared deviations:

$$W_n = \frac{1}{n}\sum_{i=1}^n (X_i - \mu)^2$$

Now define the bivariate random vector for the $i$-th observation:

$$\mathbf{U}_i = \begin{pmatrix} X_i \\ (X_i - \mu)^2 \end{pmatrix}$$

The expectation vector is:

$$\mathbb{E}[\mathbf{U}_i] = \begin{pmatrix} \mu \\ \sigma^2 \end{pmatrix}$$

Compute the elements of the $2 \times 2$ covariance matrix $\boldsymbol{\Sigma}$:
1. Top-left variance:
   $$\text{Var}(X_i) = \sigma^2$$
2. Bottom-right variance:
   $$\text{Var}((X_i - \mu)^2) = \mathbb{E}[(X_i - \mu)^4] - (\mathbb{E}[(X_i - \mu)^2])^2 = \mu_4 - \sigma^4$$
3. Off-diagonal covariance:
   $$\text{Cov}(X_i, (X_i - \mu)^2) = \mathbb{E}[(X_i - \mu)(X_i - \mu)^2] = \mathbb{E}[(X_i - \mu)^3] = \mu_3$$

Thus, the population covariance matrix of $\mathbf{U}_i$ is:

$$\boldsymbol{\Sigma} = \begin{pmatrix} \sigma^2 & \mu_3 \\ \mu_3 & \mu_4 - \sigma^4 \end{pmatrix}$$

By the bivariate Lindeberg-Lévy Central Limit Theorem:

$$\sqrt{n}\left( \begin{pmatrix} \bar{X}_n \\ S_n^2 \end{pmatrix} - \begin{pmatrix} \mu \\ \sigma^2 \end{pmatrix} \right) \xrightarrow{d} \mathcal{N}_2\left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \, \begin{pmatrix} \sigma^2 & \mu_3 \\ \mu_3 & \mu_4 - \sigma^4 \end{pmatrix} \right)$$

---

### Solution, step 2: Multivariate Delta Method Application
Let $u = \bar{X}_n$ and $v = S_n^2$. The function representing the sample coefficient of variation is:

$$g(u, v) = \frac{\sqrt{v}}{u} = u^{-1} v^{1/2}$$

Compute the partial derivatives evaluated at $(u, v) = (\mu, \sigma^2)$:
1. Partial derivative with respect to $u$:
   $$\frac{\partial g}{\partial u} = -\frac{\sqrt{v}}{u^2} \implies \left. \frac{\partial g}{\partial u} \right|_{(\mu, \sigma^2)} = -\frac{\sigma}{\mu^2}$$
2. Partial derivative with respect to $v$:
   $$\frac{\partial g}{\partial v} = \frac{1}{2 u \sqrt{v}} \implies \left. \frac{\partial g}{\partial v} \right|_{(\mu, \sigma^2)} = \frac{1}{2 \mu \sigma}$$

Thus, the gradient row vector is:

$$\nabla g(\mu, \sigma^2)^T = \begin{pmatrix} -\frac{\sigma}{\mu^2} & \frac{1}{2\mu\sigma} \end{pmatrix}$$

By the Multivariate Delta Method, $\sqrt{n}(V_n - V) \xrightarrow{d} \mathcal{N}(0, \sigma_V^2)$, where the asymptotic variance is:

$$\sigma_V^2 = \nabla g^T \boldsymbol{\Sigma} \nabla g = \begin{pmatrix} -\frac{\sigma}{\mu^2} & \frac{1}{2\mu\sigma} \end{pmatrix} \begin{pmatrix} \sigma^2 & \mu_3 \\ \mu_3 & \mu_4 - \sigma^4 \end{pmatrix} \begin{pmatrix} -\frac{\sigma}{\mu^2} \\ \frac{1}{2\mu\sigma} \end{pmatrix}$$

Expand the matrix quadratic product:

$$\sigma_V^2 = \left( -\frac{\sigma}{\mu^2} \right)^2 \sigma^2 + 2 \left( -\frac{\sigma}{\mu^2} \right) \left( \frac{1}{2\mu\sigma} \right) \mu_3 + \left( \frac{1}{2\mu\sigma} \right)^2 (\mu_4 - \sigma^4)$$

Simplify each term:
- First term:
  $$\frac{\sigma^2}{\mu^4} \sigma^2 = \frac{\sigma^4}{\mu^4} = V^4$$
- Second term:
  $$-2 \frac{\sigma}{2 \mu^3 \sigma} \mu_3 = -\frac{\mu_3}{\mu^3}$$
- Third term:
  $$\frac{\mu_4 - \sigma^4}{4 \mu^2 \sigma^2}$$

Factor out $V^2 = \frac{\sigma^2}{\mu^2}$:

$$\sigma_V^2 = \frac{\sigma^2}{\mu^2} \left[ \frac{\sigma^2}{\mu^2} - \frac{\mu_3}{\mu \sigma^2} + \frac{\mu_4 - \sigma^4}{4\sigma^4} \right]$$

Thus, the general asymptotic distribution of the sample coefficient of variation is:

$$\sqrt{n}(V_n - V) \xrightarrow{d} \mathcal{N}\left( 0, \, \frac{\sigma^2}{\mu^2} \left[ \frac{\mu_4 - \sigma^4}{4\sigma^4} - \frac{\mu_3}{\mu \sigma^2} + \frac{\sigma^2}{\mu^2} \right] \right) \quad \blacksquare$$

---

### Solution, step 3: Specialization to Gaussian Populations
When the population is Gaussian, $X \sim \mathcal{N}(\mu, \sigma^2)$:
1. By the symmetry of the Gaussian distribution about $\mu$, all odd central moments vanish:
   $$\mu_3 = \mathbb{E}[(X - \mu)^3] = 0$$
2. The fourth central moment of a Gaussian distribution is:
   $$\mu_4 = \mathbb{E}[(X - \mu)^4] = 3\sigma^4$$

Substitute these Gaussian moments into the asymptotic variance expression:
- The skewness cross-covariance term disappears: $-\frac{\mu_3}{\mu \sigma^2} = 0$.
- The kurtosis term simplifies:
  $$\frac{\mu_4 - \sigma^4}{4\sigma^4} = \frac{3\sigma^4 - \sigma^4}{4\sigma^4} = \frac{2\sigma^4}{4\sigma^4} = \frac{1}{2}$$

Substituting back:

$$\sigma_V^2 = \frac{\sigma^2}{\mu^2} \left[ \frac{1}{2} + \frac{\sigma^2}{\mu^2} \right] = V^2 \left( \frac{1}{2} + V^2 \right)$$

Therefore, under normality:

$$\sqrt{n}(V_n - V) \xrightarrow{d} \mathcal{N}\left( 0, \, V^2 \left( \frac{1}{2} + V^2 \right) \right)$$

This demonstrates that the estimation uncertainty of the sample coefficient of variation scales with $V^4$ for large relative variability, highlighting the loss of precision when estimating dispersion relative to small means. $\blacksquare$


## Fully worked question 3: Asymptotic Relative Efficiency of the Sample Median vs Sample Mean

### Question
Let $X_1, X_2, \dots, X_n$ be an i.i.d. sample of size $n = 2m + 1$ (an odd integer) drawn from a continuous probability distribution with density $f(x - \theta)$ that is symmetric about the unknown location parameter $\theta \in \mathbb{R}$, so that $f(u) = f(-u)$ for all $u \in \mathbb{R}$.
Assume that $f(0) > 0$ and that $f$ is continuous in an open neighborhood of 0.
Let:
- $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ denote the sample mean;
- $\tilde{X}_n = X_{(m+1)}$ denote the sample median.

1. State the asymptotic distributions of $\bar{X}_n$ and $\tilde{X}_n$, and express the Asymptotic Relative Efficiency $\text{ARE}(\tilde{X}, \bar{X})$ in terms of the population variance $\sigma^2$ and the central density height $f(0)$.
2. Calculate the exact numerical value of $\text{ARE}(\tilde{X}, \bar{X})$ when $f$ is the Standard Gaussian density:
   $$f(u) = \frac{1}{\sqrt{2\pi}} e^{-u^2/2}$$
3. Calculate the exact value of $\text{ARE}(\tilde{X}, \bar{X})$ when $f$ is the Standard Double Exponential (Laplace) density:
   $$f(u) = \frac{1}{2} e^{-|u|}$$
4. Discuss the methodological implications for statistical robustness when choosing between the sample mean and the sample median.

---

### Solution, step 1: Asymptotic Distributions and ARE Formulation
1. **Asymptotic Distribution of the Sample Mean $\bar{X}_n$**:
   Since the density is symmetric about $\theta$, the population mean is $\mathbb{E}[X] = \theta$. Assuming finite population variance $\sigma^2 = \text{Var}(X) < \infty$, the Lindeberg-Lévy Central Limit Theorem asserts:
   $$\sqrt{n}(\bar{X}_n - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma^2)$$

2. **Asymptotic Distribution of the Sample Median $\tilde{X}_n$**:
   Let $p = 0.5$ denote the median quantile. The population median satisfies $F(\theta) = 0.5$, and the density at the median is $f(\theta - \theta) = f(0)$.
   By the general theorem for the asymptotic distribution of sample quantiles (Unit 6):
   $$\sqrt{n}(\tilde{X}_n - \theta) \xrightarrow{d} \mathcal{N}\left( 0, \, \frac{p(1-p)}{[f(F^{-1}(p))]^2} \right) = \mathcal{N}\left( 0, \, \frac{0.5(1-0.5)}{[f(0)]^2} \right) = \mathcal{N}\left( 0, \, \frac{1}{4 [f(0)]^2} \right)$$

3. **Asymptotic Relative Efficiency**:
   The ARE of the sample median relative to the sample mean is the reciprocal ratio of their asymptotic variances:
   $$\text{ARE}(\tilde{X}, \bar{X}) = \frac{\text{Avar}(\bar{X}_n)}{\text{Avar}(\tilde{X}_n)} = \frac{\sigma^2}{\frac{1}{4 [f(0)]^2}} = 4 \sigma^2 [f(0)]^2$$

---

### Solution, step 2: Calculation for the Gaussian Distribution
Let $X \sim \mathcal{N}(\theta, \sigma^2)$. The density is:

$$f(u) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{u^2}{2\sigma^2} \right)$$

1. Evaluate the density at the center $u = 0$:
   $$f(0) = \frac{1}{\sigma \sqrt{2\pi}} e^0 = \frac{1}{\sigma \sqrt{2\pi}}$$
2. The population variance is $\sigma^2$.
3. Substitute into the ARE formula:
   $$\text{ARE}(\tilde{X}, \bar{X}) = 4 \sigma^2 [f(0)]^2 = 4 \sigma^2 \left( \frac{1}{\sigma \sqrt{2\pi}} \right)^2 = 4 \sigma^2 \left( \frac{1}{2\pi \sigma^2} \right) = \frac{4}{2\pi} = \frac{2}{\pi}$$

Numerically:

$$\text{ARE}(\tilde{X}, \bar{X}) = \frac{2}{\pi} \approx 0.6366198$$

Interpretation: Under Gaussian assumptions, the sample median has an asymptotic efficiency of $63.66\%$ compared to the sample mean. The sample mean achieves the Cramér-Rao lower bound, whereas using the median discards approximately $36.34\%$ of the statistical information contained in the sample.

---

### Solution, step 3: Calculation for the Double Exponential (Laplace) Distribution
Let $X$ follow the Laplace distribution with scale parameter $\beta > 0$:

$$f(u) = \frac{1}{2\beta} \exp\left( -\frac{|u|}{\beta} \right)$$

1. Evaluate the density at the center $u = 0$:
   $$f(0) = \frac{1}{2\beta} e^0 = \frac{1}{2\beta}$$
2. Compute the population variance:
   $$\sigma^2 = \int_{-\infty}^\infty u^2 \frac{1}{2\beta} e^{-|u|/\beta} \, du = \frac{1}{\beta} \int_0^\infty u^2 e^{-u/\beta} \, du$$
   Using the Gamma integral $\int_0^\infty u^k e^{-u/\beta} \, du = k! \, \beta^{k+1}$:
   $$\sigma^2 = \frac{1}{\beta} (2! \beta^3) = 2\beta^2$$
3. Substitute into the ARE formula:
   $$\text{ARE}(\tilde{X}, \bar{X}) = 4 \sigma^2 [f(0)]^2 = 4 (2\beta^2) \left( \frac{1}{2\beta} \right)^2 = 8\beta^2 \left( \frac{1}{4\beta^2} \right) = \frac{8}{4} = 2.0$$

Numerically:

$$\text{ARE}(\tilde{X}, \bar{X}) = 2.0$$

Interpretation: Under Laplace (heavy-tailed) distributions, the sample median is **twice as efficient** as the sample mean ($200\%$ relative efficiency). The sample mean requires $2n$ observations to match the estimation precision achieved by the sample median with only $n$ observations!

---

### Solution, step 4: Robustness and Practical Implications
These results demonstrate the fundamental trade-offs in robust estimation:

1. **Vulnerability of the Sample Mean**:
   The sample mean $\bar{X}_n$ is the Maximum Likelihood Estimator and Best Linear Unbiased Estimator (BLUE) strictly under the Gaussian distribution. However, its breakdown point is $0\%$: a single arbitrarily large outlier ($X_i \to \infty$) can drag the sample mean to infinity. In the presence of heavy tails (such as the Laplace distribution, Student's $t$, or contaminated distributions), extreme values inflate the variance $\sigma^2 = \text{Var}(X)$, crippling the efficiency of $\bar{X}_n$.

2. **Resilience of the Sample Median**:
   The sample median $\tilde{X}_n$ is the Maximum Likelihood Estimator for the location of the Laplace distribution. It possesses the maximal possible finite-sample breakdown point of $50\%$: half of the sample data must be corrupted before the median can be dragged to infinity.

3. **The Efficiency Trade-Off**:
   - In clean, idealized Gaussian environments, the insurance cost of using the median is a $36.3\%$ loss of efficiency.
   - In noisy or heavy-tailed environments, the payoff of using the median is massive: an efficiency gain of $100\%$ (or infinite gain if variance does not exist, as in the Cauchy distribution where the sample mean has infinite variance while the median converges at rate $\sqrt{n}$).

This insight motivated modern robust statistics, including Huber's $M$-estimators, trimmed means, and Hodges-Lehmann estimators, which achieve $> 95\%$ efficiency at the normal distribution while maintaining strict robustness against heavy tails and outliers. $\blacksquare$
