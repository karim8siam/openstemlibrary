# -*- coding: utf-8 -*-
"""
build_tensor_unit3.py
Constructs Unit 3: Metric Tensors, Riemannian Spaces & Index Manipulation
Strictly ZERO course numbers.
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Metric Tensors, Riemannian Spaces & Index Manipulation",
        "leadSummary": "Foundations of Riemannian geometry and metric tensor calculus: the fundamental quadratic differential form ds^2 = g_ij dx^i dx^j, Riemannian vs Pseudo-Riemannian manifolds, the covariant metric tensor g_ij and contravariant reciprocal metric tensor g^ij, metric determinant g and its derivative identities, natural basis vectors e_i and dual covectors e^i, the musical isomorphisms for raising and lowering indices (associated tensors), vector magnitudes, Riemannian angles, and orthogonal coordinate systems.",
        "simulations": ["sim_tensor_metric_geometry"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "The Fundamental Metric Form $ds^2 = g_{ij} dx^i dx^j$ & Riemannian Manifolds",
                "content": r"""### 1. The Riemannian Metric Axioms

In 1854, Bernhard Riemann generalized Euclidean geometry to arbitrary $n$-dimensional curved manifolds by postulating that the infinitesimal distance $ds$ between two neighboring points $P(x^i)$ and $Q(x^i + dx^i)$ is given by the square root of a quadratic differential form.

> **Definition 3.1 (Fundamental Metric Form):**
> A differentiable manifold $V_n$ is a **Riemannian space** $R_n$ if it is equipped with a symmetric, second-rank covariant tensor field $g_{ij}(x) = g_{ji}(x)$ called the **metric tensor**, such that the arc length element $ds$ satisfies:
> $$ds^2 = g_{ij} dx^i dx^j = g_{11}(dx^1)^2 + 2g_{12} dx^1 dx^2 + \dots + g_{nn}(dx^n)^2$$
> In a proper (positive-definite) Riemannian space, $ds^2 > 0$ for any non-zero displacement $dx^i \ne 0$.

#### Signature Classifications:
1. **Positive-Definite Riemannian Space:** All eigenvalues of the matrix $(g_{ij})$ are strictly positive ($++++\dots$). Distance $ds$ is always real and positive.
2. **Pseudo-Riemannian (Lorentzian) Space:** The metric is non-degenerate ($\det(g) \ne 0$) but indefinite. In 4D relativistic spacetime, the metric signature is $(-, +, +, +)$ (or $(+, -, -, -)$):
   $$ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2 = \eta_{\mu\nu} dx^\mu dx^\nu$$
   where intervals are classified into timelike ($ds^2 < 0$), spacelike ($ds^2 > 0$), and lightlike / null ($ds^2 = 0$).

---

### 2. Transformation Law of the Metric Tensor

Let $x^i \to \bar{x}^k$ be a regular coordinate transformation.
Since the arc length $ds$ is an intrinsic physical distance, the quadratic form is an **absolute scalar invariant**:
$$d\bar{s}^2 = ds^2 \implies \bar{g}_{kl} d\bar{x}^k d\bar{x}^l = g_{ij} dx^i dx^j$$
Substituting the differential transformation $dx^i = \frac{\partial x^i}{\partial \bar{x}^k} d\bar{x}^k$ and $dx^j = \frac{\partial x^j}{\partial \bar{x}^l} d\bar{x}^l$:
$$\bar{g}_{kl} d\bar{x}^k d\bar{x}^l = g_{ij} \left( \frac{\partial x^i}{\partial \bar{x}^k} d\bar{x}^k \right) \left( \frac{\partial x^j}{\partial \bar{x}^l} d\bar{x}^l \right) = \left( \frac{\partial x^i}{\partial \bar{x}^k} \frac{\partial x^j}{\partial \bar{x}^l} g_{ij} \right) d\bar{x}^k d\bar{x}^l$$
Because the coordinate differentials $d\bar{x}^k$ are arbitrary, we deduce:
$$\bar{g}_{kl} = \frac{\partial x^i}{\partial \bar{x}^k} \frac{\partial x^j}{\partial \bar{x}^l} g_{ij}$$
This rigorously confirms that $g_{ij}$ transforms as a **symmetric covariant tensor of rank 2**."""
            },
            {
                "secNumber": "3.2",
                "title": "The Metric Tensor $g_{ij}$, Conjugate Metric $g^{ij}$ & Determinant $g$",
                "content": r"""### 1. The Conjugate (Reciprocal) Metric Tensor $g^{ij}$

Let $g = \det(g_{ij})$ denote the determinant of the $n \times n$ matrix of metric components. For a non-degenerate Riemannian space, $g \ne 0$.

> **Definition 3.2 (Conjugate Metric Tensor):**
> The **conjugate (reciprocal) metric tensor** $g^{ij}$ is defined as the matrix inverse of $g_{ij}$:
> $$g^{ik} g_{kj} = \delta_j^i, \qquad g^{ik} g_{jk} = \delta_j^i$$
> In terms of the matrix cofactors of $g_{ij}$:
> $$g^{ij} = \frac{\text{Cofactor}(g_{ji})}{g} = \frac{G^{ij}}{g}$$
> where $G^{ij}$ is the cofactor of the entry $g_{ij}$ in the determinant $g$.

By symmetry of $g_{ij}$, the conjugate metric tensor is also symmetric: $g^{ij} = g^{ji}$.

---

### 2. Derivative Identities of the Metric Determinant

The derivative of the metric determinant with respect to coordinate $x^k$ plays a central role in constructing Christoffel symbols and invariant divergence formulas.

> **Theorem 3.1 (Derivative of Metric Determinant):**
> Let $g = \det(g_{ij})$. Then:
> $$\frac{\partial g}{\partial x^k} = g \, g^{ij} \frac{\partial g_{ij}}{\partial x^k}$$
> or equivalently:
> $$\frac{\partial \ln \sqrt{g}}{\partial x^k} = \frac{1}{2g} \frac{\partial g}{\partial x^k} = \frac{1}{2} g^{ij} \frac{\partial g_{ij}}{\partial x^k}$$

*Proof:*
Expanding determinant $g$ along its $i$-th row:
$$g = \sum_{j=1}^n g_{ij} G^{ij}$$
Differentiating with respect to $g_{ij}$ yields $\frac{\partial g}{\partial g_{ij}} = G^{ij} = g \, g^{ij}$.
By the multivariable chain rule:
$$\frac{\partial g}{\partial x^k} = \sum_{i,j} \frac{\partial g}{\partial g_{ij}} \frac{\partial g_{ij}}{\partial x^k} = g \, g^{ij} \frac{\partial g_{ij}}{\partial x^k} \blacksquare$$

Similarly, differentiating the relation $g^{ij} g_{jk} = \delta_k^i$:
$$\frac{\partial g^{ij}}{\partial x^k} g_{jk} + g^{ij} \frac{\partial g_{jk}}{\partial x^k} = 0 \implies \frac{\partial g^{im}}{\partial x^k} = -g^{ij} g^{ml} \frac{\partial g_{jl}}{\partial x^k}$$"""
            },
            {
                "secNumber": "3.3",
                "title": "Tangent Vectors, Reciprocal Bases ($\mathbf{e}_i, \mathbf{e}^i$) & Coordinate Frames",
                "content": r"""### 1. Natural Tangent Basis Vectors $\mathbf{e}_i$

Let $\mathbf{r}(x^1, \dots, x^n)$ be the position vector in an embedding space.
The **natural coordinate basis vectors** tangent to the coordinate curves are:
$$\mathbf{e}_i = \frac{\partial \mathbf{r}}{\partial x^i}$$
The infinitesimal displacement vector is:
$$d\mathbf{r} = \frac{\partial \mathbf{r}}{\partial x^i} dx^i = \mathbf{e}_i dx^i$$
Computing the squared arc length:
$$ds^2 = d\mathbf{r} \cdot d\mathbf{r} = (\mathbf{e}_i dx^i) \cdot (\mathbf{e}_j dx^j) = (\mathbf{e}_i \cdot \mathbf{e}_j) dx^i dx^j$$
Comparing directly with $ds^2 = g_{ij} dx^i dx^j$, we obtain the profound geometric identity:
$$g_{ij} = \mathbf{e}_i \cdot \mathbf{e}_j$$
The components of the metric tensor are the scalar products of the natural tangent basis vectors!

---

### 2. Reciprocal Dual Basis Vectors $\mathbf{e}^i$

> **Definition 3.3 (Dual Reciprocal Basis):**
> The **reciprocal basis vectors** $\mathbf{e}^1, \mathbf{e}^2, \dots, \mathbf{e}^n$ are the unique vectors satisfying the biorthogonality condition:
> $$\mathbf{e}_i \cdot \mathbf{e}^j = \delta_i^j$$

In terms of the metric tensor and conjugate metric:
$$\mathbf{e}^i = g^{ij} \mathbf{e}_j, \qquad \mathbf{e}_i = g_{ij} \mathbf{e}^j$$
Computing their mutual inner products:
$$\mathbf{e}^i \cdot \mathbf{e}^j = (g^{im} \mathbf{e}_m) \cdot (g^{jn} \mathbf{e}_n) = g^{im} g^{jn} (\mathbf{e}_m \cdot \mathbf{e}_n) = g^{im} g^{jn} g_{mn} = g^{im} \delta_m^j = g^{ij}$$
Thus, the conjugate metric components are the scalar products of the reciprocal dual basis vectors:
$$g^{ij} = \mathbf{e}^i \cdot \mathbf{e}^j$$"""
            },
            {
                "secNumber": "3.4",
                "title": "Raising and Lowering Indices: Associated Vectors & Tensors",
                "content": r"""### 1. The Musical Isomorphisms ($\flat$ and $\sharp$)

The metric tensor establishes a canonical linear isomorphism between the tangent space $T_p M$ (contravariant vectors) and cotangent space $T_p^* M$ (covariant covectors).
In differential geometry, these are called the **musical isomorphisms**:
- **Flat ($\flat$, Index Lowering):** Converts a contravariant vector into a covariant covector.
- **Sharp ($\sharp$, Index Raising):** Converts a covariant covector into a contravariant vector.

---

### 2. Algebraic Index Manipulation

For any contravariant vector $A^i$:
$$A_i = g_{ij} A^j \quad (\text{Lowering the Index via } g_{ij})$$
Conversely, for any covariant vector $A_i$:
$$A^i = g^{ij} A_j \quad (\text{Raising the Index via } g^{ij})$$

Consistency verification using the inverse relationship:
$$g^{ik} A_k = g^{ik} (g_{kj} A^j) = (g^{ik} g_{kj}) A^j = \delta_j^i A^j = A^i$$
The operations of raising and lowering indices are exact mutual inverses!

#### Raising and Lowering in Higher-Rank Tensors:
The metric tensor raises and lowers individual indices independently:
- Lowering the first index of $T^{ij}$:
  $$T_k^{\; j} = g_{ki} T^{ij}$$
- Lowering both indices of $T^{ij}$:
  $$T_{kl} = g_{ki} g_{lj} T^{ij}$$
- Mixed associated tensor from covariant tensor $T_{ij}$:
  $$T^i_{\; j} = g^{ik} T_{kj}, \qquad T_i^{\; j} = g^{jk} T_{ik}$$
*(Note: If $T_{ij}$ is not symmetric, the position of the dot placeholder matters: $T^i_{\; j} \ne T_j^{\; i}$).*"""
            },
            {
                "secNumber": "3.5",
                "title": "Lengths, Angles & Orthogonal Coordinate Systems",
                "content": r"""### 1. Vector Magnitude and Angle between Vectors

In a Riemannian space with metric $g_{ij}$:
1. **Magnitude (Norm) of a Vector:**
   The length $\|A\|$ of a contravariant vector $A^i$ is defined by:
   $$\|A\| = \sqrt{g_{ij} A^i A^j} = \sqrt{A^i A_i}$$
   For a covariant vector $B_i$:
   $$\|B\| = \sqrt{g^{ij} B_i B_j} = \sqrt{B^i B_i}$$
2. **Angle between Two Vectors:**
   The angle $\theta$ between two non-zero contravariant vectors $A^i$ and $B^i$ is:
   $$\cos\theta = \frac{g_{ij} A^i B^j}{\|A\| \|B\|} = \frac{g_{ij} A^i B^j}{\sqrt{g_{kl} A^k A^l} \sqrt{g_{mn} B^m B^n}}$$
   By the Cauchy-Schwarz inequality for positive-definite metrics, $-1 \le \cos\theta \le 1$.
3. **Orthogonality Condition:**
   Two vectors $A^i$ and $B^i$ are orthogonal if and only if their Riemannian inner product vanishes:
   $$g_{ij} A^i B^j = 0 \iff A^i B_i = 0$$

---

### 2. Orthogonal Curvilinear Coordinate Systems

A coordinate system is **orthogonal** if the coordinate lines intersect at right angles everywhere.
In an orthogonal coordinate system:
$$g_{ij} = 0 \qquad \text{for all } i \ne j$$
The metric tensor and its conjugate are purely diagonal:
$$(g_{ij}) = \begin{pmatrix} g_{11} & 0 & \dots & 0 \\ 0 & g_{22} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & g_{nn} \end{pmatrix}, \qquad (g^{ij}) = \begin{pmatrix} 1/g_{11} & 0 & \dots & 0 \\ 0 & 1/g_{22} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1/g_{nn} \end{pmatrix}$$
The metric determinant is simply the product of diagonal entries:
$$g = g_{11} g_{22} \cdots g_{nn} = (h_1 h_2 \cdots h_n)^2 \implies \sqrt{g} = h_1 h_2 \cdots h_n$$
where $h_i = \sqrt{g_{ii}}$ are the Lamé scale factors."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 3.1: Metric Tensors & Scale Factors in Cylindrical & Spherical Geometries",
                "statement": r"""1. Cylindrical coordinates $(\bar{x}^1, \bar{x}^2, \bar{x}^3) = (r, \theta, z)$ are defined by:
   $$x^1 = r \cos\theta, \qquad x^2 = r \sin\theta, \qquad x^3 = z$$
   Compute the covariant metric tensor components $g_{ij}$, the conjugate metric components $g^{ij}$, and the determinant $g$.
2. Spherical polar coordinates $(\bar{x}^1, \bar{x}^2, \bar{x}^3) = (r, \theta, \phi)$ have metric:
   $$ds^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2$$
   Find the matrices $(g_{ij})$ and $(g^{ij})$.
3. Given a contravariant vector with components $A^i = (1, 2, 3)$ in spherical coordinates at a point where $r = 2, \theta = \pi/2$, compute its associated covariant components $A_i$ and evaluate its invariant length $\|A\| = \sqrt{A^i A_i}$.""",
                "hints": [
                    "Compute differentials $dx^1, dx^2, dx^3$ and substitute into $ds^2 = (dx^1)^2 + (dx^2)^2 + (dx^3)^2$.",
                    "For a diagonal metric, $g^{ii} = 1/g_{ii}$.",
                    "Lower indices via $A_i = g_{ij} A^j$."
                ],
                "solution": r"""### 1. Cylindrical Coordinates Metric Tensor
In Cartesian coordinates $ds^2 = (dx^1)^2 + (dx^2)^2 + (dx^3)^2$.
Differentiating the coordinate relations:
$$dx^1 = \cos\theta dr - r\sin\theta d\theta$$
$$dx^2 = \sin\theta dr + r\cos\theta d\theta$$
$$dx^3 = dz$$
Squaring and adding:
$$\begin{aligned}
(dx^1)^2 + (dx^2)^2 &= (\cos^2\theta + \sin^2\theta) dr^2 + r^2 (\sin^2\theta + \cos^2\theta) d\theta^2 - 2r\sin\theta\cos\theta dr d\theta + 2r\sin\theta\cos\theta dr d\theta \\
&= dr^2 + r^2 d\theta^2
\end{aligned}$$
Thus:
$$ds^2 = dr^2 + r^2 d\theta^2 + dz^2$$

Matching with $ds^2 = g_{ij} d\bar{x}^i d\bar{x}^j$ where $\bar{x} = (r, \theta, z)$:
$$(g_{ij}) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & r^2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
The metric determinant is:
$$g = \det(g_{ij}) = 1 \times r^2 \times 1 = r^2 \implies \sqrt{g} = r$$
The conjugate metric tensor is the matrix inverse:
$$(g^{ij}) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1/r^2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

---

### 2. Spherical Polar Coordinates Metric Matrices
From $ds^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2$ with $\bar{x} = (r, \theta, \phi)$:
$$(g_{ij}) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & r^2 & 0 \\ 0 & 0 & r^2 \sin^2\theta \end{pmatrix}$$
Determinant:
$$g = (1)(r^2)(r^2 \sin^2\theta) = r^4 \sin^2\theta \implies \sqrt{g} = r^2 \sin\theta$$
The conjugate metric is:
$$(g^{ij}) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1/r^2 & 0 \\ 0 & 0 & 1/(r^2 \sin^2\theta) \end{pmatrix}$$

---

### 3. Lowering Indices and Computing Invariant Length
At $r = 2, \theta = \pi/2$:
$$g_{11} = 1, \qquad g_{22} = r^2 = 4, \qquad g_{33} = r^2 \sin^2(\pi/2) = 4(1)^2 = 4$$
All off-diagonal entries are 0.
The contravariant vector components are $A^1 = 1, A^2 = 2, A^3 = 3$.
Lowering indices via $A_i = g_{ij} A^j$:
- $A_1 = g_{11} A^1 = 1 \times 1 = 1$
- $A_2 = g_{22} A^2 = 4 \times 2 = 8$
- $A_3 = g_{33} A^3 = 4 \times 3 = 12$
Thus, the covariant components are:
$$A_i = (1, 8, 12)$$

Now compute the invariant scalar magnitude:
$$\|A\|^2 = A^i A_i = A^1 A_1 + A^2 A_2 + A^3 A_3 = (1)(1) + (2)(8) + (3)(12) = 1 + 16 + 36 = 53$$
$$\|A\| = \sqrt{53} \approx 7.28$$
Notice that calculating via $\|A\|^2 = g_{ij} A^i A^j = 1(1)^2 + 4(2)^2 + 4(3)^2 = 1 + 16 + 36 = 53$ yields the exact same invariant. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 3.2: Angle between Coordinate Curves & Necessary Orthogonality Condition",
                "statement": r"""Let $V_n$ be a Riemannian space with metric $g_{ij}$.
1. Find the unit tangent vectors $\mathbf{u}_{(i)}$ along the $i$-th coordinate curves (where only $x^i$ varies while all other coordinates are held constant).
2. Compute the cosine of the Riemannian angle $\theta_{ij}$ between the $i$-th and $j$-th coordinate curves.
3. Prove that the coordinate curves are mutually orthogonal at a point if and only if all off-diagonal metric components vanish at that point:
   $$g_{ij} = 0 \quad \text{for all } i \ne j$$
4. In an oblique coordinate system in $\mathbb{R}^2$ with axes meeting at angle $\omega$, compute the metric tensor $g_{ij}$ and its conjugate $g^{ij}$.""",
                "hints": [
                    "Along the $i$-th coordinate curve, $dx^i \\ne 0$ and $dx^k = 0$ for $k \\ne i$.",
                    "The arc length along the $i$-th curve is $ds_{(i)} = \\sqrt{g_{ii}} dx^i$.",
                    "For part 4, consider $ds^2 = dx^2 + dy^2 + 2\\cos\\omega dx dy$."
                ],
                "solution": r"""### 1. Tangent Vectors along Coordinate Curves
Along the $i$-th coordinate curve, all coordinates except $x^i$ are held fixed.
Thus, the differential displacement vector has components:
$$dx^k = \delta_i^k dx^i \quad (\text{no sum on } i)$$
The Riemannian arc length along this curve is:
$$ds_{(i)} = \sqrt{g_{kl} dx^k dx^l} = \sqrt{g_{ii} (dx^i)^2} = \sqrt{g_{ii}} dx^i \quad (\text{no sum on } i)$$
The unit tangent vector $u_{(i)}^k$ along the $i$-th coordinate curve is:
$$u_{(i)}^k = \frac{dx^k}{ds_{(i)}} = \frac{\delta_i^k dx^i}{\sqrt{g_{ii}} dx^i} = \frac{\delta_i^k}{\sqrt{g_{ii}}}$$

---

### 2. Cosine of the Angle $\theta_{ij}$ between Coordinate Curves
The Riemannian angle $\theta_{ij}$ between the $i$-th coordinate curve (direction $u_{(i)}$) and $j$-th coordinate curve (direction $u_{(j)}$) is given by:
$$\cos\theta_{ij} = g_{kl} u_{(i)}^k u_{(j)}^l$$
Substitute $u_{(i)}^k = \frac{\delta_i^k}{\sqrt{g_{ii}}}$ and $u_{(j)}^l = \frac{\delta_j^l}{\sqrt{g_{jj}}}$:
$$\cos\theta_{ij} = g_{kl} \left(\frac{\delta_i^k}{\sqrt{g_{ii}}}\right) \left(\frac{\delta_j^l}{\sqrt{g_{jj}}}\right) = \frac{g_{kl} \delta_i^k \delta_j^l}{\sqrt{g_{ii}} \sqrt{g_{jj}}} = \frac{g_{ij}}{\sqrt{g_{ii} g_{jj}}} \quad (\text{no sum on } i, j)$$

---

### 3. Proof of Mutual Orthogonality Criterion
The coordinate curves $x^i$ and $x^j$ ($i \ne j$) are orthogonal if and only if $\theta_{ij} = \pi/2$, which means:
$$\cos\theta_{ij} = 0 \iff \frac{g_{ij}}{\sqrt{g_{ii} g_{jj}}} = 0$$
Since $g_{ii} > 0$ and $g_{jj} > 0$ in a positive-definite Riemannian space:
$$\cos\theta_{ij} = 0 \iff g_{ij} = 0$$
Therefore, the coordinate curves are mutually orthogonal if and only if the metric tensor is purely diagonal ($g_{ij} = 0$ for all $i \ne j$). $\blacksquare$

---

### 4. Oblique Coordinates in $\mathbb{R}^2$ with Angle $\omega$
In Cartesian coordinates, let the $x^1$-axis lie along the $x$-axis and the $x^2$-axis be tilted at angle $\omega$:
$$\mathbf{r}(x^1, x^2) = (x^1 + x^2 \cos\omega) \hat{\mathbf{i}} + (x^2 \sin\omega) \hat{\mathbf{j}}$$
Differentiating:
$$\mathbf{e}_1 = \frac{\partial \mathbf{r}}{\partial x^1} = \hat{\mathbf{i}}$$
$$\mathbf{e}_2 = \frac{\partial \mathbf{r}}{\partial x^2} = \cos\omega \hat{\mathbf{i}} + \sin\omega \hat{\mathbf{j}}$$
Computing the metric components:
- $g_{11} = \mathbf{e}_1 \cdot \mathbf{e}_1 = 1$
- $g_{12} = \mathbf{e}_1 \cdot \mathbf{e}_2 = \cos\omega$
- $g_{22} = \mathbf{e}_2 \cdot \mathbf{e}_2 = \cos^2\omega + \sin^2\omega = 1$

Thus, the metric tensor is:
$$(g_{ij}) = \begin{pmatrix} 1 & \cos\omega \\ \cos\omega & 1 \end{pmatrix}$$
Determinant:
$$g = \det(g_{ij}) = 1 - \cos^2\omega = \sin^2\omega$$
The conjugate metric tensor is:
$$(g^{ij}) = \frac{1}{\sin^2\omega} \begin{pmatrix} 1 & -\cos\omega \\ -\cos\omega & 1 \end{pmatrix} \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 3.3: Poincaré Upper Half-Plane $\mathbb{H}^2$ & Invariance under $PSL(2, \mathbb{R})$",
                "statement": r"""Consider the Poincaré upper half-plane model of 2D hyperbolic geometry:
$$\mathbb{H}^2 = \{(x, y) \in \mathbb{R}^2 \mid y > 0\}$$
equipped with the Riemannian metric:
$$ds^2 = \frac{dx^2 + dy^2}{y^2} = \frac{(dx^1)^2 + (dx^2)^2}{(x^2)^2}$$
where $x^1 = x, x^2 = y$.

1. Write down the metric matrix $(g_{ij})$, compute its determinant $g$, and find the conjugate metric $(g^{ij})$.
2. Express the hyperbolic metric in complex coordinate notation $z = x + i y \in \mathbb{C}$ with $y = \text{Im}(z) = \frac{z - \bar{z}}{2i}$.
3. Consider a general Möbius transformation:
   $$w = \frac{a z + b}{c z + d}, \qquad \text{where } a, b, c, d \in \mathbb{R} \text{ and } ad - bc = 1 \quad (PSL(2, \mathbb{R}))$$
   Prove rigorously that the metric $ds^2$ is **strictly invariant** under all such transformations ($d\tilde{s}^2 = ds^2$).
4. Compute the hyperbolic distance between two points $(0, y_1)$ and $(0, y_2)$ along the vertical $y$-axis.""",
                "hints": [
                    "Notice that $dx^2 + dy^2 = |dz|^2 = dz d\\bar{z}$.",
                    "Compute $dw = \\frac{a(cz+d) - c(az+b)}{(cz+d)^2} dz = \\frac{ad-bc}{(cz+d)^2} dz$.",
                    "Compute $\\text{Im}(w) = \\frac{\\text{Im}(z)}{|cz+d|^2}$."
                ],
                "solution": r"""### 1. Metric Components and Conjugate Metric of $\mathbb{H}^2$
From $ds^2 = \frac{1}{(x^2)^2} (dx^1)^2 + \frac{1}{(x^2)^2} (dx^2)^2$:
$$(g_{ij}) = \begin{pmatrix} \frac{1}{y^2} & 0 \\ 0 & \frac{1}{y^2} \end{pmatrix} = \frac{1}{y^2} I_2$$
Determinant:
$$g = \det(g_{ij}) = \left(\frac{1}{y^2}\right) \left(\frac{1}{y^2}\right) = \frac{1}{y^4} \implies \sqrt{g} = \frac{1}{y^2}$$
Conjugate metric tensor:
$$(g^{ij}) = (g_{ij})^{-1} = \begin{pmatrix} y^2 & 0 \\ 0 & y^2 \end{pmatrix} = y^2 I_2$$

---

### 2. Complex Coordinate Representation
Let $z = x + i y$. Then $dz = dx + i dy$ and $d\bar{z} = dx - i dy$.
The Euclidean numerator is:
$$|dz|^2 = dz \, d\bar{z} = (dx + i dy)(dx - i dy) = dx^2 + dy^2$$
The imaginary part is $\text{Im}(z) = y$.
Therefore, the hyperbolic metric is expressed compactly as:
$$ds^2 = \frac{|dz|^2}{(\text{Im}(z))^2} = \frac{dz \, d\bar{z}}{\left(\frac{z - \bar{z}}{2i}\right)^2} = -\frac{4 \, dz \, d\bar{z}}{(z - \bar{z})^2}$$

---

### 3. Invariance under Möbius Transformations $PSL(2, \mathbb{R})$
Let $w = \frac{a z + b}{c z + d}$ with $a, b, c, d \in \mathbb{R}$ and $ad - bc = 1$.

#### Step A: Differential $dw$
$$dw = \frac{d}{dz}\left( \frac{a z + b}{c z + d} \right) dz = \frac{a(c z + d) - c(a z + b)}{(c z + d)^2} dz = \frac{a d - b c}{(c z + d)^2} dz$$
Since $ad - bc = 1$:
$$dw = \frac{dz}{(c z + d)^2} \implies |dw|^2 = dw \, d\bar{w} = \frac{|dz|^2}{|c z + d|^4}$$

#### Step B: Imaginary Part $\text{Im}(w)$
$$\begin{aligned}
\text{Im}(w) &= \frac{w - \bar{w}}{2i} = \frac{1}{2i} \left( \frac{a z + b}{c z + d} - \frac{a \bar{z} + b}{c \bar{z} + d} \right) \\
&= \frac{1}{2i} \frac{(a z + b)(c \bar{z} + d) - (a \bar{z} + b)(c z + d)}{|c z + d|^2} \\
&= \frac{1}{2i} \frac{(a d - b c)(z - \bar{z})}{|c z + d|^2} = \frac{1}{2i} \frac{1 \cdot (2i \, \text{Im}(z))}{|c z + d|^2} \\
&= \frac{\text{Im}(z)}{|c z + d|^2}
\end{aligned}$$

#### Step C: Ratio for Transformed Metric
Now assemble the transformed hyperbolic metric $d\tilde{s}^2$:
$$d\tilde{s}^2 = \frac{|dw|^2}{(\text{Im}(w))^2} = \frac{\frac{|dz|^2}{|c z + d|^4}}{\left( \frac{\text{Im}(z)}{|c z + d|^2} \right)^2} = \frac{\frac{|dz|^2}{|c z + d|^4}}{\frac{(\text{Im}(z))^2}{|c z + d|^4}} = \frac{|dz|^2}{(\text{Im}(z))^2} = ds^2$$

The conformal denominators $|c z + d|^4$ cancel out identically!
Thus, $ds^2$ is **strictly invariant** under the entire Möbius group $PSL(2, \mathbb{R})$ of hyperbolic isometries. $\blacksquare$

---

### 4. Hyperbolic Distance along the Vertical Line $x = 0$
Along the line $x = 0$, $dx = 0$, so $ds = \frac{dy}{y}$.
Integrating from $y_1$ to $y_2$ (assuming $y_2 > y_1 > 0$):
$$d_{\mathbb{H}}(y_1, y_2) = \int_{y_1}^{y_2} \frac{dy}{y} = \ln(y_2) - \ln(y_1) = \ln\left(\frac{y_2}{y_1}\right)$$
Notice that as $y_1 \to 0$ (approaching the boundary real axis), the hyperbolic distance diverges to $\infty$:
$$\lim_{y_1 \to 0} \ln\left(\frac{y_2}{y_1}\right) = +\infty$$
The boundary of the upper half-plane is infinitely far away in hyperbolic geometry! $\blacksquare$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u3 = get_unit3()
    print(f"Loaded Unit 3: {u3['title']} with {len(u3['sections'])} sections and {len(u3['problems'])} problems.")
