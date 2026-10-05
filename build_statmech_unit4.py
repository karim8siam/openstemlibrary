# Build Script for Unit 4: Fermi Systems
import json

u4_sections = [
    {
        "id": "sec-4-1",
        "number": "§4.1",
        "heading": "The Fermi-Dirac Distribution Function",
        "simulation": "fermi-dirac-step-sim",
        "content": """The **Fermi-Dirac distribution function** governs the statistical occupation of single-particle quantum states for any system of identical fermions (particles with half-integer spin, obeying the Pauli exclusion principle).

<h4>1. Derivation via the Grand Canonical Ensemble</h4>
Consider a single-particle state $i$ with energy $\\epsilon_i$. Due to the Pauli exclusion principle, the state can be occupied by either $n_i = 0$ or $n_i = 1$ fermion.
The grand canonical partition function for this single state is:
$$\\Xi_i = \\sum_{n_i \\in \\{0, 1\\}} e^{-\\beta(\\epsilon_i - \\mu)n_i} = 1 + e^{-\\beta(\\epsilon_i - \\mu)}$$
The mean occupation number (probability of the state being occupied) is:
$$f(\\epsilon_i) = \\langle n_i \\rangle = -\\frac{1}{\\beta}\\frac{\\partial \\ln \\Xi_i}{\\partial \\epsilon_i} = \\frac{e^{-\\beta(\\epsilon_i - \\mu)}}{1 + e^{-\\beta(\\epsilon_i - \\mu)}} = \\frac{1}{e^{(\\epsilon_i - \\mu)/(k_B T)} + 1}$$
This is the celebrated **Fermi-Dirac Distribution Function**.

<h4>2. Behavior at Absolute Zero ($T = 0\\text{ K}$)</h4>
At $T = 0\\text{ K}$, the chemical potential defines the **Fermi Energy**: $\\mu(0) \\equiv \\epsilon_F$.
$$\\lim_{T \\to 0} \\frac{\\epsilon - \\epsilon_F}{k_B T} = \\begin{cases} -\\infty & \\text{if } \\epsilon < \\epsilon_F \\\\ +\\infty & \\text{if } \\epsilon > \\epsilon_F \\end{cases}$$
Therefore:
$$f(\\epsilon) = \\begin{cases} 1 & \\text{if } \\epsilon < \\epsilon_F \\\\ 0 & \\text{if } \\epsilon > \\epsilon_F \\end{cases}$$
At absolute zero, the distribution is an exact Heaviside step function: all quantum states below $\\epsilon_F$ are $100\\%$ completely occupied, while all states above $\\epsilon_F$ are strictly empty.

<h4>3. Thermal Broadening at Finite Temperature ($T > 0$)</h4>
At any finite temperature $T > 0$:
<ul>
  <li>At $\\epsilon = \\mu$, $f(\\mu) = \\frac{1}{e^0 + 1} = \\frac{1}{2}$ regardless of temperature! The chemical potential is always the exact energy level where the occupation probability is $50\\%$.</li>
  <li>Thermal excitation only affects states within a narrow energy window of width $\\sim 2 k_B T$ to $4 k_B T$ around $\\mu$.</li>
  <li>For $\\epsilon - \\mu \\gg k_B T$, $f(\\epsilon) \\approx e^{-(\\epsilon - \\mu)/k_B T}$, decaying into the classical Maxwell-Boltzmann tail.</li>
</ul>"""
    },
    {
        "id": "sec-4-2",
        "number": "§4.2",
        "heading": "The Ideal Fermi-Dirac Gas and Density of States",
        "simulation": "fermi-dirac-step-sim",
        "content": """We now consider an ideal gas of $N$ non-interacting spin-1/2 fermions (electrons, neutrons) confined in a container of volume $V$.

<h4>1. Quantum Density of States for Spin-1/2 Particles</h4>
In 3D reciprocal wavevector space ($k$-space), the volume occupied by one spatial orbital with periodic boundary conditions is $(2\\pi/L)^3 = 8\\pi^3 / V$.
Taking into account electron spin degeneracy $g_s = 2s + 1 = 2$ (spin-up and spin-down):
$$g(k) \\, dk = 2 \\times \\frac{V}{(2\\pi)^3} \\, 4\\pi k^2 dk = \\frac{V}{\\pi^2} k^2 dk$$
For non-relativistic fermions, energy is $\\epsilon = \\frac{\\hbar^2 k^2}{2m} \\implies k = \\frac{\\sqrt{2m\\epsilon}}{\\hbar}$, and $dk = \\frac{1}{2\\hbar}\\sqrt{\\frac{2m}{\\epsilon}} d\\epsilon$:
$$g(\\epsilon) \\, d\\epsilon = \\frac{V}{\\pi^2} \\left(\\frac{2m\\epsilon}{\\hbar^2}\\right) \\frac{1}{2\\hbar}\\sqrt{\\frac{2m}{\\epsilon}} d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\epsilon^{1/2} d\\epsilon$$
The density of states grows as the square root of energy: $g(\\epsilon) \\propto \\epsilon^{1/2}$.

<h4>2. Normalization Conditions</h4>
The total number of particles $N$ and total internal energy $U$ are given by:
$$N = \\int_0^\\infty g(\\epsilon) f(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\int_0^\\infty \\frac{\\epsilon^{1/2} d\\epsilon}{e^{(\\epsilon - \\mu)/k_B T} + 1}$$
$$U = \\int_0^\\infty \\epsilon \\, g(\\epsilon) f(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\int_0^\\infty \\frac{\\epsilon^{3/2} d\\epsilon}{e^{(\\epsilon - \\mu)/k_B T} + 1}$$"""
    },
    {
        "id": "sec-4-3",
        "number": "§4.3",
        "heading": "Fermi Energy, Fermi Momentum, and the Fermi Surface",
        "simulation": "fermi-surface-sphere-sim",
        "content": """At absolute zero, fermions pack into the lowest available quantum states up to a sharp energy cutoff termed the **Fermi Energy** $\\epsilon_F$.

<h4>1. Derivation of the Fermi Energy</h4>
Setting $T = 0\\text{ K}$, where $f(\\epsilon) = 1$ for $\\epsilon \\le \\epsilon_F$ and $0$ for $\\epsilon > \\epsilon_F$:
$$N = \\int_0^{\\epsilon_F} g(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\int_0^{\\epsilon_F} \\epsilon^{1/2} d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\frac{2}{3} \\epsilon_F^{3/2}$$
$$N = \\frac{V}{3\\pi^2} \\left( \\frac{2m \\epsilon_F}{\\hbar^2} \\right)^{3/2}$$
Solving explicitly for $\\epsilon_F$ in terms of particle number density $n = N/V$:
$$\\epsilon_F = \\frac{\\hbar^2}{2m} (3\\pi^2 n)^{2/3}$$

<h4>2. Fermi Wavevector and Fermi Momentum</h4>
In $k$-space, occupied states fill a sphere of radius $k_F$ called the **Fermi Sphere**:
$$k_F = (3\\pi^2 n)^{1/3}$$
The corresponding **Fermi Momentum** is:
$$p_F = \\hbar k_F = \\hbar (3\\pi^2 n)^{1/3}$$
The boundary in momentum space separating occupied from unoccupied states at $T = 0\\text{ K}$ is the **Fermi Surface**.

<h4>3. Ground-State Total Energy and Zero-Point Pressure</h4>
The total kinetic energy of the Fermi gas at $T = 0\\text{ K}$ is:
$$U_0 = \\int_0^{\\epsilon_F} \\epsilon \\, g(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\frac{2}{5} \\epsilon_F^{5/2} = \\frac{3}{5} N \\epsilon_F$$
The average energy per particle at absolute zero is $\\langle \\epsilon \\rangle = \\frac{3}{5}\\epsilon_F > 0$.
Even at absolute zero, fermions possess substantial kinetic energy due to quantum confinement and Pauli exclusion, exerting an enormous **Zero-Point Degeneracy Pressure**:
$$P_0 = -\\frac{\\partial U_0}{\\partial V} = -\\frac{3}{5} N \\frac{\\partial \\epsilon_F}{\\partial V} = \\frac{2}{5} \\frac{N}{V} \\epsilon_F = \\frac{2}{3} \\frac{U_0}{V} = \\frac{2}{5} n \\epsilon_F$$"""
    },
    {
        "id": "sec-4-4",
        "number": "§4.4",
        "heading": "The Fermi Temperature and Characteristic Scales",
        "simulation": "fermi-surface-sphere-sim",
        "content": """To understand why quantum effects dominate electron behavior at room temperature, we introduce the **Fermi Temperature**.

<h4>1. Definition of Fermi Temperature ($T_F$)</h4>
The Fermi temperature is defined as:
$$T_F \\equiv \\frac{\\epsilon_F}{k_B} = \\frac{\\hbar^2}{2m k_B} (3\\pi^2 n)^{2/3}$$

<h4>2. Characteristic Numerical Values for Real Metals</h4>
Consider metallic Copper (Cu):
<ul>
  <li>Electron density: $n \\approx 8.49 \\times 10^{28}\\text{ electrons/m}^3$</li>
  <li>Fermi energy: $\\epsilon_F = \\frac{(1.055 \\times 10^{-34})^2}{2(9.109 \\times 10^{-31})} [3\\pi^2 (8.49 \\times 10^{28})]^{2/3} = 1.125 \\times 10^{-18}\\text{ J} \\approx 7.03\\text{ eV}$</li>
  <li>Fermi temperature: $T_F = \\frac{1.125 \\times 10^{-18}\\text{ J}}{1.381 \\times 10^{-23}\\text{ J/K}} \\approx 81,600\\text{ K}$</li>
</ul>

<h4>3. The Extreme Quantum Degeneracy of Metals</h4>
Because $T_F \\approx 80,000\\text{ K}$ is vastly higher than room temperature ($T = 300\\text{ K}$), the ratio is:
$$\\frac{T}{T_F} \\approx \\frac{300}{80,000} \\approx 0.0037 \\ll 1$$
Even glowing white-hot molten steel ($T \\sim 1800\\text{ K}$) has $T/T_F \\sim 0.02 \\ll 1$.
Conduction electrons in metals are **permanently and deeply in their quantum degenerate ground state** under all terrestrial conditions!"""
    },
    {
        "id": "sec-4-5",
        "number": "§4.5",
        "heading": "Fermi Velocity and Mean Velocity of Free Electrons",
        "simulation": "fermi-dirac-step-sim",
        "content": """Because electrons are packed into states up to $\\epsilon_F$, electrons at the Fermi surface move with tremendous speeds.

<h4>1. The Fermi Velocity ($v_F$)</h4>
The speed of an electron residing on the Fermi surface is:
$$v_F = \\frac{p_F}{m} = \\frac{\\hbar k_F}{m} = \\sqrt{\\frac{2\\epsilon_F}{m}}$$
For Copper ($\\epsilon_F = 7.03\\text{ eV}$):
$$v_F = \\sqrt{\\frac{2 \\times (7.03 \\times 1.602 \\times 10^{-19}\\text{ J})}{9.109 \\times 10^{-31}\\text{ kg}}} = 1.57 \\times 10^6\\text{ m/s}$$
This is approximately $0.5\\%$ of the speed of light ($c$)!
Even at absolute zero, electrons zip through the atomic crystal lattice at over $1,500\\text{ km/second}$.

<h4>2. Mean Velocity of Free Electrons</h4>
The mean speed $\\langle v \\rangle$ of electrons throughout the Fermi sphere at $T = 0\\text{ K}$ is:
$$\\langle v \\rangle = \\frac{1}{N} \\int_0^{\\epsilon_F} \\sqrt{\\frac{2\\epsilon}{m}} \\, g(\\epsilon) \\, d\\epsilon = \\frac{1}{N} \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\sqrt{\\frac{2}{m}} \\int_0^{\\epsilon_F} \\epsilon \\, d\\epsilon = \\frac{3}{4} v_F$$
For Copper, $\\langle v \\rangle = 0.75 \\times 1.57 \\times 10^6\\text{ m/s} = 1.18 \\times 10^6\\text{ m/s}$."""
    },
    {
        "id": "sec-4-6",
        "number": "§4.6",
        "heading": "Degenerate Fermi Systems and the Sommerfeld Expansion",
        "simulation": "fermi-dirac-step-sim",
        "content": """To evaluate thermodynamic quantities at temperatures $T \\ll T_F$, we use the **Sommerfeld Expansion**.

<h4>1. The Sommerfeld Lemma</h4>
For any smooth function $H(\\epsilon)$ that vanishes at $\\epsilon = 0$:
$$\\int_0^\\infty H(\\epsilon) f(\\epsilon) \\, d\\epsilon = \\int_0^\\mu H(\\epsilon) \\, d\\epsilon + \\frac{\\pi^2}{6}(k_B T)^2 H'(\\mu) + \\frac{7\\pi^4}{360}(k_B T)^4 H'''(\\mu) + \\dots$$

<h4>2. Temperature Dependence of Chemical Potential $\\mu(T)$</h4>
Applying the Sommerfeld expansion to the particle number $N = \\int_0^\\infty g(\\epsilon) f(\\epsilon) d\\epsilon$:
$$N = \\int_0^\\mu g(\\epsilon) d\\epsilon + \\frac{\\pi^2}{6}(k_B T)^2 g'(\\mu)$$
Since $N = \\int_0^{\\epsilon_F} g(\\epsilon) d\\epsilon$, and $g(\\epsilon) \\propto \\epsilon^{1/2} \\implies g'(\\mu) = \\frac{1}{2\\mu} g(\\mu)$:
$$\\mu(T) \\approx \\epsilon_F \\left[ 1 - \\frac{\\pi^2}{12} \\left( \\frac{T}{T_F} \\right)^2 \\right]$$
The chemical potential shifts downward slightly with increasing temperature.

<h4>3. Electronic Heat Capacity of Metals ($C_V^{\\text{el}}$)</h4>
Expanding total energy $U(T)$:
$$U(T) \\approx U_0 + \\frac{\\pi^2}{6} g(\\epsilon_F) (k_B T)^2 = \\frac{3}{5}N\\epsilon_F + \\frac{\\pi^2}{4} N k_B \\frac{T^2}{T_F}$$
Differentiating with respect to temperature gives the celebrated **Sommerfeld Linear Heat Capacity**:
$$C_V^{\\text{el}} = \\frac{\\partial U}{\\partial T} = \\frac{\\pi^2}{2} N k_B \\left( \\frac{T}{T_F} \\right) = \\gamma T$$
where $\\gamma = \\frac{\\pi^2}{2} \\frac{N k_B}{T_F}$ is the **Sommerfeld constant**.

<h4>4. Resolution of the Classical Heat Capacity Catastrophe</h4>
Classical physics predicted that conduction electrons should contribute $C_V = \\frac{3}{2} N k_B$, which was contradicted by experiments showing total heat capacity in metals at room temperature was dominated by phonons ($3R$).
Quantum statistics explains this: only a tiny fraction of electrons—those within $k_B T$ of the Fermi surface (a fraction $\\sim T / T_F \\approx 0.004$)—can be thermally excited. The remaining $99.6\\%$ of electrons are locked in lower states by the Pauli exclusion principle and cannot absorb thermal energy!"""
    },
    {
        "id": "sec-4-7",
        "number": "§4.7",
        "heading": "Landau Diamagnetism",
        "simulation": "fermi-surface-sphere-sim",
        "content": """When an external magnetic field $\\mathbf{B} = B\\hat{\\mathbf{z}}$ is applied to a free electron gas, classical mechanics (the Bohr-van Leeuwen theorem) asserts that thermal equilibrium orbital magnetism is identically zero. Lev Landau (1930) showed that quantum mechanics produces a purely orbital diamagnetic response.

<h4>1. Quantized Landau Energy Levels</h4>
In a uniform magnetic field $B$, classical cyclotron orbits are quantized into discrete **Landau levels**:
$$\\epsilon(n, p_z) = \\left( n + \\frac{1}{2} \\right) \\hbar \\omega_c + \\frac{p_z^2}{2m}$$
where $\\omega_c = \\frac{e B}{m}$ is the **cyclotron frequency**, and $n = 0, 1, 2, \\dots$.
Each Landau level has an enormous macroscopic degeneracy per unit area:
$$g_L = \\frac{e B}{h} = \\frac{1}{2\\pi \\ell_B^2}$$
where $\\ell_B = \\sqrt{\\hbar / eB}$ is the magnetic length.

<h4>2. Landau Diamagnetic Susceptibility</h4>
Summing over the discrete Landau levels in the grand potential and expanding for weak fields ($k_B T \\gg \\hbar \\omega_c$ or $\\epsilon_F \\gg \\hbar \\omega_c$):
$$\\Phi_G(B) \\approx \\Phi_G(0) + \\frac{V}{6} \\mu_B^2 \\left( \\frac{\\partial n}{\\partial \\mu} \\right) B^2$$
The resulting magnetization $M = -\\frac{1}{V}\\frac{\\partial \\Phi_G}{\\partial B}$ yields the **Landau Diamagnetic Susceptibility**:
$$\\chi_{\\text{Landau}} = -\\frac{1}{3} \\mu_B^2 g(\\epsilon_F) = -\\frac{1}{3} \\chi_{\\text{Pauli}}$$
Quantized orbital motion creates an opposing diamagnetic moment exactly one-third the magnitude of spin paramagnetism."""
    },
    {
        "id": "sec-4-8",
        "number": "§4.8",
        "heading": "Pauli Paramagnetism",
        "simulation": "fermi-surface-sphere-sim",
        "content": """Wolfgang Pauli (1927) explained why the conduction electrons in metals exhibit a small, temperature-independent paramagnetic susceptibility.

<h4>1. Zeeman Splitting in the Conduction Band</h4>
Each electron possesses an intrinsic magnetic dipole moment $\\boldsymbol{\\mu} = -g \\mu_B \\mathbf{s} \\approx -2 \\mu_B \\mathbf{s}$, where $\\mu_B = \\frac{e\\hbar}{2m} = 9.274 \\times 10^{-24}\\text{ J/T}$ is the Bohr magneton.
In an external field $B$, Zeeman interaction splits the energy levels:
$$\\epsilon_\\uparrow = \\epsilon - \\mu_B B \\quad (\\text{spin parallel to } B), \\quad \\epsilon_\\downarrow = \\epsilon + \\mu_B B \\quad (\\text{spin antiparallel})$$

<h4>2. Fermi Surface Asymmetry</h4>
In equilibrium, both spin sub-bands must fill to the identical chemical potential $\\epsilon_F$. Consequently, spin-up states expand while spin-down states contract:
$$N_\\uparrow = \\frac{1}{2} \\int_0^{\\epsilon_F + \\mu_B B} g(\\epsilon) d\\epsilon \\approx \\frac{N}{2} + \\frac{1}{2} g(\\epsilon_F) \\mu_B B$$
$$N_\\downarrow = \\frac{1}{2} \\int_0^{\\epsilon_F - \\mu_B B} g(\\epsilon) d\\epsilon \\approx \\frac{N}{2} - \\frac{1}{2} g(\\epsilon_F) \\mu_B B$$
The net excess of parallel spins is:
$$\\Delta N = N_\\uparrow - N_\\downarrow = g(\\epsilon_F) \\mu_B B$$

<h4>3. The Pauli Susceptibility Formula</h4>
The macroscopic magnetic moment is $M = \\mu_B \\Delta N = \\mu_B^2 g(\\epsilon_F) B$.
The magnetic susceptibility per unit volume is:
$$\\chi_{\\text{Pauli}} = \\frac{\\mu_0 M}{B} = \\mu_0 \\mu_B^2 g(\\epsilon_F) = \\frac{3 n \\mu_0 \\mu_B^2}{2 \\epsilon_F}$$
Notice that:
<ol>
  <li>$\\chi_{\\text{Pauli}}$ is **strictly independent of temperature** to leading order (unlike classical Curie paramagnetism $\\chi \\propto 1/T$).</li>
  <li>Combining Pauli paramagnetism with Landau diamagnetism gives the net response:
  $$\\chi_{\\text{total}} = \\chi_{\\text{Pauli}} + \\chi_{\\text{Landau}} = \\left(1 - \\frac{1}{3}\\right) \\chi_{\\text{Pauli}} = \\frac{2}{3} \\chi_{\\text{Pauli}} > 0$$
  The electron gas in normal metals remains weakly paramagnetic overall.</li>
</ol>"""
    },
    {
        "id": "sec-4-9",
        "number": "§4.9",
        "heading": "Thermionic Emission and the Richardson-Dushman Law",
        "simulation": "fermi-dirac-step-sim",
        "content": """Thermionic emission is the thermally induced flow of charge carriers over a surface potential barrier (used in vacuum tubes, electron microscopes, and cathode ray tubes).

<h4>1. The Escape Condition and Work Function</h4>
Inside a metal, electrons occupy states up to the Fermi energy $\\epsilon_F$. The minimum energy required to liberate an electron from the Fermi level into vacuum at rest is the **Work Function** $\\Phi$ (typically $4.5\\text{ eV}$ for tungsten).
An electron at surface $z = 0$ can escape into vacuum only if its kinetic energy perpendicular to the surface exceeds the barrier:
$$\\frac{p_z^2}{2m} \\ge \\epsilon_F + \\Phi$$

<h4>2. Derivation of the Emission Current Density</h4>
The emission current density $J$ is obtained by integrating the flux $v_z = p_z / m$ over all escape states:
$$J = 2 e \\left(\\frac{1}{h^3}\\right) \\int_{-\\infty}^\\infty dp_x \\int_{-\\infty}^\\infty dp_y \\int_{p_{z,\\min}}^\\infty dp_z \\, \\frac{p_z}{m} \\frac{1}{e^{(\\epsilon - \\mu)/k_B T} + 1}$$
Because $\\epsilon - \\mu \\ge \\Phi \\gg k_B T$, the Fermi-Dirac distribution reduces to the Maxwell-Boltzmann approximation $e^{-(\\epsilon - \\epsilon_F)/k_B T}$:
$$J = \\frac{2 e}{m h^3} e^{\\epsilon_F / k_B T} \\left( \\int_{-\\infty}^\\infty e^{-p_x^2 / 2m k_B T} dp_x \\right)^2 \\int_{p_{z,\\min}}^\\infty p_z e^{-p_z^2 / 2m k_B T} dp_z$$
The transverse integrals yield $(2\\pi m k_B T)$. Evaluating the $p_z$ integral:
$$\\int_{p_{z,\\min}}^\\infty p_z e^{-p_z^2 / 2m k_B T} dp_z = m k_B T \\exp\\left( -\\frac{\\epsilon_F + \\Phi}{k_B T} \\right)$$

<h4>3. The Richardson-Dushman Equation</h4>
Combining terms gives the famous **Richardson-Dushman Law**:
$$J = A T^2 \\exp\\left( -\\frac{\\Phi}{k_B T} \\right)$$
where $A$ is the universal **Richardson constant**:
$$A = \\frac{4\\pi m e k_B^2}{h^3} = 1.20173 \\times 10^6\\text{ A/(m}^2\\cdot\\text{K}^2)$$"""
    },
    {
        "id": "sec-4-10",
        "number": "§4.10",
        "heading": "Statistical Equilibrium in White Dwarf Stars and Chandrasekhar Limit",
        "simulation": "white-dwarf-chandrasekhar-sim",
        "content": """When an intermediate-mass star (such as the Sun) exhausts its nuclear fuel, it collapses under self-gravity until halted by the **electron degeneracy pressure** of its completely degenerate electron gas, forming a **White Dwarf star**.

<h4>1. Non-Relativistic Equilibrium</h4>
In a star of mass $M$ and radius $R$, the gravitational potential energy is:
$$U_{\\text{grav}} = -\\frac{3}{5} \\frac{G M^2}{R}$$
For non-relativistic degenerate electrons ($p_F \\ll m_e c$), the kinetic energy scales as:
$$U_{\\text{kin}} = \\frac{3}{5} N \\epsilon_F \\propto N \\frac{\\hbar^2}{m_e} \\left(\\frac{N}{R^3}\\right)^{2/3} \\propto \\frac{\\hbar^2 N^{5/3}}{m_e R^2}$$
Minimizing total energy $E = U_{\\text{kin}} + U_{\\text{grav}}$ with respect to $R$:
$$\\frac{dE}{dR} = -\\frac{2 C_1}{R^3} + \\frac{C_2 G M^2}{R^2} = 0 \\implies R \\propto M^{-1/3}$$
Remarkably, a heavier white dwarf is physically smaller!

<h4>2. Relativistic Core Collapse and the Chandrasekhar Limit</h4>
As stellar mass increases, the star contracts and core density soars, driving the Fermi momentum into the ultra-relativistic regime:
$$p_F = \\hbar (3\\pi^2 n)^{1/3} \\gg m_e c$$
For ultra-relativistic electrons, energy is linear in momentum: $\\epsilon = p c$. The kinetic degeneracy energy becomes:
$$U_{\\text{kin}}^{\\text{rel}} \\propto N p_F c \\propto \\hbar c \\frac{N^{4/3}}{R}$$
Notice that both gravitational and relativistic kinetic energy scale as $1/R$:
$$E_{\\text{total}} = \\left( A \\hbar c N^{4/3} - B G M^2 \\right) \\frac{1}{R}$$
If gravity exceeds degeneracy pressure ($B G M^2 > A \\hbar c N^{4/3}$), no stable equilibrium radius exists: the star collapses indefinitely!
Equating the two terms yields the **Chandrasekhar Mass Limit** (Subrahmanyan Chandrasekhar, 1930):
$$M_{\\text{Ch}} = \\frac{\\omega_3^0}{4\\pi} \\left( \\frac{h c}{G} \\right)^{3/2} \\left( \\frac{1}{\\mu_e m_p} \\right)^2 \\approx 1.44 M_\\odot$$
Any stellar core exceeding $1.44$ solar masses cannot be supported by electron degeneracy and must collapse into a neutron star or black hole."""
    }
]

u4_problems = [
    {
        "id": "prob-4-1",
        "difficulty": "Medium",
        "title": "Fermi Energy and Degeneracy Pressure in Liquid 3He",
        "question": "Liquid helium-3 ($^3\\text{He}$) is a fermion liquid with spin-1/2 and atomic mass $m = 5.01 \\times 10^{-27}\\text{ kg}$. At low temperatures, its mass density is $\\rho = 81\\text{ kg/m}^3$. (a) Calculate the number density $n$, Fermi wavevector $k_F$, and Fermi energy $\\epsilon_F$ in Kelvin. (b) Calculate the zero-point degeneracy pressure $P_0$ exerted by the liquid at $T = 0\\text{ K}$.",
        "steps": [
            {
                "title": "Step 1: Compute particle number density",
                "math": "$$n = \\frac{\\rho}{m} = \\frac{81\\text{ kg/m}^3}{5.01 \\times 10^{-27}\\text{ kg}} = 1.617 \\times 10^{28}\\text{ atoms/m}^3$$",
                "explanation": "This establishes the atomic number density of the liquid."
            },
            {
                "title": "Step 2: Determine Fermi wavevector and Fermi energy",
                "math": "$$k_F = (3\\pi^2 n)^{1/3} = [3\\pi^2 (1.617 \\times 10^{28})]^{1/3} = 7.823 \\times 10^9\\text{ m}^{-1}$$\n$$\\epsilon_F = \\frac{\\hbar^2 k_F^2}{2m} = \\frac{(1.055 \\times 10^{-34})^2 (7.823 \\times 10^9)^2}{2 (5.01 \\times 10^{-27})} = 6.792 \\times 10^{-23}\\text{ J}$$\n$$T_F = \\frac{\\epsilon_F}{k_B} = \\frac{6.792 \\times 10^{-23}\\text{ J}}{1.381 \\times 10^{-23}\\text{ J/K}} = 4.92\\text{ K}$$",
                "explanation": "Because $T_F \\approx 4.9\\text{ K}$, liquid $^3\\text{He}$ below $1\\text{ K}$ is a degenerate quantum Fermi liquid."
            },
            {
                "title": "Step 3: Calculate the zero-point degeneracy pressure",
                "math": "$$P_0 = \\frac{2}{5} n \\epsilon_F = 0.4 \\times (1.617 \\times 10^{28}\\text{ m}^{-3}) \\times (6.792 \\times 10^{-23}\\text{ J}) = 4.393 \\times 10^5\\text{ Pa} \\approx 4.34\\text{ atm}$$",
                "explanation": "The quantum zero-point degeneracy pressure exceeds 4 atmospheres, preventing liquid $^3\\text{He}$ from freezing into a solid under ambient pressure down to absolute zero."
            }
        ]
    },
    {
        "id": "prob-4-2",
        "difficulty": "Hard",
        "title": "Electronic vs Lattice Heat Capacity in Copper",
        "question": "For Copper, the Fermi temperature is $T_F = 81,600\\text{ K}$ and the Debye temperature is $\\Theta_D = 343\\text{ K}$. (a) Express the electronic heat capacity $C_V^{\\text{el}} = \\gamma T$ and lattice heat capacity $C_V^{\\text{ph}} = A T^3$. (b) Find the crossover temperature $T^*$ below which the electronic contribution exceeds the phonon contribution.",
        "steps": [
            {
                "title": "Step 1: Write down electronic and lattice heat capacities",
                "math": "$$C_V^{\\text{el}} = \\frac{\\pi^2}{2} R \\left(\\frac{T}{T_F}\\right) = \\gamma T, \\quad \\gamma = \\frac{\\pi^2 (8.314)}{2 (81,600)} = 5.03 \\times 10^{-4}\\text{ J/(mol}\\cdot\\text{K}^2)$$\n$$C_V^{\\text{ph}} = \\frac{12\\pi^4}{5} R \\left(\\frac{T}{\\Theta_D}\\right)^3 = A T^3, \\quad A = \\frac{12\\pi^4 (8.314)}{5 (343)^3} = 4.80 \\times 10^{-5}\\text{ J/(mol}\\cdot\\text{K}^4)$$",
                "explanation": "At low temperatures, total heat capacity is $C_V = \\gamma T + A T^3$."
            },
            {
                "title": "Step 2: Equate contributions to find crossover temperature T*",
                "math": "$$\\gamma T^* = A (T^*)^3 \\implies (T^*)^2 = \\frac{\\gamma}{A} = \\frac{5.03 \\times 10^{-4}}{4.80 \\times 10^{-5}} = 10.48\\text{ K}^2$$\n$$T^* = \\sqrt{10.48} \\approx 3.24\\text{ K}$$",
                "explanation": "Below $3.24\\text{ K}$, the linear electronic term dominates over the cubic lattice term, while at room temperature ($300\\text{ K}$) phonons dominate overwhelmingly."
            }
        ]
    },
    {
        "id": "prob-4-3",
        "difficulty": "Hard",
        "title": "Ultra-Relativistic Electron Degeneracy in a Massive White Dwarf",
        "question": "In a dense white dwarf, electrons are ultra-relativistic with $\\epsilon \\approx p c$. (a) Derive the density of states $g(\\epsilon)$ and Fermi energy $\\epsilon_F$. (b) Derive the relativistic degeneracy equation of state $P \\propto \\rho^{4/3}$.",
        "steps": [
            {
                "title": "Step 1: Compute relativistic density of states",
                "math": "$$\\epsilon = p c = \\hbar k c \\implies k = \\frac{\\epsilon}{\\hbar c}, \\quad dk = \\frac{d\\epsilon}{\\hbar c}$$\n$$g(\\epsilon) d\\epsilon = 2 \\times \\frac{V}{2\\pi^2} k^2 dk = \\frac{V}{\\pi^2 (\\hbar c)^3} \\epsilon^2 d\\epsilon$$",
                "explanation": "For ultra-relativistic particles, the density of states grows quadratically with energy."
            },
            {
                "title": "Step 2: Integrate to obtain Fermi energy",
                "math": "$$N = \\int_0^{\\epsilon_F} g(\\epsilon) d\\epsilon = \\frac{V}{3\\pi^2 (\\hbar c)^3} \\epsilon_F^3 \\implies \\epsilon_F = \\hbar c (3\\pi^2 n)^{1/3}$$",
                "explanation": "The ultra-relativistic Fermi energy scales with density as $n^{1/3}$ rather than $n^{2/3}$."
            },
            {
                "title": "Step 3: Calculate energy and pressure",
                "math": "$$U_0 = \\int_0^{\\epsilon_F} \\epsilon g(\\epsilon) d\\epsilon = \\frac{V}{4\\pi^2 (\\hbar c)^3} \\epsilon_F^4 = \\frac{3}{4} N \\epsilon_F = \\frac{3}{4} \\hbar c (3\\pi^2)^{1/3} V \\left(\\frac{N}{V}\\right)^{4/3}$$\n$$P_0 = -\\frac{\\partial U_0}{\\partial V} = \\frac{1}{3}\\frac{U_0}{V} = \\frac{1}{4} \\hbar c (3\\pi^2)^{1/3} n^{4/3} \\propto \\rho^{4/3}$$",
                "explanation": "The adiabatic index softens from $\\gamma = 5/3$ down to $\\gamma = 4/3$, leading directly to the gravitational instability discovered by Chandrasekhar."
            }
        ]
    }
]

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/unit4_data.json', 'w') as f:
    json.dump({"number": 4, "title": "Fermi Systems", "leadSummary": "Fermi-Dirac distribution, Fermi energy, Fermi surface, Sommerfeld expansion, Landau diamagnetism, Pauli paramagnetism, thermionic emission, and white dwarf degeneracy.", "sections": u4_sections, "problems": u4_problems}, f, indent=2)

print("Unit 4 built successfully with 10 topics and 3 solved problems!")
