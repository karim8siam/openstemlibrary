# Unit 1: Architecture of Statistical Hypothesis Testing: Neyman-Pearson Paradigm, Power Functions & P-Values

Simple and composite statistical hypotheses, parameter space partitions, and critical versus acceptance regions; non-randomized and randomized test functions phi(x), Type I error probability alpha(theta), and Type II error beta(theta); test size, significance level alpha, power function beta(theta) = E_theta[phi(X)], and operating characteristic curves; duality between (1 - alpha) confidence sets and size-alpha hypothesis tests; mathematical properties of p-values and multiple testing corrections.

## 1.1 Statistical Hypotheses, Parameter Space Partitions, and Decision Spaces

In mathematical statistics, inferential theory is divided into two complementary branches: parameter estimation, where observed data are used to construct numerical approximations or plausible sets for unknown parameters, and **statistical hypothesis testing**, where empirical observations are evaluated to adjudicate between competing structural assertions about the underlying probability law governing an experiment. While estimation addresses the question of what value a parameter assumes, hypothesis testing addresses a binary decision problem regarding whether the true state of nature resides within a specified subset of the parameter manifold.

Let $(\mathcal{X}, \mathcal{A}, \mathcal{P})$ denote a parametric statistical model, where $\mathcal{X} \subseteq \mathbb{R}^n$ is the sample space of an observable random vector $\mathbf{X} = (X_1, X_2, \dots, X_n)^T$, $\mathcal{A}$ is a $\sigma$-algebra of measurable events on $\mathcal{X}$, and $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ is a family of candidate probability distributions indexed by a parameter vector $\theta$ belonging to the parameter space $\Theta \subseteq \mathbb{R}^k$. A **statistical hypothesis** is any formal, falsifiable assertion concerning the probability distribution $P_\theta$ of the observable random vector $\mathbf{X}$. In a parametric setting, because the probability law $P_\theta$ is completely indexed by $\theta$, every statistical hypothesis corresponds bijectively to an assertion that the true parameter lies within a particular nonempty subset of $\Theta$.

Formally, the parameter space $\Theta$ is partitioned into two mutually exclusive and exhaustive subsets, denoted by $\Theta_0$ and $\Theta_1$, satisfying the set-theoretic conditions:

$$\Theta = \Theta_0 \cup \Theta_1, \quad \Theta_0 \cap \Theta_1 = \emptyset, \quad \Theta_0 \neq \emptyset, \quad \Theta_1 \neq \emptyset$$

The competing assertions are then formulated as the **null hypothesis**, denoted $H_0$, and the **alternative hypothesis** (or research hypothesis), denoted $H_1$ (or $H_a$):

$$H_0 : \theta \in \Theta_0 \quad \text{versus} \quad H_1 : \theta \in \Theta_1$$

The structural complexity of a hypothesis is governed by the cardinality and topological dimension of its associated parameter subset:
1. **Simple Hypothesis**: A statistical hypothesis is termed **simple** if it completely specifies the probability distribution of the observable sample $\mathbf{X}$ without leaving any unknown nuisance parameters or free coordinates. Equivalently, $H_0 : \theta \in \Theta_0$ is simple if and only if $\Theta_0 = \{\theta_0\}$ is a singleton set containing a single fully specified point in $\Theta$. For example, in an independent and identically distributed Gaussian model $X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2)$ where the variance $\sigma^2 = \sigma_0^2$ is known, the assertion $H_0 : \mu = 0$ is a simple hypothesis because the joint density on $\mathbb{R}^n$ is uniquely determined.
2. **Composite Hypothesis**: A statistical hypothesis is termed **composite** if the corresponding parameter subset contains more than one element, so that the exact probability distribution of the sample remains incompletely specified even when the hypothesis holds true. Composite hypotheses arise in two principal ways: either the parameter of interest ranges over an interval—such as a **one-sided alternative** $H_1 : \theta > \theta_0$ or a **two-sided alternative** $H_1 : \theta \neq \theta_0$—or the model contains unspecified **nuisance parameters**. For instance, in a normal population $\mathcal{N}(\mu, \sigma^2)$ where both $\mu \in \mathbb{R}$ and $\sigma^2 > 0$ are unknown, the hypothesis $H_0 : \mu = 0$ is composite because the null subspace $\Theta_0 = \{(0, \sigma^2) : \sigma^2 > 0\}$ is a one-dimensional half-line rather than a single point.

### Non-Randomized Tests and Sample Space Partitions

In its classical deterministic formulation, a statistical hypothesis test is a measurable rule that partitions the sample space $\mathcal{X}$ into two disjoint Borel sets: the **acceptance region** (or non-rejection region) $\mathcal{C}^c \in \mathcal{A}$ and the **critical region** (or rejection region) $\mathcal{C} \in \mathcal{A}$, satisfying $\mathcal{X} = \mathcal{C} \cup \mathcal{C}^c$ and $\mathcal{C} \cap \mathcal{C}^c = \emptyset$. When the experiment yields a sample realization $\mathbf{x} \in \mathcal{X}$, the investigator applies the binary decision rule:
- If $\mathbf{x} \in \mathcal{C}$, the null hypothesis $H_0$ is **rejected** in favor of the alternative $H_1$.
- If $\mathbf{x} \in \mathcal{C}^c$, the investigator **fails to reject** the null hypothesis $H_0$.

In practice, the critical region $\mathcal{C}$ is almost always defined through a scalar or vector-valued **test statistic** $T : \mathcal{X} \to \mathbb{R}^m$, which compresses the $n$-dimensional sample vector $\mathbf{X}$ into a summary measure of departure from the null hypothesis, such that $\mathcal{C} = \{\mathbf{x} \in \mathcal{X} : T(\mathbf{x}) \in R\}$ for a rejection region $R \subseteq \mathbb{R}^m$.

In scientific epistemology and Popperian falsificationism, the expressions "accepting $H_0$" and "failing to reject $H_0$" carry distinct interpretations. While Abraham Wald's decision-theoretic framework treats hypothesis testing as a two-action decision space $\mathcal{D} = \{d_0, d_1\}$ where $d_0$ denotes acting as though $H_0$ is true and $d_1$ denotes acting as though $H_1$ is true, empirical data of finite sample size can rarely prove the exact validity of a point null hypothesis $\theta = \theta_0$ against arbitrary infinitesimal perturbations $\theta = \theta_0 + \varepsilon$. Consequently, falling inside $\mathcal{C}^c$ signifies that the empirical evidence is insufficient to refute $H_0$ beyond the prescribed threshold of reasonable doubt, rather than establishing that $H_0$ is literally true with certainty.

## 1.2 Randomized Decision Functions, Asymmetric Errors, and the Neyman-Pearson Paradigm

To construct a unified mathematical theory of hypothesis testing that encompasses both continuous and discrete probability distributions and permits the application of functional analysis and convex optimization, Jerzy Neyman and Egon Pearson replaced the rigid indicator set $\mathcal{C}$ with the more general concept of a **randomized test function**.

A **test function** (or critical function) is a Borel-measurable mapping $\phi : \mathcal{X} \to [0, 1]$ that assigns to every possible sample realization $\mathbf{x} \in \mathcal{X}$ a conditional probability $\phi(\mathbf{x})$ of rejecting the null hypothesis $H_0$ given that $\mathbf{X} = \mathbf{x}$ has been observed. Once the data vector $\mathbf{x}$ is recorded, the investigator performs an auxiliary independent Bernoulli trial—generating a uniform random variable $U \sim \text{Uniform}(0, 1)$—and rejects $H_0$ if $U \le \phi(\mathbf{x})$, while failing to reject $H_0$ if $U > \phi(\mathbf{x})$.
- A **non-randomized test** is the special case in which the test function takes values exclusively in the binary set $\{0, 1\}$. In that setting, $\phi(\mathbf{x}) = \mathbf{1}_{\mathcal{C}}(\mathbf{x})$ is simply the indicator function of the critical region $\mathcal{C} = \{\mathbf{x} \in \mathcal{X} : \phi(\mathbf{x}) = 1\}$.
- A **randomized test** takes fractional values $0 < \phi(\mathbf{x}) < 1$ on a boundary subset of the sample space (typically where a discrete test statistic equals a critical threshold). The space of all measurable test functions $\Phi = \{\phi : \mathcal{X} \to [0, 1]\}$ forms a convex, weak-star compact subset of $L^\infty(\mathcal{X}, \mathcal{A}, \mu)$, which guarantees the mathematical existence of optimal tests across arbitrary probability spaces.

### Type I and Type II Errors and Asymmetric Loss Structure

Because the sample $\mathbf{X}$ exhibits random variability, any decision rule $\phi$ is susceptible to two fundamentally distinct modes of inferential error depending on the true, unobserved location of the parameter $\theta$:
1. **Type I Error (False Positive / False Discovery)**: Rejecting the null hypothesis $H_0$ when the true parameter actually resides in the null subspace ($\theta \in \Theta_0$). For a given parameter point $\theta \in \Theta_0$, the probability of committing a Type I error is the expected value of the test function under $P_\theta$:
   $$\alpha(\theta) = \mathbb{P}_\theta(\text{Reject } H_0) = \mathbb{E}_\theta[\phi(\mathbf{X})] = \int_{\mathcal{X}} \phi(\mathbf{x}) \, dP_\theta(\mathbf{x}), \quad \theta \in \Theta_0$$
2. **Type II Error (False Negative / Missed Detection)**: Failing to reject the null hypothesis $H_0$ when the true parameter actually resides in the alternative subspace ($\theta \in \Theta_1$). For a given parameter point $\theta \in \Theta_1$, the probability of committing a Type II error is:
   $$\tilde{\beta}(\theta) = \mathbb{P}_\theta(\text{Fail to Reject } H_0) = \mathbb{E}_\theta[1 - \phi(\mathbf{X})] = 1 - \mathbb{E}_\theta[\phi(\mathbf{X})], \quad \theta \in \Theta_1$$

<div class="table-wrapper"><table class="data-table"><thead><tr><th>True State of Nature</th><th>Decision: Fail to Reject H0 (d0)</th><th>Decision: Reject H0 (d1)</th></tr></thead><tbody><tr><td><strong>Null Hypothesis True (theta in Theta0)</strong></td><td>Correct Retention (Probability 1 - alpha(theta))</td><td><strong>Type I Error</strong> (False Positive, Probability alpha(theta))</td></tr><tr><td><strong>Alternative True (theta in Theta1)</strong></td><td><strong>Type II Error</strong> (False Negative, Probability 1 - beta(theta))</td><td>Correct Detection / Power (Probability beta(theta))</td></tr></tbody></table></div>

In a decision-theoretic framework with loss function $L(\theta, d)$, where $L(\theta, d_0) = 0$ for $\theta \in \Theta_0$ and $L(\theta, d_1) = c_{\text{I}} > 0$ for $\theta \in \Theta_0$, while $L(\theta, d_1) = 0$ for $\theta \in \Theta_1$ and $L(\theta, d_0) = c_{\text{II}} > 0$ for $\theta \in \Theta_1$, the risk function $R(\theta, \phi) = \mathbb{E}_\theta[L(\theta, \phi(\mathbf{X}))]$ reduces directly to $c_{\text{I}} \alpha(\theta)$ on $\Theta_0$ and $c_{\text{II}} \tilde{\beta}(\theta)$ on $\Theta_1$.

Ideally, an investigator would seek a test function $\phi$ that simultaneously drives both $\alpha(\theta)$ and $\tilde{\beta}(\theta)$ to zero for a fixed sample size $n$. However, for any non-trivial statistical model where the measures $P_{\theta_0}$ and $P_{\theta_1}$ are mutually absolutely continuous (or share overlapping support), these two error probabilities stand in strict mathematical opposition. Shrinking the critical region $\mathcal{C}$ to reduce the probability of a Type I error inevitably enlarges the acceptance region $\mathcal{C}^c$, thereby inflating the probability of a Type II error. Conversely, expanding $\mathcal{C}$ to capture more alternative realizations increases the false positive rate under $H_0$. Only by increasing the total Fisher information through a larger sample size $n$ can both error rates be reduced simultaneously.

To resolve this fundamental trade-off for a fixed sample size $n$, the **Neyman-Pearson paradigm** introduces an asymmetric optimization hierarchy:
- The null hypothesis $H_0$ is designated as the conservative baseline status quo (analogous to the presumption of innocence in jurisprudence or the absence of therapeutic efficacy in a clinical trial) whose false rejection carries severe scientific or regulatory consequences.
- We first impose a strict, predetermined upper bound $\alpha \in (0, 1)$—called the **level of significance**—on the permissible probability of a Type I error across the entire null parameter space:
  $$\sup_{\theta \in \Theta_0} \mathbb{E}_\theta[\phi(\mathbf{X})] \le \alpha$$
- Subject to this hard constraint on Type I error, we then search within the feasible class of level-$\alpha$ tests for a rule $\phi^*$ that minimizes the Type II error probability $\tilde{\beta}(\theta)$ (or equivalently maximizes detection probability) across $\theta \in \Theta_1$.

## 1.3 The Power Function, Test Size, Significance Level, and Operating Characteristic Curves

The complete frequentist performance of any statistical test $\phi : \mathcal{X} \to [0, 1]$ across the entire parameter space $\Theta = \Theta_0 \cup \Theta_1$ is encapsulated by a single analytical mapping known as the **power function**.

### Definition of the Power Function and Operating Characteristic Curve

For any test function $\phi(\mathbf{X})$, the **power function** $\beta_\phi : \Theta \to [0, 1]$ (often written simply as $\beta(\theta)$ when $\phi$ is clear from context) is defined for every $\theta \in \Theta$ as the expected value of $\phi(\mathbf{X})$ under the probability measure $P_\theta$:

$$\beta(\theta) = \mathbb{E}_\theta[\phi(\mathbf{X})] = \int_{\mathcal{X}} \phi(\mathbf{x}) f(\mathbf{x}; \theta) \, d\mu(\mathbf{x}) \quad \forall \theta \in \Theta$$

When $\phi(\mathbf{x}) = \mathbf{1}_{\mathcal{C}}(\mathbf{x})$ is a non-randomized test with critical region $\mathcal{C}$, the power function reduces to the exact probability that the sample falls inside the rejection region when $\theta$ is the true parameter:

$$\beta(\theta) = \mathbb{P}_\theta(\mathbf{X} \in \mathcal{C}) \quad \forall \theta \in \Theta$$

Note carefully the dual role played by $\beta(\theta)$ across the two partitions of the parameter space:
- When $\theta \in \Theta_0$, $\beta(\theta)$ equals the **Type I error probability** at $\theta$.
- When $\theta \in \Theta_1$, $\beta(\theta)$ equals the **power** of the test against the specific alternative $\theta$, which is $1 - \tilde{\beta}(\theta)$, the probability of correctly detecting a false null hypothesis.

In industrial quality control, reliability engineering, and sequential analysis, analysts frequently examine the complement of the power function, known as the **Operating Characteristic (OC) curve**, denoted $L(\theta)$:

$$L(\theta) = 1 - \beta(\theta) = \mathbb{E}_\theta[1 - \phi(\mathbf{X})] = \mathbb{P}_\theta(\text{Fail to Reject } H_0)$$

For an ideal test with infinite information, the power function would coincide with the indicator function of the alternative space, $\beta_{\text{ideal}}(\theta) = \mathbf{1}_{\Theta_1}(\theta)$, vanishing identically on $\Theta_0$ and jumping discontinuously to unity on $\Theta_1$. For finite sample sizes in regular parametric families where $f(\mathbf{x}; \theta)$ varies smoothly with $\theta$, dominated convergence implies that $\beta(\theta)$ is a continuous—and frequently real-analytic—function of $\theta$. Because a continuous function cannot jump instantaneously from $0$ to $1$ at the boundary separating $\Theta_0$ and $\Theta_1$, any finite-sample test has power close to $\alpha$ for alternative parameter values $\theta \in \Theta_1$ located in the immediate topological neighborhood of $\Theta_0$.

### Exact Distinction Between Test Size and Significance Level

A crucial theoretical distinction separates the **size** of a test from its **level of significance**:
1. **Level of Significance ($\alpha$)**: A test $\phi$ is said to have **significance level** $\alpha \in [0, 1]$ (or to be a **level-$\alpha$ test**) if its power function never exceeds $\alpha$ anywhere in the null parameter space:
   $$\beta(\theta) \le \alpha \quad \forall \theta \in \Theta_0$$
2. **Size of a Test ($\alpha_{\text{size}}$)**: The **size** of a test $\phi$ is defined as the supremum of the Type I error probability over the entire null parameter space $\Theta_0$:
   $$\text{Size}(\phi) = \sup_{\theta \in \Theta_0} \beta(\theta) = \sup_{\theta \in \Theta_0} \mathbb{E}_\theta[\phi(\mathbf{X})]$$

Every size-$\alpha$ test is automatically a level-$\alpha$ test, and any test of size $\alpha_0 \le \alpha$ is a valid level-$\alpha$ test. However, a level-$\alpha$ test may have a strict inequality $\sup_{\theta \in \Theta_0} \beta(\theta) < \alpha$. This distinction arises constantly in two settings:
- **Discrete Non-Randomized Tests**: If $X \sim \text{Binomial}(n = 10, p)$ and we test $H_0 : p = 0.5$ against $H_1 : p > 0.5$ at target significance level $\alpha = 0.05$ without randomization, the cumulative tail probabilities under $p = 0.5$ are $\mathbb{P}(X \ge 9) = 11/1024 \approx 0.01074$ and $\mathbb{P}(X \ge 8) = 56/1024 \approx 0.05469$. To respect the level constraint $\beta(0.5) \le 0.05$, a non-randomized rule must choose $\mathcal{C} = \{9, 10\}$, yielding a test of **level** $0.05$ whose actual **size** is $0.01074$. Conceding the gap between $0.01074$ and $0.05$ sacrifices substantial statistical power under $H_1$.
- **Composite Null Hypotheses with Monotone Power**: When testing $H_0 : \theta \le \theta_0$ versus $H_1 : \theta > \theta_0$, if the power function $\beta(\theta)$ is monotonically non-decreasing in $\theta$, then for every interior null point $\theta < \theta_0$ we have $\beta(\theta) \le \beta(\theta_0)$. Consequently, the supremum over $\Theta_0 = (-\infty, \theta_0]$ is attained precisely on the topological boundary $\partial \Theta_0 = \{\theta_0\}$:
  $$\sup_{\theta \le \theta_0} \beta(\theta) = \beta(\theta_0)$$
  This boundary reduction allows the investigator to calibrate the critical value exclusively at the boundary distribution $P_{\theta_0}$.

### Consistency and Asymptotic Power Sequences

Let $\{\phi_n\}_{n=1}^\infty$ be a sequence of level-$\alpha$ tests based on samples of increasing size $n$. The test sequence is called **consistent** against the alternative $\Theta_1$ if its power converges to unity at every fixed alternative parameter point as the sample size grows without bound:

$$\lim_{n \to \infty} \beta_{\phi_n}(\theta) = 1 \quad \forall \theta \in \Theta_1$$

Consistency guarantees that for any fixed departure from $H_0$, however small, a sufficiently large sample will detect the departure with probability approaching certainty.

## 1.4 Duality Between Hypothesis Tests and Confidence Regions: The Inversion Theorem

One of the deepest structural results in mathematical statistics is the exact mathematical equivalence—or **duality**—between the theory of hypothesis testing and the theory of confidence set estimation. Every family of hypothesis tests generates a confidence region, and every confidence region defines a family of hypothesis tests, with optimality properties translating directly across the two domains.

### Theorem 1.1: The Test-Confidence Set Inversion Duality

Let $(\mathcal{X}, \mathcal{A}, \{P_\theta : \theta \in \Theta\})$ be a statistical model.
1. **From Tests to Confidence Sets**: Suppose that for every possible parameter point $\theta_0 \in \Theta$, we have a non-randomized level-$\alpha$ test for the point null hypothesis $H_0(\theta_0) : \theta = \theta_0$ with acceptance region $A(\theta_0) \subseteq \mathcal{X}$ and critical region $\mathcal{C}(\theta_0) = \mathcal{X} \setminus A(\theta_0)$, satisfying:
   $$\mathbb{P}_{\theta_0}\left(\mathbf{X} \in A(\theta_0)\right) \ge 1 - \alpha \quad \forall \theta_0 \in \Theta$$
   For each observed sample vector $\mathbf{x} \in \mathcal{X}$, define the subset $S(\mathbf{x}) \subseteq \Theta$ as the collection of all parameter values $\theta_0$ that are **not rejected** when $\mathbf{X} = \mathbf{x}$ is observed:
   $$S(\mathbf{x}) = \{\theta_0 \in \Theta : \mathbf{x} \in A(\theta_0)\}$$
   Then the random set $S(\mathbf{X})$ is a valid $(1 - \alpha)$ **confidence set** for $\theta$, satisfying:
   $$\mathbb{P}_\theta\left(\theta \in S(\mathbf{X})\right) \ge 1 - \alpha \quad \forall \theta \in \Theta$$
2. **From Confidence Sets to Tests**: Conversely, suppose $S(\mathbf{X}) \subseteq \Theta$ is a $(1 - \alpha)$ confidence set for $\theta$ satisfying $\mathbb{P}_\theta(\theta \in S(\mathbf{X})) \ge 1 - \alpha$ for all $\theta \in \Theta$. For each $\theta_0 \in \Theta$, define the acceptance region:
   $$A(\theta_0) = \{\mathbf{x} \in \mathcal{X} : \theta_0 \in S(\mathbf{x})\}$$
   Then the decision rule that rejects $H_0 : \theta = \theta_0$ if and only if $\mathbf{X} \notin A(\theta_0)$ (equivalently, if and only if $\theta_0 \notin S(\mathbf{X})$) is a valid level-$\alpha$ test of $H_0 : \theta = \theta_0$.

#### Formal Set-Theoretic Proof:
The proof rests on the fundamental equivalence of set membership across the Cartesian product space $\mathcal{X} \times \Theta$. Consider the subset $M \subseteq \mathcal{X} \times \Theta$ defined by:

$$M = \{(\mathbf{x}, \theta) \in \mathcal{X} \times \Theta : \mathbf{x} \in A(\theta)\} = \{(\mathbf{x}, \theta) \in \mathcal{X} \times \Theta : \theta \in S(\mathbf{x})\}$$

For a fixed parameter $\theta \in \Theta$, the horizontal slice of $M$ is the acceptance region $A(\theta) \subseteq \mathcal{X}$. For a fixed sample realization $\mathbf{x} \in \mathcal{X}$, the vertical slice of $M$ is the confidence set $S(\mathbf{x}) \subseteq \Theta$. Therefore, for every pair $(\mathbf{x}, \theta) \in \mathcal{X} \times \Theta$, the logical equivalence holds identically:

$$\theta \in S(\mathbf{x}) \iff \mathbf{x} \in A(\theta)$$

Replacing the deterministic point $\mathbf{x}$ with the random sample vector $\mathbf{X} \sim P_\theta$, the two events $\{\theta \in S(\mathbf{X})\}$ and $\{\mathbf{X} \in A(\theta)\}$ are identical subsets of the underlying probability space! Consequently, for every $\theta \in \Theta$:

$$\mathbb{P}_\theta\left(\theta \in S(\mathbf{X})\right) = \mathbb{P}_\theta\left(\mathbf{X} \in A(\theta)\right) = 1 - \mathbb{P}_\theta\left(\mathbf{X} \in \mathcal{C}(\theta)\right) = 1 - \beta_{\theta}(\theta)$$

Since each test $H_0(\theta) : \vartheta = \theta$ has level $\alpha$, its Type I error satisfies $\beta_\theta(\theta) \le \alpha$, which immediately implies $\mathbb{P}_\theta(\theta \in S(\mathbf{X})) \ge 1 - \alpha$. If every test has exact size $\alpha$ so that $\mathbb{P}_\theta(\mathbf{X} \in A(\theta)) = 1 - \alpha$, then $S(\mathbf{X})$ has exact coverage probability $1 - \alpha$ everywhere in $\Theta$.

### Uniformly Most Accurate (UMA) Confidence Bounds

The duality theorem extends beyond coverage probability to optimality criteria. How do we measure the accuracy of a confidence set $S(\mathbf{X})$? If $\theta$ is the true parameter and $\theta' \neq \theta$ is any false parameter value, an erroneous inclusion occurs whenever the confidence set $S(\mathbf{X})$ covers the false value $\theta'$. Using the fundamental equivalence $\theta' \in S(\mathbf{X}) \iff \mathbf{X} \in A(\theta')$, the probability of covering a false parameter value $\theta'$ when $\theta$ is true is:

$$\mathbb{P}_\theta\left(\theta' \in S(\mathbf{X})\right) = \mathbb{P}_\theta\left(\mathbf{X} \in A(\theta')\right) = 1 - \mathbb{P}_\theta\left(\mathbf{X} \in \mathcal{C}(\theta')\right) = 1 - \beta_{\theta'}(\theta)$$

Notice what this equation reveals: **minimizing the probability that the confidence set $S(\mathbf{X})$ covers a false value $\theta'$ under the true parameter $\theta$ is mathematically identical to maximizing the power $\beta_{\theta'}(\theta)$ of the size-$\alpha$ test for $H_0 : \vartheta = \theta'$ against the alternative $H_1 : \vartheta = \theta$!**

A $(1 - \alpha)$ confidence set $S^*(\mathbf{X})$ is defined to be **Uniformly Most Accurate (UMA)** if for every true parameter $\theta$ and false parameter $\theta'$, $\mathbb{P}_\theta(\theta' \in S^*(\mathbf{X}))$ is minimized among all $(1 - \alpha)$ confidence sets. By Theorem 1.1:
- Inverting a family of Uniformly Most Powerful (UMP) one-sided tests for $H_0 : \theta = \theta_0$ against $H_1 : \theta > \theta_0$ yields a **Uniformly Most Accurate (UMA) lower confidence bound** $[\underline{\theta}(\mathbf{X}), \infty)$ that minimizes $\mathbb{P}_\theta(\underline{\theta}(\mathbf{X}) \le \theta')$ for all $\theta' < \theta$.
- Inverting a family of Uniformly Most Powerful Unbiased (UMPU) two-sided tests yields a **Uniformly Most Accurate Unbiased (UMAU) confidence interval** $[\underline{\theta}(\mathbf{X}), \overline{\theta}(\mathbf{X})]$.

## 1.5 Mathematical Theory of P-Values: Probability Integral Transform and Stochastic Dominance

While a fixed-level Neyman-Pearson test reports only a binary decision at a pre-selected significance threshold $\alpha$, scientific reporting requires quantifying the exact strength of the empirical evidence against $H_0$. This role is fulfilled by the **p-value** (or observed significance level).

### Formal Measure-Theoretic Definition of a Valid P-Value

Suppose we have a nested family of critical regions $\{\mathcal{C}_\alpha : \alpha \in (0, 1)\}$ for testing $H_0 : \theta \in \Theta_0$, where each $\mathcal{C}_\alpha$ is a valid level-$\alpha$ rejection region ($\sup_{\theta \in \Theta_0} \mathbb{P}_\theta(\mathbf{X} \in \mathcal{C}_\alpha) \le \alpha$) and the regions are monotonically nested so that $\mathcal{C}_\alpha \subseteq \mathcal{C}_{\alpha'}$ whenever $\alpha < \alpha'$. The **p-value** $p(\mathbf{X})$ is defined as the infimum of all significance levels $\alpha$ at which the observed data $\mathbf{X}$ would lead to rejection of $H_0$:

$$p(\mathbf{x}) = \inf\left\{\alpha \in (0, 1) : \mathbf{x} \in \mathcal{C}_\alpha\right\}$$

More generally, a measurable statistic $P(\mathbf{X}) : \mathcal{X} \to [0, 1]$ is defined to be a **valid p-value** for the null hypothesis $H_0 : \theta \in \Theta_0$ if for every $\theta \in \Theta_0$ and every threshold $u \in [0, 1]$:

$$\mathbb{P}_\theta\left(P(\mathbf{X}) \le u\right) \le u \quad \forall \theta \in \Theta_0, \quad \forall u \in [0, 1]$$

If equality holds for some $\theta_0 \in \Theta_0$ across all $u \in [0, 1]$, then $P(\mathbf{X}) \sim \text{Uniform}(0, 1)$ under $P_{\theta_0}$, and the p-value is said to be **exact**. If $\mathbb{P}_\theta(P(\mathbf{X}) \le u) \le u$ with strict inequality for some $u$, the p-value is **conservative** (stochastically larger than a standard uniform random variable under $H_0$).

### Theorem 1.2: Uniform Null Distribution of Continuous P-Values

Let $T(\mathbf{X})$ be a real-valued test statistic such that large values of $T(\mathbf{X})$ provide evidence against a simple null hypothesis $H_0 : \theta = \theta_0$ in favor of $H_1 : \theta \in \Theta_1$. Suppose the cumulative distribution function of $T(\mathbf{X})$ under $H_0$, denoted $F_0(t) = \mathbb{P}_{\theta_0}(T(\mathbf{X}) \le t)$, is continuous on $\mathbb{R}$, and define the upper-tail survival function $S_0(t) = 1 - F_0(t) = \mathbb{P}_{\theta_0}(T(\mathbf{X}) \ge t)$. Then the p-value statistic defined by:

$$P(\mathbf{X}) = S_0(T(\mathbf{X})) = 1 - F_0(T(\mathbf{X})) = \mathbb{P}_{\theta_0}\left(T(\mathbf{X}^*) \ge T(\mathbf{X}) \;\middle|\; \mathbf{X}\right)$$

where $\mathbf{X}^* \sim P_{\theta_0}$ is an independent copy of the sample under $H_0$, follows an exact continuous uniform distribution on $[0, 1]$ when $H_0$ is true:

$$P(\mathbf{X}) \sim \text{Uniform}(0, 1) \quad \text{under } H_0$$

#### Proof via the Probability Integral Transform:
Let $F_0^{-1}(q) = \inf\{t \in \mathbb{R} : F_0(t) \ge q\}$ denote the generalized quantile function of $F_0$. Because $F_0$ is continuous, $F_0(F_0^{-1}(q)) = q$ for all $q \in (0, 1)$, and for any $t \in \mathbb{R}$ and $q \in (0, 1)$, the inequality $F_0(t) \ge q$ holds if and only if $t \ge F_0^{-1}(q)$. For any $u \in (0, 1)$, evaluate the cumulative distribution function of $P(\mathbf{X}) = 1 - F_0(T(\mathbf{X}))$ under $H_0$:

$$\mathbb{P}_{\theta_0}\left(P(\mathbf{X}) \le u\right) = \mathbb{P}_{\theta_0}\left(1 - F_0(T(\mathbf{X})) \le u\right) = \mathbb{P}_{\theta_0}\left(F_0(T(\mathbf{X})) \ge 1 - u\right)$$

Using the quantile equivalence and the continuity of $T(\mathbf{X})$ under $H_0$:

$$\mathbb{P}_{\theta_0}\left(F_0(T(\mathbf{X})) \ge 1 - u\right) = \mathbb{P}_{\theta_0}\left(T(\mathbf{X}) \ge F_0^{-1}(1 - u)\right) = 1 - F_0\left(F_0^{-1}(1 - u)\right) = 1 - (1 - u) = u$$

Thus $\mathbb{P}_{\theta_0}(P(\mathbf{X}) \le u) = u$ for all $u \in [0, 1]$, proving that $P(\mathbf{X}) \sim \text{Uniform}(0, 1)$ under $H_0$.

### Distribution of P-Values Under the Alternative Hypothesis and Discrete Randomization

What is the probability distribution of the p-value $P(\mathbf{X}) = 1 - F_0(T(\mathbf{X}))$ when the alternative hypothesis $H_1 : \theta = \theta_1$ is true? Let $F_1(t) = \mathbb{P}_{\theta_1}(T(\mathbf{X}) \le t)$ denote the cumulative distribution function of $T(\mathbf{X})$ under the alternative $\theta_1$. Then for any $u \in (0, 1)$, the cumulative distribution function of $P(\mathbf{X})$ under $H_1$ is:

$$G_1(u) = \mathbb{P}_{\theta_1}\left(P(\mathbf{X}) \le u\right) = \mathbb{P}_{\theta_1}\left(T(\mathbf{X}) \ge F_0^{-1}(1 - u)\right) = 1 - F_1\left(F_0^{-1}(1 - u)\right)$$

Notice that $F_0^{-1}(1 - u)$ is the exact critical value $c_u$ of a size-$u$ upper-tail test, so $G_1(u) = \beta_{\theta_1}(u)$ is precisely the **power of the size-$u$ test** against $\theta_1$! Whenever the test is unbiased ($\beta_{\theta_1}(u) > u$), we have $G_1(u) > u$ for all $u \in (0, 1)$, meaning that $P(\mathbf{X})$ under $H_1$ is **stochastically smaller** than $\text{Uniform}(0, 1)$, concentrating probability mass heavily near zero.

When $T(\mathbf{X})$ is a discrete random variable taking values $\{t_1 < t_2 < \dots\}$, the standard tail probability $p_{\text{disc}}(t_k) = \mathbb{P}_{\theta_0}(T \ge t_k)$ only assumes discrete jump values $u_k = \mathbb{P}_{\theta_0}(T \ge t_k)$ and is strictly conservative between jumps. To obtain an exact $\text{Uniform}(0, 1)$ p-value in discrete models, one defines the **randomized p-value**:

$$P_{\text{rand}}(\mathbf{X}, U) = \mathbb{P}_{\theta_0}\left(T(\mathbf{X}^*) > T(\mathbf{X})\right) + U \cdot \mathbb{P}_{\theta_0}\left(T(\mathbf{X}^*) = T(\mathbf{X})\right), \quad U \sim \text{Uniform}(0, 1)$$

And in applied reporting where auxiliary randomization is undesirable, Lancaster's **mid-p-value** replaces the random $U$ with its expectation $\mathbb{E}[U] = 1/2$, yielding $p_{\text{mid}}(t) = \mathbb{P}_{\theta_0}(T > t) + \frac{1}{2} \mathbb{P}_{\theta_0}(T = t)$.

## 1.6 Simultaneous Inference and Multiple Hypothesis Testing: FWER, Bonferroni, Holm, and Benjamini-Hochberg FDR

In contemporary scientific domains such as genomics, neuroimaging, high-energy astrophysics, and quantitative finance, investigators routinely test $m$ statistical hypotheses $H_{0,1}, H_{0,2}, \dots, H_{0,m}$ simultaneously from the same dataset (where $m$ may range from tens to millions). If each individual hypothesis $H_{0,i}$ is tested separately at significance level $\alpha = 0.05$, the probability of committing at least one Type I error across the collection of $m$ tests escalates rapidly. For $m$ mutually independent true null hypotheses, the probability of making at least one false rejection is:

$$\mathbb{P}(\text{At least one false rejection}) = 1 - (1 - \alpha)^m$$

Even for a modest family of $m = 20$ independent true null hypotheses at $\alpha = 0.05$, this probability reaches $1 - (0.95)^{20} \approx 0.6415$ ($64.15\%$), and the expected number of false discoveries is $m\alpha = 1$. Controlling false positives across simultaneous tests requires rigorous multiple testing error metrics.

### Classification of Multiple Testing Outcomes

Suppose $m$ hypotheses are tested simultaneously, of which $m_0$ are truly null (the set $\mathcal{M}_0 \subseteq \{1, \dots, m\}$ with $|\mathcal{M}_0| = m_0$ unknown) and $m_1 = m - m_0$ are truly alternative. Let $R$ denote the total observable number of rejected hypotheses, and let $V$ denote the unobservable number of false rejections (Type I errors):

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Hypothesis Status</th><th>Failed to Reject (m - R)</th><th>Rejected (R)</th><th>Total Hypotheses</th></tr></thead><tbody><tr><td><strong>True Null Hypotheses</strong></td><td>U (True Negatives)</td><td><strong>V (False Positives / Type I)</strong></td><td>m0 (Unknown)</td></tr><tr><td><strong>True Alternative Hypotheses</strong></td><td><strong>T (False Negatives / Type II)</strong></td><td>S (True Discoveries)</td><td>m1 = m - m0</td></tr><tr><td><strong>Total Decisions</strong></td><td>m - R</td><td>R (Observable Rejections)</td><td>m (Known Total)</td></tr></tbody></table></div>

### Family-Wise Error Rate (FWER): Bonferroni and Holm Step-Down Procedures

The **Family-Wise Error Rate (FWER)** is defined as the probability of committing one or more false rejections across the entire family of $m$ tests:

$$\text{FWER} = \mathbb{P}(V \ge 1)$$

A multiple testing procedure controls FWER in the **weak sense** if $\mathbb{P}(V \ge 1) \le \alpha$ only under the complete null configuration $m_0 = m$, and controls FWER in the **strong sense** if $\mathbb{P}(V \ge 1) \le \alpha$ for *every* possible subset of true nulls $\mathcal{M}_0 \subseteq \{1, \dots, m\}$.
1. **The Bonferroni Procedure**: Reject $H_{0,i}$ if its p-value satisfies $P_i \le \alpha / m$. To prove strong FWER control under **arbitrary dependence** among the p-values, apply Boole's union bound over the set of true null hypotheses $\mathcal{M}_0$:
   $$\text{FWER} = \mathbb{P}\left(\bigcup_{i \in \mathcal{M}_0} \left\{P_i \le \frac{\alpha}{m}\right\}\right) \le \sum_{i \in \mathcal{M}_0} \mathbb{P}\left(P_i \le \frac{\alpha}{m}\right) \le \sum_{i \in \mathcal{M}_0} \frac{\alpha}{m} = \frac{m_0}{m} \alpha \le \alpha$$
2. **Holm's Step-Down Procedure (1979)**: Because Bonferroni divides by $m$ even when many hypotheses are clearly false ($m_0 < m$), Sture Holm developed a uniformly more powerful step-down method that still guarantees strong FWER control under arbitrary dependence. Order the observed p-values from smallest to largest: $P_{(1)} \le P_{(2)} \le \dots \le P_{(m)}$, with associated hypotheses $H_{0,(1)}, \dots, H_{0,(m)}$. For each step $k = 1, 2, \dots, m$, compare $P_{(k)}$ against the threshold $\frac{\alpha}{m - k + 1}$. Let $k^*$ be the smallest index such that $P_{(k^*)} > \frac{\alpha}{m - k^* + 1}$. Reject all hypotheses $H_{0,(1)}, \dots, H_{0,(k^*-1)}$ and fail to reject $H_{0,(k^*)}, \dots, H_{0,(m)}$.
   - *Proof of Strong FWER Control*: Suppose $V \ge 1$, and let $j$ be the smallest ordered index among all rejected hypotheses that actually belongs to the true null set $\mathcal{M}_0$. Since at most $m - m_0$ false nulls could have preceded $j$ in the ordering, the rank $j$ must satisfy $j \le m - m_0 + 1$, which implies $m - j + 1 \ge m_0$. Because $H_{0,(j)}$ was rejected, we must have $P_{(j)} \le \frac{\alpha}{m - j + 1} \le \frac{\alpha}{m_0}$. Thus the event $\{V \ge 1\}$ implies that at least one true null hypothesis $i \in \mathcal{M}_0$ has $P_i \le \alpha / m_0$. By Boole's inequality, $\mathbb{P}(V \ge 1) \le \sum_{i \in \mathcal{M}_0} \mathbb{P}(P_i \le \alpha / m_0) \le m_0 (\alpha / m_0) = \alpha$.

### False Discovery Rate (FDR) and the Benjamini-Hochberg Step-Up Procedure

When $m$ is in the thousands, guarding against even a single false rejection via FWER destroys statistical power. Yoav Benjamini and Yosef Hochberg (1995) revolutionized large-scale inference by introducing the **False Discovery Rate (FDR)**, defined as the expected proportion of false discoveries among all rejected hypotheses (defining $V / R = 0$ when $R = 0$):

$$\text{FDR} = \mathbb{E}\left[\frac{V}{\max(R, 1)}\right] = \mathbb{E}\left[\frac{V}{R} \,\mathbf{1}_{\{R > 0\}}\right]$$

In the **Benjamini-Hochberg (BH) Step-Up Procedure** at target FDR level $q \in (0, 1)$, we order the p-values $P_{(1)} \le P_{(2)} \le \dots \le P_{(m)}$ and find the **largest** index $\hat{k}$ satisfying:

$$\hat{k} = \max\left\{k \in \{1, \dots, m\} : P_{(k)} \le \frac{k}{m} q\right\}$$

If such a $\hat{k}$ exists, we reject all hypotheses $H_{0,(1)}, H_{0,(2)}, \dots, H_{0,(\hat{k})}$; otherwise we reject none. Benjamini and Hochberg proved that when the test statistics corresponding to the true null hypotheses $\mathcal{M}_0$ are mutually independent (or satisfy positive regression dependence on a subset, PRDS), the BH procedure satisfies the exact mathematical identity (for continuous uniform null p-values):

$$\text{FDR} = \frac{m_0}{m} q \le q$$

Because the BH threshold $\frac{k}{m} q$ scales linearly with the rank $k$ rather than remaining fixed at $\alpha / m$, it achieves dramatically higher statistical power in high-dimensional screening studies while rigorously bounding the expected fraction of false leads.

## Fully worked question 1: Exact Power Function, Randomized Level-Alpha Construction, and Sample Size Calibration for Discrete Poisson Counts

### Question
An astrophysics detector records the number of neutrino arrival events $X_1, X_2, \dots, X_n$ over $n = 5$ independent observation intervals, where each $X_i \overset{\text{iid}}{\sim} \text{Poisson}(\lambda)$. We wish to test the background rate hypothesis $H_0 : \lambda \le 0.4$ against the burst alternative $H_1 : \lambda > 0.4$ at exact significance level $\alpha = 0.05$ using the sufficient statistic $T = \sum_{i=1}^n X_i$.

1. Derive the exact sampling distribution of $T$ under arbitrary $\lambda > 0$ and prove that the power function $\beta(\lambda)$ of any upper-tail test based on $T$ is strictly increasing in $\lambda$, confirming that the test size is governed by the boundary parameter $\lambda_0 = 0.4$.
2. Determine the non-randomized critical region $\mathcal{C}_{\text{non-rand}} = \{T \ge k\}$, calculate its actual test size, and construct the exact randomized test function $\phi(t)$ that achieves $\text{Size}(\phi) = \beta(0.4) = 0.05$ with four-decimal precision.
3. Evaluate and compare the exact statistical power of the non-randomized test versus the randomized test at the alternative rate $\lambda_1 = 1.0$.

### Solution, step 1: Sufficient statistic distribution and monotonicity of the power function
By the reproductive property of independent Poisson random variables, the sum of $n = 5$ independent $\text{Poisson}(\lambda)$ variables follows a Poisson distribution with rate parameter $\mu = n\lambda = 5\lambda$:

$$T = \sum_{i=1}^5 X_i \sim \text{Poisson}(5\lambda), \quad \mathbb{P}_\lambda(T = t) = \frac{e^{-5\lambda} (5\lambda)^t}{t!}, \quad t = 0, 1, 2, \dots$$

For any upper-tail randomized test rejecting $H_0$ when $T > c$ and rejecting with probability $\gamma \in [0, 1)$ when $T = c$, the power function is:

$$\beta(\lambda) = \sum_{t=c+1}^\infty \frac{e^{-5\lambda} (5\lambda)^t}{t!} + \gamma \frac{e^{-5\lambda} (5\lambda)^c}{c!}$$

Recall the exact analytical identity linking the cumulative Poisson tail to the incomplete Gamma integral:

$$\sum_{t=k}^\infty \frac{e^{-\mu} \mu^t}{t!} = \int_0^\mu \frac{u^{k-1} e^{-u}}{(k-1)!} \, du$$

Differentiating $\beta(\lambda)$ with respect to $\lambda$ via the chain rule ($\mu = 5\lambda$, $d\mu/d\lambda = 5$) yields:

$$\frac{d\beta(\lambda)}{d\lambda} = 5 \left[ \frac{(5\lambda)^c e^{-5\lambda}}{c!} + \gamma e^{-5\lambda} \left( \frac{c(5\lambda)^{c-1}}{c!} - \frac{(5\lambda)^c}{c!} \right) \right] = 5 e^{-5\lambda} \left[ (1 - \gamma) \frac{(5\lambda)^c}{c!} + \gamma \frac{(5\lambda)^{c-1}}{(c-1)!} \right] > 0$$

Since $d\beta(\lambda)/d\lambda > 0$ for all $\lambda > 0$, $\beta(\lambda)$ is strictly increasing on $(0, \infty)$. Consequently, the supremum of Type I error over $\Theta_0 = (0, 0.4]$ is attained strictly at the boundary $\lambda_0 = 0.4$:

$$\text{Size}(\phi) = \sup_{\lambda \le 0.4} \beta(\lambda) = \beta(0.4)$$

### Solution, step 2: Non-randomized size and randomized test construction at lambda_0 = 0.4
Under the boundary parameter $\lambda_0 = 0.4$, the null mean of $T$ is $\mu_0 = 5(0.4) = 2.0$, so $T \sim \text{Poisson}(2)$. Let us compute the exact point probabilities $\mathbb{P}_0(T = t) = e^{-2} 2^t / t!$ and upper-tail probabilities $\mathbb{P}_0(T \ge k)$:
- $t = 0$: $\mathbb{P}_0(T = 0) = e^{-2} \approx 0.135335$
- $t = 1$: $\mathbb{P}_0(T = 1) = 2 e^{-2} \approx 0.270671$
- $t = 2$: $\mathbb{P}_0(T = 2) = 2 e^{-2} \approx 0.270671$
- $t = 3$: $\mathbb{P}_0(T = 3) = \frac{8}{6} e^{-2} = \frac{4}{3} e^{-2} \approx 0.180447$
- $t = 4$: $\mathbb{P}_0(T = 4) = \frac{16}{24} e^{-2} = \frac{2}{3} e^{-2} \approx 0.090224$
- $t = 5$: $\mathbb{P}_0(T = 5) = \frac{32}{120} e^{-2} = \frac{4}{15} e^{-2} \approx 0.036089$

Summing the cumulative probabilities from $0$ to $4$ gives $\mathbb{P}_0(T \le 4) = \left(1 + 2 + 2 + \frac{4}{3} + \frac{2}{3}\right) e^{-2} = 7 e^{-2} \approx 0.947347$. Therefore:

$$\mathbb{P}_0(T \ge 5) = 1 - 7 e^{-2} \approx 0.052653 > 0.05$$

$$\mathbb{P}_0(T \ge 6) = 1 - \left(7 + \frac{4}{15}\right) e^{-2} = 1 - \frac{109}{15} e^{-2} \approx 0.016564 < 0.05$$

Because $\mathbb{P}_0(T \ge 5) = 0.052653$ exceeds the level constraint $\alpha = 0.05$, the **non-randomized level-$0.05$ test** must use the critical region $\mathcal{C}_{\text{non-rand}} = \{T \ge 6\}$, which has actual test size $\alpha_{\text{non-rand}} = 0.016564$ ($1.66\%$).

To achieve exact size $\alpha = 0.05$, the **randomized test** $\phi(t)$ rejects with probability $1$ when $t \ge 6$, rejects with probability $\gamma$ when $t = 5$, and equals $0$ when $t \le 4$:

$$\mathbb{E}_{\lambda_0}[\phi(T)] = \mathbb{P}_0(T \ge 6) + \gamma \, \mathbb{P}_0(T = 5) = 0.05$$

Solving for the boundary randomization probability $\gamma$:

$$\gamma = \frac{0.05 - \mathbb{P}_0(T \ge 6)}{\mathbb{P}_0(T = 5)} = \frac{0.05 - 0.0165636}{0.0360894} = \frac{0.0334364}{0.0360894} \approx 0.926488$$

Thus the exact size-$0.05$ randomized test function is:

$$\phi(t) = \begin{cases} 1, & t \ge 6 \\ 0.9265, & t = 5 \\ 0, & t \le 4 \end{cases}$$

### Solution, step 3: Power evaluation and comparison under the alternative lambda_1 = 1.0
Under the alternative rate $\lambda_1 = 1.0$, the sufficient statistic follows $T \sim \text{Poisson}(5(1.0)) = \text{Poisson}(5)$. We compute the cumulative probabilities under $\mu_1 = 5$:

$$\mathbb{P}_1(T \le 4) = e^{-5} \left(1 + 5 + \frac{25}{2} + \frac{125}{6} + \frac{625}{24}\right) = e^{-5} \left(\frac{24 + 120 + 300 + 500 + 625}{24}\right) = \frac{1569}{24} e^{-5} = 65.375 \, e^{-5} \approx 0.440493$$

$$\mathbb{P}_1(T = 5) = e^{-5} \frac{5^5}{5!} = \frac{3125}{120} e^{-5} \approx 0.175467$$

Therefore, the upper-tail probability for the non-randomized test $\{T \ge 6\}$ is:

$$\beta_{\text{non-rand}}(1.0) = \mathbb{P}_1(T \ge 6) = 1 - \mathbb{P}_1(T \le 4) - \mathbb{P}_1(T = 5) = 1 - 0.440493 - 0.175467 = 0.384039 \quad (38.40\%)$$

In contrast, the exact power of the size-$0.05$ randomized test $\phi(T)$ at $\lambda_1 = 1.0$ is:

$$\beta_{\text{rand}}(1.0) = \mathbb{P}_1(T \ge 6) + \gamma \, \mathbb{P}_1(T = 5) = 0.384039 + (0.926488)(0.175467) = 0.384039 + 0.162568 = 0.546607 \quad (54.66\%)$$

Incorporating randomized boundary splitting at $T = 5$ increases detection power at $\lambda_1 = 1.0$ from $38.40\%$ to $54.66\%$, recovering $16.26$ percentage points of power that would otherwise be lost due to lattice discreteness.

## Fully worked question 2: Duality Inversion of a Shifted Exponential Acceptance Region to Derive Exact Confidence Intervals

### Question
Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed random sample from a two-parameter shifted Exponential distribution with unknown location threshold $\theta \in \mathbb{R}$ and known scale parameter $\sigma_0 = 1$, having probability density function:

$$f(x; \theta) = e^{-(x - \theta)} \mathbf{1}_{[\theta, \infty)}(x)$$

We wish to test the point null hypothesis $H_0 : \theta = \theta_0$ against the two-sided alternative $H_1 : \theta \neq \theta_0$ at significance level $\alpha \in (0, 1)$.

1. Prove that the minimum order statistic $X_{(1)} = \min(X_1, \dots, X_n)$ is a sufficient statistic for $\theta$, and derive the exact sampling distribution of the pivotal quantity $W = n(X_{(1)} - \theta)$.
2. Construct a size-$\alpha$ acceptance region $A(\theta_0)$ for $H_0 : \theta = \theta_0$ based on $X_{(1)}$, and prove that restricting impossible parameter values ($\theta_0 > X_{(1)}$) yields a strictly shorter acceptance interval than an equal-tail allocation.
3. Invert the optimal size-$\alpha$ acceptance region $A(\theta_0)$ via Theorem 1.1 to obtain the exact $(1 - \alpha)$ Uniformly Most Accurate (UMA) confidence interval for $\theta$, and evaluate it numerically for $n = 10$, $x_{(1)} = 4.25$, and $\alpha = 0.05$.

### Solution, step 1: Sufficiency of the minimum order statistic and pivotal distribution
The joint probability density function of the sample $\mathbf{X} = (X_1, \dots, X_n)$ is the product of the individual densities:

$$f_n(\mathbf{x}; \theta) = \prod_{i=1}^n \left[ e^{-(x_i - \theta)} \mathbf{1}_{[\theta, \infty)}(x_i) \right] = \exp\left(-\sum_{i=1}^n x_i + n\theta\right) \prod_{i=1}^n \mathbf{1}_{[\theta, \infty)}(x_i)$$

Notice that every observation satisfies $x_i \ge \theta$ for $i = 1, \dots, n$ if and only if the minimum order statistic $x_{(1)} = \min_{1 \le i \le n} x_i$ satisfies $x_{(1)} \ge \theta$. Thus we can factor the joint density as:

$$f_n(\mathbf{x}; \theta) = \underbrace{\left[ e^{n\theta} \mathbf{1}_{[\theta, \infty)}(x_{(1)}) \right]}_{g(x_{(1)}; \theta)} \cdot \underbrace{\exp\left(-\sum_{i=1}^n x_i\right)}_{h(\mathbf{x})}$$

By the Neyman-Fisher Factorization Theorem, $X_{(1)}$ is a sufficient statistic for $\theta$. To find its sampling distribution, compute its survival function for $t \ge \theta$:

$$\mathbb{P}_\theta(X_{(1)} > t) = \mathbb{P}_\theta(X_1 > t, \dots, X_n > t) = \left[ \mathbb{P}_\theta(X_1 > t) \right]^n = \left( e^{-(t - \theta)} \right)^n = e^{-n(t - \theta)}, \quad t \ge \theta$$

Define the pivotal quantity $W = n(X_{(1)} - \theta)$. For any $w \ge 0$:

$$\mathbb{P}_\theta(W > w) = \mathbb{P}_\theta\left(X_{(1)} > \theta + \frac{w}{n}\right) = e^{-n(\theta + w/n - \theta)} = e^{-w}, \quad w \ge 0$$

Thus $W = n(X_{(1)} - \theta) \sim \text{Exponential}(1)$ is an exact pivot whose distribution is completely free of $\theta$.

### Solution, step 2: Optimal size-alpha acceptance region for H0: theta = theta_0
Under $H_0 : \theta = \theta_0$, the statistic $W_0 = n(X_{(1)} - \theta_0) \sim \text{Exponential}(1)$ takes values strictly in $[0, \infty)$. Any interval $[a, b] \subseteq [0, \infty)$ satisfying:

$$\mathbb{P}_{\theta_0}(a \le n(X_{(1)} - \theta_0) \le b) = e^{-a} - e^{-b} = 1 - \alpha$$

defines a valid size-$\alpha$ acceptance region $A(\theta_0) = \{\mathbf{x} : \theta_0 + a/n \le x_{(1)} \le \theta_0 + b/n\}$. The geometric length of this interval in terms of $W_0$ is $L = b - a$. Since $e^{-b} = e^{-a} - (1 - \alpha)$, we have $b = -\ln(e^{-a} - 1 + \alpha)$, so the length is:

$$L(a) = -\ln\left(e^{-a} - 1 + \alpha\right) - a = -\ln\left(1 - (1 - \alpha) e^a\right), \quad 0 \le a \le -\ln(1 - \alpha)$$

Differentiating $L(a)$ with respect to $a$ gives:

$$\frac{dL}{da} = \frac{(1 - \alpha) e^a}{1 - (1 - \alpha) e^a} > 0 \quad \forall a \in [0, -\ln(1 - \alpha))$$

Because $L(a)$ is strictly increasing in $a$, the shortest acceptance region (and sharpest test) is achieved at the boundary $a^* = 0$, which corresponds to $e^{-b^*} = 1 - (1 - \alpha) = \alpha \implies b^* = -\ln(\alpha)$. Setting $a^* = 0$ reflects the physical truth that any observation $X_{(1)} < \theta_0$ has zero probability under $H_0$ and immediately refutes $H_0$ with certainty! Thus the optimal size-$\alpha$ acceptance region is:

$$A(\theta_0) = \left\{ \mathbf{x} \in \mathbb{R}^n : 0 \le n(x_{(1)} - \theta_0) \le -\ln(\alpha) \right\} = \left\{ \mathbf{x} \in \mathbb{R}^n : \theta_0 \le x_{(1)} \le \theta_0 - \frac{\ln(\alpha)}{n} \right\}$$

### Solution, step 3: Inversion to the (1 - alpha) confidence interval and numerical evaluation
Applying the Test-Confidence Set Inversion Duality (Theorem 1.1), the $(1 - \alpha)$ confidence set $S(\mathbf{x})$ consists of all parameter values $\theta_0$ for which $\mathbf{x} \in A(\theta_0)$. We invert the double inequality with respect to $\theta_0$:

$$\theta_0 \le x_{(1)} \le \theta_0 - \frac{\ln(\alpha)}{n} \iff \begin{cases} \theta_0 \le x_{(1)} \\ \theta_0 \ge x_{(1)} + \frac{\ln(\alpha)}{n} \end{cases}$$

Writing $-\ln(\alpha) = \ln(1/\alpha) > 0$, the exact $(1 - \alpha)$ confidence interval for $\theta$ is:

$$S(\mathbf{X}) = \left[ X_{(1)} + \frac{\ln(\alpha)}{n}, \; X_{(1)} \right] = \left[ X_{(1)} - \frac{\ln(1/\alpha)}{n}, \; X_{(1)} \right]$$

For the given numerical data $n = 10$, $x_{(1)} = 4.25$, and $\alpha = 0.05$, we have $\ln(1 / 0.05) = \ln(20) \approx 2.995732$. Substituting these values yields:

$$\underline{\theta} = 4.25 - \frac{2.995732}{10} = 4.25 - 0.299573 = 3.9504, \quad \overline{\theta} = 4.2500$$

Thus the exact $95\%$ UMA confidence interval for the location threshold $\theta$ is $[3.9504, 4.2500]$, with width $0.2996$.

## Fully worked question 3: Multiple Hypothesis Testing Comparison: Bonferroni, Holm Step-Down, and Benjamini-Hochberg FDR Procedures

### Question
A genomics laboratory conducts $m = 8$ simultaneous hypothesis tests examining differential gene expression across candidate biomarkers. The observed two-sided p-values for the eight genes are recorded as follows:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Biomarker Gene</th><th>G1</th><th>G2</th><th>G3</th><th>G4</th><th>G5</th><th>G6</th><th>G7</th><th>G8</th></tr></thead><tbody><tr><td><strong>Observed P-Value</strong></td><td>0.0320</td><td>0.0015</td><td>0.0410</td><td>0.0080</td><td>0.0240</td><td>0.0040</td><td>0.1800</td><td>0.0150</td></tr></tbody></table></div>

1. Sort the p-values in ascending order $P_{(1)} \le P_{(2)} \le \dots \le P_{(8)}$ and determine which biomarkers are declared statistically significant under the **Bonferroni procedure** at Family-Wise Error Rate $\alpha = 0.05$.
2. Apply **Holm's Step-Down procedure** at $\alpha = 0.05$, explicitly tabulating the step-down thresholds $\alpha / (m - k + 1)$ and identifying all rejected hypotheses.
3. Apply the **Benjamini-Hochberg (BH) Step-Up procedure** at False Discovery Rate level $q = 0.05$, explicitly tabulating the step-up thresholds $(k / m) q$, and explain why the three procedures yield different discovery sets.

### Solution, step 1: Ordering the p-values and applying the Bonferroni procedure
First, we arrange the $m = 8$ observed p-values in strictly increasing order from $k = 1$ to $k = 8$:
- $k = 1$: $P_{(1)} = 0.0015$ (Gene G2)
- $k = 2$: $P_{(2)} = 0.0040$ (Gene G6)
- $k = 3$: $P_{(3)} = 0.0080$ (Gene G4)
- $k = 4$: $P_{(4)} = 0.0150$ (Gene G8)
- $k = 5$: $P_{(5)} = 0.0240$ (Gene G5)
- $k = 6$: $P_{(6)} = 0.0320$ (Gene G1)
- $k = 7$: $P_{(7)} = 0.0410$ (Gene G3)
- $k = 8$: $P_{(8)} = 0.1800$ (Gene G7)

Under the **Bonferroni procedure** at target FWER $\alpha = 0.05$, the uniform single-step critical threshold is:

$$\alpha_{\text{Bonf}} = \frac{\alpha}{m} = \frac{0.05}{8} = 0.00625$$

Comparing each ordered p-value against $0.00625$:
- $P_{(1)} = 0.0015 \le 0.00625$ (Reject $H_{0,(1)}$: G2)
- $P_{(2)} = 0.0040 \le 0.00625$ (Reject $H_{0,(2)}$: G6)
- $P_{(3)} = 0.0080 > 0.00625$ (Fail to reject $H_{0,(3)}$: G4, and all subsequent hypotheses)

Thus, the Bonferroni procedure rejects **2 hypotheses**: **G2 and G6**.

### Solution, step 2: Applying Holm's step-down FWER procedure
In **Holm's Step-Down procedure** at $\alpha = 0.05$, we sequentially test $P_{(k)} \le \frac{0.05}{8 - k + 1}$ starting from $k = 1$ and stopping at the first index $k^*$ where the inequality fails:
- $k = 1$: Threshold $\frac{0.05}{8} = 0.00625$. Since $P_{(1)} = 0.0015 \le 0.00625$, reject $H_{0,(1)}$ (G2) and continue.
- $k = 2$: Threshold $\frac{0.05}{7} \approx 0.00714$. Since $P_{(2)} = 0.0040 \le 0.00714$, reject $H_{0,(2)}$ (G6) and continue.
- $k = 3$: Threshold $\frac{0.05}{6} \approx 0.00833$. Since $P_{(3)} = 0.0080 \le 0.00833$, reject $H_{0,(3)}$ (G4) and continue.
- $k = 4$: Threshold $\frac{0.05}{5} = 0.01000$. Since $P_{(4)} = 0.0150 > 0.01000$, the step-down condition fails at $k^* = 4$!

We stop immediately at $k^* = 4$ and fail to reject $H_{0,(4)}, \dots, H_{0,(8)}$. Therefore, Holm's step-down procedure rejects **3 hypotheses**: **G2, G6, and G4**. Notice that Gene G4 ($P_{(3)} = 0.0080$) was missed by Bonferroni ($0.0080 > 0.00625$) but successfully detected by Holm because the prior rejections of G2 and G6 reduced the remaining pool of potential true nulls from $8$ to $6$, raising the valid FWER threshold to $0.05 / 6 = 0.00833$.

### Solution, step 3: Applying the Benjamini-Hochberg step-up FDR procedure and synthesis
In the **Benjamini-Hochberg (BH) Step-Up procedure** at target FDR $q = 0.05$, we compute the linear critical thresholds $c_k = \frac{k}{8}(0.05) = 0.00625 k$ for $k = 1, \dots, 8$ and seek the **largest** index $\hat{k}$ such that $P_{(k)} \le c_k$:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Rank k</th><th>Gene</th><th>Ordered P-Value P(k)</th><th>Bonferroni (0.05/8)</th><th>Holm (0.05/(9-k))</th><th>BH Threshold (0.05k/8)</th><th>BH Condition P(k) &le; ck</th></tr></thead><tbody><tr><td>1</td><td>G2</td><td>0.0015</td><td>0.00625</td><td>0.00625</td><td>0.00625</td><td>Yes (0.0015 &le; 0.00625)</td></tr><tr><td>2</td><td>G6</td><td>0.0040</td><td>0.00625</td><td>0.00714</td><td>0.01250</td><td>Yes (0.0040 &le; 0.01250)</td></tr><tr><td>3</td><td>G4</td><td>0.0080</td><td>0.00625</td><td>0.00833</td><td>0.01875</td><td>Yes (0.0080 &le; 0.01875)</td></tr><tr><td>4</td><td>G8</td><td>0.0150</td><td>0.00625</td><td>0.01000</td><td>0.02500</td><td>Yes (0.0150 &le; 0.02500)</td></tr><tr><td>5</td><td>G5</td><td>0.0240</td><td>0.00625</td><td>0.01250</td><td>0.03125</td><td>Yes (0.0240 &le; 0.03125)</td></tr><tr><td>6</td><td>G1</td><td>0.0320</td><td>0.00625</td><td>0.01667</td><td>0.03750</td><td>Yes (0.0320 &le; 0.03750)</td></tr><tr><td>7</td><td>G3</td><td>0.0410</td><td>0.00625</td><td>0.02500</td><td>0.04375</td><td><strong>Yes (0.0410 &le; 0.04375)</strong></td></tr><tr><td>8</td><td>G7</td><td>0.1800</td><td>0.00625</td><td>0.05000</td><td>0.05000</td><td>No (0.1800 &gt; 0.05000)</td></tr></tbody></table></div>

The largest index satisfying $P_{(k)} \le \frac{k}{8}(0.05)$ is $\hat{k} = 7$ ($P_{(7)} = 0.0410 \le 0.04375$). Consequently, the Benjamini-Hochberg procedure rejects all **7 hypotheses** $H_{0,(1)}$ through $H_{0,(7)}$ (**G2, G6, G4, G8, G5, G1, and G3**), retaining only G7. Because seven of the eight biomarkers show strong collective evidence of differential expression, controlling the expected proportion of false discoveries (FDR $\le 5\%$) rather than the probability of any single false positive (FWER $\le 5\%$) dramatically increases discovery power from $2$ (Bonferroni) or $3$ (Holm) to $7$ biomarkers.
