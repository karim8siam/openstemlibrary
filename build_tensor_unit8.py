# -*- coding: utf-8 -*-
"""
build_tensor_unit8.py
Constructs Unit 8: Physical Applications: Continuum Mechanics, Electromagnetism & Gravitation
Strictly ZERO course numbers.
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Physical Applications: Continuum Mechanics, Electromagnetism & Gravitation",
        "leadSummary": "Application of tensor analysis to the fundamental laws of classical physics and general relativity: Cauchy stress and the stress-energy-momentum tensor T^{\\mu\\nu}, relativistic conservation laws \\nabla_\\mu T^{\\mu\\nu} = 0, covariant formulation of Maxwell electrodynamics with electromagnetic field tensor F_{\\mu\\nu} = \\partial_\\mu A_\\nu - \\partial_\\nu A_\\mu and Lorentz force, the geodesic principle and gravitational time dilation / redshift, derivation and physical interpretation of the Einstein Field Equations G_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = (8\\pi G / c^4) T_{\\mu\\nu}, the static spherically symmetric Schwarzschild solution, Mercury's anomalous perihelion precession, and gravitational deflection of light.",
        "simulations": ["sim_tensor_einstein_field"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Stress-Energy-Momentum Tensors & Conservation Laws in Curved Coordinates",
                "content": r"""### 1. Cauchy Stress Tensor in Continuum Mechanics
In classical 3D continuum mechanics, internal contact forces distributed across an infinitesimal area element $d\mathbf{S} = \mathbf{n} \, dS$ are characterized by the **Cauchy stress tensor** $\sigma^{ij}$:
$$dF^i = \sigma^{ij} n_j \, dS$$
- **Conservation of Linear Momentum:** In the absence of body forces:
  $$\nabla_j \sigma^{ij} = \rho \frac{D v^i}{Dt}$$
  where $\nabla_j$ is the covariant derivative associated with the spatial Riemannian metric $g_{ij}$.
- **Conservation of Angular Momentum:** By requiring the net torque on an infinitesimal volume element to vanish, the stress tensor must be symmetric:
  $$\sigma^{ij} = \sigma^{ji}$$

---

### 2. The Relativistic Stress-Energy-Momentum Tensor $T^{\mu\nu}$
In 4-dimensional pseudo-Riemannian spacetime $(M, g_{\mu\nu})$, energy, momentum density, shear stress, and isotropic pressure are unified into a symmetric rank-2 contravariant tensor field $T^{\mu\nu}$:

$$\left( T^{\mu\nu} \right) = \begin{pmatrix} 
T^{00} & T^{01} & T^{02} & T^{03} \\
T^{10} & T^{11} & T^{12} & T^{13} \\
T^{20} & T^{21} & T^{22} & T^{23} \\
T^{30} & T^{31} & T^{32} & T^{33}
\end{pmatrix} = \begin{pmatrix}
\text{Energy Density } (\rho c^2) & \text{Energy Flux / } c \\
c \times \text{Momentum Density} & \text{Stress Tensor } (\sigma^{ij})
\end{pmatrix}$$

#### Perfect Fluid Stress-Energy Tensor:
For an ideal fluid characterized by proper energy density $\rho(x)$, isotropic pressure $p(x)$, and 4-velocity field $u^\mu = \frac{dx^\mu}{d\tau}$ (normalized such that $g_{\mu\nu} u^\mu u^\nu = -c^2$):
$$T^{\mu\nu} = \left( \rho + \frac{p}{c^2} \right) u^\mu u^\nu + p g^{\mu\nu}$$

---

### 3. Local Conservation Laws
In special relativity (flat Minkowski spacetime $\eta_{\mu\nu}$), conservation of energy and momentum is expressed as $\partial_\mu T^{\mu\nu} = 0$.
According to the principle of **minimal gravitational coupling** (equivalence principle), the physical conservation law in curved spacetime is obtained by replacing ordinary derivatives with covariant derivatives:

> **Fundamental Conservation Law:**
> $$\nabla_\mu T^{\mu\nu} = 0 \iff \frac{1}{\sqrt{-g}} \frac{\partial}{\partial x^\mu} \left( \sqrt{-g} T^{\mu\nu} \right) + \Gamma^\nu_{\mu\alpha} T^{\mu\alpha} = 0$$

Projecting along and orthogonal to the 4-velocity $u^\nu$ yields the relativistic continuity equation and the **relativistic Euler equation** of fluid dynamics!"""
            },
            {
                "secNumber": "8.2",
                "title": "Covariant Formulation of Maxwell's Electrodynamics ($F_{\\mu\\nu}$, $\\nabla_\\mu F^{\\mu\\nu} = \\mu_0 J^\\nu$)",
                "content": r"""### 1. The 4-Potential and Field Strength Tensor
Classical electrodynamics is governed by electric and magnetic vector fields $\mathbf{E}$ and $\mathbf{B}$, which mix under Lorentz coordinate transformations.
Tensor analysis unifies them into a single antisymmetric rank-2 covariant tensor field $F_{\mu\nu}$, called the **Faraday (electromagnetic field) tensor**.

Let $A_\mu = (-\phi/c, \mathbf{A})$ be the covariant electromagnetic 4-potential.

> **Definition 8.1 (Electromagnetic Field Tensor):**
> $$F_{\mu\nu} \equiv \nabla_\mu A_\nu - \nabla_\nu A_\mu = \partial_\mu A_\nu - \partial_\nu A_\mu$$
> Because the connection coefficients $\Gamma^\lambda_{\mu\nu} = \Gamma^\lambda_{\nu\mu}$ are symmetric, the Christoffel symbols cancel identically!

In matrix form with metric signature $(-, +, +, +)$:
$$(F_{\mu\nu}) = \begin{pmatrix}
0 & -E_x/c & -E_y/c & -E_z/c \\
E_x/c & 0 & B_z & -B_y \\
E_y/c & -B_z & 0 & B_x \\
E_z/c & B_y & -B_x & 0
\end{pmatrix}$$
By raising indices with $g^{\mu\alpha} g^{\nu\beta}$, we obtain the contravariant tensor $F^{\mu\nu}$.

---

### 2. Covariant Maxwell Equations

> **Theorem 8.1 (Maxwell's Equations in Curved Spacetime):**
> The four classical Maxwell equations reduce to two elegant, manifestly covariant tensor equations:
> 1. **Inhomogeneous Maxwell Equations (Sources):**
>    $$\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu \iff \frac{1}{\sqrt{-g}} \partial_\mu \left( \sqrt{-g} F^{\mu\nu} \right) = \mu_0 J^\nu$$
>    where $J^\nu = (\rho c, \mathbf{J})$ is the 4-current density.
> 2. **Homogeneous Maxwell Equations (Bianchi Identity):**
>    $$\nabla_\lambda F_{\mu\nu} + \nabla_\mu F_{\nu\lambda} + \nabla_\nu F_{\lambda\mu} = \partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0$$

#### Automatic Charge Conservation:
Taking the covariant divergence of the inhomogeneous equation:
$$\mu_0 \nabla_\nu J^\nu = \nabla_\nu \nabla_\mu F^{\mu\nu} = \frac{1}{2} [\nabla_\nu, \nabla_\mu] F^{\mu\nu} = 0$$
because $F^{\mu\nu}$ is antisymmetric while the commutator contraction is symmetric.
Thus, **electric charge conservation $\nabla_\nu J^\nu = 0$ is an exact geometric identity**!

---

### 3. The Lorentz Force Density
The electromagnetic 4-force density acting on charged matter is:
$$f^\mu = F^{\mu\nu} J_\nu$$
which unifies Coulomb electric force and magnetic Lorentz force $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$."""
            },
            {
                "secNumber": "8.3",
                "title": "The Geodesic Principle & Gravitational Time Dilation / Redshift",
                "content": r"""### 1. The Geodesic Hypothesis
In Einstein's theory of General Relativity, gravity is not a physical Newtonian force, but the curvature of spacetime.
Free particles experiencing no non-gravitational forces follow **geodesics** of the spacetime metric:
$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0$$
where $\tau$ is the proper time experienced by a clock moving along the worldline:
$$c^2 d\tau^2 = -g_{\mu\nu} dx^\mu dx^\nu$$

---

### 2. Gravitational Time Dilation
Consider a static gravitational field with metric:
$$ds^2 = g_{00}(x) (dx^0)^2 + g_{ij}(x) dx^i dx^j = -c^2 d\tau^2$$
For a stationary observer situated at fixed spatial coordinates ($dx^i = 0$):
$$-c^2 d\tau^2 = g_{00}(x) c^2 dt^2 \implies d\tau = \sqrt{-g_{00}(x)} \, dt$$
Let two clocks be stationed at positions $A$ and $B$ where the metric components are $g_{00}(A)$ and $g_{00}(B)$:
$$\frac{d\tau_A}{d\tau_B} = \frac{\sqrt{-g_{00}(A)}}{\sqrt{-g_{00}(B)}}$$
In a weak Newtonian gravitational potential $\Phi(x)$, $g_{00} \approx -\left( 1 + \frac{2\Phi}{c^2} \right)$:
$$d\tau \approx \left( 1 + \frac{\Phi}{c^2} \right) dt$$
Clocks situated deeper in a gravitational well ($\Phi < 0$) run measurably slower than clocks higher up!

---

### 3. Gravitational Redshift of Light
A light wave emitted at position $A$ with frequency $\nu_A$ and received at position $B$ undergoes a gravitational frequency shift:
$$\frac{\nu_B}{\nu_A} = \frac{\sqrt{-g_{00}(A)}}{\sqrt{-g_{00}(B)}}$$
For light escaping from the surface of a star of mass $M$ and radius $R$ ($g_{00} = -\left(1 - \frac{2GM}{c^2 R}\right)$) to a distant observer ($g_{00}(\infty) = -1$):
$$\nu_\infty = \nu_{\text{emit}} \sqrt{1 - \frac{2GM}{c^2 R}} < \nu_{\text{emit}}$$
The light is **redshifted** ($\Delta \lambda > 0$), directly confirming the curvature of the metric tensor!"""
            },
            {
                "secNumber": "8.4",
                "title": "The Einstein Field Equations $G_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = \\frac{8\\pi G}{c^4} T_{\\mu\\nu}$",
                "content": r"""### 1. The Search for the Gravitational Field Equations
In Newtonian gravity, the gravitational potential $\Phi$ satisfies Poisson's equation:
$$\nabla^2 \Phi = 4\pi G \rho$$
Einstein sought a tensorial equation of the form:
$$\mathcal{G}_{\mu\nu} = \kappa T_{\mu\nu}$$
where $\mathcal{G}_{\mu\nu}$ is a symmetric rank-2 geometric tensor constructed from the metric $g_{\mu\nu}$ and its first and second derivatives.

#### Essential Constraints:
1. Since energy-momentum is conserved ($\nabla^\mu T_{\mu\nu} = 0$), the geometric tensor must satisfy the divergence-free identity:
   $$\nabla^\mu \mathcal{G}_{\mu\nu} = 0$$
2. In 1915, David Hilbert and Albert Einstein proved that the unique symmetric tensor containing at most second derivatives of the metric that satisfies this condition (Lovelock's theorem in 4D) is:
   $$\mathcal{G}_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = G_{\mu\nu} + \Lambda g_{\mu\nu}$$

---

### 2. The Einstein Field Equations

> **Definition 8.2 (The Einstein Field Equations):**
> $$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$
> where:
> - $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$ is the Einstein tensor.
> - $\Lambda$ is the cosmological constant.
> - $G = 6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$ is Newton's gravitational constant.
> - $c$ is the speed of light.
> - $\kappa = \frac{8\pi G}{c^4} \approx 2.076 \times 10^{-43} \, \text{N}^{-1}$ is Einstein's gravitational coupling constant.

---

### 3. Trace-Reversed Form and Vacuum Equations
Taking the trace with $g^{\mu\nu}$:
$$g^{\mu\nu} G_{\mu\nu} + 4\Lambda = \kappa g^{\mu\nu} T_{\mu\nu} \implies -R + 4\Lambda = \kappa T \implies R = -\kappa T + 4\Lambda$$
Substituting back into $G_{\mu\nu}$:
$$R_{\mu\nu} = \frac{8\pi G}{c^4} \left( T_{\mu\nu} - \frac{1}{2} T g_{\mu\nu} \right) + \Lambda g_{\mu\nu}$$

#### Vacuum Field Equations ($\Lambda = 0, T_{\mu\nu} = 0$):
In empty spacetime outside mass distributions:
$$R_{\mu\nu} = 0$$
Spacetimes satisfying $R_{\mu\nu} = 0$ are called **Ricci-flat**.
Crucially, $R_{\mu\nu} = 0$ does NOT imply flat spacetime! The full Riemann tensor $R^\rho_{\mu\sigma\nu}$ can still be non-zero through its Weyl tensor component, propagating **gravitational waves** and mediating gravitational attraction!"""
            },
            {
                "secNumber": "8.5",
                "title": "The Schwarzschild Metric, Planetary Perihelion Precession & Gravitational Deflection",
                "content": r"""### 1. The Schwarzschild Solution (1916)
Karl Schwarzschild derived the exact vacuum solution ($R_{\mu\nu} = 0$) for a static, spherically symmetric mass $M$:

> **Definition 8.3 (Schwarzschild Metric):**
> $$ds^2 = -\left( 1 - \frac{r_s}{r} \right) c^2 dt^2 + \left( 1 - \frac{r_s}{r} \right)^{-1} dr^2 + r^2 \left( d\theta^2 + \sin^2\theta \, d\phi^2 \right)$$
> where $r_s = \frac{2GM}{c^2}$ is the **Schwarzschild radius** (event horizon).
> For the Sun: $r_s \approx 2.95 \text{ km}$; for the Earth: $r_s \approx 8.87 \text{ mm}$.

---

### 2. Relativistic Planetary Orbits and Perihelion Precession
Consider motion confined to the equatorial plane $\theta = \frac{\pi}{2}$.
From the geodesic equations, energy per unit mass $E$ and angular momentum per unit mass $L$ are conserved:
$$\left( 1 - \frac{r_s}{r} \right) c \frac{dt}{d\tau} = \frac{E}{c}, \qquad r^2 \frac{d\phi}{d\tau} = L$$
Substituting into the metric $g_{\mu\nu} \dot{x}^\mu \dot{x}^\nu = -c^2$:
$$\frac{1}{2} \left(\frac{dr}{d\tau}\right)^2 + V_{\text{eff}}(r) = \frac{E^2 - c^4}{2c^2}$$
where the relativistic effective potential is:
$$V_{\text{eff}}(r) = -\frac{GM}{r} + \frac{L^2}{2r^2} - \frac{G M L^2}{c^2 r^3}$$
The third term $-\frac{GML^2}{c^2 r^3}$ is the general relativistic correction to Newtonian gravity.

Using $u = 1/r$, the orbital Binet equation becomes:
$$\frac{d^2 u}{d\phi^2} + u = \frac{GM}{L^2} + \frac{3GM}{c^2} u^2$$
By perturbation theory, an elliptical orbit precesses by an angle per revolution:
$$\Delta\phi = \frac{6\pi GM}{c^2 a (1 - e^2)}$$
For Mercury: $a = 5.79 \times 10^{10} \text{ m}, e = 0.2056$.
This yields $\Delta\phi = 42.98'' \text{ per century}$, matching the observed anomalous 43 arcseconds per century unexplained by Newtonian planetary perturbations!

---

### 3. Gravitational Deflection of Starlight
For null geodesics (photons, $ds^2 = 0$), the orbital equation with impact parameter $b$ gives:
$$\frac{d^2 u}{d\phi^2} + u = \frac{3GM}{c^2} u^2$$
Integrating the perturbation from $\phi = -\pi/2$ to $\pi/2$ for light grazing the Sun at radius $R$:

> **Deflection Angle Formula:**
> $$\delta\theta = \frac{4GM}{c^2 R_{\odot}}$$
> For the Sun ($M = M_\odot, R = R_\odot$):
> $$\delta\theta \approx 1.751'' \text{ (arcseconds)}$$
> Exactly twice the naive Newtonian corpuscular value ($0.875''$)! This famous prediction was confirmed by Arthur Eddington's 1919 solar eclipse expedition, providing historic observational confirmation of general relativity."""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 8.1: Relativistic Energy-Momentum Tensor of Dust and Energy Density",
                "statement": r"""Consider a pressureless cloud of non-interacting particles ('dust') in spacetime with proper mass density $\rho_0$ and 4-velocity field $u^\mu = \frac{dx^\mu}{d\tau}$.
Its stress-energy tensor is given by:
$$T^{\mu\nu} = \rho_0 u^\mu u^\nu$$

1. Verify that $T^{\mu\nu}$ is symmetric.
2. In the rest frame of the dust, where $u^\mu = (c, 0, 0, 0)$ in Minkowski spacetime $\eta_{\mu\nu} = \text{diag}(-1, 1, 1, 1)$, write down the matrix components of $T^{\mu\nu}$ and $T^\mu_\nu$.
3. Compute the scalar trace $T = g_{\mu\nu} T^{\mu\nu}$.
4. Show that the conservation law $\nabla_\mu T^{\mu\nu} = 0$ decomposes into the continuity equation $\nabla_\mu (\rho_0 u^\mu) = 0$ and the geodesic equation $u^\mu \nabla_\mu u^\nu = 0$.""",
                "hints": [
                    "Recall $u^\\mu u_\\mu = -c^2$.",
                    "Expand $\\nabla_\\mu (\\rho_0 u^\\mu u^\\nu) = [\\nabla_\\mu (\\rho_0 u^\\mu)] u^\\nu + \\rho_0 u^\\mu \\nabla_\\mu u^\\nu$.",
                    "Contract with $u_\\nu$ and note $u_\\nu u^\\mu \\nabla_\\mu u^\\nu = \\frac{1}{2} u^\\mu \\nabla_\\mu (u^\\nu u_\\nu) = 0$."
                ],
                "solution": r"""### 1. Symmetry
$$T^{\nu\mu} = \rho_0 u^\nu u^\mu = \rho_0 u^\mu u^\nu = T^{\mu\nu}$$
Symmetric by definition. $\blacksquare$

---

### 2. Matrix Components in Rest Frame
With $u^\mu = (c, 0, 0, 0)$:
$$T^{00} = \rho_0 c^2, \qquad T^{0i} = T^{i0} = T^{ij} = 0$$
$$(T^{\mu\nu}) = \begin{pmatrix} \rho_0 c^2 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
Lowering the second index with $\eta_{\nu\lambda} = \text{diag}(-1, 1, 1, 1)$:
$$T^0_0 = \eta_{00} T^{00} = -1(\rho_0 c^2) = -\rho_0 c^2$$
$$(T^\mu_\nu) = \begin{pmatrix} -\rho_0 c^2 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \qquad \blacksquare$$

---

### 3. Trace $T$
$$T = T^\mu_\mu = g_{\mu\nu} T^{\mu\nu} = \rho_0 (g_{\mu\nu} u^\mu u^\nu) = \rho_0 (-c^2) = -\rho_0 c^2 \qquad \blacksquare$$

---

### 4. Decomposition of Conservation Law
Expand $\nabla_\mu T^{\mu\nu} = 0$:
$$\nabla_\mu (\rho_0 u^\mu u^\nu) = \left[ \nabla_\mu (\rho_0 u^\mu) \right] u^\nu + \rho_0 u^\mu \nabla_\mu u^\nu = 0$$
Contract this equation with the 4-velocity covector $u_\nu$:
$$\left[ \nabla_\mu (\rho_0 u^\mu) \right] (u^\nu u_\nu) + \rho_0 u^\mu (u_\nu \nabla_\mu u^\nu) = 0$$
Since $u^\nu u_\nu = -c^2 = \text{const}$:
$$u_\nu \nabla_\mu u^\nu = \frac{1}{2} \nabla_\mu (u_\nu u^\nu) = \frac{1}{2} \nabla_\mu (-c^2) = 0$$
Thus, the second term vanishes identically:
$$\left[ \nabla_\mu (\rho_0 u^\mu) \right] (-c^2) + 0 = 0 \implies \nabla_\mu (\rho_0 u^\mu) = 0$$
This is the **relativistic mass-continuity equation** (conservation of particle number).

Now substitute $\nabla_\mu (\rho_0 u^\mu) = 0$ back into the original conservation equation:
$$0 \cdot u^\nu + \rho_0 u^\mu \nabla_\mu u^\nu = 0 \implies u^\mu \nabla_\mu u^\nu = 0$$
This is the **geodesic equation** for the dust worldlines $\frac{D u^\nu}{d\tau} = 0$!
Energy-momentum conservation automatically forces pressureless dust particles to follow spacetime geodesics! $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 8.2: Electromagnetic Energy-Momentum Tensor and Trace-Free Property",
                "statement": r"""The electromagnetic stress-energy tensor in 4D spacetime is defined as:
$$T^{\mu\nu}_{\text{EM}} = \frac{1}{\mu_0} \left( F^{\mu\alpha} F^\nu_{\ \alpha} - \frac{1}{4} g^{\mu\nu} F_{\alpha\beta} F^{\alpha\beta} \right)$$

1. Prove that $T^{\mu\nu}_{\text{EM}}$ is strictly symmetric.
2. Prove that in $n = 4$ spacetime dimensions, the trace of $T^{\mu\nu}_{\text{EM}}$ vanishes identically: $T = g_{\mu\nu} T^{\mu\nu}_{\text{EM}} = 0$.
3. Use Maxwell's equations $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ and $\nabla_{[\lambda} F_{\mu\nu]} = 0$ to calculate $\nabla_\mu T^{\mu\nu}_{\text{EM}}$ and show that $\nabla_\mu T^{\mu\nu}_{\text{EM}} = -F^{\nu\alpha} J_\alpha$.
4. What physical principle does $\nabla_\mu (T^{\mu\nu}_{\text{matter}} + T^{\mu\nu}_{\text{EM}}) = 0$ express?""",
                "hints": [
                    "For symmetry, note $F^{\\mu\\alpha} F^\\nu_{\\ \\alpha} = g^{\\alpha\\beta} F^{\\mu\\alpha} F^\\nu_\\beta$.",
                    "For trace, note $g_{\\mu\\nu} g^{\\mu\\nu} = n = 4$.",
                    "The right side $-F^{\\nu\\alpha} J_\\alpha$ is the Lorentz force density with opposite sign."
                ],
                "solution": r"""### 1. Proof of Symmetry
$$F^{\mu\alpha} F^\nu_{\ \alpha} = F^{\mu\alpha} g_{\alpha\beta} F^{\nu\beta} = g_{\alpha\beta} F^{\mu\alpha} F^{\nu\beta}$$
Using antisymmetry $F^{\mu\alpha} = -F^{\alpha\mu}$ and $F^{\nu\beta} = -F^{\beta\nu}$:
$$g_{\alpha\beta} (-F^{\alpha\mu})(-F^{\beta\nu}) = g_{\alpha\beta} F^{\alpha\mu} F^{\beta\nu} = F^\beta_{\ \mu} F^{\nu\beta} = F^{\nu\beta} F_{\mu\beta} = F^{\nu\alpha} F^\mu_{\ \alpha}$$
Thus $T^{\mu\nu}_{\text{EM}} = T^{\nu\mu}_{\text{EM}}$. $\blacksquare$

---

### 2. Trace-Free Property in 4 Dimensions
$$T = g_{\mu\nu} T^{\mu\nu}_{\text{EM}} = \frac{1}{\mu_0} \left( g_{\mu\nu} F^{\mu\alpha} F^\nu_{\ \alpha} - \frac{1}{4} g_{\mu\nu} g^{\mu\nu} F_{\alpha\beta} F^{\alpha\beta} \right)$$
Evaluate each term:
- $g_{\mu\nu} F^{\mu\alpha} F^\nu_{\ \alpha} = F_\nu^{\ \alpha} F^\nu_{\ \alpha} = F^{\alpha\nu} F_{\alpha\nu} = F_{\alpha\beta} F^{\alpha\beta}$.
- In 4D, $g_{\mu\nu} g^{\mu\nu} = \delta^\mu_\mu = 4$.
Substituting:
$$T = \frac{1}{\mu_0} \left( F_{\alpha\beta} F^{\alpha\beta} - \frac{1}{4}(4) F_{\alpha\beta} F^{\alpha\beta} \right) = \frac{1}{\mu_0} \left( F_{\alpha\beta} F^{\alpha\beta} - F_{\alpha\beta} F^{\alpha\beta} \right) = 0 \qquad \blacksquare$$
Because $T \equiv 0$, pure radiation has zero gravitational trace, meaning $R = 0$ in the presence of electromagnetic fields!

---

### 3. Covariant Divergence
$$\nabla_\mu T^{\mu\nu}_{\text{EM}} = \frac{1}{\mu_0} \left[ (\nabla_\mu F^{\mu\alpha}) F^\nu_{\ \alpha} + F^{\mu\alpha} \nabla_\mu F^\nu_{\ \alpha} - \frac{1}{4} g^{\mu\nu} \nabla_\mu (F_{\alpha\beta} F^{\alpha\beta}) \right]$$
Using $\nabla_\mu F^{\mu\alpha} = \mu_0 J^\alpha$:
$$\frac{1}{\mu_0} (\mu_0 J^\alpha) F^\nu_{\ \alpha} = F^\nu_{\ \alpha} J^\alpha = -F^{\nu\alpha} J_\alpha = -f^\nu_{\text{Lorentz}}$$
The remaining terms cancel by the homogeneous Maxwell equation $\nabla_{[\mu} F_{\alpha\beta]} = 0$:
$$F^{\mu\alpha} \nabla_\mu F^\nu_{\ \alpha} - \frac{1}{2} F^{\alpha\beta} \nabla^\nu F_{\alpha\beta} = 0$$
Therefore:
$$\nabla_\mu T^{\mu\nu}_{\text{EM}} = -F^{\nu\alpha} J_\alpha \qquad \blacksquare$$

---

### 4. Physical Conservation Principle
Since $\nabla_\mu T^{\mu\nu}_{\text{matter}} = +F^{\nu\alpha} J_\alpha$ (Lorentz force acting on matter):
$$\nabla_\mu \left( T^{\mu\nu}_{\text{matter}} + T^{\mu\nu}_{\text{EM}} \right) = F^{\nu\alpha} J_\alpha - F^{\nu\alpha} J_\alpha = 0$$
This expresses **total energy-momentum conservation**: whatever energy and momentum the electromagnetic field loses is transferred into kinetic energy and momentum of the charged matter! $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 8.3: Derivation of the Schwarzschild Metric from Vacuum Einstein Equations",
                "statement": r"""Consider a general static, spherically symmetric spacetime metric in spherical coordinates $(t, r, \theta, \phi) = (x^0, x^1, x^2, x^3)$:
$$ds^2 = -e^{2\Phi(r)} c^2 dt^2 + e^{2\Lambda(r)} dr^2 + r^2 (d\theta^2 + \sin^2\theta \, d\phi^2)$$
where $\Phi(r)$ and $\Lambda(r)$ are unknown radial metric functions.

1. Compute the non-zero Christoffel symbols $\Gamma^\lambda_{\mu\nu}$ for this metric.
2. Compute the Ricci tensor components $R_{00}$, $R_{11}$, and $R_{22}$.
3. Impose the vacuum Einstein field equations $R_{\mu\nu} = 0$:
   - Combine $R_{00}$ and $R_{11}$ to show that $\Phi'(r) + \Lambda'(r) = 0 \implies \Phi(r) = -\Lambda(r) + \text{const}$.
   - Use $R_{22} = 0$ to solve for $e^{-2\Lambda(r)}$.
4. Determine the integration constant from the Newtonian weak-field limit and arrive at the exact Schwarzschild metric.""",
                "hints": [
                    "Non-zero metric components: $g_{00} = -c^2 e^{2\\Phi}$, $g_{11} = e^{2\\Lambda}$, $g_{22} = r^2$, $g_{33} = r^2 \\sin^2\\theta$.",
                    "Form the combination $e^{-2\\Phi} R_{00} + c^2 e^{-2\\Lambda} R_{11} = \\frac{2}{r} (\\Phi' + \\Lambda') = 0$.",
                    "Boundary condition at $r \\to \\infty$: $\\Phi, \\Lambda \\to 0$ (asymptotic flatness)."
                ],
                "solution": r"""### 1. Christoffel Symbols
Using $\Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\sigma} (\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu})$:
- $\Gamma^0_{01} = \Phi'$, $\Gamma^1_{00} = c^2 \Phi' e^{2(\Phi - \Lambda)}$
- $\Gamma^1_{11} = \Lambda'$, $\Gamma^1_{22} = -r e^{-2\Lambda}$, $\Gamma^1_{33} = -r \sin^2\theta e^{-2\Lambda}$
- $\Gamma^2_{12} = \frac{1}{r}$, $\Gamma^2_{33} = -\sin\theta\cos\theta$
- $\Gamma^3_{13} = \frac{1}{r}$, $\Gamma^3_{23} = \cot\theta$

---

### 2. Ricci Tensor Components
Evaluating $R_{\mu\nu} = \partial_\lambda \Gamma^\lambda_{\mu\nu} - \partial_\nu \Gamma^\lambda_{\mu\lambda} + \Gamma^\lambda_{\mu\nu} \Gamma^\sigma_{\lambda\sigma} - \Gamma^\lambda_{\mu\sigma} \Gamma^\sigma_{\nu\lambda}$:
$$\begin{aligned}
R_{00} &= c^2 e^{2(\Phi - \Lambda)} \left[ \Phi'' + (\Phi')^2 - \Phi' \Lambda' + \frac{2}{r} \Phi' \right] \\
R_{11} &= -\left[ \Phi'' + (\Phi')^2 - \Phi' \Lambda' - \frac{2}{r} \Lambda' \right] \\
R_{22} &= e^{-2\Lambda} \left[ r(\Lambda' - \Phi') - 1 \right] + 1 \\
R_{33} &= R_{22} \sin^2\theta
\end{aligned}$$

---

### 3. Vacuum Field Equations $R_{\mu\nu} = 0$

#### Step A: Sum of $R_{00}$ and $R_{11}$
Consider the linear combination:
$$\frac{e^{-2(\Phi - \Lambda)}}{c^2} R_{00} + R_{11} = \left[ \Phi'' + (\Phi')^2 - \Phi'\Lambda' + \frac{2}{r}\Phi' \right] - \left[ \Phi'' + (\Phi')^2 - \Phi'\Lambda' - \frac{2}{r}\Lambda' \right]$$
$$\frac{e^{-2(\Phi - \Lambda)}}{c^2} R_{00} + R_{11} = \frac{2}{r} (\Phi' + \Lambda') = 0$$
Since $r \ne 0$:
$$\Phi'(r) + \Lambda'(r) = 0 \implies \Phi(r) + \Lambda(r) = C_0$$
As $r \to \infty$, spacetime must be flat Minkowski space: $\Phi(\infty) = 0$ and $\Lambda(\infty) = 0 \implies C_0 = 0$.
Thus:
$$\Phi(r) = -\Lambda(r) \implies e^{2\Phi} = e^{-2\Lambda}$$

#### Step B: Solve $R_{22} = 0$
Substituting $\Phi' = -\Lambda'$ into $R_{22}$:
$$R_{22} = e^{-2\Lambda} [ r(2\Lambda') - 1 ] + 1 = 0$$
Notice that:
$$\frac{d}{dr}\left( r e^{-2\Lambda} \right) = e^{-2\Lambda} - 2 r \Lambda' e^{-2\Lambda} = - \left( e^{-2\Lambda} [ 2 r \Lambda' - 1 ] \right)$$
Therefore, $R_{22} = 0$ is equivalent to:
$$1 - \frac{d}{dr}\left( r e^{-2\Lambda} \right) = 0 \implies \frac{d}{dr}\left( r e^{-2\Lambda} \right) = 1$$
Integrating with respect to $r$:
$$r e^{-2\Lambda} = r - r_s \implies e^{-2\Lambda(r)} = 1 - \frac{r_s}{r}$$
where $r_s$ is a constant of integration.
Since $e^{2\Phi} = e^{-2\Lambda}$:
$$e^{2\Phi(r)} = 1 - \frac{r_s}{r}$$

---

### 4. Determination of Integration Constant $r_s$
At large distances $r \gg r_s$, the Newtonian limit requires:
$$g_{00} = -c^2 e^{2\Phi} \approx -c^2 \left( 1 + \frac{2\Phi_{\text{Newton}}}{c^2} \right) = -c^2 \left( 1 - \frac{2GM}{c^2 r} \right)$$
Comparing with $e^{2\Phi} = 1 - \frac{r_s}{r}$:
$$r_s = \frac{2GM}{c^2}$$
Substituting back into the line element:
$$ds^2 = -\left( 1 - \frac{2GM}{c^2 r} \right) c^2 dt^2 + \left( 1 - \frac{2GM}{c^2 r} \right)^{-1} dr^2 + r^2 \left( d\theta^2 + \sin^2\theta \, d\phi^2 \right)$$
This completes the exact, closed-form derivation of the **Schwarzschild Metric**! $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u8 = get_unit8()
    print(f"Loaded Unit 8: {u8['title']} with {len(u8['sections'])} sections and {len(u8['problems'])} problems.")
