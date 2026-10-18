# -*- coding: utf-8 -*-
"""
Builder for Nuclear Physics II Units 7 & 8
Unit 7: Elementary Particles I: Fundamental Interactions, Symmetries & Quark Model
Unit 8: Elementary Particles II: Hadron Spectroscopy, SU(3) Flavor & Electroweak Unification
"""
import json

u7_data = {
    "title": "Elementary Particles I: Fundamental Interactions, Symmetries & Quark Model",
    "subtitle": "Forces, Quantum Numbers, Deep Inelastic Scattering, Discrete Symmetries & CP Violation",
    "summary": "Systematic survey of the subatomic particle realm: classification of the four fundamental interactions (gravitational, weak, electromagnetic, strong), mediation by spin-1 gauge bosons (γ, W±, Z0, gluons), quantum conservation laws (baryon number, lepton flavor numbers, strangeness, isospin, and hypercharge), Deep Inelastic Scattering (DIS) establishing quarks as point-like fractionally charged partons, asymptotic freedom and Cornell confinement potential, discrete spacetime symmetries (Parity P, Charge Conjugation C, Time Reversal T), historical discovery of parity non-conservation in 60Co beta decay, and neutral kaon oscillations revealing subtle CP violation and the Sakharov conditions for cosmological baryogenesis.",
    "sections": [
        {
            "id": "sec-7-1",
            "title": "The Four Fundamental Interactions & Gauge Mediators",
            "content": r"""
<h3>1. Classification of Fundamental Physical Forces</h3>
<p>
Modern fundamental physics recognizes four distinct interactions through which all matter in the universe influences and transforms itself. In quantum field theory, each interaction is mediated by the virtual exchange of vector (spin-1) or tensor (spin-2) gauge bosons:
</p>
<table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;">
<thead>
<tr style="border-bottom:2px solid var(--border-color); text-align:left;">
<th style="padding:8px;">Interaction</th>
<th style="padding:8px;">Mediator (Gauge Boson)</th>
<th style="padding:8px;">Spin / Parity $J^P$</th>
<th style="padding:8px;">Rest Mass</th>
<th style="padding:8px;">Relative Strength ($\sim 1\text{ fm}$)</th>
<th style="padding:8px;">Effective Range</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Strong (QCD)</strong></td>
<td style="padding:8px;">8 Gluons ($g$)</td>
<td style="padding:8px;">$1^-$</td>
<td style="padding:8px;">$0$</td>
<td style="padding:8px;">$\alpha_s \approx 1$</td>
<td style="padding:8px;">$\sim 10^{-15}\text{ m}$ (confinement)</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Electromagnetic (QED)</strong></td>
<td style="padding:8px;">Photon ($\gamma$)</td>
<td style="padding:8px;">$1^-$</td>
<td style="padding:8px;">$0$</td>
<td style="padding:8px;">$\alpha = \frac{e^2}{4\pi\varepsilon_0\hbar c} \approx \frac{1}{137}$</td>
<td style="padding:8px;">$\infty$ ($1/r^2$ Coulomb potential)</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;"><strong>Weak (Flavor)</strong></td>
<td style="padding:8px;">$W^+, W^-, Z^0$</td>
<td style="padding:8px;">$1^-$</td>
<td style="padding:8px;">$M_W = 80.4, M_Z = 91.2\text{ GeV}/c^2$</td>
<td style="padding:8px;">$\alpha_W \approx 10^{-5}\text{ to }10^{-6}$</td>
<td style="padding:8px;">$\frac{\hbar}{M_W c} \approx 2.5 \times 10^{-18}\text{ m}$</td>
</tr>
<tr>
<td style="padding:8px;"><strong>Gravitational</strong></td>
<td style="padding:8px;">Graviton ($G$, hypothetical)</td>
<td style="padding:8px;">$2^+$</td>
<td style="padding:8px;">$0$</td>
<td style="padding:8px;">$\alpha_G = \frac{G M_p^2}{\hbar c} \approx 6 \times 10^{-39}$</td>
<td style="padding:8px;">$\infty$ ($1/r^2$ Newtonian)</td>
</tr>
</tbody>
</table>

<h3>2. Characteristic Time Scales and Cross Sections</h3>
<p>
The vast disparity in coupling constants directly dictates the lifetimes of decaying particles and reaction cross sections:
</p>
<ul>
<li><strong>Strong Decays:</strong> Mediated in characteristic nuclear transit times:
$$\tau_{\text{strong}} \sim \frac{R_{\text{nuc}}}{c} \approx \frac{1.4\text{ fm}}{3 \times 10^{23}\text{ fm/s}} \approx 10^{-23}\text{ s}, \qquad \sigma_{\text{strong}} \sim 10\text{ to }100\text{ mb}$$
Examples include hadron resonance decays such as $\Delta(1232) \to N + \pi$ and $\rho(770) \to \pi + \pi$.</li>
<li><strong>Electromagnetic Decays:</strong> Photon emission or pair creation:
$$\tau_{\text{EM}} \sim 10^{-16}\text{ to }10^{-20}\text{ s}, \qquad \sigma_{\text{EM}} \sim 1\text{ to }100\text{ }\mu\text{b}$$
Examples include neutral pion decay $\pi^0 \to \gamma + \gamma$ ($\tau = 8.5 \times 10^{-17}\text{ s}$) and nuclear gamma transitions.</li>
<li><strong>Weak Decays:</strong> Flavor-changing transitions mediated by massive $W^\pm$ or $Z^0$:
$$\tau_{\text{weak}} \sim 10^{-6}\text{ to }10^{-13}\text{ s}\text{ (or longer for beta decay)}, \qquad \sigma_{\text{weak}} \sim 10^{-38}\text{ to }10^{-44}\text{ cm}^2$$
Examples include free muon decay $\mu^- \to e^- + \bar{\nu}_e + \nu_\mu$ ($\tau = 2.2 \times 10^{-6}\text{ s}$), charged pion decay $\pi^+ \to \mu^+ + \nu_\mu$ ($\tau = 2.6 \times 10^{-8}\text{ s}$), and neutron beta decay $n \to p + e^- + \bar{\nu}_e$ ($\tau = 879\text{ s}$).</li>
</ul>
"""
        },
        {
            "id": "sec-7-2",
            "title": "Quantum Numbers, Conservation Laws & Gell-Mann-Nishijima Formula",
            "content": r"""
<h3>1. Additive and Multiplicative Quantum Numbers</h3>
<p>
Subatomic particle processes are strictly regulated by internal conservation laws originating from continuous gauge symmetries (via Noether's theorem) or discrete space-time and internal transformations:
</p>
<table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;">
<thead>
<tr style="border-bottom:2px solid var(--border-color); text-align:left;">
<th style="padding:8px;">Quantity</th>
<th style="padding:8px;">Strong</th>
<th style="padding:8px;">Electromagnetic</th>
<th style="padding:8px;">Weak</th>
<th style="padding:8px;">Associated Symmetry / Group</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Energy / Momentum $(E, \vec{p})$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td>
<td style="padding:8px;">Spacetime translations (Poincaré)</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Angular Momentum $\vec{J}$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td>
<td style="padding:8px;">Spatial rotations $SO(3)$</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Electric Charge $Q$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td>
<td style="padding:8px;">$U(1)_{\text{EM}}$ local gauge phase</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Baryon Number $B$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td>
<td style="padding:8px;">$U(1)_B$ global phase</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Lepton Numbers $L_e, L_\mu, L_\tau$</td>
<td style="padding:8px;">N/A</td><td style="padding:8px;">Yes</td><td style="padding:8px;">Conserved (except $\nu$-oscillations)</td>
<td style="padding:8px;">$U(1)_{L_i}$ global phases</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Total Isospin $I$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">No ($\Delta I = 0, \pm 1$)</td><td style="padding:8px;">No</td>
<td style="padding:8px;">$SU(2)_I$ flavor symmetry</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Isospin Component $I_3$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;">No ($\Delta I_3 = \pm 1/2$)</td>
<td style="padding:8px;">$U(1)_{I_3}$ subgroup of $SU(2)$</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Strangeness $S$ / Hypercharge $Y$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;">No ($\Delta S = 0, \pm 1$)</td>
<td style="padding:8px;">$U(1)_S$ flavor phase</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Parity $\mathcal{P}$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;"><strong>Violated maximally</strong></td>
<td style="padding:8px;">Spatial inversion $\vec{x} \to -\vec{x}$</td>
</tr>
<tr>
<td style="padding:8px;">Charge Conjugation $\mathcal{C}$</td>
<td style="padding:8px;">Yes</td><td style="padding:8px;">Yes</td><td style="padding:8px;"><strong>Violated maximally</strong></td>
<td style="padding:8px;">Particle $\leftrightarrow$ antiparticle swap</td>
</tr>
</tbody>
</table>

<h3>2. The Gell-Mann-Nishijima Formula</h3>
<p>
In the 1950s, Murray Gell-Mann and Kazuhiko Nishijima established an algebraic relation connecting electric charge $Q$ (in units of $e$), third component of isospin $I_3$, baryon number $B$, and strangeness $S$:
$$Q = I_3 + \frac{B + S}{2} = I_3 + \frac{Y}{2}$$
where the <strong>strong hypercharge</strong> $Y$ is defined as:
$$Y \equiv B + S + C + B' + T$$
incorporating charm $C$, bottomness $B'$, and topness $T$ for heavier quark generations.
</p>
<p>
For the nucleon doublet ($p, n$): $B = 1, S = 0 \implies Y = 1$:
$$Q_p = (+1/2) + \frac{1}{2} = +1, \qquad Q_n = (-1/2) + \frac{1}{2} = 0$$
For the strange lambda hyperon $\Lambda^0$: $I=0, I_3 = 0, B = 1, S = -1 \implies Y = 0$:
$$Q_\Lambda = 0 + \frac{0}{2} = 0$$
For the sigma triplet ($\Sigma^+, \Sigma^0, \Sigma^-$): $I=1, B = 1, S = -1 \implies Y = 0$:
$$Q_{\Sigma^+} = +1 + 0 = +1, \quad Q_{\Sigma^0} = 0, \quad Q_{\Sigma^-} = -1$$
</p>
"""
        },
        {
            "id": "sec-7-3",
            "title": "Deep Inelastic Scattering, Asymptotic Freedom & Quark Confinement",
            "content": r"""
<h3>1. Deep Inelastic Scattering (DIS) and the Parton Model</h3>
<p>
In the late 1960s at SLAC, high-energy electron-proton scattering experiments revealed that at colossal four-momentum transfer $Q^2 \equiv -q^2 > 1\text{ GeV}^2$, electrons scatter elastically off point-like, spin-$1/2$ constituents within the proton:
$$e^- + p \to e^- + X$$
Defining the four-momentum transfer $q^\mu = k^\mu - k'^\mu$ and proton target four-momentum $P^\mu$:
$$Q^2 \equiv -q^2 = 4 E E' \sin^2(\theta/2), \qquad \nu \equiv \frac{P \cdot q}{M_p} = E - E' \text{ (in lab frame)}$$
The dimensionless <strong>Bjorken scaling variable</strong> is:
$$x \equiv \frac{Q^2}{2 P \cdot q} = \frac{Q^2}{2 M_p \nu}, \qquad 0 < x \le 1$$
In Richard Feynman's <strong>infinite momentum frame</strong>, $x$ represents the fraction of the proton's total longitudinal four-momentum carried by the struck constituent ("parton").
</p>
<p>
In the deep inelastic limit ($Q^2 \to \infty, \nu \to \infty$ with $x$ fixed), the structure functions depend only on $x$ rather than $Q^2$ and $\nu$ independently:
$$F_1(x, Q^2) \longrightarrow F_1(x), \qquad F_2(x, Q^2) \longrightarrow F_2(x) \quad \text{(Bjorken Scaling)}$$
Furthermore, the Callan-Gross relation $F_2(x) = 2x F_1(x)$ proved experimentally that the constituents have intrinsic spin $s = 1/2$.
</p>

<h3>2. The Cornell Static Potential and Color Confinement</h3>
<p>
Unlike QED, where the electric force weakens as $1/r^2$ at large distances, the strong interaction between quarks exhibits two extraordinary non-perturbative phenomena:
</p>
<ol>
<li><strong>Asymptotic Freedom:</strong> At short distances ($r \ll 0.1\text{ fm}$ or high momentum transfer $Q^2 \to \infty$), the running strong coupling constant $\alpha_s(Q^2)$ diminishes logarithmically:
$$\alpha_s(Q^2) = \frac{12\pi}{(33 - 2 n_f) \ln\left( Q^2 / \Lambda_{\text{QCD}}^2 \right)}$$
Quarks behave as virtually free, non-interacting particles inside the nucleon core.</li>
<li><strong>Color Confinement:</strong> As quarks are pulled apart ($r > 0.5\text{ fm}$), non-Abelian gluon self-interactions squeeze color field lines into a narrow flux tube (string) of constant energy per unit length.</li>
</ol>
<p>
The heavy quark-antiquark ($c\bar{c}, b\bar{b}$) interaction is accurately parameterized by the <strong>Cornell potential</strong>:
$$V_{\text{Cornell}}(r) = -\frac{4}{3}\frac{\alpha_s}{r} + \kappa r$$
where:
<ul>
<li>$-\frac{4}{3}\frac{\alpha_s}{r}$ is the short-range one-gluon exchange Coulomb-like term with color Casimir factor $C_F = 4/3$.</li>
<li>$\kappa r$ is the long-range confining string tension, where $\kappa \approx 1\text{ GeV/fm} \approx 1.6 \times 10^5\text{ N}$ (a colossal mechanical tension of $16\text{ metric tons}$!).</li>
</ul>
</p>
<p>
When the energy stored in the flux tube exceeds the threshold to create a light quark-antiquark pair ($2 m_q c^2 \approx 2 m_\pi c^2$):
$$\Delta E = \kappa \Delta r \ge 2 m_q c^2$$
the flux tube snaps ("hadronization"), producing two color-singlet hadrons ($q\bar{q}'$ mesons). Isolated, free quarks are never observed in isolation in nature.
</p>
""",
            "simulation": "nuc2-quark-confinement-potential-sim"
        },
        {
            "id": "sec-7-4",
            "title": "Constituent Quark Model: Flavors, Baryon Spin-Flavor Wavefunctions & Color",
            "content": r"""
<h3>1. The Three Light Flavors</h3>
<p>
In the Gell-Mann-Zweig model, all known hadrons are color-singlet bound states composed of constituent quarks:
</p>
<table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;">
<thead>
<tr style="border-bottom:2px solid var(--border-color); text-align:left;">
<th style="padding:8px;">Flavor</th>
<th style="padding:8px;">Symbol</th>
<th style="padding:8px;">Spin $s$</th>
<th style="padding:8px;">Charge $Q/e$</th>
<th style="padding:8px;">Baryon $B$</th>
<th style="padding:8px;">$I$</th>
<th style="padding:8px;">$I_3$</th>
<th style="padding:8px;">Strangeness $S$</th>
<th style="padding:8px;">Constituent Mass</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Up</td><td style="padding:8px;">$u$</td><td style="padding:8px;">$1/2$</td><td style="padding:8px;">$+2/3$</td><td style="padding:8px;">$+1/3$</td><td style="padding:8px;">$1/2$</td><td style="padding:8px;">$+1/2$</td><td style="padding:8px;">$0$</td><td style="padding:8px;">$\approx 330\text{ MeV}/c^2$</td>
</tr>
<tr style="border-bottom:1px solid var(--border-color);">
<td style="padding:8px;">Down</td><td style="padding:8px;">$d$</td><td style="padding:8px;">$1/2$</td><td style="padding:8px;">$-1/3$</td><td style="padding:8px;">$+1/3$</td><td style="padding:8px;">$1/2$</td><td style="padding:8px;">$-1/2$</td><td style="padding:8px;">$0$</td><td style="padding:8px;">$\approx 330\text{ MeV}/c^2$</td>
</tr>
<tr>
<td style="padding:8px;">Strange</td><td style="padding:8px;">$s$</td><td style="padding:8px;">$1/2$</td><td style="padding:8px;">$-1/3$</td><td style="padding:8px;">$+1/3$</td><td style="padding:8px;">$0$</td><td style="padding:8px;">$0$</td><td style="padding:8px;">$-1$</td><td style="padding:8px;">$\approx 500\text{ MeV}/c^2$</td>
</tr>
</tbody>
</table>

<h3>2. The $\Delta^{++}$ Paradox and the Discovery of Color $SU(3)_C$</h3>
<p>
The $\Delta^{++}(1232)$ baryon has spin $J = 3/2$, electric charge $+2$, and consists of three up quarks: $|uuu\rangle$. In the ground state ($L = 0$):
<ul>
<li><strong>Spatial state:</strong> Symmetric under particle exchange ($\psi_{\text{space}}(1,2,3)$ symmetric).</li>
<li><strong>Flavor state:</strong> $|uuu\rangle$ is manifestly totally symmetric.</li>
<li><strong>Spin state:</strong> $|J=3/2, M=3/2\rangle = |\uparrow\uparrow\uparrow\rangle$ is manifestly totally symmetric.</li>
</ul>
Hence, the total wavefunction $\Psi = \psi_{\text{space}} \otimes \chi_{\text{spin}} \otimes \phi_{\text{flavor}}$ is completely symmetric under interchange of identical fermions, directly violating Pauli's Spin-Statistics Theorem!
</p>
<p>
To resolve this crisis, Oscar Greenberg, Yoichiro Nambu, and Moo-Young Han proposed that each quark flavor carries an additional three-valued degree of freedom called <strong>Color Charge</strong>: Red ($R$), Green ($G$), Blue ($B$).
The overall baryon wavefunction is:
$$\Psi_{\text{baryon}} = \psi_{\text{space}} \otimes \chi_{\text{spin}} \otimes \phi_{\text{flavor}} \otimes \xi_{\text{color}}$$
All physical hadrons must be color singlets (colorless invariant under $SU(3)_C$). For a three-quark baryon, the unique color singlet is totally antisymmetric:
$$\xi_{\text{color}} = \frac{1}{\sqrt{6}} \left( |RGB\rangle - |RBG\rangle + |BRG\rangle - |BGR\rangle + |GBR\rangle - |GRB\rangle \right) = \frac{1}{\sqrt{6}} \epsilon_{ijk} |q_i q_j q_k\rangle$$
Because $\xi_{\text{color}}$ is antisymmetric, the total product $\Psi_{\text{baryon}}$ is totally antisymmetric under identical fermion exchange, brilliantly preserving Fermi-Dirac statistics!
</p>
"""
        },
        {
            "id": "sec-7-5",
            "title": "Discrete Symmetries: Parity Inversion P & Discovery of Parity Violation",
            "content": r"""
<h3>1. The Spatial Parity Operator $\mathcal{P}$</h3>
<p>
Spatial parity $\mathcal{P}$ represents reflection of coordinates through the origin:
$$\mathcal{P}: \vec{x} \longrightarrow -\vec{x}, \qquad \vec{p} \longrightarrow -\vec{p}, \qquad \vec{L} = \vec{r}\times\vec{p} \longrightarrow +\vec{L}, \qquad \vec{S} \longrightarrow +\vec{S}$$
True vectors ($\vec{x}, \vec{p}$) are odd under parity, whereas axial vectors (pseudovectors like spin $\vec{S}$ and magnetic field $\vec{B}$) are even under parity:
$$\mathcal{P} \vec{r} \mathcal{P}^{-1} = -\vec{r}, \qquad \mathcal{P} \vec{S} \mathcal{P}^{-1} = +\vec{S}$$
The scalar product of a polar vector and an axial vector is a <strong>pseudoscalar</strong>:
$$\mathcal{P} (\vec{S} \cdot \vec{p}) \mathcal{P}^{-1} = (+\vec{S}) \cdot (-\vec{p}) = -(\vec{S} \cdot \vec{p})$$
Any physical observable proportional to $\vec{S} \cdot \vec{p}$ changes sign under spatial reflection. If a physical interaction is invariant under $\mathcal{P}$, no pseudoscalar observable can have a non-zero expectation value.
</p>

<h3>2. The $\theta$-$\tau$ Puzzle and Madame Wu's 1957 Experiment</h3>
<p>
In the mid-1950s, two particles designated $\theta^+$ and $\tau^+$ had identical masses and lifetimes, yet decayed into final states of opposite parity:
$$\theta^+ \longrightarrow \pi^+ + \pi^0 \quad (P = +1), \qquad \tau^+ \longrightarrow \pi^+ + \pi^+ + \pi^- \quad (P = -1)$$
Tsung-Dao Lee and Chen-Ning Yang recognized that while parity conservation had been exhaustively verified in strong and electromagnetic interactions, no experiment had tested it in weak decays.
</p>
<p>
In 1957, Chien-Shiung Wu (Madame Wu) along with the National Bureau of Standards polarized $^{60}\text{Co}$ nuclei ($J^\pi = 5^+$) at cryogenic temperatures ($T \approx 0.01\text{ K}$) using a strong magnetic field $\vec{B}$:
$$^{60}_{27}\text{Co} \longrightarrow {}^{60}_{28}\text{Ni}^* + e^- + \bar{\nu}_e$$
The beta decay transition is a pure Gamow-Teller transition ($5^+ \to 4^+$), requiring the emitted electron and antineutrino spins to align parallel to the nuclear spin: $\vec{S}_e \uparrow\uparrow \vec{J}$.
</p>
<p>
Wu measured the angular distribution of emitted beta electrons relative to the nuclear polarization axis:
$$I(\theta) = 1 + A \frac{v}{c} \cos\theta = 1 + A \frac{\vec{J} \cdot \vec{p}_e}{J E_e}$$
where $\theta$ is the angle between the nuclear polarization $\vec{J}$ and electron momentum $\vec{p}_e$.
Experimentally, electrons were emitted predominantly <strong>opposite</strong> to the nuclear spin axis ($A \approx -1$). Reversing the magnetic field $\vec{B} \to -\vec{B}$ flipped the emission asymmetry.
This direct measurement of a non-zero pseudoscalar $\langle \vec{J} \cdot \vec{p}_e \rangle \neq 0$ proved definitively that <strong>parity is maximally violated in weak interactions</strong> ($V - A$ theory).
</p>
"""
        },
        {
            "id": "sec-7-6",
            "title": "Charge Conjugation C, Time Reversal T & The CPT Theorem",
            "content": r"""
<h3>1. Charge Conjugation Operator $\mathcal{C}$</h3>
<p>
Charge conjugation replaces every particle with its corresponding antiparticle while preserving spacetime coordinates, spin, and momentum:
$$\mathcal{C} |p\rangle = |\bar{p}\rangle, \qquad \mathcal{C} |e^-\rangle = |e^+\rangle, \qquad \mathcal{C} |\nu_L\rangle = |\bar{\nu}_L\rangle$$
Only neutral particles that are their own antiparticles (such as $\gamma, \pi^0, \eta, \rho^0$) can be eigenstates of $\mathcal{C}$:
$$\mathcal{C} |\gamma\rangle = -|\gamma\rangle \quad (C_\gamma = -1), \qquad \mathcal{C} |\pi^0\rangle = +|\pi^0\rangle \quad (C_{\pi^0} = +1)$$
Because $C$ is conserved in electromagnetic interactions:
$$\pi^0 \longrightarrow \gamma + \gamma \implies C_{\text{final}} = (-1)(-1) = +1 \quad \text{(Allowed)}$$
$$\pi^0 \centernot\longrightarrow \gamma + \gamma + \gamma \implies C_{\text{final}} = (-1)^3 = -1 \quad \text{(Strictly Forbidden, branching ratio } < 3 \times 10^{-8}\text{)}$$
</p>

<h3>2. Failure of $\mathcal{C}$ and $CP$ Invariance in Weak Interactions</h3>
<p>
In the Standard Model, weak charged currents couple exclusively to left-handed fermions ($h = -1$) and right-handed antifermions ($h = +1$):
$$\mathcal{C} |\nu_L\rangle = |\bar{\nu}_L\rangle \quad \text{(Does not exist in SM!)}$$
Therefore, the weak interaction violates $\mathcal{C}$ maximally. However, applying the combined operation $\mathcal{CP}$:
$$\mathcal{CP} |\nu_L\rangle = |\bar{\nu}_R\rangle \quad \text{(Physically observed!)}$$
For several years, it was believed that while $\mathcal{C}$ and $\mathcal{P}$ individually fail, the combined symmetry $\mathcal{CP}$ was exact.
</p>

<h3>3. The CPT Theorem</h3>
<p>
The <strong>$CPT$ Theorem</strong> (Lüders, Pauli, Bell, Schwinger) is a mathematical theorem of axiomatic quantum field theory stating that any local, Lorentz-invariant quantum field theory with a Hermitian Hamiltonian must be invariant under the anti-unitary combined operation $\mathcal{CPT}$:
$$\mathcal{CPT} \mathcal{H}(x) (\mathcal{CPT})^{-1} = \mathcal{H}(-x)$$
Direct, inescapable consequences of exact $CPT$ invariance include:
<ol>
<li>Particles and antiparticles have identical rest masses: $m_p = m_{\bar{p}}$ (tested to $1$ part in $10^{10}$).</li>
<li>Particles and antiparticles have identical total decay lifetimes: $\tau_{\mu^+} = \tau_{\mu^-}$.</li>
<li>Particles and antiparticles possess equal and opposite electric charges and magnetic dipole moments: $q_{\bar{p}} = -q_p, \mu_{\bar{p}} = -\mu_p$.</li>
</ol>
If $CP$ is violated in nature, then by the $CPT$ theorem, time-reversal invariance $\mathcal{T}$ must be violated by an identical compensating amount.
</p>
"""
        },
        {
            "id": "sec-7-7",
            "title": "Neutral Kaon Oscillations, CP Violation & Cosmological Baryogenesis",
            "content": r"""
<h3>1. Neutral Kaon Strangeness Oscillations ($K^0 - \bar{K}^0$ Mixing)</h3>
<p>
Neutral kaons are produced as strangeness eigenstates via strong interactions:
$$\pi^- + p \longrightarrow K^0 + \Lambda^0 \quad (S = +1), \qquad \pi^+ + p \longrightarrow \bar{K}^0 + K^+ + p \quad (S = -1)$$
where $|K^0\rangle = |d\bar{s}\rangle$ and $|\bar{K}^0\rangle = |\bar{d}s\rangle$.
Under charge conjugation and parity:
$$\mathcal{CP} |K^0\rangle = -|\bar{K}^0\rangle, \qquad \mathcal{CP} |\bar{K}^0\rangle = -|K^0\rangle$$
Because weak second-order box diagrams involving $W^\pm$ and virtual $u, c, t$ quarks connect $K^0 \leftrightarrow \bar{K}^0$ ($\Delta S = 2$), strangeness is not conserved in decay.
</p>
<p>
The $CP$ eigenstates are linear superpositions:
$$|K_1^0\rangle = \frac{1}{\sqrt{2}}\left( |K^0\rangle - |\bar{K}^0\rangle \right) \quad (CP = +1), \qquad |K_2^0\rangle = \frac{1}{\sqrt{2}}\left( |K^0\rangle + |\bar{K}^0\rangle \right) \quad (CP = -1)$$
A two-pion state $|\pi\pi\rangle_{l=0}$ has $CP = +1$, whereas a three-pion state $|\pi\pi\pi\rangle_{l=0}$ has $CP = -1$.
Due to available phase space, $K_1^0 \to 2\pi$ decays $\sim 600$ times faster than $K_2^0 \to 3\pi$:
$$\tau_S \equiv \tau(K_1) \approx 0.895 \times 10^{-10}\text{ s} \quad (c\tau_S \approx 2.68\text{ cm})$$
$$\tau_L \equiv \tau(K_2) \approx 5.11 \times 10^{-8}\text{ s} \quad (c\tau_L \approx 15.3\text{ m})$$
</p>

<h3>2. The Cronin-Fitch Discovery of CP Violation (1964)</h3>
<p>
If $CP$ were an exact symmetry, a beam of neutral kaons traveling several meters would consist of $100\%$ pure $K_2^0$ ($CP = -1$), which could never decay into $2\pi$ ($CP = +1$).
In 1964 at Brookhaven, James Cronin and Val Fitch directed a neutral kaon beam into a spark chamber spectrometer $17\text{ meters}$ downstream (over $500 K_S$ decay lengths). Out of $22,700$ decays, they observed $45$ clear instances of:
$$K_L^0 \longrightarrow \pi^+ + \pi^-$$
proving that the physical long-lived state $K_L^0$ is an impure mixture with a tiny $CP = +1$ admixture:
$$|K_S^0\rangle = \frac{|K_1^0\rangle + \epsilon |K_2^0\rangle}{\sqrt{1 + |\epsilon|^2}}, \qquad |K_L^0\rangle = \frac{|K_2^0\rangle + \epsilon |K_1^0\rangle}{\sqrt{1 + |\epsilon|^2}}$$
The empirical CP violation parameter is:
$$|\epsilon| \approx (2.228 \pm 0.011) \times 10^{-3}, \qquad \arg(\epsilon) \approx 43.5^\circ$$
</p>

<h3>3. Andrei Sakharov's Conditions for Baryogenesis (1967)</h3>
<p>
The universe today is composed overwhelmingly of matter rather than antimatter (baryon-to-photon ratio $\eta \equiv n_B / n_\gamma \approx 6 \times 10^{-10}$).
In 1967, Andrei Sakharov demonstrated that generating a net baryon asymmetry from an initially symmetric Big Bang requires three fundamental conditions:
</p>
<ol>
<li><strong>Baryon Number ($B$) Violation:</strong> Non-perturbative electroweak sphaleron processes or GUT gauge boson decays ($X, Y \to q q, q l$).</li>
<li><strong>$\mathcal{C}$ and $\mathcal{CP}$ Violation:</strong> Without $C$ and $CP$ violation, reactions producing excess baryons would proceed at exactly equal rates to reactions producing excess antibaryons, yielding net $\Delta B = 0$.</li>
<li><strong>Departure from Thermal Equilibrium:</strong> In strict thermodynamic equilibrium, the CPT theorem guarantees that the equilibrium densities of particles and antiparticles are identical, wiping out any generated asymmetry.</li>
</ol>
""",
            "simulation": "nuc2-cp-violation-kaon-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-7-1",
            "title": "Quantum Number Conservation and Reaction Feasibility Analysis",
            "statement": r"""Determine whether each of the following subatomic reactions or decays is allowed or forbidden by the fundamental conservation laws. If allowed, specify the dominant interaction (Strong, Electromagnetic, or Weak). If forbidden, identify all violated conservation laws:
(a) $\pi^- + p \longrightarrow K^0 + \Lambda^0$
(b) $p + p \longrightarrow p + \Sigma^+ + K^0$
(c) $\Lambda^0 \longrightarrow p + \pi^-$
(d) $\Sigma^0 \longrightarrow \Lambda^0 + \gamma$
(e) $\mu^- \longrightarrow e^- + \gamma$""",
            "solution": r"""**(a) $\pi^- + p \longrightarrow K^0 + \Lambda^0$:**
- **Electric Charge $Q$:** $(-1) + (+1) = 0$; $0 + 0 = 0$. Conserved ($\Delta Q = 0$).
- **Baryon Number $B$:** $0 + 1 = 1$; $0 + 1 = 1$. Conserved ($\Delta B = 0$).
- **Lepton Numbers $L_i$:** All $0$. Conserved.
- **Strangeness $S$:** $0 + 0 = 0$; $(+1) + (-1) = 0$. Conserved ($\Delta S = 0$).
- **Isospin $I, I_3$:** $\pi^-(1, -1), p(1/2, +1/2) \implies I_3 = -1/2$. Final: $K^0(1/2, -1/2), \Lambda^0(0, 0) \implies I_3 = -1/2$. Conserved. Total $I = 1/2$ is accessible in both channels.
**Conclusion:** **Allowed via the Strong Interaction** (associated production of strange hadrons).

**(b) $p + p \longrightarrow p + \Sigma^+ + K^0$:**
- **Electric Charge $Q$:** $1 + 1 = 2$; $1 + 1 + 0 = 2$. Conserved.
- **Baryon Number $B$:** $1 + 1 = 2$; $1 + 1 + 0 = 2$. Conserved.
- **Strangeness $S$:** Initial: $0 + 0 = 0$. Final: $\Sigma^+(S = -1)$, $K^0(S = +1) \implies S_{\text{final}} = -1 + 1 = 0$. Conserved ($\Delta S = 0$).
- **Isospin $I_3$:** Initial: $+1/2 + 1/2 = +1$. Final: $p(+1/2) + \Sigma^+(+1) + K^0(-1/2) = +1/2 + 1 - 1/2 = +1$. Conserved ($\Delta I_3 = 0$).
**Conclusion:** **Allowed via the Strong Interaction**.

**(c) $\Lambda^0 \longrightarrow p + \pi^-$:**
- **Electric Charge $Q$:** $0 \to (+1) + (-1) = 0$. Conserved.
- **Baryon Number $B$:** $1 \to 1 + 0 = 1$. Conserved.
- **Strangeness $S$:** Initial $S = -1$; Final $0 + 0 = 0 \implies \Delta S = +1$.
Because $\Delta S = +1 \neq 0$, the strong and electromagnetic interactions are strictly forbidden.
However, charged weak currents allow $|\Delta S| = 1$ flavor transitions ($s \to u + W^-$).
**Conclusion:** **Allowed via the Weak Interaction** (lifetime $\tau = 2.6 \times 10^{-10}\text{ s}$).

**(d) $\Sigma^0 \longrightarrow \Lambda^0 + \gamma$:**
- **Electric Charge $Q$:** $0 \to 0 + 0$. Conserved.
- **Baryon Number $B$:** $1 \to 1 + 0 = 1$. Conserved.
- **Strangeness $S$:** Initial $S = -1$; Final $S = -1 \implies \Delta S = 0$. Conserved.
- **Isospin:** Initial $\Sigma^0$ has $I = 1, I_3 = 0$. Final $\Lambda^0$ has $I = 0, I_3 = 0$. Thus $\Delta I = 1, \Delta I_3 = 0$.
The photon carries $\Delta I = 0, 1$ in electromagnetic transitions.
**Conclusion:** **Allowed via the Electromagnetic Interaction** (lifetime $\tau = 7.4 \times 10^{-20}\text{ s}$).

**(e) $\mu^- \longrightarrow e^- + \gamma$:**
- **Electric Charge $Q$:** $-1 \to -1 + 0$. Conserved.
- **Muon Lepton Number $L_\mu$:** Initial $L_\mu = +1$; Final $L_\mu = 0 \implies \Delta L_\mu = -1$.
- **Electron Lepton Number $L_e$:** Initial $L_e = 0$; Final $L_e = +1 \implies \Delta L_e = +1$.
Individual lepton flavor numbers are violated.
**Conclusion:** **Strictly Forbidden in the Minimal Standard Model** (experimental branching ratio limit $< 4.2 \times 10^{-13}$ via MEG experiment)."""
        },
        {
            "id": "nuc2-prob-7-2",
            "title": "Quantitative Parity Violation in Polarized Cobalt-60 Beta Decay",
            "statement": r"""In Madame Wu's 1957 parity violation experiment, $^{60}\text{Co}$ nuclei undergo pure Gamow-Teller allowed beta decay:
$$^{60}_{27}\text{Co} (J^\pi = 5^+) \longrightarrow {}^{60}_{28}\text{Ni}^* (J^\pi = 4^+) + e^- + \bar{\nu}_e$$
The differential angular distribution of beta electrons emitted at angle $\theta$ relative to the nuclear spin polarization vector $\vec{J}$ is:
$$I(\theta) = 1 + \mathcal{A} \frac{v}{c} \cos\theta$$
where $\mathcal{A}$ is the beta asymmetry parameter and $v/c$ is the electron velocity in units of $c$.
(a) For a pure Gamow-Teller transition $J \to J - 1$, standard $V-A$ electroweak theory predicts:
$$\mathcal{A} = -\frac{1}{J + 1}$$
Evaluate $\mathcal{A}$ for the decay of $^{60}\text{Co}$ ($J = 5$).
(b) A beta electron is emitted with kinetic energy $T_e = 150\text{ keV}$. Given the electron rest mass $m_e c^2 = 511\text{ keV}$, calculate the velocity ratio $v/c$.
(c) Assuming nuclear polarization $P = \langle J_z \rangle / J = 0.65$ was achieved, calculate the forward-to-backward counting ratio:
$$\mathcal{R} \equiv \frac{I(0^\circ)}{I(180^\circ)}$$
and discuss why this ratio proves parity violation.""",
            "solution": r"""**(a) Asymmetry Parameter $\mathcal{A}$:**
For a pure $J \to J - 1$ transition with $J = 5$:
$$\mathcal{A} = -\frac{1}{5 + 1} = -\frac{1}{6} \approx \mathbf{-0.1667}$$
*(Note: If the nuclear polarization is defined with respect to the initial parent spin vector, the electron angular distribution scales with the polarization fraction $P$.)*

**(b) Relativistic Velocity $v/c$ for $T_e = 150\text{ keV}$:**
Total relativistic energy of the electron:
$$E = T_e + m_e c^2 = 150\text{ keV} + 511\text{ keV} = 661\text{ keV}$$
Lorentz factor:
$$\gamma = \frac{E}{m_e c^2} = \frac{661}{511} \approx 1.2935$$
Velocity ratio:
$$\frac{v}{c} = \sqrt{1 - \frac{1}{\gamma^2}} = \sqrt{1 - \frac{1}{(1.2935)^2}} = \sqrt{1 - \frac{1}{1.6732}} = \sqrt{1 - 0.5976} = \sqrt{0.4024} \approx \mathbf{0.6343}$$

**(c) Forward-to-Backward Counting Ratio $\mathcal{R}$:**
Including the degree of polarization $P = 0.65$:
$$I(\theta) = 1 + P \mathcal{A} \frac{v}{c} \cos\theta$$
$$P \mathcal{A} \frac{v}{c} = (0.65) \times (-0.1667) \times (0.6343) \approx -0.0687$$
Evaluating at $\theta = 0^\circ$ (forward, parallel to $\vec{J}$) and $\theta = 180^\circ$ (backward, antiparallel to $\vec{J}$):
$$I(0^\circ) = 1 - 0.0687 = 0.9313$$
$$I(180^\circ) = 1 - 0.0687(-1) = 1 + 0.0687 = 1.0687$$
The forward-to-backward ratio is:
$$\mathcal{R} = \frac{I(0^\circ)}{I(180^\circ)} = \frac{0.9313}{1.0687} \approx \mathbf{0.871}$$
**Parity Violation Demonstration:**
Under spatial inversion $\vec{x} \to -\vec{x}$, the polar momentum vector flips ($\vec{p}_e \to -\vec{p}_e$) while the axial spin vector remains unchanged ($\vec{J} \to +\vec{J}$).
Thus, parity reflection transforms $\theta \to 180^\circ - \theta$, mapping forward emission into backward emission.
If parity were conserved, the physical law would require $I(\theta) = I(180^\circ - \theta)$, demanding $\mathcal{R} = 1.000$.
The measured ratio $\mathcal{R} = 0.871 \neq 1$ definitively demonstrates that nature distinguishes between left-handed and right-handed coordinate systems!"""
        },
        {
            "id": "nuc2-prob-7-3",
            "title": "Neutral Kaon Mass Splitting and Strangeness Oscillation Frequency",
            "statement": r"""The long-lived and short-lived neutral kaon states have experimentally measured lifetimes:
$$\tau_S = 0.895 \times 10^{-10}\text{ s}, \qquad \tau_L = 5.11 \times 10^{-8}\text{ s}$$
and an exceptionally tiny mass difference:
$$\Delta m \equiv m_L - m_S \approx 3.484 \times 10^{-12}\text{ MeV}/c^2 = 3.484 \times 10^{-6}\text{ eV}/c^2$$
(a) Convert the mass difference $\Delta m$ into an oscillation frequency $\Delta\omega = \Delta m c^2 / \hbar$ in radians per second ($\text{rad/s}$).
(b) Evaluate the dimensionless ratio $\Delta m / \Gamma_S$, where $\Gamma_S = \hbar / \tau_S$ is the total decay width of the short-lived kaon.
(c) Suppose a pure $K^0$ beam ($S = +1$) is produced at $t = 0$. Neglecting CP violation ($\epsilon = 0$), the probability of finding a $\bar{K}^0$ ($S = -1$) at proper time $t$ is:
$$P(\bar{K}^0, t) = \frac{1}{4}\left[ e^{-\Gamma_S t} + e^{-\Gamma_L t} - 2 e^{-\frac{\Gamma_S + \Gamma_L}{2} t} \cos\left( \frac{\Delta m c^2}{\hbar} t \right) \right]$$
Calculate the proper time $t_{\text{max}}$ (in units of $\tau_S$) at which the probability of detecting $\bar{K}^0$ reaches its absolute maximum, and evaluate $P(\bar{K}^0, t_{\text{max}})$.""",
            "solution": r"""**(a) Oscillation Frequency $\Delta\omega$:**
Given $\hbar = 6.5821 \times 10^{-16}\text{ eV}\cdot\text{s}$:
$$\Delta\omega = \frac{\Delta m c^2}{\hbar} = \frac{3.484 \times 10^{-6}\text{ eV}}{6.5821 \times 10^{-16}\text{ eV}\cdot\text{s}} \approx \mathbf{5.293 \times 10^9\text{ rad/s}}$$
The neutral kaon oscillates between $K^0$ and $\bar{K}^0$ at over 5 billion radians per second!

**(b) Dimensionless Ratio $\Delta m / \Gamma_S$:**
Decay width of $K_S$:
$$\Gamma_S = \frac{\hbar}{\tau_S} = \frac{6.5821 \times 10^{-16}\text{ eV}\cdot\text{s}}{0.895 \times 10^{-10}\text{ s}} \approx 7.354 \times 10^{-6}\text{ eV}$$
Comparing $\Delta m c^2$ with $\Gamma_S$:
$$\frac{\Delta m c^2}{\Gamma_S} = \frac{3.484 \times 10^{-6}\text{ eV}}{7.354 \times 10^{-6}\text{ eV}} \approx \mathbf{0.4738} \approx \frac{1}{2}$$
Remarkably, $\Delta m \approx 0.5 \Gamma_S$. This means the mass splitting between $K_L$ and $K_S$ is almost exactly half the decay width of $K_S$, allowing the kaon to complete approximately half an oscillation cycle before the short-lived component decays away!

**(c) Time of Maximum $\bar{K}^0$ Probability:**
Since $\tau_L \approx 570 \tau_S$, over the timescale $t \sim \text{few } \tau_S$ we have $\Gamma_L \ll \Gamma_S$ and $e^{-\Gamma_L t} \approx 1$.
Let $x \equiv t / \tau_S = \Gamma_S t$ and $\delta \equiv \frac{\Delta m}{\Gamma_S} \approx 0.474$:
$$P(\bar{K}^0, x) \approx \frac{1}{4}\left[ e^{-x} + 1 - 2 e^{-x/2} \cos(\delta x) \right]$$
Taking the derivative with respect to $x$ and setting to zero:
$$\frac{dP}{dx} \propto -e^{-x} + e^{-x/2} \cos(\delta x) + 2 \delta e^{-x/2} \sin(\delta x) = 0$$
Dividing by $e^{-x/2}$:
$$e^{-x/2} = \cos(\delta x) + 2 \delta \sin(\delta x)$$
Substituting $\delta = 0.4738$:
Solving numerically:
At $x = 0$: $e^0 = 1 = 1 + 0$ (minimum $P=0$).
For small $x$, $1 - x/2 \approx 1 - \frac{1}{2}\delta^2 x^2 + 2\delta^2 x \implies$ increases.
Testing values:
At $x = 4.0$:
- $e^{-2.0} \approx 0.1353$
- $\delta x = 0.4738 \times 4.0 = 1.895\text{ rad} \approx 108.6^\circ$
- $\cos(1.895) \approx -0.3188$
- $\sin(1.895) \approx 0.9478$
- RHS $= -0.3188 + 2(0.4738)(0.9478) = -0.3188 + 0.8981 = 0.5793$
Testing $x = 4.8$:
- $e^{-2.4} \approx 0.0907$
- $\delta x = 2.274\text{ rad} \implies \cos(2.274) \approx -0.6457, \sin(2.274) \approx 0.7636$
- RHS $= -0.6457 + 2(0.4738)(0.7636) = -0.6457 + 0.7236 = +0.0779$
The exact root is at **$t_{\text{max}} \approx 4.75 \tau_S$**.
Evaluating the probability at $t_{\text{max}}$:
$$e^{-4.75} \approx 0.00865, \qquad e^{-2.375} \approx 0.0930$$
$$\cos(0.4738 \times 4.75) = \cos(2.250\text{ rad}) \approx -0.6282$$
$$P(\bar{K}^0, t_{\text{max}}) \approx \frac{1}{4}\left[ 0.0087 + 1.000 - 2(0.0930)(-0.6282) \right] = \frac{1}{4}\left[ 1.0087 + 0.1168 \right] = \frac{1.1255}{4} \approx \mathbf{0.281} = \mathbf{28.1\%}$$
A beam that started as pure $K^0$ evolves so that after $4.75$ lifetimes of $K_S$, **$28.1\%$** of the surviving kaons are antikaons $\bar{K}^0$!"""
        }
    ]
}

u8_data = {
    "title": "Elementary Particles II: Hadron Spectroscopy, SU(3) Flavor & Electroweak Unification",
    "subtitle": "Eightfold Way, Gell-Mann-Okubo Formula, Color QCD, Electroweak GWS & Neutrino Oscillations",
    "summary": "Deep journey into modern particle physics and gauge field symmetries: Lie algebra su(3) flavor and the Eightfold Way, Young tableaux and tensor decomposition 3 ⊗ 3̄ = 8 ⊕ 1 and 3 ⊗ 3 ⊗ 3 = 10 ⊕ 8 ⊕ 8 ⊕ 1, Gell-Mann-Okubo mass formula and the historic prediction and discovery of the Ω- hyperon, Quantum Chromodynamics (QCD) as a non-Abelian SU(3)_C gauge theory with running coupling and asymptotic freedom, Glashow-Weinberg-Salam electroweak unification SU(2)_L × U(1)_Y with spontaneous symmetry breaking and the Higgs mechanism, CKM quark mixing, and neutrino oscillation physics through the PMNS matrix and MSW solar matter resonances.",
    "sections": [
        {
            "id": "sec-8-1",
            "title": "Lie Group SU(3) Flavor Symmetry & The Eight Gell-Mann Matrices",
            "content": r"""
<h3>1. The Special Unitary Group $SU(3)$</h3>
<p>
The mathematical foundation of hadron classification is the compact Lie group $SU(3)$—the group of $3 \times 3$ unitary matrices with unit determinant ($\det U = 1, U^\dagger U = \mathbb{I}$).
Any element of $SU(3)$ near the identity can be parameterized in terms of $8$ traceless, Hermitian generator matrices $T_a \equiv \frac{1}{2}\lambda_a$ ($a = 1, 2, \dots, 8$):
$$U = \exp\left( i \sum_{a=1}^8 \theta_a T_a \right) = \exp\left( \frac{i}{2} \sum_{a=1}^8 \theta_a \lambda_a \right)$$
where $\lambda_a$ are the standard <strong>Gell-Mann matrices</strong>:
$$\lambda_1 = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_2 = \begin{pmatrix} 0 & -i & 0 \\ i & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
$$\lambda_4 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}, \quad
\lambda_5 = \begin{pmatrix} 0 & 0 & -i \\ 0 & 0 & 0 \\ i & 0 & 0 \end{pmatrix}, \quad
\lambda_6 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \quad
\lambda_7 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -i \\ 0 & i & 0 \end{pmatrix}$$
$$\lambda_8 = \frac{1}{\sqrt{3}}\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -2 \end{pmatrix}$$
</p>

<h3>2. Cartan Subalgebra and Commutation Relations</h3>
<p>
The Lie algebra satisfies the commutation relations:
$$[T_a, T_b] = i \sum_{c=1}^8 f_{abc} T_c$$
where $f_{abc}$ are the totally antisymmetric structure constants of $SU(3)$ ($f_{123} = 1, f_{147} = 1/2, f_{458} = \sqrt{3}/2$, etc.).
The rank of $SU(3)$ is $2$, meaning that at most two generators can be simultaneously diagonalized. These two mutually commuting operators define the <strong>Cartan subalgebra</strong>:
$$I_3 = T_3 = \frac{1}{2}\lambda_3 \quad \text{(Third component of Isospin)}$$
$$Y = \frac{2}{\sqrt{3}} T_8 = \frac{1}{\sqrt{3}}\lambda_8 \quad \text{(Strong Hypercharge)}$$
Every state in an $SU(3)$ multiplet is uniquely plotted on a 2D <strong>weight diagram</strong> using eigenvalues $(I_3, Y)$ as orthogonal Cartesian axes.
</p>
"""
        },
        {
            "id": "sec-8-2",
            "title": "Hadron Multiplet Decomposition: Meson Nonets & Baryon Decuplet/Octet",
            "content": r"""
<h3>1. The Fundamental Triplet and Meson Multiplets</h3>
<p>
The fundamental representation $\mathbf{3}$ consists of the three light quark flavors $(u, d, s)^T$:
$$u: \left( I_3 = +1/2, Y = +1/3 \right), \quad d: \left( I_3 = -1/2, Y = +1/3 \right), \quad s: \left( I_3 = 0, Y = -2/3 \right)$$
The conjugate representation $\bar{\mathbf{3}}$ consists of the antiquarks $(\bar{u}, \bar{d}, \bar{s})$ with inverted quantum numbers.
</p>
<p>
Mesons are quark-antiquark bound states:
$$\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$$
decomposing into an $SU(3)$ octet and a flavor singlet.
For pseudoscalar mesons ($J^P = 0^-$):
<ul>
<li><strong>Isospin Triplet ($Y = 0$):</strong> $\pi^+ = |u\bar{d}\rangle$, $\pi^0 = \frac{1}{\sqrt{2}}(|u\bar{u}\rangle - |d\bar{d}\rangle)$, $\pi^- = -|d\bar{u}\rangle$.</li>
<li><strong>Strange Doublets:</strong> $K^+ = |u\bar{s}\rangle, K^0 = |d\bar{s}\rangle$ ($Y = +1$); $\bar{K}^0 = -|s\bar{d}\rangle, K^- = |s\bar{u}\rangle$ ($Y = -1$).</li>
<li><strong>Octet Singlet ($I = 0, Y = 0$):</strong> $\eta_8 = \frac{1}{\sqrt{6}}(|u\bar{u}\rangle + |d\bar{d}\rangle - 2|s\bar{s}\rangle)$.</li>
<li><strong>Flavor Singlet ($I = 0, Y = 0$):</strong> $\eta_1 = \frac{1}{\sqrt{3}}(|u\bar{u}\rangle + |d\bar{d}\rangle + |s\bar{s}\rangle)$.</li>
</ul>
Due to $SU(3)$ breaking, the physical $\eta$ and $\eta'$ mesons mix with mixing angle $\theta_P \approx -11.5^\circ$:
$$\eta = \eta_8 \cos\theta_P - \eta_1 \sin\theta_P, \qquad \eta' = \eta_8 \sin\theta_P + \eta_1 \cos\theta_P$$
</p>

<h3>2. Baryon Multiplets ($qqq$)</h3>
<p>
Combining three fundamental triplets:
$$\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10}_S \oplus \mathbf{8}_{M_S} \oplus \mathbf{8}_{M_A} \oplus \mathbf{1}_A$$
<ol>
<li><strong>The Baryon Decuplet ($\mathbf{10}$, $J^P = 3/2^+$):</strong> Totally symmetric in flavor and spin. Comprises the four $\Delta(1232)$ resonances ($Y = 1$), the three $\Sigma^*(1385)$ resonances ($Y = 0$), the two $\Xi^*(1530)$ resonances ($Y = -1$), and the singular $\Omega^-(1672)$ hyperon ($Y = -2$).</li>
<li><strong>The Baryon Octet ($\mathbf{8}$, $J^P = 1/2^+$):</strong> Mixed symmetry. Comprises the nucleon doublet ($p, n$, $Y=1$), the sigma triplet ($\Sigma^+, \Sigma^0, \Sigma^-$, $Y=0$), the lambda singlet ($\Lambda^0$, $Y=0$), and the cascade doublet ($\Xi^0, \Xi^-$, $Y=-1$).</li>
</ol>
</p>
"""
        },
        {
            "id": "sec-8-3",
            "title": "The Gell-Mann-Okubo Mass Formula & Discovery of the Omega-Minus",
            "content": r"""
<h3>1. Breaking of Flavor $SU(3)$ and the Mass Formula</h3>
<p>
If flavor $SU(3)$ were an exact symmetry, all eight baryons in the octet would have identically degenerate masses. However, because the strange quark is substantially heavier than the up and down quarks ($m_s - m_{u,d} \approx 150\text{ MeV}/c^2$), $SU(3)$ symmetry is broken.
The symmetry-breaking Hamiltonian transforms as the $T_8$ (hypercharge) component of an octet:
$$\mathcal{H}_{\text{break}} \propto T_8 \propto Y$$
</p>
<p>
Applying the Wigner-Eckart theorem to the matrix elements of $\mathcal{H}_{\text{break}}$ within the baryon octet yields the famous <strong>Gell-Mann-Okubo (GMO) Mass Formula</strong>:
$$M = M_0 + a Y + b\left[ I(I+1) - \frac{Y^2}{4} \right]$$
where $M_0, a, b$ are empirical constants.
This establishes a rigorous linear constraint among the masses of the four octet sub-multiplets:
$$\frac{M_N + M_\Xi}{2} = \frac{3 M_\Lambda + M_\Sigma}{4}$$
Inserting experimental values:
$$\text{LHS} = \frac{938.9 + 1318.3}{2} = 1128.6\text{ MeV}/c^2$$
$$\text{RHS} = \frac{3(1115.7) + 1193.1}{4} = \frac{3347.1 + 1193.1}{4} = 1135.0\text{ MeV}/c^2$$
Agreement is within an astonishing **$0.5\%$**, providing breathtaking proof of the underlying Lie algebraic symmetry!
</p>

<h3>2. The Decuplet Equal-Spacing Rule and the Historic $\Omega^-$ Prediction</h3>
<p>
For the totally symmetric baryon decuplet ($\mathbf{10}$), $I = 1 + Y/2$. Substituting this into the GMO formula causes the quadratic terms to cancel identically, yielding a strictly linear relation:
$$M(\mathbf{10}) = M_0' + c Y = M_0'' - c S$$
This predicts that adjacent strangeness rows in the decuplet must have **equal mass spacing**:
$$M_{\Sigma^*} - M_\Delta = M_{\Xi^*} - M_{\Sigma^*} = M_{\Omega^-} - M_{\Xi^*} \equiv \Delta M \approx 145\text{ to }147\text{ MeV}/c^2$$
</p>
<p>
In 1962, the $\Delta$ ($1232\text{ MeV}$), $\Sigma^*$ ($1385\text{ MeV}$), and $\Xi^*$ ($1530\text{ MeV}$) were known, but the bottom tip of the decuplet triangle was completely vacant.
Murray Gell-Mann famously stood up at the 1962 CERN conference and predicted:
<ol>
<li>A new particle $\Omega^-$ with strangeness $S = -3$ and quark content $|sss\rangle$.</li>
<li>Spin and parity $J^P = 3/2^+$, electric charge $Q = -1$.</li>
<li>Rest mass $M_{\Omega^-} = 1530 + 145 = \mathbf{1675\text{ MeV}/c^2}$.</li>
<li>Because it is the lightest hadron with $S = -3$, it cannot decay via strong interactions (which conserve strangeness); it must decay via weak interactions with a long lifetime $\tau \sim 10^{-10}\text{ s}$ via $\Omega^- \to \Xi^0 \pi^-$ or $\Lambda K^-$.</li>
</ol>
In February 1964 at Brookhaven National Laboratory, Nicholas Samios and his team observed the first $\Omega^-$ in an 80-inch liquid hydrogen bubble chamber with mass **$1672.45 \pm 0.29\text{ MeV}/c^2$**—a triumph of theoretical physics that earned Gell-Mann the 1969 Nobel Prize in Physics.
</p>
""",
            "simulation": "nuc2-su3-flavor-multiplet-sim"
        },
        {
            "id": "sec-8-4",
            "title": "Quantum Chromodynamics (QCD) & The Non-Abelian Gauge Theory",
            "content": r"""
<h3>1. Non-Abelian $SU(3)_C$ Local Gauge Invariance</h3>
<p>
Quantum Chromodynamics is the quantum field theory describing the strong interaction. The QCD Lagrangian density is:
$$\mathcal{L}_{\text{QCD}} = \sum_{f} \bar{\psi}_f^i (i \gamma^\mu D_\mu - m_f) \psi_f^i - \frac{1}{4} G_{\mu\nu}^a G^{\mu\nu}_a$$
where $\psi_f^i$ is the quark Dirac field for flavor $f$ and color index $i \in \{1,2,3\}$ (red, green, blue).
The gauge-covariant derivative is:
$$D_\mu = \partial_\mu - i g_s \sum_{a=1}^8 T_a A_\mu^a$$
where $A_\mu^a$ are the $8$ gluon gauge fields and $T_a = \lambda_a / 2$ are the generators of $SU(3)_C$.
</p>
<p>
Because $SU(3)$ is non-Abelian (its generators do not commute), the gluon field strength tensor includes a non-linear quadratic self-coupling term:
$$G_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g_s f_{abc} A_\mu^b A_\nu^c$$
This self-coupling enables gluons to interact directly with other gluons via 3-gluon and 4-gluon vertices—the physical origin of anti-screening, asymptotic freedom, and confinement.
</p>

<h3>2. The Beta Function and the 2004 Nobel Prize</h3>
<p>
The scale dependence of the strong coupling $\alpha_s \equiv g_s^2 / (4\pi)$ is dictated by the Callan-Symanzik beta function:
$$\mu \frac{\partial \alpha_s}{\partial \mu} = \beta(\alpha_s) = - \frac{\beta_0}{2\pi} \alpha_s^2 - \frac{\beta_1}{4\pi^2} \alpha_s^3 - \dots$$
At one-loop order:
$$\beta_0 = 11 - \frac{2}{3} n_f$$
where $11$ originates from gluon self-energy (antiscreening) and $-\frac{2}{3} n_f$ arises from virtual quark-antiquark loops (screening).
For the Standard Model with $n_f = 6$ active quark flavors:
$$\beta_0 = 11 - \frac{2}{3}(6) = 11 - 4 = +7 > 0$$
Because $\beta_0 > 0$, the beta function is strictly negative ($\beta(\alpha_s) < 0$), causing the coupling constant to decrease monotonically as energy scale increases (Asymptotic Freedom).
David Gross, David Politzer, and Frank Wilczek were awarded the 2004 Nobel Prize in Physics for this profound discovery.
</p>
"""
        },
        {
            "id": "sec-8-5",
            "title": "Electroweak Unification: The Glashow-Weinberg-Salam Model",
            "content": r"""
<h3>1. The $SU(2)_L \times U(1)_Y$ Gauge Group</h3>
<p>
Sheldon Glashow, Steven Weinberg, and Abdus Salam unified the electromagnetic and weak interactions into a single gauge theory based on the local symmetry group:
$$\mathcal{G}_{\text{EW}} = SU(2)_L \times U(1)_Y$$
where:
<ul>
<li>$SU(2)_L$ acts only on left-handed fermion doublets, with coupling constant $g$ and three gauge bosons $W_\mu^1, W_\mu^2, W_\mu^3$.</li>
<li>$U(1)_Y$ couples to weak hypercharge $Y = 2(Q - T_3)$, with coupling constant $g'$ and one gauge boson $B_\mu$.</li>
</ul>
Fermions are arranged into chiral representations:
$$\begin{pmatrix} \nu_e \\ e^- \end{pmatrix}_L \quad \left( T = \frac{1}{2}, Y = -1 \right), \qquad e^-_R \quad (T = 0, Y = -2)$$
$$\begin{pmatrix} u \\ d' \end{pmatrix}_L \quad \left( T = \frac{1}{2}, Y = +\frac{1}{3} \right), \qquad u_R \quad \left( T = 0, Y = +\frac{4}{3} \right), \qquad d'_R \quad \left( T = 0, Y = -\frac{2}{3} \right)$$
</p>

<h3>2. Spontaneous Symmetry Breaking and the Higgs Mechanism</h3>
<p>
To generate masses for the gauge bosons without destroying gauge invariance, a complex scalar doublet $\Phi$ is introduced with the Mexican-hat potential:
$$V(\Phi) = \mu^2 \Phi^\dagger \Phi + \lambda (\Phi^\dagger \Phi)^2, \qquad \mu^2 < 0$$
The vacuum acquires a non-zero vacuum expectation value (VEV):
$$\langle \Phi \rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ v \end{pmatrix}, \qquad v = \sqrt{\frac{-\mu^2}{\lambda}} \approx 246.22\text{ GeV}$$
Spontaneous symmetry breaking breaks the symmetry group down to the electromagnetic subgroup:
$$SU(2)_L \times U(1)_Y \xrightarrow{\langle \Phi \rangle} U(1)_{\text{EM}}$$
The three Goldstone bosons are "eaten" by the gauge fields, giving mass to three vector bosons:
$$W^\pm_\mu = \frac{1}{\sqrt{2}} \left( W_\mu^1 \mp i W_\mu^2 \right) \implies M_W = \frac{1}{2} g v \approx 80.38\text{ GeV}/c^2$$
The neutral gauge bosons mix by the <strong>weak mixing angle</strong> (Weinberg angle) $\theta_W$:
$$\begin{pmatrix} Z_\mu \\ A_\mu \end{pmatrix} = \begin{pmatrix} \cos\theta_W & -\sin\theta_W \\ \sin\theta_W & \cos\theta_W \end{pmatrix} \begin{pmatrix} W_\mu^3 \\ B_\mu \end{pmatrix}$$
where:
$$\cos\theta_W \equiv \frac{g}{\sqrt{g^2 + g'^2}} = \frac{M_W}{M_Z}, \qquad \sin\theta_W \equiv \frac{g'}{\sqrt{g^2 + g'^2}}$$
The neutral $Z^0$ boson acquires a mass:
$$M_Z = \frac{M_W}{\cos\theta_W} = \frac{1}{2} \sqrt{g^2 + g'^2} v \approx 91.1876\text{ GeV}/c^2$$
while the photon $A_\mu$ remains strictly massless ($M_\gamma = 0$) with electric charge coupling:
$$e = g \sin\theta_W = g' \cos\theta_W$$
The experimental measurement $\sin^2\theta_W \approx 0.2312$ accurately links all electroweak phenomena.
</p>
"""
        },
        {
            "id": "sec-8-6",
            "title": "The CKM Quark Mixing Matrix & Discovery of the Higgs Boson",
            "content": r"""
<h3>1. The Cabibbo-Kobayashi-Maskawa (CKM) Matrix</h3>
<p>
In the Standard Model, the quark mass eigenstates $(d, s, b)$ are not identical to the weak interaction eigenstates $(d', s', b')$. The weak charged current transitions involve the unitary $3 \times 3$ <strong>CKM mixing matrix</strong>:
$$\begin{pmatrix} d' \\ s' \\ b' \end{pmatrix} = \begin{pmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{pmatrix} \begin{pmatrix} d \\ s \\ b \end{pmatrix}$$
In the Chau-Keung standard parameterization, the CKM matrix is expressed in terms of three Euler angles $(\theta_{12}, \theta_{23}, \theta_{13})$ and one complex Dirac $CP$-violating phase $\delta_{13}$:
$$V_{\text{CKM}} = \begin{pmatrix} c_{12} c_{13} & s_{12} c_{13} & s_{13} e^{-i\delta_{13}} \\ -s_{12} c_{23} - c_{12} s_{23} s_{13} e^{i\delta_{13}} & c_{12} c_{23} - s_{12} s_{23} s_{13} e^{i\delta_{13}} & s_{23} c_{13} \\ s_{12} s_{23} - c_{12} c_{23} s_{13} e^{i\delta_{13}} & -c_{12} s_{23} - s_{12} c_{23} s_{13} e^{i\delta_{13}} & c_{23} c_{13} \end{pmatrix}$$
where $c_{ij} = \cos\theta_{ij}, s_{ij} = \sin\theta_{ij}$.
Experimental magnitudes:
$$|V_{\text{CKM}}| \approx \begin{pmatrix} 0.974 & 0.225 & 0.0038 \\ 0.225 & 0.973 & 0.041 \\ 0.0086 & 0.040 & 0.999 \end{pmatrix}$$
The non-zero complex phase $\delta_{13} \approx 65^\circ$ is the fundamental source of all $CP$ violation observed in the quark sector.
Makoto Kobayashi and Toshihide Maskawa shared the 2008 Nobel Prize in Physics for demonstrating that $CP$ violation requires at least three generations of quarks.
</p>

<h3>2. Discovery of the Higgs Boson at CERN LHC (2012)</h3>
<p>
The final missing cornerstone of the Standard Model was the Higgs boson—the excitation of the scalar field above the vacuum: $\Phi = \frac{1}{\sqrt{2}} (0, v + h(x))^T$.
On July 4, 2012, the ATLAS and CMS collaborations at CERN's Large Hadron Collider announced the discovery of a neutral scalar particle:
$$m_H = 125.18 \pm 0.16\text{ GeV}/c^2, \qquad J^P = 0^+$$
detected primarily via the rare but ultra-clean decays $H \to \gamma\gamma$ and $H \to Z Z^* \to 4\ell$.
This momentous discovery completed the Standard Model and led to the 2013 Nobel Prize in Physics for François Englert and Peter Higgs.
</p>
"""
        },
        {
            "id": "sec-8-7",
            "title": "Neutrino Oscillations: PMNS Mixing, Solar/Atmospheric Mass Splittings & MSW Effect",
            "content": r"""
<h3>1. The Lepton Mixing Phenomenon</h3>
<p>
In the original Standard Model, neutrinos were assumed to be strictly massless. However, definitive measurements from Super-Kamiokande (1998, atmospheric neutrinos) and SNO (2001, solar neutrinos) proved that neutrinos undergo flavor oscillations, demonstrating conclusively that neutrinos possess non-zero masses and mix across generations.
</p>
<p>
The weak flavor eigenstates $|\nu_\alpha\rangle$ ($\alpha = e, \mu, \tau$) are quantum superpositions of mass eigenstates $|\nu_i\rangle$ ($i = 1, 2, 3$ with masses $m_i$):
$$|\nu_\alpha\rangle = \sum_{i=1}^3 U_{\alpha i}^* |\nu_i\rangle$$
where $U$ is the $3 \times 3$ <strong>Pontecorvo-Maki-Nakagawa-Sakata (PMNS)</strong> matrix:
$$U_{\text{PMNS}} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & c_{23} & s_{23} \\ 0 & -s_{23} & c_{23} \end{pmatrix}
\begin{pmatrix} c_{13} & 0 & s_{13} e^{-i\delta_{\text{CP}}} \\ 0 & 1 & 0 \\ -s_{13} e^{i\delta_{\text{CP}}} & 0 & c_{13} \end{pmatrix}
\begin{pmatrix} c_{12} & s_{12} & 0 \\ -s_{12} & c_{12} & 0 \\ 0 & 0 & 1 \end{pmatrix} \times \text{diag}(e^{i\alpha_1/2}, e^{i\alpha_2/2}, 1)$$
where:
<ul>
<li>$\theta_{12} \approx 33.4^\circ$ is the solar mixing angle.</li>
<li>$\theta_{23} \approx 45^\circ$ is the atmospheric mixing angle (near maximal!).</li>
<li>$\theta_{13} \approx 8.6^\circ$ is the reactor mixing angle (Daya Bay, RENO).</li>
<li>$\delta_{\text{CP}}$ is the leptonic Dirac CP violation phase.</li>
</ul>
</p>

<h3>2. Vacuum Oscillation Probability</h3>
<p>
In the simplified two-flavor approximation (valid when one mass splitting dominates), the probability that a neutrino produced with flavor $\alpha$ is detected with flavor $\beta$ after propagating a baseline distance $L$ with energy $E$ is:
$$P(\nu_\alpha \to \nu_\beta) = \sin^2(2\theta) \sin^2\left( \frac{\Delta m^2 c^4 L}{4 \hbar c E} \right) = \sin^2(2\theta) \sin^2\left( 1.267 \frac{\Delta m^2 [\text{eV}^2] L [\text{km}]}{E [\text{GeV}]} \right)$$
where $\Delta m^2 \equiv m_2^2 - m_1^2$.
Global experimental data reveals two distinct mass-squared differences:
$$\Delta m_{21}^2 \text{ (Solar)} \approx (7.53 \pm 0.18) \times 10^{-5}\text{ eV}^2$$
$$|\Delta m_{32}^2| \text{ (Atmospheric)} \approx (2.45 \pm 0.05) \times 10^{-3}\text{ eV}^2$$
</p>

<h3>3. The Mikheyev-Smirnov-Wolfenstein (MSW) Matter Effect</h3>
<p>
When neutrinos propagate through dense solar or terrestrial matter, electron neutrinos $\nu_e$ experience an additional coherent forward scattering potential with electrons via charged-current $W$-exchange:
$$V_{\text{CC}} = \sqrt{2} G_F n_e(r)$$
where $n_e(r)$ is the electron number density. Muon and tau neutrinos experience only neutral-current scattering.
This introduces an effective in-medium mixing angle:
$$\sin^2(2\theta_m) = \frac{\sin^2(2\theta)}{\left( \cos 2\theta - \frac{2\sqrt{2} G_F n_e E}{\Delta m^2} \right)^2 + \sin^2(2\theta)}$$
At the critical <strong>MSW resonance density</strong> where $\cos 2\theta = \frac{2\sqrt{2} G_F n_e^{\text{res}} E}{\Delta m^2}$, the effective mixing angle becomes maximal ($\theta_m = 45^\circ$) regardless of how small the vacuum mixing angle is!
As $\nu_e$ created in the solar core travel outward through decreasing density, they undergo an adiabatic level crossing, emerging almost completely as $\nu_2$ mass eigenstates, brilliantly explaining the long-standing "Solar Neutrino Problem" resolved by SNO and Super-Kamiokande (2015 Nobel Prize for Takaaki Kajita and Arthur McDonald).
</p>
""",
            "simulation": "nuc2-neutrino-oscillation-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-8-1",
            "title": "Decuplet Equal-Spacing Rule and Omega-Minus Mass Prediction",
            "statement": r"""The experimental masses of the lowest three members of the baryon spin-$3/2^+$ decuplet are:
$$M(\Delta) = 1232\text{ MeV}/c^2 \quad (S = 0), \qquad M(\Sigma^*) = 1385\text{ MeV}/c^2 \quad (S = -1), \qquad M(\Xi^*) = 1532\text{ MeV}/c^2 \quad (S = -2)$$
(a) Evaluate the two experimental mass splittings $\Delta M_1 = M(\Sigma^*) - M(\Delta)$ and $\Delta M_2 = M(\Xi^*) - M(\Sigma^*)$, and test whether they support the Gell-Mann-Okubo decuplet equal-spacing prediction.
(b) Predict the rest mass $M(\Omega^-)$ of the $S = -3$ decuplet state using the average mass splitting.
(c) Compare your theoretical prediction with the modern PDG world average mass $M_{\text{PDG}}(\Omega^-) = 1672.45\text{ MeV}/c^2$ and calculate the percentage error.""",
            "solution": r"""**(a) Experimental Mass Splittings:**
$$\Delta M_1 = M(\Sigma^*) - M(\Delta) = 1385\text{ MeV}/c^2 - 1232\text{ MeV}/c^2 = \mathbf{153\text{ MeV}/c^2}$$
$$\Delta M_2 = M(\Xi^*) - M(\Sigma^*) = 1532\text{ MeV}/c^2 - 1385\text{ MeV}/c^2 = \mathbf{147\text{ MeV}/c^2}$$
The two splittings differ by only $6\text{ MeV}/c^2$ ($< 4\%$), strongly confirming the Gell-Mann-Okubo equal-spacing rule $\Delta M \approx \text{constant}$.

**(b) Theoretical Prediction of $M(\Omega^-)$:**
Average mass splitting:
$$\langle \Delta M \rangle = \frac{\Delta M_1 + \Delta M_2}{2} = \frac{153 + 147}{2} = \mathbf{150\text{ MeV}/c^2}$$
Predicting the mass of $\Omega^-$:
$$M(\Omega^-) = M(\Xi^*) + \langle \Delta M \rangle = 1532\text{ MeV}/c^2 + 150\text{ MeV}/c^2 = \mathbf{1682\text{ MeV}/c^2}$$
*(If using $\Delta M_2 = 147\text{ MeV}/c^2$ directly: $M(\Omega^-) = 1532 + 147 = 1679\text{ MeV}/c^2$.)*

**(c) Comparison with PDG Value:**
$$M_{\text{PDG}}(\Omega^-) = 1672.45\text{ MeV}/c^2$$
Discrepancy:
$$\Delta M_{\text{diff}} = 1682 - 1672.45 = +9.55\text{ MeV}/c^2$$
Percentage error:
$$\text{Error} = \frac{|1682 - 1672.45|}{1672.45} \times 100\% = \frac{9.55}{1672.45} \times 100\% \approx \mathbf{0.57\%}$$
The theoretical prediction matches the physical measurement to within **$0.57\%$**, one of the most stunning triumphs of symmetry in 20th-century physics."""
        },
        {
            "id": "nuc2-prob-8-2",
            "title": "Electroweak Unification Relations, W/Z Masses and the Fermi Constant",
            "statement": r"""In the Glashow-Weinberg-Salam electroweak model, the masses of the intermediate vector bosons are related to the gauge couplings and the Higgs VEV $v$ by:
$$M_W = \frac{1}{2} g v, \qquad M_Z = \frac{M_W}{\cos\theta_W}$$
and the low-energy Fermi coupling constant is given at tree level by:
$$\frac{G_F}{\sqrt{2}} = \frac{g^2}{8 M_W^2} = \frac{1}{2 v^2}$$
Given the experimental values $G_F = 1.1663787 \times 10^{-5}\text{ GeV}^{-2}$, $M_Z = 91.1876\text{ GeV}/c^2$, and the on-shell weak mixing parameter $\sin^2\theta_W = 0.2229$:
(a) Calculate the vacuum expectation value of the Higgs field $v$ in $\text{GeV}$.
(b) Calculate the predicted tree-level mass of the charged $W^\pm$ boson $M_W$ in $\text{GeV}/c^2$.
(c) Determine the $SU(2)_L$ gauge coupling constant $g$ and the fine structure constant $\alpha = \frac{e^2}{4\pi} = \frac{g^2 \sin^2\theta_W}{4\pi}$ at the electroweak scale.""",
            "solution": r"""**(a) Higgs Vacuum Expectation Value $v$:**
$$v = \frac{1}{\sqrt{\sqrt{2} G_F}} = \left( \sqrt{2} \times 1.1663787 \times 10^{-5}\text{ GeV}^{-2} \right)^{-1/2}$$
$$\sqrt{2} G_F = 1.4142136 \times 1.1663787 \times 10^{-5} \approx 1.649508 \times 10^{-5}\text{ GeV}^{-2}$$
$$v = \frac{1}{\sqrt{1.649508 \times 10^{-5}}} = \frac{1}{0.0040614} \approx \mathbf{246.22\text{ GeV}}$$
The Higgs vacuum expectation value is **$246.22\text{ GeV}$**.

**(b) Predicted $W^\pm$ Boson Mass:**
Using the tree-level relation $\cos\theta_W = \sqrt{1 - \sin^2\theta_W}$:
$$\cos\theta_W = \sqrt{1 - 0.2229} = \sqrt{0.7771} \approx 0.88153$$
The $W$ mass is:
$$M_W = M_Z \cos\theta_W = 91.1876\text{ GeV}/c^2 \times 0.88153 \approx \mathbf{80.385\text{ GeV}/c^2}$$
This matches the experimental world average $M_W^{\text{exp}} = 80.379 \pm 0.012\text{ GeV}/c^2$ with outstanding sub-per-mille precision!

**(c) Electroweak Gauge Couplings:**
From $M_W = \frac{1}{2} g v$:
$$g = \frac{2 M_W}{v} = \frac{2 \times 80.385\text{ GeV}}{246.22\text{ GeV}} \approx \mathbf{0.6529}$$
Electromagnetic fine structure constant at the $M_Z$ scale:
$$\alpha(M_Z) = \frac{g^2 \sin^2\theta_W}{4\pi} = \frac{(0.6529)^2 \times 0.2229}{4\pi} = \frac{0.4263 \times 0.2229}{12.5664} = \frac{0.09502}{12.5664} \approx 0.007561 \approx \mathbf{\frac{1}{128.2}}$$
At the electroweak energy scale $\sim M_Z$, vacuum polarization screens the electric charge less, so the effective coupling increases from its low-energy Thomson limit ($\alpha \approx 1/137$) to $\alpha(M_Z) \approx 1/128$!"""
        },
        {
            "id": "nuc2-prob-8-3",
            "title": "Two-Flavor Neutrino Oscillation in the KamLAND Reactor Experiment",
            "statement": r"""The KamLAND experiment in Japan measured electron antineutrino ($\bar{\nu}_e$) disappearance from dozens of nuclear power reactors at an average flux-weighted baseline of $L = 180\text{ km}$.
In the two-flavor approximation, the survival probability of electron antineutrinos of energy $E$ is:
$$P(\bar{\nu}_e \to \bar{\nu}_e) = 1 - \sin^2(2\theta) \sin^2\left( 1.267 \frac{\Delta m^2 [\text{eV}^2] L [\text{km}]}{E [\text{MeV}]} \right)$$
Assume the solar-reactor oscillation parameters $\sin^2(2\theta) = 0.86$ and $\Delta m^2 = 7.50 \times 10^{-5}\text{ eV}^2$.
(a) Evaluate the survival probability for reactor antineutrinos with energy $E = 3.5\text{ MeV}$.
(b) Calculate the oscillation phase $\Phi \equiv 1.267 \frac{\Delta m^2 L}{E}$ and determine the specific neutrino energy $E_{\text{min}}$ at which the survival probability reaches its first local minimum.
(c) Calculate the survival probability at that minimum $P_{\text{min}}$.""",
            "solution": r"""**(a) Survival Probability for $E = 3.5\text{ MeV}$:**
Evaluate the argument of the sine function:
$$\Phi = 1.267 \frac{\Delta m^2 [\text{eV}^2] L [\text{km}]}{E [\text{MeV}]} = 1.267 \times \frac{(7.50 \times 10^{-5}) \times 180}{3.5}$$
Numerator:
$$1.267 \times 7.50 \times 10^{-5} \times 180 = 1.267 \times 0.01350 = 0.0171045$$
Dividing by $E = 3.5\text{ MeV}$:
$$\Phi = \frac{0.0171045}{3.5} \approx 0.004887\text{ rad ... wait!}$$
Let's verify the constant $1.267$:
$$\frac{\Delta m^2 c^4 L}{4 \hbar c E} = \frac{\Delta m^2 [\text{eV}^2] \times 10^3\text{ m}}{4 \times (1.97327 \times 10^{-7}\text{ eV}\cdot\text{m}) \times (E [\text{MeV}] \times 10^6\text{ eV})} = \frac{10^3}{4 \times 0.197327} \frac{\Delta m^2 [\text{eV}^2] L [\text{km}]}{E [\text{MeV}]} = 1266.9 \frac{\Delta m^2 [\text{eV}^2] L [\text{km}]}{E [\text{MeV}]}$$
Notice that $1.267$ applies when $L$ is in $\text{km}$ and $E$ is in $\text{GeV}$, OR when using $L$ in $\text{m}$ and $E$ in $\text{MeV}$.
When $L$ is in $\text{km}$ and $E$ is in $\text{MeV}$, the conversion factor is **$1267$**!
Let us re-evaluate with the correct factor $1267$:
$$\Phi = 1267 \times \frac{(7.50 \times 10^{-5}) \times 180}{3.5} = \frac{1267 \times 0.01350}{3.5} = \frac{17.1045}{3.5} \approx \mathbf{4.887\text{ rad}}$$
In degrees:
$$\Phi = 4.887 \times \frac{180^\circ}{\pi} \approx 280.0^\circ$$
Evaluating the sine:
$$\sin(4.887\text{ rad}) \approx -0.9848 \implies \sin^2(4.887) \approx (-0.9848)^2 \approx 0.9698$$
Survival probability:
$$P(\bar{\nu}_e \to \bar{\nu}_e) = 1 - 0.86 \times 0.9698 = 1 - 0.8340 \approx \mathbf{0.166} = \mathbf{16.6\%}$$
Only $16.6\%$ of the electron antineutrinos survive at $E = 3.5\text{ MeV}$; over $83\%$ have oscillated away into muon and tau antineutrinos!

**(b) Energy of First Minimum $E_{\text{min}}$:**
The first oscillation minimum occurs when the phase reaches $\Phi = \frac{\pi}{2} \approx 1.5708\text{ rad}$:
$$1267 \frac{\Delta m^2 L}{E_{\text{min}}} = \frac{\pi}{2} \implies E_{\text{min}} = \frac{1267 \Delta m^2 L}{\pi / 2} = \frac{2 \times 17.1045}{\pi} = \frac{34.209}{3.14159} \approx \mathbf{10.89\text{ MeV}}$$
For higher oscillation peaks, $\Phi = 3\pi/2 \approx 4.712\text{ rad}$:
$$E_{\text{min, 2}} = \frac{17.1045}{4.712} \approx \mathbf{3.63\text{ MeV}}$$
which is very close to our $3.5\text{ MeV}$ probe point!

**(c) Survival Probability at Minimum:**
At any oscillation minimum where $\sin^2\Phi = 1$:
$$P_{\text{min}} = 1 - \sin^2(2\theta)(1) = 1 - 0.86 = \mathbf{0.140} = \mathbf{14.0\%}$$
The survival probability drops to a minimum of **$14.0\%$**, directly confirming reactor antineutrino disappearance and pinning down $\Delta m_{21}^2$."""
        }
    ]
}

with open("nuc2_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7_data, f, indent=2, ensure_ascii=False)

with open("nuc2_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8_data, f, indent=2, ensure_ascii=False)

print("nuc2_u7.json and nuc2_u8.json successfully written!")
