# build_ssp2_units_3_4.py
# Generates ssp2_u3.json and ssp2_u4.json for Course #18: Solid State Physics II

import json

# =========================================================================
# UNIT 3: Microscopic Magnetism: Diamagnetism, Paramagnetism & Quantum Exchange
# =========================================================================

u3_data = {
    "title": "Microscopic Magnetism: Diamagnetism, Paramagnetism & Quantum Exchange",
    "subtitle": "Larmor Precession, Brillouin Function, Hund's Rules & Exchange Interactions",
    "summary": "This unit establishes the quantum mechanical foundation of magnetism in solids from the isolated atom to macroscopic solids. We derive Larmor diamagnetism and contrast classical Langevin paramagnetism with the quantum Brillouin theory governed by Hund's rules and crystal-field split multiplets. We examine Van Vleck temperature-independent paramagnetism alongside Pauli spin paramagnetism and Landau diamagnetism in Fermi liquids. Finally, we resolve the historical Bohr-van Leeuwen theorem by showing that magnetic ordering originates from electrostatic Coulomb repulsion coupled with Pauli exclusion, formulating the Heisenberg exchange Hamiltonian, Anderson superexchange, and oscillatory RKKY interactions.",
    "sections": [
        {
            "id": "sec-3-1",
            "title": "Classical & Quantum Theory of Diamagnetism: Larmor Precession & Langevin Susceptibility",
            "content": r"""
<h3>1. Classical Larmor Precession</h3>
<p>
Consider an electron with mass $m$ and charge $-e$ in a central atomic potential $V(r)$. When an external magnetic field $\vec{B} = B\hat{z}$ is switched on, the electron experiences the Lorentz force $-e(\vec{v} \times \vec{B})$.
</p>
<p>
Transforming into a coordinate frame rotating with angular velocity $\vec{\omega}_L$:
</p>
$$\vec{\omega}_L = \frac{e\vec{B}}{2m}$$
<p>
The Coriolis force $-2m(\vec{\omega}_L \times \vec{v}')$ exactly cancels the Lorentz force to first order in $B$. This precession of the electronic orbits at the <strong>Larmor frequency</strong> $\omega_L$ constitutes an effective circulating electric current:
</p>
$$I = -\frac{Z e}{2\pi} \omega_L = -\frac{Z e^2 B}{4\pi m}$$
<p>
The induced magnetic dipole moment opposing the applied field is:
</p>
$$\mu_{\text{ind}} = I \cdot \langle A \rangle = -\frac{Z e^2 B}{4\pi m} \pi \langle \rho^2 \rangle = -\frac{Z e^2 B}{4m} \langle x^2 + y^2 \rangle$$
<p>
For spherically symmetric atomic charge distributions, $\langle x^2 \rangle = \langle y^2 \rangle = \langle z^2 \rangle = \frac{1}{3}\langle r^2 \rangle$, so $\langle x^2 + y^2 \rangle = \frac{2}{3}\langle r^2 \rangle$. The induced magnetic dipole moment per atom is:
</p>
$$\vec{\mu}_{\text{ind}} = -\frac{Z e^2}{6m} \langle r^2 \rangle \vec{B}$$

<h3>2. Langevin Diamagnetic Susceptibility</h3>
<p>
In a macroscopic sample with atomic number density $N$, the magnetization $\vec{M} = N \vec{\mu}_{\text{ind}}$ yields the <strong>Langevin diamagnetic susceptibility</strong>:
</p>
$$\chi_{\text{dia}} = \frac{\mu_0 M}{B} = -\frac{\mu_0 N Z e^2}{6m} \langle r^2 \rangle$$
<p>
Quantum mechanically, this result is derived from first-order perturbation theory using the diamagnetic term $\frac{e^2}{8m} \sum_i (\vec{B} \times \vec{r}_i)^2$ in the minimal coupling Hamiltonian $(\vec{p} + e\vec{A})^2/2m$. Diamagnetism is fundamentally <em>temperature-independent</em> and negative, characteristic of all closed-shell inert gas atoms (He, Ne, Ar) and noble metal core ions.
</p>
"""
        },
        {
            "id": "sec-3-2",
            "title": "Classical Theory of Paramagnetism: The Langevin Function & Curie's Law",
            "content": r"""
<h3>1. Statistical Mechanics of Classical Magnetic Dipoles</h3>
<p>
Atoms or molecules with unfilled shells possess a permanent microscopic magnetic dipole moment $\vec{\mu}$. In an external magnetic field $\vec{B} = B\hat{z}$, the classical potential energy is:
</p>
$$U(\theta) = -\vec{\mu} \cdot \vec{B} = -\mu B \cos\theta$$
<p>
According to Maxwell-Boltzmann statistics, the probability of finding a dipole oriented at polar angle $\theta$ within solid angle $d\Omega = 2\pi\sin\theta d\theta$ is:
</p>
$$P(\theta) d\theta = \frac{e^{\mu B \cos\theta / k_B T} \sin\theta d\theta}{\int_0^\pi e^{\mu B \cos\theta / k_B T} \sin\theta d\theta}$$
<p>
Defining the dimensionless parameter $x \equiv \frac{\mu B}{k_B T}$:
</p>
$$\langle \cos\theta \rangle = \frac{\int_{-1}^1 u e^{x u} du}{\int_{-1}^1 e^{x u} du} = \frac{d}{dx} \ln\left( \frac{e^x - e^{-x}}{x} \right) = \coth x - \frac{1}{x} \equiv L(x)$$
<p>
where $L(x)$ is the <strong>Langevin function</strong>.
</p>

<h3>2. The Langevin Function & Curie's Law</h3>
<p>
The total macroscopic magnetization for $N$ dipoles per unit volume is:
</p>
$$M(B, T) = N \mu L(x) = N \mu \left( \coth\left(\frac{\mu B}{k_B T}\right) - \frac{k_B T}{\mu B} \right)$$
<ul>
  <li><strong>Weak Field Limit ($x \ll 1$, high temperature):</strong>
  Expanding $\coth x \approx \frac{1}{x} + \frac{x}{3} - \frac{x^3}{45} + \dots$:
  $$L(x) \approx \frac{x}{3} = \frac{\mu B}{3 k_B T}$$
  $$M \approx \frac{N \mu^2 B}{3 k_B T} \implies \chi_{\text{para}} = \frac{\mu_0 M}{B} = \frac{\mu_0 N \mu^2}{3 k_B T} = \frac{C}{T}$$
  This is the classical <strong>Curie's Law</strong>, where $C = \frac{\mu_0 N \mu^2}{3 k_B}$ is the Curie constant.</li>
  <li><strong>Strong Field Limit ($x \gg 1$, low temperature):</strong>
  $\coth x \to 1$, so $L(x) \to 1 - \frac{1}{x} \to 1$. All dipoles align perfectly parallel to the field, reaching the saturation magnetization:
  $$M_{\text{sat}} = N \mu$$</li>
</ul>
"""
        },
        {
            "id": "sec-3-3",
            "title": "Quantum Theory of Paramagnetism: Hund's Rules, Landé $g$-Factor & The Brillouin Function",
            "content": r"""
<h3>1. Atomic Multi-Electron States & Hund's Rules</h3>
<p>
In open $d$- or $f$-electron shells, electron-electron Coulomb repulsion and spin-orbit coupling determine the total orbital angular momentum $\vec{L} = \sum \vec{l}_i$, total spin $\vec{S} = \sum \vec{s}_i$, and total angular momentum $\vec{J} = \vec{L} + \vec{S}$. According to <strong>Hund's Empirical Rules</strong>, the ground state multiplet maximizes:
</p>
<ol>
  <li>$S$: Total spin is maximized to reduce Coulomb repulsion via exchange holes.</li>
  <li>$L$: Total orbital angular momentum is maximized subject to the maximum $S$.</li>
  <li>$J$: $J = |L - S|$ for shells less than half full; $J = L + S$ for shells more than half full.</li>
</ol>
<p>
The total magnetic dipole operator is $\hat{\vec{\mu}} = -\mu_B (\hat{\vec{L}} + 2\hat{\vec{S}}) = -g_J \mu_B \hat{\vec{J}}$, where $g_J$ is the <strong>Landé $g$-factor</strong>:
</p>
$$g_J = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)}$$

<h3>2. The Quantum Brillouin Function</h3>
<p>
In an external field $B\hat{z}$, spatial quantization restricts the magnetic quantum number $m_J$ to discrete values:
</p>
$$m_J = -J, -J+1, \dots, +J \quad (2J+1 \text{ states})$$
$$E_{m_J} = -g_J \mu_B B m_J$$
<p>
The canonical partition function is a finite geometric series:
</p>
$$Z = \sum_{m_J = -J}^J \exp\left( \frac{g_J \mu_B B m_J}{k_B T} \right) = \frac{\sinh\left( \frac{2J+1}{2J} x \right)}{\sinh\left( \frac{1}{2J} x \right)}, \quad x \equiv \frac{g_J \mu_B J B}{k_B T}$$
<p>
The thermal average magnetization is $M = N k_B T \frac{\partial \ln Z}{\partial B} = N g_J \mu_B J \mathcal{B}_J(x)$, where $\mathcal{B}_J(x)$ is the <strong>Brillouin function</strong>:
</p>
$$\mathcal{B}_J(x) \equiv \frac{2J+1}{2J} \coth\left( \frac{2J+1}{2J} x \right) - \frac{1}{2J} \coth\left( \frac{1}{2J} x \right)$$
<ul>
  <li>For $x \ll 1$, expanding $\coth u \approx \frac{1}{u} + \frac{u}{3}$ gives:
  $$\mathcal{B}_J(x) \approx \frac{J+1}{3J} x \implies M \approx \frac{N g_J^2 \mu_B^2 J(J+1) B}{3 k_B T}$$
  $$\chi_{\text{quantum}} = \frac{\mu_0 N p_{\text{eff}}^2 \mu_B^2}{3 k_B T}, \quad p_{\text{eff}} \equiv g_J \sqrt{J(J+1)}$$</li>
  <li>In the classical limit where $J \to \infty$ while $g_J \mu_B J \equiv \mu$ remains constant:
  $$\lim_{J \to \infty} \mathcal{B}_J(x) = L(x) \quad (\text{Exact Langevin function!})$$</li>
</ul>
""",
            "simulation": "ssp2-brillouin-paramagnetism-sim",
            "simulations": ["ssp2-brillouin-paramagnetism-sim"]
        },
        {
            "id": "sec-3-4",
            "title": "Van Vleck Paramagnetism & Conduction Electron Magnetism (Pauli Spin & Landau Orbital)",
            "content": r"""
<h3>1. Van Vleck Temperature-Independent Paramagnetism</h3>
<p>
When an atom or ion has a non-magnetic ground state ($J = 0$, such as $\text{Eu}^{3+}$ or closed subshells) with low-lying excited states $|n\rangle$ separated by energy $\Delta_n = E_n - E_0$, second-order perturbation theory yields an energy shift quadratic in $B$:
</p>
$$\Delta E_0^{(2)} = -\sum_{n \ne 0} \frac{|\langle 0 | \mu_B (\hat{\vec{L}} + 2\hat{\vec{S}}) \cdot \vec{B} | n \rangle|^2}{E_n - E_0}$$
<p>
This gives rise to a positive, strictly <strong>temperature-independent paramagnetic susceptibility</strong> known as <strong>Van Vleck paramagnetism</strong>:
</p>
$$\chi_{\text{VV}} = 2\mu_0 N \mu_B^2 \sum_{n \ne 0} \frac{|\langle 0 | \hat{L}_z + 2\hat{S}_z | n \rangle|^2}{E_n - E_0} > 0$$

<h3>2. Pauli Spin Paramagnetism & Landau Diamagnetism in Metals</h3>
<p>
In simple metals, the conduction electrons form a degenerate Fermi sea ($T \ll T_F \sim 50{,}000\text{ K}$). An external magnetic field $B$ shifts the energy of spin-up electrons down by $\mu_B B$ and spin-down electrons up by $\mu_B B$:
</p>
$$E_{\uparrow}(k) = E(k) - \mu_B B, \quad E_{\downarrow}(k) = E(k) + \mu_B B$$
<p>
Because only electrons within a thermal energy slice $\sim k_B T$ around the Fermi surface can flip their spins into unoccupied states:
</p>
$$\delta n = \frac{1}{2} g(E_F) \mu_B B - \left(-\frac{1}{2} g(E_F) \mu_B B\right) = g(E_F) \mu_B B$$
<p>
The resulting magnetic moment per unit volume is $M = \mu_B \delta n = \mu_B^2 g(E_F) B$, yielding the <strong>Pauli spin susceptibility</strong>:
</p>
$$\chi_{\text{Pauli}} = \mu_0 \mu_B^2 g(E_F) = \frac{3 \mu_0 n \mu_B^2}{2 E_F}$$
<p>
Unlike Curie paramagnetism, $\chi_{\text{Pauli}}$ is virtually temperature-independent!
</p>
<p>
Simultaneously, the orbital motion of conduction electrons is quantized into discrete Landau levels $E_n = (n + 1/2)\hbar\omega_c + \frac{\hbar^2 k_z^2}{2m}$. Calculating the free energy via Poisson summation reveals <strong>Landau orbital diamagnetism</strong>:
</p>
$$\chi_{\text{Landau}} = -\frac{1}{3} \left( \frac{m}{m^*} \right)^2 \chi_{\text{Pauli}}$$
<p>
For free electrons ($m^* = m$), the total electronic susceptibility is $\chi_{\text{total}} = \chi_{\text{Pauli}} + \chi_{\text{Landau}} = +\frac{2}{3}\chi_{\text{Pauli}} > 0$.
</p>
"""
        },
        {
            "id": "sec-3-5",
            "title": "The Microscopic Origin of Magnetic Ordering: Coulomb Interaction & Pauli Principle",
            "content": r"""
<h3>1. Failure of Dipolar Interaction & The Bohr-van Leeuwen Theorem</h3>
<p>
The classical Bohr-van Leeuwen theorem states that at thermal equilibrium, the partition function of any classical charged system with Hamiltonian $\mathcal{H}(\vec{r}_i, \vec{p}_i + e\vec{A})$ is completely independent of the vector potential $\vec{A}$ because the momentum integral over $(-\infty, \infty)$ simply shifts by $-e\vec{A}$. Therefore:
</p>
$$\vec{M} = -\frac{\partial F}{\partial \vec{B}} = 0 \quad (\text{Classical magnetism is impossible!})$$
<p>
Furthermore, direct magnetic dipole-dipole interactions between neighboring atomic moments separated by $a \approx 2.5\text{ \AA}$ have an energy scale of:
</p>
$$E_{\text{dipole}} \sim \frac{\mu_0 \mu_B^2}{4\pi a^3} \approx 10^{-23}\text{ J} \sim 10^{-4}\text{ eV} \implies T_C \approx \frac{E_{\text{dipole}}}{k_B} \sim 1\text{ K}$$
<p>
Yet iron ($\text{Fe}$) is ferromagnetic up to $T_C = 1043\text{ K}$ ($k_B T_C \approx 0.1\text{ eV}$)! Dipolar forces are over <strong>three orders of magnitude too weak</strong> to explain ferromagnetism.
</p>

<h3>2. Quantum Origin: Coulomb Repulsion + Antisymmetry</h3>
<p>
According to the Pauli exclusion principle, the total electronic wavefunction for a two-electron system must be antisymmetric under particle exchange:
</p>
$$\Psi(1, 2) = \psi_{\text{spatial}}(\vec{r}_1, \vec{r}_2) \chi_{\text{spin}}(s_1, s_2) = -\Psi(2, 1)$$
<ul>
  <li><strong>Singlet Spin State ($S = 0$, antiparallel spins):</strong> Spin function is antisymmetric, requiring a <strong>symmetric spatial wavefunction</strong>:
  $$\psi_S(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}} [\phi_a(\vec{r}_1)\phi_b(\vec{r}_2) + \phi_b(\vec{r}_1)\phi_a(\vec{r}_2)]$$
  Here $\psi_S(\vec{r}, \vec{r}) \ne 0$: electrons can be close together, increasing their mutual electrostatic Coulomb repulsion energy.</li>
  <li><strong>Triplet Spin State ($S = 1$, parallel spins):</strong> Spin function is symmetric, requiring an <strong>antisymmetric spatial wavefunction</strong>:
  $$\psi_A(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}} [\phi_a(\vec{r}_1)\phi_b(\vec{r}_2) - \phi_b(\vec{r}_1)\phi_a(\vec{r}_2)]$$
  Here $\psi_A(\vec{r}, \vec{r}) = 0$: the spatial Pauli exchange hole keeps the two electrons apart, drastically lowering their electrostatic repulsion energy!</li>
</ul>
<p>
The energy difference between the singlet and triplet configurations is:
</p>
$$E_S - E_T = 2 J_{\text{ex}}$$
<p>
where $J_{\text{ex}} = \iint \phi_a^*(\vec{r}_1)\phi_b^*(\vec{r}_2) \frac{e^2}{4\pi\epsilon_0 |\vec{r}_1 - \vec{r}_2|} \phi_b(\vec{r}_1)\phi_a(\vec{r}_2) d^3r_1 d^3r_2$ is the <strong>exchange integral</strong>. Magnetic ordering is a purely electrostatic Coulomb phenomenon disguised as a magnetic interaction!
</p>
"""
        },
        {
            "id": "sec-3-6",
            "title": "The Heisenberg Exchange Hamiltonian & Direct vs Indirect Exchange Mechanisms",
            "content": r"""
<h3>1. The Heisenberg Exchange Hamiltonian</h3>
<p>
For two electrons with spins $\vec{S}_1$ and $\vec{S}_2$ (in units of $\hbar$), the total spin operator is $\vec{S}_{\text{tot}} = \vec{S}_1 + \vec{S}_2$:
</p>
$$\vec{S}_{\text{tot}}^2 = \vec{S}_1^2 + \vec{S}_2^2 + 2\vec{S}_1 \cdot \vec{S}_2 = \frac{3}{4} + \frac{3}{4} + 2\vec{S}_1 \cdot \vec{S}_2 = \frac{3}{2} + 2\vec{S}_1 \cdot \vec{S}_2$$
<p>
Evaluating the eigenvalues:
</p>
$$\vec{S}_1 \cdot \vec{S}_2 = \begin{cases} -\frac{3}{4}, & S = 0 \text{ (Singlet)} \\ +\frac{1}{4}, & S = 1 \text{ (Triplet)} \end{cases}$$
<p>
We can write the effective spin-dependent Hamiltonian as:
</p>
$$\hat{\mathcal{H}} = \frac{1}{4}(E_S + 3E_T) - (E_S - E_T) \vec{S}_1 \cdot \vec{S}_2 = \text{const} - 2 J_{\text{ex}} \vec{S}_1 \cdot \vec{S}_2$$
<p>
Generalizing to a macroscopic lattice of localized spins yields the famous <strong>Heisenberg Hamiltonian</strong>:
</p>
$$\hat{\mathcal{H}}_{\text{Heisenberg}} = -2 \sum_{i < j} J_{ij} \vec{S}_i \cdot \vec{S}_j$$
<ul>
  <li>If $J_{ij} > 0$: Parallel spin alignment minimizes the energy $\implies$ <strong>Ferromagnetism</strong>.</li>
  <li>If $J_{ij} < 0$: Antiparallel spin alignment minimizes the energy $\implies$ <strong>Antiferromagnetism</strong>.</li>
</ul>

<h3>2. Direct Exchange & The Bethe-Slater Curve</h3>
<p>
Direct exchange occurs via the direct spatial overlap of the magnetic orbitals of adjacent atoms. The Bethe-Slater curve plots $J$ as a function of the ratio of interatomic distance $D$ to the radius of the unfilled $3d$ shell $d$:
</p>
<ul>
  <li>For $D/d < 1.5$ (e.g. Cr, Mn), wavefunctions overlap strongly, kinetic energy penalizes parallel spins, and $J < 0$ (antiferromagnetic).</li>
  <li>For $D/d > 1.5$ (e.g. Fe, Co, Ni), the overlap is modest, Coulomb exchange dominates, and $J > 0$ (ferromagnetic).</li>
</ul>
""",
            "simulation": "ssp2-exchange-interaction-sim",
            "simulations": ["ssp2-exchange-interaction-sim"]
        },
        {
            "id": "sec-3-7",
            "title": "Superexchange in Oxides & RKKY Oscillatory Coupling in Metals",
            "content": r"""
<h3>1. Anderson Superexchange in Transition Metal Oxides</h3>
<p>
In insulating transition metal oxides (such as $\text{MnO}$, $\text{NiO}$, $\text{Fe}_2\text{O}_3$), magnetic transition metal cations ($\text{Mn}^{2+}$) are separated by non-magnetic oxygen anions ($\text{O}^{2-}$). Direct overlap between $3d$ orbitals is essentially zero.
</p>
<p>
Instead, magnetic coupling is mediated by <strong>superexchange</strong>: virtual hopping of electrons through the filled intermediate oxygen $2p$ orbital.
</p>
<p>
According to the Goodenough-Kanamori-Anderson rules:
</p>
<ul>
  <li>For a $180^\circ$ cation-anion-cation bond ($\text{Mn}^{2+}-\text{O}^{2-}-\text{Mn}^{2+}$), an electron from the oxygen $2p$ orbital hops into an empty or half-filled $d$-orbital on one cation. By Hund's rule and Pauli exclusion, the remaining oxygen electron must have opposite spin and hops to the opposite cation. This mediates an overwhelmingly strong <strong>antiferromagnetic coupling</strong> ($J < 0$).</li>
  <li>For a $90^\circ$ bond angle, orthogonal oxygen $p_x$ and $p_y$ orbitals mediate a weak <strong>ferromagnetic coupling</strong> ($J > 0$).</li>
</ul>

<h3>2. The RKKY Oscillatory Interaction in Metals</h3>
<p>
In metallic alloys containing localized magnetic moments (such as rare-earth $4f$ ions in Gd, or dilute magnetic semiconductors), the direct overlap between deeply buried $4f$ shells is negligible.
</p>
<p>
Instead, coupling is mediated by the <strong>RKKY (Ruderman-Kittel-Kasuya-Yosida) interaction</strong> via the conduction electron gas. A localized spin $\vec{S}_i$ at the origin polarizes the conduction electron spins, creating a decaying, oscillatory spin density wave:
</p>
$$\delta s(r) \propto \frac{\sin(2k_F r) - 2k_F r \cos(2k_F r)}{(2k_F r)^4}$$
<p>
A second localized spin $\vec{S}_j$ at distance $R$ interacts with this spin ripple, producing an effective exchange constant:
</p>
$$J_{\text{RKKY}}(R) \propto J_{sf}^2 \frac{\cos(2k_F R)}{(2k_F R)^3}, \quad (R \gg 1/k_F)$$
<p>
The exchange constant oscillates in sign between ferromagnetic ($J > 0$) and antiferromagnetic ($J < 0$) as a function of distance $R$, leading to complex helical spin orders and spin glasses.
</p>
"""
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-3-1",
            "title": "Quantum Brillouin Paramagnetism: Exact Derivation & Limits",
            "statement": "A paramagnetic crystal contains $N$ independent atoms per unit volume, each characterized by total angular momentum quantum number $J$ and Landé $g$-factor $g_J$ in a uniform magnetic field $B$.\\n\\n(a) Evaluate the canonical partition function $Z = \\sum_{m_J = -J}^J e^{m_J x / J}$, where $x = \\frac{g_J \\mu_B J B}{k_B T}$.\\n(b) Derive the exact Brillouin function $\\mathcal{B}_J(x)$ for the magnetization $M = N g_J \\mu_B J \\mathcal{B}_J(x)$.\\n(c) Prove mathematically that in the limit $J \\to \\infty$, $\\mathcal{B}_J(x)$ reduces precisely to the classical Langevin function $L(x) = \\coth x - 1/x$, and prove that for $x \\ll 1$, it yields Curie's Law $\\chi = \\frac{C}{T}$.",
            "solution": r"""**(a) Canonical Partition Function:**
Let $\\eta \\equiv x / J = \\frac{g_J \\mu_B B}{k_B T}$. The partition function is:
$$Z = \\sum_{m_J = -J}^J e^{m_J \\eta} = e^{-J\\eta} \\sum_{n = 0}^{2J} (e^\\eta)^n$$
This is a geometric progression with first term $a = e^{-J\\eta}$, common ratio $r = e^\\eta$, and $2J+1$ terms:
$$Z = e^{-J\\eta} \\frac{1 - e^{(2J+1)\\eta}}{1 - e^\\eta} = \\frac{e^{-(J + 1/2)\\eta} - e^{(J + 1/2)\\eta}}{e^{-\\eta/2} - e^{\\eta/2}} = \\frac{\\sinh\\left( (J + 1/2)\\eta \\right)}{\\sinh(\\eta/2)}$$
Substituting $\\eta = x / J$:
$$Z(x) = \\frac{\\sinh\\left( \\frac{2J+1}{2J} x \\right)}{\\sinh\\left( \\frac{1}{2J} x \\right)}$$

**(b) Magnetization & Brillouin Function:**
The thermal average magnetization per unit volume is:
$$M = N k_B T \\frac{\\partial \\ln Z}{\\partial B} = N k_B T \\left( \\frac{\\partial x}{\\partial B} \\right) \\frac{\\partial \\ln Z}{\\partial x}$$
Since $\\frac{\\partial x}{\\partial B} = \\frac{g_J \\mu_B J}{k_B T}$:
$$M = N g_J \\mu_B J \\frac{d}{dx} \\left[ \\ln\\sinh\\left( \\frac{2J+1}{2J} x \\right) - \\ln\\sinh\\left( \\frac{1}{2J} x \\right) \\right]$$
Evaluating the derivative:
$$\\frac{d}{dx} \\ln\\sinh(a x) = a \\coth(a x)$$
$$M = N g_J \\mu_B J \\left[ \\frac{2J+1}{2J} \\coth\\left( \\frac{2J+1}{2J} x \\right) - \\frac{1}{2J} \\coth\\left( \\frac{1}{2J} x \\right) \\right] \\equiv N g_J \\mu_B J \\mathcal{B}_J(x)$$
where $\\mathcal{B}_J(x) \\equiv \\frac{2J+1}{2J} \\coth\\left( \\frac{2J+1}{2J} x \\right) - \\frac{1}{2J} \\coth\\left( \\frac{1}{2J} x \\right)$.

**(c) Asymptotic Limits:**
**1. Classical Limit ($J \\to \\infty$):**
Let $u = x / 2J \\to 0$. Then $\\frac{2J+1}{2J} x = x + u \\to x$.
$$\\lim_{J \\to \\infty} \\mathcal{B}_J(x) = \\coth x - \\lim_{u \\to 0} \\left[ \\frac{u}{x} \\coth u \\right]$$
Since $\\lim_{u \\to 0} u \\coth u = \\lim_{u \\to 0} \\frac{u}{\\tanh u} = 1$:
$$\\lim_{J \\to \\infty} \\mathcal{B}_J(x) = \\coth x - \\frac{1}{x} = L(x) \\quad \\text{(Q.E.D.)}$$

**2. Weak-Field Limit ($x \\ll 1$):**
Expand $\\coth y = \\frac{1}{y} + \\frac{y}{3} - \\frac{y^3}{45} + \\dots$ for both terms:
$$\\mathcal{B}_J(x) \\approx \\frac{2J+1}{2J} \\left[ \\frac{2J}{(2J+1)x} + \\frac{1}{3} \\frac{2J+1}{2J} x \\right] - \\frac{1}{2J} \\left[ \\frac{2J}{x} + \\frac{1}{3} \\frac{1}{2J} x \\right]$$
$$\\mathcal{B}_J(x) = \\left( \\frac{1}{x} - \\frac{1}{x} \\right) + \\frac{x}{3} \\left[ \\left(\\frac{2J+1}{2J}\\right)^2 - \\left(\\frac{1}{2J}\\right)^2 \\right] = \\frac{x}{3} \\left[ \\frac{(2J+1)^2 - 1}{4J^2} \\right] = \\frac{x}{3} \\left[ \\frac{4J^2 + 4J}{4J^2} \\right] = \\frac{J+1}{3J} x$$
Substitute into $M$:
$$M = N g_J \\mu_B J \\left( \\frac{J+1}{3J} \\frac{g_J \\mu_B J B}{k_B T} \\right) = \\frac{N g_J^2 \\mu_B^2 J(J+1)}{3 k_B T} B$$
The magnetic susceptibility is:
$$\\chi = \\frac{\\mu_0 M}{B} = \\frac{\\mu_0 N p_{\\text{eff}}^2 \\mu_B^2}{3 k_B T} = \\frac{C}{T}, \\quad \\text{where } p_{\\text{eff}} = g_J \\sqrt{J(J+1)}$$
This is exact Curie's Law."""
        },
        {
            "id": "ssp2-prob-3-2",
            "title": "Pauli Spin Paramagnetism & Landau Diamagnetism in a 3D Degenerate Fermi Gas",
            "statement": "Consider a 3D degenerate free electron gas with density $n$ and Fermi energy $E_F$ in a magnetic field $B$.\\n\\n(a) Calculate the spin-split densities of states $g_\\uparrow(E)$ and $g_\\downarrow(E)$ under Zeeman energy $\\pm \\mu_B B$, and derive the Pauli spin susceptibility $\\chi_{\\text{Pauli}}$ at $T = 0\\text{ K}$.\\n(b) Using the Sommerfeld expansion, calculate the leading finite-temperature correction to $\\chi_{\\text{Pauli}}(T)$ up to order $(T/T_F)^2$.\\n(c) The Landau orbital diamagnetic susceptibility is $\\chi_{\\text{Landau}} = -\\frac{1}{3}\\chi_{\\text{Pauli}}$. Calculate the net magnetic susceptibility $\\chi_{\\text{net}}$ of metallic sodium ($n = 2.65 \\times 10^{28}\\text{ m}^{-3}, E_F = 3.24\\text{ eV}$), and determine whether it is paramagnetically or diamagnetically dominated.",
            "solution": r"""**(a) Pauli Spin Susceptibility at $T = 0\\text{ K}$:**
The total density of states per unit volume for both spins is:
$$g(E) = \\frac{1}{2\\pi^2} \\left(\\frac{2m}{\\hbar^2}\\right)^{3/2} \\sqrt{E} = \\frac{3n}{2 E_F} \\sqrt{\\frac{E}{E_F}}$$
In field $B$, the single-spin densities are shifted by $\\pm \\mu_B B$:
$$g_\\uparrow(E) = \\frac{1}{2} g(E + \\mu_B B), \\quad g_\\downarrow(E) = \\frac{1}{2} g(E - \\mu_B B)$$
At $T = 0\\text{ K}$, all states up to chemical potential $\\mu \\approx E_F$ are filled:
$$n_\\uparrow = \\int_{-\\mu_B B}^{E_F} \\frac{1}{2} g(E + \\mu_B B) dE = \\int_0^{E_F + \\mu_B B} \\frac{1}{2} g(\\epsilon) d\\epsilon \\approx \\frac{n}{2} + \\frac{1}{2} g(E_F) \\mu_B B$$
$$n_\\downarrow = \\int_{\\mu_B B}^{E_F} \\frac{1}{2} g(E - \\mu_B B) dE = \\int_0^{E_F - \\mu_B B} \\frac{1}{2} g(\\epsilon) d\\epsilon \\approx \\frac{n}{2} - \\frac{1}{2} g(E_F) \\mu_B B$$
The magnetization is:
$$M = \\mu_B (n_\\uparrow - n_\\downarrow) = \\mu_B [g(E_F) \\mu_B B] = \\mu_B^2 g(E_F) B$$
The Pauli susceptibility is:
$$\\chi_{\\text{Pauli}} = \\frac{\\mu_0 M}{B} = \\mu_0 \\mu_B^2 g(E_F) = \\frac{3 \\mu_0 n \\mu_B^2}{2 E_F}$$

**(b) Finite-Temperature Correction via Sommerfeld Expansion:**
At finite $T$:
$$M(T) = \\mu_B \\int_0^\\infty \\frac{1}{2} g(E) [f(E - \\mu_B B) - f(E + \\mu_B B)] dE$$
For weak fields, $f(E - \\mu_B B) - f(E + \\mu_B B) \\approx -2\\mu_B B \\frac{\\partial f}{\\partial E}$:
$$M(T) = \\mu_B^2 B \\int_0^\\infty g(E) \\left(-\\frac{\\partial f}{\\partial E}\\right) dE$$
Using the Sommerfeld expansion for $\\int_0^\\infty H(E) \\left(-\\frac{\\partial f}{\\partial E}\\right) dE = H(\\mu) + \\frac{\\pi^2}{6}(k_B T)^2 H''(\\mu) + \\dots$:
With $g(E) = C E^{1/2}$, $g''(E) = -\\frac{1}{4} C E^{-3/2} = -\\frac{1}{4} \\frac{g(E)}{E^2}$:
$$\\int_0^\\infty g(E) \\left(-\\frac{\\partial f}{\\partial E}\\right) dE \\approx g(E_F) \\left[ 1 - \\frac{\\pi^2}{24} \\left( \\frac{k_B T}{E_F} \\right)^2 \\right]$$
Taking into account the temperature drift of the chemical potential $\\mu(T) = E_F [1 - \\frac{\\pi^2}{12}(k_B T / E_F)^2]$:
$$\\chi_{\\text{Pauli}}(T) = \\chi_{\\text{Pauli}}(0) \\left[ 1 - \\frac{\\pi^2}{12} \\left( \\frac{T}{T_F} \\right)^2 \\right]$$
For sodium with $T_F \\approx 37{,}600\\text{ K}$, at $300\\text{ K}$, $(T/T_F)^2 \\sim 6 \\times 10^{-5}$, so the temperature variation is less than $0.01\\%$.

**(c) Net Magnetic Susceptibility of Sodium:**
Given:
$$n = 2.65 \\times 10^{28}\\text{ m}^{-3}, \\quad E_F = 3.24\\text{ eV} = 5.191 \\times 10^{-19}\\text{ J}$$
$$\\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}, \\quad \\mu_B = 9.274 \\times 10^{-24}\\text{ J/T}$$
Compute $\\chi_{\\text{Pauli}}$:
$$\\chi_{\\text{Pauli}} = \\frac{3 (4\\pi \\times 10^{-7})(2.65 \\times 10^{28})(9.274 \\times 10^{-24})^2}{2 \\times 5.191 \\times 10^{-19}} = \\frac{3 \\times 1.2566 \\times 10^{-6} \\times 2.65 \\times 10^{28} \\times 8.601 \\times 10^{-47}}{1.0382 \\times 10^{-18}}$$
$$\\chi_{\\text{Pauli}} = \\frac{8.592 \\times 10^{-24}}{1.0382 \\times 10^{-18}} \\approx 8.28 \\times 10^{-6}$$
Landau diamagnetism:
$$\\chi_{\\text{Landau}} = -\\frac{1}{3} \\chi_{\\text{Pauli}} = -2.76 \\times 10^{-6}$$
Core ion diamagnetism of $\\text{Na}^+$:
$$\\chi_{\\text{core}} \\approx -0.42 \\times 10^{-6}$$
Net total susceptibility:
$$\\chi_{\\text{net}} = \\chi_{\\text{Pauli}} + \\chi_{\\text{Landau}} + \\chi_{\\text{core}} = (8.28 - 2.76 - 0.42) \\times 10^{-6} = +5.10 \\times 10^{-6}$$
Because $\\chi_{\\text{net}} > 0$, metallic sodium is **paramagnetically dominated**."""
        },
        {
            "id": "ssp2-prob-3-3",
            "title": "Quantum Exchange Singlet-Triplet Splitting in a Two-Electron Model",
            "statement": "Two electrons occupy two orthogonal spatial orbitals $\\phi_a(\\vec{r})$ and $\\phi_b(\\vec{r})$ under a Hamiltonian $\\hat{H} = \\hat{h}_1 + \\hat{h}_2 + \\frac{e^2}{4\\pi\\epsilon_0 r_{12}}$.\\n\\n(a) Write down the spatial wavefunctions $\\psi_S(\\vec{r}_1, \\vec{r}_2)$ and $\\psi_T(\\vec{r}_1, \\vec{r}_2)$ for the spin singlet ($S = 0$) and spin triplet ($S = 1$) states.\\n(b) Calculate the expectation energies $E_S$ and $E_T$ in terms of the single-particle energy $E_0 = \\epsilon_a + \\epsilon_b$, the direct Coulomb integral $K$, and the exchange integral $J_{\\text{ex}}$.\\n(c) Express the effective Hamiltonian in terms of the spin operators $\\vec{S}_1$ and $\\vec{S}_2$, and explain why a positive exchange integral $J_{\\text{ex}} > 0$ energetically favors ferromagnetic alignment.",
            "solution": r"""**(a) Singlet and Triplet Spatial Wavefunctions:**
By the generalized Pauli principle, the total electronic state must be antisymmetric:
$$\\Psi(1, 2) = \\psi_{\\text{spatial}}(\\vec{r}_1, \\vec{r}_2) \\chi_{\\text{spin}}(1, 2) = -\\Psi(2, 1)$$
- For the Singlet ($S = 0$), the spin state is the antisymmetric singlet:
$$\\chi_0^0 = \\frac{1}{\\sqrt{2}} (|\\uparrow\\downarrow\\rangle - |\\downarrow\\uparrow\\rangle)$$
Hence the spatial wavefunction must be symmetric:
$$\\psi_S(\\vec{r}_1, \\vec{r}_2) = \\frac{1}{\\sqrt{2}} [\\phi_a(\\vec{r}_1)\\phi_b(\\vec{r}_2) + \\phi_b(\\vec{r}_1)\\phi_a(\\vec{r}_2)]$$
- For the Triplet ($S = 1$), the spin states are symmetric ($|\\uparrow\\uparrow\\rangle, \\frac{1}{\\sqrt{2}}(|\\uparrow\\downarrow\\rangle + |\\downarrow\\uparrow\\rangle), |\\downarrow\\downarrow\\rangle$). Hence the spatial wavefunction must be antisymmetric:
$$\\psi_T(\\vec{r}_1, \\vec{r}_2) = \\frac{1}{\\sqrt{2}} [\\phi_a(\\vec{r}_1)\\phi_b(\\vec{r}_2) - \\phi_b(\\vec{r}_1)\\phi_a(\\vec{r}_2)]$$

**(b) Singlet and Triplet Energies:**
Define the direct Coulomb integral $K$ and exchange integral $J_{\\text{ex}}$:
$$K = \\iint |\\phi_a(\\vec{r}_1)|^2 \\frac{e^2}{4\\pi\\epsilon_0 r_{12}} |\\phi_b(\\vec{r}_2)|^2 d^3r_1 d^3r_2$$
$$J_{\\text{ex}} = \\iint \\phi_a^*(\\vec{r}_1)\\phi_b^*(\\vec{r}_2) \\frac{e^2}{4\\pi\\epsilon_0 r_{12}} \\phi_b(\\vec{r}_1)\\phi_a(\\vec{r}_2) d^3r_1 d^3r_2$$
Computing the expectation values:
$$E_S = \\langle \\psi_S | \\hat{H} | \\psi_S \\rangle = \\epsilon_a + \\epsilon_b + K + J_{\\text{ex}}$$
$$E_T = \\langle \\psi_T | \\hat{H} | \\psi_T \\rangle = \\epsilon_a + \\epsilon_b + K - J_{\\text{ex}}$$
The energy splitting is:
$$\\Delta E = E_S - E_T = 2 J_{\\text{ex}}$$

**(c) Effective Spin Hamiltonian:**
Notice that:
$$\\vec{S}_1 \\cdot \\vec{S}_2 = \\frac{1}{2} [(\\vec{S}_1 + \\vec{S}_2)^2 - \\vec{S}_1^2 - \\vec{S}_2^2] = \\frac{1}{2} [S(S+1) - 3/4 - 3/4]$$
For $S = 0$: $\\vec{S}_1 \\cdot \\vec{S}_2 = -3/4$.
For $S = 1$: $\\vec{S}_1 \\cdot \\vec{S}_2 = +1/4$.
Constructing the operator $\\hat{H}_{\\text{spin}} = C_0 - 2 J_{\\text{ex}} \\vec{S}_1 \\cdot \\vec{S}_2$:
- For $S = 0$: $E = C_0 - 2 J_{\\text{ex}}(-3/4) = C_0 + \\frac{3}{2}J_{\\text{ex}}$
- For $S = 1$: $E = C_0 - 2 J_{\\text{ex}}(1/4) = C_0 - \\frac{1}{2}J_{\\text{ex}}$
Setting $C_0 = \\epsilon_a + \\epsilon_b + K - \\frac{1}{2}J_{\\text{ex}}$, the difference is:
$$E_S - E_T = 2 J_{\\text{ex}}$$
Matching the Heisenberg Hamiltonian:
$$\\hat{H}_{\\text{eff}} = -2 J_{\\text{ex}} \\vec{S}_1 \\cdot \\vec{S}_2 + \\text{const}$$
Physical origin:
When $J_{\\text{ex}} > 0$, $E_T < E_S$. The triplet state has lower energy because its spatial wavefunction $\\psi_T$ vanishes whenever $\\vec{r}_1 = \\vec{r}_2$. This exchange hole keeps electrons separated in real space, minimizing repulsive Coulomb energy $\\frac{e^2}{4\\pi\\epsilon_0 r_{12}}$. Thus, parallel spins ($S = 1$) minimize electrostatic energy, producing ferromagnetism."""
        }
    ]
}

# =========================================================================
# UNIT 4: Ordered Magnetism: Ferromagnetism, Antiferromagnetism, Domains & Resonance
# =========================================================================

u4_data = {
    "title": "Ordered Magnetism: Ferromagnetism, Antiferromagnetism, Domains & Resonance",
    "subtitle": "Weiss Field, Néel Sublattices, Domain Walls, Hysteresis & Multiferroics",
    "summary": "This unit provides a complete theoretical exposition of cooperative magnetic phenomena in condensed matter. We analyze Weiss molecular field theory, self-consistent spontaneous magnetization, critical exponents, and the Curie-Weiss law. We develop the Néel two-sublattice model of antiferromagnetism, calculate parallel and perpendicular susceptibilities, and explain ferrimagnetic spinel structures. We formulate the micromagnetic energy minimization governing domain formation, derive the exact spatial profile and width of 180° Bloch domain walls, model the B-H hysteresis loop, and examine ferromagnetic resonance (FMR) via the Kittel equation alongside modern multiferroic magnetoelectric coupling.",
    "sections": [
        {
            "id": "sec-4-1",
            "title": "Weiss Molecular Field Theory of Ferromagnetism & Spontaneous Magnetization",
            "content": r"""
<h3>1. The Weiss Molecular Field Hypothesis</h3>
<p>
In 1907, Pierre Weiss proposed that ferromagnetism arises from an immense internal effective magnetic field $\vec{B}_m$, called the <strong>molecular field</strong>, proportional to the macroscopic magnetization $\vec{M}$:
</p>
$$\vec{B}_{\text{eff}} = \vec{B}_{\text{ext}} + \vec{B}_m = \vec{B}_{\text{ext}} + \lambda \vec{M}$$
<p>
where $\lambda$ is the dimensionless Weiss molecular field parameter.
</p>
<p>
From quantum Heisenberg exchange $\hat{\mathcal{H}} = -2\sum_j J_{ij} \vec{S}_i \cdot \vec{S}_j$, in the mean-field approximation we replace neighboring spins by their thermal average $\langle \vec{S}_j \rangle = \frac{\vec{M}}{N g\mu_B}$. The effective magnetic field is:
</p>
$$\vec{B}_m = \frac{2 z J}{N g^2 \mu_B^2} \vec{M} \implies \lambda = \frac{2 z J}{N g^2 \mu_B^2}$$
<p>
where $z$ is the coordination number of nearest neighbors. For iron ($T_C = 1043\text{ K}$), $\lambda \sim 10^3$, yielding an astronomical internal field $B_m = \lambda \mu_0 M_s \sim 1000\text{ Tesla}$!
</p>

<h3>2. Graphical Solution for Spontaneous Magnetization</h3>
<p>
In zero applied field ($\vec{B}_{\text{ext}} = 0$), the internal field is simply $B = \lambda M$. Substituting this into the quantum Brillouin equation:
</p>
$$\frac{M(T)}{M_0} = \mathcal{B}_J(x), \quad x = \frac{g\mu_B J (\lambda M)}{k_B T}$$
<p>
where $M_0 = N g \mu_B J$ is the absolute saturation magnetization at $T = 0\text{ K}$.
</p>
<p>
Expressing $M/M_0$ as a linear function of $x$:
</p>
$$\frac{M}{M_0} = \left( \frac{k_B T}{N g^2 \mu_B^2 J^2 \lambda} \right) x = \frac{T}{3 T_C} \left( \frac{J+1}{J} \right)^{-1} x$$
<p>
The intersection between the curved Brillouin function $\mathcal{B}_J(x)$ and the straight line determines the self-consistent magnetization:
</p>
<ul>
  <li>For $T \ge T_C$, the only intersection is at $x = 0$ ($M = 0$, paramagnetic state).</li>
  <li>For $T < T_C$, the straight line has a shallower initial slope than the Brillouin function ($\frac{d\mathcal{B}_J}{dx}|_0 = \frac{J+1}{3J}$). A non-trivial intersection exists at $x_0 > 0$, yielding a stable <strong>spontaneous magnetization</strong> $M_s(T) > 0$ without any applied external field!</li>
  <li>The transition temperature is the <strong>Curie temperature</strong> $T_C$:
  $$T_C = \frac{N g^2 \mu_B^2 J(J+1) \lambda}{3 k_B} = \frac{C \lambda}{\mu_0}$$</li>
</ul>
"""
        },
        {
            "id": "sec-4-2",
            "title": "The Curie-Weiss Law, Critical Exponents & Phase Transitions",
            "content": r"""
<h3>1. Derivation of the Curie-Weiss Law</h3>
<p>
In the paramagnetic temperature regime above the Curie point ($T > T_C$), an applied external field $B_{\text{ext}}$ induces a small magnetization, so $x \ll 1$. Expanding the Brillouin function:
</p>
$$M = N g \mu_B J \mathcal{B}_J(x) \approx N g \mu_B J \left( \frac{J+1}{3J} \right) x = \frac{N g^2 \mu_B^2 J(J+1)}{3 k_B T} (B_{\text{ext}} + \lambda M)$$
<p>
Using $C = \frac{\mu_0 N g^2 \mu_B^2 J(J+1)}{3 k_B}$:
</p>
$$\mu_0 M = \frac{C}{T} (B_{\text{ext}} + \lambda M) \implies \mu_0 M \left( 1 - \frac{\lambda C}{\mu_0 T} \right) = \frac{C B_{\text{ext}}}{T}$$
<p>
Recognizing $T_C = \frac{\lambda C}{\mu_0}$:
</p>
$$\chi = \frac{\mu_0 M}{B_{\text{ext}}} = \frac{C}{T - T_C}$$
<p>
This is the celebrated <strong>Curie-Weiss Law</strong>. As $T \to T_C^+$, the magnetic susceptibility diverges towards infinity ($\chi \to \infty$), signaling an instability toward spontaneous ferromagnetic symmetry breaking.
</p>

<h3>2. Critical Exponents Near the Second-Order Phase Transition</h3>
<p>
In the terminology of modern phase transitions, the paramagnetic-to-ferromagnetic transition is a continuous second-order phase transition characterized by universal critical exponents:
</p>
<ul>
  <li><strong>Spontaneous Magnetization:</strong> $M_s(T) \propto (T_C - T)^\beta$ as $T \to T_C^-$.
  Mean-field theory predicts $\beta_{\text{MF}} = 1/2$, while the 3D Heisenberg model gives $\beta \approx 0.365$.</li>
  <li><strong>Magnetic Susceptibility:</strong> $\chi(T) \propto (T - T_C)^{-\gamma}$ as $T \to T_C^+$.
  Mean-field theory predicts $\gamma_{\text{MF}} = 1$, while 3D Heisenberg gives $\gamma \approx 1.386$.</li>
  <li><strong>Specific Heat:</strong> $C_V(T) \propto |T - T_C|^{-\alpha}$.
  Mean-field theory predicts a finite jump $\Delta C = \frac{5}{2} N k_B \frac{J(J+1)}{J^2 + (J+1)^2}$ at $T_C$ ($\alpha = 0$).</li>
</ul>
"""
        },
        {
            "id": "sec-4-3",
            "title": "Néel Two-Sublattice Theory of Antiferromagnetism & Susceptibility $\chi(T)$",
            "content": r"""
<h3>1. Sublattice Magnetization & Néel Temperature</h3>
<p>
In an antiferromagnet (such as $\text{MnO}$, $\text{FeF}_2$, $\text{Cr}$), negative exchange coupling ($J < 0$) favors antiparallel alignment of neighboring spins. Louis Néel (1932) modeled the crystal as two interpenetrating sublattices, $A$ and $B$:
</p>
$$\vec{M} = \vec{M}_A + \vec{M}_B$$
<p>
The effective molecular fields acting on sublattices $A$ and $B$ are:
</p>
$$\vec{B}_A = \vec{B}_{\text{ext}} - \lambda \vec{M}_B - \lambda' \vec{M}_A$$
$$\vec{B}_B = \vec{B}_{\text{ext}} - \lambda \vec{M}_A - \lambda' \vec{M}_B$$
<p>
where $-\lambda$ represents the strong inter-sublattice antiferromagnetic molecular field coefficient ($\lambda > 0$), and $\lambda'$ represents intra-sublattice interactions.
</p>
<p>
In zero applied field, below the <strong>Néel temperature</strong> $T_N$:
</p>
$$\vec{M}_A = -\vec{M}_B = \vec{M}_s(T) \implies \vec{M}_{\text{net}} = \vec{M}_A + \vec{M}_B = 0$$
<p>
The transition occurs at:
</p>
$$T_N = \frac{C' (\lambda - \lambda')}{2}$$
<p>
where $C'$ is the Curie constant of a single sublattice. Above $T_N$, the susceptibility follows the modified Curie-Weiss law:
</p>
$$\chi = \frac{C}{T + \theta}, \quad \theta = \frac{C (\lambda + \lambda')}{2} > 0$$

<h3>2. Anisotropic Susceptibility Below $T_N$ & The Spin-Flop Transition</h3>
<ul>
  <li><strong>Perpendicular Susceptibility ($\vec{B} \perp \text{easy axis}$):</strong> The external field cants both sublattices slightly toward the field by angle $\phi \approx B / (2\lambda M_s)$. The resulting transverse magnetization is independent of temperature:
  $$\chi_\perp(T) = \frac{\mu_0 M}{B} = \frac{1}{\lambda} = \text{constant} \quad (\text{for all } T \le T_N)$$</li>
  <li><strong>Parallel Susceptibility ($\vec{B} \parallel \text{easy axis}$):</strong> The external field cannot cant the collinear spins without overcoming the full exchange field. As $T \to 0\text{ K}$, all thermal fluctuations freeze out, making it impossible to flip antiparallel spins against the exchange gap:
  $$\chi_\parallel(T) \to 0 \quad \text{as } T \to 0\text{ K}$$</li>
  <li><strong>Spin-Flop Transition:</strong> If a strong magnetic field is applied parallel to the easy axis exceeding the critical spin-flop field $B_{\text{sf}} = \sqrt{2 B_{\text{ex}} B_{\text{aniso}}}$, the spins abruptly rotate by $90^\circ$ perpendicular to $\vec{B}$ to gain canting susceptibility energy ($\frac{1}{2}\chi_\perp B^2 > \frac{1}{2}\chi_\parallel B^2$).</li>
</ul>
"""
        },
        {
            "id": "sec-4-4",
            "title": "Ferrimagnetism, Spinel Ferrites & Applications of High-Resistivity Magnets",
            "content": r"""
<h3>1. Sublattice Imbalance & Ferrimagnetism</h3>
<p>
In a <strong>ferrimagnet</strong>, negative exchange coupling aligns sublattices antiparallel, but the sublattices contain unequal magnetic moments:
</p>
$$|\vec{M}_A| \ne |\vec{M}_B| \implies \vec{M}_{\text{net}} = \vec{M}_A + \vec{M}_B \ne 0$$
<p>
This results in a spontaneous net macroscopic magnetization below the Curie/Néel temperature, combining the macroscopic magnetic strength of a ferromagnet with the microscopic antiferromagnetic exchange topology.
</p>

<h3>2. Crystal Structure of Spinel Ferrites</h3>
<p>
The prototypical ferrimagnets are the <strong>spinel ferrites</strong>, having the chemical formula $\text{MO}\cdot\text{Fe}_2\text{O}_3$ or $\text{MFe}_2\text{O}_4$, where $\text{M}$ is a divalent cation ($\text{Fe}^{2+}, \text{Ni}^{2+}, \text{Co}^{2+}, \text{Mn}^{2+}, \text{Mg}^{2+}, \text{Zn}^{2+}$).
</p>
<p>
The oxygen anions form a face-centered cubic (FCC) close-packed lattice containing two distinct interstitial crystallographic sites:
</p>
<ul>
  <li><strong>Tetrahedral $A$-sites:</strong> Surrounded by 4 oxygen ions (1/8 occupied).</li>
  <li><strong>Octahedral $B$-sites:</strong> Surrounded by 6 oxygen ions (1/2 occupied). There are twice as many occupied $B$-sites as $A$-sites.</li>
</ul>
<p>
In magnetite ($\text{Fe}_3\text{O}_4 = \text{Fe}^{3+}[\text{Fe}^{2+}\text{Fe}^{3+}]\text{O}_4$, an <em>inverse spinel</em>):
</p>
<ul>
  <li>$A$-sites are occupied by $\text{Fe}^{3+}$ ($3d^5$, $5\mu_B$).</li>
  <li>$B$-sites are occupied by equal numbers of $\text{Fe}^{3+}$ ($5\mu_B$) and $\text{Fe}^{2+}$ ($3d^6$, $4\mu_B$).</li>
  <li>Antiferromagnetic $A$-$B$ superexchange couples all $A$-spins antiparallel to all $B$-spins:
  $$\mu_{\text{net}} = \mu_B(\text{site}) - \mu_A(\text{site}) = (5\mu_B + 4\mu_B) - 5\mu_B = 4\mu_B \text{ per formula unit}$$
  The two sublattices of $\text{Fe}^{3+}$ exactly cancel, leaving a net magnetic moment solely due to the $\text{Fe}^{2+}$ ions ($4\mu_B$).</li>
</ul>
<p>
<strong>Technological Importance:</strong> Unlike metallic ferromagnets (Fe, Co, Ni), ferrites are electrical insulators with electrical resistivities $\rho \sim 10^2 - 10^9\ \Omega\cdot\text{cm}$ (up to $10^{14}$ times higher than metals). This completely suppresses high-frequency eddy current dissipation, making ferrites indispensable for microwave circulators, radar isolators, RF transformer cores, and switch-mode power supplies.
</p>
"""
        },
        {
            "id": "sec-4-5",
            "title": "Energetics of Magnetic Domains: Free Energy Minimization & Hysteresis Loops",
            "content": r"""
<h3>1. Thermodynamic Origin of Magnetic Domains</h3>
<p>
A macroscopic ferromagnetic specimen below $T_C$ does not normally exhibit a net external magnetic field unless magnetized. Pierre Weiss recognized that the crystal subdivides into small regions called <strong>magnetic domains</strong>, inside each of which the spins are fully aligned to the spontaneous magnetization $M_s$, but the orientation of $\vec{M}$ varies among domains to minimize the total free energy:
</p>
$$F_{\text{total}} = E_{\text{exchange}} + E_{\text{magnetostatic}} + E_{\text{anisotropy}} + E_{\text{magnetostrictive}}$$
<ol>
  <li><strong>Magnetostatic Energy ($E_{\text{ms}} = \frac{1}{2}\mu_0 \int H_d^2 dV$):</strong> A single uniformly magnetized domain creates a large demagnetizing field $\vec{H}_d$ with substantial stray field energy. Subdividing into multiple opposing antiparallel domains reduces $E_{\text{ms}}$ by a factor of $N$. Creating closure domains eliminates $E_{\text{ms}}$ entirely.</li>
  <li><strong>Exchange Energy ($E_{\text{ex}} = -2J \sum \vec{S}_i \cdot \vec{S}_j$):</strong> Favors parallel spin alignment; penalizes the creation of domain walls.</li>
  <li><strong>Magnetocrystalline Anisotropy ($E_{\text{an}} = K_1 (\alpha_1^2 \alpha_2^2 + \dots)$):</strong> Favors magnetization along specific crystallographic "easy" directions (e.g. $\langle 100 \rangle$ in Fe, $\langle 111 \rangle$ in Ni, $[0001]$ in Co).</li>
  <li><strong>Magnetostrictive Energy ($E_{\text{ms}}$):</strong> Elastic strain energy caused by mechanical deformation during spontaneous alignment along easy axes.</li>
</ol>

<h3>2. The Magnetic Hysteresis Loop</h3>
<p>
When an unmagnetized sample is subjected to an external cycling field $H$:
</p>
<ul>
  <li><strong>Domain Wall Displacement:</strong> At low fields, domains favorably oriented with $\vec{H}$ expand at the expense of unfavorable domains via domain wall motion. Inclusions, voids, and dislocations pin domain walls, causing discontinuous irreversible jumps known as <strong>Barkhausen jumps</strong>.</li>
  <li><strong>Domain Rotation:</strong> At high fields, domain walls are fully eliminated, and the magnetization vectors rotate coherently away from easy crystal axes into alignment with $\vec{H}$, reaching the <strong>saturation magnetization</strong> $M_s$.</li>
  <li><strong>Remanence $M_r$:</strong> When $H$ returns to zero, domain wall pinning prevents complete recovery, leaving remanent magnetization $M_r$.</li>
  <li><strong>Coercivity $H_c$:</strong> The reverse magnetic field required to reduce the net magnetization back to zero.
  <ul>
    <li><em>Soft Magnets</em> ($H_c < 100\text{ A/m}$, narrow loop): Low hysteresis loss $\oint B dH$, ideal for transformer cores (e.g. Supermalloy, Si-Fe).</li>
    <li><em>Hard Magnets</em> ($H_c > 10^4\text{ A/m}$, broad loop): Immense energy product $(BH)_{\max}$, permanent magnets (e.g. $\text{Nd}_2\text{Fe}_{14}\text{B}$, $\text{SmCo}_5$).</li>
  </ul>
  </li>
</ul>
""",
            "simulation": "ssp2-weiss-hysteresis-sim",
            "simulations": ["ssp2-weiss-hysteresis-sim"]
        },
        {
            "id": "sec-4-6",
            "title": "Structure and Width of Bloch & Néel Domain Walls",
            "content": r"""
<h3>1. The Structure of a 180° Bloch Domain Wall</h3>
<p>
The boundary separating two adjacent ferromagnetic domains with opposing magnetizations is a <strong>domain wall</strong>. The transition does not happen abruptly across a single atomic plane, because misaligning neighboring spins by $180^\circ$ would cost huge exchange energy:
</p>
$$\Delta E_{\text{ex}} = -2J S^2 (\cos\pi - 1) = 4 J S^2$$
<p>
Instead, the spin direction rotates gradually over a transition layer of $N$ atomic planes. For a rotation of $\Delta\theta = \pi / N$ between adjacent planes:
</p>
$$\Delta E_{\text{ex}} \approx -2J S^2 \left(1 - \frac{(\pi/N)^2}{2} - 1\right) = J S^2 \left(\frac{\pi}{N}\right)^2$$
<p>
The total exchange energy per unit area across $N$ planes (with $1/a^2$ atoms per unit area) is:
</p>
$$\sigma_{\text{ex}} = N \left( \frac{J S^2 \pi^2}{N^2 a^2} \right) = \frac{\pi^2 J S^2}{N a^2} = \frac{\pi^2 A}{N a} \propto \frac{1}{\delta_w}$$
<p>
where $A = J S^2 / a$ is the exchange stiffness constant and $\delta_w = N a$ is the wall thickness.
</p>

<h3>2. Equilibrium Wall Width & Energy</h3>
<p>
However, as the wall widens, spins point away from the crystallographic easy axis, increasing the magnetocrystalline anisotropy energy:
</p>
$$\sigma_{\text{aniso}} \approx K_1 \delta_w = K_1 N a$$
<p>
The total surface energy per unit area of the wall is:
</p>
$$\sigma_w = \sigma_{\text{ex}} + \sigma_{\text{aniso}} = \frac{\pi^2 A}{\delta_w} + K_1 \delta_w$$
<p>
Minimizing with respect to $\delta_w$:
</p>
$$\frac{d\sigma_w}{d\delta_w} = -\frac{\pi^2 A}{\delta_w^2} + K_1 = 0 \implies \delta_w = \pi \sqrt{\frac{A}{K_1}}$$
<p>
The minimum areal energy of the 180° Bloch wall is:
</p>
$$\sigma_w = 2\pi \sqrt{A K_1}$$
<p>
For iron ($A \approx 2 \times 10^{-11}\text{ J/m}, K_1 \approx 4.8 \times 10^4\text{ J/m}^3$):
</p>
$$\delta_w = \pi \sqrt{\frac{2 \times 10^{-11}}{4.8 \times 10^4}} \approx 6.4 \times 10^{-8}\text{ m} = 64\text{ nm} \sim 220 \text{ lattice constants}$$
<p>
In thin films where specimen thickness is smaller than $\delta_w$, magnetostatic surface charges penalize out-of-plane rotation, favoring <strong>Néel domain walls</strong> where the magnetization rotates strictly within the film plane.
</p>
"""
        },
        {
            "id": "sec-4-7",
            "title": "Ferromagnetic Resonance (Kittel Equations), Electron Spin Resonance & Multiferroic Materials",
            "content": r"""
<h3>1. Ferromagnetic Resonance (FMR) & Kittel Equations</h3>
<p>
In ferromagnetic resonance, a uniform precessional mode of the macroscopic magnetization vector $\vec{M}$ about an effective magnetic field is excited by a transverse microwave field. The equation of motion is:
</p>
$$\frac{d\vec{M}}{dt} = -\gamma (\vec{M} \times \vec{B}_{\text{eff}})$$
<p>
where $\gamma = g e / 2m$ is the gyromagnetic ratio.
</p>
<p>
Because the specimen has finite dimensions, transverse precession generates oscillating demagnetizing fields governed by demagnetizing factors $N_x, N_y, N_z$ ($N_x + N_y + N_z = 1$):
</p>
$$\vec{B}_{\text{eff}} = (B_0 - \mu_0 N_z M_s) \hat{z} - \mu_0 N_x m_x \hat{x} - \mu_0 N_y m_y \hat{y}$$
<p>
Solving the linearized precessional equations yields the <strong>Kittel resonance frequency</strong>:
</p>
$$\omega_{\text{FMR}} = \gamma \sqrt{ [B_0 + \mu_0(N_x - N_z) M_s] [B_0 + \mu_0(N_y - N_z) M_s] }$$
<ul>
  <li><strong>Sphere ($N_x = N_y = N_z = 1/3$):</strong> $\omega = \gamma B_0$ (Identical to free-electron Larmor precession!).</li>
  <li><strong>Flat Plate with in-plane field ($N_x = 1, N_y = N_z = 0$):</strong>
  $$\omega = \gamma \sqrt{B_0 (B_0 + \mu_0 M_s)}$$</li>
</ul>

<h3>2. Multiferroic Materials & Magnetoelectric Coupling</h3>
<p>
<strong>Multiferroics</strong> are rare single-phase or composite materials that simultaneously exhibit two or more primary ferroic orders:
</p>
<ul>
  <li><strong>Ferromagnetism:</strong> Spontaneous magnetic polarization $\vec{M}$ breaking time-reversal symmetry $\mathcal{T}$.</li>
  <li><strong>Ferroelectricity:</strong> Spontaneous electric polarization $\vec{P}$ breaking spatial inversion symmetry $\mathcal{P}$.</li>
  <li><strong>Ferroelasticity:</strong> Spontaneous mechanical strain $\epsilon_{ij}$.</li>
</ul>
<p>
The mutual interaction between electric and magnetic orders is quantified by the <strong>magnetoelectric free energy</strong>:
</p>
$$F_{\text{ME}} = -\alpha_{ij} \mathcal{E}_i H_j - \frac{1}{2}\beta_{ijk} \mathcal{E}_i H_j H_k - \frac{1}{2}\gamma_{ijk} \mathcal{E}_i \mathcal{E}_j H_k$$
<p>
where $\alpha_{ij}$ is the linear magnetoelectric coupling tensor. This allows an electric field $\vec{\mathcal{E}}$ to manipulate magnetic bits, and magnetic fields to switch electric polarization—enabling ultra-low-power non-volatile magnetoelectric RAM (MeRAM) with zero Joule heating from write currents! Prototypical single-phase multiferroics include bismuth ferrite ($\text{BiFeO}_3$, $T_N \approx 643\text{ K}, T_C \approx 1100\text{ K}$) and $\text{TbMnO}_3$.
</p>
""",
            "simulation": "ssp2-antiferro-resonance-sim",
            "simulations": ["ssp2-antiferro-resonance-sim"]
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-4-1",
            "title": "Weiss Mean-Field Theory: Spontaneous Magnetization & Specific Heat Jump",
            "statement": "A ferromagnetic solid with $N$ spins of $S = 1/2$ per unit volume ($g = 2$) is described by Weiss molecular field theory with molecular parameter $\\lambda$.\\n\\n(a) Write down the transcendental equation for spontaneous magnetization $m = M_s(T) / M_0$ in zero applied field, and find the Curie temperature $T_C$.\\n(b) By expanding the transcendental equation for temperatures slightly below $T_C$ ($T \\to T_C^-$), prove that $m(T) \\approx \\sqrt{3} \\left(1 - \\frac{T}{T_C}\\right)^{1/2}$, confirming the mean-field critical exponent $\\beta = 1/2$.\\n(c) Calculate the internal magnetic energy $E(T) = -\\frac{1}{2}\\mu_0 \\lambda M_s^2(T)$ and evaluate the discontinuous jump in magnetic specific heat $\\Delta C = C(T_C^-) - C(T_C^+)$ per mole.",
            "solution": r"""**(a) Transcendental Equation & Curie Temperature:**
For $S = 1/2$, the Brillouin function simplifies to:
$$\\mathcal{B}_{1/2}(x) = \\frac{2(1/2)+1}{2(1/2)} \\coth(x) - \\frac{1}{2(1/2)} \\coth(x) = 2\\coth(2x) - \\coth(x) = \\tanh(x)$$
With $B_{\\text{ext}} = 0$, $x = \\frac{g\\mu_B (1/2) \\lambda M_s}{k_B T} = \\frac{\\mu_B \\lambda M_s}{k_B T}$.
Defining reduced magnetization $m = M_s / M_0$, where $M_0 = N \\mu_B$:
$$x = \\frac{\\mu_B \\lambda (N \\mu_B m)}{k_B T} = \\left( \\frac{N \\mu_B^2 \\lambda}{k_B T} \\right) m$$
The transcendental equation is:
$$m = \\tanh\\left( \\frac{T_C}{T} m \\right), \\quad \\text{where } T_C = \\frac{N \\mu_B^2 \\lambda}{k_B}$$

**(b) Behavior Just Below $T_C$ ($T \\to T_C^-$):**
For $T \\lesssim T_C$, $m \\ll 1$. Let $t \\equiv T / T_C \\approx 1$.
Expand $\\tanh(u) \\approx u - \\frac{u^3}{3} + \\dots$ with $u = m / t$:
$$m = \\frac{m}{t} - \\frac{1}{3} \\left(\\frac{m}{t}\\right)^3$$
Divide by $m \\ne 0$:
$$1 = \\frac{1}{t} - \\frac{m^2}{3 t^3} \\implies \\frac{m^2}{3 t^3} = \\frac{1 - t}{t}$$
$$m^2 = 3 t^2 (1 - t) \\approx 3 (1 - t) = 3 \\left(1 - \\frac{T}{T_C}\\right)$$
Taking the square root:
$$m(T) = \\sqrt{3} \\left( 1 - \\frac{T}{T_C} \\right)^{1/2}$$
This proves that $m \\propto (T_C - T)^\\beta$ with the universal mean-field exponent **$\\beta = 1/2$**.

**(c) Discontinuous Jump in Specific Heat:**
The internal magnetic energy per unit volume is:
$$E(T) = -\\frac{1}{2} \\mu_0 \\lambda M_s^2(T) = -\\frac{1}{2} \\mu_0 \\lambda M_0^2 m^2(T)$$
For $T > T_C$, $m = 0 \\implies E(T) = 0 \\implies C(T_C^+) = 0$.
For $T < T_C$, substituting $m^2(T) \\approx 3(1 - T/T_C)$:
$$E(T) = -\\frac{3}{2} \\mu_0 \\lambda M_0^2 \\left( 1 - \\frac{T}{T_C} \\right)$$
The magnetic specific heat capacity is:
$$C(T) = \\frac{\\partial E}{\\partial T} = \\frac{3}{2} \\frac{\\mu_0 \\lambda M_0^2}{T_C}$$
Since $T_C = \\frac{\\mu_0 \\lambda M_0^2}{N k_B}$:
$$C(T_C^-) = \\frac{3}{2} N k_B$$
The jump in specific heat per mole ($N = N_A$, $N_A k_B = R$) is:
$$\\Delta C = C(T_C^-) - C(T_C^+) = \\frac{3}{2} R \\approx 1.5 \\times 8.314\\text{ J/(mol}\\cdot\\text{K)} \\approx 12.47\\text{ J/(mol}\\cdot\\text{K)}$$
This finite discontinuity proves that the ferromagnetic Curie transition in mean-field theory is a **second-order phase transition**."""
        },
        {
            "id": "ssp2-prob-4-2",
            "title": "Néel Antiferromagnetic Susceptibility & Spin-Flop Field Derivation",
            "statement": "An antiferromagnet has two identical sublattices $A$ and $B$ with exchange molecular field parameter $\\lambda > 0$ and uniaxial anisotropy energy density $E_K = K (\\sin^2\\theta_A + \\sin^2\\theta_B)$.\\n\\n(a) Show that the perpendicular susceptibility below $T_N$ is strictly constant $\\chi_\\perp = 1/\\lambda$, independent of temperature.\\n(b) Show that the parallel susceptibility $\\chi_\\parallel(T) \\to 0$ as $T \\to 0\\text{ K}$, and derive its expression near $T_N$.\\n(c) A magnetic field $B$ is applied along the easy axis. Calculate the critical spin-flop field $B_{\\text{sf}}$ at which the collinear state abruptly rotates into the canted perpendicular state.",
            "solution": r"""**(a) Perpendicular Susceptibility $\\chi_\\perp$:**
Apply an external field $\\vec{B} \\perp$ easy axis. The field exerts a torque that cants both sublattices toward $\\vec{B}$ by a small angle $\\phi$.
The magnetic energy per unit volume is:
$$E = \\lambda \\vec{M}_A \\cdot \\vec{M}_B - (\\vec{M}_A + \\vec{M}_B) \\cdot \\vec{B}$$
With $|M_A| = |M_B| = M_s$, the angle between $\\vec{M}_A$ and $\\vec{M}_B$ is $\\pi - 2\\phi$:
$$\\vec{M}_A \\cdot \\vec{M}_B = M_s^2 \\cos(\\pi - 2\\phi) = -M_s^2 \\cos(2\\phi) \\approx -M_s^2 (1 - 2\\phi^2)$$
$$(\\vec{M}_A + \\vec{M}_B) \\cdot \\vec{B} = 2 M_s B \\sin\\phi \\approx 2 M_s B \\phi$$
$$E(\\phi) \\approx -\\lambda M_s^2 + 2 \\lambda M_s^2 \\phi^2 - 2 M_s B \\phi$$
Minimizing with respect to $\\phi$:
$$\\frac{dE}{d\\phi} = 4 \\lambda M_s^2 \\phi - 2 M_s B = 0 \\implies \\phi = \\frac{B}{2 \\lambda M_s}$$
The net induced magnetization along the field is:
$$M_\\perp = 2 M_s \\sin\\phi \\approx 2 M_s \\phi = 2 M_s \\left( \\frac{B}{2 \\lambda M_s} \\right) = \\frac{B}{\\lambda}$$
The perpendicular susceptibility is:
$$\\chi_\\perp = \\frac{\\mu_0 M_\\perp}{B} = \\frac{\\mu_0}{\\lambda} = \\text{constant}$$
Since neither $\\lambda$ nor the canting torque depends on temperature, $\\chi_\\perp$ is **strictly independent of temperature** for all $T \\le T_N$.

**(b) Parallel Susceptibility $\\chi_\\parallel$:**
When $\\vec{B} \\parallel$ easy axis, the field acts directly along the spin quantization axis without canting.
Sublattice $A$ feels $B_A = \\lambda M_s + B$, and sublattice $B$ feels $B_B = \\lambda M_s - B$.
At $T = 0\\text{ K}$, all spins are fully frozen in their ground state ($M_A = M_B = M_0$). Since there are no thermal excitations to flip a spin against the exchange field $B_{\\text{ex}} = \\lambda M_s \\sim 100\\text{ T}$:
$$\\lim_{T \\to 0} \\chi_\\parallel(T) = 0$$
As $T \\to T_N^-$, thermal fluctuations allow spin inversions, and $\\chi_\\parallel(T)$ rises monotonically until it merges smoothly with $\\chi_\\perp$ at $T = T_N$:
$$\\chi_\\parallel(T_N) = \\chi_\\perp = \\frac{\\mu_0}{\\lambda}$$

**(c) Critical Spin-Flop Field $B_{\\text{sf}}$:**
In the parallel collinear configuration ($\\vec{M} \\parallel \\vec{B}$):
The anisotropy energy is zero (spins along easy axis). The magnetic energy gain is $-\\frac{1}{2}\\chi_\\parallel B^2$.
$$E_\\parallel = -\\frac{1}{2} \\chi_\\parallel B^2$$
In the spin-flop canted configuration ($\\vec{M} \\perp \\vec{B}$):
The spins have rotated away from the easy axis, costing anisotropy energy $K$. But they can cant toward the field, gaining $-\\frac{1}{2}\\chi_\\perp B^2$:
$$E_\\perp = K - \\frac{1}{2} \\chi_\\perp B^2$$
The spin-flop transition occurs when $E_\\perp < E_\\parallel$:
$$K - \\frac{1}{2}\\chi_\\perp B^2 < -\\frac{1}{2}\\chi_\\parallel B^2 \\implies \\frac{1}{2}(\\chi_\\perp - \\chi_\\parallel) B^2 > K$$
At low temperatures where $\\chi_\\parallel \\approx 0$ and $\\chi_\\perp = \\mu_0 / \\lambda$:
$$\\frac{\\mu_0}{2\\lambda} B_{\\text{sf}}^2 = K \\implies B_{\\text{sf}} = \\sqrt{\\frac{2 \\lambda K}{\\mu_0}} = \\sqrt{2 B_{\\text{ex}} B_{\\text{aniso}}}$$
where $B_{\\text{ex}} = \\lambda M_s / \\mu_0$ is the exchange field and $B_{\\text{aniso}} = K / M_s$ is the anisotropy field. The spin-flop field is the geometric mean of the exchange and anisotropy fields!"""
        },
        {
            "id": "ssp2-prob-4-3",
            "title": "Variational Theory of 180° Bloch Domain Wall Width & Energy",
            "statement": "The spatial magnetization angle $\\theta(x)$ across a 180° Bloch domain wall varies from $\\theta(-\\infty) = 0$ to $\\theta(+\\infty) = \\pi$. The areal energy functional is:\\n$$\\sigma_w = \\int_{-\\infty}^\\infty \\left[ A \\left( \\frac{d\\theta}{dx} \\right)^2 + K_1 \\sin^2\\theta \\right] dx$$\\n\\n(a) Use the Euler-Lagrange variational equation to derive the first-order differential equation governing the spin profile $\\theta(x)$.\\n(b) Integrate the differential equation to prove the exact soliton profile $\\cos\\theta(x) = -\\tanh(x / \\delta_0)$ and determine the characteristic domain wall parameter $\\delta_0 = \\sqrt{A/K_1}$.\\n(c) Calculate the exact total areal wall energy $\\sigma_w = 4\\sqrt{A K_1}$. For iron with $A = 2.0 \\times 10^{-11}\\text{ J/m}$ and $K_1 = 4.8 \\times 10^4\\text{ J/m}^3$, evaluate $\\delta_0$, the effective wall width $\\pi\\delta_0$, and the areal energy $\\sigma_w$ in $\\text{mJ/m}^2$.",
            "solution": r"""**(a) Euler-Lagrange Equation for Domain Wall:**
Let the integrand be $\\mathcal{L}\\left(\\theta, \\frac{d\\theta}{dx}\\right) = A \\left(\\frac{d\\theta}{dx}\\right)^2 + K_1 \\sin^2\\theta$.
Because $\\mathcal{L}$ does not depend explicitly on $x$, the Beltrami identity (first integral of Euler-Lagrange) holds:
$$\\mathcal{L} - \\left(\\frac{d\\theta}{dx}\\right) \\frac{\\partial \\mathcal{L}}{\\partial (d\\theta/dx)} = \\text{constant}$$
$$A \\left(\\frac{d\\theta}{dx}\\right)^2 + K_1 \\sin^2\\theta - 2A \\left(\\frac{d\\theta}{dx}\\right)^2 = \\text{const} \\implies K_1 \\sin^2\\theta - A \\left(\\frac{d\\theta}{dx}\\right)^2 = \\text{const}$$
As $x \\to \\pm\\infty$, $\\theta \\to 0$ or $\\pi$, where $\\sin\\theta \\to 0$ and $d\\theta/dx \\to 0$. Thus the constant is zero:
$$A \\left(\\frac{d\\theta}{dx}\\right)^2 = K_1 \\sin^2\\theta \\implies \\frac{d\\theta}{dx} = \\sqrt{\\frac{K_1}{A}} \\sin\\theta$$
Notice that at every point inside the domain wall, the exchange energy density $A(d\\theta/dx)^2$ exactly equals the anisotropy energy density $K_1 \\sin^2\\theta$ (equipartition of micromagnetic energy!).

**(b) Integration of the Spin Profile:**
Separate variables:
$$\\frac{d\\theta}{\\sin\\theta} = \\sqrt{\\frac{K_1}{A}} dx = \\frac{dx}{\\delta_0}, \\quad \\delta_0 \\equiv \\sqrt{\\frac{A}{K_1}}$$
Using the standard integral $\\int \\frac{d\\theta}{\\sin\\theta} = \\ln\\left|\\tan\\left(\\frac{\\theta}{2}\\right)\\right|$:
$$\\ln\\tan\\left(\\frac{\\theta}{2}\\right) = \\frac{x}{\\delta_0} \\implies \\tan\\left(\\frac{\\theta}{2}\\right) = e^{x / \\delta_0}$$
Using the trigonometric identity $\\cos\\theta = \\frac{1 - \\tan^2(\\theta/2)}{1 + \\tan^2(\\theta/2)}$:
$$\\cos\\theta = \\frac{1 - e^{2x/\\delta_0}}{1 + e^{2x/\\delta_0}} = \\frac{e^{-x/\\delta_0} - e^{x/\\delta_0}}{e^{-x/\\delta_0} + e^{x/\\delta_0}} = -\\tanh\\left(\\frac{x}{\\delta_0}\\right)$$
Also, $\\sin\\theta = \\operatorname{sech}(x / \\delta_0)$.
The effective wall width is historically defined by the maximum slope $\\pi / (d\\theta/dx)_{x=0} = \\pi \\delta_0 = \\pi \\sqrt{A/K_1}$.

**(c) Exact Total Wall Energy & Numerical Values for Iron:**
Substitute $A(d\\theta/dx)^2 = K_1 \\sin^2\\theta$ into the energy integral:
$$\\sigma_w = \\int_{-\\infty}^\\infty 2 K_1 \\sin^2\\theta dx = 2 K_1 \\int_{-\\infty}^\\infty \\sin\\theta \\left(\\sin\\theta \\frac{dx}{d\\theta}\\right) d\\theta$$
Since $\\frac{dx}{d\\theta} = \\frac{\\delta_0}{\\sin\\theta}$:
$$\\sigma_w = 2 K_1 \\delta_0 \\int_0^\\pi \\sin\\theta d\\theta = 2 K_1 \\sqrt{\\frac{A}{K_1}} [-\\cos\\theta]_0^\\pi = 2\\sqrt{A K_1} [1 - (-1)] = 4\\sqrt{A K_1}$$

**Numerical Evaluation for Iron:**
$$A = 2.0 \\times 10^{-11}\\text{ J/m}, \\quad K_1 = 4.8 \\times 10^4\\text{ J/m}^3$$
$$\\delta_0 = \\sqrt{\\frac{2.0 \\times 10^{-11}}{4.8 \\times 10^4}} = \\sqrt{4.167 \\times 10^{-16}} \\approx 2.04 \\times 10^{-8}\\text{ m} = 20.4\\text{ nm}$$
$$\\text{Effective wall width } \\delta_w = \\pi \\delta_0 = 3.1416 \\times 20.4\\text{ nm} \\approx 64.1\\text{ nm}$$
The total wall energy is:
$$\\sigma_w = 4\\sqrt{(2.0 \\times 10^{-11})(4.8 \\times 10^4)} = 4\\sqrt{9.6 \\times 10^{-7}} = 4 \\times (9.798 \\times 10^{-4}) \\approx 3.92 \\times 10^{-3}\\text{ J/m}^2 = 3.92\\text{ mJ/m}^2$$
The Bloch wall in iron spans $\\sim 64\\text{ nm}$ (roughly 220 atomic lattice planes) with an areal tension of $3.92\\text{ mJ/m}^2$."""
        }
    ]
}

with open("ssp2_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3_data, f, indent=2)

with open("ssp2_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4_data, f, indent=2)

print("Generated ssp2_u3.json and ssp2_u4.json successfully.")
