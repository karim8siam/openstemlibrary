# -*- coding: utf-8 -*-
# Unit 2: Propagation of Electromagnetic Waves in Media & Plasmas

UNIT_2 = {
    "id": "unit-2",
    "number": 2,
    "title": "Propagation of Electromagnetic Waves in Media & Plasmas",
    "leadSummary": "Rigorous analytical treatment of classical electromagnetic wave propagation: the vector wave equation derivation from Maxwell's field equations, monochromatic plane waves, orthogonality and transverse nature of electric and magnetic fields, intrinsic wave impedance of free space, lossy propagation in conducting media, attenuation constant, skin depth and phase delay in metals, and dispersion relations and plasma cutoff frequencies in ionized gases.",
    "simulations": ["em-wave-3d", "skin-depth"],
    "sections": [
        {
            "secNumber": "2.1",
            "heading": "The Electromagnetic Wave Equations in Vacuum & Media",
            "content": """
#### Derivation of the Vector Wave Equation
Consider source-free vacuum where charge density $\\rho = 0$ and conduction current density $\\mathbf{J} = 0$. Maxwell's equations reduce to:
1. $\\nabla \\cdot \\mathbf{E} = 0$
2. $\\nabla \\cdot \\mathbf{B} = 0$
3. $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$
4. $\\nabla \\times \\mathbf{B} = \\mu_0 \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t}$

To decouple these coupled first-order partial differential equations, take the curl of Faraday's law:
$$\\nabla \\times (\\nabla \\times \\mathbf{E}) = -\\nabla \\times \\left( \\frac{\\partial \\mathbf{B}}{\\partial t} \\right) = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{B})$$

Using the fundamental vector identity $\\nabla \\times (\\nabla \\times \\mathbf{A}) \\equiv \\nabla(\\nabla \\cdot \\mathbf{A}) - \\nabla^2 \\mathbf{A}$ on the left-hand side:
$$\\nabla(\\nabla \\cdot \\mathbf{E}) - \\nabla^2 \\mathbf{E} = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{B})$$

Since $\\nabla \\cdot \\mathbf{E} = 0$ in vacuum, and substituting Ampère-Maxwell's law for $\\nabla \\times \\mathbf{B}$:
$$-\\nabla^2 \\mathbf{E} = -\\frac{\\partial}{\\partial t} \\left( \\mu_0 \\epsilon_0 \\frac{\\partial \\mathbf{E}}{\\partial t} \\right) = -\\mu_0 \\epsilon_0 \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2}$$

Rearranging gives the celebrated **homogeneous vector wave equation for the electric field**:
$$\\nabla^2 \\mathbf{E} - \\mu_0 \\epsilon_0 \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2} = 0$$

Taking the curl of Ampère-Maxwell's law in identical fashion yields the **wave equation for the magnetic field**:
$$\\nabla^2 \\mathbf{B} - \\mu_0 \\epsilon_0 \\frac{\\partial^2 \\mathbf{B}}{\\partial t^2} = 0$$

#### The Speed of Light and Maxwell's Synthesis
Comparing these to the standard 3D scalar wave equation $\\nabla^2 \\psi - \\frac{1}{v^2} \\frac{\\partial^2 \\psi}{\\partial t^2} = 0$, the wave propagation speed $v$ is determined strictly by electromagnetic constants:
$$v = \\frac{1}{\\sqrt{\\epsilon_0 \\mu_0}}$$

Substituting experimental values:
$$\\epsilon_0 \\approx 8.8541878 \\times 10^{-12} \\text{ F/m}, \\quad \\mu_0 = 4\\pi \\times 10^{-7} \\text{ H/m}$$
$$v = \\frac{1}{\\sqrt{(8.8541878 \\times 10^{-12})(4\\pi \\times 10^{-7})}} = 2.99792458 \\times 10^8 \\text{ m/s} \\equiv c$$

This exact match between the derived velocity of electromagnetic waves and the measured speed of light led James Clerk Maxwell to declare: *"Light is an electromagnetic disturbance in the form of waves propagating through the electromagnetic field according to electromagnetic laws."*
"""
        },
        {
            "secNumber": "2.2",
            "heading": "Plane Waves, Transverse Nature, and Orthogonality of Fields",
            "content": """
#### Monochromatic Plane Wave Solutions
A plane wave traveling in direction $\\hat{\\mathbf{k}}$ with wavevector $\\mathbf{k} = k \\hat{\\mathbf{k}}$ and angular frequency $\\omega$ is described in complex exponential notation by:
$$\\mathbf{E}(\\mathbf{r}, t) = \\mathbf{E}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)}, \\quad \\mathbf{B}(\\mathbf{r}, t) = \\mathbf{B}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)}$$
where physical fields are the real parts $\\text{Re}\\{\\mathbf{E}\\}$.

Substituting into the wave equation gives the vacuum **dispersion relation**:
$$-k^2 + \\frac{\\omega^2}{c^2} = 0 \\implies k = \\frac{\\omega}{c} = \\frac{2\\pi}{\\lambda}$$

#### Rigorous Proof of Transverse Nature (No Longitudinal Component)
Apply Gauss's law $\\nabla \\cdot \\mathbf{E} = 0$:
$$\\nabla \\cdot \\left( \\mathbf{E}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)} \\right) = i \\mathbf{k} \\cdot \\mathbf{E}_0 e^{i(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t)} = i \\mathbf{k} \\cdot \\mathbf{E} = 0$$
$$\\implies \\mathbf{k} \\cdot \\mathbf{E} = 0$$

Similarly, applying $\\nabla \\cdot \\mathbf{B} = 0$:
$$i \\mathbf{k} \\cdot \\mathbf{B} = 0 \\implies \\mathbf{k} \\cdot \\mathbf{B} = 0$$

**Conclusion:** Both $\\mathbf{E}$ and $\\mathbf{B}$ are strictly perpendicular to the propagation vector $\\mathbf{k}$. Electromagnetic waves in unbounded homogeneous media are **purely transverse waves** ($E_k = 0, B_k = 0$).

#### Orthogonality and Phase Relationship
Applying Faraday's law $\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$:
$$i \\mathbf{k} \\times \\mathbf{E} = i \\omega \\mathbf{B} \\implies \\mathbf{B} = \\frac{\\mathbf{k} \\times \\mathbf{E}}{\\omega} = \\frac{1}{c} (\\hat{\\mathbf{k}} \\times \\mathbf{E})$$

This fundamental vector relation establishes that:
1. $\\mathbf{B}$ is perpendicular to $\\mathbf{E}$ ($\\mathbf{E} \\cdot \\mathbf{B} = 0$).
2. $\\mathbf{E}$, $\\mathbf{B}$, and $\\hat{\\mathbf{k}}$ form an orthogonal right-handed triad:
$$\\hat{\\mathbf{k}} = \\frac{\\mathbf{E} \\times \\mathbf{B}}{|\\mathbf{E}||\\mathbf{B}|}$$
3. The magnitudes are related by $B_0 = \\frac{E_0}{c}$.
4. In vacuum, $\\mathbf{E}$ and $\\mathbf{B}$ oscillate **exactly in phase**, reaching crests and nodes at identical positions and times.
"""
        },
        {
            "secNumber": "2.3",
            "heading": "Wave Impedance, Energy Flow, and Time-Averaged Poynting Flux",
            "content": """
#### Intrinsic Wave Impedance of Free Space
The ratio of the transverse electric field to the transverse magnetic intensity $H = B/\\mu_0$ defines the **wave impedance**:
$$\\eta_0 \\equiv \\frac{|\\mathbf{E}|}{|\\mathbf{H}|} = \\frac{E_0}{B_0 / \\mu_0} = \\mu_0 \\frac{E_0}{B_0} = \\mu_0 c = \\sqrt{\\frac{\\mu_0}{\\epsilon_0}}$$

Evaluating numerically:
$$\\eta_0 = \\sqrt{\\frac{4\\pi \\times 10^{-7} \\text{ H/m}}{8.8541878 \\times 10^{-12} \\text{ F/m}}} \\approx 376.7303135 \\, \\Omega \\approx 120\\pi \\, \\Omega$$

The wave impedance of free space represents the resistance of vacuum to the generation of electric and magnetic flux. In a linear medium with permittivity $\\epsilon$ and permeability $\\mu$, the intrinsic impedance is $\\eta = \\sqrt{\\mu / \\epsilon}$.

#### Time-Averaged Energy Flux (Intensity)
For real sinusoidal fields traveling along $+z$:
$$\\mathbf{E}(z, t) = E_0 \\cos(kz - \\omega t) \\hat{\\mathbf{x}}, \\quad \\mathbf{B}(z, t) = \\frac{E_0}{c} \\cos(kz - \\omega t) \\hat{\\mathbf{y}}$$
The instantaneous Poynting vector is:
$$\\mathbf{S}(z, t) = \\frac{1}{\\mu_0} (\\mathbf{E} \\times \\mathbf{B}) = \\frac{E_0^2}{\\mu_0 c} \\cos^2(kz - \\omega t) \\hat{\\mathbf{z}} = c \\epsilon_0 E_0^2 \\cos^2(kz - \\omega t) \\hat{\\mathbf{z}}$$

Since the time average of $\\cos^2(\\theta)$ over a full cycle is $\\frac{1}{2}$, the **time-averaged Poynting vector** (wave intensity $I$) is:
$$\\langle \\mathbf{S} \\rangle = \\frac{1}{2} c \\epsilon_0 E_0^2 \\hat{\\mathbf{z}} = \\frac{1}{2} \\frac{E_0^2}{\\eta_0} \\hat{\\mathbf{z}} = \\frac{1}{2} \\text{Re}\\{\\mathbf{E} \\times \\mathbf{H}^*\\}$$

#### Energy Density Distribution
The time-averaged electric energy density is:
$$\\langle u_E \\rangle = \\frac{1}{4} \\epsilon_0 E_0^2$$
The time-averaged magnetic energy density is:
$$\\langle u_B \\rangle = \\frac{1}{4\\mu_0} B_0^2 = \\frac{1}{4\\mu_0} \\left( \\frac{E_0}{c} \\right)^2 = \\frac{1}{4} \\epsilon_0 E_0^2$$
Thus, $\\langle u_E \\rangle = \\langle u_B \\rangle$: **electromagnetic energy is partitioned equally between electric and magnetic fields** at all times in a plane wave.
"""
        },
        {
            "secNumber": "2.4",
            "heading": "Propagation in Isotropic Non-Conducting Media",
            "content": """
In a linear, homogeneous, isotropic dielectric medium with permittivity $\\epsilon = \\epsilon_r \\epsilon_0$, permeability $\\mu = \\mu_r \\mu_0$, and conductivity $\\sigma = 0$:

Maxwell's equations yield the modified wave velocity:
$$v = \\frac{1}{\\sqrt{\\epsilon \\mu}} = \\frac{1}{\\sqrt{\\epsilon_r \\epsilon_0 \\mu_r \\mu_0}} = \\frac{c}{\\sqrt{\\epsilon_r \\mu_r}} = \\frac{c}{n}$$
where $n \\equiv \\sqrt{\\epsilon_r \\mu_r}$ is the **index of refraction** of the medium. For non-magnetic optical materials ($\\mu_r \\approx 1$), Maxwell's relation gives:
$$n = \\sqrt{\\epsilon_r}$$

#### Wavelength and Wavevector in Matter
Because frequency $\\omega$ is fixed by the driving source, the wavelength in the dielectric shrinks:
$$\\lambda = \\frac{v}{f} = \\frac{c}{n f} = \\frac{\\lambda_0}{n}$$
The wavevector increases:
$$k = \\frac{\\omega}{v} = n k_0$$
The wave impedance becomes:
$$\\eta = \\sqrt{\\frac{\\mu}{\\epsilon}} = \\frac{\\eta_0}{n} \\quad (\\text{for } \\mu_r = 1)$$
The time-averaged intensity in the dielectric is:
$$I = \\frac{1}{2} v \\epsilon E_0^2 = \\frac{1}{2} n c \\epsilon_0 E_0^2$$
"""
        },
        {
            "secNumber": "2.5",
            "heading": "Propagation in Conducting Media: Loss Tangent & Complex Wavevector",
            "content": """
#### The Telegrapher-Type Wave Equation in Conductors
In an ohmic conducting medium with electric conductivity $\\sigma$, free conduction currents flow according to **Ohm's Law**: $\\mathbf{J}_f = \\sigma \\mathbf{E}$. There are no static free charges ($\\rho_f = 0$).

Maxwell's curl equations become:
$$\\nabla \\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}$$
$$\\nabla \\times \\mathbf{B} = \\mu \\mathbf{J}_f + \\mu \\epsilon \\frac{\\partial \\mathbf{E}}{\\partial t} = \\mu \\sigma \\mathbf{E} + \\mu \\epsilon \\frac{\\partial \\mathbf{E}}{\\partial t}$$

Taking the curl of Faraday's law:
$$\\nabla \\times (\\nabla \\times \\mathbf{E}) = -\\frac{\\partial}{\\partial t} (\\nabla \\times \\mathbf{B}) = -\\mu \\sigma \\frac{\\partial \\mathbf{E}}{\\partial t} - \\mu \\epsilon \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2}$$
Since $\\nabla \\cdot \\mathbf{E} = 0$:
$$\\nabla^2 \\mathbf{E} - \\mu \\epsilon \\frac{\\partial^2 \\mathbf{E}}{\\partial t^2} - \\mu \\sigma \\frac{\\partial \\mathbf{E}}{\\partial t} = 0$$

The first-order time derivative term $\\mu \\sigma \\frac{\\partial \\mathbf{E}}{\\partial t}$ acts as a dissipative frictional damping term that extracts energy from the wave and converts it into Joule heat.

#### Complex Wavevector Formulation
Substitute a monochromatic plane wave $\\mathbf{E} = \\mathbf{E}_0 e^{i(\\tilde{k} z - \\omega t)}$:
$$-\\tilde{k}^2 \\mathbf{E} + \\mu \\epsilon \\omega^2 \\mathbf{E} + i \\mu \\sigma \\omega \\mathbf{E} = 0$$
$$\\tilde{k}^2 = \\mu \\epsilon \\omega^2 \\left( 1 + i \\frac{\\sigma}{\\omega \\epsilon} \\right)$$

The ratio $\\tan \\delta \\equiv \\frac{\\sigma}{\\omega \\epsilon}$ is known as the **loss tangent**. It quantifies the relative magnitude of conduction current compared to displacement current:
$$\\frac{|\\mathbf{J}_c|}{|\\mathbf{J}_d|} = \\frac{|\\sigma \\mathbf{E}|}{|\\epsilon \\partial \\mathbf{E}/\\partial t|} = \\frac{\\sigma}{\\omega \\epsilon}$$

Let the complex wavevector be $\\tilde{k} \\equiv \\beta + i \\alpha$:
$$\\tilde{k}^2 = (\\beta + i \\alpha)^2 = \\beta^2 - \\alpha^2 + 2i \\alpha \\beta = \\mu \\epsilon \\omega^2 + i \\mu \\sigma \\omega$$

Equating real and imaginary parts:
$$\\beta^2 - \\alpha^2 = \\mu \\epsilon \\omega^2$$
$$2 \\alpha \\beta = \\mu \\sigma \\omega$$

Solving this system yields the exact analytical expressions:
$$\\beta = \\omega \\sqrt{\\frac{\\mu \\epsilon}{2}} \\left[ \\sqrt{1 + \\left( \\frac{\\sigma}{\\omega \\epsilon} \\right)^2} + 1 \\right]^{1/2} \\quad (\\text{Phase constant})$$
$$\\alpha = \\omega \\sqrt{\\frac{\\mu \\epsilon}{2}} \\left[ \\sqrt{1 + \\left( \\frac{\\sigma}{\\omega \\epsilon} \\right)^2} - 1 \\right]^{1/2} \\quad (\\text{Attenuation constant})$$

The spatial electric field in the conductor is therefore:
$$\\mathbf{E}(z, t) = \\mathbf{E}_0 e^{-\\alpha z} e^{i(\\beta z - \\omega t)}$$
The wave amplitude decays exponentially with distance into the conductor.
"""
        },
        {
            "secNumber": "2.6",
            "heading": "Attenuation Constant, Phase Shift, and the Skin Depth (δ)",
            "content": """
#### The Good Conductor Limit ($\\sigma \\gg \\omega \\epsilon$)
For metals and good conductors (such as copper, silver, aluminum, and sea water at radio frequencies), conduction current dwarfs displacement current:
$$\\frac{\\sigma}{\\omega \\epsilon} \\gg 1$$

Under this approximation, the term $\\sqrt{1 + (\\sigma/\\omega\\epsilon)^2} \\approx \\frac{\\sigma}{\\omega \\epsilon}$, and the formulas for $\\alpha$ and $\\beta$ simplify dramatically:
$$\\beta \\approx \\alpha \\approx \\omega \\sqrt{\\frac{\\mu \\epsilon}{2} \\frac{\\sigma}{\\omega \\epsilon}} = \\sqrt{\\frac{\\omega \\mu \\sigma}{2}} = \\sqrt{\\pi f \\mu \\sigma}$$

#### Definition of Skin Depth ($\\delta$)
The **skin depth** $\\delta$ (also called penetration depth) is defined as the distance over which the wave amplitude drops by a factor of $1/e \\approx 0.3679$ (36.8% of its surface value):
$$\\delta \\equiv \\frac{1}{\\alpha} = \\sqrt{\\frac{2}{\\omega \\mu \\sigma}} = \\frac{1}{\\sqrt{\\pi f \\mu \\sigma}}$$

Over a depth of $z = 5\\delta$, the wave amplitude decays to $e^{-5} \\approx 0.0067$ (under 0.7%), meaning high-frequency currents are confined almost entirely to a microscopically thin outer shell of a conductor.

#### Table: Practical Skin Depths Across Frequencies
For pure copper ($\\sigma = 5.8 \\times 10^7 \\text{ S/m}$, $\\mu = \\mu_0$):

| Frequency ($f$) | Skin Depth $\\delta$ in Copper | Application / Impact |
| :--- | :--- | :--- |
| **50 Hz / 60 Hz** | $9.38 \\text{ mm}$ | AC mains power transmission (large cables require hollow or stranded conductors). |
| **10 kHz** | $0.66 \\text{ mm}$ | Audio and induction heating frequencies. |
| **1 MHz** | $66 \\, \\mu\\text{m}$ | AM radio broadcast frequencies. |
| **100 MHz** | $6.6 \\, \\mu\\text{m}$ | FM radio and VHF communications. |
| **10 GHz** | $0.66 \\, \\mu\\text{m}$ | X-band radar and microwave waveguides (requires surface silver plating). |

#### Phase Delay Between $\\mathbf{E}$ and $\\mathbf{B}$
From Faraday's law in a good conductor:
$$\\mathbf{B} = \\frac{\\tilde{k}}{\\omega} (\\hat{\\mathbf{z}} \\times \\mathbf{E})$$
Since $\\tilde{k} = \\beta + i \\alpha = \\alpha(1 + i) = \\alpha \\sqrt{2} e^{i\\pi/4}$:
$$\\mathbf{B}(z, t) = \\frac{\\sqrt{2} \\alpha}{\\omega} E_0 e^{-\\alpha z} e^{i(\\beta z - \\omega t + \\pi/4)} (\\hat{\\mathbf{z}} \\times \\hat{\\mathbf{x}})$$

**Physical Result:** In a good conductor, the magnetic field lags the electric field by a phase angle of $45^\\circ$ ($\\pi/4$ radians), and the magnetic energy density dramatically exceeds the electric energy density:
$$\\frac{\\langle u_B \\rangle}{\\langle u_E \\rangle} = \\frac{\\sigma}{\\omega \\epsilon} \\gg 1$$
"""
        },
        {
            "secNumber": "2.7",
            "heading": "Electromagnetic Waves in Ionized Gases (Plasmas) and Ionospheric Propagation",
            "content": """
#### The Cold Plasma Dielectric Function
Consider an ionized gas (such as the Earth's ionosphere or interstellar plasma) consisting of free electrons (mass $m_e$, charge $-e$, density $n_e$) and heavy, immobile positive ions. In the presence of a monochromatic electric field $\\mathbf{E}(t) = \\mathbf{E}_0 e^{-i\\omega t}$, the equation of motion for a conduction electron (neglecting damping collisions) is:
$$m_e \\frac{d^2 \\mathbf{r}}{dt^2} = -e \\mathbf{E} = -e \\mathbf{E}_0 e^{-i\\omega t}$$
$$\\mathbf{r}(t) = \\frac{e}{m_e \\omega^2} \\mathbf{E}(t)$$

The induced macroscopic dipole polarization density is:
$$\\mathbf{P} = -n_e e \\mathbf{r} = -\\frac{n_e e^2}{m_e \\omega^2} \\mathbf{E}$$

The electric displacement is:
$$\\mathbf{D} = \\epsilon_0 \\mathbf{E} + \\mathbf{P} = \\epsilon_0 \\left( 1 - \\frac{n_e e^2}{\\epsilon_0 m_e \\omega^2} \\right) \\mathbf{E} \\equiv \\epsilon(\\omega) \\mathbf{E}$$

#### The Plasma Frequency ($\\omega_p$)
We define the characteristic **electron plasma frequency**:
$$\\omega_p \\equiv \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} \\quad [\\text{rad/s}]$$
In terms of frequency in Hertz:
$$f_p = \\frac{\\omega_p}{2\\pi} = \\frac{1}{2\\pi} \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} \\approx 8.98 \\sqrt{n_e} \\quad [\\text{Hz}]$$
where $n_e$ is in $\\text{electrons/m}^3$.

The relative permittivity of the plasma is:
$$\\epsilon_r(\\omega) = 1 - \\frac{\\omega_p^2}{\\omega^2}$$

#### Dispersion Relation and Propagation Regimes
The wavevector in the plasma satisfies:
$$k^2 = \\frac{\\omega^2}{c^2} \\epsilon_r(\\omega) = \\frac{\\omega^2}{c^2} \\left( 1 - \\frac{\\omega_p^2}{\\omega^2} \\right) = \\frac{\\omega^2 - \\omega_p^2}{c^2}$$

1. **High Frequency Regime ($\\omega > \\omega_p$):**
   $k$ is purely real:
   $$k = \\frac{1}{c} \\sqrt{\\omega^2 - \\omega_p^2}$$
   The wave propagates freely without attenuation. The phase velocity exceeds the speed of light:
   $$v_p = \\frac{\\omega}{k} = \\frac{c}{\\sqrt{1 - \\omega_p^2/\\omega^2}} > c$$
   The group velocity (signal energy velocity) is strictly less than $c$:
   $$v_g = \\frac{d\\omega}{dk} = c \\sqrt{1 - \\frac{\\omega_p^2}{\\omega^2}} < c$$
   Notice that $v_p \\cdot v_g = c^2$, satisfying special relativity.

2. **Low Frequency Cutoff Regime ($\\omega < \\omega_p$):**
   $k$ becomes purely imaginary:
   $$k = i \\kappa = i \\frac{1}{c} \\sqrt{\\omega_p^2 - \\omega^2}$$
   The fields decay exponentially: $\\mathbf{E}(z, t) = \\mathbf{E}_0 e^{-\\kappa z} e^{-i\\omega t}$. No real energy is propagated; instead, the wave undergoes **total reflection** at the plasma boundary.

**Application to Radio Communications:** The Earth's ionosphere has peak electron density $n_e \\approx 10^{12} \\text{ m}^{-3}$, giving a plasma critical frequency $f_p \\approx 9 \\text{ MHz}$. Shortwave radio signals ($3 - 30 \\text{ MHz}$) below the critical frequency are totally reflected back to Earth, enabling global intercontinental communication without satellites. Satellite transmissions (GPS, 1.5 GHz) easily exceed $f_p$ and pass through the ionosphere unhindered.
"""
        }
    ],
    "problems": [
        {
            "id": "p2-1",
            "title": "Example 2.1: High-Power Monochromatic Laser Beam Parameters and Peak Field Strengths",
            "difficulty": "Medium",
            "question": "A focused Nd:YAG laser beam ($\\lambda = 1064\\text{ nm}$) operates at an average output power of $P = 150\\text{ W}$. It is focused down to a circular spot of radius $w_0 = 25\\,\\mu\\text{m}$ in air. Calculate: (a) the laser beam intensity $I$, (b) the peak electric field amplitude $E_0$, (c) the peak magnetic field amplitude $B_0$, and (d) the radiation pressure $P_{\\text{rad}}$ on a totally absorbing target placed at the focal spot.",
            "steps": [
                {
                    "stepName": "Step 1: Laser Intensity Calculation",
                    "math": "A = \\pi w_0^2 = \\pi (25 \\times 10^{-6}\\text{ m})^2 = 1.963 \\times 10^{-9}\\text{ m}^2\\nI = \\frac{P}{A} = \\frac{150\\text{ W}}{1.963 \\times 10^{-9}\\text{ m}^2} = 7.64 \\times 10^{10}\\text{ W/m}^2",
                    "explanation": "Focusing the laser concentrates 150 watts into a flux of over 76 gigawatts per square meter."
                },
                {
                    "stepName": "Step 2: Peak Electric Field Amplitude",
                    "math": "I = \\frac{1}{2} c \\epsilon_0 E_0^2 \\implies E_0 = \\sqrt{\\frac{2I}{c \\epsilon_0}}\\nE_0 = \\sqrt{\\frac{2(7.64 \\times 10^{10})}{(3.00 \\times 10^8)(8.854 \\times 10^{-12})}} = \\sqrt{5.753 \\times 10^{13}} = 7.58 \\times 10^6\\text{ V/m} = 7.58\\text{ MV/m}",
                    "explanation": "The electric field exceeds the dielectric breakdown threshold of ambient air ($3\\text{ MV/m}$), ionizing air molecules and generating a visible optical plasma spark."
                },
                {
                    "stepName": "Step 3: Peak Magnetic Field Amplitude",
                    "math": "B_0 = \\frac{E_0}{c} = \\frac{7.58 \\times 10^6\\text{ V/m}}{3.00 \\times 10^8\\text{ m/s}} = 0.0253\\text{ T} = 25.3\\text{ mT}",
                    "explanation": "The magnetic induction reaches 253 Gauss, illustrating the immense strength of focused optical fields."
                },
                {
                    "stepName": "Step 4: Radiation Pressure",
                    "math": "P_{\\text{rad}} = \\frac{I}{c} = \\frac{7.64 \\times 10^{10}\\text{ W/m}^2}{3.00 \\times 10^8\\text{ m/s}} = 254.7\\text{ N/m}^2 \\approx 255\\text{ Pa}",
                    "explanation": "Radiation pressure reaches several millibars, easily enough to trap and levitate microscopic dielectric beads in optical tweezers."
                }
            ]
        },
        {
            "id": "p2-2",
            "title": "Example 2.2: Penetration Depth of ELF Radio Waves in Seawater for Submarine Communications",
            "difficulty": "Hard",
            "question": "Seawater has electrical conductivity $\\sigma = 4.0\\text{ S/m}$, relative permittivity $\\epsilon_r = 81$, and $\\mu_r = 1$. (a) Determine whether seawater behaves as a good conductor or dielectric at $f = 75\\text{ Hz}$ (Extremely Low Frequency, ELF) and at $f = 2.4\\text{ GHz}$ (Wi-Fi). (b) Calculate the skin depth $\\delta$ at $75\\text{ Hz}$. (c) Calculate the depth $z$ at which a $75\\text{ Hz}$ submarine communications signal is attenuated by $60\\text{ dB}$ (power factor of $10^{-6}$).",
            "steps": [
                {
                    "stepName": "Step 1: Loss Tangent Verification",
                    "math": "\\text{At } f = 75\\text{ Hz}: \\frac{\\sigma}{\\omega \\epsilon} = \\frac{4.0}{2\\pi(75)(81)(8.854 \\times 10^{-12})} = \\frac{4.0}{3.385 \\times 10^{-7}} = 1.18 \\times 10^7 \\gg 1\\n\\text{At } f = 2.4\\text{ GHz}: \\frac{\\sigma}{\\omega \\epsilon} = \\frac{4.0}{2\\pi(2.4 \\times 10^9)(81)(8.854 \\times 10^{-12})} = 0.369 \\sim 1",
                    "explanation": "At 75 Hz, seawater is an exceptional conductor (conduction current dominates by 7 orders of magnitude). At 2.4 GHz, seawater is a lossy dielectric."
                },
                {
                    "stepName": "Step 2: Skin Depth at 75 Hz",
                    "math": "\\delta = \\frac{1}{\\sqrt{\\pi f \\mu_0 \\sigma}} = \\frac{1}{\\sqrt{\\pi(75)(4\\pi \\times 10^{-7})(4.0)}} = \\frac{1}{\\sqrt{1.184 \\times 10^{-3}}} = \\frac{1}{0.0344} = 29.06\\text{ m}",
                    "explanation": "The electromagnetic field amplitude decays by a factor of $1/e$ every 29 meters of seawater depth."
                },
                {
                    "stepName": "Step 3: Depth for 60 dB Power Attenuation",
                    "math": "\\text{Power ratio } \\frac{P(z)}{P(0)} = e^{-2\\alpha z} = e^{-2z/\\delta} = 10^{-6}\\n-\\frac{2z}{\\delta} = \\ln(10^{-6}) = -6 \\ln(10) = -13.816\\nz = \\frac{13.816}{2} \\delta = 6.908 \\times 29.06\\text{ m} = 200.7\\text{ m}",
                    "explanation": "ELF signals at 75 Hz can successfully reach nuclear submarines operating submerged at depths up to 200 meters (660 feet) without surfacing."
                }
            ]
        },
        {
            "id": "p2-3",
            "title": "Example 2.3: Phase Delay, Skin Effect, and AC Surface Resistance in Copper",
            "difficulty": "Medium",
            "question": "For a microwave frequency of $f = 10\\text{ GHz}$ propagating in copper ($\\sigma = 5.8 \\times 10^7\\text{ S/m}$, $\\mu = \\mu_0$): (a) calculate the skin depth $\\delta$, (b) calculate the phase velocity $v_p$ and wavelength $\\lambda$ inside the copper, and (c) find the surface resistance $R_s = \\frac{1}{\\sigma \\delta}$ per square.",
            "steps": [
                {
                    "stepName": "Step 1: Skin Depth Calculation",
                    "math": "\\delta = \\frac{1}{\\sqrt{\\pi f \\mu_0 \\sigma}} = \\frac{1}{\\sqrt{\\pi(10^{10})(4\\pi \\times 10^{-7})(5.8 \\times 10^7)}} = \\frac{1}{\\sqrt{2.2898 \\times 10^{12}}} = 6.61 \\times 10^{-7}\\text{ m} = 0.661\\,\\mu\\text{m}",
                    "explanation": "At 10 GHz, the entire microwave current flows in an ultra-thin surface skin of just 661 nanometers."
                },
                {
                    "stepName": "Step 2: Phase Velocity and Wavelength Inside the Metal",
                    "math": "\\beta = \\frac{1}{\\delta} = 1.513 \\times 10^6\\text{ rad/m}\\n\\lambda_{\\text{copper}} = \\frac{2\\pi}{\\beta} = 2\\pi \\delta = 2\\pi(6.61 \\times 10^{-7}\\text{ m}) = 4.15 \\times 10^{-6}\\text{ m} = 4.15\\,\\mu\\text{m}\\nv_p = \\frac{\\omega}{\\beta} = \\omega \\delta = 2\\pi(10^{10})(6.61 \\times 10^{-7}) = 4.15 \\times 10^4\\text{ m/s}",
                    "explanation": "In free space, a 10 GHz wave has $\\lambda_0 = 3\\text{ cm}$ and $v_p = c$. Inside the metal, the wave slows down to 41.5 km/s (a factor of 7200 slower), and its wavelength compresses to just 4.15 micrometers."
                },
                {
                    "stepName": "Step 3: Surface Resistance Calculation",
                    "math": "R_s = \\frac{1}{\\sigma \\delta} = \\sqrt{\\frac{\\pi f \\mu_0}{\\sigma}} = \\frac{1}{(5.8 \\times 10^7)(6.61 \\times 10^{-7})} = 0.0261\\,\\Omega = 26.1\\text{ m}\\Omega / \\text{sq}",
                    "explanation": "This non-zero surface resistance causes wall conduction loss and attenuation in microwave waveguides and cavity resonators."
                }
            ]
        },
        {
            "id": "p2-4",
            "title": "Example 2.4: Ionospheric Cutoff Frequency and Maximum Usable Frequency (MUF)",
            "difficulty": "Hard",
            "question": "The daytime ionospheric F2 layer has an electron density of $n_e = 1.5 \\times 10^{12}\\text{ m}^{-3}$. (a) Calculate the critical plasma frequency $f_p$. (b) For radio waves incident on the ionosphere at an angle of incidence $\\theta_i = 65^\\circ$ relative to the normal, use Snell's law to derive and calculate the Maximum Usable Frequency (MUF) that can still be reflected back to Earth (secant law).",
            "steps": [
                {
                    "stepName": "Step 1: Critical Plasma Frequency Calculation",
                    "math": "f_p = \\frac{1}{2\\pi} \\sqrt{\\frac{n_e e^2}{\\epsilon_0 m_e}} = \\frac{1}{2\\pi} \\sqrt{\\frac{(1.5 \\times 10^{12})(1.602 \\times 10^{-19})^2}{(8.854 \\times 10^{-12})(9.109 \\times 10^{-31})}}\\nf_p = \\frac{1}{2\\pi} \\sqrt{4.777 \\times 10^{14}} = \\frac{2.1856 \\times 10^7}{2\\pi} = 3.478 \\times 10^6\\text{ Hz} \\approx 11.0\\text{ MHz}",
                    "explanation": "Vertical incidence signals ($0^\\circ$) at frequencies above 11.0 MHz will penetrate straight through the ionosphere into outer space."
                },
                {
                    "stepName": "Step 2: Oblique Incidence and the Secant Law",
                    "math": "n_1 \\sin\\theta_i = n_2 \\sin\\theta_r\\n\\text{For total internal reflection at turning point: } \\theta_r = 90^\\circ \\implies \\sin\\theta_i = n = \\sqrt{1 - \\frac{f_p^2}{f^2}}\\n\\sin^2\\theta_i = 1 - \\frac{f_p^2}{f^2} \\implies \\frac{f_p^2}{f^2} = 1 - \\sin^2\\theta_i = \\cos^2\\theta_i\\nf_{\\text{MUF}} = \\frac{f_p}{\\cos\\theta_i} = f_p \\sec\\theta_i",
                    "explanation": "This celebrated relation is known as Martyn's Secant Law for ionospheric radio reflection."
                },
                {
                    "stepName": "Step 3: Maximum Usable Frequency Calculation",
                    "math": "f_{\\text{MUF}} = f_p \\sec(65^\\circ) = \\frac{11.0\\text{ MHz}}{\\cos(65^\\circ)} = \\frac{11.0\\text{ MHz}}{0.4226} = 26.03\\text{ MHz}",
                    "explanation": "Because oblique incidence glances off the ionosphere, shortwave radio operators can communicate across continents at frequencies up to 26 MHz, well above the 11 MHz vertical critical frequency."
                }
            ]
        }
    ]
}

print("Unit 2 built successfully. Sections:", len(UNIT_2["sections"]), "Problems:", len(UNIT_2["problems"]))
