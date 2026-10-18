# -*- coding: utf-8 -*-
"""
build_nuclear_units_1_2_3.py
Builds Units 1, 2, and 3 for Nuclear and Radiochemistry (#47):
- Unit 1: Historical Evolution of Radioactivity & Nuclear Foundations
- Unit 2: Atomic Nucleus: Composition, Binding Energy & Structural Models
- Unit 3: Radioactive Decay Kinetics, Decay Chains & Bateman Equilibria
Strictly Zero Course Numbers or Marks. All math in raw strings r\"\"\"...\"\"\".
"""

import json

def get_units_1_2_3():
    units = [
        # =====================================================================
        # UNIT 1
        # =====================================================================
        {
            "id": "unit-1-historical-evolution-radioactivity",
            "unitNumber": 1,
            "title": "Unit 1: The Discovery of Radioactivity & Evolution of Atomic Theory",
            "leadSummary": "Comprehensive historical, experimental, and mathematical foundation of nuclear discovery: from Becquerel's phosphorescence observations and the Curie isolation of radium to Rutherford's alpha scattering, the Bohr-Sommerfeld quantization, Moseley's atomic number law, Chadwick's discovery of the neutron, and the fundamental taxonomy of nuclear transformations.",
            "simulations": ["sim_nuc_decay_series_bateman"],
            "sections": [
                {
                    "id": "sec-1-1",
                    "secNumber": "1.1",
                    "title": "Historical Genesis: Becquerel, Curies & the Phenomenological Discovery of Radioactivity",
                    "content": r"""The dawn of modern nuclear science began not with deliberate theoretical planning, but through the rigorous investigation of anomalous luminescent phenomena. In early 1896, following Wilhelm Röntgen's discovery of penetrating X-rays emitted by cathode-ray vacuum discharge tubes, the French physicist Henri Becquerel hypothesized that luminescent salts might emit similar penetrating radiations upon exposure to solar illumination.

### Becquerel's Serendipitous Investigation
Becquerel selected potassium uranyl sulfate ($\text{K}_2\text{UO}_2(\text{SO}_4)_2 \cdot 2\text{H}_2\text{O}$), a known phosphorescent compound. Placing crystalline specimens atop photographic emulsion plates wrapped in thick black paper (to shield optical photons) alongside copper silhouettes, Becquerel initially observed weak photographic fogging after solar exposure. In late February 1896, overcast Paris skies halted the solar experiments; Becquerel stored the wrapped plates in a dark cabinet with the uranium salt specimens resting directly on them.

Upon developing the plates on March 1, 1896, anticipating faint or absent images, Becquerel observed intense, sharp silhouettes of the copper objects. Crucially:
1. The emission of penetrating rays was entirely independent of external luminescent excitation (optical or thermal).
2. The radiation persisted indefinitely in total darkness, exhibiting no measurable attenuation over months.
3. The rays spontaneously ionized air, causing charged gold-leaf electroscopes to discharge at a rate proportional to the uranium mass.

Becquerel demonstrated that the emission was an inherent property of uranium itself, independent of whether it existed in elemental form, as uranyl nitrate, or as double sulfates.

### Marie and Pierre Curie: The Atomic Hypothesis and Polonium/Radium Isolation
In 1897, Marie Skłodowska-Curie initiated a systematic quantitative survey of all known elements and mineral ores to determine whether elements other than uranium possessed spontaneous ionizing emissions. Employing a sensitive piezoelectric quartz electrometer designed by Pierre and Jacques Curie, she measured saturation ionization currents in air.

```
Ionizing Radiation
        │
        ▼
   Ion Pairs Created in Air (e⁻ + Ar⁺)
        │
        ▼
   Electric Potential Gradient (Parallel Plate Chamber)
        │
        ▼
   Saturation Ionization Current I = dq/dt
        │
        ▼
   Piezoelectric Quartz Electrometer Null-Balance Metrology
```

Marie Curie established that:
- Thorium compounds also spontaneously emitted penetrating ionizing rays, confirming that uranium was not unique. She coined the term **radioactivity** (*radio-activité*) to describe this atomic property.
- Natural uranium ores—specifically Joachimsthal pitchblende ($\text{U}_3\text{O}_8$) and chalcolite—exhibited specific activities 4 to 5 times greater than pure metallic uranium.

Synthesizing artificial chalcolite ($\text{Cu}(\text{UO}_2)_2(\text{PO}_4)_2 \cdot 8\text{H}_2\text{O}$) from pure laboratory salts, Marie Curie discovered it exhibited only normal uranium activity. This proved that pitchblende contained trace quantities of an unknown element far more radioactive than uranium.

Through arduous fractional crystallization and wet-chemical inorganic separations (precipitating bismuth-sulfide fractions followed by fractional sublimation), Marie and Pierre Curie announced the discovery of:
1. **Polonium** ($^{210}\text{Po}$, named after Marie Curie's native Poland) in July 1898, precipitating alongside bismuth sulfide.
2. **Radium** ($^{226}\text{Ra}$) in December 1898, separating alongside barium chloride via fractional crystallization of the chlorides, exploiting the lower solubility of radium chloride in boiling water and hydrochloric acid.

| Milestone | Year | Discoverer(s) | Key Experimental Technique | Metrological Discovery |
| :--- | :--- | :--- | :--- | :--- |
| **Spontaneous Radioactivity** | 1896 | Henri Becquerel | Photographic fogging & electroscope discharge | Spontaneous penetrating atomic emission from Uranium |
| **Thorium Activity** | 1898 | M. Curie / G. Schmidt | Piezoelectric quartz electrometer | Radioactivity is an element-general atomic property |
| **Discovery of Polonium** | 1898 | P. & M. Curie | $\text{H}_2\text{S}$ precipitation with Bi carrier | Trace emitter $>400\times$ more active than uranium |
| **Discovery of Radium** | 1898 | P. & M. Curie | $\text{BaCl}_2$ fractional crystallization | Million-fold specific activity; isolated pure Ra metal in 1910 |

The Curies demonstrated that radioactivity is an intrinsic **atomic phenomenon**, unaffected by chemical bonding, valence state, temperature (from liquid hydrogen to blast furnaces), pressure, or intense magnetic fields.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-1-2",
                    "secNumber": "1.2",
                    "title": "Rutherford's Gold Foil Scattering & the Emergence of the Nuclear Atomic Model",
                    "content": r"""Prior to 1911, the prevailing paradigm of atomic architecture was J.J. Thomson's "plum pudding" model (1904). In Thomson's conception, an atom of radius $R \approx 10^{-10}\text{ m}$ consisted of a continuous, diffuse sphere of positive electrostatic charge containing $Z$ negatively charged corpuscles (electrons) embedded like raisins in a dough. Because the positive charge was dispersed uniformly throughout the atomic volume, the internal electric field was weak, incapable of exerting massive Coulomb deflections on high-energy charged projectiles.

### The Geiger-Marsden Scattering Experiment
At the University of Manchester, Ernest Rutherford directed Hans Geiger and Ernest Marsden to direct collimated alpha particles ($^{4}\text{He}^{2+}$ with kinetic energy $T_\alpha \approx 5.5\text{ MeV}$) from a bismuth-214 ($^{214}\text{Bi}$) source against ultra-thin gold foils ($\text{Au}$, thickness $t \approx 400\text{ nm} \approx 2000\text{ atomic layers}$). Scintillations produced by scattered alphas were counted visually via a microscope on a zinc sulfide ($\text{ZnS}$) phosphorescent screen in a darkened chamber.

Under Thomson's model, the maximum scattering angle $\theta$ suffered by an alpha particle traversing an entire gold atom was calculated via classical impulse theory:
$$\Delta p_\perp \approx \bar{F}_\perp \Delta t \approx \left(\frac{1}{4\pi\varepsilon_0}\frac{2 Z e^2}{R^2}\right) \left(\frac{2R}{v_\alpha}\right) \implies \theta \approx \frac{\Delta p_\perp}{p_\parallel} \sim 10^{-4}\text{ radians} \approx 0.01^\circ$$
Multiple independent stochastic deflections across 2000 atomic layers should follow a narrow Gaussian distribution, with probability of deflections exceeding $90^\circ$ bounded below $10^{-3500}$.

Astonishingly, Geiger and Marsden discovered that approximately **1 in 8,000** alpha particles suffered deflections greater than $90^\circ$, with some rebounding almost backward ($\theta \approx 180^\circ$). As Rutherford famously remarked: *"It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you."*

### Rutherford Scattering Differential Cross-Section Derivation
To explain the wide-angle deflections, Rutherford posited in 1911 that the entire positive charge $+Z e$ and virtually the total atomic mass $M$ are concentrated in an ultra-dense central core: the **atomic nucleus**, with radius $R_{\text{nuc}} \le 10^{-14}\text{ m}$.

Consider an alpha particle of mass $m$, charge $q_1 = +2e$, and incident velocity $v_0$ approaching a stationary nucleus of charge $q_2 = +Ze$ at an impact parameter $b$. Because the nucleus is far heavier than the alpha particle ($M_{\text{Au}} \approx 197 \gg m_\alpha \approx 4$), the center of mass frame coincides with the lab frame to high precision.

```
       Alpha (2e)
       ───────►              Impact parameter b
                             │
                             ▼
  - - - - - - - - - - - - - - - - - - - - - - - - - - 
                           \   θ (Scattering Angle)
                            \
                             Nucleus (+Ze)
```

The repulsive electrostatic potential is central:
$$V(r) = \frac{1}{4\pi\varepsilon_0} \frac{2 Z e^2}{r}$$

1. **Conservation of Angular Momentum**:
$$L = m v_0 b = m r^2 \frac{d\phi}{dt} = \text{constant} \implies \frac{d\phi}{dt} = \frac{v_0 b}{r^2}$$

2. **Conservation of Linear Momentum (along axis of symmetry)**:
Let the angle between the position vector $\vec{r}$ and the apse of the hyperbolic orbit be $\phi$. The total transverse momentum transfer $\Delta p$ satisfies:
$$\Delta p = 2 m v_0 \sin\left(\frac{\theta}{2}\right) = \int_{-\infty}^{\infty} F_\parallel dt = \int_{-\phi_0}^{\phi_0} \frac{2 Z e^2}{4\pi\varepsilon_0 r^2} \cos\phi \left(\frac{dt}{d\phi}\right) d\phi$$
Substituting $dt/d\phi = r^2 / (v_0 b)$:
$$2 m v_0 \sin\left(\frac{\theta}{2}\right) = \frac{2 Z e^2}{4\pi\varepsilon_0 v_0 b} \int_{-\frac{\pi-\theta}{2}}^{\frac{\pi-\theta}{2}} \cos\phi \, d\phi = \frac{2 Z e^2}{4\pi\varepsilon_0 v_0 b} \cdot 2 \cos\left(\frac{\theta}{2}\right)$$
Dividing both sides by $2 \sin(\theta/2)$:
$$b = \frac{2 Z e^2}{4\pi\varepsilon_0 m v_0^2} \cot\left(\frac{\theta}{2}\right) = \frac{Z e^2}{4\pi\varepsilon_0 T} \cot\left(\frac{\theta}{2}\right)$$
where $T = \frac{1}{2} m v_0^2$ is the projectile kinetic energy.

3. **Differential Cross-Section**:
The incident particles passing through an annular ring of area $d\sigma = 2\pi b |db|$ are scattered into a solid angle $d\Omega = 2\pi \sin\theta d\theta$:
$$\frac{d\sigma}{d\Omega} = \frac{b}{\sin\theta} \left|\frac{db}{d\theta}\right|$$
Differentiating $b$ with respect to $\theta$:
$$\frac{db}{d\theta} = -\frac{Z e^2}{8\pi\varepsilon_0 T} \csc^2\left(\frac{\theta}{2}\right)$$
Using $\sin\theta = 2 \sin(\theta/2) \cos(\theta/2)$ and substituting:
$$\frac{d\sigma}{d\Omega} = \frac{\frac{Z e^2}{4\pi\varepsilon_0 T} \cot\left(\frac{\theta}{2}\right)}{2 \sin\left(\frac{\theta}{2}\right)\cos\left(\frac{\theta}{2}\right)} \cdot \frac{Z e^2}{8\pi\varepsilon_0 T} \csc^2\left(\frac{\theta}{2}\right)$$
Yielding the foundational **Rutherford Scattering Formula**:
$$\frac{d\sigma}{d\Omega} = \left(\frac{1}{4\pi\varepsilon_0}\right)^2 \left(\frac{z Z e^2}{4 T}\right)^2 \frac{1}{\sin^4\left(\frac{\theta}{2}\right)}$$

### Distance of Closest Approach (Head-On Collision)
For a head-on collision ($\theta = 180^\circ$, impact parameter $b = 0$), the entire kinetic energy $T$ transforms into electrostatic potential energy at the distance of closest approach $d_0$:
$$T = \frac{1}{4\pi\varepsilon_0} \frac{z Z e^2}{d_0} \implies d_0 = \frac{1}{4\pi\varepsilon_0} \frac{2 Z e^2}{T}$$
For a $7.7\text{ MeV}$ alpha particle colliding with gold ($Z = 79$):
$$d_0 = \frac{(8.988 \times 10^9)(2)(79)(1.602 \times 10^{-19})^2}{(7.7 \times 10^6 \times 1.602 \times 10^{-19})} \approx 2.96 \times 10^{-14}\text{ m} = 29.6\text{ fm}$$
Because Rutherford scattering followed the pure $1/\sin^4(\theta/2)$ law up to this energy, the radius of the gold nucleus had to be strictly smaller than $30\text{ fm}$—over $10,000$ times smaller than the total atomic radius ($100,000\text{ fm}$). The atom is mostly empty space.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-1-3",
                    "secNumber": "1.3",
                    "title": "Bohr-Sommerfeld Quantum Atom, Moseley's X-Ray Law & Atomic Number Z",
                    "content": r"""Rutherford's nuclear planetary model suffered a fatal classical instability: according to Maxwellian electrodynamics, an accelerating electron on a circular orbit must continuously radiate electromagnetic energy at the Larmor rate:
$$P = \frac{e^2 a^2}{6\pi\varepsilon_0 c^3} = \frac{e^2}{6\pi\varepsilon_0 c^3} \left(\frac{v^2}{r}\right)^2$$
This continuous radiative loss would cause the electron to spiral into the nucleus within $\tau \sim 10^{-11}\text{ seconds}$, predicting an instantaneous collapse of all matter and a continuous emission spectrum.

### The Bohr Postulates (1913)
Niels Bohr resolved this crisis by introducing quantum hypotheses:
1. **Stationary States**: Electrons occupy discrete circular orbits characterized by non-radiating stationary energy states.
2. **Quantization of Orbital Angular Momentum**:
$$L = m_e v r = n \hbar = n \frac{h}{2\pi}, \quad n \in \{1, 2, 3, \dots\}$$
3. **Bohr Frequency Condition**: Emission or absorption occurs only during discontinuous transitions between stationary states:
$$\Delta E = E_i - E_f = h\nu = \hbar \omega$$

Equating the centripetal force to the Coulomb electrostatic attraction:
$$\frac{m_e v^2}{r} = \frac{1}{4\pi\varepsilon_0}\frac{Z e^2}{r^2} \implies v = \frac{Z e^2}{4\pi\varepsilon_0 n \hbar}$$
Substituting velocity into the orbital radius expression:
$$r_n = \frac{4\pi\varepsilon_0 \hbar^2 n^2}{m_e Z e^2} = \frac{n^2}{Z} a_0$$
where $a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m_e e^2} \approx 0.529177 \times 10^{-10}\text{ m} = 0.529\text{ \AA}$ is the first Bohr radius of hydrogen.

The total mechanical energy in state $n$ is:
$$E_n = T + V = \frac{1}{2}m_e v^2 - \frac{Z e^2}{4\pi\varepsilon_0 r} = -\frac{1}{2} \frac{Z e^2}{4\pi\varepsilon_0 r_n} = -\frac{m_e Z^2 e^4}{32\pi^2\varepsilon_0^2 \hbar^2 n^2} = -\frac{Z^2}{n^2} R_\infty h c$$
where the Rydberg constant for an infinitely massive nucleus is:
$$R_\infty = \frac{m_e e^4}{8\varepsilon_0^2 h^3 c} \approx 109,737.31568\text{ cm}^{-1} \implies E_1 = -13.606\text{ eV} \cdot Z^2$$

### Moseley's Law and the Physical Meaning of Atomic Number Z (1913-1914)
Prior to 1913, elements were arranged in Dmitri Mendeleev's periodic table in order of increasing atomic weight $A$. This introduced notable anomalies:
- Argon ($A = 39.95$) preceded Potassium ($A = 39.10$).
- Tellurium ($A = 127.60$) preceded Iodine ($A = 126.90$).
- Cobalt ($A = 58.93$) preceded Nickel ($A = 58.69$).

Henry Moseley systematically bombarded 38 elements from aluminum to gold with high-energy electron beams in a vacuum tube and recorded their characteristic X-ray emission spectra via Bragg crystal spectrometry ($n\lambda = 2d \sin\theta$).

Moseley discovered that the frequency $\nu$ of the characteristic $K_\alpha$ and $L_\alpha$ lines satisfied a remarkably precise linear relationship with the integer position index $Z$ of the element:
$$\sqrt{\nu} = a (Z - \sigma)$$
where $a$ is a proportionality constant and $\sigma$ is an electrostatic screening (shielding) constant ($\sigma \approx 1$ for $K_\alpha$ transitions; $\sigma \approx 7.4$ for $L_\alpha$ transitions).

```
   √ν (Square Root of X-Ray Frequency)
     ▲
     │           /  K_α Line: √ν = C(Z - 1)
     │          /
     │         /
     │        /
     │       /
     │      /
     │     /
     │    /
     │   /
     └──┴────────────────────────► Atomic Number Z
        1  2  3  4  5 ...
```

For the $K_\alpha$ transition, an electron drops from the $n = 2$ ($L$-shell) to $n = 1$ ($K$-shell). Because one electron remains in the $1s$ orbital, the effective nuclear charge experienced by the transitioning electron is screened to $Z_{\text{eff}} = Z - 1$:
$$h\nu_{K_\alpha} = R_\infty h c (Z - 1)^2 \left(\frac{1}{1^2} - \frac{1}{2^2}\right) = \frac{3}{4} R_\infty h c (Z - 1)^2$$
Taking the square root:
$$\sqrt{\nu_{K_\alpha}} = \sqrt{\frac{3}{4} R_\infty c} (Z - 1)$$

Moseley's law proved unequivocally that:
1. **Atomic Number $Z$ is not an arbitrary sorting index**, but the exact fundamental integer number of positive elemental charges $+e$ in the nucleus.
2. The inversions in the periodic table (Ar/K, Co/Ni, Te/I) were resolved because $Z$ was monotonically increasing even when atomic weight did not.
3. Moseley identified missing elements with precision, predicting the existence of unknown elements at $Z = 43$ (Technetium), $Z = 61$ (Promethium), $Z = 72$ (Hafnium), and $Z = 75$ (Rhenium).""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-1-4",
                    "secNumber": "1.4",
                    "title": "The Discovery of the Neutron: Chadwick, Bothe-Becker & Nuclear Constituents",
                    "content": r"""Following the discovery that the nucleus possessed positive charge $+Ze$ while having an atomic mass $A$ approximately twice $Z$, physicists initially hypothesized the **proton-electron model of the nucleus**. In this view, a nucleus with mass number $A$ and atomic number $Z$ consisted of $A$ protons and $A - Z$ "nuclear electrons" bound tightly inside the core.

### Fatal Flaws of the Proton-Electron Nuclear Hypothesis
By the late 1920s, quantum mechanics demonstrated that the proton-electron model was physically untenable:

1. **Heisenberg Uncertainty Principle**:
If an electron is confined inside a nuclear volume of diameter $\Delta x \approx 2 R \approx 10^{-14}\text{ m}$, its momentum uncertainty must satisfy:
$$\Delta p \ge \frac{\hbar}{2 \Delta x} \approx \frac{1.055 \times 10^{-34}\text{ J}\cdot\text{s}}{2 \times 10^{-14}\text{ m}} \approx 5.3 \times 10^{-21}\text{ kg}\cdot\text{m/s}$$
For a relativistic electron ($E \approx p c$):
$$E \approx (5.3 \times 10^{-21}\text{ kg}\cdot\text{m/s})(3 \times 10^8\text{ m/s}) \approx 1.6 \times 10^{-12}\text{ J} \approx 10\text{ MeV}$$
Electrons emitted in beta decay possessed kinetic energies of only $\sim 0.1\text{ to }3\text{ MeV}$, and no known nuclear potential well was deep enough to confine an electron with $>10\text{ MeV}$ zero-point energy.

2. **Nuclear Spin Paradox**:
Consider the nitrogen-14 nucleus ($^{14}\text{N}$, $Z = 7, A = 14$). Under the proton-electron model, it must contain 14 protons and 7 electrons, totaling $21$ spin-$1/2$ fermions. An odd number of fermions must possess a half-integer total spin:
$$I(^{14}\text{N}) \in \left\{\frac{1}{2}, \frac{3}{2}, \frac{5}{2}, \dots\right\} \implies \text{Fermi-Dirac statistics}$$
However, molecular band spectra of $\text{N}_2$ (Rasetti, 1929) proved definitively that $^{14}\text{N}$ has an **integer spin $I = 1$** and obeys **Bose-Einstein statistics**.

3. **Nuclear Magnetic Moments**:
The electron possesses a Dirac magnetic moment:
$$\mu_B = \frac{e\hbar}{2m_e} \approx 9.274 \times 10^{-24}\text{ J/T}$$
If electrons existed inside the nucleus, nuclear magnetic moments should be on the order of $\mu_B$. In reality, measured nuclear magnetic moments were $\sim 1000$ times smaller, scaling with the nuclear magneton:
$$\mu_N = \frac{e\hbar}{2m_p} = \frac{\mu_B}{1836.15} \approx 5.051 \times 10^{-27}\text{ J/T}$$

### The Experimental Sequence to the Neutron
In 1930, Walther Bothe and Herbert Becker bombarded light elements ($\text{Be}, \text{B}, \text{Li}$) with energetic alpha particles from a polonium source. Beryllium emitted an extraordinarily penetrating, electrically neutral radiation capable of traversing several centimeters of lead:
$$^{9}\text{Be} + \alpha \longrightarrow \text{Penetrating Neutral Rays}$$
Bothe and Becker assumed this radiation was ultra-hard bremsstrahlung or high-energy gamma rays ($h\nu \sim 10\text{ MeV}$).

In 1932, Irène Joliot-Curie and Frédéric Joliot placed paraffin wax ($\text{C}_n\text{H}_{2n+2}$, rich in hydrogen atoms) in the path of the radiation. They observed that the mysterious neutral rays ejected high-energy recoil protons from the paraffin with kinetic energies up to $T_p \approx 5.7\text{ MeV}$.
Assuming the rays were gamma photons ($m = 0$) undergoing Compton-like scattering with protons:
$$T_p = \frac{2 h\nu}{1 + \frac{m_p c^2}{2 h\nu}} \implies h\nu \ge \sqrt{\frac{m_p c^2 T_p}{2}} \approx 55\text{ MeV}$$
A $55\text{ MeV}$ photon could not be produced by a $5.3\text{ MeV}$ alpha reaction due to energy conservation limits.

### James Chadwick's Breakthrough (1932)
James Chadwick repeated the experiment using an ionization chamber connected to an oscilloscope, measuring recoil velocities not only from paraffin (protons, $A = 1$) but also from helium ($A = 4$), lithium ($A = 7$), beryllium ($A = 9$), carbon ($A = 12$), and nitrogen ($A = 14$).

Chadwick modeled the interaction as a classical, non-relativistic elastic head-on collision between a neutral particle of mass $m_n$ and velocity $v_n$ and target nuclei of mass $M$ at rest.
By conservation of momentum and energy:
$$m_n v_n = m_n v'_n + M V_{\text{recoil}}$$
$$\frac{1}{2}m_n v_n^2 = \frac{1}{2}m_n (v'_n)^2 + \frac{1}{2}M V_{\text{recoil}}^2$$
Solving for the recoil velocity $V$:
$$V_{\text{recoil}} = \frac{2 m_n}{m_n + M} v_n$$
Chadwick measured the maximum recoil velocity of protons ($V_p$) and nitrogen nuclei ($V_N$):
$$\frac{V_p}{V_N} = \frac{m_n + M_N}{m_n + m_p}$$
Substituting the experimental values $V_p \approx 3.3 \times 10^7\text{ m/s}$ and $V_N \approx 4.7 \times 10^6\text{ m/s}$, with $m_p \approx 1\text{ u}$ and $M_N \approx 14\text{ u}$:
$$\frac{3.3 \times 10^7}{4.7 \times 10^6} \approx 7.02 = \frac{m_n + 14}{m_n + 1} \implies 7.02(m_n + 1) = m_n + 14 \implies 6.02 m_n \approx 6.98 \implies m_n \approx 1.15\text{ u} \approx 1\text{ u}$$

Chadwick established the existence of a neutral baryon with mass nearly equal to the proton: the **neutron**:
$$^{9}_4\text{Be} + ^{4}_2\alpha \longrightarrow ^{12}_6\text{C} + ^{1}_0n$$
The discovery immediately resolved all quantum paradoxes: $^{14}\text{N}$ contains 7 protons and 7 neutrons (14 total fermions), naturally giving integer spin $I = 1$ and Bose-Einstein statistics.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-1-5",
                    "secNumber": "1.5",
                    "title": "Tripartite Radiation Phenomenology: Physical Properties of Alpha, Beta & Gamma Rays",
                    "content": r"""Natural radionuclides emit three primary categories of penetrating radiations, designated by Rutherford (1899) as alpha ($\alpha$), beta ($\beta$), and gamma ($\gamma$) radiation according to their penetrating power in matter.

### 1. Alpha Radiation ($\alpha$)
Alpha particles are helium-4 nuclei ($^{4}\text{He}^{2+}$) consisting of two protons and two neutrons tightly bound ($B \approx 28.3\text{ MeV}$).
- **Charge**: $q = +2e = +3.204 \times 10^{-19}\text{ C}$.
- **Rest Mass**: $m_\alpha = 4.001506\text{ u} = 6.644657 \times 10^{-27}\text{ kg} \approx 3727.38\text{ MeV}/c^2$.
- **Emission Energies**: Monoenergetic discrete lines typically between $4.0\text{ MeV}$ and $9.0\text{ MeV}$ (e.g., $^{238}\text{U} \to 4.198\text{ MeV}$; $^{212}\text{Po} \to 8.785\text{ MeV}$).
- **Velocity**: $v_\alpha \approx 1.4 \times 10^7\text{ m/s}$ to $2.1 \times 10^7\text{ m/s}$ ($\sim 0.05 c$).
- **Linear Energy Transfer (LET)**: Extremely high, $\sim 100\text{ keV}/\mu\text{m}$.
- **Range**: Only $2\text{ to }8\text{ cm}$ in air; stopped completely by a single sheet of paper or the dead stratum corneum of human skin ($\sim 40\,\mu\text{m}$).

### 2. Beta Radiation ($\beta^-$ and $\beta^+$)
Beta particles are high-speed electrons ($\beta^-$) or positrons ($\beta^+$) ejected from the nucleus during weak force isobaric transitions.
- **Charge**: $q = -e$ ($\beta^-$) or $q = +e$ ($\beta^+$).
- **Rest Mass**: $m_e = 0.00054858\text{ u} = 9.10938 \times 10^{-31}\text{ kg} \approx 0.5109989\text{ MeV}/c^2$.
- **Energy Spectrum**: **Continuous** from zero to a well-defined endpoint energy $E_{\max}$ ($Q_\beta$), because decay energy is shared stochastically with a three-body partner (antineutrino $\bar{\nu}_e$ or neutrino $\nu_e$):
$$n \longrightarrow p + e^- + \bar{\nu}_e, \quad p \longrightarrow n + e^+ + \nu_e$$
- **Velocity**: Highly relativistic, $v_\beta \approx 0.5c\text{ to }>0.999c$.
- **Linear Energy Transfer**: Low LET, $\sim 0.2\text{ keV}/\mu\text{m}$.
- **Range**: Several meters in air, a few millimeters in soft tissue; attenuated completely by a few millimeters of aluminum or Lucite acrylic. High-$Z$ shields must be avoided to prevent bremsstrahlung X-ray production.

### 3. Gamma Radiation ($\gamma$)
Gamma rays are high-energy, uncharged electromagnetic photons emitted during transitions between excited nuclear states following preceding alpha or beta decay.
- **Charge**: $q = 0$.
- **Rest Mass**: $m_0 = 0$.
- **Velocity**: Exactly $c = 2.99792458 \times 10^8\text{ m/s}$ in vacuum.
- **Energy**: Discrete photon energies typically ranging from $10\text{ keV}$ to $10\text{ MeV}$ ($\lambda \sim 10^{-11}\text{ to }10^{-14}\text{ m}$).
- **Penetrating Power**: Exponential attenuation in matter:
$$I(x) = I_0 e^{-\mu x}$$
Requires centimeters of dense lead ($\text{Pb}$), depleted uranium ($\text{DU}$), or meters of reinforced concrete to attenuate by factors of $10^3\text{ to }10^6$.

| Property | Alpha ($\alpha$) | Beta ($\beta^-$ / $\beta^+$) | Gamma ($\gamma$) |
| :--- | :--- | :--- | :--- |
| **Physical Identity** | $^{4}\text{He}^{2+}$ nucleus | Fast electron / positron | Electromagnetic photon |
| **Charge ($e$)** | $+2$ | $-1$ or $+1$ | $0$ |
| **Rest Mass** | $6.645 \times 10^{-27}\text{ kg}$ ($4.0015\text{ u}$) | $9.109 \times 10^{-31}\text{ kg}$ ($0.00055\text{ u}$) | $0$ |
| **Typical Energy** | $4 - 9\text{ MeV}$ (Discrete) | $0.018 - 3.5\text{ MeV}$ (Continuous) | $0.05 - 3.0\text{ MeV}$ (Discrete) |
| **Velocity ($c$)** | $\sim 0.05 c$ | $0.5 c - 0.999 c$ | $1.0 c$ |
| **Specific Ionization** | $10^4 - 10^5\text{ ion pairs/mm air}$ | $50 - 500\text{ ion pairs/mm air}$ | $1 - 10\text{ ion pairs/mm air}$ |
| **Range in Air** | $2.5 - 8.5\text{ cm}$ | $0.5 - 10\text{ m}$ | Tens to hundreds of meters |
| **Shielding Material** | Paper, skin, air column | Plastic (acrylic), Al sheet | Lead, steel, thick concrete |""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-1-6",
                    "secNumber": "1.6",
                    "title": "Fundamental Laws of Radioactive Transformation: Rutherford-Soddy Hypothesis & Disintegration Rates",
                    "content": r"""In 1902-1903, Ernest Rutherford and Frederick Soddy published their revolutionary **theory of atomic disintegration**. Overturning the ancient chemical doctrine of elemental immutability, Rutherford and Soddy stated that radioactivity is an explosive subatomic transformation in which an atom of one chemical element spontaneously changes into an atom of a completely different chemical element.

### The Fundamental Differential Rate Law
Radioactive decay is an intrinsically stochastic quantum phenomenon. The probability that a given unstable radioactive nucleus will undergo nuclear transition within an infinitesimal time increment $dt$ is a constant, denoted by the **decay constant** $\lambda$ (dimensions $\text{time}^{-1}$).

Because each nucleus decays independently of its neighbors and is unaffected by past history (a memoryless Poisson process), the net rate of disintegration $-dN/dt$ occurring in an ensemble of $N(t)$ identical radioactive nuclei is directly proportional to the number of surviving parent nuclei present at that instant:
$$-\frac{dN}{dt} = \lambda N(t)$$

Separating variables:
$$\frac{dN}{N} = -\lambda \, dt$$
Integrating both sides from $t = 0$ (where $N = N_0$) to time $t$:
$$\int_{N_0}^{N(t)} \frac{dN'}{N'} = -\lambda \int_0^t dt' \implies \ln\left(\frac{N(t)}{N_0}\right) = -\lambda t$$
Exponentiating both sides yields the foundational **Exponential Decay Law**:
$$N(t) = N_0 e^{-\lambda t}$$

```
   Number of Surviving Nuclei N(t)
   N₀ ▲
      │\
      │ \
 N₀/2 │--\---- (Half-Life T₁/₂)
      │   \
 N₀/4 │----\-- (Two Half-Lives 2T₁/₂)
      │     \
      └──────┴──────┴────────────────► Time t
             T₁/₂   2T₁/₂
```

### Derivation of Half-Life ($T_{1/2}$) and Mean Life ($\tau$)
The **half-life** $T_{1/2}$ is the time required for one-half of the initial population of radioactive atoms to disintegrate:
$$N(T_{1/2}) = \frac{N_0}{2} = N_0 e^{-\lambda T_{1/2}}$$
Dividing by $N_0$ and taking the natural logarithm:
$$\ln\left(\frac{1}{2}\right) = -\lambda T_{1/2} \implies -\ln 2 = -\lambda T_{1/2}$$
$$T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.69314718\dots}{\lambda}$$

The **mean life** (or average lifetime) $\tau$ of a radioactive nucleus represents the mathematical expectation value of the survival time $t$:
$$\tau = \langle t \rangle = \frac{\int_0^\infty t \left|\frac{dN}{dt}\right| dt}{\int_0^\infty \left|\frac{dN}{dt}\right| dt} = \frac{\int_0^\infty t (\lambda N_0 e^{-\lambda t}) dt}{N_0} = \lambda \int_0^\infty t e^{-\lambda t} dt$$
Integrating by parts ($\int u \, dv = u v - \int v \, du$ with $u = t, dv = e^{-\lambda t} dt$):
$$\int_0^\infty t e^{-\lambda t} dt = \left[ -\frac{t}{\lambda} e^{-\lambda t} \right]_0^\infty + \frac{1}{\lambda} \int_0^\infty e^{-\lambda t} dt = 0 + \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$$
Therefore:
$$\tau = \lambda \left(\frac{1}{\lambda^2}\right) = \frac{1}{\lambda}$$
The relationship between half-life and mean life is:
$$\tau = \frac{T_{1/2}}{\ln 2} \approx 1.442695 \cdot T_{1/2}$$
During one mean life $\tau$, the population decreases to $1/e \approx 36.788\%$ of its initial value:
$$N(\tau) = N_0 e^{-\lambda (1/\lambda)} = N_0 e^{-1} \approx 0.3679 N_0$$""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-1-7",
                    "secNumber": "1.7",
                    "title": "Metrology of Nuclear Activity: Becquerel, Curie, Specific Activity & Disintegration Standards",
                    "content": r"""In radiochemical metrology, the primary quantity describing the source strength of a radioactive substance is **radioactivity** (or simply **activity**), denoted by $A(t)$. Activity is defined as the absolute rate of nuclear transformations (disintegrations) per unit time:
$$A(t) = \left| \frac{dN}{dt} \right| = \lambda N(t) = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$$

### Units of Radioactive Activity
1. **The Becquerel (Bq)**:
The derived SI unit of activity is the **Becquerel**, defined by the 15th General Conference on Weights and Measures (CGPM) in 1975:
$$1\text{ Bq} = 1\text{ nuclear disintegration per second } (1\text{ dps}) = 1\text{ s}^{-1}$$
Multiples include:
- Kilobecquerel ($\text{kBq} = 10^3\text{ Bq}$)
- Megabecquerel ($\text{MBq} = 10^6\text{ Bq}$)
- Gigabecquerel ($\text{GBq} = 10^9\text{ Bq}$)
- Terabecquerel ($\text{TBq} = 10^{12}\text{ Bq}$)
- Petabecquerel ($\text{PBq} = 10^{15}\text{ Bq}$)

2. **The Curie (Ci)**:
The historical non-SI unit, originally established in 1910 to honor Marie and Pierre Curie, was defined as the activity of radon gas ($^{222}\text{Rn}$) in radioactive equilibrium with $1.000\text{ gram}$ of pure radium-226 ($^{226}\text{Ra}$).
In 1953, the International Commission on Radiation Units and Measurements (ICRU) standardized the Curie as an exact physical definition:
$$1\text{ Ci} \equiv 3.700 \times 10^{10}\text{ disintegrations per second} = 3.700 \times 10^{10}\text{ Bq} = 37\text{ GBq}$$
Common subunits:
- Millicurie ($\text{mCi} = 10^{-3}\text{ Ci} = 37\text{ MBq}$)
- Microcurie ($\mu\text{Ci} = 10^{-6}\text{ Ci} = 37\text{ kBq}$)
- Nanocurie ($\text{nCi} = 10^{-9}\text{ Ci} = 37\text{ Bq}$)
- Picocurie ($\text{pCi} = 10^{-12}\text{ Ci} = 0.037\text{ Bq}$)

3. **The Rutherford (rd)**:
A short-lived unit proposed in 1946:
$$1\text{ rd} \equiv 1.0 \times 10^6\text{ dps} = 1\text{ MBq}$$

### Specific Activity Formulation
The **specific activity** ($a$ or $SA$) represents the activity per unit mass of a pure radionuclide or labeled chemical substance:
$$a = \frac{A}{m} = \frac{\lambda N}{m}$$
For a chemically pure, carrier-free radionuclide of molar mass $M$ ($\text{g/mol}$) and half-life $T_{1/2}$ ($\text{seconds}$), the number of atoms per gram is $N_A / M$, where $N_A = 6.02214076 \times 10^{23}\text{ mol}^{-1}$:
$$a = \frac{\lambda N_A}{M} = \frac{\ln 2}{T_{1/2}} \frac{N_A}{M} = \frac{0.69315 \times 6.02214 \times 10^{23}}{M \cdot T_{1/2}} = \frac{4.174 \times 10^{23}}{M \cdot T_{1/2}}\text{ Bq/g}$$

Converting specific activity to Curies per gram ($\text{Ci/g}$):
$$a_{\text{Ci/g}} = \frac{4.174 \times 10^{23}}{3.7 \times 10^{10} \cdot M \cdot T_{1/2}} \approx \frac{1.128 \times 10^{13}}{M \cdot T_{1/2 (\text{sec})}}\text{ Ci/g}$$

| Radionuclide | Half-Life $T_{1/2}$ | Molar Mass $M$ | Carrier-Free Specific Activity ($\text{Bq/g}$) | Specific Activity ($\text{Ci/g}$) |
| :--- | :--- | :--- | :--- | :--- |
| **Uranium-238** | $4.468 \times 10^9\text{ yr}$ | $238.05\text{ g/mol}$ | $1.24 \times 10^4\text{ Bq/g}$ | $0.336\,\mu\text{Ci/g}$ |
| **Radium-226** | $1600\text{ yr}$ | $226.03\text{ g/mol}$ | $3.66 \times 10^{10}\text{ Bq/g}$ | $0.989\text{ Ci/g} \approx 1\text{ Ci/g}$ |
| **Cobalt-60** | $5.271\text{ yr}$ | $59.93\text{ g/mol}$ | $4.18 \times 10^{13}\text{ Bq/g}$ | $1,130\text{ Ci/g}$ |
| **Iodine-131** | $8.025\text{ days}$ | $130.91\text{ g/mol}$ | $4.60 \times 10^{15}\text{ Bq/g}$ | $124,000\text{ Ci/g}$ |
| **Technetium-99m** | $6.007\text{ hours}$ | $98.91\text{ g/mol}$ | $1.95 \times 10^{17}\text{ Bq/g}$ | $5,270,000\text{ Ci/g}$ |
| **Polonium-210** | $138.38\text{ days}$ | $209.98\text{ g/mol}$ | $1.66 \times 10^{14}\text{ Bq/g}$ | $4,490\text{ Ci/g}$ |

Notice the dramatic inverse proportionality: radionuclides with short half-lives exhibit enormous specific activities. A single microgram of carrier-free $^{99m}\text{Tc}$ possesses an activity of nearly $200\text{ MBq}$, sufficient for multiple clinical SPECT scans.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                }
            ],
            "problems": [
                {
                    "id": "prob-1-1",
                    "problemNumber": "1.1",
                    "title": "Rutherford Scattering Distance of Closest Approach & Cross-Section Ratio",
                    "difficulty": "Intermediate",
                    "statement": r"""A beam of alpha particles with laboratory kinetic energy $T_\alpha = 6.00\text{ MeV}$ is directed against an ultra-thin gold foil ($Z = 79$). 
1. Calculate the classical distance of closest approach $d_0$ for a head-on collision ($\theta = 180^\circ$).
2. Compute the ratio of the differential scattering cross-section at $\theta_1 = 60^\circ$ to that at $\theta_2 = 120^\circ$.""",
                    "solution": r"""### Step 1: Classical Distance of Closest Approach
In a head-on collision ($b = 0$, $\theta = 180^\circ$), the alpha particle comes momentarily to rest when all its kinetic energy converts to electrostatic potential energy:
$$T_\alpha = \frac{1}{4\pi\varepsilon_0} \frac{z Z e^2}{d_0}$$
where $z = 2$ for alpha, $Z = 79$ for gold, and $T_\alpha = 6.00\text{ MeV} = 6.00 \times 10^6 \times 1.60218 \times 10^{-19}\text{ J} = 9.613 \times 10^{-13}\text{ J}$.
Using $\frac{1}{4\pi\varepsilon_0} \approx 8.98755 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$:
$$d_0 = \frac{(8.98755 \times 10^9)(2)(79)(1.60218 \times 10^{-19})^2}{9.613 \times 10^{-13}\text{ J}} = \frac{3.6427 \times 10^{-26}}{9.613 \times 10^{-13}} = 3.789 \times 10^{-14}\text{ m} = 37.9\text{ fm}$$

### Step 2: Ratio of Differential Scattering Cross-Sections
Rutherford's differential cross-section formula states:
$$\frac{d\sigma}{d\Omega} \propto \frac{1}{\sin^4(\theta/2)}$$
The ratio of cross-sections at $\theta_1 = 60^\circ$ ($\theta_1/2 = 30^\circ$) and $\theta_2 = 120^\circ$ ($\theta_2/2 = 60^\circ$) is:
$$\frac{\frac{d\sigma}{d\Omega}(60^\circ)}{\frac{d\sigma}{d\Omega}(120^\circ)} = \frac{\sin^4(60^\circ)}{\sin^4(30^\circ)} = \left(\frac{\sin 60^\circ}{\sin 30^\circ}\right)^4 = \left(\frac{\sqrt{3}/2}{1/2}\right)^4 = (\sqrt{3})^4 = 9$$
Thus, the scattering cross section at $60^\circ$ is exactly **9 times larger** than at $120^\circ$.""",
                    "hints": ["Remember that kinetic energy must be converted from MeV to Joules (1 MeV = 1.602e-13 J).", "The cross-section angular dependence is governed strictly by the factor 1/sin^4(theta/2)."]
                },
                {
                    "id": "prob-1-2",
                    "problemNumber": "1.2",
                    "title": "Moseley's Law and Characteristic X-Ray Wavelength of Unknown Element",
                    "difficulty": "Intermediate",
                    "statement": r"""A target of an unknown metallic element is bombarded with electrons. The measured wavelength of the characteristic $K_\alpha$ X-ray line is $\lambda_{K_\alpha} = 0.15418\text{ nm}$ ($1.5418\text{ \AA}$).
Given the Rydberg constant $R_\infty = 1.097373 \times 10^7\text{ m}^{-1}$ and screening constant $\sigma = 1$:
1. Derive the atomic number $Z$ of the metallic target.
2. Identify the chemical element.""",
                    "solution": r"""### Step 1: Theoretical Formula for $K_\alpha$ Transition
According to Moseley's law and the Bohr-Rydberg formula:
$$\frac{1}{\lambda_{K_\alpha}} = R_\infty (Z - 1)^2 \left(\frac{1}{1^2} - \frac{1}{2^2}\right) = \frac{3}{4} R_\infty (Z - 1)^2$$

### Step 2: Solve for $(Z - 1)$
Given $\lambda = 0.15418 \times 10^{-9}\text{ m}$:
$$\frac{1}{0.15418 \times 10^{-9}\text{ m}} = 6.4859 \times 10^6\text{ m}^{-1}$$
Equating:
$$6.4859 \times 10^6 = \frac{3}{4} (1.097373 \times 10^7) (Z - 1)^2 = 8.2303 \times 10^6 (Z - 1)^2$$
$$(Z - 1)^2 = \frac{6.4859 \times 10^6}{8.2303 \times 10^6} \approx 788.05 \implies Z - 1 = \sqrt{788.05} \approx 28.07$$
Rounding to the nearest integer:
$$Z - 1 = 28 \implies Z = 29$$

### Step 3: Elemental Identification
Element $Z = 29$ is **Copper ($\text{Cu}$)**. The emission line is the globally famous **$\text{Cu } K_\alpha$ line** ubiquitous in X-ray powder diffraction (XRD).""",
                    "hints": ["Use the Rydberg equation with effective charge Z - 1.", "Ensure units of wavelength are converted from nm to meters before taking reciprocal wave numbers."]
                },
                {
                    "id": "prob-1-3",
                    "problemNumber": "1.3",
                    "title": "Chadwick Neutron Mass Determination from Elastic Recoil Kinematics",
                    "difficulty": "Advanced",
                    "statement": r"""In Chadwick's 1932 discovery experiment, a beam of unknown neutral particles collides elastically and head-on with stationary protons ($M_p = 1.0073\text{ u}$) and nitrogen nuclei ($M_N = 14.003\text{ u}$).
The measured maximum recoil velocities are $V_p = 3.30 \times 10^7\text{ m/s}$ for protons and $V_N = 4.72 \times 10^6\text{ m/s}$ for nitrogen.
1. Formulate the ratio of recoil velocities in terms of neutron mass $m_n$.
2. Calculate the experimental mass of the neutron $m_n$ in atomic mass units ($\text{u}$).""",
                    "solution": r"""### Step 1: Classical 1D Elastic Collision Kinematics
For a particle of mass $m_n$ moving with incident speed $v_n$ striking a target mass $M$ initially at rest:
By conservation of momentum:
$$m_n v_n = m_n v'_n + M V$$
By conservation of kinetic energy:
$$\frac{1}{2}m_n v_n^2 = \frac{1}{2}m_n (v'_n)^2 + \frac{1}{2} M V^2$$
Expressing $v'_n = v_n - \frac{M}{m_n} V$ and substituting into the energy equation yields:
$$V = \frac{2 m_n}{m_n + M} v_n$$

### Step 2: Velocity Ratio Formulation
The ratio of proton recoil velocity to nitrogen recoil velocity is:
$$\frac{V_p}{V_N} = \frac{\frac{2 m_n}{m_n + M_p} v_n}{\frac{2 m_n}{m_n + M_N} v_n} = \frac{m_n + M_N}{m_n + M_p}$$

### Step 3: Calculate $m_n$
Compute the empirical ratio:
$$\frac{V_p}{V_N} = \frac{3.30 \times 10^7\text{ m/s}}{4.72 \times 10^6\text{ m/s}} \approx 6.9915$$
Set up the linear equation:
$$6.9915 = \frac{m_n + 14.003}{m_n + 1.0073}$$
$$6.9915(m_n + 1.0073) = m_n + 14.003$$
$$6.9915 m_n + 7.0425 = m_n + 14.003$$
$$5.9915 m_n = 14.003 - 7.0425 = 6.9605$$
$$m_n = \frac{6.9605}{5.9915} \approx 1.16\text{ u}$$
Considering higher-order experimental corrections and finite scattering angles, Chadwick obtained $m_n = 1.008\text{ u}$, very close to the modern value of $1.008665\text{ u}$.""",
                    "hints": ["Set up the elastic head-on collision formula for recoil velocity: V = 2*m_n / (m_n + M) * v_n.", "Divide the two velocity expressions to cancel the unknown incident neutron speed v_n."]
                },
                {
                    "id": "prob-1-4",
                    "problemNumber": "1.4",
                    "title": "Specific Activity of Carrier-Free Iodine-131 and Patient Administration Mass",
                    "difficulty": "Easy",
                    "statement": r"""A nuclear medicine patient undergoing radioiodine thyroid therapy receives an oral therapeutic dose of $100\text{ mCi}$ of carrier-free $^{131}\text{I}$. 
The physical half-life of $^{131}\text{I}$ is $T_{1/2} = 8.025\text{ days}$ and its atomic mass is $130.91\text{ g/mol}$.
1. Calculate the decay constant $\lambda$ in $\text{s}^{-1}$.
2. Determine the carrier-free specific activity of $^{131}\text{I}$ in $\text{Bq/g}$ and $\text{Ci/g}$.
3. Calculate the actual physical mass of $^{131}\text{I}$ administered to the patient in nanograms ($\text{ng}$).""",
                    "solution": r"""### Step 1: Decay Constant $\lambda$
Convert half-life to seconds:
$$T_{1/2} = 8.025\text{ days} \times 86400\text{ s/day} = 693,360\text{ s}$$
$$\lambda = \frac{\ln 2}{T_{1/2}} = \frac{0.693147}{693,360\text{ s}} = 9.9969 \times 10^{-7}\text{ s}^{-1}$$

### Step 2: Specific Activity
Number of atoms per gram:
$$\frac{N_A}{M} = \frac{6.02214 \times 10^{23}}{130.91} = 4.6002 \times 10^{21}\text{ atoms/g}$$
Specific activity in SI:
$$a = \lambda \frac{N_A}{M} = (9.9969 \times 10^{-7}\text{ s}^{-1})(4.6002 \times 10^{21}\text{ g}^{-1}) = 4.5988 \times 10^{15}\text{ Bq/g}$$
In Curies per gram:
$$a_{\text{Ci/g}} = \frac{4.5988 \times 10^{15}\text{ Bq/g}}{3.700 \times 10^{10}\text{ Bq/Ci}} = 124,292\text{ Ci/g} \approx 1.24 \times 10^5\text{ Ci/g}$$

### Step 3: Administered Mass
The prescribed activity is:
$$A = 100\text{ mCi} = 0.100\text{ Ci}$$
The required mass is:
$$m = \frac{A}{a_{\text{Ci/g}}} = \frac{0.100\text{ Ci}}{124,292\text{ Ci/g}} = 8.045 \times 10^{-7}\text{ g} = 804.5\text{ ng}$$
Only **$\sim 805\text{ nanograms}$** of iodine-131 delivers a full therapeutic ablative thyroid radiation dose!""",
                    "hints": ["Always convert time to SI seconds when calculating decay constants.", "1 Ci = 3.7e10 Bq exactly."]
                },
                {
                    "id": "prob-1-5",
                    "problemNumber": "1.5",
                    "title": "Decay Law and Survival Fraction Over Geological Time",
                    "difficulty": "Easy",
                    "statement": r"""Natural uranium contains $^{235}\text{U}$ ($T_{1/2} = 7.04 \times 10^8\text{ yr}$) and $^{238}\text{U}$ ($T_{1/2} = 4.468 \times 10^9\text{ yr}$). 
Assuming the solar system formed $t = 4.54 \times 10^9\text{ years}$ ago with an initial isotopic abundance ratio $N_{235}(0) / N_{238}(0) = 0.300$:
1. Calculate the fraction of the initial $^{235}\text{U}$ and $^{238}\text{U}$ surviving today.
2. Determine the present-day natural isotopic ratio $N_{235}(t) / N_{238}(t)$ and verify against the modern natural abundance of $\approx 0.72\%$.""",
                    "solution": r"""### Step 1: Survival Fractions
1. For $^{238}\text{U}$:
$$\lambda_{238} = \frac{\ln 2}{4.468 \times 10^9\text{ yr}} = 1.55136 \times 10^{-10}\text{ yr}^{-1}$$
$$f_{238} = e^{-\lambda_{238} t} = \exp(-(1.55136 \times 10^{-10})(4.54 \times 10^9)) = e^{-0.70432} \approx 0.4944$$
Approximately **$49.44\%$** of initial $^{238}\text{U}$ remains.

2. For $^{235}\text{U}$:
$$\lambda_{235} = \frac{\ln 2}{7.04 \times 10^8\text{ yr}} = 9.8458 \times 10^{-10}\text{ yr}^{-1}$$
$$f_{235} = e^{-\lambda_{235} t} = \exp(-(9.8458 \times 10^{-10})(4.54 \times 10^9)) = e^{-4.4700} \approx 0.011447$$
Only **$1.145\%$** of primordial $^{235}\text{U}$ has survived!

### Step 2: Present Isotopic Ratio
$$\frac{N_{235}(t)}{N_{238}(t)} = \frac{N_{235}(0)}{N_{238}(0)} \cdot \frac{f_{235}}{f_{238}} = 0.300 \cdot \frac{0.011447}{0.4944} = 0.300 \times 0.023153 = 0.006946 \approx 0.0072$$
Expressed as an abundance percentage:
$$\frac{0.006946}{1 + 0.006946} \times 100\% \approx 0.72\%$$
This matches the known terrestrial isotopic abundance of $^{235}\text{U}$ ($0.720\%$).""",
                    "hints": ["Calculate the exponential decay factor exp(-lambda * t) independently for each isotope.", "Recall that N_235 / N_238 changes over time because lambda_235 > lambda_238."]
                },
                {
                    "id": "prob-1-6",
                    "problemNumber": "1.6",
                    "title": "Alpha Particle Relativistic Kinetic Correction in High-Q Decays",
                    "difficulty": "Intermediate",
                    "statement": r"""The ground-state alpha decay of polonium-212 ($^{212}_{84}\text{Po} \to ^{208}_{82}\text{Pb} + \alpha$) has an exceptional decay energy $Q_\alpha = 8.954\text{ MeV}$.
1. Using non-relativistic conservation of momentum, derive the exact analytical formula for the kinetic energy $T_\alpha$ carried away by the alpha particle in terms of $Q_\alpha$ and daughter mass number $A_D$.
2. Compute $T_\alpha$ and the recoil kinetic energy of the daughter nucleus $^{208}\text{Pb}$.
3. Calculate the relativistic parameter $\beta = v_\alpha / c$ and determine whether relativistic corrections exceed $0.5\%$.""",
                    "solution": r"""### Step 1: Two-Body Kinematics Derivation
In the rest frame of the parent nucleus at rest ($P_{\text{parent}} = 0$):
$$\vec{p}_D + \vec{p}_\alpha = 0 \implies p_D = p_\alpha = p$$
Total decay energy $Q_\alpha$:
$$Q_\alpha = T_\alpha + T_D = \frac{p^2}{2 m_\alpha} + \frac{p^2}{2 M_D} = \frac{p^2}{2 m_\alpha}\left(1 + \frac{m_\alpha}{M_D}\right) = T_\alpha \left(\frac{M_D + m_\alpha}{M_D}\right)$$
Substituting mass numbers $M_D \approx A_D = A - 4$ and $m_\alpha \approx 4$:
$$T_\alpha = Q_\alpha \left(\frac{A_D}{A_D + 4}\right) = Q_\alpha \left(\frac{A - 4}{A}\right)$$
The daughter recoil energy is:
$$T_D = Q_\alpha - T_\alpha = Q_\alpha \left(\frac{4}{A}\right)$$

### Step 2: Numerical Calculation
For $^{212}\text{Po}$, $A = 212$ and $A_D = 208$:
$$T_\alpha = 8.954\text{ MeV} \times \left(\frac{208}{212}\right) = 8.954 \times 0.981132 = 8.785\text{ MeV}$$
The recoil energy of $^{208}\text{Pb}$ is:
$$T_D = 8.954\text{ MeV} - 8.785\text{ MeV} = 0.169\text{ MeV} = 169\text{ keV}$$

### Step 3: Relativistic Velocity $\beta$
The rest mass energy of an alpha particle is:
$$m_\alpha c^2 \approx 3727.38\text{ MeV}$$
The relativistic Lorentz factor is:
$$\gamma = 1 + \frac{T_\alpha}{m_\alpha c^2} = 1 + \frac{8.785}{3727.38} = 1.002357$$
$$\beta = \sqrt{1 - \frac{1}{\gamma^2}} \approx \sqrt{2(\gamma - 1)} = \sqrt{2(0.002357)} = \sqrt{0.004714} \approx 0.0687 \implies v_\alpha \approx 6.87\% \, c$$
Because $\gamma - 1 \approx 0.236\%$, the relativistic kinetic energy correction is well below $0.5\%$, validating classical kinematics.""",
                    "hints": ["Set total momentum to zero: momentum of alpha particle equals momentum of recoil daughter.", "Use the mass fraction (A - 4)/A to partition energy."]
                },
                {
                    "id": "prob-1-7",
                    "problemNumber": "1.7",
                    "title": "Piezoelectric Quartz Electrometer Null-Balance Electrodynamics",
                    "difficulty": "Advanced",
                    "statement": r"""In Marie Curie's electrometer setup, an ionization chamber with volume $V = 1.20\text{ L}$ containing air at STP is exposed to a radium preparation. 
The radiation produces an average ionization rate of $q_0 = 4.50 \times 10^8\text{ ion pairs/s}\cdot\text{cm}^3$.
To balance the electrometer at zero deflection, a weight of mass $m = 2.50\text{ kg}$ is suspended from a piezoelectric quartz blade with piezoelectric coefficient $k_q = 6.00 \times 10^{-11}\text{ C/N}$.
1. Calculate the saturation ionization current $I_{\text{sat}}$ in amperes ($\text{A}$).
2. Determine the time rate of mass unloading $dm/dt$ required to maintain exact null-deflection.""",
                    "solution": r"""### Step 1: Saturation Ionization Current $I_{\text{sat}}$
Volume of chamber:
$$V = 1.20\text{ L} = 1200\text{ cm}^3$$
Total ion pair generation rate:
$$\dot{N} = q_0 V = (4.50 \times 10^8\text{ pairs/s}\cdot\text{cm}^3)(1200\text{ cm}^3) = 5.40 \times 10^{11}\text{ ion pairs/s}$$
Each ion pair carries elementary charge $e = 1.60218 \times 10^{-19}\text{ C}$. In the saturation regime, all created ions are collected before recombination occurs:
$$I_{\text{sat}} = \dot{N} e = (5.40 \times 10^{11}\text{ s}^{-1})(1.60218 \times 10^{-19}\text{ C}) = 8.6518 \times 10^{-8}\text{ A} = 86.5\text{ nA}$$

### Step 2: Null-Balance Piezoelectric Electrodynamics
The piezoelectric charge $Q_p$ generated on the quartz faces by applied gravitational force $F = m g$ is:
$$Q_p = k_q F = k_q m g$$
Differentiating with respect to time to get compensating piezoelectric current $I_p$:
$$I_p = \frac{dQ_p}{dt} = k_q g \frac{dm}{dt}$$
For electrometer null balance, the piezoelectric compensation current must exactly equal the ionization current:
$$I_p = I_{\text{sat}} \implies k_q g \left|\frac{dm}{dt}\right| = I_{\text{sat}}$$
$$\left|\frac{dm}{dt}\right| = \frac{I_{\text{sat}}}{k_q g} = \frac{8.6518 \times 10^{-8}\text{ A}}{(6.00 \times 10^{-11}\text{ C/N})(9.80665\text{ m/s}^2)} = \frac{8.6518 \times 10^{-8}}{5.884 \times 10^{-10}} \approx 147.0\text{ kg/s}$$
Curie used weights on the order of grams producing micro-currents of $10^{-11}\text{ A}$ with smooth unloading mechanisms.""",
                    "hints": ["Saturation current equals total ions generated per second multiplied by elementary charge e.", "Piezoelectric charge generated is directly proportional to applied force F = m*g."]
                }
            ]
        },

        # =====================================================================
        # UNIT 2
        # =====================================================================
        {
            "id": "unit-2-atomic-nucleus-structure-models",
            "unitNumber": 2,
            "title": "Unit 2: Atomic Nucleus: Composition, Binding Energy & Structural Models",
            "leadSummary": "In-depth treatment of nuclear morphology, spatial density distributions, mass defect energetics, the binding energy per nucleon curve, nuclear stability criteria, the Weizsäcker Semi-Empirical Mass Formula, and fundamental structural frameworks including the Nuclear Shell Model, Magic Numbers, and Collective Deformations.",
            "simulations": ["sim_nuc_binding_energy_curve"],
            "sections": [
                {
                    "id": "sec-2-1",
                    "secNumber": "2.1",
                    "title": "Nucleonic Composition & Nuclear Dimensions: Radius Scaling, Density & Charge Distributions",
                    "content": r"""The atomic nucleus is an ultra-dense, quantum many-body system bound by the strong nuclear interaction. It consists of two constituent fermionic species collectively termed **nucleons**:
- **Protons** ($p$): Baryons with positive charge $+e = +1.60217663 \times 10^{-19}\text{ C}$, rest mass $m_p = 1.0072764666\text{ u} = 938.272\text{ MeV}/c^2$, intrinsic spin $s = 1/2$, and isospin projection $T_3 = +1/2$.
- **Neutrons** ($n$): Electrically neutral baryons ($q = 0$), rest mass $m_n = 1.0086649158\text{ u} = 939.565\text{ MeV}/c^2$, intrinsic spin $s = 1/2$, and isospin projection $T_3 = -1/2$.

The composition of any nuclide $^{A}_{Z}\text{X}_N$ is defined by:
- **Atomic number** $Z$: Number of protons.
- **Neutron number** $N$: Number of neutrons.
- **Mass number** $A = Z + N$: Total nucleon count.

### Nuclear Dimensions and Radius Scaling
Because nucleons are subject to the Pauli exclusion principle and the strong nuclear force exhibits a hard repulsive core at inter-nucleon separations $r < 0.5\text{ fm}$ alongside short-range saturation at $r \approx 1.0 - 1.5\text{ fm}$, nuclear matter is essentially **incompressible**.

Consequently, the volume of a nucleus $V$ is directly proportional to the total number of nucleons $A$:
$$V = \frac{4}{3}\pi R^3 \propto A \implies R \propto A^{1/3}$$
The nuclear radius $R$ is parameterized by the foundational empirical scaling law:
$$R = R_0 A^{1/3}$$
where $R_0$ is the nuclear radius parameter.
- High-energy electron scattering measurements (Hofstadter, 1950s) sensitive to the nuclear **charge distribution** yield:
$$R_0 \approx 1.20\text{ to }1.25\text{ fm} \quad (1\text{ fm} = 10^{-15}\text{ m})$$
- Nuclear potential measurements (neutron scattering, alpha decay barriers) yield slightly larger values:
$$R_{0,\text{matter}} \approx 1.4\text{ fm}$$

### Nuclear Density and Incompressibility
Using $R_0 = 1.25\text{ fm} = 1.25 \times 10^{-15}\text{ m}$ and average nucleon mass $m \approx 1.67 \times 10^{-27}\text{ kg}$:
$$\rho_{\text{nuc}} = \frac{M}{V} = \frac{A \cdot m}{\frac{4}{3}\pi R^3} = \frac{A \cdot m}{\frac{4}{3}\pi R_0^3 A} = \frac{3 m}{4\pi R_0^3}$$
Notice that **mass number $A$ cancels out completely**!
$$\rho_{\text{nuc}} = \frac{3 (1.67 \times 10^{-27}\text{ kg})}{4\pi (1.25 \times 10^{-15}\text{ m})^3} \approx 2.04 \times 10^{17}\text{ kg/m}^3 \approx 2 \times 10^{14}\text{ g/cm}^3$$

The nuclear matter nucleon number density $\rho_0$ is:
$$\rho_0 = \frac{3}{4\pi R_0^3} \approx 0.17\text{ nucleons/fm}^3$$
This incredible density—over 200 trillion times denser than liquid water—is uniform across all nuclei from helium to uranium, confirming that nuclear matter behaves like an incompressible quantum liquid drop.

### Woods-Saxon Radial Charge Distribution
High-energy elastic electron scattering demonstrates that nuclei do not possess sharp, hard-sphere boundaries. Instead, the charge density profile $\rho(r)$ is modeled accurately by the **Woods-Saxon (two-parameter Fermi) distribution**:
$$\rho(r) = \frac{\rho_0}{1 + \exp\left(\frac{r - c}{a}\right)}$$
where:
- $\rho_0$ is the central interior nuclear density.
- $c$ is the half-density radius ($c \approx 1.07 A^{1/3}\text{ fm}$), where $\rho(c) = 0.5 \rho_0$.
- $a$ is the surface diffuseness parameter ($a \approx 0.54\text{ fm}$), governing the rate of density falloff.
- The skin thickness $t_{90-10}$, defined as the distance over which the density drops from $90\%$ to $10\%$ of $\rho_0$, is universally:
$$t_{90-10} = 4 a \ln(3) \approx 4.394 a \approx 2.4\text{ fm}$$
across virtually all stable nuclei.""",
                    "simulations": ["sim_nuc_binding_energy_curve"]
                },
                {
                    "id": "sec-2-2",
                    "secNumber": "2.2",
                    "title": "Mass Defect, Einsteinian Equivalence & the Systematics of Binding Energy per Nucleon",
                    "content": r"""One of the most striking findings of precise mass spectrometry (Aston, Bainbridge) is that the precise mass of any bound nucleus $M(A,Z)$ is strictly **less than** the sum of the rest masses of its constituent free protons and neutrons.

### The Mass Defect $\Delta m$
The difference between the total mass of the individual constituent nucleons at infinite separation and the actual bound atomic mass is defined as the **mass defect** $\Delta m$:
$$\Delta m = \left[ Z \cdot m(^1\text{H}) + (A - Z) \cdot m_n \right] - M(A,Z)$$
where:
- $m(^1\text{H}) = 1.007825032\text{ u}$ is the atomic mass of neutral hydrogen-1 (accounting for electron mass $m_e$).
- $m_n = 1.008664916\text{ u}$ is the free neutron mass.
- $M(A,Z)$ is the neutral atomic mass of the nuclide.
- $1\text{ u} \equiv \frac{1}{12} m(^{12}\text{C}) = 1.66053906660 \times 10^{-27}\text{ kg} \equiv 931.49410242\text{ MeV}/c^2$.

### Total Nuclear Binding Energy ($B$)
According to Einstein's mass-energy equivalence principle ($E = mc^2$), this missing mass was liberated as binding energy during the nucleosynthetic coalescence of the nucleus:
$$B(A,Z) = \Delta m \cdot c^2 = \left[ Z m(^1\text{H}) + (A - Z) m_n - M(A,Z) \right] c^2$$

### Binding Energy per Nucleon ($B/A$) Curve Morphology
To compare the relative thermodynamic stability of different nuclear species, we define the **binding energy per nucleon** $B/A$:
$$\frac{B}{A} = \frac{B(A,Z)}{A}$$

```
   B/A (MeV / Nucleon)
 9 ▲              ⁵⁶Fe (8.79 MeV)  ⁶²Ni (8.79 MeV)
   │                 ▲
 8 │     ⁴He        / \_____________
   │      ▲        /                \_______
 7 │     / \      /                         \_____ ²³⁸U (7.57 MeV)
   │    /   \____/                                 \
 6 │   /
 5 │  /      EXOTHERMIC FUSION              EXOTHERMIC FISSION
 4 │ /
 3 │/
 2 │ ²H (1.11 MeV)
 1 │
 0 └──┴───────────┴─────────────────────────┴────────► Mass Number A
      0          56                        238
```

The universal curve of binding energy per nucleon reveals fundamental properties of nuclear forces:
1. **Low Mass Region ($A < 20$)**:
The curve rises steeply from $1.11\text{ MeV/nucleon}$ for deuterium ($^{2}\text{H}$) up to $\approx 8\text{ MeV}$. Prominent periodic spikes appear at $^{4}\text{He}$ ($7.07\text{ MeV}$), $^{8}\text{Be}$, $^{12}\text{C}$ ($7.68\text{ MeV}$), and $^{16}\text{O}$ ($7.98\text{ MeV}$). These peaks reflect the exceptional stability of tightly bound $\alpha$-conjugate nuclei ($Z = N = 2n$).
2. **The Global Peak at $A \approx 56 - 62$**:
The maximum of the curve occurs in the iron-nickel group:
- $^{56}_{26}\text{Fe}$: $B/A = 8.790\text{ MeV/nucleon}$
- $^{62}_{28}\text{Ni}$: $B/A = 8.7946\text{ MeV/nucleon}$ (highest absolute binding energy per nucleon of all known nuclides)
- $^{58}_{26}\text{Fe}$: $B/A = 8.792\text{ MeV/nucleon}$
These nuclides represent the thermodynamically most stable nuclear states in the cosmos ("iron peak" in stellar nucleosynthesis).
3. **High Mass Plateau and Decline ($A > 60$)**:
Beyond iron, the binding energy per nucleon gently and monotonically declines from $\sim 8.8\text{ MeV}$ down to $7.57\text{ MeV/nucleon}$ for uranium-238 ($^{238}\text{U}$). This decline is driven directly by long-range Coulomb electrostatic repulsion between protons, which scales quadratically with $Z^2$ and overcomes the short-range strong nuclear attraction.
4. **Thermodynamic Implications for Nuclear Energy**:
- **Nuclear Fusion**: Coalescing light nuclei ($A < 56$, e.g., $^2\text{H} + ^3\text{H} \to ^4\text{He} + n$) moves upward along the curve toward higher $B/A$, releasing millions of electron volts per reaction.
- **Nuclear Fission**: Splitting heavy nuclei ($A > 200$, e.g., $n + ^{235}\text{U} \to \text{Ba} + \text{Kr} + 3n$) breaks a less tightly bound nucleus ($7.6\text{ MeV/nucleon}$) into two intermediate fragments ($8.5\text{ MeV/nucleon}$), releasing $\approx 0.9\text{ MeV/nucleon} \times 235 \approx 200\text{ MeV}$ of net kinetic energy per fission.""",
                    "simulations": ["sim_nuc_binding_energy_curve"]
                },
                {
                    "id": "sec-2-3",
                    "secNumber": "2.3",
                    "title": "The Nuclear Valley of Beta-Stability: N/Z Ratios, Neutron Driplines & Proton Driplines",
                    "content": r"""If we plot all known nuclides on a Segrè chart (the chart of nuclides) with proton number $Z$ on the ordinate and neutron number $N$ on the abscissa, stable nuclei form a narrow ribbon termed the **valley of beta-stability**.

```
   Z (Proton Number)
92 ▲                                   / N = Z line
   │                                 /
82 │ Pb                            /
   │                             /  Valley of Beta Stability
   │                           /  (N > Z for heavy nuclei)
   │                         /•
40 │ Zr                    /••
   │                     /••
20 │ Ca                /•••  (N ≈ Z for light nuclei)
   │                /••••
   │              /••••
   └────────────┴──────────────────────────► N (Neutron Number)
   0           20   40        82       126
```

### The $N/Z$ Ratio Trajectory
1. **Light Stable Nuclei ($Z \le 20$)**:
For light nuclei, the valley follows the line of symmetry $N = Z$ ($N/Z \approx 1.0$). Examples include $^{4}_{2}\text{He}$, $^{12}_{6}\text{C}$, $^{14}_{7}\text{N}$, $^{16}_{8}\text{O}$, $^{20}_{10}\text{Ne}$, $^{28}_{14}\text{Si}$, and $^{40}_{20}\text{Ca}$. This symmetry arises from the Pauli exclusion principle, which penalizes unequal filling of neutron and proton quantum energy levels.
2. **Heavy Stable Nuclei ($Z > 20$)**:
As $Z$ increases, Coulomb repulsion among protons scales as $Z(Z-1)/R \propto Z^2 / A^{1/3}$. To maintain binding against this disruptive force, the nucleus must incorporate an increasing excess of neutrons, which supply attractive strong nuclear force without adding disruptive electrostatic charge. Consequently, the $N/Z$ ratio increases monotonically:
- Iron-56: $^{56}_{26}\text{Fe}_{30} \implies N/Z = 30/26 \approx 1.15$
- Silver-107: $^{107}_{47}\text{Ag}_{60} \implies N/Z = 60/47 \approx 1.28$
- Lead-208: $^{208}_{82}\text{Pb}_{126} \implies N/Z = 126/82 \approx 1.54$
- Uranium-238: $^{238}_{92}\text{U}_{146} \implies N/Z = 146/92 \approx 1.59$

### Nuclear Decay Modes Relative to the Valley of Stability
Nuclides lying off the central floor of the valley undergo spontaneous radioactive transitions to reach stability:
- **Neutron-Rich Nuclides** (Lying below/to the right of the valley):
Excess neutrons result in negative beta decay ($\beta^-$) where a neutron converts to a proton:
$$n \longrightarrow p + e^- + \bar{\nu}_e \quad (\Delta Z = +1, \Delta N = -1, A = \text{constant})$$
For extreme neutron excess, prompt neutron emission ($S_n \le 0$) defines the **neutron dripline**.
- **Proton-Rich Nuclides** (Lying above/to the left of the valley):
Excess protons result in positron emission ($\beta^+$) or electron capture (EC):
$$p \longrightarrow n + e^+ + \nu_e \quad (\Delta Z = -1, \Delta N = +1, A = \text{constant})$$
$$p + e^- \longrightarrow n + \nu_e$$
For extreme proton excess, proton emission ($S_p \le 0$) defines the **proton dripline**.
- **Superheavy Unstable Nuclides ($Z > 82, A > 209$)**:
Coulomb repulsion is so massive that beta decay cannot stabilize the nucleus; alpha decay ($\Delta Z = -2, \Delta A = -4$) and spontaneous fission become dominant. The heaviest completely stable nuclide is **lead-208** ($^{208}_{82}\text{Pb}$). Bismuth-209 is very weakly alpha active ($T_{1/2} = 2.01 \times 10^{19}\text{ yr}$).

### Even-Odd Nuclear Stability Systematics
The pairing interaction in nuclear forces produces dramatic patterns in stable isotope abundances:

| Nucleus Type | $Z$ | $N$ | Number of Stable Nuclides | Average Stable Isotopes per Element | Examples |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Even-Even** | Even | Even | **166** | $\sim 5.5$ | $^{12}\text{C}, ^{16}\text{O}, ^{56}\text{Fe}, ^{208}\text{Pb}$ |
| **Even-Odd** | Even | Odd | **57** | $\sim 1.4$ | $^{13}\text{C}, ^{57}\text{Fe}, ^{207}\text{Pb}$ |
| **Odd-Even** | Odd | Even | **53** | $\sim 1.3$ | $^{19}\text{F}, ^{23}\text{Na}, ^{63}\text{Cu}$ |
| **Odd-Odd** | Odd | Odd | **9** (only 4 stable light) | $< 0.1$ | $^{2}\text{H}, ^{6}\text{Li}, ^{10}\text{B}, ^{14}\text{N}$ ($^{50}\text{V}, ^{138}\text{La}, ^{180m}\text{Ta}$) |

Over $60\%$ of all stable nuclides in the universe are **even-even**, while only four completely stable odd-odd nuclides exist in nature ($^{2}\text{H}, ^{6}\text{Li}, ^{10}\text{B}, ^{14}\text{N}$). This disparity provides direct evidence that nucleons of identical species couple into anti-parallel pairs ($J^\pi = 0^+$) with enhanced binding energy.""",
                    "simulations": ["sim_nuc_binding_energy_curve"]
                },
                {
                    "id": "sec-2-4",
                    "secNumber": "2.4",
                    "title": "Nuclear Taxonomy: Isotopes, Isobars, Isotones, Nuclear Isomers & Mirror Nuclei",
                    "content": r"""Nuclear species (nuclides) are classified into specific families based on relationships between their proton count $Z$, neutron count $N$, and total mass number $A$.

### 1. Isotopes ($\Delta Z = 0$)
Nuclides possessing the **same atomic number $Z$** (identical chemical identity) but differing neutron numbers $N$ and mass numbers $A$.
- Examples: 
  - Hydrogen isotopes: $^{1}_{1}\text{H}$ (protium), $^{2}_{1}\text{H}$ (deuterium), $^{3}_{1}\text{H}$ (tritium).
  - Uranium isotopes: $^{234}_{92}\text{U}$, $^{235}_{92}\text{U}$, $^{238}_{92}\text{U}$.
- Because their electron configurations are identical, isotopes exhibit nearly identical chemical properties (governed by the same electron shell structure), but display distinct nuclear properties (spins, magnetic moments, cross sections, decay half-lives).

### 2. Isobars ($\Delta A = 0$)
Nuclides possessing the **same total mass number $A$** but differing atomic numbers $Z$ and neutron numbers $N$.
- Examples: 
  - $A = 14$: $^{14}_{6}\text{C}$, $^{14}_{7}\text{N}$, $^{14}_{8}\text{O}$.
  - $A = 40$: $^{40}_{18}\text{Ar}$, $^{40}_{19}\text{K}$, $^{40}_{20}\text{Ca}$.
- Isobars possess completely different chemical identities. In any isobaric chain, **Mattauch's Isobar Rule** states that two neighboring stable isobars ($\Delta Z = 1$) cannot exist; one must beta decay into the other.

### 3. Isotones ($\Delta N = 0$)
Nuclides possessing the **same neutron number $N$** but differing atomic numbers $Z$ and mass numbers $A$.
- Examples ($N = 82$, magic neutron shell):
  - $^{138}_{56}\text{Ba}_{82}$, $^{139}_{57}\text{La}_{82}$, $^{140}_{58}\text{Ce}_{82}$, $^{141}_{59}\text{Pr}_{82}$, $^{142}_{60}\text{Nd}_{82}$.
- Isotones are invaluable in nuclear structure research because variations in binding energy and excitation spectra reflect changes in proton configuration against an identical neutron core.

### 4. Nuclear Isomers
Nuclides possessing the **identical $Z$ and identical $A$** that exist in different, long-lived metastable nuclear energy states (isomeric states, denoted with an "m", e.g., $^{99m}\text{Tc}$, $^{180m}\text{Ta}$).
- A metastable excited state arises when the angular momentum difference $\Delta I$ between the excited isomer and the lower state is large (high multipolarity, e.g., $E4$ or $M4$) and the transition energy $\Delta E$ is low, severely suppressing the probability of gamma electromagnetic de-excitation (isomeric transition, IT).
- Example: Technetium-99m ($^{99m}_{43}\text{Tc}$):
  The $142.6\text{ keV}$ state has spin-parity $1/2^-$ while the ground state $^{99}\text{Tc}$ has $9/2^+$. The large spin change $\Delta I = 4$ produces an exceptionally long half-life of $T_{1/2} = 6.01\text{ hours}$, making it the premier radiotracer in nuclear medicine.
- Tantalum-180m ($^{180m}_{73}\text{Ta}$, $I^\pi = 9^-$) has a half-life exceeding $4.5 \times 10^{16}\text{ years}$—longer than the age of the universe!

### 5. Mirror Nuclei
A pair of isobaric nuclei ($A_1 = A_2$) where the proton count of one equals the neutron count of the other:
$$Z_1 = N_2 \quad \text{and} \quad N_1 = Z_2 \implies |Z_1 - Z_2| = 1$$
- Examples: $(^3_1\text{H}, ^3_2\text{He})$, $(^7_3\text{Li}, ^7_4\text{Be})$, $(^{11}_5\text{B}, ^{11}_6\text{C})$, $(^{15}_7\text{N}, ^{15}_8\text{O})$.
- Because the strong nuclear interaction is **charge-symmetric** (the $p-p$, $n-n$, and $p-n$ strong potentials are identical in the same quantum state), the binding energy difference between mirror nuclei is due almost exclusively to the difference in **Coulomb electrostatic self-energy**:
$$\Delta E_C = B(Z_1, N_1) - B(Z_2, N_2) \approx \frac{3}{5}\frac{e^2}{4\pi\varepsilon_0 R} \left[ Z_2(Z_2 - 1) - Z_1(Z_1 - 1) \right]$$
Measuring this mass difference enables precise experimental determination of the nuclear charge radius $R_0$.""",
                    "simulations": ["sim_nuc_binding_energy_curve"]
                },
                {
                    "id": "sec-2-5",
                    "secNumber": "2.5",
                    "title": "The Liquid Drop Model & Weizsäcker Semi-Empirical Mass Formula (SEMF)",
                    "content": r"""In 1935, Carl Friedrich von Weizsäcker developed the **Liquid Drop Model**, analogizing the atomic nucleus to a macroscopic droplet of incompressible charged liquid. Nucleons interact through short-range, saturating attractive strong forces analogous to van der Waals forces in a liquid, counteracted by long-range electrostatic repulsion between protons.

The resulting **Semi-Empirical Mass Formula (SEMF)** provides an analytical formulation for total binding energy $B(A,Z)$:
$$B(A,Z) = a_v A - a_s A^{2/3} - a_c \frac{Z(Z - 1)}{A^{1/3}} - a_a \frac{(A - 2Z)^2}{A} + \delta(A,Z)$$

```
      SEMF Binding Energy Components
  B(A,Z) = + Volume Term        [+ a_v * A]
           - Surface Term       [- a_s * A^(2/3)]
           - Coulomb Term       [- a_c * Z(Z-1) / A^(1/3)]
           - Asymmetry Term     [- a_a * (A - 2Z)^2 / A]
           + Pairing Term       [+ δ(A,Z)]
```

### Physical Derivation of the Five Terms

1. **Volume Energy Term ($+a_v A$)**:
Because the strong nuclear force is short-ranged and exhibits saturation, each interior nucleon interacts only with its immediate nearest neighbors ($\sim 12$ nucleons), contributing a constant binding energy independent of total drop size:
$$B_{\text{volume}} = +a_v A \quad (a_v \approx 15.75\text{ MeV})$$

2. **Surface Energy Term ($-a_s A^{2/3}$)**:
Nucleons residing on the nuclear surface have fewer neighboring nucleons than those in the interior, reducing the net binding. By analogy with surface tension in liquids, this deficit is proportional to the surface area of the sphere:
$$\text{Area} = 4\pi R^2 = 4\pi (R_0 A^{1/3})^2 \propto A^{2/3}$$
$$B_{\text{surface}} = -a_s A^{2/3} \quad (a_s \approx 17.80\text{ MeV})$$

3. **Coulomb Repulsion Term ($-a_c Z(Z-1)/A^{1/3}$)**:
The $Z$ protons uniformly distributed throughout the nuclear sphere repel each other electrostatically. The classical self-energy of a uniformly charged sphere of radius $R$ is:
$$E_C = \frac{3}{5}\frac{Q^2}{4\pi\varepsilon_0 R} = \frac{3}{5}\frac{(Z e)^2}{4\pi\varepsilon_0 R_0 A^{1/3}}$$
Correcting for quantum self-interaction (a proton does not repel itself, yielding $Z(Z-1)$ pairs):
$$B_{\text{Coulomb}} = -a_c \frac{Z(Z - 1)}{A^{1/3}} \quad \text{where } a_c = \frac{3}{5}\frac{e^2}{4\pi\varepsilon_0 R_0} \approx 0.711\text{ MeV}$$

4. **Asymmetry Energy Term ($-a_a (A - 2Z)^2 / A$)**:
Quantum mechanics (Pauli exclusion principle) dictates that protons and neutrons fill separate fermion energy wells. For a fixed total nucleon count $A$, the state of lowest total kinetic energy occurs when $N = Z = A/2$.
Any neutron excess $(N - Z) = (A - 2Z)$ forces nucleons into higher unoccupied quantum states. In a Fermi gas approximation, expanding the energy difference in powers of $(N - Z)$:
$$B_{\text{asymmetry}} = -a_a \frac{(A - 2Z)^2}{A} \quad (a_a \approx 23.70\text{ MeV})$$

5. **Pairing Energy Term ($\delta(A,Z)$)**:
Due to the spin-orbit pairing force, identical nucleons with antiparallel spins form pairs ($J^\pi = 0^+$) with enhanced binding energy. The pairing term is:
$$\delta(A,Z) = \begin{cases} +\frac{a_p}{A^{1/2}} & \text{for Even-Even nuclei (extra stable)} \\ 0 & \text{for Even-Odd / Odd-Even nuclei} \\ -\frac{a_p}{A^{1/2}} & \text{for Odd-Odd nuclei (least stable)} \end{cases}$$
where $a_p \approx 11.18\text{ MeV}$ (or alternatively parameterized as $a_p / A^{3/4}$).

### Prediction of the Most Stable Isobar ($Z_{\text{stable}}$)
For a constant mass number $A$, the binding energy is a quadratic parabola in $Z$:
$$\frac{\partial B(A,Z)}{\partial Z} = 0 \implies \frac{\partial}{\partial Z}\left[ -a_c \frac{Z(Z-1)}{A^{1/3}} - a_a \frac{(A - 2Z)^2}{A} \right] = 0$$
Evaluating the derivative:
$$- \frac{a_c}{A^{1/3}}(2Z - 1) - \frac{a_a}{A}[-4(A - 2Z)] = 0$$
$$\frac{a_c}{A^{1/3}}(2Z) + \frac{8 a_a Z}{A} = 4 a_a + \frac{a_c}{A^{1/3}}$$
Neglecting small terms, we solve for $Z_{\text{stable}}$:
$$Z_{\text{stable}} = \frac{A}{2 + \frac{a_c}{2 a_a} A^{2/3}} \approx \frac{A}{2 + 0.015 A^{2/3}}$$
- For light nuclei ($A \to 0$): $Z_{\text{stable}} \to A/2$ ($N = Z$).
- For heavy nuclei ($A = 208$): $Z_{\text{stable}} = \frac{208}{2 + 0.015(208)^{2/3}} = \frac{208}{2 + 0.015(35.1)} = \frac{208}{2.527} \approx 82.3 \implies Z = 82$ (Lead-208), in remarkable agreement with experiment!""",
                    "simulations": ["sim_nuc_binding_energy_curve"]
                },
                {
                    "id": "sec-2-6",
                    "secNumber": "2.6",
                    "title": "The Nuclear Shell Model: Spin-Orbit Coupling, Magic Numbers & Single-Particle States",
                    "content": r"""While the Liquid Drop Model explains macroscopic binding energies and fission, it completely fails to explain quantum micro-structure:
1. Exceptional binding energy spikes at specific proton or neutron counts:
$$\mathbf{2, \; 8, \; 20, \; 28, \; 50, \; 82, \; 126} \quad \text{("Magic Numbers")}$$
2. Nuclei with magic numbers of nucleons (such as $^{4}_{2}\text{He}_2$, $^{16}_{8}\text{O}_8$, $^{40}_{20}\text{Ca}_{20}$, $^{48}_{20}\text{Ca}_{28}$, $^{208}_{82}\text{Pb}_{126}$) are "doubly magic" and possess zero electric quadrupole moments, exceptionally high first-excited state energies, and extraordinarily small neutron capture cross sections.
3. Ground-state nuclear spins and parities ($J^\pi$) and magnetic dipole moments.

### The Shell Model Potential and Mayer-Jensen Spin-Orbit Coupling
In 1949, Maria Goeppert Mayer and J. Hans D. Jensen independently recognized that nucleons move in a mean central potential created by all other nucleons, accompanied by an extraordinarily strong **spin-orbit interaction** ($\vec{l}\cdot\vec{s}$ coupling):
$$V(r) = V_{\text{central}}(r) + V_{ls}(r) \, (\vec{l} \cdot \vec{s})$$

### Mathematical Derivation of Spin-Orbit Level Splitting
For a nucleon with orbital angular momentum $\vec{l}$ and spin $\vec{s}$ ($s = 1/2$), the total single-particle angular momentum is:
$$\vec{j} = \vec{l} + \vec{s} \implies j = l + \frac{1}{2} \quad \text{or} \quad j = l - \frac{1}{2}$$
Squaring $\vec{j}$:
$$\vec{j}^2 = (\vec{l} + \vec{s})^2 = \vec{l}^2 + \vec{s}^2 + 2 (\vec{l} \cdot \vec{s})$$
$$\vec{l} \cdot \vec{s} = \frac{1}{2}\left( \vec{j}^2 - \vec{l}^2 - \vec{s}^2 \right)$$
Evaluating the quantum expectation values:
$$\langle \vec{l} \cdot \vec{s} \rangle = \frac{\hbar^2}{2} [ j(j + 1) - l(l + 1) - s(s + 1) ]$$
With $s = 1/2 \implies s(s+1) = 3/4$:
1. For state with $j = l + 1/2$:
$$\langle \vec{l} \cdot \vec{s} \rangle = \frac{\hbar^2}{2} \left[ (l + 1/2)(l + 3/2) - l(l + 1) - 3/4 \right] = \frac{\hbar^2}{2} [l^2 + 2l + 3/4 - l^2 - l - 3/4] = +\frac{l}{2}\hbar^2$$
2. For state with $j = l - 1/2$:
$$\langle \vec{l} \cdot \vec{s} \rangle = \frac{\hbar^2}{2} \left[ (l - 1/2)(l + 1/2) - l(l + 1) - 3/4 \right] = \frac{\hbar^2}{2} [l^2 - 1/4 - l^2 - l - 3/4] = -\frac{l + 1}{2}\hbar^2$$

The energy splitting between the two sub-states is:
$$\Delta E_{ls} = \langle V_{ls} \rangle \left[ \frac{l}{2} - \left(-\frac{l+1}{2}\right) \right] = \langle V_{ls} \rangle \left(l + \frac{1}{2}\right)\hbar^2$$

Crucially, in the nuclear interaction (unlike atomic atomic fine structure), the spin-orbit potential $V_{ls}(r)$ is **negative**. 
Therefore, the state with **higher total angular momentum $j = l + 1/2$ is pushed downward in energy**, while $j = l - 1/2$ is pushed upward!

```
 Harmonic Oscillator    With Spin-Orbit Splitting     Magic Shell
       Levels                   (V_ls < 0)               Closure
 ────────────────────────────────────────────────────────────────
        1f (l=3) ────────── 1f_5/2 (6 states) ─────── 
                 \
                  \──────── 1f_7/2 (8 states) ─────── ► [28] MAGIC
 ────────────────────────────────────────────────────────────────
        1d (l=2) ────────── 1d_3/2 (4 states) ─────── ► [20] MAGIC
        2s (l=0) ────────── 2s_1/2 (2 states)
        1d (l=2) ────────── 1d_5/2 (6 states)
 ────────────────────────────────────────────────────────────────
        1p (l=1) ────────── 1p_1/2 (2 states) ─────── ► [8] MAGIC
                 ────────── 1p_3/2 (4 states)
 ────────────────────────────────────────────────────────────────
        1s (l=0) ────────── 1s_1/2 (2 states) ─────── ► [2] MAGIC
```

For large orbital angular momentum $l$ ($l = 3$ for $f$-states, $l = 4$ for $g$-states), this downward shift is so massive that the $j = l + 1/2$ level drops completely across the oscillator gap into the major shell below. This accounts for every observed magic number:
- $1s_{1/2}$ (capacity 2) $\implies \mathbf{2}$
- $1p_{3/2}, 1p_{1/2}$ (capacity $4 + 2 = 6$) $\implies 2 + 6 = \mathbf{8}$
- $1d_{5/2}, 2s_{1/2}, 1d_{3/2}$ (capacity $6 + 2 + 4 = 12$) $\implies 8 + 12 = \mathbf{20}$
- Intruder state $1f_{7/2}$ pushed down (capacity 8) $\implies 20 + 8 = \mathbf{28}$
- $2p_{3/2}, 1f_{5/2}, 2p_{1/2}$ plus intruder $1g_{9/2}$ (capacity 22) $\implies 28 + 22 = \mathbf{50}$
- $2d_{5/2}, 1g_{7/2}, 1h_{11/2}$, etc. $\implies \mathbf{82}$
- Intruder $1i_{13/2}$, etc. $\implies \mathbf{126}$""",
                    "simulations": ["sim_nuc_binding_energy_curve"]
                },
                {
                    "id": "sec-2-7",
                    "secNumber": "2.7",
                    "title": "Collective & Statistical Nuclear Models: Bohr-Mottelson Deformations & the Fermi Gas Model",
                    "content": r"""The spherical Shell Model succeeds near magic numbers, but fails in the mid-shell regions ($150 < A < 190$ and $A > 220$). In these regions, nuclei exhibit:
- Electric quadrupole moments $Q_0$ up to 30 times larger than the single-particle limit.
- Rotational band excitation spectra following exact $E_J \propto J(J+1)$ sequences.
- Strongly enhanced collective electric quadrupole transition rates $B(E2)$.

### The Bohr-Mottelson Unified Collective Model (1953)
Aage Bohr, Ben Mottelson, and James Rainwater resolved this disparity by modeling the nucleus as a deformed, non-spherical liquid drop whose collective surface vibrations and rotations couple to individual valence nucleon orbits.

The deformed nuclear surface is parameterized via spherical harmonics $Y_{\lambda \mu}(\theta, \phi)$:
$$R(\theta, \phi) = R_0 \left[ 1 + \sum_{\lambda=2}^{\infty} \sum_{\mu=-\lambda}^{\lambda} \alpha_{\lambda \mu} Y_{\lambda \mu}^*(\theta, \phi) \right]$$
For axially symmetric quadrupole deformations ($\lambda = 2, \mu = 0$), this simplifies in terms of the deformation parameter $\beta$:
$$R(\theta) = R_0 \left[ 1 + \beta \sqrt{\frac{5}{16\pi}} (3\cos^2\theta - 1) \right] = R_0 [ 1 + \beta Y_{20}(\theta) ]$$
- $\beta > 0$: **Prolate spheroid** (cigar-shaped, major axis along symmetry axis; predominant in nature).
- $\beta < 0$: **Oblate spheroid** (doorknob / disk-shaped).

### Rotational Energy Spectra
For an even-even deformed nucleus with ground state $J^\pi = 0^+$, quantum rotation of the collective core about an axis perpendicular to the symmetry axis yields kinetic rotational energy:
$$E_{\text{rot}}(J) = \frac{\hbar^2}{2 \mathcal{I}} J(J + 1), \quad J = 0, 2, 4, 6, 8, \dots$$
where $\mathcal{I}$ is the effective moment of inertia of the deformed nucleus.
The excitation energy ratios in a pure rotational band follow:
$$\frac{E(4^+)}{E(2^+)} = \frac{4(5)}{2(3)} = \frac{20}{6} = 3.333$$
$$\frac{E(6^+)}{E(2^+)} = \frac{6(7)}{6} = 7.000, \quad \frac{E(8^+)}{E(2^+)} = \frac{8(9)}{6} = 12.000$$
Experimental spectra for deformed nuclei (e.g., $^{160}\text{Gd}, ^{174}\text{Yb}, ^{238}\text{U}$) match this $3.33$ ratio precisely, confirming collective rotation.

### The Fermi Gas Model of Nuclear Matter
For high-energy nuclear reactions and statistical level densities, the nucleus is treated as a degenerate quantum gas of non-interacting fermions (protons and neutrons) confined within a spherical volume $V = \frac{4}{3}\pi R^3$.

The number of spatial momentum states in phase space volume $d^3r \, d^3p$ is:
$$dN = \frac{2}{(2\pi\hbar)^3} d^3r \, d^3p = \frac{2 V}{(2\pi\hbar)^3} 4\pi p^2 dp$$
where the factor 2 accounts for spin degeneracy ($s_z = \pm 1/2$).
Integrating from $p = 0$ to the **Fermi momentum** $p_F$:
$$N = \frac{8\pi V}{(2\pi\hbar)^3} \int_0^{p_F} p^2 dp = \frac{8\pi V}{(2\pi\hbar)^3} \frac{p_F^3}{3} = \frac{V p_F^3}{3\pi^2 \hbar^3}$$
Substituting nuclear matter density $\rho = N / V$:
$$p_F = \hbar (3\pi^2 \rho)^{1/3} \implies k_F = (3\pi^2 \rho)^{1/3}$$
For symmetric nuclear matter ($N = Z = A/2$) with $\rho_0 \approx 0.17\text{ fm}^{-3}$:
$$k_F = \left( 3\pi^2 \cdot \frac{0.17}{2} \right)^{1/3} \approx 1.36\text{ fm}^{-1}$$
The **Fermi Energy** $E_F$ of a nucleon is:
$$E_F = \frac{p_F^2}{2 m_N} = \frac{\hbar^2 k_F^2}{2 m_N} = \frac{(197.3\text{ MeV}\cdot\text{fm})^2 (1.36\text{ fm}^{-1})^2}{2 (938\text{ MeV})} \approx 38.4\text{ MeV}$$
The average kinetic energy per nucleon in the ground state is:
$$\langle T \rangle = \frac{\int_0^{E_F} E \cdot g(E) dE}{\int_0^{E_F} g(E) dE} = \frac{3}{5} E_F \approx \frac{3}{5}(38.4\text{ MeV}) \approx 23.0\text{ MeV}$$
Adding the average nucleon binding energy ($B/A \approx 8\text{ MeV}$), the total depth of the nuclear potential well is:
$$V_0 = E_F + B/A \approx 38.4 + 8.0 \approx 46 - 50\text{ MeV}$$""",
                    "simulations": ["sim_nuc_binding_energy_curve"]
                }
            ],
            "problems": [
                {
                    "id": "prob-2-1",
                    "problemNumber": "2.1",
                    "title": "Nuclear Matter Density and Radius of Lead-208",
                    "difficulty": "Easy",
                    "statement": r"""Given the nuclear radius constant $R_0 = 1.25\text{ fm}$:
1. Calculate the charge radius $R$ of the doubly magic nucleus lead-208 ($^{208}_{82}\text{Pb}$).
2. Determine the nuclear mass density of $^{208}\text{Pb}$ in $\text{kg/m}^3$ assuming a uniform sphere with atomic mass $M = 207.97665\text{ u}$.""",
                    "solution": r"""### Step 1: Nuclear Radius
Using the radius scaling law $R = R_0 A^{1/3}$:
$$A = 208 \implies A^{1/3} = (208)^{1/3} \approx 5.9250$$
$$R = 1.25\text{ fm} \times 5.9250 \approx 7.406\text{ fm} = 7.406 \times 10^{-15}\text{ m}$$

### Step 2: Mass Density $\rho$
Volume of the nuclear sphere:
$$V = \frac{4}{3}\pi R^3 = \frac{4}{3}\pi (7.406 \times 10^{-15}\text{ m})^3 = \frac{4}{3}\pi (4.062 \times 10^{-43}) \approx 1.7015 \times 10^{-42}\text{ m}^3$$
Total nuclear mass in kilograms:
$$M = 207.97665\text{ u} \times 1.66054 \times 10^{-27}\text{ kg/u} \approx 3.4535 \times 10^{-25}\text{ kg}$$
Density:
$$\rho = \frac{M}{V} = \frac{3.4535 \times 10^{-25}\text{ kg}}{1.7015 \times 10^{-42}\text{ m}^3} \approx 2.03 \times 10^{17}\text{ kg/m}^3$$
The density is $\approx 2.0 \times 10^{14}\text{ g/cm}^3$ (200 million metric tons per cubic centimeter).""",
                    "hints": ["Use R = R_0 * A^(1/3).", "Convert mass from atomic mass units (u) to kilograms using 1 u = 1.66054e-27 kg."]
                },
                {
                    "id": "prob-2-2",
                    "problemNumber": "2.2",
                    "title": "Exact Binding Energy and Energy Release in Deuteron Fusion",
                    "difficulty": "Easy",
                    "statement": r"""Consider the fusion reaction between two deuterons:
$$^2_1\text{H} + ^2_1\text{H} \longrightarrow ^4_2\text{He} + \Delta E$$
Given the atomic masses:
- $m(^2_1\text{H}) = 2.01410178\text{ u}$
- $m(^4_2\text{He}) = 4.00260325\text{ u}$
- $1\text{ u} = 931.4941\text{ MeV}/c^2$
1. Calculate the binding energy per nucleon of $^2\text{H}$ and $^4\text{He}$.
2. Calculate the total energy released $\Delta E$ in $\text{MeV}$ per fusion reaction and per gram of deuterium fuel.""",
                    "solution": r"""### Step 1: Binding Energy per Nucleon
1. For Deuterium ($^2\text{H}$, $Z = 1, N = 1$):
$$\Delta m(^2\text{H}) = m(^1\text{H}) + m_n - m(^2\text{H}) = 1.00782503 + 1.00866492 - 2.01410178 = 0.00238817\text{ u}$$
$$B(^2\text{H}) = 0.00238817 \times 931.4941\text{ MeV} = 2.2246\text{ MeV}$$
$$\frac{B}{A}(^2\text{H}) = \frac{2.2246\text{ MeV}}{2} = 1.1123\text{ MeV/nucleon}$$

2. For Helium-4 ($^4\text{He}$, $Z = 2, N = 2$):
$$\Delta m(^4\text{He}) = 2(1.00782503) + 2(1.00866492) - 4.00260325 = 2.01565006 + 2.01732984 - 4.00260325 = 0.03037665\text{ u}$$
$$B(^4\text{He}) = 0.03037665 \times 931.4941\text{ MeV} = 28.2957\text{ MeV}$$
$$\frac{B}{A}(^4\text{He}) = \frac{28.2957\text{ MeV}}{4} = 7.0739\text{ MeV/nucleon}$$

### Step 2: Energy Release $\Delta E$
$$\Delta m = 2 m(^2\text{H}) - m(^4\text{He}) = 2(2.01410178) - 4.00260325 = 4.02820356 - 4.00260325 = 0.02560031\text{ u}$$
$$\Delta E = 0.02560031 \times 931.4941\text{ MeV} = 23.8465\text{ MeV}$$
Alternatively: $\Delta E = B(^4\text{He}) - 2 B(^2\text{H}) = 28.2957 - 2(2.2246) = 23.8465\text{ MeV}$.

### Energy Per Gram of Deuterium:
Two deuterons ($M \approx 4.028\text{ g/mol}$) release $23.85\text{ MeV}$:
$$\text{Specific Energy} = \frac{23.8465 \times 1.60218 \times 10^{-13}\text{ J}}{2 \times 2.0141 \times 1.66054 \times 10^{-24}\text{ g}} = \frac{3.8206 \times 10^{-12}\text{ J}}{6.688 \times 10^{-24}\text{ g}} \approx 5.71 \times 10^{11}\text{ J/g} = 571\text{ GJ/g}$$
One gram of deuterium yields energy equivalent to combusting over 13 metric tons of oil!""",
                    "hints": ["Mass defect uses neutral atomic masses because electron masses cancel exactly.", "Energy release equals difference in binding energies: B(products) - B(reactants)."]
                },
                {
                    "id": "prob-2-3",
                    "problemNumber": "2.3",
                    "title": "Semi-Empirical Mass Formula Calculation of Iron-56 Binding Energy",
                    "difficulty": "Intermediate",
                    "statement": r"""Using the Weizsäcker Semi-Empirical Mass Formula with parameters:
$a_v = 15.75\text{ MeV}$, $a_s = 17.80\text{ MeV}$, $a_c = 0.711\text{ MeV}$, $a_a = 23.70\text{ MeV}$, and $a_p = 11.18\text{ MeV}$ (with $\delta = +a_p / A^{1/2}$ for even-even):
1. Compute each of the five individual energetic terms for iron-56 ($^{56}_{26}\text{Fe}$, $Z = 26, N = 30$).
2. Calculate the total binding energy $B$ and binding energy per nucleon $B/A$.
3. Compare with the experimental value of $8.790\text{ MeV/nucleon}$ and calculate the percentage discrepancy.""",
                    "solution": r"""### Step 1: Compute Individual SEMF Terms for $^{56}_{26}\text{Fe}$
Here $A = 56$, $Z = 26$, $N = 30$.
- $A^{1/3} = (56)^{1/3} \approx 3.82586$
- $A^{2/3} = (3.82586)^2 \approx 14.6372$
- $A^{1/2} = \sqrt{56} \approx 7.4833$

1. **Volume Term**:
$$B_{\text{vol}} = a_v A = 15.75 \times 56 = +882.000\text{ MeV}$$

2. **Surface Term**:
$$B_{\text{surf}} = -a_s A^{2/3} = -17.80 \times 14.6372 = -260.542\text{ MeV}$$

3. **Coulomb Term**:
$$B_{\text{coul}} = -a_c \frac{Z(Z-1)}{A^{1/3}} = -0.711 \times \frac{26 \times 25}{3.82586} = -0.711 \times \frac{650}{3.82586} = -0.711 \times 169.896 = -120.796\text{ MeV}$$

4. **Asymmetry Term**:
$$A - 2Z = 56 - 52 = 4$$
$$B_{\text{asym}} = -a_a \frac{(A - 2Z)^2}{A} = -23.70 \times \frac{4^2}{56} = -23.70 \times \frac{16}{56} = -23.70 \times 0.285714 = -6.771\text{ MeV}$$

5. **Pairing Term**:
Since $Z = 26$ (even) and $N = 30$ (even), the nucleus is even-even ($\delta > 0$):
$$B_{\text{pair}} = +\frac{a_p}{A^{1/2}} = +\frac{11.18}{7.4833} = +1.494\text{ MeV}$$

### Step 2: Total Binding Energy and $B/A$
$$B = 882.000 - 260.542 - 120.796 - 6.771 + 1.494 = 495.385\text{ MeV}$$
$$\frac{B}{A} = \frac{495.385\text{ MeV}}{56} \approx 8.846\text{ MeV/nucleon}$$

### Step 3: Comparison with Experiment
$$\% \text{ Discrepancy} = \frac{|8.846 - 8.790|}{8.790} \times 100\% = \frac{0.056}{8.790} \times 100\% \approx 0.64\%$$
The SEMF reproduces the binding energy of iron-56 to within **$0.64\%$**.""",
                    "hints": ["Calculate powers of A carefully: A^(1/3), A^(2/3), and A^(1/2).", "For iron-56, Z=26 and N=30 are both even, so the pairing term is positive."]
                },
                {
                    "id": "prob-2-4",
                    "problemNumber": "2.4",
                    "title": "Most Stable Isobar for Mass Chain A = 135",
                    "difficulty": "Intermediate",
                    "statement": r"""Fission of uranium produces radioactive fission products along the isobaric decay chain $A = 135$.
Using the SEMF parameters $a_c = 0.711\text{ MeV}$ and $a_a = 23.70\text{ MeV}$:
1. Derive the theoretical most stable atomic number $Z_{\text{stable}}$ for $A = 135$.
2. Identify the stable isobar that terminates this decay chain and write down the decay sequence starting from $^{135}_{53}\text{I}$.""",
                    "solution": r"""### Step 1: Calculate $Z_{\text{stable}}$
From the SEMF minimization condition:
$$Z_{\text{stable}} = \frac{A}{2 + \frac{a_c}{2 a_a} A^{2/3}}$$
For $A = 135$:
$$A^{2/3} = (135)^{2/3} \approx 26.326$$
$$\frac{a_c}{2 a_a} = \frac{0.711}{2 \times 23.70} = \frac{0.711}{47.40} \approx 0.01500$$
Denominator:
$$2 + 0.01500 \times 26.326 = 2 + 0.39489 = 2.39489$$
$$Z_{\text{stable}} = \frac{135}{2.39489} \approx 56.37$$
Rounding to the nearest integer yields:
$$Z_{\text{stable}} = 56 \quad (\text{Barium, Ba})$$

### Step 2: Isobaric Decay Chain Sequence
The chain terminates at the stable nuclide **$^{135}_{56}\text{Ba}$**.
Starting from iodine-135 (a critical reactor fission product):
$$^{135}_{53}\text{I} \xrightarrow[\beta^-]{6.57\text{ h}} \, ^{135}_{54}\text{Xe} \xrightarrow[\beta^-]{9.14\text{ h}} \, ^{135}_{55}\text{Cs} \xrightarrow[\beta^-]{2.3 \times 10^6\text{ yr}} \, ^{135}_{56}\text{Ba} \text{ (Stable)}$$
Notice that $^{135}\text{Xe}$ is the notorious "reactor poison" with a thermal neutron capture cross section of $2.6 \times 10^6\text{ barns}$.""",
                    "hints": ["Use Z_stable = A / [2 + (a_c / 2*a_a) * A^(2/3)].", "The stable endpoint must be an integer Z."]
                },
                {
                    "id": "prob-2-5",
                    "problemNumber": "2.5",
                    "title": "Nuclear Shell Model Ground-State Spin and Parity Predictions",
                    "difficulty": "Intermediate",
                    "statement": r"""Using the extreme single-particle Shell Model, predict the ground-state total angular momentum and parity ($J^\pi$) for:
1. Oxygen-17 ($^{17}_{8}\text{O}$, $Z = 8, N = 9$)
2. Potassium-39 ($^{39}_{19}\text{K}$, $Z = 19, N = 20$)
3. Scandium-45 ($^{45}_{21}\text{Sc}$, $Z = 21, N = 24$)""",
                    "solution": r"""### Shell Model Filling Sequence:
Single-particle levels in order of increasing energy:
$1s_{1/2}$ (2), $1p_{3/2}$ (4), $1p_{1/2}$ (2) [closure at 8]
$1d_{5/2}$ (6), $2s_{1/2}$ (2), $1d_{3/2}$ (4) [closure at 20]
$1f_{7/2}$ (8) [closure at 28]

### 1. Oxygen-17 ($^{17}_{8}\text{O}$):
- Protons: $Z = 8$ (closed shell, paired, contributes $0^+$).
- Neutrons: $N = 9$.
The first 8 neutrons fill the closed shell ($1s_{1/2}^2 1p_{3/2}^4 1p_{1/2}^2$).
The 9th valence neutron enters the **$1d_{5/2}$** orbital ($l = 2, j = 5/2$).
Parity: $\pi = (-1)^l = (-1)^2 = +1$.
Predicted ground state: **$J^\pi = \frac{5}{2}^+$** (Matches experiment exactly).

### 2. Potassium-39 ($^{39}_{19}\text{K}$):
- Neutrons: $N = 20$ (magic closed shell, contributes $0^+$).
- Protons: $Z = 19$.
The proton shell has 19 protons, which is one proton hole short of the $Z = 20$ shell closure.
The hole resides in the **$1d_{3/2}$** orbital ($l = 2, j = 3/2$).
Parity: $\pi = (-1)^2 = +1$.
Predicted ground state: **$J^\pi = \frac{3}{2}^+$** (Matches experiment exactly).

### 3. Scandium-45 ($^{45}_{21}\text{Sc}$):
- Neutrons: $N = 24$ (even, paired, contributes $0^+$).
- Protons: $Z = 21$.
The first 20 protons fill through $1d_{3/2}$. The 21st proton enters the **$1f_{7/2}$** orbital ($l = 3, j = 7/2$).
Parity: $\pi = (-1)^3 = -1$.
Predicted ground state: **$J^\pi = \frac{7}{2}^-$** (Matches experiment exactly).""",
                    "hints": ["Even numbers of nucleons pair to zero spin and positive parity J^pi = 0^+.", "The unpaired nucleon determines the net nuclear spin j and parity (-1)^l."]
                },
                {
                    "id": "prob-2-6",
                    "problemNumber": "2.6",
                    "title": "Coulomb Energy Difference of Mirror Nuclei and Nuclear Radius Parameter",
                    "difficulty": "Advanced",
                    "statement": r"""The mirror pair Carbon-11 ($^{11}_{6}\text{C}_5$) and Boron-11 ($^{11}_{5}\text{B}_6$) have a measured nuclear mass difference:
$$\Delta M = M(^{11}\text{C}) - M(^{11}\text{B}) = 1.982\text{ MeV}/c^2$$
Assuming the difference in binding energy is entirely due to Coulomb self-energy:
$$\Delta E_C = \frac{3}{5}\frac{e^2}{4\pi\varepsilon_0 R} [Z_1(Z_1 - 1) - Z_2(Z_2 - 1)]$$
and accounting for the neutron-proton mass difference ($m_n - m_H = 0.782\text{ MeV}$):
1. Determine the experimental Coulomb energy difference $\Delta E_C$.
2. Calculate the nuclear radius $R$ and the radius parameter $R_0$ for $A = 11$.""",
                    "solution": r"""### Step 1: Relation Between Mass Difference and Coulomb Energy
The mass difference between neutral mirror atoms is:
$$\Delta M c^2 = [M(Z+1, A) - M(Z, A)] c^2 = \Delta E_C - (m_n - m_H) c^2$$
$$\Delta E_C = \Delta M c^2 + (m_n - m_H) c^2$$
Given $\Delta M c^2 = 1.982\text{ MeV}$ and $(m_n - m_H)c^2 = 0.782\text{ MeV}$:
$$\Delta E_C = 1.982 + 0.782 = 2.764\text{ MeV}$$

### Step 2: Coulomb Energy Expression
For $^{11}\text{C}$ ($Z_1 = 6$) and $^{11}\text{B}$ ($Z_2 = 5$):
$$Z_1(Z_1 - 1) - Z_2(Z_2 - 1) = 6(5) - 5(4) = 30 - 20 = 10$$
Therefore:
$$\Delta E_C = \frac{3}{5}\frac{e^2}{4\pi\varepsilon_0 R} \cdot 10 = \frac{6 e^2}{4\pi\varepsilon_0 R}$$
Using $\frac{e^2}{4\pi\varepsilon_0} \approx 1.43996\text{ MeV}\cdot\text{fm}$:
$$\Delta E_C = \frac{6 \times 1.43996\text{ MeV}\cdot\text{fm}}{R} = \frac{8.6398\text{ MeV}\cdot\text{fm}}{R}$$

### Step 3: Solve for $R$ and $R_0$
$$R = \frac{8.6398\text{ MeV}\cdot\text{fm}}{2.764\text{ MeV}} \approx 3.126\text{ fm}$$
Using $R = R_0 A^{1/3}$ with $A = 11$:
$$A^{1/3} = (11)^{1/3} \approx 2.224$$
$$R_0 = \frac{R}{A^{1/3}} = \frac{3.126\text{ fm}}{2.224} \approx 1.405\text{ fm}$$
This value ($1.40\text{ fm}$) agrees with the accepted strong interaction matter radius parameter.""",
                    "hints": ["Remember to account for the neutron-proton mass difference in mirror nuclei.", "e^2 / (4*pi*epsilon_0) = 1.44 MeV*fm is a very handy physical constant."]
                },
                {
                    "id": "prob-2-7",
                    "problemNumber": "2.7",
                    "title": "Collective Rotational Band Energies of Uranium-238",
                    "difficulty": "Intermediate",
                    "statement": r"""The ground-state rotational band of the deformed even-even nucleus $^{238}_{92}\text{U}$ exhibits its first excited $2^+$ state at an excitation energy of $E(2^+) = 44.91\text{ keV}$.
1. Assuming a rigid rotor $E(J) = \frac{\hbar^2}{2\mathcal{I}} J(J+1)$, calculate the rotational inertia parameter $\frac{\hbar^2}{2\mathcal{I}}$ in $\text{keV}$.
2. Predict the excitation energies of the $4^+$, $6^+$, and $8^+$ rotational states.
3. Compare the predicted values with the experimental energies ($E(4^+) = 148.4\text{ keV}$, $E(6^+) = 307.2\text{ keV}$) and comment on centrifugal stretching.""",
                    "solution": r"""### Step 1: Rotational Inertia Parameter
For $J = 2$:
$$E(2^+) = \frac{\hbar^2}{2\mathcal{I}} 2(2 + 1) = 6 \left(\frac{\hbar^2}{2\mathcal{I}}\right) = 44.91\text{ keV}$$
$$\frac{\hbar^2}{2\mathcal{I}} = \frac{44.91\text{ keV}}{6} = 7.485\text{ keV}$$

### Step 2: Predict $4^+$, $6^+$, and $8^+$ Energies
1. State $4^+$ ($J = 4$):
$$E(4^+) = \left(\frac{\hbar^2}{2\mathcal{I}}\right) 4(5) = 20 \times 7.485\text{ keV} = 149.70\text{ keV}$$
2. State $6^+$ ($J = 6$):
$$E(6^+) = \left(\frac{\hbar^2}{2\mathcal{I}}\right) 6(7) = 42 \times 7.485\text{ keV} = 314.37\text{ keV}$$
3. State $8^+$ ($J = 8$):
$$E(8^+) = \left(\frac{\hbar^2}{2\mathcal{I}}\right) 8(9) = 72 \times 7.485\text{ keV} = 538.92\text{ keV}$$

### Step 3: Comparison with Experiment and Centrifugal Stretching
- Experimental $E(4^+) = 148.4\text{ keV}$ vs Predicted $149.7\text{ keV}$ (Discrepancy: $+0.87\%$)
- Experimental $E(6^+) = 307.2\text{ keV}$ vs Predicted $314.4\text{ keV}$ (Discrepancy: $+2.3\%$)
The experimental energies are slightly lower than the rigid rotor prediction. As the nucleus spins faster at higher $J$, centrifugal forces stretch the deformed nucleus, increasing its moment of inertia $\mathcal{I}$ and lowering the rotational energy spacing (centrifugal stretching correction $-D J^2(J+1)^2$).""",
                    "hints": ["Rotational energies follow E(J) = A * J*(J+1).", "Find the constant A from the 2+ state and multiply by J*(J+1) for higher states."]
                }
            ]
        },

        # =====================================================================
        # UNIT 3
        # =====================================================================
        {
            "id": "unit-3-decay-kinetics-bateman-equilibria",
            "unitNumber": 3,
            "title": "Unit 3: Decay Kinetics of Unstable Nuclei: Half-Life, Successive Decay & Bateman Equilibria",
            "leadSummary": "Comprehensive mathematical exposition of radioactive decay kinetics: the differential decay rate law, mean life derivations, Poisson counting statistics, branching decay channels, the general solution of successive multi-nuclide decay chains via the Bateman equations, and quantitative criteria for secular, transient, and non-equilibrium regimes.",
            "simulations": ["sim_nuc_decay_series_bateman"],
            "sections": [
                {
                    "id": "sec-3-1",
                    "secNumber": "3.1",
                    "title": "The Fundamental Radioactive Decay Differential Rate Law & Integral Kinetics",
                    "content": r"""Radioactive decay is a first-order unimolecular kinetic transformation governed by the fundamental quantum decay probability $\lambda$. Consider an ensemble of $N(t)$ identical, non-interacting unstable radioactive nuclei. In any infinitesimal time interval $dt$, the probability $dp$ that an individual nucleus disintegrates is:
$$dp = \lambda \, dt$$
where $\lambda$ is the **decay constant** ($\text{s}^{-1}$), an intrinsic nuclear property independent of chemical bonding, physical state, temperature, or pressure.

### The Differential Rate Law
The expected number of nuclear disintegrations $dN$ occurring in the sample within time interval $dt$ is:
$$dN = -N(t) \cdot dp = -\lambda N(t) dt \implies \frac{dN}{dt} = -\lambda N(t)$$
The negative sign signifies that the population of parent nuclei decreases monotonically over time.

### Integral Form of the Decay Law
Separating variables and integrating from initial boundary condition $N(0) = N_0$ at $t = 0$:
$$\int_{N_0}^{N(t)} \frac{dN'}{N'} = -\lambda \int_0^t dt'$$
$$\ln\left(\frac{N(t)}{N_0}\right) = -\lambda t \implies N(t) = N_0 e^{-\lambda t}$$

The number of disintegrated daughter nuclei $N_D(t)$ formed (assuming a stable daughter and $N_D(0) = 0$) is:
$$N_D(t) = N_0 - N(t) = N_0 (1 - e^{-\lambda t})$$

```
   Number of Nuclei
 N₀ ▲
    │\  Parent N(t) = N₀ e^(-λt)        Daughter N_D(t) = N₀ (1 - e^(-λt))
    │ \                                /
N₀/2│--\------------------------------/-- (Half-Life T₁/₂)
    │   \                            /
    │    \                          /
    │     \________________________/
    └──────┴────────────────────────► Time t
           T₁/₂
```

### Radioactive Activity Formulation
The absolute rate of disintegration is defined as **activity** $A(t)$:
$$A(t) \equiv -\frac{dN}{dt} = \lambda N(t) = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$$
Activity decays with the identical exponential rate constant $\lambda$ as the number of atoms.

### Logarithmic Linearization
Taking the natural logarithm of both sides:
$$\ln A(t) = \ln A_0 - \lambda t$$
Plotting $\ln A(t)$ versus time $t$ yields a straight line with:
- Vertical intercept: $\ln A_0$
- Slope: $-\lambda$
In base-10 logarithms:
$$\log_{10} A(t) = \log_{10} A_0 - \frac{\lambda}{2.302585} t$$""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-3-2",
                    "secNumber": "3.2",
                    "title": "Half-Life, Mean Life & Decay Rate Parameter Interconversions",
                    "content": r"""The kinetics of radionuclide disappearance can be characterized using three mathematically related parameters:
1. **Decay Constant** $\lambda$ (dimensions: $[\text{T}]^{-1}$, typically $\text{s}^{-1}$, $\text{h}^{-1}$, or $\text{yr}^{-1}$)
2. **Half-Life** $T_{1/2}$ (dimensions: $[\text{T}]$)
3. **Mean Life** $\tau$ (dimensions: $[\text{T}]$)

### Detailed Derivation of Half-Life ($T_{1/2}$)
The half-life is the duration required for the active population (or activity) to decline to exactly half its initial value:
$$\frac{N(T_{1/2})}{N_0} = \frac{1}{2} = e^{-\lambda T_{1/2}}$$
Taking the natural logarithm:
$$\ln\left(\frac{1}{2}\right) = -\ln 2 = -\lambda T_{1/2} \implies T_{1/2} = \frac{\ln 2}{\lambda}$$
Using $\ln 2 \approx 0.69314718056$:
$$T_{1/2} \approx \frac{0.693147}{\lambda} \quad \text{or} \quad \lambda = \frac{0.693147}{T_{1/2}}$$

The surviving fraction after an arbitrary number of half-lives $n = t / T_{1/2}$ is:
$$\frac{N(t)}{N_0} = e^{-\lambda t} = e^{-(\ln 2 / T_{1/2}) t} = \left(e^{-\ln 2}\right)^{t / T_{1/2}} = \left(\frac{1}{2}\right)^{t / T_{1/2}} = 2^{-n}$$

| Half-Lives Elapsed ($n$) | Surviving Fraction ($N/N_0$) | Percentage Surviving | Decayed Fraction ($1 - N/N_0$) |
| :--- | :--- | :--- | :--- |
| **0** | $1$ | $100.00\%$ | $0.00\%$ |
| **1** | $1/2$ | $50.00\%$ | $50.00\%$ |
| **2** | $1/4$ | $25.00\%$ | $75.00\%$ |
| **3** | $1/8$ | $12.50\%$ | $87.50\%$ |
| **5** | $1/32$ | $3.125\%$ | $96.875\%$ |
| **7** | $1/128$ | $0.781\%$ | $99.219\%$ |
| **10** | $1/1024$ | $0.0977\%$ | $99.9023\%$ |

After 10 half-lives, less than $0.1\%$ ($1/1024$) of the initial radioactivity remains. In radioprotection and waste management, $10 T_{1/2}$ is the standard operational threshold for total decay of short-lived isotopes.

### Detailed Derivation of Mean Life ($\tau$)
The mean lifetime $\tau$ is the arithmetic average lifespan of all nuclei in an ensemble. The probability distribution function $P(t) dt$ representing the probability that a nucleus decays between time $t$ and $t + dt$ is:
$$P(t) dt = \frac{|dN|}{N_0} = \lambda e^{-\lambda t} dt$$
Note that this distribution is properly normalized:
$$\int_0^\infty P(t) dt = \lambda \int_0^\infty e^{-\lambda t} dt = \lambda \left[ -\frac{1}{\lambda} e^{-\lambda t} \right]_0^\infty = 1$$
The expectation value $\langle t \rangle = \tau$ is:
$$\tau = \int_0^\infty t P(t) dt = \int_0^\infty t (\lambda e^{-\lambda t}) dt = \lambda \int_0^\infty t e^{-\lambda t} dt$$
Using the standard definite integral $\int_0^\infty t^n e^{-\lambda t} dt = \frac{n!}{\lambda^{n+1}}$ with $n = 1$:
$$\tau = \lambda \left(\frac{1!}{\lambda^2}\right) = \frac{1}{\lambda}$$

Converting between mean life and half-life:
$$\tau = \frac{T_{1/2}}{\ln 2} \approx 1.442695 \cdot T_{1/2}$$
$$T_{1/2} = \tau \ln 2 \approx 0.693147 \cdot \tau$$

### Total Number of Decays Over All Time
The total cumulative disintegrations $N_{\text{tot}}$ that occur between $t = 0$ and $t = \infty$ is:
$$N_{\text{tot}} = \int_0^\infty A(t) dt = \int_0^\infty A_0 e^{-\lambda t} dt = A_0 \left[ -\frac{1}{\lambda} e^{-\lambda t} \right]_0^\infty = \frac{A_0}{\lambda} = A_0 \cdot \tau$$
The total number of atoms initially present is equal to the initial activity multiplied by the mean life:
$$N_0 = A_0 \tau$$""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-3-3",
                    "secNumber": "3.3",
                    "title": "Stochastic Foundations of Nuclear Counting: Poisson Statistics & Variance Limits",
                    "content": r"""Because radioactive decay is a completely random stochastic process, repeated counts recorded over identical time intervals fluctuate. Understanding these statistical fluctuations is essential for determining experimental uncertainties, detection limits, and confidence intervals in radiation measurements.

### The Binomial Distribution Formulation
Consider a sample containing $N_0$ radioactive atoms. Over an observation interval $\Delta t$, the probability that any specific nucleus decays is:
$$p = 1 - e^{-\lambda \Delta t}$$
The probability that it survives is $q = 1 - p = e^{-\lambda \Delta t}$.
The probability $P(n)$ of observing exactly $n$ disintegrations out of $N_0$ atoms is governed by the **Binomial distribution**:
$$P(n) = \frac{N_0!}{n! (N_0 - n)!} p^n (1 - p)^{N_0 - n}$$

### The Poisson Approximation
In real radiochemical counting experiments:
1. The total number of atoms is extraordinarily large ($N_0 \sim 10^{12} - 10^{20}$).
2. The decay probability over typical counting intervals is tiny ($p \ll 1$).
3. The expected mean count $\mu = N_0 p$ remains finite.

Taking the mathematical limit $N_0 \to \infty$ and $p \to 0$ while holding $\mu = N_0 p$ constant, the Binomial distribution converges rigorously to the **Poisson distribution**:
$$P(n) = \frac{\mu^n e^{-\mu}}{n!}$$
where $\mu$ is the true mean count.

```
   P(n) Probability
  ▲
  │         Poisson Distribution (μ = 10)
  │             ___
  │           /     \
  │          /       \
  │         /         \
  │        /           \
  │_______/             \________
  └───────┴──────┴───────┴───────► Recorded Counts n
          0      μ=10    20
```

### Variance and Standard Deviation of Poisson Counting
For a Poisson distribution:
- **Expectation Value**: $\langle n \rangle = \mu$
- **Variance**: $\sigma^2 = \mu$
- **Standard Deviation**: $\sigma = \sqrt{\mu}$

In an experimental determination, the true mean $\mu$ is unknown and is estimated by the observed single count $N$:
$$\sigma \approx \sqrt{N}$$
The result of any radiation measurement is expressed with its one-sigma standard uncertainty ($68.3\%$ confidence interval) as:
$$\text{Measured Count} = N \pm \sqrt{N}$$

### Relative Standard Deviation (RSD) and Counting Precision
The relative standard uncertainty (coefficient of variation) is:
$$\text{RSD} = \frac{\sigma}{N} = \frac{\sqrt{N}}{N} = \frac{1}{\sqrt{N}}$$
$$\% \text{RSD} = \frac{100\%}{\sqrt{N}}$$

| Observed Counts ($N$) | Standard Deviation ($\sigma = \sqrt{N}$) | Relative Standard Deviation (% RSD) | Metrological Level |
| :--- | :--- | :--- | :--- |
| **100** | $\pm 10$ | $10.0\%$ | Screening survey |
| **1,000** | $\pm 31.6$ | $3.16\%$ | Routine monitoring |
| **10,000** | $\pm 100$ | $1.00\%$ | Analytical standard |
| **100,000** | $\pm 316.2$ | $0.316\%$ | High-precision metrology |
| **1,000,000** | $\pm 1000$ | $0.100\%$ | Absolute activity calibration |

To improve counting precision by a factor of 10, the counting duration (or accumulated count total) must be increased by a factor of **$10^2 = 100$**.

### Net Count Rate and Background Subtraction Uncertainty
Every radiation detector records ambient background radiation counts $N_b$ during background counting time $t_b$, in addition to gross sample counts $N_g$ accumulated over sample counting time $t_g$.
The net count rate $R_n$ is:
$$R_n = R_g - R_b = \frac{N_g}{t_g} - \frac{N_b}{t_b}$$
By propagation of independent random errors:
$$\sigma_{R_n}^2 = \sigma_{R_g}^2 + \sigma_{R_b}^2 = \frac{\sigma_{N_g}^2}{t_g^2} + \frac{\sigma_{N_b}^2}{t_b^2} = \frac{N_g}{t_g^2} + \frac{N_b}{t_b^2} = \frac{R_g}{t_g} + \frac{R_b}{t_b}$$
$$\sigma_{R_n} = \sqrt{\frac{R_g}{t_g} + \frac{R_b}{t_b}}$$""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-3-4",
                    "secNumber": "3.4",
                    "title": "Branching Decay Mechanics, Partial Decay Constants & Competing Transition Ratios",
                    "content": r"""Many unstable nuclei can decay through multiple competing pathways. For example, potassium-40 ($^{40}\text{K}$) undergoes both negative beta decay ($\beta^-$) into calcium-40 and electron capture (EC) into argon-40:
```
                    ┌───► ⁴⁰Ca + e⁻ + ν̄_e   (β⁻ decay: 89.28%)
         ⁴⁰K ───────┤
                    └───► ⁴⁰Ar + ν_e + γ     (EC decay: 10.72%)
```
Similarly, copper-64 ($^{64}\text{Cu}$) decays via three competing modes: $\beta^-$ ($39.0\%$), $\beta^+$ ($17.6\%$), and electron capture ($43.4\%$).

### Partial Decay Constants
Let an unstable nuclide decay through $m$ independent competing branches, each characterized by its own **partial decay constant** $\lambda_i$:
$$-\left(\frac{dN}{dt}\right)_i = \lambda_i N$$
The total rate of disappearance of the parent nucleus is the sum of the disappearance rates across all individual decay modes:
$$-\frac{dN}{dt} = \sum_{i=1}^m -\left(\frac{dN}{dt}\right)_i = \sum_{i=1}^m \lambda_i N = \left(\sum_{i=1}^m \lambda_i\right) N$$
Defining the **total decay constant** $\lambda_{\text{tot}}$:
$$\lambda_{\text{tot}} = \sum_{i=1}^m \lambda_i = \lambda_1 + \lambda_2 + \dots + \lambda_m$$

The population of the parent decays exponentially according to the **total** decay constant:
$$N(t) = N_0 e^{-\lambda_{\text{tot}} t}$$

### Effective Total Half-Life
Because $T_{1/2} = \ln 2 / \lambda$, the total half-life $T_{1/2,\text{tot}}$ satisfies:
$$\frac{\ln 2}{T_{1/2,\text{tot}}} = \frac{\ln 2}{T_{1/2,1}} + \frac{\ln 2}{T_{1/2,2}} + \dots + \frac{\ln 2}{T_{1/2,m}}$$
Dividing through by $\ln 2$:
$$\frac{1}{T_{1/2,\text{tot}}} = \sum_{i=1}^m \frac{1}{T_{1/2,i}} = \frac{1}{T_{1/2,1}} + \frac{1}{T_{1/2,2}} + \dots + \frac{1}{T_{1/2,m}}$$
Notice that this is formally identical to the formula for resistors connected in parallel.
For two competing branches:
$$T_{1/2,\text{tot}} = \frac{T_{1/2,1} \cdot T_{1/2,2}}{T_{1/2,1} + T_{1/2,2}}$$
The total half-life is **always strictly shorter** than the shortest partial half-life.

### Branching Ratio (Branching Fraction)
The **branching ratio** $BR_i$ (or branching fraction $f_i$) of the $i$-th decay channel is defined as the fraction of all decays that proceed through that channel:
$$BR_i = \frac{\lambda_i}{\lambda_{\text{tot}}} = \frac{\lambda_i}{\sum \lambda_k} = \frac{T_{1/2,\text{tot}}}{T_{1/2,i}}$$
By definition, the sum of all branching ratios equals unity:
$$\sum_{i=1}^m BR_i = 1.00 \quad (100\%)$$

### Daughter Growth Kinetics in Branching Decay
The production rate of daughter nucleus $D_i$ formed via the $i$-th branch is:
$$\frac{d N_{D,i}}{dt} = \lambda_i N(t) = \lambda_i N_0 e^{-\lambda_{\text{tot}} t}$$
Assuming $N_{D,i}(0) = 0$ and that the daughter is stable:
$$N_{D,i}(t) = \int_0^t \lambda_i N_0 e^{-\lambda_{\text{tot}} t'} dt' = \frac{\lambda_i}{\lambda_{\text{tot}}} N_0 (1 - e^{-\lambda_{\text{tot}} t}) = BR_i \cdot N_0 (1 - e^{-\lambda_{\text{tot}} t})$$
At any time $t$, the ratio of the numbers of atoms of two alternative stable daughters produced is:
$$\frac{N_{D,1}(t)}{N_{D,2}(t)} = \frac{BR_1}{BR_2} = \frac{\lambda_1}{\lambda_2} = \text{constant}$$
This constant ratio forms the physical foundation of **K-Ar (potassium-argon) geological dating**, where the accumulated $^{40}\text{Ar}$ relative to $^{40}\text{Ca}$ determines rock crystallization age over billions of years.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-3-5",
                    "secNumber": "3.5",
                    "title": "Successive Decay Series & Rigorous Derivation of the Master Bateman Equations",
                    "content": r"""In many radioactive decay chains, an unstable parent radionuclide decays into a daughter which is itself radioactive, giving rise to a cascade of successive decays:
$$N_1 \xrightarrow{\lambda_1} N_2 \xrightarrow{\lambda_2} N_3 \xrightarrow{\lambda_3} \dots \xrightarrow{\lambda_{n-1}} N_n \xrightarrow{\lambda_n} \dots$$

### The System of Coupled Differential Rate Equations
The time evolution of the population of each nuclide in the chain is governed by a balance between production from its immediate parent and disappearance via its own decay:
$$\frac{dN_1}{dt} = -\lambda_1 N_1$$
$$\frac{dN_2}{dt} = \lambda_1 N_1 - \lambda_2 N_2$$
$$\frac{dN_3}{dt} = \lambda_2 N_2 - \lambda_3 N_3$$
$$\vdots$$
$$\frac{dN_i}{dt} = \lambda_{i-1} N_{i-1} - \lambda_i N_i$$

### Derivation for a Two-Step Chain ($N_1 \to N_2 \to N_3$)
Let the initial conditions at $t = 0$ be $N_1(0) = N_1^0$ and $N_2(0) = 0, N_3(0) = 0$.
1. **Parent Solution**:
$$N_1(t) = N_1^0 e^{-\lambda_1 t}$$

2. **Daughter Solution**:
Substitute $N_1(t)$ into the daughter differential equation:
$$\frac{dN_2}{dt} + \lambda_2 N_2 = \lambda_1 N_1^0 e^{-\lambda_1 t}$$
This is a first-order linear ordinary differential equation. Multiplying by the integrating factor $e^{\lambda_2 t}$:
$$e^{\lambda_2 t}\left(\frac{dN_2}{dt} + \lambda_2 N_2\right) = \frac{d}{dt}\left(N_2 e^{\lambda_2 t}\right) = \lambda_1 N_1^0 e^{(\lambda_2 - \lambda_1) t}$$
Integrating both sides from $0$ to $t$:
$$N_2(t) e^{\lambda_2 t} - N_2(0) = \lambda_1 N_1^0 \int_0^t e^{(\lambda_2 - \lambda_1) t'} dt'$$
Assuming $\lambda_1 \ne \lambda_2$:
$$N_2(t) e^{\lambda_2 t} = \frac{\lambda_1 N_1^0}{\lambda_2 - \lambda_1} \left( e^{(\lambda_2 - \lambda_1) t} - 1 \right)$$
Multiplying by $e^{-\lambda_2 t}$:
$$N_2(t) = \frac{\lambda_1}{\lambda_2 - \lambda_1} N_1^0 \left( e^{-\lambda_1 t} - e^{-\lambda_2 t} \right)$$

The daughter activity $A_2(t) = \lambda_2 N_2(t)$ is:
$$A_2(t) = \frac{\lambda_2 \lambda_1}{\lambda_2 - \lambda_1} N_1^0 \left( e^{-\lambda_1 t} - e^{-\lambda_2 t} \right) = \frac{\lambda_2}{\lambda_2 - \lambda_1} A_1(t) \left( 1 - e^{-(\lambda_2 - \lambda_1) t} \right)$$

### General Harry Bateman Solution (1910)
For an arbitrary linear chain of $n$ nuclides with initial condition $N_1(0) = N_1^0$ and $N_2(0) = N_3(0) = \dots = N_n(0) = 0$, Harry Bateman proved via Laplace transforms that the population of the $n$-th nuclide is:
$$N_n(t) = N_1^0 \left( \prod_{i=1}^{n-1} \lambda_i \right) \sum_{j=1}^n \frac{e^{-\lambda_j t}}{\prod_{\substack{k=1 \\ k \ne j}}^n (\lambda_k - \lambda_j)}$$
Expanded explicitly:
$$N_n(t) = C_1 e^{-\lambda_1 t} + C_2 e^{-\lambda_2 t} + \dots + C_n e^{-\lambda_n t}$$
where each coefficient $C_j$ is given by:
$$C_j = \frac{\lambda_1 \lambda_2 \cdots \lambda_{n-1}}{(\lambda_1 - \lambda_j)(\lambda_2 - \lambda_j)\cdots(\lambda_{j-1} - \lambda_j)(\lambda_{j+1} - \lambda_j)\cdots(\lambda_n - \lambda_j)} N_1^0$$

This elegant theorem solves the isotopic inventory of any nuclear decay chain, from uranium decay series to complex reactor core transmutations.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-3-6",
                    "secNumber": "3.6",
                    "title": "Secular and Transient Radioactive Equilibria: Mathematical Conditions & Time-to-Peak",
                    "content": r"""In a successive decay chain $N_1 \xrightarrow{\lambda_1} N_2 \xrightarrow{\lambda_2} N_3$, the temporal relationship between parent and daughter activities depends fundamentally on the relative magnitudes of the decay constants $\lambda_1$ and $\lambda_2$. Three distinct kinetic regimes emerge:

### 1. Secular Equilibrium ($\lambda_1 \ll \lambda_2$, i.e., $T_{1/2,1} \gg T_{1/2,2}$)
When the parent half-life is thousands or millions of times longer than the daughter half-life, the parent activity remains essentially constant over experimental timescales:
$$\lambda_1 \approx 0 \implies e^{-\lambda_1 t} \approx 1 \quad \text{and} \quad \lambda_2 - \lambda_1 \approx \lambda_2$$
Substituting into the daughter activity equation:
$$A_2(t) = \frac{\lambda_2 \lambda_1}{\lambda_2 - \lambda_1} N_1^0 (e^{-\lambda_1 t} - e^{-\lambda_2 t}) \approx \frac{\lambda_2 \lambda_1}{\lambda_2} N_1^0 (1 - e^{-\lambda_2 t}) = \lambda_1 N_1^0 (1 - e^{-\lambda_2 t})$$
$$A_2(t) = A_1^0 (1 - e^{-\lambda_2 t})$$

```
   Activity A(t)
 A₁ ▲──────────────────────────────────── Parent A₁(t) = A₁⁰ (Constant)
    │           /──────────────────────── Daughter A₂(t) in Secular Eq: A₂ = A₁
    │          /
    │         /
    │        /
    │_______/
    └───────┴────────────────────────────► Time t
            ~ 7 T₁/₂,₂
```

As $t \gg T_{1/2,2}$ ($t \ge 7 T_{1/2,2}$), $e^{-\lambda_2 t} \to 0$:
$$A_2(t) \longrightarrow A_1(t) \implies \lambda_1 N_1 = \lambda_2 N_2$$
$$\frac{N_1}{N_2} = \frac{\lambda_2}{\lambda_1} = \frac{T_{1/2,1}}{T_{1/2,2}}$$
In secular equilibrium, the daughter activity **becomes exactly equal to the parent activity**, and the abundance ratio of parent to daughter is directly proportional to their half-lives!
Classic natural examples:
- $^{226}\text{Ra}$ ($T_{1/2} = 1600\text{ yr}$) $\xrightarrow{\alpha} \, ^{222}\text{Rn}$ ($T_{1/2} = 3.82\text{ days}$)
- $^{238}\text{U}$ ($T_{1/2} = 4.47 \times 10^9\text{ yr}$) $\xrightarrow{\alpha} \, ^{234}\text{Th}$ ($T_{1/2} = 24.1\text{ days}$)

### 2. Transient Equilibrium ($\lambda_1 < \lambda_2$, but parent decays noticeably, $T_{1/2,1} \approx 10 T_{1/2,2}$)
When the parent half-life is moderately longer than the daughter, the daughter activity rises, reaches a maximum, and then decays with the apparent half-life of the parent.
For large $t$ such that $e^{-\lambda_2 t} \ll e^{-\lambda_1 t}$:
$$A_2(t) \approx \frac{\lambda_2}{\lambda_2 - \lambda_1} A_1^0 e^{-\lambda_1 t} = \frac{\lambda_2}{\lambda_2 - \lambda_1} A_1(t)$$
Notice that in transient equilibrium, the daughter activity **exceeds the parent activity** by the constant factor:
$$\frac{A_2(t)}{A_1(t)} = \frac{\lambda_2}{\lambda_2 - \lambda_1} > 1$$

### Derivation of Time to Maximum Daughter Activity ($t_{\max}$)
To determine when the daughter activity reaches its peak, differentiate $N_2(t)$ with respect to $t$ and set the derivative to zero:
$$\frac{dN_2}{dt} = \frac{\lambda_1 N_1^0}{\lambda_2 - \lambda_1} \left( -\lambda_1 e^{-\lambda_1 t} + \lambda_2 e^{-\lambda_2 t} \right) = 0$$
$$\lambda_1 e^{-\lambda_1 t_{\max}} = \lambda_2 e^{-\lambda_2 t_{\max}}$$
Taking natural logarithms:
$$\ln\lambda_1 - \lambda_1 t_{\max} = \ln\lambda_2 - \lambda_2 t_{\max}$$
$$(\lambda_2 - \lambda_1) t_{\max} = \ln\left(\frac{\lambda_2}{\lambda_1}\right)$$
Yielding the **Time-to-Peak Equation**:
$$t_{\max} = \frac{\ln(\lambda_2 / \lambda_1)}{\lambda_2 - \lambda_1} = \frac{\ln(T_{1/2,1} / T_{1/2,2})}{\lambda_2 - \lambda_1}$$

At exactly $t = t_{\max}$, substituting $\lambda_1 e^{-\lambda_1 t} = \lambda_2 e^{-\lambda_2 t}$ into $A_2(t)$:
$$A_2(t_{\max}) = A_1(t_{\max})$$
At the peak, the parent and daughter activity curves **cross each other**!
The premier radiopharmaceutical example is the **$^{99}\text{Mo} \to ^{99m}\text{Tc}$ generator**:
- $^{99}\text{Mo}$: $T_{1/2} = 66.0\text{ hours}$
- $^{99m}\text{Tc}$: $T_{1/2} = 6.01\text{ hours}$
- $t_{\max} \approx 22.9\text{ hours}$ post-elution, determining the optimal clinical elution schedule.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                },
                {
                    "id": "sec-3-7",
                    "secNumber": "3.7",
                    "title": "Non-Equilibrium Decay Regimes & Radionuclide Inventory Evolution",
                    "content": r"""The third kinetic regime occurs when the parent decays faster than the daughter.

### No Equilibrium ($\lambda_1 > \lambda_2$, i.e., $T_{1/2,1} < T_{1/2,2}$)
When the parent has a shorter half-life than the daughter, **no equilibrium is ever established**.
As time progresses:
$$e^{-\lambda_1 t} \ll e^{-\lambda_2 t}$$
The exponential term of the parent vanishes rapidly, leaving only the daughter's decay term:
$$N_2(t) \approx \frac{\lambda_1}{\lambda_1 - \lambda_2} N_1^0 e^{-\lambda_2 t}$$
All initial parent nuclei disintegrate into daughter nuclei, which then decay away at their own leisurely characteristic rate $\lambda_2$.
Examples:
- $^{140}\text{Ba}$ ($T_{1/2} = 12.75\text{ days}$) $\xrightarrow{\beta^-} \, ^{140}\text{La}$ ($T_{1/2} = 1.678\text{ days}$)
- $^{218}\text{Po}$ ($T_{1/2} = 3.10\text{ min}$) $\xrightarrow{\alpha} \, ^{214}\text{Pb}$ ($T_{1/2} = 26.8\text{ min}$)

```
   Activity A(t)
 ▲
 │   Parent A₁(t) (Rapid Fall)
 │   \
 │    \          Daughter Growth and Slow Decay A₂(t)
 │     \       /──────────────\
 │      \____/                 \_________________
 └────────────────────────────────────────────────► Time t
```

### Comprehensive Comparison of Equilibrium Regimes

| Equilibrium Type | Half-Life Relationship | Ratio of Decay Constants | Activity Ratio at Late Times | Cross-Over at $t_{\max}$? | Representative Real-World Example |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Secular** | $T_{1/2,1} \gg T_{1/2,2}$ ($>10^4\times$) | $\lambda_1 \ll \lambda_2$ | $\frac{A_2(t)}{A_1(t)} \to 1.000$ | No ($A_2$ approaches $A_1$ asymptotically) | $^{226}\text{Ra} \xrightarrow{\alpha} ^{222}\text{Rn}$ |
| **Transient** | $T_{1/2,1} > T_{1/2,2}$ ($\sim 10\times$) | $\lambda_1 < \lambda_2$ | $\frac{A_2(t)}{A_1(t)} \to \frac{\lambda_2}{\lambda_2 - \lambda_1} > 1$ | **Yes** ($A_2 = A_1$ at $t = t_{\max}$) | $^{99}\text{Mo} \xrightarrow{\beta^-} ^{99m}\text{Tc}$ |
| **No Equilibrium** | $T_{1/2,1} < T_{1/2,2}$ | $\lambda_1 > \lambda_2$ | $\frac{A_2(t)}{A_1(t)} \to \infty$ ($A_1 \to 0$) | **Yes** ($A_2$ overtakes $A_1$, parent vanishes) | $^{218}\text{Po} \xrightarrow{\alpha} ^{214}\text{Pb}$ |

### Radionuclide Inventory in Nuclear Reactors and Spent Fuel
Understanding these three regimes is the core principle of **nuclear fuel inventory codes** (e.g., ORIGEN). In freshly discharged spent nuclear fuel:
1. Short-lived fission products ($T_{1/2} \sim \text{seconds to days}$) undergo rapid non-equilibrium cascades into longer-lived daughters.
2. In intermediate storage ponds ($1 - 5\text{ years}$), isotopes like $^{137}\text{Cs} \to ^{137m}\text{Ba}$ ($T_{1/2} = 2.55\text{ min}$) and $^{90}\text{Sr} \to ^{90}\text{Y}$ ($T_{1/2} = 64.1\text{ hours}$) exist in strict **secular equilibrium**, where the daughter activity matches the 30-year parent activity.
3. In deep geological repositories ($>10^4\text{ years}$), actinide decay chains ($^{241}\text{Pu} \to ^{241}\text{Am} \to ^{237}\text{Np}$) govern long-term radiotoxicity.""",
                    "simulations": ["sim_nuc_decay_series_bateman"]
                }
            ],
            "problems": [
                {
                    "id": "prob-3-1",
                    "problemNumber": "3.1",
                    "title": "Bateman Transient Equilibrium Peak Time for Mo-99 / Tc-99m Generator",
                    "difficulty": "Intermediate",
                    "statement": r"""A molybdenum-99 / technetium-99m medical generator utilizes fission-produced $^{99}\text{Mo}$ ($T_{1/2,1} = 66.00\text{ hours}$) which beta-decays with a branching fraction $BR = 0.875$ into metastable $^{99m}\text{Tc}$ ($T_{1/2,2} = 6.007\text{ hours}$).
Immediately following complete saline elution (milking) at $t = 0$, the column contains zero $^{99m}\text{Tc}$ ($N_2(0) = 0$).
1. Calculate the decay constants $\lambda_1$ and $\lambda_2$ in $\text{h}^{-1}$.
2. Derive and calculate the exact time $t_{\max}$ (in hours) at which the $^{99m}\text{Tc}$ activity on the column reaches its theoretical maximum.
3. Calculate the ratio of $^{99m}\text{Tc}$ activity to $^{99}\text{Mo}$ activity on the column at transient equilibrium ($t \gg t_{\max}$).""",
                    "solution": r"""### Step 1: Decay Constants
$$\lambda_1 = \frac{\ln 2}{66.00\text{ h}} = \frac{0.693147}{66.00} \approx 0.010502\text{ h}^{-1}$$
$$\lambda_2 = \frac{\ln 2}{6.007\text{ h}} = \frac{0.693147}{6.007} \approx 0.115390\text{ h}^{-1}$$

### Step 2: Time to Maximum Activity $t_{\max}$
Because branching fraction $BR$ is a constant multiplier, it does not alter the location of the extremum:
$$t_{\max} = \frac{\ln(\lambda_2 / \lambda_1)}{\lambda_2 - \lambda_1}$$
Compute the ratio and difference:
$$\frac{\lambda_2}{\lambda_1} = \frac{0.115390}{0.010502} \approx 10.9874$$
$$\ln\left(\frac{\lambda_2}{\lambda_1}\right) = \ln(10.9874) \approx 2.39675$$
$$\lambda_2 - \lambda_1 = 0.115390 - 0.010502 = 0.104888\text{ h}^{-1}$$
$$t_{\max} = \frac{2.39675}{0.104888\text{ h}^{-1}} \approx 22.85\text{ hours}$$
The technetium activity peaks at **$22.85\text{ hours}$** post-elution (explaining why radiopharmacies elute generators once every 24 hours).

### Step 3: Activity Ratio at Transient Equilibrium
Accounting for the branching ratio $BR = 0.875$:
$$\frac{A_2(t)}{A_1(t)} = BR \cdot \frac{\lambda_2}{\lambda_2 - \lambda_1} = 0.875 \times \frac{0.115390}{0.104888} = 0.875 \times 1.10012 \approx 0.9626$$
At transient equilibrium, the $^{99m}\text{Tc}$ activity tracks at **$96.3\%$** of the $^{99}\text{Mo}$ parent activity.""",
                    "hints": ["Remember that branching ratio BR multiplies daughter activity: A_2 = BR * lambda_2 * N_2.", "t_max is found from ln(lambda_2 / lambda_1) / (lambda_2 - lambda_1)."]
                },
                {
                    "id": "prob-3-2",
                    "problemNumber": "3.2",
                    "title": "Secular Equilibrium Activity and Mass in Natural Uranium Ores",
                    "difficulty": "Easy",
                    "statement": r"""In an undisturbed geological mineral specimen of pitchblende ($\text{U}_3\text{O}_8$) containing $1.000\text{ kg}$ of natural uranium ($99.274\%$ $^{238}\text{U}$, $T_{1/2} = 4.468 \times 10^9\text{ yr}$), all decay chain daughters reside in strict secular equilibrium.
Radium-226 ($^{226}\text{Ra}$, $T_{1/2} = 1600\text{ yr}$) is one of the intermediate alpha-emitting daughters in the uranium series.
1. Calculate the absolute activity of $^{238}\text{U}$ in the rock in $\text{MBq}$.
2. State the activity of $^{226}\text{Ra}$ in the rock.
3. Calculate the mass of $^{226}\text{Ra}$ present in milligrams ($\text{mg}$).""",
                    "solution": r"""### Step 1: Activity of $^{238}\text{U}$
Mass of $^{238}\text{U}$:
$$m = 1000\text{ g} \times 0.99274 = 992.74\text{ g}$$
Number of atoms:
$$N_{238} = \frac{992.74\text{ g}}{238.05\text{ g/mol}} \times 6.02214 \times 10^{23}\text{ mol}^{-1} \approx 2.5113 \times 10^{24}\text{ atoms}$$
Decay constant in $\text{s}^{-1}$:
$$T_{1/2} = 4.468 \times 10^9\text{ yr} \times 3.15576 \times 10^7\text{ s/yr} = 1.40999 \times 10^{17}\text{ s}$$
$$\lambda_{238} = \frac{\ln 2}{1.40999 \times 10^{17}\text{ s}} \approx 4.91597 \times 10^{-18}\text{ s}^{-1}$$
Activity:
$$A_{238} = \lambda_{238} N_{238} = (4.91597 \times 10^{-18}\text{ s}^{-1})(2.5113 \times 10^{24}) \approx 1.2345 \times 10^7\text{ Bq} = 12.35\text{ MBq}$$

### Step 2: Activity of $^{226}\text{Ra}$
In secular equilibrium, the activity of every radioactive member in an unbranched chain is identical:
$$A_{\text{Ra}} = A_{238} = 12.35\text{ MBq} \quad (0.334\text{ mCi})$$

### Step 3: Mass of $^{226}\text{Ra}$
From secular equilibrium relation:
$$\lambda_{\text{Ra}} N_{\text{Ra}} = \lambda_{238} N_{238} \implies N_{\text{Ra}} = N_{238} \frac{\lambda_{238}}{\lambda_{\text{Ra}}} = N_{238} \frac{T_{1/2,\text{Ra}}}{T_{1/2,238}}$$
$$N_{\text{Ra}} = (2.5113 \times 10^{24}) \times \frac{1600\text{ yr}}{4.468 \times 10^9\text{ yr}} \approx 8.993 \times 10^{17}\text{ atoms}$$
Mass of radium:
$$m_{\text{Ra}} = \frac{N_{\text{Ra}}}{N_A} \times M_{\text{Ra}} = \frac{8.993 \times 10^{17}}{6.02214 \times 10^{23}} \times 226.03\text{ g/mol} \approx 3.376 \times 10^{-4}\text{ g} = 0.338\text{ mg}$$
One metric ton ($1000\text{ kg}$) of uranium ore yields only $\approx 338\text{ milligrams}$ of radium (illustrating why the Curies had to process tons of pitchblende).""",
                    "hints": ["In secular equilibrium, A_parent = A_daughter.", "N_daughter / N_parent = T_half(daughter) / T_half(parent)."]
                },
                {
                    "id": "prob-3-3",
                    "problemNumber": "3.3",
                    "title": "Poisson Counting Statistics and Minimum Detectable Activity",
                    "difficulty": "Intermediate",
                    "statement": r"""A low-background proportional counter records gross counts from an environmental water sample over a counting period $t_g = 60.0\text{ min}$, registering $N_g = 1,440\text{ counts}$.
A blank background count accumulated over $t_b = 120.0\text{ min}$ registered $N_b = 1,800\text{ counts}$.
1. Calculate the gross count rate $R_g$ and background count rate $R_b$ in counts per minute (cpm).
2. Calculate the net count rate $R_n$ and its standard uncertainty $\sigma_{R_n}$ in cpm.
3. Compute the $95\%$ confidence interval ($1.96 \sigma$) for the net count rate.
4. If detector efficiency is $\epsilon = 0.350$ ($35\%$), calculate the sample activity in Becquerels (Bq).""",
                    "solution": r"""### Step 1: Gross and Background Count Rates
Gross count rate:
$$R_g = \frac{N_g}{t_g} = \frac{1440\text{ counts}}{60.0\text{ min}} = 24.00\text{ cpm}$$
Background count rate:
$$R_b = \frac{N_b}{t_b} = \frac{1800\text{ counts}}{120.0\text{ min}} = 15.00\text{ cpm}$$

### Step 2: Net Count Rate and Uncertainty
Net count rate:
$$R_n = R_g - R_b = 24.00 - 15.00 = 9.00\text{ cpm}$$
Uncertainty propagation:
$$\sigma_{R_n} = \sqrt{\frac{R_g}{t_g} + \frac{R_b}{t_b}} = \sqrt{\frac{24.00}{60.0} + \frac{15.00}{120.0}} = \sqrt{0.400 + 0.125} = \sqrt{0.525} \approx 0.7246\text{ cpm}$$
Result: $R_n = 9.00 \pm 0.72\text{ cpm}$.

### Step 3: 95% Confidence Interval
$$95\%\text{ CI} = R_n \pm 1.96 \sigma_{R_n} = 9.00 \pm (1.96 \times 0.7246) = 9.00 \pm 1.42\text{ cpm} \quad [7.58\text{ to }10.42\text{ cpm}]$$

### Step 4: Net Activity in Becquerels
Convert net rate to counts per second (cps):
$$R_n = \frac{9.00\text{ cpm}}{60\text{ s/min}} = 0.150\text{ cps}$$
Sample activity:
$$A = \frac{R_n}{\epsilon} = \frac{0.150\text{ cps}}{0.350\text{ cps/Bq}} \approx 0.4286\text{ Bq} \pm 0.035\text{ Bq}$$""",
                    "hints": ["Net count rate variance is R_g/t_g + R_b/t_b.", "Divide cpm by 60 to convert to disintegrations per second before dividing by efficiency."]
                },
                {
                    "id": "prob-3-4",
                    "problemNumber": "3.4",
                    "title": "Potassium-40 Dual Branching Decay and K-Ar Geochronology",
                    "difficulty": "Advanced",
                    "statement": r"""Potassium-40 ($^{40}\text{K}$) undergoes branched decay with a total half-life $T_{1/2,\text{tot}} = 1.248 \times 10^9\text{ yr}$:
- $89.28\%$ via $\beta^-$ to $^{40}\text{Ca}$ ($\lambda_\beta = 4.962 \times 10^{-10}\text{ yr}^{-1}$)
- $10.72\%$ via Electron Capture / $\beta^+$ to $^{40}\text{Ar}$ ($\lambda_{\text{EC}} = 5.960 \times 10^{-11}\text{ yr}^{-1}$)
A volcanic rock specimen contains $N_{\text{Ar}} = 3.50 \times 10^{15}\text{ atoms}$ of radiogenic $^{40}\text{Ar}$ and $N_{\text{K}} = 2.80 \times 10^{16}\text{ atoms}$ of $^{40}\text{K}$.
Assuming zero initial argon was trapped at solidification:
1. Derive the K-Ar age equation for $t$ in terms of $N_{\text{Ar}} / N_{\text{K}}$.
2. Calculate the geological age $t$ of the volcanic formation in millions of years (Ma).""",
                    "solution": r"""### Step 1: Derivation of K-Ar Age Equation
The accumulation rate of $^{40}\text{Ar}$ is:
$$N_{\text{Ar}}(t) = \frac{\lambda_{\text{EC}}}{\lambda_{\text{tot}}} N_{\text{K}}(0) (1 - e^{-\lambda_{\text{tot}} t})$$
The remaining potassium-40 atoms is:
$$N_{\text{K}}(t) = N_{\text{K}}(0) e^{-\lambda_{\text{tot}} t} \implies N_{\text{K}}(0) = N_{\text{K}}(t) e^{\lambda_{\text{tot}} t}$$
Substituting $N_{\text{K}}(0)$:
$$N_{\text{Ar}}(t) = \frac{\lambda_{\text{EC}}}{\lambda_{\text{tot}}} N_{\text{K}}(t) e^{\lambda_{\text{tot}} t} (1 - e^{-\lambda_{\text{tot}} t}) = \frac{\lambda_{\text{EC}}}{\lambda_{\text{tot}}} N_{\text{K}}(t) (e^{\lambda_{\text{tot}} t} - 1)$$
Dividing by $N_{\text{K}}(t)$:
$$\frac{N_{\text{Ar}}}{N_{\text{K}}} = \frac{\lambda_{\text{EC}}}{\lambda_{\text{tot}}} (e^{\lambda_{\text{tot}} t} - 1)$$
Solving for age $t$:
$$e^{\lambda_{\text{tot}} t} = 1 + \frac{\lambda_{\text{tot}}}{\lambda_{\text{EC}}} \left(\frac{N_{\text{Ar}}}{N_{\text{K}}}\right)$$
$$t = \frac{1}{\lambda_{\text{tot}}} \ln\left[ 1 + \frac{\lambda_{\text{tot}}}{\lambda_{\text{EC}}} \left(\frac{N_{\text{Ar}}}{N_{\text{K}}}\right) \right]$$

### Step 2: Numerical Age Calculation
Given parameters:
$$\lambda_{\text{tot}} = \lambda_\beta + \lambda_{\text{EC}} = 4.962 \times 10^{-10} + 5.960 \times 10^{-11} = 5.558 \times 10^{-10}\text{ yr}^{-1}$$
$$\frac{\lambda_{\text{tot}}}{\lambda_{\text{EC}}} = \frac{5.558 \times 10^{-10}}{5.960 \times 10^{-11}} \approx 9.3255$$
Atomic ratio:
$$\frac{N_{\text{Ar}}}{N_{\text{K}}} = \frac{3.50 \times 10^{15}}{2.80 \times 10^{16}} = 0.1250$$
Argument of logarithm:
$$1 + 9.3255 \times 0.1250 = 1 + 1.16569 = 2.16569$$
Calculate age $t$:
$$t = \frac{\ln(2.16569)}{5.558 \times 10^{-10}\text{ yr}^{-1}} = \frac{0.77274}{5.558 \times 10^{-10}} \approx 1.3903 \times 10^9\text{ yr} \approx 1,390\text{ Ma}$$
The rock solidified **$1.39\text{ billion years}$** ago.""",
                    "hints": ["Remember that Ar-40 is formed only via the EC channel with partial decay constant lambda_EC.", "Age formula has the factor lambda_tot / lambda_EC inside the logarithm."]
                },
                {
                    "id": "prob-3-5",
                    "problemNumber": "3.5",
                    "title": "Three-Nuclide Bateman Chain Activity Inventory",
                    "difficulty": "Advanced",
                    "statement": r"""Consider a three-member decay series:
$$N_1 \xrightarrow{\lambda_1 = 0.20\text{ h}^{-1}} N_2 \xrightarrow{\lambda_2 = 0.50\text{ h}^{-1}} N_3 \xrightarrow{\lambda_3 = 0.80\text{ h}^{-1}} N_4 \text{ (Stable)}$$
Initially at $t = 0$, pure parent nuclide is prepared with $N_1(0) = 1.00 \times 10^{12}\text{ atoms}$ and $N_2(0) = N_3(0) = 0$.
1. Write down the explicit Bateman expansion for $N_3(t)$.
2. Calculate the number of atoms $N_3$ and activity $A_3$ at $t = 2.0\text{ hours}$.""",
                    "solution": r"""### Step 1: Bateman Coefficients for $N_3(t)$
For $n = 3$, Bateman formula gives:
$$N_3(t) = N_1(0) \lambda_1 \lambda_2 \left[ \frac{e^{-\lambda_1 t}}{(\lambda_2 - \lambda_1)(\lambda_3 - \lambda_1)} + \frac{e^{-\lambda_2 t}}{(\lambda_1 - \lambda_2)(\lambda_3 - \lambda_2)} + \frac{e^{-\lambda_3 t}}{(\lambda_1 - \lambda_3)(\lambda_2 - \lambda_3)} \right]$$
Pre-factor:
$$N_1(0) \lambda_1 \lambda_2 = (1.00 \times 10^{12})(0.20)(0.50) = 1.00 \times 10^{11}$$
Denominators:
1. Term 1 ($j = 1$):
$$(\lambda_2 - \lambda_1)(\lambda_3 - \lambda_1) = (0.50 - 0.20)(0.80 - 0.20) = (0.30)(0.60) = 0.18$$
$$C_1 = \frac{1.00 \times 10^{11}}{0.18} \approx 5.5556 \times 10^{11}$$

2. Term 2 ($j = 2$):
$$(\lambda_1 - \lambda_2)(\lambda_3 - \lambda_2) = (0.20 - 0.50)(0.80 - 0.50) = (-0.30)(0.30) = -0.09$$
$$C_2 = \frac{1.00 \times 10^{11}}{-0.09} \approx -1.1111 \times 10^{12}$$

3. Term 3 ($j = 3$):
$$(\lambda_1 - \lambda_3)(\lambda_2 - \lambda_3) = (0.20 - 0.80)(0.50 - 0.80) = (-0.60)(-0.30) = +0.18$$
$$C_3 = \frac{1.00 \times 10^{11}}{0.18} \approx 5.5556 \times 10^{11}$$

Notice $C_1 + C_2 + C_3 = 5.5556 \times 10^{11} - 11.1111 \times 10^{11} + 5.5556 \times 10^{11} = 0$, satisfying $N_3(0) = 0$.

### Step 2: Evaluation at $t = 2.0\text{ h}$
$$e^{-\lambda_1 t} = e^{-0.20 \times 2} = e^{-0.40} \approx 0.67032$$
$$e^{-\lambda_2 t} = e^{-0.50 \times 2} = e^{-1.00} \approx 0.36788$$
$$e^{-\lambda_3 t} = e^{-0.80 \times 2} = e^{-1.60} \approx 0.20190$$

Substitute:
$$N_3(2) = 10^{11} \left[ \frac{0.67032}{0.18} - \frac{0.36788}{0.09} + \frac{0.20190}{0.18} \right] = 10^{11} [3.7240 - 4.0876 + 1.1217] = 10^{11} [0.7581] \approx 7.581 \times 10^{10}\text{ atoms}$$

Activity $A_3$ in Becquerels:
$$\lambda_3 = 0.80\text{ h}^{-1} = \frac{0.80}{3600\text{ s}} \approx 2.222 \times 10^{-4}\text{ s}^{-1}$$
$$A_3 = \lambda_3 N_3 = (2.222 \times 10^{-4}\text{ s}^{-1})(7.581 \times 10^{10}) \approx 1.685 \times 10^7\text{ Bq} = 16.85\text{ MBq}$$""",
                    "hints": ["The sum of Bateman coefficients C_1 + C_2 + C_3 must equal zero for N_3(0) = 0.", "Convert lambda_3 to s^-1 when computing activity in Becquerels."]
                },
                {
                    "id": "prob-3-6",
                    "problemNumber": "3.6",
                    "title": "Continuous Radionuclide Production Kinetics in Cyclotron Beam",
                    "difficulty": "Intermediate",
                    "statement": r"""A target is irradiated in a biomedical cyclotron to produce fluorine-18 ($^{18}\text{F}$, $T_{1/2} = 109.77\text{ min}$) via the $^{18}\text{O}(p, n)^{18}\text{F}$ nuclear reaction at a constant production rate $R = 2.50 \times 10^9\text{ atoms/s}$.
1. Formulate the differential rate equation for $^{18}\text{F}$ inventory during irradiation and derive $N(t)$ and $A(t)$.
2. Calculate the saturation activity $A_{\text{sat}}$ in $\text{GBq}$.
3. Calculate the activity produced after an irradiation time of $t = 2.00\text{ hours}$.
4. Determine the percentage of saturation achieved.""",
                    "solution": r"""### Step 1: Production Differential Rate Equation
During irradiation, atoms are generated at constant rate $R$ and simultaneously decay at rate $\lambda N$:
$$\frac{dN}{dt} = R - \lambda N \implies \frac{dN}{dt} + \lambda N = R$$
Using integrating factor $e^{\lambda t}$:
$$\frac{d}{dt}(N e^{\lambda t}) = R e^{\lambda t}$$
Integrating with $N(0) = 0$:
$$N(t) e^{\lambda t} = \frac{R}{\lambda}(e^{\lambda t} - 1) \implies N(t) = \frac{R}{\lambda}(1 - e^{-\lambda t})$$
The activity $A(t) = \lambda N(t)$ is:
$$A(t) = R (1 - e^{-\lambda t})$$

### Step 2: Saturation Activity $A_{\text{sat}}$
As $t \to \infty$, the decay rate exactly equals the production rate ($e^{-\lambda t} \to 0$):
$$A_{\text{sat}} = R = 2.50 \times 10^9\text{ Bq} = 2.50\text{ GBq} \quad (\sim 67.6\text{ mCi})$$

### Step 3: Activity After $t = 2.00\text{ hours}$
Convert half-life to hours:
$$T_{1/2} = \frac{109.77\text{ min}}{60\text{ min/h}} \approx 1.8295\text{ h}$$
$$\lambda = \frac{\ln 2}{1.8295\text{ h}} \approx 0.37887\text{ h}^{-1}$$
Saturation factor:
$$1 - e^{-\lambda t} = 1 - e^{-(0.37887 \times 2.00)} = 1 - e^{-0.75774} = 1 - 0.46872 = 0.53128$$
Activity:
$$A(2\text{ h}) = 2.50\text{ GBq} \times 0.53128 \approx 1.328\text{ GBq}$$

### Step 4: Percentage of Saturation
$$\% \text{ Saturation} = 53.13\%$$
After $\approx 1.1$ half-lives, over half of the maximum achievable activity has already been reached.""",
                    "hints": ["During constant production, activity approaches saturation according to A(t) = R*(1 - exp(-lambda*t)).", "Saturation activity in Bq equals the production rate R in atoms/s."]
                },
                {
                    "id": "prob-3-7",
                    "problemNumber": "3.7",
                    "title": "Decay Chain Daughter Growth with Non-Zero Initial Daughter Activity",
                    "difficulty": "Intermediate",
                    "statement": r"""A radionuclide generator container arrives at a hospital containing $^{131m}\text{Xe}$ ($T_{1/2,1} = 11.9\text{ days}$) which decays into ground-state $^{131}\text{Xe}$ or similar chain. Consider an idealized chain where parent $N_1$ ($T_{1/2,1} = 20.0\text{ h}$) decays to daughter $N_2$ ($T_{1/2,2} = 4.0\text{ h}$).
Due to incomplete prior separation, at $t = 0$ the daughter activity is not zero, with initial values:
$A_1(0) = 50.0\text{ MBq}$ and $A_2(0) = 15.0\text{ MBq}$.
1. Derive the general Bateman expression for $N_2(t)$ and $A_2(t)$ incorporating $N_2(0) \ne 0$.
2. Calculate the daughter activity $A_2$ at $t = 6.0\text{ hours}$.""",
                    "solution": r"""### Step 1: Derivation with Initial Daughter Population
The differential equation is:
$$\frac{dN_2}{dt} + \lambda_2 N_2 = \lambda_1 N_1(0) e^{-\lambda_1 t}$$
Integrating with integrating factor $e^{\lambda_2 t}$ from $N_2(0)$ to $N_2(t)$:
$$N_2(t) e^{\lambda_2 t} - N_2(0) = \frac{\lambda_1 N_1(0)}{\lambda_2 - \lambda_1}(e^{(\lambda_2 - \lambda_1) t} - 1)$$
$$N_2(t) = N_2(0) e^{-\lambda_2 t} + \frac{\lambda_1 N_1(0)}{\lambda_2 - \lambda_1}(e^{-\lambda_1 t} - e^{-\lambda_2 t})$$
Multiplying through by $\lambda_2$:
$$A_2(t) = A_2(0) e^{-\lambda_2 t} + \frac{\lambda_2}{\lambda_2 - \lambda_1} A_1(0) (e^{-\lambda_1 t} - e^{-\lambda_2 t})$$
This reflects linear superposition: independent exponential decay of initial daughter plus in-growth from parent decay.

### Step 2: Numerical Calculation at $t = 6.0\text{ h}$
Decay constants:
$$\lambda_1 = \frac{\ln 2}{20.0\text{ h}} = 0.034657\text{ h}^{-1}$$
$$\lambda_2 = \frac{\ln 2}{4.0\text{ h}} = 0.173287\text{ h}^{-1}$$
$$\lambda_2 - \lambda_1 = 0.173287 - 0.034657 = 0.138630\text{ h}^{-1}$$
$$\frac{\lambda_2}{\lambda_2 - \lambda_1} = \frac{0.173287}{0.138630} = 1.250$$

Exponentials at $t = 6.0\text{ h}$:
$$e^{-\lambda_1 t} = e^{-0.034657 \times 6} = e^{-0.20794} \approx 0.81225$$
$$e^{-\lambda_2 t} = e^{-0.173287 \times 6} = e^{-1.03972} \approx 0.35355$$

Compute components:
1. Residual initial daughter:
$$A_{2,\text{init}} = 15.0\text{ MBq} \times 0.35355 \approx 5.303\text{ MBq}$$

2. Growth from parent:
$$A_{2,\text{growth}} = 1.250 \times 50.0\text{ MBq} \times (0.81225 - 0.35355) = 62.5 \times 0.45870 \approx 28.669\text{ MBq}$$

Total daughter activity:
$$A_2(6\text{ h}) = 5.303 + 28.669 = 33.97\text{ MBq}$$""",
                    "hints": ["The solution is a linear sum of initial daughter decaying as exp(-lambda_2 * t) plus in-growth from parent.", "Calculate each term independently and sum."]
                }
            ]
        }
    ]
    return units

if __name__ == '__main__':
    u = get_units_1_2_3()
    print(f"Generated {len(u)} units.")
    for idx, unit in enumerate(u):
        print(f"Unit {unit['unitNumber']}: {unit['title']} -> {len(unit['sections'])} sections, {len(unit['problems'])} problems")
