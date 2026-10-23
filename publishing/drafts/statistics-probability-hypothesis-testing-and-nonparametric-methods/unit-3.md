# Unit 3: Uniformly Most Powerful Unbiased (UMPU) Tests, Similar Regions & Invariance Principles

Unbiased hypothesis tests, alpha-similar boundary conditions, and Neyman structure with respect to complete sufficient statistics; two-sided UMPU tests in one-parameter exponential families with dual critical values and equal-tail approximations; multiparameter exponential families with nuisance parameters and conditional UMPU tests (Student's t, Fisher's exact test, Poisson rate ratio); group invariance in hypothesis testing, maximal invariants, and Uniformly Most Powerful Invariant (UMPI) tests; Pitman asymptotic relative efficiency (ARE) and Bahadur efficiency.

## 3.1 Unbiased Hypothesis Tests, Boundary Continuity, and Alpha-Similar Regions

As established in Unit 2, Uniformly Most Powerful (UMP) tests frequently fail to exist when the alternative hypothesis is two-sided ($H_0 : \theta = \theta_0$ versus $H_1 : \theta \neq \theta_0$) or when the statistical model contains unspecified **nuisance parameters** ($\theta = (\vartheta, \boldsymbol{\eta})$ where $\vartheta$ is the parameter of interest and $\boldsymbol{\eta}$ is a vector of nuisance parameters). The reason a UMP test fails to exist over the full class of level-$\alpha$ tests is that the unrestricted class contains "cheating" one-sided tests (such as the pure right-tailed test $\phi_+$) that achieve high power on one side of the alternative space only by sacrificing power below $\alpha$ on the opposite side of the alternative space.

In exact analogy with point estimation—where the non-existence of a globally minimum mean squared error estimator motivates restricting attention to unbiased estimators to obtain a Uniformly Minimum Variance Unbiased Estimator (UMVUE)—Jerzy Neyman and Egon Pearson resolved the non-existence of UMP tests by restricting the competition to the class of **unbiased level-$\alpha$ tests**.

### Definition of Unbiasedness and Uniformly Most Powerful Unbiased (UMPU) Tests

A test function $\phi : \mathcal{X} \to [0, 1]$ for testing $H_0 : \theta \in \Theta_0$ against $H_1 : \theta \in \Theta_1$ is defined to be **unbiased of level $\alpha$** if its power function $\beta_\phi(\theta) = \mathbb{E}_\theta[\phi(\mathbf{X})]$ simultaneously satisfies two conditions across the parameter space:

$$\beta_\phi(\theta) \le \alpha \quad \forall \theta \in \Theta_0, \qquad \text{and} \qquad \beta_\phi(\theta) \ge \alpha \quad \forall \theta \in \Theta_1$$

That is, an unbiased test never rejects a true null hypothesis with probability exceeding $\alpha$, and never rejects a true alternative hypothesis with probability smaller than $\alpha$. Within the restricted class $\mathcal{U}_\alpha$ of all unbiased level-$\alpha$ tests, a test $\phi^* \in \mathcal{U}_\alpha$ is called a **Uniformly Most Powerful Unbiased (UMPU) level-$\alpha$ test** if it maximizes power uniformly across $\Theta_1$ among all unbiased level-$\alpha$ competitors:

$$\mathbb{E}_\theta[\phi^*(\mathbf{X})] \ge \mathbb{E}_\theta[\phi(\mathbf{X})] \quad \forall \theta \in \Theta_1, \quad \forall \phi \in \mathcal{U}_\alpha$$

### Continuity of Power Functions and Alpha-Similarity on the Common Boundary

Suppose the parameter space $\Theta \subseteq \mathbb{R}^k$ is endowed with the usual Euclidean topology, and let $\omega = \overline{\Theta}_0 \cap \overline{\Theta}_1$ denote the **common topological boundary** separating the null parameter space $\Theta_0$ and the alternative parameter space $\Theta_1$. In regular parametric families (and throughout exponential families), the power function $\theta \mapsto \beta_\phi(\theta) = \int_{\mathcal{X}} \phi(\mathbf{x}) f(\mathbf{x}; \theta) \, d\mu(\mathbf{x})$ of any test function $\phi$ is a continuous function on $\Theta$.

Consider any boundary parameter point $\theta_b \in \omega = \overline{\Theta}_0 \cap \overline{\Theta}_1$:
1. Because $\theta_b$ is a limit point of a sequence $\{\theta_n^{(0)}\} \subset \Theta_0$ where $\beta_\phi(\theta_n^{(0)}) \le \alpha$, continuity of $\beta_\phi$ forces $\beta_\phi(\theta_b) = \lim_{n \to \infty} \beta_\phi(\theta_n^{(0)}) \le \alpha$.
2. Simultaneously, because $\theta_b$ is a limit point of a sequence $\{\theta_n^{(1)}\} \subset \Theta_1$ where unbiasedness requires $\beta_\phi(\theta_n^{(1)}) \ge \alpha$, continuity of $\beta_\phi$ forces $\beta_\phi(\theta_b) = \lim_{n \to \infty} \beta_\phi(\theta_n^{(1)}) \ge \alpha$.

Combining these two inequalities proves a fundamental structural theorem: **every unbiased level-$\alpha$ test with a continuous power function must have constant rejection probability identically equal to $\alpha$ across the entire topological boundary $\omega = \overline{\Theta}_0 \cap \overline{\Theta}_1$**:

$$\beta_\phi(\theta) = \mathbb{E}_\theta[\phi(\mathbf{X})] = \alpha \quad \forall \theta \in \omega = \overline{\Theta}_0 \cap \overline{\Theta}_1$$

A test $\phi$ that satisfies $\mathbb{E}_\theta[\phi(\mathbf{X})] = \alpha$ for all $\theta \in \omega$ is said to be **$\alpha$-similar on the boundary $\omega$** (or simply a **similar test** when $\Theta_0 = \omega$). Furthermore, when $\Theta \subseteq \mathbb{R}$ is one-dimensional and $\Theta_0 = \{\theta_0\}$ is a point null hypothesis tested against the two-sided alternative $\Theta_1 = \{\theta : \theta \neq \theta_0\}$, the power function $\beta_\phi(\theta)$ of an unbiased test achieves a **local minimum** at $\theta = \theta_0$ ($\beta_\phi(\theta_0) = \alpha$ and $\beta_\phi(\theta) \ge \alpha$ for all $\theta \neq \theta_0$). Therefore, if $\beta_\phi(\theta)$ is differentiable at $\theta_0$, Fermat's theorem on stationary points requires its first derivative (slope) at $\theta_0$ to vanish identically:

$$\beta_\phi(\theta_0) = \alpha \qquad \text{and} \qquad \beta_\phi'(\theta_0) = \left.\frac{d}{d\theta} \mathbb{E}_\theta[\phi(\mathbf{X})]\right|_{\theta = \theta_0} = 0$$

This zero-slope tangential condition at $\theta_0$ is the analytical constraint that eliminates one-sided tests and pins down the unique two-sided UMPU test.

## 3.2 Two-Sided UMPU Tests in One-Parameter Exponential Families and Dual Critical Cutoffs

Let us apply the boundary level and zero-derivative unbiasedness conditions to derive the exact Uniformly Most Powerful Unbiased (UMPU) test for a two-sided hypothesis in a one-parameter exponential family. Suppose $\mathbf{X}$ has probability density or mass function:

$$f(\mathbf{x}; \theta) = \exp\left(\theta T(\mathbf{x}) - B(\theta)\right) h(\mathbf{x}), \quad \theta \in \Theta \subseteq \mathbb{R}$$

written in natural parameter form (since any strictly monotone transformation $\eta(\theta)$ maps $\theta = \theta_0$ bijectively to $\eta = \eta_0$), and consider testing the point null hypothesis against the two-sided alternative:

$$H_0 : \theta = \theta_0 \quad \text{versus} \quad H_1 : \theta \neq \theta_0$$

By analytical properties of exponential families, the power function $\beta_\phi(\theta) = \int \phi(\mathbf{x}) \exp(\theta T(\mathbf{x}) - B(\theta)) h(\mathbf{x}) \, d\mu(\mathbf{x})$ is infinitely differentiable inside the natural parameter space, and differentiation can be interchanged with integration:

$$\beta_\phi'(\theta) = \frac{d}{d\theta} \mathbb{E}_\theta[\phi(\mathbf{X})] = \mathbb{E}_\theta\left[\phi(\mathbf{X}) \left(T(\mathbf{X}) - B'(\theta)\right)\right] = \mathbb{E}_\theta\left[T(\mathbf{X}) \phi(\mathbf{X})\right] - \mathbb{E}_\theta[T(\mathbf{X})] \mathbb{E}_\theta[\phi(\mathbf{X})]$$

Evaluating $\beta_\phi(\theta_0) = \alpha$ and $\beta_\phi'(\theta_0) = 0$ at $\theta = \theta_0$, the second term equals $\alpha \mathbb{E}_{\theta_0}[T(\mathbf{X})]$. Therefore, every unbiased level-$\alpha$ test $\phi$ must satisfy two simultaneous moment constraints under the null distribution $P_{\theta_0}$:

$$\mathbb{E}_{\theta_0}[\phi(\mathbf{X})] = \alpha \qquad \text{and} \qquad \mathbb{E}_{\theta_0}[T(\mathbf{X}) \phi(\mathbf{X})] = \alpha \, \mathbb{E}_{\theta_0}[T(\mathbf{X})]$$

Notice the statistical meaning of the second equation: dividing by $\alpha$ gives $\frac{\mathbb{E}_{\theta_0}[T \phi]}{\mathbb{E}_{\theta_0}[\phi]} = \mathbb{E}_{\theta_0}[T]$, which states that **the conditional expectation of the sufficient statistic $T(\mathbf{X})$ inside the rejection region under $H_0$ must equal the unconditional null mean $\mathbb{E}_{\theta_0}[T(\mathbf{X})]$**! Equivalently, under $H_0$, the test function $\phi(\mathbf{X})$ and the sufficient statistic $T(\mathbf{X})$ must have **zero covariance**: $\text{Cov}_{\theta_0}(T(\mathbf{X}), \phi(\mathbf{X})) = 0$.

### Theorem 3.1: Two-Sided UMPU Test in One-Parameter Exponential Families

In the natural exponential family $f(\mathbf{x}; \theta) = \exp(\theta T(\mathbf{x}) - B(\theta)) h(\mathbf{x})$, for any $\alpha \in (0, 1)$, there exist unique critical constants $c_1 < c_2$ and boundary randomization constants $\gamma_1, \gamma_2 \in [0, 1]$ such that the **two-tailed test function**:

$$\phi^*(\mathbf{x}) = \begin{cases} 1, & \text{if } T(\mathbf{x}) < c_1 \text{ or } T(\mathbf{x}) > c_2 \\ \gamma_1, & \text{if } T(\mathbf{x}) = c_1 \\ \gamma_2, & \text{if } T(\mathbf{x}) = c_2 \\ 0, & \text{if } c_1 < T(\mathbf{x}) < c_2 \end{cases}$$

satisfies the two simultaneous linear integral equations:

$$\mathbb{E}_{\theta_0}[\phi^*(T)] = \alpha \qquad \text{and} \qquad \mathbb{E}_{\theta_0}[T \phi^*(T)] = \alpha \, \mathbb{E}_{\theta_0}[T]$$

This test $\phi^*$ is the unique **Uniformly Most Powerful Unbiased (UMPU) level-$\alpha$ test** for $H_0 : \theta = \theta_0$ versus $H_1 : \theta \neq \theta_0$ (and also for the interval hypothesis $H_0 : \theta_1 \le \theta \le \theta_2$ versus $H_1 : \theta \notin [\theta_1, \theta_2]$ when calibrated by $\beta(\theta_1) = \beta(\theta_2) = \alpha$).

#### Proof via the Generalized Neyman-Pearson Lemma:
Fix any alternative parameter value $\theta_1 \neq \theta_0$. Maximizing $\mathbb{E}_{\theta_1}[\phi(T)]$ subject to the two linear equality constraints $\mathbb{E}_{\theta_0}[\phi(T)] = \alpha$ and $\mathbb{E}_{\theta_0}[T \phi(T)] = \alpha \mathbb{E}_{\theta_0}[T]$ is a linear program solved by the Generalized Neyman-Pearson Lemma with two Lagrange multipliers $(k_1, k_2)$: the optimal test $\phi^*(t)$ must equal $1$ whenever:

$$f_T(t; \theta_1) > (k_1 + k_2 t) f_T(t; \theta_0) \iff e^{(\theta_1 - \theta_0) t - [B(\theta_1) - B(\theta_0)]} > k_1 + k_2 t$$

Because the left-hand side $g(t) = e^{(\theta_1 - \theta_0) t - \Delta B}$ is a **strictly convex exponential function** of $t$ for every $\theta_1 \neq \theta_0$, while the right-hand side $\ell(t) = k_1 + k_2 t$ is a **straight line**, a strictly convex curve can intersect a straight line in at most two points $c_1 < c_2$, lying strictly *above* the line on the exterior region $\{t < c_1\} \cup \{t > c_2\}$ and strictly *below* the line on the interior interval $(c_1, c_2)$! Because $c_1, c_2, \gamma_1, \gamma_2$ are determined solely by the two null moment equations at $\theta_0$ and do not depend on $\theta_1$, the resulting exterior two-tailed test $\phi^*(T)$ maximizes power uniformly for all $\theta_1 \neq \theta_0$.

### Symmetric Versus Asymmetric Distributions: Equal-Tailed vs Unbiased Cutoffs

1. **Symmetric Null Distribution (e.g., Normal Mean $\mathcal{N}(\mu, \sigma_0^2)$)**: When the null distribution of $T(\mathbf{X}) = \bar{X}$ is symmetric about $\mu_0 = \mathbb{E}_{\mu_0}[\bar{X}]$, choosing symmetric critical values $c_1 = \mu_0 - d$ and $c_2 = \mu_0 + d$ with equal tail probabilities $\mathbb{P}_{\mu_0}(\bar{X} < c_1) = \mathbb{P}_{\mu_0}(\bar{X} > c_2) = \alpha / 2$ automatically satisfies the zero-covariance condition $\mathbb{E}_{\mu_0}[(\bar{X} - \mu_0)\phi^*(\bar{X})] = 0$ by odd symmetry! Thus for a normal mean, the standard **equal-tailed $Z$-test** $|\bar{X} - \mu_0| > z_{1-\alpha/2} \sigma_0 / \sqrt{n}$ is exact UMPU.
2. **Skewed Null Distribution (e.g., Normal Variance $\chi^2_{n-1}$)**: For testing $H_0 : \sigma^2 = \sigma_0^2$ versus $H_1 : \sigma^2 \neq \sigma_0^2$, the sufficient statistic $V = (n-1)S^2 / \sigma_0^2 \sim \chi^2_\nu$ ($\nu = n - 1$) is right-skewed. Using the Chi-Square density identity $v f_\nu(v) = \nu f_{\nu+2}(v)$, the second UMPU equation $\mathbb{E}_0[V \phi^*(V)] = \alpha \nu$ simplifies to:
   $$\int_0^{c_1} f_\nu(v) \, dv + \int_{c_2}^\infty f_\nu(v) \, dv = \alpha \quad \text{and} \quad \int_0^{c_1} f_{\nu+2}(v) \, dv + \int_{c_2}^\infty f_{\nu+2}(v) \, dv = \alpha$$
   Equivalently, subtracting the equations yields $c_1^{\nu/2} e^{-c_1/2} = c_2^{\nu/2} e^{-c_2/2}$, meaning that the exact UMPU test requires $c_1$ and $c_2$ to have equal values of $v f_\nu(v)$ rather than equal tail probabilities $\alpha/2$!

## 3.3 Neyman Structure, Completeness, and Multiparameter Exponential Families with Nuisance Parameters

The true power of UMPU theory emerges in **multiparameter statistical models containing nuisance parameters**. Suppose the parameter vector decomposes as $\theta = (\vartheta, \boldsymbol{\eta}) \in \Theta$, where $\vartheta \in \mathbb{R}$ is the scalar target parameter of interest and $\boldsymbol{\eta} = (\eta_1, \dots, \eta_k)^T \in \mathbb{R}^k$ is a vector of unknown nuisance parameters. Whether we test the one-sided composite hypothesis $H_0 : \vartheta \le \vartheta_0$ versus $H_1 : \vartheta > \vartheta_0$ or the two-sided hypothesis $H_0 : \vartheta = \vartheta_0$ versus $H_1 : \vartheta \neq \vartheta_0$, the common boundary separating $\Theta_0$ and $\Theta_1$ is the $k$-dimensional hyperplane:

$$\omega = \left\{(\vartheta, \boldsymbol{\eta}) \in \Theta : \vartheta = \vartheta_0, \; \boldsymbol{\eta} \in \Omega_\omega\right\}$$

By Section 3.1, any unbiased level-$\alpha$ test $\phi(\mathbf{X})$ must be **$\alpha$-similar on the boundary hyperplane $\omega$**:

$$\mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}[\phi(\mathbf{X})] = \alpha \quad \forall \boldsymbol{\eta} \in \Omega_\omega$$

How can a test $\phi(\mathbf{X})$ guarantee that its expectation equals the constant $\alpha$ for *every* possible value of the unknown nuisance parameter vector $\boldsymbol{\eta}$?

### Definition of Neyman Structure and Conditioning on Boundary Sufficient Statistics

Suppose that when the target parameter is fixed on the boundary $\vartheta = \vartheta_0$, the statistic $\mathbf{U} = \mathbf{U}(\mathbf{X})$ is a **sufficient statistic for the nuisance parameter $\boldsymbol{\eta}$** under the boundary family $\mathcal{P}_\omega = \{P_{\vartheta_0, \boldsymbol{\eta}} : \boldsymbol{\eta} \in \Omega_\omega\}$. By sufficiency of $\mathbf{U}$ on $\omega$, the conditional distribution of $\mathbf{X}$ given $\mathbf{U} = \mathbf{u}$ at $\vartheta = \vartheta_0$ is completely free of the nuisance parameter $\boldsymbol{\eta}$! Therefore, if a test function $\phi(\mathbf{X})$ satisfies the **conditional size constraint** almost everywhere in $\mathbf{u}$:

$$\mathbb{E}_{\vartheta_0}\left[\phi(\mathbf{X}) \;\middle|\; \mathbf{U}(\mathbf{X}) = \mathbf{u}\right] = \alpha \quad \text{for } P_\omega^U\text{-almost all } \mathbf{u}$$

then taking the unconditional expectation via the law of iterated expectations immediately guarantees $\alpha$-similarity for all $\boldsymbol{\eta}$:

$$\mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}[\phi(\mathbf{X})] = \mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}\Big[ \mathbb{E}_{\vartheta_0}\left[\phi(\mathbf{X}) \mid \mathbf{U}\right] \Big] = \mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}[\alpha] = \alpha \quad \forall \boldsymbol{\eta} \in \Omega_\omega$$

A test $\phi(\mathbf{X})$ that satisfies $\mathbb{E}_{\vartheta_0}[\phi(\mathbf{X}) \mid \mathbf{U} = \mathbf{u}] = \alpha$ almost everywhere is said to have **Neyman structure** with respect to the boundary sufficient statistic $\mathbf{U}$.

### Theorem 3.2: Lehmann-Scheffé Completeness Theorem for Similar Tests

Let $\mathbf{U}(\mathbf{X})$ be a sufficient statistic for the boundary family $\mathcal{P}_\omega = \{P_{\vartheta_0, \boldsymbol{\eta}} : \boldsymbol{\eta} \in \Omega_\omega\}$. Then **every** $\alpha$-similar test on $\omega$ has Neyman structure with respect to $\mathbf{U}$ if and only if the family of distributions of $\mathbf{U}$ on $\omega$, denoted $\mathcal{P}_\omega^U$, is **boundedly complete**.

#### Formal Proof:
Suppose $\mathcal{P}_\omega^U$ is boundedly complete, and let $\phi(\mathbf{X})$ be any test that is $\alpha$-similar on $\omega$, so $\mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}[\phi(\mathbf{X})] = \alpha$ for all $\boldsymbol{\eta} \in \Omega_\omega$. Define the measurable conditional expectation function $g(\mathbf{u}) = \mathbb{E}_{\vartheta_0}[\phi(\mathbf{X}) \mid \mathbf{U} = \mathbf{u}] - \alpha$. Because $0 \le \phi(\mathbf{x}) \le 1$, the function $g(\mathbf{u})$ is bounded ($|g(\mathbf{u})| \le 1$). By the law of total expectation:

$$\mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}[g(\mathbf{U})] = \mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}\left[\mathbb{E}_{\vartheta_0}[\phi(\mathbf{X}) \mid \mathbf{U}] - \alpha\right] = \mathbb{E}_{\vartheta_0, \boldsymbol{\eta}}[\phi(\mathbf{X})] - \alpha = 0 \quad \forall \boldsymbol{\eta} \in \Omega_\omega$$

By bounded completeness of $\mathbf{U}$ on $\omega$, any bounded function of $\mathbf{U}$ with zero expectation for all $\boldsymbol{\eta} \in \Omega_\omega$ must vanish almost everywhere! Thus $g(\mathbf{u}) = 0$ almost everywhere, meaning $\mathbb{E}_{\vartheta_0}[\phi(\mathbf{X}) \mid \mathbf{U} = \mathbf{u}] = \alpha$ almost everywhere.

### Theorem 3.3: Conditional UMPU Tests in Multiparameter Exponential Families

Suppose $\mathbf{X}$ follows a $(k+1)$-parameter exponential family written in the canonical form:

$$f(\mathbf{x}; \vartheta, \boldsymbol{\eta}) = C(\vartheta, \boldsymbol{\eta}) \exp\left( \vartheta T(\mathbf{x}) + \sum_{j=1}^k \eta_j U_j(\mathbf{x}) \right) h(\mathbf{x})$$

Then:
1. On the boundary $\vartheta = \vartheta_0$, the vector $\mathbf{U} = (U_1, \dots, U_k)^T$ is a complete sufficient statistic for the nuisance parameter vector $\boldsymbol{\eta}$.
2. The conditional distribution of $T$ given $\mathbf{U} = \mathbf{u}$ depends **only on the target parameter $\vartheta$** and is completely free of $\boldsymbol{\eta}$, forming a one-parameter exponential family in $\vartheta$:
   $$f_{T \mid \mathbf{U}}(t \mid \mathbf{u}; \vartheta) = C_{\mathbf{u}}(\vartheta) e^{\vartheta t} h_{\mathbf{u}}(t)$$
3. Therefore, constructing a UMP one-sided test or UMPU two-sided test **within each conditional slice $\mathbf{U} = \mathbf{u}$ at conditional size $\alpha$** using Theorem 2.3 or Theorem 3.1 yields the unconditional **Uniformly Most Powerful Unbiased (UMPU) level-$\alpha$ test** for $\vartheta$ in the presence of unknown nuisance parameters $\boldsymbol{\eta}$!

## 3.4 Canonical Applications of Multiparameter UMPU Theory: Student's t, Fisher's Exact Test, and Basu's Simplification

Theorem 3.3 provides a unified, exact derivation for the most famous tests in classical parametric statistics—eliminating nuisance parameters by conditioning on complete boundary sufficient statistics, and then simplifying to unconditional pivotal statistics whenever **Basu's Theorem** applies.

### 1. Derivation of Student's $t$-Test as the Exact UMPU Test via Basu's Theorem

Let $X_1, \dots, X_n \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma^2)$ where both $\mu \in \mathbb{R}$ and $\sigma^2 > 0$ are unknown, and consider testing $H_0 : \mu = 0$ (by shifting $X_i - \mu_0$) against $H_1 : \mu > 0$ or $H_1 : \mu \neq 0$ with $\sigma^2$ as an unknown nuisance parameter. Writing the joint Gaussian density in multiparameter exponential form:

$$f_n(\mathbf{x}; \mu, \sigma^2) = (2\pi\sigma^2)^{-n/2} \exp\left(-\frac{n\mu^2}{2\sigma^2}\right) \exp\left( \underbrace{\frac{\mu}{\sigma^2}}_{\vartheta} \underbrace{\sum_{i=1}^n x_i}_{T(\mathbf{x})} + \underbrace{\left(-\frac{1}{2\sigma^2}\right)}_{\eta} \underbrace{\sum_{i=1}^n x_i^2}_{U(\mathbf{x})} \right)$$

Notice that $\vartheta = \mu / \sigma^2 = 0 \iff \mu = 0$ (and $\vartheta > 0 \iff \mu > 0$). Under the boundary null hypothesis $H_0 : \vartheta = 0$, the statistic $U(\mathbf{X}) = \sum_{i=1}^n X_i^2$ is a complete sufficient statistic for the nuisance parameter $\eta = -1/(2\sigma^2)$. By Theorem 3.3, the UMPU one-sided test rejects $H_0$ for large values of $T = \sum X_i$ **conditional on $U = u$**: $T > c(u)$.

How do we avoid having a critical cutoff $c(u)$ that depends on $u$? Define the **Student's $t$-statistic**:

$$t(\mathbf{X}) = \frac{\sqrt{n}\bar{X}}{S} = \frac{T / \sqrt{n}}{\sqrt{\frac{1}{n-1}\left(U - T^2/n\right)}} = \frac{\sqrt{n-1} \, (T / \sqrt{U})}{\sqrt{1 - (T/\sqrt{U})^2 / n}}$$

Notice two decisive mathematical properties of $t(\mathbf{X})$:
1. For any fixed value of $U = u > 0$, $t(\mathbf{X})$ is a **strictly increasing function of $T$** on $(-\sqrt{nu}, \sqrt{nu})$. Therefore, the conditional rejection region $\{T > c(u)\}$ is mathematically identical to $\{t(\mathbf{X}) > k(u)\}$!
2. Under the null hypothesis $H_0 : \mu = 0$, the distribution of $t(\mathbf{X})$ is the central Student's $t_{n-1}$ distribution, which is **completely free of the nuisance parameter $\sigma^2$**—that is, $t(\mathbf{X})$ is an **ancillary statistic** on the boundary $\omega = \{\mu = 0, \sigma^2 > 0\}$! Since $U(\mathbf{X}) = \sum X_i^2$ is a complete sufficient statistic for $\sigma^2$ on $\omega$, **Basu's Theorem** proves that $t(\mathbf{X})$ and $U(\mathbf{X})$ are **statistically independent under $H_0$**!

Because $t(\mathbf{X})$ is independent of $U(\mathbf{X})$ under $H_0$, the conditional distribution of $t(\mathbf{X})$ given $U = u$ is identical to its unconditional $t_{n-1}$ distribution! Consequently, the conditional cutoff $k(u) \equiv t_{n-1, 1-\alpha}$ is a constant independent of $u$, proving that the classical **one-sided and two-sided Student's $t$-tests are the exact UMPU tests** for a normal mean with unknown variance!

### 2. Conditioning in Discrete Exponential Families: Poisson Ratio and Fisher's Exact Test

In discrete models, Basu's Theorem does not apply because no scale-free ancillary pivot exists, so the UMPU test remains explicitly **conditional on $U = u$**:
1. **Comparison of Two Independent Poisson Rates**: Let $X \sim \text{Poisson}(\lambda_1)$ and $Y \sim \text{Poisson}(\lambda_2)$ be independent. To test $H_0 : \lambda_1 = \lambda_2$ (or $\lambda_1 / \lambda_2 = \rho_0$) against $H_1 : \lambda_1 > \lambda_2$, write the joint mass function as:
   $$\mathbb{P}(X = x, Y = y) = \frac{e^{-(\lambda_1 + \lambda_2)}}{x! y!} \exp\Big( \underbrace{\ln(\lambda_1 / \lambda_2)}_{\vartheta} x + \underbrace{\ln(\lambda_2)}_{\eta} \underbrace{(x + y)}_{U} \Big)$$
   Conditioning on the total count $U = X + Y = u$, the conditional distribution of $X$ given $X + Y = u$ is **Binomial**:
   $$X \mid (X + Y = u) \sim \text{Binomial}\left(u, \; p = \frac{\lambda_1}{\lambda_1 + \lambda_2}\right)$$
   Under $H_0 : \lambda_1 = \lambda_2$, $p = 1/2$, so the exact UMPU test of $H_0 : \lambda_1 \le \lambda_2$ versus $H_1 : \lambda_1 > \lambda_2$ is the exact conditional $\text{Binomial}(u, 0.5)$ test!
2. **Comparison of Two Binomial Proportions (Fisher's Exact Test)**: Let $X \sim \text{Binomial}(m, p_1)$ and $Y \sim \text{Binomial}(n, p_2)$ be independent. The joint mass function factors in terms of the **log-odds ratio** $\vartheta = \ln\left(\frac{p_1(1-p_2)}{p_2(1-p_1)}\right)$ multiplying $X$ and the nuisance parameter $\eta = \ln\left(\frac{p_2}{1-p_2}\right)$ multiplying the total successes $U = X + Y$. Conditioning on the marginal total $X + Y = u$ under $H_0 : p_1 = p_2$ ($\vartheta = 0$) yields the central **Hypergeometric distribution** $\mathbb{P}_0(X = x \mid X + Y = u) = \binom{m}{x}\binom{n}{u-x} / \binom{m+n}{u}$, proving that **Fisher's Exact Test** (with boundary randomization) is the exact UMPU test for $2 \times 2$ contingency tables!

## 3.5 Symmetry and Group Invariance: Maximal Invariants and Uniformly Most Powerful Invariant (UMPI) Tests

Alongside unbiasedness, a second fundamental structural principle for resolving composite hypotheses and nuisance parameters is **group invariance**, developed systematically by E. J. G. Pitman, Abraham Wald, Charles Stein, and Erich Lehmann. The invariance principle asserts that if a statistical testing problem is symmetric with respect to a natural mathematical group of coordinate transformations (such as changes in units of measurement, shifts of origin, permutations of sample indices, or orthogonal rotations), then the statistical decision rule should respect that same symmetry—yielding identical inferences regardless of which coordinate system the investigator chooses.

### Group Action on the Sample Space and Induced Action on the Parameter Space

Let $\mathcal{G}$ be a mathematical **group** of bijective, bimeasurable transformations $g : \mathcal{X} \to \mathcal{X}$ acting on the sample space $(\mathcal{X}, \mathcal{A})$.
1. **Invariance of the Statistical Model $\mathcal{P}$**: The family of probability distributions $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ is said to be **invariant under the group $\mathcal{G}$** if for every transformation $g \in \mathcal{G}$ and every parameter $\theta \in \Theta$, the transformed random vector $g(\mathbf{X})$ (when $\mathbf{X} \sim P_\theta$) belongs to the same family $\mathcal{P}$, with a uniquely determined parameter denoted $\bar{g}(\theta) \in \Theta$:
   $$\mathbb{P}_\theta\left(g(\mathbf{X}) \in A\right) = \mathbb{P}_{\bar{g}(\theta)}(\mathbf{X} \in A) \quad \forall A \in \mathcal{A}$$
   The induced mapping $\bar{g} : \Theta \to \Theta$ forms a group $\bar{\mathcal{G}}$ of transformations on the parameter space $\Theta$.
2. **Invariance of the Hypothesis Testing Problem**: The testing problem $H_0 : \theta \in \Theta_0$ versus $H_1 : \theta \in \Theta_1$ is said to be **invariant under $\mathcal{G}$** if the model $\mathcal{P}$ is invariant under $\mathcal{G}$ and every induced transformation $\bar{g} \in \bar{\mathcal{G}}$ preserves both the null and alternative parameter spaces:
   $$\bar{g}(\Theta_0) = \Theta_0 \qquad \text{and} \qquad \bar{g}(\Theta_1) = \Theta_1 \quad \forall g \in \mathcal{G}$$

### Invariant Tests and Characterization via Maximal Invariants

A test function $\phi : \mathcal{X} \to [0, 1]$ is defined to be **invariant under $\mathcal{G}$** if it produces the exact same rejection probability before and after applying any transformation $g \in \mathcal{G}$:

$$\phi(g(\mathbf{x})) = \phi(\mathbf{x}) \quad \forall \mathbf{x} \in \mathcal{X}, \quad \forall g \in \mathcal{G}$$

Equivalently, $\phi$ is constant on each **orbit** $\mathcal{O}_{\mathbf{x}} = \{g(\mathbf{x}) : g \in \mathcal{G}\}$ of the sample space. How do we characterize all invariant functions algebraically?

**Definition (Maximal Invariant Statistic)**: A statistic $M : \mathcal{X} \to \mathcal{M}$ is called a **maximal invariant** under the group $\mathcal{G}$ if it satisfies two properties:
1. **Invariance**: $M(g(\mathbf{x})) = M(\mathbf{x})$ for all $\mathbf{x} \in \mathcal{X}$ and all $g \in \mathcal{G}$.
2. **Maximality (Orbit Separation)**: Whenever two sample realizations have the same value of $M$, they must lie on the same orbit of $\mathcal{G}$:
   $$M(\mathbf{x}_1) = M(\mathbf{x}_2) \implies \exists g \in \mathcal{G} \text{ such that } \mathbf{x}_2 = g(\mathbf{x}_1)$$

### Theorem 3.4: Reduction of Invariant Tests to the Maximal Invariant

Let $M(\mathbf{X})$ be a maximal invariant under $\mathcal{G}$.
1. A test function $\phi(\mathbf{x})$ is invariant under $\mathcal{G}$ **if and only if** $\phi(\mathbf{x})$ is a function of the maximal invariant $M(\mathbf{x})$ alone—that is, there exists a measurable function $h : \mathcal{M} \to [0, 1]$ such that $\phi(\mathbf{x}) = h(M(\mathbf{x}))$ for all $\mathbf{x} \in \mathcal{X}$.
2. The probability distribution of $M(\mathbf{X})$ under $P_\theta$ depends on $\theta$ **only through the parameter maximal invariant** $\nu(\theta)$ under the induced group $\bar{\mathcal{G}}$.

#### Proof of Part 1:
If $\phi(\mathbf{x}) = h(M(\mathbf{x}))$, then $\phi(g(\mathbf{x})) = h(M(g(\mathbf{x}))) = h(M(\mathbf{x})) = \phi(\mathbf{x})$, so $\phi$ is invariant. Conversely, suppose $\phi$ is invariant under $\mathcal{G}$. If $M(\mathbf{x}_1) = M(\mathbf{x}_2)$, then by maximality there exists $g \in \mathcal{G}$ such that $\mathbf{x}_2 = g(\mathbf{x}_1)$, which implies $\phi(\mathbf{x}_2) = \phi(g(\mathbf{x}_1)) = \phi(\mathbf{x}_1)$. Because $\phi(\mathbf{x})$ takes a single well-defined value on each level set $\{M(\mathbf{x}) = m\}$, $\phi(\mathbf{x}) = h(M(\mathbf{x}))$ is a function of $M(\mathbf{x})$ alone!

### Canonical UMPI Derivations: Student's $t$-Test and Variance Ratio $F$-Tests

A test $\phi^*$ in the class of invariant level-$\alpha$ tests is called **Uniformly Most Powerful Invariant (UMPI)** if it maximizes power uniformly across $\Theta_1$ among all invariant level-$\alpha$ tests.
- **Scale Invariance and One-Sided Student's $t$-Test**: For $X_1, \dots, X_n \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma^2)$, consider testing $H_0 : \mu \le 0$ versus $H_1 : \mu > 0$ with $\sigma^2 > 0$ unknown. The problem is invariant under the **positive scale group** $\mathcal{G}_+ = \{g_c(\mathbf{x}) = c\mathbf{x} : c > 0\}$, which induces $\bar{g}_c(\mu, \sigma^2) = (c\mu, c^2\sigma^2)$, preserving $\{\mu \le 0\}$ and $\{\mu > 0\}$. Reducing to the sufficient statistic $(\bar{X}, S^2)$ where $g_c(\bar{X}, S^2) = (c\bar{X}, c^2 S^2)$, the maximal invariant is the **Student's $t$-statistic** $M(\bar{X}, S^2) = \frac{\sqrt{n}\bar{X}}{S}$! The parameter maximal invariant is the signal-to-noise ratio $\delta = \sqrt{n}\mu/\sigma$. Under $\delta$, $M(\mathbf{X}) \sim t_{n-1}(\delta)$ follows the **non-central $t$-distribution**, which has a strict Monotone Likelihood Ratio in $t$. By the Karlin-Rubin Theorem applied to $M(\mathbf{X})$, the one-sided $t$-test $\{t(\mathbf{X}) > t_{n-1, 1-\alpha}\}$ is UMPI!
- **Sign-and-Scale Invariance and Two-Sided $t$-Test**: For $H_0 : \mu = 0$ versus $H_1 : \mu \neq 0$, the problem is invariant under the full non-zero scale group $\mathcal{G}_{\pm} = \{g_c(\mathbf{x}) = c\mathbf{x} : c \neq 0\}$, which maps $(\bar{X}, S^2) \mapsto (c\bar{X}, c^2 S^2)$. The maximal invariant is $M(\bar{X}, S^2) = t^2 = \frac{n\bar{X}^2}{S^2} \sim F_{1, n-1}(\delta^2)$, which has a strict MLR in $t^2$ with respect to $\delta^2 = n\mu^2/\sigma^2$. Thus the two-sided $t$-test $\{|t(\mathbf{X})| > t_{n-1, 1-\alpha/2}\}$ is UMPI!

## 3.6 Asymptotic Comparison of Competing Tests: Pitman Asymptotic Relative Efficiency (ARE) and Bahadur Efficiency

When comparing two competing test sequences $\{T_{1,n}\}$ and $\{T_{2,n}\}$—such as comparing a nonparametric rank test against a parametric Student's $t$-test, or comparing a sign test against a sample mean test—both tests are typically **consistent**: for any fixed alternative parameter $\theta_1 > \theta_0$, the power of both tests converges to $1$ as $n \to \infty$. Consequently, comparing their limiting power at a fixed alternative yields the uninformative tie $1 = 1$.

To obtain a sharp, discriminating asymptotic comparison between two consistent test sequences, E. J. G. Pitman (1948) and G. E. Noether (1955) introduced the framework of **contiguous local alternatives** and **Pitman Asymptotic Relative Efficiency (ARE)**.

### Local Pitman Alternatives and the Efficacy Functional

Instead of holding the alternative parameter $\theta_1$ fixed as $n \to \infty$, we consider a sequence of **local Pitman alternatives** that shrink toward the null hypothesis $\theta_0$ at the canonical parametric rate $n^{-1/2}$:

$$H_{1,n} : \theta_n = \theta_0 + \frac{h}{\sqrt{n}}, \quad h > 0$$

At this $O(n^{-1/2})$ local scale, the growing sample information $O(n)$ balances the shrinking signal squared $O(n^{-1})$, so that the limiting power of a size-$\alpha$ test converges to a non-trivial value $\beta^*(h) \in (\alpha, 1)$ strictly between $\alpha$ and $1$!

**Theorem 3.5 (Noether's Theorem for Asymptotic Power and Pitman Efficacy)**: Suppose $T_n = T_n(\mathbf{X}_n)$ is a sequence of test statistics for testing $H_0 : \theta = \theta_0$ against $H_1 : \theta > \theta_0$ satisfying the following regularity conditions in a neighborhood of $\theta_0$:
1. There exist a differentiable asymptotic mean function $\mu(\theta)$ with $\mu'(\theta_0) > 0$ and a continuous asymptotic scale function $\sigma(\theta) > 0$ such that under $P_\theta$:
   $$\frac{\sqrt{n}\left(T_n - \mu(\theta)\right)}{\sigma(\theta)} \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{as } n \to \infty$$
2. Continuity of variance at the null: $\lim_{n \to \infty} \frac{\sigma(\theta_n)}{\sigma(\theta_0)} = 1$ for $\theta_n = \theta_0 + h/\sqrt{n}$.

Then the upper-tail size-$\alpha$ test rejecting $H_0$ when $\frac{\sqrt{n}(T_n - \mu(\theta_0))}{\sigma(\theta_0)} > z_{1-\alpha}$ has **asymptotic local power** under $\theta_n = \theta_0 + h/\sqrt{n}$ given by:

$$\lim_{n \to \infty} \beta_n\left(\theta_0 + \frac{h}{\sqrt{n}}\right) = 1 - \Phi\Big( z_{1-\alpha} - h \cdot c(T) \Big) = \Phi\Big( h \cdot c(T) - z_{1-\alpha} \Big)$$

where the quantity $c(T)$ (or its square $e(T) = [c(T)]^2$) is defined as the **Pitman Efficacy** of the test sequence $\{T_n\}$ at $\theta_0$:

$$c(T) = \frac{\mu'(\theta_0)}{\sigma(\theta_0)} = \lim_{n \to \infty} \frac{\left.\frac{d}{d\theta} \mathbb{E}_\theta[T_n]\right|_{\theta = \theta_0}}{\sqrt{n \, \text{Var}_{\theta_0}(T_n)}}$$

#### Proof of Noether's Formula and Pitman ARE:
Under the local alternative $\theta_n = \theta_0 + h/\sqrt{n}$, expand $\mu(\theta_n)$ around $\theta_0$ via a first-order Taylor expansion: $\mu(\theta_n) = \mu(\theta_0) + \frac{h}{\sqrt{n}} \mu'(\theta_0) + o(n^{-1/2})$. We rewrite the null-standardized test statistic $Z_{n,0} = \frac{\sqrt{n}(T_n - \mu(\theta_0))}{\sigma(\theta_0)}$ in terms of the $\theta_n$-standardized variable $Z_{n,\theta_n} = \frac{\sqrt{n}(T_n - \mu(\theta_n))}{\sigma(\theta_n)} \xrightarrow{d} \mathcal{N}(0, 1)$:

$$Z_{n,0} = \frac{\sigma(\theta_n)}{\sigma(\theta_0)} Z_{n,\theta_n} + \frac{\sqrt{n}\left(\mu(\theta_n) - \mu(\theta_0)\right)}{\sigma(\theta_0)} = \left(1 + o(1)\right) Z_{n,\theta_n} + h \frac{\mu'(\theta_0)}{\sigma(\theta_0)} + o(1)$$

By Slutsky's Theorem, under $\theta_n$, $Z_{n,0} \xrightarrow{d} \mathcal{N}\left(h \frac{\mu'(\theta_0)}{\sigma(\theta_0)}, \, 1\right)$, so $\mathbb{P}_{\theta_n}(Z_{n,0} > z_{1-\alpha}) \to 1 - \Phi\left(z_{1-\alpha} - h \frac{\mu'(\theta_0)}{\sigma(\theta_0)}\right)$.

Now suppose two competing test sequences $\{T_{1,n_1}\}$ (using sample size $n_1$) and $\{T_{2,n_2}\}$ (using sample size $n_2$) are applied at the same significance level $\alpha$ against the same local alternative $\theta = \theta_0 + \Delta$ (so $h_1 = \sqrt{n_1}\Delta$ and $h_2 = \sqrt{n_2}\Delta$). For both tests to achieve the **exact same limiting power** $\beta \in (\alpha, 1)$, their non-centrality shifts must be equal:

$$\sqrt{n_1} \Delta \frac{\mu_1'(\theta_0)}{\sigma_1(\theta_0)} = \sqrt{n_2} \Delta \frac{\mu_2'(\theta_0)}{\sigma_2(\theta_0)} \implies \frac{n_2}{n_1} = \left( \frac{\mu_1'(\theta_0) / \sigma_1(\theta_0)}{\mu_2'(\theta_0) / \sigma_2(\theta_0)} \right)^2$$

The **Pitman Asymptotic Relative Efficiency (ARE)** of test $T_1$ relative to test $T_2$ is defined as the limiting reciprocal ratio of sample sizes $\lim \frac{n_2}{n_1}$ required to achieve identical power $\beta$ at the same level $\alpha$ as $\Delta \to 0$:

$$\text{ARE}(T_1, T_2) = \lim_{n_1 \to \infty} \frac{n_2(\alpha, \beta, n_1)}{n_1} = \left[ \frac{c(T_1)}{c(T_2)} \right]^2 = \frac{\left[\mu_1'(\theta_0) / \sigma_1(\theta_0)\right]^2}{\left[\mu_2'(\theta_0) / \sigma_2(\theta_0)\right]^2}$$

For example, if $\text{ARE}(T_1, T_2) = 0.637$ (as for the Sign test relative to Student's $t$-test under a normal distribution, $2/\pi \approx 0.6366$), then Student's $t$-test requires only $63.7\%$ as many observations as the Sign test ($n_2 \approx 0.637 n_1$) to achieve the same local detection power!

### Bahadur Efficiency and Exact Slopes

An alternative asymptotic framework introduced by R. R. Bahadur (1960) reverses the roles of $\alpha$ and $\beta$: instead of shrinking $\theta_n \to \theta_0$ at fixed $\alpha$, **Bahadur efficiency** fixes the alternative parameter $\theta \in \Theta_1$ and fixes the target power $\beta \in (0, 1)$, and examines the exponential rate at which the observed **p-value** $P_n(\mathbf{X}_n)$ decays to zero as $n \to \infty$:

$$-\frac{2}{n} \ln P_n(\mathbf{X}_n) \xrightarrow{P_\theta} c_{\text{Bahadur}}(\theta)$$

The limit $c_{\text{Bahadur}}(\theta)$ is called the **Bahadur slope** of the test sequence at $\theta$. By Ragnar Bahadur's theorem, for any test sequence, the Bahadur slope is bounded above by twice the Kullback-Leibler divergence $2 D_{\text{KL}}(P_\theta \,\|\, P_{\theta_0})$, and Likelihood Ratio tests achieve this maximal Bahadur slope globally.

### Comparison of Pitman, Bahadur, and Hodges-Lehmann Asymptotic Efficiencies

In advanced mathematical statistics, competing test sequences are evaluated across three complementary asymptotic regimes, corresponding to which of the three quantities—significance level $\alpha_n$, Type II error $\tilde{\beta}_n = 1 - \beta_n$, and effect size $\Delta_n = |\theta_n - \theta_0|$—is driven to zero as the sample size $n$ approaches infinity:
1. **Pitman Efficiency (Local Moderate-Deviation Regime)**: Fixes both the significance level $\alpha \in (0, 1)$ and the target power $\beta \in (\alpha, 1)$, while shrinking the alternative parameter toward the null hypothesis at the inverse square-root rate $\theta_n = \theta_0 + h / \sqrt{n}$. Because Pitman efficiency depends exclusively on the first derivative of the asymptotic mean $\mu'(\theta_0)$ and the null variance $\sigma^2(\theta_0)$, its computation requires only Central Limit Theorem (normal) approximations rather than large-deviation tail probabilities.
2. **Bahadur Efficiency (Fixed-Alternative Type I Large-Deviation Regime)**: Fixes the alternative parameter $\theta \in \Theta_1$ and fixes the target power $\beta \in (0, 1)$, while driving the Type I error (or p-value $P_n$) exponentially to zero as $n \to \infty$. Evaluating Bahadur slopes requires Cramér-Chernoff large-deviation theory for the extreme upper tail of the test statistic under the null hypothesis $H_0$.
3. **Hodges-Lehmann Efficiency (Fixed-Alternative Type II Large-Deviation Regime)**: Introduced by J. L. Hodges and E. L. Lehmann (1956), this regime fixes the significance level $\alpha \in (0, 1)$ and fixes the alternative parameter $\theta \in \Theta_1$, and examines the exponential decay rate $d_{\text{HL}}(\theta) = \lim_{n \to \infty} -\frac{2}{n} \ln \tilde{\beta}_n(\theta)$ of the Type II error probability $\tilde{\beta}_n(\theta) = 1 - \beta_n(\theta)$ under the alternative distribution $P_\theta$. By Stein's Lemma in information theory, the optimal Hodges-Lehmann exponent is governed by the reversed Kullback-Leibler divergence $2 D_{\text{KL}}(P_{\theta_0} \,\|\, P_\theta)$.

### The Hunt-Stein Theorem: Group Invariance and Minimax Optimality

Why does restricting attention to group-invariant tests (Section 3.5) or unbiased tests (Section 3.1) yield procedures with exceptional global risk properties even among non-invariant competitors? The deep mathematical answer is provided by the **Hunt-Stein Theorem** (proved by Gilbert Hunt and Charles Stein in 1946).

Suppose a hypothesis testing problem $H_0 : \theta \in \Theta_0$ versus $H_1 : \theta \in \Theta_1$ is invariant under a transformation group $\mathcal{G}$ that is **amenable** (meaning $\mathcal{G}$ is compact, finite, abelian, or solvable—such as the translation group $\mathbb{R}^k$, the positive scale group $\mathbb{R}_+$, the permutation group $S_n$, or the orthogonal rotation group $O(n)$). The Hunt-Stein Theorem establishes that for any arbitrary level-$\alpha$ test $\phi(\mathbf{x})$ (even one that violates invariance), there exists an **invariant** level-$\alpha$ test $\phi_{\text{inv}}(\mathbf{x})$ (constructed by averaging $\phi(g(\mathbf{x}))$ over $\mathcal{G}$ using a right-invariant Haar measure or amenability sequence) whose worst-case minimum power across every group orbit in $\Theta_1$ is at least as high as that of $\phi$:

$$\inf_{\theta \in \mathcal{O}} \mathbb{E}_\theta\left[\phi_{\text{inv}}(\mathbf{X})\right] \ge \inf_{\theta \in \mathcal{O}} \mathbb{E}_\theta\left[\phi(\mathbf{X})\right]$$

Consequently, whenever a Uniformly Most Powerful Invariant (UMPI) test exists under an amenable group $\mathcal{G}$, that UMPI test is automatically a **minimax test** across the entire unrestricted class of all level-$\alpha$ tests! Conversely, when the transformation group $\mathcal{G}$ is non-amenable (such as the full general linear group $GL(p, \mathbb{R})$ of all invertible $p \times p$ matrices), the Hunt-Stein Theorem can fail, showing that mathematical symmetry and amenability dictate when invariance preserves global minimaxity.

## Fully worked question 1: Exact Two-Sided UMPU Test vs Equal-Tailed Test for Exponential Scale Parameter

### Question
Let $X_1, X_2, \dots, X_n \overset{\text{iid}}{\sim} \text{Exponential}(\theta)$ be a random sample of size $n = 2$ with probability density function $f(x; \theta) = \frac{1}{\theta} e^{-x/\theta}$ for $x > 0, \theta > 0$. We wish to test the point null hypothesis $H_0 : \theta = 1$ against the two-sided alternative $H_1 : \theta \neq 1$ at significance level $\alpha = 0.05$.

1. Express the joint density in natural exponential family form in terms of $T = X_1 + X_2$, state the exact null distribution of $T$ under $H_0 : \theta = 1$, and write down the two integral equations that determine the critical values $0 < c_1 < c_2$ of the Uniformly Most Powerful Unbiased (UMPU) size-$\alpha$ test.
2. Prove by integration by parts that the two UMPU conditions simplify to the system of equations:
   $$(1 + c_1) e^{-c_1} - (1 + c_2) e^{-c_2} = 1 - \alpha \qquad \text{and} \qquad c_1^2 e^{-c_1} = c_2^2 e^{-c_2}$$
3. Compare the equal-tailed critical values $(c_{1,\text{eq}}, c_{2,\text{eq}})$ for $\alpha = 0.05$ against the exact UMPU critical values $(c_1^*, c_2^*) = (0.2062, 6.2656)$, and show explicitly that the equal-tailed test is **biased** (having derivative $\beta_{\text{eq}}'(1) \neq 0$ and power strictly below $\alpha = 0.05$ for $\theta$ slightly smaller than $1$).

### Solution, step 1: Exponential family representation, null distribution, and UMPU moment conditions
For $n = 2$ independent $\text{Exponential}(\theta)$ observations, the joint density is:

$$f_2(x_1, x_2; \theta) = \frac{1}{\theta^2} \exp\left(-\frac{x_1 + x_2}{\theta}\right) = \exp\Big( \eta(\theta) T - 2\ln(\theta) \Big), \quad x_1, x_2 > 0$$

where $\eta(\theta) = -1/\theta$ is a strictly increasing function of $\theta$ and $T = X_1 + X_2$ is the complete sufficient statistic. Under any $\theta > 0$, $T \sim \text{Gamma}(2, \theta)$ with probability density function:

$$f_T(t; \theta) = \frac{t}{\theta^2} e^{-t/\theta}, \quad t > 0$$

Under the null hypothesis $H_0 : \theta = 1$, the density is $f_T(t; 1) = t e^{-t}$ for $t > 0$, with null expectation $\mathbb{E}_1[T] = 2$. By Theorem 3.1, the UMPU size-$\alpha$ test rejects $H_0$ when $T < c_1$ or $T > c_2$, where the acceptance interval $[c_1, c_2]$ satisfies the complementary size and first-moment conditions:

$$\mathbb{P}_1(c_1 \le T \le c_2) = \int_{c_1}^{c_2} t e^{-t} \, dt = 1 - \alpha$$

$$\mathbb{E}_1\left[T \, \mathbf{1}_{[c_1, c_2]}(T)\right] = \int_{c_1}^{c_2} t^2 e^{-t} \, dt = (1 - \alpha) \mathbb{E}_1[T] = 2(1 - \alpha)$$

### Solution, step 2: Algebraic reduction of the UMPU integral system via integration by parts
Evaluate the first integral using the antiderivative $\frac{d}{dt}\left[-(1 + t)e^{-t}\right] = t e^{-t}$:

$$\int_{c_1}^{c_2} t e^{-t} \, dt = \Big[-(1 + t) e^{-t}\Big]_{c_1}^{c_2} = (1 + c_1) e^{-c_1} - (1 + c_2) e^{-c_2} = 1 - \alpha$$

This establishes the first equation. Now apply integration by parts to the second integral with $u = t^2$ ($du = 2t \, dt$) and $dv = e^{-t} \, dt$ ($v = -e^{-t}$):

$$\int_{c_1}^{c_2} t^2 e^{-t} \, dt = \Big[-t^2 e^{-t}\Big]_{c_1}^{c_2} + 2 \int_{c_1}^{c_2} t e^{-t} \, dt = \left(c_1^2 e^{-c_1} - c_2^2 e^{-c_2}\right) + 2(1 - \alpha)$$

Equating this expression to the required UMPU moment condition $2(1 - \alpha)$:

$$\left(c_1^2 e^{-c_1} - c_2^2 e^{-c_2}\right) + 2(1 - \alpha) = 2(1 - \alpha) \implies c_1^2 e^{-c_1} = c_2^2 e^{-c_2}$$

Notice the geometric elegance of $c_1^2 e^{-c_1} = c_2^2 e^{-c_2}$: since $t f_T(t; 1) = t^2 e^{-t}$, the exact UMPU critical values $c_1 < c_2$ occur where the weighted density function $g(t) = t^2 e^{-t}$ (which peaks at $t = 2$) takes equal heights on either side of its mode $t = 2$!

### Solution, step 3: Numerical comparison and proof of bias for the equal-tailed test
For the **equal-tailed test** at $\alpha = 0.05$, we set each tail probability to $\alpha / 2 = 0.025$:
- Left tail: $\int_0^{c_{1,\text{eq}}} t e^{-t} \, dt = 1 - (1 + c_{1,\text{eq}}) e^{-c_{1,\text{eq}}} = 0.025 \implies c_{1,\text{eq}} \approx 0.2422$
- Right tail: $\int_{c_{2,\text{eq}}}^\infty t e^{-t} \, dt = (1 + c_{2,\text{eq}}) e^{-c_{2,\text{eq}}} = 0.025 \implies c_{2,\text{eq}} \approx 5.5716$

Let us check the slope of the power function $\beta(\theta) = 1 - \int_{c_1/\theta}^{c_2/\theta} u e^{-u} \, du$ at $\theta = 1$. By Leibniz's rule, differentiating $\beta(\theta)$ with respect to $\theta$ at $\theta = 1$ gives:

$$\beta'(1) = c_1^2 e^{-c_1} - c_2^2 e^{-c_2}$$

For the equal-tailed cutoffs $(0.2422, 5.5716)$:
- $c_{1,\text{eq}}^2 e^{-c_{1,\text{eq}}} = (0.2422)^2 e^{-0.2422} \approx 0.05866 \times 0.78490 = 0.04604$
- $c_{2,\text{eq}}^2 e^{-c_{2,\text{eq}}} = (5.5716)^2 e^{-5.5716} \approx 31.0427 \times 0.003804 = 0.11810$

Thus $\beta_{\text{eq}}'(1) = 0.04604 - 0.11810 = -0.07206 < 0$? Wait: let us check the sign of $\beta'(\theta)$ carefully! Since $\beta(\theta) = 1 - \left[(1 + c_1/\theta)e^{-c_1/\theta} - (1 + c_2/\theta)e^{-c_2/\theta}\right]$, differentiating with respect to $\theta$ gives:

$$\beta'(\theta) = -\left[ \frac{c_1^2}{\theta^3} e^{-c_1/\theta} - \frac{c_2^2}{\theta^3} e^{-c_2/\theta} \right] = \frac{1}{\theta^3} \left( c_2^2 e^{-c_2/\theta} - c_1^2 e^{-c_1/\theta} \right)$$

At $\theta = 1$, $\beta_{\text{eq}}'(1) = c_{2,\text{eq}}^2 e^{-c_{2,\text{eq}}} - c_{1,\text{eq}}^2 e^{-c_{1,\text{eq}}} = 0.11810 - 0.04604 = +0.07206 > 0$! Because the slope at $\theta = 1$ is strictly positive ($+0.07206$), for values of $\theta$ slightly smaller than $1$ (e.g., $\theta = 0.90$), the power of the equal-tailed test drops **strictly below $\alpha = 0.05$** ($\beta_{\text{eq}}(0.90) \approx 0.0457 < 0.05$), proving that the equal-tailed test is **biased**!

In contrast, for the UMPU cutoffs $(c_1^*, c_2^*) = (0.2062, 6.2656)$, both sides equal $(0.2062)^2 e^{-0.2062} \approx (6.2656)^2 e^{-6.2656} \approx 0.07462$, so $\beta_{\text{UMPU}}'(1) = 0$ and $\beta_{\text{UMPU}}(\theta) > 0.05$ for all $\theta \neq 1$.

## Fully worked question 2: Conditional UMPU Test for Comparing Two Poisson Rates and Fisher's Exact 2x2 Test

### Question
Two independent radiation counters monitor background alpha-particle emissions in two separate chambers over identical 1-hour windows, recording $X_1 \sim \text{Poisson}(\lambda_1)$ and $X_2 \sim \text{Poisson}(\lambda_2)$. We wish to test the null hypothesis $H_0 : \lambda_1 \le \lambda_2$ against the alternative $H_1 : \lambda_1 > \lambda_2$ at exact significance level $\alpha = 0.05$ in the presence of the unknown nuisance rate $\lambda_2 > 0$.

1. Express the joint probability mass function of $(X_1, X_2)$ in multiparameter exponential family form with target parameter $\vartheta = \ln(\lambda_1 / \lambda_2)$ and nuisance parameter $\eta = \ln(\lambda_2)$, and derive the exact conditional distribution of $X_1$ given $U = X_1 + X_2 = u$.
2. Suppose the experiment observes $x_1 = 9$ counts in Chamber 1 and $x_2 = 1$ count in Chamber 2 (so $u = 10$). Construct the exact conditional UMPU randomized test $\phi^*(x_1 \mid u = 10)$ at $\alpha = 0.05$, and calculate both the non-randomized p-value and Lancaster's mid-p-value for $(x_1, x_2) = (9, 1)$.
3. Compute the exact conditional power of $\phi^*(X_1 \mid u = 10)$ when the true rate ratio is $\lambda_1 / \lambda_2 = 3$.

### Solution, step 1: Multiparameter exponential factorization and conditional Binomial distribution
By independence of $X_1 \sim \text{Poisson}(\lambda_1)$ and $X_2 \sim \text{Poisson}(\lambda_2)$, the joint probability mass function for non-negative integers $(x_1, x_2)$ is:

$$f(x_1, x_2; \lambda_1, \lambda_2) = \frac{e^{-\lambda_1} \lambda_1^{x_1}}{x_1!} \frac{e^{-\lambda_2} \lambda_2^{x_2}}{x_2!} = \frac{e^{-(\lambda_1 + \lambda_2)}}{x_1! x_2!} \lambda_1^{x_1} \lambda_2^{(x_1 + x_2) - x_1} = \frac{e^{-(\lambda_1 + \lambda_2)}}{x_1! x_2!} \left(\frac{\lambda_1}{\lambda_2}\right)^{x_1} \lambda_2^{x_1 + x_2}$$

Exponentiating the powers yields the canonical two-parameter exponential family form:

$$f(x_1, x_2; \vartheta, \eta) = \frac{\exp\left(-e^\eta (1 + e^\vartheta)\right)}{x_1! x_2!} \exp\Big( \vartheta x_1 + \eta (x_1 + x_2) \Big)$$

where $\vartheta = \ln(\lambda_1 / \lambda_2)$ ($\vartheta \le 0 \iff \lambda_1 \le \lambda_2$) and $\eta = \ln(\lambda_2)$ is the nuisance parameter with complete boundary sufficient statistic $U = X_1 + X_2$. Since $U = X_1 + X_2 \sim \text{Poisson}(\lambda_1 + \lambda_2)$, the conditional probability mass function of $X_1$ given $U = u$ is:

$$\mathbb{P}(X_1 = x_1 \mid X_1 + X_2 = u) = \frac{\frac{e^{-\lambda_1} \lambda_1^{x_1}}{x_1!} \frac{e^{-\lambda_2} \lambda_2^{u - x_1}}{(u - x_1)!}}{\frac{e^{-(\lambda_1 + \lambda_2)} (\lambda_1 + \lambda_2)^u}{u!}} = \binom{u}{x_1} p^{x_1} (1 - p)^{u - x_1}, \quad x_1 = 0, 1, \dots, u$$

where $p = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{e^\vartheta}{1 + e^\vartheta}$. Thus $X_1 \mid (U = u) \sim \text{Binomial}(u, p)$, and testing $H_0 : \lambda_1 \le \lambda_2$ ($\vartheta \le 0$) versus $H_1 : \lambda_1 > \lambda_2$ ($\vartheta > 0$) reduces conditionally to testing $H_0 : p \le 0.5$ versus $H_1 : p > 0.5$.

### Solution, step 2: Conditional UMPU test construction for u = 10 and p-value evaluation at x_1 = 9
Given the observed total count $u = x_1 + x_2 = 9 + 1 = 10$, under the boundary null hypothesis $p_0 = 0.5$, $X_1 \mid (U = 10) \sim \text{Binomial}(10, 0.5)$ with denominator $2^{10} = 1024$. Let us compute the upper tail probabilities:
- $\mathbb{P}_{p=0.5}(X_1 = 10 \mid U = 10) = \binom{10}{10} / 1024 = 1 / 1024 \approx 0.000977$
- $\mathbb{P}_{p=0.5}(X_1 = 9 \mid U = 10) = \binom{10}{9} / 1024 = 10 / 1024 \approx 0.009766$
- $\mathbb{P}_{p=0.5}(X_1 = 8 \mid U = 10) = \binom{10}{8} / 1024 = 45 / 1024 \approx 0.043945$

Summing from the top:
- $\mathbb{P}_{0.5}(X_1 \ge 9 \mid U = 10) = \frac{1 + 10}{1024} = \frac{11}{1024} \approx 0.010742 < 0.05$
- $\mathbb{P}_{0.5}(X_1 \ge 8 \mid U = 10) = \frac{1 + 10 + 45}{1024} = \frac{56}{1024} \approx 0.054688 > 0.05$

Therefore, the exact conditional UMPU test of size $\alpha = 0.05$ rejects with probability $1$ when $X_1 \ge 9$, and randomizes at $X_1 = 8$ with probability:

$$\gamma = \frac{0.05 - \frac{11}{1024}}{\frac{45}{1024}} = \frac{51.2 - 11}{45} = \frac{40.2}{45} = \frac{67}{75} \approx 0.893333$$

Since our observed value is $x_1 = 9 \ge 9$, **even the non-randomized test rejects $H_0$ unequivocally at $\alpha = 0.05$**! The exact non-randomized conditional p-value and Lancaster's mid-p-value at $x_1 = 9$ are:

$$p_{\text{exact}} = \mathbb{P}_{0.5}(X_1 \ge 9 \mid U = 10) = \frac{11}{1024} \approx 0.01074, \quad p_{\text{mid}} = \frac{1}{1024} + \frac{1}{2}\left(\frac{10}{1024}\right) = \frac{6}{1024} \approx 0.00586$$

### Solution, step 3: Conditional power evaluation under alternative rate ratio lambda_1 / lambda_2 = 3
When the true alternative rate ratio is $\lambda_1 / \lambda_2 = 3$, the conditional Binomial success probability is:

$$p_1 = \frac{\lambda_1 / \lambda_2}{1 + \lambda_1 / \lambda_2} = \frac{3}{1 + 3} = 0.75$$

Thus $X_1 \mid (U = 10) \sim \text{Binomial}(10, 0.75)$. We compute the point probabilities at $x_1 = 8, 9, 10$:
- $\mathbb{P}_{0.75}(X_1 = 10) = (0.75)^{10} \approx 0.056314$
- $\mathbb{P}_{0.75}(X_1 = 9) = 10 (0.75)^9 (0.25)^1 \approx 0.187712$
- $\mathbb{P}_{0.75}(X_1 = 8) = 45 (0.75)^8 (0.25)^2 \approx 0.281568$

Therefore, the exact conditional power of the size-$0.05$ UMPU test $\phi^*(X_1 \mid U = 10)$ at $\lambda_1 / \lambda_2 = 3$ is:

$$\beta(p_1 = 0.75 \mid U = 10) = \mathbb{P}_{0.75}(X_1 \ge 9) + \gamma \, \mathbb{P}_{0.75}(X_1 = 8) = (0.056314 + 0.187712) + \left(\frac{67}{75}\right)(0.281568)$$

$$\beta(p_1 = 0.75 \mid U = 10) = 0.244025 + 0.251534 = 0.495559 \quad (49.56\%)$$

## Fully worked question 3: Maximal Invariant and UMPI Test for Two-Sample Scale Ratio and Pitman ARE of Sign vs t-Test

### Question
1. **Group Invariance (UMPI)**: Let $X_1, \dots, X_m \overset{\text{iid}}{\sim} \mathcal{N}(\mu_1, \sigma_1^2)$ and $Y_1, \dots, Y_n \overset{\text{iid}}{\sim} \mathcal{N}(\mu_2, \sigma_2^2)$ be two independent normal samples where all four parameters $(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2)$ are unknown. Consider testing $H_0 : \sigma_1^2 \le \sigma_2^2$ against $H_1 : \sigma_1^2 > \sigma_2^2$ at level $\alpha$. Identify the natural location-scale transformation group $\mathcal{G}$ that leaves this testing problem invariant, find the maximal invariant $M$ acting on the sufficient statistics $(\bar{X}, \bar{Y}, S_X^2, S_Y^2)$, and derive the Uniformly Most Powerful Invariant (UMPI) test.
2. **Pitman Asymptotic Relative Efficiency (ARE)**: Let $Z_1, \dots, Z_n$ be an i.i.d. sample from a location family $f(z - \theta)$ where $f(u)$ is symmetric about $0$ with variance $\sigma^2 < \infty$ and positive density $f(0) > 0$ at the median. Derive the Pitman Efficacy of the one-sample Sign Test $S_n = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{\{Z_i > 0\}}$ and the Student's $t$-test for testing $H_0 : \theta = 0$ versus $H_1 : \theta > 0$, prove the general formula $\text{ARE}(S, t) = 4 \sigma^2 [f(0)]^2$, and evaluate $\text{ARE}(S, t)$ under both the **Normal** distribution and the **Laplace (Double Exponential)** distribution.

### Solution, step 1: Location-scale group invariance and maximal invariant for the two-sample variance ratio
In the two-sample normal model, the joint minimal sufficient statistic is the four-dimensional vector $\mathbf{T} = (\bar{X}, \bar{Y}, S_X^2, S_Y^2)$, where $S_X^2 = \frac{1}{m-1}\sum_{i=1}^m (X_i - \bar{X})^2$ and $S_Y^2 = \frac{1}{n-1}\sum_{j=1}^n (Y_j - \bar{Y})^2$. The hypotheses $H_0 : \sigma_1^2 / \sigma_2^2 \le 1$ versus $H_1 : \sigma_1^2 / \sigma_2^2 > 1$ depend only on the variance ratio $\Delta = \sigma_1^2 / \sigma_2^2$, and remain unchanged if we shift the two samples by arbitrary location constants $a_1, a_2 \in \mathbb{R}$ and rescale both samples by a **common positive scale factor** $c > 0$:

$$\mathcal{G} = \left\{ g_{a_1, a_2, c}(\mathbf{x}, \mathbf{y}) = (c\mathbf{x} + a_1 \mathbf{1}_m, \; c\mathbf{y} + a_2 \mathbf{1}_n) : a_1, a_2 \in \mathbb{R}, \; c > 0 \right\}$$

On the space of sufficient statistics, $g_{a_1, a_2, c}$ acts via:

$$\bar{g}_{a_1, a_2, c}\left(\bar{X}, \bar{Y}, S_X^2, S_Y^2\right) = \left(c\bar{X} + a_1, \; c\bar{Y} + a_2, \; c^2 S_X^2, \; c^2 S_Y^2\right)$$

First, invariance under translations $(a_1, a_2) \in \mathbb{R}^2$ eliminates $(\bar{X}, \bar{Y})$ completely (since choosing $a_1 = -\bar{X}$ and $a_2 = -\bar{Y}$ maps the first two coordinates to $(0, 0)$), leaving $(S_X^2, S_Y^2)$. Second, under common positive scaling $(c^2 S_X^2, c^2 S_Y^2)$ with $c > 0$, choosing $c = 1 / S_Y$ reduces $(S_X^2, S_Y^2)$ to the single ratio:

$$M\left(\bar{X}, \bar{Y}, S_X^2, S_Y^2\right) = \frac{S_X^2}{S_Y^2} = F$$

Because $M$ is invariant and $S_X^2 / S_Y^2 = \tilde{S}_X^2 / \tilde{S}_Y^2 \implies (\tilde{S}_X^2, \tilde{S}_Y^2) = c^2 (S_X^2, S_Y^2)$ with $c = \tilde{S}_Y / S_Y > 0$, the **sample variance ratio $F = S_X^2 / S_Y^2$ is the unique maximal invariant**! Under parameter ratio $\Delta = \sigma_1^2 / \sigma_2^2$, the scaled variable $\frac{1}{\Delta} F = \frac{S_X^2 / \sigma_1^2}{S_Y^2 / \sigma_2^2} \sim F_{m-1, n-1}$ follows Snedecor's central $F$-distribution with density:

$$f_F(w; \Delta) = \frac{\Gamma\left(\frac{m+n-2}{2}\right)}{\Gamma\left(\frac{m-1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)} \left(\frac{m-1}{n-1}\right)^{\frac{m-1}{2}} \Delta^{-\frac{m-1}{2}} w^{\frac{m-3}{2}} \left(1 + \frac{m-1}{n-1} \frac{w}{\Delta}\right)^{-\frac{m+n-2}{2}}$$

For $0 < \Delta_1 < \Delta_2$, the ratio $f_F(w; \Delta_2) / f_F(w; \Delta_1)$ is proportional to $\left(\frac{1 + \frac{m-1}{(n-1)\Delta_1} w}{1 + \frac{m-1}{(n-1)\Delta_2} w}\right)^{\frac{m+n-2}{2}}$, which is a **strictly increasing function of $w = F$**! By the Karlin-Rubin Theorem, the upper-tail $F$-test rejecting $H_0$ when $F = S_X^2 / S_Y^2 > F_{m-1, n-1, 1-\alpha}$ is the exact **UMPI level-$\alpha$ test**.

### Solution, step 2: Derivation of Pitman Efficacy for the Sign Test and Student's t-Test
Let $Z_1, \dots, Z_n \overset{\text{iid}}{\sim} f(z - \theta)$ with Cumulative Distribution Function $F(z - \theta) = \int_{-\infty}^{z-\theta} f(u) \, du$, where $F(0) = 1/2$ and $F'(0) = f(0) > 0$.
1. **Efficacy of the Sign Test**: Consider the sample proportion of positive observations $S_n = \frac{1}{n}\sum_{i=1}^n \mathbf{1}_{\{Z_i > 0\}}$. Under parameter $\theta$, each indicator $\mathbf{1}_{\{Z_i > 0\}} \sim \text{Bernoulli}(p(\theta))$ with mean and variance:
   $$\mu_S(\theta) = \mathbb{P}_\theta(Z_i > 0) = \int_0^\infty f(z - \theta) \, dz = \int_{-\theta}^\infty f(u) \, du = 1 - F(-\theta)$$
   $$\text{Var}_\theta(S_n) = \frac{p(\theta)(1 - p(\theta))}{n} \implies \sigma_S(\theta) = \sqrt{p(\theta)(1 - p(\theta))}$$
   Differentiating $\mu_S(\theta) = 1 - F(-\theta)$ with respect to $\theta$ via the chain rule yields $\mu_S'(\theta) = f(-\theta)$. Evaluating at the null $\theta_0 = 0$ where $p(0) = 1/2$ and $\sigma_S(0) = \sqrt{(1/2)(1/2)} = 1/2$:
   $$c(S) = \frac{\mu_S'(0)}{\sigma_S(0)} = \frac{f(0)}{1/2} = 2 f(0)$$
2. **Efficacy of Student's $t$-Test**: By Slutsky's Theorem, the Student $t$-statistic $t_n = \frac{\sqrt{n}\bar{Z}_n}{S_n}$ is asymptotically equivalent to $\bar{Z}_n$, which has exact mean $\mu_t(\theta) = \mathbb{E}_\theta[\bar{Z}_n] = \theta$ (so $\mu_t'(0) = 1$) and asymptotic scale $\sigma_t(0) = \sigma = \sqrt{\text{Var}_0(Z_i)}$. Thus the Pitman efficacy of the $t$-test is:
   $$c(t) = \frac{\mu_t'(0)}{\sigma_t(0)} = \frac{1}{\sigma}$$

Taking the squared ratio of their efficacies yields the universal Pitman ARE formula comparing the Sign test to Student's $t$-test:

$$\text{ARE}(S, t) = \left[\frac{c(S)}{c(t)}\right]^2 = \left[\frac{2 f(0)}{1 / \sigma}\right]^2 = 4 \sigma^2 \left[f(0)\right]^2$$

### Solution, step 3: Numerical evaluation under Gaussian vs Laplace distributions
We now evaluate $\text{ARE}(S, t) = 4 \sigma^2 [f(0)]^2$ for the two benchmark distributions:
1. **Gaussian Distribution $\mathcal{N}(\theta, \sigma^2)$**: The zero-mean density is $f(u) = \frac{1}{\sqrt{2\pi}\sigma} e^{-u^2/(2\sigma^2)}$, so the density at the median $u = 0$ is $f(0) = \frac{1}{\sqrt{2\pi}\sigma}$. Substituting into the ARE formula:
   $$\text{ARE}_{\text{Normal}}(S, t) = 4 \sigma^2 \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^2 = \frac{4 \sigma^2}{2\pi \sigma^2} = \frac{2}{\pi} \approx 0.6366 \quad (63.66\%)$$
   Under pure normality, the Sign test retains $63.66\%$ asymptotic efficiency relative to the UMPU $t$-test.
2. **Laplace (Double Exponential) Distribution**: The density with scale parameter $b > 0$ is $f(u) = \frac{1}{2b} e^{-|u|/b}$ for $u \in \mathbb{R}$. Its density at the median $u = 0$ is $f(0) = \frac{1}{2b}$, and its variance is:
   $$\sigma^2 = \int_{-\infty}^\infty u^2 \frac{1}{2b} e^{-|u|/b} \, du = \frac{1}{b} \int_0^\infty u^2 e^{-u/b} \, du = \frac{1}{b} \left(2! \, b^3\right) = 2b^2$$
   Substituting $\sigma^2 = 2b^2$ and $f(0) = \frac{1}{2b}$ into the ARE formula gives:
   $$\text{ARE}_{\text{Laplace}}(S, t) = 4 (2b^2) \left(\frac{1}{2b}\right)^2 = 8b^2 \cdot \frac{1}{4b^2} = 2.0000 \quad (200.0\%)$$

Under the heavier-tailed, sharply peaked Laplace distribution, the simple nonparametric Sign test is **twice as efficient ($200\%$)** as Student's $t$-test—requiring only half as many observations as the $t$-test to achieve identical asymptotic local power!
