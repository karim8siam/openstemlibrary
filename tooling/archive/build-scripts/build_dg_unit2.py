# -*- coding: utf-8 -*-
"""
build_dg_unit2.py
Constructs Unit 2: The Frenet-Serret Apparatus: Curvature, Torsion & The Moving Trihedron
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "The Frenet-Serret Apparatus: Curvature, Torsion & The Moving Trihedron",
        "leadSummary": "Comprehensive theory of the Frenet-Serret apparatus: the orthonormal moving trihedron {T, N, B}, the three fundamental planes (osculating, normal, rectifying), geometric definitions of curvature kappa and torsion tau, formulas for arbitrary parameters, the complete line-by-line derivation of the Frenet-Serret equations, the Darboux rotation vector, and the Fundamental Theorem of Space Curves.",
        "simulations": ["sim_dg_frenet_frame"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "The Principal Normal, Binormal & The Frenet Moving Trihedron",
                "content": r"""### 1. Construction of the Moving Orthonormal Frame

Let $\mathbf{r}: I \to \mathbb{R}^3$ be a regular $C^3$ space curve parametrized by arc-length $s$.
By definition, the unit tangent vector is:
$$\mathbf{T}(s) = \mathbf{r}'(s) = \frac{d\mathbf{r}}{ds}$$
Since $\mathbf{T}(s)$ has constant unit length for all $s$:
$$\langle \mathbf{T}(s), \mathbf{T}(s) \rangle = \|\mathbf{T}(s)\|^2 = 1$$
Differentiating both sides with respect to arc-length $s$ using the product rule:
$$\frac{d}{ds} \langle \mathbf{T}(s), \mathbf{T}(s) \rangle = 2 \left\langle \frac{d\mathbf{T}}{ds}, \mathbf{T}(s) \right\rangle = 0 \implies \mathbf{T}'(s) \perp \mathbf{T}(s)$$
The derivative vector $\mathbf{T}'(s)$ is strictly orthogonal to $\mathbf{T}(s)$ at every point where it is non-zero!

---

### 2. The Principal Normal Vector $\mathbf{N}$

> **Definition 2.1 (Curvature and Principal Normal):**
> Let $s$ be a point where $\mathbf{T}'(s) \ne \mathbf{0}$.
> 1. The **curvature** $\kappa(s)$ of the curve is the magnitude of the rate of change of the unit tangent vector:
>    $$\kappa(s) = \|\mathbf{T}'(s)\| = \left\| \frac{d^2\mathbf{r}}{ds^2} \right\| > 0$$
>    The reciprocal $\rho(s) = \frac{1}{\kappa(s)}$ is the **radius of curvature**.
> 2. The **principal normal vector** $\mathbf{N}(s)$ is the unit vector pointing in the direction of $\mathbf{T}'(s)$:
>    $$\mathbf{N}(s) = \frac{\mathbf{T}'(s)}{\|\mathbf{T}'(s)\|} = \frac{1}{\kappa(s)} \mathbf{T}'(s) \iff \mathbf{T}'(s) = \kappa(s) \mathbf{N}(s)$$

---

### 3. The Binormal Vector $\mathbf{B}$ and the Frenet Trihedron

> **Definition 2.2 (Binormal Vector $\mathbf{B}$):**
> The **binormal vector** $\mathbf{B}(s)$ is defined as the cross product of the unit tangent and principal normal vectors:
> $$\mathbf{B}(s) = \mathbf{T}(s) \times \mathbf{N}(s)$$

> **Theorem 2.1 (The Frenet Moving Trihedron):**
> The ordered set of vectors $\{\mathbf{T}(s), \mathbf{N}(s), \mathbf{B}(s)\}$ forms a right-handed orthonormal basis of $\mathbb{R}^3$ at each point of the curve where $\kappa(s) > 0$:
> $$\|\mathbf{T}\| = \|\mathbf{N}\| = \|\mathbf{B}\| = 1$$
> $$\mathbf{T} \cdot \mathbf{N} = \mathbf{N} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{T} = 0$$
> $$\mathbf{T} \times \mathbf{N} = \mathbf{B}, \quad \mathbf{N} \times \mathbf{B} = \mathbf{T}, \quad \mathbf{B} \times \mathbf{T} = \mathbf{N}$$
> This moving orthonormal coordinate frame is called the **Frenet-Serret Moving Trihedron**."""
            },
            {
                "secNumber": "2.2",
                "title": "The Three Fundamental Planes of Curve Theory",
                "content": r"""### 1. Geometric Definition of the Fundamental Planes

At every point $\mathbf{r}(s)$ of a regular curve with $\kappa(s) > 0$, the Frenet trihedron $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ defines three mutually perpendicular coordinate planes.

> **Definition 2.3 (The Three Fundamental Planes):**
> Let $\mathbf{X} = (X, Y, Z)$ denote an arbitrary point in space.
> 1. **Osculating Plane (Plane of Curvature):**
>    The plane spanned by the tangent $\mathbf{T}$ and principal normal $\mathbf{N}$.
>    Its normal vector is the binormal $\mathbf{B}$.
>    $$\mathbf{B}(s) \cdot (\mathbf{X} - \mathbf{r}(s)) = 0$$
> 2. **Normal Plane:**
>    The plane spanned by the principal normal $\mathbf{N}$ and binormal $\mathbf{B}$.
>    Its normal vector is the unit tangent $\mathbf{T}$.
>    $$\mathbf{T}(s) \cdot (\mathbf{X} - \mathbf{r}(s)) = 0$$
> 3. **Rectifying Plane:**
>    The plane spanned by the unit tangent $\mathbf{T}$ and binormal $\mathbf{B}$.
>    Its normal vector is the principal normal $\mathbf{N}$.
>    $$\mathbf{N}(s) \cdot (\mathbf{X} - \mathbf{r}(s)) = 0$$

---

### 2. Physical and Geometric Roles

- **Osculating Plane:** Contains the instantaneous velocity and acceleration vectors ($\mathbf{r}' = \mathbf{T}$, $\mathbf{r}'' = \kappa \mathbf{N}$). Any planar curve lies entirely within its osculating plane.
- **Normal Plane:** Contains all lines passing through $\mathbf{r}(s)$ perpendicular to the curve's direction of motion. The circle of curvature (osculating circle) intersects this plane perpendicularly.
- **Rectifying Plane:** The plane along which the curve can be "unrolled" or rectified. If a curve is a geodesic on a developable surface, the surface is the envelope of the curve's rectifying planes."""
            },
            {
                "secNumber": "2.3",
                "title": "Curvature, Torsion & Arbitrary Parametrization Formulas",
                "content": r"""### 1. Geometric Definition and Interpretation of Torsion

Just as curvature $\kappa$ measures the rate at which the curve turns away from its tangent line, **torsion** $\tau$ measures the rate at which the curve twists out of its osculating plane.

> **Definition 2.4 (Torsion):**
> Since $\mathbf{B}(s)$ is a unit vector, $\mathbf{B}'(s) \perp \mathbf{B}(s)$.
> Furthermore, since $\mathbf{B} = \mathbf{T} \times \mathbf{N}$, differentiating gives:
> $$\mathbf{B}' = \mathbf{T}' \times \mathbf{N} + \mathbf{T} \times \mathbf{N}' = (\kappa \mathbf{N}) \times \mathbf{N} + \mathbf{T} \times \mathbf{N}' = \mathbf{0} + \mathbf{T} \times \mathbf{N}'$$
> This shows $\mathbf{B}'(s) \perp \mathbf{T}(s)$.
> Since $\mathbf{B}'$ is perpendicular to both $\mathbf{B}$ and $\mathbf{T}$, it must be collinear with $\mathbf{N}$!
> The **torsion** $\tau(s)$ is defined by:
> $$\frac{d\mathbf{B}}{ds} = -\tau(s) \mathbf{N}(s) \iff \tau(s) = -\mathbf{N}(s) \cdot \mathbf{B}'(s)$$
> The radius of torsion is $\sigma(s) = \frac{1}{\tau(s)}$.

---

### 2. Arbitrary Parametrization Formulas

In practical applications, curves are rarely parametrized by arc-length. We require formulas for $\kappa$ and $\tau$ expressed directly in terms of an arbitrary parameter $t$.

> **Theorem 2.2 (General Parameter Curvature & Torsion Formulas):**
> Let $\mathbf{r}(t)$ be a regular $C^3$ curve with arbitrary parameter $t$. Then:
> 1. **Curvature:**
>    $$\kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$$
> 2. **Torsion:**
>    $$\tau(t) = \frac{[\mathbf{r}'(t), \mathbf{r}''(t), \mathbf{r}'''(t)]}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|^2} = \frac{(\mathbf{r}'(t) \times \mathbf{r}''(t)) \cdot \mathbf{r}'''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|^2}$$
> 3. **The Frenet Vectors:**
>    $$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}, \quad \mathbf{B}(t) = \frac{\mathbf{r}'(t) \times \mathbf{r}''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}, \quad \mathbf{N}(t) = \mathbf{B}(t) \times \mathbf{T}(t)$$

#### Complete Line-by-Line Proof:
Let $s$ be arc-length, and let $v = \frac{ds}{dt} = \|\mathbf{r}'(t)\|$.
By the Chain Rule:
$$\mathbf{r}'(t) = \frac{d\mathbf{r}}{ds} \frac{ds}{dt} = v \mathbf{T}$$
Differentiating with respect to $t$:
$$\mathbf{r}''(t) = v' \mathbf{T} + v \frac{d\mathbf{T}}{dt} = v' \mathbf{T} + v \left( \frac{d\mathbf{T}}{ds} \frac{ds}{dt} \right) = v' \mathbf{T} + v^2 \kappa \mathbf{N}$$
Computing the vector cross product $\mathbf{r}'(t) \times \mathbf{r}''(t)$:
$$\mathbf{r}'(t) \times \mathbf{r}''(t) = (v \mathbf{T}) \times (v' \mathbf{T} + v^2 \kappa \mathbf{N}) = v v' (\mathbf{T} \times \mathbf{T}) + v^3 \kappa (\mathbf{T} \times \mathbf{N}) = v^3 \kappa \mathbf{B}$$
Taking the Euclidean norm of both sides (since $\|\mathbf{B}\| = 1$ and $\kappa > 0, v > 0$):
$$\|\mathbf{r}'(t) \times \mathbf{r}''(t)\| = v^3 \kappa = \|\mathbf{r}'(t)\|^3 \kappa \implies \kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$$
Next, differentiating $\mathbf{r}''(t)$ to find $\mathbf{r}'''(t)$:
$$\mathbf{r}'''(t) = \frac{d}{dt}[v' \mathbf{T} + v^2 \kappa \mathbf{N}] = v'' \mathbf{T} + v' (v \kappa \mathbf{N}) + (v^2 \kappa)' \mathbf{N} + v^2 \kappa (v \mathbf{N}') = \dots + v^3 \kappa \tau \mathbf{B}$$
Now take the dot product with $\mathbf{r}'(t) \times \mathbf{r}''(t) = v^3 \kappa \mathbf{B}$:
$$(\mathbf{r}'(t) \times \mathbf{r}''(t)) \cdot \mathbf{r}'''(t) = (v^3 \kappa \mathbf{B}) \cdot (\dots + v^3 \kappa \tau \mathbf{B}) = (v^3 \kappa)^2 \tau = \|\mathbf{r}'(t) \times \mathbf{r}''(t)\|^2 \tau$$
Solving for $\tau$ yields:
$$\tau(t) = \frac{[\mathbf{r}'(t), \mathbf{r}''(t), \mathbf{r}'''(t)]}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|^2} \quad \blacksquare$$"""
            },
            {
                "secNumber": "2.4",
                "title": "The Frenet-Serret Formulas & The Darboux Vector",
                "content": r"""### 1. The Frenet-Serret Formulas

The fundamental differential equations governing space curves were discovered independently by Jean Frédéric Frenet (1847) and Joseph Alfred Serret (1851).

> **Theorem 2.3 (The Frenet-Serret Equations):**
> Let $\mathbf{r}(s)$ be an arc-length parametrized $C^3$ curve with curvature $\kappa(s) > 0$ and torsion $\tau(s)$.
> The derivatives of the moving orthonormal frame $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ with respect to arc-length satisfy:
> $$\begin{aligned}
> \frac{d\mathbf{T}}{ds} &= \kappa \mathbf{N} \\
> \frac{d\mathbf{N}}{ds} &= -\kappa \mathbf{T} + \tau \mathbf{B} \\
> \frac{d\mathbf{B}}{ds} &= -\tau \mathbf{N}
> \end{aligned}$$
> In matrix notation:
> $$\frac{d}{ds} \begin{pmatrix} \mathbf{T} \\ \mathbf{N} \\ \mathbf{B} \end{pmatrix} = \begin{pmatrix}
> 0 & \kappa & 0 \\
> -\kappa & 0 & \tau \\
> 0 & -\tau & 0
> \end{pmatrix} \begin{pmatrix} \mathbf{T} \\ \mathbf{N} \\ \mathbf{B} \end{pmatrix}$$
> Notice that the coefficient matrix is **skew-symmetric** ($A^T = -A$), reflecting the fact that the frame remains orthonormal at all times.

#### Complete Line-by-Line Proof:
1. **First equation $\mathbf{T}' = \kappa \mathbf{N}$:**
   This holds by Definition 2.1 of curvature $\kappa$ and principal normal $\mathbf{N}$.
2. **Third equation $\mathbf{B}' = -\tau \mathbf{N}$:**
   This holds by Definition 2.4 of torsion $\tau$.
3. **Second equation $\mathbf{N}' = -\kappa \mathbf{T} + \tau \mathbf{B}$:**
   Since $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ is an orthonormal basis, we can express $\mathbf{N}'$ as a linear combination:
   $$\mathbf{N}' = c_1 \mathbf{T} + c_2 \mathbf{N} + c_3 \mathbf{B}$$
   where $c_1 = \mathbf{N}' \cdot \mathbf{T}$, $c_2 = \mathbf{N}' \cdot \mathbf{N}$, and $c_3 = \mathbf{N}' \cdot \mathbf{B}$.
   - Differentiating $\mathbf{N} \cdot \mathbf{N} = 1$:
     $$2 (\mathbf{N}' \cdot \mathbf{N}) = 0 \implies c_2 = 0$$
   - Differentiating $\mathbf{N} \cdot \mathbf{T} = 0$:
     $$\mathbf{N}' \cdot \mathbf{T} + \mathbf{N} \cdot \mathbf{T}' = 0 \implies c_1 = -\mathbf{N} \cdot \mathbf{T}' = -\mathbf{N} \cdot (\kappa \mathbf{N}) = -\kappa \|\mathbf{N}\|^2 = -\kappa$$
   - Differentiating $\mathbf{N} \cdot \mathbf{B} = 0$:
     $$\mathbf{N}' \cdot \mathbf{B} + \mathbf{N} \cdot \mathbf{B}' = 0 \implies c_3 = -\mathbf{N} \cdot \mathbf{B}' = -\mathbf{N} \cdot (-\tau \mathbf{N}) = \tau \|\mathbf{N}\|^2 = \tau$$
   Substituting $c_1, c_2, c_3$ gives:
   $$\mathbf{N}' = -\kappa \mathbf{T} + \tau \mathbf{B} \quad \blacksquare$$

---

### 2. The Darboux Rotation Vector

Jean Gaston Darboux observed that the Frenet-Serret equations can be unified into a single kinematic angular velocity equation:

> **Definition 2.5 (Darboux Vector):**
> The **Darboux vector** (or angular velocity vector of the frame) is:
> $$\boldsymbol{\omega}(s) = \tau(s) \mathbf{T}(s) + \kappa(s) \mathbf{B}(s)$$

> **Theorem 2.4 (Darboux Kinematic Law):**
> For each vector $\mathbf{F} \in \{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$, the rate of change is given by:
> $$\frac{d\mathbf{F}}{ds} = \boldsymbol{\omega} \times \mathbf{F}$$
> 
> *Proof:*
> - $\boldsymbol{\omega} \times \mathbf{T} = (\tau \mathbf{T} + \kappa \mathbf{B}) \times \mathbf{T} = \tau(\mathbf{T} \times \mathbf{T}) + \kappa(\mathbf{B} \times \mathbf{T}) = \mathbf{0} + \kappa \mathbf{N} = \frac{d\mathbf{T}}{ds}$.
> - $\boldsymbol{\omega} \times \mathbf{N} = (\tau \mathbf{T} + \kappa \mathbf{B}) \times \mathbf{N} = \tau(\mathbf{T} \times \mathbf{N}) + \kappa(\mathbf{B} \times \mathbf{N}) = \tau \mathbf{B} - \kappa \mathbf{T} = \frac{d\mathbf{N}}{ds}$.
> - $\boldsymbol{\omega} \times \mathbf{B} = (\tau \mathbf{T} + \kappa \mathbf{B}) \times \mathbf{B} = \tau(\mathbf{T} \times \mathbf{B}) + \kappa(\mathbf{B} \times \mathbf{B}) = -\tau \mathbf{N} + \mathbf{0} = \frac{d\mathbf{B}}{ds}$. $\blacksquare$"""
            },
            {
                "secNumber": "2.5",
                "title": "The Fundamental Theorem of Space Curves",
                "content": r"""### 1. The Natural / Intrinsic Equations of a Curve

A remarkable consequence of the Frenet apparatus is that curvature $\kappa(s)$ and torsion $\tau(s)$ contain **complete geometric information** about the curve. The equations $\kappa = \kappa(s)$ and $\tau = \tau(s)$ are called the **natural equations** (or intrinsic equations) of the curve.

---

### 2. Statement of the Fundamental Theorem

> **Theorem 2.5 (Fundamental Theorem of Space Curves / Bonnet's Theorem):**
> Let $I \subseteq \mathbb{R}$ be an interval containing $s_0$.
> Let $\kappa: I \to \mathbb{R}$ and $\tau: I \to \mathbb{R}$ be continuous functions such that $\kappa(s) > 0$ for all $s \in I$.
> 1. **Existence:** There exists a $C^3$ curve $\mathbf{r}: I \to \mathbb{R}^3$ parametrized by arc-length $s$ whose curvature is $\kappa(s)$ and whose torsion is $\tau(s)$.
> 2. **Uniqueness:** If $\tilde{\mathbf{r}}: I \to \mathbb{R}^3$ is another curve with the same curvature $\kappa(s)$ and torsion $\tau(s)$, then $\tilde{\mathbf{r}}$ differs from $\mathbf{r}$ by at most a **rigid motion of Euclidean space** (a translation and a rotation in $\mathrm{SO}(3)$).

#### Proof Outline (Linear ODE Systems):
1. **Solve for the frame:** The Frenet-Serret system $\frac{d\mathbf{F}}{ds} = A(s)\mathbf{F}$ is a linear homogeneous system of ODEs with skew-symmetric coefficient matrix $A(s)$. By the Picard-Lindelöf theorem, given an initial orthonormal frame $\{\mathbf{T}_0, \mathbf{N}_0, \mathbf{B}_0\}$ at $s_0$, there exists a unique solution $\{\mathbf{T}(s), \mathbf{N}(s), \mathbf{B}(s)\}$ on $I$. Because $A(s)$ is skew-symmetric, the frame remains orthonormal for all $s$.
2. **Integrate for the curve:** Define $\mathbf{r}(s) = \mathbf{r}_0 + \int_{s_0}^s \mathbf{T}(u) \, du$.
   Then $\mathbf{r}'(s) = \mathbf{T}(s)$, $\|\mathbf{r}'(s)\| = 1$, and its curvature and torsion match $\kappa(s)$ and $\tau(s)$.
3. **Uniqueness:** If two curves have identical $\kappa(s)$ and $\tau(s)$, apply a rotation to align their initial frames at $s_0$, and a translation to align their initial positions. By uniqueness of solutions to linear ODEs, the two curves must coincide everywhere on $I$. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 2.1",
                "title": "Complete Frenet Apparatus Computation for the Circular Helix",
                "statement": r"""Consider the standard circular helix with radius $a > 0$ and pitch parameter $b > 0$:
$$\mathbf{r}(t) = \begin{pmatrix} a \cos t \\ a \sin t \\ b t \end{pmatrix}, \quad t \in \mathbb{R}$$
1. Find the speed $v = \|\mathbf{r}'(t)\|$ and the arc-length function $s(t)$ measured from $t_0 = 0$.
2. Compute the unit tangent vector $\mathbf{T}$, principal normal vector $\mathbf{N}$, and binormal vector $\mathbf{B}$ as functions of $t$.
3. Compute the curvature $\kappa(t)$ and torsion $\tau(t)$. Show that both are constants and find their ratio $\tau / \kappa$.""",
                "hints": [
                    "Speed is sqrt(a^2 sin^2 t + a^2 cos^2 t + b^2) = sqrt(a^2 + b^2).",
                    "Differentiate T with respect to s or use arbitrary parameter formulas.",
                    "Recall B = T x N and tau = -N . B' / v."
                ],
                "solution": r"""### 1. Speed and Arc-Length Computation
Differentiating $\mathbf{r}(t)$:
$$\mathbf{r}'(t) = \begin{pmatrix} -a \sin t \\ a \cos t \\ b \end{pmatrix}$$
The speed is:
$$v = \|\mathbf{r}'(t)\| = \sqrt{(-a \sin t)^2 + (a \cos t)^2 + b^2} = \sqrt{a^2(\sin^2 t + \cos^2 t) + b^2} = \sqrt{a^2 + b^2}$$
Let $c = \sqrt{a^2 + b^2} > 0$. The speed is constant $v = c$.
The arc-length function from $t_0 = 0$ is:
$$s(t) = \int_0^t c \, du = c t \iff t = \frac{s}{c}$$

---

### 2. Frenet Moving Trihedron $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$
- **Unit Tangent Vector $\mathbf{T}$:**
  $$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|} = \frac{1}{c} \begin{pmatrix} -a \sin t \\ a \cos t \\ b \end{pmatrix}$$

- **Principal Normal Vector $\mathbf{N}$:**
  Differentiating $\mathbf{T}$ with respect to arc-length $s$:
  $$\frac{d\mathbf{T}}{ds} = \frac{d\mathbf{T}}{dt} \frac{dt}{ds} = \frac{1}{c} \frac{d}{dt} \left[ \frac{1}{c} \begin{pmatrix} -a \sin t \\ a \cos t \\ b \end{pmatrix} \right] = \frac{1}{c^2} \begin{pmatrix} -a \cos t \\ -a \sin t \\ 0 \end{pmatrix} = -\frac{a}{c^2} \begin{pmatrix} \cos t \\ \sin t \\ 0 \end{pmatrix}$$
  The curvature is the norm:
  $$\kappa = \left\| \frac{d\mathbf{T}}{ds} \right\| = \frac{a}{c^2} \sqrt{\cos^2 t + \sin^2 t} = \frac{a}{c^2} = \frac{a}{a^2 + b^2}$$
  The principal normal vector is:
  $$\mathbf{N} = \frac{1}{\kappa} \frac{d\mathbf{T}}{ds} = \begin{pmatrix} -\cos t \\ -\sin t \\ 0 \end{pmatrix}$$

- **Binormal Vector $\mathbf{B}$:**
  $$\mathbf{B} = \mathbf{T} \times \mathbf{N} = \frac{1}{c} \begin{vmatrix}
  \mathbf{i} & \mathbf{j} & \mathbf{k} \\
  -a \sin t & a \cos t & b \\
  -\cos t & -\sin t & 0
  \end{vmatrix} = \frac{1}{c} \begin{pmatrix} b \sin t \\ -b \cos t \\ a \sin^2 t + a \cos^2 t \end{pmatrix} = \frac{1}{c} \begin{pmatrix} b \sin t \\ -b \cos t \\ a \end{pmatrix}$$

---

### 3. Torsion and Ratio $\tau / \kappa$
Differentiating $\mathbf{B}$ with respect to $s$:
$$\frac{d\mathbf{B}}{ds} = \frac{1}{c} \frac{d\mathbf{B}}{dt} = \frac{1}{c} \cdot \frac{1}{c} \begin{pmatrix} b \cos t \\ b \sin t \\ 0 \end{pmatrix} = \frac{b}{c^2} \begin{pmatrix} \cos t \\ \sin t \\ 0 \end{pmatrix} = -\frac{b}{c^2} \mathbf{N}$$
Comparing with the Frenet formula $\frac{d\mathbf{B}}{ds} = -\tau \mathbf{N}$:
$$\tau = \frac{b}{c^2} = \frac{b}{a^2 + b^2}$$
Both $\kappa$ and $\tau$ are **strictly constant**.
Their ratio is:
$$\frac{\tau}{\kappa} = \frac{b / (a^2 + b^2)}{a / (a^2 + b^2)} = \frac{b}{a} = \text{constant} \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced / Problem 2.2",
                "title": "Complete Rigorous Proof of the Planar Curve Criterion (tau = 0)",
                "statement": r"""Let $\mathbf{r}: I \to \mathbb{R}^3$ be a regular $C^3$ curve parametrized by arc-length $s$ with $\kappa(s) > 0$ for all $s \in I$.
1. Prove that if $\mathbf{r}(I)$ lies in a fixed plane $\Pi \subset \mathbb{R}^3$, then its torsion $\tau(s) \equiv 0$ everywhere on $I$.
2. Conversely, prove that if $\tau(s) \equiv 0$ for all $s \in I$, then the curve lies entirely in a fixed plane.
3. Explicitly construct the equation of this plane in terms of the initial point $\mathbf{r}(s_0)$ and binormal $\mathbf{B}(s_0)$.""",
                "hints": [
                    "A plane has equation n . (r(s) - r_0) = 0 for constant unit vector n.",
                    "Differentiate repeatedly with respect to s to relate n to T, N, B.",
                    "For the converse, show B'(s) = -tau N = 0 implies B(s) is a constant vector B_0."
                ],
                "solution": r"""### 1. Forward Direction: Curve Lies in a Plane $\implies \tau(s) \equiv 0$
Assume $\mathbf{r}(I)$ lies in a fixed plane $\Pi$.
The equation of $\Pi$ is:
$$\mathbf{n}_0 \cdot (\mathbf{r}(s) - \mathbf{r}_0) = 0 \quad \forall s \in I$$
where $\mathbf{n}_0$ is a fixed constant unit normal vector ($\|\mathbf{n}_0\| = 1$), and $\mathbf{r}_0 \in \Pi$.
- Differentiating once with respect to $s$:
  $$\mathbf{n}_0 \cdot \mathbf{r}'(s) = 0 \iff \mathbf{n}_0 \cdot \mathbf{T}(s) = 0$$
  Thus, $\mathbf{n}_0$ is perpendicular to $\mathbf{T}(s)$ for all $s$.
- Differentiating a second time with respect to $s$:
  $$\mathbf{n}_0 \cdot \mathbf{T}'(s) = 0 \iff \mathbf{n}_0 \cdot (\kappa(s) \mathbf{N}(s)) = 0$$
  Since $\kappa(s) > 0$, dividing by $\kappa(s)$ gives:
  $$\mathbf{n}_0 \cdot \mathbf{N}(s) = 0$$
Since $\mathbf{n}_0$ is a unit vector orthogonal to both $\mathbf{T}(s)$ and $\mathbf{N}(s)$, and $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ is an orthonormal basis, $\mathbf{n}_0$ must be parallel to $\mathbf{B}(s)$:
$$\mathbf{B}(s) = \pm \mathbf{n}_0 \quad \text{for all } s \in I$$
Since $\mathbf{n}_0$ is constant, $\mathbf{B}(s)$ is a **constant vector**:
$$\frac{d\mathbf{B}}{ds} = \mathbf{0}$$
By the third Frenet-Serret formula:
$$\frac{d\mathbf{B}}{ds} = -\tau(s) \mathbf{N}(s) = \mathbf{0}$$
Since $\|\mathbf{N}(s)\| = 1 \ne 0$, we must have:
$$\tau(s) \equiv 0 \quad \forall s \in I \quad \blacksquare$$

---

### 2. Reverse Direction: $\tau(s) \equiv 0 \implies$ Curve Lies in a Plane
Assume $\tau(s) \equiv 0$ for all $s \in I$.
By the third Frenet formula:
$$\frac{d\mathbf{B}}{ds} = -\tau(s) \mathbf{N}(s) = -0 \cdot \mathbf{N}(s) = \mathbf{0}$$
Since $\frac{d\mathbf{B}}{ds} = \mathbf{0}$ on the connected interval $I$, the binormal vector is **constant**:
$$\mathbf{B}(s) = \mathbf{B}_0 \quad \forall s \in I$$
Now fix a point $s_0 \in I$ and consider the scalar function:
$$f(s) = \mathbf{B}_0 \cdot (\mathbf{r}(s) - \mathbf{r}(s_0))$$
Notice that:
- At $s = s_0$: $f(s_0) = \mathbf{B}_0 \cdot \mathbf{0} = 0$.
- Differentiating with respect to $s$:
  $$f'(s) = \mathbf{B}_0 \cdot \mathbf{r}'(s) = \mathbf{B}(s) \cdot \mathbf{T}(s) = 0$$
  since the binormal and tangent vectors of the Frenet frame are strictly orthogonal.
Since $f'(s) = 0$ everywhere on $I$ and $f(s_0) = 0$, $f(s)$ is identically zero for all $s \in I$:
$$f(s) = \mathbf{B}_0 \cdot (\mathbf{r}(s) - \mathbf{r}(s_0)) \equiv 0 \quad \forall s \in I$$
This is precisely the equation of a plane passing through $\mathbf{r}(s_0)$ with normal vector $\mathbf{B}_0$.
Therefore, the curve lies entirely within this fixed plane! $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 2.3",
                "title": "Picard-Lindelöf Proof of the Fundamental Theorem of Space Curves",
                "statement": r"""Provide a complete, rigorous proof of the Fundamental Theorem of Space Curves (Theorem 2.5):
1. Formulate the Frenet-Serret equations as a first-order system of linear ordinary differential equations $\frac{d\Phi}{ds} = A(s)\Phi(s)$ for the $3 \times 3$ matrix $\Phi(s) = [\mathbf{T}(s), \mathbf{N}(s), \mathbf{B}(s)]^T$.
2. Prove that the matrix $A(s)$ is skew-symmetric, and deduce that any solution with orthonormal initial conditions $\Phi(s_0) \in \mathrm{SO}(3)$ remains in $\mathrm{SO}(3)$ for all $s \in I$.
3. Prove that two curves with identical curvature $\kappa(s)$ and torsion $\tau(s)$ differ by at most a rigid Euclidean transformation $\mathbf{r}_2(s) = R \mathbf{r}_1(s) + \mathbf{r}_0$ where $R \in \mathrm{SO}(3)$.""",
                "hints": [
                    "Compute the derivative of the Grammian matrix G(s) = Phi(s) Phi(s)^T.",
                    "Show d/ds [Phi Phi^T] = A Phi Phi^T + Phi Phi^T A^T = A + A^T = 0.",
                    "Apply the Picard-Lindelöf theorem for linear ODE systems."
                ],
                "solution": r"""### 1. Matrix Formulation of the Frenet System
Let $\mathbf{T}, \mathbf{N}, \mathbf{B}$ be arranged as the rows of a $3 \times 3$ matrix:
$$\Phi(s) = \begin{pmatrix} \mathbf{T}(s)^T \\ \mathbf{N}(s)^T \\ \mathbf{B}(s)^T \end{pmatrix}$$
The Frenet-Serret equations can be written compactly as:
$$\frac{d\Phi}{ds} = A(s) \Phi(s)$$
where the $3 \times 3$ coefficient matrix $A(s)$ is:
$$A(s) = \begin{pmatrix}
0 & \kappa(s) & 0 \\
-\kappa(s) & 0 & \tau(s) \\
0 & -\tau(s) & 0
\end{pmatrix}$$
Since $\kappa(s)$ and $\tau(s)$ are continuous on $I$, the matrix-valued function $A(s)$ is continuous on $I$.
By the Picard-Lindelöf Theorem for linear differential equations, given any initial condition $\Phi(s_0) = \Phi_0$, there exists a **unique** $C^1$ matrix solution $\Phi(s)$ defined on the entire interval $I$.

---

### 2. Preservation of Orthonormality ($\Phi(s) \in \mathrm{SO}(3)$)
Notice that the matrix $A(s)$ is **skew-symmetric**:
$$A(s)^T = \begin{pmatrix}
0 & -\kappa(s) & 0 \\
\kappa(s) & 0 & -\tau(s) \\
0 & \tau(s) & 0
\end{pmatrix} = -A(s)$$
We examine the Grammian matrix $G(s) = \Phi(s) \Phi(s)^T$.
Differentiating with respect to $s$ using the product rule:
$$\frac{d}{ds} \left( \Phi(s) \Phi(s)^T \right) = \frac{d\Phi}{ds} \Phi(s)^T + \Phi(s) \left( \frac{d\Phi}{ds} \right)^T$$
Substituting $\frac{d\Phi}{ds} = A(s) \Phi(s)$:
$$\begin{aligned}
\frac{d}{ds} \left( \Phi(s) \Phi(s)^T \right) &= (A(s) \Phi(s)) \Phi(s)^T + \Phi(s) (A(s) \Phi(s))^T \\
&= A(s) (\Phi(s) \Phi(s)^T) + \Phi(s) (\Phi(s)^T A(s)^T) \\
&= A(s) G(s) + G(s) A(s)^T
\end{aligned}$$
Suppose we choose an initial frame $\Phi(s_0) = \Phi_0 \in \mathrm{SO}(3)$, so $G(s_0) = \Phi_0 \Phi_0^T = I_3$ (the $3 \times 3$ identity matrix).
Notice that the constant function $\tilde{G}(s) \equiv I_3$ satisfies the differential equation:
$$A(s) I_3 + I_3 A(s)^T = A(s) + A(s)^T = A(s) - A(s) = 0$$
By the uniqueness theorem for linear ODEs, the unique solution satisfying $G(s_0) = I_3$ must be:
$$G(s) = \Phi(s) \Phi(s)^T = I_3 \quad \forall s \in I$$
Furthermore, since $\det(\Phi(s_0)) = 1$ and $\det(\Phi(s)) = \pm 1$ continuously, $\det(\Phi(s)) \equiv 1$ for all $s \in I$.
Therefore, $\Phi(s) \in \mathrm{SO}(3)$ for all $s \in I$.
This guarantees that $\{\mathbf{T}(s), \mathbf{N}(s), \mathbf{B}(s)\}$ remains a valid right-handed orthonormal frame throughout $I$!

---

### 3. Proof of Uniqueness up to Euclidean Rigid Motion
Let $\mathbf{r}_1(s)$ and $\mathbf{r}_2(s)$ be two unit-speed curves with identical curvature $\kappa(s)$ and torsion $\tau(s)$.
Let their Frenet frames be $\Phi_1(s)$ and $\Phi_2(s)$.
At the initial point $s_0$, $\Phi_1(s_0), \Phi_2(s_0) \in \mathrm{SO}(3)$.
Define the rotation matrix:
$$R = \Phi_2(s_0)^T \Phi_1(s_0) \in \mathrm{SO}(3)$$
which maps the frame of curve 1 to the frame of curve 2 at $s_0$: $\Phi_2(s_0) = \Phi_1(s_0) R^T$.
Now define the rotated curve:
$$\tilde{\mathbf{r}}_1(s) = R \mathbf{r}_1(s) + (\mathbf{r}_2(s_0) - R \mathbf{r}_1(s_0))$$
The rotated curve $\tilde{\mathbf{r}}_1(s)$ satisfies:
- $\tilde{\mathbf{r}}_1(s_0) = \mathbf{r}_2(s_0)$.
- Its Frenet frame is $\tilde{\Phi}_1(s) = \Phi_1(s) R^T$.
- At $s_0$, $\tilde{\Phi}_1(s_0) = \Phi_1(s_0) R^T = \Phi_2(s_0)$.
Both $\tilde{\Phi}_1(s)$ and $\Phi_2(s)$ satisfy the identical linear ODE system $\frac{d\Phi}{ds} = A(s) \Phi(s)$ with identical initial values at $s_0$.
By the uniqueness theorem for ODEs:
$$\tilde{\Phi}_1(s) = \Phi_2(s) \quad \forall s \in I \implies \tilde{\mathbf{T}}_1(s) = \mathbf{T}_2(s) \quad \forall s \in I$$
Integrating the velocity vectors:
$$\mathbf{r}_2(s) - \mathbf{r}_2(s_0) = \int_{s_0}^s \mathbf{T}_2(u) \, du = \int_{s_0}^s \tilde{\mathbf{T}}_1(u) \, du = \tilde{\mathbf{r}}_1(s) - \tilde{\mathbf{r}}_1(s_0)$$
Since $\tilde{\mathbf{r}}_1(s_0) = \mathbf{r}_2(s_0)$, it follows that:
$$\mathbf{r}_2(s) = \tilde{\mathbf{r}}_1(s) = R \mathbf{r}_1(s) + \mathbf{r}_0 \quad \forall s \in I$$
where $R \in \mathrm{SO}(3)$ is a rotation and $\mathbf{r}_0 \in \mathbb{R}^3$ is a translation.
This completes the proof of the Fundamental Theorem. $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u = get_unit2()
    print(f"Loaded Unit 2: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
