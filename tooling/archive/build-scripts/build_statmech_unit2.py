# Build Script for Unit 2: Statistics and Thermodynamics
import json

u2_sections = [
    {
        "id": "sec-2-1",
        "number": "§2.1",
        "heading": "The Statistical Concept of Temperature and the Zeroth Law",
        "simulation": "canonical-boltzmann-sim",
        "content": """In classical thermodynamics, temperature is introduced empirically through the Zeroth Law via thermal equilibrium. Statistical mechanics provides the microscopic explanation of temperature.

<h4>1. Microscopic Definition of Temperature</h4>
When two systems $A_1$ and $A_2$ are in thermal contact with fixed volumes and particle numbers, their total energy $E = E_1 + E_2$ is conserved. As proven in Chapter 1, the condition for the combined multiplicity $W(E_1, E_2) = W_1(E_1)W_2(E_2)$ to attain its maximum is:
$$\\left(\\frac{\\partial \\ln W_1}{\\partial E_1}\\right)_{V_1, N_1} = \\left(\\frac{\\partial \\ln W_2}{\\partial E_2}\\right)_{V_2, N_2}$$
We define the thermodynamic parameter $\\beta$:
$$\\beta \\equiv \\left(\\frac{\\partial \\ln W}{\\partial E}\\right)_{V, N}$$
The statistical absolute temperature $T$ is defined fundamentally as:
$$\\frac{1}{T} \\equiv k_B \\beta = k_B \\left(\\frac{\\partial \\ln W}{\\partial E}\\right)_{V, N} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V, N}$$

<h4>2. Statistical Derivation of the Zeroth Law</h4>
The Zeroth Law states: *If body A is in thermal equilibrium with body C, and body B is in thermal equilibrium with body C, then body A is in thermal equilibrium with body B.*
Microscopically, thermal equilibrium between A and C implies $\\beta_A = \\beta_C$. Equilibrium between B and C implies $\\beta_B = \\beta_C$.
By the transitivity of real numbers:
$$\\beta_A = \\beta_B \\iff T_A = T_B$$
The Zeroth Law is thus a mathematical consequence of the transitivity of equality for the statistical parameter $\\beta$.

<h4>3. Physical Direction of Heat Flow</h4>
If two systems with $\\beta_1 \\ne \\beta_2$ are placed in thermal contact, spontaneous heat exchange $dE_1 = -dE_2$ changes the total entropy by:
$$dS = dS_1 + dS_2 = \\left(\\frac{\\partial S_1}{\\partial E_1} - \\frac{\\partial S_2}{\\partial E_2}\\right) dE_1 = k_B (\\beta_1 - \\beta_2) dE_1 = \\left(\\frac{1}{T_1} - \\frac{1}{T_2}\\right) dE_1$$
According to the Second Law, $dS > 0$. If $T_1 > T_2$, then $\\frac{1}{T_1} - \\frac{1}{T_2} < 0$, which requires $dE_1 < 0$.
Heat must flow spontaneously from the body with higher temperature to the body with lower temperature."""
    },
    {
        "id": "sec-2-2",
        "number": "§2.2",
        "heading": "Ensembles: The Microcanonical Ensemble",
        "simulation": "microstates-macrostates-sim",
        "content": """An **ensemble** is an idealized mental collection of a very large number $\\mathcal{N}$ of independent, macroscopic replicas of a system, all satisfying identical thermodynamic constraints.

<h4>1. Specification of the Microcanonical Ensemble</h4>
The **Microcanonical Ensemble** represents an **isolated system** with strictly fixed:
<ul>
  <li>Total internal energy $E$ within an infinitesimal range $[E, E + \\delta E]$</li>
  <li>Volume $V$</li>
  <li>Total number of particles $N$</li>
</ul>
No energy or particle exchange occurs with the exterior environment.

<h4>2. Microcanonical Probability Distribution</h4>
According to the Postulate of Equal A Priori Probabilities, every accessible microstate $r$ within the energy shell is equally likely:
$$P_r = \\begin{cases} \\frac{1}{\\Omega(E, V, N)} & \\text{if } E \\le E_r \\le E + \\delta E \\\\ 0 & \\text{otherwise} \\end{cases}$$
The microcanonical partition function $\\Omega(E, V, N)$ is the total number of quantum microstates accessible to the system:
$$\\Omega(E, V, N) = \\sum_{E \\le E_r \\le E + \\delta E} 1 = \\frac{1}{N! \\, h^{3N}} \\int_{E \\le H(q, p) \\le E + \\delta E} d^{3N}q \\, d^{3N}p$$

<h4>3. Thermodynamics from the Microcanonical Ensemble</h4>
The bridge to thermodynamics is Boltzmann's relation:
$$S(E, V, N) = k_B \\ln \\Omega(E, V, N)$$
From the fundamental thermodynamic relation $dE = T dS - P dV + \\mu dN$, or rearranged:
$$dS = \\frac{1}{T} dE + \\frac{P}{T} dV - \\frac{\\mu}{T} dN$$
We determine all thermodynamic quantities directly:
$$\\frac{1}{T} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V, N}, \\quad \\frac{P}{T} = \\left(\\frac{\\partial S}{\\partial V}\\right)_{E, N}, \\quad \\frac{\\mu}{T} = -\\left(\\frac{\\partial S}{\\partial N}\\right)_{E, V}$$"""
    },
    {
        "id": "sec-2-3",
        "number": "§2.3",
        "heading": "The Canonical Ensemble and Connection with Thermodynamics",
        "simulation": "canonical-boltzmann-sim",
        "content": """Most physical systems in laboratory experiments are not isolated; they are maintained at a constant temperature by thermal contact with a large heat bath. This situation is described by the **Canonical Ensemble**.

<h4>1. Derivation of the Boltzmann Canonical Distribution</h4>
Consider a small system $A$ with microstates $r$ of energy $E_r$, in thermal contact with a huge heat reservoir $R$ at temperature $T$. The combined system $A_0 = A + R$ is isolated with total energy $E_0 = E_r + E_R = \\text{constant}$.
The probability $P_r$ of finding system $A$ in a specific microstate $r$ is proportional to the number of accessible states of the reservoir $\\Omega_R(E_0 - E_r)$:
$$P_r \\propto \\Omega_R(E_0 - E_r) = \\exp\\left( \\frac{S_R(E_0 - E_r)}{k_B} \\right)$$
Because the reservoir is much larger than the system ($E_r \\ll E_0$), we expand $S_R$ in a Taylor series about $E_0$:
$$S_R(E_0 - E_r) \\approx S_R(E_0) - E_r \\left(\\frac{\\partial S_R}{\\partial E_R}\\right)_{E_R=E_0} = S_R(E_0) - \\frac{E_r}{T}$$
Therefore:
$$P_r \\propto e^{S_R(E_0)/k_B} \\, e^{-E_r / (k_B T)} = \\text{const} \\times e^{-\\beta E_r}$$
Normalizing $\\sum_r P_r = 1$, we obtain the **Boltzmann Canonical Distribution**:
$$P_r = \\frac{e^{-\\beta E_r}}{Z}$$
where $\\beta = \\frac{1}{k_B T}$, and $Z$ is the **Canonical Partition Function** (German: *Zustandssumme* - sum over states):
$$Z(T, V, N) = \\sum_r e^{-\\beta E_r}$$

<h4>2. Connection with Helmholtz Free Energy ($F$)</h4>
The ensemble average energy is:
$$\\langle E \\rangle = U = \\sum_r P_r E_r = \\frac{1}{Z} \\sum_r E_r e^{-\\beta E_r} = -\\frac{\\partial \\ln Z}{\\partial \\beta}$$
Gibbs defined the statistical entropy as:
$$S = -k_B \\sum_r P_r \\ln P_r = -k_B \\sum_r P_r (-\\beta E_r - \\ln Z) = k_B \\beta \\langle E \\rangle + k_B \\ln Z = \\frac{U}{T} + k_B \\ln Z$$
Rearranging gives $U - TS = -k_B T \\ln Z$.
Recalling the definition of Helmholtz Free Energy $F = U - TS$, we obtain the fundamental bridge:
$$F(T, V, N) = -k_B T \\ln Z(T, V, N)$$

<h4>3. Complete Thermodynamic Equations of State</h4>
From the differential $dF = -S dT - P dV + \\mu dN$, all thermodynamic variables are computed by simple differentiation of $\\ln Z$:
$$S = -\\left(\\frac{\\partial F}{\\partial T}\\right)_{V, N} = k_B \\ln Z + k_B T \\left(\\frac{\\partial \\ln Z}{\\partial T}\\right)_{V, N}$$
$$P = -\\left(\\frac{\\partial F}{\\partial V}\\right)_{T, N} = k_B T \\left(\\frac{\\partial \\ln Z}{\\partial V}\\right)_{T, N}$$
$$\\mu = \\left(\\frac{\\partial F}{\\partial N}\\right)_{T, V} = -k_B T \\left(\\frac{\\partial \\ln Z}{\\partial N}\\right)_{T, V}$$
$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = k_B \\beta^2 \\frac{\\partial^2 \\ln Z}{\\partial \\beta^2}$$"""
    },
    {
        "id": "sec-2-4",
        "number": "§2.4",
        "heading": "The Grand Canonical Ensemble",
        "simulation": "canonical-boltzmann-sim",
        "content": """The **Grand Canonical Ensemble** describes an open system that can exchange both thermal energy and particles with a large reservoir at fixed temperature $T$ and chemical potential $\\mu$.

<h4>1. Grand Canonical Probability Distribution</h4>
Let the system $A$ have state $r$ with energy $E_r$ and particle number $N$. The combined system $A_0 = A + R$ is isolated with total energy $E_0 = E_r + E_R$ and total particles $N_0 = N + N_R$.
Expanding the reservoir entropy $S_R(E_0 - E_r, N_0 - N)$:
$$S_R \\approx S_R(E_0, N_0) - E_r \\left(\\frac{\\partial S_R}{\\partial E_R}\\right) - N \\left(\\frac{\\partial S_R}{\\partial N_R}\\right) = S_R(E_0, N_0) - \\frac{E_r}{T} + \\frac{\\mu N}{T}$$
The grand canonical probability distribution is:
$$P_{r, N} = \\frac{e^{-\\beta (E_r - \\mu N)}}{\\Xi}$$
where $\\Xi(T, V, \\mu)$ is the **Grand Canonical Partition Function**:
$$\\Xi(T, V, \\mu) = \\sum_{N=0}^\\infty \\sum_r e^{-\\beta (E_r - \\mu N)} = \\sum_{N=0}^\\infty z^N Z_N(T, V)$$
Here, $z \\equiv e^{\\beta \\mu} = e^{\\mu / k_B T}$ is called the **fugacity** (absolute activity).

<h4>2. Connection with the Grand Potential ($\\Phi_G$)</h4>
The thermodynamic characteristic potential for open systems is the **Grand Potential** $\\Phi_G$ (also denoted $\\Omega$):
$$\\Phi_G = F - \\mu N = U - TS - \\mu N = -P V$$
Its statistical connection is:
$$\\Phi_G(T, V, \\mu) = -k_B T \\ln \\Xi(T, V, \\mu) = -P V$$
This remarkable relation directly gives the equation of state:
$$P(T, \\mu) = \\frac{k_B T}{V} \\ln \\Xi$$
The mean particle number and its fluctuations are:
$$\\langle N \\rangle = k_B T \\left(\\frac{\\partial \\ln \\Xi}{\\partial \\mu}\\right)_{T, V}$$
$$\\sigma_N^2 = \\langle N^2 \\rangle - \\langle N \\rangle^2 = (k_B T)^2 \\frac{\\partial^2 \\ln \\Xi}{\\partial \\mu^2} = k_B T \\left(\\frac{\\partial \\langle N \\rangle}{\\partial \\mu}\\right)_{T, V}$$"""
    },
    {
        "id": "sec-2-5",
        "number": "§2.5",
        "heading": "Thermodynamic Functions, Potentials, and Equilibrium Conditions",
        "simulation": "canonical-boltzmann-sim",
        "content": """Thermodynamics uses Legendre transformations to define four fundamental thermodynamic potentials, each corresponding to different experimental constraints.

<h4>1. The Four Fundamental Thermodynamic Potentials</h4>
<table style="width:100%; border-collapse:collapse; margin:1rem 0;">
  <tr style="border-bottom:1px solid #334155;">
    <th style="text-align:left; padding:6px;">Potential</th>
    <th style="text-align:left; padding:6px;">Definition</th>
    <th style="text-align:left; padding:6px;">Differential Form</th>
    <th style="text-align:left; padding:6px;">Natural Variables</th>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Internal Energy $U$</strong></td>
    <td style="padding:6px;">$U$</td>
    <td style="padding:6px;">$dU = T dS - P dV + \\mu dN$</td>
    <td style="padding:6px;">$(S, V, N)$</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Helmholtz Free Energy $F$</strong></td>
    <td style="padding:6px;">$F = U - TS$</td>
    <td style="padding:6px;">$dF = -S dT - P dV + \\mu dN$</td>
    <td style="padding:6px;">$(T, V, N)$</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Enthalpy $H$</strong></td>
    <td style="padding:6px;">$H = U + PV$</td>
    <td style="padding:6px;">$dH = T dS + V dP + \\mu dN$</td>
    <td style="padding:6px;">$(S, P, N)$</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Gibbs Free Energy $G$</strong></td>
    <td style="padding:6px;">$G = U - TS + PV$</td>
    <td style="padding:6px;">$dG = -S dT + V dP + \\mu dN$</td>
    <td style="padding:6px;">$(T, P, N)$</td>
  </tr>
</table>

<h4>2. Maxwell Relations</h4>
Because mixed second partial derivatives of state functions are invariant under order of differentiation, we derive the four fundamental **Maxwell Relations**:
$$\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial P}{\\partial S}\\right)_V, \\quad \\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V$$
$$\\left(\\frac{\\partial T}{\\partial P}\\right)_S = \\left(\\frac{\\partial V}{\\partial S}\\right)_P, \\quad \\left(\\frac{\\partial S}{\\partial P}\\right)_T = -\\left(\\frac{\\partial V}{\\partial T}\\right)_P$$

<h4>3. Equilibrium Conditions</h4>
A system undergoing spontaneous evolution at constant:
<ul>
  <li>$(E, V)$: Maximizes entropy $S$ ($dS \\ge 0$, maximum at equilibrium).</li>
  <li>$(T, V)$: Minimizes Helmholtz free energy $F$ ($dF \\le 0$, minimum at equilibrium).</li>
  <li>$(T, P)$: Minimizes Gibbs free energy $G$ ($dG \\le 0$, minimum at equilibrium).</li>
</ul>"""
    },
    {
        "id": "sec-2-6",
        "number": "§2.6",
        "heading": "Statistical Distribution Functions and Energy Fluctuations",
        "simulation": "canonical-boltzmann-sim",
        "content": """Why does the canonical ensemble (where energy fluctuates) yield identical thermodynamic results to the microcanonical ensemble (where energy is strictly fixed)?

<h4>1. Energy Fluctuations in the Canonical Ensemble</h4>
In the canonical ensemble, the average energy is:
$$\\langle E \\rangle = -\\frac{\\partial \\ln Z}{\\partial \\beta} = \\frac{1}{Z} \\sum_r E_r e^{-\\beta E_r}$$
Differentiating $\\langle E \\rangle$ with respect to $\\beta$:
$$\\frac{\\partial \\langle E \\rangle}{\\partial \\beta} = \\frac{\\partial}{\\partial \\beta} \\left( \\frac{1}{Z} \\sum_r E_r e^{-\\beta E_r} \\right) = -\\frac{1}{Z^2} \\left(\\frac{\\partial Z}{\\partial \\beta}\\right) \\sum_r E_r e^{-\\beta E_r} - \\frac{1}{Z} \\sum_r E_r^2 e^{-\\beta E_r}$$
$$\\frac{\\partial \\langle E \\rangle}{\\partial \\beta} = \\langle E \\rangle^2 - \\langle E^2 \\rangle = -(\\langle E^2 \\rangle - \\langle E \\rangle^2) = -\\sigma_E^2$$
Therefore, the variance of energy is:
$$\\sigma_E^2 = -\\frac{\\partial U}{\\partial \\beta} = -\\frac{\\partial U}{\\partial T} \\frac{\\partial T}{\\partial \\beta} = C_V k_B T^2$$

<h4>2. Relative Energy Fluctuations in the Thermodynamic Limit</h4>
For a macroscopic system of $N$ particles:
$$U \\propto N, \\quad C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V \\propto N$$
Therefore, the root-mean-square energy fluctuation is:
$$\\sigma_E = \\sqrt{k_B T^2 C_V} \\propto \\sqrt{N}$$
The relative energy fluctuation is:
$$\\frac{\\sigma_E}{\\langle E \\rangle} = \\frac{\\sqrt{k_B T^2 C_V}}{U} \\propto \\frac{\\sqrt{N}}{N} = \\frac{1}{\\sqrt{N}}$$
For $N = 10^{24}$:
$$\\frac{\\sigma_E}{\\langle E \\rangle} \\approx \\frac{1}{\\sqrt{10^{24}}} = 10^{-12}$$
Energy fluctuations in the canonical ensemble are so vanishingly tiny that canonical and microcanonical ensembles are strictly mathematically equivalent in the thermodynamic limit ($N \\to \\infty$)."""
    },
    {
        "id": "sec-2-7",
        "number": "§2.7",
        "heading": "The Boltzmann Partition Function for Independent Particles",
        "simulation": "canonical-boltzmann-sim",
        "content": """For systems composed of non-interacting, independent particles, the total Hamiltonian is the sum of single-particle Hamiltonians:
$$H(\\mathbf{X}) = \\sum_{i=1}^N h_i(\\mathbf{x}_i)$$

<h4>1. Distinguishable Particles (Localized Lattice Sites)</h4>
If particles are distinguishable (such as atoms fixed at crystal lattice sites), each particle microstate is independent:
$$Z_N = \\sum_{r_1, r_2, \\dots, r_N} e^{-\\beta (\\epsilon_{r_1} + \\epsilon_{r_2} + \\dots + \\epsilon_{r_N})} = \\left( \\sum_{r_1} e^{-\\beta \\epsilon_{r_1}} \\right) \\left( \\sum_{r_2} e^{-\\beta \\epsilon_{r_2}} \\right) \\dots \\left( \\sum_{r_N} e^{-\\beta \\epsilon_{r_N}} \\right)$$
$$Z_N = [z_1(T, V)]^N$$
where $z_1 = \\sum_j e^{-\\beta \\epsilon_j}$ is the **single-particle partition function**.

<h4>2. Indistinguishable Particles and Gibbs' Correction Factor ($1/N!$)</h4>
In a gas of identical atoms, particles are fundamentally indistinguishable. Permuting any two particles does not create a new physical state.
If we used $Z_N = z_1^N$, we would overcount states by $N!$, leading to **Gibbs' Paradox** (entropy not being extensive: mixing two samples of the same gas would erroneously yield an entropy increase).
Gibbs introduced the correct quantum statistical count:
$$Z_N = \\frac{[z_1(T, V)]^N}{N!}$$
Using Stirling's approximation $\\ln(N!) \\approx N \\ln N - N$:
$$\\ln Z_N = N \\ln z_1 - N \\ln N + N = N \\ln\\left(\\frac{z_1}{N}\\right) + N$$

<h4>3. Factorization of Molecular Degrees of Freedom</h4>
For a gas of independent polyatomic molecules, the single-particle Hamiltonian decouples:
$$h_i = h_{\\text{trans}} + h_{\\text{rot}} + h_{\\text{vib}} + h_{\\text{elec}} + h_{\\text{nucl}}$$
The single-particle partition function factorizes into a product:
$$z_1 = z_{\\text{trans}} \\times z_{\\text{rot}} \\times z_{\\text{vib}} \\times z_{\\text{elec}} \\times z_{\\text{nucl}}$$
Each degree of freedom contributes additively to free energy and heat capacity."""
    },
    {
        "id": "sec-2-8",
        "number": "§2.8",
        "heading": "Maxwell-Boltzmann Velocity Distribution and Mean Values",
        "simulation": "canonical-boltzmann-sim",
        "content": """Maxwell (1859) and Boltzmann (1871) derived the fundamental distribution of molecular speeds in an ideal thermal gas.

<h4>1. 3D Velocity Distribution</h4>
For a classical particle of mass $m$, the kinetic energy is $\\epsilon = \\frac{1}{2}m(v_x^2 + v_y^2 + v_z^2)$. The probability of finding a molecule with velocity in range $[\\mathbf{v}, \\mathbf{v} + d^3\\mathbf{v}]$ is:
$$f(v_x, v_y, v_z) \\, dv_x dv_y dv_z = C \\exp\\left( -\\frac{m(v_x^2 + v_y^2 + v_z^2)}{2 k_B T} \\right) dv_x dv_y dv_z$$
Normalizing via standard Gaussian integrals $\\int_{-\\infty}^\\infty e^{-\\alpha v_x^2} dv_x = \\sqrt{\\frac{\\pi}{\\alpha}}$ with $\\alpha = \\frac{m}{2 k_B T}$:
$$f(\\mathbf{v}) = \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right)$$

<h4>2. Maxwell Speed Distribution</h4>
Transforming to spherical velocity coordinates $(v, \\theta, \\phi)$ where $d^3\\mathbf{v} = v^2 \\sin\\theta \\, dv \\, d\\theta \\, d\\phi$, and integrating over angles $\\int_0^{2\\pi} d\\phi \\int_0^\\pi \\sin\\theta d\\theta = 4\\pi$:
$$F(v) \\, dv = 4\\pi \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} v^2 \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) dv$$

<h4>3. Analytical Derivation of Characteristic Molecular Speeds</h4>
<ul>
  <li><strong>Most Probable Speed ($v_p$):</strong> Found by maximizing $F(v)$:
  $$\\frac{dF(v)}{dv} = 0 \\implies \\frac{d}{dv}\\left( v^2 e^{-\\alpha v^2} \\right) = (2v - 2\\alpha v^3)e^{-\\alpha v^2} = 0 \\implies v_p = \\frac{1}{\\sqrt{\\alpha}} = \\sqrt{\\frac{2 k_B T}{m}}$$
  </li>
  <li><strong>Average (Mean) Speed ($\\langle v \\rangle$):</strong>
  $$\\langle v \\rangle = \\int_0^\\infty v F(v) \\, dv = 4\\pi \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} \\int_0^\\infty v^3 e^{-\\frac{m v^2}{2 k_B T}} \\, dv = \\sqrt{\\frac{8 k_B T}{\\pi m}}$$
  </li>
  <li><strong>Root-Mean-Square (RMS) Speed ($v_{\\text{rms}}$):</strong>
  $$\\langle v^2 \\rangle = \\int_0^\\infty v^2 F(v) \\, dv = \\frac{3 k_B T}{m} \\implies v_{\\text{rms}} = \\sqrt{\\langle v^2 \\rangle} = \\sqrt{\\frac{3 k_B T}{m}}$$
  </li>
</ul>
Notice the invariant universal ratio:
$$v_p : \\langle v \\rangle : v_{\\text{rms}} = \\sqrt{2} : \\sqrt{\\frac{8}{\\pi}} : \\sqrt{3} \\approx 1.414 : 1.596 : 1.732$$
The most probable speed is always less than the average, which is always less than the RMS speed."""
    },
    {
        "id": "sec-2-9",
        "number": "§2.9",
        "heading": "The Ideal Monatomic Gas and the Sackur-Tetrode Equation",
        "simulation": "canonical-boltzmann-sim",
        "content": """We now derive the complete thermodynamic properties of an ideal monatomic gas from microscopic first principles.

<h4>1. Translational Partition Function ($z_{\\text{trans}}$)</h4>
For a single particle confined in volume $V$:
$$z_{\\text{trans}} = \\frac{1}{h^3} \\int_V d^3\\mathbf{r} \\int_{-\\infty}^\\infty d^3\\mathbf{p} \\, e^{-\\beta p^2 / (2m)} = \\frac{V}{h^3} \\left( \\int_{-\\infty}^\\infty e^{-\\beta p_x^2 / 2m} dp_x \\right)^3 = \\frac{V}{h^3} (2\\pi m k_B T)^{3/2}$$
We define the **thermal de Broglie wavelength** $\\lambda_{\\text{th}}$:
$$\\lambda_{\\text{th}} \\equiv \\frac{h}{\\sqrt{2\\pi m k_B T}}$$
Thus:
$$z_{\\text{trans}} = \\frac{V}{\\lambda_{\\text{th}}^3}$$

<h4>2. $N$-Particle Partition Function and Helmholtz Free Energy</h4>
Applying Gibbs' indistinguishability factor $1/N!$:
$$Z_N = \\frac{z_{\\text{trans}}^N}{N!} = \\frac{1}{N!} \\left( \\frac{V}{\\lambda_{\\text{th}}^3} \\right)^N$$
$$F = -k_B T \\ln Z_N = -N k_B T \\left[ \\ln\\left( \\frac{V}{N \\lambda_{\\text{th}}^3} \\right) + 1 \\right]$$

<h4>3. Derivation of the Ideal Gas Law and Internal Energy</h4>
Pressure is obtained by volume differentiation:
$$P = -\\left(\\frac{\\partial F}{\\partial V}\\right)_{T, N} = N k_B T \\frac{\\partial}{\\partial V}\\ln V = \\frac{N k_B T}{V} \\implies P V = N k_B T$$
The Ideal Gas Equation of State is derived microscopically!
The internal energy is:
$$U = -\\frac{\\partial \\ln Z_N}{\\partial \\beta} = N \\left( -\\frac{\\partial}{\\partial \\beta}\\ln\\beta^{-3/2} \\right) = \\frac{3}{2} N k_B T$$
The heat capacity at constant volume is:
$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = \\frac{3}{2} N k_B = \\frac{3}{2} n R$$

<h4>4. The Sackur-Tetrode Equation for Entropy</h4>
Using $S = -\\left(\\frac{\\partial F}{\\partial T}\\right)_{V, N}$:
$$S = N k_B \\left[ \\ln\\left( \\frac{V}{N \\lambda_{\\text{th}}^3} \\right) + \\frac{5}{2} \\right] = N k_B \\left[ \\ln\\left( \\frac{V}{N} \\left(\\frac{2\\pi m k_B T}{h^2}\\right)^{3/2} \\right) + \\frac{5}{2} \\right]$$
This is the renowned **Sackur-Tetrode Equation** (1912). It provides the absolute entropy of an ideal gas and explicitly contains Planck's constant $h$, proving that classical thermodynamics requires quantum mechanics for complete consistency!"""
    },
    {
        "id": "sec-2-10",
        "number": "§2.10",
        "heading": "The Classical and Quantum Harmonic Oscillator",
        "simulation": "equipartition-dof-sim",
        "content": """The harmonic oscillator is the foundation for modeling vibrational states of molecules and lattice vibrations in solids.

<h4>1. The Classical Harmonic Oscillator</h4>
For a 1D classical oscillator with Hamiltonian $H = \\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 q^2$:
$$z_{\\text{class}} = \\frac{1}{h} \\int_{-\\infty}^\\infty dq \\int_{-\\infty}^\\infty dp \\, e^{-\\beta \\left(\\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 q^2\\right)}$$
Using Gaussian integrals $\\int e^{-\\alpha u^2} du = \\sqrt{\\pi / \\alpha}$:
$$z_{\\text{class}} = \\frac{1}{h} \\sqrt{\\frac{2\\pi m}{\\beta}} \\sqrt{\\frac{2\\pi}{m\\omega^2 \\beta}} = \\frac{2\\pi}{\\beta \\omega h} = \\frac{k_B T}{\\hbar \\omega}$$
The average energy is:
$$\\langle E \\rangle_{\\text{class}} = -\\frac{\\partial \\ln z_{\\text{class}}}{\\partial \\beta} = \\frac{1}{\\beta} = k_B T$$
Each degree of freedom (kinetic and potential) contributes $\\frac{1}{2}k_B T$, giving $k_B T$ total.

<h4>2. The Quantum Harmonic Oscillator</h4>
In quantum mechanics, energy levels are quantized:
$$E_n = \\left(n + \\frac{1}{2}\\right)\\hbar \\omega, \\quad n = 0, 1, 2, \\dots$$
The quantum partition function is a geometric series:
$$z_{\\text{quant}} = \\sum_{n=0}^\\infty e^{-\\beta \\hbar \\omega (n + 1/2)} = e^{-\\beta \\hbar \\omega / 2} \\sum_{n=0}^\\infty \\left(e^{-\\beta \\hbar \\omega}\\right)^n = \\frac{e^{-\\beta \\hbar \\omega / 2}}{1 - e^{-\\beta \\hbar \\omega}} = \\frac{1}{2 \\sinh(\\beta \\hbar \\omega / 2)}$$
The average energy is:
$$\\langle E \\rangle_{\\text{quant}} = -\\frac{\\partial \\ln z_{\\text{quant}}}{\\partial \\beta} = \\frac{1}{2}\\hbar \\omega + \\frac{\\hbar \\omega}{e^{\\beta \\hbar \\omega} - 1}$$
Here $\\frac{1}{2}\\hbar \\omega$ is the **Zero-Point Energy**, and $\\frac{1}{e^{\\beta \\hbar \\omega} - 1}$ is the Planck-Bose distribution of thermal oscillator quanta (phonons).

<h4>3. High- and Low-Temperature Limits</h4>
<ul>
  <li><strong>High Temperature ($k_B T \\gg \\hbar \\omega$):</strong> Expanding $e^{\\beta \\hbar \\omega} - 1 \\approx \\beta \\hbar \\omega$:
  $$\\langle E \\rangle \\approx \\frac{1}{2}\\hbar \\omega + \\frac{\\hbar \\omega}{\\beta \\hbar \\omega} = k_B T + \\frac{1}{2}\\hbar \\omega \\to k_B T$$
  The quantum result recovers the classical equipartition theorem!</li>
  <li><strong>Low Temperature ($k_B T \\ll \\hbar \\omega$):</strong> As $T \\to 0$, $e^{\\beta \\hbar \\omega} \\to \\infty$:
  $$\\langle E \\rangle \\to \\frac{1}{2}\\hbar \\omega$$
  Thermal excitations vanish; the oscillator is frozen into its quantum ground state.</li>
</ul>"""
    },
    {
        "id": "sec-2-11",
        "number": "§2.11",
        "heading": "Specific Heat of Solids and the Classical Limit",
        "simulation": "equipartition-dof-sim",
        "content": """The specific heat of crystalline solids provided the first historical proof of the breakdown of classical statistical mechanics and the necessity of quantum physics.

<h4>1. The Classical Dulong-Petit Law (1819)</h4>
In a 3D crystalline solid containing $N$ atoms, each atom oscillates around its equilibrium lattice site in three dimensions.
The system can be modeled as $3N$ independent 1D harmonic oscillators.
According to the classical equipartition theorem, each harmonic oscillator has two quadratic energy terms (kinetic $\\frac{p^2}{2m}$ and potential $\\frac{1}{2}m\\omega^2 q^2$), each contributing $\\frac{1}{2}k_B T$:
$$U = 3N \\times k_B T = 3 N k_B T$$
The heat capacity at constant volume is:
$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = 3 N k_B$$
For one mole of atoms ($N = N_A$):
$$C_V = 3 N_A k_B = 3 R \\approx 3 \\times 8.314\\text{ J/(mol}\\cdot\\text{K)} = 24.94\\text{ J/(mol}\\cdot\\text{K)}$$
This is the empirical **Dulong-Petit Law**.

<h4>2. The Classical Breakdown at Low Temperatures</h4>
Experimentally, while the Dulong-Petit law holds well at room temperature for heavy metals (lead, copper), it fails completely for light, stiff solids like diamond at room temperature, and **fails for all solids as $T \\to 0$**.
Experimentally:
$$\\lim_{T \\to 0} C_V(T) = 0$$
Classical mechanics predicts a strictly constant $C_V = 3R$ down to absolute zero, in direct violation of the Third Law of Thermodynamics (Nernst Heat Theorem).
The resolution of this crisis was achieved by Albert Einstein (1907) and Peter Debye (1912) by applying quantum quantization to lattice vibrations."""
    }
]

u2_problems = [
    {
        "id": "prob-2-1",
        "difficulty": "Medium",
        "title": "Equipartition Theorem and Heat Capacity of a Diatomic Gas",
        "question": "A container contains $N$ molecules of a rigid diatomic gas (e.g., $N_2$ at room temperature). Each molecule has 3 translational degrees of freedom and 2 rotational degrees of freedom, while vibrational modes are frozen ($k_B T \\ll \\hbar \\omega_{\\text{vib}}$). (a) Use the classical equipartition theorem to calculate the total internal energy $U$ and molar heat capacities $C_V$ and $C_P$. (b) Determine the adiabatic index $\\gamma = C_P / C_V$.",
        "steps": [
            {
                "title": "Step 1: Count quadratic degrees of freedom",
                "math": "$$f = f_{\\text{trans}} + f_{\\text{rot}} = 3 + 2 = 5$$",
                "explanation": "Because the molecule is linear, rotation about the internuclear axis has negligible moment of inertia, leaving exactly 2 active rotational degrees of freedom."
            },
            {
                "title": "Step 2: Apply the equipartition theorem for internal energy",
                "math": "$$U = N \\times \\frac{f}{2} k_B T = \\frac{5}{2} N k_B T = \\frac{5}{2} n R T$$",
                "explanation": "Each quadratic degree of freedom contributes $\\frac{1}{2}k_B T$ to the internal energy."
            },
            {
                "title": "Step 3: Calculate heat capacities and adiabatic index",
                "math": "$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = \\frac{5}{2} n R \\implies c_V = \\frac{5}{2} R \\approx 20.79\\text{ J/(mol}\\cdot\\text{K)}$$\n$$C_P = C_V + n R = \\frac{7}{2} n R \\implies c_P = \\frac{7}{2} R \\approx 29.10\\text{ J/(mol}\\cdot\\text{K)}$$\n$$\\gamma = \\frac{C_P}{C_V} = \\frac{7/2 R}{5/2 R} = \\frac{7}{5} = 1.40$$",
                "explanation": "This precisely matches the experimental adiabatic index of air and diatomic nitrogen ($\gamma = 1.40$)."
            }
        ]
    },
    {
        "id": "prob-2-2",
        "difficulty": "Hard",
        "title": "Sackur-Tetrode Entropy Calculation for Argon Gas",
        "question": "One mole ($N_A = 6.022 \\times 10^{23}$) of argon gas (atomic mass $M = 39.95\\text{ g/mol}$) is at standard temperature and pressure ($T = 298.15\\text{ K}, P = 1.013 \\times 10^5\\text{ Pa}$). Using the Sackur-Tetrode equation, calculate the absolute molar entropy $S$ from fundamental quantum constants and compare with the experimental value ($154.8\\text{ J/(mol}\\cdot\\text{K)}$).",
        "steps": [
            {
                "title": "Step 1: Compute particle mass and volume per particle",
                "math": "$$m = \\frac{M}{N_A} = \\frac{0.03995\\text{ kg/mol}}{6.022 \\times 10^{23}\\text{ mol}^{-1}} = 6.634 \\times 10^{-26}\\text{ kg}$$\n$$V = \\frac{n R T}{P} = \\frac{(1)(8.314)(298.15)}{1.013 \\times 10^5} = 0.02447\\text{ m}^3$$\n$$\\frac{V}{N} = \\frac{0.02447}{6.022 \\times 10^{23}} = 4.063 \\times 10^{-26}\\text{ m}^3$$",
                "explanation": "This establishes the average volume available to a single argon atom in the gas phase."
            },
            {
                "title": "Step 2: Calculate the thermal de Broglie wavelength",
                "math": "$$\\lambda_{\\text{th}} = \\frac{h}{\\sqrt{2\\pi m k_B T}} = \\frac{6.626 \\times 10^{-34}}{\\sqrt{2\\pi (6.634 \\times 10^{-26})(1.381 \\times 10^{-23})(298.15)}} = 1.601 \\times 10^{-11}\\text{ m} = 0.1601\\text{ Å}$$\n$$\\lambda_{\\text{th}}^3 = (1.601 \\times 10^{-11})^3 = 4.103 \\times 10^{-33}\\text{ m}^3$$",
                "explanation": "Because $\\lambda_{\\text{th}} \\ll (V/N)^{1/3} \\approx 34\\text{ Å}$, quantum wavepackets do not overlap, confirming the validity of classical Maxwell-Boltzmann statistics."
            },
            {
                "title": "Step 3: Evaluate the Sackur-Tetrode formula",
                "math": "$$\\frac{V}{N \\lambda_{\\text{th}}^3} = \\frac{4.063 \\times 10^{-26}}{4.103 \\times 10^{-33}} = 9.902 \\times 10^6$$\n$$\\ln\\left(\\frac{V}{N \\lambda_{\\text{th}}^3}\\right) = \\ln(9.902 \\times 10^6) = 16.108$$\n$$S = N_A k_B \\left[ 16.108 + 2.5 \\right] = R [18.608] = 8.314 \\times 18.608 = 154.71\\text{ J/(mol}\\cdot\\text{K)}$$",
                "explanation": "The derived theoretical entropy ($154.71\\text{ J/(mol}\\cdot\\text{K)}$) matches the experimental calorimeter measurement ($154.8\\text{ J/(mol}\\cdot\\text{K)}$) to within $0.06\\%$, demonstrating the predictive power of statistical thermodynamics."
            }
        ]
    },
    {
        "id": "prob-2-3",
        "difficulty": "Hard",
        "title": "Einstein Model of Heat Capacity of a Solid",
        "question": "In the Einstein model of a solid, $N$ atoms are treated as $3N$ independent quantum harmonic oscillators with identical frequency $\\omega_E$. (a) Derive the Einstein expression for heat capacity $C_V(T)$. (b) Define the Einstein temperature $\\Theta_E = \\hbar \\omega_E / k_B$ and show that $C_V$ vanishes exponentially as $T \\to 0$.",
        "steps": [
            {
                "title": "Step 1: Write down total energy for 3N quantum oscillators",
                "math": "$$U = 3N \\langle \\epsilon \\rangle = 3N \\left( \\frac{1}{2}\\hbar \\omega_E + \\frac{\\hbar \\omega_E}{e^{\\hbar \\omega_E / k_B T} - 1} \\right) = \\frac{3}{2}N \\hbar \\omega_E + \\frac{3N k_B \\Theta_E}{e^{\\Theta_E / T} - 1}$$",
                "explanation": "Here $\\Theta_E \\equiv \\frac{\\hbar \\omega_E}{k_B}$ is the characteristic Einstein temperature of the solid."
            },
            {
                "title": "Step 2: Differentiate with respect to temperature to find C_V",
                "math": "$$C_V = \\frac{\\partial U}{\\partial T} = 3N k_B \\Theta_E \\left( -\\frac{1}{(e^{\\Theta_E / T} - 1)^2} \\right) e^{\\Theta_E / T} \\left( -\\frac{\\Theta_E}{T^2} \\right)$$\n$$C_V(T) = 3 N k_B \\left(\\frac{\\Theta_E}{T}\\right)^2 \\frac{e^{\\Theta_E / T}}{(e^{\\Theta_E / T} - 1)^2}$$",
                "explanation": "This is the famous Einstein Heat Capacity formula."
            },
            {
                "title": "Step 3: Analyze the low-temperature limit (T << \\Theta_E)",
                "math": "$$\\text{As } T \\to 0, \\quad e^{\\Theta_E / T} \\gg 1 \\implies e^{\\Theta_E / T} - 1 \\approx e^{\\Theta_E / T}$$\n$$C_V(T) \\approx 3 N k_B \\left(\\frac{\\Theta_E}{T}\\right)^2 \\frac{e^{\\Theta_E / T}}{e^{2\\Theta_E / T}} = 3 N k_B \\left(\\frac{\\Theta_E}{T}\\right)^2 e^{-\\Theta_E / T} \\xrightarrow{T \\to 0} 0$$",
                "explanation": "Because $e^{-\\Theta_E/T}$ drops to zero faster than any power of $T$, the specific heat freezes to zero, explaining the observed failure of the classical Dulong-Petit law."
            }
        ]
    }
]

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/unit2_data.json', 'w') as f:
    json.dump({"number": 2, "title": "Statistics and Thermodynamics", "leadSummary": "Statistical temperature, microcanonical, canonical, and grand canonical ensembles, free energy, Maxwell velocity distribution, ideal gas Sackur-Tetrode equation, harmonic oscillators, and specific heat.", "sections": u2_sections, "problems": u2_problems}, f, indent=2)

print("Unit 2 built successfully with 11 topics and 3 solved problems!")
