# -*- coding: utf-8 -*-
"""
build_pde_unit7.py
Constructs Unit 7: Boundary Value Problems with Cylindrical & Spherical Symmetry: Special Functions
Strictly ZERO course numbers.
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Boundary Value Problems with Cylindrical & Spherical Symmetry: Special Functions",
        "leadSummary": "Advanced boundary value problems in curvilinear geometries: derivation of the Laplacian in cylindrical and spherical coordinate systems, Bessel's differential equation and Frobenius series solutions for J_n(x) and Y_n(x), vibrations of circular drumhead membranes and transient radial heat conduction in solid cylinders, Legendre's differential equation and orthogonal Legendre polynomials P_n(cos θ), and multipole expansions in spherical harmonics.",
        "simulations": ["sim_pde_cylindrical_drumhead_bessel"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Orthogonal Curvilinear Coordinates: Cylindrical & Spherical Laplacians",
                "content": r"""### 1. General Metric Scale Factors

Let $(u_1, u_2, u_3)$ be an orthogonal curvilinear coordinate system related to Cartesian coordinates $(x, y, z)$.
The differential displacement vector is:
$$d\mathbf{r} = \frac{\partial \mathbf{r}}{\partial u_1}\,du_1 + \frac{\partial \mathbf{r}}{\partial u_2}\,du_2 + \frac{\partial \mathbf{r}}{\partial u_3}\,du_3 = h_1 \hat{\mathbf{e}}_1\,du_1 + h_2 \hat{\mathbf{e}}_2\,du_2 + h_3 \hat{\mathbf{e}}_3\,du_3$$
where the **scale factors** (Lamé coefficients) are:
$$h_i = \left\| \frac{\partial \mathbf{r}}{\partial u_i} \right\| = \sqrt{ \left(\frac{\partial x}{\partial u_i}\right)^2 + \left(\frac{\partial y}{\partial u_i}\right)^2 + \left(\frac{\partial z}{\partial u_i}\right)^2 }, \quad i = 1, 2, 3$$
The gradient of a scalar field $\psi$ is:
$$\nabla \psi = \frac{1}{h_1}\frac{\partial \psi}{\partial u_1}\hat{\mathbf{e}}_1 + \frac{1}{h_2}\frac{\partial \psi}{\partial u_2}\hat{\mathbf{e}}_2 + \frac{1}{h_3}\frac{\partial \psi}{\partial u_3}\hat{\mathbf{e}}_3$$
The divergence of a vector field $\mathbf{A} = A_1 \hat{\mathbf{e}}_1 + A_2 \hat{\mathbf{e}}_2 + A_3 \hat{\mathbf{e}}_3$ is:
$$\nabla \cdot \mathbf{A} = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial u_1}(h_2 h_3 A_1) + \frac{\partial}{\partial u_2}(h_1 h_3 A_2) + \frac{\partial}{\partial u_3}(h_1 h_2 A_3) \right]$$
Combining $\nabla \cdot (\nabla \psi)$ gives the universal **Laplacian in orthogonal curvilinear coordinates**:
$$\nabla^2 \psi = \frac{1}{h_1 h_2 h_3} \left[ \frac{\partial}{\partial u_1}\left(\frac{h_2 h_3}{h_1}\frac{\partial \psi}{\partial u_1}\right) + \frac{\partial}{\partial u_2}\left(\frac{h_1 h_3}{h_2}\frac{\partial \psi}{\partial u_2}\right) + \frac{\partial}{\partial u_3}\left(\frac{h_1 h_2}{h_3}\frac{\partial \psi}{\partial u_3}\right) \right]$$

---

### 2. Cylindrical Coordinates $(r, \theta, z)$
The coordinates are $x = r\cos\theta, y = r\sin\theta, z = z$.
The scale factors are:
$$h_r = 1, \qquad h_\theta = r, \qquad h_z = 1$$
$$h_1 h_2 h_3 = r$$
Applying the Laplacian formula:
$$\nabla^2 \psi = \frac{1}{r} \left[ \frac{\partial}{\partial r}\left( r \frac{\partial \psi}{\partial r} \right) + \frac{\partial}{\partial \theta}\left( \frac{1}{r} \frac{\partial \psi}{\partial \theta} \right) + \frac{\partial}{\partial z}\left( r \frac{\partial \psi}{\partial z} \right) \right]$$

> **The Cylindrical Laplacian:**
> $$\nabla^2 \psi = \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial \psi}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 \psi}{\partial \theta^2} + \frac{\partial^2 \psi}{\partial z^2} = \frac{\partial^2 \psi}{\partial r^2} + \frac{1}{r}\frac{\partial \psi}{\partial r} + \frac{1}{r^2}\frac{\partial^2 \psi}{\partial \theta^2} + \frac{\partial^2 \psi}{\partial z^2}$$

---

### 3. Spherical Coordinates $(r, \theta, \phi)$
The coordinates are $x = r\sin\theta\cos\phi, y = r\sin\theta\sin\phi, z = r\cos\theta$ (where $\theta$ is the polar colatitude and $\phi$ is the azimuthal longitude).
The scale factors are:
$$h_r = 1, \qquad h_\theta = r, \qquad h_\phi = r\sin\theta$$
$$h_1 h_2 h_3 = r^2 \sin\theta$$

> **The Spherical Laplacian:**
> $$\nabla^2 \psi = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial \psi}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial \psi}{\partial \theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 \psi}{\partial \phi^2}$$"""
            },
            {
                "secNumber": "7.2",
                "title": "Bessel's Equation & Bessel Functions Jn, Yn",
                "content": r"""### 1. Separation of Variables in Cylindrical Geometry

Consider the Helmholtz eigenvalue equation $\nabla^2 u + \lambda u = 0$ in polar coordinates $(r, \theta)$.
Assume $u(r, \theta) = R(r) \Theta(\theta)$:
$$\frac{1}{r}(r R')' \Theta + \frac{1}{r^2} R \Theta'' + \lambda R \Theta = 0$$
Dividing by $R \Theta$ and multiplying by $r^2$:
$$\frac{r}{R}(r R')' + \lambda r^2 = -\frac{\Theta''}{\Theta} = m^2 \quad (m \in \{0, 1, 2, \dots\})$$
Multiplying out the radial part:
$$r^2 R'' + r R' + (\lambda r^2 - m^2) R = 0$$
Let $x = \sqrt{\lambda} r$. By the chain rule, this reduces to **Bessel's Differential Equation of order $m$**:
$$x^2 \frac{d^2 R}{dx^2} + x \frac{dR}{dx} + (x^2 - m^2) R = 0$$

---

### 2. Series Solution via the Frobenius Method

Since $x = 0$ is a regular singular point, assume a generalized power series $R(x) = \sum_{k=0}^\infty c_k x^{k+s}$.
The indicial equation is $s(s-1) + s - m^2 = 0 \implies s^2 - m^2 = 0 \implies s = \pm m$.
For $s = +m$:

> **Definition 7.1 (Bessel Function of the First Kind $J_m(x)$):**
> $$J_m(x) = \sum_{k=0}^\infty \frac{(-1)^k}{k!\,(k+m)!} \left(\frac{x}{2}\right)^{2k+m}$$
> The series converges absolutely and uniformly for all $x \in \mathbb{C}$.
> - $J_0(0) = 1$, and $J_m(0) = 0$ for all $m \ge 1$.
> - As $x \to \infty$, $J_m(x)$ behaves asymptotically as an oscillating decaying cosine wave:
>   $$J_m(x) \sim \sqrt{\frac{2}{\pi x}} \cos\left( x - \frac{m\pi}{2} - \frac{\pi}{4} \right)$$

> **Definition 7.2 (Bessel Function of the Second Kind $Y_m(x)$ / Weber Function):**
> The second linearly independent solution is defined for non-integer $\nu$ by:
> $$Y_\nu(x) = \frac{J_\nu(x)\cos(\nu\pi) - J_{-\nu}(x)}{\sin(\nu\pi)}$$
> and for integer $m$ by the limit $Y_m(x) = \lim_{\nu \to m} Y_\nu(x)$.
> Crucially, as $x \to 0^+$, $Y_m(x)$ diverges logarithmically:
> $$Y_0(x) \sim \frac{2}{\pi} \ln x \to -\infty \quad \text{as } x \to 0^+$$
> Therefore, for any physical domain containing the center axis $r = 0$, $Y_m$ must be rejected, retaining only $J_m$."""
            },
            {
                "secNumber": "7.3",
                "title": "Circular Drumhead Vibrations & Radial Cylindrical Diffusion",
                "content": r"""### 1. Vibrations of an Elastic Circular Drumhead

Consider a circular membrane of radius $a$ clamped at its boundary $r = a$:
$$\begin{cases}
u_{tt} = c^2 \nabla^2 u = c^2 \left[ u_{rr} + \frac{1}{r} u_r + \frac{1}{r^2} u_{\theta\theta} \right], & 0 < r < a, \quad t > 0 \\
u(a, \theta, t) = 0, & t \ge 0 \\
u(r, \theta, 0) = f(r, \theta), \quad u_t(r, \theta, 0) = g(r, \theta)
\end{cases}$$

Separating variables $u(r, \theta, t) = R(r) \Theta(\theta) T(t)$ yields:
1. $\Theta_m(\theta) = A_m \cos(m\theta) + B_m \sin(m\theta)$ ($m = 0, 1, 2, \dots$)
2. $R_m(r) = J_m(k r)$, where the boundary condition requires:
   $$J_m(k a) = 0 \implies k_{m,n} = \frac{\alpha_{m,n}}{a}, \quad n = 1, 2, 3, \dots$$
   where $\alpha_{m,n}$ is the $n$-th positive zero of $J_m(x)$.
3. The natural circular frequencies are:
   $$\omega_{m,n} = c k_{m,n} = \frac{c \alpha_{m,n}}{a}$$

> **Theorem 7.1 (Eigenmode Structure):**
> Each **normal mode $(m, n)$** of the vibrating circular membrane is given by:
> $$u_{m,n}(r, \theta, t) = J_m\left(\frac{\alpha_{m,n} r}{a}\right) \left[ A_{m,n} \cos(m\theta) + B_{m,n} \sin(m\theta) \right] \cos(\omega_{m,n} t - \delta_{m,n})$$
> The nodal lines where $u_{m,n} = 0$ at all times consist of:
> - **$m$ Nodal Diameters** where $\cos(m\theta) = 0$.
> - **$n - 1$ Internal Nodal Circles** where $r = \frac{\alpha_{m,k}}{\alpha_{m,n}} a$ for $k = 1, \dots, n - 1$ (plus the rim $r = a$)."""
            },
            {
                "secNumber": "7.4",
                "title": "Spherical Symmetry: Legendre's Differential Equation & Polynomials",
                "content": r"""### 1. Axisymmetric Laplace Equation in Spherical Coordinates

When a physical potential possesses azimuthal symmetry around the $z$-axis (no dependence on $\phi$), Laplace's equation in spherical coordinates reduces to:
$$\nabla^2 u = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 \frac{\partial u}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial u}{\partial \theta}\right) = 0$$
Assume a product solution $u(r, \theta) = R(r) \Theta(\theta)$:
$$\frac{1}{R}\frac{d}{dr}\left(r^2 \frac{dR}{dr}\right) = -\frac{1}{\Theta\sin\theta}\frac{d}{d\theta}\left(\sin\theta \frac{d\Theta}{d\theta}\right) = \lambda$$

---

### 2. Legendre's Differential Equation

Consider the angular ODE:
$$\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta \frac{d\Theta}{d\theta}\right) + \lambda \Theta = 0$$
Substitute the variable $\xi = \cos\theta$ (where $\xi \in [-1, 1]$ as $\theta \in [0, \pi]$).
Then $\frac{d\xi}{d\theta} = -\sin\theta$ and $\sin^2\theta = 1 - \xi^2$.
The chain rule gives:
$$\frac{d\Theta}{d\theta} = -\sin\theta \frac{d\Theta}{d\xi} \implies \sin\theta \frac{d\Theta}{d\theta} = -(1 - \xi^2) \frac{d\Theta}{d\xi}$$
Substituting into the angular equation:
$$\frac{d}{d\xi}\left[ (1 - \xi^2) \frac{d\Theta}{d\xi} \right] + \lambda \Theta = 0 \implies (1 - \xi^2)\frac{d^2 \Theta}{d\xi^2} - 2\xi \frac{d\Theta}{d\xi} + \lambda \Theta = 0$$
This is **Legendre's Differential Equation**.

> **Theorem 7.2 (Quantization of $\lambda$ and Legendre Polynomials):**
> Solutions to Legendre's equation that remain finite and non-singular at both poles $\theta = 0$ ($\xi = 1$) and $\theta = \pi$ ($\xi = -1$) exist **if and only if** the separation constant is quantized as:
> $$\lambda = n(n + 1), \qquad n \in \{0, 1, 2, 3, \dots\}$$
> Under this quantization, the bounded solutions are the **Legendre Polynomials** $P_n(\xi)$:
> - $P_0(\xi) = 1$
> - $P_1(\xi) = \xi = \cos\theta$
> - $P_2(\xi) = \frac{1}{2}(3\xi^2 - 1) = \frac{1}{2}(3\cos^2\theta - 1)$
> - $P_3(\xi) = \frac{1}{2}(5\xi^3 - 3\xi) = \frac{1}{2}(5\cos^3\theta - 3\cos\theta)$

> **Definition 7.3 (Rodrigues' Formula):**
> $$P_n(\xi) = \frac{1}{2^n n!} \frac{d^n}{d\xi^n}\left[ (\xi^2 - 1)^n \right]$$"""
            },
            {
                "secNumber": "7.5",
                "title": "Multipole Expansions & Orthogonality in Spherical Harmonics",
                "content": r"""### 1. Orthogonality of Legendre Polynomials

> **Theorem 7.3 (Orthogonality Relation):**
> On the interval $[-1, 1]$, the Legendre polynomials form a complete orthogonal set with respect to unit weight:
> $$\int_{-1}^1 P_n(\xi) P_m(\xi)\,d\xi = \frac{2}{2n + 1} \delta_{nm}$$
> In terms of colatitude $\theta$:
> $$\int_0^\pi P_n(\cos\theta) P_m(\cos\theta) \sin\theta\,d\theta = \frac{2}{2n + 1} \delta_{nm}$$

---

### 2. Radial Solutions and General Axisymmetric Potential

For $\lambda = n(n + 1)$, the radial ODE is:
$$\frac{d}{dr}\left(r^2 \frac{dR}{dr}\right) - n(n + 1) R = 0 \implies r^2 R'' + 2r R' - n(n + 1) R = 0$$
This is an Euler-Cauchy ODE with trial solutions $R(r) = r^\gamma$:
$$\gamma(\gamma - 1) + 2\gamma - n(n + 1) = 0 \implies \gamma^2 + \gamma - n(n + 1) = (\gamma - n)(\gamma + n + 1) = 0$$
The roots are $\gamma = n$ and $\gamma = -(n + 1)$.
Thus:
$$R_n(r) = A_n r^n + \frac{B_n}{r^{n+1}}$$

> **Theorem 7.4 (General Axisymmetric Harmonic Potential):**
> Any axisymmetric solution to Laplace's equation $\nabla^2 u = 0$ in spherical coordinates is represented by:
> $$u(r, \theta) = \sum_{n=0}^\infty \left[ A_n r^n + \frac{B_n}{r^{n+1}} \right] P_n(\cos\theta)$$
> - For interior problems (containing origin $r = 0$), all $B_n = 0$.
> - For exterior problems (bounded as $r \to \infty$), all $A_n = 0$ (except possibly $A_0$ for potential at infinity).

---

### 3. Generating Function and Multipole Expansion

The generating function for Legendre polynomials is:
$$\frac{1}{\sqrt{1 - 2\xi t + t^2}} = \sum_{n=0}^\infty P_n(\xi) t^n, \qquad |t| < 1$$
In electrostatics, the potential of a point charge $q$ at $\mathbf{r}' = (0, 0, d)$ observed at $\mathbf{r} = (r, \theta, \phi)$ with $r > d$ is:
$$\Phi(r, \theta) = \frac{q}{4\pi\epsilon_0} \frac{1}{|\mathbf{r} - \mathbf{r}'|} = \frac{q}{4\pi\epsilon_0} \frac{1}{\sqrt{r^2 - 2rd\cos\theta + d^2}} = \frac{q}{4\pi\epsilon_0 r} \sum_{n=0}^\infty P_n(\cos\theta) \left(\frac{d}{r}\right)^n$$
- $n = 0$: Monopole potential $\propto 1/r$.
- $n = 1$: Dipole potential $\propto d\cos\theta / r^2$.
- $n = 2$: Quadrupole potential $\propto d^2 P_2(\cos\theta) / r^3$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Axisymmetric Radial Heat Flow in a Long Solid Cylinder",
                "statement": r"""A long solid cylinder of radius $a$ and thermal diffusivity $\alpha$ initially has uniform temperature $T_0$.
At $t = 0$, its outer surface $r = a$ is plunged into an ice bath held at zero temperature:
$$u(a, t) = 0 \quad \forall t > 0$$
Assuming no dependence on $\theta$ or $z$:
1. Set up the radial initial-boundary value problem.
2. Find the complete Fourier-Bessel series solution $u(r, t)$.
3. Determine the temperature at the center axis $r = 0$ as a function of time.""",
                "solution": r"""### 1. Radial Initial-Boundary Value Problem
The heat equation in axisymmetric cylindrical coordinates is:
$$\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial r^2} + \frac{1}{r} \frac{\partial u}{\partial r} \right), \qquad 0 \le r < a, \quad t > 0$$
subject to:
- Boundary condition: $u(a, t) = 0$
- Regularity condition: $|u(0, t)| < \infty$
- Initial condition: $u(r, 0) = T_0$ for $0 \le r < a$.

---

### 2. Separation of Variables and Bessel Expansion
Separating variables $u(r, t) = R(r) T(t)$:
$$\frac{T'(t)}{\alpha T(t)} = \frac{R''(r) + \frac{1}{r} R'(r)}{R(r)} = -\lambda = -k^2$$
1. Radial equation: $r^2 R'' + r R' + k^2 r^2 R = 0$.
   The general solution is $R(r) = C_1 J_0(k r) + C_2 Y_0(k r)$.
   Since $Y_0(k r) \to -\infty$ as $r \to 0$, regularity forces $C_2 = 0$.
   Thus $R(r) = J_0(k r)$.
   Boundary condition at $r = a$:
   $$J_0(k a) = 0 \implies k_m = \frac{\alpha_{0,m}}{a}, \quad m = 1, 2, 3, \dots$$
   where $\alpha_{0,m}$ are the positive roots of $J_0(x) = 0$.
2. Temporal ODE: $T_m'(t) + \alpha k_m^2 T_m(t) = 0 \implies T_m(t) = \exp\left( -\alpha \left(\frac{\alpha_{0,m}}{a}\right)^2 t \right)$.

The general solution is:
$$u(r, t) = \sum_{m=1}^\infty c_m J_0\left(\frac{\alpha_{0,m} r}{a}\right) \exp\left( -\alpha \frac{\alpha_{0,m}^2}{a^2} t \right)$$

---

### 3. Fourier-Bessel Coefficients
At $t = 0$:
$$T_0 = \sum_{m=1}^\infty c_m J_0\left(\frac{\alpha_{0,m} r}{a}\right)$$
By the orthogonality of Bessel functions with weight $r$:
$$c_m = \frac{2}{a^2 [J_1(\alpha_{0,m})]^2} \int_0^a r T_0 J_0\left(\frac{\alpha_{0,m} r}{a}\right)\,dr$$
Using the Bessel recurrence identity $\frac{d}{dx}[x J_1(x)] = x J_0(x)$:
Let $\xi = \frac{\alpha_{0,m} r}{a} \implies r = \frac{a}{\alpha_{0,m}}\xi \implies dr = \frac{a}{\alpha_{0,m}}d\xi$.
$$\int_0^a r J_0\left(\frac{\alpha_{0,m} r}{a}\right)\,dr = \frac{a^2}{\alpha_{0,m}^2} \int_0^{\alpha_{0,m}} \xi J_0(\xi)\,d\xi = \frac{a^2}{\alpha_{0,m}^2} \left[ \xi J_1(\xi) \right]_0^{\alpha_{0,m}} = \frac{a^2}{\alpha_{0,m}} J_1(\alpha_{0,m})$$
Substituting into $c_m$:
$$c_m = \frac{2 T_0}{a^2 [J_1(\alpha_{0,m})]^2} \frac{a^2}{\alpha_{0,m}} J_1(\alpha_{0,m}) = \frac{2 T_0}{\alpha_{0,m} J_1(\alpha_{0,m})}$$

Therefore, the complete series solution is:
$$u(r, t) = 2 T_0 \sum_{m=1}^\infty \frac{J_0\left(\frac{\alpha_{0,m} r}{a}\right)}{\alpha_{0,m} J_1(\alpha_{0,m})} \exp\left( -\alpha \frac{\alpha_{0,m}^2}{a^2} t \right)$$

---

### 4. Center Temperature ($r = 0$)
Since $J_0(0) = 1$:
$$u(0, t) = 2 T_0 \sum_{m=1}^\infty \frac{1}{\alpha_{0,m} J_1(\alpha_{0,m})} \exp\left( -\alpha \frac{\alpha_{0,m}^2}{a^2} t \right)$$
For large times, the first root $\alpha_{0,1} \approx 2.4048$ dominates:
$$u(0, t) \sim \frac{2 T_0}{\alpha_{0,1} J_1(\alpha_{0,1})} \exp\left( -\frac{5.783 \alpha t}{a^2} \right)$$
$\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Grounded Conducting Sphere in a Uniform External Electric Field",
                "statement": r"""A grounded conducting sphere of radius $a$ is placed in an initially uniform electric field $\mathbf{E} = E_0 \hat{\mathbf{z}}$.
1. Set up the boundary value problem for the electrostatic potential $\Phi(r, \theta)$ in spherical coordinates.
2. Solve for $\Phi(r, \theta)$ for all $r \ge a$ using Legendre polynomials.
3. Determine the induced surface charge density $\sigma(\theta)$ on the sphere.""",
                "solution": r"""### 1. Formulation of the Boundary Value Problem
In the vacuum region exterior to the sphere ($r > a$), there is no charge, so $\nabla^2 \Phi = 0$.
The problem has azimuthal symmetry around the $z$-axis, so $\Phi = \Phi(r, \theta)$.
Boundary conditions:
1. Grounded sphere at $r = a$: $\Phi(a, \theta) = 0$.
2. Far from the sphere ($r \to \infty$), the potential must approach the uniform field potential:
   $$\mathbf{E} = -\nabla \Phi_0 = E_0 \hat{\mathbf{z}} \implies \Phi_0 = -E_0 z = -E_0 r \cos\theta = -E_0 r P_1(\cos\theta)$$
   Thus: $\Phi(r, \theta) \to -E_0 r P_1(\cos\theta)$ as $r \to \infty$.

---

### 2. Series Solution via Legendre Polynomials
The general exterior axisymmetric solution to Laplace's equation is:
$$\Phi(r, \theta) = \sum_{n=0}^\infty \left( A_n r^n + \frac{B_n}{r^{n+1}} \right) P_n(\cos\theta)$$
Matching the asymptotic condition as $r \to \infty$:
- For $n = 1$: $A_1 = -E_0$.
- For all $n \ne 1$: $A_n = 0$ (so the potential does not blow up faster than $r$).
Thus:
$$\Phi(r, \theta) = -E_0 r P_1(\cos\theta) + \sum_{n=0}^\infty \frac{B_n}{r^{n+1}} P_n(\cos\theta)$$

Now apply the boundary condition on the grounded sphere $r = a$:
$$\Phi(a, \theta) = -E_0 a P_1(\cos\theta) + \sum_{n=0}^\infty \frac{B_n}{a^{n+1}} P_n(\cos\theta) = 0$$
By orthogonality of the Legendre polynomials, coefficients of each $P_n(\cos\theta)$ must vanish:
- For $n = 1$: $-E_0 a + \frac{B_1}{a^2} = 0 \implies B_1 = E_0 a^3$.
- For all $n \ne 1$: $\frac{B_n}{a^{n+1}} = 0 \implies B_n = 0$.

Therefore, the exact potential outside the sphere is:
$$\Phi(r, \theta) = -E_0 r \cos\theta + \frac{E_0 a^3}{r^2} \cos\theta = -E_0 \left( r - \frac{a^3}{r^2} \right) \cos\theta$$

---

### 3. Induced Surface Charge Density
By Gauss's law at a conducting boundary:
$$\sigma(\theta) = -\epsilon_0 \left. \frac{\partial \Phi}{\partial r} \right|_{r=a}$$
Compute the radial derivative:
$$\frac{\partial \Phi}{\partial r} = -E_0 \left( 1 + \frac{2a^3}{r^3} \right) \cos\theta$$
Evaluating at $r = a$:
$$\left. \frac{\partial \Phi}{\partial r} \right|_{r=a} = -E_0 (1 + 2) \cos\theta = -3 E_0 \cos\theta$$
Therefore, the induced surface charge density is:
$$\sigma(\theta) = -\epsilon_0 (-3 E_0 \cos\theta) = 3 \epsilon_0 E_0 \cos\theta$$
The charge density is positive on the upper hemisphere ($\theta < \pi/2$) and negative on the lower hemisphere ($\theta > \pi/2$), forming an induced dipole moment $\mathbf{p} = 4\pi \epsilon_0 a^3 E_0 \hat{\mathbf{z}}$. $\blacksquare$"""
            },
            {
                "tier": "Honors Challenge",
                "title": "Bessel Function Orthogonality and Fourier-Bessel Completeness",
                "statement": r"""Let $J_n(x)$ be the Bessel function of the first kind of integer order $n \ge 0$, and let $\alpha_{n,1} < \alpha_{n,2} < \dots$ denote its consecutive positive zeros.
1. Rigorously prove the Sturm-Liouville orthogonality relation:
   $$\int_0^a r J_n\left(\frac{\alpha_{n,k} r}{a}\right) J_n\left(\frac{\alpha_{n,m} r}{a}\right)\,dr = 0 \quad \text{for } k \ne m$$
2. Prove the normalization integral formula:
   $$\int_0^a r \left[ J_n\left(\frac{\alpha_{n,k} r}{a}\right) \right]^2\,dr = \frac{a^2}{2} \left[ J_{n+1}(\alpha_{n,k}) \right]^2$$""",
                "solution": r"""### 1. Proof of Orthogonality for $k \ne m$
Let $u(r) = J_n\left(\frac{\alpha_{n,k} r}{a}\right)$ and $v(r) = J_n\left(\frac{\alpha_{n,m} r}{a}\right)$, with $\lambda_k = \frac{\alpha_{n,k}^2}{a^2}$ and $\lambda_m = \frac{\alpha_{n,m}^2}{a^2}$.
Both functions satisfy Bessel's differential equation in self-adjoint Sturm-Liouville form:
$$(r u')' + \left( \lambda_k r - \frac{n^2}{r} \right) u = 0$$
$$(r v')' + \left( \lambda_m r - \frac{n^2}{r} \right) v = 0$$
Multiply the first equation by $v$ and the second equation by $u$, and subtract:
$$v (r u')' - u (r v')' + (\lambda_k - \lambda_m) r u v = 0$$
Notice that:
$$v (r u')' - u (r v')' = \frac{d}{dr}\left[ r (v u' - u v') \right]$$
Integrating from $r = 0$ to $r = a$:
$$\int_0^a \frac{d}{dr}\left[ r (v u' - u v') \right]\,dr + (\lambda_k - \lambda_m) \int_0^a r u v\,dr = 0$$
Evaluating the boundary term:
$$\left[ r (v(r) u'(r) - u(r) v'(r)) \right]_0^a = a [v(a) u'(a) - u(a) v'(a)] - 0$$
Since $\alpha_{n,k}$ and $\alpha_{n,m}$ are roots of $J_n$, we have:
$$u(a) = J_n(\alpha_{n,k}) = 0, \qquad v(a) = J_n(\alpha_{n,m}) = 0$$
Thus the boundary term vanishes identically at both $r = a$ and $r = 0$!
$$(\lambda_k - \lambda_m) \int_0^a r J_n\left(\frac{\alpha_{n,k} r}{a}\right) J_n\left(\frac{\alpha_{n,m} r}{a}\right)\,dr = 0$$
Since $k \ne m$, $\lambda_k \ne \lambda_m$, which forces:
$$\int_0^a r J_n\left(\frac{\alpha_{n,k} r}{a}\right) J_n\left(\frac{\alpha_{n,m} r}{a}\right)\,dr = 0 \quad \blacksquare$$

---

### 2. Proof of the Normalization Integral
To evaluate the integral when $k = m$, consider Bessel's ODE for $y(r) = J_n(k r)$:
$$r^2 y'' + r y' + (k^2 r^2 - n^2) y = 0$$
Multiply the entire equation by $2 y'$:
$$2 r^2 y' y'' + 2 r (y')^2 + 2 k^2 r^2 y y' - 2 n^2 y y' = 0$$
Notice the derivative identities:
- $2 r^2 y' y'' + 2 r (y')^2 = \frac{d}{dr}\left[ r^2 (y')^2 \right]$
- $2 k^2 r^2 y y' = \frac{d}{dr}\left[ k^2 r^2 y^2 \right] - 2 k^2 r y^2$
- $2 n^2 y y' = \frac{d}{dr}\left[ n^2 y^2 \right]$

Substitute these into the equation:
$$\frac{d}{dr}\left[ r^2 (y')^2 \right] + \frac{d}{dr}\left[ k^2 r^2 y^2 \right] - 2 k^2 r y^2 - \frac{d}{dr}\left[ n^2 y^2 \right] = 0$$
Rearranging to isolate $2 k^2 r y^2$:
$$2 k^2 r y^2 = \frac{d}{dr}\left[ r^2 (y')^2 + (k^2 r^2 - n^2) y^2 \right]$$
Now integrate from $r = 0$ to $r = a$:
$$2 k^2 \int_0^a r [J_n(k r)]^2\,dr = \left[ r^2 [y'(r)]^2 + (k^2 r^2 - n^2) [y(r)]^2 \right]_0^a$$
At $r = 0$, both terms vanish.
At $r = a$, since $k = \alpha_{n,k}/a$, we have $y(a) = J_n(k a) = J_n(\alpha_{n,k}) = 0$.
Thus the second term vanishes at $r = a$!
$$2 k^2 \int_0^a r [J_n(k r)]^2\,dr = a^2 [y'(a)]^2$$
Now compute $y'(a)$:
$$y(r) = J_n(k r) \implies y'(r) = k J_n'(k r) \implies y'(a) = k J_n'(\alpha_{n,k})$$
Using the Bessel recurrence relation $x J_n'(x) = n J_n(x) - x J_{n+1}(x)$:
At $x = \alpha_{n,k}$, since $J_n(\alpha_{n,k}) = 0$:
$$\alpha_{n,k} J_n'(\alpha_{n,k}) = -\alpha_{n,k} J_{n+1}(\alpha_{n,k}) \implies J_n'(\alpha_{n,k}) = -J_{n+1}(\alpha_{n,k})$$
Thus:
$$[y'(a)]^2 = k^2 [J_n'(\alpha_{n,k})]^2 = k^2 [J_{n+1}(\alpha_{n,k})]^2$$
Substituting this back into the integrated formula:
$$2 k^2 \int_0^a r [J_n(k r)]^2\,dr = a^2 k^2 [J_{n+1}(\alpha_{n,k})]^2$$
Dividing both sides by $2 k^2$:
$$\int_0^a r \left[ J_n\left(\frac{\alpha_{n,k} r}{a}\right) \right]^2\,dr = \frac{a^2}{2} [J_{n+1}(\alpha_{n,k})]^2 \quad \blacksquare$$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u7 = get_unit7()
    print(f"Loaded Unit 7: {u7['title']} with {len(u7['sections'])} sections and {len(u7['problems'])} problems.")
