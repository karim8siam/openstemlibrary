# tooling/expand-unit-5.py
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "r", encoding="utf-8") as f:
    text = f.read()

addition = r"""

---

## 5.6 Quasi-Monte Carlo Methods, Low-Discrepancy Sequences, and the Koksma–Hlawka Inequality

Standard Monte Carlo integration relies on pseudo-random sequences. While pseudo-random sequences are statistically independent, random sampling inevitably produces **stochastic clustering**: random points bunch together in some regions of the integration domain while leaving large voids in others. These random clusters and voids are the fundamental cause of the slow $\mathcal{O}(N^{-1/2})$ error rate.

To achieve faster deterministic convergence, **Quasi-Monte Carlo (QMC)** replaces pseudo-random sampling with carefully engineered **low-discrepancy sequences** that fill the integration domain as uniformly as possible.

### Discrepancy Theory and the Star Discrepancy Metric

Let $\mathcal{P} = \{\mathbf{x}_1, \dots, \mathbf{x}_N\}$ be a point set in the $d$-dimensional unit hypercube $I^d = [0, 1)^d$.
Let $\mathcal{J}^*$ denote the family of all axis-aligned sub-rectangles anchored at the origin:
$$B = \prod_{j=1}^d [0, u_j), \quad 0 \le u_j \le 1$$
The volume of $B$ is $\lambda(B) = \prod_{j=1}^d u_j$.

The **Star Discrepancy** $D_N^*(\mathcal{P})$ measures the maximum absolute deviation between the empirical proportion of points landing in $B$ and the theoretical volume $\lambda(B)$:

$$D_N^*(\mathcal{P}) = \sup_{B \in \mathcal{J}^*} \left| \frac{\#\{\mathbf{x}_i \in B\}}{N} - \lambda(B) \right|$$

- For a completely uniform grid or ideal point set, $D_N^* \to 0$ rapidly.
- For independent random points (Monte Carlo), the law of the iterated logarithm implies:
  $$D_N^*(\mathcal{P}_{random}) = \mathcal{O}\left( \sqrt{\frac{\log \log N}{N}} \right) \approx \mathcal{O}\left( N^{-1/2} \right)$$
- For a **low-discrepancy sequence** (QMC), the discrepancy satisfies:
  $$D_N^*(\mathcal{P}_{QMC}) = \mathcal{O}\left( \frac{(\log N)^d}{N} \right)$$

### The Koksma–Hlawka Inequality

The foundational theoretical guarantee of Quasi-Monte Carlo integration is the **Koksma–Hlawka Inequality**, established by Jurjen Koksma (1942) and Edmund Hlawka (1961).

#### The Theorem:
Let $h: [0, 1]^d \to \mathbb{R}$ be a function with bounded variation in the sense of Hardy and Krause, denoted $V_{HK}(h) < \infty$. For any deterministic point set $\mathcal{P} = \{\mathbf{x}_1, \dots, \mathbf{x}_N\} \subset [0, 1)^d$:

$$\left| \frac{1}{N} \sum_{i=1}^N h(\mathbf{x}_i) - \int_{[0, 1]^d} h(\mathbf{x}) \, d\mathbf{x} \right| \le V_{HK}(h) \cdot D_N^*(\mathcal{P})$$

#### Convergence Implications:
The Koksma–Hlawka inequality neatly decouples the integration error into two orthogonal factors:
1. $V_{HK}(h)$: A constant depending solely on the mathematical smoothness and variation of the integrand $h$.
2. $D_N^*(\mathcal{P})$: The geometric uniformity of the sampling nodes $\mathcal{P}$.

For low-discrepancy point sets, substituting $D_N^*(\mathcal{P}) = \mathcal{O}((\log N)^d / N)$ yields an asymptotic error rate of:

$$\text{Error}_{QMC} = \mathcal{O}\left( \frac{(\log N)^d}{N} \right)$$

For any fixed dimension $d$, as $N \to \infty$, the factor $(\log N)^d / N$ approaches $\mathcal{O}(N^{-1})$:
- Standard Monte Carlo error: $\mathcal{O}(N^{-0.5})$.
- Quasi-Monte Carlo error: $\approx \mathcal{O}(N^{-1.0})$.

To achieve an error of $10^{-4}$ in low dimensions:
- Crude Monte Carlo requires $N \approx (10^4)^2 = 10^8 = 100,000,000$ points.
- Quasi-Monte Carlo requires only $N \approx 10^4 = 10,000$ points—a **$10,000$-fold reduction in computational evaluations**!

### Construction of Low-Discrepancy Sequences: Van der Corput, Halton, and Sobol'

#### 1. The 1D Van der Corput Sequence
The simplest low-discrepancy sequence is the **Van der Corput sequence** in base $b \ge 2$.
Any non-negative integer $n$ can be expanded uniquely in base $b$:
$$n = \sum_{j=0}^k a_j(n) b^j, \quad a_j(n) \in \{0, 1, \dots, b - 1\}$$
The radical inverse function $\phi_b(n)$ reflects the base-$b$ digits across the decimal (radix) point:
$$\phi_b(n) = \sum_{j=0}^k a_j(n) b^{-(j + 1)}$$

For example, in base $b = 2$:
- $n = 1 = (1)_2 \implies \phi_2(1) = 0.1_2 = 1/2 = 0.5$
- $n = 2 = (10)_2 \implies \phi_2(2) = 0.01_2 = 1/4 = 0.25$
- $n = 3 = (11)_2 \implies \phi_2(3) = 0.11_2 = 3/4 = 0.75$
- $n = 4 = (100)_2 \implies \phi_2(4) = 0.001_2 = 1/8 = 0.125$

The sequence systematically bisects existing intervals, preventing clustering.

#### 2. The Halton Sequence in Dimension $d$
J. H. Halton (1960) generalized the Van der Corput construction to $d$ dimensions by choosing $d$ distinct pairwise co-prime prime numbers $p_1, p_2, \dots, p_d$ (e.g. $2, 3, 5, 7, 11, \dots$):
$$\mathbf{x}_n = (\phi_{p_1}(n), \, \phi_{p_2}(n), \, \dots, \, \phi_{p_d}(n)) \in [0, 1)^d$$

#### 3. Sobol' Sequences
For higher dimensions ($d > 10$), Halton sequences can suffer from linear correlation artifacts between high-index primes. Ilya M. Sobol' (1967) introduced **Sobol' sequences**, constructed in base 2 using primitive polynomials and direction numbers over Galois fields $\mathbb{F}_2$. Sobol' sequences form digital $(t, s)$-sequences with exceptional uniformity across projections.

### Randomized Quasi-Monte Carlo (RQMC)

A limitation of pure QMC is that the error bound $V_{HK}(h) D_N^*$ is non-probabilistic: because the sequence is deterministic, one cannot compute a sample standard error or confidence interval from a single QMC run.

To solve this, Art Owen (1995) developed **Randomized Quasi-Monte Carlo (RQMC)**.
RQMC introduces a stochastic randomization that preserves the low-discrepancy properties of the sequence while making each point uniformly distributed on $[0, 1)^d$:
1. **Cranley–Patterson Rotation (Random Shift Modulo 1)**:
   Draw a single random vector $\mathbf{U} \sim \text{Uniform}[0, 1)^d$. Shift all points:
   $$\tilde{\mathbf{x}}_i = (\mathbf{x}_i + \mathbf{U}) \pmod 1$$
2. **Owen Scrambling**:
   Permutes the digits of the radical inverse tree using random independent permutations at each branch.

Under RQMC:
- The estimator $\hat{\theta}_{RQMC} = \frac{1}{N} \sum_{i=1}^N h(\tilde{\mathbf{x}}_i)$ is **strictly unbiased**: $\mathbb{E}[\hat{\theta}_{RQMC}] = \theta$.
- For smooth functions, the variance decays at the astonishing asymptotic rate of $\mathcal{O}(N^{-3})$, enabling standard empirical confidence interval construction by running $R$ independent randomizations ($R \in [10, 30]$).

---

## 5.7 Markov Chain Monte Carlo (MCMC) Foundations: Metropolis–Hastings, Gibbs Sampling, and Convergence Diagnostics

When target distributions are high-dimensional, unnormalized, and non-standard—as is universally the case in modern Bayesian posterior inference:

$$p(\boldsymbol{\theta} \mid \mathbf{y}) = \frac{p(\mathbf{y} \mid \boldsymbol{\theta}) p(\boldsymbol{\theta})}{\int p(\mathbf{y} \mid \boldsymbol{\theta}') p(\boldsymbol{\theta}') d\boldsymbol{\theta}'} \propto p(\mathbf{y} \mid \boldsymbol{\theta}) p(\boldsymbol{\theta})$$

the normalizing marginal likelihood (evidence) constant in the denominator is an intractable high-dimensional integral. Direct inversion, rejection sampling, and importance sampling all fail in high dimensions due to exponential rejection rates and weight degeneracy.

The universal solution is **Markov Chain Monte Carlo (MCMC)**: constructing an ergodic Markov chain whose stationary (limiting) distribution is precisely the target posterior distribution $\pi(\boldsymbol{\theta}) = p(\boldsymbol{\theta} \mid \mathbf{y})$.

```text
MCMC Trajectory Flow (Ergodic Convergence to Target Stationary Distribution):
  Initial State \theta_0
           |
           v (Burn-in / Warmup Phase)
  State \theta_1 ---> State \theta_2 ---> State \theta_t
                                               |
                                               v (Sampling Phase)
                                   [ Samples Drawn from \pi(\theta) ]
```

### The Detailed Balance Condition

Let $P(\mathbf{x}, \mathbf{y})$ denote the transition kernel of a discrete-time continuous-state Markov chain, representing the conditional probability density of transitioning from state $\mathbf{x}$ to state $\mathbf{y}$.

A distribution $\pi(\mathbf{x})$ is a **stationary (invariant) distribution** of the chain if:

$$\int \pi(\mathbf{x}) P(\mathbf{x}, \mathbf{y}) \, d\mathbf{x} = \pi(\mathbf{y})$$

A sufficient (though not strictly necessary) condition for stationarity is the **Detailed Balance Condition (Microscopic Reversibility)**:

$$\pi(\mathbf{x}) P(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{y}) P(\mathbf{y}, \mathbf{x}) \quad \text{for all } \mathbf{x}, \mathbf{y}$$

Integrating both sides with respect to $\mathbf{x}$:
$$\int \pi(\mathbf{x}) P(\mathbf{x}, \mathbf{y}) \, d\mathbf{x} = \pi(\mathbf{y}) \int P(\mathbf{y}, \mathbf{x}) \, d\mathbf{x} = \pi(\mathbf{y}) \cdot 1 = \pi(\mathbf{y})$$
Detailed balance guarantees that the target distribution $\pi$ is invariant.

### The Metropolis–Hastings Algorithm

In 1953, Nicholas Metropolis and colleagues developed the symmetric algorithm for physics simulations. In 1970, Canadian statistician W. K. Hastings generalized the framework to arbitrary statistical proposal distributions.

#### Algorithmic Formulation:
Let $\pi(\boldsymbol{\theta})$ be the target density, known up to a normalizing constant: $\pi(\boldsymbol{\theta}) = c \cdot \tilde{\pi}(\boldsymbol{\theta})$.
Let $q(\boldsymbol{\theta}' \mid \boldsymbol{\theta})$ be a candidate **proposal distribution** generating a new proposed state $\boldsymbol{\theta}'$ given current state $\boldsymbol{\theta}$.

At iteration $t$ with current state $\boldsymbol{\theta}_t$:
1. Generate candidate state $\boldsymbol{\theta}^* \sim q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta}_t)$.
2. Compute the **Metropolis–Hastings Acceptance Probability**:
   $$\alpha(\boldsymbol{\theta}_t, \boldsymbol{\theta}^*) = \min\left( 1, \, \frac{\pi(\boldsymbol{\theta}^*) q(\boldsymbol{\theta}_t \mid \boldsymbol{\theta}^*)}{\pi(\boldsymbol{\theta}_t) q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta}_t)} \right) = \min\left( 1, \, \frac{\tilde{\pi}(\boldsymbol{\theta}^*) q(\boldsymbol{\theta}_t \mid \boldsymbol{\theta}^*)}{\tilde{\pi}(\boldsymbol{\theta}_t) q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta}_t)} \right)$$
   Notice that the intractable normalizing constant $c$ cancels out completely in the ratio!
3. Draw $U \sim \text{Uniform}(0, 1)$.
   - If $U \le \alpha(\boldsymbol{\theta}_t, \boldsymbol{\theta}^*)$, **ACCEPT**: set $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}^*$.
   - Otherwise, **REJECT**: retain the previous state $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t$.

#### Mathematical Proof of Detailed Balance:
The transition kernel is:
$$P(\mathbf{x}, \mathbf{y}) = q(\mathbf{y} \mid \mathbf{x}) \alpha(\mathbf{x}, \mathbf{y}) \quad (\text{for } \mathbf{x} \ne \mathbf{y})$$
Assume without loss of generality that $\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \le \pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})$.
Then:
$$\alpha(\mathbf{x}, \mathbf{y}) = \frac{\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})}{\pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})} \quad \text{and} \quad \alpha(\mathbf{y}, \mathbf{x}) = 1$$
Now evaluate both sides of detailed balance:
- Left-hand side:
  $$\pi(\mathbf{x}) P(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x}) \left( \frac{\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})}{\pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})} \right) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})$$
- Right-hand side:
  $$\pi(\mathbf{y}) P(\mathbf{y}, \mathbf{x}) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \cdot 1 = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})$$
Both sides match identically! Detailed balance is strictly satisfied.

### The Gibbs Sampler

Introduced by Stuart and Donald Geman (1984) in image processing and popularized in statistics by Alan Gelfand and Adrian Smith (1990), **Gibbs Sampling** is a special case of Metropolis–Hastings where parameters are updated scalar-by-scalar (or block-by-block) from their **full conditional distributions**:

$$\theta_j^{(t+1)} \sim p(\theta_j \mid \theta_1^{(t+1)}, \dots, \theta_{j-1}^{(t+1)}, \theta_{j+1}^{(t)}, \dots, \theta_p^{(t)}, \mathbf{y})$$

Because the proposal distribution is the exact conditional distribution $q(\theta_j^* \mid \boldsymbol{\theta}) = p(\theta_j^* \mid \boldsymbol{\theta}_{-j})$, the Metropolis–Hastings acceptance ratio evaluates to:
$$\alpha = \min\left( 1, \, \frac{p(\theta_j^* \mid \boldsymbol{\theta}_{-j}) p(\theta_j \mid \boldsymbol{\theta}_{-j})}{p(\theta_j \mid \boldsymbol{\theta}_{-j}) p(\theta_j^* \mid \boldsymbol{\theta}_{-j})} \right) = \min(1, 1) = 1.0$$
In Gibbs sampling, **every single proposal is accepted with probability $100\%$**!

### MCMC Diagnostics: Autocorrelation, ESS, and Gelman–Rubin $\hat{R}$

Because MCMC samples are generated sequentially by a Markov chain, consecutive draws are **correlated** ($\text{Corr}(\boldsymbol{\theta}_t, \boldsymbol{\theta}_{t+k}) > 0$). To evaluate sampling adequacy:

#### 1. Autocorrelation and Integrated Autocorrelation Time ($\tau_{int}$)
The lag-$k$ autocorrelation is:
$$\rho_k = \frac{\mathbb{E}[(\theta_t - \mu)(\theta_{t+k} - \mu)]}{\sigma^2}$$
The **Integrated Autocorrelation Time** is:
$$\tau_{int} = 1 + 2 \sum_{k=1}^\infty \rho_k$$
$\tau_{int}$ represents the number of dependent Markov chain steps required to obtain the statistical information equivalent to one independent draw.

#### 2. Effective Sample Size (ESS)
For a chain of length $N$, the effective number of independent draws is:

$$\text{ESS} = \frac{N}{\tau_{int}} = \frac{N}{1 + 2 \sum_{k=1}^\infty \rho_k}$$

If $N = 10,000$ and $\tau_{int} = 20$, the chain contains only $\text{ESS} = 500$ independent pieces of information. Standard errors must be computed using $\text{SE} = \hat{\sigma} / \sqrt{\text{ESS}}$.

#### 3. Gelman–Rubin Convergence Diagnostic ($\hat{R}$)
Andrew Gelman and Donald Rubin (1992) formulated the **Potential Scale Reduction Factor ($\hat{R}$)** based on running $M \ge 3$ independent chains from over-dispersed starting points.
Let each chain have length $N$ after discarding warmup/burn-in.
- Compute the **Between-Chain Variance ($B$)**:
  $$B = \frac{N}{M - 1} \sum_{m=1}^M (\bar{\theta}_m - \bar{\theta}_{\cdot})^2$$
- Compute the **Within-Chain Variance ($W$)**:
  $$W = \frac{1}{M} \sum_{m=1}^M s_m^2 = \frac{1}{M (N - 1)} \sum_{m=1}^M \sum_{i=1}^N (\theta_{mi} - \bar{\theta}_m)^2$$
- The estimated marginal posterior variance is:
  $$\widehat{\text{Var}}(\theta) = \frac{N - 1}{N} W + \frac{1}{N} B$$
- The convergence metric $\hat{R}$ is defined as:
  $$\hat{R} = \sqrt{\frac{\widehat{\text{Var}}(\theta)}{W}}$$

**Convergence Rule**:
- If chains have converged and thoroughly mixed, $B \to 0$ and $\hat{R} \to 1.0$.
- In modern practice (Gelman et al., 2013), sampling is declared converged if **$\hat{R} < 1.05$** (or strictly $\hat{R} < 1.01$ for critical inferences) across all monitored parameters.
"""

marker = "## Fully worked question 1:"
idx = text.find(marker)
new_text = text[:idx] + addition.strip() + "\n\n" + text[idx:]

with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated Unit 5 successfully!")
