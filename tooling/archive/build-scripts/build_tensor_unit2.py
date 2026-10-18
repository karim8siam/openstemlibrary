# -*- coding: utf-8 -*-
"""
build_tensor_unit2.py
Constructs Unit 2: Tensor Algebra, Operations & The Quotient Law
Strictly ZERO course numbers.
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Tensor Algebra, Operations & The Quotient Law",
        "leadSummary": "Comprehensive mathematical theory of tensor algebra: classification of tensors into contravariant, covariant, and mixed types of arbitrary rank (r, s), multilinear coordinate transformation laws, linear combinations, outer (Kronecker) tensor products, index contraction reducing rank by (1, 1), inner products and trace invariants, the Quotient Law of tensors, symmetric and antisymmetric tensor decompositions, and the Levi-Civita alternating pseudo-tensor.",
        "simulations": ["sim_tensor_algebra_contraction"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Higher-Rank Tensors: Covariant, Contravariant & Mixed Transformation Laws",
                "content": r"""### 1. General Definition of a Tensor of Type $(r, s)$

In modern differential geometry and multilinear algebra, a tensor is an invariant geometric object whose components with respect to a coordinate basis transform multilinearly under changes of coordinates.

> **Definition 2.1 (Tensor of Rank $(r, s)$):**
> A geometric entity is called a **tensor of contravariant rank $r$ and covariant rank $s$** (or simply a tensor of type $(r, s)$ and total rank $r + s$) at point $P \in V_n$ if it is characterized by $n^{r+s}$ real numbers:
> $$T^{i_1 i_2 \dots i_r}_{j_1 j_2 \dots j_s}$$
> in coordinate system $x^k$, such that under an arbitrary regular coordinate transformation $x^k \to \bar{x}^k$, its components in the new system $\bar{T}$ are given by:
> $$\bar{T}^{i_1 \dots i_r}_{j_1 \dots j_s} = \left( \prod_{\alpha=1}^r \frac{\partial \bar{x}^{i_\alpha}}{\partial x^{p_\alpha}} \right) \left( \prod_{\beta=1}^s \frac{\partial x^{q_\beta}}{\partial \bar{x}^{j_\beta}} \right) T^{p_1 \dots p_r}_{q_1 \dots q_s}$$

#### Special Cases of Tensor Ranks:
1. **Rank $(0, 0)$:** A scalar invariant $\Phi$ ($\bar{\Phi} = \Phi$, 1 component).
2. **Rank $(1, 0)$:** A contravariant vector $A^i$ ($\bar{A}^i = \frac{\partial \bar{x}^i}{\partial x^p} A^p$, $n$ components).
3. **Rank $(0, 1)$:** A covariant vector (covector / 1-form) $B_j$ ($\bar{B}_j = \frac{\partial x^q}{\partial \bar{x}^j} B_q$, $n$ components).
4. **Rank $(2, 0)$:** A contravariant tensor of second rank $T^{ij}$ ($\bar{T}^{ij} = \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial \bar{x}^j}{\partial x^q} T^{pq}$, $n^2$ components).
5. **Rank $(0, 2)$:** A covariant tensor of second rank $T_{ij}$ ($\bar{T}_{ij} = \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} T_{pq}$, $n^2$ components).
6. **Rank $(1, 1)$:** A mixed tensor of second rank $T^i_{\; j}$ ($\bar{T}^i_{\; j} = \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial x^q}{\partial \bar{x}^j} T^p_{\; q}$, $n^2$ components).

---

### 2. Group Property of Tensor Transformations

The set of all admissible coordinate transformations forms a mathematical Lie group under composition.
If coordinate transition $x \to \bar{x}$ has Jacobian $J_1$ and $\bar{x} \to \bar{\bar{x}}$ has Jacobian $J_2$, then the composite transformation $x \to \bar{\bar{x}}$ satisfies:
$$\frac{\partial \bar{\bar{x}}^i}{\partial x^k} = \frac{\partial \bar{\bar{x}}^i}{\partial \bar{x}^m} \frac{\partial \bar{x}^m}{\partial x^k}$$
Applying this identity to the tensor transformation law verifies that the composition of two tensor transformations is itself a tensor transformation of the exact same type. Thus, tensor character is an intrinsic, coordinate-independent mathematical property."""
            },
            {
                "secNumber": "2.2",
                "title": "Tensor Algebra: Linear Combinations, Outer Products & Contraction",
                "content": r"""### 1. Addition and Linear Combinations

> **Theorem 2.1 (Addition of Tensors):**
> If $A^{i_1 \dots i_r}_{j_1 \dots j_s}$ and $B^{i_1 \dots i_r}_{j_1 \dots j_s}$ are two tensors of the **exact same type $(r, s)$**, then their linear combination:
> $$C^{i_1 \dots i_r}_{j_1 \dots j_s} = \alpha A^{i_1 \dots i_r}_{j_1 \dots j_s} + \beta B^{i_1 \dots i_r}_{j_1 \dots j_s} \qquad (\alpha, \beta \in \mathbb{R})$$
> is also a tensor of type $(r, s)$.

*Proof:* Follows directly from the linearity of the Jacobian transformation matrices.
*(Note: Tensors of different ranks or different index heights cannot be added, as their transformation laws do not factor).*

---

### 2. Outer Product (Tensor Product $\otimes$)

> **Theorem 2.2 (Outer Product Theorem):**
> Let $A$ be a tensor of type $(r, s)$ and $B$ be a tensor of type $(p, q)$. The **outer product** $C = A \otimes B$, defined by:
> $$C^{i_1 \dots i_r k_1 \dots k_p}_{j_1 \dots j_s l_1 \dots l_q} = A^{i_1 \dots i_r}_{j_1 \dots j_s} B^{k_1 \dots k_p}_{l_1 \dots l_q}$$
> is a tensor of contravariant rank $r + p$ and covariant rank $s + q$ (type $(r+p, s+q)$).

*Proof:*
Transform each tensor factor independently:
$$\bar{C}^{\bar{I} \bar{K}}_{\bar{J} \bar{L}} = \bar{A}^{\bar{I}}_{\bar{J}} \bar{B}^{\bar{K}}_{\bar{L}} = \left( \frac{\partial \bar{x}^I}{\partial x^P} \frac{\partial x^Q}{\partial \bar{x}^J} A^P_Q \right) \left( \frac{\partial \bar{x}^K}{\partial x^M} \frac{\partial x^N}{\partial \bar{x}^L} B^M_N \right) = \left( \frac{\partial \bar{x}^I}{\partial x^P} \frac{\partial \bar{x}^K}{\partial x^M} \frac{\partial x^Q}{\partial \bar{x}^J} \frac{\partial x^N}{\partial \bar{x}^L} \right) C^{PM}_{QN}$$
The transformation law factors into the product of $r+p$ contravariant Jacobian factors and $s+q$ covariant Jacobian factors. Thus $C$ is a tensor of type $(r+p, s+q)$. $\blacksquare$

---

### 3. Contraction of Indices

**Contraction** consists of setting one upper index equal to one lower index and summing over their common values according to the Einstein summation convention.

> **Theorem 2.3 (Contraction Theorem):**
> If $T^{i_1 \dots i_r}_{j_1 \dots j_s}$ is a tensor of type $(r, s)$ with $r \ge 1$ and $s \ge 1$, then contracting one contravariant index with one covariant index (e.g., setting $i_1 = j_1 = k$ and summing):
> $$U^{i_2 \dots i_r}_{j_2 \dots j_s} = T^{k i_2 \dots i_r}_{k j_2 \dots j_s}$$
> produces a tensor of type $(r-1, s-1)$.

*Proof:*
Transform the contracted tensor:
$$\bar{T}^{k i_2 \dots i_r}_{k j_2 \dots j_s} = \frac{\partial \bar{x}^k}{\partial x^p} \frac{\partial x^q}{\partial \bar{x}^k} \left( \frac{\partial \bar{x}^{i_2}}{\partial x^{p_2}} \cdots \frac{\partial x^{q_2}}{\partial \bar{x}^{j_2}} \cdots \right) T^{p p_2 \dots p_r}_{q q_2 \dots q_s}$$
Observe the contracted Jacobian factors:
$$\frac{\partial \bar{x}^k}{\partial x^p} \frac{\partial x^q}{\partial \bar{x}^k} = \frac{\partial x^q}{\partial x^p} = \delta^q_p$$
Substituting $\delta^q_p$ collapses the indices $p$ and $q$:
$$\delta^q_p T^{p p_2 \dots p_r}_{q q_2 \dots q_s} = T^{p p_2 \dots p_r}_{p q_2 \dots q_s}$$
The remaining Jacobian factors are precisely those of a tensor of type $(r-1, s-1)$. $\blacksquare$"""
            },
            {
                "secNumber": "2.3",
                "title": "Inner Products, Traces & Index Contraction Properties",
                "content": r"""### 1. Inner Product of Tensors

The **inner product** of two tensors is defined as the outer product followed immediately by one or more contractions.
- **Example 1:** Vector $A^i$ and covector $B_j$. Outer product: $T^i_{\; j} = A^i B_j$ (rank 2). Contracting $i = j$ yields the scalar inner product $A^i B_i$ (rank 0).
- **Example 2:** Rank-2 tensor $T_{ij}$ and contravariant vector $v^j$. The inner product $w_i = T_{ij} v^j$ is a covariant vector (rank 1).
- **Example 3:** Two rank-2 tensors $A^{ij}$ and $B_{jk}$. Inner product $C^i_{\; k} = A^{ij} B_{jk}$ is a mixed rank-2 tensor.

---

### 2. The Trace Invariant of Mixed Tensors

For a mixed tensor of second rank $T^i_{\; j}$, contracting the upper index with the lower index yields:
$$\text{Tr}(T) = T^i_{\; i} = T^1_{\; 1} + T^2_{\; 2} + \dots + T^n_{\; n}$$
By Theorem 2.3, contracting type $(1, 1)$ yields type $(0, 0)$, which is an **absolute scalar invariant**.
In contrast, the diagonal sum of a purely covariant tensor $\sum_i T_{ii}$ is **NOT an invariant** under general coordinate transformations.

---

### 3. The Generalized Kronecker Delta

> **Definition 2.2 (Generalized Kronecker Delta):**
> The generalized Kronecker delta of rank $2k$ is defined by the determinant:
> $$\delta^{i_1 i_2 \dots i_k}_{j_1 j_2 \dots j_k} = \begin{vmatrix} \delta_{j_1}^{i_1} & \delta_{j_2}^{i_1} & \dots & \delta_{j_k}^{i_1} \\ \delta_{j_1}^{i_2} & \delta_{j_2}^{i_2} & \dots & \delta_{j_k}^{i_2} \\ \vdots & \vdots & \ddots & \vdots \\ \delta_{j_1}^{i_k} & \delta_{j_2}^{i_k} & \dots & \delta_{j_k}^{i_k} \end{vmatrix}$$
> It is $+1$ if $(j_1, \dots, j_k)$ is an even permutation of distinct indices $(i_1, \dots, i_k)$, $-1$ if an odd permutation, and $0$ if any index is repeated. It is an isotropic mixed tensor of type $(k, k)$."""
            },
            {
                "secNumber": "2.4",
                "title": "The Quotient Law of Tensors & Tensor Criteria",
                "content": r"""### 1. Formulation of the Quotient Law

Testing whether a candidate array of $n^k$ functions forms a tensor by verifying the multilinear transformation law directly can be algebraically prohibitive. The **Quotient Law of Tensors** provides an indispensable criterion: if the inner product of a candidate entity with an arbitrary known tensor always produces a tensor, then the candidate entity is itself a tensor.

> **Theorem 2.4 (The Quotient Law for Rank-2 Tensors):**
> Let $A(i, j)$ be a set of $n^2$ quantities defined in every coordinate system.
> If for every **arbitrary contravariant vector** $u^i$ and every **arbitrary contravariant vector** $v^j$, the scalar contraction:
> $$\Phi = A(i, j) u^i v^j$$
> is an **invariant scalar** ($\bar{\Phi} = \Phi$), then $A(i, j)$ are the components of a **covariant tensor of rank 2** ($A(i, j) = A_{ij}$).

*Proof:*
1. In coordinate system $x^k$: $\Phi = A(p, q) u^p v^q$.
2. In coordinate system $\bar{x}^k$: $\bar{\Phi} = \bar{A}(i, j) \bar{u}^i \bar{v}^j$.
3. Since $u^p$ and $v^q$ are known contravariant vectors:
   $$\bar{u}^i = \frac{\partial \bar{x}^i}{\partial x^p} u^p, \qquad \bar{v}^j = \frac{\partial \bar{x}^j}{\partial x^q} v^q$$
4. Substitute these into $\bar{\Phi}$:
   $$\bar{\Phi} = \bar{A}(i, j) \left( \frac{\partial \bar{x}^i}{\partial x^p} u^p \right) \left( \frac{\partial \bar{x}^j}{\partial x^q} v^q \right) = \left[ \bar{A}(i, j) \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial \bar{x}^j}{\partial x^q} \right] u^p v^q$$
5. Since $\bar{\Phi} = \Phi$, we equate both expressions:
   $$\left[ \bar{A}(i, j) \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial \bar{x}^j}{\partial x^q} - A(p, q) \right] u^p v^q = 0$$
6. Crucially, the vectors $u^p$ and $v^q$ are **completely arbitrary**. Setting $u^p = \delta^p_a$ and $v^q = \delta^q_b$ selects the individual $(a, b)$-component:
   $$\bar{A}(i, j) \frac{\partial \bar{x}^i}{\partial x^a} \frac{\partial \bar{x}^j}{\partial x^b} - A(a, b) = 0 \implies A(a, b) = \frac{\partial \bar{x}^i}{\partial x^a} \frac{\partial \bar{x}^j}{\partial x^b} \bar{A}(i, j)$$
7. Multiplying both sides by $\frac{\partial x^a}{\partial \bar{x}^k} \frac{\partial x^b}{\partial \bar{x}^l}$ and contracting over $a$ and $b$:
   $$\bar{A}(k, l) = \frac{\partial x^a}{\partial \bar{x}^k} \frac{\partial x^b}{\partial \bar{x}^l} A(a, b)$$
   This is precisely the transformation law of a covariant tensor of rank 2. $\blacksquare$"""
            },
            {
                "secNumber": "2.5",
                "title": "Symmetric, Antisymmetric Tensors & Interactive Algebra Lab",
                "content": r"""### 1. Symmetric and Antisymmetric Tensors

Let $T_{ij}$ be a second-rank covariant tensor:
- **Symmetric Tensor:** $T_{ij} = T_{ji}$ for all $i, j$.
- **Antisymmetric (Skew-Symmetric) Tensor:** $T_{ij} = -T_{ji}$ for all $i, j$ (implying $T_{ii} = 0$ along the diagonal).

> **Theorem 2.5 (Preservation of Symmetry under Coordinate Changes):**
> If a tensor is symmetric (or antisymmetric) with respect to two indices in one coordinate system, it is **symmetric (or antisymmetric) in all coordinate systems**.

*Proof for Symmetry:*
Assume $T_{pq} = T_{qp}$ in coordinates $x^k$.
$$\bar{T}_{ij} = \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} T_{pq} = \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} T_{qp}$$
Renaming dummy indices $p \leftrightarrow q$:
$$\bar{T}_{ij} = \frac{\partial x^q}{\partial \bar{x}^i} \frac{\partial x^p}{\partial \bar{x}^j} T_{pq} = \frac{\partial x^p}{\partial \bar{x}^j} \frac{\partial x^q}{\partial \bar{x}^i} T_{pq} = \bar{T}_{ji}$$
Thus symmetry is a true coordinate invariant. $\blacksquare$

---

### 2. Decomposition of a Rank-2 Tensor

Any second-rank tensor $T_{ij}$ can be uniquely decomposed into the sum of a symmetric tensor $S_{ij} = T_{(ij)}$ and an antisymmetric tensor $A_{ij} = T_{[ij]}$:
$$T_{ij} = T_{(ij)} + T_{[ij]}$$
where:
$$T_{(ij)} = \frac{1}{2}(T_{ij} + T_{ji}), \qquad T_{[ij]} = \frac{1}{2}(T_{ij} - T_{ji})$$

- Number of independent components of symmetric tensor in $n$ dimensions: $\frac{n(n + 1)}{2}$.
- Number of independent components of antisymmetric tensor in $n$ dimensions: $\frac{n(n - 1)}{2}$.
- Total sum: $\frac{n(n+1)}{2} + \frac{n(n-1)}{2} = n^2$.

---

### 3. The Levi-Civita Permutation Symbol and Pseudo-Tensors

The **Levi-Civita permutation symbol** $\epsilon_{ijk}$ in 3 dimensions is defined by:
$$\epsilon_{ijk} = \begin{cases} +1 & \text{if } (i, j, k) \text{ is an even permutation of } (1, 2, 3) \\ -1 & \text{if } (i, j, k) \text{ is an odd permutation of } (1, 2, 3) \\ 0 & \text{if any two indices are equal} \end{cases}$$

Under coordinate transformations:
$$\bar{\epsilon}_{ijk} = \det\left(\frac{\partial x}{\partial \bar{x}}\right) \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} \frac{\partial x^r}{\partial \bar{x}^k} \epsilon_{pqr} = \frac{1}{J} \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} \frac{\partial x^r}{\partial \bar{x}^k} \epsilon_{pqr}$$
The appearance of the Jacobian factor $\frac{1}{J}$ indicates that $\epsilon_{ijk}$ is a **tensor density** (or relative pseudo-tensor) of weight $-1$. To make it a true absolute tensor, it must be multiplied by $\sqrt{g}$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 2.1: Outer Product, Dual Contractions & Trace Invariance",
                "statement": r"""Consider two vectors in $\mathbb{R}^3$: a contravariant vector $A^i = (2, -1, 3)$ and a covariant vector $B_j = (4, 1, -2)$.
1. Compute the components of the rank-$(1, 1)$ mixed tensor formed by their outer product:
   $$T^i_{\; j} = A^i B_j$$
2. Calculate the trace invariant $\text{Tr}(T) = T^i_{\; i}$.
3. Verify that $\text{Tr}(T)$ equals the direct scalar inner product $A^k B_k$.
4. Prove that if $S^i_{\; j} = u^i v_j$, then $S^i_{\; k} S^k_{\; j} = \lambda S^i_{\; j}$, where $\lambda$ is a scalar invariant, and determine $\lambda$.""",
                "hints": [
                    "Form the $3 \\times 3$ matrix $T^i_{\\; j} = A^i B_j$.",
                    "Sum the diagonal elements $T^1_{\\; 1} + T^2_{\\; 2} + T^3_{\\; 3}$.",
                    "For part 4, substitute $S^k_{\\; j} = u^k v_j$ into $S^i_{\\; k} S^k_{\\; j}$ and factor out scalar $v_k u^k$."
                ],
                "solution": r"""### 1. Outer Product Matrix $T^i_{\; j} = A^i B_j$
Given $A^i = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$ and $B_j = \begin{pmatrix} 4 & 1 & -2 \end{pmatrix}$:
$$T^i_{\; j} = \begin{pmatrix}
A^1 B_1 & A^1 B_2 & A^1 B_3 \\
A^2 B_1 & A^2 B_2 & A^2 B_3 \\
A^3 B_1 & A^3 B_2 & A^3 B_3
\end{pmatrix} = \begin{pmatrix}
(2)(4) & (2)(1) & (2)(-2) \\
(-1)(4) & (-1)(1) & (-1)(-2) \\
(3)(4) & (3)(1) & (3)(-2)
\end{pmatrix} = \begin{pmatrix}
8 & 2 & -4 \\
-4 & -1 & 2 \\
12 & 3 & -6
\end{pmatrix}$$

---

### 2. Trace Invariant Calculation
The trace is the contraction of the upper index with the lower index:
$$\text{Tr}(T) = T^i_{\; i} = T^1_{\; 1} + T^2_{\; 2} + T^3_{\; 3} = 8 + (-1) + (-6) = 1$$

---

### 3. Comparison with Direct Inner Product
Computing $A^k B_k$:
$$A^k B_k = A^1 B_1 + A^2 B_2 + A^3 B_3 = (2)(4) + (-1)(1) + (3)(-2) = 8 - 1 - 6 = 1$$
The two values coincide identically: $\text{Tr}(T) = A^k B_k = 1$.

---

### 4. Proof of Projector Idempotency Property $S^i_{\; k} S^k_{\; j} = \lambda S^i_{\; j}$
Substitute the dyadic representation $S^i_{\; j} = u^i v_j$:
$$S^i_{\; k} S^k_{\; j} = (u^i v_k) (u^k v_j) = u^i (v_k u^k) v_j$$
Since $v_k u^k = \lambda$ is a scalar number (an invariant scalar contraction):
$$S^i_{\; k} S^k_{\; j} = \lambda (u^i v_j) = \lambda S^i_{\; j}$$
where the eigenvalue scalar factor is precisely:
$$\lambda = u^k v_k = \text{Tr}(S) \blacksquare$$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 2.2: Comprehensive Proof of the Quotient Law for Rank-2 Mixed Tensors",
                "statement": r"""Let $Q^i_{\; j}$ be a set of $n^2$ functions defined in every coordinate system.
Suppose that for every arbitrary contravariant vector $v^j$, the contraction:
$$w^i = Q^i_{\; j} v^j$$
transforms as a **contravariant vector** under all regular coordinate transformations $x^k \to \bar{x}^k$.

1. Formulate the explicit transformation laws for $v^j$ and $w^i$.
2. Prove rigorously that $Q^i_{\; j}$ must transform as a **mixed tensor of rank $(1, 1)$**:
   $$\bar{Q}^i_{\; j} = \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial x^q}{\partial \bar{x}^j} Q^p_{\; q}$$
3. State whether the theorem remains valid if the vector $v^j$ is NOT completely arbitrary, and justify with a counterexample.""",
                "hints": [
                    "Express $\\bar{w}^i = \\frac{\\partial \\bar{x}^i}{\\partial x^p} w^p = \\frac{\\partial \\bar{x}^i}{\\partial x^p} Q^p_{\\; q} v^q$.",
                    "Also express $\\bar{w}^i = \\bar{Q}^i_{\\; j} \\bar{v}^j = \\bar{Q}^i_{\\; j} \\frac{\\partial \\bar{x}^j}{\\partial x^q} v^q$.",
                    "Equate both expressions and use the fact that $v^q$ is arbitrary."
                ],
                "solution": r"""### 1. Transformation Laws of Vectors $v^j$ and $w^i$
Since $v^j$ and $w^i$ are contravariant vectors, under $x^k \to \bar{x}^k$:
$$\bar{v}^j = \frac{\partial \bar{x}^j}{\partial x^q} v^q$$
$$\bar{w}^i = \frac{\partial \bar{x}^i}{\partial x^p} w^p$$

---

### 2. Proof that $Q^i_{\; j}$ is a Mixed Tensor
In the new coordinate system, by definition of the relationship:
$$\bar{w}^i = \bar{Q}^i_{\; j} \bar{v}^j$$
Substitute the transformation of $\bar{v}^j$:
$$\bar{w}^i = \bar{Q}^i_{\; j} \left( \frac{\partial \bar{x}^j}{\partial x^q} v^q \right) = \left( \bar{Q}^i_{\; j} \frac{\partial \bar{x}^j}{\partial x^q} \right) v^q \quad \text{--- (Equation A)}$$

On the other hand, using the vector transformation of $w^p = Q^p_{\; q} v^q$:
$$\bar{w}^i = \frac{\partial \bar{x}^i}{\partial x^p} w^p = \frac{\partial \bar{x}^i}{\partial x^p} (Q^p_{\; q} v^q) = \left( \frac{\partial \bar{x}^i}{\partial x^p} Q^p_{\; q} \right) v^q \quad \text{--- (Equation B)}$$

Subtracting Equation B from Equation A:
$$\left( \bar{Q}^i_{\; j} \frac{\partial \bar{x}^j}{\partial x^q} - \frac{\partial \bar{x}^i}{\partial x^p} Q^p_{\; q} \right) v^q = 0$$

Because the vector $v^q$ is **arbitrary**, we may set $v^q = \delta^q_k$ for any chosen index $k \in \{1, 2, \dots, n\}$.
This isolates the bracketed term for each individual $k$:
$$\bar{Q}^i_{\; j} \frac{\partial \bar{x}^j}{\partial x^k} - \frac{\partial \bar{x}^i}{\partial x^p} Q^p_{\; k} = 0 \implies \bar{Q}^i_{\; j} \frac{\partial \bar{x}^j}{\partial x^k} = \frac{\partial \bar{x}^i}{\partial x^p} Q^p_{\; k}$$

To solve for $\bar{Q}^i_{\; m}$, multiply both sides by $\frac{\partial x^k}{\partial \bar{x}^m}$ and sum over $k$:
$$\bar{Q}^i_{\; j} \left( \frac{\partial \bar{x}^j}{\partial x^k} \frac{\partial x^k}{\partial \bar{x}^m} \right) = \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial x^k}{\partial \bar{x}^m} Q^p_{\; k}$$
By the chain rule identity, $\frac{\partial \bar{x}^j}{\partial x^k} \frac{\partial x^k}{\partial \bar{x}^m} = \delta^j_m$:
$$\bar{Q}^i_{\; j} \delta^j_m = \bar{Q}^i_{\; m} = \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial x^k}{\partial \bar{x}^m} Q^p_{\; k}$$
Relabeling dummy index $k \to q$ and free index $m \to j$:
$$\bar{Q}^i_{\; j} = \frac{\partial \bar{x}^i}{\partial x^p} \frac{\partial x^q}{\partial \bar{x}^j} Q^p_{\; q}$$
This is precisely the defining transformation law of a mixed tensor of rank $(1, 1)$. $\blacksquare$

---

### 3. Critical Importance of the Arbitrary Vector Hypothesis
If $v^j$ is **not arbitrary** (for example, if $v^j$ is restricted to a fixed constant vector or a single subspace), the quotient law **fails completely**.
*Counterexample:*
Suppose $Q_{ij} u^i u^j = 0$ for a single specific vector $u^i = (1, 0, \dots, 0)$. This merely implies $Q_{11} = 0$ in that coordinate system, providing zero information about the remaining components, and certainly does not force $Q_{ij}$ to transform as a tensor. Arbitrariness across the entire vector space is strictly necessary to deduce equality of the component coefficients. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 2.3: Irreducible Decomposition & The Levi-Civita Alternating Tensor",
                "statement": r"""1. Prove that for any rank-2 tensor $T_{ij}$, its contraction with an arbitrary symmetric tensor $S^{ij} = S^{ji}$ satisfies:
   $$T_{ij} S^{ij} = T_{(ij)} S^{ij}$$
   and its contraction with an arbitrary antisymmetric tensor $A^{ij} = -A^{ji}$ satisfies:
   $$T_{ij} A^{ij} = T_{[ij]} A^{ij}$$
2. Prove that the contraction of any symmetric tensor with any antisymmetric tensor vanishes identically:
   $$S_{ij} A^{ij} = 0$$
3. In a 3-dimensional Riemannian space with metric determinant $g = \det(g_{ij}) > 0$, define the Levi-Civita permutation symbol $\epsilon_{ijk}$.
   Prove that the quantity:
   $$e_{ijk} = \sqrt{g} \, \epsilon_{ijk}$$
   transforms as a **true covariant tensor of rank 3** (the Levi-Civita alternating tensor).""",
                "hints": [
                    "Decompose $T_{ij} = T_{(ij)} + T_{[ij]}$ and expand the contraction.",
                    "For part 2, swap dummy indices $i \\leftrightarrow j$ and use $S_{ji} = S_{ij}$ and $A^{ji} = -A^{ij}$.",
                    "Recall that $\\det(A) \\epsilon_{ijk} = \\epsilon_{pqr} A^p_i A^q_j A^r_k$ and the transformation law of the metric determinant $\\bar{g} = J^{-2} g$."
                ],
                "solution": r"""### 1. Contraction with Symmetric and Antisymmetric Tensors
Decompose $T_{ij}$ into symmetric and antisymmetric parts:
$$T_{ij} = T_{(ij)} + T_{[ij]}$$
where $T_{(ij)} = \frac{1}{2}(T_{ij} + T_{ji})$ and $T_{[ij]} = \frac{1}{2}(T_{ij} - T_{ji})$.

#### Contraction with $S^{ij} = S^{ji}$:
$$T_{ij} S^{ij} = (T_{(ij)} + T_{[ij]}) S^{ij} = T_{(ij)} S^{ij} + T_{[ij]} S^{ij}$$
We will show below that $T_{[ij]} S^{ij} = 0$. Therefore:
$$T_{ij} S^{ij} = T_{(ij)} S^{ij}$$

#### Contraction with $A^{ij} = -A^{ji}$:
$$T_{ij} A^{ij} = (T_{(ij)} + T_{[ij]}) A^{ij} = T_{(ij)} A^{ij} + T_{[ij]} A^{ij} = 0 + T_{[ij]} A^{ij} = T_{[ij]} A^{ij}$$

---

### 2. Proof that $S_{ij} A^{ij} = 0$
Let $X = S_{ij} A^{ij}$, where $S_{ij} = S_{ji}$ and $A^{ij} = -A^{ji}$.
Since $i$ and $j$ are dummy summation indices, interchange their names ($i \leftrightarrow j$):
$$X = S_{ji} A^{ji}$$
Now use the symmetry of $S$ and antisymmetry of $A$:
$$S_{ji} = S_{ij}, \qquad A^{ji} = -A^{ij}$$
Substituting these into $X$:
$$X = S_{ij} (-A^{ij}) = -S_{ij} A^{ij} = -X$$
This implies:
$$X = -X \implies 2X = 0 \implies X = 0$$
Thus, the contraction of any symmetric tensor with any antisymmetric tensor is **identically zero**:
$$S_{ij} A^{ij} \equiv 0 \blacksquare$$

---

### 3. Proof that $e_{ijk} = \sqrt{g} \epsilon_{ijk}$ is a True Covariant Tensor

#### Step A: Transformation of the Permutation Symbol
By the definition of the matrix determinant:
$$\det(M) \epsilon_{ijk} = \epsilon_{pqr} M^p_{\; i} M^q_{\; j} M^r_{\; k}$$
Applying this to the Jacobian transformation matrix $M^p_{\; i} = \frac{\partial x^p}{\partial \bar{x}^i}$:
$$\det\left( \frac{\partial x}{\partial \bar{x}} \right) \bar{\epsilon}_{ijk} = \epsilon_{pqr} \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} \frac{\partial x^r}{\partial \bar{x}^k}$$
Recall that the Jacobian determinant is $J = \det\left(\frac{\partial x}{\partial \bar{x}}\right)$.
Therefore:
$$\bar{\epsilon}_{ijk} = \frac{1}{J} \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} \frac{\partial x^r}{\partial \bar{x}^k} \epsilon_{pqr} \quad \text{--- (Equation 1)}$$

#### Step B: Transformation of the Metric Determinant $g$
The metric tensor transforms as a rank-$(0, 2)$ covariant tensor:
$$\bar{g}_{ij} = \frac{\partial x^a}{\partial \bar{x}^i} \frac{\partial x^b}{\partial \bar{x}^j} g_{ab}$$
Taking determinants of both sides:
$$\det(\bar{g}) = \det\left(\frac{\partial x}{\partial \bar{x}}\right) \det(g) \det\left(\frac{\partial x}{\partial \bar{x}}\right) = J^2 g$$
Taking the positive square root:
$$\sqrt{\bar{g}} = |J| \sqrt{g} = J \sqrt{g} \quad (\text{for orientation-preserving transformations } J > 0) \quad \text{--- (Equation 2)}$$

#### Step C: Combining into $e_{ijk} = \sqrt{g} \epsilon_{ijk}$
In the new coordinate system:
$$\bar{e}_{ijk} = \sqrt{\bar{g}} \, \bar{\epsilon}_{ijk}$$
Substitute Equations 1 and 2:
$$\bar{e}_{ijk} = (J \sqrt{g}) \left( \frac{1}{J} \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} \frac{\partial x^r}{\partial \bar{x}^k} \epsilon_{pqr} \right) = \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} \frac{\partial x^r}{\partial \bar{x}^k} (\sqrt{g} \epsilon_{pqr})$$
Since $e_{pqr} = \sqrt{g} \epsilon_{pqr}$, this becomes:
$$\bar{e}_{ijk} = \frac{\partial x^p}{\partial \bar{x}^i} \frac{\partial x^q}{\partial \bar{x}^j} \frac{\partial x^r}{\partial \bar{x}^k} e_{pqr}$$

The Jacobian factor $J$ has canceled out completely!
This is precisely the transformation law of an absolute covariant tensor of rank 3.
Thus, $e_{ijk} = \sqrt{g} \epsilon_{ijk}$ is a **true covariant tensor** (the Levi-Civita volume form). $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u2 = get_unit2()
    print(f"Loaded Unit 2: {u2['title']} with {len(u2['sections'])} sections and {len(u2['problems'])} problems.")
