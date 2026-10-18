# -*- coding: utf-8 -*-
"""
build_tensor_unit4.py
Constructs Unit 4: Christoffel Symbols & Affine Connections
Strictly ZERO course numbers.
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Christoffel Symbols & Affine Connections",
        "leadSummary": "Detailed theory of affine connections and Christoffel symbols of the first and second kind: index definitions [ij, k] and \\Gamma^k_{ij}, explicit non-tensorial coordinate transformation laws, metric compatibility identities, the fundamental divergence contraction \\Gamma^i_{ij} = \\partial_j \\ln \\sqrt{|g|}, geodesic equations of motion derived from the variational principle \\delta \\int ds = 0, and parallel transport along curves.",
        "simulations": ["sim_tensor_christoffel_geodesic"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Christoffel Symbols of the First Kind $[ij, k]$ & Second Kind $\\Gamma^k_{ij}$",
                "content": r"""### 1. Introduction and Historical Context
In Euclidean space with Cartesian coordinates, the partial derivatives of basis vectors vanish identically ($\partial_j \mathbf{e}_i = 0$), so ordinary partial derivatives of vector fields transform as tensors. However, in curvilinear coordinates or on a curved Riemannian manifold, the coordinate basis vectors $\mathbf{e}_i = \frac{\partial \mathbf{r}}{\partial x^i}$ vary from point to point.

To quantify how the basis changes along coordinate directions, Elwin Bruno Christoffel (1869) introduced connection coefficients that express the derivatives of basis vectors in terms of the basis itself.

---

### 2. Christoffel Symbol of the First Kind $[ij, k]$

> **Definition 4.1 (Christoffel Symbol of the First Kind):**
> Let $g_{ij}$ be the covariant metric tensor of an $n$-dimensional Riemannian manifold $V_n$. The **Christoffel symbol of the first kind**, denoted by $[ij, k]$ or $\Gamma_{k, ij}$, is defined by the three-index metric derivative combination:
> $$[ij, k] = \frac{1}{2} \left( \frac{\partial g_{ik}}{\partial x^j} + \frac{\partial g_{jk}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^k} \right)$$

#### Essential Properties:
1. **Symmetry in Lower Indices:** Because $g_{ik} = g_{ki}$ and $g_{jk} = g_{kj}$:
   $$[ji, k] = \frac{1}{2} \left( \frac{\partial g_{jk}}{\partial x^i} + \frac{\partial g_{ik}}{\partial x^j} - \frac{\partial g_{ji}}{\partial x^k} \right) = [ij, k]$$
   The symbol $[ij, k]$ is strictly symmetric in its first two indices $i$ and $j$.
2. **Derivative of the Metric Tensor:**
   By adding $[ik, j]$ and $[jk, i]$:
   $$[ik, j] + [jk, i] = \frac{1}{2}\left(\partial_k g_{ij} + \partial_i g_{kj} - \partial_j g_{ik}\right) + \frac{1}{2}\left(\partial_k g_{ji} + \partial_j g_{ki} - \partial_i g_{jk}\right) = \frac{\partial g_{ij}}{\partial x^k}$$
   Hence, the partial derivative of any metric component can be expressed as a sum of Christoffel symbols:
   $$\frac{\partial g_{ij}}{\partial x^k} = [ik, j] + [jk, i]$$

---

### 3. Christoffel Symbol of the Second Kind $\Gamma^k_{ij}$

> **Definition 4.2 (Christoffel Symbol of the Second Kind):**
> The **Christoffel symbol of the second kind** (or Levi-Civita affine connection coefficients), denoted by $\Gamma^k_{ij}$ or $\begin{Bmatrix} k \\ ij \end{Bmatrix}$, is defined by raising the last index of $[ij, m]$ using the conjugate metric tensor $g^{km}$:
> $$\Gamma^k_{ij} = g^{km} [ij, m] = \frac{1}{2} g^{km} \left( \frac{\partial g_{im}}{\partial x^j} + \frac{\partial g_{jm}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^m} \right)$$

Conversely, lowering the upper index retrieves the symbol of the first kind:
$$g_{kl} \Gamma^k_{ij} = g_{kl} g^{km} [ij, m] = \delta_l^m [ij, m] = [ij, l]$$

#### Symmetry:
$$\Gamma^k_{ji} = g^{km} [ji, m] = g^{km} [ij, m] = \Gamma^k_{ij}$$
In a torsion-free (Levi-Civita) connection, $\Gamma^k_{ij}$ is symmetric in the lower indices $i$ and $j$. In an $n$-dimensional space, the number of independent components of $\Gamma^k_{ij}$ is:
$$N = n \times \frac{n(n+1)}{2} = \frac{n^2(n+1)}{2}$$
For $n = 2$: $2 \times 3 = 6$ components. For $n = 3$: $3 \times 6 = 18$ components. For $n = 4$: $4 \times 10 = 40$ components."""
            },
            {
                "secNumber": "4.2",
                "title": "Transformation Law of Christoffel Symbols (Affine Connection & Non-Tensor Nature)",
                "content": r"""### 1. Proof of the Inhomogeneous Transformation Law
A critical foundational result in differential geometry is that **Christoffel symbols are NOT tensors**. Under coordinate transformations, an inhomogeneous second-derivative term arises.

> **Theorem 4.1 (Non-Tensorial Transformation of $\Gamma^k_{ij}$):**
> Under a smooth, invertible coordinate transformation $x^i \to \bar{x}^\alpha$, the Christoffel symbols of the second kind transform according to:
> $$\bar{\Gamma}^\gamma_{\alpha\beta} = \frac{\partial \bar{x}^\gamma}{\partial x^k} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} \Gamma^k_{ij} + \frac{\partial \bar{x}^\gamma}{\partial x^k} \frac{\partial^2 x^k}{\partial \bar{x}^\alpha \partial \bar{x}^\beta}$$
> Alternatively, expressing in terms of derivatives of $\bar{x}$ on the right:
> $$\bar{\Gamma}^\gamma_{\alpha\beta} = \frac{\partial \bar{x}^\gamma}{\partial x^k} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} \Gamma^k_{ij} - \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} \frac{\partial^2 \bar{x}^\gamma}{\partial x^i \partial x^j}$$

#### Rigorous Proof:
Start with the transformation law of the metric tensor:
$$\bar{g}_{\alpha\beta} = g_{ij} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta}$$
Differentiating with respect to $\bar{x}^\mu$:
$$\frac{\partial \bar{g}_{\alpha\beta}}{\partial \bar{x}^\mu} = \frac{\partial g_{ij}}{\partial x^k} \frac{\partial x^k}{\partial \bar{x}^\mu} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} + g_{ij} \frac{\partial^2 x^i}{\partial \bar{x}^\mu \partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} + g_{ij} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial^2 x^j}{\partial \bar{x}^\mu \partial \bar{x}^\beta}$$
Forming the cyclic permutation combination for the first kind:
$$[\alpha\beta, \mu]_{\bar{x}} = \frac{1}{2}\left( \frac{\partial \bar{g}_{\alpha\mu}}{\partial \bar{x}^\beta} + \frac{\partial \bar{g}_{\beta\mu}}{\partial \bar{x}^\alpha} - \frac{\partial \bar{g}_{\alpha\beta}}{\partial \bar{x}^\mu} \right)$$
Substituting the derivatives of $\bar{g}$, the metric derivative terms combine to give $[ij, k] \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} \frac{\partial x^k}{\partial \bar{x}^\mu}$, while four of the second-derivative terms cancel symmetrically, leaving:
$$[\alpha\beta, \mu]_{\bar{x}} = [ij, k] \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} \frac{\partial x^k}{\partial \bar{x}^\mu} + g_{ij} \frac{\partial x^i}{\partial \bar{x}^\mu} \frac{\partial^2 x^j}{\partial \bar{x}^\alpha \partial \bar{x}^\beta}$$
Now multiply by $\bar{g}^{\gamma\mu} = g^{lm} \frac{\partial \bar{x}^\gamma}{\partial x^l} \frac{\partial \bar{x}^\mu}{\partial x^m}$:
$$\bar{\Gamma}^\gamma_{\alpha\beta} = \bar{g}^{\gamma\mu} [\alpha\beta, \mu]_{\bar{x}} = \Gamma^l_{ij} \frac{\partial \bar{x}^\gamma}{\partial x^l} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} + \frac{\partial \bar{x}^\gamma}{\partial x^l} \frac{\partial^2 x^l}{\partial \bar{x}^\alpha \partial \bar{x}^\beta} \qquad \blacksquare$$

---

### 2. The Difference Between Two Connections is a Tensor
Although an individual connection $\Gamma^k_{ij}$ does not transform as a tensor, the difference between two arbitrary connections on the same manifold does:

> **Theorem 4.2:**
> If $\Gamma^k_{ij}$ and $\tilde{\Gamma}^k_{ij}$ are two affine connections on $M$, their difference:
> $$T^k_{ij} \equiv \Gamma^k_{ij} - \tilde{\Gamma}^k_{ij}$$
> transforms as a **true tensor of type $(1, 2)$**.

*Proof:*
Subtracting their transformation equations, the non-tensorial second-derivative terms $\frac{\partial \bar{x}^\gamma}{\partial x^l} \frac{\partial^2 x^l}{\partial \bar{x}^\alpha \partial \bar{x}^\beta}$ are identical and cancel out:
$$\bar{\Gamma}^\gamma_{\alpha\beta} - \bar{\tilde{\Gamma}}^\gamma_{\alpha\beta} = \left( \Gamma^l_{ij} - \tilde{\Gamma}^l_{ij} \right) \frac{\partial \bar{x}^\gamma}{\partial x^l} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta}$$
which is the exact tensor transformation law for a $(1, 2)$ tensor. $\blacksquare$"""
            },
            {
                "secNumber": "4.3",
                "title": "Metric Compatibility, Metric Derivative Formulae & Symmetries",
                "content": r"""### 1. The Metric Compatibility Axiom
A Riemannian manifold $(M, g)$ possesses a unique affine connection $\nabla$ that is:
1. **Torsion-Free:** $\Gamma^k_{ij} = \Gamma^k_{ji}$ (or $\nabla_X Y - \nabla_Y X = [X, Y]$).
2. **Metric Compatible:** The inner product of any two parallel-transported vectors is preserved along any curve. In terms of the metric tensor:
   $$\nabla_k g_{ij} = 0$$

This unique connection is known as the **Levi-Civita connection**.

---

### 2. Fundamental Derivative Formulae
From metric compatibility and the definition of Christoffel symbols, we have several fundamental identities frequently used in tensor computations:

#### Identity 1: Derivative of Covariant Metric
$$\frac{\partial g_{ij}}{\partial x^k} = [ik, j] + [jk, i] = g_{mj} \Gamma^m_{ik} + g_{im} \Gamma^m_{jk}$$

#### Identity 2: Derivative of Contravariant Metric
Differentiating the relation $g_{im} g^{mj} = \delta_i^j$ with respect to $x^k$:
$$\frac{\partial g_{im}}{\partial x^k} g^{mj} + g_{im} \frac{\partial g^{mj}}{\partial x^k} = 0$$
Contracting with $g^{il}$:
$$\frac{\partial g^{lj}}{\partial x^k} = -g^{il} g^{mj} \frac{\partial g_{im}}{\partial x^k}$$
Substituting $\frac{\partial g_{im}}{\partial x^k} = g_{sm} \Gamma^s_{ik} + g_{is} \Gamma^s_{mk}$:
$$\frac{\partial g^{lj}}{\partial x^k} = -g^{il} g^{mj} (g_{sm} \Gamma^s_{ik} + g_{is} \Gamma^s_{mk}) = -g^{il} \Gamma^j_{ik} - g^{mj} \Gamma^l_{mk}$$
Renaming indices:
$$\frac{\partial g^{ij}}{\partial x^k} = -g^{mj} \Gamma^i_{mk} - g^{im} \Gamma^j_{mk}$$

---

### 3. Local Geodesic (Riemann Normal) Coordinates
By virtue of the inhomogeneous term in the transformation law:
$$\bar{\Gamma}^\gamma_{\alpha\beta} = \frac{\partial \bar{x}^\gamma}{\partial x^k} \frac{\partial x^i}{\partial \bar{x}^\alpha} \frac{\partial x^j}{\partial \bar{x}^\beta} \Gamma^k_{ij} + \frac{\partial \bar{x}^\gamma}{\partial x^k} \frac{\partial^2 x^k}{\partial \bar{x}^\alpha \partial \bar{x}^\beta}$$
At any given point $P$, one can choose a coordinate transformation such that:
$$\left. \frac{\partial^2 x^k}{\partial \bar{x}^\alpha \partial \bar{x}^\beta} \right|_P = -\left. \Gamma^k_{\alpha\beta} \right|_P$$
In this special coordinate frame (called **Riemann normal coordinates** centered at $P$):
$$\left. \bar{\Gamma}^\gamma_{\alpha\beta} \right|_P = 0, \qquad \left. \frac{\partial \bar{g}_{\alpha\beta}}{\partial \bar{x}^\gamma} \right|_P = 0$$
This is the mathematical embodiment of Einstein's **Equivalence Principle**: at any single spacetime point, the effects of gravitation (curvature) can be locally transformed away into a locally flat inertial frame."""
            },
            {
                "secNumber": "4.4",
                "title": "Contraction of Christoffel Symbols & The Divergence Formula $\\Gamma^i_{ij} = \\partial_j \\ln \\sqrt{|g|}$",
                "content": r"""### 1. Jacobi's Determinant Formula
Let $g = \det(g_{ij})$. From Jacobi's formula for the derivative of a matrix determinant:
$$\frac{\partial g}{\partial x^k} = g \, g^{ij} \frac{\partial g_{ij}}{\partial x^k}$$

#### Proof:
By Laplace expansion along row $i$:
$$g = \sum_{j=1}^n g_{ij} G^{ij}$$
where $G^{ij}$ is the cofactor. Since $g^{ij} = \frac{G^{ji}}{g} = \frac{G^{ij}}{g}$, we have $G^{ij} = g g^{ij}$.
Differentiating with respect to $g_{ij}$:
$$\frac{\partial g}{\partial g_{ij}} = G^{ij} = g g^{ij}$$
Applying the multivariable chain rule:
$$\frac{\partial g}{\partial x^k} = \frac{\partial g}{\partial g_{ij}} \frac{\partial g_{ij}}{\partial x^k} = g \, g^{ij} \frac{\partial g_{ij}}{\partial x^k} \qquad \blacksquare$$

---

### 2. The Contracted Christoffel Symbol $\Gamma^i_{ik}$

> **Theorem 4.3 (Contracted Connection Identity):**
> The contracted Christoffel symbol with upper index contracted against a lower index satisfies:
> $$\Gamma^i_{ik} = \Gamma^i_{ki} = \frac{1}{2} g^{ij} \frac{\partial g_{ij}}{\partial x^k} = \frac{1}{2g} \frac{\partial g}{\partial x^k} = \frac{\partial}{\partial x^k} \ln \sqrt{|g|}$$

#### Complete Proof:
From definition 4.2:
$$\Gamma^i_{ik} = \frac{1}{2} g^{im} \left( \frac{\partial g_{im}}{\partial x^k} + \frac{\partial g_{km}}{\partial x^i} - \frac{\partial g_{ik}}{\partial x^m} \right)$$
Distribute the contraction:
$$\Gamma^i_{ik} = \frac{1}{2} g^{im} \frac{\partial g_{im}}{\partial x^k} + \frac{1}{2} \left( g^{im} \frac{\partial g_{km}}{\partial x^i} - g^{im} \frac{\partial g_{ik}}{\partial x^m} \right)$$
In the second term, rename the dummy indices in $g^{im} \frac{\partial g_{ik}}{\partial x^m}$: swap $i \leftrightarrow m$.
Since $g^{im} = g^{mi}$, the term becomes $g^{mi} \frac{\partial g_{mk}}{\partial x^i} = g^{im} \frac{\partial g_{km}}{\partial x^i}$.
Thus, the second and third terms cancel identically:
$$g^{im} \frac{\partial g_{km}}{\partial x^i} - g^{im} \frac{\partial g_{ik}}{\partial x^m} = 0$$
We are left with:
$$\Gamma^i_{ik} = \frac{1}{2} g^{im} \frac{\partial g_{im}}{\partial x^k}$$
Using Jacobi's formula $g^{im} \frac{\partial g_{im}}{\partial x^k} = \frac{1}{g} \frac{\partial g}{\partial x^k}$:
$$\Gamma^i_{ik} = \frac{1}{2g} \frac{\partial g}{\partial x^k} = \frac{\partial}{\partial x^k} \left( \frac{1}{2} \ln |g| \right) = \frac{\partial}{\partial x^k} \ln \sqrt{|g|} \qquad \blacksquare$$

---

### 3. Divergence of a Contravariant Vector
This identity allows us to compute the invariant divergence of a vector field $A^i$ without needing individual Christoffel symbols:
$$\nabla_i A^i = \frac{\partial A^i}{\partial x^i} + \Gamma^i_{ki} A^k = \frac{\partial A^i}{\partial x^i} + A^k \frac{\partial}{\partial x^k} \ln \sqrt{|g|} = \frac{1}{\sqrt{|g|}} \frac{\partial}{\partial x^i} \left( \sqrt{|g|} A^i \right)$$
This proves that the divergence $\text{div}(\mathbf{A}) = \frac{1}{\sqrt{|g|}} \partial_i (\sqrt{|g|} A^i)$ is an invariant scalar!"""
            },
            {
                "secNumber": "4.5",
                "title": "Geodesic Equations of Motion & Geodesic Deviation",
                "content": r"""### 1. Geodesics as Extremals of Arc Length
In Riemannian geometry, a **geodesic** is the curve that extremizes the distance between two fixed points $P$ and $Q$.
Let the curve be parameterized by an arbitrary parameter $\lambda \in [\lambda_0, \lambda_1]$:
$$L = \int_{\lambda_0}^{\lambda_1} \sqrt{g_{ij}(x) \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}} \, d\lambda$$
Instead of the square root, it is standard and dynamically equivalent to extremize the **action / energy functional**:
$$S[x] = \frac{1}{2} \int \mathcal{L}(x, \dot{x}) \, d\lambda, \qquad \mathcal{L} = g_{ij} \dot{x}^i \dot{x}^j, \quad \dot{x}^i = \frac{dx^i}{d\lambda}$$

---

### 2. Derivation of the Geodesic Equation

> **Theorem 4.4 (The Geodesic Differential Equations):**
> If an affine parameter $s$ (the arc length parameter) is used, the Euler-Lagrange equations for the Lagrangian $\mathcal{L} = g_{ij} \frac{dx^i}{ds} \frac{dx^j}{ds}$ yield:
> $$\frac{d^2 x^k}{ds^2} + \Gamma^k_{ij} \frac{dx^i}{ds} \frac{dx^j}{ds} = 0$$

#### Step-by-Step Variational Derivation:
1. Compute the functional derivatives:
   $$\frac{\partial \mathcal{L}}{\partial x^k} = \frac{\partial g_{ij}}{\partial x^k} \dot{x}^i \dot{x}^j$$
   $$\frac{\partial \mathcal{L}}{\partial \dot{x}^k} = g_{kj} \dot{x}^j + g_{ik} \dot{x}^i = 2 g_{ki} \dot{x}^i$$
2. Apply the Euler-Lagrange equation $\frac{d}{ds}\left( \frac{\partial \mathcal{L}}{\partial \dot{x}^k} \right) - \frac{\partial \mathcal{L}}{\partial x^k} = 0$:
   $$\frac{d}{ds} \left( 2 g_{ki} \dot{x}^i \right) - \frac{\partial g_{ij}}{\partial x^k} \dot{x}^i \dot{x}^j = 0$$
   Expanding the total derivative via the chain rule $\frac{d}{ds} g_{ki} = \frac{\partial g_{ki}}{\partial x^j} \dot{x}^j$:
   $$2 g_{ki} \ddot{x}^i + 2 \frac{\partial g_{ki}}{\partial x^j} \dot{x}^j \dot{x}^i - \frac{\partial g_{ij}}{\partial x^k} \dot{x}^i \dot{x}^j = 0$$
3. Symmetrize the second term: $2 \frac{\partial g_{ki}}{\partial x^j} \dot{x}^i \dot{x}^j = \left( \frac{\partial g_{ki}}{\partial x^j} + \frac{\partial g_{kj}}{\partial x^i} \right) \dot{x}^i \dot{x}^j$.
   Grouping terms:
   $$2 g_{ki} \ddot{x}^i + \left( \frac{\partial g_{ki}}{\partial x^j} + \frac{\partial g_{kj}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^k} \right) \dot{x}^i \dot{x}^j = 0$$
   Recognizing the term in parentheses as $2 [ij, k]$:
   $$2 g_{ki} \ddot{x}^i + 2 [ij, k] \dot{x}^i \dot{x}^j = 0 \implies g_{ki} \ddot{x}^i + [ij, k] \dot{x}^i \dot{x}^j = 0$$
4. Contract with the conjugate metric $g^{km}$:
   $$g^{km} g_{ki} \ddot{x}^i + g^{km} [ij, k] \dot{x}^i \dot{x}^j = 0 \implies \delta_i^m \ddot{x}^i + \Gamma^m_{ij} \dot{x}^i \dot{x}^j = 0$$
   Renaming index $m \to k$:
   $$\frac{d^2 x^k}{ds^2} + \Gamma^k_{ij} \frac{dx^i}{ds} \frac{dx^j}{ds} = 0 \qquad \blacksquare$$

---

### 3. Geodesic Deviation & Tidal Forces
When two neighboring geodesics $x^i(s)$ and $x^i(s) + \xi^i(s)$ propagate with separation vector $\xi^i$, the relative acceleration of the geodesics is governed by the **Jacobi equation (Equation of Geodesic Deviation)**:
$$\frac{D^2 \xi^k}{ds^2} + R^k_{imj} \frac{dx^i}{ds} \xi^m \frac{dx^j}{ds} = 0$$
where $R^k_{imj}$ is the Riemann curvature tensor.
- In flat space ($R = 0$), $\frac{D^2 \xi^k}{ds^2} = 0$: initially parallel geodesics remain parallel forever (Euclid's 5th postulate).
- In curved space ($R \ne 0$), geodesics converge or diverge. In General Relativity, this relative acceleration is observed physically as **gravitational tidal force**!"""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 4.1: Christoffel Symbols for Cylindrical Polar Coordinates",
                "statement": r"""Consider 3D Euclidean space parameterized by cylindrical coordinates $(r, \theta, z) = (x^1, x^2, x^3)$ with metric:
$$ds^2 = dr^2 + r^2 d\theta^2 + dz^2$$

1. Write out the non-zero components of the metric tensor $g_{ij}$ and its conjugate $g^{ij}$.
2. Calculate all non-vanishing Christoffel symbols of the first kind $[ij, k]$.
3. Calculate all non-vanishing Christoffel symbols of the second kind $\Gamma^k_{ij}$.
4. Write down the three geodesic equations of motion in cylindrical coordinates.""",
                "hints": [
                    "Notice that only $g_{22} = r^2$ depends on coordinates (specifically $x^1 = r$).",
                    "All metric derivatives vanish except $\\partial_1 g_{22} = 2r$.",
                    "Use $[ij, k] = \\frac{1}{2}(\\partial_j g_{ik} + \\partial_i g_{jk} - \\partial_k g_{ij})$."
                ],
                "solution": r"""### 1. Metric Components
$$(g_{ij}) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & r^2 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad (g^{ij}) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \frac{1}{r^2} & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
Metric determinant: $g = r^2$, $\sqrt{g} = r$.

---

### 2. Metric Derivatives
The only non-zero partial derivative of metric components is:
$$\frac{\partial g_{22}}{\partial x^1} = \frac{\partial (r^2)}{\partial r} = 2r$$

---

### 3. Christoffel Symbols of the First Kind $[ij, k]$
Using $[ij, k] = \frac{1}{2}(\partial_j g_{ik} + \partial_i g_{jk} - \partial_k g_{ij})$:
- For $k = 1$:
  $$[22, 1] = \frac{1}{2}\left( \partial_2 g_{21} + \partial_2 g_{21} - \partial_1 g_{22} \right) = -\frac{1}{2}(2r) = -r$$
- For $k = 2$:
  $$[12, 2] = [21, 2] = \frac{1}{2}\left( \partial_2 g_{12} + \partial_1 g_{22} - \partial_2 g_{12} \right) = \frac{1}{2}(2r) = r$$
All other components $[ij, k] = 0$.

---

### 4. Christoffel Symbols of the Second Kind $\Gamma^k_{ij}$
Using $\Gamma^k_{ij} = g^{km} [ij, m]$:
- $\Gamma^1_{22} = g^{11} [22, 1] = 1 \cdot (-r) = -r$
- $\Gamma^2_{12} = \Gamma^2_{21} = g^{22} [12, 2] = \frac{1}{r^2} (r) = \frac{1}{r}$
All other $\Gamma^k_{ij} = 0$.

---

### 5. Geodesic Equations
The geodesic equations $\ddot{x}^k + \Gamma^k_{ij} \dot{x}^i \dot{x}^j = 0$ yield:
- For $k = 1$ ($r$):
  $$\frac{d^2 r}{ds^2} + \Gamma^1_{22} \left(\frac{d\theta}{ds}\right)^2 = 0 \implies \frac{d^2 r}{ds^2} - r \left(\frac{d\theta}{ds}\right)^2 = 0$$
  This is the familiar centripetal acceleration balance for uniform straight-line motion!
- For $k = 2$ ($\theta$):
  $$\frac{d^2 \theta}{ds^2} + 2\Gamma^2_{12} \frac{dr}{ds} \frac{d\theta}{ds} = 0 \implies \frac{d^2 \theta}{ds^2} + \frac{2}{r} \frac{dr}{ds} \frac{d\theta}{ds} = 0 \implies \frac{d}{ds}\left( r^2 \frac{d\theta}{ds} \right) = 0$$
  which represents conservation of angular momentum along a straight line.
- For $k = 3$ ($z$):
  $$\frac{d^2 z}{ds^2} = 0 \implies z(s) = a s + b \qquad \blacksquare$$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 4.2: Christoffel Symbols & Geodesics on the 2-Sphere $S^2$",
                "statement": r"""Consider the unit 2-sphere $S^2$ parameterized by spherical coordinates $(\theta, \phi) = (x^1, x^2)$ with metric:
$$ds^2 = d\theta^2 + \sin^2\theta \, d\phi^2$$

1. Calculate all Christoffel symbols of the second kind $\Gamma^k_{ij}$.
2. Verify explicitly that the contraction $\Gamma^i_{ik} = \partial_k \ln \sqrt{g}$.
3. Write out the geodesic equations for $(\theta(s), \phi(s))$.
4. Show that the equator $\theta(s) = \frac{\pi}{2}$ is an exact geodesic, while a parallel of latitude $\theta(s) = \theta_0 \ne \frac{\pi}{2}$ is NOT a geodesic.""",
                "hints": [
                    "Non-zero metric components: $g_{11} = 1, g_{22} = \\sin^2\\theta$. Determinant $g = \\sin^2\\theta$.",
                    "Compute $\\partial_1 g_{22} = 2\\sin\\theta\\cos\\theta$.",
                    "Evaluate $\\frac{d^2\\theta}{ds^2} - \\sin\\theta\\cos\\theta (\\dot{\\phi})^2 = 0$ for $\\theta = \\text{const}$."
                ],
                "solution": r"""### 1. Christoffel Symbols of $S^2$
Metric tensor:
$$g_{11} = 1, \quad g_{22} = \sin^2\theta, \quad g^{11} = 1, \quad g^{22} = \frac{1}{\sin^2\theta}, \quad g = \sin^2\theta$$
Derivative: $\partial_1 g_{22} = 2\sin\theta\cos\theta$. All other $\partial_k g_{ij} = 0$.

Christoffel symbols of the second kind:
- $\Gamma^1_{22} = g^{11}[22, 1] = 1 \cdot \left(-\frac{1}{2}\partial_1 g_{22}\right) = -\sin\theta\cos\theta$
- $\Gamma^2_{12} = \Gamma^2_{21} = g^{22}[12, 2] = \frac{1}{\sin^2\theta} \left(\frac{1}{2}\partial_1 g_{22}\right) = \frac{\sin\theta\cos\theta}{\sin^2\theta} = \cot\theta$
- All other components $\Gamma^1_{11} = \Gamma^1_{12} = \Gamma^2_{11} = \Gamma^2_{22} = 0$.

---

### 2. Verification of Contracted Identity
Determinant is $g = \sin^2\theta \implies \sqrt{g} = \sin\theta$.
- For $k = 1$ ($\theta$):
  $$\Gamma^i_{i1} = \Gamma^1_{11} + \Gamma^2_{21} = 0 + \cot\theta = \cot\theta$$
  Direct logarithmic derivative:
  $$\frac{\partial}{\partial\theta} \ln \sqrt{g} = \frac{\partial}{\partial\theta} \ln(\sin\theta) = \frac{\cos\theta}{\sin\theta} = \cot\theta$$
  Matches identically!
- For $k = 2$ ($\phi$):
  $$\Gamma^i_{i2} = \Gamma^1_{12} + \Gamma^2_{22} = 0 + 0 = 0$$
  Direct logarithmic derivative:
  $$\frac{\partial}{\partial\phi} \ln(\sin\theta) = 0$$
  Matches identically!

---

### 3. Geodesic Equations
$$\frac{d^2\theta}{ds^2} - \sin\theta\cos\theta \left(\frac{d\phi}{ds}\right)^2 = 0$$
$$\frac{d^2\phi}{ds^2} + 2\cot\theta \frac{d\theta}{ds} \frac{d\phi}{ds} = 0$$

---

### 4. Proof for Latitude Circles
Let $\theta(s) = \theta_0$ (constant). Then $\frac{d\theta}{ds} = 0$ and $\frac{d^2\theta}{ds^2} = 0$.
The second equation gives $\frac{d^2\phi}{ds^2} = 0 \implies \frac{d\phi}{ds} = \omega = \text{const} \ne 0$.
Substituting into the first geodesic equation:
$$0 - \sin\theta_0\cos\theta_0 \, \omega^2 = 0 \implies \sin\theta_0\cos\theta_0 = 0$$
Since $\theta_0 \in (0, \pi)$, $\sin\theta_0 > 0$.
Thus, we must have:
$$\cos\theta_0 = 0 \implies \theta_0 = \frac{\pi}{2}$$
Therefore, the equator $\theta = \frac{\pi}{2}$ is a geodesic (a great circle).
Any parallel of latitude with $\theta_0 \ne \frac{\pi}{2}$ has $\cos\theta_0 \ne 0$, which violates the geodesic equation. Hence, non-equatorial parallels are NOT geodesics. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 4.3: Euler-Lagrange Derivation of the Geodesic Equation & Conformal Metric Connection",
                "statement": r"""Consider two Riemannian metrics on $M$ related by a conformal factor $\Omega(x) = e^{\sigma(x)}$:
$$\tilde{g}_{ij} = e^{2\sigma(x)} g_{ij}$$

1. Derive the explicit relationship between the Christoffel symbols $\tilde{\Gamma}^k_{ij}$ of $\tilde{g}$ and $\Gamma^k_{ij}$ of $g$.
2. Prove that the difference $\tilde{\Gamma}^k_{ij} - \Gamma^k_{ij}$ transforms as a genuine tensor of type $(1, 2)$ and express it strictly in terms of the gradient $\partial_i \sigma = \sigma_{, i}$.
3. Compute the contracted Christoffel symbol difference $\tilde{\Gamma}^i_{ik} - \Gamma^i_{ik}$ in $n$ dimensions.
4. If $g_{ij} = \delta_{ij}$ (flat space), show how the conformal Christoffel symbols describe the geometry of hyperbolic space $\mathbb{H}^n$ where $e^{2\sigma} = \frac{1}{(x^n)^2}$.""",
                "hints": [
                    "Compute $\\partial_k \\tilde{g}_{ij} = 2 e^{2\\sigma} \\sigma_{, k} g_{ij} + e^{2\\sigma} \\partial_k g_{ij}$.",
                    "Inverse metric transforms as $\\tilde{g}^{km} = e^{-2\\sigma} g^{km}$.",
                    "Assemble $[ij, m]_{\\tilde{g}}$ and contract with $\\tilde{g}^{km}$."
                ],
                "solution": r"""### 1. Conformal Christoffel Symbols Derivation
Given $\tilde{g}_{ij} = e^{2\sigma} g_{ij}$ and $\tilde{g}^{km} = e^{-2\sigma} g^{km}$.
Partial derivatives of the metric:
$$\frac{\partial \tilde{g}_{ij}}{\partial x^k} = 2 e^{2\sigma} \sigma_{, k} g_{ij} + e^{2\sigma} \frac{\partial g_{ij}}{\partial x^k}$$
Compute the Christoffel symbol of the first kind:
$$\begin{aligned}
[ij, m]_{\tilde{g}} &= \frac{1}{2}\left( \partial_j \tilde{g}_{im} + \partial_i \tilde{g}_{jm} - \partial_m \tilde{g}_{ij} \right) \\
&= e^{2\sigma} [ij, m]_g + e^{2\sigma}\left( \sigma_{, j} g_{im} + \sigma_{, i} g_{jm} - \sigma_{, m} g_{ij} \right)
\end{aligned}$$
Now raise the index using $\tilde{g}^{km} = e^{-2\sigma} g^{km}$:
$$\begin{aligned}
\tilde{\Gamma}^k_{ij} &= \tilde{g}^{km} [ij, m]_{\tilde{g}} \\
&= e^{-2\sigma} g^{km} \left[ e^{2\sigma} [ij, m]_g + e^{2\sigma} (\sigma_{, j} g_{im} + \sigma_{, i} g_{jm} - \sigma_{, m} g_{ij}) \right] \\
&= \Gamma^k_{ij} + g^{km} \left( \sigma_{, j} g_{im} + \sigma_{, i} g_{jm} - \sigma_{, m} g_{ij} \right) \\
&= \Gamma^k_{ij} + \delta_i^k \sigma_{, j} + \delta_j^k \sigma_{, i} - g_{ij} g^{km} \sigma_{, m}
\end{aligned}$$
Letting $\sigma^{, k} = g^{km} \sigma_{, m} = \nabla^k \sigma$:
$$\tilde{\Gamma}^k_{ij} = \Gamma^k_{ij} + \delta_i^k \partial_j \sigma + \delta_j^k \partial_i \sigma - g_{ij} g^{km} \partial_m \sigma \qquad \blacksquare$$

---

### 2. Tensorial Nature of the Difference
The difference tensor is:
$$C^k_{ij} \equiv \tilde{\Gamma}^k_{ij} - \Gamma^k_{ij} = \delta_i^k \partial_j \sigma + \delta_j^k \partial_i \sigma - g_{ij} g^{km} \partial_m \sigma$$
Since $\sigma$ is a scalar field, $\partial_i \sigma$ is a covariant vector (type $(0, 1)$).
$\delta_i^k$ is the Kronecker tensor (type $(1, 1)$), and $g_{ij}$ and $g^{km}$ are metric tensors.
By tensor product and contraction rules, every term in $C^k_{ij}$ transforms as a true tensor of type $(1, 2)$.
Thus, $C^k_{ij}$ is rigorously a $(1, 2)$ tensor. $\blacksquare$

---

### 3. Contraction in $n$ Dimensions
Contract indices $k$ and $i$:
$$\begin{aligned}
\tilde{\Gamma}^i_{ik} - \Gamma^i_{ik} &= C^i_{ik} = \delta_i^i \partial_k \sigma + \delta_k^i \partial_i \sigma - g_{ik} g^{im} \partial_m \sigma \\
&= n \partial_k \sigma + \partial_k \sigma - \delta_k^m \partial_m \sigma \\
&= n \partial_k \sigma + \partial_k \sigma - \partial_k \sigma \\
&= n \partial_k \sigma
\end{aligned}$$
This beautiful result shows:
$$\tilde{\Gamma}^i_{ik} - \Gamma^i_{ik} = n \frac{\partial \sigma}{\partial x^k} \qquad \blacksquare$$
Check with determinant formula: $\tilde{g} = \det(\tilde{g}_{ij}) = e^{2n\sigma} g \implies \sqrt{\tilde{g}} = e^{n\sigma} \sqrt{g}$.
Then $\partial_k \ln \sqrt{\tilde{g}} = n \partial_k \sigma + \partial_k \ln \sqrt{g} \implies \tilde{\Gamma}^i_{ik} = n \partial_k \sigma + \Gamma^i_{ik}$, confirming exact consistency!

---

### 4. Application to Hyperbolic Space $\mathbb{H}^n$
In Poincaré upper half-space coordinates $(x^1, \dots, x^n)$ with $x^n > 0$:
$$d\tilde{s}^2 = \frac{\delta_{ij} dx^i dx^j}{(x^n)^2} \implies g_{ij} = \delta_{ij}, \quad e^{2\sigma} = (x^n)^{-2} \implies \sigma = -\ln x^n$$
Then $\Gamma^k_{ij} = 0$ (since background is flat Euclidean space).
The gradient of $\sigma$ is:
$$\partial_m \sigma = -\frac{1}{x^n} \delta_m^n$$
Hence $\sigma^{, m} = \delta^{ml} \partial_l \sigma = -\frac{1}{x^n} \delta^{mn}$.
Substitute into the conformal formula:
$$\tilde{\Gamma}^k_{ij} = -\frac{1}{x^n} \left( \delta_i^k \delta_j^n + \delta_j^k \delta_i^n - \delta_{ij} \delta^{kn} \right)$$
Specifically:
- For $i=n, j=n, k=n$: $\tilde{\Gamma}^n_{nn} = -\frac{1}{x^n}(1 + 1 - 1) = -\frac{1}{x^n}$.
- For $i=a, j=n, k=a$ ($a < n$): $\tilde{\Gamma}^a_{an} = -\frac{1}{x^n}(1 + 0 - 0) = -\frac{1}{x^n}$.
- For $i=a, j=b, k=n$ ($a, b < n$): $\tilde{\Gamma}^n_{ab} = -\frac{1}{x^n}(0 + 0 - \delta_{ab}) = \frac{\delta_{ab}}{x^n}$.
All other components vanish. This gives the complete connection for hyperbolic geometry in a single line! $\blacksquare$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u4 = get_unit4()
    print(f"Loaded Unit 4: {u4['title']} with {len(u4['sections'])} sections and {len(u4['problems'])} problems.")
