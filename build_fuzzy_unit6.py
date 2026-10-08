# -*- coding: utf-8 -*-
"""
build_fuzzy_unit6.py
Constructs Unit 6: Fuzzy Relations, Similarity & Compatibility
Strictly ZERO course numbers.
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Fuzzy Relations, Similarity & Compatibility",
        "leadSummary": "Comprehensive mathematical theory of fuzzy relations on Cartesian products X × Y: fuzzy relation matrices, domain, range, height, and inverse relations R^{-1}, Max-Min (sup-min) and Max-Product (sup-product) compositions, properties of associativity and distributivity, fuzzy equivalence and similarity relations (reflexivity, symmetry, max-min transitivity), the algorithm for computing transitive closures R_T = R ∪ R^2 ∪ ... ∪ R^{n-1}, compatibility (tolerance) relations, α-compatibility classes, and similarity quotient partitions.",
        "simulations": ["sim_fuzzy_relations_matrix"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Crisp vs Fuzzy Relations on Cartesian Products $X \\times Y$ & Membership Matrices",
                "content": r"""### 1. From Classical to Fuzzy Relations
A classical binary relation $R$ between two sets $X$ and $Y$ is a subset of the Cartesian product $X \times Y$: an ordered pair $(x, y)$ is either related ($(x, y) \in R$) or not ($(x, y) \notin R$).
In fuzzy set theory, associations between entities often possess intermediate strengths (e.g. *"x is much larger than y"*, *"patient x strongly exhibits symptom y"*).

> **Definition 6.1 (Fuzzy Binary Relation):**
> A **fuzzy binary relation** $R$ from universe $X$ to universe $Y$ is a fuzzy subset of the Cartesian product $X \times Y$, characterized by a bivariate membership function:
> $$\mu_R: X \times Y \to [0, 1]$$
> where $\mu_R(x, y)$ denotes the **degree of association, correlation, or relationship** between $x \in X$ and $y \in Y$.

---

### 2. The Fuzzy Relation Matrix
When $X = \{x_1, \dots, x_m\}$ and $Y = \{y_1, \dots, y_n\}$ are finite sets, a fuzzy relation $R$ is represented by an $m \times n$ **membership matrix** $M_R = (r_{ij}) \in [0, 1]^{m \times n}$:

$$M_R = \begin{pmatrix}
r_{11} & r_{12} & \dots & r_{1n} \\
r_{21} & r_{22} & \dots & r_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
r_{m1} & r_{m2} & \dots & r_{mn}
\end{pmatrix}$$
where $r_{ij} = \mu_R(x_i, y_j) \in [0, 1]$."""
            },
            {
                "secNumber": "6.2",
                "title": "Domain, Range, Height, and Inverse of Fuzzy Relations",
                "content": r"""### 1. Fundamental Geometric Metrics of Fuzzy Relations

> **Definition 6.2 (Domain, Range, and Height):**
> Let $R$ be a fuzzy relation on $X \times Y$ with membership function $\mu_R(x, y)$.
> 1. **Domain of $R$:** The fuzzy subset $\text{dom}(R)$ on $X$ defined by:
>    $$\mu_{\text{dom}(R)}(x) = \sup_{y \in Y} \mu_R(x, y)$$
> 2. **Range of $R$:** The fuzzy subset $\text{ran}(R)$ on $Y$ defined by:
>    $$\mu_{\text{ran}(R)}(y) = \sup_{x \in X} \mu_R(x, y)$$
> 3. **Height of $R$:** The supremum membership grade over the entire product space:
>    $$h(R) = \sup_{x \in X, y \in Y} \mu_R(x, y)$$
>    If $h(R) = 1$, the relation is **normal**; otherwise it is **subnormal**.

---

### 2. The Inverse Fuzzy Relation $R^{-1}$

> **Definition 6.3 (Inverse Relation):**
> The **inverse** of a fuzzy relation $R$ on $X \times Y$ is a fuzzy relation $R^{-1}$ (or $R^T$) on $Y \times X$ defined by:
> $$\mu_{R^{-1}}(y, x) = \mu_R(x, y) \quad (\forall x \in X, y \in Y)$$
> In matrix notation: $M_{R^{-1}} = (M_R)^T$ (the matrix transpose).

#### Properties of Inversion:
1. $(R^{-1})^{-1} = R$ (Involution).
2. $(R \cup S)^{-1} = R^{-1} \cup S^{-1}$.
3. $(R \cap S)^{-1} = R^{-1} \cap S^{-1}$.
4. $(R \circ S)^{-1} = S^{-1} \circ R^{-1}$ (Reversal of composition order)."""
            },
            {
                "secNumber": "6.3",
                "title": "Max-Min and Max-Product Compositions of Fuzzy Relations",
                "content": r"""### 1. Composition of Fuzzy Relations
Let $R$ be a fuzzy relation on $X \times Y$ and let $S$ be a fuzzy relation on $Y \times Z$.
We seek the composite relation $T = R \circ S$ that relates elements $x \in X$ directly to $z \in Z$ through the intermediate universe $Y$.

> **Definition 6.4 (Max-Min Composition):**
> The **Max-Min (sup-min) composition** of $R$ and $S$, denoted $R \circ S$, is a fuzzy relation on $X \times Z$ defined by:
> $$\mu_{R \circ S}(x, z) = \sup_{y \in Y} \min\left( \mu_R(x, y), \mu_S(y, z) \right)$$
> For finite sets with matrices $M_R = (r_{ik})$ and $M_S = (s_{kj})$:
> $$t_{ij} = \max_{k=1}^p \min(r_{ik}, s_{kj})$$

> **Definition 6.5 (Max-Product Composition):**
> The **Max-Product (sup-product) composition**, denoted $R \odot S$, is defined by:
> $$\mu_{R \odot S}(x, z) = \sup_{y \in Y} \left( \mu_R(x, y) \cdot \mu_S(y, z) \right)$$
> In matrix form:
> $$t_{ij} = \max_{k=1}^p (r_{ik} \cdot s_{kj})$$

---

### 2. Algebraic Properties of Composition
1. **Associativity:**
   $$(R \circ S) \circ T = R \circ (S \circ T)$$
2. **Distributivity over Union:**
   $$R \circ (S \cup T) = (R \circ S) \cup (R \circ T)$$
3. **Monotonicity:**
   $$S \subseteq T \implies R \circ S \subseteq R \circ T$$
4. **Non-Distributivity over Intersection:** In general:
   $$R \circ (S \cap T) \subseteq (R \circ S) \cap (R \circ T)$$
   (Equality holds only under strict full-rank conditions)."""
            },
            {
                "secNumber": "6.4",
                "title": "Fuzzy Equivalence and Similarity Relations, Transitive Closures",
                "content": r"""### 1. Axioms of Similarity Relations
A classical equivalence relation partitions a set into disjoint equivalence classes.
Zadeh (1971) generalized this to fuzzy sets via **similarity relations**:

> **Definition 6.6 (Fuzzy Similarity Relation):**
> A fuzzy relation $R$ on $X \times X$ is called a **similarity relation** (or fuzzy equivalence relation) if it satisfies:
> 1. **Reflexivity:** $\mu_R(x, x) = 1$ for all $x \in X$. (Diagonal entries of $M_R$ are all 1).
> 2. **Symmetry:** $\mu_R(x, y) = \mu_R(y, x)$ for all $x, y \in X$. ($M_R = M_R^T$).
> 3. **Max-Min Transitivity:** $R \circ R \subseteq R$, meaning:
>    $$\mu_R(x, z) \ge \sup_{y \in X} \min(\mu_R(x, y), \mu_R(y, z)) \quad (\forall x, z \in X)$$

---

### 2. The Transitive Closure $R_T$
If a relation $R$ is reflexive and symmetric but fails transitivity, its **transitive closure** $R_T$ (or $R^\infty$) is the smallest similarity relation containing $R$.

> **Theorem 6.1 (Algorithm for Transitive Closure):**
> Let $R$ be a reflexive and symmetric fuzzy relation on a finite set $X$ with $|X| = n$.
> The powers under max-min composition satisfy the monotonic inclusion chain:
> $$R \subseteq R^2 \subseteq R^3 \subseteq \dots \subseteq R^k \subseteq R^{k+1} \dots$$
> There exists a finite integer $k \le n - 1$ such that:
> $$R^k = R^{k+1} = R^{k+2} = \dots = R_T$$
> The relation $R_T = R^{n-1}$ is guaranteed to be max-min transitive!"""
            },
            {
                "secNumber": "6.5",
                "title": "Compatibility (Tolerance) Relations, $\\alpha$-Compatibility Classes and Partitions",
                "content": r"""### 1. Compatibility (Tolerance) Relations
In many practical domains (psychology, clustering, image segmentation), similarity cannot satisfy transitivity.
*(E.g.: A is similar to B, B is similar to C, but A is completely dissimilar to C).*

> **Definition 6.7 (Compatibility Relation):**
> A fuzzy relation $R$ on $X \times X$ is called a **compatibility (or tolerance) relation** if it is:
> 1. **Reflexive:** $\mu_R(x, x) = 1$.
> 2. **Symmetric:** $\mu_R(x, y) = \mu_R(y, x)$.
> (Transitivity is NOT required).

---

### 2. $\alpha$-Cuts of Similarity Relations and Quotients

> **Theorem 6.2 (Partitions via Similarity $\alpha$-Cuts):**
> Let $R$ be a similarity relation on $X$. For every $\alpha \in (0, 1]$, the crisp $\alpha$-cut $R_\alpha$ is a **classical crisp equivalence relation** on $X$.
> Therefore, $R_\alpha$ induces a true partition of $X$ into disjoint equivalence classes:
> $$X / R_\alpha = \{ [x]_\alpha \mid x \in X \}$$
> As $\alpha$ increases from 0 to 1, the partitions form a **nested hierarchical tree of clusters** (dendrogram)!"""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 6.1: Max-Min and Max-Product Composition of $3 \\times 3$ Fuzzy Relation Matrices",
                "statement": r"""Consider two fuzzy relations $R$ and $S$ on $X \times X$ where $X = \{x_1, x_2, x_3\}$, defined by the membership matrices:
$$M_R = \begin{pmatrix} 0.6 & 0.8 & 0.3 \\ 0.2 & 0.7 & 0.9 \\ 0.5 & 0.4 & 0.1 \end{pmatrix}, \qquad M_S = \begin{pmatrix} 0.4 & 0.5 & 0.7 \\ 0.9 & 0.2 & 0.6 \\ 0.3 & 0.8 & 0.1 \end{pmatrix}$$

1. Compute the Max-Min composition matrix $M_{R \circ S}$.
2. Compute the Max-Product composition matrix $M_{R \odot S}$.
3. Verify that $M_{R \odot S} \le M_{R \circ S}$ entrywise.""",
                "hints": [
                    "For entry $(i, j)$: $t_{ij} = \\max_k \\min(r_{ik}, s_{kj})$.",
                    "For max-product: $p_{ij} = \\max_k (r_{ik} \\cdot s_{kj})$.",
                    "Recall $a \\cdot b \\le \\min(a, b)$ for all $a, b \\in [0, 1]$."
                ],
                "solution": r"""### 1. Max-Min Composition $M_{R \circ S}$
$$t_{ij} = \max_k \min(r_{ik}, s_{kj}) = \max( \min(r_{i1}, s_{1j}), \min(r_{i2}, s_{2j}), \min(r_{i3}, s_{3j}) )$$

- **Row 1:**
  - $t_{11} = \max(\min(0.6, 0.4), \min(0.8, 0.9), \min(0.3, 0.3)) = \max(0.4, 0.8, 0.3) = 0.8$
  - $t_{12} = \max(\min(0.6, 0.5), \min(0.8, 0.2), \min(0.3, 0.8)) = \max(0.5, 0.2, 0.3) = 0.5$
  - $t_{13} = \max(\min(0.6, 0.7), \min(0.8, 0.6), \min(0.3, 0.1)) = \max(0.6, 0.6, 0.1) = 0.6$
- **Row 2:**
  - $t_{21} = \max(\min(0.2, 0.4), \min(0.7, 0.9), \min(0.9, 0.3)) = \max(0.2, 0.7, 0.3) = 0.7$
  - $t_{22} = \max(\min(0.2, 0.5), \min(0.7, 0.2), \min(0.9, 0.8)) = \max(0.2, 0.2, 0.8) = 0.8$
  - $t_{23} = \max(\min(0.2, 0.7), \min(0.7, 0.6), \min(0.9, 0.1)) = \max(0.2, 0.6, 0.1) = 0.6$
- **Row 3:**
  - $t_{31} = \max(\min(0.5, 0.4), \min(0.4, 0.9), \min(0.1, 0.3)) = \max(0.4, 0.4, 0.1) = 0.4$
  - $t_{32} = \max(\min(0.5, 0.5), \min(0.4, 0.2), \min(0.1, 0.8)) = \max(0.5, 0.2, 0.1) = 0.5$
  - $t_{33} = \max(\min(0.5, 0.7), \min(0.4, 0.6), \min(0.1, 0.1)) = \max(0.5, 0.4, 0.1) = 0.5$

$$M_{R \circ S} = \begin{pmatrix} 0.8 & 0.5 & 0.6 \\ 0.7 & 0.8 & 0.6 \\ 0.4 & 0.5 & 0.5 \end{pmatrix} \qquad \blacksquare$$

---

### 2. Max-Product Composition $M_{R \odot S}$
$$p_{ij} = \max( r_{i1} s_{1j}, \; r_{i2} s_{2j}, \; r_{i3} s_{3j} )$$

- **Row 1:**
  - $p_{11} = \max(0.6 \times 0.4, 0.8 \times 0.9, 0.3 \times 0.3) = \max(0.24, 0.72, 0.09) = 0.72$
  - $p_{12} = \max(0.6 \times 0.5, 0.8 \times 0.2, 0.3 \times 0.8) = \max(0.30, 0.16, 0.24) = 0.30$
  - $p_{13} = \max(0.6 \times 0.7, 0.8 \times 0.6, 0.3 \times 0.1) = \max(0.42, 0.48, 0.03) = 0.48$
- **Row 2:**
  - $p_{21} = \max(0.2 \times 0.4, 0.7 \times 0.9, 0.9 \times 0.3) = \max(0.08, 0.63, 0.27) = 0.63$
  - $p_{22} = \max(0.2 \times 0.5, 0.7 \times 0.2, 0.9 \times 0.8) = \max(0.10, 0.14, 0.72) = 0.72$
  - $p_{23} = \max(0.2 \times 0.7, 0.7 \times 0.6, 0.9 \times 0.1) = \max(0.14, 0.42, 0.09) = 0.42$
- **Row 3:**
  - $p_{31} = \max(0.5 \times 0.4, 0.4 \times 0.9, 0.1 \times 0.3) = \max(0.20, 0.36, 0.03) = 0.36$
  - $p_{32} = \max(0.5 \times 0.5, 0.4 \times 0.2, 0.1 \times 0.8) = \max(0.25, 0.08, 0.08) = 0.25$
  - $p_{33} = \max(0.5 \times 0.7, 0.4 \times 0.6, 0.1 \times 0.1) = \max(0.35, 0.24, 0.01) = 0.35$

$$M_{R \odot S} = \begin{pmatrix} 0.72 & 0.30 & 0.48 \\ 0.63 & 0.72 & 0.42 \\ 0.36 & 0.25 & 0.35 \end{pmatrix} \qquad \blacksquare$$

---

### 3. Verification of Inequality
Comparing element by element:
$$\begin{pmatrix} 0.72 & 0.30 & 0.48 \\ 0.63 & 0.72 & 0.42 \\ 0.36 & 0.25 & 0.35 \end{pmatrix} \le \begin{pmatrix} 0.8 & 0.5 & 0.6 \\ 0.7 & 0.8 & 0.6 \\ 0.4 & 0.5 & 0.5 \end{pmatrix}$$
Since $a b \le \min(a, b)$ for all $a, b \in [0, 1]$, each term in the maximum is smaller.
Thus $M_{R \odot S} \le M_{R \circ S}$ holds strictly everywhere. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 6.2: Computation of the Transitive Closure of a Compatibility Relation",
                "statement": r"""Let $X = \{1, 2, 3, 4\}$ and let $R$ be a compatibility relation on $X$ given by the matrix:
$$M_R = \begin{pmatrix} 
1.0 & 0.7 & 0.0 & 0.3 \\ 
0.7 & 1.0 & 0.8 & 0.0 \\ 
0.0 & 0.8 & 1.0 & 0.5 \\ 
0.3 & 0.0 & 0.5 & 1.0 
\end{pmatrix}$$

1. Verify that $R$ is reflexive and symmetric.
2. Check whether $R$ is max-min transitive by evaluating $(R \circ R)_{13}$.
3. Compute the powers $R^2$ and $R^3$ under max-min composition.
4. Determine the transitive closure $R_T$ and show the stopping criterion $R^k = R^{k+1}$.
5. Find the partition classes induced by the similarity cuts $(R_T)_{0.5}$ and $(R_T)_{0.75}$.""",
                "hints": [
                    "For transitivity, check if $r_{13} \\ge \\min(r_{12}, r_{23})$.",
                    "Compute $M_{R^2} = M_R \\circ M_R$.",
                    "For partitions, group elements with relation $\\ge \\alpha$."
                ],
                "solution": r"""### 1. Reflexivity and Symmetry
- **Reflexivity:** The diagonal entries are $r_{11} = r_{22} = r_{33} = r_{44} = 1.0$. (Reflexive).
- **Symmetry:** $r_{12} = r_{21} = 0.7$, $r_{14} = r_{41} = 0.3$, $r_{23} = r_{32} = 0.8$, $r_{34} = r_{43} = 0.5$, $r_{13} = r_{31} = 0$, $r_{24} = r_{42} = 0$. (Symmetric). $\blacksquare$

---

### 2. Failure of Transitivity
Consider $x=1, y=2, z=3$:
$$r_{12} = 0.7, \qquad r_{23} = 0.8$$
$$\min(r_{12}, r_{23}) = \min(0.7, 0.8) = 0.7$$
However, $r_{13} = 0.0 < 0.7$.
Thus $R \circ R \not\subseteq R$, so $R$ is **NOT transitive**. $\blacksquare$

---

### 3. Computation of $R^2 = R \circ R$
Compute $M_{R^2}$:
- $(R^2)_{13} = \max(\min(1, 0), \min(0.7, 0.8), \min(0, 1), \min(0.3, 0.5)) = \max(0, 0.7, 0, 0.3) = 0.7$
- $(R^2)_{14} = \max(\min(1, 0.3), \min(0.7, 0), \min(0, 0.5), \min(0.3, 1)) = \max(0.3, 0, 0, 0.3) = 0.3$
- $(R^2)_{24} = \max(\min(0.7, 0.3), \min(1, 0), \min(0.8, 0.5), \min(0, 1)) = \max(0.3, 0, 0.5, 0) = 0.5$
All other entries update to:
$$M_{R^2} = \begin{pmatrix} 
1.0 & 0.7 & 0.7 & 0.3 \\ 
0.7 & 1.0 & 0.8 & 0.5 \\ 
0.7 & 0.8 & 1.0 & 0.5 \\ 
0.3 & 0.5 & 0.5 & 1.0 
\end{pmatrix}$$

---

### 4. Computation of $R^3 = R^2 \circ R$
Evaluating $M_{R^3}$:
- Entry $(1, 4)$:
  $$(R^3)_{14} = \max(\min(1, 0.3), \min(0.7, 0), \min(0.7, 0.5), \min(0.3, 1)) = \max(0.3, 0, 0.5, 0.3) = 0.5$$
All other entries remain stable:
$$M_{R^3} = \begin{pmatrix} 
1.0 & 0.7 & 0.7 & 0.5 \\ 
0.7 & 1.0 & 0.8 & 0.5 \\ 
0.7 & 0.8 & 1.0 & 0.5 \\ 
0.5 & 0.5 & 0.5 & 1.0 
\end{pmatrix}$$

Now compute $R^4 = R^3 \circ R$:
Computing all entries reveals $M_{R^4} = M_{R^3}$.
Since $R^3 = R^4$, the stopping criterion is reached at $k = 3 \le 4 - 1$.
The transitive closure is:
$$M_{R_T} = M_{R^3} = \begin{pmatrix} 
1.0 & 0.7 & 0.7 & 0.5 \\ 
0.7 & 1.0 & 0.8 & 0.5 \\ 
0.7 & 0.8 & 1.0 & 0.5 \\ 
0.5 & 0.5 & 0.5 & 1.0 
\end{pmatrix} \qquad \blacksquare$$

---

### 5. Partitions Induced by $\alpha$-Cuts of $R_T$
- **For $\alpha = 0.75$:**
  Only entries $\ge 0.75$ are connected: $r_{23} = r_{32} = 0.8 \ge 0.75$.
  Equivalence classes:
  $$\{1\}, \quad \{2, 3\}, \quad \{4\}$$
  Partition: $X / (R_T)_{0.75} = \{ \{1\}, \{2, 3\}, \{4\} \}$.
- **For $\alpha = 0.50$:**
  Every pair has relation grade $\ge 0.50$:
  All 4 elements merge into a single universal cluster:
  $$X / (R_T)_{0.50} = \{ \{1, 2, 3, 4\} \} \qquad \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 6.3: Theorem on Crisp Equivalence Cuts of Fuzzy Similarity Relations",
                "statement": r"""Let $R$ be a fuzzy similarity relation on a non-empty universe $X$.
1. Prove rigorously that for every $\alpha \in (0, 1]$, the crisp $\alpha$-cut $R_\alpha$ is a **classical crisp equivalence relation** on $X$ (reflexive, symmetric, and transitive).
2. For any two levels $\alpha_1 < \alpha_2$, prove that the partition $X / R_{\alpha_2}$ is a **refinement** of the partition $X / R_{\alpha_1}$ (i.e. every block in $X / R_{\alpha_2}$ is contained in a block of $X / R_{\alpha_1}$).
3. Show by explicit counterexample that if $R$ is only max-product transitive ($\mu_R(x, z) \ge \sup_y (\mu_R(x, y) \cdot \mu_R(y, z))$), then $R_\alpha$ is **NOT necessarily transitive** in the classical sense.""",
                "hints": [
                    "For part 1, check reflexivity $r(x, x) = 1 \\ge \\alpha$, symmetry $r(x, y) \\ge \\alpha \\implies r(y, x) \\ge \\alpha$, and transitivity using $\\min(\\alpha, \\alpha) = \\alpha$.",
                    "For part 2, use $R_{\\alpha_2} \\subseteq R_{\\alpha_1}$.",
                    "For part 3, choose $\\mu(x, y) = 0.8, \\mu(y, z) = 0.8$ with product $0.64$ and $\\alpha = 0.7$."
                ],
                "solution": r"""### 1. Proof that $R_\alpha$ is a Crisp Equivalence Relation
Let $R$ be a similarity relation on $X$ (reflexive, symmetric, max-min transitive).
Let $\alpha \in (0, 1]$. Recall:
$$(x, y) \in R_\alpha \iff \mu_R(x, y) \ge \alpha$$

#### A. Reflexivity:
Since $R$ is reflexive, $\mu_R(x, x) = 1$ for all $x \in X$.
Since $\alpha \le 1$, $\mu_R(x, x) \ge \alpha$, so $(x, x) \in R_\alpha$ for all $x \in X$.

#### B. Symmetry:
Suppose $(x, y) \in R_\alpha$. Then $\mu_R(x, y) \ge \alpha$.
By symmetry of $R$, $\mu_R(y, x) = \mu_R(x, y) \ge \alpha$.
Thus $(y, x) \in R_\alpha$.

#### C. Transitivity:
Suppose $(x, y) \in R_\alpha$ and $(y, z) \in R_\alpha$.
Then $\mu_R(x, y) \ge \alpha$ and $\mu_R(y, z) \ge \alpha$.
By max-min transitivity of $R$:
$$\mu_R(x, z) \ge \sup_{w \in X} \min(\mu_R(x, w), \mu_R(w, z)) \ge \min(\mu_R(x, y), \mu_R(y, z))$$
Substituting the inequalities:
$$\min(\mu_R(x, y), \mu_R(y, z)) \ge \min(\alpha, \alpha) = \alpha$$
Therefore:
$$\mu_R(x, z) \ge \alpha \implies (x, z) \in R_\alpha$$
Hence $R_\alpha$ is reflexive, symmetric, and transitive, meaning it is a **classical crisp equivalence relation**. $\blacksquare$

---

### 2. Proof of Nested Partition Refinement
Let $\alpha_1 < \alpha_2$.
By cut monotonicity (Theorem 3.1):
$$R_{\alpha_2} \subseteq R_{\alpha_1}$$
Let $[x]_{\alpha_2}$ be an equivalence class in $X / R_{\alpha_2}$, and let $y \in [x]_{\alpha_2}$.
Then $(x, y) \in R_{\alpha_2}$.
Since $R_{\alpha_2} \subseteq R_{\alpha_1}$, $(x, y) \in R_{\alpha_1}$, which means $y \in [x]_{\alpha_1}$.
Therefore:
$$[x]_{\alpha_2} \subseteq [x]_{\alpha_1}$$
Every equivalence class of $X / R_{\alpha_2}$ is a subset of an equivalence class of $X / R_{\alpha_1}$.
Thus, the partition at the higher threshold $\alpha_2$ is a **strict refinement** of the partition at $\alpha_1$. $\blacksquare$

---

### 3. Counterexample for Max-Product Transitivity
Suppose $R$ satisfies max-product transitivity:
$$\mu_R(x, z) \ge \sup_y (\mu_R(x, y) \cdot \mu_R(y, z))$$
Consider universe $X = \{1, 2, 3\}$ and relation:
$$\mu_R(1, 2) = 0.8, \quad \mu_R(2, 3) = 0.8, \quad \mu_R(1, 3) = 0.65$$
Check max-product transitivity for $(1, 3)$:
$$\mu_R(1, 2) \cdot \mu_R(2, 3) = 0.8 \times 0.8 = 0.64$$
Since $\mu_R(1, 3) = 0.65 \ge 0.64$, max-product transitivity is satisfied!

Now choose cut level $\alpha = 0.70$:
- $(1, 2) \in R_{0.7}$ because $\mu_R(1, 2) = 0.8 \ge 0.70$.
- $(2, 3) \in R_{0.7}$ because $\mu_R(2, 3) = 0.8 \ge 0.70$.
- However, $(1, 3) \notin R_{0.7}$ because $\mu_R(1, 3) = 0.65 < 0.70$!

Therefore:
$$(1, 2) \in R_{0.7} \text{ and } (2, 3) \in R_{0.7} \centernot\implies (1, 3) \in R_{0.7}$$
The crisp cut $R_{0.7}$ is **NOT transitive**!
This highlights that **max-min transitivity is the UNIQUE composition law that preserves classical equivalence partitions across all $\alpha$-cuts**! $\blacksquare$"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u6 = get_unit6()
    print(f"Loaded Unit 6: {u6['title']} with {len(u6['sections'])} sections and {len(u6['problems'])} problems.")
