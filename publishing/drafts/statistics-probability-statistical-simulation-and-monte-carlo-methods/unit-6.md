# Unit 6: Markov Chain Monte Carlo (MCMC): Metropolis-Hastings Algorithms

In Bayesian statistics, statistical physics, and spatial econometrics, posterior probability distributions often involve high-dimensional parameter spaces ($\mathbf{\theta} \in \mathbb{R}^p$ where $p \ge 10$) with intractable normalizing constants:
$$\pi(\mathbf{\theta} \mid \mathbf{y}) = \frac{p(\mathbf{y} \mid \mathbf{\theta}) p(\mathbf{\theta})}{\int_{\Theta} p(\mathbf{y} \mid \mathbf{\theta}) p(\mathbf{\theta})\,d\mathbf{\theta}}$$
In high dimensions, standard rejection sampling and importance sampling fail catastrophically because the volume of the proposal density's support dwarfs the region of high target posterior density, causing acceptance rates and effective sample sizes to drop to zero.

**Markov Chain Monte Carlo (MCMC)** overcomes this limitation by constructing an ergodic Markov chain whose stationary invariant distribution is *identically equal* to the target distribution $\pi(\mathbf{\theta} \mid \mathbf{y})$. Instead of generating independent draws, MCMC produces a dependent sequence of states that explores the high-probability contours of the parameter space.

## 6.1 Markov Chain Foundations: Ergodicity and Detailed Balance

Let $\{\mathbf{X}_0, \mathbf{X}_1, \mathbf{X}_2, \dots\}$ be a discrete-time, continuous-state Markov chain defined on state space $\mathcal{X} \subseteq \mathbb{R}^p$.
The chain is governed by a **transition kernel** $P(\mathbf{x}, \mathcal{A}) = P(\mathbf{X}_{t+1} \in \mathcal{A} \mid \mathbf{X}_t = \mathbf{x})$. When the transition kernel admits a transition density $K(\mathbf{x}, \mathbf{y})$:
$$P(\mathbf{x}, d\mathbf{y}) = K(\mathbf{x}, \mathbf{y})\,d\mathbf{y} + r(\mathbf{x}) \delta_{\mathbf{x}}(d\mathbf{y})$$
where $r(\mathbf{x}) = 1 - \int K(\mathbf{x}, \mathbf{y})\,d\mathbf{y}$ is the probability of remaining at $\mathbf{x}$.

### 1. Invariance and Detailed Balance
A probability density $\pi(\mathbf{x})$ is a **stationary (invariant) distribution** for the Markov chain if:
$$\pi(\mathbf{y}) = \int_{\mathcal{X}} \pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y})\,d\mathbf{x} \quad \text{for all } \mathbf{y} \in \mathcal{X}$$

A sufficient (though not strictly necessary) condition for $\pi(\mathbf{x})$ to be stationary is the **Detailed Balance (Reversibility)** condition:

$$\pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x}) \quad \text{for all } \mathbf{x}, \mathbf{y} \in \mathcal{X}$$

*Proof that Detailed Balance Implies Invariance*:
Integrating both sides of detailed balance with respect to $\mathbf{x}$:
$$\int_{\mathcal{X}} \pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y})\,d\mathbf{x} = \int_{\mathcal{X}} \pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x})\,d\mathbf{x} = \pi(\mathbf{y}) \int_{\mathcal{X}} K(\mathbf{y}, \mathbf{x})\,d\mathbf{x}$$
Since $K(\mathbf{y}, \mathbf{x})$ is a probability density integrating to 1 over $\mathcal{X}$:
$$\int_{\mathcal{X}} \pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y})\,d\mathbf{x} = \pi(\mathbf{y}) \cdot 1 = \pi(\mathbf{y})$$
Thus, detailed balance guarantees that $\pi(\mathbf{x})$ is the stationary distribution of the chain.

### 2. Ergodicity and the Ergodic Theorem
A Markov chain is **ergodic** if it is:
1. **$\pi$-irreducible**: Every Borel set $\mathcal{A}$ with $\pi(\mathcal{A}) > 0$ can be reached from any starting state in a finite number of steps.
2. **Aperiodic**: The chain does not cycle deterministically between disjoint partitions.
3. **Harris recurrent**: The chain revisits every non-negligible region infinitely often with probability 1.

*Theorem (The Ergodic Theorem / Strong Law for MCMC)*: If a Markov chain $\{\mathbf{X}_t\}$ is ergodic with stationary distribution $\pi$, then for any integrable function $h: \mathcal{X} \to \mathbb{R}$ ($\mathbb{E}_\pi[|h|] < \infty$), the empirical trajectory average converges almost surely to the true expectation:

$$\lim_{N \to \infty} \frac{1}{N} \sum_{t=1}^N h(\mathbf{X}_t) = \mathbb{E}_\pi[h(\mathbf{X})] \quad \text{almost surely}$$
regardless of the initial starting state $\mathbf{X}_0$.

## 6.2 The Metropolis-Hastings Algorithm

In 1953, Nicholas Metropolis, Arianna Rosenbluth, Marshall Rosenbluth, Augusta Teller, and Edward Teller published the seminal Metropolis algorithm for symmetric proposals. In 1970, W. K. Hastings generalized the algorithm to arbitrary, non-symmetric proposal distributions.

### The Metropolis-Hastings Algorithm Mechanics
Let $\pi(\mathbf{x}) = \frac{\tilde{\pi}(\mathbf{x})}{Z}$ be the target probability density, where the normalizing constant $Z$ is unknown.
Let $q(\mathbf{y} \mid \mathbf{x})$ be a candidate **proposal distribution** specifying the probability density of proposing a move from current state $\mathbf{x}$ to candidate state $\mathbf{y}$.

Given current state $\mathbf{X}_t = \mathbf{x}$:
1. **Propose Candidate**: Draw a candidate state $\mathbf{Y} \sim q(\mathbf{y} \mid \mathbf{x})$.
2. **Compute Acceptance Probability**:
   $$\alpha(\mathbf{x}, \mathbf{Y}) = \min\left( 1, \; \frac{\pi(\mathbf{Y}) q(\mathbf{x} \mid \mathbf{Y})}{\pi(\mathbf{x}) q(\mathbf{Y} \mid \mathbf{x})} \right) = \min\left( 1, \; \frac{\tilde{\pi}(\mathbf{Y}) q(\mathbf{x} \mid \mathbf{Y})}{\tilde{\pi}(\mathbf{x}) q(\mathbf{Y} \mid \mathbf{x})} \right)$$
   Notice that the intractable normalizing constant $Z$ cancels out identically in the ratio $\frac{\tilde{\pi}(\mathbf{Y})/Z}{\tilde{\pi}(\mathbf{x})/Z}$!
3. **Acceptance Step**:
   - Draw $U \sim \mathcal{U}(0, 1)$.
   - If $U \le \alpha(\mathbf{x}, \mathbf{Y})$, **accept** the proposal: $\mathbf{X}_{t+1} = \mathbf{Y}$.
   - Otherwise, **reject** the proposal: $\mathbf{X}_{t+1} = \mathbf{x}$ (the chain remains at the current state).

### Proof of Detailed Balance
The effective transition density for a move from $\mathbf{x} \ne \mathbf{y}$ is:
$$K(\mathbf{x}, \mathbf{y}) = q(\mathbf{y} \mid \mathbf{x}) \alpha(\mathbf{x}, \mathbf{y})$$
Assume without loss of generality that $\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \le \pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})$.
Then:
$$\alpha(\mathbf{x}, \mathbf{y}) = \frac{\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})}{\pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})}, \quad \text{while} \quad \alpha(\mathbf{y}, \mathbf{x}) = 1$$
We evaluate the forward probability flow:
$$\pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x}) \left( \frac{\pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})}{\pi(\mathbf{x}) q(\mathbf{y} \mid \mathbf{x})} \right) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})$$
We evaluate the reverse probability flow:
$$\pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x}) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \alpha(\mathbf{y}, \mathbf{x}) = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y}) \cdot 1 = \pi(\mathbf{y}) q(\mathbf{x} \mid \mathbf{y})$$
Both flows are strictly equal:
$$\pi(\mathbf{x}) K(\mathbf{x}, \mathbf{y}) \equiv \pi(\mathbf{y}) K(\mathbf{y}, \mathbf{x})$$
Detailed balance holds exactly.

## 6.3 Proposal Mechanisms and the 0.234 Optimal Tuning Rule

The statistical performance and mixing speed of Metropolis-Hastings depends critically on the proposal density $q(\mathbf{y} \mid \mathbf{x})$.

### 1. Random-Walk Metropolis-Hastings
The candidate is generated by adding a zero-mean random perturbation $\mathbf{\epsilon}$ to the current state:
$$\mathbf{Y} = \mathbf{x} + \mathbf{\epsilon}, \quad \mathbf{\epsilon} \sim g(\mathbf{\epsilon})$$
where $g(\mathbf{\epsilon})$ is symmetric ($g(\mathbf{\epsilon}) = g(-\mathbf{\epsilon})$), such as a Gaussian $\mathcal{N}(\mathbf{0}, \sigma_{\text{prop}}^2 \mathbf{I})$.
Because $q(\mathbf{y} \mid \mathbf{x}) = g(\mathbf{y} - \mathbf{x}) = g(\mathbf{x} - \mathbf{y}) = q(\mathbf{x} \mid \mathbf{y})$, the proposal ratio cancels to 1:
$$\alpha(\mathbf{x}, \mathbf{y}) = \min\left( 1, \; \frac{\pi(\mathbf{y})}{\pi(\mathbf{x})} \right)$$
This recovers the original **Metropolis Algorithm**.

**The Proposal Scale Dilemma**:
- If proposal scale $\sigma_{\text{prop}}$ is **too small**: Candidates $\mathbf{y}$ are close to $\mathbf{x}$, resulting in very high acceptance ($\alpha \approx 100\%$), but the chain moves via minuscule Brownian diffusion, taking millions of iterations to traverse the target distribution (high autocorrelation, poor mixing).
- If proposal scale $\sigma_{\text{prop}}$ is **too large**: Candidates land in low-probability tail regions where $\pi(\mathbf{y}) \ll \pi(\mathbf{x})$, resulting in near-zero acceptance ($\alpha \approx 0\%$). The chain gets stuck at the same state for thousands of iterations.

### 2. The Roberts-Gelman-Gilks Optimal Scaling Rule (0.234)
In 1997, Gareth Roberts, Andrew Gelman, and Walter Gilks published a foundational asymptotic theorem:
*Theorem (Roberts, Gelman, & Gilks, 1997)*: For an i.i.d. target distribution in $d$-dimensional Euclidean space $\mathbb{R}^d$ as $d \to \infty$, the optimal proposal standard deviation that maximizes the speed of diffusion of the Markov chain scales as:
$$\sigma_{\text{prop}}^* \approx \frac{2.38}{\sqrt{d}} \sigma_{\text{target}}$$
Under this optimal scaling, the asymptotic average acceptance rate converges to:

$$\alpha^* \approx 0.234 \quad (23.4\%)$$

For 1-dimensional targets, the optimal acceptance rate is approximately $44\%$; for $d \ge 5$ dimensions, tuning the proposal variance to maintain an acceptance rate between **$20\%$ and $25\%$** provides optimal mixing.

## 6.4 MCMC Convergence Diagnostics

Because MCMC samples are auto-correlated and depend on the initial arbitrary starting state $\mathbf{X}_0$, analysts must determine when the chain has reached stationarity (the **burn-in period**) and assess the precision of trajectory estimates.

### 1. Burn-In and Trace Plots
- **Burn-In Period ($B$)**: Early iterations ($t = 1, \dots, B$) generated while the chain travels from the starting point $\mathbf{X}_0$ toward the mode of $\pi$ are discarded:
  $$\hat{\theta} = \frac{1}{N - B} \sum_{t=B+1}^N h(\mathbf{X}_t)$$
- **Trace Plots**: Plotting state values $X_t$ against iteration number $t$. A healthy chain exhibits a "hairy caterpillar" appearance, oscillating rapidly without secular drift.

### 2. Autocorrelation and Effective Sample Size (ESS)
Due to positive serial correlation $\rho_k = \mathrm{Corr}(X_t, X_{t+k})$, the variance of the sample mean is inflated by the **Integrated Autocorrelation Time (IACT)**:
$$\tau = 1 + 2 \sum_{k=1}^\infty \rho_k$$
$$\mathrm{Var}(\hat{\theta}) \approx \frac{\sigma^2}{N} \tau$$
The **Effective Sample Size (ESS)** represents the number of equivalent independent draws:

$$\text{ESS} = \frac{N}{\tau} = \frac{N}{1 + 2 \sum_{k=1}^\infty \rho_k}$$

If $N = 10,000$ and $\tau = 20$, the chain contains only $\text{ESS} = 500$ independent pieces of statistical information.

### 3. The Gelman-Rubin Diagnostic ($\hat{R}$)
Andrew Gelman and Donald Rubin (1992) introduced the standard multi-chain convergence metric:
- Run $M \ge 3$ parallel chains with overdispersed initial values for $N$ iterations.
- Compute the **Between-Chain Variance** $B / N$ and **Within-Chain Variance** $W$.
- The estimated marginal posterior variance is:
  $$\hat{V} = \frac{N - 1}{N} W + \frac{M + 1}{M \cdot N} B$$
- The **Potential Scale Reduction Factor (PSRF)** is:
  $$\hat{R} = \sqrt{\frac{\hat{V}}{W}}$$
At convergence, between-chain variance vanishes, and $\hat{R} \to 1.0$. As a regulatory and scientific convention, convergence is diagnosed when:
$$\hat{R} < 1.05 \quad (\text{or } \hat{R} < 1.01 \text{ for rigorous clinical trials})$$

## Fully worked question 1: Random-Walk Metropolis on an Unnormalized Mixture

### Question
An astronomer models stellar brightness using an unnormalized bimodal Gaussian mixture density:
$$\tilde{\pi}(x) = 0.40 \exp\left( -\frac{(x + 2)^2}{2} \right) + 0.60 \exp\left( -\frac{(x - 3)^2}{4} \right) \quad \text{for } x \in \mathbb{R}$$
The astronomer runs a Random-Walk Metropolis algorithm with Gaussian proposal:
$$Y \sim \mathcal{N}(x_t, \sigma_{\text{prop}}^2 = 1.0)$$
The chain is currently at state $x_0 = 1.0$.
1. Compute the unnormalized target density at current state $\tilde{\pi}(1.0)$.
2. A random draw from the proposal distribution yields candidate $Y = 2.20$.
   - Compute the unnormalized target density $\tilde{\pi}(2.20)$.
   - Calculate the exact Metropolis acceptance probability $\alpha(1.0, 2.20)$.
3. Given a uniform draw $u = 0.750$, determine whether the candidate is accepted or rejected, and specify state $x_1$.

### Solution, step 1: Evaluation of Current State Density $\tilde{\pi}(1.0)$
The target function is:
$$\tilde{\pi}(x) = 0.40 e^{-(x + 2)^2 / 2} + 0.60 e^{-(x - 3)^2 / 4}$$
Evaluating at $x_0 = 1.0$:
- Term 1:
  $$(x + 2)^2 = (1.0 + 2)^2 = 3^2 = 9 \implies -\frac{9}{2} = -4.5$$
  $$e^{-4.5} \approx 0.011109 \implies 0.40 \times 0.011109 \approx 0.004444$$
- Term 2:
  $$(x - 3)^2 = (1.0 - 3)^2 = (-2)^2 = 4 \implies -\frac{4}{4} = -1.0$$
  $$e^{-1.0} \approx 0.367879 \implies 0.60 \times 0.367879 \approx 0.220728$$

Summing the terms:
$$\tilde{\pi}(1.0) = 0.004444 + 0.220728 = 0.225172$$

### Solution, step 2: Candidate Density $\tilde{\pi}(2.20)$ and Acceptance Probability
Evaluating at candidate $Y = 2.20$:
- Term 1:
  $$(x + 2)^2 = (2.20 + 2)^2 = 4.20^2 = 17.64 \implies -\frac{17.64}{2} = -8.82$$
  $$e^{-8.82} \approx 0.0001477 \implies 0.40 \times 0.0001477 \approx 0.000059$$
- Term 2:
  $$(x - 3)^2 = (2.20 - 3)^2 = (-0.80)^2 = 0.64 \implies -\frac{0.64}{4} = -0.16$$
  $$e^{-0.16} \approx 0.852144 \implies 0.60 \times 0.852144 \approx 0.511286$$

Summing the terms:
$$\tilde{\pi}(2.20) = 0.000059 + 0.511286 = 0.511345$$

Because the proposal is symmetric (Gaussian random walk, $q(y|x) = q(x|y)$):
$$\alpha(1.0, 2.20) = \min\left( 1, \; \frac{\tilde{\pi}(2.20)}{\tilde{\pi}(1.0)} \right) = \min\left( 1, \; \frac{0.511345}{0.225172} \right)$$
$$\frac{0.511345}{0.225172} \approx 2.2709$$
Since the ratio exceeds 1.0:
$$\alpha(1.0, 2.20) = 1.0000 \quad (100\%)$$
The proposed move is toward a state of higher probability density, so it is accepted deterministically.

### Solution, step 3: Evaluation of Acceptance Step
The uniform filter draw is $u = 0.750$.
Comparing $u \le \alpha$:
$$u = 0.750 \le 1.0000$$
The move is **accepted**!
The new state of the Markov chain is:
$$x_1 = 2.20$$

## Fully worked question 2: Independence Metropolis-Hastings with Asymmetric Proposal

### Question
A Bayesian statistician samples an unnormalized target posterior density:
$$\tilde{\pi}(x) = x^3 e^{-x} \quad \text{for } x > 0 \quad (\text{a Gamma}(4, 1) \text{ distribution})$$
using an **Independence Metropolis-Hastings sampler** with exponential proposal:
$$q(y \mid x) = g(y) = \frac{1}{3} e^{-y / 3} \quad \text{for } y > 0 \quad (\text{an Exp}(\lambda = 1/3) \text{ distribution})$$
The chain is currently at state $x_t = 3.0$.
1. A candidate is drawn from the proposal distribution: $Y = 6.0$.
   Formulate the exact Metropolis-Hastings acceptance ratio:
   $$\rho(x, y) = \frac{\tilde{\pi}(y) q(x \mid y)}{\tilde{\pi}(x) q(y \mid x)}$$
2. Calculate the acceptance probability $\alpha(3.0, 6.0)$ to 4 decimal places.
3. If the candidate had been $Y = 0.50$, compute the corresponding acceptance probability $\alpha(3.0, 0.50)$.

### Solution, step 1: Algebraic Formulation of the Acceptance Ratio
For an independence sampler, $q(y \mid x) = g(y)$ and $q(x \mid y) = g(x)$.
The ratio is:
$$\rho(x, y) = \frac{\tilde{\pi}(y) g(x)}{\tilde{\pi}(x) g(y)} = \frac{y^3 e^{-y} \cdot \frac{1}{3} e^{-x/3}}{x^3 e^{-x} \cdot \frac{1}{3} e^{-y/3}} = \left( \frac{y}{x} \right)^3 \frac{e^{-y + x/3}}{e^{-x + y/3}} = \left( \frac{y}{x} \right)^3 \exp\left( -(y - x) + \frac{1}{3}(x - y) \right)$$
$$\rho(x, y) = \left( \frac{y}{x} \right)^3 \exp\left( -\frac{4}{3}(y - x) \right)$$

### Solution, step 2: Calculation for $x = 3.0$ and $Y = 6.0$
Given $x = 3.0$ and $y = 6.0$:
- Coordinate ratio:
  $$\frac{y}{x} = \frac{6.0}{3.0} = 2.0 \implies \left( \frac{y}{x} \right)^3 = 2.0^3 = 8.0$$
- Coordinate difference:
  $$y - x = 6.0 - 3.0 = +3.0$$
  $$-\frac{4}{3}(y - x) = -\frac{4}{3} \times 3.0 = -4.0$$
- Exponential factor:
  $$e^{-4.0} \approx 0.0183156$$

The acceptance ratio is:
$$\rho(3.0, 6.0) = 8.0 \times 0.0183156 \approx 0.146525$$
The acceptance probability is:
$$\alpha(3.0, 6.0) = \min(1, \; 0.146525) \approx 0.1465 \quad (14.65\%)$$

### Solution, step 3: Calculation for $x = 3.0$ and $Y = 0.50$
Given $x = 3.0$ and $y = 0.50$:
- Coordinate ratio:
  $$\frac{y}{x} = \frac{0.50}{3.0} = \frac{1}{6} \implies \left( \frac{y}{x} \right)^3 = \frac{1}{216} \approx 0.0046296$$
- Coordinate difference:
  $$y - x = 0.50 - 3.0 = -2.50$$
  $$-\frac{4}{3}(y - x) = -\frac{4}{3} \times (-2.50) = +\frac{10}{3} \approx +3.33333$$
- Exponential factor:
  $$e^{10/3} \approx e^{3.33333} \approx 28.0316$$

The acceptance ratio is:
$$\rho(3.0, 0.50) = \frac{1}{216} \times 28.0316 \approx 0.129776$$
The acceptance probability is:
$$\alpha(3.0, 0.50) = \min(1, \; 0.129776) \approx 0.1298 \quad (12.98\%)$$

*Insight*: The independence sampler penalizes candidate proposals in both tails because the proposal density $g(y) = \frac{1}{3} e^{-y/3}$ fails to match the Gamma shape ($y^3 e^{-y}$), demonstrating why proposal matching is vital.

## Fully worked question 3: Effective Sample Size and Gelman-Rubin Convergence Diagnostic

### Question
Two parallel MCMC chains ($M = 2$) are run to estimate a posterior parameter $\theta$.
Each chain is run for $N = 1,000$ iterations after discarding burn-in:
- **Chain 1**: Sample mean $\bar{X}_1 = 10.40$, sample variance $s_1^2 = 4.20$.
- **Chain 2**: Sample mean $\bar{X}_2 = 10.80$, sample variance $s_2^2 = 4.60$.
- The estimated lag-1 autocorrelation within chains is $\hat{\rho}_1 = 0.70$, with negligible higher-order autocorrelations ($\hat{\rho}_k \approx 0$ for $k \ge 2$).

1. Compute the Within-Chain Variance $W$, Between-Chain Variance $B$, and the Gelman-Rubin diagnostic $\hat{R}$.
2. Determine whether the chains have successfully achieved convergence according to the standard threshold $\hat{R} < 1.05$.
3. Compute the Effective Sample Size (ESS) for a combined sample of $2,000$ draws.

### Solution, step 1: Computation of Within and Between Variances and $\hat{R}$
Let $M = 2$ chains of length $N = 1,000$.
1. **Within-Chain Variance ($W$)**:
   $$W = \frac{1}{M} \sum_{m=1}^M s_m^2 = \frac{s_1^2 + s_2^2}{2} = \frac{4.20 + 4.60}{2} = \frac{8.80}{2} = 4.40$$

2. **Overall Mean**:
   $$\bar{X} = \frac{\bar{X}_1 + \bar{X}_2}{2} = \frac{10.40 + 10.80}{2} = 10.60$$

3. **Between-Chain Variance ($B$)**:
   $$\frac{B}{N} = \frac{1}{M - 1} \sum_{m=1}^M (\bar{X}_m - \bar{X})^2 = (10.40 - 10.60)^2 + (10.80 - 10.60)^2 = (-0.20)^2 + (0.20)^2 = 0.04 + 0.04 = 0.08$$
   $$B = N \times 0.08 = 1,000 \times 0.08 = 80.0$$

4. **Pooled Marginal Posterior Variance ($\hat{V}$)**:
   $$\hat{V} = \frac{N - 1}{N} W + \frac{M + 1}{M \cdot N} B = \frac{999}{1000} (4.40) + \frac{3}{2 \times 1000} (80.0)$$
   $$\hat{V} = (0.999 \times 4.40) + (0.0015 \times 80.0) = 4.3956 + 0.1200 = 4.5156$$

5. **Gelman-Rubin Statistic ($\hat{R}$)**:
   $$\hat{R} = \sqrt{\frac{\hat{V}}{W}} = \sqrt{\frac{4.5156}{4.40}} = \sqrt{1.02627} \approx 1.01305 \approx 1.013$$

### Solution, step 2: Convergence Assessment
The calculated potential scale reduction factor is:
$$\hat{R} = 1.013$$
Since $\hat{R} = 1.013 < 1.05$ (and even satisfies the ultra-strict threshold $\hat{R} < 1.02$), between-chain variation is negligible compared to within-chain variation. The chains have successfully converged to a common stationary posterior distribution.

### Solution, step 3: Calculation of Effective Sample Size (ESS)
Given lag-1 autocorrelation $\hat{\rho}_1 = 0.70$ and $\hat{\rho}_k \approx 0$ for $k \ge 2$:
The integrated autocorrelation time is:
$$\tau \approx 1 + 2 \hat{\rho}_1 = 1 + 2(0.70) = 1 + 1.40 = 2.40$$

For the combined simulation sample of $N_{\text{total}} = M \times N = 2 \times 1,000 = 2,000$ draws:
$$\text{ESS} = \frac{N_{\text{total}}}{\tau} = \frac{2,000}{2.40} = \frac{2,000}{2.4} \approx 833.3 \approx 833 \text{ independent draws}$$
Even though $2,000$ correlated iterations were executed, the statistical precision of the posterior mean estimate is equivalent to only $833$ independent Monte Carlo draws.


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


## 6.14 Multimodal Target Distributions and Parallel Tempering

When the target posterior $\pi(\mathbf{x})$ possesses multiple isolated modes separated by deep valleys of near-zero probability, standard Random Walk Metropolis and Hamiltonian Monte Carlo fail completely: the proposal probability of crossing an energy barrier decays exponentially with barrier height, trapping the chain in a single local mode for millions of iterations.

Charles J. Geyer (1991) and Koji Hukushima and Koji Nemoto (1996) introduced **Parallel Tempering** (also known as **Replica Exchange MCMC**) to traverse multimodal landscapes.

### 1. The Tempered Ladder System
We construct an ensemble of $K$ parallel replicas running at different "temperatures" indexed by inverse temperatures (temperatures $\beta_k \in (0, 1]$):
$$1 = \beta_1 > \beta_2 > \dots > \beta_K > 0$$
Each replica $k$ explores a tempered target distribution:
$$\pi_k(\mathbf{x}) \propto [\pi(\mathbf{x})]^{\beta_k} = \exp\left( -\beta_k U(\mathbf{x}) \right)$$
- At the target temperature $\beta_1 = 1$, $\pi_1(\mathbf{x}) = \pi(\mathbf{x})$ is the exact cold distribution of scientific interest.
- At high temperatures ($\beta_K \ll 1$), the potential energy barriers are flattened: high-temperature chains diffuse effortlessly between isolated modes.

### 2. Replica Swap Moves
In addition to standard MCMC updates within each chain, the algorithm proposes swapping states between adjacent temperature rungs $\mathbf{x}_j$ and $\mathbf{x}_{j+1}$ with Metropolis-Hastings acceptance probability:
$$\alpha_{\text{swap}} = \min\left( 1, \frac{\pi_j(\mathbf{x}_{j+1}) \pi_{j+1}(\mathbf{x}_j)}{\pi_j(\mathbf{x}_j) \pi_{j+1}(\mathbf{x}_{j+1})} \right) = \min\left( 1, \exp\left( (\beta_j - \beta_{j+1}) [U(\mathbf{x}_j) - U(\mathbf{x}_{j+1})] \right) \right)$$

When a high-temperature chain discovers a new mode, the swap moves propagate that state downward through the temperature ladder to the cold target chain $\beta_1 = 1$, achieving ergodic mixing across severely fractured multimodal posteriors.


## 5.16 Computational Laboratory: Diagnosing MCMC Pathologies in Neal's Funnel

A classic benchmark for diagnosing MCMC algorithms in hierarchical Bayesian modeling is **Neal's Funnel**:
$$y \sim \mathcal{N}(0, 3^2), \quad x_i \sim \mathcal{N}(0, e^y), \quad i = 1, \dots, 9$$
In this 10-dimensional distribution, as $y$ becomes negative, the variance of $x_i$ shrinks exponentially, forming a narrow, high-curvature "neck" (the funnel).

When testing algorithms on $10^5$ iterations:
- **Random Walk Metropolis**: Becomes completely trapped in the wide opening of the funnel ($y > 0$), failing to visit the narrow neck and yielding an erroneous $\hat{R} = 1.34$.
- **Standard HMC with Fixed Step Size**: Experiences widespread divergent transitions as the particle bounces uncontrollably in the high-curvature neck where gradients explode.
- **NUTS with Adaptive Dual Averaging and Non-Centered Parameterization**: Setting $\tilde{x}_i \sim \mathcal{N}(0, 1)$ with $x_i = \tilde{x}_i e^{y/2}$ completely untangles the funnel geometry, eliminating all divergences and achieving $\hat{R} \le 1.002$ across all parameters.


## 6.15 Unit 6 Review and Methodological Synthesis

Unit 6 developed the mathematical foundations of Markov Chain Monte Carlo (MCMC) algorithms. We established the conditions of $\pi$-irreducibility, aperiodicity, and Harris recurrence necessary to guarantee that the transition kernel $K(\mathbf{x}, \cdot)$ converges in total variation to the stationary distribution $\pi$. We formulated the Metropolis-Hastings algorithm, proving that enforcing the detailed balance condition $\pi(\mathbf{x}) T(\mathbf{x}, \mathbf{y}) = \pi(\mathbf{y}) T(\mathbf{y}, \mathbf{x})$ guarantees $\pi$ invariance. We analyzed Random Walk Metropolis and the Roberts-Gelman-Gilks optimal scaling theorem, which proves that in high dimensions, the optimal proposal dispersion yields an acceptance rate of exactly $23.4\%$. We analyzed geometric ergodicity through Foster-Lyapunov drift and minorization conditions, linking exponential convergence to the existence of a positive absolute spectral gap. Finally, we surveyed convergence diagnostics, detailing rank-normalized split-$\hat{R}$, effective sample size (ESS) based on integrated autocorrelation time, and parallel tempering for navigating multimodal posterior landscapes.


## 6.16 Convergence Assessment via the Geweke Spectral Diagnostic

While the Gelman-Rubin $\hat{R}$ statistic requires running multiple independent parallel Markov chains, John Geweke (1992) proposed a spectral time-series diagnostic for evaluating the stationarity of a single MCMC chain.

Geweke's method compares the sample mean of the early portion of the chain (typically the first $10\%$, denoted $\bar{X}_A$) with the sample mean of the concluding portion of the chain (typically the last $50\%$, denoted $\bar{X}_B$), omitting the middle $40\%$ to ensure independence between the two windows. The test statistic is a two-sample asymptotic z-score:
$$Z = \frac{\bar{X}_A - \bar{X}_B}{\sqrt{\frac{\hat{S}_A(0)}{n_A} + \frac{\hat{S}_B(0)}{n_B}}}$$
where $\hat{S}_A(0)$ and $\hat{S}_B(0)$ are spectral density estimates of the asymptotic variance at zero frequency, computed using Parzen or Tukey-Hanning spectral windows to account for serial autocorrelation. Under the null hypothesis that the Markov chain has achieved stationarity, $Z$ is asymptotically distributed as standard normal $\mathcal{N}(0, 1)$. Values of $|Z| > 2$ provide strong statistical evidence of non-stationarity, warning the analyst that burn-in was insufficient.
