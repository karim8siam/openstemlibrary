#!/usr/bin/env python3
"""
Second expansion pass for Statistical Simulation and Monte Carlo Methods
to comfortably exceed 25,000 substantive prose words across all 8 units.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} boosted.")

# -------------------------------------------------------------
# UNIT 1 BOOST
# -------------------------------------------------------------
u1_boost = r"""
## 1.13 Cryptographic Randomness and Operating System Entropy Harvesting

In security-sensitive simulation applications—such as privacy-preserving synthetic data generation, cryptographic key renewal, and randomized clinical trial blinding—standard scientific PRNGs like Xoshiro256** and Mersenne Twister cannot be used. Because standard PRNGs possess linear or invertible state transitions, an adversary observing a modest sequence of outputs (e.g., 624 consecutive 32-bit integers for MT19937) can run Gaussian elimination over $\mathbb{F}_2$ to reconstruct the entire internal register state, thereby predicting all future and past outputs with $100\%$ certainty.

### 1. Cryptographically Secure Pseudo-Random Number Generators (CSPRNGs)
A pseudo-random bit generator $G: \{0, 1\}^k \to \{0, 1\}^m$ is defined to be **Cryptographically Secure (CSPRNG)** if it passes the **Next-Bit Test** (Yao 1982).
*Definition (Next-Bit Test)*: For all polynomial-time statistical algorithms $A$, and for all indices $i \in \{1, \dots, m-1\}$:
$$P\left( A(s_1, s_2, \dots, s_i) = s_{i+1} \right) \le \frac{1}{2} + \epsilon(k)$$
where $\epsilon(k)$ is a negligible function decaying faster than $k^{-c}$ for all constants $c > 0$. If no computational adversary can predict the next bit with advantage better than a fair coin flip, the generator is indistinguishable from true randomness.

Two primary classes of CSPRNGs dominate modern systems:
1. **Number-Theoretic Generators (e.g., Blum-Blum-Shub)**:
$$x_{n+1} = x_n^2 \pmod M$$
where $M = p \cdot q$ is a Blum integer (the product of two large prime numbers $p \equiv q \equiv 3 \pmod 4$). The security of BBS reduces directly to the computational hardness of the Quadratic Residuosity problem and integer factorization. While provably secure, BBS requires large multi-precision integer modular multiplications, rendering it too slow for high-throughput scientific simulations.
2. **Symmetric Keystream Generators (e.g., ChaCha20)**:
Developed by Daniel J. Bernstein, ChaCha20 operates on a $4 \times 4$ matrix of 32-bit words using twenty rounds of Addition-Rotation-XOR (ARX) operations. ChaCha20 produces pseudo-random output at speeds exceeding 3 gigabytes per second on standard hardware while resisting all known differential, linear, and algebraic cryptanalytic attacks.

### 2. Operating System Entropy Architecture
Modern operating systems supply non-deterministic randomness to statistical environments through special kernel device interfaces such as `/dev/urandom` and the `getrandom()` system call.

The kernel maintains an internal **Entropy Pool** populated by environmental hardware noise:
- Microsecond timing jitter from external physical interrupts (keyboard keystrokes, network packet arrivals, disk seek latency).
- Direct CPU hardware instructions such as Intel/AMD `RDRAND` and `RDSEED`, which measure thermal noise in on-die ring oscillators.

These asynchronous entropy inputs are processed through a cryptographic compression function (such as BLAKE2s or SHA-256) into a master pool. An internal CSPRNG (typically ChaCha20) continuously outputs pseudo-random numbers keyed by the pool. Even if the external hardware noise ceases temporarily, the cryptographic back-tracking resistance ensures that compromise of the current state reveals zero information about previous simulation realizations.
"""

# -------------------------------------------------------------
# UNIT 2 BOOST
# -------------------------------------------------------------
u2_boost = r"""
## 2.12 Exact Simulation of Truncated Distributions

In survival analysis, econometric modeling of censored earnings, and truncated regression (Tobit models), statisticians must draw variates from standard distributions conditioned on belonging to a restricted interval:

$$X \sim f(x \mid a \le X \le b) = \frac{f(x)}{F(b) - F(a)} \mathbb{I}(a \le x \le b)$$

When the truncation interval $[a, b]$ falls in the central body of the distribution, naive acceptance-rejection—drawing $X \sim f$ and discarding draws outside $[a, b]$—works well. However, when simulating rare tail events where $a \gg 0$ (e.g., simulating standard normal variates conditioned on $Z \ge 6$), the probability of landing in the interval is $P(Z \ge 6) \approx 9.86 \times 10^{-10}$. Naive rejection sampling requires an average of over one billion simulation draws per accepted variate, resulting in complete computational stalling.

### 1. Inversion of Truncated Normal CDFs
Using the probability integral transform on the truncated CDF:
$$F_T(x) = \frac{\Phi(x) - \Phi(a)}{\Phi(b) - \Phi(a)} = U \sim \mathcal{U}(0, 1)$$
Solving for $x$ yields:
$$X = \Phi^{-1}\left( \Phi(a) + U \cdot [\Phi(b) - \Phi(a)] \right)$$
While mathematically exact, this formula suffers from catastrophic numerical floating-point underflow when $a$ is large. In standard 64-bit IEEE double precision, $\Phi(6) = 1.0 - \epsilon$ evaluates to $1.0$, causing $\Phi(b) - \Phi(a)$ to round to zero and producing `NaN` or infinite values.

### 2. Christian Robert's Optimal Translated Exponential Proposal
Christian P. Robert (1995) designed an optimal rejection algorithm for simulating truncated normal variates $Z \sim \mathcal{N}(0, 1) \mathbb{I}(Z \ge a)$ that achieves bounded, near-unity acceptance rates for arbitrarily large truncation thresholds $a$.

Robert proposed utilizing a translated exponential distribution:
$$g(z; \lambda) = \lambda e^{-\lambda(z - a)}, \quad z \ge a$$
The acceptance ratio is:
$$\frac{f(z)}{g(z; \lambda)} = \frac{\frac{1}{\sqrt{2\pi}} e^{-z^2/2}}{\lambda e^{-\lambda(z - a)}} = \frac{e^{\lambda a}}{\lambda \sqrt{2\pi}} \exp\left( -\frac{z^2}{2} + \lambda z \right) = \frac{e^{\lambda a + \lambda^2/2}}{\lambda \sqrt{2\pi}} \exp\left( -\frac{(z - \lambda)^2}{2} \right)$$
To maximize the acceptance probability, we minimize the supremum of the ratio over $z \ge a$. The quadratic exponent achieves its maximum at $z = \lambda$ if $\lambda \ge a$, or at $z = a$ if $\lambda < a$. 
Robert proved that the optimal scale parameter $\lambda^*$ is:
$$\lambda^*(a) = \frac{a + \sqrt{a^2 + 4}}{2}$$
Under this optimal parameter, the acceptance ratio simplifies remarkably:
$$\alpha(z) = \exp\left( -\frac{(z - \lambda^*(a))^2}{2} \right)$$
The simulation algorithm proceeds as follows:
1. Generate $E_1, E_2 \sim \text{Exp}(1)$ independently.
2. Set proposed value $Z = a + E_1 / \lambda^*$.
3. If $E_2 \ge \frac{(Z - \lambda^*)^2}{2}$, accept $Z$; otherwise reject and repeat.

Because the acceptance probability satisfies $P(\text{accept}) \ge 0.76$ for all $a \ge 0$, and approaches $1.0$ as $a \to \infty$, this algorithm produces exact extreme tail draws in milliseconds with zero numerical underflow.

## 2.13 Simulation of Hawkes Processes and Self-Exciting Point Processes

Point processes model the stochastic arrival of discrete events in continuous time $t \in [0, T]$. In seismology (aftershocks), high-frequency financial microstructure (order book transactions), and epidemiology (contagion propagation), event arrivals exhibit temporal clustering: the occurrence of an event increases the instantaneous probability of subsequent events. Alan G. Hawkes (1971) formalized this behavior in the **Hawkes Self-Exciting Process**.

The conditional intensity function $\lambda(t \mid \mathcal{H}_t)$ given event history $\mathcal{H}_t = \{t_i : t_i < t\}$ is:
$$\lambda(t \mid \mathcal{H}_t) = \mu + \sum_{t_i < t} \alpha \, e^{-\beta(t - t_i)}$$
where $\mu > 0$ is the baseline background rate, $\alpha > 0$ is the excitation magnitude, and $\beta > \alpha$ is the exponential decay rate. The ratio $n = \alpha / \beta < 1$ represents the branching ratio, ensuring stability.

### The Lewis-Shedler Thinning Algorithm for Hawkes Processes
Because $\lambda(t)$ jumps discontinuously at each arrival time and decays continuously between arrivals, direct inversion of the cumulative intensity is intractable. P. A. W. Lewis and G. S. Shedler (1979) introduced the **Thinning Algorithm** (a continuous-time Poisson analog of rejection sampling):

1. Set current time $t = 0$ and event counter $k = 0$.
2. Compute the maximum instantaneous intensity immediately after the most recent event:
$$\lambda_{\max} = \lambda(t \mid \mathcal{H}_t) = \mu + \sum_{t_i < t} \alpha e^{-\beta(t - t_i)}$$
3. Generate a candidate inter-arrival time from a homogeneous Poisson process with rate $\lambda_{\max}$:
$$\Delta t \sim \text{Exp}(\lambda_{\max}), \quad t_{\text{cand}} = t + \Delta t$$
If $t_{\text{cand}} > T$, terminate simulation.
4. Evaluate the exact decaying intensity at the candidate time:
$$\lambda(t_{\text{cand}}) = \mu + \sum_{t_i < t} \alpha e^{-\beta(t_{\text{cand}} - t_i)}$$
5. Draw $U \sim \mathcal{U}(0, 1)$. If $U \le \frac{\lambda(t_{\text{cand}})}{\lambda_{\max}}$, the candidate arrival is accepted:
$$k \leftarrow k + 1, \quad t_k = t_{\text{cand}}, \quad t \leftarrow t_{\text{cand}}$$
Otherwise, the candidate arrival is "thinned" (rejected), and we set $t \leftarrow t_{\text{cand}}$ without recording an arrival.
6. Repeat from Step 2 until the time horizon $T$ is reached.
"""

# -------------------------------------------------------------
# UNIT 3 BOOST
# -------------------------------------------------------------
u3_boost = r"""
## 3.13 The Wild Bootstrap for Heteroskedastic Regression Models

In linear regression models $Y_i = \mathbf{x}_i^T \boldsymbol{\beta} + \epsilon_i$, standard residual bootstrap resamples the centered residuals $\hat{\epsilon}_i = Y_i - \mathbf{x}_i^T \hat{\boldsymbol{\beta}}$ with equal probability $1/n$. However, this formulation assumes homoskedasticity: $\mathrm{Var}(\epsilon_i \mid \mathbf{x}_i) = \sigma^2$. When the error variance depends on covariates ($\mathrm{Var}(\epsilon_i \mid \mathbf{x}_i) = \sigma^2(\mathbf{x}_i)$), standard residual resampling spreads the variance uniformly across all design points, destroying the heteroskedastic structure and invalidating inferences.

C. F. J. Wu (1986) and Enno Mammen (1993) introduced the **Wild Bootstrap** to resolve heteroskedasticity.

### 1. Mathematical Formulation
Instead of shuffling residuals across different observations, the Wild Bootstrap keeps each residual tied strictly to its own observation index $i$, but scales it by an independent random multiplier $v_i$:

$$Y_i^* = \mathbf{x}_i^T \hat{\boldsymbol{\beta}} + \hat{\epsilon}_i \cdot v_i$$

where $v_1, \dots, v_n$ are independent and identically distributed random variables drawn from an auxiliary distribution $G$ satisfying:
$$\mathbb{E}[v_i] = 0 \quad \text{and} \quad \mathrm{Var}(v_i) = \mathbb{E}[v_i^2] = 1$$
Because $\mathbb{E}[Y_i^* \mid \mathbf{x}_i] = \mathbf{x}_i^T \hat{\boldsymbol{\beta}}$ and $\mathrm{Var}(Y_i^* \mid \mathbf{x}_i) = \hat{\epsilon}_i^2 \mathrm{Var}(v_i) = \hat{\epsilon}_i^2$, the bootstrap resample mimics both the conditional mean and the observation-specific heteroskedastic variance.

### 2. Multiplier Distributions
To achieve higher-order asymptotic accuracy, the third moment of $v_i$ should match the skewness of the underlying distribution ($\mathbb{E}[v_i^3] = 1$):

1. **Mammen's Two-Point Distribution**:
$$v_i = \begin{cases} -(\sqrt{5} - 1)/2 \approx -0.6180, & \text{with probability } p = \frac{\sqrt{5} + 1}{2\sqrt{5}} \approx 0.7236 \\ (\sqrt{5} + 1)/2 \approx 1.6180, & \text{with probability } 1 - p = \frac{\sqrt{5} - 1}{2\sqrt{5}} \approx 0.2764 \end{cases}$$
Mammen's distribution satisfies $\mathbb{E}[v] = 0$, $\mathbb{E}[v^2] = 1$, and $\mathbb{E}[v^3] = 1$, eliminating the leading skewness error term in asymptotic expansions.
2. **The Rademacher Distribution**:
$$v_i = \begin{cases} -1, & \text{with probability } 0.5 \\ +1, & \text{with probability } 0.5 \end{cases}$$
While $\mathbb{E}[v_i^3] = 0$ (symmetric), Emmanuel Flachaire (2005) and Colin Cameron et al. (2008) demonstrated that Rademacher multipliers exhibit superior finite-sample power and avoid spurious tail distortion when testing symmetric hypotheses.
3. **Standard Normal Multiplier**: $v_i \sim \mathcal{N}(0, 1)$, widely known as the Gaussian wild bootstrap.

## 3.14 The Smoothed Bootstrap and Kernel Resampling

The standard empirical distribution function $F_n(x) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}(X_i \le x)$ is a step function with jump discontinuities of size $1/n$ at each observed data point. Consequently, standard bootstrap resamples $\mathbf{x}^*$ consist entirely of ties and duplicate values from the observed sample. 

When estimating quantities sensitive to the local continuity of the density—such as quantiles, density modes, or when data are generated by an inherently continuous physical process—the discrete nature of $F_n$ introduces non-negligible bias. Bernard Silverman (1986) introduced the **Smoothed Bootstrap** to sample from a continuous non-parametric density estimate.

### Algorithmic Mechanics
Let $\hat{f}_h(x)$ be the standard Rosenblatt-Parzen kernel density estimator:
$$\hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^n K\left( \frac{x - X_i}{h} \right)$$
where $K(\cdot)$ is a symmetric probability density kernel (such as the Gaussian kernel) with $\int u K(u)\,du = 0$ and $\int u^2 K(u)\,du = \sigma_K^2 = 1$, and $h > 0$ is the smoothing bandwidth.

Drawing a variate $X^*$ from $\hat{f}_h(x)$ is computationally equivalent to:
1. Drawing an observation $X_I$ uniformly at random from the original sample $\{X_1, \dots, X_n\}$ with replacement.
2. Drawing a continuous perturbation $\epsilon \sim K$ from the kernel distribution.
3. Setting:
$$X^* = X_I + h \cdot \epsilon$$

Because convolution adds variance ($\mathrm{Var}(X^*) = S_n^2 + h^2$), Silverman developed the **Variance-Corrected Smoothed Bootstrap**:
$$X_{\text{corrected}}^* = \bar{X} + \frac{1}{\sqrt{1 + h^2 / S_n^2}} \left( X_I - \bar{X} + h \cdot \epsilon \right)$$
This linear shrinkage adjustment ensures that the bootstrap resample possesses exactly the sample mean $\bar{X}$ and sample variance $S_n^2$ of the original dataset while sampling from a smooth continuous continuum.
"""

# -------------------------------------------------------------
# UNIT 4 BOOST
# -------------------------------------------------------------
u4_boost = r"""
## 4.12 Multilevel Monte Carlo (MLMC) for Stochastic Differential Equations

In computational finance, mathematical biology, and fluid dynamics, models are defined by Stochastic Differential Equations (SDEs):
$$d\mathbf{X}_t = \boldsymbol{\mu}(\mathbf{X}_t, t)\,dt + \boldsymbol{\sigma}(\mathbf{X}_t, t)\,d\mathbf{W}_t$$
To estimate the expected payoff $\mathbb{E}[g(\mathbf{X}_T)]$, the continuous SDE must be discretized into $M$ discrete timesteps of size $h = T/M$ using the Euler-Maruyama or Milstein scheme, producing an approximation $\hat{X}_{T, h}$.

The total mean squared error (MSE) consists of two competing errors:
$$\text{MSE} = \mathbb{E}\left[ (\hat{\theta} - \theta)^2 \right] = \underbrace{(\mathbb{E}[\hat{\theta}] - \theta)^2}_{\text{Discretization Bias } O(h^2)} + \underbrace{\mathrm{Var}(\hat{\theta})}_{\text{Sampling Variance } O(N^{-1})}$$
To achieve an accuracy tolerance of $\epsilon$, one must choose $h = O(\epsilon)$ and $N = O(\epsilon^{-2})$. Because each simulated path requires $M = O(h^{-1}) = O(\epsilon^{-1})$ operations, the total computational complexity of standard Monte Carlo integration is:
$$\text{Cost} = N \times M = O(\epsilon^{-3})$$

Michael B. Giles (2008) revolutionized computational simulation by introducing **Multilevel Monte Carlo (MLMC)**, slashing the complexity to $O(\epsilon^{-2})$.

### 1. Telescoping Sum Decomposition
Let $L$ denote the finest discretization level, with geometric timestep refinement $h_l = h_0 \cdot M^{-l}$ for levels $l = 0, 1, \dots, L$ (typically with $M = 2$ or $4$). Let $P_l$ denote the simulation approximation of payoff $g(\mathbf{X}_T)$ computed with timestep $h_l$.
By linearity of expectation, the expectation at the finest level $P_L$ can be expressed as a **telescoping sum**:

$$\mathbb{E}[P_L] = \mathbb{E}[P_0] + \sum_{l=1}^L \mathbb{E}[P_l - P_{l-1}]$$

Instead of evaluating $P_L$ directly on a massive sample size, MLMC estimates each correction term $\mathbb{E}[P_l - P_{l-1}]$ independently using $N_l$ simulation paths:

$$\hat{Y}_l = \frac{1}{N_l} \sum_{i=1}^{N_l} \left( P_l^{(i)} - P_{l-1}^{(i)} \right)$$

*The Crucial Coupling Trick*: To evaluate $P_l^{(i)} - P_{l-1}^{(i)}$, the fine path $P_l$ and the coarse path $P_{l-1}$ are simulated using the **exact same Brownian motion path** $W_t$. The fine path evaluates increments $\Delta W$ at steps of size $h_l$, while the coarse path simply sums adjacent Brownian increments $\Delta W_{\text{coarse}} = \Delta W_1 + \dots + \Delta W_M$. 

Because both paths are driven by identical Brownian realizations, $P_l^{(i)}$ and $P_{l-1}^{(i)}$ are intensely positively correlated. Consequently:
$$V_l = \mathrm{Var}(P_l - P_{l-1}) = \mathrm{Var}(P_l) + \mathrm{Var}(P_{l-1}) - 2\,\mathrm{Cov}(P_l, P_{l-1}) \to 0 \quad \text{as } l \to \infty$$

### 2. Giles' Complexity Theorem
*Theorem (Giles 2008)*: Let $C_l = O(h_l^{-1})$ be the computational cost per path at level $l$, and suppose the variance decays as $V_l = O(h_l^\beta)$ with $\beta > 0$. The optimal allocation of sample sizes minimizing total variance subject to fixed cost is:
$$N_l \propto \sqrt{\frac{V_l}{C_l}} \propto \sqrt{h_l^\beta \cdot h_l} = h_l^{(\beta + 1)/2}$$
Under the Milstein discretization scheme, strong convergence is of order 1, yielding $\beta = 2$. Because $\beta > 1$, the variance decays faster than the cost increases. The sum of computational work across all levels is dominated by the coarsest level $l = 0$. 

The total computational cost to achieve root mean squared error $\epsilon$ is bounded by:
$$\text{Cost}_{\text{MLMC}} = O(\epsilon^{-2})$$
MLMC eliminates the penalty of time-discretization, achieving the theoretical complexity bound of an exact continuous sampler.
"""

# -------------------------------------------------------------
# UNIT 5 BOOST
# -------------------------------------------------------------
u5_boost = r"""
## 5.12 Bridge Sampling and Path Sampling for Normalizing Constants

In Bayesian model selection and hypothesis testing, the fundamental challenge is computing the **marginal likelihood** (also called the **evidence**) of model $\mathcal{M}$:

$$Z = p(\mathbf{y} \mid \mathcal{M}) = \int_{\boldsymbol{\Theta}} p(\mathbf{y} \mid \boldsymbol{\theta}, \mathcal{M}) p(\boldsymbol{\theta} \mid \mathcal{M})\,d\boldsymbol{\theta}$$

Evaluating $Z$ is essential for calculating Bayes factors $B_{12} = Z_1 / Z_2$ and posterior model probabilities $P(\mathcal{M}_k \mid \mathbf{y})$. However, standard MCMC draws only from the unnormalized posterior $p(\boldsymbol{\theta} \mid \mathbf{y}) \propto q(\boldsymbol{\theta}) = p(\mathbf{y} \mid \boldsymbol{\theta}) p(\boldsymbol{\theta})$, where $Z$ cancels out of the Metropolis acceptance ratio.

Naive Monte Carlo integration using prior draws $\hat{Z}_{\text{prior}} = \frac{1}{N} \sum p(\mathbf{y} \mid \boldsymbol{\theta}^{(i)})$ has catastrophic variance because the posterior mass occupies a tiny fraction of the prior support. Conversely, the harmonic mean estimator of Newton and Raftery (1994) $\hat{Z}_{\text{HM}} = \left[ \frac{1}{N} \sum p(\mathbf{y} \mid \boldsymbol{\theta}^{(i)})^{-1} \right]^{-1}$ has infinite variance in virtually all non-trivial models.

Andrew Gelman and Xiao-Li Meng (1998) introduced **Bridge Sampling** and **Path Sampling** to provide robust, finite-variance estimators of normalizing constants.

### 1. Mathematical Formulation of Bridge Sampling
Let $p_1(\boldsymbol{\theta}) = q_1(\boldsymbol{\theta}) / Z_1$ be the target posterior and $p_0(\boldsymbol{\theta}) = q_0(\boldsymbol{\theta}) / Z_0$ be a tractable proposal distribution (such as a multivariate Gaussian or Student-$t$ distribution matching the posterior mean and covariance). 

Let $\alpha(\boldsymbol{\theta})$ be an arbitrary bridge function. By multiplying and dividing by $\alpha$:
$$\int \alpha(\boldsymbol{\theta}) q_1(\boldsymbol{\theta}) p_0(\boldsymbol{\theta})\,d\boldsymbol{\theta} = \int \alpha(\boldsymbol{\theta}) \frac{q_1(\boldsymbol{\theta}) q_0(\boldsymbol{\theta})}{Z_0}\,d\boldsymbol{\theta}$$
$$\int \alpha(\boldsymbol{\theta}) q_0(\boldsymbol{\theta}) p_1(\boldsymbol{\theta})\,d\boldsymbol{\theta} = \int \alpha(\boldsymbol{\theta}) \frac{q_0(\boldsymbol{\theta}) q_1(\boldsymbol{\theta})}{Z_1}\,d\boldsymbol{\theta}$$
Taking the ratio of these two expectations yields the exact bridge identity:

$$\frac{Z_1}{Z_0} = \frac{\mathbb{E}_{p_0}\left[ \alpha(\boldsymbol{\theta}) q_1(\boldsymbol{\theta}) \right]}{\mathbb{E}_{p_1}\left[ \alpha(\boldsymbol{\theta}) q_0(\boldsymbol{\theta}) \right]}$$

Given $N_0$ independent draws from $p_0$ and $N_1$ MCMC draws from $p_1$:
$$\frac{\widehat{Z_1}}{Z_0} = \frac{\frac{1}{N_0} \sum_{i=1}^{N_0} \alpha(\boldsymbol{\theta}_{0, i}) q_1(\boldsymbol{\theta}_{0, i})}{\frac{1}{N_1} \sum_{j=1}^{N_1} \alpha(\boldsymbol{\theta}_{1, j}) q_0(\boldsymbol{\theta}_{1, j})}$$

### 2. The Optimal Bridge Function
Meng and Wong (1996) proved that the bridge function $\alpha^*(\boldsymbol{\theta})$ minimizing the asymptotic relative mean squared error is:

$$\alpha^*(\boldsymbol{\theta}) \propto \frac{1}{N_0 p_0(\boldsymbol{\theta}) + N_1 p_1(\boldsymbol{\theta})} = \frac{1}{N_0 q_0(\boldsymbol{\theta}) + N_1 \frac{Z_0}{Z_1} q_1(\boldsymbol{\theta})}$$

Because the optimal function depends on the unknown ratio $r = Z_1 / Z_0$, bridge sampling solves for $r$ via fixed-point iteration:
$$r^{(t+1)} = \frac{\frac{1}{N_0} \sum_{i=1}^{N_0} \frac{q_1(\boldsymbol{\theta}_{0, i})}{N_0 q_0(\boldsymbol{\theta}_{0, i}) + N_1 r^{(t)} q_1(\boldsymbol{\theta}_{0, i})}}{\frac{1}{N_1} \sum_{j=1}^{N_1} \frac{q_0(\boldsymbol{\theta}_{1, j})}{N_0 q_0(\boldsymbol{\theta}_{1, j}) + N_1 r^{(t)} q_1(\boldsymbol{\theta}_{1, j})}}$$
This fixed-point iteration converges in 5 to 10 steps, providing numerically stable estimates of marginal likelihoods with bounded variance.
"""

# -------------------------------------------------------------
# UNIT 6 BOOST
# -------------------------------------------------------------
u6_boost = r"""
## 6.12 Non-Reversible MCMC and Piecewise Deterministic Markov Processes (PDMP)

All classical MCMC algorithms—including Metropolis-Hastings and Gibbs sampling—are constructed to satisfy the **Detailed Balance** condition:
$$\pi(\mathbf{x}) T(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{y}) T(\mathbf{y}, \mathbf{x})$$
Detailed balance guarantees reversibility: viewing the Markov trajectory forward or backward in time reveals identical statistical distributions.

However, reversibility is merely a mathematically convenient *sufficient* condition for stationarity, not a necessary one. The necessary and sufficient condition for $\pi$ to be invariant is the **Global Balance** equation:
$$\int \pi(\mathbf{x}) T(\mathbf{x}, \mathbf{y})\,d\mathbf{x} = \pi(\mathbf{y})$$

Persi Diaconis, Susan Holmes, and Radford Neal (2000) demonstrated that enforcing reversibility actually harms simulation efficiency: reversible chains are forced to move via diffusion, repeatedly back-tracking over previously visited states. By breaking detailed balance and constructing **Non-Reversible Markov Processes**, one introduces directed momentum, dramatically reducing autocorrelation and accelerating convergence.

### 1. The Continuous-Time PDMP Framework
Modern non-reversible simulation operates via **Piecewise Deterministic Markov Processes (PDMP)**, where state trajectories consist of continuous deterministic motion punctuated by discrete stochastic events.

Let $(\mathbf{x}(t), \mathbf{v}(t)) \in \mathbb{R}^d \times \mathbb{R}^d$ represent continuous position and discrete velocity. A PDMP is governed by three operators:
1. **Deterministic Drift**: Between jump events, the state evolves along deterministic vector fields: $\frac{d\mathbf{x}}{dt} = \mathbf{v}$.
2. **Jump Rate (Intensity)**: Jump events occur as an inhomogeneous Poisson process with state-dependent event rate $\lambda(\mathbf{x}, \mathbf{v})$.
3. **Transition Kernel**: When a jump event occurs, the velocity updates instantaneously to $\mathbf{v}^* \sim Q((\mathbf{x}, \mathbf{v}), \cdot)$, while position remains continuous.

### 2. The Zig-Zag Sampler and the Bouncy Particle Sampler
Two breakthrough PDMP algorithms illustrate this non-reversible paradigm:
1. **The Zig-Zag Sampler** (Bierkens, Fearnhead, and Roberts 2019):
The velocity components are restricted to discrete signs $v_i \in \{-1, +1\}$. The particle travels in straight lines parallel to hypercube diagonals. Component $i$ flips velocity sign $v_i \to -v_i$ with event rate:
$$\lambda_i(\mathbf{x}, \mathbf{v}) = \max\left( 0, v_i \frac{\partial U(\mathbf{x})}{\partial x_i} \right)$$
where $U(\mathbf{x}) = -\log \pi(\mathbf{x})$. When the particle moves uphill against the potential (away from posterior mass), the switching rate increases, flipping direction back toward the mode.
2. **The Bouncy Particle Sampler (BPS)** (Bouchard-Côté, Vollmer, and Doucet 2018):
Velocity moves freely on the unit sphere $\|\mathbf{v}\|_2 = 1$. When an event occurs at rate $\lambda(\mathbf{x}, \mathbf{v}) = \max(0, \langle \mathbf{v}, \nabla U(\mathbf{x}) \rangle)$, the velocity undergoes a specular reflection off the gradient hyperplane $\nabla U(\mathbf{x})$:
$$\mathbf{v}^* = \mathbf{v} - 2 \frac{\langle \mathbf{v}, \nabla U(\mathbf{x}) \rangle}{\|\nabla U(\mathbf{x})\|_2^2} \nabla U(\mathbf{x})$$

Because PDMPs require zero Metropolis reject-and-stay steps and accept continuous gradient information, they scale effectively to tall-data settings: Poisson thinning allows unbiased gradient evaluation using small mini-batches of data, enabling exact Bayesian MCMC on billion-row datasets.
"""

# -------------------------------------------------------------
# UNIT 7 BOOST
# -------------------------------------------------------------
u7_boost = r"""
## 7.12 Variational Inference vs. Markov Chain Monte Carlo

In modern computational statistics and machine learning, Bayesian posterior approximation is divided into two competing paradigms: **Markov Chain Monte Carlo (MCMC)** and **Variational Inference (VI)**. While MCMC approaches posterior estimation via stochastic simulation, VI recasts posterior inference as a deterministic optimization problem.

### 1. The Evidence Lower Bound (ELBO)
Let $\mathbf{x}$ be observed data and $\mathbf{z}$ be latent variables or model parameters with joint density $p(\mathbf{x}, \mathbf{z}) = p(\mathbf{x} \mid \mathbf{z}) p(\mathbf{z})$. We specify a family of tractable approximate distributions $\mathcal{Q} = \{ q_\phi(\mathbf{z}) \}$ and search for the variational parameters $\phi^*$ that minimize the Kullback-Leibler (KL) divergence to the exact posterior:

$$\phi^* = \arg\min_\phi \mathcal{D}_{\text{KL}}(q_\phi(\mathbf{z}) \parallel p(\mathbf{z} \mid \mathbf{x})) = \arg\min_\phi \int q_\phi(\mathbf{z}) \log \left( \frac{q_\phi(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{x})} \right) d\mathbf{z}$$

Because the posterior $p(\mathbf{z} \mid \mathbf{x}) = p(\mathbf{x}, \mathbf{z}) / p(\mathbf{x})$ contains the intractable evidence $p(\mathbf{x})$, the KL divergence cannot be minimized directly. However, decomposing the marginal log-likelihood reveals:

$$\log p(\mathbf{x}) = \int q_\phi(\mathbf{z}) \log p(\mathbf{x})\,d\mathbf{z} = \int q_\phi(\mathbf{z}) \log \left( \frac{p(\mathbf{x}, \mathbf{z})}{q_\phi(\mathbf{z})} \cdot \frac{q_\phi(\mathbf{z})}{p(\mathbf{z} \mid \mathbf{x})} \right) d\mathbf{z}$$
$$\log p(\mathbf{x}) = \underbrace{\mathbb{E}_{q_\phi}\left[ \log \frac{p(\mathbf{x}, \mathbf{z})}{q_\phi(\mathbf{z})} \right]}_{\text{ELBO}(\phi)} + \underbrace{\mathcal{D}_{\text{KL}}(q_\phi(\mathbf{z}) \parallel p(\mathbf{z} \mid \mathbf{x}))}_{\ge 0}$$

Because the KL divergence is strictly non-negative, the **Evidence Lower Bound (ELBO)** forms a rigorous lower bound on the marginal likelihood:
$$\log p(\mathbf{x}) \ge \text{ELBO}(\phi) = \mathbb{E}_{q_\phi}[\log p(\mathbf{x}, \mathbf{z})] - \mathbb{E}_{q_\phi}[\log q_\phi(\mathbf{z})]$$
Maximizing $\text{ELBO}(\phi)$ with respect to $\phi$ is mathematically identical to minimizing $\mathcal{D}_{\text{KL}}(q_\phi \parallel p(\cdot \mid \mathbf{x}))$.

### 2. Methodological Trade-Off Comparison
<div class="table-wrapper">
<table class="data-table">
<thead>
<tr>
<th>Dimension / Property</th>
<th>Markov Chain Monte Carlo (MCMC / HMC)</th>
<th>Variational Inference (VI / CAVI / SVI)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Asymptotic Guarantee</strong></td>
<td>Exact in the limit ($n \to \infty$ simulation draws). Guarantees consistent posterior estimation.</td>
<td>Inherently biased. Confined to the variational family $\mathcal{Q}$ even with infinite computation.</td>
</tr>
<tr>
<td><strong>Computational Speed</strong></td>
<td>Slow to moderate. Requires serial evaluation of thousands of sequential proposal steps.</td>
<td>Fast. Leverages numerical optimization (gradient ascent, SGD) to converge in seconds.</td>
</tr>
<tr>
<td><strong>Scalability to Big Data</strong></td>
<td>Difficult. Standard MCMC requires evaluating the likelihood over all $N$ data points at each step.</td>
<td>Seamless. Stochastic Variational Inference (SVI) evaluates mini-batches using Robbins-Monro updates.</td>
</tr>
<tr>
<td><strong>Uncertainty / Variance</strong></td>
<td>Captures full non-Gaussian geometry, multimodality, skewness, and exact parameter correlations.</td>
<td>Underestimates posterior variance; mean-field factorization assumes independence, suppressing covariances.</td>
</tr>
<tr>
<td><strong>Diagnostic Verification</strong></td>
<td>Rigorous diagnostics ($\hat{R} \le 1.01$, ESS, trace plots, divergence flags).</td>
<td>Difficult to assess error without comparing against an expensive MCMC gold standard.</td>
</tr>
</tbody>
</table>
</div>

In modern workflows, VI is routinely deployed for rapid exploratory data analysis, initial hyperparameter screening, and initializing MCMC warmup trajectories, while Hamiltonian Monte Carlo is employed for final regulatory and scientific hypothesis reporting.
"""

# -------------------------------------------------------------
# UNIT 8 BOOST
# -------------------------------------------------------------
u8_boost = r"""
## 8.12 Particle MCMC and Particle Marginal Metropolis-Hastings (PMMH)

When analyzing non-linear state space models, the joint parameter-state inference problem involves two coupled estimation layers:
1. The static parameter vector $\boldsymbol{\theta}$ governing system dynamics (e.g., volatility parameters, transmission rates).
2. The dynamic time-varying latent state trajectory $\mathbf{x}_{1:T}$.

Standard MCMC can alternate between updating $\boldsymbol{\theta} \mid \mathbf{x}_{1:T}$ and updating $\mathbf{x}_{1:T} \mid \boldsymbol{\theta}$. However, because the dimension of $\mathbf{x}_{1:T}$ grows linearly with time $T$, the parameters and states become tightly coupled, causing Gibbs samplers to mix with glacial slowness.

Christophe Andrieu, Arnaud Doucet, and Roman Holenstein (2010) formulated **Particle Markov Chain Monte Carlo (PMCMC)**, embedding Sequential Monte Carlo inside MCMC to sample directly from the exact marginal posterior $p(\boldsymbol{\theta} \mid \mathbf{y}_{1:T})$.

### 1. The Particle Marginal Metropolis-Hastings (PMMH) Algorithm
Suppose we propose a new parameter vector $\boldsymbol{\theta}^* \sim q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta})$. To evaluate the ideal marginal Metropolis-Hastings ratio:
$$\alpha(\boldsymbol{\theta}, \boldsymbol{\theta}^*) = \min\left( 1, \frac{p(\boldsymbol{\theta}^*) p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}^*)}{p(\boldsymbol{\theta}) p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})} \frac{q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^*)}{q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta})} \right)$$
the marginal likelihood $p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}) = \prod_{t=1}^T p(\mathbf{y}_t \mid \mathbf{y}_{1:t-1}, \boldsymbol{\theta})$ must be evaluated.

Because this likelihood is analytically intractable, PMMH runs a bootstrap particle filter with $N$ particles targeted at $\boldsymbol{\theta}^*$. The particle filter provides an unbiased Monte Carlo estimate of the marginal likelihood:
$$\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}^*) = \prod_{t=1}^T \left( \frac{1}{N} \sum_{i=1}^N \tilde{w}_t^{(i)} \right)$$

PMMH replaces the exact intractable likelihood with this particle-filter estimate in the acceptance ratio:
$$\alpha_{\text{PMMH}} = \min\left( 1, \frac{p(\boldsymbol{\theta}^*) \hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}^*)}{p(\boldsymbol{\theta}) \hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})} \frac{q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^*)}{q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta})} \right)$$

### 2. The Pseudo-Marginal Theorem
A naive statistician might assume that substituting a stochastic estimate $\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$ introduces approximation error into the resulting Markov chain. Remarkably, the **Pseudo-Marginal Theorem** (Beaumont 2003, Andrieu and Roberts 2009) proves that this is not the case:

*Theorem (Pseudo-Marginal Validity)*: If the likelihood estimator $\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$ is non-negative and strictly unbiased:
$$\mathbb{E}[\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})] = p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$$
for all $\boldsymbol{\theta}$, then the stationary distribution of the Markov chain generated by PMMH is **identically and exactly** the true posterior distribution $p(\boldsymbol{\theta} \mid \mathbf{y}_{1:T})$, regardless of the number of particles $N \ge 1$.

*Proof Intuition*: The particle filter's internal random numbers $\mathbf{U}$ can be viewed as auxiliary variables on an extended state space $(\boldsymbol{\theta}, \mathbf{U})$. Because the joint target distribution on this extended space integrates out to the exact marginal target, the Metropolis-Hastings acceptance ratio on the extended space matches $\alpha_{\text{PMMH}}$ exactly.

The number of particles $N$ affects only the variance of the likelihood estimator: if $N$ is too small, $\hat{p}$ occasionally overestimates the likelihood, trapping the chain at an unrepresentative parameter value. Doucet et al. (2015) proved that the optimal computational efficiency is achieved when $N$ is tuned so that the standard deviation of $\log \hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$ is approximately $1.2$ to $1.8$.
"""

def main():
    append_to_unit(1, u1_boost)
    append_to_unit(2, u2_boost)
    append_to_unit(3, u3_boost)
    append_to_unit(4, u4_boost)
    append_to_unit(5, u5_boost)
    append_to_unit(6, u6_boost)
    append_to_unit(7, u7_boost)
    append_to_unit(8, u8_boost)
    print("All 8 units boosted successfully.")

if __name__ == "__main__":
    main()
