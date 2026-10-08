# -*- coding: utf-8 -*-
"""
build_pde_unit1.py
Constructs Unit 1: First-Order Linear & Quasilinear PDEs: Foundations, Integral Surfaces & Lagrange's Method
Strictly ZERO course numbers.
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "First-Order Linear & Quasilinear PDEs: Foundations, Integral Surfaces & Lagrange's Method",
        "leadSummary": "Geometric foundations of first-order partial differential equations: classification by linearity, formation of PDEs by eliminating arbitrary constants and functions, complete integrals, envelopes and singular solutions, Lagrange's method of auxiliary equations for quasilinear equations P p + Q q = R, integral surfaces passing through a space curve, transversality conditions, and physical applications to traffic flow and 1D conservation laws.",
        "simulations": ["sim_pde_lagrange_characteristics"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Geometric Derivation, Classification, and Formulation of First-Order PDEs",
                "content": r"""### 1. Fundamental Definitions and Terminology

A **partial differential equation (PDE)** is an equation relating an unknown function of two or more independent variables to its partial derivatives. For a function $z = z(x, y)$ of two real independent variables $x$ and $y$, the standard Monge notation denotes the first partial derivatives by:
$$p = \frac{\partial z}{\partial x} \equiv z_x, \qquad q = \frac{\partial z}{\partial y} \equiv z_y$$

> **Definition 1.1 (Order and General First-Order Form):**
> The **order** of a PDE is the order of the highest derivative occurring in the equation. The most general first-order PDE in two independent variables is expressed implicitly as:
> $$F(x, y, z, p, q) = 0$$
> where $F$ is a continuously differentiable function on some open domain $D \subseteq \mathbb{R}^5$ such that $(F_p)^2 + (F_q)^2 \ne 0$.

---

### 2. Classification by Linearity

First-order PDEs are partitioned into four distinct mathematical categories based on the algebraic structure of the derivative terms $p$ and $q$:

1. **Linear PDEs:** The equation is linear in $z, p,$ and $q$, with coefficients depending exclusively on the independent variables $x$ and $y$:
   $$A(x, y) p + B(x, y) q + C(x, y) z = D(x, y)$$

2. **Semilinear PDEs:** The derivatives $p$ and $q$ appear linearly with coefficients depending only on $x$ and $y$, but the lower-order term may be non-linear in $z$:
   $$A(x, y) p + B(x, y) q = R(x, y, z)$$

3. **Quasilinear PDEs:** The derivatives $p$ and $q$ enter linearly, but their coefficients may depend on the dependent variable $z$ as well as $x$ and $y$:
   $$P(x, y, z) p + Q(x, y, z) q = R(x, y, z)$$

4. **Fully Non-Linear PDEs:** The equation depends non-linearly on the derivatives $p$ and $q$ (e.g., $p^2 + q^2 = 1$ or $p q = z$).

---

### 3. Formation of PDEs: Elimination of Arbitrary Constants and Functions

A PDE frequently arises in physics and geometry as the governing relation characterizing a whole family of geometric surfaces.

#### Method A: Elimination of Arbitrary Constants
Let $\Phi(x, y, z, a, b) = 0$ represent a two-parameter family of surfaces, where $a$ and $b$ are arbitrary real parameters.
Differentiating implicitly with respect to $x$ and $y$:
$$\frac{\partial \Phi}{\partial x} + p \frac{\partial \Phi}{\partial z} = 0, \qquad \frac{\partial \Phi}{\partial y} + q \frac{\partial \Phi}{\partial z} = 0$$
These three equations contain the two constants $a$ and $b$. Eliminating $a$ and $b$ yields a single relationship of the form $F(x, y, z, p, q) = 0$.

> **Example 1.1 (Spheres with Centers on the $z$-Axis):**
> Consider the family of spheres $x^2 + y^2 + (z - c)^2 = r^2$, having two arbitrary constants $c$ and $r$.
> Differentiating with respect to $x$: $2x + 2(z - c) p = 0 \implies z - c = -\frac{x}{p}$.
> Differentiating with respect to $y$: $2y + 2(z - c) q = 0 \implies z - c = -\frac{y}{q}$.
> Equating the two expressions for $(z - c)$:
> $$-\frac{x}{p} = -\frac{y}{q} \implies y p - x q = 0$$
> This is a first-order linear PDE whose solutions encompass all surfaces of revolution around the $z$-axis.

#### Method B: Elimination of Arbitrary Functions
Let $u = u(x, y, z)$ and $v = v(x, y, z)$ be two known independent differentiable functions, and let $\Phi(u, v) = 0$ be an arbitrary relation (or equivalently $v = f(u)$ for an arbitrary function $f$).
Differentiating $v = f(u)$ with respect to $x$ and $y$:
$$\frac{\partial v}{\partial x} + p \frac{\partial v}{\partial z} = f'(u) \left( \frac{\partial u}{\partial x} + p \frac{\partial u}{\partial z} \right)$$
$$\frac{\partial v}{\partial y} + q \frac{\partial v}{\partial z} = f'(u) \left( \frac{\partial u}{\partial y} + q \frac{\partial u}{\partial z} \right)$$
Dividing these two equations eliminates the arbitrary derivative $f'(u)$:
$$\frac{v_x + p v_z}{v_y + q v_z} = \frac{u_x + p u_z}{u_y + q u_z}$$
Cross-multiplying and collecting terms in $p$ and $q$:
$$p \left( \frac{\partial u}{\partial y}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial y} \right) + q \left( \frac{\partial u}{\partial z}\frac{\partial v}{\partial x} - \frac{\partial u}{\partial x}\frac{\partial v}{\partial z} \right) = \frac{\partial u}{\partial x}\frac{\partial v}{\partial y} - \frac{\partial u}{\partial y}\frac{\partial v}{\partial x}$$
Using the Jacobian determinant notation $\frac{\partial(u, v)}{\partial(y, z)} = u_y v_z - u_z v_y$:
$$\frac{\partial(u, v)}{\partial(y, z)} p + \frac{\partial(u, v)}{\partial(z, x)} q = \frac{\partial(u, v)}{\partial(x, y)}$$
This is precisely **Lagrange's quasilinear equation** $P p + Q q = R$, demonstrating that eliminating an arbitrary function always generates a quasilinear first-order PDE."""
            },
            {
                "secNumber": "1.2",
                "title": "Complete Integrals, General Solutions, Singular Solutions, and Envelopes",
                "content": r"""### 1. The Hierarchy of Integral Solutions

For an ordinary differential equation of order $n$, the general solution contains $n$ arbitrary constants. In contrast, for a first-order PDE, solutions manifest in three fundamentally distinct geometric forms:

> **Definition 1.2 (Complete Integral):**
> A relation $\phi(x, y, z, a, b) = 0$ containing two independent arbitrary constants $a$ and $b$ is called a **complete integral** (or complete primitive) of $F(x, y, z, p, q) = 0$ if, on the domain of interest:
> $$\operatorname{rank} \begin{pmatrix} \phi_a & \phi_b & \phi_{xa} & \phi_{xb} \\ \phi_{ya} & \phi_{yb} & \phi_{za} & \phi_{zb} \end{pmatrix} = 2$$
> ensuring that neither parameter is redundant.

> **Definition 1.3 (General Integral / General Solution):**
> If in the complete integral $\phi(x, y, z, a, b) = 0$ we establish an arbitrary functional dependence between the parameters by setting $b = \psi(a)$, where $\psi$ is an arbitrary $C^1$ function, then the envelope of the resulting one-parameter family of surfaces:
> $$\phi(x, y, z, a, \psi(a)) = 0, \qquad \frac{\partial \phi}{\partial a} + \psi'(a) \frac{\partial \phi}{\partial b} = 0$$
> obtained by eliminating the parameter $a$, is called the **general integral** (or general solution) of the PDE.

> **Definition 1.4 (Singular Integral / Singular Solution):**
> The envelope of the entire two-parameter family of surfaces $\phi(x, y, z, a, b) = 0$ obtained by eliminating both parameters $a$ and $b$ simultaneously from the system:
> $$\phi(x, y, z, a, b) = 0, \qquad \frac{\partial \phi}{\partial a}(x, y, z, a, b) = 0, \qquad \frac{\partial \phi}{\partial b}(x, y, z, a, b) = 0$$
> (provided the Hessian determinant $\phi_{aa}\phi_{bb} - (\phi_{ab})^2 \ne 0$) is called the **singular integral**.
> Geometrically, the singular integral represents a surface that is tangent at every point to some member of the family of complete integral surfaces, but cannot be obtained from the general integral by any choice of the arbitrary function $\psi$.

---

### 2. Envelope Theory and Clairaut-Type PDEs

> **Theorem 1.1 (Singular Solution from the PDE Itself):**
> The singular solution of $F(x, y, z, p, q) = 0$ can alternatively be determined directly from the PDE without prior knowledge of the complete integral by eliminating $p$ and $q$ from the system:
> $$F(x, y, z, p, q) = 0, \qquad \frac{\partial F}{\partial p}(x, y, z, p, q) = 0, \qquad \frac{\partial F}{\partial q}(x, y, z, p, q) = 0$$
> provided the resulting surface satisfies the original PDE and is not merely a locus of singular points (such as cuspidal edges or nodal lines).

*Proof:*
Let $z = \psi(x, y)$ be the envelope of the two-parameter family of integral surfaces $z = f(x, y, a, b)$.
At each point of contact $(x, y)$, the envelope surface shares the same value of $z$ and the same tangent plane (hence the same derivatives $p$ and $q$) as the member surface with parameters $a(x, y), b(x, y)$:
$$p = f_x(x, y, a, b), \qquad q = f_y(x, y, a, b)$$
Since $f$ satisfies $F(x, y, f, f_x, f_y) = 0$ identically for all $a$ and $b$, differentiating this identity with respect to $a$ yields:
$$F_z f_a + F_p f_{xa} + F_q f_{ya} = 0$$
However, along the envelope, the tangency condition requires $f_a = 0$ and $f_b = 0$.
Differentiating $f_a(x, y, a, b) = 0$ with respect to $x$ and $y$:
$$f_{xa} + f_{aa} a_x + f_{ab} b_x = 0$$
Substituting this into the differential identity forces $F_p = 0$ and symmetrically $F_q = 0$. $\blacksquare$"""
            },
            {
                "secNumber": "1.3",
                "title": "Lagrange's Method of Auxiliary Equations: Quasi-Linear PDEs",
                "content": r"""### 1. Geometric Interpretation of Quasilinear PDEs

Consider the general quasilinear first-order equation:
$$P(x, y, z) \frac{\partial z}{\partial x} + Q(x, y, z) \frac{\partial z}{\partial y} = R(x, y, z)$$
where $P, Q, R$ are continuously differentiable functions with $P^2 + Q^2 + R^2 \ne 0$.

Let the solution surface (called an **integral surface**) be given implicitly by $S(x, y, z) = z - f(x, y) = 0$.
The normal vector to this surface at any point $(x, y, z)$ is given by the gradient:
$$\nabla S = \left( -\frac{\partial z}{\partial x}, -\frac{\partial z}{\partial y}, 1 \right) = (-p, -q, 1) \quad \text{or equivalently} \quad \mathbf{n} = (p, q, -1)$$
Now consider the three-dimensional vector field:
$$\mathbf{V}(x, y, z) = \begin{pmatrix} P(x, y, z) \\ Q(x, y, z) \\ R(x, y, z) \end{pmatrix}$$
Taking the dot product of the vector field $\mathbf{V}$ with the surface normal $\mathbf{n}$:
$$\mathbf{V} \cdot \mathbf{n} = P p + Q q - R = 0$$
This dot product vanishes identically on the solution surface!

> **Geometric Fundamental Principle:**
> The quasilinear PDE $P p + Q q = R$ asserts that at every point $(x, y, z)$ of an integral surface, the vector field $\mathbf{V} = (P, Q, R)$ is **orthogonal to the surface normal**, meaning $\mathbf{V}$ lies entirely in the **tangent plane** of the integral surface.
> Consequently, the integral surface is generated by a one-parameter family of integral curves of the vector field $\mathbf{V}$. These curves are called the **characteristic curves** of the PDE.

---

### 2. Lagrange's Auxiliary (Subsidiary) System

The characteristic curves are the field lines of $\mathbf{V}(x, y, z)$, described by the autonomous system of ODEs in parameter $t$:
$$\frac{dx}{dt} = P(x, y, z), \qquad \frac{dy}{dt} = Q(x, y, z), \qquad \frac{dz}{dt} = R(x, y, z)$$
Eliminating the parameter $t$ gives the celebrated **Lagrange Auxiliary System**:
$$\frac{dx}{P(x, y, z)} = \frac{dy}{Q(x, y, z)} = \frac{dz}{R(x, y, z)}$$

> **Theorem 1.2 (Lagrange's Theorem on General Solution):**
> Let $u(x, y, z) = c_1$ and $v(x, y, z) = c_2$ be two functionally independent first integrals of Lagrange's auxiliary system, such that $\nabla u \times \nabla v \ne \mathbf{0}$.
> Then the general solution of the quasilinear PDE $P p + Q q = R$ is given implicitly by:
> $$\Phi(u(x, y, z), v(x, y, z)) = 0$$
> or explicitly by $u = \psi(v)$ (or $v = \phi(u)$), where $\Phi$ and $\psi$ are arbitrary continuously differentiable functions.

*Proof:*
Since $u(x, y, z) = c_1$ is a first integral of $\dot{x} = P, \dot{y} = Q, \dot{z} = R$, the total derivative along any characteristic trajectory vanishes:
$$\frac{du}{dt} = u_x \frac{dx}{dt} + u_y \frac{dy}{dt} + u_z \frac{dz}{dt} = P u_x + Q u_y + R u_z = 0$$
Similarly for $v(x, y, z) = c_2$:
$$P v_x + Q v_y + R v_z = 0$$
Now let the surface be defined by $\Phi(u, v) = 0$. Differentiating implicitly with respect to $x$ and $y$:
$$\Phi_u (u_x + p u_z) + \Phi_v (v_x + p v_z) = 0$$
$$\Phi_u (u_y + q u_z) + \Phi_v (v_y + q v_z) = 0$$
For a non-trivial relation, the determinant of coefficients with respect to $(\Phi_u, \Phi_v)$ must vanish:
$$(u_x + p u_z)(v_y + q v_z) - (u_y + q u_z)(v_x + p v_z) = 0$$
Expanding this determinant:
$$(u_x v_y - u_y v_x) + p (u_z v_y - u_y v_z) + q (u_x v_z - u_z v_x) = 0$$
Using the Jacobian cross-product identity $\nabla u \times \nabla v = \begin{pmatrix} u_y v_z - u_z v_y \\ u_z v_x - u_x v_z \\ u_x v_y - u_y v_x \end{pmatrix}$:
Notice that since $P u_x + Q u_y + R u_z = 0$ and $P v_x + Q v_y + R v_z = 0$, the characteristic vector $(P, Q, R)$ is parallel to the cross product $\nabla u \times \nabla v$:
$$(P, Q, R) = \lambda (\nabla u \times \nabla v)$$
Substituting the components:
$$P = \lambda (u_y v_z - u_z v_y), \quad Q = \lambda (u_z v_x - u_x v_z), \quad R = \lambda (u_x v_y - u_y v_x)$$
Dividing by $\lambda$ reveals:
$$- p P - q Q + R = 0 \implies P p + Q q = R$$
Thus every surface $\Phi(u, v) = 0$ is a valid solution of the PDE. $\blacksquare$

---

### 3. Methods for Integrating Lagrange's Auxiliary Equations

Two primary algebraic techniques are utilized to integrate the system $\frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R}$:

1. **Method of Grouping:** Select two ratios involving only two variables (or where the third cancels out), yielding a direct ordinary differential equation.
2. **Method of Multipliers:** By the algebraic properties of equal ratios:
   $$\frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} = \frac{l\,dx + m\,dy + n\,dz}{l P + m Q + n R}$$
   If multipliers $(l, m, n)$ can be discovered such that:
   $$l P + m Q + n R = 0$$
   then it immediately follows that $l\,dx + m\,dy + n\,dz = 0$. If this 1-form is exact (or possesses an integrating factor), integrating yields $u(x, y, z) = c_1$."""
            },
            {
                "secNumber": "1.4",
                "title": "Integral Surfaces Passing Through a Given Space Curve & Transversality Conditions",
                "content": r"""### 1. Geometric Formulation of the Cauchy Initial Value Problem

In applications, we do not seek the most general family of solutions containing an arbitrary function $\Phi$; rather, we seek the specific integral surface $z = f(x, y)$ that contains a specified space curve $\Gamma$.

Let the initial curve $\Gamma$ be parametrized by an arc parameter $s$:
$$\Gamma: \quad x = x_0(s), \quad y = y_0(s), \quad z = z_0(s), \qquad s \in I \subseteq \mathbb{R}$$

To construct the integral surface through $\Gamma$:
1. Solve Lagrange's auxiliary system $\frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R}$ to obtain two independent first integrals $u(x, y, z) = c_1$ and $v(x, y, z) = c_2$.
2. Restrict $u$ and $v$ to the initial curve $\Gamma$ by substituting the parametric coordinates:
   $$U(s) = u(x_0(s), y_0(s), z_0(s)), \qquad V(s) = v(x_0(s), y_0(s), z_0(s))$$
3. Eliminate the parameter $s$ between $U(s) = c_1$ and $V(s) = c_2$ to find an algebraic relation $F(c_1, c_2) = 0$.
4. Replace $c_1$ and $c_2$ with $u(x, y, z)$ and $v(x, y, z)$ to obtain the explicit equation of the unique integral surface $F(u(x,y,z), v(x,y,z)) = 0$.

---

### 2. Transversality and Existence-Uniqueness Breakdown

Alternatively, we can trace the two-parameter family of characteristic curves issuing from each point of $\Gamma$:
$$\begin{cases}
\frac{dx}{dt} = P(x, y, z), & x(0, s) = x_0(s) \\
\frac{dy}{dt} = Q(x, y, z), & y(0, s) = y_0(s) \\
\frac{dz}{dt} = R(x, y, z), & z(0, s) = z_0(s)
\end{cases}$$
This yields the parametric representation of the surface: $x = X(s, t), y = Y(s, t), z = Z(s, t)$.
To express $z$ as a single-valued function of $x$ and $y$, the Inverse Function Theorem requires the Jacobian determinant of the spatial transformation $(s, t) \mapsto (x, y)$ to be non-zero along the initial curve $t = 0$:

> **Definition 1.5 (Transversality Condition):**
> The initial curve $\Gamma$ is said to be **transversal** (non-characteristic) to the vector field $\mathbf{V} = (P, Q, R)$ if:
> $$J(s) = \left. \frac{\partial(x, y)}{\partial(s, t)} \right|_{t=0} = \det \begin{pmatrix} x_0'(s) & P(x_0(s), y_0(s), z_0(s)) \\ y_0'(s) & Q(x_0(s), y_0(s), z_0(s)) \end{pmatrix} \ne 0$$
> for all $s \in I$.
> That is, $x_0'(s) Q(x_0, y_0, z_0) - y_0'(s) P(x_0, y_0, z_0) \ne 0$.

> **Theorem 1.3 (Cauchy-Kovalevskaya Local Existence for Quasilinear First-Order PDEs):**
> 1. If the transversality condition $J(s) \ne 0$ holds at $s_0 \in I$, there exists an open neighborhood of $\Gamma$ in which there exists a **unique** local integral surface $z = f(x, y)$ containing $\Gamma$.
> 2. If $J(s) = 0$ along $\Gamma$ and the curve is a characteristic curve (meaning $\frac{x_0'(s)}{P} = \frac{y_0'(s)}{Q} = \frac{z_0'(s)}{R}$), there exist **infinitely many** integral surfaces passing through $\Gamma$.
> 3. If $J(s) = 0$ along $\Gamma$ but $\frac{x_0'(s)}{P} \ne \frac{z_0'(s)}{R}$, **no solution exists**."""
            },
            {
                "secNumber": "1.5",
                "title": "Applications to Orthogonal Surfaces, Traffic Flow Models & Conservation Laws",
                "content": r"""### 1. Surfaces Orthogonal to a Given Family

A classic geometric problem is finding the family of surfaces $z = f(x, y)$ that cut a given two-parameter family of surfaces $F(x, y, z, c) = 0$ at right angles.
At every point of intersection, the normal vector $\mathbf{n}_1 = (p, q, -1)$ of the required surface must be perpendicular to the normal vector $\mathbf{n}_2 = (F_x, F_y, F_z)$ of the given family:
$$\mathbf{n}_1 \cdot \mathbf{n}_2 = 0 \implies F_x p + F_y q - F_z = 0$$
This is a quasilinear PDE of the form $P p + Q q = R$ with $P = F_x, Q = F_y, R = F_z$, solvable directly via Lagrange's method.

---

### 2. 1D Conservation Laws and Kinematic Waves

In continuum mechanics and transportation engineering, consider a conserved scalar quantity (such as vehicular traffic, fluid mass, or pollutant concentration) distributed along a 1D conduit $x \in \mathbb{R}$.
Let $\rho(x, t)$ denote the density per unit length, and $q(x, t)$ denote the flux (rate of transfer across coordinate $x$).

For an arbitrary control volume $[x_1, x_2]$, the rate of change of total mass equals the net flux across boundaries:
$$\frac{d}{dt} \int_{x_1}^{x_2} \rho(x, t)\,dx = q(x_1, t) - q(x_2, t) = - \int_{x_1}^{x_2} \frac{\partial q}{\partial x}\,dx$$
Since the interval $[x_1, x_2]$ is arbitrary, assuming $C^1$ smoothness gives the **differential conservation law**:
$$\frac{\partial \rho}{\partial t} + \frac{\partial q}{\partial x} = 0$$

#### The Lighthill-Whitham-Richards (LWR) Traffic Flow Model
In the LWR traffic theory, vehicular flux depends solely on the local traffic density: $q = Q(\rho)$.
By the chain rule:
$$\frac{\partial q}{\partial x} = Q'(\rho) \frac{\partial \rho}{\partial x}$$
Setting $c(\rho) = Q'(\rho)$ yields the **quasilinear kinematic wave equation**:
$$\rho_t + c(\rho) \rho_x = 0$$

1. **Greenshields Model:** The velocity $v(\rho)$ decreases linearly from free-flow speed $v_{\max}$ to zero at jam density $\rho_{\max}$:
   $$v(\rho) = v_{\max} \left( 1 - \frac{\rho}{\rho_{\max}} \right) \implies q(\rho) = \rho v(\rho) = v_{\max} \left( \rho - \frac{\rho^2}{\rho_{\max}} \right)$$
2. **Kinematic Wave Speed:**
   $$c(\rho) = \frac{dq}{d\rho} = v_{\max} \left( 1 - \frac{2\rho}{\rho_{\max}} \right)$$
Notice that for dense traffic ($\rho > \frac{1}{2}\rho_{\max}$), $c(\rho) < 0$: waves of congestion propagate **backward** relative to the road, explaining the physical origin of phantom traffic jams!"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Lagrange Integration of a Homogeneous Quasilinear Equation",
                "statement": r"""Find the general solution of the quasilinear partial differential equation:
$$x^2 \frac{\partial z}{\partial x} + y^2 \frac{\partial z}{\partial y} = z^2$$
and deduce the specific integral surface that passes through the hyperbola $x y = 1, z = 1$.""",
                "solution": r"""### 1. Setup of Lagrange's Auxiliary Equations
The PDE is in Lagrange form $P p + Q q = R$ where:
$$P = x^2, \qquad Q = y^2, \qquad R = z^2$$
The auxiliary subsidiary system is:
$$\frac{dx}{x^2} = \frac{dy}{y^2} = \frac{dz}{z^2}$$

---

### 2. Integration of the Auxiliary System
We select two independent pairs using the method of grouping:
1. **First Pair:**
   $$\frac{dx}{x^2} = \frac{dy}{y^2} \implies \int x^{-2}\,dx = \int y^{-2}\,dy \implies -\frac{1}{x} = -\frac{1}{y} + c_1'$$
   Multiplying by $-1$:
   $$u(x, y, z) = \frac{1}{x} - \frac{1}{y} = c_1$$

2. **Second Pair:**
   $$\frac{dy}{y^2} = \frac{dz}{z^2} \implies \int y^{-2}\,dy = \int z^{-2}\,dz \implies -\frac{1}{y} = -\frac{1}{z} + c_2'$$
   Multiplying by $-1$:
   $$v(x, y, z) = \frac{1}{y} - \frac{1}{z} = c_2$$

The two first integrals $u = \frac{1}{x} - \frac{1}{y}$ and $v = \frac{1}{y} - \frac{1}{z}$ are functionally independent since:
$$\nabla u \times \nabla v = \begin{pmatrix} -1/x^2 \\ 1/y^2 \\ 0 \end{pmatrix} \times \begin{pmatrix} 0 \\ -1/y^2 \\ 1/z^2 \end{pmatrix} = \begin{pmatrix} 1/(y^2 z^2) \\ 1/(x^2 z^2) \\ 1/(x^2 y^2) \end{pmatrix} \ne \mathbf{0}$$

Therefore, the **general solution** is:
$$\Phi\left( \frac{1}{x} - \frac{1}{y}, \frac{1}{y} - \frac{1}{z} \right) = 0 \quad \text{or} \quad \frac{1}{y} - \frac{1}{z} = f\left( \frac{1}{x} - \frac{1}{y} \right)$$
where $f$ is an arbitrary differentiable function.

---

### 3. Integral Surface Passing Through the Given Curve
The initial curve $\Gamma$ is given by $x y = 1, z = 1$.
Parametrizing $\Gamma$ using parameter $t$:
$$x(t) = t, \qquad y(t) = \frac{1}{t}, \qquad z(t) = 1$$
Substituting into our two first integrals:
$$c_1 = \frac{1}{x(t)} - \frac{1}{y(t)} = \frac{1}{t} - t$$
$$c_2 = \frac{1}{y(t)} - \frac{1}{z(t)} = t - 1$$
From $c_2 = t - 1$, we solve for $t$:
$$t = c_2 + 1$$
Substitute this into the expression for $c_1$:
$$c_1 = \frac{1}{c_2 + 1} - (c_2 + 1) = \frac{1 - (c_2 + 1)^2}{c_2 + 1} = \frac{-c_2^2 - 2c_2}{c_2 + 1}$$
Cross-multiplying:
$$c_1(c_2 + 1) + c_2^2 + 2c_2 = 0 \implies (c_1 + 2) c_2 + c_2^2 + c_1 = 0$$
Now restore the original coordinates $c_1 = \frac{1}{x} - \frac{1}{y}$ and $c_2 = \frac{1}{y} - \frac{1}{z}$:
$$\left( \frac{1}{x} - \frac{1}{y} \right) \left( \frac{1}{y} - \frac{1}{z} + 1 \right) + \left( \frac{1}{y} - \frac{1}{z} \right)^2 + 2\left( \frac{1}{y} - \frac{1}{z} \right) = 0$$
This is the exact implicit equation of the unique integral surface containing the hyperbolic curve. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Cauchy Problem with Parabolic Initial Data and Transversality Verification",
                "statement": r"""Solve the Cauchy problem for the quasilinear first-order equation:
$$x \frac{\partial z}{\partial x} + y \frac{\partial z}{\partial y} = 2z$$
subject to the initial condition that the integral surface passes through the space curve:
$$\Gamma: \quad x_0(s) = s, \quad y_0(s) = s^2, \quad z_0(s) = s^3, \qquad s > 0$$
Verify that the transversality condition holds everywhere along $\Gamma$.""",
                "solution": r"""### 1. Transversality Check along the Initial Curve
Here $P(x, y, z) = x$ and $Q(x, y, z) = y$.
The initial curve has tangent components:
$$x_0'(s) = 1, \qquad y_0'(s) = 2s$$
Evaluating $P$ and $Q$ on $\Gamma$:
$$P(x_0, y_0, z_0) = s, \qquad Q(x_0, y_0, z_0) = s^2$$
The transversality Jacobian is:
$$J(s) = \det \begin{pmatrix} x_0'(s) & P(x_0, y_0, z_0) \\ y_0'(s) & Q(x_0, y_0, z_0) \end{pmatrix} = \det \begin{pmatrix} 1 & s \\ 2s & s^2 \end{pmatrix} = s^2 - 2s^2 = -s^2$$
Since $s > 0$, $J(s) = -s^2 \ne 0$ for all $s > 0$.
The transversality condition holds strictly, guaranteeing the existence of a unique local integral surface.

---

### 2. Characteristic Equations
The characteristic equations are:
$$\frac{dx}{dt} = x, \qquad \frac{dy}{dt} = y, \qquad \frac{dz}{dt} = 2z$$
subject to initial conditions at $t = 0$:
$$x(0, s) = s, \qquad y(0, s) = s^2, \qquad z(0, s) = s^3$$

Integrating each ODE with respect to $t$:
1. $\frac{dx}{x} = dt \implies x(s, t) = s e^t$
2. $\frac{dy}{y} = dt \implies y(s, t) = s^2 e^t$
3. $\frac{dz}{z} = 2 dt \implies z(s, t) = s^3 e^{2t}$

---

### 3. Inverting the Parametric Coordinates
We need to eliminate the parameters $(s, t)$ in terms of $(x, y)$:
From $x = s e^t$ and $y = s^2 e^t$, divide $y$ by $x$:
$$\frac{y}{x} = \frac{s^2 e^t}{s e^t} = s \implies s = \frac{y}{x}$$
Now substitute $s = y/x$ back into $x = s e^t$:
$$x = \left(\frac{y}{x}\right) e^t \implies e^t = \frac{x^2}{y}$$
Now evaluate $z(s, t)$:
$$z = s^3 e^{2t} = s^3 (e^t)^2 = \left( \frac{y}{x} \right)^3 \left( \frac{x^2}{y} \right)^2 = \frac{y^3}{x^3} \frac{x^4}{y^2} = x y$$

---

### 4. Verification
The candidate solution is:
$$z(x, y) = x y$$
1. Check the PDE:
   $$p = \frac{\partial z}{\partial x} = y, \qquad q = \frac{\partial z}{\partial y} = x$$
   $$x p + y q = x(y) + y(x) = 2xy = 2z \quad \checkmark$$
2. Check initial curve data on $\Gamma$ ($x = s, y = s^2$):
   $$z(s, s^2) = (s)(s^2) = s^3 = z_0(s) \quad \checkmark$$
The unique solution is indeed $z = x y$. $\blacksquare$"""
            },
            {
                "tier": "Honors Challenge",
                "title": "Complete Integral of Clairaut PDE and Singular Envelope Verification",
                "statement": r"""Consider the non-linear first-order partial differential equation of Clairaut type:
$$z = p x + q y + \frac{1}{2}(p^2 + q^2)$$
1. Find the complete integral of this equation containing two arbitrary constants $a$ and $b$.
2. Derive the singular solution by calculating the envelope of this two-parameter family.
3. Rigorously prove that the singular surface is tangent to every member plane of the complete integral family along its characteristic contact points.""",
                "solution": r"""### 1. Complete Integral
A PDE of the form $z = p x + q y + f(p, q)$ is known as **Clairaut's equation for partial derivatives**.
Assume a trial plane solution of the form:
$$z = a x + b y + c$$
Then the partial derivatives are constants:
$$p = \frac{\partial z}{\partial x} = a, \qquad q = \frac{\partial z}{\partial y} = b$$
Substituting into the PDE:
$$a x + b y + c = a x + b y + \frac{1}{2}(a^2 + b^2) \implies c = \frac{1}{2}(a^2 + b^2)$$
Thus, the **complete integral** is the 2-parameter family of planes:
$$z = a x + b y + \frac{1}{2}(a^2 + b^2)$$

---

### 2. Envelope and Singular Solution
Let $\phi(x, y, z, a, b) = a x + b y + \frac{1}{2}(a^2 + b^2) - z = 0$.
To determine the envelope, we take partial derivatives with respect to the parameters $a$ and $b$ and set them to zero:
$$\frac{\partial \phi}{\partial a} = x + a = 0 \implies a = -x$$
$$\frac{\partial \phi}{\partial b} = y + b = 0 \implies b = -y$$
Substituting $a = -x$ and $b = -y$ into the complete integral:
$$z = (-x) x + (-y) y + \frac{1}{2}\left( (-x)^2 + (-y)^2 \right) = -x^2 - y^2 + \frac{1}{2}(x^2 + y^2) = -\frac{1}{2}(x^2 + y^2)$$
Thus, the **singular solution** is the paraboloid of revolution:
$$z = -\frac{1}{2}(x^2 + y^2)$$

---

### 3. Verification of Tangency
To rigorously prove tangency:
1. **The singular solution satisfies the PDE:**
   For $z = -\frac{1}{2}(x^2 + y^2)$:
   $$p = -x, \qquad q = -y$$
   Substitute into the PDE:
   $$p x + q y + \frac{1}{2}(p^2 + q^2) = (-x)x + (-y)y + \frac{1}{2}(x^2 + y^2) = -x^2 - y^2 + \frac{1}{2}(x^2 + y^2) = -\frac{1}{2}(x^2 + y^2) = z$$
   The PDE is satisfied identically!

2. **Geometric Tangency:**
   For any fixed parameters $(a_0, b_0)$, consider the member plane:
   $$\Pi(a_0, b_0): \quad z = a_0 x + b_0 y + \frac{1}{2}(a_0^2 + b_0^2)$$
   The contact point with the paraboloid occurs at $x_0 = -a_0, y_0 = -b_0$.
   At this point:
   - Value on the plane:
     $$z_{\text{plane}} = a_0(-a_0) + b_0(-b_0) + \frac{1}{2}(a_0^2 + b_0^2) = -\frac{1}{2}(a_0^2 + b_0^2)$$
   - Value on the paraboloid:
     $$z_{\text{parab}} = -\frac{1}{2}(x_0^2 + y_0^2) = -\frac{1}{2}((-a_0)^2 + (-b_0)^2) = -\frac{1}{2}(a_0^2 + b_0^2) = z_{\text{plane}}$$
   - Normal vector of the plane: $\mathbf{n}_{\text{plane}} = (a_0, b_0, -1)$.
   - Normal vector of the paraboloid:
     $$\nabla(z + \frac{1}{2}(x^2 + y^2)) = (x_0, y_0, 1) \implies (-x_0, -y_0, -1) = (a_0, b_0, -1) = \mathbf{n}_{\text{plane}}$$
   The values and the normal vectors coincide perfectly at $(x_0, y_0)$.
   Hence, the singular paraboloid is strictly tangent to every member plane of the family. $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u1 = get_unit1()
    print(f"Loaded Unit 1: {u1['title']} with {len(u1['sections'])} sections and {len(u1['problems'])} problems.")
