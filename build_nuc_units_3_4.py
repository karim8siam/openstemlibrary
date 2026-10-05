import json

# ==========================================
# UNIT 3: Mechanisms of Nuclear Decay: Alpha, Beta & Gamma Transitions
# ==========================================
u3 = {
    "unitNumber": 3,
    "unitId": "unit3-nuclear-decay-mechanisms",
    "title": "Mechanisms of Nuclear Decay: Alpha, Beta & Gamma Transitions",
    "description": "Rigorous quantum mechanics of radioactive decay: alpha disintegration energetics, Geiger-Nuttall systematics, Gamow quantum tunneling theory; beta decay kinematics (beta-minus, beta-plus, electron capture), Pauli neutrino hypothesis, Fermi golden rule theory of beta transitions, Fermi-Kurie plots, selection rules (Fermi vs Gamow-Teller), and parity violation; gamma electromagnetic multipole radiation, selection rules, Weisskopf transition rates, internal conversion, and primary photon matter interactions.",
    "sections": [
        {
            "id": "nuc-3-1",
            "title": "Alpha Decay Energetics: Q-Value, Recoil Sharing & Fine Structure",
            "content": r"""<h4>1. Kinematics and Q-Value of Alpha Disintegration</h4>
<p>In spontaneous alpha decay, a parent nucleus $^A_Z\text{X}$ emits an alpha particle ($^4_2\text{He}$ nucleus) and transmutes into a daughter nucleus $^{A-4}_{Z-2}\text{Y}$:</p>
<div class="math-display">
$$^A_Z\text{X} \longrightarrow {^{A-4}_{Z-2}\text{Y}} + {^4_2\text{He}} \quad (\alpha)$$
</div>
<p>By conservation of relativistic energy in the rest frame of the parent ($M_P c^2 = M_D c^2 + T_D + M_\alpha c^2 + T_\alpha$), the decay energy or <strong>$Q_\alpha$-value</strong> is:</p>
<div class="math-display">
$$Q_\alpha = [M(A, Z) - M(A-4, Z-2) - M(^4\text{He})] c^2$$
</div>
<p>where $M$ denotes neutral atomic masses (atomic electron binding energies cancel to high precision). Alpha emission is energetically permissible if and only if $Q_\alpha > 0$. Using the SEMF, $Q_\alpha$ becomes positive for mass numbers $A \gtrsim 150$, but observable half-lives ($T_{1/2} < 10^{20}\text{ years}$) require $A \gtrsim 208$ ($Q_\alpha \gtrsim 4 - 9\text{ MeV}$).</p>

<h4>2. Kinetic Energy Sharing & Daughter Recoil</h4>
<p>By linear momentum conservation in the rest frame of the parent ($p_D = p_\alpha = p$):</p>
<div class="math-display">
$$T_\alpha = \frac{p^2}{2 M_\alpha}, \quad T_D = \frac{p^2}{2 M_D} = \frac{M_\alpha}{M_D} T_\alpha$$
</div>
<p>Substituting into $Q_\alpha = T_\alpha + T_D$:</p>
<div class="math-display">
$$Q_\alpha = T_\alpha \left( 1 + \frac{M_\alpha}{M_D} \right) = T_\alpha \left( \frac{M_D + M_\alpha}{M_D} \right) \approx T_\alpha \left( \frac{A}{A - 4} \right)$$
</div>
<div class="math-display">
$$T_\alpha \approx \frac{A - 4}{A} Q_\alpha, \quad T_D \approx \frac{4}{A} Q_\alpha$$
</div>
<p>For heavy nuclei ($A \sim 200 - 240$), the emitted alpha carries approximately $98\%$ of the total available energy, while the recoiling daughter carries $\approx 2\%$ (typically $80 - 120\text{ keV}$). This recoil energy is sufficient to displace the daughter atom from its crystal lattice, creating radiation damage tracks in minerals.</p>

<h4>3. Alpha Spectrum Fine Structure & Hindrance Factors</h4>
<p>If the alpha transition populates the ground state of the daughter nucleus, a monoenergetic group of alpha particles is emitted. However, if the daughter nucleus possesses low-lying excited states, the decay branches into multiple discrete energy lines, known as <strong>alpha fine structure</strong>. The partial decay width to each excited level depends critically on:</p>
<ul>
<li><strong>Energy suppression:</strong> Lower $Q_i = Q_0 - E^*_i$ drastically thickens the Coulomb barrier, exponentially depressing transition probability.</li>
<li><strong>Orbital angular momentum:</strong> If the parent and daughter states differ in spin $\vec{I}_i \to \vec{I}_f$, the alpha particle must carry orbital angular momentum $\vec{L} = \vec{I}_i - \vec{I}_f$ ($|I_i - I_f| \le L \le I_i + I_f$), adding a centrifugal barrier $V_\ell(r) = \frac{\hbar^2 \ell(\ell+1)}{2\mu r^2}$.</li>
<li><strong>Hindrance Factor ($HF$):</strong> The ratio of the theoretical barrier penetration half-life to the experimental partial half-life. Transitions between spherical states with $\Delta L = 0$ have $HF \approx 1$ (favored decays), whereas transitions requiring intrinsic nucleon rearrangement or high $\ell$ have $HF \sim 10^2 - 10^4$ (hindered decays).</li>
</ul>"""
        },
        {
            "id": "nuc-3-2",
            "title": "Geiger-Nuttall Law & Gamow Quantum Barrier Tunneling Theory",
            "simulation": "nuc-alpha-gamow-tunneling-sim",
            "content": r"""<h4>1. The Geiger-Nuttall Empirical Systematics</h4>
<p>In 1911, Hans Geiger and John Mitchell Nuttall discovered an astonishing empirical regularity connecting the decay constant $\lambda$ of alpha emitters to the range $R_\alpha$ (or kinetic energy $E_\alpha$) of the emitted particles:</p>
<div class="math-display">
$$\log_{10} \lambda = A + B \log_{10} E_\alpha \quad \text{or} \quad \log_{10} T_{1/2} = C + \frac{D}{\sqrt{Q_\alpha}}$$
</div>
<p>A modest factor of two change in alpha particle energy ($Q_\alpha \approx 4\text{ MeV}$ for $^{238}\text{U}$ to $Q_\alpha \approx 8.8\text{ MeV}$ for $^{212}\text{Po}$) causes the half-life to plunge over <strong>24 orders of magnitude</strong>—from $4.47 \times 10^9\text{ years}$ down to $0.3\text{ \mu s}$. Classical mechanics could offer no explanation: the Coulomb barrier height between an alpha particle ($Z_1=2$) and daughter nucleus ($Z_2=Z-2$) at nuclear contact radius $R \approx 8\text{ fm}$ is:</p>
<div class="math-display">
$$V_C(R) = \frac{1}{4\pi\varepsilon_0} \frac{2(Z - 2)e^2}{R} \approx \frac{1.44 \times 2 \times 90}{8.5}\text{ MeV} \approx 30.5\text{ MeV}$$
</div>
<p>An alpha particle with $E_\alpha \approx 4 - 8\text{ MeV}$ lacks more than $20\text{ MeV}$ of energy required to surmount the barrier classically.</p>

<h4>2. George Gamow's Quantum Tunneling Derivation (1928)</h4>
<p>George Gamow (and independently Ronald Gurney and Edward Condon) resolved this puzzle by recognizing alpha decay as the <strong>quantum mechanical tunneling</strong> of a pre-formed alpha particle through the classically forbidden Coulomb potential barrier.</p>
<p>The decay constant $\lambda$ is modeled as the product of two probabilities:</p>
<div class="math-display">
$$\lambda = f \cdot P$$
</div>
<ol>
<li><strong>Assault Frequency ($f$):</strong> The frequency with which the alpha particle inside the nuclear well strikes the barrier. If the particle has internal velocity $v_0 \approx \sqrt{2 E_0 / m_\alpha} \approx 2 \times 10^7\text{ m/s}$ in a nuclear well of diameter $2R \approx 1.5 \times 10^{-14}\text{ m}$:</p>
<div class="math-display">
$$f = \frac{v_0}{2R} \approx 10^{21} - 10^{22}\text{ s}^{-1}$$
</div></li>
<li><strong>Tunneling Transmission Probability ($P$):</strong> In the WKB (Wentzel-Kramers-Brillouin) approximation, the transmission through a potential barrier $V(r)$ from the nuclear surface $R$ to the classical turning point $b$ ($V(b) = Q_\alpha$) is:</p>
<div class="math-display">
$$P = \exp\left( -2 \int_{R}^{b} k(r) dr \right) = \exp\left( -2 \int_{R}^{b} \sqrt{\frac{2\mu}{\hbar^2} [V_C(r) - Q_\alpha]} dr \right)$$
</div>
<p>where $\mu = \frac{M_D M_\alpha}{M_D + M_\alpha}$ is the reduced mass and $V_C(r) = \frac{2(Z - 2)e^2}{4\pi\varepsilon_0 r}$. At the turning point, $b = \frac{2(Z - 2)e^2}{4\pi\varepsilon_0 Q_\alpha}$.</p></li>
</ol>

<h4>3. Analytical Evaluation of the Gamow Factor</h4>
<p>Evaluating the WKB integral by setting $r = b \cos^2\theta$ yields:</p>
<div class="math-display">
$$\int_R^b \sqrt{\frac{b}{r} - 1} dr = b \left[ \arccos\left(\sqrt{\frac{R}{b}}\right) - \sqrt{\frac{R}{b}\left(1 - \frac{R}{b}\right)} \right]$$
</div>
<p>For heavy nuclei, $b \gg R$, so $\arccos(\sqrt{R/b}) \approx \frac{\pi}{2} - \sqrt{R/b}$. Thus:</p>
<div class="math-display">
$$2 G = 2 \sqrt{\frac{2\mu}{\hbar^2}} \sqrt{\frac{2(Z-2)e^2 b}{4\pi\varepsilon_0}} \left[ \frac{\pi}{2} - 2\sqrt{\frac{R}{b}} \right] = \pi \left(\frac{2(Z-2)e^2}{4\pi\varepsilon_0 \hbar v}\right) - 4 \sqrt{\frac{2\mu}{\hbar^2} \frac{2(Z-2)e^2 R}{4\pi\varepsilon_0}}$$
</div>
<div class="math-display">
$$\ln P = - 2 G = - C_1 \frac{Z - 2}{\sqrt{Q_\alpha}} + C_2 \sqrt{(Z - 2) R}$$
</div>
<p>This reproduces the Geiger-Nuttall law from first principles: the exponent depends inversely on $\sqrt{Q_\alpha}$, explaining how minor variations in alpha energy produce astronomical differences in nuclear half-lives.</p>"""
        },
        {
            "id": "nuc-3-3",
            "title": "Beta Decay Kinematics, Continuous Spectra & Neutrino Hypothesis",
            "content": r"""<h4>1. The Three Modes of Nuclear Beta Decay</h4>
<p>Beta decay is a weak interaction process in which an isobaric nucleon changes its isospin state ($\Delta Z = \pm 1$, constant $A$):</p>
<ol>
<li><strong>Beta-Minus ($\beta^-$) Decay:</strong> Occurs in neutron-rich nuclei. A bound neutron transforms into a proton, emitting an electron ($e^-$) and an electron antineutrino ($\bar{\nu}_e$):
<div class="math-display">
$$^A_Z\text{X} \longrightarrow {^A_{Z+1}\text{Y}} + e^- + \bar{\nu}_e \quad (n \to p + e^- + \bar{\nu}_e)$$
</div>
<div class="math-display">
$$Q_{\beta^-} = [M(A, Z) - M(A, Z+1)] c^2$$
</div></li>
<li><strong>Beta-Plus ($\beta^+$) Decay (Positron Emission):</strong> Occurs in proton-rich nuclei. A bound proton transforms into a neutron, emitting a positron ($e^+$) and an electron neutrino ($\nu_e$):
<div class="math-display">
$$^A_Z\text{X} \longrightarrow {^A_{Z-1}\text{Y}} + e^+ + \nu_e \quad (p \to n + e^+ + \nu_e)$$
</div>
<p>Accounting for the two electron rest masses in neutral atomic mass accounting ($M_P - M_D - 2m_e$):</p>
<div class="math-display">
$$Q_{\beta^+} = [M(A, Z) - M(A, Z-1) - 2m_e] c^2 = [M(A, Z) - M(A, Z-1)] c^2 - 1.022\text{ MeV}$$
</div>
<p>Positron decay requires a minimum mass threshold difference of $2 m_e c^2 = 1.022\text{ MeV}$.</p></li>
<li><strong>Orbital Electron Capture ($EC$):</strong> The nucleus captures an inner atomic orbital electron (typically $K$-shell):
<div class="math-display">
$$^A_Z\text{X} + e^- \longrightarrow {^A_{Z-1}\text{Y}} + \nu_e \quad (p + e^- \to n + \nu_e)$$
</div>
<div class="math-display">
$$Q_{EC} = [M(A, Z) - M(A, Z-1)] c^2 - B_n$$
</div>
<p>where $B_n$ is the atomic binding energy of the captured electron. Electron capture competes with $\beta^+$ and is the sole decay mode when $[M(A,Z) - M(A,Z-1)]c^2 < 1.022\text{ MeV}$.</p></li>
</ol>

<h4>2. The Continuous Beta Spectrum Crisis & Pauli's Neutrino Hypothesis</h4>
<p>In 1914, James Chadwick demonstrated that whereas alpha particles are emitted with sharp discrete energies, beta electrons exhibit a <strong>continuous kinetic energy distribution</strong> extending from zero up to a well-defined maximum end-point energy $E_{\text{max}} = Q_\beta$. If beta decay were a two-body transition ($^A_Z\text{X} \to {^A_{Z+1}\text{Y}} + e^-$), conservation of energy and linear momentum would require the electron to possess a unique discrete energy:</p>
<div class="math-display">
$$T_e = \frac{M_D}{M_D + m_e} Q_\beta \approx Q_\beta \quad (\text{Discrete!})$$
</div>
<p>The continuous spectrum, combined with apparent violations of angular momentum (e.g., $^{14}_6\text{C}(0^+) \to {^{14}_7\text{N}}(1^+) + e^-(1/2)$ has non-conserved half-integer spin), led Niels Bohr to suggest that energy might only be conserved statistically. To preserve strict conservation laws, Wolfgang Pauli (1930) proposed his "desperate remedy": an undetectable, neutral, spin-$1/2$ fermion with vanishingly small rest mass emitted simultaneously with the electron. Enrico Fermi named this elusive particle the <strong>neutrino</strong> ($\nu$). In three-body decay:</p>
<div class="math-display">
$$Q_\beta = T_e + T_\nu + T_{\text{recoil}} \approx T_e + T_\nu$$
</div>
<p>The three-body phase space partitions energy continuously between $T_e$ and $T_\nu$, exactly resolving the anomaly.</p>"""
        },
        {
            "id": "nuc-3-4",
            "title": "Fermi Theory of Beta Decay, Kurie Plots & Selection Rules",
            "simulation": "nuc-beta-energy-spectrum-sim",
            "content": r"""<h4>1. Fermi's Quantum Formulation of Beta Disintegration</h4>
<p>In 1934, Enrico Fermi formulated the quantum theory of beta decay using time-dependent perturbation theory (Fermi's Golden Rule #2). The transition rate per unit energy interval is:</p>
<div class="math-display">
$$\lambda = \frac{2\pi}{\hbar} |V_{fi}|^2 \rho(E_0)$$
</div>
<p>where $V_{fi} = g \int [\psi_f^* \phi_e^*(\vec{r}) \phi_\nu^*(\vec{r})] \mathcal{O}_{\text{weak}} \psi_i d^3r$, $g \approx 1.4 \times 10^{-62}\text{ J}\cdot\text{m}^3$ ($G_F \approx 1.166 \times 10^{-5}\text{ GeV}^{-2}$) is Fermi's weak coupling constant, and $\rho(E_0)$ is the density of accessible two-particle continuum states.</p>
<p>Because the electron de Broglie wavelength ($\lambda_e \sim 1000\text{ fm}$) is vastly larger than the nuclear radius ($R \sim 5\text{ fm}$), the lepton wave functions can be approximated as plane waves and expanded as $e^{i \vec{k}\cdot\vec{r}} \approx 1 + i \vec{k}\cdot\vec{r} + \dots$. Retaining the leading term ($\ell = 0$) defines <strong>allowed transitions</strong>.</p>

<h4>2. Theoretical Electron Energy Spectrum & The Fermi Function</h4>
<p>The statistical phase space factor combined with the Coulomb correction of the daughter nucleus yields the differential electron momentum distribution:</p>
<div class="math-display">
$$N(p_e) dp_e = \frac{g^2 |M_{fi}|^2}{2\pi^3 \hbar^7 c^3} F(Z', p_e) p_e^2 (E_0 - E_e)^2 dp_e$$
</div>
<p>where $E_0 = Q_\beta + m_e c^2$ is the total endpoint energy ($E_e^2 = p_e^2 c^2 + m_e^2 c^4$), and $F(Z', p_e)$ is the relativistic <strong>Fermi Function</strong> representing Coulomb distortion of the electron wave function by the daughter nucleus ($Z' = +Z_D$ for $e^-$, $Z' = -Z_D$ for $e^+$):</p>
<div class="math-display">
$$F(Z', p_e) = \frac{|\psi_e(0)|_{\text{Coulomb}}^2}{|\psi_e(0)|_{\text{plane wave}}^2} \approx \frac{2\pi \eta}{1 - e^{-2\pi \eta}}, \quad \eta = \frac{\pm Z' e^2}{4\pi\varepsilon_0 \hbar v_e} = \frac{\pm Z' \alpha}{v_e / c}$$
</div>

<h4>3. The Fermi-Kurie Plot</h4>
<p>Linearizing the spectral distribution provides a sensitive test of the theory and precise measurement of the decay endpoint:</p>
<div class="math-display">
$$K(p_e) \equiv \sqrt{ \frac{N(p_e)}{p_e^2 F(Z', p_e)} } \propto (E_0 - E_e)$$
</div>
<p>Plotting $K(p_e)$ against electron total energy $E_e$ yields a perfect straight line for allowed transitions whose intercept on the horizontal axis determines $E_0$. A non-zero neutrino mass $m_\nu$ would produce a vertical downturn with infinite slope at the extreme endpoint $E_e = E_0 - m_\nu c^2$. Current tritium beta decay experiments (KATRIN) establish an upper bound $m_\nu < 0.45\text{ eV}/c^2$.</p>

<h4>4. Classification & Selection Rules: Fermi vs Gamow-Teller</h4>
<p>In allowed transitions ($\ell = 0$), the emitted leptons carry zero orbital angular momentum. Their intrinsic spins ($s_e = 1/2, s_\nu = 1/2$) can couple in two distinct orientations:</p>
<div class="table-responsive">
<table class="table table-bordered">
<thead>
<tr><th>Transition Type</th><th>Lepton Spin Coupling ($S$)</th><th>Nuclear Spin Change ($\Delta I$)</th><th>Nuclear Parity Change ($\Delta \pi$)</th><th>Operator</th></tr>
</thead>
<tbody>
<tr><td><strong>Fermi ($F$)</strong></td><td>Singlet: $S = 0$ (antiparallel)</td><td>$\Delta I = |I_i - I_f| = 0$ ($0 \to 0$ allowed)</td><td>$\Delta \pi = \text{no} \quad (+ \to + \text{ or } - \to -)$</td><td>$\mathbf{1}$ or $\tau^\pm$ (Vector: $V$)</td></tr>
<tr><td><strong>Gamow-Teller ($GT$)</strong></td><td>Triplet: $S = 1$ (parallel)</td><td>$\Delta I = 0, \pm 1$ ($0 \to 0$ forbidden)</td><td>$\Delta \pi = \text{no}$</td><td>$\vec{\sigma} \tau^\pm$ (Axial Vector: $A$)</td></tr>
<tr><td><strong>Forbidden ($\ell \ge 1$)</strong></td><td>$\ell = 1$ (1st forbidden), etc.</td><td>$\Delta I = 0, \pm 1, \pm 2$</td><td>$\Delta \pi = (-1)^\ell$ (Parity change for odd $\ell$)</td><td>Retarded multipoles</td></tr>
</tbody>
</table>
</div>
<p>Superallowed $0^+ \to 0^+$ pure Fermi decays (e.g., $^{14}\text{O} \to {^{14m}\text{N}}$) have matrix elements $|M_F|^2 = 2$ governed strictly by isospin symmetry, allowing high-precision determination of the vector coupling constant $G_V$ and the Cabibbo-Kobayashi-Maskawa matrix element $V_{ud}$.</p>"""
        },
        {
            "id": "nuc-3-5",
            "title": "Gamma Transitions: Multipole Radiation, Lifetimes & Isomerism",
            "content": r"""<h4>1. Electromagnetic Multipole Radiations</h4>
<p>Following alpha or beta decay, the daughter nucleus is typically left in an excited quantum state. It de-excites to the ground state by emitting a gamma-ray photon ($\gamma$). Photons are spin-$1$ bosons; because a photon has intrinsic spin $1$, monoenergetic transitions between two spin-zero states ($0^+ \to 0^+$) via single photon emission are <strong>strictly forbidden</strong> ($\gamma$ carries at least $L = 1\hbar$ angular momentum).</p>
<p>Gamma transitions are classified by the multipole order $L$ (dipole $L=1$, quadrupole $L=2$, octupole $L=3$) and electromagnetic character (Electric $EL$ or Magnetic $ML$):</p>
<div class="math-display">
$$|I_i - I_f| \le L \le I_i + I_f \quad (L \ge 1)$$
</div>
<p>The parity selection rules dictate:</p>
<div class="math-display">
$$\pi_i \pi_f = (-1)^L \quad (\text{Electric Multipole: } EL), \qquad \pi_i \pi_f = (-1)^{L+1} \quad (\text{Magnetic Multipole: } ML)$$
</div>

<h4>2. Weisskopf Single-Particle Estimates</h4>
<p>Victor Weisskopf derived standard reference single-particle transition rates $\lambda(EL)$ and $\lambda(ML)$ assuming a single proton transitions between single-particle shell model orbitals within a sphere of radius $R = R_0 A^{1/3}$ ($E_\gamma$ in MeV, $A$ mass number):</p>
<div class="math-display">
$$\lambda(E1) \approx 1.0 \times 10^{14} A^{2/3} E_\gamma^3\text{ s}^{-1}, \quad \lambda(M1) \approx 3.1 \times 10^{13} E_\gamma^3\text{ s}^{-1}$$
</div>
<div class="math-display">
$$\lambda(E2) \approx 7.3 \times 10^7 A^{4/3} E_\gamma^5\text{ s}^{-1}, \quad \lambda(M2) \approx 2.2 \times 10^7 A^{2/3} E_\gamma^5\text{ s}^{-1}$$
</div>
<div class="math-display">
$$\lambda(E3) \approx 3.4 \times 10^1 A^2 E_\gamma^7\text{ s}^{-1}, \quad \lambda(M3) \approx 1.0 \times 10^1 A^{4/3} E_\gamma^7\text{ s}^{-1}$$
</div>
<p>Key physical conclusions from Weisskopf rates:</p>
<ul>
<li>For a given multipole order $L$, electric transitions are typically two orders of magnitude faster than magnetic: $\lambda(EL) / \lambda(ML) \sim 100$.</li>
<li>Each unit increase in multipole order $L$ suppresses the decay rate by a factor of roughly $10^5 - 10^6$ due to the small nuclear size parameter $(k R)^2 \approx (E_\gamma R / \hbar c)^2 \ll 1$.</li>
<li>Consequently, transitions proceed predominantly via the lowest allowed multipole order ($L_{\text{min}} = |I_i - I_f|$), with $M1/E2$ mixing commonly observed when $L=1$ and $L=2$ compete.</li>
</ul>

<h4>3. Nuclear Isomerism & Metastable States</h4>
<p>When an excited nuclear state requires a high multipole transition ($L \ge 3$ or $4$) combined with a low transition energy ($E_\gamma \lesssim 100\text{ keV}$), the transition probability becomes exceedingly small. The excited state exhibits a remarkably long lifetime (seconds, hours, or even years), termed a <strong>nuclear isomer</strong> (denoted with an 'm', e.g., $^{99m}_{43}\text{Tc}$ with $T_{1/2} = 6.01\text{ h}$, decaying via an $M4$ transition to the ground state). The longest known isomer is $^{180m}_{73}\text{Ta}$ ($9^-$ state), with a half-life exceeding $10^{15}\text{ years}$, exceeding the age of the universe.</p>"""
        },
        {
            "id": "nuc-3-6",
            "title": "Internal Conversion & Photon Interactions with Matter",
            "simulation": "nuc-photon-attenuation-sim",
            "content": r"""<h4>1. Internal Conversion (IC)</h4>
<p>Internal conversion is an electromagnetic de-excitation mechanism that competes directly with gamma-ray photon emission. Instead of emitting a photon, the excited nucleus interacts directly via the near-field Coulomb interaction with an atomic inner-shell electron ($K, L, M$), ejecting the electron into the continuum:</p>
<div class="math-display">
$$T_e = E^* - B_e$$
</div>
<p>where $E^*$ is the nuclear excitation energy and $B_e$ is the electron atomic binding energy. Unlike beta decay electrons, internal conversion electrons are <strong>strictly monoenergetic</strong>. Vacancies created in inner atomic shells subsequently trigger the emission of characteristic <strong>X-rays</strong> or <strong>Auger electrons</strong>.</p>
<p>The <strong>internal conversion coefficient ($\alpha$)</strong> is defined as the branching ratio:</p>
<div class="math-display">
$$\alpha \equiv \frac{\lambda_{IC}}{\lambda_\gamma} = \alpha_K + \alpha_L + \alpha_M + \dots, \quad \lambda_{\text{total}} = \lambda_\gamma (1 + \alpha)$$
</div>
<p>Internal conversion dominates under three conditions:</p>
<ul>
<li><strong>High atomic number:</strong> $\alpha \propto Z^3$, because inner atomic electrons spend greater time inside the nucleus.</li>
<li><strong>Low transition energy:</strong> $\alpha \propto E_\gamma^{-(L + 5/2)}$.</li>
<li><strong>High multipolarity:</strong> $\alpha$ increases dramatically with multipole order $L$. For $0^+ \to 0^+$ transitions (e.g., $^{16}\text{O}^*$ at $6.05\text{ MeV}$, $^{72}\text{Ge}$), single photon emission is forbidden ($\lambda_\gamma = 0$), forcing decay to occur 100% via internal conversion ($\alpha = \infty$) or $e^+e^-$ pair conversion.</li>
</ul>

<h4>2. Four Primary Photon Interactions with Matter</h4>
<p>As gamma-ray photons traverse matter, they do not lose energy continuously; instead, they undergo catastrophic single-interaction scattering or absorption events characterized by a linear attenuation coefficient $\mu(E_\gamma)$:</p>
<div class="math-display">
$$I(x) = I_0 e^{-\mu x} = I_0 e^{-(\sigma_{\text{pe}} + \sigma_{\text{C}} + \sigma_{\text{pp}}) n x}$$
</div>
<ol>
<li><strong>Photoelectric Absorption ($\sigma_{\text{pe}} \propto Z^{4-5} / E_\gamma^{3.5}$):</strong> The photon is completely absorbed by a bound atomic electron, which is ejected with kinetic energy $T_e = E_\gamma - B_K$. Dominates at low energies ($E_\gamma < 0.1\text{ MeV}$) and in high-$Z$ absorbers (e.g., Lead, $Z=82$).</li>
<li><strong>Compton Scattering ($\sigma_C \propto Z / E_\gamma$):</strong> Inelastic scattering of the photon from a quasi-free electron. By energy-momentum conservation, the scattered photon energy is given by the Compton formula:
<div class="math-display">
$$E_\gamma' = \frac{E_\gamma}{1 + \frac{E_\gamma}{m_e c^2}(1 - \cos\theta)}$$
</div>
The scattered electron recoils with kinetic energy $T_e = E_\gamma - E_\gamma'$, reaching its maximum at backscattering ($\theta = 180^\circ$), defining the sharp <strong>Compton edge</strong> in gamma spectroscopy:
<div class="math-display">
$$T_{\text{max}} = E_\gamma \left[ \frac{2 E_\gamma / m_e c^2}{1 + 2 E_\gamma / m_e c^2} \right]$$
</div>
Compton scattering dominates in the intermediate energy regime ($0.5\text{ MeV} < E_\gamma < 5\text{ MeV}$).</li>
<li><strong>Pair Production ($\sigma_{\text{pp}} \propto Z^2 \ln(E_\gamma)$):</strong> In the strong Coulomb field of an atomic nucleus, a high-energy photon transforms into an electron-positron pair: $\gamma \to e^- + e^+$. Requires a strict threshold energy $E_{\text{threshold}} = 2 m_e c^2 = 1.022\text{ MeV}$. Dominates at high energies ($E_\gamma > 5 - 10\text{ MeV}$). Subsequent positron annihilation produces two collinear $511\text{ keV}$ annihilation photons.</li>
<li><strong>Photonuclear Reactions ($\gamma, n$):</strong> For photon energies exceeding the nuclear neutron separation energy ($E_\gamma > S_n \sim 7 - 10\text{ MeV}$), the photon excites the Giant Dipole Resonance (GDR), ejecting a neutron.</li>
</ol>"""
        }
    ],
    "problems": [
        {
            "id": "nuc-p-3-1",
            "title": "Alpha Decay Energetics and Recoil Kinetic Energy in Uranium-238",
            "statement": "The parent nucleus $^{238}_{92}\\text{U}$ decays via alpha emission into $^{234}_{90}\\text{Th}$. The atomic masses are: $M(^{238}\\text{U}) = 238.050788 \\text{ u}$, $M(^{234}\\text{Th}) = 234.043601 \\text{ u}$, and $M(^4\\text{He}) = 4.002603 \\text{ u}$. (a) Calculate the total disintegration energy $Q_\\alpha$ in $\\text{MeV}$. (b) Determine the kinetic energy of the emitted alpha particle $T_\\alpha$ and the recoiling $^{234}\\text{Th}$ daughter nucleus $T_D$. (c) If the daughter recoil velocity is $v_D$, compute $v_D$ and verify that the daughter recoil energy exceeds typical chemical bond strengths ($3 - 5\\text{ eV}$) by five orders of magnitude.",
            "steps": [
                {
                    "stepName": "Step 1: Compute Mass Defect and Q-Value",
                    "math": r"\Delta m = M(^{238}\text{U}) - M(^{234}\text{Th}) - M(^4\text{He}) = 238.050788\text{ u} - (234.043601 + 4.002603)\text{ u} = 0.004584\text{ u}",
                    "explanation": "Subtract daughter and alpha atomic masses from parent mass."
                },
                {
                    "stepName": "Step 2: Convert to Energy in MeV",
                    "math": r"Q_\alpha = \Delta m \times 931.494\text{ MeV/u} = (0.004584\text{ u}) \times 931.494\text{ MeV/u} \approx 4.270\text{ MeV}",
                    "explanation": "Multiply mass defect in u by 931.494 MeV/u."
                },
                {
                    "stepName": "Step 3: Calculate Kinetic Energy Sharing",
                    "math": r"T_\alpha = Q_\alpha \frac{M_D}{M_D + M_\alpha} = 4.270\text{ MeV} \times \frac{234.04}{238.05} \approx 4.198\text{ MeV}",
                    "explanation": "Apply non-relativistic momentum conservation sharing."
                },
                {
                    "stepName": "Step 4: Calculate Daughter Recoil Energy and Velocity",
                    "math": r"T_D = Q_\alpha - T_\alpha = 4.270\text{ MeV} - 4.198\text{ MeV} = 0.072\text{ MeV} = 72.0\text{ keV}",
                    "explanation": "Evaluate daughter recoil energy."
                },
                {
                    "stepName": "Step 5: Compute Recoil Velocity",
                    "math": r"v_D = \sqrt{\frac{2 T_D}{M_D}} = c \sqrt{\frac{2 \times 0.072\text{ MeV}}{234.04 \times 931.5\text{ MeV}}} = c \sqrt{6.604 \times 10^{-7}} \approx 8.13 \times 10^{-4} c \approx 2.44 \times 10^5\text{ m/s}",
                    "explanation": "Evaluate velocity: 244 km/s. The 72 keV recoil energy vastly exceeds molecular bond strengths (5 eV), destroying the lattice."
                }
            ],
            "answer": "Q_\\alpha = 4.270 \\text{ MeV}, \\quad T_\\alpha = 4.198 \\text{ MeV}, \\quad T_D = 72.0 \\text{ keV}, \\quad v_D = 2.44 \\times 10^5 \\text{ m/s}"
        },
        {
            "id": "nuc-p-3-2",
            "title": "Beta Decay End-Point Energy and Maximum Neutrino Energy in Carbon-14",
            "statement": "Carbon-14 ($^{14}_6\\text{C}$) decays to $^{14}_7\\text{N}$ via beta-minus emission with atomic masses: $M(^{14}\\text{C}) = 14.003242 \\text{ u}$ and $M(^{14}\\text{N}) = 14.003074 \\text{ u}$. (a) Calculate the total decay energy $Q_{\\beta^-}$ in $\\text{keV}$. (b) If an emitted beta electron is detected with kinetic energy $T_e = 45.0 \\text{ keV}$, calculate the simultaneous kinetic energy carried away by the antineutrino $T_{\\bar{\\nu}}$ (assuming negligible daughter recoil). (c) Given that the half-life of $^{14}\\text{C}$ is $5730\\text{ years}$, calculate the comparative half-life parameter $\\log_{10}(f t)$ and classify the transition.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Mass Difference and Q-Value",
                    "math": r"\Delta m = M(^{14}\text{C}) - M(^{14}\text{N}) = 14.003242\text{ u} - 14.003074\text{ u} = 0.000168\text{ u}",
                    "explanation": "Find neutral atomic mass difference for beta-minus decay."
                },
                {
                    "stepName": "Step 2: Convert to keV",
                    "math": r"Q_{\beta^-} = \Delta m \times 931494\text{ keV/u} = (0.000168\text{ u}) \times 931494\text{ keV/u} \approx 156.5\text{ keV}",
                    "explanation": "Calculate Q-value in keV."
                },
                {
                    "stepName": "Step 3: Determine Antineutrino Kinetic Energy",
                    "math": r"T_{\bar{\nu}} \approx Q_{\beta^-} - T_e = 156.5\text{ keV} - 45.0\text{ keV} = 111.5\text{ keV}",
                    "explanation": "Subtract electron kinetic energy from total Q-value."
                },
                {
                    "stepName": "Step 4: Compute Log ft Value",
                    "math": r"t_{1/2} = 5730\text{ y} \approx 1.808 \times 10^{11}\text{ s}, \quad f \approx 1.67 \times 10^{-6} \implies f t \approx 3.02 \times 10^5 \implies \log_{10}(f t) \approx 9.04",
                    "explanation": "The large log ft value (9.04) classifies the 14C -> 14N (0+ -> 1+) transition as an 'allowed Gamow-Teller' transition with strong nuclear matrix element cancellation (anomalously slow)."
                }
            ],
            "answer": "Q_{\\beta^-} = 156.5 \\text{ keV}, \\quad T_{\\bar{\\nu}} = 111.5 \\text{ keV}, \\quad \\log_{10}(ft) \\approx 9.04 \\quad (\\text{Hindered Allowed } GT)"
        },
        {
            "id": "nuc-p-3-3",
            "title": "Gamma Multipolarity Classification and Weisskopf Decay Rate",
            "statement": "An excited state of $^{137}_{56}\\text{Ba}$ at an excitation energy of $E^* = 661.7 \\text{ keV}$ has spin-parity $I_i^{\\pi} = 11/2^-$ and de-excites to the ground state with $I_f^{\\pi} = 3/2^+$. (a) Determine the allowed electromagnetic multipole orders $L$ and their electric or magnetic character ($EL$ or $ML$). (b) Identify the dominant multipole transition mode. (c) Using the Weisskopf single-particle formula for this multipole order ($A = 137, E_\\gamma = 0.662\\text{ MeV}$), estimate the theoretical transition rate $\\lambda_W$ and the expected half-life $T_{1/2}$.",
            "steps": [
                {
                    "stepName": "Step 1: Determine Allowed Angular Momentum L",
                    "math": r"|I_i - I_f| \le L \le I_i + I_f \implies |11/2 - 3/2| \le L \le 11/2 + 3/2 \implies 4 \le L \le 7",
                    "explanation": "Conservation of angular momentum allows multipoles L = 4, 5, 6, 7."
                },
                {
                    "stepName": "Step 2: Determine Parity and Radiation Type",
                    "math": r"\pi_i \pi_f = (-1) \times (+1) = -1. \quad \text{For } L=4: \quad \pi(E4) = (-1)^4 = +1 \ (\text{No}), \quad \pi(M4) = (-1)^{4+1} = -1 \ (\text{Yes!})",
                    "explanation": "Because parity changes (- to +), odd parity operators are required. For L=4, M4 has parity (-1)^5 = -1, matching the transition."
                },
                {
                    "stepName": "Step 3: Dominant Multipole Order",
                    "math": r"\text{Lowest allowed multipole is } M4 \ (L=4). \quad (\text{Next is } E5 \text{ which is suppressed by } 10^5). \implies \text{Dominant mode: } M4",
                    "explanation": "Identify dominant multipolarity as M4 (hexadecapole magnetic)."
                },
                {
                    "stepName": "Step 4: Compute Weisskopf Single-Particle Rate for M4",
                    "math": r"\lambda_W(M4) \approx 3.0 \times 10^{-6} A^2 E_\gamma^9\text{ s}^{-1} = (3.0 \times 10^{-6})(137)^2 (0.6617)^9 \approx 3.0 \times 10^{-6} \times 18769 \times 0.0240 \approx 0.00135\text{ s}^{-1}",
                    "explanation": "Evaluate Weisskopf single-particle rate for L=4 magnetic."
                },
                {
                    "stepName": "Step 5: Calculate Theoretical Half-Life",
                    "math": r"T_{1/2} = \frac{\ln(2)}{\lambda_W} \approx \frac{0.693}{0.00135\text{ s}^{-1}} \approx 513\text{ s} \approx 2.55\text{ minutes}",
                    "explanation": "Evaluate half-life: approximately 2.5 minutes (experimental T_1/2 of 137mBa is 2.55 minutes, extraordinary agreement!)."
                }
            ],
            "answer": "\\text{Allowed: } M4, E5, M6, E7; \\quad \\text{Dominant: } M4; \\quad \\lambda_W \\approx 1.35 \\times 10^{-3} \\text{ s}^{-1}, \\quad T_{1/2} \\approx 2.55 \\text{ min}"
        }
    ]
}

# ==========================================
# UNIT 4: Nuclear Reactions, Fission & Thermonuclear Fusion
# ==========================================
u4 = {
    "unitNumber": 4,
    "unitId": "unit4-nuclear-reactions-fission-fusion",
    "title": "Nuclear Reactions, Fission & Thermonuclear Fusion",
    "description": "Exhaustive dynamics of nuclear interactions: reaction kinematics in laboratory and center-of-mass frames, Q-value equations, threshold energies; reaction cross-sections, Breit-Wigner single-level resonance, optical model; direct reactions versus the Bohr compound nucleus hypothesis; nuclear fission physics, liquid drop deformation barrier, mass yield asymmetry, prompt and delayed neutron emissions; four-factor formula and nuclear reactor kinetics; stellar nucleosynthesis (proton-proton chain, CNO cycle) and thermonuclear fusion physics (Lawson criterion, magnetic confinement).",
    "sections": [
        {
            "id": "nuc-4-1",
            "title": "Reaction Kinematics: Laboratory vs CM Frames & Threshold Energy",
            "simulation": "nuc-reaction-kinematics-sim",
            "content": r"""<h4>1. General Nuclear Reaction Formulation & Q-Value</h4>
<p>A generic two-body nuclear reaction is denoted as $a + X \to Y + b$ or in compact Bethe notation $X(a, b)Y$, where projectile $a$ strikes stationary target nucleus $X$, producing ejectile $b$ and residual nucleus $Y$. The <strong>reaction $Q$-value</strong> is defined as the invariant rest-mass energy difference:</p>
<div class="math-display">
$$Q = [ (M_a + M_X) - (M_b + M_Y) ] c^2 = (T_b + T_Y) - T_a$$
</div>
<ul>
<li><strong>Exothermic Reactions ($Q > 0$):</strong> Mass is converted into kinetic energy. The reaction can occur even at zero incident projectile energy ($T_a \to 0$).</li>
<li><strong>Endothermic Reactions ($Q < 0$):</strong> Kinetic energy is converted into mass. The reaction is forbidden unless the projectile delivers a kinetic energy exceeding a strict <strong>threshold energy</strong> $E_{\text{th}}$.</li>
</ul>

<h4>2. Laboratory vs Center-of-Mass (CM) Transformation</h4>
<p>In the laboratory frame, the total momentum is $p_{\text{lab}} = p_a = \sqrt{2 M_a T_a}$. The velocity of the center-of-mass frame is:</p>
<div class="math-display">
$$v_{\text{cm}} = \frac{M_a}{M_a + M_X} v_a$$
</div>
<p>The total kinetic energy available in the center-of-mass frame ($T_{\text{cm}}$) represents the fraction of laboratory energy available to induce nuclear transformations (the remainder $T_{\text{cm, motion}} = \frac{1}{2}(M_a + M_X)v_{\text{cm}}^2$ is locked up in rigid motion of the system):</p>
<div class="math-display">
$$T_{\text{cm}} = \frac{1}{2} \mu v_{\text{rel}}^2 = \frac{M_X}{M_a + M_X} T_a$$
</div>
<p>where $\mu = \frac{M_a M_X}{M_a + M_X}$ is the reduced mass.</p>

<h4>3. Derivation of Reaction Threshold Energy</h4>
<p>For an endothermic reaction ($Q < 0$), the reaction can occur if and only if the center-of-mass kinetic energy is at least sufficient to supply the mass deficit: $T_{\text{cm}} \ge |Q|$. Substituting $T_{\text{cm}}$ gives the threshold laboratory kinetic energy:</p>
<div class="math-display">
$$\frac{M_X}{M_a + M_X} E_{\text{th}} = |Q| \implies E_{\text{th}} = |Q| \left( \frac{M_a + M_X}{M_X} \right) = |Q| \left( 1 + \frac{M_a}{M_X} \right)$$
</div>
<p>If Coulomb forces are present (charged projectile and target), the projectile must also overcome or tunnel through the Coulomb barrier $V_C = \frac{1}{4\pi\varepsilon_0}\frac{Z_a Z_X e^2}{R_a + R_X}$, significantly elevating the effective practical threshold.</p>"""
        },
        {
            "id": "nuc-4-2",
            "title": "Cross-Sections, Breit-Wigner Resonances & The Optical Model",
            "content": r"""<h4>1. Reaction Cross-Section & Beam Attenuation</h4>
<p>The reaction probability is quantified by the <strong>cross-section $\sigma$</strong>, possessing units of area (standard unit: $1\text{ barn (b)} \equiv 10^{-28}\text{ m}^2 = 100\text{ fm}^2$). For a uniform projectile beam of flux $\Phi = n_a v_a$ (particles per unit area per second) incident on a thin target containing $N_{\text{t}}$ target nuclei per unit area, the reaction rate $R$ is:</p>
<div class="math-display">
$$R = \Phi N_{\text{t}} \sigma$$
</div>
<p>For a thick target of mass density $\rho$ and thickness $x$, the unscattered beam intensity decreases exponentially:</p>
<div class="math-display">
$$I(x) = I_0 e^{-\Sigma_t x} = I_0 e^{-n_X \sigma_t x}, \quad \Sigma_t = \frac{\rho N_A}{A} \sigma_t$$
</div>
<p>where $\Sigma_t$ is the macroscopic total cross-section ($\text{cm}^{-1}$).</p>

<h4>2. Breit-Wigner Single-Level Resonance Formula</h4>
<p>When the incident projectile energy matches a quasi-bound quantum level of the composite system ($E_0$), the cross-section displays a dramatic, sharp peak called a <strong>resonance</strong>. Gregory Breit and Eugene Wigner derived the cross-section for isolated s-wave ($\ell = 0$) resonance reactions using quantum scattering theory:</p>
<div class="math-display">
$$\sigma(a, b) = \pi \lambda\hspace{-0.45em}\bar{}^2 g \frac{\Gamma_a \Gamma_b}{(E - E_0)^2 + (\Gamma / 2)^2}$$
</div>
<p>where:</p>
<ul>
<li>$\lambda\hspace{-0.45em}\bar{} = \frac{\lambda}{2\pi} = \frac{\hbar}{p_{\text{cm}}}$ is the reduced de Broglie wavelength of the incident channel.</li>
<li>$\Gamma = \Gamma_a + \Gamma_b + \Gamma_\gamma + \dots$ is the total resonance energy width, related to the compound state lifetime by $\tau = \hbar / \Gamma$.</li>
<li>$\Gamma_a, \Gamma_b$ are partial decay widths for the entrance and exit channels.</li>
<li>$g = \frac{2 J + 1}{(2 s_a + 1)(2 I_X + 1)}$ is the spin statistical factor for compound nuclear spin $J$.</li>
</ul>
<p>At the peak ($E = E_0$), the maximum cross-section is $\sigma_{\text{peak}} = 4\pi \lambda\hspace{-0.45em}\bar{}^2 g \frac{\Gamma_a \Gamma_b}{\Gamma^2}$. For slow neutrons where $\lambda \sim 10^{-10}\text{ m} \gg R$, thermal resonance cross-sections can reach tens of thousands of barns (e.g., $^{113}\text{Cd}$ has $\sigma \approx 20,000\text{ b}$, $^{135}\text{Xe}$ has $\sigma \approx 2.6 \times 10^6\text{ b}$).</p>

<h4>3. The Optical Model Potential</h4>
<p>To describe both elastic scattering and non-elastic absorption of nucleons by nuclei, Herman Feshbach introduced the <strong>optical model</strong>, representing the nucleus as a refractive, cloudy crystal ball with a complex potential:</p>
<div class="math-display">
$$U(r) = - V(r) - i W(r) + V_{\text{so}}(r) (\vec{\ell}\cdot\vec{s})$$
</div>
<p>The real depth $V(r) \approx 50\text{ MeV}$ governs nuclear refraction (elastic scattering), while the imaginary depth $W(r) \approx 5 - 15\text{ MeV}$ acts as an energy sink, absorbing flux from the incident channel to simulate all possible inelastic, transfer, and compound nuclear reactions.</p>"""
        },
        {
            "id": "nuc-4-3",
            "title": "Reaction Mechanisms: Direct Reactions vs Compound Nucleus",
            "content": r"""<h4>1. Niels Bohr's Compound Nucleus Hypothesis (1936)</h4>
<p>Niels Bohr proposed that low-energy nuclear reactions proceed through a distinct two-stage process:</p>
<div class="math-display">
$$a + X \longrightarrow C^* \longrightarrow Y + b$$
</div>
<ol>
<li><strong>Formation:</strong> The projectile enters the target and undergoes repeated collisions with multiple nucleons, dissipating its kinetic energy across the whole nucleus to form an excited <strong>compound nucleus</strong> $C^*$. The formation time is $\tau_{\text{form}} \sim 10^{-22}\text{ s}$ (nuclear transit time).</li>
<li><strong>Independence Hypothesis:</strong> The compound nucleus survives for a long duration ($\tau_C \sim 10^{-16} - 10^{-18}\text{ s}$, thousands of times longer than transit time) during which all memory of the entrance channel ($a+X$) is completely erased, except for exact conserved quantum numbers (energy $E$, angular momentum $J$, and parity $\pi$).</li>
<li><strong>Decay:</strong> De-excitation occurs through statistical evaporation when fluctuations concentrate sufficient energy on a single particle or photon channel:
<div class="math-display">
$$\sigma(a, b) = \sigma_{\text{form}}(C^*) \times P_{\text{decay}}(b)$$
</div>
</li>
</ol>
<p>Compound reactions produce <strong>isotropic or forward-backward symmetric</strong> angular distributions in the center-of-mass frame ($\frac{d\sigma}{d\Omega}(\theta) = \frac{d\sigma}{d\Omega}(\pi - \theta)$).</p>

<h4>2. Direct Reactions (Stripping & Pickup)</h4>
<p>At higher incident energies ($E \gtrsim 20 - 100\text{ MeV}$), the projectile traverses the nucleus in a single passage ($\tau \sim 10^{-22}\text{ s}$) and interacts with only one or two valence nucleons at the nuclear surface:</p>
<ul>
<li><strong>Stripping Reactions:</strong> The projectile deposits one or more nucleons into a single-particle orbit of the target nucleus, while the remainder continues forward (e.g., $(d, p)$ stripping deposits a neutron).</li>
<li><strong>Pickup Reactions:</strong> The projectile scoops up a nucleon from the target (e.g., $(p, d)$ picks up a neutron).</li>
</ul>
<p>Direct reactions display strong <strong>forward-peaked</strong> angular distributions whose diffraction peaks depend uniquely on the transferred orbital angular momentum $\ell$, providing a powerful experimental probe of single-particle shell structures.</p>"""
        },
        {
            "id": "nuc-4-4",
            "title": "Nuclear Fission: Deformation Barrier, Mass Yield & Neutrons",
            "simulation": "nuc-fission-chain-reaction-sim",
            "content": r"""<h4>1. Liquid Drop Model Explanation of Nuclear Fission</h4>
<p>In 1939, Otto Frisch and Lise Meitner interpreted Otto Hahn and Fritz Strassmann's discovery of barium in neutron-irradiated uranium as the binary splitting—<strong>nuclear fission</strong>—of the heavy uranium nucleus. Niels Bohr and John Wheeler parameterized the stability of a spherical drop deformed into a prolate spheroid with eccentricity $\varepsilon$:</p>
<div class="math-display">
$$R(\theta) = R_0 [1 + \alpha_2 P_2(\cos\theta)], \quad E_{\text{def}} = \Delta E_S + \Delta E_C \approx E_S^{(0)} \left( \frac{2}{5} \alpha_2^2 \right) + E_C^{(0)} \left( - \frac{1}{5} \alpha_2^2 \right)$$
</div>
<p>The deformed droplet is stable against spontaneous fission if $E_{\text{def}} > 0$. The threshold for spontaneous instability occurs when Coulomb repulsion exceeds twice surface tension:</p>
<div class="math-display">
$$\frac{E_C^{(0)}}{2 E_S^{(0)}} \ge 1 \implies \frac{a_c Z^2 / A^{1/3}}{2 a_s A^{2/3}} \ge 1 \implies \frac{Z^2}{A} \ge \frac{2 a_s}{a_c} \approx \frac{2 \times 17.8}{0.711} \approx 50$$
</div>
<p>The ratio $x = \frac{Z^2 / A}{(Z^2 / A)_{\text{crit}}} \approx \frac{Z^2 / A}{48}$ is the <strong>fissility parameter</strong>. For $^{238}_{92}\text{U}$, $Z^2/A \approx 35.6$, resulting in a finite fission barrier height $E_f \approx 5.8\text{ MeV}$.</p>

<h4>2. Energy Release in Fission</h4>
<p>For a typical heavy nucleus ($A \approx 236$), $B/A \approx 7.6\text{ MeV}$, while the medium-mass fission fragments have $B/A \approx 8.5\text{ MeV}$. The energy released per fission event is:</p>
<div class="math-display">
$$Q_{\text{fission}} \approx A [ (B/A)_{\text{fragments}} - (B/A)_{\text{parent}} ] \approx 236 \times (8.5 - 7.6)\text{ MeV} \approx 200\text{ MeV}$$
</div>
<p>The $200\text{ MeV}$ is partitioned as follows:</p>
<ul>
<li><strong>Fragment Kinetic Energy:</strong> $\approx 168\text{ MeV}$ ($84\%$, deposited immediately as heat within a few micrometers).</li>
<li><strong>Prompt Fission Neutrons:</strong> $\approx 5\text{ MeV}$ (average $2 - 3$ neutrons per fission, mean kinetic energy $\sim 2\text{ MeV}$).</li>
<li><strong>Prompt Gamma Rays:</strong> $\approx 7\text{ MeV}$.</li>
<li><strong>Delayed Beta Particles:</strong> $\approx 8\text{ MeV}$ from fragment radioactive decay chains.</li>
<li><strong>Delayed Antineutrinos:</strong> $\approx 12\text{ MeV}$ (escapes the reactor without depositing heat).</li>
</ul>

<h4>3. Mass Yield Asymmetry & Fission Neutrons</h4>
<p>Low-energy thermal neutron fission of $^{235}\text{U}$ produces an asymmetric two-humped mass yield curve with peaks at light mass $A_L \approx 95$ and heavy mass $A_H \approx 140$. Symmetric fission ($A_1 = A_2 \approx 118$) is suppressed by a factor of 600 due to shell closures in the nascent fragments ($Z=50, N=82$). At high excitation energies ($E_n > 50\text{ MeV}$), shell effects wash out and symmetric fission dominates.</p>
<p>Fission releases an average of $\bar{\nu} \approx 2.43$ neutrons per event for $^{235}\text{U}$. Crucially, approximately $0.65\%$ of these neutrons are <strong>delayed neutrons</strong> emitted seconds to minutes later by beta-decay precursors (e.g., $^{87}\text{Br} \to {^{87}\text{Kr}} \to {^{86}\text{Kr}} + n$), providing the indispensable time delay required for mechanical control rods to safely stabilize nuclear power reactors.</p>"""
        },
        {
            "id": "nuc-4-5",
            "title": "Controlled Fission: Four-Factor Formula & Reactor Kinetics",
            "content": r"""<h4>1. The Neutron Multiplication Factor (k)</h4>
<p>The continuity of a nuclear fission chain reaction is dictated by the effective multiplication factor $k_{\text{eff}}$, defined as the ratio of neutrons in generation $n+1$ to neutrons in generation $n$:</p>
<ul>
<li>$k_{\text{eff}} < 1$: <strong>Subcritical</strong> (neutron population and fission power die away exponentially).</li>
<li>$k_{\text{eff}} = 1$: <strong>Critical</strong> (steady, self-sustaining stationary power generation).</li>
<li>$k_{\text{eff}} > 1$: <strong>Supercritical</strong> (neutron flux grows exponentially).</li>
</ul>

<h4>2. Fermi's Four-Factor Formula ($k_\infty$)</h4>
<p>In an infinitely extended homogeneous or heterogeneous reactor core (ignoring surface neutron leakage), the multiplication factor is governed by the <strong>Four-Factor Formula</strong>:</p>
<div class="math-display">
$$k_\infty = \varepsilon \cdot p \cdot \eta \cdot f$$
</div>
<ol>
<li><strong>Fast Fission Factor ($\varepsilon \approx 1.03 - 1.08$):</strong> Ratio of total neutrons produced by both fast and thermal fissions to those produced solely by thermal fissions.</li>
<li><strong>Resonance Escape Probability ($p \approx 0.85 - 0.92$):</strong> The probability that a fast fission neutron slows down through the dangerous intermediate resonance capture region of $^{238}\text{U}$ ($1 - 1000\text{ eV}$) without being absorbed. Heterogeneous fuel lump arrangements maximize $p$ through spatial self-shielding.</li>
<li><strong>Thermal Utilization Factor ($f \approx 0.70 - 0.90$):</strong> The probability that a completely moderated thermal neutron is absorbed in the nuclear fuel rather than in the moderator, structural cladding, or control poisons:
<div class="math-display">
$$f = \frac{\Sigma_a^{\text{fuel}}}{\Sigma_a^{\text{fuel}} + \Sigma_a^{\text{other}}}$$
</div></li>
<li><strong>Neutron Reproduction Factor ($\eta \approx 1.3 - 2.1$):</strong> The average number of fission neutrons emitted per thermal neutron absorbed in the fuel:
<div class="math-display">
$$\eta = \nu \frac{\Sigma_f^{\text{fuel}}}{\Sigma_a^{\text{fuel}}}$$
</div></li>
</ol>

<h4>3. Reactor Kinetics and Prompt Criticality</h4>
<p>If all fission neutrons were prompt, the average neutron lifetime would be $\ell \sim 10^{-4}\text{ s}$ (in a thermal reactor). The reactor power would evolve as $P(t) = P_0 e^{(k - 1)t / \ell}$. Even a $0.1\%$ excess ($k = 1.001$) would cause power to escalate by $e^{10} \approx 22,000$ in one second, rendering reactor control physically impossible.</p>
<p>With delayed neutron fraction $\beta \approx 0.0065$, the effective mean lifetime is extended to $\bar{\ell} = (1 - \beta)\ell + \sum \beta_i \tau_i \approx 0.08 - 0.1\text{ seconds}$. Provided $k_{\text{eff}} < 1 + \beta$, the reactor is <strong>delayed critical</strong> and responds smoothly over human and mechanical timescales.</p>"""
        },
        {
            "id": "nuc-4-6",
            "title": "Thermonuclear Fusion: Stellar Cycles & The Lawson Criterion",
            "simulation": "nuc-thermonuclear-fusion-sim",
            "content": r"""<h4>1. Stellar Nucleosynthesis: The Proton-Proton Chain</h4>
<p>In main-sequence stars like our Sun ($T_{\text{core}} \approx 1.5 \times 10^7\text{ K}$, $k_B T \approx 1.3\text{ keV}$), stellar energy generation is powered by the fusion of four protons into helium-4 ($4 p \to {^4\text{He}} + 2 e^+ + 2 \nu_e + 26.73\text{ MeV}$). The dominant sequence is the <strong>$p$-$p$ chain</strong>:</p>
<ol>
<li><strong>$p + p \to {^2\text{H}} + e^+ + \nu_e$ ($Q = 1.442\text{ MeV}$):</strong> Weak interaction bottle-neck process ($p \to n + e^+ + \nu_e$) with an extraordinarily tiny cross-section ($\sigma \sim 10^{-47}\text{ cm}^2$). A proton in the solar core waits an average of $10^9\text{ years}$ to undergo this reaction, ensuring the Sun's multi-billion-year stability.</li>
<li><strong>$^2\text{H} + p \to {^3\text{He}} + \gamma$ ($Q = 5.493\text{ MeV}$):</strong> Rapid electromagnetic capture ($\sim 1\text{ second}$).</li>
<li><strong>$^3\text{He} + {^3\text{He}} \to {^4\text{He}} + 2 p$ ($Q = 12.86\text{ MeV}$, $pp\text{-I}$ branch):</strong> Completes the synthesis of $^4\text{He}$.</li>
</ol>
<p>In heavier, hotter stars ($T > 2 \times 10^7\text{ K}$), the catalytic <strong>CNO cycle</strong> ($^{12}\text{C} \to {^{13}\text{N}} \to {^{13}\text{C}} \to {^{14}\text{N}} \to {^{15}\text{O}} \to {^{15}\text{N}} \to {^{12}\text{C}} + {^4\text{He}}$) dominates due to its steeper temperature dependence ($\epsilon_{\text{CNO}} \propto T^{17}$ vs $\epsilon_{pp} \propto T^4$).</p>

<h4>2. Controlled Terrestrial Fusion: The D-T Reaction</h4>
<p>For magnetic confinement fusion (tokamaks, stellarators), the most accessible reaction is Deuterium-Tritium fusion:</p>
<div class="math-display">
$$^2_1\text{H} + {^3_1\text{H}} \longrightarrow {^4_2\text{He}} (3.5\text{ MeV}) + n (14.1\text{ MeV}) \quad (Q = 17.59\text{ MeV})$$
</div>
<p>The D-T reaction possesses the lowest Coulomb barrier and highest cross-section ($\sigma_{\text{peak}} \approx 5.0\text{ b}$ at $E_{\text{cm}} \approx 64\text{ keV}$, accessible at thermal plasma temperatures $T \sim 15\text{ keV} \approx 1.7 \times 10^8\text{ K}$). The Gamow window represents the convolution of the Maxwell-Boltzmann tail $e^{-E / k_B T}$ with the quantum tunneling transmission $e^{-b / \sqrt{E}}$.</p>

<h4>3. The Lawson Criterion & Triple Product</h4>
<p>In 1957, J. D. Lawson formulated the ignition condition where thermonuclear self-heating by alpha particles ($E_\alpha = 3.5\text{ MeV}$) exceeds plasma Bremsstrahlung radiation and conduction losses without external heating:</p>
<div class="math-display">
$$n \cdot \tau_E \ge \frac{12 k_B T}{\langle \sigma v \rangle Q_\alpha}$$
</div>
<p>where $n$ is fuel ion density and $\tau_E$ is the energy confinement time. For D-T fusion at the optimum temperature $T \approx 15\text{ keV}$, this requires the famous <strong>fusion triple product</strong>:</p>
<div class="math-display">
$$n \cdot T \cdot \tau_E \ge 3 \times 10^{21}\text{ keV}\cdot\text{s}\cdot\text{m}^{-3} \approx 5 \times 10^{28}\text{ K}\cdot\text{s}\cdot\text{m}^{-3}$$
</div>
<p>Magnetic confinement achieves this at low density and high confinement ($n \sim 10^{20}\text{ m}^{-3}, \tau_E \sim 3\text{ s}$), while inertial confinement uses extreme compression ($n \sim 10^{31}\text{ m}^{-3}, \tau_E \sim 10^{-10}\text{ s}$).</p>"""
        }
    ],
    "problems": [
        {
            "id": "nuc-p-4-1",
            "title": "Threshold Kinetic Energy and Kinematics of Nitrogen-14 Alpha Reaction",
            "statement": "The historical Rutherford nuclear reaction is $^{14}_7\\text{N}(\\alpha, p)^{17}_8\\text{O}$. The atomic masses are: $M(^{14}\\text{N}) = 14.003074 \\text{ u}$, $M(^4\\text{He}) = 4.002603 \\text{ u}$, $M(^1\\text{H}) = 1.007825 \\text{ u}$, and $M(^{17}\\text{O}) = 16.999131 \\text{ u}$. (a) Calculate the reaction $Q$-value in $\\text{MeV}$. Is the reaction endothermic or exothermic? (b) Determine the minimum threshold kinetic energy $E_{\\text{th}}$ of the incident alpha particle in the laboratory frame. (c) If the incident alpha particle has laboratory energy $T_\\alpha = 7.70 \\text{ MeV}$, find the total kinetic energy available in the center-of-mass frame.",
            "steps": [
                {
                    "stepName": "Step 1: Compute Mass Difference and Q-Value",
                    "math": r"\Delta m = [M(^{14}\text{N}) + M(^4\text{He})] - [M(^1\text{H}) + M(^{17}\text{O})] = [14.003074 + 4.002603] - [1.007825 + 16.999131]\text{ u} = -0.001279\text{ u}",
                    "explanation": "Subtract product masses from reactant masses."
                },
                {
                    "stepName": "Step 2: Convert Q-Value to MeV",
                    "math": r"Q = (-0.001279\text{ u}) \times 931.494\text{ MeV/u} \approx -1.1914\text{ MeV}",
                    "explanation": "Because Q < 0, the reaction is endothermic."
                },
                {
                    "stepName": "Step 3: Calculate Threshold Laboratory Kinetic Energy",
                    "math": r"E_{\text{th}} = |Q| \left( 1 + \frac{M_\alpha}{M_N} \right) = 1.1914\text{ MeV} \times \left( 1 + \frac{4.0026}{14.0031} \right) \approx 1.1914 \times (1 + 0.2858) \approx 1.532\text{ MeV}",
                    "explanation": "Calculate minimum projectile energy required in laboratory frame."
                },
                {
                    "stepName": "Step 4: Center-of-Mass Kinetic Energy at 7.70 MeV",
                    "math": r"T_{\text{cm}} = T_\alpha \left( \frac{M_N}{M_\alpha + M_N} \right) = 7.70\text{ MeV} \times \left( \frac{14.0031}{18.0057} \right) \approx 7.70 \times 0.7777 \approx 5.988\text{ MeV}",
                    "explanation": "Compute available CM energy at 7.70 MeV."
                }
            ],
            "answer": "Q = -1.191 \\text{ MeV} \\quad (\\text{Endothermic}), \\quad E_{\\text{th}} = 1.532 \\text{ MeV}, \\quad T_{\\text{cm}} = 5.988 \\text{ MeV}"
        },
        {
            "id": "nuc-p-4-2",
            "title": "Nuclear Energy Release in Complete Fission of Uranium-235",
            "statement": "A commercial nuclear reactor operates at a thermal power output of $P_{\\text{th}} = 3000 \\text{ MW}$ ($3.0 \\times 10^9 \\text{ J/s}$). Assuming an average usable energy release of $Q = 200 \\text{ MeV}$ per fission event of $^{235}_{92}\\text{U}$: (a) Calculate the fission rate (number of fissions per second). (b) Determine the rate of mass consumption of $^{235}\\text{U}$ in kilograms per day. (c) Compare this daily fuel consumption to that of a coal-fired power plant of identical thermal capacity burning coal with a heat of combustion of $29.0 \\text{ MJ/kg}$.",
            "steps": [
                {
                    "stepName": "Step 1: Convert Energy per Fission to Joules",
                    "math": r"E_{\text{fission}} = 200\text{ MeV} \times (1.6022 \times 10^{-13}\text{ J/MeV}) = 3.2044 \times 10^{-11}\text{ J}",
                    "explanation": "Convert 200 MeV to Joules."
                },
                {
                    "stepName": "Step 2: Calculate Fission Rate per Second",
                    "math": r"R_{\text{fiss}} = \frac{P_{\text{th}}}{E_{\text{fission}}} = \frac{3.0 \times 10^9\text{ J/s}}{3.2044 \times 10^{-11}\text{ J}} \approx 9.362 \times 10^{19}\text{ fissions/s}",
                    "explanation": "Divide power by energy per fission."
                },
                {
                    "stepName": "Step 3: Calculate Daily Mass Consumption of Uranium-235",
                    "math": r"m_{\text{day}} = \frac{R_{\text{fiss}} \times 86400\text{ s} \times 0.23504\text{ kg/mol}}{6.0221 \times 10^{23}\text{ mol}^{-1}} = \frac{(8.089 \times 10^{24}) \times 0.23504}{6.0221 \times 10^{23}}\text{ kg} \approx 3.157\text{ kg/day}",
                    "explanation": "Multiply daily fissions by molar mass divided by Avogadro's number: approx 3.16 kg/day."
                },
                {
                    "stepName": "Step 4: Calculate Coal Consumption for Comparison",
                    "math": r"m_{\text{coal}} = \frac{3.0 \times 10^9\text{ J/s} \times 86400\text{ s}}{29.0 \times 10^6\text{ J/kg}} = \frac{2.592 \times 10^{14}\text{ J}}{2.90 \times 10^7\text{ J/kg}} \approx 8.938 \times 10^6\text{ kg/day} \approx 8940\text{ metric tons/day}",
                    "explanation": "Compute coal consumption: 8,940 tonnes per day, demonstrating a ~3,000,000:1 fuel mass density advantage."
                }
            ],
            "answer": "R_{\\text{fiss}} = 9.36 \\times 10^{19} \\text{ s}^{-1}, \\quad m_{\\text{U}} = 3.16 \\text{ kg/day}, \\quad m_{\\text{coal}} = 8940 \\text{ tonnes/day} \\quad (2.83 \\times 10^6 \\times)"
        },
        {
            "id": "nuc-p-4-3",
            "title": "Thermonuclear D-T Fusion Power Density and Lawson Parameter",
            "statement": "In a D-T magnetic confinement fusion reactor, the deuterium and tritium ion densities are equal: $n_D = n_T = \frac{1}{2} n_i = 1.0 \\times 10^{20} \\text{ m}^{-3}$ ($n_i = 2.0 \\times 10^{20} \\text{ m}^{-3}$). At a plasma temperature of $T = 15.0 \\text{ keV}$ ($1.74 \\times 10^8 \\text{ K}$), the reaction rate parameter is $\\langle \\sigma v \\rangle = 2.80 \\times 10^{-22} \\text{ m}^3/\\text{s}$, and each reaction produces $Q = 17.6 \\text{ MeV}$ ($2.82 \\times 10^{-12} \\text{ J}$), including an alpha particle of $E_\\alpha = 3.52 \\text{ MeV}$ ($5.64 \\times 10^{-13} \\text{ J}$). (a) Calculate the total fusion power density $P_f$ in $\\text{MW/m}^3$. (b) Calculate the alpha particle self-heating power density $P_\\alpha$. (c) If the plasma energy confinement time is $\\tau_E = 3.50 \\text{ s}$, evaluate the Lawson ignition parameter and determine if ignition is achieved.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Total Fusion Power Density",
                    "math": r"P_f = n_D n_T \langle \sigma v \rangle Q = (1.0 \times 10^{20})^2 (2.80 \times 10^{-22}\text{ m}^3/\text{s})(2.82 \times 10^{-12}\text{ J}) \approx 7.896 \times 10^6\text{ W/m}^3 = 7.90\text{ MW/m}^3",
                    "explanation": "Evaluate fusion power density P_f."
                },
                {
                    "stepName": "Step 2: Calculate Alpha Self-Heating Power Density",
                    "math": r"P_\alpha = n_D n_T \langle \sigma v \rangle E_\alpha = (1.0 \times 10^{40})(2.80 \times 10^{-22})(5.64 \times 10^{-13}\text{ J}) \approx 1.579 \times 10^6\text{ W/m}^3 = 1.58\text{ MW/m}^3",
                    "explanation": "Evaluate alpha heating power density P_alpha."
                },
                {
                    "stepName": "Step 3: Evaluate Plasma Energy Loss Rate",
                    "math": r"P_{\text{loss}} = \frac{3 n_e k_B T}{\tau_E} = \frac{3 (2.0 \times 10^{20}\text{ m}^{-3})(15.0 \times 1.6022 \times 10^{-16}\text{ J})}{3.50\text{ s}} = \frac{1.442 \times 10^6}{3.50}\text{ W/m}^3 \approx 0.412\text{ MW/m}^3",
                    "explanation": "Calculate plasma thermal energy loss per unit volume."
                },
                {
                    "stepName": "Step 4: Check Ignition Criterion",
                    "math": r"\frac{P_\alpha}{P_{\text{loss}}} = \frac{1.579\text{ MW/m}^3}{0.412\text{ MW/m}^3} \approx 3.83 > 1. \quad \text{Triple Product: } n_i T \tau_E = (2.0 \times 10^{20})(15)(3.5) = 1.05 \times 10^{22}\text{ keV}\cdot\text{s}\cdot\text{m}^{-3} > 3 \times 10^{21}",
                    "explanation": "Because P_alpha exceeds P_loss by a factor of 3.8, alpha self-heating sustains the temperature without auxiliary heating: ignition is robustly achieved."
                }
            ],
            "answer": "P_f = 7.90 \\text{ MW/m}^3, \\quad P_\\alpha = 1.58 \\text{ MW/m}^3, \\quad n T \\tau_E = 1.05 \\times 10^{22} \\text{ keV}\\cdot\\text{s}\\cdot\\text{m}^{-3} \\quad (\\text{Ignition Achieved})"
        }
    ]
}

with open("nuc_u3.json", "w") as f:
    json.dump(u3, f, indent=2)
print("nuc_u3.json created successfully!")

with open("nuc_u4.json", "w") as f:
    json.dump(u4, f, indent=2)
print("nuc_u4.json created successfully!")
