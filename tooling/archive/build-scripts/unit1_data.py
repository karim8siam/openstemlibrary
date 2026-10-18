# -*- coding: utf-8 -*-
# Unit 1: Electromagnetic Field Equations & Conservation Laws

UNIT_1 = {
    "id": "unit-1",
    "number": 1,
    "title": "Electromagnetic Field Equations & Conservation Laws",
    "leadSummary": "Comprehensive formulation of classical field theory: the breakdown and inconsistency of Ampère's circuital law for non-steady currents, Maxwell's hypothesis of displacement current, charge conservation via the equation of continuity, the complete Maxwell equations in differential and integral forms across free space and material media, the rigorous vector derivation of Poynting's theorem, electromagnetic momentum density, and radiation pressure.",
    "simulations": ["displacement-current", "poynting-vector"],
    "sections": [
        {
            "secNumber": "1.1",
            "heading": "Inadequacy of Ampère's Circuital Law and the Capacitor Paradox",
            "content": """
Before the revolutionary theoretical synthesis by James Clerk Maxwell (1861–1865), classical electromagnetism was formulated through empirical laws developed primarily for static or steady-state conditions:

1. **Gauss's Law for Electrostatics:** $\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\epsilon_0}$
2. **Gauss's Law for Magnetism:** $\\nabla \\cdot \\mathbf{B} = 0$
3. **Faraday's Law of Electromagnetic Induction:** $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$
4. **Ampère's Circuital Law:** $\\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J}$

#### The Fundamental Mathematical Contradiction
In vector calculus, the divergence of any curl of a vector field identically vanishes. Applying the divergence operator to both sides of Ampère's law yields:
$$\\nabla \\cdot (\\nabla \\times \\mathbf{B}) = \\mu_0 (\\nabla \\cdot \\mathbf{J})$$
Since $\\nabla \\cdot (\\nabla \\times \\mathbf{A}) \\equiv 0$ for any twice-differentiable vector field $\\mathbf{A}$, the left-hand side is identically zero:
$$0 = \\mu_0 (\\nabla \\cdot \\mathbf{J}) \\implies \\nabla \\cdot \\mathbf{J} = 0$$

However, the fundamental law of **Conservation of Electric Charge** requires that the divergence of the current density equals the negative rate of charge accumulation, as stated by the **Continuity Equation**:
$$\\nabla \\cdot \\mathbf{J} + \\frac{\\partial \\rho}{\\partial t} = 0 \\implies \\nabla \\cdot \\mathbf{J} = -\\frac{\\partial \\rho}{\\partial t}$$

Ampère's circuital law is therefore mathematically incompatible with the conservation of charge whenever the charge density varies with time ($\\partial \\rho / \\partial t \\neq 0$). Ampère's law holds strictly for steady currents (magnetostatics) where $\\partial \\rho / \\partial t = 0$, but fails catastrophically for time-dependent circuits.

#### The Physical Gedankenexperiment: The Capacitor Paradox
Consider a circular parallel-plate capacitor being charged by a steady current $I(t)$ flowing through a connecting wire. Draw a closed loop $C$ encircling the wire. By Stokes' theorem, the line integral of $\\mathbf{B}$ around $C$ equals the surface integral of current density through any open surface $S$ bounded by $C$:
$$\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 \\int_S \\mathbf{J} \\cdot d\\mathbf{a} = \\mu_0 I_{\\text{enc}}$$

- **Surface $S_1$ (Flat Disk):** Choose a flat circular disk bounded by $C$. The conducting wire pierces $S_1$, so the enclosed current is $I_{\\text{enc}} = I$, giving $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I$.
- **Surface $S_2$ (Balloon/Bowl Shape):** Bulge the surface out like a balloon so that it passes entirely between the capacitor plates without touching the wire. Since no conduction current passes through the vacuum gap between the plates, $I_{\\text{enc}} = 0$, giving $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = 0$.

Because the line integral $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l}$ around the exact same physical curve $C$ cannot depend on the arbitrary mathematical choice of surface $S$, classical electrodynamics faced an irreconcilable paradox.
"""
        },
        {
            "secNumber": "1.2",
            "heading": "Maxwell's Displacement Current and the Equation of Continuity",
            "content": """
#### The Displacement Current Derivation
To resolve the contradiction, Maxwell proposed adding a missing current density term, $\\mathbf{J}_d$ (the **displacement current density**), to Ampère's equation:
$$\\nabla \\times \\mathbf{B} = \\mu_0 (\\mathbf{J} + \\mathbf{J}_d)$$

Taking the divergence of both sides:
$$\\nabla \\cdot (\\nabla \\times \\mathbf{B}) = 0 = \\mu_0 \\left( \\nabla \\cdot \\mathbf{J} + \\nabla \\cdot \\mathbf{J}_d \\right)$$
$$\\nabla \\cdot \\mathbf{J}_d = -\\nabla \\cdot \\mathbf{J}$$

Using the continuity equation $\\nabla \\cdot \\mathbf{J} = -\\frac{\\partial \\rho}{\\partial t}$:
$$\\nabla \\cdot \\mathbf{J}_d = \\frac{\\partial \\rho}{\\partial t}$$

Now, substitute Gauss's law $\\rho = \\epsilon_0 (\\nabla \\cdot \\mathbf{E})$:
$$\\nabla \\cdot \\mathbf{J}_d = \\frac{\\partial}{\\partial t} \\left( \\epsilon_0 \\nabla \\cdot \\mathbf{E} \\right) = \\nabla \\cdot \\left( \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t} \\right)$$

Equating the vector terms under the divergence yields Maxwell's formulation for the **displacement current density in free space**:
$$\\mathbf{J}_d = \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$$

#### Total Current in the Capacitor Gap
The total displacement current $I_d$ passing through the cross-sectional area $A$ between the capacitor plates is:
$$I_d = \\int_A \\mathbf{J}_d \\cdot d\\mathbf{a} = \\epsilon_0 \\frac{d}{dt} \\int_A \\mathbf{E} \\cdot d\\mathbf{a} = \\epsilon_0 \\frac{d\\Phi_E}{dt}$$
where $\\Phi_E$ is the electric flux. For a parallel-plate capacitor with plate charge $Q(t)$ and plate area $A$:
$$E(t) = \\frac{\\sigma(t)}{\\epsilon_0} = \\frac{Q(t)}{\\epsilon_0 A} \\implies \\Phi_E(t) = E(t) A = \\frac{Q(t)}{\\epsilon_0}$$
Differentiating with respect to time:
$$I_d = \\epsilon_0 \\frac{d}{dt} \\left( \\frac{Q(t)}{\\epsilon_0} \\right) = \\frac{dQ}{dt} = I_c(t)$$

Thus, the displacement current $I_d$ between the plates is **identically equal** to the conduction current $I_c$ flowing in the external circuit wires. The total current $I_{\\text{tot}} = I_c + I_d$ is perfectly continuous everywhere in the circuit, completely eliminating the capacitor paradox.
"""
        },
        {
            "secNumber": "1.3",
            "heading": "The Complete System of Maxwell's Equations (Differential & Integral Forms)",
            "content": """
The addition of the displacement current term completed the classical theory of electrodynamics. Maxwell's equations describe the behavior of macroscopic and microscopic electromagnetic fields in terms of charge densities $\\rho$ and current densities $\\mathbf{J}$.

#### Maxwell's Equations in Vacuum (Microscopic Form)

| Physical Law | Differential Equation | Integral Equation | Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Gauss's Law for $\\mathbf{E}$** | $\\nabla \\cdot \\mathbf{E} = \\frac{\\rho}{\\epsilon_0}$ | $\\oint_S \\mathbf{E} \\cdot d\\mathbf{a} = \\frac{Q_{\\text{enc}}}{\\epsilon_0}$ | Electric field flux through a closed surface is proportional to the enclosed electric charge. Electric field lines originate on positive charges and terminate on negative charges. |
| **Gauss's Law for $\\mathbf{B}$** | $\\nabla \\cdot \\mathbf{B} = 0$ | $\\oint_S \\mathbf{B} \\cdot d\\mathbf{a} = 0$ | Magnetic fields are solenoidal; magnetic monopoles do not exist in classical physics. Magnetic field lines form continuous closed loops without sources or sinks. |
| **Faraday's Law of Induction** | $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$ | $\\oint_C \\mathbf{E} \\cdot d\\mathbf{l} = -\\frac{d\\Phi_B}{dt}$ | A time-varying magnetic flux induces a non-conservative, curling electric field (electromotive force, EMF). |
| **Ampère-Maxwell Law** | $\\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J} + \\mu_0 \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$ | $\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{\\text{enc}} + \\mu_0 \\epsilon_0 \\frac{d\\Phi_E}{dt}$ | Magnetic fields are generated by both conduction electric currents and time-varying electric flux (displacement current). |

#### Maxwell's Equations in Matter (Macroscopic Form)
In material media, charges and currents are split into **free** charges/currents (conducted electrons, free ions: $\\rho_f, \\mathbf{J}_f$) and **bound** charges/currents arising from dielectric polarization $\\mathbf{P}$ and magnetization $\\mathbf{M}$:
$$\\rho_b = -\\nabla \\cdot \\mathbf{P}, \\quad \\mathbf{J}_b = \\nabla \\times \\mathbf{M}, \\quad \\mathbf{J}_p = \\frac{\\partial \\mathbf{P}}{\\partial t}$$

Defining the auxiliary fields:
- **Electric Displacement:** $\\mathbf{D} \\equiv \\epsilon_0 \\mathbf{E} + \\mathbf{P}$
- **Magnetic Field Intensity:** $\\mathbf{H} \\equiv \\frac{1}{\\mu_0} \\mathbf{B} - \\mathbf{M}$

The macroscopic Maxwell equations take the form:
1. $\\nabla \\cdot \\mathbf{D} = \\rho_f$
2. $\\nabla \\cdot \\mathbf{B} = 0$
3. $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$
4. $\\nabla \\times \\mathbf{H} = \\mathbf{J}_f + \\frac{\\partial \\mathbf{D}}{\\partial t}$

For linear, isotropic, and homogeneous media:
$$\\mathbf{D} = \\epsilon \\mathbf{E} = \\epsilon_r \\epsilon_0 \\mathbf{E}, \\quad \\mathbf{B} = \\mu \\mathbf{H} = \\mu_r \\mu_0 \\mathbf{H}$$
"""
        },
        {
            "secNumber": "1.4",
            "heading": "Physical Significance, Symmetry, and Non-Existence of Magnetic Monopoles",
            "content": """
#### The Dynamic Cross-Coupling of Fields
A critical insight of Maxwell's equations is the mutual interdependence of electric and magnetic fields in time-dependent situations:
$$\\frac{\\partial \\mathbf{B}}{\\partial t} \\neq 0 \\implies \\nabla \\times \\mathbf{E} \\neq 0 \\quad \\text{and} \\quad \\frac{\\partial \\mathbf{E}}{\\partial t} \\neq 0 \\implies \\nabla \\times \\mathbf{B} \\neq 0$$
Even in a pure vacuum with zero charges ($\\rho = 0$) and zero currents ($\\mathbf{J} = 0$), a changing magnetic field creates an electric field, and that changing electric field in turn generates a magnetic field. This self-sustaining, reciprocal generation allows electromagnetic disturbances to detach from their sources and propagate across infinite distances through empty space as **electromagnetic radiation**.

#### Asymmetry and Magnetic Monopoles
Notice the apparent asymmetry between electricity and magnetism:
$$\\nabla \\cdot \\mathbf{E} = \\frac{\\rho_e}{\\epsilon_0}, \\quad \\nabla \\cdot \\mathbf{B} = 0$$
$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}, \\quad \\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J}_e + \\frac{1}{c^2} \\frac{\\partial \\mathbf{E}}{\\partial t}$$

If magnetic monopoles existed in nature with magnetic charge density $\\rho_m$ and magnetic current density $\\mathbf{J}_m$, Maxwell's equations would achieve perfect dual symmetry:
$$\\nabla \\cdot \\mathbf{E} = \\frac{\\rho_e}{\\epsilon_0}, \\quad \\nabla \\cdot \\mathbf{B} = \\mu_0 \\rho_m$$
$$\\nabla \\times \\mathbf{E} = -\\mu_0 \\mathbf{J}_m - \\frac{\\partial \\mathbf{B}}{\\partial t}, \\quad \\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J}_e + \\frac{1}{c^2} \\frac{\\partial \\mathbf{E}}{\\partial t}$$

Despite extensive experimental searches in particle colliders, cosmic rays, and lunar rock samples, no isolated magnetic monopole has ever been conclusively observed. Paul Dirac proved in 1931 that the existence of even a single magnetic monopole anywhere in the universe would explain the quantization of electric charge:
$$q_e q_m = 2\\pi n \\hbar, \\quad n \\in \\mathbb{Z}$$
"""
        },
        {
            "secNumber": "1.5",
            "heading": "Energy Considerations: Poynting's Theorem & Electromagnetic Energy Flux",
            "content": """
#### Step-by-Step Mathematical Derivation of Poynting's Theorem
The work done by electromagnetic forces on a distribution of charges in volume $V$ is governed by the Lorentz force law. The mechanical work per unit time (power) delivered to the charges is:
$$\\frac{dW_{\\text{mech}}}{dt} = \\int_V (\\mathbf{F} \\cdot \\mathbf{v}) dq = \\int_V \\mathbf{E} \\cdot \\mathbf{J} \\, d\\tau$$
where $d\\tau$ is the differential volume element.

To express $\\mathbf{E} \\cdot \\mathbf{J}$ in terms of field quantities alone, solve for $\\mathbf{J}$ using the Ampère-Maxwell law:
$$\\mathbf{J} = \\frac{1}{\\mu_0} (\\nabla \\times \\mathbf{B}) - \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$$

Dot both sides with $\\mathbf{E}$:
$$\\mathbf{E} \\cdot \\mathbf{J} = \\frac{1}{\\mu_0} \\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B}) - \\epsilon_0 \\mathbf{E} \\cdot \\frac{\\partial \\mathbf{E}}{\\partial t}$$

Recall the fundamental vector calculus product rule:
$$\\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B}) = \\mathbf{B} \\cdot (\\nabla \\times \\mathbf{E}) - \\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B})$$
$$\\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B}) = \\mathbf{B} \\cdot (\\nabla \\times \\mathbf{E}) - \\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B})$$

Substitute Faraday's law $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$:
$$\\mathbf{E} \\cdot (\\nabla \\times \\mathbf{B}) = -\\mathbf{B} \\cdot \\frac{\\partial \\mathbf{B}}{\\partial t} - \\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B})$$

Now, observe that:
$$\\mathbf{E} \\cdot \\frac{\\partial \\mathbf{E}}{\\partial t} = \\frac{1}{2} \\frac{\\partial}{\\partial t}(E^2), \\quad \\mathbf{B} \\cdot \\frac{\\partial \\mathbf{B}}{\\partial t} = \\frac{1}{2} \\frac{\\partial}{\\partial t}(B^2)$$

Substituting these identities back into the expression for $\\mathbf{E} \\cdot \\mathbf{J}$:
$$\\mathbf{E} \\cdot \\mathbf{J} = -\\frac{1}{2} \\frac{\\partial}{\\partial t} \\left( \\epsilon_0 E^2 + \\frac{1}{\\mu_0} B^2 \\right) - \\frac{1}{\\mu_0} \\nabla \\cdot (\\mathbf{E} \\times \\mathbf{B})$$

#### Definitions of the Field Quantities
1. **Electromagnetic Energy Density ($u$):**
$$u \\equiv \\frac{1}{2} \\left( \\epsilon_0 E^2 + \\frac{1}{\\mu_0} B^2 \\right) \\quad [\\text{Joules} / \\text{m}^3]$$

2. **The Poynting Vector ($\\mathbf{S}$):**
$$\\mathbf{S} \\equiv \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) \\quad [\\text{Watts} / \\text{m}^2]$$
The Poynting vector represents the directional rate of electromagnetic energy transfer per unit area.

#### Differential Form of Poynting's Theorem
$$-\\frac{\\partial u}{\\partial t} = \\nabla \\cdot \\mathbf{S} + \\mathbf{E} \\cdot \\mathbf{J}$$
or in conservation law form:
$$\\frac{\\partial u}{\\partial t} + \\nabla \\cdot \\mathbf{S} = -\\mathbf{E} \\cdot \\mathbf{J}$$

#### Integral Form of Poynting's Theorem
Integrating over a finite volume $V$ bounded by closed surface $S$ and applying Gauss's divergence theorem:
$$-\\frac{d}{dt} \\int_V u \\, d\\tau = \\oint_S \\mathbf{S} \\cdot d\\mathbf{a} + \\int_V (\\mathbf{E} \\cdot \\mathbf{J}) \\, d\\tau$$

**Physical Interpretation:** The time rate of decrease of electromagnetic energy stored in volume $V$ equals the total power radiated outward across the boundary surface $S$ plus the rate of work done on the charges inside $V$ (such as Ohmic Joule heating $\\mathbf{J} \\cdot \\mathbf{E} = \\sigma E^2$).
"""
        },
        {
            "secNumber": "1.6",
            "heading": "Momentum of the Electromagnetic Field, Maxwell Stress Tensor & Radiation Pressure",
            "content": """
#### Electromagnetic Momentum Density
Electromagnetic fields carry not only energy, but also linear momentum. By applying the Lorentz force equation to volume charges, one derives the total momentum balance:
$$\\frac{d}{dt} (\\mathbf{p}_{\\text{mech}} + \\mathbf{p}_{\\text{field}}) = 0$$

The **electromagnetic momentum density** $\\mathbf{g}$ stored in the fields is directly proportional to the Poynting vector:
$$\\mathbf{g} = \\epsilon_0 (\\mathbf{E} \\times \\mathbf{B}) = \\frac{\\mathbf{S}}{c^2} \\quad [\\text{kg} / (\\text{m}^2 \\cdot \\text{s})]$$

#### The Maxwell Stress Tensor
The spatial flow of momentum is described by the **Maxwell stress tensor** $\\overleftrightarrow{\\mathbf{T}}$, a rank-2 symmetric tensor with components:
$$T_{ij} \\equiv \\epsilon_0 \\left( E_i E_j - \\frac{1}{2} \\delta_{ij} E^2 \\right) + \\frac{1}{\\mu_0} \\left( B_i B_j - \\frac{1}{2} \\delta_{ij} B^2 \\right)$$
where $\\delta_{ij}$ is the Kronecker delta. The electromagnetic force per unit volume is given by:
$$\\mathbf{f} = \\nabla \\cdot \\overleftrightarrow{\\mathbf{T}} - \\epsilon_0 \\mu_0 \\frac{\\partial \\mathbf{S}}{\\partial t}$$

#### Radiation Pressure
When an electromagnetic wave impinges on a physical surface, it transfers linear momentum to the matter, exerting a mechanical pressure known as **radiation pressure** ($P_{\\text{rad}}$).

Let the incident wave carry intensity $I = \\langle S \\rangle = c \\langle u \\rangle$:

1. **Total Absorption (Perfect Blackbody Surface):**
All incident momentum is transferred to the surface:
$$P_{\\text{rad}} = \\frac{\\langle S \\rangle}{c} = \\langle u \\rangle = \\frac{I}{c}$$

2. **Total Reflection (Ideal Conducting Mirror):**
The reflected wave has reversed momentum ($\\Delta p = p_{\\text{final}} - p_{\\text{initial}} = -p - p = -2p$). By Newton's third law, the impulse delivered to the surface is doubled:
$$P_{\\text{rad}} = \\frac{2 \\langle S \\rangle}{c} = 2 \\langle u \\rangle = \\frac{2I}{c}$$

3. **Oblique Incidence at Angle $\\theta$:**
$$P_{\\text{rad}} = \\frac{I}{c} (1 + R) \\cos^2\\theta$$
where $R$ is the surface reflection coefficient ($R=0$ for complete absorption, $R=1$ for total reflection).
"""
        }
    ],
    "problems": [
        {
            "id": "p1-1",
            "title": "Example 1.1: Complete Field and Displacement Current Distribution in a Circular Capacitor",
            "difficulty": "Medium",
            "question": "A parallel-plate capacitor consists of circular plates of radius $R$ separated by distance $d$. It is charged by a constant current $I$. Determine: (a) the electric field $E(t)$ between the plates, (b) the displacement current density $J_d$ and total displacement current $I_d$, (c) the induced magnetic field $B(r)$ at radial distance $r$ from the axis for both $r \\le R$ and $r > R$, and (d) verify the continuity of $B$ at $r = R$.",
            "steps": [
                {
                    "stepName": "Step 1: Electric Field and Displacement Current Density",
                    "math": "Q(t) = I t \\implies \\sigma(t) = \\frac{I t}{\\pi R^2} \\implies E(t) = \\frac{\\sigma(t)}{\\epsilon_0} = \\frac{I t}{\\epsilon_0 \\pi R^2}\\nJ_d = \\epsilon_0 \\frac{\\partial E}{\\partial t} = \\epsilon_0 \\frac{d}{dt}\\left( \\frac{I t}{\\epsilon_0 \\pi R^2} \\right) = \\frac{I}{\\pi R^2}\\nI_d = \\int_0^R J_d (2\\pi r dr) = \\frac{I}{\\pi R^2} (\\pi R^2) = I",
                    "explanation": "The displacement current density is completely uniform across the entire plate area, and its surface integral yields exactly $I$, proving current continuity across the dielectric gap."
                },
                {
                    "stepName": "Step 2: Induced Magnetic Field Inside the Plates (r <= R)",
                    "math": "\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{d,\\text{enc}} = \\mu_0 \\int_0^r J_d (2\\pi r' dr') = \\mu_0 \\left(\\frac{I}{\\pi R^2}\\right) (\\pi r^2) = \\mu_0 I \\frac{r^2}{R^2}\\nB(2\\pi r) = \\mu_0 I \\frac{r^2}{R^2} \\implies B(r) = \\frac{\\mu_0 I r}{2\\pi R^2} \\quad (r \\le R)",
                    "explanation": "Inside the gap, the magnetic field increases linearly with radial distance $r$, starting from zero at the central axis."
                },
                {
                    "stepName": "Step 3: Induced Magnetic Field Outside the Plates (r > R)",
                    "math": "\\oint_C \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I_{d,\\text{total}} = \\mu_0 I\\nB(2\\pi r) = \\mu_0 I \\implies B(r) = \\frac{\\mu_0 I}{2\\pi r} \\quad (r > R)",
                    "explanation": "Outside the plates, the magnetic field is identical to that produced by a continuous, infinitely long straight wire carrying current $I$."
                },
                {
                    "stepName": "Step 4: Boundary Matching at r = R",
                    "math": "B(R^-) = \\frac{\\mu_0 I R}{2\\pi R^2} = \\frac{\\mu_0 I}{2\\pi R}, \\quad B(R^+) = \\frac{\\mu_0 I}{2\\pi R}",
                    "explanation": "The magnetic field is continuous across $r=R$, with a maximum value of $B_{\\text{max}} = \\frac{\\mu_0 I}{2\\pi R}$."
                }
            ]
        },
        {
            "id": "p1-2",
            "title": "Example 1.2: Radial Poynting Energy Flow in a Current-Carrying Resistive Wire",
            "difficulty": "Hard",
            "question": "A cylindrical ohmic wire of length $L$, radius $a$, and conductivity $\\sigma$ carries a steady uniform DC current $I$. Calculate: (a) the electric field $\\mathbf{E}$ inside and on the surface of the wire, (b) the magnetic field $\\mathbf{B}$ at the wire surface, (c) the direction and magnitude of the Poynting vector $\\mathbf{S}$ at the surface, and (d) integrate $\\mathbf{S}$ over the wire surface to demonstrate that electromagnetic field energy flows into the wire to supply Joule heating.",
            "steps": [
                {
                    "stepName": "Step 1: Surface Electric and Magnetic Fields",
                    "math": "J = \\frac{I}{\\pi a^2} \\implies \\mathbf{E} = \\frac{\\mathbf{J}}{\\sigma} = \\frac{I}{\\sigma \\pi a^2} \\hat{\\mathbf{z}}\\n\\oint \\mathbf{B} \\cdot d\\mathbf{l} = \\mu_0 I \\implies B(a)(2\\pi a) = \\mu_0 I \\implies \\mathbf{B}(a) = \\frac{\\mu_0 I}{2\\pi a} \\hat{\\boldsymbol{\\phi}}",
                    "explanation": "The electric field points along the length of the wire (axial $\\hat{\\mathbf{z}}$), while the magnetic field curls azimuthally (tangential $\\hat{\\boldsymbol{\\phi}}$)."
                },
                {
                    "stepName": "Step 2: Poynting Vector Computation",
                    "math": "\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{1}{\\mu_0} \\left( \\frac{I}{\\sigma \\pi a^2} \\hat{\\mathbf{z}} \\times \\frac{\\mu_0 I}{2\\pi a} \\hat{\\boldsymbol{\\phi}} \\right) = -\\frac{I^2}{2\\pi^2 \\sigma a^3} \\hat{\\mathbf{r}}",
                    "explanation": "Since $\\hat{\\mathbf{z}} \\times \\hat{\\boldsymbol{\\phi}} = -\\hat{\\mathbf{r}}$, the Poynting vector points radially INWARD into the wire from the surrounding space."
                },
                {
                    "stepName": "Step 3: Surface Integration and Joule Dissipation",
                    "math": "P_{\\text{in}} = -\\oint \\mathbf{S} \\cdot d\\mathbf{a} = |S| (2\\pi a L) = \\left( \\frac{I^2}{2\\pi^2 \\sigma a^3} \\right) (2\\pi a L) = I^2 \\left( \\frac{L}{\\sigma \\pi a^2} \\right) = I^2 R",
                    "explanation": "Energy does not flow down the wire inside the conductor like a fluid; rather, electrical energy travels through the electromagnetic field outside the wire and enters radially through the outer surface to be dissipated as thermal Joule heat $I^2 R$."
                }
            ]
        },
        {
            "id": "p1-3",
            "title": "Example 1.3: Electromagnetic Energy Transport in a Coaxial Cable",
            "difficulty": "Hard",
            "question": "A coaxial cable consists of an inner solid conductor of radius $a$ at potential $V$ carrying current $I$ in the $+z$ direction, and a thin outer coaxial cylindrical shell of radius $b$ at potential $0$ carrying the return current $I$ in the $-z$ direction. Calculate: (a) $\\mathbf{E}$ and $\\mathbf{B}$ in the insulating region $a < r < b$, (b) the Poynting vector $\\mathbf{S}(r)$, and (c) the total power transported along the cable by integrating $\\mathbf{S}$ over the annular cross section.",
            "steps": [
                {
                    "stepName": "Step 1: Field Distributions in the Annular Gap",
                    "math": "\\mathbf{E}(r) = \\frac{V}{\\ln(b/a)} \\frac{1}{r} \\hat{\\mathbf{r}}, \\quad \\mathbf{B}(r) = \\frac{\\mu_0 I}{2\\pi r} \\hat{\\boldsymbol{\\phi}}",
                    "explanation": "Gauss's law gives the radial electrostatic field, and Ampère's circuital law gives the azimuthal magnetic field."
                },
                {
                    "stepName": "Step 2: Poynting Vector in the Dielectric",
                    "math": "\\mathbf{S} = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{1}{\\mu_0} \\left( \\frac{V}{\\ln(b/a)} \\frac{1}{r} \\hat{\\mathbf{r}} \\times \\frac{\\mu_0 I}{2\\pi r} \\hat{\\boldsymbol{\\phi}} \\right) = \\frac{V I}{2\\pi \\ln(b/a)} \\frac{1}{r^2} \\hat{\\mathbf{z}}",
                    "explanation": "Because $\\hat{\\mathbf{r}} \\times \\hat{\\boldsymbol{\\phi}} = \\hat{\\mathbf{z}}$, the energy flux flows purely along the $+z$ direction parallel to the cable axis through the insulating dielectric."
                },
                {
                    "stepName": "Step 3: Total Power Transmission",
                    "math": "P = \\int_{r=a}^b \\mathbf{S} \\cdot d\\mathbf{a} = \\int_a^b \\left( \\frac{V I}{2\\pi \\ln(b/a)} \\frac{1}{r^2} \\right) (2\\pi r dr) = \\frac{V I}{\\ln(b/a)} \\int_a^b \\frac{dr}{r} = \\frac{V I}{\\ln(b/a)} [\\ln(b/a)] = V I",
                    "explanation": "The integrated Poynting flux equals precisely $P = VI$, proving that electric circuit power is transported entirely through the electromagnetic field in the dielectric space surrounding the conductors."
                }
            ]
        },
        {
            "id": "p1-4",
            "title": "Example 1.4: Solar Radiation Pressure and Spacecraft Solar Sail Propulsion",
            "difficulty": "Medium",
            "question": "The solar radiation flux (solar constant) reaching Earth's orbit at distance $R_E = 1.496 \\times 10^{11}\\text{ m}$ is $I_0 = 1361\\text{ W/m}^2$. A solar sail spacecraft with mass $m = 250\\text{ kg}$ deploys an ultra-reflective flat sail of area $A = 10^4\\text{ m}^2$ (reflectance $R = 0.98$). Calculate: (a) the radiation pressure on the sail at normal incidence, (b) the total repulsive radiation force exerted on the spacecraft, and (c) the initial acceleration imparted to the spacecraft.",
            "steps": [
                {
                    "stepName": "Step 1: Radiation Pressure Calculation",
                    "math": "P_{\\text{rad}} = \\frac{I_0}{c} (1 + R) = \\frac{1361\\text{ W/m}^2}{3.00 \\times 10^8\\text{ m/s}} (1 + 0.98) = (4.537 \\times 10^{-6}\\text{ N/m}^2) \\times 1.98 = 8.983 \\times 10^{-6}\\text{ N/m}^2",
                    "explanation": "The reflected photons deliver momentum $\\Delta p = 2p$, so near-perfect reflectance nearly doubles the thrust compared to an absorbing sail."
                },
                {
                    "stepName": "Step 2: Total Radiation Force",
                    "math": "F_{\\text{rad}} = P_{\\text{rad}} \\times A = (8.983 \\times 10^{-6}\\text{ N/m}^2) \\times (10^4\\text{ m}^2) = 0.0898\\text{ N} \\approx 0.090\\text{ N}",
                    "explanation": "A $100\\text{ m} \\times 100\\text{ m}$ sail intercepts over 13 megawatts of solar photon beam power, yielding roughly 0.09 Newtons of continuous fuel-free thrust."
                },
                {
                    "stepName": "Step 3: Initial Acceleration",
                    "math": "a = \\frac{F_{\\text{rad}}}{m} = \\frac{0.0898\\text{ N}}{250\\text{ kg}} = 3.59 \\times 10^{-4}\\text{ m/s}^2",
                    "explanation": "Although the acceleration is small ($0.36\\text{ mm/s}^2$), because it acts continuously without fuel consumption, the spacecraft gains over $31\\text{ m/s}$ ($112\\text{ km/h}$) of velocity every single day."
                }
            ]
        }
    ]
}

print("Unit 1 built successfully. Sections:", len(UNIT_1["sections"]), "Problems:", len(UNIT_1["problems"]))
