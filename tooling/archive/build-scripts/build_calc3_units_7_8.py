import json

def build_unit_7():
    return {
        "id": "calc3-u7",
        "title": "Unit 7: Vector Fields, Path Integrals & Green's Theorem",
        "description": "Exhaustive treatment of vector differential operators (gradient, divergence, curl, vector identities), scalar and vector line integrals, path independence, conservative fields, and Green's theorem in the plane.",
        "sections": [
            {
                "id": "u7-sec1",
                "title": "Vector Fields, Divergence, Curl and Fundamental Identities",
                "content": r"""### 1. Vector Fields in Space

A **vector field** on $\mathbb{R}^3$ is a function $\vec{F}$ that assigns to each point $(x, y, z)$ a three-dimensional vector:

$$\vec{F}(x, y, z) = P(x, y, z)\hat{i} + Q(x, y, z)\hat{j} + R(x, y, z)\hat{k} = \langle P, Q, R \rangle$$

Physical examples include fluid velocity fields $\vec{v}(x, y, z)$, gravitational fields $\vec{F}_g = -\frac{G M m}{r^3}\vec{r}$, and electrostatic fields $\vec{E} = \frac{q}{4\pi\epsilon_0 r^3}\vec{r}$.

If there exists a scalar function $f$ such that $\vec{F} = \nabla f$, then $\vec{F}$ is called a **conservative vector field**, and $f$ is called a **scalar potential** for $\vec{F}$.

---

### 2. Divergence of a Vector Field

**Definition:**  
The **divergence** of a vector field $\vec{F} = \langle P, Q, R \rangle$ is the scalar field defined by the symbolic dot product with the del operator $\nabla = \langle \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \rangle$:

$$\mathbf{\text{div} \, \vec{F} = \nabla \cdot \vec{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}}$$

#### Physical Meaning:
The divergence measures the net rate of outward fluid flux per unit volume at a given point:
- $\text{div} \, \vec{F} > 0$: The point is a **source** (fluid is being produced or expanding).
- $\text{div} \, \vec{F} < 0$: The point is a **sink** (fluid is draining or compressing).
- $\text{div} \, \vec{F} = 0$: The field is **incompressible** or **solenoidal** (e.g., magnetic fields $\nabla \cdot \vec{B} = 0$).

---

### 3. Curl of a Vector Field

**Definition:**  
The **curl** of $\vec{F} = \langle P, Q, R \rangle$ is the vector field defined by the symbolic cross product with $\nabla$:

$$\mathbf{\text{curl} \, \vec{F} = \nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{vmatrix} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)\hat{i} + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right)\hat{j} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\hat{k}}$$

#### Physical Meaning:
The curl measures the tendency of particles to rotate about the axis parallel to $\text{curl} \, \vec{F}$ (vorticity). If a tiny paddle wheel is placed in a fluid flow, it rotates with angular velocity proportional to $|\text{curl} \, \vec{F}|$.
- If $\text{curl} \, \vec{F} = \vec{0}$ everywhere, the vector field is called **irrotational**.

---

### 4. Fundamental Vector Differential Identities

1. **Identity 1 (Curl of a Gradient is Zero):**  
   If $f$ has continuous second partial derivatives:
   $$\mathbf{\nabla \times (\nabla f) = \vec{0}}$$
   *Significance:* Every conservative vector field is irrotational.

2. **Identity 2 (Divergence of a Curl is Zero):**  
   If $\vec{F}$ has continuous second partial derivatives:
   $$\mathbf{\nabla \cdot (\nabla \times \vec{F}) = 0}$$
   *Significance:* A vector field cannot be the curl of another field unless its divergence is identically zero.

3. **The Laplacian:**  
   $$\nabla^2 f = \Delta f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$"""
            },
            {
                "id": "u7-sec2",
                "title": "Line Integrals of Scalar and Vector Fields",
                "content": r"""### 1. Line Integrals of Scalar Fields

Let $C$ be a smooth space curve parameterized by $\vec{r}(t) = \langle x(t), y(t), z(t) \rangle$ for $a \le t \le b$. The **line integral of a scalar function $f$ along $C$** with respect to arc length is:

$$\mathbf{\int_C f(x, y, z) \, ds = \int_a^b f(x(t), y(t), z(t)) |\vec{r}'(t)| \, dt = \int_a^b f(\vec{r}(t)) \sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2} \, dt}$$

If $f(x, y, z) = \rho(x, y, z)$ is linear mass density, the integral gives the **total mass** of the wire.

---

### 2. Line Integrals of Vector Fields (Work and Circulation)

The line integral of a vector field $\vec{F} = \langle P, Q, R \rangle$ along an oriented curve $C$ is the integral of the tangential component of $\vec{F}$:

$$\mathbf{\int_C \vec{F} \cdot d\vec{r} = \int_C \vec{F} \cdot \vec{T} \, ds = \int_a^b \vec{F}(\vec{r}(t)) \cdot \vec{r}'(t) \, dt = \int_C P \, dx + Q \, dy + R \, dz}$$

- **Work:** If $\vec{F}$ is a force field, $\int_C \vec{F} \cdot d\vec{r}$ represents the total **work done** by the field in moving a particle along curve $C$.
- **Circulation:** When $C$ is a closed curve, $\oint_C \vec{F} \cdot d\vec{r}$ is called the **circulation** of $\vec{F}$ around $C$.

---

### 3. The Fundamental Theorem for Line Integrals

**Theorem:**  
Let $C$ be a smooth curve parameterized by $\vec{r}(t)$ for $a \le t \le b$. If $f$ is a continuously differentiable scalar function, then:

$$\mathbf{\int_C \nabla f \cdot d\vec{r} = f(\vec{r}(b)) - f(\vec{r}(a))}$$

#### Proof:
By the Chain Rule:
$$\int_C \nabla f \cdot d\vec{r} = \int_a^b \nabla f(\vec{r}(t)) \cdot \vec{r}'(t) \, dt = \int_a^b \left( \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \frac{\partial f}{\partial z}\frac{dz}{dt} \right) dt = \int_a^b \frac{d}{dt}[f(\vec{r}(t))] \, dt$$
By the single-variable Fundamental Theorem of Calculus:
$$= f(\vec{r}(b)) - f(\vec{r}(a)) \quad \blacksquare$$

#### Fundamental Consequences:
1. **Path Independence:** The line integral of a conservative vector field depends only on the starting point $A = \vec{r}(a)$ and ending point $B = \vec{r}(b)$, and is completely independent of the path taken between them.
2. **Closed Loops:** For any closed loop $C$ ($\vec{r}(a) = \vec{r}(b)$):
   $$\oint_C \nabla f \cdot d\vec{r} = 0$$"""
            },
            {
                "id": "u7-sec3",
                "title": "Green's Theorem in the Plane",
                "content": r"""George Green (1828) discovered a profound theorem connecting a line integral around the boundary of a plane region to a double integral over the interior of the region.

---

### 1. Statement of Green's Theorem

**Theorem (Green's Theorem):**  
Let $D$ be a positively oriented, piecewise-smooth, simply connected region in the $xy$-plane, bounded by a simple closed curve $C = \partial D$. If $P(x, y)$ and $Q(x, y)$ have continuous partial derivatives on an open region containing $D$, then:

$$\mathbf{\oint_C P \, dx + Q \, dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA}$$

> **Positive Orientation:**  
> $C$ is traversed counterclockwise, so that the region $D$ always remains on the left as a traveler walks along the boundary.

---

### 2. Proof for Simple Regions

Assume $D$ is simultaneously Type I ($a \le x \le b, g_1(x) \le y \le g_2(x)$) and Type II.

We prove $\oint_C P \, dx = -\iint_D \frac{\partial P}{\partial y} \, dA$:
$$\iint_D \frac{\partial P}{\partial y} \, dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} \frac{\partial P}{\partial y} \, dy \right) dx = \int_a^b [P(x, g_2(x)) - P(x, g_1(x))] \, dx$$
Now evaluate $\oint_C P \, dx$. The boundary consists of four paths: bottom curve $C_1$, right vertical edge $C_2$, top curve $C_3$ (traversed right-to-left), and left edge $C_4$. Along vertical edges, $dx = 0$.
$$\oint_C P \, dx = \int_{C_1} P \, dx + \int_{C_3} P \, dx = \int_a^b P(x, g_1(x)) \, dx + \int_b^a P(x, g_2(x)) \, dx = -\int_a^b [P(x, g_2(x)) - P(x, g_1(x))] \, dx$$
Thus:
$$\oint_C P \, dx = -\iint_D \frac{\partial P}{\partial y} \, dA$$

An identical argument treating $D$ as a Type II region proves $\oint_C Q \, dy = \iint_D \frac{\partial Q}{\partial x} \, dA$.  
Adding the two equations yields Green's Theorem. $\blacksquare$

---

### 3. Planar Area via Boundary Line Integrals

If we choose functions $P, Q$ such that $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 1$:
1. $P = 0, Q = x \implies \text{Area} = \oint_C x \, dy$
2. $P = -y, Q = 0 \implies \text{Area} = -\oint_C y \, dx$
3. $P = -\frac{y}{2}, Q = \frac{x}{2} \implies \mathbf{A(D) = \frac{1}{2}\oint_C (x \, dy - y \, dx)}$

This formula allows exact calculation of enclosed area solely by integrating along the outer boundary perimeter."""
            }
        ],
        "simulations": [
            {
                "id": "sim_calc3_vector_fields",
                "title": "2D/3D Vector Fields, Circulation & Green's Theorem Engine",
                "description": "Visualize dynamic vector fields (vortices, sinks, saddles). Place and trace closed loop contours, compute line integral circulation work, and verify Green's curl theorem in real time.",
                "controls": [
                    {"param": "fieldPreset", "label": "Field (0:Vortex, 1:Source, 2:Saddle)", "min": 0, "max": 2, "step": 1, "default": 0},
                    {"param": "loopRadius", "label": "Loop Radius R", "min": 0.5, "max": 2.5, "step": 0.1, "default": 1.5},
                    {"param": "loopCenterX", "label": "Loop Center X", "min": -1.5, "max": 1.5, "step": 0.1, "default": 0.0},
                    {"param": "rotY", "label": "Orbit Yaw (°)", "min": -180, "max": 180, "step": 2, "default": 30}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-calc3-7-1",
                "tier": 1,
                "title": "Work Done by a 3D Force Field along a Helical Path",
                "statement": r"""Find the work done by the force field:
$$\vec{F}(x, y, z) = y\hat{i} - x\hat{j} + z\hat{k}$$
in moving a particle along the helical curve:
$$\vec{r}(t) = \langle \cos t, \; \sin t, \; t \rangle \quad \text{from } t = 0 \text{ to } t = 2\pi$$""",
                "solution": r"""**Step 1: Parametrize the components and compute $d\vec{r}$**  
From $\vec{r}(t) = \langle \cos t, \; \sin t, \; t \rangle$:
$$x(t) = \cos t \implies dx = -\sin t \, dt$$
$$y(t) = \sin t \implies dy = \cos t \, dt$$
$$z(t) = t \implies dz = dt$$

---

**Step 2: Express $\vec{F}$ in terms of the parameter $t$**  
$$\vec{F}(\vec{r}(t)) = \langle \sin t, \; -\cos t, \; t \rangle$$

---

**Step 3: Evaluate the dot product $\vec{F} \cdot \vec{r}'(t)$**  
$$\vec{r}'(t) = \langle -\sin t, \; \cos t, \; 1 \rangle$$
$$\vec{F} \cdot \vec{r}'(t) = (\sin t)(-\sin t) + (-\cos t)(\cos t) + (t)(1)$$
$$= -\sin^2 t - \cos^2 t + t = -(\sin^2 t + \cos^2 t) + t = -1 + t$$

---

**Step 4: Integrate from $t = 0$ to $t = 2\pi$**  
$$W = \int_C \vec{F} \cdot d\vec{r} = \int_0^{2\pi} (t - 1) \, dt$$
$$= \left[ \frac{t^2}{2} - t \right]_0^{2\pi} = \left( \frac{(2\pi)^2}{2} - 2\pi \right) - 0 = \frac{4\pi^2}{2} - 2\pi = \mathbf{2\pi^2 - 2\pi}$$
Numerically, $W \approx 2(9.8696) - 2(3.1416) = 19.739 - 6.283 = \mathbf{13.456} \text{ Joules}$."""
            },
            {
                "id": "prob-calc3-7-2",
                "tier": 2,
                "title": "Finding a Scalar Potential and Path-Independent Line Integral",
                "statement": r"""Consider the vector field:
$$\vec{F}(x, y, z) = (2xy + z^3)\hat{i} + (x^2 + 2yz)\hat{j} + (3xz^2 + y^2)\hat{k}$$
(a) Prove that $\vec{F}$ is a conservative vector field.  
(b) Find a scalar potential function $f(x, y, z)$ such that $\nabla f = \vec{F}$.  
(c) Evaluate $\int_C \vec{F} \cdot d\vec{r}$ along any path $C$ from $A(1, 0, 2)$ to $B(2, 1, 3)$.""",
                "solution": r"""**Part (a): Verify $\nabla \times \vec{F} = \vec{0}$**  
Let $P = 2xy + z^3$, $Q = x^2 + 2yz$, $R = 3xz^2 + y^2$.  
Compute the curl:
$$\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} = 2y - 2y = 0$$
$$\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} = 3z^2 - 3z^2 = 0$$
$$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2x - 2x = 0$$

Since $\nabla \times \vec{F} = \vec{0}$ throughout $\mathbb{R}^3$ (a simply connected domain), $\vec{F}$ is strictly **conservative**. $\blacksquare$

---

**Part (b): Construct the Potential Function $f$**  
We require $\nabla f = \langle f_x, f_y, f_z \rangle = \vec{F}$:
1. $f_x = 2xy + z^3 \implies f(x, y, z) = x^2 y + x z^3 + g(y, z)$
2. Differentiate with respect to $y$:
   $$f_y = x^2 + \frac{\partial g}{\partial y}$$
   Equate to $Q = x^2 + 2yz$:
   $$x^2 + \frac{\partial g}{\partial y} = x^2 + 2yz \implies \frac{\partial g}{\partial y} = 2yz \implies g(y, z) = y^2 z + h(z)$$
   Thus: $f(x, y, z) = x^2 y + x z^3 + y^2 z + h(z)$.
3. Differentiate with respect to $z$:
   $$f_z = 3x z^2 + y^2 + h'(z)$$
   Equate to $R = 3x z^2 + y^2$:
   $$3x z^2 + y^2 + h'(z) = 3x z^2 + y^2 \implies h'(z) = 0 \implies h(z) = C$$

Choosing $C = 0$, the scalar potential is:
$$\mathbf{f(x, y, z) = x^2 y + x z^3 + y^2 z}$$

---

**Part (c): Evaluate the Line Integral**  
By the Fundamental Theorem for Line Integrals:
$$\int_C \vec{F} \cdot d\vec{r} = f(B) - f(A) = f(2, 1, 3) - f(1, 0, 2)$$

Evaluate at $B(2, 1, 3)$:
$$f(2, 1, 3) = (2^2)(1) + 2(3^3) + (1^2)(3) = 4 + 2(27) + 3 = 4 + 54 + 3 = 61$$

Evaluate at $A(1, 0, 2)$:
$$f(1, 0, 2) = (1^2)(0) + 1(2^3) + (0^2)(2) = 0 + 8 + 0 = 8$$

Thus:
$$\int_C \vec{F} \cdot d\vec{r} = 61 - 8 = \mathbf{53}$$"""
            },
            {
                "id": "prob-calc3-7-3",
                "tier": 3,
                "title": "Enclosed Area of an Astroid via Green's Theorem Line Integral",
                "statement": r"""Use Green's Theorem line integral area formula:
$$A = \frac{1}{2}\oint_C (x \, dy - y \, dx)$$
to calculate the exact area enclosed by the astroid (hypocycloid with four cusps) parameterized by:
$$\vec{r}(t) = \langle a\cos^3 t, \; a\sin^3 t \rangle \quad (0 \le t \le 2\pi, \; a > 0)$$""",
                "solution": r"""**Step 1: Compute $x, y, dx, dy$**  
$$x(t) = a\cos^3 t \implies dx = 3a\cos^2 t (-\sin t) \, dt = -3a\cos^2 t \sin t \, dt$$
$$y(t) = a\sin^3 t \implies dy = 3a\sin^2 t (\cos t) \, dt = 3a\sin^2 t \cos t \, dt$$

---

**Step 2: Evaluate the integrand $x \, dy - y \, dx$**  
$$x \, dy = (a\cos^3 t)(3a\sin^2 t \cos t) \, dt = 3a^2 \cos^4 t \sin^2 t \, dt$$
$$y \, dx = (a\sin^3 t)(-3a\cos^2 t \sin t) \, dt = -3a^2 \sin^4 t \cos^2 t \, dt$$

Subtracting:
$$x \, dy - y \, dx = [3a^2 \cos^4 t \sin^2 t - (-3a^2 \sin^4 t \cos^2 t)] \, dt$$
$$= 3a^2 \sin^2 t \cos^2 t (\cos^2 t + \sin^2 t) \, dt$$
Since $\cos^2 t + \sin^2 t = 1$:
$$x \, dy - y \, dx = 3a^2 \sin^2 t \cos^2 t \, dt$$

Recall the double-angle identity: $\sin t \cos t = \frac{1}{2}\sin 2t$:
$$\sin^2 t \cos^2 t = \frac{1}{4}\sin^2(2t)$$
Therefore:
$$x \, dy - y \, dx = \frac{3a^2}{4}\sin^2(2t) \, dt$$

---

**Step 3: Integrate along $0 \le t \le 2\pi$**  
$$A = \frac{1}{2}\oint_C (x \, dy - y \, dx) = \frac{1}{2} \int_0^{2\pi} \frac{3a^2}{4}\sin^2(2t) \, dt = \frac{3a^2}{8} \int_0^{2\pi} \sin^2(2t) \, dt$$

Using $\sin^2(2t) = \frac{1 - \cos 4t}{2}$:
$$\int_0^{2\pi} \sin^2(2t) \, dt = \int_0^{2\pi} \frac{1 - \cos 4t}{2} \, dt = \left[ \frac{t}{2} - \frac{\sin 4t}{8} \right]_0^{2\pi} = \frac{2\pi}{2} - 0 = \pi$$

---

**Step 4: Compute Final Enclosed Area**  
$$A = \frac{3a^2}{8} \cdot \pi = \mathbf{\frac{3\pi}{8} a^2}$$

This demonstrates the extraordinary elegance of Green's theorem: a complicated non-convex planar region with four cusps is integrated around its boundary in closed form. $\blacksquare$"""
            }
        ]
    }

def build_unit_8():
    return {
        "id": "calc3-u8",
        "title": "Unit 8: Surface Integrals, Stokes' Theorem & Gauss' Divergence Theorem",
        "description": "Parametric surfaces, area differentials, surface integrals of scalar and vector fields, Stokes' curl circulation theorem, Gauss' divergence theorem, physical applications, and the grand unification of differential forms.",
        "sections": [
            {
                "id": "u8-sec1",
                "title": "Parametric Surfaces, Tangent Planes and Surface Area",
                "content": r"""Just as a space curve is traced out by a vector function of a single parameter $t$, a two-dimensional surface in $\mathbb{R}^3$ is described by a vector function of **two parameters** $u$ and $v$:

$$\vec{r}(u, v) = x(u, v)\hat{i} + y(u, v)\hat{j} + z(u, v)\hat{k} = \langle x(u, v), y(u, v), z(u, v) \rangle$$
where $(u, v)$ varies over a planar parameter region $D \subset \mathbb{R}^2$.

---

### 1. Tangent Vectors and Normal Vectors

Holding $v = v_0$ constant, $\vec{r}(u, v_0)$ traces a grid curve on the surface whose tangent vector is:
$$\vec{r}_u = \frac{\partial\vec{r}}{\partial u} = \left\langle \frac{\partial x}{\partial u}, \frac{\partial y}{\partial u}, \frac{\partial z}{\partial u} \right\rangle$$

Similarly, holding $u = u_0$ constant gives the grid curve tangent vector:
$$\vec{r}_v = \frac{\partial\vec{r}}{\partial v} = \left\langle \frac{\partial x}{\partial v}, \frac{\partial y}{\partial v}, \frac{\partial z}{\partial v} \right\rangle$$

The normal vector to the tangent plane at $(u_0, v_0)$ is the cross product:

$$\mathbf{\vec{n} = \vec{r}_u \times \vec{r}_v}$$

The surface is called **smooth** if $\vec{r}_u \times \vec{r}_v \neq \vec{0}$ everywhere.

---

### 2. The Surface Area Differential and Total Area

An infinitesimal parameter rectangle $\Delta u \times \Delta v$ maps to a curved patch on the surface approximated by the tangent parallelogram spanned by $\vec{r}_u \Delta u$ and $\vec{r}_v \Delta v$.

The area of this parallelogram is:
$$\Delta S \approx |(\vec{r}_u \Delta u) \times (\vec{r}_v \Delta v)| = |\vec{r}_u \times \vec{r}_v| \Delta u \Delta v$$

In differential form:
$$\mathbf{dS = |\vec{r}_u \times \vec{r}_v| \, du \, dv}$$

**Total Surface Area:**
$$\mathbf{A(S) = \iint_D |\vec{r}_u \times \vec{r}_v| \, dA}$$

#### Explicit Cartesian Surfaces $z = g(x, y)$:
Parameterize with $u = x, v = y$: $\vec{r}(x, y) = \langle x, y, g(x, y) \rangle$.  
$\vec{r}_x = \langle 1, 0, g_x \rangle$, $\vec{r}_y = \langle 0, 1, g_y \rangle$.  
$\vec{r}_x \times \vec{r}_y = \langle -g_x, -g_y, 1 \rangle$.  
$$|\vec{r}_x \times \vec{r}_y| = \sqrt{1 + g_x^2 + g_y^2}$$

$$\mathbf{A(S) = \iint_D \sqrt{1 + \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2} \, dx \, dy}$$"""
            },
            {
                "id": "u8-sec2",
                "title": "Surface Integrals of Scalar Fields and Vector Flux",
                "content": r"""### 1. Surface Integrals of Scalar Fields

If $f(x, y, z)$ is a continuous scalar function defined on a smooth surface $S$:

$$\mathbf{\iint_S f(x, y, z) \, dS = \iint_D f(\vec{r}(u, v)) |\vec{r}_u \times \vec{r}_v| \, du \, dv}$$

If $f(x, y, z) = \rho(x, y, z)$ is surface mass density, the integral computes the **total mass** of the curved shell.

---

### 2. Oriented Surfaces and Unit Normals

A surface $S$ is **orientable** (two-sided) if it is possible to define a continuous unit normal vector field $\hat{n}$ across the entire surface (excluding non-orientable manifolds like the Möbius strip).

For a parameterized smooth surface, the unit normal is:
$$\mathbf{\hat{n} = \frac{\vec{r}_u \times \vec{r}_v}{|\vec{r}_u \times \vec{r}_v|}}$$

---

### 3. Surface Integrals of Vector Fields (Flux Integrals)

Let $\vec{F}$ be a continuous vector field on an oriented surface $S$ with unit normal $\hat{n}$.

**Definition:**  
The **flux** of $\vec{F}$ across $S$ is the surface integral of the normal component of $\vec{F}$:

$$\mathbf{\Phi = \iint_S \vec{F} \cdot d\vec{S} = \iint_S \vec{F} \cdot \hat{n} \, dS = \iint_D \vec{F}(\vec{r}(u, v)) \cdot (\vec{r}_u \times \vec{r}_v) \, du \, dv}$$

Notice that the magnitude $|\vec{r}_u \times \vec{r}_v|$ in the unit normal cancels directly with the area element $dS = |\vec{r}_u \times \vec{r}_v| du dv$!

#### Physical Meaning:
If $\vec{F} = \rho \vec{v}$ is the mass flow rate per unit area of a moving fluid, $\iint_S \vec{F} \cdot d\vec{S}$ represents the total **mass of fluid passing through surface $S$ per unit time**."""
            },
            {
                "id": "u8-sec3",
                "title": "Stokes' Theorem, Gauss' Divergence Theorem & Grand Unification",
                "content": r"""### 1. Stokes' Theorem (Curl Circulation Theorem)

Sir George Gabriel Stokes (1854) established the higher-dimensional generalization of Green's theorem relating the circulation around a boundary curve in 3D space to the flux of curl through any spanning surface.

**Theorem (Stokes' Theorem):**  
Let $S$ be an oriented piecewise-smooth surface bounded by a simple, closed, piecewise-smooth space curve $C = \partial S$ whose orientation is positive relative to the normal vector $\hat{n}$ of $S$ (by the right-hand rule). If $\vec{F}$ is a vector field with continuous partial derivatives:

$$\mathbf{\oint_{\partial S} \vec{F} \cdot d\vec{r} = \iint_S (\nabla \times \vec{F}) \cdot d\vec{S}}$$

#### Fundamental Invariance (Surface Independence):
If $S_1$ and $S_2$ are any two distinct surfaces that share the exact same boundary curve $\partial S_1 = \partial S_2 = C$, then:
$$\iint_{S_1} (\nabla \times \vec{F}) \cdot d\vec{S} = \iint_{S_2} (\nabla \times \vec{F}) \cdot d\vec{S} = \oint_C \vec{F} \cdot d\vec{r}$$
The flux of curl through a surface depends solely on its boundary rim, not on its bulging shape!

---

### 2. Gauss' Divergence Theorem

Carl Friedrich Gauss (1813) proved the fundamental theorem connecting the flux of a vector field across a closed bounding surface to the volume integral of its divergence throughout the enclosed solid.

**Theorem (The Divergence Theorem):**  
Let $E$ be a simple solid region in $\mathbb{R}^3$, and let $S = \partial E$ be its boundary surface, oriented with outward-pointing unit normal $\hat{n}$. If $\vec{F}$ is a vector field with continuous partial derivatives on an open region containing $E$:

$$\mathbf{\iint_{\partial E} \vec{F} \cdot d\vec{S} = \iiint_E (\nabla \cdot \vec{F}) \, dV}$$

#### Physical Interpretation:
The total net fluid volume exiting a closed container across its skin must equal the sum of all internal sources (divergence) within the container.

#### Major Applications in Physics:
1. **Gauss' Law in Electromagnetism:** $\iint_{\partial E} \vec{E} \cdot d\vec{S} = \frac{1}{\epsilon_0}\iiint_E \rho \, dV = \frac{Q_{enc}}{\epsilon_0} \implies \nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$ (Maxwell's First Equation).
2. **Fluid Continuity Equation:** $\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0$.

---

### 3. The Grand Unification: Generalized Stokes' Theorem

All the fundamental integral theorems of calculus across all dimensions are manifestations of one single, universal topological equation for differential forms on an oriented manifold $\Omega$ with boundary $\partial \Omega$:

$$\mathbf{\int_{\partial \Omega} \omega = \int_\Omega d\omega}$$

| Dimension | Manifold $\Omega$ | Boundary $\partial \Omega$ | Classical Theorem |
| :---: | :---: | :---: | :---: |
| **$n = 1$** | Curve $[a, b]$ | Points $\{a, b\}$ | **Fundamental Theorem of Calculus:** $\int_a^b F'(x) dx = F(b) - F(a)$ |
| **$n = 2$** | Plane Region $D$ | Boundary Curve $C$ | **Green's Theorem:** $\oint_C P dx + Q dy = \iint_D (Q_x - P_y) dA$ |
| **$n = 2$** | Spatial Surface $S$ | Space Curve $C$ | **Stokes' Theorem:** $\oint_{\partial S} \vec{F} \cdot d\vec{r} = \iint_S (\nabla \times \vec{F}) \cdot d\vec{S}$ |
| **$n = 3$** | Solid Volume $E$ | Closed Surface $S$ | **Divergence Theorem:** $\iint_{\partial E} \vec{F} \cdot d\vec{S} = \iiint_E (\nabla \cdot \vec{F}) dV$ |"""
            }
        ],
        "simulations": [
            {
                "id": "sim_calc3_flux_divergence",
                "title": "3D Surface Flux, Stokes & Gauss Divergence Engine",
                "description": "Interact with 3D closed surfaces (cylinder, sphere, cube). Observe vector flux arrows piercing the boundary, evaluate Stokes' loop circulation, and verify Gauss' divergence theorem in real time.",
                "controls": [
                    {"param": "solidShape", "label": "Solid (0:Cylinder, 1:Sphere, 2:Paraboloid)", "min": 0, "max": 2, "step": 1, "default": 0},
                    {"param": "fieldPower", "label": "Divergence Strength k", "min": 0.5, "max": 3.0, "step": 0.2, "default": 1.5},
                    {"param": "solidRadius", "label": "Radius / Size R", "min": 1.0, "max": 3.0, "step": 0.2, "default": 2.0},
                    {"param": "rotY", "label": "Orbit Yaw (°)", "min": -180, "max": 180, "step": 2, "default": 35}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-calc3-8-1",
                "tier": 1,
                "title": "Surface Area of a Paraboloid Cap Cut by a Plane",
                "statement": r"""Find the exact surface area of the portion of the circular paraboloid:
$$z = 4 - x^2 - y^2$$
that lies above the $xy$-plane ($z \ge 0$).""",
                "solution": r"""**Step 1: Express the surface and find the projection domain $D$**  
The surface is $z = g(x, y) = 4 - x^2 - y^2$.  
It intersects $z = 0$ when:
$$4 - x^2 - y^2 = 0 \implies x^2 + y^2 = 4$$

The projection domain $D$ in the $xy$-plane is a circular disk of radius $R = 2$:
$$D = \{ (x, y) \in \mathbb{R}^2 : x^2 + y^2 \le 4 \}$$

---

**Step 2: Compute partial derivatives and surface area element $dS$**  
$$g_x = \frac{\partial z}{\partial x} = -2x, \qquad g_y = \frac{\partial z}{\partial y} = -2y$$
$$1 + g_x^2 + g_y^2 = 1 + (-2x)^2 + (-2y)^2 = 1 + 4(x^2 + y^2)$$

Thus:
$$dS = \sqrt{1 + 4(x^2 + y^2)} \, dA$$

---

**Step 3: Convert to polar coordinates and integrate**  
In polar coordinates, $x^2 + y^2 = r^2$ with $0 \le r \le 2$ and $0 \le \theta \le 2\pi$:
$$A = \iint_D \sqrt{1 + 4r^2} \, (r \, dr \, d\theta) = \left( \int_0^{2\pi} d\theta \right) \left( \int_0^2 r \sqrt{1 + 4r^2} \, dr \right)$$

Evaluate the $r$-integral with $u = 1 + 4r^2 \implies du = 8r \, dr \implies r \, dr = \frac{1}{8} du$:
When $r = 0$, $u = 1$; when $r = 2$, $u = 1 + 4(4) = 17$:
$$\int_0^2 r \sqrt{1 + 4r^2} \, dr = \frac{1}{8} \int_1^{17} u^{1/2} \, du = \frac{1}{8} \left[ \frac{2}{3} u^{3/2} \right]_1^{17} = \frac{1}{12} (17^{3/2} - 1)$$

Multiply by $2\pi$:
$$A = 2\pi \cdot \frac{1}{12}(17\sqrt{17} - 1) = \mathbf{\frac{\pi}{6}(17\sqrt{17} - 1)} \approx \frac{\pi}{6}(70.093 - 1) \approx \mathbf{36.177}$$"""
            },
            {
                "id": "prob-calc3-8-2",
                "tier": 2,
                "title": "Verification of Stokes' Theorem over an Open Hemisphere",
                "statement": r"""Verify Stokes' Theorem for the vector field:
$$\vec{F}(x, y, z) = -y\hat{i} + x\hat{j} - 2\hat{k}$$
where $S$ is the upper hemisphere $z = \sqrt{1 - x^2 - y^2}$ ($z \ge 0$), oriented with upward normal, and $C = \partial S$ is the unit boundary circle $x^2 + y^2 = 1, z = 0$ oriented counterclockwise.""",
                "solution": r"""**Step 1: Evaluate the Line Integral $\oint_C \vec{F} \cdot d\vec{r}$**  
Parametrize the boundary circle $C$:
$$\vec{r}(t) = \langle \cos t, \; \sin t, \; 0 \rangle \quad (0 \le t \le 2\pi)$$
$$\vec{r}'(t) = \langle -\sin t, \; \cos t, \; 0 \rangle$$

Substitute into $\vec{F}$:
$$\vec{F}(\vec{r}(t)) = \langle -\sin t, \; \cos t, \; -2 \rangle$$

Compute the dot product:
$$\vec{F} \cdot \vec{r}'(t) = (-\sin t)(-\sin t) + (\cos t)(\cos t) + (-2)(0) = \sin^2 t + \cos^2 t = 1$$

Integrate:
$$\oint_C \vec{F} \cdot d\vec{r} = \int_0^{2\pi} 1 \, dt = \mathbf{2\pi}$$

---

**Step 2: Compute $\text{curl} \, \vec{F}$**  
$$\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ -y & x & -2 \end{vmatrix} = \hat{i}(0 - 0) - \hat{j}(0 - 0) + \hat{k}\left(\frac{\partial}{\partial x}(x) - \frac{\partial}{\partial y}(-y)\right) = \hat{k}(1 - (-1)) = 2\hat{k}$$

Thus:
$$\nabla \times \vec{F} = \langle 0, \; 0, \; 2 \rangle$$

---

**Step 3: Evaluate the Surface Integral $\iint_S (\nabla \times \vec{F}) \cdot d\vec{S}$**  
Using surface independence (or projecting $S: z = \sqrt{1 - x^2 - y^2}$ onto $D: x^2 + y^2 \le 1$):
For explicit surface $z = g(x, y)$:
$$d\vec{S} = \langle -g_x, \; -g_y, \; 1 \rangle \, dA$$

Now compute the dot product with $\nabla \times \vec{F} = \langle 0, 0, 2 \rangle$:
$$(\nabla \times \vec{F}) \cdot d\vec{S} = \langle 0, \; 0, \; 2 \rangle \cdot \langle -g_x, \; -g_y, \; 1 \rangle \, dA = 2 \, dA$$

Integrate over the unit disk $D$:
$$\iint_S (\nabla \times \vec{F}) \cdot d\vec{S} = \iint_D 2 \, dA = 2 \iint_D 1 \, dA = 2 \times (\pi \cdot 1^2) = \mathbf{2\pi}$$

---

**Step 4: Conclusion**  
$$\oint_C \vec{F} \cdot d\vec{r} = 2\pi = \iint_S (\nabla \times \vec{F}) \cdot d\vec{S}$$
Stokes' Theorem is verified with exact precision. $\blacksquare$"""
            },
            {
                "id": "prob-calc3-8-3",
                "tier": 3,
                "title": "Outward Flux Calculation via Gauss' Divergence Theorem",
                "statement": r"""Use the Divergence Theorem to calculate the outward flux $\iint_S \vec{F} \cdot d\vec{S}$ of the vector field:
$$\vec{F}(x, y, z) = (x^3 + \tan(yz))\hat{i} + (y^3 + e^{xz})\hat{j} + (z^3 + \ln(1+x^2))\hat{k}$$
across the closed boundary surface $S$ of the solid cylinder $E$ defined by:
$$x^2 + y^2 \le 4, \qquad 0 \le z \le 3$$""",
                "solution": r"""**Step 1: Compute $\text{div} \, \vec{F}$**  
Notice that evaluating the flux directly over the three distinct boundary patches of the cylinder (top disk, bottom disk, lateral cylinder) would be exceedingly difficult due to the non-elementary terms $\tan(yz), e^{xz}, \ln(1+x^2)$.

Compute the divergence:
$$\text{div} \, \vec{F} = \frac{\partial}{\partial x}(x^3 + \tan(yz)) + \frac{\partial}{\partial y}(y^3 + e^{xz}) + \frac{\partial}{\partial z}(z^3 + \ln(1+x^2))$$
$$= 3x^2 + 0 + 3y^2 + 0 + 3z^2 + 0 = 3(x^2 + y^2 + z^2)$$

Remarkably, all non-elementary terms vanish identically under differentiation!

---

**Step 2: Apply the Divergence Theorem**  
$$\iint_S \vec{F} \cdot d\vec{S} = \iiint_E 3(x^2 + y^2 + z^2) \, dV$$

---

**Step 3: Convert to Cylindrical Coordinates**  
The solid cylinder $E$ in cylindrical coordinates is:
$$0 \le r \le 2, \qquad 0 \le \theta \le 2\pi, \qquad 0 \le z \le 3$$
Since $x^2 + y^2 = r^2$ and $dV = r \, dz \, dr \, d\theta$:

$$\iiint_E 3(r^2 + z^2) r \, dz \, dr \, d\theta = 3 \int_0^{2\pi} \int_0^2 \int_0^3 (r^3 + r z^2) \, dz \, dr \, d\theta$$

---

**Step 4: Evaluate the Triple Integral**  
The $\theta$-integral gives $2\pi$:
$$\Phi = 3(2\pi) \int_0^2 \left( \int_0^3 (r^3 + r z^2) \, dz \right) dr = 6\pi \int_0^2 \left[ r^3 z + r \frac{z^3}{3} \right]_{z=0}^{z=3} dr$$
$$= 6\pi \int_0^2 (3r^3 + 9r) \, dr$$

Evaluate the $r$-integral:
$$\int_0^2 (3r^3 + 9r) \, dr = \left[ \frac{3r^4}{4} + \frac{9r^2}{2} \right]_0^2 = \frac{3(16)}{4} + \frac{9(4)}{2} = 12 + 18 = 30$$

Multiply:
$$\Phi = 6\pi \times 30 = \mathbf{180\pi} \approx 565.487$$

The outward flux is exactly $180\pi$. $\blacksquare$"""
            }
        ]
    }

if __name__ == "__main__":
    print("Building Calculus III: Units 7 & 8...")
    u7 = build_unit_7()
    with open("calc3_u7.json", "w", encoding="utf-8") as f:
        json.dump(u7, f, indent=2, ensure_ascii=False)
    print("Saved calc3_u7.json successfully.")

    u8 = build_unit_8()
    with open("calc3_u8.json", "w", encoding="utf-8") as f:
        json.dump(u8, f, indent=2, ensure_ascii=False)
    print("Saved calc3_u8.json successfully.")
