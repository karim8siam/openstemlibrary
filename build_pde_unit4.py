# -*- coding: utf-8 -*-
"""
build_pde_unit4.py
Constructs Unit 4: The 1D & Multi-D Wave Equation: D'Alembert's Formula & Energy Methods
Strictly ZERO course numbers.
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "The 1D & Multi-D Wave Equation: D'Alembert's Formula & Energy Methods",
        "leadSummary": "Exhaustive treatment of hyperbolic wave propagation: physical derivation from tensioned strings and acoustics, D'Alembert's traveling wave formula for infinite strings, domain of dependence, range of influence and relativistic causality cones, semi-infinite strings and the method of images, Fourier separation of variables into standing normal modes, and rigorous proofs of energy conservation and solution uniqueness via energy integrals.",
        "simulations": ["sim_pde_wave_dalembert_modes"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "The 1D Infinite String Cauchy Problem: D'Alembert's Formula",
                "content": r"""### 1. Physical Derivation of the 1D Wave Equation

Consider a flexible, perfectly elastic string of constant linear mass density $\rho$ stretched under high uniform tension $T$ along the $x$-axis.
Let $u(x, t)$ denote the small transverse displacement at position $x$ and time $t$.
Assuming small slopes ($|\partial u/\partial x| \ll 1$), tension variations are negligible, and longitudinal displacements are negligible.

Consider an infinitesimal string element between $x$ and $x + \Delta x$.
The vertical component of tension at $x + \Delta x$ is $T \sin\theta_2 \approx T \tan\theta_2 = T u_x(x + \Delta x, t)$.
The vertical component of tension at $x$ is $-T \sin\theta_1 \approx -T u_x(x, t)$.
By Newton's second law ($F = m a$):
$$\Delta m \frac{\partial^2 u}{\partial t^2} = (\rho \Delta x) u_{tt} = T [u_x(x + \Delta x, t) - u_x(x, t)]$$
Dividing by $\rho \Delta x$ and taking the limit $\Delta x \to 0$:
$$\frac{\partial^2 u}{\partial t^2} = \frac{T}{\rho} \frac{\partial^2 u}{\partial x^2}$$
Setting the propagation wave speed $c = \sqrt{T/\rho}$ yields the **1D wave equation**:
$$u_{tt} - c^2 u_{xx} = 0$$

---

### 2. Complete Derivation of D'Alembert's Formula

Consider the Cauchy initial value problem on the infinite domain $x \in \mathbb{R}$:
$$\begin{cases}
u_{tt} - c^2 u_{xx} = 0, & x \in \mathbb{R}, \quad t > 0 \\
u(x, 0) = f(x), & x \in \mathbb{R} \quad (\text{initial displacement}) \\
u_t(x, 0) = g(x), & x \in \mathbb{R} \quad (\text{initial velocity})
\end{cases}$$

Factor the wave operator into two directional transport derivatives:
$$\left( \frac{\partial}{\partial t} - c \frac{\partial}{\partial x} \right) \left( \frac{\partial}{\partial t} + c \frac{\partial}{\partial x} \right) u = 0$$
Let $v(x, t) = u_t + c u_x$. Then $v$ satisfies the first-order homogeneous advection equation:
$$v_t - c v_x = 0$$
whose general solution is $v(x, t) = h(x + ct)$ for an arbitrary function $h$.
Now solve the inhomogeneous first-order PDE for $u$:
$$u_t + c u_x = h(x + ct)$$
Using the characteristic coordinates $\xi = x - ct$ and $\eta = x + ct$:
$$\frac{\partial^2 u}{\partial \xi \partial \eta} = 0$$
Integrating twice with respect to $\xi$ and $\eta$ yields the **general traveling wave solution**:
$$u(x, t) = \phi(x - ct) + \psi(x + ct)$$
where $\phi(x - ct)$ represents a right-moving wave at speed $c$, and $\psi(x + ct)$ represents a left-moving wave at speed $c$.

#### Determining $\phi$ and $\psi$ from Initial Data:
At $t = 0$:
1. $u(x, 0) = \phi(x) + \psi(x) = f(x)$
2. $u_t(x, 0) = -c \phi'(x) + c \psi'(x) = g(x)$

Dividing equation (2) by $c$ and integrating from an arbitrary base point $x_0$ to $x$:
$$-\phi(x) + \psi(x) = \frac{1}{c} \int_{x_0}^x g(s)\,ds + K$$
We now have a linear system for $\phi(x)$ and $\psi(x)$:
- Adding the two equations:
  $$2\psi(x) = f(x) + \frac{1}{c}\int_{x_0}^x g(s)\,ds + K \implies \psi(x) = \frac{1}{2}f(x) + \frac{1}{2c}\int_{x_0}^x g(s)\,ds + \frac{K}{2}$$
- Subtracting the two equations:
  $$2\phi(x) = f(x) - \frac{1}{c}\int_{x_0}^x g(s)\,ds - K \implies \phi(x) = \frac{1}{2}f(x) - \frac{1}{2c}\int_{x_0}^x g(s)\,ds - \frac{K}{2}$$

Substituting $\phi(x - ct)$ and $\psi(x + ct)$ into $u(x, t) = \phi(x - ct) + \psi(x + ct)$:
$$u(x, t) = \frac{1}{2}[f(x - ct) + f(x + ct)] + \frac{1}{2c}\left[ \int_{x_0}^{x+ct} g(s)\,ds - \int_{x_0}^{x-ct} g(s)\,ds \right]$$
Combining the integral limits:

> **Theorem 4.1 (D'Alembert's Formula):**
> The unique solution to the Cauchy problem for the 1D wave equation is:
> $$u(x, t) = \frac{1}{2}\left[ f(x - ct) + f(x + ct) \right] + \frac{1}{2c} \int_{x - ct}^{x + ct} g(s)\,ds$$"""
            },
            {
                "secNumber": "4.2",
                "title": "Domain of Dependence, Range of Influence & Strict Causality",
                "content": r"""### 1. Spacetime Geometry of Hyperbolic Waves

D'Alembert's formula reveals profound relativistic and geometric properties that distinguish hyperbolic PDEs from parabolic and elliptic equations.

> **Definition 4.1 (Domain of Dependence):**
> For any spacetime point $(x_0, t_0)$ with $t_0 > 0$, the value $u(x_0, t_0)$ depends exclusively on:
> 1. The values of initial displacement $f$ at the two endpoints: $x_0 - c t_0$ and $x_0 + c t_0$.
> 2. The values of initial velocity $g$ on the closed spatial interval:
>    $$D(x_0, t_0) = [x_0 - c t_0, x_0 + c t_0]$$
> The interval $D(x_0, t_0)$ is called the **domain of dependence** of the point $(x_0, t_0)$.
> In the $(x, t)$ spacetime plane, the triangular region with base $D(x_0, t_0)$ and apex $(x_0, t_0)$ bounded by the characteristic lines $x - ct = x_0 - ct_0$ and $x + ct = x_0 + ct_0$ is the **past light cone**.

---

### 2. Range of Influence

> **Definition 4.2 (Range of Influence):**
> Conversely, an initial disturbance originating at a point $x = \xi$ at $t = 0$ can only affect spacetime points $(x, t)$ satisfying:
> $$\xi - ct \le x \le \xi + ct \iff |x - \xi| \le ct$$
> The region $I(\xi) = \{ (x, t) \in \mathbb{R} \times [0, \infty) : |x - \xi| \le ct \}$ is the **future light cone** or **range of influence** of the point $\xi$.

---

### 3. Strict Causality vs Parabolic Infinite Speed

1. **Finite Speed of Propagation:** Disturbances propagate at the exact finite speed $c$. If initial data $f$ and $g$ are supported on a compact interval $[a, b]$, then at time $t$, $u(x, t) = 0$ everywhere outside $[a - ct, b + ct]$.
2. **Contrast with Diffusion:** In the heat equation $u_t = \alpha u_{xx}$, an initial point disturbance at $x = 0$ is instantly felt across the entire universe ($u(x, t) > 0$ for all $x \in \mathbb{R}$ for any $t > 0$, no matter how small). Hyperbolic physics strictly respects relativistic causality."""
            },
            {
                "secNumber": "4.3",
                "title": "Semi-Infinite & Finite Strings: The Method of Images",
                "content": r"""### 1. The Semi-Infinite String with Fixed End (Dirichlet Boundary)

Consider the semi-infinite string $x \ge 0, t \ge 0$ with a clamped boundary at $x = 0$:
$$\begin{cases}
u_{tt} - c^2 u_{xx} = 0, & x > 0, \quad t > 0 \\
u(x, 0) = f(x), \quad u_t(x, 0) = g(x), & x > 0 \\
u(0, t) = 0, & t \ge 0 \quad (\text{fixed end})
\end{cases}$$
where $f(0) = g(0) = 0$ for compatibility.

For points where $x \ge ct$, the backward characteristic $x - ct \ge 0$ does not touch the boundary $x = 0$, so D'Alembert's formula holds directly.
For points where $x < ct$, the characteristic $x - ct < 0$ reflects off the wall $x = 0$.

#### The Method of Odd Reflection:
To enforce $u(0, t) = 0$ automatically, extend the initial data to the entire real line $\mathbb{R}$ as **odd functions**:
$$f_{\text{odd}}(x) = \begin{cases} f(x), & x > 0 \\ 0, & x = 0 \\ -f(-x), & x < 0 \end{cases}, \qquad g_{\text{odd}}(x) = \begin{cases} g(x), & x > 0 \\ 0, & x = 0 \\ -g(-x), & x < 0 \end{cases}$$
Applying D'Alembert's formula with these odd extensions:
For $x < ct$, since $x - ct < 0$:
$$f_{\text{odd}}(x - ct) = -f(-(x - ct)) = -f(ct - x)$$
Thus, the solution for $0 < x < ct$ is:
$$u(x, t) = \frac{1}{2}[f(x + ct) - f(ct - x)] + \frac{1}{2c}\int_{ct - x}^{x + ct} g(s)\,ds$$

> **Physical Interpretation:**
> The term $-f(ct - x)$ represents an inverted wave packet reflected from the fixed boundary with a **phase shift of $\pi$** (inversion).

---

### 2. Free End (Neumann Boundary Condition)

If the end at $x = 0$ is free to slide frictionlessly on a vertical rod, the boundary condition is $u_x(0, t) = 0$.
By applying **even extensions** $f_{\text{even}}(-x) = f(x)$, the reflected wave maintains its sign:
$$u(x, t) = \frac{1}{2}[f(x + ct) + f(ct - x)] + \frac{1}{2c}\left[ \int_0^{ct - x} g(s)\,ds + \int_0^{x + ct} g(s)\,ds \right]$$
No inversion occurs upon reflection from a free boundary."""
            },
            {
                "secNumber": "4.4",
                "title": "Separation of Variables: Normal Modes & Standing Waves",
                "content": r"""### 1. Separation of Variables on a Finite Interval $[0, L]$

Consider the vibrating string of finite length $L$ with clamped endpoints:
$$\begin{cases}
u_{tt} = c^2 u_{xx}, & 0 < x < L, \quad t > 0 \\
u(0, t) = 0, \quad u(L, t) = 0, & t \ge 0 \\
u(x, 0) = f(x), \quad u_t(x, 0) = g(x), & 0 \le x \le L
\end{cases}$$

Assume a product solution of the form:
$$u(x, t) = X(x) T(t)$$
Substituting into the wave equation:
$$X(x) T''(t) = c^2 X''(x) T(t) \implies \frac{T''(t)}{c^2 T(t)} = \frac{X''(x)}{X(x)} = -\lambda$$
where $-\lambda$ is a separation constant.

#### Spatial Boundary Value Problem (Sturm-Liouville Eigenvalue Problem):
$$X''(x) + \lambda X(x) = 0, \qquad X(0) = 0, \quad X(L) = 0$$
- If $\lambda \le 0$, only trivial solutions $X \equiv 0$ exist.
- For $\lambda > 0$, set $\lambda = k^2$:
  $$X(x) = A \cos(kx) + B \sin(kx)$$
  $X(0) = 0 \implies A = 0$.
  $X(L) = B \sin(kL) = 0 \implies k_n L = n\pi \implies k_n = \frac{n\pi}{L}, \quad n = 1, 2, 3, \dots$
Thus, the **eigenvalues** and **eigenfunctions** are:
$$\lambda_n = \left(\frac{n\pi}{L}\right)^2, \qquad X_n(x) = \sin\left(\frac{n\pi x}{L}\right), \quad n \in \mathbb{N}$$

#### Temporal Equation:
$$T_n''(t) + c^2 k_n^2 T_n(t) = 0 \implies T_n''(t) + \omega_n^2 T_n(t) = 0$$
where the **natural circular frequencies** are:
$$\omega_n = c k_n = \frac{n\pi c}{L}$$
The general solution for $T_n(t)$ is:
$$T_n(t) = A_n \cos(\omega_n t) + B_n \sin(\omega_n t)$$

---

### 2. General Fourier Superposition

By the principle of linear superposition, the general solution is:
$$u(x, t) = \sum_{n=1}^\infty \left[ A_n \cos\left(\frac{n\pi c t}{L}\right) + B_n \sin\left(\frac{n\pi c t}{L}\right) \right] \sin\left(\frac{n\pi x}{L}\right)$$

The Fourier coefficients are determined from initial data by orthogonality:
$$A_n = \frac{2}{L} \int_0^L f(x) \sin\left(\frac{n\pi x}{L}\right)\,dx$$
$$B_n = \frac{2}{n\pi c} \int_0^L g(x) \sin\left(\frac{n\pi x}{L}\right)\,dx$$"""
            },
            {
                "secNumber": "4.5",
                "title": "Uniqueness and Stability: Conservation of Energy & Energy Integrals",
                "content": r"""### 1. Total Mechanical Energy of the Vibrating String

The kinetic energy of the string of linear mass density $\rho$ is:
$$E_K(t) = \frac{1}{2} \int_0^L \rho \left(\frac{\partial u}{\partial t}\right)^2\,dx$$
The potential (elastic strain) energy under tension $T$ is:
$$E_P(t) = \frac{1}{2} \int_0^L T \left(\frac{\partial u}{\partial x}\right)^2\,dx$$
Dividing by $\rho$ (recalling $c^2 = T/\rho$), the normalized **total energy** is defined as:
$$E(t) = \frac{1}{2} \int_0^L \left[ u_t^2 + c^2 u_x^2 \right]\,dx$$

---

### 2. Rigorous Proof of Conservation of Energy

> **Theorem 4.2 (Conservation of Energy):**
> Let $u(x, t)$ be a $C^2$ solution of the wave equation $u_{tt} = c^2 u_{xx}$ on $[0, L] \times [0, \infty)$ satisfying either Dirichlet boundaries ($u(0, t) = u(L, t) = 0$) or Neumann boundaries ($u_x(0, t) = u_x(L, t) = 0$).
> Then the total energy is strictly constant in time:
> $$\frac{dE}{dt} = 0 \implies E(t) = E(0) \quad \forall t \ge 0$$

*Proof:*
Differentiate $E(t)$ under the integral sign:
$$\frac{dE}{dt} = \frac{1}{2} \int_0^L \frac{\partial}{\partial t} \left[ u_t^2 + c^2 u_x^2 \right]\,dx = \int_0^L \left[ u_t u_{tt} + c^2 u_x u_{xt} \right]\,dx$$
Since $u$ is $C^2$, by Schwarz's theorem $u_{xt} = u_{tx}$.
Apply integration by parts to the second term:
$$\int_0^L c^2 u_x u_{tx}\,dx = \left[ c^2 u_x u_t \right]_0^L - \int_0^L c^2 u_{xx} u_t\,dx$$
Substitute this back into the derivative of energy:
$$\frac{dE}{dt} = \int_0^L u_t \left[ u_{tt} - c^2 u_{xx} \right]\,dx + \left[ c^2 u_x u_t \right]_0^L$$
1. In the interior, $u_{tt} - c^2 u_{xx} = 0$ by the wave equation.
2. At the boundaries $x = 0$ and $x = L$:
   - For Dirichlet conditions, $u(0, t) = u(L, t) = 0 \implies u_t(0, t) = u_t(L, t) = 0$.
   - For Neumann conditions, $u_x(0, t) = u_x(L, t) = 0$.
   In either case, the boundary term vanishes identically: $[c^2 u_x u_t]_0^L = 0$.
Therefore:
$$\frac{dE}{dt} = 0 \implies E(t) = E(0) \quad \forall t \ge 0$$ $\blacksquare$

---

### 3. Proof of Solution Uniqueness via the Energy Method

> **Theorem 4.3 (Uniqueness of Solutions to the Wave Equation):**
> The initial-boundary value problem for the 1D wave equation with Dirichlet boundary conditions has at most one $C^2$ solution.

*Proof:*
Suppose $u_1$ and $u_2$ are two $C^2$ solutions with identical initial conditions and boundary conditions.
Define the difference function $w(x, t) = u_1(x, t) - u_2(x, t)$.
By linearity:
- $w_{tt} - c^2 w_{xx} = 0$ on $(0, L) \times (0, \infty)$
- $w(x, 0) = f(x) - f(x) = 0$
- $w_t(x, 0) = g(x) - g(x) = 0$
- $w(0, t) = 0$ and $w(L, t) = 0$

Now evaluate the energy of the difference function at $t = 0$:
$$E_w(0) = \frac{1}{2}\int_0^L [w_t(x, 0)^2 + c^2 w_x(x, 0)^2]\,dx = \frac{1}{2}\int_0^L [0 + c^2(0)^2]\,dx = 0$$
By Theorem 4.2 (Conservation of Energy):
$$E_w(t) = E_w(0) = 0 \quad \forall t \ge 0$$
Since the integrand $w_t^2 + c^2 w_x^2 \ge 0$ is non-negative and continuous, $E_w(t) = 0$ forces:
$$w_t(x, t) \equiv 0 \quad \text{and} \quad w_x(x, t) \equiv 0 \quad \forall (x, t) \in [0, L] \times [0, \infty)$$
Since all first derivatives vanish identically on a connected domain, $w(x, t)$ is constant:
$$w(x, t) = C$$
Using the boundary condition $w(0, t) = 0$, we find $C = 0$.
Thus:
$$w(x, t) \equiv 0 \implies u_1(x, t) \equiv u_2(x, t)$$
The solution is strictly unique. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "D'Alembert Solution with Symmetric Triangular Displacement",
                "statement": r"""Solve the infinite wave equation:
$$u_{tt} = c^2 u_{xx}, \qquad x \in \mathbb{R}, \quad t > 0$$
with initial velocity $g(x) \equiv 0$ and initial displacement given by the symmetric triangular pluck:
$$f(x) = \begin{cases} h \left(1 - \frac{|x|}{a}\right), & |x| \le a \\ 0, & |x| > a \end{cases}$$
1. Write the explicit piecewise expression for $u(x, t)$ for $t > a/c$.
2. Sketch and describe the evolution of the two separating wave pulses.""",
                "solution": r"""### 1. Application of D'Alembert's Formula
Since the initial velocity is zero ($g(x) = 0$), D'Alembert's formula simplifies to:
$$u(x, t) = \frac{1}{2} [f(x - ct) + f(x + ct)]$$
This represents the superposition of two identical triangular pulses, each of half the original height $h/2$, propagating in opposite directions at constant velocity $\pm c$.

---

### 2. Piecewise Analysis for Large Times ($t > a/c$)
When $t > a/c$, the two pulses have completely separated because their centers are at $x = ct$ and $x = -ct$, and the distance between their centers is $2ct > 2a$ (which exceeds the sum of their half-widths $a + a = 2a$).

1. **Right-Traveling Pulse:** Supported on $[ct - a, ct + a]$:
   $$f(x - ct) = h \left( 1 - \frac{|x - ct|}{a} \right) \quad \text{for } |x - ct| \le a$$
   Contribution: $\frac{h}{2} \left( 1 - \frac{|x - ct|}{a} \right)$.

2. **Left-Traveling Pulse:** Supported on $[-ct - a, -ct + a]$:
   $$f(x + ct) = h \left( 1 - \frac{|x + ct|}{a} \right) \quad \text{for } |x + ct| \le a$$
   Contribution: $\frac{h}{2} \left( 1 - \frac{|x + ct|}{a} \right)$.

3. **Intermediate Region:** For $-ct + a < x < ct - a$, both pulses vanish, so:
   $$u(x, t) = 0$$

Therefore, for $t > a/c$, the complete solution is:
$$u(x, t) = \begin{cases}
\frac{h}{2}\left(1 - \frac{|x + ct|}{a}\right), & -ct - a \le x \le -ct + a \\
0, & -ct + a < x < ct - a \\
\frac{h}{2}\left(1 - \frac{|x - ct|}{a}\right), & ct - a \le x \le ct + a \\
0, & |x| > ct + a
\end{cases}$$

---

### 3. Physical Behavior
At $t = 0$, the single triangular tent of peak height $h$ is at rest.
As $t$ advances from $0$ to $a/(2c)$, the peak flattens into a plateau of height $h/2$ as the right and left components slide past each other.
At $t = a/c$, the two triangles touch at the origin with zero height.
For $t > a/c$, two separate triangular pulses of height $h/2$ and base $2a$ travel indefinitely to $\pm\infty$ without attenuation or dispersion. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Semi-Infinite String with Fixed End and Incoming Gaussian Pulse",
                "statement": r"""Consider the semi-infinite string $x > 0$ with fixed clamped end $u(0, t) = 0$.
The string is initially at rest with initial velocity $g(x) \equiv 0$ and an initial Gaussian displacement centered at $x_0 > 0$:
$$f(x) = A \exp\left( -\frac{(x - x_0)^2}{2\sigma^2} \right)$$
where $\sigma \ll x_0$.
Using the method of odd reflection:
1. Find the exact solution $u(x, t)$ for all $x > 0, t > 0$.
2. Analyze the reflected wave packet and prove that reflection produces an exact phase inversion.""",
                "solution": r"""### 1. Odd Reflection Extension
To satisfy the Dirichlet boundary condition $u(0, t) = 0$ for all $t \ge 0$, we extend $f(x)$ to the entire real line as an odd function $f_{\text{odd}}(x)$:
$$f_{\text{odd}}(x) = \begin{cases} f(x) = A e^{-(x - x_0)^2 / (2\sigma^2)}, & x > 0 \\ 0, & x = 0 \\ -f(-x) = -A e^{-(-x - x_0)^2 / (2\sigma^2)} = -A e^{-(x + x_0)^2 / (2\sigma^2)}, & x < 0 \end{cases}$$
Notice that the fictitious image source is located at $-x_0$ with negative amplitude $-A$.

---

### 2. D'Alembert Representation
Since $g \equiv 0$, the solution on $x > 0$ is:
$$u(x, t) = \frac{1}{2} [ f_{\text{odd}}(x - ct) + f_{\text{odd}}(x + ct) ]$$
Since $x > 0$ and $t > 0$, $x + ct > 0$ always; hence:
$$f_{\text{odd}}(x + ct) = f(x + ct) = A e^{-(x + ct - x_0)^2 / (2\sigma^2)}$$
For the term $x - ct$:
- If $x \ge ct$ (before reflection reaches point $x$):
  $$x - ct \ge 0 \implies f_{\text{odd}}(x - ct) = f(x - ct) = A e^{-(x - ct - x_0)^2 / (2\sigma^2)}$$
  So for $x \ge ct$:
  $$u(x, t) = \frac{A}{2} \left[ e^{-(x - ct - x_0)^2 / (2\sigma^2)} + e^{-(x + ct - x_0)^2 / (2\sigma^2)} \right]$$

- If $x < ct$ (after reflection has occurred):
  $$x - ct < 0 \implies f_{\text{odd}}(x - ct) = -f(-(x - ct)) = -f(ct - x) = -A e^{-(ct - x - x_0)^2 / (2\sigma^2)} = -A e^{-(x - ct + x_0)^2 / (2\sigma^2)}$$
  So for $x < ct$:
  $$u(x, t) = \frac{A}{2} \left[ e^{-(x + ct - x_0)^2 / (2\sigma^2)} - e^{-(x - ct + x_0)^2 / (2\sigma^2)} \right]$$

---

### 3. Analysis of Phase Inversion
At $t = x_0/c$, the incoming left-traveling pulse $\frac{A}{2}e^{-(x + ct - x_0)^2 / (2\sigma^2)}$ strikes the boundary $x = 0$.
For $t > x_0/c$, the reflected pulse travels toward the right in the region $x > 0$, described by:
$$u_{\text{refl}}(x, t) = -\frac{A}{2} \exp\left( -\frac{(x - c(t - x_0/c))^2}{2\sigma^2} \right)$$
1. **Negative Amplitude:** The amplitude is $-\frac{A}{2}$, which is an exact vertical flip (phase shift of $\pi$).
2. **Boundary Verification:** At $x = 0$:
   $$u(0, t) = \frac{A}{2} \left[ e^{-(ct - x_0)^2 / (2\sigma^2)} - e^{-( -ct + x_0)^2 / (2\sigma^2)} \right]$$
   Since $(ct - x_0)^2 = (-ct + x_0)^2$, the two terms cancel identically:
   $$u(0, t) \equiv 0 \quad \forall t \ge 0$$
The boundary condition is strictly preserved. $\blacksquare$"""
            },
            {
                "tier": "Honors Challenge",
                "title": "Conservation of Energy and Dirichlet Wave Uniqueness",
                "statement": r"""Consider the inhomogeneous 1D wave equation:
$$u_{tt} - c^2 u_{xx} = F(x, t), \qquad 0 < x < L, \quad t > 0$$
subject to time-dependent boundary conditions $u(0, t) = h_1(t), u(L, t) = h_2(t)$, and initial conditions $u(x, 0) = f(x), u_t(x, 0) = g(x)$.
1. Formulate the total mechanical energy integral for the homogeneous problem.
2. Prove that the initial-boundary value problem has at most one classical $C^2$ solution.
3. Show that the solution depends continuously on the initial data in the energy norm.""",
                "solution": r"""### 1. Difference Function and Homogeneous System
Suppose $u(x, t)$ and $v(x, t)$ are two $C^2$ solutions satisfying the same inhomogeneous PDE, boundary conditions, and initial data.
Define $w(x, t) = u(x, t) - v(x, t)$.
Then $w(x, t)$ satisfies:
$$\begin{cases}
w_{tt} - c^2 w_{xx} = F(x, t) - F(x, t) = 0, & 0 < x < L, \quad t > 0 \\
w(0, t) = h_1(t) - h_1(t) = 0, & t \ge 0 \\
w(L, t) = h_2(t) - h_2(t) = 0, & t \ge 0 \\
w(x, 0) = f(x) - f(x) = 0, & 0 \le x \le L \\
w_t(x, 0) = g(x) - g(x) = 0, & 0 \le x \le L
\end{cases}$$

---

### 2. Proof of Energy Conservation for $w$
Define the energy of the error function $w$:
$$E[w](t) = \frac{1}{2} \int_0^L \left[ (w_t(x, t))^2 + c^2 (w_x(x, t))^2 \right]\,dx$$
Taking the time derivative:
$$\frac{dE}{dt} = \int_0^L \left[ w_t w_{tt} + c^2 w_x w_{xt} \right]\,dx$$
Integrate the second term by parts with respect to $x$:
$$\int_0^L c^2 w_x w_{xt}\,dx = \left[ c^2 w_x w_t \right]_0^L - \int_0^L c^2 w_{xx} w_t\,dx$$
Combine the terms:
$$\frac{dE}{dt} = \int_0^L w_t (w_{tt} - c^2 w_{xx})\,dx + c^2 w_x(L, t) w_t(L, t) - c^2 w_x(0, t) w_t(0, t)$$
- $w_{tt} - c^2 w_{xx} = 0$ in $(0, L)$.
- Since $w(0, t) = 0$ for all $t$, differentiating with respect to $t$ gives $w_t(0, t) = 0$.
- Since $w(L, t) = 0$ for all $t$, differentiating with respect to $t$ gives $w_t(L, t) = 0$.
Therefore, both boundary terms vanish:
$$\frac{dE}{dt} = 0 \implies E[w](t) = E[w](0) \quad \forall t \ge 0$$

---

### 3. Evaluation of Initial Energy and Uniqueness
At $t = 0$:
$$w_t(x, 0) = 0, \qquad w_x(x, 0) = \frac{d}{dx}[w(x, 0)] = \frac{d}{dx}[0] = 0$$
Hence:
$$E[w](0) = \frac{1}{2}\int_0^L [0^2 + c^2(0)^2]\,dx = 0$$
Consequently:
$$E[w](t) = 0 \quad \forall t \ge 0$$
Because the integrand $w_t^2 + c^2 w_x^2$ is continuous and non-negative:
$$w_t(x, t) = 0 \quad \text{and} \quad w_x(x, t) = 0 \quad \forall (x, t) \in [0, L] \times [0, \infty)$$
This implies $w(x, t) = C$ (constant).
Since $w(0, t) = 0$, $C = 0$.
Therefore:
$$w(x, t) \equiv 0 \implies u(x, t) \equiv v(x, t)$$
The solution is strictly unique.

---

### 4. Continuous Dependence on Initial Data
Let $u$ and $\tilde{u}$ be solutions with initial data $(f, g)$ and $(\tilde{f}, \tilde{g})$.
By linearity, their difference $\delta u = u - \tilde{u}$ satisfies:
$$E[\delta u](t) = E[\delta u](0) = \frac{1}{2}\int_0^L \left[ (g - \tilde{g})^2 + c^2 (f' - \tilde{f}')^2 \right]\,dx$$
If $\|g - \tilde{g}\|_{L^2} < \epsilon$ and $\|f' - \tilde{f}'\|_{L^2} < \epsilon$, then:
$$E[\delta u](t) \le \frac{1}{2}(1 + c^2)\epsilon^2$$
By Poincaré's inequality, since $\delta u(0, t) = 0$:
$$\max_{x \in [0, L]} |\delta u(x, t)|^2 \le L \int_0^L |\delta u_x|^2\,dx \le \frac{2L}{c^2} E[\delta u](t) \le \frac{L(1+c^2)}{c^2}\epsilon^2$$
Thus, small variations in initial data result in uniformly small variations in the solution for all future times, establishing Hadamard **well-posedness**. $\blacksquare$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u4 = get_unit4()
    print(f"Loaded Unit 4: {u4['title']} with {len(u4['sections'])} sections and {len(u4['problems'])} problems.")
