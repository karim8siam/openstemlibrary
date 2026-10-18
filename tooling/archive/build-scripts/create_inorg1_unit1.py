# -*- coding: utf-8 -*-
"""
create_inorg1_unit1.py
Creates build_inorg1_unit1.py: Unit 1 for Inorganic Chemistry I
Massive 2x depth (>9,000 words), unskipped derivations, zero course numbers.
"""

import sys

content = r'''# -*- coding: utf-8 -*-
"""
build_inorg1_unit1.py
Unit 1: Quantum Theory & Electronic Structure of the Atom
Master-level inorganic chemistry textbook module with 2x depth,
complete mathematical derivations, and strictly zero course numbers.
"""

def get_unit1():
    return {
        "number": 1,
        "title": "Quantum Theory & Electronic Structure of the Atom",
        "leadSummary": "Foundational quantum mechanical foundations of inorganic chemistry: the wave-particle nature of electromagnetic radiation, Planck's blackbody quantization, the photoelectric effect and Compton scattering, historical evolution of atomic models from Rutherford scattering to the Bohr-Sommerfeld quantization of angular momentum and the Rydberg spectral formula, de Broglie matter wave duality, Heisenberg's uncertainty principle, the three-dimensional time-independent Schrödinger wave equation in spherical polar coordinates, exact separation of variables for hydrogenic systems into radial functions and spherical harmonics, physical interpretation of quantum numbers (n, l, ml, ms), radial distribution probability functions 4πr²R²(r) and nodal topologies, polyelectronic atoms and central field approximation, Pauli exclusion principle and antisymmetric Slater determinants, Aufbau building-up principle, Hund's rule of maximum multiplicity and exchange energy stabilization, and Slater's empirical rules for electron screening and effective nuclear charge (Z_eff).",
        "sections": [
            {
                "secNumber": "1.1",
                "title": "The Wave-Particle Nature of Light & Quantized Energy",
                "content": r"""Inorganic chemistry is fundamentally anchored in the quantum electronic structure of atoms. The macroscopic chemical reactivity, coordination geometry, and magnetic properties of elements across the periodic table cannot be understood without the quantum mechanical principles governing electrons bound within atomic potentials.

### The Breakdown of Classical Electromagnetic Theory

In nineteenth-century classical physics, James Clerk Maxwell unified electricity and magnetism into a continuous wave theory governed by Maxwell's equations:
$$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}, \quad \nabla \cdot \mathbf{B} = 0, \quad \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \tag{1.1}$$
In free space ($\rho = 0, \mathbf{J} = \mathbf{0}$), electromagnetic waves propagate as transverse vector oscillations at the invariant vacuum speed of light:
$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 2.99792458 \times 10^8\text{ m}\cdot\text{s}^{-1} \tag{1.2}$$
The wave nature of light was experimentally solidified through Thomas Young's double-slit interference (1801) and Augustin-Jean Fresnel's diffraction experiments. A monochromatic continuous electromagnetic wave is completely characterized by its frequency $\nu$ ($\text{s}^{-1}$ or $\text{Hz}$), wavelength $\lambda$ ($\text{m}$), and wavenumber $\tilde{\nu} \equiv 1/\lambda$ ($\text{m}^{-1}$ or $\text{cm}^{-1}$):
$$c = \nu \lambda \iff \tilde{\nu} = \frac{\nu}{c} = \frac{1}{\lambda} \tag{1.3}$$
However, three monumental physical phenomena demonstrated that classical continuous electrodynamics fails catastrophically when describing energy exchange between radiation and matter at atomic length scales:
1. **Blackbody Radiation & The Ultraviolet Catastrophe**
2. **The Photoelectric Effect**
3. **Discrete Atomic Emission & Absorption Line Spectra**

### Blackbody Radiation & Planck's Quantum Postulate

An ideal **blackbody** is an idealized physical object that absorbs all incident electromagnetic radiation regardless of frequency or angle of incidence, and emits radiation in complete thermodynamic equilibrium with its walls at absolute temperature $T$.

#### The Classical Rayleigh-Jeans Catastrophe
Applying classical equipartition of energy ($k_B T$ per standing wave mode in a three-dimensional cavity) to the density of electromagnetic standing wave modes per unit volume in frequency interval $[\nu, \nu + d\nu]$:
$$g(\nu) d\nu = \frac{8\pi \nu^2}{c^3} d\nu \tag{1.4}$$
Lord Rayleigh and Sir James Jeans derived the spectral energy density $\rho(\nu, T)$:
$$\rho_{\text{RJ}}(\nu, T) d\nu = g(\nu) \langle E \rangle d\nu = \frac{8\pi \nu^2}{c^3} (k_B T) d\nu \tag{1.5}$$
As frequency approaches the ultraviolet and beyond ($\nu \to \infty$), Eq. (1.5) predicts that the radiated energy density diverges to infinity:
$$\lim_{\nu \to \infty} \rho_{\text{RJ}}(\nu, T) = \infty, \quad \int_0^\infty \rho_{\text{RJ}}(\nu, T) d\nu = \infty \tag{1.6}$$
This unphysical divergence, termed the **Ultraviolet Catastrophe** by Paul Ehrenfest, meant classical physics predicted that every warm object should instantly incinerate the universe with infinite ultraviolet and X-ray energy.

#### Planck's Revolutionary Quantum Postulate (1900)
On December 14, 1900, Max Planck resolved the catastrophe by introducing a radical, non-classical postulate:
> **Planck's Quantum Postulate**:
> The microscopic subatomic harmonic oscillators in the cavity walls cannot absorb or emit energy continuously. Instead, an oscillator of frequency $\nu$ can only exist in discrete energy states separated by integer multiples of an elementary quantum of action:
> $$E_n = n h \nu, \quad n \in \{0, 1, 2, 3, \dots\} \tag{1.7}$$
> where $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$ is **Planck's Constant**.

Using Boltzmann statistical mechanics, the thermal probability of finding an oscillator in state $n$ is given by the canonical distribution $P_n = e^{-n h \nu / k_B T} / Z$, where the partition function $Z$ is a geometric series:
$$Z = \sum_{n=0}^\infty e^{-n h \nu / k_B T} = \frac{1}{1 - e^{-h\nu / k_B T}} \tag{1.8}$$
The average thermal energy $\langle E \rangle$ of a quantum oscillator is:
$$\langle E \rangle = -\frac{\partial \ln Z}{\partial (1/k_B T)} = \frac{\sum_{n=0}^\infty (n h \nu) e^{-n h \nu / k_B T}}{\sum_{n=0}^\infty e^{-n h \nu / k_B T}} = \frac{h \nu}{e^{h\nu / k_B T} - 1} \tag{1.9}$$
Multiplying the mode density $g(\nu)$ by this quantum average energy yields **Planck's Radiation Law**:
$$\rho(\nu, T) d\nu = \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu / k_B T} - 1} d\nu \tag{1.10}$$
Expressed in terms of wavelength $\lambda$ using $|d\nu| = (c/\lambda^2) d\lambda$:
$$\rho(\lambda, T) d\lambda = \frac{8\pi h c}{\lambda^5} \frac{1}{e^{h c / (\lambda k_B T)} - 1} d\lambda \tag{1.11}$$

#### Asymptotic Limits of Planck's Law:
1. **Low Frequency / High Temperature Limit ($h\nu \ll k_B T$)**:
   Taylor expanding the exponential $e^{h\nu / k_B T} \approx 1 + \frac{h\nu}{k_B T}$:
   $$\rho(\nu, T) \approx \frac{8\pi h \nu^3}{c^3} \frac{1}{1 + \frac{h\nu}{k_B T} - 1} = \frac{8\pi \nu^2}{c^3} k_B T = \rho_{\text{RJ}}(\nu, T) \tag{1.12}$$
   Planck's quantum distribution smoothly recovers the classical Rayleigh-Jeans law in the classical correspondence limit.
2. **High Frequency Limit ($h\nu \gg k_B T$)**:
   The denominator is dominated by the exponential $e^{h\nu / k_B T} \gg 1$:
   $$\rho(\nu, T) \approx \frac{8\pi h \nu^3}{c^3} e^{-h\nu / k_B T} \tag{1.13}$$
   This exponential suppression extinguishes the ultraviolet catastrophe completely.
3. **Wien's Displacement Law**:
   Differentiating Eq. (1.11) with respect to $\lambda$ and setting $d\rho/d\lambda = 0$ yields the transcendental equation $5(1 - e^{-x}) = x$ where $x = hc / (\lambda_{\text{max}} k_B T) \approx 4.965114$. Therefore:
   $$\lambda_{\text{max}} T = \frac{h c}{4.965114 k_B} = b \approx 2.89777 \times 10^{-3}\text{ m}\cdot\text{K} \tag{1.14}$$
4. **Stefan-Boltzmann Law**:
   Integrating Eq. (1.10) over all frequencies ($0 \le \nu < \infty$) with standard definite integral $\int_0^\infty \frac{x^3}{e^x - 1} dx = \frac{\pi^4}{15}$ yields total radiant exitance:
   $$M = \frac{c}{4} \int_0^\infty \rho(\nu, T) d\nu = \left( \frac{2\pi^5 k_B^4}{15 c^2 h^3} \right) T^4 = \sigma_{\text{SB}} T^4 \tag{1.15}$$
   where the **Stefan-Boltzmann Constant** is $\sigma_{\text{SB}} \approx 5.670374 \times 10^{-8}\text{ W}\cdot\text{m}^{-2}\cdot\text{K}^{-4}$.

---

### The Photoelectric Effect & Einstein's Light Quanta (1905)

In 1887, Heinrich Hertz discovered that ultraviolet light incident on a spark gap promoted electrical discharge. Philipp Lenard subsequently discovered three puzzling experimental facts:
1. **Zero Time Delay**: Electrons are ejected virtually instantaneously ($< 10^{-9}\text{ s}$) upon illumination, even at ultra-low light intensities. Classically, a spread-out wave would require hours or days to accumulate sufficient localized energy to dislodge an electron.
2. **Intensity Independence of Kinetic Energy**: Increasing the intensity of the light increases the number of ejected electrons (photocurrent), but does **not** increase their kinetic energy.
3. **Threshold Frequency ($\nu_0$)**: If the frequency of incident radiation is below a critical threshold $\nu_0$ characteristic of the metal, **zero electrons** are emitted regardless of beam intensity.

In 1905, Albert Einstein extended Planck's hypothesis by proposing that electromagnetic radiation is not merely emitted and absorbed in quanta, but **travels through space as localized, indivisible packets of energy**—later named **photons** by Gilbert Lewis (1926).
Each photon carries an energy:
$$E = h \nu = \hbar \omega \tag{1.16}$$
where $\hbar \equiv \frac{h}{2\pi} \approx 1.0545718 \times 10^{-34}\text{ J}\cdot\text{s}$ is the reduced Planck constant, and $\omega = 2\pi\nu$ is angular frequency.

When a photon collides with an electron bound in a metal lattice, the interaction is a 1-to-1 inelastic collision. A portion of the photon's energy is consumed to overcome the electrostatic binding barrier of the surface, known as the **work function ($\Phi$)**, and any remaining energy is converted into the maximum kinetic energy of the ejected photoelectron:
$$h \nu = \Phi + K_{\text{max}} = h \nu_0 + \frac{1}{2} m_e v_{\text{max}}^2 \tag{1.17}$$
$$K_{\text{max}} = e V_s = h \nu - \Phi \tag{1.18}$$
where $V_s$ is the **stopping potential** required to retard the photocurrent to zero, and $e \approx 1.602176634 \times 10^{-19}\text{ C}$ is the elementary charge.
Plotting $V_s$ versus frequency $\nu$ yields a universal straight line:
$$V_s = \left(\frac{h}{e}\right) \nu - \frac{\Phi}{e} \tag{1.19}$$
The slope is universally $h/e$, independent of the metal cathode, as experimentally verified with colossal precision by Robert Millikan in 1916.

---

### The Compton Effect: Photons Carry Linear Momentum (1923)

Arthur H. Compton demonstrated that photons possess particle-like relativistic momentum by scattering monochromatic X-rays of wavelength $\lambda$ from stationary electrons in graphite:
From special relativity, the energy-momentum dispersion relation for a particle with rest mass $m_0$ is:
$$E^2 = (p c)^2 + (m_0 c^2)^2 \tag{1.20}$$
For a photon, $m_0 = 0$, which yields the fundamental photon momentum:
$$p = \frac{E}{c} = \frac{h \nu}{c} = \frac{h}{\lambda} \tag{1.21}$$
Applying relativistic conservation of four-momentum to the elastic collision between a photon and a stationary electron ($E_e = m_e c^2, \mathbf{p}_e = \mathbf{0}$):
* **Conservation of Energy**:
  $$h \nu + m_e c^2 = h \nu' + E_e' = h \nu' + \sqrt{(p_e' c)^2 + (m_e c^2)^2} \tag{1.22}$$
* **Conservation of Linear Momentum**:
  $$\mathbf{p}_{\gamma} = \mathbf{p}_{\gamma}' + \mathbf{p}_e' \implies (\mathbf{p}_e')^2 = p_\gamma^2 + (p_\gamma')^2 - 2 p_\gamma p_\gamma' \cos\theta \tag{1.23}$$
Eliminating the final electron momentum $p_e'$ between Eqs. (1.22) and (1.23) yields the **Compton Scattering Formula**:
$$\Delta \lambda \equiv \lambda' - \lambda = \frac{h}{m_e c} (1 - \cos\theta) = \lambda_C (1 - \cos\theta) \tag{1.24}$$
where $\theta$ is the photon scattering angle, and $\lambda_C$ is the **Compton Wavelength of the electron**:
$$\lambda_C \equiv \frac{h}{m_e c} \approx 2.4263102 \times 10^{-12}\text{ m} = 0.02426\text{ Å} = 2.426\text{ pm} \tag{1.25}$$
Compton scattering provided conclusive, undeniable proof that light quanta behave as discrete relativistic particles carrying momentum $\mathbf{p} = \hbar \mathbf{k}$.

---

### Atomic Emission Line Spectra & The Rydberg Formula

When a gas-discharge tube containing atomic hydrogen is energized with high electrical voltage, the emitted light is not a continuous rainbow, but a collection of sharp, discrete spectral lines.
In 1885, Swiss high school teacher Johann Jakob Balmer empirically discovered that the wavelengths of the visible lines of hydrogen (now known as the Balmer series: $H_\alpha$ at $656.3\text{ nm}$, $H_\beta$ at $486.1\text{ nm}$, $H_\gamma$ at $434.0\text{ nm}$, $H_\delta$ at $410.2\text{ nm}$) obeyed the formula:
$$\lambda = B \left(\frac{n^2}{n^2 - 4}\right), \quad n = 3, 4, 5, \dots \tag{1.26}$$
In 1888, Johannes Rydberg generalized this expression into terms of wavenumber $\tilde{\nu} = 1/\lambda$:
$$\tilde{\nu} = \frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right), \quad n_2 > n_1 \tag{1.27}$$
where $R_H \approx 109\,677.58\text{ cm}^{-1} \approx 1.0967758 \times 10^7\text{ m}^{-1}$ is the **Rydberg Constant for Hydrogen**.

| Spectral Series | Lower State ($n_1$) | Upper States ($n_2$) | Spectral Region | Discovery Date |
| :--- | :---: | :---: | :---: | :---: |
| **Lyman Series** | $n_1 = 1$ | $n_2 = 2, 3, 4, \dots$ | Ultraviolet (UV) | 1906 (Theodore Lyman) |
| **Balmer Series** | $n_1 = 2$ | $n_2 = 3, 4, 5, \dots$ | Visible & Near UV | 1885 (Johann Balmer) |
| **Paschen Series** | $n_1 = 3$ | $n_2 = 4, 5, 6, \dots$ | Near Infrared (IR) | 1908 (Friedrich Paschen) |
| **Brackett Series** | $n_1 = 4$ | $n_2 = 5, 6, 7, \dots$ | Intermediate Infrared | 1922 (Frederick Brackett) |
| **Pfund Series** | $n_1 = 5$ | $n_2 = 6, 7, 8, \dots$ | Far Infrared | 1924 (August Pfund) |
| **Humphreys Series**| $n_1 = 6$ | $n_2 = 7, 8, 9, \dots$ | Far Infrared | 1953 (Curtis Humphreys) |

Why should an atom emit only these sharp, discrete mathematical integers? Classical physics could offer no explanation: an electron orbiting a positive nucleus would continuously radiate energy, spiraling into the nucleus in less than $10^{-10}$ seconds. A new model of the atom was imperative."""
            },
            {
                "secNumber": "1.2",
                "title": "Evolution of Atomic Models: From Rutherford to Bohr & Sommerfeld",
                "content": r"""The physical nature of the atom underwent rapid conceptual revolutions in the early twentieth century, transitioning from Thomson's static electrostatics to the planetary nuclear model, and culminating in the Bohr-Sommerfeld semi-classical quantization framework.

### Thomson's "Plum Pudding" Model (1897–1904)

Following his 1897 cathode-ray tube discovery of the electron ($e/m_e \approx 1.76 \times 10^{11}\text{ C}\cdot\text{kg}^{-1}$), J. J. Thomson proposed that the atom consists of a diffuse, uniform sphere of positive electric charge (radius $\sim 10^{-10}\text{ m}$) within which negatively charged electrons are embedded like plums in a pudding.
While this model explained overall electrical neutrality and qualitative optical dispersion, it predicted that all alpha particles ($\alpha \equiv \text{He}^{2+}$) passing through thin metal foils should experience only negligible small-angle deflections ($\ll 1^\circ$).

---

### The Rutherford Alpha Scattering Experiment & The Nuclear Model (1909–1911)

Under Ernest Rutherford's direction, Hans Geiger and Ernest Marsden directed a collimated beam of high-energy $\alpha$-particles ($5.5\text{ MeV}$ from radioactive bismuth/radium) at an ultra-thin gold foil ($\sim 400\text{ nm}$ thick, $\sim 1000$ atoms deep). While the vast majority ($>99.99\%$) passed straight through with negligible deflections, approximately 1 in 8,000 was scattered through colossal angles greater than $90^\circ$, with some rebounding directly backwards toward the source ($\theta \approx 180^\circ$).
Rutherford later famously remarked: *"It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you."*

#### Rutherford Scattering Differential Cross-Section Derivation
Rutherford modeled the collision as classical Coulomb repulsion between a point-like alpha particle (charge $q_1 = +2e$) and a heavy, stationary point nucleus (charge $q_2 = +Ze$):
$$F_e = \frac{1}{4\pi\varepsilon_0} \frac{2 Z e^2}{r^2} \tag{1.28}$$
For an alpha particle with mass $m_\alpha$, incident velocity $v_0$, and impact parameter $b$, angular momentum conservation ($L = m_\alpha v_0 b$) and energy conservation yield the classical trajectory as a hyperbola. The scattering angle $\theta$ is related to the impact parameter $b$ by:
$$b = \frac{Z e^2}{2\pi \varepsilon_0 m_\alpha v_0^2} \cot\left(\frac{\theta}{2}\right) \tag{1.29}$$
The differential cross-section per unit solid angle $d\Omega = 2\pi \sin\theta d\theta$ is:
$$\frac{d\sigma}{d\Omega} = \left| \frac{b}{\sin\theta} \frac{db}{d\theta} \right| = \left( \frac{Z e^2}{4\pi \varepsilon_0 \cdot 2 m_\alpha v_0^2} \right)^2 \frac{1}{\sin^4(\theta/2)} = \left( \frac{Z e^2}{8\pi \varepsilon_0 K_\alpha} \right)^2 \frac{1}{\sin^4(\theta/2)} \tag{1.30}$$
Equation (1.30) is **Rutherford's Scattering Formula**. Geiger and Marsden verified the exact $\csc^4(\theta/2)$ dependence across five orders of magnitude.

#### Distance of Closest Approach & Nuclear Radius ($R_N$)
For a head-on collision ($\theta = 180^\circ, b = 0$), all initial kinetic energy $K_\alpha$ is converted into electrostatic potential energy at the turning point $d_{\text{min}}$:
$$K_\alpha = \frac{1}{4\pi\varepsilon_0} \frac{2 Z e^2}{d_{\text{min}}} \implies d_{\text{min}} = \frac{2 Z e^2}{4\pi\varepsilon_0 K_\alpha} \tag{1.31}$$
For gold ($Z = 79$) and $K_\alpha = 7.7\text{ MeV}$:
$$d_{\text{min}} = \frac{(8.988 \times 10^9) \times 2 \times 79 \times (1.602 \times 10^{-19})^2}{7.7 \times 10^6 \times 1.602 \times 10^{-19}} \approx 2.95 \times 10^{-14}\text{ m} \approx 30\text{ fm} \tag{1.32}$$
Thus, the positive charge and virtually all mass of the atom are concentrated in a tiny core of radius $R_N \sim 10^{-15}\text{ to } 10^{-14}\text{ m}$, while the electrons occupy a surrounding volume $10^5$ times larger ($R_{\text{atom}} \sim 10^{-10}\text{ m}$).

---

### The Instability of the Classical Planetary Atom

While Rutherford established the nuclear topology of the atom, classical physics rendered it fatally unstable:
According to Larmor's classical electrodynamic formula, any accelerating electric charge radiates power at a rate:
$$P = \frac{e^2 a^2}{6\pi \varepsilon_0 c^3} \tag{1.33}$$
An electron moving in a circular orbit of radius $r$ experiences centripetal acceleration $a = v^2/r = \frac{e^2}{4\pi\varepsilon_0 m_e r^2}$. Substituting into Larmor's formula:
$$P = \frac{e^2}{6\pi \varepsilon_0 c^3} \left( \frac{e^2}{4\pi \varepsilon_0 m_e r^2} \right)^2 = \frac{e^6}{96 \pi^3 \varepsilon_0^3 m_e^2 c^3 r^4} \tag{1.34}$$
As the electron loses total energy $E = -\frac{e^2}{8\pi\varepsilon_0 r}$, its orbital radius decays:
$$\frac{dE}{dt} = \frac{e^2}{8\pi\varepsilon_0 r^2} \frac{dr}{dt} = -P \implies \frac{dr}{dt} = -\frac{e^4}{12 \pi^2 \varepsilon_0^2 m_e^2 c^3 r^2} \tag{1.35}$$
Separating variables and integrating from initial atomic radius $r_0 \approx 10^{-10}\text{ m}$ to $r = 0$:
$$\tau_{\text{collapse}} = \int_0^{\tau} dt = -\frac{12 \pi^2 \varepsilon_0^2 m_e^2 c^3}{e^4} \int_{r_0}^0 r^2 dr = \frac{4 \pi^2 \varepsilon_0^2 m_e^2 c^3 r_0^3}{e^4} \approx 1.5 \times 10^{-11}\text{ s} \tag{1.36}$$
Classically, matter cannot exist: all electrons must collapse into their nuclei within 15 picoseconds, emitting a continuous death-spiral streak of radiation!

---

### The Bohr Model of Hydrogenic Atoms (1913)

In 1913, Danish physicist Niels Bohr rescued atomic physics by formulating three non-classical postulates:
1. **Postulate of Stationary States**: Electrons move in stable circular orbits around the positive nucleus without radiating electromagnetic energy.
2. **Quantization of Orbital Angular Momentum**: The only allowed stationary orbits are those for which the orbital angular momentum $L$ is an integer multiple of $\hbar = h / (2\pi)$:
   $$L = m_e v r = n \hbar = n \frac{h}{2\pi}, \quad n \in \{1, 2, 3, \dots\} \tag{1.37}$$
3. **Bohr Frequency Condition**: Emission or absorption of radiation occurs only when an electron undergoes a discrete quantum jump between two stationary states $E_i$ and $E_f$, releasing or absorbing a single photon:
   $$\Delta E = |E_i - E_f| = h \nu = \frac{h c}{\lambda} \tag{1.38}$$

#### Rigorous Mathematical Derivation of Hydrogenic States (Atomic Number $Z$)
Consider an electron of mass $m_e$ and charge $-e$ orbiting a nucleus of charge $+Ze$ at radius $r_n$ with speed $v_n$.
The electrostatic Coulomb attraction provides the required centripetal acceleration:
$$\frac{1}{4\pi\varepsilon_0} \frac{Z e^2}{r_n^2} = \frac{m_e v_n^2}{r_n} \implies m_e v_n^2 r_n = \frac{Z e^2}{4\pi\varepsilon_0} \tag{1.39}$$
From Bohr's quantization condition, $v_n = \frac{n \hbar}{m_e r_n}$. Substitute into Eq. (1.39):
$$m_e \left( \frac{n^2 \hbar^2}{m_e^2 r_n^2} \right) r_n = \frac{Z e^2}{4\pi\varepsilon_0} \implies \frac{n^2 \hbar^2}{m_e r_n} = \frac{Z e^2}{4\pi\varepsilon_0}$$
Solving explicitly for the **Bohr Orbital Radii ($r_n$)**:
$$r_n = \frac{4\pi \varepsilon_0 \hbar^2}{m_e e^2} \frac{n^2}{Z} = a_0 \frac{n^2}{Z} \tag{1.40}$$
where $a_0$ is the **Bohr Radius** (the radius of ground-state hydrogen $n=1, Z=1$):
$$a_0 \equiv \frac{4\pi \varepsilon_0 \hbar^2}{m_e e^2} = \frac{\varepsilon_0 h^2}{\pi m_e e^2} \approx 5.2917721 \times 10^{-11}\text{ m} = 0.52918\text{ Å} = 52.92\text{ pm} \tag{1.41}$$

Solving for the **Orbital Velocity ($v_n$)**:
$$v_n = \frac{n \hbar}{m_e r_n} = \frac{Z e^2}{4\pi \varepsilon_0 \hbar} \frac{1}{n} = c \alpha \frac{Z}{n} \tag{1.42}$$
where $\alpha$ is the dimensionless **Fine Structure Constant**:
$$\alpha \equiv \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137.035999} \approx 7.29735 \times 10^{-3} \tag{1.43}$$
For hydrogen in the ground state ($n=1, Z=1$), $v_1 / c = \alpha \approx 1/137 \approx 0.73\%$, proving that non-relativistic mechanics is an excellent approximation for light atoms.

#### Total Hydrogenic Energy Levels ($E_n$)
Total energy is the sum of kinetic energy $K$ and Coulomb potential energy $V$:
$$K = \frac{1}{2} m_e v_n^2 = \frac{1}{2} \left( \frac{Z e^2}{4\pi\varepsilon_0 r_n} \right) = \frac{Z e^2}{8\pi\varepsilon_0 r_n} \tag{1.44}$$
$$V = -\frac{1}{4\pi\varepsilon_0} \frac{Z e^2}{r_n} \tag{1.45}$$
Notice that $K = -\frac{1}{2}V$ and $E_n = K + V = \frac{1}{2}V$, in exact accordance with the **Virial Theorem**.
Substituting $r_n$ from Eq. (1.40):
$$E_n = -\frac{Z e^2}{8\pi\varepsilon_0 r_n} = -\frac{m_e Z^2 e^4}{32 \pi^2 \varepsilon_0^2 \hbar^2} \frac{1}{n^2} = -\left( \frac{m_e e^4}{8 \varepsilon_0^2 h^2} \right) \frac{Z^2}{n^2} \tag{1.46}$$
Defining the **Rydberg Energy Unit** $R_\infty$:
$$R_\infty \equiv \frac{m_e e^4}{8 \varepsilon_0^2 h^2} \approx 2.179872 \times 10^{-18}\text{ J} \approx 13.605698\text{ eV} \tag{1.47}$$
Thus:
$$E_n = -13.606\text{ eV} \times \frac{Z^2}{n^2} \tag{1.48}$$

#### Derivation of the Theoretical Rydberg Constant
From the third postulate, transition from upper level $n_2$ to lower level $n_1$ emits a photon of wavenumber $\tilde{\nu}$:
$$\tilde{\nu} = \frac{1}{\lambda} = \frac{\Delta E}{h c} = \frac{E_{n_2} - E_{n_1}}{h c} = \left( \frac{m_e Z^2 e^4}{8 \varepsilon_0^2 h^3 c} \right) \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right) \tag{1.49}$$
Comparing Eq. (1.49) with the empirical Rydberg formula Eq. (1.27) yields the fundamental theoretical identity:
$$R_\infty = \frac{m_e e^4}{8 \varepsilon_0^2 h^3 c} \approx 109\,737.31568\text{ cm}^{-1} \tag{1.50}$$

#### Nuclear Motion & Reduced Mass Correction
Because the nucleus has finite mass $M_N$, both nucleus and electron orbit their common center of mass. Replacing electron mass $m_e$ with the **reduced mass $\mu$**:
$$\mu \equiv \frac{m_e M_N}{m_e + M_N} = \frac{m_e}{1 + m_e / M_N} \tag{1.51}$$
For hydrogen ($M_N = m_p \approx 1836.15 m_e$):
$$R_H = R_\infty \left( \frac{1}{1 + m_e / m_p} \right) = \frac{109\,737.32}{1 + 1/1836.15} = 109\,677.58\text{ cm}^{-1} \tag{1.52}$$
This reduced-mass effect explained the spectral isotope shift between hydrogen ($^1\text{H}$) and deuterium ($^2\text{H}$ or $\text{D}$, with $M_D \approx 2 m_p$), which Harold Urey used in 1931 to discover deuterium, earning the 1934 Nobel Prize in Chemistry!

---

### The Sommerfeld Relativistic Generalization (1916)

While Bohr's theory was a monumental breakthrough, high-resolution spectroscopy revealed that hydrogen lines possess a subtle **fine structure**—each Balmer line is split into closely spaced doublets.
Arnold Sommerfeld expanded Bohr's model by introducing:
1. **Elliptical Orbits**: Quantized via two quantum numbers: principal quantum number $n$ and azimuthal quantum number $k$ (where $k \in \{1, 2, \dots, n\}$; in modern terminology, $l = k - 1$):
   $$\oint p_r dr = n_r h, \quad \oint p_\phi d\phi = k h, \quad n = n_r + k \tag{1.53}$$
   The ratio of semi-minor axis $b$ to semi-major axis $a$ of the ellipse is:
   $$\frac{b}{a} = \frac{k}{n} \tag{1.54}$$
2. **Relativistic Mass Variation**: Because an electron moves faster near the perihelion of an elliptical orbit ($v \sim \alpha c$), relativistic mass increase $m = m_0 / \sqrt{1 - v^2/c^2}$ causes the elliptical orbit to precess (perihelion precession), breaking the energy degeneracy between orbits of different eccentricity:
   $$E_{n,k} = -\frac{R_H h c Z^2}{n^2} \left[ 1 + \frac{\alpha^2 Z^2}{n^2} \left( \frac{n}{k} - \frac{3}{4} \right) \right] \tag{1.55}$$
Although brilliant, the Bohr-Sommerfeld model could not explain the spectra of polyelectronic atoms (even helium, $\text{He}$), could not account for chemical bonding, and could not predict spectral transition intensities or selection rules."""
            },
            {
                "secNumber": "1.3",
                "title": "Wave-Particle Duality & The Heisenberg Uncertainty Principle",
                "content": r"""The limitations of semi-classical orbital mechanics revealed that classical concepts of discrete trajectories ($\mathbf{r}(t), \mathbf{p}(t)$) are invalid at atomic dimensions. In 1924–1927, wave-particle duality and the quantum uncertainty principle forged the conceptual architecture of modern wave mechanics.

### Louis de Broglie's Matter Wave Hypothesis (1924)

Drawing inspiration from Einstein's dual treatment of light (which behaves as a wave in diffraction and as a particle in the photoelectric effect), French physicist Louis-Victor de Broglie proposed a bold, universal symmetry in nature:
> **De Broglie Hypothesis**:
> If electromagnetic waves can exhibit particle properties (photons with momentum $p = h/\lambda$), then material particles with rest mass (such as electrons, protons, and neutrons) must likewise possess an associated wave character.

Equating photon energy from relativity $E = m c^2$ to quantum energy $E = h \nu = h c / \lambda$, the photon momentum is $p = h / \lambda$. Generalizing to any material particle of relativistic momentum $p = \gamma m_0 v$:
$$\lambda_{\text{dB}} = \frac{h}{p} = \frac{h}{m v} = \frac{h}{\sqrt{2 m_e K}} \tag{1.56}$$
For an electron accelerated through an electrostatic potential difference $V$:
$$K = e V \implies p = \sqrt{2 m_e e V}$$
$$\lambda_{\text{dB}} = \frac{h}{\sqrt{2 m_e e V}} = \frac{6.626 \times 10^{-34}}{\sqrt{2 \times 9.109 \times 10^{-31} \times 1.602 \times 10^{-19} \times V}} = \frac{1.2264 \times 10^{-9}\text{ m}}{\sqrt{V}} = \frac{1.226\text{ nm}}{\sqrt{V}} = \frac{12.26\text{ Å}}{\sqrt{V}} \tag{1.57}$$
For an accelerating voltage of $V = 100\text{ V}$:
$$\lambda_{\text{dB}} = \frac{12.26\text{ Å}}{\sqrt{100}} = 1.226\text{ Å} = 0.1226\text{ nm}$$
This wavelength is of the exact same order of magnitude as interatomic lattice spacings in crystal planes ($d \sim 1 - 3\text{ Å}$), meaning crystal lattices can act as three-dimensional diffraction gratings for electron waves!

#### Physical Explanation of Bohr's Angular Momentum Quantization
De Broglie demonstrated that Bohr's ad-hoc angular momentum postulate is simply the condition for a **stable standing matter wave** along a circular orbit.
To avoid destructive self-interference upon completing a full $2\pi$ revolution, the orbital circumference must accommodate an exact integer number $n$ of de Broglie wavelengths:
$$2\pi r_n = n \lambda_{\text{dB}} = n \left( \frac{h}{m_e v_n} \right) \tag{1.58}$$
Rearranging terms:
$$m_e v_n r_n = n \left( \frac{h}{2\pi} \right) = n \hbar \tag{1.59}$$
Bohr's quantization of angular momentum ($L = n\hbar$) is identical to the standing wave boundary condition for an electron confined to a ring.

---

### Experimental Confirmation: The Davisson-Germer Experiment (1927)

In 1927 at Bell Telephone Laboratories, Clinton Davisson and Lester Germer scattered slow electrons ($V = 54\text{ V}$) from the surface of a single crystal of nickel.
The target atoms in the nickel lattice formed parallel atomic planes with spacing $d = 0.91\text{ Å} = 0.091\text{ nm}$.
A distinct intensity maximum was observed at a scattering angle of $\phi = 50^\circ$, corresponding to a Bragg glancing angle:
$$\theta = 90^\circ - \frac{\phi}{2} = 90^\circ - 25^\circ = 65^\circ$$
Applying **Bragg's Law of Crystal Diffraction** ($n\lambda = 2d \sin\theta$) for first-order reflection ($n=1$):
$$\lambda_{\text{exp}} = 2 d \sin\theta = 2 \times (0.91\text{ Å}) \times \sin(65^\circ) = 2 \times 0.91 \times 0.9063 \approx 1.65\text{ Å} \tag{1.60}$$
Calculating the theoretical de Broglie wavelength for $54\text{ V}$ electrons via Eq. (1.57):
$$\lambda_{\text{dB}} = \frac{12.26\text{ Å}}{\sqrt{54}} = \frac{12.26}{7.348} \approx 1.67\text{ Å} \tag{1.61}$$
The experimental diffraction value ($\lambda_{\text{exp}} = 1.65\text{ Å}$) matched de Broglie's theoretical prediction within $1.2\%$, proving unequivocally that electrons possess wave reality.

---

### The Heisenberg Uncertainty Principle (1927)

In classical mechanics, a particle has a definite position $\mathbf{r}(t)$ and a definite momentum $\mathbf{p}(t)$ at every instant of time. In wave mechanics, a localized particle is represented as a **wave packet**—a Fourier superposition of plane waves:
$$\psi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty \phi(k) e^{i k x} dk \tag{1.62}$$
From Fourier transform analysis, the spatial spread of a wave packet $\Delta x$ and its wavenumber spread $\Delta k$ satisfy the reciprocal bandwidth theorem:
$$\Delta x \cdot \Delta k \ge \frac{1}{2} \tag{1.63}$$
Using de Broglie's relation $p = \hbar k \implies \Delta p_x = \hbar \Delta k$:
$$\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2} \tag{1.64}$$
In 1927, Werner Heisenberg formulated this fundamental physical law:
> **The Heisenberg Uncertainty Principle**:
> It is physically impossible to simultaneously determine both the exact position and exact momentum of a microscopic particle along the same Cartesian coordinate. The product of their fundamental uncertainties must satisfy:
> $$\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}, \quad \Delta y \cdot \Delta p_y \ge \frac{\hbar}{2}, \quad \Delta z \cdot \Delta p_z \ge \frac{\hbar}{2} \tag{1.65}$$

#### Rigorous Quantum Mechanical Proof via Operator Commutation
In quantum mechanics, physical observables are represented by linear Hermitian operators. Position $\hat{x} = x$ and momentum $\hat{p}_x = -i\hbar \frac{\partial}{\partial x}$ satisfy the **Canonical Commutation Relation**:
$$[\hat{x}, \hat{p}_x] \equiv \hat{x}\hat{p}_x - \hat{p}_x\hat{x} = i\hbar \hat{I} \tag{1.66}$$
Proof for an arbitrary test wavefunction $f(x)$:
$$[\hat{x}, \hat{p}_x] f(x) = x \left(-i\hbar \frac{df}{dx}\right) - \left(-i\hbar \frac{d}{dx}(x f)\right) = -i\hbar x \frac{df}{dx} + i\hbar \left( f + x \frac{df}{dx} \right) = i\hbar f(x)$$
For any two Hermitian operators $\hat{A}$ and $\hat{B}$, the generalized Robertson-Schrödinger uncertainty relation states:
$$\Delta A \cdot \Delta B \ge \frac{1}{2} |\langle [\hat{A}, \hat{B}] \rangle| \tag{1.67}$$
Substituting $\hat{A} = \hat{x}$ and $\hat{B} = \hat{p}_x$:
$$\Delta x \cdot \Delta p_x \ge \frac{1}{2} |i\hbar| = \frac{\hbar}{2} \tag{Q.E.D.}$$

#### Heisenberg's Microscope Thought Experiment
To measure the position of an electron with an optical microscope, one must scatter at least one photon off it into the microscope objective lens of angular aperture $2\alpha$.
By the Abbe diffraction resolution limit, spatial precision is bounded by:
$$\Delta x \approx \frac{\lambda}{2\sin\alpha} \tag{1.68}$$
During the collision, the photon transfers an uncertain fraction of its momentum $p = h/\lambda$ to the electron inside the aperture angle:
$$\Delta p_x \approx 2 p \sin\alpha = 2 \left(\frac{h}{\lambda}\right) \sin\alpha \tag{1.69}$$
Multiplying position and momentum uncertainties:
$$\Delta x \cdot \Delta p_x \approx \left(\frac{\lambda}{2\sin\alpha}\right) \left(\frac{2h\sin\alpha}{\lambda}\right) \approx h > \frac{\hbar}{2} \tag{1.70}$$
To resolve position more precisely ($\Delta x \downarrow$), one must use shorter wavelength ($\lambda \downarrow$), which increases photon momentum ($p = h/\lambda \uparrow$), uncontrollably kicking the electron and violently disrupting its momentum ($\Delta p_x \uparrow$)!

#### Physical Consequences in Inorganic Chemistry:
1. **Non-Existence of Electrons in Atomic Nuclei**:
   If an electron were confined inside a nucleus of radius $R_N \approx 5\text{ fm} = 5 \times 10^{-15}\text{ m}$, its position uncertainty would be $\Delta x \approx 5 \times 10^{-15}\text{ m}$.
   By uncertainty, its minimum momentum spread must be:
   $$\Delta p \ge \frac{\hbar}{2\Delta x} = \frac{1.055 \times 10^{-34}}{2 \times 5 \times 10^{-15}} \approx 1.055 \times 10^{-20}\text{ kg}\cdot\text{m}\cdot\text{s}^{-1}$$
   Relativistic kinetic energy $E \approx c \Delta p \approx (3 \times 10^8) \times (1.055 \times 10^{-20})\text{ J} \approx 3.16 \times 10^{-12}\text{ J} \approx 20\text{ MeV}$.
   Nuclear potential wells are only $\sim 5 - 8\text{ MeV}$ deep, proving that **free electrons cannot exist within the nucleus** (explaining why beta-decay electrons must be created at the instant of neutron decay).
2. **Zero-Point Energy**:
   A particle confined to any finite domain cannot have zero kinetic energy ($p = 0$), because $\Delta p = 0$ would require $\Delta x = \infty$.
   Every quantum oscillator possesses irreducible **zero-point vibrational energy** $E_0 = \frac{1}{2}\hbar\omega$, preventing absolute thermal standstill even at $T = 0\text{ K}$.
3. **Abolition of Bohr Orbits**:
   Because $\Delta x$ and $\Delta p$ cannot both be zero, the concept of a precise geometric circular orbit $r_n(t)$ with a simultaneous trajectory velocity $v_n(t)$ is physically meaningless. The electron must instead be described as a three-dimensional **probabilistic orbital cloud**."""
            },
            {
                "secNumber": "1.4",
                "title": "Quantum Mechanics of Hydrogenic Atoms & Orbitals",
                "content": r"""The definitive description of electronic structure in chemistry is provided by the **Time-Independent Schrödinger Equation (TISE)**, formulated by Erwin Schrödinger in 1926. For a single electron of mass $m_e$ moving in three-dimensional space within a static electrostatic potential $V(\mathbf{r})$:
$$\hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r}) \tag{1.71}$$
where $\hat{H}$ is the **Hamiltonian Operator**:
$$\hat{H} = -\frac{\hbar^2}{2m_e} \nabla^2 + V(\mathbf{r}) \tag{1.72}$$
and $\nabla^2 \equiv \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$ is the spatial Laplacian.

### Born's Probabilistic Interpretation of the Wavefunction ($\psi$)

The wavefunction $\psi(\mathbf{r})$ is generally a complex-valued scalar field. Max Born (1926) established its fundamental physical meaning:
> **Born Statistical Interpretation**:
> The wavefunction $\psi(\mathbf{r})$ represents a **probability amplitude**. The probability density of finding the electron in an infinitesimal volume element $d\tau = dx\,dy\,dz$ centered at position $\mathbf{r}$ is proportional to the square modulus of the wavefunction:
> $$dP = |\psi(\mathbf{r})|^2 d\tau = \psi^*(\mathbf{r}) \psi(\mathbf{r}) d\tau \tag{1.73}$$

Because the electron must exist somewhere in the universe, the wavefunction must satisfy the **normalization condition**:
$$\int_{\text{all space}} |\psi(\mathbf{r})|^2 d\tau = 1 \tag{1.74}$$
To be physically acceptable, any eigenfunction $\psi$ must be single-valued, continuous, have continuous first derivatives, and be square-integrable (well-behaved boundary conditions).

---

### Separation of Variables in Spherical Polar Coordinates

For a hydrogenic atom (nucleus of charge $+Ze$ at the origin), the Coulomb potential is spherically symmetric:
$$V(r) = -\frac{1}{4\pi\varepsilon_0} \frac{Z e^2}{r} \tag{1.75}$$
Because $V(r)$ depends exclusively on the radial distance $r = \sqrt{x^2 + y^2 + z^2}$, the Schrödinger equation is non-separable in Cartesian coordinates $(x, y, z)$, but separates cleanly in **spherical polar coordinates** $(r, \theta, \phi)$:
$$x = r \sin\theta \cos\phi, \quad y = r \sin\theta \sin\phi, \quad z = r \cos\theta \tag{1.76}$$
$$r \in [0, \infty), \quad \theta \in [0, \pi] \text{ (polar angle)}, \quad \phi \in [0, 2\pi) \text{ (azimuthal angle)}$$
The volume element in spherical coordinates is:
$$d\tau = r^2 \sin\theta\, dr\, d\theta\, d\phi \tag{1.77}$$
The Laplacian operator expands to:
$$\nabla^2 = \frac{1}{r^2} \frac{\partial}{\partial r} \left( r^2 \frac{\partial}{\partial r} \right) + \frac{1}{r^2 \sin\theta} \frac{\partial}{\partial \theta} \left( \sin\theta \frac{\partial}{\partial \theta} \right) + \frac{1}{r^2 \sin^2\theta} \frac{\partial^2}{\partial \phi^2} \tag{1.78}$$
We seek separable product solutions factoring the radial and angular dependences:
$$\psi(r, \theta, \phi) = R(r) \cdot Y(\theta, \phi) = R(r) \cdot \Theta(\theta) \cdot \Phi(\phi) \tag{1.79}$$
Substituting Eq. (1.79) into $\hat{H}\psi = E\psi$ and multiplying throughout by $-\frac{2m_e r^2}{\hbar^2 R Y}$:
$$\frac{1}{R(r)} \frac{d}{dr} \left( r^2 \frac{dR}{dr} \right) + \frac{2m_e r^2}{\hbar^2} [E - V(r)] = -\frac{1}{Y(\theta, \phi)} \left[ \frac{1}{\sin\theta} \frac{\partial}{\partial \theta} \left( \sin\theta \frac{\partial Y}{\partial \theta} \right) + \frac{1}{\sin^2\theta} \frac{\partial^2 Y}{\partial \phi^2} \right] \tag{1.80}$$
The left-hand side is a function strictly of $r$, while the right-hand side is a function strictly of $(\theta, \phi)$. Two independent functions of independent variables can be identically equal for all $(r, \theta, \phi)$ if and only if **both sides equal a common separation constant**, denoted $\beta = l(l+1)$:

#### 1. The Angular Equation: Spherical Harmonics ($Y_{lm}$)
$$\frac{1}{\sin\theta} \frac{\partial}{\partial \theta} \left( \sin\theta \frac{\partial Y}{\partial \theta} \right) + \frac{1}{\sin^2\theta} \frac{\partial^2 Y}{\partial \phi^2} = -l(l+1) Y(\theta, \phi) \tag{1.81}$$
This is the eigenvalue equation for the orbital angular momentum operator $\hat{L}^2$:
$$\hat{L}^2 Y_{lm}(\theta, \phi) = \hbar^2 l(l+1) Y_{lm}(\theta, \phi) \tag{1.82}$$
Separating $Y(\theta, \phi) = \Theta(\theta) \Phi(\phi)$ with separation constant $m_l^2$:
* **The Azimuthal Equation**:
  $$\frac{d^2\Phi}{d\phi^2} = -m_l^2 \Phi \implies \Phi(\phi) = \frac{1}{\sqrt{2\pi}} e^{i m_l \phi} \tag{1.83}$$
  To ensure single-valuedness under a complete rotation ($\Phi(\phi + 2\pi) = \Phi(\phi)$), $e^{i m_l 2\pi} = 1$, which quantizes the **magnetic quantum number**:
  $$m_l \in \{0, \pm 1, \pm 2, \dots\} \tag{1.84}$$
  This governs the $z$-component of orbital angular momentum:
  $$\hat{L}_z \Phi = -i\hbar \frac{\partial}{\partial \phi} \Phi = m_l \hbar \Phi \implies L_z = m_l \hbar \tag{1.85}$$
* **The Polar Equation**:
  $$\frac{1}{\sin\theta} \frac{d}{d\theta} \left( \sin\theta \frac{d\Theta}{d\theta} \right) + \left[ l(l+1) - \frac{m_l^2}{\sin^2\theta} \right] \Theta = 0 \tag{1.86}$$
  Substituting $w = \cos\theta$ converts Eq. (1.86) into the **Associated Legendre Differential Equation**. Solutions remain finite at $\theta = 0, \pi$ if and only if the **orbital (azimuthal) quantum number $l$** is a non-negative integer and $|m_l| \le l$:
  $$l \in \{0, 1, 2, 3, \dots\}, \quad m_l \in \{-l, -l+1, \dots, 0, \dots, l-1, l\} \tag{1.87}$$
  The solutions are the **Spherical Harmonics**:
  $$Y_{lm}(\theta, \phi) = (-1)^{\frac{m_l+|m_l|}{2}} \sqrt{\frac{2l+1}{4\pi} \frac{(l-|m_l|)!}{(l+|m_l|)!}} P_l^{|m_l|}(\cos\theta) e^{i m_l \phi} \tag{1.88}$$

#### 2. The Radial Equation ($R_{nl}(r)$)
$$\frac{1}{r^2} \frac{d}{dr} \left( r^2 \frac{dR}{dr} \right) + \left[ \frac{2m_e}{\hbar^2} \left( E + \frac{Z e^2}{4\pi\varepsilon_0 r} \right) - \frac{l(l+1)}{r^2} \right] R(r) = 0 \tag{1.89}$$
Substituting $u(r) = r R(r)$ yields an effective one-dimensional Schrödinger equation with an **effective potential** $V_{\text{eff}}(r)$:
$$-\frac{\hbar^2}{2m_e} \frac{d^2 u}{dr^2} + V_{\text{eff}}(r) u = E u \tag{1.90}$$
$$V_{\text{eff}}(r) = -\frac{Z e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2 l(l+1)}{2m_e r^2} \tag{1.91}$$
The term $\frac{\hbar^2 l(l+1)}{2m_e r^2}$ is the **centrifugal potential barrier**. For $l > 0$, it diverges as $+1/r^2$ at small $r$, preventing $p, d, f$ electrons from penetrating close to the nucleus, whereas $s$ electrons ($l=0$) experience zero centrifugal barrier and can penetrate directly to the nucleus!

Solving Eq. (1.89) via asymptotic substitution and power series leads to the **Associated Laguerre Polynomials** $L_{n-l-1}^{2l+1}(\rho)$ where $\rho = \frac{2Zr}{n a_0}$. Boundary conditions require the series to terminate, which quantizes the **principal quantum number**:
$$n \in \{1, 2, 3, \dots\}, \quad l \in \{0, 1, 2, \dots, n-1\} \tag{1.92}$$
The bound state energy eigenvalues depend **strictly on $n$** (for single-electron hydrogenic systems):
$$E_n = -\frac{m_e Z^2 e^4}{32\pi^2\varepsilon_0^2\hbar^2 n^2} = -\frac{13.606 Z^2}{n^2}\text{ eV} \tag{1.93}$$
All orbitals with the same principal quantum number $n$ ($s, p, d, f$) have identically the same energy in hydrogen—a symmetry termed **Coulomb (accidental) degeneracy**.

---

### Analytic Hydrogenic Wavefunctions & Orbital Geometries

The total hydrogenic wavefunction is:
$$\psi_{nlm_l}(r, \theta, \phi) = R_{nl}(r) \cdot Y_{lm_l}(\theta, \phi) \tag{1.94}$$
Letting $\sigma \equiv \frac{Z r}{a_0}$:

| Orbital ($n, l, m_l$) | Radial Function $R_{nl}(r)$ | Real Angular Function $Y(\theta, \phi)$ | Total Normalized Wavefunction $\psi(r, \theta, \phi)$ |
| :--- | :--- | :--- | :--- |
| **$1s$** ($1, 0, 0$) | $2 \left(\frac{Z}{a_0}\right)^{3/2} e^{-\sigma}$ | $\frac{1}{\sqrt{4\pi}}$ | $\frac{1}{\sqrt{\pi}} \left(\frac{Z}{a_0}\right)^{3/2} e^{-\sigma}$ |
| **$2s$** ($2, 0, 0$) | $\frac{1}{\sqrt{2}} \left(\frac{Z}{a_0}\right)^{3/2} \left(1 - \frac{\sigma}{2}\right) e^{-\sigma/2}$ | $\frac{1}{\sqrt{4\pi}}$ | $\frac{1}{4\sqrt{2\pi}} \left(\frac{Z}{a_0}\right)^{3/2} (2 - \sigma) e^{-\sigma/2}$ |
| **$2p_z$** ($2, 1, 0$) | $\frac{1}{2\sqrt{6}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma e^{-\sigma/2}$ | $\sqrt{\frac{3}{4\pi}} \cos\theta$ | $\frac{1}{4\sqrt{2\pi}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma \cos\theta e^{-\sigma/2}$ |
| **$2p_x$** ($2, 1, \pm 1$) | $\frac{1}{2\sqrt{6}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma e^{-\sigma/2}$ | $\sqrt{\frac{3}{4\pi}} \sin\theta \cos\phi$ | $\frac{1}{4\sqrt{2\pi}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma \sin\theta \cos\phi e^{-\sigma/2}$ |
| **$2p_y$** ($2, 1, \mp 1$) | $\frac{1}{2\sqrt{6}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma e^{-\sigma/2}$ | $\sqrt{\frac{3}{4\pi}} \sin\theta \sin\phi$ | $\frac{1}{4\sqrt{2\pi}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma \sin\theta \sin\phi e^{-\sigma/2}$ |
| **$3d_{z^2}$** ($3, 2, 0$) | $\frac{4}{81\sqrt{30}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma^2 e^{-\sigma/3}$ | $\sqrt{\frac{5}{16\pi}} (3\cos^2\theta - 1)$ | $\frac{1}{81\sqrt{6\pi}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma^2 (3\cos^2\theta - 1) e^{-\sigma/3}$ |
| **$3d_{x^2-y^2}$** ($3, 2, \pm 2$) | $\frac{4}{81\sqrt{30}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma^2 e^{-\sigma/3}$ | $\sqrt{\frac{15}{16\pi}} \sin^2\theta \cos(2\phi)$ | $\frac{1}{81\sqrt{2\pi}} \left(\frac{Z}{a_0}\right)^{3/2} \sigma^2 \sin^2\theta \cos(2\phi) e^{-\sigma/3}$ |

---

### Radial Distribution Function & Nodal Topologies

While $|\psi|^2$ gives probability per unit volume, the probability of finding an electron inside a spherical shell of thickness $dr$ at radius $r$ regardless of direction is the **Radial Distribution Function $P(r)$**:
$$P(r) dr = \left( \int_{\theta=0}^\pi \int_{\phi=0}^{2\pi} |\psi|^2 \sin\theta\, d\theta\, d\phi \right) r^2 dr = [R_{nl}(r)]^2 r^2 dr \tag{1.95}$$
$$P(r) = 4\pi r^2 [R_{nl}(r)]^2 \tag{1.96}$$

#### Anatomy of Atomic Nodes
A **node** is a point, surface, or plane where the wavefunction passes through zero ($\psi = 0$), meaning electron probability density is identically zero ($|\psi|^2 = 0$):
1. **Radial Nodes (Spherical Nodal Shells)**: Occur where the radial function $R_{nl}(r) = 0$ (excluding $r = 0$ and $r \to \infty$):
   $$\text{Number of Radial Nodes} = n - l - 1 \tag{1.97}$$
   * $1s$: $1 - 0 - 1 = 0$ radial nodes.
   * $2s$: $2 - 0 - 1 = 1$ radial node (at $r = 2a_0/Z$).
   * $2p$: $2 - 1 - 1 = 0$ radial nodes.
   * $3s$: $3 - 0 - 1 = 2$ radial nodes.
   * $3d$: $3 - 2 - 1 = 0$ radial nodes.
2. **Angular Nodes (Planar or Conical Nodal Surfaces)**: Occur where the spherical harmonic $Y_{lm}(\theta, \phi) = 0$:
   $$\text{Number of Angular Nodes} = l \tag{1.98}$$
   * $s$-orbitals ($l=0$): $0$ angular nodes (spherically symmetric).
   * $p$-orbitals ($l=1$): $1$ angular nodal plane (e.g., $p_z$ has the $xy$-plane at $z = 0$).
   * $d$-orbitals ($l=2$): $2$ angular nodal surfaces (e.g., $d_{xy}$ has planes $x=0$ and $y=0$; $d_{z^2}$ has two nodal cones at $\cos\theta = \pm 1/\sqrt{3} \approx 54.7^\circ$).
3. **Total Nodes**:
   $$\text{Total Nodes} = \text{Radial Nodes} + \text{Angular Nodes} = (n - l - 1) + l = n - 1 \tag{1.99}$$

#### Orbital Penetration & The Radial Extrema
For the $1s$ orbital, $P(r) = 4\pi r^2 \left[ \frac{1}{\sqrt{\pi}a_0^{3/2}} e^{-r/a_0} \right]^2 = \frac{4}{a_0^3} r^2 e^{-2r/a_0}$.
Finding the radius of maximum probability:
$$\frac{dP}{dr} = \frac{4}{a_0^3} \left( 2r - \frac{2r^2}{a_0} \right) e^{-2r/a_0} = 0 \implies r_{\text{max}} = a_0 \tag{1.100}$$
The most probable radius for the electron in ground-state hydrogen is **identically the Bohr radius $a_0$**!
However, the expectation value $\langle r \rangle$ is slightly larger due to the asymmetrical exponential tail:
$$\langle r \rangle = \int_0^\infty r P(r) dr = \frac{a_0}{2Z} [3n^2 - l(l+1)] = \frac{3}{2} a_0 \tag{1.101}$$"""
            },
            {
                "secNumber": "1.5",
                "title": "Polyelectronic Atoms, Electron Spin & Orbital Filling Rules",
                "content": r"""When transitioning from hydrogenic atoms to polyelectronic atoms ($N \ge 2$ electrons), exact analytical solutions to the Schrödinger equation become fundamentally impossible due to electron-electron Coulomb repulsion terms:
$$\hat{H} = \sum_{i=1}^N \left( -\frac{\hbar^2}{2m_e} \nabla_i^2 - \frac{Z e^2}{4\pi\varepsilon_0 r_i} \right) + \sum_{i < j}^N \frac{e^2}{4\pi\varepsilon_0 r_{ij}} \tag{1.102}$$
The term $\frac{e^2}{4\pi\varepsilon_0 r_{ij}}$ couples the coordinates of every electron to every other electron. This multi-body problem necessitates approximation methods (the Hartree-Fock Self-Consistent Field method, Density Functional Theory, and Slater screening models) and gives rise to the fundamental rules governing the electronic configuration of elements across the periodic table.

### Electron Spin & The Stern-Gerlach Experiment (1922)

In 1922, Otto Stern and Walther Gerlach directed a collimated beam of neutral silver atoms ($Z=47$) through an inhomogeneous magnetic field $\frac{\partial B_z}{\partial z}$.
Classically, or with orbital angular momentum $L=0$ ($[\text{Kr}] 4d^{10} 5s^1$), the beam should have broadened continuously or remained a single undeflected line. Instead, the beam **split cleanly into two discrete, symmetrically separated components**.

In 1925, Samuel Goudsmit and George Uhlenbeck proposed that the electron possesses an intrinsic, non-orbital angular momentum—**spin angular momentum ($\mathbf{S}$)**:
$$|\mathbf{S}| = \hbar \sqrt{s(s+1)} = \hbar \sqrt{\frac{1}{2}\left(\frac{1}{2}+1\right)} = \frac{\sqrt{3}}{2} \hbar \tag{1.103}$$
$$S_z = m_s \hbar, \quad m_s \in \left\{+\frac{1}{2}, -\frac{1}{2}\right\} \quad (\alpha \equiv \text{spin-up}, \beta \equiv \text{spin-down}) \tag{1.104}$$
The associated spin magnetic dipole moment is:
$$\boldsymbol{\mu}_s = -g_e \frac{e}{2m_e} \mathbf{S} = -g_e \mu_B \frac{\mathbf{S}}{\hbar} \tag{1.105}$$
where $\mu_B \equiv \frac{e\hbar}{2m_e} \approx 9.27401 \times 10^{-24}\text{ J}\cdot\text{T}^{-1}$ is the **Bohr Magneton**, and $g_e \approx 2.0023193$ is the electron spin g-factor (explained by Dirac relativistic quantum mechanics and QED).

---

### The Pauli Exclusion Principle & Antisymmetric Slater Determinants

Electrons are identical, indistinguishable **fermions** possessing half-integer spin ($s=1/2$).
According to the **Spin-Statistics Theorem**:
> **The Pauli Exclusion Principle (1925)**:
> 1. **Qualitative Formulation**: No two electrons in a single atom can have identical values for all four quantum numbers $(n, l, m_l, m_s)$.
> 2. **Fundamental Quantum Formulation**: The total many-electron wavefunction must be **strictly antisymmetric** under the interchange of space and spin coordinates of any two electrons:
>    $$\Psi(\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_i, \dots, \mathbf{x}_j, \dots, \mathbf{x}_N) = -\Psi(\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_j, \dots, \mathbf{x}_i, \dots, \mathbf{x}_N) \tag{1.106}$$
>    where $\mathbf{x}_i \equiv (\mathbf{r}_i, \sigma_i)$ represents combined spatial and spin coordinates.

#### Slater Determinants (1929)
John C. Slater demonstrated that an antisymmetric $N$-electron wavefunction constructed from $N$ single-electron spin-orbitals $\chi_k(\mathbf{x}) = \phi_k(\mathbf{r}) \cdot \chi_{\text{spin}}(\sigma)$ is written as a determinant:
$$\Psi(\mathbf{x}_1, \dots, \mathbf{x}_N) = \frac{1}{\sqrt{N!}} \begin{vmatrix} 
\chi_1(\mathbf{x}_1) & \chi_2(\mathbf{x}_1) & \dots & \chi_N(\mathbf{x}_1) \\
\chi_1(\mathbf{x}_2) & \chi_2(\mathbf{x}_2) & \dots & \chi_N(\mathbf{x}_2) \\
\vdots & \vdots & \ddots & \vdots \\
\chi_1(\mathbf{x}_N) & \chi_2(\mathbf{x}_N) & \dots & \chi_N(\mathbf{x}_N)
\end{vmatrix} \tag{1.107}$$
If any two electrons occupy the exact same spin-orbital ($\chi_a = \chi_b$), two columns of the determinant become identical, which causes the determinant to **vanish identically ($\Psi = 0$)**! This proves mathematically that two electrons cannot occupy the same quantum state.

---

### The Aufbau (Building-Up) Principle & The $(n+l)$ Madelung Rule

In polyelectronic atoms, inner electrons shield the nucleus, which breaks the Coulomb degeneracy between $s, p, d, f$ subshells of the same principal quantum number $n$:
$$E_{ns} < E_{np} < E_{nd} < E_{nf} \tag{1.108}$$
Orbitals are filled in order of increasing energy according to the **Madelung Rule (Klechkowski Rule)**:
1. Orbitals fill in order of increasing value of $(n + l)$.
2. If two subshells have the identical value of $(n + l)$, the subshell with the smaller value of $n$ fills first.

| Subshell | $n$ | $l$ | $(n + l)$ Value | Filling Sequence |
| :---: | :---: | :---: | :---: | :---: |
| **$1s$** | 1 | 0 | 1 | 1st |
| **$2s$** | 2 | 0 | 2 | 2nd |
| **$2p$** | 2 | 1 | 3 | 3rd |
| **$3s$** | 3 | 0 | 3 | 4th ($n=3 < n+l=3$) |
| **$3p$** | 3 | 1 | 4 | 5th |
| **$4s$** | 4 | 0 | 4 | 6th ($4s$ fills before $3d$!) |
| **$3d$** | 3 | 2 | 5 | 7th |
| **$4p$** | 4 | 1 | 5 | 8th |
| **$5s$** | 5 | 0 | 5 | 9th |
| **$4d$** | 4 | 2 | 6 | 10th |
| **$5p$** | 5 | 1 | 6 | 11th |
| **$6s$** | 6 | 0 | 6 | 12th |
| **$4f$** | 4 | 3 | 7 | 13th |
| **$5d$** | 5 | 2 | 7 | 14th |

The complete universal filling sequence is:
$$1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d < 5p < 6s < 4f < 5d < 6p < 7s < 5f < 6d < 7p \tag{1.109}$$

---

### Hund's Rule of Maximum Multiplicity & Exchange Energy Stabilization

When filling degenerate orbitals of equal energy (such as the three $2p$ or five $3d$ orbitals), **Hund's First Rule** dictates:
> **Hund's Rule of Maximum Multiplicity**:
> The lowest energy electronic state is the one that maximizes the total spin quantum number $S$ (and therefore maximizes the spin multiplicity $2S + 1$). Electrons occupy degenerate orbitals singly with parallel spins before any pairing occurs.

#### Physical Origin: Quantum Exchange Energy ($K$)
The stability of parallel spins is not merely classical Coulomb repulsion minimization; it is driven by quantum mechanical **Exchange Energy**.
For two electrons with parallel spins ($\alpha_1 \alpha_2$), the spin wavefunction is symmetric:
$$\chi_{\text{spin}} = \alpha(1)\alpha(2) \quad (\text{Symmetric}) \tag{1.110}$$
To satisfy the Pauli exclusion principle, their spatial wavefunction must be strictly antisymmetric:
$$\psi_{\text{space}}(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}} [\phi_a(\mathbf{r}_1)\phi_b(\mathbf{r}_2) - \phi_a(\mathbf{r}_2)\phi_b(\mathbf{r}_1)] \tag{1.111}$$
When $\mathbf{r}_1 \to \mathbf{r}_2$, $\psi_{\text{space}} \to 0$. Parallel-spin electrons are forced apart by a quantum **Fermi Hole**, drastically reducing inter-electron repulsion.
The total energy of the two-electron configuration is:
$$E = J_{ab} - K_{ab} \tag{1.112}$$
where $J_{ab} = \int \frac{|\phi_a(1)|^2 |\phi_b(2)|^2}{r_{12}} d\tau$ is the positive Coulomb repulsion integral, and:
$$K_{ab} = \int \frac{\phi_a^*(1)\phi_b(1) \phi_b^*(2)\phi_a(2)}{r_{12}} d\tau > 0 \tag{1.113}$$
is the **Exchange Integral**. The exchange energy $-K_{ab}$ is purely stabilizing.
For an atom with $n$ parallel-spin electrons, the total number of exchange interactions is:
$$\text{Number of Exchange Pairs} = \frac{n(n - 1)}{2} \tag{1.114}$$
For example, nitrogen ($2p^3$ with 3 parallel spins): $\frac{3(2)}{2} = 3$ exchange pairs $\implies E_{\text{ex}} = -3K$.
If one electron were paired ($\uparrow\downarrow, \uparrow$): only 1 exchange pair $\implies E_{\text{ex}} = -K$. The parallel configuration is stabilized by an extra $-2K$!

---

### Effective Nuclear Charge ($Z_{\text{eff}}$) & Slater's Screening Rules

In polyelectronic atoms, an electron does not experience the full nuclear charge $+Ze$. The electron cloud of inner-shell and peer electrons partially cancels the nuclear field. The net positive charge experienced by an electron is the **effective nuclear charge ($Z_{\text{eff}}$)**:
$$Z_{\text{eff}} = Z - \sigma \tag{1.115}$$
where $\sigma$ is the dimensionless **screening (shielding) constant**.

In 1930, John C. Slater formulated empirical rules to calculate $\sigma$ quantitatively for any electron in an atom:

#### Algorithm for Slater's Rules:
1. **Group the atomic orbitals** in order of increasing $n$ and $l$ into parentheses:
   $$(1s)(2s, 2p)(3s, 3p)(3d)(4s, 4p)(4d)(4f)(5s, 5p)\dots$$
2. **Electrons to the right** of the group containing the target electron contribute **$0.00$** to $\sigma$ (no shielding from outer electrons).
3. **For an electron in an $(ns, np)$ group**:
   * Other electrons in the **same $(ns, np)$ group** contribute **$0.35$** each (except in $1s$, where the other electron contributes **$0.30$**).
   * All electrons in the **$(n - 1)$ shell** (with principal quantum number $n - 1$) contribute **$0.85$** each.
   * All electrons in **deeper shells** ($n - 2, n - 3, \dots$) contribute **$1.00$** each.
4. **For an electron in an $(nd)$ or $(nf)$ group**:
   * Other electrons in the **same $(nd)$ or $(nf)$ group** contribute **$0.35$** each.
   * All electrons in **all groups to the left** (all inner electrons regardless of $n$) contribute **$1.00$** each.

#### Example Calculation: Effective Nuclear Charge of Zinc ($Z=30$)
Ground-state configuration of $\text{Zn}$: $1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^2$.
Grouping: $(1s)^2 (2s, 2p)^8 (3s, 3p)^8 (3d)^{10} (4s)^2$.

1. **For a $4s$ valence electron ($n=4$)**:
   * Same group $(4s)$: $1 \text{ other electron} \times 0.35 = 0.35$
   * $(n - 1) = 3$ shell: $(3s, 3p)^8 (3d)^{10} = 18 \text{ electrons} \times 0.85 = 15.30$
   * $(n - 2) \text{ and } (n - 3)$ shells: $(1s)^2 (2s, 2p)^8 = 10 \text{ electrons} \times 1.00 = 10.00$
   $$\sigma(4s) = 0.35 + 15.30 + 10.00 = 25.65$$
   $$Z_{\text{eff}}(4s) = 30 - 25.65 = +4.35$$
2. **For a $3d$ electron ($n=3$)**:
   * Same group $(3d)$: $9 \text{ other electrons} \times 0.35 = 3.15$
   * All groups to the left: $(1s)^2 (2s, 2p)^8 (3s, 3p)^8 = 18 \text{ electrons} \times 1.00 = 18.00$
   * $(4s)^2$ is to the right $\implies 0.00$
   $$\sigma(3d) = 3.15 + 18.00 = 21.15$$
   $$Z_{\text{eff}}(3d) = 30 - 21.15 = +8.85$$

> **Crucial Chemical Insight: Why $4s$ Electrons Are Lost First in Ionization of Transition Metals**:
> Notice that $Z_{\text{eff}}(3d) = +8.85$ is dramatically higher than $Z_{\text{eff}}(4s) = +4.35$.
> The $3d$ electrons feel a much stronger electrostatic attraction to the nucleus than the $4s$ electrons.
> Therefore, when zinc or other transition metals ionize ($\text{Zn} \to \text{Zn}^{2+} + 2e^-$), **the $4s$ electrons are lost first**, yielding $[\text{Ar}] 3d^{10}$, because their lower effective nuclear charge renders them more weakly bound!"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Comprehensive Bohr Hydrogen Atom Spectroscopy, Orbital Velocity & Rydberg Transition",
                "statement": r"""A gas of atomic hydrogen is excited into the $n = 5$ quantum state at room temperature.
Given fundamental physical constants:
* Planck's constant: $h = 6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}, \hbar = 1.0545718 \times 10^{-34}\text{ J}\cdot\text{s}$
* Electron mass: $m_e = 9.1093837 \times 10^{-31}\text{ kg}$
* Elementary charge: $e = 1.602176634 \times 10^{-19}\text{ C}$
* Vacuum permittivity: $\varepsilon_0 = 8.8541878 \times 10^{-12}\text{ F}\cdot\text{m}^{-1}$
* Speed of light: $c = 2.99792458 \times 10^8\text{ m}\cdot\text{s}^{-1}$
* Rydberg constant for hydrogen: $R_H = 109\,677.58\text{ cm}^{-1}$

Calculate:
1. The orbital radius $r_5$ and the classical orbital velocity $v_5$ of the electron in the $n = 5$ state, and express $v_5$ as a fraction of the speed of light $c$.
2. The total energy $E_5$ of the electron in both electronvolts ($\text{eV}$) and joules ($\text{J}$).
3. The wavelength $\lambda$, frequency $\nu$, and photon energy in $\text{eV}$ emitted when the electron undergoes a radiative quantum transition directly from $n = 5$ to $n = 2$ (the Balmer series $H_\gamma$ line).
4. The recoil velocity $v_{\text{recoil}}$ imparted to the hydrogen atom (proton mass $m_p = 1.67262 \times 10^{-27}\text{ kg}$) upon emitting this photon.""",
                "solution": r"""### Step 1: Calculation of Orbital Radius $r_5$ & Orbital Velocity $v_5$

From Bohr's theory, the orbital radius for hydrogen ($Z = 1$) is:
$$r_n = a_0 n^2$$
where $a_0 = \frac{4\pi \varepsilon_0 \hbar^2}{m_e e^2} \approx 5.29177 \times 10^{-11}\text{ m} = 0.52918\text{ Å}$.
For $n = 5$:
$$r_5 = a_0 (5^2) = 25 \times (5.29177 \times 10^{-11}\text{ m}) = 1.32294 \times 10^{-9}\text{ m} = 13.229\text{ Å} = 1.323\text{ nm}$$

Calculate the orbital velocity $v_5$:
From angular momentum quantization $L = m_e v_5 r_5 = 5 \hbar$:
$$v_5 = \frac{5 \hbar}{m_e r_5} = \frac{5 \times (1.05457 \times 10^{-34}\text{ J}\cdot\text{s})}{(9.10938 \times 10^{-31}\text{ kg}) \times (1.32294 \times 10^{-9}\text{ m})}$$
$$v_5 = \frac{5.27286 \times 10^{-34}}{1.20512 \times 10^{-39}} \approx 4.37538 \times 10^5\text{ m}\cdot\text{s}^{-1}$$
Alternatively, using $v_n = \frac{c \alpha}{n}$:
$$v_5 = \frac{(2.9979 \times 10^8) \times (1/137.036)}{5} = \frac{2.18769 \times 10^6}{5} \approx 4.3754 \times 10^5\text{ m}\cdot\text{s}^{-1}$$
Fraction of speed of light:
$$\frac{v_5}{c} = \frac{4.37538 \times 10^5}{2.99792 \times 10^8} \approx 1.459 \times 10^{-3} = 0.146\%$$

---

### Step 2: Total Energy $E_5$ of the Electron

$$E_n = -\frac{13.6057\text{ eV}}{n^2}$$
For $n = 5$:
$$E_5 = -\frac{13.6057\text{ eV}}{25} \approx -0.54423\text{ eV}$$
Convert to joules ($1\text{ eV} = 1.6021766 \times 10^{-19}\text{ J}$):
$$E_5 = -0.54423 \times (1.6021766 \times 10^{-19}\text{ J}) \approx -8.7195 \times 10^{-20}\text{ J}$$

---

### Step 3: Wavelength, Frequency & Photon Energy for $n = 5 \to n = 2$ Transition

Apply the Rydberg formula:
$$\tilde{\nu} = \frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right) = R_H \left( \frac{1}{2^2} - \frac{1}{5^2} \right) = R_H \left( \frac{1}{4} - \frac{1}{25} \right) = R_H \left( \frac{21}{100} \right) = 0.21 R_H$$
Substitute $R_H = 109\,677.58\text{ cm}^{-1}$:
$$\tilde{\nu} = 0.21 \times 109\,677.58\text{ cm}^{-1} = 23\,032.29\text{ cm}^{-1} = 2.303229 \times 10^6\text{ m}^{-1}$$
Wavelength $\lambda$:
$$\lambda = \frac{1}{\tilde{\nu}} = \frac{1}{2.303229 \times 10^6\text{ m}^{-1}} \approx 4.3417 \times 10^{-7}\text{ m} = 434.17\text{ nm} = 4341.7\text{ Å}$$
This wavelength corresponds to the vibrant blue-violet $H_\gamma$ line of the hydrogen Balmer emission series.

Frequency $\nu$:
$$\nu = \frac{c}{\lambda} = \frac{2.997925 \times 10^8\text{ m}\cdot\text{s}^{-1}}{4.34173 \times 10^{-7}\text{ m}} \approx 6.9049 \times 10^{14}\text{ Hz}$$
Photon energy:
$$E_{\text{photon}} = h \nu = (6.62607 \times 10^{-34}\text{ J}\cdot\text{s}) \times (6.9049 \times 10^{14}\text{ s}^{-1}) = 4.5752 \times 10^{-19}\text{ J}$$
In electronvolts:
$$E_{\text{photon}} = \frac{4.5752 \times 10^{-19}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 2.8556\text{ eV}$$
Notice: $E_2 = -\frac{13.6057}{4} = -3.4014\text{ eV}$; $\Delta E = E_5 - E_2 = -0.5442 - (-3.4014) = +2.8572\text{ eV}$, matching perfectly.

---

### Step 4: Recoil Velocity of the Emitting Hydrogen Atom

The emitted photon carries linear momentum:
$$p_{\text{photon}} = \frac{E_{\text{photon}}}{c} = \frac{4.5752 \times 10^{-19}\text{ J}}{2.99792 \times 10^8\text{ m}\cdot\text{s}^{-1}} \approx 1.5261 \times 10^{-27}\text{ kg}\cdot\text{m}\cdot\text{s}^{-1}$$
By conservation of linear momentum, the hydrogen atom recoils with equal and opposite momentum:
$$p_{\text{atom}} = M_H v_{\text{recoil}} = p_{\text{photon}}$$
Taking $M_H \approx m_p + m_e \approx 1.6735 \times 10^{-27}\text{ kg}$:
$$v_{\text{recoil}} = \frac{p_{\text{photon}}}{M_H} = \frac{1.5261 \times 10^{-27}\text{ kg}\cdot\text{m}\cdot\text{s}^{-1}}{1.6735 \times 10^{-27}\text{ kg}} \approx 0.9119\text{ m}\cdot\text{s}^{-1} \approx 0.912\text{ m/s}$$
The recoil kinetic energy of the atom is $K_{\text{recoil}} = \frac{1}{2} M_H v_{\text{recoil}}^2 \approx 6.95 \times 10^{-28}\text{ J} \approx 4.3 \times 10^{-9}\text{ eV}$, which is infinitesimal compared to the $2.86\text{ eV}$ photon energy, verifying the approximation of negligible nuclear recoil."""
            },
            {
                "tier": "Advanced Level",
                "title": "Rigorous Slater Rules Evaluation of Effective Nuclear Charge & Ionization Order of 3d vs 4s Electrons",
                "statement": r"""Consider neutral atomic titanium ($\text{Ti}$, atomic number $Z = 22$) and the divalent titanium cation ($\text{Ti}^{2+}$).
1. Write the full ground-state electron configuration of neutral titanium, group the orbitals according to Slater's rules, and calculate the screening constant $\sigma$ and effective nuclear charge $Z_{\text{eff}}$ for:
   * A $4s$ valence electron
   * A $3d$ electron
2. Using the Slater effective potential formula $E \approx -13.6\text{ eV} \times \left(\frac{Z_{\text{eff}}}{n^*}\right)^2$ (where $n^* = 3.7$ for $n = 4$, and $n^* = 3.0$ for $n = 3$), estimate the single-electron binding energies for a $4s$ electron and a $3d$ electron in titanium.
3. Determine the theoretical total energy of the two competing electron configurations of $\text{Ti}^{2+}$:
   * Configuration A: $[\text{Ar}] 3d^2 4s^0$
   * Configuration B: $[\text{Ar}] 3d^0 4s^2$
   Use your calculations to explain why the $4s$ electrons are ionized before the $3d$ electrons, yet $4s$ fills before $3d$ during the Aufbau building-up process of neutral atoms.""",
                "solution": r"""### Step 1: Slater Rules Calculation for Neutral Titanium ($Z = 22$)

The electron configuration of neutral $\text{Ti}$ is:
$$1s^2 2s^2 2p^6 3s^2 3p^6 3d^2 4s^2$$
Organizing into Slater groups:
$$(1s)^2 (2s, 2p)^8 (3s, 3p)^8 (3d)^2 (4s)^2$$

#### 1. Screening Constant & $Z_{\text{eff}}$ for a $4s$ Electron ($n = 4$):
* Same group $(4s)$: $1 \text{ other electron} \times 0.35 = 0.35$
* $(n - 1) = 3$ shell: $(3s, 3p)^8 (3d)^2 = 10 \text{ electrons} \times 0.85 = 8.50$
* $(n - 2) \text{ and } (n - 3)$ shells: $(1s)^2 (2s, 2p)^8 = 10 \text{ electrons} \times 1.00 = 10.00$
$$\sigma(4s) = 0.35 + 8.50 + 10.00 = 18.85$$
$$Z_{\text{eff}}(4s) = Z - \sigma = 22 - 18.85 = +3.15$$

#### 2. Screening Constant & $Z_{\text{eff}}$ for a $3d$ Electron ($n = 3$):
* Same group $(3d)$: $1 \text{ other electron} \times 0.35 = 0.35$
* All groups to the left: $(1s)^2 (2s, 2p)^8 (3s, 3p)^8 = 18 \text{ electrons} \times 1.00 = 18.00$
* $(4s)^2$ is to the right $\implies 0.00$
$$\sigma(3d) = 0.35 + 18.00 = 18.35$$
$$Z_{\text{eff}}(3d) = Z - \sigma = 22 - 18.35 = +3.65$$

---

### Step 2: Estimated Single-Electron Orbital Energies

Using Slater's energy formula:
$$E = -13.606\text{ eV} \times \left( \frac{Z_{\text{eff}}}{n^*} \right)^2$$
For $n = 4$, Slater's effective quantum number is $n^* = 3.7$:
$$E(4s) = -13.606 \times \left( \frac{3.15}{3.7} \right)^2 = -13.606 \times (0.85135)^2 = -13.606 \times 0.7248 \approx -9.86\text{ eV}$$

For $n = 3$, $n^* = 3.0$:
$$E(3d) = -13.606 \times \left( \frac{3.65}{3.0} \right)^2 = -13.606 \times (1.21667)^2 = -13.606 \times 1.4803 \approx -20.14\text{ eV}$$
Notice that $E(3d) = -20.14\text{ eV}$ is far more negative (much more tightly bound) than $E(4s) = -9.86\text{ eV}$ in the neutral titanium atom!

---

### Step 3: Analysis of Competing $\text{Ti}^{2+}$ Configurations & Ionization Order

When titanium loses two electrons to form the divalent cation $\text{Ti}^{2+}$, consider the two competing configurations:
* **Configuration A**: $[\text{Ar}] 3d^2$ (both $4s$ electrons removed)
  Slater grouping: $(1s)^2 (2s, 2p)^8 (3s, 3p)^8 (3d)^2$.
  $\sigma(3d) = 1 \times 0.35 + 18 \times 1.00 = 18.35$.
  $Z_{\text{eff}}(3d) = 22 - 18.35 = +3.65$.
  Energy of each $3d$ electron: $-20.14\text{ eV}$.
  Total valence energy $\approx 2 \times (-20.14) = -40.28\text{ eV}$.
* **Configuration B**: $[\text{Ar}] 4s^2$ (both $3d$ electrons removed)
  Slater grouping: $(1s)^2 (2s, 2p)^8 (3s, 3p)^8 (4s)^2$.
  $\sigma(4s) = 1 \times 0.35 + 8 \times 0.85 + 10 \times 1.00 = 0.35 + 6.80 + 10.00 = 17.15$.
  $Z_{\text{eff}}(4s) = 22 - 17.15 = +4.85$.
  Energy of each $4s$ electron: $E(4s) = -13.606 \times (4.85 / 3.7)^2 = -13.606 \times (1.3108)^2 \approx -23.38\text{ eV}$.
  Total valence energy $\approx 2 \times (-23.38) = -46.76\text{ eV}$.
  However, in Configuration A, the two $3d$ electrons enjoy an exchange stabilization energy $-K_{3d}$, whereas the paired $4s^2$ electrons in Configuration B experience inter-electron Coulomb repulsion $J_{4s,4s}$ without any exchange stabilization! High-level ab initio Hartree-Fock calculations and experimental spectroscopic ground states confirm that $[\text{Ar}] 3d^2$ is the true ground state of $\text{Ti}^{2+}$.

#### Resolution of the Aufbau Paradox:
1. **During Neutral Atom Aufbau ($4s$ fills before $3d$)**:
   In potassium ($Z = 19$) and calcium ($Z = 20$), the empty $3d$ orbital has zero radial penetration, whereas the $4s$ orbital possesses small inner radial maxima that penetrate inside the $(1s)^2 (2s)^2 (2p)^6$ core close to the nucleus. This radial penetration lowers the energy of the $4s$ orbital below the empty $3d$ orbital.
2. **Once $3d$ Electrons Are Present (Transition Elements)**:
   As the nuclear charge increases and electrons populate the $3d$ subshell, the $3d$ orbitals contract dramatically toward the nucleus, dropping substantially in energy.
3. **During Ionization ($4s$ leaves first)**:
   Because the $4s$ electrons have a larger principal quantum number ($n = 4$) and a much larger average distance $\langle r \rangle \approx 1.5\text{ Å}$ compared to $\langle r \rangle_{3d} \approx 0.6\text{ Å}$, the $4s$ electrons are on the spatial periphery of the atom, shielded by the inner $3d$ electrons. Consequently, removing a $4s$ electron requires significantly less energy than removing a tightly bound $3d$ electron!"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Exact Quantum Derivation of the 2s Hydrogenic Radial Wavefunction, Radial Node Radius & Expectation Value ⟨r⟩",
                "statement": r"""The normalized radial wavefunction for a hydrogenic atom of atomic number $Z$ in the $n = 2, l = 0$ ($2s$) state is given by:
$$R_{2s}(r) = N_{2s} \left( 2 - \frac{Z r}{a_0} \right) e^{-Z r / (2 a_0)}$$
where $a_0 \equiv \frac{4\pi \varepsilon_0 \hbar^2}{m_e e^2}$ is the Bohr radius, and $N_{2s}$ is the normalization constant.

1. **Prove from first principles** that the normalization constant is:
   $$N_{2s} = \frac{1}{2\sqrt{2}} \left( \frac{Z}{a_0} \right)^{3/2}$$
   *(Hint: Use the standard gamma/Euler integral formula $\int_0^\infty x^n e^{-k x} dx = \frac{n!}{k^{n+1}}$.)*
2. **Determine the exact radius $r_{\text{node}}$** of the spherical radial node for the $2s$ orbital, and express it in terms of $a_0$ and $Z$.
3. **Calculate the exact expectation value $\langle r \rangle_{2s}$** for the electron's distance from the nucleus, and compare it with the ground-state value $\langle r \rangle_{1s} = \frac{3}{2} \frac{a_0}{Z}$.
4. **Prove that the $2s$ orbital is strictly orthogonal** to the $1s$ radial wavefunction $R_{1s}(r) = 2 \left(\frac{Z}{a_0}\right)^{3/2} e^{-Z r / a_0}$ under the spherical radial inner product:
   $$\int_0^\infty R_{1s}(r) R_{2s}(r) r^2 dr = 0$$""",
                "solution": r"""### Step 1: Derivation of the Normalization Constant $N_{2s}$

The normalization condition for the radial function requires:
$$\int_0^\infty [R_{2s}(r)]^2 r^2 dr = 1 \tag{1}$$
Substitute $R_{2s}(r) = N_{2s} (2 - \sigma) e^{-\sigma/2}$, where dimensionless variable $\sigma \equiv \frac{Z r}{a_0} \implies r = \frac{a_0}{Z} \sigma$ and $dr = \frac{a_0}{Z} d\sigma$:
$$r^2 dr = \left(\frac{a_0}{Z}\right)^3 \sigma^2 d\sigma$$
Substitute into Eq. (1):
$$N_{2s}^2 \left(\frac{a_0}{Z}\right)^3 \int_0^\infty (2 - \sigma)^2 e^{-\sigma} \sigma^2 d\sigma = 1 \tag{2}$$
Expand the integrand:
$$(2 - \sigma)^2 \sigma^2 = (4 - 4\sigma + \sigma^2) \sigma^2 = 4\sigma^2 - 4\sigma^3 + \sigma^4$$
The integral becomes:
$$I = \int_0^\infty (4\sigma^2 - 4\sigma^3 + \sigma^4) e^{-\sigma} d\sigma = 4 \int_0^\infty \sigma^2 e^{-\sigma} d\sigma - 4 \int_0^\infty \sigma^3 e^{-\sigma} d\sigma + \int_0^\infty \sigma^4 e^{-\sigma} d\sigma$$
Using the standard identity $\int_0^\infty x^n e^{-x} dx = n!$:
* $n = 2: 2! = 2 \implies 4 \times 2 = 8$
* $n = 3: 3! = 6 \implies -4 \times 6 = -24$
* $n = 4: 4! = 24 \implies 1 \times 24 = 24$
Summing the terms:
$$I = 8 - 24 + 24 = 8 \tag{3}$$
Substitute $I = 8$ back into Eq. (2):
$$N_{2s}^2 \left(\frac{a_0}{Z}\right)^3 (8) = 1 \implies N_{2s}^2 = \frac{1}{8} \left(\frac{Z}{a_0}\right)^3$$
Taking the positive square root:
$$N_{2s} = \frac{1}{\sqrt{8}} \left(\frac{Z}{a_0}\right)^{3/2} = \frac{1}{2\sqrt{2}} \left(\frac{Z}{a_0}\right)^{3/2} \tag{Q.E.D.}$$

---

### Step 2: Exact Radius of the Radial Node

A radial node occurs where the radial wavefunction vanishes ($R_{2s}(r) = 0$):
$$R_{2s}(r) = \frac{1}{2\sqrt{2}} \left(\frac{Z}{a_0}\right)^{3/2} \left( 2 - \frac{Z r}{a_0} \right) e^{-Z r / (2 a_0)} = 0$$
Since exponential $e^{-Z r / (2 a_0)} > 0$ for all finite $r$, the zero must satisfy the polynomial root:
$$2 - \frac{Z r_{\text{node}}}{a_0} = 0 \implies \frac{Z r_{\text{node}}}{a_0} = 2$$
$$r_{\text{node}} = \frac{2 a_0}{Z} \tag{4}$$
For neutral hydrogen ($Z = 1$):
$$r_{\text{node}} = 2 a_0 \approx 2 \times 0.52918\text{ Å} = 1.05836\text{ Å} = 0.1058\text{ nm}$$
At this exact spherical radius $r = 2a_0$, the probability density of finding the $2s$ electron is identically zero!
* Inside the nodal sphere ($r < 2a_0$): $\psi_{2s} > 0$ (positive phase).
* Outside the nodal sphere ($r > 2a_0$): $\psi_{2s} < 0$ (negative phase).

---

### Step 3: Exact Expectation Value $\langle r \rangle_{2s}$

By quantum definition of expectation values:
$$\langle r \rangle_{2s} = \int_0^\infty r [R_{2s}(r)]^2 r^2 dr = \int_0^\infty [R_{2s}(r)]^2 r^3 dr \tag{5}$$
Substitute $r = \frac{a_0}{Z}\sigma$ and $R_{2s}$:
$$\langle r \rangle_{2s} = N_{2s}^2 \left(\frac{a_0}{Z}\right)^4 \int_0^\infty (2 - \sigma)^2 \sigma^3 e^{-\sigma} d\sigma$$
Substitute $N_{2s}^2 = \frac{1}{8} \left(\frac{Z}{a_0}\right)^3$:
$$\langle r \rangle_{2s} = \frac{1}{8} \left(\frac{a_0}{Z}\right) \int_0^\infty (4\sigma^3 - 4\sigma^4 + \sigma^5) e^{-\sigma} d\sigma$$
Evaluate the three integrals via $n!$:
* $\int_0^\infty 4\sigma^3 e^{-\sigma} d\sigma = 4 \times 3! = 4 \times 6 = 24$
* $\int_0^\infty -4\sigma^4 e^{-\sigma} d\sigma = -4 \times 4! = -4 \times 24 = -96$
* $\int_0^\infty \sigma^5 e^{-\sigma} d\sigma = 5! = 120$
Summing terms:
$$J = 24 - 96 + 120 = 48$$
Therefore:
$$\langle r \rangle_{2s} = \frac{1}{8} \left(\frac{a_0}{Z}\right) (48) = 6 \frac{a_0}{Z} \tag{6}$$
For hydrogen ($Z = 1$):
$$\langle r \rangle_{2s} = 6 a_0 \approx 3.175\text{ Å}$$
Comparing with the general hydrogenic formula $\langle r \rangle_{nl} = \frac{a_0}{2Z}[3n^2 - l(l+1)]$:
For $n = 2, l = 0$:
$$\langle r \rangle_{2s} = \frac{a_0}{2Z} [3(4) - 0] = \frac{12 a_0}{2Z} = 6 \frac{a_0}{Z} \tag{Verified}$$
Notice that $\langle r \rangle_{2s} = 6 a_0$ is four times larger than $\langle r \rangle_{1s} = 1.5 a_0$, reflecting the enormous radial expansion of the second quantum shell.

---

### Step 4: Rigorous Proof of Orthogonality between $1s$ & $2s$ States

Compute the radial overlap integral:
$$\mathcal{I}_{12} = \int_0^\infty R_{1s}(r) R_{2s}(r) r^2 dr \tag{7}$$
Given:
$$R_{1s}(r) = 2 \left(\frac{Z}{a_0}\right)^{3/2} e^{-\sigma}$$
$$R_{2s}(r) = \frac{1}{2\sqrt{2}} \left(\frac{Z}{a_0}\right)^{3/2} (2 - \sigma) e^{-\sigma/2}$$
where $\sigma = \frac{Z r}{a_0}, r^2 dr = \left(\frac{a_0}{Z}\right)^3 \sigma^2 d\sigma$.
Multiplying:
$$\mathcal{I}_{12} = \left[ 2 \left(\frac{Z}{a_0}\right)^{3/2} \right] \left[ \frac{1}{2\sqrt{2}} \left(\frac{Z}{a_0}\right)^{3/2} \right] \left(\frac{a_0}{Z}\right)^3 \int_0^\infty e^{-\sigma} (2 - \sigma) e^{-\sigma/2} \sigma^2 d\sigma$$
$$\mathcal{I}_{12} = \frac{1}{\sqrt{2}} \int_0^\infty (2\sigma^2 - \sigma^3) e^{-3\sigma/2} d\sigma \tag{8}$$
Let $u = \frac{3\sigma}{2} \implies \sigma = \frac{2}{3}u, d\sigma = \frac{2}{3}du$:
$$\mathcal{I}_{12} = \frac{1}{\sqrt{2}} \int_0^\infty \left[ 2 \left(\frac{2}{3}u\right)^2 - \left(\frac{2}{3}u\right)^3 \right] e^{-u} \left(\frac{2}{3}\right) du$$
$$\mathcal{I}_{12} = \frac{1}{\sqrt{2}} \left(\frac{2}{3}\right) \left[ 2 \left(\frac{4}{9}\right) \int_0^\infty u^2 e^{-u} du - \left(\frac{8}{27}\right) \int_0^\infty u^3 e^{-u} du \right]$$
Using $\int_0^\infty u^2 e^{-u} du = 2! = 2$ and $\int_0^\infty u^3 e^{-u} du = 3! = 6$:
$$\mathcal{I}_{12} = \frac{\sqrt{2}}{3} \left[ \frac{8}{9}(2) - \frac{8}{27}(6) \right] = \frac{\sqrt{2}}{3} \left[ \frac{16}{9} - \frac{48}{27} \right]$$
Notice that $\frac{48}{27} = \frac{16}{9}$ identically!
$$\mathcal{I}_{12} = \frac{\sqrt{2}}{3} \left[ \frac{16}{9} - \frac{16}{9} \right] = \frac{\sqrt{2}}{3} (0) = 0 \tag{Q.E.D.}$$
This proves conclusively from first principles that the $1s$ and $2s$ radial wavefunctions are mutually orthogonal."""
            }
        ]
    }
'''

with open("build_inorg1_unit1.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_inorg1_unit1.py written successfully.")
