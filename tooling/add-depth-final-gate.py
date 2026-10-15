# tooling/add-depth-final-gate.py

# 1. Expand Unit 7
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "r", encoding="utf-8") as f:
    u7 = f.read()

u7_addition = r"""

---

## 7.9 Stochastic Variance Reduction: SVRG, SAGA, and Wolfe Line-Search Conditions

While Stochastic Gradient Descent (SGD) achieves rapid early progress in large-scale machine learning, its constant gradient noise variance $\mathbb{E}[\|\mathbf{g}_{\mathcal{B}} - \nabla f\|^2] \ge \sigma^2 > 0$ forces the algorithm to use decaying step sizes, slowing its asymptotic convergence rate from linear to sub-linear $\mathcal{O}(1/t)$.

To overcome this fundamental limitation, Rie Johnson and Tong Zhang (2013) formulated **Stochastic Variance Reduced Gradient (SVRG)**, while Aaron Defazio, Francis Bach, and Simon Lacoste-Julien (2014) developed **SAGA**.

### The SVRG Algorithmic Architecture
SVRG operates in two nested loops: an outer epoch loop and an inner stochastic update loop.
1. **Outer Epoch Loop**:
   At the beginning of each epoch, compute the **exact full-sample gradient** across all $n$ observations at snapshot parameter $\tilde{\boldsymbol{\theta}}$:
   $$\tilde{\boldsymbol{\mu}} = \nabla f(\tilde{\boldsymbol{\theta}}) = \frac{1}{n} \sum_{i=1}^n \nabla f_i(\tilde{\boldsymbol{\theta}})$$
2. **Inner Stochastic Loop**:
   For $m$ steps (typically $m \approx 2n$), draw a single random observation index $i_t \in \{1, \dots, n\}$ and compute the **variance-reduced gradient estimator**:
   $$\mathbf{v}_t = \nabla f_{i_t}(\boldsymbol{\theta}_t) - \nabla f_{i_t}(\tilde{\boldsymbol{\theta}}) + \tilde{\boldsymbol{\mu}}$$
   Update the parameter:
   $$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \gamma \mathbf{v}_t$$

#### Unbiasedness and Variance Decay:
Notice that:
$$\mathbb{E}[\mathbf{v}_t \mid \boldsymbol{\theta}_t] = \mathbb{E}[\nabla f_{i_t}(\boldsymbol{\theta}_t)] - \mathbb{E}[\nabla f_{i_t}(\tilde{\boldsymbol{\theta}})] + \tilde{\boldsymbol{\mu}} = \nabla f(\boldsymbol{\theta}_t) - \nabla f(\tilde{\boldsymbol{\theta}}) + \nabla f(\tilde{\boldsymbol{\theta}}) = \nabla f(\boldsymbol{\theta}_t)$$
The estimator $\mathbf{v}_t$ is strictly unbiased!
Furthermore, as $\boldsymbol{\theta}_t$ and $\tilde{\boldsymbol{\theta}}$ both converge to the true optimum $\boldsymbol{\theta}^*$:
$$\nabla f_{i_t}(\boldsymbol{\theta}_t) - \nabla f_{i_t}(\tilde{\boldsymbol{\theta}}) \to \mathbf{0} \quad \text{and} \quad \tilde{\boldsymbol{\mu}} \to \mathbf{0}$$
The variance of $\mathbf{v}_t$ **asymptotically vanishes to zero** ($\text{Var}(\mathbf{v}_t) \to 0$) without requiring step size decay! Consequently, SVRG achieves **geometric linear convergence** $\mathcal{O}(\rho^k)$ like full-batch gradient descent, while requiring only two gradient evaluations per step.

### The Wolfe Conditions for Quasi-Newton Line Search

In Quasi-Newton optimization (BFGS / L-BFGS), inexact line searches along search direction $\mathbf{p}_k$ must choose step size $\alpha_k$ to satisfy the **Wolfe Conditions**:

1. **Sufficient Decrease (Armijo Condition)**:
   $$f(\boldsymbol{\theta}_k + \alpha_k \mathbf{p}_k) \le f(\boldsymbol{\theta}_k) + c_1 \alpha_k \nabla f(\boldsymbol{\theta}_k)^\top \mathbf{p}_k$$
   where $0 < c_1 < 1$ (typically $c_1 = 10^{-4}$). This prevents the step from being too large.

2. **Curvature Condition**:
   $$\nabla f(\boldsymbol{\theta}_k + \alpha_k \mathbf{p}_k)^\top \mathbf{p}_k \ge c_2 \nabla f(\boldsymbol{\theta}_k)^\top \mathbf{p}_k$$
   where $c_1 < c_2 < 1$ (typically $c_2 = 0.9$ for BFGS). This guarantees that the slope has decreased sufficiently, preventing steps from being infinitesimally small.

The **Strong Wolfe Conditions** restrict the absolute curvature:
$$|\nabla f(\boldsymbol{\theta}_k + \alpha_k \mathbf{p}_k)^\top \mathbf{p}_k| \le c_2 |\nabla f(\boldsymbol{\theta}_k)^\top \mathbf{p}_k|$$
Satisfying the Strong Wolfe conditions guarantees that the displacement vectors $\mathbf{s}_k = \alpha_k \mathbf{p}_k$ and $\mathbf{y}_k = \nabla f_{k+1} - \nabla f_k$ satisfy the positive definiteness condition:
$$\mathbf{s}_k^\top \mathbf{y}_k > 0$$
ensuring that the BFGS updated inverse Hessian approximation $\mathbf{B}_{k+1}$ remains strictly positive definite at every iteration.
"""

marker = "## Fully worked question 1:"
idx = u7.find(marker)
u7_new = u7[:idx] + u7_addition.strip() + "\n\n" + u7[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "w", encoding="utf-8") as f:
    f.write(u7_new)
print("Expanded Unit 7 extra!")

# 2. Expand Unit 6
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "r", encoding="utf-8") as f:
    u6 = f.read()

u6_addition = r"""

---

## 6.9 Subsampling, the m-out-of-n Bootstrap, and Infinitesimal Jackknife Influence Functions

While Efron's standard non-parametric bootstrap (resampling $n$ items from a sample of size $n$) is asymptotically valid for smooth statistics, it fails dramatically in non-regular estimation problems:
- Estimating the support boundary of a uniform distribution: $\hat{\theta} = \max(X_1, \dots, X_n)$.
- Extreme order statistics.
- Parameter estimation on boundaries of parameter spaces.
- Non-differentiable estimators (e.g. cube-root asymptotics in Manski's maximum score estimator).

In these non-regular contexts, the bootstrap distribution $\hat{F}^*$ does not converge to the true asymptotic distribution of the estimator:
$$\sup_x |\mathbb{P}^*(\sqrt{n}(\hat{\theta}^* - \hat{\theta}) \le x) - \mathbb{P}(\sqrt{n}(\hat{\theta} - \theta) \le x)| \nrightarrow 0$$

### The m-out-of-n Bootstrap (Bickel, Götze, and van Zwet, 1997)

To restore bootstrap consistency across non-regular and heavy-tailed estimation problems, Peter Bickel, Friedrich Götze, and Willem van Zwet formulated the **$m$-out-of-$n$ Bootstrap**.

#### Algorithmic Formulation:
Instead of drawing resamples of size $n$, the algorithm draws resamples of size $m$, where $m < n$:
$$\mathbf{x}^{*b} = (x_1^{*b}, \dots, x_m^{*b}) \quad \text{sampled with replacement from } \mathbf{x}$$
The sample size $m$ must satisfy two asymptotic scaling conditions:
$$m \to \infty \quad \text{and} \quad \frac{m}{n} \to 0 \quad \text{as } n \to \infty$$
Typically, $m$ is chosen proportional to $n^{2/3}$ or $n^{1/2}$.

#### Why the m-out-of-n Bootstrap Succeeds:
The probability that any specific observation $x_i$ is chosen in an $m$-sized resample is:
$$p_{draw} \approx 1 - \left( 1 - \frac{1}{n} \right)^m \approx 1 - e^{-m/n} \approx \frac{m}{n} \to 0$$
The probability that extreme observations or ties are duplicated drops to zero, smoothing out the empirical distribution and restoring asymptotic consistency for non-smooth, non-regular, and heavy-tailed statistics.

### The Infinitesimal Jackknife and Empirical Influence Curves

In robust statistics, Frank Hampel (1974) introduced the **Influence Function (IF)**, measuring the sensitivity of an estimator functional $T(F)$ to an infinitesimal contamination at point $x$:

$$\text{IF}(x; T, F) = \lim_{\epsilon \to 0} \frac{T((1 - \epsilon)F + \epsilon \delta_x) - T(F)}{\epsilon} = \left. \frac{d}{d\epsilon} T(F + \epsilon (\delta_x - F)) \right|_{\epsilon = 0}$$

where $\delta_x$ is the Dirac point mass at $x$.

#### Jaeckel's Infinitesimal Jackknife:
In 1972, Louis Jaeckel and Bradley Efron translated the influence function into an ultra-fast computational variance estimator: the **Infinitesimal Jackknife**.

Let $\hat{\theta} = T(\hat{F}_n)$ be a plug-in estimator. Associate with each observation $x_i$ a continuous weight $w_i \ge 0$, where the baseline uniform weighting is $\mathbf{w}_0 = (1/n, \dots, 1/n)^\top$.
The **Empirical Influence Value** for observation $i$ is the directional derivative:

$$U_i = \left. \frac{\partial T(\mathbf{w})}{\partial w_i} \right|_{\mathbf{w} = \mathbf{w}_0}$$

The **Infinitesimal Jackknife Variance Estimator** is defined as:

$$v_{IJ} = \frac{1}{n^2} \sum_{i=1}^n U_i^2$$

#### Computational Supremacy:
Unlike the classical delete-1 jackknife (which requires evaluating the estimator $n$ separate times) or the bootstrap (which requires $B$ simulations), the Infinitesimal Jackknife computes the empirical influence values $U_1, \dots, U_n$ analytically or via automatic differentiation in a **single evaluation pass**!

Furthermore, in modern machine learning, Stefan Wager, Trevor Hastie, and Bradley Efron (2014) applied the Infinitesimal Jackknife to compute **standard errors and confidence intervals for Random Forests**, extracting honest prediction uncertainties without requiring nested tree retraining.
"""

marker = "## Fully worked question 1:"
idx = u6.find(marker)
u6_new = u6[:idx] + u6_addition.strip() + "\n\n" + u6[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-6.md", "w", encoding="utf-8") as f:
    f.write(u6_new)
print("Expanded Unit 6 extra!")

# 3. Expand Unit 5
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "r", encoding="utf-8") as f:
    u5 = f.read()

u5_addition = r"""

---

## 5.10 Exact Coupling and Perfect Sampling: Propp–Wilson Coupling from the Past

A universal challenge in Markov Chain Monte Carlo (MCMC) is the **burn-in problem**: how long must a Markov chain run before its distribution is sufficiently close to the stationary target distribution $\pi$?
Standard MCMC heuristics (such as discarding the first 1,000 draws and checking trace plots) can never guarantee that the chain has fully mixed. If the target distribution contains multiple isolated modes, a chain may remain trapped in one local basin for millions of steps, producing heavily biased inferences.

In 1996, James Propp and David Wilson introduced **Coupling from the Past (CFTP)**, an algorithm that generates **exact, perfectly independent, unbiased draws from the stationary distribution $\pi$** without burn-in error!

### The Coupling from the Past (CFTP) Principle

Suppose a Markov chain has a finite state space $\mathcal{S}$ with stationary distribution $\pi$.
If we start $N = |\mathcal{S}|$ independent chains—one starting from **every single possible state in $\mathcal{S}$**—and simulate them forward in time using shared random numbers:
- Due to the random updates, chains will collide and coalesce: once two chains enter the same state at the same time, they share identical future random transitions and remain merged forever.
- However, if we simply run the chains forward until they coalesce at some random forward time $T_{forward}$, the state at $T_{forward}$ is **biased** toward states that facilitate early coalescence!

#### The Propp–Wilson Breakthrough: Backward Coupling
To eliminate forward selection bias, Propp and Wilson realized that the simulation must start in the **past** at time $-T$ and run forward to time $t = 0$:

```text
Propp-Wilson Coupling from the Past (Coalescence at t = 0):
  Time -T_2       Time -T_1                    Time 0
      *---------------+---------------------------*
      |               |                           |
  x_max -------------> \                          |
                        \                         |
  x_mid -----------------\----------------------> X^* (Single Coalesced Exact Draw!)
                         /                        |
  x_min --------------> /                         |
      |               |                           |
      *---------------+---------------------------*
```

1. Start all $|\mathcal{S}|$ chains at past time $-T$ (e.g. $T = 1, 2, 4, 8, 16, \dots$).
2. Simulate all chains forward to time $t = 0$ using a fixed sequence of random update functions:
   $$X_{t+1} = \phi(X_t, U_t), \quad t = -T, \dots, -1$$
   where $U_t \sim \text{i.i.d. Uniform}(0, 1)$ are pre-generated random seeds.
3. Check whether all $|\mathcal{S}|$ chains have **coalesced into a single unique state at time $t = 0$**:
   $$\#\{ X_0(x) : x \in \mathcal{S} \} = 1$$
4. If all chains have coalesced: the single state $X_0$ is an **exact, perfect draw from the stationary distribution $\pi$**!
5. If the chains have not coalesced: double the backward time $T \leftarrow 2T$, reuse the exact same random seeds for times $-T, \dots, -1$, generate new seeds for times $-2T, \dots, -T - 1$, and run forward again.

#### Monotone CFTP (Overcoming Exponential State Spaces):
If the state space has size $|\mathcal{S}| = 2^{1000}$ (such as an Ising spin model in physics or binary spatial random field), tracking all $2^{1000}$ chains is impossible.
Propp and Wilson proved that if the update function $\phi(x, u)$ preserves a partial order on $\mathcal{S}$ (i.e. $x \le y \implies \phi(x, u) \le \phi(y, u)$), one needs to simulate only **two chains**:
1. The chain starting from the **unique minimal state** $\hat{0}$.
2. The chain starting from the **unique maximal state** $\hat{1}$.

Because all intermediate states are mathematically sandwiched between $\hat{0}$ and $\hat{1}$:
$$X_t(\hat{0}) \le X_t(x) \le X_t(\hat{1}) \quad \text{for all } x \in \mathcal{S}$$
When the minimal and maximal chains coalesce ($X_0(\hat{0}) = X_0(\hat{1})$), **every single one of the $2^{1000}$ intermediate chains has coalesced into that exact same state**!
Monotone CFTP delivers exact, perfect Bayesian sampling in polynomial time, completely eliminating MCMC burn-in ambiguity.
"""

marker = "## Fully worked question 1:"
idx = u5.find(marker)
u5_new = u5[:idx] + u5_addition.strip() + "\n\n" + u5[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "w", encoding="utf-8") as f:
    f.write(u5_new)
print("Expanded Unit 5 extra!")

# 4. Expand Unit 8
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "r", encoding="utf-8") as f:
    u8 = f.read()

u8_addition = r"""

---

## 8.9 Declarative System Environment Isolation: Nix, GNU Guix, and Hermetic Builds

In scientific computing, reproducibility failure is most frequently caused not by bugs in the statistical code, but by **environmental drift** in the underlying operating system: differing versions of the C standard library (`glibc`), compiler optimization flags, dynamic link libraries (`libgfortran`), and BLAS/LAPACK implementations.

To achieve bit-for-bit reproducible computational science, researchers deploy **functional declarative package managers: Nix and GNU Guix**.

### The Functional Package Management Architecture

Traditional operating system package managers (Debian `apt`, RedHat `rpm`, macOS `brew`) modify a shared global filesystem root (`/usr/lib`, `/usr/bin`). When a package is updated, existing shared libraries are overwritten, silently mutating the runtime dependencies of existing statistical scripts.

In contrast, Eelco Dolstra's **Nix** (2004) and Ludovic Courtès' **GNU Guix** (2015) treat software deployment as a **pure mathematical function**:

$$\text{Build Output} = f(\text{Source Code}, \, \text{Compiler}, \, \text{Dependencies}, \, \text{Flags})$$

#### Key Architectural Principles:
1. **Content-Addressed Store Paths**:
   Packages are never installed into `/usr/lib`. Every package is installed into its own isolated directory in `/gnu/store/` or `/nix/store/`, prefixed by a cryptographic hash of all its inputs:
   ```text
   /gnu/store/b9x3j7...-r-survival-3.5-0/
   /gnu/store/f4k8a1...-python-scipy-1.11.2/
   ```
   If two statistical projects require different versions of R or SciPy, both versions co-exist on the system without interference.
2. **Hermetic Build Isolation**:
   During compilation, builds are executed inside isolated Linux namespaces with network access disabled and environment variables stripped. Compilers can access only explicitly declared dependencies.
3. **Bit-Reproducible Container Profiles**:
   A single declarative manifest file (`manifest.scm` or `flake.nix`) defines the entire software environment. Running `guix time-machine` allows a researcher to instantiate the exact, byte-for-byte identical computing environment a decade in the future, guaranteeing permanent scientific reproducibility.
"""

marker = "## Fully worked question 1:"
idx = u8.find(marker)
u8_new = u8[:idx] + u8_addition.strip() + "\n\n" + u8[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "w", encoding="utf-8") as f:
    f.write(u8_new)
print("Expanded Unit 8 extra 2!")

# 5. Expand Unit 4
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "r", encoding="utf-8") as f:
    u4 = f.read()

u4_addition = r"""

---

## 4.10 Randomized Linear Algebra: Fast Matrix Multiplication and Leverage Score Sampling

When massive datasets contain billions of rows ($n = 10^9$), even $\mathcal{O}(n p)$ algorithms strain disk I/O and CPU memory bus bandwidth. The field of **Randomized Numerical Linear Algebra (RandNLA)**, pioneered by Petros Drineas and Michael Mahoney (2006), uses non-uniform probability sampling to approximate matrix multiplication and linear regression with provable theoretical error bounds.

### Randomized Matrix Multiplication via Importance Sampling

Suppose we wish to compute the matrix product $\mathbf{C} = \mathbf{A} \mathbf{B}$, where $\mathbf{A} \in \mathbb{R}^{m \times n}$ and $\mathbf{B} \in \mathbb{R}^{n \times p}$.
The exact matrix product is the sum of $n$ outer products of columns of $\mathbf{A}$ and rows of $\mathbf{B}$:
$$\mathbf{A} \mathbf{B} = \sum_{k=1}^n \mathbf{A}_{*, k} \mathbf{B}_{k, *}$$
Evaluating this exact sum requires $2 m n p$ FLOPs.

RandNLA approximates $\mathbf{A} \mathbf{B}$ by sampling a small subset of $c \ll n$ column-row pairs according to non-uniform sampling probabilities $p_k$:

$$p_k = \frac{\|\mathbf{A}_{*, k}\|_2 \|\mathbf{B}_{k, *}\|_2}{\sum_{j=1}^n \|\mathbf{A}_{*, j}\|_2 \|\mathbf{B}_{j, *}\|_2}, \quad \sum_{k=1}^n p_k = 1$$

The randomized estimator constructs sampled matrices $\mathbf{S} \in \mathbb{R}^{m \times c}$ and $\mathbf{R} \in \mathbb{R}^{c \times p}$, scaling each sampled pair by $\frac{1}{\sqrt{c \cdot p_{i_t}}}$:

$$\mathbf{C}_{approx} = \mathbf{S} \mathbf{R} = \frac{1}{c} \sum_{t=1}^c \frac{\mathbf{A}_{*, i_t} \mathbf{B}_{i_t, *}}{p_{i_t}}$$

#### Mathematical Properties:
1. **Strict Unbiasedness**:
   $$\mathbb{E}[\mathbf{C}_{approx}] = \frac{1}{c} \sum_{t=1}^c \sum_{k=1}^n p_k \left( \frac{\mathbf{A}_{*, k} \mathbf{B}_{k, *}}{p_k} \right) = \sum_{k=1}^n \mathbf{A}_{*, k} \mathbf{B}_{k, *} = \mathbf{A} \mathbf{B}$$
2. **Minimal Variance Optimality**:
   Drineas and Mahoney proved that sampling probabilities $p_k \propto \|\mathbf{A}_{*, k}\|_2 \|\mathbf{B}_{k, *}\|_2$ **minimize the Frobenius norm variance $\mathbb{E}[\|\mathbf{A}\mathbf{B} - \mathbf{S}\mathbf{R}\|_F^2]$**.
   The expected approximation error satisfies:
   $$\mathbb{E}[\|\mathbf{A} \mathbf{B} - \mathbf{S} \mathbf{R}\|_F] \le \frac{1}{\sqrt{c}} \|\mathbf{A}\|_F \|\mathbf{B}\|_F$$

### Statistical Leverage Score Sampling for Terabyte Regression

In massive linear regression $\min_{\boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2$ where $\mathbf{X} \in \mathbb{R}^{n \times p}$ has $n = 10^8$ rows, standard OLS is too slow.

Uniform random downsampling of rows introduces severe bias if high-leverage outliers are missed. RandNLA solves this using **Statistical Leverage Score Sampling**:
- Let $\mathbf{X} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top$ be the thin SVD of $\mathbf{X}$.
- The leverage score of row $i$ is the squared Euclidean norm of the $i$-th row of the left singular matrix $\mathbf{U}$:
  $$h_i = \|\mathbf{U}_{i, :}\|_2^2 = \mathbf{x}_i (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i^\top, \quad \sum_{i=1}^n h_i = p$$
- Sample $r = \mathcal{O}(p \log p / \epsilon^2)$ rows from $(\mathbf{X}, \mathbf{y})$ with non-uniform probabilities:
  $$\pi_i = \frac{h_i}{p}$$
- Solve the weighted least squares regression on the tiny $r \times p$ sample:
  $$\hat{\boldsymbol{\beta}}_{sub} = (\tilde{\mathbf{X}}^\top \tilde{\mathbf{X}})^{-1} \tilde{\mathbf{X}}^\top \tilde{\mathbf{y}}$$

Drineas, Mahoney, and Muthukrishnan (2006) proved that the subsampled solution satisfies the **Relative-Error Guarantee**:

$$\|\mathbf{y} - \mathbf{X} \hat{\boldsymbol{\beta}}_{sub}\|_2 \le (1 + \epsilon) \|\mathbf{y} - \mathbf{X} \hat{\boldsymbol{\beta}}_{OLS}\|_2$$

with probability at least $0.99$, reducing the computational workload from hours to fractions of a second while guaranteeing near-optimal prediction accuracy.
"""

marker = "## Fully worked question 1:"
idx = u4.find(marker)
u4_new = u4[:idx] + u4_addition.strip() + "\n\n" + u4[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "w", encoding="utf-8") as f:
    f.write(u4_new)
print("Expanded Unit 4 extra!")
