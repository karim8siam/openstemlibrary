# -*- coding: utf-8 -*-
"""
build_top_unit5.py
Constructs Unit 5: Separation Axioms: T0, T1, Hausdorff (T2) & Regular Spaces (T3)
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Separation Axioms: T0, T1, Hausdorff (T2) & Regular Spaces (T3)",
        "leadSummary": "The lower hierarchy of separation axioms: Kolmogorov ($T_0$) spaces, Fréchet ($T_1$) spaces and closed singletons, Hausdorff ($T_2$) spaces and uniqueness of limits, closedness of the diagonal $\\Delta$ in $X \\times X$, regular spaces and $T_3$ spaces, closed neighborhood bases, heredity under arbitrary subspaces, preservation under arbitrary Cartesian products, and classical counterexamples including the Line with Two Origins and the Zariski topology.",
        "simulations": ["sim_top_separation_axioms"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Kolmogorov ($T_0$) & Fréchet ($T_1$) Spaces",
                "content": r"""### 1. The Separation Hierarchy

The separation axioms (named $T$ from the German *Trennungsaxiom*) measure the extent to which points and sets can be distinguished by the open sets of the topology.

---

### 2. Kolmogorov Spaces ($T_0$)

> **Definition 5.1 ($T_0$ / Kolmogorov Axiom):**
> A topological space $(X, \mathcal{T})$ is called a **$T_0$ space** (or **Kolmogorov space**) if for every pair of distinct points $x \ne y \in X$, there exists an open set $U \in \mathcal{T}$ that contains **one** of the points but not the other:
> $$(x \in U \text{ and } y \notin U) \quad \text{or} \quad (y \in U \text{ and } x \notin U)$$

> **Example 5.1 (Sierpiński Space is $T_0$ but not $T_1$):**
> On $X = \{0, 1\}$ with $\mathcal{T} = \{\emptyset, \{1\}, \{0, 1\}\}$, the open set $\{1\}$ contains $1$ but not $0$.
> Thus Sierpiński space is $T_0$.
> However, there is **no open set** containing $0$ without $1$ (the only open set containing $0$ is the whole space $X$).
> Hence Sierpiński space fails $T_1$!

---

### 3. Fréchet Spaces ($T_1$)

> **Definition 5.2 ($T_1$ / Fréchet Axiom):**
> A topological space $(X, \mathcal{T})$ is called a **$T_1$ space** (or **Fréchet space**) if for every pair of distinct points $x \ne y \in X$, there exist open sets $U, V \in \mathcal{T}$ such that:
> $$x \in U, \; y \notin U \qquad \text{and} \qquad y \in V, \; x \notin V$$

> **Theorem 5.1 (Characterization of $T_1$ via Singletons):**
> A topological space $(X, \mathcal{T})$ is $T_1$ if and only if **every singleton set $\{x\}$ is closed in $X$**.

> **Proof:**
> **($\Rightarrow$) Assume $X$ is $T_1$:**
> Let $x \in X$. To show $\{x\}$ is closed, we prove $X \setminus \{x\}$ is open.
> For any $y \in X \setminus \{x\}$, $y \ne x$.
> Since $X$ is $T_1$, there exists an open set $V_y$ containing $y$ such that $x \notin V_y$.
> This means $V_y \subseteq X \setminus \{x\}$.
> Then $X \setminus \{x\} = \bigcup_{y \ne x} V_y$, which is a union of open sets, hence open.
> Thus $\{x\}$ is closed.
>
> **($\Leftarrow$) Assume all singletons are closed:**
> Let $x \ne y \in X$. Since $\{y\}$ is closed, $U = X \setminus \{y\}$ is open.
> $x \in U$ and $y \notin U$.
> Similarly, $\{x\}$ is closed, so $V = X \setminus \{x\}$ is open, with $y \in V$ and $x \notin V$.
> Thus $X$ is $T_1$. $\blacksquare$

> **Corollary 5.1:**
> In any $T_1$ space, every finite subset is closed."""
            },
            {
                "secNumber": "5.2",
                "title": "Hausdorff Spaces ($T_2$) & The Closed Diagonal Theorem",
                "content": r"""### 1. Hausdorff Spaces ($T_2$)

Introduced by Felix Hausdorff in his seminal 1914 *Grundzüge der Mengenlehre*, the $T_2$ axiom is the cornerstone of modern topology and analysis.

> **Definition 5.3 ($T_2$ / Hausdorff Space):**
> A topological space $(X, \mathcal{T})$ is called a **Hausdorff space** (or **$T_2$ space**) if for every pair of distinct points $x \ne y \in X$, there exist **disjoint open neighborhoods** $U, V \in \mathcal{T}$ such that:
> $$x \in U, \quad y \in V, \qquad \text{and} \qquad U \cap V = \emptyset$$

---

### 2. Uniqueness of Sequence Limits

> **Theorem 5.2 (Limits are Unique in Hausdorff Spaces):**
> Let $(X, \mathcal{T})$ be a Hausdorff space.
> If a sequence $(x_n)_{n=1}^\infty$ converges to $x$ and also converges to $y$, then:
> $$x = y$$

> **Proof:**
> Suppose for contradiction that $x \ne y$.
> Since $X$ is Hausdorff, there exist disjoint open sets $U, V$ with $x \in U$, $y \in V$, and $U \cap V = \emptyset$.
> Since $x_n \to x$, there exists $N_1$ such that $x_n \in U$ for all $n \ge N_1$.
> Since $x_n \to y$, there exists $N_2$ such that $x_n \in V$ for all $n \ge N_2$.
> For any $n \ge \max\{N_1, N_2\}$, $x_n \in U \cap V$.
> This contradicts $U \cap V = \emptyset$!
> Therefore, $x = y$. $\blacksquare$

---

### 3. The Closed Diagonal Characterization

A profound global geometric characterization of the Hausdorff property:

> **Theorem 5.3 (Closed Diagonal Theorem):**
> A topological space $X$ is **Hausdorff** if and only if the diagonal:
> $$\Delta = \{(x, x) : x \in X\} \subseteq X \times X$$
> is a **closed subset** of the product space $X \times X$ equipped with the product topology.

> **Proof:**
> **($\Rightarrow$) Assume $X$ is Hausdorff:**
> We show $(X \times X) \setminus \Delta$ is open.
> Let $(x, y) \in (X \times X) \setminus \Delta$. Then $x \ne y$.
> Since $X$ is Hausdorff, there exist open sets $U, V \subseteq X$ with $x \in U, y \in V$, and $U \cap V = \emptyset$.
> The product $U \times V$ is open in $X \times X$ and contains $(x, y)$.
> If $(z, z) \in (U \times V) \cap \Delta$, then $z \in U \cap V = \emptyset$, contradiction!
> Thus $(U \times V) \cap \Delta = \emptyset$, meaning $U \times V \subseteq (X \times X) \setminus \Delta$.
> Thus $(X \times X) \setminus \Delta$ is open, so $\Delta$ is closed.
>
> **($\Leftarrow$) Assume $\Delta$ is closed:**
> If $x \ne y$, then $(x, y) \notin \Delta$.
> Since $(X \times X) \setminus \Delta$ is open, there exists a basic open set $U \times V$ in $X \times X$ such that:
> $$(x, y) \in U \times V \subseteq (X \times X) \setminus \Delta$$
> Then $x \in U$ and $y \in V$.
> If $z \in U \cap V$, then $(z, z) \in U \times V \subseteq (X \times X) \setminus \Delta$, which contradicts $(z, z) \in \Delta$!
> Thus $U \cap V = \emptyset$. Hence $X$ is Hausdorff. $\blacksquare$"""
            },
            {
                "secNumber": "5.3",
                "title": "Regular Spaces & $T_3$ Topological Spaces",
                "content": r"""### 1. Regular Spaces

Moving up the hierarchy, the $T_3$ axiom separates points from closed sets.

> **Definition 5.4 (Regular Space & $T_3$ Space):**
> 1. A topological space $X$ is called **regular** if for every closed set $F \subseteq X$ and every point $x \notin F$, there exist disjoint open sets $U, V \subseteq X$ such that:
>    $$x \in U, \quad F \subseteq V, \qquad \text{and} \qquad U \cap V = \emptyset$$
> 2. A space is called a **$T_3$ space** if it is both **regular** and **$T_1$**.

> **Remark on Terminology:**
> Some authors define $T_3$ to include $T_1$; under our standard modern convention, a regular space that is also $T_1$ is called $T_3$.
> Since singletons $\{y\}$ are closed in a $T_1$ space, separating $x$ from $\{y\}$ immediately gives disjoint neighborhoods, so:
> $$T_3 \implies T_2 \implies T_1 \implies T_0$$

---

### 2. Characterization via Closed Neighborhood Bases

> **Theorem 5.4 (Closed Neighborhood Base Characterization):**
> A $T_1$ space $X$ is **$T_3$ (regular)** if and only if for every point $x \in X$ and every open neighborhood $U$ of $x$, there exists an open neighborhood $V$ of $x$ such that:
> $$x \in V \subseteq \operatorname{cl}(V) \subseteq U$$
> In other words, every point has a neighborhood base consisting of **closed sets**.

> **Proof:**
> **($\Rightarrow$)** Let $x \in U$ with $U$ open. The set $F = X \setminus U$ is closed, and $x \notin F$.
> By regularity, there exist disjoint open sets $V$ and $W$ such that $x \in V$ and $F \subseteq W$.
> Since $V \cap W = \emptyset$, we have $V \subseteq X \setminus W$.
> Since $X \setminus W$ is closed, $\operatorname{cl}(V) \subseteq X \setminus W$.
> Since $F \subseteq W$, we have $X \setminus W \subseteq X \setminus F = U$.
> Thus $x \in V \subseteq \operatorname{cl}(V) \subseteq U$.
>
> **($\Leftarrow$)** Let $F$ be closed and $x \notin F$. Then $U = X \setminus F$ is an open neighborhood of $x$.
> By hypothesis, choose open $V$ with $x \in V \subseteq \operatorname{cl}(V) \subseteq U$.
> Let $W = X \setminus \operatorname{cl}(V)$.
> Then $W$ is open, $F = X \setminus U \subseteq X \setminus \operatorname{cl}(V) = W$, and $V \cap W = \emptyset$.
> Thus $x$ and $F$ are separated by disjoint open sets, so $X$ is regular. $\blacksquare$"""
            },
            {
                "secNumber": "5.4",
                "title": "Heredity & Product Invariance of $T_0, T_1, T_2, T_3$",
                "content": r"""### 1. Hereditary Properties

How do the axioms $T_0, T_1, T_2, T_3$ behave when taking subspaces?

> **Theorem 5.5 (Heredity of Lower Separation Axioms):**
> Each of the separation properties $T_0, T_1, T_2$, and $T_3$ is **hereditary**:
> If $X$ satisfies $T_i$ ($i \in \{0, 1, 2, 3\}$), then **every subspace** $Y \subseteq X$ with the relative topology satisfies $T_i$.

> **Proof for $T_2$:**
> Let $x \ne y \in Y$. Since $Y \subseteq X$, $x, y \in X$.
> Since $X$ is $T_2$, there exist disjoint open sets $U, V \subseteq X$ with $x \in U, y \in V$, and $U \cap V = \emptyset$.
> In the subspace topology on $Y$, $U_Y = U \cap Y$ and $V_Y = V \cap Y$ are open in $Y$.
> Moreover:
> $$x \in U_Y, \quad y \in V_Y, \qquad \text{and} \qquad U_Y \cap V_Y = (U \cap V) \cap Y = \emptyset \cap Y = \emptyset$$
> Thus $Y$ is Hausdorff. $\blacksquare$

---

### 2. Product Invariance

> **Theorem 5.6 (Product Invariance):**
> Let $\{X_\alpha\}_{\alpha \in I}$ be an arbitrary non-empty family of topological spaces.
> The product space $X = \prod_{\alpha \in I} X_\alpha$ equipped with the product topology satisfies $T_i$ ($i \in \{0, 1, 2, 3\}$) if and only if **every coordinate space $X_\alpha$ satisfies $T_i$**.

> **Proof for $T_2$:**
> **($\Leftarrow$)** Let $x = (x_\alpha)$ and $y = (y_\alpha)$ be distinct points in $\prod X_\alpha$.
> Then there exists some coordinate $\beta \in I$ such that $x_\beta \ne y_\beta \in X_\beta$.
> Since $X_\beta$ is Hausdorff, there exist disjoint open sets $U_\beta, V_\beta \subseteq X_\beta$ separating $x_\beta$ and $y_\beta$.
> Consider the cylinders $U = \pi_\beta^{-1}(U_\beta)$ and $V = \pi_\beta^{-1}(V_\beta)$.
> Both $U$ and $V$ are open in the product topology, $x \in U$, $y \in V$, and:
> $$U \cap V = \pi_\beta^{-1}(U_\beta \cap V_\beta) = \pi_\beta^{-1}(\emptyset) = \emptyset$$
> Thus $\prod X_\alpha$ is Hausdorff. $\blacksquare$"""
            },
            {
                "secNumber": "5.5",
                "title": "Classical Separation Counterexamples: The Line with Two Origins",
                "content": r"""### 1. The Line with Two Origins

A celebrated counterexample that shows local Euclidean structure does not guarantee the Hausdorff property!

> **Definition 5.5 (Line with Two Origins):**
> Let $X = (\mathbb{R} \setminus \{0\}) \cup \{0_A, 0_B\}$ where $0_A \ne 0_B$ are two distinct points.
> Topologize $X$ by declaring:
> - Any open interval in $\mathbb{R}$ not containing $0$ is open in $X$.
> - Basic neighborhoods of $0_A$ are of the form $(-\varepsilon, 0) \cup \{0_A\} \cup (0, \varepsilon)$ for $\varepsilon > 0$.
> - Basic neighborhoods of $0_B$ are of the form $(-\varepsilon, 0) \cup \{0_B\} \cup (0, \varepsilon)$ for $\varepsilon > 0$.

> **Theorem 5.7 (Properties of the Line with Two Origins):**
> 1. $X$ is **locally Euclidean** (every point has a neighborhood homeomorphic to an open interval in $\mathbb{R}$).
> 2. $X$ is **$T_1$** (singletons are closed).
> 3. $X$ is **NOT Hausdorff ($T_2$)!**

> **Proof that $X$ fails $T_2$:**
> Consider the two origins $0_A \ne 0_B$.
> Let $U$ be any open neighborhood of $0_A$, and $V$ any open neighborhood of $0_B$.
> By definition, $U$ contains $(-\varepsilon_1, 0) \cup (0, \varepsilon_1)$ and $V$ contains $(-\varepsilon_2, 0) \cup (0, \varepsilon_2)$ for some $\varepsilon_1, \varepsilon_2 > 0$.
> Let $\delta = \min\{\varepsilon_1, \varepsilon_2\} > 0$.
> Then $(0, \delta) \subseteq U \cap V$.
> Thus $U \cap V \ne \emptyset$!
> The two origins $0_A$ and $0_B$ can **never be separated by disjoint open sets**.
> Hence $X$ is not Hausdorff.
> Consequently, the sequence $x_n = 1/n$ converges **simultaneously to both $0_A$ and $0_B$**! $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "prob_5_1",
                "tier": "Foundational",
                "title": "The Diagonal Characterization of Hausdorff Spaces",
                "statement": r"""Let $(X, \mathcal{T})$ be a topological space.
Prove that $X$ is a Hausdorff ($T_2$) space if and only if the diagonal:
$$\Delta = \{(x, x) \in X \times X : x \in X\}$$
is a closed subset of the Cartesian product space $X \times X$ equipped with the product topology.""",
                "solution": r"""### 1. Necessity ($\Rightarrow$): Hausdorff $\implies$ Diagonal is Closed

Assume $X$ is Hausdorff.
To prove $\Delta$ is closed in $X \times X$, we show its complement:
$$U = (X \times X) \setminus \Delta = \{(x, y) \in X \times X : x \ne y\}$$
is open in the product topology.

Let $(x, y) \in U$. Then $x \ne y$.
Since $X$ is Hausdorff, there exist disjoint open sets $V, W \in \mathcal{T}$ such that:
$$x \in V, \quad y \in W, \qquad \text{and} \qquad V \cap W = \emptyset$$
By definition of the product topology, the Cartesian product $V \times W$ is a basic open set in $X \times X$.
Clearly $(x, y) \in V \times W$.

Now we check that $V \times W \subseteq U$:
Suppose for contradiction that $(V \times W) \cap \Delta \ne \emptyset$.
Then there exists some point $(z, z) \in V \times W$.
This implies $z \in V$ and $z \in W$, which means $z \in V \cap W$.
However, $V \cap W = \emptyset$, contradiction!
Therefore, $(V \times W) \cap \Delta = \emptyset$, which means:
$$(x, y) \in V \times W \subseteq (X \times X) \setminus \Delta$$
Since every point in $(X \times X) \setminus \Delta$ has an open neighborhood contained in $(X \times X) \setminus \Delta$, the complement is open.
Thus $\Delta$ is closed in $X \times X$.

---

### 2. Sufficiency ($\Leftarrow$): Diagonal Closed $\implies$ Hausdorff

Assume $\Delta$ is closed in $X \times X$.
Then $(X \times X) \setminus \Delta$ is open.
Let $x \ne y$ be any two distinct points in $X$.
Then $(x, y) \in (X \times X) \setminus \Delta$.
Since $(X \times X) \setminus \Delta$ is open, there exists a basic open set in the product topology containing $(x, y)$ and contained in $(X \times X) \setminus \Delta$.
Basic open sets in $X \times X$ are of the form $V \times W$ where $V, W \in \mathcal{T}$.
Thus:
$$(x, y) \in V \times W \subseteq (X \times X) \setminus \Delta$$
This implies:
1. $x \in V$ and $y \in W$.
2. For all $a \in V$ and $b \in W$, $(a, b) \notin \Delta \implies a \ne b$.
If there existed any point $z \in V \cap W$, then $(z, z) \in V \times W$, which contradicts $V \times W \subseteq (X \times X) \setminus \Delta$.
Therefore:
$$V \cap W = \emptyset$$
We have found disjoint open neighborhoods $V$ of $x$ and $W$ of $y$.
Thus $X$ is Hausdorff ($T_2$). $\blacksquare$"""
            },
            {
                "id": "prob_5_2",
                "tier": "Advanced",
                "title": "Failure of Sequence Limit Uniqueness on the Line with Two Origins",
                "statement": r"""Consider the Line with Two Origins $X = (\mathbb{R} \setminus \{0\}) \cup \{p, q\}$ where $p \ne q$:
1. Prove that $X$ is a $T_1$ space by showing that every singleton $\{x\} \subset X$ is closed.
2. Consider the sequence $x_n = 1/n$ for $n \in \mathbb{N}$. Prove that $x_n \to p$ and $x_n \to q$ simultaneously.
3. Why does this not contradict Theorem 1.2 on uniqueness of limits in metric spaces?""",
                "solution": r"""### 1. Proof that $X$ is $T_1$

We show that every singleton $\{x\}$ is closed by showing $X \setminus \{x\}$ is open:
- If $x \in \mathbb{R} \setminus \{0\}$, then $X \setminus \{x\} = (\mathbb{R} \setminus \{0, x\}) \cup \{p, q\}$.
  For any $y \ne x$: if $y \notin \{p, q\}$, choose $\varepsilon < |y - x|$; if $y = p$ or $q$, choose $\varepsilon < |x|$.
  In all cases, an open neighborhood avoiding $x$ exists.
- If $x = p$, consider $X \setminus \{p\} = (\mathbb{R} \setminus \{0\}) \cup \{q\}$.
  Any $y \in \mathbb{R} \setminus \{0\}$ has an open interval avoiding $p$.
  The point $q$ has open neighborhood $(-\varepsilon, 0) \cup \{q\} \cup (0, \varepsilon)$, which does not contain $p$!
  Thus $X \setminus \{p\}$ is open, so $\{p\}$ is closed.
- Identically, $\{q\}$ is closed.
Since all singletons are closed, by Theorem 5.1, $X$ is a **$T_1$ space**.

---

### 2. Simultaneous Convergence of $x_n = 1/n$ to Both $p$ and $q$

- **Convergence to $p$:**
  Let $U$ be any open neighborhood of $p$.
  By definition of the topology on $X$, there exists $\varepsilon > 0$ such that:
  $$N_\varepsilon(p) = (-\varepsilon, 0) \cup \{p\} \cup (0, \varepsilon) \subseteq U$$
  By the Archimedean property, choose $N \in \mathbb{N}$ such that $1/N < \varepsilon$.
  Then for all $n \ge N$:
  $$0 < x_n = \frac{1}{n} \le \frac{1}{N} < \varepsilon \implies x_n \in (0, \varepsilon) \subseteq N_\varepsilon(p) \subseteq U$$
  Thus $x_n \to p$.

- **Convergence to $q$:**
  Let $V$ be any open neighborhood of $q$.
  There exists $\delta > 0$ such that $N_\delta(q) = (-\delta, 0) \cup \{q\} \cup (0, \delta) \subseteq V$.
  Choosing $M \in \mathbb{N}$ with $1/M < \delta$, for all $n \ge M$:
  $$x_n = \frac{1}{n} < \delta \implies x_n \in (0, \delta) \subseteq N_\delta(q) \subseteq V$$
  Thus $x_n \to q$.

Therefore, the sequence $(x_n)_{n=1}^\infty$ converges **simultaneously to both distinct points $p \ne q$**!

---

### 3. Resolution of Metric Space Limit Uniqueness

Theorem 1.2 on uniqueness of limits requires the space to be **metrizable** (or more generally, Hausdorff).
As shown in Section 5.5, the Line with Two Origins is **NOT Hausdorff** ($T_2$), because any neighborhood of $p$ intersects every neighborhood of $q$ in an interval $(0, \min\{\varepsilon, \delta\})$.
Because $X$ is not Hausdorff, $X$ is **not metrizable**!
Thus, there is no contradiction with metric space theory; sequence limits are only guaranteed to be unique in spaces satisfying at least the Hausdorff ($T_2$) separation axiom."""
            },
            {
                "id": "prob_5_3",
                "tier": "Honors / Proof Challenge",
                "title": "Every Metric Space is Regular ($T_3$)",
                "statement": r"""Prove with full mathematical rigor that:
1. Every metric space $(X, d)$ is a **regular space**.
2. Combined with the fact that metric spaces are $T_1$, conclude that every metric space is a **$T_3$ space**.
3. Prove that in any metric space, every closed set $F$ can be expressed as a countable intersection of open sets ($F$ is a $G_\delta$ set).""",
                "solution": r"""### 1. Proof of Regularity

Let $(X, d)$ be a metric space.
Let $F \subseteq X$ be a closed set and let $x \in X$ be a point with $x \notin F$.
Since $F$ is closed, its complement $X \setminus F$ is open.
Since $x \in X \setminus F$, by Definition 1.3 of an open set in a metric space, there exists a radius $r > 0$ such that:
$$B(x, r) \subseteq X \setminus F \implies B(x, r) \cap F = \emptyset$$
Define the two sets:
$$U = B\left(x, \frac{r}{2}\right)$$
$$V = \bigcup_{y \in F} B\left(y, \frac{r}{2}\right)$$

Notice that:
- $U$ is an open ball, hence open, and $x \in U$.
- $V$ is a union of open balls, hence open, and clearly $F \subseteq V$ (since every $y \in F$ is the center of $B(y, r/2)$).

Now we prove that $U \cap V = \emptyset$:
Suppose for contradiction that there exists $z \in U \cap V$.
- Since $z \in U$, $d(x, z) < r/2$.
- Since $z \in V$, $z \in B(y_0, r/2)$ for some $y_0 \in F$, so $d(y_0, z) < r/2$.
By the triangle inequality:
$$d(x, y_0) \le d(x, z) + d(z, y_0) < \frac{r}{2} + \frac{r}{2} = r$$
This implies that $y_0 \in B(x, r)$.
However, $y_0 \in F$, so $y_0 \in B(x, r) \cap F$.
This directly contradicts $B(x, r) \cap F = \emptyset$!
Therefore, $U \cap V = \emptyset$.
We have separated the point $x$ and the closed set $F$ by disjoint open sets $U$ and $V$.
Thus, $(X, d)$ is **regular**.

---

### 2. Metric Spaces are $T_3$

For any two distinct points $x \ne y$ in $X$, $d(x, y) = \varepsilon > 0$.
The ball $B(x, \varepsilon)$ contains $x$ but not $y$, so singletons are closed, proving $X$ is $T_1$.
Since $(X, d)$ is regular and $T_1$, it is a **$T_3$ space**.

---

### 3. Closed Sets are $G_\delta$ Sets

For any non-empty closed set $F \subseteq X$, define for each $n \in \mathbb{N}$:
$$U_n = \bigcup_{y \in F} B\left(y, \frac{1}{n}\right) = \{x \in X : d(x, F) < 1/n\}$$
Each $U_n$ is a union of open balls, hence open.
Clearly $F \subseteq U_n$ for all $n$, so $F \subseteq \bigcap_{n=1}^\infty U_n$.
Conversely, if $x \in \bigcap_{n=1}^\infty U_n$, then $d(x, F) < 1/n$ for all $n \in \mathbb{N}$, which forces $d(x, F) = 0$.
Since $F$ is closed, $d(x, F) = 0 \iff x \in \operatorname{cl}(F) = F$.
Therefore:
$$F = \bigcap_{n=1}^\infty U_n$$
Every closed set in a metric space is a countable intersection of open sets (a $G_\delta$ set). $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u5 = get_unit5()
    print(f"Loaded Unit 5: {u5['title']} with {len(u5['sections'])} sections and {len(u5['problems'])} problems.")
