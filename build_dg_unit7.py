# -*- coding: utf-8 -*-
"""
build_dg_unit7.py
Constructs Unit 7: Lines of Curvature, Asymptotic Curves & The Dupin Indicatrix
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Lines of Curvature, Asymptotic Curves & The Dupin Indicatrix",
        "leadSummary": "Directional geometry on surfaces: Rodrigues' formula for lines of curvature, Euler's theorem on normal curvature, the Dupin indicatrix conic sections, asymptotic directions and curves ($II = 0$), the Beltrami-Enneper theorem on the torsion of asymptotic curves ($\tau = \pm \sqrt{-K}$), conjugate directions, and triply orthogonal systems.",
        "simulations": ["sim_dg_dupin_indicatrix"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Rodrigues' Formula & Differential Equations of Lines of Curvature",
                "content": r"""### 1. Definition of Lines of Curvature

> **Definition 7.1 (Line of Curvature):**
> A regular curve $C$ on a surface $S$ is called a **line of curvature** (or curvature line) if its tangent vector at every point points along a principal direction of the surface.

---

### 2. Rodrigues' Formula

> **Theorem 7.1 (Rodrigues' Formula, 1815):**
> A regular curve $\mathbf{r}(t)$ on a surface $S$ is a line of curvature if and only if there exists a scalar function $\kappa(t)$ (the principal curvature) such that:
> $$d\mathbf{n} + \kappa \, d\mathbf{r} = \mathbf{0} \iff \mathbf{n}'(t) = -\kappa(t) \mathbf{r}'(t)$$

> **Proof:**
> By definition, $\mathbf{r}'(t)$ is an eigenvector of the Shape Operator $S_p$ if and only if:
> $$S_p(\mathbf{r}'(t)) = \kappa(t) \mathbf{r}'(t)$$
> Recall that the Shape Operator is defined by $S_p(\mathbf{w}) = -d\mathbf{n}_p(\mathbf{w})$.
> Applying this to $\mathbf{w} = \mathbf{r}'(t)$:
> $$-d\mathbf{n}(\mathbf{r}'(t)) = -\mathbf{n}'(t) = \kappa(t) \mathbf{r}'(t) \iff \mathbf{n}'(t) + \kappa(t) \mathbf{r}'(t) = \mathbf{0}$$
> This establishes Rodrigues' formula directly. $\blacksquare$

---

### 3. Differential Equation of Lines of Curvature

Let $d\mathbf{r} = \mathbf{r}_u \, du + \mathbf{r}_v \, dv$ and $d\mathbf{n} = \mathbf{n}_u \, du + \mathbf{n}_v \, dv$.
By Rodrigues' formula, $d\mathbf{n}$ is collinear with $d\mathbf{r}$.
Hence, their cross product must vanish in $\mathbb{R}^3$:
$$d\mathbf{n} \times d\mathbf{r} = \mathbf{0}$$
Since both $d\mathbf{n}$ and $d\mathbf{r}$ lie in the tangent plane $T_p S$, the vector $d\mathbf{n} \times d\mathbf{r}$ is parallel to the normal vector $\mathbf{n}$.
Therefore:
$$(d\mathbf{n} \times d\mathbf{r}) \cdot \mathbf{n} = 0 \iff \det(d\mathbf{r}, d\mathbf{n}, \mathbf{n}) = 0$$
Using the Weingarten equations to express $d\mathbf{n}$ in terms of $E, F, G$ and $L, M, N$, this determinant expands into the classical Monge-Darby determinant:

> **Theorem 7.2 (Differential Equation of Lines of Curvature):**
> The lines of curvature on a surface patch satisfy the second-order quadratic ODE:
> $$\det \begin{pmatrix} dv^2 & -du \, dv & du^2 \\ E & F & G \\ L & M & N \end{pmatrix} = 0$$
> Expanding this $3 \times 3$ determinant:
> $$(EM - FL) \, du^2 + (EN - GL) \, du \, dv + (FN - GM) \, dv^2 = 0$$

> **Corollary 7.1 (Coordinate Curves as Lines of Curvature):**
> The coordinate curves $u = \text{const}$ and $v = \text{const}$ form a family of lines of curvature if and only if:
> $$F = 0 \quad \text{and} \quad M = 0$$
> In this case, the principal curvatures are simply $\kappa_1 = L/E$ and $\kappa_2 = N/G$."""
            },
            {
                "secNumber": "7.2",
                "title": "Euler's Theorem on Normal Curvature & Mean Curvature Invariance",
                "content": r"""### 1. Statement and Proof of Euler's Formula

Let $p \in S$ be a non-umbilical point ($\kappa_1 \ne \kappa_2$).
Choose an orthonormal basis $\{\mathbf{e}_1, \mathbf{e}_2\}$ in $T_p S$ along the principal directions:
$$S_p(\mathbf{e}_1) = \kappa_1 \mathbf{e}_1, \qquad S_p(\mathbf{e}_2) = \kappa_2 \mathbf{e}_2$$
Any unit tangent vector $\mathbf{u} \in T_p S$ can be represented as:
$$\mathbf{u} = \cos\theta \, \mathbf{e}_1 + \sin\theta \, \mathbf{e}_2$$
where $\theta \in [0, 2\pi)$ is the angle made by $\mathbf{u}$ with the first principal direction $\mathbf{e}_1$.

> **Theorem 7.3 (Euler's Theorem, 1760):**
> The normal curvature $\kappa_n(\theta)$ along the direction making an angle $\theta$ with the first principal direction is given by:
> $$\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta$$

> **Proof:**
> Recall from Section 5.2 that the normal curvature along a unit tangent vector $\mathbf{u}$ is:
> $$\kappa_n = II(\mathbf{u}) = \langle S_p(\mathbf{u}), \mathbf{u} \rangle$$
> Substituting $\mathbf{u} = \cos\theta \, \mathbf{e}_1 + \sin\theta \, \mathbf{e}_2$:
> $$S_p(\mathbf{u}) = \cos\theta \, S_p(\mathbf{e}_1) + \sin\theta \, S_p(\mathbf{e}_2) = \kappa_1 \cos\theta \, \mathbf{e}_1 + \kappa_2 \sin\theta \, \mathbf{e}_2$$
> Taking the inner product with $\mathbf{u}$:
> $$\langle S_p(\mathbf{u}), \mathbf{u} \rangle = (\kappa_1 \cos\theta \, \mathbf{e}_1 + \kappa_2 \sin\theta \, \mathbf{e}_2) \cdot (\cos\theta \, \mathbf{e}_1 + \sin\theta \, \mathbf{e}_2)$$
> Since $\mathbf{e}_1 \cdot \mathbf{e}_1 = 1$, $\mathbf{e}_2 \cdot \mathbf{e}_2 = 1$, and $\mathbf{e}_1 \cdot \mathbf{e}_2 = 0$:
> $$\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta \quad \blacksquare$$

---

### 2. Orthogonal Pairs and the Invariance of Mean Curvature

Consider two mutually perpendicular tangent directions: $\theta$ and $\theta + \pi/2$.
The normal curvature in the perpendicular direction is:
$$\kappa_n\left(\theta + \frac{\pi}{2}\right) = \kappa_1 \cos^2\left(\theta + \frac{\pi}{2}\right) + \kappa_2 \sin^2\left(\theta + \frac{\pi}{2}\right) = \kappa_1 \sin^2\theta + \kappa_2 \cos^2\theta$$
Adding the two normal curvatures together:
$$\kappa_n(\theta) + \kappa_n\left(\theta + \frac{\pi}{2}\right) = \kappa_1(\cos^2\theta + \sin^2\theta) + \kappa_2(\sin^2\theta + \cos^2\theta) = \kappa_1 + \kappa_2 = 2H$$

> **Corollary 7.2 (Invariance of Sum of Orthogonal Curvatures):**
> For any pair of orthogonal unit tangent vectors on a surface, the sum of their normal curvatures is constant and equals twice the Mean Curvature:
> $$\kappa_n(\theta) + \kappa_n\left(\theta + \frac{\pi}{2}\right) = 2H$$"""
            },
            {
                "secNumber": "7.3",
                "title": "The Dupin Indicatrix & Osculating Quadrics",
                "content": r"""### 1. Construction of the Dupin Indicatrix

The Dupin indicatrix is a geometric construction in the tangent plane $T_p S$ that visually characterizes the local second-order shape of the surface.
Let Cartesian coordinates $(\xi, \eta)$ be chosen in $T_p S$ along the principal directions $\mathbf{e}_1, \mathbf{e}_2$.
For each direction defined by angle $\theta$ ($\xi = r \cos\theta, \eta = r \sin\theta$), plot a segment of length:
$$r = \frac{1}{\sqrt{|\kappa_n(\theta)|}}$$
Squaring and multiplying by $|\kappa_n(\theta)|$:
$$r^2 |\kappa_n(\theta)| = 1 \iff r^2 |\kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta| = 1$$
Substituting $\xi = r \cos\theta$ and $\eta = r \sin\theta$:
$$|\kappa_1 \xi^2 + \kappa_2 \eta^2| = 1$$

> **Definition 7.2 (The Dupin Indicatrix):**
> The **Dupin indicatrix** at a point $p \in S$ is the quadratic curve in $T_p S$ given by:
> $$\kappa_1 \xi^2 + \kappa_2 \eta^2 = \pm 1$$

---

### 2. Geometric Shape Depending on Point Type

1. **At an Elliptic Point ($K > 0$):**
   $\kappa_1$ and $\kappa_2$ have the same sign.
   The equation is:
   $$\kappa_1 \xi^2 + \kappa_2 \eta^2 = 1 \quad (\text{if } \kappa_1, \kappa_2 > 0)$$
   This is an **ellipse** with semi-axes $a = 1/\sqrt{\kappa_1}$ and $b = 1/\sqrt{\kappa_2}$.
   If the point is an umbilic ($\kappa_1 = \kappa_2$), the ellipse becomes a circle.
2. **At a Hyperbolic Point ($K < 0$):**
   $\kappa_1$ and $\kappa_2$ have opposite signs (say $\kappa_1 > 0, \kappa_2 < 0$).
   The Dupin indicatrix consists of a pair of **conjugate hyperbolas**:
   $$\kappa_1 \xi^2 - |\kappa_2| \eta^2 = 1 \quad \text{and} \quad \kappa_1 \xi^2 - |\kappa_2| \eta^2 = -1$$
   The asymptotes of these hyperbolas are given by $\kappa_1 \xi^2 + \kappa_2 \eta^2 = 0$, which correspond to the **asymptotic directions** of the surface!
3. **At a Parabolic Point ($K = 0, \kappa_1 \ne 0, \kappa_2 = 0$):**
   The equation reduces to:
   $$\kappa_1 \xi^2 = \pm 1 \implies \xi = \pm \frac{1}{\sqrt{|\kappa_1|}}$$
   This is a pair of **parallel straight lines** parallel to the direction of zero curvature."""
            },
            {
                "secNumber": "7.4",
                "title": "Asymptotic Curves & The Beltrami-Enneper Torsion Theorem",
                "content": r"""### 1. Asymptotic Directions and Curves

> **Definition 7.3 (Asymptotic Direction and Curve):**
> 1. A tangent direction $(du, dv)$ at $p \in S$ is called an **asymptotic direction** if the normal curvature along that direction is zero:
>    $$\kappa_n = 0 \iff II(du, dv) = L \, du^2 + 2M \, du \, dv + N \, dv^2 = 0$$
> 2. A regular curve on $S$ whose tangent vector at every point points along an asymptotic direction is called an **asymptotic curve** (or asymptotic line).

From Euler's theorem, $\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta = 0$:
$$\tan^2\theta = -\frac{\kappa_1}{\kappa_2}$$
- At an **elliptic point** ($K > 0$): $\kappa_1 / \kappa_2 > 0$, so $\tan^2\theta < 0$, which has **no real solutions**. There are no asymptotic directions at elliptic points!
- At a **parabolic point** ($K = 0$): there is **one unique** asymptotic direction (along the direction of $\kappa_2 = 0$).
- At a **hyperbolic point** ($K < 0$): $\tan\theta = \pm \sqrt{-\kappa_1 / \kappa_2}$, yielding **two distinct real asymptotic directions** symmetric about the principal directions!

---

### 2. The Beltrami-Enneper Theorem

Along an asymptotic curve, $\kappa_n = \kappa \cos \theta = 0$.
Assuming the space curvature $\kappa > 0$, Meusnier's theorem dictates that $\cos \theta = 0 \implies \mathbf{N} \cdot \mathbf{n} = 0$.
Thus, the principal normal to the curve $\mathbf{N}$ is perpendicular to the surface normal $\mathbf{n}$!
Consequently, the binormal vector $\mathbf{B} = \mathbf{T} \times \mathbf{N}$ is parallel to $\mathbf{n}$:
$$\mathbf{B} = \pm \mathbf{n}$$
The osculating plane of an asymptotic curve coincides with the tangent plane to the surface!

> **Theorem 7.4 (Beltrami-Enneper Theorem, 1870):**
> Let $C$ be an asymptotic curve with non-vanishing space curvature $\kappa > 0$ on a surface with negative Gaussian curvature $K < 0$.
> Then the torsion $\tau$ of the asymptotic curve satisfies:
> $$\tau^2 = -K \iff \tau = \pm \sqrt{-K}$$

> **Proof:**
> Along the asymptotic curve, the binormal satisfies $\mathbf{B} = \mathbf{n}$ (up to a sign $\pm 1$).
> By the Serret-Frenet formulas:
> $$\mathbf{B}'(s) = -\tau(s) \mathbf{N}(s)$$
> Taking the norm squared:
> $$\|\mathbf{B}'(s)\|^2 = \tau^2$$
> Since $\mathbf{B} = \mathbf{n}$, $\mathbf{B}'(s) = d\mathbf{n}(\mathbf{T}) = -S_p(\mathbf{T})$.
> Thus:
> $$\tau^2 = \|S_p(\mathbf{T})\|^2 = \langle S_p^2(\mathbf{T}), \mathbf{T} \rangle = III(\mathbf{T})$$
> By the fundamental form identity (Theorem 5.4):
> $$III(\mathbf{T}) = 2H II(\mathbf{T}) - K I(\mathbf{T})$$
> Since the curve is asymptotic, $II(\mathbf{T}) = 0$.
> Since $\mathbf{T}$ is a unit vector, $I(\mathbf{T}) = 1$.
> Substituting these values:
> $$\tau^2 = 2H(0) - K(1) = -K$$
> Since $K < 0$, $-K > 0$, taking the square root gives:
> $$\tau = \pm \sqrt{-K} \quad \blacksquare$$"""
            },
            {
                "secNumber": "7.5",
                "title": "Conjugate Directions, Koenigs Nets & Triply Orthogonal Systems",
                "content": r"""### 1. Conjugate Directions

> **Definition 7.4 (Conjugate Directions):**
> Two tangent directions $\mathbf{w}_1 = (du, dv)$ and $\mathbf{w}_2 = (\delta u, \delta v)$ at $p \in S$ are called **conjugate directions** if:
> $$\langle S_p(\mathbf{w}_1), \mathbf{w}_2 \rangle = 0 \iff -d\mathbf{n}(\mathbf{w}_1) \cdot \mathbf{w}_2 = 0$$
> In coordinates, the conjugacy condition is:
> $$L \, du \, \delta u + M(du \, \delta v + dv \, \delta u) + N \, dv \, \delta v = 0$$

> **Theorem 7.5 (Geometric Properties of Conjugate Directions):**
> 1. The principal directions are the only mutually orthogonal conjugate directions.
> 2. An asymptotic direction is self-conjugate ($II(du, dv) = 0$).
> 3. Two directions $\theta_1, \theta_2$ relative to the principal frame are conjugate if and only if:
>    $$\kappa_1 \cos\theta_1 \cos\theta_2 + \kappa_2 \sin\theta_1 \sin\theta_2 = 0 \iff \tan\theta_1 \tan\theta_2 = -\frac{\kappa_1}{\kappa_2}$$

---

### 2. Triply Orthogonal Systems & Dupin's Theorem

> **Definition 7.5 (Triply Orthogonal System):**
> A system of three families of surfaces in $\mathbb{R}^3$ is called a **triply orthogonal system** if through each point there passes exactly one surface from each family, and the three surfaces intersect each other pairwise orthogonally.

> **Theorem 7.6 (Dupin's Theorem, 1813):**
> The intersection curves of the surfaces of any triply orthogonal system are lines of curvature on all three intersecting surfaces!

*Example:* Confocal quadrics (ellipsoids, hyperboloids of one sheet, and hyperboloids of two sheets sharing the same focal conics) form a triply orthogonal system. By Dupin's Theorem, their curves of intersection are automatically the lines of curvature on each quadric surface!"""
            }
        ],
        "problems": [
            {
                "id": "dg-prob-7-1",
                "tier": "Foundational",
                "title": "Verification of Euler's Formula & Directional Average of Normal Curvature",
                "statement": r"""Let $p \in S$ be a regular point with principal curvatures $\kappa_1$ and $\kappa_2$.
1. By Euler's formula, the normal curvature in direction $\theta$ is $\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta$. Prove that the maximum and minimum values of $\kappa_n(\theta)$ over $\theta \in [0, 2\pi)$ are indeed $\kappa_1$ and $\kappa_2$.
2. Compute the angular average of the normal curvature:
   $$\bar{\kappa}_n = \frac{1}{2\pi} \int_0^{2\pi} \kappa_n(\theta) \, d\theta$$
   and show that this average is identically equal to the Mean Curvature $H$.""",
                "hints": [
                    "Recall that cos^2(theta) = (1 + cos(2*theta))/2 and sin^2(theta) = (1 - cos(2*theta))/2.",
                    "Integrate cos(2*theta) over [0, 2*pi]; it vanishes.",
                    "Verify that the average simplifies to (kappa_1 + kappa_2)/2."
                ],
                "solution": r"""### 1. Extrema of Euler's Formula
Euler's formula gives:
$$\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta$$
Without loss of generality, assume $\kappa_1 \ge \kappa_2$.
Rewriting $\sin^2\theta = 1 - \cos^2\theta$:
$$\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 (1 - \cos^2\theta) = \kappa_2 + (\kappa_1 - \kappa_2)\cos^2\theta$$
Since $0 \le \cos^2\theta \le 1$:
- When $\cos^2\theta = 1$ ($\theta = 0$ or $\theta = \pi$), $\kappa_n(\theta) = \kappa_2 + (\kappa_1 - \kappa_2)(1) = \kappa_1$ (maximum).
- When $\cos^2\theta = 0$ ($\theta = \pi/2$ or $\theta = 3\pi/2$), $\kappa_n(\theta) = \kappa_2 + (\kappa_1 - \kappa_2)(0) = \kappa_2$ (minimum).
Thus, the principal curvatures $\kappa_1$ and $\kappa_2$ are the absolute maximum and minimum of normal curvature! $\blacksquare$

---

### 2. Angular Average of Normal Curvature
Using the half-angle identities:
$$\cos^2\theta = \frac{1 + \cos(2\theta)}{2}, \qquad \sin^2\theta = \frac{1 - \cos(2\theta)}{2}$$
Substitute these into Euler's formula:
$$\kappa_n(\theta) = \kappa_1 \left(\frac{1 + \cos(2\theta)}{2}\right) + \kappa_2 \left(\frac{1 - \cos(2\theta)}{2}\right) = \frac{\kappa_1 + \kappa_2}{2} + \frac{\kappa_1 - \kappa_2}{2} \cos(2\theta)$$
Now integrate over $\theta \in [0, 2\pi)$:
$$\int_0^{2\pi} \kappa_n(\theta) \, d\theta = \int_0^{2\pi} \left[ \frac{\kappa_1 + \kappa_2}{2} + \frac{\kappa_1 - \kappa_2}{2} \cos(2\theta) \right] d\theta$$
Notice that:
$$\int_0^{2\pi} \cos(2\theta) \, d\theta = \left[ \frac{\sin(2\theta)}{2} \right]_0^{2\pi} = \frac{\sin(4\pi) - \sin(0)}{2} = 0$$
Therefore:
$$\int_0^{2\pi} \kappa_n(\theta) \, d\theta = \int_0^{2\pi} \frac{\kappa_1 + \kappa_2}{2} \, d\theta = \left(\frac{\kappa_1 + \kappa_2}{2}\right)(2\pi)$$
Dividing by $2\pi$:
$$\bar{\kappa}_n = \frac{1}{2\pi} \int_0^{2\pi} \kappa_n(\theta) \, d\theta = \frac{\kappa_1 + \kappa_2}{2} = H \quad \blacksquare$$

This provides a beautiful physical and geometric interpretation: the Mean Curvature $H$ is the exact uniform average of normal curvatures over all possible directions!"""
            },
            {
                "id": "dg-prob-7-2",
                "tier": "Advanced",
                "title": "Asymptotic Curves of the Catenoid & Orthogonality",
                "statement": r"""Consider the standard Catenoid parametrized by:
$$\mathbf{r}(u, v) = \begin{pmatrix} \cosh u \cos v \\ \cosh u \sin v \\ u \end{pmatrix}, \quad u \in \mathbb{R}, \; v \in [0, 2\pi)$$
Recall that $E = \cosh^2 u$, $F = 0$, $G = \cosh^2 u$, and $L = -1$, $M = 0$, $N = 1$.
1. Set up the differential equation of asymptotic curves $II = 0$.
2. Solve this differential equation explicitly to find the two families of asymptotic curves.
3. Show that these two families of curves intersect at right angles everywhere on the catenoid.""",
                "hints": [
                    "Recall II = L du^2 + 2M dudv + N dv^2 = 0.",
                    "With L = -1, M = 0, N = 1, this factors as -du^2 + dv^2 = 0.",
                    "Integrate du = +/- dv, then test orthogonality using the First Fundamental Form."
                ],
                "solution": r"""### 1. Differential Equation of Asymptotic Curves
The condition for an asymptotic direction is:
$$II(du, dv) = L \, du^2 + 2M \, du \, dv + N \, dv^2 = 0$$
For the catenoid, $L = -1$, $M = 0$, and $N = 1$.
Thus:
$$-du^2 + 0 + dv^2 = 0 \iff dv^2 - du^2 = 0 \quad \blacksquare$$

---

### 2. Solving for the Families of Curves
Factor the difference of squares:
$$(dv - du)(dv + du) = 0$$
This yields two first-order ODEs:
1. Family 1: $dv - du = 0 \implies \frac{dv}{du} = 1 \implies v - u = c_1$
2. Family 2: $dv + du = 0 \implies \frac{dv}{du} = -1 \implies v + u = c_2$
where $c_1, c_2$ are arbitrary integration constants.
These are straight diagonal lines in the $uv$-parameter plane! $\blacksquare$

---

### 3. Orthogonality of the Asymptotic Net
Let direction 1 be $(du_1, dv_1) = (1, 1) \, dt$ and direction 2 be $(du_2, dv_2) = (1, -1) \, ds$.
The inner product of these tangent directions with respect to the First Fundamental Form is:
$$\langle d\mathbf{r}_1, d\mathbf{r}_2 \rangle = E \, du_1 \, du_2 + F(du_1 \, dv_2 + dv_1 \, du_2) + G \, dv_1 \, dv_2$$
Recall that $E = G = \cosh^2 u$ and $F = 0$:
$$\langle d\mathbf{r}_1, d\mathbf{r}_2 \rangle = \cosh^2 u (1)(1) + 0 + \cosh^2 u (1)(-1) = \cosh^2 u - \cosh^2 u = 0$$
Because the inner product vanishes everywhere on the surface, the two families of asymptotic curves form an **orthogonal net**!

> **Remark:** On any minimal surface ($H = 0$), $\kappa_1 = -\kappa_2$. By Euler's formula, $\kappa_n(\theta) = \kappa_1(\cos^2\theta - \sin^2\theta) = \kappa_1 \cos(2\theta) = 0 \implies 2\theta = \pm \pi/2 \implies \theta = \pm \pi/4$.
> Hence, on any minimal surface, the asymptotic directions bisect the principal directions and are always mutually orthogonal! $\blacksquare$"""
            },
            {
                "id": "dg-prob-7-3",
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Proof of the Beltrami-Enneper Torsion Theorem",
                "statement": r"""Let $S \subset \mathbb{R}^3$ be a $C^3$ regular surface with negative Gaussian curvature $K < 0$, and let $C: \mathbf{r}(s)$ be an asymptotic curve on $S$ parametrized by arc-length $s$ with space curvature $\kappa(s) > 0$.
1. Prove that the binormal vector $\mathbf{B}(s)$ to the curve is collinear with the surface normal $\mathbf{n}(s)$, and determine the sign relationship.
2. Differentiate $\mathbf{B}(s) = \pm \mathbf{n}(s)$ along the curve and express $\mathbf{n}'(s)$ using the Shape Operator.
3. Compute the torsion $\tau(s)$ of the curve and prove that $\tau^2 = -K(s)$, so that $\tau(s) = \pm \sqrt{-K(s)}$.""",
                "hints": [
                    "Recall that for an asymptotic curve, normal curvature kappa_n = 0.",
                    "Meusnier's theorem gives kappa_n = kappa * (N . n) = 0, so N is perpendicular to n.",
                    "Since both T and N are perpendicular to n, B = T x N must be parallel to n."
                ],
                "solution": r"""### 1. Collinearity of Binormal and Surface Normal
Let $C: \mathbf{r}(s)$ be parametrized by arc-length.
Its unit tangent is $\mathbf{T}(s) = \mathbf{r}'(s) \in T_p S$, so $\mathbf{T} \cdot \mathbf{n} = 0$.
By Serret-Frenet, $\mathbf{r}''(s) = \kappa \mathbf{N}$.
The normal curvature of the curve on the surface is:
$$\kappa_n = \mathbf{r}''(s) \cdot \mathbf{n} = \kappa (\mathbf{N} \cdot \mathbf{n})$$
Because $C$ is an asymptotic curve, $\kappa_n = 0$ by definition.
Since $\kappa > 0$ by assumption:
$$\mathbf{N} \cdot \mathbf{n} = 0$$
Thus, both $\mathbf{T}$ and $\mathbf{N}$ are orthogonal to the surface normal $\mathbf{n}$.
In Euclidean 3-space, the orthogonal complement of the plane spanned by $\{\mathbf{T}, \mathbf{N}\}$ is one-dimensional, spanned by the binormal $\mathbf{B} = \mathbf{T} \times \mathbf{N}$.
Since $\mathbf{n}$ is orthogonal to both $\mathbf{T}$ and $\mathbf{N}$, and $\|\mathbf{n}\| = \|\mathbf{B}\| = 1$, we must have:
$$\mathbf{B}(s) = \epsilon \, \mathbf{n}(s), \quad \text{where } \epsilon = \pm 1 \quad \blacksquare$$

---

### 2. Derivative of the Normal and Binormal
Differentiating $\mathbf{B}(s) = \epsilon \, \mathbf{n}(s)$ with respect to arc-length $s$:
$$\mathbf{B}'(s) = \epsilon \, \mathbf{n}'(s)$$
By the third Serret-Frenet formula (Unit 2):
$$\mathbf{B}'(s) = -\tau(s) \mathbf{N}(s)$$
On the other hand, applying the chain rule to the Gauss map:
$$\mathbf{n}'(s) = d\mathbf{n}(\mathbf{r}'(s)) = d\mathbf{n}(\mathbf{T}) = -S_p(\mathbf{T})$$
where $S_p$ is the Shape Operator.
Equating the two expressions for $\mathbf{B}'(s)$:
$$-\tau(s) \mathbf{N}(s) = -\epsilon S_p(\mathbf{T}) \iff \tau(s) \mathbf{N}(s) = \epsilon S_p(\mathbf{T})$$

---

### 3. Evaluating the Torsion $\tau^2 = -K$
Taking the norm squared of both sides:
$$\tau(s)^2 \|\mathbf{N}(s)\|^2 = \epsilon^2 \|S_p(\mathbf{T})\|^2$$
Since $\|\mathbf{N}(s)\| = 1$ and $\epsilon^2 = 1$:
$$\tau^2 = \|S_p(\mathbf{T})\|^2 = \langle S_p(\mathbf{T}), S_p(\mathbf{T}) \rangle = \langle S_p^2(\mathbf{T}), \mathbf{T} \rangle = III(\mathbf{T})$$
Recall the fundamental form operator identity (Theorem 5.4):
$$III(\mathbf{T}) = 2H II(\mathbf{T}) - K I(\mathbf{T})$$
Because $\mathbf{T}$ points along an asymptotic direction, $II(\mathbf{T}) = 0$.
Because $\mathbf{T}$ is a unit tangent vector, $I(\mathbf{T}) = \|\mathbf{T}\|^2 = 1$.
Substituting these values:
$$\tau^2 = 2H(0) - K(1) = -K$$
Because $S$ has negative Gaussian curvature, $K < 0$, which ensures that $-K > 0$.
Taking the square root:
$$\tau(s) = \pm \sqrt{-K(s)} \quad \blacksquare$$

This remarkable theorem proves that the torsion of an asymptotic curve depends **only** on the Gaussian curvature of the surface at that point!"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u = get_unit7()
    print(f"Loaded Unit 7: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
