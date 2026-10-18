# -*- coding: utf-8 -*-
"""
build_top_unit3.py
Constructs Unit 3: Continuity, Homeomorphisms, Weak Topologies & Quotient Spaces
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Continuity, Homeomorphisms, Weak Topologies & Quotient Spaces",
        "leadSummary": "Mappings between topological spaces: continuous functions and their equivalent characterizations (open preimages, closed preimages, closure inclusions $f(\\bar{A}) \\subseteq \\overline{f(A)}$), the Pasting (Gluing) Lemma, homeomorphisms and topological invariants, topological embeddings, initial (weak) and final topologies, function algebras $C(X, \\mathbb{R})$, and quotient spaces with 2-manifold identifications (cylinder, Möbius strip, torus, Klein bottle, and real projective plane $\\mathbb{RP}^2$).",
        "simulations": ["sim_top_quotient_surfaces"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Continuous Functions: Open Preimages & Closure Characterizations",
                "content": r"""### 1. Topological Continuity

In elementary calculus, continuity is formulated via $\varepsilon$-$\delta$ bounds. In general topology, continuity is expressed purely in terms of the preimage of open sets.

> **Definition 3.1 (Continuous Function):**
> Let $(X, \mathcal{T}_X)$ and $(Y, \mathcal{T}_Y)$ be topological spaces.
> A function $f: X \to Y$ is called **continuous** if the preimage of every open set in $Y$ is open in $X$:
> $$f^{-1}(V) \in \mathcal{T}_X \qquad \text{for every } V \in \mathcal{T}_Y$$
> We say $f$ is **continuous at a point $x_0 \in X$** if for every neighborhood $V$ of $f(x_0)$ in $Y$, the preimage $f^{-1}(V)$ is a neighborhood of $x_0$ in $X$.

---

### 2. Fundamental Characterization Theorem

> **Theorem 3.1 (Equivalent Characterizations of Continuity):**
> Let $f: X \to Y$ be a map between topological spaces. The following are logically equivalent:
> 1. $f$ is continuous (preimages of open sets are open).
> 2. The preimage of every closed set in $Y$ is closed in $X$:
>    $$K \text{ closed in } Y \implies f^{-1}(K) \text{ closed in } X$$
> 3. For every subset $A \subseteq X$, $f(\operatorname{cl}(A)) \subseteq \operatorname{cl}(f(A))$.
> 4. For every subset $B \subseteq Y$, $\operatorname{cl}(f^{-1}(B)) \subseteq f^{-1}(\operatorname{cl}(B))$.
> 5. For every subset $B \subseteq Y$, $f^{-1}(\operatorname{int}(B)) \subseteq \operatorname{int}(f^{-1}(B))$.
> 6. For a basis $\mathcal{B}$ of $Y$, $f^{-1}(B)$ is open in $X$ for all $B \in \mathcal{B}$.
> 7. For a subbasis $\mathcal{S}$ of $Y$, $f^{-1}(S)$ is open in $X$ for all $S \in \mathcal{S}$.

> **Proof of (1) $\iff$ (2):**
> Follows from the set-theoretic identity for complements under preimages:
> $$f^{-1}(Y \setminus B) = X \setminus f^{-1}(B)$$
> If $K \subseteq Y$ is closed, then $Y \setminus K$ is open.
> By (1), $f^{-1}(Y \setminus K) = X \setminus f^{-1}(K)$ is open in $X$, so $f^{-1}(K)$ is closed in $X$.
> The converse is identical.
>
> **Proof of (1) $\iff$ (3):**
> - **(1 $\implies$ 3):** Let $A \subseteq X$. The set $\operatorname{cl}(f(A))$ is closed in $Y$.
>   By (2), $f^{-1}(\operatorname{cl}(f(A)))$ is closed in $X$.
>   Since $f(A) \subseteq \operatorname{cl}(f(A))$, we have $A \subseteq f^{-1}(\operatorname{cl}(f(A)))$.
>   Since $\operatorname{cl}(A)$ is the smallest closed set containing $A$:
>   $$\operatorname{cl}(A) \subseteq f^{-1}(\operatorname{cl}(f(A))) \implies f(\operatorname{cl}(A)) \subseteq \operatorname{cl}(f(A))$$
> - **(3 $\implies$ 2):** Let $K \subseteq Y$ be closed. Let $A = f^{-1}(K)$.
>   By (3), $f(\operatorname{cl}(A)) \subseteq \operatorname{cl}(f(A)) = \operatorname{cl}(f(f^{-1}(K))) \subseteq \operatorname{cl}(K) = K$.
>   Thus $\operatorname{cl}(A) \subseteq f^{-1}(K) = A$.
>   Since $A \subseteq \operatorname{cl}(A)$ always, we have $\operatorname{cl}(A) = A$, so $A = f^{-1}(K)$ is closed. $\blacksquare$"""
            },
            {
                "secNumber": "3.2",
                "title": "The Pasting (Gluing) Lemma & Local Criteria",
                "content": r"""### 1. The Pasting (Gluing) Lemma

A crucial tool for constructing continuous maps from piecewise components.

> **Theorem 3.2 (The Pasting Lemma):**
> Let $X = A \cup B$, where $A$ and $B$ are **both closed** (or **both open**) in $X$.
> Let $f: A \to Y$ and $g: B \to Y$ be continuous functions that agree on the overlap:
> $$f(x) = g(x) \qquad \forall x \in A \cap B$$
> Then the combined function $h: X \to Y$ defined by:
> $$h(x) = \begin{cases} f(x) & \text{if } x \in A \\ g(x) & \text{if } x \in B \end{cases}$$
> is **continuous** on $X$.

> **Proof (Closed Case):**
> Let $K \subseteq Y$ be any closed set in $Y$.
> The preimage under $h$ is:
> $$h^{-1}(K) = \{x \in X : h(x) \in K\} = \{x \in A : f(x) \in K\} \cup \{x \in B : g(x) \in K\} = f^{-1}(K) \cup g^{-1}(K)$$
> - Since $f: A \to Y$ is continuous, $f^{-1}(K)$ is closed in the subspace $A$.
> - Since $A$ is closed in $X$, by Proposition 2.1, $f^{-1}(K)$ is **closed in $X$**.
> - Similarly, $g^{-1}(K)$ is closed in $B$, and since $B$ is closed in $X$, $g^{-1}(K)$ is **closed in $X$**.
> - The union of two closed sets in $X$ is closed in $X$:
>   $$h^{-1}(K) = f^{-1}(K) \cup g^{-1}(K) \text{ is closed in } X$$
> By Theorem 3.1, $h$ is continuous on $X$. $\blacksquare$

> **Cautionary Remark:**
> The Pasting Lemma **fails** if one set is open and the other is closed, or if neither is closed/open!
> For example, in $\mathbb{R} = (-\infty, 0) \cup [0, \infty)$, $f(x) = -1$ on $(-\infty, 0)$ and $g(x) = 1$ on $[0, \infty)$ are continuous on their domains, but the combined Heaviside step function is discontinuous at $x = 0$!"""
            },
            {
                "secNumber": "3.3",
                "title": "Homeomorphisms, Topological Invariants & Embeddings",
                "content": r"""### 1. Homeomorphisms

A homeomorphism is the topological analogue of an isomorphism: two spaces connected by a homeomorphism are structurally indistinguishable from the standpoint of topology.

> **Definition 3.2 (Homeomorphism):**
> A function $f: X \to Y$ between topological spaces is called a **homeomorphism** if:
> 1. $f$ is a **bijection** (one-to-one and onto).
> 2. $f$ is **continuous**.
> 3. The inverse function $f^{-1}: Y \to X$ is **continuous** (equivalently, $f$ is an **open map**).
>
> If a homeomorphism exists between $X$ and $Y$, we say that $X$ and $Y$ are **homeomorphic** (denoted $X \cong Y$).

> **Warning:**
> A continuous bijection is **NOT necessarily a homeomorphism**!
> Example: Let $X = [0, 2\pi)$ with the subspace topology of $\mathbb{R}$, and $Y = S^1 = \{e^{i\theta}\} \subset \mathbb{C}$.
> The map $f(\theta) = e^{i\theta}$ is a continuous bijection, but its inverse $f^{-1}$ is **discontinuous** at $(1, 0)$! (The half-open interval $[0, \pi)$ is open in $X$, but its image $f([0, \pi))$ is not open in $S^1$).

---

### 2. Topological Invariants

> **Definition 3.3 (Topological Invariant):**
> A property $P$ of a topological space is a **topological invariant** (or **topological property**) if whenever $X \cong Y$ and $X$ possesses property $P$, then $Y$ must also possess property $P$.
>
> **Canonical Topological Invariants:**
> - Compactness, Sequential Compactness, Local Compactness
> - Connectedness, Path-Connectedness, Number of Connected Components
> - Separation Axioms ($T_0, T_1, T_2, T_3, T_4$)
> - Countability Axioms (First-countability, Second-countability, Separability)
> - Fundamental Group $\pi_1(X)$, Homology Groups $H_k(X)$
> - Topological Dimension (Invariance of Domain: $\mathbb{R}^m \not\cong \mathbb{R}^n$ if $m \ne n$).

---

### 3. Topological Embeddings

> **Definition 3.4 (Embedding):**
> An injective continuous map $f: X \to Y$ is called a **topological embedding** if the corestriction:
> $$f: X \to f(X)$$
> is a homeomorphism onto its image $f(X)$ (equipped with the subspace topology inherited from $Y$)."""
            },
            {
                "secNumber": "3.4",
                "title": "Initial Topologies, Weak Topologies & Function Algebras",
                "content": r"""### 1. Initial (Weak) Topology

Given a set $X$ and a family of maps $f_\alpha: X \to Y_\alpha$ into topological spaces $(Y_\alpha, \mathcal{T}_\alpha)$, what is the most economical topology on $X$ that makes all $f_\alpha$ continuous?

> **Definition 3.5 (Initial / Weak Topology):**
> The **initial topology** (or **weak topology**) on $X$ induced by the family of maps $\{f_\alpha: X \to Y_\alpha\}_{\alpha \in I}$ is the **coarsest (smallest) topology** on $X$ with respect to which every map $f_\alpha$ is continuous.
> A subbasis for the initial topology is:
> $$\mathcal{S} = \{f_\alpha^{-1}(V_\alpha) : \alpha \in I, \; V_\alpha \in \mathcal{T}_\alpha\}$$

> **Theorem 3.3 (Universal Property of Initial Topologies):**
> A map $g: Z \to X$ from an arbitrary topological space $Z$ into $(X, \mathcal{T}_{\text{initial}})$ is **continuous** if and only if each composition:
> $$f_\alpha \circ g: Z \to Y_\alpha$$
> is continuous for all $\alpha \in I$.

---

### 2. The Product Topology as an Initial Topology

> **Definition 3.6 (Product Topology):**
> Let $\{X_\alpha\}_{\alpha \in I}$ be a family of topological spaces. The **product topology** on the Cartesian product $X = \prod_{\alpha \in I} X_\alpha$ is precisely the **initial topology** induced by the canonical projection maps:
> $$\pi_\beta: \prod_{\alpha \in I} X_\alpha \to X_\beta, \qquad \pi_\beta((x_\alpha)_{\alpha \in I}) = x_\beta$$
> A basis for the product topology consists of **cylinders**:
> $$B = \prod_{\alpha \in I} U_\alpha, \qquad \text{where } U_\alpha \text{ is open in } X_\alpha \text{ and } U_\alpha = X_\alpha \text{ for all but finitely many } \alpha \in I$$

---

### 3. Function Algebras $C(X, \mathbb{R})$

For any topological space $X$, the set of continuous real-valued functions $C(X, \mathbb{R})$ forms an associative, commutative $\mathbb{R}$-algebra under pointwise addition, scalar multiplication, and pointwise multiplication:
$$(f + g)(x) = f(x) + g(x), \qquad (\lambda f)(x) = \lambda f(x), \qquad (f \cdot g)(x) = f(x) g(x)$$
The weak topology on $X$ induced by $C(X, \mathbb{R})$ plays a central role in Tychonoff spaces and Gelfand duality."""
            },
            {
                "secNumber": "3.5",
                "title": "Quotient Spaces, Identification Maps & Surface Topologies",
                "content": r"""### 1. The Quotient Topology

> **Definition 3.7 (Quotient Space & Quotient Map):**
> Let $(X, \mathcal{T}_X)$ be a topological space and let $\sim$ be an equivalence relation on $X$.
> Let $Y = X / \sim$ be the set of equivalence classes, and let $q: X \to Y$ be the canonical projection $q(x) = [x]$.
> The **quotient topology** on $Y$ is the **finest (largest) topology** that makes $q$ continuous:
> $$\mathcal{T}_Y = \{V \subseteq Y : q^{-1}(V) \in \mathcal{T}_X\}$$
> More generally, a surjective map $p: X \to Y$ is called a **quotient map** (or **identification map**) if a subset $V \subseteq Y$ is open in $Y$ if and only if $p^{-1}(V)$ is open in $X$.

> **Theorem 3.4 (Universal Mapping Property of Quotient Spaces):**
> Let $p: X \to Y$ be a quotient map. A function $g: Y \to Z$ is **continuous** if and only if the composite map $g \circ p: X \to Z$ is continuous.

---

### 2. Classical Surface Topologies from the Unit Square $I^2$

Let $I^2 = [0, 1] \times [0, 1] \subset \mathbb{R}^2$ with the Euclidean subspace topology.

> **Identification 1: The Cylinder $S^1 \times [0, 1]$**
> Identify left and right edges with the same orientation:
> $$(0, y) \sim (1, y), \qquad \forall y \in [0, 1]$$
> The resulting quotient space is homeomorphic to the standard cylinder $S^1 \times [0, 1]$. It is an orientable 2-manifold with boundary.

> **Identification 2: The Möbius Strip**
> Identify left and right edges with a half-twist (reversed orientation):
> $$(0, y) \sim (1, 1 - y), \qquad \forall y \in [0, 1]$$
> The resulting quotient space is the **Möbius strip**. It is a **non-orientable** 2-manifold with boundary (a single closed boundary curve homeomorphic to $S^1$).

> **Identification 3: The Torus $T^2 = S^1 \times S^1$**
> Identify both pairs of opposite edges with standard orientation:
> $$(0, y) \sim (1, y) \quad \text{and} \quad (x, 0) \sim (x, 1)$$
> The quotient is a compact, connected, orientable 2-manifold without boundary, with Euler characteristic $\chi(T^2) = 0$.

> **Identification 4: The Klein Bottle $K^2$**
> Identify one pair of edges directly and the other with a twist:
> $$(0, y) \sim (1, 1 - y) \quad \text{and} \quad (x, 0) \sim (x, 1)$$
> The Klein bottle is a compact, connected, **non-orientable** 2-manifold without boundary, with $\chi(K^2) = 0$. It cannot be embedded in $\mathbb{R}^3$ without self-intersection, but embeds smoothly in $\mathbb{R}^4$.

> **Identification 5: The Real Projective Plane $\mathbb{RP}^2$**
> Identify antipodal points on the boundary:
> $$(x, 0) \sim (1 - x, 1) \quad \text{and} \quad (0, y) \sim (1, 1 - y)$$
> Equivalently, $\mathbb{RP}^2 \cong S^2 / \{\pm x\}$. It is a closed non-orientable surface with $\chi(\mathbb{RP}^2) = 1$."""
            }
        ],
        "problems": [
            {
                "id": "prob_3_1",
                "tier": "Foundational",
                "title": "Rigorous Application of the Pasting Lemma",
                "statement": r"""Consider the piecewise function $f: \mathbb{R} \to \mathbb{R}$ defined by:
$$f(x) = \begin{cases} x^2 + 2x & \text{if } x \le 1 \\ 4 - x & \text{if } x > 1 \end{cases}$$
1. Decompose the domain $\mathbb{R}$ into two closed subsets $A$ and $B$.
2. State the continuity of the restricted functions $f|_A$ and $f|_B$.
3. Check the gluing compatibility condition on $A \cap B$.
4. Formally invoke the Pasting Lemma (Theorem 3.2) to conclude that $f$ is continuous on the entire real line $\mathbb{R}$.""",
                "solution": r"""### 1. Closed Domain Decomposition

Let:
$$A = (-\infty, 1] \quad \text{and} \quad B = [1, \infty)$$
Notice that:
- $A$ is closed in $\mathbb{R}$ because its complement $(1, \infty)$ is open.
- $B$ is closed in $\mathbb{R}$ because its complement $(-\infty, 1)$ is open.
- $A \cup B = (-\infty, 1] \cup [1, \infty) = \mathbb{R}$.

---

### 2. Continuity of Domain Restrictions

- On $A$, $f|_A(x) = x^2 + 2x$ is a polynomial function, which is continuous on $\mathbb{R}$, hence continuous on the closed subspace $A$.
- On $B$, $f|_B(x) = 4 - x$ is an affine polynomial function, which is continuous on $\mathbb{R}$, hence continuous on the closed subspace $B$.

---

### 3. Compatibility Condition on Overlap

The intersection of the two closed domains is the singleton:
$$A \cap B = (-\infty, 1] \cap [1, \infty) = \{1\}$$
Evaluate both functions at the single intersection point $x = 1$:
$$f|_A(1) = 1^2 + 2(1) = 1 + 2 = 3$$
$$f|_B(1) = 4 - 1 = 3$$
Since $f|_A(1) = f|_B(1) = 3$, the functions agree on $A \cap B$.

---

### 4. Conclusion via Pasting Lemma

By the Pasting Lemma (Theorem 3.2):
Since $\mathbb{R} = A \cup B$ where both $A$ and $B$ are closed in $\mathbb{R}$, and $f|_A, f|_B$ are continuous on $A, B$ respectively with $f|_A|_{A \cap B} = f|_B|_{A \cap B}$, the combined function $f: \mathbb{R} \to \mathbb{R}$ is **continuous on all of $\mathbb{R}$**. $\blacksquare$"""
            },
            {
                "id": "prob_3_2",
                "tier": "Advanced",
                "title": "Stereographic Projection as a Homeomorphism",
                "statement": r"""Let $S^n = \{x \in \mathbb{R}^{n+1} : \|x\|_2 = 1\}$ be the $n$-dimensional sphere, and let $N = (0, \dots, 0, 1)$ be the North Pole.
The **stereographic projection** map $\sigma: S^n \setminus \{N\} \to \mathbb{R}^n$ is defined by projecting from $N$ onto the equatorial hyperplane $x_{n+1} = 0$:
$$\sigma(x_1, \dots, x_n, x_{n+1}) = \left( \frac{x_1}{1 - x_{n+1}}, \dots, \frac{x_n}{1 - x_{n+1}} \right)$$
1. Derive the explicit formula for the inverse map $\sigma^{-1}: \mathbb{R}^n \to S^n \setminus \{N\}$.
2. Prove rigorously that $\sigma$ and $\sigma^{-1}$ are both continuous.
3. Conclude that $S^n \setminus \{N\} \cong \mathbb{R}^n$ are homeomorphic.""",
                "solution": r"""### 1. Inversion Formula

Let $y = (y_1, \dots, y_n) \in \mathbb{R}^n$. Let $\|y\|^2 = \sum_{i=1}^n y_i^2$.
The line connecting $N = (0, \dots, 0, 1)$ to $(y_1, \dots, y_n, 0)$ is parametrized by:
$$L(t) = (1 - t)N + t(y, 0) = (t y_1, \dots, t y_n, 1 - t)$$
We seek the non-trivial intersection of $L(t)$ with $S^n$:
$$\|L(t)\|^2 = t^2 \|y\|^2 + (1 - t)^2 = 1$$
$$t^2 \|y\|^2 + 1 - 2t + t^2 = 1 \implies t [ t(\|y\|^2 + 1) - 2 ] = 0$$
The root $t = 0$ corresponds to $N$. The intersection point on $S^n \setminus \{N\}$ corresponds to:
$$t = \frac{2}{\|y\|^2 + 1}$$
Substituting this $t$ into $L(t)$:
$$\sigma^{-1}(y) = \left( \frac{2 y_1}{\|y\|^2 + 1}, \dots, \frac{2 y_n}{\|y\|^2 + 1}, \frac{\|y\|^2 - 1}{\|y\|^2 + 1} \right)$$

---

### 2. Continuity of $\sigma$ and $\sigma^{-1}$

- **Continuity of $\sigma$:**
  Each component function $\sigma_i(x) = \frac{x_i}{1 - x_{n+1}}$ is a rational function of the coordinates $(x_1, \dots, x_{n+1})$.
  On the domain $S^n \setminus \{N\}$, $x_{n+1} < 1$, so the denominator $1 - x_{n+1} > 0$ never vanishes!
  Since rational functions with non-zero denominators are continuous, each component $\sigma_i$ is continuous.
  Hence $\sigma$ is continuous.
- **Continuity of $\sigma^{-1}$:**
  Each component function of $\sigma^{-1}(y)$ has denominator $\|y\|^2 + 1 \ge 1 > 0$, which is non-zero everywhere on $\mathbb{R}^n$.
  Hence all component functions are rational functions with non-vanishing denominators, proving $\sigma^{-1}$ is continuous on $\mathbb{R}^n$.

---

### 3. Conclusion

Since $\sigma \circ \sigma^{-1} = \operatorname{id}_{\mathbb{R}^n}$ and $\sigma^{-1} \circ \sigma = \operatorname{id}_{S^n \setminus \{N\}}$, $\sigma$ is a continuous bijection with a continuous inverse.
Therefore, $\sigma: S^n \setminus \{N\} \to \mathbb{R}^n$ is a **homeomorphism**:
$$S^n \setminus \{N\} \cong \mathbb{R}^n \quad \blacksquare$$"""
            },
            {
                "id": "prob_3_3",
                "tier": "Honors / Proof Challenge",
                "title": "Universal Property & Quotient Homeomorphism $I^2 / \sim \; \cong S^1 \times S^1$",
                "statement": r"""Let $I^2 = [0, 1] \times [0, 1]$ equipped with the standard topology.
Let $\sim$ be the equivalence relation on $I^2$ identifying opposite sides:
$$(0, y) \sim (1, y) \quad \text{and} \quad (x, 0) \sim (x, 1), \qquad \forall x, y \in [0, 1]$$
Let $q: I^2 \to I^2 / \sim$ be the canonical quotient projection.
Consider the map $F: I^2 \to S^1 \times S^1 \subset \mathbb{C}^2$ defined by:
$$F(x, y) = \left( e^{2\pi i x}, e^{2\pi i y} \right)$$
1. Prove that $F$ is continuous and constant on the equivalence classes of $\sim$.
2. By the Universal Mapping Property of quotient spaces, show there exists a unique continuous bijection $\bar{F}: I^2 / \sim \; \to S^1 \times S^1$.
3. Prove that $\bar{F}$ is a **homeomorphism**, using the fact that $I^2 / \sim$ is compact and $S^1 \times S^1$ is Hausdorff.""",
                "solution": r"""### 1. Continuity and Invariance of $F$

The map $F: I^2 \to S^1 \times S^1$ has coordinate functions:
$$F_1(x, y) = e^{2\pi i x} = \cos(2\pi x) + i \sin(2\pi x)$$
$$F_2(x, y) = e^{2\pi i y} = \cos(2\pi y) + i \sin(2\pi y)$$
Both component functions are standard trigonometric continuous maps, so $F$ is continuous.

Now verify invariance on equivalence classes:
- For $(0, y)$ and $(1, y)$:
  $$F(0, y) = (e^0, e^{2\pi i y}) = (1, e^{2\pi i y})$$
  $$F(1, y) = (e^{2\pi i}, e^{2\pi i y}) = (1, e^{2\pi i y})$$
  Thus $F(0, y) = F(1, y)$.
- For $(x, 0)$ and $(x, 1)$:
  $$F(x, 0) = (e^{2\pi i x}, 1) = F(x, 1)$$
- For the four corner points $(0,0), (1,0), (0,1), (1,1)$, all evaluate to $(1, 1)$.

Thus, $(x_1, y_1) \sim (x_2, y_2) \implies F(x_1, y_1) = F(x_2, y_2)$.
$F$ is constant on all equivalence classes!

---

### 2. Induced Continuous Map $\bar{F}$

By the Universal Property of Quotient Topologies (Theorem 3.4):
Since $q: I^2 \to I^2 / \sim$ is a quotient map and $F: I^2 \to S^1 \times S^1$ is continuous with $F$ constant on fibres of $q$, there exists a **unique continuous map**:
$$\bar{F}: I^2 / \sim \; \to S^1 \times S^1$$
satisfying $\bar{F} \circ q = F$, defined by $\bar{F}([x, y]) = F(x, y)$.

**Injectivity of $\bar{F}$:**
Suppose $\bar{F}([x_1, y_1]) = \bar{F}([x_2, y_2])$.
Then $e^{2\pi i x_1} = e^{2\pi i x_2} \implies x_1 - x_2 \in \mathbb{Z}$.
Since $x_1, x_2 \in [0, 1]$, this implies either $x_1 = x_2$, or $\{x_1, x_2\} = \{0, 1\}$.
Similarly, $e^{2\pi i y_1} = e^{2\pi i y_2} \implies y_1 = y_2$ or $\{y_1, y_2\} = \{0, 1\}$.
In all cases, $(x_1, y_1) \sim (x_2, y_2)$, so $[x_1, y_1] = [x_2, y_2]$.
Thus $\bar{F}$ is **injective**.

**Surjectivity of $\bar{F}$:**
For any $(e^{i\theta}, e^{i\phi}) \in S^1 \times S^1$, choosing $x = \frac{\theta \pmod{2\pi}}{2\pi} \in [0, 1)$ and $y = \frac{\phi \pmod{2\pi}}{2\pi} \in [0, 1)$, we have $F(x, y) = (e^{i\theta}, e^{i\phi})$.
Thus $\bar{F}$ is **surjective**.

Hence $\bar{F}$ is a continuous bijection.

---

### 3. Proof that $\bar{F}$ is a Homeomorphism

- The unit square $I^2 = [0, 1] \times [0, 1]$ is closed and bounded in $\mathbb{R}^2$, hence **compact** by the Heine-Borel theorem.
- The canonical quotient map $q: I^2 \to I^2 / \sim$ is surjective and continuous.
  The continuous image of a compact space is compact; therefore, the quotient space $I^2 / \sim$ is **compact**.
- The torus $S^1 \times S^1 \subset \mathbb{C}^2 \cong \mathbb{R}^4$ is a subspace of Euclidean space, hence it is **Hausdorff** ($T_2$).

Now we apply the classical topological theorem:
> **Theorem:** Any continuous bijection from a compact space to a Hausdorff space is a **homeomorphism**!

Since $\bar{F}: I^2 / \sim \; \to S^1 \times S^1$ is a continuous bijection from a compact space to a Hausdorff space, its inverse $\bar{F}^{-1}$ is automatically continuous.
Therefore, $\bar{F}$ is a **homeomorphism**:
$$I^2 / \sim \; \cong S^1 \times S^1 = T^2 \quad \blacksquare$$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u3 = get_unit3()
    print(f"Loaded Unit 3: {u3['title']} with {len(u3['sections'])} sections and {len(u3['problems'])} problems.")
