# -*- coding: utf-8 -*-
"""
build_tensor_unit1.py
Constructs Unit 1: Coordinates, Index Notation, Summation Convention & Affine Spaces
Strictly ZERO course numbers.
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Coordinates, Index Notation, Summation Convention & Affine Spaces",
        "leadSummary": "Foundations of tensor calculus and differential invariants: curvilinear coordinate systems, regular coordinate transformations, the Einstein summation convention, index classification into free and dummy indices, the mixed Kronecker delta symbol, the geometry of n-dimensional affine and differential spaces, the distinction between contravariant vectors (tangent arrows) and covariant vectors (differential 1-forms/gradients), and the coordinate invariance of the inner product pairing.",
        "simulations": ["sim_tensor_coord_transform"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Curvilinear Coordinates, Scale Factors & Coordinate Transformations",
                "content": r"""### 1. Curvilinear Coordinate Systems in $\mathbb{R}^n$

Let $\mathbb{R}^n$ denote $n$-dimensional Euclidean space equipped with standard rectangular Cartesian coordinates $(x^1, x^2, \dots, x^n)$. A system of **curvilinear coordinates** $(\bar{x}^1, \bar{x}^2, \dots, \bar{x}^n)$ is introduced by establishing a set of $n$ invertible, single-valued, continuously differentiable functions:
$$x^i = x^i(\bar{x}^1, \bar{x}^2, \dots, \bar{x}^n), \qquad (i = 1, 2, \dots, n)$$

> **Definition 1.1 (Regular Coordinate Transformation & Jacobian):**
> A coordinate transformation is said to be **regular (admissible)** in an open domain $\mathcal{U} \subseteq \mathbb{R}^n$ if:
> 1. The functions $x^i(\bar{x}^1, \dots, \bar{x}^n)$ possess continuous partial derivatives of class at least $C^2$.
> 2. The **Jacobian determinant** $J$ does not vanish at any point of $\mathcal{U}$:
>    $$J = \frac{\partial(x^1, x^2, \dots, x^n)}{\partial(\bar{x}^1, \bar{x}^2, \dots, \bar{x}^n)} = \det\left( \frac{\partial x^i}{\partial \bar{x}^j} \right) \ne 0$$

By the Inverse Function Theorem, non-vanishing of $J$ guarantees the existence of a unique, continuously differentiable local inverse transformation:
$$\bar{x}^j = \bar{x}^j(x^1, x^2, \dots, x^n), \qquad (j = 1, 2, \dots, n)$$
satisfying the inverse Jacobian relationship:
$$\det\left( \frac{\partial \bar{x}^j}{\partial x^i} \right) = \frac{1}{J} \ne 0$$

---

### 2. Coordinate Curves and Coordinate Surfaces

Fixing all new coordinates except one defines a **coordinate curve**:
- **$i$-th Coordinate Curve:** The locus of points where $\bar{x}^j = c^j$ (constant) for all $j \ne i$, parameterized solely by $\bar{x}^i$.
- **$i$-th Coordinate Surface:** The locus of points where $\bar{x}^i = c^i$ (constant), while the remaining $n-1$ coordinates vary freely.

The intersection of $n-1$ coordinate surfaces forms a single coordinate curve.

---

### 3. Tangent Basis Vectors and Lamé Scale Factors

Let $\mathbf{r} = \mathbf{r}(x^1, \dots, x^n)$ denote the position vector of an arbitrary point in $\mathbb{R}^n$. Under the transformation to curvilinear coordinates $\bar{x}^i$, the tangent vector to the $i$-th coordinate curve is:
$$\mathbf{e}_i = \frac{\partial \mathbf{r}}{\partial \bar{x}^i} = \sum_{k=1}^n \frac{\partial x^k}{\partial \bar{x}^i} \hat{\mathbf{i}}_k$$

> **Definition 1.2 (Scale Factors / Lamé Coefficients):**
> The **scale factor** $h_i$ associated with coordinate $\bar{x}^i$ is the magnitude of the natural tangent vector $\mathbf{e}_i$:
> $$h_i = \|\mathbf{e}_i\| = \sqrt{\mathbf{e}_i \cdot \mathbf{e}_i} = \sqrt{\sum_{k=1}^n \left( \frac{\partial x^k}{\partial \bar{x}^i} \right)^2}$$
> The corresponding unit tangent vector is $\hat{\mathbf{e}}_i = \frac{\mathbf{e}_i}{h_i}$.

A curvilinear coordinate system is **orthogonal** if the coordinate curves intersect at right angles at every point, which occurs if and only if:
$$\mathbf{e}_i \cdot \mathbf{e}_j = 0 \qquad \text{for all } i \ne j$$"""
            },
            {
                "secNumber": "1.2",
                "title": "Einstein Summation Convention & The Kronecker Delta",
                "content": r"""### 1. The Einstein Summation Convention

In 1916, Albert Einstein introduced a concise notational convention to streamline tensor calculations.

> **Axiom 1.1 (Einstein Summation Convention):**
> Whenever an index appears **twice in a single monomial term**—once as a superscript (upper index) and once as a subscript (lower index)—summation over that repeated index is automatically implied over its complete allowable range (typically $1, 2, \dots, n$), without writing the summation symbol $\sum$:
> $$A^i B_i \equiv \sum_{i=1}^n A^i B_i = A^1 B_1 + A^2 B_2 + \dots + A^n B_n$$

#### Rigorous Rules Governing Index Balancing:
1. **Dummy (Umbral) Indices:**
   An index that appears once as a superscript and once as a subscript in a term is a **dummy index**. A dummy index can be freely replaced by any unused letter without altering the mathematical meaning:
   $$A^i B_i = A^k B_k = A^\alpha B_\alpha$$
2. **Free Indices:**
   An index that appears only once in a term is a **free index**.
   - Every term in a valid tensor equation must contain the **exact same free indices** at the **exact same height** (upper or lower).
   - If an equation has $p$ free indices, it represents a system of $n^p$ separate scalar equations.
3. **Index Multiplicity Prohibition:**
   An index must **never appear more than twice** in any single term. An expression such as $A^i B_i C^i$ is mathematically meaningless and strictly forbidden in tensor calculus.

---

### 2. The Kronecker Delta Symbol

The **mixed Kronecker delta** $\delta_j^i$ is defined by:
$$\delta_j^i = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \ne j \end{cases}$$

#### Algebraic Properties of the Kronecker Delta:
1. **Substitution / Sifting Property:**
   Contraction with the Kronecker delta replaces the contracted index:
   $$\delta_j^i A^j = A^i, \qquad \delta_j^i B_i = B_j, \qquad \delta_j^i T^j_{\; k} = T^i_{\; k}$$
2. **Trace / Dimensionality Property:**
   Summing over both indices yields the dimension $n$ of the underlying space:
   $$\delta_i^i = \delta_1^1 + \delta_2^2 + \dots + \delta_n^n = 1 + 1 + \dots + 1 = n$$
3. **Chain Rule Inversion:**
   For any regular coordinate transformation $x^i \leftrightarrow \bar{x}^j$:
   $$\frac{\partial x^i}{\partial \bar{x}^k} \frac{\partial \bar{x}^k}{\partial x^j} = \frac{\partial x^i}{\partial x^j} = \delta_j^i, \qquad \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial x^k}{\partial \bar{x}^j} = \delta_j^i$$"""
            },
            {
                "secNumber": "1.3",
                "title": "Space of n-Dimensions, Affine Spaces & Jacobian Transitions",
                "content": r"""### 1. Spaces of $n$-Dimensions ($V_n, E_n, R_n$)

In differential geometry and physics, we distinguish between three fundamental mathematical structures:
1. **Affine Space ($A_n$):** A geometric space consisting of points where parallel displacement and linear combinations of displacement vectors are defined, but no intrinsic concept of angle or metric length exists.
2. **Euclidean Space ($E_n$):** An affine space equipped with a constant, positive-definite metric tensor (in Cartesian coordinates, $g_{ij} = \delta_{ij}$).
3. **Riemannian Space ($R_n$ or $V_n$):** A differentiable manifold equipped with a position-dependent metric tensor $g_{ij}(x)$, where distance along curves is defined by $ds^2 = g_{ij}(x) dx^i dx^j$.

---

### 2. Jacobian Matrix of Coordinate Transitions

Consider two overlapping coordinate charts $x^i$ and $\bar{x}^j$ covering an open region $\mathcal{U} \subseteq V_n$.
The transition between charts is governed by the **Jacobian transition matrix**:
$$\Lambda^i_{\; j} = \frac{\partial x^i}{\partial \bar{x}^j}, \qquad (\Lambda^{-1})^j_{\; k} = \frac{\partial \bar{x}^j}{\partial x^k}$$
Their matrix product satisfies identity:
$$\Lambda^i_{\; j} (\Lambda^{-1})^j_{\; k} = \frac{\partial x^i}{\partial \bar{x}^j} \frac{\partial \bar{x}^j}{\partial x^k} = \delta^i_k$$

> **Theorem 1.1 (Transformation of Volume Elements):**
> Let $d^n x = dx^1 dx^2 \cdots dx^n$ denote the differential coordinate volume element in the $x^i$ frame, and $d^n \bar{x} = d\bar{x}^1 \cdots d\bar{x}^n$ in the $\bar{x}^j$ frame. Then:
> $$d^n x = |J| \, d^n \bar{x} = \left| \det\left( \frac{\partial x^i}{\partial \bar{x}^j} \right) \right| d^n \bar{x}$$
> Volume elements do not transform as scalar invariants, but rather as scalar densities of weight $-1$."""
            },
            {
                "secNumber": "1.4",
                "title": "Contravariant Vectors vs Covariant Vectors (Covectors / 1-Forms)",
                "content": r"""### 1. Contravariant Vectors (Tangent Vectors)

Consider the differential displacement vector between two neighboring points $P(x^i)$ and $Q(x^i + dx^i)$. By the multi-variable chain rule:
$$d\bar{x}^i = \frac{\partial \bar{x}^i}{\partial x^j} dx^j$$

> **Definition 1.3 (Contravariant Vector):**
> A set of $n$ quantities $A^1, A^2, \dots, A^n$ defined at a point $P$ constitutes the components of a **contravariant vector** (or tensor of rank $(1, 0)$) if, under an arbitrary regular coordinate transformation $x^i \to \bar{x}^i$, its components transform according to the direct Jacobian law:
> $$\bar{A}^i = \frac{\partial \bar{x}^i}{\partial x^j} A^j$$

The superscript indicates that the components transform with the partial derivatives of the *new* coordinates with respect to the *old* coordinates (in the same manner as coordinate differentials $dx^i$).
- **Physical Examples:** Velocity vector $v^i = \frac{dx^i}{dt}$, acceleration vector $a^i = \frac{d^2 x^i}{dt^2}$, displacement $dx^i$, current density 4-vector $J^\mu$.

---

### 2. Covariant Vectors (Covectors / Differential 1-Forms)

Consider a scalar field $\phi(x^1, \dots, x^n)$ that is invariant under coordinate changes ($\bar{\phi}(\bar{x}) = \phi(x)$).
Computing the gradient components via the chain rule:
$$\frac{\partial \bar{\phi}}{\partial \bar{x}^i} = \frac{\partial \phi}{\partial x^j} \frac{\partial x^j}{\partial \bar{x}^i}$$

> **Definition 1.4 (Covariant Vector / Covector):**
> A set of $n$ quantities $B_1, B_2, \dots, B_n$ defined at a point $P$ constitutes the components of a **covariant vector** (or covector, 1-form, tensor of rank $(0, 1)$) if, under an arbitrary regular coordinate transformation $x^i \to \bar{x}^i$, its components transform according to the inverse Jacobian law:
> $$\bar{B}_i = \frac{\partial x^j}{\partial \bar{x}^i} B_j$$

The subscript indicates that the components transform with the partial derivatives of the *old* coordinates with respect to the *new* coordinates (in the inverse manner to coordinate differentials).
- **Physical Examples:** Gradient of a scalar potential $\nabla_i \phi = \frac{\partial \phi}{\partial x^i}$, electromagnetic 4-potential $A_\mu$, normal vector to a hypersurface $n_i = \partial_i f$.

```
                 Geometric Duality of Vectors and Covectors
                 
         Contravariant Vector Aⁱ               Covariant Vector Bᵢ
            (Tangent Arrow)                    (Stack of Hyperplanes)
                 ▲                                   │   │   │   │
                /                                    │   │   │   │
               /  vⁱ = dxⁱ/dt                        │   │   │   │
              •                                      ▼   ▼   ▼   ▼
     Direction of displacement             Rate of variation / gradient
     Transforms via ∂x̄ⁱ/∂xʲ                Transforms via ∂xʲ/∂x̄ⁱ
```"""
            },
            {
                "secNumber": "1.5",
                "title": "Invariance of the Inner Product & Interactive Transformation Engine",
                "content": r"""### 1. Invariance of the Inner Product (Contraction of Vector and Covector)

A central postulate of tensor calculus is that physical quantities must not depend on the arbitrary choice of coordinates.

> **Theorem 1.2 (Scalar Invariance of Contraction):**
> Let $A^i$ be a contravariant vector and $B_i$ be a covariant vector at point $P$. Then the contraction:
> $$\Phi = A^i B_i = A^1 B_1 + A^2 B_2 + \dots + A^n B_n$$
> is an **absolute scalar invariant** under all regular coordinate transformations:
> $$\bar{\Phi} = \bar{A}^i \bar{B}_i = A^j B_j = \Phi$$

*Proof:*
Transform each vector according to its definition:
$$\bar{A}^i = \frac{\partial \bar{x}^i}{\partial x^j} A^j, \qquad \bar{B}_i = \frac{\partial x^k}{\partial \bar{x}^i} B_k$$
Form the contracted product in the new coordinate system:
$$\bar{A}^i \bar{B}_i = \left( \frac{\partial \bar{x}^i}{\partial x^j} A^j \right) \left( \frac{\partial x^k}{\partial \bar{x}^i} B_k \right) = \left( \frac{\partial \bar{x}^i}{\partial x^j} \frac{\partial x^k}{\partial \bar{x}^i} \right) A^j B_k$$
By the chain rule identity:
$$\frac{\partial x^k}{\partial \bar{x}^i} \frac{\partial \bar{x}^i}{\partial x^j} = \frac{\partial x^k}{\partial x^j} = \delta^k_j$$
Substituting this Kronecker delta:
$$\bar{A}^i \bar{B}_i = \delta^k_j A^j B_k = A^j (\delta^k_j B_k) = A^j B_j$$
The value of $\Phi$ is identical in all coordinate systems. $\blacksquare$

---

### 2. Interactive Coordinate Transformation & Dual-Frame Engine

The simulation below provides a real-time laboratory for coordinate geometry:
- **Continuous Transformation Control:** Switch seamlessly between Cartesian, Polar $(r, \theta)$, and Oblique Shear $(u, v)$ frames.
- **Dual Basis Inspector:** Observe the natural tangent vectors $\mathbf{e}_1, \mathbf{e}_2$ alongside the dual reciprocal covectors $\mathbf{e}^1, \mathbf{e}^2$.
- **Metric Verification:** Real-time calculation of $g_{ij} = \mathbf{e}_i \cdot \mathbf{e}_j$ and verification that $\mathbf{e}_i \cdot \mathbf{e}^j = \delta_i^j$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 1.1: Vector Component Transformations under 2D Rotation and Shear",
                "statement": r"""Consider the two-dimensional Cartesian plane with coordinates $(x^1, x^2) = (x, y)$.
1. A new coordinate system $(\bar{x}^1, \bar{x}^2)$ is obtained by rotating the axes counterclockwise by an angle $\theta$:
   $$\bar{x}^1 = x^1 \cos\theta + x^2 \sin\theta, \qquad \bar{x}^2 = -x^1 \sin\theta + x^2 \cos\theta$$
   Compute the Jacobian transformation matrices $\frac{\partial \bar{x}^i}{\partial x^j}$ and $\frac{\partial x^j}{\partial \bar{x}^i}$, and verify $\frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial x^k}{\partial \bar{x}^j} = \delta^i_j$.
2. Given a contravariant vector with components $A^1 = 3, A^2 = 4$ at the origin, find its components $(\bar{A}^1, \bar{A}^2)$ in the rotated system for $\theta = \pi/4$.
3. Given a covariant vector with components $B_1 = 3, B_2 = 4$, compute its components $(\bar{B}_1, \bar{B}_2)$ and verify that the scalar contraction $A^i B_i = \bar{A}^i \bar{B}_i$ is strictly conserved.""",
                "hints": [
                    "For rotation, the inverse transformation has $\\theta$ replaced by $-\\theta$.",
                    "Contravariant components transform via $\\bar{A}^i = \\frac{\\partial \\bar{x}^i}{\\partial x^j} A^j$.",
                    "Covariant components transform via $\\bar{B}_i = \\frac{\\partial x^j}{\\partial \\bar{x}^i} B_j$."
                ],
                "solution": r"""### 1. Calculation of the Jacobian Transformation Matrices
The forward coordinate relations are:
$$\bar{x}^1 = x^1 \cos\theta + x^2 \sin\theta, \qquad \bar{x}^2 = -x^1 \sin\theta + x^2 \cos\theta$$
The Jacobian matrix $\Lambda^i_{\; j} = \frac{\partial \bar{x}^i}{\partial x^j}$ is:
$$\left( \frac{\partial \bar{x}^i}{\partial x^j} \right) = \begin{pmatrix} \frac{\partial \bar{x}^1}{\partial x^1} & \frac{\partial \bar{x}^1}{\partial x^2} \\ \frac{\partial \bar{x}^2}{\partial x^1} & \frac{\partial \bar{x}^2}{\partial x^2} \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}$$

The inverse relations (expressing old coordinates in terms of new) are obtained by inverting the orthogonal rotation matrix:
$$x^1 = \bar{x}^1 \cos\theta - \bar{x}^2 \sin\theta, \qquad x^2 = \bar{x}^1 \sin\theta + \bar{x}^2 \cos\theta$$
The inverse Jacobian matrix is:
$$\left( \frac{\partial x^j}{\partial \bar{x}^i} \right) = \begin{pmatrix} \frac{\partial x^1}{\partial \bar{x}^1} & \frac{\partial x^1}{\partial \bar{x}^2} \\ \frac{\partial x^2}{\partial \bar{x}^1} & \frac{\partial x^2}{\partial \bar{x}^2} \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

Now verify the contraction:
$$\left( \frac{\partial \bar{x}^i}{\partial x^k} \right) \left( \frac{\partial x^k}{\partial \bar{x}^j} \right) = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = \begin{pmatrix} \cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta \\ -\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \delta^i_j$$

---

### 2. Transformation of Contravariant Vector $A^i = (3, 4)$
For $\theta = \pi/4$, $\cos(\pi/4) = \sin(\pi/4) = \frac{\sqrt{2}}{2}$.
$$\bar{A}^1 = \frac{\partial \bar{x}^1}{\partial x^1} A^1 + \frac{\partial \bar{x}^1}{\partial x^2} A^2 = 3\left(\frac{\sqrt{2}}{2}\right) + 4\left(\frac{\sqrt{2}}{2}\right) = \frac{7\sqrt{2}}{2}$$
$$\bar{A}^2 = \frac{\partial \bar{x}^2}{\partial x^1} A^1 + \frac{\partial \bar{x}^2}{\partial x^2} A^2 = -3\left(\frac{\sqrt{2}}{2}\right) + 4\left(\frac{\sqrt{2}}{2}\right) = \frac{\sqrt{2}}{2}$$
Thus:
$$\bar{A}^i = \left( \frac{7\sqrt{2}}{2}, \; \frac{\sqrt{2}}{2} \right)$$

---

### 3. Transformation of Covariant Vector $B_i = (3, 4)$
For covariant vectors:
$$\bar{B}_1 = \frac{\partial x^1}{\partial \bar{x}^1} B_1 + \frac{\partial x^2}{\partial \bar{x}^1} B_2 = 3(\cos\theta) + 4(\sin\theta) = \frac{7\sqrt{2}}{2}$$
$$\bar{B}_2 = \frac{\partial x^1}{\partial \bar{x}^2} B_1 + \frac{\partial x^2}{\partial \bar{x}^2} B_2 = 3(-\sin\theta) + 4(\cos\theta) = \frac{\sqrt{2}}{2}$$
Thus:
$$\bar{B}_i = \left( \frac{7\sqrt{2}}{2}, \; \frac{\sqrt{2}}{2} \right)$$

---

### 4. Verification of Invariant Contraction
- In the original $(x^1, x^2)$ coordinates:
  $$A^i B_i = A^1 B_1 + A^2 B_2 = (3)(3) + (4)(4) = 9 + 16 = 25$$
- In the rotated $(\bar{x}^1, \bar{x}^2)$ coordinates:
  $$\bar{A}^i \bar{B}_i = \bar{A}^1 \bar{B}_1 + \bar{A}^2 \bar{B}_2 = \left(\frac{7\sqrt{2}}{2}\right)\left(\frac{7\sqrt{2}}{2}\right) + \left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{2}}{2}\right) = \frac{49 \times 2}{4} + \frac{1 \times 2}{4} = \frac{98 + 2}{4} = \frac{100}{4} = 25$$

The scalar product $\bar{A}^i \bar{B}_i = A^i B_i = 25$ is strictly conserved. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 1.2: General Curvilinear Coordinate System in $\mathbb{R}^3$, Jacobian & Scale Factors",
                "statement": r"""Consider spherical polar coordinates in $\mathbb{R}^3$ defined by:
$$x^1 = r \sin\theta \cos\phi, \qquad x^2 = r \sin\theta \sin\phi, \qquad x^3 = r \cos\theta$$
where $\bar{x}^1 = r, \bar{x}^2 = \theta, \bar{x}^3 = \phi$ with $r > 0, 0 < \theta < \pi, 0 \le \phi < 2\pi$.

1. Compute the Jacobian matrix $\frac{\partial x^i}{\partial \bar{x}^j}$ and evaluate its determinant $J = \det\left(\frac{\partial x^i}{\partial \bar{x}^j}\right)$.
2. Calculate the natural basis vectors $\mathbf{e}_1 = \frac{\partial \mathbf{r}}{\partial r}, \mathbf{e}_2 = \frac{\partial \mathbf{r}}{\partial \theta}, \mathbf{e}_3 = \frac{\partial \mathbf{r}}{\partial \phi}$.
3. Determine the Lamé scale factors $h_r, h_\theta, h_\phi$ and prove that the coordinate system is strictly orthogonal everywhere.
4. Express the differential volume element $dV$ in terms of $r, \theta, \phi$.""",
                "hints": [
                    "Recall that $\\mathbf{r} = x^1 \\hat{\\mathbf{i}} + x^2 \\hat{\\mathbf{j}} + x^3 \\hat{\\mathbf{k}}$.",
                    "Take partial derivatives with respect to $r, \\theta, \\phi$.",
                    "Show that $\\mathbf{e}_i \\cdot \\mathbf{e}_j = 0$ for all $i \\ne j$."
                ],
                "solution": r"""### 1. Jacobian Matrix and Determinant
The Jacobian matrix $\Lambda^i_{\; j} = \frac{\partial x^i}{\partial \bar{x}^j}$ is:
$$\left( \frac{\partial x^i}{\partial \bar{x}^j} \right) = \begin{pmatrix}
\sin\theta\cos\phi & r\cos\theta\cos\phi & -r\sin\theta\sin\phi \\
\sin\theta\sin\phi & r\cos\theta\sin\phi & r\sin\theta\cos\phi \\
\cos\theta & -r\sin\theta & 0
\end{pmatrix}$$

Expanding the determinant along the third row:
$$\begin{aligned}
J &= \cos\theta \begin{vmatrix} r\cos\theta\cos\phi & -r\sin\theta\sin\phi \\ r\cos\theta\sin\phi & r\sin\theta\cos\phi \end{vmatrix} - (-r\sin\theta) \begin{vmatrix} \sin\theta\cos\phi & -r\sin\theta\sin\phi \\ \sin\theta\sin\phi & r\sin\theta\cos\phi \end{vmatrix} \\
&= \cos\theta \left( r^2\sin\theta\cos\theta\cos^2\phi + r^2\sin\theta\cos\theta\sin^2\phi \right) + r\sin\theta \left( r\sin^2\theta\cos^2\phi + r\sin^2\theta\sin^2\phi \right) \\
&= \cos\theta (r^2\sin\theta\cos\theta) + r\sin\theta (r\sin^2\theta) \\
&= r^2\sin\theta\cos^2\theta + r^2\sin^3\theta = r^2\sin\theta(\cos^2\theta + \sin^2\theta) = r^2\sin\theta
\end{aligned}$$
Thus, $J = r^2 \sin\theta$, which is strictly positive for $r > 0$ and $0 < \theta < \pi$.

---

### 2. Natural Tangent Basis Vectors
Differentiating $\mathbf{r}(r, \theta, \phi)$:
- $\mathbf{e}_1 = \mathbf{e}_r = \frac{\partial \mathbf{r}}{\partial r} = (\sin\theta\cos\phi)\hat{\mathbf{i}} + (\sin\theta\sin\phi)\hat{\mathbf{j}} + (\cos\theta)\hat{\mathbf{k}}$
- $\mathbf{e}_2 = \mathbf{e}_\theta = \frac{\partial \mathbf{r}}{\partial \theta} = (r\cos\theta\cos\phi)\hat{\mathbf{i}} + (r\cos\theta\sin\phi)\hat{\mathbf{j}} - (r\sin\theta)\hat{\mathbf{k}}$
- $\mathbf{e}_3 = \mathbf{e}_\phi = \frac{\partial \mathbf{r}}{\partial \phi} = (-r\sin\theta\sin\phi)\hat{\mathbf{i}} + (r\sin\theta\cos\phi)\hat{\mathbf{j}}$

---

### 3. Lamé Scale Factors and Orthogonality Proof
Compute the magnitudes $h_i = \|\mathbf{e}_i\| = \sqrt{\mathbf{e}_i \cdot \mathbf{e}_i}$:
- $h_r^2 = \mathbf{e}_r \cdot \mathbf{e}_r = \sin^2\theta\cos^2\phi + \sin^2\theta\sin^2\phi + \cos^2\theta = \sin^2\theta + \cos^2\theta = 1 \implies h_r = 1$
- $h_\theta^2 = \mathbf{e}_\theta \cdot \mathbf{e}_\theta = r^2\cos^2\theta\cos^2\phi + r^2\cos^2\theta\sin^2\phi + r^2\sin^2\theta = r^2(\cos^2\theta + \sin^2\theta) = r^2 \implies h_\theta = r$
- $h_\phi^2 = \mathbf{e}_\phi \cdot \mathbf{e}_\phi = r^2\sin^2\theta\sin^2\phi + r^2\sin^2\theta\cos^2\phi = r^2\sin^2\theta \implies h_\phi = r\sin\theta$

Now compute the mutual dot products for $i \ne j$:
- $\mathbf{e}_r \cdot \mathbf{e}_\theta = r\sin\theta\cos\theta\cos^2\phi + r\sin\theta\cos\theta\sin^2\phi - r\sin\theta\cos\theta = r\sin\theta\cos\theta - r\sin\theta\cos\theta = 0$
- $\mathbf{e}_r \cdot \mathbf{e}_\phi = -r\sin^2\theta\cos\phi\sin\phi + r\sin^2\theta\sin\phi\cos\phi + 0 = 0$
- $\mathbf{e}_\theta \cdot \mathbf{e}_\phi = -r^2\sin\theta\cos\theta\cos\phi\sin\phi + r^2\sin\theta\cos\theta\sin\phi\cos\phi + 0 = 0$

Since $\mathbf{e}_i \cdot \mathbf{e}_j = 0$ for all $i \ne j$, spherical coordinates form a strictly **orthogonal** curvilinear coordinate system.

---

### 4. Differential Volume Element
For an orthogonal coordinate system, the volume element is the product of the differential arc lengths:
$$dV = (h_r dr)(h_\theta d\theta)(h_\phi d\phi) = (1 \, dr)(r \, d\theta)(r\sin\theta \, d\phi) = r^2 \sin\theta \, dr \, d\theta \, d\phi$$
Notice that this matches $|J| \, dr \, d\theta \, d\phi = r^2 \sin\theta \, dr \, d\theta \, d\phi$ identically! $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 1.3: Rigorous Tensor Criteria & The Failure of the Hessian Matrix",
                "statement": r"""Let $\phi(x^1, \dots, x^n)$ be an arbitrary scalar field of class $C^2$ on an $n$-dimensional differentiable manifold $V_n$.
1. Prove rigorously that the gradient vector components $G_i = \frac{\partial \phi}{\partial x^i}$ transform as a **covariant vector** under any arbitrary regular coordinate transformation $x^i \to \bar{x}^i$.
2. Prove that the tangent velocity components $V^i = \frac{dx^i}{dt}$ along a parameterized curve $x^i(t)$ transform as a **contravariant vector**.
3. Examine the Hessian matrix of second partial derivatives:
   $$H_{ij} = \frac{\partial^2 \phi}{\partial x^i \partial x^j}$$
   Derive its exact transformation law under $x^i \to \bar{x}^i$.
4. Prove that $H_{ij}$ **fails** to transform as a tensor, identify the exact mathematical term responsible for this failure, and state under what restricted class of coordinate transformations $H_{ij}$ behaves as a tensor.""",
                "hints": [
                    "For part 1, apply the multivariable chain rule to $\\bar{\\phi}(\\bar{x}) = \\phi(x)$.",
                    "For part 3, differentiate $\\bar{G}_i = \\frac{\\partial x^k}{\\partial \\bar{x}^i} G_k$ with respect to $\\bar{x}^j$ using the product rule.",
                    "Look for the appearance of second partial derivatives $\\frac{\\partial^2 x^k}{\\partial \\bar{x}^i \\partial \\bar{x}^j}$."
                ],
                "solution": r"""### 1. Proof that the Gradient $G_i$ is a Covariant Vector
Let $\phi(x)$ be a scalar field. Since it is an invariant scalar:
$$\bar{\phi}(\bar{x}^1, \dots, \bar{x}^n) = \phi(x^1(\bar{x}), \dots, x^n(\bar{x}))$$
Differentiating with respect to the new coordinate $\bar{x}^i$ using the chain rule:
$$\bar{G}_i = \frac{\partial \bar{\phi}}{\partial \bar{x}^i} = \frac{\partial \phi}{\partial x^k} \frac{\partial x^k}{\partial \bar{x}^i} = \frac{\partial x^k}{\partial \bar{x}^i} G_k$$
This is precisely the defining transformation law of a covariant vector (Definition 1.4).
Thus, $G_i = \partial_i \phi$ is a true covariant vector. $\blacksquare$

---

### 2. Proof that Tangent Velocity $V^i$ is a Contravariant Vector
Let $x^i(t)$ be a curve parameterized by parameter $t$ (an invariant scalar).
The coordinates in the new frame are $\bar{x}^i(t) = \bar{x}^i(x^1(t), \dots, x^n(t))$.
Differentiating with respect to $t$ using the chain rule:
$$\bar{V}^i = \frac{d\bar{x}^i}{dt} = \frac{\partial \bar{x}^i}{\partial x^k} \frac{dx^k}{dt} = \frac{\partial \bar{x}^i}{\partial x^k} V^k$$
This is precisely the defining transformation law of a contravariant vector (Definition 1.3).
Thus, $V^i = \frac{dx^i}{dt}$ is a true contravariant vector. $\blacksquare$

---

### 3. Transformation Law of the Hessian Matrix $H_{ij}$
In the original coordinates, $H_{kl} = \frac{\partial^2 \phi}{\partial x^k \partial x^l} = \frac{\partial G_k}{\partial x^l}$.
In the new coordinates:
$$\bar{H}_{ij} = \frac{\partial^2 \bar{\phi}}{\partial \bar{x}^i \partial \bar{x}^j} = \frac{\partial}{\partial \bar{x}^j} \left( \frac{\partial \bar{\phi}}{\partial \bar{x}^i} \right) = \frac{\partial}{\partial \bar{x}^j} \left( \frac{\partial x^k}{\partial \bar{x}^i} \frac{\partial \phi}{\partial x^k} \right)$$
Applying the product rule of differentiation:
$$\bar{H}_{ij} = \frac{\partial x^k}{\partial \bar{x}^i} \frac{\partial}{\partial \bar{x}^j}\left(\frac{\partial \phi}{\partial x^k}\right) + \frac{\partial \phi}{\partial x^k} \frac{\partial}{\partial \bar{x}^j}\left(\frac{\partial x^k}{\partial \bar{x}^i}\right)$$
Using the chain rule on the first term:
$$\frac{\partial}{\partial \bar{x}^j}\left(\frac{\partial \phi}{\partial x^k}\right) = \frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial}{\partial x^l}\left(\frac{\partial \phi}{\partial x^k}\right) = \frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial^2 \phi}{\partial x^k \partial x^l} = \frac{\partial x^l}{\partial \bar{x}^j} H_{kl}$$
For the second term:
$$\frac{\partial}{\partial \bar{x}^j}\left(\frac{\partial x^k}{\partial \bar{x}^i}\right) = \frac{\partial^2 x^k}{\partial \bar{x}^j \partial \bar{x}^i}$$
Combining both terms yields the exact transformation law:
$$\bar{H}_{ij} = \frac{\partial x^k}{\partial \bar{x}^i} \frac{\partial x^l}{\partial \bar{x}^j} H_{kl} + \frac{\partial^2 x^k}{\partial \bar{x}^i \partial \bar{x}^j} \frac{\partial \phi}{\partial x^k}$$

---

### 4. Non-Tensor Character and Remediation
For $H_{ij}$ to be a valid rank-$(0, 2)$ covariant tensor, it would have to transform strictly homogeneously as:
$$\bar{H}_{ij} = \frac{\partial x^k}{\partial \bar{x}^i} \frac{\partial x^l}{\partial \bar{x}^j} H_{kl}$$
However, the actual transformation law contains an **inhomogeneous second-derivative term**:
$$\text{Inhomogeneous Obstruction} = \frac{\partial^2 x^k}{\partial \bar{x}^i \partial \bar{x}^j} \frac{\partial \phi}{\partial x^k}$$
Due to this extra term, $H_{ij}$ is **NOT a tensor** under general coordinate transformations!

#### Special Cases where $H_{ij}$ Behaves as a Tensor:
1. **Affine / Linear Transformations:** If the coordinate transformation is purely linear:
   $$x^k = A^k_{\; m} \bar{x}^m + c^k \implies \frac{\partial^2 x^k}{\partial \bar{x}^i \partial \bar{x}^j} = 0$$
   The second partial derivatives vanish identically, so $H_{ij}$ transforms as a tensor under affine transformations (rotations, translations, scaling).
2. **Critical / Stationary Points:** At a point where $\nabla \phi = 0$ ($\frac{\partial \phi}{\partial x^k} = 0$), the inhomogeneous term vanishes, meaning the Hessian is a local tensor at critical points!
3. **General Resolution in Curved Spaces:** To obtain a true tensor everywhere in curved manifolds, one must replace ordinary partial derivatives with **covariant derivatives**:
   $$\nabla_j \nabla_i \phi = \frac{\partial^2 \phi}{\partial x^j \partial x^i} - \Gamma_{ji}^k \frac{\partial \phi}{\partial x^k}$$
   The Christoffel symbol $\Gamma_{ji}^k$ cancels the inhomogeneous second-derivative term, yielding a true tensor! $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u1 = get_unit1()
    print(f"Loaded Unit 1: {u1['title']} with {len(u1['sections'])} sections and {len(u1['problems'])} problems.")
