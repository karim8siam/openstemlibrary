# -*- coding: utf-8 -*-
"""
Builder for Linear Algebra Units 3 and 4:
- Unit 3: Linear Combinations, Span, Linear Independence & Basis Dimension
- Unit 4: The Four Fundamental Matrix Subspaces & Rank-Nullity of Matrices
"""
import json

def build_unit_3():
    return {
        "id": "la-u3",
        "title": "Unit 3: Linear Combinations, Span, Linear Independence & Basis Dimension",
        "description": "Linear span, linear independence, the Linear Dependence Lemma, Wronskian determinant test, basis as minimal spanning set and maximal independent set, coordinate isomorphism, Steinitz Exchange Lemma, dimension invariance, and the Dimension Formula for Subspace Sums.",
        "sections": [
            {
                "id": "u3-sec1",
                "title": "Linear Combinations, Span & the Linear Dependence Lemma",
                "content": r"""### 1. Linear Combinations and Linear Span

Let $V$ be a vector space over a field $F$. A vector $\vec{v} \in V$ is a **linear combination** of a non-empty set of vectors $S = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k\} \subseteq V$ if there exist scalars $c_1, c_2, \dots, c_k \in F$ such that:

$$\vec{v} = c_1 \vec{v}_1 + c_2 \vec{v}_2 + \cdots + c_k \vec{v}_k = \sum_{i=1}^k c_i \vec{v}_i$$

The **Linear Span** of $S$, denoted by $\text{span}(S)$ or $\text{span}\{\vec{v}_1, \dots, \vec{v}_k\}$, is the set of all linear combinations of vectors in $S$:

$$\text{span}(S) = \left\{ \sum_{i=1}^k c_i \vec{v}_i : c_i \in F, \; k \in \mathbb{N}, \; \vec{v}_i \in S \right\}$$

By convention, the span of the empty set is the zero subspace: $\text{span}(\emptyset) = \{\vec{0}\}$.

#### Theorem 3.1 (Span is the Minimal Subspace):
Let $S$ be a non-empty subset of $V$. Then:
1. $\text{span}(S)$ is a subspace of $V$.
2. $\text{span}(S)$ is the **smallest subspace** of $V$ containing $S$, in the sense that if $W$ is any subspace of $V$ containing $S$, then $\text{span}(S) \subseteq W$.

*Proof:*
1. $\vec{0} = 0\vec{v}_1 \in \text{span}(S)$. If $\vec{u} = \sum a_i \vec{v}_i$ and $\vec{w} = \sum b_i \vec{v}_i$ are in $\text{span}(S)$, then for any $\alpha, \beta \in F$, $\alpha\vec{u} + \beta\vec{w} = \sum (\alpha a_i + \beta b_i)\vec{v}_i \in \text{span}(S)$. Thus $\text{span}(S) \le V$.
2. If $W \le V$ and $S \subseteq W$, then by closure of $W$ under addition and scalar multiplication, every linear combination $\sum c_i \vec{v}_i$ must belong to $W$. Hence $\text{span}(S) \subseteq W$. $\blacksquare$

---

### 2. Linear Independence and Dependence

A set of vectors $S = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k\} \subseteq V$ is **Linearly Independent** if the vector equation:

$$c_1 \vec{v}_1 + c_2 \vec{v}_2 + \cdots + c_k \vec{v}_k = \vec{0}$$

has **only the trivial solution** $c_1 = c_2 = \cdots = c_k = 0$.

If there exist scalars $c_1, \dots, c_k \in F$, **not all zero**, such that $\sum_{i=1}^k c_i \vec{v}_i = \vec{0}$, then the set $S$ is **Linearly Dependent**.

#### Theorem 3.2 (The Linear Dependence Lemma):
A set $S = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k\}$ ($k \ge 2$) with $\vec{v}_1 \ne \vec{0}$ is linearly dependent if and only if there exists an index $j \in \{2, 3, \dots, k\}$ such that $\vec{v}_j$ is a linear combination of the preceding vectors:

$$\vec{v}_j \in \text{span}\{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_{j-1}\}$$

Furthermore, removing $\vec{v}_j$ does not alter the span: $\text{span}(S \setminus \{\vec{v}_j\}) = \text{span}(S)$.

---

### 3. The Wronskian Determinant in Function Spaces

In the function space $C^{n-1}[a, b]$, let $f_1(x), f_2(x), \dots, f_n(x)$ be $(n-1)$-times continuously differentiable functions. The **Wronskian** is defined by the functional determinant:

$$W(f_1, \dots, f_n)(x) = \det \begin{pmatrix} f_1(x) & f_2(x) & \cdots & f_n(x) \\ f_1'(x) & f_2'(x) & \cdots & f_n'(x) \\ \vdots & \vdots & \ddots & \vdots \\ f_1^{(n-1)}(x) & f_2^{(n-1)}(x) & \cdots & f_n^{(n-1)}(x) \end{pmatrix}$$

#### Theorem 3.3 (Wronskian Test for Linear Independence):
If there exists at least one point $x_0 \in [a, b]$ such that $W(f_1, \dots, f_n)(x_0) \ne 0$, then the functions $\{f_1, f_2, \dots, f_n\}$ are **linearly independent** on $[a, b]$."""
            },
            {
                "id": "u3-sec2",
                "title": "Bases of Vector Spaces & Unique Coordinate Representation",
                "simulation": "sim_la_span_independence",
                "content": r"""### 1. Definition and Characterization of a Basis

A subset $\mathcal{B} = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n\} \subseteq V$ is a **Basis** of vector space $V$ if:
1. $\mathcal{B}$ is linearly independent.
2. $\mathcal{B}$ spans $V$: $\text{span}(\mathcal{B}) = V$.

#### Equivalent Formulations:
- $\mathcal{B}$ is a **minimal spanning set** of $V$: Spans $V$, but removing any vector reduces the span.
- $\mathcal{B}$ is a **maximal linearly independent set** in $V$: Linearly independent, but adding any vector produces a linearly dependent set.

---

### 2. The Unique Representation Theorem

#### Theorem 3.4 (Unique Representation Theorem):
Let $\mathcal{B} = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n\}$ be a basis for $V$. Then for every vector $\vec{v} \in V$, there exists **one and only one** ordered $n$-tuple of scalars $(c_1, c_2, \dots, c_n) \in F^n$ such that:

$$\vec{v} = c_1 \vec{v}_1 + c_2 \vec{v}_2 + \cdots + c_n \vec{v}_n$$

*Proof:*
Since $\mathcal{B}$ spans $V$, at least one representation exists. To prove uniqueness, suppose there exist two representations:
$$\vec{v} = \sum_{i=1}^n c_i \vec{v}_i = \sum_{i=1}^n d_i \vec{v}_i$$
Subtracting the two equations gives:
$$\sum_{i=1}^n (c_i - d_i)\vec{v}_i = \vec{0}$$
Since $\mathcal{B}$ is linearly independent, the coefficients must all be zero:
$$c_i - d_i = 0 \implies c_i = d_i \quad \forall i = 1, 2, \dots, n$$
Thus the representation is strictly unique. $\blacksquare$

#### Coordinate Vectors and Isomorphism:
The unique scalars $c_1, \dots, c_n$ are called the **coordinates** of $\vec{v}$ relative to the ordered basis $\mathcal{B}$, denoted by:

$$[\vec{v}]_{\mathcal{B}} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} \in F^n$$

The mapping $[\cdot]_{\mathcal{B}} : V \to F^n$ is a **vector space isomorphism** (bijective linear map), preserving all vector space operations:
- $[\vec{u} + \vec{v}]_{\mathcal{B}} = [\vec{u}]_{\mathcal{B}} + [\vec{v}]_{\mathcal{B}}$
- $[c\vec{v}]_{\mathcal{B}} = c[\vec{v}]_{\mathcal{B}}$"""
            },
            {
                "id": "u3-sec3",
                "title": "Dimension Theory, Steinitz Exchange & Subspace Sums",
                "content": r"""### 1. The Steinitz Exchange Lemma

#### Theorem 3.5 (Steinitz Exchange Lemma):
Let $V$ be a vector space. Suppose $S = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_m\}$ is a linearly independent subset of $V$, and $G = \{\vec{w}_1, \vec{w}_2, \dots, \vec{w}_n\}$ spans $V$. Then:
1. $m \le n$ (no linearly independent set can have more elements than a spanning set).
2. There exists a subset of $n - m$ vectors from $G$ which, together with $S$, spans $V$.

*Proof by Induction on $m$:*
- For $m = 1$: Since $\vec{v}_1 \ne \vec{0}$ and $G$ spans $V$, $\vec{v}_1 = \sum_{i=1}^n c_i \vec{w}_i$ with at least one $c_k \ne 0$. We can replace $\vec{w}_k$ with $\vec{v}_1$, and the new set $\{\vec{v}_1\} \cup (G \setminus \{\vec{w}_k\})$ still spans $V$.
- By induction, if $k$ vectors $\vec{v}_1, \dots, \vec{v}_k$ have replaced $k$ vectors in $G$, the remaining set spans $V$. If $m > n$, we could replace all $n$ vectors in $G$, leaving $\{\vec{v}_1, \dots, \vec{v}_n\}$ spanning $V$. Then $\vec{v}_{n+1}$ would be a linear combination of $\{\vec{v}_1, \dots, \vec{v}_n\}$, violating the linear independence of $S$. Therefore, $m \le n$. $\blacksquare$

---

### 2. Invariance of Basis Cardinality and Definition of Dimension

#### Theorem 3.6 (Dimension Invariance Theorem):
If $\mathcal{B}_1$ and $\mathcal{B}_2$ are two bases of a finite-dimensional vector space $V$, then they contain the exact same number of elements:

$$|\mathcal{B}_1| = |\mathcal{B}_2|$$

*Proof:*
Since $\mathcal{B}_1$ is linearly independent and $\mathcal{B}_2$ spans $V$, by Steinitz Exchange Lemma, $|\mathcal{B}_1| \le |\mathcal{B}_2|$. Reversing roles, since $\mathcal{B}_2$ is linearly independent and $\mathcal{B}_1$ spans $V$, $|\mathcal{B}_2| \le |\mathcal{B}_1|$. Therefore, $|\mathcal{B}_1| = |\mathcal{B}_2|$. $\blacksquare$

**Definition of Dimension:**  
The **Dimension** of a finite-dimensional vector space $V$, denoted by $\dim(V)$ or $\dim_F(V)$, is the number of vectors in any basis of $V$. If $V = \{\vec{0}\}$, $\dim(V) = 0$.

---

### 3. The Dimension Theorem for Subspace Sums

#### Theorem 3.7 (Grassmann's Subspace Sum Dimension Formula):
Let $W_1$ and $W_2$ be finite-dimensional subspaces of a vector space $V$. Then:

$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

*Proof:*
Let $k = \dim(W_1 \cap W_2)$. Choose a basis $\mathcal{B}_0 = \{\vec{u}_1, \vec{u}_2, \dots, \vec{u}_k\}$ for $W_1 \cap W_2$.
- Since $W_1 \cap W_2 \le W_1$, extend $\mathcal{B}_0$ to a basis of $W_1$:
  $$\mathcal{B}_1 = \{\vec{u}_1, \dots, \vec{u}_k, \; \vec{v}_1, \dots, \vec{v}_r\} \implies \dim(W_1) = k + r$$
- Since $W_1 \cap W_2 \le W_2$, extend $\mathcal{B}_0$ to a basis of $W_2$:
  $$\mathcal{B}_2 = \{\vec{u}_1, \dots, \vec{u}_k, \; \vec{w}_1, \dots, \vec{w}_s\} \implies \dim(W_2) = k + s$$

We claim that $\mathcal{B} = \{\vec{u}_1, \dots, \vec{u}_k, \; \vec{v}_1, \dots, \vec{v}_r, \; \vec{w}_1, \dots, \vec{w}_s\}$ is a basis for $W_1 + W_2$.
1. **Spans $W_1 + W_2$:** Any vector $\vec{x} \in W_1 + W_2$ is $\vec{x} = \vec{x}_1 + \vec{x}_2$ with $\vec{x}_1 \in W_1$ and $\vec{x}_2 \in W_2$. Since $\vec{x}_1 \in \text{span}(\mathcal{B}_1)$ and $\vec{x}_2 \in \text{span}(\mathcal{B}_2)$, their sum is in $\text{span}(\mathcal{B})$.
2. **Linear Independence:** Suppose:
   $$\sum_{i=1}^k a_i \vec{u}_i + \sum_{j=1}^r b_j \vec{v}_j + \sum_{l=1}^s c_l \vec{w}_l = \vec{0}$$
   Rearrange to isolate the $\vec{w}$ terms:
   $$\sum_{l=1}^s c_l \vec{w}_l = -\sum_{i=1}^k a_i \vec{u}_i - \sum_{j=1}^r b_j \vec{v}_j$$
   The left-hand side is in $W_2$, while the right-hand side is in $W_1$. Therefore, the vector $\vec{y} = \sum_{l=1}^s c_l \vec{w}_l$ lies in $W_1 \cap W_2$.
   Since $\mathcal{B}_0$ is a basis for $W_1 \cap W_2$, $\vec{y}$ can be written in terms of $\vec{u}_1, \dots, \vec{u}_k$:
   $$\sum_{l=1}^s c_l \vec{w}_l = \sum_{i=1}^k d_i \vec{u}_i \implies \sum_{i=1}^k d_i \vec{u}_i - \sum_{l=1}^s c_l \vec{w}_l = \vec{0}$$
   Because $\mathcal{B}_2 = \{\vec{u}_1, \dots, \vec{u}_k, \vec{w}_1, \dots, \vec{w}_s\}$ is a basis of $W_2$, it is linearly independent, so all $c_l = 0$ and $d_i = 0$.
   Substitute $c_l = 0$ back into the original equation:
   $$\sum_{i=1}^k a_i \vec{u}_i + \sum_{j=1}^r b_j \vec{v}_j = \vec{0}$$
   Since $\mathcal{B}_1$ is a basis for $W_1$, it is linearly independent, so all $a_i = 0$ and $b_j = 0$.
   Therefore, all coefficients are zero, proving $\mathcal{B}$ is linearly independent!

Thus $\dim(W_1 + W_2) = |\mathcal{B}| = k + r + s$.
Computing the right side:
$$\dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2) = (k + r) + (k + s) - k = k + r + s = \dim(W_1 + W_2)$$
The proof is complete. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "la-prob-3-1",
                "difficulty": "Easy",
                "difficultyLabel": "Tier 1: Foundational",
                "title": "Linear Independence & Basis Verification in R^4",
                "statement": r"""Consider the following set of vectors in $\mathbb{R}^4$:

$$\vec{v}_1 = \begin{pmatrix} 1 \\ 2 \\ -1 \\ 3 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 2 \\ 5 \\ -1 \\ 8 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 1 \\ 1 \\ -2 \\ 1 \end{pmatrix}, \quad \vec{v}_4 = \begin{pmatrix} 3 \\ 7 \\ -2 \\ 11 \end{pmatrix}$$

(a) Determine whether the set $S = \{\vec{v}_1, \vec{v}_2, \vec{v}_3, \vec{v}_4\}$ is linearly independent.  
(b) Find the dimension of $W = \text{span}(S)$ and extract a basis for $W$ from the set $S$.  
(c) Express any redundant vectors as explicit linear combinations of the chosen basis vectors.""",
                "solution": r"""**Step 1: Form the matrix $A$ with vectors as columns and row reduce:**
$$A = \begin{pmatrix} 1 & 2 & 1 & 3 \\ 2 & 5 & 1 & 7 \\ -1 & -1 & -2 & -2 \\ 3 & 8 & 1 & 11 \end{pmatrix}$$

Apply elementary row operations:
- $R_2 \to R_2 - 2R_1$: $(0, \; 5 - 4 = 1, \; 1 - 2 = -1, \; 7 - 6 = 1)$
- $R_3 \to R_3 + R_1$: $(0, \; -1 + 2 = 1, \; -2 + 1 = -1, \; -2 + 3 = 1)$
- $R_4 \to R_4 - 3R_1$: $(0, \; 8 - 6 = 2, \; 1 - 3 = -2, \; 11 - 9 = 2)$

Matrix after Column 1 clearance:
$$\begin{pmatrix} 1 & 2 & 1 & 3 \\ 0 & 1 & -1 & 1 \\ 0 & 1 & -1 & 1 \\ 0 & 2 & -2 & 2 \end{pmatrix}$$

Now clear Column 2:
- $R_1 \to R_1 - 2R_2$: $(1, 0, \; 1 - 2(-1) = 3, \; 3 - 2(1) = 1)$
- $R_3 \to R_3 - R_2$: $(0, 0, 0, 0)$
- $R_4 \to R_4 - 2R_2$: $(0, 0, 0, 0)$

The Reduced Row Echelon Form is:
$$\text{rref}(A) = \begin{pmatrix} 1 & 0 & 3 & 1 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

**Step 2: Linear Independence and Basis Determination:**
- Pivot columns are **Columns 1 and 2**.
- Non-pivot (free) columns are **Columns 3 and 4**.
Since non-pivot columns exist, $S$ is **linearly dependent**.
- The dimension of $W = \text{span}(S)$ is $\text{rank}(A) = 2$.
- A basis for $W$ consists of the original vectors corresponding to the pivot columns:
  $$\mathcal{B} = \{\vec{v}_1, \vec{v}_2\}$$

**Step 3: Linear Combinations for Redundant Vectors:**
From the RREF:
- Column 3: $\begin{pmatrix} 3 \\ -1 \\ 0 \\ 0 \end{pmatrix} \implies \vec{v}_3 = 3\vec{v}_1 - \vec{v}_2$
  Check: $3(1, 2, -1, 3)^T - (2, 5, -1, 8)^T = (1, 1, -2, 1)^T = \vec{v}_3$. Match!
- Column 4: $\begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix} \implies \vec{v}_4 = \vec{v}_1 + \vec{v}_2$
  Check: $(1, 2, -1, 3)^T + (2, 5, -1, 8)^T = (3, 7, -2, 11)^T = \vec{v}_4$. Match!""",
                "answer": r"""$S$ is linearly dependent. $\dim(\text{span}(S)) = 2$. A basis for $W$ is $\{\vec{v}_1, \vec{v}_2\}$. The redundant vectors satisfy $\vec{v}_3 = 3\vec{v}_1 - \vec{v}_2$ and $\vec{v}_4 = \vec{v}_1 + \vec{v}_2$."""
            },
            {
                "id": "la-prob-3-2",
                "difficulty": "Medium",
                "difficultyLabel": "Tier 2: Intermediate Exam",
                "title": "Basis Construction & Dimension of Constrained Polynomial Subspaces",
                "statement": r"""Let $\mathbb{P}_3(\mathbb{R}) = \{a_0 + a_1 t + a_2 t^2 + a_3 t^3 : a_i \in \mathbb{R}\}$ be the 4-dimensional vector space of polynomials of degree at most 3 over $\mathbb{R}$. Consider the subset:

$$W = \{p(t) \in \mathbb{P}_3(\mathbb{R}) : p(1) = 0 \quad \text{and} \quad p'(0) = 0\}$$

(a) Prove that $W$ is a subspace of $\mathbb{P}_3(\mathbb{R})$.  
(b) Find the dimension of $W$.  
(c) Construct an explicit basis $\mathcal{B}_W$ for $W$.  
(d) Extend the basis $\mathcal{B}_W$ to a full basis of $\mathbb{P}_3(\mathbb{R})$.""",
                "solution": r"""**Step 1: Subspace Verification:**
Let $p(t), q(t) \in W$ and $c, d \in \mathbb{R}$.
- $(c p + d q)(1) = c p(1) + d q(1) = c(0) + d(0) = 0$.
- $(c p + d q)'(0) = c p'(0) + d q'(0) = c(0) + d(0) = 0$.
- The zero polynomial satisfies $\mathbf{0}(1) = 0$ and $\mathbf{0}'(0) = 0$.
By the Subspace Criterion, $W$ is a subspace of $\mathbb{P}_3(\mathbb{R})$.

**Step 2: Translate constraints into a linear system:**
Let $p(t) = a_0 + a_1 t + a_2 t^2 + a_3 t^3$.
Then $p'(t) = a_1 + 2 a_2 t + 3 a_3 t^2$.
- Constraint 1: $p'(0) = a_1 = 0$.
- Constraint 2: $p(1) = a_0 + a_1 + a_2 + a_3 = 0$.
Substitute $a_1 = 0$:
$$a_0 + a_2 + a_3 = 0 \implies a_0 = -a_2 - a_3$$

**Step 3: Parametric representation and basis construction:**
The coefficients $a_2$ and $a_3$ are free variables:
$$p(t) = (-a_2 - a_3) + 0 t + a_2 t^2 + a_3 t^3 = a_2(t^2 - 1) + a_3(t^3 - 1)$$

Define:
$$p_1(t) = t^2 - 1, \qquad p_2(t) = t^3 - 1$$
Every $p \in W$ is a linear combination of $p_1(t)$ and $p_2(t)$.
Furthermore, neither polynomial is a scalar multiple of the other, so $\{p_1, p_2\}$ is linearly independent.
Thus:
$$\mathcal{B}_W = \{t^2 - 1, \; t^3 - 1\}, \qquad \dim(W) = 2$$

**Step 4: Extension to full basis of $\mathbb{P}_3(\mathbb{R})$:**
Since $\dim(\mathbb{P}_3) = 4$, we need to append 2 vectors from the standard basis $\{1, t, t^2, t^3\}$ that are linearly independent of $\mathcal{B}_W$.
Consider $q_1(t) = 1$ and $q_2(t) = t$.
Evaluate coordinate vectors with respect to the ordered basis $\{1, t, t^2, t^3\}$:
$$[p_1] = \begin{pmatrix} -1 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \quad [p_2] = \begin{pmatrix} -1 \\ 0 \\ 0 \\ 1 \end{pmatrix}, \quad [q_1] = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad [q_2] = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$$
Form the matrix:
$$M = \begin{pmatrix} -1 & -1 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}$$
Expanding determinant: $\det(M) = -1 \cdot (1 \cdot 1) = -1 \ne 0$.
Thus the set $\{t^2 - 1, \; t^3 - 1, \; 1, \; t\}$ is linearly independent and forms a complete basis for $\mathbb{P}_3(\mathbb{R})$.""",
                "answer": r"""$\dim(W) = 2$. An explicit basis for $W$ is $\mathcal{B}_W = \{t^2 - 1, \; t^3 - 1\}$. Extended basis for $\mathbb{P}_3(\mathbb{R})$: $\{t^2 - 1, \; t^3 - 1, \; 1, \; t\}$."""
            },
            {
                "id": "la-prob-3-3",
                "difficulty": "Hard",
                "difficultyLabel": "Tier 3: Honors / Proof Challenge",
                "title": "Complete Proof of the Dimension Theorem for Subspace Sums",
                "statement": r"""Let $W_1$ and $W_2$ be two finite-dimensional subspaces of an arbitrary vector space $V$ over field $F$.

(a) Prove Grassmann's formula: $\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$.  
(b) Deduce the direct sum dimension formula: If $V = W_1 \oplus W_2$, then $\dim(V) = \dim(W_1) + \dim(W_2)$.  
(c) In $\mathbb{R}^6$, let $W_1$ and $W_2$ be subspaces with $\dim(W_1) = 4$ and $\dim(W_2) = 5$. Determine all possible values for $\dim(W_1 \cap W_2)$ and $\dim(W_1 + W_2)$.""",
                "solution": r"""**Part (a): Formal Proof of Grassmann's Formula:**
Let $k = \dim(W_1 \cap W_2)$, $d_1 = \dim(W_1)$, $d_2 = \dim(W_2)$.
Let $\mathcal{U} = \{\vec{u}_1, \dots, \vec{u}_k\}$ be a basis for the subspace $W_1 \cap W_2$.
By the Basis Extension Theorem:
- Extend $\mathcal{U}$ to a basis of $W_1$: $\mathcal{B}_1 = \{\vec{u}_1, \dots, \vec{u}_k, \; \vec{v}_1, \dots, \vec{v}_{d_1 - k}\}$.
- Extend $\mathcal{U}$ to a basis of $W_2$: $\mathcal{B}_2 = \{\vec{u}_1, \dots, \vec{u}_k, \; \vec{w}_1, \dots, \vec{w}_{d_2 - k}\}$.

Let $\mathcal{B} = \{\vec{u}_1, \dots, \vec{u}_k, \; \vec{v}_1, \dots, \vec{v}_{d_1 - k}, \; \vec{w}_1, \dots, \vec{w}_{d_2 - k}\}$.
1. **$\text{span}(\mathcal{B}) = W_1 + W_2$:**
   Every $\vec{x} \in W_1 + W_2$ is $\vec{x}_1 + \vec{x}_2$ with $\vec{x}_1 \in W_1, \vec{x}_2 \in W_2$.
   Since $\vec{x}_1 \in \text{span}(\mathcal{B}_1) \subseteq \text{span}(\mathcal{B})$ and $\vec{x}_2 \in \text{span}(\mathcal{B}_2) \subseteq \text{span}(\mathcal{B})$, $\vec{x} \in \text{span}(\mathcal{B})$.
2. **Linear Independence of $\mathcal{B}$:**
   Suppose:
   $$\sum_{i=1}^k a_i \vec{u}_i + \sum_{j=1}^{d_1 - k} b_j \vec{v}_j + \sum_{l=1}^{d_2 - k} c_l \vec{w}_l = \vec{0}$$
   Isolate the $\vec{w}_l$ terms:
   $$\sum_{l=1}^{d_2 - k} c_l \vec{w}_l = -\sum_{i=1}^k a_i \vec{u}_i - \sum_{j=1}^{d_1 - k} b_j \vec{v}_j$$
   The left-hand side belongs to $W_2$, while the right-hand side belongs to $W_1$.
   Therefore, $\vec{y} = \sum_{l=1}^{d_2 - k} c_l \vec{w}_l \in W_1 \cap W_2$.
   Since $\mathcal{U}$ is a basis for $W_1 \cap W_2$, there exist scalars $\lambda_1, \dots, \lambda_k$ such that:
   $$\sum_{l=1}^{d_2 - k} c_l \vec{w}_l = \sum_{i=1}^k \lambda_i \vec{u}_i \implies \sum_{i=1}^k \lambda_i \vec{u}_i - \sum_{l=1}^{d_2 - k} c_l \vec{w}_l = \vec{0}$$
   Since $\mathcal{B}_2 = \{\vec{u}_1, \dots, \vec{u}_k, \vec{w}_1, \dots, \vec{w}_{d_2 - k}\}$ is a basis for $W_2$, it is linearly independent.
   Hence all $c_l = 0$ (and $\lambda_i = 0$).
   Substituting $c_l = 0$ into the original dependence relation yields:
   $$\sum_{i=1}^k a_i \vec{u}_i + \sum_{j=1}^{d_1 - k} b_j \vec{v}_j = \vec{0}$$
   Since $\mathcal{B}_1$ is a basis for $W_1$, it is linearly independent, so all $a_i = 0$ and $b_j = 0$.
   Therefore, all coefficients are zero, proving $\mathcal{B}$ is linearly independent.

Thus $\mathcal{B}$ is a basis for $W_1 + W_2$, with cardinality:
$$|\mathcal{B}| = k + (d_1 - k) + (d_2 - k) = d_1 + d_2 - k = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$
Hence $\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$. $\blacksquare$

**Part (b): Direct Sum Formula:**
If $V = W_1 \oplus W_2$, then $V = W_1 + W_2$ and $W_1 \cap W_2 = \{\vec{0}\}$.
Thus $\dim(W_1 \cap W_2) = 0$, giving:
$$\dim(V) = \dim(W_1) + \dim(W_2) - 0 = \dim(W_1) + \dim(W_2)$$

**Part (c): Dimension Bounds in $\mathbb{R}^6$:**
$W_1, W_2 \le \mathbb{R}^6$ with $\dim(W_1) = 4, \dim(W_2) = 5$.
Since $W_1 + W_2 \le \mathbb{R}^6$, $\dim(W_1 + W_2) \le 6$.
Also, $W_2 \subseteq W_1 + W_2 \implies \dim(W_1 + W_2) \ge \dim(W_2) = 5$.
So $\dim(W_1 + W_2) \in \{5, 6\}$.

By Grassmann's formula:
$$\dim(W_1 \cap W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 + W_2) = 4 + 5 - \dim(W_1 + W_2) = 9 - \dim(W_1 + W_2)$$
- If $\dim(W_1 + W_2) = 5$: $\dim(W_1 \cap W_2) = 9 - 5 = 4$ (here $W_1 \subseteq W_2$).
- If $\dim(W_1 + W_2) = 6$: $\dim(W_1 \cap W_2) = 9 - 6 = 3$ (here $W_1 + W_2 = \mathbb{R}^6$).
Possible values: $(\dim(W_1 + W_2), \dim(W_1 \cap W_2)) \in \{(5, 4), (6, 3)\}$.""",
                "answer": r"""Grassmann's formula: $\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$. For direct sum $W_1 \oplus W_2$, $\dim(W_1 \oplus W_2) = \dim(W_1) + \dim(W_2)$. In $\mathbb{R}^6$ with dimensions 4 and 5: either $\dim(W_1 + W_2) = 6$ with $\dim(W_1 \cap W_2) = 3$, or $\dim(W_1 + W_2) = 5$ with $\dim(W_1 \cap W_2) = 4$."""
            }
        ]
    }

def build_unit_4():
    return {
        "id": "la-u4",
        "title": "Unit 4: The Four Fundamental Matrix Subspaces & Rank-Nullity of Matrices",
        "description": "Row space, column space, null space, and left null space of a matrix; basis construction via RREF; proof that row rank equals column rank; the Rank-Nullity Theorem for matrices; orthogonality and the Fundamental Theorem of Linear Algebra; and Sylvester's Rank Inequality.",
        "sections": [
            {
                "id": "u4-sec1",
                "title": "The Four Fundamental Subspaces of a Matrix",
                "content": r"""### 1. Definition of the Four Fundamental Subspaces

Let $A \in M_{m \times n}(F)$ be an $m \times n$ matrix over a field $F$. Associated with $A$ are four canonical subspaces:

1. **The Row Space $\text{Row}(A) \subseteq F^n$:**  
   The subspace of $F^n$ spanned by the rows of $A$:
   $$\text{Row}(A) = \text{span}\{\vec{r}_1, \vec{r}_2, \dots, \vec{r}_m\} = \text{Col}(A^T)$$

2. **The Column Space (Range / Image) $\text{Col}(A) \subseteq F^m$:**  
   The subspace of $F^m$ spanned by the columns of $A$:
   $$\text{Col}(A) = \text{span}\{\vec{c}_1, \vec{c}_2, \dots, \vec{c}_n\} = \{A\vec{x} : \vec{x} \in F^n\}$$

3. **The Null Space (Kernel) $\text{Null}(A) \subseteq F^n$:**  
   The set of all solutions to the homogeneous linear system $A\vec{x} = \vec{0}$:
   $$\text{Null}(A) = \{\vec{x} \in F^n : A\vec{x} = \vec{0}\}$$

4. **The Left Null Space $\text{Null}(A^T) \subseteq F^m$:**  
   The null space of $A^T$, or the set of row vectors $\vec{y}^T$ satisfying $\vec{y}^T A = \vec{0}^T$:
   $$\text{Null}(A^T) = \{\vec{y} \in F^m : A^T \vec{y} = \vec{0}\}$$

---

### 2. Systematic Basis Construction Algorithms via RREF

Let $R = \text{rref}(A)$.
- **Basis for $\text{Row}(A)$:** Elementary row operations preserve the row space ($\text{Row}(A) = \text{Row}(R)$). The **non-zero rows of $R$** form an orthonormal-like, canonical basis for $\text{Row}(A)$.
- **Basis for $\text{Col}(A)$:** EROs do **not** preserve the column space! However, EROs preserve all linear dependence relations among columns. The **original columns of $A$ corresponding to the pivot columns of $R$** form a basis for $\text{Col}(A)$.
- **Basis for $\text{Null}(A)$:** Solve $R\vec{x} = \vec{0}$. Express each pivot variable in terms of free variables $t_1, \dots, t_{n-r}$. Decomposing into vector parametric form $\vec{x} = \sum_{j=1}^{n-r} t_j \vec{v}_j$ yields the **special solutions** $\{\vec{v}_1, \dots, \vec{v}_{n-r}\}$, which form a basis for $\text{Null}(A)$."""
            },
            {
                "id": "u4-sec2",
                "title": "Row Rank Equals Column Rank & The Rank-Nullity Theorem",
                "simulation": "sim_la_four_subspaces",
                "content": r"""### 1. Theorem: Row Rank Equals Column Rank

The **Row Rank** of $A$ is $\dim(\text{Row}(A))$. The **Column Rank** of $A$ is $\dim(\text{Col}(A))$.

#### Theorem 4.1 (Row Rank = Column Rank):
For any matrix $A \in M_{m \times n}(F)$:

$$\dim(\text{Row}(A)) = \dim(\text{Col}(A)) = \text{rank}(A)$$

*Proof:*
Let $R = \text{rref}(A)$, and let $r$ be the number of pivot entries (leading $1$s) in $R$.
1. The non-zero rows of $R$ are linearly independent and span $\text{Row}(R) = \text{Row}(A)$. Since there are $r$ non-zero rows, $\dim(\text{Row}(A)) = r$.
2. The columns of $A$ corresponding to the $r$ pivot columns of $R$ form a basis for $\text{Col}(A)$. Therefore, $\dim(\text{Col}(A)) = r$.
Since both dimensions equal the number of pivots $r$, we have $\dim(\text{Row}(A)) = \dim(\text{Col}(A)) = r$. $\blacksquare$

---

### 2. The Rank-Nullity Theorem for Matrices

#### Theorem 4.2 (The Matrix Rank-Nullity Theorem):
For any $m \times n$ matrix $A$:

$$\text{rank}(A) + \text{nullity}(A) = n$$

where $\text{rank}(A) = \dim(\text{Col}(A))$ and $\text{nullity}(A) = \dim(\text{Null}(A))$.

*Proof:*
Let $r = \text{rank}(A)$ be the number of pivot columns in $\text{rref}(A)$.
The total number of columns in $A$ is $n$.
Every column of $\text{rref}(A)$ is either a pivot column or a free-variable column.
Thus, the number of free variables is $n - r$.
The dimension of the null space $\dim(\text{Null}(A))$ is precisely the number of free variables in the homogeneous solution:
$$\text{nullity}(A) = n - r$$
Rearranging gives:
$$r + (n - r) = n \implies \text{rank}(A) + \text{nullity}(A) = n$$
The proof is complete. $\blacksquare$"""
            },
            {
                "id": "u4-sec3",
                "title": "The Fundamental Theorem of Linear Algebra & Orthogonality",
                "content": r"""### 1. Orthogonal Complements in $\mathbb{R}^n$

Let $W$ be a subspace of $\mathbb{R}^n$. The **Orthogonal Complement** of $W$, denoted by $W^\perp$, is:

$$W^\perp = \{\vec{x} \in \mathbb{R}^n : \vec{x} \cdot \vec{w} = 0 \quad \forall \vec{w} \in W\}$$

Properties of orthogonal complements:
1. $W^\perp$ is a subspace of $\mathbb{R}^n$.
2. $W \cap W^\perp = \{\vec{0}\}$.
3. $\mathbb{R}^n = W \oplus W^\perp$, and $\dim(W) + \dim(W^\perp) = n$.
4. $(W^\perp)^\perp = W$.

---

### 2. The Fundamental Theorem of Linear Algebra (Strang's Four Subspaces)

#### Theorem 4.3 (The Fundamental Theorem of Linear Algebra):
For any real $m \times n$ matrix $A$:
1. The null space is the orthogonal complement of the row space in $\mathbb{R}^n$:
   $$\text{Null}(A) = (\text{Row}(A))^\perp \quad \iff \quad \mathbb{R}^n = \text{Row}(A) \oplus \text{Null}(A)$$
2. The left null space is the orthogonal complement of the column space in $\mathbb{R}^m$:
   $$\text{Null}(A^T) = (\text{Col}(A))^\perp \quad \iff \quad \mathbb{R}^m = \text{Col}(A) \oplus \text{Null}(A^T)$$

*Proof of Part 1:*
A vector $\vec{x} \in \text{Null}(A)$ if and only if $A\vec{x} = \vec{0}$.
In terms of rows $\vec{r}_1, \dots, \vec{r}_m$ of $A$:
$$A\vec{x} = \begin{pmatrix} \vec{r}_1 \cdot \vec{x} \\ \vec{r}_2 \cdot \vec{x} \\ \vdots \\ \vec{r}_m \cdot \vec{x} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$
This holds if and only if $\vec{x}$ is orthogonal to every row $\vec{r}_i$ of $A$, which is equivalent to $\vec{x}$ being orthogonal to all linear combinations of rows, i.e., $\vec{x} \in (\text{Row}(A))^\perp$.
Applying this to $A^T$ yields Part 2. $\blacksquare$

---

### 3. Sylvester's Rank Inequality

#### Theorem 4.4 (Sylvester's Rank Inequality):
Let $A \in M_{m \times n}(F)$ and $B \in M_{n \times p}(F)$. Then:

$$\text{rank}(A) + \text{rank}(B) - n \le \text{rank}(AB) \le \min(\text{rank}(A), \text{rank}(B))$$"""
            }
        ],
        "problems": [
            {
                "id": "la-prob-4-1",
                "difficulty": "Easy",
                "difficultyLabel": "Tier 1: Foundational",
                "title": "Systematic Derivation of the Four Fundamental Subspaces",
                "statement": r"""Given the matrix $A \in M_{3 \times 4}(\mathbb{R})$:

$$A = \begin{pmatrix} 1 & -1 & 2 & 3 \\ 2 & 2 & 0 & 2 \\ 4 & 0 & 4 & 8 \end{pmatrix}$$

(a) Compute the Reduced Row Echelon Form $\text{rref}(A)$.  
(b) Find the rank and nullity of $A$.  
(c) Construct explicit bases for all four fundamental subspaces: $\text{Row}(A), \text{Col}(A), \text{Null}(A)$, and $\text{Null}(A^T)$.  
(d) Explicitly verify that every basis vector of $\text{Null}(A)$ is orthogonal to every basis vector of $\text{Row}(A)$.""",
                "solution": r"""**Step 1: Compute RREF of $A$:**
$$A = \begin{pmatrix} 1 & -1 & 2 & 3 \\ 2 & 2 & 0 & 2 \\ 4 & 0 & 4 & 8 \end{pmatrix}$$

Apply row operations:
- $R_2 \to R_2 - 2R_1$: $(0, \; 2 - 2(-1) = 4, \; 0 - 4 = -4, \; 2 - 6 = -4)$
- $R_3 \to R_3 - 4R_1$: $(0, \; 0 - 4(-1) = 4, \; 4 - 8 = -4, \; 8 - 12 = -4)$

Row 2 divided by 4: $R_2 \to \frac{1}{4}R_2 = (0, 1, -1, -1)$.
Row 3 minus Row 2: $R_3 \to R_3 - 4R_2 = (0, 0, 0, 0)$.
Clear Row 1 above pivot: $R_1 \to R_1 + R_2 = (1, 0, \; 2 - 1 = 1, \; 3 - 1 = 2)$.

The RREF is:
$$\text{rref}(A) = \begin{pmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & -1 & -1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

**Step 2: Rank and Nullity:**
- Number of pivots = 2 $\implies \text{rank}(A) = 2$.
- Number of columns $n = 4 \implies \text{nullity}(A) = 4 - 2 = 2$.

**Step 3: Bases for the Four Subspaces:**
1. **Row Space $\text{Row}(A) \subseteq \mathbb{R}^4$:**
   $$\mathcal{B}_{\text{Row}} = \left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \\ 2 \end{pmatrix}, \; \begin{pmatrix} 0 \\ 1 \\ -1 \\ -1 \end{pmatrix} \right\}$$
2. **Column Space $\text{Col}(A) \subseteq \mathbb{R}^3$:**
   Pivots are in columns 1 and 2:
   $$\mathcal{B}_{\text{Col}} = \left\{ \begin{pmatrix} 1 \\ 2 \\ 4 \end{pmatrix}, \; \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix} \right\}$$
3. **Null Space $\text{Null}(A) \subseteq \mathbb{R}^4$:**
   From RREF: $x_1 + x_3 + 2x_4 = 0 \implies x_1 = -x_3 - 2x_4$; $x_2 - x_3 - x_4 = 0 \implies x_2 = x_3 + x_4$.
   Free variables $x_3 = s, x_4 = t$:
   $$\vec{x} = s \begin{pmatrix} -1 \\ 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -2 \\ 1 \\ 0 \\ 1 \end{pmatrix} \implies \mathcal{B}_{\text{Null}} = \left\{ \begin{pmatrix} -1 \\ 1 \\ 1 \\ 0 \end{pmatrix}, \; \begin{pmatrix} -2 \\ 1 \\ 0 \\ 1 \end{pmatrix} \right\}$$
4. **Left Null Space $\text{Null}(A^T) \subseteq \mathbb{R}^3$:**
   Solve $A^T \vec{y} = \vec{0}$:
   $$A^T = \begin{pmatrix} 1 & 2 & 4 \\ -1 & 2 & 0 \\ 2 & 0 & 4 \\ 3 & 2 & 8 \end{pmatrix} \to \text{rref}(A^T) = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
   $y_1 = -2y_3, y_2 = -y_3$. Letting $y_3 = 1$:
   $$\mathcal{B}_{\text{LeftNull}} = \left\{ \begin{pmatrix} -2 \\ -1 \\ 1 \end{pmatrix} \right\}$$

**Step 4: Verify Orthogonality $\text{Row}(A) \perp \text{Null}(A)$:**
- $\vec{r}_1 \cdot \vec{n}_1 = 1(-1) + 0(1) + 1(1) + 2(0) = -1 + 1 = 0$.
- $\vec{r}_1 \cdot \vec{n}_2 = 1(-2) + 0(1) + 1(0) + 2(1) = -2 + 2 = 0$.
- $\vec{r}_2 \cdot \vec{n}_1 = 0(-1) + 1(1) + (-1)(1) + (-1)(0) = 1 - 1 = 0$.
- $\vec{r}_2 \cdot \vec{n}_2 = 0(-2) + 1(1) + (-1)(0) + (-1)(1) = 1 - 1 = 0$.
Orthogonality strictly verified!""",
                "answer": r"""$\text{rank}(A) = 2, \text{nullity}(A) = 2$. $\mathcal{B}_{\text{Row}} = \{(1, 0, 1, 2)^T, (0, 1, -1, -1)^T\}$, $\mathcal{B}_{\text{Col}} = \{(1, 2, 4)^T, (-1, 2, 0)^T\}$, $\mathcal{B}_{\text{Null}} = \{(-1, 1, 1, 0)^T, (-2, 1, 0, 1)^T\}$, $\mathcal{B}_{\text{LeftNull}} = \{(-2, -1, 1)^T\}$. Orthogonality verified."""
            },
            {
                "id": "la-prob-4-2",
                "difficulty": "Medium",
                "difficultyLabel": "Tier 2: Intermediate Exam",
                "title": "Rank Analysis of Matrix Products & Invariance Under Multiplication",
                "statement": r"""(a) Prove that for any two matrices $A \in M_{m \times n}(F)$ and $B \in M_{n \times p}(F)$:
$$\text{rank}(AB) \le \min(\text{rank}(A), \text{rank}(B))$$
(b) If $P \in M_{m \times m}(F)$ is an invertible matrix, prove that $\text{rank}(PA) = \text{rank}(A)$.  
(c) If $Q \in M_{n \times n}(F)$ is an invertible matrix, prove that $\text{rank}(AQ) = \text{rank}(A)$.  
(d) Find a concrete counterexample showing that $\text{rank}(AB)$ can be strictly less than $\min(\text{rank}(A), \text{rank}(B))$. Under what necessary and sufficient condition on the fundamental subspaces does equality $\text{rank}(AB) = \text{rank}(B)$ hold?""",
                "solution": r"""**Part (a): Proof of $\text{rank}(AB) \le \min(\text{rank}(A), \text{rank}(B))$:**
1. Column space containment: Each column of $AB$ is a linear combination of the columns of $A$:
   $$(AB)_{*j} = A (B_{*j}) \in \text{Col}(A)$$
   Therefore, $\text{Col}(AB) \subseteq \text{Col}(A)$.
   Since a subspace cannot have a larger dimension than its parent space:
   $$\text{rank}(AB) = \dim(\text{Col}(AB)) \le \dim(\text{Col}(A)) = \text{rank}(A)$$
2. Row space containment: Similarly, each row of $AB$ is a linear combination of the rows of $B$:
   $$(AB)_{i*} = (A_{i*}) B \in \text{Row}(B)$$
   Therefore, $\text{Row}(AB) \subseteq \text{Row}(B)$, implying:
   $$\text{rank}(AB) = \dim(\text{Row}(AB)) \le \dim(\text{Row}(B)) = \text{rank}(B)$$
Combining both inequalities gives $\text{rank}(AB) \le \min(\text{rank}(A), \text{rank}(B))$. $\blacksquare$

**Part (b): Invariance under invertible pre-multiplication:**
Since $P$ is invertible, $A = P^{-1}(PA)$. Applying Part (a):
$$\text{rank}(PA) \le \text{rank}(A) \quad \text{and} \quad \text{rank}(A) = \text{rank}(P^{-1}(PA)) \le \text{rank}(PA)$$
Thus $\text{rank}(PA) = \text{rank}(A)$.

**Part (c): Invariance under invertible post-multiplication:**
Since $Q$ is invertible, $A = (AQ) Q^{-1}$. Applying Part (a):
$$\text{rank}(AQ) \le \text{rank}(A) \quad \text{and} \quad \text{rank}(A) = \text{rank}((AQ)Q^{-1}) \le \text{rank}(AQ)$$
Thus $\text{rank}(AQ) = \text{rank}(A)$.

**Part (d): Counterexample and Condition for Equality:**
Let $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
Here $\text{rank}(A) = 1$ and $\text{rank}(B) = 1$.
However:
$$AB = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \implies \text{rank}(AB) = 0 < \min(1, 1)$$

*Condition for $\text{rank}(AB) = \text{rank}(B)$:*
Consider the linear transformation $T_A: \text{Col}(B) \to F^m$ defined by $T_A(\vec{v}) = A\vec{v}$.
By the Rank-Nullity Theorem applied to $T_A|_{\text{Col}(B)}$:
$$\dim(\text{Col}(B)) = \dim(\ker(T_A|_{\text{Col}(B)})) + \dim(\text{im}(T_A|_{\text{Col}(B)})) = \dim(\text{Col}(B) \cap \text{Null}(A)) + \text{rank}(AB)$$
Therefore, $\text{rank}(AB) = \text{rank}(B)$ if and only if $\dim(\text{Col}(B) \cap \text{Null}(A)) = 0$, i.e.:
$$\text{Col}(B) \cap \text{Null}(A) = \{\vec{0}\}$$""",
                "answer": r"""$\text{rank}(AB) \le \min(\text{rank}(A), \text{rank}(B))$. Invertible multiplication preserves rank. Strictly smaller rank occurs when $\text{Col}(B)$ intersects $\text{Null}(A)$ non-trivially (e.g. nilpotents $A=B=\begin{pmatrix}0&1\\0&0\end{pmatrix} \implies AB = O$). Equality $\text{rank}(AB) = \text{rank}(B)$ holds $\iff \text{Col}(B) \cap \text{Null}(A) = \{\vec{0}\}$."""
            },
            {
                "id": "la-prob-4-3",
                "difficulty": "Hard",
                "difficultyLabel": "Tier 3: Honors / Proof Challenge",
                "title": "Rigorous Proof of Sylvester's Rank Inequality",
                "statement": r"""Let $A \in M_{m \times n}(F)$ and $B \in M_{n \times p}(F)$ be matrices over field $F$.

(a) Prove rigorously Sylvester's Rank Inequality:
$$\text{rank}(A) + \text{rank}(B) - n \le \text{rank}(AB)$$
(b) Give an alternative geometric proof using the restriction of the linear map $T_A$ to the subspace $\text{Col}(B)$.  
(c) Deduce that if $n = p$ and $AB = O$, then $\text{rank}(A) + \text{rank}(B) \le n$. Provide an example achieving equality.""",
                "solution": r"""**Part (a): Formal Proof via Rank-Nullity:**
Consider the linear transformation $T_A: F^n \to F^m$ defined by $T_A(\vec{x}) = A\vec{x}$.
Restrict $T_A$ to the subspace $W = \text{Col}(B) \subseteq F^n$.
The image of this restriction is:
$$T_A(W) = T_A(\text{Col}(B)) = \{A(B\vec{y}) : \vec{y} \in F^p\} = \text{Col}(AB)$$
The kernel of this restriction is:
$$\ker(T_A|_{W}) = \{\vec{w} \in W : A\vec{w} = \vec{0}\} = W \cap \ker(T_A) = \text{Col}(B) \cap \text{Null}(A)$$

By the Rank-Nullity Theorem applied to $T_A|_W$:
$$\dim(W) = \dim(\ker(T_A|_W)) + \dim(T_A(W))$$
$$\text{rank}(B) = \dim(\text{Col}(B) \cap \text{Null}(A)) + \text{rank}(AB)$$
Rearranging for $\text{rank}(AB)$:
$$\text{rank}(AB) = \text{rank}(B) - \dim(\text{Col}(B) \cap \text{Null}(A))$$

Since $\text{Col}(B) \cap \text{Null}(A) \subseteq \text{Null}(A)$:
$$\dim(\text{Col}(B) \cap \text{Null}(A)) \le \dim(\text{Null}(A)) = \text{nullity}(A)$$
By the Rank-Nullity Theorem for matrix $A$:
$$\text{nullity}(A) = n - \text{rank}(A)$$
Therefore:
$$\dim(\text{Col}(B) \cap \text{Null}(A)) \le n - \text{rank}(A)$$

Substituting this bound into our expression for $\text{rank}(AB)$:
$$\text{rank}(AB) = \text{rank}(B) - \dim(\text{Col}(B) \cap \text{Null}(A)) \ge \text{rank}(B) - (n - \text{rank}(A))$$
$$\text{rank}(AB) \ge \text{rank}(A) + \text{rank}(B) - n$$
This establishes Sylvester's Rank Inequality. $\blacksquare$

**Part (b): Alternative Proof via Grassmann's Formula:**
In $F^n$, consider the two subspaces $W_1 = \text{Null}(A)$ and $W_2 = \text{Col}(B)$.
By Grassmann's dimension formula:
$$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$
Since $W_1 + W_2 \subseteq F^n$, we have $\dim(W_1 + W_2) \le n$. Thus:
$$\dim(W_1 \cap W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 + W_2) \ge \dim(\text{Null}(A)) + \dim(\text{Col}(B)) - n$$
Substituting $\dim(\text{Null}(A)) = n - \text{rank}(A)$ and $\dim(\text{Col}(B)) = \text{rank}(B)$:
$$\dim(W_1 \cap W_2) \ge (n - \text{rank}(A)) + \text{rank}(B) - n = \text{rank}(B) - \text{rank}(A)$$
From $\text{rank}(AB) = \text{rank}(B) - \dim(W_1 \cap W_2)$:
$$\text{rank}(AB) \ge \text{rank}(B) - \dim(W_1 \cap W_2)$$
Substituting $\dim(W_1 \cap W_2) \le \dim(\text{Null}(A)) = n - \text{rank}(A)$ yields $\text{rank}(AB) \ge \text{rank}(A) + \text{rank}(B) - n$. $\blacksquare$

**Part (c): Consequence for $AB = O$:**
If $AB = O$, then $\text{rank}(AB) = 0$.
Applying Sylvester's inequality:
$$0 \ge \text{rank}(A) + \text{rank}(B) - n \implies \text{rank}(A) + \text{rank}(B) \le n$$
Alternatively, $AB = O \implies \text{Col}(B) \subseteq \text{Null}(A) \implies \text{rank}(B) \le \text{nullity}(A) = n - \text{rank}(A)$.

*Equality Example for $n = 4$:*
Let $A = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$.
$\text{rank}(A) = 2, \text{rank}(B) = 2$.
$AB = O$, and $\text{rank}(A) + \text{rank}(B) = 2 + 2 = 4 = n$. Equality achieved!""",
                "answer": r"""$\text{rank}(AB) \ge \text{rank}(A) + \text{rank}(B) - n$ proved via Rank-Nullity on $T_A|_{\text{Col}(B)}$. If $AB = O$, $\text{rank}(A) + \text{rank}(B) \le n$. Equality holds when $\text{Col}(B) = \text{Null}(A)$ (e.g. complementary projection matrices $A = \text{diag}(1,1,0,0)$ and $B = \text{diag}(0,0,1,1)$)."""
            }
        ]
    }

if __name__ == "__main__":
    u3 = build_unit_3()
    u4 = build_unit_4()
    with open("la_u3.json", "w", encoding="utf-8") as f:
        json.dump(u3, f, indent=2)
    with open("la_u4.json", "w", encoding="utf-8") as f:
        json.dump(u4, f, indent=2)
    print("Units 3 and 4 successfully built: la_u3.json, la_u4.json")
