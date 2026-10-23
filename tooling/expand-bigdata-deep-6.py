#!/usr/bin/env python3
"""
Deep Expansion Pass 6 for Big Data Methods for Statistics (Book 16) - Units 5 to 8.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 6 applied.")

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
u5_deep6 = r"""
## 5.11 Communication-Compressed Distributed SGD: SignSGD and Error Feedback

When training massive distributed machine learning models across hundreds of GPU compute nodes connected over standard data center networks, parameter synchronization during AllReduce becomes the dominant latency bottleneck: communicating full 32-bit floating-point gradients for $d = 10^9$ weights transfers 4 gigabytes per step.

Jeremy Bernstein et al. (2018) formulated **SignSGD**, compressing gradients to a single bit per coordinate:
$$\mathrm{sign}(\mathbf{g}_t) \in \{-1, +1\}^d$$
Transmitting 1 bit instead of 32 bits slashes network bandwidth requirements by a factor of 32!

### 1. The Majority Vote Consensus Mechanism
In distributed SignSGD with $M$ worker nodes:
1. Each worker node $m$ computes its local mini-batch gradient $\mathbf{g}_{t, m}$ and evaluates its sign:
$$\mathbf{s}_{t, m} = \mathrm{sign}(\mathbf{g}_{t, m})$$
2. Workers transmit their binary signs to the master aggregator, which performs an element-wise **Majority Vote**:
$$\tilde{\mathbf{s}}_t = \mathrm{sign}\left( \sum_{m=1}^M \mathbf{s}_{t, m} \right)$$
3. The parameter updates along the majority sign vector:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \tilde{\mathbf{s}}_t$$

### 2. Error Feedback Mechanisms
Naive gradient quantization can suffer from catastrophic drift if small, informative gradients are repeatedly rounded to zero.
Sai Praneeth Karimireddy et al. (2019) introduced **Error Feedback (EF-SGD)**: each worker maintains an internal local error buffer $\mathbf{e}_t \in \mathbb{R}^d$:
$$\mathbf{p}_t = \mathbf{e}_{t-1} + \eta \mathbf{g}_t$$
$$\boldsymbol{\Delta}_t = \mathcal{Q}(\mathbf{p}_t)$$
$$\mathbf{e}_t = \mathbf{p}_t - \boldsymbol{\Delta}_t$$
where $\mathcal{Q}(\cdot)$ is the quantization operator. Unquantized residual errors are saved locally and added back into the next iteration. Error feedback provably restores the optimal asymptotic convergence rate of uncompressed SGD, enabling distributed training at multi-gigabit speeds.

## 5.12 Unit 5 Review and Methodological Synthesis

In Unit 5, we developed first-order stochastic optimization theory for massive datasets. We derived the Robbins-Monro stochastic gradient descent update rule, proving that single-sample stochastic gradients $\nabla f_i(\mathbf{w})$ are strictly unbiased estimators of the full population gradient $\nabla F(\mathbf{w})$. We proved that under the Robbins-Monro step size schedule ($\sum \eta_t = \infty, \sum \eta_t^2 < \infty$), SGD converges almost surely at rate $O(1/\sqrt{t})$ for general convex losses and $O(1/t)$ for strongly convex functions. We analyzed Mini-Batch SGD, showing that batch size $B$ scales hardware vectorization while reducing gradient variance by $1/B$. We studied accelerated optimizers: Polyak momentum, Nesterov accelerated gradient (proving the optimal $O(1/t^2)$ rate and Su-Boyd-Candès continuous ODE limit), AdaGrad, RMSprop, and Adam with bias correction. We developed variance-reduced stochastic optimization via SVRG and SAGA, proving linear convergence rates $O(\rho^k)$ without step size decay. Finally, we analyzed Hogwild! lock-free asynchronous optimization, Amari's natural gradient descent with K-FAC, and communication-compressed SignSGD with error feedback.
"""

# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
u6_deep6 = r"""
## 6.10 Column Subset Selection and CUR Matrix Decompositions

In Unit 2, we showed that the Singular Value Decomposition (SVD) $\mathbf{A} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$ provides the theoretically optimal rank-$k$ low-rank approximation in Frobenius and spectral norms (the Eckart-Young-Mirsky Theorem).
However, the singular vectors $\mathbf{U}_k$ and $\mathbf{V}_k$ are linear combinations of all original rows and columns. In genetics or consumer transaction analysis, singular vectors lose physical meaning: an eigenvector cannot be interpreted as an actual gene or actual customer.

The **Column Subset Selection Problem (CSSP)** and the **CUR Matrix Decomposition** resolve this by decomposing a matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ directly using actual, observable columns and rows:

$$\mathbf{A} \approx \mathbf{C} \mathbf{U} \mathbf{R}$$
where:
1. $\mathbf{C} \in \mathbb{R}^{m \times c}$ consists of $c$ actual columns sampled from $\mathbf{A}$.
2. $\mathbf{R} \in \mathbb{R}^{r \times n}$ consists of $r$ actual rows sampled from $\mathbf{A}$.
3. $\mathbf{U} \in \mathbb{R}^{c \times r}$ is a small link matrix computed via Moore-Penrose pseudoinversion: $\mathbf{U} = \mathbf{C}^\dagger \mathbf{A} \mathbf{R}^\dagger$.

### Statistical Leverage Score Sampling for CUR
Petros Drineas, Michael W. Mahoney, and S. Muthukrishnan (2006, 2008) proved that if columns and rows are sampled with probabilities proportional to their statistical leverage scores:
$$p_j = \frac{\|\mathbf{v}_{k, j}\|_2^2}{k}, \quad q_i = \frac{\|\mathbf{u}_{k, i}\|_2^2}{k}$$
then for $c = O(k \ln k / \epsilon^2)$ and $r = O(k \ln k / \epsilon^2)$, the CUR approximation satisfies the relative-error guarantee:

$$\|\mathbf{A} - \mathbf{C} \mathbf{U} \mathbf{R}\|_F \le (1 + \epsilon) \|\mathbf{A} - \mathbf{A}_k\|_F$$
with high probability. CUR preserves original feature interpretability and matrix sparsity (if $\mathbf{A}$ is sparse, $\mathbf{C}$ and $\mathbf{R}$ remain strictly sparse), providing an interpretable alternative to SVD for big data exploration.

## 6.11 Unit 6 Review and Methodological Synthesis

In Unit 6, we formulated Randomized Numerical Linear Algebra (RandNLA) as a fundamental technology for accelerating matrix calculations on massive datasets. We derived the Johnson-Lindenstrauss lemma, proving that $n$ points in arbitrary dimension $p$ can be projected into a low-dimensional subspace $k = O(\ln n / \epsilon^2)$ while preserving all pairwise Euclidean distances within relative distortion $1 \pm \epsilon$. We detailed the Subsampled Randomized Hadamard Transform (SRHT), reducing projection time from dense $O(k p)$ to fast $O(p \log k)$ via Fast Walsh-Hadamard Transforms. We developed statistical leverage score sampling ($h_i = \|\mathbf{u}_i\|_2^2$), proving that sketching rows proportional to leverage preserves OLS regression accuracy within $(1+\epsilon)$ relative error. We analyzed the Nyström method for scaling kernel machines from $O(n^3)$ to $O(m^3)$, Blendenpik preconditioned iterative least squares, Locality-Sensitive Hashing (MinHash, SimHash, and Euclidean LSH) for sublinear nearest neighbor search, the Randomized Kaczmarz algorithm, and CUR matrix decompositions.
"""

# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
u7_deep6 = r"""
## 7.12 Online Regret Minimization and the Multiplicative Weights Update

In theoretical computer science and online game theory, streaming decision-making is framed as **Online Regret Minimization**.
At each round $t = 1, \dots, T$:
1. The learner chooses a probability distribution $\mathbf{p}_t \in \Delta^{K-1}$ over $K$ available actions or statistical expert models.
2. The environment reveals a loss vector $\boldsymbol{\ell}_t \in [0, 1]^K$.
3. The learner incurs expected loss $\langle \mathbf{p}_t, \boldsymbol{\ell}_t \rangle$.

The **Regret** of the learner compared to the best static action in hindsight is:
$$\mathrm{Regret}_T = \sum_{t=1}^T \langle \mathbf{p}_t, \boldsymbol{\ell}_t \rangle - \min_{k=1,\dots,K} \sum_{t=1}^T \ell_{t, k}$$
An algorithm is defined to be **No-Regret** if its average regret vanishes asymptotically: $\lim_{T \to \infty} \frac{\mathrm{Regret}_T}{T} \le 0$.

### The Multiplicative Weights Update (MWU) / Hedge Algorithm
Yoav Freund and Robert Schapire (1997) formulated the **Hedge Algorithm**:
Maintain action weights $w_{t, k}$, initialized to $w_{1, k} = 1$.
At step $t$:
$$p_{t, k} = \frac{w_{t, k}}{\sum_{j=1}^K w_{t, j}}$$
After observing loss $\ell_{t, k}$, update weights multiplicatively:
$$w_{t+1, k} = w_{t, k} \cdot e^{-\eta \ell_{t, k}}$$

*Theorem (Hedge Regret Bound)*: Setting learning rate $\eta = \sqrt{\frac{8 \ln K}{T}}$ guarantees that for any sequence of losses (even adversarial non-stationary choices):
$$\mathrm{Regret}_T \le \sqrt{\frac{T \ln K}{2}} \implies \frac{\mathrm{Regret}_T}{T} \le \sqrt{\frac{\ln K}{2T}} \to 0$$
MWU provides the foundational theoretical engine for online portfolio selection, boosting algorithms (AdaBoost), and online convex optimization.

## 7.13 Unit 7 Review and Methodological Synthesis

In Unit 7, we established the mathematical foundations of streaming data architectures and online learning. We analyzed the streaming constraints: unknown stream length $N$, sublinear memory, and single-pass ingestion. We derived Welford's one-pass numerically stable recurrence algorithm for running sample mean and variance. We proved the uniformity of Vitter's Algorithm R for Reservoir Sampling, showing that every item maintains exact selection probability $k/t$ at all times. We formulated the Count-Min Sketch (CMS), proving bounded overestimation $\hat{f}_x \le f_x + \epsilon \|\mathbf{f}\|_1$ with sublinear memory $O(\frac{1}{\epsilon} \ln \frac{1}{\delta})$. We examined HyperLogLog (HLL) for cardinality estimation, showing that harmonic mean aggregation of leading-zero bit registers estimates distinct elements with relative standard error $1.04/\sqrt{m}$ using $O(\log \log n)$ bits. Finally, we studied the Alon-Matias-Szegedy (AMS) sketch for second frequency moments, the $t$-Digest for tail quantiles, FTRL-Proximal for sparse online advertising models, ADWIN for concept drift, Space-Saving for heavy hitters, and the DGIM sliding-window algorithm.
"""

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
u8_deep6 = r"""
## 8.11 The Benjamini-Yekutieli Procedure for Arbitrary Dependence

In Section 8.2, we proved that the standard Benjamini-Hochberg (BH) procedure controls the False Discovery Rate at level $\frac{m_0}{m} q^* \le q^*$ when $p$-values are independent or satisfy Positive Regression Dependency on a Subset (PRDS).
However, in dense time series, complex spatial models, or high-dimensional brain networks with negative feedback loops, test statistics can exhibit arbitrary negative correlations.

Yoav Benjamini and Daniel Yekutieli (2001) established the universal **BY Procedure** for controlling FDR under **arbitrary, unknown dependence structures**.

### The Benjamini-Yekutieli (BY) Step-Up Algorithm
To control FDR at level $q^*$ under arbitrary dependence:
1. Sort the $m$ observed $p$-values: $p_{(1)} \le p_{(2)} \le \dots \le p_{(m)}$.
2. Compute the harmonic correction factor:
$$c(m) = \sum_{i=1}^m \frac{1}{i} \approx \ln m + \gamma + \frac{1}{2m}$$
where $\gamma \approx 0.577215$ is the Euler-Mascheroni constant.
3. Find the largest index $k$ such that:
$$p_{(k)} \le \frac{k}{m \cdot c(m)} q^*$$
4. Reject all hypotheses $H_{(1)}, \dots, H_{(k)}$.

*Theorem (Benjamini-Yekutieli 2001)*: For any dependency structure whatsoever among the $m$ test statistics (including severe negative correlations):
$$\mathrm{FDR} \le \frac{m_0}{m} q^* \le q^*$$
While the factor $c(m) \approx \ln m$ reduces statistical power relative to standard BH (e.g., for $m = 10,000$, $c(m) \approx \ln(10,000) \approx 9.21$, reducing the threshold by roughly a factor of 9), the BY procedure provides an unshakeable mathematical guarantee when dependence structures cannot be verified.

## 8.12 Unit 8 Review and Methodological Synthesis

In Unit 8, we synthesized the statistical theory of high-dimensional multiple testing and False Discovery Rate (FDR) control. We formulated the multiple testing crisis, demonstrating that testing $m = 100,000$ hypotheses at $\alpha = 0.05$ produces 5,000 spurious discoveries under the global null. We analyzed the Family-Wise Error Rate (FWER) and the union-bound Bonferroni correction $\alpha/m$, showing that Bonferroni destroys statistical power in big data science. We formulated the False Discovery Rate of Benjamini and Hochberg ($\mathrm{FDR} = \mathbb{E}[V / \max(R, 1)]$) and proved the validity of the step-up thresholding rule $p_{(k)} \le \frac{k}{m} q^*$. We detailed Storey's positive FDR (pFDR) and $q$-value methodology via estimation of $\pi_0$. We examined Bradley Efron's empirical Bayes Local False Discovery Rate ($\mathrm{lfdr}(z) = \pi_0 f_0(z) / f(z)$) and two-groups mixture model. Finally, we studied the Knockoffs framework of Barber and Candès for exact finite-sample FDR control in high-dimensional regression, post-selection inference via the Polyhedral Lemma, Surrogate Variable Analysis (SVA) for latent confounders, weighted FDR with functional biological priors, and split Conformal Prediction for exact distribution-free predictive intervals.
"""

def main():
    append_to_unit(5, u5_deep6)
    append_to_unit(6, u6_deep6)
    append_to_unit(7, u7_deep6)
    append_to_unit(8, u8_deep6)
    print("Units 5-8 deep pass 6 applied.")

if __name__ == "__main__":
    main()
