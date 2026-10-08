# -*- coding: utf-8 -*-
"""
build_pde_unit8.py
Constructs Unit 8: Integral Transform Methods & Green's Functions for Inhomogeneous PDEs
Strictly ZERO course numbers.
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Integral Transform Methods & Green's Functions for Inhomogeneous PDEs",
        "leadSummary": "Advanced continuous transform calculus and distributional Green's function methods for partial differential equations: Fourier sine, cosine, and bilateral exponential transforms for infinite and semi-infinite domains, Laplace transform operational methods for initial-boundary value problems, Green's identities, distributional Dirac delta sources and fundamental solutions, and the method of images for constructing exact Green's functions in half-spaces, wedges, and spheres.",
        "simulations": ["sim_pde_greens_function_images"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Fourier Sine and Cosine Transforms for Semi-Infinite Domains",
                "content": r"""### 1. Definitions of the Fourier Sine and Cosine Transforms

For functions defined on the semi-infinite line $x \in [0, \infty)$, boundary conditions at $x = 0$ determine whether the Fourier sine or cosine transform is the appropriate integral operator:

> **Definition 8.1 (Fourier Sine Transform):**
> $$\mathcal{F}_s[f](k) = \tilde{f}_s(k) = \sqrt{\frac{2}{\pi}} \int_0^\infty f(x) \sin(kx)\,dx$$
> with inverse transform:
> $$\mathcal{F}_s^{-1}[\tilde{f}_s](x) = f(x) = \sqrt{\frac{2}{\pi}} \int_0^\infty \tilde{f}_s(k) \sin(kx)\,dk$$

> **Definition 8.2 (Fourier Cosine Transform):**
> $$\mathcal{F}_c[f](k) = \tilde{f}_c(k) = \sqrt{\frac{2}{\pi}} \int_0^\infty f(x) \cos(kx)\,dx$$
> with inverse transform:
> $$\mathcal{F}_c^{-1}[\tilde{f}_c](x) = f(x) = \sqrt{\frac{2}{\pi}} \int_0^\infty \tilde{f}_c(k) \cos(kx)\,dk$$

---

### 2. Operational Properties for Second Derivatives

Integrating by parts twice under the decay assumption $f(x), f'(x) \to 0$ as $x \to \infty$:

1. **Transform of $f''(x)$ under Fourier Sine Transform:**
   $$\mathcal{F}_s[f''](k) = \sqrt{\frac{2}{\pi}}\int_0^\infty f''(x)\sin(kx)\,dx = \left[ \sqrt{\frac{2}{\pi}} f'(x)\sin(kx) \right]_0^\infty - k \sqrt{\frac{2}{\pi}}\int_0^\infty f'(x)\cos(kx)\,dx$$
   $$= 0 - k \left( \left[ \sqrt{\frac{2}{\pi}} f(x)\cos(kx) \right]_0^\infty + k \sqrt{\frac{2}{\pi}}\int_0^\infty f(x)\sin(kx)\,dx \right)$$
   $$\mathcal{F}_s[f''](k) = -k^2 \tilde{f}_s(k) + \sqrt{\frac{2}{\pi}} k f(0)$$
   **Rule:** Automatically absorbs Dirichlet boundary data $f(0)$!

2. **Transform of $f''(x)$ under Fourier Cosine Transform:**
   $$\mathcal{F}_c[f''](k) = -k^2 \tilde{f}_c(k) - \sqrt{\frac{2}{\pi}} f'(0)$$
   **Rule:** Automatically absorbs Neumann boundary data $f'(0)$!"""
            },
            {
                "secNumber": "8.2",
                "title": "Bilateral Fourier Transform Applied to Infinite Wave & Diffusion",
                "content": r"""### 1. Bilateral Fourier Transform on $L^2(\mathbb{R})$

For problems on the entire real line $x \in (-\infty, \infty)$:
$$\hat{u}(k, t) = \mathcal{F}[u](k, t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty u(x, t) e^{-ikx}\,dx$$
with inversion formula:
$$u(x, t) = \mathcal{F}^{-1}[\hat{u}](x, t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty \hat{u}(k, t) e^{ikx}\,dk$$
The spatial derivative operational property is:
$$\mathcal{F}\left[\frac{\partial^n u}{\partial x^n}\right](k, t) = (ik)^n \hat{u}(k, t)$$

---

### 2. Solution of the Infinite 1D Diffusion Equation

Applying the Fourier transform to $u_t = \alpha u_{xx}$ with $u(x, 0) = f(x)$:
$$\frac{\partial \hat{u}}{\partial t}(k, t) = \alpha (ik)^2 \hat{u}(k, t) = -\alpha k^2 \hat{u}(k, t)$$
This is a decoupled ODE in $t$ for each wavenumber $k$:
$$\hat{u}(k, t) = \hat{f}(k) e^{-\alpha k^2 t}$$
By the **Convolution Theorem** for Fourier transforms:
$$\mathcal{F}^{-1}[\hat{f}(k) \hat{g}(k)] = \frac{1}{\sqrt{2\pi}} (f * g)(x)$$
Here $\hat{g}(k) = e^{-\alpha k^2 t}$. Its inverse Fourier transform is the Gaussian:
$$g(x) = \mathcal{F}^{-1}[e^{-\alpha k^2 t}] = \frac{1}{\sqrt{2\alpha t}} e^{-x^2 / (4\alpha t)}$$
Therefore:
$$u(x, t) = \frac{1}{\sqrt{2\pi}} \left( f * \frac{1}{\sqrt{2\alpha t}} e^{-x^2 / (4\alpha t)} \right) = \frac{1}{\sqrt{4\pi \alpha t}} \int_{-\infty}^\infty f(y) e^{-(x - y)^2 / (4\alpha t)}\,dy$$
This independently re-derives the Gaussian heat kernel without guessing similarity variables!"""
            },
            {
                "secNumber": "8.3",
                "title": "Laplace Transform for Initial-Boundary Value Problems",
                "content": r"""### 1. The Laplace Transform with Respect to Time

When the PDE evolves forward in time $t \ge 0$ with initial conditions at $t = 0$, the Laplace transform with respect to $t$ converts time derivatives into algebraic polynomials in the complex frequency variable $s$:
$$\bar{u}(x, s) = \mathcal{L}[u](x, s) = \int_0^\infty u(x, t) e^{-st}\,dt, \qquad \operatorname{Re}(s) > s_0$$
The operational properties for time derivatives are:
$$\mathcal{L}[u_t](x, s) = s \bar{u}(x, s) - u(x, 0)$$
$$\mathcal{L}[u_{tt}](x, s) = s^2 \bar{u}(x, s) - s u(x, 0) - u_t(x, 0)$$

---

### 2. Reduction to Spatial Ordinary Differential Equations

Applying the Laplace transform to a linear PDE in $(x, t)$ transforms the PDE into a boundary value problem for an **ordinary differential equation** in $x$, parameterized by $s$.

> **Example 8.1 (Semi-Infinite Heat Conduction):**
> $$u_t = \alpha u_{xx}, \quad x > 0, \quad t > 0, \qquad u(x, 0) = 0, \quad u(0, t) = T_0$$
> Taking the Laplace transform:
> $$s \bar{u}(x, s) - 0 = \alpha \frac{d^2 \bar{u}}{dx^2} \implies \frac{d^2 \bar{u}}{dx^2} - \frac{s}{\alpha} \bar{u} = 0$$
> The general solution bounded as $x \to \infty$ is:
> $$\bar{u}(x, s) = C_1(s) e^{-\sqrt{s/\alpha}\,x}$$
> Boundary condition at $x = 0$: $\bar{u}(0, s) = \mathcal{L}[T_0] = \frac{T_0}{s}$.
> Thus:
> $$\bar{u}(x, s) = \frac{T_0}{s} e^{-\sqrt{s/\alpha}\,x}$$
> Using the standard Laplace inversion identity $\mathcal{L}^{-1}\left[ \frac{1}{s} e^{-a\sqrt{s}} \right] = \operatorname{erfc}\left( \frac{a}{2\sqrt{t}} \right)$:
> $$u(x, t) = T_0 \operatorname{erfc}\left( \frac{x}{2\sqrt{\alpha t}} \right) = T_0 \left[ 1 - \frac{2}{\sqrt{\pi}} \int_0^{x/(2\sqrt{\alpha t})} e^{-z^2}\,dz \right]$$"""
            },
            {
                "secNumber": "8.4",
                "title": "Green's Identities & Fundamental Solutions for Poisson's Equation",
                "content": r"""### 1. Green's Classical Identities

Let $\Omega \subset \mathbb{R}^n$ be a bounded domain with $C^1$ boundary $\partial \Omega$.
Let $u, v \in C^2(\bar{\Omega})$.

> **Theorem 8.1 (Green's First Identity):**
> $$\int_\Omega \left( v \nabla^2 u + \nabla u \cdot \nabla v \right) d\mathbf{x} = \int_{\partial \Omega} v \frac{\partial u}{\partial \mathbf{n}}\,dS$$

> **Theorem 8.2 (Green's Second Identity):**
> Interchanging $u$ and $v$ and subtracting yields:
> $$\int_\Omega \left( v \nabla^2 u - u \nabla^2 v \right) d\mathbf{x} = \int_{\partial \Omega} \left( v \frac{\partial u}{\partial \mathbf{n}} - u \frac{\partial v}{\partial \mathbf{n}} \right) dS$$

---

### 2. The Fundamental Solution of the Laplacian

> **Definition 8.3 (Fundamental Solution / Free-Space Green's Function):**
> The fundamental solution $\Phi(\mathbf{x}, \mathbf{y}) = \Phi(\mathbf{x} - \mathbf{y})$ satisfies the distributional Poisson equation:
> $$\nabla_\mathbf{x}^2 \Phi(\mathbf{x}, \mathbf{y}) = -\delta(\mathbf{x} - \mathbf{y})$$
> In two dimensions ($n = 2$):
> $$\Phi(\mathbf{x}, \mathbf{y}) = -\frac{1}{2\pi} \ln\|\mathbf{x} - \mathbf{y}\|$$
> In three dimensions ($n = 3$):
> $$\Phi(\mathbf{x}, \mathbf{y}) = \frac{1}{4\pi \|\mathbf{x} - \mathbf{y}\|}$$

---

### 3. Representation Formula for Poisson's Equation

Applying Green's Second Identity with $v(\mathbf{x}) = \Phi(\mathbf{x}, \mathbf{y})$ on $\Omega \setminus B_\epsilon(\mathbf{y})$ and taking $\epsilon \to 0^+$:

> **Theorem 8.3 (Green's Representation Formula):**
> For any $u \in C^2(\bar{\Omega})$:
> $$u(\mathbf{y}) = - \int_\Omega \Phi(\mathbf{x}, \mathbf{y}) \nabla^2 u(\mathbf{x})\,d\mathbf{x} + \int_{\partial \Omega} \left[ \Phi(\mathbf{x}, \mathbf{y}) \frac{\partial u}{\partial \mathbf{n}}(\mathbf{x}) - u(\mathbf{x}) \frac{\partial \Phi}{\partial \mathbf{n}_\mathbf{x}}(\mathbf{x}, \mathbf{y}) \right] dS_x$$"""
            },
            {
                "secNumber": "8.5",
                "title": "Construction of Green's Functions via the Method of Images",
                "content": r"""### 1. Definition of the Dirichlet Green's Function

The representation formula in Theorem 8.3 requires knowledge of both $u$ and its normal derivative $\frac{\partial u}{\partial \mathbf{n}}$ on $\partial\Omega$. In a Dirichlet problem, only $u$ is prescribed.
To eliminate $\frac{\partial u}{\partial \mathbf{n}}$ from the formula, we define the **Dirichlet Green's function**:
$$G(\mathbf{x}, \mathbf{y}) = \Phi(\mathbf{x}, \mathbf{y}) + h^\mathbf{y}(\mathbf{x})$$
where the **corrector potential** $h^\mathbf{y}(\mathbf{x})$ satisfies:
$$\begin{cases} \nabla_\mathbf{x}^2 h^\mathbf{y}(\mathbf{x}) = 0 & \text{in } \Omega \\ h^\mathbf{y}(\mathbf{x}) = -\Phi(\mathbf{x}, \mathbf{y}) & \text{on } \partial\Omega \end{cases}$$
By construction, $G(\mathbf{x}, \mathbf{y}) \equiv 0$ for all $\mathbf{x} \in \partial\Omega$.
Substituting $G$ into Green's Second Identity yields the complete **solution formula**:
$$u(\mathbf{y}) = - \int_\Omega G(\mathbf{x}, \mathbf{y}) f(\mathbf{x})\,d\mathbf{x} - \int_{\partial\Omega} g(\mathbf{x}) \frac{\partial G}{\partial \mathbf{n}_\mathbf{x}}(\mathbf{x}, \mathbf{y})\,dS_x$$
where $\nabla^2 u = f$ in $\Omega$ and $u = g$ on $\partial\Omega$.

---

### 2. Method of Images for the Upper Half-Space $\mathbb{R}^n_+$

Let $\mathbb{R}^n_+ = \{ \mathbf{x} = (x_1, \dots, x_n) \in \mathbb{R}^n : x_n > 0 \}$.
For a source point $\mathbf{y} = (y_1, \dots, y_{n-1}, y_n)$, the mirror image point reflected across the boundary plane $x_n = 0$ is:
$$\mathbf{y}^* = (y_1, \dots, y_{n-1}, -y_n)$$
Define:
$$G(\mathbf{x}, \mathbf{y}) = \Phi(\mathbf{x} - \mathbf{y}) - \Phi(\mathbf{x} - \mathbf{y}^*)$$
On the boundary $x_n = 0$:
$$\|\mathbf{x} - \mathbf{y}\|^2 = \sum_{i=1}^{n-1} (x_i - y_i)^2 + (0 - y_n)^2 = \sum_{i=1}^{n-1} (x_i - y_i)^2 + (0 - (-y_n))^2 = \|\mathbf{x} - \mathbf{y}^*\|^2$$
Thus $\Phi(\mathbf{x} - \mathbf{y}) = \Phi(\mathbf{x} - \mathbf{y}^*)$ on $x_n = 0$, so $G(\mathbf{x}, \mathbf{y}) \equiv 0$ on $\partial \mathbb{R}^n_+$!

In $\mathbb{R}^3_+$:
$$G(\mathbf{x}, \mathbf{y}) = \frac{1}{4\pi} \left[ \frac{1}{\sqrt{\sum_{i=1}^2 (x_i - y_i)^2 + (x_3 - y_3)^2}} - \frac{1}{\sqrt{\sum_{i=1}^2 (x_i - y_i)^2 + (x_3 + y_3)^2}} \right]$$
The outward normal on the boundary $x_3 = 0$ is $\mathbf{n} = -\hat{\mathbf{e}}_3$.
$$\frac{\partial G}{\partial \mathbf{n}_\mathbf{x}} = -\left.\frac{\partial G}{\partial x_3}\right|_{x_3=0} = -\frac{y_3}{2\pi \left( \sum_{i=1}^2 (x_i - y_i)^2 + y_3^2 \right)^{3/2}}$$
This yields the **Poisson Integral Formula for the Half-Space**:
$$u(\mathbf{y}) = \frac{y_3}{2\pi} \int_{\mathbb{R}^2} \frac{g(x_1, x_2)}{\left( (x_1 - y_1)^2 + (x_2 - y_2)^2 + y_3^2 \right)^{3/2}}\,dx_1 dx_2$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Fourier Sine Transform Solution of Semi-Infinite Heat Conduction",
                "statement": r"""Solve the semi-infinite heat conduction problem:
$$\begin{cases}
u_t = \alpha u_{xx}, & x > 0, \quad t > 0 \\
u(0, t) = T_0, & t > 0 \quad (\text{constant surface temperature}) \\
u(x, 0) = 0, & x > 0 \\
u(x, t) \to 0, & x \to \infty
\end{cases}$$
using the Fourier sine transform, and express the result in terms of the complementary error function $\operatorname{erfc}(z)$.""",
                "solution": r"""### 1. Application of the Fourier Sine Transform
Let $\tilde{u}(k, t) = \mathcal{F}_s[u](k, t) = \sqrt{\frac{2}{\pi}}\int_0^\infty u(x, t) \sin(kx)\,dx$.
Taking the Fourier sine transform of $u_t = \alpha u_{xx}$:
$$\frac{\partial \tilde{u}}{\partial t} = \alpha \mathcal{F}_s[u_{xx}] = \alpha \left[ -k^2 \tilde{u}(k, t) + \sqrt{\frac{2}{\pi}} k u(0, t) \right]$$
Substitute the boundary condition $u(0, t) = T_0$:
$$\frac{\partial \tilde{u}}{\partial t} + \alpha k^2 \tilde{u} = \alpha k T_0 \sqrt{\frac{2}{\pi}}$$

---

### 2. Solving the First-Order Linear ODE in $t$
This is an inhomogeneous ODE for $\tilde{u}$ with integrating factor $e^{\alpha k^2 t}$:
$$\frac{\partial}{\partial t}\left( \tilde{u} e^{\alpha k^2 t} \right) = \sqrt{\frac{2}{\pi}} \alpha k T_0 e^{\alpha k^2 t}$$
Integrating with respect to $t$:
$$\tilde{u}(k, t) e^{\alpha k^2 t} = \sqrt{\frac{2}{\pi}} \frac{\alpha k T_0}{\alpha k^2} e^{\alpha k^2 t} + C(k) = \sqrt{\frac{2}{\pi}} \frac{T_0}{k} e^{\alpha k^2 t} + C(k)$$
Dividing by $e^{\alpha k^2 t}$:
$$\tilde{u}(k, t) = \sqrt{\frac{2}{\pi}} \frac{T_0}{k} + C(k) e^{-\alpha k^2 t}$$
Using the initial condition $u(x, 0) = 0 \implies \tilde{u}(k, 0) = 0$:
$$0 = \sqrt{\frac{2}{\pi}} \frac{T_0}{k} + C(k) \implies C(k) = -\sqrt{\frac{2}{\pi}} \frac{T_0}{k}$$
Thus:
$$\tilde{u}(k, t) = \sqrt{\frac{2}{\pi}} \frac{T_0}{k} \left( 1 - e^{-\alpha k^2 t} \right)$$

---

### 3. Inverse Fourier Sine Transform
Using the inversion formula:
$$u(x, t) = \sqrt{\frac{2}{\pi}}\int_0^\infty \tilde{u}(k, t) \sin(kx)\,dk = \frac{2 T_0}{\pi} \int_0^\infty \frac{1 - e^{-\alpha k^2 t}}{k} \sin(kx)\,dk$$
Split into two integrals:
$$u(x, t) = \frac{2 T_0}{\pi} \int_0^\infty \frac{\sin(kx)}{k}\,dk - \frac{2 T_0}{\pi} \int_0^\infty \frac{e^{-\alpha k^2 t} \sin(kx)}{k}\,dk$$
Recall the Dirichlet integral $\int_0^\infty \frac{\sin(kx)}{k}\,dk = \frac{\pi}{2}$ for $x > 0$.
So the first term is $\frac{2 T_0}{\pi} \frac{\pi}{2} = T_0$.
The second integral is the classic Laplace integral:
$$\int_0^\infty \frac{e^{-\alpha k^2 t} \sin(kx)}{k}\,dk = \frac{\pi}{2} \operatorname{erf}\left( \frac{x}{2\sqrt{\alpha t}} \right)$$
Therefore:
$$u(x, t) = T_0 - T_0 \operatorname{erf}\left( \frac{x}{2\sqrt{\alpha t}} \right) = T_0 \left[ 1 - \operatorname{erf}\left( \frac{x}{2\sqrt{\alpha t}} \right) \right] = T_0 \operatorname{erfc}\left( \frac{x}{2\sqrt{\alpha t}} \right)$$
where $\operatorname{erfc}(z) = \frac{2}{\sqrt{\pi}}\int_z^\infty e^{-s^2}\,ds$ is the complementary error function. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Laplace Transform Solution of Semi-Infinite Wave Equation",
                "statement": r"""Solve the 1D wave equation on the semi-infinite line $x > 0$:
$$u_{tt} = c^2 u_{xx}, \qquad x > 0, \quad t > 0$$
subject to rest initial conditions $u(x, 0) = 0, u_t(x, 0) = 0$, bounded solution as $x \to \infty$, and prescribed boundary displacement:
$$u(0, t) = f(t), \qquad t \ge 0$$
using the Laplace transform.""",
                "solution": r"""### 1. Laplace Transform in Time
Let $\bar{u}(x, s) = \mathcal{L}[u(x, t)] = \int_0^\infty u(x, t) e^{-st}\,dt$.
Taking the Laplace transform of the wave equation:
$$\mathcal{L}[u_{tt}] = s^2 \bar{u}(x, s) - s u(x, 0) - u_t(x, 0) = s^2 \bar{u}(x, s)$$
$$\mathcal{L}[c^2 u_{xx}] = c^2 \frac{d^2 \bar{u}}{dx^2}$$
Thus:
$$c^2 \frac{d^2 \bar{u}}{dx^2} - s^2 \bar{u} = 0 \implies \frac{d^2 \bar{u}}{dx^2} - \frac{s^2}{c^2} \bar{u} = 0$$

---

### 2. Solving the Spatial ODE
The general solution of this ODE is:
$$\bar{u}(x, s) = A(s) e^{-(s/c) x} + B(s) e^{+(s/c) x}$$
For $\operatorname{Re}(s) > 0$, the term $e^{+(s/c) x}$ diverges exponentially as $x \to \infty$.
Boundedness of the solution requires $B(s) \equiv 0$.
Thus:
$$\bar{u}(x, s) = A(s) e^{-(s/c) x}$$
At $x = 0$:
$$\bar{u}(0, s) = A(s) = \mathcal{L}[f(t)] = \bar{f}(s)$$
Therefore:
$$\bar{u}(x, s) = \bar{f}(s) e^{-s(x/c)}$$

---

### 3. Inverse Laplace Transform via the Time-Shift Property
Recall the fundamental Laplace time-delay / shift theorem:
$$\mathcal{L}^{-1}\left[ \bar{f}(s) e^{-s \tau} \right] = f(t - \tau) H(t - \tau)$$
where $H$ is the Heaviside step function:
$$H(t - \tau) = \begin{cases} 1, & t \ge \tau \\ 0, & t < \tau \end{cases}$$
Setting the delay time $\tau = \frac{x}{c}$:
$$u(x, t) = f\left(t - \frac{x}{c}\right) H\left(t - \frac{x}{c}\right) = \begin{cases} f\left(t - \frac{x}{c}\right), & t \ge \frac{x}{c} \\ 0, & t < \frac{x}{c} \end{cases}$$
This proves that the boundary signal propagates into the medium at the exact finite speed $c$ without distortion. Points at distance $x$ remain completely undisturbed until the wave front arrives at $t = x/c$. $\blacksquare$"""
            },
            {
                "tier": "Honors Challenge",
                "title": "Dirichlet Green's Function for the Upper Half-Plane and Poisson Formula",
                "statement": r"""Consider the upper half-plane $\Omega = \mathbb{R}^2_+ = \{ (x, y) \in \mathbb{R}^2 : y > 0 \}$.
1. Using the method of images, construct the exact Dirichlet Green's function $G(x, y; \xi, \eta)$ for Laplace's equation in $\mathbb{R}^2_+$.
2. Compute the normal derivative $\frac{\partial G}{\partial \mathbf{n}}$ along the boundary line $y = 0$.
3. Rigorously derive the Poisson Integral Formula for the upper half-plane and prove that for any bounded continuous boundary function $g(x)$, $\lim_{y \to 0^+} u(x, y) = g(x)$.""",
                "solution": r"""### 1. Construction of Green's Function via Method of Images
The fundamental solution in $\mathbb{R}^2$ with a source at $(\xi, \eta)$ (with $\eta > 0$) is:
$$\Phi(x, y; \xi, \eta) = -\frac{1}{2\pi} \ln\sqrt{(x - \xi)^2 + (y - \eta)^2} = -\frac{1}{4\pi}\ln\left[ (x - \xi)^2 + (y - \eta)^2 \right]$$
The image source point reflected across the boundary $y = 0$ is $(\xi, -\eta)$.
Define the Green's function:
$$G(x, y; \xi, \eta) = \Phi(x, y; \xi, \eta) - \Phi(x, y; \xi, -\eta) = -\frac{1}{4\pi}\ln\left[ \frac{(x - \xi)^2 + (y - \eta)^2}{(x - \xi)^2 + (y + \eta)^2} \right]$$
Notice that along the boundary $y = 0$:
$$G(x, 0; \xi, \eta) = -\frac{1}{4\pi}\ln\left[ \frac{(x - \xi)^2 + (-\eta)^2}{(x - \xi)^2 + (\eta)^2} \right] = -\frac{1}{4\pi}\ln(1) = 0$$
The Dirichlet boundary condition $G \equiv 0$ on $\partial\Omega$ is satisfied identically!

---

### 2. Normal Derivative on the Boundary
The outward unit normal vector to the domain $y > 0$ along $y = 0$ points in the negative $y$-direction: $\mathbf{n} = -\hat{\mathbf{j}}$.
Therefore:
$$\frac{\partial G}{\partial \mathbf{n}} = -\left. \frac{\partial G}{\partial y} \right|_{y=0}$$
Differentiating $G$ with respect to $y$:
$$\frac{\partial G}{\partial y} = -\frac{1}{4\pi} \left[ \frac{2(y - \eta)}{(x - \xi)^2 + (y - \eta)^2} - \frac{2(y + \eta)}{(x - \xi)^2 + (y + \eta)^2} \right]$$
Evaluating at $y = 0$:
$$\left. \frac{\partial G}{\partial y} \right|_{y=0} = -\frac{1}{4\pi} \left[ \frac{-2\eta}{(x - \xi)^2 + \eta^2} - \frac{2\eta}{(x - \xi)^2 + \eta^2} \right] = -\frac{1}{4\pi} \left[ \frac{-4\eta}{(x - \xi)^2 + \eta^2} \right] = \frac{\eta}{\pi [(x - \xi)^2 + \eta^2]}$$
Thus:
$$\frac{\partial G}{\partial \mathbf{n}} = -\left. \frac{\partial G}{\partial y} \right|_{y=0} = -\frac{\eta}{\pi [(x - \xi)^2 + \eta^2]}$$

---

### 3. Deduction of the Poisson Integral Formula
By Green's representation formula, for $\nabla^2 u = 0$ in $\mathbb{R}^2_+$ with $u(x, 0) = g(x)$:
$$u(\xi, \eta) = -\int_{-\infty}^\infty g(x) \frac{\partial G}{\partial \mathbf{n}}(x, 0; \xi, \eta)\,dx = \frac{\eta}{\pi} \int_{-\infty}^\infty \frac{g(x)}{(x - \xi)^2 + \eta^2}\,dx$$
Swapping notation so $(x, y)$ is the observation point and $s$ is the integration dummy variable:
$$u(x, y) = \frac{y}{\pi} \int_{-\infty}^\infty \frac{g(s)}{(s - x)^2 + y^2}\,ds$$

---

### 4. Boundary Limit Verification: $\lim_{y \to 0^+} u(x, y) = g(x)$
Let $z = \frac{s - x}{y} \implies s = x + y z \implies ds = y\,dz$.
Substitute this change of variables into the Poisson integral:
$$u(x, y) = \frac{y}{\pi} \int_{-\infty}^\infty \frac{g(x + y z)}{y^2 z^2 + y^2} y\,dz = \frac{1}{\pi} \int_{-\infty}^\infty \frac{g(x + y z)}{z^2 + 1}\,dz$$
Notice that the kernel is normalized:
$$\frac{1}{\pi}\int_{-\infty}^\infty \frac{1}{z^2 + 1}\,dz = \frac{1}{\pi} [\arctan(z)]_{-\infty}^\infty = \frac{1}{\pi}\left( \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) \right) = 1$$
Therefore:
$$u(x, y) - g(x) = \frac{1}{\pi}\int_{-\infty}^\infty \frac{g(x + y z) - g(x)}{z^2 + 1}\,dz$$
For any $\epsilon > 0$, by continuity of $g$ at $x$, choose $\delta > 0$ such that $|g(x + \tau) - g(x)| < \epsilon/2$ whenever $|\tau| \le \delta$.
Split the integral into $|z| \le \delta/y$ and $|z| > \delta/y$:
1. For $|z| \le \delta/y$, $|y z| \le \delta$:
   $$\left| \frac{1}{\pi}\int_{|z| \le \delta/y} \frac{g(x + yz) - g(x)}{z^2 + 1}\,dz \right| \le \frac{\epsilon}{2\pi} \int_{-\infty}^\infty \frac{dz}{z^2 + 1} = \frac{\epsilon}{2}$$
2. For $|z| > \delta/y$, since $g$ is bounded ($|g| \le M$):
   $$\left| \frac{1}{\pi}\int_{|z| > \delta/y} \frac{g(x + yz) - g(x)}{z^2 + 1}\,dz \right| \le \frac{2M}{\pi} \int_{|z| > \delta/y} \frac{dz}{z^2} = \frac{4M}{\pi} \frac{y}{\delta} \to 0 \quad \text{as } y \to 0^+$$
Choosing $y$ sufficiently small ensures the second term is $< \epsilon/2$.
Thus $|u(x, y) - g(x)| < \epsilon$ for all sufficiently small $y > 0$.
Hence $\lim_{y \to 0^+} u(x, y) = g(x)$. $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u8 = get_unit8()
    print(f"Loaded Unit 8: {u8['title']} with {len(u8['sections'])} sections and {len(u8['problems'])} problems.")
