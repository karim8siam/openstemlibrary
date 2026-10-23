# Unit 7: Nonparametric One-Sample & Two-Sample Rank Tests: Sign, Wilcoxon, Mann-Whitney & Scale Tests

Throughout the classical theory of parametric inference, optimal tests such as Student's one-sample and two-sample $t$-tests and Fisher's $F$-test for variance homogeneity are derived under the stringent assumption that the underlying population distributions are exactly Gaussian. In real-world scientific investigations—ranging from financial asset returns and clinical biomarker concentrations to survival times and environmental pollutant measurements—empirical distributions frequently exhibit severe skewness, heavy leptokurtic tails, gross recording outliers, or purely ordinal measurement scales where arithmetic means and variances are distorted or undefined. When a parametric model is misspecified, classical procedures suffer from two critical vulnerabilities: (1) in finite samples (and even asymptotically for variance tests), the actual Type I error probability can deviate drastically from the nominal significance level $\alpha$, and (2) under heavy-tailed distributions such as the Laplace, Logistic, or Cauchy families, the sample mean $\bar{X}$ and sample variance $S^2$ become highly inefficient, causing the power of Student's $t$-test to collapse relative to outlier-resistant alternatives.

**Nonparametric and distribution-free methods**, pioneered in the mid-twentieth century by Frank Wilcoxon (1945), Henry Mann and Donald Whitney (1947), Wassily Hoeffding (1948), Erich Lehmann (1953), and Jaroslav Hájek (1962), resolve these vulnerabilities by replacing the raw numerical magnitudes $X_1, \dots, X_n$ with their relative **signs**, **ranks**, or **order statistics**. Because the joint distribution of the ranks of independent and identically distributed continuous random variables is purely combinatorial and completely invariant under any strictly increasing transformation, rank-based hypothesis tests achieve an **exact finite-sample significance level $\alpha$ across the entire nonparametric class of continuous distributions**. Even more remarkably, as we prove via Pitman Asymptotic Relative Efficiency (ARE), rank tests sacrifice less than $4.5\%$ efficiency relative to Student's $t$-test when the true population is perfectly normal ($\text{ARE} = 3/\pi \approx 0.9549$), while achieving substantially higher—and potentially infinite—efficiency under heavy-tailed distributions! In this unit, we develop the rigorous mathematical theory of distribution-free statistics, the one-sample Sign Test and Wilcoxon Signed-Rank Test ($T^+$), Walsh averages and the Hodges-Lehmann location estimator, the two-sample Wilcoxon Rank-Sum ($W$) and Mann-Whitney ($U$) tests, linear rank statistics and normal scores (van der Waerden and Terry-Hoeffding), the Wald-Wolfowitz runs test for randomness, and nonparametric two-sample scale dispersion tests (Ansari-Bradley, Mood, and Siegel-Tukey).

## 7.1 Order Statistics, Rank Invariance, and Exact Combinatorial Null Distributions

Let $X_1, X_2, \dots, X_n$ be independent and identically distributed random variables with common cumulative distribution function $F(x) \in \mathcal{F}_c$, where $\mathcal{F}_c$ denotes the class of all **continuous** cumulative distribution functions on $\mathbb{R}$. Because $F$ is continuous, the probability of any two observations taking the exact same numerical value (a tie) is zero: $\mathbb{P}_F(X_i = X_j) = 0$ for all $i \ne j$. Consequently, with probability one, sorting the sample observations in strictly ascending magnitude produces the unique **Order Statistics**:

$$X_{(1)} < X_{(2)} < \dots < X_{(n)}$$

While the order statistics $(X_{(1)}, \dots, X_{(n)})$ capture the numerical magnitudes of the sample (and in fact form a **complete sufficient statistic** for the entire nonparametric family $\mathcal{F}_c$), we can separate the sample information into two complementary, statistically independent components under $H_0$: the ordered magnitudes $X_{(\cdot)} = (X_{(1)}, \dots, X_{(n)})$ and the **Rank Vector** $\mathbf{R} = (R_1, R_2, \dots, R_n)$, where the rank $R_i$ of observation $X_i$ is defined as the number of sample observations less than or equal to $X_i$:

$$R_i = \sum_{j=1}^n \mathbb{I}\left( X_j \le X_i \right) \in \{1, 2, \dots, n\}, \quad \text{so that } X_i = X_{(R_i)}$$

Equivalently, we define the **Anti-Rank Vector** $\mathbf{D} = (D_1, \dots, D_n)$ as the inverse permutation of $\mathbf{R}$, where $D_k$ is the index of the observation that achieved rank $k$: $X_{(k)} = X_{D_k}$.

Why do the ranks $\mathbf{R} = (R_1, \dots, R_n)$ form the universal building blocks of nonparametric hypothesis testing? Two foundational theorems explain their power: **Maximal Invariance under Monotone Transformations** and **Exact Uniformity over the Symmetric Group $\mathcal{S}_n$**.

### Theorem 7.1 (Combinatorial Uniformity, Moments, and Independence of Ranks and Order Statistics)
Let $X_1, X_2, \dots, X_n \stackrel{\text{i.i.d.}}{\sim} F \in \mathcal{F}_c$ be a random sample from any continuous distribution $F$. Let $\mathcal{S}_n$ denote the symmetric group of all $n!$ permutations $\mathbf{r} = (r_1, r_2, \dots, r_n)$ of $\{1, 2, \dots, n\}$. Then:
1. **Distribution-Free Uniformity**: The rank vector $\mathbf{R} = (R_1, \dots, R_n)$ is uniformly distributed over $\mathcal{S}_n$:
   $$\mathbb{P}_F\left( \mathbf{R} = \mathbf{r} \right) = \frac{1}{n!} \quad \text{for every } \mathbf{r} \in \mathcal{S}_n \text{ and every } F \in \mathcal{F}_c$$
2. **Statistical Independence of Ranks and Order Statistics**: The rank vector $\mathbf{R}$ and the order statistic vector $X_{(\cdot)} = (X_{(1)}, \dots, X_{(n)})$ are statistically independent under any $F \in \mathcal{F}_c$.
3. **Maximal Invariance**: Let $\mathcal{G}$ be the group of all strictly increasing, continuous transformations $g : \mathbb{R} \to \mathbb{R}$ acting coordinate-wise via $g(X_1, \dots, X_n) = (g(X_1), \dots, g(X_n))$. The rank vector $\mathbf{R}(X_1, \dots, X_n)$ is a **maximal invariant** under $\mathcal{G}$, meaning every distribution-free statistic invariant under monotone transformations is strictly a function of the ranks $\mathbf{R}$.
4. **Exact Marginal Moments and Covariance of Ranks**: For every $i \ne j \in \{1, \dots, n\}$:
   $$\mathbb{E}[R_i] = \frac{n + 1}{2}, \qquad \text{Var}(R_i) = \frac{n^2 - 1}{12}, \qquad \text{Cov}(R_i, R_j) = -\frac{n + 1}{12}$$

#### Proof:
Because $X_1, \dots, X_n$ are i.i.d. (and hence exchangeable), for any permutation $\mathbf{r} \in \mathcal{S}_n$, the event $\{\mathbf{R} = \mathbf{r}\} = \{X_{d_1} < X_{d_2} < \dots < X_{d_n}\}$ has the exact same probability as $\{X_1 < X_2 < \dots < X_n\}$. Since ties have probability zero under $F \in \mathcal{F}_c$, the $n!$ strict ordering events form a mutually exclusive partition of the sample space (up to a null set of measure zero), so $n! \, \mathbb{P}_F(\mathbf{R} = \mathbf{r}) = 1 \implies \mathbb{P}_F(\mathbf{R} = \mathbf{r}) = \frac{1}{n!}$. Moreover, conditioned on the order statistics $X_{(\cdot)} = (x_{(1)}, \dots, x_{(n)})$, exchangeability implies that each of the $n!$ assignments of $(x_{(1)}, \dots, x_{(n)})$ to $(X_1, \dots, X_n)$ has conditional probability $1/n!$, which does not depend on $x_{(\cdot)}$, proving that $\mathbf{R}$ and $X_{(\cdot)}$ are independent!
To verify maximal invariance, note that if $g \in \mathcal{G}$ is strictly increasing, $X_j \le X_i \iff g(X_j) \le g(X_i)$, so $\mathbf{R}(g(\mathbf{X})) = \mathbf{R}(\mathbf{X})$. Conversely, if two untied vectors $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$ have the same rank vector $\mathbf{R}(\mathbf{x}) = \mathbf{R}(\mathbf{y})$, then $x_{(1)} < \dots < x_{(n)}$ and $y_{(1)} < \dots < y_{(n)}$ are in the exact same order, so piecewise-linear interpolation between the points $(x_{(k)}, y_{(k)})$ constructs a strictly increasing continuous function $g \in \mathcal{G}$ mapping $g(x_i) = y_i$ for all $i$.
Finally, since $R_i$ is marginally uniform on $\{1, 2, \dots, n\}$ with PMF $\mathbb{P}(R_i = k) = 1/n$:

$$\mathbb{E}[R_i] = \frac{1}{n} \sum_{k=1}^n k = \frac{n + 1}{2}, \qquad \text{Var}(R_i) = \frac{1}{n}\sum_{k=1}^n k^2 - \left(\frac{n+1}{2}\right)^2 = \frac{(n+1)(2n+1)}{6} - \frac{(n+1)^2}{4} = \frac{n^2 - 1}{12}$$

Because the sum of all $n$ ranks is the deterministic constant $\sum_{i=1}^n R_i = \frac{n(n+1)}{2}$, the variance of the sum is zero:

$$0 = \text{Var}\left(\sum_{i=1}^n R_i\right) = n \text{Var}(R_1) + n(n - 1) \text{Cov}(R_1, R_2) \implies \text{Cov}(R_1, R_2) = -\frac{\text{Var}(R_1)}{n - 1} = -\frac{n + 1}{12}$$

If $F$ has a probability density function $f(x)$, the exact marginal density of the $k$-th order statistic $X_{(k)}$ is given by the Beta-transformed integral:

$$f_{X_{(k)}}(x) = \frac{n!}{(k - 1)!(n - k)!} \left[ F(x) \right]^{k - 1} \left[ 1 - F(x) \right]^{n - k} f(x)$$

and the Probability Integral Transform $U_{(k)} = F(X_{(k)}) \sim \text{Beta}(k, n - k + 1)$ has exact mean $\mathbb{E}[F(X_{(k)})] = \frac{k}{n + 1}$ and variance $\text{Var}(F(X_{(k)})) = \frac{k(n - k + 1)}{(n + 1)^2(n + 2)}$, irrespective of $F \in \mathcal{F}_c$!

## 7.2 One-Sample & Paired Sign Test and Wilcoxon Signed-Rank Test ($T^+$)

Consider the one-sample location problem (or equivalently the paired-sample difference problem $X_i = Y_{i1} - Y_{i2}$ for $n$ matched pairs), where $X_1, X_2, \dots, X_n$ are i.i.d. observations from a continuous distribution $F(x - \theta)$ with unique population median $\theta_0$ under $H_0$. Without loss of generality, by subtracting the hypothesized median $\theta_0$ from each observation ($D_i = X_i - \theta_0$), we test the canonical null hypothesis $H_0 : \theta = 0$ against $H_1 : \theta > 0$ (or two-sided $H_1 : \theta \ne 0$).

### 1. The Sign Test ($B$)
The **Sign Test**, originally used by John Arbuthnot in 1710 to analyze London christening records, makes **no symmetry assumption whatsoever** about $F$: it requires only that $F(0) = \mathbb{P}_{H_0}(X_i < 0) = \mathbb{P}_{H_0}(X_i > 0) = 1/2$ (i.e., the population median is $0$). Define the positive sign indicators $S_i = \mathbb{I}(X_i > 0)$ for $i = 1, \dots, n$ (discarding any exact zero differences $X_i = 0$ and reducing $n$ to the number of non-zero observations). The Sign Test statistic is the total count of positive observations:

$$B = \sum_{i=1}^n \mathbb{I}(X_i > 0) \stackrel{H_0}{\sim} \text{Binomial}\left(n, \frac{1}{2}\right)$$

Under $H_0$, $\mathbb{E}_{H_0}[B] = \frac{n}{2}$ and $\text{Var}_{H_0}(B) = \frac{n}{4}$, with exact right-tail $p$-value $\mathbb{P}_{H_0}(B \ge b_{\text{obs}}) = 2^{-n} \sum_{k = b_{\text{obs}}}^n \binom{n}{k}$ and continuity-corrected normal approximation $Z = \frac{B - 0.5 - n/2}{\sqrt{n/4}} \xrightarrow{d} \mathcal{N}(0, 1)$. Moreover, inverting the Sign Test yields an exact **Distribution-Free Confidence Interval for the Population Median $M$** bounded by symmetric order statistics:

$$\mathbb{P}_F\left( X_{(k)} \le M \le X_{(n - k + 1)} \right) = 1 - 2 \sum_{j=0}^{k-1} \binom{n}{j} \left(\frac{1}{2}\right)^n = \sum_{j=k}^{n-k} \binom{n}{j} \left(\frac{1}{2}\right)^n$$

### 2. Frank Wilcoxon's Signed-Rank Test ($T^+$)
While the Sign Test is completely robust to skewness, it discards all information about the **relative magnitudes** of the deviations $|X_i|$: an observation of $+0.001$ receives the exact same weight $+1$ as an observation of $+100.0$. Suppose now that under $H_0$, the underlying distribution $F$ is **continuous and symmetric about $0$**, so that $F(-x) = 1 - F(x)$ (or in terms of the density, $f(-x) = f(x)$ for all $x \in \mathbb{R}$). Frank Wilcoxon (1945) recognized that under symmetry about $0$, not only are the signs $\text{sgn}(X_i)$ independent $\text{Bernoulli}(1/2)$ trials, but the **absolute values** $|X_1|, |X_2|, \dots, |X_n|$ are statistically independent of the signs!

Let $R_i^+ = \text{Rank}(|X_i|)$ denote the rank of the absolute magnitude $|X_i|$ among $\{|X_1|, |X_2|, \dots, |X_n|\}$ arranged from smallest ($1$) to largest ($n$). **Wilcoxon's Signed-Rank Statistic $T^+$** is defined as the sum of the ranks of the absolute values corresponding to the strictly positive observations:

$$T^+ = \sum_{i=1}^n R_i^+ \mathbb{I}(X_i > 0) = \sum_{k=1}^n k \, W_k, \quad \text{where } W_k = \mathbb{I}\left( \text{observation with } |X|_{(\text{rank } k)} \text{ is positive} \right)$$

Similarly, let $T^- = \sum_{i=1}^n R_i^+ \mathbb{I}(X_i < 0) = \sum_{k=1}^n k(1 - W_k)$ be the sum of the negative signed ranks, so that $T^+ + T^- = \sum_{k=1}^n k = \frac{n(n+1)}{2}$, and the difference is $T = T^+ - T^- = 2 T^+ - \frac{n(n+1)}{2} = \sum_{i=1}^n \text{sgn}(X_i) R_i^+$.

### Theorem 7.2 (Exact Null Distribution, Moment Generating Function, Recursion, and Moments of $T^+$)
Under the null hypothesis $H_0$ that $X_1, \dots, X_n$ are i.i.d. from a continuous distribution symmetric about $0$:
1. **Mutual Independence of Signed-Rank Indicators**: The indicator variables $W_1, W_2, \dots, W_n$ are **mutually independent and identically distributed $\text{Bernoulli}(1/2)$ random variables**: $\mathbb{P}_{H_0}(W_1 = w_1, \dots, W_n = w_n) = 2^{-n}$ for all $(w_1, \dots, w_n) \in \{0, 1\}^n$.
2. **Exact Moment Generating Function and Symmetric Recursion**: The MGF of $T^+ = \sum_{k=1}^n k W_k$ is:
   $$M_{T^+}(t) = \mathbb{E}_{H_0}\left[ e^{t T^+} \right] = \prod_{k=1}^n \left( \frac{1 + e^{kt}}{2} \right)$$
   Consequently, $T^+$ is symmetrically distributed about $\frac{n(n+1)}{4}$ on $\left\{0, 1, \dots, \frac{n(n+1)}{2}\right\}$, and the number $c_n(u)$ of sign configurations summing to $T^+ = u$ (where $\mathbb{P}_{H_0}(T^+ = u) = c_n(u) / 2^n$) satisfies the exact dynamic programming recursion:
   $$c_n(u) = c_{n-1}(u) + c_{n-1}(u - n), \quad \text{with } c_0(0) = 1 \text{ and } c_0(u) = 0 \text{ for } u \ne 0$$
3. **Exact Null Mean, Variance, and Tie-Corrected Variance**:
   $$\mathbb{E}_{H_0}[T^+] = \frac{n(n + 1)}{4}, \qquad \text{Var}_{H_0}(T^+) = \frac{n(n + 1)(2n + 1)}{24}$$
   If there are $g$ groups of tied absolute values $|X_i|$ of sizes $t_1, t_2, \dots, t_g$ (assigned average mid-ranks), the exact conditional variance of $T^+$ reduces to:
   $$\text{Var}_{H_0, \text{ties}}(T^+) = \frac{n(n + 1)(2n + 1)}{24} - \frac{1}{48} \sum_{j=1}^g t_j (t_j^2 - 1)$$

#### Proof:
Under $H_0$, $f(-x) = f(x)$, so for each observation $X_i$, the conditional probability that $X_i > 0$ given its magnitude $|X_i| = y > 0$ is $\mathbb{P}_{H_0}(X_i > 0 \mid |X_i| = y) = \frac{f(y)}{f(y) + f(-y)} = \frac{1}{2}$. Because the pairs $(\text{sgn}(X_i), |X_i|)$ are independent across $i = 1, \dots, n$, and $\text{sgn}(X_i)$ is independent of $|X_i|$, re-indexing the signs by the order of $|X|_{(1)} < \dots < |X|_{(n)}$ preserves the i.i.d. $\text{Bernoulli}(1/2)$ distribution of $W_k = \mathbb{I}(X_{D_k^+} > 0)$.
Because $T^+ = \sum_{k=1}^n k W_k$ is a linear combination of **independent** $\text{Bernoulli}(1/2)$ random variables with $\mathbb{E}[W_k] = 1/2$ and $\text{Var}(W_k) = 1/4$, the mean and variance follow immediately without any covariance terms:

$$\mathbb{E}_{H_0}[T^+] = \sum_{k=1}^n k \left(\frac{1}{2}\right) = \frac{n(n + 1)}{4}, \qquad \text{Var}_{H_0}(T^+) = \sum_{k=1}^n k^2 \left(\frac{1}{4}\right) = \frac{n(n + 1)(2n + 1)}{24}$$

By the Lindeberg-Feller Central Limit Theorem (since the maximum variance contribution $\frac{n^2/4}{\text{Var}(T^+)} = \frac{6n}{(n+1)(2n+1)} \to 0$ as $n \to \infty$), the standardized statistic is asymptotically standard normal:

$$Z = \frac{T^+ - \frac{n(n+1)}{4}}{\sqrt{\frac{n(n+1)(2n+1)}{24}}} \xrightarrow{d} \mathcal{N}(0, 1)$$

### 3. Walsh Averages and the Hodges-Lehmann Estimator ($\hat{\theta}_{\text{HL}}$)
Remarkably, the Wilcoxon Signed-Rank statistic $T^+$ has a dual representation in terms of the $\frac{n(n+1)}{2}$ pairwise **Walsh Averages** (John E. Walsh, 1949):

$$A_{ij} = \frac{X_i + X_j}{2}, \quad \text{for all } 1 \le i \le j \le n$$

### Theorem 7.3 (Walsh Average Representation of $T^+$ and the Hodges-Lehmann Estimator)
For any untied sample $X_1, \dots, X_n$, the Wilcoxon Signed-Rank statistic $T^+$ equals the exact number of positive Walsh averages:

$$T^+ = \sum_{i=1}^n R_i^+ \mathbb{I}(X_i > 0) = \sum_{1 \le i \le j \le n} \mathbb{I}\left( \frac{X_i + X_j}{2} > 0 \right)$$

Consequently, the **Hodges-Lehmann Point Estimator** $\hat{\theta}_{\text{HL}}$ of the symmetry center $\theta$—defined as the value of $\theta_0$ at which $T^+(\theta_0)$ equals its null median $\frac{n(n+1)}{4}$—is the **median of the $\frac{n(n+1)}{2}$ Walsh averages**:

$$\hat{\theta}_{\text{HL}} = \text{Median}_{1 \le i \le j \le n} \left( \frac{X_i + X_j}{2} \right)$$

#### Proof:
Notice that for any pair $1 \le i \le j \le n$, the Walsh average $\frac{X_i + X_j}{2} > 0 \iff X_i + X_j > 0$. If $i = j$, then $\frac{X_i + X_i}{2} = X_i > 0 \iff \mathbb{I}(X_i > 0) = 1$. If $i \ne j$ with $|X_j| < |X_i|$, then the sign of $X_i + X_j$ is strictly governed by the sign of the larger-magnitude observation $X_i$: specifically, $X_i + X_j > 0 \iff X_i > 0$! Therefore, for each observation $X_i$ with $X_i > 0$, the number of indices $j \in \{1, \dots, n\}$ satisfying $|X_j| \le |X_i|$ and $X_i + X_j > 0$ is precisely $R_i^+ = \text{Rank}(|X_i|)$. Summing over all $i$ with $X_i > 0$ yields $\sum_{1 \le i \le j \le n} \mathbb{I}\left(\frac{X_i + X_j}{2} > 0\right) = \sum_{i=1}^n R_i^+ \mathbb{I}(X_i > 0) = T^+$.

## 7.3 Two-Sample Location Problem: Wilcoxon Rank-Sum ($W$) and Mann-Whitney ($U$) Tests

Now consider two independent random samples $X_1, \dots, X_{n_1} \stackrel{\text{i.i.d.}}{\sim} F(x)$ and $Y_1, \dots, Y_{n_2} \stackrel{\text{i.i.d.}}{\sim} G(y)$ of sizes $n_1$ and $n_2$, where both $F$ and $G$ are continuous distributions and $N = n_1 + n_2$ denotes the total combined sample size. Under the **location-shift model**, $G(y) = F(y - \Delta)$, where $\Delta \in \mathbb{R}$ represents the treatment shift parameter (or more generally, under the stochastic dominance alternative, $\mathbb{P}(X < Y) \ne 1/2$). We wish to test the null hypothesis of distributional identity:

$$H_0 : F(x) = G(x) \text{ for all } x \in \mathbb{R} \quad (\text{i.e., } \Delta = 0) \qquad \text{vs.} \qquad H_1 : \Delta \ne 0 \text{ (or } \Delta > 0\text{)}$$

In 1945, Frank Wilcoxon proposed pooling all $N = n_1 + n_2$ observations into a single combined sample, sorting them in ascending order from $1$ to $N$, and computing the **Wilcoxon Rank-Sum Statistic $W_X$** (or $W_Y$), defined as the sum of the combined-sample ranks $R(X_i)$ assigned to the first sample $X_1, \dots, X_{n_1}$:

$$W_X = \sum_{i=1}^{n_1} R(X_i), \qquad W_Y = \sum_{j=1}^{n_2} R(Y_j), \qquad \text{with } W_X + W_Y = \frac{N(N + 1)}{2}$$

Two years later, Henry B. Mann and Donald R. Whitney (1947) independently formulated the **Mann-Whitney $U$ Statistic**, which counts the number of all $n_1 n_2$ cross-sample pairs $(X_i, Y_j)$ in which $Y_j$ precedes $X_i$ (or $X_i$ precedes $Y_j$):

$$U_X = \sum_{i=1}^{n_1} \sum_{j=1}^{n_2} \mathbb{I}\left( X_i > Y_j \right), \qquad U_Y = \sum_{i=1}^{n_1} \sum_{j=1}^{n_2} \mathbb{I}\left( Y_j > X_i \right), \qquad \text{with } U_X + U_Y = n_1 n_2$$

Notice that $\frac{U_Y}{n_1 n_2} = \frac{1}{n_1 n_2} \sum_{i=1}^{n_1} \sum_{j=1}^{n_2} \mathbb{I}(X_i < Y_j)$ is the **Minimum Variance Unbiased Estimator (and two-sample U-statistic)** of the functional $\theta(F, G) = \mathbb{P}(X < Y) = \int_{-\infty}^\infty F(y) \, dG(y)$ (the area under the Receiver Operating Characteristic curve, AUC)! Under $H_0 : F = G$, $\theta(F, F) = \int_0^1 u \, du = \frac{1}{2}$.

### Theorem 7.4 (Deterministic Equivalence of $W$ and $U$, Exact Recursion, and Null Moments)
Let $X_1, \dots, X_{n_1} \stackrel{\text{i.i.d.}}{\sim} F$ and $Y_1, \dots, Y_{n_2} \stackrel{\text{i.i.d.}}{\sim} G$ be untied continuous samples with $N = n_1 + n_2$.
1. **Exact Algebraic Equivalence of $W_X$ and $U_X$**:
   $$W_X = U_X + \frac{n_1(n_1 + 1)}{2} \quad \Longleftrightarrow \quad U_X = W_X - \frac{n_1(n_1 + 1)}{2}$$
2. **Exact Null Distribution and Mann-Whitney Recursion**: Under $H_0 : F = G$, all $\binom{n_1 + n_2}{n_1}$ subsets of size $n_1$ from $\{1, 2, \dots, N\}$ are equally likely with probability $1 / \binom{N}{n_1}$, and $p_{n_1, n_2}(u) = \mathbb{P}_{H_0}(U_X = u)$ satisfies the recursion:
   $$p_{n_1, n_2}(u) = \frac{n_1}{n_1 + n_2} p_{n_1 - 1, n_2}(u - n_2) + \frac{n_2}{n_1 + n_2} p_{n_1, n_2 - 1}(u)$$
3. **Exact Null Mean, Variance, and Tie-Corrected Variance**: Under $H_0 : F = G$:
   $$\mathbb{E}_{H_0}[U_X] = \frac{n_1 n_2}{2}, \qquad \mathbb{E}_{H_0}[W_X] = \frac{n_1(n_1 + n_2 + 1)}{2}$$
   $$\text{Var}_{H_0}(U_X) = \text{Var}_{H_0}(W_X) = \frac{n_1 n_2 (n_1 + n_2 + 1)}{12}$$
   In the presence of $g$ tied groups of sizes $t_1, \dots, t_g$ in the combined sample (assigned average mid-ranks), the exact tie-corrected null variance is:
   $$\text{Var}_{H_0, \text{ties}}(W_X) = \frac{n_1 n_2}{12}\left[ N + 1 - \frac{\sum_{j=1}^g t_j(t_j^2 - 1)}{N(N - 1)} \right]$$

#### Proof:
Arrange the first sample in ascending order $X_{(1)} < X_{(2)} < \dots < X_{(n_1)}$. Consider the rank $R(X_{(k)})$ of the $k$-th ordered $X$-observation in the combined sample of size $N$. Among the $X$-observations alone, there are exactly $k$ values less than or equal to $X_{(k)}$ (namely $X_{(1)}, \dots, X_{(k)}$); among the $Y$-observations, there are $\sum_{j=1}^{n_2} \mathbb{I}(Y_j < X_{(k)})$ values less than $X_{(k)}$. Therefore:

$$R\left(X_{(k)}\right) = k + \sum_{j=1}^{n_2} \mathbb{I}\left( Y_j < X_{(k)} \right)$$

Summing this identity over all $k = 1, 2, \dots, n_1$ yields:

$$W_X = \sum_{k=1}^{n_1} R\left(X_{(k)}\right) = \sum_{k=1}^{n_1} k + \sum_{k=1}^{n_1} \sum_{j=1}^{n_2} \mathbb{I}\left( X_{(k)} > Y_j \right) = \frac{n_1(n_1 + 1)}{2} + U_X$$

which proves $U_X = W_X - \frac{n_1(n_1+1)}{2}$! To compute the exact null mean and variance of $W_X = \sum_{i=1}^{n_1} R(X_i)$ under $H_0$, recall from Theorem 7.1(4) that the ranks $(R_1, \dots, R_N)$ of a combined sample of size $N = n_1 + n_2$ have $\mathbb{E}[R_i] = \frac{N+1}{2}$, $\text{Var}(R_i) = \frac{N^2 - 1}{12}$, and $\text{Cov}(R_i, R_j) = -\frac{N+1}{12}$ for $i \ne j$. Therefore:

$$\mathbb{E}_{H_0}[W_X] = n_1 \mathbb{E}[R_1] = \frac{n_1(N + 1)}{2} = \frac{n_1(n_1 + n_2 + 1)}{2}$$

$$\text{Var}_{H_0}(W_X) = n_1 \text{Var}(R_1) + n_1(n_1 - 1) \text{Cov}(R_1, R_2) = n_1 \left(\frac{N^2 - 1}{12}\right) - n_1(n_1 - 1)\left(\frac{N + 1}{12}\right)$$

Factoring out $\frac{n_1(N + 1)}{12}$ leaves $\frac{n_1(N + 1)}{12} \left[ (N - 1) - (n_1 - 1) \right] = \frac{n_1 n_2 (n_1 + n_2 + 1)}{12}$, completing the proof!
Furthermore, the two-sample **Hodges-Lehmann shift estimator** $\hat{\Delta}_{\text{HL}}$ associated with the Mann-Whitney test is the median of all $n_1 n_2$ pairwise cross-sample differences:

$$\hat{\Delta}_{\text{HL}} = \text{Median}_{\substack{1 \le i \le n_1 \\ 1 \le j \le n_2}} \left( Y_j - X_i \right)$$

## 7.4 General Linear Rank Statistics, Normal Scores & Pitman Asymptotic Relative Efficiency

Both the Wilcoxon Rank-Sum statistic and the normal-scores tests belong to the unified class of **Two-Sample Linear Rank Statistics** studied by Jaroslav Hájek and Erich Lehmann:

$$S_N = \sum_{i=1}^{n_1} a_N(R_i) = \sum_{k=1}^N c_k a_N(k)$$

where $c_k = 1$ if the $k$-th order statistic of the combined sample belongs to the first sample ($X$) and $c_k = 0$ otherwise, and $a_N(1) \le a_N(2) \le \dots \le a_N(N)$ is a set of monotone **rank scores** generated by a score function $\varphi : (0, 1) \to \mathbb{R}$ via either $a_N(k) = \varphi\left(\frac{k}{N + 1}\right)$ or $a_N(k) = \mathbb{E}\left[\varphi(U_{(k)})\right]$. Under $H_0$, for any score vector $a_N(1), \dots, a_N(N)$ with average $\bar{a}_N = \frac{1}{N} \sum_{k=1}^N a_N(k)$, finite-population sampling theory immediately gives the exact null mean and variance of $S_N$:

$$\mathbb{E}_{H_0}[S_N] = n_1 \bar{a}_N, \qquad \text{Var}_{H_0}(S_N) = \frac{n_1 n_2}{N(N - 1)} \sum_{k=1}^N \left( a_N(k) - \bar{a}_N \right)^2$$

Three canonical score functions $\varphi(u)$ govern location testing:
1. **Wilcoxon Scores ($\varphi(u) = u$, or $a_N(k) = k$)**: Locally Most Powerful Rank (LMPR) test when the underlying error distribution is **Logistic** with density $f(x) = \frac{e^{-x}}{(1 + e^{-x})^2}$.
2. **Sign / Median Scores ($\varphi(u) = \text{sgn}(u - 1/2)$)**: Locally Most Powerful Rank test when the underlying error distribution is **Laplace (Double Exponential)** $f(x) = \frac{1}{2} e^{-|x|}$.
3. **Normal Scores ($\varphi(u) = \Phi^{-1}(u)$)**: Locally Most Powerful Rank test when the underlying distribution is **Gaussian** $\mathcal{N}(\mu, \sigma^2)$! Two versions are used:
   - **van der Waerden (1952) Quantile Normal Scores**: $a_N(k) = \Phi^{-1}\left(\frac{k}{N + 1}\right)$.
   - **Terry-Hoeffding / Fisher-Yates Expected Normal Scores**: $a_N(k) = \mathbb{E}\left[ Z_{(k)} \right]$, where $Z_{(1)} < \dots < Z_{(N)}$ are order statistics of a standard normal sample $\mathcal{N}(0, 1)$.

How much efficiency does the Wilcoxon test ($W$ or $T^+$) retain or gain compared to Student's $t$-test under arbitrary continuous distributions $F$ with density $f(x)$ and finite variance $\sigma_F^2$? We compute the **Pitman Asymptotic Relative Efficiency (ARE)** under local shift alternatives $\Delta_N = \delta / \sqrt{N}$.

### Theorem 7.5 (Pitman ARE of Wilcoxon Tests and Normal Scores Tests Relative to Student's $t$-Test)
Let $F$ be a symmetric continuous distribution with density $f(x)$ and finite variance $\sigma^2 = \text{Var}_F(X) < \infty$.
1. **Pitman ARE of Wilcoxon ($W$ or $T^+$) vs. Student's $t$-Test**:
   $$\text{ARE}(W, t; F) = \text{ARE}(T^+, t; F) = 12 \sigma^2 \left( \int_{-\infty}^\infty f^2(x) \, dx \right)^2$$
   Moreover, **Hodges and Lehmann (1956)** proved the universal lower bound across **all** continuous densities $f$ with finite variance:
   $$\inf_{f} \text{ARE}(W, t; f) = \frac{108}{125} = 0.864$$
   achieved by the parabolic Epanechnikov kernel density $f^*(x) = \frac{3}{20\sqrt{5}}(5 - x^2) \mathbb{I}(|x| \le \sqrt{5})$.
2. **Chernoff-Savage Theorem (1958) for Normal Scores ($V_{\text{vdW}}$) vs. Student's $t$-Test**:
   $$\text{ARE}\left( V_{\text{vdW}}, t; F \right) = \sigma^2 \left( \int_{-\infty}^\infty \frac{f^2(x)}{\phi\left(\Phi^{-1}(F(x))\right)} \, dx \right)^2 \ge 1 \quad \text{for ALL } F!$$
   with equality $= 1$ if and only if $F$ is Gaussian!

#### Proof of the Wilcoxon Pitman ARE Formula and Evaluation for Gaussian, Logistic, and Laplace Laws:
Consider the one-sample test based on $U_n(\theta) = \frac{2}{n(n+1)} T^+(\theta) = \binom{n}{2}^{-1} \sum_{i < j} \mathbb{I}\left(\frac{X_i + X_j}{2} > 0\right) + O_p(n^{-1})$. Under local alternatives $\theta_n = \delta / \sqrt{n}$, the expectation of $\mathbb{I}(X_1 + X_2 > 0)$ is:

$$\mu(\theta) = \mathbb{P}_\theta(X_1 + X_2 > 0) = \mathbb{P}_0(X_1 + X_2 > -2\theta) = \int_{-\infty}^\infty \left[ 1 - F(-x - 2\theta) \right] f(x) \, dx$$

Differentiating $\mu(\theta)$ with respect to $\theta$ at $\theta = 0$ and using symmetry $f(-x) = f(x)$ yields the Pitman sensitivity slope:

$$\mu'(0) = \left. \frac{d}{d\theta} \mathbb{P}_\theta(X_1 + X_2 > 0) \right|_{\theta = 0} = 2 \int_{-\infty}^\infty f(-x) f(x) \, dx = 2 \int_{-\infty}^\infty f^2(x) \, dx$$

Under $H_0$, the asymptotic variance of $\sqrt{n}\left(U_n - \frac{1}{2}\right)$ is $\lim_{n \to \infty} n \left(\frac{2}{n(n+1)}\right)^2 \frac{n(n+1)(2n+1)}{24} = \frac{1}{3}$, so the squared Pitman efficacy of the Wilcoxon test is:

$$c_W^2 = \frac{[\mu'(0)]^2}{1/3} = \frac{\left(2 \int f^2(x) \, dx\right)^2}{1/3} = 12 \left( \int_{-\infty}^\infty f^2(x) \, dx \right)^2$$

For Student's $t$-test, the test statistic is driven by $\bar{X}$ with $\mu_t(\theta) = \theta$, $\mu_t'(0) = 1$, and variance $\sigma^2$, so its squared Pitman efficacy is $c_t^2 = \frac{1}{\sigma^2}$. Taking the ratio of squared efficacies gives:

$$\text{ARE}(W, t; F) = \frac{c_W^2}{c_t^2} = 12 \sigma^2 \left( \int_{-\infty}^\infty f^2(x) \, dx \right)^2$$

Let us evaluate this fundamental formula across four classic distributions:
- **Normal Distribution $\mathcal{N}(0, 1)$**: Here $\sigma^2 = 1$ and $\int_{-\infty}^\infty \phi^2(x) \, dx = \int_{-\infty}^\infty \frac{1}{2\pi} e^{-x^2} \, dx = \frac{1}{2\sqrt{\pi}}$. Thus:
  $$\text{ARE}(W, t; \text{Normal}) = 12 (1) \left( \frac{1}{2\sqrt{\pi}} \right)^2 = \frac{12}{4\pi} = \frac{3}{\pi} \approx 0.9549 \quad (95.5\%)$$
- **Uniform Distribution $\text{Uniform}(-1/2, 1/2)$**: Here $\sigma^2 = 1/12$ and $\int_{-1/2}^{1/2} 1^2 \, dx = 1$, so $\text{ARE}(W, t; \text{Uniform}) = 12(1/12)(1)^2 = 1.000$.
- **Logistic Distribution ($f(x) = e^{-x}/(1 + e^{-x})^2$)**: Here $\sigma^2 = \pi^2 / 3$ and $\int_{-\infty}^\infty f^2(x) \, dx = \int_0^1 u^2(1 - u)^2 \, du = \text{B}(3, 3) = \frac{1}{6}$, so:
  $$\text{ARE}(W, t; \text{Logistic}) = 12 \left(\frac{\pi^2}{3}\right) \left(\frac{1}{6}\right)^2 = \frac{\pi^2}{9} \approx 1.0966 \quad (109.7\%)$$
- **Laplace Distribution ($f(x) = \frac{1}{2}e^{-|x|}$)**: Here $\sigma^2 = 2$ and $\int_{-\infty}^\infty \frac{1}{4} e^{-2|x|} \, dx = \frac{1}{4}$, so:
  $$\text{ARE}(W, t; \text{Laplace}) = 12 (2) \left(\frac{1}{4}\right)^2 = \frac{24}{16} = 1.500 \quad (150.0\%)$$
- **Cauchy Distribution**: Since $\sigma^2 = \infty$ while $\int f^2(x) \, dx = \frac{1}{2\pi} > 0$, $\text{ARE}(W, t; \text{Cauchy}) = +\infty$!

This proves the remarkable robustness of the Wilcoxon test: it can **never** have an efficiency below $86.4\%$ relative to Student's $t$-test for any continuous distribution, retains $95.5\%$ efficiency under exact normality, and achieves $110\%$, $150\%$, or $\infty$ efficiency under heavy tails!

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Underlying Distribution $F$</th><th>ARE(Sign, $t$)</th><th>ARE(Wilcoxon $W / T^+$, $t$)</th><th>ARE(Normal Scores $V_{\text{vdW}}$, $t$)</th></tr>
</thead>
<tbody>
<tr><td><strong>Normal $\mathcal{N}(\mu, \sigma^2)$</strong></td><td>$\frac{2}{\pi} \approx 0.6366$</td><td>$\frac{3}{\pi} \approx 0.9549$</td><td>$1.0000$</td></tr>
<tr><td><strong>Uniform $(a, b)$</strong></td><td>$\frac{1}{3} \approx 0.3333$</td><td>$1.0000$</td><td>$+\infty$</td></tr>
<tr><td><strong>Logistic</strong></td><td>$\frac{\pi^2}{12} \approx 0.8225$</td><td>$\frac{\pi^2}{9} \approx 1.0966$</td><td>$\frac{\pi}{3} \approx 1.0472$</td></tr>
<tr><td><strong>Laplace (Double Exponential)</strong></td><td>$2.0000$</td><td>$1.5000$</td><td>$\frac{4}{\pi} \approx 1.2732$</td></tr>
<tr><td><strong>Cauchy / $\alpha$-Stable ($\alpha < 2$)</strong></td><td>$+\infty$</td><td>$+\infty$</td><td>$+\infty$</td></tr>
<tr><td><strong>Infimum over all continuous $F$</strong></td><td>$\frac{1}{3} \approx 0.3333$</td><td>$\frac{108}{125} = 0.8640$</td><td>$1.0000$ (Chernoff-Savage)</td></tr>
</tbody>
</table></div>

## 7.5 Nonparametric Tests for Randomness: The Wald-Wolfowitz Runs Test

Before applying any i.i.d. statistical procedure, an investigator must verify that the sequential observations $X_1, X_2, \dots, X_N$ are genuinely **random and mutually independent** over time, rather than exhibiting serial autocorrelation, cyclical oscillation, or monotonic trend. Suppose an ordered sequence of $N = n_1 + n_2$ binary symbols contains $n_1$ elements of Type 1 (e.g., `+`, Heads, or observations above the sample median $\tilde{X}$) and $n_2$ elements of Type 2 (e.g., `-`, Tails, or observations below $\tilde{X}$).

A **run** is defined as a maximal contiguous subsequence of identical symbols. For example, the sequence `+ + + - - + - - - - + +` of length $N = 12$ ($n_1 = 6$ pluses and $n_2 = 6$ minuses) consists of $R = 5$ runs: `+++`, `--`, `+`, `----`, `++`. Notice how the total number of runs $R$ diagnoses departures from randomness:
- **Too few runs ($R$ abnormally small)**: Indicates positive serial correlation, clustering, or a secular trend (e.g., `++++++------` has $R = 2$ runs).
- **Too many runs ($R$ abnormally large)**: Indicates negative serial correlation or rapid systematic alternation (e.g., `+-+-+-+-+-+-` has $R = 12$ runs).

### Theorem 7.6 (Exact Combinatorial Null Distribution and Moments of the Wald-Wolfowitz Runs Statistic $R$)
Under the null hypothesis $H_0$ of randomness, all $\binom{n_1 + n_2}{n_1}$ arrangements of $n_1$ symbols of Type 1 and $n_2$ symbols of Type 2 are equally likely. Let $R$ denote the total number of runs ($2 \le R \le 2\min(n_1, n_2) + 1$).
1. **Exact Probability Mass Function**: For any integer $k \ge 1$:
   $$\mathbb{P}_{H_0}(R = 2k) = \frac{2 \binom{n_1 - 1}{k - 1} \binom{n_2 - 1}{k - 1}}{\binom{n_1 + n_2}{n_1}}, \qquad \mathbb{P}_{H_0}(R = 2k + 1) = \frac{\binom{n_1 - 1}{k} \binom{n_2 - 1}{k - 1} + \binom{n_1 - 1}{k - 1} \binom{n_2 - 1}{k}}{\binom{n_1 + n_2}{n_1}}$$
2. **Exact Null Mean and Variance**:
   $$\mathbb{E}_{H_0}[R] = \frac{2 n_1 n_2}{n_1 + n_2} + 1, \qquad \text{Var}_{H_0}(R) = \frac{2 n_1 n_2 (2 n_1 n_2 - n_1 - n_2)}{(n_1 + n_2)^2 (n_1 + n_2 - 1)}$$

#### Proof:
To obtain exactly $R = 2k$ runs, the $n_1$ Type 1 symbols must be partitioned into $k$ non-empty contiguous blocks and the $n_2$ Type 2 symbols must also be partitioned into $k$ non-empty contiguous blocks, which then interleave either starting with Type 1 (`1-2-1-2...`) or starting with Type 2 (`2-1-2-1...`). By the classic "stars and bars" combinatorial lemma, the number of ways to place $k - 1$ dividers into the $n_1 - 1$ internal gaps between $n_1$ identical Type 1 items is $\binom{n_1 - 1}{k - 1}$, and similarly $\binom{n_2 - 1}{k - 1}$ for Type 2. Multiplying by $2$ for the two starting choices gives $2 \binom{n_1 - 1}{k - 1} \binom{n_2 - 1}{k - 1}$ favorable arrangements out of $\binom{n_1 + n_2}{n_1}$. For $R = 2k + 1$ odd runs, either Type 1 has $k + 1$ blocks and Type 2 has $k$ blocks ($\binom{n_1 - 1}{k}\binom{n_2 - 1}{k - 1}$ ways) or vice versa.
To derive $\mathbb{E}_{H_0}[R]$ effortlessly, express $R$ as $1$ plus the sum of $N - 1$ transition indicators:

$$R = 1 + \sum_{j=1}^{N - 1} I_j, \quad \text{where } I_j = \mathbb{I}\left( \text{symbol } j \ne \text{symbol } j + 1 \right)$$

At any adjacent pair $(j, j+1)$, the probability that one symbol is Type 1 and the other is Type 2 is $\mathbb{E}_{H_0}[I_j] = \frac{2 n_1 n_2}{N(N - 1)}$. Summing over all $N - 1$ adjacent transitions immediately gives:

$$\mathbb{E}_{H_0}[R] = 1 + (N - 1) \frac{2 n_1 n_2}{N(N - 1)} = 1 + \frac{2 n_1 n_2}{n_1 + n_2}$$

Similarly, expanding $\text{Var}_{H_0}\left(\sum_{j=1}^{N-1} I_j\right)$ across adjacent overlapping pairs ($|j - l| = 1$) and disjoint pairs ($|j - l| \ge 2$) yields $\text{Var}_{H_0}(R) = \frac{2 n_1 n_2(2 n_1 n_2 - n_1 - n_2)}{(n_1 + n_2)^2(n_1 + n_2 - 1)}$.

## 7.6 Two-Sample Nonparametric Scale Dispersion Tests: Ansari-Bradley, Mood & Siegel-Tukey

In classical parametric analysis, testing the equality of two population dispersions $H_0 : \sigma_1^2 = \sigma_2^2$ relies on the two-sample variance ratio $F = S_1^2 / S_2^2 \sim F_{n_1 - 1, n_2 - 1}$. As George Box (1953) memorably remarked, however, the parametric $F$-test for variances is so violently non-robust to kurtosis $\gamma_2 = \frac{\mathbb{E}[(X - \mu)^4]}{\sigma^4} - 3 \ne 0$ (since $\sqrt{n}(S^2 - \sigma^2) \xrightarrow{d} \mathcal{N}(0, \sigma^4(2 + \gamma_2))$) that *"to make the preliminary test on variances is rather like putting to sea in arowing boat to find out whether conditions are sufficiently calm for an ocean liner to leave port!"*

To construct **exact distribution-free tests for scale dispersion**, let $X_1, \dots, X_{n_1} \stackrel{\text{i.i.d.}}{\sim} F\left(\frac{x - \theta}{\sigma_1}\right)$ and $Y_1, \dots, Y_{n_2} \stackrel{\text{i.i.d.}}{\sim} F\left(\frac{y - \theta}{\sigma_2}\right)$ share a common median $\theta$ (or have been centered by subtracting known/estimated medians) and test $H_0 : \sigma_1 = \sigma_2$ against $H_1 : \sigma_1 \ne \sigma_2$ (with $N = n_1 + n_2$). Because a sample with larger scale $\sigma_1 > \sigma_2$ places its observations at both the **extreme lower ranks** ($1, 2, \dots$) and the **extreme upper ranks** ($N, N-1, \dots$) of the combined sample while the less dispersed sample clusters near the middle rank $\frac{N+1}{2}$, linear rank tests for scale assign symmetric U-shaped or V-shaped scores $a_N(k)$ based on distance from the center:

1. **Mood's Quadratic Rank Dispersion Test (1954)**: Assigns squared deviations from the average rank $\frac{N+1}{2}$:
   $$M = \sum_{i=1}^{n_1} \left( R(X_i) - \frac{N + 1}{2} \right)^2$$
   Under $H_0$, applying the linear rank formulas with $\bar{a}_N = \frac{N^2 - 1}{12}$ gives exact null moments:
   $$\mathbb{E}_{H_0}[M] = \frac{n_1(N^2 - 1)}{12}, \qquad \text{Var}_{H_0}(M) = \frac{n_1 n_2 (N + 1)(N^2 - 4)}{180}$$
   Relative to the parametric $F$-test under normality, Mood's test has Pitman efficiency $\text{ARE}(M, F; \text{Normal}) = \frac{15}{2\pi^2} \approx 0.760$.
2. **Ansari-Bradley Symmetric Folding Rank Test (1960)**: Assigns rank $1$ to both the smallest ($k = 1$) and largest ($k = N$) observations, rank $2$ to the second smallest ($k = 2$) and second largest ($k = N - 1$), continuing inward toward the median:
   $$a_N(k) = \min(k, N - k + 1) = \frac{N + 1}{2} - \left| k - \frac{N + 1}{2} \right|, \qquad AB = \sum_{i=1}^{n_1} a_N\left(R(X_i)\right)$$
   Note that smaller values of $AB$ correspond to larger dispersion $\sigma_1 > \sigma_2$ (since outer extremes receive small scores $1, 2, \dots$). Under $H_0$:
   - **For $N = n_1 + n_2$ even**:
     $$\mathbb{E}_{H_0}[AB] = \frac{n_1(N + 2)}{4}, \qquad \text{Var}_{H_0}(AB) = \frac{n_1 n_2 (N^2 - 4)}{48(N - 1)}$$
   - **For $N = n_1 + n_2$ odd**:
     $$\mathbb{E}_{H_0}[AB] = \frac{n_1(N + 1)^2}{4 N}, \qquad \text{Var}_{H_0}(AB) = \frac{n_1 n_2 (N + 1)(N^2 + 3)}{48 N^2}$$
   Under normality, $\text{ARE}(AB, F; \text{Normal}) = \frac{6}{\pi^2} \approx 0.608$.
3. **Siegel-Tukey Alternating Rank Test (1960)**: Instead of assigning tied scores $(1, 2, \dots, 2, 1)$ to the two ends as in Ansari-Bradley, Sidney Siegel and John W. Tukey assigned distinct alternating integer ranks from $1$ to $N$ starting at the outside extremes: rank $1$ to $Z_{(1)}$, ranks $2, 3$ to $Z_{(N)}, Z_{(N-1)}$, ranks $4, 5$ to $Z_{(2)}, Z_{(3)}$, and so on inward:
   $$\text{Scores: } (1, \; 4, \; 5, \; 8, \; 9, \; \dots, \; 10, \; 7, \; 6, \; 3, \; 2)$$
   Because the Siegel-Tukey scores are a permutation of the exact integers $\{1, 2, \dots, N\}$, the null distribution, critical values, mean $\frac{n_1(N+1)}{2}$, and variance $\frac{n_1 n_2(N+1)}{12}$ of the Siegel-Tukey statistic $ST$ are **identically equal to those of the Wilcoxon Rank-Sum statistic $W_X$**, allowing investigators to use standard Wilcoxon tables to test for scale differences!

### Handling Unknown Location Nuisance Parameters in Scale Tests: The Fligner-Killeen, Levene, and Moses Tests
A critical practical caveat when applying the classical Mood ($M$), Ansari-Bradley ($AB$), or Siegel-Tukey ($ST$) rank dispersion tests is their foundational assumption that the two populations $F\left(\frac{x - \theta_1}{\sigma_1}\right)$ and $F\left(\frac{y - \theta_2}{\sigma_2}\right)$ share an **identical known location parameter** $\theta_1 = \theta_2 = \theta$. If the true medians differ ($\theta_1 \ne \theta_2$) and an investigator applies the Ansari-Bradley or Mood test directly to the uncentered raw observations, the location difference shifts one sample entirely toward the upper ranks and the other toward the lower ranks, confounding location shift with dispersion and invalidating the Type I error rate!

What if we center each sample first by subtracting its respective sample median—defining the median-centered residuals $\tilde{X}_i = X_i - \tilde{X}$ and $\tilde{Y}_j = Y_j - \tilde{Y}$—before ranking? Raghu Raj Bahadur and Erich Lehmann showed that while plug-in median centering restores asymptotic validity when the underlying density $f(x)$ is symmetric, if $f(x)$ is **asymmetric (skewed)**, the estimation error in $\tilde{X}$ and $\tilde{Y}$ induces a correlation between the centered ranks that distorts the asymptotic null variance of the Ansari-Bradley and Mood tests! Three robust nonparametric procedures overcome this location-nuisance difficulty:

1. **The Fligner-Killeen (1976) Normal-Scores Dispersion Test**: Michael A. Fligner and Timothy J. Killeen centered each sample around its sample median ($\left|X_i - \tilde{X}\right|$ and $\left|Y_j - \tilde{Y}\right|$), ranked the $N = n_1 + n_2$ absolute deviations from $1$ to $N$, and assigned **folded normal quantile scores**:
   $$a_N(k) = \Phi^{-1}\left( \frac{1 + \frac{k}{N + 1}}{2} \right), \quad k = 1, 2, \dots, N$$
   Remarkably, because the derivative of the folded normal score function is symmetric, the Fligner-Killeen statistic is asymptotically distribution-free across symmetric densities and achieves a Pitman ARE of **$100\%$ ($\text{ARE} = 1.000$) relative to the classical $F$-test under normality**, while remaining highly resistant to heavy tails and outliers!
2. **The Brown-Forsythe (1974) / Median-Centered Levene Test**: Applies a one-way analysis of variance (or two-sample $t$-test / rank-sum test) directly to the absolute deviations from the group medians $Z_{1i} = |X_i - \tilde{X}|$ and $Z_{2j} = |Y_j - \tilde{Y}|$. Unlike Howard Levene's (1960) original mean-centered deviations $|X_i - \bar{X}|$, which suffer from Type I error inflation under skewed distributions, the Brown-Forsythe median-centered transformation maintains accurate size across skewed and heavy-tailed families.
3. **Moses' (1963) Rank-Like Dispersion Test without Centering**: Lincoln E. Moses constructed a genuinely distribution-free dispersion test that requires **no knowledge or estimation of the location parameters $\theta_1, \theta_2$** even under arbitrary skewness! The Moses procedure randomly partitions Sample $X$ into $m_1$ small subgroups of fixed size $k$ (e.g., $k = 3$ or $4$) and Sample $Y$ into $m_2$ small subgroups of size $k$, computes the within-subgroup sum of squared deviations $S_{X, r}^2$ and $S_{Y, s}^2$ inside each subgroup, and applies the two-sample Wilcoxon Rank-Sum test to the $m_1 + m_2$ independent subgroup variances. Because each within-subgroup variance is strictly location-invariant ($S^2(X + \theta_1) = S^2(X)$), the resulting Wilcoxon rank-sum test on the subgroup dispersions is **exact and strictly distribution-free** regardless of any location difference $\theta_1 \ne \theta_2$ or population skewness!

---

## Worked Questions and Solutions

### Question 1: Paired Wilcoxon Signed-Rank Test ($T^+$), Tie Adjustments, Walsh Averages, and Hodges-Lehmann Estimator
A clinical pharmacology study evaluates a novel antihypertensive compound on $n = 8$ patients by measuring systolic blood pressure reduction $X_i = \text{BP}_{\text{baseline}, i} - \text{BP}_{\text{post}, i}$ (in mmHg) after 4 weeks of therapy, yielding the observed differences:

$$X_1 = -3.0, \quad X_2 = +5.0, \quad X_3 = +5.0, \quad X_4 = +8.0, \quad X_5 = -1.0, \quad X_6 = +11.0, \quad X_7 = +14.0, \quad X_8 = +18.0$$

1. Rank the absolute differences $|X_i|$ using mid-ranks for ties, compute the Wilcoxon Signed-Rank statistic $T^+$, and calculate both the unadjusted null variance $\text{Var}_{H_0}(T^+)$ and the exact tie-corrected variance $\text{Var}_{H_0, \text{ties}}(T^+)$.
2. Perform a one-sided hypothesis test of $H_0 : \theta = 0$ against $H_1 : \theta > 0$ at significance level $\alpha = 0.025$ using both the exact combinatorial tail probability (on untied bounds) and the tie-corrected normal approximation $Z$.
3. Compute all $\frac{8(9)}{2} = 36$ pairwise Walsh averages $\frac{X_i + X_j}{2}$ ($1 \le i \le j \le 8$) to determine the exact Hodges-Lehmann point estimator $\hat{\theta}_{\text{HL}}$ and compare it with the sample mean $\bar{X}$ and sample median $\tilde{X}$.

### Solution, step 1: Signed ranks with mid-rank tie assignment and exact variance calculation
Sorting the $n = 8$ observations by their absolute magnitudes $|X_i|$ gives:
- $|X_5| = |-1.0| = 1.0$ (Negative): Rank $R_5^+ = 1$
- $|X_1| = |-3.0| = 3.0$ (Negative): Rank $R_1^+ = 2$
- $|X_2| = |+5.0| = 5.0$ and $|X_3| = |+5.0| = 5.0$ (Both Positive): Tied for positions $3$ and $4$, so each receives mid-rank $R_2^+ = R_3^+ = \frac{3 + 4}{2} = 3.5$ (one tied group of size $t_1 = 2$)
- $|X_4| = |+8.0| = 8.0$ (Positive): Rank $R_4^+ = 5$
- $|X_6| = |+11.0| = 11.0$ (Positive): Rank $R_6^+ = 6$
- $|X_7| = |+14.0| = 14.0$ (Positive): Rank $R_7^+ = 7$
- $|X_8| = |+18.0| = 18.0$ (Positive): Rank $R_8^+ = 8$

Summing the ranks of the positive differences ($X_2, X_3, X_4, X_6, X_7, X_8$) and negative differences ($X_1, X_5$) gives:

$$T^+ = 3.5 + 3.5 + 5 + 6 + 7 + 8 = 33.0, \qquad T^- = 1 + 2 = 3.0, \qquad T^+ + T^- = 36 = \frac{8(9)}{2}$$

Under $H_0$, the null mean, unadjusted variance, and tie-corrected variance (with $t_1 = 2$, so $t_1(t_1^2 - 1) = 2(3) = 6$) are:

$$\mathbb{E}_{H_0}[T^+] = \frac{8(9)}{4} = 18.0, \qquad \text{Var}_{H_0}(T^+) = \frac{8(9)(17)}{24} = 51.0$$

$$\text{Var}_{H_0, \text{ties}}(T^+) = 51.0 - \frac{2(2^2 - 1)}{48} = 51.0 - \frac{6}{48} = 51.0 - 0.125 = 50.875$$

### Solution, step 2: Exact combinatorial p-value and tie-corrected normal approximation
Notice that the two tied observations $X_2 = +5.0$ and $X_3 = +5.0$ have the **same sign** (both positive), so their combined rank contribution is $3.5 + 3.5 = 3 + 4 = 7$ regardless of how the tie is broken! In the exact distribution of $T^+$ for $n = 8$ ($2^8 = 256$ equally likely sign configurations), the number of subsets of $\{1, 2, \dots, 8\}$ whose sum is $\le 3$ (so $T^- \le 3$, equivalent to $T^+ \ge 33$) is:
- $T^- = 0$: $\emptyset$ ($1$ configuration)
- $T^- = 1$: $\{1\}$ ($1$ configuration)
- $T^- = 2$: $\{2\}$ ($1$ configuration)
- $T^- = 3$: $\{3\}$ and $\{1, 2\}$ ($2$ configurations)

Thus there are exactly $1 + 1 + 1 + 2 = 5$ configurations with $T^+ \ge 33$, giving the **exact one-sided $p$-value**:

$$p_{\text{exact}} = \mathbb{P}_{H_0}(T^+ \ge 33) = \frac{5}{256} \approx 0.01953 < \alpha = 0.025$$

Using the continuity-corrected normal approximation with $\text{Var}_{H_0, \text{ties}}(T^+) = 50.875$:

$$Z = \frac{33.0 - 0.5 - 18.0}{\sqrt{50.875}} = \frac{14.5}{7.1327} \approx 2.0329 \implies p_{\text{normal}} = 1 - \Phi(2.0329) \approx 0.0210 < 0.025$$

Both the exact test and the normal approximation reject $H_0$ at $\alpha = 0.025$, confirming a statistically significant blood pressure reduction.

### Solution, step 3: Walsh averages and Hodges-Lehmann location estimator $\hat{\theta}_{\text{HL}}$
There are $M = \frac{8(9)}{2} = 36$ Walsh averages $A_{ij} = \frac{X_i + X_j}{2}$ ($1 \le i \le j \le 8$). Since $T^+ = 33$, exactly $3$ Walsh averages are negative—namely $\frac{-3 - 3}{2} = -3.0$, $\frac{-3 - 1}{2} = -2.0$, and $\frac{-1 - 1}{2} = -1.0$—and $33$ are positive. Sorting all $36$ Walsh averages in ascending order, the median is the average of the $18$-th and $19$-th ordered values $A_{(18)}$ and $A_{(19)}$:
Listing the smallest $19$ Walsh averages in ascending order:
1–3: $-3.0, \; -2.0, \; -1.0$
4–7: $+1.0, \; +1.0, \; +2.0, \; +2.0$ (from $(-3+5)/2$ twice and $(-1+5)/2$ twice)
8–10: $+2.5, \; +3.5, \; +4.0$ (from $(-3+8)/2$, $(-1+8)/2$, $(-3+11)/2$)
11–14: $+5.0, \; +5.0, \; +5.0, \; +5.0$ (from $(5+5)/2$ three times and $(-1+11)/2$)
15–19: $+5.5, \; +6.5, \; +6.5, \; \mathbf{+6.5}, \; \mathbf{+7.5}$ (where $+5.5 = (-3+14)/2$; the three $+6.5$ values come from $(-1+14)/2$ and $(5+8)/2$ twice; and $+7.5 = (-3+18)/2$).
Thus $A_{(18)} = 6.5$ and $A_{(19)} = 7.5$, giving the **Hodges-Lehmann estimator**:

$$\hat{\theta}_{\text{HL}} = \frac{A_{(18)} + A_{(19)}}{2} = \frac{6.5 + 7.5}{2} = 7.00\text{ mmHg}$$

For comparison, the sample mean is $\bar{X} = \frac{57.0}{8} = 7.125\text{ mmHg}$ and the sample median is $\tilde{X} = \frac{5.0 + 8.0}{2} = 6.50\text{ mmHg}$.

---

### Question 2: Two-Sample Wilcoxon Rank-Sum ($W$), Mann-Whitney ($U$), and Ansari-Bradley Scale ($AB$) Tests
An environmental hydrologist compares dissolved oxygen concentrations (in mg/L) between an upstream pristine reference reach ($X$, $n_1 = 5$) and a downstream industrial discharge reach ($Y$, $n_2 = 6$), obtaining the untied measurements:
- **Sample $X$ ($n_1 = 5$)**: $6.2, \; 7.1, \; 7.8, \; 8.4, \; 9.0$
- **Sample $Y$ ($n_2 = 6$)**: $4.5, \; 5.1, \; 5.9, \; 6.8, \; 7.4, \; 9.5$
1. Pool the $N = 11$ observations, assign combined ranks $1, \dots, 11$, and compute the Wilcoxon Rank-Sum statistics $W_X, W_Y$, the Mann-Whitney statistics $U_X, U_Y$, the stochastic dominance estimate $\hat{\theta} = \widehat{\mathbb{P}}(X > Y)$, and the Hodges-Lehmann shift estimate $\hat{\Delta}_{\text{HL}} = \text{Median}(X_i - Y_j)$.
2. Test $H_0 : F_X = F_Y$ against $H_1 : X \text{ is stochastically larger than } Y$ at $\alpha = 0.05$ using both the exact Mann-Whitney table and the normal approximation.
3. Assuming the two populations have comparable medians, compute the **Ansari-Bradley scale dispersion statistic $AB$** for Sample $X$, along with its exact null mean and variance for $N = 11$ (odd).

### Solution, step 1: Combined ranking, $W_X, U_X$, $\widehat{\mathbb{P}}(X > Y)$, and Hodges-Lehmann shift $\hat{\Delta}_{\text{HL}}$
Sorting all $N = n_1 + n_2 = 11$ observations in ascending order and identifying their sample membership ($X$ vs. $Y$):
1. $4.5$ ($Y$, Rank $1$)
2. $5.1$ ($Y$, Rank $2$)
3. $5.9$ ($Y$, Rank $3$)
4. $6.2$ ($X$, Rank $4$)
5. $6.8$ ($Y$, Rank $5$)
6. $7.1$ ($X$, Rank $6$)
7. $7.4$ ($Y$, Rank $7$)
8. $7.8$ ($X$, Rank $8$)
9. $8.4$ ($X$, Rank $9$)
10. $9.0$ ($X$, Rank $10$)
11. $9.5$ ($Y$, Rank $11$)

Summing the combined ranks of Sample $X$ ($4, 6, 8, 9, 10$) and Sample $Y$ ($1, 2, 3, 5, 7, 11$):

$$W_X = 4 + 6 + 8 + 9 + 10 = 37, \qquad W_Y = 1 + 2 + 3 + 5 + 7 + 11 = 29, \qquad W_X + W_Y = 66 = \frac{11(12)}{2}$$

Using the identity $U_X = W_X - \frac{n_1(n_1 + 1)}{2}$ with $\frac{5(6)}{2} = 15$:

$$U_X = 37 - 15 = 22, \qquad U_Y = n_1 n_2 - U_X = 30 - 22 = 8$$

Thus, out of the $n_1 n_2 = 30$ cross-sample pairs $(X_i, Y_j)$, $X_i > Y_j$ in $22$ pairs, giving the nonparametric AUC/stochastic dominance estimate:

$$\hat{\theta} = \widehat{\mathbb{P}}(X > Y) = \frac{U_X}{n_1 n_2} = \frac{22}{30} \approx 0.7333$$

Computing all $30$ pairwise differences $X_i - Y_j$ and sorting them, the $15$-th and $16$-th ordered differences are $+1.2$ ($7.1 - 5.9$) and $+1.3$ ($6.2 - 4.9$ or $8.4 - 7.1 \to$ specifically $6.2 - 5.1 = 1.1$, $7.1 - 5.9 = 1.2$, $8.4 - 6.8 = 1.6$, $9.0 - 7.4 = 1.6$, $7.8 - 6.8 = 1.0$, $6.2 - 4.5 = 1.7$, $7.8 - 5.9 = 1.9$, etc.: sorting all $30$ differences $X_i - Y_j$ yields the $15$-th and $16$-th values as $1.1$ and $1.2$), so $\hat{\Delta}_{\text{HL}} = \frac{1.1 + 1.2}{2} = +1.15\text{ mg/L}$.

### Solution, step 2: Null moments and hypothesis test for location shift
Under $H_0 : F_X = F_Y$, with $n_1 = 5$ and $n_2 = 6$:

$$\mathbb{E}_{H_0}[U_X] = \frac{5(6)}{2} = 15.0, \qquad \text{Var}_{H_0}(U_X) = \text{Var}_{H_0}(W_X) = \frac{5(6)(5 + 6 + 1)}{12} = \frac{360}{12} = 30.0$$

The continuity-corrected normal test statistic is:

$$Z = \frac{U_X - 0.5 - 15.0}{\sqrt{30.0}} = \frac{6.5}{5.4772} \approx 1.1867 \implies p_{\text{one-sided}} = 1 - \Phi(1.1867) \approx 0.1177$$

(The exact combinatorial probability $\mathbb{P}_{H_0}(U_X \ge 22)$ out of $\binom{11}{5} = 462$ ways is $58 / 462 \approx 0.1255 > 0.05$). Hence at $\alpha = 0.05$, the difference does not reach statistical significance with these small sample sizes.

### Solution, step 3: Ansari-Bradley scale dispersion test ($AB$)
For $N = 11$, the symmetric Ansari-Bradley folding scores $a_{11}(k) = \min(k, 12 - k)$ across ranks $k = 1, \dots, 11$ are:

$$(1, \; 2, \; 3, \; 4, \; 5, \; 6, \; 5, \; 4, \; 3, \; 2, \; 1)$$

Since Sample $X$ occupies combined ranks $k \in \{4, 6, 8, 9, 10\}$, its Ansari-Bradley scores are $a_{11}(4) = 4$, $a_{11}(6) = 6$, $a_{11}(8) = 4$, $a_{11}(9) = 3$, and $a_{11}(10) = 2$:

$$AB_X = 4 + 6 + 4 + 3 + 2 = 19$$

Using the exact odd-$N$ Ansari-Bradley formulas with $n_1 = 5, n_2 = 6, N = 11$:

$$\mathbb{E}_{H_0}[AB_X] = \frac{n_1(N + 1)^2}{4 N} = \frac{5(144)}{44} = \frac{180}{11} \approx 16.3636$$

$$\text{Var}_{H_0}(AB_X) = \frac{n_1 n_2 (N + 1)(N^2 + 3)}{48 N^2} = \frac{5(6)(12)(124)}{48(121)} = \frac{44,640}{5,808} \approx 7.68595 \implies \text{SD}_{H_0}(AB_X) \approx 2.772$$

Notice that $AB_X = 19 > \mathbb{E}_{H_0}[AB_X] = 16.36$, indicating that Sample $X$ is clustered more tightly in the interior ranks (smaller dispersion) while Sample $Y$ occupies both extreme tails (ranks $1, 2, 3$ and $11$).

---

### Question 3: Pitman Asymptotic Relative Efficiency of Sign, Wilcoxon, and Student's $t$-Tests under Heavy-Tailed Student-$t_\nu$ Errors
Suppose observations follow the location model $X_i = \theta + \varepsilon_i$, where the error $\varepsilon_i$ follows a Student-$t$ distribution with $\nu > 2$ degrees of freedom and density:

$$f_\nu(x) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \, \Gamma\left(\frac{\nu}{2}\right)} \left( 1 + \frac{x^2}{\nu} \right)^{-\frac{\nu + 1}{2}}, \quad -\infty < x < \infty$$

1. Using the known variance $\sigma_\nu^2 = \text{Var}(\varepsilon_i) = \frac{\nu}{\nu - 2}$ (for $\nu > 2$) and evaluating the quadratic density integral $\int_{-\infty}^\infty f_\nu^2(x) \, dx$, derive the closed-form formulas for $\text{ARE}(\text{Sign}, t; t_\nu)$ and $\text{ARE}(\text{Wilcoxon}, t; t_\nu)$ as functions of $\nu$.
2. Evaluate $\text{ARE}(\text{Sign}, t; t_\nu)$ and $\text{ARE}(\text{Wilcoxon}, t; t_\nu)$ numerically for $\nu = 3$, $\nu = 5$, and in the Gaussian limit $\nu \to \infty$.
3. Explain the physical and statistical behavior of both AREs as $\nu \to 2^+$ (where variance diverges) and at $\nu = 1$ (the Cauchy distribution).

### Solution, step 1: Derivation of $\int_{-\infty}^\infty f_\nu^2(x) \, dx$ and closed-form ARE formulas
First, let us evaluate $f_\nu(0)$ and the integral $\int_{-\infty}^\infty f_\nu^2(x) \, dx$. At $x = 0$, the density is simply:

$$f_\nu(0) = \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\sqrt{\nu \pi} \, \Gamma\left(\frac{\nu}{2}\right)}$$

Since the Pitman ARE of the Sign Test relative to Student's $t$-test is $\text{ARE}(\text{Sign}, t; f_\nu) = 4 \sigma_\nu^2 [f_\nu(0)]^2$ with $\sigma_\nu^2 = \frac{\nu}{\nu - 2}$, we immediately obtain:

$$\text{ARE}(\text{Sign}, t; t_\nu) = 4 \left( \frac{\nu}{\nu - 2} \right) \frac{\Gamma^2\left(\frac{\nu + 1}{2}\right)}{\nu \pi \, \Gamma^2\left(\frac{\nu}{2}\right)} = \frac{4}{\pi(\nu - 2)} \left[ \frac{\Gamma\left(\frac{\nu + 1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)} \right]^2$$

Next, to compute $\int_{-\infty}^\infty f_\nu^2(x) \, dx$, we square $f_\nu(x)$ and substitute $1 + \frac{x^2}{\nu} = \frac{1}{u}$ (Beta integral identity $\int_{-\infty}^\infty \left(1 + \frac{x^2}{\nu}\right)^{-(\nu + 1)} dx = \sqrt{\nu \pi} \frac{\Gamma(\nu + 1/2)}{\Gamma(\nu + 1)}$):

$$\int_{-\infty}^\infty f_\nu^2(x) \, dx = \frac{\Gamma^2\left(\frac{\nu + 1}{2}\right)}{\nu \pi \, \Gamma^2\left(\frac{\nu}{2}\right)} \sqrt{\nu \pi} \frac{\Gamma\left(\nu + \frac{1}{2}\right)}{\Gamma(\nu + 1)} = \frac{\Gamma^2\left(\frac{\nu + 1}{2}\right) \Gamma\left(\nu + \frac{1}{2}\right)}{\sqrt{\nu \pi} \, \Gamma^2\left(\frac{\nu}{2}\right) \Gamma(\nu + 1)}$$

Substituting this into $\text{ARE}(\text{Wilcoxon}, t; t_\nu) = 12 \sigma_\nu^2 \left(\int_{-\infty}^\infty f_\nu^2(x) \, dx\right)^2$ with $\sigma_\nu^2 = \frac{\nu}{\nu - 2}$ yields the exact analytical formula:

$$\text{ARE}(\text{Wilcoxon}, t; t_\nu) = \frac{12}{\pi(\nu - 2)} \left[ \frac{\Gamma^2\left(\frac{\nu + 1}{2}\right) \Gamma\left(\nu + \frac{1}{2}\right)}{\Gamma^2\left(\frac{\nu}{2}\right) \Gamma(\nu + 1)} \right]^2$$

### Solution, step 2: Numerical evaluation for $\nu = 3$, $\nu = 5$, and $\nu \to \infty$
- **For $\nu = 3$**: Here $\Gamma(2) = 1$, $\Gamma(3/2) = \frac{\sqrt{\pi}}{2}$, $\Gamma(7/2) = \frac{15\sqrt{\pi}}{8}$, and $\Gamma(4) = 6$, with $\nu - 2 = 1$:
  $$\text{ARE}(\text{Sign}, t; t_3) = \frac{4}{\pi(1)} \left(\frac{1}{\sqrt{\pi}/2}\right)^2 = \frac{16}{\pi^2} \approx 1.6211 \quad (162.1\%)$$
  $$\text{ARE}(\text{Wilcoxon}, t; t_3) = \frac{12}{\pi(1)} \left[ \frac{1^2 \cdot (15\sqrt{\pi}/8)}{(\pi/4) \cdot 6} \right]^2 = \frac{12}{\pi} \left( \frac{5}{4\sqrt{\pi}} \right)^2 = \frac{75}{4\pi^2} \approx 1.8998 \quad (190.0\%)$$
- **For $\nu = 5$**: Here $\Gamma(3) = 2$, $\Gamma(5/2) = \frac{3\sqrt{\pi}}{4}$, $\Gamma(11/2) = \frac{945\sqrt{\pi}}{32}$, and $\Gamma(6) = 120$, with $\nu - 2 = 3$:
  $$\text{ARE}(\text{Sign}, t; t_5) = \frac{4}{3\pi} \left(\frac{2}{3\sqrt{\pi}/4}\right)^2 = \frac{256}{27\pi^2} \approx 0.9607 \quad (96.1\%)$$
  $$\text{ARE}(\text{Wilcoxon}, t; t_5) = \frac{12}{3\pi} \left[ \frac{4 \cdot (945\sqrt{\pi}/32)}{(9\pi/16) \cdot 120} \right]^2 = \frac{4}{\pi} \left( \frac{7}{4\sqrt{\pi}} \right)^2 = \frac{49}{4\pi^2} \approx 1.2412 \quad (124.1\%)$$
- **As $\nu \to \infty$ (Gaussian limit)**: By Stirling's approximation, $\text{ARE}(\text{Sign}, t; t_\infty) \to \frac{2}{\pi} \approx 0.6366$ and $\text{ARE}(\text{Wilcoxon}, t; t_\infty) \to \frac{3}{\pi} \approx 0.9549$.

### Solution, step 3: Asymptotic divergence as $\nu \to 2^+$ and Cauchy behavior at $\nu = 1$
Notice that both ARE formulas contain the factor $\frac{1}{\nu - 2}$ coming from $\sigma_\nu^2 = \frac{\nu}{\nu - 2}$, while the density integrals $f_\nu(0)$ and $\int f_\nu^2(x) \, dx$ remain strictly positive and finite for all $\nu > 0$! Consequently, as $\nu \to 2^+$, $\sigma_\nu^2 \to +\infty$, causing **both $\text{ARE}(\text{Sign}, t; t_\nu) \to +\infty$ and $\text{ARE}(\text{Wilcoxon}, t; t_\nu) \to +\infty$**. At $\nu = 1$ (the Cauchy distribution), Student's $t$-test fails to converge to $\theta$ altogether, whereas between the two nonparametric tests, $\text{ARE}(\text{Sign}, \text{Wilcoxon}; \text{Cauchy}) = \frac{4[f_1(0)]^2}{12(\int f_1^2)^2} = \frac{4(1/\pi)^2}{12(1/(2\pi))^2} = \frac{4}{3} \approx 1.333$, showing that for extremely heavy Cauchy tails, the Sign Test even surpasses the Wilcoxon test by $33.3\%$!
