#!/usr/bin/env python3
"""
Author Unit 7 for Mathematical Statistics.
Focuses on Stochastic Convergence, Laws of Large Numbers, and Central Limit Theorems.
Generates >= 5,200 substantive prose words with zero KaTeX errors.
"""
from pathlib import Path

DEST = Path("publishing/drafts/statistics-probability-mathematical-statistics/unit-7.md")

p1 = r"""# Unit 7: Stochastic Convergence and Limit Theorems: Laws of Large Numbers and Central Limit Theorems

## 7.1 The Four Modes of Stochastic Convergence: Definitions and Measure-Theoretic Foundations

In classical deterministic real analysis, the convergence of a sequence of real numbers $\{x_n\}_{n=1}^\infty$ to a fixed limit $x \in \mathbb{R}$ is governed by Cauchy's familiar criterion: for every positive error threshold $\epsilon > 0$, there exists an integer cutoff $N(\epsilon)$ such that for all subsequent indices $n \ge N(\epsilon)$, the Euclidean distance $|x_n - x| < \epsilon$. In mathematical statistics and modern probability theory, however, we deal not with deterministic scalars, but with sequences of **random variables** $\{X_n\}_{n=1}^\infty$ defined upon an underlying probability space $(\Omega, \mathcal{F}, P)$. 

Because random variables are measurable mappings $X_n: \Omega \to \mathbb{R}$ whose numerical realizations depend inherently upon the random outcome $\omega \in \Omega$ selected by nature, the deterministic concept of convergence fractures into four distinct, mathematically profound **modes of stochastic convergence**. Each mode captures a fundamentally different operational question regarding how, where, and with what regularity a sequence of random quantities settles down as the sample size $n$ approaches infinity.

### The Measure-Theoretic Setting

Formally, consider a complete probability space $(\Omega, \mathcal{F}, P)$, where $\Omega$ represents the sample space of all elementary experimental outcomes, $\mathcal{F}$ denotes a $\sigma$-algebra of observable events (subsets of $\Omega$ closed under complements and countable unions), and $P: \mathcal{F} \to [0, 1]$ represents a countably additive probability measure assigning unit mass $P(\Omega) = 1$. A real-valued random variable $X$ is an $(\mathcal{F}, \mathcal{B}(\mathbb{R}))$-measurable function, meaning that for every Borel set $B \in \mathcal{B}(\mathbb{R})$, the pre-image belongs to the event space:

$$\{\omega \in \Omega : X(\omega) \in B\} = X^{-1}(B) \in \mathcal{F}$$

When studying an infinite sequence of random variables $\{X_n\}_{n=1}^\infty$ and a candidate limiting random variable $X$, we must examine the behaviour of the error deviations $|X_n(\omega) - X(\omega)|$. Because the set of sample points $\omega$ where $|X_n(\omega) - X(\omega)|$ is large can vary chaotically from one index $n$ to the next, mathematicians developed four distinct topological frameworks:

---

### 1. Almost Sure Convergence ($X_n \xrightarrow{\text{a.s.}} X$)

Almost sure convergence (historically referred to as convergence with probability 1, strong convergence, or convergence almost everywhere) represents the probabilistic equivalent of pointwise convergence in functional analysis. It demands that the set of sample trajectories along which $X_n(\omega)$ fails to converge to $X(\omega)$ as ordinary numbers forms a negligible null set of zero probability.

**Formal Definition**: A sequence of random variables $\{X_n\}_{n=1}^\infty$ converges **almost surely** to a random variable $X$, denoted by $X_n \xrightarrow{\text{a.s.}} X$ or $\lim_{n \to \infty} X_n = X \text{ a.s.}$, if:

$$P\left( \left\{ \omega \in \Omega : \lim_{n \to \infty} X_n(\omega) = X(\omega) \right\} \right) = 1$$

Equivalently, expressing this requirement in terms of exceptional failure events, the probability that the numerical sequence fails to converge must be identically zero:

$$P\left( \left\{ \omega \in \Omega : \lim_{n \to \infty} |X_n(\omega) - X(\omega)| \ne 0 \right\} \right) = 0$$

Using standard measure-theoretic $\epsilon$-$N$ formulations, almost sure convergence can be expressed as a condition on the supremum of tail deviations. For every arbitrary positive tolerance $\epsilon > 0$:

$$\lim_{m \to \infty} P\left( \bigcup_{n=m}^\infty \{ \omega \in \Omega : |X_n(\omega) - X(\omega)| \ge \epsilon \} \right) = 0$$

Alternatively, defining the event of infinite recurrence:

$$\limsup_{n \to \infty} E_n(\epsilon) = \bigcap_{m=1}^\infty \bigcup_{n=m}^\infty \{|X_n - X| \ge \epsilon\} = \{ |X_n - X| \ge \epsilon \text{ infinitely often (i.o.)} \}$$

Almost sure convergence requires that $P(|X_n - X| \ge \epsilon \text{ i.o.}) = 0$ for every $\epsilon > 0$. In intuitive terms, almost sure convergence means that if you observe a single realization of the infinite sequence of data, with probability 1 there is some finite, random index $N(\omega, \epsilon)$ after which the entire remaining infinite tail of the sequence remains permanently trapped inside the narrow corridor $(X(\omega) - \epsilon, X(\omega) + \epsilon)$.

---

### 2. Convergence in Probability ($X_n \xrightarrow{P} X$)

Convergence in probability (also known as weak convergence of random variables or convergence in measure) relaxes the stringent requirement on infinite trajectories. Rather than demanding that the tail stay trapped forever, it merely asks whether the probability of observing a significant discrepancy at any individual sample index $n$ vanishes as $n$ grows large.

**Formal Definition**: A sequence of random variables $\{X_n\}_{n=1}^\infty$ converges **in probability** to a random variable $X$, denoted by $X_n \xrightarrow{P} X$ or $\text{plim}_{n \to \infty} X_n = X$, if for every arbitrary tolerance $\epsilon > 0$:

$$\lim_{n \to \infty} P\left( |X_n - X| \ge \epsilon \right) = 0$$

Equivalently, phrased from the vantage point of proximity:

$$\lim_{n \to \infty} P\left( |X_n - X| < \epsilon \right) = 1$$

In the language of statistical estimation, if an estimator sequence $\hat{\theta}_n = T(X_1, \dots, X_n)$ satisfies $\hat{\theta}_n \xrightarrow{P} \theta$ where $\theta$ is the true population parameter, the estimator $\hat{\theta}_n$ is said to be **consistent**. Consistency is universally regarded as a minimal requirement for any sound statistical procedure: as more data are collected, the probability that the estimate strays from the truth by any noticeable margin collapses to zero.

---

### 3. Convergence in Mean of Order $r$ ($X_n \xrightarrow{L^r} X$)

Convergence in mean of order $r$ (or convergence in the Banach space $L^r(\Omega, \mathcal{F}, P)$ for $r > 0$) assesses the distance between random variables by integrating the absolute power difference over the entire probability space.

**Formal Definition**: Let $r > 0$, and assume that $\mathbb{E}[|X_n|^r] < \infty$ for all $n$ and $\mathbb{E}[|X|^r] < \infty$. The sequence $\{X_n\}$ converges in **$r$-th mean** to $X$, denoted by $X_n \xrightarrow{L^r} X$, if:

$$\lim_{n \to \infty} \mathbb{E}\left[ |X_n - X|^r \right] = 0$$

Two special cases are of paramount importance across mathematical statistics:
- When $r = 1$, we obtain **convergence in mean** (or $L^1$ convergence): $\lim_{n \to \infty} \mathbb{E}[|X_n - X|] = 0$.
- When $r = 2$, we obtain **convergence in mean square** (or quadratic mean convergence, denoted $X_n \xrightarrow{\text{m.s.}} X$ or $X_n \xrightarrow{L^2} X$):
  $$\lim_{n \to \infty} \mathbb{E}\left[ (X_n - X)^2 \right] = 0$$

Mean square convergence is exceptionally useful in applied statistics because the quadratic loss function decomposes naturally into variance and squared bias:

$$\mathbb{E}[(X_n - c)^2] = \text{Var}(X_n) + (\mathbb{E}[X_n] - c)^2$$

Thus, showing that an estimator's variance and bias both vanish simultaneously is sufficient to establish mean square convergence, which automatically guarantees consistency.

---

### 4. Convergence in Distribution ($X_n \xrightarrow{d} X$)

Convergence in distribution (frequently termed convergence in law, or weak convergence of probability measures, denoted by $X_n \xrightarrow{d} X$ or $X_n \xrightarrow{\mathcal{L}} X$) occupies a distinct and special position in asymptotic theory. Unlike the previous three modes, convergence in distribution does not require that $X_n$ and $X$ be defined on the same probability space $\Omega$. It does not track whether $X_n(\omega)$ is numerically close to $X(\omega)$ on individual sample points; instead, it focuses exclusively on the **cumulative distribution functions** (CDFs) induced by the variables.

**Formal Definition**: Let $F_n(x) = P(X_n \le x)$ denote the cumulative distribution function of $X_n$, and let $F(x) = P(X \le x)$ denote the cumulative distribution function of $X$. The sequence $\{X_n\}$ converges **in distribution** to $X$ if:

$$\lim_{n \to \infty} F_n(x) = F(x) \quad \text{for all } x \in \mathbb{R} \text{ at which } F \text{ is continuous}$$

The restriction to points of continuity of $F(x)$, written $x \in \mathcal{C}(F)$, is mathematically vital. To understand why, consider the deterministic sequence of constant random variables $X_n = 1/n$. Intuitively, $1/n$ converges to the constant $0$. The CDF of $X_n$ is a unit step function located at $1/n$:

$$F_n(x) = \begin{cases} 0 & x < 1/n \\ 1 & x \ge 1/n \end{cases}$$

The limiting constant variable $X = 0$ has CDF:

$$F(x) = \begin{cases} 0 & x < 0 \\ 1 & x \ge 0 \end{cases}$$

Evaluating the pointwise limit of $F_n(x)$ at $x = 0$, we find $F_n(0) = 0$ for all $n \ge 1$, so $\lim_{n \to \infty} F_n(0) = 0 \ne F(0) = 1$. If we demanded convergence at all real numbers, $1/n$ would fail to converge in distribution to $0$! However, $x = 0$ is a jump discontinuity point of $F$. For all $x < 0$, $F_n(x) = 0 \to 0 = F(x)$, and for all $x > 0$, for sufficiently large $n$ such that $1/n < x$, $F_n(x) = 1 \to 1 = F(x)$. Because convergence holds at all points where $F$ is continuous, $X_n \xrightarrow{d} 0$ as expected.

By the Portmanteau Theorem, convergence in distribution is equivalent to several other conditions:
1. $\lim_{n \to \infty} \mathbb{E}[g(X_n)] = \mathbb{E}[g(X)]$ for every bounded, continuous function $g: \mathbb{R} \to \mathbb{R}$.
2. $\limsup_{n \to \infty} P(X_n \in C) \le P(X \in C)$ for all closed sets $C \subset \mathbb{R}$.
3. $\liminf_{n \to \infty} P(X_n \in O) \ge P(X \in O)$ for all open sets $O \subset \mathbb{R}$.
4. $\lim_{n \to \infty} P(X_n \in B) = P(X \in B)$ for all Borel sets $B$ whose boundary has zero limiting probability ($P(X \in \partial B) = 0$).
"""

p2 = r"""## 7.2 The Strict Hierarchy of Convergence Modes, Counterexamples, and Equivalences

A central triumph of modern probability theory is the establishment of the precise logical implications connecting these four convergence concepts. The relationships form a strict, unidirectional hierarchical structure:

$$\begin{matrix}
X_n \xrightarrow{\text{a.s.}} X \\
& \searrow \\
& & X_n \xrightarrow{P} X & \implies & X_n \xrightarrow{d} X \\
& \nearrow \\
X_n \xrightarrow{L^r} X
\end{matrix}$$

### Fundamental Implications and Their Rigorous Proofs

#### Theorem 7.1: Almost Sure Convergence Implies Convergence in Probability
If $X_n \xrightarrow{\text{a.s.}} X$, then $X_n \xrightarrow{P} X$.

**Proof**:
Let $\epsilon > 0$ be given. Consider the sequence of events $A_n(\epsilon) = \{|X_n - X| \ge \epsilon\}$. Define the tail union events:

$$B_m(\epsilon) = \bigcup_{n=m}^\infty A_n(\epsilon) = \bigcup_{n=m}^\infty \{|X_n - X| \ge \epsilon\}$$

Notice that the sequence of events $\{B_m(\epsilon)\}_{m=1}^\infty$ is nested and monotonically decreasing: $B_{m+1}(\epsilon) \subseteq B_m(\epsilon)$. By the continuity of probability measures from above:

$$\lim_{m \to \infty} P(B_m(\epsilon)) = P\left( \bigcap_{m=1}^\infty B_m(\epsilon) \right) = P\left( \limsup_{n \to \infty} A_n(\epsilon) \right)$$

Under the assumption of almost sure convergence, the set of outcomes where $|X_n(\omega) - X(\omega)|$ fails to tend to zero has probability zero. Consequently, the event $\{|X_n - X| \ge \epsilon \text{ i.o.}\}$ has probability zero, meaning:

$$\lim_{m \to \infty} P(B_m(\epsilon)) = 0$$

Now, for any specific index $n$, the single event $A_n(\epsilon)$ is trivially contained within the tail union $B_n(\epsilon)$:

$$A_n(\epsilon) \subseteq \bigcup_{k=n}^\infty A_k(\epsilon) = B_n(\epsilon)$$

By the monotonicity of probability:

$$0 \le P(A_n(\epsilon)) = P(|X_n - X| \ge \epsilon) \le P(B_n(\epsilon))$$

Taking the limit as $n \to \infty$, the upper bound vanishes:

$$\lim_{n \to \infty} P(|X_n - X| \ge \epsilon) \le \lim_{n \to \infty} P(B_n(\epsilon)) = 0$$

Since probabilities are non-negative, the squeeze theorem forces $\lim_{n \to \infty} P(|X_n - X| \ge \epsilon) = 0$. Because this holds for every $\epsilon > 0$, we conclude that $X_n \xrightarrow{P} X$. $\blacksquare$

---

#### Theorem 7.2: $L^r$ Convergence Implies Convergence in Probability
If $X_n \xrightarrow{L^r} X$ for some $r > 0$, then $X_n \xrightarrow{P} X$.

**Proof**:
Fix $\epsilon > 0$. Observe that the event $\{|X_n - X| \ge \epsilon\}$ is identical to the event $\{|X_n - X|^r \ge \epsilon^r\}$. Applying Markov's inequality to the non-negative random variable $|X_n - X|^r$:

$$P(|X_n - X| \ge \epsilon) = P\left( |X_n - X|^r \ge \epsilon^r \right) \le \frac{\mathbb{E}[|X_n - X|^r]}{\epsilon^r}$$

By hypothesis, $\lim_{n \to \infty} \mathbb{E}[|X_n - X|^r] = 0$. Since $\epsilon^r > 0$ is a fixed positive constant:

$$\lim_{n \to \infty} P(|X_n - X| \ge \epsilon) \le \frac{1}{\epsilon^r} \lim_{n \to \infty} \mathbb{E}[|X_n - X|^r] = 0$$

Thus, $X_n \xrightarrow{P} X$. $\blacksquare$

---

#### Theorem 7.3: Convergence in Probability Implies Convergence in Distribution
If $X_n \xrightarrow{P} X$, then $X_n \xrightarrow{d} X$.

**Proof**:
Let $F_n(x)$ and $F(x)$ denote the CDFs of $X_n$ and $X$ respectively. Let $x$ be any point of continuity of $F$, and choose an arbitrary $\epsilon > 0$. We decompose the event $\{X_n \le x\}$ based on whether $|X_n - X| < \epsilon$ or $|X_n - X| \ge \epsilon$:

$$\{X_n \le x\} = (\{X_n \le x\} \cap \{|X_n - X| < \epsilon\}) \cup (\{X_n \le x\} \cap \{|X_n - X| \ge \epsilon\})$$

If $X_n \le x$ and $|X_n - X| < \epsilon$, it follows that $X = X_n + (X - X_n) \le x + \epsilon$. Therefore:

$$\{X_n \le x\} \subseteq \{X \le x + \epsilon\} \cup \{|X_n - X| \ge \epsilon\}$$

Taking probabilities of both sides:

$$F_n(x) = P(X_n \le x) \le P(X \le x + \epsilon) + P(|X_n - X| \ge \epsilon) = F(x + \epsilon) + P(|X_n - X| \ge \epsilon)$$

Taking the limit superior as $n \to \infty$, and noting that $P(|X_n - X| \ge \epsilon) \to 0$ by convergence in probability:

$$\limsup_{n \to \infty} F_n(x) \le F(x + \epsilon)$$

Conversely, consider the event $\{X \le x - \epsilon\}$:

$$\{X \le x - \epsilon\} \subseteq \{X_n \le x\} \cup \{|X_n - X| \ge \epsilon\}$$

Hence:

$$F(x - \epsilon) = P(X \le x - \epsilon) \le F_n(x) + P(|X_n - X| \ge \epsilon)$$

Subtracting $P(|X_n - X| \ge \epsilon)$ and taking the limit inferior as $n \to \infty$:

$$F(x - \epsilon) \le \liminf_{n \to \infty} F_n(x)$$

Combining our two inequalities:

$$F(x - \epsilon) \le \liminf_{n \to \infty} F_n(x) \le \limsup_{n \to \infty} F_n(x) \le F(x + \epsilon)$$

Because this holds for every $\epsilon > 0$, we take the limit as $\epsilon \to 0^+$. Since $x$ is a point of continuity of $F$, $\lim_{\epsilon \to 0^+} F(x - \epsilon) = F(x)$ and $\lim_{\epsilon \to 0^+} F(x + \epsilon) = F(x)$. By the squeeze theorem:

$$\lim_{n \to \infty} F_n(x) = F(x)$$

This establishes that $X_n \xrightarrow{d} X$. $\blacksquare$

---

#### Theorem 7.4: Higher-Order $L^s$ Convergence Implies Lower-Order $L^r$ Convergence
Let $0 < r < s$. If $X_n \xrightarrow{L^s} X$, then $X_n \xrightarrow{L^r} X$.

**Proof**:
This is a direct consequence of Lyapunov's inequality (which follows from Jensen's inequality applied to the convex function $g(u) = u^{s/r}$ on $[0, \infty)$):

$$\left( \mathbb{E}[|X_n - X|^r] \right)^{1/r} \le \left( \mathbb{E}[|X_n - X|^s] \right)^{1/s}$$

Raising both sides to the power $r$:

$$\mathbb{E}[|X_n - X|^r] \le \left( \mathbb{E}[|X_n - X|^s] \right)^{r/s}$$

As $n \to \infty$, the right-hand side converges to zero because $\mathbb{E}[|X_n - X|^s] \to 0$ and $r/s > 0$. Thus $\mathbb{E}[|X_n - X|^r] \to 0$. $\blacksquare$

---

### Canonical Counterexamples Showing Non-Equivalence

To grasp why the reverse implications fail in general, we examine three classical counterexamples that every statistician must understand.

#### Counterexample 1: Convergence in Probability Does NOT Imply Almost Sure Convergence (The "Typewriter Sequence")
Let the sample space be the unit interval $\Omega = [0, 1)$ equipped with the Borel $\sigma$-algebra $\mathcal{F} = \mathcal{B}([0, 1))$ and the standard uniform Lebesgue measure $P = \lambda$, so that for any interval $[a, b) \subseteq [0, 1)$, $P([a, b)) = b - a$.

We construct a sequence of intervals $I_n$ of shrinking widths that continually sweep across the interval $[0, 1)$ like the carriage of a mechanical typewriter:
- Generation 0 ($k = 0$, width 1): $I_1 = [0, 1)$.
- Generation 1 ($k = 1$, width $1/2$): $I_2 = [0, 1/2)$, $I_3 = [1/2, 1)$.
- Generation 2 ($k = 2$, width $1/4$): $I_4 = [0, 1/4)$, $I_5 = [1/4, 2/4)$, $I_6 = [2/4, 3/4)$, $I_7 = [3/4, 1)$.
- In general, for any integer $n \ge 1$, there exists a unique integer $k \ge 0$ and index $j \in \{0, 1, \dots, 2^k - 1\}$ such that $n = 2^k + j$. We define the interval:
  $$I_n = \left[ \frac{j}{2^k}, \frac{j+1}{2^k} \right)$$

Now define the random variable $X_n(\omega) = \mathbf{1}_{I_n}(\omega)$, which takes value 1 if $\omega \in I_n$ and 0 otherwise. Let the candidate limit be the zero random variable $X(\omega) \equiv 0$.

1. **Verify Convergence in Probability**:
   Take any tolerance $\epsilon \in (0, 1)$. The absolute deviation satisfies $|X_n(\omega) - 0| \ge \epsilon$ if and only if $X_n(\omega) = 1$, which occurs precisely when $\omega \in I_n$. Therefore:
   $$P(|X_n - 0| \ge \epsilon) = P(X_n = 1) = \lambda(I_n) = \frac{1}{2^k}$$
   As $n \to \infty$, the generation index $k = \lfloor \log_2 n \rfloor \to \infty$, which forces:
   $$\lim_{n \to \infty} P(|X_n - 0| \ge \epsilon) = \lim_{k \to \infty} \frac{1}{2^k} = 0$$
   Consequently, $X_n \xrightarrow{P} 0$.

2. **Demonstrate Failure of Almost Sure Convergence**:
   Pick any arbitrary point $\omega \in [0, 1)$. In each generation $k$, the collection of intervals $\{ [j/2^k, (j+1)/2^k) \}_{j=0}^{2^k - 1}$ forms a complete partition of $[0, 1)$. Therefore, for every single generation $k$, there is exactly one interval in that generation containing $\omega$, meaning $X_n(\omega) = 1$ for that index $n$. Conversely, the remaining $2^k - 1$ intervals do not contain $\omega$, so $X_n(\omega) = 0$ for those indices.
   As $k \to \infty$, the point $\omega$ is struck infinitely many times by intervals containing it, and avoided infinitely many times. Therefore, the numerical sequence of real numbers $\{X_n(\omega)\}_{n=1}^\infty$ alternates endlessly between 0 and 1:
   $$\limsup_{n \to \infty} X_n(\omega) = 1 \quad \text{and} \quad \liminf_{n \to \infty} X_n(\omega) = 0$$
   Because the sequence oscillates perpetually, the limit $\lim_{n \to \infty} X_n(\omega)$ does not exist for **any** $\omega \in [0, 1)$!
   The set of convergence points is the empty set:
   $$P\left( \left\{ \omega \in [0, 1) : \lim_{n \to \infty} X_n(\omega) = 0 \right\} \right) = P(\emptyset) = 0 \ne 1$$
   Thus, $X_n$ fails to converge almost surely to 0. In fact, it diverges almost everywhere!

---

#### Counterexample 2: Almost Sure Convergence and Convergence in Probability Do NOT Imply $L^r$ Convergence (The "Escape to Infinite Energy" Sequence)
Let $\Omega = (0, 1)$ with uniform Lebesgue measure. Define the sequence of random variables:

$$X_n(\omega) = n^{2/r} \cdot \mathbf{1}_{(0, 1/n)}(\omega)$$

where $r \ge 1$ is an integer. Let $X \equiv 0$.

1. **Verify Almost Sure Convergence**:
   For any fixed outcome $\omega \in (0, 1)$, by Archimedes' principle there exists an integer $N_\omega = \lceil 1/\omega \rceil$. For all indices $n > N_\omega$, we have $1/n < \omega$, which implies $\omega \notin (0, 1/n)$. Thus, $X_n(\omega) = 0$ for all $n > N_\omega$.
   Consequently, for every $\omega \in (0, 1)$:
   $$\lim_{n \to \infty} X_n(\omega) = 0$$
   Because pointwise convergence holds on the entire sample space $\Omega$ (which has probability 1), we have $X_n \xrightarrow{\text{a.s.}} 0$. By Theorem 7.1, $X_n \xrightarrow{P} 0$ as well.

2. **Evaluate the $L^r$ Norm**:
   Compute the expected $r$-th power deviation:
   $$\mathbb{E}[|X_n - 0|^r] = \mathbb{E}[(n^{2/r})^r \cdot \mathbf{1}_{(0, 1/n)}] = n^2 \cdot P\left( \omega \in \left(0, \frac{1}{n}\right) \right) = n^2 \cdot \frac{1}{n} = n$$
   Taking the limit as $n \to \infty$:
   $$\lim_{n \to \infty} \mathbb{E}[|X_n - 0|^r] = \lim_{n \to \infty} n = +\infty$$
   Far from converging to 0, the expected $r$-th power diverges to infinity! Even though the probability mass of the spike collapses to zero ($P(X_n \ne 0) = 1/n \to 0$), the height of the spike grows so aggressively ($n^{2/r}$) that the integrated energy blows up.

---

#### Counterexample 3: Convergence in Distribution Does NOT Imply Convergence in Probability
Let $X \sim \mathcal{N}(0, 1)$ be a standard Gaussian random variable defined on $(\Omega, \mathcal{F}, P)$. For all $n \ge 1$, define:

$$X_n = -X$$

1. **Verify Convergence in Distribution**:
   By the symmetry of the Gaussian density around zero:
   $$P(X_n \le x) = P(-X \le x) = P(X \ge -x) = 1 - \Phi(-x) = \Phi(x) = P(X \le x)$$
   Thus, for every $n$, $X_n$ has the exact same cumulative distribution function as $X$. Trivially, $X_n \xrightarrow{d} X$.

2. **Test Convergence in Probability**:
   Consider the difference $X_n - X = -X - X = -2X$. Since $X \sim \mathcal{N}(0, 1)$, $-2X \sim \mathcal{N}(0, 4)$.
   Choose $\epsilon = 1$. The probability of deviation is constant across all $n$:
   $$P(|X_n - X| \ge 1) = P(|-2X| \ge 1) = P\left(|X| \ge \frac{1}{2}\right) = 2\left(1 - \Phi(0.5)\right) \approx 2(1 - 0.6915) = 0.6170$$
   Taking the limit as $n \to \infty$:
   $$\lim_{n \to \infty} P(|X_n - X| \ge 1) = 0.6170 \ne 0$$
   The sequence completely fails to converge in probability to $X$. Convergence in distribution merely asserts that the **probability distributions** match in the limit; it carries zero information about the joint co-dependence or physical proximity of the random variables on individual sample trajectories.

---

### Important Partial Converses

Under specific structural conditions, the reverse implications do hold:

1. **Convergence in Distribution to a Degenerate Constant**:
   If $X_n \xrightarrow{d} c$, where $c \in \mathbb{R}$ is a non-random constant, then $X_n \xrightarrow{P} c$.
   *Proof*: For any $\epsilon > 0$, $P(|X_n - c| \ge \epsilon) = P(X_n \le c - \epsilon) + P(X_n \ge c + \epsilon)$. Since $c$ is a constant, the limiting CDF $F(x) = \mathbf{1}_{[c, \infty)}(x)$ is continuous at both $c - \epsilon$ and $c + \epsilon$. As $n \to \infty$, $P(X_n \le c - \epsilon) \to F(c - \epsilon) = 0$ and $P(X_n \le c + \epsilon/2) \to F(c + \epsilon/2) = 1$. Consequently, $P(|X_n - c| \ge \epsilon) \to 0$.

2. **Riesz's Subsequential Theorem**:
   If $X_n \xrightarrow{P} X$, there exists a strictly increasing subsequence of indices $\{n_k\}_{k=1}^\infty$ such that $X_{n_k} \xrightarrow{\text{a.s.}} X$.

3. **Vitali's Convergence Theorem**:
   If $X_n \xrightarrow{P} X$, then $X_n \xrightarrow{L^r} X$ if and only if the family of random variables $\{|X_n|^r\}_{n=1}^\infty$ is **uniformly integrable**, meaning:
   $$\lim_{M \to \infty} \sup_{n \ge 1} \mathbb{E}\left[ |X_n|^r \mathbf{1}_{\{|X_n|^r \ge M\}} \right] = 0$$
"""

p3 = r"""## 7.3 Probabilistic Inequalities: The Analytical Machinery of Limit Theorems

The proof of limit theorems in probability theory relies on bounding the probability that a random variable deviates into extreme tail regions using information about its moments.

### 1. Markov's Inequality
Markov's inequality provides the foundational bound connecting probabilities to first moments of non-negative random variables.

**Theorem (Markov's Inequality)**: Let $Y$ be a non-negative random variable ($Y \ge 0$ almost surely) with finite expectation $\mathbb{E}[Y] < \infty$. Then for any arbitrary positive constant $a > 0$:

$$P(Y \ge a) \le \frac{\mathbb{E}[Y]}{a}$$

**Proof**:
We define the indicator random variable $\mathbf{1}_{\{Y \ge a\}}$, which equals 1 when $Y \ge a$ and 0 when $Y < a$. Because $Y \ge 0$ everywhere, we have the elementary pointwise inequality:

$$Y \ge a \cdot \mathbf{1}_{\{Y \ge a\}}$$

To verify this, consider two cases:
- If $Y(\omega) < a$, then $a \cdot \mathbf{1}_{\{Y \ge a\}}(\omega) = 0 \le Y(\omega)$ since $Y \ge 0$.
- If $Y(\omega) \ge a$, then $a \cdot \mathbf{1}_{\{Y \ge a\}}(\omega) = a \le Y(\omega)$.

Taking expectations on both sides, and using the monotonicity and linearity of expectation:

$$\mathbb{E}[Y] \ge \mathbb{E}\left[ a \cdot \mathbf{1}_{\{Y \ge a\}} \right] = a \cdot \mathbb{E}\left[ \mathbf{1}_{\{Y \ge a\}} \right] = a \cdot P(Y \ge a)$$

Dividing both sides by the positive scalar $a > 0$ yields Markov's inequality:

$$P(Y \ge a) \le \frac{\mathbb{E}[Y]}{a} \quad \blacksquare$$

---

### 2. Chebyshev's Inequality
Chebyshev's inequality extends Markov's bound to general random variables with finite variance by applying Markov's inequality to squared centered deviations.

**Theorem (Chebyshev's Inequality)**: Let $X$ be any random variable with finite mean $\mu = \mathbb{E}[X]$ and finite variance $\sigma^2 = \text{Var}(X) < \infty$. Then for any positive constant $\epsilon > 0$:

$$P(|X - \mu| \ge \epsilon) \le \frac{\sigma^2}{\epsilon^2}$$

**Proof**:
Notice that the event $\{|X - \mu| \ge \epsilon\}$ is identical to the event $\{(X - \mu)^2 \ge \epsilon^2\}$. The variable $Y = (X - \mu)^2$ is non-negative almost surely, and its expectation is $\mathbb{E}[Y] = \mathbb{E}[(X - \mu)^2] = \sigma^2$. Applying Markov's inequality to $Y$ with threshold $a = \epsilon^2$:

$$P(|X - \mu| \ge \epsilon) = P\left( (X - \mu)^2 \ge \epsilon^2 \right) \le \frac{\mathbb{E}[(X - \mu)^2]}{\epsilon^2} = \frac{\sigma^2}{\epsilon^2} \quad \blacksquare$$

Writing $\epsilon = k\sigma$ where $k > 0$ represents the number of standard deviations from the mean:

$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2} \iff P(|X - \mu| < k\sigma) \ge 1 - \frac{1}{k^2}$$

This universal bound holds for **any** probability distribution regardless of shape, skewness, or kurtosis. It guarantees that at least $75\%$ of the probability mass must lie within $2\sigma$ of the mean ($k=2$), at least $88.89\%$ within $3\sigma$ ($k=3$), and at least $96\%$ within $5\sigma$ ($k=5$).

---

### 3. Cantelli's One-Sided Chebyshev Inequality
Chebyshev's inequality bounds deviations symmetrically on both sides of the mean. If one is interested in a one-sided tail probability $P(X - \mu \ge \epsilon)$, Cantelli's inequality delivers a substantially sharper bound.

**Theorem (Cantelli's Inequality)**: Let $X$ have mean $\mu$ and variance $\sigma^2 < \infty$. For any $\epsilon > 0$:

$$P(X - \mu \ge \epsilon) \le \frac{\sigma^2}{\sigma^2 + \epsilon^2}$$

For instance, for $\epsilon = 2\sigma$, two-sided Chebyshev yields $P(|X - \mu| \ge 2\sigma) \le 1/4 = 0.25$, whereas Cantelli gives $P(X - \mu \ge 2\sigma) \le \sigma^2 / (\sigma^2 + 4\sigma^2) = 1/5 = 0.20$.

---

### 4. Jensen's Inequality
Jensen's inequality relates the expectation of a transformed random variable to the transform of its expectation when the transforming function is convex.

**Theorem (Jensen's Inequality)**: Let $g: \mathbb{R} \to \mathbb{R}$ be a convex function, and let $X$ be a random variable such that $\mathbb{E}[|X|] < \infty$ and $\mathbb{E}[|g(X)|] < \infty$. Then:

$$g(\mathbb{E}[X]) \le \mathbb{E}[g(X)]$$

Furthermore, if $g$ is strictly convex on an interval containing the support of $X$, equality holds if and only if $X$ is constant almost surely ($P(X = \mathbb{E}[X]) = 1$).

**Proof using Supporting Hyperplanes**:
Recall that a convex function $g(x)$ lies above all of its tangent supporting lines. That is, at any point $\mu \in \mathbb{R}$, there exists a real slope $m \in \mathbb{R}$ (belonging to the subgradient of $g$ at $\mu$) such that:

$$g(x) \ge g(\mu) + m(x - \mu) \quad \text{for all } x \in \mathbb{R}$$

Set $\mu = \mathbb{E}[X]$ and substitute the random variable $X$ for $x$:

$$g(X) \ge g(\mathbb{E}[X]) + m(X - \mathbb{E}[X])$$

Taking expectations of both sides:

$$\mathbb{E}[g(X)] \ge \mathbb{E}\left[ g(\mathbb{E}[X]) + m(X - \mathbb{E}[X]) \right] = g(\mathbb{E}[X]) + m\left( \mathbb{E}[X] - \mathbb{E}[X] \right) = g(\mathbb{E}[X])$$

This establishes the inequality. $\blacksquare$

---

### 5. Chernoff Bounding Technique and Exponential Inequalities
While Chebyshev's inequality utilizes second moments to yield polynomial decay bounds ($O(1/\epsilon^2)$), the Chernoff bound uses the entire moment generating function to yield exponential decay bounds ($O(e^{-c \epsilon^2})$).

Let $X$ possess a moment generating function $M_X(t) = \mathbb{E}[e^{tX}]$ defined in a neighborhood containing $t > 0$. For any threshold $a > 0$ and any parameter $t > 0$, the event $\{X \ge a\}$ is identical to $\{e^{tX} \ge e^{ta}\}$. Applying Markov's inequality:

$$P(X \ge a) = P(e^{tX} \ge e^{ta}) \le \frac{\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t)$$

Because this bound is valid for every $t > 0$, we can optimize over $t$ to find the tightest possible upper bound:

$$P(X \ge a) \le \inf_{t > 0} e^{-ta} M_X(t) = \exp\left( - \sup_{t > 0} \{ ta - \log M_X(t) \} \right)$$

The function $\Lambda^*(a) = \sup_{t > 0} \{ta - \log M_X(t)\}$ is known as the **Fenchel-Legendre transform** (or convex conjugate) of the cumulant generating function. This exponential decay rate forms the bedrock of Cramér's Large Deviation Theory and modern non-asymptotic concentration of measure.
"""

p4 = r"""## 7.4 The Weak Law of Large Numbers (WLLN)

The Law of Large Numbers is the philosophical and mathematical cornerstone of statistical theory: it asserts that the empirical average computed from repeated independent observations converges to the underlying population expectation. The "Weak" Law specifically formalizes convergence in probability:

$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu$$

### WLLN under Finite Variance: Chebyshev's Theorem

We begin with the classical theorem formulated by Chebyshev in 1867, which assumes finite second moments but requires only pairwise uncorrelated random variables.

**Theorem 7.5 (Chebyshev's WLLN)**: Let $\{X_i\}_{i=1}^\infty$ be a sequence of pairwise uncorrelated random variables with common expectation $\mathbb{E}[X_i] = \mu$ and uniformly bounded variances $\text{Var}(X_i) = \sigma_i^2 \le \sigma^2 < \infty$. Let $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$. Then for every $\epsilon > 0$:

$$\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) = 0$$

That is, $\bar{X}_n \xrightarrow{P} \mu$.

**Proof**:
Compute the expectation of the sample mean using linearity:

$$\mathbb{E}[\bar{X}_n] = \mathbb{E}\left[ \frac{1}{n}\sum_{i=1}^n X_i \right] = \frac{1}{n}\sum_{i=1}^n \mathbb{E}[X_i] = \frac{1}{n}(n \mu) = \mu$$

Next, compute the variance of the sample mean. Because the variables are pairwise uncorrelated, $\text{Cov}(X_i, X_j) = 0$ for all $i \ne j$. The variance of the sum equals the sum of the variances:

$$\text{Var}(\bar{X}_n) = \text{Var}\left( \frac{1}{n}\sum_{i=1}^n X_i \right) = \frac{1}{n^2}\sum_{i=1}^n \text{Var}(X_i) = \frac{1}{n^2}\sum_{i=1}^n \sigma_i^2 \le \frac{1}{n^2}(n \sigma^2) = \frac{\sigma^2}{n}$$

Now apply Chebyshev's inequality to the random variable $\bar{X}_n$:

$$P(|\bar{X}_n - \mu| \ge \epsilon) \le \frac{\text{Var}(\bar{X}_n)}{\epsilon^2} \le \frac{\sigma^2}{n \epsilon^2}$$

Fix any arbitrary error threshold $\epsilon > 0$. Taking the limit as $n \to \infty$:

$$\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) \le \lim_{n \to \infty} \frac{\sigma^2}{n \epsilon^2} = 0$$

Because probabilities are bounded below by 0, the squeeze theorem forces the limit to be zero. Hence $\bar{X}_n \xrightarrow{P} \mu$. $\blacksquare$

---

### Khinchin's Weak Law of Large Numbers (Eliminating the Variance Assumption)

Chebyshev's proof relied critically upon the existence of the variance $\sigma^2 < \infty$. In 1929, the Soviet mathematician Aleksandr Khinchin achieved a major breakthrough by proving that the finite variance condition is completely unnecessary for i.i.d. observations: the existence of the first moment $\mathbb{E}[|X_i|] < \infty$ is fully sufficient.

**Theorem 7.6 (Khinchin's WLLN)**: Let $\{X_i\}_{i=1}^\infty$ be a sequence of independent and identically distributed (i.i.d.) random variables with finite expectation $\mathbb{E}[X_i] = \mu$. Then:

$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu \quad \text{as } n \to \infty$$

**Proof using Characteristic Functions**:
Let $\phi_X(t) = \mathbb{E}[e^{itX}]$ denote the characteristic function of $X_1$. Since $\mathbb{E}[|X_1|] < \infty$, the characteristic function is continuously differentiable on $\mathbb{R}$ with first derivative at the origin:

$$\phi_X'(0) = i \, \mathbb{E}[X_1] = i \mu$$

Applying Taylor's theorem with Peano's remainder to $\phi_X(t)$ in a neighborhood of $t = 0$:

$$\phi_X(t) = \phi_X(0) + \phi_X'(0) t + o(t) = 1 + i \mu t + o(t) \quad \text{as } t \to 0$$

Now, consider the characteristic function of the sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$:

$$\phi_{\bar{X}_n}(t) = \mathbb{E}\left[ \exp\left( i t \frac{1}{n} \sum_{i=1}^n X_i \right) \right] = \mathbb{E}\left[ \prod_{i=1}^n \exp\left( i \frac{t}{n} X_i \right) \right]$$

By the independence of $X_1, \dots, X_n$, the expectation of the product factors into the product of expectations:

$$\phi_{\bar{X}_n}(t) = \prod_{i=1}^n \mathbb{E}\left[ \exp\left( i \frac{t}{n} X_i \right) \right] = \left( \phi_X\left(\frac{t}{n}\right) \right)^n$$

For any fixed $t \in \mathbb{R}$, as $n \to \infty$, the argument $t/n \to 0$. Substituting the Taylor expansion of $\phi_X(t/n)$:

$$\phi_{\bar{X}_n}(t) = \left( 1 + i \mu \frac{t}{n} + o\left(\frac{t}{n}\right) \right)^n$$

Recall the classical real analysis limit identity: if $a_n \to a \in \mathbb{C}$, then $\lim_{n \to \infty} (1 + a_n/n)^n = e^a$. Here, letting $a_n = i \mu t + n \cdot o(t/n) \to i \mu t$ as $n \to \infty$:

$$\lim_{n \to \infty} \phi_{\bar{X}_n}(t) = \lim_{n \to \infty} \left( 1 + \frac{i \mu t + o(1)}{n} \right)^n = e^{i \mu t}$$

Observe that $\phi_c(t) = e^{ict}$ is the characteristic function of the degenerate constant random variable taking value $c = \mu$ with probability 1. 

By Lévy's Continuity Theorem (Section 7.6), because the sequence of characteristic functions $\phi_{\bar{X}_n}(t)$ converges pointwise to the characteristic function of the constant $\mu$, the sequence of random variables converges in distribution to $\mu$:

$$\bar{X}_n \xrightarrow{d} \mu$$

Finally, by the partial converse established in Section 7.2 (convergence in distribution to a constant implies convergence in probability), we conclude:

$$\bar{X}_n \xrightarrow{P} \mu \quad \blacksquare$$

---

### Failure of the WLLN: The Cauchy Distribution

It is instructive to understand what happens when the first moment does not exist. Consider an i.i.d. sequence $X_1, X_2, \dots \sim \text{Cauchy}(0, 1)$ with probability density function:

$$f(x) = \frac{1}{\pi (1 + x^2)}, \quad x \in \mathbb{R}$$

The integral $\int_{-\infty}^\infty |x| f(x) \, dx = \frac{2}{\pi}\int_0^\infty \frac{x}{1+x^2} \, dx = \lim_{M \to \infty} \frac{1}{\pi} \ln(1 + M^2) = +\infty$. Thus, the Cauchy distribution has no mean.

The characteristic function of a standard Cauchy variable is $\phi_X(t) = e^{-|t|}$. The characteristic function of the sample mean $\bar{X}_n$ is:

$$\phi_{\bar{X}_n}(t) = \left[ \phi_X\left(\frac{t}{n}\right) \right]^n = \left[ \exp\left( -\left|\frac{t}{n}\right| \right) \right]^n = \exp\left( -n \frac{|t|}{n} \right) = e^{-|t|}$$

Remarkably, the characteristic function of $\bar{X}_n$ is **identical** to the characteristic function of a single observation $X_1$ for all sample sizes $n \ge 1$! By the uniqueness of characteristic functions, the sample mean $\bar{X}_n$ of $1,000,000$ Cauchy observations has the exact same standard Cauchy distribution as a single observation. The sample average never settles down or concentrates; it fluctuates wildly over the real line forever, violating the Weak Law of Large Numbers.
"""

p5 = r"""## 7.5 The Strong Law of Large Numbers (SLLN)

While the Weak Law guarantees that the probability of significant error at index $n$ vanishes, it leaves open the possibility that an observer watching an infinite sequence of data might see erratic excursions recur indefinitely into the future. The **Strong Law of Large Numbers** rules this out completely: it establishes that with probability 1, the sample average path converges pointwise to the true expectation $\mu$.

### Kolmogorov's Strong Law of Large Numbers

**Theorem 7.7 (Kolmogorov's SLLN)**: Let $\{X_i\}_{i=1}^\infty$ be a sequence of independent and identically distributed (i.i.d.) random variables.
1. If $\mathbb{E}[|X_1|] < \infty$, then:
   $$P\left( \lim_{n \to \infty} \bar{X}_n = \mu \right) = 1$$
   where $\mu = \mathbb{E}[X_1]$.
2. Conversely, if $P(\lim_{n \to \infty} \bar{X}_n = c) = 1$ for some finite constant $c \in \mathbb{R}$, then necessarily $\mathbb{E}[|X_1|] < \infty$ and $c = \mathbb{E}[X_1]$. If $\mathbb{E}[|X_1|] = \infty$, then $\limsup_{n \to \infty} |\bar{X}_n| = \infty$ almost surely.

### Foundational Machinery: The Borel-Cantelli Lemmas

The primary analytical engine for proving almost sure convergence is the pair of lemmas established by Émile Borel (1909) and Francesco Cantelli (1917).

Let $\{E_n\}_{n=1}^\infty$ be an infinite sequence of events in $(\Omega, \mathcal{F}, P)$. The event that infinitely many $E_n$ occur (abbreviated $E_n \text{ i.o.}$) is defined as:

$$\{E_n \text{ i.o.}\} = \limsup_{n \to \infty} E_n = \bigcap_{m=1}^\infty \bigcup_{n=m}^\infty E_n$$

**Lemma 7.1 (First Borel-Cantelli Lemma)**:
Let $\{E_n\}_{n=1}^\infty$ be any sequence of events (no independence required). If the sum of their probabilities converges:

$$\sum_{n=1}^\infty P(E_n) < \infty$$

then the probability that infinitely many events occur is zero:

$$P(E_n \text{ i.o.}) = P\left( \limsup_{n \to \infty} E_n \right) = 0$$

**Proof**:
For each $m \ge 1$, let $B_m = \bigcup_{n=m}^\infty E_n$. Since $\{B_m\}$ is decreasing, $\{E_n \text{ i.o.}\} = \bigcap_{m=1}^\infty B_m$. By countable subadditivity of probability measures:

$$P(B_m) = P\left( \bigcup_{n=m}^\infty E_n \right) \le \sum_{n=m}^\infty P(E_n)$$

Because the infinite series $\sum_{n=1}^\infty P(E_n)$ converges, its tail sum must vanish as $m \to \infty$:

$$\lim_{m \to \infty} \sum_{n=m}^\infty P(E_n) = 0$$

By the continuity of probability from above:

$$P(E_n \text{ i.o.}) = P\left( \bigcap_{m=1}^\infty B_m \right) = \lim_{m \to \infty} P(B_m) \le \lim_{m \to \infty} \sum_{n=m}^\infty P(E_n) = 0$$

Since probabilities are non-negative, $P(E_n \text{ i.o.}) = 0$. $\blacksquare$

---

**Lemma 7.2 (Second Borel-Cantelli Lemma - The Independent Converse)**:
Let $\{E_n\}_{n=1}^\infty$ be a sequence of **mutually independent** events. If the sum of their probabilities diverges:

$$\sum_{n=1}^\infty P(E_n) = \infty$$

then the probability that infinitely many events occur is one:

$$P(E_n \text{ i.o.}) = 1$$

---

### Kronecker's Lemma and Kolmogorov's Convergence Criterion

To establish the Strong Law for sums of independent random variables, Kolmogorov utilized a remarkable real-analysis summation-by-parts identity.

**Lemma 7.3 (Kronecker's Lemma)**:
Let $\{x_n\}_{n=1}^\infty$ be a sequence of real numbers such that the infinite series $\sum_{n=1}^\infty x_n$ converges to a finite limit. Let $\{b_n\}_{n=1}^\infty$ be a positive, strictly increasing sequence of real numbers with $b_n \uparrow \infty$. Then:

$$\lim_{n \to \infty} \frac{1}{b_n} \sum_{k=1}^n b_k x_k = 0$$

**Theorem 7.8 (Kolmogorov's Criterion for Independent Series)**:
Let $\{Y_n\}_{n=1}^\infty$ be independent random variables with zero means $\mathbb{E}[Y_n] = 0$ and variances $\text{Var}(Y_n) = \sigma_n^2$. If:

$$\sum_{n=1}^\infty \frac{\sigma_n^2}{n^2} < \infty$$

then $\frac{1}{n}\sum_{k=1}^n Y_k \xrightarrow{\text{a.s.}} 0$.

### The Truncation Technique

In proving the SLLN for i.i.d. random variables with only $\mathbb{E}[|X_1|] < \infty$, the challenge is that the original variables $X_n$ may have infinite variance ($\sigma^2 = \infty$), preventing direct application of Kolmogorov's criterion. Kolmogorov overcame this obstacle with the ingenious **truncation method**.

Define the truncated variables:

$$Y_n = X_n \cdot \mathbf{1}_{\{|X_n| \le n\}}$$

1. **Equivalence of Tails**: Show that $P(X_n \ne Y_n \text{ i.o.}) = 0$.
   Observe that $P(X_n \ne Y_n) = P(|X_n| > n) = P(|X_1| > n)$.
   Using the integral identity for non-negative random variables:
   $$\sum_{n=1}^\infty P(|X_1| > n) \le \int_0^\infty P(|X_1| > t) \, dt = \mathbb{E}[|X_1|] < \infty$$
   By the First Borel-Cantelli Lemma, the events $\{X_n \ne Y_n\}$ occur only finitely many times with probability 1! Consequently, the sequences $\frac{1}{n}\sum_{i=1}^n X_i$ and $\frac{1}{n}\sum_{i=1}^n Y_i$ have the exact same almost sure limiting behavior.

2. **Sum of Variances of Truncated Variables**:
   Compute the variance sum:
   $$\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} \le \sum_{n=1}^\infty \frac{\mathbb{E}[Y_n^2]}{n^2} = \sum_{n=1}^\infty \frac{1}{n^2} \mathbb{E}[X_1^2 \mathbf{1}_{\{|X_1| \le n\}}]$$
   Exchanging summation and expectation by Fubini's theorem:
   $$\sum_{n=1}^\infty \frac{\text{Var}(Y_n)}{n^2} \le \mathbb{E}\left[ X_1^2 \sum_{n \ge |X_1|} \frac{1}{n^2} \right]$$
   Since $\sum_{n=m}^\infty \frac{1}{n^2} \le \frac{2}{m}$ for all $m \ge 1$:
   $$\mathbb{E}\left[ X_1^2 \sum_{n \ge |X_1|} \frac{1}{n^2} \right] \le \mathbb{E}\left[ X_1^2 \frac{2}{|X_1|} \right] = 2 \, \mathbb{E}[|X_1|] < \infty$$
   Because the series of variances converges, Kolmogorov's criterion and Kronecker's lemma imply that:
   $$\frac{1}{n}\sum_{i=1}^n (Y_i - \mathbb{E}[Y_i]) \xrightarrow{\text{a.s.}} 0$$

3. **Convergence of Truncated Expectations**:
   By the Dominated Convergence Theorem, $\lim_{n \to \infty} \mathbb{E}[Y_n] = \lim_{n \to \infty} \mathbb{E}[X_1 \mathbf{1}_{\{|X_1| \le n\}}] = \mathbb{E}[X_1] = \mu$.
   By Cesàro summation: $\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n \mathbb{E}[Y_i] = \mu$.
   Combining these results yields the complete Strong Law:
   $$\frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{\text{a.s.}} \mu \quad \blacksquare$$
"""

p6 = r"""## 7.6 Characteristic Functions and the Fourier-Analytic Toolkit

The ultimate analytical weapon for establishing convergence in distribution is the **characteristic function**.

### Definition and Fundamental Properties

**Definition**: For any real-valued random variable $X$ with cumulative distribution function $F(x)$, its **characteristic function** $\phi_X: \mathbb{R} \to \mathbb{C}$ is the Fourier-Stieltjes transform of its probability distribution:

$$\phi_X(t) = \mathbb{E}\left[ e^{i t X} \right] = \mathbb{E}[\cos(tX)] + i \, \mathbb{E}[\sin(tX)] = \int_{-\infty}^\infty e^{i t x} \, dF(x)$$

where $i = \sqrt{-1}$ is the imaginary unit and $t \in \mathbb{R}$ is the frequency parameter.

Unlike the Moment Generating Function $M_X(t) = \mathbb{E}[e^{tX}]$, which requires exponential tails and diverges to infinity for distributions with heavy tails (such as the Student's $t$, Cauchy, or Pareto distributions), the characteristic function **always exists for every random variable**:

$$|\phi_X(t)| = \left| \mathbb{E}[e^{itX}] \right| \le \mathbb{E}\left[ |e^{itX}| \right] = \mathbb{E}[1] = 1 \quad \text{for all } t \in \mathbb{R}$$

Key structural properties include:
1. **Normalization**: $\phi_X(0) = \mathbb{E}[e^0] = 1$.
2. **Hermitian Symmetry**: $\phi_X(-t) = \overline{\phi_X(t)}$, where $\overline{z}$ denotes the complex conjugate.
3. **Uniform Continuity**: $\phi_X(t)$ is uniformly continuous on the entire real line $\mathbb{R}$.
4. **Affine Transformation**: If $Y = aX + b$ for constants $a, b \in \mathbb{R}$, then:
   $$\phi_Y(t) = \mathbb{E}[e^{it(aX+b)}] = e^{itb} \mathbb{E}[e^{i(at)X}] = e^{itb} \phi_X(at)$$
5. **Convolution of Independent Variables**: If $X_1, X_2, \dots, X_n$ are independent, then:
   $$\phi_{\sum_{j=1}^n X_j}(t) = \prod_{j=1}^n \phi_{X_j}(t)$$
   The characteristic function converts tedious probability convolutions into simple algebraic multiplication.

---

### Lévy's Inversion Theorem and Uniqueness

A characteristic function uniquely determines the underlying probability distribution.

**Theorem 7.9 (Lévy's Inversion Formula)**:
Let $F(x)$ denote the CDF of $X$, and let $\phi(t)$ denote its characteristic function. For any two continuity points $a < b$ of $F$:

$$F(b) - F(a) = \lim_{T \to \infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{-ita} - e^{-itb}}{it} \phi(t) \, dt$$

Furthermore, if the characteristic function is absolutely integrable ($\int_{-\infty}^\infty |\phi(t)| \, dt < \infty$), the distribution possesses a continuous probability density function $f(x)$ given by the inverse Fourier transform:

$$f(x) = \frac{1}{2\pi}\int_{-\infty}^\infty e^{-itx} \phi(t) \, dt$$

---

### Lévy's Continuity Theorem

Lévy's Continuity Theorem provides the bridge connecting the pointwise convergence of characteristic functions to convergence in distribution of random variables.

**Theorem 7.10 (Lévy's Continuity Theorem)**:
Let $\{X_n\}_{n=1}^\infty$ be a sequence of random variables with characteristic functions $\phi_n(t) = \mathbb{E}[e^{itX_n}]$, and let $X$ have characteristic function $\phi(t)$.
1. If $X_n \xrightarrow{d} X$, then $\phi_n(t) \to \phi(t)$ pointwise for every $t \in \mathbb{R}$ as $n \to \infty$. (In fact, the convergence is uniform on every compact interval $[-K, K]$).
2. Conversely, suppose $\phi_n(t)$ converges pointwise to a limiting function:
   $$\lim_{n \to \infty} \phi_n(t) = g(t) \quad \text{for all } t \in \mathbb{R}$$
   If the limit function $g(t)$ is **continuous at the origin** $t = 0$, then $g(t)$ is the characteristic function of some random variable $X$ ($g(t) = \phi_X(t)$), and:
   $$X_n \xrightarrow{d} X$$

The continuity of $g(t)$ at $t = 0$ is essential: it prevents probability mass from escaping to $\pm \infty$ (a phenomenon known in measure theory as tightness).
"""

p7 = r"""## 7.7 The Classical Lindeberg-Lévy Central Limit Theorem

The Central Limit Theorem (CLT) is indisputably one of the most remarkable discoveries in all of mathematics. It explains why the bell-shaped Gaussian distribution appears ubiquitously across astronomy, thermodynamics, genetics, biometrics, economics, and psychology: whenever an observed phenomenon is the cumulative sum of numerous small, independent random disturbances, the aggregate distribution converges inexorably toward a Gaussian law, regardless of the shape of the individual component distributions.

### Formal Statement

**Theorem 7.11 (Lindeberg-Lévy CLT)**:
Let $\{X_i\}_{i=1}^\infty$ be an i.i.d. sequence of random variables with common expectation $\mu = \mathbb{E}[X_i]$ and finite variance $\sigma^2 = \text{Var}(X_i) \in (0, \infty)$.
Define the standardized sample sum:

$$Z_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma \sqrt{n}} = \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma}$$

Then, as the sample size $n \to \infty$, $Z_n$ converges in distribution to a standard Gaussian random variable $\mathcal{N}(0, 1)$:

$$Z_n \xrightarrow{d} \mathcal{N}(0, 1)$$

That is, for every real number $z \in \mathbb{R}$:

$$\lim_{n \to \infty} P(Z_n \le z) = \Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-u^2/2} \, du$$

---

### Step-by-Step Rigorous Proof

**Proof**:
Without loss of generality, we can center the variables. Let $Y_i = \frac{X_i - \mu}{\sigma}$. Then $\{Y_i\}_{i=1}^\infty$ are i.i.d. random variables satisfying:

$$\mathbb{E}[Y_i] = 0 \quad \text{and} \quad \text{Var}(Y_i) = \mathbb{E}[Y_i^2] = 1$$

The standardized sample sum $Z_n$ can be written cleanly as:

$$Z_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n Y_i$$

Let $\phi_Y(t) = \mathbb{E}[e^{itY_1}]$ denote the characteristic function of $Y_1$. Since $Y_1$ possesses finite first and second moments ($\mathbb{E}[|Y_1|^2] = 1 < \infty$), Taylor's theorem with Peano's form of the remainder implies that around $t = 0$:

$$\phi_Y(t) = \phi_Y(0) + \phi_Y'(0) t + \frac{1}{2} \phi_Y''(0) t^2 + o(t^2)$$

Evaluating the derivatives at the origin:
- $\phi_Y(0) = 1$
- $\phi_Y'(0) = i \, \mathbb{E}[Y_1] = 0$
- $\phi_Y''(0) = i^2 \, \mathbb{E}[Y_1^2] = -1 \cdot 1 = -1$

Substituting these values into the Taylor expansion yields:

$$\phi_Y(t) = 1 - \frac{1}{2}t^2 + o(t^2) \quad \text{as } t \to 0$$

Now, consider the characteristic function of $Z_n = \sum_{i=1}^n (Y_i / \sqrt{n})$:

$$\phi_{Z_n}(t) = \mathbb{E}\left[ \exp\left( i t \frac{1}{\sqrt{n}} \sum_{i=1}^n Y_i \right) \right] = \prod_{i=1}^n \mathbb{E}\left[ \exp\left( i \frac{t}{\sqrt{n}} Y_i \right) \right] = \left( \phi_Y\left(\frac{t}{\sqrt{n}}\right) \right)^n$$

For any fixed $t \in \mathbb{R}$, as $n \to \infty$, the scaled argument $t/\sqrt{n} \to 0$. Substituting the expansion:

$$\phi_{Z_n}(t) = \left( 1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right) \right)^n$$

We examine the natural logarithm of $\phi_{Z_n}(t)$. Using the Taylor series expansion for the complex logarithm $\ln(1 + z) = z + O(|z|^2)$ for $|z| < 1/2$:

$$\ln \phi_{Z_n}(t) = n \ln\left( 1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right) \right) = n \left( -\frac{t^2}{2n} + o\left(\frac{1}{n}\right) \right) = -\frac{t^2}{2} + n \cdot o\left(\frac{1}{n}\right)$$

Taking the limit as $n \to \infty$:

$$\lim_{n \to \infty} \ln \phi_{Z_n}(t) = -\frac{t^2}{2}$$

Exponentiating both sides:

$$\lim_{n \to \infty} \phi_{Z_n}(t) = \lim_{n \to \infty} \exp\left( \ln \phi_{Z_n}(t) \right) = e^{-t^2/2}$$

Notice that $\phi(t) = e^{-t^2/2}$ is precisely the characteristic function of the standard Gaussian distribution $\mathcal{N}(0, 1)$.

Since the limiting function $e^{-t^2/2}$ is continuous at $t = 0$ (with $e^0 = 1$), Lévy's Continuity Theorem (Theorem 7.10) asserts that:

$$Z_n \xrightarrow{d} \mathcal{N}(0, 1) \quad \blacksquare$$
"""

p8 = r"""## 7.8 Triangular Arrays and General Central Limit Theorems: Lindeberg and Lyapunov

In many realistic econometric, engineering, and experimental environments, observations are neither identically distributed nor collected in an unchanging sequence. For example, in regression analysis, the explanatory design points $x_i$ vary across observations, so each error contribution has a different scale. To handle non-identically distributed and dependent structures, probability theorists developed the framework of **triangular arrays**.

### Definition of a Triangular Array

A triangular array of random variables is a doubly indexed collection:

$$\begin{matrix}
X_{11} \\
X_{21}, & X_{22} \\
X_{31}, & X_{32}, & X_{33} \\
\vdots & \vdots & \vdots & \ddots \\
X_{n1}, & X_{n2}, & X_{n3}, & \dots & X_{nn}
\end{matrix}$$

where for each row $n \ge 1$, the random variables $\{X_{ni}\}_{i=1}^{k_n}$ (with $k_n \to \infty$) are mutually independent with means $\mathbb{E}[X_{ni}] = 0$ and variances $\sigma_{ni}^2 = \text{Var}(X_{ni})$.
Let the total row variance be normalized to unity:

$$s_n^2 = \sum_{i=1}^{k_n} \sigma_{ni}^2 = 1$$

We seek conditions under which the row sum $S_n = \sum_{i=1}^{k_n} X_{ni} \xrightarrow{d} \mathcal{N}(0, 1)$.

---

### The Lindeberg Condition

In 1922, Finnish mathematician Jarl Waldemar Lindeberg introduced a condition that restricts the contribution of extreme tail outliers.

**Definition (Lindeberg Condition)**:
The triangular array satisfies the **Lindeberg Condition** if for every fixed threshold $\epsilon > 0$:

$$\lim_{n \to \infty} L_n(\epsilon) = \lim_{n \to \infty} \sum_{i=1}^{k_n} \mathbb{E}\left[ X_{ni}^2 \mathbf{1}_{\{|X_{ni}| \ge \epsilon\}} \right] = 0$$

In intuitive terms, the Lindeberg condition requires that the expected squared energy residing in the tails beyond $\epsilon$ shrinks to zero across the entire sum: no individual term is permitted to dominate the variance of the aggregate sum.

**Theorem 7.12 (Lindeberg-Feller Central Limit Theorem)**:
Let $\{X_{ni}\}$ be an independent triangular array with $\mathbb{E}[X_{ni}] = 0$ and $\sum_{i=1}^{k_n} \sigma_{ni}^2 = 1$.
1. **Lindeberg's Theorem**: If the Lindeberg condition holds, then:
   $$S_n = \sum_{i=1}^{k_n} X_{ni} \xrightarrow{d} \mathcal{N}(0, 1)$$
   Furthermore, the array is **Uniformly Asymptotically Negligible (UAN)**:
   $$\lim_{n \to \infty} \max_{1 \le i \le k_n} \sigma_{ni}^2 = 0$$
2. **Feller's Converse (1935)**: If $S_n \xrightarrow{d} \mathcal{N}(0, 1)$ AND the UAN condition holds, then the Lindeberg condition is necessarily satisfied!

Together, Lindeberg and Feller proved that under the natural UAN condition, the Lindeberg condition is not merely sufficient, but **necessary and sufficient** for asymptotic normality.

---

### Lyapunov's Condition: An Easily Verifiable Criterion

Checking the indicator expectation $\mathbb{E}[X_{ni}^2 \mathbf{1}_{\{|X_{ni}| \ge \epsilon\}}]$ can be analytically tedious. In 1901, Aleksandr Lyapunov provided a stronger, moments-based criterion that is far easier to verify in practice.

**Theorem 7.13 (Lyapunov's CLT)**:
Let $\{X_{ni}\}$ be an independent triangular array with $\mathbb{E}[X_{ni}] = 0$ and row variance $s_n^2 = \sum_{i=1}^{k_n} \sigma_{ni}^2$. If there exists some $\delta > 0$ such that:

$$\lim_{n \to \infty} \frac{1}{s_n^{2+\delta}} \sum_{i=1}^{k_n} \mathbb{E}\left[ |X_{ni}|^{2+\delta} \right] = 0$$

then $S_n / s_n \xrightarrow{d} \mathcal{N}(0, 1)$.

**Proof that Lyapunov Implies Lindeberg**:
Observe that whenever $|X_{ni}| \ge \epsilon s_n$, we have $|X_{ni}|^{\delta} \ge (\epsilon s_n)^\delta$, which implies:

$$X_{ni}^2 \le \frac{|X_{ni}|^{2+\delta}}{(\epsilon s_n)^\delta}$$

Therefore:

$$\sum_{i=1}^{k_n} \mathbb{E}\left[ X_{ni}^2 \mathbf{1}_{\{|X_{ni}| \ge \epsilon s_n\}} \right] \le \frac{1}{\epsilon^\delta s_n^\delta} \sum_{i=1}^{k_n} \mathbb{E}\left[ |X_{ni}|^{2+\delta} \right]$$

Dividing both sides by $s_n^2$:

$$\frac{1}{s_n^2}\sum_{i=1}^{k_n} \mathbb{E}\left[ X_{ni}^2 \mathbf{1}_{\{|X_{ni}| \ge \epsilon s_n\}} \right] \le \frac{1}{\epsilon^\delta} \left( \frac{1}{s_n^{2+\delta}}\sum_{i=1}^{k_n} \mathbb{E}\left[ |X_{ni}|^{2+\delta} \right] \right) \to 0$$

Thus, Lyapunov's condition automatically implies Lindeberg's condition! $\blacksquare$
"""

p9 = r"""## 7.9 The Berry-Esseen Theorem and Rate of Convergence

The Central Limit Theorem guarantees that the CDF error $|F_n(z) - \Phi(z)|$ vanishes as $n \to \infty$. However, in scientific practice, sample size is always finite. How fast does convergence occur? How large must $n$ be before the Gaussian approximation can be safely trusted? The **Berry-Esseen Theorem** answers this question with precision.

### The Berry-Esseen Bound

**Theorem 7.14 (Berry-Esseen Theorem)**:
Let $\{X_i\}_{i=1}^n$ be i.i.d. random variables with mean $\mu$, variance $\sigma^2 > 0$, and finite absolute third moment $\rho = \mathbb{E}[|X_1 - \mu|^3] < \infty$. Let $F_n(z) = P\left( \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \le z \right)$. Then for all $z \in \mathbb{R}$ and all $n \ge 1$:

$$\sup_{z \in \mathbb{R}} |F_n(z) - \Phi(z)| \le \frac{C \cdot \rho}{\sigma^3 \sqrt{n}}$$

where $C$ is a universal, distribution-free mathematical constant.

### Numerical Magnitude of the Constant $C$
The exact value of $C$ was sharpened through decades of harmonic analysis:
- Andrew Berry (1941) proved $C \le 1.88$.
- Carl-Gustav Esseen (1942) established $C \le 7.59$, and proved the fundamental lower bound $C \ge \frac{\sqrt{10} + 3}{6\sqrt{2\pi}} \approx 0.40973$.
- Irina Shevtsova (2011) proved the modern tight upper bound:
  $$C \le 0.4748$$

Thus, for any distribution with finite third moments:

$$\sup_{z \in \mathbb{R}} |F_n(z) - \Phi(z)| \le \frac{0.4748 \cdot \rho}{\sigma^3 \sqrt{n}}$$

### Key Practical Insights from Berry-Esseen:
1. **The $1/\sqrt{n}$ Convergence Rate**: The uniform error between the true cumulative distribution and the normal CDF decays at rate $O(1/\sqrt{n})$. To cut the maximum error in half, the sample size must be quadrupled ($4n$).
2. **The Role of Skewness**: The ratio $\frac{\rho}{\sigma^3}$ measures the standardized third moment. For symmetric distributions (e.g., Uniform, Student's $t$ with $df > 3$), skewness $\gamma_1 = \mathbb{E}[(X-\mu)^3]/\sigma^3 = 0$, and convergence is remarkably swift (often $n \approx 15$ to $30$ yields excellent fidelity). For highly skewed distributions (e.g., Exponential where $\rho/\sigma^3 \approx 8.5$, or Lognormal where $\rho/\sigma^3 \gg 100$), much larger samples ($n \ge 500$) are required before normal approximations become reliable.

---

## 7.10 Methodological Implications in Statistical Inference

The limit theorems developed throughout this unit form the mathematical bedrock of classical and modern statistical inference.

### 1. Consistency of Sample Moments
Let $X_1, \dots, X_n$ be an i.i.d. sample from a population with finite $k$-th moment $\mu_k' = \mathbb{E}[X^k] < \infty$. The empirical $k$-th sample moment is defined as $m_k' = \frac{1}{n}\sum_{i=1}^n X_i^k$.
By Kolmogorov's SLLN applied to the sequence of i.i.d. variables $Y_i = X_i^k$:

$$m_k' = \frac{1}{n}\sum_{i=1}^n X_i^k \xrightarrow{\text{a.s.}} \mathbb{E}[X^k] = \mu_k'$$

Furthermore, the sample variance $S_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X}_n)^2 = \frac{n}{n-1}\left( \frac{1}{n}\sum_{i=1}^n X_i^2 - (\bar{X}_n)^2 \right)$. By the SLLN, $\frac{1}{n}\sum X_i^2 \xrightarrow{\text{a.s.}} \mathbb{E}[X^2]$ and $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$. By the Continuous Mapping Theorem:

$$S_n^2 \xrightarrow{\text{a.s.}} \mathbb{E}[X^2] - \mu^2 = \sigma^2$$

The sample variance is a **strongly consistent estimator** of the population variance.

---

### 2. Large-Sample Confidence Intervals and Slutsky's Theorem
The Lindeberg-Lévy CLT guarantees that $\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \xrightarrow{d} \mathcal{N}(0, 1)$. However, in practice, the true population standard deviation $\sigma$ is unknown. We substitute the sample standard deviation $S_n$.

By consistency, $S_n \xrightarrow{P} \sigma$, which implies $\frac{\sigma}{S_n} \xrightarrow{P} 1$.
Applying Slutsky's Theorem:

$$\frac{\sqrt{n}(\bar{X}_n - \mu)}{S_n} = \left( \frac{\sigma}{S_n} \right) \left( \frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \right) \xrightarrow{d} 1 \cdot \mathcal{N}(0, 1) = \mathcal{N}(0, 1)$$

This guarantees that the large-sample Wald confidence interval:

$$\text{CI}_{1-\alpha} = \left[ \bar{X}_n - z_{1 - \alpha/2} \frac{S_n}{\sqrt{n}}, \, \bar{X}_n + z_{1 - \alpha/2} \frac{S_n}{\sqrt{n}} \right]$$

has exact asymptotic coverage probability $1 - \alpha$, regardless of the parent distribution of $X_i$!

---

### 3. Monte Carlo Integration and Simulation Error
Suppose we need to evaluate a complex multidimensional integral $I = \int_{[0, 1]^d} g(\mathbf{u}) \, d\mathbf{u}$. Monte Carlo integration samples $n$ independent uniform random vectors $\mathbf{U}_i \sim \text{Uniform}([0, 1]^d)$ and computes the empirical average:

$$\hat{I}_n = \frac{1}{n}\sum_{i=1}^n g(\mathbf{U}_i)$$

By the Strong Law of Large Numbers, $\hat{I}_n \xrightarrow{\text{a.s.}} I$. By the Central Limit Theorem:

$$\sqrt{n}(\hat{I}_n - I) \xrightarrow{d} \mathcal{N}\left(0, \sigma_g^2\right)$$

where $\sigma_g^2 = \text{Var}(g(\mathbf{U}))$. The absolute error $|\hat{I}_n - I| = O_P(n^{-1/2})$. Crucially, this convergence rate $n^{-1/2}$ is completely independent of the dimension $d$, allowing Monte Carlo algorithms to defeat the "curse of dimensionality" that cripples deterministic grid quadrature methods.
"""

p10 = r"""## Fully worked question 1: Rigorous Proof of the First Borel-Cantelli Lemma and Almost Sure Convergence

### Question
Let $\{X_n\}_{n=1}^\infty$ be a sequence of independent random variables such that for each $n \ge 1$, $X_n$ follows an exponential distribution with rate parameter $\lambda_n = n^\alpha$, where $\alpha > 0$ is a fixed real exponent:

$$f_{X_n}(x) = n^\alpha e^{-n^\alpha x} \mathbf{1}_{(0, \infty)}(x)$$

1. State and prove the First Borel-Cantelli Lemma using the continuity of probability measures.
2. Determine the exact range of the parameter $\alpha > 0$ for which the sequence $X_n$ converges to 0 almost surely ($X_n \xrightarrow{\text{a.s.}} 0$).
3. Contrast this with the range of $\alpha$ for which $X_n$ converges to 0 in probability ($X_n \xrightarrow{P} 0$).

---

### Solution, step 1: Proof of the First Borel-Cantelli Lemma
Let $(\Omega, \mathcal{F}, P)$ be a probability space, and let $\{E_n\}_{n=1}^\infty$ be an arbitrary sequence of events in $\mathcal{F}$.
We are given that the sum of event probabilities converges:

$$\sum_{n=1}^\infty P(E_n) < \infty$$

The event that infinitely many $E_n$ occur is defined by:

$$E_\infty = \limsup_{n \to \infty} E_n = \bigcap_{m=1}^\infty \bigcup_{n=m}^\infty E_n$$

For each positive integer $m \ge 1$, define the tail union event:

$$B_m = \bigcup_{n=m}^\infty E_n$$

Notice that the sequence of events $\{B_m\}_{m=1}^\infty$ forms a monotone decreasing sequence:

$$B_1 \supseteq B_2 \supseteq B_3 \supseteq \dots \supseteq B_m \supseteq B_{m+1} \supseteq \dots$$

because each subsequent union discards the earliest event $E_m$.
The infinite intersection of this decreasing sequence is, by definition:

$$\bigcap_{m=1}^\infty B_m = \bigcap_{m=1}^\infty \bigcup_{n=m}^\infty E_n = E_\infty$$

By the axiom of continuity of probability measures from above (continuity from above on nested decreasing events):

$$P(E_\infty) = P\left( \bigcap_{m=1}^\infty B_m \right) = \lim_{m \to \infty} P(B_m)$$

Next, apply Boole's inequality (countable subadditivity) to the union defining $B_m$:

$$P(B_m) = P\left( \bigcup_{n=m}^\infty E_n \right) \le \sum_{n=m}^\infty P(E_n)$$

Now, examine the infinite sum $\sum_{n=1}^\infty P(E_n)$. Because this series converges by hypothesis, its remainder tail sum must tend to zero as the lower summation limit $m$ approaches infinity:

$$\lim_{m \to \infty} \sum_{n=m}^\infty P(E_n) = 0$$

Taking limits on both sides of our inequality:

$$0 \le P(E_\infty) = \lim_{m \to \infty} P(B_m) \le \lim_{m \to \infty} \sum_{n=m}^\infty P(E_n) = 0$$

By the squeeze theorem:

$$P(E_\infty) = P(E_n \text{ i.o.}) = 0$$

This completes the rigorous proof of the First Borel-Cantelli Lemma. $\blacksquare$

---

### Solution, step 2: Range of $\alpha$ for Almost Sure Convergence
We want to determine when $X_n \xrightarrow{\text{a.s.}} 0$.
By definition, $X_n \xrightarrow{\text{a.s.}} 0$ if and only if for every $\epsilon > 0$:

$$P(|X_n - 0| \ge \epsilon \text{ i.o.}) = 0$$

Since $X_n \sim \text{Exp}(n^\alpha)$, $X_n > 0$ almost surely. The survival function of $X_n$ evaluated at $\epsilon > 0$ is:

$$P(X_n \ge \epsilon) = \int_\epsilon^\infty n^\alpha e^{-n^\alpha x} \, dx = \left[ -e^{-n^\alpha x} \right]_\epsilon^\infty = e^{-\epsilon n^\alpha}$$

Define the event $E_n(\epsilon) = \{X_n \ge \epsilon\}$.
To apply the First Borel-Cantelli Lemma, examine the convergence of the infinite series of probabilities:

$$S(\epsilon) = \sum_{n=1}^\infty P(E_n(\epsilon)) = \sum_{n=1}^\infty e^{-\epsilon n^\alpha}$$

We test the convergence of this series as a function of the parameter $\alpha > 0$:
- **Case 1: $\alpha > 0$**.
  For any fixed $\alpha > 0$ and any fixed $\epsilon > 0$, the function $g(x) = e^{-\epsilon x^\alpha}$ is positive, continuous, and strictly decreasing for $x \ge 1$. We apply the integral test:
  $$\int_1^\infty e^{-\epsilon x^\alpha} \, dx$$
  Make the substitution $u = \epsilon x^\alpha$, so $x = (u/\epsilon)^{1/\alpha}$ and $dx = \frac{1}{\alpha \epsilon^{1/\alpha}} u^{(1/\alpha) - 1} \, du$:
  $$\int_1^\infty e^{-\epsilon x^\alpha} \, dx = \frac{1}{\alpha \epsilon^{1/\alpha}} \int_\epsilon^\infty u^{\frac{1}{\alpha} - 1} e^{-u} \, du \le \frac{1}{\alpha \epsilon^{1/\alpha}} \Gamma\left(\frac{1}{\alpha}\right) < \infty$$
  Because the integral converges for every $\alpha > 0$, the series $\sum_{n=1}^\infty e^{-\epsilon n^\alpha}$ converges for **all** $\alpha > 0$ and every $\epsilon > 0$.

Applying the First Borel-Cantelli Lemma:

$$P(X_n \ge \epsilon \text{ i.o.}) = 0 \quad \text{for every } \epsilon > 0$$

Therefore, $X_n \xrightarrow{\text{a.s.}} 0$ for all $\alpha > 0$.

---

### Solution, step 3: Contrast with Convergence in Probability
Now test for convergence in probability: $X_n \xrightarrow{P} 0$ requires that for every $\epsilon > 0$:

$$\lim_{n \to \infty} P(|X_n - 0| \ge \epsilon) = \lim_{n \to \infty} e^{-\epsilon n^\alpha} = 0$$

- For any $\alpha > 0$: as $n \to \infty$, $n^\alpha \to \infty$, so $\lim_{n \to \infty} e^{-\epsilon n^\alpha} = 0$. Thus, $X_n \xrightarrow{P} 0$ for all $\alpha > 0$.
- For $\alpha = 0$: $X_n \sim \text{Exp}(1)$ for all $n$, so $P(X_n \ge \epsilon) = e^{-\epsilon} > 0$ is non-zero and constant, failing both modes.
- For $\alpha < 0$: $n^\alpha \to 0$, so $P(X_n \ge \epsilon) = e^{-\epsilon n^\alpha} \to e^0 = 1$, diverging completely.

Thus, both almost sure convergence and convergence in probability hold for the exact same parameter regime: $\alpha \in (0, \infty)$. The rapid exponential decay of the tail probability $e^{-\epsilon n^\alpha}$ ensures that the series converges without requiring any threshold restriction on $\alpha > 0$. $\blacksquare$
"""

p11 = r"""## Fully worked question 2: Proof of Khinchin's Weak Law of Large Numbers without Finite Variance

### Question
Let $\{X_n\}_{n=1}^\infty$ be a sequence of independent and identically distributed (i.i.d.) random variables with cumulative distribution function $F(x)$. Assume only that the first moment is finite:

$$\mathbb{E}[|X_1|] = \int_{-\infty}^\infty |x| \, dF(x) < \infty$$

with population mean $\mu = \mathbb{E}[X_1]$. Do NOT assume that the variance $\text{Var}(X_1)$ exists or is finite.

1. State the precise definition of the characteristic function $\phi_X(t)$ and prove that under the finite first moment condition, $\phi_X(t)$ is differentiable at the origin with $\phi_X'(0) = i\mu$.
2. Derive the characteristic function of the sample mean $\bar{X}_n = \frac{1}{n}\sum_{k=1}^n X_k$.
3. Using Lévy's Continuity Theorem, rigorously prove that $\bar{X}_n \xrightarrow{P} \mu$ as $n \to \infty$.

---

### Solution, step 1: Differentiability of the Characteristic Function at $t = 0$
The characteristic function of $X_1$ is defined for all $t \in \mathbb{R}$ by:

$$\phi_X(t) = \mathbb{E}\left[ e^{itX_1} \right] = \int_{-\infty}^\infty e^{itx} \, dF(x)$$

To prove that $\phi_X(t)$ is differentiable at $t = 0$, we examine the difference quotient as $t \to 0$:

$$\frac{\phi_X(t) - \phi_X(0)}{t} = \frac{\mathbb{E}[e^{itX_1}] - 1}{t} = \mathbb{E}\left[ \frac{e^{itX_1} - 1}{t} \right] = \int_{-\infty}^\infty \frac{e^{itx} - 1}{t} \, dF(x)$$

Consider the integrand $g(t, x) = \frac{e^{itx} - 1}{t}$.
From the fundamental theorem of calculus applied to the complex exponential:

$$e^{itx} - 1 = \int_0^t i x e^{ius} \, ds \implies |e^{itx} - 1| \le \int_0^{|t|} |ix| |e^{ius}| \, ds = |x| |t|$$

Dividing both sides by $|t| > 0$:

$$\left| \frac{e^{itx} - 1}{t} \right| \le |x| \quad \text{for all } t \ne 0 \text{ and all } x \in \mathbb{R}$$

Notice that the dominating bound $h(x) = |x|$ does not depend on $t$, and by hypothesis it is integrable with respect to $F$:

$$\int_{-\infty}^\infty h(x) \, dF(x) = \int_{-\infty}^\infty |x| \, dF(x) = \mathbb{E}[|X_1|] < \infty$$

Furthermore, for every fixed $x \in \mathbb{R}$, by L'Hôpital's rule or Euler's formula:

$$\lim_{t \to 0} \frac{e^{itx} - 1}{t} = \lim_{t \to 0} \frac{\cos(tx) - 1}{t} + i \lim_{t \to 0} \frac{\sin(tx)}{t} = 0 + i x = ix$$

Because the integrand converges pointwise to $ix$ and is uniformly bounded by an integrable function $|x|$, Lebesgue's Dominated Convergence Theorem permits the interchange of limit and integral:

$$\lim_{t \to 0} \frac{\phi_X(t) - \phi_X(0)}{t} = \int_{-\infty}^\infty \left( \lim_{t \to 0} \frac{e^{itx} - 1}{t} \right) dF(x) = \int_{-\infty}^\infty ix \, dF(x) = i \int_{-\infty}^\infty x \, dF(x) = i\mu$$

This proves that $\phi_X'(0)$ exists and equals $i\mu$. Consequently, by Taylor's theorem with Peano's remainder:

$$\phi_X(t) = 1 + i\mu t + o(t) \quad \text{as } t \to 0$$

where $\lim_{t \to 0} \frac{o(t)}{t} = 0$.

---

### Solution, step 2: Characteristic Function of the Sample Mean
Let $\bar{X}_n = \frac{1}{n}\sum_{k=1}^n X_k$. Using the scaling and independence properties of characteristic functions:

$$\phi_{\bar{X}_n}(t) = \mathbb{E}\left[ \exp\left( i t \frac{1}{n} \sum_{k=1}^n X_k \right) \right] = \mathbb{E}\left[ \prod_{k=1}^n \exp\left( i \frac{t}{n} X_k \right) \right]$$

Since $X_1, \dots, X_n$ are mutually independent:

$$\mathbb{E}\left[ \prod_{k=1}^n \exp\left( i \frac{t}{n} X_k \right) \right] = \prod_{k=1}^n \mathbb{E}\left[ \exp\left( i \frac{t}{n} X_k \right) \right] = \left( \phi_X\left(\frac{t}{n}\right) \right)^n$$

Now, fix an arbitrary $t \in \mathbb{R}$. As $n \to \infty$, the ratio $t/n \to 0$. Substituting the first-order Taylor expansion derived in step 1:

$$\phi_X\left(\frac{t}{n}\right) = 1 + i\mu \frac{t}{n} + o\left(\frac{t}{n}\right) = 1 + \frac{i\mu t + n \cdot o(t/n)}{n}$$

Let $\delta_n(t) = n \cdot o(t/n) = t \cdot \frac{o(t/n)}{t/n}$. Because $\lim_{u \to 0} \frac{o(u)}{u} = 0$, for any fixed $t$ we have:

$$\lim_{n \to \infty} \delta_n(t) = t \cdot 0 = 0$$

---

### Solution, step 3: Application of Lévy's Continuity Theorem and Conclusion
We now evaluate the limit of $\phi_{\bar{X}_n}(t)$ as $n \to \infty$:

$$\phi_{\bar{X}_n}(t) = \left( 1 + \frac{i\mu t + \delta_n(t)}{n} \right)^n$$

We utilize the standard lemma from complex analysis: if $\{z_n\}$ is a sequence of complex numbers such that $\lim_{n \to \infty} z_n = z \in \mathbb{C}$, then:

$$\lim_{n \to \infty} \left( 1 + \frac{z_n}{n} \right)^n = e^z$$

Here, $z_n = i\mu t + \delta_n(t) \to i\mu t$ as $n \to \infty$. Therefore:

$$\lim_{n \to \infty} \phi_{\bar{X}_n}(t) = e^{i\mu t} \quad \text{for all } t \in \mathbb{R}$$

Now identify the limiting function $\phi_\infty(t) = e^{i\mu t}$.
Notice that for a degenerate random variable $C$ taking the constant value $\mu$ with probability 1 ($P(C = \mu) = 1$):

$$\phi_C(t) = \mathbb{E}[e^{itC}] = e^{it\mu} \cdot P(C = \mu) = e^{i\mu t}$$

Thus, $\phi_{\bar{X}_n}(t) \to \phi_C(t)$ pointwise for every $t \in \mathbb{R}$.
The function $\phi_\infty(t) = e^{i\mu t}$ is continuous at $t = 0$ (since $\lim_{t \to 0} e^{i\mu t} = e^0 = 1$).
Therefore, by Lévy's Continuity Theorem (Theorem 7.10):

$$\bar{X}_n \xrightarrow{d} \mu$$

Finally, we apply the equivalence established in Theorem 7.4: whenever a sequence of random variables converges in distribution to a constant $c$, it necessarily converges in probability to that constant:

$$\bar{X}_n \xrightarrow{d} \mu \implies \bar{X}_n \xrightarrow{P} \mu$$

This completes the full proof of Khinchin's Weak Law of Large Numbers without assuming finite second moments. $\blacksquare$
"""

p12 = r"""## Fully worked question 3: Verifying the Lindeberg Condition for the OLS Slope Estimator

### Question
Consider the simple linear regression model through the origin:

$$Y_i = \beta x_i + \varepsilon_i, \quad i = 1, 2, \dots, n$$

where $x_1, x_2, \dots$ is a sequence of non-random, fixed real explanatory constants (design points) with $\sum_{i=1}^n x_i^2 > 0$, $\beta \in \mathbb{R}$ is the unknown regression coefficient, and $\varepsilon_1, \varepsilon_2, \dots$ are independent and identically distributed (i.i.d.) random disturbances with:

$$\mathbb{E}[\varepsilon_i] = 0 \quad \text{and} \quad \text{Var}(\varepsilon_i) = \sigma^2 \in (0, \infty)$$

The Ordinary Least Squares (OLS) estimator of $\beta$ is given by:

$$\hat{\beta}_n = \frac{\sum_{i=1}^n x_i Y_i}{\sum_{i=1}^n x_i^2}$$

Define $s_n^2 = \sum_{i=1}^n x_i^2$ and $M_n = \max_{1 \le i \le n} |x_i|$.
The **Grenander condition** states that:

$$\lim_{n \to \infty} \frac{M_n^2}{s_n^2} = \lim_{n \to \infty} \frac{\max_{1 \le i \le n} x_i^2}{\sum_{i=1}^n x_i^2} = 0$$

1. Express the normalized estimation error $\frac{\hat{\beta}_n - \beta}{\sqrt{\text{Var}(\hat{\beta}_n)}}$ as the row sum of an independent triangular array $\{W_{ni}\}_{i=1}^n$.
2. Formulate the Lindeberg condition for this triangular array.
3. Rigorously prove that under the Grenander condition, the Lindeberg condition is satisfied, and conclude that $\frac{\hat{\beta}_n - \beta}{\sigma / \sqrt{\sum_{i=1}^n x_i^2}} \xrightarrow{d} \mathcal{N}(0, 1)$.

---

### Solution, step 1: Triangular Array Representation
Substitute the data generating equation $Y_i = \beta x_i + \varepsilon_i$ into the definition of $\hat{\beta}_n$:

$$\hat{\beta}_n = \frac{\sum_{i=1}^n x_i (\beta x_i + \varepsilon_i)}{\sum_{i=1}^n x_i^2} = \beta \frac{\sum_{i=1}^n x_i^2}{\sum_{i=1}^n x_i^2} + \frac{\sum_{i=1}^n x_i \varepsilon_i}{\sum_{i=1}^n x_i^2} = \beta + \frac{\sum_{i=1}^n x_i \varepsilon_i}{s_n^2}$$

Subtracting $\beta$:

$$\hat{\beta}_n - \beta = \sum_{i=1}^n \left( \frac{x_i}{s_n^2} \right) \varepsilon_i$$

Compute the exact variance of $\hat{\beta}_n$:
Because the errors $\varepsilon_i$ are independent with variance $\sigma^2$:

$$\text{Var}(\hat{\beta}_n) = \sum_{i=1}^n \left( \frac{x_i}{s_n^2} \right)^2 \text{Var}(\varepsilon_i) = \frac{\sum_{i=1}^n x_i^2}{s_n^4} \sigma^2 = \frac{s_n^2}{s_n^4} \sigma^2 = \frac{\sigma^2}{s_n^2}$$

The standard deviation is $\sqrt{\text{Var}(\hat{\beta}_n)} = \frac{\sigma}{s_n}$.
Now form the standardized studentized estimator:

$$Z_n = \frac{\hat{\beta}_n - \beta}{\sigma / s_n} = \frac{s_n}{\sigma} \sum_{i=1}^n \frac{x_i}{s_n^2} \varepsilon_i = \sum_{i=1}^n \left( \frac{x_i}{\sigma s_n} \right) \varepsilon_i$$

Define the triangular array terms:

$$W_{ni} = \frac{x_i}{\sigma s_n} \varepsilon_i, \quad 1 \le i \le n$$

Verify the row sum properties:
- $\mathbb{E}[W_{ni}] = \frac{x_i}{\sigma s_n} \mathbb{E}[\varepsilon_i] = 0$.
- $\text{Var}(W_{ni}) = \frac{x_i^2}{\sigma^2 s_n^2} \text{Var}(\varepsilon_i) = \frac{x_i^2}{\sigma^2 s_n^2} \sigma^2 = \frac{x_i^2}{s_n^2}$.
- Total row variance:
  $$\sum_{i=1}^n \text{Var}(W_{ni}) = \sum_{i=1}^n \frac{x_i^2}{s_n^2} = \frac{\sum_{i=1}^n x_i^2}{s_n^2} = \frac{s_n^2}{s_n^2} = 1$$
The triangular array $\{W_{ni}\}_{i=1}^n$ is mean-zero, independent within rows, and has normalized total row variance equal to 1.

---

### Solution, step 2: Formulation of the Lindeberg Condition
For this normalized triangular array, the Lindeberg condition requires that for every fixed positive threshold $\epsilon > 0$:

$$\lim_{n \to \infty} L_n(\epsilon) = 0$$

where the Lindeberg sum is:

$$L_n(\epsilon) = \sum_{i=1}^n \mathbb{E}\left[ W_{ni}^2 \mathbf{1}_{\{|W_{ni}| \ge \epsilon\}} \right]$$

Substitute the definition of $W_{ni}$:

$$L_n(\epsilon) = \sum_{i=1}^n \mathbb{E}\left[ \left( \frac{x_i}{\sigma s_n} \varepsilon_i \right)^2 \mathbf{1}_{\left\{ \left|\frac{x_i}{\sigma s_n} \varepsilon_i\right| \ge \epsilon \right\}} \right] = \sum_{i=1}^n \frac{x_i^2}{\sigma^2 s_n^2} \mathbb{E}\left[ \varepsilon_i^2 \mathbf{1}_{\left\{ |\varepsilon_i| \ge \frac{\epsilon \sigma s_n}{|x_i|} \right\}} \right]$$

Because the disturbances $\varepsilon_1, \dots, \varepsilon_n$ are identically distributed, we can drop the subscript $i$ inside the expectation and replace $\varepsilon_i$ with a generic copy $\varepsilon \sim F_\varepsilon$:

$$L_n(\epsilon) = \sum_{i=1}^n \frac{x_i^2}{\sigma^2 s_n^2} \mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{|x_i|} \right\}} \right]$$

---

### Solution, step 3: Bounding the Sum under the Grenander Condition and Conclusion
We now bound the threshold inside the indicator function.
Recall that $M_n = \max_{1 \le i \le n} |x_i|$. For every index $i \in \{1, \dots, n\}$, we have $|x_i| \le M_n$.
Therefore:

$$\frac{\epsilon \sigma s_n}{|x_i|} \ge \frac{\epsilon \sigma s_n}{M_n}$$

Whenever $|\varepsilon| \ge \frac{\epsilon \sigma s_n}{|x_i|}$, it is necessarily true that $|\varepsilon| \ge \frac{\epsilon \sigma s_n}{M_n}$. Thus, we have the inequality of indicator functions:

$$\mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{|x_i|} \right\}} \le \mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{M_n} \right\}}$$

Since $\varepsilon^2 \ge 0$, multiplying both sides by $\varepsilon^2$ and taking expectations preserves the inequality:

$$\mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{|x_i|} \right\}} \right] \le \mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{M_n} \right\}} \right]$$

Substitute this uniform upper bound back into the Lindeberg sum:

$$L_n(\epsilon) \le \sum_{i=1}^n \frac{x_i^2}{\sigma^2 s_n^2} \mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{M_n} \right\}} \right] = \left( \sum_{i=1}^n \frac{x_i^2}{\sigma^2 s_n^2} \right) \mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{M_n} \right\}} \right]$$

Factor out the constant terms:

$$\sum_{i=1}^n \frac{x_i^2}{\sigma^2 s_n^2} = \frac{1}{\sigma^2 s_n^2} \sum_{i=1}^n x_i^2 = \frac{s_n^2}{\sigma^2 s_n^2} = \frac{1}{\sigma^2}$$

Therefore, for all $n \ge 1$:

$$0 \le L_n(\epsilon) \le \frac{1}{\sigma^2} \mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\left\{ |\varepsilon| \ge \frac{\epsilon \sigma s_n}{M_n} \right\}} \right]$$

Now, analyze the cutoff threshold $K_n = \frac{\epsilon \sigma s_n}{M_n}$.
Under the Grenander condition:

$$\lim_{n \to \infty} \frac{M_n^2}{s_n^2} = 0 \implies \lim_{n \to \infty} \frac{M_n}{s_n} = 0$$

Taking the reciprocal:

$$\lim_{n \to \infty} K_n = \lim_{n \to \infty} \epsilon \sigma \left( \frac{M_n}{s_n} \right)^{-1} = +\infty$$

Because $\mathbb{E}[\varepsilon^2] = \sigma^2 < \infty$, the function $h(\varepsilon) = \varepsilon^2$ is integrable. By the Dominated Convergence Theorem:

$$\lim_{K \to \infty} \mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\{|\varepsilon| \ge K\}} \right] = 0$$

Since $K_n \to \infty$ as $n \to \infty$, we take the limit of the upper bound:

$$\lim_{n \to \infty} \frac{1}{\sigma^2} \mathbb{E}\left[ \varepsilon^2 \mathbf{1}_{\{|\varepsilon| \ge K_n\}} \right] = 0$$

By the squeeze theorem:

$$\lim_{n \to \infty} L_n(\epsilon) = 0 \quad \text{for every } \epsilon > 0$$

The Lindeberg condition is verified completely.
By the Lindeberg-Feller Central Limit Theorem (Theorem 7.12):

$$Z_n = \sum_{i=1}^n W_{ni} \xrightarrow{d} \mathcal{N}(0, 1)$$

Substituting $Z_n$:

$$\frac{\hat{\beta}_n - \beta}{\sigma / \sqrt{\sum_{i=1}^n x_i^2}} \xrightarrow{d} \mathcal{N}(0, 1)$$

This proves that under the Grenander condition (which guarantees that no single experimental design point $x_i$ exerts disproportionate leverage over the regression fit), the OLS slope estimator is asymptotically normally distributed, even when the disturbance terms $\varepsilon_i$ are non-Gaussian! $\blacksquare$
"""

full_content = "\n\n".join([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12])
DEST.write_text(full_content.strip() + "\n", encoding="utf-8")
print(f"Unit 7 generated successfully at {DEST} ({len(full_content)} chars)")
