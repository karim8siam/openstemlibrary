#!/usr/bin/env python3
"""
build_kinetics_units_1_2_3.py
Builds Units 1, 2, and 3 (Sections 1-7, Solved Problems 1-7) for Molecular Motion and Reaction Kinetics.
"""

import json

def get_units_1_2_3():
    units = []

    # =========================================================================
    # UNIT 1: Kinetic Theory of Gases & Gas Transport Phenomena
    # =========================================================================
    u1 = {
        "id": "unit-1",
        "unitNumber": 1,
        "title": "Unit 1: Kinetic Theory of Gases & Gas Transport Phenomena",
        "leadSummary": "Comprehensive statistical-mechanical and transport formulation of dilute gases: microscopic pressure derivation via momentum transfer, canonical Maxwell-Boltzmann velocity and speed distributions, characteristic velocity averages, molecular collision cross-sections, Knudsen effusion flux, and classical kinetic transport phenomena (viscosity, thermal conductivity, and gas self-diffusion).",
        "simulations": ["sim_kin_maxwell_boltzmann_effusion"],
        "sections": [
            {
                "id": "sec-1-1",
                "secNumber": "1.1",
                "title": "Kinetic Molecular Model of Gases: Microscopic Momentum Transfer & Pressure Derivation",
                "content": """The classical kinetic molecular theory of ideal gases establishes a direct, rigorous bridge between microscopic particle kinematics and macroscopic thermodynamic state variables. 

### Fundamental Postulates
1. **Point-Mass Particles**: The gas consists of an ensemble of $N$ identical molecules of mass $m$, occupying a container of volume $V$. The volume of the individual molecules is negligibly small compared to $V$.
2. **Elastic Collisions**: Intermolecular forces are negligible except during instantaneous, perfectly elastic collisions where total kinetic energy and linear momentum are conserved.
3. **Random Isotropic Motion**: Particles move continuously in straight-line trajectories governed by Newton's equations of motion, distributed isotropically in velocity space.

### Microscopic Derivation of Ideal Gas Pressure
Consider a cubical container of side length $L$ and volume $V = L^3$. Let a molecule possess Cartesian velocity components $(v_x, v_y, v_z)$. Upon colliding with an elastic planar wall perpendicular to the $x$-axis at $x = L$, the velocity component $v_x$ reverses to $-v_x$, while $v_y$ and $v_z$ remain unaltered.

The linear momentum transferred to the wall in a single collision event is:
$$\\Delta p_x = m v_x - (-m v_x) = 2 m v_x$$

The time elapsed between successive collisions of this molecule with the same wall is:
$$\\Delta t = \\frac{2L}{v_x}$$

The average microscopic force exerted by this single particle on the wall is given by Newton's second law:
$$f_{x, i} = \\frac{\\Delta p_x}{\\Delta t} = \\frac{2 m v_{x, i}^2}{2 L} = \\frac{m v_{x, i}^2}{L}$$

Summing over all $N$ molecules, the total force on the wall of area $A = L^2$ is:
$$F_x = \\sum_{i=1}^N f_{x, i} = \\frac{m}{L} \\sum_{i=1}^N v_{x, i}^2 = \\frac{m N}{L} \\langle v_x^2 \\rangle$$

The pressure $P$ exerted on the wall is:
$$P = \\frac{F_x}{A} = \\frac{m N}{L^3} \\langle v_x^2 \\rangle = \\frac{N m}{V} \\langle v_x^2 \\rangle$$

Because particle velocity is isotropic in three-dimensional space:
$$\\langle v^2 \\rangle = \\langle v_x^2 \\rangle + \\langle v_y^2 \\rangle + \\langle v_z^2 \\rangle = 3 \\langle v_x^2 \\rangle \\implies \\langle v_x^2 \\rangle = \\frac{1}{3} \\langle v^2 \\rangle$$

Substituting into the pressure expression yields the fundamental kinetic equation of gas pressure:
$$P V = \\frac{1}{3} N m \\langle v^2 \\rangle = \\frac{2}{3} N \\left( \\frac{1}{2} m \\langle v^2 \\rangle \\right) = \\frac{2}{3} E_{\\text{trans}}$$

Comparing with the macroscopic ideal gas equation of state $P V = n R T = N k_B T$, where $k_B = R / N_A$ is the Boltzmann constant:
$$\\frac{1}{3} m \\langle v^2 \\rangle = k_B T \\implies \\langle \\epsilon_{\\text{trans}} \\rangle = \\frac{1}{2} m \\langle v^2 \\rangle = \\frac{3}{2} k_B T$$

Each translational degree of freedom contributes precisely $\\frac{1}{2} k_B T$ to the average kinetic energy of a molecule, in full accord with the classical Equipartition Theorem."""
            },
            {
                "id": "sec-1-2",
                "secNumber": "1.2",
                "title": "Maxwell-Boltzmann Velocity & Speed Distributions in Three Dimensions",
                "content": """The equilibrium distribution of molecular velocities is governed by the Boltzmann factor $\\exp(-\\epsilon / k_B T)$. In three dimensions, translational kinetic energy is quadratic and uncoupled in each Cartesian component: $\\epsilon = \\frac{1}{2} m (v_x^2 + v_y^2 + v_z^2)$.

### Cartesian 1D Velocity Probability Density
The probability $f(v_x) dv_x$ that a molecule has an $x$-velocity between $v_x$ and $v_x + dv_x$ is normalized:
$$f(v_x) = \\left( \\frac{m}{2 \\pi k_B T} \\right)^{1/2} \\exp\\left( -\\frac{m v_x^2}{2 k_B T} \\right)$$

This is a Gaussian centered at $\\langle v_x \\rangle = 0$, with variance $\\sigma_x^2 = \\langle v_x^2 \\rangle = k_B T / m$.

### 3D Velocity Distribution
Because the Cartesian velocity components are statistically independent:
$$f(\\vec{v}) dv_x dv_y dv_z = f(v_x) f(v_y) f(v_z) dv_x dv_y dv_z = \\left( \\frac{m}{2 \\pi k_B T} \\right)^{3/2} \\exp\\left( -\\frac{m(v_x^2 + v_y^2 + v_z^2)}{2 k_B T} \\right) dv_x dv_y dv_z$$

### Transformation to Scalar Speed Distribution $f(v)$
To obtain the probability distribution of scalar speeds $v = (v_x^2 + v_y^2 + v_z^2)^{1/2}$, we transform from Cartesian coordinates to spherical polar coordinates in velocity space:
$$dv_x dv_y dv_z = v^2 \\sin\\theta \\, dv \\, d\\theta \\, d\\phi$$

Integrating over all solid angles $\\int_0^\\pi \\sin\\theta d\\theta \\int_0^{2\\pi} d\\phi = 4\\pi$:
$$f(v) dv = 4 \\pi v^2 \\left( \\frac{m}{2 \\pi k_B T} \\right)^{3/2} \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) dv$$

In terms of molar mass $M = m N_A$ and gas constant $R = N_A k_B$:
$$f(v) = 4 \\pi \\left( \\frac{M}{2 \\pi R T} \\right)^{3/2} v^2 \\exp\\left( -\\frac{M v^2}{2 R T} \\right)$$

The factor $v^2$ represents the growing volume of spherical shells in velocity space (density of states), while the exponential factor represents the Boltzmann thermal decay. The competition between these two terms generates an asymmetric distribution with a positive skew."""
            },
            {
                "id": "sec-1-3",
                "secNumber": "1.3",
                "title": "Characteristic Molecular Speeds: Most Probable, Mean & Root-Mean-Square Derivations",
                "content": """From the Maxwell-Boltzmann scalar speed distribution, three characteristic molecular speeds quantify different aspects of kinetic motion.

### 1. Most Probable Speed ($v_{\\text{mp}}$)
The most probable speed corresponds to the local maximum of the probability density function $f(v)$. Setting $\\frac{df(v)}{dv} = 0$:
$$\\frac{d}{dv} \\left[ v^2 \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) \\right] = 2 v \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) - \\frac{m v^3}{k_B T} \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) = 0$$

Dividing by $v \\exp(-m v^2 / 2 k_B T) \\neq 0$:
$$2 - \\frac{m v_{\\text{mp}}^2}{k_B T} = 0 \\implies v_{\\text{mp}} = \\sqrt{\\frac{2 k_B T}{m}} = \\sqrt{\\frac{2 R T}{M}}$$

### 2. Mean (Average) Speed ($\\bar{v}$ or $\\langle v \\rangle$)
The mean speed is the first moment of the distribution:
$$\\bar{v} = \\int_0^\\infty v f(v) dv = 4 \\pi \\left( \\frac{m}{2 \\pi k_B T} \\right)^{3/2} \\int_0^\\infty v^3 \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) dv$$

Using standard Gaussian definite integrals $\\int_0^\\infty x^3 e^{-a x^2} dx = \\frac{1}{2 a^2}$, with $a = \\frac{m}{2 k_B T}$:
$$\\bar{v} = 4 \\pi \\left( \\frac{m}{2 \\pi k_B T} \\right)^{3/2} \\cdot \\frac{1}{2 \\left( \\frac{m}{2 k_B T} \\right)^2} = \\sqrt{\\frac{8 k_B T}{\\pi m}} = \\sqrt{\\frac{8 R T}{\\pi M}}$$

### 3. Root-Mean-Square Speed ($v_{\\text{rms}}$)
The root-mean-square speed is the square root of the second moment:
$$\\langle v^2 \\rangle = \\int_0^\\infty v^2 f(v) dv = 4 \\pi \\left( \\frac{m}{2 \\pi k_B T} \\right)^{3/2} \\int_0^\\infty v^4 \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) dv$$

Using $\\int_0^\\infty x^4 e^{-a x^2} dx = \\frac{3}{8} \\sqrt{\\frac{\\pi}{a^5}}$:
$$\\langle v^2 \\rangle = \\frac{3 k_B T}{m} = \\frac{3 R T}{M} \\implies v_{\\text{rms}} = \\sqrt{\\langle v^2 \\rangle} = \\sqrt{\\frac{3 R T}{M}}$$

### Numerical Ordering & Comparison
$$v_{\\text{mp}} : \\bar{v} : v_{\\text{rms}} = \\sqrt{2} : \\sqrt{\\frac{8}{\\pi}} : \\sqrt{3} \\approx 1.000 : 1.128 : 1.225$$

At any temperature $T$, $v_{\\text{mp}} < \\bar{v} < v_{\\text{rms}}$ because the long exponential tail at high speeds pulls the higher-order moments towards higher velocities."""
            },
            {
                "id": "sec-1-4",
                "secNumber": "1.4",
                "title": "Molecular Collisions, Collision Cross-Sections & Mean Free Path",
                "content": """Molecules in a gas do not traverse infinite distances unobstructed; they undergo frequent binary collisions that randomize trajectories.

### Hard-Sphere Collision Cross-Section
Consider spherical molecules of diameter $d$. Two identical molecules collide when the distance between their centers is $r \\le d$. The collision cross-section $\\sigma$ is the circular target area presented by one molecule to another:
$$\\sigma = \\pi d^2$$

### Relative Speed of Colliding Pairs
When two identical molecules collide with velocities $\\vec{v}_1$ and $\\vec{v}_2$, their relative velocity is $\\vec{v}_{\\text{rel}} = \\vec{v}_1 - \\vec{v}_2$. Taking the ensemble average over isotropic distributions:
$$\\langle v_{\\text{rel}}^2 \\rangle = \\langle (\\vec{v}_1 - \\vec{v}_2)^2 \\rangle = \\langle v_1^2 \\rangle + \\langle v_2^2 \\rangle - 2 \\langle \\vec{v}_1 \\cdot \\vec{v}_2 \\rangle = 2 \\langle v^2 \\rangle$$
$$\\bar{v}_{\\text{rel}} = \\sqrt{2} \\bar{v} = \\sqrt{2} \\sqrt{\\frac{8 k_B T}{\\pi m}} = \\sqrt{\\frac{16 k_B T}{\\pi m}}$$

### Collision Frequency of a Single Molecule ($z$)
In time $\\Delta t$, a target molecule sweeps out a collision cylinder of volume $V_{\\text{cyl}} = \\sigma \\bar{v}_{\\text{rel}} \\Delta t$. With number density $\\mathcal{N} = N/V = P/(k_B T)$, the number of collisions per unit time experienced by one molecule is:
$$z = \\sigma \\bar{v}_{\\text{rel}} \\mathcal{N} = \\sqrt{2} \\pi d^2 \\bar{v} \\left( \\frac{P}{k_B T} \\right) = \\sqrt{2} \\pi d^2 \\sqrt{\\frac{8 k_B T}{\\pi m}} \\left( \\frac{P}{k_B T} \\right)$$

### Total Collision Density ($Z_{AA}$)
The total number of binary collisions per unit volume per unit time in a pure gas is:
$$Z_{AA} = \\frac{1}{2} \\mathcal{N} z = \\frac{1}{\\sqrt{2}} \\pi d^2 \\bar{v} \\mathcal{N}^2 = \\frac{1}{\\sqrt{2}} \\pi d^2 \\bar{v} \\left( \\frac{P}{k_B T} \\right)^2$$
The factor $\\frac{1}{2}$ prevents double-counting the collision pair.

### Mean Free Path ($\\lambda$)
The mean free path $\\lambda$ is the average distance traversed by a molecule between successive collisions:
$$\\lambda = \\frac{\\bar{v}}{z} = \\frac{\\bar{v}}{\\sqrt{2} \\pi d^2 \\bar{v} \\mathcal{N}} = \\frac{1}{\\sqrt{2} \\pi d^2 \\mathcal{N}} = \\frac{k_B T}{\\sqrt{2} \\pi d^2 P}$$

Key scaling relationships:
- $\\lambda \\propto T$ at constant pressure $P$.
- $\\lambda \\propto \\frac{1}{P}$ at constant temperature $T$.
- $\\lambda$ is independent of temperature $T$ at constant volume/density."""
            },
            {
                "id": "sec-1-5",
                "secNumber": "1.5",
                "title": "Wall Collisions, Effusion Flux & Knudsen Flow Mechanics",
                "content": """The rate at which gas molecules strike a surface governs effusion, adsorption, chemical vapor deposition, and heterogeneous reaction rates.

### Derivation of Collision Frequency with Walls ($Z_w$)
Consider an element of wall area $A$ in the $xy$-plane at $z = 0$. Molecules with positive $z$-velocity $v_z > 0$ located within distance $v_z \\Delta t$ will strike area $A$ during time interval $\\Delta t$.

The number of molecules with velocity between $v_z$ and $v_z + dv_z$ striking area $A$ in $\\Delta t$ is:
$$dN = A \\mathcal{N} v_z \\Delta t \\, f(v_z) dv_z$$

Integrating over all positive velocities $v_z \\in [0, \\infty)$:
$$Z_w = \\frac{N}{A \\Delta t} = \\mathcal{N} \\int_0^\\infty v_z f(v_z) dv_z = \\mathcal{N} \\left( \\frac{m}{2 \\pi k_B T} \\right)^{1/2} \\int_0^\\infty v_z \\exp\\left( -\\frac{m v_z^2}{2 k_B T} \\right) dv_z$$

Evaluating the integral:
$$\\int_0^\\infty v_z \\exp\\left( -\\frac{m v_z^2}{2 k_B T} \\right) dv_z = \\frac{k_B T}{m}$$

Thus:
$$Z_w = \\mathcal{N} \\left( \\frac{m}{2 \\pi k_B T} \\right)^{1/2} \\left( \\frac{k_B T}{m} \\right) = \\mathcal{N} \\sqrt{\\frac{k_B T}{2 \\pi m}} = \\frac{1}{4} \\mathcal{N} \\bar{v}$$

Using $\\mathcal{N} = P / (k_B T)$:
$$Z_w = \\frac{P}{\\sqrt{2 \\pi m k_B T}} = \\frac{P N_A}{\\sqrt{2 \\pi M R T}}$$

### Knudsen Effusion & Graham's Law
If a pinhole orifice of area $A_0$ has dimensions much smaller than the mean free path ($d_{\\text{hole}} \\ll \\lambda$, Knudsen number $\\text{Kn} = \\lambda / d_{\\text{hole}} \\gg 1$), molecules escape into vacuum without undergoing collisions in the aperture. This is **effusion**.

The molar rate of effusion is:
$$\\Phi_{\\text{eff}} = \\frac{Z_w A_0}{N_A} = \\frac{P A_0}{\\sqrt{2 \\pi M R T}}$$

The mass rate of effusion is:
$$\\frac{dm}{dt} = A_0 P \\sqrt{\\frac{M}{2 \\pi R T}}$$

For two different gases at identical temperature and pressure:
$$\\frac{\\text{Rate}_1}{\\text{Rate}_2} = \\sqrt{\\frac{M_2}{M_1}}$$
This provides the rigorous kinetic derivation of **Graham's Law of Effusion**."""
            },
            {
                "id": "sec-1-6",
                "secNumber": "1.6",
                "title": "Transport Properties of Dilute Gases I: Viscosity & Momentum Transport",
                "content": """Transport phenomena describe the macroscopic non-equilibrium flux of physical quantities—momentum, thermal energy, and mass—driven by gradients in macroscopic fields.

### Phenomenological Definition of Viscosity
Newton's law of viscosity states that when a shear velocity gradient $\\frac{du_x}{dz}$ exists in a fluid, a shear stress $\\tau_{xz}$ (momentum flux per unit area) opposes the shear:
$$J_{p_x} = -\\eta \\frac{du_x}{dz}$$
where $\\eta$ is the dynamic viscosity coefficient (SI units: $\\text{Pa}\\cdot\\text{s}$ or $\\text{kg}/(\\text{m}\\cdot\\text{s})$).

### Kinetic Theory Derivation of Viscosity
Consider a gas with a macroscopic velocity profile $u_x(z)$ moving in the $x$-direction, where $u_x$ increases with $z$. Molecules crossing a reference plane at $z = z_0$ last collided on average at distance $\\lambda$ above or below the plane.

1. Downward flux of molecules from $z_0 + \\frac{2}{3}\\lambda$:
   $$Z_{\\text{down}} = \\frac{1}{4} \\mathcal{N} \\bar{v}$$
   Molecules carrying momentum $p_x^+ = m u_x\\left(z_0 + \\frac{2}{3}\\lambda\\right) \\approx m \\left[ u_x(z_0) + \\frac{2}{3}\\lambda \\frac{du_x}{dz} \\right]$.

2. Upward flux of molecules from $z_0 - \\frac{2}{3}\\lambda$:
   $$Z_{\\text{up}} = \\frac{1}{4} \\mathcal{N} \\bar{v}$$
   Molecules carrying momentum $p_x^- = m u_x\\left(z_0 - \\frac{2}{3}\\lambda\\right) \\approx m \\left[ u_x(z_0) - \\frac{2}{3}\\lambda \\frac{du_x}{dz} \\right]$.

The net momentum flux $J_{p_x}$ transported downward across the plane per unit area per second is:
$$J_{p_x} = Z_{\\text{down}} p_x^+ - Z_{\\text{up}} p_x^- = \\frac{1}{4} \\mathcal{N} \\bar{v} \\cdot 2 m \\cdot \\frac{2}{3} \\lambda \\frac{du_x}{dz} = -\\frac{1}{3} \\mathcal{N} m \\bar{v} \\lambda \\frac{du_x}{dz}$$

Comparing with Newton's law:
$$\\eta = \\frac{1}{3} \\rho \\bar{v} \\lambda$$
where $\\rho = \\mathcal{N} m$ is the mass density.

Substituting $\\lambda = \\frac{1}{\\sqrt{2} \\pi d^2 \\mathcal{N}}$ and $\\bar{v} = \\sqrt{\\frac{8 k_B T}{\\pi m}}$:
$$\\eta = \\frac{1}{3} \\mathcal{N} m \\bar{v} \\left( \\frac{1}{\\sqrt{2} \\pi d^2 \\mathcal{N}} \\right) = \\frac{m \\bar{v}}{3 \\sqrt{2} \\pi d^2} = \\frac{2}{3 \\pi^{3/2} d^2} \\sqrt{m k_B T} = \\frac{2 \\sqrt{M R T}}{3 \\pi^{3/2} N_A d^2}$$

### Surprising Physical Consequences
1. **Pressure Independence**: Because $\\rho \\propto P$ and $\\lambda \\propto 1/P$, their product $\\rho \\lambda$ is independent of pressure. Dilute gas viscosity is independent of gas pressure (Maxwell's celebrated prediction, verified by experiment).
2. **Positive Temperature Dependence**: $\\eta \\propto \\sqrt{T}$. As temperature increases, gases become more viscous, in sharp contrast to liquids."""
            },
            {
                "id": "sec-1-7",
                "secNumber": "1.7",
                "title": "Transport Properties of Dilute Gases II: Thermal Conductivity & Energy Transport",
                "content": """Thermal conductivity represents the transport of kinetic energy down a temperature gradient $\\frac{dT}{dz}$.

### Phenomenological Law (Fourier's Law)
The heat flux vector $J_q$ (energy per unit area per unit time) is proportional to the negative thermal gradient:
$$J_q = -\\kappa \\frac{dT}{dz}$$
where $\\kappa$ is the thermal conductivity coefficient (SI units: $\\text{W}/(\\text{m}\\cdot\\text{K})$).

### Kinetic Theory Derivation of $\\kappa$
By analogy with momentum transport, molecules crossing a reference plane at $z_0$ carry the average thermal energy characteristic of their last collision at $z_0 \\pm \\frac{2}{3}\\lambda$:
$$\\epsilon(z) = \\epsilon(z_0) + \\frac{d\\epsilon}{dT} \\left( \\pm \\frac{2}{3}\\lambda \\frac{dT}{dz} \\right)$$

Noting that $\\frac{d\\epsilon}{dT} = c_v = \\frac{C_{V, m}}{N_A}$ is the heat capacity per molecule at constant volume:
$$J_q = -\\frac{1}{3} \\mathcal{N} \\bar{v} \\lambda c_v \\frac{dT}{dz}$$

Comparing with Fourier's law yields:
$$\\kappa = \\frac{1}{3} \\mathcal{N} c_v \\bar{v} \\lambda = \\frac{1}{3} \\frac{C_{V, m}}{M} \\rho \\bar{v} \\lambda$$

Substituting $\\eta = \\frac{1}{3} \\rho \\bar{v} \\lambda$:
$$\\kappa = \\frac{C_{V, m}}{M} \\eta$$

### Eucken Correction for Polyatomic Gases
For a monatomic gas with only translational degrees of freedom, $C_{V, m} = \\frac{3}{2} R$. Rigorous Chapman-Enskog kinetic theory yields a factor of $2.5$ for translational motion:
$$\\kappa_{\\text{mono}} = 2.5 \\eta \\frac{C_{V, \\text{trans}}}{M} = \\frac{15}{4} \\frac{R}{M} \\eta$$

For polyatomic gases carrying rotational and vibrational energy, the Eucken formula partitions transport into translational and internal modes:
$$\\kappa = \\frac{\\eta}{M} \\left( 2.5 C_{V, \\text{trans}} + 1.0 C_{V, \\text{int}} \\right) = \\frac{\\eta}{M} \\left( C_{V, m} + \\frac{9}{4} R \\right)$$

Like viscosity, dilute gas thermal conductivity $\\kappa$ is independent of pressure and scales as $\\sqrt{T}$."""
            }
        ],
        "problems": [
            {
                "id": "p1-1",
                "title": "Comprehensive Calculation of Characteristic Molecular Speeds of Nitrogen Gas",
                "difficulty": "Easy",
                "statement": "Calculate the most probable speed $v_{\\text{mp}}$, average speed $\\bar{v}$, and root-mean-square speed $v_{\\text{rms}}$ of dinitrogen molecules ($N_2$, molar mass $M = 28.0134\\text{ g/mol}$) at $T = 298.15\\text{ K}$ and at $T = 1000.0\\text{ K}$.",
                "solution": """**Step 1: Convert units to SI base units**
Molar mass of $N_2$:
$$M = 28.0134 \\times 10^{-3}\\text{ kg/mol}$$
Universal gas constant:
$$R = 8.314462\\text{ J}/(\\text{mol}\\cdot\\text{K})$$

**Step 2: Calculate speeds at $T = 298.15\\text{ K}$**
1. Most probable speed:
$$v_{\\text{mp}} = \\sqrt{\\frac{2 R T}{M}} = \\sqrt{\\frac{2 \\times 8.314462 \\times 298.15}{28.0134 \\times 10^{-3}}} = \\sqrt{1.76953 \\times 10^5} = 420.66\\text{ m/s}$$

2. Average speed:
$$\\bar{v} = \\sqrt{\\frac{8 R T}{\\pi M}} = \\sqrt{\\frac{8 \\times 8.314462 \\times 298.15}{\\pi \\times 28.0134 \\times 10^{-3}}} = \\sqrt{2.25302 \\times 10^5} = 474.66\\text{ m/s}$$

3. Root-mean-square speed:
$$v_{\\text{rms}} = \\sqrt{\\frac{3 R T}{M}} = \\sqrt{\\frac{3 \\times 8.314462 \\times 298.15}{28.0134 \\times 10^{-3}}} = \\sqrt{2.65430 \\times 10^5} = 515.20\\text{ m/s}$$

Ratio verification:
$$\\frac{v_{\\text{mp}}}{\\bar{v}} = \\frac{420.66}{474.66} = 0.8862 \\approx \\sqrt{\\frac{\\pi}{4}} = 0.8862$$
$$\\frac{v_{\\text{rms}}}{v_{\\text{mp}}} = \\frac{515.20}{420.66} = 1.2247 \\approx \\sqrt{\\frac{3}{2}} = 1.2247$$

**Step 3: Calculate speeds at $T = 1000.0\\text{ K}$**
Using scaling $v(T_2) = v(T_1) \\sqrt{T_2 / T_1}$:
$$\\sqrt{\\frac{1000.0}{298.15}} = \\sqrt{3.3540} = 1.8314$$
$$v_{\\text{mp}}(1000\\text{ K}) = 420.66 \\times 1.8314 = 770.39\\text{ m/s}$$
$$\\bar{v}(1000\\text{ K}) = 474.66 \\times 1.8314 = 869.29\\text{ m/s}$$
$$v_{\\text{rms}}(1000\\text{ K}) = 515.20 \\times 1.8314 = 943.53\\text{ m/s}$$"""
            },
            {
                "id": "p1-2",
                "title": "Fraction of Gas Molecules within a Specified Speed Interval",
                "difficulty": "Medium",
                "statement": "Using the Maxwell-Boltzmann distribution, determine the fraction of argon atoms ($M = 39.948\\text{ g/mol}$) at $T = 300.0\\text{ K}$ having speeds in the narrow interval between $400.0\\text{ m/s}$ and $405.0\\text{ m/s}$.",
                "solution": """**Step 1: Maxwell-Boltzmann differential approximation**
For a narrow speed interval $\\Delta v = 5.0\\text{ m/s} \\ll \\bar{v}$, the fraction is given by:
$$\\Delta F = f(v) \\Delta v = 4 \\pi \\left( \\frac{M}{2 \\pi R T} \\right)^{3/2} v^2 \\exp\\left( -\\frac{M v^2}{2 R T} \\right) \\Delta v$$
evaluated at the midpoint $v = 402.5\\text{ m/s}$.

**Step 2: Evaluate constants**
$$M = 39.948 \\times 10^{-3}\\text{ kg/mol}$$
$$R T = 8.314462 \\times 300.0 = 2494.34\\text{ J/mol}$$
$$\\frac{M}{2 R T} = \\frac{0.039948}{2 \\times 2494.34} = 8.00773 \\times 10^{-6}\\text{ s}^2/\\text{m}^2$$

Prefactor:
$$4 \\pi \\left( \\frac{M}{2 \\pi R T} \\right)^{3/2} = 4 \\pi \\left( \\frac{8.00773 \\times 10^{-6}}{\\pi} \\right)^{3/2} = 4 \\pi (2.54894 \\times 10^{-6})^{3/2} = 5.1122 \\times 10^{-8}$$

**Step 3: Evaluate exponential and speed term**
$$v^2 = (402.5)^2 = 1.62006 \\times 10^5\\text{ m}^2/\\text{s}^2$$
$$-\\frac{M v^2}{2 R T} = -8.00773 \\times 10^{-6} \\times 1.62006 \\times 10^5 = -1.2973$$
$$\\exp(-1.2973) = 0.27327$$

**Step 4: Compute probability density $f(v)$ and fraction $\\Delta F$**
$$f(402.5\\text{ m/s}) = (5.1122 \\times 10^{-8}) \\times (1.62006 \\times 10^5) \\times 0.27327 = 2.2632 \\times 10^{-3}\\text{ s/m}$$
$$\\Delta F = f(v) \\Delta v = (2.2632 \\times 10^{-3}\\text{ s/m}) \\times (5.0\\text{ m/s}) = 0.011316 = 1.132\\%$$

Thus, approximately $1.13\\%$ of all argon atoms possess speeds between $400$ and $405\\text{ m/s}$ at $300\\text{ K}$."""
            },
            {
                "id": "p1-3",
                "title": "Mean Free Path and Total Binary Collision Rate of Methane",
                "difficulty": "Medium",
                "statement": "For methane gas ($CH_4$, molecular collision diameter $d = 0.380\\text{ nm}$, molar mass $M = 16.043\\text{ g/mol}$) at $P = 1.000\\text{ bar}$ ($10^5\\text{ Pa}$) and $T = 293.15\\text{ K}$, calculate: (a) the mean free path $\\lambda$, (b) the collision frequency of a single molecule $z$, and (c) the total binary collision density $Z_{AA}$ in $\\text{m}^{-3}\\text{s}^{-1}$.",
                "solution": """**Step 1: Molecular diameter and collision cross-section**
$$d = 0.380 \\times 10^{-9}\\text{ m}$$
$$\\sigma = \\pi d^2 = \\pi (0.380 \\times 10^{-9})^2 = 4.53646 \\times 10^{-19}\\text{ m}^2$$

**Step 2: Number density $\\mathcal{N}$**
$$\\mathcal{N} = \\frac{P}{k_B T} = \\frac{1.000 \\times 10^5}{1.380649 \\times 10^{-23} \\times 293.15} = 2.4708 \\times 10^{25}\\text{ molecules/m}^3$$

**Step 3: Mean free path $\\lambda$**
$$\\lambda = \\frac{1}{\\sqrt{2} \\pi d^2 \\mathcal{N}} = \\frac{1}{\\sqrt{2} \\sigma \\mathcal{N}} = \\frac{1}{\\sqrt{2} \\times (4.53646 \\times 10^{-19}) \\times (2.4708 \\times 10^{25})} = 6.309 \\times 10^{-8}\\text{ m} = 63.09\\text{ nm}$$

**Step 4: Average speed $\\bar{v}$ and single-molecule collision frequency $z$**
$$\\bar{v} = \\sqrt{\\frac{8 R T}{\\pi M}} = \\sqrt{\\frac{8 \\times 8.314462 \\times 293.15}{\\pi \\times 0.016043}} = \\sqrt{3.8690 \\times 10^5} = 622.01\\text{ m/s}$$
$$z = \\frac{\\bar{v}}{\\lambda} = \\frac{622.01}{6.309 \\times 10^{-8}} = 9.859 \\times 10^9\\text{ collisions/s} \\approx 9.86\\text{ GHz}$$

**Step 5: Total binary collision rate density $Z_{AA}$**
$$Z_{AA} = \\frac{1}{2} \\mathcal{N} z = \\frac{1}{2} \\times (2.4708 \\times 10^{25}) \\times (9.859 \\times 10^9) = 1.218 \\times 10^{35}\\text{ collisions}/(\\text{m}^3\\cdot\\text{s})$$"""
            },
            {
                "id": "p1-4",
                "title": "Knudsen Effusion Separation Factor for Uranium Hexafluoride Isotopes",
                "difficulty": "Hard",
                "statement": "In the historical isotope enrichment of uranium, gaseous uranium hexafluoride ($^{235}UF_6$ and $^{238}UF_6$) effuses through a porous membrane. Given atomic masses $^{235}U = 235.0439\\text{ u}$, $^{238}U = 238.0508\\text{ u}$, and $^{19}F = 18.9984\\text{ u}$: (a) calculate the ideal single-stage Knudsen separation factor $\\alpha$, (b) calculate the number of successive stages required to enrich natural uranium ($0.720\\%\\; ^{235}U$) to reactor-grade fuel ($4.00\\%\\; ^{235}U$).",
                "solution": """**Step 1: Calculate molecular weights of the hexafluorides**
$$M_1(^{235}UF_6) = 235.0439 + 6(18.9984) = 349.0343\\text{ g/mol}$$
$$M_2(^{238}UF_6) = 238.0508 + 6(18.9984) = 352.0412\\text{ g/mol}$$

**Step 2: Ideal separation factor $\\alpha$**
By Graham's Law of Effusion, the single-stage separation factor is:
$$\\alpha = \\sqrt{\\frac{M_2}{M_1}} = \\sqrt{\\frac{352.0412}{349.0343}} = \\sqrt{1.008615} = 1.004298$$

Each single stage enriches the gas by an infinitesimal factor of only $0.43\\%$.

**Step 3: Multi-stage cascade calculation**
Let $R = \\frac{x}{1 - x}$ be the isotope abundance ratio ($^{235}U / ^{238}U$).
Initial feed ratio:
$$x_0 = 0.00720 \\implies R_0 = \\frac{0.00720}{1 - 0.00720} = \\frac{0.00720}{0.99280} = 7.2522 \\times 10^{-3}$$

Target product ratio:
$$x_N = 0.0400 \\implies R_N = \\frac{0.0400}{1 - 0.0400} = \\frac{0.0400}{0.9600} = 4.1667 \\times 10^{-2}$$

For an ideal gaseous diffusion cascade of $N$ stages:
$$R_N = R_0 \\cdot \\alpha^N \\implies \\alpha^N = \\frac{R_N}{R_0}$$
$$\\alpha^N = \\frac{4.1667 \\times 10^{-2}}{7.2522 \\times 10^{-3}} = 5.7454$$

Taking natural logarithms:
$$N \\ln(\\alpha) = \\ln(5.7454)$$
$$N = \\frac{\\ln(5.7454)}{\\ln(1.004298)} = \\frac{1.7484}{4.2888 \\times 10^{-3}} = 407.7$$

Rounding up: **408 stages** are theoretically required in an ideal cascade, illustrating why gaseous diffusion plants required miles of cascade halls."""
            },
            {
                "id": "p1-5",
                "title": "Molecular Diameter Derivation from Experimental Gas Viscosity",
                "difficulty": "Medium",
                "statement": "The experimental dynamic viscosity of gaseous argon ($M = 39.948\\text{ g/mol}$) at $T = 273.15\\text{ K}$ and $P = 1.00\\text{ atm}$ is $\\eta = 2.10 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$. From kinetic theory, determine: (a) the effective hard-sphere molecular diameter $d$, and (b) the predicted viscosity of argon at $T = 500.0\\text{ K}$.",
                "solution": """**Step 1: Relate viscosity to molecular diameter**
From kinetic theory:
$$\\eta = \\frac{2 \\sqrt{M R T}}{3 \\pi^{3/2} N_A d^2}$$

Solving for $d^2$:
$$d^2 = \\frac{2 \\sqrt{M R T}}{3 \\pi^{3/2} N_A \\eta}$$

**Step 2: Evaluate constants at $T = 273.15\\text{ K}$**
$$M = 0.039948\\text{ kg/mol}$$
$$R = 8.314462\\text{ J}/(\\text{mol}\\cdot\\text{K})$$
$$\\sqrt{M R T} = \\sqrt{0.039948 \\times 8.314462 \\times 273.15} = \\sqrt{90.725} = 9.5250\\text{ kg}\\cdot\\text{m}/(\\text{s}\\cdot\\text{mol})$$

$$d^2 = \\frac{2 \\times 9.5250}{3 \\times (\\pi)^{1.5} \\times (6.02214 \\times 10^{23}) \\times (2.10 \\times 10^{-5})}$$
$$3 \\times \\pi^{1.5} = 3 \\times 5.56833 = 16.705$$
$$\\text{Denominator} = 16.705 \\times 6.02214 \\times 10^{23} \\times 2.10 \\times 10^{-5} = 2.1126 \\times 10^{20}$$

$$d^2 = \\frac{19.050}{2.1126 \\times 10^{20}} = 9.0173 \\times 10^{-20}\\text{ m}^2$$
$$d = \\sqrt{9.0173 \\times 10^{-20}} = 3.003 \\times 10^{-10}\\text{ m} = 0.300\\text{ nm} = 3.00\\text{ Å}$$

**Step 3: Predicted viscosity at $T = 500.0\\text{ K}$**
Since $\\eta \\propto \\sqrt{T}$:
$$\\eta(500\\text{ K}) = \\eta(273.15\\text{ K}) \\sqrt{\\frac{500.0}{273.15}} = 2.10 \\times 10^{-5} \\times \\sqrt{1.8305} = 2.10 \\times 10^{-5} \\times 1.35296 = 2.84 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$$"""
            },
            {
                "id": "p1-6",
                "title": "Thermal Conductivity of Neon and Verification of Eucken Factor",
                "difficulty": "Hard",
                "statement": "Neon is a monatomic noble gas ($M = 20.1797\\text{ g/mol}$, $C_{V, m} = \\frac{3}{2} R$, $d = 0.260\\text{ nm}$). At $T = 300.0\\text{ K}$: (a) calculate the dynamic viscosity $\\eta$, (b) calculate the thermal conductivity $\\kappa$ using the Chapman-Enskog relation $\\kappa = 2.5 \\eta \\frac{C_{V, m}}{M}$, and (c) determine the heat flux through a $1.00\\text{ cm}$ neon gas gap held between plates at $305\\text{ K}$ and $295\\text{ K}$.",
                "solution": """**Step 1: Viscosity of Neon at $300\\text{ K}$**
$$d = 0.260 \\times 10^{-9}\\text{ m}$$
$$\\sqrt{M R T} = \\sqrt{0.02018 \\times 8.31446 \\times 300.0} = \\sqrt{50.336} = 7.0948$$
$$\\eta = \\frac{2 \\sqrt{M R T}}{3 \\pi^{3/2} N_A d^2} = \\frac{2 \\times 7.0948}{16.705 \\times (6.02214 \\times 10^{23}) \\times (0.260 \\times 10^{-9})^2}$$
$$\\eta = \\frac{14.1896}{16.705 \\times 6.02214 \\times 10^{23} \\times 6.76 \\times 10^{-20}} = \\frac{14.1896}{6.7997 \\times 10^5} = 2.0868 \\times 10^{-5}\\text{ Pa}\\cdot\\text{s}$$

**Step 2: Thermal conductivity $\\kappa$**
For a monatomic gas:
$$\\frac{C_{V, m}}{M} = \\frac{1.5 \\times 8.314462}{0.0201797} = 618.03\\text{ J}/(\\text{kg}\\cdot\\text{K})$$
$$\\kappa = 2.5 \\times \\eta \\times \\frac{C_{V, m}}{M} = 2.5 \\times (2.0868 \\times 10^{-5}) \\times 618.03 = 0.03224\\text{ W}/(\\text{m}\\cdot\\text{K})$$

Experimental value for neon at $300\\text{ K}$ is $0.0318\\text{ W}/(\\text{m}\\cdot\\text{K})$, yielding $< 1.5\\%$ error.

**Step 3: Heat flux between plates**
$$J_q = -\\kappa \\frac{dT}{dz} = \\kappa \\frac{\\Delta T}{\\Delta z}$$
$$\\Delta T = 305 - 295 = 10.0\\text{ K}$$
$$\\Delta z = 1.00 \\times 10^{-2}\\text{ m}$$
$$J_q = 0.03224 \\times \\frac{10.0}{0.0100} = 32.24\\text{ W/m}^2$$"""
            },
            {
                "id": "p1-7",
                "title": "Sublimation Vapor Pressure Measurement via Knudsen Effusion Loss",
                "difficulty": "Hard",
                "statement": "A solid organic compound of molar mass $M = 152.15\\text{ g/mol}$ is placed in a Knudsen effusion cell with a circular pinhole of diameter $d_{\\text{hole}} = 1.20\\text{ mm}$. The cell is maintained in high vacuum at $T = 320.0\\text{ K}$. Over an exposure period of $t = 2.50\\text{ hours}$, the measured mass loss is $\\Delta m = 18.6\\text{ mg}$. Calculate the equilibrium sublimation vapor pressure $P$ of the compound in Pascals.",
                "solution": """**Step 1: Pinhole orifice area and mass loss rate**
Pinhole radius:
$$r = \\frac{1.20 \\times 10^{-3}}{2} = 6.00 \\times 10^{-4}\\text{ m}$$
$$A_0 = \\pi r^2 = \\pi (6.00 \\times 10^{-4})^2 = 1.13097 \\times 10^{-6}\\text{ m}^2$$

Exposure time:
$$t = 2.50 \\times 3600 = 9000.0\\text{ s}$$

Mass loss:
$$\\Delta m = 18.6 \\times 10^{-6}\\text{ kg}$$
$$\\frac{dm}{dt} = \\frac{18.6 \\times 10^{-6}\\text{ kg}}{9000.0\\text{ s}} = 2.0667 \\times 10^{-9}\\text{ kg/s}$$

**Step 2: Knudsen effusion equation for vapor pressure**
$$\\frac{dm}{dt} = A_0 P \\sqrt{\\frac{M}{2 \\pi R T}}$$
$$P = \\frac{dm/dt}{A_0} \\sqrt{\\frac{2 \\pi R T}{M}}$$

**Step 3: Evaluate square root factor**
$$M = 0.15215\\text{ kg/mol}$$
$$2 \\pi R T = 2 \\times \\pi \\times 8.314462 \\times 320.0 = 1.67167 \\times 10^4\\text{ J/mol}$$
$$\\sqrt{\\frac{2 \\pi R T}{M}} = \\sqrt{\\frac{1.67167 \\times 10^4}{0.15215}} = \\sqrt{1.09870 \\times 10^5} = 331.47\\text{ m/s}$$

**Step 4: Compute vapor pressure $P$**
$$P = \\frac{2.0667 \\times 10^{-9}}{1.13097 \\times 10^{-6}} \\times 331.47 = (1.82737 \\times 10^{-3}) \\times 331.47 = 0.6057\\text{ Pa}$$

Expressed in Torr:
$$P = 0.6057 \\times \\frac{760}{101325} = 4.54 \\times 10^{-3}\\text{ Torr}$$"""
            }
        ]
    }
    units.append(u1)

    # =========================================================================
    # UNIT 2: Ion Transport & Electrolytic Conduction in Solution
    # =========================================================================
    u2 = {
        "id": "unit-2",
        "unitNumber": 2,
        "title": "Unit 2: Ion Transport & Electrolytic Conduction in Solution",
        "leadSummary": "Thermodynamics and physical electrochemistry of electrolytic conduction: Ohm's law in ionic solutions, specific and molar conductivities, Kohlrausch's law of independent ionic migration, ionic drift velocity under external electric potential gradients, Stokes-Einstein hydrodynamic drag, Walden's rule, transference numbers via Hittorf and moving-boundary methods, and the Debye-Hückel-Onsager theory of electrophoretic and relaxation effects.",
        "simulations": ["sim_kin_electrolyte_ionic_mobility"],
        "sections": [
            {
                "id": "sec-2-1",
                "secNumber": "2.1",
                "title": "Electrolytic Conduction & Ohm's Law: Specific & Molar Conductance",
                "content": """Electrolytic solutions conduct electricity through the physical migration of dissolved cations and anions under an applied electric potential gradient.

### Resistance, Resistivity & Specific Conductance
Consider a uniform electrolytic column of length $l$ and cross-sectional area $A$. According to Ohm's law, the electric resistance $R$ is:
$$R = \\rho \\frac{l}{A}$$
where $\\rho$ is the resistivity ($\\Omega\\cdot\\text{m}$). The reciprocal of resistance is conductance $G = 1/R$ (Siemens, $\\text{S} = \\Omega^{-1}$).

The **specific conductivity** (or electrolytic conductivity) $\\kappa$ is defined as the reciprocal of resistivity:
$$\\kappa = \\frac{1}{\\rho} = \\frac{l}{R A} = G \\cdot \\left( \\frac{l}{A} \\right) = G \\cdot K_{\\text{cell}}$$
where $K_{\\text{cell}} = l/A$ is the cell constant ($\\text{m}^{-1}$ or $\\text{cm}^{-1}$), routinely calibrated using primary aqueous $KCl$ standard solutions.

### Molar Conductivity ($\\Lambda_m$)
To compare the conducting capabilities of different electrolytes on a per-mole basis, the **molar conductivity** $\\Lambda_m$ normalizes specific conductivity by stoichiometric concentration $c$ (mol/L or $\\text{mol/m}^3$):
$$\\Lambda_m = \\frac{\\kappa}{c}$$

In laboratory practical units where $\\kappa$ is in $\\text{S}\\cdot\\text{cm}^{-1}$ and $c$ is in $\\text{mol/L}$ ($\text{M}$):
$$\\Lambda_m (\\text{S}\\cdot\\text{cm}^2\\text{/mol}) = \\frac{1000 \\times \\kappa (\\text{S}\\cdot\\text{cm}^{-1})}{c (\\text{mol/L})}$$
In SI base units where $\\kappa$ is in $\\text{S}\\cdot\\text{m}^{-1}$ and $c$ is in $\\text{mol}\\cdot\\text{m}^{-3}$:
$$\\Lambda_m (\\text{S}\\cdot\\text{m}^2\\text{/mol}) = \\frac{\\kappa}{c}$$"""
            },
            {
                "id": "sec-2-2",
                "secNumber": "2.2",
                "title": "Concentration Dependence of Molar Conductivity: Strong vs. Weak Electrolytes",
                "content": """The variation of molar conductivity $\\Lambda_m$ with concentration reveals the degree of ionization and interionic interactions.

### Strong Electrolytes: Kohlrausch's Square-Root Law
For strong electrolytes (e.g., $NaCl, KCl, HCl, K_2SO_4$), which dissociate virtually completely in dilute aqueous solution, Friedrich Kohlrausch discovered empirically (1875) that $\\Lambda_m$ decreases linearly with the square root of concentration:
$$\\Lambda_m = \\Lambda_m^\\circ - K \\sqrt{c}$$
where:
- $\\Lambda_m^\\circ$ is the **limiting molar conductivity** at infinite dilution.
- $K$ is the Kohlrausch empirical slope constant, depending on electrolyte valence stoichiometry, solvent dielectric permittivity, and temperature.

The decrease in $\\Lambda_m$ with increasing concentration for strong electrolytes arises not from incomplete ionization, but from electrostatic interionic retarding forces (electrophoretic and relaxation effects).

### Weak Electrolytes: Ostwald's Dilution Law
For weak electrolytes (e.g., $CH_3COOH, NH_3$), which are only partially ionized in solution ($AB \\rightleftharpoons A^+ + B^-$):
$$\\alpha = \\frac{\\Lambda_m}{\\Lambda_m^\\circ}$$
where $\\alpha$ is the degree of dissociation (Arrhenius relation).

The thermodynamic acid dissociation equilibrium constant is:
$$K_a = \\frac{[A^+][B^-]}{[AB]} = \\frac{c \\alpha^2}{1 - \\alpha}$$
Substituting $\\alpha = \\Lambda_m / \\Lambda_m^\\circ$:
$$K_a = \\frac{c (\\Lambda_m / \\Lambda_m^\\circ)^2}{1 - (\\Lambda_m / \\Lambda_m^\\circ)} = \\frac{c \\Lambda_m^2}{\\Lambda_m^\\circ (\\Lambda_m^\\circ - \\Lambda_m)}$$

Rearranging into linear form yields **Ostwald's Dilution Law**:
$$\\frac{1}{\\Lambda_m} = \\frac{1}{\\Lambda_m^\\circ} + \\frac{c \\Lambda_m}{K_a (\\Lambda_m^\\circ)^2}$$
Plotting $1/\\Lambda_m$ versus $c \\Lambda_m$ yields an intercept of $1/\\Lambda_m^\\circ$ and a slope of $1 / [K_a (\\Lambda_m^\\circ)^2]$, enabling the simultaneous determination of both limiting conductivity and the dissociation constant."""
            },
            {
                "id": "sec-2-3",
                "secNumber": "2.3",
                "title": "Kohlrausch's Law of Independent Migration of Ions",
                "content": """At infinite dilution ($c \\to 0$), interionic Coulombic interactions vanish as ion-ion separations approach infinity. Consequently, each ion moves independently of its counterions.

### Formulation of the Law
**Kohlrausch's Law of Independent Migration of Ions** states that the limiting molar conductivity of an electrolyte is the sum of the individual limiting molar ionic conductivities of its constituent ions:
$$\\Lambda_m^\\circ = \\nu_+ \\lambda_+^\\circ + \\nu_- \\lambda_-^\\circ$$
where $\\nu_+$ and $\\nu_-$ are the stoichiometric stoichiometric numbers of cations and anions per formula unit, and $\\lambda_+^\\circ$ and $\\lambda_-^\\circ$ are their limiting molar ionic conductivities.

### Determination of $\\Lambda_m^\\circ$ for Weak Electrolytes
Weak electrolytes do not permit direct linear extrapolation of $\\Lambda_m$ versus $\\sqrt{c}$ to obtain $\\Lambda_m^\\circ$, because the curve turns sharply upward at extreme dilutions. Kohlrausch's law circumvents this limitation through linear combinations of strong electrolyte conductivities.

For acetic acid ($CH_3COOH$):
$$\\Lambda_m^\\circ(CH_3COOH) = \\lambda^\\circ(H^+) + \\lambda^\\circ(CH_3COO^-)$$
By measuring the strong electrolytes $HCl$, $CH_3COONa$, and $NaCl$:
$$\\Lambda_m^\\circ(CH_3COOH) = \\Lambda_m^\\circ(HCl) + \\Lambda_m^\\circ(CH_3COONa) - \\Lambda_m^\\circ(NaCl)$$
$$= [\\lambda^\\circ(H^+) + \\lambda^\\circ(Cl^-)] + [\\lambda^\\circ(Na^+) + \\lambda^\\circ(CH_3COO^-)] - [\\lambda^\\circ(Na^+) + \\lambda^\\circ(Cl^-)] = \\lambda^\\circ(H^+) + \\lambda^\\circ(CH_3COO^-)$$
This algebraic cancellation provides exact limiting conductivities for any weak electrolyte."""
            },
            {
                "id": "sec-2-4",
                "secNumber": "2.4",
                "title": "Ionic Drift Velocities, Mobilities & Stokes-Einstein Hydrodynamic Drag",
                "content": """When an external electric field $\\vec{E} = -\\nabla \\phi$ is applied across an electrolyte solution, an ion of charge $q_i = z_i e$ experiences an electrostatic force:
$$\\vec{F}_{\\text{elec}} = z_i e \\vec{E}$$

### Terminal Drift Velocity and Ionic Mobility
As the ion accelerates, it encounters hydrodynamic frictional drag from solvent molecules. In the low Reynolds number regime, the drag force opposes motion:
$$\\vec{F}_{\\text{drag}} = -f_i \\vec{v}_{\\text{drift}}$$
where $f_i$ is the hydrodynamic friction coefficient.

Terminal drift velocity is achieved almost instantaneously (picoseconds) when $\\vec{F}_{\\text{elec}} + \\vec{F}_{\\text{drag}} = 0$:
$$z_i e E = f_i v_{\\text{drift}} \\implies v_{\\text{drift}} = \\frac{|z_i| e}{f_i} E$$

The **ionic mobility** $u_i$ is defined as the drift speed per unit electric field:
$$u_i = \\frac{v_{\\text{drift}}}{E} = \\frac{|z_i| e}{f_i}$$
SI units: $\\text{m}^2/(\\text{V}\\cdot\\text{s})$ or $\\text{m}^2/(\\text{J}/\\text{C}\\cdot\\text{s})$.

### Stokes Frictional Drag and Hydrated Radii
Assuming a spherical ion of effective hydrodynamic (hydrated) radius $r_{\\text{hyd}}$ moving through a continuous viscous solvent of dynamic viscosity $\\eta$, Stokes' law gives:
$$f_i = 6 \\pi \\eta r_{\\text{hyd}}$$

Substituting into mobility:
$$u_i = \\frac{|z_i| e}{6 \\pi \\eta r_{\\text{hyd}}}$$

### Relation to Limiting Molar Ionic Conductivity
Consider 1 mole of ions moving under field $E$. The electric current transported by species $i$ through area $A$ is:
$$I_i = |z_i| F \\cdot (c_i A v_{\\text{drift}}) = |z_i| F c_i A u_i E$$
Current density $j_i = I_i / A = |z_i| F c_i u_i E = \\kappa_i E$.
Thus, specific conductivity $\\kappa_i = |z_i| F c_i u_i$, and limiting molar ionic conductivity is:
$$\\lambda_i^\\circ = |z_i| F u_i = \\frac{|z_i|^2 e F}{6 \\pi \\eta r_{\\text{hyd}}} = \\frac{|z_i|^2 F^2}{6 \\pi N_A \\eta r_{\\text{hyd}}}$$"""
            },
            {
                "id": "sec-2-5",
                "secNumber": "2.5",
                "title": "Walden's Rule & Solvent Viscosity: Grotthuss Proton Hopping Mechanism",
                "content": """The interplay between ionic mobility and solvent friction provides deep insights into solvation dynamics.

### Walden's Rule
From the Stokes-Einstein expression $\\lambda_i^\\circ = \\frac{|z_i|^2 F^2}{6 \\pi N_A \\eta r_{\\text{hyd}}}$, if the effective hydrodynamic radius $r_{\\text{hyd}}$ of an ion remains constant across different non-aqueous solvents:
$$\\lambda_i^\\circ \\eta = \\text{constant} \\quad \\text{and} \\quad \\Lambda_m^\\circ \\eta = \\text{constant}$$
This product is **Walden's Rule**. It holds well for large, hydrophobic ions (such as tetraalkylammonium cations $(C_4H_9)_4N^+$) that do not perturb solvent structure or vary their solvation shells.

### Anomaly of Alkali Metal Ions
In aqueous solution, bare ionic radii increase down Group 1:
$$r_{\\text{bare}}(Li^+) = 0.76\\text{ Å} < r_{\\text{bare}}(Na^+) = 1.02\\text{ Å} < r_{\\text{bare}}(K^+) = 1.38\\text{ Å} < r_{\\text{bare}}(Cs^+) = 1.67\\text{ Å}$$

However, limiting ionic conductivities exhibit the exact opposite trend:
$$\\lambda^\\circ(Li^+) = 38.7 < \\lambda^\\circ(Na^+) = 50.1 < \\lambda^\\circ(K^+) = 73.5 < \\lambda^\\circ(Cs^+) = 77.2\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$$

**Physical Explanation**: Due to its high surface charge density ($z/r_{\\text{bare}}$), the small $Li^+$ ion strongly polarizes water molecules, binding an extensive primary and secondary hydration shell ($r_{\\text{hyd}}(Li^+) \\approx 3.8\\text{ Å}$). The larger $Cs^+$ has low charge density and carries a minimal hydration shell ($r_{\\text{hyd}}(Cs^+) \\approx 2.3\\text{ Å}$). Moving through water, $Li^+$ drags a much larger hydrodynamic water envelope, increasing Stokes drag and lowering mobility.

### Grotthuss Mechanism for $H^+$ and $OH^-$
Hydrogen ($H_3O^+$) and hydroxide ($OH^-$) ions exhibit extraordinarily large conductivities in water:
$$\\lambda^\\circ(H^+) = 349.8\\text{ S}\\cdot\\text{cm}^2\\text{/mol}, \\quad \\lambda^\\circ(OH^-) = 198.3\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$$
compared to normal ions ($\\approx 50\\text{--}75\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$).

These ions do not migrate primarily via hydrodynamic translation. Instead, charge transport occurs via the **Grotthuss mechanism** (proton jumping). A proton hops from a hydronium ion to an adjacent hydrogen-bonded water molecule through rapid rearrangement of covalent bonds and hydrogen bonds:
$$H_3O^+ + H_2O \\longrightarrow H_2O + H_3O^+$$
The net positive charge translocates across several molecular diameters without requiring physical diffusion of the oxygen nucleus through the viscous matrix."""
            },
            {
                "id": "sec-2-6",
                "secNumber": "2.6",
                "title": "Transport Numbers: Hittorf Method & Moving Boundary Method Balances",
                "content": """The fraction of total electrical current carried by an individual ionic species in solution is its **transport number** (or transference number) $t_i$.

### Definition and Relations
$$t_+ = \\frac{I_+}{I_{\\text{total}}} = \\frac{\\nu_+ z_+ u_+}{\\nu_+ z_+ u_+ + \\nu_- |z_-| u_-} = \\frac{\\nu_+ \\lambda_+}{\\Lambda_m}$$
$$t_- = \\frac{I_-}{I_{\\text{total}}} = \\frac{\\nu_- |z_-| u_-}{\\nu_+ z_+ u_+ + \\nu_- |z_-| u_-} = \\frac{\\nu_- \\lambda_-}{\\Lambda_m}$$
For a binary 1:1 electrolyte ($NaCl, HCl$):
$$t_+ + t_- = 1$$

### Hittorf Method
Developed by Wilhelm Hittorf (1853), this classical method measures the concentration changes in the anode and cathode compartments of an electrolysis cell following passage of a known quantity of charge $Q = I \\cdot t$ (measured with a silver coulometer).

Consider electrolysis of $AgNO_3$ with silver electrodes:
- At the anode: silver dissolves ($Ag \\to Ag^+ + e^-$), adding $Q/F$ moles of $Ag^+$.
- Simultaneously, $Ag^+$ cations migrate out of the anode compartment toward the cathode ($t_+ Q / F$ moles).
- Net increase in $Ag^+$ in the anode compartment:
  $$\\Delta n(\\text{anode}) = \\frac{Q}{F} - t_+ \\frac{Q}{F} = (1 - t_+) \\frac{Q}{F} = t_- \\frac{Q}{F}$$
Measuring $\\Delta n$ and $Q$ yields $t_-$ directly, and $t_+ = 1 - t_-$.

### Moving Boundary Method
The moving boundary method provides higher precision by directly tracking the physical displacement of an interface between two solutions having a common ion.

Let solution 1 be the leading electrolyte ($HCl$) and solution 2 be the indicator electrolyte ($CdCl_2$), with $H^+$ and $Cd^{2+}$ sharing common $Cl^-$.
The boundary between $HCl$ and $CdCl_2$ moves upward as $H^+$ ions migrate toward the cathode.

In time $t$, if the boundary of tube cross-section $A$ sweeps through distance $x$:
- The volume swept is $V = x A$.
- The moles of $H^+$ passing the boundary is $n(H^+) = c \\cdot V = c x A$.
- Charge carried by these $H^+$ ions is $Q_+ = z_+ F n(H^+) = F c x A$.
- Total charge passed through the circuit is $Q = I \\cdot t$.

Therefore, the transport number of the leading cation is:
$$t_+ = \\frac{Q_+}{Q} = \\frac{z_+ F c x A}{I t}$$
By maintaining the Kohlrausch regulating condition $\\frac{t_+}{c_1} = \\frac{t_{2,+}}{c_2}$, the boundary remains sharp throughout the experiment."""
            },
            {
                "id": "sec-2-7",
                "secNumber": "2.7",
                "title": "Ion-Ion Interactions & the Debye-Hückel-Onsager (DHO) Limiting Law",
                "content": """In strong electrolyte solutions, electrostatic interactions between ions create a local spherical distribution called the **ionic atmosphere**, in which every cation is surrounded on average by excess negative charge, and vice versa.

### Origin of Conductivity Retardation
Under an external electric field $\\vec{E}$, two distinct retarding phenomena decrease molar conductivity below $\\Lambda_m^\\circ$:

1. **Relaxation Effect (Asymmetry Potential)**:
   When an ion moves, its ionic atmosphere is disrupted ahead and must reform behind. Because polarization and ionic rearrangement take a finite relaxation time $\\tau_{\\text{relax}} \\sim 10^{-10}\\text{ s}$, the ionic atmosphere becomes distorted and asymmetric, accumulating excess opposite charge behind the moving ion. This creates a retarding electric field $E_{\\text{relax}}$ opposing the external field.

2. **Electrophoretic Effect**:
   The ionic atmosphere carries counter-ions with bound solvent molecules. When an electric field is applied, the atmosphere drifts in the opposite direction to the central ion, creating a local solvent counter-flow. The central ion must move upstream against this moving solvent, experiencing enhanced hydrodynamic viscous drag.

### Lars Onsager's Treatment (1927)
Incorporating Brownian motion and hydrodynamic Navier-Stokes equations into the Debye-Hückel framework, Lars Onsager derived the limiting equation for a 1:1 electrolyte:
$$\\Lambda_m = \\Lambda_m^\\circ - \\left( A + B \\Lambda_m^\\circ \\right) \\sqrt{c}$$
where:
- $A$ represents the **electrophoretic retardation**:
  $$A = \\frac{z^2 e F}{3 \\pi \\eta} \\left( \\frac{2 e^2 N_A}{\\varepsilon_r \\varepsilon_0 k_B T} \\right)^{1/2}$$
- $B$ represents the **relaxation retardation**:
  $$B = \\frac{z^3 e^2}{24 \\pi \\varepsilon_r \\varepsilon_0 k_B T} \\cdot \\frac{q}{1 + \\sqrt{q}} \\left( \\frac{2 e^2 N_A}{\\varepsilon_r \\varepsilon_0 k_B T} \\right)^{1/2}$$
  with $q = 0.5$ for symmetrical 1:1 electrolytes.

For aqueous 1:1 electrolytes at $T = 298.15\\text{ K}$ ($\varepsilon_r = 78.36$, $\\eta = 0.8903\\text{ cP}$):
$$A = 60.20\\text{ S}\\cdot\\text{cm}^2\\text{/mol}\\cdot(\\text{L/mol})^{1/2}$$
$$B = 0.229\\;(\\text{L/mol})^{1/2}$$
$$\\Lambda_m = \\Lambda_m^\\circ - \\left( 60.20 + 0.229 \\Lambda_m^\\circ \\right) \\sqrt{c}$$

The Debye-Hückel-Onsager equation provides the first-principles theoretical explanation for Kohlrausch's empirical $\\sqrt{c}$ law in dilute solutions ($c < 0.01\\text{ M}$)."""
            }
        ],
        "problems": [
            {
                "id": "p2-1",
                "title": "Specific and Molar Conductivity from Resistance and Cell Constant",
                "difficulty": "Easy",
                "statement": "A conductivity cell filled with a $0.0200\\text{ M}$ aqueous solution of potassium chloride ($KCl$) has a measured resistance of $R_1 = 432.0\\;\\Omega$ at $25.0^\\circ\\text{C}$. The same cell filled with a $0.0100\\text{ M}$ solution of potassium sulfate ($K_2SO_4$) has a resistance of $R_2 = 478.5\\;\\Omega$. Given that the specific conductivity of $0.0200\\text{ M}\\; KCl$ at $25.0^\\circ\\text{C}$ is $\\kappa = 0.2768\\text{ S/m}$, calculate: (a) the cell constant $K_{\\text{cell}}$, (b) the specific conductivity of the $K_2SO_4$ solution, and (c) the molar conductivity $\\Lambda_m$ of $K_2SO_4$.",
                "solution": """**Step 1: Determine the cell constant $K_{\\text{cell}}$**
Using the standard $KCl$ calibration data:
$$\\kappa_{KCl} = G_{KCl} \\cdot K_{\\text{cell}} = \\frac{K_{\\text{cell}}}{R_1}$$
$$K_{\\text{cell}} = \\kappa_{KCl} \\cdot R_1 = (0.2768\\text{ S/m}) \\times (432.0\\;\\Omega) = 119.578\\text{ m}^{-1} = 1.1958\\text{ cm}^{-1}$$

**Step 2: Calculate specific conductivity of $K_2SO_4$**
$$\\kappa_{K_2SO_4} = \\frac{K_{\\text{cell}}}{R_2} = \\frac{119.578\\text{ m}^{-1}}{478.5\\;\\Omega} = 0.24990\\text{ S/m} = 2.4990 \\times 10^{-3}\\text{ S/cm}$$

**Step 3: Calculate molar conductivity $\\Lambda_m$**
Concentration in SI units:
$$c = 0.0100\\text{ mol/L} = 10.00\\text{ mol/m}^3$$
$$\\Lambda_m = \\frac{\\kappa}{c} = \\frac{0.24990\\text{ S/m}}{10.00\\text{ mol/m}^3} = 0.024990\\text{ S}\\cdot\\text{m}^2\\text{/mol}$$

In conventional units:
$$\\Lambda_m = 0.024990 \\times 10^4 = 249.9\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$$"""
            },
            {
                "id": "p2-2",
                "title": "Limiting Conductivity and Dissociation Constant of Acetic Acid via Kohlrausch",
                "difficulty": "Medium",
                "statement": "At $298.15\\text{ K}$, the limiting molar conductivities are: $\\Lambda_m^\\circ(HCl) = 426.16\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$, $\\Lambda_m^\\circ(CH_3COONa) = 91.04\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$, and $\\Lambda_m^\\circ(NaCl) = 126.45\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$. For a $0.0500\\text{ M}$ solution of acetic acid ($CH_3COOH$), the measured molar conductivity is $\\Lambda_m = 7.36\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$. Calculate: (a) $\\Lambda_m^\\circ(CH_3COOH)$, (b) the degree of dissociation $\\alpha$, and (c) the acid dissociation constant $K_a$.",
                "solution": """**Step 1: Kohlrausch combination for $\\Lambda_m^\\circ(CH_3COOH)$**
$$\\Lambda_m^\\circ(CH_3COOH) = \\Lambda_m^\\circ(HCl) + \\Lambda_m^\\circ(CH_3COONa) - \\Lambda_m^\\circ(NaCl)$$
$$\\Lambda_m^\\circ(CH_3COOH) = 426.16 + 91.04 - 126.45 = 390.75\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$$

**Step 2: Degree of dissociation $\\alpha$**
$$\\alpha = \\frac{\\Lambda_m}{\\Lambda_m^\\circ} = \\frac{7.36}{390.75} = 0.018836 \\approx 1.884\\%$$

**Step 3: Dissociation constant $K_a$**
Using Ostwald's dilution law:
$$K_a = \\frac{c \\alpha^2}{1 - \\alpha} = \\frac{(0.0500) \\times (0.018836)^2}{1 - 0.018836} = \\frac{0.0500 \\times 3.5479 \\times 10^{-4}}{0.98116} = 1.808 \\times 10^{-5}\\text{ mol/L}$$
$$pK_a = -\\log_{10}(1.808 \\times 10^{-5}) = 4.743$$"""
            },
            {
                "id": "p2-3",
                "title": "Ionic Mobility and Hydrated Radius from Limiting Ionic Conductivity",
                "difficulty": "Medium",
                "statement": "The limiting molar ionic conductivity of the sulfate ion ($SO_4^{2-}$, $z = -2$) in water at $25.0^\\circ\\text{C}$ is $\\lambda^\\circ = 160.0\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$. The dynamic viscosity of water is $\\eta = 0.8903 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$. Calculate: (a) the ionic mobility $u(SO_4^{2-})$ in $\\text{m}^2/(\\text{V}\\cdot\\text{s})$, (b) the drift velocity under an electric field of $E = 150\\text{ V/m}$, and (c) the effective Stokes hydrated radius $r_{\\text{hyd}}$.",
                "solution": """**Step 1: Calculate ionic mobility $u$**
Convert $\\lambda^\\circ$ to SI units:
$$\\lambda^\\circ = 160.0 \\times 10^{-4}\\text{ S}\\cdot\\text{m}^2\\text{/mol} = 0.01600\\text{ S}\\cdot\\text{m}^2\\text{/mol}$$
Since $\\lambda^\\circ = |z| F u$:
$$u = \\frac{\\lambda^\\circ}{|z| F} = \\frac{0.01600}{2 \\times 96485.3} = \\frac{0.01600}{192970.6} = 8.2914 \\times 10^{-8}\\text{ m}^2/(\\text{V}\\cdot\\text{s})$$

**Step 2: Drift velocity under $E = 150\\text{ V/m}$**
$$v_{\\text{drift}} = u E = (8.2914 \\times 10^{-8}\\text{ m}^2/(\\text{V}\\cdot\\text{s})) \\times (150\\text{ V/m}) = 1.2437 \\times 10^{-5}\\text{ m/s} = 12.44\\;\\mu\\text{m/s}$$

**Step 3: Effective Stokes hydrated radius $r_{\\text{hyd}}$**
From Stokes' drag:
$$u = \\frac{|z| e}{6 \\pi \\eta r_{\\text{hyd}}} \\implies r_{\\text{hyd}} = \\frac{|z| e}{6 \\pi \\eta u}$$
$$r_{\\text{hyd}} = \\frac{2 \\times (1.6021766 \\times 10^{-19})}{6 \\pi \\times (0.8903 \\times 10^{-3}) \\times (8.2914 \\times 10^{-8})}$$
$$\\text{Denominator} = 18.8496 \\times (0.8903 \\times 10^{-3}) \\times (8.2914 \\times 10^{-8}) = 1.3915 \\times 10^{-9}$$
$$r_{\\text{hyd}} = \\frac{3.20435 \\times 10^{-19}}{1.3915 \\times 10^{-9}} = 2.303 \\times 10^{-10}\\text{ m} = 0.230\\text{ nm} = 2.30\\text{ Å}$$"""
            },
            {
                "id": "p2-4",
                "title": "Hittorf Transference Number Determination of Silver Nitrate",
                "difficulty": "Hard",
                "statement": "In a Hittorf experiment with silver electrodes, a $0.0500\\text{ M}\\; AgNO_3$ solution was electrolyzed. A silver coulometer in series deposited $0.1620\\text{ g}$ of silver on its cathode. After electrolysis, the anode compartment contained $25.13\\text{ g}$ of solution which yielded $0.2314\\text{ g}$ of silver upon analytical precipitation. Before electrolysis, $25.13\\text{ g}$ of the original solution contained $0.1856\\text{ g}$ of silver. Determine: (a) total charge passed in Faradays, (b) the transport number $t_+$ of $Ag^+$, and (c) the transport number $t_-$ of $NO_3^-$.",
                "solution": """**Step 1: Total charge passed in Faradays**
Molar mass of silver: $M(Ag) = 107.8682\\text{ g/mol}$.
Silver deposited in coulometer:
$$n(Ag)_{\\text{coul}} = \\frac{0.1620\\text{ g}}{107.8682\\text{ g/mol}} = 1.50183 \\times 10^{-3}\\text{ mol}$$
Total charge passed:
$$Q = 1.50183 \\times 10^{-3}\\text{ Faradays}$$

**Step 2: Silver balance in the anode compartment**
- Initial silver present in anode compartment:
  $$n(Ag)_{\\text{initial}} = \\frac{0.1856\\text{ g}}{107.8682\\text{ g/mol}} = 1.72062 \\times 10^{-3}\\text{ mol}$$
- Final silver present in anode compartment:
  $$n(Ag)_{\\text{final}} = \\frac{0.2314\\text{ g}}{107.8682\\text{ g/mol}} = 2.14521 \\times 10^{-3}\\text{ mol}$$
- Net increase in silver in anode compartment:
  $$\\Delta n(Ag) = 2.14521 \\times 10^{-3} - 1.72062 \\times 10^{-3} = 4.2459 \\times 10^{-4}\\text{ mol}$$

**Step 3: Transference number derivation**
At the silver anode, oxidation adds $Q/F$ moles of $Ag^+$:
$$n(Ag)_{\\text{added}} = 1.50183 \\times 10^{-3}\\text{ mol}$$
Meanwhile, $Ag^+$ cations migrate out toward the cathode:
$$n(Ag)_{\\text{migrated}} = t_+ \\frac{Q}{F}$$
The net increase in the anode compartment is:
$$\\Delta n(Ag) = \\frac{Q}{F} - t_+ \\frac{Q}{F} = (1 - t_+) \\frac{Q}{F} = t_- \\frac{Q}{F}$$

Therefore:
$$t_- = \\frac{\\Delta n(Ag)}{Q/F} = \\frac{4.2459 \\times 10^{-4}}{1.50183 \\times 10^{-3}} = 0.2827$$
$$t_+(Ag^+) = 1 - t_- = 1 - 0.2827 = 0.7173$$"""
            },
            {
                "id": "p2-5",
                "title": "Moving Boundary Transference Number Determination of Hydrochloric Acid",
                "difficulty": "Medium",
                "statement": "In a moving boundary apparatus with a capillary tube of internal radius $r = 1.05\\text{ mm}$, a $0.0200\\text{ M}$ solution of hydrochloric acid ($HCl$) is layered over $CdCl_2$. A constant current of $I = 2.50\\text{ mA}$ is passed for $t = 15.0\\text{ minutes}$, during which the $H^+/Cd^{2+}$ boundary moves a distance of $x = 7.42\\text{ cm}$. Calculate the transference number $t_+$ of $H^+$ and $t_-$ of $Cl^-$.",
                "solution": """**Step 1: Capillary cross-sectional area and swept volume**
$$r = 1.05 \\times 10^{-3}\\text{ m}$$
$$A = \\pi r^2 = \\pi (1.05 \\times 10^{-3})^2 = 3.4636 \\times 10^{-6}\\text{ m}^2$$
$$x = 7.42 \\times 10^{-2}\\text{ m}$$
Volume swept by boundary:
$$V = A x = (3.4636 \\times 10^{-6}\\text{ m}^2) \\times (7.42 \\times 10^{-2}\\text{ m}) = 2.5700 \\times 10^{-7}\\text{ m}^3 = 0.25700\\text{ cm}^3$$

**Step 2: Total charge passed**
$$I = 2.50 \\times 10^{-3}\\text{ A}$$
$$t = 15.0 \\times 60 = 900.0\\text{ s}$$
$$Q = I t = (2.50 \\times 10^{-3}) \\times 900.0 = 2.250\\text{ C}$$

**Step 3: Calculate transference number $t_+$**
Concentration of $HCl$:
$$c = 0.0200\\text{ mol/L} = 20.00\\text{ mol/m}^3$$
Number of moles of $H^+$ displaced:
$$n(H^+) = c V = 20.00 \\times (2.5700 \\times 10^{-7}) = 5.1400 \\times 10^{-6}\\text{ mol}$$

Charge carried by $H^+$:
$$Q_+ = n(H^+) F = (5.1400 \\times 10^{-6}\\text{ mol}) \\times (96485.3\\text{ C/mol}) = 0.49593\\text{ C}$$

Transport number:
$$t_+(H^+) = \\frac{Q_+}{Q} = \\frac{0.49593}{2.250} = 0.8204$$
$$t_-(Cl^-) = 1 - t_+(H^+) = 1 - 0.8204 = 0.1796$$

This verifies that the anomalous Grotthuss proton hopping carries over $82\\%$ of the total current in dilute $HCl$."""
            },
            {
                "id": "p2-6",
                "title": "Debye-Hückel-Onsager Theoretical Slope for Sodium Chloride",
                "difficulty": "Hard",
                "statement": "For aqueous $NaCl$ at $25.0^\\circ\\text{C}$, $\\Lambda_m^\\circ = 126.45\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$. Using the Debye-Hückel-Onsager constants for water ($A = 60.20\\text{ S}\\cdot\\text{cm}^2\\text{/mol}\\cdot(\\text{L/mol})^{1/2}$, $B = 0.229\\;(\\text{L/mol})^{1/2}$): (a) calculate the theoretical Onsager slope $S$, (b) predict the molar conductivity at $c = 0.00500\\text{ M}$, and (c) calculate the percent deviation from experimental $\\Lambda_m = 120.65\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$.",
                "solution": """**Step 1: Calculate the theoretical Onsager slope $S$**
$$\\Lambda_m = \\Lambda_m^\\circ - S \\sqrt{c}$$
where $S = A + B \\Lambda_m^\\circ$.
$$S = 60.20 + 0.229 \\times 126.45 = 60.20 + 28.957 = 89.157\\text{ S}\\cdot\\text{cm}^2\\text{/mol}\\cdot(\\text{L/mol})^{1/2}$$

**Step 2: Predict molar conductivity at $c = 0.00500\\text{ M}$**
$$\\sqrt{c} = \\sqrt{0.00500} = 0.070711\\;(\\text{mol/L})^{1/2}$$
$$\\Delta \\Lambda_m = S \\sqrt{c} = 89.157 \\times 0.070711 = 6.304\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$$
$$\\Lambda_m(\\text{pred}) = \\Lambda_m^\\circ - \\Delta \\Lambda_m = 126.45 - 6.304 = 120.146\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$$

**Step 3: Percent deviation from experimental value**
$$\\text{Error} = \\frac{|120.146 - 120.65|}{120.65} \\times 100\\% = \\frac{0.504}{120.65} \\times 100\\% = 0.418\\%$$
The Debye-Hückel-Onsager equation predicts conductivity within $0.42\\%$ of experiment."""
            },
            {
                "id": "p2-7",
                "title": "Solvent Viscosity and Walden Product Across Polar Media",
                "difficulty": "Hard",
                "statement": "The tetraethylammonium ion ($Et_4N^+$) has a limiting molar ionic conductivity of $\\lambda^\\circ = 32.66\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$ in water at $25^\\circ\\text{C}$ ($\\eta_1 = 0.8903\\text{ cP}$). In acetonitrile ($CH_3CN$, $\\eta_2 = 0.345\\text{ cP}$), calculate: (a) the Walden product $\\lambda^\\circ \\eta$, (b) the predicted $\\lambda^\\circ(Et_4N^+)$ in acetonitrile, and (c) the effective hydrodynamic radius $r_{\\text{hyd}}$ from Stokes' law.",
                "solution": """**Step 1: Calculate the Walden product in water**
Convert viscosity:
$$\\eta_1 = 0.8903\\text{ cP} = 0.8903 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$$
$$\\text{Walden Product } \\mathcal{W} = \\lambda^\\circ \\eta_1 = 32.66\\text{ S}\\cdot\\text{cm}^2\\text{/mol} \\times 0.8903\\text{ cP} = 29.077\\text{ S}\\cdot\\text{cm}^2\\text{cP/mol}$$

In SI units:
$$\\lambda^\\circ = 32.66 \\times 10^{-4} = 3.266 \\times 10^{-3}\\text{ S}\\cdot\\text{m}^2\\text{/mol}$$
$$\\mathcal{W}_{SI} = (3.266 \\times 10^{-3}) \\times (0.8903 \\times 10^{-3}) = 2.9077 \\times 10^{-6}\\text{ N}\\cdot\\text{s}/(\\text{V}\\cdot\\text{mol})$$

**Step 2: Predict $\\lambda^\\circ$ in acetonitrile**
Using Walden's rule $\\lambda_2^\\circ \\eta_2 = \\lambda_1^\\circ \\eta_1$:
$$\\lambda_2^\\circ = \\frac{\\mathcal{W}}{\\eta_2} = \\frac{29.077}{0.345} = 84.28\\text{ S}\\cdot\\text{cm}^2\\text{/mol}$$
Because acetonitrile is less viscous than water, the ionic conductivity increases by a factor of $2.58$.

**Step 3: Effective hydrodynamic radius $r_{\\text{hyd}}$**
$$r_{\\text{hyd}} = \\frac{|z| F^2}{6 \\pi N_A \\mathcal{W}_{SI}} = \\frac{1 \\times (96485.3)^2}{6 \\pi \\times (6.02214 \\times 10^{23}) \\times (2.9077 \\times 10^{-6})}$$
$$\\text{Numerator} = 9.30941 \\times 10^9$$
$$\\text{Denominator} = 18.8496 \\times 6.02214 \\times 10^{23} \\times 2.9077 \\times 10^{-6} = 3.3007 \\times 10^{19}$$
$$r_{\\text{hyd}} = \\frac{9.30941 \\times 10^9}{3.3007 \\times 10^{19}} = 2.820 \\times 10^{-10}\\text{ m} = 0.282\\text{ nm} = 2.82\\text{ Å}$$"""
            }
        ]
    }
    units.append(u2)

    # =========================================================================
    # UNIT 3: Diffusion Phenomena & Brownian Motion
    # =========================================================================
    u3 = {
        "id": "unit-3",
        "unitNumber": 3,
        "title": "Unit 3: Diffusion Phenomena & Brownian Motion",
        "leadSummary": "Thermodynamics and continuum mechanics of diffusion: chemical potential gradients as thermodynamic driving forces, Fick's first and second laws in multidimensional geometries, error-function and Gaussian solutions to non-steady-state diffusion, the Einstein-Smoluchowski random walk model, Langevin stochastic mechanics, and membrane permeability transport.",
        "simulations": ["sim_kin_fick_diffusion_brownian_walk"],
        "sections": [
            {
                "id": "sec-3-1",
                "secNumber": "3.1",
                "title": "Thermodynamic Driving Force of Diffusion: Chemical Potential Gradients",
                "content": """Diffusion is fundamentally a thermodynamic process driven by the minimization of Gibbs free energy, rather than a purely mechanical concentration effect.

### Chemical Potential Gradient as Generalized Force
For a solute species $i$ in solution, the chemical potential $\\mu_i$ is given by:
$$\\mu_i = \\mu_i^\\circ + R T \\ln a_i = \\mu_i^\\circ + R T \\ln(\\gamma_i c_i)$$
where $a_i$ is activity, $\\gamma_i$ is the activity coefficient, and $c_i$ is concentration.

The thermodynamic force $F_{\\text{therm}}$ acting on a single molecule is the negative spatial gradient of chemical potential per particle:
$$F_{\\text{therm}} = -\\frac{1}{N_A} \\frac{\\partial \\mu_i}{\\partial x} = -\\frac{k_B T}{a_i} \\frac{\\partial a_i}{\\partial x} = -k_B T \\left( \\frac{\\partial \\ln a_i}{\\partial x} \\right)$$

For an ideal solution ($\\gamma_i = 1$, $a_i = c_i$):
$$F_{\\text{therm}} = -\\frac{k_B T}{c_i} \\frac{\\partial c_i}{\\partial x}$$

### Terminal Drift Velocity and Flux
Under this thermodynamic force, solute molecules acquire a terminal drift velocity $v_{\\text{drift}}$ balanced by the Stokes hydrodynamic friction coefficient $f$:
$$v_{\\text{drift}} = \\frac{F_{\\text{therm}}}{f} = -\\frac{k_B T}{f c_i} \\frac{\\partial c_i}{\\partial x}$$

The macroscopic molar diffusion flux $J$ (moles passing through unit area per unit time) is the product of concentration and velocity:
$$J = c_i v_{\\text{drift}} = c_i \\left( -\\frac{k_B T}{f c_i} \\frac{\\partial c_i}{\\partial x} \\right) = -\\left( \\frac{k_B T}{f} \\right) \\frac{\\partial c_i}{\\partial x}$$

Comparing with Fick's First Law $J = -D \\frac{\\partial c_i}{\\partial x}$ yields the **Stokes-Einstein Relation**:
$$D = \\frac{k_B T}{f} = \\frac{k_B T}{6 \\pi \\eta r_{\\text{hyd}}}$$
This links macroscopic diffusion directly to molecular thermal agitation $k_B T$ and solvent viscosity $\\eta$."""
            },
            {
                "id": "sec-3-2",
                "secNumber": "3.2",
                "title": "Fick's First Law of Steady-State Diffusion & Permeation Flux",
                "content": """Adolf Fick (1855) formulated the phenomenological laws of diffusion by drawing a direct mathematical analogy to Fourier's law of heat conduction and Ohm's law of electrical conduction.

### Statement of Fick's First Law
In a one-dimensional isotropic medium, the diffusion flux $J_x$ (amount of substance crossing a unit area perpendicular to the $x$-axis per unit time) is proportional to the negative spatial concentration gradient:
$$J_x = -D \\frac{\\partial c}{\\partial x}$$
where:
- $J_x$ is diffusion flux (SI: $\\text{mol}/(\\text{m}^2\\cdot\\text{s})$ or $\\text{kg}/(\\text{m}^2\\cdot\\text{s})$).
- $D$ is the diffusion coefficient (SI: $\\text{m}^2\\text{/s}$ or $\\text{cm}^2\\text{/s}$).
- $\\frac{\\partial c}{\\partial x}$ is the concentration gradient (SI: $\\text{mol/m}^4$).

The negative sign signifies that mass transport proceeds spontaneously from regions of higher chemical potential/concentration to regions of lower concentration.

### General Vector Formulation
In three dimensions:
$$\\vec{J} = -D \\nabla c = -D \\left( \\frac{\\partial c}{\\partial x} \\hat{i} + \\frac{\\partial c}{\\partial y} \\hat{j} + \\frac{\\partial c}{\\partial z} \\hat{k} \\right)$$

For anisotropic media (e.g., layered crystals, stretched polymers), $D$ is a second-rank tensor:
$$J_i = -\\sum_{j=1}^3 D_{ij} \\frac{\\partial c}{\\partial x_j}$$

### Steady-State Diffusion Through a Membrane
Under steady-state conditions, $\\frac{\\partial c}{\\partial t} = 0$, meaning the flux $J$ is uniform across a planar membrane of thickness $L$ separated by constant concentrations $c_1$ and $c_2$:
$$\\frac{dc}{dx} = \\frac{c_2 - c_1}{L} \\implies J = -D \\frac{c_2 - c_1}{L} = D \\frac{c_1 - c_2}{L}$$

Introducing the membrane partition coefficient $K = c_{\\text{mem}} / c_{\\text{aq}}$ and membrane permeability $P_{\\text{perm}} = \\frac{K D}{L}$:
$$J = P_{\\text{perm}} \\Delta c$$"""
            },
            {
                "id": "sec-3-3",
                "secNumber": "3.3",
                "title": "Fick's Second Law of Non-Steady-State Diffusion & Continuity Equation",
                "content": """When concentration varies with both position and time, mass conservation dictates non-steady-state diffusion.

### Derivation from the Continuity Equation
Consider a volume element $\\Delta V = A \\Delta x$ between planes at $x$ and $x + \\Delta x$. The rate of accumulation of solute in this volume element is:
$$\\frac{\\partial n}{\\partial t} = A \\Delta x \\frac{\\partial c}{\\partial t}$$

Mass conservation requires that accumulation equals the net inflow minus outflow across the boundary planes:
$$\\frac{\\partial n}{\\partial t} = A J_x(x) - A J_x(x + \\Delta x)$$

Dividing by $A \\Delta x$ and taking the limit $\\Delta x \\to 0$:
$$\\frac{\\partial c}{\\partial t} = -\\frac{\\partial J_x}{\\partial x}$$
This is the **Continuity Equation** for diffusion.

Substituting Fick's first law $J_x = -D \\frac{\\partial c}{\\partial x}$:
$$\\frac{\\partial c}{\\partial t} = -\\frac{\\partial}{\\partial x} \\left( -D \\frac{\\partial c}{\\partial x} \\right)$$

If the diffusion coefficient $D$ is independent of concentration (dilute regime):
$$\\frac{\\partial c}{\\partial t} = D \\frac{\\partial^2 c}{\\partial x^2}$$
This is **Fick's Second Law of Diffusion** (the classic parabolic diffusion equation).

### Multi-Dimensional Geometries
1. **Three-Dimensional Cartesian**:
   $$\\frac{\\partial c}{\\partial t} = D \\nabla^2 c = D \\left( \\frac{\\partial^2 c}{\\partial x^2} + \\frac{\\partial^2 c}{\\partial y^2} + \\frac{\\partial^2 c}{\\partial z^2} \\right)$$
2. **Cylindrical Coordinates** (radial symmetry):
   $$\\frac{\\partial c}{\\partial t} = D \\left( \\frac{\\partial^2 c}{\\partial r^2} + \\frac{1}{r} \\frac{\\partial c}{\\partial r} \\right) = \\frac{D}{r} \\frac{\\partial}{\\partial r} \\left( r \\frac{\\partial c}{\\partial r} \\right)$$
3. **Spherical Coordinates** (radial symmetry):
   $$\\frac{\\partial c}{\\partial t} = D \\left( \\frac{\\partial^2 c}{\\partial r^2} + \\frac{2}{r} \\frac{\\partial c}{\\partial r} \\right) = \\frac{D}{r^2} \\frac{\\partial}{\\partial r} \\left( r^2 \\frac{\\partial c}{\\partial r} \\right)$$"""
            },
            {
                "id": "sec-3-4",
                "secNumber": "3.4",
                "title": "Analytical Solutions to the Diffusion Equation: Error Functions & Gaussian Spreading",
                "content": """Analytical solutions to Fick's second law depend on initial and boundary conditions.

### 1. Instantaneous Planar Source (Gaussian Spreading)
Consider an infinitesimal sheet at $x = 0$ containing $N_0$ moles of solute per unit area injected at $t = 0$ into an infinite medium ($-\\infty < x < \\infty$):
$$c(x, 0) = N_0 \\delta(x)$$

The fundamental solution (Green's function) of $\\frac{\\partial c}{\\partial t} = D \\frac{\\partial^2 c}{\\partial x^2}$ is a spreading Gaussian:
$$c(x, t) = \\frac{N_0}{\\sqrt{4 \\pi D t}} \\exp\\left( -\\frac{x^2}{4 D t} \\right)$$

Key features:
- Standard deviation of the spreading profile is $\\sigma(t) = \\sqrt{2 D t}$.
- Peak concentration at the center $x = 0$ decays as $c(0, t) = \\frac{N_0}{\\sqrt{4 \\pi D t}} \\propto t^{-1/2}$.

### 2. Semi-Infinite Medium with Constant Surface Concentration (Error Function)
Consider a semi-infinite medium ($x \\ge 0$) initially at uniform concentration $c_0$, whose surface at $x = 0$ is held at fixed concentration $c_s$ for all $t > 0$:
$$c(x, 0) = c_0 \\quad (x > 0); \\quad c(0, t) = c_s \\quad (t > 0); \\quad c(\\infty, t) = c_0$$

Using the similarity variable $\\eta = \\frac{x}{\\sqrt{4 D t}}$, the partial differential equation reduces to an ordinary differential equation:
$$\\frac{d^2 c}{d\\eta^2} + 2 \\eta \\frac{dc}{d\\eta} = 0$$

Integrating yields the solution in terms of the **Gauss error function** ($\\text{erf}$):
$$\\frac{c(x, t) - c_0}{c_s - c_0} = 1 - \\text{erf}\\left( \\frac{x}{2 \\sqrt{D t}} \\right) = \\text{erfc}\\left( \\frac{x}{2 \\sqrt{D t}} \\right)$$
where:
$$\\text{erf}(z) = \\frac{2}{\\sqrt{\\pi}} \\int_0^z e^{-u^2} du, \\quad \\text{erfc}(z) = 1 - \\text{erf}(z)$$

The penetration depth where concentration reaches halfway ($c = \\frac{c_s + c_0}{2}$) occurs at $z \\approx 0.4769$:
$$x_{1/2} \\approx \\sqrt{D t}$$"""
            },
            {
                "id": "sec-3-5",
                "secNumber": "3.5",
                "title": "Einstein-Smoluchowski Random Walk Model & Mean Squared Displacement",
                "content": """In 1905, Albert Einstein and Marian Smoluchowski established that macroscopic diffusion is the statistical ensemble manifestation of microscopic Brownian motion.

### Discrete One-Dimensional Random Walk
Consider a particle starting at the origin $x = 0$ at $t = 0$. In each discrete time step $\\tau$, the particle steps a distance $\\pm \\lambda$ with equal probability $p = 1/2$.
After $N$ steps (time $t = N \\tau$), the particle's position is:
$$x_N = \\sum_{i=1}^N \\Delta x_i, \\quad \\text{where } \\Delta x_i = \\pm \\lambda$$

The average displacement is zero due to symmetry:
$$\\langle x_N \\rangle = \\sum_{i=1}^N \\langle \\Delta x_i \\rangle = 0$$

The mean squared displacement (MSD) is:
$$\\langle x_N^2 \\rangle = \\left\\langle \\left( \\sum_{i=1}^N \\Delta x_i \\right)^2 \\right\\rangle = \\sum_{i=1}^N \\langle \\Delta x_i^2 \\rangle + 2 \\sum_{i < j} \\langle \\Delta x_i \\Delta x_j \\rangle$$

Because successive steps are statistically uncorrelated, $\\langle \\Delta x_i \\Delta x_j \\rangle = 0$ for $i \\neq j$, and $\\langle \\Delta x_i^2 \\rangle = \\lambda^2$:
$$\\langle x_N^2 \\rangle = N \\lambda^2 = \\left( \\frac{t}{\\tau} \\right) \\lambda^2 = \\left( \\frac{\\lambda^2}{\\tau} \\right) t$$

### Connection to Fick's Second Law
In the continuum limit ($\\lambda \\to 0, \\tau \\to 0$ such that $\\frac{\\lambda^2}{2\\tau} = D$):
$$\\langle x^2 \\rangle = 2 D t$$

In three dimensions, with independent motion along $x, y, z$:
$$\\langle r^2 \\rangle = \\langle x^2 \\rangle + \\langle y^2 \\rangle + \\langle z^2 \\rangle = 2 D t + 2 D t + 2 D t = 6 D t$$

This is the celebrated **Einstein-Smoluchowski equation**:
$$\\langle r^2 \\rangle = 6 D t = \\frac{k_B T}{\\pi \\eta r_{\\text{hyd}}} t$$
Jean Perrin used this equation in 1908 to track the Brownian motion of colloidal mastic particles, experimentally calculating Avogadro's number $N_A$ and confirming the physical reality of atoms."""
            },
            {
                "id": "sec-3-6",
                "secNumber": "3.6",
                "title": "Langevin Stochastic Mechanics & Velocity Autocorrelation Functions",
                "content": """Paul Langevin (1908) formulated the first dynamical equation for Brownian motion by separating the total force on a particle into a systematic friction term and a fluctuating stochastic force.

### The Langevin Equation
For a Brownian particle of mass $m$ and velocity $v(t)$:
$$m \\frac{dv}{dt} = -\\gamma v(t) + R(t)$$
where:
- $-\\gamma v(t)$ is the macroscopic frictional drag ($\\gamma = 6 \\pi \\eta r$).
- $R(t)$ is the fluctuating, zero-mean stochastic Gaussian white noise representing instantaneous molecular impacts from the solvent.

Properties of $R(t)$:
1. $\\langle R(t) \\rangle = 0$.
2. $\\langle R(t) R(t') \\rangle = 2 \\gamma k_B T \\delta(t - t')$ (Fluctuation-Dissipation Theorem).

### Velocity Autocorrelation Function (VACF)
Multiplying by $v(0)$ and ensemble averaging:
$$\\frac{d}{dt} \\langle v(t) v(0) \\rangle = -\\frac{\\gamma}{m} \\langle v(t) v(0) \\rangle$$
Integrating yields an exponential decay with momentum relaxation time $\\tau_m = m / \\gamma$:
$$\\langle v(t) v(0) \\rangle = \\langle v(0)^2 \\rangle \\exp\\left( -\\frac{t}{\\tau_m} \\right) = \\frac{k_B T}{m} \\exp\\left( -\\frac{\\gamma t}{m} \\right)$$

### Green-Kubo Formula for Diffusion
The diffusion coefficient is the time integral of the velocity autocorrelation function:
$$D = \\int_0^\\infty \\langle v(t) v(0) \\rangle dt = \\frac{k_B T}{m} \\int_0^\\infty \\exp\\left( -\\frac{\\gamma t}{m} \\right) dt = \\frac{k_B T}{m} \\left( \\frac{m}{\\gamma} \\right) = \\frac{k_B T}{\\gamma}$$
recovering the Stokes-Einstein relation from microscopic stochastic dynamics."""
            },
            {
                "id": "sec-3-7",
                "secNumber": "3.7",
                "title": "Membrane Transport, Osmotic Diffusion & Donnan Equilibrium Dynamics",
                "content": """Transport across biological and synthetic semipermeable membranes couples concentration diffusion with electrical potential gradients and osmotic pressure.

### Osmotic Flux & Kedem-Katchalsky Formalism
When a membrane separates a pure solvent from a solution containing non-permeating solute, chemical potential equality across the membrane establishes an osmotic pressure $\\Pi$:
$$\\Pi = i c R T$$
(van 't Hoff equation).

Under combined hydrostatic pressure difference $\\Delta P$ and osmotic pressure difference $\\Delta \\Pi$, the total volume flux $J_v$ is:
$$J_v = L_p (\\Delta P - \\sigma_{\\text{ref}} \\Delta \\Pi)$$
where:
- $L_p$ is the hydraulic permeability coefficient.
- $\\sigma_{\\text{ref}}$ is the Staverman reflection coefficient ($0 \\le \\sigma_{\\text{ref}} \\le 1$; $\\sigma_{\\text{ref}} = 1$ for a completely impermeable solute).

The solute flux $J_s$ across the membrane is:
$$J_s = \\omega \\Delta \\Pi + (1 - \\sigma_{\\text{ref}}) \\bar{c}_s J_v$$
where $\\omega$ is the solute permeability coefficient and $\\bar{c}_s$ is the mean intra-membrane solute concentration.

### Donnan Equilibrium
When a semipermeable membrane separates an electrolyte solution containing an impermeable macromolecular poly-ion (e.g., protein $P^{z-}$ with $Na^+$ counterions) on side 1 from diffusible $NaCl$ on side 2, electrochemical equilibrium for diffusible $Na^+$ and $Cl^-$ requires:
$$\\mu_{Na^+, 1} + \\mu_{Cl^-, 1} = \\mu_{Na^+, 2} + \\mu_{Cl^-, 2}$$

Assuming unit activity coefficients:
$$[Na^+]_1 [Cl^-]_1 = [Na^+]_2 [Cl^-]_2$$

Electroneutrality demands:
- Side 1: $[Na^+]_1 = [Cl^-]_1 + z [P^{z-}]_1$
- Side 2: $[Na^+]_2 = [Cl^-]_2 = c$

Because $[Na^+]_1 > [Cl^-]_1$, substitution shows:
$$[Na^+]_1 > c > [Cl^-]_1$$
The presence of non-diffusible poly-ions forces an asymmetric distribution of small mobile ions, producing a permanent transmembrane electric potential: the **Donnan Potential**:
$$\\Delta \\phi = \\phi_1 - \\phi_2 = -\\frac{R T}{F} \\ln\\left( \\frac{[Na^+]_1}{[Na^+]_2} \\right) = \\frac{R T}{F} \\ln\\left( \\frac{[Cl^-]_1}{[Cl^-]_2} \\right)$$"""
            }
        ],
        "problems": [
            {
                "id": "p3-1",
                "title": "Stokes-Einstein Diffusion Coefficient of Sucrose in Aqueous Solution",
                "difficulty": "Easy",
                "statement": "Sucrose ($C_{12}H_{22}O_{11}$) has an effective hydrodynamic radius of $r_{\\text{hyd}} = 0.520\\text{ nm}$. The viscosity of water is $\\eta = 0.8903 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$ at $T = 298.15\\text{ K}$. Calculate: (a) the diffusion coefficient $D$ of sucrose in water, (b) the root-mean-square displacement $\\sqrt{\\langle x^2 \\rangle}$ along one dimension after $t = 1.00\\text{ hour}$, and (c) after $t = 24.0\\text{ hours}$.",
                "solution": """**Step 1: Calculate diffusion coefficient $D$**
Using the Stokes-Einstein relation:
$$D = \\frac{k_B T}{6 \\pi \\eta r_{\\text{hyd}}}$$
$$k_B T = (1.380649 \\times 10^{-23}\\text{ J/K}) \\times (298.15\\text{ K}) = 4.1164 \\times 10^{-21}\\text{ J}$$
$$\\text{Denominator} = 6 \\pi \\times (0.8903 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}) \\times (0.520 \\times 10^{-9}\\text{ m}) = 8.7251 \\times 10^{-12}\\text{ kg/s}$$
$$D = \\frac{4.1164 \\times 10^{-21}}{8.7251 \\times 10^{-12}} = 4.7179 \\times 10^{-10}\\text{ m}^2/\\text{s} = 4.72 \\times 10^{-6}\\text{ cm}^2/\\text{s}$$

**Step 2: RMS displacement after $t = 1.00\\text{ hour}$**
$$t_1 = 3600\\text{ s}$$
$$\\sqrt{\\langle x^2 \\rangle} = \\sqrt{2 D t_1} = \\sqrt{2 \\times (4.7179 \\times 10^{-10}) \\times 3600} = \\sqrt{3.3969 \\times 10^{-6}} = 1.843 \\times 10^{-3}\\text{ m} = 1.84\\text{ mm}$$

**Step 3: RMS displacement after $t = 24.0\\text{ hours}$**
$$t_2 = 24 \\times 3600 = 86400\\text{ s}$$
$$\\sqrt{\\langle x^2 \\rangle} = \\sqrt{2 D t_2} = \\sqrt{\\langle x_1^2 \\rangle} \\times \\sqrt{24} = 1.843 \\times 4.8990 = 9.03\\text{ mm}$$

Notice that while time increases by a factor of $24$, diffusion displacement increases only by $\\sqrt{24} \\approx 4.90$."""
            },
            {
                "id": "p3-2",
                "title": "Gaussian Concentration Spreading from an Instantaneous Thin-Film Source",
                "difficulty": "Medium",
                "statement": "A radioactive tracer pulse of $N_0 = 5.00 \\times 10^{-3}\\text{ mol/m}^2$ of gold is deposited on the surface of a semi-infinite copper bar at $x = 0$. The diffusion coefficient of gold in copper at $T = 1000\\text{ K}$ is $D = 1.20 \\times 10^{-14}\\text{ m}^2/\\text{s}$. Calculate: (a) the peak concentration at $x = 0$ after annealing for $t = 10.0\\text{ hours}$, and (b) the concentration at depth $x = 20.0\\;\\mu\\text{m}$.",
                "solution": """**Step 1: Formula for semi-infinite instantaneous source**
For a semi-infinite medium ($x \\ge 0$) with an impermeable boundary at $x = 0$, all mass remains in $x \\ge 0$, reflecting the Gaussian:
$$c(x, t) = \\frac{N_0}{\\sqrt{\\pi D t}} \\exp\\left( -\\frac{x^2}{4 D t} \\right)$$

**Step 2: Evaluate constants after $t = 10.0\\text{ hours}$**
$$t = 10.0 \\times 3600 = 36000\\text{ s}$$
$$D t = (1.20 \\times 10^{-14}\\text{ m}^2/\\text{s}) \\times 36000\\text{ s} = 4.320 \\times 10^{-10}\\text{ m}^2$$
$$4 D t = 1.728 \\times 10^{-9}\\text{ m}^2$$
$$\\sqrt{\\pi D t} = \\sqrt{\\pi \\times 4.320 \\times 10^{-10}} = \\sqrt{1.35717 \\times 10^{-9}} = 3.6840 \\times 10^{-5}\\text{ m}$$

**Step 3: Surface concentration ($x = 0$)**
$$c(0, t) = \\frac{N_0}{\\sqrt{\\pi D t}} = \\frac{5.00 \\times 10^{-3}\\text{ mol/m}^2}{3.6840 \\times 10^{-5}\\text{ m}} = 135.72\\text{ mol/m}^3 = 0.1357\\text{ M}$$

**Step 4: Concentration at $x = 20.0\\;\\mu\\text{m} = 2.00 \\times 10^{-5}\\text{ m}$**
$$x^2 = (2.00 \\times 10^{-5})^2 = 4.00 \\times 10^{-10}\\text{ m}^2$$
$$\\frac{x^2}{4 D t} = \\frac{4.00 \\times 10^{-10}}{1.728 \\times 10^{-9}} = 0.23148$$
$$\\exp(-0.23148) = 0.79336$$
$$c(20\\;\\mu\\text{m}, t) = 135.72 \\times 0.79336 = 107.68\\text{ mol/m}^3 = 0.1077\\text{ M}$$"""
            },
            {
                "id": "p3-3",
                "title": "Carbon Carburization Depth via Error Function Solution",
                "difficulty": "Hard",
                "statement": "Low-carbon steel containing $0.200\\text{ wt}\\%$ carbon is carburized in a gas atmosphere maintaining a constant surface concentration of $c_s = 1.200\\text{ wt}\\%$ carbon at $T = 950^\\circ\\text{C}$. The diffusion coefficient of carbon in austenite is $D = 1.28 \\times 10^{-11}\\text{ m}^2/\\text{s}$. (a) Calculate the time required to achieve a carbon concentration of $0.600\\text{ wt}\\%$ at a depth of $x = 1.00\\text{ mm}$. Given: $\\text{erf}(0.600) = 0.6039$, $\\text{erf}(0.595) = 0.6000$.",
                "solution": """**Step 1: Set up the error function equation**
$$c(x, t) = c_s - (c_s - c_0) \\text{erf}\\left( \\frac{x}{2 \\sqrt{D t}} \\right)$$
$$\\frac{c(x, t) - c_s}{c_0 - c_s} = \\text{erf}\\left( \\frac{x}{2 \\sqrt{D t}} \\right)$$
$$\\frac{0.600 - 1.200}{0.200 - 1.200} = \\frac{-0.600}{-1.000} = 0.6000$$

Thus:
$$\\text{erf}\\left( \\frac{x}{2 \\sqrt{D t}} \\right) = 0.6000$$

**Step 2: Invert the error function**
From the provided data:
$$\\text{erf}(z) = 0.6000 \\implies z = 0.595$$
$$\\frac{x}{2 \\sqrt{D t}} = 0.595$$

**Step 3: Solve for carburization time $t$**
$$x = 1.00\\text{ mm} = 1.00 \\times 10^{-3}\\text{ m}$$
$$2 \\sqrt{D t} = \\frac{x}{0.595} = \\frac{1.00 \\times 10^{-3}}{0.595} = 1.68067 \\times 10^{-3}\\text{ m}$$
$$\\sqrt{D t} = 8.40336 \\times 10^{-4}\\text{ m}$$
$$D t = (8.40336 \\times 10^{-4})^2 = 7.06165 \\times 10^{-7}\\text{ m}^2$$

$$t = \\frac{7.06165 \\times 10^{-7}\\text{ m}^2}{1.28 \\times 10^{-11}\\text{ m}^2/\\text{s}} = 55169\\text{ s}$$

Converting to hours:
$$t = \\frac{55169}{3600} = 15.32\\text{ hours}$$"""
            },
            {
                "id": "p3-4",
                "title": "Colloidal Particle Size Determination via Brownian Motion Statistics",
                "difficulty": "Medium",
                "statement": "In a modern video microscopy experiment replicating Jean Perrin's work, spherical gold nanoparticles are tracked in water at $T = 293.15\\text{ K}$ ($\\eta = 1.002 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$). The observed two-dimensional mean squared displacement over an observation interval of $\\Delta t = 2.00\\text{ s}$ is $\\langle r_{2D}^2 \\rangle = 1.76 \\times 10^{-12}\\text{ m}^2$. Calculate: (a) the diffusion coefficient $D$, and (b) the hydrodynamic radius $r$ of the nanoparticles.",
                "solution": """**Step 1: Relate 2D mean squared displacement to diffusion coefficient**
In two dimensions:
$$\\langle r_{2D}^2 \\rangle = \\langle x^2 \\rangle + \\langle y^2 \\rangle = 2 D \\Delta t + 2 D \\Delta t = 4 D \\Delta t$$

Solving for $D$:
$$D = \\frac{\\langle r_{2D}^2 \\rangle}{4 \\Delta t} = \\frac{1.76 \\times 10^{-12}\\text{ m}^2}{4 \\times 2.00\\text{ s}} = 2.20 \\times 10^{-13}\\text{ m}^2/\\text{s}$$

**Step 2: Hydrodynamic radius via Stokes-Einstein equation**
$$D = \\frac{k_B T}{6 \\pi \\eta r} \\implies r = \\frac{k_B T}{6 \\pi \\eta D}$$
$$k_B T = (1.380649 \\times 10^{-23}) \\times (293.15) = 4.04737 \\times 10^{-21}\\text{ J}$$
$$\\text{Denominator} = 6 \\pi \\times (1.002 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}) \\times (2.20 \\times 10^{-13}\\text{ m}^2/\\text{s}) = 4.1551 \\times 10^{-15}\\text{ N}$$
$$r = \\frac{4.04737 \\times 10^{-21}}{4.1551 \\times 10^{-15}} = 9.7407 \\times 10^{-7}\\text{ m} = 974\\text{ nm} = 0.974\\;\\mu\\text{m}$$"""
            },
            {
                "id": "p3-5",
                "title": "Donnan Membrane Potential and Mobile Ion Asymmetry",
                "difficulty": "Hard",
                "statement": "A rigid semipermeable membrane separates two aqueous compartments of equal volume at $T = 298.15\\text{ K}$. Compartment 1 contains a non-diffusible poly-anion protein $Na_{10}P$ at concentration $c_p = 0.0100\\text{ M}$ (completely dissociated into $10\\; Na^+$ and $1\\; P^{10-}$). Compartment 2 initially contains $NaCl$ at concentration $c_s = 0.1000\\text{ M}$. At Donnan equilibrium: (a) calculate the equilibrium concentrations of $Na^+$ and $Cl^-$ in both compartments, (b) calculate the Donnan membrane electrical potential $\\Delta \\phi = \\phi_1 - \\phi_2$.",
                "solution": """**Step 1: Set up equilibrium variables and electroneutrality**
Let $x$ moles/L of $NaCl$ diffuse from compartment 2 into compartment 1.
Initial state:
- Compartment 1: $[Na^+]_{1, \\text{init}} = 10 c_p = 0.100\\text{ M}$, $[P^{10-}]_1 = 0.0100\\text{ M}$, $[Cl^-]_{1, \\text{init}} = 0$.
- Compartment 2: $[Na^+]_{2, \\text{init}} = 0.100\\text{ M}$, $[Cl^-]_{2, \\text{init}} = 0.100\\text{ M}$.

Equilibrium state:
- Compartment 1: $[Na^+]_1 = 0.100 + x$, $[Cl^-]_1 = x$.
- Compartment 2: $[Na^+]_2 = 0.100 - x$, $[Cl^-]_2 = 0.100 - x$.

**Step 2: Donnan product condition**
$$[Na^+]_1 [Cl^-]_1 = [Na^+]_2 [Cl^-]_2$$
$$(0.100 + x) x = (0.100 - x)^2$$
$$0.100 x + x^2 = 0.0100 - 0.200 x + x^2$$
$$0.100 x = 0.0100 - 0.200 x \\implies 0.300 x = 0.0100$$
$$x = \\frac{0.0100}{0.300} = 0.03333\\text{ M}$$

**Step 3: Evaluate equilibrium concentrations**
- Compartment 1:
  $$[Na^+]_1 = 0.100 + 0.03333 = 0.13333\\text{ M}$$
  $$[Cl^-]_1 = 0.03333\\text{ M}$$
- Compartment 2:
  $$[Na^+]_2 = 0.100 - 0.03333 = 0.06667\\text{ M}$$
  $$[Cl^-]_2 = 0.06667\\text{ M}$$

Verification of Donnan product:
$$(0.13333) \\times (0.03333) = 0.004444$$
$$(0.06667) \\times (0.06667) = 0.004445$$

**Step 4: Calculate Donnan membrane potential $\\Delta \\phi$**
$$\\Delta \\phi = \\phi_1 - \\phi_2 = -\\frac{R T}{F} \\ln\\left( \\frac{[Na^+]_1}{[Na^+]_2} \\right)$$
$$\\frac{R T}{F} = \\frac{8.314462 \\times 298.15}{96485.3} = 0.025693\\text{ V} = 25.693\\text{ mV}$$
$$\\Delta \\phi = -25.693\\text{ mV} \\times \\ln\\left( \\frac{0.13333}{0.06667} \\right) = -25.693 \\times \\ln(2.000) = -25.693 \\times 0.69315 = -17.81\\text{ mV}$$
Compartment 1 is at a negative electric potential of $-17.81\\text{ mV}$ relative to compartment 2."""
            },
            {
                "id": "p3-6",
                "title": "Steady-State Drug Diffusion Through a Polymeric Transdermal Patch",
                "difficulty": "Medium",
                "statement": "A transdermal therapeutic patch of area $A = 10.0\\text{ cm}^2$ and membrane thickness $L = 120\\;\\mu\\text{m}$ delivers a lipophilic drug of molar mass $M = 314.4\\text{ g/mol}$. The drug concentration in the patch reservoir is maintained at saturation $c_1 = 45.0\\text{ mg/mL}$. In the receptor skin sink, $c_2 \\approx 0$. The membrane partition coefficient is $K_{\\text{mem}} = 2.40$, and the diffusion coefficient within the polymer is $D = 3.50 \\times 10^{-9}\\text{ cm}^2/\\text{s}$. Calculate: (a) the membrane permeability $P_{\\text{perm}}$, (b) the steady-state drug delivery rate in $\\text{mg/day}$.",
                "solution": """**Step 1: Calculate membrane permeability $P_{\\text{perm}}$**
$$L = 120 \\times 10^{-4}\\text{ cm} = 0.0120\\text{ cm}$$
$$P_{\\text{perm}} = \\frac{K_{\\text{mem}} D}{L} = \\frac{2.40 \\times (3.50 \\times 10^{-9}\\text{ cm}^2/\\text{s})}{0.0120\\text{ cm}} = \\frac{8.40 \\times 10^{-9}}{0.0120} = 7.00 \\times 10^{-7}\\text{ cm/s}$$

**Step 2: Steady-state flux $J$**
$$J = P_{\\text{perm}} (c_1 - c_2) = (7.00 \\times 10^{-7}\\text{ cm/s}) \\times (45.0\\text{ mg/cm}^3) = 3.150 \\times 10^{-5}\\text{ mg}/(\\text{cm}^2\\cdot\\text{s})$$

**Step 3: Total daily delivery rate**
Patch area: $A = 10.0\\text{ cm}^2$.
Time per day: $t = 86400\\text{ s/day}$.
$$\\text{Rate} = J \\times A \\times 86400 = (3.150 \\times 10^{-5}\\text{ mg}/(\\text{cm}^2\\cdot\\text{s})) \\times (10.0\\text{ cm}^2) \\times (86400\\text{ s/day})$$
$$\\text{Rate} = 3.150 \\times 10^{-4} \\times 86400 = 27.22\\text{ mg/day}$$"""
            },
            {
                "id": "p3-7",
                "title": "Velocity Relaxation Time and Ballistic-to-Diffusive Crossover in Langevin Dynamics",
                "difficulty": "Hard",
                "statement": "A spherical silica bead of radius $r = 0.500\\;\\mu\\text{m}$ and mass density $\\rho = 2.00 \\times 10^3\\text{ kg/m}^3$ undergoes Brownian motion in water ($\\eta = 1.00 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$). (a) Calculate the mass $m$ and Stokes friction coefficient $\\gamma$, (b) calculate the momentum relaxation time $\\tau_m = m / \\gamma$, and (c) determine whether motion is ballistic or diffusive at $t_1 = 10\\text{ ns}$ and at $t_2 = 1.0\\;\\mu\\text{s}$.",
                "solution": """**Step 1: Particle mass and friction coefficient**
$$r = 5.00 \\times 10^{-7}\\text{ m}$$
Volume of sphere:
$$V = \\frac{4}{3} \\pi r^3 = \\frac{4}{3} \\pi (5.00 \\times 10^{-7})^3 = 5.2360 \\times 10^{-19}\\text{ m}^3$$
Mass:
$$m = \\rho V = (2.00 \\times 10^3\\text{ kg/m}^3) \\times (5.2360 \\times 10^{-19}\\text{ m}^3) = 1.0472 \\times 10^{-15}\\text{ kg}$$

Stokes friction coefficient:
$$\\gamma = 6 \\pi \\eta r = 6 \\pi \\times (1.00 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}) \\times (5.00 \\times 10^{-7}\\text{ m}) = 9.4248 \\times 10^{-9}\\text{ kg/s}$$

**Step 2: Momentum relaxation time $\\tau_m$**
$$\\tau_m = \\frac{m}{\\gamma} = \\frac{1.0472 \\times 10^{-15}\\text{ kg}}{9.4248 \\times 10^{-9}\\text{ kg/s}} = 1.111 \\times 10^{-7}\\text{ s} = 111.1\\text{ ns}$$

**Step 3: Regime analysis**
The crossover between ballistic motion ($\\langle x^2 \\rangle \\propto t^2$, dominated by inertia) and diffusive motion ($\\langle x^2 \\rangle \\propto t$, dominated by friction) occurs at $t \\sim \\tau_m = 111.1\\text{ ns}$.

- At $t_1 = 10\\text{ ns} \\ll \\tau_m$:
  $$\\frac{t_1}{\\tau_m} = \\frac{10}{111.1} = 0.090 \\ll 1$$
  The motion is **ballistic**: $\\langle x^2 \\rangle \\approx \\frac{k_B T}{m} t^2$. The particle retains memory of its initial velocity.

- At $t_2 = 1.0\\;\\mu\\text{s} = 1000\\text{ ns} \\gg \\tau_m$:
  $$\\frac{t_2}{\\tau_m} = \\frac{1000}{111.1} = 9.0 \\gg 1$$
  The motion is purely **diffusive**: $\\langle x^2 \\rangle \\approx 2 D t$. Multiple random collisions have completely thermalized velocity memory."""
            }
        ]
    }
    units.append(u3)

    return units

if __name__ == "__main__":
    units = get_units_1_2_3()
    print(f"Built Units 1, 2, and 3 successfully! Total units: {len(units)}")
    for u in units:
        print(f"  - {u['title']}: {len(u['sections'])} sections, {len(u['problems'])} problems")
