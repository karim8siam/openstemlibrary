# build_plasma_units_1_2.py
# Generates plasma_u1.json and plasma_u2.json for Plasma Physics Course #17

import json

# =========================================================================
# UNIT 1: FOUNDATIONS OF PLASMA PHYSICS & DEBYE SHIELDING
# =========================================================================

unit1_data = {
    "unitId": "unit1-plasma",
    "title": "Foundations of Plasma Physics, Debye Shielding & Plasma Parameters",
    "subtitle": "Ionization, Debye Length, Plasma Frequency & Gas Discharges",
    "summary": "Comprehensive foundations of the fourth state of matter: natural occurrence and astrophysics, Saha ionization thermodynamics, Maxwellian velocity distributions and thermal velocity, temperature in electron-volts, Poisson's equation and the complete linearized spherical Debye shielding derivation, Debye length, the plasma parameter and the plasma approximation, criteria for plasma collective behavior, electron plasma frequency, DC glow discharges and the Townsend avalanche, Paschen breakdown curve, and magnetic/inertial confinement principles.",
    "sections": [
        {
            "id": "sec-1-1",
            "number": "1.1",
            "title": "Plasma as the Fourth State of Matter & Occurrence in Nature and Astrophysics",
            "content": """
<h3>1. The Fourth State of Matter</h3>
<p>
Matter transitions through distinct thermodynamic phases as thermal energy per particle increases: solid, liquid, gas, and ultimately <strong>plasma</strong>. In a solid, intermolecular Coulomb forces bind particles into rigid lattices. As thermal kinetic energy $k_B T$ exceeds binding energies, lattice bonds melt into disordered liquids, which subsequently vaporize into neutral molecular or atomic gases. When thermal kinetic energies reach or exceed the atomic ionization potential ($E_{\\text{ion}} \\sim 1\\text{ to }25\\text{ eV}$), collisions between neutral atoms strip orbital electrons, yielding an ensemble of freely moving negatively charged electrons and positively charged ions:
</p>
$$\\text{Solid} \\xrightarrow{\\Delta Q} \\text{Liquid} \\xrightarrow{\\Delta Q} \\text{Gas} \\xrightarrow{\\Delta Q} \\text{Plasma}$$
<p>
Unlike neutral gases governed by short-range Lennard-Jones intermolecular collisions, plasmas are dominated by long-range electromagnetic Coulomb interactions ($V(r) \\propto 1/r$). This imparts macroscopic collective behavior: a local charge displacement generates long-range electric and magnetic fields that instantaneously influence millions of surrounding particles simultaneously.
</p>

<h3>2. Ubiquity in the Observable Universe</h3>
<p>
Although plasmas are rare in everyday terrestrial conditions due to low ambient temperatures ($T \\sim 300\\text{ K} \\approx 0.025\\text{ eV}$) and atmospheric pressure, plasma constitutes more than <strong>99% of the visible baryonic matter</strong> in the universe:
</p>
<ul>
  <li><strong>Stellar Interiors and Atmospheres:</strong> The core of the Sun ($T_c \\approx 1.57 \\times 10^7\\text{ K}$, $n_e \\approx 10^{26}\\text{ cm}^{-3}$) is a completely ionized, dense electron-proton plasma undergoing thermonuclear $p$-$p$ fusion.</li>
  <li><strong>The Solar Wind:</strong> A continuous, supersonic, collisionless magnetized plasma flow ($n_e \\sim 5\\text{ cm}^{-3}$, $v_{\\text{sw}} \\sim 400\\text{ km/s}$) expanding through interplanetary space.</li>
  <li><strong>Planetary Ionospheres:</strong> Photoionization of upper atmospheric gases by solar extreme ultraviolet (EUV) and X-ray radiation produces the Earth's ionosphere ($h \\approx 60\\text{ to }1000\\text{ km}$, $n_e \\sim 10^4\\text{ to }10^6\\text{ cm}^{-3}$).</li>
  <li><strong>Astrophysical Jets and Interstellar Medium (ISM):</strong> Relativistic synchrotron-emitting plasma jets ejected by active galactic nuclei (AGN) and microquasars, as well as the diffuse warm ionized interstellar medium.</li>
</ul>
"""
        },
        {
            "id": "sec-1-2",
            "number": "1.2",
            "title": "Thermodynamics of Ionization & The Saha Ionization Equation",
            "content": """
<h3>1. Thermal Ionization Equilibrium</h3>
<p>
Consider a neutral gas of atoms $A$ at absolute temperature $T$ undergoing reversible thermal ionization:
</p>
$$A + \\Delta E \\rightleftharpoons A^+ + e^-$$
<p>
where $\\chi_i$ is the first ionization potential of the atom (e.g., $13.6\\text{ eV}$ for hydrogen). At thermodynamic equilibrium, the chemical potentials satisfy $\\mu_A = \\mu_{A^+} + \\mu_e$. Applying quantum statistical mechanics through the grand canonical partition function yields the <strong>Saha ionization equation</strong>:
</p>
$$\\frac{n_i n_e}{n_n} = \\frac{2 g_i}{g_n} \\left( \\frac{2\\pi m_e k_B T}{h^2} \\right)^{3/2} \\exp\\left( -\\frac{\\chi_i}{k_B T} \\right)$$
<p>
where $n_i$, $n_e$, and $n_n$ are the number densities of ions, electrons, and neutral atoms; $g_i$ and $g_n$ are the statistical degeneracy weights of the ion and neutral ground states; and the factor of 2 accounts for the two spin orientations of the free electron.
</p>

<h3>2. The Fractional Degree of Ionization</h3>
<p>
Defining the degree of ionization $\\alpha \\equiv \\frac{n_i}{n_i + n_n} = \\frac{n_e}{n_0}$, where $n_0 = n_i + n_n$ is the total heavy particle density, and assuming pure hydrogen ($g_i = 1, g_n = 2, n_e = n_i$):
</p>
$$\\frac{\\alpha^2}{1 - \\alpha} = \\frac{1}{n_0} \\left( \\frac{2\\pi m_e k_B T}{h^2} \\right)^{3/2} \\exp\\left( -\\frac{\\chi_i}{k_B T} \\right)$$
<p>
Because the quantum density of states prefactor $(2\\pi m_e k_B T / h^2)^{3/2} \\sim 10^{21}\\text{ cm}^{-3} \\text{ at } 1\\text{ eV}$ is colossal, a gas transitions abruptly from nearly neutral ($\alpha \\ll 1$) to fully ionized ($\alpha \\to 1$) at temperatures far below the ionization potential—typically when $k_B T \\approx \\chi_i / 10$.
</p>
"""
        },
        {
            "id": "sec-1-3",
            "number": "1.3",
            "title": "Kinetic Temperature, Maxwellian Velocity Distributions & Electron-Volts",
            "content": """
<h3>1. Maxwell-Boltzmann Velocity Distribution</h3>
<p>
In thermal equilibrium, particles of species $\\alpha$ (mass $m_\\alpha$, temperature $T_\\alpha$) possess a three-dimensional Maxwellian distribution of velocities:
</p>
$$f_\\alpha(\\vec{v}) = n_\\alpha \\left( \\frac{m_\\alpha}{2\\pi k_B T_\\alpha} \\right)^{3/2} \\exp\\left( -\\frac{m_\\alpha v^2}{2 k_B T_\\alpha} \\right)$$
<p>
The root-mean-square thermal speed $v_{\\text{th},\\alpha}$ in one dimension and three dimensions is defined by:
</p>
$$v_{\\text{th},\\alpha}^{(1D)} = \\sqrt{\\frac{k_B T_\\alpha}{m_\\alpha}}, \\quad v_{\\text{th},\\alpha}^{(3D)} = \\sqrt{\\frac{3 k_B T_\\alpha}{m_\\alpha}}$$

<h3>2. Temperature Units in Electron-Volts</h3>
<p>
In plasma physics, thermal energy is universally expressed in <strong>electron-volts (eV)</strong> rather than Kelvin, representing the kinetic energy an electron gains accelerating across a potential of 1 Volt:
</p>
$$1\\text{ eV} = e \\times 1\\text{ V} = 1.6022 \\times 10^{-19}\\text{ Joules}$$
<p>
Setting $k_B T = 1\\text{ eV}$, where $k_B = 1.3807 \\times 10^{-23}\\text{ J/K}$:
</p>
$$T = \\frac{1.6022 \\times 10^{-19}\\text{ J}}{1.3807 \\times 10^{-23}\\text{ J/K}} \\approx 11,604.5\\text{ K} \\approx 11,600\\text{ K}$$
<p>
Thus, a room temperature plasma of $300\\text{ K}$ corresponds to $k_B T \\approx 0.026\\text{ eV}$, whereas magnetic fusion tokamak plasmas operate at $10\\text{ to }20\\text{ keV} \\approx 1.16 \\times 10^8\\text{ to }2.32 \\times 10^8\\text{ K}$.
</p>

<h3>3. Multi-Temperature Plasmas</h3>
<p>
Because the electron-to-ion mass ratio is minuscule ($m_e / M_i \\approx 1/1836$ for protons), collisional kinetic energy transfer between electrons and ions is inefficient by a factor of $m_e / M_i$. Consequently, laboratory plasmas frequently sustain separate thermodynamic temperatures for electrons and ions over long time scales:
</p>
$$T_e \\ne T_i$$
<p>
In typical low-pressure glow discharges, electrons are efficiently heated by RF or DC electric fields ($T_e \\sim 2\\text{ to }5\\text{ eV} \\approx 23,000\\text{ to }58,000\\text{ K}$), while heavy ions remain in thermal equilibrium with the background neutral gas ($T_i \\approx T_n \\sim 0.03\\text{ eV} \\approx 350\\text{ K}$).
</p>
"""
        },
        {
            "id": "sec-1-4",
            "number": "1.4",
            "title": "Quasi-Neutrality & Derivation of the Linearized Debye Shielding Potential",
            "content": """
<h3>1. Quasi-Neutrality</h3>
<p>
In the absence of external perturbations, the number density of electrons $n_e$ matches the number density of ions $n_i$ multiplied by ionic charge state $Z$:
</p>
$$n_e \\approx Z n_i \\equiv n_0$$
<p>
This condition is termed <strong>quasi-neutrality</strong>: the plasma is neutral on macroscopic spatial scales ($L \\gg \\lambda_D$), but local microscopic charge separations readily occur over small distances.
</p>

<h3>2. Derivation of the Debye Shielding Potential</h3>
<p>
Suppose a positive test charge $+Q$ is introduced at the origin $\\vec{r} = 0$ inside an initially uniform plasma of background density $n_0$. The test charge polarizes the surrounding plasma: mobile electrons are attracted toward the test charge, while massive positive ions are repelled.
</p>
<p>
The electrostatic potential $\\phi(r)$ is governed by Poisson's equation:
</p>
$$\\nabla^2 \\phi = -\\frac{\\rho_q}{\\varepsilon_0} = -\\frac{e(n_i - n_e) + Q\\delta(\\vec{r})}{\\varepsilon_0}$$
<p>
Assuming the electrons are in isothermal thermodynamic equilibrium at temperature $T_e$, their number density obeys the Boltzmann distribution:
</p>
$$n_e(r) = n_0 \\exp\\left( \\frac{e\\phi(r)}{k_B T_e} \\right)$$
<p>
Because ions are heavy and immobile on electron response timescales, we take $n_i(r) \\approx n_0$ (or $n_i = n_0 \\exp(-e\\phi/k_B T_i)$ if ions also reach equilibrium). In the weak-field approximation, the electrostatic potential energy is much smaller than the thermal kinetic energy ($e\\phi \\ll k_B T_e$). Taylor expanding the exponential to first order:
</p>
$$n_e(r) \\approx n_0 \\left( 1 + \\frac{e\\phi(r)}{k_B T_e} \\right)$$
<p>
Substituting this expansion into Poisson's equation for $r > 0$:
</p>
$$\\nabla^2 \\phi = -\\frac{e}{\\varepsilon_0} \\left[ n_0 - n_0\\left(1 + \\frac{e\\phi}{k_B T_e}\\right) \\right] = \\frac{n_0 e^2}{\\varepsilon_0 k_B T_e} \\phi$$
<p>
Defining the <strong>Debye length</strong> $\\lambda_D$ (or $\\lambda_{De}$):
</p>
$$\\lambda_D \\equiv \\sqrt{\\frac{\\varepsilon_0 k_B T_e}{n_0 e^2}}$$
<p>
Poisson's equation reduces to the Helmholtz-type screening equation:
</p>
$$\\nabla^2 \\phi - \\frac{1}{\\lambda_D^2}\\phi = 0$$
<p>
In spherically symmetric coordinates where $\\nabla^2 \\phi = \\frac{1}{r}\\frac{d^2}{dr^2}(r\\phi)$:
</p>
$$\\frac{d^2}{dr^2}(r\\phi) = \\frac{r\\phi}{\\lambda_D^2} \\implies r\\phi(r) = A e^{-r/\\lambda_D} + B e^{+r/\\lambda_D}$$
<p>
To satisfy the boundary condition that the potential vanishes as $r \\to \\infty$, we require $B = 0$. As $r \\to 0$, the potential must approach the unshielded Coulomb potential of the point charge $Q$:
</p>
$$\\lim_{r\\to 0} \\phi(r) = \\frac{Q}{4\\pi\\varepsilon_0 r} \\implies A = \\frac{Q}{4\\pi\\varepsilon_0}$$
<p>
Therefore, the shielded electrostatic potential is the classic <strong>Debye-Hückel (Yukawa) potential</strong>:
</p>
$$\\phi(r) = \\frac{Q}{4\\pi\\varepsilon_0 r} \\exp\\left( -\\frac{r}{\\lambda_D} \\right)$$
<p>
The exponential damping factor $\\exp(-r/\\lambda_D)$ effectively screens the Coulomb field of any charge within a few Debye lengths, shielding the bulk plasma from external electrostatic intrusions.
</p>
"""
        },
        {
            "id": "sec-1-5",
            "number": "1.5",
            "title": "The Plasma Parameter, Collective Behavior & The Three Criteria for Plasma",
            "content": """
<h3>1. The Plasma Parameter & Debye Sphere</h3>
<p>
A sphere of radius equal to the Debye length centered on any particle is termed the <strong>Debye sphere</strong>. The number of electrons enclosed within this shielding sphere is defined by the <strong>plasma parameter</strong> $N_D$:
</p>
$$N_D \\equiv \\frac{4}{3}\\pi n_e \\lambda_D^3 = \\frac{4}{3}\\pi n_e \\left( \\frac{\\varepsilon_0 k_B T_e}{n_e e^2} \\right)^{3/2} = \\frac{4\\pi}{3} \\frac{(\\varepsilon_0 k_B T_e)^{3/2}}{e^3 n_e^{1/2}}$$
<p>
For Debye shielding to be statistically valid, there must be a vast number of particles available to participate in the screening cloud. This leads to the fundamental condition:
</p>
$$N_D \\gg 1$$
<p>
When $N_D \\gg 1$, collective long-range interactions dominate over discrete binary electron-ion collisions. The ratio of the average Coulomb potential energy between nearest neighbors ($E_{\\text{pot}} \\sim e^2 / (4\\pi\\varepsilon_0 r_{\\text{avg}})$ where $r_{\\text{avg}} \\sim n_e^{-1/3}$) to average thermal kinetic energy $k_B T_e$ is related to $N_D$ by:
</p>
$$\\frac{\\langle E_{\\text{pot}} \\rangle}{\\langle E_{\\text{kin}} \\rangle} \\sim \\frac{1}{N_D^{2/3}} \\ll 1$$
<p>
Thus, plasmas with $N_D \\gg 1$ are weakly coupled, nearly ideal gas-like thermodynamic systems.
</p>

<h3>2. The Three Fundamental Criteria for Plasma</h3>
<p>
An ionized gas qualifies as a true physical plasma if and only if it satisfies three strict criteria:
</p>
<ol>
  <li><strong>Spatial Scale Criterion (Debye Shielding):</strong> The macroscopic physical dimensions $L$ of the system must be much larger than the Debye length:
  $$\\lambda_D \\ll L$$
  This ensures that boundary surface charges do not penetrate into the bulk plasma, allowing quasi-neutrality to hold over the bulk interior.</li>
  <li><strong>Collective Behavior Criterion (Plasma Parameter):</strong> The number of particles in a Debye sphere must be much greater than unity:
  $$N_D = \\frac{4}{3}\\pi n_e \\lambda_D^3 \\gg 1$$
  This guarantees that collective shielding is a smooth statistical phenomenon rather than a fluctuating binary interaction.</li>
  <li><strong>Dynamic Collisionless Criterion (Plasma Frequency vs Collisions):</strong> The characteristic electron plasma oscillation frequency $\\omega_{pe}$ must exceed the electron-neutral collision frequency $\\nu_{en}$:
  $$\\omega_{pe} \\tau_{\\text{coll}} > 1 \\iff \\omega_{pe} > \\nu_{en}$$
  where $\\tau_{\\text{coll}} = 1/\\nu_{en}$ is the mean time between collisions. This ensures that electrostatic collective oscillations can complete multiple cycles before being damped out by collisional friction with neutrals.</li>
</ol>
"""
        },
        {
            "id": "sec-1-6",
            "number": "1.6",
            "title": "High-Frequency Collective Dynamics: Electron Plasma Oscillations & Plasma Frequency",
            "content": """
<h3>1. Mechanism of Plasma Oscillations</h3>
<p>
Consider a uniform slab of cold, quasi-neutral plasma ($n_e = n_i = n_0$). Suppose all electrons in a slab of thickness $L$ are displaced by a small macroscopic distance $\\delta x$ along the $x$-axis, while the heavy ions remain stationary.
</p>
<p>
This displacement creates two unneutralized surface charge sheets at the boundaries: a positive surface charge density $\\sigma = +n_0 e \\delta x$ at $x = 0$, and a negative surface charge density $\\sigma = -n_0 e \\delta x$ at $x = L$. By Gauss's law, this charge separation establishes an internal restoring electric field:
</p>
$$E_x = -\\frac{\\sigma}{\\varepsilon_0} = -\\frac{n_0 e \\delta x}{\\varepsilon_0}$$

<h3>2. Equation of Motion & Electron Plasma Frequency</h3>
<p>
Each displaced electron experiences the electrostatic restoring force $F_x = -e E_x$:
</p>
$$m_e \\frac{d^2(\\delta x)}{dt^2} = -e E_x = -\\frac{n_0 e^2}{\\varepsilon_0} \\delta x$$
<p>
This is the differential equation of a simple harmonic oscillator:
</p>
$$\\frac{d^2(\\delta x)}{dt^2} + \\omega_{pe}^2 (\\delta x) = 0$$
<p>
where the natural resonant frequency of oscillation is the <strong>electron plasma frequency</strong> $\\omega_{pe}$:
</p>
$$\\omega_{pe} = \\sqrt{\\frac{n_0 e^2}{\\varepsilon_0 m_e}}$$
<p>
In practical numerical units with $n_e$ expressed in $\\text{m}^{-3}$ and $f_{pe} = \\omega_{pe} / (2\\pi)$ in Hz:
</p>
$$f_{pe} \\approx 8.98 \\sqrt{n_e [\\text{m}^{-3}]}\\text{ Hz} \\approx 8980 \\sqrt{n_e [\\text{cm}^{-3}]}\\text{ Hz}$$
<p>
The electron plasma frequency represents the fastest fundamental collective response time ($\tau_{pe} = 2\\pi / \\omega_{pe}$) of the plasma. Perturbations slower than $\\omega_{pe}$ are dynamically shielded by mobile electrons, whereas high-frequency electromagnetic waves ($\omega > \\omega_{pe}$) can propagate through the plasma without being reflected.
</p>
"""
        },
        {
            "id": "sec-1-7",
            "number": "1.7",
            "title": "Laboratory Plasma Production: DC Glow Discharges, Townsend Avalanches & The Paschen Curve",
            "content": """
<h3>1. Townsend Avalanche Ionization</h3>
<p>
In laboratory gas discharge tubes, plasma is initiated by applying a high voltage potential difference $V$ across two planar electrodes separated by distance $d$ in a neutral gas at pressure $p$. A stray electron created by background cosmic rays accelerates in the electric field $E = V/d$. If its kinetic energy exceeds the ionization potential $\\chi_i$, an inelastic impact ionization occurs:
</p>
$$e^- + A \\to A^+ + 2e^-$$
<p>
The rate of electron multiplication per unit length is defined by <strong>Townsend's first ionization coefficient</strong> $\\alpha$:
</p>
$$\\frac{dn_e}{dx} = \\alpha n_e \\implies n_e(x) = n_{e0} \\exp(\\alpha x)$$
<p>
As positive ions drift back toward the cathode, their impact ejects secondary electrons with probability $\\gamma$ (Townsend's second ionization coefficient). The steady-state cathode-to-anode current density is:
</p>
$$J = J_0 \\frac{e^{\\alpha d}}{1 - \\gamma(e^{\\alpha d} - 1)}$$
<p>
Self-sustained electrical breakdown occurs when the denominator vanishes:
</p>
$$\\gamma(e^{\\alpha d} - 1) = 1 \\implies \\alpha d = \\ln\\left( 1 + \\frac{1}{\\gamma} \\right)$$

<h3>2. The Paschen Breakdown Law</h3>
<p>
Semi-empirically, Townsend's coefficient is given by $\\alpha / p = A \\exp(-B p / E)$. Substituting $E = V / d$:
</p>
$$\\alpha d = A p d \\exp\\left( -\\frac{B p d}{V} \\right)$$
<p>
Setting this equal to the breakdown threshold yields the famous <strong>Paschen breakdown equation</strong> for breakdown voltage $V_B$:
</p>
$$V_B = \\frac{B (p\\cdot d)}{\\ln\\left(\\frac{A (p\\cdot d)}{\\ln(1 + 1/\\gamma)}\\right)}$$
<p>
Plotting $V_B$ versus the product $p\\cdot d$ reveals the classic <strong>Paschen curve</strong>:
</p>
<ul>
  <li><strong>High $p\\cdot d$ branch:</strong> Frequent collisions damp electron energy; high voltage is required to achieve ionizing speeds between mean free paths.</li>
  <li><strong>Low $p\\cdot d$ branch:</strong> Gas density is too low; electrons traverse the gap without colliding with neutral atoms, necessitating massive voltages to spark breakdown.</li>
  <li><strong>Paschen Minimum $(p\\cdot d)_{\\text{min}}$:</strong> An optimal product (typically $\\sim 1\\text{ to }10\\text{ Torr}\\cdot\\text{cm}$) where the breakdown voltage reaches a global minimum $V_{B,\\text{min}}$ (typically $\\sim 100\\text{ to }300\\text{ V}$).</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-1-1",
            "title": "Rigorous Spherical Poisson-Boltzmann Derivation of Debye Screening Potential and Shielding Cloud Charge",
            "statement": """A point test charge $+Q$ is immersed at the origin $\\vec{r}=0$ within an infinite, homogeneous, unmagnetized electron-proton plasma ($Z=1$) with unperturbed density $n_0$ and electron temperature $T_e$. Assume the ions form a uniform neutralizing background ($n_i = n_0$).
(a) Formulate the exact nonlinear Poisson-Boltzmann equation for the electrostatic potential $\\phi(r)$ and state the physical condition required for linearization.
(b) Solve the linearized equation subject to regular boundary conditions at $r \\to 0$ and $r \\to \\infty$, deriving the Debye-Hückel potential $\\phi(r) = \\frac{Q}{4\\pi\\varepsilon_0 r}e^{-r/\\lambda_D}$.
(c) Calculate the net induced charge $Q_{\\text{cloud}}$ residing in the surrounding electron shielding cloud from $r=0$ to $r\\to\\infty$, and prove that the test charge is perfectly neutralized macroscopically.""",
            "solution": """**(a) Formulation of the Nonlinear Poisson-Boltzmann Equation:**
The electrostatic potential $\\phi(r)$ satisfies Poisson's equation:
$$\\nabla^2 \\phi = -\\frac{\\rho_q}{\\varepsilon_0} = -\\frac{e(n_i - n_e)}{\\varepsilon_0}$$
Assuming the electrons are in isothermal thermodynamic equilibrium at temperature $T_e$, their density follows the Boltzmann distribution:
$$n_e(r) = n_0 \\exp\\left( \\frac{e\\phi(r)}{k_B T_e} \\right)$$
With fixed background ions $n_i = n_0$:
$$\\nabla^2 \\phi(r) = \\frac{e n_0}{\\varepsilon_0}\\left[ \\exp\\left( \\frac{e\\phi(r)}{k_B T_e} \\right) - 1 \\right]$$
Linearization is strictly valid when the electrostatic potential energy is much smaller than the average thermal kinetic energy:
$$\\frac{e\\phi(r)}{k_B T_e} \\ll 1$$
Taylor expanding $\\exp(x) \\approx 1 + x + \\mathcal{O}(x^2)$ yields:
$$\\nabla^2 \\phi(r) = \\frac{e n_0}{\\varepsilon_0}\\left[ 1 + \\frac{e\\phi}{k_B T_e} - 1 \\right] = \\frac{n_0 e^2}{\\varepsilon_0 k_B T_e}\\phi(r) = \\frac{1}{\\lambda_D^2}\\phi(r)$$
where $\\lambda_D = \\sqrt{\\frac{\\varepsilon_0 k_B T_e}{n_0 e^2}}$ is the Debye length.

**(b) Spherical Solution:**
In spherical polar coordinates with radial symmetry:
$$\\frac{1}{r}\\frac{d^2}{dr^2}(r\\phi) = \\frac{1}{\\lambda_D^2}\\phi \\implies \\frac{d^2}{dr^2}(r\\phi) - \\frac{1}{\\lambda_D^2}(r\\phi) = 0$$
The general solution for the auxiliary variable $u(r) = r\\phi(r)$ is:
$$u(r) = C_1 e^{-r/\\lambda_D} + C_2 e^{+r/\\lambda_D} \\implies \\phi(r) = \\frac{C_1}{r}e^{-r/\\lambda_D} + \\frac{C_2}{r}e^{+r/\\lambda_D}$$
Boundary conditions:
1. As $r \\to \\infty$, the potential must remain finite and decay to zero: this requires $C_2 = 0$.
2. As $r \\to 0$, the screening effect becomes negligible and $\\phi(r)$ must approach the bare Coulomb potential $\\phi_{\\text{bare}}(r) = \\frac{Q}{4\\pi\\varepsilon_0 r}$:
$$\\lim_{r\\to 0} \\phi(r) = \\lim_{r\\to 0} \\frac{C_1}{r}e^{-r/\\lambda_D} = \\frac{C_1}{r} = \\frac{Q}{4\\pi\\varepsilon_0 r} \\implies C_1 = \\frac{Q}{4\\pi\\varepsilon_0}$$
Therefore, the shielded Debye-Hückel potential is:
$$\\phi(r) = \\frac{Q}{4\\pi\\varepsilon_0 r} \\exp\\left( -\\frac{r}{\\lambda_D} \\right)$$

**(c) Net Induced Shielding Cloud Charge:**
The induced charge density in the electron cloud is:
$$\\rho_{\\text{ind}}(r) = -e(n_e - n_0) \\approx -e n_0 \\left(\\frac{e\\phi(r)}{k_B T_e}\\right) = -\\varepsilon_0 \\frac{1}{\\lambda_D^2}\\phi(r) = -\\frac{Q}{4\\pi \\lambda_D^2 r}e^{-r/\\lambda_D}$$
The total charge contained within the spherical shielding cloud from $r = 0$ to $r \\to \\infty$ is obtained by integrating over all space:
$$Q_{\\text{cloud}} = \\int_0^\\infty \\rho_{\\text{ind}}(r) 4\\pi r^2 dr = -\\int_0^\\infty \\frac{Q}{4\\pi \\lambda_D^2 r}e^{-r/\\lambda_D} 4\\pi r^2 dr$$
$$Q_{\\text{cloud}} = -\\frac{Q}{\\lambda_D^2} \\int_0^\\infty r e^{-r/\\lambda_D} dr$$
Evaluating the definite integral using integration by parts $\\int_0^\\infty x e^{-a x} dx = \\frac{1}{a^2}$:
$$\\int_0^\\infty r e^{-r/\\lambda_D} dr = \\lambda_D^2$$
Substituting this result:
$$Q_{\\text{cloud}} = -\\frac{Q}{\\lambda_D^2} (\\lambda_D^2) = -Q$$
The total net charge of the system (test charge + shielding cloud) is:
$$Q_{\\text{total}} = Q + Q_{\\text{cloud}} = Q - Q = 0$$
This rigorously proves that the test charge is **100% neutralized** by the surrounding polarization cloud for any observer situated at distances $r \\gg \\lambda_D$."""
        },
        {
            "id": "plasma-prob-1-2",
            "title": "Exact Numerical Calculation of Plasma Parameter, Debye Length, and Plasma Frequency for Fusion Tokamak vs Ionosphere",
            "statement": """Compare the fundamental plasma characteristics of two representative systems:
1. **Magnetic Confinement Fusion Tokamak Core:** $n_e = 1.0 \\times 10^{20}\\text{ m}^{-3}$, $k_B T_e = 10.0\\text{ keV}$.
2. **Earth's Ionospheric F-Layer:** $n_e = 1.0 \\times 10^{12}\\text{ m}^{-3}$, $k_B T_e = 0.15\\text{ eV}$ ($T_e \\approx 1740\\text{ K}$).
For both regimes, compute:
(a) The Debye shielding length $\\lambda_D$.
(b) The plasma parameter $N_D$ (number of particles in a Debye sphere).
(c) The electron plasma frequency $f_{pe} = \\omega_{pe} / (2\\pi)$ in Hz.
(d) Verify whether both regimes satisfy the criteria for true collective plasma behavior.""",
            "solution": """**(a) Debye Shielding Length $\\lambda_D$:**
The formula for the Debye length is:
$$\\lambda_D = \\sqrt{\\frac{\\varepsilon_0 k_B T_e}{n_e e^2}}$$
Using fundamental constants: $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$, $e = 1.6022 \\times 10^{-19}\\text{ C}$.
Writing $k_B T_e = (k_B T_e)_{[\\text{eV}]} \\times e$:
$$\\lambda_D = \\sqrt{\\frac{\\varepsilon_0 (k_B T_e)_{[\\text{eV}]}}{n_e e}} = 7434 \\times \\sqrt{\\frac{(k_B T_e)_{[\\text{eV}]}}{n_e [\\text{m}^{-3}]}}\\text{ meters}$$

1. **Tokamak Core:** $(k_B T_e = 10^4\\text{ eV}$, $n_e = 10^{20}\\text{ m}^{-3}$):
$$\\lambda_D = \\sqrt{\\frac{(8.854\\times 10^{-12})(10^4 \\times 1.6022\\times 10^{-19})}{(10^{20})(1.6022\\times 10^{-19})^2}} = \\sqrt{\\frac{1.4186\\times 10^{-26}}{2.567\\times 10^{-18}}} = \\sqrt{5.526\\times 10^{-9}}\\text{ m}$$
$$\\lambda_{D,\\text{toka}} = 7.43 \\times 10^{-5}\\text{ m} = 74.3\\;\\mu\\text{m}$$

2. **Ionospheric F-Layer:** $(k_B T_e = 0.15\\text{ eV}$, $n_e = 10^{12}\\text{ m}^{-3}$):
$$\\lambda_{D,\\text{iono}} = \\sqrt{\\frac{(8.854\\times 10^{-12})(0.15 \\times 1.6022\\times 10^{-19})}{(10^{12})(1.6022\\times 10^{-19})^2}} = \\sqrt{\\frac{2.128\\times 10^{-31}}{2.567\\times 10^{-26}}} = \\sqrt{8.29\\times 10^{-6}}\\text{ m}$$
$$\\lambda_{D,\\text{iono}} = 2.88 \\times 10^{-3}\\text{ m} = 2.88\\text{ mm}$$

**(b) Plasma Parameter $N_D$:**
$$N_D = \\frac{4}{3}\\pi n_e \\lambda_D^3$$
1. **Tokamak Core:**
$$N_{D,\\text{toka}} = \\frac{4}{3}\\pi (10^{20}\\text{ m}^{-3})(7.434\\times 10^{-5}\\text{ m})^3 = \\frac{4}{3}\\pi (10^{20})(4.108\\times 10^{-13}) = 1.72 \\times 10^8$$
2. **Ionospheric F-Layer:**
$$N_{D,\\text{iono}} = \\frac{4}{3}\\pi (10^{12}\\text{ m}^{-3})(2.88\\times 10^{-3}\\text{ m})^3 = \\frac{4}{3}\\pi (10^{12})(2.389\\times 10^{-8}) = 1.00 \\times 10^5$$

**(c) Electron Plasma Frequency $f_{pe}$:**
$$f_{pe} = \\frac{1}{2\\pi}\\sqrt{\\frac{n_e e^2}{\\varepsilon_0 m_e}} \\approx 8.98\\sqrt{n_e [\\text{m}^{-3}]}\\text{ Hz}$$
Using $m_e = 9.109 \\times 10^{-31}\\text{ kg}$:
1. **Tokamak Core:**
$$f_{pe,\\text{toka}} = 8.98\\sqrt{10^{20}} = 8.98 \\times 10^{10}\\text{ Hz} = 89.8\\text{ GHz}$$
2. **Ionospheric F-Layer:**
$$f_{pe,\\text{iono}} = 8.98\\sqrt{10^{12}} = 8.98 \\times 10^6\\text{ Hz} = 8.98\\text{ MHz}$$

**(d) Verification of Plasma Criteria:**
- **Tokamak:** Typical machine scale $L \\sim 2\\text{ m} \\gg \\lambda_D = 74.3\\;\\mu\\text{m}$; $N_D = 1.72\\times 10^8 \\gg 1$; collision frequency $\\nu_{ei} \\sim 10^4\\text{ s}^{-1} \\ll \\omega_{pe} \\approx 5.6\\times 10^{11}\\text{ rad/s}$. All three criteria rigorously satisfied!
- **Ionosphere:** Scale $L \\sim 100\\text{ km} \\gg \\lambda_D = 2.88\\text{ mm}$; $N_D = 1.0\\times 10^5 \\gg 1$; $\\omega_{pe} \\approx 5.6\\times 10^7\\text{ rad/s} \\gg \\nu_{en} \\sim 10^2\\text{ s}^{-1}$. Both qualify definitively as collective plasmas."""
        },
        {
            "id": "plasma-prob-1-3",
            "title": "Analytical Minimum Breakdown Voltage Derivation from the Paschen Equation and Townsend Ionization Coefficients",
            "statement": """The Paschen law relates the DC electrical breakdown voltage $V_B$ of a planar gas gap to the product of gas pressure $p$ and electrode separation $d$:
$$V_B(p\\cdot d) = \\frac{B (p\\cdot d)}{\\ln\\left[ \\frac{A (p\\cdot d)}{\\ln(1 + 1/\\gamma)} \\right]}$$
where $A$ and $B$ are gas-specific Townsend constants, and $\\gamma$ is the secondary electron emission coefficient of the cathode.
(a) Analytically differentiate $V_B$ with respect to the variable $x \\equiv p\\cdot d$ to determine the exact location of the Paschen minimum $(p\\cdot d)_{\\text{min}}$.
(b) Evaluate the absolute minimum breakdown voltage $V_{B,\\text{min}}$ in terms of $A, B$, and $\\gamma$.
(c) For air with parameters $A = 15.0\\text{ cm}^{-1}\\cdot\\text{Torr}^{-1}$, $B = 365\\text{ V}\\cdot\\text{cm}^{-1}\\cdot\\text{Torr}^{-1}$, and cathode emission coefficient $\\gamma = 0.01$, calculate numerical values for $(p\\cdot d)_{\\text{min}}$ and $V_{B,\\text{min}}$.""",
            "solution": """**(a) Location of Paschen Minimum:**
Let $x = p\\cdot d$ and define the constant $C \\equiv \\ln(1 + 1/\\gamma)$. The Paschen equation becomes:
$$V_B(x) = \\frac{B x}{\\ln(A x / C)} = \\frac{B x}{\\ln(A x) - \\ln C}$$
To find the extremum, differentiate $V_B(x)$ with respect to $x$ using the quotient rule:
$$\\frac{dV_B}{dx} = \\frac{B \\cdot [\\ln(Ax/C)] - B x \\cdot \\left[\\frac{1}{Ax/C} \\cdot \\frac{A}{C}\\right]}{[\\ln(Ax/C)]^2} = \\frac{B \\left[ \\ln(Ax/C) - 1 \\right]}{[\\ln(Ax/C)]^2}$$
Setting the derivative to zero $\\frac{dV_B}{dx} = 0$:
$$\\ln\\left( \\frac{A x}{C} \\right) - 1 = 0 \\implies \\ln\\left( \\frac{A x}{C} \\right) = 1 \\implies \\frac{A x}{C} = e$$
Solving for $x = (p\\cdot d)_{\\text{min}}$:
$$(p\\cdot d)_{\\text{min}} = \\frac{e C}{A} = \\frac{e \\ln(1 + 1/\\gamma)}{A}$$
where $e = 2.71828\\dots$ is Euler's number. Checking the second derivative verifies this is a true minimum ($\frac{d^2V_B}{dx^2} > 0$).

**(b) Absolute Minimum Breakdown Voltage $V_{B,\\text{min}}$:**
Substitute $(p\\cdot d)_{\\text{min}} = \\frac{e C}{A}$ into the expression for $V_B$:
$$V_{B,\\text{min}} = V_B\\left( \\frac{e C}{A} \\right) = \\frac{B \\left( \\frac{e C}{A} \\right)}{\\ln(e)} = \\frac{e B C}{A} = \\frac{e B \\ln(1 + 1/\\gamma)}{A}$$
Notice the elegant relation:
$$V_{B,\\text{min}} = B \\times (p\\cdot d)_{\\text{min}}$$

**(c) Numerical Calculation for Air:**
Given:
$A = 15.0\\text{ cm}^{-1}\\cdot\\text{Torr}^{-1}$
$B = 365\\text{ V}/(\\text{cm}\\cdot\\text{Torr})$
$\\gamma = 0.01$
First, calculate $C$:
$$C = \\ln\\left(1 + \\frac{1}{0.01}\\right) = \\ln(1 + 100) = \\ln(101) \\approx 4.6151$$
Now evaluate $(p\\cdot d)_{\\text{min}}$:
$$(p\\cdot d)_{\\text{min}} = \\frac{e \\times C}{A} = \\frac{2.71828 \\times 4.6151}{15.0} = \\frac{12.545}{15.0} \\approx 0.836\\text{ Torr}\\cdot\\text{cm}$$
Finally, evaluate $V_{B,\\text{min}}$:
$$V_{B,\\text{min}} = B \\times (p\\cdot d)_{\\text{min}} = 365\\text{ V}/(\\text{cm}\\cdot\\text{Torr}) \\times 0.8363\\text{ Torr}\\cdot\\text{cm} \\approx 305.3\\text{ Volts}$$
This proves that in air, no continuous DC spark discharge can be struck below $\\sim 305\\text{ V}$, regardless of how close the electrodes are placed or how the pressure is varied."""
        }
    ]
}

# =========================================================================
# UNIT 2: SINGLE-PARTICLE MOTION IN UNIFORM FIELDS
# =========================================================================

unit2_data = {
    "unitId": "unit2-plasma",
    "title": "Single-Particle Motion in Uniform Fields & Electric Drifts",
    "subtitle": "Lorentz Force, Gyration, Electric Drift & Polarization Dynamics",
    "summary": "Rigorous kinematics and dynamics of charged particles in uniform electromagnetic fields: Lorentz force equation of motion, cyclotron frequency and Larmor radius, helicity and direction of gyration for electrons versus ions, complete mathematical decomposition into guiding center motion and circular gyration, cross-field electric drift velocity derivation and proof of charge/mass independence, general external force drifts (gravitational, centrifugal, collisional drag), time-varying electric fields and the polarization drift velocity, polarization current density, and the low-frequency effective dielectric permittivity of a magnetized plasma.",
    "sections": [
        {
            "id": "sec-2-1",
            "number": "2.1",
            "title": "The Fundamental Lorentz Equation of Motion & Gyration in Static Uniform Magnetic Fields",
            "content": """
<h3>1. The Lorentz Equation of Motion</h3>
<p>
The classical trajectory of a point particle of rest mass $m$ and electric charge $q$ moving with velocity $\\vec{v}$ in macroscopic electric $\\vec{E}$ and magnetic $\\vec{B}$ fields is governed by Newton's second law with the Lorentz force:
</p>
$$m \\frac{d\\vec{v}}{dt} = q\\left( \\vec{E} + \\vec{v}\\times\\vec{B} \\right)$$
<p>
Taking the scalar dot product with the velocity $\\vec{v}$:
</p>
$$m \\vec{v}\\cdot\\frac{d\\vec{v}}{dt} = \\frac{d}{dt}\\left( \\frac{1}{2}m v^2 \\right) = q \\vec{v}\\cdot\\vec{E} + q \\vec{v}\\cdot(\\vec{v}\\times\\vec{B}) = q \\vec{v}\\cdot\\vec{E}$$
<p>
Because $\\vec{v}\\cdot(\\vec{v}\\times\\vec{B}) \\equiv 0$, a pure magnetic field does <strong>zero work</strong> on a charged particle; it alters only the direction of the velocity vector while conserving total kinetic energy $\\frac{1}{2}m v^2 = \\text{const}$.
</p>

<h3>2. Gyration in a Static Uniform Magnetic Field</h3>
<p>
Let $\\vec{B} = B_0 \\hat{z}$ be static and spatially uniform, with $\\vec{E} = 0$. Resolving the equation of motion into Cartesian components:
</p>
$$m \\frac{dv_x}{dt} = q B_0 v_y, \\quad m \\frac{dv_y}{dt} = -q B_0 v_x, \\quad m \\frac{dv_z}{dt} = 0$$
<p>
Along the magnetic field, the parallel velocity is constant:
</p>
$$v_z(t) = v_\\parallel = \\text{const} \\implies z(t) = z_0 + v_\\parallel t$$
<p>
Differentiating the $x$-component and substituting $dv_y/dt$:
</p>
$$\\frac{d^2 v_x}{dt^2} = \\frac{q B_0}{m} \\frac{dv_y}{dt} = \\frac{q B_0}{m} \\left( -\\frac{q B_0}{m} v_x \\right) = -\\left( \\frac{q B_0}{m} \\right)^2 v_x$$
<p>
Defining the <strong>cyclotron frequency</strong> (or gyrofrequency) $\\omega_c$:
</p>
$$\\omega_c \\equiv \\frac{|q| B_0}{m}$$
<p>
The transverse velocity components oscillate harmonically at $\\omega_c$:
</p>
$$\\frac{d^2 v_x}{dt^2} + \\omega_c^2 v_x = 0, \\quad \\frac{d^2 v_y}{dt^2} + \\omega_c^2 v_y = 0$$
"""
        },
        {
            "id": "sec-2-2",
            "number": "2.2",
            "title": "Helical Trajectories, Larmor Radius & Sense of Gyration for Electrons and Ions",
            "content": """
<h3>1. Larmor Radius & Gyration Circle</h3>
<p>
Choosing initial conditions such that $v_x(0) = v_\\perp \\cos\\delta$ and integrating:
</p>
$$v_x(t) = v_\\perp \\cos(\\mp \\omega_c t + \\delta), \\quad v_y(t) = \\pm v_\\perp \\sin(\\mp \\omega_c t + \\delta)$$
<p>
where the upper sign corresponds to positive ions ($q > 0$) and the lower sign to electrons ($q = -e < 0$). Integrating the velocity components yields the spatial coordinates:
</p>
$$x(t) = X_0 + \\frac{v_\\perp}{\\omega_c} \\sin(\\mp \\omega_c t + \\delta) = X_0 + r_L \\sin(\\mp \\omega_c t + \\delta)$$
$$y(t) = Y_0 \\mp \\frac{v_\\perp}{\\omega_c} \\cos(\\mp \\omega_c t + \\delta) = Y_0 \\mp r_L \\cos(\\mp \\omega_c t + \\delta)$$
<p>
where $(X_0, Y_0)$ represents the fixed center of gyration, known as the <strong>guiding center</strong>. The radius of the gyration circle is the <strong>Larmor radius</strong> (or gyroradius) $r_L$:
</p>
$$r_L \\equiv \\frac{v_\\perp}{\\omega_c} = \\frac{m v_\\perp}{|q| B_0}$$

<h3>2. Helicity and Sense of Gyration</h3>
<p>
Looking along the direction of $\\vec{B}$ (the $+z$ axis):
</p>
<ul>
  <li><strong>Positive Ions ($q > 0$):</strong> Gyrate in a <em>counter-clockwise</em> sense (left-handed rotation).</li>
  <li><strong>Electrons ($q < 0$):</strong> Gyrate in a <em>clockwise</em> sense (right-handed rotation).</li>
</ul>
<p>
Because an orbiting charge forms an infinitesimal circular current loop $I = q (\\omega_c / 2\\pi)$, the magnetic dipole moment $\\vec{\\mu} = I \\vec{A}$ produced by the orbiting particle is directed <strong>opposite to the background magnetic field $\\vec{B}$</strong> for both ions and electrons:
</p>
$$\\vec{\\mu} = -\\frac{m v_\\perp^2}{2 B^2} \\vec{B}$$
<p>
Consequently, a plasma of gyrating particles is fundamentally <strong>diamagnetic</strong>: particle gyration naturally generates an opposing internal magnetic field that reduces the ambient $\\vec{B}$.
</p>
"""
        },
        {
            "id": "sec-2-3",
            "number": "2.3",
            "title": "Motion in Orthogonal Uniform Electric and Magnetic Fields (E perp B)",
            "content": """
<h3>1. Coupled Equations of Motion</h3>
<p>
Now introduce a static, uniform electric field perpendicular to $\\vec{B}$. Let $\\vec{B} = B_0 \\hat{z}$ and $\\vec{E} = E_y \\hat{y}$. The Lorentz equations of motion become:
</p>
$$m \\frac{dv_x}{dt} = q B_0 v_y, \\quad m \\frac{dv_y}{dt} = q E_y - q B_0 v_x, \\quad m \\frac{dv_z}{dt} = 0$$
<p>
Differentiating the $x$-equation with respect to time:
</p>
$$\\frac{d^2 v_x}{dt^2} = \\frac{q B_0}{m}\\frac{dv_y}{dt} = \\frac{q B_0}{m}\\left[ \\frac{q E_y}{m} - \\frac{q B_0}{m}v_x \\right] = -\\omega_c^2 \\left( v_x - \\frac{E_y}{B_0} \\right)$$
<p>
Defining a shifted velocity coordinate $u_x \\equiv v_x - \\frac{E_y}{B_0}$:
</p>
$$\\frac{d^2 u_x}{dt^2} + \\omega_c^2 u_x = 0$$
<p>
This demonstrates that in the moving reference frame, the particle undergoes ordinary cyclotron gyration around a guiding center translating steadily along the $+x$-axis with constant velocity:
</p>
$$v_E = \\frac{E_y}{B_0}$$
"""
        },
        {
            "id": "sec-2-4",
            "number": "2.4",
            "title": "Derivation of the Guiding Center E x B Drift Velocity & Absence of Current",
            "content": """
<h3>1. General Vector Derivation of E x B Drift</h3>
<p>
To derive the guiding center drift velocity in general coordinate-free vector form, partition the particle velocity $\\vec{v}$ into a slowly varying guiding center drift velocity $\\vec{v}_E$ and a rapidly oscillating gyration velocity $\\vec{v}_c$:
</p>
$$\\vec{v} = \\vec{v}_E + \\vec{v}_c$$
<p>
Averaging the Lorentz force equation over one complete cyclotron gyration period $\\tau_c = 2\\pi / \\omega_c$, the periodic gyration acceleration averages to zero: $\\langle d\\vec{v}_c / dt \\rangle = 0$. For a steady drift ($d\\vec{v}_E / dt = 0$):
</p>
$$0 = q \\left( \\vec{E} + \\vec{v}_E \\times \\vec{B} \\right)$$
<p>
Taking the vector cross product with $\\vec{B}$ on both sides:
</p>
$$\\vec{E} \\times \\vec{B} + (\\vec{v}_E \\times \\vec{B}) \\times \\vec{B} = 0$$
<p>
Applying the vector triple product identity $(\\vec{A}\\times\\vec{B})\\times\\vec{C} = (\\vec{A}\\cdot\\vec{C})\\vec{B} - (\\vec{B}\\cdot\\vec{C})\\vec{A}$:
</p>
$$(\\vec{v}_E \\times \\vec{B}) \\times \\vec{B} = (\\vec{v}_E \\cdot \\vec{B})\\vec{B} - B^2 \\vec{v}_E = -B^2 \\vec{v}_{E,\\perp}$$
<p>
Assuming the drift is purely perpendicular to $\\vec{B}$ ($\\vec{v}_E \\cdot \\vec{B} = 0$):
</p>
$$\\vec{E} \\times \\vec{B} - B^2 \\vec{v}_E = 0 \\implies \\vec{v}_E = \\frac{\\vec{E} \\times \\vec{B}}{B^2}$$

<h3>2. Fundamental Physical Properties of E x B Drift</h3>
<p>
The $\\vec{E}\\times\\vec{B}$ drift possesses several remarkable physical properties:
</p>
<ol>
  <li><strong>Charge Independence:</strong> The drift velocity $\\vec{v}_E$ is completely independent of the sign of the electric charge $q$. Both positive ions and negative electrons drift in the <em>identical direction</em> with the <em>identical velocity</em>.</li>
  <li><strong>Mass Independence:</strong> The drift velocity does not depend on the particle mass $m$. Protons, heavy impurities, and electrons all drift together.</li>
  <li><strong>Absence of Net Electric Current:</strong> Because both species move in unison:
  $$\\vec{J}_E = n_e q_e \\vec{v}_{E,e} + n_i q_i \\vec{v}_{E,i} = n_0 (-e) \\vec{v}_E + n_0 (+e) \\vec{v}_E = 0$$
  The $\\vec{E}\\times\\vec{B}$ drift produces <strong>zero net electric current</strong> in a quasi-neutral plasma.</li>
</ol>
"""
        },
        {
            "id": "sec-2-5",
            "number": "2.5",
            "title": "Generalized External Force Drifts: Gravitational, Centrifugal & Collisional Frictional Drifts",
            "content": """
<h3>1. Generalized Guiding Center Force Drift</h3>
<p>
Any general non-electromagnetic force $\\vec{F}$ (such as gravity $\\vec{F}_g = m\\vec{g}$ or centrifugal force $\\vec{F}_c = m v_\\parallel^2 \\hat{R}_c / R_c$) acting on a charged particle can be represented by an effective electric field:
</p>
$$\\vec{E}_{\\text{eff}} = \\frac{\\vec{F}}{q}$$
<p>
Substituting $\\vec{E}_{\\text{eff}}$ into the drift formula yields the <strong>generalized force drift velocity</strong> $\\vec{v}_F$:
</p>
$$\\vec{v}_F = \\frac{\\vec{E}_{\\text{eff}} \\times \\vec{B}}{B^2} = \\frac{1}{q} \\frac{\\vec{F} \\times \\vec{B}}{B^2}$$

<h3>2. Gravitational Drift</h3>
<p>
For a constant gravitational acceleration $\\vec{g}$:
</p>
$$\\vec{v}_g = \\frac{m}{q} \\frac{\\vec{g} \\times \\vec{B}}{B^2}$$
<p>
Crucially, because of the explicit factor of $q$ in the denominator:
</p>
<ul>
  <li>Ions and electrons drift in <strong>opposite directions</strong>!</li>
  <li>Because $m_i \\gg m_e$, the ion gravitational drift velocity is larger than the electron drift velocity by the mass ratio $M_i / m_e \\approx 1836$.</li>
  <li>This opposite motion establishes a net macroscopic cross-field electric current density:
  $$\\vec{J}_g = n_0 e (\\vec{v}_{gi} - \\vec{v}_{ge}) \\approx n_0 (M_i + m_e) \\frac{\\vec{g}\\times\\vec{B}}{B^2} \\approx \\rho_m \\frac{\\vec{g}\\times\\vec{B}}{B^2}$$
  where $\\rho_m = n_0 M_i$ is the mass density of the plasma.</li>
</ul>
"""
        },
        {
            "id": "sec-2-6",
            "number": "2.6",
            "title": "Time-Varying Electric Fields: Derivation of the Polarization Drift Velocity v_p",
            "content": """
<h3>1. Inertial Lag in Time-Varying Fields</h3>
<p>
Consider a slowly time-varying electric field $\\vec{E}(t) \\perp \\vec{B}_0$, where the rate of change is much slower than the cyclotron frequency:
</p>
$$\\omega \\ll \\omega_c \\iff \\left| \\frac{1}{E}\\frac{dE}{dt} \\right| \\ll \\omega_c$$
<p>
As $\\vec{E}$ changes, the guiding center $\\vec{E}\\times\\vec{B}$ drift velocity $\\vec{v}_E(t) = \\frac{\\vec{E}(t)\\times\\vec{B}}{B^2}$ must also accelerate with time:
</p>
$$\\frac{d\\vec{v}_E}{dt} = \\frac{1}{B^2}\\left( \\frac{d\\vec{E}}{dt} \\times \\vec{B} \\right)$$
<p>
Because the particle possesses finite mass $m$, inertia resists this acceleration. The particle experiences an effective inertial D'Alembert force:
</p>
$$\\vec{F}_{\\text{inertial}} = -m \\frac{d\\vec{v}_E}{dt} = -\\frac{m}{B^2}\\left( \\frac{d\\vec{E}}{dt} \\times \\vec{B} \\right)$$

<h3>2. The Polarization Drift Velocity</h3>
<p>
This inertial force drives an additional guiding center drift according to the general force drift formula:
</p>
$$\\vec{v}_p = \\frac{1}{q}\\frac{\\vec{F}_{\\text{inertial}} \\times \\vec{B}}{B^2} = -\\frac{m}{q B^4}\\left[ \\left( \\frac{d\\vec{E}}{dt} \\times \\vec{B} \\right) \\times \\vec{B} \\right]$$
<p>
Applying the vector triple product identity $(\\vec{A}\\times\\vec{B})\\times\\vec{B} = -B^2 \\vec{A}_\\perp$:
</p>
$$\\vec{v}_p = -\\frac{m}{q B^4} \\left( -B^2 \\frac{d\\vec{E}_\\perp}{dt} \\right) = \\frac{m}{q B^2} \\frac{d\\vec{E}_\\perp}{dt}$$
<p>
This is the <strong>polarization drift velocity</strong>. Notice the critical features:
</p>
<ul>
  <li>$\\vec{v}_p$ is parallel to the changing electric field $\\frac{d\\vec{E}_\\perp}{dt}$.</li>
  <li>$\\vec{v}_p$ is proportional to particle mass $m$. Because $M_i \\gg m_e$, polarization drift is overwhelmingly an <strong>ion phenomenon</strong>: $\\vec{v}_{pi} \\gg \\vec{v}_{pe}$.</li>
  <li>$\\vec{v}_p$ depends on charge $q$; ions and electrons drift in opposite directions, causing physical charge separation (polarization of the plasma).</li>
</ul>
"""
        },
        {
            "id": "sec-2-7",
            "number": "2.7",
            "title": "Polarization Current Density & The Effective Dielectric Permittivity of Magnetized Plasma",
            "content": """
<h3>1. The Polarization Current Density</h3>
<p>
Because positive ions and negative electrons drift in opposite directions along $\\frac{d\\vec{E}}{dt}$, the polarization drift creates a net macroscopic current density, termed the <strong>polarization current</strong> $\\vec{J}_p$:
</p>
$$\\vec{J}_p = n_0 e (\\vec{v}_{pi} - \\vec{v}_{pe}) = n_0 e \\left( \\frac{M_i}{e B^2}\\frac{d\\vec{E}}{dt} - \\frac{m_e}{-e B^2}\\frac{d\\vec{E}}{dt} \\right) = \\frac{n_0(M_i + m_e)}{B^2}\\frac{d\\vec{E}}{dt}$$
<p>
Defining the total mass density $\\rho_m \\equiv n_0(M_i + m_e) \\approx n_0 M_i$:
</p>
$$\\vec{J}_p = \\frac{\\rho_m}{B^2} \\frac{d\\vec{E}}{dt}$$

<h3>2. Dielectric Permittivity & Plasma Capacitance</h3>
<p>
In Maxwell's Ampère-Maxwell law, the total transverse current is the sum of conduction current, polarization current, and vacuum displacement current:
</p>
$$\\nabla \\times \\vec{B} = \\mu_0 \\left( \\vec{J} + \\varepsilon_0 \\frac{\\partial \\vec{E}}{\\partial t} \\right) = \\mu_0 \\left( \\vec{J}_p + \\varepsilon_0 \\frac{\\partial \\vec{E}}{\\partial t} \\right) = \\mu_0 \\left( \\frac{\\rho_m}{B^2} + \\varepsilon_0 \\right) \\frac{\\partial \\vec{E}}{\\partial t}$$
<p>
The combined term acts as an effective displacement current in a medium with effective permittivity $\\varepsilon$:
</p>
$$\\varepsilon \\equiv \\varepsilon_0 + \\frac{\\rho_m}{B^2} = \\varepsilon_0 \\left( 1 + \\frac{\\rho_m}{\\varepsilon_0 B^2} \\right)$$
<p>
Recalling the definition of the <strong>Alfvén speed</strong> $v_A \\equiv \\frac{B}{\\sqrt{\\mu_0 \\rho_m}}$, and noting $c^2 = 1/(\\mu_0 \\varepsilon_0)$:
</p>
$$\\frac{\\rho_m}{\\varepsilon_0 B^2} = \\frac{\\rho_m \\mu_0 c^2}{B^2} = \\frac{c^2}{v_A^2}$$
<p>
Thus, the low-frequency relative dielectric constant (dielectric permittivity) $\\epsilon_r$ of a magnetized plasma is:
</p>
$$\\epsilon_r = \\frac{\\varepsilon}{\\varepsilon_0} = 1 + \\frac{c^2}{v_A^2}$$
<p>
In typical laboratory fusion and space plasmas where $v_A \\ll c$ (e.g., $v_A \\sim 10^6\\text{ m/s}$), the dielectric constant is enormous: $\\epsilon_r \\sim 10^4 \\text{ to } 10^6$. The magnetized plasma acts as an immense energy storage capacitor.
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "plasma-prob-2-1",
            "title": "Complete Analytical Integration of Cyclotron Trajectory in Crossed E x B Fields from First Principles",
            "statement": """A singly ionized ion of mass $m$ and charge $q > 0$ is released from rest at the origin $\\vec{r}(0) = 0$ at $t = 0$ in static uniform fields $\\vec{E} = E_0 \\hat{y}$ and $\\vec{B} = B_0 \\hat{z}$.
(a) Set up the differential equations of motion for $v_x(t)$ and $v_y(t)$.
(b) Solve analytically for the velocity vector $\\vec{v}(t)$ using Laplace transforms or decoupling, and identify the guiding center drift velocity $v_E$.
(c) Integrate the velocity to obtain the parametric trajectory $(x(t), y(t))$ in the $xy$-plane.
(d) Identify the geometric nature of the curve and determine the maximum excursion $y_{\\text{max}}$ in the direction of the electric field.""",
            "solution": """**(a) Equations of Motion:**
The Lorentz force equation is $m \\frac{d\\vec{v}}{dt} = q(\\vec{E} + \\vec{v}\\times\\vec{B})$.
With $\\vec{E} = (0, E_0, 0)$ and $\\vec{B} = (0, 0, B_0)$:
$$\\vec{v}\\times\\vec{B} = \\det\\begin{pmatrix} \\hat{x} & \\hat{y} & \\hat{z} \\\\ v_x & v_y & v_z \\\\ 0 & 0 & B_0 \\end{pmatrix} = (v_y B_0)\\hat{x} - (v_x B_0)\\hat{y}$$
Component equations:
1. $m \\dot{v}_x = q B_0 v_y \\implies \\dot{v}_x = \\omega_c v_y$
2. $m \\dot{v}_y = q E_0 - q B_0 v_x \\implies \\dot{v}_y = \\frac{q E_0}{m} - \\omega_c v_x$
3. $m \\dot{v}_z = 0 \\implies v_z(t) = v_z(0) = 0$
where $\\omega_c = q B_0 / m$ is the cyclotron frequency.

**(b) Velocity Solution:**
Differentiating the second equation:
$$\\ddot{v}_y = -\\omega_c \\dot{v}_x = -\\omega_c (\\omega_c v_y) = -\\omega_c^2 v_y$$
The general solution for $v_y(t)$ is:
$$v_y(t) = C_1 \\cos(\\omega_c t) + C_2 \\sin(\\omega_c t)$$
Given the initial condition $v_y(0) = 0$:
$$v_y(0) = C_1 = 0 \\implies v_y(t) = C_2 \\sin(\\omega_c t)$$
From the equation of motion for $\\dot{v}_y$ at $t = 0$:
$$\\dot{v}_y(0) = \\omega_c C_2 = \\frac{q E_0}{m} - \\omega_c v_x(0) = \\frac{q E_0}{m} \\implies C_2 = \\frac{q E_0}{m \\omega_c} = \\frac{E_0}{B_0}$$
Therefore:
$$v_y(t) = \\frac{E_0}{B_0} \\sin(\\omega_c t)$$
Now substitute $v_y(t)$ into the $\\dot{v}_x$ equation:
$$\\dot{v}_x = \\omega_c \\frac{E_0}{B_0} \\sin(\\omega_c t)$$
Integrating with initial condition $v_x(0) = 0$:
$$v_x(t) = -\\frac{E_0}{B_0}\\cos(\\omega_c t) + C_3$$
$$v_x(0) = -\\frac{E_0}{B_0} + C_3 = 0 \\implies C_3 = \\frac{E_0}{B_0}$$
$$v_x(t) = \\frac{E_0}{B_0}\\left[ 1 - \\cos(\\omega_c t) \\right]$$
The constant term represents the guiding center $\\vec{E}\\times\\vec{B}$ drift velocity:
$$v_E = \\frac{E_0}{B_0}$$

**(c) Parametric Spatial Trajectory:**
Integrate $v_x(t)$ with $x(0) = 0$:
$$x(t) = \\int_0^t v_x(t') dt' = \\frac{E_0}{B_0} \\int_0^t [1 - \\cos(\\omega_c t')] dt' = \\frac{E_0}{B_0}\\left[ t - \\frac{\\sin(\\omega_c t)}{\\omega_c} \\right]$$
Integrate $v_y(t)$ with $y(0) = 0$:
$$y(t) = \\int_0^t v_y(t') dt' = \\frac{E_0}{B_0} \\int_0^t \\sin(\\omega_c t') dt' = \\frac{E_0}{\\omega_c B_0}\\left[ 1 - \\cos(\\omega_c t) \\right]$$
Defining the radius $R_c = \\frac{E_0}{\\omega_c B_0} = \\frac{m E_0}{q B_0^2}$:
$$x(t) = R_c (\\omega_c t - \\sin(\\omega_c t)), \\quad y(t) = R_c (1 - \\cos(\\omega_c t))$$

**(d) Geometric Curve & Maximum Excursion:**
These parametric equations represent a standard **cycloid** generated by a circle of radius $R_c$ rolling without slipping along the $x$-axis at velocity $v_E = R_c \\omega_c = E_0 / B_0$.
The maximum excursion in the $y$-direction occurs when $\\cos(\\omega_c t) = -1$ (at $\\omega_c t = \\pi, 3\\pi, \\dots$):
$$y_{\\text{max}} = 2 R_c = \\frac{2 m E_0}{q B_0^2}$$
At this peak, the particle's velocity is entirely in the $+x$-direction with magnitude $v_x = 2 E_0 / B_0$."""
        },
        {
            "id": "plasma-prob-2-2",
            "title": "Relativistic Gyro-Radius and Synchrotron Pitch Angle Kinematics in High-Magnetic-Field Laboratory Environments",
            "statement": """A relativistic electron with total kinetic energy $T_e = 5.0\\text{ MeV}$ is injected into a uniform magnetic field $B_0 = 4.0\\text{ Tesla}$ with pitch angle $\\alpha = 60^\\circ$ relative to $\\vec{B}_0$.
(a) Compute the relativistic Lorentz factor $\\gamma$, total energy $E$, and momentum magnitude $p$ of the electron.
(b) Calculate the relativistic cyclotron frequency $\\omega_{c,\\text{rel}}$ and the relativistic Larmor radius $r_{L,\\text{rel}}$.
(c) Compare these relativistic values with the naive non-relativistic formulas and compute the percentage discrepancy.
(d) Calculate the longitudinal distance $\\Delta z$ traversed along $\\vec{B}_0$ in one full gyration period.""",
            "solution": """**(a) Relativistic Energy & Momentum:**
Electron rest mass energy is $m_e c^2 = 0.511\\text{ MeV}$.
Total relativistic energy:
$$E = T_e + m_e c^2 = 5.0\\text{ MeV} + 0.511\\text{ MeV} = 5.511\\text{ MeV}$$
Lorentz factor $\\gamma$:
$$\\gamma = \\frac{E}{m_e c^2} = \\frac{5.511\\text{ MeV}}{0.511\\text{ MeV}} \\approx 10.785$$
Total momentum $p$:
$$p c = \\sqrt{E^2 - (m_e c^2)^2} = \\sqrt{(5.511)^2 - (0.511)^2} = \\sqrt{30.371 - 0.261} = \\sqrt{30.110} \\approx 5.487\\text{ MeV}$$
$$p = \\frac{5.487 \\times 10^6 \\times 1.6022\\times 10^{-19}\\text{ J}}{2.9979\\times 10^8\\text{ m/s}} = 2.932 \\times 10^{-21}\\text{ kg}\\cdot\\text{m/s}$$
Perpendicular momentum component with pitch angle $\\alpha = 60^\\circ$:
$$p_\\perp = p \\sin(60^\\circ) = (2.932\\times 10^{-21}) \\times 0.8660 = 2.539 \\times 10^{-21}\\text{ kg}\\cdot\\text{m/s}$$
Parallel momentum component:
$$p_\\parallel = p \\cos(60^\\circ) = (2.932\\times 10^{-21}) \\times 0.500 = 1.466 \\times 10^{-21}\\text{ kg}\\cdot\\text{m/s}$$

**(b) Relativistic Cyclotron Frequency & Larmor Radius:**
In relativistic dynamics, the relativistic mass is $\\gamma m_e$.
Relativistic cyclotron frequency:
$$\\omega_{c,\\text{rel}} = \\frac{e B_0}{\\gamma m_e} = \\frac{\\omega_{c0}}{\\gamma}$$
Non-relativistic gyrofrequency $\\omega_{c0}$:
$$\\omega_{c0} = \\frac{(1.6022\\times 10^{-19})(4.0)}{9.109\\times 10^{-31}} = 7.036 \\times 10^{11}\\text{ rad/s}$$
$$\\omega_{c,\\text{rel}} = \\frac{7.036 \\times 10^{11}}{10.785} = 6.524 \\times 10^{10}\\text{ rad/s}$$
Relativistic Larmor radius:
$$r_{L,\\text{rel}} = \\frac{p_\\perp}{e B_0} = \\frac{2.539 \\times 10^{-21}\\text{ kg}\\cdot\\text{m/s}}{(1.6022\\times 10^{-19}\\text{ C})(4.0\\text{ T})} = 3.962 \\times 10^{-3}\\text{ m} \\approx 3.96\\text{ mm}$$

**(c) Comparison with Non-Relativistic Values:**
Naive non-relativistic calculation would use $v_\\perp = \\sqrt{2 T_e / m_e}$, which exceeds the speed of light ($v > c$), giving an erroneous gyrofrequency:
$$\\omega_{c,\\text{naive}} = 7.036 \\times 10^{11}\\text{ rad/s}$$
The true relativistic frequency is smaller by a factor of $\\gamma = 10.785$ (a factor of over 10 reduction, or $-90.7\\%$ discrepancy).
The relativistic Larmor radius $r_{L,\\text{rel}}$ is enlarged by a factor of $\\gamma$ relative to the momentum scaling, emphasizing that relativistic inertia dramatically expands gyro-orbits.

**(d) Longitudinal Distance per Gyration:**
The gyration period is:
$$\\tau_c = \\frac{2\\pi}{\\omega_{c,\\text{rel}}} = \\frac{2\\pi}{6.524\\times 10^{10}} = 9.63 \\times 10^{-11}\\text{ s}$$
The parallel velocity is $v_\\parallel = \\frac{p_\\parallel}{\\gamma m_e} = \\frac{1.466\\times 10^{-21}}{10.785 \\times 9.109\\times 10^{-31}} = 1.492 \\times 10^8\\text{ m/s} \\approx 0.498 c$.
The pitch advance distance per gyration loop is:
$$\\Delta z = v_\\parallel \\tau_c = (1.492\\times 10^8\\text{ m/s}) \\times (9.63\\times 10^{-11}\\text{ s}) = 1.437 \\times 10^{-2}\\text{ m} = 1.44\\text{ cm}$$"""
        },
        {
            "id": "plasma-prob-2-3",
            "title": "Derivation of Polarization Current Density and Effective Low-Frequency Dielectric Permittivity for Alfvenic Fields",
            "statement": """A slab of hydrogen plasma (protons $M_i = 1.673\\times 10^{-27}\\text{ kg}$, electrons $m_e = 9.109\\times 10^{-31}\\text{ kg}$, density $n_0 = 5.0\\times 10^{19}\\text{ m}^{-3}$) is embedded in a static magnetic field $\\vec{B}_0 = 2.0\\text{ T} \\hat{z}$. A linearly ramped transverse electric field $\\vec{E}(t) = (E_0 t / \\tau) \\hat{x}$ is applied across the plasma for $0 \\le t \\le \\tau$, where $E_0 = 10.0\\text{ kV/m}$ and $\\tau = 1.0\\;\\mu\\text{s}$.
(a) Compute the polarization drift velocity for ions $\\vec{v}_{pi}$ and electrons $\\vec{v}_{pe}$.
(b) Calculate the resulting polarization current density $\\vec{J}_p$.
(c) Determine the Alfvén velocity $v_A$ and the low-frequency relative dielectric constant $\\epsilon_r$ of the plasma.
(d) Compute the total electric charge per unit area accumulated on the plasma boundary faces perpendicular to $\\hat{x}$ by time $t = \\tau$.""",
            "solution": """**(a) Polarization Drift Velocities:**
The electric field ramps linearly:
$$\\frac{d\\vec{E}}{dt} = \\frac{E_0}{\\tau}\\hat{x} = \\frac{10^4\\text{ V/m}}{10^{-6}\\text{ s}}\\hat{x} = 1.0 \\times 10^{10}\\text{ V}/(\\text{m}\\cdot\\text{s})\\hat{x}$$
The polarization drift formula is:
$$\\vec{v}_{p} = \\frac{m}{q B_0^2} \\frac{d\\vec{E}}{dt}$$
1. **For Ions ($q = +e, m = M_i$):**
$$v_{pi} = \\frac{M_i}{e B_0^2}\\frac{dE}{dt} = \\frac{1.673\\times 10^{-27}\\text{ kg}}{(1.6022\\times 10^{-19}\\text{ C})(2.0\\text{ T})^2}(1.0\\times 10^{10}\\text{ V/ms}) = \\frac{1.673\\times 10^{-17}}{6.409\\times 10^{-19}} \\approx 26.1\\text{ m/s}$$
$$\\vec{v}_{pi} = +26.1\\hat{x}\\text{ m/s}$$
2. **For Electrons ($q = -e, m = m_e$):**
$$v_{pe} = \\frac{m_e}{-e B_0^2}\\frac{dE}{dt} = -\\frac{9.109\\times 10^{-31}}{(1.6022\\times 10^{-19})(4.0)}(1.0\\times 10^{10}) = -1.42 \\times 10^{-2}\\text{ m/s}$$
$$\\vec{v}_{pe} = -0.0142\\hat{x}\\text{ m/s}$$
Notice that $\\vec{v}_{pi} / |\\vec{v}_{pe}| = M_i / m_e \\approx 1836$: the ions completely dominate the physical mass transport.

**(b) Polarization Current Density $\\vec{J}_p$:**
$$\\vec{J}_p = n_0 e (\\vec{v}_{pi} - \\vec{v}_{pe}) = \\frac{n_0 (M_i + m_e)}{B_0^2}\\frac{d\\vec{E}}{dt} \\approx \\frac{\\rho_m}{B_0^2}\\frac{d\\vec{E}}{dt}$$
Mass density $\\rho_m$:
$$\\rho_m = n_0 M_i = (5.0\\times 10^{19}\\text{ m}^{-3})(1.673\\times 10^{-27}\\text{ kg}) = 8.365 \\times 10^{-8}\\text{ kg/m}^3$$
Evaluating $\\vec{J}_p$:
$$J_p = \\frac{8.365\\times 10^{-8}\\text{ kg/m}^3}{(2.0\\text{ T})^2} \\times (1.0\\times 10^{10}\\text{ V/ms}) = (2.091\\times 10^{-8}) \\times 10^{10} = 209.1\\text{ A/m}^2$$
$$\\vec{J}_p = +209.1\\hat{x}\\text{ A/m}^2$$

**(c) Alfvén Speed $v_A$ & Relative Permittivity $\\epsilon_r$:**
Alfvén speed:
$$v_A = \\frac{B_0}{\\sqrt{\\mu_0 \\rho_m}} = \\frac{2.0}{\\sqrt{(4\\pi\\times 10^{-7})(8.365\\times 10^{-8})}} = \\frac{2.0}{\\sqrt{1.051\\times 10^{-13}}} = \\frac{2.0}{3.242\\times 10^{-7}} = 6.169 \\times 10^6\\text{ m/s}$$
Relative dielectric permittivity:
$$\\epsilon_r = 1 + \\frac{c^2}{v_A^2} = 1 + \\frac{(2.998\\times 10^8)^2}{(6.169\\times 10^6)^2} = 1 + (48.6)^2 = 1 + 2362 = 2363$$
The magnetized plasma has an effective dielectric constant of $\\epsilon_r \\approx 2363$, demonstrating immense capacitive polarizability.

**(d) Accumulated Boundary Surface Charge Density:**
Because the current $J_p$ is steady over the time interval $\Delta t = \\tau = 1.0\\;\\mu\\text{s}$:
$$\\sigma_{\\text{pol}} = \\int_0^\\tau J_p dt = J_p \\tau = (209.1\\text{ A/m}^2)(1.0\\times 10^{-6}\\text{ s}) = 2.091 \\times 10^{-4}\\text{ C/m}^2 = 209.1\\;\\mu\\text{C/m}^2$$
This surface charge density creates a macroscopic internal polarization electric field opposing the external applied field, analogous to a dielectric capacitor."""
        }
    ]
}

with open("plasma_u1.json", "w", encoding="utf-8") as f:
    json.dump(unit1_data, f, indent=2)
print("plasma_u1.json written successfully")

with open("plasma_u2.json", "w", encoding="utf-8") as f:
    json.dump(unit2_data, f, indent=2)
print("plasma_u2.json written successfully")
