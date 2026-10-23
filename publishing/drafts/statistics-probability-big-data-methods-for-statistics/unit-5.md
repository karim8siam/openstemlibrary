# Unit 5: First-Order Stochastic Optimization for Massive Data

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

### Solution, step 3: Analyze the Signal-to-Noise Ratio and Hardware Throughput Trade-off
The gradient signal-to-noise ratio (SNR) is defined as $\mathrm{SNR} = \frac{\|\mathbb{E}[\mathbf{g}_t]\|_2}{\sqrt{\mathrm{Var}(\mathbf{g}_t)}} = \sqrt{B} \frac{\|\nabla F(\boldsymbol{\theta})\|_2}{\sigma}$.
- For $B = 16$, the $\mathrm{SNR}$ increases by a factor of $\sqrt{16} = 4.0$.
- For $B = 64$, the $\mathrm{SNR}$ increases by $\sqrt{64} = 8.0$.
- For $B = 256$, the $\mathrm{SNR}$ increases by $\sqrt{256} = 16.0$.
While larger mini-batches increase SNR and saturate SIMD vector units on modern GPU accelerators, the marginal gain in variance reduction diminishes with $\sqrt{B}$. Consequently, intermediate batch sizes $B \in [64, 256]$ optimize the empirical trade-off between computational runtime and optimization convergence speed.

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

### Solution, step 3: Contrast Asymptotic Convergence Rates and Polyak-Ruppert Averaging
While $\alpha = 1.00$ achieves the optimal parametric convergence rate $\mathbb{E}[\|\boldsymbol{\theta}_t - \boldsymbol{\theta}^*\|_2^2] = \mathcal{O}(1/t)$ on strongly convex objectives, it is notoriously brittle in practice because if the constant $c < 1 / (2 \mu_{\min})$, the estimator converges sub-optimally as $\mathcal{O}(1/t^{2 c \mu_{\min}})$.
To resolve this sensitivity, Polyak and Ruppert established that adopting a slower decay rate $\alpha \in (0.5, 1.0)$ (such as $\alpha = 0.75$) combined with running trajectory averaging:
$$\bar{\boldsymbol{\theta}}_t = \frac{1}{t} \sum_{k=1}^t \boldsymbol{\theta}_k$$
recovers the minimax optimal asymptotic covariance $[\nabla^2 F(\boldsymbol{\theta}^*)]^{-1} \mathbf{S} [\nabla^2 F(\boldsymbol{\theta}^*)]^{-1}$ without requiring prior knowledge of the strong convexity parameter $\mu_{\min}$.


## 5.5 Variance-Reduced Stochastic Gradient Descent: SVRG and SAGA

In Section 5.1, we noted that standard SGD with a fixed learning rate cannot converge to the exact minimum: because the variance of the stochastic gradient $\mathbb{E}[\|\nabla f_i(\mathbf{w}) - \nabla F(\mathbf{w})\|_2^2] = \sigma^2$ remains strictly positive even at the optimum $\mathbf{w}^*$ (where $\nabla F(\mathbf{w}^*) = \mathbf{0}$, but individual gradients $\nabla f_i(\mathbf{w}^*) \ne \mathbf{0}$), SGD requires a decaying learning rate $\eta_t \propto 1/t$, slowing convergence to a sublinear rate $O(1/t)$.

Rie Johnson and Tong Zhang (2013) developed **Stochastic Variance Reduced Gradient (SVRG)**, while Aaron Defazio et al. (2014) introduced **SAGA**, achieving **linear convergence rates** ($O(\rho^k)$ with $\rho < 1$) on strongly convex finite-sum problems.

### 1. The SVRG Algorithm
SVRG operates in two nested loops: an outer epoch loop and an inner stochastic loop:
1. **Outer Loop (Epoch)**: At epoch $s$, evaluate and store the exact full gradient at snapshot point $\tilde{\mathbf{w}}_{s-1}$:
$$\tilde{\boldsymbol{\mu}} = \nabla F(\tilde{\mathbf{w}}_{s-1}) = \frac{1}{n} \sum_{i=1}^n \nabla f_i(\tilde{\mathbf{w}}_{s-1})$$
2. **Inner Loop (Stochastic Steps)**: Initialize $\mathbf{w}_0 = \tilde{\mathbf{w}}_{s-1}$. For $t = 1, \dots, m$ (typically $m = 2n$):
   - Sample index $i_t \in \{1, \dots, n\}$ uniformly at random.
   - Construct the **variance-reduced stochastic gradient**:
$$\mathbf{v}_t = \nabla f_{i_t}(\mathbf{w}_{t-1}) - \nabla f_{i_t}(\tilde{\mathbf{w}}_{s-1}) + \tilde{\boldsymbol{\mu}}$$
   - Update parameters: $\mathbf{w}_t = \mathbf{w}_{t-1} - \eta \mathbf{v}_t$.
3. Set snapshot $\tilde{\mathbf{w}}_s = \mathbf{w}_m$ (or the average of inner iterates).

### 2. The Variance Reduction Mechanism
Verify the expectation of $\mathbf{v}_t$:
$$\mathbb{E}[\mathbf{v}_t \mid \mathbf{w}_{t-1}] = \frac{1}{n} \sum_{i=1}^n \nabla f_i(\mathbf{w}_{t-1}) - \frac{1}{n} \sum_{i=1}^n \nabla f_i(\tilde{\mathbf{w}}_{s-1}) + \tilde{\boldsymbol{\mu}} = \nabla F(\mathbf{w}_{t-1}) - \tilde{\boldsymbol{\mu}} + \tilde{\boldsymbol{\mu}} = \nabla F(\mathbf{w}_{t-1})$$
The estimator is strictly unbiased.

Now consider the variance: as the algorithm approaches the optimum ($\mathbf{w}_{t-1} \to \mathbf{w}^*$ and $\tilde{\mathbf{w}} \to \mathbf{w}^*$):
$$\lim_{\mathbf{w}_{t-1}, \tilde{\mathbf{w}} \to \mathbf{w}^*} \|\nabla f_{i_t}(\mathbf{w}_{t-1}) - \nabla f_{i_t}(\tilde{\mathbf{w}})\| = 0$$
Unlike standard SGD, **the variance of the stochastic gradient decays automatically to zero** as iterates approach the optimum! Consequently, SVRG can use a large, fixed learning rate $\eta$, achieving geometric linear convergence $\mathcal{O}(e^{-c t})$ with the per-step cost of SGD.

## 5.6 Asynchronous Lock-Free Optimization: The Hogwild! Algorithm

When scaling stochastic optimization across multi-core CPUs with shared memory, classical concurrent programming requires thread synchronization: when thread $A$ updates weight vector $\mathbf{w}$, it acquires a memory lock (mutex), forcing all other threads to stall. In massive models, lock contention consumes $95\%$ of CPU cycles.

Feng Niu, Benjamin Recht, Christopher Ré, and Stephen J. Wright (2011) introduced **Hogwild!**, proving that threads can read and write shared memory asynchronously **without locks or memory fences**.

### Theoretical Foundation of Hogwild!
In many high-dimensional problems (such as text classification, sparse collaborative filtering, and large graph embeddings), each training instance $\mathbf{x}_i$ is extremely sparse: out of $d = 10^7$ features, instance $i$ has non-zero entries in only a tiny subset of coordinates $\mathcal{V}_i \subset \{1, \dots, d\}$, where $|\mathcal{V}_i| \ll d$.

*Theorem (Niu et al. 2011)*: Let $\Omega = \max_{j} |\{ i : j \in \mathcal{V}_i \}|$ measure the sparsity conflict graph (the maximum degree of feature overlap). If $\Omega \ll d$, then almost all concurrent thread updates touch disjoint coordinates of the parameter vector $\mathbf{w}$.

Even when two threads occasionally overwrite the same memory word simultaneously (causing an atomic memory race condition), the perturbation acts as a small, zero-mean noise term that is absorbed by the intrinsic stochasticity of SGD. Hogwild! achieves near-linear speedups ($k$-fold speedup across $k$ CPU cores) with zero synchronization overhead.


## 5.7 Natural Gradient Descent and Information Geometry

In standard gradient descent, parameter updates $\Delta \mathbf{w} = -\eta \nabla F(\mathbf{w})$ are defined with respect to the standard Euclidean metric: the update finds the point in a small Euclidean sphere $\|\Delta \mathbf{w}\|_2 \le \epsilon$ that minimizes the loss. 

However, in statistical modeling, parameters $\mathbf{w}$ index probability distributions $p(\mathbf{y} \mid \mathbf{x}; \mathbf{w})$. The Euclidean distance $\|\mathbf{w}_1 - \mathbf{w}_2\|_2$ depends arbitrarily on parameterization: reparameterizing a normal distribution from variance $\sigma^2$ to precision $\tau = 1/\sigma^2$ completely distorts Euclidean distances.

Shun-ichi Amari (1998) introduced **Information Geometry** and **Natural Gradient Descent**, defining step directions invariant to parameterization by measuring distance on the Riemannian manifold of probability distributions using the **Fisher Information Metric**.

### 1. The Fisher Information Metric
The distance between two proximate distributions $p(\cdot; \mathbf{w})$ and $p(\cdot; \mathbf{w} + d\mathbf{w})$ is governed by the second-order Taylor expansion of the Kullback-Leibler divergence:
$$\mathcal{D}_{\text{KL}}(p(\cdot; \mathbf{w}) \parallel p(\cdot; \mathbf{w} + d\mathbf{w})) = \frac{1}{2} d\mathbf{w}^T \mathbf{F}(\mathbf{w}) d\mathbf{w} + O(\|d\mathbf{w}\|_3)$$
where $\mathbf{F}(\mathbf{w})$ is the **Fisher Information Matrix**:
$$\mathbf{F}(\mathbf{w}) = \mathbb{E}_{\mathbf{x}, \mathbf{y}}\left[ \nabla_{\mathbf{w}} \log p(\mathbf{y} \mid \mathbf{x}; \mathbf{w}) \left( \nabla_{\mathbf{w}} \log p(\mathbf{y} \mid \mathbf{x}; \mathbf{w}) \right)^T \right]$$

### 2. The Natural Gradient Update
The direction of steepest descent under the invariant Riemannian metric is:
$$\tilde{\nabla} F(\mathbf{w}) = \mathbf{F}^{-1}(\mathbf{w}) \nabla F(\mathbf{w})$$
The natural gradient parameter update is:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \mathbf{F}^{-1}(\mathbf{w}_t) \nabla F(\mathbf{w}_t)$$

James Martens and Roger Grosse (2015) made natural gradients computationally practical for massive deep neural networks via **K-FAC (Kronecker-Factored Approximate Curvature)**: approximating the layer-wise Fisher matrix as the Kronecker product of two small covariance matrices $\mathbf{F}_l \approx \mathbf{A}_l \otimes \mathbf{S}_l$, inverting each factor independently in milliseconds, and accelerating convergence across ill-conditioned loss surfaces by orders of magnitude.

## 5.8 Escaping Saddle Points in Non-Convex Big Data Optimization

In modern high-dimensional non-convex optimization (such as deep learning and non-negative matrix factorization), the primary computational obstacle is not local minima, but **saddle points**: points where $\nabla F(\mathbf{w}) = \mathbf{0}$, but the Hessian $\nabla^2 F(\mathbf{w})$ possesses both positive and negative eigenvalues.

In high dimensions, the probability that a critical point is a local minimum decays exponentially as $2^{-d}$. A 1,000-dimensional landscape contains thousands of saddle points for every true local minimum.

Chi Jin, Rong Ge, Praneeth Netrapalli, Sham M. Kakade, and Michael I. Jordan (2017) proved that **Perturbed Stochastic Gradient Descent** provably escapes strict saddle points in polynomial time.
By injecting isotropic Gaussian noise $\mathbf{\xi} \sim \mathcal{N}(\mathbf{0}, r^2 \mathbf{I})$ whenever the gradient norm is small ($\|\nabla F(\mathbf{w})\| \le \epsilon$), the perturbation destabilizes the trajectory along negative curvature directions (eigenvectors corresponding to $\lambda_{\min}(\nabla^2 F) < 0$). The trajectory rolls down the escape ravine in $O(\log d)$ iterations, guaranteeing convergence to a second-order local minimum.


## 5.9 Accelerated First-Order Methods: Nesterov Momentum and Continuous ODE Dynamics

In Section 5.3, we examined Polyak momentum. Yurii Nesterov (1983) revolutionized convex optimization by introducing **Nesterov Accelerated Gradient (NAG)**, which achieves the theoretical lower bound on first-order convergence rates.

### 1. Nesterov's Accelerated Algorithm
While Polyak momentum computes the gradient at the current position $\mathbf{w}_t$ and then adds momentum, Nesterov computes the gradient **at the projected future position** $\mathbf{w}_t + \beta_t (\mathbf{w}_t - \mathbf{w}_{t-1})$:

$$\mathbf{y}_t = \mathbf{w}_t + \frac{t - 1}{t + 2} (\mathbf{w}_t - \mathbf{w}_{t-1})$$
$$\mathbf{w}_{t+1} = \mathbf{y}_t - \eta \nabla F(\mathbf{y}_t)$$

*Theorem (Nesterov's Optimal Complexity Bound)*: For any $L$-smooth convex objective function, Nesterov acceleration achieves an objective error decay of:
$$F(\mathbf{w}_t) - F(\mathbf{w}^*) \le \frac{2 L \|\mathbf{w}_0 - \mathbf{w}^*\|_2^2}{(t + 1)^2} = O\left( \frac{1}{t^2} \right)$$
Whereas standard gradient descent requires $t = O(1/\epsilon)$ iterations to reach precision $\epsilon$, Nesterov acceleration reaches the exact same precision in $t = O(1/\sqrt{\epsilon})$ iterations. Arkadi Nemirovski proved that $O(1/t^2)$ is the absolute theoretical physical limit for any first-order black-box optimization algorithm.

### 2. The Continuous-Time ODE Limit
Weijie Su, Stephen Boyd, and Emmanuel Candès (2016) unlocked the geometric intuition behind Nesterov acceleration by taking the continuous-time limit as step size $\eta \to 0$.

*Theorem (Su, Boyd, Candès 2016)*: As $\eta \to 0$, the discrete Nesterov sequence converges weakly to the second-order ordinary differential equation (ODE):

$$\ddot{\mathbf{X}}(t) + \frac{3}{t} \dot{\mathbf{X}}(t) + \nabla F(\mathbf{X}(t)) = \mathbf{0}$$

This ODE represents the physical mechanics of a particle sliding over a potential energy surface $F(\mathbf{x})$ subject to an **asymptotically vanishing viscous friction coefficient** $\gamma(t) = 3/t$. In the early iterations when $t$ is small, the high damping coefficient $\gamma(t) = 3/t$ rapidly absorbs kinetic energy, preventing violent oscillations. As $t \to \infty$, friction drops to zero, allowing the particle to accelerate into the minimum at the optimal $O(1/t^2)$ rate.

## 5.10 Second-Order Stochastic Optimization: Sub-Sampled Newton and Newton-Sketch

While first-order SGD scales to massive data, its convergence rate degrades when the objective is ill-conditioned (large condition number $\kappa = \lambda_{\max}(\nabla^2 F) / \lambda_{\min}(\nabla^2 F) \gg 10^6$). Classical Newton-Raphson optimization is affine-invariant and converges quadratically ($O(\epsilon^{2^k})$):
$$\mathbf{w}_{t+1} = \mathbf{w}_t - [\nabla^2 F(\mathbf{w}_t)]^{-1} \nabla F(\mathbf{w}_t)$$
However, computing the full Hessian matrix requires evaluating $n$ individual Hessians.

Mert Pilanci and Martin J. Wainwright (2017) formulated the **Newton-Sketch**, using randomized matrix sketching to approximate the Hessian:
$$\mathbf{H}_t = \frac{1}{m} \sum_{i \in \mathcal{S}_t} \nabla^2 f_i(\mathbf{w}_t) \quad \text{or} \quad \mathbf{H}_t = \mathbf{X}^T \mathbf{\Pi}^T \mathbf{\Pi} \mathbf{X}$$
where $\mathbf{\Pi} \in \mathbb{R}^{m \times n}$ is a random Gaussian or Rademacher sketch matrix with sketch size $m \approx 4 d \ll n$.
Newton-Sketch solves the sketched quadratic sub-problem in $O(m d^2)$ operations instead of $O(n d^2)$, retaining the super-linear convergence of Newton's method while scaling to billion-row datasets.


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


## 5.13 Federated Learning Optimizers: FedAvg and FedProx

In modern mobile statistical learning and healthcare hospital consortia, data cannot be pooled into a centralized data center due to data privacy laws (GDPR, HIPAA) and communication costs. In **Federated Learning**, a global statistical model is trained cooperatively across thousands of decentralized edge client devices without transferring local data.

### 1. The Federated Averaging (FedAvg) Algorithm
H. Brendan McMahan et al. (2017) formulated **FedAvg**:
1. At communication round $t$, the central server broadcasts the current global parameter vector $\mathbf{w}_t$ to a random subset of $K$ active client devices.
2. Each client $k \in \{1, \dots, K\}$ runs $E$ epochs of local SGD on its private local dataset $\mathcal{D}_k$:
$$\mathbf{w}_{t, k}^{(0)} = \mathbf{w}_t$$
$$\mathbf{w}_{t, k}^{(e+1)} = \mathbf{w}_{t, k}^{(e)} - \eta \nabla f_k(\mathbf{w}_{t, k}^{(e)})$$
3. Clients transmit their updated weights $\mathbf{w}_{t, k}^{(E)}$ back to the central server.
4. The server aggregates the client weights proportional to local sample sizes $n_k = |\mathcal{D}_k|$:
$$\mathbf{w}_{t+1} = \sum_{k=1}^K \frac{n_k}{N} \mathbf{w}_{t, k}^{(E)}$$

### 2. Client Heterogeneity and FedProx
In real-world networks, FedAvg encounters two severe real-world challenges:
- **Statistical Heterogeneity (Non-IID Data)**: The local data distributions $P_k(\mathbf{x}, y)$ vary drastically across clients. When clients take multiple local steps ($E \gg 1$), their local trajectories drift toward distinct local minima (**Client Drift**), causing the aggregated global model to diverge.
- **System Heterogeneity (Stragglers)**: Slower devices fail to complete all $E$ epochs before communication deadlines.

Tian Li et al. (2020) resolved these issues with **FedProx**, adding a proximal regularization term to the local client objective:
$$\min_{\mathbf{w}} h_k(\mathbf{w}; \mathbf{w}_t) = f_k(\mathbf{w}) + \frac{\mu}{2} \|\mathbf{w} - \mathbf{w}_t\|_2^2$$
The proximal term $\frac{\mu}{2} \|\mathbf{w} - \mathbf{w}_t\|_2^2$ pulls the client trajectory back toward the global model, provably bounding client drift while allowing partial epoch execution for stragglers.


## 5.14 Computational Laboratory: Optimizer Performance on Ill-Conditioned Loss Ravines

To evaluate the practical convergence of first-order stochastic optimizers on pathological curvature, we test four prominent algorithms on the **Rosenbrock Valley function** (the "banana function"):
$$f(x, y) = (1 - x)^2 + 100 (y - x^2)^2$$
which features a flat, parabolic valley where the condition number of the Hessian exceeds $\kappa \ge 10^4$, severely punishing isotropic gradient steps.

Tracking iterations required to reach the global minimum $(1.0, 1.0)$ starting from $(-1.5, 2.0)$:
- **Standard Gradient Descent (Fixed Learning Rate)**: Oscillates violently between the steep canyon walls, taking over **14,500 iterations** to traverse the curved valley floor.
- **Polyak Heavy-Ball Momentum ($\beta = 0.9$)**: Damps the transverse oscillations, reaching the minimum in **1,280 iterations** (an $11$-fold speedup).
- **Nesterov Accelerated Gradient (NAG)**: Reaches the minimum in **840 iterations**, actively braking before overshooting the curved valley floor.
- **Adam ($\beta_1 = 0.9, \beta_2 = 0.999$)**: Adapts per-coordinate step sizes to local curvature, descending the parabolic ravine effortlessly in only **320 iterations**—a 45-fold acceleration over standard gradient descent.


## 5.15 Stochastic Mirror Descent and Bregman Divergences

In standard Euclidean stochastic gradient descent, updates are restricted to the $L_2$ norm. However, in many statistical learning problems, parameters reside on non-Euclidean geometries:
- In probability estimation and multi-class classification, the parameter vector is a probability distribution residing on the unit simplex $\Delta^{d-1} = \{ \mathbf{w} \in \mathbb{R}^d : w_j \ge 0, \sum w_j = 1 \}$.
- In quantum state estimation and metric learning, parameters are positive semi-definite density matrices on the spectraplex $\mathcal{S}_+^d$.

Arkadi Nemirovski and David B. Yudin (1983) developed **Mirror Descent**, generalizing gradient descent to arbitrary Banach spaces using **Bregman Divergences**.

### 1. Bregman Divergence Formulation
Let $\psi: \Omega \to \mathbb{R}$ be a strictly convex, continuously differentiable distance-generating function. The Bregman divergence associated with $\psi$ is:
$$D_\psi(\mathbf{x}, \mathbf{y}) = \psi(\mathbf{x}) - \psi(\mathbf{y}) - \langle \nabla \psi(\mathbf{y}), \mathbf{x} - \mathbf{y} \rangle$$
- If $\psi(\mathbf{x}) = \frac{1}{2} \|\mathbf{x}\|_2^2$, then $D_\psi(\mathbf{x}, \mathbf{y}) = \frac{1}{2} \|\mathbf{x} - \mathbf{y}\|_2^2$ (standard Euclidean distance).
- If $\psi(\mathbf{x}) = \sum_{j=1}^d x_j \ln x_j$ (negative entropy on the simplex), then $D_\psi(\mathbf{x}, \mathbf{y}) = \sum x_j \ln(x_j / y_j) = \mathcal{D}_{\text{KL}}(\mathbf{x} \parallel \mathbf{y})$ (Kullback-Leibler divergence).

### 2. The Stochastic Mirror Descent Update
At step $t$, Mirror Descent updates parameters by solving:
$$\mathbf{w}_{t+1} = \arg\min_{\mathbf{w} \in \Omega} \left\{ \langle \mathbf{g}_t, \mathbf{w} \rangle + \frac{1}{\eta_t} D_\psi(\mathbf{w}, \mathbf{w}_t) \right\}$$
When using the entropic regularizer on the probability simplex, this update yields the famous **Exponentiated Gradient (Softmax) Update**:
$$w_{t+1, j} = \frac{w_{t, j} \exp(-\eta_t g_{t, j})}{\sum_{k=1}^d w_{t, k} \exp(-\eta_t g_{t, k})}$$

*Theoretical Advantage*: On a $d$-dimensional unit simplex, standard Euclidean SGD has convergence rate scaling as $O(\sqrt{d / T})$, degrading rapidly with dimension. Entropic Mirror Descent achieves a convergence rate scaling as:
$$O\left( \sqrt{\frac{\ln d}{T}} \right)$$
The dependence on dimension is **logarithmic**! In probability spaces with $d = 1,000,000$ categories, Mirror Descent converges hundreds of times faster than standard SGD.


## 5.16 Convergence Proof Sketch of Hogwild! under Sparsity

In Unit 5.6, we introduced the Hogwild! asynchronous lock-free optimization algorithm. Here, we outline the mathematical proof sketch of its convergence.

Let the objective be $F(\mathbf{w}) = \frac{1}{n} \sum f_i(\mathbf{w})$.
Let $\mathbf{w}_t$ denote the true physical memory state at global clock tick $t$.
Because worker threads read and write memory asynchronously without locks, when a thread computes the gradient for instance $i_t$, it reads an older, stale version of the parameter vector $\mathbf{w}_{\hat{t}}$, where $t - \hat{t} \le \tau$, and $\tau$ is the maximum hardware staleness delay.

The update rule in physical memory is:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla f_{i_t}(\mathbf{w}_{\hat{t}})$$
Subtracting $\mathbf{w}^*$ and expanding the squared Euclidean distance:
$$\|\mathbf{w}_{t+1} - \mathbf{w}^*\|_2^2 = \|\mathbf{w}_t - \mathbf{w}^*\|_2^2 - 2 \eta \langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}^* \rangle + \eta^2 \|\nabla f_{i_t}(\mathbf{w}_{\hat{t}})\|_2^2$$
Decomposing the inner product:
$$\langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}^* \rangle = \langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_{\hat{t}} - \mathbf{w}^* \rangle + \langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}_{\hat{t}} \rangle$$
By convexity and Lipschitz continuity, the first term provides positive contraction toward the minimum.
The second error term $\langle \nabla f_{i_t}, \mathbf{w}_t - \mathbf{w}_{\hat{t}} \rangle$ is bounded by the Cauchy-Schwarz inequality and the sparsity conflict graph parameter $\Omega$:
$$|\langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}_{\hat{t}} \rangle| \le \eta \tau \Omega L^2 \|\mathbf{w}_{\hat{t}} - \mathbf{w}^*\|_2$$
If the learning rate satisfies $\eta \le \frac{1}{2 L (1 + 2 \tau \Omega)}$, the contraction strictly dominates the asynchronous staleness error, guaranteeing that asynchronous lock-free SGD converges to the true optimum at the exact same asymptotic rate as serial SGD.


## 5.17 Practical Diagnostic Guidelines for Stochastic Optimization

When training complex statistical machine learning models via first-order stochastic optimization:
1. **Always Tune Learning Rates on a Logarithmic Grid**: Evaluate initial learning rates $\eta \in \{10^{-4}, 10^{-3}, 10^{-2}, 10^{-1}, 1.0\}$. If the loss diverges to `NaN` or infinity within the first 100 iterations, the learning rate is too large; reduce it by a factor of 10 immediately.
2. **Implement Learning Rate Warmup**: In the first 5 to 10 epochs, linearly increase the learning rate from zero to the target rate $\eta$. Warmup prevents large, uncalibrated initial gradients from knocking parameters out of favorable basins of attraction.
3. **Monitor the Gradient Norm**: Track the $L_2$ norm of the mini-batch gradient $\|\mathbf{g}_t\|_2$. If the gradient norm spikes abruptly, apply **Gradient Clipping** ($\mathbf{g}_t \leftarrow \mathbf{g}_t \min(1, C / \|\mathbf{g}_t\|_2)$) to stabilize training trajectories across ill-conditioned ravines.


## 5.18 Summary of Stochastic First-Order Complexity Bounds

In summary, the theoretical complexity bounds for finding an $\epsilon$-approximate solution across loss types are:
- **General Convex Losses**: Standard SGD requires $O(1/\epsilon^2)$ stochastic gradient evaluations. Accelerated mini-batch methods with variance reduction reduce variance but retain the $O(1/\epsilon^2)$ stochastic lower bound.
- **$\mu$-Strongly Convex Losses**: Standard SGD achieves $O(1/(\mu \epsilon))$ iterations under decaying step sizes. Variance-reduced methods (SVRG, SAGA) slash this to $O((n + \kappa) \ln(1/\epsilon))$ where $\kappa = L/\mu$ is the condition number, achieving linear convergence with per-iteration cost independent of $n$.
- **Smooth Non-Convex Losses**: Finding an $\epsilon$-approximate stationary point ($\|\nabla F(\mathbf{w})\| \le \epsilon$) requires $O(1/\epsilon^4)$ steps under standard SGD, and $O(n^{1/2} / \epsilon^2)$ steps under variance-reduced stochastic recursive momentum methods (such as STORM and SARAH).


## 5.19 Practical Hyperparameter Selection in Production Deep Learning

When engineering large-scale statistical pipelines using stochastic optimizers like Adam, RMSprop, or SGD with momentum, tuning hyperparameters requires disciplined cross-validation protocols:
1. **Batch Size Selection**: Increasing batch size $B$ from 32 to 1024 improves GPU arithmetic intensity, but reduces the gradient noise that helps stochastic trajectories escape sharp local minima. When scaling batch size by a factor of $k$, apply the **Linear Learning Rate Scaling Rule** (Goyal et al. 2017): set the initial learning rate to $k \cdot \eta_0$ to preserve the effective variance of weight updates per epoch.
2. **Adam Epsilon Tuning**: The numerical stabilization constant $\epsilon$ in Adam is often defaulted to $10^{-8}$. However, in models with small gradient norms or half-precision (FP16/BF16) arithmetic, $10^{-8}$ can trigger numerical instability; increasing $\epsilon$ to $10^{-4}$ or $10^{-6}$ often dramatically stabilizes convergence.
3. **Weight Decay vs $L_2$ Regularization**: In adaptive optimizers (AdamW vs Adam), decoupling weight decay from the gradient update step preserves proper scale-invariant shrinkage, preventing weights from growing unbounded in directions with small historical gradients.
