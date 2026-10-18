# -*- coding: utf-8 -*-
"""
Builder for Linear Algebra Units 1 and 2:
- Unit 1: Vectors in R^n and C^n, Systems of Linear Equations, and Applications
- Unit 2: Algebraic Foundations: Groups, Fields, Vector Spaces & Subspaces
"""
import json

def build_unit_1():
    return {
        "id": "la-u1",
        "title": "Unit 1: Vectors in R^n & C^n, Systems of Linear Equations & Applications",
        "description": "Foundations of Euclidean and complex vector spaces, geometry of R^n and C^n, Cauchy-Schwarz and Minkowski inequalities, Gaussian elimination and Gauss-Jordan reduction to Reduced Row Echelon Form (RREF), consistency criteria, and applied network flow, electrical networks, chemical balancing, and polynomial interpolation.",
        "sections": [
            {
                "id": "u1-sec1",
                "title": "Vectors in Euclidean R^n and Complex C^n Spaces",
                "content": r"""### 1. Vectors in Real Euclidean Space $\mathbb{R}^n$

Let $n$ be a positive integer. The set of all ordered $n$-tuples of real numbers is denoted by $\mathbb{R}^n$:

$$\mathbb{R}^n = \left\{ \vec{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} : x_i \in \mathbb{R}, \; i = 1, 2, \dots, n \right\}$$

Vectors in $\mathbb{R}^n$ admit two fundamental algebraic operations:
1. **Vector Addition:** For $\vec{x}, \vec{y} \in \mathbb{R}^n$,
   $$\vec{x} + \vec{y} = \begin{pmatrix} x_1 + y_1 \\ x_2 + y_2 \\ \vdots \\ x_n + y_n \end{pmatrix}$$
2. **Scalar Multiplication:** For $c \in \mathbb{R}$ and $\vec{x} \in \mathbb{R}^n$,
   $$c\vec{x} = \begin{pmatrix} c x_1 \\ c x_2 \\ \vdots \\ c x_n \end{pmatrix}$$

#### The Standard Euclidean Inner Product (Dot Product)
The standard inner product of $\vec{x}, \vec{y} \in \mathbb{R}^n$ is the scalar:

$$\vec{x} \cdot \vec{y} = \langle \vec{x}, \vec{y} \rangle = \sum_{i=1}^n x_i y_i = \vec{x}^T \vec{y}$$

The **Euclidean Norm (Length)** of $\vec{x}$ is defined by:

$$\|\vec{x}\| = \sqrt{\vec{x} \cdot \vec{x}} = \sqrt{\sum_{i=1}^n x_i^2}$$

The **Euclidean Distance Metric** between two points $\vec{x}, \vec{y} \in \mathbb{R}^n$ is:

$$d(\vec{x}, \vec{y}) = \|\vec{x} - \vec{y}\| = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$

---

### 2. Fundamental Inequalities in $\mathbb{R}^n$

#### Theorem 1.1 (The Cauchy-Schwarz Inequality):
For any vectors $\vec{x}, \vec{y} \in \mathbb{R}^n$:

$$|\vec{x} \cdot \vec{y}| \le \|\vec{x}\| \|\vec{y}\|$$

*Rigorous Proof:*
If $\vec{y} = \vec{0}$, both sides are $0$ and the equality holds trivially. Assume $\vec{y} \ne \vec{0}$. For any real scalar $t \in \mathbb{R}$, consider the squared norm:

$$0 \le \|\vec{x} - t\vec{y}\|^2 = (\vec{x} - t\vec{y}) \cdot (\vec{x} - t\vec{y}) = \|\vec{x}\|^2 - 2t(\vec{x} \cdot \vec{y}) + t^2 \|\vec{y}\|^2$$

This is a non-negative quadratic polynomial $q(t) = A t^2 + B t + C$ where $A = \|\vec{y}\|^2 > 0$, $B = -2(\vec{x} \cdot \vec{y})$, and $C = \|\vec{x}\|^2$. Since $q(t) \ge 0$ for all $t \in \mathbb{R}$, its discriminant $\Delta = B^2 - 4AC$ must be non-positive:

$$\Delta = 4(\vec{x} \cdot \vec{y})^2 - 4 \|\vec{y}\|^2 \|\vec{x}\|^2 \le 0 \implies (\vec{x} \cdot \vec{y})^2 \le \|\vec{x}\|^2 \|\vec{y}\|^2$$

Taking the positive square root of both sides yields $|\vec{x} \cdot \vec{y}| \le \|\vec{x}\| \|\vec{y}\|$. Equality holds if and only if $\vec{x}$ and $\vec{y}$ are linearly dependent. $\blacksquare$

#### Theorem 1.2 (The Triangle / Minkowski Inequality):
For any $\vec{x}, \vec{y} \in \mathbb{R}^n$:

$$\|\vec{x} + \vec{y}\| \le \|\vec{x}\| + \|\vec{y}\|$$

*Proof:*
Expanding the squared norm using the Cauchy-Schwarz inequality:
$$\|\vec{x} + \vec{y}\|^2 = (\vec{x} + \vec{y}) \cdot (\vec{x} + \vec{y}) = \|\vec{x}\|^2 + 2(\vec{x} \cdot \vec{y}) + \|\vec{y}\|^2 \le \|\vec{x}\|^2 + 2\|\vec{x}\|\|\vec{y}\| + \|\vec{y}\|^2 = (\|\vec{x}\| + \|\vec{y}\|)^2$$
Taking square roots on both sides establishes the inequality. $\blacksquare$

---

### 3. Vectors in Complex Space $\mathbb{C}^n$

The set of ordered $n$-tuples of complex numbers is denoted by $\mathbb{C}^n$:

$$\mathbb{C}^n = \left\{ \vec{z} = \begin{pmatrix} z_1 \\ z_2 \\ \vdots \\ z_n \end{pmatrix} : z_k = a_k + i b_k \in \mathbb{C}, \; a_k, b_k \in \mathbb{R} \right\}$$

For $\vec{z} \in \mathbb{C}^n$, its **complex conjugate** is $\overline{\vec{z}} = (\overline{z}_1, \dots, \overline{z}_n)^T$, and its **conjugate transpose (Hermitian adjoint)** is:

$$\vec{z}^* = \vec{z}^H = \overline{\vec{z}}^T = (\overline{z}_1, \overline{z}_2, \dots, \overline{z}_n)$$

#### Standard Inner Product in $\mathbb{C}^n$
To ensure that the norm of a non-zero complex vector is always a positive real number, the inner product in $\mathbb{C}^n$ is defined with complex conjugation:

$$\langle \vec{u}, \vec{v} \rangle = \vec{v}^* \vec{u} = \sum_{k=1}^n u_k \overline{v}_k$$

This inner product satisfies:
1. **Conjugate Symmetry:** $\langle \vec{v}, \vec{u} \rangle = \overline{\langle \vec{u}, \vec{v} \rangle}$
2. **Linearity in First Argument:** $\langle \alpha \vec{u}_1 + \beta \vec{u}_2, \vec{v} \rangle = \alpha \langle \vec{u}_1, \vec{v} \rangle + \beta \langle \vec{u}_2, \vec{v} \rangle$
3. **Conjugate Linearity in Second Argument:** $\langle \vec{u}, \alpha \vec{v}_1 + \beta \vec{v}_2 \rangle = \overline{\alpha} \langle \vec{u}, \vec{v}_1 \rangle + \overline{\beta} \langle \vec{u}, \vec{v}_2 \rangle$
4. **Positive Definiteness:** $\langle \vec{z}, \vec{z} \rangle = \sum_{k=1}^n |z_k|^2 \ge 0$, and $\langle \vec{z}, \vec{z} \rangle = 0 \iff \vec{z} = \vec{0}$

The **Complex Euclidean Norm** is $\|\vec{z}\| = \sqrt{\langle \vec{z}, \vec{z} \rangle} = \sqrt{\sum_{k=1}^n |z_k|^2}$, and the distance metric is $d(\vec{u}, \vec{v}) = \|\vec{u} - \vec{v}\| = \sqrt{\sum_{k=1}^n |u_k - v_k|^2}$."""
            },
            {
                "id": "u1-sec2",
                "title": "Systems of Linear Equations, Gaussian Elimination & RREF",
                "simulation": "sim_la_linear_systems",
                "content": r"""### 1. General System of Linear Equations

A general system of $m$ linear equations in $n$ unknowns $x_1, x_2, \dots, x_n$ over a field $F$ ($\mathbb{R}$ or $\mathbb{C}$) is formulated as:

$$\begin{aligned}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1 \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n &= b_2 \\
&\vdots \\
a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n &= b_m
\end{aligned}$$

In compact matrix notation:

$$A\vec{x} = \vec{b}$$

where $A \in M_{m \times n}(F)$ is the **coefficient matrix**, $\vec{x} \in F^n$ is the **unknown vector**, and $\vec{b} \in F^m$ is the **constant vector**:

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}, \quad \vec{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}$$

The **Augmented Matrix** is denoted by $[A \mid \vec{b}] \in M_{m \times (n+1)}(F)$.

- If $\vec{b} = \vec{0}$, the system $A\vec{x} = \vec{0}$ is **homogeneous**. It always possesses the trivial solution $\vec{x} = \vec{0}$.
- If $\vec{b} \ne \vec{0}$, the system is **non-homogeneous**.

---

### 2. Elementary Row Operations and Row Equivalence

Two augmented matrices are **row equivalent** if one can be transformed into the other via a finite sequence of **Elementary Row Operations (EROs)**:
1. **Row Swap ($R_i \leftrightarrow R_j$):** Interchange rows $i$ and $j$.
2. **Row Scaling ($R_i \to c R_i$):** Multiply row $i$ by a non-zero scalar $c \ne 0$.
3. **Row Addition ($R_i \to R_i + c R_j$):** Add $c$ times row $j$ to row $i$ ($i \ne j$).

Each ERO corresponds to left multiplication by an invertible **elementary matrix** $E \in M_{m \times m}(F)$. Because elementary matrices are invertible, EROs preserve the solution set of the linear system.

---

### 3. Reduced Row Echelon Form (RREF)

A matrix is in **Row Echelon Form (REF)** if:
1. All zero rows are at the bottom of the matrix.
2. The leading entry (first non-zero entry from the left, called the **pivot**) of each non-zero row is strictly to the right of the leading entry of the row above it.
3. All entries in a column below a leading entry are zero.

A matrix is in **Reduced Row Echelon Form (RREF)** if, in addition:
4. The leading entry (pivot) in each non-zero row is strictly equal to $1$.
5. Each column containing a leading $1$ has zeros in all other entries (both above and below the pivot).

#### Theorem 1.3 (Uniqueness of RREF):
Every matrix $A \in M_{m \times n}(F)$ is row-equivalent to one and only one matrix $R$ in Reduced Row Echelon Form: $R = \text{rref}(A)$.

#### Classification of Variables and Solutions:
Let $R = [R_A \mid \vec{d}] = \text{rref}([A \mid \vec{b}])$ have $r$ non-zero rows (pivots):
- **Pivot Variables (Basic Variables):** Unknowns $x_j$ corresponding to columns of $R_A$ containing a pivot $1$.
- **Free Variables:** Unknowns $x_j$ corresponding to columns without pivots. Total free variables = $n - r$.

#### Theorem 1.4 (The Rouché-Capelli Consistency Theorem):
A linear system $A\vec{x} = \vec{b}$ is **consistent** (has at least one solution) if and only if the augmented matrix $[A \mid \vec{b}]$ has the same rank as the coefficient matrix $A$:

$$\text{rank}(A) = \text{rank}([A \mid \vec{b}])$$

Equivalently, the system is consistent if and only if the last column of $\text{rref}([A \mid \vec{b}])$ does not contain a pivot row of the form $(0, 0, \dots, 0 \mid 1)$.
- **Unique Solution:** Consistent and $\text{rank}(A) = n$ (zero free variables).
- **Infinitely Many Solutions:** Consistent and $\text{rank}(A) = r < n$ ($n - r$ free variables).
- **Inconsistent (No Solution):** $\text{rank}([A \mid \vec{b}]) = \text{rank}(A) + 1$."""
            },
            {
                "id": "u1-sec3",
                "title": "Applied Linear Systems: Networks, Circuits, Chemistry & Interpolation",
                "content": r"""### 1. Network Flow Analysis

A directed network consists of a set of junctions (nodes) connected by branches (edges) carrying flow rates $x_1, x_2, \dots, x_k$. The governing physical principle is **Kirchhoff's Flow Conservation Law**:

$$\sum \text{Flow In} = \sum \text{Flow Out} \quad \text{at every junction node}$$

For an urban traffic grid or pipeline network with $m$ nodes and external net inputs/outputs $b_i$:

$$\sum_{j \in \text{incoming}(i)} x_j - \sum_{k \in \text{outgoing}(i)} x_k = b_i \quad (i = 1, \dots, m)$$

This yields a linear system $A\vec{x} = \vec{b}$. Overall network feasibility requires total inflow equals total outflow: $\sum_{i=1}^m b_i = 0$.

---

### 2. Electrical Resistor Networks

Consider an electrical circuit containing resistors and DC voltage sources:
1. **Kirchhoff's Current Law (KCL):** The algebraic sum of currents at any node is zero: $\sum I_{\text{in}} = \sum I_{\text{out}}$.
2. **Kirchhoff's Voltage Law (KVL):** The algebraic sum of voltage changes around any closed loop is zero: $\sum V_{\text{sources}} = \sum I R$.

By defining loop currents $I_1, I_2, \dots, I_L$ (Mesh Current Analysis), KVL produces a symmetric, diagonally dominant linear system:

$$\begin{pmatrix} R_{11} & -R_{12} & \cdots \\ -R_{21} & R_{22} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix} \begin{pmatrix} I_1 \\ I_2 \\ \vdots \end{pmatrix} = \begin{pmatrix} \mathcal{E}_1 \\ \mathcal{E}_2 \\ \vdots \end{pmatrix}$$

Solving via Gauss-Jordan elimination determines all branch currents and power dissipations $P_k = I_k^2 R_k$.

---

### 3. Balancing Chemical Reaction Equations

A chemical reaction preserves the number of atoms of each chemical element. Consider balancing the combustion of propane:

$$x_1 \text{C}_3\text{H}_8 + x_2 \text{O}_2 \to x_3 \text{CO}_2 + x_4 \text{H}_2\text{O}$$

Equating atom counts for Carbon ($\text{C}$), Hydrogen ($\text{H}$), and Oxygen ($\text{O}$):
- $\text{C}: 3x_1 - 1x_3 = 0$
- $\text{H}: 8x_1 - 2x_4 = 0$
- $\text{O}: 2x_2 - 2x_3 - 1x_4 = 0$

This is a homogeneous linear system $A\vec{x} = \vec{0}$ with coefficient matrix:

$$A = \begin{pmatrix} 3 & 0 & -1 & 0 \\ 8 & 0 & 0 & -2 \\ 0 & 2 & -2 & -1 \end{pmatrix}$$

Row reduction to RREF yields:
$$\begin{pmatrix} 1 & 0 & 0 & -1/4 \\ 0 & 1 & 0 & -5/4 \\ 0 & 0 & 1 & -3/4 \end{pmatrix} \implies \begin{cases} x_1 = \frac{1}{4}x_4 \\ x_2 = \frac{5}{4}x_4 \\ x_3 = \frac{3}{4}x_4 \end{cases}$$

Choosing the smallest positive integer for the free variable $x_4 = 4$ gives the unique stoichiometric solution $\vec{x} = (1, 5, 3, 4)^T$:

$$\text{C}_3\text{H}_8 + 5\text{O}_2 \to 3\text{CO}_2 + 4\text{H}_2\text{O}$$

---

### 4. Polynomial Curve Interpolation and the Vandermonde Matrix

Given $n+1$ distinct data points $(t_0, y_0), (t_1, y_1), \dots, (t_n, y_n)$ with $t_i \ne t_j$ for $i \ne j$, there exists a unique polynomial of degree at most $n$:

$$p(t) = c_0 + c_1 t + c_2 t^2 + \cdots + c_n t^n$$

satisfying the interpolation conditions $p(t_i) = y_i$ for all $i = 0, \dots, n$. Setting up the linear system $V\vec{c} = \vec{y}$ reveals the **Vandermonde Matrix** $V$:

$$\begin{pmatrix} 1 & t_0 & t_0^2 & \cdots & t_0^n \\ 1 & t_1 & t_1^2 & \cdots & t_1^n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & t_n & t_n^2 & \cdots & t_n^n \end{pmatrix} \begin{pmatrix} c_0 \\ c_1 \\ \vdots \\ c_n \end{pmatrix} = \begin{pmatrix} y_0 \\ y_1 \\ \vdots \\ y_n \end{pmatrix}$$

#### Theorem 1.5 (Vandermonde Determinant Identity):
$$\det(V) = \prod_{0 \le j < i \le n} (t_i - t_j)$$

Since the interpolation nodes $t_i$ are pairwise distinct, $t_i - t_j \ne 0$ for all $i > j$. Consequently, $\det(V) \ne 0$, proving that $V$ is invertible and the interpolating polynomial $p(t)$ exists and is strictly unique."""
            }
        ],
        "problems": [
            {
                "id": "la-prob-1-1",
                "difficulty": "Easy",
                "difficultyLabel": "Tier 1: Foundational",
                "title": "Complete Gauss-Jordan Reduction & Parametric Vector Solution",
                "statement": r"""Solve the following non-homogeneous system of linear equations in four variables over $\mathbb{R}$ using elementary row operations and Gauss-Jordan elimination:

$$\begin{aligned}
x_1 - 2x_2 + x_3 + 3x_4 &= 2 \\
2x_1 - 4x_2 + 3x_3 + 8x_4 &= 7 \\
-x_1 + 2x_2 + 2x_3 + 3x_4 &= 7
\end{aligned}$$

Find the Reduced Row Echelon Form (RREF) of the augmented matrix, identify the pivot and free variables, and express the general solution in parametric vector form.""",
                "solution": r"""**Step 1: Set up the augmented matrix $[A \mid \vec{b}]$:**
$$[A \mid \vec{b}] = \begin{pmatrix} 1 & -2 & 1 & 3 & 2 \\ 2 & -4 & 3 & 8 & 7 \\ -1 & 2 & 2 & 3 & 7 \end{pmatrix}$$

**Step 2: Eliminate entries below pivot in Column 1:**
Apply $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 + R_1$:
- Row 2: $(2 - 2, \; -4 - 2(-2), \; 3 - 2(1), \; 8 - 2(3), \; 7 - 2(2)) = (0, 0, 1, 2, 3)$
- Row 3: $(-1 + 1, \; 2 - 2, \; 2 + 1, \; 3 + 3, \; 7 + 2) = (0, 0, 3, 6, 9)$

The matrix becomes:
$$\begin{pmatrix} 1 & -2 & 1 & 3 & 2 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 3 & 6 & 9 \end{pmatrix}$$

**Step 3: Eliminate entries in Column 3 to achieve RREF:**
Apply $R_3 \to R_3 - 3R_2$:
- Row 3: $(0, 0, 3 - 3, \; 6 - 6, \; 9 - 9) = (0, 0, 0, 0, 0)$

Apply $R_1 \to R_1 - R_2$:
- Row 1: $(1, -2, \; 1 - 1, \; 3 - 2, \; 2 - 3) = (1, -2, 0, 1, -1)$

The resulting matrix is in Reduced Row Echelon Form:
$$\text{rref}([A \mid \vec{b}]) = \begin{pmatrix} 1 & -2 & 0 & 1 & -1 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$

**Step 4: Identify pivots and free variables:**
- Pivots are located in columns 1 and 3. Therefore, $x_1$ and $x_3$ are **basic (pivot) variables**.
- Columns 2 and 4 contain no pivots. Therefore, $x_2$ and $x_4$ are **free variables**. Let $x_2 = s$ and $x_4 = t$ where $s, t \in \mathbb{R}$.

From Row 1: $x_1 - 2s + t = -1 \implies x_1 = -1 + 2s - t$.  
From Row 2: $x_3 + 2t = 3 \implies x_3 = 3 - 2t$.

**Step 5: Write the solution in parametric vector form:**
$$\vec{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} -1 + 2s - t \\ s \\ 3 - 2t \\ t \end{pmatrix} = \begin{pmatrix} -1 \\ 0 \\ 3 \\ 0 \end{pmatrix} + s \begin{pmatrix} 2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ -2 \\ 1 \end{pmatrix}$$""",
                "answer": r"""$\text{rref}([A \mid \vec{b}]) = \begin{pmatrix} 1 & -2 & 0 & 1 & -1 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$. The general solution is $\vec{x} = \vec{x}_p + s\vec{v}_1 + t\vec{v}_2 = \begin{pmatrix} -1 \\ 0 \\ 3 \\ 0 \end{pmatrix} + s \begin{pmatrix} 2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ -2 \\ 1 \end{pmatrix}$ for all $s, t \in \mathbb{R}$."""
            },
            {
                "id": "la-prob-1-2",
                "difficulty": "Medium",
                "difficultyLabel": "Tier 2: Intermediate Exam",
                "title": "Network Flow & Resistor Loop Conservation",
                "statement": r"""A traffic network has four intersections $A, B, C, D$ connected by one-way streets with traffic flows $x_1, x_2, x_3, x_4, x_5$ (measured in vehicles/hour):
- Node $A$: Inflow of $400$ enters; flows $x_1$ (to $B$) and $x_2$ (to $C$) leave.
- Node $B$: Inflow $x_1$ arrives; flows $x_3$ (to $D$) and external outflow of $250$ leave.
- Node $C$: Inflow $x_2$ arrives along with external inflow of $150$; flow $x_4$ (to $D$) and $x_5$ leave.
- Node $D$: Inflows $x_3$ and $x_4$ arrive; external outflow of $300$ leaves.

(a) Set up the linear system balancing inflow and outflow at every intersection.  
(b) Solve the system to determine the general flow vector.  
(c) If the road segment $CD$ is closed ($x_4 = 0$), determine the required flows on all remaining streets to avoid traffic congestion.""",
                "solution": r"""**Step 1: Write node conservation equations ($\text{Inflow} = \text{Outflow}$):**
- At Node $A$: $400 = x_1 + x_2 \implies x_1 + x_2 = 400$
- At Node $B$: $x_1 = x_3 + 250 \implies x_1 - x_3 = 250$
- At Node $C$: $x_2 + 150 = x_4 + x_5 \implies x_2 - x_4 - x_5 = -150$
- At Node $D$: $x_3 + x_4 = 300 \implies x_3 + x_4 = 300$

**Step 2: Construct the augmented matrix and row reduce:**
$$\begin{pmatrix} 1 & 1 & 0 & 0 & 0 & 400 \\ 1 & 0 & -1 & 0 & 0 & 250 \\ 0 & 1 & 0 & -1 & -1 & -150 \\ 0 & 0 & 1 & 1 & 0 & 300 \end{pmatrix}$$

Apply $R_2 \to R_2 - R_1$:
$$\begin{pmatrix} 1 & 1 & 0 & 0 & 0 & 400 \\ 0 & -1 & -1 & 0 & 0 & -150 \\ 0 & 1 & 0 & -1 & -1 & -150 \\ 0 & 0 & 1 & 1 & 0 & 300 \end{pmatrix}$$

Apply $R_2 \to -R_2$, then $R_3 \to R_3 - R_2$ and $R_1 \to R_1 - R_2$:
- $R_2 = (0, 1, 1, 0, 0, 150)$
- $R_1 = (1, 0, -1, 0, 0, 250)$
- $R_3 = (0, 0, -1, -1, -1, -300) \implies (0, 0, 1, 1, 1, 300)$

Now with $R_3 = (0, 0, 1, 1, 1, 300)$, apply $R_4 \to R_4 - R_3$:
- $R_4 = (0, 0, 0, 0, -1, 0) \implies x_5 = 0$ !
- $R_1 \to R_1 + R_3 = (1, 0, 0, 1, 1, 550) \implies x_1 + x_4 + x_5 = 550$
- $R_2 \to R_2 - R_3 = (0, 1, 0, -1, -1, -150) \implies x_2 - x_4 - x_5 = -150$

Since $x_5 = 0$:
$$x_1 = 550 - x_4, \quad x_2 = -150 + x_4, \quad x_3 = 300 - x_4, \quad x_5 = 0$$

Check at $A$: $x_1 + x_2 = (550 - x_4) + (x_4 - 150) = 400$. Conserved!

**Step 3: Analyze segment closure $x_4 = 0$:**
If $x_4 = 0$, then $x_2 = -150 < 0$. But one-way street flows must satisfy $x_i \ge 0$.  
For $x_2 \ge 0$, we require $x_4 \ge 150$. For $x_3 \ge 0$, $x_4 \le 300$.  
Thus, closing road $CD$ ($x_4 = 0$) causes an impossible bottleneck without reversing flow direction on $AC$.""",
                "answer": r"""General flow: $x_1 = 550 - x_4$, $x_2 = x_4 - 150$, $x_3 = 300 - x_4$, $x_5 = 0$, with $150 \le x_4 \le 300$. Setting $x_4 = 0$ violates non-negativity ($x_2 = -150$), proving $CD$ cannot be closed without grid gridlock."""
            },
            {
                "id": "la-prob-1-3",
                "difficulty": "Hard",
                "difficultyLabel": "Tier 3: Honors / Proof Challenge",
                "title": "Vandermonde Determinant & Polynomial Interpolation Uniqueness",
                "statement": r"""Prove rigorously by induction on $n \ge 1$ that the determinant of the $(n+1) \times (n+1)$ Vandermonde matrix:

$$V_n = \begin{pmatrix} 1 & t_0 & t_0^2 & \cdots & t_0^n \\ 1 & t_1 & t_1^2 & \cdots & t_1^n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & t_n & t_n^2 & \cdots & t_n^n \end{pmatrix}$$

satisfies the product formula $\det(V_n) = \prod_{0 \le j < i \le n} (t_i - t_j)$. Then, deduce that if the nodes $t_0, t_1, \dots, t_n \in F$ are distinct, there exists a unique polynomial $p(t) \in F[t]$ of degree $\le n$ passing through any prescribed points $(t_i, y_i)$. Explain the connection to the Lagrange interpolation formula.""",
                "solution": r"""**Step 1: Base Case $n = 1$:**
$$V_1 = \begin{pmatrix} 1 & t_0 \\ 1 & t_1 \end{pmatrix} \implies \det(V_1) = 1 \cdot t_1 - 1 \cdot t_0 = t_1 - t_0 = \prod_{0 \le j < i \le 1} (t_i - t_j)$$
The base case holds.

**Step 2: Inductive Step:**
Assume the formula holds for size $n$, i.e., for any $n$ distinct nodes, $\det(V_{n-1}) = \prod_{0 \le j < i \le n-1} (t_i - t_j)$.

To compute $\det(V_n)$, perform elementary column operations from right to left: subtract $t_0$ times column $k-1$ from column $k$, for $k = n+1, n, \dots, 2$:
$$C_k \to C_k - t_0 C_{k-1}$$

These column operations do not alter the determinant ($\det(V_n)$ is invariant).
In the first row, every entry from column $2$ onward becomes:
$$t_0^k - t_0 t_0^{k-1} = 0$$
Thus, the first row becomes $(1, 0, 0, \dots, 0)$.

For row $i$ ($i \ge 1$), entry in column $k$ becomes:
$$t_i^k - t_0 t_i^{k-1} = (t_i - t_0) t_i^{k-1}$$

Expanding $\det(V_n)$ along the first row:
$$\det(V_n) = 1 \cdot \det \begin{pmatrix} (t_1 - t_0) & (t_1 - t_0)t_1 & \cdots & (t_1 - t_0)t_1^{n-1} \\ (t_2 - t_0) & (t_2 - t_0)t_2 & \cdots & (t_2 - t_0)t_2^{n-1} \\ \vdots & \vdots & \ddots & \vdots \\ (t_n - t_0) & (t_n - t_0)t_n & \cdots & (t_n - t_0)t_n^{n-1} \end{pmatrix}$$

Factor out the common scalar $(t_i - t_0)$ from each row $i = 1, 2, \dots, n$:
$$\det(V_n) = \left( \prod_{i=1}^n (t_i - t_0) \right) \cdot \det \begin{pmatrix} 1 & t_1 & \cdots & t_1^{n-1} \\ 1 & t_2 & \cdots & t_2^{n-1} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & t_n & \cdots & t_n^{n-1} \end{pmatrix}$$

The remaining matrix is precisely $V_{n-1}$ for the nodes $(t_1, t_2, \dots, t_n)$. By the induction hypothesis:
$$\det(V_{n-1}) = \prod_{1 \le j < i \le n} (t_i - t_j)$$

Multiplying this by $\prod_{i=1}^n (t_i - t_0)$ includes all terms where $j = 0$:
$$\det(V_n) = \prod_{0 \le j < i \le n} (t_i - t_j)$$
The induction is complete.

**Step 3: Uniqueness of Interpolating Polynomial:**
Since nodes $t_0, \dots, t_n$ are pairwise distinct, $t_i - t_j \ne 0$ for all $i > j$, so $\det(V_n) \ne 0$. Hence $V_n$ is non-singular and invertible. The linear system $V_n \vec{c} = \vec{y}$ has the unique solution $\vec{c} = V_n^{-1} \vec{y}$, establishing the existence and uniqueness of $p(t) \in \mathbb{P}_n$.

In the Lagrange basis $\ell_i(t) = \prod_{j \ne i} \frac{t - t_j}{t_i - t_j}$, the unique polynomial is expressed directly as $p(t) = \sum_{i=0}^n y_i \ell_i(t)$, avoiding explicit matrix inversion.""",
                "answer": r"""$\det(V_n) = \prod_{0 \le j < i \le n} (t_i - t_j)$. Since $t_i \ne t_j$ for $i \ne j$, $\det(V_n) \ne 0$, which guarantees $V_n$ is invertible, proving the interpolating polynomial $p(t)$ of degree $\le n$ is strictly unique."""
            }
        ]
    }

def build_unit_2():
    return {
        "id": "la-u2",
        "title": "Unit 2: Algebraic Foundations: Groups, Fields, Vector Spaces & Subspaces",
        "description": "Abstract algebraic structures, groups, fields (R, C, Z_p), vector space axioms over arbitrary fields, function and matrix spaces, subspace criteria, intersection, sum, and direct sum decompositions.",
        "sections": [
            {
                "id": "u2-sec1",
                "title": "Abstract Algebraic Foundations: Groups, Rings, and Fields",
                "content": r"""### 1. The Concept of a Group

A **Group** is an algebraic structure $(G, *)$ consisting of a non-empty set $G$ together with a binary operation $*: G \times G \to G$ satisfying the following four axioms:
1. **Closure:** For all $a, b \in G$, $a * b \in G$.
2. **Associativity:** For all $a, b, c \in G$, $(a * b) * c = a * (b * c)$.
3. **Identity Element:** There exists an element $e \in G$ such that for every $a \in G$:
   $$a * e = e * a = a$$
4. **Inverse Element:** For each $a \in G$, there exists an element $a^{-1} \in G$ such that:
   $$a * a^{-1} = a^{-1} * a = e$$

If, in addition, the operation satisfies **commutativity**:
$$a * b = b * a \quad \forall a, b \in G$$
then $(G, *)$ is called an **Abelian (Commutative) Group**.

---

### 2. Rings and Fields

#### Definition of a Field
A **Field** $(F, +, \cdot)$ is a set $F$ equipped with two binary operations called **addition** ($+$) and **multiplication** ($\cdot$) such that:
1. $(F, +)$ is an abelian group with additive identity denoted by $0$ and additive inverse of $a$ denoted by $-a$.
2. $(F \setminus \{0\}, \cdot)$ is an abelian group with multiplicative identity denoted by $1$ ($1 \ne 0$) and multiplicative inverse of $a \ne 0$ denoted by $a^{-1}$ or $1/a$.
3. **Distributivity:** Multiplication distributes over addition:
   $$a \cdot (b + c) = a \cdot b + a \cdot c \quad \forall a, b, c \in F$$

#### Canonical Examples of Fields:
- The field of rational numbers $(\mathbb{Q}, +, \cdot)$.
- The field of real numbers $(\mathbb{R}, +, \cdot)$.
- The field of complex numbers $(\mathbb{C}, +, \cdot)$.
- The finite Galois field of prime order $(\mathbb{Z}_p, +, \cdot)$ where $p$ is prime and arithmetic is modulo $p$.
- Note: The integers $\mathbb{Z}$ do **not** form a field because non-zero integers other than $\pm 1$ do not possess multiplicative inverses in $\mathbb{Z}$.

#### Fundamental Field Properties:
From these axioms, several universal properties follow:
- $0 \cdot a = 0$ for all $a \in F$.
- $(-a) \cdot b = -(a \cdot b) = a \cdot (-b)$ for all $a, b \in F$.
- If $a \cdot b = 0$, then either $a = 0$ or $b = 0$ (no zero divisors)."""
            },
            {
                "id": "u2-sec2",
                "title": "Axiomatic Vector Spaces over an Arbitrary Field",
                "simulation": "sim_la_subspaces",
                "content": r"""### 1. Axiomatic Definition of a Vector Space

Let $F$ be a field (whose elements are called **scalars**). A **Vector Space** over $F$ is a non-empty set $V$ (whose elements are called **vectors**), equipped with two operations:
1. **Vector Addition:** $+ : V \times V \to V$, assigning to each pair $(\vec{u}, \vec{v})$ a vector $\vec{u} + \vec{v} \in V$.
2. **Scalar Multiplication:** $\cdot : F \times V \to V$, assigning to each pair $(c, \vec{v})$ a vector $c\vec{v} \in V$.

such that for all $\vec{u}, \vec{v}, \vec{w} \in V$ and all $c, d \in F$, the following **eight axioms** are satisfied:

#### Axioms of Addition (Abelian Group $(V, +)$):
1. **A1 (Commutativity):** $\vec{u} + \vec{v} = \vec{v} + \vec{u}$
2. **A2 (Associativity):** $(\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})$
3. **A3 (Additive Identity):** There exists a vector $\vec{0} \in V$ such that $\vec{v} + \vec{0} = \vec{v}$ for all $\vec{v} \in V$.
4. **A4 (Additive Inverse):** For every $\vec{v} \in V$, there exists a vector $-\vec{v} \in V$ such that $\vec{v} + (-\vec{v}) = \vec{0}$.

#### Axioms of Scalar Multiplication:
5. **M1 (Distributivity over Vector Addition):** $c(\vec{u} + \vec{v}) = c\vec{u} + c\vec{v}$
6. **M2 (Distributivity over Scalar Addition):** $(c + d)\vec{v} = c\vec{v} + d\vec{v}$
7. **M3 (Compatibility of Scalar Multiplication):** $c(d\vec{v}) = (cd)\vec{v}$
8. **M4 (Scalar Identity):** $1\vec{v} = \vec{v}$, where $1 \in F$ is the multiplicative identity of $F$.

---

### 2. Canonical Examples of Vector Spaces

1. **Coordinate Spaces $F^n$:** Column vectors of length $n$ with entries in $F$.
2. **Matrix Spaces $M_{m \times n}(F)$:** The set of all $m \times n$ matrices with entries in $F$ under standard matrix addition and scalar multiplication.
3. **Polynomial Spaces $\mathbb{P}_n(F)$ and $\mathbb{P}(F)$:** The set $\mathbb{P}_n(F) = \{a_0 + a_1 t + \cdots + a_n t^n : a_i \in F\}$ of polynomials of degree $\le n$.
4. **Function Spaces $C[a, b]$:** The set of all continuous real-valued functions $f: [a, b] \to \mathbb{R}$ with $(f + g)(t) = f(t) + g(t)$ and $(cf)(t) = c f(t)$.
5. **Sequence Spaces $\ell^2$ and $\ell^\infty$:** The set of infinite sequences $(x_1, x_2, \dots)$ with $\sum |x_i|^2 < \infty$."""
            },
            {
                "id": "u2-sec3",
                "title": "Subspaces, Intersections, Sums & Direct Sum Decompositions",
                "content": r"""### 1. Vector Subspaces

Let $V$ be a vector space over field $F$. A subset $W \subseteq V$ is a **subspace** of $V$ (written $W \le V$) if $W$ is itself a vector space over $F$ under the operations of addition and scalar multiplication inherited from $V$.

#### Theorem 2.1 (The Subspace Criterion / Two-Step Test):
A non-empty subset $W \subseteq V$ is a subspace of $V$ if and only if:
1. **Contains Zero:** $\vec{0} \in W$.
2. **Closure under Addition:** For all $\vec{u}, \vec{v} \in W$, $\vec{u} + \vec{v} \in W$.
3. **Closure under Scalar Multiplication:** For all $c \in F$ and $\vec{u} \in W$, $c\vec{u} \in W$.

Equivalently (One-Step Test): $W \ne \emptyset$ and for all $c, d \in F$ and $\vec{u}, \vec{v} \in W$, $c\vec{u} + d\vec{v} \in W$.

---

### 2. Intersection and Sum of Subspaces

Let $W_1$ and $W_2$ be subspaces of $V$.

#### Theorem 2.2 (Intersection of Subspaces):
The intersection $W_1 \cap W_2 = \{\vec{v} \in V : \vec{v} \in W_1 \text{ and } \vec{v} \in W_2\}$ is always a subspace of $V$.

*Proof:*
1. Since $\vec{0} \in W_1$ and $\vec{0} \in W_2$, $\vec{0} \in W_1 \cap W_2$.
2. If $\vec{u}, \vec{v} \in W_1 \cap W_2$, then $\vec{u}, \vec{v} \in W_1 \implies \vec{u} + \vec{v} \in W_1$, and $\vec{u}, \vec{v} \in W_2 \implies \vec{u} + \vec{v} \in W_2$. Thus $\vec{u} + \vec{v} \in W_1 \cap W_2$.
3. If $c \in F$ and $\vec{u} \in W_1 \cap W_2$, then $c\vec{u} \in W_1$ and $c\vec{u} \in W_2$, so $c\vec{u} \in W_1 \cap W_2$. $\blacksquare$

*Warning on Unions:* The union $W_1 \cup W_2$ is **generally not a subspace** unless one subspace is completely contained in the other ($W_1 \subseteq W_2$ or $W_2 \subseteq W_1$).

#### Definition: Sum of Subspaces
The sum of two subspaces $W_1, W_2$ is defined by:

$$W_1 + W_2 = \{\vec{w}_1 + \vec{w}_2 : \vec{w}_1 \in W_1, \; \vec{w}_2 \in W_2\}$$

$W_1 + W_2$ is the smallest subspace of $V$ containing both $W_1$ and $W_2$.

---

### 3. Direct Sums and Uniqueness of Decomposition

The sum $W_1 + W_2$ is called an **Internal Direct Sum**, denoted by:

$$V = W_1 \oplus W_2$$

if every vector $\vec{v} \in V$ can be written **uniquely** as $\vec{v} = \vec{w}_1 + \vec{w}_2$ with $\vec{w}_1 \in W_1$ and $\vec{w}_2 \in W_2$.

#### Theorem 2.3 (Direct Sum Equivalence Theorem):
Let $W_1, W_2$ be subspaces of $V$. Then $V = W_1 \oplus W_2$ if and only if:
1. $V = W_1 + W_2$, and
2. $W_1 \cap W_2 = \{\vec{0}\}$.

*Proof:*
$(\implies)$ Assume $V = W_1 \oplus W_2$. Then $V = W_1 + W_2$ by definition. Suppose $\vec{x} \in W_1 \cap W_2$. Then we can express $\vec{0} \in V$ in two ways:
$$\vec{0} = \vec{0} + \vec{0} \quad (\vec{0} \in W_1, \vec{0} \in W_2)$$
$$\vec{0} = \vec{x} + (-\vec{x}) \quad (\vec{x} \in W_1, -\vec{x} \in W_2)$$
By the uniqueness of decomposition, we must have $\vec{x} = \vec{0}$. Hence $W_1 \cap W_2 = \{\vec{0}\}$.

$(\impliedby)$ Assume $V = W_1 + W_2$ and $W_1 \cap W_2 = \{\vec{0}\}$. Let $\vec{v} \in V$. Since $V = W_1 + W_2$, there exist $\vec{w}_1 \in W_1$ and $\vec{w}_2 \in W_2$ such that $\vec{v} = \vec{w}_1 + \vec{w}_2$. To prove uniqueness, suppose $\vec{v} = \vec{w}_1' + \vec{w}_2'$ with $\vec{w}_1' \in W_1$ and $\vec{w}_2' \in W_2$. Then:
$$\vec{w}_1 + \vec{w}_2 = \vec{w}_1' + \vec{w}_2' \implies \vec{w}_1 - \vec{w}_1' = \vec{w}_2' - \vec{w}_2$$
The left side is in $W_1$ (since $W_1$ is a subspace), and the right side is in $W_2$. Thus:
$$\vec{w}_1 - \vec{w}_1' \in W_1 \cap W_2 = \{\vec{0}\} \implies \vec{w}_1 = \vec{w}_1' \quad \text{and} \quad \vec{w}_2 = \vec{w}_2'$$
This proves that the decomposition is strictly unique. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "la-prob-2-1",
                "difficulty": "Easy",
                "difficultyLabel": "Tier 1: Foundational",
                "title": "Subspace Verification for Matrix Subsets",
                "statement": r"""Let $V = M_{n \times n}(\mathbb{R})$ be the vector space of all $n \times n$ real matrices. Determine, with complete mathematical justification using the Subspace Criterion, whether each of the following subsets is a subspace of $V$:
(a) $W_1 = \{A \in M_{n \times n}(\mathbb{R}) : A^T = A\}$ (the set of symmetric matrices).  
(b) $W_2 = \{A \in M_{n \times n}(\mathbb{R}) : \det(A) = 0\}$ (the set of singular matrices).  
(c) $W_3 = \{A \in M_{n \times n}(\mathbb{R}) : \text{tr}(A) = 0\}$ (the set of trace-zero matrices).""",
                "solution": r"""**(a) Analysis of $W_1$ (Symmetric Matrices):**
1. **Contains Zero:** The zero matrix $O_{n \times n}$ satisfies $O^T = O$, so $O \in W_1$.
2. **Closure under Addition:** Let $A, B \in W_1$. Then $A^T = A$ and $B^T = B$. Using the linearity of the transpose operation:
   $$(A + B)^T = A^T + B^T = A + B$$
   Thus $A + B \in W_1$.
3. **Closure under Scalar Multiplication:** For $c \in \mathbb{R}$ and $A \in W_1$:
   $$(c A)^T = c (A^T) = c A$$
   Thus $c A \in W_1$.  
Therefore, $W_1$ is a subspace of $M_{n \times n}(\mathbb{R})$.

**(b) Analysis of $W_2$ (Singular Matrices):**
$W_2$ is **NOT** a subspace for $n \ge 2$. While $O \in W_2$ and scalar multiples of singular matrices are singular, $W_2$ is **not closed under addition**.  
*Counterexample for $n = 2$:*
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in W_2 \quad (\det(A) = 0), \qquad B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \in W_2 \quad (\det(B) = 0)$$
However:
$$A + B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2 \implies \det(A + B) = 1 \ne 0 \implies A + B \notin W_2$$
Hence $W_2$ fails closure under addition and is not a subspace.

**(c) Analysis of $W_3$ (Trace-Zero Matrices):**
The trace of a matrix is $\text{tr}(A) = \sum_{i=1}^n a_{ii}$.
1. **Contains Zero:** $\text{tr}(O) = 0$, so $O \in W_3$.
2. **Closure under Addition & Scalar Multiplication:** For $A, B \in W_3$ and $c, d \in \mathbb{R}$:
   $$\text{tr}(c A + d B) = c\,\text{tr}(A) + d\,\text{tr}(B) = c(0) + d(0) = 0$$
   Thus $c A + d B \in W_3$.  
Therefore, $W_3$ is a subspace of $M_{n \times n}(\mathbb{R})$.""",
                "answer": r"""$W_1$ (symmetric matrices) and $W_3$ (trace-zero matrices) are subspaces of $M_{n \times n}(\mathbb{R})$. $W_2$ (singular matrices) is NOT a subspace because it is not closed under addition ($A = \text{diag}(1,0)$ and $B = \text{diag}(0,1)$ both have det 0, but $A+B = I$ has det 1)."""
            },
            {
                "id": "la-prob-2-2",
                "difficulty": "Medium",
                "difficultyLabel": "Tier 2: Intermediate Exam",
                "title": "Direct Sum Decomposition of Symmetric and Skew-Symmetric Matrices",
                "statement": r"""Let $V = M_{n \times n}(\mathbb{R})$. Let $W_{\text{sym}} = \{A \in V : A^T = A\}$ be the subspace of symmetric matrices, and let $W_{\text{skew}} = \{A \in V : A^T = -A\}$ be the subspace of skew-symmetric matrices.

(a) Prove that $W_{\text{sym}} \cap W_{\text{skew}} = \{O\}$.  
(b) Prove that every matrix $A \in V$ can be decomposed into a sum $A = A_{\text{sym}} + A_{\text{skew}}$ with $A_{\text{sym}} \in W_{\text{sym}}$ and $A_{\text{skew}} \in W_{\text{skew}}$.  
(c) Conclude that $M_{n \times n}(\mathbb{R}) = W_{\text{sym}} \oplus W_{\text{skew}}$, and compute the unique decomposition for the matrix:
$$A = \begin{pmatrix} 2 & 5 & -1 \\ 1 & 4 & 6 \\ 3 & -2 & 7 \end{pmatrix}$$""",
                "solution": r"""**Step 1: Prove $W_{\text{sym}} \cap W_{\text{skew}} = \{O\}$:**
Let $A \in W_{\text{sym}} \cap W_{\text{skew}}$.
- Since $A \in W_{\text{sym}}$, $A^T = A$.
- Since $A \in W_{\text{skew}}$, $A^T = -A$.
Therefore:
$$A = -A \implies 2A = O \implies A = O$$
Thus $W_{\text{sym}} \cap W_{\text{skew}} = \{O\}$.

**Step 2: Prove $V = W_{\text{sym}} + W_{\text{skew}}$:**
For any arbitrary matrix $A \in M_{n \times n}(\mathbb{R})$, write:
$$A = \frac{A + A^T}{2} + \frac{A - A^T}{2}$$
Define:
$$A_{\text{sym}} = \frac{1}{2}(A + A^T), \qquad A_{\text{skew}} = \frac{1}{2}(A - A^T)$$

Verify membership:
$$(A_{\text{sym}})^T = \left(\frac{A + A^T}{2}\right)^T = \frac{A^T + (A^T)^T}{2} = \frac{A^T + A}{2} = A_{\text{sym}} \implies A_{\text{sym}} \in W_{\text{sym}}$$
$$(A_{\text{skew}})^T = \left(\frac{A - A^T}{2}\right)^T = \frac{A^T - A}{2} = -\frac{A - A^T}{2} = -A_{\text{skew}} \implies A_{\text{skew}} \in W_{\text{skew}}$$
Since $A = A_{\text{sym}} + A_{\text{skew}}$, every matrix in $V$ is in $W_{\text{sym}} + W_{\text{skew}}$.

**Step 3: Direct Sum Conclusion:**
By Theorem 2.3, since $V = W_{\text{sym}} + W_{\text{skew}}$ and $W_{\text{sym}} \cap W_{\text{skew}} = \{O\}$, we have:
$$M_{n \times n}(\mathbb{R}) = W_{\text{sym}} \oplus W_{\text{skew}}$$

**Step 4: Explicit computation for given matrix $A$:**
$$A = \begin{pmatrix} 2 & 5 & -1 \\ 1 & 4 & 6 \\ 3 & -2 & 7 \end{pmatrix}, \qquad A^T = \begin{pmatrix} 2 & 1 & 3 \\ 5 & 4 & -2 \\ -1 & 6 & 7 \end{pmatrix}$$

$$A_{\text{sym}} = \frac{A + A^T}{2} = \frac{1}{2} \begin{pmatrix} 4 & 6 & 2 \\ 6 & 8 & 4 \\ 2 & 4 & 14 \end{pmatrix} = \begin{pmatrix} 2 & 3 & 1 \\ 3 & 4 & 2 \\ 1 & 2 & 7 \end{pmatrix}$$

$$A_{\text{skew}} = \frac{A - A^T}{2} = \frac{1}{2} \begin{pmatrix} 0 & 4 & -4 \\ -4 & 0 & 8 \\ 4 & -8 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 & -2 \\ -2 & 0 & 4 \\ 2 & -4 & 0 \end{pmatrix}$$
Check: $A_{\text{sym}} + A_{\text{skew}} = \begin{pmatrix} 2+0 & 3+2 & 1-2 \\ 3-2 & 4+0 & 2+4 \\ 1+2 & 2-4 & 7+0 \end{pmatrix} = \begin{pmatrix} 2 & 5 & -1 \\ 1 & 4 & 6 \\ 3 & -2 & 7 \end{pmatrix} = A$. Verified!""",
                "answer": r"""$M_{n \times n}(\mathbb{R}) = W_{\text{sym}} \oplus W_{\text{skew}}$. For the given matrix: $A_{\text{sym}} = \begin{pmatrix} 2 & 3 & 1 \\ 3 & 4 & 2 \\ 1 & 2 & 7 \end{pmatrix}$ and $A_{\text{skew}} = \begin{pmatrix} 0 & 2 & -2 \\ -2 & 0 & 4 \\ 2 & -4 & 0 \end{pmatrix}$."""
            },
            {
                "id": "la-prob-2-3",
                "difficulty": "Hard",
                "difficultyLabel": "Tier 3: Honors / Proof Challenge",
                "title": "Subspace Union Condition: Theorem & Complete Proof",
                "statement": r"""Let $W_1$ and $W_2$ be two vector subspaces of a vector space $V$ over a field $F$.

(a) Prove rigorously that the union $W_1 \cup W_2$ is a subspace of $V$ if and only if either $W_1 \subseteq W_2$ or $W_2 \subseteq W_1$.  
(b) Provide a concrete geometric counterexample in $\mathbb{R}^2$ demonstrating the failure of closure under vector addition when neither subspace contains the other.  
(c) Generalization: If $F$ is an infinite field, prove that a vector space $V$ cannot be written as the union of a finite number of proper subspaces $V = \bigcup_{k=1}^m W_k$ with $W_k \subsetneq V$.""",
                "solution": r"""**Part (a): Proof of Subspace Union Equivalence:**
We wish to prove: $W_1 \cup W_2 \le V \iff W_1 \subseteq W_2 \text{ or } W_2 \subseteq W_1$.

$(\impliedby)$ If $W_1 \subseteq W_2$, then $W_1 \cup W_2 = W_2$. Since $W_2$ is a subspace, $W_1 \cup W_2$ is a subspace. The same holds if $W_2 \subseteq W_1$, where $W_1 \cup W_2 = W_1$.

$(\implies)$ Suppose $W_1 \cup W_2 \le V$. We proceed by contradiction.  
Assume that $W_1 \not\subseteq W_2$ and $W_2 \not\subseteq W_1$.  
Then:
- There exists a vector $\vec{w}_1 \in W_1$ such that $\vec{w}_1 \notin W_2$.
- There exists a vector $\vec{w}_2 \in W_2$ such that $\vec{w}_2 \notin W_1$.

Both $\vec{w}_1, \vec{w}_2 \in W_1 \cup W_2$. Since $W_1 \cup W_2$ is assumed to be a subspace, it must be closed under addition:
$$\vec{w}_1 + \vec{w}_2 \in W_1 \cup W_2$$
This implies that either $\vec{w}_1 + \vec{w}_2 \in W_1$ or $\vec{w}_1 + \vec{w}_2 \in W_2$.

- Case 1: Suppose $\vec{w}_1 + \vec{w}_2 \in W_1$. Since $W_1$ is a subspace and $\vec{w}_1 \in W_1$, $(-\vec{w}_1) \in W_1$. Then:
  $$\vec{w}_2 = (\vec{w}_1 + \vec{w}_2) - \vec{w}_1 \in W_1$$
  This contradicts our premise that $\vec{w}_2 \notin W_1$.
- Case 2: Suppose $\vec{w}_1 + \vec{w}_2 \in W_2$. Since $W_2$ is a subspace and $\vec{w}_2 \in W_2$, $(-\vec{w}_2) \in W_2$. Then:
  $$\vec{w}_1 = (\vec{w}_1 + \vec{w}_2) - \vec{w}_2 \in W_2$$
  This contradicts our premise that $\vec{w}_1 \notin W_2$.

Both cases yield a contradiction. Hence, we must have $W_1 \subseteq W_2$ or $W_2 \subseteq W_1$. $\blacksquare$

**Part (b): Geometric Counterexample in $\mathbb{R}^2$:**
In $\mathbb{R}^2$, let $W_1 = \text{span}\{(1, 0)\} = \{(x, 0) : x \in \mathbb{R}\}$ ($x$-axis) and $W_2 = \text{span}\{(0, 1)\} = \{(0, y) : y \in \mathbb{R}\}$ ($y$-axis). Both are 1D subspaces of $\mathbb{R}^2$.  
$\vec{u} = (1, 0) \in W_1 \subseteq W_1 \cup W_2$ and $\vec{v} = (0, 1) \in W_2 \subseteq W_1 \cup W_2$.  
Their sum is $\vec{u} + \vec{v} = (1, 1)$.  
Since $(1, 1) \notin W_1$ and $(1, 1) \notin W_2$, $(1, 1) \notin W_1 \cup W_2$. Closure under addition fails!

**Part (c): Proof for Union of Finitely Many Subspaces over Infinite Field:**
Let $V = \bigcup_{k=1}^m W_k$ with proper subspaces $W_k \subsetneq V$. Assume $m$ is minimal, so $m \ge 2$ and $V \ne \bigcup_{k \ne j} W_k$.  
Pick $\vec{u} \in W_1 \setminus \bigcup_{k=2}^m W_k$, and pick $\vec{v} \in V \setminus W_1$.  
Consider the infinite family of vectors $\{\vec{v} + c\vec{u} : c \in F\}$. Since $F$ is infinite, this family is infinite.  
If two distinct scalars $c_1 \ne c_2$ give vectors in the same subspace $W_j$:
$$(\vec{v} + c_1\vec{u}) \in W_j \quad \text{and} \quad (\vec{v} + c_2\vec{u}) \in W_j$$
Then their difference $(c_1 - c_2)\vec{u} \in W_j \implies \vec{u} \in W_j$ (since $c_1 - c_2 \ne 0$).  
- If $j = 1$, then $\vec{v} = (\vec{v} + c_1\vec{u}) - c_1\vec{u} \in W_1$, contradicting $\vec{v} \notin W_1$.
- If $j \ge 2$, then $\vec{u} \in W_j$, contradicting $\vec{u} \notin \bigcup_{k=2}^m W_k$.  
Thus, each subspace $W_j$ can contain at most ONE vector from the infinite set $\{\vec{v} + c\vec{u} : c \in F\}$.  
Since $m$ is finite and $F$ is infinite, the union $\bigcup_{j=1}^m W_j$ cannot cover the set, contradicting $V = \bigcup W_k$. $\blacksquare$""",
                "answer": r"""$W_1 \cup W_2$ is a subspace if and only if $W_1 \subseteq W_2$ or $W_2 \subseteq W_1$. Geometrically in $\mathbb{R}^2$, the union of the $x$-axis and $y$-axis contains $(1,0)$ and $(0,1)$ but not their sum $(1,1)$. Furthermore, an infinite-dimensional or finite-dimensional vector space over an infinite field cannot be covered by a finite union of proper subspaces."""
            }
        ]
    }

if __name__ == "__main__":
    u1 = build_unit_1()
    u2 = build_unit_2()
    with open("la_u1.json", "w", encoding="utf-8") as f:
        json.dump(u1, f, indent=2)
    with open("la_u2.json", "w", encoding="utf-8") as f:
        json.dump(u2, f, indent=2)
    print("Units 1 and 2 successfully built: la_u1.json, la_u2.json")
