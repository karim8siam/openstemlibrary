#!/usr/bin/env python3
"""
Generate Units 5 to 8 for Big Data Methods for Statistics (Stat H-308).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"
DRAFT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
u5 = r"""# Unit 5: First-Order Stochastic Optimization for Massive Data

In large-scale statistical machine learning and empirical risk minimization, models are trained by optimizing a loss function defined across $n$ training instances:

$$\min_{\mathbf{w} \in \mathbb{R}^d} F(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^n f_i(\mathbf{w})$$
where $f_i(\mathbf{w}) = \ell(h(\mathbf{x}_i; \mathbf{w}), y_i)$ is the convex loss incurred on the $i$-th observation (such as squared error loss in linear regression or cross-entropy loss in logistic regression).

When sample sizes reach $n \ge 10^8$ rows, classical second-order optimization methods (such as Newton-Raphson or Fisher Scoring) are unusable: evaluating the $d \times d$ Hessian matrix $\nabla^2 F(\mathbf{w}) = \frac{1}{n} \sum \nabla^2 f_i(\mathbf{w})$ requires $O(n d^2)$ operations, and inverting it requires $O(d^3)$ time per step. Even standard first-order Batch Gradient Descent (GD), which evaluates the full gradient:
$$\nabla F(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^n \nabla f_i(\mathbf{w})$$
requires $O(n d)$ operations to take a single infinitesimal step, taking hours per iteration. First-order stochastic optimization enables continuous parameter updates in strict $O(d)$ time.

## 5.1 Stochastic Gradient Descent (SGD) and the Robbins-Monro Framework

Herbert Robbins and Sutton Monro (1951) invented stochastic approximation, which was subsequently adapted into **Stochastic Gradient Descent (SGD)**.

### 1. The Stochastic Gradient Update Rule
Instead of calculating the average gradient over all $n$ data points, SGD randomly samples a single index $i_t \in \{1, \dots, n\}$ uniformly at random at iteration $t$, and updates the parameter vector using exclusively the localized gradient of that single point:

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta_t \nabla f_{i_t}(\mathbf{w}_t)$$
where $\eta_t > 0$ is the learning rate (step size).

### 2. Unbiasedness of the Stochastic Gradient
Because the index $i_t$ is sampled uniformly from $\{1, \dots, n\}$:
$$\mathbb{E}_{i_t}[\nabla f_{i_t}(\mathbf{w}_t) \mid \mathbf{w}_t] = \sum_{i=1}^n P(i_t = i) \nabla f_i(\mathbf{w}_t) = \frac{1}{n} \sum_{i=1}^n \nabla f_i(\mathbf{w}_t) = \nabla F(\mathbf{w}_t)$$

The stochastic gradient is an **unbiased estimator** of the true full population gradient. The computational cost per step drops from $O(n d)$ to $O(d)$, independent of the total sample size $n$. In the time Batch Gradient Descent computes one single step, SGD executes $n = 10^8$ updates.

### 3. Convergence Guarantees and Robbins-Monro Step Size Schedule
Because individual stochastic gradients $\nabla f_{i_t}$ contain sampling noise $\mathbf{\xi}_t = \nabla f_{i_t}(\mathbf{w}_t) - \nabla F(\mathbf{w}_t)$ with variance $\mathbb{E}[\|\mathbf{\xi}_t\|_2^2] = \sigma^2 > 0$, fixed step size SGD cannot converge to the exact minimum $\mathbf{w}^*$: the noise causes the trajectory to oscillate in a limit cycle around $\mathbf{w}^*$.

*Theorem (Robbins-Monro Conditions)*: If the step size sequence $\eta_t$ satisfies:
$$\sum_{t=1}^\infty \eta_t = \infty \quad \text{and} \quad \sum_{t=1}^\infty \eta_t^2 < \infty$$
(such as $\eta_t = \eta_0 / t$ or $\eta_0 / \sqrt{t}$), then for any convex $L$-Lipschitz loss function, the iterate sequence converges almost surely to the global minimum:
$$\lim_{t \to \infty} \mathbf{w}_t = \mathbf{w}^* \quad \text{almost surely}$$

Under $\mu$-strong convexity, the convergence rate is $O(1/t)$. For general convex functions, the rate is $O(1/\sqrt{t})$.

## 5.2 Mini-Batch Stochastic Gradient Descent

In practical high-performance computing, updating parameters from a single record ($B = 1$) underutilizes modern GPU and multi-core CPU architectures: vector arithmetic units (AVX-512, CUDA tensor cores) achieve optimal memory bandwidth when processing blocks of data in parallel.

**Mini-Batch SGD** draws a random subset $\mathcal{B}_t \subset \{1, \dots, n\}$ of size $B$ (typically $B \in [32, 2048]$) and updates parameters along the mini-batch average gradient:

$$\mathbf{g}_t = \frac{1}{B} \sum_{i \in \mathcal{B}_t} \nabla f_i(\mathbf{w}_t)$$
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta_t \mathbf{g}_t$$

The variance of the mini-batch gradient estimator decays linearly with batch size:
$$\mathrm{Var}(\mathbf{g}_t) = \frac{\sigma^2}{B}$$
Mini-batching strikes an optimal balance: it achieves an order-of-magnitude reduction in gradient noise variance compared to pure SGD, while executing at near-peak hardware vectorization efficiency.

## 5.3 Accelerated and Adaptive Stochastic Optimizers

While standard SGD converges asymptotically, its progress can be severely hindered by pathological curvature: ravines where the surface curves much more steeply in some directions than others, causing SGD to oscillate erratically across the canyon walls rather than progressing down the valley floor.

### 1. Polyak Momentum
Boris Polyak (1964) introduced the **Heavy-Ball Momentum** method, adding an exponential moving average of past gradients to simulate physical momentum:
$$\mathbf{v}_{t+1} = \beta \mathbf{v}_t + \mathbf{g}_t$$
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \mathbf{v}_{t+1}$$
where $\beta \in [0.9, 0.99]$ is the momentum coefficient. Momentum damps out high-frequency orthogonal oscillations while accelerating velocity along persistent gradient directions.

### 2. The Adam Optimizer (Adaptive Moment Estimation)
Diederik Kingma and Jimmy Ba (2014) combined momentum with adaptive learning rates into **Adam**, the undisputed standard optimizer for deep neural networks and complex statistical loss surfaces.

Adam maintains running exponential moving averages of both the first moment (the mean gradient) and the second uncentered moment (the variance of the gradient):
$$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \mathbf{g}_t$$
$$\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) \mathbf{g}_t^2$$
where $\mathbf{g}_t^2$ denotes the element-wise Hadamard square, with default hyperparameters $\beta_1 = 0.9$ and $\beta_2 = 0.999$.

Because $\mathbf{m}_0 = \mathbf{0}$ and $\mathbf{v}_0 = \mathbf{0}$, the raw vectors are biased toward zero in initial iterations. Adam applies **Bias Correction**:
$$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1 - \beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t}$$
The parameter vector updates element-wise as:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \odot \hat{\mathbf{m}}_t$$
where $\epsilon \approx 10^{-8}$ prevents division by zero. Parameters receiving small or infrequent gradients receive larger relative step sizes, enabling rapid progress across ill-conditioned saddles and plateaus.

## 5.4 Worked Problem Examples

### Fully worked question 1: Variance Decay in Mini-Batch SGD
In training a high-dimensional logistic regression model, single-sample stochastic gradients have variance $\sigma^2 = 80.0$.
1. Compute the gradient variance when using mini-batch sizes of $B = 16, 64,$ and $256$.
2. For an overall computational budget of $N_{\text{eval}} = 102,400$ gradient evaluations, calculate the total number of parameter update steps executed under each batch size.

### Solution, step 1: Calculate Variance for Each Mini-Batch Size
The variance of the mini-batch average gradient $\mathbf{g}_t = \frac{1}{B} \sum_{i=1}^B \nabla f_i$ is:
$$\mathrm{Var}(\mathbf{g}_t) = \frac{\sigma^2}{B}$$
For $\sigma^2 = 80.0$:
- $B = 16$: $\mathrm{Var}(\mathbf{g}) = \frac{80.0}{16} = \mathbf{5.0}$ (a $16$-fold variance reduction).
- $B = 64$: $\mathrm{Var}(\mathbf{g}) = \frac{80.0}{64} = \mathbf{1.25}$ (a $64$-fold variance reduction).
- $B = 256$: $\mathrm{Var}(\mathbf{g}) = \frac{80.0}{256} = \mathbf{0.3125}$ (a $256$-fold variance reduction).

### Solution, step 2: Compute Number of Parameter Updates
The total number of update steps $T$ under a fixed computational budget of $N_{\text{eval}} = 102,400$ is:
$$T = \frac{N_{\text{eval}}}{B}$$
- $B = 16$: $T = \frac{102400}{16} = \mathbf{6,400 \text{ update steps}}$.
- $B = 64$: $T = \frac{102400}{64} = \mathbf{1,600 \text{ update steps}}$.
- $B = 256$: $T = \frac{102400}{256} = \mathbf{400 \text{ update steps}}$.
Practitioners select $B = 64$ or $B = 128$ to achieve strong hardware parallel throughput while retaining thousands of iterative parameter updates.

---

### Fully worked question 2: Adam Optimizer Bias Correction Step
At iteration $t = 2$, an Adam optimizer with standard parameters $\beta_1 = 0.9$ and $\beta_2 = 0.999$ records raw moment vector values $m_2 = 0.38$ and $v_2 = 0.045$.
1. Calculate the bias-correction multipliers for the first and second moments.
2. Compute the bias-corrected values $\hat{m}_2$ and $\hat{v}_2$.
3. Compute the effective parameter update step $\Delta w_2$ for learning rate $\eta = 0.01$ and $\epsilon = 10^{-8}$.

### Solution, step 1: Calculate the Bias-Correction Multipliers
The bias-correction denominators at step $t = 2$ are:
$$1 - \beta_1^t = 1 - 0.9^2 = 1 - 0.81 = 0.19$$
$$1 - \beta_2^t = 1 - 0.999^2 = 1 - 0.998001 = 0.001999$$

### Solution, step 2: Compute Bias-Corrected Moments
Compute $\hat{m}_2$:
$$\hat{m}_2 = \frac{m_2}{1 - \beta_1^2} = \frac{0.38}{0.19} = \mathbf{2.00}$$
Compute $\hat{v}_2$:
$$\hat{v}_2 = \frac{v_2}{1 - \beta_2^2} = \frac{0.045}{0.001999} \approx \mathbf{22.5113}$$
Notice that without bias correction, the raw moments would severely underestimate the true scale of the gradient dynamics by orders of magnitude during initial warmup.

### Solution, step 3: Compute the Effective Parameter Step
The parameter update is:
$$\Delta w = -\frac{\eta}{\sqrt{\hat{v}_2} + \epsilon} \hat{m}_2$$
Compute the denominator:
$$\sqrt{\hat{v}_2} = \sqrt{22.5113} \approx 4.7446$$
Compute the step:
$$\Delta w = -\frac{0.01}{4.7446} \times 2.00 = -0.0021077 \times 2.00 \approx \mathbf{-0.004215}$$
The parameter updates by subtracting $0.004215$.

---

### Fully worked question 3: Theoretical Convergence of Robbins-Monro Step Sizes
Verify whether the step size sequence $\eta_t = \frac{c}{t^\alpha}$ satisfies the Robbins-Monro convergence criteria for $\alpha = 0.50$, $\alpha = 0.75$, and $\alpha = 1.00$.

### Solution, step 1: State the Robbins-Monro Criteria
The two conditions for almost sure convergence are:
1. Condition 1: $\sum_{t=1}^\infty \eta_t = \infty$ (infinite total travel distance).
2. Condition 2: $\sum_{t=1}^\infty \eta_t^2 < \infty$ (finite total squared variance).

### Solution, step 2: Apply the $p$-Series Convergence Test
For a $p$-series $\sum_{t=1}^\infty \frac{1}{t^p}$:
- The series diverges if $p \le 1$.
- The series converges if $p > 1$.

Evaluate each candidate exponent $\alpha$:
1. **Case 1 ($\alpha = 0.50$, $\eta_t = c / t^{1/2}$)**:
   - Condition 1: $\sum \frac{1}{t^{1/2}}$ has $p = 0.5 \le 1 \implies$ **Diverges to $\infty$ (Satisfied)**.
   - Condition 2: $\sum \eta_t^2 = c^2 \sum \frac{1}{t}$ has $p = 1.0 \le 1 \implies$ **Diverges to $\infty$ (Fails Condition 2)**.
   Because Condition 2 fails, gradient noise does not decay fast enough, causing non-vanishing asymptotic variance.
2. **Case 2 ($\alpha = 0.75$, $\eta_t = c / t^{3/4}$)**:
   - Condition 1: $\sum \frac{1}{t^{3/4}}$ has $p = 0.75 \le 1 \implies$ **Diverges to $\infty$ (Satisfied)**.
   - Condition 2: $\sum \eta_t^2 = c^2 \sum \frac{1}{t^{3/2}}$ has $p = 1.5 > 1 \implies$ **Converges (Satisfied)**.
   Both criteria are strictly satisfied! $\alpha = 0.75$ guarantees almost sure convergence.
3. **Case 3 ($\alpha = 1.00$, $\eta_t = c / t$)**:
   - Condition 1: $\sum \frac{1}{t}$ has $p = 1.0 \le 1 \implies$ **Diverges to $\infty$ (Satisfied)**.
   - Condition 2: $\sum \frac{1}{t^2}$ has $p = 2.0 > 1 \implies$ **Converges (Satisfied)**.
   Both criteria are strictly satisfied! $\alpha = 1.00$ is the classical asymptotically optimal schedule.
"""

(DRAFT_DIR / "unit-5.md").write_text(u5.strip() + "\n", encoding="utf-8")
print("Unit 5 generated.")

# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
u6 = r"""# Unit 6: Randomized Numerical Linear Algebra (RandNLA)

In computational statistics, fundamental operations—such as computing least squares regression $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$, evaluating principal components via SVD $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, and matrix multiplication $\mathbf{A} \mathbf{B}$—form the core numerical primitives. When datasets scale to millions of rows and columns, exact deterministic algorithms incur super-linear computational scaling ($O(n p^2)$ or $O(n^3)$) and require storing massive matrices in active memory.

**Randomized Numerical Linear Algebra (RandNLA)**, pioneered by Petros Drineas, Michael W. Mahoney, and Joel A. Tropp, resolves this scalability barrier by deliberately injecting randomness into linear algebra algorithms. By constructing random matrix projections and statistical sampling sketches, RandNLA computes provably accurate matrix approximations with orders-of-magnitude lower computational and memory complexity.

## 6.1 The Johnson-Lindenstrauss Lemma and Dimension Reduction

William B. Johnson and Joram Lindenstrauss (1984) proved a foundational theorem in geometric functional analysis: high-dimensional point sets can be projected onto a logarithmic subspace while preserving all pairwise Euclidean distances.

*Theorem (The Johnson-Lindenstrauss Lemma)*: Let $\mathcal{X} = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ be an arbitrary collection of $n$ points in Euclidean space $\mathbb{R}^p$. For any distortion tolerance $\epsilon \in (0, 1)$, there exists a linear mapping $f: \mathbb{R}^p \to \mathbb{R}^k$ with target dimension:

$$k \ge \frac{4 \ln n}{\epsilon^2 / 2 - \epsilon^3 / 3} = O\left( \frac{\ln n}{\epsilon^2} \right)$$
such that for all pairs $\mathbf{x}_i, \mathbf{x}_j \in \mathcal{X}$, the pairwise Euclidean distances are preserved up to a $(1 \pm \epsilon)$ relative distortion:

$$(1 - \epsilon) \|\mathbf{x}_i - \mathbf{x}_j\|_2^2 \le \|f(\mathbf{x}_i) - f(\mathbf{x}_j)\|_2^2 \le (1 + \epsilon) \|\mathbf{x}_i - \mathbf{x}_j\|_2^2$$

### Profound Practical Implications
1. **Independence of Original Dimension $p$**: The required sketch dimension $k$ depends **strictly on the number of points $n$**, completely independent of the original ambient dimension $p$! Whether $p = 1,000$ or $p = 10,000,000$, $n$ points can be embedded into the same low-dimensional subspace $k \approx 4 \ln n / \epsilon^2$.
2. **Construction via Random Matrices**: Dimitris Achlioptas (2003) proved that the mapping $f(\mathbf{x}) = \frac{1}{\sqrt{k}} \mathbf{\Pi} \mathbf{x}$ is satisfied with high probability when $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ is a random matrix whose entries are independent standard Gaussian variates $\mathcal{N}(0, 1)$, or sparse Rademacher entries:
$$\Pi_{ij} = \begin{cases} +1, & \text{with probability } 0.5 \\ -1, & \text{with probability } 0.5 \end{cases}$$

## 6.2 Fast Random Projections: The Subsampled Randomized Hadamard Transform (SRHT)

While a dense Gaussian projection matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ achieves the Johnson-Lindenstrauss bound, projecting a vector $\mathbf{x} \in \mathbb{R}^p$ requires a dense matrix-vector multiplication $\mathbf{\Pi} \mathbf{x}$, taking $O(k p)$ operations. For large $p$, this projection step itself becomes an expensive computational bottleneck.

Ailon and Chazelle (2009) introduced the **Subsampled Randomized Hadamard Transform (SRHT)**, accelerating the projection time to $O(p \log k)$ using the Fast Walsh-Hadamard Transform (FWHT).

The SRHT matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ is structured as the product of three structured matrices:
$$\mathbf{\Pi} = \sqrt{\frac{p}{k}} \mathbf{R} \mathbf{H}_p \mathbf{D}$$
where:
1. $\mathbf{D} \in \mathbb{R}^{p \times p}$ is a random diagonal Rademacher matrix whose diagonal entries are drawn independently from $\{-1, +1\}$ with equal probability. $\mathbf{D}$ acts as an "equalizer", spreading localized information across all coordinates.
2. $\mathbf{H}_p \in \mathbb{R}^{p \times p}$ is the normalized recursive Walsh-Hadamard matrix:
$$\mathbf{H}_{2k} = \frac{1}{\sqrt{2}} \begin{pmatrix} \mathbf{H}_k & \mathbf{H}_k \\ \mathbf{H}_k & -\mathbf{H}_k \end{pmatrix}, \quad \mathbf{H}_1 = (1)$$
Multiplying by $\mathbf{H}_p$ requires zero floating-point multiplications, executing in $O(p \log p)$ additions and subtractions via FFT-style butterfly networks.
3. $\mathbf{R} \in \mathbb{R}^{k \times p}$ is a uniform subsampling matrix that randomly selects $k$ coordinates out of the $p$ transformed outputs.

The entire projection executes in $O(n p \log k)$ time, providing a near-isometric subspace embedding with minimal computational overhead.

## 6.3 Statistical Leverage Scores and CUR Decompositions

In classical regression diagnostics, the **leverage score** of the $i$-th observation measures its structural distance from the center of the covariate space:
$$h_{ii} = \mathbf{x}_i^T (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{x}_i$$
Let the thin SVD of design matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ (with rank $r$) be $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, where $\mathbf{U} \in \mathbb{R}^{n \times r}$ has orthonormal columns. The leverage score is identically the squared Euclidean norm of the $i$-th row of $\mathbf{U}$:

$$h_i = \|\mathbf{u}_i\|_2^2 = \sum_{j=1}^r U_{ij}^2$$
Notice that $\sum_{i=1}^n h_i = \mathrm{Tr}(\mathbf{U} \mathbf{U}^T) = \mathrm{Tr}(\mathbf{U}^T \mathbf{U}) = \mathrm{Tr}(\mathbf{I}_r) = r$. The normalized values:
$$\pi_i = \frac{h_i}{r} = \frac{\|\mathbf{u}_i\|_2^2}{r}$$
form a valid probability distribution over $\{1, \dots, n\}$.

### Leverage Score Sampling
When sketching a tall-and-skinny matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ ($n \gg p$) to solve least squares $\min \|\mathbf{X} \boldsymbol{\beta} - \mathbf{y}\|_2$, sampling rows uniformly at random fails: influential outlier rows carrying crucial structural signal are omitted, destroying estimation accuracy.

Mahoney and Drineas (2009) proved that sampling rows with probabilities proportional to their leverage scores $\pi_i$:
$$P(\text{select row } i) \propto h_i$$
guarantees that the sketched least squares solution $\tilde{\boldsymbol{\beta}}$ satisfies:
$$\|\mathbf{X} \tilde{\boldsymbol{\beta}} - \mathbf{y}\|_2^2 \le (1 + \epsilon) \|\mathbf{X} \hat{\boldsymbol{\beta}}_{\text{OLS}} - \mathbf{y}\|_2^2$$
with sample size $k = O(p \log p / \epsilon^2)$, achieving near-optimal OLS performance on a sketched sub-sample of size $k \ll n$.

## 6.4 Worked Problem Examples

### Fully worked question 1: Johnson-Lindenstrauss Target Dimension
A social network dataset contains $n = 100,000$ user activity profiles residing in an ambient space of $p = 50,000$ dimensions. A data scientist requires a random projection that preserves all pairwise Euclidean distances within a relative error tolerance of $\epsilon = 0.10$ ($10\%$).
Compute the minimum projection dimension $k$ mandated by the Johnson-Lindenstrauss lemma.

### Solution, step 1: Formulate the JL Target Dimension Bound
The Johnson-Lindenstrauss target dimension $k$ is given by:
$$k \ge \frac{4 \ln n}{\frac{\epsilon^2}{2} - \frac{\epsilon^3}{3}}$$
where $n = 100,000$ and $\epsilon = 0.10$.

### Solution, step 2: Evaluate the Numerator and Denominator
Compute the natural logarithm of $n$:
$$\ln(100,000) \approx 11.512925$$
Numerator:
$$4 \ln n = 4 \times 11.512925 \approx 46.0517$$
Compute the denominator:
$$\frac{\epsilon^2}{2} = \frac{0.10^2}{2} = \frac{0.01}{2} = 0.0050$$
$$\frac{\epsilon^3}{3} = \frac{0.10^3}{3} = \frac{0.001}{3} \approx 0.0003333$$
$$\text{Denominator} = 0.0050 - 0.0003333 = 0.0046667$$

### Solution, step 3: Calculate the Minimum Dimension $k$
Divide numerator by denominator:
$$k \ge \frac{46.0517}{0.0046667} \approx 9868.2 \implies k = \mathbf{9,869}$$
By projecting the $50,000$-dimensional vectors onto a $9,869$-dimensional random subspace, all $\binom{100,000}{2} \approx 5 \times 10^9$ pairwise Euclidean distances are guaranteed to be preserved within $\pm 10\%$ relative error.

---

### Fully worked question 2: Rademacher vs. Gaussian Random Projection Memory
Compare the memory footprint required to store a random projection matrix $\mathbf{\Pi} \in \mathbb{R}^{k \times p}$ with $k = 2000$ and $p = 10,000$:
1. When $\mathbf{\Pi}$ is populated with 64-bit IEEE double-precision Gaussian entries.
2. When $\mathbf{\Pi}$ is populated with 1-bit packed Rademacher entries $\pm 1$.
Determine the memory reduction factor.

### Solution, step 1: Compute Matrix Element Count
The total number of matrix elements is:
$$N_{\text{elements}} = k \times p = 2000 \times 10,000 = 20,000,000 \text{ entries}$$

### Solution, step 2: Calculate Memory Footprint
1. **Gaussian Matrix (Double Precision)**:
Each double-precision float requires 8 bytes (64 bits):
$$\text{Memory}_{\text{Gaussian}} = 20,000,000 \times 8 \text{ bytes} = 160,000,000 \text{ bytes} = \mathbf{160 \text{ MB}}$$
2. **Rademacher Matrix (1-Bit Packed)**:
Because entries are strictly binary $\pm 1$, each entry requires only 1 bit:
$$\text{Memory}_{\text{Rademacher}} = \frac{20,000,000 \text{ bits}}{8 \text{ bits/byte}} = 2,500,000 \text{ bytes} = \mathbf{2.5 \text{ MB}}$$

### Solution, step 3: Determine the Memory Reduction Ratio
$$\text{Reduction Factor} = \frac{160 \text{ MB}}{2.5 \text{ MB}} = \mathbf{64\times}$$
Bit-packed Rademacher sketching reduces memory consumption by a factor of 64, enabling high-dimensional random projections to fit entirely inside L3 processor caches.

---

### Fully worked question 3: Statistical Leverage Score Normalization
A design matrix $\mathbf{X} \in \mathbb{R}^{5 \times 2}$ has left singular vector matrix:
$$\mathbf{U} = \begin{pmatrix} 0.50 & 0.10 \\ 0.20 & -0.40 \\ 0.80 & 0.20 \\ 0.10 & 0.60 \\ 0.245 & -0.648 \end{pmatrix}$$
Verify that $\mathbf{U}$ has rank $r = 2$, compute the statistical leverage score $h_i$ for each of the 5 rows, and calculate the leverage sampling probabilities $\pi_i$.

### Solution, step 1: Verify Column Orthonormality and Rank
Check column norms:
$$\|\mathbf{u}_1\|_2^2 = 0.5^2 + 0.2^2 + 0.8^2 + 0.1^2 + 0.245^2 = 0.25 + 0.04 + 0.64 + 0.01 + 0.060 = 1.00$$
$$\|\mathbf{u}_2\|_2^2 = 0.1^2 + (-0.4)^2 + 0.2^2 + 0.6^2 + (-0.648)^2 = 0.01 + 0.16 + 0.04 + 0.36 + 0.420 = 0.99 \approx 1.00$$
Inner product $\langle \mathbf{u}_1, \mathbf{u}_2 \rangle \approx 0.0$. Thus $r = 2$.

### Solution, step 2: Compute Leverage Scores $h_i = \|\mathbf{u}_i\|_2^2$
Compute row squared norms:
- Row 1: $h_1 = 0.50^2 + 0.10^2 = 0.25 + 0.01 = \mathbf{0.26}$
- Row 2: $h_2 = 0.20^2 + (-0.40)^2 = 0.04 + 0.16 = \mathbf{0.20}$
- Row 3: $h_3 = 0.80^2 + 0.20^2 = 0.64 + 0.04 = \mathbf{0.68}$
- Row 4: $h_4 = 0.10^2 + 0.60^2 = 0.01 + 0.36 = \mathbf{0.37}$
- Row 5: $h_5 = 0.245^2 + (-0.648)^2 \approx 0.060 + 0.420 = \mathbf{0.48}$
Sum of leverage scores:
$$\sum_{i=1}^5 h_i = 0.26 + 0.20 + 0.68 + 0.37 + 0.48 = 1.99 \approx r = 2.00$$

### Solution, step 3: Compute Sampling Probabilities $\pi_i = h_i / r$
Divide each leverage score by $r = 2.0$:
- $\pi_1 = 0.26 / 2 = \mathbf{0.130} \quad (13.0\%)$
- $\pi_2 = 0.20 / 2 = \mathbf{0.100} \quad (10.0\%)$
- $\pi_3 = 0.68 / 2 = \mathbf{0.340} \quad (34.0\%)$
- $\pi_4 = 0.37 / 2 = \mathbf{0.185} \quad (18.5\%)$
- $\pi_5 = 0.48 / 2 = \mathbf{0.240} \quad (24.0\%)$
Row 3 carries the highest statistical leverage ($h_3 = 0.68$), giving it a $34\%$ probability of selection in randomized sketching algorithms.
"""

(DRAFT_DIR / "unit-6.md").write_text(u6.strip() + "\n", encoding="utf-8")
print("Unit 6 generated.")

# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
u7 = r"""# Unit 7: Streaming Data, Online Learning & One-Pass Sketching Algorithms

In high-frequency algorithmic finance, internet backbone network telemetry, internet-of-things (IoT) environmental sensor grids, and social media event processing, data arrive as continuous, unbounded, high-velocity streams. In this **streaming data regime**:
1. The total stream length $N$ is unknown and potentially infinite.
2. The data arrival rate far exceeds the write bandwidth of physical storage; data cannot be persisted to disk.
3. Algorithms are granted strictly **one single pass** over the incoming data stream, with strict sublinear memory $M \ll N$ (typically logarithmic $M = O(\log N)$ or polylogarithmic).

Statisticians must maintain accurate running estimates of summary statistics, quantiles, item frequencies, and cardinality while processing millions of events per second.

## 7.1 Welford's One-Pass Algorithm for Running Mean and Variance

A naive computation of sample variance evaluates:
$$\bar{x} = \frac{1}{N} \sum_{i=1}^N x_i, \quad s^2 = \frac{1}{N-1} \sum_{i=1}^N (x_i - \bar{x})^2$$
This requires two sequential passes over the data (one pass to compute the mean, and a second pass to compute squared deviations), which is impossible in streaming data.

Conversely, the textbook "one-pass" algebraic expansion $s^2 = \frac{1}{N-1} \left( \sum x_i^2 - \frac{(\sum x_i)^2}{N} \right)$ is notoriously vulnerable to **catastrophic floating-point cancellation**: when variance is small relative to the mean ($\sigma / \mu \ll 1$), subtracting two nearly identical large numbers destroys numerical precision, frequently producing negative variance estimates!

B. P. Welford (1962) formulated an exact, numerically stable recurrence relation:

### Welford's Streaming Recurrence
Let $M_k$ denote the running mean and $S_k$ denote the running sum of squared deviations after observing $k$ stream elements:
$$M_k = \bar{x}_k, \quad S_k = \sum_{i=1}^k (x_i - M_k)^2$$

When observation $x_{k+1}$ arrives from the stream:
1. Compute the delta from the previous mean:
$$\delta = x_{k+1} - M_k$$
2. Update the running mean:
$$M_{k+1} = M_k + \frac{\delta}{k + 1}$$
3. Compute the delta from the updated mean:
$$\delta_2 = x_{k+1} - M_{k+1}$$
4. Update the running sum of squares:
$$S_{k+1} = S_k + \delta \cdot \delta_2 = S_k + (x_{k+1} - M_k)(x_{k+1} - M_{k+1})$$

The unbiased sample variance at step $k+1$ is simply:
$$s_{k+1}^2 = \frac{S_{k+1}}{k}$$
Welford's algorithm requires storing only three numbers ($k, M_k, S_k$), executes in $O(1)$ operations per stream arrival, and is immune to numerical cancellation.

## 7.2 Reservoir Sampling: Algorithm R

Suppose a continuous stream of data items $x_1, x_2, \dots$ arrives sequentially, and we wish to maintain a uniform random sample of exactly $k$ items (**a reservoir**) without knowing the total stream length $N$ in advance.

Alan G. Vitter (1985) formalized **Algorithm R (Reservoir Sampling)**:

### Algorithmic Mechanics
1. **Initialization**: Fill the reservoir $R$ with the first $k$ items from the stream: $R = [x_1, x_2, \dots, x_k]$.
2. **Streaming Ingestion**: For each subsequent item $x_t$ arriving at time $t > k$:
   - Generate a random integer $j$ uniformly distributed in $\{1, 2, \dots, t\}$.
   - If $j \le k$, replace the $j$-th element of the reservoir with the new item: $R[j] \leftarrow x_t$.
   - If $j > k$, discard $x_t$.

*Theorem (Uniformity of Reservoir Sampling)*: At any time $t \ge k$, every item $x_i$ observed so far ($1 \le i \le t$) has an exact, equal probability of residing in the reservoir:
$$P(x_i \in R) = \frac{k}{t}$$

*Proof by Induction*:
- Base case: At $t = k$, all $k$ items are placed in the reservoir, so $P(x_i \in R) = k/k = 1.0$.
- Induction step: Assume true for time $t-1$, so $P(x_i \in R_{t-1}) = \frac{k}{t-1}$.
When item $x_t$ arrives:
1. For the new item $x_t$, it enters the reservoir if $j \le k$:
$$P(x_t \in R_t) = \frac{k}{t}$$
2. For an existing item $x_i$ ($i < t$): it survives in the reservoir if it was present at $t-1$ AND was not replaced by $x_t$.
The replacement candidate $j$ is chosen uniformly from $\{1, \dots, t\}$. The probability that item $i$ is replaced is the probability that $x_t$ is accepted ($k/t$) times the probability that slot $j$ was selected ($1/k$):
$$P(\text{item } i \text{ evicted}) = \frac{k}{t} \times \frac{1}{k} = \frac{1}{t}$$
Therefore, the probability of survival is $1 - 1/t = \frac{t-1}{t}$.
By the induction hypothesis:
$$P(x_i \in R_t) = P(x_i \in R_{t-1}) \times P(\text{survives}) = \frac{k}{t-1} \times \frac{t-1}{t} = \frac{k}{t}$$
which completes the proof for all $t \ge k$.

## 7.3 Frequency Estimation: The Count-Min Sketch

Graham Cormode and S. Muthukrishnan (2005) invented the **Count-Min Sketch (CMS)**, a probabilistic data structure that tracks event frequencies in data streams using sublinear memory.

### 1. Data Structure Layout
A Count-Min Sketch consists of a 2D array of counters $C$ of depth $d$ and width $w$:
$$C \in \mathbb{N}^{d \times w}$$
paired with $d$ independent pairwise hash functions $h_1, \dots, h_d: \mathcal{U} \to \{1, \dots, w\}$.

1. **Update Step**: When item $x$ with count $c$ arrives:
   For each row $j \in \{1, \dots, d\}$, increment the hashed counter:
   $$C[j, h_j(x)] \leftarrow C[j, h_j(x)] + c$$
2. **Point Query**: To estimate the frequency $\hat{f}_x$ of item $x$:
   $$\hat{f}_x = \min_{1 \le j \le d} C[j, h_j(x)]$$

### 2. Theoretical Accuracy Guarantees
Because hash collisions can only increase counter values (never decrease them), the Count-Min Sketch satisfies two rigorous guarantees:
1. **No Underestimation**: $\hat{f}_x \ge f_x$ always.
2. **Bounded Overestimation**: For user-specified error tolerance $\epsilon$ and failure probability $\delta$, set:
$$w = \lceil e / \epsilon \rceil, \quad d = \lceil \ln(1 / \delta) \rceil$$
Then with probability at least $1 - \delta$:
$$\hat{f}_x \le f_x + \epsilon \|\mathbf{f}\|_1$$
where $\|\mathbf{f}\|_1 = \sum f_i$ is the total stream volume. CMS tracks heavy hitters in internet traffic using mere kilobytes of memory.

## 7.4 Cardinality Estimation: The HyperLogLog Algorithm

Philippe Flajolet et al. (2007) introduced **HyperLogLog (HLL)**, estimating the number of distinct elements $n$ (cardinality) in a data stream using only $O(\log \log n)$ bits of memory.

HLL hashes stream elements into 64-bit binary strings and observes the number of leading zeros $\rho(h(x))$: observing a binary string beginning with $k$ zeros is an event with probability $2^{-(k+1)}$, implying that roughly $2^{k+1}$ distinct elements have passed through the stream. To suppress variance, HLL partitions the stream into $m = 2^b$ registers using the first $b$ bits of the hash, computes the maximum leading zeros $M_j$ in each register, and aggregates using the **harmonic mean**:

$$\hat{n} = \alpha_m m^2 \left( \sum_{j=1}^m 2^{-M_j} \right)^{-1}$$
where $\alpha_m$ is a bias-correction constant. HLL estimates cardinalities up to $10^9$ unique items with a relative standard error of $\frac{1.04}{\sqrt{m}} \approx 1.04\%$ using only 1.5 kilobytes of memory.

## 7.5 Worked Problem Examples

### Fully worked question 1: Welford Recurrence Trace
A data stream emits the sequential values $x_1 = 12.0, x_2 = 18.0, x_3 = 15.0$.
Trace Welford's streaming algorithm step-by-step to compute the running mean and sample variance after each arrival.

### Solution, step 1: Process Step 1 ($k = 1, x_1 = 12.0$)
- Initial state: $k = 1$.
- Mean: $M_1 = 12.0$.
- Sum of squares: $S_1 = 0.0$.
- Variance: undefined for $k = 1$ ($0/0$).

### Solution, step 2: Process Step 2 ($k = 2, x_2 = 18.0$)
- Delta: $\delta = x_2 - M_1 = 18.0 - 12.0 = 6.0$.
- Mean update: $M_2 = M_1 + \delta / 2 = 12.0 + 6.0 / 2 = \mathbf{15.0}$.
- Delta 2: $\delta_2 = x_2 - M_2 = 18.0 - 15.0 = 3.0$.
- Sum of squares: $S_2 = S_1 + \delta \times \delta_2 = 0.0 + 6.0 \times 3.0 = \mathbf{18.0}$.
- Sample variance:
$$s_2^2 = \frac{S_2}{k - 1} = \frac{18.0}{2 - 1} = \mathbf{18.0}$$

### Solution, step 3: Process Step 3 ($k = 3, x_3 = 15.0$)
- Delta: $\delta = x_3 - M_2 = 15.0 - 15.0 = 0.0$.
- Mean update: $M_3 = M_2 + \delta / 3 = 15.0 + 0.0 = \mathbf{15.0}$.
- Delta 2: $\delta_2 = x_3 - M_3 = 15.0 - 15.0 = 0.0$.
- Sum of squares: $S_3 = S_2 + \delta \times \delta_2 = 18.0 + 0.0 = \mathbf{18.0}$.
- Sample variance:
$$s_3^2 = \frac{S_3}{k - 1} = \frac{18.0}{3 - 1} = \frac{18.0}{2} = \mathbf{9.0}$$
Final running mean is $15.0$ and unbiased sample variance is $9.0$, computed in $O(1)$ memory without re-evaluating past data.

---

### Fully worked question 2: Sizing a Count-Min Sketch
A network security monitoring system monitors IP packet arrivals to detect denial-of-service (DoS) attack sources across a stream of $N = 50,000,000$ packets.
The engineer requires that frequency estimation error be bounded by at most $0.05\%$ of total stream volume ($\epsilon = 0.0005$) with confidence at least $99.9\%$ ($\delta = 0.001$).
Calculate the required width $w$, depth $d$, and total memory consumption assuming 4-byte 32-bit integer counters.

### Solution, step 1: Calculate Required Matrix Dimensions
The Count-Min Sketch parameter sizing formulas are:
$$w = \left\lceil \frac{e}{\epsilon} \right\rceil, \quad d = \left\lceil \ln\left(\frac{1}{\delta}\right) \right\rceil$$
For $\epsilon = 0.0005$ and $\delta = 0.001$:
Compute width $w$:
$$w = \left\lceil \frac{2.71828}{0.0005} \right\rceil = \lceil 5436.56 \rceil = \mathbf{5,437 \text{ columns}}$$
Compute depth $d$:
$$d = \left\lceil \ln\left( \frac{1}{0.001} \right) \right\rceil = \lceil \ln(1000) \rceil = \lceil 6.90775 \rceil = \mathbf{7 \text{ rows}}$$

### Solution, step 2: Compute Total Counter Count and Memory Footprint
Total number of counters in the sketch:
$$N_{\text{counters}} = d \times w = 7 \times 5437 = 38,059 \text{ counters}$$
With 4 bytes per counter:
$$\text{Memory} = 38,059 \times 4 \text{ bytes} = 152,236 \text{ bytes} \approx \mathbf{148.67 \text{ Kilobytes}}$$

### Solution, step 3: Determine the Error Bound Magnitude
The maximum frequency overestimation error with $99.9\%$ probability is:
$$\epsilon N = 0.0005 \times 50,000,000 = \mathbf{25,000 \text{ packets}}$$
Using less than $150$ Kilobytes of memory, the system tracks frequency across 50 million packets to within $\pm 25,000$ packets.

---

### Fully worked question 3: HyperLogLog Relative Standard Error
A database engineer configures a HyperLogLog data structure with $b = 12$ indexing bits ($m = 2^{12} = 4096$ registers).
1. Calculate the theoretical relative standard error of the cardinality estimate.
2. If 6 bits are allocated per register, compute the total memory consumption of the HLL sketch.

### Solution, step 1: Compute the Relative Standard Error
The theoretical relative standard error of the HyperLogLog estimator is:
$$\mathrm{RSE} = \frac{1.04}{\sqrt{m}}$$
For $b = 12$, $m = 2^{12} = 4096$:
$$\sqrt{m} = \sqrt{4096} = 64$$
$$\mathrm{RSE} = \frac{1.04}{64} = 0.01625 = \mathbf{1.625\%}$$
The cardinality estimate has a relative standard error of only $1.625\%$.

### Solution, step 2: Calculate Memory Footprint
With $m = 4096$ registers and 6 bits per register:
$$\text{Total Bits} = 4096 \times 6 = 24,576 \text{ bits}$$
Convert bits to bytes:
$$\text{Memory} = \frac{24,576}{8} = 3,072 \text{ bytes} = \mathbf{3.0 \text{ Kilobytes}}$$
Using just $3.0$ Kilobytes of memory, HyperLogLog estimates cardinalities up to $2^{64} \approx 1.8 \times 10^{19}$ unique items with a $1.625\%$ standard error.
"""

(DRAFT_DIR / "unit-7.md").write_text(u7.strip() + "\n", encoding="utf-8")
print("Unit 7 generated.")

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
u8 = r"""# Unit 8: High-Dimensional Multiple Testing & False Discovery Rate (FDR)

In modern big data analytics—such as genome-wide association studies (GWAS), neuroimaging voxel analysis, and web-scale e-commerce A/B testing—statisticians simultaneously evaluate thousands or millions of statistical hypothesis tests:

$$H_{0, 1}, H_{0, 2}, \dots, H_{0, m}, \quad m \ge 10^5$$

If an analyst evaluates $m = 100,000$ null hypotheses at the classical single-test significance level $\alpha = 0.05$, then even if **all** null hypotheses are strictly true (pure noise), the expected number of spurious false discoveries is:
$$\mathbb{E}[\text{False Positives}] = m \times \alpha = 100,000 \times 0.05 = \mathbf{5,000 \text{ false positives!}}$$
This phenomenon is known as the **Multiple Testing Crisis**. Developing rigorous statistical methodology to separate genuine biological or economic discoveries from high-dimensional noise is paramount.

## 8.1 The Multiple Testing Framework and Family-Wise Error Rate (FWER)

Consider the outcome table of $m$ simultaneous hypothesis tests:

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Hypothesis State</th>
<th>Declared Not Significant (Accept $H_0$)</th>
<th>Declared Significant (Reject $H_0$)</th>
<th>Total Hypotheses</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>True Null ($H_0$ is true)</strong></td>
<td>$U$ (True Negatives)</td>
<td>$V$ (False Positives / Type I Error)</td>
<td>$m_0$</td>
</tr>
<tr>
<td><strong>Non-Null ($H_1$ is true)</strong></td>
<td>$T$ (False Negatives / Type II Error)</td>
<td>$S$ (True Positives / Power)</td>
<td>$m_1$</td>
</tr>
<tr>
<td><strong>Total Declared</strong></td>
<td>$m - R$</td>
<td>$R$ (Total Discoveries)</td>
<td>$m$</td>
</tr>
</tbody>
</table>
</div>

The total number of hypotheses $m$ and total rejected hypotheses $R$ are observed, while $U, V, T, S$ and the number of true nulls $m_0$ are unobservable latent quantities.

### The Family-Wise Error Rate (FWER)
Classical multiple comparison theory controls the **Family-Wise Error Rate (FWER)**: the probability of committing at least one Type I error:

$$\mathrm{FWER} = P(V \ge 1)$$

1. **The Bonferroni Correction**: By Boole's inequality (the union bound):
$$P(V \ge 1) = P\left( \bigcup_{i \in I_0} \{ p_i \le \alpha_{\text{ind}} \} \right) \le \sum_{i \in I_0} P(p_i \le \alpha_{\text{ind}}) = m_0 \alpha_{\text{ind}} \le m \alpha_{\text{ind}}$$
To guarantee $\mathrm{FWER} \le \alpha$, Bonferroni rejects $H_{0, i}$ if:
$$p_i \le \frac{\alpha}{m}$$

*Fatal Limitation of Bonferroni in Big Data*: If $m = 1,000,000$, Bonferroni requires $p \le 0.05 / 10^6 = 5 \times 10^{-8}$. This criterion is paralyzingly conservative: to prevent a single false positive, it sacrifices virtually all statistical power, discarding dozens of genuine scientific discoveries.

## 8.2 The False Discovery Rate (FDR) of Benjamini and Hochberg

Yoav Benjamini and Yosef Hochberg (1995) revolutionized high-dimensional statistics by proposing the **False Discovery Rate (FDR)**:

$$\mathrm{FDR} = \mathbb{E}[Q] = \mathbb{E}\left[ \frac{V}{\max(R, 1)} \right]$$
where $Q = V / R$ is the False Discovery Proportion (FDP) if $R > 0$, and $0$ if $R = 0$.

Rather than requiring that zero false positives occur across the entire study ($P(V \ge 1) \le \alpha$), FDR controls the **expected proportion of false discoveries among all rejected hypotheses**. Tolerating a small, controlled fraction of false discoveries (e.g., $\mathrm{FDR} \le 0.05$, meaning that among 1,000 declared discoveries, roughly 50 are false positives) yields immense statistical power in big data analysis.

### The Benjamini-Hochberg (BH) Step-Up Procedure
To control FDR at level $q^* \in (0, 1)$:
1. Sort the $m$ observed $p$-values in ascending order:
$$p_{(1)} \le p_{(2)} \le \dots \le p_{(m)}$$
2. Find the largest index $k$ such that:
$$p_{(k)} \le \frac{k}{m} q^*$$
3. If such a $k$ exists, reject all null hypotheses corresponding to the $k$ smallest $p$-values:
$$\text{Reject } H_{(1)}, H_{(2)}, \dots, H_{(k)}$$
If no such $k$ exists, reject nothing.

*Theorem (Benjamini-Hochberg 1995)*: If the $p$-values corresponding to the $m_0$ true null hypotheses are independent (or satisfy Positive Regression Dependency on a Subset - PRDS), the BH procedure guarantees:

$$\mathrm{FDR} \le \frac{m_0}{m} q^* \le q^*$$
for any configuration of false null hypotheses.

## 8.3 Storey's Positive FDR (pFDR) and $q$-Values

John D. Storey (2002) noted that when $m_0 < m$, the BH procedure is conservative by a factor of $\pi_0 = m_0 / m$. Storey formulated the **positive False Discovery Rate (pFDR)**:

$$\mathrm{pFDR} = \mathbb{E}\left[ \frac{V}{R} \,\middle|\, R > 0 \right]$$

### Estimating $\pi_0$ (The Proportion of True Nulls)
Because true null $p$-values are uniformly distributed on $[0, 1]$, while alternative $p$-values concentrate near $0$, $p$-values in the upper interval $(\lambda, 1]$ (typically $\lambda = 0.50$) consist almost entirely of true nulls.
Storey's estimator of $\pi_0$ is:
$$\hat{\pi}_0(\lambda) = \frac{\#\{ p_i > \lambda \}}{(1 - \lambda) m}$$
The **$q$-value** of an observed hypothesis is defined as the minimum FDR at which that hypothesis would be declared significant:
$$q(p_{(k)}) = \min_{l \ge k} \left\{ \frac{\hat{\pi}_0 m \cdot p_{(l)}}{l} \right\}$$
$q$-values provide an intuitive Bayesian-like posterior probability metric for high-dimensional discovery reporting.

## 8.4 Empirical Bayes Multiple Testing: Efron's Local False Discovery Rate

Bradley Efron (2004, 2012) developed the **Local False Discovery Rate (lfdr)** using an empirical Bayes two-groups mixture model.

Let test statistics be converted to $z$-scores $z_i = \Phi^{-1}(1 - p_i) \sim f(z)$. The density decomposes as a mixture:
$$f(z) = \pi_0 f_0(z) + (1 - \pi_0) f_1(z)$$
where $f_0(z)$ is the theoretical or empirical null density (often modeled as $\mathcal{N}(\delta, \sigma_0^2)$ to absorb unobserved confounding) and $f_1(z)$ is the non-null alternative density.

By Bayes' rule, the posterior probability that a specific observation with $z$-score $z$ is a true null is:

$$\mathrm{lfdr}(z) = P(H_0 \mid Z = z) = \frac{\pi_0 f_0(z)}{f(z)}$$

Unlike tail-area FDR (which averages over all points more extreme than $z$), the local FDR quantifies the exact posterior probability of false discovery **at the specific point $z$**, providing the modern gold standard for large-scale genetic and proteomic screening.

## 8.5 Worked Problem Examples

### Fully worked question 1: Benjamini-Hochberg Step-Up Thresholding
In a genomic differential expression experiment evaluating $m = 10$ genes, the sorted $p$-values are:
$$p = (0.002, 0.008, 0.015, 0.022, 0.038, 0.045, 0.060, 0.085, 0.120, 0.350)$$
1. Determine which hypotheses are rejected under the Bonferroni correction at $\alpha = 0.05$.
2. Determine which hypotheses are rejected under the Benjamini-Hochberg procedure at FDR $q^* = 0.05$.

### Solution, step 1: Apply the Bonferroni Correction
The Bonferroni single-test critical threshold is:
$$\alpha_{\text{Bonf}} = \frac{\alpha}{m} = \frac{0.05}{10} = \mathbf{0.005}$$
Compare sorted $p$-values to $0.005$:
- $p_{(1)} = 0.002 \le 0.005 \implies$ **Reject $H_{(1)}$**.
- $p_{(2)} = 0.008 > 0.005 \implies$ Fail to reject.
Bonferroni declares **only 1 discovery** ($H_{(1)}$).

### Solution, step 2: Apply the Benjamini-Hochberg Procedure
Compute the critical thresholds $T_k = \frac{k}{m} q^* = \frac{k}{10} \times 0.05 = 0.005 \times k$:
<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Rank ($k$)</th>
<th>$p_{(k)}$</th>
<th>BH Threshold ($\frac{k}{10} \times 0.05$)</th>
<th>Condition ($p_{(k)} \le T_k$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0.002</td>
<td>0.005</td>
<td>True</td>
</tr>
<tr>
<td>2</td>
<td>0.008</td>
<td>0.010</td>
<td>True</td>
</tr>
<tr>
<td>3</td>
<td>0.015</td>
<td>0.015</td>
<td>True ($0.015 \le 0.015$)</td>
</tr>
<tr>
<td>4</td>
<td>0.022</td>
<td>0.020</td>
<td>False ($0.022 > 0.020$)</td>
</tr>
<tr>
<td>5</td>
<td>0.038</td>
<td>0.025</td>
<td>False</td>
</tr>
<tr>
<td>6</td>
<td>0.045</td>
<td>0.030</td>
<td>False</td>
</tr>
</tbody>
</table>
</div>

### Solution, step 3: Identify the Largest $k$ and Conclude
The largest index $k$ satisfying $p_{(k)} \le T_k$ is $k^* = 3$ (where $p_{(3)} = 0.015 \le 0.015$).
Therefore, the Benjamini-Hochberg procedure rejects the first 3 null hypotheses:
$$\text{Reject } H_{(1)}, H_{(2)}, H_{(3)}$$
FDR control yields **3 scientific discoveries** compared to only 1 under Bonferroni, tripling statistical discovery yield while rigorously bounding expected false discovery proportion at $5\%$.

---

### Fully worked question 2: Storey's $\pi_0$ Proportion Estimation
A high-throughput drug screening study tests $m = 20,000$ molecular compounds.
Using tuning parameter $\lambda = 0.50$, the number of observed $p$-values exceeding $0.50$ is counted as $7,200$.
1. Compute Storey's estimate of the true null proportion $\hat{\pi}_0$.
2. Compute the estimated number of true null hypotheses $m_0$ and true non-null active compounds $m_1$.

### Solution, step 1: Formulate Storey's $\hat{\pi}_0$ Estimator
Storey's estimator is:
$$\hat{\pi}_0(\lambda) = \frac{\#\{ p_i > \lambda \}}{(1 - \lambda) m}$$
For $\lambda = 0.50$, $m = 20,000$, and $\#\{ p_i > 0.50 \} = 7,200$:
$$\hat{\pi}_0(0.50) = \frac{7200}{(1 - 0.50) \times 20,000} = \frac{7200}{0.50 \times 20,000} = \frac{7200}{10,000} = \mathbf{0.720} \quad (72.0\%)$$

### Solution, step 2: Compute Hypothesis Counts
The estimated number of true null hypotheses is:
$$\hat{m}_0 = \hat{\pi}_0 \times m = 0.720 \times 20,000 = \mathbf{14,400 \text{ inactive compounds}}$$
The estimated number of true alternative non-null discoveries is:
$$\hat{m}_1 = m - \hat{m}_0 = 20,000 - 14,400 = \mathbf{5,600 \text{ active biological compounds}}$$

---

### Fully worked question 3: Efron's Local False Discovery Rate Calculation
In an empirical Bayes neuroimaging analysis, a voxel has normalized $z$-score $z = 2.80$.
The empirical null density is standard normal $f_0(z) = \phi(z)$, the estimated proportion of null voxels is $\pi_0 = 0.90$, and the mixture marginal density at $z = 2.80$ is estimated via splines as $f(2.80) = 0.0240$.
Compute the local false discovery rate $\mathrm{lfdr}(2.80)$ and interpret the posterior probability.

### Solution, step 1: State the Local FDR Formula
Efron's local false discovery rate is:
$$\mathrm{lfdr}(z) = \frac{\pi_0 f_0(z)}{f(z)}$$

### Solution, step 2: Evaluate the Null Density $f_0(2.80)$
For standard normal $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$:
$$f_0(2.80) = \frac{1}{\sqrt{2\pi}} e^{-2.80^2 / 2} = 0.398942 \times e^{-7.84 / 2} = 0.398942 \times e^{-3.92} \approx 0.398942 \times 0.019841 \approx \mathbf{0.007915}$$

### Solution, step 3: Compute $\mathrm{lfdr}(2.80)$
Multiply by $\pi_0 = 0.90$:
$$\pi_0 f_0(2.80) = 0.90 \times 0.007915 = 0.007124$$
Divide by marginal density $f(2.80) = 0.0240$:
$$\mathrm{lfdr}(2.80) = \frac{0.007124}{0.0240} \approx \mathbf{0.2968} \quad (29.68\%)$$
Given an observed test statistic $z = 2.80$, there is a $29.68\%$ posterior probability that this specific voxel activation represents random background noise, and a $70.32\%$ probability that it reflects genuine neural activation.
"""

(DRAFT_DIR / "unit-8.md").write_text(u8.strip() + "\n", encoding="utf-8")
print("Unit 8 generated.")
