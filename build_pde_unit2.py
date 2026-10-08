# -*- coding: utf-8 -*-
"""
build_pde_unit2.py
Constructs Unit 2: The Cauchy Problem, Method of Characteristics & Non-Linear First-Order PDEs
Strictly ZERO course numbers.
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "The Cauchy Problem, Method of Characteristics & Non-Linear First-Order PDEs",
        "leadSummary": "Advanced theory of first-order PDEs: the Cauchy problem and local existence-uniqueness theorems, characteristic strips in contact space, shock wave formation in quasilinear conservation laws and the Rankine-Hugoniot condition, Monge cones and contact elements, Charpit's method for fully non-linear equations F(x, y, z, p, q) = 0, and the four classical standard forms.",
        "simulations": ["sim_pde_charpit_monge_cone"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "The Cauchy Problem for Quasilinear Equations & Local Existence-Uniqueness",
                "content": r"""### 1. Rigorous Formulation of the Cauchy Problem

Consider the quasilinear partial differential equation:
$$P(x, y, z) \frac{\partial z}{\partial x} + Q(x, y, z) \frac{\partial z}{\partial y} = R(x, y, z)$$
on an open domain $\Omega \subseteq \mathbb{R}^2$. Let $\Gamma \subset \mathbb{R}^3$ be a simple regular $C^1$ space curve parametrized by arc parameter $s \in [a, b]$:
$$\Gamma: \quad x = x_0(s), \quad y = y_0(s), \quad z = z_0(s)$$
The **Cauchy problem** consists in determining a $C^1$ surface $z = u(x, y)$ defined on a neighborhood of the projection curve $\gamma_0 = (x_0(s), y_0(s))$ such that:
1. $u(x, y)$ satisfies the PDE on $\Omega$: $P(x, y, u) u_x + Q(x, y, u) u_y = R(x, y, u)$.
2. The surface contains $\Gamma$: $u(x_0(s), y_0(s)) = z_0(s)$ for all $s \in [a, b]$.

---

### 2. Characteristic System and Coordinate Transformation

To solve the Cauchy problem, we construct the characteristic curves emanating from each point of $\Gamma$. For each fixed $s$, consider the initial value problem for the autonomous ODE system:
$$\begin{cases}
\frac{\partial X}{\partial t}(s, t) = P(X(s, t), Y(s, t), Z(s, t)), & X(s, 0) = x_0(s) \\
\frac{\partial Y}{\partial t}(s, t) = Q(X(s, t), Y(s, t), Z(s, t)), & Y(s, 0) = y_0(s) \\
\frac{\partial Z}{\partial t}(s, t) = R(X(s, t), Y(s, t), Z(s, t)), & Z(s, 0) = z_0(s)
\end{cases}$$
By the Picard-Lindelöf theorem for ODEs, since $P, Q, R$ are $C^1$, this system possesses a unique local solution $(X(s, t), Y(s, t), Z(s, t))$ defined for $(s, t) \in [a, b] \times (-\delta, \delta)$.

---

### 3. The Local Existence and Uniqueness Theorem

> **Theorem 2.1 (Cauchy-Kovalevskaya Local Existence for Quasilinear First-Order PDEs):**
> Let $P, Q, R \in C^1(\mathbb{R}^3)$ and let $\Gamma = (x_0(s), y_0(s), z_0(s))$ be a $C^1$ curve. Suppose that at $s = s_0$:
> $$J(s_0) = \left. \frac{\partial(X, Y)}{\partial(s, t)} \right|_{t=0} = x_0'(s_0) Q(x_0(s_0), y_0(s_0), z_0(s_0)) - y_0'(s_0) P(x_0(s_0), y_0(s_0), z_0(s_0)) \ne 0$$
> Then there exists an open neighborhood $U$ of $(x_0(s_0), y_0(s_0))$ in $\mathbb{R}^2$ containing a unique $C^1$ function $z = u(x, y)$ solving the Cauchy problem.

*Proof:*
Consider the planar mapping $\Phi: (s, t) \mapsto (X(s, t), Y(s, t))$.
At $t = 0$, the Jacobian matrix of $\Phi$ is:
$$D\Phi(s, 0) = \begin{pmatrix} X_s(s, 0) & X_t(s, 0) \\ Y_s(s, 0) & Y_t(s, 0) \end{pmatrix} = \begin{pmatrix} x_0'(s) & P(x_0, y_0, z_0) \\ y_0'(s) & Q(x_0, y_0, z_0) \end{pmatrix}$$
Its determinant is precisely:
$$\det D\Phi(s_0, 0) = x_0'(s_0) Q(x_0, y_0, z_0) - y_0'(s_0) P(x_0, y_0, z_0) = J(s_0) \ne 0$$
By the **Inverse Function Theorem**, $\Phi$ is a local $C^1$-diffeomorphism from an open neighborhood $V$ of $(s_0, 0)$ onto an open neighborhood $U$ of $(x_0(s_0), y_0(s_0))$.
Thus, we can invert the mapping smoothly:
$$s = S(x, y), \qquad t = T(x, y)$$
Now define the candidate solution surface by:
$$u(x, y) = Z(S(x, y), T(x, y))$$
Along the initial curve ($t = 0$), $u(x_0(s), y_0(s)) = Z(s, 0) = z_0(s)$, satisfying the initial condition.
To verify that $u$ satisfies the PDE, differentiate $Z(s, t) = u(X(s, t), Y(s, t))$ with respect to $t$:
$$Z_t = u_x X_t + u_y Y_t$$
Since $(X, Y, Z)$ are characteristic trajectories, $X_t = P, Y_t = Q, Z_t = R$:
$$R = u_x P + u_y Q \implies P u_x + Q u_y = R$$
Hence, $u(x, y)$ is a genuine $C^1$ solution. Uniqueness follows because any integral surface containing $\Gamma$ must contain all characteristic curves issuing from $\Gamma$. $\blacksquare$"""
            },
            {
                "secNumber": "2.2",
                "title": "Characteristic Curves, Characteristic Strips & Shock Waves",
                "content": r"""### 1. Wave Steepening in Nonlinear Conservation Laws

Consider the inviscid **Burgers equation**, the prototype for nonlinear wave propagation and gas dynamics:
$$u_t + u u_x = 0, \qquad x \in \mathbb{R}, \quad t > 0$$
subject to initial profile $u(x, 0) = f(x)$.

The characteristic equations are:
$$\frac{dt}{d\tau} = 1, \qquad \frac{dx}{d\tau} = u, \qquad \frac{du}{d\tau} = 0$$
Along a characteristic trajectory issuing from $(x_0, 0)$:
1. $u(x, t) = f(x_0)$ is **constant** along each characteristic.
2. The characteristic curve is a straight line in the $(x, t)$ plane:
   $$x(t) = x_0 + f(x_0) t$$
Thus, points with higher values of $u$ travel with greater speed $c = u$.

---

### 2. Gradient Catastrophe and Shock Formation Time

Differentiating the implicit relation $u = f(x - u t)$ with respect to $x$:
$$u_x = f'(x - u t) \cdot (1 - u_x t) \implies u_x [1 + t f'(x - u t)] = f'(x - u t)$$
Solving for the spatial gradient $u_x$:
$$u_x(x, t) = \frac{f'(x_0)}{1 + t f'(x_0)}$$

> **Theorem 2.2 (Gradient Catastrophe / Breaking Time):**
> If $f'(x_0) \ge 0$ for all $x_0 \in \mathbb{R}$ (rarefaction / expansion profile), characteristics diverge forward in time and the classical $C^1$ solution exists for all $t > 0$.
> If there exists any point $x_0$ where $f'(x_0) < 0$ (compressive profile), the denominator vanishes at a finite time. The earliest such time, called the **breaking time** (or **shock formation time**), is given by:
> $$t_{\text{shock}} = \frac{1}{\max_{x_0 \in \mathbb{R}} (-f'(x_0))} = -\frac{1}{\min_{x_0} f'(x_0)} > 0$$
> At $t = t_{\text{shock}}$, the gradient $u_x \to -\infty$, characteristics intersect, and the single-valued classical solution ceases to exist.

---

### 3. Weak Solutions and the Rankine-Hugoniot Condition

Beyond $t > t_{\text{shock}}$, physics dictates the formation of a **shock wave**: a propagating jump discontinuity across a curve $x = s(t)$.

> **Definition 2.1 (Rankine-Hugoniot Jump Condition):**
> For a scalar conservation law $u_t + (f(u))_x = 0$, the propagation speed $\dot{s}(t) = \frac{ds}{dt}$ of a discontinuity separating state $u_L$ on the left and $u_R$ on the right satisfies:
> $$\frac{ds}{dt} = \frac{[f(u)]}{[u]} = \frac{f(u_L) - f(u_R)}{u_L - u_R}$$
> For Burgers' equation $f(u) = \frac{1}{2}u^2$:
> $$\frac{ds}{dt} = \frac{\frac{1}{2}u_L^2 - \frac{1}{2}u_R^2}{u_L - u_R} = \frac{u_L + u_R}{2}$$
> The shock speed is the arithmetic mean of the states immediately to its left and right."""
            },
            {
                "secNumber": "2.3",
                "title": "Non-Linear First-Order Equations: Contact Elements and Monge Cones",
                "content": r"""### 1. Contact Elements and the Geometry of Solution Surfaces

Let $F(x, y, z, p, q) = 0$ be a general non-linear first-order PDE.
At any point $P_0(x_0, y_0, z_0)$, a planar element through $P_0$ is defined by:
$$Z - z_0 = p (X - x_0) + q (Y - y_0)$$
The set $(x_0, y_0, z_0, p, q)$ is called a **contact element** or **tangent element**.
For a fixed point $(x_0, y_0, z_0)$, the PDE $F(x_0, y_0, z_0, p, q) = 0$ is a relation between $p$ and $q$. Thus, at each point, there is not a single tangent plane (as in linear PDEs), but a **one-parameter family of tangent planes**:
$$Z - z_0 = p(t) (X - x_0) + q(t) (Y - y_0)$$
where $F(x_0, y_0, z_0, p(t), q(t)) = 0$.

---

### 2. The Monge Cone

> **Definition 2.2 (Monge Cone):**
> The envelope of this one-parameter family of tangent planes passing through $(x_0, y_0, z_0)$ is a cone with vertex at $(x_0, y_0, z_0)$, known as the **Monge cone**.
> Every integral surface $z = u(x, y)$ passing through $(x_0, y_0, z_0)$ must have a tangent plane that belongs to this family; consequently, the integral surface must be **tangent to the Monge cone** along a straight-line generator!

To determine the generators of the Monge cone, differentiate the tangent plane equation with respect to parameter $t$:
$$p'(t) (X - x_0) + q'(t) (Y - y_0) = 0$$
Differentiating $F(x_0, y_0, z_0, p(t), q(t)) = 0$ with respect to $t$:
$$F_p p'(t) + F_q q'(t) = 0 \implies \frac{p'(t)}{q'(t)} = -\frac{F_q}{F_p}$$
Substituting this into the envelope equation:
$$- F_q (X - x_0) + F_p (Y - y_0) = 0 \implies \frac{X - x_0}{F_p} = \frac{Y - y_0}{F_q}$$
Along this generator, the increment $dZ$ on the tangent plane is:
$$dZ = p\,dX + q\,dY = p \lambda F_p + q \lambda F_q = \lambda (p F_p + q F_q)$$
Therefore, the direction ratios of the generator of the Monge cone are:
$$dx : dy : dz = F_p : F_q : (p F_p + q F_q)$$
This direction is the **characteristic direction** for non-linear equations."""
            },
            {
                "secNumber": "2.4",
                "title": "Charpit's Method for General Non-Linear PDEs F(x, y, z, p, q) = 0",
                "content": r"""### 1. Compatibility and Charpit's Auxiliary Equations

Paul Charpit (1784) established the universal method for finding a complete integral of an arbitrary non-linear PDE $F(x, y, z, p, q) = 0$.
The foundational strategy is to seek a second relation:
$$\Phi(x, y, z, p, q) = a$$
such that $F = 0$ and $\Phi = a$ are **compatible**: that is, solving them simultaneously for $p$ and $q$:
$$p = p(x, y, z, a), \qquad q = q(x, y, z, a)$$
makes the Pfaffian differential form:
$$dz = p\,dx + q\,dy \quad \iff \quad dz - p\,dx - q\,dy = 0$$
an **exact (integrable) differential**.

By Frobenius' integrability theorem, the integrability condition is:
$$\frac{\partial p}{\partial y} + q \frac{\partial p}{\partial z} = \frac{\partial q}{\partial x} + p \frac{\partial q}{\partial z}$$

---

### 2. Complete Derivation of Charpit's System

Differentiating both $F(x, y, z, p, q) = 0$ and $\Phi(x, y, z, p, q) = a$ with respect to $x$ (treating $z$ as depending on $x, y$):
$$\begin{cases}
F_x + F_z p + F_p \frac{\partial p}{\partial x} + F_q \frac{\partial q}{\partial x} = 0 \\
\Phi_x + \Phi_z p + \Phi_p \frac{\partial p}{\partial x} + \Phi_q \frac{\partial q}{\partial x} = 0
\end{cases}$$
Similarly differentiating with respect to $y$:
$$\begin{cases}
F_y + F_z q + F_p \frac{\partial p}{\partial y} + F_q \frac{\partial q}{\partial y} = 0 \\
\Phi_y + \Phi_z q + \Phi_p \frac{\partial p}{\partial y} + \Phi_q \frac{\partial q}{\partial y} = 0
\end{cases}$$
Eliminating the mixed second derivatives $\frac{\partial p}{\partial x}, \frac{\partial q}{\partial x}, \frac{\partial p}{\partial y}, \frac{\partial q}{\partial y}$ using $\frac{\partial p}{\partial y} = \frac{\partial q}{\partial x}$ leads to the linear first-order PDE for $\Phi$:
$$-F_p \frac{\partial \Phi}{\partial x} - F_q \frac{\partial \Phi}{\partial y} - (p F_p + q F_q) \frac{\partial \Phi}{\partial z} + (F_x + p F_z) \frac{\partial \Phi}{\partial p} + (F_y + q F_z) \frac{\partial \Phi}{\partial q} = 0$$

Applying Lagrange's auxiliary ODE method to this equation gives **Charpit's Auxiliary Equations**:

> **Theorem 2.3 (Charpit's Auxiliary System):**
> $$\frac{dx}{-F_p} = \frac{dy}{-F_q} = \frac{dz}{-(p F_p + q F_q)} = \frac{dp}{F_x + p F_z} = \frac{dq}{F_y + q F_z} = \frac{d\Phi}{0}$$
> or with signs reversed:
> $$\frac{dx}{F_p} = \frac{dy}{F_q} = \frac{dz}{p F_p + q F_q} = \frac{dp}{-(F_x + p F_z)} = \frac{dq}{-(F_y + q F_z)}$$

Any non-trivial first integral $\Phi(x, y, z, p, q) = a$ obtained from this system provides the compatible relation. Solving for $p$ and $q$ and integrating $dz = p dx + q dy$ yields the complete integral with two arbitrary constants $a$ and $b$."""
            },
            {
                "secNumber": "2.5",
                "title": "Special Standard Forms of Non-Linear PDEs",
                "content": r"""### 1. The Four Classical Standard Forms

When the non-linear equation $F(x, y, z, p, q) = 0$ lacks certain variables, Charpit's system simplifies drastically into four canonical forms:

#### Standard Form I: Equations Involving Only $p$ and $q$ ($f(p, q) = 0$)
Here $F_x = F_y = F_z = 0$. Charpit's equations give:
$$\frac{dp}{0} = \frac{dq}{0} \implies p = a \quad (\text{constant})$$
Substituting $p = a$ into $f(p, q) = 0$ gives $q = Q(a)$ (constant).
Integrating $dz = p dx + q dy = a dx + Q(a) dy$:
$$z = a x + Q(a) y + b$$
This is the complete integral, representing a family of planes.

#### Standard Form II: Equations Not Involving $x$ and $y$ ($f(z, p, q) = 0$)
Here $F_x = F_y = 0$. Charpit's system gives $\frac{dp}{p F_z} = \frac{dq}{q F_z} \implies \frac{dp}{p} = \frac{dq}{q} \implies q = a p$.
Assume $z = Z(u)$ where $u = x + a y$. Then:
$$p = \frac{\partial z}{\partial x} = Z'(u), \qquad q = \frac{\partial z}{\partial y} = a Z'(u)$$
Substituting into $f(z, p, q) = 0$ yields an ODE for $Z(u)$:
$$f(z, Z', a Z') = 0 \implies \int \frac{dz}{Z'(z)} = x + a y + b$$

#### Standard Form III: Separable Equations ($f(x, p) = g(y, q)$)
Here $x$ and $p$ can be separated from $y$ and $q$. Set each side equal to an arbitrary constant $a$:
$$f(x, p) = a \implies p = P(x, a)$$
$$g(y, q) = a \implies q = Q(y, a)$$
Integrating the total differential:
$$dz = P(x, a)\,dx + Q(y, a)\,dy \implies z = \int P(x, a)\,dx + \int Q(y, a)\,dy + b$$

#### Standard Form IV: Clairaut's Equation ($z = p x + q y + f(p, q)$)
As established in Unit 1, setting $p = a$ and $q = b$ directly yields the complete integral:
$$z = a x + b y + f(a, b)$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Charpit's Method for the Eikonal Unit-Slope Equation",
                "statement": r"""Find the complete integral of the non-linear first-order partial differential equation:
$$p^2 + q^2 = 1$$
using Charpit's auxiliary equations, and determine its singular solution.""",
                "solution": r"""### 1. Formulating Charpit's Equations
Let $F(x, y, z, p, q) = p^2 + q^2 - 1 = 0$.
The partial derivatives of $F$ are:
$$F_x = 0, \quad F_y = 0, \quad F_z = 0, \quad F_p = 2p, \quad F_q = 2q$$
Charpit's auxiliary equations are:
$$\frac{dx}{F_p} = \frac{dy}{F_q} = \frac{dz}{p F_p + q F_q} = \frac{dp}{-(F_x + p F_z)} = \frac{dq}{-(F_y + q F_z)}$$
Substituting our derivatives:
$$\frac{dx}{2p} = \frac{dy}{2q} = \frac{dz}{2(p^2 + q^2)} = \frac{dp}{0} = \frac{dq}{0}$$

---

### 2. Finding a Compatible Integral
From $\frac{dp}{0}$, we immediately have:
$$dp = 0 \implies p = a \quad (\text{arbitrary constant})$$
Substitute $p = a$ into the original PDE $F = 0$:
$$a^2 + q^2 = 1 \implies q = \sqrt{1 - a^2}$$
(where $|a| \le 1$).

---

### 3. Integrating the Pfaffian Form
Now assemble the total differential $dz = p dx + q dy$:
$$dz = a\,dx + \sqrt{1 - a^2}\,dy$$
Integrating directly:
$$z = a x + \sqrt{1 - a^2}\,y + b$$
This 2-parameter family of planes is the **complete integral**.

---

### 4. Singular Solution
To check for a singular solution, eliminate $p$ and $q$ from:
$$F = p^2 + q^2 - 1 = 0, \qquad F_p = 2p = 0, \qquad F_q = 2q = 0$$
From $F_p = 0$ and $F_q = 0$, we have $p = 0, q = 0$.
Substituting into $F$:
$$0^2 + 0^2 - 1 = -1 \ne 0$$
This is a contradiction! Therefore, **no singular solution exists**. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Non-Linear Cauchy Problem on a Contact Strip",
                "statement": r"""Solve the Cauchy problem for the non-linear first-order partial differential equation:
$$z = p x + q y + p^2 + q^2$$
subject to the initial data on the curve:
$$\Gamma: \quad x_0(s) = s, \quad y_0(s) = 0, \quad z_0(s) = s^2, \qquad s \in \mathbb{R}$$""",
                "solution": r"""### 1. Complete Integral
The equation is of Clairaut form $z = p x + q y + f(p, q)$ where $f(p, q) = p^2 + q^2$.
The complete integral is:
$$z = a x + b y + a^2 + b^2$$
where $a$ and $b$ are arbitrary constants.

---

### 2. Envelope of the Complete Integral Restricted to $\Gamma$
To find the integral surface containing $\Gamma$, we establish an arbitrary relationship $b = \phi(a)$ such that the surface contains each point $(s, 0, s^2)$:
$$z_0(s) = a x_0(s) + b y_0(s) + a^2 + b^2$$
Substitute $x_0 = s, y_0 = 0, z_0 = s^2$:
$$s^2 = a s + a^2 + b^2 \implies s^2 - a s - (a^2 + b^2) = 0$$
Along the characteristic curve, the strip condition requires tangency:
$$\frac{dz_0}{ds} = p_0 \frac{dx_0}{ds} + q_0 \frac{dy_0}{ds}$$
Since $x_0 = s, y_0 = 0, z_0 = s^2$, we have $x_0'(s) = 1, y_0'(s) = 0, z_0'(s) = 2s$.
Thus:
$$2s = p_0(1) + q_0(0) \implies p_0 = 2s$$
From the complete integral, $p = a$, which means:
$$a = 2s \implies s = \frac{a}{2}$$
Substitute $s = a/2$ into the condition $s^2 = a s + a^2 + b^2$:
$$\left(\frac{a}{2}\right)^2 = a \left(\frac{a}{2}\right) + a^2 + b^2 \implies \frac{a^2}{4} = \frac{a^2}{2} + a^2 + b^2 = \frac{3a^2}{2} + b^2$$
Rearranging:
$$b^2 = \frac{a^2}{4} - \frac{6a^2}{4} = -\frac{5a^2}{4}$$
For real solutions, this forces $a = 0, b = 0$, which yields only the point $(0,0,0)$.

---

### 3. Alternative Method via Characteristic Strips
Let us construct the characteristic strip $(x(t), y(t), z(t), p(t), q(t))$ directly using Charpit's ODEs:
Here $F(x, y, z, p, q) = p x + q y + p^2 + q^2 - z = 0$.
The characteristic equations are:
$$\dot{x} = F_p = x + 2p$$
$$\dot{y} = F_q = y + 2q$$
$$\dot{z} = p F_p + q F_q = p(x + 2p) + q(y + 2q)$$
$$\dot{p} = -(F_x + p F_z) = -(p + p(-1)) = 0 \implies p(t) = p_0(s) = 2s$$
$$\dot{q} = -(F_y + q F_z) = -(q + q(-1)) = 0 \implies q(t) = q_0(s)$$

To find $q_0(s)$, substitute initial values into $F = 0$ at $t = 0$:
$$p_0 x_0 + q_0 y_0 + p_0^2 + q_0^2 - z_0 = 0$$
$$(2s)(s) + q_0(0) + (2s)^2 + q_0^2 - s^2 = 0$$
$$2s^2 + 4s^2 + q_0^2 - s^2 = 0 \implies 5s^2 + q_0^2 = 0$$
For real $(x, y, z, p, q)$, $5s^2 + q_0^2 = 0$ forces $s = 0$ and $q_0 = 0$.
Thus, the strip condition has **no real solution** for $s \ne 0$ because the curve $\Gamma$ lies outside the region of real contact elements for this PDE.
In the complex plane, $q_0 = \pm i \sqrt{5} s$, leading to complex integral surfaces.
This demonstrates an essential property of non-linear Cauchy problems: a real solution exists if and only if the initial data strip admits real contact elements $F(x_0, y_0, z_0, p_0, q_0) = 0$. $\blacksquare$"""
            },
            {
                "tier": "Honors Challenge",
                "title": "Shock Formation Time in Inviscid Burgers Equation",
                "statement": r"""Consider the inviscid Burgers equation:
$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = 0, \qquad x \in \mathbb{R}, \quad t > 0$$
subject to the smooth initial Cauchy data:
$$u(x, 0) = \frac{1}{1 + x^2}$$
1. Find the exact breaking time $t_{\text{shock}}$ at which the first shock wave is formed.
2. Determine the spatial coordinate $x_{\text{shock}}$ where the shock first appears.
3. Rigorously prove that $u_x \to -\infty$ as $t \to t_{\text{shock}}^-$, while the solution remains bounded.""",
                "solution": r"""### 1. Calculation of the Breaking Time
Along the characteristic curve issuing from $x_0 \in \mathbb{R}$ at $t = 0$:
$$u(x, t) = u(x_0, 0) = f(x_0) = \frac{1}{1 + x_0^2}$$
The characteristic line equation is:
$$x = x_0 + f(x_0) t = x_0 + \frac{t}{1 + x_0^2}$$
Differentiating with respect to $x$:
$$u_x(x, t) = \frac{f'(x_0)}{1 + t f'(x_0)}$$
A singularity in the spatial gradient occurs when the denominator vanishes:
$$1 + t f'(x_0) = 0 \implies t = -\frac{1}{f'(x_0)}$$
Since $t > 0$, shock formation requires $f'(x_0) < 0$. The earliest breaking time is:
$$t_{\text{shock}} = \min_{x_0 : f'(x_0) < 0} \left( -\frac{1}{f'(x_0)} \right) = \frac{1}{\max_{x_0} (-f'(x_0))}$$

---

### 2. Finding the Maximum Negative Slope of $f(x)$
The initial profile is $f(x) = (1 + x^2)^{-1}$.
Its first derivative is:
$$f'(x) = -\frac{2x}{(1 + x^2)^2}$$
To find the minimum of $f'(x)$ (maximum of $-f'(x)$), differentiate again:
$$f''(x) = - \frac{2(1 + x^2)^2 - 2x \cdot 2(1 + x^2)(2x)}{(1 + x^2)^4} = - \frac{2(1 + x^2) - 8x^2}{(1 + x^2)^3} = - \frac{2 - 6x^2}{(1 + x^2)^3} = \frac{6x^2 - 2}{(1 + x^2)^3}$$
Setting $f''(x) = 0$:
$$6x^2 - 2 = 0 \implies x^2 = \frac{1}{3} \implies x = \pm \frac{1}{\sqrt{3}}$$
For $f'(x)$ to be negative, we need $x > 0$:
$$x_0^* = \frac{1}{\sqrt{3}}$$
Evaluate $f'(x_0^*)$:
$$1 + (x_0^*)^2 = 1 + \frac{1}{3} = \frac{4}{3}$$
$$f'(x_0^*) = - \frac{2 / \sqrt{3}}{(4/3)^2} = - \frac{2 / \sqrt{3}}{16 / 9} = - \frac{2 \cdot 9}{16 \sqrt{3}} = - \frac{18}{16\sqrt{3}} = - \frac{9}{8\sqrt{3}} = - \frac{3\sqrt{3}}{8}$$
Thus, the maximum negative slope is:
$$\max (-f'(x)) = \frac{3\sqrt{3}}{8}$$
Therefore, the **shock formation time** is:
$$t_{\text{shock}} = \frac{8}{3\sqrt{3}} = \frac{8\sqrt{3}}{9} \approx 1.5396\text{ s}$$

---

### 3. Spatial Location of First Shock Inception
At $t = t_{\text{shock}}$ and $x_0 = \frac{1}{\sqrt{3}}$:
$$x_{\text{shock}} = x_0^* + f(x_0^*) t_{\text{shock}}$$
We have:
$$f(x_0^*) = \frac{1}{1 + 1/3} = \frac{3}{4}$$
Therefore:
$$x_{\text{shock}} = \frac{1}{\sqrt{3}} + \left(\frac{3}{4}\right) \left( \frac{8}{3\sqrt{3}} \right) = \frac{1}{\sqrt{3}} + \frac{2}{\sqrt{3}} = \frac{3}{\sqrt{3}} = \sqrt{3} \approx 1.732$$

---

### 4. Gradient Divergence with Bounded Solution
As $t \to t_{\text{shock}}^-$ along the critical characteristic $x_0 = \frac{1}{\sqrt{3}}$:
$$1 + t f'(x_0^*) = 1 - t \frac{3\sqrt{3}}{8} \to 0^+$$
Hence:
$$u_x(x(t), t) = \frac{-3\sqrt{3}/8}{1 - t(3\sqrt{3}/8)} \to -\infty$$
However, along every characteristic, $u(x, t) = f(x_0) = \frac{1}{1 + x_0^2}$.
Since $0 < f(x_0) \le 1$ for all $x_0 \in \mathbb{R}$, we have:
$$0 < u(x, t) \le 1 \quad \forall t \ge 0$$
The solution remains strictly bounded in the supremum norm $\|u(\cdot, t)\|_\infty \le 1$, but its derivative blows up: a classic **gradient catastrophe**. $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u2 = get_unit2()
    print(f"Loaded Unit 2: {u2['title']} with {len(u2['sections'])} sections and {len(u2['problems'])} problems.")
