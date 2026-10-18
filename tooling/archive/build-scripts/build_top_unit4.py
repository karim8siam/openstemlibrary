# -*- coding: utf-8 -*-
"""
build_top_unit4.py
Constructs Unit 4: Countability Axioms: First, Second Countable & Separable Spaces
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Countability Axioms: First, Second Countable & Separable Spaces",
        "leadSummary": "Topological countability conditions: first-countable spaces and neighborhood bases, second-countable spaces and global countable bases, Lindelöf spaces and Lindelöf's Covering Theorem, separable spaces and countable dense subsets, the countability implication hierarchy ($C_2 \\implies C_1$, $C_2 \\implies S$, $C_2 \\implies L$), equivalence in metric spaces, the Sorgenfrey line $\\mathbb{R}_\\ell$, and the Sorgenfrey plane product pathology failing the Lindelöf property.",
        "simulations": ["sim_top_countability_hierarchy"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "First-Countable Spaces & Neighborhood Bases",
                "content": r"""### 1. Local Countability: The First Countability Axiom

The first countability axiom ensures that local properties around any point can be controlled by a countable sequence of neighborhoods, making sequential arguments sufficient for topology.

> **Definition 4.1 (Local Basis / Neighborhood Base):**
> Let $(X, \mathcal{T})$ be a topological space and $x \in X$.
> A collection of open neighborhoods $\mathcal{B}(x)$ of $x$ is called a **local basis** (or **neighborhood base**) at $x$ if for every open neighborhood $U$ of $x$, there exists $B \in \mathcal{B}(x)$ such that:
> $$x \in B \subseteq U$$

> **Definition 4.2 (First-Countable Space - $C_1$):**
> A topological space $(X, \mathcal{T})$ is called **first-countable** (or satisfies the **first axiom of countability**) if every point $x \in X$ has a **countable local basis**.

---

### 2. Metric Spaces are First-Countable

> **Theorem 4.1 (First-Countability of Metric Spaces):**
> Every metric space $(X, d)$ is first-countable.

> **Proof:**
> For any point $x \in X$, consider the countable family of open balls with rational radii:
> $$\mathcal{B}(x) = \left\{ B\left(x, \frac{1}{n}\right) : n \in \mathbb{N} \right\}$$
> For any open neighborhood $U$ of $x$, by Definition 1.3 there exists $r > 0$ such that $B(x, r) \subseteq U$.
> By the Archimedean property, choose $n \in \mathbb{N}$ such that $1/n < r$.
> Then:
> $$x \in B\left(x, \frac{1}{n}\right) \subseteq B(x, r) \subseteq U$$
> Since $\mathcal{B}(x)$ is indexed by $\mathbb{N}$, it is countable.
> Thus every point has a countable local basis, so $(X, d)$ is first-countable. $\blacksquare$

---

### 3. Sequences in First-Countable Spaces

In general topological spaces, sequences are insufficient to detect closure or continuity (one requires nets or filters). However, in first-countable spaces, sequences suffice!

> **Theorem 4.2 (Sequential Characterization of Closure):**
> Let $(X, \mathcal{T})$ be a first-countable space and $A \subseteq X$.
> A point $x \in \operatorname{cl}(A)$ if and only if there exists a sequence $(a_n)_{n=1}^\infty \subseteq A$ such that $a_n \to x$."""
            },
            {
                "secNumber": "4.2",
                "title": "Second-Countable Spaces & Lindelöf's Theorem",
                "content": r"""### 1. Global Countability: The Second Countability Axiom

While first-countability is a local condition, second-countability is a powerful global finiteness condition.

> **Definition 4.3 (Second-Countable Space - $C_2$):**
> A topological space $(X, \mathcal{T})$ is called **second-countable** (or satisfies the **second axiom of countability**) if its topology $\mathcal{T}$ admits a **countable basis**.
> That is, there exists a countable collection $\mathcal{B} = \{B_n\}_{n=1}^\infty \subseteq \mathcal{T}$ such that every open set $U \in \mathcal{T}$ is a union of members of $\mathcal{B}$.

> **Example 4.1 (Euclidean Space $\mathbb{R}^n$ is Second-Countable):**
> In $\mathbb{R}^n$, consider the collection of open balls with rational centers and rational radii:
> $$\mathcal{B} = \{B(q, r) : q \in \mathbb{Q}^n, \; r \in \mathbb{Q}_{> 0}\}$$
> Since $\mathbb{Q}^n$ and $\mathbb{Q}$ are countable, the Cartesian product $\mathbb{Q}^n \times \mathbb{Q}_{> 0}$ is countable.
> By denseness of $\mathbb{Q}$ in $\mathbb{R}$, every open ball in $\mathbb{R}^n$ is a union of balls in $\mathcal{B}$.
> Hence $\mathcal{B}$ is a countable basis, proving $\mathbb{R}^n$ is second-countable.

---

### 2. Lindelöf's Covering Theorem

> **Definition 4.4 (Lindelöf Space):**
> A topological space $X$ is called a **Lindelöf space** if every open covering of $X$ contains a **countable subcovering**.

> **Theorem 4.3 (Lindelöf's Theorem):**
> Every second-countable space is **Lindelöf**.

> **Proof:**
> Let $X$ be second-countable with countable basis $\mathcal{B} = \{B_n\}_{n=1}^\infty$.
> Let $\mathcal{U} = \{U_\alpha\}_{\alpha \in I}$ be any arbitrary open cover of $X$: $\bigcup_{\alpha \in I} U_\alpha = X$.
>
> For each point $x \in X$, there exists some $\alpha(x) \in I$ such that $x \in U_{\alpha(x)}$.
> Since $\mathcal{B}$ is a basis, there exists a basis element $B_{n(x)} \in \mathcal{B}$ such that:
> $$x \in B_{n(x)} \subseteq U_{\alpha(x)}$$
> Consider the subcollection of basis elements:
> $$\mathcal{B}^* = \{B_n \in \mathcal{B} : \exists \alpha \in I \text{ with } B_n \subseteq U_\alpha\}$$
> Since $\mathcal{B}^* \subseteq \mathcal{B}$ and $\mathcal{B}$ is countable, $\mathcal{B}^*$ is countable:
> $$\mathcal{B}^* = \{B_{n_k}\}_{k=1}^\infty$$
> For each $B_{n_k} \in \mathcal{B}^*$, choose **one** set $U_{\alpha_k} \in \mathcal{U}$ containing $B_{n_k}$.
>
> We claim that $\{U_{\alpha_k}\}_{k=1}^\infty$ covers $X$:
> For any $x \in X$, $x \in B_{n(x)} \subseteq U_{\alpha(x)}$.
> Since $B_{n(x)} \in \mathcal{B}^*$, $B_{n(x)} = B_{n_k}$ for some $k$.
> Then $x \in B_{n_k} \subseteq U_{\alpha_k}$.
> Thus $X = \bigcup_{k=1}^\infty U_{\alpha_k}$.
> We have extracted a countable subcover from the arbitrary open cover $\mathcal{U}$!
> Therefore, $X$ is a Lindelöf space. $\blacksquare$"""
            },
            {
                "secNumber": "4.3",
                "title": "Separability & Countable Dense Subsets",
                "content": r"""### 1. Separable Spaces

> **Definition 4.5 (Separable Space):**
> A topological space $(X, \mathcal{T})$ is called **separable** if it contains a **countable dense subset**.
> That is, there exists a countable set $D \subseteq X$ such that:
> $$\operatorname{cl}(D) = X$$
> Equivalently, $D$ intersects every non-empty open set in $X$.

> **Example 4.2 ($\mathbb{R}^n$ is Separable):**
> $\mathbb{Q}^n$ is countable and dense in $\mathbb{R}^n$, so $\mathbb{R}^n$ is separable.

> **Example 4.3 (Non-separable Sequence Space $\ell^\infty$):**
> Consider the space $\ell^\infty$ of bounded real sequences with norm $\|x\|_\infty = \sup_n |x_n|$.
> For each subset $S \subseteq \mathbb{N}$, define the characteristic sequence $\mathbf{1}_S = (s_n)_{n=1}^\infty$ where $s_n = 1$ if $n \in S$ and $0$ otherwise.
> For any two distinct subsets $S \ne T \subseteq \mathbb{N}$:
> $$\|\mathbf{1}_S - \mathbf{1}_T\|_\infty = 1$$
> Thus, the open balls $B(\mathbf{1}_S, 1/2)$ for all $S \in \mathcal{P}(\mathbb{N})$ are **mutually disjoint**!
> The power set $\mathcal{P}(\mathbb{N})$ has cardinality $2^{\aleph_0} = \mathfrak{c}$ (uncountable).
> If $D$ were any dense subset of $\ell^\infty$, each of these uncountably many disjoint open balls would have to contain at least one point of $D$.
> This forces $D$ to be uncountable!
> Therefore, $\ell^\infty$ **cannot be separable**."""
            },
            {
                "secNumber": "4.4",
                "title": "Hierarchy & Equivalence in Metric Spaces",
                "content": r"""### 1. The Countability Implication Hierarchy

For general topological spaces, the relationships among countability axioms are strictly directional:

$$\begin{array}{ccc}
\text{Second-Countable } (C_2) & \implies & \text{First-Countable } (C_1) \\
\Downarrow & & \\
\text{Separable } (S) & & \\
\Downarrow & & \\
\text{Lindelöf } (L) & &
\end{array}$$

> **Theorem 4.4 (Second-Countable Implies Separable):**
> If $(X, \mathcal{T})$ is second-countable, then $X$ is separable.

> **Proof:**
> Let $\mathcal{B} = \{B_n\}_{n=1}^\infty$ be a countable basis for $X$.
> For each non-empty $B_n \in \mathcal{B}$, choose one point $d_n \in B_n$.
> Let $D = \{d_n : B_n \ne \emptyset\}$.
> $D$ is a countable subset of $X$.
> For any non-empty open set $U \subseteq X$, since $\mathcal{B}$ is a basis, there exists non-empty $B_k \in \mathcal{B}$ with $B_k \subseteq U$.
> Then $d_k \in B_k \subseteq U$, so $d_k \in D \cap U$.
> Thus $D$ intersects every non-empty open set, proving $\operatorname{cl}(D) = X$.
> Hence $X$ is separable. $\blacksquare$

---

### 2. Complete Equivalence in Metric Spaces

In metric spaces, the distinction between global countability properties collapses!

> **Theorem 4.5 (Metric Countability Equivalence):**
> For any metric space $(X, d)$, the following three properties are **logically equivalent**:
> 1. $(X, d)$ is **Second-Countable** ($C_2$).
> 2. $(X, d)$ is **Separable** ($S$).
> 3. $(X, d)$ is **Lindelöf** ($L$).

> **Proof ($S \implies C_2$):**
> Let $D = \{d_n\}_{n=1}^\infty$ be a countable dense subset of $(X, d)$.
> Consider the countable family of open balls:
> $$\mathcal{B} = \left\{ B\left(d_n, \frac{1}{m}\right) : n, m \in \mathbb{N} \right\}$$
> We claim $\mathcal{B}$ is a basis for $(X, d)$.
> Let $U$ be open and $x \in U$. There exists $\varepsilon > 0$ such that $B(x, \varepsilon) \subseteq U$.
> Choose $m \in \mathbb{N}$ such that $1/m < \varepsilon / 2$.
> Since $D$ is dense, there exists $d_n \in D$ such that $d(x, d_n) < 1/m$.
> Then:
> 1. $x \in B(d_n, 1/m)$.
> 2. For any $y \in B(d_n, 1/m)$: $d(y, x) \le d(y, d_n) + d(d_n, x) < 1/m + 1/m = 2/m < \varepsilon$.
>    Thus $B(d_n, 1/m) \subseteq B(x, \varepsilon) \subseteq U$.
> Hence $\mathcal{B}$ is a countable basis, proving $X$ is second-countable. $\blacksquare$"""
            },
            {
                "secNumber": "4.5",
                "title": "The Sorgenfrey Line $\\mathbb{R}_\\ell$ & Sorgenfrey Plane Pathology",
                "content": r"""### 1. The Sorgenfrey Line (Lower Limit Topology)

Robert Sorgenfrey introduced in 1947 one of the most famous counterexamples in general topology.

> **Definition 4.6 (Sorgenfrey Line $\mathbb{R}_\ell$):**
> The **Sorgenfrey line** $\mathbb{R}_\ell$ is the real line $\mathbb{R}$ equipped with the topology generated by the basis of **half-open intervals**:
> $$\mathcal{B} = \{[a, b) : a < b, \; a, b \in \mathbb{R}\}$$
> The topology is strictly finer than the Euclidean topology: every open interval $(a, b) = \bigcup_{n=1}^\infty [a + 1/n, b)$ is open in $\mathbb{R}_\ell$.
> Moreover, each $[a, b)$ is **clopen** (both open and closed)!

> **Properties of $\mathbb{R}_\ell$:**
> 1. **First-Countable:** The countable family $\{[x, x + 1/n) : n \in \mathbb{N}\}$ forms a local basis at $x$.
> 2. **Separable:** The rational numbers $\mathbb{Q}$ are dense in $\mathbb{R}_\ell$ (every $[a, b)$ contains a rational).
> 3. **Lindelöf:** Every open cover of $\mathbb{R}_\ell$ has a countable subcover.
> 4. **NOT Second-Countable:** Any basis $\mathcal{B}$ for $\mathbb{R}_\ell$ must be uncountable! (Each point $x$ must be the unique left endpoint of some basis element).

---

### 2. The Sorgenfrey Plane $\mathbb{R}_\ell \times \mathbb{R}_\ell$

The product of two Lindelöf spaces is **NOT necessarily Lindelöf**!

> **Theorem 4.6 (Pathology of the Sorgenfrey Plane):**
> The Sorgenfrey plane $\mathbb{S} = \mathbb{R}_\ell \times \mathbb{R}_\ell$ is:
> 1. First-countable and Separable ($\mathbb{Q} \times \mathbb{Q}$ is dense).
> 2. **NOT Lindelöf!**
> 3. **NOT Normal ($T_4$)!**

> **Proof that $\mathbb{R}_\ell^2$ is not Lindelöf:**
> Consider the "anti-diagonal" line in $\mathbb{R}^2$:
> $$L = \{(x, -x) : x \in \mathbb{R}\}$$
> For each point $p = (x, -x) \in L$, consider the basic open rectangle in $\mathbb{S}$:
> $$U_x = [x, x+1) \times [-x, -x+1)$$
> Notice that for any other point $(y, -y) \in L$ with $y \ne x$:
> If $y > x$, then $-y < -x$, so $(y, -y) \notin U_x$ because its second coordinate is strictly less than $-x$.
> If $y < x$, then $y \notin [x, x+1)$.
> Thus:
> $$U_x \cap L = \{(x, -x)\} = \{p\}$$
> The relative topology on $L$ is **DISCRETE**!
> Since $L$ is an uncountable discrete closed subspace, the open cover $\mathcal{U} = \{U_x : x \in \mathbb{R}\} \cup \{\mathbb{S} \setminus L\}$ of $\mathbb{S}$ contains no countable subcover.
> Therefore, $\mathbb{S} = \mathbb{R}_\ell \times \mathbb{R}_\ell$ is **not Lindelöf**. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "prob_4_1",
                "tier": "Foundational",
                "title": "Countability Classification of Discrete Topological Spaces",
                "statement": r"""Let $X$ be an arbitrary non-empty set equipped with the discrete topology $\mathcal{T}_{\text{disc}} = \mathcal{P}(X)$.
Determine the exact conditions on the cardinality $|X|$ under which $(X, \mathcal{T}_{\text{disc}})$ is:
1. First-countable ($C_1$).
2. Second-countable ($C_2$).
3. Separable ($S$).
4. Lindelöf ($L$).""",
                "solution": r"""### 1. First-Countability ($C_1$)

In the discrete topology, for any point $x \in X$, the singleton $\{x\}$ is an open set.
The family $\mathcal{B}(x) = \{\{x\}\}$ consists of a single set, which is finite (hence countable).
For any open neighborhood $U$ of $x$, $x \in \{x\} \subseteq U$.
Thus, $\{\{x\}\}$ is a countable local basis for **every** point $x \in X$.
Therefore, $(X, \mathcal{T}_{\text{disc}})$ is **first-countable for ANY set $X$**, regardless of whether $X$ is finite, countably infinite, or uncountably infinite!

---

### 2. Second-Countability ($C_2$)

Let $\mathcal{B}$ be any basis for $\mathcal{T}_{\text{disc}}$.
For each $x \in X$, the singleton $\{x\}$ is open, so it must be a union of basis elements in $\mathcal{B}$.
This forces $\{x\} \in \mathcal{B}$ for every $x \in X$.
Thus:
$$\{\{x\} : x \in X\} \subseteq \mathcal{B} \implies |\mathcal{B}| \ge |X|$$
For $\mathcal{B}$ to be countable, $X$ must be countable.
Therefore, $(X, \mathcal{T}_{\text{disc}})$ is **second-countable if and only if $X$ is at most countable** ($|X| \le \aleph_0$).

---

### 3. Separability ($S$)

Let $D \subseteq X$ be a dense subset.
In the discrete topology, every singleton $\{x\}$ is open.
If $D$ is dense, $D$ must intersect every non-empty open set:
$$D \cap \{x\} \ne \emptyset \implies x \in D \qquad \forall x \in X$$
This forces $D = X$!
The only dense subset in a discrete space is the entire set $X$ itself.
For $D$ to be countable, $X$ must be countable.
Therefore, $(X, \mathcal{T}_{\text{disc}})$ is **separable if and only if $X$ is at most countable** ($|X| \le \aleph_0$).

---

### 4. Lindelöf Property ($L$)

Consider the open cover by singletons:
$$\mathcal{U} = \{\{x\} : x \in X\}$$
Since the sets in $\mathcal{U}$ are pairwise disjoint, no subcover can omit even a single point!
Any subcovering of $\mathcal{U}$ that covers $X$ must be $\mathcal{U}$ itself.
Thus $\mathcal{U}$ has a countable subcover if and only if $\mathcal{U}$ (and hence $X$) is countable.
Therefore, $(X, \mathcal{T}_{\text{disc}})$ is **Lindelöf if and only if $X$ is at most countable** ($|X| \le \aleph_0$)."""
            },
            {
                "id": "prob_4_2",
                "tier": "Advanced",
                "title": "Rigorous Proof that the Sorgenfrey Line Fails Second-Countability",
                "statement": r"""Prove rigorously that the Sorgenfrey line $\mathbb{R}_\ell$ (the real line with the lower limit topology generated by $\{[a, b) : a < b\}$) is:
1. Separable ($S$).
2. Lindelöf ($L$).
3. **NOT** second-countable ($C_2$).
Conclude that the converse of Theorem 4.4 ($S \implies C_2$) is false in general topological spaces.""",
                "solution": r"""### 1. Proof of Separability

We show that the set of rational numbers $\mathbb{Q}$ is dense in $\mathbb{R}_\ell$.
Let $U$ be any non-empty basic open set in $\mathbb{R}_\ell$, so $U = [a, b)$ with $a < b$.
By the density of rational numbers in $\mathbb{R}$ with respect to the standard order, there exists $q \in \mathbb{Q}$ such that:
$$a < q < b \implies q \in [a, b)$$
Thus $\mathbb{Q} \cap [a, b) \ne \emptyset$.
Since every open set in $\mathbb{R}_\ell$ contains a basic interval $[a, b)$, $\mathbb{Q}$ intersects every non-empty open set in $\mathbb{R}_\ell$.
Thus $\operatorname{cl}(\mathbb{Q}) = \mathbb{R}_\ell$.
Since $\mathbb{Q}$ is countable, $\mathbb{R}_\ell$ is **separable**.

---

### 2. Proof that $\mathbb{R}_\ell$ Fails Second-Countability

Suppose for contradiction that $\mathbb{R}_\ell$ admits a countable basis $\mathcal{B} = \{B_n\}_{n=1}^\infty$.
For each real number $x \in \mathbb{R}$, consider the open set $[x, x+1) \in \mathcal{T}_{\mathbb{R}_\ell}$.
Since $\mathcal{B}$ is a basis and $x \in [x, x+1)$, there exists some basis element $B(x) \in \mathcal{B}$ such that:
$$x \in B(x) \subseteq [x, x+1)$$
Since $B(x) \subseteq [x, x+1)$, we have $\inf B(x) \ge x$.
On the other hand, since $x \in B(x)$, we have $\inf B(x) \le x$.
Therefore:
$$\inf B(x) = x$$
Now, suppose $x \ne y$ are two distinct real numbers.
Then $\inf B(x) = x \ne y = \inf B(y)$, which implies:
$$B(x) \ne B(y)$$
Thus, the association $x \mapsto B(x)$ defines an **injective function** from the real numbers $\mathbb{R}$ into the basis $\mathcal{B}$:
$$\mathbb{R} \hookrightarrow \mathcal{B}$$
This implies that $|\mathcal{B}| \ge |\mathbb{R}| = \mathfrak{c} > \aleph_0$.
The basis $\mathcal{B}$ must be **uncountable**!
This contradicts the hypothesis that $\mathcal{B}$ was countable.
Therefore, $\mathbb{R}_\ell$ is **NOT second-countable**. $\blacksquare$

---

### 3. Conclusion

Since $\mathbb{R}_\ell$ is separable but not second-countable, this provides a definitive counterexample demonstrating that:
$$\text{Separable } (S) \; \not\implies \; \text{Second-Countable } (C_2)$$
in non-metrizable topological spaces."""
            },
            {
                "id": "prob_4_3",
                "tier": "Honors / Proof Challenge",
                "title": "Non-Preservation of Lindelöf Property in Products: The Sorgenfrey Plane",
                "statement": r"""Prove with full mathematical rigor that the Sorgenfrey plane $\mathbb{S} = \mathbb{R}_\ell \times \mathbb{R}_\ell$ fails the Lindelöf property:

1. Prove that the anti-diagonal line $L = \{(x, -x) : x \in \mathbb{R}\}$ is a **closed subset** of $\mathbb{S}$.
2. Prove that the subspace topology induced on $L$ is the **uncountable discrete topology**.
3. Using the open cover of $L$ by singleton-isolating open rectangles, construct an explicit open cover of $\mathbb{S}$ that admits **no countable subcover**.
4. Conclude that the product of two Lindelöf spaces is not necessarily Lindelöf.""",
                "solution": r"""### 1. Proof that $L$ is Closed in $\mathbb{S}$

We show that the complement $\mathbb{S} \setminus L$ is open.
Let $(x, y) \in \mathbb{S} \setminus L$. This means $x + y \ne 0$.
- **Case 1: $x + y > 0$.**
  Let $\varepsilon = (x + y) / 2 > 0$.
  Consider the basic open rectangle in $\mathbb{S}$:
  $$U = [x, x + \varepsilon) \times [y, y + \varepsilon)$$
  For any $(u, v) \in U$, we have $u \ge x$ and $v \ge y$, so $u + v \ge x + y > 0$.
  Thus no point in $U$ satisfies $u + v = 0$.
  Hence $U \cap L = \emptyset$, so $U \subseteq \mathbb{S} \setminus L$.
- **Case 2: $x + y < 0$.**
  Let $\delta = -(x + y) / 2 > 0$.
  The rectangle $V = [x, x + \delta) \times [y, y + \delta)$ satisfies for any $(u, v) \in V$:
  $u < x + \delta$ and $v < y + \delta$, so $u + v < x + y + 2\delta = 0$.
  Thus $V \cap L = \emptyset$, so $V \subseteq \mathbb{S} \setminus L$.

In both cases, every point in $\mathbb{S} \setminus L$ has an open neighborhood disjoint from $L$.
Therefore, $\mathbb{S} \setminus L$ is open in $\mathbb{S}$, so $L$ is **closed in $\mathbb{S}$**.

---

### 2. Subspace Topology on $L$ is Discrete

For each real number $x \in \mathbb{R}$, consider the basic open rectangle in $\mathbb{S}$:
$$U_x = [x, x + 1) \times [-x, -x + 1)$$
The point $p = (x, -x)$ belongs to $U_x$ because $x \in [x, x+1)$ and $-x \in [-x, -x+1)$.
Now consider any other point $q = (y, -y) \in L$ with $y \ne x$:
- If $y > x$, then $-y < -x$, so $-y \notin [-x, -x+1)$. Thus $q \notin U_x$.
- If $y < x$, then $y \notin [x, x+1)$. Thus $q \notin U_x$.
Therefore:
$$U_x \cap L = \{(x, -x)\}$$
The intersection of the open rectangle $U_x$ with $L$ is the singleton $\{(x, -x)\}$.
By Definition 2.9 of the subspace topology, every singleton in $L$ is open in the subspace topology!
Since every subset of $L$ is a union of singletons, the subspace topology on $L$ is the **discrete topology**.

---

### 3. Construction of an Uncountable Open Cover with No Countable Subcover

Consider the family of open sets in $\mathbb{S}$:
$$\mathcal{U} = \{U_x : x \in \mathbb{R}\} \cup \{\mathbb{S} \setminus L\}$$
- Each $U_x$ is open in $\mathbb{S}$.
- Since $L$ is closed, $\mathbb{S} \setminus L$ is open in $\mathbb{S}$.
- For every point $(x, y) \in \mathbb{S}$: if $(x, y) \in L$, then $(x, y) = (x, -x) \in U_x$; if $(x, y) \notin L$, then $(x, y) \in \mathbb{S} \setminus L$.
Thus $\mathcal{U}$ is an open cover of $\mathbb{S}$.

Now, suppose for contradiction that $\mathcal{U}$ admits a **countable subcover** $\mathcal{U}^* \subseteq \mathcal{U}$:
$$\mathcal{U}^* = \{U_{x_k}\}_{k=1}^\infty \cup \{\mathbb{S} \setminus L\}$$
(or without $\mathbb{S} \setminus L$).
Every point $p = (x, -x) \in L$ must be covered by some set in $\mathcal{U}^*$.
Since $p \notin \mathbb{S} \setminus L$, $p$ must belong to some $U_{x_k}$.
However, as proved in Part 2:
$$U_{x_k} \cap L = \{(x_k, -x_k)\}$$
Thus, each $U_{x_k}$ covers **at most one point** of $L$!
The countable subcollection can cover at most the countably many points:
$$L \cap \bigcup_{k=1}^\infty U_{x_k} = \bigcup_{k=1}^\infty \{(x_k, -x_k)\} = \{(x_1, -x_1), (x_2, -x_2), \dots\}$$
Since the real line $\mathbb{R}$ is uncountably infinite, $L$ contains uncountably many points.
Thus, uncountably many points of $L$ remain **completely uncovered**!
This contradiction proves that $\mathcal{U}$ has NO countable subcover.

---

### 4. Conclusion

$\mathbb{S} = \mathbb{R}_\ell \times \mathbb{R}_\ell$ is **not Lindelöf**.
Since both factor spaces $\mathbb{R}_\ell$ are Lindelöf, this proves that the Lindelöf property is **not preserved under Cartesian products**:
$$X \text{ and } Y \text{ Lindelöf} \;\not\implies\; X \times Y \text{ Lindelöf} \quad \blacksquare$$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u4 = get_unit4()
    print(f"Loaded Unit 4: {u4['title']} with {len(u4['sections'])} sections and {len(u4['problems'])} problems.")
