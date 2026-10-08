# -*- coding: utf-8 -*-
"""
build_dg_unit8.py
Constructs Unit 8: Fundamental Equations of Surface Theory & Theorema Egregium
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Fundamental Equations of Surface Theory & Theorema Egregium",
        "leadSummary": "The pinnacle of classical differential geometry: Gauss's moving frame and Christoffel symbols of the second kind, the Gauss and Codazzi-Mainardi compatibility integrability equations, Bonnet's fundamental existence and uniqueness theorem, Gauss's celebrated Theorema Egregium (the intrinsic nature of Gaussian curvature) and the Brioschi formula, geodesic differential equations and Clairaut's relation on surfaces of revolution, and the local Gauss-Bonnet theorem connecting curvature to topological angle excess.",
        "simulations": ["sim_dg_geodesic_egregium"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Gauss's Moving Frame & Christoffel Symbols of the Second Kind",
                "content": r"""### 1. The Moving Gauss Trihedron

At every regular point $p$ of a surface $S = \mathbf{r}(u, v)$, the three vectors:
$$\{\mathbf{r}_u, \mathbf{r}_v, \mathbf{n}\}$$
form a linearly independent basis of $\mathbb{R}^3$, known as **Gauss's moving frame** (analogous to the Frenet-Serret frame $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ for space curves).
Any vector in $\mathbb{R}^3$, in particular the second partial derivatives $\mathbf{r}_{uu}, \mathbf{r}_{uv}, \mathbf{r}_{vv}$, can be uniquely decomposed along this basis:
$$\begin{cases}
\mathbf{r}_{uu} = \Gamma_{11}^1 \mathbf{r}_u + \Gamma_{11}^2 \mathbf{r}_v + L \mathbf{n} \\
\mathbf{r}_{uv} = \Gamma_{12}^1 \mathbf{r}_u + \Gamma_{12}^2 \mathbf{r}_v + M \mathbf{n} \\
\mathbf{r}_{vv} = \Gamma_{22}^1 \mathbf{r}_u + \Gamma_{22}^2 \mathbf{r}_v + N \mathbf{n}
\end{cases}$$
The normal components are precisely the coefficients of the Second Fundamental Form:
$$\mathbf{r}_{uu} \cdot \mathbf{n} = L, \qquad \mathbf{r}_{uv} \cdot \mathbf{n} = M, \qquad \mathbf{r}_{vv} \cdot \mathbf{n} = N$$
The coefficients of the tangential components $\Gamma_{ij}^k$ are called the **Christoffel symbols of the second kind**.

---

### 2. Derivation of Christoffel Symbols in Terms of the Metric $E, F, G$

Because mixed partial derivatives commute for $C^2$ surfaces ($\mathbf{r}_{uv} = \mathbf{r}_{vu}$), the Christoffel symbols are symmetric in their lower indices:
$$\Gamma_{12}^1 = \Gamma_{21}^1, \qquad \Gamma_{12}^2 = \Gamma_{21}^2$$

To express $\Gamma_{ij}^k$ purely in terms of the metric coefficients $E, F, G$ and their partial derivatives, take the dot product of the Gauss decomposition equations with $\mathbf{r}_u$ and $\mathbf{r}_v$:
For $\mathbf{r}_{uu}$:
$$\begin{cases}
\mathbf{r}_{uu} \cdot \mathbf{r}_u = \Gamma_{11}^1 E + \Gamma_{11}^2 F \\
\mathbf{r}_{uu} \cdot \mathbf{r}_v = \Gamma_{11}^1 F + \Gamma_{11}^2 G
\end{cases}$$
Recall that:
$$\frac{\partial E}{\partial u} = \frac{\partial}{\partial u}(\mathbf{r}_u \cdot \mathbf{r}_u) = 2 \mathbf{r}_{uu} \cdot \mathbf{r}_u \implies \mathbf{r}_{uu} \cdot \mathbf{r}_u = \frac{1}{2} E_u$$
$$\frac{\partial F}{\partial u} = \frac{\partial}{\partial u}(\mathbf{r}_u \cdot \mathbf{r}_v) = \mathbf{r}_{uu} \cdot \mathbf{r}_v + \mathbf{r}_u \cdot \mathbf{r}_{uv} = \mathbf{r}_{uu} \cdot \mathbf{r}_v + \frac{1}{2} E_v \implies \mathbf{r}_{uu} \cdot \mathbf{r}_v = F_u - \frac{1}{2} E_v$$
Thus, we obtain the $2 \times 2$ linear system:
$$\begin{pmatrix} E & F \\ F & G \end{pmatrix} \begin{pmatrix} \Gamma_{11}^1 \\ \Gamma_{11}^2 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} E_u \\ F_u - \frac{1}{2} E_v \end{pmatrix}$$
Multiplying by the inverse metric matrix $g^{-1} = \frac{1}{EG - F^2}\begin{pmatrix} G & -F \\ -F & E \end{pmatrix}$:

> **Theorem 8.1 (Explicit Formulas for Christoffel Symbols):**
> Letting $D = EG - F^2 > 0$:
> $$\Gamma_{11}^1 = \frac{G E_u - 2F F_u + F E_v}{2D}, \qquad \Gamma_{11}^2 = \frac{2E F_u - E E_u - F E_u}{2D}$$
> For an **orthogonal coordinate system** ($F = 0$):
> $$\Gamma_{11}^1 = \frac{E_u}{2E}, \quad \Gamma_{11}^2 = -\frac{E_v}{2G}, \quad \Gamma_{12}^1 = \frac{E_v}{2E}, \quad \Gamma_{12}^2 = \frac{G_u}{2G}, \quad \Gamma_{22}^1 = -\frac{G_u}{2E}, \quad \Gamma_{22}^2 = \frac{G_v}{2G}$$

This shows that all six Christoffel symbols $\Gamma_{ij}^k$ are completely determined by the First Fundamental Form!"""
            },
            {
                "secNumber": "8.2",
                "title": "Gauss and Codazzi-Mainardi Compatibility Equations & Bonnet's Theorem",
                "content": r"""### 1. The Integrability Condition for Surfaces

For a smooth $C^3$ surface, the third partial derivatives of the position vector must commute:
$$\mathbf{r}_{uuv} = \mathbf{r}_{uvu} \iff \frac{\partial}{\partial v}(\mathbf{r}_{uu}) = \frac{\partial}{\partial u}(\mathbf{r}_{uv})$$
$$\mathbf{r}_{uvv} = \mathbf{r}_{vvu} \iff \frac{\partial}{\partial v}(\mathbf{r}_{uv}) = \frac{\partial}{\partial u}(\mathbf{r}_{vv})$$

Let us substitute the Gauss frame decompositions and Weingarten equations into $\frac{\partial}{\partial v}(\mathbf{r}_{uu}) = \frac{\partial}{\partial u}(\mathbf{r}_{uv})$:
$$\frac{\partial}{\partial v}(\Gamma_{11}^1 \mathbf{r}_u + \Gamma_{11}^2 \mathbf{r}_v + L \mathbf{n}) = \frac{\partial}{\partial u}(\Gamma_{12}^1 \mathbf{r}_u + \Gamma_{12}^2 \mathbf{r}_v + M \mathbf{n})$$
Expanding both sides using the product rule and substituting $\mathbf{r}_{uu}, \mathbf{r}_{uv}, \mathbf{r}_{vv}, \mathbf{n}_u, \mathbf{n}_v$ gives a linear combination of $\{\mathbf{r}_u, \mathbf{r}_v, \mathbf{n}\}$.
Because $\{\mathbf{r}_u, \mathbf{r}_v, \mathbf{n}\}$ is a basis of $\mathbb{R}^3$, the coefficients of $\mathbf{r}_u, \mathbf{r}_v,$ and $\mathbf{n}$ must match independently on both sides!

---

### 2. The Gauss Equation and the Codazzi-Mainardi Equations

Equating the coefficients of $\mathbf{r}_v$ yields the **Gauss Equation**:
$$LN - M^2 = F\left( \frac{\partial \Gamma_{12}^1}{\partial u} - \frac{\partial \Gamma_{11}^1}{\partial v} + \Gamma_{12}^2 \Gamma_{12}^1 - \Gamma_{11}^2 \Gamma_{22}^1 \right) + G\left( \frac{\partial \Gamma_{12}^2}{\partial u} - \frac{\partial \Gamma_{11}^2}{\partial v} + \Gamma_{12}^1 \Gamma_{11}^2 + (\Gamma_{12}^2)^2 - \Gamma_{11}^1 \Gamma_{12}^2 - \Gamma_{11}^2 \Gamma_{22}^2 \right)$$

Equating the normal components ($\mathbf{n}$) yields the **Codazzi-Mainardi Equations**:

> **Theorem 8.2 (The Codazzi-Mainardi Equations):**
> $$L_v - M_u = L \Gamma_{12}^1 + M(\Gamma_{12}^2 - \Gamma_{11}^1) - N \Gamma_{11}^2$$
> $$M_v - N_u = L \Gamma_{22}^1 + M(\Gamma_{22}^2 - \Gamma_{12}^1) - N \Gamma_{12}^2$$

---

### 3. Bonnet's Fundamental Theorem of Surface Theory

> **Theorem 8.3 (Bonnet's Theorem, 1867):**
> Let $U \subseteq \mathbb{R}^2$ be a simply connected domain.
> Let $E, F, G$ and $L, M, N$ be smooth functions on $U$ such that:
> 1. $E > 0$ and $EG - F^2 > 0$ (positive definiteness of $I$).
> 2. The Gauss equation is satisfied.
> 3. The Codazzi-Mainardi equations are satisfied.
> Then there exists a smooth regular surface patch $\mathbf{r}: U \to \mathbb{R}^3$ having $I$ and $II$ as its First and Second Fundamental Forms.
> Furthermore, this surface is **unique up to a rigid Euclidean motion** (rotation and translation) in $\mathbb{R}^3$!

Bonnet's theorem is the surface analogue of the Fundamental Theorem of Space Curves (Theorem 2.5), stating that $I$ and $II$ completely characterize a surface up to rigid positioning in space."""
            },
            {
                "secNumber": "8.3",
                "title": "Gauss's Theorema Egregium & The Brioschi Determinant Formula",
                "content": r"""### 1. Gauss's Remarkable Discovery: Theorema Egregium

In 1827, Carl Friedrich Gauss proved what he appropriately named the **Theorema Egregium** ("Remarkable Theorem"), one of the most celebrated results in all of mathematics.
By definition, Gaussian curvature is extrinsic:
$$K = \frac{LN - M^2}{EG - F^2}$$
It was computed via the Second Fundamental Form $II$, which relies on the surface normal $\mathbf{n}$ and the 3D spatial embedding.

> **Theorem 8.4 (Gauss's Theorema Egregium, 1827):**
> The Gaussian Curvature $K$ of a regular surface in $\mathbb{R}^3$ depends **only** on the coefficients of the First Fundamental Form $E, F, G$ and their first and second derivatives.
> That is, $K$ is an **intrinsic invariant** of the surface!

> **Proof:**
> By the Gauss compatibility equation derived in Section 8.2:
> $$LN - M^2 = \text{expression involving only } E, F, G \text{ and their first and second derivatives}$$
> Dividing both sides by $EG - F^2$:
> $$K = \frac{LN - M^2}{EG - F^2}$$
> Since both $LN - M^2$ and $EG - F^2$ are completely expressible in terms of $E, F, G, E_u, E_v, F_u, F_v, G_u, G_v$ and their second derivatives, $K$ depends exclusively on the metric! $\blacksquare$

> **Profound Corollaries:**
> 1. **Invariance Under Isometry:** If two surfaces are locally isometric, they have identical Gaussian curvature at corresponding points: $K_1 = K_2$.
> 2. **Impossible Planar Map of the Earth:** A flat sheet of paper has $K = 0$. A sphere of radius $R$ has $K = 1/R^2 > 0$. Since $K_{\text{sphere}} \ne K_{\text{plane}}$, **it is mathematically impossible to construct a distance-preserving flat map of any portion of the Earth without distortion**!

---

### 2. The Brioschi Determinant Formula for $K$

Francesco Brioschi (1852) gave a compact determinant expression for $K$:

> **Theorem 8.5 (Brioschi's Formula):**
> For any regular coordinate patch with metric $E, F, G$ and $D = EG - F^2$:
> $$K = \frac{1}{D^2} \left[ \det \begin{pmatrix} -\frac{1}{2} E_{vv} + F_{uv} - \frac{1}{2} G_{uu} & \frac{1}{2} E_u & F_u - \frac{1}{2} E_v \\ F_v - \frac{1}{2} G_u & E & F \\ \frac{1}{2} G_v & F & G \end{pmatrix} - \det \begin{pmatrix} 0 & \frac{1}{2} E_v & \frac{1}{2} G_u \\ \frac{1}{2} E_v & E & F \\ \frac{1}{2} G_u & F & G \end{pmatrix} \right]$$

For an **orthogonal coordinate patch** ($F = 0$), Brioschi's formula simplifies to the famous formula:
$$K = -\frac{1}{2\sqrt{EG}} \left[ \frac{\partial}{\partial u}\left( \frac{G_u}{\sqrt{EG}} \right) + \frac{\partial}{\partial v}\left( \frac{E_v}{\sqrt{EG}} \right) \right]$$"""
            },
            {
                "secNumber": "8.4",
                "title": "Geodesics on Surfaces, Euler-Lagrange Equations & Clairaut's Relation",
                "content": r"""### 1. Geodesics: The Straightest Curves on a Surface

> **Definition 8.1 (Geodesic):**
> A regular curve $C: \mathbf{r}(s)$ parametrized by arc-length $s$ on a surface $S$ is called a **geodesic** if its acceleration vector $\mathbf{r}''(s)$ is perpendicular to the tangent plane $T_p S$ at every point:
> $$\mathbf{r}''(s) \parallel \mathbf{n}(s) \iff \mathbf{r}''(s) = \kappa_n \mathbf{n}(s)$$
> Equivalently, its geodesic curvature vanishes identically: $\mathbf{k}_g = \mathbf{0}$.

Geodesics represent:
1. Curves of zero intrinsic acceleration (free-particle trajectories constrained to the surface).
2. Curves that locally minimize arc-length between two nearby points on the surface.

---

### 2. The Differential Equations of Geodesics

Let a curve be parametrized by arc-length $s$: $u = u(s), v = v(s)$.
The velocity vector is $\mathbf{r}'(s) = \mathbf{r}_u u' + \mathbf{r}_v v'$.
The acceleration vector is:
$$\mathbf{r}''(s) = \mathbf{r}_{uu}(u')^2 + 2\mathbf{r}_{uv} u' v' + \mathbf{r}_{vv}(v')^2 + \mathbf{r}_u u'' + \mathbf{r}_v v''$$
Substituting the Gauss frame decompositions $\mathbf{r}_{ij} = \Gamma_{ij}^1 \mathbf{r}_u + \Gamma_{ij}^2 \mathbf{r}_v + b_{ij} \mathbf{n}$:
$$\mathbf{r}''(s) = \left[ u'' + \Gamma_{11}^1 (u')^2 + 2\Gamma_{12}^1 u' v' + \Gamma_{22}^1 (v')^2 \right] \mathbf{r}_u + \left[ v'' + \Gamma_{11}^2 (u')^2 + 2\Gamma_{12}^2 u' v' + \Gamma_{22}^2 (v')^2 \right] \mathbf{r}_v + II(u', v') \mathbf{n}$$
For $\mathbf{r}''(s)$ to be parallel to $\mathbf{n}$, its tangential components along $\mathbf{r}_u$ and $\mathbf{r}_v$ must vanish!

> **Theorem 8.6 (Geodesic Differential Equations):**
> A curve $u(s), v(s)$ is a geodesic if and only if it satisfies the coupled non-linear ODEs:
> $$\frac{d^2 u}{ds^2} + \Gamma_{11}^1 \left(\frac{du}{ds}\right)^2 + 2\Gamma_{12}^1 \left(\frac{du}{ds}\right)\left(\frac{dv}{ds}\right) + \Gamma_{22}^1 \left(\frac{dv}{ds}\right)^2 = 0$$
> $$\frac{d^2 v}{ds^2} + \Gamma_{11}^2 \left(\frac{du}{ds}\right)^2 + 2\Gamma_{12}^2 \left(\frac{du}{ds}\right)\left(\frac{dv}{ds}\right) + \Gamma_{22}^2 \left(\frac{dv}{ds}\right)^2 = 0$$

By standard ODE existence and uniqueness theory, given any initial point $p \in S$ and initial unit tangent direction $\mathbf{v} \in T_p S$, there exists a **unique** geodesic starting at $p$ with initial velocity $\mathbf{v}$!

---

### 3. Clairaut's Relation on Surfaces of Revolution

For a surface of revolution $\mathbf{r}(u, v) = (r(u)\cos v, r(u)\sin v, z(u))$ where $r(u)$ is the distance to the axis of rotation:

> **Theorem 8.7 (Clairaut's Relation, 1735):**
> Along any geodesic on a surface of revolution:
> $$r \sin \alpha = \text{constant}$$
> where $r$ is the radius (distance to the rotation axis) and $\alpha$ is the angle made by the geodesic with the meridian curve."""
            },
            {
                "secNumber": "8.5",
                "title": "Geodesic Curvature, Liouville's Formula & The Local Gauss-Bonnet Theorem",
                "content": r"""### 1. Geodesic Curvature $\kappa_g$ and the Darboux Frame

For a curve $C: \mathbf{r}(s)$ on a surface $S$, consider the **Darboux frame** $\{\mathbf{T}, \mathbf{V}, \mathbf{n}\}$:
- $\mathbf{T} = \mathbf{r}'(s)$ is the unit tangent vector.
- $\mathbf{n}$ is the surface unit normal.
- $\mathbf{V} = \mathbf{n} \times \mathbf{T}$ is the **intrinsic normal** lying in the tangent plane $T_p S$.

The acceleration vector decomposes as:
$$\mathbf{r}''(s) = \kappa_g \mathbf{V} + \kappa_n \mathbf{n}$$
where:
- $\kappa_n = \mathbf{r}''(s) \cdot \mathbf{n}$ is the normal curvature.
- $\kappa_g = \mathbf{r}''(s) \cdot \mathbf{V} = \det(\mathbf{T}, \mathbf{r}'', \mathbf{n})$ is the **geodesic curvature**.

By the Pythagorean theorem:
$$\kappa^2 = \kappa_n^2 + \kappa_g^2$$
where $\kappa$ is the space curvature of the curve.
Geodesic curvature $\kappa_g$ measures how much the curve curves **within the surface itself**. A curve is a geodesic if and only if $\kappa_g \equiv 0$.

---

### 2. Liouville's Formula for Geodesic Curvature

In an orthogonal coordinate system ($F = 0$):
Let $\alpha$ be the angle that the unit tangent $\mathbf{T}$ makes with the $u$-coordinate curve ($\mathbf{r}_u / \sqrt{E}$).

> **Theorem 8.8 (Liouville's Formula):**
> $$\kappa_g = \frac{d\alpha}{ds} + \frac{1}{2\sqrt{EG}} \left[ E_v \cos\alpha - G_u \sin\alpha \right]$$

---

### 3. The Local Gauss-Bonnet Theorem

The Gauss-Bonnet theorem connects the differential geometry of curvature directly to the global topology of the surface!

> **Theorem 8.9 (Local Gauss-Bonnet Theorem):**
> Let $T \subset S$ be a simply connected region (e.g., a curvilinear geodesic triangle) bounded by a piecewise smooth curve $\partial T$ with exterior angles $\epsilon_1, \epsilon_2, \dots, \epsilon_k$ at the corners.
> Then:
> $$\iint_T K \, dA + \int_{\partial T} \kappa_g \, ds + \sum_{i=1}^k \epsilon_i = 2\pi$$

> **Corollary 8.1 (Geodesic Triangles):**
> If $T$ is a **geodesic triangle** (its three boundary edges are geodesics, so $\kappa_g = 0$ along all edges) with interior angles $\alpha_1, \alpha_2, \alpha_3$:
> Since exterior angles are $\epsilon_i = \pi - \alpha_i$:
> $$\iint_T K \, dA + \sum_{i=1}^3 (\pi - \alpha_i) = 2\pi \iff \iint_T K \, dA = (\alpha_1 + \alpha_2 + \alpha_3) - \pi$$
> The integral of Gaussian curvature over the triangle equals the **angular excess** $\Delta = \sum \alpha_i - \pi$!
> - On a sphere ($K > 0$): sum of angles $> \pi$.
> - On a plane ($K = 0$): sum of angles $= \pi$.
> - On a pseudosphere ($K < 0$): sum of angles $< \pi$."""
            }
        ],
        "problems": [
            {
                "id": "dg-prob-8-1",
                "tier": "Foundational",
                "title": "Christoffel Symbols & Intrinsic Flatness of the Cylinder",
                "statement": r"""Consider the cylinder parametrized by $\mathbf{r}(u, v) = (R \cos u, R \sin u, v)^T$ with $R > 0$.
1. Compute the metric coefficients $E, F, G$ and their partial derivatives.
2. Calculate all Christoffel symbols $\Gamma_{ij}^k$ for this patch.
3. Apply Brioschi's simplified formula for orthogonal coordinates to evaluate the Gaussian curvature $K$ and confirm that the cylinder is intrinsically flat ($K = 0$).""",
                "hints": [
                    "Recall E = R^2, F = 0, G = 1.",
                    "Since E and G are constant, all partial derivatives vanish.",
                    "Substitute into the Christoffel formulas and the Brioschi formula."
                ],
                "solution": r"""### 1. Metric Coefficients and Derivatives
For $\mathbf{r}(u, v) = (R \cos u, R \sin u, v)^T$:
$$\mathbf{r}_u = \begin{pmatrix} -R \sin u \\ R \cos u \\ 0 \end{pmatrix}, \qquad \mathbf{r}_v = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$
Metric coefficients:
$$E = \mathbf{r}_u \cdot \mathbf{r}_u = R^2, \qquad F = \mathbf{r}_u \cdot \mathbf{r}_v = 0, \qquad G = \mathbf{r}_v \cdot \mathbf{r}_v = 1$$
Since $E, F, G$ are constants:
$$E_u = 0, \quad E_v = 0, \quad F_u = 0, \quad F_v = 0, \quad G_u = 0, \quad G_v = 0 \quad \blacksquare$$

---

### 2. Christoffel Symbols
For an orthogonal coordinate system ($F = 0$):
$$\Gamma_{11}^1 = \frac{E_u}{2E} = 0, \qquad \Gamma_{11}^2 = -\frac{E_v}{2G} = 0$$
$$\Gamma_{12}^1 = \frac{E_v}{2E} = 0, \qquad \Gamma_{12}^2 = \frac{G_u}{2G} = 0$$
$$\Gamma_{22}^1 = -\frac{G_u}{2E} = 0, \qquad \Gamma_{22}^2 = \frac{G_v}{2G} = 0$$
All Christoffel symbols vanish identically:
$$\Gamma_{ij}^k \equiv 0 \quad \forall i, j, k \in \{1, 2\} \quad \blacksquare$$

---

### 3. Gaussian Curvature via Brioschi's Formula
For orthogonal coordinates, Brioschi's formula gives:
$$K = -\frac{1}{2\sqrt{EG}} \left[ \frac{\partial}{\partial u}\left( \frac{G_u}{\sqrt{EG}} \right) + \frac{\partial}{\partial v}\left( \frac{E_v}{\sqrt{EG}} \right) \right]$$
Since $G_u = 0$ and $E_v = 0$:
$$K = -\frac{1}{2\sqrt{R^2 \cdot 1}} \left[ \frac{\partial}{\partial u}(0) + \frac{\partial}{\partial v}(0) \right] = 0 \quad \blacksquare$$

> **Conclusion:** Although the cylinder is curved in 3D space (extrinsic curvature), its Gaussian curvature is identically zero ($K = 0$). By Gauss's Theorema Egregium, the cylinder is **intrinsically flat** and locally isometric to the Euclidean plane!"""
            },
            {
                "id": "dg-prob-8-2",
                "tier": "Advanced",
                "title": "Geodesics on a Right Circular Cone & Planar Unfolding",
                "statement": r"""Consider a right circular cone with semi-vertical opening angle $\alpha \in (0, \pi/2)$, parametrized by:
$$\mathbf{r}(u, v) = \begin{pmatrix} u \sin\alpha \cos v \\ u \sin\alpha \sin v \\ u \cos\alpha \end{pmatrix}, \quad u > 0, \; v \in [0, 2\pi)$$
1. Compute the First Fundamental Form $I = E \, du^2 + G \, dv^2$.
2. Formulate the geodesic equations using the metric coefficients.
3. Show that under the polar coordinate substitution $\rho = u$ and $\theta = v \sin\alpha$, the metric transforms into the standard Euclidean metric $ds^2 = d\rho^2 + \rho^2 d\theta^2$. Conclude that geodesics on the cone correspond to straight lines in its planar development.""",
                "hints": [
                    "Compute partials r_u and r_v to find E = 1 and G = u^2 sin^2(alpha).",
                    "Use ds^2 = du^2 + u^2 sin^2(alpha) dv^2.",
                    "Substitute rho = u and theta = v sin(alpha) to see ds^2 = d(rho)^2 + rho^2 d(theta)^2."
                ],
                "solution": r"""### 1. Partial Derivatives and Metric
$$\mathbf{r}_u = \begin{pmatrix} \sin\alpha \cos v \\ \sin\alpha \sin v \\ \cos\alpha \end{pmatrix}, \qquad \mathbf{r}_v = \begin{pmatrix} -u \sin\alpha \sin v \\ u \sin\alpha \cos v \\ 0 \end{pmatrix}$$
Computing the dot products:
$$E = \mathbf{r}_u \cdot \mathbf{r}_u = \sin^2\alpha(\cos^2 v + \sin^2 v) + \cos^2\alpha = \sin^2\alpha + \cos^2\alpha = 1$$
$$F = \mathbf{r}_u \cdot \mathbf{r}_v = -u \sin^2\alpha \sin v \cos v + u \sin^2\alpha \sin v \cos v + 0 = 0$$
$$G = \mathbf{r}_v \cdot \mathbf{r}_v = u^2 \sin^2\alpha(\sin^2 v + \cos^2 v) = u^2 \sin^2\alpha$$
Thus, the First Fundamental Form is:
$$I = du^2 + u^2 \sin^2\alpha \, dv^2 \quad \blacksquare$$

---

### 2. Christoffel Symbols and Geodesic Equations
Non-vanishing metric derivative: $G_u = 2u \sin^2\alpha$.
All other derivatives of $E$ and $G$ vanish.
Christoffel symbols:
$$\Gamma_{22}^1 = -\frac{G_u}{2E} = -u \sin^2\alpha, \qquad \Gamma_{12}^2 = \frac{G_u}{2G} = \frac{2u \sin^2\alpha}{2u^2 \sin^2\alpha} = \frac{1}{u}$$
All other $\Gamma_{ij}^k = 0$.
The geodesic ODEs (Theorem 8.6) are:
$$\frac{d^2 u}{ds^2} - u \sin^2\alpha \left(\frac{dv}{ds}\right)^2 = 0$$
$$\frac{d^2 v}{ds^2} + \frac{2}{u} \left(\frac{du}{ds}\right)\left(\frac{dv}{ds}\right) = 0 \quad \blacksquare$$

---

### 3. Planar Development and Euclidean Transformation
Introduce new coordinates:
$$\rho = u, \qquad \theta = v \sin\alpha$$
Then:
$$d\rho = du, \qquad d\theta = \sin\alpha \, dv \implies dv = \frac{d\theta}{\sin\alpha}$$
Substitute these differentials into the First Fundamental Form:
$$ds^2 = du^2 + u^2 \sin^2\alpha \, dv^2 = d\rho^2 + \rho^2 \sin^2\alpha \left(\frac{d\theta}{\sin\alpha}\right)^2 = d\rho^2 + \rho^2 \, d\theta^2$$
This is the standard Euclidean metric in planar polar coordinates $(\rho, \theta)$!
Since local isometries preserve geodesics, any geodesic on the cone maps under this isometric coordinate change to a curve satisfying the geodesic equations in the Euclidean plane, which are **straight lines**:
$$\rho(\theta) \cos(\theta - \theta_0) = \rho_0$$
Thus, if we cut the cone along a generator and unfold it flat onto a desk, all geodesics become straight line segments! $\blacksquare$"""
            },
            {
                "id": "dg-prob-8-3",
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Proof of Gauss's Theorema Egregium",
                "statement": r"""Let $S \subset \mathbb{R}^3$ be a $C^3$ regular surface patch $\mathbf{r}(u, v)$.
1. Write down Gauss's frame decomposition for $\mathbf{r}_{uu}$ and $\mathbf{r}_{uv}$.
2. Compute the compatibility condition $\frac{\partial}{\partial v}(\mathbf{r}_{uu}) - \frac{\partial}{\partial u}(\mathbf{r}_{uv}) = \mathbf{0}$ and project it onto the tangent vector $\mathbf{r}_v$ by taking the dot product.
3. Use the Weingarten equations to simplify the extrinsic term, and prove rigorously that:
   $$LN - M^2 = F\left[ (\Gamma_{12}^1)_u - (\Gamma_{11}^1)_v + \Gamma_{12}^1 \Gamma_{12}^2 - \Gamma_{11}^1 \Gamma_{22}^2 \right] + G\left[ (\Gamma_{12}^2)_u - (\Gamma_{11}^2)_v + \Gamma_{12}^1 \Gamma_{11}^2 + (\Gamma_{12}^2)^2 - \Gamma_{11}^1 \Gamma_{12}^2 - \Gamma_{11}^2 \Gamma_{22}^2 \right]$$
4. Conclude that Gaussian curvature $K = \frac{LN - M^2}{EG - F^2}$ is an intrinsic invariant determined solely by the First Fundamental Form.""",
                "hints": [
                    "Expand (r_{uu})_v - (r_{uv})_u = 0 using the product rule on Christoffel symbols.",
                    "Use n_v . r_v = -N and n_u . r_v = -M from the Second Fundamental Form.",
                    "Show that the normal derivative contribution produces precisely LN - M^2."
                ],
                "solution": r"""### 1. Gauss Frame Decompositions
From Section 8.1, the second derivatives of $\mathbf{r}$ decompose as:
$$\mathbf{r}_{uu} = \Gamma_{11}^1 \mathbf{r}_u + \Gamma_{11}^2 \mathbf{r}_v + L \mathbf{n}$$
$$\mathbf{r}_{uv} = \Gamma_{12}^1 \mathbf{r}_u + \Gamma_{12}^2 \mathbf{r}_v + M \mathbf{n}$$
$$\mathbf{r}_{vv} = \Gamma_{22}^1 \mathbf{r}_u + \Gamma_{22}^2 \mathbf{r}_v + N \mathbf{n}$$

---

### 2. Differentiating and Compatibility Condition
Differentiating $\mathbf{r}_{uu}$ with respect to $v$:
$$\mathbf{r}_{uuv} = (\Gamma_{11}^1)_v \mathbf{r}_u + \Gamma_{11}^1 \mathbf{r}_{uv} + (\Gamma_{11}^2)_v \mathbf{r}_v + \Gamma_{11}^2 \mathbf{r}_{vv} + L_v \mathbf{n} + L \mathbf{n}_v$$
Differentiating $\mathbf{r}_{uv}$ with respect to $u$:
$$\mathbf{r}_{uvu} = (\Gamma_{12}^1)_u \mathbf{r}_u + \Gamma_{12}^1 \mathbf{r}_{uu} + (\Gamma_{12}^2)_u \mathbf{r}_v + \Gamma_{12}^2 \mathbf{r}_{uv} + M_u \mathbf{n} + M \mathbf{n}_u$$
By smoothness ($C^3$), $\mathbf{r}_{uuv} = \mathbf{r}_{uvu}$.
Subtracting the two expressions:
$$\mathbf{0} = \mathbf{r}_{uuv} - \mathbf{r}_{uvu}$$
Now, isolate the term involving derivatives of the normal vector:
$$L \mathbf{n}_v - M \mathbf{n}_u$$
Taking the dot product with $\mathbf{r}_v$:
$$(L \mathbf{n}_v - M \mathbf{n}_u) \cdot \mathbf{r}_v = L(\mathbf{n}_v \cdot \mathbf{r}_v) - M(\mathbf{n}_u \cdot \mathbf{r}_v)$$
Recall from Theorem 5.2 that:
$$\mathbf{n}_v \cdot \mathbf{r}_v = -N, \qquad \mathbf{n}_u \cdot \mathbf{r}_v = -M$$
Substituting these values:
$$(L \mathbf{n}_v - M \mathbf{n}_u) \cdot \mathbf{r}_v = L(-N) - M(-M) = -(LN - M^2)$$

---

### 3. Projecting the Tangential Terms onto $\mathbf{r}_v$
Now substitute the Gauss frame expansions of $\mathbf{r}_{uu}, \mathbf{r}_{uv}, \mathbf{r}_{vv}$ into $\mathbf{r}_{uuv} - \mathbf{r}_{uvu}$ and take the dot product with $\mathbf{r}_v$.
Recall that $\mathbf{r}_u \cdot \mathbf{r}_v = F$ and $\mathbf{r}_v \cdot \mathbf{r}_v = G$.
The normal component $L_v \mathbf{n} - M_u \mathbf{n}$ vanishes when dotted with $\mathbf{r}_v$ because $\mathbf{n} \cdot \mathbf{r}_v = 0$.
Collecting the coefficients of $\mathbf{r}_u$ and $\mathbf{r}_v$:
- The coefficient of $\mathbf{r}_u$ in $\mathbf{r}_{uuv} - \mathbf{r}_{uvu}$ is:
  $$C_1 = (\Gamma_{11}^1)_v + \Gamma_{11}^1 \Gamma_{12}^1 + \Gamma_{11}^2 \Gamma_{22}^1 - (\Gamma_{12}^1)_u - \Gamma_{12}^1 \Gamma_{11}^1 - \Gamma_{12}^2 \Gamma_{12}^1 = (\Gamma_{11}^1)_v - (\Gamma_{12}^1)_u + \Gamma_{11}^2 \Gamma_{22}^1 - \Gamma_{12}^2 \Gamma_{12}^1$$
- The coefficient of $\mathbf{r}_v$ in $\mathbf{r}_{uuv} - \mathbf{r}_{uvu}$ is:
  $$C_2 = (\Gamma_{11}^2)_v + \Gamma_{11}^1 \Gamma_{12}^2 + \Gamma_{11}^2 \Gamma_{22}^2 - (\Gamma_{12}^2)_u - \Gamma_{12}^1 \Gamma_{11}^2 - (\Gamma_{12}^2)^2$$
Taking the dot product with $\mathbf{r}_v$:
$$(\mathbf{r}_{uuv} - \mathbf{r}_{uvu}) \cdot \mathbf{r}_v = C_1 F + C_2 G - (LN - M^2) = 0$$
Rearranging gives:
$$LN - M^2 = F(-C_1) + G(-C_2)$$
$$LN - M^2 = F\left[ (\Gamma_{12}^1)_u - (\Gamma_{11}^1)_v + \Gamma_{12}^2 \Gamma_{12}^1 - \Gamma_{11}^2 \Gamma_{22}^1 \right] + G\left[ (\Gamma_{12}^2)_u - (\Gamma_{11}^2)_v + \Gamma_{12}^1 \Gamma_{11}^2 + (\Gamma_{12}^2)^2 - \Gamma_{11}^1 \Gamma_{12}^2 - \Gamma_{11}^2 \Gamma_{22}^2 \right] \quad \blacksquare$$

---

### 4. Conclusion of Gauss's Theorema Egregium
By Theorem 8.1, all Christoffel symbols $\Gamma_{ij}^k$ and their derivatives are completely determined by $E, F, G$ and their first and second derivatives.
Therefore, the quantity $LN - M^2$ is an **intrinsic invariant**.
Dividing by $EG - F^2$, the Gaussian curvature:
$$K = \frac{LN - M^2}{EG - F^2}$$
depends **exclusively** on the First Fundamental Form!
Hence, two-dimensional beings living on a surface could measure $K$ at every point by measuring lengths and angles within the surface, without ever knowing whether their surface is embedded in a 3-dimensional space! $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u = get_unit8()
    print(f"Loaded Unit 8: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
