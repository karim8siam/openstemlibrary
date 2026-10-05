# -*- coding: utf-8 -*-
# Unit 3: Waves in Bounded Regions, Waveguides & Resonators

UNIT_3 = {
    "id": "unit-3",
    "number": 3,
    "title": "Waves in Bounded Regions, Waveguides & Cavity Resonators",
    "leadSummary": "Comprehensive mathematical analysis of bounded electromagnetic radiation: rigorous derivation of electromagnetic boundary conditions from Maxwell's integral laws, normal and oblique reflection and refraction at dielectric boundaries, Fresnel reflection and transmission equations for TE and TM polarizations, Brewster's angle, total internal reflection with evanescent decay, metallic boundary reflection, wave propagation between parallel conducting plates, boundary-value eigenvalue problems in rectangular waveguides, TE/TM cutoff frequencies, phase and group velocities, and microwave cavity resonators.",
    "simulations": ["fresnel-reflection", "waveguide-modes"],
    "sections": [
        {
            "secNumber": "3.1",
            "heading": "General Electromagnetic Boundary Conditions at Media Interfaces",
            "content": """
#### Derivation of Boundary Conditions from Maxwell's Integral Equations
When an electromagnetic wave encounters an interface separating two distinct physical media (characterized by $\\epsilon_1, \\mu_1, \\sigma_1$ and $\\epsilon_2, \\mu_2, \\sigma_2$), the fields must satisfy fundamental boundary conditions derived directly from the integral forms of Maxwell's equations.

Let $\\hat{\\mathbf{n}}$ be the unit normal vector pointing from medium 2 into medium 1.

#### 1. Normal Component of Electric Displacement Field ($\\mathbf{D}$)
Construct a Gaussian pillbox of cross-sectional area $\\Delta A$ and height $h$ straddling the interface. Applying Gauss's law $\\oint_S \\mathbf{D} \\cdot d\\mathbf{a} = Q_{f,\\text{enc}}$ in the limit as $h \\to 0$:
$$(\\mathbf{D}_1 \\cdot \\hat{\\mathbf{n}} - \\mathbf{D}_2 \\cdot \\hat{\\mathbf{n}}) \\Delta A = \\sigma_f \\Delta A$$
$$D_{1n} - D_{2n} = \\sigma_f \\quad \\iff \\quad \\epsilon_1 E_{1n} - \\epsilon_2 E_{2n} = \\sigma_f$$
where $\\sigma_f$ is the free surface charge density on the interface. For linear dielectrics without free surface charge ($\\sigma_f = 0$):
$$D_{1n} = D_{2n} \\implies \\epsilon_1 E_{1n} = \\epsilon_2 E_{2n}$$

#### 2. Normal Component of Magnetic Induction Field ($\\mathbf{B}$)
Applying Gauss's law for magnetism $\\oint_S \\mathbf{B} \\cdot d\\mathbf{a} = 0$ over the same pillbox as $h \\to 0$:
$$B_{1n} - B_{2n} = 0 \\implies B_{1n} = B_{2n}$$
**Result:** The normal component of the magnetic induction $\\mathbf{B}$ is **always continuous** across any interface without exception.

#### 3. Tangential Component of Electric Field ($\\mathbf{E}$)
Construct an Amperian loop of width $\\Delta l$ parallel to the interface and height $h$ perpendicular to it. Applying Faraday's law $\\oint_C \\mathbf{E} \\cdot d\\mathbf{l} = -\\frac{d}{dt} \\int_S \\mathbf{B} \\cdot d\\mathbf{a}$:
As $h \\to 0$, the magnetic flux through the loop vanishes ($h \\Delta l \\to 0$), leaving:
$$(E_{1t} - E_{2t}) \\Delta l = 0 \\implies E_{1t} = E_{2t}$$
$$\\hat{\\mathbf{n}} \\times (\\mathbf{E}_1 - \\mathbf{E}_2) = 0$$
**Result:** The tangential component of the electric field is **always continuous** across any boundary.

#### 4. Tangential Component of Magnetic Field Intensity ($\\mathbf{H}$)
Applying the Ampère-Maxwell law $\\oint_C \\mathbf{H} \\cdot d\\mathbf{l} = I_{f,\\text{enc}} + \\frac{d}{dt} \\int_S \\mathbf{D} \\cdot d\\mathbf{a}$:
As $h \\to 0$, the displacement current flux vanishes, but a surface free current density $\\mathbf{K}_f$ perpendicular to the loop can contribute:
$$H_{1t} - H_{2t} = K_{f,\\perp}$$
$$\\hat{\\mathbf{n}} \\times (\\mathbf{H}_1 - \\mathbf{H}_2) = \\mathbf{K}_f$$
For non-conducting dielectric media where no surface free currents exist ($\\mathbf{K}_f = 0$):
$$H_{1t} = H_{2t} \\implies \\frac{B_{1t}}{\\mu_1} = \\frac{B_{2t}}{\\mu_2}$$
"""
        },
        {
            "secNumber": "3.2",
            "heading": "Reflection and Refraction at a Plane Dielectric Interface (Normal Incidence)",
            "content": """
Consider a monochromatic plane wave traveling along $+z$ in medium 1 ($z < 0$, parameters $\\epsilon_1, \\mu_1, n_1$) normally incident upon a flat boundary at $z = 0$ with medium 2 ($z > 0$, parameters $\\epsilon_2, \\mu_2, n_2$).

#### Field Formulations
1. **Incident Wave:**
$$\\mathbf{E}_i(z, t) = E_{0i} e^{i(k_1 z - \\omega t)} \\hat{\\mathbf{x}}, \\quad \\mathbf{B}_i(z, t) = \\frac{E_{0i}}{v_1} e^{i(k_1 z - \\omega t)} \\hat{\\mathbf{y}}$$
2. **Reflected Wave:** (travels along $-z$)
$$\\mathbf{E}_r(z, t) = E_{0r} e^{i(-k_1 z - \\omega t)} \\hat{\\mathbf{x}}, \\quad \\mathbf{B}_r(z, t) = -\\frac{E_{0r}}{v_1} e^{i(-k_1 z - \\omega t)} \\hat{\\mathbf{y}}$$
3. **Transmitted Wave:** (travels along $+z$ in medium 2)
$$\\mathbf{E}_t(z, t) = E_{0t} e^{i(k_2 z - \\omega t)} \\hat{\\mathbf{x}}, \\quad \\mathbf{B}_t(z, t) = \\frac{E_{0t}}{v_2} e^{i(k_2 z - \\omega t)} \\hat{\\mathbf{y}}$$

#### Matching Boundary Conditions at $z = 0$
1. **Continuity of Tangential $\\mathbf{E}$:**
$$E_{0i} + E_{0r} = E_{0t}$$
2. **Continuity of Tangential $\\mathbf{H}$ (assuming $\\mu_1 \\approx \\mu_2 \\approx \\mu_0$):**
$$\\frac{E_{0i}}{v_1} - \\frac{E_{0r}}{v_1} = \\frac{E_{0t}}{v_2} \\implies n_1(E_{0i} - E_{0r}) = n_2 E_{0t}$$

#### Amplitude Reflection and Transmission Coefficients
Solving this $2 \\times 2$ algebraic system:
$$r \\equiv \\frac{E_{0r}}{E_{0i}} = \\frac{n_1 - n_2}{n_1 + n_2}$$
$$t \\equiv \\frac{E_{0t}}{E_{0i}} = \\frac{2n_1}{n_1 + n_2}$$

Notice that if $n_2 > n_1$ (denser medium, e.g., air into glass), $r < 0$, corresponding to a **$\\\\pi$ phase reversal** upon reflection.

#### Energy Conservation: Reflectance ($R$) and Transmittance ($T$)
The time-averaged power reflected and transmitted per unit area are:
$$R \\equiv \\frac{|\\langle \\mathbf{S}_r \\rangle|}{|\\langle \\mathbf{S}_i \\rangle|} = \\left| \\frac{E_{0r}}{E_{0i}} \\right|^2 = \\left( \\frac{n_1 - n_2}{n_1 + n_2} \\right)^2$$
$$T \\equiv \\frac{|\\langle \\mathbf{S}_t \\rangle|}{|\\langle \\mathbf{S}_i \\rangle|} = \\frac{v_2 \\epsilon_2 E_{0t}^2}{v_1 \\epsilon_1 E_{0i}^2} = \\frac{n_2}{n_1} \\left( \\frac{2n_1}{n_1 + n_2} \\right)^2 = \\frac{4 n_1 n_2}{(n_1 + n_2)^2}$$

Summing the two:
$$R + T = \\frac{(n_1 - n_2)^2 + 4n_1 n_2}{(n_1 + n_2)^2} = \\frac{(n_1 + n_2)^2}{(n_1 + n_2)^2} \\equiv 1$$
Energy flux is conserved across the interface.
"""
        },
        {
            "secNumber": "3.3",
            "heading": "Oblique Incidence, Snell's Law, and the Fresnel Equations",
            "content": """
#### Phase Matching and the Laws of Reflection & Refraction
Let a plane wave with wavevector $\\mathbf{k}_i$ strike the interface ($z=0$) at angle of incidence $\\theta_i$ relative to the normal $\\hat{\\mathbf{z}}$. For boundary conditions to hold at all spatial positions $(x, y)$ on the interface and at all times $t$, the spatial phases must match:
$$(\\mathbf{k}_i \\cdot \\mathbf{r})_{z=0} = (\\mathbf{k}_r \\cdot \\mathbf{r})_{z=0} = (\\mathbf{k}_t \\cdot \\mathbf{r})_{z=0}$$
$$k_i \\sin\\theta_i = k_r \\sin\\theta_r = k_t \\sin\\theta_t$$

Since $k_i = k_r = n_1 \\frac{\\omega}{c}$ and $k_t = n_2 \\frac{\\omega}{c}$:
1. **Law of Reflection:** $\\theta_r = \\theta_i$
2. **Snell's Law of Refraction:** $n_1 \\sin\\theta_i = n_2 \\sin\\theta_t$

#### The Two Orthogonal Polarizations
Any arbitrarily polarized plane wave can be decomposed into two fundamental linear modes:
1. **$s$-Polarization (TE / Perpendicular):** Electric field $\\mathbf{E}$ is perpendicular to the plane of incidence.
2. **$p$-Polarization (TM / Parallel):** Electric field $\\mathbf{E}$ lies entirely within the plane of incidence.

#### The Fresnel Equations (for $\\mu_1 = \\mu_2 = \\mu_0$)

#### 1. Perpendicular Polarization ($s$ / TE):
$$r_s = \\frac{E_{0r}}{E_{0i}} = \\frac{n_1 \\cos\\theta_i - n_2 \\cos\\theta_t}{n_1 \\cos\\theta_i + n_2 \\cos\\theta_t} = -\\frac{\\sin(\\theta_i - \\theta_t)}{\\sin(\\theta_i + \\theta_t)}$$
$$t_s = \\frac{E_{0t}}{E_{0i}} = \\frac{2n_1 \\cos\\theta_i}{n_1 \\cos\\theta_i + n_2 \\cos\\theta_t} = \\frac{2\\sin\\theta_t \\cos\\theta_i}{\\sin(\\theta_i + \\theta_t)}$$

#### 2. Parallel Polarization ($p$ / TM):
$$r_p = \\frac{E_{0r}}{E_{0i}} = \\frac{n_2 \\cos\\theta_i - n_1 \\cos\\theta_t}{n_2 \\cos\\theta_i + n_1 \\cos\\theta_t} = \\frac{\\tan(\\theta_i - \\theta_t)}{\\tan(\\theta_i + \\theta_t)}$$
$$t_p = \\frac{E_{0t}}{E_{0i}} = \\frac{2n_1 \\cos\\theta_i}{n_2 \\cos\\theta_i + n_1 \\cos\\theta_t} = \\frac{2\\sin\\theta_t \\cos\\theta_i}{\\sin(\\theta_i + \\theta_t)\\cos(\\theta_i - \\theta_t)}$$
"""
        },
        {
            "secNumber": "3.4",
            "heading": "Brewster's Polarization Angle and External Reflection",
            "content": """
#### Derivation of Brewster's Angle ($\\theta_B$)
Observe the parallel reflection coefficient:
$$r_p = \\frac{\\tan(\\theta_i - \\theta_t)}{\\tan(\\theta_i + \\theta_t)}$$

If the denominator approaches infinity, $r_p$ drops to identically zero. This occurs when:
$$\\theta_i + \\theta_t = \\frac{\\pi}{2} = 90^\\circ \\implies \\theta_t = \\frac{\\pi}{2} - \\theta_i$$

Substitute this into Snell's law:
$$n_1 \\sin\\theta_i = n_2 \\sin\\left( \\frac{\\pi}{2} - \\theta_i \\right) = n_2 \\cos\\theta_i$$
$$\\frac{\\sin\\theta_i}{\\cos\\theta_i} = \\frac{n_2}{n_1} \\implies \\tan\\theta_B = \\frac{n_2}{n_1}$$

This unique angle of incidence is called **Brewster's Angle** (or the polarizing angle):
$$\\theta_B = \\arctan\\left( \\frac{n_2}{n_1} \\right)$$

For an air-to-glass interface ($n_1 = 1.00, n_2 = 1.50$):
$$\\theta_B = \\arctan(1.50) \\approx 56.3^\\circ$$

#### Microscopic Physical Mechanism
When incident light excites atomic bound electrons in medium 2, they oscillate parallel to the transmitted electric field vector $\\mathbf{E}_t$. Oscillating electric dipoles radiate with an intensity proportional to $\\sin^2\\phi$, where $\\phi$ is the angle between the dipole axis and the radiation direction. Because $\\theta_i + \\theta_t = 90^\\circ$, the direction of reflected ray $\\mathbf{k}_r$ lies precisely along the axis of oscillation of the dipoles! An oscillating dipole radiates zero electromagnetic power along its axis of oscillation. Hence, **no reflected wave can be generated for $p$-polarization**.

**Practical Application:** If unpolarized sunlight strikes a glass window or water puddle at Brewster's angle, the reflected light is **100% linearly polarized** perpendicular to the plane of incidence ($s$-polarized). Polarized sunglasses with vertical transmission axes completely filter out this blinding horizontal glare.
"""
        },
        {
            "secNumber": "3.5",
            "heading": "Total Internal Reflection, Evanescent Waves, and Penetration Depth",
            "content": """
#### The Critical Angle ($\\theta_c$)
When an electromagnetic wave travels from an optically denser medium into a rarer medium ($n_1 > n_2$, e.g., glass to air):
$$n_1 \\sin\\theta_i = n_2 \\sin\\theta_t \\implies \\sin\\theta_t = \\frac{n_1}{n_2} \\sin\\theta_i$$

As $\\theta_i$ increases, $\\theta_t$ reaches $90^\\circ$ before $\\theta_i$ does. The angle of incidence for which $\\theta_t = 90^\\circ$ is the **critical angle**:
$$\\sin\\theta_c = \\frac{n_2}{n_1} \\implies \\theta_c = \\arcsin\\left( \\frac{n_2}{n_1} \\right)$$

For water into air ($n_1 = 1.333, n_2 = 1.00$): $\\theta_c = \\arcsin(1/1.333) \\approx 48.6^\\circ$.
For glass into air ($n_1 = 1.50, n_2 = 1.00$): $\\theta_c = \\arcsin(1/1.50) \\approx 41.8^\\circ$.

#### Total Internal Reflection ($\\theta_i > \\theta_c$)
When $\\theta_i > \\theta_c$, $\\sin\\theta_t = \\frac{n_1}{n_2} \\sin\\theta_i > 1$. The cosine of the transmitted angle becomes purely imaginary:
$$\\cos\\theta_t = \\sqrt{1 - \\sin^2\\theta_t} = \\sqrt{1 - \\left(\\frac{n_1}{n_2}\\sin\\theta_i\\right)^2} = i \\sqrt{\\left(\\frac{n_1}{n_2}\\sin\\theta_i\\right)^2 - 1} \\equiv i \\Gamma$$

Substituting into the transmitted spatial wave term $e^{i\\mathbf{k}_t \\cdot \\mathbf{r}} = e^{i(k_{tx} x + k_{tz} z)}$:
$$k_{tz} = k_t \\cos\\theta_t = i k_t \\Gamma = i \\kappa$$
where $\\kappa = \\frac{\\omega}{c} \\sqrt{n_1^2 \\sin^2\\theta_i - n_2^2}$.

The transmitted electric field is therefore:
$$\\mathbf{E}_t(x, z, t) = \\mathbf{E}_{0t} e^{-\\kappa z} e^{i(k_{tx} x - \\omega t)}$$

#### Properties of the Evanescent Wave
1. **Exponential Decay:** The field amplitude decays exponentially into medium 2 with distance $z$ from the interface.
2. **Characteristic Penetration Depth ($d_p$):**
$$d_p = \\frac{1}{\\kappa} = \\frac{\\lambda_0}{2\\pi \\sqrt{n_1^2 \\sin^2\\theta_i - n_2^2}}$$
3. **Zero Time-Averaged Power Transport:** The time-averaged Poynting vector normal to the boundary is identically zero: $\\langle S_z \\rangle = 0$. All energy is reflected back into medium 1 ($R = |r|^2 \\equiv 1.00$).
4. **Frustrated Total Internal Reflection (FTIR):** If a third medium is placed within a distance $z < d_p$, photons tunnel through the gap via quantum-like electromagnetic barrier penetration, transmitting energy into the third medium.
"""
        },
        {
            "secNumber": "3.6",
            "heading": "Metallic Reflection at Optical and Microwave Frequencies",
            "content": """
When an electromagnetic wave strikes a good conductor or metal (conductivity $\\sigma$), Snell's law and the Fresnel equations generalize by introducing the complex refractive index:
$$\\tilde{n} = n + i\\kappa$$
where $\\kappa = \\frac{c\\alpha}{\\omega}$ is the extinction coefficient.

At normal incidence from air ($n_1 = 1$) into metal:
$$r = \\frac{1 - \\tilde{n}}{1 + \\tilde{n}} = \\frac{1 - (n + i\\kappa)}{1 + (n + i\\kappa)}$$
The reflectance is:
$$R = |r|^2 = \\frac{(1 - n)^2 + \\kappa^2}{(1 + n)^2 + \\kappa^2}$$

For good conductors at microwave and radio frequencies, $\\kappa \\approx n \\gg 1$:
$$R \\approx 1 - \\frac{4n}{n^2 + \\kappa^2} \\approx 1 - \\frac{4}{n} = 1 - 2\\sqrt{\\frac{2\\epsilon_0 \\omega}{\\sigma}}$$

This relation is the **Hagen-Rubens formula**. For polished metals (such as gold, silver, and copper), $R > 0.99$ for infrared and microwave radiation, making metals ideal mirrors and waveguide boundaries.
"""
        },
        {
            "secNumber": "3.7",
            "heading": "Waveguides: Parallel Conducting Plates & Rectangular Waveguides",
            "content": """
#### Boundary Value Problem in Rectangular Waveguides
Consider a hollow rectangular metallic pipe of inner width $a$ along $x$ ($0 \\le x \\le a$) and height $b$ along $y$ ($0 \\le y \\le b$), with walls made of an ideal conductor (conductivity $\\sigma \\to \\infty$). The wave propagates along $+z$:
$$\\mathbf{E}(x, y, z, t) = \\mathbf{E}_0(x, y) e^{i(k_z z - \\omega t)}$$

Because the walls are perfect conductors, boundary conditions dictate that tangential $\\mathbf{E}$ and normal $\\mathbf{B}$ must vanish at the boundaries:
$$E_z = 0, \\quad E_y = 0 \\quad \\text{at } x = 0, a$$
$$E_z = 0, \\quad E_x = 0 \\quad \\text{at } y = 0, b$$

#### Decomposition into Transverse Electric (TE) and Transverse Magnetic (TM) Modes
1. **Transverse Electric (TE) Modes ($E_z = 0$):**
   The longitudinal magnetic field $H_z$ satisfies the 2D Helmholtz equation:
   $$\\left( \\frac{\\partial^2}{\\partial x^2} + \\frac{\\partial^2}{\\partial y^2} + k_c^2 \\right) H_z = 0, \\quad k_c^2 = \\frac{\\omega^2}{c^2} - k_z^2$$
   Applying the boundary condition $\\frac{\\partial H_z}{\\partial n} = 0$:
   $$H_z(x, y) = H_0 \\cos\\left( \\frac{m\\pi x}{a} \\right) \\cos\\left( \\frac{n\\pi y}{b} \\right)$$

2. **Transverse Magnetic (TM) Modes ($H_z = 0$):**
   Applying $E_z = 0$ on the walls:
   $$E_z(x, y) = E_0 \\sin\\left( \\frac{m\\pi x}{a} \\right) \\sin\\left( \\frac{n\\pi y}{b} \\right)$$

#### Cutoff Frequencies ($f_{c,mn}$)
The transverse cutoff wavenumber is:
$$k_{c,mn} = \\sqrt{ \\left(\\frac{m\\pi}{a}\\right)^2 + \\left(\\frac{n\\pi}{b}\\right)^2 }$$
The **cutoff frequency** for mode $(m, n)$ is:
$$f_{c,mn} = \\frac{c}{2\\pi} k_{c,mn} = \\frac{c}{2} \\sqrt{ \\left(\\frac{m}{a}\\right)^2 + \\left(\\frac{n}{b}\\right)^2 }$$

#### Propagation Constant ($k_z$), Guide Wavelength ($\\lambda_g$), and Velocities
$$k_z = \\sqrt{\\frac{\\omega^2}{c^2} - k_c^2} = \\frac{\\omega}{c} \\sqrt{1 - \\left(\\frac{f_c}{f}\\right)^2}$$

- **If $f < f_c$:** $k_z$ is imaginary. The mode is evanescent and attenuates exponentially; **no wave propagation occurs**.
- **If $f > f_c$:** $k_z$ is real and propagation proceeds.

The **guide wavelength** $\\lambda_g$ inside the pipe is:
$$\\lambda_g = \\frac{2\\pi}{k_z} = \\frac{\\lambda_0}{\\sqrt{1 - (f_c/f)^2}} > \\lambda_0$$

The **phase velocity** exceeds the speed of light:
$$v_p = \\frac{\\omega}{k_z} = \\frac{c}{\\sqrt{1 - (f_c/f)^2}} > c$$

The **group velocity** (energy velocity) is strictly subluminal:
$$v_g = \\frac{d\\omega}{dk_z} = c \\sqrt{1 - \\left(\\frac{f_c}{f}\\right)^2} < c$$
Notice that:
$$v_p \\cdot v_g = c^2$$

#### The Dominant Mode ($\\text{TE}_{10}$)
In standard rectangular waveguides with $a > b$, the lowest cutoff frequency belongs to the **$\\text{TE}_{10}$ mode** ($m=1, n=0$):
$$f_{c,10} = \\frac{c}{2a}$$
For this dominant mode, the fields are:
$$E_y(x) = E_0 \\sin\\left(\\frac{\\pi x}{a}\\right) e^{i(k_z z - \\omega t)}$$
$$H_x(x) = -\\frac{k_z}{\\omega \\mu_0} E_0 \\sin\\left(\\frac{\\pi x}{a}\\right) e^{i(k_z z - \\omega t)}$$
$$H_z(x) = i \\frac{\\pi}{\\omega \\mu_0 a} E_0 \\cos\\left(\\frac{\\pi x}{a}\\right) e^{i(k_z z - \\omega t)}$$
"""
        },
        {
            "secNumber": "3.8",
            "heading": "Resonant Cavities and Quality Factor (Q)",
            "content": """
#### Resonant Microwave Cavities
Closing both ends of a rectangular waveguide with conducting plates at $z = 0$ and $z = d$ forms a closed metallic enclosure called a **cavity resonator**.

Boundary conditions force standing waves along all three spatial axes:
$$f_{mnp} = \\frac{c}{2} \\sqrt{ \\left(\\frac{m}{a}\\right)^2 + \\left(\\frac{n}{b}\\right)^2 + \\left(\\frac{p}{d}\\right)^2 }$$
where $m, n, p$ are mode integers.

#### Quality Factor ($Q$)
Due to the non-zero surface resistance $R_s$ of the metallic cavity walls, electromagnetic energy stored in the cavity is dissipated as thermal Joule losses. The **Quality Factor** $Q$ measures the sharpness of the cavity resonance:
$$Q \\equiv \\omega \\frac{\\text{Time-averaged Energy Stored}}{\\text{Power Dissipated in Cavity Walls}} = \\omega \\frac{U}{P_{\\text{loss}}}$$

For microwave cavities constructed from copper or silver, $Q$ typically ranges from $10^4$ to $10^5$, and in superconducting niobium RF cavities used in particle colliders, $Q$ exceeds $10^{10}$.
"""
        }
    ],
    "problems": [
        {
            "id": "p3-1",
            "title": "Example 3.1: Air-Glass Interface Reflection and Transmission at Normal Incidence",
            "difficulty": "Easy",
            "question": "A monochromatic laser beam in air ($n_1 = 1.00$) is incident normally upon a flat optical crown glass window ($n_2 = 1.52$). Calculate: (a) the amplitude reflection coefficient $r$ and transmission coefficient $t$, (b) the percentage of incident power reflected (Reflectance $R$), (c) the percentage of power transmitted (Transmittance $T$), and (d) the phase shift experienced by the reflected electric field.",
            "steps": [
                {
                    "stepName": "Step 1: Amplitude Coefficients",
                    "math": "r = \\frac{n_1 - n_2}{n_1 + n_2} = \\frac{1.00 - 1.52}{1.00 + 1.52} = \\frac{-0.52}{2.52} = -0.2063\\nt = \\frac{2n_1}{n_1 + n_2} = \\frac{2(1.00)}{2.52} = +0.7937",
                    "explanation": "The negative sign on $r$ indicates an immediate $\\pi$ ($180^\\circ$) phase inversion for the reflected electric field."
                },
                {
                    "stepName": "Step 2: Power Reflectance",
                    "math": "R = |r|^2 = (-0.2063)^2 = 0.0426 \\implies 4.26\\%",
                    "explanation": "Approximately 4.26% of incident light power is lost to Fresnel surface reflection at each air-glass boundary."
                },
                {
                    "stepName": "Step 3: Power Transmittance",
                    "math": "T = \\frac{n_2}{n_1} |t|^2 = \\frac{1.52}{1.00} (0.7937)^2 = 1.52 \\times 0.6299 = 0.9574 \\implies 95.74\\%\\nR + T = 4.26\\% + 95.74\\% = 100.00\\%",
                    "explanation": "Energy conservation is verified exactly."
                }
            ]
        },
        {
            "id": "p3-2",
            "title": "Example 3.2: Complete Polarization of Sunlight Reflected from Water",
            "difficulty": "Medium",
            "question": "Unpolarized sunlight reflects from the smooth surface of a freshwater lake ($n_2 = 1.333$) into air ($n_1 = 1.00$). Determine: (a) Brewster's angle $\\theta_B$, (b) the corresponding refraction angle $\\theta_t$, (c) the reflectance for $s$-polarization $R_s$ at this angle, and (d) explain why reflected light is 100% linearly polarized.",
            "steps": [
                {
                    "stepName": "Step 1: Brewster Angle Calculation",
                    "math": "\\tan\\theta_B = \\frac{n_2}{n_1} = \\frac{1.333}{1.00} \\implies \\theta_B = \\arctan(1.333) = 53.12^\\circ",
                    "explanation": "At an angle of incidence of $53.12^\\circ$, Brewster's condition is satisfied."
                },
                {
                    "stepName": "Step 2: Refraction Angle Calculation",
                    "math": "\\theta_t = 90^\\circ - \\theta_B = 90^\\circ - 53.12^\\circ = 36.88^\\circ",
                    "explanation": "The reflected and refracted rays are precisely orthogonal to one another: $\\theta_r + \\theta_t = 90^\\circ$."
                },
                {
                    "stepName": "Step 3: Reflectance for Perpendicular Polarization",
                    "math": "r_s = -\\frac{\\sin(\\theta_i - \\theta_t)}{\\sin(\\theta_i + \\theta_t)} = -\\frac{\\sin(53.12^\\circ - 36.88^\\circ)}{\\sin(90^\\circ)} = -\\sin(16.24^\\circ) = -0.2796\\nR_s = |r_s|^2 = (-0.2796)^2 = 0.0782 \\implies 7.82\\%\\nR_p = 0.00\\%",
                    "explanation": "Because $R_p = 0$, all reflected photons belong exclusively to the perpendicular state ($s$-polarization), producing 100% linearly polarized horizontal glare."
                }
            ]
        },
        {
            "id": "p3-3",
            "title": "Example 3.3: X-Band Rectangular Waveguide Cutoff, Dispersion, and Velocities",
            "difficulty": "Hard",
            "question": "A standard WR-90 X-band rectangular waveguide has internal dimensions $a = 2.286\\text{ cm}$ and $b = 1.016\\text{ cm}$. For operation at $f = 9.80\\text{ GHz}$: (a) calculate the cutoff frequencies for modes $\\text{TE}_{10}$, $\\text{TE}_{20}$, and $\\text{TE}_{01}$, (b) confirm single-mode operation, (c) calculate the guide wavelength $\\lambda_g$, (d) calculate the phase velocity $v_p$, and (e) calculate the group velocity $v_g$.",
            "steps": [
                {
                    "stepName": "Step 1: Cutoff Frequency Calculations",
                    "math": "f_{c,10} = \\frac{c}{2a} = \\frac{3.00 \\times 10^{10}\\text{ cm/s}}{2(2.286\\text{ cm})} = 6.557\\text{ GHz}\\nf_{c,20} = \\frac{c}{a} = 2 \\times 6.557\\text{ GHz} = 13.114\\text{ GHz}\\nf_{c,01} = \\frac{c}{2b} = \\frac{3.00 \\times 10^{10}\\text{ cm/s}}{2(1.016\\text{ cm})} = 14.764\\text{ GHz}",
                    "explanation": "At $f = 9.80\\text{ GHz}$, since $f_{c,10} < f < f_{c,20} < f_{c,01}$, only the dominant $\\text{TE}_{10}$ mode can propagate; all higher-order modes are evanescent."
                },
                {
                    "stepName": "Step 2: Guide Wavelength Calculation",
                    "math": "\\lambda_0 = \\frac{c}{f} = \\frac{3.00 \\times 10^8\\text{ m/s}}{9.80 \\times 10^9\\text{ Hz}} = 3.061\\text{ cm}\\n\\lambda_g = \\frac{\\lambda_0}{\\sqrt{1 - (f_{c,10}/f)^2}} = \\frac{3.061\\text{ cm}}{\\sqrt{1 - (6.557/9.80)^2}} = \\frac{3.061\\text{ cm}}{\\sqrt{1 - 0.4477}} = \\frac{3.061\\text{ cm}}{0.7431} = 4.119\\text{ cm}",
                    "explanation": "The wavelength inside the waveguide is stretched by 35% compared to free space."
                },
                {
                    "stepName": "Step 3: Phase and Group Velocities",
                    "math": "v_p = \\frac{c}{\\sqrt{1 - (f_{c,10}/f)^2}} = \\frac{3.00 \\times 10^8\\text{ m/s}}{0.7431} = 4.037 \\times 10^8\\text{ m/s} = 1.346 \\, c\\nv_g = c \\sqrt{1 - (f_{c,10}/f)^2} = (3.00 \\times 10^8\\text{ m/s})(0.7431) = 2.229 \\times 10^8\\text{ m/s} = 0.743 \\, c\\nv_p \\times v_g = (1.346 c)(0.743 c) = c^2",
                    "explanation": "The phase velocity exceeds $c$ without violating causality because signal information travels at group velocity $v_g < c$."
                }
            ]
        },
        {
            "id": "p3-4",
            "title": "Example 3.4: Resonant Frequency and Quality Factor (Q) of a Microwave Cavity",
            "difficulty": "Hard",
            "question": "A cubic resonant cavity has dimensions $a = b = d = 5.0\\text{ cm}$ with walls made of pure copper ($\\sigma = 5.8 \\times 10^7\\text{ S/m}$). Calculate: (a) the lowest resonant frequency $f_{101}$ for the dominant $\\text{TE}_{101}$ mode, (b) the skin depth $\\delta$ at resonance, and (c) the theoretical quality factor $Q$ of the cavity.",
            "steps": [
                {
                    "stepName": "Step 1: Resonant Frequency Calculation",
                    "math": "f_{101} = \\frac{c}{2} \\sqrt{\\frac{1}{a^2} + 0 + \\frac{1}{d^2}} = \\frac{c}{2} \\sqrt{\\frac{2}{a^2}} = \\frac{c}{\\sqrt{2} a}\\nf_{101} = \\frac{3.00 \\times 10^8\\text{ m/s}}{\\sqrt{2}(0.05\\text{ m})} = \\frac{3.00 \\times 10^8}{0.07071} = 4.243 \\times 10^9\\text{ Hz} = 4.243\\text{ GHz}",
                    "explanation": "The fundamental resonant frequency is 4.243 GHz in the C-band."
                },
                {
                    "stepName": "Step 2: Skin Depth at Resonance",
                    "math": "\\delta = \\frac{1}{\\sqrt{\\pi f \\mu_0 \\sigma}} = \\frac{1}{\\sqrt{\\pi (4.243 \\times 10^9)(4\\pi \\times 10^{-7})(5.8 \\times 10^7)}} = 1.013 \\times 10^{-6}\\text{ m} = 1.013\\,\\mu\\text{m}",
                    "explanation": "Microwave wall currents penetrate only 1.01 micrometers into the copper surface."
                },
                {
                    "stepName": "Step 3: Quality Factor (Q) Calculation",
                    "math": "\\text{For a cubic cavity of side } a: Q = \\frac{a}{3\\delta}\\nQ = \\frac{0.05\\text{ m}}{3(1.013 \\times 10^{-6}\\text{ m})} = \\frac{0.05}{3.039 \\times 10^{-6}} = 16,450",
                    "explanation": "The extraordinarily high Q-factor of 16,450 confirms minimal internal dissipation, storing electromagnetic energy for over 16,000 oscillation cycles before decaying."
                }
            ]
        }
    ]
}

print("Unit 3 built successfully. Sections:", len(UNIT_3["sections"]), "Problems:", len(UNIT_3["problems"]))
