# -*- coding: utf-8 -*-
"""
build_pde_unit3.py
Constructs Unit 3: Classification and Canonical Reduction of Second-Order Linear PDEs
Strictly ZERO course numbers.
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Classification and Canonical Reduction of Second-Order Linear PDEs",
        "leadSummary": "Comprehensive classification theory for second-order linear partial differential equations in two independent variables: the characteristic quadratic form and invariance of the discriminant Delta = B^2 - AC, canonical reduction of Hyperbolic equations to wave-like forms, Parabolic equations to diffusion forms, Elliptic equations to Laplace-Poisson forms, and variable-coefficient mixed-type equations exemplified by Tricomi's equation.",
        "simulations": ["sim_pde_canonical_classifier"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "General Second-Order Linear PDE: The Discriminant Δ = B² - AC",
                "content": r"""### 1. General Form of Second-Order Equations

The most general second-order linear (or semilinear) partial differential equation in two independent variables $(x, y)$ is:
$$A(x, y) u_{xx} + 2B(x, y) u_{xy} + C(x, y) u_{yy} + D(x, y) u_x + E(x, y) u_y + F(x, y) u = G(x, y)$$
where $A, B, C, D, E, F, G$ are real-valued continuous functions on a domain $\Omega \subseteq \mathbb{R}^2$, with $A^2 + B^2 + C^2 \ne 0$.
(Note: The convention $2B$ is standard in academic mathematics so that the discriminant takes the clean form $\Delta = B^2 - AC$).

The principal part containing the highest-order derivatives is the differential operator:
$$\mathcal{L}_0 = A \frac{\partial^2}{\partial x^2} + 2B \frac{\partial^2}{\partial x \partial y} + C \frac{\partial^2}{\partial y^2}$$
Associated with $\mathcal{L}_0$ is the **characteristic polynomial** (quadratic form) in variables $(\xi_1, \xi_2)$:
$$Q(\xi_1, \xi_2) = A \xi_1^2 + 2B \xi_1 \xi_2 + C \xi_2^2$$

---

### 2. Classification Criteria

> **Definition 3.1 (Discriminant and PDE Classification):**
> The **discriminant** (or indicator) of the second-order equation is defined at each point $(x, y) \in \Omega$ by:
> $$\Delta(x, y) = [B(x, y)]^2 - A(x, y) C(x, y)$$
> The PDE is classified at $(x, y)$ as:
> 1. **Hyperbolic** if $\Delta(x, y) > 0$ (analogous to the hyperbola $B^2 - AC > 0$).
> 2. **Parabolic** if $\Delta(x, y) = 0$ (analogous to the parabola $B^2 - AC = 0$).
> 3. **Elliptic** if $\Delta(x, y) < 0$ (analogous to the ellipse $B^2 - AC < 0$).
>
> If an equation retains the same type at all points of $\Omega$, it is of **pure type**; if $\Delta(x, y)$ changes sign across $\Omega$, it is of **mixed type**.

---

### 3. Coordinate Invariance of the Discriminant

Let $(\xi, \eta) = (\phi(x, y), \psi(x, y))$ be a non-singular $C^2$ change of variables with non-vanishing Jacobian:
$$J = \frac{\partial(\xi, \eta)}{\partial(x, y)} = \xi_x \eta_y - \xi_y \eta_x \ne 0$$
By the multivariable chain rule:
$$u_x = u_\xi \xi_x + u_\eta \eta_x, \qquad u_y = u_\xi \xi_y + u_\eta \eta_y$$
Differentiating again:
$$u_{xx} = u_{\xi\xi} \xi_x^2 + 2u_{\xi\eta} \xi_x \eta_x + u_{\eta\eta} \eta_x^2 + u_\xi \xi_{xx} + u_\eta \eta_{xx}$$
$$u_{xy} = u_{\xi\xi} \xi_x \xi_y + u_{\xi\eta} (\xi_x \eta_y + \xi_y \eta_x) + u_{\eta\eta} \eta_x \eta_y + u_\xi \xi_{xy} + u_\eta \eta_{xy}$$
$$u_{yy} = u_{\xi\xi} \xi_y^2 + 2u_{\xi\eta} \xi_y \eta_y + u_{\eta\eta} \eta_y^2 + u_\xi \xi_{yy} + u_\eta \eta_{yy}$$
Substituting into the PDE yields the transformed equation in coordinates $(\xi, \eta)$:
$$A^* u_{\xi\xi} + 2B^* u_{\xi\eta} + C^* u_{\eta\eta} + D^* u_\xi + E^* u_\eta + F^* u = G^*$$
where the new coefficients of the principal part are:
$$A^* = A \xi_x^2 + 2B \xi_x \xi_y + C \xi_y^2$$
$$B^* = A \xi_x \eta_x + B (\xi_x \eta_y + \xi_y \eta_x) + C \xi_y \eta_y$$
$$C^* = A \eta_x^2 + 2B \eta_x \eta_y + C \eta_y^2$$

> **Theorem 3.1 (Discriminant Invariance Theorem):**
> Under any smooth non-singular coordinate transformation, the transformed discriminant satisfies:
> $$\Delta^* = (B^*)^2 - A^* C^* = J^2 (B^2 - AC) = J^2 \Delta$$
> Since $J \ne 0$, $J^2 > 0$; therefore, the sign of the discriminant is an **absolute geometric invariant** of the PDE.

*Proof:*
Express the transformation in matrix form:
$$\begin{pmatrix} A^* & B^* \\ B^* & C^* \end{pmatrix} = \begin{pmatrix} \xi_x & \xi_y \\ \eta_x & \eta_y \end{pmatrix} \begin{pmatrix} A & B \\ B & C \end{pmatrix} \begin{pmatrix} \xi_x & \eta_x \\ \xi_y & \eta_y \end{pmatrix} = M K M^T$$
where $M = \begin{pmatrix} \xi_x & \xi_y \\ \eta_x & \eta_y \end{pmatrix}$ and $K = \begin{pmatrix} A & B \\ B & C \end{pmatrix}$.
Taking the determinant of both sides:
$$\det \begin{pmatrix} A^* & B^* \\ B^* & C^* \end{pmatrix} = \det(M) \det(K) \det(M^T) = (\det M)^2 \det(K)$$
Evaluating the determinants:
$$A^* C^* - (B^*)^2 = J^2 (AC - B^2) \implies -((B^*)^2 - A^* C^*) = -J^2 (B^2 - AC)$$
Multiplying by $-1$:
$$\Delta^* = J^2 \Delta$$
Since $J^2 > 0$, $\operatorname{sgn}(\Delta^*) = \operatorname{sgn}(\Delta)$. $\blacksquare$"""
            },
            {
                "secNumber": "3.2",
                "title": "Hyperbolic Equations: Real Characteristics & Canonical Form",
                "content": r"""### 1. Characteristic Equations for Hyperbolic PDEs

For a hyperbolic PDE, $\Delta = B^2 - AC > 0$.
We seek coordinates $(\xi, \eta)$ such that the diagonal second-derivative terms vanish:
$$A^* = 0 \quad \text{and} \quad C^* = 0$$
Recall that:
$$A^* = A \xi_x^2 + 2B \xi_x \xi_y + C \xi_y^2 = 0$$
Dividing by $\xi_y^2$ (assuming $\xi_y \ne 0$):
$$A \left(-\frac{\xi_x}{\xi_y}\right)^2 - 2B \left(-\frac{\xi_x}{\xi_y}\right) + C = 0$$
Along any level curve $\xi(x, y) = \text{constant}$, implicit differentiation gives $\frac{dy}{dx} = -\frac{\xi_x}{\xi_y}$.
Thus, the curve $y = y(x)$ satisfies the **characteristic ODE**:
$$A \left(\frac{dy}{dx}\right)^2 - 2B \left(\frac{dy}{dx}\right) + C = 0$$
Solving for the characteristic slopes $\frac{dy}{dx}$:
$$\frac{dy}{dx} = \frac{B \pm \sqrt{B^2 - AC}}{A}$$
Since $B^2 - AC > 0$, there exist **two distinct families of real characteristic curves**:
$$\frac{dy}{dx} = \frac{B + \sqrt{B^2 - AC}}{A} \implies \phi(x, y) = c_1 \implies \xi = \phi(x, y)$$
$$\frac{dy}{dx} = \frac{B - \sqrt{B^2 - AC}}{A} \implies \psi(x, y) = c_2 \implies \eta = \psi(x, y)$$

---

### 2. The Two Canonical Forms of Hyperbolic PDEs

#### Canonical Form 1 (D'Alembert Cross-Derivative Form):
Setting $\xi = \phi(x, y)$ and $\eta = \psi(x, y)$ forces $A^* = 0$ and $C^* = 0$.
Dividing through by $2B^* \ne 0$, the PDE reduces to:
$$\frac{\partial^2 u}{\partial \xi \partial \eta} = \Phi\left(\xi, \eta, u, u_\xi, u_\eta\right)$$

#### Canonical Form 2 (Wave Operator Form):
Introducing the rotated coordinates:
$$\alpha = \frac{\xi + \eta}{2}, \qquad \beta = \frac{\xi - \eta}{2}$$
We have:
$$\frac{\partial}{\partial \xi} = \frac{1}{2}\left(\frac{\partial}{\partial \alpha} + \frac{\partial}{\partial \beta}\right), \qquad \frac{\partial}{\partial \eta} = \frac{1}{2}\left(\frac{\partial}{\partial \alpha} - \frac{\partial}{\partial \beta}\right)$$
The cross-derivative transforms into:
$$u_{\xi\eta} = \frac{1}{4}(u_{\alpha\alpha} - u_{\beta\beta})$$
Thus, the equation becomes the **standard 1D wave operator**:
$$\frac{\partial^2 u}{\partial \alpha^2} - \frac{\partial^2 u}{\partial \beta^2} = \Psi\left(\alpha, \beta, u, u_\alpha, u_\beta\right)$$"""
            },
            {
                "secNumber": "3.3",
                "title": "Parabolic Equations: Single Family of Characteristics & Canonical Form",
                "content": r"""### 1. Characteristic Degeneracy in Parabolic PDEs

For a parabolic PDE, the discriminant vanishes identically:
$$\Delta = B^2 - AC = 0 \implies B^2 = AC$$
The characteristic equation:
$$A \left(\frac{dy}{dx}\right)^2 - 2B \left(\frac{dy}{dx}\right) + C = 0$$
has equal roots:
$$\frac{dy}{dx} = \frac{B}{A}$$
Therefore, there exists only **one real family of characteristic curves**:
$$\phi(x, y) = c_1 \implies \xi = \phi(x, y)$$
This single family leaves $A^* = 0$.
Furthermore, since $\Delta^* = (B^*)^2 - A^* C^* = J^2 \Delta = 0$, having $A^* = 0$ immediately forces:
$$(B^*)^2 = 0 \implies B^* = 0$$
Both $A^*$ and $B^*$ vanish automatically!

---

### 2. Reduction to Canonical Form

To complete the transformation, we choose the second coordinate $\eta = \psi(x, y)$ as **any arbitrary smooth function** that is functionally independent of $\xi$, ensuring $J \ne 0$.
(A convenient choice is often $\eta = x$ or $\eta = y$).
Since $A^* = 0$ and $B^* = 0$, while $C^* \ne 0$ (otherwise $J$ would vanish), dividing by $C^*$ yields:

> **Theorem 3.2 (Parabolic Canonical Form):**
> Every parabolic equation can be reduced to the canonical form:
> $$\frac{\partial^2 u}{\partial \eta^2} = \Phi\left(\xi, \eta, u, u_\xi, u_\eta\right)$$
> If $\Phi$ contains $u_\xi$ with non-zero coefficient, dividing produces the standard heat/diffusion form:
> $$\frac{\partial u}{\partial \xi} = k \frac{\partial^2 u}{\partial \eta^2} + \dots$$"""
            },
            {
                "secNumber": "3.4",
                "title": "Elliptic Equations: Complex Characteristics & Laplace Canonical Form",
                "content": r"""### 1. Complex Characteristics for Elliptic PDEs

For an elliptic PDE, $\Delta = B^2 - AC < 0$.
The characteristic equation:
$$A \left(\frac{dy}{dx}\right)^2 - 2B \left(\frac{dy}{dx}\right) + C = 0$$
has **no real roots**. Instead, it yields two complex conjugate characteristic slopes:
$$\frac{dy}{dx} = \frac{B \pm i \sqrt{AC - B^2}}{A}$$
Integrating these gives complex conjugate first integrals:
$$\phi(x, y) + i \psi(x, y) = c_1, \qquad \phi(x, y) - i \psi(x, y) = c_2$$

---

### 2. Real Canonical Reduction to Laplace Form

If we were to use the complex coordinates $\tilde{\xi} = \phi + i\psi$ and $\tilde{\eta} = \phi - i\psi$, the equation would reduce to $u_{\tilde{\xi}\tilde{\eta}} = \dots$, but the coordinates would be complex.
To obtain a real canonical form, we define the real transformation:
$$\xi = \phi(x, y) = \frac{\tilde{\xi} + \tilde{\eta}}{2}, \qquad \eta = \psi(x, y) = \frac{\tilde{\xi} - \tilde{\eta}}{2i}$$
By the chain rule relating $(\tilde{\xi}, \tilde{\eta})$ to $(\xi, \eta)$:
$$\frac{\partial^2 u}{\partial \tilde{\xi} \partial \tilde{\eta}} = \frac{1}{4} \left( \frac{\partial^2 u}{\partial \xi^2} + \frac{\partial^2 u}{\partial \eta^2} \right)$$
Thus, in the real coordinates $(\xi, \eta)$, the equation reduces to:

> **Theorem 3.3 (Elliptic Canonical Form):**
> Every elliptic second-order linear PDE can be transformed into the canonical form:
> $$\frac{\partial^2 u}{\partial \xi^2} + \frac{\partial^2 u}{\partial \eta^2} = \Phi\left(\xi, \eta, u, u_\xi, u_\eta\right)$$
> which is the classical **Laplace / Poisson operator** $\nabla^2 u = \Phi$."""
            },
            {
                "secNumber": "3.5",
                "title": "Second-Order PDEs with Variable Coefficients: The Tricomi Equation",
                "content": r"""### 1. Equations of Mixed Type

When the coefficients $A(x, y), B(x, y), C(x, y)$ depend on position, the sign of the discriminant $\Delta(x, y) = B^2 - AC$ may vary across the domain, producing equations of **mixed type**.
The boundary curve separating different types is the **parabolic transition curve** where $\Delta(x, y) = 0$.

---

### 2. The Tricomi Equation

The most celebrated mixed-type PDE in mathematical physics is the **Tricomi equation**, introduced by Francesco Tricomi in 1923 to model transonic fluid flow (aerodynamics near Mach 1):
$$y \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$
Here $A = y, B = 0, C = 1$. The discriminant is:
$$\Delta = B^2 - AC = 0^2 - (y)(1) = -y$$

> **Classification of Tricomi's Equation:**
> - In the upper half-plane $y > 0$: $\Delta = -y < 0 \implies$ **Elliptic** (subsonic flow, $M < 1$).
> - Along the line $y = 0$: $\Delta = 0 \implies$ **Parabolic** (sonic transition line, $M = 1$).
> - In the lower half-plane $y < 0$: $\Delta = -y > 0 \implies$ **Hyperbolic** (supersonic flow, $M > 1$).

#### Canonical Reduction in the Hyperbolic Half-Plane ($y < 0$):
The characteristic ODE is:
$$y \left(\frac{dy}{dx}\right)^2 + 1 = 0 \implies \left(\frac{dy}{dx}\right)^2 = -\frac{1}{y} = \frac{1}{-y}$$
Taking the square root:
$$\frac{dy}{dx} = \pm \frac{1}{\sqrt{-y}} \implies \sqrt{-y}\,dy = \pm dx$$
Integrating:
$$\int (-y)^{1/2}\,dy = -\frac{2}{3}(-y)^{3/2} = \pm x + c$$
Thus, the two real characteristic coordinates are:
$$\xi = x - \frac{2}{3}(-y)^{3/2}, \qquad \eta = x + \frac{2}{3}(-y)^{3/2}$$
In these coordinates, Tricomi's equation reduces to the Euler-Poisson-Darboux form:
$$u_{\xi\eta} + \frac{1}{6(\xi - \eta)}(u_\xi - u_\eta) = 0$$
Notice the characteristic curves are semi-cubical parabolas with cusps touching the sonic line $y = 0$!"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Canonical Reduction of a Constant-Coefficient Hyperbolic Equation",
                "statement": r"""Classify the following partial differential equation and reduce it to its canonical form:
$$\frac{\partial^2 u}{\partial x^2} - 4 \frac{\partial^2 u}{\partial x \partial y} + 3 \frac{\partial^2 u}{\partial y^2} = 0$$
Determine its general solution.""",
                "solution": r"""### 1. Classification
The PDE is $A u_{xx} + 2B u_{xy} + C u_{yy} = 0$ where:
$$A = 1, \qquad 2B = -4 \implies B = -2, \qquad C = 3$$
The discriminant is:
$$\Delta = B^2 - AC = (-2)^2 - (1)(3) = 4 - 3 = 1 > 0$$
Since $\Delta > 0$, the equation is strictly **Hyperbolic**.

---

### 2. Characteristic Slopes and Coordinates
The characteristic ODE is:
$$\frac{dy}{dx} = \frac{B \pm \sqrt{B^2 - AC}}{A} = \frac{-2 \pm \sqrt{1}}{1} = -2 \pm 1$$
This yields two characteristic slopes:
1. $\frac{dy}{dx} = -1 \implies dy + dx = 0 \implies y + x = c_1 \implies \xi = y + x$
2. $\frac{dy}{dx} = -3 \implies dy + 3dx = 0 \implies y + 3x = c_2 \implies \eta = y + 3x$

---

### 3. Coordinate Transformation
Let $\xi = x + y$ and $\eta = 3x + y$.
Compute partial derivatives via the chain rule:
$$\frac{\partial}{\partial x} = \xi_x \frac{\partial}{\partial \xi} + \eta_x \frac{\partial}{\partial \eta} = \frac{\partial}{\partial \xi} + 3 \frac{\partial}{\partial \eta}$$
$$\frac{\partial}{\partial y} = \xi_y \frac{\partial}{\partial \xi} + \eta_y \frac{\partial}{\partial \eta} = \frac{\partial}{\partial \xi} + \frac{\partial}{\partial \eta}$$

Now compute the second derivatives:
1. $u_{xx} = (\partial_\xi + 3\partial_\eta)^2 u = u_{\xi\xi} + 6u_{\xi\eta} + 9u_{\eta\eta}$
2. $u_{xy} = (\partial_\xi + 3\partial_\eta)(\partial_\xi + \partial_\eta) u = u_{\xi\xi} + 4u_{\xi\eta} + 3u_{\eta\eta}$
3. $u_{yy} = (\partial_\xi + \partial_\eta)^2 u = u_{\xi\xi} + 2u_{\xi\eta} + u_{\eta\eta}$

Substitute into the original equation $u_{xx} - 4u_{xy} + 3u_{yy}$:
- Coefficient of $u_{\xi\xi}$: $1 - 4(1) + 3(1) = 0$
- Coefficient of $u_{\eta\eta}$: $9 - 4(3) + 3(1) = 9 - 12 + 3 = 0$
- Coefficient of $u_{\xi\eta}$: $6 - 4(4) + 3(2) = 6 - 16 + 6 = -4$

Thus:
$$-4 \frac{\partial^2 u}{\partial \xi \partial \eta} = 0 \implies \frac{\partial^2 u}{\partial \xi \partial \eta} = 0$$
This is the **canonical form**.

---

### 4. General Solution
Integrating $\frac{\partial}{\partial \xi}\left(\frac{\partial u}{\partial \eta}\right) = 0$ with respect to $\xi$:
$$\frac{\partial u}{\partial \eta} = g(\eta)$$
Integrating with respect to $\eta$:
$$u(\xi, \eta) = f(\xi) + \int g(\eta)\,d\eta = f(\xi) + G(\eta)$$
Substituting back $\xi = x + y$ and $\eta = 3x + y$:
$$u(x, y) = f(x + y) + G(3x + y)$$
where $f$ and $G$ are arbitrary twice-differentiable functions. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Canonical Reduction of a Variable-Coefficient Equation",
                "statement": r"""Classify the variable-coefficient partial differential equation:
$$x^2 \frac{\partial^2 u}{\partial x^2} - y^2 \frac{\partial^2 u}{\partial y^2} = 0$$
in the first quadrant $x > 0, y > 0$, reduce it to canonical form, and find its general solution.""",
                "solution": r"""### 1. Classification
Here $A(x, y) = x^2, B(x, y) = 0, C(x, y) = -y^2$.
The discriminant is:
$$\Delta = B^2 - AC = 0 - (x^2)(-y^2) = x^2 y^2$$
Since $x > 0$ and $y > 0$, $\Delta = x^2 y^2 > 0$ strictly.
The equation is **Hyperbolic** throughout the entire first quadrant.

---

### 2. Characteristic Slopes and Coordinates
The characteristic equation is:
$$A \left(\frac{dy}{dx}\right)^2 + C = 0 \implies x^2 \left(\frac{dy}{dx}\right)^2 - y^2 = 0 \implies \frac{dy}{dx} = \pm \frac{y}{x}$$
Separating variables:
1. $\frac{dy}{y} = \frac{dx}{x} \implies \ln y - \ln x = c_1 \implies \frac{y}{x} = C_1 \implies \xi = \frac{y}{x}$
2. $\frac{dy}{y} = -\frac{dx}{x} \implies \ln y + \ln x = c_2 \implies x y = C_2 \implies \eta = x y$

---

### 3. Coordinate Transformation to Canonical Form
Let $\xi = y/x$ and $\eta = xy$.
Compute partial derivatives:
$$\xi_x = -y/x^2 = -\xi/x, \quad \xi_y = 1/x = \xi/y$$
$$\eta_x = y = \eta/x, \quad \eta_y = x = \eta/y$$

By the chain rule:
$$u_x = -\frac{\xi}{x} u_\xi + \frac{\eta}{x} u_\eta$$
$$u_{xx} = \frac{\xi^2}{x^2} u_{\xi\xi} - 2\frac{\xi\eta}{x^2} u_{\xi\eta} + \frac{\eta^2}{x^2} u_{\eta\eta} + \frac{2\xi}{x^2} u_\xi$$
$$u_y = \frac{\xi}{y} u_\xi + \frac{\eta}{y} u_\eta$$
$$u_{yy} = \frac{\xi^2}{y^2} u_{\xi\xi} + 2\frac{\xi\eta}{y^2} u_{\xi\eta} + \frac{\eta^2}{y^2} u_{\eta\eta}$$

Substitute into $x^2 u_{xx} - y^2 u_{yy}$:
$$x^2 u_{xx} = \xi^2 u_{\xi\xi} - 2\xi\eta u_{\xi\eta} + \eta^2 u_{\eta\eta} + 2\xi u_\xi$$
$$y^2 u_{yy} = \xi^2 u_{\xi\xi} + 2\xi\eta u_{\xi\eta} + \eta^2 u_{\eta\eta}$$
Subtracting:
$$x^2 u_{xx} - y^2 u_{yy} = -4\xi\eta u_{\xi\eta} + 2\xi u_\xi = 0$$
Dividing by $-4\xi\eta$ (since $\xi > 0, \eta > 0$):
$$\frac{\partial^2 u}{\partial \xi \partial \eta} - \frac{1}{2\eta} \frac{\partial u}{\partial \xi} = 0$$
This is the **canonical form**.

---

### 4. General Solution
Let $v = \frac{\partial u}{\partial \xi}$. The canonical equation becomes a first-order separable ODE for $v$ with respect to $\eta$:
$$\frac{\partial v}{\partial \eta} - \frac{1}{2\eta} v = 0 \implies \frac{1}{v}\frac{\partial v}{\partial \eta} = \frac{1}{2\eta}$$
Integrating with respect to $\eta$:
$$\ln v = \frac{1}{2} \ln \eta + \ln \phi(\xi) \implies v = \phi(\xi) \sqrt{\eta}$$
Since $v = u_\xi$:
$$\frac{\partial u}{\partial \xi} = \phi(\xi) \sqrt{\eta}$$
Integrating with respect to $\xi$:
$$u(\xi, \eta) = \sqrt{\eta} \int \phi(\xi)\,d\xi + \psi(\eta) = \sqrt{\eta}\,f(\xi) + \psi(\eta)$$
Substitute back $\xi = y/x$ and $\eta = xy$:
$$u(x, y) = \sqrt{xy}\,f\left(\frac{y}{x}\right) + \psi(xy)$$
where $f$ and $\psi$ are arbitrary $C^2$ functions. $\blacksquare$"""
            },
            {
                "tier": "Honors Challenge",
                "title": "Canonical Reduction of Tricomi's Equation and Singular Cusps",
                "statement": r"""Consider Tricomi's equation of mixed type:
$$y \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$
1. For $y < 0$ (the hyperbolic half-plane), derive the characteristic coordinates and reduce the equation to the Euler-Poisson-Darboux canonical form.
2. For $y > 0$ (the elliptic half-plane), determine the canonical transformation to the Laplace form.
3. Prove that the characteristic curves in the hyperbolic region form semi-cubical parabolas that terminate tangentially on the parabolic sonic line $y = 0$.""",
                "solution": r"""### 1. Canonical Reduction in the Hyperbolic Region ($y < 0$)
Here $A = y < 0, B = 0, C = 1$. The discriminant is $\Delta = -y > 0$.
The characteristic ODE is:
$$y \left(\frac{dy}{dx}\right)^2 + 1 = 0 \implies \left(\frac{dy}{dx}\right)^2 = -\frac{1}{y}$$
Taking the square root:
$$\frac{dy}{dx} = \pm \frac{1}{\sqrt{-y}} \implies \sqrt{-y}\,dy = \pm dx$$
Integrate both sides:
$$\int (-y)^{1/2}\,dy = -\frac{2}{3}(-y)^{3/2} = \pm x + c$$
Define the characteristic coordinates:
$$\xi = x - \frac{2}{3}(-y)^{3/2}, \qquad \eta = x + \frac{2}{3}(-y)^{3/2}$$
Notice that:
$$\xi - \eta = -\frac{4}{3}(-y)^{3/2} \implies (-y)^{1/2} = \left( \frac{3}{4}(\eta - \xi) \right)^{1/3}$$
Compute partial derivatives:
$$\xi_x = 1, \qquad \xi_y = -(-y)^{1/2}$$
$$\eta_x = 1, \qquad \eta_y = +(-y)^{1/2}$$
Now evaluate $u_{xx}$ and $u_{yy}$:
$$u_x = u_\xi + u_\eta \implies u_{xx} = u_{\xi\xi} + 2u_{\xi\eta} + u_{\eta\eta}$$
$$u_y = (-y)^{1/2} (-u_\xi + u_\eta)$$
$$u_{yy} = (-y)[u_{\xi\xi} - 2u_{\xi\eta} + u_{\eta\eta}] + \frac{1}{2}(-y)^{-1/2}(-1)(-u_\xi + u_\eta) = -y[u_{\xi\xi} - 2u_{\xi\eta} + u_{\eta\eta}] + \frac{1}{2(-y)^{1/2}}(u_\xi - u_\eta)$$
Substitute into $y u_{xx} + u_{yy}$:
$$y(u_{\xi\xi} + 2u_{\xi\eta} + u_{\eta\eta}) + \left( -y[u_{\xi\xi} - 2u_{\xi\eta} + u_{\eta\eta}] + \frac{1}{2(-y)^{1/2}}(u_\xi - u_\eta) \right) = 0$$
The terms $y u_{\xi\xi}$ and $y u_{\eta\eta}$ cancel completely!
$$4y u_{\xi\eta} + \frac{1}{2(-y)^{1/2}}(u_\xi - u_\eta) = 0$$
Dividing by $4y = -4(-y)$:
$$u_{\xi\eta} - \frac{1}{8(-y)^{3/2}}(u_\xi - u_\eta) = 0$$
Since $(-y)^{3/2} = \frac{3}{4}(\eta - \xi)$:
$$u_{\xi\eta} - \frac{1}{8 \cdot \frac{3}{4}(\eta - \xi)}(u_\xi - u_\eta) = 0 \implies \frac{\partial^2 u}{\partial \xi \partial \eta} + \frac{1}{6(\xi - \eta)}\left( \frac{\partial u}{\partial \xi} - \frac{\partial u}{\partial \eta} \right) = 0$$
This is the celebrated **Euler-Poisson-Darboux form**.

---

### 2. Canonical Reduction in the Elliptic Region ($y > 0$)
Here $\Delta = -y < 0$. The characteristic ODE is:
$$\frac{dy}{dx} = \pm \frac{i}{\sqrt{y}} \implies \sqrt{y}\,dy = \pm i dx \implies \frac{2}{3}y^{3/2} \mp i x = c$$
Define real coordinates:
$$\alpha = x, \qquad \beta = \frac{2}{3}y^{3/2}$$
Then $\beta_y = y^{1/2}$ and $\beta_{yy} = \frac{1}{2}y^{-1/2}$.
We have $u_{xx} = u_{\alpha\alpha}$ and:
$$u_{yy} = y u_{\beta\beta} + \frac{1}{2\sqrt{y}} u_\beta$$
Substitute into $y u_{xx} + u_{yy} = 0$:
$$y u_{\alpha\alpha} + y u_{\beta\beta} + \frac{1}{2\sqrt{y}} u_\beta = 0$$
Dividing by $y$:
$$\frac{\partial^2 u}{\partial \alpha^2} + \frac{\partial^2 u}{\partial \beta^2} + \frac{1}{3\beta}\frac{\partial u}{\partial \beta} = 0$$
This is the **canonical elliptic form**, equivalent to an axisymmetric Laplace equation in 5 dimensions!

---

### 3. Geometry of Characteristic Cusps
In the hyperbolic region, the characteristic curves satisfy:
$$x \pm \frac{2}{3}(-y)^{3/2} = c \implies -y = \left( \frac{3}{2}|x - c| \right)^{2/3} \implies y = - \left( \frac{3}{2} \right)^{2/3} (x - c)^{2/3}$$
As $y \to 0^-$, $x \to c$.
The slope of the characteristic curve is:
$$\frac{dy}{dx} = \pm \frac{1}{\sqrt{-y}} \to \pm \infty \quad \text{as } y \to 0^-$$
Thus, every characteristic curve approaches the sonic line $y = 0$ **vertically**, forming a semi-cubical cuspidal edge tangent to the normal of the sonic line! $\blacksquare$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u3 = get_unit3()
    print(f"Loaded Unit 3: {u3['title']} with {len(u3['sections'])} sections and {len(u3['problems'])} problems.")
