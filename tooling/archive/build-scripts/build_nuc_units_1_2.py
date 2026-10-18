import json

# ==========================================
# UNIT 1: Nuclear Structure, Masses, Radii & Nuclear Models
# ==========================================
u1 = {
    "unitNumber": 1,
    "unitId": "unit1-nuclear-properties",
    "title": "Nuclear Structure, Masses, Radii & Nuclear Models",
    "description": "Comprehensive foundation of nuclear physics: subatomic constitution, high-energy electron scattering, charge radius measurement, mass defect, binding energy systematics, semi-empirical mass formula (SEMF), valley of beta stability, electromagnetic moments (Schmidt lines, quadrupole deformation), nuclear force characteristics, and comparative evaluation of the Liquid Drop and Shell Models.",
    "sections": [
        {
            "id": "nuc-1-1",
            "title": "Nuclear Constitution, Quarks, Nucleons & Charge Radii",
            "content": r"""<h4>1. Fundamental Constitution of the Atomic Nucleus</h4>
<p>An atomic nucleus is a tightly bound quantum many-body system composed of $A$ nucleons: $Z$ positively charged <strong>protons</strong> and $N = A - Z$ electrically neutral <strong>neutrons</strong>. Protons and neutrons are not point particles, but composite hadrons belonging to the <strong>baryon</strong> family, each formed by three valence quarks bound via the strong interaction mediated by gluons ($SU(3)_C$ color gauge theory):</p>
<ul>
<li><strong>Proton ($p$):</strong> Valence quark composition $uud$ (two up quarks, one down quark). Net electric charge $Q = 2(+2/3 e) + (-1/3 e) = +1 e$. Rest mass $m_p = 938.272\text{ MeV}/c^2 = 1.67262 \times 10^{-27}\text{ kg} = 1.007276\text{ u}$. Intrinsic spin $s = 1/2$.</li>
<li><strong>Neutron ($n$):</strong> Valence quark composition $udd$ (one up quark, two down quarks). Net electric charge $Q = +2/3 e + 2(-1/3 e) = 0$. Rest mass $m_n = 939.565\text{ MeV}/c^2 = 1.67493 \times 10^{-27}\text{ kg} = 1.008665\text{ u}$. Intrinsic spin $s = 1/2$. Free neutrons undergo beta decay ($n \to p + e^- + \bar{\nu}_e$) with a mean lifetime $\tau \approx 879.4\text{ s}$.</li>
</ul>

<h4>2. Nuclear Size & High-Energy Electron Scattering</h4>
<p>Because the nuclear strong force saturates, nuclear matter exhibits nearly constant volume density $\rho_0 \approx 0.17\text{ nucleons/fm}^3 = 2.7 \times 10^{17}\text{ kg/m}^3$. Consequently, the mean nuclear charge radius $R$ scales with the cube root of the mass number $A$:</p>
<div class="math-display">
$$R = R_0 A^{1/3} \quad (R_0 \approx 1.20 - 1.25\text{ fm})$$
</div>
<p>The definitive experimental measurement of the spatial nuclear charge density $\rho(r)$ was conducted by Robert Hofstadter (1950s) utilizing <strong>high-energy elastic electron scattering</strong> ($E_e \sim 200 - 1000\text{ MeV}$, where de Broglie wavelength $\lambda = hc/E \sim 0.5 - 2\text{ fm}$ is smaller than the nuclear radius). In the first Born approximation, the differential scattering cross-section is the Rutherford cross-section modulated by the squared nuclear <strong>Form Factor</strong> $F(\vec{q})$:</p>
<div class="math-display">
$$\left(\frac{d\sigma}{d\Omega}\right) = \left(\frac{d\sigma}{d\Omega}\right)_{\text{Mott}} |F(\vec{q})|^2, \quad F(\vec{q}) = \frac{1}{Z e} \int \rho(\vec{r}) e^{i \vec{q}\cdot\vec{r}/\hbar} d^3r$$
</div>
<p>where $\vec{q} = \vec{p} - \vec{p}'$ is the momentum transfer. The experimental form factor maps directly to the <strong>Fermi Two-Parameter Charge Distribution</strong>:</p>
<div class="math-display">
$$\rho(r) = \frac{\rho_0}{1 + e^{(r - c)/a}}$$
</div>
<p>where $c \approx 1.18 A^{1/3}\text{ fm}$ is the half-density radius, and $a \approx 0.54\text{ fm}$ is the surface diffuseness parameter (corresponding to a 90%-to-10% surface thickness $t \approx 4.4 a \approx 2.4\text{ fm}$).</p>

<h4>3. Muonic X-Ray Atoms</h4>
<p>In a <strong>muonic atom</strong>, a negative muon ($\mu^-$, mass $m_\mu \approx 206.77 m_e$) replaces an orbital electron. Because the Bohr radius scales inversely with mass ($a_\mu = \frac{m_e}{m_\mu} a_0 \approx \frac{0.529\text{ \AA}}{207} \approx 256\text{ fm}$), the lowest muonic orbits ($1s$) reside largely <em>inside</em> the nuclear volume. The severe perturbation of the Coulomb potential inside the charge sphere shifts the $2p \to 1s$ Lyman muonic X-ray transition energies by hundreds of keV, providing a complementary sub-femtometer measurement of the nuclear charge radius.</p>"""
        },
        {
            "id": "nuc-1-2",
            "title": "Mass Defect, Binding Energy & Mirror Nuclei Coulomb Energy",
            "simulation": "nuc-binding-energy-sim",
            "content": r"""<h4>1. Mass Defect and Nuclear Binding Energy</h4>
<p>When $Z$ free protons and $N$ free neutrons coalesce to synthesize a bound nucleus $^A_Z\text{X}$, total energy conservation dictates that a substantial quantity of energy, the <strong>nuclear binding energy</strong> $B(A, Z)$, is liberated. By Einstein's mass-energy equivalence $E = m c^2$, the rest mass of the bound neutral atom $M(A, Z)$ is strictly less than the sum of its isolated constituents:</p>
<div class="math-display">
$$\Delta m = Z m_p + N m_n - M(A, Z) = Z m(^1\text{H}) + (A - Z) m_n - M(A, Z)$$
</div>
<div class="math-display">
$$B(A, Z) = \Delta m \cdot c^2 = \left[ Z m(^1\text{H}) + (A - Z) m_n - M(A, Z) \right] c^2$$
</div>
<p>Using the atomic mass unit definition ($1\text{ u} \equiv \frac{1}{12} M(^{12}\text{C}) = 931.494\text{ MeV}/c^2$), the binding energy per nucleon is defined as:</p>
<div class="math-display">
$$f = \frac{B(A, Z)}{A}$$
</div>

<h4>2. The Binding Energy per Nucleon Curve</h4>
<p>Plotting $B/A$ against mass number $A$ reveals the fundamental energetic landscape of the universe:</p>
<ul>
<li><strong>Light Nuclei ($A < 20$):</strong> Rapid rise with sharp local stability spikes at alpha-conjugate even-even nuclei ($^4\text{He}$, $^8\text{Be}$, $^{12}\text{C}$, $^{16}\text{O}$, $^{20}\text{Ne}$), with $^4\text{He}$ displaying $B/A \approx 7.07\text{ MeV/nucleon}$.</li>
<li><strong>Broad Maximum ($A \approx 56 - 62$):</strong> The curve attains its global peak at $^{56}\text{Fe}$ ($B/A \approx 8.790\text{ MeV/nucleon}$) and $^{62}\text{Ni}$ ($B/A \approx 8.795\text{ MeV/nucleon}$), representing the most thermodynamically stable nuclear matter.</li>
<li><strong>Heavy Nuclei ($A > 100$):</strong> Gradual monotonic descent toward $B/A \approx 7.5\text{ MeV/nucleon}$ at $^{238}\text{U}$, driven by the disruptive Coulomb repulsion of $Z^2$ protons scaling faster than short-range nuclear attraction.</li>
<li><strong>Nuclear Power Consequences:</strong>
<ul>
<li><strong>Nuclear Fusion:</strong> Combining light nuclei ($A \ll 56$, e.g., $\text{D} + \text{T} \to {^4\text{He}} + n$) moves up the steep left slope, releasing enormous kinetic energy.</li>
<li><strong>Nuclear Fission:</strong> Splitting a heavy actinide ($A \sim 235 \to A_1, A_2 \sim 118$) moves up the right slope toward the iron peak, liberating $\approx 200\text{ MeV}$ per fission event.</li>
</ul></li>
</ul>

<h4>3. Coulomb Displacement Energy in Mirror Nuclei</h4>
<p><strong>Mirror nuclei</strong> are pairs of isobars related by exchanging the numbers of protons and neutrons: $Z_1 = N_2$ and $N_1 = Z_2$ (e.g., $^{15}_7\text{N}$ and $^{15}_8\text{O}$, or $^{27}_{13}\text{Al}$ and $^{27}_{14}\text{Si}$). Because the strong nuclear interaction is charge-symmetric, the difference in their binding energies is due solely to the difference in electrostatic Coulomb self-energy $E_C$:</p>
<div class="math-display">
$$\Delta E_C = E_C(Z_1) - E_C(Z_2) = \frac{3}{5} \frac{e^2}{4\pi\varepsilon_0 R} \left[ Z_1(Z_1 - 1) - Z_2(Z_2 - 1) \right]$$
</div>
<p>For isobars differing by $\Delta Z = 1$ ($Z_1 = Z$ and $Z_2 = Z - 1$):</p>
<div class="math-display">
$$\Delta E_C = \frac{3}{5} \frac{e^2}{4\pi\varepsilon_0 R} [2Z - 1] = \frac{3}{5} \frac{e^2}{4\pi\varepsilon_0 (R_0 A^{1/3})} (2Z - 1)$$
</div>
<p>Measuring the beta-decay end-point energy between mirror nuclei provides an independent experimental method to determine the nuclear radius parameter $R_0 \approx 1.20\text{ fm}$.</p>"""
        },
        {
            "id": "nuc-1-3",
            "title": "The Semi-Empirical Mass Formula (SEMF) & Valley of Stability",
            "content": r"""<h4>1. The Weizsäcker Semi-Empirical Mass Formula</h4>
<p>Carl Friedrich von Weizsäcker (1935) modeled the nucleus as an incompressible, charged liquid drop of nuclear fluid. The total nuclear binding energy $B(A, Z)$ is parameterized by five physical terms:</p>
<div class="math-display">
$$B(A, Z) = a_v A - a_s A^{2/3} - a_c \frac{Z(Z-1)}{A^{1/3}} - a_a \frac{(A - 2Z)^2}{A} + \delta(A, Z)$$
</div>
<p>where the standard empirical coefficients (in MeV) are:</p>
<ol>
<li><strong>Volume Term ($+ a_v A$, $a_v \approx 15.75\text{ MeV}$):</strong> Reflects the short-range, saturating nature of nuclear forces. Each nucleon interacts only with its nearest neighbors, contributing a constant volume energy proportional to $A$.</li>
<li><strong>Surface Term ($- a_s A^{2/3}$, $a_s \approx 17.8\text{ MeV}$):</strong> Nucleons at the nuclear surface have fewer neighbors than interior nucleons, reducing binding energy proportional to the nuclear surface area $4\pi R^2 \propto A^{2/3}$ (analogous to surface tension).</li>
<li><strong>Coulomb Term ($- a_c \frac{Z(Z-1)}{A^{1/3}}$, $a_c \approx 0.711\text{ MeV}$):</strong> Mutual electrostatic repulsion among all $Z(Z-1)/2$ proton pairs distributed uniformly within a sphere of radius $R = R_0 A^{1/3}$:
<div class="math-display">
$$E_C = \frac{3}{5} \frac{Z(Z-1) e^2}{4\pi\varepsilon_0 R_0 A^{1/3}} = a_c \frac{Z(Z-1)}{A^{1/3}}$$
</div></li>
<li><strong>Asymmetry Term ($- a_a \frac{(A - 2Z)^2}{A}$, $a_a \approx 23.7\text{ MeV}$):</strong> A purely quantum mechanical consequence of the Pauli exclusion principle. Displacing protons into neutron levels increases total Fermi energy proportional to $(N - Z)^2/A = (A - 2Z)^2/A$.</li>
<li><strong>Pairing Term ($\delta(A, Z)$):</strong> Arises from the spin-pairing attraction between identical nucleons in time-reversed orbits:
<div class="math-display">
$$\delta(A, Z) = \begin{cases} + a_p A^{-1/2} \text{ (or } + a_p A^{-3/4}), & \text{even } Z, \text{even } N \text{ (even-even: most stable)} \\ 0, & \text{odd } A \text{ (even-odd or odd-even)} \\ - a_p A^{-1/2} \text{ (or } - a_p A^{-3/4}), & \text{odd } Z, \text{odd } N \text{ (odd-odd: least stable)} \end{cases}$$
</div>
<p>where $a_p \approx 11.2\text{ MeV}$ (or $a_p \approx 34\text{ MeV}$ with $A^{-3/4}$).</p></li>
</ol>

<h4>2. The Valley of Beta Stability</h4>
<p>For a fixed mass number $A$, the binding energy is a quadratic parabola in $Z$. The most stable isobar $Z_0$ corresponds to the maximum binding energy: $\left.\frac{\partial B(A, Z)}{\partial Z}\right|_{Z_0} = 0$:</p>
<div class="math-display">
$$- \frac{a_c (2Z_0 - 1)}{A^{1/3}} + \frac{4 a_a (A - 2Z_0)}{A} = 0 \implies Z_0 = \frac{A}{2 + \frac{a_c}{2 a_a} A^{2/3}} \approx \frac{A}{2 + 0.015 A^{2/3}}$$
</div>
<ul>
<li>For light nuclei ($A \ll 40$), the Coulomb term is negligible ($A^{2/3} \ll 1$), giving $Z_0 \approx A/2$ ($N \approx Z$).</li>
<li>For heavy nuclei ($A \sim 200$), Coulomb repulsion shifts the valley of stability toward neutron-rich compositions: $Z_0 \approx 82$ for $A = 208$, giving $N/Z \approx 1.54$.</li>
</ul>"""
        },
        {
            "id": "nuc-1-4",
            "title": "Nuclear Spin, Parity, Magnetic Moments & Quadrupole Moments",
            "simulation": "nuc-quadrupole-deformation-sim",
            "content": r"""<h4>1. Nuclear Total Angular Momentum (Nuclear Spin $\vec{I}$) & Parity $\pi$</h4>
<p>The total angular momentum of a nucleus in its rest frame, conventionally designated as the <strong>nuclear spin</strong> $\vec{I}$, is the vector sum of individual nucleon orbital angular momenta $\vec{l}_i$ and intrinsic spin angular momenta $\vec{s}_i$:</p>
<div class="math-display">
$$\vec{I} = \sum_{i=1}^A (\vec{l}_i + \vec{s}_i)$$
</div>
<p>Nuclear state parities $\pi = \pm 1$ reflect spatial inversion symmetry: $\psi(-\vec{r}) = \pi \psi(\vec{r})$, where single-particle states have parity $\pi = (-1)^l$. Total nuclear parity is the product over all occupied single-particle orbitals: $\pi = \prod_{i=1}^A (-1)^{l_i}$.</p>
<ul>
<li><strong>Even-Even Nuclei ($Z$ even, $N$ even):</strong> In the ground state, all nucleon spins pair off identically in time-reversed orbits ($J^\pi = 0^+$ without exception).</li>
<li><strong>Odd-$A$ Nuclei:</strong> Spin and parity are determined entirely by the single unpaired valence nucleon: $I = j_{\text{val}}$, $\pi = (-1)^{l_{\text{val}}}$.</li>
<li><strong>Odd-Odd Nuclei:</strong> Coupling of unpaired proton and neutron: $|j_p - j_n| \le I \le j_p + j_n$ (Nordheim's empirical coupling rules).</li>
</ul>

<h4>2. Nuclear Magnetic Dipole Moments & Schmidt Limits</h4>
<p>The nuclear magnetic moment operator is expressed in units of the <strong>nuclear magneton</strong> $\mu_N = \frac{e\hbar}{2m_p} \approx 5.05078 \times 10^{-27}\text{ J/T}$ (which is $\approx 1/1836$ of the Bohr magneton $\mu_B$):</p>
<div class="math-display">
$$\vec{\mu} = \sum_{i=1}^A \left[ g_l^{(i)} \vec{l}_i + g_s^{(i)} \vec{s}_i \right] \mu_N$$
</div>
<p>where the bare nucleon $g$-factors are:</p>
<ul>
<li>Proton: $g_l = 1$, $g_s = +5.5857$</li>
<li>Neutron: $g_l = 0$, $g_s = -3.8263$</li>
</ul>
<p>In the extreme single-particle shell model, the magnetic moment of an odd-$A$ nucleus is generated entirely by the single valence nucleon, yielding the <strong>Schmidt limits</strong>:</p>
<ul>
<li>For $j = l + 1/2$: $\mu = \left[ (j - 1/2) g_l + \frac{1}{2} g_s \right] \mu_N$</li>
<li>For $j = l - 1/2$: $\mu = \frac{j}{j+1} \left[ (j + 3/2) g_l - \frac{1}{2} g_s \right] \mu_N$</li>
</ul>

<h4>3. Electric Quadrupole Moment $Q$ & Nuclear Deformation</h4>
<p>The nuclear electric quadrupole moment $Q$ measures the deviation of the nuclear charge distribution $\rho(\vec{r})$ from spherical symmetry:</p>
<div class="math-display">
$$e Q = \int \rho(\vec{r}) (3 z^2 - r^2) d^3r = \int \rho(\vec{r}) r^2 (3\cos^2\theta - 1) d^3r$$
</div>
<ul>
<li><strong>Spherical Nucleus ($Q = 0$):</strong> $\langle z^2 \rangle = \langle x^2 \rangle = \langle y^2 \rangle = \frac{1}{3}\langle r^2 \rangle$. Occurs for all closed-shell magic nuclei and all $I = 0$ or $I = 1/2$ states.</li>
<li><strong>Prolate Ellipsoid ($Q > 0$):</strong> Elongated along the spin axis like an American football ($z_{\text{axis}} > x, y$). Common in rare-earth and actinide deformed nuclei.</li>
<li><strong>Oblate Ellipsoid ($Q < 0$):</strong> Flattened along the spin axis like a discus ($z_{\text{axis}} < x, y$).</li>
</ul>"""
        },
        {
            "id": "nuc-1-5",
            "title": "Nuclear Forces & Yukawa Meson Exchange Theory",
            "content": r"""<h4>1. Empirical Characteristics of the Strong Nuclear Force</h4>
<p>Detailed scattering experiments ($p$-$p$ and $n$-$p$) and deuteron binding properties reveal seven defining characteristics of the nuclear force:</p>
<ol>
<li><strong>Short Range:</strong> Acts strongly across $r \approx 1 - 2\text{ fm}$, vanishing exponentially beyond $r \sim 2.5\text{ fm}$. Possesses a hard repulsive core at $r < 0.5\text{ fm}$ preventing nuclear collapse.</li>
<li><strong>Enormous Strength:</strong> At $r \approx 1\text{ fm}$, it is $\sim 100$ times stronger than electromagnetic Coulomb repulsion.</li>
<li><strong>Charge Independence:</strong> The nuclear interaction between two nucleons in the same quantum state is identical: $V_{pp} = V_{nn} = V_{np}$ (isospin symmetry $T = 1$).</li>
<li><strong>Charge Symmetry:</strong> Invariant under proton-neutron reflection ($V_{pp} = V_{nn}$).</li>
<li><strong>Spin Dependence:</strong> The force is significantly stronger when nucleon spins are aligned parallel ($S = 1$, triplet, as in the bound deuteron $^2\text{H}$) than antiparallel ($S = 0$, singlet, where di-proton and di-neutron are unbound).</li>
<li><strong>Non-Central (Tensor) Force:</strong> Contains a non-central component $S_{12} = \frac{3}{r^2}(\vec{\sigma}_1\cdot\vec{r})(\vec{\sigma}_2\cdot\vec{r}) - \vec{\sigma}_1\cdot\vec{\sigma}_2$, explaining the non-zero electric quadrupole moment of the deuteron ($Q_d = +0.00286\text{ b}$) and $D$-state orbital mixing.</li>
<li><strong>Saturation:</strong> Each nucleon interacts only with immediate nearest neighbors, keeping $B/A$ approximately constant.</li>
</ol>

<h4>2. Yukawa's Meson Exchange Theory (1935)</h4>
<p>Hideki Yukawa proposed that the strong nuclear force is mediated by the virtual exchange of massive scalar bosons called <strong>pions</strong> ($\pi^\pm, \pi^0$). In relativistic quantum field theory, the static wave equation for a scalar field $\phi(r)$ generated by a point nucleon source is the Klein-Gordon equation:</p>
<div class="math-display">
$$\left( \nabla^2 - \frac{m_\pi^2 c^2}{\hbar^2} \right) \phi(r) = - g \delta(\vec{r})$$
</div>
<p>The spherically symmetric solution is the <strong>Yukawa Potential</strong>:</p>
<div class="math-display">
$$V(r) = - g^2 \frac{e^{- r / \lambda_\pi}}{r} = - g^2 \frac{e^{- \mu r}}{r}$$
</div>
<p>where $\lambda_\pi = \frac{\hbar}{m_\pi c}$ is the Compton wavelength of the mediating pion. Estimating the force range as $R \approx 1.4\text{ fm}$ using the Heisenberg uncertainty principle ($\Delta E \Delta t \sim (m_\pi c^2) (R/c) \sim \hbar$):</p>
<div class="math-display">
$$m_\pi \approx \frac{\hbar}{R c} = \frac{197.3\text{ MeV}\cdot\text{fm}}{(1.4\text{ fm}) c^2} \approx 140\text{ MeV}/c^2$$
</div>
<p>Yukawa's predicted pion was discovered experimentally in cosmic rays in 1947 with rest masses $m_{\pi^\pm} = 139.57\text{ MeV}/c^2$ and $m_{\pi^0} = 134.98\text{ MeV}/c^2$.</p>"""
        },
        {
            "id": "nuc-1-6",
            "title": "Nuclear Models: Liquid Drop vs. The Nuclear Shell Model",
            "simulation": "nuc-shell-model-levels-sim",
            "content": r"""<h4>1. The Nuclear Liquid Drop Model</h4>
<p>The liquid drop model treats the nucleus collectively as a droplet of incompressible quantum fluid. It accurately predicts:</p>
<ul>
<li>Nuclear binding energies across the chart of nuclides via the SEMF.</li>
<li>Low-lying collective quadrupole ($\lambda = 2$) and octupole ($\lambda = 3$) vibrational excitations.</li>
<li>The mechanism of induced nuclear fission (Bohr-Wheeler theory) through liquid drop ellipsoidal surface distortions.</li>
</ul>
<p>However, it completely fails to explain the dramatic stability spikes observed at specific nucleon numbers.</p>

<h4>2. Experimental Evidence for Magic Numbers</h4>
<p>Nuclei possessing specific numbers of protons or neutrons—<strong>Magic Numbers</strong>: $2, 8, 20, 28, 50, 82, 126$—exhibit extraordinary stability:</p>
<ul>
<li>Abrupt discontinuities in separation energies $S_n$ and $S_p$ (analogous to atomic noble gas ionization potentials).</li>
<li>Small neutron capture cross-sections $\sigma_{(n,\gamma)}$.</li>
<li>Doubly magic nuclei ($^4_2\text{He}_2$, $^{16}_8\text{O}_8$, $^{40}_{20}\text{Ca}_{20}$, $^{48}_{20}\text{Ca}_{28}$, $^{208}_{82}\text{Pb}_{126}$) possess exceptionally large binding energies and spherical ground states ($Q = 0$).</li>
</ul>

<h4>3. The Nuclear Shell Model & Spin-Orbit Coupling</h4>
<p>Maria Goeppert-Mayer and J. Hans D. Jensen (1949, Nobel Prize 1963) resolved the magic number sequence by introducing a strong attractive <strong>spin-orbit interaction</strong> into the 3D central potential (Woods-Saxon or Harmonic Oscillator):</p>
<div class="math-display">
$$\hat{H} = \hat{H}_0 + V_{ls}(r) \vec{l} \cdot \vec{s}$$
</div>
<p>Because $\vec{j} = \vec{l} + \vec{s}$, we have $\vec{j}^2 = \vec{l}^2 + \vec{s}^2 + 2\vec{l}\cdot\vec{s}$, which gives:</p>
<div class="math-display">
$$\langle \vec{l} \cdot \vec{s} \rangle = \frac{1}{2} [j(j+1) - l(l+1) - s(s+1)] = \begin{cases} +\frac{l}{2}, & j = l + 1/2 \\ -\frac{l+1}{2}, & j = l - 1/2 \end{cases}$$
</div>
<p>The energy splitting between the two spin-orbit partner states is:</p>
<div class="math-display">
$$\Delta E_{ls} = \left( l + \frac{1}{2} \right) \hbar^2 \langle V_{ls} \rangle$$
</div>
<p>Because $V_{ls} < 0$, the $j = l + 1/2$ state is shifted downward in energy. For large orbital angular momentum $l$ (e.g., $1f_{7/2}$, $1g_{9/2}$, $1h_{11/2}$, $1i_{13/2}$), the downward shift is so massive that the $j = l + 1/2$ level drops across the major oscillator shell gap into the shell below. These "intruder states" produce major shell closures at precisely <strong>28, 50, 82, and 126</strong>, reproducing the complete sequence of nuclear magic numbers.</p>"""
        }
    ],
    "problems": [
        {
            "id": "nuc-p-1-1",
            "title": "Nuclear Radius and Binding Energy Calculation for Iron-56",
            "statement": "Iron-56 ($^{56}_{26}\\text{Fe}$) has an atomic mass of $M = 55.9349375 \\text{ u}$. The rest masses of a neutral hydrogen atom and a free neutron are $m(^1\\text{H}) = 1.007825 \\text{ u}$ and $m_n = 1.008665 \\text{ u}$. (a) Calculate the nuclear charge radius $R$ assuming $R_0 = 1.22 \\text{ fm}$. (b) Determine the mass defect $\\Delta m$ in $\\text{u}$ and total binding energy $B$ in $\\text{MeV}$. (c) Calculate the binding energy per nucleon $B/A$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Nuclear Radius R",
                    "math": r"R = R_0 A^{1/3} = (1.22\text{ fm}) (56)^{1/3} = (1.22\text{ fm}) (3.82586) \approx 4.668\text{ fm} = 4.67 \times 10^{-15}\text{ m}",
                    "explanation": "Evaluate R using the standard nuclear scaling law with A = 56."
                },
                {
                    "stepName": "Step 2: Calculate the Mass Defect Delta m",
                    "math": r"\Delta m = Z m(^1\text{H}) + (A - Z) m_n - M(^{56}\text{Fe}) = 26(1.007825\text{ u}) + 30(1.008665\text{ u}) - 55.934938\text{ u} = 26.203450\text{ u} + 30.259950\text{ u} - 55.934938\text{ u} = 56.463400\text{ u} - 55.934938\text{ u} = 0.528462\text{ u}",
                    "explanation": "Compute the difference between the constituent masses and the bound atomic mass."
                },
                {
                    "stepName": "Step 3: Convert Mass Defect to Binding Energy in MeV",
                    "math": r"B = \Delta m \times 931.494\text{ MeV/u} = (0.528462\text{ u}) \times (931.494\text{ MeV/u}) \approx 492.269\text{ MeV}",
                    "explanation": "Multiply by the atomic mass energy conversion factor."
                },
                {
                    "stepName": "Step 4: Compute the Binding Energy per Nucleon B / A",
                    "math": r"\frac{B}{A} = \frac{492.269\text{ MeV}}{56} \approx 8.7905\text{ MeV/nucleon}",
                    "explanation": "Divide total binding energy by mass number A = 56. This matches the peak of the experimental binding energy curve."
                }
            ],
            "answer": "R = 4.67 \\text{ fm}, \\quad \\Delta m = 0.5285 \\text{ u}, \\quad B = 492.27 \\text{ MeV}, \\quad B/A = 8.791 \\text{ MeV/nucleon}"
        },
        {
            "id": "nuc-p-1-2",
            "title": "Coulomb Displacement Energy and Radius of Mirror Pair Nitrogen-15 and Oxygen-15",
            "statement": "The mirror pair $^{15}_7\\text{N}$ and $^{15}_8\\text{O}$ differ by one proton ($Z_1 = 8, Z_2 = 7$). The atomic mass difference is $\\Delta M = M(^{15}\\text{O}) - M(^{15}\\text{N}) = 2.754 \\text{ MeV}/c^2$. The neutron-proton mass difference is $(m_n - m_H)c^2 = 0.782 \\text{ MeV}$. (a) Calculate the experimental Coulomb displacement energy $\\Delta E_C$. (b) Using the uniform sphere Coulomb model $\\Delta E_C = \\frac{3e^2}{5(4\\pi\\varepsilon_0)R}(2Z - 1)$, determine the nuclear radius $R$ and the radius parameter $R_0$.",
            "steps": [
                {
                    "stepName": "Step 1: Relate Mass Difference to Coulomb Energy Difference",
                    "math": r"\Delta E_C = [M(^{15}\text{O}) - M(^{15}\text{N})]c^2 + (m_n - m_H)c^2 = 2.754\text{ MeV} + 0.782\text{ MeV} = 3.536\text{ MeV}",
                    "explanation": "The binding energy difference between mirror nuclei equals the mass difference plus the neutron-hydrogen rest mass difference."
                },
                {
                    "stepName": "Step 2: Formulate the Coulomb Energy Equation for R",
                    "math": r"\Delta E_C = \frac{3}{5} \frac{e^2}{4\pi\varepsilon_0 R} (2Z - 1) = \frac{3}{5} \frac{1.440\text{ MeV}\cdot\text{fm}}{R} (2 \times 8 - 1) = \frac{0.864\text{ MeV}\cdot\text{fm} \times 15}{R} = \frac{12.96\text{ MeV}\cdot\text{fm}}{R}",
                    "explanation": "Substitute Z = 8 and e^2 / (4 pi epsilon_0) = 1.440 MeV * fm into the formula."
                },
                {
                    "stepName": "Step 3: Solve for the Nuclear Radius R",
                    "math": r"R = \frac{12.96\text{ MeV}\cdot\text{fm}}{3.536\text{ MeV}} \approx 3.665\text{ fm}",
                    "explanation": "Divide the Coulomb coefficient by the measured energy shift."
                },
                {
                    "stepName": "Step 4: Extract the Radius Parameter R_0",
                    "math": r"R_0 = \frac{R}{A^{1/3}} = \frac{3.665\text{ fm}}{(15)^{1/3}} = \frac{3.665\text{ fm}}{2.4662} \approx 1.243\text{ fm}",
                    "explanation": "Divide R by 15^(1/3) to obtain R_0."
                }
            ],
            "answer": "\\Delta E_C = 3.536 \\text{ MeV}, \\quad R = 3.67 \\text{ fm}, \\quad R_0 = 1.24 \\text{ fm}"
        },
        {
            "id": "nuc-p-1-3",
            "title": "Most Stable Isobar Prediction for A = 125 via Weizsacker Formula",
            "statement": "Using the Weizsäcker Semi-Empirical Mass Formula with Coulomb coefficient $a_c = 0.711 \\text{ MeV}$ and asymmetry coefficient $a_a = 23.7 \\text{ MeV}$: (a) Derive and calculate the theoretical most stable atomic number $Z_0$ for mass number $A = 125$. (b) Determine the stable chemical element corresponding to this isobar and verify whether it matches the known stable nuclide Tellurium-125 ($Z=52$).",
            "steps": [
                {
                    "stepName": "Step 1: Recall the Formula for the Valley of Beta Stability",
                    "math": r"Z_0 = \frac{A}{2 + \frac{a_c}{2 a_a} A^{2/3}}",
                    "explanation": "Set the first derivative of the SEMF binding energy with respect to Z to zero."
                },
                {
                    "stepName": "Step 2: Evaluate the Denominator Terms for A = 125",
                    "math": r"A^{2/3} = (125)^{2/3} = (5)^2 = 25.0 \implies \frac{a_c}{2 a_a} A^{2/3} = \frac{0.711\text{ MeV}}{2 \times 23.7\text{ MeV}} \times 25.0 = \frac{0.711}{47.4} \times 25.0 \approx 0.0150 \times 25.0 = 0.375",
                    "explanation": "Compute the Coulomb correction to the symmetry denominator."
                },
                {
                    "stepName": "Step 3: Calculate the Theoretical Value of Z_0",
                    "math": r"Z_0 = \frac{125}{2 + 0.375} = \frac{125}{2.375} \approx 52.63",
                    "explanation": "Divide A by the total denominator."
                },
                {
                    "stepName": "Step 4: Identify the Nearest Integer Stable Isobar",
                    "math": r"Z_0 \approx 52.63 \implies \text{Nearest Integer } Z = 52 \text{ or } 53",
                    "explanation": "Tellurium (Z = 52) has 73 neutrons and is an extraordinarily stable even-Z nuclide (^125_52Te, natural abundance 7.07%). Iodine-125 (Z = 53) decays to Te-125 via electron capture with T_1/2 = 59.4 days. The SEMF prediction matches experiment."
                }
            ],
            "answer": "Z_0 = 52.63 \\implies Z = 52 \\quad (^{125}_{52}\\text{Te}, \\text{Tellurium-125})"
        }
    ]
}

# ==========================================
# UNIT 2: Radioactivity, Decay Kinetics & Radiometric Dating
# ==========================================
u2 = {
    "unitNumber": 2,
    "unitId": "unit2-radioactivity",
    "title": "Radioactivity, Decay Kinetics & Radiometric Dating",
    "description": "Rigorous mathematical formulation of nuclear decay: Segre chart of stability, differential and integral radioactive decay laws, half-life, mean lifetime, activity units (Becquerel, Curie), Bateman equations for successive multi-step chains, secular and transient radioactive equilibria, and radiometric dating (Carbon-14, Potassium-Argon, Uranium-Lead isochrons).",
    "sections": [
        {
            "id": "nuc-2-1",
            "title": "Nuclear Stability, the Segre Chart & The Radioactive Decay Law",
            "simulation": "nuc-decay-kinetics-sim",
            "content": r"""<h4>1. The Segrè Chart of Nuclides ($N$ vs. $Z$)</h4>
<p>Nuclear stability is dictated by the delicate quantum balance between attractive short-range nucleon-nucleon strong forces and long-range disruptive Coulomb electrostatic repulsion between protons. Plotting neutron number $N$ against atomic number $Z$ for all known nuclides yields the <strong>Segrè Chart</strong>:</p>
<ul>
<li><strong>Light Stable Nuclei ($Z \le 20$):</strong> Follow the $N = Z$ line of exact symmetry ($N/Z = 1.0$), as in $^4_2\text{He}, {^{12}_6\text{C}}, {^{16}_8\text{O}}, {^{40}_{20}\text{Ca}}$.</li>
<li><strong>Heavy Stable Nuclei ($Z > 20$):</strong> Curve progressively toward the neutron axis to provide additional strong-force binding without adding disruptive Coulomb charges, reaching $N/Z \approx 1.54$ at $^{208}_{82}\text{Pb}_{126}$.</li>
<li><strong>Proton Drip Line & Neutron Drip Line:</strong> Boundaries beyond which proton or neutron separation energies vanish ($S_p \le 0$ or $S_n \le 0$); nucleons drip spontaneously from the nucleus on strong-interaction timescales ($\sim 10^{-21}\text{ s}$).</li>
<li><strong>Upper Limit of Natural Stability:</strong> Terminated at Bismuth-209 ($Z = 83$). All heavier elements ($Z \ge 84$) are naturally radioactive.</li>
</ul>

<h4>2. The Fundamental Radioactive Decay Law</h4>
<p>Radioactive decay is an intrinsically stochastic, memoryless quantum process governed by the uncertainty principle. For a population of $N(t)$ identical, unstable radioactive parent nuclei at time $t$, the probability of any given nucleus disintegrating per unit time is a fundamental constant, the <strong>decay constant</strong> $\lambda$ ($\text{s}^{-1}$):</p>
<div class="math-display">
$$-\frac{dN}{dt} = \lambda N(t)$$
</div>
<p>Integrating with the initial condition $N(0) = N_0$ at $t = 0$ yields the exponential <strong>Rutherford-Soddy Radioactive Decay Law</strong>:</p>
<div class="math-display">
$$N(t) = N_0 e^{-\lambda t}$$
</div>

<h4>3. Half-Life $T_{1/2}$ and Mean Lifetime $\tau$</h4>
<ul>
<li><strong>Half-Life ($T_{1/2}$):</strong> The elapsed time required for exactly one-half of the initial radioactive nuclei to decay ($N(T_{1/2}) = N_0 / 2$):
<div class="math-display">
$$\frac{N_0}{2} = N_0 e^{-\lambda T_{1/2}} \implies T_{1/2} = \frac{\ln(2)}{\lambda} = \frac{0.693147}{\lambda}$$
</div></li>
<li><strong>Mean Lifetime ($\tau$):</strong> The statistical average lifetime of a radioactive nucleus:
<div class="math-display">
$$\tau = \langle t \rangle = \frac{\int_0^\infty t \left( \lambda N_0 e^{-\lambda t} \right) dt}{N_0} = \frac{1}{\lambda} = \frac{T_{1/2}}{\ln(2)} \approx 1.4427 T_{1/2}$$
</div></li>
</ul>"""
        },
        {
            "id": "nuc-2-2",
            "title": "Activity, Radiation Units & Counting Statistics",
            "content": r"""<h4>1. Radioactivity and Decay Rate</h4>
<p>The <strong>activity</strong> $A(t)$ of a radioactive sample is defined as the number of disintegrations occurring per unit time:</p>
<div class="math-display">
$$A(t) = -\frac{dN}{dt} = \lambda N(t) = \lambda N_0 e^{-\lambda t} = A_0 e^{-\lambda t}$$
</div>

<h4>2. Units of Radioactivity</h4>
<ul>
<li><strong>Becquerel ($\text{Bq}$):</strong> The SI unit of activity, defined as precisely one nuclear disintegration per second:
<div class="math-display">
$$1\text{ Bq} \equiv 1\text{ disintegration/s}$$
</div></li>
<li><strong>Curie ($\text{Ci}$):</strong> The historical unit, historically based on the activity of 1 gram of pure Radium-226:
<div class="math-display">
$$1\text{ Ci} \equiv 3.700 \times 10^{10}\text{ Bq} = 37\text{ GBq}$$
</div></li>
<li><strong>Specific Activity ($a$):</strong> Activity per unit mass of the pure radioisotope:
<div class="math-display">
$$a_{\text{spec}} = \frac{A}{m} = \frac{\lambda N_A}{M} = \frac{\ln(2) N_A}{T_{1/2} M}$$
</div></li>
</ul>

<h4>3. Counting Statistics: Poisson and Gaussian Distributions</h4>
<p>Because nuclear disintegrations are independent random events occurring with small probability $p \ll 1$ in a large population $N \gg 1$, the probability of recording exactly $n$ counts in a time interval $\Delta t$ follows the <strong>Poisson distribution</strong>:</p>
<div class="math-display">
$$P(n; \mu) = \frac{\mu^n e^{-\mu}}{n!}$$
</div>
<p>where $\mu = \langle n \rangle$ is the mean count. The variance equals the mean: $\sigma^2 = \mu$. The standard deviation in any single nuclear counting measurement of $N_{\text{counts}}$ is:</p>
<div class="math-display">
$$\sigma = \sqrt{N_{\text{counts}}}$$
</div>
<p>The fractional statistical counting uncertainty is $\frac{\sigma}{N} = \frac{1}{\sqrt{N_{\text{counts}}}}$. To achieve a precision of $1\%$, one must accumulate at least $N_{\text{counts}} = (1/0.01)^2 = 10,000$ counts.</p>"""
        },
        {
            "id": "nuc-2-3",
            "title": "Successive Radioactive Transformations & Bateman Equations",
            "content": r"""<h4>1. Multi-Step Radioactive Decay Series</h4>
<p>In nature, heavy radioactive isotopes decay through successive chains (e.g., the Uranium-238, Thorium-232, and Actinium-235 series). Consider a general radioactive cascade:</p>
<div class="math-display">
$$N_1 \xrightarrow{\lambda_1} N_2 \xrightarrow{\lambda_2} N_3 \xrightarrow{\lambda_3} \dots \xrightarrow{\lambda_m} N_m \text{ (stable)}$$
</div>
<p>The system of coupled linear differential equations governing the populations is:</p>
<div class="math-display">
$$\frac{dN_1}{dt} = - \lambda_1 N_1$$
</div>
<div class="math-display">
$$\frac{dN_2}{dt} = \lambda_1 N_1 - \lambda_2 N_2$$
</div>
<div class="math-display">
$$\frac{dN_i}{dt} = \lambda_{i-1} N_{i-1} - \lambda_i N_i$$
</div>

<h4>2. Derivation of the Daughter Population $N_2(t)$</h4>
<p>Assuming initially pure parent at $t = 0$ ($N_1(0) = N_0$ and $N_2(0) = 0$):</p>
<div class="math-display">
$$\frac{dN_2}{dt} + \lambda_2 N_2 = \lambda_1 N_0 e^{-\lambda_1 t}$$
</div>
<p>Multiplying by the integrating factor $e^{\lambda_2 t}$:</p>
<div class="math-display">
$$\frac{d}{dt} \left( N_2 e^{\lambda_2 t} \right) = \lambda_1 N_0 e^{(\lambda_2 - \lambda_1)t} \implies N_2 e^{\lambda_2 t} = \frac{\lambda_1 N_0}{\lambda_2 - \lambda_1} e^{(\lambda_2 - \lambda_1)t} + C$$
</div>
<p>Applying initial condition $N_2(0) = 0 \implies C = - \frac{\lambda_1 N_0}{\lambda_2 - \lambda_1}$ yields:</p>
<div class="math-display">
$$N_2(t) = \frac{\lambda_1 N_0}{\lambda_2 - \lambda_1} \left( e^{-\lambda_1 t} - e^{-\lambda_2 t} \right)$$
</div>
<p>The daughter activity is $A_2(t) = \lambda_2 N_2(t) = \frac{\lambda_1 \lambda_2 N_0}{\lambda_2 - \lambda_1} (e^{-\lambda_1 t} - e^{-\lambda_2 t})$.</p>

<h4>3. General Bateman Solution for the $n$-th Isotope</h4>
<p>Harry Bateman (1910) solved the general $n$-step system in closed analytical form:</p>
<div class="math-display">
$$N_n(t) = N_1(0) \left( \prod_{i=1}^{n-1} \lambda_i \right) \sum_{j=1}^n \frac{e^{-\lambda_j t}}{\prod_{k \neq j}^n (\lambda_k - \lambda_j)}$$
</div>"""
        },
        {
            "id": "nuc-2-4",
            "title": "Radioactive Equilibria: Secular, Transient & Non-Equilibrium",
            "content": r"""<h4>1. Classification of Radioactive Equilibria</h4>
<p>The physical behavior of a parent-daughter system depends on the ratio of parent half-life $T_{1/2, 1}$ to daughter half-life $T_{1/2, 2}$ (or decay constants $\lambda_1$ vs. $\lambda_2$):</p>

<h4>2. Secular Equilibrium ($\lambda_1 \ll \lambda_2$ or $T_{1/2, 1} \gg T_{1/2, 2}$)</h4>
<p>When the parent is extremely long-lived compared to the daughter (e.g., $^{226}\text{Ra}$ with $T_{1/2} = 1600\text{ y}$ decaying to $^{222}\text{Rn}$ with $T_{1/2} = 3.82\text{ d}$, or $^{238}\text{U}$ with $4.47 \times 10^9\text{ y}$):</p>
<ul>
<li>$\lambda_2 - \lambda_1 \approx \lambda_2$ and $e^{-\lambda_1 t} \approx 1$.</li>
<li>For times $t \gg \tau_2 = 1/\lambda_2$, the transient exponential vanishes ($e^{-\lambda_2 t} \to 0$):</li>
</ul>
<div class="math-display">
$$N_2(t) \to \frac{\lambda_1}{\lambda_2} N_1 \implies \lambda_1 N_1 = \lambda_2 N_2 \implies A_1 = A_2$$
</div>
<p>In <strong>secular equilibrium</strong>, the activity of the daughter equals the activity of the parent. Across an entire undisturbed natural decay series:</p>
<div class="math-display">
$$A_1 = A_2 = A_3 = \dots = A_n \implies \lambda_1 N_1 = \lambda_2 N_2 = \dots = \lambda_n N_n$$
</div>

<h4>3. Transient Equilibrium ($\lambda_1 < \lambda_2$, comparable orders of magnitude)</h4>
<p>When the parent is longer-lived than the daughter, but parent decay is non-negligible (e.g., $^{99}\text{Mo}$ with $T_{1/2} = 66\text{ h}$ decaying to $^{99m}\text{Tc}$ with $T_{1/2} = 6.0\text{ h}$, widely used in nuclear medicine generators):</p>
<p>For $t \gg 1/\lambda_2$, $e^{-\lambda_2 t} \ll e^{-\lambda_1 t}$, yielding:</p>
<div class="math-display">
$$N_2(t) \approx \frac{\lambda_1}{\lambda_2 - \lambda_1} N_1(t) \implies \frac{A_2(t)}{A_1(t)} = \frac{\lambda_2}{\lambda_2 - \lambda_1} > 1$$
</div>
<p>In <strong>transient equilibrium</strong>, the daughter activity decays with the half-life of the parent, but exceeds the parent activity by the constant factor $\frac{\lambda_2}{\lambda_2 - \lambda_1}$.</p>

<h4>4. Non-Equilibrium ($\lambda_1 > \lambda_2$)</h4>
<p>If the parent is shorter-lived than the daughter, no equilibrium can ever be established. The parent decays rapidly, leaving the daughter to decay independently with its own characteristic decay constant $\lambda_2$.</p>"""
        },
        {
            "id": "nuc-2-5",
            "title": "Radiometric Dating Principles: Carbon-14, K-Ar & U-Pb Isochrons",
            "simulation": "nuc-carbon-dating-sim",
            "content": r"""<h4>1. Radiocarbon ($^{14}\text{C}$) Dating</h4>
<p>Willard Libby (1949, Nobel Prize 1960) developed radiocarbon dating based on cosmic-ray production of $^{14}\text{C}$ in the upper atmosphere via neutron capture on nitrogen:</p>
<div class="math-display">
$$^1_0 n + {^{14}_7\text{N}} \to {^{14}_6\text{C}} + {^1_1 p}$$
</div>
<p>The radioactive $^{14}\text{C}$ ($T_{1/2} = 5730\pm40\text{ y}$, $\beta^-$ emitter) oxidizes to $^{14}\text{CO}_2$ and mixes into the biosphere via photosynthesis and the food chain, establishing an equilibrium specific activity in living organic tissue:</p>
<div class="math-display">
$$A_0 \approx 15.3\text{ disintegrations per minute per gram of Carbon} \approx 0.255\text{ Bq/g}$$
</div>
<p>Upon death, biological carbon exchange terminates, and $^{14}\text{C}$ decays exponentially without replenishment: $A(t) = A_0 e^{-\lambda t}$. The age of the archaeological specimen is calculated as:</p>
<div class="math-display">
$$t = \frac{1}{\lambda} \ln\left(\frac{A_0}{A(t)}\right) = \frac{T_{1/2}}{\ln(2)} \ln\left(\frac{A_0}{A(t)}\right) = 8267 \ln\left(\frac{A_0}{A(t)}\right) \text{ years}$$
</div>

<h4>2. Potassium-Argon ($^{40}\text{K}$-$^{40}\text{Ar}$) Dating</h4>
<p>Used for geological samples ($10^5$ to $4.5 \times 10^9$ years). Natural Potassium contains $0.0117\%$ $^{40}\text{K}$ ($T_{1/2} = 1.248 \times 10^9\text{ y}$), which exhibits branched decay:</p>
<ul>
<li>$89.3\%$ decays via $\beta^-$ to $^{40}\text{Ca}$.</li>
<li>$10.7\%$ decays via electron capture to noble gas $^{40}\text{Ar}$.</li>
</ul>
<p>When volcanic rock crystallizes from magma, molten lava outgasses all volatile Argon ($^{40}\text{Ar}_{\text{initial}} = 0$). Trapped radiogenic $^{40}\text{Ar}$ subsequently accumulates in the solid mineral lattice:</p>
<div class="math-display">
$$N(^{40}\text{Ar}) = \frac{\lambda_{EC}}{\lambda_{\text{tot}}} N(^{40}\text{K}) \left( e^{\lambda_{\text{tot}} t} - 1 \right) \implies t = \frac{1}{\lambda_{\text{tot}}} \ln\left( 1 + \frac{\lambda_{\text{tot}}}{\lambda_{EC}} \frac{N(^{40}\text{Ar})}{N(^{40}\text{K})} \right)$$
</div>

<h4>3. Uranium-Lead ($^{238}\text{U}$-$^{206}\text{Pb}$) Isochron Dating</h4>
<p>In zircon crystals ($\text{ZrSiO}_4$), initial lead contamination is eliminated during crystallization. For mineral samples containing non-radiogenic common lead ($^{204}\text{Pb}$), measuring the isotopic ratios yields the <strong>isochron equation</strong>:</p>
<div class="math-display">
$$\left( \frac{^{206}\text{Pb}}{^{204}\text{Pb}} \right)_{\text{today}} = \left( \frac{^{206}\text{Pb}}{^{204}\text{Pb}} \right)_0 + \left( \frac{^{238}\text{U}}{^{204}\text{Pb}} \right)_{\text{today}} \left( e^{\lambda_{238} t} - 1 \right)$$
</div>
<p>Plotting $^{206}\text{Pb}/^{204}\text{Pb}$ vs. $^{238}\text{U}/^{204}\text{Pb}$ for different co-genetic mineral grains yields a straight line whose slope $m = e^{\lambda_{238} t} - 1$ determines the geological age $t$ independently of the initial lead content.</p>"""
        }
    ],
    "problems": [
        {
            "id": "nuc-p-2-1",
            "title": "Activity and Specific Activity of Cobalt-60 Radiation Source",
            "statement": "Cobalt-60 ($^{60}_{27}\\text{Co}$) is a widely used industrial and medical gamma source with a half-life of $T_{1/2} = 5.271 \\text{ years}$ ($1.663 \\times 10^8 \\text{ s}$) and atomic mass $M = 59.9338 \\text{ g/mol}$. (a) Calculate the decay constant $\\lambda$ in $\\text{s}^{-1}$. (b) Determine the specific activity of pure $^{60}\\text{Co}$ in $\\text{Bq/g}$ and in $\\text{Ci/g}$. (c) What mass of $^{60}\\text{Co}$ is required to fabricate a $5000 \\text{ Ci}$ radiotherapy source?",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Decay Constant lambda",
                    "math": r"\lambda = \frac{\ln(2)}{T_{1/2}} = \frac{0.693147}{1.6635 \times 10^8\text{ s}} \approx 4.1668 \times 10^{-9}\text{ s}^{-1}",
                    "explanation": "Evaluate lambda = ln(2) / T_1/2 in SI units."
                },
                {
                    "stepName": "Step 2: Calculate the Specific Activity per Gram",
                    "math": r"a_{\text{spec}} = \frac{\lambda N_A}{M} = \frac{(4.1668 \times 10^{-9}\text{ s}^{-1})(6.0221 \times 10^{23}\text{ mol}^{-1})}{59.9338\text{ g/mol}} = \frac{2.5093 \times 10^{15}}{59.9338}\text{ Bq/g} \approx 4.1868 \times 10^{13}\text{ Bq/g} = 41.87\text{ TBq/g}",
                    "explanation": "Compute activity per gram of pure isotope."
                },
                {
                    "stepName": "Step 3: Convert Specific Activity to Curies per Gram",
                    "math": r"a_{\text{spec}} = \frac{4.1868 \times 10^{13}\text{ Bq/g}}{3.700 \times 10^{10}\text{ Bq/Ci}} \approx 1131.6\text{ Ci/g}",
                    "explanation": "Divide by 3.7 x 10^10 Bq per Curie."
                },
                {
                    "stepName": "Step 4: Calculate the Mass Required for a 5000 Ci Source",
                    "math": r"m = \frac{A_{\text{target}}}{a_{\text{spec}}} = \frac{5000\text{ Ci}}{1131.6\text{ Ci/g}} \approx 4.419\text{ g}",
                    "explanation": "Divide target activity by specific activity."
                }
            ],
            "answer": "\\lambda = 4.17 \\times 10^{-9} \\text{ s}^{-1}, \\quad a_{\\text{spec}} = 4.19 \\times 10^{13} \\text{ Bq/g} \\quad (1132 \\text{ Ci/g}), \\quad m = 4.42 \\text{ g}"
        },
        {
            "id": "nuc-p-2-2",
            "title": "Transient Equilibrium and Maximum Activity in Technetium-99m Generator",
            "statement": "In a $^{99}\\text{Mo}$-$^{99m}\\text{Tc}$ medical isotope generator, parent $^{99}\\text{Mo}$ ($T_{1/2, 1} = 66.0 \\text{ h}$, $\\lambda_1 = 0.01050 \\text{ h}^{-1}$) decays to daughter $^{99m}\\text{Tc}$ ($T_{1/2, 2} = 6.01 \\text{ h}$, $\\lambda_2 = 0.11533 \\text{ h}^{-1}$) with a branching ratio of $87.5\\%$. Starting with fresh pure $^{99}\\text{Mo}$ ($N_2(0) = 0$): (a) Calculate the time $t_{\\text{max}}$ at which the daughter $^{99m}\\text{Tc}$ activity reaches its maximum value. (b) Calculate the ratio of daughter activity to parent activity at transient equilibrium.",
            "steps": [
                {
                    "stepName": "Step 1: Formulate the Condition for Maximum Daughter Activity",
                    "math": r"\frac{dN_2}{dt} = 0 \implies \lambda_1 N_1(t_{\text{max}}) = \lambda_2 N_2(t_{\text{max}}) \implies t_{\text{max}} = \frac{\ln(\lambda_2 / \lambda_1)}{\lambda_2 - \lambda_1}",
                    "explanation": "Setting the derivative of N_2(t) in the Bateman equation to zero yields the maximum population time."
                },
                {
                    "stepName": "Step 2: Calculate the Numerical Value of t_max",
                    "math": r"t_{\text{max}} = \frac{\ln(0.11533 / 0.01050)}{0.11533 - 0.01050} = \frac{\ln(10.984)}{0.10483}\text{ h} = \frac{2.3964}{0.10483}\text{ h} \approx 22.86\text{ hours}",
                    "explanation": "Evaluate t_max in hours. The generator reaches peak activity at approx 22.9 hours after elution."
                },
                {
                    "stepName": "Step 3: Calculate the Equilibrium Activity Ratio",
                    "math": r"\frac{A_2}{A_1} = \text{Branching Ratio} \times \frac{\lambda_2}{\lambda_2 - \lambda_1} = 0.875 \times \frac{0.11533}{0.11533 - 0.01050} = 0.875 \times \frac{0.11533}{0.10483} \approx 0.875 \times 1.1001 \approx 0.9626",
                    "explanation": "Multiply the transient equilibrium activity factor by the 87.5% branching fraction."
                }
            ],
            "answer": "t_{\\text{max}} = 22.86 \\text{ hours}, \\quad \\frac{A_2}{A_1} = 0.963 \\quad (\\text{Transient Equilibrium})"
        },
        {
            "id": "nuc-p-2-3",
            "title": "Archaeological Radiocarbon Dating of an Ancient Wooden Artifact",
            "statement": "An ancient charcoal sample excavated from an archaeological site has a measured $^{14}\\text{C}$ activity of $3.82 \\text{ disintegrations per minute per gram of Carbon}$ ($\\text{dpm/g}$). A living modern reference standard exhibits an activity of $15.30 \\text{ dpm/g}$. The half-life of $^{14}\\text{C}$ is $5730 \\text{ years}$. (a) Calculate the decay constant $\\lambda$ of $^{14}\\text{C}$ in $\\text{year}^{-1}$. (b) Determine the calendar age of the archaeological sample.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate the Decay Constant lambda",
                    "math": r"\lambda = \frac{\ln(2)}{T_{1/2}} = \frac{0.693147}{5730\text{ y}} \approx 1.2097 \times 10^{-4}\text{ y}^{-1}",
                    "explanation": "Compute the decay constant per year."
                },
                {
                    "stepName": "Step 2: Apply the Radiocarbon Age Equation",
                    "math": r"t = \frac{1}{\lambda} \ln\left(\frac{A_0}{A(t)}\right) = \frac{1}{1.2097 \times 10^{-4}\text{ y}^{-1}} \ln\left(\frac{15.30}{3.82}\right) = (8266.5\text{ y}) \ln(4.0052)",
                    "explanation": "Substitute modern initial activity A_0 and measured activity A(t)."
                },
                {
                    "stepName": "Step 3: Evaluate Natural Logarithm and Final Age",
                    "math": r"t = (8266.5\text{ y}) \times (1.3876) \approx 11470\text{ years}",
                    "explanation": "Multiply to find the age in years."
                }
            ],
            "answer": "\\lambda = 1.21 \\times 10^{-4} \\text{ y}^{-1}, \\quad t = 11470 \\text{ years} \\quad (\\sim 9450 \\text{ BCE})"
        }
    ]
}

with open("nuc_u1.json", "w") as f:
    json.dump(u1, f, indent=2)
print("nuc_u1.json created successfully!")

with open("nuc_u2.json", "w") as f:
    json.dump(u2, f, indent=2)
print("nuc_u2.json created successfully!")
