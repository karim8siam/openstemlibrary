# -*- coding: utf-8 -*-
"""
build_dg_unit4.py
Constructs Unit 4: Parametric Surfaces & The First Fundamental Form
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Parametric Surfaces & The First Fundamental Form",
        "leadSummary": "Foundations of two-dimensional surface theory in Euclidean 3-space: smooth coordinate patches, regularity conditions, tangent planes and surface normals, the First Fundamental Form (surface metric) $I = E du^2 + 2F dudv + G dv^2$, positive definiteness, arc-length of surface curves, angles between tangent vectors, orthogonal coordinates, and the intrinsic surface area element.",
        "simulations": ["sim_dg_first_fundamental_form"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Parametric Surfaces, Coordinate Patches & Regular Points",
                "content": r"""### 1. Vector Parametrization of Surfaces in $\mathbb{R}^3$

Just as a curve is described by a single scalar parameter, a surface in $\mathbb{R}^3$ is locally parametrized by two independent real parameters $(u, v)$.

> **Definition 4.1 (Parametrized Surface Patch):**
> Let $U \subseteq \mathbb{R}^2$ be an open connected domain in the $uv$-plane.
> A **parametrized surface** (or local coordinate patch) is a smooth vector-valued function:
> $$\mathbf{r}: U \to \mathbb{R}^3, \quad (u, v) \mapsto \mathbf{r}(u, v) = \begin{pmatrix} x(u, v) \\ y(u, v) \\ z(u, v) \end{pmatrix}$$
> The set of points $S = \mathbf{r}(U) \subset \mathbb{R}^3$ is the **trace** or image of the surface patch.

---

### 2. Partial Derivatives and Coordinate Curves

For a fixed $v = v_0$, the mapping $u \mapsto \mathbf{r}(u, v_0)$ traces a curve on $S$ called the **$u$-coordinate curve** (or $u$-parameter curve).
Similarly, for a fixed $u = u_0$, $v \mapsto \mathbf{r}(u_0, v)$ traces a **$v$-coordinate curve**.

The partial derivative vectors are tangent to these coordinate curves:
$$\mathbf{r}_u = \frac{\partial \mathbf{r}}{\partial u} = \begin{pmatrix} \frac{\partial x}{\partial u} \\ \frac{\partial y}{\partial u} \\ \frac{\partial z}{\partial u} \end{pmatrix}, \qquad \mathbf{r}_v = \frac{\partial \mathbf{r}}{\partial v} = \begin{pmatrix} \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial v} \\ \frac{\partial z}{\partial v} \end{pmatrix}$$

---

### 3. Regularity and the Tangent Plane

> **Definition 4.2 (Regular Point of a Surface):**
> A point $p = \mathbf{r}(u_0, v_0)$ is called a **regular point** of the surface patch if the partial derivative vectors $\mathbf{r}_u$ and $\mathbf{r}_v$ are linearly independent at $(u_0, v_0)$:
> $$\mathbf{r}_u \times \mathbf{r}_v \ne \mathbf{0}$$
> Equivalently, the Jacobian matrix $J = \begin{pmatrix} x_u & x_v \\ y_u & y_v \\ z_u & z_v \end{pmatrix}$ has maximal rank $2$.
> A surface patch is **regular** if every point in $U$ is regular.

> **Definition 4.3 (Tangent Plane $T_p S$ and Unit Normal $\mathbf{n}$):**
> At any regular point $p \in S$, the vectors $\mathbf{r}_u$ and $\mathbf{r}_v$ span a two-dimensional vector subspace of $\mathbb{R}^3$ called the **tangent plane** to $S$ at $p$, denoted $T_p S$:
> $$T_p S = \operatorname{span}\{\mathbf{r}_u, \mathbf{r}_v\} = \{\lambda \mathbf{r}_u + \mu \mathbf{r}_v : \lambda, \mu \in \mathbb{R}\}$$
> The **unit normal vector** $\mathbf{n}(u, v)$ to the surface at $p$ is defined by:
> $$\mathbf{n}(u, v) = \frac{\mathbf{r}_u \times \mathbf{r}_v}{\|\mathbf{r}_u \times \mathbf{r}_v\|}$$
> By construction, $\mathbf{n} \cdot \mathbf{r}_u = 0$, $\mathbf{n} \cdot \mathbf{r}_v = 0$, and $\|\mathbf{n}\| = 1$.

The Cartesian equation of the tangent plane passing through $\mathbf{r}(u_0, v_0)$ is:
$$\mathbf{n}(u_0, v_0) \cdot (\mathbf{R} - \mathbf{r}(u_0, v_0)) = 0 \iff (\mathbf{R} - \mathbf{r}) \cdot (\mathbf{r}_u \times \mathbf{r}_v) = 0$$
where $\mathbf{R} = (X, Y, Z)^T$ is an arbitrary point on the plane."""
            },
            {
                "secNumber": "4.2",
                "title": "The First Fundamental Form: Metric Coefficients E, F, G & Positive Definiteness",
                "content": r"""### 1. Differential of the Position Vector

Let $\mathbf{r}: U \to \mathbb{R}^3$ be a regular surface.
Consider an infinitesimal displacement on the parameter domain $d\mathbf{u} = (du, dv)^T$.
The corresponding infinitesimal displacement vector on the surface in $\mathbb{R}^3$ is given by the differential:
$$d\mathbf{r} = \mathbf{r}_u \, du + \mathbf{r}_v \, dv \in T_p S$$

The square of the infinitesimal Euclidean distance between $\mathbf{r}(u, v)$ and $\mathbf{r}(u + du, v + dv)$ is:
$$ds^2 = \|d\mathbf{r}\|^2 = d\mathbf{r} \cdot d\mathbf{r} = (\mathbf{r}_u \, du + \mathbf{r}_v \, dv) \cdot (\mathbf{r}_u \, du + \mathbf{r}_v \, dv)$$
Expanding the dot product bilinearly:
$$ds^2 = (\mathbf{r}_u \cdot \mathbf{r}_u) \, du^2 + 2(\mathbf{r}_u \cdot \mathbf{r}_v) \, du \, dv + (\mathbf{r}_v \cdot \mathbf{r}_v) \, dv^2$$

---

### 2. Definition of the First Fundamental Form

> **Definition 4.4 (First Fundamental Form):**
> The **First Fundamental Form** of a surface $S$, denoted by $I$ or $I_p$, is the quadratic form on the tangent space $T_p S$ induced by the Euclidean metric of $\mathbb{R}^3$:
> $$I(du, dv) = E \, du^2 + 2F \, du \, dv + G \, dv^2$$
> where the **metric coefficients** (Gauss coefficients) are:
> $$E = \mathbf{r}_u \cdot \mathbf{r}_u = \|\mathbf{r}_u\|^2$$
> $$F = \mathbf{r}_u \cdot \mathbf{r}_v$$
> $$G = \mathbf{r}_v \cdot \mathbf{r}_v = \|\mathbf{r}_v\|^2$$

In matrix notation, for a tangent vector $\mathbf{w} = \lambda \mathbf{r}_u + \mu \mathbf{r}_v \in T_p S$, represented in coordinates by $\mathbf{\xi} = \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$:
$$I(\mathbf{w}) = \mathbf{\xi}^T g \, \mathbf{\xi} = \begin{pmatrix} \lambda & \mu \end{pmatrix} \begin{pmatrix} E & F \\ F & G \end{pmatrix} \begin{pmatrix} \lambda \\ \mu \end{pmatrix}$$
where $g = \begin{pmatrix} E & F \\ F & G \end{pmatrix}$ is the **metric tensor matrix**.

---

### 3. Positive Definiteness and the Metric Determinant

> **Theorem 4.1 (Positive Definiteness of the First Fundamental Form):**
> At every regular point of a surface, the First Fundamental Form is strictly positive definite:
> $$I(du, dv) > 0 \quad \text{for all } (du, dv) \ne (0, 0)$$
> Moreover, the determinant of the metric tensor satisfies:
> $$g = \det \begin{pmatrix} E & F \\ F & G \end{pmatrix} = EG - F^2 = \|\mathbf{r}_u \times \mathbf{r}_v\|^2 > 0$$

> **Proof:**
> By Lagrange's vector identity for any two vectors $\mathbf{a}, \mathbf{b} \in \mathbb{R}^3$:
> $$\|\mathbf{a} \times \mathbf{b}\|^2 = \|\mathbf{a}\|^2 \|\mathbf{b}\|^2 - (\mathbf{a} \cdot \mathbf{b})^2$$
> Setting $\mathbf{a} = \mathbf{r}_u$ and $\mathbf{b} = \mathbf{r}_v$:
> $$\|\mathbf{r}_u \times \mathbf{r}_v\|^2 = (\mathbf{r}_u \cdot \mathbf{r}_u)(\mathbf{r}_v \cdot \mathbf{r}_v) - (\mathbf{r}_u \cdot \mathbf{r}_v)^2 = EG - F^2$$
> Because the point is regular, $\mathbf{r}_u \times \mathbf{r}_v \ne \mathbf{0}$, which implies:
> $$EG - F^2 = \|\mathbf{r}_u \times \mathbf{r}_v\|^2 > 0$$
> Next, consider $I(du, dv) = E du^2 + 2F dudv + G dv^2$.
> Since $\mathbf{r}_u \ne \mathbf{0}$, $E = \|\mathbf{r}_u\|^2 > 0$. We complete the square:
> $$I(du, dv) = E \left[ du^2 + \frac{2F}{E} du dv + \frac{F^2}{E^2} dv^2 \right] + \left( G - \frac{F^2}{E} \right) dv^2$$
> $$I(du, dv) = E \left( du + \frac{F}{E} dv \right)^2 + \frac{EG - F^2}{E} dv^2$$
> Both coefficients $E > 0$ and $\frac{EG - F^2}{E} > 0$ are strictly positive.
> Thus $I(du, dv) \ge 0$, with equality holding if and only if $dv = 0$ and $du + \frac{F}{E} dv = 0 \implies du = 0$.
> Hence, $I$ is strictly positive definite. $\blacksquare$"""
            },
            {
                "secNumber": "4.3",
                "title": "Arc-Length of Surface Curves, Isometries & Conformal Mappings",
                "content": r"""### 1. Arc-Length of Curves Lying on a Surface

Let $C$ be a smooth curve lying entirely on the surface $S$, defined parametrically by $u = u(t), v = v(t)$ for $t \in [a, b]$.
The position vector of the curve in $\mathbb{R}^3$ is:
$$\mathbf{c}(t) = \mathbf{r}(u(t), v(t))$$
Applying the chain rule, the velocity vector is:
$$\mathbf{c}'(t) = \mathbf{r}_u \, u'(t) + \mathbf{r}_v \, v'(t)$$
The speed of the curve is the norm of the velocity vector:
$$\|\mathbf{c}'(t)\| = \sqrt{\mathbf{c}'(t) \cdot \mathbf{c}'(t)} = \sqrt{E (u')^2 + 2F u' v' + G (v')^2} = \sqrt{I(u', v')}$$

> **Theorem 4.2 (Arc-Length Formula on Surfaces):**
> The arc-length $L$ of the curve $C$ from $t = a$ to $t = b$ is given intrinsically by:
> $$L = \int_a^b \|\mathbf{c}'(t)\| \, dt = \int_a^b \sqrt{E \left(\frac{du}{dt}\right)^2 + 2F \left(\frac{du}{dt}\right)\left(\frac{dv}{dt}\right) + G \left(\frac{dv}{dt}\right)^2} \, dt$$

This fundamental result demonstrates that distance along curves on a surface can be computed solely from the metric coefficients $E(u, v), F(u, v), G(u, v)$ without knowing how the surface is embedded in 3D space!

---

### 2. Isometries and Intrinsic Geometry

> **Definition 4.5 (Local Isometry):**
> A diffeomorphism $\phi: S_1 \to S_2$ between two surfaces is called a **local isometry** if it preserves the lengths of all curves.
> Equivalently, for any point $p \in S_1$ and tangent vectors $\mathbf{w}_1, \mathbf{w}_2 \in T_p S_1$:
> $$I_p(\mathbf{w}_1, \mathbf{w}_2) = I_{\phi(p)}(d\phi(\mathbf{w}_1), d\phi(\mathbf{w}_2))$$
> If $S_1$ and $S_2$ are parametrized by coordinates $(u, v)$ such that their metric coefficients satisfy:
> $$E_1(u, v) = E_2(u, v), \quad F_1(u, v) = F_2(u, v), \quad G_1(u, v) = G_2(u, v)$$
> then the mapping is an isometry.

Surfaces related by an isometry share all **intrinsic** geometric properties (such as arc-length, angles, and Gaussian curvature), even though their spatial embeddings may look completely different (e.g., a plane sheet rolling into a cylinder).

---

### 3. Conformal Mappings and Orthogonal Coordinates

> **Definition 4.6 (Conformal Mapping):**
> A diffeomorphism $\phi: S_1 \to S_2$ is **conformal** (angle-preserving) if there exists a smooth positive function $\lambda(u, v) > 0$ (the conformal factor) such that:
> $$I_2 = \lambda^2(u, v) I_1$$

> **Definition 4.7 (Orthogonal Coordinate Systems):**
> A coordinate patch $(u, v)$ is called **orthogonal** if the coordinate curves intersect at right angles everywhere on $U$:
> $$\mathbf{r}_u \cdot \mathbf{r}_v = 0 \iff F(u, v) \equiv 0$$
> When $F \equiv 0$, the First Fundamental Form simplifies to:
> $$I = E(u, v) \, du^2 + G(u, v) \, dv^2$$
> In addition, if $E = G = \lambda^2(u, v)$ and $F = 0$, the coordinates are called **isothermal** (or conformal):
> $$I = \lambda^2(u, v)(du^2 + dv^2)$$"""
            },
            {
                "secNumber": "4.4",
                "title": "Angles Between Curves on Surfaces & Direction Fields",
                "content": r"""### 1. Angle Between Tangent Vectors on a Surface

Let $p \in S$ be a regular point, and let $\mathbf{w}_1, \mathbf{w}_2 \in T_p S$ be two non-zero tangent vectors.
In local coordinates:
$$\mathbf{w}_1 = \mathbf{r}_u \, du + \mathbf{r}_v \, dv = d\mathbf{r}$$
$$\mathbf{w}_2 = \mathbf{r}_u \, \delta u + \mathbf{r}_v \, \delta v = \delta\mathbf{r}$$

The inner product of these tangent vectors is:
$$\mathbf{w}_1 \cdot \mathbf{w}_2 = (\mathbf{r}_u \, du + \mathbf{r}_v \, dv) \cdot (\mathbf{r}_u \, \delta u + \mathbf{r}_v \, \delta v)$$
Expanding:
$$\mathbf{w}_1 \cdot \mathbf{w}_2 = E \, du \, \delta u + F(du \, \delta v + dv \, \delta u) + G \, dv \, \delta v$$

> **Theorem 4.3 (Angle Between Directions on a Surface):**
> The angle $\theta \in [0, \pi]$ between the directions $d\mathbf{r} = (du, dv)$ and $\delta\mathbf{r} = (\delta u, \delta v)$ is given by:
> $$\cos \theta = \frac{\mathbf{w}_1 \cdot \mathbf{w}_2}{\|\mathbf{w}_1\| \|\mathbf{w}_2\|} = \frac{E \, du \, \delta u + F(du \, \delta v + dv \, \delta u) + G \, dv \, \delta v}{\sqrt{E \, du^2 + 2F \, du \, dv + G \, dv^2} \sqrt{E \, \delta u^2 + 2F \, \delta u \, \delta v + G \, \delta v^2}}$$
> In particular, the two directions are **orthogonal** ($\theta = \pi/2$) if and only if:
> $$E \, du \, \delta u + F(du \, \delta v + dv \, \delta u) + G \, dv \, \delta v = 0$$

---

### 2. Angle of a Curve with Coordinate Curves

For the $u$-coordinate curve ($dv = 0, du > 0$), the tangent vector is $\mathbf{r}_u$.
The angle $\alpha$ between an arbitrary curve direction $(du, dv)$ and the $u$-coordinate curve satisfies:
$$\cos \alpha = \frac{\mathbf{r}_u \cdot (\mathbf{r}_u du + \mathbf{r}_v dv)}{\|\mathbf{r}_u\| \|d\mathbf{r}\|} = \frac{E du + F dv}{\sqrt{E} \sqrt{E du^2 + 2F dudv + G dv^2}}$$
For an orthogonal coordinate system ($F = 0$):
$$\cos \alpha = \frac{\sqrt{E} du}{\sqrt{E du^2 + G dv^2}} = \frac{\sqrt{E} du}{ds}, \qquad \sin \alpha = \frac{\sqrt{G} dv}{ds}$$

---

### 3. Orthogonal Trajectories of a Family of Curves

Suppose a family of curves on $S$ is defined by a differential equation:
$$P(u, v) \, du + Q(u, v) \, dv = 0 \implies \frac{dv}{du} = -\frac{P}{Q}$$
To find the family of **orthogonal trajectories** $(\delta u, \delta v)$, we apply the orthogonality condition:
$$E \, du \, \delta u + F(du \, \delta v + dv \, \delta u) + G \, dv \, \delta v = 0$$
Dividing by $du \, \delta u$:
$$E + F \left( \frac{\delta v}{\delta u} + \frac{dv}{du} \right) + G \left( \frac{dv}{du} \right)\left( \frac{\delta v}{\delta u} \right) = 0$$
Substituting $\frac{dv}{du} = -\frac{P}{Q}$:
$$E + F \left( \frac{\delta v}{\delta u} - \frac{P}{Q} \right) - G \frac{P}{Q} \frac{\delta v}{\delta u} = 0$$
Multiplying by $Q$:
$$(E Q - F P) \delta u + (F Q - G P) \delta v = 0$$
This first-order ODE governs the orthogonal trajectories across the surface patch."""
            },
            {
                "secNumber": "4.5",
                "title": "Surface Area Element, Jacobians & Integrals on Surfaces",
                "content": r"""### 1. Infinitesimal Area Element on a Surface

Consider an infinitesimal curvilinear parallelogram on the surface bounded by the vectors $\mathbf{r}_u \, du$ and $\mathbf{r}_v \, dv$.
The area $dA$ of this infinitesimal parallelogram in $\mathbb{R}^3$ is the magnitude of their cross product:
$$dA = \|\mathbf{r}_u \, du \times \mathbf{r}_v \, dv\| = \|\mathbf{r}_u \times \mathbf{r}_v\| \, du \, dv$$

Using Lagrange's identity from Section 4.2:
$$\|\mathbf{r}_u \times \mathbf{r}_v\| = \sqrt{EG - F^2}$$

> **Definition 4.8 (Surface Area Element):**
> The **intrinsic area element** (or Riemannian volume element $d\sigma$) on a regular surface patch is:
> $$dA = \sqrt{EG - F^2} \, du \, dv$$
> The positive quantity $W = \sqrt{EG - F^2} > 0$ is the **Gram determinant factor**.

---

### 2. Surface Integral and Total Area

> **Definition 4.9 (Surface Area):**
> Let $S = \mathbf{r}(U)$ be a regular surface patch where $U \subset \mathbb{R}^2$ is bounded.
> The **surface area** of $S$ is defined by the double integral:
> $$\operatorname{Area}(S) = \iint_U dA = \iint_U \sqrt{EG - F^2} \, du \, dv$$
> For a scalar function $f: S \to \mathbb{R}$, the surface integral of $f$ over $S$ is:
> $$\iint_S f \, dA = \iint_U f(\mathbf{r}(u, v)) \sqrt{EG - F^2} \, du \, dv$$

---

### 3. Invariance Under Reparametrization

> **Theorem 4.4 (Invariance of Surface Area):**
> The surface area $\operatorname{Area}(S)$ is invariant under orientation-preserving or orientation-reversing smooth reparametrizations.

> **Proof:**
> Let $(\bar{u}, \bar{v})$ be an alternative coordinate system related to $(u, v)$ by a diffeomorphism $\Phi: \bar{U} \to U$, $(u, v) = \Phi(\bar{u}, \bar{v})$.
> By the multi-variable chain rule:
> $$\mathbf{r}_{\bar{u}} = \mathbf{r}_u \frac{\partial u}{\partial \bar{u}} + \mathbf{r}_v \frac{\partial v}{\partial \bar{u}}, \qquad \mathbf{r}_{\bar{v}} = \mathbf{r}_u \frac{\partial u}{\partial \bar{v}} + \mathbf{r}_v \frac{\partial v}{\partial \bar{v}}$$
> Taking the cross product:
> $$\mathbf{r}_{\bar{u}} \times \mathbf{r}_{\bar{v}} = \left( \mathbf{r}_u \frac{\partial u}{\partial \bar{u}} + \mathbf{r}_v \frac{\partial v}{\partial \bar{u}} \right) \times \left( \mathbf{r}_u \frac{\partial u}{\partial \bar{v}} + \mathbf{r}_v \frac{\partial v}{\partial \bar{v}} \right)$$
> Since $\mathbf{r}_u \times \mathbf{r}_u = \mathbf{0}$ and $\mathbf{r}_v \times \mathbf{r}_v = \mathbf{0}$, this simplifies to:
> $$\mathbf{r}_{\bar{u}} \times \mathbf{r}_{\bar{v}} = \left( \frac{\partial u}{\partial \bar{u}}\frac{\partial v}{\partial \bar{v}} - \frac{\partial v}{\partial \bar{u}}\frac{\partial u}{\partial \bar{v}} \right) (\mathbf{r}_u \times \mathbf{r}_v) = \det(J_\Phi) (\mathbf{r}_u \times \mathbf{r}_v)$$
> Taking norms on both sides:
> $$\sqrt{\bar{E}\bar{G} - \bar{F}^2} = \|\mathbf{r}_{\bar{u}} \times \mathbf{r}_{\bar{v}}\| = |\det(J_\Phi)| \|\mathbf{r}_u \times \mathbf{r}_v\| = |\det(J_\Phi)| \sqrt{EG - F^2}$$
> By the multivariable change-of-variables theorem for double integrals:
> $$\iint_{\bar{U}} \sqrt{\bar{E}\bar{G} - \bar{F}^2} \, d\bar{u} \, d\bar{v} = \iint_{\bar{U}} \sqrt{EG - F^2} |\det(J_\Phi)| \, d\bar{u} \, d\bar{v} = \iint_U \sqrt{EG - F^2} \, du \, dv$$
> Thus the surface area is completely independent of the choice of coordinate patch! $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "id": "dg-prob-4-1",
                "tier": "Foundational",
                "title": "First Fundamental Form and Total Surface Area of the 2-Sphere",
                "statement": r"""Consider the 2-sphere of radius $R > 0$ parametrized by spherical angles $(\theta, \phi)$:
$$\mathbf{r}(\theta, \phi) = \begin{pmatrix} R \sin\theta \cos\phi \\ R \sin\theta \sin\phi \\ R \cos\theta \end{pmatrix}, \quad \theta \in (0, \pi), \; \phi \in (0, 2\pi)$$
1. Compute the partial derivatives $\mathbf{r}_\theta$ and $\mathbf{r}_\phi$.
2. Calculate the metric coefficients $E, F, G$ and write down the First Fundamental Form $I$.
3. Compute the area element $dA = \sqrt{EG - F^2} \, d\theta \, d\phi$ and evaluate the total surface area of the sphere.""",
                "hints": [
                    "Differentiate with respect to theta and phi. Check orthogonality r_theta . r_phi.",
                    "Use sin^2(theta) + cos^2(theta) = 1 to simplify E and G.",
                    "Integrate dphi from 0 to 2*pi and dtheta from 0 to pi."
                ],
                "solution": r"""### 1. Partial Derivatives
Differentiating $\mathbf{r}(\theta, \phi)$ with respect to $\theta$:
$$\mathbf{r}_\theta = \begin{pmatrix} R \cos\theta \cos\phi \\ R \cos\theta \sin\phi \\ -R \sin\theta \end{pmatrix}$$
Differentiating with respect to $\phi$:
$$\mathbf{r}_\phi = \begin{pmatrix} -R \sin\theta \sin\phi \\ R \sin\theta \cos\phi \\ 0 \end{pmatrix}$$

---

### 2. Metric Coefficients and First Fundamental Form
Computing $E = \mathbf{r}_\theta \cdot \mathbf{r}_\theta$:
$$E = R^2 \cos^2\theta \cos^2\phi + R^2 \cos^2\theta \sin^2\phi + R^2 \sin^2\theta = R^2 \cos^2\theta (\cos^2\phi + \sin^2\phi) + R^2 \sin^2\theta = R^2 (\cos^2\theta + \sin^2\theta) = R^2$$

Computing $F = \mathbf{r}_\theta \cdot \mathbf{r}_\phi$:
$$F = (R \cos\theta \cos\phi)(-R \sin\theta \sin\phi) + (R \cos\theta \sin\phi)(R \sin\theta \cos\phi) + (-R \sin\theta)(0)$$
$$F = -R^2 \sin\theta \cos\theta \sin\phi \cos\phi + R^2 \sin\theta \cos\theta \sin\phi \cos\phi = 0$$
Since $F = 0$, the spherical coordinate lines are orthogonal everywhere!

Computing $G = \mathbf{r}_\phi \cdot \mathbf{r}_\phi$:
$$G = (-R \sin\theta \sin\phi)^2 + (R \sin\theta \cos\phi)^2 + 0^2 = R^2 \sin^2\theta (\sin^2\phi + \cos^2\phi) = R^2 \sin^2\theta$$

Thus, the First Fundamental Form of the sphere is:
$$I = R^2 \, d\theta^2 + R^2 \sin^2\theta \, d\phi^2 \quad \blacksquare$$

---

### 3. Surface Area Element and Total Area
The metric determinant is:
$$EG - F^2 = (R^2)(R^2 \sin^2\theta) - 0 = R^4 \sin^2\theta$$
Since $\theta \in (0, \pi)$, $\sin\theta > 0$, so:
$$\sqrt{EG - F^2} = R^2 \sin\theta$$
The area element is:
$$dA = R^2 \sin\theta \, d\theta \, d\phi$$
Evaluating the total surface area:
$$\operatorname{Area}(S^2) = \int_0^{2\pi} d\phi \int_0^\pi R^2 \sin\theta \, d\theta = 2\pi R^2 [-\cos\theta]_0^\pi = 2\pi R^2 (-(-1) - (-1)) = 2\pi R^2 (2) = 4\pi R^2 \quad \blacksquare$$"""
            },
            {
                "id": "dg-prob-4-2",
                "tier": "Advanced",
                "title": "Local Isometry Between the Catenoid and Helicoid",
                "statement": r"""The **Catenoid** $S_{\text{cat}}$ and the **Helicoid** $S_{\text{hel}}$ are parametrized by:
$$\mathbf{r}_{\text{cat}}(u, v) = \begin{pmatrix} \cosh u \cos v \\ \cosh u \sin v \\ u \end{pmatrix}, \quad (u, v) \in \mathbb{R} \times (0, 2\pi)$$
$$\mathbf{r}_{\text{hel}}(\bar{u}, \bar{v}) = \begin{pmatrix} \bar{u} \cos \bar{v} \\ \bar{u} \sin \bar{v} \\ \bar{v} \end{pmatrix}, \quad (\bar{u}, \bar{v}) \in \mathbb{R} \times (0, 2\pi)$$
1. Compute the metric coefficients $E, F, G$ of the Catenoid.
2. Compute the metric coefficients $\bar{E}, \bar{F}, \bar{G}$ of the Helicoid.
3. Show that under the coordinate transformation $\bar{u} = \sinh u$ and $\bar{v} = v$, the two First Fundamental Forms coincide, proving that the Catenoid and Helicoid are locally isometric.""",
                "hints": [
                    "Recall the hyperbolic identity cosh^2(u) - sinh^2(u) = 1, and d/du cosh(u) = sinh(u).",
                    "For the catenoid, E = sinh^2(u) + 1 = cosh^2(u).",
                    "Use d(u_bar) = cosh(u) du to transform the helicoid metric."
                ],
                "solution": r"""### 1. Metric Coefficients of the Catenoid
For $\mathbf{r}_{\text{cat}}(u, v) = (\cosh u \cos v, \cosh u \sin v, u)^T$:
$$\mathbf{r}_u = \begin{pmatrix} \sinh u \cos v \\ \sinh u \sin v \\ 1 \end{pmatrix}, \qquad \mathbf{r}_v = \begin{pmatrix} -\cosh u \sin v \\ \cosh u \cos v \\ 0 \end{pmatrix}$$
Now compute the dot products:
$$E = \mathbf{r}_u \cdot \mathbf{r}_u = \sinh^2 u (\cos^2 v + \sin^2 v) + 1 = \sinh^2 u + 1 = \cosh^2 u$$
$$F = \mathbf{r}_u \cdot \mathbf{r}_v = -\sinh u \cosh u \sin v \cos v + \sinh u \cosh u \sin v \cos v + 0 = 0$$
$$G = \mathbf{r}_v \cdot \mathbf{r}_v = \cosh^2 u (\sin^2 v + \cos^2 v) + 0 = \cosh^2 u$$
Thus, the First Fundamental Form of the catenoid is:
$$I_{\text{cat}} = \cosh^2 u \, du^2 + \cosh^2 u \, dv^2 = \cosh^2 u (du^2 + dv^2) \quad \blacksquare$$

---

### 2. Metric Coefficients of the Helicoid
For $\mathbf{r}_{\text{hel}}(\bar{u}, \bar{v}) = (\bar{u} \cos \bar{v}, \bar{u} \sin \bar{v}, \bar{v})^T$:
$$\mathbf{r}_{\bar{u}} = \begin{pmatrix} \cos \bar{v} \\ \sin \bar{v} \\ 0 \end{pmatrix}, \qquad \mathbf{r}_{\bar{v}} = \begin{pmatrix} -\bar{u} \sin \bar{v} \\ \bar{u} \cos \bar{v} \\ 1 \end{pmatrix}$$
Now compute the metric coefficients:
$$\bar{E} = \mathbf{r}_{\bar{u}} \cdot \mathbf{r}_{\bar{u}} = \cos^2 \bar{v} + \sin^2 \bar{v} + 0 = 1$$
$$\bar{F} = \mathbf{r}_{\bar{u}} \cdot \mathbf{r}_{\bar{v}} = -\bar{u} \sin \bar{v} \cos \bar{v} + \bar{u} \sin \bar{v} \cos \bar{v} + 0 = 0$$
$$\bar{G} = \mathbf{r}_{\bar{v}} \cdot \mathbf{r}_{\bar{v}} = \bar{u}^2 (\sin^2 \bar{v} + \cos^2 \bar{v}) + 1 = \bar{u}^2 + 1$$
Thus, the First Fundamental Form of the helicoid is:
$$I_{\text{hel}} = d\bar{u}^2 + (\bar{u}^2 + 1) \, d\bar{v}^2 \quad \blacksquare$$

---

### 3. Coordinate Transformation and Local Isometry
Let $\bar{u} = \sinh u$ and $\bar{v} = v$.
Then:
$$d\bar{u} = \cosh u \, du, \qquad d\bar{v} = dv$$
Substitute these into $I_{\text{hel}}$:
$$d\bar{u}^2 = (\cosh u \, du)^2 = \cosh^2 u \, du^2$$
$$\bar{u}^2 + 1 = \sinh^2 u + 1 = \cosh^2 u$$
$$(\bar{u}^2 + 1) \, d\bar{v}^2 = \cosh^2 u \, dv^2$$
Therefore:
$$I_{\text{hel}} = \cosh^2 u \, du^2 + \cosh^2 u \, dv^2 = I_{\text{cat}}$$
Since the First Fundamental Forms match identically under this smooth bijection, the Catenoid and Helicoid are **locally isometric**! $\blacksquare$"""
            },
            {
                "id": "dg-prob-4-3",
                "tier": "Honors / Proof Challenge",
                "title": "Angle Preservation of Isothermal Coordinates & Conformal Invariance",
                "statement": r"""A regular coordinate system $(u, v)$ on a surface $S$ is called **isothermal** (or conformal) if the First Fundamental Form takes the form:
$$I = \lambda^2(u, v)(du^2 + dv^2)$$
where $\lambda(u, v) > 0$ is a smooth non-vanishing function.
1. Let $\mathbf{w}_1 = \mathbf{r}_u \, du_1 + \mathbf{r}_v \, dv_1$ and $\mathbf{w}_2 = \mathbf{r}_u \, du_2 + \mathbf{rv} \, dv_2$ be two tangent vectors at $p = \mathbf{r}(u, v)$. Prove that the geometric angle $\theta \in [0, \pi]$ between $\mathbf{w}_1$ and $\mathbf{w}_2$ in $\mathbb{R}^3$ equals the Euclidean angle $\alpha$ between the parameter displacement vectors $\mathbf{v}_1 = (du_1, dv_1)^T$ and $\mathbf{v}_2 = (du_2, dv_2)^T$ in the parameter plane $\mathbb{R}^2$.
2. Conclude that the parameter mapping $\mathbf{r}: U \subset \mathbb{R}^2 \to S \subset \mathbb{R}^3$ is a conformal map, preserving all angles and shapes of infinitesimal figures.""",
                "hints": [
                    "For isothermal coordinates, E = lambda^2, F = 0, G = lambda^2.",
                    "Compute the inner product w_1 . w_2 using the First Fundamental Form.",
                    "Compare cos(theta) = (w_1 . w_2) / (||w_1|| ||w_2||) with the 2D dot product (v_1 . v_2) / (||v_1|| ||v_2||)."
                ],
                "solution": r"""### 1. Inner Product and Norms Under Isothermal Coordinates
Assume the metric coefficients satisfy:
$$E = \lambda^2(u, v), \quad F = 0, \quad G = \lambda^2(u, v)$$
with $\lambda(u, v) > 0$.
The inner product of the tangent vectors $\mathbf{w}_1, \mathbf{w}_2 \in T_p S$ is given by the bilinear form:
$$\mathbf{w}_1 \cdot \mathbf{w}_2 = E \, du_1 \, du_2 + F(du_1 \, dv_2 + dv_1 \, du_2) + G \, dv_1 \, dv_2$$
Substituting $E = G = \lambda^2$ and $F = 0$:
$$\mathbf{w}_1 \cdot \mathbf{w}_2 = \lambda^2 \, du_1 \, du_2 + 0 + \lambda^2 \, dv_1 \, dv_2 = \lambda^2 (du_1 \, du_2 + dv_1 \, dv_2)$$
Notice that:
$$du_1 \, du_2 + dv_1 \, dv_2 = \mathbf{v}_1 \cdot \mathbf{v}_2$$
where $\mathbf{v}_1 = (du_1, dv_1)^T$ and $\mathbf{v}_2 = (du_2, dv_2)^T$ are vectors in the flat parameter plane $\mathbb{R}^2$.
Thus:
$$\mathbf{w}_1 \cdot \mathbf{w}_2 = \lambda^2 (\mathbf{v}_1 \cdot \mathbf{v}_2)$$

Next, compute the norms of $\mathbf{w}_1$ and $\mathbf{w}_2$:
$$\|\mathbf{w}_1\|^2 = I(du_1, dv_1) = \lambda^2 (du_1^2 + dv_1^2) = \lambda^2 \|\mathbf{v}_1\|^2 \implies \|\mathbf{w}_1\| = \lambda \|\mathbf{v}_1\|$$
$$\|\mathbf{w}_2\|^2 = I(du_2, dv_2) = \lambda^2 (du_2^2 + dv_2^2) = \lambda^2 \|\mathbf{v}_2\|^2 \implies \|\mathbf{w}_2\| = \lambda \|\mathbf{v}_2\|$$

---

### 2. Angle Equivalence
The cosine of the 3D angle $\theta$ between $\mathbf{w}_1$ and $\mathbf{w}_2$ on the surface is:
$$\cos \theta = \frac{\mathbf{w}_1 \cdot \mathbf{w}_2}{\|\mathbf{w}_1\| \|\mathbf{w}_2\|}$$
Substituting the expressions derived above:
$$\cos \theta = \frac{\lambda^2 (\mathbf{v}_1 \cdot \mathbf{v}_2)}{(\lambda \|\mathbf{v}_1\|) (\lambda \|\mathbf{v}_2\|)} = \frac{\lambda^2 (\mathbf{v}_1 \cdot \mathbf{v}_2)}{\lambda^2 \|\mathbf{v}_1\| \|\mathbf{v}_2\|} = \frac{\mathbf{v}_1 \cdot \mathbf{v}_2}{\|\mathbf{v}_1\| \|\mathbf{v}_2\|}$$
The right-hand side is precisely the definition of $\cos \alpha$, where $\alpha$ is the standard Euclidean angle between $\mathbf{v}_1$ and $\mathbf{v}_2$ in $\mathbb{R}^2$:
$$\cos \theta = \cos \alpha$$
Since both $\theta, \alpha \in [0, \pi]$, we have:
$$\theta = \alpha \quad \blacksquare$$

---

### 3. Conclusion: Conformal Mapping
Because $\theta = \alpha$ for any two arbitrary non-zero tangent directions at every point $p \in S$:
1. Every angle between curves on the surface is identical to the angle between their preimage curves in the $uv$-plane.
2. The coordinate mapping $\mathbf{r}: U \to S$ is a **conformal map** (angle-preserving).
3. Infinitesimal circles in the parameter plane are mapped to infinitesimal circles on the surface, scaled uniformly in all directions by the factor $\lambda(u, v)$ without angular shearing. $\blacksquare$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u = get_unit4()
    print(f"Loaded Unit 4: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
