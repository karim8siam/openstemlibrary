# -*- coding: utf-8 -*-
"""
build_top_unit8.py
Constructs Unit 8: Connectedness, Path-Connectedness & Components
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Connectedness, Path-Connectedness & Components",
        "leadSummary": "Global topological cohesion: connected spaces, separations and clopen sets, continuous image preservation and the Intermediate Value Theorem, connected components and quasi-components, closure preservation ($C \\subseteq A \\subseteq \\bar{C}$), path-connectedness and arc-connectedness, the Topologist's Sine Curve (connected but not path-connected), locally connected and locally path-connected spaces, and preservation of connectedness under arbitrary Cartesian products.",
        "simulations": ["sim_top_connected_sine_curve"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Connected Spaces, Separations & The Intermediate Value Theorem",
                "content": r"""### 1. Connected Spaces and Separations

Connectedness formalizes the geometric property of a space consisting of a single indivisible piece.

> **Definition 8.1 (Connected Space & Separation):**
> Let $(X, \mathcal{T})$ be a topological space.
> 1. A **separation** of $X$ is a pair of non-empty disjoint open subsets $U, V \subseteq X$ such that:
>    $$U \cup V = X, \qquad U \ne \emptyset, \quad V \ne \emptyset, \qquad U \cap V = \emptyset$$
> 2. The space $X$ is called **connected** if there exists **no separation** of $X$.
> 3. Equivalently, $X$ is connected if and only if the only **clopen subsets** (subsets that are simultaneously open and closed) are $\emptyset$ and $X$.

---

### 2. Preservation Under Continuous Maps

> **Theorem 8.1 (Continuous Images of Connected Spaces are Connected):**
> Let $f: X \to Y$ be a continuous map. If $X$ is connected, then the image $f(X)$ is a **connected subspace** of $Y$.

> **Proof:**
> Suppose for contradiction that $f(X)$ is not connected.
> Then there exists a separation of $f(X)$ into two non-empty disjoint open sets in the subspace topology:
> $$f(X) = U \cup V, \qquad U \ne \emptyset, \quad V \ne \emptyset, \qquad U \cap V = \emptyset$$
> Since $f: X \to f(X)$ is continuous, the preimages $f^{-1}(U)$ and $f^{-1}(V)$ are open in $X$.
> - Since $U, V \ne \emptyset$, their preimages are non-empty: $f^{-1}(U) \ne \emptyset$ and $f^{-1}(V) \ne \emptyset$.
> - $f^{-1}(U) \cap f^{-1}(V) = f^{-1}(U \cap V) = f^{-1}(\emptyset) = \emptyset$.
> - $f^{-1}(U) \cup f^{-1}(V) = f^{-1}(U \cup V) = f^{-1}(f(X)) = X$.
> Thus $f^{-1}(U)$ and $f^{-1}(V)$ form a separation of $X$!
> This contradicts the hypothesis that $X$ is connected.
> Therefore, $f(X)$ must be connected. $\blacksquare$

---

### 3. Connected Subsets of $\mathbb{R}$ & The Intermediate Value Theorem

> **Theorem 8.2 (Connected Subsets of the Real Line):**
> A subset $S \subseteq \mathbb{R}$ is connected if and only if $S$ is an **interval** (open, closed, half-open, rays, or $\mathbb{R}$).

> **Theorem 8.3 (Topological Intermediate Value Theorem):**
> Let $X$ be a connected topological space and let $f: X \to \mathbb{R}$ be a continuous function.
> If $a, b \in X$ and $r \in \mathbb{R}$ is any value between $f(a)$ and $f(b)$ ($f(a) \le r \le f(b)$), then there exists a point $c \in X$ such that:
> $$f(c) = r$$

> **Proof:**
> By Theorem 8.1, the image $f(X)$ is a connected subset of $\mathbb{R}$.
> By Theorem 8.2, $f(X)$ is an interval.
> Since $f(a), f(b) \in f(X)$ and $r$ lies between $f(a)$ and $f(b)$, $r \in f(X)$.
> Hence there exists $c \in X$ such that $f(c) = r$. $\blacksquare$"""
            },
            {
                "secNumber": "8.2",
                "title": "Connected Components, Closures & Partitions",
                "content": r"""### 1. Connected Components

When a space is not connected, it decomposes uniquely into maximal connected pieces.

> **Definition 8.2 (Connected Component):**
> Let $X$ be a topological space. For any point $x \in X$, the **connected component** of $x$, denoted $C(x)$, is the **union of all connected subsets of $X$ containing $x$**:
> $$C(x) = \bigcup \{S \subseteq X : x \in S \text{ and } S \text{ is connected}\}$$

> **Theorem 8.4 (Properties of Connected Components):**
> 1. Each component $C(x)$ is **connected**.
> 2. The components of $X$ form a **partition** of $X$ into mutually disjoint equivalence classes under the relation $x \sim y \iff \exists \text{ connected } S \ni x, y$.
> 3. Each connected component is a **closed subset** of $X$.

---

### 2. Closures of Connected Sets

> **Theorem 8.5 (Intermediate Sets are Connected):**
> If $C \subseteq X$ is a connected subset of $X$, and $A \subseteq X$ satisfies:
> $$C \subseteq A \subseteq \operatorname{cl}(C)$$
> then $A$ is **connected**.
> In particular, the closure $\operatorname{cl}(C)$ of a connected set is always connected.

> **Proof:**
> Suppose for contradiction that $A$ is not connected.
> Then there exists a separation of $A$: $A = U \cup V$ with $U, V$ open in $A$, non-empty, and disjoint.
> Since $C \subseteq A$, $C = (C \cap U) \cup (C \cap V)$.
> Since $C$ is connected, one of these pieces must be empty, say $C \cap V = \emptyset$.
> Then $C \subseteq U$.
> Taking the closure in $A$:
> $$A = \operatorname{cl}_A(C) \subseteq \operatorname{cl}_A(U)$$
> But $V$ is open in $A$ and disjoint from $U$, so $V \cap \operatorname{cl}_A(U) = \emptyset$.
> Since $V \subseteq A \subseteq \operatorname{cl}_A(U)$, this forces $V = \emptyset$, contradicting $V \ne \emptyset$!
> Thus $A$ is connected. $\blacksquare$"""
            },
            {
                "secNumber": "8.3",
                "title": "Path-Connectedness & Arc-Connectedness",
                "content": r"""### 1. Paths and Path-Connected Spaces

A stronger, more intuitive geometric form of connectedness is the ability to travel between points along a continuous curve.

> **Definition 8.3 (Path & Path-Connected Space):**
> 1. A **path** in a topological space $X$ from a point $x$ to a point $y$ is a **continuous function**:
>    $$\gamma: [0, 1] \to X \qquad \text{such that} \quad \gamma(0) = x \quad \text{and} \quad \gamma(1) = y$$
> 2. A space $X$ is called **path-connected** if for every pair of points $x, y \in X$, there exists a path in $X$ connecting $x$ to $y$.

---

### 2. Path-Connected Implies Connected

> **Theorem 8.6:**
> Every **path-connected space** is **connected**.

> **Proof:**
> Suppose $X$ is path-connected. Fix a base point $x_0 \in X$.
> For every point $x \in X$, there exists a continuous path $\gamma_x: [0, 1] \to X$ with $\gamma_x(0) = x_0$ and $\gamma_x(1) = x$.
> The image $P_x = \gamma_x([0, 1])$ is the continuous image of the connected interval $[0, 1]$, so $P_x$ is a connected subset of $X$ containing $x_0$.
> The whole space $X$ is the union of all these paths:
> $$X = \bigcup_{x \in X} P_x$$
> Since each $P_x$ is connected and all share the common point $x_0 \in \bigcap_{x \in X} P_x$, their union $X$ is **connected**. $\blacksquare$

The converse of Theorem 8.6 is **FALSE**: a connected space is not necessarily path-connected!"""
            },
            {
                "secNumber": "8.4",
                "title": "The Topologist's Sine Curve Counterexample",
                "content": r"""### 1. Definition of the Topologist's Sine Curve

The classic counterexample separating connectedness from path-connectedness.

> **Definition 8.4 (Topologist's Sine Curve):**
> In $\mathbb{R}^2$, consider the graph of $\sin(1/x)$ on $(0, 1]$:
> $$S = \left\{ \left(x, \sin \frac{1}{x}\right) \in \mathbb{R}^2 : 0 < x \le 1 \right\}$$
> The **Topologist's Sine Curve** is the closure of $S$ in $\mathbb{R}^2$:
> $$\bar{S} = S \cup L, \qquad \text{where } L = \{0\} \times [-1, 1]$$
> is the vertical limit segment on the $y$-axis.

---

### 2. Proof that $\bar{S}$ is Connected but Not Path-Connected

> **Theorem 8.7 (Properties of the Topologist's Sine Curve):**
> 1. $\bar{S}$ is **connected**.
> 2. $\bar{S}$ is **NOT path-connected**.

> **Proof:**
> 1. **Connectedness:**
>    The mapping $x \mapsto (x, \sin(1/x))$ is continuous on the interval $(0, 1]$.
>    Since $(0, 1]$ is connected, its image $S$ is connected.
>    By Theorem 8.5, the closure of any connected set is connected:
>    $$\bar{S} = \operatorname{cl}(S) \text{ is connected!}$$
>
> 2. **Failure of Path-Connectedness:**
>    Suppose for contradiction that there exists a continuous path $\gamma: [0, 1] \to \bar{S}$ with:
>    $$\gamma(0) = (0, 0) \in L \quad \text{and} \quad \gamma(1) = \left(\frac{1}{\pi}, 0\right) \in S$$
>    Let $t_0 = \sup \{t \in [0, 1] : \gamma(t) \in L\}$.
>    Since $L$ is closed, $\gamma(t_0) \in L$.
>    For all $t > t_0$, $\gamma(t) \in S$.
>    Writing $\gamma(t) = (x(t), y(t))$:
>    As $t \to t_0^+$, $x(t) \to 0^+$.
>    Since $y(t) = \sin(1/x(t))$ oscillates infinitely often between $-1$ and $+1$ as $x \to 0^+$, the limit $\lim_{t \to t_0^+} y(t)$ **cannot exist**!
>    This contradicts the continuity of $\gamma$ at $t_0$.
>    Therefore, no continuous path can bridge $L$ and $S$.
>    Hence $\bar{S}$ is **not path-connected**. $\blacksquare$"""
            },
            {
                "secNumber": "8.5",
                "title": "Local Connectedness & Product Invariance",
                "content": r"""### 1. Locally Connected and Locally Path-Connected Spaces

> **Definition 8.5 (Locally Connected & Locally Path-Connected):**
> 1. A topological space $X$ is **locally connected** if every point has a local basis consisting of **connected open sets**.
> 2. A topological space $X$ is **locally path-connected** if every point has a local basis consisting of **path-connected open sets**.

> **Theorem 8.8 (Equivalence for Locally Path-Connected Spaces):**
> If $X$ is **locally path-connected**, then:
> $$X \text{ is connected} \iff X \text{ is path-connected}$$
> In particular, every topological manifold (which is locally Euclidean) is connected if and only if it is path-connected!

---

### 2. Product Invariance of Connectedness

> **Theorem 8.9 (Products of Connected Spaces are Connected):**
> Let $\{X_\alpha\}_{\alpha \in I}$ be an arbitrary non-empty family of **connected topological spaces**.
> Then the product space:
> $$X = \prod_{\alpha \in I} X_\alpha$$
> equipped with the product topology is **connected**.

> **Proof:**
> 1. For finite products: $X_1 \times X_2$ is covered by horizontal and vertical cross-sections $X_1 \times \{y\}$ and $\{x\} \times X_2$, which are each connected and intersect, proving $X_1 \times X_2$ is connected.
> 2. For arbitrary products: fix a base point $b = (b_\alpha) \in X$.
>    For each finite subset $J \subseteq I$, let $X_J = \{x \in X : x_\alpha = b_\alpha \text{ for all } \alpha \notin J\}$.
>    $X_J \cong \prod_{\alpha \in J} X_\alpha$ is connected, and all $X_J$ contain $b$.
>    The union $Y = \bigcup_{J \subseteq I \text{ finite}} X_J$ is connected.
>    By definition of the product topology, $Y$ is **dense** in $X$: $\bar{Y} = X$.
>    By Theorem 8.5, $X = \bar{Y}$ is **connected**. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "prob_8_1",
                "tier": "Foundational",
                "title": "Continuous Images and The Fixed Point Intermediate Value Theorem",
                "statement": r"""1. Let $X$ be a connected topological space and let $f: X \to Y$ be a continuous surjective map. Prove that $Y$ is connected.
2. Let $f: [0, 1] \to [0, 1]$ be a continuous function. Using connectedness of $[0, 1]$, prove that $f$ has a **fixed point**: there exists $c \in [0, 1]$ such that $f(c) = c$.""",
                "solution": r"""### 1. Surjective Continuous Images are Connected

Suppose for contradiction that $Y$ is not connected.
Then there exists a separation of $Y$ into two non-empty, disjoint open sets $U$ and $V$:
$$Y = U \cup V, \qquad U \ne \emptyset, \quad V \ne \emptyset, \qquad U \cap V = \emptyset$$
Consider their preimages under $f$:
$$A = f^{-1}(U) \quad \text{and} \quad B = f^{-1}(V)$$
- Since $f$ is continuous and $U, V$ are open in $Y$, $A$ and $B$ are **open in $X$**.
- Since $f$ is surjective and $U, V$ are non-empty, their preimages are non-empty: $A \ne \emptyset$ and $B \ne \emptyset$.
- Disjointness: $A \cap B = f^{-1}(U) \cap f^{-1}(V) = f^{-1}(U \cap V) = f^{-1}(\emptyset) = \emptyset$.
- Union: $A \cup B = f^{-1}(U) \cup f^{-1}(V) = f^{-1}(U \cup V) = f^{-1}(Y) = X$.
Therefore, $A$ and $B$ form a separation of $X$, which contradicts the hypothesis that $X$ is connected!
Thus $Y$ must be connected.

---

### 2. Fixed Point on the Unit Interval

Define the auxiliary function $g: [0, 1] \to \mathbb{R}$ by:
$$g(x) = f(x) - x$$
- Since $f$ and $x \mapsto x$ are continuous, $g$ is continuous on $[0, 1]$.
- Evaluate $g$ at the endpoints:
  - At $x = 0$: $g(0) = f(0) - 0 = f(0) \ge 0$ (since $f([0, 1]) \subseteq [0, 1]$).
  - At $x = 1$: $g(1) = f(1) - 1 \le 0$ (since $f([0, 1]) \subseteq [0, 1]$).
- If $g(0) = 0$, then $f(0) = 0$, so $c = 0$ is a fixed point.
- If $g(1) = 0$, then $f(1) = 1$, so $c = 1$ is a fixed point.
- Otherwise, $g(0) > 0$ and $g(1) < 0$.
  The domain $[0, 1]$ is a connected interval.
  By the Intermediate Value Theorem (Theorem 8.3), since $0$ lies between $g(1) < 0$ and $g(0) > 0$, there exists $c \in (0, 1)$ such that:
  $$g(c) = 0 \implies f(c) - c = 0 \implies f(c) = c$$
Thus, $f$ has a fixed point $c \in [0, 1]$. $\blacksquare$"""
            },
            {
                "id": "prob_8_2",
                "tier": "Advanced",
                "title": "Disconnection of the Topologist's Sine Curve under Paths",
                "statement": r"""Consider the Topologist's Sine Curve $\bar{S} = S \cup L \subset \mathbb{R}^2$ where:
$$S = \left\{\left(x, \sin \frac{1}{x}\right) : x \in (0, 1]\right\}, \qquad L = \{0\} \times [-1, 1]$$
Prove rigorously that no continuous path $\gamma: [0, 1] \to \bar{S}$ can connect the origin $(0, 0) \in L$ to the point $(1/\pi, 0) \in S$.""",
                "solution": r"""### 1. Setup and Extremal Time Parameter

Suppose for contradiction that there exists a continuous path $\gamma: [0, 1] \to \bar{S}$ such that:
$$\gamma(0) = (0, 0) \in L \quad \text{and} \quad \gamma(1) = (1/\pi, 0) \in S$$
Write the path in components: $\gamma(t) = (x(t), y(t))$ for $t \in [0, 1]$.
Define the set of times when the path visits the vertical line $L$:
$$T_L = \{t \in [0, 1] : \gamma(t) \in L\} = \{t \in [0, 1] : x(t) = 0\}$$
- Since $x: [0, 1] \to \mathbb{R}$ is continuous, $T_L = x^{-1}(\{0\})$ is a **closed subset** of $[0, 1]$.
- Since $0 \in T_L$, $T_L$ is non-empty.
- Since $1 \notin T_L$ (as $x(1) = 1/\pi > 0$), $T_L \subseteq [0, 1)$.

Define the supremum:
$$t_0 = \sup T_L$$
Since $T_L$ is closed, $t_0 \in T_L$, so $x(t_0) = 0$ and $\gamma(t_0) \in L$.
Moreover, $t_0 < 1$.

---

### 2. Behavior for $t > t_0$

By definition of the supremum, for all $t \in (t_0, 1]$, we have $t \notin T_L$, which means:
$$x(t) > 0 \implies \gamma(t) \in S$$
On $S$, the coordinates satisfy the exact equation:
$$y(t) = \sin \left(\frac{1}{x(t)}\right), \qquad \forall t \in (t_0, 1]$$

---

### 3. Producing the Discontinuity Contradiction

By continuity of the path $\gamma$ at $t_0$, as $t \to t_0^+$, we must have:
$$\lim_{t \to t_0^+} x(t) = x(t_0) = 0$$
$$\lim_{t \to t_0^+} y(t) = y(t_0)$$
Since $x(t)$ is continuous and $x(t) > 0$ for $t \in (t_0, 1]$ with $x(t_0) = 0$, by the Intermediate Value Theorem, $x(t)$ takes all values in $(0, \varepsilon)$ for sufficiently small $t - t_0 > 0$.

For each positive integer $n \in \mathbb{N}$ large enough:
- Choose $u_n = \frac{1}{\frac{\pi}{2} + 2\pi n} \to 0$, where $\sin(1/u_n) = 1$.
- Choose $v_n = \frac{1}{\frac{3\pi}{2} + 2\pi n} \to 0$, where $\sin(1/v_n) = -1$.
By the Intermediate Value Theorem for $x(t)$, there exist sequences of times $t_n, t'_n \in (t_0, 1]$ converging to $t_0$ such that:
$$x(t_n) = u_n \implies y(t_n) = \sin\left(\frac{1}{u_n}\right) = 1$$
$$x(t'_n) = v_n \implies y(t'_n) = \sin\left(\frac{1}{v_n}\right) = -1$$
As $n \to \infty$, both $t_n \to t_0$ and $t'_n \to t_0$.
However:
$$\lim_{n \to \infty} y(t_n) = 1 \ne -1 = \lim_{n \to \infty} y(t'_n)$$
This proves that the limit $\lim_{t \to t_0^+} y(t)$ **DOES NOT EXIST**!
This directly contradicts the continuity of $y(t)$ at $t_0$.

---

### 4. Conclusion

Therefore, no continuous path connecting $(0, 0)$ to $(1/\pi, 0)$ can exist in $\bar{S}$.
Hence, $\bar{S}$ is **not path-connected**. $\blacksquare$"""
            },
            {
                "id": "prob_8_3",
                "tier": "Honors / Proof Challenge",
                "title": "Complete Proof of Connectedness of Arbitrary Cartesian Products",
                "statement": r"""Prove with full mathematical rigor that if $\{X_\alpha\}_{\alpha \in I}$ is an arbitrary non-empty family of connected topological spaces, then the product space:
$$X = \prod_{\alpha \in I} X_\alpha$$
equipped with the product topology is **connected**:

1. Prove that the product of two connected spaces $X_1 \times X_2$ is connected.
2. By induction, establish that any finite product $\prod_{k=1}^n X_k$ is connected.
3. Fix a base point $b = (b_\alpha) \in X$, and define $X_J = \{x \in X : x_\alpha = b_\alpha \text{ for all } \alpha \notin J\}$ for finite $J \subset I$. Prove that $X_J$ is connected.
4. Prove that $Y = \bigcup_{J \subset I \text{ finite}} X_J$ is connected and **dense** in $X$.
5. Deduce by closure preservation that $X = \bar{Y}$ is connected.""",
                "solution": r"""### 1. Step 1: Product of Two Connected Spaces

Let $X_1$ and $X_2$ be connected spaces.
Fix a point $x_0 \in X_1$ and $y_0 \in X_2$.
For any $(x, y) \in X_1 \times X_2$, define the slice set:
$$T_x = (X_1 \times \{y_0\}) \cup (\{x\} \times X_2)$$
- The slice $X_1 \times \{y_0\}$ is homeomorphic to $X_1$, hence connected.
- The slice $\{x\} \times X_2$ is homeomorphic to $X_2$, hence connected.
- Both slices intersect at the point $(x, y_0)$.
Since the union of two connected sets sharing a common point is connected, $T_x$ is a **connected subset** of $X_1 \times X_2$.
Now consider the union over all $x \in X_1$:
$$X_1 \times X_2 = \bigcup_{x \in X_1} T_x$$
Each $T_x$ contains the common point $(x_0, y_0) \in X_1 \times \{y_0\}$.
Since $\{T_x\}_{x \in X_1}$ is a family of connected subsets sharing the common point $(x_0, y_0)$, their union $X_1 \times X_2$ is **connected**.

---

### 2. Step 2: Finite Products

By mathematical induction on $n$, for any $n \in \mathbb{N}$, if $X_1, \dots, X_n$ are connected, then $\prod_{k=1}^n X_k \cong \left(\prod_{k=1}^{n-1} X_k\right) \times X_n$ is connected.

---

### 3. Step 3: Subspaces with Finitely Many Non-Base Coordinates

Let $I$ be an arbitrary index set, and let $X = \prod_{\alpha \in I} X_\alpha$.
Fix an arbitrary point $b = (b_\alpha)_{\alpha \in I} \in X$.
For each finite subset $J \subseteq I$, define:
$$X_J = \{x \in X : x_\alpha = b_\alpha \text{ for all } \alpha \in I \setminus J\}$$
The subspace $X_J$ is canonically homeomorphic to the finite product $\prod_{\alpha \in J} X_\alpha$.
By Step 2, each $X_J$ is **connected**.
Moreover, the base point $b$ belongs to $X_J$ for every finite $J$.

---

### 4. Step 4: Union $Y$ is Connected and Dense

Define:
$$Y = \bigcup_{\substack{J \subseteq I \\ J \text{ finite}}} X_J$$
Since each $X_J$ is connected and $b \in \bigcap_{J} X_J$, the union $Y$ is a **connected subset of $X$**.

Now we show that $Y$ is **dense in $X$**:
Let $U \subseteq X$ be any non-empty basic open set in the product topology.
By Definition 3.6, $U$ has the form:
$$U = \prod_{\alpha \in I} U_\alpha$$
where each $U_\alpha$ is open in $X_\alpha$, and there exists a **finite subset** $K \subseteq I$ such that $U_\alpha = X_\alpha$ for all $\alpha \in I \setminus K$.
For each $\alpha \in K$, choose a point $x_\alpha \in U_\alpha$ (which is non-empty).
For $\alpha \notin K$, set $x_\alpha = b_\alpha$.
Consider the point $x^* = (x_\alpha)_{\alpha \in I}$.
- By definition of $x^*$, $x^*_\alpha = b_\alpha$ for all $\alpha \notin K$. Since $K$ is finite, $x^* \in X_K \subseteq Y$.
- By definition of $x^*$, for $\alpha \in K$, $x^*_\alpha \in U_\alpha$, and for $\alpha \notin K$, $x^*_\alpha = b_\alpha \in X_\alpha = U_\alpha$. Thus $x^* \in U$.
Therefore:
$$x^* \in Y \cap U \implies Y \cap U \ne \emptyset$$
Since $Y$ intersects every non-empty basic open set, $Y$ is **dense in $X$**:
$$\operatorname{cl}(Y) = X$$

---

### 5. Step 5: Conclusion via Closure Preservation

By Theorem 8.5 (Intermediate sets are connected):
Since $Y$ is connected and $Y \subseteq X = \operatorname{cl}(Y)$, the closure $X$ must be **connected**.
Therefore, the arbitrary Cartesian product $\prod_{\alpha \in I} X_\alpha$ is **connected** in the product topology. $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u8 = get_unit8()
    print(f"Loaded Unit 8: {u8['title']} with {len(u8['sections'])} sections and {len(u8['problems'])} problems.")
