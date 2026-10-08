# -*- coding: utf-8 -*-
"""
build_dg_unit5.py
Constructs Unit 5: The Second Fundamental Form & The Weingarten Map
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "The Second Fundamental Form & The Weingarten Map",
        "leadSummary": "Extrinsic geometry of surfaces in Euclidean 3-space: the spherical Gauss map, the shape operator (Weingarten map) as a self-adjoint linear endomorphism of the tangent plane, the Second Fundamental Form $II = L du^2 + 2M dudv + N dv^2$, the Weingarten equations connecting derivatives of the normal vector to tangent vectors, the Third Fundamental Form $III$, the fundamental operator identity $III - 2H II + K I = 0$, and Meusnier's theorem for normal curvature.",
        "simulations": ["sim_dg_gauss_map_weingarten"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "The Gauss Map, Spherical Image & The Shape Operator",
                "content": r"""### 1. The Spherical Gauss Map

While the First Fundamental Form captures the intrinsic geometry of distances and angles within a surface, the way a surface bends and curves in the surrounding Euclidean space $\mathbb{R}^3$ is governed by how its unit normal vector changes from point to point.

> **Definition 5.1 (The Gauss Map):**
> Let $S \subset \mathbb{R}^3$ be an oriented regular surface with unit normal field $\mathbf{n}: S \to \mathbb{R}^3$, where $\|\mathbf{n}(p)\| = 1$ for all $p \in S$.
> The **Gauss map** is the smooth mapping:
> $$\mathbf{n}: S \to S^2 \subset \mathbb{R}^3, \quad p \mapsto \mathbf{n}(p)$$
> which assigns to each point $p \in S$ the point on the unit sphere $S^2$ corresponding to the unit normal vector at $p$.
> The image $\mathbf{n}(S) \subseteq S^2$ is called the **spherical image** of the surface.

---

### 2. The Differential of the Gauss Map and the Shape Operator

For each point $p \in S$, consider the differential of the Gauss map $d\mathbf{n}_p: T_p S \to T_{\mathbf{n}(p)} S^2$.
Because $\|\mathbf{n}(p)\|^2 = 1$, any variation of $\mathbf{n}$ must be orthogonal to $\mathbf{n}(p)$:
$$\frac{d}{dt} \|\mathbf{n}(t)\|^2 = 2 \mathbf{n} \cdot \frac{d\mathbf{n}}{dt} = 0 \implies d\mathbf{n}_p(\mathbf{w}) \cdot \mathbf{n}(p) = 0 \quad \forall \mathbf{w} \in T_p S$$
Since $T_p S$ is precisely the plane perpendicular to $\mathbf{n}(p)$, the tangent space to the unit sphere at $\mathbf{n}(p)$ is canonically identical to $T_p S$:
$$T_{\mathbf{n}(p)} S^2 = T_p S$$
Therefore, $d\mathbf{n}_p$ can be viewed as a linear operator from $T_p S$ to itself!

> **Definition 5.2 (Shape Operator / Weingarten Map):**
> The **Shape Operator** (or **Weingarten Map**) $S_p: T_p S \to T_p S$ is defined as the negative differential of the Gauss map:
> $$S_p(\mathbf{w}) = -d\mathbf{n}_p(\mathbf{w}), \quad \mathbf{w} \in T_p S$$
> The conventional minus sign ensures that for an outwardly convex surface (like a sphere with outward normal), the shape operator has positive eigenvalues.

---

### 3. Self-Adjointness of the Shape Operator

> **Theorem 5.1 (Symmetry / Self-Adjointness):**
> The Shape Operator $S_p: T_p S \to T_p S$ is a self-adjoint (symmetric) linear operator with respect to the metric inner product of $T_p S$:
> $$\langle S_p(\mathbf{w}_1), \mathbf{w}_2 \rangle = \langle \mathbf{w}_1, S_p(\mathbf{w}_2) \rangle \quad \forall \mathbf{w}_1, \mathbf{w}_2 \in T_p S$$

> **Proof:**
> It suffices to verify the identity on the basis vectors $\{\mathbf{r}_u, \mathbf{r}_v\}$ of $T_p S$.
> Note that $S_p(\mathbf{r}_u) = -\mathbf{n}_u$ and $S_p(\mathbf{r}_v) = -\mathbf{n}_v$.
> We must prove:
> $$\langle -\mathbf{n}_u, \mathbf{r}_v \rangle = \langle \mathbf{r}_u, -\mathbf{n}_v \rangle \iff \mathbf{n}_u \cdot \mathbf{r}_v = \mathbf{r}_u \cdot \mathbf{n}_v$$
> Since $\mathbf{n}$ is perpendicular to the tangent vectors everywhere on $S$:
> $$\mathbf{n} \cdot \mathbf{r}_u = 0 \quad \text{and} \quad \mathbf{n} \cdot \mathbf{r}_v = 0$$
> Differentiating $\mathbf{n} \cdot \mathbf{r}_u = 0$ with respect to $v$:
> $$\frac{\partial}{\partial v}(\mathbf{n} \cdot \mathbf{r}_u) = \mathbf{n}_v \cdot \mathbf{r}_u + \mathbf{n} \cdot \mathbf{r}_{uv} = 0 \implies \mathbf{r}_u \cdot \mathbf{n}_v = -\mathbf{n} \cdot \mathbf{r}_{uv}$$
> Similarly, differentiating $\mathbf{n} \cdot \mathbf{r}_v = 0$ with respect to $u$:
> $$\frac{\partial}{\partial u}(\mathbf{n} \cdot \mathbf{r}_v) = \mathbf{n}_u \cdot \mathbf{r}_v + \mathbf{n} \cdot \mathbf{r}_{vu} = 0 \implies \mathbf{n}_u \cdot \mathbf{r}_v = -\mathbf{n} \cdot \mathbf{r}_{vu}$$
> By Clairaut's theorem for $C^2$ surfaces, mixed partial derivatives commute: $\mathbf{r}_{uv} = \mathbf{r}_{vu}$.
> Therefore:
> $$\mathbf{n}_u \cdot \mathbf{r}_v = -\mathbf{n} \cdot \mathbf{r}_{uv} = \mathbf{r}_u \cdot \mathbf{n}_v$$
> Hence $\langle S_p(\mathbf{r}_u), \mathbf{r}_v \rangle = \langle \mathbf{r}_u, S_p(\mathbf{r}_v) \rangle$, proving that $S_p$ is self-adjoint. $\blacksquare$"""
            },
            {
                "secNumber": "5.2",
                "title": "The Second Fundamental Form: Coefficients L, M, N & Normal Curvature",
                "content": r"""### 1. Definition of the Second Fundamental Form

The self-adjoint shape operator $S_p$ naturally induces a symmetric bilinear form and quadratic form on the tangent space $T_p S$.

> **Definition 5.3 (The Second Fundamental Form):**
> The **Second Fundamental Form** of a surface $S$ at $p$, denoted by $II$ or $II_p$, is the quadratic form:
> $$II(\mathbf{w}) = \langle S_p(\mathbf{w}), \mathbf{w} \rangle = -d\mathbf{n}_p(\mathbf{w}) \cdot \mathbf{w}, \quad \mathbf{w} \in T_p S$$
> For an infinitesimal displacement $d\mathbf{r} = \mathbf{r}_u \, du + \mathbf{r}_v \, dv$, the quadratic form is:
> $$II(du, dv) = -d\mathbf{n} \cdot d\mathbf{r} = -(\mathbf{n}_u \, du + \mathbf{n}_v \, dv) \cdot (\mathbf{r}_u \, du + \mathbf{r}_v \, dv)$$
> Expanding bilinearly:
> $$II(du, dv) = L \, du^2 + 2M \, du \, dv + N \, dv^2$$
> (also conventionally written as $e \, du^2 + 2f \, du \, dv + g \, dv^2$ or $b_{11} du^2 + 2b_{12} dudv + b_{22} dv^2$).

---

### 2. Formulas for the Coefficients $L, M, N$

> **Theorem 5.2 (Computation of Coefficients $L, M, N$):**
> The coefficients of the Second Fundamental Form can be evaluated using either first derivatives of the normal vector or second derivatives of the position vector:
> $$L = -\mathbf{n}_u \cdot \mathbf{r}_u = \mathbf{r}_{uu} \cdot \mathbf{n} = \frac{\det(\mathbf{r}_{uu}, \mathbf{r}_u, \mathbf{r}_v)}{\sqrt{EG - F^2}}$$
> $$M = -\mathbf{n}_u \cdot \mathbf{r}_v = -\mathbf{n}_v \cdot \mathbf{r}_u = \mathbf{r}_{uv} \cdot \mathbf{n} = \frac{\det(\mathbf{r}_{uv}, \mathbf{r}_u, \mathbf{r}_v)}{\sqrt{EG - F^2}}$$
> $$N = -\mathbf{n}_v \cdot \mathbf{r}_v = \mathbf{r}_{vv} \cdot \mathbf{n} = \frac{\det(\mathbf{r}_{vv}, \mathbf{r}_u, \mathbf{r}_v)}{\sqrt{EG - F^2}}$$

> **Proof:**
> We proved in Section 5.1 that differentiating $\mathbf{n} \cdot \mathbf{r}_u = 0$ with respect to $u$ yields:
> $$\mathbf{n}_u \cdot \mathbf{r}_u + \mathbf{n} \cdot \mathbf{r}_{uu} = 0 \implies L = -\mathbf{n}_u \cdot \mathbf{r}_u = \mathbf{r}_{uu} \cdot \mathbf{n}$$
> Similarly, differentiating $\mathbf{n} \cdot \mathbf{r}_v = 0$ with respect to $v$ gives:
> $$\mathbf{n}_v \cdot \mathbf{r}_v + \mathbf{n} \cdot \mathbf{r}_{vv} = 0 \implies N = -\mathbf{n}_v \cdot \mathbf{r}_v = \mathbf{r}_{vv} \cdot \mathbf{n}$$
> And differentiating $\mathbf{n} \cdot \mathbf{r}_u = 0$ with respect to $v$ gives:
> $$\mathbf{n}_v \cdot \mathbf{r}_u + \mathbf{n} \cdot \mathbf{r}_{uv} = 0 \implies M = -\mathbf{n}_v \cdot \mathbf{r}_u = \mathbf{r}_{uv} \cdot \mathbf{n}$$
> Since $\mathbf{n} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{\|\mathbf{r}_u \times \mathbf{r}_v\|} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{\sqrt{EG - F^2}}$, the dot product $\mathbf{r}_{uu} \cdot \mathbf{n}$ is:
> $$\mathbf{r}_{uu} \cdot \mathbf{n} = \frac{\mathbf{r}_{uu} \cdot (\mathbf{r}_u \times \mathbf{r}_v)}{\sqrt{EG - F^2}} = \frac{\det(\mathbf{r}_{uu}, \mathbf{r}_u, \mathbf{r}_v)}{\sqrt{EG - F^2}}$$
> The formulas for $M$ and $N$ follow identically. $\blacksquare$"""
            },
            {
                "secNumber": "5.3",
                "title": "The Weingarten Equations & Tangent Operator Matrix",
                "content": r"""### 1. Resolving Normal Derivatives in the Tangent Basis

Since $\mathbf{n}(u, v)$ is a unit vector, its partial derivatives $\mathbf{n}_u$ and $\mathbf{n}_v$ are perpendicular to $\mathbf{n}$, and hence must lie entirely in the tangent plane $T_p S = \operatorname{span}\{\mathbf{r}_u, \mathbf{r}_v\}$.
Therefore, there exist scalar coefficients $a_{11}, a_{12}, a_{21}, a_{22}$ such that:
$$\begin{cases} -\mathbf{n}_u = a_{11} \mathbf{r}_u + a_{21} \mathbf{r}_v \\ -\mathbf{n}_v = a_{12} \mathbf{r}_u + a_{22} \mathbf{r}_v \end{cases}$$
The matrix $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$ represents the Shape Operator $S_p$ with respect to the coordinate basis $\{\mathbf{r}_u, \mathbf{r}_v\}$.

---

### 2. Derivation of the Weingarten Equations

Taking the dot product of $-\mathbf{n}_u = a_{11} \mathbf{r}_u + a_{21} \mathbf{r}_v$ with $\mathbf{r}_u$ and $\mathbf{r}_v$:
$$\begin{cases} -\mathbf{n}_u \cdot \mathbf{r}_u = a_{11}(\mathbf{r}_u \cdot \mathbf{r}_u) + a_{21}(\mathbf{r}_v \cdot \mathbf{r}_u) = a_{11} E + a_{21} F = L \\ -\mathbf{n}_u \cdot \mathbf{r}_v = a_{11}(\mathbf{r}_u \cdot \mathbf{r}_v) + a_{21}(\mathbf{r}_v \cdot \mathbf{r}_v) = a_{11} F + a_{21} G = M \end{cases}$$
Similarly, for $-\mathbf{n}_v = a_{12} \mathbf{r}_u + a_{22} \mathbf{r}_v$:
$$\begin{cases} -\mathbf{n}_v \cdot \mathbf{r}_u = a_{12} E + a_{22} F = M \\ -\mathbf{n}_v \cdot \mathbf{r}_v = a_{12} F + a_{22} G = N \end{cases}$$
In matrix form:
$$\begin{pmatrix} E & F \\ F & G \end{pmatrix} \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \begin{pmatrix} L & M \\ M & N \end{pmatrix} \iff g A = b$$
Multiplying by the inverse matrix $g^{-1} = \frac{1}{EG - F^2} \begin{pmatrix} G & -F \\ -F & E \end{pmatrix}$:
$$A = g^{-1} b = \frac{1}{EG - F^2} \begin{pmatrix} G & -F \\ -F & E \end{pmatrix} \begin{pmatrix} L & M \\ M & N \end{pmatrix}$$
Carrying out the matrix multiplication:
$$a_{11} = \frac{GL - FM}{EG - F^2}, \qquad a_{21} = \frac{EM - FL}{EG - F^2}$$
$$a_{12} = \frac{GM - FN}{EG - F^2}, \qquad a_{22} = \frac{EN - FM}{EG - F^2}$$

> **Theorem 5.3 (The Weingarten Equations):**
> The partial derivatives of the surface normal $\mathbf{n}$ are expressed in terms of the tangent vectors by:
> $$\mathbf{n}_u = \frac{FM - GL}{EG - F^2} \mathbf{r}_u + \frac{FL - EM}{EG - F^2} \mathbf{r}_v$$
> $$\mathbf{n}_v = \frac{FN - GM}{EG - F^2} \mathbf{r}_u + \frac{FM - EN}{EG - F^2} \mathbf{r}_v$$"""
            },
            {
                "secNumber": "5.4",
                "title": "The Third Fundamental Form & The Cayley-Hamilton Invariant Identity",
                "content": r"""### 1. Definition of the Third Fundamental Form

Just as the First Fundamental Form measures the length of tangent vectors on $S$ ($I(d\mathbf{r}) = \|d\mathbf{r}\|^2$), we can measure the length of their spherical images on $S^2$ under the Gauss map.

> **Definition 5.4 (The Third Fundamental Form):**
> The **Third Fundamental Form** of a surface $S$, denoted $III$, is the quadratic form defined by the Euclidean inner product of the differentials of the normal vector:
> $$III(du, dv) = \|d\mathbf{n}\|^2 = d\mathbf{n} \cdot d\mathbf{n} = (\mathbf{n}_u \, du + \mathbf{n}_v \, dv) \cdot (\mathbf{n}_u \, du + \mathbf{n}_v \, dv)$$
> Expanding:
> $$III(du, dv) = e \, du^2 + 2f \, du \, dv + g \, dv^2$$
> where:
> $$e = \mathbf{n}_u \cdot \mathbf{n}_u, \qquad f = \mathbf{n}_u \cdot \mathbf{n}_v, \qquad g = \mathbf{n}_v \cdot \mathbf{n}_v$$

In terms of the Shape Operator $S_p$:
$$III(\mathbf{w}) = \langle S_p(\mathbf{w}), S_p(\mathbf{w}) \rangle = \langle S_p^2(\mathbf{w}), \mathbf{w} \rangle$$

---

### 2. Characteristic Polynomial of the Shape Operator

Since $S_p: T_p S \to T_p S$ is a linear operator on a 2D vector space, its characteristic polynomial $P(\lambda)$ is:
$$P(\lambda) = \det(\lambda I_{\text{id}} - S_p) = \lambda^2 - \operatorname{tr}(S_p) \lambda + \det(S_p)$$
The two fundamental scalar invariants of $S_p$ are:
- **Mean Curvature:** $H = \frac{1}{2} \operatorname{tr}(S_p) = \frac{1}{2}(a_{11} + a_{22}) = \frac{EN - 2FM + GL}{2(EG - F^2)}$
- **Gaussian Curvature:** $K = \det(S_p) = \det(A) = \frac{LN - M^2}{EG - F^2}$
Thus:
$$P(\lambda) = \lambda^2 - 2H \lambda + K$$

---

### 3. The Fundamental Invariant Identity

> **Theorem 5.4 (Operator Identity and Fundamental Form Relation):**
> 1. By the **Cayley-Hamilton Theorem**, the Shape Operator satisfies its own characteristic equation:
>    $$S_p^2 - 2H S_p + K I_{\text{id}} = 0$$
> 2. Consequently, the three fundamental forms satisfy the universal linear relation:
>    $$III - 2H II + K I = 0 \iff III = 2H II - K I$$

> **Proof:**
> For any tangent vector $\mathbf{w} \in T_p S$, apply the Cayley-Hamilton operator equation:
> $$(S_p^2 - 2H S_p + K I_{\text{id}})(\mathbf{w}) = \mathbf{0}$$
> Taking the inner product with $\mathbf{w}$:
> $$\langle S_p^2(\mathbf{w}), \mathbf{w} \rangle - 2H \langle S_p(\mathbf{w}), \mathbf{w} \rangle + K \langle \mathbf{w}, \mathbf{w} \rangle = 0$$
> Recognizing the definitions:
> $$\langle S_p^2(\mathbf{w}), \mathbf{w} \rangle = III(\mathbf{w}), \quad \langle S_p(\mathbf{w}), \mathbf{w} \rangle = II(\mathbf{w}), \quad \langle \mathbf{w}, \mathbf{w} \rangle = I(\mathbf{w})$$
> Substituting these yields:
> $$III(\mathbf{w}) - 2H II(\mathbf{w}) + K I(\mathbf{w}) = 0 \quad \blacksquare$$"""
            },
            {
                "secNumber": "5.5",
                "title": "Normal Curvature & Meusnier's Geometric Theorem",
                "content": r"""### 1. Curvature of a Surface Curve and Normal Curvature

Let $C: \mathbf{r}(s)$ be a regular curve parametrized by arc-length $s$ lying on a regular surface $S$.
The unit tangent vector is $\mathbf{T}(s) = \mathbf{r}'(s) \in T_p S$.
By the Serret-Frenet formulas (Unit 2), the derivative of the tangent vector is:
$$\mathbf{r}''(s) = \kappa \mathbf{N}$$
where $\kappa$ is the space curvature of $C$ and $\mathbf{N}$ is the curve's principal normal vector.

Since $\mathbf{n}(s)$ is the surface normal and $\mathbf{T}(s)$ lies in the tangent plane, the acceleration vector $\mathbf{r}''(s)$ can be decomposed into two orthogonal components:
$$\mathbf{r}''(s) = \mathbf{k}_n + \mathbf{k}_g = \kappa_n \mathbf{n} + \mathbf{k}_g$$
where:
- $\mathbf{k}_n = \kappa_n \mathbf{n}$ is the **normal curvature vector**, directed along the surface normal $\mathbf{n}$.
- $\mathbf{k}_g$ is the **geodesic curvature vector**, lying in the tangent plane $T_p S$.

---

### 2. Formula for Normal Curvature

Taking the dot product of $\mathbf{r}''(s)$ with the surface unit normal $\mathbf{n}$:
$$\kappa_n = \mathbf{r}''(s) \cdot \mathbf{n}$$
Since $\mathbf{r}'(s) \cdot \mathbf{n}(s) = 0$ along the curve, differentiating with respect to $s$ gives:
$$\mathbf{r}''(s) \cdot \mathbf{n} + \mathbf{r}'(s) \cdot \mathbf{n}'(s) = 0 \implies \kappa_n = -\mathbf{n}'(s) \cdot \mathbf{r}'(s)$$
Writing $\mathbf{r}'(s) = \mathbf{r}_u u' + \mathbf{r}_v v'$:
$$\kappa_n = -(\mathbf{n}_u u' + \mathbf{n}_v v') \cdot (\mathbf{r}_u u' + \mathbf{r}_v v') = L (u')^2 + 2M u' v' + N (v')^2$$
For an arbitrary parameter $t$ (not necessarily arc-length):

> **Theorem 5.5 (Normal Curvature Formula):**
> The normal curvature of a surface along a tangent direction $d\mathbf{r} = (du, dv)$ is the ratio of the Second and First Fundamental Forms:
> $$\kappa_n = \frac{II(du, dv)}{I(du, dv)} = \frac{L \, du^2 + 2M \, du \, dv + N \, dv^2}{E \, du^2 + 2F \, du \, dv + G \, dv^2}$$

Notice that $\kappa_n$ depends **only** on the direction of the tangent vector $(du : dv)$ and the surface at $p$, and is completely independent of the curve chosen passing through $p$ with that tangent!

---

### 3. Meusnier's Theorem

> **Theorem 5.6 (Meusnier's Theorem, 1776):**
> Let $C$ be a regular curve on a surface $S$ passing through $p$ with curvature $\kappa > 0$ and principal normal $\mathbf{N}$.
> Let $\theta$ be the angle between the principal normal to the curve $\mathbf{N}$ and the surface normal $\mathbf{n}$ ($\cos \theta = \mathbf{N} \cdot \mathbf{n}$).
> Then:
> $$\kappa_n = \kappa \cos \theta$$
> Equivalently, the radius of curvature $\rho_n = 1/|\kappa_n|$ of the normal section is related to the radius of curvature $\rho = 1/\kappa$ of the curve by:
> $$\rho = \rho_n |\cos \theta|$$

> **Proof:**
> Starting from the definition:
> $$\kappa_n = \mathbf{r}''(s) \cdot \mathbf{n}$$
> By Serret-Frenet, $\mathbf{r}''(s) = \kappa \mathbf{N}$. Therefore:
> $$\kappa_n = (\kappa \mathbf{N}) \cdot \mathbf{n} = \kappa (\mathbf{N} \cdot \mathbf{n}) = \kappa \cos \theta \quad \blacksquare$$

> **Geometric Interpretation:**
> All curves lying on a surface passing through $p$ and sharing the same tangent line $\mathbf{T}$ have the same osculating circle projection onto the normal plane. If a plane section of the surface is tilted by an angle $\theta$ from the normal plane, its radius of curvature shrinks by a factor of $\cos \theta$!"""
            }
        ],
        "problems": [
            {
                "id": "dg-prob-5-1",
                "tier": "Foundational",
                "title": "Second Fundamental Form & Normal Curvature of a Circular Cylinder",
                "statement": r"""Consider a right circular cylinder of radius $R > 0$ parametrized by:
$$\mathbf{r}(u, v) = \begin{pmatrix} R \cos u \\ R \sin u \\ v \end{pmatrix}, \quad u \in (0, 2\pi), \; v \in \mathbb{R}$$
1. Find the unit normal vector $\mathbf{n}(u, v)$.
2. Calculate the Second Fundamental Form coefficients $L, M, N$.
3. Compute the normal curvature $\kappa_n$ along an arbitrary direction $(du, dv)$ and determine the directions of maximum and zero normal curvature.""",
                "hints": [
                    "Compute partials r_u, r_v and unit normal n = (r_u x r_v) / ||r_u x r_v||.",
                    "Compute r_{uu}, r_{uv}, r_{vv} and dot each with n.",
                    "Write kappa_n = (L du^2 + 2M dudv + N dv^2) / (E du^2 + 2F dudv + G dv^2)."
                ],
                "solution": r"""### 1. Partial Derivatives and Normal Vector
$$\mathbf{r}_u = \begin{pmatrix} -R \sin u \\ R \cos u \\ 0 \end{pmatrix}, \qquad \mathbf{r}_v = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$
Computing the cross product:
$$\mathbf{r}_u \times \mathbf{r}_v = \begin{pmatrix} R \cos u \\ R \sin u \\ 0 \end{pmatrix}, \quad \|\mathbf{r}_u \times \mathbf{r}_v\| = R$$
The unit normal vector is:
$$\mathbf{n}(u, v) = \frac{\mathbf{r}_u \times \mathbf{r}_v}{R} = \begin{pmatrix} \cos u \\ \sin u \\ 0 \end{pmatrix}$$

---

### 2. Second Fundamental Form Coefficients
Compute the second partial derivatives of $\mathbf{r}$:
$$\mathbf{r}_{uu} = \begin{pmatrix} -R \cos u \\ -R \sin u \\ 0 \end{pmatrix}, \quad \mathbf{r}_{uv} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{r}_{vv} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
Taking dot products with $\mathbf{n} = (\cos u, \sin u, 0)^T$:
$$L = \mathbf{r}_{uu} \cdot \mathbf{n} = (-R \cos u)(\cos u) + (-R \sin u)(\sin u) + 0 = -R(\cos^2 u + \sin^2 u) = -R$$
$$M = \mathbf{r}_{uv} \cdot \mathbf{n} = 0$$
$$N = \mathbf{r}_{vv} \cdot \mathbf{n} = 0$$
Thus, the Second Fundamental Form is:
$$II = -R \, du^2 \quad \blacksquare$$

---

### 3. Normal Curvature Analysis
Recall that for this cylinder:
$$E = R^2, \quad F = 0, \quad G = 1 \implies I = R^2 \, du^2 + dv^2$$
The normal curvature along direction $(du, dv)$ is:
$$\kappa_n = \frac{II}{I} = \frac{-R \, du^2}{R^2 \, du^2 + dv^2}$$
- Along the circular cross-section ($dv = 0, du \ne 0$):
  $$\kappa_n = \frac{-R \, du^2}{R^2 \, du^2} = -\frac{1}{R}$$
  This is the maximum magnitude of normal curvature (the circle bends with radius $R$).
- Along the vertical generator lines ($du = 0, dv \ne 0$):
  $$\kappa_n = \frac{0}{dv^2} = 0$$
  The generator lines are straight lines with zero normal curvature! $\blacksquare$"""
            },
            {
                "id": "dg-prob-5-2",
                "tier": "Advanced",
                "title": "Weingarten Matrix & Shape Operator of the Hyperbolic Paraboloid",
                "statement": r"""Consider the saddle surface (hyperbolic paraboloid) given by the Monge patch:
$$\mathbf{r}(u, v) = \begin{pmatrix} u \\ v \\ uv \end{pmatrix}, \quad (u, v) \in \mathbb{R}^2$$
1. Find the First Fundamental Form coefficients $E, F, G$ and the unit normal vector $\mathbf{n}(u, v)$.
2. Compute the Second Fundamental Form coefficients $L, M, N$.
3. Compute the Shape Operator matrix $A = g^{-1} b$ at the origin $(0, 0)$ and find its eigenvalues and eigenvectors.""",
                "hints": [
                    "At the origin (0, 0), u = v = 0, which greatly simplifies E, F, G and L, M, N.",
                    "Notice that r_{uu} = 0 and r_{vv} = 0, so L = 0 and N = 0.",
                    "Solve det(A - lambda I) = 0 to find principal curvatures at the origin."
                ],
                "solution": r"""### 1. Partial Derivatives and Metric at Any Point
$$\mathbf{r}_u = \begin{pmatrix} 1 \\ 0 \\ v \end{pmatrix}, \qquad \mathbf{r}_v = \begin{pmatrix} 0 \\ 1 \\ u \end{pmatrix}$$
Cross product:
$$\mathbf{r}_u \times \mathbf{r}_v = \begin{pmatrix} -v \\ -u \\ 1 \end{pmatrix}, \quad \|\mathbf{r}_u \times \mathbf{r}_v\| = \sqrt{1 + u^2 + v^2}$$
Unit normal:
$$\mathbf{n}(u, v) = \frac{1}{\sqrt{1 + u^2 + v^2}} \begin{pmatrix} -v \\ -u \\ 1 \end{pmatrix}$$
First Fundamental Form coefficients:
$$E = 1 + v^2, \quad F = uv, \quad G = 1 + u^2$$
At the origin $(u, v) = (0, 0)$:
$$E(0, 0) = 1, \quad F(0, 0) = 0, \quad G(0, 0) = 1 \implies g = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$
$$\mathbf{n}(0, 0) = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

---

### 2. Second Derivatives and Second Fundamental Form
$$\mathbf{r}_{uu} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{r}_{uv} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, \quad \mathbf{r}_{vv} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
Taking dot products with $\mathbf{n}(u, v)$:
$$L = \mathbf{r}_{uu} \cdot \mathbf{n} = 0$$
$$M = \mathbf{r}_{uv} \cdot \mathbf{n} = \frac{1}{\sqrt{1 + u^2 + v^2}}$$
$$N = \mathbf{r}_{vv} \cdot \mathbf{n} = 0$$
At the origin $(0, 0)$:
$$L(0, 0) = 0, \quad M(0, 0) = 1, \quad N(0, 0) = 0 \implies b = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \blacksquare$$

---

### 3. Shape Operator Matrix and Spectral Decomposition at the Origin
The matrix of the Shape Operator is:
$$A = g^{-1} b = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}^{-1} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
The characteristic polynomial is:
$$\det(A - \lambda I) = \det \begin{pmatrix} -\lambda & 1 \\ 1 & -\lambda \end{pmatrix} = \lambda^2 - 1 = 0 \implies \lambda = \pm 1$$
Thus, the principal curvatures at the origin are:
$$\kappa_1 = 1, \qquad \kappa_2 = -1$$
Eigenvectors:
- For $\lambda_1 = 1$: $\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} \xi_1 \\ \xi_2 \end{pmatrix} = 0 \implies \xi_1 = \xi_2 \implies \mathbf{v}_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
- For $\lambda_2 = -1$: $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} \xi_1 \\ \xi_2 \end{pmatrix} = 0 \implies \xi_1 = -\xi_2 \implies \mathbf{v}_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$
At the origin, Gaussian curvature $K = \kappa_1 \kappa_2 = -1 < 0$ (hyperbolic point), and Mean curvature $H = \frac{1}{2}(\kappa_1 + \kappa_2) = 0$ (minimal surface point)! $\blacksquare$"""
            },
            {
                "id": "dg-prob-5-3",
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Proof of the Fundamental Form Identity III - 2H II + K I = 0",
                "statement": r"""Let $S_p: T_p S \to T_p S$ be the Shape Operator on the 2D tangent space $T_p S$ of a regular surface $S$ in $\mathbb{R}^3$.
1. Let $\mathbf{e}_1, \mathbf{e}_2$ be an orthonormal basis of $T_p S$ consisting of eigenvectors of $S_p$ with corresponding eigenvalues $\kappa_1, \kappa_2$ (the principal curvatures). Express the action of $S_p$, $S_p^2$, and the fundamental forms $I, II, III$ on an arbitrary tangent vector $\mathbf{w} = c_1 \mathbf{e}_1 + c_2 \mathbf{e}_2$.
2. Prove algebraically that for every $\mathbf{w} \in T_p S$:
   $$III(\mathbf{w}) - 2H II(\mathbf{w}) + K I(\mathbf{w}) = 0$$
   where $H = \frac{1}{2}(\kappa_1 + \kappa_2)$ and $K = \kappa_1 \kappa_2$.
3. Conclude that this identity holds coordinate-free at every regular point of any smooth surface in $\mathbb{R}^3$.""",
                "hints": [
                    "Express I(w), II(w), and III(w) in terms of c_1, c_2, kappa_1, kappa_2.",
                    "Recall that II(w) = <S(w), w> and III(w) = <S^2(w), w>.",
                    "Substitute H = (kappa_1 + kappa_2)/2 and K = kappa_1 * kappa_2 and expand."
                ],
                "solution": r"""### 1. Eigenbasis Decomposition
By the Spectral Theorem for finite-dimensional self-adjoint operators (Theorem 5.1), $S_p$ possesses an orthonormal basis of eigenvectors $\{\mathbf{e}_1, \mathbf{e}_2\}$ in $T_p S$ with real eigenvalues $\kappa_1, \kappa_2$:
$$S_p(\mathbf{e}_1) = \kappa_1 \mathbf{e}_1, \qquad S_p(\mathbf{e}_2) = \kappa_2 \mathbf{e}_2$$
$$\langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij}$$
Let $\mathbf{w} = c_1 \mathbf{e}_1 + c_2 \mathbf{e}_2 \in T_p S$ be an arbitrary tangent vector.
Applying $S_p$ and $S_p^2$:
$$S_p(\mathbf{w}) = c_1 \kappa_1 \mathbf{e}_1 + c_2 \kappa_2 \mathbf{e}_2$$
$$S_p^2(\mathbf{w}) = S_p(S_p(\mathbf{w})) = c_1 \kappa_1^2 \mathbf{e}_1 + c_2 \kappa_2^2 \mathbf{e}_2$$

Now evaluate the three fundamental forms on $\mathbf{w}$:
1. First Fundamental Form:
   $$I(\mathbf{w}) = \langle \mathbf{w}, \mathbf{w} \rangle = c_1^2 + c_2^2$$
2. Second Fundamental Form:
   $$II(\mathbf{w}) = \langle S_p(\mathbf{w}), \mathbf{w} \rangle = \langle c_1 \kappa_1 \mathbf{e}_1 + c_2 \kappa_2 \mathbf{e}_2, c_1 \mathbf{e}_1 + c_2 \mathbf{e}_2 \rangle = \kappa_1 c_1^2 + \kappa_2 c_2^2$$
3. Third Fundamental Form:
   $$III(\mathbf{w}) = \langle S_p^2(\mathbf{w}), \mathbf{w} \rangle = \langle c_1 \kappa_1^2 \mathbf{e}_1 + c_2 \kappa_2^2 \mathbf{e}_2, c_1 \mathbf{e}_1 + c_2 \mathbf{e}_2 \rangle = \kappa_1^2 c_1^2 + \kappa_2^2 c_2^2$$

---

### 2. Algebraic Verification of the Identity
Recall the definitions of Mean and Gaussian curvature:
$$H = \frac{\kappa_1 + \kappa_2}{2} \implies 2H = \kappa_1 + \kappa_2$$
$$K = \kappa_1 \kappa_2$$
Now, substitute these into the linear combination $III(\mathbf{w}) - 2H II(\mathbf{w}) + K I(\mathbf{w})$:
$$III(\mathbf{w}) - 2H II(\mathbf{w}) + K I(\mathbf{w}) = (\kappa_1^2 c_1^2 + \kappa_2^2 c_2^2) - (\kappa_1 + \kappa_2)(\kappa_1 c_1^2 + \kappa_2 c_2^2) + (\kappa_1 \kappa_2)(c_1^2 + c_2^2)$$

Group terms by $c_1^2$ and $c_2^2$:
- The coefficient of $c_1^2$ is:
  $$\kappa_1^2 - (\kappa_1 + \kappa_2)\kappa_1 + \kappa_1 \kappa_2 = \kappa_1^2 - \kappa_1^2 - \kappa_1 \kappa_2 + \kappa_1 \kappa_2 = 0$$
- The coefficient of $c_2^2$ is:
  $$\kappa_2^2 - (\kappa_1 + \kappa_2)\kappa_2 + \kappa_1 \kappa_2 = \kappa_2^2 - \kappa_1 \kappa_2 - \kappa_2^2 + \kappa_1 \kappa_2 = 0$$

Therefore:
$$III(\mathbf{w}) - 2H II(\mathbf{w}) + K I(\mathbf{w}) = 0 \cdot c_1^2 + 0 \cdot c_2^2 = 0 \quad \blacksquare$$

---

### 3. Coordinate-Free Invariance
Because the orthonormal eigenbasis $\{\mathbf{e}_1, \mathbf{e}_2\}$ exists at every regular point by the Spectral Theorem, and the tangent vector $\mathbf{w}$ was chosen completely arbitrarily:
$$III - 2H II + K I \equiv 0$$
holds identically on the entire tangent bundle of any smooth surface in $\mathbb{R}^3$.
This identity confirms that the Third Fundamental Form contains no new geometric information beyond what is already determined by $I, II, H,$ and $K$. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u = get_unit5()
    print(f"Loaded Unit 5: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
