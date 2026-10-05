# -*- coding: utf-8 -*-
# Unit 5: Scattering of Electromagnetic Radiation

UNIT_5 = {
    "id": "unit-5",
    "number": 5,
    "title": "Scattering of Electromagnetic Radiation",
    "leadSummary": "Comprehensive mathematical theory of electromagnetic scattering: definitions of differential and total cross-sections, Thomson scattering of unpolarized and polarized radiation by free electrons, classical electron radius, forced damped harmonic oscillator models of bound electrons, complete mathematical derivation of Rayleigh scattering and the omega^4 (lambda^-4) frequency law, optical polarization of skylight, and resonance scattering and atomic fluorescence.",
    "simulations": ["scattering-simulator"],
    "sections": [
        {
            "secNumber": "5.1",
            "heading": "Concepts of Differential and Total Scattering Cross-Sections",
            "content": """
#### Definition of the Scattering Process
When an incident electromagnetic wave impinges upon a localized target (such as an electron, an atom, a molecule, or an aerosol particle), the electric and magnetic fields exert forces on the charges in the target. These accelerated charges oscillate and re-radiate electromagnetic waves in all directions. This redistribution of electromagnetic energy away from the forward propagation direction is called **scattering**.

Let the incident wave carry time-averaged intensity $I_{\\text{inc}} = \\langle S_{\\text{inc}} \\rangle$ (power per unit area). The scattered power $dP_{\\text{scat}}$ emitted into a differential solid angle element $d\\Omega = \\sin\\theta \\, d\\theta \\, d\\phi$ at distance $r$ is detected as scattered intensity $I_{\\text{scat}}(r, \\theta, \\phi)$:
$$dP_{\\text{scat}} = I_{\\text{scat}}(r, \\theta, \\phi) r^2 d\\Omega$$

#### The Differential Scattering Cross-Section
The **differential scattering cross-section** $\\frac{d\\sigma}{d\\Omega}$ is defined as the ratio of the power scattered per unit solid angle to the incident intensity:
$$\\frac{d\\sigma}{d\\Omega} \\equiv \\frac{1}{I_{\\text{inc}}} \\frac{dP_{\\text{scat}}}{d\\Omega} = \\frac{r^2 I_{\\text{scat}}(r, \\theta, \\phi)}{I_{\\text{inc}}} \\quad [\\text{m}^2 / \\text{sr}]$$

Physically, $\\frac{d\\sigma}{d\\Omega}$ represents the effective geometric area that the target presents to the incident beam for scattering radiation into direction $(\\theta, \\phi)$.

#### The Total Scattering Cross-Section
Integrating the differential cross-section over all $4\\pi$ steradians yields the **total scattering cross-section** $\\sigma_{\\text{total}}$:
$$\\sigma_{\\text{total}} \\equiv \\oint_{4\\pi} \\left( \\frac{d\\sigma}{d\\Omega} \\right) d\\Omega = \\int_0^{2\\pi} d\\phi \\int_0^\\pi \\left( \\frac{d\\sigma}{d\\Omega} \\right) \\sin\\theta \\, d\\theta \\quad [\\text{m}^2]$$

The total power extracted from the incident beam by scattering is simply:
$$P_{\\text{total}} = \\sigma_{\\text{total}} I_{\\text{inc}}$$
"""
        },
        {
            "secNumber": "5.2",
            "heading": "Thomson Scattering of Electromagnetic Waves by Free Electrons",
            "content": """
#### Interaction with a Free Unbound Electron
Consider an unbound, free electron (mass $m_e$, charge $-e$) in a vacuum, illuminated by a linearly polarized monochromatic plane wave:
$$\\mathbf{E}(\\mathbf{r}, t) = E_0 \\cos(\\mathbf{k} \\cdot \\mathbf{r} - \\omega t) \\hat{\\mathbf{z}}$$

In the non-relativistic regime ($v \\ll c$), the magnetic Lorentz force $\\mathbf{F}_B = -e(\\mathbf{v} \\times \\mathbf{B})$ is negligible compared to the electric force $\\mathbf{F}_E = -e\\mathbf{E}$ by a factor of $v/c$. Newton's second law for the electron motion is:
$$m_e \\mathbf{a}(t) = -e \\mathbf{E}(t) \\implies \\mathbf{a}(t) = -\\frac{e E_0}{m_e} \\cos(\\omega t) \\hat{\\mathbf{z}}$$

#### Re-Radiated Radiation Fields
The accelerating electron emits dipole radiation with an induced acceleration amplitude $a_0 = \\frac{e E_0}{m_e}$. From Larmor's radiation formula, the electric field in the far radiation zone at distance $r$ is:
$$\\mathbf{E}_{\\text{scat}}(r, \\theta, t) = \\frac{e a(t - r/c)}{4\\pi \\epsilon_0 c^2 r} \\sin\\theta \\hat{\\boldsymbol{\\theta}} = -\\frac{e^2 E_0}{4\\pi \\epsilon_0 m_e c^2} \\left( \\frac{\\sin\\theta}{r} \\right) \\cos(\\omega(t - r/c)) \\hat{\\boldsymbol{\\theta}}$$
where $\\theta$ is the angle between the acceleration axis $\\hat{\\mathbf{z}}$ and the observation direction $\\hat{\\mathbf{r}}$.

#### The Classical Electron Radius ($r_0$)
We define the fundamental physical constant known as the **classical electron radius**:
$$r_0 \\equiv \\frac{e^2}{4\\pi \\epsilon_0 m_e c^2} \\approx 2.81794 \\times 10^{-15} \\text{ m}$$

The scattered electric field amplitude simplifies to:
$$E_{\\text{scat}} = -r_0 E_0 \\frac{\\sin\\theta}{r}$$

The scattered intensity is:
$$I_{\\text{scat}} = \\frac{1}{2} c \\epsilon_0 E_{\\text{scat}}^2 = \\frac{1}{2} c \\epsilon_0 E_0^2 \\frac{r_0^2 \\sin^2\\theta}{r^2} = I_{\\text{inc}} \\frac{r_0^2 \\sin^2\\theta}{r^2}$$

#### Differential and Total Thomson Cross-Sections
1. **For Linearly Polarized Incident Light:**
$$\\left( \\frac{d\\sigma}{d\\Omega} \\right)_{\\text{pol}} = r_0^2 \\sin^2\\theta$$

2. **For Unpolarized Incident Light:**
Averaging over all polarization angles yields the angular dependence in terms of the scattering angle $\\Theta$ between incident ray $\\mathbf{k}_i$ and scattered ray $\\mathbf{k}_s$:
$$\\left( \\frac{d\\sigma}{d\\Omega} \\right)_{\\text{unpol}} = r_0^2 \\frac{1 + \\cos^2\\Theta}{2}$$

3. **The Total Thomson Scattering Cross-Section ($\\sigma_T$):**
Integrating over the solid angle:
$$\\sigma_T = \\int_0^{2\\pi} d\\phi \\int_0^\\pi r_0^2 \\left( \\frac{1 + \\cos^2\\Theta}{2} \\right) \\sin\\Theta \\, d\\Theta = \\pi r_0^2 \\int_{-1}^1 (1 + u^2) du = \\pi r_0^2 \\left[ 2 + \\frac{2}{3} \\right] = \\frac{8\\pi}{3} r_0^2$$

Substituting numerical values:
$$\\sigma_T = \\frac{8\\pi}{3} (2.81794 \\times 10^{-15} \\text{ m})^2 = 6.65246 \\times 10^{-29} \\text{ m}^2 = 0.6652 \\, \\text{barn}$$

#### Profound Physical Properties of Thomson Scattering
1. **Frequency Independence:** The Thomson cross-section $\\sigma_T$ is **completely independent of the frequency $\\omega$ of the incident wave**. X-rays, microwaves, and radio waves are scattered by a free electron with the exact same cross-section!
2. **Forward-Backward Symmetry:** The angular factor $\\frac{1 + \\cos^2\\Theta}{2}$ is symmetric between forward scattering ($\\Theta = 0^\\circ$) and back-scattering ($\\Theta = 180^\\circ$).
"""
        },
        {
            "secNumber": "5.3",
            "heading": "Scattering by Bound Electrons & Forced Damped Oscillations",
            "content": """
#### The Harmonically Bound Electron Model
In real gases, liquids, and solids, electrons are not free; they are bound to atomic nuclei by electrostatic restoring forces. We model a bound atomic electron as a classical damped harmonic oscillator with natural resonance frequency $\\omega_0$ and radiative damping constant $\\gamma$.

Under the driving force of an incident monochromatic plane wave $\\mathbf{E}(t) = E_0 e^{-i\\omega t} \\hat{\\mathbf{z}}$, the equation of motion is:
$$m_e \\left( \\frac{d^2 x}{dt^2} + \\gamma \\frac{dx}{dt} + \\omega_0^2 x \\right) = -e E_0 e^{-i\\omega t}$$

Assuming the steady-state sinusoidal response $x(t) = x_0 e^{-i\\omega t}$:
$$m_e \\left( -\\omega^2 - i\\gamma \\omega + \\omega_0^2 \\right) x_0 = -e E_0$$
$$x_0 = -\\frac{e E_0 / m_e}{\\omega_0^2 - \\omega^2 - i\\gamma \\omega}$$

The induced oscillating electric dipole moment is:
$$p(t) = -e x(t) = \\frac{e^2 E_0 / m_e}{\\omega_0^2 - \\omega^2 - i\\gamma \\omega} e^{-i\\omega t} \\equiv p_0 e^{-i\\omega t}$$

#### Radiation and Total Cross-Section Formula
Substituting the dipole moment amplitude $p_0$ into the Larmor power formula $P_{\\text{scat}} = \\frac{p_0^2 \\omega^4}{12\\pi \\epsilon_0 c^3}$:
$$P_{\\text{scat}} = \\frac{\\omega^4}{12\\pi \\epsilon_0 c^3} \\frac{e^4 E_0^2 / m_e^2}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$

Dividing by the incident intensity $I_{\\text{inc}} = \\frac{1}{2} c \\epsilon_0 E_0^2$:
$$\\sigma(\\omega) = \\frac{P_{\\text{scat}}}{I_{\\text{inc}}} = \\left( \\frac{8\\pi}{3} r_0^2 \\right) \\frac{\\omega^4}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$

In terms of the Thomson cross-section $\\sigma_T$:
$$\\sigma(\\omega) = \\sigma_T \\frac{\\omega^4}{(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2}$$

This master equation governs the entire spectrum of electromagnetic scattering across physics.
"""
        },
        {
            "secNumber": "5.4",
            "heading": "Rayleigh Scattering: The ω⁴ Law and the Color of the Daytime Sky",
            "content": """
#### Derivation of the Low-Frequency Limit ($\\omega \\ll \\omega_0$)
For atmospheric air molecules ($N_2, O_2$), electronic absorption transitions lie deep in the far-ultraviolet (resonance wavelengths $\\lambda_0 \\approx 100 - 150\\text{ nm}$, so $\\omega_0 \\approx 1.5 \\times 10^{16}\\text{ rad/s}$). Visible light spans $\\lambda \\approx 400 - 700\\text{ nm}$ (frequencies $\\omega \\approx 3 - 5 \\times 10^{15}\\text{ rad/s}$).

Therefore, for visible sunlight traversing the atmosphere:
$$\\omega \\ll \\omega_0$$

In this low-frequency limit, the denominator $(\\omega_0^2 - \\omega^2)^2 + \\gamma^2 \\omega^2 \\approx \\omega_0^4$. The scattering cross-section reduces to **Lord Rayleigh's celebrated scattering law** (1871):
$$\\sigma_{\\text{Rayleigh}}(\\omega) = \\sigma_T \\left( \\frac{\\omega}{\\omega_0} \\right)^4$$

Since $\\omega = \\frac{2\\pi c}{\\lambda}$, the scattering cross-section is inversely proportional to the **fourth power of wavelength**:
$$\\sigma_{\\text{Rayleigh}}(\\lambda) \\propto \\frac{1}{\\lambda^4}$$

#### Why the Daytime Sky is Blue
Compare blue sunlight ($\\lambda_{\\text{blue}} \\approx 430\\text{ nm}$) to red sunlight ($\\lambda_{\\text{red}} \\approx 680\\text{ nm}$):
$$\\frac{\\sigma(\\lambda_{\\text{blue}})}{\\sigma(\\lambda_{\\text{red}})} = \\left( \\frac{680\\text{ nm}}{430\\text{ nm}} \\right)^4 \\approx (1.581)^4 \\approx 6.25$$
Blue photons are scattered by atmospheric nitrogen and oxygen molecules over **6 times more intensely** than red photons. When you look anywhere in the sky away from the direct disc of the Sun, you are viewing this scattered light, which is heavily dominated by short blue and violet wavelengths.

#### Why Sunsets are Deep Red
At sunset and sunrise, sunlight travels through a very long oblique path through Earth's atmosphere (air mass factor up to 40 times greater than at noon). By the **Beer-Lambert transmission law**:
$$I(x) = I_0 e^{-N \\sigma_{\\text{scat}} x}$$
The short blue and green wavelengths are almost entirely scattered out of the direct beam line of sight. Only the least-scattered long wavelengths—orange and deep red—penetrate the thick atmospheric column to reach the observer's eyes.
"""
        },
        {
            "secNumber": "5.5",
            "heading": "Polarization of Scattered Sunlight and Neutral Points",
            "content": """
#### Polarization Mechanism of Skylight
Unpolarized incident sunlight traveling along $+z$ possesses electric field vibrations in all directions within the $xy$-plane.

Consider an observer viewing scattered light from an air molecule at an angle of $90^\\circ$ relative to the incident solar beam (e.g., looking toward the horizon while the Sun is overhead):
1. Oscillations of the molecule's electrons parallel to the line of sight cannot radiate toward the observer (because oscillating dipoles emit zero power along their axis of oscillation).
2. Only oscillations perpendicular to both the solar beam and the line of sight produce radiation reaching the observer.

Consequently, sunlight scattered at an angle of **$90^\\circ$ from the Sun is nearly 100% linearly polarized**. Bees and migratory birds utilize this celestial polarization pattern (the e-vector sky compass) for biological navigation even on overcast days.
"""
        },
        {
            "secNumber": "5.6",
            "heading": "Resonance Scattering and Atomic Fluorescence",
            "content": """
#### Near-Resonance Behavior ($\\omega \\approx \\omega_0$)
When the frequency of incident radiation closely approaches an atomic resonance ($\\omega \\to \\omega_0$):
$$\\omega_0^2 - \\omega^2 = (\\omega_0 + \\omega)(\\omega_0 - \\omega) \\approx 2\\omega_0 (\\omega_0 - \\omega)$$

The cross-section becomes:
$$\\sigma_{\\text{res}}(\\omega) = \\frac{8\\pi}{3} r_0^2 \\frac{\\omega_0^4}{4\\omega_0^2(\\omega - \\omega_0)^2 + \\gamma^2 \\omega_0^2} = \\frac{2\\pi r_0^2 \\omega_0^2}{3} \\frac{1}{(\\omega - \\omega_0)^2 + (\\gamma/2)^2}$$

At exact resonance ($\\omega = \\omega_0$), the cross-section reaches a peak value:
$$\\sigma_{\\text{max}} = \\frac{8\\pi r_0^2 \\omega_0^2}{3 \\gamma^2}$$

Using the classical radiative damping constant $\\gamma = \\frac{2 r_0 \\omega_0^2}{3 c}$:
$$\\sigma_{\\text{max}} = \\frac{3}{2\\pi} \\left( \\frac{2\\pi c}{\\omega_0} \\right)^2 = \\frac{3}{2\\pi} \\lambda_0^2$$

**Profound Physical Result:** At atomic resonance, the effective scattering cross-section is proportional to the **square of the wavelength $\\lambda_0^2$**, rather than the physical geometric size of the atom ($r_{\\text{atom}}^2 \\sim 10^{-20}\\text{ m}^2$). For yellow sodium D-light ($\\lambda_0 = 589\\text{ nm}$), $\\sigma_{\\text{max}} \\approx 1.6 \\times 10^{-13}\\text{ m}^2$, which is over **seven orders of magnitude larger** than the geometric cross-section of a sodium atom! This phenomenon is known as **resonance fluorescence**.
"""
        }
    ],
    "problems": [
        {
            "id": "p5-1",
            "title": "Example 5.1: Thomson Scattering Cross-Section of Solar X-Rays in Coronal Plasma",
            "difficulty": "Easy",
            "question": "A burst of solar flare X-rays ($E = 10\\text{ keV}$, $\\lambda = 0.124\\text{ nm}$) passes through a solar coronal plasma loop containing free electrons with density $n_e = 10^{15}\\text{ m}^{-3}$ and column depth $L = 5 \\times 10^7\\text{ m}$. (a) Calculate the classical electron radius $r_0$. (b) Calculate the total Thomson cross-section $\\sigma_T$. (c) Determine the optical depth $\\tau = n_e \\sigma_T L$ and the fraction of X-ray beam power scattered by the plasma.",
            "steps": [
                {
                    "stepName": "Step 1: Classical Electron Radius",
                    "math": "r_0 = \\frac{e^2}{4\\pi \\epsilon_0 m_e c^2} = \\frac{(1.602 \\times 10^{-19})^2}{4\\pi (8.854 \\times 10^{-12})(9.109 \\times 10^{-31})(3.00 \\times 10^8)^2} = 2.818 \\times 10^{-15}\\text{ m}",
                    "explanation": "This fundamental scale represents the radius at which the electrostatic self-energy of a sphere equals the electron's rest mass energy $m_e c^2$."
                },
                {
                    "stepName": "Step 2: Total Thomson Cross-Section",
                    "math": "\\sigma_T = \\frac{8\\pi}{3} r_0^2 = \\frac{8\\pi}{3} (2.818 \\times 10^{-15}\\text{ m})^2 = 6.652 \\times 10^{-29}\\text{ m}^2",
                    "explanation": "Every free electron presents a microscopic scattering cross-section of $0.665\\text{ barn}$ to the beam."
                },
                {
                    "stepName": "Step 3: Optical Depth and Fraction Scattered",
                    "math": "\\tau = n_e \\sigma_T L = (10^{15}\\text{ m}^{-3})(6.652 \\times 10^{-29}\\text{ m}^2)(5 \\times 10^7\\text{ m}) = 3.326 \\times 10^{-6}\\n\\text{Fraction Scattered } = 1 - e^{-\\tau} \\approx \\tau = 3.33 \\times 10^{-6} \\implies 0.00033\\%",
                    "explanation": "Because the coronal plasma is optically thin ($\\tau \\ll 1$), virtually all X-rays pass through unhindered, allowing solar satellite telescopes to image the flare directly."
                }
            ]
        },
        {
            "id": "p5-2",
            "title": "Example 5.2: Ratio of Rayleigh Scattering Cross-Sections for Violet vs Red Sunlight",
            "difficulty": "Easy",
            "question": "Calculate the exact ratio of the Rayleigh scattering cross-sections for extreme violet sunlight ($\\lambda_1 = 390\\text{ nm}$) compared to extreme red sunlight ($\\lambda_2 = 720\\text{ nm}$) by molecular nitrogen and oxygen in Earth's atmosphere.",
            "steps": [
                {
                    "stepName": "Step 1: Rayleigh Wavelength Scaling Law",
                    "math": "\\sigma_{\\text{Rayleigh}}(\\lambda) \\propto \\frac{1}{\\lambda^4} \\implies \\frac{\\sigma(\\lambda_1)}{\\sigma(\\lambda_2)} = \\left( \\frac{\\lambda_2}{\\lambda_1} \\right)^4",
                    "explanation": "Because visible light frequencies are well below the UV resonance frequencies of nitrogen molecules, the $\\lambda^{-4}$ law holds strictly."
                },
                {
                    "stepName": "Step 2: Numerical Ratio Evaluation",
                    "math": "\\frac{\\sigma(390\\text{ nm})}{\\sigma(720\\text{ nm})} = \\left( \\frac{720\\text{ nm}}{390\\text{ nm}} \\right)^4 = (1.84615)^4 = 11.616 \\approx 11.6",
                    "explanation": "Violet photons are scattered nearly 12 times more intensely than red photons, causing the predominant blue-violet illumination of clear skies."
                }
            ]
        },
        {
            "id": "p5-3",
            "title": "Example 5.3: Degree of Polarization of Skylight Scattered at 90° from the Sun",
            "difficulty": "Medium",
            "question": "Unpolarized sunlight of intensity $I_0$ strikes an air molecule. (a) For single Rayleigh scattering observed at angle $\\Theta$ from the incident beam, write down the intensities of the two orthogonal polarization components $I_\\perp$ and $I_\\parallel$. (b) Define the degree of linear polarization $P(\\Theta)$ and evaluate it at $\\Theta = 90^\\circ$. (c) Explain why real atmospheric skylight at $90^\\circ$ exhibits a degree of polarization of approximately 75% to 85% rather than a theoretical 100%.",
            "steps": [
                {
                    "stepName": "Step 1: Polarized Component Intensities",
                    "math": "I_\\perp(\\Theta) = \\frac{1}{2} I_0 \\left( \\frac{d\\sigma_0}{d\\Omega} \\right), \\quad I_\\parallel(\\Theta) = \\frac{1}{2} I_0 \\left( \\frac{d\\sigma_0}{d\\Omega} \\right) \\cos^2\\Theta",
                    "explanation": "The perpendicular component has full dipole projection and is independent of $\\Theta$, whereas the parallel component varies as $\\cos^2\\Theta$."
                },
                {
                    "stepName": "Step 2: Degree of Linear Polarization",
                    "math": "P(\\Theta) \\equiv \\frac{I_\\perp - I_\\parallel}{I_\\perp + I_\\parallel} = \\frac{1 - \\cos^2\\Theta}{1 + \\cos^2\\Theta} = \\frac{\\sin^2\\Theta}{1 + \\cos^2\\Theta}\\n\\text{At } \\Theta = 90^\\circ: P(90^\\circ) = \\frac{\\sin^2(90^\\circ)}{1 + \\cos^2(90^\\circ)} = \\frac{1}{1 + 0} = 1.00 \\implies 100\\%",
                    "explanation": "Single scattering from an ideal isotropic spherical molecule produces complete 100% linear polarization at $90^\\circ$."
                },
                {
                    "stepName": "Step 3: Real Atmospheric Depolarization Factors",
                    "math": "P_{\\text{real}} \\approx 75\\% - 85\\%",
                    "explanation": "The observed polarization is reduced due to: (1) molecular anisotropy of non-spherical $N_2$ and $O_2$ diatomic molecules (depolarization factor $\\rho_n \\approx 0.03$), (2) multiple scattering events in thick air columns, and (3) background scattering from unpolarized aerosol dust and water haze."
                }
            ]
        },
        {
            "id": "p5-4",
            "title": "Example 5.4: Resonance Scattering Cross-Section at the Sodium D-Line (589 nm)",
            "difficulty": "Hard",
            "question": "A tunable dye laser is tuned precisely to the sodium atom D2 resonance line ($\\lambda_0 = 589.0\\text{ nm}$, transition frequency $\\omega_0 = 3.20 \\times 10^{15}\\text{ rad/s}$). (a) Calculate the theoretical maximum resonance scattering cross-section $\\sigma_{\\text{max}} = \\frac{3}{2\\pi} \\lambda_0^2$. (b) Compare this cross-section with the geometric area of the sodium atom ($r_{\\text{atom}} \\approx 0.18\\text{ nm}$). (c) If a sodium vapor cell has density $n = 10^{16}\\text{ atoms/m}^3$, calculate the photon penetration depth (attenuation length $l = 1/(n\\sigma)$).",
            "steps": [
                {
                    "stepName": "Step 1: Maximum Resonance Cross-Section",
                    "math": "\\sigma_{\\text{max}} = \\frac{3}{2\\pi} \\lambda_0^2 = \\frac{3}{2\\pi} (5.890 \\times 10^{-7}\\text{ m})^2 = \\frac{3}{6.283} (3.469 \\times 10^{-13}\\text{ m}^2) = 1.656 \\times 10^{-13}\\text{ m}^2",
                    "explanation": "The resonance cross-section is $1.66 \\times 10^{-13}\\text{ m}^2$ (over $1.6 \\times 10^{15}\\text{ barns}$)."
                },
                {
                    "stepName": "Step 2: Comparison with Geometric Atomic Size",
                    "math": "A_{\\text{atom}} = \\pi r_{\\text{atom}}^2 = \\pi (0.18 \\times 10^{-9}\\text{ m})^2 = 1.018 \\times 10^{-19}\\text{ m}^2\\n\\frac{\\sigma_{\\text{max}}}{A_{\\text{atom}}} = \\frac{1.656 \\times 10^{-13}\\text{ m}^2}{1.018 \\times 10^{-19}\\text{ m}^2} = 1.63 \\times 10^6",
                    "explanation": "The effective resonant scattering cross-section is over 1.6 million times larger than the physical size of the sodium atom."
                },
                {
                    "stepName": "Step 3: Attenuation Depth in Sodium Vapor",
                    "math": "l = \\frac{1}{n \\sigma_{\\text{max}}} = \\frac{1}{(10^{16}\\text{ m}^{-3})(1.656 \\times 10^{-13}\\text{ m}^2)} = \\frac{1}{1656\\text{ m}^{-1}} = 6.04 \\times 10^{-4}\\text{ m} = 0.604\\text{ mm}",
                    "explanation": "Resonant light cannot penetrate more than 0.6 millimeters into the vapor before being completely scattered and re-emitted in all directions."
                }
            ]
        }
    ]
}

print("Unit 5 built successfully. Sections:", len(UNIT_5["sections"]), "Problems:", len(UNIT_5["problems"]))
