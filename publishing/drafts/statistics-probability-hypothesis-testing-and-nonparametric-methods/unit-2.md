# Unit 2: Most Powerful Tests, the Neyman-Pearson Fundamental Lemma & Monotone Likelihood Ratio Families

Simple-versus-simple hypothesis testing and the Neyman-Pearson Fundamental Lemma (existence, uniqueness, and sufficiency); randomized Neyman-Pearson tests for discrete distributions (Binomial, Poisson, Hypergeometric) to achieve exact size alpha; strict unbiasedness of Most Powerful (MP) tests; one-parameter exponential families and families with Monotone Likelihood Ratio (MLR); the Karlin-Rubin Theorem for Uniformly Most Powerful (UMP) one-sided tests and non-existence of two-sided UMP tests.

## 2.1 Simple-Versus-Simple Hypothesis Testing and the Neyman-Pearson Fundamental Lemma

The foundational cornerstone of mathematical hypothesis testing is the solution to the **simple-versus-simple testing problem**, first established by Jerzy Neyman and Egon Pearson in their landmark 1933 memoir. Suppose the parameter space $\Theta = \{\theta_0, \theta_1\}$ contains only two distinct candidate states of nature, so that both the null hypothesis $H_0 : \theta = \theta_0$ and the alternative hypothesis $H_1 : \theta = \theta_1$ are completely specified simple hypotheses. Let $P_0 = P_{\theta_0}$ and $P_1 = P_{\theta_1}$ denote the corresponding probability measures on the measurable sample space $(\mathcal{X}, \mathcal{A})$. Because any pair of probability measures is dominated by the $\sigma$-finite sum measure $\mu = P_0 + P_1$ (or by Lebesgue measure in continuous Euclidean models and counting measure in discrete models), Radon-Nikodym densities $f_0(\mathbf{x}) = f(\mathbf{x}; \theta_0)$ and $f_1(\mathbf{x}) = f(\mathbf{x}; \theta_1)$ always exist with respect to $\mu$.

A test function $\phi^* : \mathcal{X} \to [0, 1]$ is defined to be a **Most Powerful (MP) test of size $\alpha$** for testing $H_0 : \theta = \theta_0$ against $H_1 : \theta = \theta_1$ if it satisfies two conditions:
1. **Exact Size Constraint**: $\mathbb{E}_{\theta_0}[\phi^*(\mathbf{X})] = \int_{\mathcal{X}} \phi^*(\mathbf{x}) f_0(\mathbf{x}) \, d\mu(\mathbf{x}) = \alpha$.
2. **Maximal Power (Minimal Type II Error)**: For every competing level-$\alpha$ test function $\phi : \mathcal{X} \to [0, 1]$ satisfying $\mathbb{E}_{\theta_0}[\phi(\mathbf{X})] \le \alpha$, the power under $H_1$ obeys:
   $$\mathbb{E}_{\theta_1}[\phi^*(\mathbf{X})] \ge \mathbb{E}_{\theta_1}[\phi(\mathbf{X})]$$

Intuitively, choosing a critical region of size $\alpha$ is isomorphic to the **continuous knapsack problem** in mathematical economics: we have a "Type I error budget" of total weight $\alpha$ under the null density $f_0(\mathbf{x})$, and we wish to pack sample points $\mathbf{x} \in \mathcal{X}$ into our rejection region so as to maximize the total "return" (power) accumulated under the alternative density $f_1(\mathbf{x})$. The return per unit of Type I error cost at any sample point $\mathbf{x}$ is precisely the **likelihood ratio**:

$$\Lambda(\mathbf{x}) = \frac{f_1(\mathbf{x})}{f_0(\mathbf{x})} = \frac{f(\mathbf{x}; \theta_1)}{f(\mathbf{x}; \theta_0)}$$

Sample realizations with the largest likelihood ratio $\Lambda(\mathbf{x})$ provide the greatest alternative probability per unit of null probability expended, and should therefore be prioritized for inclusion in the rejection region down to a cutoff threshold $k$.

### Theorem 2.1: The Neyman-Pearson Fundamental Lemma (Sufficiency, Existence, and Uniqueness)

Let $P_0$ and $P_1$ be probability measures possessing densities $f_0(\mathbf{x})$ and $f_1(\mathbf{x})$ with respect to a $\sigma$-finite measure $\mu$ on $(\mathcal{X}, \mathcal{A})$.
1. **Sufficiency (Optimality)**: Any test function $\phi^*(\mathbf{x})$ of the likelihood-ratio threshold form:
   $$\phi^*(\mathbf{x}) = \begin{cases} 1, & \text{if } f_1(\mathbf{x}) > k f_0(\mathbf{x}) \\ \gamma(\mathbf{x}), & \text{if } f_1(\mathbf{x}) = k f_0(\mathbf{x}) \\ 0, & \text{if } f_1(\mathbf{x}) < k f_0(\mathbf{x}) \end{cases}$$
   for some non-negative threshold $k \ge 0$ and measurable boundary function $0 \le \gamma(\mathbf{x}) \le 1$, is a **Most Powerful (MP) test** of its size $\alpha = \mathbb{E}_0[\phi^*(\mathbf{X})]$ for testing $H_0 : f = f_0$ against $H_1 : f = f_1$.
2. **Existence**: For every pre-assigned significance level $\alpha \in (0, 1)$, there exist a constant $k \ge 0$ and a constant randomization weight $\gamma \in [0, 1]$ such that the test $\phi^*(\mathbf{x})$ defined above has exact size $\mathbb{E}_0[\phi^*(\mathbf{X})] = \alpha$.
3. **Uniqueness (Necessity)**: If $\phi$ is any Most Powerful test of size $\alpha \in (0, 1]$, then $\phi(\mathbf{x})$ must coincide with $\phi^*(\mathbf{x})$ $\mu$-almost everywhere on the set $\{\mathbf{x} \in \mathcal{X} : f_1(\mathbf{x}) \neq k f_0(\mathbf{x})\}$. Furthermore, if $\alpha < \mathbb{P}_0(f_1(\mathbf{X}) > 0)$, then $k > 0$ and $\mathbb{E}_0[\phi(\mathbf{X})] = \alpha$.

#### Complete Analytical Proof:
**Proof of Sufficiency**: Let $\phi^*(\mathbf{x})$ have the Neyman-Pearson structure above with size $\mathbb{E}_0[\phi^*(\mathbf{X})] = \alpha$, and let $\phi(\mathbf{x})$ be any competing test function satisfying $0 \le \phi(\mathbf{x}) \le 1$ and $\mathbb{E}_0[\phi(\mathbf{X})] \le \alpha$. Consider the pointwise integrand product:

$$\Delta(\mathbf{x}) = \left[\phi^*(\mathbf{x}) - \phi(\mathbf{x})\right] \left[f_1(\mathbf{x}) - k f_0(\mathbf{x})\right]$$

We partition the sample space $\mathcal{X}$ into three disjoint measurable regions according to the sign of $f_1(\mathbf{x}) - k f_0(\mathbf{x})$:
- On $S_+ = \{\mathbf{x} : f_1(\mathbf{x}) > k f_0(\mathbf{x})\}$, we have $\phi^*(\mathbf{x}) = 1$. Since $\phi(\mathbf{x}) \le 1$, the first factor satisfies $\phi^*(\mathbf{x}) - \phi(\mathbf{x}) = 1 - \phi(\mathbf{x}) \ge 0$, while the second factor satisfies $f_1(\mathbf{x}) - k f_0(\mathbf{x}) > 0$. Their product is therefore non-negative: $\Delta(\mathbf{x}) \ge 0$.
- On $S_0 = \{\mathbf{x} : f_1(\mathbf{x}) = k f_0(\mathbf{x})\}$, the second factor vanishes identically ($f_1(\mathbf{x}) - k f_0(\mathbf{x}) = 0$), so $\Delta(\mathbf{x}) = 0$.
- On $S_- = \{\mathbf{x} : f_1(\mathbf{x}) < k f_0(\mathbf{x})\}$, we have $\phi^*(\mathbf{x}) = 0$. Since $\phi(\mathbf{x}) \ge 0$, the first factor satisfies $\phi^*(\mathbf{x}) - \phi(\mathbf{x}) = -\phi(\mathbf{x}) \le 0$, while the second factor is strictly negative ($f_1(\mathbf{x}) - k f_0(\mathbf{x}) < 0$). The product of two non-positive numbers is non-negative: $\Delta(\mathbf{x}) \ge 0$.

Consequently, $\Delta(\mathbf{x}) \ge 0$ holds pointwise for every $\mathbf{x} \in \mathcal{X}$! Integrating $\Delta(\mathbf{x})$ with respect to $\mu$ over $\mathcal{X}$ yields:

$$\int_{\mathcal{X}} \left[\phi^*(\mathbf{x}) - \phi(\mathbf{x})\right] \left[f_1(\mathbf{x}) - k f_0(\mathbf{x})\right] d\mu(\mathbf{x}) \ge 0$$

By linearity of the integral, we separate the terms under $f_1$ and $f_0$:

$$\left(\mathbb{E}_1[\phi^*(\mathbf{X})] - \mathbb{E}_1[\phi(\mathbf{X})]\right) - k \left(\mathbb{E}_0[\phi^*(\mathbf{X})] - \mathbb{E}_0[\phi(\mathbf{X})]\right) \ge 0$$

Rearranging this inequality gives the fundamental power comparison:

$$\mathbb{E}_1[\phi^*(\mathbf{X})] - \mathbb{E}_1[\phi(\mathbf{X})] \ge k \left(\alpha - \mathbb{E}_0[\phi(\mathbf{X})]\right)$$

Because $k \ge 0$ and the competing test $\phi$ satisfies the level constraint $\mathbb{E}_0[\phi(\mathbf{X})] \le \alpha$ (so $\alpha - \mathbb{E}_0[\phi(\mathbf{X})] \ge 0$), the right-hand side is non-negative. Thus $\mathbb{E}_1[\phi^*(\mathbf{X})] \ge \mathbb{E}_1[\phi(\mathbf{X})]$, proving that $\phi^*$ is Most Powerful.

**Proof of Uniqueness**: Suppose $\phi$ is also a Most Powerful level-$\alpha$ test, so $\mathbb{E}_1[\phi(\mathbf{X})] = \mathbb{E}_1[\phi^*(\mathbf{X})]$. Then the non-negative integral $\int_{\mathcal{X}} \Delta(\mathbf{x}) \, d\mu(\mathbf{x})$ is bounded above by $k(\mathbb{E}_0[\phi(\mathbf{X})] - \alpha) \le 0$, forcing $\int_{\mathcal{X}} \Delta(\mathbf{x}) \, d\mu(\mathbf{x}) = 0$. Since $\Delta(\mathbf{x}) \ge 0$ everywhere on $\mathcal{X}$, we must have $\Delta(\mathbf{x}) = 0$ $\mu$-almost everywhere. On $S_+ \cup S_- = \{\mathbf{x} : f_1(\mathbf{x}) \neq k f_0(\mathbf{x})\}$, the factor $f_1(\mathbf{x}) - k f_0(\mathbf{x})$ is strictly non-zero, forcing $\phi(\mathbf{x}) = \phi^*(\mathbf{x})$ $\mu$-almost everywhere.

## 2.2 Existence Construction, Randomized Discrete NP Tests, and Sufficiency Reduction

To complete the proof of the Neyman-Pearson Fundamental Lemma and apply it to discrete probability models, we must demonstrate constructively how the threshold $k \ge 0$ and randomization weight $\gamma \in [0, 1]$ are determined for any target size $\alpha \in (0, 1)$.

### Constructive Proof of Existence via the Tail Function of the Likelihood Ratio

For all points where $f_0(\mathbf{x}) > 0$, define the likelihood ratio random variable $R(\mathbf{X}) = f_1(\mathbf{X}) / f_0(\mathbf{X})$ (setting $R(\mathbf{x}) = \infty$ where $f_0(\mathbf{x}) = 0$ and $f_1(\mathbf{x}) > 0$). Under the null hypothesis $H_0$, $\mathbb{P}_0(f_0(\mathbf{X}) = 0) = 0$, so $R(\mathbf{X})$ is finite with $P_0$-probability $1$. Define the right-continuous tail probability function $\Psi : [0, \infty) \to [0, 1]$ under $H_0$:

$$\Psi(k) = \mathbb{P}_0\left(R(\mathbf{X}) > k\right) = \mathbb{P}_0\left(f_1(\mathbf{X}) > k f_0(\mathbf{X})\right)$$

Because $1 - \Psi(k) = \mathbb{P}_0(R(\mathbf{X}) \le k)$ is a cumulative distribution function, $\Psi(k)$ possesses three standard analytical properties:
1. $\Psi(k)$ is monotonically non-increasing in $k \in [0, \infty)$.
2. $\Psi(k)$ is right-continuous: $\lim_{t \downarrow k} \Psi(t) = \Psi(k)$, whereas its left-hand limit is $\Psi(k^-) = \lim_{t \uparrow k} \Psi(t) = \mathbb{P}_0(R(\mathbf{X}) \ge k)$. The jump discontinuity at $k$ equals the point mass $\Psi(k^-) - \Psi(k) = \mathbb{P}_0(R(\mathbf{X}) = k)$.
3. At the limits, $\lim_{k \to \infty} \Psi(k) = 0$ and $\Psi(0) = \mathbb{P}_0(f_1(\mathbf{X}) > 0) \le 1$.

Now, given any target significance level $\alpha \in (0, 1)$:
- **Case 1 ($\alpha \le \Psi(0)$)**: Define the critical threshold $k^*$ as the generalized quantile:
  $$k^* = \inf\left\{k \ge 0 : \Psi(k) \le \alpha\right\}$$
  By right-continuity of $\Psi$ and the definition of the infimum, we have the bracketing inequality:
  $$\Psi(k^*) = \mathbb{P}_0(R(\mathbf{X}) > k^*) \le \alpha \le \mathbb{P}_0(R(\mathbf{X}) \ge k^*) = \Psi((k^*)^-)$$
  - If $R(\mathbf{X})$ is a continuous random variable (or has no atom at $k^*$), then $\mathbb{P}_0(R(\mathbf{X}) = k^*) = 0$, so $\Psi(k^*) = \alpha$ exactly, and we may set $\gamma = 0$ (yielding a purely non-randomized test).
  - If $R(\mathbf{X})$ has a positive point mass $\mathbb{P}_0(R(\mathbf{X}) = k^*) > 0$ (as occurs in Binomial, Poisson, and Hypergeometric distributions), we solve the linear interpolation equation $\mathbb{P}_0(R > k^*) + \gamma \, \mathbb{P}_0(R = k^*) = \alpha$ by setting:
    $$\gamma^* = \frac{\alpha - \mathbb{P}_0\left(f_1(\mathbf{X}) > k^* f_0(\mathbf{X})\right)}{\mathbb{P}_0\left(f_1(\mathbf{X}) = k^* f_0(\mathbf{X})\right)} \in [0, 1]$$
- **Case 2 ($\alpha > \Psi(0)$)**: If the null probability of the support of $f_1$ is strictly smaller than $\alpha$, we set $k^* = 0$, so that $\phi^*(\mathbf{x}) = 1$ wherever $f_1(\mathbf{x}) > 0$, and on the boundary set $\{f_1(\mathbf{x}) = 0\}$ we randomize with probability $\gamma^* = \frac{\alpha - \Psi(0)}{1 - \Psi(0)}$ to exhaust the remaining Type I error budget.

### Factorization Through Sufficient Statistics

Suppose $T(\mathbf{X})$ is a sufficient statistic for the family $\{P_{\theta_0}, P_{\theta_1}\}$. By the Neyman-Fisher Factorization Theorem, $f_i(\mathbf{x}) = g_i(T(\mathbf{x})) h(\mathbf{x})$ for $i = 0, 1$, where $h(\mathbf{x}) > 0$ on the common support. Canceling $h(\mathbf{x})$ in the likelihood ratio yields:

$$\Lambda(\mathbf{x}) = \frac{f_1(\mathbf{x})}{f_0(\mathbf{x})} = \frac{g_1(T(\mathbf{x})) h(\mathbf{x})}{g_0(T(\mathbf{x})) h(\mathbf{x})} = \frac{g_1(T(\mathbf{x}))}{g_0(T(\mathbf{x}))} = \Lambda_T(T(\mathbf{x}))$$

This demonstrates that the likelihood ratio depends on the sample $\mathbf{x}$ **exclusively through the sufficient statistic $T(\mathbf{x})$**. Furthermore, if $\Lambda_T(t)$ is a strictly increasing (or strictly decreasing) function of a real-valued sufficient statistic $T(\mathbf{x})$, the inequality $\Lambda_T(T(\mathbf{x})) > k$ is mathematically equivalent to the direct sample-statistic inequality $T(\mathbf{x}) > c$ (or $T(\mathbf{x}) < c$), where $c = \Lambda_T^{-1}(k)$. Rather than solving for the raw density ratio cutoff $k$, the statistician immediately replaces $\Lambda(\mathbf{x}) > k$ with $T(\mathbf{x}) > c$ and calibrates $c$ directly from the null distribution of $T(\mathbf{X})$ under $H_0$!

## 2.3 Strict Unbiasedness of Most Powerful Tests and Geometry of the Risk Set

A fundamental sanity requirement for any statistical hypothesis test is that it should be more likely to reject the null hypothesis when the alternative hypothesis is true than when the null hypothesis is true. A test $\phi$ of level $\alpha$ is defined to be **unbiased** if its power under every alternative parameter value is at least as large as its significance level:

$$\mathbb{E}_{\theta}[\phi(\mathbf{X})] \ge \alpha \quad \forall \theta \in \Theta_1$$

An immediate, profound corollary of the Neyman-Pearson Fundamental Lemma is that **every Most Powerful test for a simple-versus-simple problem is automatically unbiased**, and is **strictly unbiased** ($\beta(\theta_1) > \alpha$) whenever the two probability distributions $P_0$ and $P_1$ are distinct.

### Corollary 2.1: Strict Unbiasedness of Neyman-Pearson Most Powerful Tests

Let $\phi^*(\mathbf{X})$ be the Most Powerful test of size $\alpha \in (0, 1)$ for testing $H_0 : P = P_0$ against $H_1 : P = P_1$. Then the power $\beta = \mathbb{E}_1[\phi^*(\mathbf{X})]$ satisfies:

$$\beta = \mathbb{E}_1[\phi^*(\mathbf{X})] \ge \alpha$$

with strict inequality $\mathbb{E}_1[\phi^*(\mathbf{X})] > \alpha$ holding if and only if $P_0 \neq P_1$ (that is, $f_0(\mathbf{x})$ and $f_1(\mathbf{x})$ are not identical $\mu$-almost everywhere).

#### Formal Proof:
Consider the trivial, data-blind randomized test function $\phi_{\text{coin}}(\mathbf{x}) \equiv \alpha$ for all $\mathbf{x} \in \mathcal{X}$, which ignores the experimental sample entirely and rejects $H_0$ by flipping a biased coin with success probability $\alpha$. Let us compute the size and power of $\phi_{\text{coin}}$:

$$\mathbb{E}_0[\phi_{\text{coin}}(\mathbf{X})] = \int_{\mathcal{X}} \alpha f_0(\mathbf{x}) \, d\mu(\mathbf{x}) = \alpha, \quad \mathbb{E}_1[\phi_{\text{coin}}(\mathbf{X})] = \int_{\mathcal{X}} \alpha f_1(\mathbf{x}) \, d\mu(\mathbf{x}) = \alpha$$

Because $\phi_{\text{coin}}$ is a legitimate level-$\alpha$ test function ($\phi_{\text{coin}} \in \Phi$ with size $\alpha$) and $\phi^*$ is Most Powerful among all level-$\alpha$ tests, Theorem 2.1 immediately guarantees:

$$\mathbb{E}_1[\phi^*(\mathbf{X})] \ge \mathbb{E}_1[\phi_{\text{coin}}(\mathbf{X})] = \alpha$$

Now suppose equality holds: $\mathbb{E}_1[\phi^*(\mathbf{X})] = \alpha$. Then the trivial test $\phi_{\text{coin}}(\mathbf{x}) \equiv \alpha$ achieves the maximum possible power $\alpha$, meaning that $\phi_{\text{coin}}$ is *itself* a Most Powerful test of size $\alpha$! By the Uniqueness clause of the Neyman-Pearson Fundamental Lemma (Theorem 2.1, Part 3), any Most Powerful size-$\alpha$ test must equal $1$ or $0$ $\mu$-almost everywhere on the set $\{\mathbf{x} : f_1(\mathbf{x}) \neq k f_0(\mathbf{x})\}$. However, since $0 < \alpha < 1$, the constant function $\phi_{\text{coin}}(\mathbf{x}) = \alpha$ never takes the value $0$ or $1$ at any point $\mathbf{x} \in \mathcal{X}$. For uniqueness to be satisfied, the set $\{\mathbf{x} : f_1(\mathbf{x}) \neq k f_0(\mathbf{x})\}$ must have $\mu$-measure zero! Thus:

$$f_1(\mathbf{x}) = k f_0(\mathbf{x}) \quad \mu\text{-almost everywhere}$$

Integrating both sides over $\mathcal{X}$ with respect to $\mu$ gives $1 = k \cdot 1 \implies k = 1$, which implies $f_1(\mathbf{x}) = f_0(\mathbf{x})$ $\mu$-almost everywhere ($P_0 = P_1$). By contraposition, whenever $P_0 \neq P_1$, we must have the strict inequality $\mathbb{E}_1[\phi^*(\mathbf{X})] > \alpha$.

### Convex Geometry of the Neyman-Pearson Risk Region and Lyapunov's Theorem

Geometrically, we can map every test function $\phi \in \Phi$ to its error-probability pair $(\alpha(\phi), \beta(\phi)) = (\mathbb{E}_0[\phi], \mathbb{E}_1[\phi]) \in [0, 1]^2$. By **Lyapunov's Convexity Theorem** for vector-valued measures, the attainable region $\mathcal{R} = \{(\mathbb{E}_0[\phi], \mathbb{E}_1[\phi]) : 0 \le \phi \le 1\} \subseteq [0, 1]^2$ is a closed, convex subset of the unit square containing $(0, 0)$ and $(1, 1)$ and symmetric about $(1/2, 1/2)$.
- The diagonal line $\beta = \alpha$ corresponds to the family of data-blind coin flips $\phi(\mathbf{x}) \equiv \alpha$.
- The upper boundary of $\mathcal{R}$—the **optimal power curve** $\alpha \mapsto \beta^*(\alpha)$—is traced out by the Neyman-Pearson likelihood ratio tests $\phi^*_\alpha$ as the threshold $k$ decreases from $\infty$ to $0$. Because $\mathcal{R}$ is convex, $\beta^*(\alpha)$ is a concave, continuous, monotonically increasing function of $\alpha$ whose right derivative at $\alpha$ is precisely the likelihood-ratio cutoff $k(\alpha)$!
- Conversely, the lower boundary of $\mathcal{R}$ (lying below the diagonal $\beta = \alpha$) is traced out by reversing the inequalities in the Neyman-Pearson lemma—rejecting $H_0$ when $f_1(\mathbf{x}) < k f_0(\mathbf{x})$—which yields the *least powerful* (worst possible) size-$\alpha$ test.

## 2.4 One-Parameter Exponential Families and Monotone Likelihood Ratio (MLR) Models

In most scientific investigations, the alternative hypothesis is not a single point $\theta_1$, but a composite domain $\Theta_1$ (such as $\theta > \theta_0$ or $\theta \neq \theta_0$). A test function $\phi^*(\mathbf{x})$ of level $\alpha$ for testing $H_0 : \theta \in \Theta_0$ against $H_1 : \theta \in \Theta_1$ is defined to be a **Uniformly Most Powerful (UMP) level-$\alpha$ test** if it satisfies $\sup_{\theta \in \Theta_0} \mathbb{E}_\theta[\phi^*(\mathbf{X})] \le \alpha$ and simultaneously maximizes power against **every** parameter point in the alternative space:

$$\mathbb{E}_\theta[\phi^*(\mathbf{X})] \ge \mathbb{E}_\theta[\phi(\mathbf{X})] \quad \forall \theta \in \Theta_1$$

for every competing level-$\alpha$ test $\phi$. For a UMP test to exist, the simple-versus-simple Most Powerful test obtained by fixing a specific alternative point $\theta_1 \in \Theta_1$ must turn out to have a critical region that does **not depend on the specific choice of $\theta_1$**. The structural property that guarantees this uniformity across one-sided alternatives is the **Monotone Likelihood Ratio (MLR)** property.

### Definition of Monotone Likelihood Ratio (MLR)

Let $\mathcal{P} = \{f(\mathbf{x}; \theta) : \theta \in \Theta\}$ be a family of probability densities indexed by a real scalar parameter $\theta \in \Theta \subseteq \mathbb{R}$. The family $\mathcal{P}$ is said to have a **Monotone Likelihood Ratio (MLR)** in a real-valued statistic $T(\mathbf{x})$ if, for every pair of parameter values $\theta_1 < \theta_2$ in $\Theta$, the densities $f(\mathbf{x}; \theta_1)$ and $f(\mathbf{x}; \theta_2)$ are distinct, and the likelihood ratio:

$$\Lambda(\mathbf{x}; \theta_1, \theta_2) = \frac{f(\mathbf{x}; \theta_2)}{f(\mathbf{x}; \theta_1)}$$

depends on $\mathbf{x}$ only through $T(\mathbf{x})$ and is a **monotonically non-decreasing function of $T(\mathbf{x})$** on the set of points where at least one of $f(\mathbf{x}; \theta_1)$ or $f(\mathbf{x}; \theta_2)$ is positive (defining $c / 0 = \infty$ for $c > 0$). If the ratio is strictly increasing in $T(\mathbf{x})$ for all $\theta_1 < \theta_2$, the family has a **strict MLR** in $T(\mathbf{x})$.

### Theorem 2.2: MLR Structure of One-Parameter Exponential Families

Suppose $\mathbf{X}$ follows a one-parameter exponential family with density or mass function of the canonical form:

$$f(\mathbf{x}; \theta) = \exp\left( \eta(\theta) T(\mathbf{x}) - B(\theta) \right) h(\mathbf{x})$$

with respect to a dominating measure $\mu$.
1. If the natural parameter mapping $\eta(\theta)$ is a **strictly increasing function of $\theta$** on $\Theta$, then the family $\{f(\mathbf{x}; \theta) : \theta \in \Theta\}$ possesses a strict **Monotone Likelihood Ratio in $T(\mathbf{x})$**.
2. If $\eta(\theta)$ is a **strictly decreasing function of $\theta$**, then the family possesses a strict **Monotone Likelihood Ratio in $-T(\mathbf{x})$** (or in $1/T(\mathbf{x})$ if $T(\mathbf{x}) > 0$).

#### Proof:
For any two parameter values $\theta_1 < \theta_2$, evaluate the likelihood ratio on the common support $\{\mathbf{x} : h(\mathbf{x}) > 0\}$:

$$\frac{f(\mathbf{x}; \theta_2)}{f(\mathbf{x}; \theta_1)} = \frac{\exp(\eta(\theta_2) T(\mathbf{x}) - B(\theta_2)) h(\mathbf{x})}{\exp(\eta(\theta_1) T(\mathbf{x}) - B(\theta_1)) h(\mathbf{x})} = \exp\Big( \left[\eta(\theta_2) - \eta(\theta_1)\right] T(\mathbf{x}) - \left[B(\theta_2) - B(\theta_1)\right] \Big)$$

When $\eta(\theta)$ is strictly increasing in $\theta$, the inequality $\theta_1 < \theta_2$ implies $\eta(\theta_2) - \eta(\theta_1) > 0$. Because the exponential function $u \mapsto e^u$ is strictly increasing and the coefficient $\eta(\theta_2) - \eta(\theta_1)$ multiplying $T(\mathbf{x})$ is strictly positive, the likelihood ratio is a strictly increasing function of $T(\mathbf{x})$ for every pair $\theta_1 < \theta_2$.

This single theorem immediately establishes the MLR property for virtually all standard parametric families:
- **Normal Mean $\mathcal{N}(\theta, \sigma_0^2)$**: $\eta(\theta) = \theta / \sigma_0^2$ is strictly increasing, with $T(\mathbf{x}) = \sum_{i=1}^n x_i$ (or $\bar{x}$).
- **Normal Variance $\mathcal{N}(\mu_0, \theta)$** ($\theta = \sigma^2$): $\eta(\theta) = -1/(2\theta)$ is strictly increasing in $\theta$, with $T(\mathbf{x}) = \sum_{i=1}^n (x_i - \mu_0)^2$.
- **Poisson($\theta$) and Binomial($n, \theta$)**: $\eta(\theta) = \ln(\theta)$ and $\eta(\theta) = \ln\left(\frac{\theta}{1-\theta}\right)$ are both strictly increasing in $\theta$, with $T(\mathbf{x}) = \sum_{i=1}^n x_i$.
- **Exponential Scale $f(x; \theta) = \frac{1}{\theta} e^{-x/\theta}$**: $\eta(\theta) = -1/\theta$ is strictly increasing in $\theta$, with $T(\mathbf{x}) = \sum_{i=1}^n x_i$. (Equivalently, under rate parameterization $f(x; \lambda) = \lambda e^{-\lambda x}$, $\eta(\lambda) = -\lambda$ is decreasing, so MLR holds in $-\sum_{i=1}^n x_i$).

### Non-Exponential MLR Families and Non-MLR Counterexamples

The class of MLR distributions is strictly broader than the exponential family! Important non-exponential families with MLR include:
1. **Uniform Scale Family $\text{Uniform}(0, \theta)$**: For $\theta_1 < \theta_2$, the joint density ratio is:
   $$\frac{f_n(\mathbf{x}; \theta_2)}{f_n(\mathbf{x}; \theta_1)} = \frac{\theta_2^{-n} \mathbf{1}_{(0, \theta_2]}(x_{(n)})}{\theta_1^{-n} \mathbf{1}_{(0, \theta_1]}(x_{(n)})} = \begin{cases} (\theta_1 / \theta_2)^n, & \text{if } 0 < x_{(n)} \le \theta_1 \\ +\infty, & \text{if } \theta_1 < x_{(n)} \le \theta_2 \end{cases}$$
   As a function of the maximum order statistic $T(\mathbf{x}) = X_{(n)}$, this step function jumps from the finite positive constant $(\theta_1/\theta_2)^n$ on $(0, \theta_1]$ to $+\infty$ on $(\theta_1, \theta_2]$, so it is non-decreasing in $X_{(n)}$!
2. **Hypergeometric Distribution**: Sampling without replacement from a finite lot with $M = \theta$ defectives has MLR in the sample defective count $X$.
3. **Logistic and Double-Exponential (Laplace) Location Families ($n = 1$)**: A single observation from a location family $f(x - \theta)$ has MLR in $x$ if and only if $-\ln f(u)$ is a convex function on $\mathbb{R}$ (i.e., $f$ is a **log-concave** or Pólya frequency function of order 2, $PF_2$).

Conversely, the **Cauchy Location Family** $f(x; \theta) = \frac{1}{\pi [1 + (x - \theta)^2]}$ is **not** log-concave and **fails the MLR property**: for $\theta_1 < \theta_2$, the likelihood ratio $\frac{1 + (x - \theta_1)^2}{1 + (x - \theta_2)^2}$ converges to $1$ as $x \to +\infty$ and as $x \to -\infty$, achieving a global maximum at $x_{\max} = \frac{\theta_1 + \theta_2}{2} + \sqrt{1 + \left(\frac{\theta_2 - \theta_1}{2}\right)^2}$ and then **decreasing** toward $1$ for larger $x$! In a Cauchy model, an extreme outlier $x$ is nearly as improbable under $\theta_2$ as under $\theta_1$, destroying monotonicity of the likelihood ratio.

## 2.5 The Karlin-Rubin Theorem for UMP One-Sided Tests and Non-Existence of Two-Sided UMP Tests

Whenever a statistical model possesses the Monotone Likelihood Ratio property in a real-valued statistic $T(\mathbf{X})$, the existence and explicit structure of the Uniformly Most Powerful (UMP) test for composite one-sided hypotheses are completely resolved by the **Karlin-Rubin Theorem** (Samuel Karlin and Herman Rubin, 1956).

### Theorem 2.3: The Karlin-Rubin Theorem for One-Sided Composite Hypotheses

Let $\mathbf{X}$ have probability distribution $P_\theta$ belonging to a family $\{P_\theta : \theta \in \Theta\}$ with scalar parameter $\theta \in \Theta \subseteq \mathbb{R}$ that possesses a Monotone Likelihood Ratio (MLR) in a real-valued statistic $T(\mathbf{X})$. Consider testing the composite one-sided null hypothesis against the one-sided alternative:

$$H_0 : \theta \le \theta_0 \quad \text{versus} \quad H_1 : \theta > \theta_0$$

for a fixed boundary value $\theta_0 \in \Theta$.
1. For any significance level $\alpha \in (0, 1)$, there exist a critical value $t_0 \in \mathbb{R}$ and a randomization constant $\gamma \in [0, 1]$ such that the upper-tail test function:
   $$\phi^*(\mathbf{x}) = \begin{cases} 1, & \text{if } T(\mathbf{x}) > t_0 \\ \gamma, & \text{if } T(\mathbf{x}) = t_0 \\ 0, & \text{if } T(\mathbf{x}) < t_0 \end{cases}$$
   satisfies the boundary size calibration $\mathbb{E}_{\theta_0}[\phi^*(\mathbf{X})] = \alpha$.
2. The power function $\beta(\theta) = \mathbb{E}_\theta[\phi^*(\mathbf{X})]$ is a **strictly increasing function of $\theta$** for all $\theta$ such that $0 < \beta(\theta) < 1$ (and non-decreasing everywhere on $\Theta$).
3. Consequently, $\phi^*(\mathbf{x})$ satisfies the composite level constraint $\sup_{\theta \le \theta_0} \beta(\theta) = \beta(\theta_0) = \alpha$, and $\phi^*(\mathbf{x})$ is the **Uniformly Most Powerful (UMP) level-$\alpha$ test** for $H_0 : \theta \le \theta_0$ versus $H_1 : \theta > \theta_0$.
4. By symmetry, for testing the reverse one-sided hypothesis $H_0' : \theta \ge \theta_0$ versus $H_1' : \theta < \theta_0$, the lower-tail test rejecting when $T(\mathbf{x}) < t_0'$ (with boundary randomization at $T(\mathbf{x}) = t_0'$) calibrated so that $\mathbb{E}_{\theta_0}[\phi^{**}(\mathbf{X})] = \alpha$ has strictly decreasing power in $\theta$ and is UMP of level $\alpha$.

#### Complete Mathematical Proof:
**Step 1 (Pointwise Optimality against any $\theta_1 > \theta_0$)**: Fix any specific alternative parameter value $\theta_1 > \theta_0$. Consider the restricted simple-versus-simple testing problem $H_{0,\text{simple}} : \theta = \theta_0$ against $H_{1,\text{simple}} : \theta = \theta_1$ at size $\alpha = \mathbb{E}_{\theta_0}[\phi^*(\mathbf{X})]$. Because the family has MLR in $T(\mathbf{x})$, the likelihood ratio $\Lambda(\mathbf{x}) = f(\mathbf{x}; \theta_1) / f(\mathbf{x}; \theta_0)$ is a non-decreasing function $g(T(\mathbf{x}))$ of $T(\mathbf{x})$. Therefore, for every $\mathbf{x} \in \mathcal{X}$:
- $T(\mathbf{x}) > t_0 \implies \Lambda(\mathbf{x}) = g(T(\mathbf{x})) \ge g(t_0) \equiv k$
- $T(\mathbf{x}) < t_0 \implies \Lambda(\mathbf{x}) = g(T(\mathbf{x})) \le g(t_0) \equiv k$

This implies that the upper-tail test $\phi^*(\mathbf{x})$ satisfies the exact Neyman-Pearson Fundamental Lemma inequalities $\left[\phi^*(\mathbf{x}) - \phi(\mathbf{x})\right] \left[f(\mathbf{x}; \theta_1) - k f(\mathbf{x}; \theta_0)\right] \ge 0$ for all $\mathbf{x} \in \mathcal{X}$! By Theorem 2.1, $\phi^*(\mathbf{x})$ is a Most Powerful test of size $\alpha$ for testing $\theta = \theta_0$ against $\theta = \theta_1$. Crucially, notice that the definition of $\phi^*(\mathbf{x})$ depends **only** on $t_0$ and $\gamma$, which are determined solely by the null distribution at $\theta_0$ ($\mathbb{E}_{\theta_0}[\phi^*(\mathbf{X})] = \alpha$) and do **not** depend on $\theta_1$! Therefore, $\phi^*$ is simultaneously Most Powerful against *every* $\theta_1 > \theta_0$ among all tests satisfying $\mathbb{E}_{\theta_0}[\phi(\mathbf{X})] \le \alpha$.

**Step 2 (Monotonicity of the Power Function and Composite Level Validity)**: Let $\theta' < \theta''$ be any two arbitrary parameter points in $\Theta$ such that $\alpha' = \mathbb{E}_{\theta'}[\phi^*(\mathbf{X})] \in (0, 1)$. By the exact same argument as Step 1 applied to the simple-versus-simple pair $(\theta', \theta'')$, $\phi^*(\mathbf{x})$ is the Most Powerful test of size $\alpha'$ for testing $H_0^* : \theta = \theta'$ against $H_1^* : \theta = \theta''$. By Corollary 2.1 (Strict Unbiasedness of MP tests), its power under $\theta''$ must strictly exceed its size under $\theta'$:

$$\beta(\theta'') = \mathbb{E}_{\theta''}[\phi^*(\mathbf{X})] > \mathbb{E}_{\theta'}[\phi^*(\mathbf{X})] = \beta(\theta')$$

This proves that $\beta(\theta)$ is strictly increasing in $\theta$! Because $\beta(\theta)$ is non-decreasing, for all $\theta \le \theta_0$ we have $\beta(\theta) \le \beta(\theta_0) = \alpha$, confirming that $\phi^*$ is a valid level-$\alpha$ test for the composite null $H_0 : \theta \le \theta_0$. Finally, let $\mathcal{F}_{\le \theta_0} = \{\phi : \beta_\phi(\theta) \le \alpha \; \forall \theta \le \theta_0\}$ be the class of level-$\alpha$ tests for the composite null, and let $\mathcal{F}_{=\theta_0} = \{\phi : \beta_\phi(\theta_0) \le \alpha\}$ be the larger class of level-$\alpha$ tests for the boundary point $\theta = \theta_0$. Since $\mathcal{F}_{\le \theta_0} \subseteq \mathcal{F}_{=\theta_0}$ and $\phi^* \in \mathcal{F}_{\le \theta_0}$ maximizes power over the larger class $\mathcal{F}_{=\theta_0}$ for every $\theta_1 > \theta_0$, it a fortiori maximizes power over $\mathcal{F}_{\le \theta_0}$ for every $\theta_1 > \theta_0$, establishing that $\phi^*$ is UMP of level $\alpha$.

### Fundamental Non-Existence of Two-Sided UMP Tests in Exponential Families

What happens if we attempt to test a point null hypothesis against a **two-sided alternative** in a regular exponential family?

$$H_0 : \theta = \theta_0 \quad \text{versus} \quad H_1 : \theta \neq \theta_0 \quad (\Theta_1 = \{\theta : \theta < \theta_0\} \cup \{\theta : \theta > \theta_0\})$$

**Theorem 2.4**: In any continuous one-parameter exponential family (such as $\mathcal{N}(\theta, \sigma_0^2)$), **no Uniformly Most Powerful level-$\alpha$ test exists for testing $H_0 : \theta = \theta_0$ against $H_1 : \theta \neq \theta_0$** ($0 < \alpha < 1$).

*Proof*: Suppose by way of contradiction that a UMP level-$\alpha$ test $\phi_{\text{two}}(\mathbf{x})$ existed for $H_0 : \theta = \theta_0$ versus $H_1 : \theta \neq \theta_0$.
1. Against any specific right-sided alternative $\theta_1 > \theta_0$, the unique (up to measure zero) Most Powerful level-$\alpha$ test is the right-tailed test $\phi_+(\mathbf{x}) = \mathbf{1}_{\{T(\mathbf{x}) > c_+\}}$. For $\phi_{\text{two}}$ to match the power of $\phi_+$ at $\theta_1 > \theta_0$, uniqueness in the Neyman-Pearson Lemma requires $\phi_{\text{two}}(\mathbf{x}) = \phi_+(\mathbf{x})$ almost everywhere.
2. Against any specific left-sided alternative $\theta_2 < \theta_0$, the unique Most Powerful level-$\alpha$ test is the left-tailed test $\phi_-(\mathbf{x}) = \mathbf{1}_{\{T(\mathbf{x}) < c_-\}}$. For $\phi_{\text{two}}$ to match the power of $\phi_-$ at $\theta_2 < \theta_0$, uniqueness requires $\phi_{\text{two}}(\mathbf{x}) = \phi_-(\mathbf{x})$ almost everywhere.
3. However, the right-tail indicator $\mathbf{1}_{\{T > c_+\}}$ and the left-tail indicator $\mathbf{1}_{\{T < c_-\}}$ are disjoint functions that disagree on a set of positive probability! Indeed, the right-tailed test $\phi_+$ has power strictly less than $\alpha$ for all $\theta < \theta_0$ ($\beta_+(\theta_2) < \alpha < \beta_-(\theta_2)$), while the left-tailed test $\phi_-$ has power strictly less than $\alpha$ for all $\theta > \theta_0$. Because no single critical region can simultaneously concentrate all $\alpha$ of its rejection mass in the extreme right tail and all $\alpha$ of its rejection mass in the extreme left tail, a two-sided UMP test cannot exist.

## 2.6 Non-Regular Support-Dependent UMP Tests, Minimax Dualities, and Bayesian Connections

While two-sided UMP tests fail to exist in regular exponential families whose supports are independent of $\theta$, a striking exception occurs in **non-regular boundary-support families** such as the Uniform distribution $\text{Uniform}(0, \theta)$.

### Existence of a Two-Sided UMP Test in the Uniform $(0, \theta)$ Model

Let $X_1, \dots, X_n \overset{\text{iid}}{\sim} \text{Uniform}(0, \theta)$ with $\theta > 0$, and consider testing the point null hypothesis against the **two-sided alternative**:

$$H_0 : \theta = \theta_0 \quad \text{versus} \quad H_1 : \theta \neq \theta_0$$

at significance level $\alpha \in (0, 1)$. The sufficient statistic is the sample maximum $T(\mathbf{X}) = X_{(n)}$, which under $H_0$ has cumulative distribution function $F_0(t) = (t / \theta_0)^n$ on $(0, \theta_0]$.
1. **Right-Sided Alternatives ($\theta_1 > \theta_0$)**: If the observed maximum satisfies $X_{(n)} > \theta_0$, the null density is $f_n(\mathbf{x}; \theta_0) = 0$ while $f_n(\mathbf{x}; \theta_1) = \theta_1^{-n} > 0$. The likelihood ratio is $\Lambda(\mathbf{x}) = +\infty$! Thus, including the entire region $\{X_{(n)} > \theta_0\}$ inside the critical region $\mathcal{C}$ costs **zero Type I error** under $H_0$ while capturing all sample realizations in $(\theta_0, \theta_1]$ under $H_1$.
2. **Left-Sided Alternatives ($\theta_2 < \theta_0$)**: When $\theta_2 < \theta_0$, the support of $X_{(n)}$ under $\theta_2$ is $(0, \theta_2] \subset (0, \theta_0]$. On $(0, \theta_2]$, the likelihood ratio $f_n(\mathbf{x}; \theta_2) / f_n(\mathbf{x}; \theta_0) = (\theta_0 / \theta_2)^n > 1$ is constant, whereas on $(\theta_2, \theta_0]$ it is $0$. To maximize power simultaneously for all $\theta_2 < \theta_0$, we must place our entire Type I error budget $\alpha$ at the **leftmost end of the interval $(0, \theta_0]$**, namely $(0, c]$ where $(c / \theta_0)^n = \alpha \implies c = \theta_0 \alpha^{1/n}$, so that $(0, c] \subseteq (0, \theta_2]$ for as many $\theta_2 < \theta_0$ as possible!

Combining both regions yields the critical region:

$$\mathcal{C}^* = \left\{\mathbf{x} \in \mathbb{R}^n : X_{(n)} \le \theta_0 \alpha^{1/n} \;\text{ or }\; X_{(n)} > \theta_0\right\}$$

Let us verify that $\phi^*(\mathbf{x}) = \mathbf{1}_{\mathcal{C}^*}(\mathbf{x})$ is **Uniformly Most Powerful of size $\alpha$ for the two-sided problem $H_0 : \theta = \theta_0$ vs $H_1 : \theta \neq \theta_0$**:
- **Size**: $\mathbb{P}_{\theta_0}(\mathbf{X} \in \mathcal{C}^*) = \mathbb{P}_{\theta_0}(X_{(n)} \le \theta_0 \alpha^{1/n}) + \mathbb{P}_{\theta_0}(X_{(n)} > \theta_0) = \alpha + 0 = \alpha$.
- **Power for $\theta > \theta_0$**: $\beta^*(\theta) = \mathbb{P}_\theta(X_{(n)} \le \theta_0 \alpha^{1/n}) + \mathbb{P}_\theta(X_{(n)} > \theta_0) = \alpha (\theta_0/\theta)^n + \left[1 - (\theta_0/\theta)^n\right] = 1 - (1 - \alpha)(\theta_0/\theta)^n$, which is the exact maximum possible power of any level-$\alpha$ test at $\theta > \theta_0$.
- **Power for $\theta < \theta_0$**: If $\theta \le \theta_0 \alpha^{1/n}$, the entire support $(0, \theta]$ lies inside $(0, \theta_0 \alpha^{1/n}] \subset \mathcal{C}^*$, so $\beta^*(\theta) = 1$ (clearly maximal). If $\theta_0 \alpha^{1/n} < \theta < \theta_0$, then $\beta^*(\theta) = \mathbb{P}_\theta(X_{(n)} \le \theta_0 \alpha^{1/n}) = \alpha (\theta_0/\theta)^n$. Since any level-$\alpha$ test $\phi$ satisfies $\int_{(0, \theta]} \phi(\mathbf{x}) \theta_0^{-n} \, d\mathbf{x} \le \int_{(0, \theta_0]} \phi(\mathbf{x}) \theta_0^{-n} \, d\mathbf{x} \le \alpha$, multiplying by $(\theta_0/\theta)^n$ shows $\mathbb{E}_\theta[\phi] \le \alpha (\theta_0/\theta)^n = \beta^*(\theta)$.

Thus, because the right-tail region $\{X_{(n)} > \theta_0\}$ has null probability zero and requires zero Type I error expenditure, the entire $\alpha$ budget remains available for the left tail $\{X_{(n)} \le \theta_0 \alpha^{1/n}\}$, permitting a genuine two-sided UMP test to exist!

### Generalized Neyman-Pearson Lemma and Bayesian / Minimax Duality

The Neyman-Pearson Lemma also forms the bridge to Bayesian decision theory and Abraham Wald's minimax theory:
1. **Bayes Test for Binary Hypotheses**: Suppose $H_0 : \theta = \theta_0$ and $H_1 : \theta = \theta_1$ have prior probabilities $\pi_0 \in (0, 1)$ and $\pi_1 = 1 - \pi_0$, with loss $c_{\text{I}} > 0$ for Type I error and $c_{\text{II}} > 0$ for Type II error. The Bayes risk of a test $\phi$ is:
   $$r(\pi, \phi) = \pi_0 c_{\text{I}} \mathbb{E}_0[\phi(\mathbf{X})] + \pi_1 c_{\text{II}} \left(1 - \mathbb{E}_1[\phi(\mathbf{X})]\right) = \pi_1 c_{\text{II}} + \int_{\mathcal{X}} \phi(\mathbf{x}) \left[\pi_0 c_{\text{I}} f_0(\mathbf{x}) - \pi_1 c_{\text{II}} f_1(\mathbf{x})\right] d\mu(\mathbf{x})$$
   Minimizing $r(\pi, \phi)$ pointwise with respect to $0 \le \phi(\mathbf{x}) \le 1$ requires setting $\phi(\mathbf{x}) = 1$ whenever the bracketed integrand is negative, which is precisely the Neyman-Pearson rule $f_1(\mathbf{x}) / f_0(\mathbf{x}) > \frac{\pi_0 c_{\text{I}}}{\pi_1 c_{\text{II}}} \equiv k$! Thus every Bayes test is a Neyman-Pearson likelihood ratio test with threshold $k = \frac{\pi_0 c_{\text{I}}}{\pi_1 c_{\text{II}}}$.
2. **Minimax Test**: Under 0-1 loss ($c_{\text{I}} = c_{\text{II}} = 1$), a test $\phi_{\text{mm}}$ minimizes the maximum error probability $\max\left(\alpha(\phi), \tilde{\beta}(\phi)\right)$ if and only if it is a Neyman-Pearson likelihood ratio test whose threshold $k^*$ is calibrated to satisfy the **equalizer condition** $\alpha(\phi^*) = \tilde{\beta}(\phi^*)$, meaning Type I error probability equals Type II error probability: $\mathbb{E}_0[\phi^*(\mathbf{X})] = 1 - \mathbb{E}_1[\phi^*(\mathbf{X})]$.

### Sample Size Determination and Discrete Hypergeometric UMP Tests

In experimental design, clinical trial planning, and industrial acceptance sampling, the sample size $n$ is not fixed in advance; rather, the investigator specifies both a maximum permissible Type I error probability $\alpha \in (0, 1)$ at the null parameter $\theta_0$ and a maximum permissible Type II error probability $\tilde{\beta}_1 = 1 - \beta_1 \in (0, 1)$ at a scientifically meaningful minimum detectable effect size $\theta_1 > \theta_0$. Because the UMP power function $\beta_n(\theta)$ increases monotonically with sample size $n$, there exists a minimum integer sample size $n^*$ that simultaneously satisfies both error constraints:

$$\beta_n(\theta_0) \le \alpha \quad \text{and} \quad \beta_n(\theta_1) \ge 1 - \tilde{\beta}_1$$

### Closed-Form Sample Size Calibration in Gaussian Location Models

Let $X_1, \dots, X_n \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma_0^2)$ with known variance $\sigma_0^2 > 0$. By the Karlin-Rubin Theorem, the UMP size-$\alpha$ test for $H_0 : \mu \le \mu_0$ versus $H_1 : \mu > \mu_0$ rejects $H_0$ whenever the sample mean exceeds the critical threshold:

$$\bar{X}_n > c_n = \mu_0 + z_{1-\alpha} \frac{\sigma_0}{\sqrt{n}}$$

where $z_{1-\alpha} = \Phi^{-1}(1 - \alpha)$ is the upper $\alpha$ quantile of the standard normal distribution. Under any arbitrary mean $\mu \in \mathbb{R}$, the standardized statistic $\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma_0} \sim \mathcal{N}(0, 1)$, so the exact power function is:

$$\beta_n(\mu) = \mathbb{P}_\mu\left(\bar{X}_n > \mu_0 + z_{1-\alpha} \frac{\sigma_0}{\sqrt{n}}\right) = 1 - \Phi\left(z_{1-\alpha} - \frac{\sqrt{n}(\mu - \mu_0)}{\sigma_0}\right) = \Phi\left(\frac{\sqrt{n}(\mu - \mu_0)}{\sigma_0} - z_{1-\alpha}\right)$$

To guarantee that the power at the target alternative $\mu_1 > \mu_0$ reaches at least $1 - \tilde{\beta}_1$ (where $\tilde{\beta}_1$ is the target Type II error), we set $\beta_n(\mu_1) \ge 1 - \tilde{\beta}_1 = \Phi(z_{1-\tilde{\beta}_1})$. Applying the monotonicity of $\Phi$:

$$\frac{\sqrt{n}(\mu_1 - \mu_0)}{\sigma_0} - z_{1-\alpha} \ge z_{1-\tilde{\beta}_1} \implies \sqrt{n} \ge \frac{(z_{1-\alpha} + z_{1-\tilde{\beta}_1}) \sigma_0}{\mu_1 - \mu_0}$$

Squaring both sides yields the fundamental sample size formula for one-sided normal testing:

$$n^* = \left\lceil \frac{\left(z_{1-\alpha} + z_{1-\tilde{\beta}_1}\right)^2 \sigma_0^2}{(\mu_1 - \mu_0)^2} \right\rceil = \left\lceil \frac{\left(z_{1-\alpha} + z_{1-\tilde{\beta}_1}\right)^2}{\delta^2} \right\rceil$$

where $\delta = (\mu_1 - \mu_0)/\sigma_0$ is Cohen's standardized effect size. Notice the inverse-square scaling law: halving the minimum detectable effect size $\delta$ quadruples the required sample size $n^*$.

### Discrete UMP Tests in Binomial and Hypergeometric Sampling

In discrete families with Monotone Likelihood Ratio, the Karlin-Rubin Theorem produces exact UMP tests that require explicit randomization at the integer cutoff $t_0$ to attain exact size $\alpha$:
1. **Binomial Proportion Testing**: For $X \sim \text{Binomial}(n, p)$ testing $H_0 : p \le p_0$ against $H_1 : p > p_0$, the likelihood ratio for $p_1 < p_2$ is $\left(\frac{p_2(1-p_1)}{p_1(1-p_2)}\right)^x$, which is strictly increasing in $x$. The UMP size-$\alpha$ test rejects when $X > k$, and rejects with probability $\gamma = \frac{\alpha - \mathbb{P}_{p_0}(X > k)}{\mathbb{P}_{p_0}(X = k)}$ when $X = k$.
2. **Hypergeometric Acceptance Sampling (Lot Inspection)**: Suppose a finite manufacturing lot of $N$ items contains an unknown integer number $M \in \{0, 1, \dots, N\}$ of defective items. An inspector draws a simple random sample of $n$ items **without replacement** and observes the number of defectives $X \sim \text{Hypergeometric}(N, M, n)$:
   $$f(x; M) = \frac{\binom{M}{x} \binom{N - M}{n - x}}{\binom{N}{n}}, \quad \max(0, n - N + M) \le x \le \min(n, M)$$
   Although the Hypergeometric distribution does *not* belong to the exponential family (because its support depends on $M$), let us examine the ratio of probabilities for $M + 1$ versus $M$ defectives:
   $$\frac{f(x; M + 1)}{f(x; M)} = \frac{\binom{M+1}{x} \binom{N - M - 1}{n - x}}{\binom{M}{x} \binom{N - M}{n - x}} = \frac{M + 1}{M + 1 - x} \cdot \frac{N - M - n + x}{N - M}$$
   As $x$ increases, the numerator factor $N - M - n + x$ strictly increases while the denominator factor $M + 1 - x$ strictly decreases! Therefore, the ratio $f(x; M + 1) / f(x; M)$ is a strictly increasing function of $x$. By induction, $f(x; M_2) / f(x; M_1)$ is strictly increasing in $x$ for all $M_1 < M_2$, establishing that the Hypergeometric family has a strict Monotone Likelihood Ratio in $X$ and admits an exact UMP upper-tail test for $H_0 : M \le M_0$ versus $H_1 : M > M_0$.

## Fully worked question 1: Neyman-Pearson Most Powerful Test, Exact Chi-Square Cutoff, and Power Function for Weibull Reliability

### Question
The failure lifetimes $X_1, X_2, \dots, X_n$ of $n = 10$ aerospace turbine blades follow an independent and identically distributed Weibull distribution with known shape parameter $\beta_0 = 2$ and unknown scale parameter $\theta > 0$, having probability density function:

$$f(x; \theta) = \frac{2x}{\theta} \exp\left(-\frac{x^2}{\theta}\right), \quad x > 0$$

1. Apply the Neyman-Pearson Fundamental Lemma to derive the structure of the Most Powerful (MP) test of size $\alpha = 0.05$ for testing the simple null hypothesis $H_0 : \theta = \theta_0$ against the simple alternative $H_1 : \theta = \theta_1$ (where $\theta_1 > \theta_0$), simplified in terms of a minimal sufficient statistic $T(\mathbf{X})$.
2. Prove that the family $\{f_n(\mathbf{x}; \theta) : \theta > 0\}$ has a strict Monotone Likelihood Ratio (MLR) in $T(\mathbf{X})$ and invoke the Karlin-Rubin Theorem to establish that the test is Uniformly Most Powerful (UMP) for $H_0 : \theta \le \theta_0$ versus $H_1 : \theta > \theta_0$.
3. Derive the exact sampling distribution of $\frac{2 T(\mathbf{X})}{\theta}$ in terms of the Chi-Square family, compute the exact critical value $c$ for $\theta_0 = 100$ and $\alpha = 0.05$ (given $\chi^2_{20, 0.05} = 31.4104$ and $\chi^2_{20, 0.95} = 10.8508$), and evaluate the exact power at $\theta_1 = 289.47$.

### Solution, step 1: Neyman-Pearson likelihood ratio and sufficient statistic reduction
For an i.i.d. sample $\mathbf{X} = (X_1, \dots, X_n)$ of size $n = 10$, the joint probability density function under parameter $\theta > 0$ is:

$$f_n(\mathbf{x}; \theta) = \prod_{i=1}^n \left(\frac{2 x_i}{\theta} e^{-x_i^2 / \theta}\right) = \left(\frac{2}{\theta}\right)^n \left(\prod_{i=1}^n x_i\right) \exp\left(-\frac{1}{\theta} \sum_{i=1}^n x_i^2\right), \quad x_i > 0$$

To test $H_0 : \theta = \theta_0$ against $H_1 : \theta = \theta_1$ ($\theta_1 > \theta_0$), we form the Neyman-Pearson likelihood ratio:

$$\Lambda(\mathbf{x}) = \frac{f_n(\mathbf{x}; \theta_1)}{f_n(\mathbf{x}; \theta_0)} = \left(\frac{\theta_0}{\theta_1}\right)^n \exp\left[ \left(\frac{1}{\theta_0} - \frac{1}{\theta_1}\right) \sum_{i=1}^n x_i^2 \right]$$

Define the sufficient statistic $T(\mathbf{X}) = \sum_{i=1}^n X_i^2$. By the Neyman-Pearson Fundamental Lemma, the Most Powerful test rejects $H_0$ when $\Lambda(\mathbf{x}) > k$. Taking natural logarithms:

$$n \ln\left(\frac{\theta_0}{\theta_1}\right) + \left(\frac{1}{\theta_0} - \frac{1}{\theta_1}\right) T(\mathbf{x}) > \ln(k)$$

Because $\theta_1 > \theta_0 > 0$, the coefficient $\left(\frac{1}{\theta_0} - \frac{1}{\theta_1}\right) = \frac{\theta_1 - \theta_0}{\theta_0 \theta_1} > 0$ is strictly positive. Dividing by this positive constant preserves the direction of the inequality:

$$T(\mathbf{x}) = \sum_{i=1}^n x_i^2 > \frac{\ln(k) - n \ln(\theta_0 / \theta_1)}{\frac{1}{\theta_0} - \frac{1}{\theta_1}} \equiv c$$

Since $T(\mathbf{X})$ is a continuous random variable, no boundary randomization is required ($\gamma = 0$), and the Most Powerful size-$\alpha$ test rejects $H_0$ if and only if $T(\mathbf{X}) = \sum_{i=1}^n X_i^2 > c$.

### Solution, step 2: MLR verification and Karlin-Rubin UMP optimality
Notice that the joint density belongs to the one-parameter exponential family:

$$f_n(\mathbf{x}; \theta) = \exp\left( \eta(\theta) T(\mathbf{x}) - n \ln(\theta) \right) \left(2^n \prod_{i=1}^n x_i\right), \quad \text{where } \eta(\theta) = -\frac{1}{\theta}, \quad T(\mathbf{x}) = \sum_{i=1}^n x_i^2$$

Differentiating the natural parameter with respect to $\theta$ gives $\eta'(\theta) = \frac{1}{\theta^2} > 0$ for all $\theta > 0$. Because $\eta(\theta)$ is strictly increasing in $\theta$, Theorem 2.2 guarantees that the family possesses a strict **Monotone Likelihood Ratio (MLR)** in $T(\mathbf{X}) = \sum_{i=1}^n X_i^2$. Furthermore, the critical region $\{T(\mathbf{X}) > c\}$ depends only on the null parameter $\theta_0$ and $\alpha$, and is completely independent of $\theta_1$. By the Karlin-Rubin Theorem (Theorem 2.3), $\phi^*(\mathbf{X}) = \mathbf{1}_{\{T(\mathbf{X}) > c\}}$ is the **Uniformly Most Powerful (UMP) size-$\alpha$ test** for the composite hypotheses $H_0 : \theta \le \theta_0$ versus $H_1 : \theta > \theta_0$.

### Solution, step 3: Exact Chi-Square distribution, critical cutoff c, and power calculation
Let us determine the exact distribution of $Y_i = X_i^2 / \theta$. For $y > 0$, the cumulative distribution function of $Y_i$ is:

$$\mathbb{P}_\theta\left(\frac{X_i^2}{\theta} \le y\right) = \mathbb{P}_\theta\left(X_i \le \sqrt{\theta y}\right) = \int_0^{\sqrt{\theta y}} \frac{2x}{\theta} e^{-x^2 / \theta} \, dx = \left[-e^{-x^2 / \theta}\right]_0^{\sqrt{\theta y}} = 1 - e^{-y}, \quad y > 0$$

Thus $X_i^2 / \theta \overset{\text{iid}}{\sim} \text{Exponential}(1) \equiv \frac{1}{2} \chi^2_2$, which implies $2 X_i^2 / \theta \overset{\text{iid}}{\sim} \chi^2_2$. By the additive property of independent Chi-Square random variables over $n = 10$ observations:

$$Q(\theta) = \frac{2 T(\mathbf{X})}{\theta} = \frac{2}{\theta} \sum_{i=1}^{10} X_i^2 \sim \chi^2_{2n} = \chi^2_{20}$$

Under $H_0 : \theta_0 = 100$ at size $\alpha = 0.05$, we calibrate $c$ so that:

$$\mathbb{P}_{\theta_0}\left(T(\mathbf{X}) > c\right) = \mathbb{P}_{\theta_0}\left(\frac{2 T(\mathbf{X})}{100} > \frac{2c}{100}\right) = \mathbb{P}\left(\chi^2_{20} > \frac{c}{50}\right) = 0.05$$

Using the upper $5\%$ critical quantile $\chi^2_{20, 0.05} = 31.4104$:

$$\frac{c}{50} = 31.4104 \implies c = 50 \times 31.4104 = 1570.52$$

Finally, under the alternative $\theta_1 = 289.47$, the statistic $\frac{2 T(\mathbf{X})}{\theta_1} \sim \chi^2_{20}$. The exact power at $\theta_1 = 289.47$ is:

$$\beta(289.47) = \mathbb{P}_{\theta_1}\left(T(\mathbf{X}) > 1570.52\right) = \mathbb{P}_{\theta_1}\left(\frac{2 T(\mathbf{X})}{289.47} > \frac{2(1570.52)}{289.47}\right) = \mathbb{P}\left(\chi^2_{20} > 10.8508\right)$$

Since $\chi^2_{20, 0.95} = 10.8508$ is the lower $5\%$ quantile (upper $95\%$ tail) of $\chi^2_{20}$, the exact power is $\beta(289.47) = 0.9500$ ($95.0\%$).

## Fully worked question 2: Exact Minimax and Bayes Likelihood Ratio Tests for Simple Hypotheses in Exponential Models

### Question
A single observation $X$ is drawn from an Exponential distribution with density $f(x; \lambda) = \lambda e^{-\lambda x}$ for $x > 0$. We wish to test the simple null hypothesis $H_0 : \lambda = \lambda_0 = 1$ against the simple alternative hypothesis $H_1 : \lambda = \lambda_1 = 3$.

1. Derive the form of the Neyman-Pearson Most Powerful test of size $\alpha \in (0, 1)$, and express the Type II error probability $\tilde{\beta}(\alpha) = 1 - \beta(\alpha)$ as an explicit algebraic function of the Type I error $\alpha$.
2. Suppose the prior probabilities are $\pi_0 = 0.75$ and $\pi_1 = 0.25$, with symmetric 0-1 losses ($c_{\text{I}} = c_{\text{II}} = 1$). Find the exact **Bayes test** critical region, its Type I error $\alpha_{\text{Bayes}}$, Type II error $\tilde{\beta}_{\text{Bayes}}$, and minimum Bayes risk $r^*(\pi)$.
3. Find the exact **Minimax test** under 0-1 loss by solving the transcendental equalizer equation $\alpha = \tilde{\beta}(\alpha)$ explicitly, and compute the minimax risk.

### Solution, step 1: Neyman-Pearson critical region and exact trade-off curve between alpha and Type II error
Under $H_0 : \lambda_0 = 1$, the density is $f_0(x) = e^{-x}$, and under $H_1 : \lambda_1 = 3$, the density is $f_1(x) = 3 e^{-3x}$ for $x > 0$. The Neyman-Pearson likelihood ratio is:

$$\Lambda(x) = \frac{f_1(x)}{f_0(x)} = \frac{3 e^{-3x}}{e^{-x}} = 3 e^{-2x}, \quad x > 0$$

Notice that $\Lambda(x) = 3 e^{-2x}$ is a **strictly decreasing** function of $x$. Therefore, the inequality $\Lambda(x) > k$ is equivalent to the **lower-tail** rejection region:

$$3 e^{-2x} > k \iff e^{-2x} > \frac{k}{3} \iff x < -\frac{1}{2} \ln\left(\frac{k}{3}\right) \equiv c$$

Thus the Most Powerful test rejects $H_0$ when $X < c$ (where $c > 0$). Let us compute the Type I error probability $\alpha$ and the power $\beta$ as functions of $c$:

$$\alpha = \mathbb{P}_0(X < c) = \int_0^c e^{-x} \, dx = 1 - e^{-c} \implies e^{-c} = 1 - \alpha \implies c = -\ln(1 - \alpha)$$

$$\beta = \mathbb{P}_1(X < c) = \int_0^c 3 e^{-3x} \, dx = 1 - e^{-3c} = 1 - \left(e^{-c}\right)^3 = 1 - (1 - \alpha)^3$$

Consequently, the Type II error probability $\tilde{\beta}(\alpha) = 1 - \beta(\alpha)$ as an explicit function of $\alpha \in [0, 1]$ is:

$$\tilde{\beta}(\alpha) = (1 - \alpha)^3$$

Notice that for all $\alpha \in (0, 1)$, $\beta(\alpha) = 1 - (1 - \alpha)^3 > 1 - (1 - \alpha) = \alpha$, confirming strict unbiasedness.

### Solution, step 2: Derivation of the optimal Bayes test and minimum Bayes risk
For prior probabilities $\pi_0 = 0.75$ and $\pi_1 = 0.25$ and unit losses $c_{\text{I}} = c_{\text{II}} = 1$, the Bayes test rejects $H_0$ whenever the likelihood ratio exceeds the prior-loss threshold:

$$\Lambda(x) = 3 e^{-2x} > k_{\text{Bayes}} = \frac{\pi_0 c_{\text{I}}}{\pi_1 c_{\text{II}}} = \frac{0.75 \times 1}{0.25 \times 1} = 3$$

Solving $3 e^{-2x} > 3$ for $x > 0$:

$$e^{-2x} > 1 \iff -2x > 0 \iff x < 0$$

Because the support of $X$ is $(0, \infty)$, the event $\{X < 0\}$ is the empty set ($c_{\text{Bayes}} = 0$)! This occurs because the maximum possible value of the likelihood ratio on $(0, \infty)$ is $\sup_{x > 0} 3 e^{-2x} = 3$, which never exceeds the threshold $k_{\text{Bayes}} = 3$. Therefore, the optimal Bayes test never rejects $H_0$ ($\phi_{\text{Bayes}}(x) \equiv 0$), yielding:

$$\alpha_{\text{Bayes}} = 0, \quad \tilde{\beta}_{\text{Bayes}} = (1 - 0)^3 = 1, \quad r^*(\pi) = \pi_0(0) + \pi_1(1) = 0.2500$$

### Solution, step 3: Derivation of the exact Minimax test via the equalizer condition
Under 0-1 loss, the maximum risk of a test with error probabilities $(\alpha, \tilde{\beta}(\alpha))$ is $\max\left(\alpha, (1 - \alpha)^3\right)$. Because $\alpha$ is strictly increasing on $[0, 1]$ from $0$ to $1$ while $\tilde{\beta}(\alpha) = (1 - \alpha)^3$ is strictly decreasing on $[0, 1]$ from $1$ to $0$, the minimax test occurs at the unique **equalizer point** where Type I error equals Type II error:

$$\alpha = (1 - \alpha)^3$$

Let $u = 1 - \alpha \in (0, 1)$, so $\alpha = 1 - u$. The equalizer equation becomes the depressed cubic:

$$u^3 + u - 1 = 0$$

Applying Cardano's cubic formula for $u^3 + pu + q = 0$ with $p = 1$ and $q = -1$, the discriminant is $\Delta = (q/2)^2 + (p/3)^3 = \frac{1}{4} + \frac{1}{27} = \frac{31}{108} > 0$, giving the unique real root:

$$u = \left(\frac{1}{2} + \sqrt{\frac{31}{108}}\right)^{1/3} + \left(\frac{1}{2} - \sqrt{\frac{31}{108}}\right)^{1/3} \approx (0.5 + 0.535759)^{1/3} + (0.5 - 0.535759)^{1/3} \approx 1.011780 - 0.329450 = 0.682328$$

Therefore, the minimax error rate (minimax risk) is:

$$\alpha_{\text{mm}} = \tilde{\beta}_{\text{mm}} = 1 - u \approx 1 - 0.682328 = 0.317672 \quad (31.77\%)$$

and the minimax critical cutoff is $c_{\text{mm}} = -\ln(1 - \alpha_{\text{mm}}) = -\ln(u) = -\ln(0.682328) \approx 0.382245$, so the minimax rule rejects $H_0$ if and only if $X < 0.3822$.

## Fully worked question 3: UMP Tests and Power Comparison in the Non-Regular Uniform Scale Family

### Question
Let $X_1, X_2, \dots, X_n \overset{\text{iid}}{\sim} \text{Uniform}(0, \theta)$ with $n = 5$ and unknown boundary parameter $\theta > 0$. Consider testing the null hypothesis $H_0 : \theta = \theta_0 = 2$ at significance level $\alpha = 0.05$.

1. Construct the Uniformly Most Powerful (UMP) level-$0.05$ test $\phi_1(\mathbf{X})$ for the one-sided alternative $H_1 : \theta > 2$ that has power $\beta_1(\theta)$ strictly maximized, and show why the test size condition $\mathbb{E}_{\theta_0}[\phi_1] = 0.05$ does not uniquely determine the critical region on $(0, 2]$ unless we require smoothness or test $H_0 : \theta \le 2$.
2. Construct the unique UMP level-$0.05$ test $\phi_{\text{UMP}}(\mathbf{X})$ for the composite null $H_0 : \theta \le 2$ versus $H_1 : \theta > 2$, derive its closed-form power function $\beta(\theta)$ across $\theta > 0$, and compute $\beta(2.5)$.
3. Construct the two-sided UMP size-$0.05$ test $\phi_{\text{two}}(\mathbf{X})$ for $H_0 : \theta = 2$ versus $H_1 : \theta \neq 2$, write down its explicit critical region for $n = 5$, and compute its power at $\theta = 1.5$ and $\theta = 2.5$.

### Solution, step 1: Likelihood ratio analysis for theta_1 > 2 and non-uniqueness under simple H0
The joint density of $X_1, \dots, X_5$ is $f_5(\mathbf{x}; \theta) = \theta^{-5} \mathbf{1}_{(0, \theta]}(x_{(5)})$ where $X_{(5)} = \max(X_1, \dots, X_5)$ is the sufficient statistic. Under any parameter $\theta > 0$, the cumulative distribution function and density of $T = X_{(5)}$ are:

$$F_T(t; \theta) = \left(\frac{t}{\theta}\right)^5, \quad f_T(t; \theta) = \frac{5 t^4}{\theta^5}, \quad 0 < t \le \theta$$

For testing $H_0 : \theta = 2$ against a specific $\theta_1 > 2$, the likelihood ratio in terms of $t = x_{(5)}$ is:

$$\Lambda(t) = \frac{f_T(t; \theta_1)}{f_T(t; 2)} = \begin{cases} (2 / \theta_1)^5, & 0 < t \le 2 \\ +\infty, & 2 < t \le \theta_1 \end{cases}$$

By the Neyman-Pearson Lemma, any Most Powerful test of size $\alpha = 0.05$ must set $\phi(t) = 1$ for $t > 2$ (where $\Lambda(t) = \infty$). However, on the interval $0 < t \le 2$, the likelihood ratio is identically equal to the constant $k = (2 / \theta_1)^5$! Therefore, for a *simple* null $H_0 : \theta = 2$ against $H_1 : \theta > 2$, *any* measurable subset $B \subset (0, 2]$ having null probability $\mathbb{P}_{\theta=2}(X_{(5)} \in B) = 0.05$ combined with $(2, \infty)$ yields the exact same power under $\theta_1 > 2$:

$$\beta(\theta_1) = \mathbb{P}_{\theta_1}(X_{(5)} > 2) + \mathbb{P}_{\theta_1}(X_{(5)} \in B) = \left[1 - \left(\frac{2}{\theta_1}\right)^5\right] + \left(\frac{2}{\theta_1}\right)^5 \mathbb{P}_2(X_{(5)} \in B) = 1 - 0.95 \left(\frac{2}{\theta_1}\right)^5$$

### Solution, step 2: Unique UMP test for composite H0: theta <= 2 versus H1: theta > 2
When the null hypothesis is the **composite** interval $H_0 : \theta \le 2$ versus $H_1 : \theta > 2$, the test must also satisfy the level constraint $\mathbb{P}_\theta(X_{(5)} \in \mathcal{C}) \le 0.05$ for all interior null values $\theta < 2$. To prevent $\mathbb{P}_\theta(X_{(5)} \in B)$ from exceeding $0.05$ when $\theta < 2$, the subset $B \subset (0, 2]$ must be placed at the **extreme upper end** of $(0, 2]$, namely $B = (c_1, 2]$, which gives the Karlin-Rubin upper-tail critical region:

$$\mathcal{C}_{\text{UMP}} = \left\{ \mathbf{x} : X_{(5)} > c_1 \right\}$$

Calibrating $c_1$ at the boundary $\theta_0 = 2$ for $\alpha = 0.05$ with $n = 5$:

$$\mathbb{P}_{\theta=2}(X_{(5)} > c_1) = 1 - \left(\frac{c_1}{2}\right)^5 = 0.05 \implies \left(\frac{c_1}{2}\right)^5 = 0.95 \implies c_1 = 2 (0.95)^{1/5} \approx 2(0.989794) = 1.9796$$

The complete power function of $\mathcal{C}_{\text{UMP}} = \{X_{(5)} > 1.9796\}$ across all $\theta > 0$ is:

$$\beta_{\text{UMP}}(\theta) = \begin{cases} 0, & \text{if } 0 < \theta \le 1.9796 \\ 1 - \left(\frac{1.9796}{\theta}\right)^5 = 1 - 0.95 \left(\frac{2}{\theta}\right)^5, & \text{if } \theta > 1.9796 \end{cases}$$

Notice that for all $\theta \le 2$, $\beta_{\text{UMP}}(\theta) \le 0.05$, and at $\theta = 2.5$ the exact power is:

$$\beta_{\text{UMP}}(2.5) = 1 - 0.95 \left(\frac{2.0}{2.5}\right)^5 = 1 - 0.95 (0.8)^5 = 1 - 0.95(0.32768) = 1 - 0.311296 = 0.688704 \quad (68.87\%)$$

### Solution, step 3: Two-sided UMP test for H0: theta = 2 versus H1: theta != 2
For the two-sided problem $H_0 : \theta = 2$ versus $H_1 : \theta \neq 2$, as proven in Section 2.6, we place the zero-cost region $(2, \infty)$ in the right tail and concentrate the entire $\alpha = 0.05$ budget at the leftmost end $(0, c_2]$ of $(0, 2]$:

$$\mathbb{P}_{\theta=2}(X_{(5)} \le c_2) = \left(\frac{c_2}{2}\right)^5 = 0.05 \implies c_2 = 2 (0.05)^{1/5} \approx 2(0.549280) = 1.0986$$

Thus the unique two-sided UMP critical region is:

$$\mathcal{C}_{\text{two}} = \left\{ \mathbf{x} : X_{(5)} \le 1.0986 \;\text{ or }\; X_{(5)} > 2.0000 \right\}$$

Let us evaluate the power of $\mathcal{C}_{\text{two}}$ at $\theta = 1.5$ and $\theta = 2.5$:
- At $\theta = 1.5$ (where $1.0986 < 1.5 < 2.0$), $\mathbb{P}_{1.5}(X_{(5)} > 2.0) = 0$, so:
  $$\beta_{\text{two}}(1.5) = \mathbb{P}_{1.5}(X_{(5)} \le 1.0986) = \left(\frac{c_2}{1.5}\right)^5 = 0.05 \left(\frac{2.0}{1.5}\right)^5 = 0.05 \left(\frac{4}{3}\right)^5 = 0.05 \left(\frac{1024}{243}\right) \approx 0.210700 \quad (21.07\%)$$
- At $\theta = 2.5$ (where $\theta > 2.0$), both regions contribute:
  $$\beta_{\text{two}}(2.5) = \mathbb{P}_{2.5}(X_{(5)} \le 1.0986) + \mathbb{P}_{2.5}(X_{(5)} > 2.0) = 0.05 \left(\frac{2.0}{2.5}\right)^5 + \left[1 - \left(\frac{2.0}{2.5}\right)^5\right] = 1 - 0.95(0.8)^5 = 0.688704 \quad (68.87\%)$$

Remarkably, $\mathcal{C}_{\text{two}}$ achieves the exact same $68.87\%$ power at $\theta = 2.5$ as the one-sided UMP test while simultaneously achieving maximal $21.07\%$ power against the left-sided alternative $\theta = 1.5$!
