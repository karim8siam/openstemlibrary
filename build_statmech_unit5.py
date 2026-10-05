# Build Script for Unit 5: Bose Systems
import json

u5_sections = [
    {
        "id": "sec-5-1",
        "number": "§5.1",
        "heading": "The Bose-Einstein Distribution Function and Applications",
        "simulation": "three-statistics-comparison-sim",
        "content": """The **Bose-Einstein distribution function** governs the statistical occupancy of single-particle quantum states for any system of identical bosons (particles with integer intrinsic spin $s = 0, 1, 2, \\dots$, possessing symmetric many-body wavefunctions).

<h4>1. Derivation via the Grand Canonical Ensemble</h4>
For bosons, any single-particle quantum state $i$ can be occupied by any number of particles $n_i \\in \\{0, 1, 2, 3, \\dots\\}$.
The grand partition function for a single state $i$ is a geometric series:
$$\\Xi_i = \\sum_{n_i=0}^\\infty e^{-\\beta(\\epsilon_i - \\mu)n_i} = \\frac{1}{1 - e^{-\\beta(\\epsilon_i - \\mu)}}$$
For this geometric series to converge, the ratio $e^{-\\beta(\\epsilon_i - \\mu)}$ must be strictly less than $1$, requiring:
$$\\epsilon_i - \\mu > 0 \\implies \\mu < \\epsilon_0$$
The chemical potential of an ideal Bose gas must always be strictly less than the ground-state energy.
The mean occupation number is:
$$n(\\epsilon_i) = \\langle n_i \\rangle = -\\frac{1}{\\beta}\\frac{\\partial \\ln \\Xi_i}{\\partial \\epsilon_i} = \\frac{e^{-\\beta(\\epsilon_i - \\mu)}}{1 - e^{-\\beta(\\epsilon_i - \\mu)}} = \\frac{1}{e^{(\\epsilon_i - \\mu)/(k_B T)} - 1}$$
This is the **Bose-Einstein Distribution Function**.

<h4>2. Fundamental Differences Between Quantum Statistics</h4>
<ul>
  <li>As $\\epsilon \\to \\mu$, the Bose occupation number diverges: $n(\\epsilon) \\to +\\infty$. Bosons enjoy occupying the same quantum state, leading to macroscopic condensation.</li>
  <li>In contrast, the Fermi-Dirac occupation can never exceed $1$: $f(\\epsilon) \\le 1$.</li>
  <li>In the classical dilute limit where $e^{(\\epsilon - \\mu)/k_B T} \\gg 1$, both distributions converge to the classical Maxwell-Boltzmann exponential $e^{-(\\epsilon - \\mu)/k_B T}$.</li>
</ul>"""
    },
    {
        "id": "sec-5-2",
        "number": "§5.2",
        "heading": "Planck's Radiation Law and Cavity Modes",
        "simulation": "planck-blackbody-spectrum-sim",
        "content": """Blackbody radiation is the thermal electromagnetic radiation within an enclosed cavity in thermodynamic equilibrium with its cavity walls.

<h4>1. Photons as a Bose Gas with Zero Chemical Potential</h4>
Photons are spin-1 massless bosons. In a cavity, photons are continuously absorbed and emitted by the cavity walls; their total number $N$ is not conserved.
In thermal equilibrium, Helmholtz free energy $F$ is minimized with respect to photon number:
$$\\left(\\frac{\\partial F}{\\partial N}\\right)_{T, V} = \\mu = 0$$
The chemical potential of a photon gas is **identically zero**: $\\mu = 0$.
The mean number of photons in a cavity mode of frequency $\\nu$ is:
$$\\langle n_\\nu \\rangle = \\frac{1}{e^{h\\nu / k_B T} - 1}$$

<h4>2. Density of Electromagnetic Modes</h4>
Electromagnetic waves in a cavity of volume $V$ have wavevector $k = 2\\pi \\nu / c$.
Because electromagnetic waves are transverse, there are $g = 2$ independent orthogonal polarization states for every wavevector:
$$g(\\nu) \\, d\\nu = 2 \\times \\frac{V}{(2\\pi)^3} 4\\pi k^2 dk = 2 \\times \\frac{4\\pi V}{(2\\pi)^3} \\left(\\frac{2\\pi \\nu}{c}\\right)^2 \\frac{2\\pi}{c} d\\nu = \\frac{8\\pi V}{c^3} \\nu^2 d\\nu$$

<h4>3. Planck's Spectral Radiation Formula</h4>
Multiplying mode density by average mode energy $\\langle E_\\nu \\rangle = h\\nu \\langle n_\\nu \\rangle$:
$$u(\\nu) \\, d\\nu = \\frac{1}{V} g(\\nu) h\\nu \\langle n_\\nu \\rangle d\\nu = \\frac{8\\pi h \\nu^3}{c^3} \\frac{d\\nu}{e^{h\\nu / k_B T} - 1}$$
Expressed in terms of wavelength $\\lambda = c / \\nu$ ($|d\\nu| = \\frac{c}{\\lambda^2} d\\lambda$):
$$u(\\lambda) \\, d\\lambda = \\frac{8\\pi h c}{\\lambda^5} \\frac{d\\lambda}{e^{h c / (\\lambda k_B T)} - 1}$$
This is **Planck's Law of Blackbody Radiation** (1900), which birthed quantum physics."""
    },
    {
        "id": "sec-5-3",
        "number": "§5.3",
        "heading": "The Photon Gas and Thermodynamics of Radiation",
        "simulation": "planck-blackbody-spectrum-sim",
        "content": """We now integrate Planck's law to derive the macroscopic thermodynamic properties of blackbody radiation.

<h4>1. Total Energy Density and the Stefan-Boltzmann Law</h4>
The total electromagnetic energy density in the cavity is:
$$u(T) = \\int_0^\\infty u(\\nu) \\, d\\nu = \\frac{8\\pi h}{c^3} \\int_0^\\infty \\frac{\\nu^3 d\\nu}{e^{h\\nu / k_B T} - 1}$$
Substituting $x = \\frac{h\\nu}{k_B T}$:
$$u(T) = \\frac{8\\pi h}{c^3} \\left(\\frac{k_B T}{h}\\right)^4 \\int_0^\\infty \\frac{x^3 dx}{e^x - 1}$$
The standard Bose-Einstein definite integral is $\\int_0^\\infty \\frac{x^3 dx}{e^x - 1} = \\frac{\\pi^4}{15}$. Therefore:
$$u(T) = \\left( \\frac{8\\pi^5 k_B^4}{15 c^3 h^3} \\right) T^4 = a T^4$$
where $a = 7.5657 \\times 10^{-16}\\text{ J/(m}^3\\cdot\\text{K}^4)$ is the radiation constant.
The radiant emissive power (flux density) from an ideal blackbody surface is:
$$J = \\frac{c}{4} u(T) = \\sigma T^4$$
where $\\sigma = \\frac{a c}{4} = 5.6704 \\times 10^{-8}\\text{ W/(m}^2\\cdot\\text{K}^4)$ is the **Stefan-Boltzmann constant**.

<h4>2. Wien's Displacement Law</h4>
Maximizing $u(\\lambda)$ with respect to $\\lambda$ yields $\\frac{d}{d\\lambda} u(\\lambda) = 0$, leading to:
$$\\frac{hc}{\\lambda_{\\max} k_B T} \\left( 1 - e^{-hc/(\\lambda_{\\max} k_B T)} \\right) = 5$$
Solving numerically gives $x = \\frac{hc}{\\lambda_{\\max} k_B T} \\approx 4.9651$, establishing **Wien's Displacement Law**:
$$\\lambda_{\\max} T = \\frac{h c}{4.9651 k_B} = 2.8978 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$$

<h4>3. Radiation Pressure and Entropy of the Photon Gas</h4>
Because photons are relativistic ($E = p c$), the radiation pressure is:
$$P = \\frac{1}{3} u(T) = \\frac{1}{3} a T^4$$
The total Helmholtz free energy is:
$$F = U - TS = -PV = -\\frac{1}{3} a V T^4$$
The entropy of the photon gas is:
$$S = -\\left(\\frac{\\partial F}{\\partial T}\\right)_V = \\frac{4}{3} a V T^3$$"""
    },
    {
        "id": "sec-5-4",
        "number": "§5.4",
        "heading": "The Specific Heat of Solids and the Phonon Gas",
        "simulation": "debye-vs-einstein-cv-sim",
        "content": """In a crystalline solid, atomic nuclei do not vibrate independently; their motion is coupled by interatomic electrostatic forces, forming collective vibrational wave modes called **phonons**.

<h4>1. Phonons as Quasiparticles</h4>
A phonon is a quantum of crystal lattice vibration possessing energy $E = \\hbar \\omega$ and crystal momentum $\\mathbf{p} = \\hbar \\mathbf{k}$.
Like photons:
<ul>
  <li>Phonons are bosons with spin 0.</li>
  <li>Phonons are created and destroyed thermally without number conservation; their chemical potential is zero: $\\mu = 0$.</li>
  <li>Mean phonon occupancy is given by Planck's distribution:
  $$\\langle n_\\omega \\rangle = \\frac{1}{e^{\\hbar \\omega / k_B T} - 1}$$
  </li>
</ul>

<h4>2. Acoustic and Optical Phonon Branches</h4>
For a 3D crystal lattice with $N$ unit cells and $p$ atoms per basis:
<ul>
  <li>Total degrees of freedom: $3pN$.</li>
  <li>$3$ **Acoustic Branches:** At long wavelengths ($k \\to 0$), atoms in a cell move in phase; frequency is linear: $\\omega = v_s k$ (sound waves).</li>
  <li>$3(p - 1)$ **Optical Branches:** Adjacent basis atoms vibrate out of phase, creating oscillating electric dipoles that couple to light.</li>
</ul>"""
    },
    {
        "id": "sec-5-5",
        "number": "§5.5",
        "heading": "The Debye Model of Lattice Specific Heat",
        "simulation": "debye-vs-einstein-cv-sim",
        "content": """Peter Debye (1912) recognized that low-temperature heat capacity is dominated by long-wavelength acoustic phonons, which can be treated as an elastic continuous medium.

<h4>1. The Debye Density of States and Debye Cutoff Frequency</h4>
In an isotropic elastic solid with 1 longitudinal and 2 transverse sound speeds:
$$g(\\omega) = \\frac{V}{2\\pi^2} \\left( \\frac{1}{v_L^3} + \\frac{2}{v_T^3} \\right) \\omega^2 = \\frac{3V}{2\\pi^2 v_s^3} \\omega^2$$
Because a crystal of $N$ atoms has exactly $3N$ vibrational modes, the spectrum must terminate at a maximum **Debye Cutoff Frequency** $\\omega_D$:
$$\\int_0^{\\omega_D} g(\\omega) \\, d\\omega = 3N \\implies \\frac{V}{2\\pi^2 v_s^3} \\omega_D^3 = 3N \\implies \\omega_D = v_s \\left( \\frac{6\\pi^2 N}{V} \\right)^{1/3}$$
We define the **Debye Temperature** $\\Theta_D$:
$$\\Theta_D \\equiv \\frac{\\hbar \\omega_D}{k_B}$$

<h4>2. Total Lattice Energy and Debye Specific Heat</h4>
The total vibrational internal energy is:
$$U(T) = \\int_0^{\\omega_D} \\hbar \\omega \\langle n_\\omega \\rangle g(\\omega) d\\omega = 9 N k_B T \\left( \\frac{T}{\\Theta_D} \\right)^3 \\int_0^{\\Theta_D/T} \\frac{x^3 dx}{e^x - 1}$$
Differentiating with respect to $T$ yields the **Debye Heat Capacity**:
$$C_V(T) = 9 N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3 \\int_0^{\\Theta_D/T} \\frac{x^4 e^x}{(e^x - 1)^2} dx$$

<h4>3. The Low-Temperature Debye $T^3$ Law</h4>
At low temperatures ($T \\ll \\Theta_D$), the upper integration limit extends to infinity: $\\int_0^\\infty \\frac{x^4 e^x dx}{(e^x - 1)^2} = \\frac{4\\pi^4}{15}$.
$$C_V(T) = 9 N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3 \\frac{4\\pi^4}{15} = \\frac{12\\pi^4}{5} N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3$$
This is the famous **Debye $T^3$ Law**. It perfectly matches experimental calorimeter data for all non-magnetic insulating solids at low temperatures."""
    },
    {
        "id": "sec-5-6",
        "number": "§5.6",
        "heading": "Bose-Einstein Condensation (BEC)",
        "simulation": "bose-einstein-condensation-sim",
        "content": """Satyendra Nath Bose (1924) and Albert Einstein (1925) predicted that an ideal gas of massive bosons undergoes a spectacular phase transition at low temperatures, with a macroscopic fraction of particles collapsing into the identical zero-momentum ground state.

<h4>1. Maximum Capacity of Excited States</h4>
For a 3D gas of $N$ non-relativistic bosons of mass $m$ in volume $V$, the density of states is $g(\\epsilon) = \\frac{2\\pi V}{h^3} (2m)^{3/2} \\epsilon^{1/2}$.
The total number of particles in excited states ($\\epsilon > 0$) is:
$$N_{\\text{exc}} = \\int_0^\\infty \\frac{g(\\epsilon) d\\epsilon}{e^{(\\epsilon - \\mu)/k_B T} - 1}$$
Because $\\mu \\le 0$, the maximum number of bosons that excited states can hold occurs when $\\mu \\to 0^-$:
$$N_{\\text{exc}}^{\\max}(T) = \\frac{2\\pi V (2m)^{3/2}}{h^3} (k_B T)^{3/2} \\int_0^\\infty \\frac{x^{1/2} dx}{e^x - 1} = V \\left( \\frac{m k_B T}{2\\pi \\hbar^2} \\right)^{3/2} \\zeta(3/2)$$
where $\\zeta(3/2) \\approx 2.6124$ is the Riemann zeta function.

<h4>2. The Critical Condensation Temperature ($T_c$)</h4>
When the temperature falls below a critical value $T_c$, the maximum capacity of excited states becomes strictly less than the total number of particles: $N_{\\text{exc}}^{\\max}(T) < N$.
Setting $N_{\\text{exc}}^{\\max}(T_c) = N$ defines the **Bose-Einstein Transition Temperature**:
$$T_c = \\frac{2\\pi \\hbar^2}{m k_B} \\left( \\frac{N/V}{\\zeta(3/2)} \\right)^{2/3} = \\frac{2\\pi \\hbar^2}{m k_B} \\left( \\frac{n}{2.6124} \\right)^{2/3}$$

<h4>3. Macroscopic Ground-State Condensation Fraction</h4>
For $T < T_c$, all surplus particles must condense into the single ground state $\\epsilon_0 = 0$:
$$N_0(T) = N - N_{\\text{exc}}(T) = N \\left[ 1 - \\left( \\frac{T}{T_c} \\right)^{3/2} \\right]$$
Below $T_c$, a macroscopic fraction of the gas forms a single giant macroscopic quantum wavepacket, experimentally observed in 1995 in trapped Rubidium-87 atoms by Cornell, Wieman, and Ketterle (Nobel Prize 2001)."""
    },
    {
        "id": "sec-5-7",
        "number": "§5.7",
        "heading": "Superfluidity in Liquid Helium-4",
        "simulation": "superfluid-two-fluid-sim",
        "content": """When Helium-4 ($^4\\text{He}$, a spin-0 boson) is cooled below $T_\\lambda = 2.17\\text{ K}$ at saturated vapor pressure, it undergoes the **Lambda Transition** from normal Liquid He-I to superfluid **Liquid He-II**.

<h4>1. The Two-Fluid Model (Tisza and Landau)</h4>
Liquid He-II behaves hydrodynamically as an interpenetrating mixture of two components:
$$\\rho = \\rho_n + \\rho_s$$
<ul>
  <li><strong>Superfluid Component ($\\rho_s$):</strong> Fraction of atoms in the macroscopic quantum condensate. It possesses **strictly zero viscosity** ($\\eta_s = 0$) and **zero entropy** ($s_s = 0$). It can flow with zero friction through sub-micron capillaries!</li>
  <li><strong>Normal Fluid Component ($\\rho_n$):</strong> Thermal gas of elementary quasiparticle excitations (phonons and rotons). It has normal viscosity and carries all the entropy of the liquid.</li>
</ul>
As $T \\to 0\\text{ K}$, $\\rho_n / \\rho \\to 0$ and $\\rho_s / \\rho \\to 1$.

<h4>2. Landau's Criterion for Superfluidity and the Roton Spectrum</h4>
Lev Landau (1941) asked: *At what speed will an object moving through He-II experience frictional drag by creating elementary excitations?*
By energy and momentum conservation, creation of an excitation with energy $\\epsilon(p)$ and momentum $p$ requires:
$$v > v_c = \\min_p \\left( \\frac{\\epsilon(p)}{p} \\right)$$
For He-II, the excitation spectrum exhibits a local minimum at $p_0 / \\hbar \\approx 1.92\\text{ Å}^{-1}$ with energy gap $\\Delta / k_B \\approx 8.6\\text{ K}$ called the **Roton minimum**:
$$\\epsilon(p) \\approx \\Delta + \\frac{(p - p_0)^2}{2\\mu}$$
The minimum ratio $\\epsilon(p)/p$ is:
$$v_c = \\frac{\\Delta}{p_0} \\approx 58\\text{ m/s}$$
For any flow velocity $v < v_c$, creating excitations is kinematically forbidden by quantum mechanics: the liquid flows with **strictly zero dissipation**!"""
    },
    {
        "id": "sec-5-8",
        "number": "§5.8",
        "heading": "Thermodynamics of Bose Systems",
        "simulation": "bose-gas-momentum-distribution-sim",
        "content": """We now explore the thermodynamic behavior of the degenerate Bose gas across the BEC transition.

<h4>1. Pressure Below $T_c$</h4>
In the condensed phase ($T < T_c$), the chemical potential is locked at zero: $\\mu = 0$.
The grand potential $\\Phi_G = -PV$ is given solely by excited states:
$$P(T) = k_B T \\left( \\frac{m k_B T}{2\\pi \\hbar^2} \\right)^{3/2} \\zeta(5/2) \\propto T^{5/2}$$
where $\\zeta(5/2) \\approx 1.3415$.
Notice that:
<blockquote>
Below $T_c$, the pressure depends strictly on temperature $T$ and is <strong>completely independent of volume $V$</strong>!
$$\\left(\\frac{\\partial P}{\\partial V}\\right)_T = 0$$
</blockquote>
The isothermal compressibility $\\kappa_T = -\\frac{1}{V}\\left(\\frac{\\partial V}{\\partial P}\\right)_T \\to \\infty$ diverges. Compressing the gas simply transfers particles from excited states into the zero-volume condensate without changing pressure.

<h4>2. Heat Capacity Across the Transition</h4>
The heat capacity is:
$$C_V(T) = \\begin{cases} \\frac{15}{4} k_B \\zeta(5/2) \\left( \\frac{m k_B T}{2\\pi \\hbar^2} \\right)^{3/2} V \\propto T^{3/2} & \\text{for } T < T_c \\\\ \\frac{3}{2} N k_B \\left[ 1 + 0.231 \\left( \\frac{T_c}{T} \\right)^{3/2} + \\dots \\right] & \\text{for } T > T_c \\end{cases}$$
At $T = T_c$, $C_V$ reaches a sharp peak with value $C_V(T_c) \\approx 1.925 N k_B$, exhibiting a cusp that marks a continuous third-order thermodynamic transition in the ideal gas (and a famous logarithmic $\\lambda$-peak in interacting Liquid Helium)."""
    },
    {
        "id": "sec-5-9",
        "number": "§5.9",
        "heading": "Thermodynamic Properties of Diatomic Molecules",
        "simulation": "equipartition-dof-sim",
        "content": """The thermal properties of a diatomic gas (such as $N_2, O_2, CO$) depend on the quantum excitation of rotational and vibrational molecular levels.

<h4>1. Molecular Rotational Partition Function</h4>
Treating the diatomic molecule as a rigid rotor with moment of inertia $I = \\mu_m r_0^2$:
$$E_J = \\frac{\\hbar^2}{2I} J(J + 1) = k_B \\Theta_{\\text{rot}} J(J + 1), \\quad J = 0, 1, 2, \\dots$$
where $\\Theta_{\\text{rot}} \\equiv \\frac{\\hbar^2}{2 I k_B}$ is the **characteristic rotational temperature** (typically $2\\text{ K}$ to $85\\text{ K}$).
The degeneracy of each rotational level is $g_J = 2J + 1$:
$$z_{\\text{rot}} = \\sum_{J=0}^\\infty (2J + 1) e^{-J(J+1) \\Theta_{\\text{rot}} / T}$$
For $T \\gg \\Theta_{\\text{rot}}$ (room temperature for most gases), the sum can be approximated by an integral:
$$z_{\\text{rot}} \\approx \\int_0^\\infty (2J + 1) e^{-J(J+1) \\Theta_{\\text{rot}} / T} dJ = \\frac{T}{\\sigma \\Theta_{\\text{rot}}}$$
where $\\sigma$ is the symmetry number ($\\sigma = 2$ for homonuclear $N_2$, $\\sigma = 1$ for heteronuclear $CO$).
The rotational heat capacity in this high-temperature limit is $C_V^{\\text{rot}} = R$.

<h4>2. Molecular Vibrational Partition Function</h4>
Treated as a 1D harmonic oscillator with vibrational frequency $\\omega$:
$$\\Theta_{\\text{vib}} \\equiv \\frac{\\hbar \\omega}{k_B}$$
For typical molecules, $\\Theta_{\\text{vib}} \\sim 1,000\\text{ K}$ to $3,000\\text{ K}$ (e.g., $N_2$: $\\Theta_{\\text{vib}} = 3,374\\text{ K}$).
$$z_{\\text{vib}} = \\frac{e^{-\\Theta_{\\text{vib}} / 2T}}{1 - e^{-\\Theta_{\\text{vib}} / T}}$$
$$C_V^{\\text{vib}} = R \\left( \\frac{\\Theta_{\\text{vib}}}{T} \\right)^2 \\frac{e^{\\Theta_{\\text{vib}}/T}}{(e^{\\Theta_{\\text{vib}}/T} - 1)^2}$$
At room temperature ($300\\text{ K} \\ll \\Theta_{\\text{vib}}$), vibrational modes are frozen into their quantum ground state."""
    },
    {
        "id": "sec-5-10",
        "number": "§5.10",
        "heading": "Nuclear Spin Effects in Diatomic Molecules: Ortho- and Para-Hydrogen",
        "simulation": "equipartition-dof-sim",
        "content": """In a homonuclear diatomic molecule like Hydrogen ($H_2$), quantum statistics of the two identical atomic nuclei imposes strict selection rules on molecular rotation!

<h4>1. Nuclear Spin States of Hydrogen ($H_2$)</h4>
Each proton has nuclear spin $I = 1/2$ (fermion). The two proton spins couple to give total nuclear spin $I_{\\text{tot}} \\in \\{0, 1\\}$:
<ul>
  <li><strong>Para-Hydrogen ($I_{\\text{tot}} = 0$, Nuclear Singlet):</strong>
  $$\\chi_{\\text{para}} = \\frac{1}{\\sqrt{2}}(|\\uparrow\\downarrow\\rangle - |\\downarrow\\uparrow\\rangle) \\quad (1\\text{ antisymmetric nuclear spin state})$$
  </li>
  <li><strong>Ortho-Hydrogen ($I_{\\text{tot}} = 1$, Nuclear Triplet):</strong>
  $$\\chi_{\\text{ortho}} \\in \\left\\{ |\\uparrow\\uparrow\\rangle, \\, \\frac{|\\uparrow\\downarrow\\rangle + |\\downarrow\\uparrow\\rangle}{\\sqrt{2}}, \\, |\\downarrow\\downarrow\\rangle \\right\\} \\quad (3\\text{ symmetric nuclear spin states})$$
  </li>
</ul>

<h4>2. Total Wavefunction Symmetry Requirement</h4>
Because protons are fermions, the total molecular wavefunction must be **antisymmetric** under the exchange of the two protons:
$$\\Psi_{\\text{total}} = \\psi_{\\text{trans}} \\times \\psi_{\\text{vib}} \\times \\psi_{\\text{rot}} \\times \\chi_{\\text{spin}}$$
The spatial exchange of the two nuclei is equivalent to an inversion: $\\mathbf{r} \\to -\\mathbf{r}$, which multiplies the rotational spherical harmonic $Y_{JM}(\\theta, \\phi)$ by $(-1)^J$:
<ul>
  <li>Even $J$ ($J = 0, 2, 4, \\dots$): Symmetric rotational state ($(-1)^J = +1$).</li>
  <li>Odd $J$ ($J = 1, 3, 5, \\dots$): Antisymmetric rotational state ($(-1)^J = -1$).</li>
</ul>
To make $\\Psi_{\\text{total}}$ antisymmetric:
<ol>
  <li><strong>Para-Hydrogen:</strong> Antisymmetric spin state $\\implies$ Must have **EVEN rotational levels only** ($J = 0, 2, 4, \\dots$). Ground state energy $E_0 = 0$ ($J=0$).</li>
  <li><strong>Ortho-Hydrogen:</strong> Symmetric spin state $\\implies$ Must have **ODD rotational levels only** ($J = 1, 3, 5, \\dots$). Lowest state is $J=1$ with energy $E_1 = 2 k_B \\Theta_{\\text{rot}}$.</li>
</ol>

<h4>3. The High-Temperature 3:1 Equilibrium Ratio</h4>
At room temperature ($T \\gg \\Theta_{\\text{rot}} \\approx 85\\text{ K}$), all nuclear spin states are equally populated. The equilibrium ratio is given by their nuclear spin statistical weights:
$$\\frac{\\text{Ortho}}{\\text{Para}} = \\frac{g_{\\text{ortho}}}{g_{\\text{para}}} = \\frac{3}{1} = 75\\% \\text{ Ortho}, \\quad 25\\% \\text{ Para}$$
When hydrogen is cooled to liquid temperature ($20\\text{ K}$) without a catalyst, conversion from ortho ($J=1$) to para ($J=0$) is extraordinarily slow (taking weeks) because it requires an electron-nuclear spin-flip. Catalysts (activated carbon, ferric oxide) are added to speed conversion and prevent boil-off in liquid hydrogen rocket propellant storage!"""
    }
]

u5_problems = [
    {
        "id": "prob-5-1",
        "difficulty": "Medium",
        "title": "Bose-Einstein Critical Condensation Temperature in Rubidium-87",
        "question": "In a magneto-optical trap, $N = 2.0 \\times 10^5$ atoms of Rubidium-87 ($^{87}\\text{Rb}$, atomic mass $m = 1.443 \\times 10^{-25}\\text{ kg}$, boson with integer nuclear spin) are confined to an effective volume $V = 1.0 \\times 10^{-15}\\text{ m}^3$. (a) Calculate the critical temperature $T_c$ for Bose-Einstein condensation. (b) If the gas is cooled to $T = 0.5 T_c$, determine the number of atoms $N_0$ condensed into the zero-momentum ground state.",
        "steps": [
            {
                "title": "Step 1: Compute particle number density",
                "math": "$$n = \\frac{N}{V} = \\frac{2.0 \\times 10^5}{1.0 \\times 10^{-15}\\text{ m}^3} = 2.0 \\times 10^{20}\\text{ atoms/m}^3$$",
                "explanation": "This gives the atomic number density in the ultra-cold optical trap."
            },
            {
                "title": "Step 2: Calculate the critical condensation temperature T_c",
                "math": "$$T_c = \\frac{2\\pi \\hbar^2}{m k_B} \\left(\\frac{n}{\\zeta(3/2)}\\right)^{2/3}$$\n$$\\frac{2\\pi \\hbar^2}{m k_B} = \\frac{2\\pi (1.055 \\times 10^{-34})^2}{(1.443 \\times 10^{-25})(1.381 \\times 10^{-23})} = 3.511 \\times 10^{-20}\\text{ K}\\cdot\\text{m}^2$$\n$$\\left(\\frac{2.0 \\times 10^{20}}{2.6124}\\right)^{2/3} = (7.656 \\times 10^{19})^{2/3} = 1.803 \\times 10^{13}\\text{ m}^{-2}$$\n$$T_c = (3.511 \\times 10^{-20}) \\times (1.803 \\times 10^{13}) = 6.33 \\times 10^{-7}\\text{ K} = 633\\text{ nK}$$",
                "explanation": "The critical temperature is approximately $633$ nanokelvin, matching typical laboratory laser-cooling experiments."
            },
            {
                "title": "Step 3: Calculate the condensate fraction at T = 0.5 T_c",
                "math": "$$\\frac{N_0}{N} = 1 - \\left(\\frac{T}{T_c}\\right)^{3/2} = 1 - (0.5)^{3/2} = 1 - 0.3536 = 0.6464$$\n$$N_0 = 0.6464 \\times (2.0 \\times 10^5) \\approx 129,280\\text{ atoms}$$",
                "explanation": "At half the transition temperature, nearly $65\\%$ of all atoms occupy the single zero-momentum ground state, forming a macroscopic quantum matter wave."
            }
        ]
    },
    {
        "id": "prob-5-2",
        "difficulty": "Hard",
        "title": "Solar Surface Temperature from Planck Radiation Law",
        "question": "The total solar irradiance (solar constant) measured at Earth's distance ($R = 1.496 \\times 10^{11}\\text{ m}$) outside the atmosphere is $S_0 = 1361\\text{ W/m}^2$. The Sun's radius is $R_\\odot = 6.963 \\times 10^8\\text{ m}$. (a) Using the Stefan-Boltzmann law, calculate the effective surface temperature $T_{\\text{eff}}$ of the Sun. (b) Using Wien's displacement law, calculate the peak wavelength $\\lambda_{\\max}$ of solar radiation and determine what color of the spectrum it corresponds to.",
        "steps": [
            {
                "title": "Step 1: Relate solar constant to surface emissive power",
                "math": "$$L_\\odot = 4\\pi R^2 S_0 = 4\\pi (1.496 \\times 10^{11}\\text{ m})^2 (1361\\text{ W/m}^2) = 3.828 \\times 10^{26}\\text{ W}$$\n$$J_{\\text{surf}} = \\frac{L_\\odot}{4\\pi R_\\odot^2} = \\frac{3.828 \\times 10^{26}}{4\\pi (6.963 \\times 10^8)^2} = 6.284 \\times 10^7\\text{ W/m}^2$$",
                "explanation": "This gives the total radiant flux emitted per square meter of the solar photosphere."
            },
            {
                "title": "Step 2: Compute effective surface temperature via Stefan-Boltzmann law",
                "math": "$$J_{\\text{surf}} = \\sigma T_{\\text{eff}}^4 \\implies T_{\\text{eff}} = \\left( \\frac{6.284 \\times 10^7\\text{ W/m}^2}{5.6704 \\times 10^{-8}\\text{ W/(m}^2\\cdot\\text{K}^4)} \\right)^{1/4}$$\n$$T_{\\text{eff}} = (1.1082 \\times 10^{15})^{1/4} \\approx 5,772\\text{ K}$$",
                "explanation": "The derived effective blackbody temperature of the Sun is $5,772\\text{ K}$."
            },
            {
                "title": "Step 3: Determine peak wavelength via Wien's law",
                "math": "$$\\lambda_{\\max} = \\frac{2.8978 \\times 10^{-3}\\text{ m}\\cdot\\text{K}}{5,772\\text{ K}} = 5.020 \\times 10^{-7}\\text{ m} = 502\\text{ nm}$$",
                "explanation": "The peak wavelength is $502\\text{ nm}$, which lies directly in the green portion of the visible spectrum, where human vision has maximum optical sensitivity."
            }
        ]
    },
    {
        "id": "prob-5-3",
        "difficulty": "Hard",
        "title": "Landau Critical Velocity in Liquid Helium-4",
        "question": "In liquid $^4\\text{He}$ at $T = 1.0\\text{ K}$, the roton excitation parameters are $\\Delta / k_B = 8.65\\text{ K}$, $p_0 / \\hbar = 1.92 \\times 10^{10}\\text{ m}^{-1}$, and effective mass $\\mu = 0.16 m_4$, where $m_4 = 6.646 \\times 10^{-27}\\text{ kg}$. (a) Calculate the Landau critical velocity $v_c = \\Delta / p_0$. (b) Explain why macroscopic superfluid flow in wide pipes breaks down at much lower velocities ($v \\sim 1\\text{ cm/s}$) than $v_c$.",
        "steps": [
            {
                "title": "Step 1: Compute roton gap energy and momentum",
                "math": "$$\\Delta = (8.65\\text{ K}) \\times (1.381 \\times 10^{-23}\\text{ J/K}) = 1.195 \\times 10^{-22}\\text{ J}$$\n$$p_0 = \\hbar (1.92 \\times 10^{10}\\text{ m}^{-1}) = (1.055 \\times 10^{-34}) \\times (1.92 \\times 10^{10}) = 2.026 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}$$",
                "explanation": "These are the energy gap and characteristic momentum of the roton minimum."
            },
            {
                "title": "Step 2: Calculate Landau critical velocity",
                "math": "$$v_c = \\frac{\\Delta}{p_0} = \\frac{1.195 \\times 10^{-22}\\text{ J}}{2.026 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}} = 58.98\\text{ m/s} \\approx 59\\text{ m/s}$$",
                "explanation": "This is the microscopic Landau critical velocity required to create single roton excitations."
            },
            {
                "title": "Step 3: Explain the discrepancy in wide channels",
                "math": "$$\\text{In macroscopic channels: } v_{\\text{crit}}^{\\text{vortex}} = \\frac{\\hbar}{m_4 R} \\ln\\left(\\frac{R}{a_0}\\right) \\ll v_c$$",
                "explanation": "In pipes wider than a few nanometers, dissipation is initiated not by creating individual rotons, but by nucleating quantized vortex lines and vortex rings (Feynman-Onsager vortex creation), which have a much lower energy per unit momentum, reducing the practical critical velocity to millimeters per second."
            }
        ]
    }
]

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/unit5_data.json', 'w') as f:
    json.dump({"number": 5, "title": "Bose Systems", "leadSummary": "Bose-Einstein distribution, Planck radiation law, photon gas thermodynamics, phonon specific heat, Debye model, Bose-Einstein condensation, superfluidity, and ortho/para hydrogen.", "sections": u5_sections, "problems": u5_problems}, f, indent=2)

print("Unit 5 built successfully with 10 topics and 3 solved problems!")
