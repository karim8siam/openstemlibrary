import json

def build_unit_1():
    return {
        "id": "calc3-u1",
        "title": "Unit 1: Vector-Valued Functions, Space Curves & Arc Length",
        "description": "Foundations of vector-valued functions of a real variable: limits, derivatives, algebraic product rules, tangent vectors, trajectory dynamics, arc length integration, and intrinsic arc length reparameterization.",
        "sections": [
            {
                "id": "u1-sec1",
                "title": "Vector Functions and Space Curves in R^3",
                "content": r"""### 1. Definition and Parametric Representation

A **vector-valued function** (or simply **vector function**) is a mapping $\vec{r}: I \subseteq \mathbb{R} \to \mathbb{R}^3$ that assigns to each real number $t$ in an interval $I$ a unique spatial vector:

$$\vec{r}(t) = f(t)\hat{i} + g(t)\hat{j} + h(t)\hat{k} = \langle f(t), g(t), h(t) \rangle$$

The functions $f(t), g(t), h(t)$ are real-valued functions of the single real parameter $t$, called the **component functions** of $\vec{r}$.

As $t$ varies over the domain $I$, the terminal point of the position vector $\vec{r}(t)$ traces out a one-dimensional geometric locus in three-dimensional space called a **space curve** $C$:

$$C = \{ (x, y, z) \in \mathbb{R}^3 : x = f(t), \; y = g(t), \; z = h(t), \; t \in I \}$$

These are the **parametric equations** of the curve $C$, and $t$ is called the **parameter** (often representing physical time).

---

### 2. Canonical Examples of Space Curves

1. **The Circular Helix:**  
   $$\vec{r}(t) = \langle a\cos t, \; a\sin t, \; bt \rangle \quad (a > 0, \; b \neq 0)$$  
   The projection of this curve onto the $xy$-plane is a circle of radius $a$: $x^2 + y^2 = a^2\cos^2 t + a^2\sin^2 t = a^2$. As $t$ increases, the point winds around the cylinder $x^2 + y^2 = a^2$ while ascending steadily along the $z$-axis at rate $b$. The constant pitch between adjacent coils is $2\pi b$.

2. **The Twisted Cubic:**  
   $$\vec{r}(t) = \langle t, \; t^2, \; t^3 \rangle$$  
   This curve lies at the intersection of the parabolic cylinder $y = x^2$ and the cubic cylinder $z = x^3$. It is the simplest non-planar algebraic space curve.

3. **The Conical Helix:**  
   $$\vec{r}(t) = \langle t\cos t, \; t\sin t, \; t \rangle$$  
   Here, $x^2 + y^2 = t^2 = z^2$. The curve winds around the right circular cone $x^2 + y^2 = z^2$, expanding outward as it ascends.

---

### 3. Limits and Continuity

The limit of a vector function $\vec{r}(t)$ as $t \to a$ is evaluated componentwise:

$$\lim_{t \to a} \vec{r}(t) = \left\langle \lim_{t \to a} f(t), \; \lim_{t \to a} g(t), \; \lim_{t \to a} h(t) \right\rangle$$

provided the limits of all three component functions exist.

**Continuity:**  
A vector function $\vec{r}(t)$ is **continuous at $a$** if:

$$\lim_{t \to a} \vec{r}(t) = \vec{r}(a)$$

Equivalently, $\vec{r}(t)$ is continuous at $a$ if and only if each of its component functions $f, g, h$ is continuous at $a$."""
            },
            {
                "id": "u1-sec2",
                "title": "Differentiation and Integration of Vector Functions",
                "content": r"""### 1. The Derivative of a Vector Function

The derivative of a vector-valued function $\vec{r}(t)$ is defined analogously to that of a real-valued function:

$$\vec{r}'(t) = \frac{d\vec{r}}{dt} = \lim_{\Delta t \to 0} \frac{\vec{r}(t + \Delta t) - \vec{r}(t)}{\Delta t}$$

In terms of component functions:

$$\vec{r}'(t) = \lim_{\Delta t \to 0} \left\langle \frac{f(t+\Delta t) - f(t)}{\Delta t}, \; \frac{g(t+\Delta t) - g(t)}{\Delta t}, \; \frac{h(t+\Delta t) - h(t)}{\Delta t} \right\rangle$$
$$\mathbf{\vec{r}'(t) = \langle f'(t), \; g'(t), \; h'(t) \rangle = f'(t)\hat{i} + g'(t)\hat{j} + h'(t)\hat{k}}$$

---

### 2. Geometric Interpretation: Tangent Vector and Velocity

As $\Delta t \to 0$, the secant vector $\frac{\vec{r}(t+\Delta t) - \vec{r}(t)}{\Delta t}$ approaches a limiting vector that points in the direction of the tangent line to the curve at $P(\vec{r}(t))$.
- **Tangent Vector:** $\vec{r}'(t)$ is tangent to the space curve at $\vec{r}(t)$ in the direction of increasing $t$.
- **Unit Tangent Vector $\vec{T}(t)$:** For a curve with $\vec{r}'(t) \neq \vec{0}$:
  $$\mathbf{\vec{T}(t) = \frac{\vec{r}'(t)}{|\vec{r}'(t)|}}$$
- **Smooth Curve:** A curve parameterized by $\vec{r}(t)$ is called **smooth** on an interval $I$ if $\vec{r}'(t)$ is continuous and $\vec{r}'(t) \neq \vec{0}$ for all $t \in I$ (no sharp corners, cusps, or stopping points).
- **Tangent Line:** The parametric equation of the tangent line to the space curve at $t = t_0$ is:
  $$\vec{L}(\tau) = \vec{r}(t_0) + \tau \vec{r}'(t_0) \quad (\tau \in \mathbb{R})$$

---

### 3. Vector Differentiation Rules

Let $\vec{u}(t)$ and $\vec{v}(t)$ be differentiable vector functions, $c$ a scalar constant, and $f(t)$ a differentiable scalar function:

1. $\frac{d}{dt} [\vec{u}(t) + \vec{v}(t)] = \vec{u}'(t) + \vec{v}'(t)$
2. $\frac{d}{dt} [c\vec{u}(t)] = c\vec{u}'(t)$
3. $\frac{d}{dt} [f(t)\vec{u}(t)] = f'(t)\vec{u}(t) + f(t)\vec{u}'(t)$ (Scalar-Vector Product Rule)
4. $\frac{d}{dt} [\vec{u}(t) \cdot \vec{v}(t)] = \vec{u}'(t) \cdot \vec{v}(t) + \vec{u}(t) \cdot \vec{v}'(t)$ (Dot Product Rule)
5. $\frac{d}{dt} [\vec{u}(t) \times \vec{v}(t)] = \vec{u}'(t) \times \vec{v}(t) + \vec{u}(t) \times \vec{v}'(t)$ (Cross Product Rule — **order must be strictly preserved!**)
6. $\frac{d}{dt} [\vec{u}(f(t))] = f'(t)\vec{u}'(f(t))$ (Chain Rule)

---

### 4. Fundamental Orthogonality Theorem for Constant Length Vectors

**Theorem:**  
If a vector function $\vec{r}(t)$ has constant magnitude for all $t$, that is, $|\vec{r}(t)| = c$ (a constant), then:

$$\mathbf{\vec{r}(t) \cdot \vec{r}'(t) = 0}$$

That is, the derivative vector $\vec{r}'(t)$ is everywhere orthogonal to the position vector $\vec{r}(t)$.

#### Proof:
Since $|\vec{r}(t)| = c$, the dot product of $\vec{r}(t)$ with itself is constant:

$$\vec{r}(t) \cdot \vec{r}(t) = |\vec{r}(t)|^2 = c^2$$

Differentiating both sides with respect to $t$ using the Dot Product Rule:

$$\frac{d}{dt} [\vec{r}(t) \cdot \vec{r}(t)] = \frac{d}{dt}[c^2]$$
$$\vec{r}'(t) \cdot \vec{r}(t) + \vec{r}(t) \cdot \vec{r}'(t) = 0$$
$$2 \left( \vec{r}(t) \cdot \vec{r}'(t) \right) = 0 \implies \vec{r}(t) \cdot \vec{r}'(t) = 0 \quad \blacksquare$$

**Geometric Meaning:** If a particle moves on the surface of a sphere centered at the origin ($|\vec{r}(t)| = R$), its velocity vector is always tangent to the sphere, and therefore perpendicular to the radius vector.

---

### 5. Integration of Vector Functions

The definite integral of a continuous vector function $\vec{r}(t) = \langle f(t), g(t), h(t) \rangle$ is evaluated componentwise:

$$\int_a^b \vec{r}(t) \, dt = \left( \int_a^b f(t) \, dt \right)\hat{i} + \left( \int_a^b g(t) \, dt \right)\hat{j} + \left( \int_a^b h(t) \, dt \right)\hat{k}$$

By the Fundamental Theorem of Calculus, if $\vec{R}'(t) = \vec{r}(t)$, then $\int_a^b \vec{r}(t) \, dt = \vec{R}(b) - \vec{R}(a)$."""
            },
            {
                "id": "u1-sec3",
                "title": "Arc Length and Arc Length Parameterization",
                "content": r"""### 1. Arc Length of a Space Curve

Let $C$ be a smooth space curve parameterized by $\vec{r}(t) = \langle f(t), g(t), h(t) \rangle$ for $a \le t \le b$.

Partition the parameter interval $[a, b]$ into $n$ subintervals by $a = t_0 < t_1 < \dots < t_n = b$. The length of the polygonal secant connecting $\vec{r}(t_{i-1})$ to $\vec{r}(t_i)$ is:

$$\Delta L_i = |\vec{r}(t_i) - \vec{r}(t_{i-1})| = |\Delta \vec{r}_i| \approx |\vec{r}'(t_i^*)| \Delta t_i$$

Taking the limit as the partition mesh goes to zero ($\Delta t \to 0$):

$$\mathbf{L = \int_a^b |\vec{r}'(t)| \, dt = \int_a^b \sqrt{[f'(t)]^2 + [g'(t)]^2 + [h'(t)]^2} \, dt}$$

In differential notation:
$$ds = |\vec{r}'(t)| \, dt = \sqrt{dx^2 + dy^2 + dz^2}$$

---

### 2. The Arc Length Function

Let $t_0$ be a chosen reference starting point on the curve. The **arc length function** $s(t)$ measures the directed distance along the curve from $\vec{r}(t_0)$ to $\vec{r}(t)$:

$$\mathbf{s(t) = \int_{t_0}^t |\vec{r}'(u)| \, du}$$

By the Fundamental Theorem of Calculus, the rate of change of arc length with respect to the parameter $t$ is:

$$\frac{ds}{dt} = |\vec{r}'(t)| = v(t)$$

where $v(t)$ is the **speed** of the trajectory. Since the curve is smooth ($|\vec{r}'(t)| > 0$), $\frac{ds}{dt} > 0$ strictly, meaning $s(t)$ is a strictly monotonically increasing function of $t$.

---

### 3. Arc Length Parameterization (Natural Parameter)

Because $s(t)$ is strictly increasing, it has a unique inverse function $t = t(s)$. We can reparameterize the curve in terms of the arc length $s$ by composing:

$$\vec{r}_1(s) = \vec{r}(t(s))$$

**Theorem (Unit Speed Property of Arc Length Parameterization):**  
If a curve is parameterized by its arc length $s$, then its tangent vector has unit length everywhere:

$$\left| \frac{d\vec{r}}{ds} \right| = 1 \quad \forall s$$

#### Proof:
By the Chain Rule:
$$\frac{d\vec{r}}{ds} = \frac{d\vec{r}}{dt} \frac{dt}{ds} = \vec{r}'(t) \frac{1}{ds/dt} = \frac{\vec{r}'(t)}{|\vec{r}'(t)|} = \vec{T}(t)$$

Taking the norm:
$$\left| \frac{d\vec{r}}{ds} \right| = |\vec{T}(t)| = 1 \quad \blacksquare$$

Arc length parameterization is termed the **intrinsic** or **natural parameterization** of the curve because it depends solely on the curve's geometric shape and is entirely independent of any artificial choice of time or velocity."""
            }
        ],
        "simulations": [
            {
                "id": "sim_calc3_space_curves",
                "title": "3D Space Curves & Velocity Vector Engine",
                "description": "Visualize 3D trajectories (circular helix, twisted cubic, conical spiral). Trace tangent velocity vectors, arc length progress, and orbit around the 3D space curve in real time.",
                "controls": [
                    {"param": "curveType", "label": "Curve (0:Helix, 1:Cubic, 2:Cone)", "min": 0, "max": 2, "step": 1, "default": 0},
                    {"param": "tParam", "label": "Curve Parameter t", "min": 0.0, "max": 6.28, "step": 0.05, "default": 2.5},
                    {"param": "helixRadius", "label": "Radius / Scale a", "min": 1.0, "max": 4.0, "step": 0.2, "default": 2.5},
                    {"param": "rotY", "label": "Orbit Yaw (°)", "min": -180, "max": 180, "step": 2, "default": 35}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-calc3-1-1",
                "tier": 1,
                "title": "Tangent Line and Unit Tangent of the Twisted Cubic",
                "statement": r"""Consider the twisted cubic space curve given by:
$$\vec{r}(t) = \langle t, \; t^2, \; t^3 \rangle$$
(a) Find the derivative vector $\vec{r}'(t)$ and the unit tangent vector $\vec{T}(t)$ at $t = 1$.  
(b) Find the parametric equations of the tangent line to the curve at the point corresponding to $t = 1$.""",
                "solution": r"""**Part (a): Compute $\vec{r}'(t)$ and $\vec{T}(1)$**  
Differentiating componentwise:
$$\vec{r}'(t) = \frac{d}{dt}\langle t, \; t^2, \; t^3 \rangle = \langle 1, \; 2t, \; 3t^2 \rangle$$

Evaluate at $t = 1$:
$$\vec{r}'(1) = \langle 1, \; 2(1), \; 3(1^2) \rangle = \langle 1, \; 2, \; 3 \rangle$$

The speed (magnitude of the velocity) at $t = 1$ is:
$$|\vec{r}'(1)| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}$$

The unit tangent vector is:
$$\vec{T}(1) = \frac{\vec{r}'(1)}{|\vec{r}'(1)|} = \frac{1}{\sqrt{14}}\langle 1, \; 2, \; 3 \rangle = \left\langle \frac{1}{\sqrt{14}}, \; \frac{2}{\sqrt{14}}, \; \frac{3}{\sqrt{14}} \right\rangle$$

---

**Part (b): Parametric Equations of the Tangent Line**  
The point on the curve at $t = 1$ is:
$$\vec{r}(1) = \langle 1, \; 1^2, \; 1^3 \rangle = (1, 1, 1)$$

Using direction ratios $(1, 2, 3)$ with parameter $\tau \in \mathbb{R}$:
$$\vec{L}(\tau) = \vec{r}(1) + \tau \vec{r}'(1) = \langle 1 + \tau, \; 1 + 2\tau, \; 1 + 3\tau \rangle$$

In scalar parametric form:
$$\begin{cases} x = 1 + \tau \\ y = 1 + 2\tau \\ z = 1 + 3\tau \end{cases}$$"""
            },
            {
                "id": "prob-calc3-1-2",
                "tier": 2,
                "title": "Arc Length and Natural Reparameterization of a Circular Helix",
                "statement": r"""A circular helix is described by:
$$\vec{r}(t) = \langle a\cos t, \; a\sin t, \; bt \rangle \quad (a > 0, \; b > 0)$$
(a) Find the total arc length of one full turn of the helix ($0 \le t \le 2\pi$).  
(b) Find the arc length function $s(t)$ measured from $t_0 = 0$.  
(c) Reparameterize the helix in terms of the arc length parameter $s$, and verify that $|\frac{d\vec{r}}{ds}| = 1$.""",
                "solution": r"""**Part (a): Arc Length of One Turn**  
Differentiate the position vector:
$$\vec{r}'(t) = \langle -a\sin t, \; a\cos t, \; b \rangle$$

Compute the magnitude:
$$|\vec{r}'(t)| = \sqrt{(-a\sin t)^2 + (a\cos t)^2 + b^2} = \sqrt{a^2(\sin^2 t + \cos^2 t) + b^2} = \sqrt{a^2 + b^2}$$
Notice that $|\vec{r}'(t)| = \sqrt{a^2 + b^2}$ is **constant** for all $t$!

The arc length for one turn ($0 \le t \le 2\pi$) is:
$$L = \int_0^{2\pi} |\vec{r}'(t)| \, dt = \int_0^{2\pi} \sqrt{a^2 + b^2} \, dt = 2\pi\sqrt{a^2 + b^2}$$

---

**Part (b): Arc Length Function $s(t)$**  
Taking $t_0 = 0$:
$$s(t) = \int_0^t |\vec{r}'(u)| \, du = \int_0^t \sqrt{a^2 + b^2} \, du = t\sqrt{a^2 + b^2}$$

---

**Part (c): Reparameterization by Arc Length $s$**  
Solve for $t$ in terms of $s$:
$$t = \frac{s}{\sqrt{a^2 + b^2}}$$

Substitute this expression for $t$ into $\vec{r}(t)$:
$$\vec{r}(s) = \left\langle a\cos\left(\frac{s}{\sqrt{a^2 + b^2}}\right), \; a\sin\left(\frac{s}{\sqrt{a^2 + b^2}}\right), \; \frac{bs}{\sqrt{a^2 + b^2}} \right\rangle$$

**Verification of Unit Speed:**  
Differentiate with respect to $s$:
$$\frac{d\vec{r}}{ds} = \left\langle -\frac{a}{\sqrt{a^2 + b^2}}\sin\left(\frac{s}{\sqrt{a^2 + b^2}}\right), \; \frac{a}{\sqrt{a^2 + b^2}}\cos\left(\frac{s}{\sqrt{a^2 + b^2}}\right), \; \frac{b}{\sqrt{a^2 + b^2}} \right\rangle$$

Compute the magnitude:
$$\left| \frac{d\vec{r}}{ds} \right| = \sqrt{ \frac{a^2}{a^2 + b^2}\sin^2(\dots) + \frac{a^2}{a^2 + b^2}\cos^2(\dots) + \frac{b^2}{a^2 + b^2} }$$
$$= \sqrt{\frac{a^2 + b^2}{a^2 + b^2}} = \sqrt{1} = 1 \quad \checkmark$$

The curve is strictly unit speed when parameterized by $s$."""
            },
            {
                "id": "prob-calc3-1-3",
                "tier": 3,
                "title": "Kinematic Orthogonality Proof and Expanding Exponential Spiral",
                "statement": r"""(a) Prove analytically that if a particle moves along a smooth curve with constant speed $v(t) = |\vec{v}(t)| \equiv c$, then its velocity vector $\vec{v}(t)$ and acceleration vector $\vec{a}(t)$ are mutually orthogonal for all $t$.  
(b) Consider a particle moving along the expanding space spiral:
$$\vec{r}(t) = \langle e^t\cos t, \; e^t\sin t, \; e^t \rangle$$
Find the velocity $\vec{v}(t)$, acceleration $\vec{a}(t)$, speed $v(t)$, and show that the angle between velocity and acceleration is constant for all $t \in \mathbb{R}$.""",
                "solution": r"""**Part (a): Constant Speed Implies Orthogonality**  
Let $\vec{v}(t) = \vec{r}'(t)$ and $\vec{a}(t) = \vec{v}'(t) = \vec{r}''(t)$.  
By definition, speed is:
$$v(t)^2 = \vec{v}(t) \cdot \vec{v}(t) = c^2$$

Differentiating both sides with respect to $t$:
$$\frac{d}{dt}[\vec{v}(t) \cdot \vec{v}(t)] = \frac{d}{dt}[c^2]$$
$$\vec{v}'(t) \cdot \vec{v}(t) + \vec{v}(t) \cdot \vec{v}'(t) = 0$$
$$2(\vec{v}(t) \cdot \vec{a}(t)) = 0 \implies \vec{v}(t) \cdot \vec{a}(t) = 0$$

Thus, velocity and acceleration are strictly perpendicular whenever speed is constant. $\blacksquare$

---

**Part (b): Expanding Spiral Analysis**  
Differentiate $\vec{r}(t) = \langle e^t\cos t, \; e^t\sin t, \; e^t \rangle$ using the product rule:
$$\vec{v}(t) = \vec{r}'(t) = \langle e^t\cos t - e^t\sin t, \; e^t\sin t + e^t\cos t, \; e^t \rangle$$
$$\vec{v}(t) = e^t \langle \cos t - \sin t, \; \sin t + \cos t, \; 1 \rangle$$

Now compute speed $v(t) = |\vec{v}(t)|$:
$$|\vec{v}(t)|^2 = e^{2t} \left[ (\cos t - \sin t)^2 + (\sin t + \cos t)^2 + 1^2 \right]$$
$$= e^{2t} \left[ (\cos^2 t - 2\sin t\cos t + \sin^2 t) + (\sin^2 t + 2\sin t\cos t + \cos^2 t) + 1 \right]$$
$$= e^{2t} [ 1 + 1 + 1 ] = 3e^{2t}$$

$$\mathbf{v(t) = \sqrt{3} e^t}$$

Next, differentiate $\vec{v}(t)$ to find acceleration $\vec{a}(t)$:
$$\vec{a}(t) = \vec{v}'(t) = \frac{d}{dt} \langle e^t(\cos t - \sin t), \; e^t(\sin t + \cos t), \; e^t \rangle$$
For the $x$-component:
$$\frac{d}{dt}[e^t(\cos t - \sin t)] = e^t(\cos t - \sin t) + e^t(-\sin t - \cos t) = -2e^t\sin t$$
For the $y$-component:
$$\frac{d}{dt}[e^t(\sin t + \cos t)] = e^t(\sin t + \cos t) + e^t(\cos t - \sin t) = 2e^t\cos t$$
For the $z$-component:
$$\frac{d}{dt}[e^t] = e^t$$

Thus:
$$\mathbf{\vec{a}(t) = e^t \langle -2\sin t, \; 2\cos t, \; 1 \rangle}$$

Compute magnitude of acceleration:
$$|\vec{a}(t)|^2 = e^{2t} [ 4\sin^2 t + 4\cos^2 t + 1 ] = e^{2t}[4(1) + 1] = 5e^{2t}$$
$$|\vec{a}(t)| = \sqrt{5} e^t$$

Now compute the dot product $\vec{v}(t) \cdot \vec{a}(t)$:
$$\vec{v} \cdot \vec{a} = e^{2t} [ (\cos t - \sin t)(-2\sin t) + (\sin t + \cos t)(2\cos t) + 1(1) ]$$
$$= e^{2t} [ -2\sin t\cos t + 2\sin^2 t + 2\sin t\cos t + 2\cos^2 t + 1 ]$$
$$= e^{2t} [ 2(\sin^2 t + \cos^2 t) + 1 ] = e^{2t} [ 2(1) + 1 ] = 3e^{2t}$$

Finally, compute the angle $\theta$ between velocity and acceleration:
$$\cos\theta = \frac{\vec{v} \cdot \vec{a}}{|\vec{v}| |\vec{a}|} = \frac{3e^{2t}}{(\sqrt{3}e^t)(\sqrt{5}e^t)} = \frac{3}{\sqrt{15}} = \sqrt{\frac{3}{5}}$$

$$\mathbf{\theta = \arccos\left(\sqrt{\frac{3}{5}}\right) \approx 39.23^\circ}$$

Since $\cos\theta$ is completely independent of $t$, the angle between velocity and acceleration remains invariant for all time! $\blacksquare$"""
            }
        ]
    }

def build_unit_2():
    return {
        "id": "calc3-u2",
        "title": "Unit 2: Curvature, Torsion & The Frenet-Serret Frame",
        "description": "Exhaustive treatment of differential geometry of space curves: the TNB moving trihedron, general parametric and Cartesian curvature formulas, osculating circles, evolutes, torsion, and the Frenet-Serret equations.",
        "sections": [
            {
                "id": "u2-sec1",
                "title": "The Moving Trihedron (TNB Frame) and Fundamental Planes",
                "content": r"""At each point along a smooth curve $C$ in $\mathbb{R}^3$, we can attach a moving, right-handed orthonormal coordinate system known as the **Frenet-Serret Moving Trihedron** (or **TNB Frame**).

---

### 1. Construction of the TNB Frame

1. **Unit Tangent Vector $\vec{T}(t)$:**  
   Points in the instantaneous direction of motion:
   $$\mathbf{\vec{T}(t) = \frac{\vec{r}'(t)}{|\vec{r}'(t)|}}$$

2. **Principal Unit Normal Vector $\vec{N}(t)$:**  
   Because $|\vec{T}(t)| = 1$ is constant, $\vec{T}'(t)$ is orthogonal to $\vec{T}(t)$ ($\vec{T} \cdot \vec{T}' = 0$). The unit vector in this orthogonal direction is:
   $$\mathbf{\vec{N}(t) = \frac{\vec{T}'(t)}{|\vec{T}'(t)|}}$$
   $\vec{N}(t)$ points directly in the direction that the curve is turning.

3. **Binormal Unit Vector $\vec{B}(t)$:**  
   Defined by the vector cross product to complete a right-handed orthonormal triad:
   $$\mathbf{\vec{B}(t) = \vec{T}(t) \times \vec{N}(t)}$$
   Because $\vec{T}$ and $\vec{N}$ are orthogonal unit vectors, $|\vec{B}| = |\vec{T}| |\vec{N}| \sin(\pi/2) = 1$, and $\vec{B}$ is perpendicular to both $\vec{T}$ and $\vec{N}$.

---

### 2. The Three Fundamental Osculating Planes

At any point $P$ on the curve, the three mutually orthogonal pairs of vectors define three fundamental planes:

1. **The Osculating Plane (Spanned by $\vec{T}$ and $\vec{N}$):**  
   - Normal Vector: $\vec{B}(t)$  
   - Equation: $(\vec{r} - \vec{r}_0) \cdot \vec{B} = 0$  
   - Geometric Meaning: The plane that comes closest to containing the curve locally; it contains the instantaneous circle of curvature.

2. **The Normal Plane (Spanned by $\vec{N}$ and $\vec{B}$):**  
   - Normal Vector: $\vec{T}(t)$  
   - Equation: $(\vec{r} - \vec{r}_0) \cdot \vec{T} = 0$  
   - Geometric Meaning: The plane orthogonal to the curve; all lines normal to the curve lie in this plane.

3. **The Rectifying Plane (Spanned by $\vec{T}$ and $\vec{B}$):**  
   - Normal Vector: $\vec{N}(t)$  
   - Equation: $(\vec{r} - \vec{r}_0) \cdot \vec{N} = 0$"""
            },
            {
                "id": "u2-sec2",
                "title": "Curvature Formulas, Radius of Curvature and Osculating Circles",
                "content": r"""### 1. Geometric Definition of Curvature $\kappa$

The **curvature** $\kappa$ of a smooth curve measures how rapidly the curve changes its direction per unit change in arc length:

$$\mathbf{\kappa = \left| \frac{d\vec{T}}{ds} \right|}$$

Using the chain rule with parameter $t$:
$$\frac{d\vec{T}}{ds} = \frac{d\vec{T}/dt}{ds/dt} = \frac{\vec{T}'(t)}{|\vec{r}'(t)|} \implies \mathbf{\kappa = \frac{|\vec{T}'(t)|}{|\vec{r}'(t)|}}$$

---

### 2. General Parametric Curvature Formula in $\mathbb{R}^3$

**Theorem:**  
For any smooth space curve parameterized by $\vec{r}(t)$:

$$\mathbf{\kappa(t) = \frac{|\vec{r}'(t) \times \vec{r}''(t)|}{|\vec{r}'(t)|^3}}$$

#### Proof:
Since $\vec{v}(t) = \vec{r}'(t) = v \vec{T}$ where $v = |\vec{r}'(t)| = \frac{ds}{dt}$:
Differentiating velocity to get acceleration:
$$\vec{r}''(t) = \frac{d}{dt}[v \vec{T}] = v' \vec{T} + v \vec{T}'(t)$$

Since $\frac{d\vec{T}}{ds} = \kappa \vec{N} \implies \vec{T}'(t) = \frac{ds}{dt} \frac{d\vec{T}}{ds} = v \kappa \vec{N}$:
$$\vec{r}''(t) = v' \vec{T} + \kappa v^2 \vec{N}$$

Now compute the cross product $\vec{r}'(t) \times \vec{r}''(t)$:
$$\vec{r}' \times \vec{r}'' = (v \vec{T}) \times (v' \vec{T} + \kappa v^2 \vec{N}) = v v' (\vec{T} \times \vec{T}) + \kappa v^3 (\vec{T} \times \vec{N})$$
Since $\vec{T} \times \vec{T} = \vec{0}$ and $\vec{T} \times \vec{N} = \vec{B}$:
$$\vec{r}'(t) \times \vec{r}''(t) = \kappa v^3 \vec{B}$$

Taking the norm of both sides (since $|\vec{B}| = 1$):
$$|\vec{r}' \times \vec{r}''| = \kappa v^3 |\vec{B}| = \kappa |\vec{r}'|^3$$

Dividing by $|\vec{r}'|^3$:
$$\kappa = \frac{|\vec{r}' \times \vec{r}''|}{|\vec{r}'|^3} \quad \blacksquare$$

---

### 3. Special Curvature Formulas

1. **Plane Curve in Cartesian Form $y = f(x)$:**  
   Parameterize as $\vec{r}(x) = \langle x, \; f(x), \; 0 \rangle$.  
   Then $\vec{r}'(x) = \langle 1, \; y', \; 0 \rangle$ and $\vec{r}''(x) = \langle 0, \; y'', \; 0 \rangle$.  
   $\vec{r}' \times \vec{r}'' = \langle 0, \; 0, \; y'' \rangle \implies |\vec{r}' \times \vec{r}''| = |y''|$.  
   $|\vec{r}'| = \sqrt{1 + y'^2}$.
   $$\mathbf{\kappa(x) = \frac{|y''|}{(1 + y'^2)^{3/2}}}$$

2. **Plane Curve in Polar Coordinates $r = f(\theta)$:**  
   $$\mathbf{\kappa(\theta) = \frac{|r^2 + 2r'^2 - r r''|}{(r^2 + r'^2)^{3/2}}}$$

---

### 4. Radius of Curvature, Center of Curvature and Evolutes

- **Radius of Curvature $\rho$:** The reciprocal of curvature:
  $$\rho = \frac{1}{\kappa}$$
- **Osculating Circle (Circle of Curvature):** The circle in the osculating plane that has the same tangent, normal, and curvature as the curve at that point. Its radius is $\rho$.
- **Center of Curvature $(\alpha, \beta)$ for plane curves:**
  $$\alpha = x - \frac{y'(1 + y'^2)}{y''}, \qquad \beta = y + \frac{1 + y'^2}{y''}$$
- **Evolute:** The locus of the centers of curvature of a given curve is called its **evolute**."""
            },
            {
                "id": "u2-sec3",
                "title": "Torsion, the Frenet-Serret Formulas & Acceleration Components",
                "content": r"""### 1. Torsion $\tau$ of a Space Curve

While curvature $\kappa$ measures the rate at which $\vec{T}$ turns away from the tangent line, **torsion** $\tau$ measures how sharply the space curve twists out of its osculating plane.

Because $\vec{B}(s) \cdot \vec{B}(s) = 1$, $\frac{d\vec{B}}{ds}$ is perpendicular to $\vec{B}$. Furthermore, differentiating $\vec{B} \cdot \vec{T} = 0$:

$$\frac{d\vec{B}}{ds} \cdot \vec{T} + \vec{B} \cdot \frac{d\vec{T}}{ds} = 0 \implies \frac{d\vec{B}}{ds} \cdot \vec{T} + \vec{B} \cdot (\kappa\vec{N}) = 0 \implies \frac{d\vec{B}}{ds} \cdot \vec{T} = 0$$

Thus, $\frac{d\vec{B}}{ds}$ is perpendicular to both $\vec{B}$ and $\vec{T}$, which means it must be parallel to $\vec{N}$. We define the scalar **torsion** $\tau$ by:

$$\mathbf{\frac{d\vec{B}}{ds} = -\tau \vec{N}}$$

The negative sign is conventional so that a right-handed screw has positive torsion.

#### General Parametric Formula for Torsion:
$$\mathbf{\tau(t) = \frac{(\vec{r}'(t) \times \vec{r}''(t)) \cdot \vec{r}'''(t)}{|\vec{r}'(t) \times \vec{r}''(t)|^2}}$$

> **Criterion for Planar Curves:**  
> A space curve is a plane curve if and only if $\tau(t) \equiv 0$ for all $t$.

---

### 2. The Complete Frenet-Serret Formulas

The rate of change of the moving frame $\{\vec{T}, \vec{N}, \vec{B}\}$ with respect to arc length $s$ is governed by the celebrated **Frenet-Serret Formulas**:

$$\mathbf{\begin{cases}
\dfrac{d\vec{T}}{ds} = \kappa \vec{N} \\
\dfrac{d\vec{N}}{ds} = -\kappa \vec{T} + \tau \vec{B} \\
\dfrac{d\vec{B}}{ds} = -\tau \vec{N}
\end{cases}}$$

In matrix notation:
$$\begin{bmatrix} d\vec{T}/ds \\ d\vec{N}/ds \\ d\vec{B}/ds \end{bmatrix} = \begin{bmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{bmatrix} \begin{bmatrix} \vec{T} \\ \vec{N} \\ \vec{B} \end{bmatrix}$$

Notice that the coefficient matrix (the **Darboux matrix**) is skew-symmetric, which is a mathematical guarantee that the orthonormal nature of the basis is preserved along the entire curve.

---

### 3. Tangential and Normal Components of Acceleration

In physical kinematics, the acceleration of a particle can be decomposed uniquely into orthogonal components along the tangent and principal normal:

$$\mathbf{\vec{a} = a_T \vec{T} + a_N \vec{N}}$$

where:
- **Tangential Acceleration:** Rate of change of speed:
  $$a_T = \frac{dv}{dt} = v' = \frac{\vec{r}'(t) \cdot \vec{r}''(t)}{|\vec{r}'(t)|}$$
- **Normal (Centripetal) Acceleration:** Tendency to change direction:
  $$a_N = \kappa v^2 = \frac{|\vec{r}'(t) \times \vec{r}''(t)|}{|\vec{r}'(t)|}$$

Notice that the binormal component of acceleration is always identically zero ($a_B = 0$). Acceleration always lies entirely in the osculating plane!"""
            }
        ],
        "simulations": [
            {
                "id": "sim_calc3_curvature",
                "title": "Osculating Circle & Frenet-Serret TNB Frame Engine",
                "description": "Watch the moving Frenet-Serret trihedron (T in sky blue, N in emerald, B in rose) and the dynamic osculating circle track smoothly along a 3D curve with live curvature and radius readouts.",
                "controls": [
                    {"param": "curveChoice", "label": "Curve (0:Helix, 1:Parabola, 2:Torus)", "min": 0, "max": 2, "step": 1, "default": 0},
                    {"param": "tPos", "label": "Curve Position t", "min": 0.0, "max": 6.28, "step": 0.05, "default": 1.8},
                    {"param": "torsionScale", "label": "Helix Pitch / Depth", "min": 0.5, "max": 3.0, "step": 0.2, "default": 1.2},
                    {"param": "rotY", "label": "Orbit Yaw (°)", "min": -180, "max": 180, "step": 2, "default": 40}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-calc3-2-1",
                "tier": 1,
                "title": "Curvature and Osculating Circle of a Parabola at its Vertex",
                "statement": r"""Find the curvature $\kappa$, radius of curvature $\rho$, and center of curvature of the parabola $y = x^2$ at its vertex $(0, 0)$.""",
                "solution": r"""**Step 1: Compute derivatives of $y = x^2$**  
$$y' = \frac{dy}{dx} = 2x$$
$$y'' = \frac{d^2y}{dx^2} = 2$$

At the vertex $x = 0$:
$$y'(0) = 0, \qquad y''(0) = 2$$

---

**Step 2: Compute curvature $\kappa$**  
Using the Cartesian curvature formula:
$$\kappa(x) = \frac{|y''|}{(1 + y'^2)^{3/2}}$$

Substitute $x = 0$:
$$\kappa(0) = \frac{|2|}{(1 + 0^2)^{3/2}} = \frac{2}{1} = 2$$

---

**Step 3: Compute radius of curvature $\rho$**  
$$\rho = \frac{1}{\kappa} = \frac{1}{2} = 0.5$$

---

**Step 4: Compute center of curvature $(\alpha, \beta)$**  
Using the center of curvature formulas:
$$\alpha = x - \frac{y'(1 + y'^2)}{y''} = 0 - \frac{0(1 + 0)}{2} = 0$$
$$\beta = y + \frac{1 + y'^2}{y''} = 0 + \frac{1 + 0}{2} = \frac{1}{2}$$

Thus, the center of curvature is $(0, 1/2)$.  
The equation of the osculating circle at the vertex is:
$$(x - 0)^2 + \left(y - \frac{1}{2}\right)^2 = \left(\frac{1}{2}\right)^2 \implies x^2 + \left(y - \frac{1}{2}\right)^2 = \frac{1}{4}$$"""
            },
            {
                "id": "prob-calc3-2-2",
                "tier": 2,
                "title": "Curvature and Evolute of the Canonical Ellipse",
                "statement": r"""For the canonical ellipse parameterized by:
$$\vec{r}(t) = \langle a\cos t, \; b\sin t, \; 0 \rangle \quad (a > b > 0)$$
(a) Find the curvature $\kappa(t)$ as an explicit function of parameter $t$.  
(b) Find the maximum and minimum curvatures and the points where they occur.  
(c) Deduce the radii of curvature at the major and minor vertices.""",
                "solution": r"""**Part (a): Compute Curvature Formula**  
Compute first and second derivatives:
$$\vec{r}'(t) = \langle -a\sin t, \; b\cos t, \; 0 \rangle$$
$$\vec{r}''(t) = \langle -a\cos t, \; -b\sin t, \; 0 \rangle$$

Compute the cross product $\vec{r}' \times \vec{r}''$:
$$\vec{r}' \times \vec{r}'' = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -a\sin t & b\cos t & 0 \\ -a\cos t & -b\sin t & 0 \end{vmatrix}$$
$$= \hat{k} [(-a\sin t)(-b\sin t) - (b\cos t)(-a\cos t)] = \hat{k} [ab\sin^2 t + ab\cos^2 t] = ab\hat{k}$$

Magnitude:
$$|\vec{r}' \times \vec{r}''| = ab$$

Now compute $|\vec{r}'(t)|$:
$$|\vec{r}'(t)| = \sqrt{a^2\sin^2 t + b^2\cos^2 t}$$

Thus, the curvature is:
$$\mathbf{\kappa(t) = \frac{ab}{(a^2\sin^2 t + b^2\cos^2 t)^{3/2}}}$$

---

**Part (b): Extreme Values of Curvature**  
Rewrite the denominator:
$$a^2\sin^2 t + b^2\cos^2 t = b^2 + (a^2 - b^2)\sin^2 t$$
Since $a > b$, this denominator is minimized when $\sin t = 0$ ($t = 0, \pi$) and maximized when $\sin^2 t = 1$ ($t = \pi/2, 3\pi/2$).

- **Maximum Curvature:** Occurs at $t = 0, \pi$ (vertices $(\pm a, 0)$):
  $$\kappa_{max} = \frac{ab}{(b^2)^{3/2}} = \frac{ab}{b^3} = \mathbf{\frac{a}{b^2}}$$
- **Minimum Curvature:** Occurs at $t = \pi/2, 3\pi/2$ (vertices $(0, \pm b)$):
  $$\kappa_{min} = \frac{ab}{(a^2)^{3/2}} = \frac{ab}{a^3} = \mathbf{\frac{b}{a^2}}$$

---

**Part (c): Radii of Curvature at Vertices**  
- At major vertices $(\pm a, 0)$: $\rho = \frac{1}{\kappa_{max}} = \mathbf{\frac{b^2}{a}}$.
- At minor vertices $(0, \pm b)$: $\rho = \frac{1}{\kappa_{min}} = \mathbf{\frac{a^2}{b}}$."""
            },
            {
                "id": "prob-calc3-2-3",
                "tier": 3,
                "title": "Complete Frenet-Serret Apparatus and Lancret Ratio for a Circular Helix",
                "statement": r"""For the general circular helix:
$$\vec{r}(t) = \langle a\cos t, \; a\sin t, \; bt \rangle \quad (a > 0, \; b > 0)$$
(a) Compute the complete Frenet-Serret apparatus: $\vec{T}(t), \vec{N}(t), \vec{B}(t)$, curvature $\kappa$, and torsion $\tau$.  
(b) Prove that both curvature and torsion are constant along the entire helix.  
(c) Verify Lancret's Theorem by demonstrating that the ratio $\tau / \kappa$ is constant, and determine the angle that the tangent vector makes with the $z$-axis.""",
                "solution": r"""**Part (a): Derivation of Frenet-Serret Vectors and Invariants**  
1. **Velocity and Unit Tangent:**
   $$\vec{r}'(t) = \langle -a\sin t, \; a\cos t, \; b \rangle, \qquad |\vec{r}'(t)| = \sqrt{a^2 + b^2}$$
   $$\mathbf{\vec{T}(t) = \frac{1}{\sqrt{a^2+b^2}} \langle -a\sin t, \; a\cos t, \; b \rangle}$$

2. **Principal Normal:**
   $$\vec{T}'(t) = \frac{1}{\sqrt{a^2+b^2}} \langle -a\cos t, \; -a\sin t, \; 0 \rangle$$
   $$|\vec{T}'(t)| = \frac{a}{\sqrt{a^2+b^2}}$$
   $$\mathbf{\vec{N}(t) = \frac{\vec{T}'}{|\vec{T}'|} = \langle -\cos t, \; -\sin t, \; 0 \rangle}$$
   Notice that $\vec{N}$ points horizontally toward the $z$-axis!

3. **Curvature:**
   $$\mathbf{\kappa = \frac{|\vec{T}'(t)|}{|\vec{r}'(t)|} = \frac{a/\sqrt{a^2+b^2}}{\sqrt{a^2+b^2}} = \frac{a}{a^2 + b^2}}$$

4. **Binormal Vector:**
   $$\vec{B}(t) = \vec{T}(t) \times \vec{N}(t) = \frac{1}{\sqrt{a^2+b^2}} \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -a\sin t & a\cos t & b \\ -\cos t & -\sin t & 0 \end{vmatrix}$$
   $$\vec{B}(t) = \frac{1}{\sqrt{a^2+b^2}} \left[ \hat{i}(b\sin t) - \hat{j}(-b\cos t) + \hat{k}(a\sin^2 t + a\cos^2 t) \right]$$
   $$\mathbf{\vec{B}(t) = \frac{1}{\sqrt{a^2+b^2}} \langle b\sin t, \; -b\cos t, \; a \rangle}$$

5. **Torsion:**
   Differentiate $\vec{B}(t)$ with respect to $t$:
   $$\vec{B}'(t) = \frac{1}{\sqrt{a^2+b^2}} \langle b\cos t, \; b\sin t, \; 0 \rangle = -\frac{b}{\sqrt{a^2+b^2}} \langle -\cos t, \; -\sin t, \; 0 \rangle = -\frac{b}{\sqrt{a^2+b^2}} \vec{N}(t)$$
   By the third Frenet-Serret relation, $\frac{d\vec{B}}{dt} = \frac{ds}{dt} \frac{d\vec{B}}{ds} = \sqrt{a^2+b^2}(-\tau \vec{N})$.  
   Equating:
   $$\sqrt{a^2+b^2}(-\tau \vec{N}) = -\frac{b}{\sqrt{a^2+b^2}} \vec{N} \implies \mathbf{\tau = \frac{b}{a^2 + b^2}}$$

---

**Part (b): Constancy of Invariants**  
$$\kappa = \frac{a}{a^2+b^2} = \text{const}, \qquad \tau = \frac{b}{a^2+b^2} = \text{const}$$
Since neither $\kappa$ nor $\tau$ contains the parameter $t$, both invariants are constant everywhere. $\blacksquare$

---

**Part (c): Lancret's Theorem and Axis Incline**  
Evaluate the ratio of torsion to curvature:
$$\frac{\tau}{\kappa} = \frac{b / (a^2+b^2)}{a / (a^2+b^2)} = \frac{b}{a} = \text{constant}$$
By **Lancret's Theorem (1806)**, a space curve is a general helix (its tangent vector makes a constant angle with a fixed direction) if and only if the ratio $\tau / \kappa$ is constant.

The angle $\phi$ between $\vec{T}$ and the $z$-axis ($\hat{k}$) is:
$$\cos\phi = \vec{T} \cdot \hat{k} = \frac{b}{\sqrt{a^2+b^2}} = \text{constant}$$
Thus, $\phi = \arccos\left(\frac{b}{\sqrt{a^2+b^2}}\right)$ is strictly constant along the entire curve. $\blacksquare$"""
            }
        ]
    }

if __name__ == "__main__":
    print("Building Calculus III: Units 1 & 2...")
    u1 = build_unit_1()
    with open("calc3_u1.json", "w", encoding="utf-8") as f:
        json.dump(u1, f, indent=2, ensure_ascii=False)
    print("Saved calc3_u1.json successfully.")

    u2 = build_unit_2()
    with open("calc3_u2.json", "w", encoding="utf-8") as f:
        json.dump(u2, f, indent=2, ensure_ascii=False)
    print("Saved calc3_u2.json successfully.")
