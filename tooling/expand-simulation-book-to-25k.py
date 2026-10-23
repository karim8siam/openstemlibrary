#!/usr/bin/env python3
"""
Comprehensive expansion script for Statistical Simulation and Monte Carlo Methods
to bring the book draft past 25,000 substantive prose words across all 8 units.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} expanded.")

# -------------------------------------------------------------
# UNIT 1 EXPANSION
# -------------------------------------------------------------
u1_expansion = r"""
## 1.10 Theoretical Foundations of Pseudo-Randomness and Algorithmic Information

In rigorous mathematical statistics, the concept of randomness cannot be satisfactorily defined by purely empirical observations. A deterministic computer executing finite instruction sequences cannot produce genuine ontological indeterminacy. Instead, computational statistics relies on algorithmic information theory, developed independently by Andrey Kolmogorov, Ray Solomonoff, and Gregory Chaitin, to formalize what distinguishes an effectively random sequence from a patterned sequence.

### 1. Kolmogorov Complexity and Incompressibility
Let $s$ be a finite binary string of length $m$, denoted $s \in \{0, 1\}^m$. The Kolmogorov complexity $K_U(s)$ with respect to a universal Turing machine $U$ is defined as the length of the shortest computer program $p$ that, when executed on $U$, halts and outputs the exact string $s$:

$$K_U(s) = \min_{p} \{ |p| : U(p) = s \}$$

A sequence $s$ of length $m$ is defined to be algorithmically incompressible, or Kolmogorov random, if its descriptive complexity is approximately equal to its length:

$$K_U(s) \ge m - c$$

where $c$ is a small universal constant independent of $m$. If a sequence can be produced by a program significantly shorter than its own length, the sequence contains structural redundancies and deterministic patterns. 

By definition, any pseudo-random number generator (PRNG) initialized with an $s$-bit seed and generating an $m$-bit sequence (where $m \gg s$) produces output whose Kolmogorov complexity is bounded by $K_U(s) \le |seed| + O(1) \ll m$. Therefore, PRNG streams are completely compressible and fail algorithmic randomness in the Kolmogorov sense. What makes them statistically viable is computational indistinguishability: no polynomial-time statistical test $T$ can distinguish the output of a cryptographic-grade PRNG from a truly uniform random sequence with non-negligible advantage.

### 2. Martin-Löf Randomness and Statistical Tests
Per Martin-Löf resolved the question of randomness for infinite sequences $\mathbf{x} = (x_1, x_2, \dots) \in \{0, 1\}^\infty$ using effective measure theory. An effective null set is an intersection of a nested sequence of open sets whose Lebesgue measure decreases computably to zero. An infinite sequence is Martin-Löf random if it does not belong to any effective null set.

In statistical practice, every goodness-of-fit test, serial correlation test, or spectral lattice analysis constitutes a computable statistical hypothesis test corresponding to an effective null set. If a PRNG possesses a structural flaw, it systematically falls into the rejection region of a specific computable null set, demonstrating non-randomness.

## 1.11 Multi-Stream Random Number Generation and Parallel Architectures

Modern high-performance statistical computing operates on massively parallel multi-core central processing units (CPUs) and graphics processing units (GPUs) capable of executing tens of thousands of concurrent simulation threads. In such distributed architectures, utilizing a single shared sequential PRNG is impossible due to memory lock contention and race conditions. Furthermore, naively seeding parallel threads with sequential integers (such as thread ID $k = 0, 1, 2, \dots$) causes catastrophic inter-stream correlations, known as seed clustering.

### 1. The Block Splitting and Leapfrog Methods
Two classical strategies for distributing a single linear congruential or recurrence-based generator across $P$ parallel worker threads are:

1. **Block Splitting (Skip-Ahead)**: The total sequence length $M$ is partitioned into $P$ non-overlapping blocks of length $L = \lfloor M/P \rfloor$. Worker $p$ (for $p = 0, \dots, P-1$) is assigned the subsequence starting at state $x_{pL}$. To implement block splitting efficiently without computing $L$ sequential iterations, the state transition matrix $A$ is raised to the power $L$ using binary exponentiation (repeated squaring):
$$x_{pL} = A^L x_0 \pmod m$$
Because matrix multiplication modulo $m$ requires only $O(k^3 \log_2 L)$ operations for a state of dimension $k$, the jump-ahead step executes in microseconds even for $L = 10^{15}$.

2. **Leapfrogging (Interleaving)**: Instead of contiguous blocks, worker $p$ consumes every $P$-th element of the sequence, starting from index $p$:
$$x_{p + jP} = A^{jP} x_p \pmod m$$
The primary drawback of leapfrogging in high-dimensional simulations is that spatial and serial correlations in the base generator become cross-thread correlations, causing synchronized biases across parallel Monte Carlo estimates.

### 2. Counter-Based Pseudo-Random Number Generators
For modern GPU acceleration, the recurrence-based paradigm (where state $x_{n+1} = f(x_n)$ must be stored and updated in thread-local registers) has been superseded by Counter-Based PRNGs (CBPRNGs), pioneered by John K. Salmon, Mark A. Moraes, Ron O. Dror, and David E. Shaw (2011).

In a CBPRNG, the $n$-th pseudo-random variate is computed by evaluating a stateless, highly non-linear cryptographic permutation function $F$ parameterized by a key $K$ and a counter $C$:

$$R_n = F_K(n)$$

Prominent counter-based generators include:
- **Philox**: Employs integer multiplication and Feistel-style mixing networks over 64-bit or 32-bit words (e.g., Philox4x32-10, Philox4x64-10). It provides high statistical dispersion with minimal register overhead.
- **Threefry**: A stripped-down cryptographic permutation derived from the Threefish block cipher (part of Skein, an SHA-3 finalist). It uses only XOR, addition, and word rotation (ARX operations), executing without integer multiplication instructions.

Because counter-based generators require zero inter-thread communication and allow arbitrary $O(1)$ random access to any position in a stream of length $2^{128}$ or $2^{256}$, each thread $k$ can simply evaluate $F_K(k \cdot 2^{64} + t)$ for local iteration $t$. The risk of stream overlap or inter-thread collision is mathematically infinitesimal.

## 1.12 Empirical Testing Batteries: The TestU01 Suite in Depth

Empirical statistical testing of pseudo-random number generators was revolutionized by Pierre L'Ecuyer and Richard Simard with the release of the **TestU01** library in 2007. TestU01 remains the gold standard benchmark against which all scientific PRNGs are evaluated, comprising far more rigorous batteries than the historical DIEHARD suite of George Marsaglia or the NIST SP 800-22 standard.

TestU01 organizes its batteries into three escalating levels of stringency:
- **SmallCrush**: 10 tests, evaluating roughly $1.6 \times 10^9$ random numbers in seconds.
- **Crush**: 96 tests, evaluating approximately $5 \times 10^{11}$ random numbers in roughly one hour.
- **BigCrush**: 106 tests, consuming more than $4 \times 10^{12}$ random numbers and several hours of high-precision computation.

A test is flagged as an unambiguous failure if its resulting $p$-value falls outside the extreme interval $[10^{-15}, 1 - 10^{-15}]$. The principal statistical tests implemented in TestU01 include:

<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Test Name</th>
<th>Mathematical Phenomenon Tested</th>
<th>Degrees of Freedom / Statistic</th>
<th>Common Failing Generators</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Collision Test</strong></td>
<td>Frequency of duplicate values when throwing $n$ balls into $k$ urns ($n \ll k$). Deviations detect clustering.</td>
<td>Poisson approximation or normal approximation to total collision count $C$.</td>
<td>Short-period LCGs, 32-bit linear congruential engines.</td>
</tr>
<tr>
<td><strong>Birthday Spacings</strong></td>
<td>Sort $n$ random points on $[0, 1)$, compute spacings $S_i$, and count duplicate spacings.</td>
<td>Asymptotically Poisson distributed with parameter $\lambda = n^3 / (4m)$.</td>
<td>Nearly all linear congruential generators with modulus $m \le 2^{64}$.</td>
</tr>
<tr>
<td><strong>Matrix Rank Test</strong></td>
<td>Construct $n$ random binary matrices of dimension $L \times k$ and compute their algebraic ranks over $\mathbb{F}_2$.</td>
<td>Chi-square goodness-of-fit against theoretical rank probabilities under uniform distribution.</td>
<td>Lagged Fibonacci generators, subtract-with-borrow engines.</td>
</tr>
<tr>
<td><strong>Serial Over/Underflow</strong></td>
<td>Higher-order multivariate serial dependencies across $t$-dimensional hypercubes.</td>
<td>Chi-square statistic on cell occupancy counts across $d$-dimensional grid partitions.</td>
<td>Tausworthe generators with poor feedback polynomials.</td>
</tr>
<tr>
<td><strong>Weight Distrib / Hamming</strong></td>
<td>Calculates Hamming weight (number of 1-bits) in blocks of consecutive random words.</td>
<td>Binomial distribution $\mathcal{B}(B, 0.5)$ compared via chi-square test.</td>
<td>Inadequately mixed shift-register generators.</td>
</tr>
<tr>
<td><strong>Linear Complexity Test</strong></td>
<td>Applies the Berlekamp-Massey algorithm to find the shortest linear feedback shift register producing the bit sequence.</td>
<td>Jump complexity distribution around $L/2$ compared to theoretical distribution.</td>
<td>Mersenne Twister MT19937 (fails dramatically due to linear structure over $\mathbb{F}_2$).</td>
</tr>
</tbody>
</table>
</div>

The failure of the famous **Mersenne Twister (MT19937)** on the Linear Complexity tests of BigCrush underscores why modern scientific computing is transitioning toward non-linear permutations such as PCG (Permuted Congruential Generator) and Philox: while MT19937 has an astronomical period of $2^{19937} - 1$, its transition function is strictly linear over the Galois field $\mathbb{F}_2$, rendering it vulnerable to matrix-rank and linear-complexity deficiencies in high-dimensional simulations.
"""

# -------------------------------------------------------------
# UNIT 2 EXPANSION
# -------------------------------------------------------------
u2_expansion = r"""
## 2.9 The Walker-Vose Alias Method for Arbitrary Discrete Distributions

When conducting agent-based simulations, Markov chain simulations with large discrete state spaces, or categorical sampling in natural language models, one must repeatedly draw variates from a discrete probability mass function defined on $K$ categories:

$$P(X = k) = p_k, \quad k \in \{1, 2, \dots, K\}, \quad \sum_{k=1}^K p_k = 1$$

A standard cumulative distribution function (CDF) inversion algorithm constructs the running prefix sums $S_j = \sum_{k=1}^j p_k$ and performs a binary search for a uniform draw $U \sim \mathcal{U}(0, 1)$. This requires $O(\log_2 K)$ search operations per generated variate. If $K$ is on the order of $10^5$ or $10^6$ (as in vocabulary token sampling or large network node activation), binary search incurs severe branch mispredictions and memory latency.

In 1974, Alastair J. Walker introduced the **Alias Method**, which was subsequently refined into an optimal $O(K)$ setup and $O(1)$ sampling algorithm by Michael D. Vose in 1991.

### 1. Theoretical Foundation of the Alias Decomposition
The mathematical insight of the Alias Method is that any discrete probability distribution with $K$ outcomes can be expressed as an equiprobable mixture of $K$ two-point distributions.

Imagine $K$ rectangular urns (or bins) of equal width $1/K$ and total height $1.0$. The total area across all $K$ bins is $K \times (1/K) = 1.0$. The probability distribution $\{p_1, \dots, p_K\}$ can be scaled by $K$ so that each category $k$ has normalized weight $q_k = K \cdot p_k$. The average normalized weight is:

$$\frac{1}{K} \sum_{k=1}^K q_k = \frac{K}{K} \sum_{k=1}^K p_k = 1.0$$

Some categories have $q_k < 1.0$ (they are "underfull"), while others have $q_k \ge 1.0$ (they are "overfull"). The Alias Theorem guarantees that one can redistribute the excess mass from overfull categories into underfull categories such that every bin $i \in \{1, \dots, K\}$ contains mass from at most **two** distinct categories:
1. The primary outcome $i$, occupying probability weight $F_i \in (0, 1]$.
2. An "alias" outcome $A_i \in \{1, \dots, K\}$, occupying the remaining weight $1 - F_i$.

### 2. The Vose Construction Algorithm
The preprocessing phase partitions categories into two worklists:
- **Small**: indices with $q_k < 1.0$.
- **Large**: indices with $q_k \ge 1.0$.

While both lists are non-empty:
1. Remove an index $s$ from **Small** and an index $l$ from **Large**.
2. Set the threshold probability table entry $F_s = q_s$.
3. Set the alias table entry $A_s = l$.
4. Reduce the remaining weight of category $l$ by the shortfall of $s$:
$$q_l \leftarrow q_l - (1.0 - q_s)$$
5. If the updated $q_l < 1.0$, insert $l$ into **Small**; otherwise, return $l$ to **Large**.

Because exactly one element is permanently removed from the active pools at each iteration, the construction terminates in at most $K$ steps, yielding exact $O(K)$ computational and memory complexity.

### 3. Constant Time Sampling Step
To generate a single realization $X \sim \{p_1, \dots, p_K\}$ in real-time simulation:
1. Generate a single uniform variate $U \sim \mathcal{U}(0, 1)$.
2. Compute the continuous coordinate $V = K \cdot U$.
3. Let $i = \lfloor V \rfloor + 1 \in \{1, \dots, K\}$ be the randomly selected bin index.
4. Let $W = V - \lfloor V \rfloor \in [0, 1)$ be the fractional position within that bin.
5. If $W < F_i$, return outcome $i$; otherwise, return outcome $A_i$.

This execution path consists of a single floating-point multiplication, a floor conversion, one array lookup, and a single branch, achieving strict $O(1)$ time complexity regardless of whether $K = 10$ or $K = 10,000,000$.

## 2.10 The Ratio-of-Uniforms Method

The **Ratio-of-Uniforms (RoU)** method, developed by Albert J. Kinderman and John F. Monahan (1977), is an elegant rejection-based simulation technique that transforms two independent uniform variates into a random variable from an arbitrary target continuous distribution. Unlike the classical Acceptance-Rejection method of von Neumann, RoU does not require finding an explicit dominating proposal density $g(x)$ that bounds $f(x)$ pointwise.

### 1. Mathematical Formulation
Let $X$ be a continuous random variable with probability density function:
$$f(x) = \frac{1}{Z} h(x), \quad x \in \mathbb{R}$$
where $h(x) \ge 0$ is a computable unnormalized density function and $Z = \int_{\mathbb{R}} h(x)\,dx$ is an intractable normalizing constant.

Consider the planar region $C_h \subset \mathbb{R}^2$ defined by:
$$C_h = \left\{ (u, v) \in \mathbb{R}^2 : 0 \le u \le \sqrt{h(v/u)} \right\}$$

*Theorem (Kinderman-Monahan)*: If a pair $(U, V)$ is distributed uniformly over the region $C_h$, then the ratio:
$$X = \frac{V}{U}$$
has exact probability density function $f(x) = h(x) / Z$.

*Proof*: The area of the region $C_h$ is given by the double integral:
$$\text{Area}(C_h) = \iint_{C_h} du\,dv = \int_{-\infty}^\infty \left[ \int_0^{\sqrt{h(v/u)}} du \right] dv$$
Perform the bivariate change of variables: $x = v/u$ and $u = u$. The Jacobian matrix of the transformation $(u, v) \mapsto (u, x)$ where $v = ux$ is:
$$J = \begin{pmatrix} \frac{\partial u}{\partial u} & \frac{\partial u}{\partial x} \\ \frac{\partial v}{\partial u} & \frac{\partial v}{\partial x} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ x & u \end{pmatrix} \implies |\det(J)| = u$$
Substituting this into the area integral:
$$\text{Area}(C_h) = \int_{-\infty}^\infty \int_0^{\sqrt{h(x)}} u\,du\,dx = \int_{-\infty}^\infty \left[ \frac{u^2}{2} \right]_0^{\sqrt{h(x)}} dx = \frac{1}{2} \int_{-\infty}^\infty h(x)\,dx = \frac{Z}{2}$$

Because $(U, V)$ is uniform on $C_h$, its joint density is constant:
$$f_{U, V}(u, v) = \frac{1}{\text{Area}(C_h)} = \frac{2}{Z}, \quad (u, v) \in C_h$$
Applying the transformation $(U, V) \to (U, X)$ with $V = UX$:
$$f_{U, X}(u, x) = f_{U, V}(u, ux) \cdot |\det(J)| = \frac{2}{Z} \cdot u, \quad 0 \le u \le \sqrt{h(x)}$$
Integrating out the nuisance coordinate $u$ to find the marginal density of $X$:
$$f_X(x) = \int_0^{\sqrt{h(x)}} \frac{2u}{Z}\,du = \frac{2}{Z} \left[ \frac{u^2}{2} \right]_0^{\sqrt{h(x)}} = \frac{h(x)}{Z}$$
which is identically the target probability density function.

### 2. Computational Bounding Box Construction
To sample uniformly from $C_h$, one constructs the minimal enclosing bounding box $[0, u_{\max}] \times [v_{\min}, v_{\max}]$, where:
$$u_{\max} = \sup_{x} \sqrt{h(x)}$$
$$v_{\min} = \inf_{x} \left( x \sqrt{h(x)} \right)$$
$$v_{\max} = \sup_{x} \left( x \sqrt{h(x)} \right)$$

Provided that $h(x)$ and $x^2 h(x)$ are bounded on $\mathbb{R}$, this bounding box is finite. The algorithm generates independent uniforms $U \sim \mathcal{U}(0, u_{\max})$ and $V \sim \mathcal{U}(v_{\min}, v_{\max})$. If $U^2 \le h(V / U)$, the variate $X = V / U$ is accepted; otherwise, the pair is rejected and the step is repeated.

For standard normal variates $h(x) = e^{-x^2/2}$, we obtain $u_{\max} = 1$, $v_{\min} = -\sqrt{2/e} \approx -0.8578$, and $v_{\max} = \sqrt{2/e} \approx 0.8578$. The acceptance probability is $\text{Area}(C_h) / [u_{\max}(v_{\max} - v_{\min})] = \sqrt{\pi/2} / (2 \sqrt{2/e}) = \sqrt{\pi e} / 4 \approx 0.7306$, yielding an exceptionally efficient Gaussian generator without transcendental trigonometric evaluations.

## 2.11 Simulation of High-Dimensional Gaussian Processes and Circulant Embedding

In spatial statistics, geostatistics, and functional data analysis, simulations require generating continuous sample paths from a **Gaussian Process (GP)**:

$$X(t) \sim \mathcal{GP}(m(t), K(t, s)), \quad t, s \in \mathcal{T} \subset \mathbb{R}^d$$

where $m(t) = \mathbb{E}[X(t)]$ is the mean function and $K(t, s) = \mathrm{Cov}(X(t), X(s))$ is a symmetric positive semi-definite covariance kernel (such as the Matérn, Squared Exponential, or Ornstein-Uhlenbeck kernel).

### 1. The Standard Cholesky Factorization Approach
When evaluating the Gaussian process at $N$ discrete locations $\mathbf{t} = (t_1, \dots, t_N)^T$, the joint distribution is multivariate normal:
$$\mathbf{X} \sim \mathcal{N}(\mathbf{m}, \mathbf{\Sigma}), \quad \mathbf{\Sigma}_{ij} = K(t_i, t_j)$$

The classical method computes the Cholesky decomposition of the covariance matrix:
$$\mathbf{\Sigma} = \mathbf{L} \mathbf{L}^T$$
where $\mathbf{L}$ is a lower-triangular matrix. Given an independent standard normal vector $\mathbf{Z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_N)$, the simulated Gaussian process realization is:
$$\mathbf{X} = \mathbf{m} + \mathbf{L} \mathbf{Z}$$

While mathematically exact and applicable to irregularly spaced coordinates, Cholesky factorization requires $O(N^3)$ arithmetic operations to compute the decomposition and $O(N^2)$ memory to store the matrix. For a two-dimensional grid of size $1024 \times 1024$, the number of locations is $N = 2^{20} \approx 10^6$, requiring $\approx 10^{18}$ floating-point operations and multiple terabytes of memory, rendering Cholesky factorization impossible.

### 2. Fast Circulant Embedding and FFT Simulation
When sample locations form a regular equispaced lattice on a stationary domain (where $K(t, s) = \kappa(t - s)$ depends only on the spatial displacement vector), the covariance matrix $\mathbf{\Sigma}$ exhibits a symmetric **Toeplitz** structure (in 1D) or **Block Toeplitz with Toeplitz Blocks (BTTB)** structure (in higher dimensions).

Dietrich and Newsam (1993) and Wood and Chan (1994) introduced the **Circulant Embedding** technique to reduce the computational complexity from $O(N^3)$ to $O(N \log N)$ using the Fast Fourier Transform (FFT).

1. **Embedding into a Circulant Matrix**: The $N \times N$ Toeplitz covariance matrix $\mathbf{\Sigma}$ is embedded into a larger $M \times M$ circulant matrix $\mathbf{C}$ (typically with $M = 2N$):
$$\mathbf{C} = \begin{pmatrix} \mathbf{\Sigma} & \mathbf{B} \\ \mathbf{B}^T & \mathbf{\Sigma} \end{pmatrix}$$
where $\mathbf{B}$ is chosen such that the rows of $\mathbf{C}$ are periodic circular shifts of each other.

2. **Spectral Decomposition via Discrete Fourier Transform**: Every circulant matrix is diagonalized by the unitary Discrete Fourier Transform matrix $\mathbf{F}$:
$$\mathbf{C} = \mathbf{F}^* \mathbf{\Lambda} \mathbf{F}$$
where $\mathbf{\Lambda} = \mathrm{diag}(\lambda_0, \dots, \lambda_{M-1})$ are the eigenvalues of $\mathbf{C}$, which are computed in $O(M \log M)$ operations by taking the FFT of the first column of $\mathbf{C}$:
$$\boldsymbol{\lambda} = \mathrm{FFT}(\mathbf{c}_0)$$

3. **Non-Negative Definiteness Condition**: If all eigenvalues satisfy $\lambda_j \ge 0$, $\mathbf{C}$ is positive semi-definite. A complex normal vector $\mathbf{W} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I}_M)$ is generated with independent real and imaginary standard Gaussian components:
$$\mathbf{Y} = \mathbf{F}^* (\mathbf{\Lambda}^{1/2} \mathbf{W}) = \mathrm{IFFT}(\sqrt{\boldsymbol{\lambda}} \odot \mathrm{FFT}(\mathbf{Z}))$$
Extracting the first $N$ elements of the real part of $\mathbf{Y}$ yields an exact realization of the Gaussian process $\mathbf{X}$ with covariance $\mathbf{\Sigma}$. The entire generation completes in $O(N \log N)$ operations, enabling real-time simulation of multi-million point Gaussian random fields.
"""

# -------------------------------------------------------------
# UNIT 3 EXPANSION
# -------------------------------------------------------------
u3_expansion = r"""
## 3.10 Higher-Order Asymptotic Theory of the Bootstrap and Edgeworth Expansions

In applied data analysis, practitioners frequently employ the normal-approximation bootstrap confidence interval:
$$\left[ \hat{\theta} - z_{1-\alpha/2} \cdot \widehat{\text{SE}}_{\text{boot}}, \, \hat{\theta} + z_{1-\alpha/2} \cdot \widehat{\text{SE}}_{\text{boot}} \right]$$
or the simple percentile interval $[\hat{\theta}^*_{(\alpha/2)}, \hat{\theta}^*_{(1-\alpha/2)}]$. However, rigorous theoretical statistics reveals that both of these standard intervals achieve only **first-order accuracy**: their coverage error is of order $O(n^{-1/2})$, meaning that for a nominal $95\%$ confidence interval, the true coverage probability is $0.95 \pm O(n^{-1/2})$.

Peter Hall (1992) and Bradley Efron (1987) established that the true power of bootstrap resampling emerges when studentized and adjusted using higher-order asymptotic expansions.

### 1. The Studentized Bootstrap (Bootstrap-t)
Let $\hat{\theta}$ be an estimator of parameter $\theta$, and let $\hat{\sigma}^2$ be a consistent estimator of its asymptotic variance $\mathrm{Var}(\hat{\theta})$. Consider the studentized root:
$$T = \frac{\hat{\theta} - \theta}{\hat{\sigma}}$$
Under regularity conditions, the distribution function of $T$ admits a one-term Edgeworth expansion:
$$P(T \le x) = \Phi(x) + n^{-1/2} p_1(x) \phi(x) + O(n^{-1})$$
where $\Phi(x)$ and $\phi(x)$ are the standard normal cumulative distribution and density functions, and $p_1(x)$ is an even polynomial whose coefficients depend on the skewness of the underlying population distribution:
$$p_1(x) = -\frac{1}{6} \kappa_3 (2x^2 + 1)$$
where $\kappa_3 = \mathbb{E}[(X - \mu)^3] / \sigma^3$ is the standardized skewness coefficient.

When we generate bootstrap resamples $\mathbf{x}^{*b}$, we compute the bootstrap studentized root:
$$T^{*b} = \frac{\hat{\theta}^{*b} - \hat{\theta}}{\hat{\sigma}^{*b}}$$
The bootstrap distribution function $P^*(T^* \le x)$ admits an identical Edgeworth expansion:
$$P^*(T^* \le x) = \Phi(x) + n^{-1/2} \hat{p}_1(x) \phi(x) + O_p(n^{-1})$$
Because $\hat{p}_1(x) - p_1(x) = O_p(n^{-1/2})$, taking the difference between the true distribution and the bootstrap distribution eliminates the leading $O(n^{-1/2})$ error term:
$$P(T \le x) - P^*(T^* \le x) = O_p(n^{-1})$$

Consequently, a two-sided confidence interval constructed using the quantiles $t^*_{\alpha/2}$ and $t^*_{1-\alpha/2}$ of the studentized bootstrap root achieves **second-order accuracy**:
$$P\left( \hat{\theta} - t^*_{1-\alpha/2} \hat{\sigma} \le \theta \le \hat{\theta} - t^*_{\alpha/2} \hat{\sigma} \right) = 1 - \alpha + O(n^{-1})$$
The coverage error drops from $O(n^{-1/2})$ to $O(n^{-1})$, providing vastly superior finite-sample calibration in skewed or heavy-tailed environments.

### 2. The $BC_a$ (Bias-Corrected and Accelerated) Bootstrap
While the bootstrap-$t$ is second-order accurate, it is not transformation-invariant and can exhibit erratic instability if $\hat{\sigma}^*$ is volatile. Efron (1987) introduced the **$BC_a$ bootstrap**, which achieves second-order accuracy ($O(n^{-1})$ coverage error) while simultaneously being fully transformation-invariant.

The $BC_a$ confidence interval endpoints are given by percentiles of the original unstudentized bootstrap distribution $\hat{\theta}^{*(1)} \le \dots \le \hat{\theta}^{*(B)}$, but evaluated at adjusted probability indices $\alpha_1, \alpha_2$:
$$\alpha_1 = \Phi\left( \hat{z}_0 + \frac{\hat{z}_0 + z_{\alpha/2}}{1 - a(\hat{z}_0 + z_{\alpha/2})} \right)$$
$$\alpha_2 = \Phi\left( \hat{z}_0 + \frac{\hat{z}_0 + z_{1-\alpha/2}}{1 - a(\hat{z}_0 + z_{1-\alpha/2})} \right)$$

Two fundamental diagnostic parameters govern the adjustment:
1. **The Bias-Correction Parameter ($\hat{z}_0$)**: Measures median bias on the normal scale:
$$\hat{z}_0 = \Phi^{-1} \left( \frac{1}{B} \sum_{b=1}^B \mathbb{I}(\hat{\theta}^{*b} < \hat{\theta}) \right)$$
If the bootstrap distribution is symmetric and centered exactly at $\hat{\theta}$, then $\hat{z}_0 = \Phi^{-1}(0.5) = 0$.
2. **The Acceleration Parameter ($a$)**: Quantifies the rate of change of the standard error of $\hat{\theta}$ with respect to the true parameter $\theta$. It is calculated from the leave-one-out jackknife values $\hat{\theta}_{(-i)}$:
$$a = \frac{\sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^3}{6 \left[ \sum_{i=1}^n (\bar{\theta}_{(\cdot)} - \hat{\theta}_{(-i)})^2 \right]^{3/2}}$$
where $\bar{\theta}_{(\cdot)} = \frac{1}{n} \sum_{i=1}^n \hat{\theta}_{(-i)}$. The parameter $a$ accounts for skewness in the underlying score function. When $a = 0$ and $\hat{z}_0 = 0$, the $BC_a$ interval reduces identically to the standard percentile interval.

## 3.11 Resampling Dependent Data: Block Bootstraps and Frequency-Domain Methods

The classical i.i.d. bootstrap operates on the fundamental assumption that observations $X_1, \dots, X_n$ are mutually independent. When applied to time series, spatial lattices, or longitudinal panels, i.i.d. sampling destroys the temporal auto-covariance structure $\gamma(h) = \mathrm{Cov}(X_t, X_{t+h})$. To preserve temporal dependence, statisticians employ **Block Bootstrap** methods.

### 1. Moving Block Bootstrap (MBB) and Circular Block Bootstrap (CBB)
Introduced independently by Hans R. Künsch (1989) and Regina Y. Liu (1988), the **Moving Block Bootstrap** resamples contiguous blocks of length $b$.

Let $\{X_1, X_2, \dots, X_n\}$ be a stationary time series. Define the $i$-th overlapping block of length $b$ as:
$$B_i = (X_i, X_{i+1}, \dots, X_{i+b-1}), \quad i \in \{1, 2, \dots, n - b + 1\}$$
There are $q = n - b + 1$ such blocks. To construct a bootstrap series of length $n$, we draw $k = \lceil n/b \rceil$ blocks independently with replacement from $\{B_1, \dots, B_q\}$ and concatenate them:
$$\mathbf{X}^* = (B_{I_1}, B_{I_2}, \dots, B_{I_k})$$

The **Circular Block Bootstrap (CBB)** wraps the time series periodically onto a circle, setting $X_{n+j} = X_j$. This ensures that every observation $X_t$ appears in exactly $b$ possible blocks, eliminating edge-effect bias in the mean.

### 2. The Stationary Bootstrap of Politis and Romano
A significant theoretical limitation of both MBB and CBB is that the concatenated bootstrap time series $\mathbf{X}^*$ is non-stationary: observations within a block share their original dependence, but observations across block boundaries are mutually independent.

Dimitris N. Politis and Joseph P. Romano (1994) resolved this issue with the **Stationary Bootstrap**. Instead of fixing the block length $b$, the block length $L$ is treated as an independent geometric random variable:
$$P(L = k) = (1 - p)^{k-1} p, \quad k \in \{1, 2, \dots\}, \quad \mathbb{E}[L] = \frac{1}{p} = b$$
At each step, with probability $1 - p$, the next observation is the sequential successor $X_{t+1}$ (wrapping circularly); with probability $p$, a new starting index is sampled uniformly from $\{1, \dots, n\}$.

*Theorem (Stationary Bootstrap Validity)*: Conditional on the original data $\mathbf{X}$, the pseudo-time series $\mathbf{X}^*$ generated by the Politis-Romano algorithm is strictly stationary almost surely.

The optimal expected block length $b = 1/p$ balances variance and bias:
$$b_{\text{opt}} \propto n^{1/3}$$
If $b$ is chosen too small, the long-range autocorrelation is severed, causing severe downward bias in variance estimation. If $b$ is chosen too large, sample diversity is reduced, increasing simulation variance.

## 3.12 Subsampling and the $m$-out-of-$n$ Bootstrap

Despite its versatility, the standard $n$-out-of-$n$ bootstrap exhibits well-known catastrophic failure modes in non-regular estimation problems:
1. **Extreme Value Estimation**: Estimating the maximum of a uniform distribution $\theta = \max(X_1, \dots, X_n)$ where $X_i \sim \mathcal{U}(0, \theta)$. The probability that the bootstrap sample maximum $\hat{\theta}^* = \max(\mathbf{X}^*)$ equals the sample maximum $\hat{\theta}$ is:
$$P^*(\hat{\theta}^* = \hat{\theta}) = 1 - \left(1 - \frac{1}{n}\right)^n \to 1 - e^{-1} \approx 0.632$$
The bootstrap distribution places a discrete probability mass of $63.2\%$ at the single point $\hat{\theta}$, whereas the true normalized distribution $n(\theta - \hat{\theta})$ is continuous exponential.
2. **Parameters on the Boundary**: Estimating $\theta \ge 0$ when the true parameter is $\theta = 0$.
3. **Heavy-Tailed Distributions**: Resampling data from stable Paretian distributions with infinite second moments ($\mathbb{E}[X^2] = \infty$).

### The $m$-out-of-$n$ Bootstrap Remedy
Peter J. Bickel, Friedrich Götze, and Willem R. van Zwet (1997) proved that these failure modes can be universally resolved by drawing resamples of size $m$ strictly smaller than $n$, such that:
$$m \to \infty \quad \text{and} \quad \frac{m}{n} \to 0 \quad \text{as } n \to \infty$$

Under the $m$-out-of-$n$ scheme, the normalized bootstrap statistic:
$$\tau_m (\hat{\theta}_m^* - \hat{\theta}_n)$$
converges in probability to the true limiting distribution of $\tau_n (\hat{\theta}_n - \theta)$, restoring consistency where the standard bootstrap fails. Politis and Romano's general theory of **Subsampling** extends this further by sampling without replacement from all $\binom{n}{m}$ subsets, requiring zero distributional assumptions beyond the existence of an asymptotic limit law.
"""

# -------------------------------------------------------------
# UNIT 4 EXPANSION
# -------------------------------------------------------------
u4_expansion = r"""
## 4.9 Quasi-Monte Carlo Integration and Low-Discrepancy Sequences

While Crude Monte Carlo integration achieves an asymptotic standard error of $O(n^{-1/2})$ regardless of dimension $d$, this convergence rate is agonizingly slow: achieving four decimal places of accuracy requires $n \approx 10^8$ sample draws. 

**Quasi-Monte Carlo (QMC)** replaces pseudo-random independent draws with deterministic, highly uniform points known as **Low-Discrepancy Sequences**. By deliberately preventing points from clustering or leaving empty voids in the unit hypercube $[0, 1]^d$, QMC achieves an asymptotic convergence rate approaching:

$$O\left( \frac{(\log n)^d}{n} \right)$$

For moderate dimensions $d$, this represents an almost linear convergence rate $O(n^{-1})$, vastly outperforming pseudo-random Monte Carlo.

### 1. Discrepancy and the Koksma-Hlawka Inequality
Let $P_n = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ be a deterministic point set in the unit hypercube $I^d = [0, 1]^d$. For any sub-box anchored at the origin $[\mathbf{0}, \mathbf{y}) = \prod_{j=1}^d [0, y_j)$, the empirical count of points falling in the box is:

$$A([\mathbf{0}, \mathbf{y}); P_n) = \sum_{i=1}^n \mathbb{I}(\mathbf{x}_i \in [\mathbf{0}, \mathbf{y}))$$

The local discrepancy function measures the deviation between the empirical fraction of points and the theoretical volume $\lambda([\mathbf{0}, \mathbf{y})) = \prod_{j=1}^d y_j$:

$$R(\mathbf{y}; P_n) = \frac{A([\mathbf{0}, \mathbf{y}); P_n)}{n} - \prod_{j=1}^d y_j$$

The **Star Discrepancy** $D_n^*(P_n)$ is the supremum norm of this deviation over all origin-anchored boxes:

$$D_n^*(P_n) = \sup_{\mathbf{y} \in [0, 1]^d} |R(\mathbf{y}; P_n)|$$

*Theorem (The Koksma-Hlawka Inequality)*: If $f: [0, 1]^d \to \mathbb{R}$ has bounded variation in the sense of Hardy and Krause, denoted $V_{\text{HK}}(f) < \infty$, then the deterministic integration error is bounded by:

$$\left| \frac{1}{n} \sum_{i=1}^n f(\mathbf{x}_i) - \int_{[0, 1]^d} f(\mathbf{x})\,d\mathbf{x} \right| \le V_{\text{HK}}(f) \cdot D_n^*(P_n)$$

This fundamental theorem separates the integration error into two independent components:
1. $V_{\text{HK}}(f)$: depends purely on the smoothness and regularity of the integrand $f$.
2. $D_n^*(P_n)$: depends purely on the geometric uniformity of the point set $P_n$.

### 2. Constructions of Low-Discrepancy Sequences
A sequence $\{\mathbf{x}_n\}$ is called a low-discrepancy sequence if its first $n$ elements satisfy $D_n^*(P_n) \le C_d \frac{(\log n)^d}{n}$ for all $n$. Three major families dominate computational practice:

1. **Halton Sequences**: Generalize the 1D van der Corput sequence to $d$ dimensions. Let $p_1, \dots, p_d$ be the first $d$ prime numbers. The $i$-th point is:
$$\mathbf{x}_i = (\phi_{p_1}(i), \phi_{p_2}(i), \dots, \phi_{p_d}(i))$$
where $\phi_p(i) = \sum_{k=0}^M a_k(i) p^{-(k+1)}$ is the radical inverse function expanding integer $i = \sum_{k=0}^M a_k(i) p^k$ in base $p$.
2. **Sobol' Sequences**: Constructed in base 2 using primitive polynomials over the Galois field $\mathbb{F}_2$. A set of direction integers $v_j$ defines the bitwise XOR transformations generating coordinates. Sobol' sequences satisfy the $(t, s)$-sequence criteria, guaranteeing optimal uniformity across dyadic elementary intervals.
3. **Faure and Niederreiter Sequences**: Exploit algebraic geometry and polynomial rings over general finite fields $\mathbb{F}_q$.

## 4.10 The Curse of Dimensionality and Effective Dimension

A naive inspection of the Koksma-Hlawka upper bound $O((\log n)^d / n)$ suggests that QMC integration should fail catastrophically in high dimensions: if $d = 100$, $(\log n)^{100}$ does not decrease below $n$ until $n$ exceeds the number of subatomic particles in the observable universe. 

Yet, in financial engineering and computational physics, Sobol' sequences routinely beat Crude Monte Carlo in 100-dimensional and 360-dimensional mortgage-backed security simulations. Ian H. Sloan and Henryk Woźniakowski (1998), along with Russel E. Caflisch, William J. Morokoff, and Art B. Owen (1997), solved this paradox by introducing the concept of **Effective Dimension**.

### 1. ANOVA Decomposition of Functions
Any square-integrable function $f: [0, 1]^d \to \mathbb{R}$ admits an exact orthogonal Analysis of Variance (ANOVA) decomposition:

$$f(\mathbf{x}) = f_0 + \sum_{j=1}^d f_j(x_j) + \sum_{j < k} f_{jk}(x_j, x_k) + \dots + f_{1, 2, \dots, d}(\mathbf{x}) = \sum_{u \subseteq \{1, \dots, d\}} f_u(\mathbf{x}_u)$$

where $f_0 = \int f(\mathbf{x})\,d\mathbf{x}$, each term $f_u$ depends only on the coordinate subset $u \subseteq \{1, \dots, d\}$, and all terms are mutually orthogonal in $L^2([0, 1]^d)$:
$$\int_{[0, 1]^d} f_u(\mathbf{x}_u) f_v(\mathbf{x}_v)\,d\mathbf{x} = 0 \quad \text{for } u \ne v$$

The total variance $\sigma^2 = \mathrm{Var}(f(\mathbf{X}))$ decomposes into variance components $\sigma_u^2 = \mathrm{Var}(f_u(\mathbf{X}_u))$:
$$\sigma^2 = \sum_{u \subseteq \{1, \dots, d\}, u \ne \emptyset} \sigma_u^2$$

### 2. Truncation Dimension and Superposition Dimension
Caflisch, Morokoff, and Owen defined two operational metrics:
1. **Effective Dimension in the Truncation Sense**: The smallest integer $d_T$ such that the variance explained by the first $d_T$ coordinates constitutes at least $1 - \alpha$ (typically $99\%$) of the total variance:
$$\sum_{u \subseteq \{1, 2, \dots, d_T\}} \sigma_u^2 \ge (1 - \alpha) \sigma^2$$
If a 360-dimensional problem has truncation dimension $d_T = 3$, only the first 3 coordinates drive $99\%$ of the variation, while the remaining 357 coordinates act as negligible perturbations.
2. **Effective Dimension in the Superposition Sense**: The smallest integer $d_S$ such that terms depending on at most $d_S$ variables explain at least $1 - \alpha$ of the total variance:
$$\sum_{|u| \le d_S} \sigma_u^2 \ge (1 - \alpha) \sigma^2$$
In many quantitative models, even if all 100 coordinates are equally active, functions are dominated by low-order interactions ($|u| \le 2$, meaning single-variable and pairwise effects). Because low-discrepancy sequences exhibit exceptional bivariate and trivariate projections, QMC integrates these low-order ANOVA components with near $O(n^{-1})$ accuracy.

## 4.11 Randomized Quasi-Monte Carlo (RQMC) and Scrambled Nets

A major practical drawback of pure deterministic QMC is that the Koksma-Hlawka bound provides an uncomputable worst-case deterministic error bound: the variation $V_{\text{HK}}(f)$ is impossible to evaluate analytically for complex simulation models. Consequently, deterministic QMC cannot produce a valid statistical standard error or confidence interval.

**Randomized Quasi-Monte Carlo (RQMC)** resolves this dilemma by randomizing a low-discrepancy point set $P_n$ such that:
1. Each individual randomized point $\mathbf{X}_i$ is uniformly distributed over the hypercube: $\mathbf{X}_i \sim \mathcal{U}([0, 1]^d)$.
2. The collective low-discrepancy structure of the ensemble is strictly preserved.

### 1. Cranley-Patterson Rotation (Random Shift)
The simplest RQMC randomization, introduced by R. Cranley and T. N. Patterson (1976), generates a single uniform shift vector $\mathbf{U} \sim \mathcal{U}([0, 1]^d)$ and shifts all deterministic points modulo 1:

$$\tilde{\mathbf{x}}_i = (\mathbf{x}_i + \mathbf{U}) \pmod 1, \quad i = 1, \dots, n$$

By repeating this procedure independently $M$ times with distinct shift vectors $\mathbf{U}_1, \dots, \mathbf{U}_M$, we obtain $M$ independent, unbiased estimators $\hat{\theta}^{(1)}, \dots, \hat{\theta}^{(M)}$, where:
$$\hat{\theta}^{(m)} = \frac{1}{n} \sum_{i=1}^n f(\tilde{\mathbf{x}}_i^{(m)})$$
The grand RQMC estimator is the sample average:
$$\hat{\theta}_{\text{RQMC}} = \frac{1}{M} \sum_{m=1}^M \hat{\theta}^{(m)}$$
Its empirical standard error is calculated directly using elementary sample variance formulas:
$$\widehat{\text{SE}}(\hat{\theta}_{\text{RQMC}}) = \sqrt{\frac{1}{M(M-1)} \sum_{m=1}^M (\hat{\theta}^{(m)} - \hat{\theta}_{\text{RQMC}})^2}$$

### 2. Owen's Scrambled Nets
Art B. Owen (1995) developed a deeper randomization scheme: **Nested Scrambling**. For digital $(t, m, s)$-nets in base $b$, Owen's method applies independent random permutations to the digits of each coordinate expansion, conditioned on prefix history.

*Theorem (Owen)*: For any function $f$ whose partial derivatives satisfy Lipschitz continuity, integration over an Owen-scrambled net of size $n$ achieves a root mean square error (RMSE) of:

$$\text{RMSE}(\hat{\theta}_{\text{scrambled}}) = O\left( n^{-3/2} (\log n)^{(d-1)/2} \right)$$

This improves upon the deterministic rate $O(n^{-1})$ and destroys the classical Monte Carlo rate $O(n^{-1/2})$, establishing RQMC as the premier integration technology for smooth simulation models.
"""

# -------------------------------------------------------------
# UNIT 5 EXPANSION
# -------------------------------------------------------------
u5_expansion = r"""
## 5.9 Stratified Sampling and Optimal Neyman Allocation

In standard random sampling from a heterogeneous population or sample space $\Omega$, sample draws tend to cluster randomly in certain regions while under-representing others. **Stratified Sampling** partitions the sample space $\Omega$ into $K$ mutually exclusive and exhaustive strata:

$$\Omega = \Omega_1 \cup \Omega_2 \cup \dots \cup \Omega_K, \quad \Omega_j \cap \Omega_k = \emptyset \quad \forall j \ne k$$

Let $p_k = P(\mathbf{X} \in \Omega_k) = \int_{\Omega_k} f(\mathbf{x})\,d\mathbf{x}$ be the known probability weight of stratum $k$, such that $\sum_{k=1}^K p_k = 1$. The target quantity $\theta = \mathbb{E}[h(\mathbf{X})]$ can be decomposed by the law of total expectation:

$$\theta = \sum_{k=1}^K p_k \, \mathbb{E}[h(\mathbf{X}) \mid \mathbf{X} \in \Omega_k] = \sum_{k=1}^K p_k \, \mu_k$$

where $\mu_k = \mathbb{E}[h(\mathbf{X}) \mid \mathbf{X} \in \Omega_k]$ is the conditional stratum mean.

### 1. The Stratified Estimator
To estimate $\theta$, we allocate a total sample size $n = \sum_{k=1}^K n_k$ by drawing $n_k$ independent samples $\mathbf{X}_{k, 1}, \dots, \mathbf{X}_{k, n_k}$ strictly from the conditional density within stratum $k$:
$$f(\mathbf{x} \mid \mathbf{X} \in \Omega_k) = \frac{f(\mathbf{x}) \mathbb{I}(\mathbf{x} \in \Omega_k)}{p_k}$$

The stratified Monte Carlo estimator is:
$$\hat{\theta}_{\text{strat}} = \sum_{k=1}^K p_k \bar{Y}_k = \sum_{k=1}^K \frac{p_k}{n_k} \sum_{i=1}^{n_k} h(\mathbf{X}_{k, i})$$

Because each conditional sample average $\bar{Y}_k$ is an unbiased estimator of $\mu_k$, $\hat{\theta}_{\text{strat}}$ is strictly unbiased: $\mathbb{E}[\hat{\theta}_{\text{strat}}] = \sum_{k=1}^K p_k \mu_k = \theta$. Furthermore, because draws across distinct strata are generated independently, the variance is strictly additive:

$$\mathrm{Var}(\hat{\theta}_{\text{strat}}) = \sum_{k=1}^K p_k^2 \, \mathrm{Var}(\bar{Y}_k) = \sum_{k=1}^K \frac{p_k^2 \sigma_k^2}{n_k}$$

where $\sigma_k^2 = \mathrm{Var}(h(\mathbf{X}) \mid \mathbf{X} \in \Omega_k)$ is the within-stratum variance.

### 2. Proportional vs. Optimal Neyman Allocation
The variance of $\hat{\theta}_{\text{strat}}$ depends decisively on the choice of allocation $\{n_1, \dots, n_K\}$ subject to $\sum_{k=1}^K n_k = n$:

1. **Proportional Allocation**: Sample sizes are assigned in exact proportion to stratum probability weights: $n_k = n \cdot p_k$. Under proportional allocation:
$$\mathrm{Var}(\hat{\theta}_{\text{prop}}) = \sum_{k=1}^K \frac{p_k^2 \sigma_k^2}{n p_k} = \frac{1}{n} \sum_{k=1}^K p_k \sigma_k^2$$
Recall the Law of Total Variance:
$$\mathrm{Var}(h(\mathbf{X})) = \mathbb{E}[\mathrm{Var}(h(\mathbf{X}) \mid \text{stratum})] + \mathrm{Var}(\mathbb{E}[h(\mathbf{X}) \mid \text{stratum}]) = \sum_{k=1}^K p_k \sigma_k^2 + \sum_{k=1}^K p_k (\mu_k - \theta)^2$$
Comparing Crude Monte Carlo to proportional stratification:
$$\mathrm{Var}(\hat{\theta}_{\text{crude}}) - \mathrm{Var}(\hat{\theta}_{\text{prop}}) = \frac{1}{n} \sum_{k=1}^K p_k (\mu_k - \theta)^2 \ge 0$$
Proportional stratification is guaranteed to eliminate all between-stratum variation from the simulation error without any risk of increasing variance.

2. **Optimal Neyman Allocation**: Jerzy Neyman (1934) solved the constrained optimization problem of minimizing $\sum_{k=1}^K \frac{p_k^2 \sigma_k^2}{n_k}$ subject to $\sum_{k=1}^K n_k = n$ using Lagrange multipliers:
$$n_k^* = n \left( \frac{p_k \sigma_k}{\sum_{j=1}^K p_j \sigma_j} \right)$$
Under Neyman allocation, more computational effort is allocated to strata that are either more probable ($p_k$ is large) or more volatile ($\sigma_k$ is large). The resulting minimal variance is:
$$\mathrm{Var}(\hat{\theta}_{\text{Neyman}}) = \frac{1}{n} \left( \sum_{k=1}^K p_k \sigma_k \right)^2$$
By Cauchy-Schwarz, $\left( \sum p_k \sigma_k \right)^2 \le \sum p_k \sigma_k^2$, guaranteeing that Neyman allocation always achieves lower or equal variance compared to proportional allocation.

## 5.10 Latin Hypercube Sampling (LHS) and Orthogonal Arrays

When simulating complex computer experiments or financial models in $d$ dimensions, classical stratification becomes infeasible: dividing each coordinate axis into $K$ intervals generates $K^d$ multidimensional strata. If $d = 20$ and $K = 10$, $K^d = 10^{20}$ cells, exceeding any feasible computational sample size $n$.

Michael D. McKay, Richard J. Beckman, and William J. Conover (1979) invented **Latin Hypercube Sampling (LHS)** to extend stratified sampling to arbitrary dimensions without combinatorial cell explosion.

### 1. Construction of a Latin Hypercube Sample
To generate an LHS design of size $n$ in $d$ dimensions:
1. Divide the domain of each coordinate $j \in \{1, \dots, d\}$ into $n$ equiprobable intervals:
$$I_{j, k} = \left[ \frac{k-1}{n}, \frac{k}{n} \right], \quad k = 1, 2, \dots, n$$
2. For each dimension $j$, generate an independent uniform random permutation of the integers $\{1, 2, \dots, n\}$, denoted $\pi_j = (\pi_j(1), \dots, \pi_j(n))$.
3. Generate $n \times d$ independent uniform draws $U_{j, i} \sim \mathcal{U}(0, 1)$.
4. Construct the $i$-th simulation point $\mathbf{X}_i = (X_{1, i}, \dots, X_{d, i})^T$ where:
$$X_{j, i} = \frac{\pi_j(i) - 1 + U_{j, i}}{n}$$

By construction, each interval $I_{j, k}$ of every coordinate axis contains exactly one sample point. When projected onto any 1-dimensional coordinate margin, the Latin Hypercube sample provides perfect 1D stratification.

### 2. Variance Reduction Properties of LHS
Michael Stein (1987) established the asymptotic distribution of Latin Hypercube estimators. Let $f: [0, 1]^d \to \mathbb{R}$ be square-integrable, and consider its additive main-effects approximation:
$$f_{\text{add}}(\mathbf{x}) = \mu + \sum_{j=1}^d [f_j(x_j) - \mu]$$
where $f_j(x_j) = \mathbb{E}[f(\mathbf{X}) \mid X_j = x_j]$. Let the residual non-additive component be:
$$r(\mathbf{x}) = f(\mathbf{x}) - f_{\text{add}}(\mathbf{x})$$

*Theorem (Stein's Theorem)*: As $n \to \infty$, the Latin Hypercube estimator satisfies:
$$\sqrt{n}(\hat{\theta}_{\text{LHS}} - \theta) \xrightarrow{d} \mathcal{N}\left( 0, \int_{[0, 1]^d} r^2(\mathbf{x})\,d\mathbf{x} \right)$$

Whereas Crude Monte Carlo has asymptotic variance equal to the total variance $\mathrm{Var}(f(\mathbf{X})) = \mathrm{Var}(f_{\text{add}}) + \mathrm{Var}(r)$, Latin Hypercube Sampling asymptotically purges **$100\%$ of the additive main-effects variance**, leaving only non-linear interactions in the error term. If the target model is predominantly additive, LHS achieves order-of-magnitude variance reductions at zero additional computational cost.

## 5.11 Adaptive Importance Sampling and the Cross-Entropy Method

Standard Importance Sampling requires specifying a proposal density $g(\mathbf{x})$ in advance. If $g(\mathbf{x})$ fails to cover the heavy tails of the integrand, the importance weights $w(\mathbf{x}) = f(\mathbf{x}) / g(\mathbf{x})$ can become unbounded, resulting in infinite variance. 

**Adaptive Importance Sampling (AIS)** and the **Cross-Entropy (CE)** method, developed by Reuven Rubinstein (1997), iteratively optimize the proposal density $g(\mathbf{x}; \mathbf{v})$ within a parametric family to minimize the Kullback-Leibler (KL) divergence to the theoretical zero-variance optimal density $g^*(\mathbf{x}) \propto |h(\mathbf{x})| f(\mathbf{x})$.

### 1. Kullback-Leibler Divergence Minimization
The theoretical optimal density is $g^*(\mathbf{x}) = \frac{h(\mathbf{x}) f(\mathbf{x})}{\theta}$. The Cross-Entropy between $g^*$ and a parametric proposal $g(\mathbf{x}; \mathbf{v})$ is:

$$\mathcal{D}_{\text{KL}}(g^* \parallel g(\cdot; \mathbf{v})) = \int g^*(\mathbf{x}) \log \left( \frac{g^*(\mathbf{x})}{g(\mathbf{x}; \mathbf{v})} \right) d\mathbf{x} = \int g^*(\mathbf{x}) \log g^*(\mathbf{x})\,d\mathbf{x} - \int g^*(\mathbf{x}) \log g(\mathbf{x}; \mathbf{v})\,d\mathbf{x}$$

Minimizing this divergence is mathematically equivalent to maximizing the objective:

$$\max_{\mathbf{v}} D(\mathbf{v}) = \int \frac{h(\mathbf{x}) f(\mathbf{x})}{\theta} \log g(\mathbf{x}; \mathbf{v})\,d\mathbf{x} \iff \max_{\mathbf{v}} \mathbb{E}_{\mathbf{w}} \left[ h(\mathbf{X}) \frac{f(\mathbf{X})}{g(\mathbf{X}; \mathbf{w})} \log g(\mathbf{X}; \mathbf{v}) \right]$$

where $\mathbf{w}$ is an arbitrary reference parameter vector.

### 2. Multi-Stage Iterative Optimization
In rare-event simulation (e.g., estimating $P(S(\mathbf{X}) \ge \gamma)$ where $\gamma$ is a catastrophic risk threshold and the event occurs with probability $10^{-7}$), sampling directly from $f(\mathbf{x})$ produces zero hits. The CE method constructs a sequence of intermediate thresholds $\gamma_1 < \gamma_2 < \dots < \gamma_T = \gamma$ and parameter vectors $\mathbf{v}_1, \dots, \mathbf{v}_T$:

1. Initialize $\mathbf{v}_0$ matching the prior distribution.
2. At iteration $t$, generate $N$ draws from $g(\mathbf{x}; \mathbf{v}_{t-1})$.
3. Set the intermediate threshold $\gamma_t$ as the $(1 - \rho)$-quantile of the sample scores (typically $\rho = 0.10$).
4. Update the parameter vector $\mathbf{v}_t$ by solving the empirical maximization:
$$\mathbf{v}_t = \arg\max_{\mathbf{v}} \frac{1}{N} \sum_{i=1}^N \mathbb{I}(S(\mathbf{X}_i) \ge \gamma_t) \frac{f(\mathbf{X}_i)}{g(\mathbf{X}_i; \mathbf{v}_{t-1})} \log g(\mathbf{X}_i; \mathbf{v})$$
When $g(\mathbf{x}; \mathbf{v})$ belongs to a Natural Exponential Family (such as multivariate Gaussian), this update admits a closed-form analytical solution for the sample mean and covariance matrix.
5. Repeat until $\gamma_t \ge \gamma$, at which point the final proposal $g(\mathbf{x}; \mathbf{v}_T)$ samples rare events with high frequency, reducing the relative variance of rare-event estimators from thousands to near zero.
"""

# -------------------------------------------------------------
# UNIT 6 EXPANSION
# -------------------------------------------------------------
u6_expansion = r"""
## 6.9 Geometric Ergodicity, Spectral Gaps, and Drift Conditions

In Unit 6, we demonstrated that if a Markov transition kernel $K(\mathbf{x}, \cdot)$ satisfies $\pi$-irreducibility, aperiodicity, and Harris recurrence, the distribution of state $\mathbf{X}_n$ converges in total variation distance to the stationary target distribution $\pi$:

$$\lim_{n \to \infty} \| K^n(\mathbf{x}, \cdot) - \pi(\cdot) \|_{\text{TV}} = 0$$

However, Harris recurrence does not specify *how rapidly* this convergence occurs. If convergence is sublinear (e.g., polynomial $O(n^{-\alpha})$), an empirical MCMC run with $10^6$ iterations may remain severely contaminated by starting-value bias. To guarantee reliable simulation inference, Markov chains must satisfy **Geometric Ergodicity**.

### 1. Geometric Ergodicity and the Spectral Gap
A Markov chain with transition kernel $K$ and stationary distribution $\pi$ is **geometrically ergodic** if there exists a constant $\rho \in [0, 1)$ and a function $M(\mathbf{x}) < \infty$ such that:

$$\| K^n(\mathbf{x}, \cdot) - \pi(\cdot) \|_{\text{TV}} \le M(\mathbf{x}) \rho^n, \quad \forall n \in \mathbb{N}$$

If the bounding constant $M(\mathbf{x}) \le M$ is independent of starting state $\mathbf{x}$, the chain is **uniformly ergodic**, which implies exponential convergence uniform across the entire state space.

Consider the transition operator $K$ acting on the Hilbert space $L^2(\pi)$ of square-integrable functions with inner product $\langle g, h \rangle_\pi = \int g(\mathbf{x}) h(\mathbf{x}) \pi(d\mathbf{x})$. For reversible Markov chains (satisfying detailed balance), $K$ is a self-adjoint linear operator. The spectrum of $K$ is bounded within $[-1, 1]$, with the eigenvalue $1$ corresponding to constant functions.

The **Absolute Spectral Gap** $\gamma^*$ is defined as:
$$\gamma^* = 1 - \sup \{ |\lambda| : \lambda \in \mathrm{Spectrum}(K), \, \lambda \ne 1 \}$$
A reversible Markov chain is geometrically ergodic if and only if it possesses a positive spectral gap: $\gamma^* > 0$. The asymptotic rate of convergence is governed directly by $\rho = 1 - \gamma^*$.

### 2. Drift and Minorization (Foster-Lyapunov) Conditions
Proving geometric ergodicity directly from kernel definitions is notoriously difficult. Sean Meyn and Richard L. Tweedie (1993) established the Foster-Lyapunov drift condition framework, which provides practical analytical criteria for geometric ergodicity.

*Theorem (Foster-Lyapunov Drift Condition)*: Let $C \subset \mathcal{X}$ be a small set (meaning there exists $m \ge 1$, $\epsilon > 0$, and a probability measure $\nu$ such that $K^m(\mathbf{x}, A) \ge \epsilon \nu(A)$ for all $\mathbf{x} \in C$). If there exists a Lyapunov function $V: \mathcal{X} \to [1, \infty)$ and constants $\lambda \in (0, 1)$ and $b < \infty$ such that:

$$K V(\mathbf{x}) = \int_{\mathcal{X}} V(\mathbf{y}) K(\mathbf{x}, d\mathbf{y}) \le \lambda V(\mathbf{x}) + b \, \mathbb{I}_C(\mathbf{x}), \quad \forall \mathbf{x} \in \mathcal{X}$$

then the Markov chain is geometrically ergodic.

*Intuition*: Outside the compact core $C$, the expected value of the Lyapunov function strictly contracts by factor $\lambda < 1$ at every step. This powerful inward drift prevents the random walk from drifting into the tail regions, guaranteeing rapid geometric convergence back to the high-density core of $\pi$.

## 6.10 The Gelman-Roberts-Gilks Optimal Scaling Theorem

In Random Walk Metropolis (RWM) sampling, the practitioner must select the proposal covariance matrix $\mathbf{\Sigma}_{\text{prop}} = \sigma_d^2 \mathbf{I}_d$. If the proposal step size $\sigma_d$ is chosen too small, the chain accepts almost every proposal ($\alpha \approx 100\%$), but diffuses through the state space with agonizing slowness ($O(n^{-1/2})$ random walk exploration). If $\sigma_d$ is chosen too large, the proposals land in distant tail regions with near-zero density, causing almost all steps to be rejected ($\alpha \approx 0\%$) and leaving the chain stuck at its current state.

Andrew Gelman, Gareth O. Roberts, and Walter R. Gilks (1997) proved one of the most celebrated theorems in computational statistics: finding the optimal proposal scale and acceptance rate.

### 1. The Asymptotic Diffusion Limit
Consider an independent and identically distributed $d$-dimensional target distribution:
$$\pi_d(\mathbf{x}) = \prod_{i=1}^d f(x_i)$$
Let the proposal distribution be Gaussian with scaled variance:
$$\mathbf{Y} \sim \mathcal{N}\left( \mathbf{X}_t, \frac{\ell^2}{d} \mathbf{I}_d \right)$$
where $\ell > 0$ is a fixed scaling parameter, and time is accelerated by a factor of $d$: $Z_t^{(d)} = X_{\lfloor dt \rfloor, 1}$.

*Theorem (Roberts, Gelman, and Gilks, 1997)*: As dimension $d \to \infty$, the first coordinate process $Z_t^{(d)}$ converges weakly to a continuous Langevin diffusion process $Z_t$ satisfying the Stochastic Differential Equation (SDE):

$$dZ_t = \sqrt{h(\ell)} \, dB_t + \frac{1}{2} h(\ell) \, \nabla \log f(Z_t) \, dt$$

where $B_t$ is standard Brownian motion, and the diffusion speed function $h(\ell)$ is given by:

$$h(\ell) = 2 \ell^2 \, \Phi\left( -\frac{\ell \sqrt{I}}{2} \right)$$
where $I = \int_{-\infty}^\infty \left( \frac{f'(x)}{f(x)} \right)^2 f(x)\,dx$ is the Fisher information of a single component.

### 2. Maximizing Diffusion Speed and the 0.234 Rule
Maximizing the rate of exploration of the state space corresponds to maximizing the diffusion speed coefficient $h(\ell)$ with respect to $\ell$:

$$\frac{d}{d\ell} \left[ 2 \ell^2 \Phi\left( -\frac{\ell \sqrt{I}}{2} \right) \right] = 0$$

Solving this optimization numerically reveals that the maximum occurs when $\ell^* = 2.38 / \sqrt{I}$. Evaluating the asymptotic acceptance rate at this optimal scaling yields:

$$a(\ell^*) = 2 \Phi\left( -\frac{\ell^* \sqrt{I}}{2} \right) = 2 \Phi\left( -\frac{2.38}{2} \right) = 2 \Phi(-1.19) \approx 0.2338 \approx \mathbf{0.234}$$

This establishes the universal **23.4% Acceptance Rate Rule**: for high-dimensional random walk Metropolis, proposal dispersion should be tuned so that approximately $23.4\%$ of proposed moves are accepted. (For 1-dimensional targets, the optimal acceptance rate is approximately $0.44$).

## 6.11 Advanced MCMC Diagnostics: Rank-Normalized $\hat{R}$ and Autocorrelation Analysis

Because MCMC iterations are sequentially correlated, assessing convergence and computing genuine estimation precision requires specialized diagnostic metrics.

### 1. Effective Sample Size (ESS) and Autocorrelation
For a stationary Markov chain with variance $\sigma^2$ and lag-$k$ autocorrelation $\rho_k = \mathrm{Corr}(X_t, X_{t+k})$, the variance of the empirical sample mean $\bar{X}_n = \frac{1}{n} \sum_{t=1}^n X_t$ is:

$$\mathrm{Var}(\bar{X}_n) = \frac{\sigma^2}{n} \left[ 1 + 2 \sum_{k=1}^{n-1} \left( 1 - \frac{k}{n} \right) \rho_k \right] \approx \frac{\sigma^2}{n} \left[ 1 + 2 \sum_{k=1}^\infty \rho_k \right]$$

The quantity:
$$\tau_{\text{int}} = 1 + 2 \sum_{k=1}^\infty \rho_k$$
is the **Integrated Autocorrelation Time**. It represents the number of correlated MCMC draws required to obtain the statistical information equivalent to one independent draw. The **Effective Sample Size (ESS)** is:

$$\text{ESS} = \frac{n}{\tau_{\text{int}}} = \frac{n}{1 + 2 \sum_{k=1}^\infty \rho_k}$$

In practice, the infinite sum $\sum \rho_k$ is truncated using Geyer's initial positive sequence estimator to prevent noise accumulation from higher-order empirical autocorrelation estimates.

### 2. Rank-Normalized Split-$\hat{R}$
The classical Gelman-Rubin $\hat{R}$ diagnostic compares between-chain variance $B$ to within-chain variance $W$ across $M$ parallel chains. However, Aki Vehtari, Andrew Gelman, Daniel Simpson, Bob Carpenter, and Paul-Christian Bürkner (2021) identified two fatal flaws in classical $\hat{R}$:
1. It fails if the distribution has heavy tails or infinite variance.
2. It fails to detect within-chain non-stationarity if the chains explore different sections of the state space.

The modern **Rank-Normalized Split-$\hat{R}$** solves these deficiencies:
1. **Split-Chain Verification**: Each chain of length $n$ is split in half into two sub-chains of length $n/2$, creating $2M$ chains. This transforms within-chain drift into between-chain variance.
2. **Rank Transformation**: The pooled draws from all $2M$ chains are replaced by their normalized fractional ranks:
$$\tilde{x} = \Phi^{-1}\left( \frac{\mathrm{rank}(x) - 3/8}{N_{\text{total}} + 1/4} \right)$$
This maps the empirical draws onto standard normal quantiles, neutralizing heavy-tail outliers.
3. Compute $\hat{R}$ on the rank-transformed data:
$$\hat{R} = \sqrt{\frac{\widehat{\mathrm{Var}}^+}{W}}$$

A value of $\hat{R} \le 1.01$ indicates satisfactory mixing and chain convergence across both tails and central mass.
"""

# -------------------------------------------------------------
# UNIT 7 EXPANSION
# -------------------------------------------------------------
u7_expansion = r"""
## 7.9 Hamiltonian Monte Carlo (HMC) and Symplectic Integration

In high-dimensional parameter spaces ($d \ge 50$), Random Walk Metropolis and Gibbs sampling suffer from diffusive behavior: the distance traveled scales only as $\sqrt{n}$. To escape diffusion, Radford Neal (2011) adapted physical mechanics into **Hamiltonian Monte Carlo (HMC)**, originally introduced by Simon Duane, Anthony Kennedy, Brian Pendleton, and Duncan Roweth in 1987.

HMC translates Bayesian posterior sampling into the physical simulation of a particle sliding frictionless over a multi-dimensional energy potential.

### 1. The Hamiltonian Dynamical System
Let $\mathbf{q} \in \mathbb{R}^d$ represent the position vector (the parameters of interest), with potential energy equal to the negative unnormalized log-posterior:
$$U(\mathbf{q}) = -\log \pi(\mathbf{q})$$

We introduce fictitious auxiliary momentum variables $\mathbf{p} \in \mathbb{R}^d$, typically drawn from a multivariate Gaussian distribution $\mathbf{p} \sim \mathcal{N}(\mathbf{0}, \mathbf{M})$, where $\mathbf{M}$ is a symmetric positive-definite mass matrix. The kinetic energy is:
$$K(\mathbf{p}) = \frac{1}{2} \mathbf{p}^T \mathbf{M}^{-1} \mathbf{p}$$

The total energy of the physical system is the **Hamiltonian**:
$$H(\mathbf{q}, \mathbf{p}) = U(\mathbf{q}) + K(\mathbf{p}) = -\log \pi(\mathbf{q}) + \frac{1}{2} \mathbf{p}^T \mathbf{M}^{-1} \mathbf{p}$$

The time evolution of the system follows **Hamilton's equations of motion**:
$$\frac{d\mathbf{q}}{dt} = \frac{\partial H}{\partial \mathbf{p}} = \mathbf{M}^{-1} \mathbf{p}$$
$$\frac{d\mathbf{p}}{dt} = -\frac{\partial H}{\partial \mathbf{q}} = -\nabla U(\mathbf{q}) = \nabla \log \pi(\mathbf{q})$$

Three fundamental physical properties guarantee the validity of HMC:
1. **Conservation of Energy**: $\frac{dH}{dt} = \sum_i \left( \frac{\partial H}{\partial q_i} \frac{dq_i}{dt} + \frac{\partial H}{\partial p_i} \frac{dp_i}{dt} \right) = \sum_i \left( \frac{\partial H}{\partial q_i} \frac{\partial H}{\partial p_i} - \frac{\partial H}{\partial p_i} \frac{\partial H}{\partial q_i} \right) = 0$.
2. **Reversibility**: Negating the momentum $\mathbf{p} \to -\mathbf{p}$ reverses the trajectory precisely.
3. **Volume Preservation (Liouville's Theorem)**: The phase space flow $(\mathbf{q}(0), \mathbf{p}(0)) \mapsto (\mathbf{q}(t), \mathbf{p}(t))$ has a Jacobian determinant identically equal to $1.0$, meaning phase space volume is strictly conserved: $|\det(J)| = 1$.

### 2. The Symplectic Leapfrog Integrator
Because continuous differential equations cannot be solved analytically for arbitrary posteriors, HMC discretizes time into steps of size $\epsilon$ using the **Leapfrog Integrator**:
$$\mathbf{p}\left(t + \frac{\epsilon}{2}\right) = \mathbf{p}(t) - \frac{\epsilon}{2} \nabla U(\mathbf{q}(t))$$
$$\mathbf{q}(t + \epsilon) = \mathbf{q}(t) + \epsilon \mathbf{M}^{-1} \mathbf{p}\left(t + \frac{\epsilon}{2}\right)$$
$$\mathbf{p}(t + \epsilon) = \mathbf{p}\left(t + \frac{\epsilon}{2}\right) - \frac{\epsilon}{2} \nabla U(\mathbf{q}(t + \epsilon))$$

Unlike naive Euler integration (which spirals away due to numerical energy drift), the leapfrog integrator is **symplectic**: it exactly preserves an approximate "shadow Hamiltonian" $\tilde{H} = H + O(\epsilon^2)$.

After $L$ leapfrog steps from $(\mathbf{q}, \mathbf{p})$ to proposed state $(\mathbf{q}^*, \mathbf{p}^*)$, the Metropolis acceptance probability is:
$$\alpha = \min\left( 1, \exp\left( -H(\mathbf{q}^*, \mathbf{p}^*) + H(\mathbf{q}, \mathbf{p}) \right) \right) = \min\left( 1, \exp(-\Delta H) \right)$$
Because $\Delta H = O(\epsilon^2)$ is purely due to discretization error, $\alpha$ remains close to $1.0$ (typically tuned to $65\% - 80\%$) even across vast distances in hundreds of dimensions.

## 7.10 The No-U-Turn Sampler (NUTS) and Autonomous Tuning

While HMC overcomes random walk diffusion, its performance is sensitive to two hyperparameters: the step size $\epsilon$ and the trajectory length $L$. If $L$ is too small, the algorithm degenerates into random walk exploration. If $L$ is too large, the simulated particle loops back along its orbital trajectory, wasting expensive gradient evaluations.

Matthew D. Hoffman and Andrew Gelman (2014) introduced the **No-U-Turn Sampler (NUTS)** to automate trajectory termination.

### 1. The U-Turn Criterion
The trajectory should be terminated the instant the particle begins folding back on itself, meaning the Euclidean distance between the current position $\mathbf{q}$ and the initial position $\mathbf{q}_0$ stops increasing:

$$\frac{d}{dt} \frac{1}{2} \|\mathbf{q} - \mathbf{q}_0\|_2^2 < 0 \iff (\mathbf{q} - \mathbf{q}_0)^T \frac{d\mathbf{q}}{dt} < 0 \iff (\mathbf{q} - \mathbf{q}_0)^T \mathbf{p} < 0$$

### 2. Recursive Binary Tree Building
To preserve exact time-reversibility and detailed balance, NUTS builds a balanced binary tree by simulating leapfrog steps forward and backward in time with equal probability. If the sub-trajectories in either direction satisfy the U-turn condition:
$$(\mathbf{q}^+ - \mathbf{q}^-)^T \mathbf{p}^+ < 0 \quad \text{or} \quad (\mathbf{q}^+ - \mathbf{q}^-)^T \mathbf{p}^- < 0$$
where $\mathbf{q}^+$ and $\mathbf{q}^-$ are the leftmost and rightmost endpoints of the tree, trajectory expansion halts. A point is then sampled from the tree trajectory using progressive multinomial sampling.

### 3. Dual Averaging Step Size Adaptation
NUTS tunes step size $\epsilon$ during warmup using Yurii Nesterov's primal-dual subgradient method (**Dual Averaging**). The step size is adjusted at each iteration to match a target acceptance rate $\delta_{\text{target}}$ (typically $0.80$ in Stan and PyMC):
$$\bar{w}_{t+1} = \left( 1 - \frac{1}{t + t_0} \right) \bar{w}_t + \frac{1}{t + t_0} (\delta_{\text{target}} - \alpha_t)$$
$$\log \epsilon_{t+1} = \mu - \frac{\sqrt{t}}{\gamma} \bar{w}_{t+1}$$
This automated adaptation eliminates manual tuning, making NUTS the core computational engine of modern probabilistic programming.

## 7.11 Slice Sampling

Introduced by Radford M. Neal (2003), **Slice Sampling** provides an auxiliary variable MCMC method that samples from continuous distributions without requiring explicit proposal distribution tuning.

### 1. Univariate Slice Sampling
Let $f(x) \propto h(x)$ be an unnormalized target density. Introduce an auxiliary vertical variable $y \in \mathbb{R}$:
$$p(x, y) = \begin{cases} 1, & 0 \le y \le h(x) \\ 0, & \text{otherwise} \end{cases}$$
The marginal distribution of $x$ is:
$$\int_0^{h(x)} 1\,dy = h(x) \propto f(x)$$

Univariate slice sampling alternates between two steps:
1. **Vertical Slice Draw**: Given current state $x_0$, draw $y \sim \mathcal{U}(0, h(x_0))$. This defines a horizontal slice through the density:
$$S = \{ x \in \mathbb{R} : h(x) \ge y \}$$
2. **Horizontal Coordinate Draw**: Sample a new position $x_1$ uniformly from the horizontal slice set $S$.

### 2. Stepping-Out and Shrinkage Procedures
Because the exact boundaries of the slice $S$ cannot be determined analytically for general densities, Neal developed the **stepping-out** and **shrinkage** algorithms:
1. **Stepping-Out**: An initial interval $[L, R]$ of width $w$ is positioned randomly around $x_0$: $L = x_0 - U \cdot w$ and $R = L + w$ with $U \sim \mathcal{U}(0, 1)$. The interval is expanded outward in steps of size $w$ until both ends fall outside the slice ($h(L) < y$ and $h(R) < y$).
2. **Shrinkage**: A candidate point $x^*$ is proposed uniformly from $[L, R]$. If $h(x^*) \ge y$, $x^*$ is accepted. If $h(x^*) < y$, the candidate falls outside the slice; the interval $[L, R]$ is shrunk directly to $x^*$ (setting $L = x^*$ if $x^* < x_0$, or $R = x^*$ if $x^* > x_0$), and a new proposal is drawn from the narrowed interval.

Because rejected points immediately shrink the candidate interval, slice sampling adapts automatically to local curvature: the step size expands rapidly in flat plateaus and contracts automatically in steep ravines, achieving near-$100\%$ efficiency without tuning parameters.
"""

# -------------------------------------------------------------
# UNIT 8 EXPANSION
# -------------------------------------------------------------
u8_expansion = r"""
## 8.9 The Auxiliary Particle Filter (APF)

In Section 8.4, we examined the Sequential Importance Resampling (SIR) particle filter. While SIR is simple, it suffers from a major defect known as the "blind proposal" problem: particles $\mathbf{x}_t^{(i)}$ are propagated forward according to the state transition density $f(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(i)})$ without taking into account the newly arrived observation $\mathbf{y}_t$. If the measurement noise is small, the likelihood function $g(\mathbf{y}_t \mid \mathbf{x}_t)$ forms a narrow peak in state space. Propagating particles blindly causes almost all particles to land in regions of near-zero likelihood, triggering catastrophic particle collapse.

Michael K. Pitt and Neil Shephard (1999) solved this deficiency by inventing the **Auxiliary Particle Filter (APF)**.

### 1. The Auxiliary Joint Density
The key insight of the APF is to introduce an auxiliary index variable $k \in \{1, \dots, N\}$ that identifies which particle from time $t-1$ will be propagated forward to generate state $\mathbf{x}_t$. The joint target distribution of the pair $(k, \mathbf{x}_t)$ conditional on $\mathbf{y}_{1:t}$ is:

$$p(k, \mathbf{x}_t \mid \mathbf{y}_{1:t}) \propto g(\mathbf{y}_t \mid \mathbf{x}_t) f(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k)}) w_{t-1}^{(k)}$$

Instead of sampling from this intractable joint density directly, the APF samples from an auxiliary proposal distribution:
$$q(k, \mathbf{x}_t \mid \mathbf{y}_{1:t}) = q(k \mid \mathbf{y}_{1:t}) q(\mathbf{x}_t \mid k, \mathbf{y}_{1:t})$$

### 2. Pre-Weighting and Lookahead
To construct $q(k \mid \mathbf{y}_{1:t})$, the APF computes a deterministic point estimate $\boldsymbol{\mu}_t^{(k)}$ of the future state given $\mathbf{x}_{t-1}^{(k)}$ (such as the conditional mean $\boldsymbol{\mu}_t^{(k)} = \mathbb{E}[\mathbf{X}_t \mid \mathbf{x}_{t-1}^{(k)}]$ or the mode). The first-stage auxiliary weights are defined as:

$$\lambda_k \propto w_{t-1}^{(k)} g(\mathbf{y}_t \mid \boldsymbol{\mu}_t^{(k)}), \quad k = 1, \dots, N$$

The auxiliary weights $\lambda_k$ act as a predictive lookahead: particles whose predicted future states are consistent with the new observation $\mathbf{y}_t$ receive large auxiliary weights, while particles that would produce low likelihood are pruned **before** state propagation occurs.

### 3. Two-Stage APF Algorithm
1. **Auxiliary Selection**: Resample indices $k_1, \dots, k_N$ from $\{1, \dots, N\}$ with probabilities proportional to $\lambda_k$.
2. **State Propagation**: For each selected index $k_i$, draw the candidate state:
$$\mathbf{x}_t^{(i)} \sim q(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k_i)}, \mathbf{y}_t)$$
3. **Weight Correction**: Assign the second-stage importance weights:
$$\tilde{w}_t^{(i)} = \frac{g(\mathbf{y}_t \mid \mathbf{x}_t^{(i)}) f(\mathbf{x}_t^{(i)} \mid \mathbf{x}_{t-1}^{(k_i)})}{g(\mathbf{y}_t \mid \boldsymbol{\mu}_t^{(k_i)}) q(\mathbf{x}_t^{(i)} \mid \mathbf{x}_{t-1}^{(k_i)}, \mathbf{y}_t)}$$
When $q(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k_i)}) = f(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k_i)})$, the weight simplifies to:
$$\tilde{w}_t^{(i)} = \frac{g(\mathbf{y}_t \mid \mathbf{x}_t^{(i)})}{g(\mathbf{y}_t \mid \boldsymbol{\mu}_t^{(k_i)})}$$

Because $\mathbf{x}_t^{(i)}$ is close to $\boldsymbol{\mu}_t^{(k_i)}$, the ratio $\tilde{w}_t^{(i)}$ is nearly constant, keeping the Effective Sample Size close to $N$ and eliminating weight variance even in highly informative measurement regimes.

## 8.10 Approximate Bayesian Computation (ABC) and Likelihood-Free Inference

In evolutionary genomics, complex queueing networks, ecology, and agent-based macroeconomics, the underlying scientific forward simulation model can easily generate synthetic data $\mathbf{x} \sim p(\mathbf{x} \mid \boldsymbol{\theta})$, but the analytical likelihood function:
$$p(\mathbf{y} \mid \boldsymbol{\theta}) = \int p(\mathbf{y}, \mathbf{z} \mid \boldsymbol{\theta})\,d\mathbf{z}$$
involves integrating over millions of unobserved latent variables $\mathbf{z}$, rendering the likelihood completely intractable. 

**Approximate Bayesian Computation (ABC)** enables exact or approximate Bayesian inference using exclusively forward stochastic simulations.

### 1. The Rejection ABC Algorithm
Let $\mathbf{y}_{\text{obs}}$ be the observed dataset. Rejection ABC proceeds as follows:
1. Sample candidate parameter vector $\boldsymbol{\theta}^* \sim p(\boldsymbol{\theta})$ from the prior.
2. Simulate a synthetic dataset $\mathbf{x}^* \sim p(\mathbf{x} \mid \boldsymbol{\theta}^*)$ using the forward simulator.
3. Compute a vector of summary statistics $S(\mathbf{x}^*)$ and compare it to the observed summary statistics $S(\mathbf{y}_{\text{obs}})$ using a distance metric $\rho(\cdot, \cdot)$:
$$d = \rho\left( S(\mathbf{x}^*), S(\mathbf{y}_{\text{obs}}) \right)$$
4. Accept $\boldsymbol{\theta}^*$ if $d \le \epsilon$; otherwise, reject.

*Theorem (Rubin 1984, Tavare et al. 1997)*: If $S(\cdot)$ is a vector of sufficient statistics for $\boldsymbol{\theta}$ and the tolerance threshold $\epsilon \to 0$, the accepted draws sample exactly from the true posterior distribution $p(\boldsymbol{\theta} \mid \mathbf{y}_{\text{obs}})$.

### 2. Sequential Monte Carlo ABC (ABC-SMC)
In practice, setting $\epsilon$ small results in an acceptance rate near zero under standard rejection ABC. Tina Toni, David Welch, Natalja Strelkowa, Andreas Ipsen, and Michael P. H. Stumpf (2009) formulated **ABC-SMC**, which propagates a population of particles through a decaying sequence of tolerance thresholds $\epsilon_1 > \epsilon_2 > \dots > \epsilon_T$:
1. At population iteration $t = 1$, obtain particles using standard rejection ABC with broad tolerance $\epsilon_1$.
2. For subsequent stages $t = 2, \dots, T$:
   - Sample a particle $\boldsymbol{\theta}^*$ from the previous population $t-1$ with weights $w_{t-1}^{(i)}$.
   - Perturb the particle using a transition kernel: $\boldsymbol{\theta}^{**} \sim K_t(\boldsymbol{\theta} \mid \boldsymbol{\theta}^*)$.
   - Simulate synthetic data $\mathbf{x} \sim p(\mathbf{x} \mid \boldsymbol{\theta}^{**})$.
   - If $\rho(S(\mathbf{x}), S(\mathbf{y}_{\text{obs}})) \le \epsilon_t$, accept $\boldsymbol{\theta}^{**}$ and compute its updated importance weight:
$$w_t^{(i)} = \frac{p(\boldsymbol{\theta}^{**})}{\sum_{j=1}^N w_{t-1}^{(j)} K_t(\boldsymbol{\theta}^{**} \mid \boldsymbol{\theta}_{t-1}^{(j)})}$$
ABC-SMC maintains high acceptance rates across orders-of-magnitude reductions in $\epsilon$, providing an industrial-strength engine for simulator calibration.

## 8.11 Simulation-Based Inference (SBI) and Normalizing Flows

Over the past decade, the interface between machine learning and computational statistics has generated **Simulation-Based Inference (SBI)**, replacing heuristic summary statistic distances with deep neural density estimators.

Prominent modern SBI paradigms include:
1. **Neural Posterior Estimation (NPE)**: Trains a continuous Normalizing Flow $q_\phi(\boldsymbol{\theta} \mid \mathbf{y})$ (such as Masked Autoregressive Flow or RealNVP) by minimizing the expected Kullback-Leibler divergence over synthetic parameter-data pairs $(\boldsymbol{\theta}_i, \mathbf{x}_i) \sim p(\boldsymbol{\theta}) p(\mathbf{x} \mid \boldsymbol{\theta})$:
$$\mathcal{L}(\phi) = -\sum_{i=1}^N \log q_\phi(\boldsymbol{\theta}_i \mid \mathbf{x}_i)$$
Once trained, the normalizing flow amortizes posterior inference: evaluating $q_\phi(\boldsymbol{\theta} \mid \mathbf{y}_{\text{obs}})$ generates millions of independent posterior draws in milliseconds without running any further simulations.
2. **Neural Likelihood Estimation (NLE)**: Trains a neural density estimator $q_\psi(\mathbf{x} \mid \boldsymbol{\theta})$ to approximate the intractable simulator likelihood directly, which is subsequently embedded into standard MCMC or HMC samplers to obtain exact Bayesian posteriors.
"""

def main():
    append_to_unit(1, u1_expansion)
    append_to_unit(2, u2_expansion)
    append_to_unit(3, u3_expansion)
    append_to_unit(4, u4_expansion)
    append_to_unit(5, u5_expansion)
    append_to_unit(6, u6_expansion)
    append_to_unit(7, u7_expansion)
    append_to_unit(8, u8_expansion)
    print("All 8 units expanded successfully.")

if __name__ == "__main__":
    main()
