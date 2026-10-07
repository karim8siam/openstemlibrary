# -*- coding: utf-8 -*-
"""
build_unit5.py
Constructs Unit 5: Initial Value Problems for Ordinary Differential Equations: Single-Step Methods
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Initial Value Problems for Ordinary Differential Equations: Single-Step Methods",
        "leadSummary": "Comprehensive formulation of Initial Value Problems (IVPs), Picard's existence-uniqueness iteration, Taylor series expansions, explicit Runge-Kutta frameworks (Heun, Midpoint, classical RK4), Butcher tableaux, order condition derivations, and embedded adaptive pairs.",
        "simulations": ["sim_na_ode_single_step"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Mathematical Formulation of IVPs, Picard's Existence-Uniqueness Theorem & Successive Approximations",
                "content": r"""### 1. The General Initial Value Problem (IVP)

Consider the first-order ordinary differential equation with prescribed initial state:
$$\begin{cases} \dfrac{dy}{dt} = f(t, y), \quad t \in [t_0, T] \\ y(t_0) = y_0 \end{cases}$$
where $y: [t_0, T] \to \mathbb{R}^d$ and $f: [t_0, T] \times \mathbb{R}^d \to \mathbb{R}^d$.

#### Equivalent Volterra Integral Equation:
Integrating both sides over $[t_0, t]$ yields:
$$y(t) = y_0 + \int_{t_0}^t f(s, y(s)) \, ds$$
This integral formulation converts the differential equation into a fixed-point problem over the Banach space $C([t_0, T], \mathbb{R}^d)$.

---

### 2. The Picard-Lindelöf Existence and Uniqueness Theorem

> **Theorem (Picard-Lindelöf):**
> Let $D = [t_0 - a, t_0 + a] \times \overline{B}(y_0, b) \subset \mathbb{R} \times \mathbb{R}^d$. Suppose:
> 1. $f(t, y)$ is continuous on $D$, with $M = \max_{(t, y) \in D} \|f(t, y)\| < \infty$.
> 2. $f(t, y)$ satisfies a uniform Lipschitz condition with respect to $y$ on $D$:
>    $$\|f(t, u) - f(t, v)\| \le L \|u - v\|, \quad \forall (t, u), (t, v) \in D$$
> 
> Then there exists a unique continuously differentiable solution $y(t)$ to the IVP on the interval $I = [t_0 - h, t_0 + h]$, where $h = \min\left(a, \frac{b}{M}\right)$.

#### Picard's Method of Successive Approximations:
Define the operator $T: C(I) \to C(I)$ by:
$$(T y)(t) = y_0 + \int_{t_0}^t f(s, y(s)) \, ds$$
Starting from the constant initial guess $y^{(0)}(t) \equiv y_0$, generate the sequence:
$$y^{(k+1)}(t) = y_0 + \int_{t_0}^t f(s, y^{(k)}(s)) \, ds, \quad k = 0, 1, 2, \dots$$

#### Proof of Uniform Convergence:
For any $t \in [t_0, t_0 + h]$:
$$\|y^{(1)}(t) - y^{(0)}(t)\| = \left\|\int_{t_0}^t f(s, y_0) \, ds\right\| \le M (t - t_0)$$
By induction:
$$\|y^{(k+1)}(t) - y^{(k)}(t)\| \le \frac{M L^k}{(k+1)!} (t - t_0)^{k+1} \le \frac{M L^k h^{k+1}}{(k+1)!}$$
Since the infinite series:
$$\sum_{k=0}^\infty \frac{M L^k h^{k+1}}{(k+1)!} = \frac{M}{L} \left(e^{Lh} - 1\right) < \infty$$
converges, the Weierstrass M-test guarantees that the sequence of continuous functions $\{y^{(k)}(t)\}$ converges uniformly on $I$ to a unique limit $y^*(t) = \lim_{k \to \infty} y^{(k)}(t)$. Taking the limit under the integral sign proves $y^*(t) = T y^*(t)$."""
            },
            {
                "secNumber": "5.2",
                "title": "Taylor Series Methods & Euler's Method: Derivation, Truncation Error & Limitations",
                "content": r"""### 1. High-Order Taylor Series Method

Assuming $f(t, y)$ is $p$-times continuously differentiable, the exact solution $y(t)$ can be expanded about $t_n$ using Taylor's theorem:
$$y(t_{n+1}) = y(t_n + h) = y(t_n) + h y'(t_n) + \frac{h^2}{2!} y''(t_n) + \dots + \frac{h^p}{p!} y^{(p)}(t_n) + \frac{h^{p+1}}{(p+1)!} y^{(p+1)}(\xi_n)$$
where $\xi_n \in (t_n, t_{n+1})$.

Using the chain rule, total derivatives of $y(t)$ are evaluated directly from the governing ODE:
$$\begin{aligned}
y'(t) &= f(t, y) \\
y''(t) &= \frac{df}{dt} = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial y} y' = f_t + f f_y \\
y'''(t) &= f_{tt} + 2 f f_{ty} + f^2 f_{yy} + f_y(f_t + f f_y)
\end{aligned}$$

#### The Taylor Method of Order $p$:
$$y_{n+1} = y_n + h T_p(t_n, y_n; h)$$
where the increment function is:
$$T_p(t, y; h) = f(t, y) + \frac{h}{2!} f'(t, y) + \dots + \frac{h^{p-1}}{p!} f^{(p-1)}(t, y)$$
*Fatal Practical Limitation:* For systems of ODEs or complex nonlinear functions $f$, computing high-order total derivatives analytically requires nested symbolic chain rules whose algebraic complexity explodes exponentially (the "curse of differentiation").

---

### 2. Forward Euler's Method ($p = 1$)

Truncating after the linear term yields the simplest numerical integrator:
$$y_{n+1} = y_n + h f(t_n, y_n)$$

#### Error Analysis:
- **Local Truncation Error (LTE):**
  $$d_{n+1} = y(t_{n+1}) - \left[ y(t_n) + h f(t_n, y(t_n)) \right] = \frac{h^2}{2} y''(\xi_n) = \mathcal{O}(h^2)$$
- **Local Error per unit step:** $\tau_{n+1} = \frac{d_{n+1}}{h} = \mathcal{O}(h)$.
- **Global Truncation Error (GTE):** Over a fixed interval $[t_0, T]$ with $N = (T - t_0)/h$ steps, errors accumulate:
  $$E_N = |y(T) - y_N| \le \mathcal{O}(N \cdot h^2) = \mathcal{O}(h)$$
  Hence, Forward Euler is only **first-order accurate**. To halve the error, computational work must double."""
            },
            {
                "secNumber": "5.3",
                "title": "Explicit Runge-Kutta Families: Geometric Motivation, 2nd-Order Schemes & Butcher Tableaux",
                "content": r"""### 1. General Philosophy of Runge-Kutta Methods

The core innovation of Carl Runge (1895) and Wilhelm Kutta (1901) was to **match the Taylor series expansion up to order $p$ using only evaluations of $f(t, y)$ at intermediate points**, completely bypassing analytic differentiation.

An explicit $s$-stage Runge-Kutta (ERK) method advances from $(t_n, y_n)$ to $t_{n+1} = t_n + h$ via:
$$y_{n+1} = y_n + h \sum_{i=1}^s b_i k_i$$
where stage derivatives $k_i$ are sampled sequentially:
$$\begin{aligned}
k_1 &= f(t_n, y_n) \\
k_2 &= f(t_n + c_2 h, \, y_n + h a_{21} k_1) \\
k_3 &= f(t_n + c_3 h, \, y_n + h (a_{31} k_1 + a_{32} k_2)) \\
&\;\;\vdots \\
k_s &= f\left(t_n + c_s h, \, y_n + h \sum_{j=1}^{s-1} a_{sj} k_j\right)
\end{aligned}$$

---

### 2. The Butcher Tableau Representation

John C. Butcher formalized Runge-Kutta schemes into a compact matrix-vector tableau:
$$\begin{array}{c|cccc}
0 & & & & \\
c_2 & a_{21} & & & \\
c_3 & a_{31} & a_{32} & & \\
\vdots & \vdots & \vdots & \ddots & \\
c_s & a_{s1} & a_{s2} & \dots & a_{s, s-1} \\
\hline
& b_1 & b_2 & \dots & b_s
\end{array}
\iff
\begin{array}{c|c}
\vec{c} & A \\
\hline
& \vec{b}^T
\end{array}$$
where $c_i = \sum_{j=1}^{i-1} a_{ij}$ ensures internal stage consistency (zero-order consistency for autonomous systems).

---

### 3. Family of Two-Stage Second-Order Runge-Kutta Methods (RK2)

For $s = 2$:
$$\begin{aligned}
k_1 &= f(t_n, y_n) \\
k_2 &= f(t_n + c_2 h, \, y_n + h a_{21} k_1) \\
y_{n+1} &= y_n + h (b_1 k_1 + b_2 k_2)
\end{aligned}$$

#### Expanding in Bivariate Taylor Series:
Expanding $k_2 = f(t_n + c_2 h, y_n + h a_{21} f)$ about $(t_n, y_n)$:
$$k_2 = f + h \left( c_2 f_t + a_{21} f f_y \right) + \mathcal{O}(h^2)$$
Substituting into the numerical update:
$$y_{n+1} = y_n + h (b_1 + b_2) f + h^2 b_2 (c_2 f_t + a_{21} f f_y) + \mathcal{O}(h^3)$$
Comparing with the exact Taylor series:
$$y(t_n + h) = y(t_n) + h f + \frac{h^2}{2} (f_t + f f_y) + \mathcal{O}(h^3)$$
Equating coefficients of powers of $h$ and elementary differentials:
1. $h^1$ term: $b_1 + b_2 = 1$
2. $h^2 f_t$ term: $b_2 c_2 = \frac{1}{2}$
3. $h^2 f f_y$ term: $b_2 a_{21} = \frac{1}{2}$

This gives 3 nonlinear equations in 4 unknowns ($b_1, b_2, c_2, a_{21}$), yielding a **one-parameter family of second-order methods** where $a_{21} = c_2$ and $b_2 = \frac{1}{2 c_2}$, $b_1 = 1 - \frac{1}{2 c_2}$ for any $c_2 \ne 0$:

#### Famous Members of the RK2 Family:
1. **Explicit Midpoint Method ($c_2 = 1/2$):**
   $$b_1 = 0, \quad b_2 = 1, \quad a_{21} = 1/2 \implies y_{n+1} = y_n + h f\left(t_n + \frac{h}{2}, \, y_n + \frac{h}{2} k_1\right)$$
2. **Heun's Method / Improved Euler ($c_2 = 1$):**
   $$b_1 = 1/2, \quad b_2 = 1/2, \quad a_{21} = 1 \implies y_{n+1} = y_n + \frac{h}{2} \left[ k_1 + f(t_n + h, y_n + h k_1) \right]$$
3. **Ralston's Method ($c_2 = 2/3$):**
   Minimizes the truncation error bound: $b_1 = 1/4$, $b_2 = 3/4$, $a_{21} = 2/3$."""
            },
            {
                "secNumber": "5.4",
                "title": "The Classical Fourth-Order Runge-Kutta Method (RK4): Derivation & Implementation",
                "content": r"""### 1. The Classical RK4 Formula

The fourth-order Runge-Kutta method (often referred to simply as *the* Runge-Kutta method) is given by:
$$\begin{aligned}
k_1 &= f(t_n, y_n) \\
k_2 &= f\left(t_n + \frac{h}{2}, \, y_n + \frac{h}{2} k_1\right) \\
k_3 &= f\left(t_n + \frac{h}{2}, \, y_n + \frac{h}{2} k_2\right) \\
k_4 &= f(t_n + h, \, y_n + h k_3) \\
y_{n+1} &= y_n + \frac{h}{6} \left( k_1 + 2 k_2 + 2 k_3 + k_4 \right)
\end{aligned}$$

#### Butcher Tableau for Classical RK4:
$$\begin{array}{c|cccc}
0 & 0 & 0 & 0 & 0 \\
1/2 & 1/2 & 0 & 0 & 0 \\
1/2 & 0 & 1/2 & 0 & 0 \\
1 & 0 & 0 & 1 & 0 \\
\hline
& 1/6 & 2/6 & 2/6 & 1/6
\end{array}$$
Notice the weights $\vec{b} = \left[\frac{1}{6}, \frac{2}{6}, \frac{2}{6}, \frac{1}{6}\right]^T$, which correspond exactly to Simpson's $1/3$ rule weights across the interval $[t_n, t_{n+1}]$!

---

### 2. Derivation of Order Conditions via B-Series and Trees

For an explicit Runge-Kutta method to achieve order $p = 4$, the numerical expansion must match the Taylor series expansion for all rooted trees up to order 4:
1. **Order 1 (1 condition):** $\sum b_i = 1$
2. **Order 2 (1 condition):** $\sum b_i c_i = 1/2$
3. **Order 3 (2 conditions):**
   - $\sum b_i c_i^2 = 1/3$
   - $\sum b_i a_{ij} c_j = 1/6$
4. **Order 4 (4 conditions):**
   - $\sum b_i c_i^3 = 1/4$
   - $\sum b_i c_i a_{ij} c_j = 1/8$
   - $\sum b_i a_{ij} c_j^2 = 1/12$
   - $\sum b_i a_{ij} a_{jk} c_k = 1/24$

Together, these form a system of 8 nonlinear algebraic equations for the coefficients $\{a_{ij}, b_i, c_i\}$. The classical RK4 coefficients satisfy all 8 conditions identically, resulting in:
$$\text{Local Truncation Error: } d_{n+1} = \mathcal{O}(h^5) \implies \text{Global Error: } E_N = \mathcal{O}(h^4)$$

---

### 3. Butcher's Barrier Theorem for Higher Orders

A remarkable mathematical property discovered by J. C. Butcher is that the minimum number of stages $s(p)$ required to achieve order $p$ satisfies:
$$\begin{array}{c|cccccccc}
\text{Order } p & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hline
\text{Min Stages } s & 1 & 2 & 3 & 4 & 6 & 7 & 9 & 11
\end{array}$$

> **Theorem (Butcher's First Barrier):**
> No explicit Runge-Kutta method of order $p \ge 5$ can have $s = p$ stages. Specifically, an order 5 explicit RK method requires at least $s = 6$ stages!
> This explains why RK4 is universally regarded as the computational sweet spot in scientific computing: it achieves 4th-order accuracy with the minimum possible number of stages ($s = 4$)."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Picard Successive Approximations vs. Taylor Series Expansion",
                "statement": r"Consider the nonlinear initial value problem: $$\frac{dy}{dt} = t + y^2, \quad y(0) = 1$$ 1. Compute the first two Picard iterations $y^{(1)}(t)$ and $y^{(2)}(t)$ starting from $y^{(0)}(t) \equiv 1$. 2. Compute the 4th-degree Taylor polynomial of the exact solution $y(t)$ about $t_0 = 0$. 3. Verify how many terms of the Taylor series agree with $y^{(2)}(t)$.",
                "hints": [
                    "Recall Picard iteration: $y^{(k+1)}(t) = y_0 + \\int_{0}^t [s + (y^{(k)}(s))^2] ds$.",
                    "For Taylor series, differentiate $y' = t + y^2$ repeatedly using the chain rule and evaluate at $t=0$ where $y(0)=1$."
                ],
                "solution": r"""**Step 1: Picard Iterations**
Given $y_0 = 1$ and $f(t, y) = t + y^2$:
- Base approximation: $y^{(0)}(t) = 1$.
- First Picard iteration:
  $$y^{(1)}(t) = 1 + \int_0^t \left(s + [y^{(0)}(s)]^2\right) \, ds = 1 + \int_0^t (s + 1) \, ds = 1 + t + \frac{1}{2} t^2$$
- Second Picard iteration:
  $$y^{(2)}(t) = 1 + \int_0^t \left(s + [y^{(1)}(s)]^2\right) \, ds = 1 + \int_0^t \left[ s + \left(1 + s + \frac{1}{2} s^2\right)^2 \right] \, ds$$
  Expanding the integrand:
  $$\left(1 + s + \frac{s^2}{2}\right)^2 = 1 + 2s + 2s^2 + s^3 + \frac{s^4}{4}$$
  Adding $s$:
  $$s + \left(1 + s + \frac{s^2}{2}\right)^2 = 1 + 3s + 2s^2 + s^3 + \frac{s^4}{4}$$
  Integrating term-by-term:
  $$y^{(2)}(t) = 1 + \left[ s + \frac{3}{2} s^2 + \frac{2}{3} s^3 + \frac{1}{4} s^4 + \frac{1}{20} s^5 \right]_0^t = 1 + t + \frac{3}{2} t^2 + \frac{2}{3} t^3 + \frac{1}{4} t^4 + \frac{1}{20} t^5$$

**Step 2: Taylor Series Method**
Evaluate derivatives at $t = 0$ with $y(0) = 1$:
1. $y'(0) = 0 + (1)^2 = 1$.
2. $y''(t) = 1 + 2y y' \implies y''(0) = 1 + 2(1)(1) = 3$.
3. $y'''(t) = 2(y')^2 + 2y y'' \implies y'''(0) = 2(1)^2 + 2(1)(3) = 8$.
4. $y^{(4)}(t) = 6 y' y'' + 2y y''' \implies y^{(4)}(0) = 6(1)(3) + 2(1)(8) = 18 + 16 = 34$.

Forming the Taylor polynomial:
$$y(t) = 1 + y'(0) t + \frac{y''(0)}{2!} t^2 + \frac{y'''(0)}{3!} t^3 + \frac{y^{(4)}(0)}{4!} t^4 + \mathcal{O}(t^5)$$
$$y(t) = 1 + t + \frac{3}{2} t^2 + \frac{8}{6} t^3 + \frac{34}{24} t^4 + \mathcal{O}(t^5) = 1 + t + \frac{3}{2} t^2 + \frac{4}{3} t^3 + \frac{17}{12} t^4 + \mathcal{O}(t^5)$$

**Step 3: Comparison**
Comparing $y^{(2)}(t) = 1 + t + \frac{3}{2} t^2 + \frac{2}{3} t^3 + \dots$ with the exact Taylor expansion:
- Degree 0: $1 = 1$ (matches)
- Degree 1: $t = t$ (matches)
- Degree 2: $\frac{3}{2} t^2 = \frac{3}{2} t^2$ (matches)
- Degree 3: $\frac{2}{3} t^3 \ne \frac{4}{3} t^3$.
Thus, $y^{(2)}(t)$ correctly reproduces the exact Taylor polynomial up to degree 2."""
            },
            {
                "tier": "Advanced",
                "title": "Quantitative Comparison: Explicit Euler, Heun (RK2) and Classical RK4",
                "statement": r"Consider the test IVP: $$\frac{dy}{dt} = -2t y, \quad y(0) = 1$$ with exact analytical solution $y(t) = e^{-t^2}$. 1. Perform one single time step from $t_0 = 0$ to $t_1 = 0.2$ using step size $h = 0.2$ with: (a) Forward Euler, (b) Heun's method (RK2), and (c) Classical RK4. 2. Compute the exact solution $y(0.2)$ to 7 decimal places and calculate the absolute error $|y_{\text{exact}} - y_{\text{num}}|$ for all three methods.",
                "hints": [
                    "Evaluate $f(t, y) = -2t y$. Notice that at $t=0$, $k_1 = f(0, 1) = 0$ for all methods.",
                    "Use exact arithmetic for stages where possible before evaluating to decimals."
                ],
                "solution": r"""**Exact Solution:**
$$y(0.2) = e^{-(0.2)^2} = e^{-0.04} \approx 0.9607894$$

---

**(a) Forward Euler ($h = 0.2$):**
$$y_1 = y_0 + h f(t_0, y_0) = 1 + 0.2 \cdot (-2 \cdot 0 \cdot 1) = 1 + 0 = 1.0000000$$
- Absolute Error: $|0.9607894 - 1.0000000| = 0.0392106$ ($\approx 3.92 \times 10^{-2}$).

---

**(b) Heun's Method (RK2, $h = 0.2$):**
- Stage 1: $k_1 = f(0, 1) = 0$.
- Stage 2: $t_0 + h = 0.2$, $y_0 + h k_1 = 1 + 0.2(0) = 1$.
  $$k_2 = f(0.2, 1) = -2(0.2)(1) = -0.4$$
- Update:
  $$y_1 = y_0 + \frac{h}{2} (k_1 + k_2) = 1 + \frac{0.2}{2} (0 - 0.4) = 1 - 0.04 = 0.9600000$$
- Absolute Error: $|0.9607894 - 0.9600000| = 0.0007894$ ($\approx 7.89 \times 10^{-4}$).
  Notice error dropped by a factor of $\approx 50$ compared to Euler!

---

**(c) Classical RK4 ($h = 0.2$):**
- $k_1 = f(0, 1) = 0$.
- $k_2 = f\left(0 + \frac{0.2}{2}, 1 + \frac{0.2}{2} k_1\right) = f(0.1, 1) = -2(0.1)(1) = -0.2$.
- $k_3 = f\left(0.1, 1 + 0.1 k_2\right) = f(0.1, 1 + 0.1(-0.2)) = f(0.1, 0.98) = -2(0.1)(0.98) = -0.196$.
- $k_4 = f(0 + 0.2, 1 + 0.2 k_3) = f(0.2, 1 + 0.2(-0.196)) = f(0.2, 0.9608) = -2(0.2)(0.9608) = -0.38432$.
- Combine:
  $$\begin{aligned}
  y_1 &= 1 + \frac{0.2}{6} [0 + 2(-0.2) + 2(-0.196) + (-0.38432)] \\
  &= 1 + \frac{0.2}{6} [-0.4 - 0.392 - 0.38432] = 1 + \frac{0.2}{6} [-1.17632] \\
  &= 1 - 0.03921067 = 0.96078933
  \end{aligned}$$
- Absolute Error: $|0.96078944 - 0.96078933| = 0.00000011 = 1.1 \times 10^{-7}$.
  The classical RK4 method provides over 5 orders of magnitude higher accuracy than Euler for the same step size!"""
            },
            {
                "tier": "Rigorous Examination / Derivation",
                "title": "Complete Derivation of RK2 Order Conditions & Proof of Infeasibility for Order 3",
                "statement": r"1. Using bivariate Taylor expansions of the generic two-stage explicit Runge-Kutta scheme: $$y_{n+1} = y_n + h(b_1 k_1 + b_2 k_2), \quad k_1 = f(t_n, y_n), \quad k_2 = f(t_n + c_2 h, y_n + a_{21} h k_1)$$ derive the necessary and sufficient algebraic conditions on $(b_1, b_2, c_2, a_{21})$ for second-order accuracy $\mathcal{O}(h^2)$. 2. Prove mathematically that no two-stage explicit Runge-Kutta scheme can achieve third-order accuracy $\mathcal{O}(h^3)$.",
                "hints": [
                    "Expand $k_2$ in powers of $h$ up to $\\mathcal{O}(h^2)$ using partial derivatives $f_t, f_y, f_{tt}, f_{ty}, f_{yy}$.",
                    "For order 3, compare the required conditions with the available degrees of freedom."
                ],
                "solution": r"""**Part 1: Derivation of RK2 Order Conditions**

Let $y(t)$ be the true solution to $y' = f(t, y)$. By Taylor's theorem:
$$y(t_n + h) = y(t_n) + h y'(t_n) + \frac{h^2}{2} y''(t_n) + \frac{h^3}{6} y'''(t_n) + \mathcal{O}(h^4)$$
Computing the total derivatives using the chain rule (suppressing arguments $(t_n, y_n)$):
$$\begin{aligned}
y' &= f \\
y'' &= f_t + f f_y \\
y''' &= f_{tt} + 2 f f_{ty} + f^2 f_{yy} + f_y(f_t + f f_y)
\end{aligned}$$
Hence:
$$y(t_n + h) = y_n + h f + \frac{h^2}{2} (f_t + f f_y) + \frac{h^3}{6} \left[ f_{tt} + 2 f f_{ty} + f^2 f_{yy} + f_y(f_t + f f_y) \right] + \mathcal{O}(h^4) \quad \text{--- (Eq. 1)}$$

Now expand the numerical method. Here $k_1 = f$. For $k_2$:
$$\begin{aligned}
k_2 &= f(t_n + c_2 h, \, y_n + a_{21} h f) \\
&= f + h(c_2 f_t + a_{21} f f_y) + \frac{h^2}{2} \left( c_2^2 f_{tt} + 2 c_2 a_{21} f f_{ty} + a_{21}^2 f^2 f_{yy} \right) + \mathcal{O}(h^3)
\end{aligned}$$
Substituting into the numerical update $y_{n+1} = y_n + h b_1 k_1 + h b_2 k_2$:
$$y_{n+1} = y_n + h(b_1 + b_2) f + h^2 b_2 (c_2 f_t + a_{21} f f_y) + \frac{h^3}{2} b_2 \left( c_2^2 f_{tt} + 2 c_2 a_{21} f f_{ty} + a_{21}^2 f^2 f_{yy} \right) + \mathcal{O}(h^4) \quad \text{--- (Eq. 2)}$$

Subtracting Eq. (2) from Eq. (1) gives the local error:
$$\begin{aligned}
y(t_n + h) - y_{n+1} &= h [1 - (b_1 + b_2)] f \\
&\quad + h^2 \left[ \left(\frac{1}{2} - b_2 c_2\right) f_t + \left(\frac{1}{2} - b_2 a_{21}\right) f f_y \right] + \mathcal{O}(h^3)
\end{aligned}$$
For this error to be $\mathcal{O}(h^3)$ for all arbitrary smooth functions $f$, each bracketed term must vanish independently:
1. $b_1 + b_2 = 1$
2. $b_2 c_2 = \frac{1}{2}$
3. $b_2 a_{21} = \frac{1}{2}$

Dividing condition (3) by condition (2) immediately yields:
$$a_{21} = c_2$$
This proves the fundamental RK2 system of order conditions. $\blacksquare$

---

**Part 2: Proof of Infeasibility for Order 3 with 2 Stages**

For the scheme to be third-order accurate, the $\mathcal{O}(h^3)$ term of Eq. (2) must match the $\mathcal{O}(h^3)$ term of Eq. (1):
$$\frac{b_2}{2} \left( c_2^2 f_{tt} + 2 c_2^2 f f_{ty} + c_2^2 f^2 f_{yy} \right) \stackrel{?}{=} \frac{1}{6} \left( f_{tt} + 2 f f_{ty} + f^2 f_{yy} \right) + \frac{1}{6} f_y (f_t + f f_y)$$
Matching the coefficient of $f_{tt}$:
$$\frac{b_2 c_2^2}{2} = \frac{1}{6} \implies b_2 c_2^2 = \frac{1}{3}$$
Since $b_2 c_2 = \frac{1}{2}$, dividing gives:
$$c_2 = \frac{b_2 c_2^2}{b_2 c_2} = \frac{1/3}{1/2} = \frac{2}{3}$$
Then $b_2 = \frac{1}{2 c_2} = \frac{3}{4}$, and $b_1 = 1 - b_2 = \frac{1}{4}$.

However, examine the term $f_y (f_t + f f_y)$ in the exact Taylor expansion:
In Eq. (1), the coefficient of $f_y f_t$ is $\frac{1}{6}$.
In Eq. (2), the numerical expansion contains **no term proportional to $f_y f_t$ or $f f_y^2$ at order $h^3$**, because $k_2$ only involves partial derivatives of $f$, and does not evaluate derivatives of $k_1$!
Therefore, the coefficient of $f_y(f_t + f f_y)$ in the numerical method is identically **zero**, whereas in the exact solution it is $\frac{1}{6} \ne 0$.

Since $0 \ne \frac{1}{6}$, the difference cannot vanish for general non-linear ODEs where $f_y(f_t + f f_y) \ne 0$.
Hence, no 2-stage explicit Runge-Kutta method can achieve order 3. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    import json
    u = get_unit5()
    print("Unit 5 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
