# -*- coding: utf-8 -*-
# Unit 4: Potentials, Fields and Radiation

UNIT_4 = {
    "id": "unit-4",
    "number": 4,
    "title": "Electrodynamic Potentials, Gauge Freedom & Radiation",
    "leadSummary": "Comprehensive mathematical formulation of relativistic electrodynamics and radiation theory: vector potential A and scalar potential V, gauge transformations and degrees of freedom, Coulomb versus Lorentz gauge conditions, retarded Green's functions, causal retarded potentials, Liénard-Wiechert potentials for relativistic moving charges, electric and magnetic fields of accelerated charges (velocity vs acceleration terms), complete step-by-step vector derivation of oscillating Hertzian electric dipole radiation, far-field Poynting flux, the Larmor dipole power formula, radiation resistance, magnetic dipole radiation, and half-wave center-fed antenna theory.",
    "simulations": ["dipole-radiation"],
    "sections": [
        {
            "secNumber": "4.1",
            "heading": "Electromagnetic Potentials (V, A) and Field Formulations",
            "content": """
#### Definition of Potentials in Time-Dependent Electrodynamics
In static electromagnetism, $\\nabla \\times \\mathbf{E} = 0$ allows us to express the electric field as the gradient of a scalar potential, $\\mathbf{E} = -\\nabla V$. In dynamic electrodynamics, however, Faraday's law states:
$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$
Because $\\nabla \\times \\mathbf{E} \\neq 0$, $\\mathbf{E}$ cannot be written as the gradient of a scalar alone.

However, Gauss's law for magnetism remains strictly valid:
$$\\nabla \\cdot \\mathbf{B} = 0$$
Since the divergence of any curl vanishes identically ($\\nabla \\cdot (\\nabla \\times \\mathbf{A}) \\equiv 0$), we can always define the **magnetic vector potential** $\\mathbf{A}$:
$$\\mathbf{B} \\equiv \\nabla \\times \\mathbf{A}$$

Substitute this definition into Faraday's law:
$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{A}) = -\\nabla \\times \\left( \\frac{\\partial \\mathbf{A}}{\\partial t} \\right)$$
$$\\nabla \\times \\left( \\mathbf{E} + \\frac{\\partial \\mathbf{A}}{\\partial t} \\right) = 0$$

Because the quantity in parentheses has zero curl, it can now be expressed as the negative gradient of a dynamic **electric scalar potential** $V$:
$$\\mathbf{E} + \\frac{\\partial \\mathbf{A}}{\\partial t} = -\\nabla V \\implies \\mathbf{E} = -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t}$$

These two equations represent the fundamental relations expressing physical fields $(\\mathbf{E}, \\mathbf{B})$ in terms of electromagnetic potentials $(V, \\mathbf{A})$:
$$\\mathbf{B} = \\nabla \\times \\mathbf{A}$$
$$\\mathbf{E} = -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t}$$
"""
        },
        {
            "secNumber": "4.2",
            "heading": "Gauge Invariance: Coulomb Gauge and Lorentz Gauge Conditions",
            "content": """
#### Gauge Transformations
Potentials are not directly observable physical quantities; only fields $\\mathbf{E}$ and $\\mathbf{B}$ exert measurable Lorentz forces. If we modify $\\mathbf{A}$ and $V$ through a transformation involving an arbitrary scalar gauge function $\\lambda(\\mathbf{r}, t)$:
$$\\mathbf{A}' = \\mathbf{A} + \\nabla \\lambda$$
$$V' = V - \\frac{\\partial \\lambda}{\\partial t}$$

Let us compute the new fields:
$$\\mathbf{B}' = \\nabla \\times \\mathbf{A}' = \\nabla \\times (\\mathbf{A} + \\nabla \\lambda) = \\nabla \\times \\mathbf{A} + 0 = \\mathbf{B}$$
$$\\mathbf{E}' = -\\nabla V' - \\frac{\\partial \\mathbf{A}'}{\\partial t} = -\\nabla \\left( V - \\frac{\\partial \\lambda}{\\partial t} \\right) - \\frac{\\partial}{\\partial t} (\\mathbf{A} + \\nabla \\lambda) = -\\nabla V + \\nabla \\frac{\\partial \\lambda}{\\partial t} - \\frac{\\partial \\mathbf{A}}{\\partial t} - \\frac{\\partial \\nabla \\lambda}{\\partial t} = \\mathbf{E}$$

The physical fields are completely invariant under this **gauge transformation**. This mathematical freedom (gauge freedom) allows us to impose convenient constraints on the divergence of $\\mathbf{A}$.

#### 1. The Coulomb Gauge (Radiation Gauge)
Set the constraint:
$$\\nabla \\cdot \\mathbf{A} = 0$$
Substituting into Gauss's law $\\nabla \\cdot \\mathbf{E} = \\rho / \\epsilon_0$:
$$\\nabla \\cdot \\left( -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t} \\right) = -\\nabla^2 V - \\frac{\\partial}{\\partial t}(\\nabla \\cdot \\mathbf{A}) = \\frac{\\rho}{\\epsilon_0}$$
Since $\\nabla \\cdot \\mathbf{A} = 0$:
$$\\nabla^2 V = -\\frac{\\rho}{\\epsilon_0}$$
This is the standard Poisson equation. The scalar potential in Coulomb gauge is:
$$V(\\mathbf{r}, t) = \\frac{1}{4\\pi \\epsilon_0} \\int \\frac{\\rho(\\mathbf{r}', t)}{|\\mathbf{r} - \\mathbf{r}'|} \\, d\\tau'$$
While computationally convenient in quantum electrodynamics and atomic physics, $V$ in Coulomb gauge appears to propagate instantaneously, disguising relativistic causality.

#### 2. The Lorentz Gauge Condition
To preserve manifest relativistic covariance and causality, Ludvig Lorenz (and later Hendrik Lorentz) introduced the condition:
$$\\nabla \\cdot \\mathbf{A} + \\frac{1}{c^2} \\frac{\\partial V}{\\partial t} = 0$$

Substitute $(V, \\mathbf{A})$ into the inhomogeneous Maxwell equations (Gauss's law and Ampère-Maxwell law). Both coupled equations decouple completely into symmetric 4D **inhomogeneous d'Alembertian wave equations**:
$$\\nabla^2 V - \\frac{1}{c^2} \\frac{\\partial^2 V}{\\partial t^2} = -\\frac{\\rho}{\\epsilon_0} \\quad \\iff \\quad \\Box V = -\\frac{\\rho}{\\epsilon_0}$$
$$\\nabla^2 \\mathbf{A} - \\frac{1}{c^2} \\frac{\\partial^2 \\mathbf{A}}{\\partial t^2} = -\\mu_0 \\mathbf{J} \\quad \\iff \\quad \\Box \\mathbf{A} = -\\mu_0 \\mathbf{J}$$
where $\\Box \\equiv \\nabla^2 - \\frac{1}{c^2}\\frac{\\partial^2}{\\partial t^2}$ is the d'Alembertian operator.
"""
        },
        {
            "secNumber": "4.3",
            "heading": "Retarded Potentials and Causal Green's Function Solutions",
            "content": """
#### The Retardation Principle
Because electromagnetic signals propagate through space at the finite speed of light $c$, the potential at an observation point $\\mathbf{r}$ at time $t$ cannot depend on what source charges and currents are doing *at that exact moment*. Instead, it depends on their behavior at an earlier time $t_r$ (the **retarded time**), accounting for the travel time of light:
$$t_r \\equiv t - \\frac{|\\mathbf{r} - \\mathbf{r}'|}{c} = t - \\frac{\\imath}{c}$$
where $\\boldsymbol{\\imath} = \\mathbf{r} - \\mathbf{r}'$ is the separation vector and $\\imath = |\\mathbf{r} - \\mathbf{r}'|$.

Using the retarded Green's function of the d'Alembertian operator:
$$G(\\mathbf{r}, t; \\mathbf{r}', t') = \\frac{\\delta(t - t' - \\imath/c)}{4\\pi \\imath}$$

The exact solutions to the decoupled wave equations in Lorentz gauge are the **Retarded Potentials**:
$$V(\\mathbf{r}, t) = \\frac{1}{4\\pi \\epsilon_0} \\int \\frac{\\rho(\\mathbf{r}', t_r)}{\\imath} \\, d\\tau' = \\frac{1}{4\\pi \\epsilon_0} \\int \\frac{\\rho(\\mathbf{r}', t - \\imath/c)}{|\\mathbf{r} - \\mathbf{r}'|} \\, d\\tau'$$
$$\\mathbf{A}(\\mathbf{r}, t) = \\frac{\\mu_0}{4\\pi} \\int \\frac{\\mathbf{J}(\\mathbf{r}', t_r)}{\\imath} \\, d\\tau' = \\frac{\\mu_0}{4\\pi} \\int \\frac{\\mathbf{J}(\\mathbf{r}', t - \\imath/c)}{|\\mathbf{r} - \\mathbf{r}'|} \\, d\\tau'$$

These equations encapsulate relativistic causality: an event at the source point $\\mathbf{r}'$ can only affect the field point $\\mathbf{r}$ after the light-cone delay $\\Delta t = \\imath/c$ has elapsed.
"""
        },
        {
            "secNumber": "4.4",
            "heading": "Liénard-Wiechert Potentials for a Relativistic Moving Point Charge",
            "content": """
#### Potentials of a Point Charge on an Arbitrary Trajectory
Consider a point charge $q$ moving along an arbitrary trajectory $\\mathbf{w}(t)$ with velocity $\\mathbf{v}(t) = \\dot{\\mathbf{w}}(t)$. Because the charge is moving, different parts of the charge distribution during an integration volume emit signals that arrive at observation point $\\mathbf{r}$ at the same time $t$. This geometric elongation introduces a Doppler-like Jacobian volume factor:
$$d\\tau' = \\frac{d\\tau}{1 - \\hat{\\boldsymbol{\\imath}} \\cdot \\boldsymbol{\\beta}}$$
where $\\boldsymbol{\\beta} = \\frac{\\mathbf{v}}{c}$ and $\\hat{\\boldsymbol{\\imath}} = \\frac{\\mathbf{r} - \\mathbf{w}(t_r)}{|\\mathbf{r} - \\mathbf{w}(t_r)|}$.

Carrying out the 4D delta-function integral yields the celebrated **Liénard-Wiechert Potentials** (Alfred-Marie Liénard 1898, Emil Wiechert 1900):
$$V(\\mathbf{r}, t) = \\frac{1}{4\\pi \\epsilon_0} \\frac{q}{\\imath - \\frac{\\boldsymbol{\\imath} \\cdot \\mathbf{v}}{c}} = \\frac{1}{4\\pi \\epsilon_0} \\frac{q}{\\imath (1 - \\hat{\\boldsymbol{\\imath}} \\cdot \\boldsymbol{\\beta})}$$
$$\\mathbf{A}(\\mathbf{r}, t) = \\frac{\\mu_0}{4\\pi} \\frac{q \\mathbf{v}}{\\imath - \\frac{\\boldsymbol{\\imath} \\cdot \\mathbf{v}}{c}} = \\frac{\\mathbf{v}}{c^2} V(\\mathbf{r}, t)$$
where all source quantities $(\\mathbf{w}, \\mathbf{v}, \\boldsymbol{\\beta}, \\imath)$ are evaluated at the retarded time $t_r$ satisfying $c(t - t_r) = |\\mathbf{r} - \\mathbf{w}(t_r)|$.
"""
        },
        {
            "secNumber": "4.5",
            "heading": "Electric and Magnetic Fields of Accelerated Charges (Velocity vs Radiation Fields)",
            "content": """
#### Computing the Fields from Liénard-Wiechert Potentials
Differentiating the potentials $\\mathbf{E} = -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t}$ and $\\mathbf{B} = \\nabla \\times \\mathbf{A}$ requires taking gradients and time derivatives through the implicit dependence on retarded time $\\nabla t_r = -\\frac{\\hat{\\boldsymbol{\\imath}}}{c(1 - \\hat{\\boldsymbol{\\imath}} \\cdot \\boldsymbol{\\beta})}$.

The resulting electric field separates into two distinct physical terms:
$$\\mathbf{E}(\\mathbf{r}, t) = \\mathbf{E}_{\\text{velocity}} + \\mathbf{E}_{\\text{acceleration}}$$
$$\\mathbf{E}(\\mathbf{r}, t) = \\frac{q}{4\\pi \\epsilon_0} \\frac{\\imath}{(\\boldsymbol{\\imath} \\cdot \\mathbf{u})^3} \\left[ (c^2 - v^2) \\mathbf{u} + \\boldsymbol{\\imath} \\times (\\mathbf{u} \\times \\mathbf{a}) \\right]$$
where $\\mathbf{u} \\equiv c \\hat{\\boldsymbol{\\imath}} - \\mathbf{v}$ and $\\mathbf{a} = \\dot{\\mathbf{v}}(t_r)$ is the charge acceleration evaluated at retarded time.

The magnetic induction field is strictly orthogonal and transverse:
$$\\mathbf{B}(\\mathbf{r}, t) = \\frac{1}{c} \\left( \\hat{\\boldsymbol{\\imath}} \\times \\mathbf{E}(\\mathbf{r}, t) \\right)$$

#### Decomposition and Physical Significance
1. **The Velocity Field (Generalized Coulomb Field):**
$$\\mathbf{E}_{\\text{velocity}} \\propto \\frac{c^2 - v^2}{\\imath^2}$$
Decays as $1/\\imath^2$ with distance. It is carried along with the moving charge and represents bound field energy that cannot escape to infinity.

2. **The Acceleration Field (Radiation Field):**
$$\\mathbf{E}_{\\text{acceleration}} = \\frac{q}{4\\pi \\epsilon_0 c^2} \\frac{\\hat{\\boldsymbol{\\imath}} \\times (\\mathbf{u} \\times \\mathbf{a})}{(\\boldsymbol{\\imath} \\cdot \\mathbf{u})^3} \\propto \\frac{1}{\\imath}$$
Decays as $1/\\imath$ with distance! The associated Poynting energy flux scales as:
$$S \\propto E_{\\text{rad}}^2 \\propto \\frac{1}{\\imath^2}$$
When integrated over a giant sphere of radius $\\imath \\to \\infty$, the surface area $4\\pi \\imath^2$ cancels the $1/\\imath^2$ decay:
$$\\oint_{S_\\infty} \\mathbf{S} \\cdot d\\mathbf{a} = \\text{constant} \\neq 0$$

**Fundamental Theorem of Classical Electrodynamics:** A charge moving with uniform velocity ($a = 0$) does NOT radiate. **Only an accelerated charge ($a \\neq 0$) radiates electromagnetic energy to infinity.**
"""
        },
        {
            "secNumber": "4.6",
            "heading": "Electric Dipole Radiation (Oscillating Hertzian Dipole)",
            "content": """
#### The Oscillating Electric Dipole Model
Consider two tiny conducting spheres separated by a distance $d$ along the $z$-axis, connected by a thin filament carrying an alternating current. The electric dipole moment oscillates harmonically:
$$\\mathbf{p}(t) = p_0 \\cos(\\omega t) \\hat{\\mathbf{z}}$$
where $p_0 = q_0 d$.

We evaluate the fields under the standard **radiation zone approximations**:
1. Short dipole compared to wavelength: $d \\ll \\lambda$ (dipole approximation)
2. Far radiation field: $r \\gg \\lambda \\gg d$ where $\\lambda = 2\\pi c/\\omega$

#### Derivation of the Radiation Zone Fields
The retarded vector potential in spherical coordinates $(r, \\theta, \\phi)$ in the far zone is:
$$\\mathbf{A}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega}{4\\pi r} \\sin(\\omega(t - r/c)) \\hat{\\mathbf{z}}$$
Converting $\\hat{\\mathbf{z}} = \\cos\\theta \\hat{\\mathbf{r}} - \\sin\\theta \\hat{\\boldsymbol{\\theta}}$:
$$\\mathbf{A}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega}{4\\pi r} \\sin(\\omega(t - r/c)) (\\cos\\theta \\hat{\\mathbf{r}} - \\sin\\theta \\hat{\\boldsymbol{\\theta}})$$

Computing $\\mathbf{B} = \\nabla \\times \\mathbf{A}$ keeping only terms scaling as $1/r$:
$$\\mathbf{B}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega^2}{4\\pi c} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\phi}}$$

From $\\mathbf{E} = c(\\mathbf{B} \\times \\hat{\\mathbf{r}})$:
$$\\mathbf{E}(r, \\theta, t) = -\\frac{\\mu_0 p_0 \\omega^2}{4\\pi} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\theta}}$$

#### Key Physical Characteristics
1. **Transverse Wave:** $\\mathbf{E}$ points along $\\hat{\\boldsymbol{\\theta}}$, $\\mathbf{B}$ points along $\\hat{\\boldsymbol{\\phi}}$, and propagation is radially outward along $\\hat{\\mathbf{r}}$.
2. **Frequency Dependence:** Field amplitudes are proportional to $\\omega^2$ (or $1/\\lambda^2$). High frequencies radiate vastly more efficiently than low frequencies.
3. **Angular Profile:** Fields vanish along the dipole axis ($\\theta = 0, \\pi$) and peak in the equatorial plane ($\\theta = \\pi/2$).
"""
        },
        {
            "secNumber": "4.7",
            "heading": "Poynting Flux, Radiation Pattern, and the Larmor Power Formula",
            "content": """
#### Instantaneous and Time-Averaged Poynting Vector
The Poynting vector in the radiation zone is:
$$\\mathbf{S}(r, \\theta, t) = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{\\mu_0 p_0^2 \\omega^4}{16\\pi^2 c} \\left( \\frac{\\sin^2\\theta}{r^2} \\right) \\cos^2(\\omega(t - r/c)) \\hat{\\mathbf{r}}$$

Taking the time average over an oscillation cycle ($\\langle \\cos^2 \\rangle = 1/2$):
$$\\langle \\mathbf{S} \\rangle = \\frac{\\mu_0 p_0^2 \\omega^4}{32\\pi^2 c} \\frac{\\sin^2\\theta}{r^2} \\hat{\\mathbf{r}}$$

#### The Toroidal Doughnut Radiation Pattern
The radiated intensity depends on angle as $\\sin^2\\theta$:
- **Broadside ($\\theta = 90^\\circ$):** Maximum radiation flux perpendicular to the dipole axis.
- **Endfire ($\\theta = 0^\\circ, 180^\\circ$):** Zero radiation along the axis of the antenna wire.

#### Total Radiated Power: Larmor's Formula for Dipoles
Integrating $\\langle \\mathbf{S} \\rangle$ over a closed sphere of radius $r$:
$$P = \\oint \\langle \\mathbf{S} \\rangle \\cdot d\\mathbf{a} = \\int_0^{2\\pi} d\\phi \\int_0^\\pi \\left( \\frac{\\mu_0 p_0^2 \\omega^4}{32\\pi^2 c} \\frac{\\sin^2\\theta}{r^2} \\right) r^2 \\sin\\theta \\, d\\theta$$
$$P = \\frac{\\mu_0 p_0^2 \\omega^4}{32\\pi^2 c} (2\\pi) \\int_0^\\pi \\sin^3\\theta \\, d\\theta$$

The standard integral is $\\int_0^\\pi \\sin^3\\theta \\, d\\theta = \\frac{4}{3}$:
$$P = \\frac{\\mu_0 p_0^2 \\omega^4}{16\\pi c} \\left( \\frac{4}{3} \\right) = \\frac{\\mu_0 p_0^2 \\omega^4}{12\\pi c}$$

In terms of the speed of light in vacuum ($c = 1/\\sqrt{\\epsilon_0 \\mu_0}$):
$$P = \\frac{p_0^2 \\omega^4}{12\\pi \\epsilon_0 c^3}$$

This is the celebrated **Larmor Formula for an Oscillating Dipole**. Notice the profound $\\omega^4$ frequency dependence: doubling the frequency increases the radiated power by a factor of $2^4 = 16$.

#### Radiation Resistance of a Short Dipole Antenna
The current feeding the dipole is $I(t) = \\dot{q}(t) = -q_0 \\omega \\sin(\\omega t)$, with amplitude $I_0 = q_0 \\omega$. Thus $p_0 = q_0 d = \\frac{I_0 d}{\\omega}$.
Substituting into the total power formula:
$$P = \\frac{\\mu_0 (I_0 d / \\omega)^2 \\omega^4}{12\\pi c} = \\frac{\\mu_0 I_0^2 d^2 \\omega^2}{12\\pi c} = \\frac{1}{2} I_0^2 R_{\\text{rad}}$$

Equating to the equivalent dissipated circuit power $P = \\frac{1}{2} I_0^2 R_{\\text{rad}}$:
$$R_{\\text{rad}} = \\frac{\\mu_0 d^2 \\omega^2}{6\\pi c} = \\frac{\\mu_0 c}{6\\pi} \\left( \\frac{\\omega d}{c} \\right)^2 = \\frac{120\\pi}{6\\pi} \\left( \\frac{2\\pi d}{\\lambda} \\right)^2 = 80\\pi^2 \\left( \\frac{d}{\\lambda} \\right)^2 \\, \\Omega$$

For a short dipole where $d \\ll \\lambda$ (e.g., $d = 0.05\\lambda$):
$$R_{\\text{rad}} = 80\\pi^2 (0.05)^2 \\approx 1.97 \\, \\Omega$$
Because radiation resistance is tiny, short antennas match poorly to standard $50\\,\\Omega$ RF lines, radiating inefficiently.
"""
        },
        {
            "secNumber": "4.8",
            "heading": "Magnetic Dipole Radiation and Center-Fed Half-Wave Antennas",
            "content": """
#### Magnetic Dipole Radiation
An oscillating circular loop of radius $b$ carrying alternating current $I(t) = I_0 \\cos(\\omega t)$ constitutes an oscillating magnetic dipole $\\mathbf{m}(t) = m_0 \\cos(\\omega t) \\hat{\\mathbf{z}}$, where $m_0 = \\pi b^2 I_0$.

The radiation zone fields are:
$$\\mathbf{E}(r, \\theta, t) = \\frac{\\mu_0 m_0 \\omega^2}{4\\pi c} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\phi}}$$
$$\\mathbf{B}(r, \\theta, t) = -\\frac{\\mu_0 m_0 \\omega^2}{4\\pi c^2} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\theta}}$$

The total radiated power is:
$$P_{\\text{mag}} = \\frac{\\mu_0 m_0^2 \\omega^4}{12\\pi c^3}$$

#### Comparison Between Electric and Magnetic Dipoles
For comparable geometric dimensions ($p_0 \\sim q d, m_0 \\sim I d^2 \\sim q \\omega d^2$):
$$\\frac{P_{\\text{mag}}}{P_{\\text{elec}}} = \\left( \\frac{\\omega d}{c} \\right)^2 = \\left( \\frac{2\\pi d}{\\lambda} \\right)^2 \\ll 1$$
Magnetic dipole radiation is suppressed by a factor of $(d/\\lambda)^2$ relative to electric dipole radiation. Electric dipole transitions (E1) are vastly stronger than magnetic dipole (M1) atomic transitions.

#### The Center-Fed Half-Wave Antenna ($L = \\lambda/2$)
Practical radio communications employ resonant antennas of length $L = \\lambda/2$. The current distribution is a standing wave that vanishes at the endpoints $z = \\pm L/2$:
$$I(z) = I_0 \\cos(kz) e^{-i\\omega t}$$
where $k = \\frac{2\\pi}{\\lambda} = \\frac{\\pi}{L}$.

Integrating across the antenna length yields the far-field radiation pattern:
$$\\langle \\mathbf{S} \\rangle = \\frac{\\eta_0 I_0^2}{8\\pi^2 r^2} \\left[ \\frac{\\cos\\left( \\frac{\\pi}{2}\\cos\\theta \\right)}{\\sin\\theta} \\right]^2 \\hat{\\mathbf{r}}$$

Integrating over a sphere gives the total power radiated:
$$P = \\frac{\\eta_0 I_0^2}{4\\pi} \\int_0^\\pi \\frac{\\cos^2\\left(\\frac{\\pi}{2}\\cos\\theta\\right)}{\\sin\\theta} \\, d\\theta = \\frac{120\\pi I_0^2}{4\\pi} (1.2188) = 36.56 I_0^2 = \\frac{1}{2} I_0^2 R_{\\text{rad}}$$

Solving for the radiation resistance of a resonant half-wave antenna:
$$R_{\\text{rad}} = 2 \\times 36.56 \\, \\Omega \\approx 73.13 \\, \\Omega$$

**Engineering Significance:** A radiation resistance of $73\\,\\Omega$ provides an outstanding impedance match to standard coaxial transmission cables ($50\\,\\Omega$ or $75\\,\\Omega$), making half-wave dipoles the universal cornerstone of modern telecommunications.
"""
        }
    ],
    "problems": [
        {
            "id": "p4-1",
            "title": "Example 4.1: Gauge Transformation Connecting Coulomb and Lorentz Gauges",
            "difficulty": "Medium",
            "question": "A vector potential in a region is given by $\\mathbf{A}_1 = A_0 \\cos(kz - \\omega t) \\hat{\\mathbf{x}}$ and $V_1 = 0$. (a) Determine whether this potential satisfies the Coulomb gauge condition. (b) Determine whether it satisfies the Lorentz gauge condition. (c) Construct a gauge function $\\lambda(\\mathbf{r}, t)$ that transforms $\\mathbf{A}_1$ into a new vector potential $\\mathbf{A}_2$ and scalar potential $V_2$ such that the Lorentz gauge condition is explicitly satisfied.",
            "steps": [
                {
                    "stepName": "Step 1: Check Coulomb Gauge Condition",
                    "math": "\\nabla \\cdot \\mathbf{A}_1 = \\frac{\\partial A_{1x}}{\\partial x} = \\frac{\\partial}{\\partial x}[A_0 \\cos(kz - \\omega t)] = 0",
                    "explanation": "Since $\\mathbf{A}_1$ points along $\\hat{\\mathbf{x}}$ and varies only with $z$, its spatial divergence is identically zero. Thus, $\\mathbf{A}_1$ satisfies the Coulomb gauge."
                },
                {
                    "stepName": "Step 2: Check Lorentz Gauge Condition",
                    "math": "\\nabla \\cdot \\mathbf{A}_1 + \\frac{1}{c^2}\\frac{\\partial V_1}{\\partial t} = 0 + 0 = 0",
                    "explanation": "Remarkably, because both $\\nabla \\cdot \\mathbf{A}_1 = 0$ and $\\frac{\\partial V_1}{\\partial t} = 0$, this specific potential simultaneously satisfies both the Coulomb and Lorentz gauge conditions (this is the transverse radiation gauge)."
                },
                {
                    "stepName": "Step 3: Verification of Physical Fields",
                    "math": "\\mathbf{B} = \\nabla \\times \\mathbf{A}_1 = \\left| \\begin{matrix} \\hat{\\mathbf{x}} & \\hat{\\mathbf{y}} & \\hat{\\mathbf{z}} \\\\ \\partial_x & \\partial_y & \\partial_z \\\\ A_0\\cos(kz-\\omega t) & 0 & 0 \\end{matrix} \\right| = k A_0 \\sin(kz - \\omega t) \\hat{\\mathbf{y}}\\n\\mathbf{E} = -\\nabla V_1 - \\frac{\\partial \\mathbf{A}_1}{\\partial t} = -\\omega A_0 \\sin(kz - \\omega t) \\hat{\\mathbf{x}}",
                    "explanation": "The ratio $|E|/|B| = \\omega / k = c$, correctly reproducing a propagating plane electromagnetic wave in vacuum."
                }
            ]
        },
        {
            "id": "p4-2",
            "title": "Example 4.2: Radiated Power and Radiation Resistance of a Short AM Radio Antenna",
            "difficulty": "Easy",
            "question": "A vertical short monopole antenna of height $h = 10.0\\text{ m}$ operates at an AM broadcasting frequency of $f = 1000\\text{ kHz}$ ($1.00\\text{ MHz}$). The antenna carries a peak base current of $I_0 = 15.0\\text{ A}$. Calculate: (a) the free-space wavelength $\\lambda$, (b) the effective radiation resistance $R_{\\text{rad}}$ of the antenna (modeled as a short monopole over a conducting ground plane, $R_{\\text{rad}} = 40\\pi^2 (h/\\lambda)^2$), (c) the total time-averaged radiated power $P_{\\text{rad}}$, and (d) the radiation efficiency if the ohmic ground loss resistance is $R_{\\text{loss}} = 2.50\\,\\Omega$.",
            "steps": [
                {
                    "stepName": "Step 1: Wavelength Calculation",
                    "math": "\\lambda = \\frac{c}{f} = \\frac{3.00 \\times 10^8\\text{ m/s}}{1.00 \\times 10^6\\text{ Hz}} = 300.0\\text{ m}",
                    "explanation": "The antenna height $h = 10\\text{ m}$ is $h/\\lambda = 10/300 = 1/30 \\ll 1$, so the short antenna approximation applies."
                },
                {
                    "stepName": "Step 2: Radiation Resistance Calculation",
                    "math": "R_{\\text{rad}} = 40\\pi^2 \\left( \\frac{h}{\\lambda} \\right)^2 = 40\\pi^2 \\left( \\frac{10}{300} \\right)^2 = 40\\pi^2 \\left( \\frac{1}{900} \\right) = \\frac{40(9.8696)}{900} = 0.4386\\,\\Omega \\approx 0.439\\,\\Omega",
                    "explanation": "The radiation resistance is only 0.44 Ohms."
                },
                {
                    "stepName": "Step 3: Total Radiated Power",
                    "math": "P_{\\text{rad}} = \\frac{1}{2} I_0^2 R_{\\text{rad}} = \\frac{1}{2} (15.0\\text{ A})^2 (0.4386\\,\\Omega) = \\frac{1}{2}(225)(0.4386) = 49.34\\text{ W}",
                    "explanation": "The antenna successfully broadcasts 49.3 watts of RF power into the air."
                },
                {
                    "stepName": "Step 4: Radiation Efficiency",
                    "math": "\\eta = \\frac{R_{\\text{rad}}}{R_{\\text{rad}} + R_{\\text{loss}}} = \\frac{0.4386}{0.4386 + 2.50} = \\frac{0.4386}{2.9386} = 0.1492 \\implies 14.9\\%",
                    "explanation": "Over 85% of transmitter power is wasted as heat in ground resistance because the antenna is physically much shorter than $\\lambda/4$ ($75\\text{ m}$)."
                }
            ]
        },
        {
            "id": "p4-3",
            "title": "Example 4.3: Bremsstrahlung Radiated Power from a Decelerating Relativistic Electron",
            "difficulty": "Hard",
            "question": "An electron ($q = -e = -1.602 \\times 10^{-19}\\text{ C}$, $m_e = 9.109 \\times 10^{-31}\\text{ kg}$) in an X-ray medical tube is accelerated by a potential difference $V = 100\\text{ kV}$. Upon hitting a tungsten anode target, it decelerates to a complete stop over a distance $\\Delta x = 2.0\\,\\mu\\text{m}$ under approximately uniform deceleration $a$. (a) Calculate the kinetic energy and deceleration $a$ of the electron. (b) Use Larmor's relativistic formula $P = \\frac{e^2 a^2 \\gamma^6}{6\\pi \\epsilon_0 c^3}$ (or non-relativistic $P = \\frac{e^2 a^2}{6\\pi \\epsilon_0 c^3}$) to calculate the peak radiated power. (c) Estimate the duration of the deceleration pulse $\\Delta t$ and total radiated energy.",
            "steps": [
                {
                    "stepName": "Step 1: Electron Velocity and Deceleration",
                    "math": "K = e V = (1.602 \\times 10^{-19}\\text{ C})(10^5\\text{ V}) = 1.602 \\times 10^{-14}\\text{ J} = 100\\text{ keV}\\nv_0 = \\sqrt{\\frac{2K}{m_e}} = \\sqrt{\\frac{2(1.602 \\times 10^{-14})}{9.109 \\times 10^{-31}}} = 1.875 \\times 10^8\\text{ m/s} = 0.625 \\, c\\na = \\frac{v_0^2}{2 \\Delta x} = \\frac{(1.875 \\times 10^8\\text{ m/s})^2}{2(2.0 \\times 10^{-6}\\text{ m})} = 8.79 \\times 10^{21}\\text{ m/s}^2",
                    "explanation": "The atomic collision produces a staggering deceleration of over $8.8 \\times 10^{21}\\text{ m/s}^2$."
                },
                {
                    "stepName": "Step 2: Radiated Power via Larmor Formula",
                    "math": "P = \\frac{e^2 a^2}{6\\pi \\epsilon_0 c^3} = \\frac{(1.602 \\times 10^{-19})^2 (8.79 \\times 10^{21})^2}{6\\pi (8.854 \\times 10^{-12}) (3.00 \\times 10^8)^3}\\nP = \\frac{(2.566 \\times 10^{-38})(7.726 \\times 10^{43})}{(1.669 \\times 10^{-10})(2.70 \\times 10^{25})} = \\frac{1.983 \\times 10^6}{4.506 \\times 10^{15}} = 4.40 \\times 10^{-10}\\text{ W}",
                    "explanation": "During the deceleration instant, a single microscopic electron emits 0.44 nanowatts of continuous X-ray photon radiation."
                },
                {
                    "stepName": "Step 3: Pulse Duration and Bremsstrahlung Emission",
                    "math": "\\Delta t = \\frac{v_0}{a} = \\frac{1.875 \\times 10^8\\text{ m/s}}{8.79 \\times 10^{21}\\text{ m/s}^2} = 2.13 \\times 10^{-14}\\text{ s} = 21.3\\text{ fs}\\nE_{\\text{rad}} = P \\times \\Delta t = (4.40 \\times 10^{-10}\\text{ W})(2.13 \\times 10^{-14}\\text{ s}) = 9.37 \\times 10^{-24}\\text{ J} \\approx 58.5\\text{ meV}",
                    "explanation": "The sudden deceleration creates an ultrashort femtosecond burst of continuous X-ray radiation (Bremsstrahlung, 'braking radiation')."
                }
            ]
        },
        {
            "id": "p4-4",
            "title": "Example 4.4: Input Current and Total Power Radiated by a Half-Wave Dipole Antenna",
            "difficulty": "Medium",
            "question": "A commercial FM broadcasting station transmits at $f = 100.0\\text{ MHz}$ using a resonant half-wave dipole antenna ($L = \\lambda/2$). The station transmitter delivers a total radiated RF power of $P_{\\text{rad}} = 50.0\\text{ kW}$. (a) Calculate the physical length $L$ of the antenna. (b) Using the half-wave radiation resistance $R_{\\text{rad}} = 73.13\\,\\Omega$, find the peak antenna feedpoint input current $I_0$. (c) Calculate the peak electric field amplitude $E_0$ detected by an FM radio receiver at a distance of $r = 25.0\\text{ km}$ in the broadside direction ($\\theta = 90^\\circ$).",
            "steps": [
                {
                    "stepName": "Step 1: Antenna Length Calculation",
                    "math": "\\lambda = \\frac{c}{f} = \\frac{3.00 \\times 10^8\\text{ m/s}}{1.00 \\times 10^8\\text{ Hz}} = 3.00\\text{ m}\\nL = \\frac{\\lambda}{2} = \\frac{3.00\\text{ m}}{2} = 1.50\\text{ m}",
                    "explanation": "The half-wave dipole is exactly 1.5 meters from tip to tip."
                },
                {
                    "stepName": "Step 2: Peak Input Current",
                    "math": "P_{\\text{rad}} = \\frac{1}{2} I_0^2 R_{\\text{rad}} \\implies I_0 = \\sqrt{\\frac{2 P_{\\text{rad}}}{R_{\\text{rad}}}}\\nI_0 = \\sqrt{\\frac{2(50,000\\text{ W})}{73.13\\,\\Omega}} = \\sqrt{1367.4} = 36.98\\text{ A}",
                    "explanation": "The peak current driving the center feedpoint is approximately 37 Amperes."
                },
                {
                    "stepName": "Step 3: Detected Electric Field at 25 km Distance",
                    "math": "\\text{Broadside (}\\theta = 90^\\circ\\text{): } \\langle S \\rangle = \\frac{\\eta_0 I_0^2}{8\\pi^2 r^2} \\left[ \\frac{\\cos(0)}{1} \\right]^2 = \\frac{(376.73)(36.98)^2}{8\\pi^2 (2.50 \\times 10^4\\text{ m})^2}\\n\\langle S \\rangle = \\frac{5.152 \\times 10^5}{4.935 \\times 10^{10}} = 1.044 \\times 10^{-5}\\text{ W/m}^2 = 10.44\\,\\mu\\text{W/m}^2\\nE_0 = \\sqrt{2 \\eta_0 \\langle S \\rangle} = \\sqrt{2(376.73)(1.044 \\times 10^{-5})} = \\sqrt{7.866 \\times 10^{-3}} = 0.0887\\text{ V/m} = 88.7\\text{ mV/m}",
                    "explanation": "A field strength of 88.7 millivolts per meter provides crystal-clear reception for automobile and mobile FM receivers."
                }
            ]
        }
    ]
}

print("Unit 4 built successfully. Sections:", len(UNIT_4["sections"]), "Problems:", len(UNIT_4["problems"]))
