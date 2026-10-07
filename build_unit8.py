# -*- coding: utf-8 -*-
"""
build_unit8.py
Constructs Unit 8: Boundary Value Problems for Ordinary Differential Equations: Shooting & Finite Differences
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Boundary Value Problems for Ordinary Differential Equations: Shooting & Finite Differences",
        "leadSummary": "Mathematical formulation of two-point boundary value problems (BVPs), linear shooting via superposition, nonlinear shooting via Newton-Raphson and sensitivity variational equations, Finite Difference Methods (FDM), tridiagonal linear systems, and the Thomas algorithm (TDMA).",
        "simulations": ["sim_na_bvp_shooting"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Mathematical Formulation of Two-Point BVPs & Boundary Conditions",
                "content": r"""### 1. Two-Point Boundary Value Problems (BVPs)

In contrast to Initial Value Problems (IVPs) where all auxiliary conditions are specified at a single point $t_0$, **Boundary Value Problems (BVPs)** specify physical constraints at two or more distinct spatial endpoints $x = a$ and $x = b$.

A general second-order ODE on $x \in [a, b]$ is given by:
$$y'' = f(x, y, y'), \quad a \le x \le b$$
subject to boundary conditions at both endpoints.

---

### 2. Classification of Boundary Conditions

Boundary conditions are categorized based on function values and spatial derivatives:

#### 1. Dirichlet Boundary Conditions (First Kind):
Fixed values of the state variable at the endpoints:
$$y(a) = \alpha, \qquad y(b) = \beta$$
*Physical Example:* Prescribed temperatures at the ends of a conducting metal rod.

#### 2. Neumann Boundary Conditions (Second Kind):
Fixed values of the outward flux or derivative:
$$y'(a) = \alpha, \qquad y'(b) = \beta$$
*Physical Example:* Insulated adiabatic rod ends (zero heat flux: $y'(a) = 0$).

#### 3. Robin / Mixed Boundary Conditions (Third Kind):
Linear combinations of state values and derivatives:
$$\begin{aligned}
a_0 y(a) - a_1 y'(a) &= \alpha \\
b_0 y(b) + b_1 y'(b) &= \beta
\end{aligned}$$
with $a_0, a_1, b_0, b_1 \ge 0$ and $a_0 + a_1 > 0, b_0 + b_1 > 0$.
*Physical Example:* Newton's law of cooling / convective heat transfer at the boundary.

---

### 3. Existence and Uniqueness for Second-Order BVPs

Unlike IVPs where Picard's theorem ensures existence locally, BVPs can have **no solutions**, a **unique solution**, or **infinitely many solutions** (e.g., resonance in vibrating beams).

> **Theorem (Existence and Uniqueness for BVPs):**
> Consider the Dirichlet BVP $y'' = f(x, y, y'), y(a) = \alpha, y(b) = \beta$ on $[a, b]$. Suppose $f$ is continuous on $D = [a, b] \times \mathbb{R}^2$ and satisfies:
> 1. $\dfrac{\partial f}{\partial y}(x, y, y') > 0$ for all $(x, y, y') \in D$.
> 2. There exists a constant $M > 0$ such that $\left|\dfrac{\partial f}{\partial y'}(x, y, y')\right| \le M$ on $D$.
> 
> Then the boundary value problem has a **unique solution** $y \in C^2([a, b])$.
> *Significance of Condition 1:* Positivity $\partial f / \partial y > 0$ prevents eigenvalues from crossing zero, ruling out resonant standing wave states."""
            },
            {
                "secNumber": "8.2",
                "title": "The Linear Shooting Method: Superposition of Particular & Homogeneous Solutions",
                "content": r"""### 1. Transformation into Two Initial Value Problems

Consider a general linear second-order two-point BVP:
$$y'' = p(x) y' + q(x) y + r(x), \quad x \in [a, b]$$
with Dirichlet boundary conditions $y(a) = \alpha, y(b) = \beta$.

By the principle of linear superposition, the general solution can be written as:
$$y(x) = y_1(x) + c \, y_2(x)$$
where:
1. $y_1(x)$ solves the **non-homogeneous IVP**:
   $$\begin{cases} y_1'' = p(x) y_1' + q(x) y_1 + r(x) \\ y_1(a) = \alpha \\ y_1'(a) = 0 \end{cases}$$
2. $y_2(x)$ solves the **homogeneous IVP**:
   $$\begin{cases} y_2'' = p(x) y_2' + q(x) y_2 \\ y_2(a) = 0 \\ y_2'(a) = 1 \end{cases}$$

---

### 2. Determining the Superposition Coefficient

By construction, at the initial boundary $x = a$:
$$y(a) = y_1(a) + c \, y_2(a) = \alpha + c \cdot 0 = \alpha$$
which matches the left boundary condition automatically for any choice of $c \in \mathbb{R}$!

To satisfy the right boundary condition $y(b) = \beta$:
$$y(b) = y_1(b) + c \, y_2(b) = \beta$$
Assuming $y_2(b) \ne 0$ (which holds whenever $q(x) > 0$), we solve directly for $c$:
$$c = \frac{\beta - y_1(b)}{y_2(b)}$$

#### Computational Algorithm:
1. Convert the two second-order IVPs into two 2D first-order IVP systems.
2. Integrate both systems from $x = a$ to $x = b$ using high-order single-step methods (e.g. classical RK4).
3. Extract terminal values $y_1(b)$ and $y_2(b)$.
4. Compute $c = \frac{\beta - y_1(b)}{y_2(b)}$.
5. The initial slope is given directly by:
   $$y'(a) = y_1'(a) + c \, y_2'(a) = 0 + c(1) = c$$
6. Synthesize the complete spatial solution:
   $$y(x_n) = y_1(x_n) + c \, y_2(x_n)$$"""
            },
            {
                "secNumber": "8.3",
                "title": "The Nonlinear Shooting Method: Variational Equations & Newton-Raphson",
                "content": r"""### 1. Conceptual Framework of Nonlinear Shooting

For a nonlinear BVP:
$$\begin{cases} y'' = f(x, y, y'), \quad x \in [a, b] \\ y(a) = \alpha, \quad y(b) = \beta \end{cases}$$
superposition fails because the governing equation is nonlinear.

Instead, introduce an unknown initial slope parameter $s \in \mathbb{R}$ and define the parameter-dependent IVP:
$$\begin{cases} y'' = f(x, y, y') \\ y(a) = \alpha \\ y'(a) = s \end{cases}$$
Let $y(x; s)$ denote the solution to this IVP.
We seek a value of $s$ such that the trajectory hits the target $\beta$ at the right boundary:
$$F(s) \equiv y(b; s) - \beta = 0$$
This is a scalar root-finding problem for $s$!

---

### 2. Newton-Raphson Iteration & Variational Sensitivity Equations

Applying Newton-Raphson to $F(s) = 0$:
$$s^{(k+1)} = s^{(k)} - \frac{F(s^{(k)})}{F'(s^{(k)})} = s^{(k)} - \frac{y(b; s^{(k)}) - \beta}{\frac{\partial y}{\partial s}(b; s^{(k)})}$$
To compute the derivative $\frac{\partial y}{\partial s}(x; s)$, define the **variational sensitivity function**:
$$z(x; s) \equiv \frac{\partial y}{\partial s}(x; s)$$

Differentiating the governing ODE $y'' = f(x, y, y')$ with respect to the initial slope $s$:
$$\frac{\partial}{\partial s} \left( y'' \right) = \frac{\partial f}{\partial y} \frac{\partial y}{\partial s} + \frac{\partial f}{\partial y'} \frac{\partial y'}{\partial s}$$
Assuming smooth partial derivatives, interchange order of differentiation:
$$\frac{d^2 z}{dx^2} = f_y(x, y(x), y'(x)) z + f_{y'}(x, y(x), y'(x)) z'$$
with initial conditions obtained by differentiating the boundary constraints:
$$z(a) = \frac{\partial y}{\partial s}(a) = \frac{\partial \alpha}{\partial s} = 0$$
$$z'(a) = \frac{\partial y'}{\partial s}(a) = \frac{\partial s}{\partial s} = 1$$

#### Coupled 4D System for Nonlinear Shooting:
At each Newton iteration, integrate the coupled system of 4 first-order ODEs simultaneously from $x = a$ to $x = b$:
$$\begin{cases}
y_1' = y_2, & y_1(a) = \alpha \\
y_2' = f(x, y_1, y_2), & y_2(a) = s^{(k)} \\
z_1' = z_2, & z_1(a) = 0 \\
z_2' = f_y(x, y_1, y_2) z_1 + f_{y'}(x, y_1, y_2) z_2, & z_2(a) = 1
\end{cases}$$
Then update:
$$s^{(k+1)} = s^{(k)} - \frac{y_1(b) - \beta}{z_1(b)}$$
Repeat until $|y_1(b) - \beta| < \text{TOL}$."""
            },
            {
                "secNumber": "8.4",
                "title": "Finite Difference Methods: Discretization, Tridiagonal Systems & Thomas Algorithm",
                "content": r"""### 1. Discretization of the Domain

Instead of integrating forward in space like shooting methods, **Finite Difference Methods (FDM)** discretize the spatial domain $[a, b]$ simultaneously into $N$ subintervals of width $h = \frac{b - a}{N}$:
$$x_i = a + i h, \quad i = 0, 1, \dots, N$$
Let $w_i \approx y(x_i)$ denote the discrete numerical approximations.

Using second-order centered difference approximations:
$$y'(x_i) = \frac{w_{i+1} - w_{i-1}}{2h} - \frac{h^2}{6} y'''(\xi_i)$$
$$y''(x_i) = \frac{w_{i+1} - 2w_i + w_{i-1}}{h^2} - \frac{h^2}{12} y^{(4)}(\eta_i)$$

---

### 2. The Linear Tridiagonal System

Consider the linear BVP:
$$y'' = p(x) y' + q(x) y + r(x), \quad y(a) = \alpha, \quad y(b) = \beta$$
Substituting centered differences at interior grid points $i = 1, 2, \dots, N-1$:
$$\frac{w_{i+1} - 2w_i + w_{i-1}}{h^2} = p(x_i) \left( \frac{w_{i+1} - w_{i-1}}{2h} \right) + q(x_i) w_i + r(x_i)$$
Multiplying through by $-h^2$ and collecting terms:
$$-\left( 1 + \frac{h}{2} p(x_i) \right) w_{i-1} + \left( 2 + h^2 q(x_i) \right) w_i - \left( 1 - \frac{h}{2} p(x_i) \right) w_{i+1} = -h^2 r(x_i)$$
Set:
$$a_i = -\left( 1 + \frac{h}{2} p_i \right), \quad d_i = 2 + h^2 q_i, \quad c_i = -\left( 1 - \frac{h}{2} p_i \right), \quad b_i = -h^2 r_i$$
This forms an $(N-1) \times (N-1)$ tridiagonal linear system:
$$\begin{bmatrix}
d_1 & c_1 & & & 0 \\
a_2 & d_2 & c_2 & & \\
& a_3 & d_3 & \ddots & \\
& & \ddots & \ddots & c_{N-2} \\
0 & & & a_{N-1} & d_{N-1}
\end{bmatrix}
\begin{bmatrix}
w_1 \\ w_2 \\ w_3 \\ \vdots \\ w_{N-1}
\end{bmatrix}
=
\begin{bmatrix}
b_1 - a_1 \alpha \\
b_2 \\
b_3 \\
\vdots \\
b_{N-1} - c_{N-1} \beta
\end{bmatrix}$$

---

### 3. The Thomas Algorithm (TDMA)

The Tridiagonal Matrix Algorithm (TDMA) is a specialized $\mathcal{O}(N)$ Gaussian elimination method that bypasses the general $\mathcal{O}(N^3)$ complexity:
1. **Forward Sweep (Eliminate lower diagonal $a_i$):**
   $$\begin{aligned}
   c_1' &= \frac{c_1}{d_1}, \quad d_1^* = \frac{b_1^*}{d_1} \\
   c_i' &= \frac{c_i}{d_i - a_i c_{i-1}'}, \quad d_i^* = \frac{b_i^* - a_i d_{i-1}^*}{d_i - a_i c_{i-1}'} \quad (i = 2, \dots, N-1)
   \end{aligned}$$
2. **Backward Substitution:**
   $$\begin{aligned}
   w_{N-1} &= d_{N-1}^* \\
   w_i &= d_i^* - c_i' w_{i+1} \quad (i = N-2, N-3, \dots, 1)
   \end{aligned}$$
*Total Operation Count:* Exactly $5(N-1)$ additions and multiplications—massively faster and numerically stable whenever $q(x) > 0$ (strict diagonal dominance)."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Analytical Superposition in the Linear Shooting Method",
                "statement": r"Consider the linear two-point BVP: $$y'' - 4y = 0, \quad x \in [0, 1], \quad y(0) = 1, \quad y(1) = 3$$ 1. Find the exact analytical solutions $y_1(x)$ and $y_2(x)$ to the corresponding non-homogeneous and homogeneous IVPs. 2. Calculate the exact initial slope $s = y'(0)$ via shooting superposition. 3. Verify that the synthesized solution satisfies $y(1) = 3$.",
                "hints": [
                    "For $y'' - 4y = 0$, general solution is $c_1 \\cosh(2x) + c_2 \\sinh(2x)$.",
                    "For $y_1$: $y_1(0)=1, y_1'(0)=0$. For $y_2$: $y_2(0)=0, y_2'(0)=1$."
                ],
                "solution": r"""**Step 1: Solve the Two IVPs Analytically**
The characteristic equation is $r^2 - 4 = 0 \implies r = \pm 2$.
General solution form: $y(x) = A \cosh(2x) + B \sinh(2x)$.

1. **First IVP ($y_1$):**
   $$\begin{cases} y_1'' - 4y_1 = 0 \\ y_1(0) = 1 \\ y_1'(0) = 0 \end{cases}$$
   $y_1(0) = A = 1$.
   $y_1'(x) = 2A \sinh(2x) + 2B \cosh(2x) \implies y_1'(0) = 2B = 0 \implies B = 0$.
   Thus:
   $$y_1(x) = \cosh(2x)$$

2. **Second IVP ($y_2$):**
   $$\begin{cases} y_2'' - 4y_2 = 0 \\ y_2(0) = 0 \\ y_2'(0) = 1 \end{cases}$$
   $y_2(0) = A = 0$.
   $y_2'(0) = 2B = 1 \implies B = \frac{1}{2}$.
   Thus:
   $$y_2(x) = \frac{1}{2} \sinh(2x)$$

---

**Step 2: Superposition and Initial Slope Calculation**
Evaluate both solutions at the terminal point $x = 1$:
$$y_1(1) = \cosh(2) \approx 3.7621957$$
$$y_2(1) = \frac{1}{2} \sinh(2) \approx \frac{1}{2}(3.6268604) = 1.8134302$$
The target boundary condition is $y(1) = \beta = 3$.
Set $y(1) = y_1(1) + c \, y_2(1) = 3$:
$$c = \frac{3 - y_1(1)}{y_2(1)} = \frac{3 - \cosh(2)}{\frac{1}{2}\sinh(2)} = \frac{2(3 - \cosh(2))}{\sinh(2)}$$
Evaluating numerically:
$$c = \frac{3 - 3.7621957}{1.8134302} = \frac{-0.7621957}{1.8134302} \approx -0.420306$$
Since $y_1'(0) = 0$ and $y_2'(0) = 1$, the exact required shooting slope is:
$$s = y'(0) = y_1'(0) + c \, y_2'(0) = c \approx -0.420306$$

---

**Step 3: Verification**
The complete spatial solution is:
$$y(x) = \cosh(2x) - 0.420306 \cdot \frac{1}{2} \sinh(2x) = \cosh(2x) - 0.210153 \sinh(2x)$$
At $x = 0$: $y(0) = \cosh(0) - 0 = 1$ (matches left boundary).
At $x = 1$: $y(1) = 3.762196 - 0.210153(3.626860) = 3.762196 - 0.762196 = 3.000000$ (matches right boundary exactly)."""
            },
            {
                "tier": "Advanced",
                "title": "Finite Difference Discretization and Tridiagonal Thomas Algorithm Solve",
                "statement": r"Consider the linear boundary value problem: $$y'' + 2y' - y = x, \quad x \in [0, 1], \quad y(0) = 0, \quad y(1) = 1$$ Discretize the problem using centered finite differences with $h = 0.25$ ($N = 4$, interior points $x_1=0.25, x_2=0.5, x_3=0.75$). 1. Formulate the explicit $3 \times 3$ tridiagonal linear system $A\vec{w} = \vec{b}$. 2. Solve the linear system using the Thomas algorithm (TDMA) to find $(w_1, w_2, w_3)$.",
                "hints": [
                    "Centered differences: $y'' \\approx \\frac{w_{i-1} - 2w_i + w_{i+1}}{h^2}$, $y' \\approx \\frac{w_{i+1} - w_{i-1}}{2h}$.",
                    "Here $h=0.25 \\implies h^2 = 0.0625$, $\\frac{1}{h^2} = 16$, $\\frac{1}{2h} = 2$."
                ],
                "solution": r"""**Step 1: Discretization and Matrix Formulation**
With $h = 0.25$:
$$\frac{w_{i-1} - 2w_i + w_{i+1}}{h^2} + 2 \left( \frac{w_{i+1} - w_{i-1}}{2h} \right) - w_i = x_i$$
Multiplying by $h^2 = \frac{1}{16} = 0.0625$:
$$(w_{i-1} - 2w_i + w_{i+1}) + 2h \cdot \frac{w_{i+1} - w_{i-1}}{2} - h^2 w_i = h^2 x_i$$
$$(w_{i-1} - 2w_i + w_{i+1}) + h (w_{i+1} - w_{i-1}) - h^2 w_i = h^2 x_i$$
Collecting coefficients of $w_{i-1}, w_i, w_{i+1}$:
$$(1 - h) w_{i-1} - (2 + h^2) w_i + (1 + h) w_{i+1} = h^2 x_i$$
Multiplying by $-1$:
$$-(1 - h) w_{i-1} + (2 + h^2) w_i - (1 + h) w_{i+1} = -h^2 x_i$$

With $h = 0.25$:
- $1 - h = 1 - 0.25 = 0.75$
- $2 + h^2 = 2 + 0.0625 = 2.0625$
- $1 + h = 1 + 0.25 = 1.25$
- $h^2 = 0.0625$

General difference equation for $i = 1, 2, 3$:
$$-0.75 w_{i-1} + 2.0625 w_i - 1.25 w_{i+1} = -0.0625 x_i$$

Boundary conditions: $w_0 = y(0) = 0$, $w_4 = y(1) = 1$.

- **For $i = 1$ ($x_1 = 0.25$):**
  $$-0.75(0) + 2.0625 w_1 - 1.25 w_2 = -0.0625(0.25) = -0.015625$$
  $$2.0625 w_1 - 1.25 w_2 = -0.015625$$
- **For $i = 2$ ($x_2 = 0.50$):**
  $$-0.75 w_1 + 2.0625 w_2 - 1.25 w_3 = -0.0625(0.50) = -0.03125$$
- **For $i = 3$ ($x_3 = 0.75$):**
  $$-0.75 w_2 + 2.0625 w_3 - 1.25(1) = -0.0625(0.75) = -0.046875$$
  $$-0.75 w_2 + 2.0625 w_3 = 1.25 - 0.046875 = 1.203125$$

The $3 \times 3$ tridiagonal linear system is:
$$\begin{bmatrix} 2.0625 & -1.25 & 0 \\ -0.75 & 2.0625 & -1.25 \\ 0 & -0.75 & 2.0625 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} -0.015625 \\ -0.03125 \\ 1.203125 \end{bmatrix}$$

---

**Step 2: TDMA (Thomas Algorithm) Solve**

1. **Forward Elimination:**
   - Row 1:
     $$c_1' = \frac{-1.25}{2.0625} \approx -0.606061, \quad d_1^* = \frac{-0.015625}{2.0625} \approx -0.007576$$
   - Row 2:
     $$\text{denom}_2 = d_2 - a_2 c_1' = 2.0625 - (-0.75)(-0.606061) = 2.0625 - 0.454546 = 1.607954$$
     $$c_2' = \frac{-1.25}{1.607954} \approx -0.777385$$
     $$d_2^* = \frac{b_2 - a_2 d_1^*}{\text{denom}_2} = \frac{-0.03125 - (-0.75)(-0.007576)}{1.607954} = \frac{-0.03125 - 0.005682}{1.607954} = \frac{-0.036932}{1.607954} \approx -0.022968$$
   - Row 3:
     $$\text{denom}_3 = d_3 - a_3 c_2' = 2.0625 - (-0.75)(-0.777385) = 2.0625 - 0.583039 = 1.479461$$
     $$d_3^* = \frac{b_3 - a_3 d_2^*}{\text{denom}_3} = \frac{1.203125 - (-0.75)(-0.022968)}{1.479461} = \frac{1.203125 - 0.017226}{1.479461} = \frac{1.185899}{1.479461} \approx 0.801575$$

2. **Backward Substitution:**
   - $w_3 = d_3^* = 0.801575$
   - $w_2 = d_2^* - c_2' w_3 = -0.022968 - (-0.777385)(0.801575) = -0.022968 + 0.623133 = 0.600165$
   - $w_1 = d_1^* - c_1' w_2 = -0.007576 - (-0.606061)(0.600165) = -0.007576 + 0.363736 = 0.356160$

Computed solution vector:
$$\vec{w} \approx \begin{bmatrix} w(0.25) \\ w(0.50) \\ w(0.75) \end{bmatrix} = \begin{bmatrix} 0.3562 \\ 0.6002 \\ 0.8016 \end{bmatrix}$$"""
            },
            {
                "tier": "Rigorous Examination / Derivation",
                "title": "Derivation of the Variational Sensitivity Equations for Nonlinear Shooting",
                "statement": r"Consider the nonlinear two-point Dirichlet boundary value problem: $$y'' = f(x, y, y'), \quad x \in [a, b], \quad y(a) = \alpha, \quad y(b) = \beta$$ Let $y(x; s)$ denote the parameter-dependent solution of the initial value problem with initial slope $y'(a) = s$. 1. Prove that the sensitivity function $z(x; s) \equiv \frac{\partial y}{\partial s}(x; s)$ satisfies the linear second-order IVP: $$z'' = \frac{\partial f}{\partial y}(x, y, y') z + \frac{\partial f}{\partial y'}(x, y, y') z', \quad z(a) = 0, \quad z'(a) = 1$$ 2. Formulate the exact Newton-Raphson shooting iteration $s^{(k+1)}$ for finding the boundary root $y(b; s) - \beta = 0$, proving that its local convergence rate is quadratic under standard regularity assumptions.",
                "hints": [
                    "Differentiate the identity $\\frac{d^2}{dx^2}[y(x; s)] = f(x, y(x; s), y'(x; s))$ with respect to $s$ using Schwarz's theorem on mixed partials.",
                    "Recall the standard Newton-Raphson quadratic convergence theorem for $F(s) = y(b; s) - \\beta$."
                ],
                "solution": r"""**Part 1: Derivation of the Variational Sensitivity IVP**

Let $y(x; s)$ be the solution of:
$$\begin{cases} \dfrac{\partial^2 y}{\partial x^2}(x; s) = f\left(x, y(x; s), \dfrac{\partial y}{\partial x}(x; s)\right) \\ y(a; s) = \alpha \\ \dfrac{\partial y}{\partial x}(a; s) = s \end{cases}$$
Assuming $f$ has continuous second partial derivatives, by Schwarz's theorem the mixed partial derivatives commute:
$$\frac{\partial}{\partial s} \left( \frac{\partial^2 y}{\partial x^2} \right) = \frac{\partial^2}{\partial x^2} \left( \frac{\partial y}{\partial s} \right)$$
Define $z(x; s) \equiv \frac{\partial y}{\partial s}(x; s)$. Then:
$$\frac{\partial^2 z}{\partial x^2} = \frac{\partial}{\partial s} \left[ f\left(x, y(x; s), \frac{\partial y}{\partial x}(x; s)\right) \right]$$
Applying the multi-variable chain rule to the right-hand side:
$$\frac{\partial}{\partial s} [f] = \frac{\partial f}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial f}{\partial y} \frac{\partial y}{\partial s} + \frac{\partial f}{\partial y'} \frac{\partial}{\partial s} \left( \frac{\partial y}{\partial x} \right)$$
Since $x$ is independent of $s$, $\frac{\partial x}{\partial s} = 0$.
Interchanging derivatives in the last term:
$$\frac{\partial}{\partial s} \left( \frac{\partial y}{\partial x} \right) = \frac{\partial}{\partial x} \left( \frac{\partial y}{\partial s} \right) = \frac{\partial z}{\partial x}$$
Therefore:
$$z''(x) = \frac{\partial f}{\partial y}(x, y(x; s), y'(x; s)) \, z(x) + \frac{\partial f}{\partial y'}(x, y(x; s), y'(x; s)) \, z'(x)$$
This is a **linear** second-order differential equation in $z(x)$ whose variable coefficients depend on the trajectory $y(x; s)$.

Now determine the initial conditions for $z$ at $x = a$:
1. $z(a) = \frac{\partial y}{\partial s}(a; s) = \frac{\partial}{\partial s}[\alpha] = 0$ (since $\alpha$ is a fixed constant independent of $s$).
2. $z'(a) = \frac{\partial}{\partial x}\left( \frac{\partial y}{\partial s} \right)_{x=a} = \frac{\partial}{\partial s} \left( \frac{\partial y}{\partial x}(a; s) \right) = \frac{\partial}{\partial s}[s] = 1$.
This completes the derivation of the variational sensitivity IVP. $\blacksquare$

---

**Part 2: Newton-Raphson Iteration and Proof of Quadratic Convergence**

The target shooting condition at $x = b$ is:
$$F(s) \equiv y(b; s) - \beta = 0$$
The derivative of $F$ with respect to $s$ is:
$$F'(s) = \frac{\partial}{\partial s}[y(b; s) - \beta] = \frac{\partial y}{\partial s}(b; s) = z(b; s)$$
Applying Newton-Raphson's method:
$$s^{(k+1)} = s^{(k)} - \frac{F(s^{(k)})}{F'(s^{(k)})} = s^{(k)} - \frac{y(b; s^{(k)}) - \beta}{z(b; s^{(k)})}$$

#### Proof of Local Quadratic Convergence:
Let $s^*$ be the exact root such that $F(s^*) = y(b; s^*) - \beta = 0$.
Assume:
1. $F'(s^*) = z(b; s^*) \ne 0$ (no bifurcation / non-singular Jacobian).
2. $F''(s)$ is bounded in a neighborhood $U$ of $s^*$: $|F''(s)| \le M_2$.

Expanding $F(s^*)$ in a Taylor series about $s^{(k)}$:
$$0 = F(s^*) = F(s^{(k)}) + F'(s^{(k)})(s^* - s^{(k)}) + \frac{F''(\xi_k)}{2} (s^* - s^{(k)})^2$$
From the Newton iteration:
$$F(s^{(k)}) = F'(s^{(k)})(s^{(k)} - s^{(k+1)})$$
Substituting this into the Taylor expansion:
$$0 = F'(s^{(k)})(s^{(k)} - s^{(k+1)}) + F'(s^{(k)})(s^* - s^{(k)}) + \frac{F''(\xi_k)}{2} (s^* - s^{(k)})^2$$
$$F'(s^{(k)})(s^* - s^{(k+1)}) = -\frac{F''(\xi_k)}{2} (s^* - s^{(k)})^2$$
Dividing by $F'(s^{(k)})$:
$$s^{(k+1)} - s^* = \frac{F''(\xi_k)}{2 F'(s^{(k)})} (s^{(k)} - s^*)^2$$
Taking absolute values:
$$|s^{(k+1)} - s^*| \le \frac{M_2}{2 \min |F'(s)|} |s^{(k)} - s^*|^2 = C |s^{(k)} - s^*|^2$$
This proves that the error at step $k+1$ is proportional to the square of the error at step $k$, establishing **quadratic asymptotic convergence ($\mathcal{O}(|e_k|^2)$)**. $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u = get_unit8()
    print("Unit 8 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
