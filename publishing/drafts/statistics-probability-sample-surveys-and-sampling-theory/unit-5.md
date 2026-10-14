# Unit 5: Unequal-Probability Designs and PPS Sampling

## Foundations and Rationale for Unequal Probability Selection

In the preceding units, sampling designs selected elements or primary clusters with equal probability. Under simple random sampling, every unit in the target universe possesses an identical inclusion probability $\pi_i = n / N$. In stratified random sampling with proportional allocation, every element within the universe shares an identical unconditional selection probability. While equal probability designs possess intuitive geometric simplicity and yield self-weighting datasets where unweighted sample averages directly estimate population means, they become extraordinarily inefficient when units vary dramatically in physical size, demographic scale, economic turnover, or administrative capacity.

Consider conducting an establishment survey to estimate total industrial manufacturing output in a country. The target population comprises a small handful of massive multinational conglomerate factories employing tens of thousands of workers alongside hundreds of thousands of micro-enterprises and artisan workshops employing one or two persons. If an equal probability simple random sample of $n = 500$ establishments is selected from this population, the probability that any specific mega-factory is included is tiny. If one mega-factory happens to be selected into the sample, its enormous production volume is multiplied by the massive design weight $N / n$, causing the estimated national total to explode. If, by chance, no mega-factories are selected, the national total is severely underestimated. The sampling distribution of the estimator exhibits extreme skewness and astronomical sampling variance.

The foundational breakthrough of unequal probability sampling—pioneered independently by Morris Hansen and William Hurwitz (1943) in the United States and P. C. Mahalanobis (1944) in India—was the recognition that **units should be selected with probabilities proportional to their importance or size**. If an auxiliary measure of size $x_i > 0$ is known for every unit $i$ in the sampling frame (such as baseline employee count, historical revenue, school enrollment, or farm acreage), and if this auxiliary size is approximately proportional to the survey variable $y_i$ ($y_i \approx \beta x_i$), then selecting units with probabilities proportional to $x_i$ transforms the estimation problem. 

Under Probability Proportional to Size (PPS) selection, large units that dominate the population total are sampled with high probabilities (or even with certainty, $\pi_i = 1$), while tiny units are sampled with appropriately smaller probabilities. When an observation $y_i$ is divided by its selection probability $\pi_i$, the ratio $y_i / \pi_i$ becomes approximately constant across all units in the population:
$$\frac{y_i}{\pi_i} \approx \frac{\beta x_i}{c x_i} = \frac{\beta}{c} = \text{constant}$$
Because the sampling variance of an estimator depends on the variability of these ratios across the sampled units, making the ratio nearly invariant drives the sampling variance toward zero. Unequal probability sampling transforms auxiliary information from a passive descriptive tool into an active, variance-crushing sampling mechanism.

---

## Selection Mechanisms for PPS Sampling

To implement probability proportional to size sampling, the survey statistician must translate a vector of positive auxiliary sizes $\mathbf{x} = (x_1, x_2, \dots, x_N)^\top$ into an operational random selection protocol. Let:
$$X = \sum_{i=1}^N x_i$$
denote the total aggregate measure of size in the population. The relative size (or single-draw selection probability) of unit $i$ is defined as:
$$p_i = \frac{x_i}{X} \quad \text{such that} \quad p_i > 0 \quad \text{and} \quad \sum_{i=1}^N p_i = 1$$

Three classical algorithms are deployed to draw samples according to these probabilities:

### 1. The Cumulative Total Method

The cumulative total method, introduced by Hansen and Hurwitz (1943), operates by constructing a sequential partition of the interval $[1, X]$:
1. Compute the cumulative sums of the measures of size:
   $$T_0 = 0, \quad T_i = \sum_{k=1}^i x_k \quad (i = 1, 2, \dots, N)$$
   where $T_N = X$.
2. Associate with unit $i$ the discrete half-open integer interval:
   $$I_i = (T_{i-1}, T_i] = \{T_{i-1} + 1, T_{i-1} + 2, \dots, T_i\}$$
   The length of interval $I_i$ is exactly $T_i - T_{i-1} = x_i$.
3. Draw a random integer $R$ uniformly distributed on the set $\{1, 2, \dots, X\}$.
4. Select unit $i$ if $R \in I_i$, which occurs if and only if $T_{i-1} < R \le T_i$.

The probability of selecting unit $i$ on any single draw is:
$$P(\text{Unit } i \text{ is selected}) = \frac{\text{Length of } I_i}{X} = \frac{x_i}{X} = p_i$$
To select a sample of size $n$ with replacement (PPSWR), the procedure is repeated independently $n$ times.

### 2. Lahiri's Rejection Method

When the population frame contains hundreds of thousands of units, computing and storing the cumulative array $T_i$ can be computationally cumbersome. In 1951, D. B. Lahiri devised an ingenious rejection sampling algorithm that selects units with exact PPS probabilities without ever computing cumulative totals:
1. Determine the maximum measure of size across the population:
   $$M_{max} = \max_{1 \le i \le N} x_i$$
2. Draw a random integer $i$ uniformly from $\{1, 2, \dots, N\}$.
3. Draw an independent random integer $R$ uniformly from $\{1, 2, \dots, M_{max}\}$.
4. If $R \le x_i$, accept unit $i$ into the sample. If $R > x_i$, reject the pair $(i, R)$ and repeat steps 2 and 3 until a candidate is accepted.

To verify that Lahiri's algorithm generates exact PPS selection probabilities, we calculate the conditional probability of selecting unit $i$ given that an acceptance occurs:
$$P(\text{Accept and choose unit } i) = P(\text{Choose index } i) \times P(R \le x_i \mid \text{index } i) = \frac{1}{N} \times \frac{x_i}{M_{max}}$$
The overall probability of an acceptance on any single trial is:
$$P(\text{Acceptance}) = \sum_{k=1}^N \frac{1}{N} \frac{x_k}{M_{max}} = \frac{1}{N M_{max}} \sum_{k=1}^N x_k = \frac{X}{N M_{max}}$$
Applying Bayes' theorem:
$$P(\text{Unit } i \text{ selected} \mid \text{Acceptance}) = \frac{\frac{1}{N} \frac{x_i}{M_{max}}}{\frac{X}{N M_{max}}} = \frac{x_i}{X} = p_i$$
Lahiri's method delivers exact PPS probabilities while requiring only random access to individual $x_i$ values.

### 3. Systematic PPS Sampling (Cumulative Measure Method)

To select a sample of size $n$ **without replacement** across a continuous cumulative size scale, Goodman and Kish (1950) formulated systematic PPS selection:
1. Compute the sampling interval based on the aggregate size:
   $$k = \frac{X}{n}$$
2. Select a single random start $r$ uniformly distributed on the real interval $(0, k]$.
3. Form the sequence of $n$ selection pointers:
   $$R_j = r + (j - 1)k \quad (j = 1, 2, \dots, n)$$
4. Select unit $i$ into the sample if any selection pointer falls within its cumulative interval:
   $$T_{i-1} < R_j \le T_i$$

Under this scheme, the expected number of pointers hitting unit $i$ is:
$$\text{Expected hits} = \frac{\text{Length of } I_i}{k} = \frac{x_i}{X / n} = n \frac{x_i}{X} = n p_i$$

Provided that no individual unit exceeds the interval length ($x_i \le k$, or equivalently $n p_i \le 1$), a unit can be struck by at most one pointer. Under this condition, the design is strictly without replacement, and the first-order inclusion probability is exact:
$$\pi_i = n p_i = n \frac{x_i}{X}$$

Units whose size exceeds the interval ($x_i > k$, meaning $n p_i > 1$) would be selected multiple times. In survey practice, such dominant units are identified prior to sampling, removed from the frame, designated as **certainty units** (or self-representing strata) with $\pi_i = 1$, and enumerated completely. Systematic PPS is then executed on the remaining non-certainty units.

---

## Sampling With Replacement: The Hansen–Hurwitz Estimator

When sampling is conducted with replacement, the draws are mutually independent, which vastly simplifies mathematical derivations. Although sampling with replacement is slightly less efficient than sampling without replacement, the Hansen–Hurwitz estimator serves as the theoretical benchmark for all unequal probability designs.

### Formulation of the Estimator

Let $n$ independent draws be made from the population with selection probabilities $p_i = x_i / X$. Let $y_{(k)}$ and $p_{(k)}$ denote the survey attribute and selection probability of the unit selected on the $k$-th draw ($k = 1, 2, \dots, n$).

For each draw $k$, we define the single-draw estimator of the population total $Y$:
$$\hat{Y}_k = \frac{y_{(k)}}{p_{(k)}}$$

The **Hansen–Hurwitz Estimator** of the population total $Y$ is the arithmetic average of these $n$ independent single-draw estimators:
$$\hat{Y}_{HH} = \frac{1}{n} \sum_{k=1}^n \hat{Y}_k = \frac{1}{n} \sum_{k=1}^n \frac{y_{(k)}}{p_{(k)}}$$

To estimate the population mean per element $\bar{Y} = Y / M_0$ (where $M_0$ is the known total number of elements):
$$\hat{\bar{Y}}_{HH} = \frac{\hat{Y}_{HH}}{M_0} = \frac{1}{n M_0} \sum_{k=1}^n \frac{y_{(k)}}{p_{(k)}}$$

### Proof of Design Unbiasedness

On any single draw $k$, the random variable $\hat{Y}_k$ takes the value $\frac{y_i}{p_i}$ with probability $p_i$ ($i = 1, 2, \dots, N$). The expected value of $\hat{Y}_k$ is:
$$E(\hat{Y}_k) = \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} \right) = \sum_{i=1}^N y_i = Y$$
Therefore, every single-draw estimator is strictly unbiased.

Taking the expectation of the Hansen–Hurwitz estimator:
$$E(\hat{Y}_{HH}) = E\left[ \frac{1}{n} \sum_{k=1}^n \hat{Y}_k \right] = \frac{1}{n} \sum_{k=1}^n E(\hat{Y}_k) = \frac{1}{n} \sum_{k=1}^n Y = Y$$
This proves that the Hansen–Hurwitz estimator is strictly design-unbiased under PPSWR.

### Derivation of the Exact Sampling Variance

Because the $n$ draws are mutually independent, the variance of the average is the variance of a single draw divided by $n$:
$$V(\hat{Y}_{HH}) = V\left( \frac{1}{n} \sum_{k=1}^n \hat{Y}_k \right) = \frac{1}{n^2} \sum_{k=1}^n V(\hat{Y}_k) = \frac{1}{n} V(\hat{Y}_1)$$

The variance of a single draw $\hat{Y}_1$ is:
$$V(\hat{Y}_1) = E[(\hat{Y}_1 - E(\hat{Y}_1))^2] = \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} - Y \right)^2$$

Expanding the square:
$$V(\hat{Y}_1) = \sum_{i=1}^N p_i \left( \frac{y_i^2}{p_i^2} - \frac{2 y_i Y}{p_i} + Y^2 \right) = \sum_{i=1}^N \frac{y_i^2}{p_i} - 2 Y \sum_{i=1}^N y_i + Y^2 \sum_{i=1}^N p_i$$
Since $\sum y_i = Y$ and $\sum p_i = 1$:
$$V(\hat{Y}_1) = \sum_{i=1}^N \frac{y_i^2}{p_i} - 2 Y^2 + Y^2 = \sum_{i=1}^N \frac{y_i^2}{p_i} - Y^2$$

Therefore, the exact variance of the Hansen–Hurwitz estimator is:
$$V(\hat{Y}_{HH}) = \frac{1}{n} \left[ \sum_{i=1}^N \frac{y_i^2}{p_i} - Y^2 \right] = \frac{1}{n} \sum_{i=1}^N p_i \left( \frac{y_i}{p_i} - Y \right)^2$$

### The Pairwise Algebraic Identity
The variance of $\hat{Y}_{HH}$ can also be expressed in a deeply instructive pairwise form:
$$V(\hat{Y}_{HH}) = \frac{1}{2n} \sum_{i=1}^N \sum_{j=1}^N p_i p_j \left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)^2$$

To prove this identity:
$$\frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N p_i p_j \left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)^2 = \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N p_i p_j \left( \frac{y_i^2}{p_i^2} + \frac{y_j^2}{p_j^2} - 2 \frac{y_i y_j}{p_i p_j} \right)$$
$$= \frac{1}{2} \left[ \sum_{j=1}^N p_j \sum_{i=1}^N \frac{y_i^2}{p_i} + \sum_{i=1}^N p_i \sum_{j=1}^N \frac{y_j^2}{p_j} - 2 \sum_{i=1}^N y_i \sum_{j=1}^N y_j \right]$$
Since $\sum p_j = 1$ and $\sum y_i = Y$:
$$= \frac{1}{2} \left[ 1 \cdot \sum_{i=1}^N \frac{y_i^2}{p_i} + 1 \cdot \sum_{j=1}^N \frac{y_j^2}{p_j} - 2 Y^2 \right] = \sum_{i=1}^N \frac{y_i^2}{p_i} - Y^2$$
Dividing by $n$ completes the proof.

This pairwise formulation highlights the governing principle of PPS sampling: the variance depends directly on the differences between the ratios $\frac{y_i}{p_i}$ and $\frac{y_j}{p_j}$. If the survey variable $y$ is strictly proportional to the auxiliary measure $x$ ($y_i \propto x_i \implies y_i / p_i = \text{constant}$), then every difference $\left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)$ is identically zero, and the sampling variance vanishes completely!

### Unbiased Estimation of Variance

In practice, the true population variance $V(\hat{Y}_{HH})$ is unknown. Because the $n$ values $\hat{Y}_k = \frac{y_{(k)}}{p_{(k)}}$ are independent and identically distributed random variables with mean $Y$ and variance $n V(\hat{Y}_{HH})$, the sample variance among them provides an immediate, strictly unbiased estimator of the variance.

Define the sample variance:
$$s_{HH}^2 = \frac{1}{n - 1} \sum_{k=1}^n \left( \frac{y_{(k)}}{p_{(k)}} - \hat{Y}_{HH} \right)^2$$

Because $s_{HH}^2$ is the standard sample variance of $n$ independent observations, classical statistical theory guarantees that:
$$E(s_{HH}^2) = V(\hat{Y}_1) = n V(\hat{Y}_{HH})$$

Therefore, the strictly unbiased estimator of the variance of the Hansen–Hurwitz estimator is:
$$\hat{V}(\hat{Y}_{HH}) = \frac{s_{HH}^2}{n} = \frac{1}{n(n - 1)} \sum_{k=1}^n \left( \frac{y_{(k)}}{p_{(k)}} - \hat{Y}_{HH} \right)^2$$

Notice the profound operational elegance of this result: computing the estimated variance requires no knowledge of population totals or second-order joint inclusion probabilities. It requires only the $n$ observed values and their single-draw selection probabilities $p_{(k)}$.

---

## Sampling Without Replacement: The Horvitz–Thompson Estimator

While sampling with replacement provides mathematical tractability, drawing units with replacement is inherently wasteful because duplicate selections provide zero additional empirical information about the unobserved elements of the finite population. Sampling without replacement is always statistically more efficient.

In 1952, D. G. Horvitz and D. J. Thompson formulated the universal mathematical theory for estimating finite population parameters from any probability design without replacement, regardless of how complex the selection mechanism may be.

### Inclusion Probabilities

In sampling without replacement, an element $i$ can appear at most once in the sample $s$. The probabilistic behavior of the sample is governed by its **inclusion probabilities**:

1. **First-Order Inclusion Probability**:
   $$\pi_i = P(i \in s) = E(I_i)$$
   where $I_i$ is the sample inclusion indicator:
   $$I_i = \begin{cases} 1 & \text{if } i \in s \\ 0 & \text{if } i \notin s \end{cases}$$
   The fundamental design requirement is that $\pi_i > 0$ for all $i \in U$.

2. **Second-Order (Joint) Inclusion Probability**:
   $$\pi_{ij} = P(i \in s \text{ and } j \in s) = E(I_i I_j)$$
   Notice that for $i = j$, $I_i^2 = I_i$, so $\pi_{ii} = \pi_i$.

For any sampling design with a fixed sample size $n$ ($\sum_{i=1}^N I_i = n$), the inclusion probabilities satisfy two strict conservation laws:
$$\sum_{i=1}^N \pi_i = n$$
$$\sum_{j \ne i}^N \pi_{ij} = (n - 1) \pi_i$$
$$\sum_{i=1}^N \sum_{j \ne i}^N \pi_{ij} = n(n - 1)$$

### The Horvitz–Thompson Estimator

The **Horvitz–Thompson (HT) Estimator** of the population total $Y$ is defined as:
$$\hat{Y}_{HT} = \sum_{i \in s} \frac{y_i}{\pi_i} = \sum_{i=1}^N I_i \frac{y_i}{\pi_i}$$

The inverse of the inclusion probability $d_i = \frac{1}{\pi_i}$ is the **design weight** (or expansion factor) of unit $i$. It represents the number of units in the target population represented by sampled unit $i$.

#### Proof of Design Unbiasedness:
Taking the expectation over the randomization distribution:
$$E(\hat{Y}_{HT}) = E\left[ \sum_{i=1}^N I_i \frac{y_i}{\pi_i} \right] = \sum_{i=1}^N E(I_i) \frac{y_i}{\pi_i} = \sum_{i=1}^N \pi_i \frac{y_i}{\pi_i} = \sum_{i=1}^N y_i = Y$$
The Horvitz–Thompson estimator is strictly design-unbiased for any probability design, provided only that all $\pi_i > 0$.

### The Horvitz–Thompson Variance Formula

To derive the variance of $\hat{Y}_{HT}$, we evaluate the covariance between the sample inclusion indicators $I_i$ and $I_j$:
$$\text{Var}(I_i) = E(I_i^2) - [E(I_i)]^2 = \pi_i - \pi_i^2 = \pi_i(1 - \pi_i)$$
$$\text{Cov}(I_i, I_j) = E(I_i I_j) - E(I_i) E(I_j) = \pi_{ij} - \pi_i \pi_j \quad (i \ne j)$$

Expressing the variance of the linear combination:
$$V(\hat{Y}_{HT}) = V\left( \sum_{i=1}^N I_i \frac{y_i}{\pi_i} \right) = \sum_{i=1}^N \frac{y_i^2}{\pi_i^2} \text{Var}(I_i) + \sum_{i=1}^N \sum_{j \ne i}^N \frac{y_i y_j}{\pi_i \pi_j} \text{Cov}(I_i, I_j)$$

Substituting the covariance expressions yields the classical **Horvitz–Thompson Variance Formula**:
$$V(\hat{Y}_{HT}) = \sum_{i=1}^N \frac{1 - \pi_i}{\pi_i} y_i^2 + \sum_{i=1}^N \sum_{j \ne i}^N \frac{\pi_{ij} - \pi_i \pi_j}{\pi_i \pi_j} y_i y_j$$

### The Horvitz–Thompson Sample Variance Estimator

By substituting the unbiased estimators of the indicator products into the variance formula, Horvitz and Thompson derived the sample variance estimator:
$$\hat{V}_{HT}(\hat{Y}_{HT}) = \sum_{i \in s} \frac{1 - \pi_i}{\pi_i^2} y_i^2 + \sum_{i \in s} \sum_{j \in s, j \ne i} \frac{\pi_{ij} - \pi_i \pi_j}{\pi_i \pi_j \pi_{ij}} y_i y_j$$

Because $E\left[ \frac{I_i}{\pi_i} \right] = 1$ and $E\left[ \frac{I_i I_j}{\pi_{ij}} \right] = 1$, it is mathematically guaranteed that:
$$E[\hat{V}_{HT}(\hat{Y}_{HT})] = V(\hat{Y}_{HT})$$

#### The Fatal Flaw of the HT Variance Estimator:
Despite its theoretical unbiasedness, $\hat{V}_{HT}$ suffers from a severe practical pathology: for many empirical samples, $\hat{V}_{HT}$ can evaluate to a **negative number**. A negative variance estimate is completely meaningless and invalidates the construction of confidence intervals. This pathology occurs because when the cross-product terms $\pi_{ij} - \pi_i \pi_j$ are negative (which is common under without-replacement designs where the selection of one unit depresses the joint selection probability of another), a sample containing large positive values $y_i y_j$ can cause the negative double sum to overpower the positive single sum.

---

## The Sen–Yates–Grundy Formulation for Fixed Sample Size Designs

To rescue variance estimation from the negative-variance pathology, A. R. Sen (1953) in India and F. Yates and P. M. Grundy (1953) in the United Kingdom independently discovered an alternative, vastly superior formulation of the variance and its sample estimator, applicable to all sampling designs with a **fixed sample size** $n$.

### The Sen–Yates–Grundy Algebraic Identity

For any design where the sample size is fixed ($\sum_{i=1}^N I_i = n$), we previously established the joint probability identity:
$$\sum_{j \ne i}^N \pi_{ij} = (n - 1) \pi_i$$

Subtracting $\sum_{j \ne i}^N \pi_i \pi_j = \pi_i (n - \pi_i)$ from both sides:
$$\sum_{j \ne i}^N (\pi_{ij} - \pi_i \pi_j) = (n - 1)\pi_i - \pi_i(n - \pi_i) = n\pi_i - \pi_i - n\pi_i + \pi_i^2 = - \pi_i(1 - \pi_i)$$

Therefore, we have the critical relation:
$$\pi_i(1 - \pi_i) = - \sum_{j \ne i}^N (\pi_{ij} - \pi_i \pi_j) = \sum_{j \ne i}^N (\pi_i \pi_j - \pi_{ij})$$

Dividing by $\pi_i^2$:
$$\frac{1 - \pi_i}{\pi_i} = \sum_{j \ne i}^N \frac{\pi_i \pi_j - \pi_{ij}}{\pi_i^2}$$

### Derivation of the SYG Variance Formula

Now substitute this identity into the first term of the Horvitz–Thompson variance:
$$\sum_{i=1}^N \frac{1 - \pi_i}{\pi_i} y_i^2 = \sum_{i=1}^N \sum_{j \ne i}^N (\pi_i \pi_j - \pi_{ij}) \frac{y_i^2}{\pi_i^2}$$

Symmetrizing over all pairs $(i, j)$ with $i \ne j$:
$$\sum_{i=1}^N \frac{1 - \pi_i}{\pi_i} y_i^2 = \frac{1}{2} \sum_{i=1}^N \sum_{j \ne i}^N (\pi_i \pi_j - \pi_{ij}) \left[ \frac{y_i^2}{\pi_i^2} + \frac{y_j^2}{\pi_j^2} \right]$$

Now consider the second term of the Horvitz–Thompson variance:
$$\sum_{i=1}^N \sum_{j \ne i}^N \frac{\pi_{ij} - \pi_i \pi_j}{\pi_i \pi_j} y_i y_j = - \sum_{i=1}^N \sum_{j \ne i}^N (\pi_i \pi_j - \pi_{ij}) \frac{y_i y_j}{\pi_i \pi_j}$$
$$= - \frac{1}{2} \sum_{i=1}^N \sum_{j \ne i}^N (\pi_i \pi_j - \pi_{ij}) \left[ 2 \frac{y_i y_j}{\pi_i \pi_j} \right]$$

Adding the two components together:
$$V(\hat{Y}_{HT}) = \frac{1}{2} \sum_{i=1}^N \sum_{j \ne i}^N (\pi_i \pi_j - \pi_{ij}) \left[ \frac{y_i^2}{\pi_i^2} + \frac{y_j^2}{\pi_j^2} - 2 \frac{y_i y_j}{\pi_i \pi_j} \right]$$

Recognizing the perfect square inside the bracket, we arrive at the celebrated **Sen–Yates–Grundy (SYG) Variance Formula**:
$$V_{SYG}(\hat{Y}_{HT}) = \frac{1}{2} \sum_{i=1}^N \sum_{j \ne i}^N (\pi_i \pi_j - \pi_{ij}) \left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2 = \sum_{i=1}^N \sum_{j > i}^N (\pi_i \pi_j - \pi_{ij}) \left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2$$

### The Sen–Yates–Grundy Sample Variance Estimator

Applying the sample inclusion indicators to the SYG formula yields the sample variance estimator:
$$\hat{V}_{SYG}(\hat{Y}_{HT}) = \frac{1}{2} \sum_{i \in s} \sum_{j \in s, j \ne i} \frac{\pi_i \pi_j - \pi_{ij}}{\pi_{ij}} \left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2 = \sum_{i \in s} \sum_{j \in s, j > i} \frac{\pi_i \pi_j - \pi_{ij}}{\pi_{ij}} \left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2$$

#### Mathematical Superiority and Non-Negativity:
1. **Guaranteed Non-Negativity**: The squared difference $\left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2$ is strictly non-negative. Therefore, $\hat{V}_{SYG}$ is **guaranteed to be strictly non-negative** whenever the design satisfies:
   $$\pi_{ij} \le \pi_i \pi_j \quad \text{for all } i \ne j$$
   This condition is satisfied by all well-behaved probability sampling designs without replacement (such as Brewer's, Durbin's, and Sampford's methods).
2. **Zero-Variance Property**: If the survey variable is strictly proportional to size ($y_i \propto \pi_i$), every term $\left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)$ is identically zero. Thus, the sample variance estimator $\hat{V}_{SYG}$ evaluates to exactly zero for every single sample, reflecting the true zero variance of the design. The naive Horvitz–Thompson estimator does not possess this property.

---

## Specific PPSWOR Schemes and Joint Inclusion Probabilities

Executing PPS sampling without replacement for an arbitrary sample size $n$ requires specifying a selection protocol that achieves $\pi_i = n p_i$ while guaranteeing tractable, strictly positive joint inclusion probabilities $\pi_{ij} > 0$. Several landmark methods achieve this:

### 1. Brewer's Method for $n = 2$

For a sample size of $n = 2$, K. R. W. Brewer (1963) designed a protocol that guarantees exact $\pi_i = 2 p_i$:
1. The first unit is drawn with selection probability:
   $$p_i^{(1)} = \frac{p_i (1 - p_i)}{D(1 - 2 p_i)}$$
   where $D = \frac{1}{2} \sum_{k=1}^N \frac{p_k (1 - p_k)}{1 - 2 p_k}$.
2. The second unit is drawn from the remaining $N - 1$ units with probability proportional to its original size:
   $$p_{j|i}^{(2)} = \frac{p_j}{1 - p_i} \quad (j \ne i)$$

Brewer proved that under this two-step selection:
- The first-order inclusion probability is exact: $\pi_i = 2 p_i$.
- The joint inclusion probability is:
  $$\pi_{ij} = \frac{2 p_i p_j}{D} \left( \frac{1 - p_i - p_j}{(1 - 2 p_i)(1 - 2 p_j)} \right)$$
- Furthermore, $\pi_{ij} < \pi_i \pi_j$ holds universally, guaranteeing that the Sen–Yates–Grundy variance estimator is strictly non-negative for every possible sample!

### 2. Durbin's Method for $n = 2$

J. Durbin (1967) proposed an alternative two-draw procedure:
1. The first unit is selected with probability $p_i$.
2. If unit $i$ is selected on the first draw, the second unit $j$ ($j \ne i$) is selected with conditional probability:
   $$p_{j|i} = p_j \left[ \frac{1}{1 - 2 p_i} + \frac{1}{1 - 2 p_j} \right] \left[ 1 + \sum_{k=1}^N \frac{p_k}{1 - 2 p_k} \right]^{-1}$$
Durbin's method produces the exact same joint inclusion probabilities $\pi_{ij}$ as Brewer's method, confirming their underlying structural equivalence.

### 3. Systematic PPS Sampling and Variance Approximations

For general sample sizes $n > 2$, systematic PPS selection (arranging units along the cumulative size line and stepping by interval $k = X/n$) is universally favored in operational fieldwork due to its speed and simplicity. 

However, systematic PPS has an analytical drawback: because the selection uses a single random start, many joint inclusion probabilities $\pi_{ij}$ are identically zero (units separated by non-interval distances can never appear in the same sample). When some $\pi_{ij} = 0$, an unbiased estimator of variance does not exist!

To solve this problem, survey statisticians deploy two robust variance approximations:
1. **The Hartley–Rao Variance Approximation (1962)**:
   Assuming the population list is randomly ordered prior to systematic selection, Hartley and Rao derived the asymptotic variance:
   $$V_{HR}(\hat{Y}_{sys}) \approx \frac{1}{n} \sum_{i=1}^N p_i \left( 1 - \frac{n - 1}{n} \pi_i \right) \left( \frac{y_i}{p_i} - Y \right)^2$$
   which behaves similarly to PPSWR variance reduced by a finite-population-like factor $\left( 1 - \frac{n-1}{n}\pi_i \right)$.

2. **The Successive Difference Replication Estimator**:
   When the sample units are ordered as selected along the systematic path, $s = \{1, 2, \dots, n\}$, local successive differences eliminate linear trends and spatial gradients:
   $$\hat{V}_{diff}(\hat{Y}_{HT}) = \frac{1}{2(n - 1)} \sum_{k=1}^{n-1} \left( \frac{y_{(k+1)}}{\pi_{(k+1)}} - \frac{y_{(k)}}{\pi_{(k)}} \right)^2$$
   This estimator is widely used by national census bureaus and statistical agencies.

---

## Fully worked question 1: Hansen–Hurwitz Estimator Variance Derivation, Pairwise Identity and Relative Efficiency Under PPSWR

**Question.** Consider a small finite population of $N = 4$ commercial printing establishments. The survey variable $y_i$ represents annual paper consumption (in metric tons), and the auxiliary measure of size $x_i$ represents the number of active printing presses:

$$\begin{array}{c|cc}
\text{Establishment } i & \text{Presses } (x_i) & \text{Paper Consumption } (y_i) \\
\hline
1 & 2 & 12 \\
2 & 4 & 26 \\
3 & 6 & 34 \\
4 & 8 & 48 \\
\hline
\text{Total} & X = 20 & Y = 120
\end{array}$$

1. Compute the single-draw selection probabilities $p_i = x_i / X$ and evaluate the ratios $y_i / p_i$ for all 4 units.
2. For a sample of $n = 2$ establishments selected with replacement using PPSWR:
   - Compute the exact variance of the Hansen–Hurwitz estimator $V(\hat{Y}_{HH})$ using the classical total formula.
   - Verify the exact variance using the Sen–Yates pairwise formulation.
3. Compute the exact variance of the sample total under Simple Random Sampling With Replacement (SRSWR) of $n = 2$ units, and calculate the Relative Efficiency of PPSWR compared to SRSWR.

**Solution, step 1: Computing selection probabilities $p_i$ and ratios $y_i / p_i$.**
Given $X = 20$ and $Y = 120$:
- Unit 1: $p_1 = 2 / 20 = 0.10$. Ratio: $y_1 / p_1 = 12 / 0.10 = 120$.
- Unit 2: $p_2 = 4 / 20 = 0.20$. Ratio: $y_2 / p_2 = 26 / 0.20 = 130$.
- Unit 3: $p_3 = 6 / 20 = 0.30$. Ratio: $y_3 / p_3 = 34 / 0.30 = 113.3333$.
- Unit 4: $p_4 = 8 / 20 = 0.40$. Ratio: $y_4 / p_4 = 48 / 0.40 = 120$.

Notice how remarkably tight the ratios $y_i / p_i$ are around the true population total $Y = 120$:
$$\{120, 130, 113.3333, 120\}$$
This stability is the hallmark of a high-quality auxiliary measure.

**Solution, step 2: Computing exact variance $V(\hat{Y}_{HH})$ via classical and pairwise formulas.**

1. **Classical Variance Formula**:
   Recall:
   $$V(\hat{Y}_{HH}) = \frac{1}{n} \left[ \sum_{i=1}^N \frac{y_i^2}{p_i} - Y^2 \right]$$

   Compute $\sum_{i=1}^N \frac{y_i^2}{p_i}$:
   - Unit 1: $\frac{12^2}{0.10} = \frac{144}{0.10} = 1,440$
   - Unit 2: $\frac{26^2}{0.20} = \frac{676}{0.20} = 3,380$
   - Unit 3: $\frac{34^2}{0.30} = \frac{1,156}{0.30} = 3,853.3333$
   - Unit 4: $\frac{48^2}{0.40} = \frac{2,304}{0.40} = 5,760$

   Summing across all 4 units:
   $$\sum_{i=1}^4 \frac{y_i^2}{p_i} = 1,440 + 3,380 + 3,853.3333 + 5,760 = 14,433.3333$$

   Subtracting $Y^2 = 120^2 = 14,400$:
   $$V(\hat{Y}_1) = 14,433.3333 - 14,400 = 33.3333$$

   For $n = 2$:
   $$V(\hat{Y}_{HH}) = \frac{33.3333}{2} = 16.6667$$
   The standard error is $\text{SE}(\hat{Y}_{HH}) = \sqrt{16.6667} \approx 4.0825$.

2. **Pairwise Formulation Verification**:
   Recall:
   $$V(\hat{Y}_{HH}) = \frac{1}{n} \sum_{i=1}^N \sum_{j > i}^N p_i p_j \left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)^2$$

   Compute each of the $\binom{4}{2} = 6$ distinct pairs:
   - Pair $(1, 2)$: $p_1 p_2 = 0.10 \times 0.20 = 0.02$. Ratios: $120 - 130 = -10$. Squared: $100$. Term: $0.02 \times 100 = 2.0$.
   - Pair $(1, 3)$: $p_1 p_3 = 0.10 \times 0.30 = 0.03$. Ratios: $120 - 113.3333 = 6.6667$. Squared: $44.4444$. Term: $0.03 \times 44.4444 = 1.3333$.
   - Pair $(1, 4)$: $p_1 p_4 = 0.10 \times 0.40 = 0.04$. Ratios: $120 - 120 = 0$. Term: $0$.
   - Pair $(2, 3)$: $p_2 p_3 = 0.20 \times 0.30 = 0.06$. Ratios: $130 - 113.3333 = 16.6667$. Squared: $277.7778$. Term: $0.06 \times 277.7778 = 16.6667$.
   - Pair $(2, 4)$: $p_2 p_4 = 0.20 \times 0.40 = 0.08$. Ratios: $130 - 120 = 10$. Squared: $100$. Term: $0.08 \times 100 = 8.0$.
   - Pair $(3, 4)$: $p_3 p_4 = 0.30 \times 0.40 = 0.12$. Ratios: $113.3333 - 120 = -6.6667$. Squared: $44.4444$. Term: $0.12 \times 44.4444 = 5.3333$.

   Summing all pairs:
   $$\sum_{i=1}^4 \sum_{j > i}^4 p_i p_j \left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)^2 = 2.0 + 1.3333 + 0 + 16.6667 + 8.0 + 5.3333 = 33.3333$$
   Dividing by $n = 2$:
   $$V(\hat{Y}_{HH}) = \frac{33.3333}{2} = 16.6667$$
   The two formulas agree to the exact decimal, validating the algebraic identity.

**Solution, step 3: Comparison with Simple Random Sampling With Replacement (SRSWR).**
Under SRSWR, each unit is drawn with equal probability $1/N = 1/4 = 0.25$.
The estimator of the population total is:
$$\hat{Y}_{srs} = \frac{N}{n} \sum_{k=1}^n y_{(k)}$$
The variance under SRSWR is:
$$V(\hat{Y}_{srs}) = \frac{N^2}{n} \sigma^2$$
where $\sigma^2 = \frac{1}{N} \sum_{i=1}^N (y_i - \bar{Y})^2$.

The population mean is $\bar{Y} = 120 / 4 = 30$.
Compute deviations and variance:
- Unit 1: $(12 - 30)^2 = (-18)^2 = 324$
- Unit 2: $(26 - 30)^2 = (-4)^2 = 16$
- Unit 3: $(34 - 30)^2 = 4^2 = 16$
- Unit 4: $(48 - 30)^2 = 18^2 = 324$
Sum of squared deviations: $324 + 16 + 16 + 324 = 680$.
$$\sigma^2 = \frac{680}{4} = 170$$

Now compute the variance of $\hat{Y}_{srs}$ for $n = 2$:
$$V(\hat{Y}_{srs}) = \frac{4^2}{2} \times 170 = \frac{16}{2} \times 170 = 8 \times 170 = 1,360$$
The standard error is $\text{SE}(\hat{Y}_{srs}) = \sqrt{1,360} \approx 36.878$.

Now compute the **Relative Efficiency**:
$$\text{RE} = \frac{V(\hat{Y}_{srs})}{V(\hat{Y}_{HH})} = \frac{1,360}{16.6667} = 81.6$$
Sampling with probability proportional to size is **81.6 times more efficient** than simple random sampling! By leveraging the auxiliary press count, PPSWR reduces the sampling variance by an astonishing $98.8\%$.

---

## Fully worked question 2: Calculating Joint Inclusion Probabilities and Sen–Yates–Grundy Variance Under a Two-Draw PPSWOR Scheme

**Question.** Consider a finite population of $N = 3$ regional referral hospitals. The survey variable $y_i$ represents the monthly count of specialized surgical procedures performed, and the auxiliary measure of size $x_i$ represents the total bed capacity:

$$\begin{array}{c|cc}
\text{Hospital } i & \text{Beds } (x_i) & \text{Surgeries } (y_i) \\
\hline
1 & 100 & 40 \\
2 & 200 & 90 \\
3 & 300 & 150 \\
\hline
\text{Total} & X = 600 & Y = 280
\end{array}$$

A sample of $n = 2$ hospitals is drawn **without replacement** using the following sequential selection protocol:
- Draw 1: Select hospital $i$ with probability proportional to size: $p_i = x_i / X$.
- Draw 2: Select hospital $j$ from the remaining 2 hospitals with probability proportional to its size among the remaining units: $p_{j|i} = \frac{x_j}{X - x_i}$.

1. Derive the theoretical formulas for the first-order inclusion probabilities $\pi_i$ and the second-order joint inclusion probabilities $\pi_{ij}$. Compute their exact numerical values for all hospitals.
2. Verify that the conservation laws $\sum_{i=1}^3 \pi_i = 2$ and $\sum_{j \ne i}^3 \pi_{ij} = \pi_i$ hold exactly.
3. Compute the exact theoretical variance of the Horvitz–Thompson estimator using both the Horvitz–Thompson formula and the Sen–Yates–Grundy formula. Verify that $\pi_{ij} \le \pi_i \pi_j$ holds for all pairs, confirming non-negativity.

**Solution, step 1: Deriving and computing $\pi_i$ and $\pi_{ij}$.**
Given $X = 600$:
$$p_1 = \frac{100}{600} = \frac{1}{6}, \quad p_2 = \frac{200}{600} = \frac{1}{3} = \frac{2}{6}, \quad p_3 = \frac{300}{600} = \frac{1}{2} = \frac{3}{6}$$

Hospital $i$ and hospital $j$ can be selected in either order: $(i \text{ then } j)$ or $(j \text{ then } i)$.
The joint selection probability is:
$$\pi_{ij} = P(i \text{ 1st}, j \text{ 2nd}) + P(j \text{ 1st}, i \text{ 2nd}) = p_i \frac{p_j}{1 - p_i} + p_j \frac{p_i}{1 - p_j} = p_i p_j \left[ \frac{1}{1 - p_i} + \frac{1}{1 - p_j} \right]$$

Now compute each pair:
1. **Pair $(1, 2)$**:
   $$p_1 p_2 = \frac{1}{6} \times \frac{2}{6} = \frac{2}{36} = \frac{1}{18}$$
   $$\frac{1}{1 - p_1} + \frac{1}{1 - p_2} = \frac{1}{5/6} + \frac{1}{4/6} = \frac{6}{5} + \frac{6}{4} = \frac{6}{5} + \frac{3}{2} = \frac{12 + 15}{10} = \frac{27}{10}$$
   $$\pi_{12} = \frac{1}{18} \times \frac{27}{10} = \frac{27}{180} = \frac{3}{20} = 0.1500$$

2. **Pair $(1, 3)$**:
   $$p_1 p_3 = \frac{1}{6} \times \frac{3}{6} = \frac{3}{36} = \frac{1}{12}$$
   $$\frac{1}{1 - p_1} + \frac{1}{1 - p_3} = \frac{6}{5} + \frac{1}{1/2} = \frac{6}{5} + 2 = \frac{16}{5}$$
   $$\pi_{13} = \frac{1}{12} \times \frac{16}{5} = \frac{16}{60} = \frac{4}{15} \approx 0.2667$$

3. **Pair $(2, 3)$**:
   $$p_2 p_3 = \frac{2}{6} \times \frac{3}{6} = \frac{6}{36} = \frac{1}{6}$$
   $$\frac{1}{1 - p_2} + \frac{1}{1 - p_3} = \frac{6}{4} + 2 = \frac{3}{2} + 2 = \frac{7}{2}$$
   $$\pi_{23} = \frac{1}{6} \times \frac{7}{2} = \frac{7}{12} \approx 0.5833$$

Now compute the first-order inclusion probabilities $\pi_i = \sum_{j \ne i} \pi_{ij}$ (since $n = 2$):
- Unit 1: $\pi_1 = \pi_{12} + \pi_{13} = \frac{3}{20} + \frac{4}{15} = \frac{9 + 16}{60} = \frac{25}{60} = \frac{5}{12} \approx 0.4167$
- Unit 2: $\pi_2 = \pi_{12} + \pi_{23} = \frac{3}{20} + \frac{7}{12} = \frac{9 + 35}{60} = \frac{44}{60} = \frac{11}{15} \approx 0.7333$
- Unit 3: $\pi_3 = \pi_{13} + \pi_{23} = \frac{4}{15} + \frac{7}{12} = \frac{16 + 35}{60} = \frac{51}{60} = \frac{17}{20} = 0.8500$

**Solution, step 2: Verifying conservation laws and non-negativity conditions.**
1. **Sum of inclusion probabilities**:
   $$\sum_{i=1}^3 \pi_i = \frac{25}{60} + \frac{44}{60} + \frac{51}{60} = \frac{120}{60} = 2.000$$
   This matches the sample size $n = 2$ exactly.

2. **Checking the condition $\pi_{ij} \le \pi_i \pi_j$**:
   - Pair $(1, 2)$:
     $$\pi_1 \pi_2 = \frac{25}{60} \times \frac{44}{60} = \frac{1,100}{3,600} = \frac{11}{36} \approx 0.3056$$
     $$\pi_{12} = \frac{3}{20} = \frac{15}{100} = 0.1500$$
     $$\pi_1 \pi_2 - \pi_{12} = \frac{11}{36} - \frac{3}{20} = \frac{55 - 27}{180} = \frac{28}{180} = \frac{7}{45} \approx 0.1556 > 0$$

   - Pair $(1, 3)$:
     $$\pi_1 \pi_3 = \frac{25}{60} \times \frac{51}{60} = \frac{1,275}{3,600} = \frac{17}{48} \approx 0.3542$$
     $$\pi_{13} = \frac{4}{15} = \frac{16}{60} \approx 0.2667$$
     $$\pi_1 \pi_3 - \pi_{13} = \frac{17}{48} - \frac{4}{15} = \frac{85 - 64}{240} = \frac{21}{240} = \frac{7}{80} \approx 0.0875 > 0$$

   - Pair $(2, 3)$:
     $$\pi_2 \pi_3 = \frac{44}{60} \times \frac{51}{60} = \frac{2,244}{3,600} = \frac{187}{300} \approx 0.6233$$
     $$\pi_{23} = \frac{7}{12} = \frac{175}{300} \approx 0.5833$$
     $$\pi_2 \pi_3 - \pi_{23} = \frac{187 - 175}{300} = \frac{12}{300} = \frac{1}{25} = 0.0400 > 0$$

All differences $\pi_i \pi_j - \pi_{ij}$ are strictly positive! This guarantees that the Sen–Yates–Grundy variance estimator will yield strictly positive variance estimates for every possible sample drawn.

**Solution, step 3: Computing exact variance using HT and SYG formulations.**
First, compute the weighted ratios $y_i / \pi_i$:
- Unit 1: $\frac{y_1}{\pi_1} = \frac{40}{5/12} = 40 \times \frac{12}{5} = 96.0$
- Unit 2: $\frac{y_2}{\pi_2} = \frac{90}{11/15} = 90 \times \frac{15}{11} = \frac{1,350}{11} \approx 122.7273$
- Unit 3: $\frac{y_3}{\pi_3} = \frac{150}{17/20} = 150 \times \frac{20}{17} = \frac{3,000}{17} \approx 176.4706$

Now evaluate the **Sen–Yates–Grundy Variance**:
$$V_{SYG}(\hat{Y}_{HT}) = \sum_{i < j} (\pi_i \pi_j - \pi_{ij}) \left( \frac{y_i}{\pi_i} - \frac{y_j}{\pi_j} \right)^2$$

Compute each of the 3 pairs:
1. Pair $(1, 2)$:
   $$\frac{y_1}{\pi_1} - \frac{y_2}{\pi_2} = 96 - \frac{1,350}{11} = \frac{1,056 - 1,350}{11} = -\frac{294}{11} \approx -26.7273$$
   Squared: $\left( -\frac{294}{11} \right)^2 = \frac{86,436}{121} \approx 714.3471$
   Term: $\frac{7}{45} \times \frac{86,436}{121} = \frac{605,052}{5,445} \approx 111.1207$

2. Pair $(1, 3)$:
   $$\frac{y_1}{\pi_1} - \frac{y_3}{\pi_3} = 96 - \frac{3,000}{17} = \frac{1,632 - 3,000}{17} = -\frac{1,368}{17} \approx -80.4706$$
   Squared: $\left( -\frac{1,368}{17} \right)^2 = \frac{1,871,424}{289} \approx 6,475.5156$
   Term: $\frac{7}{80} \times \frac{1,871,424}{289} = \frac{13,099,968}{23,120} \approx 566.6076$

3. Pair $(2, 3)$:
   $$\frac{y_2}{\pi_2} - \frac{y_3}{\pi_3} = \frac{1,350}{11} - \frac{3,000}{17} = \frac{22,950 - 33,000}{187} = -\frac{10,050}{187} \approx -53.7433$$
   Squared: $\left( -\frac{10,050}{187} \right)^2 = \frac{101,002,500}{34,969} \approx 2,888.3440$
   Term: $\frac{1}{25} \times 2,888.3440 = 115.5338$

Summing all three pairwise terms:
$$V(\hat{Y}_{HT}) = 111.1207 + 566.6076 + 115.5338 = 793.2621$$
The standard error is:
$$\text{SE}(\hat{Y}_{HT}) = \sqrt{793.2621} \approx 28.165$$

This problem demonstrates the complete numerical execution of joint inclusion probabilities, exact Sen–Yates–Grundy variance computation, and verification of non-negativity.

---

## Fully worked question 3: Systematic PPS Sampling Execution with Certainty Units, Inclusion Weights and Replicate Variance Estimation

**Question.** A state environmental protection agency is conducting an inspection survey of industrial effluent discharge across $N = 6$ chemical manufacturing zones. The target variable $y_i$ is monthly toxic waste generation (in metric tons), and the auxiliary measure of size $x_i$ is registered daily manufacturing capacity (in thousands of liters):

$$\begin{array}{c|cc}
\text{Zone } i & \text{Capacity } (x_i) & \text{Toxic Waste } (y_i) \\
\hline
1 & 50 & 14 \\
2 & 80 & 22 \\
3 & 120 & 35 \\
4 & 250 & 78 \\
5 & 450 & 142 \\
6 & 1,050 & 360 \\
\hline
\text{Total} & X = 2,000 & Y = 651
\end{array}$$

The agency plans to select a total sample size of $n = 4$ zones using systematic PPS sampling.

1. Test for certainty units. If any zone satisfies $\pi_i = n \frac{x_i}{X} \ge 1.0$, isolate it as a certainty unit, adjust the sample size and aggregate measure for the remaining non-certainty frame, and recompute the final inclusion probabilities $\pi_i$ and design weights $w_i = 1 / \pi_i$ for all 6 zones.
2. Given a random start of $r = 140$ drawn on the interval $(0, k]$ for the non-certainty frame, determine the exact sample of non-certainty zones selected using systematic PPS sampling.
3. Compute the Horvitz–Thompson estimate of the total toxic waste $\hat{Y}_{HT}$ from the resulting sample (including the certainty unit), and compute the successive-difference replicate variance estimate $\hat{V}_{diff}(\hat{Y}_{HT})$.

**Solution, step 1: Identifying certainty units and computing inclusion weights.**
We are given:
- Initial total size $X = 2,000$
- Target sample size $n = 4$
- Initial sampling interval: $k_0 = \frac{X}{n} = \frac{2,000}{4} = 500$

Check each zone's initial selection probability $\pi_i^{(0)} = n \frac{x_i}{X} = \frac{x_i}{500}$:
- Zone 1: $50 / 500 = 0.10 < 1.0$
- Zone 2: $80 / 500 = 0.16 < 1.0$
- Zone 3: $120 / 500 = 0.24 < 1.0$
- Zone 4: $250 / 500 = 0.50 < 1.0$
- Zone 5: $450 / 500 = 0.90 < 1.0$
- Zone 6: $1,050 / 500 = 2.10 \ge 1.0$

Zone 6 has $\pi_6^{(0)} = 2.10 > 1.0$. If included in the systematic draw, it would be hit more than twice. Therefore, Zone 6 is designated as a **certainty unit (self-representing stratum)**:
$$\pi_6 = 1.000, \quad w_6 = \frac{1}{\pi_6} = 1.000$$

Now re-calibrate the non-certainty frame:
- Number of non-certainty units: $N' = 5$ (Zones 1 through 5)
- Non-certainty sample size: $n' = n - 1 = 4 - 1 = 3$
- Non-certainty aggregate size:
  $$X' = X - x_6 = 2,000 - 1,050 = 950$$
- New sampling interval for the non-certainty frame:
  $$k = \frac{X'}{n'} = \frac{950}{3} = 316.6667$$

Check whether any remaining zone exceeds $k$:
- Max size among Zones 1–5 is $x_5 = 450$. But $450 > 316.6667$, meaning $\pi_5' = \frac{450}{316.6667} = 1.421 \ge 1.0$!
This demonstrates that certainty checking is an **iterative process**. We must also remove Zone 5 as a certainty unit!

Iterate again:
- Designate Zone 5 as a second certainty unit:
  $$\pi_5 = 1.000, \quad w_5 = 1.000$$
- Number of non-certainty units remaining: $N'' = 4$ (Zones 1, 2, 3, 4)
- Remaining sample size: $n'' = n - 2 = 4 - 2 = 2$
- Remaining aggregate size:
  $$X'' = X' - x_5 = 950 - 450 = 500$$
- New sampling interval:
  $$k'' = \frac{X''}{n''} = \frac{500}{2} = 250.000$$

Check remaining zones against $k'' = 250$:
- Zone 1: $x_1 = 50 < 250 \implies \pi_1 = 50 / 250 = 0.20$
- Zone 2: $x_2 = 80 < 250 \implies \pi_2 = 80 / 250 = 0.32$
- Zone 3: $x_3 = 120 < 250 \implies \pi_3 = 120 / 250 = 0.48$
- Zone 4: $x_4 = 250 \le 250 \implies \pi_4 = 250 / 250 = 1.00$

Zone 4 has $x_4 = 250 = k''$, so $\pi_4 = 1.000$. It will be selected with probability 1.0.
Thus, the final inclusion probabilities and design weights across all 6 zones are:

$$\begin{array}{c|cccc}
\text{Zone } i & \text{Capacity } (x_i) & \text{Inclusion Prob } (\pi_i) & \text{Design Weight } (w_i) & \text{Status} \\
\hline
1 & 50 & 0.20 & 5.000 & \text{Sampled with prob 0.20} \\
2 & 80 & 0.32 & 3.125 & \text{Sampled with prob 0.32} \\
3 & 120 & 0.48 & 2.0833 & \text{Sampled with prob 0.48} \\
4 & 250 & 1.00 & 1.000 & \text{Certainty / Interval boundary} \\
5 & 450 & 1.00 & 1.000 & \text{Certainty unit} \\
6 & 1,050 & 1.00 & 1.000 & \text{Certainty unit} \\
\hline
\text{Total} & 2,000 & \sum \pi_i = 4.00 & & n = 4
\end{array}$$

Notice that the sum of inclusion probabilities is:
$$\sum_{i=1}^6 \pi_i = 0.20 + 0.32 + 0.48 + 1.00 + 1.00 + 1.00 = 4.00 = n$$
This confirms that the design strictly satisfies the sample size requirement.

**Solution, step 2: Systematic selection of the non-certainty units.**
The non-certainty sub-universe comprises Zones 1, 2, 3, and 4 with aggregate size $X'' = 500$ and $n'' = 2$ draws, with interval $k'' = 250$.
Construct the cumulative size intervals:
- Zone 1 ($x_1 = 50$): Interval $I_1 = (0, 50]$
- Zone 2 ($x_2 = 80$): Interval $I_2 = (50, 130]$
- Zone 3 ($x_3 = 120$): Interval $I_3 = (130, 250]$
- Zone 4 ($x_4 = 250$): Interval $I_4 = (250, 500]$

We are given a random start $r = 140$ drawn uniformly on $(0, 250]$.
The $n'' = 2$ selection pointers are:
- Pointer 1: $R_1 = r = 140$
  Since $130 < 140 \le 250$, Pointer 1 falls in $I_3 \implies$ **Zone 3 is selected**.
- Pointer 2: $R_2 = r + k'' = 140 + 250 = 390$
  Since $250 < 390 \le 500$, Pointer 2 falls in $I_4 \implies$ **Zone 4 is selected**.

Thus, the final selected sample of $n = 4$ zones comprises:
- Zone 3 (non-certainty, selected by systematic pointer)
- Zone 4 (selected by systematic pointer)
- Zone 5 (certainty unit)
- Zone 6 (certainty unit)

**Solution, step 3: Computing the estimated total and replicate variance.**
The complete observed sample is $s = \{3, 4, 5, 6\}$.
Their attributes, inclusion probabilities, and design weights are:
- Zone 3: $y_3 = 35$, $\pi_3 = 0.48$, $w_3 = \frac{1}{0.48} = 2.083333$. Weighted: $w_3 y_3 = 2.083333 \times 35 = 72.9167$
- Zone 4: $y_4 = 78$, $\pi_4 = 1.00$, $w_4 = 1.000$. Weighted: $w_4 y_4 = 1 \times 78 = 78.000$
- Zone 5: $y_5 = 142$, $\pi_5 = 1.00$, $w_5 = 1.000$. Weighted: $w_5 y_5 = 1 \times 142 = 142.000$
- Zone 6: $y_6 = 360$, $\pi_6 = 1.00$, $w_6 = 1.000$. Weighted: $w_6 y_6 = 1 \times 360 = 360.000$

Compute the estimated total toxic waste $\hat{Y}_{HT}$:
$$\hat{Y}_{HT} = \sum_{i \in s} w_i y_i = 72.9167 + 78.000 + 142.000 + 360.000 = 652.9167 \text{ metric tons}$$
Recall that the true population total is $Y = 651$ tons.
The estimate $\hat{Y}_{HT} = 652.92$ is remarkably close to the true total, with an absolute error of only $1.92$ tons ($0.29\%$).

Now consider the sampling variance:
Because Zones 4, 5, and 6 are enumerated with certainty ($\pi_i = 1$), they contribute **exactly zero sampling variance** to the total! The certainty units are known without sampling error.
The entire sampling variance originates from the stochastic selection among Zones 1, 2, and 3.

For the non-certainty stratum (Zones 1, 2, 3), the stratum total is $Y_{nc} = y_1 + y_2 + y_3 = 14 + 22 + 35 = 71$.
The selection pointer $R_1 = 140$ selected Zone 3 with $w_3 y_3 = 72.9167$.
The other possible outcomes would have been selecting Zone 1 ($w_1 y_1 = 5.0 \times 14 = 70.0$, probability $0.20$) or selecting Zone 2 ($w_2 y_2 = 3.125 \times 22 = 68.75$, probability $0.32$).
The true sampling variance of the non-certainty estimator is:
$$V(\hat{Y}_{nc}) = \sum_{i=1}^3 \pi_i (w_i y_i - Y_{nc})^2$$
$$= 0.20(70.0 - 71)^2 + 0.32(68.75 - 71)^2 + 0.48(72.9167 - 71)^2$$
$$= 0.20(-1)^2 + 0.32(-2.25)^2 + 0.48(1.9167)^2$$
$$= 0.20(1) + 0.32(5.0625) + 0.48(3.6736) = 0.20 + 1.62 + 1.7633 = 3.5833$$

The standard error of the estimated state total is:
$$\text{SE}(\hat{Y}_{HT}) = \sqrt{3.5833} \approx 1.893 \text{ metric tons}$$

This proves the extraordinary power of isolating certainty units and sampling the remainder with PPS: even with an overall sample of only 4 units out of 6, the standard error of the state total is only $1.89$ tons out of $651$ tons—a coefficient of variation of just $0.29\%$!

---

## The Rao–Hartley–Cochran (RHC) Random Group Method for PPS Sampling

While PPS sampling without replacement using the Horvitz–Thompson estimator is statistically efficient, calculating exact second-order joint inclusion probabilities $\pi_{ij}$ for general sample sizes $n > 2$ is computationally intricate. Furthermore, as proven in previous sections, systematic PPS sampling suffers from zero joint inclusion probabilities ($\pi_{ij} = 0$), precluding strictly unbiased variance estimation.

In 1962, J. N. K. Rao, H. O. Hartley, and W. G. Cochran devised an ingenious, universally celebrated sampling procedure—the **Rao–Hartley–Cochran (RHC) Random Group Method**. The RHC method achieves three simultaneous breakthroughs:
1. It selects units **without replacement** with probabilities proportional to size.
2. It yields a variance that is **strictly smaller** than the with-replacement Hansen–Hurwitz variance.
3. It provides a **simple, strictly unbiased variance estimator** that requires zero knowledge of joint inclusion probabilities $\pi_{ij}$!

### The RHC Selection Protocol

Let a finite population $U$ contain $N$ units with auxiliary sizes $x_i > 0$ and total size $X = \sum_{i=1}^N x_i$. Let $p_i = x_i / X$ denote the normalized size of unit $i$ ($\sum p_i = 1$). We wish to draw a sample of $n$ distinct units.

The RHC selection protocol executes in two distinct phases:

#### Phase 1: Random Group Partitioning
The finite population of $N$ units is partitioned at random into $n$ mutually exclusive and collectively exhaustive groups $G_1, G_2, \dots, G_n$ of predetermined sizes $N_1, N_2, \dots, N_n$, such that:
$$\sum_{g=1}^n N_g = N$$
To maximize efficiency, the group sizes $N_g$ should be as equal as possible, such that each $N_g$ is either $\lfloor N/n \rfloor$ or $\lfloor N/n \rfloor + 1$.

#### Phase 2: Independent Intra-Group PPS Selection
For each random group $g \in \{1, 2, \dots, n\}$:
Compute the aggregate group size:
$$X_g = \sum_{i \in G_g} x_i \quad \text{and group probability total} \quad P_g = \sum_{i \in G_g} p_i = \frac{X_g}{X}$$
Select **exactly one unit** from group $G_g$ with probability proportional to its size within that group:
$$P(\text{Unit } i \text{ is selected} \mid i \in G_g) = \frac{p_i}{P_g} = \frac{x_i}{X_g}$$

Because one unit is drawn from each of the $n$ disjoint groups, the resulting sample $s$ contains exactly $n$ distinct units without replacement.

### The Rao–Hartley–Cochran Estimator

Let $(g)$ denote the single unit selected from group $G_g$, with survey measurement $y_{(g)}$, auxiliary size $x_{(g)}$, and normalized size $p_{(g)} = x_{(g)} / X$.

The **Rao–Hartley–Cochran Estimator** of the population total $Y$ is:
$$\hat{Y}_{RHC} = \sum_{g=1}^n \frac{y_{(g)}}{p_{(g)}} P_g = \sum_{g=1}^n \frac{y_{(g)}}{x_{(g)}} X_g$$

### Proof of Strict Design Unbiasedness

We evaluate the expectation using iterated conditional expectation: first conditioning on the random group partition (Phase 1), and subsequently taking expectation over all possible random partitions.

Let $E_2(\cdot \mid G_1, \dots, G_n)$ denote expectation over the Phase 2 selection conditional on fixed groups:
$$E_2\left[ \frac{y_{(g)}}{p_{(g)}} P_g \;\middle|\; G_g \right] = \sum_{i \in G_g} \left( \frac{p_i}{P_g} \right) \left[ \frac{y_i}{p_i} P_g \right] = \sum_{i \in G_g} y_i = Y_g$$
where $Y_g$ is the total of the survey variable in group $G_g$.

Summing across all $n$ groups:
$$E_2(\hat{Y}_{RHC} \mid G_1, \dots, G_n) = \sum_{g=1}^n Y_g = Y$$

Now taking the Phase 1 expectation $E_1$ over all possible random group partitions:
$$E(\hat{Y}_{RHC}) = E_1\left[ E_2(\hat{Y}_{RHC} \mid G_1, \dots, G_n) \right] = E_1(Y) = Y$$
This proves that the RHC estimator is strictly design-unbiased.

### Exact Sampling Variance Derivation

Applying the Law of Total Variance:
$$V(\hat{Y}_{RHC}) = V_1\left( E_2(\hat{Y}_{RHC} \mid G_1, \dots, G_n) \right) + E_1\left( V_2(\hat{Y}_{RHC} \mid G_1, \dots, G_n) \right)$$

Because $E_2(\hat{Y}_{RHC} \mid G_1, \dots, G_n) = Y$ is a constant, the first term vanishes identically:
$$V_1(Y) = 0$$

Therefore, the entire variance is governed by the second term:
$$V(\hat{Y}_{RHC}) = E_1\left( V_2(\hat{Y}_{RHC} \mid G_1, \dots, G_n) \right)$$

Conditional on the groups, the selections within different groups are completely independent. Thus:
$$V_2(\hat{Y}_{RHC} \mid G_1, \dots, G_n) = \sum_{g=1}^n V_2\left( \frac{y_{(g)}}{p_{(g)}} P_g \;\middle|\; G_g \right)$$

For a single group $g$:
$$V_2\left( \frac{y_{(g)}}{p_{(g)}} P_g \;\middle|\; G_g \right) = \sum_{i \in G_g} \frac{p_i}{P_g} \left[ \frac{y_i}{p_i} P_g - Y_g \right]^2 = \sum_{i \in G_g} \frac{y_i^2}{p_i} P_g - Y_g^2$$
Using the pairwise identity within group $G_g$:
$$V_2 = \frac{1}{2} \sum_{i \in G_g} \sum_{j \in G_g} p_i p_j \left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)^2$$

Now take the expectation $E_1$ over all random partitions. Because the partition assigns units to groups completely at random without replacement:
$$P(i \in G_g \text{ and } j \in G_g) = \frac{N_g(N_g - 1)}{N(N - 1)} \quad (i \ne j)$$

Summing across all $n$ groups:
$$\sum_{g=1}^n P(i \in G_g \text{ and } j \in G_g) = \frac{\sum_{g=1}^n N_g(N_g - 1)}{N(N - 1)} = \frac{\sum_{g=1}^n N_g^2 - N}{N(N - 1)}$$

Substituting this expectation into the pairwise variance formula yields the exact **Rao–Hartley–Cochran Variance Formula**:
$$V(\hat{Y}_{RHC}) = \left[ \frac{\sum_{g=1}^n N_g^2 - N}{N(N - 1)} \right] \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N p_i p_j \left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)^2$$

Recall our pairwise formulation for the with-replacement Hansen–Hurwitz variance:
$$V(\hat{Y}_{HH}) = \frac{1}{n} \cdot \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N p_i p_j \left( \frac{y_i}{p_i} - \frac{y_j}{p_j} \right)^2$$

Therefore, the exact relationship connecting RHC variance to Hansen–Hurwitz variance is:
$$V(\hat{Y}_{RHC}) = \left[ \frac{n (\sum_{g=1}^n N_g^2 - N)}{N(N - 1)} \right] V(\hat{Y}_{HH})$$

#### Equal Group Size Simplification:
When $N$ is an exact multiple of $n$, each group has size $N_g = N / n$.
Then:
$$\sum_{g=1}^n N_g^2 = n \left( \frac{N}{n} \right)^2 = \frac{N^2}{n}$$
$$\frac{n (\frac{N^2}{n} - N)}{N(N - 1)} = \frac{N^2 - n N}{N(N - 1)} = \frac{N - n}{N - 1} = 1 - \frac{n - 1}{N - 1}$$

Under equal group sizes, the RHC variance reduces to the remarkably simple expression:
$$V(\hat{Y}_{RHC}) = \left( 1 - \frac{n - 1}{N - 1} \right) V(\hat{Y}_{HH})$$

Notice that because $\frac{n - 1}{N - 1} > 0$ for any sample size $n > 1$:
$$V(\hat{Y}_{RHC}) < V(\hat{Y}_{HH})$$
The Rao–Hartley–Cochran method is **strictly more efficient than sampling with replacement**, capturing a finite-population-like variance reduction of $\left( 1 - \frac{n - 1}{N - 1} \right)$.

### Unbiased Estimation of Variance from Sample Data

The paramount practical virtue of the RHC design is its variance estimator. Rao, Hartley, and Cochran proved that an strictly design-unbiased estimator of $V(\hat{Y}_{RHC})$ is:
$$\hat{V}(\hat{Y}_{RHC}) = \left[ \frac{\sum_{g=1}^n N_g^2 - N}{N^2 - \sum_{g=1}^n N_g^2} \right] \sum_{g=1}^n P_g \left( \frac{y_{(g)}}{p_{(g)}} - \hat{Y}_{RHC} \right)^2$$

For equal group sizes $N_g = N / n$, this simplifies to:
$$\hat{V}(\hat{Y}_{RHC}) = \frac{N - n}{N(n - 1)} \sum_{g=1}^n P_g \left( \frac{y_{(g)}}{p_{(g)}} - \hat{Y}_{RHC} \right)^2$$

This estimator is strictly non-negative for every sample, requires no matrix inversion, and eliminates all joint inclusion probability calculations.

---

## The Midzuno–Sen Scheme and Murthy's Unordered Estimator

Two additional landmark classical PPS schemes provide vital theoretical foundations:

### 1. The Midzuno–Sen Sampling Scheme

In 1952, H. Midzuno in Japan and A. R. Sen (1953) in India independently designed an unequal probability selection scheme that guarantees **strictly positive joint inclusion probabilities** $\pi_{ij} > 0$ for all pairs while achieving exact closed-form inclusion probabilities.

#### Protocol:
1. **Draw 1**: Select the first unit from the population with probability proportional to size:
   $$P(\text{Unit } i \text{ on Draw 1}) = p_i = \frac{x_i}{X}$$
2. **Draws 2 through $n$**: From the remaining $N - 1$ units, select $n - 1$ units with equal probability without replacement (SRSWOR).

#### First-Order Inclusion Probability:
A unit $i$ can be selected either on the first draw or during the subsequent SRSWOR draws:
$$\pi_i = P(\text{1st draw}) + P(\text{Subsequent draws}) = p_i + \sum_{j \ne i}^N p_j \left( \frac{n - 1}{N - 1} \right)$$
Since $\sum_{j \ne i} p_j = 1 - p_i$:
$$\pi_i = p_i + (1 - p_i) \left( \frac{n - 1}{N - 1} \right) = \left( \frac{N - n}{N - 1} \right) p_i + \frac{n - 1}{N - 1}$$

Notice the structure of $\pi_i$: It is a convex linear combination of the PPS probability $p_i$ and the equal-probability fraction $\frac{n - 1}{N - 1}$. 
The second-order joint inclusion probability is:
$$\pi_{ij} = \left( \frac{n - 1}{N - 1} \right) \left[ \frac{N - n}{N - 2}(p_i + p_j) + \frac{n - 2}{N - 2} \right]$$
Because $\pi_{ij} > 0$ for all pairs, strictly unbiased variance estimation under the Horvitz–Thompson and Sen–Yates–Grundy formulas is always guaranteed.

### 2. Murthy's Unordered Estimator

In sequential sampling without replacement (such as Durbin's or Brewer's methods), the units in the sample are drawn in a specific sequential order $(i_1, i_2, \dots, i_n)$. An estimator that depends upon the order of draws is called an **ordered estimator** (e.g., the Des Raj estimator).

In 1957, M. N. Murthy applied the Rao–Blackwell theorem to survey sampling, proving that conditioning an ordered estimator on the **unordered sample set** $s = \{i_1, \dots, i_n\}$ eliminates the arbitrary noise of draw order, strictly reducing sampling variance.

For a sample of size $n = 2$ drawn with initial selection probabilities $p_i$, Murthy's unordered estimator of the population total is:
$$\hat{Y}_M = \frac{1}{2 - p_1 - p_2} \left[ \frac{y_1 (1 - p_2)}{p_1} + \frac{y_2 (1 - p_1)}{p_2} \right]$$

Murthy derived the exact unbiased variance estimator:
$$\hat{V}(\hat{Y}_M) = \frac{(1 - p_1)(1 - p_2)(1 - p_1 - p_2)}{(2 - p_1 - p_2)^2} \left( \frac{y_1}{p_1} - \frac{y_2}{p_2} \right)^2$$
Because all terms in the factor are strictly positive for $p_1 + p_2 < 1$, Murthy's variance estimator is **guaranteed to be strictly non-negative** for every single sample draw, completely immune to the negative-variance pathology.

---

## Practical Synthesis and Self-Weighting Two-Stage Designs

The pinnacle of modern survey design is the integration of PPS sampling into **self-weighting two-stage designs**. This elegant architecture is deployed by virtually all major international household survey programs, including the Demographic and Health Surveys (DHS), the Multiple Indicator Cluster Surveys (MICS), and national living standards surveys.

### The Self-Weighting Architecture

Consider a two-stage national household survey:
- Primary Sampling Units (PSUs) are census enumeration areas containing varying numbers of households $M_i$.
- Secondary Sampling Units (SSUs) are individual households.

If PSUs were selected with equal probability, large enumeration areas would have the same chance of selection as small enumeration areas, requiring complex weighting adjustments at the household level that inflate variance.

Instead, the statistician implements a two-stage design with the following protocol:
1. **Stage 1**: Select $n$ PSUs with **Probability Proportional to Estimated Size (PPS)**:
   $$\pi_i = n \frac{M_i}{M_0}$$
   where $M_0 = \sum_{i=1}^N M_i$ is the total number of households in the country.
2. **Stage 2**: Within each selected PSU $i$, select a **fixed number of households** $m$ (typically $m = 20$ or $25$) using Simple Random Sampling Without Replacement (SRSWOR):
   $$\pi_{j|i} = \frac{m}{M_i}$$

### Proof of the Self-Weighting Property

The unconditional overall inclusion probability for any household $j$ residing in PSU $i$ is:
$$\pi_{ij} = \pi_i \times \pi_{j|i} = \left( n \frac{M_i}{M_0} \right) \times \left( \frac{m}{M_i} \right)$$

Notice what happens algebraically: the cluster size $M_i$ in the numerator of the first stage cancels out identically with the cluster size $M_i$ in the denominator of the second stage!
$$\pi_{ij} = \frac{n m}{M_0} = \text{constant for all } i \text{ and } j$$

The overall design weight for every household in the entire country is:
$$w_{ij} = \frac{1}{\pi_{ij}} = \frac{M_0}{n m} = \text{constant}$$

### Why This Design is Universally Revered:
1. **Self-Weighting Elegance**: Because every household has the exact same design weight, the unweighted sample average $\bar{y} = \frac{1}{nm} \sum \sum y_{ij}$ is a strictly design-unbiased estimator of the national population mean. No design weights are required to compute point estimates.
2. **Equal Fieldwork Workload**: Because exactly $m$ households are interviewed in every selected cluster, field interview teams have an identical, predictable workload in every village or neighborhood, optimizing team travel and logistical planning.
3. **Weight Variance Elimination**: Kish's weight design effect $\text{Deff}_w = 1 + L = 1.00$, meaning zero variance is lost due to unequal weights.

By combining unequal probability selection at the first stage with equal sample takes at the second stage, unequal probability sampling achieves the operational dream: equal probability of selection for ultimate elements coupled with balanced field operations. In the next unit, we examine how auxiliary information can be harnessed not only during sample selection, but post-data-collection through Ratio, Regression, and Calibration Estimation.
