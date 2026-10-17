# Unit 5: Data Reduction and Sufficiency: Factorization, Minimal Sufficiency, and Ancillarity

## 5.1 The Principle of Data Reduction and the Epistemology of Sufficient Statistics

When an empirical experiment produces an observed data vector $\mathbf{x} = (x_1, x_2, \dots, x_n) \in \mathcal{X}$, the raw sample resides in a high-dimensional Euclidean space $\mathbb{R}^n$. Retaining the entire vector of $n$ numbers creates severe cognitive and computational burdens. A central question in mathematical statistics is: can we summarize the data vector $\mathbf{x}$ into a lower-dimensional statistic $T(\mathbf{x}) \in \mathbb{R}^m$ (where $m \ll n$) without discarding *any* information whatsoever regarding the unknown state of nature $\boldsymbol{\theta} \in \Theta$?

This objective is formalised by the **Sufficiency Principle**. A statistic $T(\mathbf{X})$ is termed **sufficient** for the parameter $\boldsymbol{\theta}$ if it captures all the empirical evidence concerning $\boldsymbol{\theta}$ that was present in the original sample $\mathbf{X}$. Once the numerical value of $T(\mathbf{x})$ is known, the raw data vector $\mathbf{x}$ contains zero additional information regarding $\boldsymbol{\theta}$.

### Measure-Theoretic Definition of Sufficiency
Let $(\mathcal{X}, \mathcal{A}, \mathcal{P})$ be a statistical model, where $\mathcal{P} = \{P_{\boldsymbol{\theta}} : \boldsymbol{\theta} \in \Theta\}$ is a family of probability measures defined on the measurable observation space $(\mathcal{X}, \mathcal{A})$. Let $T: (\mathcal{X}, \mathcal{A}) \to (\mathcal{T}, \mathcal{B})$ be a Borel measurable statistic.

**Definition (Sufficient Statistic)**: The statistic $T$ is said to be **sufficient** for the family $\mathcal{P}$ (or for the parameter $\boldsymbol{\theta}$) if the conditional probability distribution of the sample $\mathbf{X}$ given $T(\mathbf{X}) = t$ is **independent of the parameter $\boldsymbol{\theta}$** for all $t \in \mathcal{T}$.

That is, for every observable event $A \in \mathcal{A}$ and for every $\boldsymbol{\theta} \in \Theta$:

$$P_{\boldsymbol{\theta}}(\mathbf{X} \in A \mid T(\mathbf{X}) = t) = P(\mathbf{X} \in A \mid T(\mathbf{X}) = t)$$

does not depend on $\boldsymbol{\theta}$ almost surely with respect to the induced distribution $P_{\boldsymbol{\theta}}^T$.

The epistemological significance of this definition is profound. If the conditional law of the data given $T(\mathbf{X}) = t$ does not involve the unknown parameter $\boldsymbol{\theta}$, an investigator who knows only the value of $T(\mathbf{x})$ could, in principle, run a computer simulation (a Monte Carlo lottery) that generates a synthetic dataset $\mathbf{X}^*$ drawn from the known conditional distribution $P(\cdot \mid T = t)$. The resulting synthetic vector $\mathbf{X}^*$ possesses the exact same probabilistic distribution as the original real-world dataset $\mathbf{X}$ under the true state of nature $\boldsymbol{\theta}$. Therefore, no inferential procedure—no estimator, no confidence interval, no hypothesis test—operating on the raw sample $\mathbf{X}$ can ever outperform an equivalent procedure operating exclusively on the summary statistic $T(\mathbf{X})$.

## 5.2 Induced Partitions and Sub-$\sigma$-Algebras

From a geometric and measure-theoretic perspective, every statistic $T: \mathcal{X} \to \mathcal{T}$ induces two fundamental mathematical structures:
1. **A Partition of the Sample Space**: For each possible value $t \in \mathcal{T}$, the pre-image:
   $$A_t = T^{-1}(\{t\}) = \{\mathbf{x} \in \mathcal{X} : T(\mathbf{x}) = t\}$$
   forms a partition cell (an equivalence class) of the sample space $\mathcal{X}$. Two sample points $\mathbf{x}, \mathbf{y} \in \mathcal{X}$ belong to the same cell if and only if $T(\mathbf{x}) = T(\mathbf{y})$.
2. **A Sub-$\sigma$-Algebra**: The collection of pre-images of measurable sets in the range space:
   $$\sigma(T) = T^{-1}(\mathcal{B}) = \{T^{-1}(B) : B \in \mathcal{B}\} \subseteq \mathcal{A}$$
   defines a sub-$\sigma$-algebra of the original event space $\mathcal{A}$.

A statistic $T$ is sufficient if and only if for every event $A \in \mathcal{A}$, there exists a $\sigma(T)$-measurable random variable $Z_A$ such that for all $\boldsymbol{\theta} \in \Theta$:

$$\mathbb{E}_{\boldsymbol{\theta}}[\mathbf{1}_A \mid \sigma(T)] = Z_A \quad P_{\boldsymbol{\theta}}\text{-almost surely}$$

Notice that $Z_A$ is a single, fixed version of the conditional expectation that serves simultaneously for all candidate probability measures $P_{\boldsymbol{\theta}} \in \mathcal{P}$. In the language of Halmos and Savage, $T$ is sufficient if the sub-$\sigma$-algebra $\sigma(T)$ is sufficient for $\mathcal{P}$.

## 5.3 The Fisher-Neyman Factorization Theorem

Verifying sufficiency directly from the definition requires calculating conditional distributions, which is frequently tedious or analytically intractable. In 1922, Ronald A. Fisher observed a fundamental multiplicative factorization of the likelihood function for sufficient statistics, which was subsequently proved in full mathematical generality by Jerzy Neyman (1935) for Euclidean spaces and Paul Halmos and Leonard Savage (1949) for dominated measure spaces.

**Theorem (Fisher-Neyman Factorization Theorem)**: Let $\mathcal{P} = \{P_{\boldsymbol{\theta}} : \boldsymbol{\theta} \in \Theta\}$ be a family of probability measures on $(\mathcal{X}, \mathcal{A})$ dominated by a $\sigma$-finite reference measure $\mu$, with generalized probability density functions $f(\mathbf{x}; \boldsymbol{\theta}) = \frac{dP_{\boldsymbol{\theta}}}{d\mu}(\mathbf{x})$.
A statistic $T(\mathbf{X}): \mathcal{X} \to \mathbb{R}^m$ is sufficient for $\boldsymbol{\theta}$ if and only if there exist two non-negative functions $g(t; \boldsymbol{\theta})$ and $h(\mathbf{x})$ such that for all $\mathbf{x} \in \mathcal{X}$ and all $\boldsymbol{\theta} \in \Theta$:

$$f(\mathbf{x}; \boldsymbol{\theta}) = g(T(\mathbf{x}); \boldsymbol{\theta}) \cdot h(\mathbf{x})$$

where:
1. $h(\mathbf{x}) \ge 0$ is a non-negative Borel measurable function of the data vector $\mathbf{x}$ alone, containing **no dependence on the parameter $\boldsymbol{\theta}$**.
2. $g(t; \boldsymbol{\theta}) \ge 0$ is a non-negative function that depends on the data vector $\mathbf{x}$ **exclusively through the summary statistic $T(\mathbf{x})$**, and may depend arbitrarily on the parameter $\boldsymbol{\theta}$.

### Heuristic Proof in the Discrete Setting
Suppose $\mathcal{X}$ is discrete, so that $f(\mathbf{x}; \boldsymbol{\theta}) = P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x})$.
First, assume the factorization holds: $P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x}) = g(T(\mathbf{x}); \boldsymbol{\theta}) h(\mathbf{x})$.
Let $t \in \mathcal{T}$ be any possible value of $T$, and let $A_t = \{\mathbf{y} \in \mathcal{X} : T(\mathbf{y}) = t\}$. The probability that $T(\mathbf{X}) = t$ is:

$$P_{\boldsymbol{\theta}}(T(\mathbf{X}) = t) = \sum_{\mathbf{y} \in A_t} P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{y}) = \sum_{\mathbf{y} \in A_t} g(T(\mathbf{y}); \boldsymbol{\theta}) h(\mathbf{y})$$

Since $T(\mathbf{y}) = t$ for all $\mathbf{y} \in A_t$, the term $g(t; \boldsymbol{\theta})$ is constant across the summation and can be factored out:

$$P_{\boldsymbol{\theta}}(T(\mathbf{X}) = t) = g(t; \boldsymbol{\theta}) \sum_{\mathbf{y} \in A_t} h(\mathbf{y})$$

Now compute the conditional probability $P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x} \mid T(\mathbf{X}) = t)$.
If $T(\mathbf{x}) \ne t$, the conditional probability is zero, which is independent of $\boldsymbol{\theta}$.
If $T(\mathbf{x}) = t$, by the definition of conditional probability:

$$P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x} \mid T(\mathbf{X}) = t) = \frac{P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x}, T(\mathbf{X}) = t)}{P_{\boldsymbol{\theta}}(T(\mathbf{X}) = t)} = \frac{P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x})}{P_{\boldsymbol{\theta}}(T(\mathbf{X}) = t)} = \frac{g(t; \boldsymbol{\theta}) h(\mathbf{x})}{g(t; \boldsymbol{\theta}) \sum_{\mathbf{y} \in A_t} h(\mathbf{y})}$$

Canceling the common factor $g(t; \boldsymbol{\theta})$ from numerator and denominator:

$$P_{\boldsymbol{\theta}}(\mathbf{X} = \mathbf{x} \mid T(\mathbf{X}) = t) = \frac{h(\mathbf{x})}{\sum_{\mathbf{y} \in A_t} h(\mathbf{y})}$$

Notice that the right-hand side contains only the function $h$ and contains **zero dependence on $\boldsymbol{\theta}$**! Thus, $T$ is a sufficient statistic.
The converse follows by defining $g(t; \boldsymbol{\theta}) = P_{\boldsymbol{\theta}}(T(\mathbf{X}) = t)$ and $h(\mathbf{x}) = P(\mathbf{X} = \mathbf{x} \mid T(\mathbf{X}) = T(\mathbf{x}))$. $\blacksquare$

### Canonical Examples of the Factorization Theorem
1. **Poisson Distribution**: Let $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} \text{Poisson}(\lambda)$. The joint PMF is:
   $$f(\mathbf{x}; \lambda) = \prod_{i=1}^n \frac{e^{-\lambda} \lambda^{x_i}}{x_i!} = e^{-n\lambda} \lambda^{\sum x_i} \left( \prod_{i=1}^n \frac{1}{x_i!} \right)$$
   Setting $T(\mathbf{x}) = \sum_{i=1}^n x_i$, $g(t; \lambda) = e^{-n\lambda} \lambda^t$, and $h(\mathbf{x}) = \prod_{i=1}^n \frac{1}{x_i!}$, the Fisher-Neyman factorization is verified, proving that the sample sum $T = \sum_{i=1}^n X_i$ is sufficient for $\lambda$.
2. **Normal Distribution with Unknown Mean and Variance**: Let $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma^2)$, with $\boldsymbol{\theta} = (\mu, \sigma^2)$. The joint PDF is:
   $$f(\mathbf{x}; \mu, \sigma^2) = (2\pi \sigma^2)^{-n/2} \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu)^2 \right)$$
   Expanding the quadratic sum: $\sum_{i=1}^n (x_i - \mu)^2 = \sum_{i=1}^n x_i^2 - 2\mu \sum_{i=1}^n x_i + n\mu^2$.
   $$f(\mathbf{x}; \mu, \sigma^2) = (2\pi \sigma^2)^{-n/2} \exp\left( -\frac{n\mu^2}{2\sigma^2} \right) \exp\left( \frac{\mu}{\sigma^2} \sum_{i=1}^n x_i - \frac{1}{2\sigma^2} \sum_{i=1}^n x_i^2 \right) \cdot 1$$
   Setting $T(\mathbf{x}) = \left(\sum_{i=1}^n x_i, \; \sum_{i=1}^n x_i^2\right)$, $h(\mathbf{x}) = 1$, and $g(t_1, t_2; \mu, \sigma^2) = (2\pi \sigma^2)^{-n/2} \exp\left( -\frac{n\mu^2}{2\sigma^2} + \frac{\mu}{\sigma^2} t_1 - \frac{1}{2\sigma^2} t_2 \right)$, the Factorization Theorem confirms that the two-dimensional statistic $T(\mathbf{X}) = \left(\sum X_i, \sum X_i^2\right)$ (or equivalently $(\bar{X}, S^2)$) is jointly sufficient for $(\mu, \sigma^2)$.
3. **Uniform Distribution on $(0, \theta)$**: Let $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} \text{Uniform}(0, \theta)$. The joint PDF is:
   $$f(\mathbf{x}; \theta) = \prod_{i=1}^n \frac{1}{\theta} \mathbf{1}_{(0, \theta)}(x_i) = \frac{1}{\theta^n} \prod_{i=1}^n \mathbf{1}_{(0, \theta)}(x_i)$$
   Notice that all $x_i \in (0, \theta)$ if and only if $\min(x_i) > 0$ and $\max(x_i) < \theta$. Therefore:
   $$f(\mathbf{x}; \theta) = \frac{1}{\theta^n} \mathbf{1}_{(-\infty, \theta)}(x_{(n)}) \cdot \mathbf{1}_{(0, \infty)}(x_{(1)})$$
   Setting $T(\mathbf{x}) = x_{(n)} = \max(x_1, \dots, x_n)$, $g(t; \theta) = \frac{1}{\theta^n} \mathbf{1}_{(0, \theta)}(t)$, and $h(\mathbf{x}) = \mathbf{1}_{(0, \infty)}(x_{(1)})$, the Factorization Theorem proves that the sample maximum $X_{(n)}$ is sufficient for $\theta$.

## 5.4 Minimal Sufficient Statistics and the Lehmann-Scheffé Criterion

While sufficiency guarantees that no information about $\boldsymbol{\theta}$ is lost, it does not guarantee that the data reduction is maximal. Indeed, the trivial statistic $T(\mathbf{X}) = (X_1, X_2, \dots, X_n)$ (the identity mapping) is *always* sufficient, because the conditional distribution of $\mathbf{X}$ given $\mathbf{X} = \mathbf{x}$ is a degenerate point mass at $\mathbf{x}$, which involves no parameters! Similarly, the complete vector of order statistics $\mathbf{X}_{(\cdot)} = (X_{(1)}, \dots, X_{(n)})$ is always sufficient, because the conditional distribution given the sorted values is uniform over all $n!$ permutations, which is parameter-free.

To achieve maximum possible data compression, mathematical statistics seeks a **minimal sufficient statistic**.

### Formal Definition of Minimal Sufficiency
A sufficient statistic $T(\mathbf{X})$ is said to be **minimal sufficient** if it can be calculated from any other sufficient statistic.

Formally, $T$ is minimal sufficient for $\mathcal{P}$ if:
1. $T(\mathbf{X})$ is sufficient for $\boldsymbol{\theta}$.
2. If $S(\mathbf{X})$ is any other sufficient statistic for $\boldsymbol{\theta}$, then there exists a Borel measurable function $\psi$ such that:
   $$T(\mathbf{X}) = \psi(S(\mathbf{X})) \quad P_{\boldsymbol{\theta}}\text{-almost surely for all } \boldsymbol{\theta} \in \Theta$$

In terms of induced partitions, a minimal sufficient statistic generates the **coarsest possible partition** of the sample space among all sufficient statistics. Every cell of a sufficient partition is contained within a cell of the minimal sufficient partition. Minimal sufficiency represents the absolute limit of data reduction: compressing the data any further would inevitably discard information about $\boldsymbol{\theta}$.

### The Lehmann-Scheffé Ratio Partition Criterion
In 1950, Erich L. Lehmann and Henry Scheffé formulated a constructive, elegant criterion for finding minimal sufficient statistics using the likelihood ratio.

**Theorem (Lehmann-Scheffé Minimal Sufficiency Criterion)**: Let $f(\mathbf{x}; \boldsymbol{\theta})$ be the probability density function of the sample vector $\mathbf{x}$. Suppose there exists a statistic $T(\mathbf{x})$ such that for any two sample points $\mathbf{x}, \mathbf{y} \in \mathcal{X}$, the likelihood ratio:

$$\frac{f(\mathbf{x}; \boldsymbol{\theta})}{f(\mathbf{y}; \boldsymbol{\theta})}$$

is **constant as a function of $\boldsymbol{\theta}$** (free of $\boldsymbol{\theta}$) if and only if $T(\mathbf{x}) = T(\mathbf{y})$. Then $T(\mathbf{X})$ is a minimal sufficient statistic for $\boldsymbol{\theta}$.

**Proof**:
First, we prove that $T$ is sufficient. Let $\mathcal{T} = \{T(\mathbf{x}) : \mathbf{x} \in \mathcal{X}\}$ denote the range of $T$. For each $t \in \mathcal{T}$, select a representative point $\mathbf{x}_t \in \mathcal{X}$ such that $T(\mathbf{x}_t) = t$.
For any $\mathbf{x} \in \mathcal{X}$, let $t = T(\mathbf{x})$. Since $T(\mathbf{x}) = T(\mathbf{x}_t)$, the ratio $\frac{f(\mathbf{x}; \boldsymbol{\theta})}{f(\mathbf{x}_t; \boldsymbol{\theta})}$ is independent of $\boldsymbol{\theta}$. Define:
$$h(\mathbf{x}) = \frac{f(\mathbf{x}; \boldsymbol{\theta})}{f(\mathbf{x}_{T(\mathbf{x})}; \boldsymbol{\theta})} \quad \text{and} \quad g(t; \boldsymbol{\theta}) = f(\mathbf{x}_t; \boldsymbol{\theta})$$
Then:
$$f(\mathbf{x}; \boldsymbol{\theta}) = g(T(\mathbf{x}); \boldsymbol{\theta}) \cdot h(\mathbf{x})$$
By the Fisher-Neyman Factorization Theorem, $T(\mathbf{X})$ is sufficient.

Second, we prove that $T$ is minimal. Let $S(\mathbf{X})$ be any other sufficient statistic. By the Factorization Theorem applied to $S$, there exist functions $g_S$ and $h_S$ such that $f(\mathbf{x}; \boldsymbol{\theta}) = g_S(S(\mathbf{x}); \boldsymbol{\theta}) h_S(\mathbf{x})$.
Suppose two points satisfy $S(\mathbf{x}) = S(\mathbf{y})$. The likelihood ratio is:
$$\frac{f(\mathbf{x}; \boldsymbol{\theta})}{f(\mathbf{y}; \boldsymbol{\theta})} = \frac{g_S(S(\mathbf{x}); \boldsymbol{\theta}) h_S(\mathbf{x})}{g_S(S(\mathbf{y}); \boldsymbol{\theta}) h_S(\mathbf{y})} = \frac{h_S(\mathbf{x})}{h_S(\mathbf{y})}$$
This ratio contains no $\boldsymbol{\theta}$!
By the condition of the theorem, whenever the likelihood ratio is free of $\boldsymbol{\theta}$, it must be that $T(\mathbf{x}) = T(\mathbf{y})$.
Therefore:
$$S(\mathbf{x}) = S(\mathbf{y}) \implies T(\mathbf{x}) = T(\mathbf{y})$$
This implies that $T(\mathbf{x})$ is a deterministic function of $S(\mathbf{x})$: $T(\mathbf{x}) = \psi(S(\mathbf{x}))$. Thus, $T$ is minimal sufficient. $\blacksquare$

## 5.5 Ancillary Statistics and the Recovery of Information

At the opposite conceptual pole from sufficient statistics are **ancillary statistics**. While a sufficient statistic contains all information about the parameter, an ancillary statistic contains **zero information about the parameter by itself**.

**Definition (Ancillary Statistic)**: A statistic $V = V(\mathbf{X})$ is said to be **ancillary** for the parameter $\boldsymbol{\theta}$ if its probability distribution does not depend on $\boldsymbol{\theta}$.

That is, for every measurable set $B \in \mathcal{B}$:

$$P_{\boldsymbol{\theta}}(V(\mathbf{X}) \in B) = P(V(\mathbf{X}) \in B) \quad \text{for all } \boldsymbol{\theta} \in \Theta$$

If the first moment of $V$ is independent of $\boldsymbol{\theta}$, $V$ is called first-order ancillary.

### Location and Scale Ancillaries
Ancillary statistics arise naturally in invariant statistical models:
1. **Location Models**: Let $X_i = \mu + \varepsilon_i$, where $\varepsilon_i \stackrel{\text{i.i.d.}}{\sim} f_0(\varepsilon)$. For any contrast vector $\mathbf{c} = (c_1, \dots, c_n)^T$ satisfying $\sum_{i=1}^n c_i = 0$:
   $$\sum_{i=1}^n c_i X_i = \sum_{i=1}^n c_i (\mu + \varepsilon_i) = \mu \sum_{i=1}^n c_i + \sum_{i=1}^n c_i \varepsilon_i = 0 + \sum_{i=1}^n c_i \varepsilon_i$$
   The distribution of any linear contrast (and in particular, the sample variance $S^2$, the sample range $X_{(n)} - X_{(1)}$, and the centered residuals $X_i - \bar{X}$) is completely independent of the location parameter $\mu$. They are location ancillaries.
2. **Scale Models**: Let $X_i = \sigma \varepsilon_i$, where $\varepsilon_i \stackrel{\text{i.i.d.}}{\sim} f_0(\varepsilon)$ with $\sigma > 0$. The ratios $X_i / X_j = (\sigma \varepsilon_i) / (\sigma \varepsilon_j) = \varepsilon_i / \varepsilon_j$ and the sample coefficient of variation $S / \bar{X}$ are scale ancillaries, possessing distributions independent of $\sigma$.

### Fisher's Recovery of Information and Conditioning
Although an ancillary statistic $V$ contains no information about $\boldsymbol{\theta}$ on its own, it frequently determines the **precision or reliability** of the sufficient statistic.

Consider estimating the location $\theta$ from $n = 2$ independent observations from a Uniform distribution $\text{Uniform}(\theta - 1/2, \theta + 1/2)$. The minimal sufficient statistic is the pair $(X_{(1)}, X_{(2)})$.
Define the sample midrange $\hat{\theta} = \frac{X_{(1)} + X_{(2)}}{2}$ and the sample range $R = X_{(2)} - X_{(1)}$.
The range $R$ is ancillary for $\theta$: its distribution on $(0, 1)$ is $f_R(r) = 2(1 - r)$ for $r \in (0, 1)$, containing zero $\theta$.
However, conditional on the observed range $R = r$:
- The parameter $\theta$ is constrained to lie in the interval $[X_{(2)} - 1/2, \; X_{(1)} + 1/2]$, whose width is $1 - (X_{(2)} - X_{(1)}) = 1 - r$.
- If $r = 0.99$, $\theta$ is pinned down within an extremely narrow interval of width $0.01$. The estimator $\hat{\theta}$ is exceptionally precise!
- If $r = 0.01$, $\theta$ could lie anywhere in an interval of width $0.99$, indicating massive uncertainty.

Fisher argued that statistical inference must be conducted **conditionally on ancillary statistics**: the relevant measure of precision is the conditional Fisher information given $V = v$, rather than the unconditional average precision.

## 5.6 Completeness and Bounded Completeness of Statistics

A property closely related to minimal sufficiency and essential for establishing optimal estimators is **completeness**.

**Definition (Complete Statistic)**: A statistic $T(\mathbf{X})$ is said to be **complete** for the family $\mathcal{P} = \{P_{\boldsymbol{\theta}} : \boldsymbol{\theta} \in \Theta\}$ if for any Borel measurable function $g: \mathcal{T} \to \mathbb{R}$:

$$\mathbb{E}_{\boldsymbol{\theta}}[g(T)] = 0 \quad \text{for all } \boldsymbol{\theta} \in \Theta \implies P_{\boldsymbol{\theta}}(g(T) = 0) = 1 \quad \text{for all } \boldsymbol{\theta} \in \Theta$$

That is, the only unbiased estimator of zero based on $T$ is the zero function almost surely.
If the condition holds for all *bounded* measurable functions $g$, the statistic is said to be **boundedly complete**.

Completeness ensures that the statistic contains no "redundant stochastic noise": if two different functions of $T$ had the same expected value, their difference would be an unbiased estimator of zero, which completeness prohibits.

## 5.7 Basu's Theorem: Formulation and Full Measure-Theoretic Proof

One of the most elegant and powerful theorems in mathematical statistics was proved by Debabrata Basu in 1955. It provides a simple algebraic tool for establishing the statistical independence of two statistics without computing joint distributions or executing multivariate integrals.

**Theorem (Basu's Theorem)**: If $T(\mathbf{X})$ is a **complete, boundedly complete, and sufficient statistic** for a family of distributions $\mathcal{P} = \{P_{\boldsymbol{\theta}} : \boldsymbol{\theta} \in \Theta\}$, and $V(\mathbf{X})$ is an **ancillary statistic** for $\mathcal{P}$, then $T(\mathbf{X})$ and $V(\mathbf{X})$ are **statistically independent** under every $P_{\boldsymbol{\theta}} \in \mathcal{P}$.

**Proof**:
Let $B$ be an arbitrary measurable event in the range space of $V$.
Because $V$ is an ancillary statistic, the unconditional probability of $B$ does not depend on $\boldsymbol{\theta}$:
$$P_{\boldsymbol{\theta}}(V \in B) = p_B \quad \text{is constant for all } \boldsymbol{\theta} \in \Theta$$
Now consider the conditional probability of $B$ given the sufficient statistic $T$:
$$g(T) = P_{\boldsymbol{\theta}}(V \in B \mid T) = \mathbb{E}_{\boldsymbol{\theta}}[\mathbf{1}_B(V) \mid T]$$
Because $T$ is a sufficient statistic for $\boldsymbol{\theta}$, by the definition of sufficiency, this conditional probability **does not depend on $\boldsymbol{\theta}$**. Therefore, $g(T)$ is a legitimate statistic containing no parameters.
Furthermore, by the definition of conditional expectation, $0 \le g(T) \le 1$ almost surely, so $g(T)$ is a bounded measurable function.
Now compute the mathematical expectation of $g(T) - p_B$:
$$\mathbb{E}_{\boldsymbol{\theta}}[g(T) - p_B] = \mathbb{E}_{\boldsymbol{\theta}}\left[ \mathbb{E}_{\boldsymbol{\theta}}[\mathbf{1}_B(V) \mid T] \right] - p_B = \mathbb{E}_{\boldsymbol{\theta}}[\mathbf{1}_B(V)] - p_B = P_{\boldsymbol{\theta}}(V \in B) - p_B = p_B - p_B = 0$$
This holds for all $\boldsymbol{\theta} \in \Theta$.
Thus, $g(T) - p_B$ is a bounded function of $T$ whose expected value is identically zero across the entire parameter space $\Theta$.
Because the statistic $T$ is boundedly complete, the completeness property forces $g(T) - p_B$ to be zero almost surely under all $P_{\boldsymbol{\theta}}$:
$$g(T) = p_B \quad P_{\boldsymbol{\theta}}\text{-almost surely for all } \boldsymbol{\theta} \in \Theta$$
Substituting the definition of $g(T)$:
$$P_{\boldsymbol{\theta}}(V \in B \mid T) = P_{\boldsymbol{\theta}}(V \in B) \quad P_{\boldsymbol{\theta}}\text{-almost surely}$$
Because the conditional probability of $V \in B$ given $T$ equals the unconditional probability for every measurable set $B$, the statistics $T$ and $V$ are **statistically independent** under every $P_{\boldsymbol{\theta}} \in \mathcal{P}$. $\blacksquare$

### Applications of Basu's Theorem
Basu's Theorem provides instantaneous proofs of results that would otherwise require tedious multi-page multivariate integration:
1. **Independence of $\bar{X}$ and $S^2$ in Normal Samples**:
   Let $X_1, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma_0^2)$, with known variance $\sigma_0^2$ and unknown mean $\mu$.
   - The sample mean $\bar{X}$ is a complete sufficient statistic for $\mu$.
   - The sample variance $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ is translation-invariant: $S^2(X_1 + c, \dots, X_n + c) = S^2(X_1, \dots, X_n)$. Its distribution depends exclusively on $\sigma_0^2$, containing zero $\mu$. Thus, $S^2$ is ancillary for $\mu$.
   - By Basu's Theorem, $\bar{X}$ and $S^2$ are strictly independent!
2. **Independence of Sample Mean and Coefficient of Variation**:
   In a normal population with unknown mean $\mu$ and known variance, the coefficient of variation is ancillary, making it independent of $\bar{X}$.
3. **Uniform Distribution Minima and Maxima Ratios**:
   Let $X_1, \dots, X_n \sim \text{Uniform}(0, \theta)$. The maximum $X_{(n)}$ is complete and sufficient for $\theta$. The ratio $X_{(1)} / X_{(n)}$ is scale-invariant and therefore ancillary for $\theta$. By Basu's Theorem, $X_{(n)}$ and $X_{(1)} / X_{(n)}$ are independent.

## 5.8 The Rao-Blackwell Theorem: Conditioning on Sufficient Statistics for Variance Reduction

Sufficiency provides the foundation for finding optimal point estimators. In 1945, C. R. Rao and David Blackwell independently proved that conditioning any crude estimator on a sufficient statistic strictly improves (or preserves) its precision.

**Theorem (Rao-Blackwell Theorem)**: Let $\mathbf{X}$ be a random sample with parameter $\boldsymbol{\theta}$, and let $T(\mathbf{X})$ be a sufficient statistic for $\boldsymbol{\theta}$. Let $W = W(\mathbf{X})$ be any unbiased estimator of a scalar parameter function $\tau(\boldsymbol{\theta})$ with finite variance: $\mathbb{E}_{\boldsymbol{\theta}}[W] = \tau(\boldsymbol{\theta})$ and $\text{Var}_{\boldsymbol{\theta}}(W) < \infty$.
Define the conditional expectation of $W$ given $T$:

$$\phi(T) = \mathbb{E}[W \mid T(\mathbf{X})]$$

Then:
1. $\phi(T)$ is a legitimate statistic (does not depend on $\boldsymbol{\theta}$, by sufficiency of $T$).
2. $\phi(T)$ is an unbiased estimator of $\tau(\boldsymbol{\theta})$:
   $$\mathbb{E}_{\boldsymbol{\theta}}[\phi(T)] = \tau(\boldsymbol{\theta})$$
3. The variance of $\phi(T)$ satisfies:
   $$\text{Var}_{\boldsymbol{\theta}}(\phi(T)) \le \text{Var}_{\boldsymbol{\theta}}(W) \quad \text{for all } \boldsymbol{\theta} \in \Theta$$
   with strict inequality $\text{Var}_{\boldsymbol{\theta}}(\phi(T)) < \text{Var}_{\boldsymbol{\theta}}(W)$ unless $W$ is already a deterministic function of $T$ ($P_{\boldsymbol{\theta}}(W = \phi(T)) = 1$).

**Proof**:
1. By definition of sufficiency, the conditional distribution of $\mathbf{X}$ given $T$ contains no $\boldsymbol{\theta}$. Since $W = W(\mathbf{X})$ is a function of $\mathbf{X}$, its conditional expectation $\phi(T) = \mathbb{E}[W \mid T]$ contains no $\boldsymbol{\theta}$, so $\phi(T)$ is a legitimate statistic.
2. By the Law of Total Expectation:
   $$\mathbb{E}_{\boldsymbol{\theta}}[\phi(T)] = \mathbb{E}_{\boldsymbol{\theta}}\left[ \mathbb{E}[W \mid T] \right] = \mathbb{E}_{\boldsymbol{\theta}}[W] = \tau(\boldsymbol{\theta})$$
   Thus, $\phi(T)$ is unbiased.
3. By the Law of Total Variance:
   $$\text{Var}_{\boldsymbol{\theta}}(W) = \text{Var}_{\boldsymbol{\theta}}\left( \mathbb{E}[W \mid T] \right) + \mathbb{E}_{\boldsymbol{\theta}}\left[ \text{Var}(W \mid T) \right] = \text{Var}_{\boldsymbol{\theta}}(\phi(T)) + \mathbb{E}_{\boldsymbol{\theta}}\left[ \text{Var}(W \mid T) \right]$$
   Because variance is non-negative, $\text{Var}(W \mid T) \ge 0$ almost surely, which implies $\mathbb{E}_{\boldsymbol{\theta}}[\text{Var}(W \mid T)] \ge 0$. Therefore:
   $$\text{Var}_{\boldsymbol{\theta}}(W) \ge \text{Var}_{\boldsymbol{\theta}}(\phi(T))$$
   The equality holds if and only if $\text{Var}(W \mid T) = 0$ almost surely, which means $W = \mathbb{E}[W \mid T] = \phi(T)$ almost surely. $\blacksquare$

The Rao-Blackwell Theorem demonstrates that an analyst should never use an estimator that is not a function of a sufficient statistic: conditioning on $T$ filters out extraneous sampling noise while preserving the mean.

## 5.9 The Lehmann-Scheffé Theorem and UMVUE Uniqueness

Combining the Rao-Blackwell Theorem with the property of completeness yields the definitive procedure for finding the unique **Uniformly Minimum Variance Unbiased Estimator (UMVUE)**.

**Theorem (Lehmann-Scheffé Theorem, 1950)**: Let $T(\mathbf{X})$ be a **complete sufficient statistic** for $\boldsymbol{\theta}$. If $W = \phi(T)$ is an unbiased estimator of $\tau(\boldsymbol{\theta})$ that is a function of $T$, then $\phi(T)$ is the **unique Uniformly Minimum Variance Unbiased Estimator (UMVUE)** of $\tau(\boldsymbol{\theta})$.

**Proof**:
Suppose $W^* = W^*(\mathbf{X})$ is any arbitrary unbiased estimator of $\tau(\boldsymbol{\theta})$.
Apply the Rao-Blackwell Theorem to $W^*$ by conditioning on the sufficient statistic $T$:
$$\phi^*(T) = \mathbb{E}[W^* \mid T]$$
Then $\phi^*(T)$ is an unbiased estimator of $\tau(\boldsymbol{\theta})$ that is a function of $T$, and $\text{Var}_{\boldsymbol{\theta}}(\phi^*(T)) \le \text{Var}_{\boldsymbol{\theta}}(W^*)$.
Now consider the difference between $\phi(T)$ and $\phi^*(T)$:
$$\mathbb{E}_{\boldsymbol{\theta}}[\phi(T) - \phi^*(T)] = \mathbb{E}_{\boldsymbol{\theta}}[\phi(T)] - \mathbb{E}_{\boldsymbol{\theta}}[\phi^*(T)] = \tau(\boldsymbol{\theta}) - \tau(\boldsymbol{\theta}) = 0$$
for all $\boldsymbol{\theta} \in \Theta$.
Because $T$ is a complete statistic, the only unbiased estimator of zero based on $T$ is the zero function almost surely:
$$\phi(T) - \phi^*(T) = 0 \iff \phi(T) = \phi^*(T) \quad P_{\boldsymbol{\theta}}\text{-almost surely}$$
Therefore, $\phi(T)$ is identical to the Rao-Blackwellized version of $W^*$. Its variance satisfies:
$$\text{Var}_{\boldsymbol{\theta}}(\phi(T)) = \text{Var}_{\boldsymbol{\theta}}(\phi^*(T)) \le \text{Var}_{\boldsymbol{\theta}}(W^*)$$
Since this holds for *every* unbiased estimator $W^*$, $\phi(T)$ has the minimum variance among all unbiased estimators for every $\boldsymbol{\theta} \in \Theta$.
Furthermore, if another UMVUE existed, its difference from $\phi(T)$ would have mean zero and variance zero, forcing it to coincide with $\phi(T)$ almost surely, establishing uniqueness. $\blacksquare$

The Lehmann-Scheffé Theorem converts the search for optimal unbiased estimators into a systematic two-step algorithm:
1. Identify a complete sufficient statistic $T$ (typically using the Exponential Family theorem from Unit 6).
2. Find a function $g(T)$ such that $\mathbb{E}[g(T)] = \tau(\boldsymbol{\theta})$. Once found, $g(T)$ is guaranteed to be the UMVUE.

## 5.10 Completeness Versus Minimal Sufficiency: The Uniform Interval Counterexample

A subtle but crucial distinction in mathematical statistics exists between **minimal sufficiency** and **completeness**. While every complete sufficient statistic is automatically minimal sufficient (Bahadur's Theorem, 1957), the converse is **not true**: a minimal sufficient statistic is not necessarily complete.

To observe this breakdown, consider a random sample $X_1, X_2, \dots, X_n$ ($n \ge 2$) drawn from a Uniform distribution on an interval of known unit length but unknown center location $\theta \in \mathbb{R}$:

$$X_i \stackrel{\text{i.i.d.}}{\sim} \text{Uniform}\left(\theta - \frac{1}{2}, \; \theta + \frac{1}{2}\right)$$

The joint probability density function is:

$$f(\mathbf{x}; \theta) = \prod_{i=1}^n \mathbf{1}_{(\theta - 1/2, \theta + 1/2)}(x_i) = \mathbf{1}_{(\theta - 1/2, \infty)}(x_{(1)}) \cdot \mathbf{1}_{(-\infty, \theta + 1/2)}(x_{(n)})$$

which is non-zero if and only if:

$$x_{(n)} - \frac{1}{2} < \theta < x_{(1)} + \frac{1}{2}$$

Applying the Lehmann-Scheffé likelihood ratio criterion from Section 5.4, the likelihood ratio $\frac{f(\mathbf{x}; \theta)}{f(\mathbf{y}; \theta)}$ is constant for all $\theta \in \mathbb{R}$ if and only if both the sample minimum and the sample maximum coincide:

$$x_{(1)} = y_{(1)} \quad \text{and} \quad x_{(n)} = y_{(n)}$$

Therefore, the two-dimensional statistic:

$$T(\mathbf{X}) = \left( X_{(1)}, \; X_{(n)} \right)$$

is the **minimal sufficient statistic** for the scalar location parameter $\theta$.

### Demonstration of Incompleteness
We now prove that this minimal sufficient statistic $T = (X_{(1)}, X_{(n)})$ is **not complete**.
Consider the sample range:

$$R = X_{(n)} - X_{(1)}$$

Notice that $R$ is a function of the minimal sufficient statistic $T$.
From Section 5.5, because the model is a pure location family, the sample range $R$ is a **location ancillary statistic**: its probability distribution does not depend on the parameter $\theta$ in any way.
Specifically, let $Z_i = X_i - \theta \sim \text{Uniform}(-1/2, 1/2)$. Then $X_{(n)} - X_{(1)} = Z_{(n)} - Z_{(1)}$.
The expected value of $R$ is a known numerical constant:

$$\mathbb{E}_\theta[R] = \mathbb{E}_\theta\left[ X_{(n)} - X_{(1)} \right] = \frac{n - 1}{n + 1}$$

Now, define the centered function of $T$:

$$g(T) = X_{(n)} - X_{(1)} - \frac{n - 1}{n + 1}$$

Compute the mathematical expectation of $g(T)$ under any parameter $\theta \in \mathbb{R}$:

$$\mathbb{E}_\theta[g(T)] = \mathbb{E}_\theta\left[ X_{(n)} - X_{(1)} \right] - \frac{n - 1}{n + 1} = \frac{n - 1}{n + 1} - \frac{n - 1}{n + 1} = 0$$

The expectation of $g(T)$ is identically zero for all $\theta \in \mathbb{R}$!
However, the random variable $g(T)$ is **not zero almost surely**: the sample range $X_{(n)} - X_{(1)}$ fluctuates continuously across the interval $(0, 1)$, so $P_\theta(g(T) = 0) = 0$.
Thus, $g(T)$ is a non-trivial unbiased estimator of zero.
Consequently, the minimal sufficient statistic $T = (X_{(1)}, X_{(n)})$ is **not complete**!

This counterexample reveals why completeness is a strictly stronger condition than minimal sufficiency. When minimal sufficiency holds without completeness, the Lehmann-Scheffé theorem cannot guarantee the uniqueness of UMVUEs, and multiple distinct unbiased estimators can achieve equal variance.

## 5.11 Group Invariance and Equivariant Estimation: Pitman Estimators

When a statistical problem exhibits physical or geometrical symmetries, the principle of invariance restricts attention to estimators that transform coherently under symmetry operations.

Let $\mathcal{G}$ be a group of transformations acting on the sample space $\mathcal{X}$. We say that a statistical model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ is **invariant under $\mathcal{G}$** if for every $g \in \mathcal{G}$ and every $\theta \in \Theta$, the transformed data $g \mathbf{X}$ has a distribution belonging to the same family, with transformed parameter $\bar{g}\theta \in \Theta$.

### Location Invariance and Equivariance
Consider the translation group $\mathcal{G} = \{g_c : c \in \mathbb{R}\}$, where $g_c(x_1, \dots, x_n) = (x_1 + c, \dots, x_n + c)$.
An estimator $d(\mathbf{X})$ of the location parameter $\theta$ is called **location equivariant** if shifting the data by any constant $c$ shifts the estimate by the exact same amount:

$$d(X_1 + c, X_2 + c, \dots, X_n + c) = d(X_1, \dots, X_n) + c \quad \text{for all } c \in \mathbb{R}$$

Any location equivariant estimator can be decomposed as:

$$d(\mathbf{X}) = X_n - u(X_1 - X_n, X_2 - X_n, \dots, X_{n - 1} - X_n)$$

where the differences $Y_i = X_i - X_n$ are maximal ancillary invariants.

Under the squared error loss function $L(\theta, d) = (d - \theta)^2$, the risk function $R(\theta, d) = \mathbb{E}_\theta[(d(\mathbf{X}) - \theta)^2]$ of any equivariant estimator is **strictly constant across all $\theta \in \mathbb{R}$**.

### The Pitman Estimator of Location
In 1939, E. J. G. Pitman derived the unique **Minimum Risk Equivariant (MRE)** estimator of location.

**Theorem (Pitman Estimator of Location)**: Let $X_1, \dots, X_n$ be an i.i.d. sample from a location family with density $f(x - \theta)$. The Pitman estimator of location, which minimizes the constant squared error risk among all equivariant estimators, is given explicitly by:

$$d^*(\mathbf{X}) = \frac{\int_{-\infty}^\infty u \prod_{i=1}^n f(x_i - u) \, du}{\int_{-\infty}^\infty \prod_{i=1}^n f(x_i - u) \, du}$$

Notice the profound connection to Bayesian statistics: the Pitman estimator coincides mathematically with the **posterior mean of $\theta$ under a uniform improper flat prior** $\pi(\theta) \propto 1$!
- If the distribution is Gaussian $\mathcal{N}(\theta, \sigma^2)$, the Pitman estimator is the sample mean: $d^*(\mathbf{X}) = \bar{X}$.
- If the distribution is Cauchy, the Pitman estimator provides an optimal non-linear compromise that weights all observations smoothly, completely avoiding the catastrophic failure of the sample mean.

## 5.12 Conditional Likelihood and Nuisance Parameter Elimination

In complex statistical investigations, the parameter vector frequently partitions into structural parameters of interest $\boldsymbol{\psi}$ and high-dimensional **nuisance parameters** $\boldsymbol{\lambda}$: $\boldsymbol{\theta} = (\boldsymbol{\psi}, \boldsymbol{\lambda})$. A classic dilemma arises when the number of nuisance parameters grows proportionally with the sample size $n$ (the Neyman-Scott Paradox, 1948), causing classical Maximum Likelihood Estimators to become severely inconsistent.

### Elimination via Conditional Sufficiency
Sufficiency provides the primary mathematical tool for eliminating nuisance parameters without making Bayesian prior assumptions.

Suppose the data vector $\mathbf{X}$ admits a joint density $f(\mathbf{x}; \boldsymbol{\psi}, \boldsymbol{\lambda})$. Suppose further that for every fixed value of the parameter of interest $\boldsymbol{\psi}$, there exists a statistic $S = S(\mathbf{X})$ that is **sufficient for the nuisance parameter $\boldsymbol{\lambda}$**.

By the definition of sufficiency, the conditional probability distribution of the data $\mathbf{X}$ given $S = s$ is **completely free of the nuisance parameter $\boldsymbol{\lambda}$**:

$$f_{\mathbf{X} \mid S}(\mathbf{x} \mid s; \boldsymbol{\psi}) = \frac{f(\mathbf{x}; \boldsymbol{\psi}, \boldsymbol{\lambda})}{f_S(s; \boldsymbol{\psi}, \boldsymbol{\lambda})}$$

This conditional density depends exclusively on the parameter of interest $\boldsymbol{\psi}$!
The resulting objective function:

$$L_c(\boldsymbol{\psi}) = f_{\mathbf{X} \mid S}(\mathbf{x} \mid S(\mathbf{x}); \boldsymbol{\psi})$$

is termed the **Conditional Likelihood**. Maximizing $L_c(\boldsymbol{\psi})$ yields the Conditional Maximum Likelihood Estimator (CMLE), which is guaranteed to be consistent and free from nuisance parameter contamination. This technique serves as the mathematical foundation for matched case-control studies in epidemiology, conditional logistic regression, and Sir David Cox's celebrated Partial Likelihood in proportional hazards survival analysis.

## 5.13 Decision-Theoretic Foundations: Convex Loss and the Rao-Blackwell Invariance

In Abraham Wald's formulation of statistical decision theory (1950), an estimator $\delta(\mathbf{X})$ is evaluated by a loss function $L(\boldsymbol{\theta}, d) \ge 0$, representing the penalty incurred when the true parameter is $\boldsymbol{\theta}$ and the action chosen is $d$. The performance of $\delta$ is quantified by its risk function:

$$R(\boldsymbol{\theta}, \delta) = \mathbb{E}_{\boldsymbol{\theta}}\left[ L(\boldsymbol{\theta}, \delta(\mathbf{X})) \right]$$

An estimator $\delta_1$ is said to **dominate** an estimator $\delta_2$ if $R(\boldsymbol{\theta}, \delta_1) \le R(\boldsymbol{\theta}, \delta_2)$ for all $\boldsymbol{\theta} \in \Theta$, with strict inequality for at least one $\boldsymbol{\theta}$. An estimator is **admissible** if no other estimator dominates it.

### General Rao-Blackwell Theorem for Convex Loss Functions
While Section 5.8 proved the Rao-Blackwell Theorem for squared error loss, the result generalizes to **any arbitrary strictly convex loss function**.

**Theorem (Rao-Blackwell Theorem for Convex Loss)**: Let $T(\mathbf{X})$ be a sufficient statistic for $\boldsymbol{\theta}$. Let $\delta(\mathbf{X})$ be any estimator of $\boldsymbol{\theta}$. Suppose the action space $\mathcal{D} \subseteq \mathbb{R}^k$ is convex, and let $L(\boldsymbol{\theta}, d)$ be a convex function of $d$ for every $\boldsymbol{\theta} \in \Theta$. Define the Rao-Blackwellized estimator:

$$\delta^*(T) = \mathbb{E}[\delta(\mathbf{X}) \mid T(\mathbf{X})]$$

Then:
1. $\delta^*(T)$ is a legitimate statistic containing no parameters.
2. For all $\boldsymbol{\theta} \in \Theta$, the risk of $\delta^*$ is no greater than the risk of $\delta$:
   $$R(\boldsymbol{\theta}, \delta^*) \le R(\boldsymbol{\theta}, \delta)$$
3. If $L(\boldsymbol{\theta}, \cdot)$ is strictly convex, the inequality is strict:
   $$R(\boldsymbol{\theta}, \delta^*) < R(\boldsymbol{\theta}, \delta)$$
   unless $\delta(\mathbf{X}) = \delta^*(T(\mathbf{X}))$ almost surely.

**Proof**:
Conditioning on $T$, apply **Jensen's Inequality** for conditional expectations. Because $L(\boldsymbol{\theta}, \cdot)$ is convex:
$$L\left( \boldsymbol{\theta}, \; \mathbb{E}[\delta(\mathbf{X}) \mid T] \right) \le \mathbb{E}\left[ L(\boldsymbol{\theta}, \delta(\mathbf{X})) \mid T \right]$$
Substituting $\delta^*(T) = \mathbb{E}[\delta(\mathbf{X}) \mid T]$:
$$L(\boldsymbol{\theta}, \delta^*(T)) \le \mathbb{E}\left[ L(\boldsymbol{\theta}, \delta(\mathbf{X})) \mid T \right]$$
Now take unconditional expectations under $P_{\boldsymbol{\theta}}$ on both sides:
$$\mathbb{E}_{\boldsymbol{\theta}}\left[ L(\boldsymbol{\theta}, \delta^*(T)) \right] \le \mathbb{E}_{\boldsymbol{\theta}}\left[ \mathbb{E}\left[ L(\boldsymbol{\theta}, \delta(\mathbf{X})) \mid T \right] \right]$$
By the Law of Total Expectation, the right-hand side simplifies:
$$R(\boldsymbol{\theta}, \delta^*) \le \mathbb{E}_{\boldsymbol{\theta}}\left[ L(\boldsymbol{\theta}, \delta(\mathbf{X})) \right] = R(\boldsymbol{\theta}, \delta)$$
If $L$ is strictly convex, Jensen's inequality holds with equality if and only if $\delta(\mathbf{X})$ is constant conditional on $T$, which means $\delta(\mathbf{X}) = \delta^*(T)$ almost surely. $\blacksquare$

This theorem demonstrates that the Sufficiency Principle is an absolute imperative in statistical decision theory: any randomized estimator or any estimator that depends on the data beyond the sufficient statistic is strictly inadmissible under strictly convex loss!

## 5.14 Sufficiency in Stochastic Processes and Martingale Stopping

The concept of sufficiency extends seamlessly from static i.i.d. random samples to dependent stochastic processes and continuous-time observations.

Let $\{X_t : t \in [0, \tau]\}$ be a continuous-time stochastic process observed over a temporal interval $[0, \tau]$, governed by a probability measure $P_\theta$. For example, consider an observed Poisson counting process $\{N_t : t \in [0, \tau]\}$ with unknown rate intensity $\lambda > 0$, or an observed diffusion process:

$$dX_t = \theta b(X_t) \, dt + \sigma \, dW_t$$

where $W_t$ is a standard Brownian motion.

### Sufficiency of the Terminal State in Homogeneous Markov Processes
In a time-homogeneous Markov jump process or Poisson process, the path $\{N_t : t \in [0, \tau]\}$ consists of the jump times $T_1 < T_2 < \dots < T_{N_\tau}$.
By the Campbell-Hardy likelihood formula for point processes, the likelihood of observing $n$ events at times $t_1, \dots, t_n$ in $[0, \tau]$ is:

$$L(\lambda; \{N_t\}_{t \in [0, \tau]}) = \left( \prod_{i=1}^n \lambda \right) \exp\left( -\int_0^\tau \lambda \, dt \right) = \lambda^n e^{-\lambda \tau} = \lambda^{N_\tau} e^{-\lambda \tau}$$

Notice that the exact jump times $t_1, t_2, \dots, t_n$ **disappear completely from the likelihood function**!
By the Fisher-Neyman Factorization Theorem, the total count at the terminal observation horizon:

$$T = N_\tau$$

is a **complete sufficient statistic** for the rate parameter $\lambda$. Knowing the final terminal count $N_\tau$ captures every scrap of statistical information contained in the continuous trajectory; the precise microscopic timings of the individual jumps are completely ancillary.

This martingale invariance reveals that data reduction is not an artifact of discrete sample indexing, but an intrinsic mathematical property of stochastic information geometry.

## 5.15 The Pitman-Koopman-Darmois Theorem: The Boundary of Finite-Dimensional Data Reduction

In elementary examples, we observed that for samples of arbitrary size $n$ from Gaussian, Poisson, or Exponential distributions, the data vector $(X_1, \dots, X_n) \in \mathbb{R}^n$ can be reduced to a fixed 1- or 2-dimensional sufficient statistic. Conversely, for Cauchy, Student's $t$, or Weibull distributions, no fixed-dimensional reduction is possible: the minimal sufficient statistic is the entire order statistic vector $(X_{(1)}, \dots, X_{(n)}) \in \mathbb{R}^n$, whose dimension grows linearly with the sample size $n$!

This profound dichotomy is answered by the **Pitman-Koopman-Darmois Theorem**, independently proved between 1935 and 1936 by E. J. G. Pitman, B. O. Koopman, and Georges Darmois.

**Theorem (Pitman-Koopman-Darmois Theorem)**: Let $X_1, X_2, \dots, X_n$ be an i.i.d. random sample from a family of distributions with probability density function $f(x; \boldsymbol{\theta})$ supported on an interval of the real line. Assume that:
1. The support $\mathcal{S} = \{x : f(x; \boldsymbol{\theta}) > 0\}$ is **independent of $\boldsymbol{\theta}$** (fixed support).
2. The density $f(x; \boldsymbol{\theta})$ is continuously differentiable with respect to $x$ and $\boldsymbol{\theta}$.

Then there exists a sufficient statistic $T(\mathbf{X}) = (T_1(\mathbf{X}), \dots, T_k(\mathbf{X}))$ whose dimension $k$ remains **strictly fixed and independent of the sample size $n$** (for all $n > k$) **if and only if** the family of distributions is an **Exponential Family** of the form:

$$f(x; \boldsymbol{\theta}) = \exp\left( \sum_{j=1}^k \eta_j(\boldsymbol{\theta}) T_j(x) - A(\boldsymbol{\theta}) + B(x) \right)$$

### Implications of the Theorem
The Pitman-Koopman-Darmois Theorem draws a sharp, definitive boundary across the mathematical universe of probability models:
1. **Inside the Boundary (Exponential Families)**: Gaussian, Gamma, Beta, Binomial, Poisson, Negative Binomial, Multinomial, and von Mises distributions possess fixed-dimensional sufficient statistics. The sample size $n$ can expand to millions of observations, yet all information about $\boldsymbol{\theta}$ can be concentrated into a few scalar counters or sums without any information loss.
2. **Outside the Boundary (Non-Exponential Families with Fixed Support)**: For Cauchy, Student's $t$, Logistic, and general mixture distributions, real data reduction is mathematically impossible. Any data compression beyond the order statistics inevitably discards information about $\boldsymbol{\theta}$.
3. **The Parameter-Dependent Support Exception**: If assumption (1) is violated—meaning the support boundary depends explicitly on $\boldsymbol{\theta}$—fixed-dimensional sufficiency can occur outside the Exponential Family. The canonical example is $\text{Uniform}(0, \theta)$, where the single scalar order statistic $X_{(n)}$ is sufficient for all $n$, but the family is non-regular and fails standard likelihood regularity conditions.

The Pitman-Koopman-Darmois Theorem justifies why the Exponential Family of distributions, studied comprehensively in Unit 6, serves as the central pillar of classical mathematical statistics.

## 5.16 Sufficiency and Fisher Information Conservation

In Unit 1, we defined Fisher Information $I_{\mathbf{X}}(\boldsymbol{\theta})$ as the expected curvature of the log-likelihood function, measuring the sensitivity of the data vector $\mathbf{X}$ to variations in the parameter $\boldsymbol{\theta}$. We now establish how sufficiency operates on Fisher Information.

Let $\mathbf{X} \sim f(\mathbf{x}; \boldsymbol{\theta})$, and let $T = T(\mathbf{X})$ be any statistic (sufficient or non-sufficient) with marginal density $f_T(t; \boldsymbol{\theta})$.
By the chain rule for probability densities:

$$f(\mathbf{x}; \boldsymbol{\theta}) = f_T(T(\mathbf{x}); \boldsymbol{\theta}) \cdot f_{\mathbf{X} \mid T}(\mathbf{x} \mid T(\mathbf{x}); \boldsymbol{\theta})$$

Taking natural logarithms:

$$\ln f(\mathbf{x}; \boldsymbol{\theta}) = \ln f_T(T(\mathbf{x}); \boldsymbol{\theta}) + \ln f_{\mathbf{X} \mid T}(\mathbf{x} \mid T(\mathbf{x}); \boldsymbol{\theta})$$

Differentiating with respect to $\boldsymbol{\theta}$ gives the score function decomposition:

$$S_{\mathbf{X}}(\boldsymbol{\theta}) = S_T(\boldsymbol{\theta}) + S_{\mathbf{X} \mid T}(\boldsymbol{\theta})$$

Because $S_T(\boldsymbol{\theta})$ is the score of the marginal distribution of $T$, the conditional expectation of the cross-product vanishes: $\mathbb{E}_{\boldsymbol{\theta}}[S_T(\boldsymbol{\theta}) S_{\mathbf{X} \mid T}(\boldsymbol{\theta})] = 0$. Taking the variance of both sides:

$$I_{\mathbf{X}}(\boldsymbol{\theta}) = I_T(\boldsymbol{\theta}) + I_{\mathbf{X} \mid T}(\boldsymbol{\theta})$$

where $I_{\mathbf{X} \mid T}(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}[\text{Var}(S_{\mathbf{X} \mid T}(\boldsymbol{\theta}) \mid T)] \ge 0$ is the **Fisher Information lost by summarizing the data through $T$**.

### The Information Conservation Theorem
This decomposition yields the definitive characterization of sufficiency in terms of information metrics.

**Theorem (Information Conservation of Sufficient Statistics)**: Under standard Cramér-Rao regularity conditions:
1. For any arbitrary statistic $T(\mathbf{X})$:
   $$I_T(\boldsymbol{\theta}) \le I_{\mathbf{X}}(\boldsymbol{\theta})$$
   Summarizing data can never increase Fisher Information.
2. The statistic $T(\mathbf{X})$ is **sufficient for $\boldsymbol{\theta}$ if and only if** Fisher Information is strictly conserved:
   $$I_T(\boldsymbol{\theta}) = I_{\mathbf{X}}(\boldsymbol{\theta}) \quad \text{for all } \boldsymbol{\theta} \in \Theta$$

**Proof**:
From the identity $I_{\mathbf{X}}(\boldsymbol{\theta}) = I_T(\boldsymbol{\theta}) + I_{\mathbf{X} \mid T}(\boldsymbol{\theta})$, equality $I_T(\boldsymbol{\theta}) = I_{\mathbf{X}}(\boldsymbol{\theta})$ holds if and only if:
$$I_{\mathbf{X} \mid T}(\boldsymbol{\theta}) = 0$$
which requires the conditional score function $S_{\mathbf{X} \mid T}(\boldsymbol{\theta}) = \frac{\partial}{\partial \boldsymbol{\theta}} \ln f_{\mathbf{X} \mid T}(\mathbf{x} \mid T(\mathbf{x}); \boldsymbol{\theta})$ to vanish almost surely for all $\boldsymbol{\theta}$.
A derivative vanishing identically means that $\ln f_{\mathbf{X} \mid T}(\mathbf{x} \mid t; \boldsymbol{\theta})$ is constant with respect to $\boldsymbol{\theta}$, which means that the conditional distribution $f_{\mathbf{X} \mid T}(\mathbf{x} \mid t)$ contains **zero dependence on $\boldsymbol{\theta}$**.
By definition, this is precisely the condition for $T(\mathbf{X})$ to be a sufficient statistic! $\blacksquare$

This theorem proves that sufficient statistics achieve **zero information loss** under the Riemannian Fisher Information metric, providing an elegant bridge between information geometry and data reduction.

## Fully worked question 1: Rigorous Proof of the Fisher-Neyman Factorization Theorem for Discrete and Dominated Continuous Models

### Question
Let $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ be a family of probability measures on $(\mathcal{X}, \mathcal{A})$ dominated by a $\sigma$-finite reference measure $\mu$, with generalized densities $f(\mathbf{x}; \theta) = \frac{dP_\theta}{d\mu}(\mathbf{x})$. Let $T: \mathcal{X} \to \mathcal{T}$ be a statistic.
1. Formulate the Halmos-Savage dominating measure $\lambda = \sum_{j=1}^\infty c_j P_{\theta_j}$ where $c_j > 0, \sum c_j = 1$.
2. Prove that sufficiency of $T$ implies the existence of non-negative functions $g(T(\mathbf{x}); \theta)$ and $h(\mathbf{x})$ such that $f(\mathbf{x}; \theta) = g(T(\mathbf{x}); \theta) h(\mathbf{x})$.
3. Prove the converse: show that if $f(\mathbf{x}; \theta) = g(T(\mathbf{x}); \theta) h(\mathbf{x})$, the conditional expectation $\mathbb{E}_\theta[\mathbf{1}_A \mid T]$ is free of $\theta$ for every $A \in \mathcal{A}$.

### Solution, step 1: Dominated Family Reduction and Halmos-Savage Measure
Because the family $\mathcal{P}$ is dominated by a $\sigma$-finite measure $\mu$, by the Halmos-Savage Lemma, there exists a countable sequence of parameter points $\{\theta_1, \theta_2, \dots\} \subset \Theta$ and positive constants $c_j > 0$ with $\sum_{j=1}^\infty c_j = 1$ such that the probability measure:

$$\lambda(A) = \sum_{j=1}^\infty c_j P_{\theta_j}(A), \quad A \in \mathcal{A}$$

is equivalent to $\mathcal{P}$ (meaning that $\lambda(A) = 0$ if and only if $P_\theta(A) = 0$ for all $\theta \in \Theta$).
Since each $P_{\theta_j} \ll \mu$, the measure $\lambda$ has Radon-Nikodym derivative with respect to $\mu$:

$$f_0(\mathbf{x}) = \frac{d\lambda}{d\mu}(\mathbf{x}) = \sum_{j=1}^\infty c_j f(\mathbf{x}; \theta_j)$$

where $f_0(\mathbf{x}) > 0$ almost everywhere on the support of $\mathcal{P}$.

### Solution, step 2: Necessity of the Factorization
Assume that $T$ is sufficient for $\mathcal{P}$.
Then for every $\theta \in \Theta$, $P_\theta \ll \lambda$. By the Radon-Nikodym Chain Rule, the density of $P_\theta$ with respect to $\lambda$ is:

$$\frac{dP_\theta}{d\lambda}(\mathbf{x}) = \frac{dP_\theta / d\mu}{d\lambda / d\mu}(\mathbf{x}) = \frac{f(\mathbf{x}; \theta)}{f_0(\mathbf{x})}$$

By the definition of sufficiency, the conditional expectation given $\sigma(T)$ under $P_\theta$ is independent of $\theta$. Since $\lambda$ is a mixture of measures in $\mathcal{P}$, $T$ is also sufficient for $\lambda$.
Therefore, the conditional expectation $\mathbb{E}_\lambda\left[ \left.\frac{dP_\theta}{d\lambda} \right| \sigma(T) \right]$ satisfies the Radon-Nikodym derivative property on the sub-$\sigma$-algebra $\sigma(T)$.
Define the non-negative $\sigma(T)$-measurable function:

$$g(T(\mathbf{x}); \theta) = \mathbb{E}_\lambda\left[ \left. \frac{dP_\theta}{d\lambda} \right| \sigma(T) \right](\mathbf{x})$$

Because $T$ is sufficient, this conditional expectation serves simultaneously as the version for all candidate measures.
By the fundamental property of conditional expectation, for any event $A \in \mathcal{A}$:

$$P_\theta(A) = \int_A \frac{dP_\theta}{d\lambda} \, d\lambda = \int_A \mathbb{E}_\lambda\left[ \left. \frac{dP_\theta}{d\lambda} \right| \sigma(T) \right] d\lambda = \int_A g(T(\mathbf{x}); \theta) \, d\lambda(\mathbf{x})$$

Expressing the integral with respect to the reference measure $\mu$ via $d\lambda(\mathbf{x}) = f_0(\mathbf{x}) \, d\mu(\mathbf{x})$:

$$P_\theta(A) = \int_A g(T(\mathbf{x}); \theta) f_0(\mathbf{x}) \, d\mu(\mathbf{x})$$

On the other hand, by definition of the Radon-Nikodym derivative $f(\mathbf{x}; \theta)$:

$$P_\theta(A) = \int_A f(\mathbf{x}; \theta) \, d\mu(\mathbf{x})$$

Since this holds for every measurable set $A \in \mathcal{A}$, the uniqueness of Radon-Nikodym derivatives guarantees that the integrands are equal $\mu$-almost everywhere:

$$f(\mathbf{x}; \theta) = g(T(\mathbf{x}); \theta) f_0(\mathbf{x})$$

Setting $h(\mathbf{x}) = f_0(\mathbf{x})$, which contains zero dependence on $\theta$, we obtain the exact factorization:

$$f(\mathbf{x}; \theta) = g(T(\mathbf{x}); \theta) \cdot h(\mathbf{x})$$

### Solution, step 3: Sufficiency of the Factorization
Now assume that the factorization holds: $f(\mathbf{x}; \theta) = g(T(\mathbf{x}); \theta) h(\mathbf{x})$.
We must show that for any event $A \in \mathcal{A}$, the conditional probability $P_\theta(\mathbf{X} \in A \mid T)$ contains no $\theta$.
Let $B$ be any measurable set in the range space $\mathcal{T}$. Consider the joint probability:

$$P_\theta(\mathbf{X} \in A, T(\mathbf{X}) \in B) = \int_{A \cap T^{-1}(B)} f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) = \int_{A \cap T^{-1}(B)} g(T(\mathbf{x}); \theta) h(\mathbf{x}) \, d\mu(\mathbf{x})$$

Define the $\sigma$-finite measure $\nu$ on $(\mathcal{X}, \mathcal{A})$ by $d\nu(\mathbf{x}) = h(\mathbf{x}) \, d\mu(\mathbf{x})$. Then:

$$P_\theta(\mathbf{X} \in A, T(\mathbf{X}) \in B) = \int_{T^{-1}(B)} \mathbf{1}_A(\mathbf{x}) g(T(\mathbf{x}); \theta) \, d\nu(\mathbf{x})$$

By Tonelli-Fubini disintegration on the induced measure space:

$$\int_{T^{-1}(B)} \mathbf{1}_A(\mathbf{x}) g(T(\mathbf{x}); \theta) \, d\nu(\mathbf{x}) = \int_B g(t; \theta) \mathbb{E}_\nu[\mathbf{1}_A \mid T = t] \, d\nu^T(t)$$

where $\nu^T$ is the push-forward measure of $\nu$ under $T$.
Setting $A = \mathcal{X}$, we obtain the marginal probability of $T(\mathbf{X}) \in B$:

$$P_\theta(T(\mathbf{X}) \in B) = \int_B g(t; \theta) \, d\nu^T(t)$$

Comparing the two equations reveals that:

$$P_\theta(\mathbf{X} \in A, T(\mathbf{X}) \in B) = \int_B \mathbb{E}_\nu[\mathbf{1}_A \mid T = t] \, dP_\theta^T(t)$$

Therefore, the conditional expectation is:

$$\mathbb{E}_\theta[\mathbf{1}_A \mid T = t] = \mathbb{E}_\nu[\mathbf{1}_A \mid T = t]$$

Notice that the right side is defined with respect to the measure $\nu$, which depends exclusively on $h(\mathbf{x})$ and contains **zero dependence on $\theta$**!
Thus, $T$ is a sufficient statistic. $\blacksquare$

## Fully worked question 2: Minimal Sufficient Statistic for the Normal Distribution with Unknown Mean and Variance via the Lehmann-Scheffé Criterion

### Question
Let $\mathbf{X} = (X_1, X_2, \dots, X_n)$ be an i.i.d. random sample from $\mathcal{N}(\mu, \sigma^2)$, with unknown parameter vector $\boldsymbol{\theta} = (\mu, \sigma^2) \in \mathbb{R} \times (0, \infty)$.
1. Formulate the joint probability density function $f(\mathbf{x}; \boldsymbol{\theta})$ of the sample vector $\mathbf{x}$.
2. For two sample points $\mathbf{x} = (x_1, \dots, x_n)$ and $\mathbf{y} = (y_1, \dots, y_n)$, write out the likelihood ratio $\frac{f(\mathbf{x}; \boldsymbol{\theta})}{f(\mathbf{y}; \boldsymbol{\theta})}$.
3. Determine the exact necessary and sufficient condition under which the likelihood ratio is constant with respect to $\boldsymbol{\theta} = (\mu, \sigma^2)$.
4. Deduce the two-dimensional minimal sufficient statistic $T(\mathbf{X})$ and demonstrate that it is equivalent to $(\bar{X}, S^2)$.

### Solution, step 1: Joint Density Formulation
The joint probability density function of $\mathbf{X} = (X_1, \dots, X_n)$ is:

$$f(\mathbf{x}; \mu, \sigma^2) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x_i - \mu)^2}{2\sigma^2} \right) = (2\pi \sigma^2)^{-n/2} \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu)^2 \right)$$

Expand the squared sum:

$$\sum_{i=1}^n (x_i - \mu)^2 = \sum_{i=1}^n x_i^2 - 2\mu \sum_{i=1}^n x_i + n\mu^2$$

Substituting this into the exponent:

$$f(\mathbf{x}; \mu, \sigma^2) = (2\pi \sigma^2)^{-n/2} \exp\left( -\frac{n\mu^2}{2\sigma^2} \right) \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n x_i^2 + \frac{\mu}{\sigma^2} \sum_{i=1}^n x_i \right)$$

### Solution, step 2: Likelihood Ratio Construction
Now consider two distinct sample realizations $\mathbf{x} = (x_1, \dots, x_n)$ and $\mathbf{y} = (y_1, \dots, y_n)$.
The likelihood ratio is:

$$\frac{f(\mathbf{x}; \mu, \sigma^2)}{f(\mathbf{y}; \mu, \sigma^2)} = \frac{(2\pi \sigma^2)^{-n/2} \exp\left( -\frac{n\mu^2}{2\sigma^2} \right) \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n x_i^2 + \frac{\mu}{\sigma^2} \sum_{i=1}^n x_i \right)}{(2\pi \sigma^2)^{-n/2} \exp\left( -\frac{n\mu^2}{2\sigma^2} \right) \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n y_i^2 + \frac{\mu}{\sigma^2} \sum_{i=1}^n y_i \right)}$$

The pre-factors cancel out completely, leaving:

$$\frac{f(\mathbf{x}; \mu, \sigma^2)}{f(\mathbf{y}; \mu, \sigma^2)} = \exp\left( -\frac{1}{2\sigma^2} \left[ \sum_{i=1}^n x_i^2 - \sum_{i=1}^n y_i^2 \right] + \frac{\mu}{\sigma^2} \left[ \sum_{i=1}^n x_i - \sum_{i=1}^n y_i \right] \right)$$

### Solution, step 3: Evaluation of the Constancy Condition
For the likelihood ratio to be constant as a function of the parameter vector $(\mu, \sigma^2) \in \mathbb{R} \times (0, \infty)$, the exponent must be constant (equal to some constant $C$) for all $\mu \in \mathbb{R}$ and all $\sigma^2 > 0$:

$$-\frac{1}{2\sigma^2} \left[ \sum_{i=1}^n x_i^2 - \sum_{i=1}^n y_i^2 \right] + \frac{\mu}{\sigma^2} \left[ \sum_{i=1}^n x_i - \sum_{i=1}^n y_i \right] \equiv C \quad \text{for all } \mu \in \mathbb{R}, \; \sigma^2 > 0$$

Differentiating this expression with respect to $\mu$ yields:

$$\frac{1}{\sigma^2} \left[ \sum_{i=1}^n x_i - \sum_{i=1}^n y_i \right] = 0 \implies \sum_{i=1}^n x_i = \sum_{i=1}^n y_i$$

Substituting $\sum_{i=1}^n x_i = \sum_{i=1}^n y_i$ back into the exponent removes the $\mu$-term, leaving:

$$-\frac{1}{2\sigma^2} \left[ \sum_{i=1}^n x_i^2 - \sum_{i=1}^n y_i^2 \right] = C \quad \text{for all } \sigma^2 > 0$$

For this expression to remain constant as $\sigma^2$ varies across $(0, \infty)$, the bracketed coefficient must vanish:

$$\sum_{i=1}^n x_i^2 - \sum_{i=1}^n y_i^2 = 0 \implies \sum_{i=1}^n x_i^2 = \sum_{i=1}^n y_i^2$$

Conversely, if both $\sum_{i=1}^n x_i = \sum_{i=1}^n y_i$ and $\sum_{i=1}^n x_i^2 = \sum_{i=1}^n y_i^2$, then the exponent evaluates to $e^0 = 1$, which is completely independent of $\mu$ and $\sigma^2$.

### Solution, step 4: Deduction of Minimal Sufficiency
By the Lehmann-Scheffé criterion, the likelihood ratio $\frac{f(\mathbf{x}; \boldsymbol{\theta})}{f(\mathbf{y}; \boldsymbol{\theta})}$ is independent of $\boldsymbol{\theta}$ if and only if:

$$T(\mathbf{x}) = T(\mathbf{y})$$

where the statistic is defined by:

$$T(\mathbf{X}) = \left( \sum_{i=1}^n X_i, \; \sum_{i=1}^n X_i^2 \right)$$

Therefore, $T(\mathbf{X}) = \left(\sum X_i, \sum X_i^2\right)$ is a **minimal sufficient statistic** for $(\mu, \sigma^2)$.

Now, consider the familiar sample mean and sample variance:

$$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$$

$$S^2 = \frac{1}{n - 1} \left( \sum_{i=1}^n X_i^2 - n \bar{X}^2 \right) = \frac{1}{n - 1} \left( \sum_{i=1}^n X_i^2 - \frac{1}{n} \left(\sum_{i=1}^n X_i\right)^2 \right)$$

Notice that $(\bar{X}, S^2)$ is obtained from $T(\mathbf{X})$ via the one-to-one invertible transformation:

$$\psi(t_1, t_2) = \left( \frac{t_1}{n}, \; \frac{1}{n - 1}\left( t_2 - \frac{t_1^2}{n} \right) \right)$$

The inverse transformation is:

$$t_1 = n \bar{X}, \quad t_2 = (n - 1)S^2 + n \bar{X}^2$$

Because any one-to-one function of a minimal sufficient statistic is also minimal sufficient, the pair $(\bar{X}, S^2)$ is likewise a **two-dimensional minimal sufficient statistic** for the normal distribution with unknown mean and variance. $\blacksquare$

## Fully worked question 3: Proof of Statistical Independence of the Sample Variance and Sample Coefficient of Variation via Basu's Theorem

### Question
Let $X_1, X_2, \dots, X_n$ be an i.i.d. random sample from $\mathcal{N}(0, \sigma^2)$, a zero-mean normal distribution with unknown scale parameter $\sigma > 0$.
Let $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ denote the sample variance, and let:

$$V = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{\left(\sum_{i=1}^n X_i^2\right)} = \frac{(n - 1)S^2}{\sum_{i=1}^n X_i^2}$$

denote the normalized dispersion ratio.
1. Identify the complete sufficient statistic $T(\mathbf{X})$ for the scale parameter $\sigma^2$.
2. Prove that $V$ is an ancillary statistic for $\sigma^2$ by demonstrating scale invariance.
3. Apply Basu's Theorem to prove that $T(\mathbf{X})$ and $V$ are statistically independent.
4. Derive the exact distribution of $V$ and evaluate $\mathbb{E}[V]$.

### Solution, step 1: Complete Sufficient Statistic
For $X_i \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)$, the joint probability density function is:

$$f(\mathbf{x}; \sigma^2) = (2\pi \sigma^2)^{-n/2} \exp\left( -\frac{1}{2\sigma^2} \sum_{i=1}^n x_i^2 \right)$$

By the Fisher-Neyman Factorization Theorem, the statistic:

$$T = \sum_{i=1}^n X_i^2$$

is sufficient for $\sigma^2$ (with $g(t; \sigma^2) = (2\pi \sigma^2)^{-n/2} e^{-t/(2\sigma^2)}$ and $h(\mathbf{x}) = 1$).
Furthermore, this distribution belongs to the 1-parameter regular Exponential Family with natural parameter $\eta = -\frac{1}{2\sigma^2} \in (-\infty, 0)$ and natural sufficient statistic $T = \sum_{i=1}^n X_i^2$.
Because the natural parameter space contains an open interval of the real line, by the Exponential Family Completeness Theorem (Unit 6), $T$ is a **complete sufficient statistic** for $\sigma^2$.

### Solution, step 2: Proof of Ancillarity
Consider the statistic $V$:

$$V = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{\sum_{i=1}^n X_i^2}$$

Let $Z_i = X_i / \sigma$. Because $X_i \sim \mathcal{N}(0, \sigma^2)$, the standardized variables $Z_i \sim \mathcal{N}(0, 1)$ are standard normal variables with zero mean and unit variance, completely independent of $\sigma$.
Express $X_i$ as $X_i = \sigma Z_i$. Then $\bar{X} = \sigma \bar{Z}$.
Substitute these expressions into the numerator and denominator of $V$:

$$V = \frac{\sum_{i=1}^n (\sigma Z_i - \sigma \bar{Z})^2}{\sum_{i=1}^n (\sigma Z_i)^2} = \frac{\sigma^2 \sum_{i=1}^n (Z_i - \bar{Z})^2}{\sigma^2 \sum_{i=1}^n Z_i^2} = \frac{\sum_{i=1}^n (Z_i - \bar{Z})^2}{\sum_{i=1}^n Z_i^2}$$

Notice that the scale parameter $\sigma^2$ cancels out completely from the ratio!
The random variable $V$ is expressed entirely in terms of the standard normal vector $\mathbf{Z} \sim \mathcal{N}_n(\mathbf{0}, \mathbf{I}_n)$.
Because the distribution of $\mathbf{Z}$ contains zero parameters, the probability distribution of $V$ is **completely independent of $\sigma^2$**.
Therefore, $V$ is an **ancillary statistic** for $\sigma^2$.

### Solution, step 3: Application of Basu's Theorem
We have verified that:
1. $T = \sum_{i=1}^n X_i^2$ is a complete and sufficient statistic for $\sigma^2$.
2. $V = \frac{\sum (X_i - \bar{X})^2}{\sum X_i^2}$ is an ancillary statistic for $\sigma^2$.

By Basu's Theorem (Section 5.7), any ancillary statistic is statistically independent of a complete sufficient statistic under all parameter values.
Therefore:

$$T = \sum_{i=1}^n X_i^2 \quad \text{and} \quad V = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{\sum_{i=1}^n X_i^2} \quad \text{are strictly independent random variables!}$$

### Solution, step 4: Exact Distribution of $V$ and Moment Evaluation
Recall the algebraic decomposition:

$$\sum_{i=1}^n X_i^2 = \sum_{i=1}^n (X_i - \bar{X})^2 + n \bar{X}^2$$

Dividing both sides by $\sigma^2$:

$$\frac{\sum_{i=1}^n X_i^2}{\sigma^2} = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{\sigma^2} + \frac{n \bar{X}^2}{\sigma^2}$$

From Unit 3:
- $U_1 = \frac{\sum (X_i - \bar{X})^2}{\sigma^2} \sim \chi_{n-1}^2$.
- $U_2 = \frac{n \bar{X}^2}{\sigma^2} \sim \chi_1^2$.
- $U_1$ and $U_2$ are independent Chi-Square random variables.

Therefore, the denominator is the sum of two independent Chi-Square variables: $T / \sigma^2 = U_1 + U_2 \sim \chi_n^2$.
The ratio $V$ can be written as:

$$V = \frac{U_1}{U_1 + U_2}$$

By the classical relationship between independent Chi-Square variables and the Beta distribution:
If $U_1 \sim \chi_{\nu_1}^2 \equiv \text{Gamma}(\nu_1/2, 1/2)$ and $U_2 \sim \chi_{\nu_2}^2 \equiv \text{Gamma}(\nu_2/2, 1/2)$ are independent, then:

$$\frac{U_1}{U_1 + U_2} \sim \text{Beta}\left( \frac{\nu_1}{2}, \; \frac{\nu_2}{2} \right)$$

Here, $\nu_1 = n - 1$ and $\nu_2 = 1$. Consequently:

$$V \sim \text{Beta}\left( \frac{n - 1}{2}, \; \frac{1}{2} \right)$$

The probability density function of $V$ for $v \in (0, 1)$ is:

$$f_V(v) = \frac{1}{B\left( \frac{n - 1}{2}, \frac{1}{2} \right)} v^{\frac{n - 1}{2} - 1} (1 - v)^{\frac{1}{2} - 1} = \frac{\Gamma(n/2)}{\Gamma((n-1)/2)\sqrt{\pi}} v^{\frac{n - 3}{2}} (1 - v)^{-1/2}, \quad 0 < v < 1$$

The expected value of $V$ is given by the standard Beta expectation formula:

$$\mathbb{E}[V] = \frac{\alpha}{\alpha + \beta} = \frac{\frac{n - 1}{2}}{\frac{n - 1}{2} + \frac{1}{2}} = \frac{n - 1}{n}$$

This demonstrates how Basu's Theorem and the geometry of Gaussian sampling combine to yield exact distributional results. $\blacksquare$
