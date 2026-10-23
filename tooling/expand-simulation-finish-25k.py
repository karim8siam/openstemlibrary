#!/usr/bin/env python3
"""
Final expansion pass for Statistical Simulation and Monte Carlo Methods
to firmly push the substantive prose word count past 25,500 words across all 8 units.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} finalized.")

# -------------------------------------------------------------
# UNIT 1 FINAL
# -------------------------------------------------------------
u1_final = r"""
## 1.14 Hardware Random Number Generators and NIST SP 800-90 Standards

In mission-critical statistical simulations, military modeling, and regulatory lottery systems, purely algorithmic pseudo-random number generators are coupled with or verified against **True Random Number Generators (TRNGs)**. TRNGs harvest entropy from fundamental microscopic quantum or thermal physical processes that are ontologically non-deterministic according to the laws of modern physics.

### 1. Physical Entropy Harvesting Mechanisms
Hardware TRNG devices convert physical analog noise into discrete binary digits using three primary mechanisms:
1. **Thermal Johnson-Nyquist Noise**: The random thermal agitation of charge carriers inside an electrical conductor or resistor at non-zero temperature $T$. The mean-square noise voltage across bandwidth $\Delta f$ is given by:
$$\overline{v_n^2} = 4 k_B T R \, \Delta f$$
where $k_B$ is the Boltzmann constant, $T$ is absolute temperature, and $R$ is resistance. Amplifying and sampling this continuous voltage waveform produces unpredictable noise bits.
2. **Avalanche Breakdown in Zener Diodes**: Operating a reverse-biased semiconductor $p$-$n$ junction in its breakdown avalanche regime generates quantum shot noise as charge carriers multiply via impact ionization.
3. **Ring Oscillator Phase Jitter**: Linking an odd number of inverter gates in a closed loop creates an autonomous clock whose phase drifts unpredictably due to localized thermal fluctuations and transistor switching noise. By sampling a high-frequency jittery ring oscillator with a slower stable reference clock, unpredictable transition bits are captured.

### 2. Conditioning and NIST SP 800-90A/B Architecture
Raw physical noise is rarely uniformly distributed: thermal drift, ambient temperature shifts, and circuit component asymmetry introduce substantial DC bias ($P(1) \ne 0.5$) and serial autocorrelation. To transform raw physical entropy into uniform, independent random bits, raw bits must pass through a **Conditioning Component** as specified by the National Institute of Standards and Technology (NIST) Special Publication 800-90B:
- **Von Neumann De-biasing**: Takes pairs of non-overlapping raw bits $(b_1, b_2)$. If the pair is $01$, output $0$; if $10$, output $1$; if $00$ or $11$, discard the pair entirely. Because $P(01) = P(0) P(1) = P(10) = P(1) P(0)$ under independence, the output stream is guaranteed to have zero bias ($P(0) = P(1) = 0.5$), though roughly $75\%$ of raw throughput is discarded.
- **Cryptographic Hash Conditioning**: Blocks of raw physical bits are processed through cryptographic sponge functions (such as SHA-3/Keccak or AES-CBC-MAC). The compression guarantees that the min-entropy of the output is strictly bounded and distributed uniformly over $\{0, 1\}^m$.

In high-performance hybrid architectures, hardware TRNGs provide continuous asynchronous seed re-keying into user-space CSPRNG algorithms, ensuring that simulations maintain multi-gigahertz throughput with genuine physical unpredictability.
"""

# -------------------------------------------------------------
# UNIT 2 FINAL
# -------------------------------------------------------------
u2_final = r"""
## 2.14 The Ziggurat Algorithm for Ultra-Fast Continuous Sampling

While the Box-Muller transform and the polar method generate standard Gaussian variates effectively, both algorithms require evaluating expensive transcendental functions: Box-Muller computes square roots, natural logarithms, and trigonometric sines and cosines, consuming dozens of clock cycles per generated pair.

George Marsaglia and Wai Wan Tsang (2000) introduced the **Ziggurat Algorithm**, which generates continuous random variates (particularly standard Normal and Exponential variables) using almost exclusively table lookups and integer comparisons, executing in fewer than 10 CPU clock cycles on modern hardware.

### 1. Geometric Construction of the Ziggurat
Let $f(x)$ be a monotonically decreasing probability density function on $[0, \infty)$ (such as the positive half of the standard normal density $f(x) = \sqrt{2/\pi} e^{-x^2/2}$).

The area under $f(x)$ is partitioned into $M$ horizontal rectangular slices (typically $M = 256$, fitting into an 8-bit index). Slices are indexed $i = 0, 1, \dots, M-1$ from bottom to top:
- Each rectangular layer $i$ extends horizontally from $0$ to $x_i$ and vertically from $y_{i-1}$ to $y_i = f(x_i)$.
- Crucially, the endpoints $x_i$ are precomputed such that **every layer has identical area $V$**:
$$V = x_i (y_i - y_{i-1}) = x_{M-1} (1 - y_{M-2}) = \text{constant}$$
The bottom slice $i = 0$ is special: it consists of a central rectangle of width $x_0$ and height $y_0 = f(x_0)$, plus an infinite right-hand tail $T = \int_{x_0}^\infty f(x)\,dx$ such that the combined area equals $V$.

Because the layers have equal area $V$, selecting a layer $i$ uniformly at random from $\{0, 1, \dots, M-1\}$ gives an exact equiprobable mixture.

### 2. The Rapid Sampling Loop
To generate a standard normal variate:
1. Generate an independent 32-bit random integer $J$.
2. Extract the lower 8 bits of $J$ to select layer index $i \in \{0, \dots, 255\}$.
3. Use the remaining 24 bits of $J$ (converted to a uniform fraction $U \in [0, 1)$) to propose a horizontal coordinate:
$$X = U \cdot x_i$$
4. **Fast Interior Acceptance Test**: If $X < x_{i+1}$, the proposed point lies strictly inside the core interior of the ziggurat layer (underneath the density curve). Accept $X$ immediately!
5. **Slow Boundary Test**: If $X \ge x_{i+1}$, the proposed point falls in the outer margin near the density boundary. Only then does the algorithm evaluate:
$$Y = y_{i-1} + U_2 \cdot (y_i - y_{i-1})$$
If $Y \le f(X)$, accept $X$; otherwise, reject and repeat.
6. **Tail Draw**: If layer $i = 0$ was selected and $X \ge x_0$, sample directly from the tail using Robert's transformed exponential tail algorithm.

Because $M = 256$ slices provide an exceptionally tight stepped approximation to the smooth Gaussian curve, the fast interior acceptance test in Step 4 succeeds **over $98.5\%$ of the time**. The ziggurat algorithm avoids transcendental evaluations on $98.5\%$ of all generated variates, making it the fastest known algorithm for standard continuous distributions.
"""

# -------------------------------------------------------------
# UNIT 3 FINAL
# -------------------------------------------------------------
u3_final = r"""
## 3.15 Permutation Tests vs. Bootstrap Resampling: An Epistemological Comparison

In non-parametric inference, computational statisticians frequently choose between two prominent computer-intensive resampling methodologies: **Permutation Tests** (Randomization Tests) and the **Bootstrap**. While both methods liberate the analyst from rigid parametric Gaussian assumptions, their mathematical structures, null hypotheses, and exchangeability assumptions are fundamentally distinct.

### 1. Permutation Tests and the Exchangeability Criterion
Developed conceptually by Ronald A. Fisher (1935) and formalized by E. J. G. Pitman (1937), permutation tests assess null hypotheses by evaluating how frequently an observed test statistic occurs under all possible relabelings of the data.

Consider a two-sample comparison: sample 1 has observations $X_1, \dots, X_{n_1}$ from distribution $F_X$, and sample 2 has observations $Y_1, \dots, Y_{n_2}$ from distribution $F_Y$. The null hypothesis is identity of distributions:
$$H_0: F_X = F_Y$$
Under $H_0$, the assignment of observations to treatment or control is an arbitrary label. The pooled vector of observations $\mathbf{Z} = (X_1, \dots, X_{n_1}, Y_1, \dots, Y_{n_2})$ of size $N = n_1 + n_2$ satisfies **Exchangeability**: every permutation $\pi \in \mathcal{S}_N$ of the indices is equally probable under the null measure.

The exact two-sided $p$-value is:
$$p = \frac{1}{N!} \sum_{\pi \in \mathcal{S}_N} \mathbb{I}(|T(\mathbf{Z}_\pi)| \ge |T_{\text{obs}}|)$$
When $N$ is moderately large, evaluating all $N!$ or $\binom{N}{n_1}$ permutations is computationally impossible. A **Monte Carlo Permutation Test** draws $B$ random permutations uniformly from $\mathcal{S}_N$:
$$\hat{p} = \frac{1 + \sum_{b=1}^B \mathbb{I}(|T(\mathbf{Z}_{\pi_b})| \ge |T_{\text{obs}}|)}{1 + B}$$
The inclusion of $+1$ in numerator and denominator guarantees that $\hat{p}$ is a strictly valid $p$-value under $H_0$, with Type I error rate $P(\hat{p} \le \alpha) \le \alpha$ for any sample size $N$ and any number of simulation draws $B$.

### 2. Methodological Differences
<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Feature / Property</th>
<th>Permutation Testing (Randomization)</th>
<th>Bootstrap Resampling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Primary Purpose</strong></td>
<td>Hypothesis testing ($p$-values, significance decisions).</td>
<td>Parameter estimation, standard errors, confidence intervals.</td>
</tr>
<tr>
<td><strong>Sampling Mechanism</strong></td>
<td>Sampling <em>without replacement</em> from the pooled data.</td>
<td>Sampling <em>with replacement</em> from the observed sample.</td>
</tr>
<tr>
<td><strong>Underlying Assumption</strong></td>
<td>Exchangeability under the sharp null hypothesis ($F_X = F_Y$).</td>
<td>Observations are i.i.d. draws from true population $F$.</td>
</tr>
<tr>
<td><strong>Finite-Sample Validity</strong></td>
<td>Exact test. Type I error is strictly controlled at $\alpha$ for any $N$.</td>
<td>Asymptotic test. Confidence interval coverage error is $O(n^{-1/2})$ or $O(n^{-1})$.</td>
</tr>
<tr>
<td><strong>Generalizability</strong></td>
<td>Restricted: cannot easily test non-sharp hypotheses (e.g., $H_0: \mu_X - \mu_Y = 0$ when $\sigma_X^2 \ne \sigma_Y^2$).</td>
<td>Broad: applies to almost any estimable functional $\theta = T(F)$.</td>
</tr>
</tbody>
</table>
</div>

Permutation tests represent the gold standard when testing sharp null hypotheses under randomized experimental designs, whereas bootstrap resampling is the premier computational technology for constructing confidence intervals for complex estimators.
"""

# -------------------------------------------------------------
# UNIT 4 FINAL
# -------------------------------------------------------------
u4_final = r"""
## 4.13 Splitting Methods and the RESTART Algorithm for Rare-Event Estimation

In reliability engineering, telecommunications network buffering, and nuclear safety verification, simulation models must quantify the probability of catastrophic failure events occurring with probability $p \le 10^{-9}$. Crude Monte Carlo requires $n \approx 10^{11}$ runs to record 100 failure events, demanding years of supercomputer time.

While Importance Sampling provides one route to variance reduction, finding an effective proposal density $g(\mathbf{x})$ in high-dimensional dynamic network systems is often impossible. **Multilevel Splitting**, originally conceived by Herman Kahn and Theodore E. Harris (1951) and refined into the **RESTART** (Repetitive Simulation Trials After Reaching Thresholds) method by Manuel Villén-Altamirano et al. (1991), provides a powerful alternative that requires zero analytical knowledge of likelihood functions.

### 1. Nested Threshold Decomposition
Let $S(\mathbf{X}_t)$ be a continuous importance function or "score" measuring the proximity of system state $\mathbf{X}_t$ to the failure domain $\mathcal{F} = \{ \mathbf{x} : S(\mathbf{x}) \ge \gamma_M \}$. 

The continuous state space is partitioned by a sequence of nested intermediate thresholds:
$$\gamma_0 < \gamma_1 < \gamma_2 < \dots < \gamma_M$$
Define intermediate events $E_k = \{ \max_{0 \le t \le T} S(\mathbf{X}_t) \ge \gamma_k \}$, such that $E_M = \mathcal{F}$ and $E_M \subset E_{M-1} \subset \dots \subset E_1$.

By the definition of conditional probability, the target rare-event probability factors into a product of conditional transition probabilities:
$$P(\mathcal{F}) = P(E_M) = P(E_1) \prod_{k=2}^M P(E_k \mid E_{k-1})$$

The thresholds $\gamma_k$ are chosen such that each conditional probability is comfortably large:
$$p_k = P(E_k \mid E_{k-1}) \approx 0.10 \quad \text{for all } k$$
Estimating ten conditional probabilities of magnitude $0.10$ requires only thousands of simulation draws per level, transforming an intractable $10^{-10}$ estimation problem into a series of easily solvable sub-problems.

### 2. The Splitting Mechanism
The algorithm executes iteratively across the threshold levels:
1. **Level 1**: Generate $N$ independent trajectories from the system initial state. Record the trajectories that successfully cross threshold $\gamma_1$. Let the empirical success fraction be $\hat{p}_1 = N_1 / N$.
2. **Branching (Splitting)**: For each trajectory that reached $\gamma_1$, split the process into $R$ cloned sub-trajectories starting from the exact state $\mathbf{X}_{\tau_1}$ at the threshold-crossing time $\tau_1$.
3. **Independent Continuation**: Propagate each cloned sub-trajectory forward independently using fresh random numbers. Record the fraction of clones that successfully cross the next threshold $\gamma_2$:
$$\hat{p}_2 = \frac{N_2}{R \cdot N_1}$$
4. Repeat the branching and propagation steps at each intermediate boundary until the failure domain $\gamma_M$ is reached.

The grand estimator of the failure probability is:
$$\widehat{P}(\mathcal{F}) = \prod_{k=1}^M \hat{p}_k$$
P. L'Ecuyer, F. Le Gland, and B. Tuffin (2007) proved that with optimal threshold spacing and clone branching ratios $R_k \approx 1 / p_k$, the computational effort scales as:
$$\text{Cost} = O\left( (\log P(\mathcal{F}))^2 \right)$$
rather than the exponential scaling $O(1 / P(\mathcal{F}))$ of Crude Monte Carlo, enabling routine estimation of events with probabilities as small as $10^{-50}$.
"""

# -------------------------------------------------------------
# UNIT 5 FINAL
# -------------------------------------------------------------
u5_final = r"""
## 5.13 Regularized Multi-Response Control Variates

In large-scale risk simulations and derivative portfolio valuations, analysts frequently possess dozens or hundreds of candidate control variates $\mathbf{Y} = (Y_1, \dots, Y_P)^T$ with known expectations $\mathbb{E}[\mathbf{Y}] = \boldsymbol{\mu}_Y$. The multi-control estimator is:

$$\hat{\theta}_{\mathbf{c}} = \bar{X} - \mathbf{c}^T (\bar{\mathbf{Y}} - \boldsymbol{\mu}_Y)$$

When the number of controls $P$ is large relative to the simulation sample size $n$, estimating the optimal control vector $\mathbf{c}^* = \mathbf{\Sigma}_{YY}^{-1} \mathbf{\Sigma}_{YX}$ via ordinary least squares incurs severe sample estimation error, causing the variance of the controlled estimator to inflate due to loss of degrees of freedom.

### 1. Degree of Freedom Loss in OLS Control Variates
Lavenberg and Welch (1981) established that when $\mathbf{c}^*$ is estimated from the same simulation sample using sample covariance matrices, the variance of the controlled estimator satisfies:

$$\mathrm{Var}(\hat{\theta}_{\hat{\mathbf{c}}}) = \frac{\sigma^2 (1 - R^2)}{n} \left( \frac{n - 2}{n - P - 2} \right)$$
where $R^2 = \mathbf{\Sigma}_{YX}^T \mathbf{\Sigma}_{YY}^{-1} \mathbf{\Sigma}_{YX} / \sigma^2$ is the squared population multiple correlation coefficient.

The factor $\frac{n - 2}{n - P - 2}$ represents the **Estimation Penalty**: if $P$ is large (e.g., $P = 50$ controls with $n = 100$ draws), the penalty is $\frac{98}{46} \approx 2.13$, doubling the simulation variance and completely erasing the variance reduction gained from $R^2$.

### 2. Ridge and Lasso Penalized Control Variates
To solve the high-dimensional control variate problem, modern statistical simulation incorporates regularization from shrinkage regression:

1. **Ridge Control Variates**: Introduces an $L_2$ penalty on the coefficient vector:
$$\mathbf{c}_{\text{ridge}} = \left( \mathbf{S}_{YY} + \lambda \mathbf{I}_P \right)^{-1} \mathbf{S}_{YX}$$
where $\mathbf{S}_{YY}$ is the sample covariance matrix and $\lambda > 0$ is a tuning parameter selected via cross-validation. Ridge regularization stabilizes matrix inversion when candidate controls are collinear (such as option payoffs evaluated across adjacent strikes).
2. **Lasso Control Variates**: Solves the penalized optimization:
$$\mathbf{c}_{\text{lasso}} = \arg\min_{\mathbf{c}} \left\{ \frac{1}{n} \sum_{i=1}^n \left( X_i - \bar{X} - \mathbf{c}^T (\mathbf{Y}_i - \boldsymbol{\mu}_Y) \right)^2 + \lambda \sum_{j=1}^P |c_j| \right\}$$
The $L_1$ penalty enforces sparsity: the algorithm automatically selects the sparse subset of auxiliary variables that provide genuine explanatory power for $X$, setting non-contributing control weights to zero and preventing degree-of-freedom degradation.
"""

# -------------------------------------------------------------
# UNIT 6 FINAL
# -------------------------------------------------------------
u6_final = r"""
## 6.13 Trans-Dimensional MCMC and Reversible Jump (RJMCMC)

In many scientific modeling challenges, the dimension of the parameter space itself is an unknown random variable. Examples include:
- Variable selection in regression: how many and which covariates should be included?
- Gaussian mixture modeling: how many mixture components $K \in \{1, 2, \dots, K_{\max}\}$ best explain the data?
- Change-point analysis: how many structural breaks occurred in an economic time series?

Let $\mathcal{M}_k$ denote a model indexed by $k \in \mathcal{K}$, where model $k$ possesses parameter vector $\boldsymbol{\theta}_k \in \mathbb{R}^{d_k}$. The state space of the Markov chain is the union of spaces of varying dimensions:
$$\Omega = \bigcup_{k \in \mathcal{K}} \left( \{k\} \times \mathbb{R}^{d_k} \right)$$

Standard Metropolis-Hastings fails because the target distribution has support on spaces of differing Lebesgue measures; moving between spaces of different dimensions causes the transition Jacobian to become non-square.

Peter J. Green (1995) formulated **Reversible Jump Markov Chain Monte Carlo (RJMCMC)**, solving trans-dimensional simulation by enforcing dimension matching.

### 1. Dimension Matching and the Auxiliary Random Vector
Suppose the chain is at state $(k, \boldsymbol{\theta})$ of dimension $d_k$, and proposes a jump to model $(k^*, \boldsymbol{\theta}^*)$ of dimension $d_{k^*}$ (assume without loss of generality that $d_{k^*} > d_k$).

To make the jump mathematically reversible, Green introduced an auxiliary random vector $\mathbf{u} \sim q(\mathbf{u})$ of dimension $d_u$ such that the total dimensions match:
$$d_k + d_u = d_{k^*} + d_{u^*}$$
where $\mathbf{u}^*$ is an auxiliary vector generated when proposing the reverse move.

A deterministic, invertible, differentiable mapping $g$ is constructed:
$$(\boldsymbol{\theta}^*, \mathbf{u}^*) = g(\boldsymbol{\theta}, \mathbf{u})$$
Because $g$ is a diffeomorphism between spaces of equal dimension, the transformation possesses a well-defined square Jacobian matrix:
$$\mathbf{J} = \frac{\partial g(\boldsymbol{\theta}, \mathbf{u})}{\partial (\boldsymbol{\theta}, \mathbf{u})} = \begin{pmatrix} \frac{\partial \boldsymbol{\theta}^*}{\partial \boldsymbol{\theta}} & \frac{\partial \boldsymbol{\theta}^*}{\partial \mathbf{u}} \\ \frac{\partial \mathbf{u}^*}{\partial \boldsymbol{\theta}} & \frac{\partial \mathbf{u}^*}{\partial \mathbf{u}} \end{pmatrix}$$

### 2. The Reversible Jump Acceptance Probability
*Theorem (Green 1995)*: The detailed balance condition across models is satisfied if the acceptance probability for jumping from $(k, \boldsymbol{\theta})$ to $(k^*, \boldsymbol{\theta}^*)$ is:

$$\alpha = \min\left( 1, \underbrace{\frac{p(k^*, \boldsymbol{\theta}^* \mid \mathbf{y})}{p(k, \boldsymbol{\theta} \mid \mathbf{y})}}_{\text{Posterior Ratio}} \times \underbrace{\frac{j(k^* \to k)}{j(k \to k^*)}}_{\text{Model Proposal Ratio}} \times \underbrace{\frac{q^*(\mathbf{u}^*)}{q(\mathbf{u})}}_{\text{Auxiliary Proposal Ratio}} \times \underbrace{|\det(\mathbf{J})|}_{\text{Jacobian Determinant}} \right)$$

where $j(k \to k^*)$ is the probability of proposing a model jump from $k$ to $k^*$.

The inclusion of the Jacobian determinant $|\det(\mathbf{J})|$ accounts precisely for the expansion or contraction of phase space volume during the dimension-changing transformation, ensuring that RJMCMC samples from the exact joint posterior distribution over both model space and parameter spaces.
"""

# -------------------------------------------------------------
# UNIT 7 FINAL
# -------------------------------------------------------------
u7_final = r"""
## 7.13 Coupling from the Past (CFTP) and Perfect Simulation

In standard MCMC simulation, the practitioner faces an insurmountable theoretical obstacle: the Markov chain only converges to the stationary distribution $\pi$ asymptotically as $n \to \infty$. In any finite simulation of $N$ steps, the distribution of state $X_N$ is only approximately equal to $\pi$, and determining the exact warmup time required to render the remaining bias negligible is notoriously difficult.

James G. Propp and David B. Wilson (1996) shocked the probability community by inventing **Coupling from the Past (CFTP)**, an algorithm that generates **exact, unbiased, perfect draws** from the stationary distribution $\pi$ of a Markov chain in finite computational time.

### 1. Monotonicity and the Coalescence Criterion
Consider a discrete or continuous state space $\mathcal{X}$ equipped with a partial order $\preceq$, with unique minimum element $\hat{0}$ and maximum element $\hat{1}$ (such as the Ising model of ferromagnetic spins on a lattice).

Suppose the Markov transition update can be represented by a deterministic update function $\phi: \mathcal{X} \times \mathcal{U} \to \mathcal{X}$ driven by independent uniform random numbers $U_t \sim \mathcal{U}$:
$$X_{t+1} = \phi(X_t, U_t)$$
The update function is said to be **monotone** if:
$$x \preceq y \implies \phi(x, u) \preceq \phi(y, u) \quad \forall u \in \mathcal{U}$$

### 2. Why Running Forward Fails vs. Coupling From the Past
If one starts two Markov chains at time $t = 0$ from different states and runs them forward until they meet (coalesce) at time $T$, the distribution at coalescence time $T$ is **biased**: stopping at the random time $T$ selects for trajectories that coalesce rapidly, violating stationarity.

Propp and Wilson realized that the coalescence must occur at fixed time $t = 0$ by starting chains in the infinite past:
1. Fix observation time $t = 0$.
2. Choose a starting time in the past $T_1 = -1$.
3. Run chains starting from **all possible states** $x \in \mathcal{X}$ from time $T_1$ up to $t = 0$, using the random sequence $(U_{-1})$.
4. If all trajectories coalesce into a single state at $t = 0$, output that common state $X_0$.
5. If trajectories have not coalesced, double the starting horizon: $T_2 = -2, -4, -8, \dots, -2^k$.
6. **Crucial Coupling Principle**: When restarting from $T_{k+1} = -2^{k+1}$, one **must reuse the exact same random numbers** $U_t$ that were used previously for $t \in [-2^k, 0)$. Only new random numbers are drawn for the extended interval $[-2^{k+1}, -2^k)$.

*The Sandwiching Property*: Thanks to monotonicity, one does not need to simulate trajectories from all $2^N$ possible states: one only simulates the two extreme chains starting from $\hat{0}$ and $\hat{1}$. If the top chain and bottom chain coalesce by time $t = 0$:
$$X_0^{\hat{0}} = X_0^{\hat{1}} = X_0$$
then every intermediate chain is squeezed between them and must also have coalesced to $X_0$.

*Theorem (Propp-Wilson)*: The coalesced state $X_0$ is distributed **exactly according to the stationary measure $\pi$**, with zero burn-in bias and zero approximation error.
"""

# -------------------------------------------------------------
# UNIT 8 FINAL
# -------------------------------------------------------------
u8_final = r"""
## 8.13 The Ensemble Kalman Filter (EnKF) for Massive Geophysical Data Assimilation

In numerical weather prediction, oceanography, and atmospheric monitoring, dynamic state vectors represent temperature, atmospheric pressure, and wind velocities across three-dimensional spatial grids, with state dimensions reaching $d \approx 10^8$ to $10^9$. In this ultra-high-dimensional regime, standard particle filters collapse instantly due to particle degeneracy, while classical Kalman filters cannot store or invert the $10^9 \times 10^9$ error covariance matrix.

Geir Evensen (1994) introduced the **Ensemble Kalman Filter (EnKF)**, combining Monte Carlo ensemble forecasting with Kalman update geometry to make global data assimilation computationally feasible.

### 1. The Stochastic Forecast and Analysis Cycle
The EnKF represents the probability distribution of the high-dimensional state $\mathbf{x}_t \in \mathbb{R}^d$ through an ensemble of $N$ model states (typically $N \approx 50$ to $100$):
$$\mathbf{X} = [\mathbf{x}^{(1)}, \mathbf{x}^{(2)}, \dots, \mathbf{x}^{(N)}] \in \mathbb{R}^{d \times N}$$

1. **Forecast Step**: Each ensemble member is integrated forward in time through the non-linear forward geophysical simulation model $\mathcal{M}$:
$$\mathbf{x}_{t|t-1}^{(i)} = \mathcal{M}(\mathbf{x}_{t-1|t-1}^{(i)}) + \boldsymbol{\eta}_t^{(i)}, \quad i = 1, \dots, N$$
The ensemble mean $\bar{\mathbf{x}}$ and ensemble perturbation matrix $\mathbf{A} = \mathbf{X} - \bar{\mathbf{x}} \mathbf{1}^T$ define an implicit low-rank sample covariance matrix:
$$\mathbf{P}^f = \frac{1}{N-1} \mathbf{A} \mathbf{A}^T$$
Crucially, $\mathbf{P}^f$ is never explicitly formed in memory.

2. **Perturbed Observation Analysis Step**: Let $\mathbf{y}_t \in \mathbb{R}^p$ be the newly arrived satellite observation vector with measurement error covariance $\mathbf{R}$. To preserve proper ensemble spread, independent random perturbations are added to the observation vector for each member (Burgers et al. 1998):
$$\mathbf{y}_t^{(i)} = \mathbf{y}_t + \boldsymbol{\epsilon}^{(i)}, \quad \boldsymbol{\epsilon}^{(i)} \sim \mathcal{N}(\mathbf{0}, \mathbf{R})$$
The analysis update for member $i$ is:
$$\mathbf{x}_{t|t}^{(i)} = \mathbf{x}_{t|t-1}^{(i)} + \mathbf{K} \left( \mathbf{y}_t^{(i)} - \mathbf{H} \mathbf{x}_{t|t-1}^{(i)} \right)$$
where the Kalman gain matrix $\mathbf{K}$ is computed directly in the low-dimensional observation space:
$$\mathbf{K} = \mathbf{P}^f \mathbf{H}^T \left( \mathbf{H} \mathbf{P}^f \mathbf{H}^T + \mathbf{R} \right)^{-1}$$

### 2. Covariance Localization and Inflation
Because the ensemble size $N \approx 100$ is astronomically smaller than the state dimension $d \approx 10^8$, the sample covariance $\mathbf{P}^f$ suffers from two critical sampling artifacts:
1. **Spurious Long-Range Correlations**: Small random correlations appear between physically distant geographic locations (e.g., surface temperature in Paris and rainfall in the South Pacific). **Covariance Localization** applies a Schur (element-wise) product with a compact smooth spatial correlation function $\boldsymbol{\rho}$:
$$\mathbf{P}_{\text{loc}}^f = \boldsymbol{\rho} \circ \mathbf{P}^f$$
forcing correlations between distant grid points to zero.
2. **Filter Divergence (Inbreeding)**: Because the ensemble systematically underestimates forecast error variance, the filter progressively ignores new incoming observations. **Covariance Inflation** multiplies the perturbation matrix by an inflation factor $\lambda > 1$:
$$\mathbf{A}_{\text{infl}} = \lambda \mathbf{A}$$
restoring realistic ensemble spread and ensuring stable, continuous tracking of planetary weather dynamics.
"""

def main():
    append_to_unit(1, u1_final)
    append_to_unit(2, u2_final)
    append_to_unit(3, u3_final)
    append_to_unit(4, u4_final)
    append_to_unit(5, u5_final)
    append_to_unit(6, u6_final)
    append_to_unit(7, u7_final)
    append_to_unit(8, u8_final)
    print("All 8 units finalized successfully.")

if __name__ == "__main__":
    main()
