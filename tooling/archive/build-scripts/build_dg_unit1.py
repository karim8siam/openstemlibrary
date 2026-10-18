# -*- coding: utf-8 -*-
"""
build_dg_unit1.py
Constructs Unit 1: Theory of Space Curves: Arc-Length, Parametrization & Tangent Lines
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Theory of Space Curves: Arc-Length, Parametrization & Tangent Lines",
        "leadSummary": "Foundations of curve theory in 3D Euclidean space: vector-valued functions of a single real variable, regular parametrizations and velocity vectors, arc-length as an intrinsic geometric parameter, unit tangent vectors, equations of tangent lines, the osculating plane and order of contact, and canonical Taylor approximations near a regular point.",
        "simulations": ["sim_dg_space_curve_tangent"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Vector Functions of a Real Variable, Smooth Curves & Regular Parametrizations",
                "content": r"""### 1. Vector Functions and Curves in Euclidean 3-Space

Let $\mathbb{R}^3$ denote standard three-dimensional Euclidean space endowed with the Cartesian coordinate system and standard inner product $\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v}$.

> **Definition 1.1 (Parametrized Space Curve):**
> A **parametrized space curve** (or vector function of a real variable) is a continuous mapping:
> $$\mathbf{r}: I \to \mathbb{R}^3, \quad t \mapsto \mathbf{r}(t) = \begin{pmatrix} x(t) \\ y(t) \\ z(t) \end{pmatrix}$$
> where $I \subseteq \mathbb{R}$ is an interval of the real line.
> The set of image points $C = \mathbf{r}(I) \subset \mathbb{R}^3$ is the **trace** (or geometric trajectory) of the curve.

---

### 2. Differentiability and Regularity

> **Definition 1.2 (Smoothness and Regular Points):**
> 1. A curve $\mathbf{r}(t)$ is of **class $C^k$** ($k \ge 1$) if its component functions $x(t), y(t), z(t)$ possess continuous derivatives up to order $k$ on $I$.
> 2. The **velocity vector** (or derivative vector) at $t$ is:
>    $$\mathbf{r}'(t) = \frac{d\mathbf{r}}{dt} = \lim_{h \to 0} \frac{\mathbf{r}(t + h) - \mathbf{r}(t)}{h} = \begin{pmatrix} x'(t) \\ y'(t) \\ z'(t) \end{pmatrix}$$
>    The scalar speed is $v(t) = \|\mathbf{r}'(t)\| = \sqrt{x'(t)^2 + y'(t)^2 + z'(t)^2}$.
> 3. A point $t_0 \in I$ is called a **regular point** if:
>    $$\mathbf{r}'(t_0) \ne \mathbf{0} \iff \|\mathbf{r}'(t_0)\| > 0$$
>    If $\mathbf{r}'(t_0) = \mathbf{0}$, the point $t_0$ is called a **singular point** (or stationary point).
> 4. A curve $\mathbf{r}: I \to \mathbb{R}^3$ is **regular** if every point in $I$ is regular: $\mathbf{r}'(t) \ne \mathbf{0}$ for all $t \in I$.

> **Remark (Significance of Regularity):**
> Regularity guarantees that the curve possesses a well-defined direction of motion at every instant, avoiding cusps, halts, or instantaneous sharp corners. For instance, the curve $\mathbf{r}(t) = (t^2, t^3, 0)$ is $C^\infty$ smooth as a vector function, but has a singular point at $t = 0$ ($\mathbf{r}'(0) = \mathbf{0}$), forming a geometric cusp in the trace.

---

### 3. Reparametrization and Equivalence of Curves

> **Definition 1.3 (Admissible Reparametrization):**
> Let $\mathbf{r}: I \to \mathbb{R}^3$ be a $C^k$ curve ($k \ge 1$). Let $J \subseteq \mathbb{R}$ be another interval, and let $\phi: J \to I$ be a $C^k$ bijective scalar function such that:
> $$\phi'(\tau) \ne 0 \quad \forall \tau \in J$$
> The composition $\tilde{\mathbf{r}} = \mathbf{r} \circ \phi: J \to \mathbb{R}^3$ is called a **reparametrization** of $\mathbf{r}$.
> - If $\phi'(\tau) > 0$ for all $\tau \in J$, $\phi$ is an **orientation-preserving** reparametrization.
> - If $\phi'(\tau) < 0$ for all $\tau \in J$, $\phi$ is an **orientation-reversing** reparametrization.

By the Chain Rule:
$$\tilde{\mathbf{r}}'(\tau) = \frac{d}{d\tau}[\mathbf{r}(\phi(\tau))] = \mathbf{r}'(\phi(\tau)) \cdot \phi'(\tau)$$
Since $\phi'(\tau) \ne 0$, $\tilde{\mathbf{r}}'(\tau) \ne \mathbf{0} \iff \mathbf{r}'(\phi(\tau)) \ne \mathbf{0}$.
Thus regularity is an intrinsic property invariant under admissible reparametrizations."""
            },
            {
                "secNumber": "1.2",
                "title": "Arc-Length as an Intrinsic Invariant Parameter & Arc-Length Reparametrization",
                "content": r"""### 1. Arc-Length of a Curve Segment

Let $\mathbf{r}: [a, b] \to \mathbb{R}^3$ be a regular $C^1$ space curve.

> **Definition 1.4 (Arc-Length Function):**
> The **arc-length** of the curve between parameter values $t_0$ and $t$ ($t \ge t_0$) is defined by the definite Riemann integral:
> $$s(t) = \int_{t_0}^t \|\mathbf{r}'(u)\| \, du = \int_{t_0}^t \sqrt{x'(u)^2 + y'(u)^2 + z'(u)^2} \, du$$

---

### 2. Properties of the Arc-Length Parameter

> **Theorem 1.1 (Fundamental Properties of Arc-Length):**
> 1. By the Fundamental Theorem of Calculus:
>    $$\frac{ds}{dt} = \|\mathbf{r}'(t)\| = v(t) > 0$$
> 2. Since $\mathbf{r}$ is regular, $\frac{ds}{dt} > 0$ everywhere on $I$.
>    Therefore, the arc-length mapping $s: I \to [0, L]$ is **strictly increasing** and hence invertible.
> 3. The differential of arc-length satisfies the Pythagorean metric identity:
>    $$ds^2 = dx^2 + dy^2 + dz^2 = \langle d\mathbf{r}, d\mathbf{r} \rangle$$

---

### 3. Reparametrization by Arc-Length (Natural / Unit-Speed Parametrization)

Because $s(t)$ is strictly increasing, its inverse function $t = t(s) = s^{-1}(s)$ exists and is $C^1$ smooth by the Inverse Function Theorem:
$$\frac{dt}{ds} = \frac{1}{\frac{ds}{dt}} = \frac{1}{\|\mathbf{r}'(t)\|}$$

> **Definition 1.5 (Unit-Speed / Natural Parametrization):**
> Reparametrizing the curve with respect to arc-length $s$ yields the **natural parametrization**:
> $$\mathbf{r}(s) = \mathbf{r}(t(s))$$

> **Theorem 1.2 (Unit-Speed Characterization):**
> A regular curve $\mathbf{r}(s)$ is parametrized by arc-length if and only if its velocity vector has constant unit magnitude at every point:
> $$\left\| \frac{d\mathbf{r}}{ds} \right\| \equiv 1 \quad \forall s$$

#### Complete Line-by-Line Proof:
Using the Chain Rule:
$$\frac{d\mathbf{r}}{ds} = \frac{d\mathbf{r}}{dt} \frac{dt}{ds} = \mathbf{r}'(t) \cdot \frac{1}{\|\mathbf{r}'(t)\|}$$
Taking the Euclidean norm of both sides:
$$\left\| \frac{d\mathbf{r}}{ds} \right\| = \left\| \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|} \right\| = \frac{\|\mathbf{r}'(t)\|}{\|\mathbf{r}'(t)\|} = 1 \quad \blacksquare$$
Parametrization by arc-length is the **natural metric parametrization** of differential geometry because it frees all geometric quantities (curvature, torsion, normal vectors) from artificial velocity variations."""
            },
            {
                "secNumber": "1.3",
                "title": "The Unit Tangent Vector, Tangent Lines & Order of Contact",
                "content": r"""### 1. The Unit Tangent Vector

> **Definition 1.6 (Unit Tangent Vector $\mathbf{T}$):**
> Let $\mathbf{r}: I \to \mathbb{R}^3$ be a regular curve.
> 1. For an arbitrary parameter $t$:
>    $$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$$
> 2. For an arc-length natural parameter $s$:
>    $$\mathbf{T}(s) = \mathbf{r}'(s) = \frac{d\mathbf{r}}{ds}$$
> Clearly, $\|\mathbf{T}(s)\| = 1$ for all $s$.

---

### 2. Equation of the Tangent Line

> **Definition 1.7 (Tangent Line to a Space Curve):**
> The **tangent line** to the curve $\mathbf{r}(t)$ at the point $P_0 = \mathbf{r}(t_0)$ is the straight line passing through $P_0$ collinear with the velocity vector $\mathbf{r}'(t_0)$.
> Its vector parametric equation is:
> $$\mathbf{X}(\lambda) = \mathbf{r}(t_0) + \lambda \mathbf{r}'(t_0), \quad \lambda \in \mathbb{R}$$
> In Cartesian coordinates, if $\mathbf{r}(t_0) = (x_0, y_0, z_0)$ and $\mathbf{r}'(t_0) = (x'_0, y'_0, z'_0)$:
> $$\frac{X - x_0}{x'_0} = \frac{Y - y_0}{y'_0} = \frac{Z - z_0}{z'_0}$$

---

### 3. Order of Contact

How tightly does a straight line, plane, or surface hug a space curve?

> **Definition 1.8 (Order of Contact):**
> Let $S$ be a smooth surface defined implicitly by $F(x, y, z) = 0$. Let $\mathbf{r}(t)$ be a curve meeting $S$ at $t = t_0$, so $F(\mathbf{r}(t_0)) = 0$.
> Define the composite scalar function $g(t) = F(\mathbf{r}(t))$.
> The curve and surface have **contact of order $n$** at $t = t_0$ if:
> $$g(t_0) = 0, \quad g'(t_0) = 0, \quad g''(t_0) = 0, \quad \dots, \quad g^{(n)}(t_0) = 0, \quad \text{and } g^{(n+1)}(t_0) \ne 0$$
> - A generic secant line intersects a curve with contact of order 0.
> - The **tangent line** is the unique straight line having contact of **order $\ge 1$** with the curve at $t_0$."""
            },
            {
                "secNumber": "1.4",
                "title": "The Osculating Plane (Plane of Curvature) & Analytical Equation",
                "content": r"""### 1. Geometric Definition of the Osculating Plane

The word *osculating* originates from the Latin *osculari* ("to kiss"). The osculating plane is the unique plane that "kisses" the curve most closely at a given point.

> **Definition 1.9 (Osculating Plane):**
> Let $\mathbf{r}(t)$ be a regular curve of class $C^2$ such that $\mathbf{r}'(t) \times \mathbf{r}''(t) \ne \mathbf{0}$.
> The **osculating plane** at point $P_0 = \mathbf{r}(t_0)$ is defined equivalently as:
> 1. The limiting position of the plane passing through three distinct points $P_0, P_1, P_2$ on the curve as $P_1, P_2 \to P_0$.
> 2. The limiting position of the plane containing the tangent line at $P_0$ and a neighboring point $P_1$ as $P_1 \to P_0$.
> 3. The unique plane having **contact of order $\ge 2$** with the curve at $P_0$.

---

### 2. Analytical Equation of the Osculating Plane

> **Theorem 1.3 (Osculating Plane Equation):**
> Let $\mathbf{X} = (X, Y, Z)$ be an arbitrary point in the osculating plane to $\mathbf{r}(t)$ at $t = t_0$.
> 1. In vector scalar triple product form:
>    $$[\mathbf{X} - \mathbf{r}(t_0), \; \mathbf{r}'(t_0), \; \mathbf{r}''(t_0)] = 0 \iff (\mathbf{X} - \mathbf{r}(t_0)) \cdot (\mathbf{r}'(t_0) \times \mathbf{r}''(t_0)) = 0$$
> 2. In determinant form:
>    $$\begin{vmatrix}
>    X - x(t_0) & Y - y(t_0) & Z - z(t_0) \\
>    x'(t_0) & y'(t_0) & z'(t_0) \\
>    x''(t_0) & y''(t_0) & z''(t_0)
>    \end{vmatrix} = 0$$
> 3. For an arc-length parametrized curve $\mathbf{r}(s)$:
>    $$[\mathbf{X} - \mathbf{r}(s_0), \; \mathbf{r}'(s_0), \; \mathbf{r}''(s_0)] = 0 \iff (\mathbf{X} - \mathbf{r}(s_0)) \cdot (\mathbf{T}(s_0) \times \mathbf{T}'(s_0)) = 0$$

#### Line-by-Line Proof:
Let $\Pi$ be a plane passing through $\mathbf{r}(t_0)$ with unit normal $\mathbf{n}_\Pi$:
$$F(\mathbf{X}) = (\mathbf{X} - \mathbf{r}(t_0)) \cdot \mathbf{n}_\Pi = 0$$
Define the distance function along the curve:
$$g(t) = F(\mathbf{r}(t)) = (\mathbf{r}(t) - \mathbf{r}(t_0)) \cdot \mathbf{n}_\Pi$$
For $\Pi$ to have contact of order $\ge 2$ with the curve at $t_0$, we require:
1. $g(t_0) = (\mathbf{r}(t_0) - \mathbf{r}(t_0)) \cdot \mathbf{n}_\Pi = 0$ (satisfied automatically).
2. $g'(t_0) = \mathbf{r}'(t_0) \cdot \mathbf{n}_\Pi = 0$.
   This implies that $\mathbf{n}_\Pi$ is perpendicular to the velocity vector $\mathbf{r}'(t_0)$.
3. $g''(t_0) = \mathbf{r}''(t_0) \cdot \mathbf{n}_\Pi = 0$.
   This implies that $\mathbf{n}_\Pi$ is also perpendicular to the acceleration vector $\mathbf{r}''(t_0)$.

Since the normal vector $\mathbf{n}_\Pi$ is perpendicular to both $\mathbf{r}'(t_0)$ and $\mathbf{r}''(t_0)$, it must be collinear with their vector cross product:
$$\mathbf{n}_\Pi \parallel \mathbf{r}'(t_0) \times \mathbf{r}''(t_0)$$
Therefore, any displacement vector $\mathbf{X} - \mathbf{r}(t_0)$ in the plane $\Pi$ must satisfy:
$$(\mathbf{X} - \mathbf{r}(t_0)) \cdot (\mathbf{r}'(t_0) \times \mathbf{r}''(t_0)) = 0 \quad \blacksquare$$

---

### 3. Tangent and Normal Planes for Implicit Surfaces

> **Definition 1.10 (Tangent and Normal Planes of Surfaces):**
> Let a surface be given implicitly by $F(x, y, z) = 0$, and let $P_0 = (x_0, y_0, z_0)$ be a regular point ($\nabla F(P_0) \ne \mathbf{0}$).
> 1. The **normal vector** to the surface at $P_0$ is the gradient vector:
>    $$\mathbf{n} = \nabla F(P_0) = \left( \frac{\partial F}{\partial x}, \frac{\partial F}{\partial y}, \frac{\partial F}{\partial z} \right)_{P_0}$$
> 2. The **tangent plane** to the surface at $P_0$ has equation:
>    $$\nabla F(P_0) \cdot (\mathbf{X} - \mathbf{P}_0) = 0 \iff F_x(X - x_0) + F_y(Y - y_0) + F_z(Z - z_0) = 0$$
> 3. The **normal line** to the surface at $P_0$ is:
>    $$\frac{X - x_0}{F_x} = \frac{Y - y_0}{F_y} = \frac{Z - z_0}{F_z}$$"""
            },
            {
                "secNumber": "1.5",
                "title": "Canonical Local Form & Taylor Expansions Near a Regular Point",
                "content": r"""### 1. Taylor Expansion of a Space Curve

Let $\mathbf{r}(s)$ be an arc-length parametrized $C^3$ curve with $\mathbf{r}(0) = \mathbf{0}$.
Expanding $\mathbf{r}(s)$ in a Taylor series about $s = 0$:
$$\mathbf{r}(s) = \mathbf{r}(0) + s \mathbf{r}'(0) + \frac{s^2}{2} \mathbf{r}''(0) + \frac{s^3}{6} \mathbf{r}'''(0) + O(s^4)$$
Recall:
- $\mathbf{r}'(0) = \mathbf{T}$ (unit tangent vector).
- $\mathbf{r}''(0) = \mathbf{T}' = \kappa \mathbf{N}$ (curvature $\times$ principal normal).
- $\mathbf{r}'''(0) = (\kappa \mathbf{N})' = \kappa' \mathbf{N} + \kappa \mathbf{N}' = \kappa' \mathbf{N} + \kappa (-\kappa \mathbf{T} + \tau \mathbf{B}) = -\kappa^2 \mathbf{T} + \kappa' \mathbf{N} + \kappa \tau \mathbf{B}$.

---

### 2. The Canonical Coordinate Form

Adopting the Frenet trihedron $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ at $s = 0$ as a local Cartesian basis, any point on the curve has coordinates $\mathbf{r}(s) = x(s) \mathbf{T} + y(s) \mathbf{N} + z(s) \mathbf{B}$:
$$\begin{aligned}
x(s) &= s - \frac{\kappa^2}{6} s^3 + O(s^4) \\
y(s) &= \frac{\kappa}{2} s^2 + \frac{\kappa'}{6} s^3 + O(s^4) \\
z(s) &= \frac{\kappa \tau}{6} s^3 + O(s^4)
\end{aligned}$$

---

### 3. Geometric Projections onto the Fundamental Coordinate Planes

By eliminating $s$ in the lowest-order leading terms, we discover the local geometric silhouette of any space curve:
1. **Projection onto the Osculating Plane (Span{$\mathbf{T}, \mathbf{N}$}, $xy$-plane):**
   $$y \approx \frac{\kappa}{2} x^2$$
   To leading order, the curve resembles a **parabola** opening along the principal normal $\mathbf{N}$.
2. **Projection onto the Rectifying Plane (Span{$\mathbf{T}, \mathbf{B}$}, $xz$-plane):**
   $$z \approx \frac{\kappa \tau}{6} x^3$$
   To leading order, the curve resembles a **cubic inflection** crossing its tangent line.
3. **Projection onto the Normal Plane (Span{$\mathbf{N}, \mathbf{B}$}, $yz$-plane):**
   $$z^2 \approx \frac{2 \tau^2}{9 \kappa} y^3 \iff y^3 \sim z^2$$
   To leading order, the curve projects as a **semicubical Neil's cusp**!"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 1.1",
                "title": "Arc-Length Reparametrization & Osculating Plane of the Twisted Cubic",
                "statement": r"""Consider the twisted cubic space curve given by:
$$\mathbf{r}(t) = \begin{pmatrix} t \\ t^2 \\ t^3 \end{pmatrix}, \quad t \in \mathbb{R}$$
1. Find the velocity vector $\mathbf{r}'(t)$, acceleration vector $\mathbf{r}''(t)$, and the cross product $\mathbf{r}'(t) \times \mathbf{r}''(t)$.
2. Determine the unit tangent vector $\mathbf{T}(t)$ and the Cartesian equation of the tangent line to the curve at $t = 1$.
3. Compute the exact Cartesian equation of the osculating plane to the curve at the point $t = 1$.""",
                "hints": [
                    "Differentiate componentwise: r'(t) = (1, 2t, 3t^2) and r''(t) = (0, 2, 6t).",
                    "The normal to the osculating plane is r'(1) x r''(1).",
                    "Equation of plane: n . (X - r(1)) = 0."
                ],
                "solution": r"""### 1. Velocity, Acceleration & Cross Product Computation
Differentiating $\mathbf{r}(t) = (t, t^2, t^3)^T$:
$$\mathbf{r}'(t) = \begin{pmatrix} 1 \\ 2t \\ 3t^2 \end{pmatrix}, \quad \mathbf{r}''(t) = \begin{pmatrix} 0 \\ 2 \\ 6t \end{pmatrix}$$
Now compute the cross product $\mathbf{r}'(t) \times \mathbf{r}''(t)$:
$$\mathbf{r}'(t) \times \mathbf{r}''(t) = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 2t & 3t^2 \\
0 & 2 & 6t
\end{vmatrix} = \mathbf{i}(12t^2 - 6t^2) - \mathbf{j}(6t - 0) + \mathbf{k}(2 - 0) = \begin{pmatrix} 6t^2 \\ -6t \\ 2 \end{pmatrix}$$

---

### 2. Unit Tangent Vector and Tangent Line at $t = 1$
At $t = 1$:
$$\mathbf{r}(1) = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{r}'(1) = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$$
The speed at $t = 1$ is:
$$\|\mathbf{r}'(1)\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}$$
Thus, the unit tangent vector is:
$$\mathbf{T}(1) = \frac{\mathbf{r}'(1)}{\|\mathbf{r}'(1)\|} = \frac{1}{\sqrt{14}} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$$
The vector equation of the tangent line at $t = 1$ is:
$$\mathbf{X}(\lambda) = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + \lambda \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \quad \lambda \in \mathbb{R}$$
In symmetric Cartesian form:
$$\frac{X - 1}{1} = \frac{Y - 1}{2} = \frac{Z - 1}{3} \quad \blacksquare$$

---

### 3. Cartesian Equation of the Osculating Plane at $t = 1$
At $t = 1$, the normal vector to the osculating plane is:
$$\mathbf{n}_{\text{osc}} = \mathbf{r}'(1) \times \mathbf{r}''(1) = \begin{pmatrix} 6(1)^2 \\ -6(1) \\ 2 \end{pmatrix} = \begin{pmatrix} 6 \\ -6 \\ 2 \end{pmatrix} = 2 \begin{pmatrix} 3 \\ -3 \\ 1 \end{pmatrix}$$
We can take the simplified normal vector $\mathbf{N}_0 = (3, -3, 1)^T$.
The equation of the osculating plane through $\mathbf{r}(1) = (1, 1, 1)$ is:
$$\mathbf{N}_0 \cdot (\mathbf{X} - \mathbf{r}(1)) = 0$$
$$3(X - 1) - 3(Y - 1) + 1(Z - 1) = 0$$
$$3X - 3 - 3Y + 3 + Z - 1 = 0 \iff 3X - 3Y + Z - 1 = 0 \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced / Problem 1.2",
                "title": "Rigorous Derivation of the Osculating Plane via Limiting Tangent Secants",
                "statement": r"""Let $\mathbf{r}(t)$ be a regular $C^3$ curve with $\mathbf{r}'(t) \times \mathbf{r}''(t) \ne \mathbf{0}$.
1. Consider the plane $\Pi(h)$ containing the tangent line at $\mathbf{r}(t)$ and passing through a neighboring point $\mathbf{r}(t + h)$ with $h \ne 0$. Find the normal vector $\mathbf{n}(h)$ to this plane.
2. Compute $\lim_{h \to 0} \frac{\mathbf{n}(h)}{h^2/2}$ and prove that the limiting plane coincides with the osculating plane $[\mathbf{X} - \mathbf{r}(t), \mathbf{r}'(t), \mathbf{r}''(t)] = 0$.
3. Prove that the distance $d(h)$ from the neighboring point $\mathbf{r}(t + h)$ to the osculating plane satisfies $d(h) = O(h^3)$, confirming contact of order $\ge 2$.""",
                "hints": [
                    "The plane contains the tangent direction r'(t) and the secant vector r(t + h) - r(t).",
                    "Use Taylor expansion r(t + h) - r(t) = h r'(t) + (h^2 / 2) r''(t) + (h^3 / 6) r'''(t) + ...",
                    "Compute the cross product r'(t) x (r(t + h) - r(t))."
                ],
                "solution": r"""### 1. Normal Vector to the Secant Plane $\Pi(h)$
The plane $\Pi(h)$ contains the point $\mathbf{r}(t)$, the direction vector of the tangent line $\mathbf{r}'(t)$, and the neighboring point $\mathbf{r}(t + h)$.
Hence, two vectors lying parallel to $\Pi(h)$ are:
$$\mathbf{v}_1 = \mathbf{r}'(t) \quad \text{and} \quad \mathbf{v}_2(h) = \mathbf{r}(t + h) - \mathbf{r}(t)$$
A normal vector to $\Pi(h)$ is given by their cross product:
$$\mathbf{n}(h) = \mathbf{r}'(t) \times (\mathbf{r}(t + h) - \mathbf{r}(t))$$

---

### 2. Limiting Position as $h \to 0$
Expanding $\mathbf{r}(t + h)$ in a Taylor series about $t$:
$$\mathbf{r}(t + h) - \mathbf{r}(t) = h \mathbf{r}'(t) + \frac{h^2}{2} \mathbf{r}''(t) + \frac{h^3}{6} \mathbf{r}'''(t) + O(h^4)$$
Substituting this into $\mathbf{n}(h)$:
$$\begin{aligned}
\mathbf{n}(h) &= \mathbf{r}'(t) \times \left( h \mathbf{r}'(t) + \frac{h^2}{2} \mathbf{r}''(t) + \frac{h^3}{6} \mathbf{r}'''(t) + O(h^4) \right) \\
&= h (\mathbf{r}'(t) \times \mathbf{r}'(t)) + \frac{h^2}{2} (\mathbf{r}'(t) \times \mathbf{r}''(t)) + \frac{h^3}{6} (\mathbf{r}'(t) \times \mathbf{r}'''(t)) + O(h^4)
\end{aligned}$$
Since $\mathbf{r}'(t) \times \mathbf{r}'(t) = \mathbf{0}$:
$$\mathbf{n}(h) = \frac{h^2}{2} (\mathbf{r}'(t) \times \mathbf{r}''(t)) + \frac{h^3}{6} (\mathbf{r}'(t) \times \mathbf{r}'''(t)) + O(h^4)$$
Dividing by $\frac{h^2}{2}$:
$$\lim_{h \to 0} \frac{\mathbf{n}(h)}{h^2/2} = \mathbf{r}'(t) \times \mathbf{r}''(t)$$
Since the orientation of a plane is determined by the direction of its normal, the limiting normal to $\Pi(h)$ as $h \to 0$ is precisely:
$$\mathbf{n}_0 = \mathbf{r}'(t) \times \mathbf{r}''(t)$$
The limiting plane equation through $\mathbf{r}(t)$ is therefore:
$$(\mathbf{X} - \mathbf{r}(t)) \cdot (\mathbf{r}'(t) \times \mathbf{r}''(t)) = 0 \iff [\mathbf{X} - \mathbf{r}(t), \mathbf{r}'(t), \mathbf{r}''(t)] = 0 \quad \blacksquare$$

---

### 3. Contact Order and Distance Estimate
The distance from $\mathbf{r}(t + h)$ to the osculating plane is:
$$d(h) = \frac{|(\mathbf{r}(t + h) - \mathbf{r}(t)) \cdot (\mathbf{r}'(t) \times \mathbf{r}''(t))|}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}$$
Substituting the Taylor expansion:
$$\mathbf{r}(t + h) - \mathbf{r}(t) = h \mathbf{r}'(t) + \frac{h^2}{2} \mathbf{r}''(t) + \frac{h^3}{6} \mathbf{r}'''(t) + O(h^4)$$
Taking the dot product with $\mathbf{r}'(t) \times \mathbf{r}''(t)$:
- $h \mathbf{r}'(t) \cdot (\mathbf{r}'(t) \times \mathbf{r}''(t)) = 0$.
- $\frac{h^2}{2} \mathbf{r}''(t) \cdot (\mathbf{r}'(t) \times \mathbf{r}''(t)) = 0$.
- The first non-zero term is the cubic term:
$$(\mathbf{r}(t + h) - \mathbf{r}(t)) \cdot (\mathbf{r}'(t) \times \mathbf{r}''(t)) = \frac{h^3}{6} [\mathbf{r}'''(t), \mathbf{r}'(t), \mathbf{r}''(t)] + O(h^4)$$
Therefore:
$$d(h) = \frac{|[\mathbf{r}'(t), \mathbf{r}''(t), \mathbf{r}'''(t)]|}{6 \|\mathbf{r}'(t) \times \mathbf{r}''(t)\|} h^3 + O(h^4) = O(h^3)$$
Since $d(h) / h^2 \to 0$ as $h \to 0$, the osculating plane has contact of order at least 2 with the curve. $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 1.3",
                "title": "Straight Line Characterization Theorem via Collinear Velocity & Acceleration",
                "statement": r"""Prove the fundamental characterization theorem of straight lines in Euclidean 3-space:
Let $\mathbf{r}: I \to \mathbb{R}^3$ be a regular $C^2$ curve on an open interval $I$.
1. Prove that $\mathbf{r}(I)$ is a segment of a straight line if and only if:
   $$\mathbf{r}''(t) \times \mathbf{r}'(t) = \mathbf{0} \quad \forall t \in I$$
2. Show that if the condition holds, there exists a scalar function $\lambda(t)$ such that $\mathbf{r}''(t) = \lambda(t) \mathbf{r}'(t)$, and solve this differential equation explicitly to prove $\mathbf{r}(t) = \mathbf{r}_0 + \mu(t) \mathbf{v}_0$ for constant vectors $\mathbf{r}_0, \mathbf{v}_0 \in \mathbb{R}^3$.""",
                "hints": [
                    "If the trace is a line, r(t) = r_0 + f(t) v_0. Differentiate twice to check cross product.",
                    "Conversely, if r''(t) x r'(t) = 0, differentiate the unit tangent vector T(t) = r'(t) / ||r'(t)||."
                ],
                "solution": r"""### 1. Forward Direction: Straight Line $\implies \mathbf{r}''(t) \times \mathbf{r}'(t) = \mathbf{0}$
Suppose $\mathbf{r}(I)$ is a straight line.
Then $\mathbf{r}(t)$ can be represented as:
$$\mathbf{r}(t) = \mathbf{r}_0 + f(t) \mathbf{v}_0$$
where $\mathbf{r}_0 \in \mathbb{R}^3$ is a fixed point, $\mathbf{v}_0 \in \mathbb{R}^3 \setminus \{\mathbf{0}\}$ is a constant direction vector, and $f: I \to \mathbb{R}$ is a $C^2$ function.
Differentiating with respect to $t$:
$$\mathbf{r}'(t) = f'(t) \mathbf{v}_0$$
Since $\mathbf{r}$ is regular, $f'(t) \ne 0$ for all $t \in I$.
Differentiating a second time:
$$\mathbf{r}''(t) = f''(t) \mathbf{v}_0$$
Computing the cross product:
$$\mathbf{r}''(t) \times \mathbf{r}'(t) = (f''(t) \mathbf{v}_0) \times (f'(t) \mathbf{v}_0) = f''(t) f'(t) (\mathbf{v}_0 \times \mathbf{v}_0) = f''(t) f'(t) \mathbf{0} = \mathbf{0} \quad \blacksquare$$

---

### 2. Reverse Direction: $\mathbf{r}''(t) \times \mathbf{r}'(t) = \mathbf{0} \implies$ Straight Line

Assume $\mathbf{r}''(t) \times \mathbf{r}'(t) = \mathbf{0}$ for all $t \in I$.
Since $\mathbf{r}$ is regular, $\mathbf{r}'(t) \ne \mathbf{0}$ everywhere.
Recall that the cross product of two vectors in $\mathbb{R}^3$ vanishes if and only if they are linearly dependent (collinear).
Thus, for each $t \in I$, there exists a scalar $\lambda(t) \in \mathbb{R}$ such that:
$$\mathbf{r}''(t) = \lambda(t) \mathbf{r}'(t)$$

Now consider the unit tangent vector $\mathbf{T}(t)$:
$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$$
We compute the derivative of $\mathbf{T}(t)$ with respect to $t$ using the quotient rule:
$$\frac{d\mathbf{T}}{dt} = \frac{\mathbf{r}''(t) \|\mathbf{r}'(t)\| - \mathbf{r}'(t) \frac{d}{dt}\|\mathbf{r}'(t)\|}{\|\mathbf{r}'(t)\|^2}$$
Recall that $\frac{d}{dt}\|\mathbf{r}'(t)\| = \frac{\mathbf{r}'(t) \cdot \mathbf{r}''(t)}{\|\mathbf{r}'(t)\|}$.
Substituting $\mathbf{r}''(t) = \lambda(t) \mathbf{r}'(t)$:
$$\mathbf{r}'(t) \cdot \mathbf{r}''(t) = \mathbf{r}'(t) \cdot (\lambda(t) \mathbf{r}'(t)) = \lambda(t) \|\mathbf{r}'(t)\|^2$$
So:
$$\frac{d}{dt}\|\mathbf{r}'(t)\| = \frac{\lambda(t) \|\mathbf{r}'(t)\|^2}{\|\mathbf{r}'(t)\|} = \lambda(t) \|\mathbf{r}'(t)\|$$
Now substitute this back into the derivative of $\mathbf{T}$:
$$\frac{d\mathbf{T}}{dt} = \frac{(\lambda(t) \mathbf{r}'(t)) \|\mathbf{r}'(t)\| - \mathbf{r}'(t) (\lambda(t) \|\mathbf{r}'(t)\|)}{\|\mathbf{r}'(t)\|^2} = \frac{\mathbf{0}}{\|\mathbf{r}'(t)\|^2} = \mathbf{0}$$
Since $\frac{d\mathbf{T}}{dt} = \mathbf{0}$ on the connected interval $I$, the unit tangent vector is **constant**:
$$\mathbf{T}(t) = \mathbf{T}_0 \quad \text{for some constant vector } \mathbf{T}_0 \in \mathbb{R}^3, \; \|\mathbf{T}_0\| = 1$$

Since $\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$, we have:
$$\mathbf{r}'(t) = \|\mathbf{r}'(t)\| \mathbf{T}_0$$
Let $v(t) = \|\mathbf{r}'(t)\| > 0$. Integrating from an initial parameter $t_0$:
$$\mathbf{r}(t) - \mathbf{r}(t_0) = \int_{t_0}^t \mathbf{r}'(u) \, du = \left( \int_{t_0}^t v(u) \, du \right) \mathbf{T}_0$$
Defining $\mathbf{r}_0 = \mathbf{r}(t_0)$ and the scalar function $\mu(t) = \int_{t_0}^t v(u) \, du$:
$$\mathbf{r}(t) = \mathbf{r}_0 + \mu(t) \mathbf{T}_0$$
This is precisely the parametric equation of a straight line in $\mathbb{R}^3$! $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u = get_unit1()
    print(f"Loaded Unit 1: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
