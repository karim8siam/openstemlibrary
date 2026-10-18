# -*- coding: utf-8 -*-
"""
build_top_unit6.py
Constructs Unit 6: Normal Spaces (T4), Urysohn's Lemma & Tietze Extension Theorem
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Normal Spaces (T4), Urysohn's Lemma & Tietze Extension Theorem",
        "leadSummary": "Higher separation axioms and functional analysis bridges: normal spaces ($T_4$), completely regular spaces ($T_{3.5}$, Tychonoff spaces), Pavel Urysohn's celebrated Lemma constructing continuous dyadic rational potentials, Heinrich Tietze's Extension Theorem extending continuous functions from closed subspaces, and the Urysohn Metrization Theorem embedding second-countable regular spaces into the Hilbert cube $[0, 1]^\\mathbb{N}$.",
        "simulations": ["sim_top_urysohn_dyadic_potential"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Normal Spaces & The $T_4$ Axiom",
                "content": r"""### 1. The Normal Space Axiom ($T_4$)

The highest classical separation axiom separates disjoint closed sets by disjoint open sets.

> **Definition 6.1 (Normal Space & $T_4$ Space):**
> 1. A topological space $(X, \mathcal{T})$ is called **normal** if for every pair of disjoint closed subsets $A, B \subseteq X$ ($A \cap B = \emptyset$), there exist **disjoint open sets** $U, V \subseteq X$ such that:
>    $$A \subseteq U, \quad B \subseteq V, \qquad \text{and} \qquad U \cap V = \emptyset$$
> 2. A space is called a **$T_4$ space** if it is both **normal** and **$T_1$**.

> **Remark on Heredity:**
> Unlike $T_0, T_1, T_2, T_3$, the normal property $T_4$ is **NOT hereditary**!
> A subspace of a normal space is not necessarily normal (e.g. the Sorgenfrey plane is not normal, but embeds as a subspace of a normal space).
> However, normality is **closed-hereditary**: every closed subspace of a normal space is normal!

---

### 2. Metric Spaces and Compact Hausdorff Spaces are Normal

> **Theorem 6.1:**
> 1. Every metric space $(X, d)$ is normal ($T_4$).
> 2. Every compact Hausdorff space is normal ($T_4$).

---

### 3. Characterization via Open Neighborhoods of Closed Sets

> **Theorem 6.2 (Normal Neighborhood Characterization):**
> A $T_1$ space $X$ is normal ($T_4$) if and only if for every closed set $A \subseteq X$ and every open set $W \supseteq A$, there exists an open set $U$ such that:
> $$A \subseteq U \subseteq \operatorname{cl}(U) \subseteq W$$

> **Proof:**
> **($\Rightarrow$)** Let $A$ be closed and $A \subseteq W$ with $W$ open.
> Then $B = X \setminus W$ is closed, and $A \cap B = \emptyset$.
> By normality, there exist disjoint open sets $U, V$ with $A \subseteq U$ and $B \subseteq V$.
> Since $U \cap V = \emptyset$, $U \subseteq X \setminus V$.
> Since $X \setminus V$ is closed, $\operatorname{cl}(U) \subseteq X \setminus V$.
> Since $B \subseteq V$, $X \setminus V \subseteq X \setminus B = W$.
> Thus $A \subseteq U \subseteq \operatorname{cl}(U) \subseteq W$.
>
> **($\Leftarrow$)** Let $A, B$ be disjoint closed sets.
> Then $W = X \setminus B$ is an open set containing $A$.
> By hypothesis, choose open $U$ with $A \subseteq U \subseteq \operatorname{cl}(U) \subseteq W$.
> Let $V = X \setminus \operatorname{cl}(U)$.
> Then $V$ is open, $B = X \setminus W \subseteq X \setminus \operatorname{cl}(U) = V$, and $U \cap V = \emptyset$.
> Thus $X$ is normal. $\blacksquare$"""
            },
            {
                "secNumber": "6.2",
                "title": "Completely Regular Spaces ($T_{3.5}$, Tychonoff Spaces)",
                "content": r"""### 1. Separation by Continuous Functions

Andrey Tychonoff in 1930 introduced the intermediate separation axiom that bridges topology and functional analysis.

> **Definition 6.2 (Completely Regular / $T_{3.5}$ / Tychonoff Space):**
> 1. A topological space $(X, \mathcal{T})$ is called **completely regular** if for every closed set $F \subseteq X$ and every point $x \notin F$, there exists a **continuous function**:
>    $$f: X \to [0, 1]$$
>    such that:
>    $$f(x) = 0 \quad \text{and} \quad f(y) = 1 \text{ for all } y \in F$$
> 2. A space is called a **Tychonoff space** (or **$T_{3.5}$ space**) if it is completely regular and $T_1$.

---

### 2. Position in the Separation Hierarchy

$$\text{Normal } (T_4) \implies \text{Tychonoff } (T_{3.5}) \implies \text{Regular } (T_3) \implies \text{Hausdorff } (T_2) \implies T_1 \implies T_0$$

> **Theorem 6.3 (Subspace and Product Preservation of $T_{3.5}$):**
> 1. Complete regularity is **hereditary**: every subspace of a Tychonoff space is a Tychonoff space.
> 2. Complete regularity is **product-invariant**: arbitrary Cartesian products of Tychonoff spaces are Tychonoff spaces.
> 3. A topological space is Tychonoff if and only if it is homeomorphic to a subspace of a compact Hausdorff space (an embedding into a cube $[0, 1]^I$)."""
            },
            {
                "secNumber": "6.3",
                "title": "Urysohn's Lemma: The Master Existence Theorem",
                "content": r"""### 1. Statement of Urysohn's Lemma

Pavel Urysohn proved in 1925 what is widely recognized as one of the most brilliant and fundamental theorems of general topology.

> **Theorem 6.4 (Urysohn's Lemma):**
> Let $X$ be a **normal space**, and let $A$ and $B$ be two disjoint closed subsets of $X$ ($A \cap B = \emptyset$).
> Then there exists a **continuous function**:
> $$f: X \to [0, 1]$$
> such that:
> $$f(x) = 0 \quad \text{for all } x \in A, \qquad \text{and} \qquad f(x) = 1 \quad \text{for all } x \in B$$

---

### 2. Full Line-by-Line Proof of Urysohn's Lemma

> **Proof:**
> The proof proceeds by constructing a nested family of open sets indexed by the **dyadic rational numbers** in $[0, 1]$.
>
> **Step 1: Dyadic Rationals Indexing.**
> Let $\mathbb{D} = \{m / 2^k : k \in \mathbb{N}_0, \; 0 \le m \le 2^k\}$ be the set of dyadic rationals in $[0, 1]$.
> $\mathbb{D}$ is countably infinite and dense in $[0, 1]$.
> Arrange the dyadic rationals in a sequence $r_0, r_1, r_2, \dots$ starting with $r_0 = 1$ and $r_1 = 0$.
>
> **Step 2: Constructing the Open Set Chain $\{U_r\}_{r \in \mathbb{D}}$.**
> We construct for each $r \in \mathbb{D}$ an open set $U_r \subseteq X$ such that:
> $$p < q \implies \operatorname{cl}(U_p) \subseteq U_q$$
> - For $r = 1$: let $U_1 = X \setminus B$. Since $B$ is closed, $U_1$ is open, and $A \subseteq U_1$.
> - For $r = 0$: $A$ is closed and $A \subseteq U_1$. By Theorem 6.2 (normality), choose open $U_0$ such that:
>   $$A \subseteq U_0 \subseteq \operatorname{cl}(U_0) \subseteq U_1$$
> - Inductive Construction: Let $\mathbb{D}_n = \{m / 2^n : 0 \le m \le 2^n\}$.
>   Assume $U_r$ has been defined for all $r \in \mathbb{D}_{n-1}$ satisfying the condition $\operatorname{cl}(U_p) \subseteq U_q$ whenever $p < q$.
>   For each new dyadic fraction $r = \frac{2m + 1}{2^n} \in \mathbb{D}_n \setminus \mathbb{D}_{n-1}$, its immediate neighbors in $\mathbb{D}_{n-1}$ are:
>   $$p = \frac{m}{2^{n-1}} = \frac{2m}{2^n} \quad \text{and} \quad q = \frac{m+1}{2^{n-1}} = \frac{2m+2}{2^n}$$
>   By induction, $\operatorname{cl}(U_p) \subseteq U_q$.
>   By Theorem 6.2, choose open $U_r$ such that:
>   $$\operatorname{cl}(U_p) \subseteq U_r \subseteq \operatorname{cl}(U_r) \subseteq U_q$$
> Repeating this for all $r \in \mathbb{D}_n$ completes the inductive step!
>
> We have constructed open sets $U_r$ for every $r \in \mathbb{D}$ such that:
> $$p < q \implies \operatorname{cl}(U_p) \subseteq U_q$$
> For convenience, define $U_r = \emptyset$ for $r < 0$, and $U_r = X$ for $r > 1$.
>
> **Step 3: Defining the Function $f: X \to [0, 1]$.**
> For every $x \in X$, define:
> $$f(x) = \inf \{r \in \mathbb{D} : x \in U_r\}$$
> - If $x \in A$, then $x \in U_r$ for all $r \ge 0$, so $f(x) = 0$.
> - If $x \in B$, then $x \notin U_1 = X \setminus B$. Hence $x \notin U_r$ for any $r \le 1$, so $f(x) = 1$.
> - For all $x \in X$, $0 \le f(x) \le 1$.
>
> **Step 4: Proving Continuity of $f$.**
> We prove that for any $a \in \mathbb{R}$, the sets $\{x : f(x) < a\}$ and $\{x : f(x) > a\}$ are open in $X$.
> 1. By definition of infimum:
>    $$f(x) < a \iff \exists r \in \mathbb{D} \text{ such that } r < a \text{ and } x \in U_r$$
>    Therefore:
>    $$\{x \in X : f(x) < a\} = \bigcup_{\substack{r \in \mathbb{D} \\ r < a}} U_r$$
>    Since each $U_r$ is open, this is an arbitrary union of open sets, which is **open**!
> 2. Next, we show:
>    $$f(x) > a \iff \exists s \in \mathbb{D} \text{ such that } s > a \text{ and } x \notin \operatorname{cl}(U_s)$$
>    - If $f(x) > a$, choose dyadics $s, t$ such that $a < s < t < f(x)$.
>      Since $t < f(x)$, $x \notin U_t$.
>      Since $\operatorname{cl}(U_s) \subseteq U_t$, we have $x \notin \operatorname{cl}(U_s)$.
>    - Conversely, if $x \notin \operatorname{cl}(U_s)$, then $x \notin U_s$, so $f(x) \ge s > a$.
>    Therefore:
>    $$\{x \in X : f(x) > a\} = \bigcup_{\substack{s \in \mathbb{D} \\ s > a}} (X \setminus \operatorname{cl}(U_s))$$
>    Since each $\operatorname{cl}(U_s)$ is closed, $X \setminus \operatorname{cl}(U_s)$ is open.
>    Hence $\{x : f(x) > a\}$ is an arbitrary union of open sets, which is **open**!
>
> Since the open rays $(-\infty, a)$ and $(a, \infty)$ form a subbasis for the standard topology on $\mathbb{R}$, $f: X \to [0, 1]$ is **continuous**. $\blacksquare$"""
            },
            {
                "secNumber": "6.4",
                "title": "The Tietze Extension Theorem",
                "content": r"""### 1. Statement of the Tietze Extension Theorem

Heinrich Tietze in 1915 proved that continuous functions on closed subspaces can always be extended continuously to the entire space!

> **Theorem 6.5 (Tietze Extension Theorem):**
> Let $X$ be a **normal space** and let $A \subseteq X$ be a **closed subset**.
> 1. **Bounded Formulation:** Any continuous function $f: A \to [a, b]$ has a continuous extension:
>    $$F: X \to [a, b] \qquad \text{such that} \quad F|_A = f$$
> 2. **Unbounded Formulation:** Any continuous function $f: A \to \mathbb{R}$ has a continuous extension:
>    $$F: X \to \mathbb{R} \qquad \text{such that} \quad F|_A = f$$

> **Proof Outline (Urysohn Series Approximation):**
> Without loss of generality, assume $[a, b] = [-1, 1]$.
> Define the disjoint closed subsets of $A$ (which are closed in $X$):
> $$A_0 = \{x \in A : f(x) \le -1/3\}, \qquad B_0 = \{x \in A : f(x) \ge 1/3\}$$
> By Urysohn's Lemma, there exists continuous $g_0: X \to [-1/3, 1/3]$ with $g_0(A_0) = -1/3$ and $g_0(B_0) = 1/3$.
> Then on $A$, the error is reduced:
> $$|f(x) - g_0(x)| \le \frac{2}{3}, \qquad \forall x \in A$$
> Inductively constructing functions $g_n: X \to \mathbb{R}$ such that:
> $$|g_n(x)| \le \frac{1}{3} \left(\frac{2}{3}\right)^n \quad \text{and} \quad \left|f(x) - \sum_{k=0}^n g_k(x)\right| \le \left(\frac{2}{3}\right)^{n+1}$$
> By the Weierstrass M-test, the series $F(x) = \sum_{n=0}^\infty g_n(x)$ converges uniformly on $X$.
> Hence $F: X \to [-1, 1]$ is continuous, and $F(x) = f(x)$ for all $x \in A$. $\blacksquare$"""
            },
            {
                "secNumber": "6.5",
                "title": "The Urysohn Metrization Theorem",
                "content": r"""### 1. When is a Topological Space Metrizable?

A fundamental quest of topology is finding purely topological conditions that guarantee a space comes from a metric.

> **Theorem 6.6 (Urysohn Metrization Theorem, 1925):**
> Every **second-countable regular ($T_3$) space** is **metrizable**.
> In fact, every such space can be **topologically embedded into the Hilbert cube** $I^\infty = [0, 1]^\mathbb{N}$.

> **Proof Strategy:**
> 1. By Urysohn's Lemma, since $X$ is regular and second-countable (hence normal), for each pair of basic open sets $B_n, B_m$ with $\operatorname{cl}(B_n) \subseteq B_m$, construct a continuous function $f_{n,m}: X \to [0, 1]$ with $f_{n,m}(\operatorname{cl}(B_n)) = 0$ and $f_{n,m}(X \setminus B_m) = 1$.
> 2. The collection $\{f_{n,m}\}$ is countable; enumerate it as $\{f_k\}_{k=1}^\infty$.
> 3. Define the embedding map $e: X \to [0, 1]^\mathbb{N}$ by $e(x) = (f_k(x))_{k=1}^\infty$.
> 4. Equip $[0, 1]^\mathbb{N}$ with the metric $d(u, v) = \sum_{k=1}^\infty \frac{|u_k - v_k|}{2^k}$.
> 5. Prove that $e: X \to e(X)$ is a homeomorphism, thereby pulling back the metric $d$ onto $X$! $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "prob_6_1",
                "tier": "Foundational",
                "title": "Normality of Metric Spaces via Distance Functions",
                "statement": r"""Let $(X, d)$ be a metric space, and let $A, B \subseteq X$ be two non-empty disjoint closed subsets ($A \cap B = \emptyset$).
For any point $x \in X$, let $d(x, A) = \inf_{a \in A} d(x, a)$.
1. Prove that the distance function $x \mapsto d(x, A)$ is Lipschitz continuous with Lipschitz constant $1$:
   $$|d(x, A) - d(y, A)| \le d(x, y), \qquad \forall x, y \in X$$
2. Prove that $d(x, A) + d(x, B) > 0$ for all $x \in X$.
3. Define the function $f: X \to [0, 1]$ by:
   $$f(x) = \frac{d(x, A)}{d(x, A) + d(x, B)}$$
   Prove that $f$ is continuous, $f(x) = 0$ for all $x \in A$, and $f(x) = 1$ for all $x \in B$.
4. Use $f$ to construct explicit disjoint open sets $U$ and $V$ separating $A$ and $B$, proving $(X, d)$ is normal ($T_4$).""",
                "solution": r"""### 1. Lipschitz Continuity of $d(x, A)$

For any $x, y \in X$ and any $a \in A$:
$$d(x, a) \le d(x, y) + d(y, a)$$
Taking the infimum over all $a \in A$:
$$d(x, A) \le d(x, y) + d(y, A) \implies d(x, A) - d(y, A) \le d(x, y)$$
Reversing the roles of $x$ and $y$:
$$d(y, A) - d(x, A) \le d(y, x) = d(x, y) \implies -(d(x, A) - d(y, A)) \le d(x, y)$$
Combining both inequalities:
$$|d(x, A) - d(y, A)| \le d(x, y)$$
Thus $x \mapsto d(x, A)$ is Lipschitz continuous with Lipschitz constant $L = 1$.

---

### 2. Denominator is Strictly Positive

Since $A$ and $B$ are closed:
- $d(x, A) = 0 \iff x \in \operatorname{cl}(A) = A$.
- $d(x, B) = 0 \iff x \in \operatorname{cl}(B) = B$.
Since $A \cap B = \emptyset$, no point $x$ can belong to both $A$ and $B$.
Therefore, it is impossible for both $d(x, A) = 0$ and $d(x, B) = 0$.
At least one of the distances is strictly positive for every $x \in X$:
$$d(x, A) + d(x, B) > 0, \qquad \forall x \in X$$

---

### 3. Properties of $f(x)$

- **Continuity:** Both the numerator $d(x, A)$ and denominator $d(x, A) + d(x, B)$ are continuous, and the denominator is strictly positive everywhere.
  The quotient of continuous functions with non-zero denominator is continuous.
  Hence $f: X \to [0, 1]$ is continuous.
- **On Set $A$:** For $x \in A$, $d(x, A) = 0$ and $d(x, B) > 0$.
  Thus $f(x) = \frac{0}{0 + d(x, B)} = 0$.
- **On Set $B$:** For $x \in B$, $d(x, B) = 0$ and $d(x, A) > 0$.
  Thus $f(x) = \frac{d(x, A)}{d(x, A) + 0} = 1$.

---

### 4. Construction of Disjoint Open Neighborhoods

Define the sets:
$$U = f^{-1}\left(\left[0, \frac{1}{3}\right)\right) = \left\{ x \in X : f(x) < \frac{1}{3} \right\}$$
$$V = f^{-1}\left(\left(\frac{2}{3}, 1\right]\right) = \left\{ x \in X : f(x) > \frac{2}{3} \right\}$$
- Since $f$ is continuous and $[0, 1/3)$ and $(2/3, 1]$ are open in the subspace $[0, 1]$, $U$ and $V$ are **open in $X$**.
- For every $x \in A$, $f(x) = 0 < 1/3 \implies A \subseteq U$.
- For every $x \in B$, $f(x) = 1 > 2/3 \implies B \subseteq V$.
- If $z \in U \cap V$, then $f(z) < 1/3$ and $f(z) > 2/3$, which is impossible! Thus $U \cap V = \emptyset$.
Therefore, $(X, d)$ is **normal ($T_4$)**. $\blacksquare$"""
            },
            {
                "id": "prob_6_2",
                "tier": "Advanced",
                "title": "Construction of Smooth Urysohn Bump Functions with Compact Support",
                "statement": r"""In Euclidean space $\mathbb{R}^n$, construct an explicit smooth ($C^\infty$) Urysohn bump function $f: \mathbb{R}^n \to [0, 1]$ such that:
1. $f(x) = 1$ for all $\|x\| \le 1$ (on the closed unit ball $\bar{B}_1$).
2. $f(x) = 0$ for all $\|x\| \ge 2$ (outside the closed ball $\bar{B}_2$).
3. $f$ is infinitely differentiable ($C^\infty$) on all of $\mathbb{R}^n$.""",
                "solution": r"""### 1. The Standard Smooth Transition Function

Define the classic Cauchy flat function $h: \mathbb{R} \to \mathbb{R}$:
$$h(t) = \begin{cases} e^{-1/t} & \text{if } t > 0 \\ 0 & \text{if } t \le 0 \end{cases}$$
By standard calculus, $h$ is infinitely differentiable ($C^\infty$) on all of $\mathbb{R}$, with all derivatives vanishing at $t = 0$: $h^{(k)}(0) = 0$ for all $k \ge 1$.

---

### 2. Constructing the 1D Transition Function

Now define $g: \mathbb{R} \to [0, 1]$ by:
$$g(t) = \frac{h(2 - t)}{h(2 - t) + h(t - 1)}$$
Notice that for all $t \in \mathbb{R}$:
- If $t \le 1$: $t - 1 \le 0 \implies h(t - 1) = 0$. Meanwhile $2 - t \ge 1 > 0 \implies h(2 - t) > 0$.
  Thus $g(t) = \frac{h(2 - t)}{h(2 - t) + 0} = 1$.
- If $t \ge 2$: $2 - t \le 0 \implies h(2 - t) = 0$. Meanwhile $t - 1 \ge 1 > 0 \implies h(t - 1) > 0$.
  Thus $g(t) = \frac{0}{0 + h(t - 1)} = 0$.
- For $1 < t < 2$: both $2 - t > 0$ and $t - 1 > 0$, so $h(2 - t) > 0$ and $h(t - 1) > 0$.
  The denominator is strictly positive everywhere, so $g(t) \in (0, 1)$ is smooth.

Hence $g: \mathbb{R} \to [0, 1]$ is a smooth function with $g(t) = 1$ for $t \le 1$ and $g(t) = 0$ for $t \ge 2$.

---

### 3. Radial Extension to $\mathbb{R}^n$

For $x \in \mathbb{R}^n$, define the radial function:
$$f(x) = g(\|x\|^2)$$
- For $\|x\| \le 1$: $\|x\|^2 \le 1 \implies f(x) = g(\|x\|^2) = 1$.
- For $\|x\| \ge \sqrt{2} \approx 1.414$ (or setting $g(t)$ to scale between $1$ and $4$ for $r \in [1, 2]$):
  Setting $f(x) = g(\|x\|)$ or $g(\|x\|^2 / 2)$:
  Specifically, setting $f(x) = \frac{h(4 - \|x\|^2)}{h(4 - \|x\|^2) + h(\|x\|^2 - 1)}$:
  - If $\|x\| \le 1$, $\|x\|^2 \le 1 \implies f(x) = 1$.
  - If $\|x\| \ge 2$, $\|x\|^2 \ge 4 \implies f(x) = 0$.
  - Since $x \mapsto \|x\|^2 = \sum_{i=1}^n x_i^2$ is smooth on $\mathbb{R}^n$, the composition $f$ is $C^\infty(\mathbb{R}^n)$.

This provides an explicit smooth Urysohn bump function with compact support in $\bar{B}_2(0)$."""
            },
            {
                "id": "prob_6_3",
                "tier": "Honors / Proof Challenge",
                "title": "Complete Proof of the Dyadic Continuity in Urysohn's Lemma",
                "statement": r"""Provide the complete, rigorous mathematical proof that the potential function:
$$f(x) = \inf \{r \in \mathbb{D} : x \in U_r\}$$
constructed in Urysohn's Lemma is **continuous**:
1. Prove that for any $a \in \mathbb{R}$, $f(x) < a \iff \exists r \in \mathbb{D} \text{ with } r < a \text{ such that } x \in U_r$.
2. Prove that for any $a \in \mathbb{R}$, $f(x) > a \iff \exists s \in \mathbb{D} \text{ with } s > a \text{ such that } x \notin \operatorname{cl}(U_s)$.
3. Deduce that the preimages $f^{-1}((-\infty, a))$ and $f^{-1}((a, \infty))$ are open in $X$, completing the proof that $f: X \to [0, 1]$ is continuous.""",
                "solution": r"""### 1. Characterization of the Sublevel Sets $\{x : f(x) < a\}$

Let $a \in \mathbb{R}$.
We prove that:
$$f(x) < a \iff x \in \bigcup_{\substack{r \in \mathbb{D} \\ r < a}} U_r$$

**($\Rightarrow$)** Suppose $f(x) < a$.
By definition, $f(x) = \inf \{r \in \mathbb{D} : x \in U_r\}$.
By the definition of the infimum, there exists some $r_0 \in \mathbb{D}$ such that $x \in U_{r_0}$ and $r_0 < a$.
Therefore, $x \in \bigcup_{r < a} U_r$.

**($\Leftarrow$)** Suppose $x \in \bigcup_{r < a} U_r$.
Then there exists some $r_0 \in \mathbb{D}$ with $r_0 < a$ such that $x \in U_{r_0}$.
By definition of $f(x)$ as the infimum of all such values:
$$f(x) = \inf \{r \in \mathbb{D} : x \in U_r\} \le r_0 < a$$
Thus $f(x) < a$.

Since each $U_r$ is open in $X$, the union:
$$f^{-1}((-\infty, a)) = \{x \in X : f(x) < a\} = \bigcup_{\substack{r \in \mathbb{D} \\ r < a}} U_r$$
is an arbitrary union of open sets, which is **open in $X$**.

---

### 2. Characterization of the Superlevel Sets $\{x : f(x) > a\}$

Let $a \in \mathbb{R}$.
We prove that:
$$f(x) > a \iff x \in \bigcup_{\substack{s \in \mathbb{D} \\ s > a}} (X \setminus \operatorname{cl}(U_s))$$

**($\Rightarrow$)** Suppose $f(x) > a$.
Since the dyadic rationals $\mathbb{D}$ are dense in $\mathbb{R}$, choose two dyadic rationals $s, t \in \mathbb{D}$ such that:
$$a < s < t < f(x)$$
Since $t < f(x) = \inf \{r \in \mathbb{D} : x \in U_r\}$, the point $x$ **cannot** belong to $U_t$ (otherwise $f(x) \le t$).
Thus $x \notin U_t$.
Recall the fundamental property of the dyadic chain:
$$s < t \implies \operatorname{cl}(U_s) \subseteq U_t$$
Since $x \notin U_t$, we must have $x \notin \operatorname{cl}(U_s)$.
Therefore:
$$x \in X \setminus \operatorname{cl}(U_s)$$
Since $s \in \mathbb{D}$ and $s > a$, $x \in \bigcup_{s > a} (X \setminus \operatorname{cl}(U_s))$.

**($\Leftarrow$)** Suppose $x \in \bigcup_{s > a} (X \setminus \operatorname{cl}(U_s))$.
Then there exists $s \in \mathbb{D}$ with $s > a$ such that $x \notin \operatorname{cl}(U_s)$.
Since $U_s \subseteq \operatorname{cl}(U_s)$, $x \notin U_s$.
Furthermore, for any $r \in \mathbb{D}$ with $r \le s$, we have $U_r \subseteq U_s$, so $x \notin U_r$.
Therefore, any $r \in \mathbb{D}$ for which $x \in U_r$ must satisfy $r > s$.
Taking the infimum over all such $r$:
$$f(x) = \inf \{r \in \mathbb{D} : x \in U_r\} \ge s > a$$
Thus $f(x) > a$.

Since each $\operatorname{cl}(U_s)$ is a closed set in $X$, the complement $X \setminus \operatorname{cl}(U_s)$ is **open in $X$**.
The union of open sets:
$$f^{-1}((a, \infty)) = \{x \in X : f(x) > a\} = \bigcup_{\substack{s \in \mathbb{D} \\ s > a}} (X \setminus \operatorname{cl}(U_s))$$
is therefore **open in $X$**.

---

### 3. Conclusion of Continuity

The collection of open rays:
$$\mathcal{S} = \{(-\infty, a) : a \in \mathbb{R}\} \cup \{(a, \infty) : a \in \mathbb{R}\}$$
forms a subbasis for the standard topology on $\mathbb{R}$.
Since the preimage under $f$ of every subbasis element is open in $X$ (as established in Parts 1 and 2), by Theorem 3.1(7), the function:
$$f: X \to [0, 1]$$
is **continuous**. $\blacksquare$"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u6 = get_unit6()
    print(f"Loaded Unit 6: {u6['title']} with {len(u6['sections'])} sections and {len(u6['problems'])} problems.")
