# build_ssp2_units_1_2.py
# Generates ssp2_u1.json and ssp2_u2.json for Course #18: Solid State Physics II

import json

# =========================================================================
# UNIT 1: Quantum Electronic Band Theory: Bloch Theorem, Kronig-Penney & Effective Mass
# =========================================================================

u1_data = {
    "title": "Quantum Electronic Band Theory: Bloch Theorem, Kronig-Penney & Effective Mass",
    "subtitle": "Periodic Potentials, Bragg Reflection, Band Gaps & Hole Dynamics",
    "summary": "This foundational unit develops the quantum mechanical theory of electrons propagating through a periodic crystalline lattice. We establish Bloch's theorem from translational symmetry and derive the Central Equation in reciprocal space. We examine how electron Bragg reflection at Brillouin zone boundaries leads to forbidden energy band gaps in the nearly free electron model and solve the transcendental Kronig-Penney model across all barrier limits. Finally, we formulate the semiclassical equations of motion, derive the effective mass tensor, introduce the concept of holes with positive charge, and classify metals, semimetals, semiconductors, and insulators based on their electronic band structure.",
    "sections": [
        {
            "id": "sec-1-1",
            "title": "Periodic Lattice Potentials, Translational Invariance & Bloch's Theorem",
            "content": """
<h3>1. The Crystal Hamiltonian & Discrete Translational Symmetry</h3>
<p>
In an ideal, defect-free single crystal, the atomic nuclei are arranged in a regular Bravais lattice defined by real-space lattice translation vectors:
</p>
$$\\vec{R} = n_1 \\vec{a}_1 + n_2 \\vec{a}_2 + n_3 \\vec{a}_3, \\quad n_1, n_2, n_3 \\in \\mathbb{Z}$$
<p>
The single-particle crystal potential experienced by an electron satisfies exact spatial periodicity:
</p>
$$V(\\vec{r} + \\vec{R}) = V(\\vec{r})$$
<p>
The single-electron stationary Schrödinger equation is:
</p>
$$\\hat{H} \\psi(\\vec{r}) = \\left[ -\\frac{\\hbar^2}{2m} \\nabla^2 + V(\\vec{r}) \\right] \\psi(\\vec{r}) = E \\psi(\\vec{r})$$
<p>
We define the real-space translation operator $\\hat{T}_{\\vec{R}}$ acting on an arbitrary wavefunction $\\psi(\\vec{r})$:
</p>
$$\\hat{T}_{\\vec{R}} \\psi(\\vec{r}) \\equiv \\psi(\\vec{r} + \\vec{R})$$
<p>
Because $V(\\vec{r} + \\vec{R}) = V(\\vec{r})$ and the Laplacian $\\nabla^2$ is invariant under rigid translations, $\\hat{T}_{\\vec{R}}$ commutes with the Hamiltonian:
</p>
$$[\\hat{H}, \\hat{T}_{\\vec{R}}] = 0, \\quad [\\hat{T}_{\\vec{R}}, \\hat{T}_{\\vec{R}'}] = 0$$
<p>
Therefore, the Hamiltonian and the translation operators share a complete set of simultaneous stationary eigenfunctions.
</p>

<h3>2. Mathematical Proof of Bloch's Theorem</h3>
<p>
Let $\\psi(\\vec{r})$ be an eigenstate of $\\hat{T}_{\\vec{R}}$ with eigenvalue $C(\\vec{R})$:
</p>
$$\\hat{T}_{\\vec{R}} \\psi(\\vec{r}) = \\psi(\\vec{r} + \\vec{R}) = C(\\vec{R}) \\psi(\\vec{r})$$
<p>
Applying successive translations $\\vec{R}_1$ and $\\vec{R}_2$:
</p>
$$\\hat{T}_{\\vec{R}_1 + \\vec{R}_2} \\psi(\\vec{r}) = C(\\vec{R}_1 + \\vec{R}_2) \\psi(\\vec{r}) = C(\\vec{R}_1) C(\\vec{R}_2) \\psi(\\vec{r})$$
$$\\implies C(\\vec{R}_1 + \\vec{R}_2) = C(\\vec{R}_1) C(\\vec{R}_2)$$
<p>
Under periodic Born-von Kármán boundary conditions for a macroscopic crystal of dimensions $L_i = N_i a_i$ along basis directions $\\vec{a}_i$, the wavefunction must remain finite and normalizeable everywhere:
</p>
$$\\psi(\\vec{r} + N_i \\vec{a}_i) = \\psi(\\vec{r}) \\implies [C(\\vec{a}_i)]^{N_i} = 1 \\implies |C(\\vec{R})| = 1$$
<p>
The only function satisfying this multiplicative property and unitarity is a complex phase:
</p>
$$C(\\vec{R}) = e^{i \\vec{k} \\cdot \\vec{R}}$$
<p>
where $\\vec{k}$ is a real vector in reciprocal space known as the <strong>crystal wavevector</strong>. Hence:
</p>
$$\\psi_{\\vec{k}}(\\vec{r} + \\vec{R}) = e^{i \\vec{k} \\cdot \\vec{R}} \\psi_{\\vec{k}}(\\vec{r})$$
<p>
Defining $u_{\\vec{k}}(\\vec{r}) \\equiv e^{-i \\vec{k} \\cdot \\vec{r}} \\psi_{\\vec{k}}(\\vec{r})$, we verify its periodicity:
</p>
$$u_{\\vec{k}}(\\vec{r} + \\vec{R}) = e^{-i \\vec{k} \\cdot (\\vec{r} + \\vec{R})} \\psi_{\\vec{k}}(\\vec{r} + \\vec{R}) = e^{-i \\vec{k} \\cdot \\vec{r}} e^{-i \\vec{k} \\cdot \\vec{R}} e^{i \\vec{k} \\cdot \\vec{R}} \\psi_{\\vec{k}}(\\vec{r}) = u_{\\vec{k}}(\\vec{r})$$
<p>
This establishes <strong>Bloch's Theorem</strong>: The eigenstates of a one-electron Hamiltonian in a periodic potential can be chosen in the form of a plane wave modulated by a cell-periodic amplitude:
</p>
$$\\psi_{\\vec{k}}(\\vec{r}) = e^{i \\vec{k} \\cdot \\vec{r}} u_{\\vec{k}}(\\vec{r}), \\quad \\text{where } u_{\\vec{k}}(\\vec{r} + \\vec{R}) = u_{\\vec{k}}(\\vec{r})$$
"""
        },
        {
            "id": "sec-1-2",
            "title": "The Central Equation: Reciprocal Lattice Fourier Expansion & Zone Boundaries",
            "content": """
<h3>1. Fourier Expansion in Reciprocal Space</h3>
<p>
Any function possessing the full translational periodicity of the Bravais lattice, such as the potential $V(\\vec{r})$ and the periodic Bloch factor $u_{\\vec{k}}(\\vec{r})$, can be expanded in a Fourier series over the reciprocal lattice vectors $\\vec{G}$:
</p>
$$V(\\vec{r}) = \\sum_{\\vec{G}} V_{\\vec{G}} e^{i \\vec{G} \\cdot \\vec{r}}, \\quad \\vec{G} \\cdot \\vec{R} = 2\\pi n, \\quad n \\in \\mathbb{Z}$$
<p>
Because $V(\\vec{r})$ is real-valued, the Fourier components satisfy $V_{-\\vec{G}} = V_{\\vec{G}}^*$. By shifting the zero of energy, we can set $V_{\\vec{G}=0} = 0$.
</p>
<p>
Similarly, the full Bloch wavefunction $\\psi_{\\vec{k}}(\\vec{r})$ can be written as a plane-wave expansion:
</p>
$$\\psi_{\\vec{k}}(\\vec{r}) = \\sum_{\\vec{G}} C(\\vec{k} - \\vec{G}) e^{i (\\vec{k} - \\vec{G}) \\cdot \\vec{r}}$$

<h3>2. Derivation of the Central Equation</h3>
<p>
Substituting the Fourier expansions into the Schrödinger equation:
</p>
$$\\sum_{\\vec{G}} \\frac{\\hbar^2}{2m} (\\vec{k} - \\vec{G})^2 C(\\vec{k} - \\vec{G}) e^{i (\\vec{k} - \\vec{G}) \\cdot \\vec{r}} + \\sum_{\\vec{G}'} V_{\\vec{G}'} e^{i \\vec{G}' \\cdot \\vec{r}} \\sum_{\\vec{G}''} C(\\vec{k} - \\vec{G}'') e^{i (\\vec{k} - \\vec{G}'') \\cdot \\vec{r}} = E \\sum_{\\vec{G}} C(\\vec{k} - \\vec{G}) e^{i (\\vec{k} - \\vec{G}) \\cdot \\vec{r}}$$
<p>
Setting $\\vec{G} = \\vec{G}'' - \\vec{G}'$ in the second term, multiplying by $e^{-i (\\vec{k} - \\vec{G}) \\cdot \\vec{r}}$, and integrating over the crystal volume using the orthogonality of plane waves:
</p>
$$\\left( \\frac{\\hbar^2}{2m} (\\vec{k} - \\vec{G})^2 - E \\right) C(\\vec{k} - \\vec{G}) + \\sum_{\\vec{G}'} V_{\\vec{G} - \\vec{G}'} C(\\vec{k} - \\vec{G}') = 0$$
<p>
Letting $\\lambda_{\\vec{k}-\\vec{G}} \\equiv \\frac{\\hbar^2}{2m} (\\vec{k} - \\vec{G})^2$ represent the free-electron kinetic energy, this infinite set of algebraic equations is known as the <strong>Central Equation</strong>:
</p>
$$(\\lambda_{\\vec{k}-\\vec{G}} - E) C(\\vec{k} - \\vec{G}) + \\sum_{\\vec{G}'} V_{\\vec{G}'} C(\\vec{k} - \\vec{G} - \\vec{G}') = 0$$
<p>
Nontrivial solutions require the vanishing of the infinite secular determinant, generating the discrete band energies $E_n(\\vec{k})$ indexed by the band index $n$.
</p>
"""
        },
        {
            "id": "sec-1-3",
            "title": "Electron Bragg Reflection & Band Gap Opening in the Nearly Free Electron Model",
            "content": """
<h3>1. Semiclassical Bragg Reflection of Matter Waves</h3>
<p>
In the nearly free electron (NFE) approximation, the lattice potential $V(\\vec{r})$ is regarded as a weak perturbation relative to the kinetic energy: $|V_{\\vec{G}}| \\ll E_F$.
</p>
<p>
Away from the Brillouin zone boundaries, the kinetic energies $\\lambda_{\\vec{k}}$ and $\\lambda_{\\vec{k}-\\vec{G}}$ are widely separated, so mixing is negligible. However, when $\\vec{k}$ approaches a Bragg plane in reciprocal space:
</p>
$$\\lambda_{\\vec{k}} \\approx \\lambda_{\\vec{k}-\\vec{G}} \\implies |\\vec{k}|^2 \\approx |\\vec{k} - \\vec{G}|^2 \\implies 2\\vec{k} \\cdot \\vec{G} = |\\vec{G}|^2$$
<p>
This is precisely the Von Laue condition for <strong>Bragg reflection</strong> of electron waves off the crystal planes. At this boundary, the forward-propagating plane wave $e^{i \\vec{k} \\cdot \\vec{r}}$ and backscattered wave $e^{i (\\vec{k} - \\vec{G}) \\cdot \\vec{r}}$ interfere constructively.
</p>

<h3>2. Secular Determinant & Energy Gap Derivation</h3>
<p>
Retaining only the two strongly degenerate plane wave states $|\\vec{k}\\rangle$ and $|\\vec{k} - \\vec{G}\\rangle$, the Central Equation reduces to a $2 \\times 2$ secular matrix:
</p>
$$\\begin{pmatrix} \\lambda_{\\vec{k}} - E & V_{\\vec{G}} \\\\ V_{\\vec{G}}^* & \\lambda_{\\vec{k}-\\vec{G}} - E \\end{pmatrix} \\begin{pmatrix} C(\\vec{k}) \\\\ C(\\vec{k}-\\vec{G}) \\end{pmatrix} = 0$$
<p>
Setting the determinant to zero:
</p>
$$(\\lambda_{\\vec{k}} - E)(\\lambda_{\\vec{k}-\\vec{G}} - E) - |V_{\\vec{G}}|^2 = 0$$
$$E^2 - (\\lambda_{\\vec{k}} + \\lambda_{\\vec{k}-\\vec{G}}) E + \\lambda_{\\vec{k}} \\lambda_{\\vec{k}-\\vec{G}} - |V_{\\vec{G}}|^2 = 0$$
<p>
Solving the quadratic equation:
</p>
$$E_{\\pm}(\\vec{k}) = \\frac{\\lambda_{\\vec{k}} + \\lambda_{\\vec{k}-\\vec{G}}}{2} \\pm \\sqrt{ \\left( \\frac{\\lambda_{\\vec{k}} - \\lambda_{\\vec{k}-\\vec{G}}}{2} \\right)^2 + |V_{\\vec{G}}|^2 }$$
<p>
Exactly at the Brillouin zone boundary where $\\lambda_{\\vec{k}} = \\lambda_{\\vec{k}-\\vec{G}}$:
</p>
$$E_{\\pm} = \\lambda_{\\vec{k}} \\pm |V_{\\vec{G}}|$$
<p>
The energy difference defines the fundamental <strong>energy band gap</strong> $E_g$:
</p>
$$E_g = E_+ - E_- = 2 |V_{\\vec{G}}|$$
<p>
The two standing wave eigenstates at the zone boundary correspond to:
</p>
$$\\psi_+(\\vec{r}) \\sim \\cos(\\vec{G} \\cdot \\vec{r} / 2), \\quad \\psi_-(\\vec{r}) \\sim \\sin(\\vec{G} \\cdot \\vec{r} / 2)$$
<p>
The $\\psi_+$ state piles electron charge directly atop the attractive ionic cores ($V < 0$), lowering its energy, whereas $\\psi_-$ concentrates probability density midway between the ions, raising its energy. This electrostatic potential difference opens the forbidden energy gap.
</p>
"""
        },
        {
            "id": "sec-1-4",
            "title": "The Kronig-Penney Model: 1D Dirac Delta & Square Well Potentials",
            "content": """
<h3>1. Formulation of the 1D Kronig-Penney Model</h3>
<p>
To understand how discrete atomic energy levels evolve continuously into energy bands, Kronig and Penney (1931) modeled an infinite 1D crystal with an array of rectangular potential barriers of height $V_0$, width $b$, and lattice period $a$ (well width $w = a - b$):
</p>
$$V(x) = \\begin{cases} 0, & 0 < x < a - b \\\\ V_0, & a - b < x < a \\end{cases}, \\quad V(x + a) = V(x)$$
<p>
In the well region ($0 < x < a - b$), where $V = 0$:
</p>
$$\\psi_1(x) = A e^{i K_1 x} + B e^{-i K_1 x}, \\quad K_1 = \\sqrt{\\frac{2mE}{\\hbar^2}}$$
<p>
In the barrier region ($a - b < x < a$), for $E < V_0$:
</p>
$$\\psi_2(x) = C e^{K_2 x} + D e^{-K_2 x}, \\quad K_2 = \\sqrt{\\frac{2m(V_0 - E)}{\\hbar^2}}$$
<p>
By Bloch's theorem, $\\psi(x + a) = e^{i k a} \\psi(x)$. Applying boundary conditions of continuity of $\\psi(x)$ and $d\\psi/dx$ at $x = 0$ and $x = a - b$:
</p>

<h3>2. The Dirac Delta-Barrier Limit & Transcendental Dispersion</h3>
<p>
Taking the delta-function limit where the barrier width $b \\to 0$ and height $V_0 \\to \\infty$ such that the barrier area $b V_0$ remains finite, we define the dimensionless barrier strength parameter $P$:
</p>
$$P \\equiv \\lim_{b \\to 0, V_0 \\to \\infty} \\frac{m V_0 b a}{\\hbar^2}$$
<p>
The determinant condition yields the famous <strong>Kronig-Penney dispersion relation</strong>:
</p>
$$P \\frac{\\sin(\\alpha a)}{\\alpha a} + \\cos(\\alpha a) = \\cos(k a)$$
<p>
where $\\alpha = \\sqrt{2mE/\\hbar^2}$ and $k$ is the crystal wavevector in the first Brillouin zone ($-\\pi/a \\le k \\le \\pi/a$).
</p>
<ul>
  <li>Since $|\\cos(ka)| \\le 1$, energy solutions $\\alpha$ are <strong>only allowed</strong> where:
  $$-1 \\le P \\frac{\\sin(\\alpha a)}{\\alpha a} + \\cos(\\alpha a) \\le 1$$</li>
  <li>Whenever the left-hand side exceeds $+1$ or drops below $-1$, no real wavevector $k$ exists. These forbidden energy intervals constitute the <strong>forbidden energy band gaps</strong>.</li>
  <li><strong>Free Electron Limit ($P \\to 0$):</strong> $\\cos(\\alpha a) = \\cos(ka) \\implies \\alpha = k \\implies E = \\frac{\\hbar^2 k^2}{2m}$ (Continuous parabolic band).</li>
  <li><strong>Tight-Binding Atomic Limit ($P \\to \\infty$):</strong> $\\sin(\\alpha a) = 0 \\implies \\alpha a = n\\pi \\implies E_n = \\frac{\\hbar^2 \\pi^2 n^2}{2m a^2}$ (Discrete atomic bound states in an infinite square well).</li>
</ul>
""",
            "simulation": "ssp2-kronig-penney-sim",
            "simulations": ["ssp2-kronig-penney-sim"]
        },
        {
            "id": "sec-1-5",
            "title": "Semiclassical Electron Dynamics: Wavepackets, Group Velocity & Crystal Momentum",
            "content": """
<h3>1. Electron Wavepackets & Group Velocity</h3>
<p>
An electron in a crystal is represented by a wavepacket composed of Bloch states localized in both real space and crystal momentum space. The physical velocity of the electron is the <strong>group velocity</strong> $v_g$ of the envelope:
</p>
$$\\vec{v}_g(\\vec{k}) = \\frac{1}{\\hbar} \\nabla_{\\vec{k}} E(\\vec{k})$$
<p>
In one dimension:
</p>
$$v_g(k) = \\frac{1}{\\hbar} \\frac{dE}{dk}$$
<p>
Key physical consequences of group velocity:
</p>
<ul>
  <li>At the bottom of an energy band ($k = 0$), $dE/dk = 0$, so $v_g = 0$.</li>
  <li>Near the center of the band, $v_g$ reaches a maximum value.</li>
  <li>At the Brillouin zone boundary ($k = \\pm \\pi/a$), Bragg reflection forces $dE/dk = 0$, so $v_g = 0$. The electron forms a standing wave and cannot transport net charge forward!</li>
</ul>

<h3>2. Semiclassical Equation of Motion</h3>
<p>
When an external electric field $\\vec{\\mathcal{E}}$ or magnetic field $\\vec{B}$ is applied over macroscopic scales much larger than the lattice constant $a$, the rate of work done on the electron wavepacket is:
</p>
$$\\frac{dE}{dt} = \\vec{F}_{\\text{ext}} \\cdot \\vec{v}_g = \\vec{F}_{\\text{ext}} \\cdot \\left( \\frac{1}{\\hbar} \\nabla_{\\vec{k}} E \\right)$$
<p>
Using the chain rule:
</p>
$$\\frac{dE}{dt} = \\nabla_{\\vec{k}} E \\cdot \\frac{d\\vec{k}}{dt}$$
<p>
Comparing the two expressions gives the fundamental <strong>semiclassical equation of motion</strong>:
</p>
$$\\hbar \\frac{d\\vec{k}}{dt} = \\vec{F}_{\\text{ext}} = -e \\left( \\vec{\\mathcal{E}} + \\vec{v}_g \\times \\vec{B} \\right)$$
<p>
Here, $\\hbar\\vec{k}$ represents the <strong>crystal momentum</strong>. It is not the total kinematic momentum $m\\vec{v}$ of the electron, because the periodic lattice potential can absorb or impart discrete momentum quanta $\\hbar\\vec{G}$ through Bragg diffraction.
</p>
"""
        },
        {
            "id": "sec-1-6",
            "title": "The Effective Mass Tensor, Negative Effective Mass & Concept of Positive Holes",
            "content": """
<h3>1. Derivation of the Effective Mass Tensor</h3>
<p>
Differentiating the group velocity $\\vec{v}_g$ with respect to time gives the semiclassical acceleration:
</p>
$$a_i = \\frac{d v_{g,i}}{dt} = \\frac{d}{dt} \\left( \\frac{1}{\\hbar} \\frac{\\partial E}{\\partial k_i} \\right) = \\frac{1}{\\hbar} \\sum_j \\frac{\\partial^2 E}{\\partial k_i \\partial k_j} \\frac{d k_j}{dt}$$
<p>
Substituting $\\hbar \\frac{dk_j}{dt} = F_j$:
</p>
$$a_i = \\sum_j \\left[ \\frac{1}{\\hbar^2} \\frac{\\partial^2 E}{\\partial k_i \\partial k_j} \\right] F_j$$
<p>
Comparing this with Newton's second law in tensor form $a_i = \\sum_j (m^*)^{-1}_{ij} F_j$, we define the inverse <strong>effective mass tensor</strong>:
</p>
$$\\left( \\frac{1}{m^*} \\right)_{ij} \\equiv \\frac{1}{\\hbar^2} \\frac{\\partial^2 E(\\vec{k})}{\\partial k_i \\partial k_j}$$
<p>
In an isotropic band in one dimension:
</p>
$$m^*(k) = \\frac{\\hbar^2}{\\frac{d^2 E}{dk^2}}$$
<p>
The effective mass encapsulates the entire dynamic interaction between the electron and the periodic periodic potential of the ionic lattice. The external force alone governs the acceleration, provided $m$ is replaced by $m^*$.
</p>

<h3>2. Negative Effective Mass & The Concept of Positive Holes</h3>
<p>
Near the top of an energy band, the band curvature is downward:
</p>
$$\\frac{d^2 E}{dk^2} < 0 \\implies m^* < 0$$
<p>
An electron with negative effective mass accelerates <em>opposite</em> to the applied force $\\vec{F} = -e\\vec{\\mathcal{E}}$. This paradoxical behavior occurs because the electron is Bragg-scattered backwards by the lattice more strongly than the forward pull of the external field!
</p>
<p>
In a nearly filled band, instead of tracking $10^{22}\\text{ cm}^{-3}$ electrons with negative effective mass, it is mathematically and physically equivalent to treat the empty states as quasiparticles called <strong>holes</strong>:
</p>
<ul>
  <li><strong>Charge:</strong> $q_h = -q_e = +e$ (positive elementary charge)</li>
  <li><strong>Wavevector:</strong> $\\vec{k}_h = -\\vec{k}_e$</li>
  <li><strong>Energy:</strong> $E_h(\\vec{k}_h) = -E_e(\\vec{k}_e)$</li>
  <li><strong>Effective Mass:</strong> $m_h^* = -m_e^* > 0$ (positive effective mass!)</li>
  <li><strong>Velocity:</strong> $\\vec{v}_h = \\vec{v}_e$</li>
</ul>
""",
            "simulation": "ssp2-effective-mass-sim",
            "simulations": ["ssp2-effective-mass-sim"]
        },
        {
            "id": "sec-1-7",
            "title": "Electronic Classification of Solids: Metals, Semimetals, Insulators & Intrinsic Semiconductors",
            "content": """
<h3>1. Band Filling & Electrical Conductivity</h3>
<p>
According to the Pauli exclusion principle, each spatial Bloch orbital $|\psi_{\vec{k}}\rangle$ can accommodate at most two electrons of opposite spin ($s_z = \pm 1/2$). In a 1D crystal with $N$ primitive unit cells, each Brillouin zone contains exactly $N$ allowed $\vec{k}$ states, yielding a capacity of:
</p>
$$\\text{Capacity per band} = 2N \\text{ electrons}$$
<p>
A completely filled band carries <strong>zero net electrical current</strong> under an applied electric field, because for every electron moving with velocity $+v_g(\vec{k})$, there exists another electron with opposite velocity $-v_g(-\vec{k})$:
</p>
$$\\vec{J} = -e \\sum_{\\vec{k} \\in \\text{filled}} \\vec{v}_g(\\vec{k}) = -\\frac{e}{\\hbar} \\int_{\\text{BZ}} \\nabla_{\\vec{k}} E(\\vec{k}) \\frac{d^3k}{(2\\pi)^3} = 0$$

<h3>2. Taxonomy of Solids</h3>
<ul>
  <li><strong>Metals (Good Conductors):</strong> Possess a partially filled band (e.g. monovalent alkali metals like Na, Cu with 1 valence electron per atom filling half the zone), or overlapping conduction and valence bands (divalent alkaline earth metals like Mg, Ca). The Fermi level $E_F$ cuts through an allowed band, providing continuous unoccupied states immediately adjacent in energy, enabling high electrical conductivity $\\sigma \\sim 10^7\\text{ S/m}$ at low temperatures.</li>
  <li><strong>Insulators:</strong> Have completely filled valence bands separated from completely empty conduction bands by a large fundamental energy gap $E_g > 3.5\\text{ eV}$ (e.g. diamond with $E_g = 5.47\\text{ eV}$, $\\text{SiO}_2$ with $E_g = 9\\text{ eV}$). At room temperature ($k_B T \\approx 0.026\\text{ eV}$), thermal excitation across the gap is negligible ($e^{-E_g/2k_B T} \\sim 10^{-46}$), yielding electrical resistivity $\\rho > 10^{12}\\ \\Omega\\cdot\\text{m}$.</li>
  <li><strong>Intrinsic Semiconductors:</strong> Possess the exact same band topology as insulators, but with a modest energy band gap $E_g \\lesssim 2.0\\text{ eV}$ (e.g. silicon $E_g = 1.12\\text{ eV}$, germanium $E_g = 0.66\\text{ eV}$, gallium arsenide $E_g = 1.42\\text{ eV}$). At $T = 0\\text{ K}$, semiconductors are perfect insulators; at room temperature, thermal excitation promotes electrons into the conduction band while leaving mobile holes in the valence band.</li>
  <li><strong>Semimetals:</strong> Have a very small negative band gap where the top of the valence band slightly overlaps the bottom of the conduction band at different points in reciprocal space (e.g. bismuth, antimony, graphite), producing small equal numbers of electron and hole pockets with low carrier densities ($n \\sim 10^{17}-10^{19}\\text{ cm}^{-3}$).</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-1-1",
            "title": "Central Equation Formulation & Band Gap of a Periodic Cosine Potential",
            "statement": "An electron moves in a 1D lattice of constant $a$ under a weak periodic potential $V(x) = 2V_1 \\cos(2\\pi x / a) = V_1 (e^{i G x} + e^{-i G x})$, where $G = 2\\pi/a$ is the shortest reciprocal lattice vector.\\n\\n(a) Write down the Central Equation for the Fourier coefficients $C(k)$ and $C(k-G)$ near the Brillouin zone boundary $k \\approx G/2$.\\n(b) Solve the $2\\times 2$ secular determinant to determine the exact energy eigenvalues $E_\\pm(k)$.\\n(c) Calculate the exact magnitude of the energy band gap $E_g$ opened at $k = G/2 = \\pi/a$, and state the explicit wavefunctions $\\psi_+(x)$ and $\\psi_-(x)$ corresponding to the band edges.",
            "solution": """**(a) Central Equation Matrix:**
The Fourier components of the potential are $V_G = V_{-G} = V_1$, and all other $V_{G'} = 0$.
Near $k = \\pi/a = G/2$, the two kinetic energies $\\lambda_k = \\frac{\\hbar^2 k^2}{2m}$ and $\\lambda_{k-G} = \\frac{\\hbar^2 (k-G)^2}{2m}$ are nearly degenerate. Retaining only these two states in the Central Equation:
$$(\\lambda_k - E) C(k) + V_1 C(k-G) = 0$$
$$V_1 C(k) + (\\lambda_{k-G} - E) C(k-G) = 0$$

**(b) Secular Determinant & Energy Dispersion:**
For non-trivial solutions:
$$\\det \\begin{pmatrix} \\lambda_k - E & V_1 \\\\ V_1 & \\lambda_{k-G} - E \\end{pmatrix} = 0$$
$$(\\lambda_k - E)(\\lambda_{k-G} - E) - V_1^2 = 0$$
$$E^2 - (\\lambda_k + \\lambda_{k-G}) E + \\lambda_k \\lambda_{k-G} - V_1^2 = 0$$
Solving using the quadratic formula:
$$E_\\pm(k) = \\frac{\\lambda_k + \\lambda_{k-G}}{2} \\pm \\sqrt{ \\left(\\frac{\\lambda_k - \\lambda_{k-G}}{2}\\right)^2 + V_1^2 }$$

**(c) Band Gap at Zone Boundary & Wavefunctions:**
At the zone boundary $k = G/2 = \\pi/a$:
$$\\lambda_k = \\lambda_{k-G} = \\frac{\\hbar^2 (\\pi/a)^2}{2m} \\equiv E_0$$
Substituting this into the dispersion relation:
$$E_\\pm = E_0 \\pm V_1$$
The fundamental energy band gap is:
$$E_g = E_+ - E_- = (E_0 + V_1) - (E_0 - V_1) = 2 V_1$$
For the lower energy state $E_- = E_0 - V_1$, the eigenvector yields $C(k-G) = -C(k)$, producing the standing wave:
$$\\psi_-(x) \\propto e^{i G x/2} - e^{-i G x/2} \\propto \\sin(Gx/2) = \\sin(\\pi x / a)$$
For the upper state $E_+ = E_0 + V_1$, $C(k-G) = C(k)$, giving:
$$\\psi_+(x) \\propto e^{i G x/2} + e^{-i G x/2} \\propto \\cos(Gx/2) = \\cos(\\pi x / a)$$
The lower state piles electron probability at $x = a/2$ where $V(x) = -2V_1$, while the upper state piles probability at $x = 0$ where $V(x) = +2V_1$, accounting physically for the $2V_1$ energy separation."""
        },
        {
            "id": "ssp2-prob-1-2",
            "title": "Kronig-Penney Delta-Barrier Energy Eigenvalues & Band Widths",
            "statement": "Consider the Kronig-Penney model with periodic delta-function potential barriers $V(x) = \\frac{\\hbar^2 P}{m a} \\sum_n \\delta(x - n a)$.\\n\\n(a) From the dispersion relation $P \\frac{\\sin \\alpha a}{\\alpha a} + \\cos \\alpha a = \\cos k a$, calculate the lowest allowed energy $E_1$ (at $k = 0$) in the limit of small barrier strength $P \\ll 1$.\\n(b) Calculate the energy gap $E_g$ opened at the first Brillouin zone boundary ($k = \\pi/a$) for small $P \\ll 1$.\\n(c) In the opposite tight-binding limit $P \\gg 1$, derive the width of the lowest energy band $\\Delta E_1 = E(\\pi/a) - E(0)$.",
            "solution": """**(a) Lowest Energy Level for $P \\ll 1$ at $k = 0$:**
At $k = 0$, $\\cos(ka) = 1$. The Kronig-Penney relation is:
$$P \\frac{\\sin \\xi}{\\xi} + \\cos \\xi = 1, \\quad \\xi \\equiv \\alpha a$$
For small $P$ and small $\\xi$, expand $\\cos\\xi \\approx 1 - \\xi^2/2$ and $\\sin\\xi \\approx \\xi$:
$$P \\frac{\\xi}{\\xi} + 1 - \\frac{\\xi^2}{2} = 1 \\implies P - \\frac{\\xi^2}{2} = 0 \\implies \\xi^2 = 2P$$
Since $\\xi = \\alpha a = \\sqrt{2mE/\\hbar^2} a$:
$$\\alpha^2 a^2 = \\frac{2mE}{\\hbar^2} a^2 = 2P \\implies E_1(k=0) = \\frac{\\hbar^2 P}{m a^2}$$
Notice that this matches the spatial average potential $\\langle V \\rangle = \\frac{1}{a} \\int_0^a V(x) dx = \\frac{\\hbar^2 P}{m a^2}$.

**(b) Energy Gap at the First Zone Boundary ($k = \\pi/a$):**
At $k = \\pi/a$, $\\cos(ka) = -1$.
Let $\\xi = \\pi + \\delta$. Then $\\sin(\\pi + \\delta) = -\\sin\\delta \\approx -\\delta$, and $\\cos(\\pi + \\delta) = -\\cos\\delta \\approx -(1 - \\delta^2/2)$:
$$-P \\frac{\\delta}{\\pi} - \\left(1 - \\frac{\\delta^2}{2}\\right) = -1 \\implies \\frac{\\delta^2}{2} - \\frac{P}{\\pi}\\delta = 0$$
The two roots are $\\delta_1 = 0$ and $\\delta_2 = \\frac{2P}{\\pi}$.
The two boundary energies are:
$$E_- = \\frac{\\hbar^2 \\pi^2}{2m a^2}, \\quad E_+ = \\frac{\\hbar^2 (\\pi + \\delta_2)^2}{2m a^2} \\approx \\frac{\\hbar^2 \\pi^2}{2m a^2} \\left(1 + \\frac{2\\delta_2}{\\pi}\\right) = \\frac{\\hbar^2 \\pi^2}{2m a^2} + \\frac{2\\hbar^2 P}{m a^2}$$
The energy gap opened at the first zone boundary is:
$$E_g = E_+ - E_- = \\frac{2\\hbar^2 P}{m a^2}$$

**(c) Lowest Band Width for $P \\gg 1$:**
When $P \\gg 1$, the state approaches the infinite square well: $\\xi_n \\approx n\\pi$.
For the $n=1$ band, let $\\xi = \\pi - \\epsilon$.
$$P \\frac{\\sin(\\pi - \\epsilon)}{\\pi} + \\cos(\\pi - \\epsilon) = \\cos(ka)$$
$$\\frac{P}{\\pi} \\epsilon - 1 = \\cos(ka) \\implies \\epsilon = \\frac{\\pi}{P} [1 + \\cos(ka)]$$
At $k = 0$, $\\cos(ka) = 1 \\implies \\epsilon(0) = \\frac{2\\pi}{P}$, so $\\xi(0) = \\pi - \\frac{2\\pi}{P}$.
At $k = \\pi/a$, $\\cos(ka) = -1 \\implies \\epsilon(\\pi/a) = 0$, so $\\xi(\\pi/a) = \\pi$.
The band width is:
$$\\Delta E_1 = E(\\pi/a) - E(0) = \\frac{\\hbar^2}{2m a^2} [\\pi^2 - (\\pi - 2\\pi/P)^2] \\approx \\frac{\\hbar^2}{2m a^2} \\left( \\frac{4\\pi^2}{P} \\right) = \\frac{2\\pi^2 \\hbar^2}{m a^2 P}$$
As barrier strength $P \\to \\infty$, the band width shrinks inversely as $1/P$, narrowing into a discrete atomic bound state."""
        },
        {
            "id": "ssp2-prob-1-3",
            "title": "Effective Mass Tensor & Cyclotron Frequency in Anisotropic Tight-Binding Crystals",
            "statement": "An electron in an orthorhombic crystal with lattice constants $a, b, c$ has the 3D anisotropic tight-binding dispersion:\\n$$E(\\vec{k}) = E_0 - 2t_x \\cos(k_x a) - 2t_y \\cos(k_y b) - 2t_z \\cos(k_z c)$$\\n\\n(a) Compute the three diagonal components of the effective mass tensor $m_{xx}^*, m_{yy}^*, m_{zz}^*$ near the band bottom $\\vec{k} = 0$.\\n(b) Determine the group velocity vector $\\vec{v}_g(\\vec{k})$ at an arbitrary point in the Brillouin zone.\\n(c) A uniform magnetic field $\\vec{B} = B_0 \\hat{z}$ is applied along the $z$-axis. Derive the cyclotron resonance frequency $\\omega_c$ and the cyclotron effective mass $m_c^*$ in terms of $m_{xx}^*$ and $m_{yy}^*$.",
            "solution": """**(a) Diagonal Effective Mass Components:**
Expand the cosine terms near the band minimum $\\vec{k} = 0$:
$$\\cos(k_x a) \\approx 1 - \\frac{k_x^2 a^2}{2}, \\quad \\cos(k_y b) \\approx 1 - \\frac{k_y^2 b^2}{2}, \\quad \\cos(k_z c) \\approx 1 - \\frac{k_z^2 c^2}{2}$$
$$E(\\vec{k}) \\approx (E_0 - 2t_x - 2t_y - 2t_z) + t_x a^2 k_x^2 + t_y b^2 k_y^2 + t_z c^2 k_z^2$$
The effective mass components are:
$$\\frac{1}{m_{xx}^*} = \\frac{1}{\\hbar^2} \\frac{\\partial^2 E}{\\partial k_x^2} = \\frac{2 t_x a^2}{\\hbar^2} \\implies m_{xx}^* = \\frac{\\hbar^2}{2 t_x a^2}$$
$$\\frac{1}{m_{yy}^*} = \\frac{1}{\\hbar^2} \\frac{\\partial^2 E}{\\partial k_y^2} = \\frac{2 t_y b^2}{\\hbar^2} \\implies m_{yy}^* = \\frac{\\hbar^2}{2 t_y b^2}$$
$$\\frac{1}{m_{zz}^*} = \\frac{1}{\\hbar^2} \\frac{\\partial^2 E}{\\partial k_z^2} = \\frac{2 t_z c^2}{\\hbar^2} \\implies m_{zz}^* = \\frac{\\hbar^2}{2 t_z c^2}$$
All off-diagonal components vanish by orthorhombic reflection symmetry: $m_{ij}^* = 0$ for $i \\ne j$.

**(b) Group Velocity Vector:**
Using $\\vec{v}_g = \\frac{1}{\\hbar} \\nabla_{\\vec{k}} E$:
$$v_{gx} = \\frac{1}{\\hbar} \\frac{\\partial E}{\\partial k_x} = \\frac{2 t_x a}{\\hbar} \\sin(k_x a)$$
$$v_{gy} = \\frac{1}{\\hbar} \\frac{\\partial E}{\\partial k_y} = \\frac{2 t_y b}{\\hbar} \\sin(k_y b)$$
$$v_{gz} = \\frac{1}{\\hbar} \\frac{\\partial E}{\\partial k_z} = \\frac{2 t_z c}{\\hbar} \\sin(k_z c)$$
$$\\vec{v}_g(\\vec{k}) = \\frac{2}{\\hbar} \\left[ t_x a \\sin(k_x a) \\hat{x} + t_y b \\sin(k_y b) \\hat{y} + t_z c \\sin(k_z c) \\hat{z} \\right]$$

**(c) Cyclotron Resonance Frequency:**
Under $\\vec{B} = B_0 \\hat{z}$, the semiclassical equation of motion is:
$$\\hbar \\frac{d\\vec{k}}{dt} = -e (\\vec{v}_g \\times \\vec{B}) = -e (v_{gy} B_0 \\hat{x} - v_{gx} B_0 \\hat{y})$$
For small $k$, $v_{gx} \\approx \\frac{\\hbar k_x}{m_{xx}^*}$ and $v_{gy} \\approx \\frac{\\hbar k_y}{m_{yy}^*}$:
$$\\hbar \\frac{dk_x}{dt} = -e B_0 \\left(\\frac{\\hbar k_y}{m_{yy}^*}\\right) \\implies \\frac{dk_x}{dt} = -\\frac{e B_0}{m_{yy}^*} k_y$$
$$\\hbar \\frac{dk_y}{dt} = +e B_0 \\left(\\frac{\\hbar k_x}{m_{xx}^*}\\right) \\implies \\frac{dk_y}{dt} = +\\frac{e B_0}{m_{xx}^*} k_x$$
Differentiating the first equation with respect to $t$:
$$\\frac{d^2 k_x}{dt^2} = -\\frac{e B_0}{m_{yy}^*} \\frac{dk_y}{dt} = -\\frac{e^2 B_0^2}{m_{xx}^* m_{yy}^*} k_x$$
This is simple harmonic motion $\\frac{d^2 k_x}{dt^2} + \\omega_c^2 k_x = 0$ with cyclotron frequency:
$$\\omega_c = \\frac{e B_0}{\\sqrt{m_{xx}^* m_{yy}^*}}$$
Defining the cyclotron effective mass $m_c^* \\equiv \\frac{e B_0}{\\omega_c}$:
$$m_c^* = \\sqrt{m_{xx}^* m_{yy}^*} = \\frac{\\hbar^2}{2 a b \\sqrt{t_x t_y}}$$
This proves that the cyclotron mass in an anisotropic crystal is the geometric mean of the transverse effective mass components."""
        }
    ]
}

# =========================================================================
# UNIT 2: Semiconductor Physics, Impurity States & Two-Carrier Transport
# =========================================================================

u2_data = {
    "title": "Semiconductor Physics, Impurity States & Two-Carrier Transport",
    "subtitle": "Direct/Indirect Gaps, Hydrogenic Impurities, Fermi Level & Hall Effect",
    "summary": "This unit provides a rigorous quantum treatment of semiconductor band structures, carrier statistics, impurity states, and magnetotransport. We contrast direct and indirect optical bandgaps, derive the density of states near parabolic band edges, and prove the mass action law for intrinsic carriers. We calculate the ionization energies of shallow hydrogenic donor and acceptor states using dielectric screening and determine the temperature evolution of the chemical potential across freeze-out, exhaustion, and intrinsic regimes. Finally, we formulate the Boltzmann transport theory for electrical conductivity, derive the two-carrier Hall coefficient and magnetoresistance, and examine cyclotron resonance.",
    "sections": [
        {
            "id": "sec-2-1",
            "title": "Band Structure of Real Semiconductors: Direct vs Indirect Fundamental Bandgaps",
            "content": """
<h3>1. Direct vs Indirect Bandgaps in Momentum Space</h3>
<p>
The fundamental optical and electronic properties of semiconductors are determined by the relative alignment of the conduction band minimum (CBM) and the valence band maximum (VBM) in the first Brillouin zone:
</p>
<ul>
  <li><strong>Direct Bandgap Semiconductors (e.g. GaAs, InP, InAs, GaN):</strong> The conduction band minimum and valence band maximum occur at the <em>exact same crystal wavevector</em>, typically at the zone center ($\Gamma$-point, $\vec{k} = 0$).
  $$\\vec{k}_{\\text{CBM}} = \\vec{k}_{\\text{VBM}} = 0$$
  An incoming photon carrying energy $E_{\\text{ph}} = h\\nu \\ge E_g$ possesses negligible momentum ($q_{\\text{ph}} = 2\\pi/\\lambda \\sim 10^7\\text{ m}^{-1} \\ll \\pi/a \\sim 10^{10}\\text{ m}^{-1}$). Because momentum is conserved directly, vertical optical transitions occur readily:
  $$E_c(\\vec{k}) - E_v(\\vec{k}) = h\\nu$$
  The optical absorption coefficient rises sharply as $\\alpha(h\\nu) \\propto (h\\nu - E_g)^{1/2}$, enabling efficient radiative recombination for solid-state lasers and LEDs.</li>
  <li><strong>Indirect Bandgap Semiconductors (e.g. Si, Ge, AlAs, GaP):</strong> The valence band maximum occurs at the $\Gamma$-point, but the conduction band minima lie along high-symmetry axes away from $\vec{k} = 0$ (e.g. along the six equivalent $\\Delta = [100]$ directions at $k \\approx 0.85 \\frac{2\\pi}{a}$ in silicon, or at the four $L = [111]$ zone boundaries in germanium).
  $$\\vec{k}_{\\text{CBM}} \\ne \\vec{k}_{\\text{VBM}}$$
  An optical transition across the fundamental gap requires a change in electron crystal momentum $\\Delta\\vec{k} = \\vec{k}_{\\text{CBM}} - \\vec{k}_{\\text{VBM}}$. Because photons cannot provide this momentum, the transition must be mediated by the simultaneous emission or absorption of a lattice phonon with wavevector $\\vec{q} \\approx \\Delta\\vec{k}$ and energy $\\hbar\\Omega_{\\vec{q}}$:
  $$h\\nu = E_g \\pm \\hbar\\Omega_{\\vec{q}}$$
  This second-order quantum perturbation process produces a much weaker absorption coefficient $\\alpha(h\\nu) \\propto (h\\nu - E_g \\mp \\hbar\\Omega_{\\vec{q}})^2$, making silicon inefficient for light emission but excellent for photovoltaics due to long carrier lifetimes.</li>
</ul>
"""
        },
        {
            "id": "sec-2-2",
            "title": "Conduction & Valence Band Density of States and the Mass Action Law",
            "content": """
<h3>1. Parabolic Band Edge Approximations</h3>
<p>
Near the band edges, the dispersion relations can be approximated quadratically:
</p>
$$E_c(\\vec{k}) = E_c + \\frac{\\hbar^2 k^2}{2 m_e^*}, \\quad E_v(\\vec{k}) = E_v - \\frac{\\hbar^2 k^2}{2 m_h^*}$$
<p>
The 3D density of states per unit volume for electrons in the conduction band is:
</p>
$$g_c(E) = \\frac{1}{2\\pi^2} \\left( \\frac{2m_e^*}{\\hbar^2} \\right)^{3/2} \\sqrt{E - E_c}, \\quad E \\ge E_c$$
<p>
Similarly, for holes in the valence band:
</p>
$$g_v(E) = \\frac{1}{2\\pi^2} \\left( \\frac{2m_h^*}{\\hbar^2} \\right)^{3/2} \\sqrt{E_v - E}, \\quad E \\le E_v$$

<h3>2. Carrier Concentrations & The Mass Action Law</h3>
<p>
In non-degenerate semiconductors where the Fermi level lies inside the band gap at least $3k_B T$ away from both band edges ($E_c - E_F \\gg k_B T$ and $E_F - E_v \\gg k_B T$), the Fermi-Dirac distribution reduces to the classical Maxwell-Boltzmann tail:
</p>
$$f(E) = \\frac{1}{e^{(E - E_F)/k_B T} + 1} \\approx e^{-(E - E_F)/k_B T}$$
<p>
The total electron density in the conduction band is obtained by integrating $n_0 = \\int_{E_c}^\\infty g_c(E) f(E) dE$:
</p>
$$n_0 = N_c \\exp\\left( -\\frac{E_c - E_F}{k_B T} \\right)$$
<p>
where $N_c$ is the <strong>effective density of states of the conduction band</strong>:
</p>
$$N_c = 2 \\left( \\frac{2\\pi m_e^* k_B T}{h^2} \\right)^{3/2}$$
<p>
Similarly, the hole density in the valence band is $p_0 = \\int_{-\\infty}^{E_v} g_v(E) [1 - f(E)] dE$:
</p>
$$p_0 = N_v \\exp\\left( -\\frac{E_F - E_v}{k_B T} \\right), \\quad N_v = 2 \\left( \\frac{2\\pi m_h^* k_B T}{h^2} \\right)^{3/2}$$
<p>
Multiplying $n_0$ and $p_0$ eliminates the Fermi energy $E_F$, yielding the fundamental <strong>Mass Action Law</strong>:
</p>
$$n_0 p_0 = N_c N_v \\exp\\left( -\\frac{E_c - E_v}{k_B T} \\right) = N_c N_v \\exp\\left( -\\frac{E_g}{k_B T} \\right) \\equiv n_i^2$$
<p>
Crucially, the product $n_0 p_0 = n_i^2$ is an invariant constant at a given temperature, regardless of donor or acceptor doping!
</p>
"""
        },
        {
            "id": "sec-2-3",
            "title": "Intrinsic Carrier Concentrations and the Intrinsic Fermi Level Position $E_{Fi}(T)$",
            "content": """
<h3>1. Intrinsic Carrier Concentration</h3>
<p>
In an ultra-pure (intrinsic) semiconductor, thermal excitation across the gap creates equal numbers of electrons in the conduction band and holes in the valence band:
</p>
$$n_0 = p_0 = n_i$$
<p>
Using the mass action law $n_i^2 = N_c N_v e^{-E_g/k_B T}$:
</p>
$$n_i(T) = \\sqrt{N_c N_v} \\exp\\left( -\\frac{E_g}{2 k_B T} \\right) = 2 \\left( \\frac{2\\pi k_B T}{h^2} \\right)^{3/2} (m_e^* m_h^*)^{3/4} \\exp\\left( -\\frac{E_g}{2 k_B T} \\right)$$
<p>
For silicon at $T = 300\\text{ K}$, with $E_g = 1.12\\text{ eV}$, $n_i \\approx 1.0 \\times 10^{10}\\text{ cm}^{-3}$, compared to an atomic density of $5 \\times 10^{22}\\text{ cm}^{-3}$.
</p>

<h3>2. The Intrinsic Fermi Level Position</h3>
<p>
Equating $n_0 = p_0$:
</p>
$$N_c \\exp\\left( -\\frac{E_c - E_{Fi}}{k_B T} \\right) = N_v \\exp\\left( -\\frac{E_{Fi} - E_v}{k_B T} \\right)$$
<p>
Taking the natural logarithm and solving for $E_{Fi}$:
</p>
$$-\\frac{E_c - E_{Fi}}{k_B T} = \\ln\\left(\\frac{N_v}{N_c}\\right) - \\frac{E_{Fi} - E_v}{k_B T}$$
$$2 E_{Fi} = E_c + E_v + k_B T \\ln\\left( \\frac{N_v}{N_c} \\right)$$
<p>
Substituting $N_v / N_c = (m_h^* / m_e^*)^{3/2}$:
</p>
$$E_{Fi}(T) = \\frac{E_c + E_v}{2} + \\frac{3}{4} k_B T \\ln\\left( \\frac{m_h^*}{m_e^*} \\right)$$
<p>
At $T = 0\\text{ K}$, the intrinsic Fermi level lies exactly at mid-gap: $E_{Fi} = (E_c + E_v)/2 = E_g/2$. As temperature rises, if $m_h^* > m_e^*$ (as in most semiconductors), $E_{Fi}$ shifts slightly upward toward the conduction band to maintain charge neutrality against the higher density of valence states.
</p>
"""
        },
        {
            "id": "sec-2-4",
            "title": "Shallow Hydrogenic Impurity States: Donor and Acceptor Ionization Energies & Bohr Radii",
            "content": """
<h3>1. The Hydrogenic Donor Impurity Model</h3>
<p>
Consider a group-V donor atom (e.g. Phosphorus or Arsenic) substituting for a host group-IV silicon atom in the crystal lattice. Four of its valence electrons participate in tetrahedral $sp^3$ covalent bonds with neighboring Si atoms. The fifth electron is attracted to the surplus positive nuclear charge $+e$ of the donor ion core.
</p>
<p>
Because the electron orbits at distances spanning many unit cells, the Coulomb potential is heavily screened by the static relative permittivity of the semiconductor crystal ($\\epsilon_r \\approx 11.7$ for Si, $13.1$ for GaAs), and the electron moves with effective mass $m_e^*$:
</p>
$$V(r) = -\\frac{e^2}{4\\pi \\epsilon_r \\epsilon_0 r}$$
<p>
This forms an effective hydrogen-like atom inside a dielectric medium. The effective Bohr radius of the donor ground state is:
</p>
$$a_d^* = a_0 \\left( \\frac{\\epsilon_r}{m_e^* / m_0} \\right)$$
<p>
where $a_0 = 0.529\\text{ \\AA}$ is the atomic Bohr radius. For silicon ($m_e^* \\approx 0.26 m_0$, $\\epsilon_r = 11.7$):
</p>
$$a_d^* \\approx 0.529 \\times \\frac{11.7}{0.26} \\approx 24\\text{ \\AA} = 2.4\\text{ nm}$$
<p>
This vast orbit encloses thousands of host lattice atoms, justifying the continuum dielectric approximation.
</p>

<h3>2. Donor and Acceptor Ionization Energies</h3>
<p>
The ionization energy required to promote the bound donor electron into the conduction band is:
</p>
$$E_d = E_H \\left( \\frac{m_e^* / m_0}{\\epsilon_r^2} \\right)$$
<p>
where $E_H = 13.6\\text{ eV}$ is the Rydberg ionization energy of atomic hydrogen. For silicon:
</p>
$$E_d \\approx 13.6 \\times \\frac{0.26}{(11.7)^2} \\approx 0.026\\text{ eV} = 26\\text{ meV}$$
<p>
Because $E_d \\sim k_B T_{\\text{room}} \\approx 26\\text{ meV}$, shallow donor levels lie just beneath the conduction band edge ($E_c - E_d$) and are nearly 100% ionized at room temperature!
</p>
<p>
Similarly, a group-III acceptor atom (e.g. Boron in Si) lacks one bonding electron, introducing a localized hole bound to a negative core with acceptor binding energy:
</p>
$$E_a = E_H \\left( \\frac{m_h^* / m_0}{\\epsilon_r^2} \\right) \\sim 45\\text{ meV}$$
"""
        },
        {
            "id": "sec-2-5",
            "title": "Temperature Regimes of Carrier Concentration: Freeze-Out, Extrinsic Exhaustion & Intrinsic",
            "content": """
<h3>1. Charge Neutrality & Fermi Level Evolution</h3>
<p>
In an $n$-type semiconductor with donor concentration $N_d$ and negligible acceptors ($N_a = 0$), overall charge neutrality demands:
</p>
$$n_0 = p_0 + N_d^+$$
<p>
where $N_d^+$ is the concentration of ionized donors given by Fermi statistics (including the factor of 2 for spin degeneracy of the donor ground state):
</p>
$$N_d^+ = \\frac{N_d}{1 + 2 \\exp\\left(\\frac{E_F - E_d}{k_B T}\\right)}$$

<h3>2. The Three Distinct Temperature Regimes</h3>
<ul>
  <li><strong>1. Freeze-Out (Cryogenic) Regime ($T \\to 0\\text{ K}$, $k_B T \\ll E_d$):</strong>
  Thermal energy is insufficient to ionize the donors. Most electrons remain bound to donor atoms ($N_d^+ \\ll N_d$), and valence band hole generation is completely negligible ($p_0 \\approx 0$).
  $$n_0 \\approx N_d^+ \\approx \\sqrt{\\frac{N_c N_d}{2}} \\exp\\left( -\\frac{E_c - E_d}{2 k_B T} \\right)$$
  The Fermi level lies midway between the donor level and the conduction band:
  $$E_F(T) \\approx \\frac{E_c + E_d}{2} + \\frac{k_B T}{2} \\ln\\left( \\frac{N_d}{2 N_c} \\right)$$
  In this regime, carrier concentration rises exponentially with slope $-E_d / (2 k_B)$ on an Arrhenius plot $\\ln n$ vs $1/T$.</li>

  <li><strong>2. Extrinsic / Exhaustion Regime (Room Temperature, $E_d \\ll k_B T \\ll E_g$):</strong>
  Virtually all donor atoms are completely ionized ($N_d^+ \\approx N_d$), while thermal excitation across the band gap remains negligible ($n_i \\ll N_d$).
  $$n_0 \\approx N_d = \\text{constant}$$
  The carrier concentration is flat and independent of temperature. The Fermi level drops continuously as $T$ increases:
  $$E_F(T) = E_c - k_B T \\ln\\left( \\frac{N_c(T)}{N_d} \\right)$$
  This is the standard operational regime for semiconductor devices.</li>

  <li><strong>3. Intrinsic Regime (High Temperatures, $k_B T \\sim E_g$):</strong>
  Band-to-band thermal generation overwhelms the donor concentration ($n_i(T) \\gg N_d$):
  $$n_0 \\approx p_0 \\approx n_i(T) \\propto T^{3/2} \\exp\\left( -\\frac{E_g}{2 k_B T} \\right)$$
  The Fermi level converges to the intrinsic level $E_{Fi} \\approx E_g / 2$. Doping no longer controls the electrical behavior, causing semiconductor device failure.</li>
</ul>
""",
            "simulation": "ssp2-semiconductor-fermi-sim",
            "simulations": ["ssp2-semiconductor-fermi-sim"]
        },
        {
            "id": "sec-2-6",
            "title": "Electrical Conductivity, Drift Mobility & Single-Carrier Hall Effect Formalism",
            "content": """
<h3>1. Semiclassical Drift Conductivity & Mobility</h3>
<p>
In the presence of an electric field $\\vec{\\mathcal{E}}$, carrier momentum relaxes via collisions with acoustic phonons, optical phonons, and ionized impurities with relaxation time $\\tau$. The drift velocity is:
</p>
$$\\vec{v}_d = -\\mu_e \\vec{\\mathcal{E}} = -\\frac{e \\tau_e}{m_e^*} \\vec{\\mathcal{E}}, \\quad \\vec{v}_{dh} = +\\mu_h \\vec{\\mathcal{E}} = +\\frac{e \\tau_h}{m_h^*} \\vec{\\mathcal{E}}$$
<p>
where $\\mu_e$ and $\\mu_h$ are the electron and hole drift mobilities. The total conduction current density is the sum of electron and hole currents:
</p>
$$\\vec{J} = \\vec{J}_e + \\vec{J}_h = (-e n \\vec{v}_d) + (+e p \\vec{v}_{dh}) = e (n \\mu_e + p \\mu_h) \\vec{\\mathcal{E}}$$
<p>
The electrical conductivity of the semiconductor is therefore:
</p>
$$\\sigma = e (n \\mu_e + p \\mu_h)$$

<h3>2. Single-Carrier Hall Effect Formalism</h3>
<p>
Apply a longitudinal electric field $\\mathcal{E}_x$ driving current density $J_x$, and a transverse magnetic field $\\vec{B} = B_z \\hat{z}$. The Lorentz force deflects mobile charges sideways along $y$:
</p>
$$\\vec{F} = q (\\vec{\\mathcal{E}} + \\vec{v} \\times \\vec{B})$$
<p>
In the steady state, charges accumulate on the lateral boundaries, generating a transverse <strong>Hall electric field</strong> $\\mathcal{E}_y$ that exactly cancels the Lorentz deflection, enforcing zero net transverse current $J_y = 0$:
</p>
$$J_y = \\sigma_0 \\mathcal{E}_y - \\mu B_z J_x = 0 \\implies \\mathcal{E}_y = \\frac{1}{q n} J_x B_z$$
<p>
We define the <strong>Hall coefficient</strong> $R_H$:
</p>
$$R_H \\equiv \\frac{\\mathcal{E}_y}{J_x B_z} = \\frac{1}{q n}$$
<ul>
  <li>For an $n$-type semiconductor ($q = -e$):
  $$R_H = -\\frac{1}{e n} < 0$$</li>
  <li>For a $p$-type semiconductor ($q = +e$):
  $$R_H = +\\frac{1}{e p} > 0$$</li>
</ul>
<p>
The sign of $R_H$ unambiguously reveals the majority carrier type, and its magnitude provides a direct experimental measurement of the carrier concentration. The <strong>Hall mobility</strong> is defined as:
</p>
$$\\mu_H \\equiv |R_H| \\sigma$$
"""
        },
        {
            "id": "sec-2-7",
            "title": "Two-Carrier Hall Effect, Mixed Conduction & Cyclotron Resonance in Semiconductors",
            "content": """
<h3>1. Derivation of the Two-Carrier Hall Coefficient</h3>
<p>
In intrinsic or compensated semiconductors where both electrons ($n, \\mu_e$) and holes ($p, \\mu_h$) contribute simultaneously to transport, each carrier species experiences opposing Hall deflections.
</p>
<p>
From the Boltzmann transport equation in the low-field limit ($\\mu B \\ll 1$), the current densities in the $x$-$y$ plane are:
</p>
$$J_x = e (n \\mu_e + p \\mu_h) \\mathcal{E}_x + e (n \\mu_e^2 - p \\mu_h^2) B_z \\mathcal{E}_y$$
$$J_y = e (n \\mu_e + p \\mu_h) \\mathcal{E}_y - e (n \\mu_e^2 - p \\mu_h^2) B_z \\mathcal{E}_x$$
<p>
Imposing the open-circuit condition $J_y = 0$, we solve for the Hall field $\\mathcal{E}_y$:
</p>
$$\\mathcal{E}_y = \\frac{p \\mu_h^2 - n \\mu_e^2}{n \\mu_e + p \\mu_h} B_z \\mathcal{E}_x$$
<p>
Substituting $J_x \\approx e (n \\mu_e + p \\mu_h) \\mathcal{E}_x$, the <strong>two-carrier Hall coefficient</strong> is:
</p>
$$R_H = \\frac{\\mathcal{E}_y}{J_x B_z} = \\frac{1}{e} \\frac{p \\mu_h^2 - n \\mu_e^2}{(p \\mu_h + n \\mu_e)^2}$$
<p>
Remarkably:
</p>
<ul>
  <li>Even in a $p$-type material where $p > n$, the Hall coefficient can be <strong>negative</strong> ($R_H < 0$) if the electron mobility is sufficiently higher than the hole mobility ($n \\mu_e^2 > p \\mu_h^2$).</li>
  <li>The Hall coefficient vanishes ($R_H = 0$) exactly when:
  $$p \\mu_h^2 = n \\mu_e^2 \\implies \\frac{p}{n} = \\left( \\frac{\\mu_e}{\\mu_h} \\right)^2$$
  Since in silicon $\\mu_e / \\mu_h \\approx 1400 / 450 \\approx 3.1$, $R_H$ crosses zero when $p \\approx 9.6 n$.</li>
</ul>

<h3>2. Cyclotron Resonance in Semiconductors</h3>
<p>
Cyclotron resonance provides the most precise direct technique for determining the effective mass tensor. A semiconductor sample is placed in a microwave cavity at cryogenic temperatures ($4.2\\text{ K}$ to avoid thermal broadening $\\omega_c \\tau \\gg 1$) with a static magnetic field $\\vec{B}$.
</p>
<p>
When the microwave frequency $\\omega$ matches the cyclotron frequency $\\omega_c = e B / m^*$, resonant absorption of microwave power occurs:
</p>
$$P(\\omega) \\propto \\frac{1}{1 + (\\omega - \\omega_c)^2 \\tau^2}$$
<p>
In silicon, rotation of $\\vec{B}$ relative to crystal axes splits the absorption peak into multiple lines, directly revealing the multi-valley spheroidal conduction band ellipsoids with longitudinal mass $m_l^* = 0.98 m_0$ and transverse mass $m_t^* = 0.19 m_0$.
</p>
""",
            "simulation": "ssp2-two-carrier-hall-sim",
            "simulations": ["ssp2-two-carrier-hall-sim"]
        }
    ],
    "problems": [
        {
            "id": "ssp2-prob-2-1",
            "title": "Intrinsic Carrier Concentration & Temperature Drift of the Fermi Level in Silicon",
            "statement": "Silicon has a fundamental bandgap $E_g(0) = 1.17\\text{ eV}$ with effective masses $m_e^* = 1.08 m_0$ and $m_h^* = 0.56 m_0$, where $m_0 = 9.109 \\times 10^{-31}\\text{ kg}$.\\n\\n(a) Calculate the effective densities of states $N_c$ and $N_v$ at $T = 300\\text{ K}$.\\n(b) Using $E_g(300\\text{ K}) = 1.12\\text{ eV}$, compute the intrinsic carrier concentration $n_i$ at $300\\text{ K}$.\\n(c) Calculate the exact energy displacement of the intrinsic Fermi level $E_{Fi}$ from the geometric mid-gap $(E_c + E_v)/2$ at $T = 300\\text{ K}$ in meV, and explain its physical origin.",
            "solution": """**(a) Effective Densities of States $N_c$ and $N_v$ at $300\\text{ K}$:**
The effective density of states formula is:
$$N_{c,v} = 2 \\left( \\frac{2\\pi m_{e,h}^* k_B T}{h^2} \\right)^{3/2}$$
For a free electron mass $m_0$ at $300\\text{ K}$:
$$2 \\left( \\frac{2\\pi m_0 k_B (300)}{h^2} \\right)^{3/2} \\approx 2.509 \\times 10^{25}\\text{ m}^{-3} = 2.509 \\times 10^{19}\\text{ cm}^{-3}$$
Therefore:
$$N_c = 2.509 \\times 10^{19} \\times (1.08)^{3/2} = 2.509 \\times 10^{19} \\times 1.122 \\approx 2.815 \\times 10^{19}\\text{ cm}^{-3}$$
$$N_v = 2.509 \\times 10^{19} \\times (0.56)^{3/2} = 2.509 \\times 10^{19} \\times 0.419 \\approx 1.051 \\times 10^{19}\\text{ cm}^{-3}$$

**(b) Intrinsic Carrier Concentration $n_i$ at $300\\text{ K}$:**
With $k_B T = 0.02585\\text{ eV}$ at $300\\text{ K}$:
$$\\frac{E_g}{2 k_B T} = \\frac{1.12}{2 \\times 0.02585} = \\frac{1.12}{0.0517} \\approx 21.663$$
$$n_i = \\sqrt{N_c N_v} \\exp\\left( -\\frac{E_g}{2 k_B T} \\right)$$
$$\\sqrt{N_c N_v} = \\sqrt{(2.815 \\times 10^{19})(1.051 \\times 10^{19})} = \\sqrt{2.959 \\times 10^{38}} \\approx 1.720 \\times 10^{19}\\text{ cm}^{-3}$$
$$n_i = 1.720 \\times 10^{19} \\times e^{-21.663} = 1.720 \\times 10^{19} \\times (3.908 \\times 10^{-10}) \\approx 6.72 \\times 10^{9}\\text{ cm}^{-3}$$
(Using the standard empirical experimental value including density of states temperature factors gives $n_i \\approx 1.0 \\times 10^{10}\\text{ cm}^{-3}$).

**(c) Intrinsic Fermi Level Shift:**
The displacement from midgap is:
$$\\Delta E = E_{Fi} - \\frac{E_c + E_v}{2} = \\frac{3}{4} k_B T \\ln\\left( \\frac{m_h^*}{m_e^*} \\right)$$
$$\\frac{m_h^*}{m_e^*} = \\frac{0.56}{1.08} \\approx 0.5185$$
$$\\ln(0.5185) \\approx -0.6568$$
$$\\Delta E = 0.75 \\times (25.85\\text{ meV}) \\times (-0.6568) \\approx -12.73\\text{ meV}$$
The intrinsic Fermi level is displaced **$12.7\\text{ meV}$ below mid-gap** (closer to the valence band).
Physical origin: Because $m_e^* > m_h^*$, the conduction band has a higher density of states ($N_c > N_v$). To equalize the thermal carrier densities $n = p$, the Fermi level must shift downward closer to the valence band, so the smaller valence density of states is compensated by a slightly higher Boltzmann occupancy factor $e^{-(E_F - E_v)/k_B T}$."""
        },
        {
            "id": "ssp2-prob-2-2",
            "title": "Hydrogenic Donor Freeze-Out & Exhaustion Threshold in Phosphorus-Doped Silicon",
            "statement": "A silicon crystal is uniformly doped with phosphorus donors at a concentration $N_d = 2.0 \\times 10^{16}\\text{ cm}^{-3}$. The relative dielectric constant is $\\epsilon_r = 11.7$ and $m_e^* = 0.26 m_0$.\\n\\n(a) Compute the effective Bohr radius $a_d^*$ and the donor ionization energy $E_d = E_c - E_D$.\\n(b) At what cryogenic temperature $T$ are 50% of the donor atoms ionized ($N_d^+ / N_d = 0.5$)?\\n(c) Determine the temperature $T_{\\text{exh}}$ marking the onset of the exhaustion regime where 99% of donors are ionized.",
            "solution": """**(a) Effective Bohr Radius and Donor Ionization Energy:**
$$a_d^* = a_0 \\frac{\\epsilon_r}{m_e^* / m_0} = 0.529\\text{ \\AA} \\times \\frac{11.7}{0.26} = 0.529 \\times 45.0 \\approx 23.8\\text{ \\AA} = 2.38\\text{ nm}$$
The donor binding energy is:
$$E_d = 13.6\\text{ eV} \\times \\frac{m_e^*/m_0}{\\epsilon_r^2} = 13.6 \\times \\frac{0.26}{(11.7)^2} = 13.6 \\times \\frac{0.26}{136.89} \\approx 0.0258\\text{ eV} = 25.8\\text{ meV}$$

**(b) Temperature for 50% Donor Ionization:**
When 50% are ionized, $N_d^+ = n = N_d/2 = 1.0 \\times 10^{16}\\text{ cm}^{-3}$.
In the freeze-out regime where $N_a = 0$:
$$n = \\sqrt{\\frac{N_c N_d}{2}} \\exp\\left( -\\frac{E_d}{2 k_B T} \\right)$$
Equating $n = N_d / 2$:
$$\\frac{N_d}{2} = \\sqrt{\\frac{N_c N_d}{2}} e^{-E_d / 2k_B T} \\implies \\frac{N_d}{2} = N_c e^{-E_d / k_B T}$$
Expressing $N_c(T) = N_{c0} (T/300)^{3/2}$ with $N_{c0} = 2.8 \\times 10^{19}\\text{ cm}^{-3}$:
$$e^{E_d / k_B T} = \\frac{2 N_c(T)}{N_d} = \\frac{2 \\times 2.8 \\times 10^{19}}{2.0 \\times 10^{16}} \\left(\\frac{T}{300}\\right)^{3/2} = 2800 \\left(\\frac{T}{300}\\right)^{3/2}$$
Taking natural log:
$$\\frac{E_d}{k_B T} = \\ln\\left( 2800 \\left(\\frac{T}{300}\\right)^{3/2} \\right)$$
Iterating numerically:
Guess $T = 35\\text{ K}$:
$$\\frac{T}{300} = 0.1167 \\implies (0.1167)^{1.5} \\approx 0.0398$$
$$2800 \\times 0.0398 \\approx 111.6 \\implies \\ln(111.6) \\approx 4.715$$
$$T = \\frac{E_d}{k_B \\times 4.715} = \\frac{25.8\\text{ meV}}{0.08617\\text{ meV/K} \\times 4.715} = \\frac{25.8}{0.4063} \\approx 63.5\\text{ K}$$
Second iteration at $T = 55\\text{ K}$:
$$(55/300)^{1.5} = (0.1833)^{1.5} \\approx 0.0785$$
$$2800 \\times 0.0785 \\approx 219.8 \\implies \\ln(219.8) \\approx 5.39$$
$$T = \\frac{25.8}{0.08617 \\times 5.39} \\approx 55.5\\text{ K}$$
Thus, 50% ionization occurs at **$T \\approx 55.5\\text{ K}$**.

**(c) Onset of Exhaustion Regime (99% Ionization):**
At 99% ionization, $N_d^+ / N_d = 0.99$, so $n \\approx N_d$.
The fraction of neutral donors is $1 - N_d^+/N_d = 0.01$.
From the donor ionization formula:
$$\\frac{N_d - N_d^+}{N_d} = \\frac{1}{1 + \\frac{1}{2} e^{(E_d - E_F)/k_B T}} = 0.01 \\implies \\frac{1}{2} e^{(E_d - E_F)/k_B T} \\approx 100$$
Using $n = N_c e^{-(E_c - E_F)/k_B T} = N_d \\implies e^{(E_c - E_F)/k_B T} = N_c / N_d$:
$$\\frac{N_c}{N_d} e^{-E_d / k_B T} \\approx 50$$
$$e^{E_d / k_B T} = \\frac{N_c(T)}{50 N_d} = \\frac{2.8 \\times 10^{19}}{50 \\times 2.0 \\times 10^{16}} \\left(\\frac{T}{300}\\right)^{3/2} = 28 \\left(\\frac{T}{300}\\right)^{3/2}$$
Solving iteratively gives **$T_{\\text{exh}} \\approx 125\\text{ K}$**.
Above $\\sim 125\\text{ K}$, all donors are exhausted and the carrier concentration remains constant at $n = N_d$ up to $\\sim 450\\text{ K}$ when intrinsic thermal generation begins."""
        },
        {
            "id": "ssp2-prob-2-3",
            "title": "Two-Carrier Hall Coefficient Zero-Crossing & Magnetoresistance Inversion",
            "statement": "An intrinsic semiconductor sample has electron mobility $\\mu_e = 3800\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$ and hole mobility $\\mu_h = 1200\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$.\\n\\n(a) Calculate the ratio of hole to electron concentrations $p/n$ at which the low-field Hall coefficient $R_H$ exactly vanishes ($R_H = 0$).\\n(b) If the sample is moderately $p$-doped such that $p = 5n$, calculate the sign and value of the Hall coefficient relative to the single-carrier hole value $R_{H0} = +1/(e p)$.\\n(c) Derive the longitudinal magnetoresistance ratio $\\Delta\\rho / \\rho_0$ in terms of $\\mu_e, \\mu_h, n, p$, and explain why single-carrier isotropic semiconductors exhibit zero orbital magnetoresistance while two-carrier systems exhibit positive magnetoresistance.",
            "solution": """**(a) Zero-Crossing Condition for Hall Coefficient:**
The low-field two-carrier Hall coefficient is:
$$R_H = \\frac{1}{e} \\frac{p \\mu_h^2 - n \\mu_e^2}{(p \\mu_h + n \\mu_e)^2}$$
For $R_H = 0$:
$$p \\mu_h^2 - n \\mu_e^2 = 0 \\implies \\frac{p}{n} = \\left( \\frac{\\mu_e}{\\mu_h} \\right)^2$$
Given $\\mu_e = 3800$ and $\\mu_h = 1200$:
$$\\frac{\\mu_e}{\\mu_h} = \\frac{3800}{1200} = \\frac{19}{6} \\approx 3.167$$
$$\\frac{p}{n} = (3.167)^2 \\approx 10.03$$
The hole concentration must exceed the electron concentration by a factor of **$10.03$** to nullify the Hall voltage!

**(b) Hall Coefficient for $p = 5n$:**
Here $p/n = 5 < 10.03$.
Substitute $p = 5n$ into $R_H$:
$$p \\mu_h^2 - n \\mu_e^2 = n [5(1200)^2 - (3800)^2] = n [5(1.44 \\times 10^6) - 14.44 \\times 10^6] = n [7.2 - 14.44] \\times 10^6 = -7.24 \\times 10^6 n$$
$$p \\mu_h + n \\mu_e = n [5(1200) + 3800] = n [6000 + 3800] = 9800 n$$
$$(p \\mu_h + n \\mu_e)^2 = (9800 n)^2 = 9.604 \\times 10^7 n^2$$
$$R_H = \\frac{1}{e} \\frac{-7.24 \\times 10^6 n}{9.604 \\times 10^7 n^2} = -\\frac{0.0754}{e n}$$
Comparing with $R_{H0} = +\\frac{1}{e p} = +\\frac{1}{5 e n} = +\\frac{0.20}{e n}$:
$$\\frac{R_H}{R_{H0}} = \\frac{-0.0754}{0.20} \\approx -0.377$$
Even though there are **5 times more holes than electrons**, the Hall coefficient is **NEGATIVE** ($R_H < 0$) and equals $-37.7\\%$ of the naive hole value! This occurs because electrons are more than 3 times faster and the Hall deflection scales as mobility squared ($\\mu^2$).

**(c) Two-Carrier Longitudinal Magnetoresistance:**
In a single-carrier system with energy-independent relaxation time $\\tau$, the Hall electric field $\\mathcal{E}_y = -\\mu B_z \\mathcal{E}_x$ perfectly balances the Lorentz force for every electron, leaving current flow along $x$ completely unhindered ($\\Delta\\rho / \\rho_0 = 0$).
In a two-carrier system, the single Hall field $\\mathcal{E}_y$ cannot simultaneously balance the Lorentz forces on both electrons and holes because they drift with different speeds ($v_{de} \\ne v_{dh}$).
From the conductivity tensor inversion:
$$\\frac{\\Delta\\rho}{\\rho_0} = \\frac{\\rho(B) - \\rho(0)}{\\rho(0)} = \\frac{n p \\mu_e \\mu_h (\\mu_e + \\mu_h)^2 B^2}{(n \\mu_e + p \\mu_h)^2 + (p - n)^2 \\mu_e^2 \\mu_h^2 B^2}$$
In the low-field limit ($B \\to 0$):
$$\\frac{\\Delta\\rho}{\\rho_0} \\approx \\frac{n p \\mu_e \\mu_h (\\mu_e + \\mu_h)^2}{(n \\mu_e + p \\mu_h)^2} B^2 > 0$$
This proves that two-carrier semiconductors always exhibit **strictly positive transverse magnetoresistance** quadratic in magnetic field ($B^2$), arising from the uncompensated Lorentz deflection of the unequal carriers."""
        }
    ]
}

with open("ssp2_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1_data, f, indent=2)

with open("ssp2_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2_data, f, indent=2)

print("Generated ssp2_u1.json and ssp2_u2.json successfully.")
