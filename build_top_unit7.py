# -*- coding: utf-8 -*-
"""
build_top_unit7.py
Constructs Unit 7: Compactness, Tychonoff's Theorem & Metric Compactness
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Compactness, Tychonoff's Theorem & Metric Compactness",
        "leadSummary": "Global topological finiteness: open coverings and finite subcovers, the Finite Intersection Property (FIP) dual formulation, compact subsets of Hausdorff spaces, compactness of continuous images and the Extreme Value Theorem, characterizations in metric spaces (equivalence of compactness, sequential compactness, and limit point compactness), the Lebesgue Covering Lemma and total boundedness, locally compact spaces and the Alexandroff one-point compactification $\\alpha X = X \\cup \\{\\infty\\}$, and Tychonoff's Theorem for arbitrary Cartesian products.",
        "simulations": ["sim_top_compact_open_covers"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Compact Spaces & The Finite Intersection Property",
                "content": r"""### 1. The Open Covering Definition of Compactness

Compactness generalizes the notion of finiteness to infinite topological spaces.

> **Definition 7.1 (Compact Space):**
> A topological space $(X, \mathcal{T})$ is called **compact** if every **open cover** of $X$ admits a **finite subcover**.
> That is, if $\mathcal{U} = \{U_\alpha\}_{\alpha \in I}$ is a family of open sets such that:
> $$\bigcup_{\alpha \in I} U_\alpha = X$$
> then there exists a finite index subset $\{ \alpha_1, \alpha_2, \dots, \alpha_n \} \subseteq I$ such that:
> $$\bigcup_{k=1}^n U_{\alpha_k} = X$$
> A subset $K \subseteq X$ is compact if it is compact as a subspace with the relative topology.

---

### 2. Dual Formulation: The Finite Intersection Property (FIP)

Taking complements translates open coverings into closed sets with empty intersection.

> **Definition 7.2 (Finite Intersection Property - FIP):**
> A family $\mathcal{F}$ of subsets of $X$ is said to satisfy the **Finite Intersection Property (FIP)** if the intersection of any finite subcollection of members of $\mathcal{F}$ is non-empty:
> $$F_1 \cap F_2 \cap \cdots \cap F_n \ne \emptyset \qquad \text{for all } F_1, \dots, F_n \in \mathcal{F}$$

> **Theorem 7.1 (FIP Characterization of Compactness):**
> A topological space $X$ is **compact** if and only if every family $\mathcal{F}$ of **closed subsets** of $X$ with the Finite Intersection Property has a **non-empty intersection**:
> $$\bigcap_{F \in \mathcal{F}} F \ne \emptyset$$

> **Proof:**
> By De Morgan's Laws, a family of closed sets $\mathcal{F} = \{F_\alpha\}_{\alpha \in I}$ has $\bigcap_{\alpha \in I} F_\alpha = \emptyset$ if and only if their complements $\mathcal{U} = \{X \setminus F_\alpha\}_{\alpha \in I}$ form an open cover of $X$:
> $$\bigcup_{\alpha \in I} (X \setminus F_\alpha) = X \setminus \left( \bigcap_{\alpha \in I} F_\alpha \right) = X \setminus \emptyset = X$$
> By compactness, $\mathcal{U}$ has a finite subcover $\bigcup_{k=1}^n (X \setminus F_{\alpha_k}) = X$, which holds if and only if $\bigcap_{k=1}^n F_{\alpha_k} = \emptyset$.
> Contrapositively, if every finite intersection is non-empty, the total intersection $\bigcap_{\alpha \in I} F_\alpha$ cannot be empty. $\blacksquare$"""
            },
            {
                "secNumber": "7.2",
                "title": "Compact Subsets of Hausdorff Spaces & Normality",
                "content": r"""### 1. Compactness in Hausdorff Spaces

In general topological spaces, compact subsets need not be closed (for example, in an indiscrete space, any subset is compact, but only $\emptyset$ and $X$ are closed). In Hausdorff spaces, however, compactness confers closedness!

> **Theorem 7.2 (Compact Subsets of $T_2$ Spaces are Closed):**
> Let $X$ be a **Hausdorff space**. If $K \subseteq X$ is a compact subset, then $K$ is **closed in $X$**.

> **Proof:**
> We prove that $X \setminus K$ is open.
> Let $x \in X \setminus K$. For every point $y \in K$, we have $x \ne y$.
> Since $X$ is Hausdorff, there exist disjoint open sets $U_y$ and $V_y$ such that:
> $$x \in U_y, \quad y \in V_y, \qquad \text{and} \qquad U_y \cap V_y = \emptyset$$
> The family $\{V_y\}_{y \in K}$ forms an open cover of $K$:
> $$K \subseteq \bigcup_{y \in K} V_y$$
> Since $K$ is compact, there exists a finite subcover $\{V_{y_1}, V_{y_2}, \dots, V_{y_n}\}$ such that:
> $$K \subseteq \bigcup_{i=1}^n V_{y_i} = V$$
> Now consider the corresponding intersection of neighborhoods of $x$:
> $$U = \bigcap_{i=1}^n U_{y_i}$$
> Since $n$ is finite, $U$ is an open neighborhood of $x$.
> Moreover, for each $i \in \{1, \dots, n\}$, $U \subseteq U_{y_i}$, and $U_{y_i} \cap V_{y_i} = \emptyset$.
> Thus:
> $$U \cap V = U \cap \left( \bigcup_{i=1}^n V_{y_i} \right) = \bigcup_{i=1}^n (U \cap V_{y_i}) \subseteq \bigcup_{i=1}^n (U_{y_i} \cap V_{y_i}) = \emptyset$$
> Since $U \cap V = \emptyset$ and $K \subseteq V$, we have $U \cap K = \emptyset$, so $U \subseteq X \setminus K$.
> Since $x \in X \setminus K$ was arbitrary, $X \setminus K$ is open.
> Therefore, $K$ is closed in $X$. $\blacksquare$

---

### 2. Compact Hausdorff Spaces are Normal

> **Theorem 7.3:**
> Every compact Hausdorff space is **normal ($T_4$)**.

> **Proof:**
> Applying the finite subcover argument of Theorem 7.2 once more separates any point $x$ from a disjoint compact set $K$ (proving regularity, $T_3$), and applying it a second time across two disjoint closed (hence compact) sets $A$ and $B$ separates them by disjoint open sets. $\blacksquare$"""
            },
            {
                "secNumber": "7.3",
                "title": "Compactness in Metric Spaces: Sequential & Total Boundedness",
                "content": r"""### 1. Three Notions of Compactness in Metric Spaces

> **Definition 7.3:**
> Let $(X, d)$ be a metric space.
> 1. $X$ is **compact** if every open cover has a finite subcover.
> 2. $X$ is **sequentially compact** if every sequence $(x_n)_{n=1}^\infty$ in $X$ has a **convergent subsequence**.
> 3. $X$ is **limit point compact** (or Bolzano-Weierstrass compact) if every infinite subset has an **accumulation point**.

> **Theorem 7.4 (Equivalence in Metric Spaces):**
> For any metric space $(X, d)$, the following three conditions are **logically equivalent**:
> $$\text{Compact} \iff \text{Sequentially Compact} \iff \text{Limit Point Compact}$$

---

### 2. The Lebesgue Covering Lemma

> **Lemma 7.1 (Lebesgue's Covering Lemma):**
> Let $(X, d)$ be a **compact metric space**, and let $\mathcal{U} = \{U_\alpha\}_{\alpha \in I}$ be an open cover of $X$.
> Then there exists a number $\delta > 0$ (called a **Lebesgue number** for $\mathcal{U}$) such that for every point $x \in X$, the open ball $B(x, \delta)$ is entirely contained in at least one member of $\mathcal{U}$:
> $$\forall x \in X, \; \exists \alpha \in I \text{ such that } B(x, \delta) \subseteq U_\alpha$$

---

### 3. Total Boundedness

> **Definition 7.4 (Total Boundedness):**
> A metric space $(X, d)$ is called **totally bounded** (or **precompact**) if for every $\varepsilon > 0$, $X$ can be covered by **finitely many open balls of radius $\varepsilon$**:
> $$X = \bigcup_{i=1}^n B(x_i, \varepsilon)$$

> **Theorem 7.5 (Metric Compactness Characterization):**
> A metric space $(X, d)$ is **compact** if and only if it is **complete and totally bounded**."""
            },
            {
                "secNumber": "7.4",
                "title": "Locally Compact Spaces & The Alexandroff Compactification",
                "content": r"""### 1. Locally Compact Spaces

Many important mathematical spaces are not compact, but possess compact neighborhoods around every point (e.g. Euclidean space $\mathbb{R}^n$).

> **Definition 7.5 (Locally Compact Space):**
> A topological space $(X, \mathcal{T})$ is called **locally compact** if every point $x \in X$ has a **compact neighborhood**.
> For Hausdorff spaces, this is equivalent to: every point has a local base consisting of compact sets.

---

### 2. Alexandroff One-Point Compactification

In 1924, Pavel Alexandroff showed that any locally compact Hausdorff space can be embedded into a compact space by adjoining a single "point at infinity" $\infty$.

> **Theorem 7.6 (Alexandroff Compactification):**
> Let $X$ be a locally compact Hausdorff space that is not compact.
> Let $\infty$ be an ideal point not in $X$, and define the extended set:
> $$\alpha X = X \cup \{\infty\}$$
> Topologize $\alpha X$ by declaring the open sets to be:
> 1. All open sets $U \subseteq X$.
> 2. All sets of the form $(X \setminus K) \cup \{\infty\}$, where $K \subseteq X$ is **compact**.
>
> Then:
> 1. $\alpha X$ is a **compact Hausdorff space**.
> 2. $X$ is a **dense open subspace** of $\alpha X$.
> 3. The compactification is unique up to homeomorphism.

> **Example 7.1 ($\alpha(\mathbb{R}^n) \cong S^n$):**
> The one-point compactification of the real line $\mathbb{R}$ is homeomorphic to the circle $S^1$.
> In general, $\alpha(\mathbb{R}^n) \cong S^n$ via inverse stereographic projection!"""
            },
            {
                "secNumber": "7.5",
                "title": "Arbitrary Products & Tychonoff's Theorem",
                "content": r"""### 1. Statement of Tychonoff's Theorem

Published by Andrey Tychonoff in 1930, this is one of the pinnacle achievements of modern general topology.

> **Theorem 7.7 (Tychonoff's Theorem):**
> Let $\{X_\alpha\}_{\alpha \in I}$ be an arbitrary (possibly uncountably infinite) family of **compact topological spaces**.
> Then the product space:
> $$X = \prod_{\alpha \in I} X_\alpha$$
> equipped with the **product topology** is **compact**.

> **Remark on Axiom of Choice:**
> Tychonoff's Theorem for arbitrary products is **logically equivalent to the Axiom of Choice** (ZFC)!

---

### 2. Proof via Alexander's Subbase Theorem

> **Theorem 7.8 (Alexander Subbase Theorem, 1939):**
> Let $X$ be a topological space and let $\mathcal{S}$ be a **subbasis** for its topology.
> If every open cover of $X$ consisting **entirely of elements of $\mathcal{S}$** has a finite subcover, then $X$ is **compact**.

> **Proof of Tychonoff's Theorem:**
> By Definition 3.6, the canonical subbasis for the product topology on $X = \prod_{\alpha \in I} X_\alpha$ is:
> $$\mathcal{S} = \{\pi_\alpha^{-1}(U_\alpha) : \alpha \in I, \; U_\alpha \text{ is open in } X_\alpha\}$$
> Let $\mathcal{U} \subseteq \mathcal{S}$ be any open cover of $X$ consisting solely of subbasic open sets.
> For each $\alpha \in I$, let:
> $$\mathcal{U}_\alpha = \{U_\alpha \text{ open in } X_\alpha : \pi_\alpha^{-1}(U_\alpha) \in \mathcal{U}\}$$
>
> Suppose for contradiction that for **every** $\alpha \in I$, the family $\mathcal{U}_\alpha$ **fails to cover $X_\alpha$**.
> Then for each $\alpha \in I$, there exists a point $x_\alpha \in X_\alpha$ such that:
> $$x_\alpha \notin \bigcup_{U_\alpha \in \mathcal{U}_\alpha} U_\alpha$$
> Consider the point in the product space:
> $$x^* = (x_\alpha)_{\alpha \in I} \in \prod_{\alpha \in I} X_\alpha$$
> Since $\mathcal{U}$ covers $X$, $x^*$ must belong to some member of $\mathcal{U}$, say $\pi_\beta^{-1}(V_\beta) \in \mathcal{U}$.
> Then $\pi_\beta(x^*) = x_\beta \in V_\beta$.
> But by definition of $\mathcal{U}_\beta$, $V_\beta \in \mathcal{U}_\beta$, which means $x_\beta \in \bigcup_{U_\beta \in \mathcal{U}_\beta} U_\beta$!
> This directly contradicts the choice of $x_\beta$!
>
> Therefore, there must exist at least one index $\beta \in I$ such that $\mathcal{U}_\beta$ **covers $X_\beta$**:
> $$\bigcup_{U_\beta \in \mathcal{U}_\beta} U_\beta = X_\beta$$
> Since $X_\beta$ is compact by hypothesis, $\mathcal{U}_\beta$ contains a **finite subcover**:
> $$X_\beta = U_{\beta, 1} \cup U_{\beta, 2} \cup \cdots \cup U_{\beta, n}$$
> Pulling back under $\pi_\beta^{-1}$:
> $$X = \pi_\beta^{-1}(X_\beta) = \pi_\beta^{-1}(U_{\beta, 1}) \cup \cdots \cup \pi_\beta^{-1}(U_{\beta, n})$$
> We have obtained a finite subcover of $X$ from $\mathcal{U}$!
> By Alexander's Subbase Theorem (Theorem 7.8), $X = \prod_{\alpha \in I} X_\alpha$ is **compact**. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "prob_7_1",
                "tier": "Foundational",
                "title": "Continuous Bijections from Compact to Hausdorff Spaces",
                "statement": r"""Prove the fundamental topological theorem:
Let $f: X \to Y$ be a continuous bijective map from a compact space $X$ to a Hausdorff space $Y$.
1. Prove that for every closed subset $F \subseteq X$, its image $f(F)$ is closed in $Y$.
2. Deduce that $f$ is a closed map, and therefore its inverse function $f^{-1}: Y \to X$ is continuous.
3. Conclude that $f$ is a **homeomorphism**.""",
                "solution": r"""### 1. Images of Closed Sets are Closed

Let $F \subseteq X$ be an arbitrary closed subset of $X$.
- Since $X$ is compact and $F$ is closed in $X$, by basic compactness theory, $F$ is a **compact subspace** of $X$.
- Since $f: X \to Y$ is continuous, the restriction $f|_F: F \to Y$ is continuous.
  The continuous image of a compact set is compact; therefore, the image set $f(F)$ is a **compact subset of $Y$**.
- Since $Y$ is a **Hausdorff space**, by Theorem 7.2 (compact subsets of Hausdorff spaces are closed), the compact set $f(F)$ must be **closed in $Y$**.
Thus, $F \text{ closed in } X \implies f(F) \text{ closed in } Y$.

---

### 2. Continuity of the Inverse Function $f^{-1}$

A function is continuous if and only if preimages of closed sets are closed (Theorem 3.1).
Let $g = f^{-1}: Y \to X$ be the set-theoretic inverse of the bijection $f$.
For any closed set $F \subseteq X$:
$$g^{-1}(F) = (f^{-1})^{-1}(F) = f(F)$$
By Part 1, $f(F)$ is closed in $Y$.
Therefore, the preimage under $g = f^{-1}$ of every closed set in $X$ is closed in $Y$.
Hence, $f^{-1}: Y \to X$ is **continuous**!

---

### 3. Conclusion

Since $f$ is a continuous bijection and its inverse $f^{-1}$ is continuous, $f$ is by definition a **homeomorphism**:
$$X \cong Y \quad \blacksquare$$

This theorem is exceptionally useful in geometry and analysis: to show an invertible continuous map is a homeomorphism, one does NOT need to calculate the inverse formula if the domain is compact and the target is Hausdorff!"""
            },
            {
                "id": "prob_7_2",
                "tier": "Advanced",
                "title": "Alexandroff One-Point Compactification of $\\mathbb{R}^n$ is $S^n$",
                "statement": r"""Let $\mathbb{R}^n$ be equipped with the standard Euclidean topology, and let $\alpha(\mathbb{R}^n) = \mathbb{R}^n \cup \{\infty\}$ be its Alexandroff one-point compactification.
Consider the $n$-dimensional sphere $S^n \subset \mathbb{R}^{n+1}$ and the North Pole $N = (0, \dots, 0, 1)$.
Using the stereographic projection $\sigma: S^n \setminus \{N\} \to \mathbb{R}^n$:
1. Define the extension map $\Phi: S^n \to \alpha(\mathbb{R}^n)$ by $\Phi(x) = \sigma(x)$ for $x \ne N$ and $\Phi(N) = \infty$.
2. Prove that $\Phi$ is a continuous bijection.
3. Conclude that $\alpha(\mathbb{R}^n) \cong S^n$ are homeomorphic.""",
                "solution": r"""### 1. Definition and Bijectivity of $\Phi$

Define $\Phi: S^n \to \alpha(\mathbb{R}^n)$ by:
$$\Phi(x) = \begin{cases} \sigma(x) & \text{if } x \in S^n \setminus \{N\} \\ \infty & \text{if } x = N \end{cases}$$
- For $x \ne N$, $\sigma(x) \in \mathbb{R}^n$.
- By Problem 3.2, $\sigma: S^n \setminus \{N\} \to \mathbb{R}^n$ is a bijection.
- Since $\Phi(N) = \infty$, $\Phi$ maps $N$ to the point at infinity.
Therefore, $\Phi$ is a **bijection**.

---

### 2. Continuity of $\Phi$

To show $\Phi$ is continuous, we check the preimage of basic open sets in $\alpha(\mathbb{R}^n)$:
- **Open sets in $\mathbb{R}^n$:** Let $U \subseteq \mathbb{R}^n$ be open.
  Then $\Phi^{-1}(U) = \sigma^{-1}(U)$.
  Since $\sigma^{-1}$ is continuous, $\sigma^{-1}(U)$ is open in $S^n \setminus \{N\}$, hence open in $S^n$.
- **Neighborhoods of $\infty$:** Basic open neighborhoods of $\infty$ in $\alpha(\mathbb{R}^n)$ have the form:
  $$V = (\mathbb{R}^n \setminus K) \cup \{\infty\}$$
  where $K \subset \mathbb{R}^n$ is compact.
  The preimage is:
  $$\Phi^{-1}(V) = \sigma^{-1}(\mathbb{R}^n \setminus K) \cup \{N\} = S^n \setminus \sigma^{-1}(K)$$
  Since $K$ is compact and $\sigma^{-1}$ is continuous, $\sigma^{-1}(K)$ is a **compact subset of $S^n$**.
  Since $S^n$ is Hausdorff, the compact set $\sigma^{-1}(K)$ is **closed in $S^n$**.
  Therefore, its complement $\Phi^{-1}(V) = S^n \setminus \sigma^{-1}(K)$ is **open in $S^n$**!

Since the preimage of every open set in $\alpha(\mathbb{R}^n)$ is open in $S^n$, $\Phi$ is **continuous**.

---

### 3. Homeomorphism

- $S^n \subset \mathbb{R}^{n+1}$ is closed and bounded, hence **compact**.
- The one-point compactification $\alpha(\mathbb{R}^n)$ of a locally compact Hausdorff space is **Hausdorff** (Theorem 7.6).
- By Problem 7.1, any continuous bijection from a compact space to a Hausdorff space is a **homeomorphism**!
Therefore, $\Phi: S^n \to \alpha(\mathbb{R}^n)$ is a homeomorphism:
$$\alpha(\mathbb{R}^n) \cong S^n \quad \blacksquare$$"""
            },
            {
                "id": "prob_7_3",
                "tier": "Honors / Proof Challenge",
                "title": "Complete Proof of the Lebesgue Covering Lemma",
                "statement": r"""Provide the complete, rigorous mathematical proof of the Lebesgue Covering Lemma:

Let $(X, d)$ be a **sequentially compact metric space**, and let $\mathcal{U} = \{U_\alpha\}_{\alpha \in I}$ be an open cover of $X$.
Prove by contradiction that there exists a positive real number $\delta > 0$ such that for every point $x \in X$, there exists some index $\alpha \in I$ such that:
$$B(x, \delta) \subseteq U_\alpha$$""",
                "solution": r"""### Proof by Contradiction

Suppose for contradiction that no such $\delta > 0$ exists.
This means that for every positive integer $n \in \mathbb{N}$, the number $\delta = 1/n$ fails to be a Lebesgue number.
By definition of failure:
$$\text{For each } n \in \mathbb{N}, \text{ there exists a point } x_n \in X \text{ such that } B\left(x_n, \frac{1}{n}\right) \not\subseteq U_\alpha \quad \text{for all } \alpha \in I$$
That is, for every $\alpha \in I$, the ball $B(x_n, 1/n)$ contains points outside $U_\alpha$.

---

### Extraction of a Convergent Subsequence

We have constructed a sequence of points $(x_n)_{n=1}^\infty$ in $X$.
Since $(X, d)$ is sequentially compact, there exists a subsequence $(x_{n_k})_{k=1}^\infty$ that converges to some limit point $x^* \in X$:
$$\lim_{k \to \infty} x_{n_k} = x^* \in X$$

---

### The Contradiction

Since $\mathcal{U}$ is an open cover of $X$ and $x^* \in X$, the limit point $x^*$ must belong to at least one member of the cover, say:
$$x^* \in U_{\alpha_0} \quad \text{for some } \alpha_0 \in I$$
Because $U_{\alpha_0}$ is open, by Definition 1.3, there exists an open ball centered at $x^*$ with some radius $r > 0$ completely contained in $U_{\alpha_0}$:
$$B(x^*, r) \subseteq U_{\alpha_0}$$

Now, since $x_{n_k} \to x^*$, choose an index $K \in \mathbb{N}$ large enough such that:
1. $d(x_{n_K}, x^*) < \frac{r}{2}$
2. $\frac{1}{n_K} < \frac{r}{2}$

Now consider the open ball $B\left(x_{n_K}, \frac{1}{n_K}\right)$.
For any point $y \in B\left(x_{n_K}, \frac{1}{n_K}\right)$, we have $d(y, x_{n_K}) < \frac{1}{n_K} < \frac{r}{2}$.
By the triangle inequality:
$$d(y, x^*) \le d(y, x_{n_K}) + d(x_{n_K}, x^*) < \frac{r}{2} + \frac{r}{2} = r$$
This implies that $y \in B(x^*, r)$.
Since $B(x^*, r) \subseteq U_{\alpha_0}$, we have:
$$y \in U_{\alpha_0}$$
Because this holds for every $y \in B\left(x_{n_K}, \frac{1}{n_K}\right)$, we have proved:
$$B\left(x_{n_K}, \frac{1}{n_K}\right) \subseteq U_{\alpha_0}$$
This directly contradicts the defining property of $x_{n_K}$, which stated that $B(x_{n_K}, 1/n_K)$ was NOT contained in any member of $\mathcal{U}$!

---

### Conclusion

This contradiction proves our initial assumption was false.
Therefore, there must exist some $\delta > 0$ such that for every $x \in X$, $B(x, \delta) \subseteq U_\alpha$ for some $\alpha \in I$. $\blacksquare$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u7 = get_unit7()
    print(f"Loaded Unit 7: {u7['title']} with {len(u7['sections'])} sections and {len(u7['problems'])} problems.")
