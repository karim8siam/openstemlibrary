# Unit 2: Simple Random Sampling and Finite Population Correction

## The Mechanics of Simple Random Selection: Without Replacement versus With Replacement

Simple random sampling constitutes the foundational baseline against which all sophisticated survey sampling designs are measured, evaluated, and benchmarked. Despite its conceptual simplicity, the mathematical theory governing simple random selection embodies the essential principles of design-based inference: fixed finite population values, random sample inclusion indicators, combinatorial sample spaces, and design-unbiased estimation. Understanding the precise mathematical distinctions between selection with replacement and selection without replacement is essential for mastering finite population inference.

Let $U = \{1, 2, \dots, N\}$ denote a fixed finite population of $N$ identifiable elements, each possessing a fixed scalar value $y_i$. In **Simple Random Sampling Without Replacement (SRSWOR)**, a sample of $n$ distinct elements ($n \le N$) is drawn in such a manner that every one of the $\binom{N}{n}$ possible distinct subsets of size $n$ has an identical probability of selection. The sample space $\mathcal{S}_{wor}$ consists of all subsets $s \subseteq U$ with cardinality $|s| = n$. The probability assigned to each sample $s \in \mathcal{S}_{wor}$ is strictly uniform:
$$p(s) = \frac{1}{\binom{N}{n}} = \frac{n! (N - n)!}{N!} \quad \forall s \in \mathcal{S}_{wor}$$
Because no unit can be selected more than once, the observed sample contains $n$ unique elements.

In contrast, in **Simple Random Sampling With Replacement (SRSWR)**, the sample is constructed through $n$ sequential and independent draws. On each individual draw, an element is selected uniformly from the entire population of $N$ units with probability $1/N$, measured, and then replaced into the population pool before the subsequent draw. The sample space $\mathcal{S}_{wr}$ consists of all ordered sequences $(i_1, i_2, \dots, i_n)$ where $i_k \in \{1, \dots, N\}$. The probability of selecting any specific sequence is:
$$p(i_1, \dots, i_n) = \frac{1}{N^n}$$
Under SRSWR, an individual element may appear multiple times in the sample. The number of distinct elements observed in an SRSWR sample is a random variable that is strictly less than or equal to $n$.

From an operational standpoint, SRSWOR is virtually always preferred over SRSWR in empirical research and official surveys. Selecting the same unit more than once provides redundant information: resurveying the same household or testing the same soil plot a second time adds no new information regarding the unobserved population, while consuming additional field budget and inflating the sampling variance. The mathematical consequence of discarding duplicates without replacement is the emergence of the **Finite Population Correction (FPC)** factor, which substantially enhances estimation precision whenever the sampling fraction $f = n/N$ is non-negligible.

## Inclusion Probabilities and Random Indicator Algebra

The mathematical analysis of probability sampling designs is vastly simplified and unified through the algebra of **sample inclusion indicators**. For each unit $i \in U$, define the random binary indicator variable:
$$I_i = \begin{cases} 1 & \text{if unit } i \in s \\ 0 & \text{if unit } i \notin s \end{cases}$$
The vector of indicators $\mathbf{I} = (I_1, I_2, \dots, I_N)^\top$ completely characterizes the realized sample. Any sample statistic can be expressed as a linear or nonlinear function of these random indicators.

### First-Order Inclusion Probabilities under SRSWOR
The **first-order inclusion probability** $\pi_i$ is the probability that unit $i$ is included in the sample $s$. Under SRSWOR, the total number of samples of size $n$ that contain a specific unit $i$ is equal to the number of ways to choose the remaining $n - 1$ sample units from the remaining $N - 1$ population units, which is $\binom{N - 1}{n - 1}$. Therefore:
$$\pi_i = P(I_i = 1) = E[I_i] = \frac{\binom{N - 1}{n - 1}}{\binom{N}{n}} = \frac{\frac{(N - 1)!}{(n - 1)! (N - n)!}}{\frac{N!}{n! (N - n)!}} = \frac{n}{N}$$
Every unit in the population has the exact same probability of being included in the sample:
$$\pi_i = \frac{n}{N} = f \quad \forall i \in U$$
where $f = n / N$ is the **sampling fraction**.

Because $I_i$ is a Bernoulli random variable with success parameter $\pi_i = f$, its design variance is:
$$V(I_i) = E[I_i^2] - (E[I_i])^2 = \pi_i - \pi_i^2 = \pi_i (1 - \pi_i) = \frac{n}{N} \left(1 - \frac{n}{N}\right) = f (1 - f)$$

### Second-Order Inclusion Probabilities under SRSWOR
The **second-order (or joint) inclusion probability** $\pi_{ij}$ is the probability that both unit $i$ and unit $j$ ($i \ne j$) are included in the sample. The number of samples of size $n$ that contain both fixed units $i$ and $j$ is the number of ways to select the remaining $n - 2$ elements from the remaining $N - 2$ population units, which is $\binom{N - 2}{n - 2}$. Therefore:
$$\pi_{ij} = P(I_i = 1 \text{ and } I_j = 1) = E[I_i I_j] = \frac{\binom{N - 2}{n - 2}}{\binom{N}{n}} = \frac{\frac{(N - 2)!}{(n - 2)! (N - n)!}}{\frac{N!}{n! (N - n)!}} = \frac{n(n - 1)}{N(N - 1)}$$
for all pairs $i \ne j \in U$.

Notice that:
$$\pi_{ij} = \frac{n(n - 1)}{N(N - 1)} \ne \pi_i \pi_j = \left(\frac{n}{N}\right)^2$$
The selection of units under SRSWOR is statistically dependent. Specifically, because sampling is conducted without replacement, selecting unit $i$ slightly diminishes the pool of available units, making the inclusion of unit $j$ marginally less likely than it would be under independent selection:
$$\pi_{ij} - \pi_i \pi_j = \frac{n(n - 1)}{N(N - 1)} - \frac{n^2}{N^2} = \frac{n [n(N) - N - n(N - 1)]}{N^2 (N - 1)} = \frac{n [n N - N - n N + n]}{N^2 (N - 1)} = -\frac{n (N - n)}{N^2 (N - 1)}$$
Thus, the design covariance between the inclusion indicators of two distinct units $i \ne j$ is strictly negative:
$$\text{Cov}(I_i, I_j) = E[I_i I_j] - E[I_i] E[I_j] = \pi_{ij} - \pi_i \pi_j = -\frac{f(1 - f)}{N - 1}$$
This negative covariance reflects the fundamental conservation constraint of fixed-size sampling: $\sum_{i=1}^N I_i = n$. If one unit is selected, the remaining units must compete for the remaining $n - 1$ slots, inducing an intrinsic negative correlation among sample indicators.

## Estimation of Population Means and Totals: Horvitz–Thompson Equivalence

The primary descriptive estimands in simple random sampling are the **finite population mean**:
$$\bar{Y} = \frac{1}{N} \sum_{i=1}^N y_i$$
and the **finite population total**:
$$Y = \sum_{i=1}^N y_i = N \bar{Y}$$

The standard sample mean computed from an SRSWOR sample $s$ of size $n$ is:
$$\bar{y} = \frac{1}{n} \sum_{i \in s} y_i$$
Using random inclusion indicators, $\bar{y}$ can be expressed as a linear combination of all $N$ population elements:
$$\bar{y} = \frac{1}{n} \sum_{i=1}^N I_i y_i$$
Notice that the Horvitz–Thompson estimator of the population total $Y$ under SRSWOR is:
$$\hat{Y}_{HT} = \sum_{i \in s} \frac{y_i}{\pi_i} = \sum_{i=1}^N I_i \frac{y_i}{n/N} = \frac{N}{n} \sum_{i=1}^N I_i y_i = N \bar{y}$$
Dividing $\hat{Y}_{HT}$ by the known population size $N$ yields the sample mean:
$$\hat{\bar{Y}}_{HT} = \frac{\hat{Y}_{HT}}{N} = \bar{y}$$
Thus, in simple random sampling, the ordinary arithmetic sample mean $\bar{y}$ is identical to the Horvitz–Thompson estimator of the population mean.

### Design Unbiasedness of the Sample Mean
The mathematical expectation of $\bar{y}$ under the SRSWOR design distribution is evaluated directly using the linearity of expectation and the first-order inclusion probability $\pi_i = n/N$:
$$E[\bar{y}] = E\left[ \frac{1}{n} \sum_{i=1}^N I_i y_i \right] = \frac{1}{n} \sum_{i=1}^N E[I_i] y_i = \frac{1}{n} \sum_{i=1}^N \left(\frac{n}{N}\right) y_i = \frac{1}{N} \sum_{i=1}^N y_i = \bar{Y}$$
This proves that the sample mean $\bar{y}$ is strictly **design-unbiased** for the population mean $\bar{Y}$.

Similarly, the total estimator $\hat{Y} = N \bar{y}$ is strictly design-unbiased for the true population total $Y$:
$$E[\hat{Y}] = E[N \bar{y}] = N E[\bar{y}] = N \bar{Y} = Y$$
Remarkably, this unbiasedness property holds unconditionally, regardless of whether the population values $y_i$ are symmetric, highly skewed, bounded, or multimodal. It requires no distributional assumptions whatsoever.

## Rigorous Derivation of Sampling Variance and the Finite Population Correction

We now derive the exact variance of the sample mean $\bar{y}$ under SRSWOR from first principles.

Recall the definition of the **finite population variance** $S^2$, defined with divisor $N - 1$:
$$S^2 = \frac{1}{N - 1} \sum_{i=1}^N (y_i - \bar{Y})^2$$
and the **population element variance** $\sigma^2$, defined with divisor $N$:
$$\sigma^2 = \frac{1}{N} \sum_{i=1}^N (y_i - \bar{Y})^2 = \frac{N - 1}{N} S^2$$

Using indicator algebra, the variance of $\bar{y} = \frac{1}{n} \sum_{i=1}^N I_i y_i$ is given by:
$$V(\bar{y}) = V\left( \frac{1}{n} \sum_{i=1}^N I_i y_i \right) = \frac{1}{n^2} V\left( \sum_{i=1}^N I_i y_i \right)$$
Expanding the variance of a linear combination of random variables into individual variances and pairwise covariances:
$$V\left( \sum_{i=1}^N I_i y_i \right) = \sum_{i=1}^N y_i^2 V(I_i) + \sum_{i=1}^N \sum_{j \ne i}^N y_i y_j \text{Cov}(I_i, I_j)$$
Substituting $V(I_i) = f(1 - f)$ and $\text{Cov}(I_i, I_j) = -\frac{f(1 - f)}{N - 1}$:
$$V\left( \sum_{i=1}^N I_i y_i \right) = f(1 - f) \sum_{i=1}^N y_i^2 - \frac{f(1 - f)}{N - 1} \sum_{i=1}^N \sum_{j \ne i}^N y_i y_j$$
Factor out $\frac{f(1 - f)}{N - 1}$:
$$V\left( \sum_{i=1}^N I_i y_i \right) = \frac{f(1 - f)}{N - 1} \left[ (N - 1) \sum_{i=1}^N y_i^2 - \sum_{i=1}^N \sum_{j \ne i}^N y_i y_j \right]$$
Now consider the algebraic identity connecting pairwise squared differences to the population variance:
$$\sum_{i=1}^N \sum_{j=1}^N (y_i - y_j)^2 = \sum_{i=1}^N \sum_{j=1}^N (y_i^2 - 2 y_i y_j + y_j^2) = N \sum_{i=1}^N y_i^2 - 2 \sum_{i=1}^N \sum_{j=1}^N y_i y_j + N \sum_{j=1}^N y_j^2$$
$$= 2 N \sum_{i=1}^N y_i^2 - 2 \left( \sum_{i=1}^N y_i \right)^2 = 2 N \left[ \sum_{i=1}^N y_i^2 - N \bar{Y}^2 \right] = 2 N (N - 1) S^2$$
Dividing by 2 gives:
$$\sum_{i < j} (y_i - y_j)^2 = N (N - 1) S^2$$
Furthermore, expanding the term in the brackets:
$$(N - 1) \sum_{i=1}^N y_i^2 - \sum_{i=1}^N \sum_{j \ne i}^N y_i y_j = N \sum_{i=1}^N y_i^2 - \left( \sum_{i=1}^N y_i^2 + \sum_{i=1}^N \sum_{j \ne i}^N y_i y_j \right) = N \sum_{i=1}^N y_i^2 - \left( \sum_{i=1}^N y_i \right)^2$$
$$= N \left[ \sum_{i=1}^N y_i^2 - N \bar{Y}^2 \right] = N (N - 1) S^2$$
Substituting this exact result back into the variance expression:
$$V\left( \sum_{i=1}^N I_i y_i \right) = \frac{f(1 - f)}{N - 1} \cdot [N (N - 1) S^2] = N f (1 - f) S^2$$
Recalling that $f = n / N$, we have $N f = n$. Therefore:
$$V\left( \sum_{i=1}^N I_i y_i \right) = n (1 - f) S^2$$
Finally, multiplying by the pre-factor $1 / n^2$:
$$V(\bar{y}) = \frac{1}{n^2} [n (1 - f) S^2] = \frac{1 - f}{n} S^2$$
This completes the rigorous derivation of the classical SRSWOR variance formula:
$$V(\bar{y}) = \frac{1 - f}{n} S^2 = \left( \frac{N - n}{N} \right) \frac{S^2}{n}$$

The term $(1 - f) = \frac{N - n}{N}$ is the **Finite Population Correction (FPC)**. 
- When the population size $N$ is vast relative to the sample size $n$, the sampling fraction $f = n/N \to 0$, and the FPC factor approaches $1$. In this asymptotic limit, the variance reduces to the familiar infinite-population formula $S^2 / n$.
- When the entire population is surveyed ($n = N$), the sampling fraction becomes $f = 1$, yielding $1 - f = 0$ and $V(\bar{y}) = 0$. A complete census carries zero sampling variance, as required by logical consistency.

For the estimated population total $\hat{Y} = N \bar{y}$, the variance is scaled by $N^2$:
$$V(\hat{Y}) = N^2 V(\bar{y}) = N^2 \left( \frac{1 - f}{n} \right) S^2 = \frac{N(N - n)}{n} S^2$$

## Unbiased Estimation of the Sampling Variance: The Sample Variance s²

In empirical surveys, the true finite population variance $S^2$ is unknown, because the population elements are not exhaustively observed. To compute confidence intervals and perform hypothesis tests, the statistician must estimate $S^2$ directly from the sample data.

The standard sample variance computed from sample $s$ is defined with divisor $n - 1$:
$$s^2 = \frac{1}{n - 1} \sum_{i \in s} (y_i - \bar{y})^2$$

### Proof of Unbiasedness: E[s²] = S²
To prove that $s^2$ is an unbiased estimator of $S^2$, we utilize the identity relating sample variance to pairwise differences among sampled elements:
$$\sum_{i \in s} (y_i - \bar{y})^2 = \frac{1}{2n} \sum_{i \in s} \sum_{j \in s} (y_i - y_j)^2 = \sum_{i \in s} \sum_{j \in s, j > i} (y_i - y_j)^2$$
Using inclusion indicators, this sum can be written across all pairs in the population:
$$\sum_{i \in s} (y_i - \bar{y})^2 = \sum_{i=1}^N \sum_{j > i}^N I_i I_j (y_i - y_j)^2$$
Taking the design expectation:
$$E\left[ \sum_{i \in s} (y_i - \bar{y})^2 \right] = \sum_{i=1}^N \sum_{j > i}^N E[I_i I_j] (y_i - y_j)^2 = \sum_{i=1}^N \sum_{j > i}^N \pi_{ij} (y_i - y_j)^2$$
Under SRSWOR, $\pi_{ij} = \frac{n(n - 1)}{N(N - 1)}$ for all pairs $j > i$. Factor this constant out of the summation:
$$E\left[ \sum_{i \in s} (y_i - \bar{y})^2 \right] = \frac{n(n - 1)}{N(N - 1)} \sum_{i=1}^N \sum_{j > i}^N (y_i - y_j)^2$$
Recall the population identity derived earlier: $\sum_{i < j} (y_i - y_j)^2 = N(N - 1) S^2 / 2 \cdot 2 = N(N - 1) S^2 / 2$? Let us verify:
$$\sum_{i=1}^N \sum_{j=1}^N (y_i - y_j)^2 = 2 \sum_{i < j} (y_i - y_j)^2 = 2 N (N - 1) S^2 \implies \sum_{i < j} (y_i - y_j)^2 = N(N - 1) S^2$$
In parallel, the sample sum of squared deviations can be written identically as:
$$\sum_{i \in s} (y_i - \bar{y})^2 = \frac{1}{n} \sum_{i < j \in s} (y_i - y_j)^2 = \frac{1}{n} \sum_{i=1}^N \sum_{j > i}^N I_i I_j (y_i - y_j)^2$$
Taking the mathematical expectation across the design distribution:
$$E\left[ \sum_{i \in s} (y_i - \bar{y})^2 \right] = \frac{1}{n} \sum_{i=1}^N \sum_{j > i}^N E[I_i I_j] (y_i - y_j)^2 = \frac{1}{n} \left( \frac{n(n - 1)}{N(N - 1)} \right) \sum_{i < j} (y_i - y_j)^2$$
Substituting $\sum_{i < j} (y_i - y_j)^2 = N(N - 1) S^2$:
$$E\left[ \sum_{i \in s} (y_i - \bar{y})^2 \right] = \frac{n - 1}{N(N - 1)} \cdot [N(N - 1) S^2] = (n - 1) S^2$$
Dividing both sides by $n - 1$:
$$E[s^2] = E\left[ \frac{1}{n - 1} \sum_{i \in s} (y_i - \bar{y})^2 \right] = \frac{1}{n - 1} (n - 1) S^2 = S^2$$
This establishes with rigorous mathematical certainty that the sample variance $s^2$ is strictly **design-unbiased** for the finite population variance $S^2$.

### The Sample Variance Estimator
Consequently, an unbiased estimator of the variance of the sample mean $V(\bar{y})$ is:
$$v(\bar{y}) = \frac{1 - f}{n} s^2 = \left( \frac{N - n}{N} \right) \frac{s^2}{n}$$
and an unbiased estimator of $V(\hat{Y})$ is:
$$v(\hat{Y}) = N^2 v(\bar{y}) = N^2 \left( \frac{1 - f}{n} \right) s^2 = \frac{N(N - n)}{n} s^2$$
The estimated standard error is simply $\text{se}(\bar{y}) = \sqrt{v(\bar{y})}$.

## Asymptotic Normality and the Finite Population Central Limit Theorem

While the design unbiasedness of $\bar{y}$ and $s^2$ holds exactly for any finite sample size $n \ge 2$, constructing valid inferential confidence intervals and conducting hypothesis tests requires knowledge of the asymptotic sampling distribution of the standardized error:
$$Z_n = \frac{\bar{y} - \bar{Y}}{\sqrt{V(\bar{y})}} = \frac{\bar{y} - \bar{Y}}{\sqrt{\frac{1 - f}{n}} S}$$

In classical mathematical statistics, the Lindeberg–Lévy Central Limit Theorem applies to independent and identically distributed random variables. Under SRSWOR, however, the observations are statistically dependent because sampling is conducted without replacement, and the population itself is finite. Formal asymptotic theory for finite populations requires formulating a sequence of nested finite populations $\{U_\nu\}_{\nu=1}^\infty$ with increasing sizes $N_\nu \to \infty$ and corresponding sample sizes $n_\nu \to \infty$.

The definitive mathematical conditions for asymptotic normality in finite population sampling were established by Jaroslav Hájek in his seminal 1960 paper. Hájek proved that $Z_n \xrightarrow{d} \mathcal{N}(0, 1)$ as $n_\nu \to \infty$ and $N_\nu - n_\nu \to \infty$ if and only if the population sequence satisfies the **Hájek Lindeberg-type Condition**:
$$\lim_{\nu \to \infty} \frac{\sum_{i \in U_{\nu, \tau}} (y_{\nu i} - \bar{Y}_\nu)^2}{(N_\nu - 1) S_\nu^2} = 0 \quad \forall \tau > 0$$
where the summation index set $U_{\nu, \tau}$ consists of all population units whose standardized deviations exceed the threshold:
$$U_{\nu, \tau} = \left\{ i \in U_\nu : \frac{|y_{\nu i} - \bar{Y}_\nu|}{\sqrt{1 - f_\nu} \sqrt{n_\nu} S_\nu} > \tau \right\}$$

### Theoretical Interpretation of the Hájek Condition
The Hájek condition establishes that asymptotic normality holds provided no single individual population element or microscopic cluster of extreme outliers dominates the total finite population variance. Specifically:
1. **Vanishing Extremes**: The maximum individual contribution to the total variance, $\max_{i \in U} (y_i - \bar{Y})^2 / \sum_{j=1}^N (y_j - \bar{Y})^2$, must vanish asymptotically as $N \to \infty$.
2. **Behavior of the Sampling Fraction**: The theorem requires that $N_\nu - n_\nu \to \infty$. If the sample size approaches the population size so rapidly that $N_\nu - n_\nu = O(1)$, the remaining unobserved population is finite, and the sampling distribution degenerates into a discrete distribution rather than a continuous Gaussian bell curve.
3. **Studentization Robustness**: In empirical practice, the true standard error is replaced by the sample-based estimate $\text{se}(\bar{y}) = \sqrt{\frac{1 - f}{n}} s$. By Slutsky’s theorem, because $s^2 / S^2 \xrightarrow{p} 1$ under mild fourth-moment regularity conditions ($\frac{1}{N}\sum (y_i - \bar{Y})^4 / S^4 < \infty$), the Studentized statistic:
   $$T_n = \frac{\bar{y} - \bar{Y}}{\sqrt{\frac{1 - f}{n}} s} \xrightarrow{d} \mathcal{N}(0, 1)$$
This justifies the construction of standard $100(1 - \alpha)\%$ Wald asymptotic confidence intervals:
$$\text{CI}_{1-\alpha}(\bar{Y}) = \left[ \bar{y} - z_{\alpha/2} \sqrt{\frac{1 - f}{n}} s, \; \bar{y} + z_{\alpha/2} \sqrt{\frac{1 - f}{n}} s \right]$$

When the underlying population exhibits severe skewness (such as enterprise revenue or personal wealth distributions) and the sample size is moderate, the coverage probability of the Wald interval can fall noticeably below the nominal level $1 - \alpha$. In such environments, survey statisticians construct log-transformed confidence intervals or deploy finite population empirical likelihood intervals to restore nominal coverage.

## Systematic Random Sampling: The Operational Bridge to Cluster Sampling

In practical fieldwork, executing a pure simple random sample without replacement can be logistically challenging if the sampling frame consists of an unindexed physical card catalog, a sequential paper ledger, or a continuous queue of incoming entities. Under such conditions, survey practitioners frequently implement **1-in-$k$ Systematic Random Sampling**.

### The Selection Protocol
Let a population of $N$ units be indexed sequentially from $1$ to $N$. Suppose we wish to draw a sample of size $n$, where $k = N / n$ is an integer representing the **sampling interval** (skip interval). The selection protocol proceeds in two transparent steps:
1. **Random Start Selection**: Generate a single uniform random integer $r$ from the set $\{1, 2, \dots, k\}$:
   $$P(R = r) = \frac{1}{k} \quad \forall r \in \{1, 2, \dots, k\}$$
2. **Deterministic Sequence**: Select every $k$-th element thereafter, yielding the sample of $n$ units:
   $$s_r = \{r, \; r + k, \; r + 2k, \; \dots, \; r + (n - 1)k\}$$

Notice that:
- Every individual unit $i \in U$ has an identical first-order inclusion probability $\pi_i = 1/k = n/N$, exactly matching SRSWOR.
- However, unlike SRSWOR—which admits $\binom{N}{n}$ possible samples—systematic sampling admits exactly **$k$ possible samples**! Once the random start $r$ is drawn, the entire sample is deterministically fixed.

### Systematic Sampling as Single-Stage Cluster Sampling
Mathematically, systematic sampling is completely equivalent to selecting a single cluster of size $n$ with uniform probability from a population partitioned into $k$ distinct systematic clusters.

Let $y_{rj}$ denote the value of the $j$-th unit in the $r$-th systematic sample ($r = 1, \dots, k; j = 1, \dots, n$). The systematic sample mean is:
$$\bar{y}_{sys} = \frac{1}{n} \sum_{j=1}^n y_{rj} = \bar{y}_r$$
The expectation over the $k$ equally likely starts is:
$$E[\bar{y}_{sys}] = \frac{1}{k} \sum_{r=1}^k \bar{y}_r = \frac{1}{k} \sum_{r=1}^k \left( \frac{1}{n} \sum_{j=1}^n y_{rj} \right) = \frac{1}{N} \sum_{i=1}^N y_i = \bar{Y}$$
Thus, $\bar{y}_{sys}$ is strictly **design-unbiased** for the population mean $\bar{Y}$.

### Exact Variance and the Intraclass Correlation Coefficient
The exact variance of $\bar{y}_{sys}$ across the $k$ possible samples is:
$$V(\bar{y}_{sys}) = \frac{1}{k} \sum_{r=1}^k (\bar{y}_r - \bar{Y})^2$$
By expressing the variance in terms of the **intraclass correlation coefficient** $\rho_{sys}$ among units belonging to the same systematic sample:
$$\rho_{sys} = \frac{\sum_{r=1}^k \sum_{j=1}^n \sum_{j' \ne j}^n (y_{rj} - \bar{Y})(y_{rj'} - \bar{Y})}{(n - 1) (N - 1) S^2}$$
William Cochran derived the foundational identity connecting systematic sampling variance to the finite population variance:
$$V(\bar{y}_{sys}) = \frac{N - 1}{N} \frac{S^2}{n} [1 + (n - 1) \rho_{sys}]$$
Recall that the variance under SRSWOR can be written as:
$$V_{wor}(\bar{y}) = \frac{N - n}{N} \frac{S^2}{n} = \frac{N - 1}{N} \frac{S^2}{n} \left( 1 - \frac{n - 1}{N - 1} \right)$$
Comparing $V(\bar{y}_{sys})$ and $V_{wor}(\bar{y})$ reveals the exact efficiency condition:
$$V(\bar{y}_{sys}) < V_{wor}(\bar{y}) \iff \rho_{sys} < -\frac{1}{N - 1}$$

### Ordering Effects on Systematic Efficiency
The efficiency of systematic sampling depends entirely on the ordering of elements on the frame:
1. **Random Order**: If the frame is ordered randomly prior to selection, $\rho_{sys} \approx -1/(N-1)$, and systematic sampling is asymptotically equivalent to SRSWOR.
2. **Linear Trend**: If the frame exhibits a monotonic trend (e.g., plots ordered by soil fertility or firms ordered by revenue), systematic sampling forces the sample to spread evenly across the entire range of values. In this case, $\rho_{sys} < 0$, and systematic sampling is vastly **more efficient** than SRSWOR!
3. **Periodic Fluctuations (The Deadly Pathology)**: If the population possesses a hidden cyclical or periodic wave with period matching the sampling interval $k$ (e.g., surveying store sales every 7th day, repeatedly sampling only Mondays), all units in the sample will occupy the same phase of the cycle. In this catastrophe, $\rho_{sys} \to +1$, and $V(\bar{y}_{sys})$ is inflated by up to a factor of $n$, destroying estimation accuracy.

### The Variance Estimation Dilemma
A profound theoretical limitation of systematic sampling is that because only **one cluster** (the single random start $r$) is selected, it is mathematically impossible to obtain an unbiased estimator of $V(\bar{y}_{sys})$ from the sample data alone! The sample space contains only one degree of freedom across clusters. 

To overcome this dilemma, methodologists deploy:
- **Multiple Random Starts**: Instead of a 1-in-$k$ sample of size $n$, draw $m$ independent systematic samples with intervals $m k$ and sample sizes $n / m$. An unbiased variance estimator is then computed directly across the $m$ independent replicates.
- **Successive Difference Estimator**: When a single start is fielded, methodologists estimate variance using squared differences between adjacent sampled units:
  $$v_{diff}(\bar{y}_{sys}) = \frac{1 - f}{n} \left[ \frac{1}{2(n - 1)} \sum_{j=1}^{n-1} (y_{j+1} - y_j)^2 \right]$$
  This difference estimator filters out linear trends and provides a highly reliable conservative approximation.

### Circular Systematic Sampling and Non-Integer Intervals
A practical complication arises when the population size $N$ is not an exact integer multiple of the desired sample size $n$, meaning $k = N / n$ is fractional. If a researcher rounds $k$ down to $\lfloor N/n \rfloor$, the final sample size may exceed $n$, or the final elements of the frame may have a zero probability of selection. Conversely, rounding up to $\lceil N/n \rceil$ can result in an realized sample size strictly smaller than $n$.

To preserve an exact fixed sample size $n$ and strictly uniform first-order inclusion probabilities $\pi_i = n / N$ across all $N$ units, statisticians implement **Circular Systematic Sampling (CSS)**, developed by D. B. Lahiri (1951) and M. N. Murthy (1967):
1. **Selection Protocol**: Conceptualize the population $U = \{1, 2, \dots, N\}$ as arranged in a continuous closed ring or circle, where element $N$ is immediately followed by element $1$.
2. **Integer Interval**: Choose the integer sampling interval $k = \text{round}(N / n)$ as the integer closest to $N / n$.
3. **Uniform Random Start**: Select a single random start $r$ with uniform probability from the entire set of population units:
   $$P(R = r) = \frac{1}{N} \quad \forall r \in \{1, 2, \dots, N\}$$
4. **Circular Sequence**: Select the $n$ elements whose indices are given by:
   $$s_r = \{i_j : i_j = [r + (j - 1)k] \pmod N, \quad j = 1, 2, \dots, n\}$$
   where the modulo operation is defined on the positive residue system $\{1, 2, \dots, N\}$ (treating residue $0$ as index $N$).

Under Circular Systematic Sampling, every unit $i \in U$ appears in exactly $n$ of the $N$ possible systematic samples, guaranteeing that:
$$\pi_i = \frac{n}{N} \quad \forall i \in U$$
Thus, Circular Systematic Sampling achieves exact first-order design unbiasedness without altering the target sample size $n$, resolving the non-integer interval dilemma.

### Implicit Stratification and Spatial Serpentine Ordering
The most powerful empirical application of systematic sampling occurs through **implicit stratification**. Rather than explicitly partitioning a population into separate administrative strata and drawing independent samples within each stratum, a practitioner sorts the sampling frame along key auxiliary variables prior to systematic selection.

Consider a national survey of schools or agricultural plots:
1. **Geographic Serpentine Sorting**: The units on the sampling frame are sorted geographically along a contiguous serpentine path (e.g., zig-zagging across administrative districts from north to south and east to west).
2. **Systematic Traversal**: When a 1-in-$k$ systematic sample is drawn through the sorted frame, the sampling interval $k$ automatically draws exactly one unit from every sequential interval of $k$ units on the list.
3. **Variance Reduction**: Because adjacent units on the sorted frame share similar geographic, climatic, or socioeconomic characteristics, the systematic mechanism forces the sample to spread evenly across all geographic zones and auxiliary categories. This completely eliminates the risk of spatial clustering or regional underrepresentation that can occur under pure SRSWOR.

Mathematically, implicit stratification achieves the precision benefits of proportional stratified sampling—and often surpasses it—because the effective number of implicit strata equals the sample size $n$. By enforcing uniform spacing across the auxiliary gradient, the intraclass correlation coefficient $\rho_{sys}$ becomes negative, substantially reducing the sampling variance relative to unstratified simple random sampling.

## Multi-Objective Sample Size Optimization: The Bethel Algorithm and Kish Penalties

In real-world surveys, statistical investigations rarely measure a single isolated characteristic $y$. National socio-economic surveys typically measure dozens of core indicators simultaneously: household consumption, employment status, educational attainment, health expenditures, and agricultural output. Each variable $j \in \{1, \dots, J\}$ possesses its own intrinsic population variance $S_j^2$ and its own policy-mandated target margin of error $d_j$.

Computing sample sizes independently for each variable produces conflicting requirements: a highly variable characteristic (such as household savings) might require $n = 4,500$ units, whereas a stable demographic proportion (such as primary school enrollment) requires only $n = 800$. Choosing the maximum sample size $\max_j n_j$ satisfies all precision goals but may vastly exceed available financial budgets. Choosing an unweighted average sample size leaves high-priority volatile variables severely underpowered.

To resolve this conflict, survey methodologists deploy the **Bethel Multi-Objective Optimization Algorithm** (Bethel, 1989). Let $c$ denote the unit cost of surveying an element, and let $V_j(\bar{y}_j) = \frac{1 - f}{n} S_j^2 = \left(\frac{1}{n} - \frac{1}{N}\right) S_j^2$ denote the sampling variance of variable $j$. The agency establishes upper variance bounds $v_j^* = d_j^2 / z^2$ for each characteristic $j \in \{1, \dots, J\}$.

The multi-variable sample size problem is formulated as a convex mathematical program:
$$\min_{n} \quad C(n) = c n$$
subject to the $J$ precision constraints:
$$\left(\frac{1}{n} - \frac{1}{N}\right) S_j^2 \le v_j^* \quad \forall j = 1, \dots, J$$
$$1 \le n \le N$$

Rewriting the constraints in terms of the inverse sample size $x = 1/n$:
$$x S_j^2 \le v_j^* + \frac{S_j^2}{N} \implies x \le \frac{v_j^* + S_j^2 / N}{S_j^2} = \frac{v_j^*}{S_j^2} + \frac{1}{N}$$
Taking the reciprocal:
$$n \ge \frac{1}{\frac{v_j^*}{S_j^2} + \frac{1}{N}} = \frac{S_j^2 / v_j^*}{1 + \frac{S_j^2 / v_j^*}{N}} = n_{j}$$
where $n_j$ is the Cochran sample size required by variable $j$. In single-stage simple random sampling, the optimal multi-objective sample size simplifies to the Chebyshev upper envelope:
$$n^* = \max_{j \in \{1, \dots, J\}} n_j$$

In multi-stage and stratified sampling, where costs differ across strata and variables interact with cluster sizes, Bethel’s algorithm utilizes Lagrangian duality to find the global optimum vector of stratum sample sizes, balancing precision trade-offs across all survey objectives.

Leslie Kish (1976) introduced an alternative **compromise allocation** based on minimizing a root-mean-square penalty function:
$$\mathcal{L}(n) = \sum_{j=1}^J w_j \left( \frac{V_j(n) - V_j^*}{V_j^*} \right)^2$$
where $w_j \ge 0$ ($\sum w_j = 1$) represents the policy priority assigned to indicator $j$. This penalty formulation allows survey directors to accept minor precision concessions on secondary indicators to achieve substantial cost savings on primary objectives.

## Subpopulation and Domain Estimation Under Simple Random Sampling

In nearly all practical surveys, inferential interest extends beyond the aggregate population mean $\bar{Y}$ to specific subgroups, designated as **domains of study** (denoted $U_d \subset U$, such as a demographic gender group, an administrative district, or a specific industry classification).

Let $N_d = |U_d|$ denote the number of population units in domain $d$. The domain total and domain mean are:
$$Y_d = \sum_{i \in U_d} y_i, \quad \bar{Y}_d = \frac{1}{N_d} \sum_{i \in U_d} y_i$$
Define the domain membership indicator:
$$z_{di} = \begin{cases} 1 & \text{if unit } i \in U_d \\ 0 & \text{if unit } i \notin U_d \end{cases}$$
and the domain-specific variable:
$$y_{di}^* = z_{di} y_i = \begin{cases} y_i & \text{if unit } i \in U_d \\ 0 & \text{if unit } i \notin U_d \end{cases}$$

### Randomness of Domain Sample Size
When an SRSWOR sample of size $n$ is drawn from the total population $U$, the number of sampled units that happen to fall in domain $d$, denoted $n_d = \sum_{i \in s} z_{di}$, is **not fixed in advance**—it is a random variable following a hypergeometric distribution:
$$n_d \sim \text{Hypergeometric}(N, N_d, n), \quad E[n_d] = n \frac{N_d}{N} = n W_d$$
The standard estimator of the domain mean is:
$$\bar{y}_d = \frac{\sum_{i \in s} y_{di}^*}{\sum_{i \in s} z_{di}} = \frac{1}{n_d} \sum_{i \in s_d} y_i$$
Because the denominator $n_d$ is a random variable, $\bar{y}_d$ is technically a non-linear **ratio estimator**.

### Unconditional and Conditional Variance Properties
The variance of $\bar{y}_d$ can be analyzed from two perspectives:
1. **Conditional Perspective (Conditioning on $n_d \ge 1$)**:
   Conditional on $n_d$, the $n_d$ units constitute a simple random sample without replacement drawn from the domain subpopulation $U_d$. Therefore:
   $$E[\bar{y}_d \mid n_d] = \bar{Y}_d$$
   $$V(\bar{y}_d \mid n_d) = \left( \frac{N_d - n_d}{N_d} \right) \frac{S_d^2}{n_d}$$
   where $S_d^2 = \frac{1}{N_d - 1} \sum_{i \in U_d} (y_i - \bar{Y}_d)^2$ is the internal domain variance.
2. **Unconditional Perspective**:
   By the law of total variance:
   $$V(\bar{y}_d) = E[V(\bar{y}_d \mid n_d)] + V(E[\bar{y}_d \mid n_d]) = E\left[ \left( \frac{1}{n_d} - \frac{1}{N_d} \right) S_d^2 \right] + V(\bar{Y}_d)$$
   Since $\bar{Y}_d$ is a constant, $V(\bar{Y}_d) = 0$. Approximating $E[1/n_d] \approx \frac{1}{E[n_d]} = \frac{1}{n W_d}$:
   $$V(\bar{y}_d) \approx \left( \frac{1}{n W_d} - \frac{1}{N_d} \right) S_d^2 = \frac{1 - f}{n W_d} S_d^2$$
   where $f = n / N = (n W_d) / N_d$.

The unbiased sample estimator of the domain variance is:
$$v(\bar{y}_d) = \left( \frac{N_d - n_d}{N_d} \right) \frac{s_d^2}{n_d}$$
where $s_d^2 = \frac{1}{n_d - 1} \sum_{i \in s_d} (y_i - \bar{y}_d)^2$. If the domain population size $N_d$ is unknown, it is estimated by $\hat{N}_d = N (n_d / n)$, leading to the classic ratio variance formula.

Domain estimation reveals that whenever subgroups are of primary inferential interest, unstratified SRSWOR leaves domain sample sizes to chance, creating vulnerability to small $n_d$ and large standard errors. This provides the direct operational motivation for stratification.

---

## Fully worked question 1: Rigorous Derivation of SRSWOR Variance and Sample Variance Unbiasedness

**Question.** Consider a small finite population of $N = 5$ university research laboratories labeled $U = \{1, 2, 3, 4, 5\}$. The recorded variable $y_i$ represents the number of peer-reviewed journal publications produced in the past academic year:
$$y_1 = 2, \quad y_2 = 4, \quad y_3 = 6, \quad y_4 = 8, \quad y_5 = 10$$
A simple random sample without replacement (SRSWOR) of size $n = 3$ is selected from this population.
(a) Compute the population mean $\bar{Y}$, the population element variance $\sigma^2$, and the finite population variance $S^2$.
(b) Enumerate all $\binom{5}{3} = 10$ possible samples. For each sample $s_k$, calculate the sample mean $\bar{y}_k$ and the sample variance $s_k^2$.
(c) Demonstrate by direct discrete expectation over all 10 equally likely samples that:
    (i) $E[\bar{y}] = \bar{Y}$ (unbiasedness of sample mean),
    (ii) $E[s^2] = S^2$ (unbiasedness of sample variance),
    (iii) $V(\bar{y}) = \frac{1 - f}{n} S^2$ (exact variance formula).

**Solution, step 1: Compute population parameters.**
Calculate the finite population mean:
$$\bar{Y} = \frac{\sum_{i=1}^5 y_i}{5} = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = 6.0$$
Calculate the squared deviations from the mean:
$$(2 - 6)^2 = 16, \quad (4 - 6)^2 = 4, \quad (6 - 6)^2 = 0, \quad (8 - 6)^2 = 4, \quad (10 - 6)^2 = 16$$
$$\sum_{i=1}^5 (y_i - \bar{Y})^2 = 16 + 4 + 0 + 4 + 16 = 40.0$$

The population element variance is:
$$\sigma^2 = \frac{1}{N} \sum_{i=1}^N (y_i - \bar{Y})^2 = \frac{40}{5} = 8.0$$
The finite population variance (with divisor $N - 1 = 4$) is:
$$S^2 = \frac{1}{N - 1} \sum_{i=1}^N (y_i - \bar{Y})^2 = \frac{40}{4} = 10.0$$
The sampling fraction is $f = n / N = 3 / 5 = 0.60$.
The theoretical variance of $\bar{y}$ predicted by our formula is:
$$V(\bar{y}) = \frac{1 - f}{n} S^2 = \left( \frac{1 - 0.60}{3} \right) (10.0) = \left( \frac{0.40}{3} \right) (10.0) = \frac{4.0}{3} \approx 1.333333$$

**Solution, step 2: Enumerate all 10 samples and compute sample statistics.**
Under SRSWOR, each of the $\binom{5}{3} = 10$ samples has an identical selection probability of $p(s_k) = 1/10 = 0.10$. We list each sample, its values, sample mean $\bar{y} = \frac{1}{3}\sum y_i$, and sample variance $s^2 = \frac{1}{2}\sum (y_i - \bar{y})^2$:

1. $s_1 = \{1, 2, 3\} \implies \{2, 4, 6\}$:
   $$\bar{y}_1 = \frac{12}{3} = 4.0, \quad \sum (y_i - 4)^2 = (2-4)^2 + (4-4)^2 + (6-4)^2 = 4 + 0 + 4 = 8 \implies s_1^2 = \frac{8}{2} = 4.0$$
2. $s_2 = \{1, 2, 4\} \implies \{2, 4, 8\}$:
   $$\bar{y}_2 = \frac{14}{3} = 4.6667, \quad \sum (y_i - \frac{14}{3})^2 = \left(-\frac{8}{3}\right)^2 + \left(-\frac{2}{3}\right)^2 + \left(\frac{10}{3}\right)^2 = \frac{64 + 4 + 100}{9} = \frac{168}{9} = \frac{56}{3} \implies s_2^2 = \frac{28}{3} \approx 9.3333$$
3. $s_3 = \{1, 2, 5\} \implies \{2, 4, 10\}$:
   $$\bar{y}_3 = \frac{16}{3} = 5.3333, \quad \sum (y_i - \frac{16}{3})^2 = \left(-\frac{10}{3}\right)^2 + \left(-\frac{4}{3}\right)^2 + \left(\frac{14}{3}\right)^2 = \frac{100 + 16 + 196}{9} = \frac{312}{9} = \frac{104}{3} \implies s_3^2 = \frac{52}{3} \approx 17.3333$$
4. $s_4 = \{1, 3, 4\} \implies \{2, 6, 8\}$:
   $$\bar{y}_4 = \frac{16}{3} = 5.3333, \quad \sum (y_i - \frac{16}{3})^2 = \left(-\frac{10}{3}\right)^2 + \left(\frac{2}{3}\right)^2 + \left(\frac{8}{3}\right)^2 = \frac{100 + 4 + 64}{9} = \frac{168}{9} = \frac{56}{3} \implies s_4^2 = \frac{28}{3} \approx 9.3333$$
5. $s_5 = \{1, 3, 5\} \implies \{2, 6, 10\}$:
   $$\bar{y}_5 = \frac{18}{3} = 6.0, \quad \sum (y_i - 6)^2 = (2-6)^2 + (6-6)^2 + (10-6)^2 = 16 + 0 + 16 = 32 \implies s_5^2 = \frac{32}{2} = 16.0$$
6. $s_6 = \{1, 4, 5\} \implies \{2, 8, 10\}$:
   $$\bar{y}_6 = \frac{20}{3} = 6.6667, \quad \sum (y_i - \frac{20}{3})^2 = \left(-\frac{14}{3}\right)^2 + \left(\frac{4}{3}\right)^2 + \left(\frac{10}{3}\right)^2 = \frac{196 + 16 + 100}{9} = \frac{312}{9} = \frac{104}{3} \implies s_6^2 = \frac{52}{3} \approx 17.3333$$
7. $s_7 = \{2, 3, 4\} \implies \{4, 6, 8\}$:
   $$\bar{y}_7 = \frac{18}{3} = 6.0, \quad \sum (y_i - 6)^2 = (4-6)^2 + (6-6)^2 + (8-6)^2 = 4 + 0 + 4 = 8 \implies s_7^2 = \frac{8}{2} = 4.0$$
8. $s_8 = \{2, 3, 5\} \implies \{4, 6, 10\}$:
   $$\bar{y}_8 = \frac{20}{3} = 6.6667, \quad \sum (y_i - \frac{20}{3})^2 = \left(-\frac{8}{3}\right)^2 + \left(-\frac{2}{3}\right)^2 + \left(\frac{10}{3}\right)^2 = \frac{64 + 4 + 100}{9} = \frac{168}{9} = \frac{56}{3} \implies s_8^2 = \frac{28}{3} \approx 9.3333$$
9. $s_9 = \{2, 4, 5\} \implies \{4, 8, 10\}$:
   $$\bar{y}_9 = \frac{22}{3} = 7.3333, \quad \sum (y_i - \frac{22}{3})^2 = \left(-\frac{10}{3}\right)^2 + \left(\frac{2}{3}\right)^2 + \left(\frac{8}{3}\right)^2 = \frac{100 + 4 + 64}{9} = \frac{168}{9} = \frac{56}{3} \implies s_9^2 = \frac{28}{3} \approx 9.3333$$
10. $s_{10} = \{3, 4, 5\} \implies \{6, 8, 10\}$:
    $$\bar{y}_{10} = \frac{24}{3} = 8.0, \quad \sum (y_i - 8)^2 = (6-8)^2 + (8-8)^2 + (10-8)^2 = 4 + 0 + 4 = 8 \implies s_{10}^2 = \frac{8}{2} = 4.0$$

**Solution, step 3: Evaluate expectations and verify theoretical theorems.**
First, evaluate the expectation of the sample mean:
$$E[\bar{y}] = \sum_{k=1}^{10} p(s_k) \bar{y}_k = \frac{1}{10} \sum_{k=1}^{10} \bar{y}_k$$
Sum the 10 sample means:
$$\sum_{k=1}^{10} \bar{y}_k = 4.0 + \frac{14}{3} + \frac{16}{3} + \frac{16}{3} + 6.0 + \frac{20}{3} + 6.0 + \frac{20}{3} + \frac{22}{3} + 8.0$$
$$= (4 + 6 + 6 + 8) + \frac{14 + 16 + 16 + 20 + 20 + 22}{3} = 24 + \frac{108}{3} = 24 + 36 = 60.0$$
Therefore:
$$E[\bar{y}] = \frac{60.0}{10} = 6.0 = \bar{Y}$$
This confirms the design unbiasedness of $\bar{y}$ by complete enumeration.

Second, evaluate the expectation of the sample variance $s^2$:
$$E[s^2] = \frac{1}{10} \sum_{k=1}^{10} s_k^2 = \frac{1}{10} \left[ 4 + \frac{28}{3} + \frac{52}{3} + \frac{28}{3} + 16 + \frac{52}{3} + 4 + \frac{28}{3} + \frac{28}{3} + 4 \right]$$
$$= \frac{1}{10} \left[ (4 + 16 + 4 + 4) + \frac{28 + 52 + 28 + 52 + 28 + 28}{3} \right] = \frac{1}{10} \left[ 28 + \frac{216}{3} \right] = \frac{1}{10} [28 + 72] = \frac{100}{10} = 10.0 = S^2$$
This confirms by exact enumeration that $E[s^2] = S^2$.

Third, evaluate the variance of $\bar{y}$ directly from its definition:
$$V(\bar{y}) = E[(\bar{y} - \bar{Y})^2] = \frac{1}{10} \sum_{k=1}^{10} (\bar{y}_k - 6.0)^2$$
Compute the squared deviations of the 10 sample means from 6.0:
$$(\bar{y}_1 - 6)^2 = (4 - 6)^2 = 4 = \frac{36}{9}$$
$$(\bar{y}_2 - 6)^2 = \left(\frac{14}{3} - 6\right)^2 = \left(-\frac{4}{3}\right)^2 = \frac{16}{9}$$
$$(\bar{y}_3 - 6)^2 = \left(\frac{16}{3} - 6\right)^2 = \left(-\frac{2}{3}\right)^2 = \frac{4}{9}$$
$$(\bar{y}_4 - 6)^2 = \left(\frac{16}{3} - 6\right)^2 = \frac{4}{9}$$
$$(\bar{y}_5 - 6)^2 = (6 - 6)^2 = 0$$
$$(\bar{y}_6 - 6)^2 = \left(\frac{20}{3} - 6\right)^2 = \left(\frac{2}{3}\right)^2 = \frac{4}{9}$$
$$(\bar{y}_7 - 6)^2 = (6 - 6)^2 = 0$$
$$(\bar{y}_8 - 6)^2 = \left(\frac{20}{3} - 6\right)^2 = \frac{4}{9}$$
$$(\bar{y}_9 - 6)^2 = \left(\frac{22}{3} - 6\right)^2 = \left(\frac{4}{3}\right)^2 = \frac{16}{9}$$
$$(\bar{y}_{10} - 6)^2 = (8 - 6)^2 = 4 = \frac{36}{9}$$
Sum of squared deviations:
$$\sum_{k=1}^{10} (\bar{y}_k - 6)^2 = \frac{36 + 16 + 4 + 4 + 0 + 4 + 0 + 4 + 16 + 36}{9} = \frac{120}{9} = \frac{40}{3}$$
Therefore, the exact sampling variance is:
$$V(\bar{y}) = \frac{1}{10} \left( \frac{40}{3} \right) = \frac{4}{3} \approx 1.333333$$
This matches the theoretical formula $\frac{1 - f}{n} S^2 = \frac{1 - 0.6}{3} (10) = \frac{4}{3}$ to the last decimal place.

---

## Fully worked question 2: Exact Sample Size Determination for a Finite Population Proportion

**Question.** A regional public health authority plans a survey to estimate the proportion $P$ of adult residents who have received an updated seasonal influenza vaccination in a metropolitan district of $N = 12,000$ adults. The health department requires:
1. An absolute margin of error $d = 0.03$ (i.e., within $\pm 3$ percentage points of the true population proportion).
2. A $95\%$ confidence level, corresponding to a standard normal two-tailed critical value of $z_{0.025} = 1.96$.

(a) Determine the initial sample size $n_0$ and the required sample size $n$ using the conservative assumption $P = 0.50$. Calculate the percentage reduction in required sample size achieved by applying the Finite Population Correction (FPC).
(b) Prior health clinic administrative records suggest that the true vaccination coverage is approximately $P \approx 0.25$. Recalculate the required sample size $n$ using this informed prior proportion.
(c) Suppose the field budget is capped at a maximum affordable sample size of $n_{max} = 600$. If $n = 600$ is fielded, determine the exact margin of error $d$ achieved under both $P = 0.50$ and $P = 0.25$, accounting for the FPC.

**Solution, step 1: Conservative sample size determination ($P = 0.50$).**
Under the conservative approach, we set $P = 0.50$, which maximizes the variance product:
$$P(1 - P) = (0.50)(1 - 0.50) = 0.25$$
Compute the initial sample size without FPC:
$$n_0 = \frac{z^2 P(1 - P)}{d^2} = \frac{(1.96)^2 (0.25)}{(0.03)^2} = \frac{(3.8416)(0.25)}{0.0009} = \frac{0.9604}{0.0009} \approx 1,067.111$$

Now apply the Cochran finite population correction for $N = 12,000$:
$$n = \frac{n_0}{1 + \frac{n_0}{N}} = \frac{1,067.111}{1 + \frac{1,067.111}{12,000}} = \frac{1,067.111}{1 + 0.088926} = \frac{1,067.111}{1.088926} \approx 979.966$$
Rounding up to the nearest integer to ensure the margin of error does not exceed $0.03$:
$$n = 980 \text{ respondents}$$

Calculate the percentage reduction in sample size due to FPC:
$$\text{Reduction} = \frac{n_0 - n}{n_0} \times 100\% = \frac{1,067.111 - 979.966}{1,067.111} \times 100\% = \frac{87.145}{1,067.111} \times 100\% \approx 8.166\%$$
The FPC saves the agency from interviewing 88 respondents, conserving significant field costs.

**Solution, step 2: Sample size using informed prior ($P = 0.25$).**
Using the informed prior proportion $P = 0.25$:
$$P(1 - P) = (0.25)(0.75) = 0.1875$$
Compute the initial sample size without FPC:
$$n_0 = \frac{z^2 P(1 - P)}{d^2} = \frac{(3.8416)(0.1875)}{0.0009} = \frac{0.7203}{0.0009} = 800.333$$

Apply the finite population correction:
$$n = \frac{n_0}{1 + \frac{n_0}{N}} = \frac{800.333}{1 + \frac{800.333}{12,000}} = \frac{800.333}{1 + 0.066694} = \frac{800.333}{1.066694} \approx 750.293$$
Rounding up:
$$n = 751 \text{ respondents}$$
Compared to the conservative sample size of 980, utilizing prior domain knowledge reduces the required sample size by:
$$980 - 751 = 229 \text{ respondents (a 23.37\% reduction)}$$

**Solution, step 3: Achieved margin of error under budget constraint ($n_{max} = 600$).**
When $n = 600$ is fixed, the sampling fraction is:
$$f = \frac{n}{N} = \frac{600}{12,000} = 0.05$$
The FPC factor is $1 - f = 1 - 0.05 = 0.95$.
The achieved margin of error is given by:
$$d = z \sqrt{V(p)} = z \sqrt{\left(\frac{N - n}{N - 1}\right) \frac{P(1 - P)}{n}}$$
Notice that $\frac{N - n}{N - 1} = \frac{12,000 - 600}{11,999} = \frac{11,400}{11,999} \approx 0.950079$.

Case 1: Under $P = 0.50$:
$$V(p) = (0.950079) \frac{0.25}{600} = (0.950079)(0.00041667) \approx 0.00039587$$
$$d = 1.96 \sqrt{0.00039587} = 1.96 (0.019896) \approx 0.038997 \implies \pm 3.90\%$$

Case 2: Under $P = 0.25$:
$$V(p) = (0.950079) \frac{0.1875}{600} = (0.950079)(0.0003125) \approx 0.00029690$$
$$d = 1.96 \sqrt{0.00029690} = 1.96 (0.017231) \approx 0.033772 \implies \pm 3.38\%$$

Under the budget-constrained sample of 600, the margin of error increases slightly from the target $3.00\%$ to $3.38\%$ (if $P=0.25$) or $3.90\%$ (if $P=0.50$). This trade-off analysis allows decision-makers to evaluate whether the additional cost of surveying 151 or 380 extra units is justified by the marginal reduction in error margin.

---

## Fully worked question 3: Theoretical and Empirical Efficiency Comparison: SRSWOR versus SRSWR

**Question.** Let a finite population $U$ contain $N$ elements with values $y_1, \dots, y_N$.
(a) Prove analytically that the variance of the sample mean under Simple Random Sampling Without Replacement ($V_{wor}$) is strictly smaller than the variance under Simple Random Sampling With Replacement ($V_{wr}$) for any sample size $n > 1$, and establish the exact relationship:
$$V_{wor}(\bar{y}) = \left( \frac{N - n}{N - 1} \right) V_{wr}(\bar{y})$$
(b) Define the Relative Efficiency (RE) of SRSWOR with respect to SRSWR as:
$$\text{RE} = \frac{V_{wr}(\bar{y})}{V_{wor}(\bar{y})}$$
Derive the expression for $\text{RE}$ in terms of the population size $N$ and the sampling fraction $f = n / N$.
(c) Evaluate $\text{RE}$ and the percentage variance reduction across a range of sampling fractions $f \in \{0.01, 0.05, 0.10, 0.25, 0.50\}$ for a finite population of size $N = 1,000$. Interpret the pedagogical and practical significance of these results.

**Solution, step 1: Prove the exact algebraic relationship between $V_{wor}$ and $V_{wr}$.**
In Simple Random Sampling With Replacement (SRSWR), the sample consists of $n$ independent draws from the population, where each draw selects unit $i$ with probability $1/N$. The expected value of a single draw is $\bar{Y}$, and the variance of a single draw is the population element variance:
$$\sigma^2 = \frac{1}{N} \sum_{i=1}^N (y_i - \bar{Y})^2$$
Because the draws are mutually independent, the variance of the sample mean $\bar{y}_{wr} = \frac{1}{n} \sum_{k=1}^n y_{(k)}$ is:
$$V_{wr}(\bar{y}) = \frac{\sigma^2}{n} = \frac{1}{n} \left( \frac{N - 1}{N} S^2 \right)$$
where we have used the identity $\sigma^2 = \frac{N - 1}{N} S^2$.

Now consider the variance of the sample mean under SRSWOR:
$$V_{wor}(\bar{y}) = \frac{1 - f}{n} S^2 = \left( \frac{N - n}{N} \right) \frac{S^2}{n}$$
Substitute $S^2 = \frac{N}{N - 1} \sigma^2$ into the expression for $V_{wor}(\bar{y})$:
$$V_{wor}(\bar{y}) = \left( \frac{N - n}{N} \right) \frac{1}{n} \left( \frac{N}{N - 1} \sigma^2 \right) = \left( \frac{N - n}{N - 1} \right) \frac{\sigma^2}{n}$$
Notice that the term $\sigma^2 / n$ is precisely $V_{wr}(\bar{y})$. Therefore:
$$V_{wor}(\bar{y}) = \left( \frac{N - n}{N - 1} \right) V_{wr}(\bar{y})$$

For any sample size $n > 1$, we have $N - n < N - 1$, which implies:
$$\frac{N - n}{N - 1} < 1 \implies V_{wor}(\bar{y}) < V_{wr}(\bar{y})$$
This completes the mathematical proof that SRSWOR is strictly more efficient than SRSWR for all $n > 1$.

**Solution, step 2: Formulate the Relative Efficiency ratio.**
The Relative Efficiency (RE) is:
$$\text{RE} = \frac{V_{wr}(\bar{y})}{V_{wor}(\bar{y})} = \frac{V_{wr}(\bar{y})}{\left( \frac{N - n}{N - 1} \right) V_{wr}(\bar{y})} = \frac{N - 1}{N - n}$$
We express this in terms of the sampling fraction $f = n/N$. Dividing numerator and denominator by $N$:
$$\text{RE} = \frac{1 - \frac{1}{N}}{1 - \frac{n}{N}} = \frac{1 - \frac{1}{N}}{1 - f}$$
When $N$ is reasonably large, $1/N \approx 0$, and the relative efficiency simplifies to:
$$\text{RE} \approx \frac{1}{1 - f}$$
The percentage reduction in variance achieved by eliminating replacement is:
$$\text{Gain} = \frac{V_{wr} - V_{wor}}{V_{wr}} \times 100\% = \left( 1 - \frac{N - n}{N - 1} \right) \times 100\% = \left( \frac{n - 1}{N - 1} \right) \times 100\% \approx f \times 100\%$$

**Solution, step 3: Numerical evaluation for $N = 1,000$.**
Let $N = 1,000$. We evaluate the exact ratio $\text{RE} = \frac{999}{1,000 - n}$ and the percentage variance reduction across the stipulated sampling fractions:

1. For $f = 0.01 \implies n = 10$:
   $$\text{RE} = \frac{999}{1,000 - 10} = \frac{999}{990} \approx 1.00909$$
   $$\text{Variance Reduction} = \frac{10 - 1}{999} \times 100\% = \frac{9}{999} \times 100\% \approx 0.901\%$$
2. For $f = 0.05 \implies n = 50$:
   $$\text{RE} = \frac{999}{1,000 - 50} = \frac{999}{950} \approx 1.05158$$
   $$\text{Variance Reduction} = \frac{50 - 1}{999} \times 100\% = \frac{49}{999} \times 100\% \approx 4.905\%$$
3. For $f = 0.10 \implies n = 100$:
   $$\text{RE} = \frac{999}{1,000 - 100} = \frac{999}{900} = 1.11000$$
   $$\text{Variance Reduction} = \frac{100 - 1}{999} \times 100\% = \frac{99}{999} \times 100\% \approx 9.910\%$$
4. For $f = 0.25 \implies n = 250$:
   $$\text{RE} = \frac{999}{1,000 - 250} = \frac{999}{750} = 1.33200$$
   $$\text{Variance Reduction} = \frac{250 - 1}{999} \times 100\% = \frac{249}{999} \times 100\% \approx 24.925\%$$
5. For $f = 0.50 \implies n = 500$:
   $$\text{RE} = \frac{999}{1,000 - 500} = \frac{999}{500} = 1.99800$$
   $$\text{Variance Reduction} = \frac{500 - 1}{999} \times 100\% = \frac{499}{999} \times 100\% \approx 49.950\%$$

### Practical and Pedagogical Interpretation
- When the sampling fraction is trivial ($f \le 0.01$), the variance reduction is less than $1\%$, and the distinction between with-replacement and without-replacement sampling is negligible. In this regime, applying infinite-population formulas produces no practical error.
- Standard textbook conventions recommend ignoring the FPC whenever $f \le 0.05$. However, at $f = 0.05$, omitting the FPC overstates the sampling variance by approximately $5.16\%$ and overestimates the standard error by $2.55\%$.
- When $f$ reaches $0.25$ or $0.50$, ignoring the FPC becomes unacceptable: at $f = 0.50$, SRSWOR is twice as efficient as SRSWR ($\text{RE} \approx 2.0$), halving the required sampling variance. A researcher who ignores the FPC at $f = 0.50$ would construct confidence intervals that are $\sqrt{2} \approx 1.414$ times wider than necessary, severely understating the true precision of the empirical investigation.

---

## Higher-Order Moments and Tschuprow's Exact Variance of the Sample Variance

In standard survey estimation, primary attention centers upon estimating the first moment—the population mean $\bar{Y}$ or total $Y$. However, in statistical quality control, auditing, and econometric risk management, the parameter of interest is frequently the dispersion itself, quantified by the finite-population variance $S^2 = \frac{1}{N - 1} \sum_{i=1}^N (y_i - \bar{Y})^2$. While we proved in Worked Question 1 that the sample variance $s^2 = \frac{1}{n - 1} \sum_{i=1}^n (y_i - \bar{y})^2$ is an strictly design-unbiased estimator of $S^2$ under SRSWOR ($E(s^2) = S^2$), evaluating the reliability of $s^2$ requires deriving its sampling variance $V(s^2)$.

### Finite-Population Central Moments

To formalize higher-order moment theory, we define the $r$-th finite-population central moment:
$$\mu_r = \frac{1}{N} \sum_{i=1}^N (y_i - \bar{Y})^r \quad (r = 2, 3, 4, \dots)$$
In particular:
- $\mu_2 = \frac{N - 1}{N} S^2$ is the population second central moment.
- $\mu_3 = \frac{1}{N} \sum_{i=1}^N (y_i - \bar{Y})^3$ measures population skewness, with standardized skewness coefficient $\gamma_1 = \mu_3 / \mu_2^{3/2}$.
- $\mu_4 = \frac{1}{N} \sum_{i=1}^N (y_i - \bar{Y})^4$ measures population tail heaviness and kurtosis, with standardized kurtosis coefficient $\beta_2 = \mu_4 / \mu_2^2$.

Similarly, we define the finite-population symmetric polynomial parameters, known as Fisher's $k$-statistics:
$$k_2 = S^2 = \frac{1}{N - 1} \sum_{i=1}^N (y_i - \bar{Y})^2$$
$$k_4 = \frac{N}{(N - 1)(N - 2)(N - 3)} \left[ (N + 1)\mu_4 - 3(N - 1)\mu_2^2 \right]$$

### Tschuprow's Exact Variance Theorem

In 1928, the mathematical statistician A. A. Tschuprow established the exact variance of the sample variance $s^2$ under SRSWOR without making any distributional assumptions (such as normality) regarding the values in the finite population.

Tschuprow's exact finite-population variance formula is:
$$V(s^2) = \frac{1}{n} \left[ \mu_4 - \left( \frac{n - 3}{n - 1} \right) \mu_2^2 \right] - \frac{1}{N} \left[ \mu_4 - \left( \frac{N - 3}{N - 1} \right) \mu_2^2 \right] + O\left(\frac{1}{n N}\right)$$

In terms of Fisher's $k$-statistics and the sampling fraction $f = n / N$, the exact expression simplifies to:
$$V(s^2) = \left( \frac{1 - f}{n} \right) \left[ k_4 + \frac{2 n}{n - 1} k_2^2 \right]$$

For large finite populations where $N \gg n \gg 1$, this expression yields the practical approximation:
$$V(s^2) \approx \frac{1 - f}{n} S^4 \left[ (\beta_2 - 1) + \frac{2}{n - 1} \right] \approx \frac{1 - f}{n} S^4 (\beta_2 - 1)$$
where $\beta_2 = \mu_4 / \mu_2^2$ is the population kurtosis.

#### Critical Methodological Lessons:
1. **Kurtosis Sensitivity**: The variance of the sample variance depends overwhelmingly on the population kurtosis $\beta_2$. If the population distribution has heavy tails or extreme outliers (such as household wealth, financial transactions, or pollutant concentrations where $\beta_2$ can exceed $10$ or $20$), $V(s^2)$ explodes. Estimating variance from a heavy-tailed population requires dramatically larger sample sizes than estimating a mean.
2. **Normal Distribution Benchmark**: If the finite population values follow an approximately Gaussian bell curve, the population kurtosis is $\beta_2 = 3$. Substituting $\beta_2 = 3$ into the formula yields:
   $$V(s^2) \approx \frac{1 - f}{n} S^4 \left[ (3 - 1) + \frac{2}{n - 1} \right] = \frac{2 (1 - f)}{n - 1} S^4$$
   This matches the classical infinite-normal-theory result $V(s^2) = \frac{2 \sigma^4}{n - 1}$, scaled by the finite population correction $(1 - f)$.
3. **Finite-Sample Stability**: Because the sample kurtosis is itself subject to severe estimation noise, sample-based estimates of $V(s^2)$ are unstable unless $n \ge 200$.

---

## Asymptotic Normality and Finite-Population Central Limit Theorems

In elementary statistics, the construction of confidence intervals $\bar{y} \pm z_{\alpha/2} \frac{S}{\sqrt{n}}$ relies upon the classical Central Limit Theorem (CLT) of Lindeberg and Lévy. However, the standard Lindeberg–Lévy theorem presumes an infinite sequence of independent and identically distributed random variables. In survey sampling without replacement:
1. The draws are **dependent**: observing unit $i$ on the first draw alters the conditional selection probabilities for all remaining units on subsequent draws.
2. The population size $N$ is **fixed and finite**: as sample size $n$ increases, the remaining unsampled universe $N - n$ shrinks, eventually terminating when $n = N$.

Establishing the mathematical validity of asymptotic normality under SRSWOR required the development of a specialized branch of probability theory: **Finite-Population Central Limit Theory**.

### The Triangular Array Asymptotic Framework

To define asymptotic limits in finite populations, we cannot simply take $n \to \infty$ while holding the population $U$ fixed, because $n$ cannot exceed $N$. Instead, following the mathematical framework formulated by Paul Erdős and Alfréd Rényi (1959) and Jaroslav Hájek (1960), we consider a sequence of finite populations:
$$\{U_\nu\}_{\nu=1}^\infty \quad \text{with population sizes } N_\nu \to \infty$$
From each population $U_\nu$, an SRSWOR sample of size $n_\nu$ is selected, such that both the sample size and the number of unobserved units grow without bound:
$$n_\nu \to \infty \quad \text{and} \quad (N_\nu - n_\nu) \to \infty \quad \text{as } \nu \to \infty$$
This condition guarantees that the sampling fraction $f_\nu = n_\nu / N_\nu$ remains strictly bounded away from $1$ ($0 \le \liminf f_\nu \le \limsup f_\nu < 1$).

For each population $\nu$, let $\bar{Y}_\nu$ and $S_\nu^2$ denote the population mean and variance. The standardized sample mean is defined as:
$$Z_\nu = \frac{\bar{y}_\nu - \bar{Y}_\nu}{\sqrt{V(\bar{y}_\nu)}} = \frac{\bar{y}_\nu - \bar{Y}_\nu}{\sqrt{\frac{1 - f_\nu}{n_\nu}} S_\nu}$$

### Hájek's Finite-Population Central Limit Theorem (1960)

Jaroslav Hájek established the necessary and sufficient condition under which the standardized sample mean $Z_\nu$ converges in distribution to the standard normal distribution $\mathcal{N}(0, 1)$.

Define the Lindeberg–Hájek sum for any fixed threshold $\tau > 0$:
$$L_\nu(\tau) = \frac{\sum_{i \in U_{\nu, \tau}} (y_{\nu i} - \bar{Y}_\nu)^2}{\sum_{i=1}^{N_\nu} (y_{\nu i} - \bar{Y}_\nu)^2}$$
where the summation in the numerator is taken over the subset of population units whose squared deviation exceeds a threshold scaled by the total variance and sample size:
$$U_{\nu, \tau} = \left\{ i \in U_\nu : |y_{\nu i} - \bar{Y}_\nu| > \tau \sqrt{n_\nu (1 - f_\nu)} S_\nu \right\}$$

**Theorem (Hájek, 1960)**:
The standardized sample mean converges in distribution to standard normal:
$$Z_\nu \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{as } \nu \to \infty$$
if and only if the Lindeberg–Hájek condition holds:
$$\lim_{\nu \to \infty} L_\nu(\tau) = 0 \quad \text{for every } \tau > 0$$

#### Substantive Meaning of Hájek's Condition:
Hájek's theorem establishes that asymptotic normality holds unless the finite population is dominated by a tiny number of extreme outlier values. Specifically, if the maximum squared deviation $\max_i (y_{\nu i} - \bar{Y}_\nu)^2$ is of smaller order than $n_\nu(1 - f_\nu) S_\nu^2$, no individual observation unit can exert a non-negligible influence on the sample mean, and the averaging effect of the randomized mechanism drives the sampling distribution toward the Gaussian curve.

### Berry–Esseen Convergence Rates for Finite Populations

While Hájek's theorem proves asymptotic convergence, practical survey analysts require knowing: *How large must $n$ be for the normal approximation to be trustworthy?*

The speed of convergence to normality is governed by the **Berry–Esseen Theorem for Finite Populations**, established by A. Bikelis (1969) and refined by T. Höglund (1978):
$$\sup_{z \in \mathbb{R}} \left| P(Z_\nu \le z) - \Phi(z) \right| \le \frac{C}{\sqrt{n(1 - f)}} \cdot \frac{\mu_3}{S^3} = \frac{C \cdot |\gamma_1|}{\sqrt{n(1 - f)}}$$
where $\Phi(z)$ is the standard normal cumulative distribution function, $\gamma_1 = \mu_3 / S^3$ is the finite-population skewness coefficient, and $C$ is a universal mathematical constant ($C \approx 0.705$).

#### Cochran's Sample Size Rule of Thumb:
From the Berry–Esseen bound, William Cochran (1977) derived a famous practical guideline: For a 95% confidence interval based on the normal approximation to have an actual error rate of less than 0.5% (meaning true coverage is between 94.5% and 95.5%), the minimum sample size must satisfy:
$$n > 25 \gamma_1^2 = 25 \left( \frac{\mu_3}{S^3} \right)^2$$

- If the population is symmetric ($\gamma_1 \approx 0$), sample sizes as small as $n = 30$ provide outstanding normal coverage.
- If the population is moderately skewed (e.g., household income in an urban district with $\gamma_1 = 2.0$), Cochran's rule requires $n > 25(2.0)^2 = 100$ observations.
- If the population is severely skewed (e.g., corporate revenues or toxic chemical spills with $\gamma_1 = 5.0$), normal approximation requires $n > 25(5.0)^2 = 625$ observations. Below this threshold, Student's $t$ or normal confidence intervals suffer from severe asymmetric coverage error, and the statistician should deploy logarithmic transformations, stratification, or empirical bootstrap intervals.

---

## Inverse Sampling (Negative Hypergeometric Sampling) for Rare Attributes

A major operational limitation of standard Simple Random Sampling arises when the objective is to estimate the prevalence of an exceptionally **rare attribute or condition** within a finite population. Consider an inquiry designed to estimate:
- The prevalence of an ultra-rare genetic disorder ($P \approx 0.001$, or 1 in 1,000 individuals).
- The presence of unexploded ordnance in agricultural land reclamation ($P \approx 0.002$).
- The proportion of fraudulent transaction files in a massive banking archive ($P \approx 0.0005$).

If an investigator applies standard fixed-sample-size SRSWOR with $n = 500$ to a population with $P = 0.001$, the probability of observing **zero positive cases** in the entire sample is:
$$P(m = 0) = \frac{\binom{N - NP}{n}}{\binom{N}{n}} \approx (1 - P)^n = (0.999)^{500} \approx 0.606$$
Over $60\%$ of all possible samples will contain zero positive units! When $m = 0$, the naive sample proportion is $p = 0 / 500 = 0$, which provides zero information regarding whether the true prevalence is $0.001$, $0.0001$, or $0.00001$, and standard Wald confidence intervals collapse to the degenerate point $[0, 0]$.

### The Haldane–Tschuprow Inverse Sampling Protocol

To solve this rare-event dilemma, J. B. S. Haldane (1945) and A. A. Tschuprow introduced **Inverse Sampling** (also known as Negative Hypergeometric Sampling). 

Instead of fixing the sample size $n$ in advance and observing a random count of positive cases $m$, inverse sampling **inverts the protocol**:
1. The statistician pre-specifies a fixed integer $m \ge 2$—the target number of positive units required to achieve reliable estimation (typically $m \in \{10, 20, 30\}$).
2. Units are drawn sequentially without replacement from the finite population $U$ of size $N$ one by one.
3. The sampling process **terminates immediately** upon encountering the $m$-th positive unit.

Under this protocol, the number of positive units $m$ is fixed deterministically, while the total number of draws $n$ required to terminate the survey is a **random variable**.

### The Negative Hypergeometric Probability Distribution

Let $M = N P$ denote the true total number of positive units in the finite population of size $N$. The random sample size $n$ required to observe exactly $m$ positive units follows the **Negative Hypergeometric Distribution**:
$$P(n = k) = \frac{\binom{M}{m - 1} \binom{N - M}{k - m}}{\binom{N}{k - 1}} \cdot \frac{M - (m - 1)}{N - (k - 1)} \quad (k = m, m + 1, \dots, N - M + m)$$

This probability mass function represents the probability of observing exactly $m - 1$ positive units in the first $k - 1$ sequential draws, multiplied by the conditional probability that the $k$-th drawn unit is positive.

### The Strictly Unbiased Estimator of Proportion

A common blunder in inverse sampling is using the naive ratio $\tilde{P} = m / n$. Haldane proved that $\frac{m}{n}$ is systematically **positively biased**:
$$E\left( \frac{m}{n} \right) > P$$
This bias occurs because smaller values of $n$ (which correspond to higher empirical ratios $m/n$) are reached more quickly by the termination rule, shifting the expectation upward.

Haldane derived the **strictly design-unbiased estimator** of the population proportion $P$:
$$\hat{P}_{inv} = \frac{m - 1}{n - 1}$$
where $m$ is the pre-specified target count and $n$ is the total number of draws observed at termination.

#### Proof of Unbiasedness:
Taking the expectation over the Negative Hypergeometric distribution:
$$E(\hat{P}_{inv}) = \sum_{k=m}^{N - M + m} \left( \frac{m - 1}{k - 1} \right) P(n = k)$$
$$= \sum_{k=m}^{N - M + m} \left( \frac{m - 1}{k - 1} \right) \frac{\binom{M}{m - 1} \binom{N - M}{k - m}}{\binom{N}{k - 1}} \frac{M - m + 1}{N - k + 1}$$

Using the combinatorial identity $\frac{m - 1}{k - 1} \frac{\binom{M}{m - 1}}{\binom{N}{k - 1}} = \frac{M}{N} \frac{\binom{M - 1}{m - 2}}{\binom{N - 1}{k - 2}}$:
$$E(\hat{P}_{inv}) = \frac{M}{N} \sum_{k=m}^{N - M + m} \frac{\binom{M - 1}{m - 2} \binom{(N - 1) - (M - 1)}{(k - 1) - (m - 1)}}{\binom{N - 1}{k - 2}} \frac{(M - 1) - (m - 2)}{(N - 1) - (k - 2)}$$
The summation on the right-hand side represents the sum of probabilities of a negative hypergeometric distribution with parameters $(N - 1, M - 1, m - 1)$, which sums identically to $1.0$.
Therefore:
$$E(\hat{P}_{inv}) = \frac{M}{N} \times 1.0 = \frac{M}{N} = P$$
The estimator $\hat{P}_{inv} = \frac{m - 1}{n - 1}$ is strictly design-unbiased for any finite population size $N$ and any attribute count $M \ge m$.

### Unbiased Variance Estimation for Inverse Sampling

The exact sampling variance of $\hat{P}_{inv}$ under finite population inverse sampling is:
$$V(\hat{P}_{inv}) = \frac{P(1 - P)}{E(n) - 1} \left( 1 - \frac{E(n)}{N} \right) + O\left(\frac{1}{E(n)^2}\right)$$

An strictly unbiased estimator of the sampling variance derived by D. G. Chapman (1951) is:
$$\hat{V}(\hat{P}_{inv}) = \frac{\hat{P}_{inv}(1 - \hat{P}_{inv})}{n - 2} \left( 1 - \frac{n}{N} \right) = \frac{(m - 1)(n - m)}{(n - 1)^2 (n - 2)} \left( 1 - \frac{n}{N} \right)$$
provided $n \ge 3$.

#### Operational Comparison: Fixed Sampling vs. Inverse Sampling:
Consider a rare financial fraud audit where the hypothesized violation rate is $P = 0.004$ (4 per 1,000 files) in an institutional database of $N = 25,000$ files:
- Under fixed SRSWOR with $n = 500$: The expected number of violations observed is $E(m) = 500 \times 0.004 = 2.0$. The probability of getting $m \le 1$ violation is $P(m = 0) + P(m = 1) \approx 0.135 + 0.271 = 40.6\%$. Over $40\%$ of all investigations will yield fewer than 2 cases, making reliable variance estimation impossible.
- Under Inverse Sampling with fixed $m = 10$: The investigator draws files until exactly 10 violations are uncovered. The expected number of files examined is $E(n) \approx \frac{m}{P} = \frac{10}{0.004} = 2,500$ files. The resulting estimate $\hat{P}_{inv} = \frac{9}{n - 1}$ is guaranteed to be based on 10 positive cases, ensuring a stable coefficient of variation of approximately $\text{CV} \approx \frac{1}{\sqrt{m}} = \frac{1}{\sqrt{10}} \approx 31.6\%$, completely eliminating the zero-event catastrophe.

---



---

## Inverse Sampling (Negative Hypergeometric Sampling) for Rare Attributes

In conventional simple random sampling without replacement (SRSWOR), the total sample size $n$ is fixed in advance, and the number of sample units $m$ possessing a rare attribute of interest (e.g. individuals infected with an emergent pathogen, businesses committing tax fraud, or rare ecological species) is a stochastic random variable. When the true population proportion $P = M / N$ is very small (for example, $P < 0.01$ or $P < 0.001$), standard fixed-sample designs suffer from a severe risk of zero-event realizations: with high probability, the realized sample may contain zero or only one positive event ($m \le 1$). In such circumstances, the standard sample proportion $\hat{P} = m / n$ has unacceptable relative error, and the sample variance estimator $s^2 / n$ collapses, preventing the construction of meaningful confidence intervals.

To resolve the catastrophic fragility of fixed-sample designs in rare-event settings, J. B. S. Haldane (1945) and D. J. Finney (1949) formulated **Inverse Sampling** (also known as Negative Hypergeometric Sampling).

### The Inverse Sampling Protocol
Instead of fixing the sample size $n$, the survey investigator predetermines a fixed target integer $m \ge 2$ of units possessing the rare attribute. Sampling proceeds sequentially without replacement, unit by unit, until exactly $m$ units possessing the rare attribute are uncovered. 

Under this protocol:
1. The number of positive units observed, $m$, is a fixed deterministic constant.
2. The total number of units sampled, $n$, is a random variable taking integer values in the range $\{m, m + 1, \dots, N - M + m\}$.

### The Negative Hypergeometric Probability Distribution
Let $M$ denote the unknown total number of units in the population possessing the rare attribute, and $N$ denote the known total population size. Sampling terminates at step $n$ if and only if:
1. Exactly $m - 1$ positive units were observed in the first $n - 1$ draws.
2. The $n$-th drawn unit possesses the rare attribute.

Under simple random sampling without replacement, the probability mass function of the stopping sample size $n$ is governed by the **Negative Hypergeometric Distribution**:
$$P(n \mid M, N, m) = \frac{\binom{M}{m - 1} \binom{N - M}{(n - 1) - (m - 1)}}{\binom{N}{n - 1}} \times \frac{M - (m - 1)}{N - (n - 1)}$$

Using combinatorial identities, this probability mass function simplifies to:
$$P(n \mid M, N, m) = \frac{\binom{n - 1}{m - 1} \binom{N - n}{M - m}}{\binom{N}{M}}$$

### Unbiased Estimation of the Population Proportion: Haldane's Estimator
In a naive attempt to estimate the proportion $P = M / N$, one might consider the empirical sample fraction:
$$\tilde{P} = \frac{m}{n}$$
However, because $n$ appears in the denominator and is stochastic, Jensen's inequality implies:
$$E\left( \frac{m}{n} \right) > \frac{m}{E(n)} \approx P$$
The naive estimator $m / n$ is systematically positively biased for the true proportion!

To eliminate this bias, Haldane (1945) derived the unique uniformly minimum-variance unbiased estimator (UMVUE) of the population proportion $P = M / N$:
$$\hat{P}_{inv} = \frac{m - 1}{n - 1}$$

#### Mathematical Proof of Strict Unbiasedness:
We evaluate the expectation of $\hat{P}_{inv}$ over all possible values of $n$:
$$E(\hat{P}_{inv}) = \sum_{n=m}^{N - M + m} \left( \frac{m - 1}{n - 1} \right) P(n \mid M, N, m)$$
$$= \sum_{n=m}^{N - M + m} \left( \frac{m - 1}{n - 1} \right) \frac{\binom{n - 1}{m - 1} \binom{N - n}{M - m}}{\binom{N}{M}}$$

Notice the cancellation between the algebraic factor and the binomial coefficient:
$$\frac{m - 1}{n - 1} \binom{n - 1}{m - 1} = \frac{m - 1}{n - 1} \frac{(n - 1)!}{(m - 1)! (n - m)!} = \frac{(n - 2)!}{(m - 2)! (n - m)!} = \binom{n - 2}{m - 2}$$

Substitute this back into the expectation sum:
$$E(\hat{P}_{inv}) = \frac{1}{\binom{N}{M}} \sum_{n=m}^{N - M + m} \binom{n - 2}{m - 2} \binom{N - n}{M - m}$$

Change index of summation by setting $k = n - 1$. As $n$ ranges from $m$ to $N - M + m$, $k$ ranges from $m - 1$ to $N - M + m - 1$:
$$\sum_{k=m - 1}^{N - M + m - 1} \binom{k - 1}{(m - 1) - 1} \binom{(N - 1) - k}{(M - 1) - (m - 1)} = \binom{N - 1}{M - 1}$$
by the classical Vandermonde convolution identity.

Therefore:
$$E(\hat{P}_{inv}) = \frac{\binom{N - 1}{M - 1}}{\binom{N}{M}} = \frac{\frac{(N - 1)!}{(M - 1)! (N - M)!}}{\frac{N!}{M! (N - M)!}} = \frac{M}{N} = P$$
This proves that Haldane's estimator $\hat{P}_{inv} = \frac{m - 1}{n - 1}$ is strictly design-unbiased for any finite population size $N$ and any target count $m \ge 2$.

### Unbiased Estimation of the Sampling Variance
Finney (1949) demonstrated that the exact sampling variance of $\hat{P}_{inv}$ is:
$$V(\hat{P}_{inv}) = \frac{P (1 - P)}{E(n - 1)} \left( 1 - \frac{E(n)}{N} \right) \approx \frac{P^2 (1 - P)}{m - 1} \left( 1 - \frac{m}{N P} \right)$$

Because the true proportion $P$ is unknown, Finney derived the strictly unbiased sample estimator of variance:
$$\hat{V}(\hat{P}_{inv}) = \frac{\hat{P}_{inv} (1 - \hat{P}_{inv})}{n - 2} \left( 1 - \frac{n - 1}{N} \right) = \frac{\left( \frac{m - 1}{n - 1} \right) \left( 1 - \frac{m - 1}{n - 1} \right)}{n - 2} \left( \frac{N - n + 1}{N} \right)$$

This variance estimator is strictly non-negative and requires only that the target quota satisfies $m \ge 3$.

### Practical Synthesis and Quality Guidance
Inverse sampling provides an invaluable safeguard for public health monitoring and industrial quality inspection:
1. **Guaranteed Precision**: The coefficient of variation of the estimate is governed entirely by the predetermined choice of $m$:
   $$\text{CV}(\hat{P}_{inv}) \approx \frac{1}{\sqrt{m - 1}}$$
   If the investigator desires a coefficient of variation of $20\%$, setting $m = 26$ guarantees $\text{CV} \approx 1/\sqrt{25} = 0.20$, regardless of how rare the attribute is in the population.
2. **Budget Monitoring**: Because the sample size $n$ is stochastic, the field budget cannot be strictly predicted in advance. The expected sample size is $E(n) \approx m / P$. To avoid budget overruns when $P$ is far lower than hypothesized, agencies typically institute a truncation cap $n_{max}$: if $m$ positive cases are not encountered by draw $n_{max}$, sampling terminates, and truncated Bayesian models are deployed.

---

## Practical Synthesis, Quality Diagnostics and Computational Verification

The execution of Simple Random Sampling requires verified algorithmic mechanisms to ensure that the mathematical requirement of uniform sample selection is faithfully realized in computational code.

In statistical software packages (such as R or Python), drawing an SRSWOR sample must avoid common pseudo-random number generator pitfalls. In Python, the standard implementation relies on the Mersenne Twister algorithm via `random.sample(population, n)`, which implements Robert Floyd’s algorithm to generate distinct integer subsets in $O(n)$ time without replacement. In R, `sample(N, n, replace = FALSE)` utilizes an optimized reservoir sampling scheme.

To verify that an empirical sampling program satisfies the theoretical requirements of SRSWOR, methodologists execute the following computational diagnostics:
1. **First-Order Inclusion Frequency Test**: Run the selection algorithm across $M = 100,000$ independent simulated draws. Count the empirical inclusion frequency $\hat{\pi}_i = \frac{1}{M} \sum_{m=1}^M I_{i}^{(m)}$ for each unit $i \in \{1, \dots, N\}$. Perform a Pearson chi-squared goodness-of-fit test:
   $$\chi^2 = \sum_{i=1}^N \frac{(M \hat{\pi}_i - M \frac{n}{N})^2}{M \frac{n}{N}}$$
   Under the null hypothesis of valid SRSWOR, $\chi^2$ follows a chi-squared distribution with $N - 1$ degrees of freedom. A failure to reject confirms uniform first-order inclusion.
2. **Second-Order Pairwise Independence Test**: Verify that the joint inclusion frequency across all pairs $i \ne j$ conforms to $\pi_{ij} = \frac{n(n-1)}{N(N-1)}$. A non-uniform distribution of pairs reveals subtle hashing collisions or modular arithmetic flaws in the underlying pseudorandom generator.
3. **Variance Shrinkage Diagnostic**: Compare the empirical variance of the sample means across all $M$ simulations against the theoretical value $\frac{1 - f}{n} S^2$. The ratio $V_{emp}(\bar{y}) / [\frac{1 - f}{n} S^2]$ must converge to $1.0$ at rate $O(1/\sqrt{M})$.

While Simple Random Sampling provides pristine mathematical properties, it treats all population units as completely homogeneous. In real-world populations, elements naturally cluster into identifiable subpopulations—such as geographical regions, enterprise size categories, or demographic age brackets—that exhibit substantial heterogeneity. In Unit 3, we extend our theoretical framework to **Stratified Random Sampling**, discovering how partitioning the population into homogeneous strata dramatically reduces sampling variance through optimal allocation.
