# -*- coding: utf-8 -*-
"""
build_top_unit1.py
Constructs Unit 1: Metric Spaces: Topologies, Completeness & Baire's Category Theorem
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Metric Spaces: Topologies, Completeness & Baire's Category Theorem",
        "leadSummary": "Foundations of metric topology: distance axioms, classical metric spaces (Euclidean, taxicab, Chebyshev, sequence spaces $\\ell^p$ and $\\ell^\\infty$, function space $C[a, b]$), open balls and open sets, equivalent metrics, Cauchy sequences and completeness, Cantor's Intersection Theorem, nowhere dense and meager sets, Baire's Category Theorem with complete proof, and the Banach Fixed-Point Contraction Mapping Theorem.",
        "simulations": ["sim_top_metric_balls_p"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Metric Spaces: Definitions, Axioms & Classical Examples",
                "content": r"""### 1. The Metric Axioms

The concept of a metric space, introduced by Maurice Fréchet in 1906, abstracts the intuitive notion of distance between two points into a rigorous mathematical framework.

> **Definition 1.1 (Metric Space):**
> Let $X$ be a non-empty set. A **metric** (or **distance function**) on $X$ is a function $d: X \times X \to \mathbb{R}$ satisfying the following four axioms for all $x, y, z \in X$:
> 1. **Non-negativity:** $d(x, y) \ge 0$.
> 2. **Identity of Indiscernibles:** $d(x, y) = 0 \iff x = y$.
> 3. **Symmetry:** $d(x, y) = d(y, x)$.
> 4. **Triangle Inequality:** $d(x, z) \le d(x, y) + d(y, z)$.
>
> The ordered pair $(X, d)$ is called a **metric space**. The elements of $X$ are called **points**.

---

### 2. Classical Examples of Metric Spaces

> **Example 1.1 (Euclidean and $\ell^p$ Spaces on $\mathbb{R}^n$):**
> For $x = (x_1, \dots, x_n)$ and $y = (y_1, \dots, y_n)$ in $\mathbb{R}^n$:
> - **Euclidean Metric ($p = 2$):**
>   $$d_2(x, y) = \left( \sum_{i=1}^n |x_i - y_i|^2 \right)^{1/2}$$
> - **Taxicab / Manhattan Metric ($p = 1$):**
>   $$d_1(x, y) = \sum_{i=1}^n |x_i - y_i|$$
> - **Chebyshev / Maximum Metric ($p = \infty$):**
>   $$d_\infty(x, y) = \max_{1 \le i \le n} |x_i - y_i|$$
> - **General $\ell^p$ Metric ($1 \le p < \infty$):**
>   $$d_p(x, y) = \left( \sum_{i=1}^n |x_i - y_i|^p \right)^{1/p}$$
> The triangle inequality for $d_p$ is precisely **Minkowski's Inequality**:
> $$\left( \sum_{i=1}^n |a_i + b_i|^p \right)^{1/p} \le \left( \sum_{i=1}^n |a_i|^p \right)^{1/p} + \left( \sum_{i=1}^n |b_i|^p \right)^{1/p}$$

> **Example 1.2 (Sequence Space $\ell^\infty$ and $\ell^p$):**
> Let $\ell^\infty$ denote the space of all bounded real sequences $x = (x_n)_{n=1}^\infty$ with norm $\|x\|_\infty = \sup_{n \ge 1} |x_n|$. The metric is:
> $$d_\infty(x, y) = \sup_{n \ge 1} |x_n - y_n|$$
> For $1 \le p < \infty$, the space $\ell^p$ consists of sequences with $\sum_{n=1}^\infty |x_n|^p < \infty$, with metric:
> $$d_p(x, y) = \left( \sum_{n=1}^\infty |x_n - y_n|^p \right)^{1/p}$$

> **Example 1.3 (Function Space $C[a, b]$ with Uniform Metric):**
> Let $C[a, b]$ be the set of all real-valued continuous functions on the closed interval $[a, b]$. The **uniform metric** (or Chebyshev metric) is:
> $$d_\infty(f, g) = \|f - g\|_\infty = \max_{t \in [a, b]} |f(t) - g(t)|$$
> By the Extreme Value Theorem, the maximum is always attained and finite.

> **Example 1.4 (The Discrete Metric):**
> For any non-empty set $X$, the **discrete metric** is defined by:
> $$d(x, y) = \begin{cases} 0 & \text{if } x = y \\ 1 & \text{if } x \ne y \end{cases}$$
> It satisfies all metric axioms trivially.

> **Example 1.5 (Ultrametric Spaces):**
> A metric space $(X, d)$ is an **ultrametric space** if it satisfies the **strong triangle inequality**:
> $$d(x, z) \le \max\{d(x, y), d(y, z)\}$$
> A canonical example is the $p$-adic metric $d_p(x, y) = |x - y|_p$ on $\mathbb{Q}$. In an ultrametric space, every triangle is isosceles, and every point inside an open ball is its center!"""
            },
            {
                "secNumber": "1.2",
                "title": "Open Balls, Open Sets & Equivalent Metrics",
                "content": r"""### 1. Open and Closed Balls

> **Definition 1.2 (Open and Closed Balls):**
> Let $(X, d)$ be a metric space, $x_0 \in X$, and $r > 0$.
> - The **open ball** of radius $r$ centered at $x_0$ is:
>   $$B(x_0, r) = \{x \in X : d(x, x_0) < r\}$$
> - The **closed ball** of radius $r$ centered at $x_0$ is:
>   $$\bar{B}(x_0, r) = \{x \in X : d(x, x_0) \le r\}$$
> - The **sphere** of radius $r$ centered at $x_0$ is:
>   $$S(x_0, r) = \{x \in X : d(x, x_0) = r\}$$

---

### 2. Open Sets and the Metric Topology

> **Definition 1.3 (Open Set in a Metric Space):**
> A subset $U \subseteq X$ is called **open** in $(X, d)$ if for every point $x \in U$, there exists a radius $r > 0$ such that the entire open ball is contained in $U$:
> $$B(x, r) \subseteq U$$

> **Theorem 1.1 (Properties of Open Sets):**
> Let $(X, d)$ be a metric space.
> 1. The empty set $\emptyset$ and the whole space $X$ are open.
> 2. The union of any arbitrary family of open sets is open:
>    $$\bigcup_{\alpha \in I} U_\alpha \text{ is open whenever each } U_\alpha \text{ is open}$$
> 3. The intersection of any finite collection of open sets is open:
>    $$\bigcap_{i=1}^n U_i \text{ is open whenever each } U_i \text{ is open}$$

> **Proof:**
> 1. $\emptyset$ is open vacuously (there are no points in $\emptyset$). For $X$, for any $x \in X$, $B(x, 1) \subseteq X$ holds trivially.
> 2. Let $U = \bigcup_{\alpha \in I} U_\alpha$. For any $x \in U$, $x \in U_{\alpha_0}$ for some $\alpha_0 \in I$. Since $U_{\alpha_0}$ is open, there exists $r > 0$ such that $B(x, r) \subseteq U_{\alpha_0} \subseteq U$. Thus $U$ is open.
> 3. Let $V = \bigcap_{i=1}^n U_i$. For any $x \in V$, $x \in U_i$ for all $i \in \{1, \dots, n\}$.
>    Since each $U_i$ is open, there exists $r_i > 0$ such that $B(x, r_i) \subseteq U_i$.
>    Let $r = \min\{r_1, r_2, \dots, r_n\} > 0$ (since $n$ is finite!).
>    Then for each $i$, $B(x, r) \subseteq B(x, r_i) \subseteq U_i$.
>    Hence $B(x, r) \subseteq \bigcap_{i=1}^n U_i = V$, proving $V$ is open. $\blacksquare$

> **Definition 1.4 (Topology Induced by a Metric):**
> The collection $\mathcal{T}_d = \{U \subseteq X : U \text{ is open in } (X, d)\}$ is called the **topology induced by the metric $d$**.

---

### 3. Equivalent Metrics

Two distinct metrics on the same underlying set $X$ can generate the exact same family of open sets.

> **Definition 1.5 (Topological and Lipschitz Equivalence):**
> Let $d_1$ and $d_2$ be two metrics on $X$.
> 1. $d_1$ and $d_2$ are **topologically equivalent** if they induce the same topology: $\mathcal{T}_{d_1} = \mathcal{T}_{d_2}$.
> 2. $d_1$ and $d_2$ are **strongly (Lipschitz) equivalent** if there exist constants $c_1, c_2 > 0$ such that for all $x, y \in X$:
>    $$c_1 d_1(x, y) \le d_2(x, y) \le c_2 d_1(x, y)$$

> **Proposition 1.1:**
> Lipschitz equivalence implies topological equivalence.
> In particular, on $\mathbb{R}^n$, the metrics $d_1, d_2, d_\infty$ and all $d_p$ ($1 \le p < \infty$) are strongly equivalent:
> $$d_\infty(x, y) \le d_2(x, y) \le d_1(x, y) \le n d_\infty(x, y)$$
> and therefore they all generate the identical Euclidean topology on $\mathbb{R}^n$."""
            },
            {
                "secNumber": "1.3",
                "title": "Sequences, Cauchy Completeness & Cantor's Intersection Theorem",
                "content": r"""### 1. Convergence of Sequences

> **Definition 1.6 (Sequence Convergence):**
> A sequence $(x_n)_{n=1}^\infty$ in a metric space $(X, d)$ is said to **converge** to a limit $x \in X$ (denoted $x_n \to x$ or $\lim_{n \to \infty} x_n = x$) if:
> $$\forall \varepsilon > 0, \; \exists N \in \mathbb{N} \text{ such that } \forall n \ge N, \; d(x_n, x) < \varepsilon$$

> **Proposition 1.2 (Uniqueness of Limits):**
> In any metric space $(X, d)$, limits of sequences are unique:
> If $x_n \to x$ and $x_n \to y$, then $x = y$.

> **Proof:**
> By the triangle inequality:
> $$0 \le d(x, y) \le d(x, x_n) + d(x_n, y)$$
> For any $\varepsilon > 0$, choose $N$ large enough that $d(x_n, x) < \varepsilon/2$ and $d(x_n, y) < \varepsilon/2$ for all $n \ge N$.
> Then $d(x, y) < \varepsilon/2 + \varepsilon/2 = \varepsilon$.
> Since this holds for all $\varepsilon > 0$, we have $d(x, y) = 0 \implies x = y$. $\blacksquare$

---

### 2. Cauchy Sequences and Completeness

> **Definition 1.7 (Cauchy Sequence & Complete Metric Space):**
> 1. A sequence $(x_n)_{n=1}^\infty$ in $(X, d)$ is a **Cauchy sequence** if:
>    $$\forall \varepsilon > 0, \; \exists N \in \mathbb{N} \text{ such that } \forall m, n \ge N, \; d(x_m, x_n) < \varepsilon$$
> 2. A metric space $(X, d)$ is called **complete** if every Cauchy sequence in $X$ converges to a limit point that belongs to $X$.

Every convergent sequence is Cauchy, but the converse is not always true!
- $(\mathbb{R}, |\cdot|)$ is complete.
- $(\mathbb{Q}, |\cdot|)$ is **not complete** (e.g. sequence of rational approximations to $\sqrt{2}$ is Cauchy in $\mathbb{Q}$, but its limit $\sqrt{2} \notin \mathbb{Q}$).
- The open interval $(0, 1)$ with the standard metric is not complete (the sequence $x_n = 1/n$ is Cauchy, but its limit $0 \notin (0, 1)$).

---

### 3. Cantor's Intersection Theorem

How is completeness characterized purely in terms of closed sets?

> **Definition 1.8 (Diameter of a Subset):**
> For non-empty $A \subseteq X$, the **diameter** is $\operatorname{diam}(A) = \sup \{d(x, y) : x, y \in A\}$.

> **Theorem 1.2 (Cantor's Intersection Theorem):**
> A metric space $(X, d)$ is **complete** if and only if for every nested sequence of non-empty closed subsets:
> $$F_1 \supseteq F_2 \supseteq F_3 \supseteq \cdots \supseteq F_n \supseteq \cdots$$
> satisfying $\lim_{n \to \infty} \operatorname{diam}(F_n) = 0$, the intersection contains **exactly one point**:
> $$\bigcap_{n=1}^\infty F_n = \{x^*\}$$

> **Proof:**
> **($\Rightarrow$) Assume $X$ is complete:**
> For each $n \in \mathbb{N}$, choose $x_n \in F_n$.
> Since $F_m \subseteq F_n$ for all $m \ge n$, both $x_m, x_n \in F_n$.
> Thus $d(x_m, x_n) \le \operatorname{diam}(F_n)$.
> Since $\lim_{n \to \infty} \operatorname{diam}(F_n) = 0$, given $\varepsilon > 0$, choose $N$ such that $\operatorname{diam}(F_N) < \varepsilon$.
> Then for all $m, n \ge N$, $d(x_m, x_n) < \varepsilon$.
> Hence $(x_n)$ is a Cauchy sequence!
> Because $X$ is complete, there exists $x^* \in X$ such that $x_n \to x^*$.
> Since each $F_k$ is closed and the tail $(x_n)_{n=k}^\infty \subseteq F_k$, the limit $x^* \in F_k$ for every $k$.
> Thus $x^* \in \bigcap_{n=1}^\infty F_n$.
> If $y \in \bigcap F_n$, then $d(x^*, y) \le \operatorname{diam}(F_n) \to 0$, forcing $y = x^*$.
>
> **($\Leftarrow$) Assume the nested intersection property holds:**
> Let $(x_n)$ be any Cauchy sequence in $X$.
> For each $k \in \mathbb{N}$, let $A_k = \{x_n : n \ge k\}$ and let $F_k = \overline{A_k}$ be its closure.
> Then $F_1 \supseteq F_2 \supseteq \cdots$ is a nested sequence of non-empty closed sets.
> Since $(x_n)$ is Cauchy, $\operatorname{diam}(F_k) = \operatorname{diam}(A_k) \to 0$.
> By hypothesis, there is a unique $x^* \in \bigcap F_k$.
> Since $x^* \in \overline{A_k}$, $d(x_n, x^*) \le \operatorname{diam}(F_k) \to 0$, so $x_n \to x^* \in X$.
> Hence $X$ is complete. $\blacksquare$"""
            },
            {
                "secNumber": "1.4",
                "title": "Nowhere Dense Sets & Baire's Category Theorem",
                "content": r"""### 1. Topological Meagerness (First and Second Category)

René Baire introduced the notions of "category" in 1899 to measure the topological size and density of sets.

> **Definition 1.9 (Dense and Nowhere Dense Sets):**
> Let $(X, d)$ be a metric space.
> 1. A subset $A \subseteq X$ is **dense** in $X$ if its closure is the entire space: $\bar{A} = X$.
> 2. A subset $E \subseteq X$ is **nowhere dense** if its closure has empty interior:
>    $$\operatorname{int}(\bar{E}) = \emptyset$$
>    Equivalently, every non-empty open set $U$ contains a non-empty open ball disjoint from $E$.

> **Definition 1.10 (Meager / First Category Sets):**
> 1. A subset $M \subseteq X$ is called **meager** (or of **first category**) in $X$ if it is a countable union of nowhere dense sets:
>    $$M = \bigcup_{n=1}^\infty E_n, \qquad \text{where each } \operatorname{int}(\bar{E}_n) = \emptyset$$
> 2. A subset that is not meager is called of **second category** (or **non-meager**).
> 3. A subset $R \subseteq X$ is called **residual** (or **comeager**) if its complement $X \setminus R$ is meager.

---

### 2. Baire's Category Theorem

Baire's Theorem asserts that complete metric spaces cannot be topologically small!

> **Theorem 1.3 (Baire's Category Theorem - BCT):**
> Let $(X, d)$ be a **complete metric space**.
> 1. If $\{U_n\}_{n=1}^\infty$ is a countable collection of **dense open subsets** of $X$, then their intersection is **dense** in $X$:
>    $$\overline{\bigcap_{n=1}^\infty U_n} = X$$
> 2. In particular, a complete metric space $X \ne \emptyset$ is **of second category in itself**; that is, $X$ cannot be represented as a countable union of nowhere dense sets.

> **Proof:**
> We prove formulation (1).
> Let $W \subseteq X$ be any non-empty open set. We must prove that $W \cap \left(\bigcap_{n=1}^\infty U_n\right) \ne \emptyset$.
>
> **Step 1:**
> Since $U_1$ is dense in $X$, $W \cap U_1$ is a non-empty open set.
> Therefore, we can choose a point $x_1 \in W \cap U_1$ and a radius $0 < r_1 < 1$ such that the closed ball satisfies:
> $$\bar{B}(x_1, r_1) \subseteq W \cap U_1$$
>
> **Step 2:**
> Now consider $B(x_1, r_1)$ and $U_2$.
> Since $U_2$ is dense in $X$, the open set $B(x_1, r_1) \cap U_2$ is non-empty.
> Hence, we can choose a point $x_2$ and radius $0 < r_2 < r_1 / 2 < 1/2$ such that:
> $$\bar{B}(x_2, r_2) \subseteq B(x_1, r_1) \cap U_2 \subseteq \bar{B}(x_1, r_1) \cap U_2$$
>
> **Inductive Step:**
> Continuing this process inductively: for each $n \ge 2$, having constructed $\bar{B}(x_{n-1}, r_{n-1})$, since $U_n$ is dense and $B(x_{n-1}, r_{n-1})$ is non-empty and open, their intersection is non-empty.
> We choose $x_n \in B(x_{n-1}, r_{n-1}) \cap U_n$ and $0 < r_n < r_{n-1}/2 < 2^{-n}$ such that:
> $$\bar{B}(x_n, r_n) \subseteq B(x_{n-1}, r_{n-1}) \cap U_n$$
>
> We have constructed a nested sequence of non-empty closed balls:
> $$\bar{B}(x_1, r_1) \supseteq \bar{B}(x_2, r_2) \supseteq \bar{B}(x_3, r_3) \supseteq \cdots$$
> with $\operatorname{diam}(\bar{B}(x_n, r_n)) \le 2 r_n < 2^{1-n} \to 0$ as $n \to \infty$.
>
> **Conclusion via Cantor's Intersection Theorem:**
> Since $(X, d)$ is complete, by Cantor's Intersection Theorem (Theorem 1.2), there exists a point $x^* \in X$ such that:
> $$x^* \in \bigcap_{n=1}^\infty \bar{B}(x_n, r_n)$$
> By construction:
> - For $n = 1$: $x^* \in \bar{B}(x_1, r_1) \subseteq W \cap U_1 \implies x^* \in W$.
> - For every $n \ge 1$: $x^* \in \bar{B}(x_n, r_n) \subseteq U_n \implies x^* \in U_n$.
>
> Therefore, $x^* \in W \cap \left( \bigcap_{n=1}^\infty U_n \right)$.
> Since $W$ was an arbitrary non-empty open set, the intersection $\bigcap_{n=1}^\infty U_n$ intersects every non-empty open set in $X$.
> Thus, $\bigcap_{n=1}^\infty U_n$ is dense in $X$. $\blacksquare$"""
            },
            {
                "secNumber": "1.5",
                "title": "Continuous Function Spaces & The Banach Fixed-Point Theorem",
                "content": r"""### 1. Completeness of $C[a, b]$ Under the Uniform Metric

> **Theorem 1.4 (Completeness of $(C[a, b], d_\infty)$):**
> The metric space of continuous functions $(C[a, b], d_\infty)$ equipped with the uniform metric $d_\infty(f, g) = \max_{t \in [a, b]} |f(t) - g(t)|$ is a **complete metric space** (a Banach space).

> **Proof:**
> Let $(f_n)_{n=1}^\infty$ be a Cauchy sequence in $(C[a, b], d_\infty)$.
> Given $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that for all $m, n \ge N$:
> $$\max_{t \in [a, b]} |f_n(t) - f_m(t)| < \varepsilon$$
> For each fixed point $t_0 \in [a, b]$:
> $$|f_n(t_0) - f_m(t_0)| \le d_\infty(f_n, f_m) < \varepsilon$$
> Thus, the real sequence $(f_n(t_0))_{n=1}^\infty$ is Cauchy in $\mathbb{R}$.
> Since $\mathbb{R}$ is complete, it converges to a real number. Define the pointwise limit function:
> $$f(t) = \lim_{n \to \infty} f_n(t), \qquad \forall t \in [a, b]$$
>
> Letting $m \to \infty$ in $|f_n(t) - f_m(t)| < \varepsilon$, we obtain:
> $$|f_n(t) - f(t)| \le \varepsilon, \qquad \forall n \ge N, \; \forall t \in [a, b]$$
> This means $f_n \to f$ **uniformly** on $[a, b]$.
> By the Uniform Limit Theorem of analysis, the uniform limit of continuous functions is continuous.
> Thus $f \in C[a, b]$, and $d_\infty(f_n, f) \to 0$.
> Hence $(C[a, b], d_\infty)$ is complete. $\blacksquare$

---

### 2. The Banach Fixed-Point Contraction Mapping Theorem

One of the most powerful analytical applications of complete metric spaces is Stefan Banach's 1922 Fixed-Point Theorem.

> **Definition 1.11 (Contraction Mapping):**
> Let $(X, d)$ be a metric space. A mapping $T: X \to X$ is called a **contraction** if there exists a constant $0 \le k < 1$ (the contraction factor) such that:
> $$d(T(x), T(y)) \le k \, d(x, y), \qquad \forall x, y \in X$$

> **Theorem 1.5 (Banach Fixed-Point Theorem):**
> Let $(X, d)$ be a **non-empty complete metric space**, and let $T: X \to X$ be a contraction mapping with factor $k \in [0, 1)$.
> Then:
> 1. $T$ has a **unique fixed point** $x^* \in X$ (i.e., $T(x^*) = x^*$).
> 2. For any arbitrary starting point $x_0 \in X$, the Picard iteration sequence defined by $x_{n+1} = T(x_n)$ converges to $x^*$:
>    $$\lim_{n \to \infty} x_n = x^*$$
> 3. The error estimate satisfies:
>    $$d(x_n, x^*) \le \frac{k^n}{1 - k} d(x_0, x_1)$$

> **Proof:**
> **Existence:**
> For any $n \in \mathbb{N}$, by induction on the contraction property:
> $$d(x_n, x_{n+1}) = d(T(x_{n-1}), T(x_n)) \le k d(x_{n-1}, x_n) \le k^n d(x_0, x_1)$$
> For any $m > n$:
> $$d(x_n, x_m) \le \sum_{j=n}^{m-1} d(x_j, x_{j+1}) \le \sum_{j=n}^{m-1} k^j d(x_0, x_1) = k^n d(x_0, x_1) \sum_{i=0}^{m-n-1} k^i < \frac{k^n}{1 - k} d(x_0, x_1)$$
> Since $0 \le k < 1$, $\lim_{n \to \infty} k^n = 0$.
> Thus, for any $\varepsilon > 0$, choosing $N$ large enough makes $d(x_n, x_m) < \varepsilon$ for all $m > n \ge N$.
> Hence $(x_n)$ is a Cauchy sequence in $X$.
>
> Because $(X, d)$ is complete, there exists $x^* \in X$ such that $x_n \to x^*$.
> Since contractions are Lipschitz continuous ($d(T(x), T(y)) \le k d(x, y)$):
> $$T(x^*) = T(\lim_{n \to \infty} x_n) = \lim_{n \to \infty} T(x_n) = \lim_{n \to \infty} x_{n+1} = x^*$$
> Thus $x^*$ is indeed a fixed point.
>
> **Uniqueness:**
> If $y^* \in X$ is another fixed point ($T(y^*) = y^*$), then:
> $$d(x^*, y^*) = d(T(x^*), T(y^*)) \le k d(x^*, y^*)$$
> $$(1 - k) d(x^*, y^*) \le 0$$
> Since $1 - k > 0$ and $d(x^*, y^*) \ge 0$, we must have $d(x^*, y^*) = 0 \implies x^* = y^*$. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "prob_1_1",
                "tier": "Foundational",
                "title": "Topological Equivalence of Norms on Finite-Dimensional Spaces",
                "statement": r"""Prove that on $\mathbb{R}^n$, the three classical metrics:
$$d_1(x, y) = \sum_{i=1}^n |x_i - y_i|, \qquad d_2(x, y) = \left( \sum_{i=1}^n |x_i - y_i|^2 \right)^{1/2}, \qquad d_\infty(x, y) = \max_{1 \le i \le n} |x_i - y_i|$$
are strongly (Lipschitz) equivalent, and establish the sharp bounding inequalities:
$$d_\infty(x, y) \le d_2(x, y) \le d_1(x, y) \le \sqrt{n} \, d_2(x, y) \le n \, d_\infty(x, y)$$
Conclude that they induce the exact same metric topology on $\mathbb{R}^n$.""",
                "solution": r"""### 1. Inequality 1: $d_\infty(x, y) \le d_2(x, y)$

Let $z = x - y \in \mathbb{R}^n$. Let $j \in \{1, \dots, n\}$ be the index where $|z_j| = \max_i |z_i| = \|z\|_\infty$.
Then:
$$d_\infty(x, y)^2 = |z_j|^2 \le \sum_{i=1}^n |z_i|^2 = d_2(x, y)^2$$
Taking square roots of both sides gives:
$$d_\infty(x, y) \le d_2(x, y)$$

---

### 2. Inequality 2: $d_2(x, y) \le d_1(x, y)$

Squaring the $L^1$ norm:
$$d_1(x, y)^2 = \left( \sum_{i=1}^n |z_i| \right)^2 = \sum_{i=1}^n |z_i|^2 + \sum_{i \ne j} |z_i| |z_j| \ge \sum_{i=1}^n |z_i|^2 = d_2(x, y)^2$$
Since both metrics are non-negative:
$$d_2(x, y) \le d_1(x, y)$$

---

### 3. Inequality 3: $d_1(x, y) \le \sqrt{n} \, d_2(x, y)$

Applying the **Cauchy-Schwarz Inequality** to the vectors $(|z_1|, \dots, |z_n|)$ and $(1, 1, \dots, 1)$:
$$d_1(x, y) = \sum_{i=1}^n 1 \cdot |z_i| \le \left( \sum_{i=1}^n 1^2 \right)^{1/2} \left( \sum_{i=1}^n |z_i|^2 \right)^{1/2} = \sqrt{n} \, d_2(x, y)$$

---

### 4. Inequality 4: $\sqrt{n} \, d_2(x, y) \le n \, d_\infty(x, y)$

From $d_2(x, y)^2 = \sum_{i=1}^n |z_i|^2 \le \sum_{i=1}^n \|z\|_\infty^2 = n \|z\|_\infty^2$:
$$d_2(x, y) \le \sqrt{n} \, d_\infty(x, y) \implies \sqrt{n} \, d_2(x, y) \le n \, d_\infty(x, y)$$
Combining all inequalities gives the chain:
$$d_\infty(x, y) \le d_2(x, y) \le d_1(x, y) \le \sqrt{n} \, d_2(x, y) \le n \, d_\infty(x, y)$$

---

### 5. Topological Equivalence

For any open ball $B_{d_\infty}(x, r)$, we have $B_{d_1}(x, r) \subseteq B_{d_2}(x, r) \subseteq B_{d_\infty}(x, r)$.
Conversely, $B_{d_\infty}(x, r/n) \subseteq B_{d_1}(x, r)$.
Thus, any set open in one metric contains an open ball in any of the other metrics.
Therefore:
$$\mathcal{T}_{d_1} = \mathcal{T}_{d_2} = \mathcal{T}_{d_\infty}$$
They generate the identical Euclidean topology on $\mathbb{R}^n$."""
            },
            {
                "id": "prob_1_2",
                "tier": "Advanced",
                "title": "Baire Category Proof: Uncountability of Complete Spaces Without Isolated Points",
                "statement": r"""Prove using Baire's Category Theorem that:
1. In any non-empty complete metric space $(X, d)$, if a point $x_0 \in X$ is not an isolated point, then the singleton $\{x_0\}$ is nowhere dense in $X$.
2. Every non-empty complete metric space without isolated points must be **uncountably infinite**.
3. Deduce as an immediate corollary that $\mathbb{R}$ and the Cantor set are uncountably infinite.""",
                "solution": r"""### 1. Singletons are Nowhere Dense

Let $x_0 \in X$.
- The singleton set $\{x_0\}$ is closed in any metric space because its complement $X \setminus \{x_0\} = \{x \in X : d(x, x_0) > 0\} = \bigcup_{r > 0} \{x : d(x, x_0) > r\}$ is open.
- The closure of $\{x_0\}$ is simply $\{x_0\}$ itself: $\overline{\{x_0\}} = \{x_0\}$.
- Now consider the interior $\operatorname{int}(\{x_0\})$.
  If $\operatorname{int}(\{x_0\}) \ne \emptyset$, there must exist an open ball $B(x_0, r) \subseteq \{x_0\}$ for some $r > 0$.
  This means $B(x_0, r) = \{x_0\}$, which implies that $x_0$ has no other points within distance $r$.
  By definition, this would mean that $x_0$ is an **isolated point**!
- Therefore, if $x_0$ is **not** an isolated point, no such ball exists, so:
  $$\operatorname{int}(\overline{\{x_0\}}) = \operatorname{int}(\{x_0\}) = \emptyset$$
  Hence, $\{x_0\}$ is a **nowhere dense** subset of $X$.

---

### 2. Complete Spaces Without Isolated Points are Uncountable

Suppose for contradiction that $X$ is countably infinite:
$$X = \{x_1, x_2, x_3, \dots\} = \bigcup_{n=1}^\infty \{x_n\}$$
Since $X$ has no isolated points, by Part 1, every singleton $\{x_n\}$ is nowhere dense in $X$.
Thus, $X$ is a countable union of nowhere dense subsets:
$$X = \bigcup_{n=1}^\infty \{x_n\} \implies X \text{ is of first category (meager) in itself!}$$
However, $X$ is a non-empty complete metric space.
By **Baire's Category Theorem** (Theorem 1.3), $X$ must be of **second category** (non-meager) in itself.
This contradiction proves that $X$ cannot be countably infinite!
Since $X$ is non-empty and has no isolated points, it cannot be finite either.
Therefore, $X$ must be **uncountably infinite**.

---

### 3. Application to $\mathbb{R}$ and the Cantor Set

- The real line $\mathbb{R}$ with standard metric $d(x, y) = |x - y|$ is complete, and no real number is isolated (every ball $(x - r, x + r)$ contains infinitely many points).
  By Part 2, $\mathbb{R}$ is uncountably infinite.
- The ternary Cantor set $C \subset [0, 1]$ is a closed subset of $\mathbb{R}$, hence $(C, |\cdot|)$ is a complete metric space.
  It is well-known that $C$ is perfect (it contains no isolated points).
  Hence, by Part 2, the Cantor set $C$ is uncountably infinite."""
            },
            {
                "id": "prob_1_3",
                "tier": "Honors / Proof Challenge",
                "title": "Baire's Category Theorem: Complete Rigorous Derivation",
                "statement": r"""Provide the complete, rigorous mathematical proof of Baire's Category Theorem for complete metric spaces in its dual formulation:

Let $(X, d)$ be a complete metric space. Prove that:
1. If $X = \bigcup_{n=1}^\infty F_n$ where each $F_n$ is a closed subset of $X$, then at least one $F_n$ must have non-empty interior:
   $$\exists n_0 \in \mathbb{N} \quad \text{such that} \quad \operatorname{int}(F_{n_0}) \ne \emptyset$$
2. Show that formulation (1) is logically equivalent to: the countable intersection of dense open subsets of $X$ is dense in $X$.
3. Give an example showing that Baire's Category Theorem fails if $(X, d)$ is not complete.""",
                "solution": r"""### 1. Proof of the Closed Set Formulation

Suppose for contradiction that for **every** $n \in \mathbb{N}$, $\operatorname{int}(F_n) = \emptyset$.
Since $F_n$ is closed, $\bar{F}_n = F_n$, so $\operatorname{int}(\bar{F}_n) = \emptyset$.
This means each $F_n$ is nowhere dense in $X$.
Let $U_n = X \setminus F_n$.
- Since $F_n$ is closed, $U_n$ is open.
- We claim $U_n$ is dense in $X$:
  For any non-empty open set $W \subseteq X$, if $W \cap U_n = \emptyset$, then $W \subseteq F_n$.
  This would imply $W \subseteq \operatorname{int}(F_n)$, contradicting $\operatorname{int}(F_n) = \emptyset$.
  Thus $W \cap U_n \ne \emptyset$, so $U_n$ is dense in $X$.

By Baire's Category Theorem (open formulation, Theorem 1.3), the intersection of dense open sets in a complete metric space is dense:
$$\overline{\bigcap_{n=1}^\infty U_n} = X$$
In particular, $\bigcap_{n=1}^\infty U_n \ne \emptyset$.
By De Morgan's Laws:
$$\bigcap_{n=1}^\infty U_n = \bigcap_{n=1}^\infty (X \setminus F_n) = X \setminus \left( \bigcup_{n=1}^\infty F_n \right)$$
Since $\bigcap U_n \ne \emptyset$, we have:
$$X \setminus \left( \bigcup_{n=1}^\infty F_n \right) \ne \emptyset \implies \bigcup_{n=1}^\infty F_n \ne X$$
This contradicts the hypothesis that $X = \bigcup_{n=1}^\infty F_n$!
Therefore, there exists at least one $n_0$ such that $\operatorname{int}(F_{n_0}) \ne \emptyset$. $\blacksquare$

---

### 2. Logical Equivalence of Both Formulations

Let $U_n$ be dense open subsets of $X$, and let $F_n = X \setminus U_n$.
Then $F_n$ are closed subsets with $\operatorname{int}(F_n) = \emptyset$.
If $V = \bigcap U_n$ were not dense, there would exist an open ball $B_0$ disjoint from $V$.
Then $B_0 \subseteq X \setminus \bigcap U_n = \bigcup F_n$.
Viewing $B_0$ as a complete metric space under a compatible metric, BCT on closed sets forces some $F_n$ to have non-empty interior in $B_0$, contradiction.
Hence both formulations are logically equivalent.

---

### 3. Failure in Non-Complete Spaces

Consider the set of rational numbers $\mathbb{Q}$ with the standard metric $d(x, y) = |x - y|$.
The space $(\mathbb{Q}, d)$ is **not complete**.
Since $\mathbb{Q}$ is countable, we can write:
$$\mathbb{Q} = \{q_1, q_2, q_3, \dots\} = \bigcup_{n=1}^\infty \{q_n\}$$
Each singleton $\{q_n\}$ is closed in $\mathbb{Q}$ and has empty interior: $\operatorname{int}(\{q_n\}) = \emptyset$ (every open interval around $q_n$ contains other rational numbers).
Thus, $\mathbb{Q}$ is a countable union of closed sets with empty interior, yet $\mathbb{Q} = \bigcup \{q_n\}$!
Furthermore, setting $U_n = \mathbb{Q} \setminus \{q_n\}$, each $U_n$ is open and dense in $\mathbb{Q}$, but:
$$\bigcap_{n=1}^\infty U_n = \mathbb{Q} \setminus \bigcup_{n=1}^\infty \{q_n\} = \emptyset$$
The empty set is certainly NOT dense in $\mathbb{Q}$!
This illustrates that completeness of the space is indispensable."""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u1 = get_unit1()
    print(f"Loaded Unit 1: {u1['title']} with {len(u1['sections'])} sections and {len(u1['problems'])} problems.")
