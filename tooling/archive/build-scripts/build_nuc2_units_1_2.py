import json

u1_data = {
    "title": "The Deuteron Problem & Two-Nucleon Bound State",
    "subtitle": "Ground State, Tensor Force, D-State Admixture, Quadrupole Moment & Photodisintegration",
    "summary": "Exhaustive treatment of the two-nucleon bound system: deuteron ground state properties (J^π = 1⁺, B = 2.2245 MeV, I = 0), radial Schrödinger equation in central square well potentials, depth-radius relationship, absence of bound excited states and the ¹S₀ virtual level, non-zero electric quadrupole moment Q = +0.286 fm², non-central tensor force and ³S₁-³D₁ state mixing (η ≈ 0.0256), magnetic dipole moment discrepancy, root-mean-square radius (R_rms ≈ 2.14 fm), and photodisintegration kinematics and cross-sections (γ + d → n + p).",
    "sections": [
        {
            "id": "sec-1-1",
            "title": "General Properties of the Deuteron Ground State (J^π = 1⁺, B = 2.2245 MeV, I = 0)",
            "content": r"""
<h3>1. The Fundamental Two-Nucleon Bound System</h3>
<p>
The <strong>deuteron</strong> (${}^2\text{H}$ or $d$), consisting of one proton and one neutron, is the simplest bound nuclear system. Just as the hydrogen atom serves as the fundamental testing ground for atomic physics and quantum electrodynamics, the deuteron is the foundational benchmark for the microscopic nucleon-nucleon ($N$-$N$) interaction.
</p>
<p>
The key empirically measured static ground-state properties of the deuteron are:
</p>
<ul>
  <li><strong>Binding Energy ($B$):</strong> Measured via high-precision mass spectrometry and the ${}^1\text{H}(n, \gamma){}^2\text{H}$ capture gamma-ray energy ($E_\gamma = 2.224575\text{ MeV}$):
  $$B = [M({}^1\text{H}) + m_n - M({}^2\text{H})] c^2 = 2.224575 \pm 0.000009\text{ MeV}$$
  Compared to typical nuclear binding energies of $\sim 8\text{ MeV/nucleon}$, the deuteron is exceptionally loosely bound ($B/A \approx 1.112\text{ MeV/nucleon}$).</li>
  <li><strong>Total Angular Momentum (Spin $J^\pi$):</strong> Experimentally determined to be $J = 1$ with positive parity ($\pi = +1$), written as $J^\pi = 1^+$.</li>
  <li><strong>Isospin ($I$):</strong> Because the neutron and proton have $I_3 = -1/2$ and $+1/2$, the total two-nucleon isospin can be $I = 0$ (antisymmetric singlet) or $I = 1$ (symmetric triplet). Because neither the diproton (${}^2\text{He}$, $I_3 = +1$) nor the dineutron (${}^2n$, $I_3 = -1$) exists as a bound state, the bound deuteron must be an isospin singlet ($I = 0, I_3 = 0$).</li>
  <li><strong>Magnetic Dipole Moment ($\mu_d$):</strong> Measured via nuclear magnetic resonance (NMR):
  $$\mu_d = +0.85743823 \pm 0.00000002\text{ }\mu_N$$
  This is remarkably close to, but measurably distinct from, the simple algebraic sum of the free proton and neutron magnetic dipole moments:
  $$\mu_p + \mu_n = +2.792847\text{ }\mu_N - 1.913043\text{ }\mu_N = +0.879804\text{ }\mu_N$$
  The small difference $\Delta\mu = \mu_d - (\mu_p + \mu_n) = -0.022366\text{ }\mu_N$ provides direct evidence for orbital angular momentum mixing ($L = 2$).</li>
  <li><strong>Electric Quadrupole Moment ($Q$):</strong>
  $$Q = +0.002859 \pm 0.000030\text{ b} = +0.2859 \pm 0.0030\text{ fm}^2$$
  A pure $S$-wave ($L = 0$) state is spherically symmetric and must have $Q \equiv 0$. The non-zero positive quadrupole moment proves that the deuteron is prolate (elongated along its spin axis), demonstrating that the nuclear force contains a non-central tensor component.</li>
</ul>
"""
        },
        {
            "id": "sec-1-2",
            "title": "Central Square Well Potential Model & Depth-Radius Relation",
            "content": r"""
<h3>1. The Two-Body Schrödinger Equation in Relative Coordinates</h3>
<p>
Let $\vec{r}_p$ and $\vec{r}_n$ denote the coordinates of the proton and neutron with masses $m_p \approx m_n \equiv M$. Introducing the center-of-mass coordinate $\vec{R} = \frac{1}{2}(\vec{r}_p + \vec{r}_n)$ and relative coordinate $\vec{r} = \vec{r}_p - \vec{r}_n$, the two-body Hamiltonian separates. With reduced mass $\mu = \frac{M\cdot M}{M + M} = \frac{M}{2}$, the relative motion satisfies:
</p>
$$\left[ -\frac{\hbar^2}{2\mu} \nabla^2 + V(\vec{r}) \right] \psi(\vec{r}) = E \psi(\vec{r}) = -B \psi(\vec{r})$$
<p>
where $E = -B < 0$ is the bound-state energy. Replacing $\frac{\hbar^2}{2\mu} = \frac{\hbar^2}{M}$:
</p>
$$\left[ -\frac{\hbar^2}{M} \nabla^2 + V(\vec{r}) \right] \psi(\vec{r}) = -B \psi(\vec{r})$$

<h3>2. The Central Spherical Square Well Approximation</h3>
<p>
As a first physical approximation, consider a central, spherically symmetric attractive potential well of depth $V_0$ and range $R$:
</p>
$$V(r) = \begin{cases} -V_0, & r < R \\ 0, & r > R \end{cases}$$
<p>
Assuming a spherically symmetric $S$-state ($L = 0$), the wavefunction is $\psi(\vec{r}) = \frac{u(r)}{r} Y_{00}(\theta, \phi)$, where the radial wavefunction $u(r)$ satisfies:
</p>
$$\frac{d^2 u(r)}{dr^2} + \frac{M}{\hbar^2}\left[ E - V(r) \right] u(r) = 0$$

<h3>3. Interior and Exterior Solutions & Boundary Matching</h3>
<p>
<strong>Region I ($r < R$):</strong> $V(r) = -V_0$. Defining $k_1^2 \equiv \frac{M(V_0 - B)}{\hbar^2} > 0$:
</p>
$$\frac{d^2 u_I}{dr^2} + k_1^2 u_I = 0 \implies u_I(r) = A \sin(k_1 r)$$
<p>
(the cosine solution is excluded by the boundary condition $u(0) = 0$ to keep $\psi(0)$ finite).
</p>
<p>
<strong>Region II ($r > R$):</strong> $V(r) = 0$. Defining $\gamma^2 \equiv \frac{M B}{\hbar^2} > 0$:
</p>
$$\frac{d^2 u_{II}}{dr^2} - \gamma^2 u_{II} = 0 \implies u_{II}(r) = C e^{-\gamma r}$$
<p>
(the growing exponential $e^{+\gamma r}$ is rejected for normalizability).
</p>
<p>
Matching the logarithmic derivatives $\frac{1}{u}\frac{du}{dr}$ at the boundary $r = R$:
</p>
$$\left. \frac{u_I'(r)}{u_I(r)} \right|_{r=R} = \left. \frac{u_{II}'(r)}{u_{II}(r)} \right|_{r=R} \implies k_1 \cot(k_1 R) = -\gamma$$
<p>
Because $B \approx 2.22\text{ MeV} \ll V_0 \approx 35\text{ to }40\text{ MeV}$, the exterior decay parameter $\gamma \approx \sqrt{\frac{M B}{\hbar^2}} \approx 0.232\text{ fm}^{-1}$ is small. In the approximation $\gamma \to 0$ (zero binding energy limit):
</p>
$$\cot(k_1 R) \approx 0 \implies k_1 R \approx \frac{\pi}{2}$$
$$\frac{M(V_0 - B) R^2}{\hbar^2} \approx \frac{\pi^2}{4} \implies V_0 R^2 \approx \frac{\pi^2 \hbar^2}{4 M} \approx 102.8\text{ MeV}\cdot\text{fm}^2$$
<p>
For a realistic nuclear force range $R \approx 2.0\text{ fm}$, this yields a well depth $V_0 \approx 35\text{ to }38\text{ MeV}$, demonstrating that the deuteron is a shallowly bound state sitting near the threshold of the potential well.
</p>
"""
        },
        {
            "id": "sec-1-3",
            "title": "Radial Wavefunction Solution & Absence of Bound Excited States",
            "content": r"""
<h3>1. The Deuteron Radial Wavefunction</h3>
<p>
Normalizing the composite radial wavefunction $\int_0^\infty |u(r)|^2 dr = 1$:
</p>
$$u(r) = \begin{cases} A \sin(k_1 r), & r \le R \\ A \sin(k_1 R) e^{-\gamma (r - R)}, & r > R \end{cases}$$
<p>
The decay parameter $\gamma$ determines the asymptotic behavior outside the potential:
</p>
$$\gamma = \frac{\sqrt{M B}}{\hbar} = \frac{\sqrt{938.9\text{ MeV} \times 2.2246\text{ MeV}}}{197.33\text{ MeV}\cdot\text{fm}} \approx 0.2317\text{ fm}^{-1}$$
<p>
The characteristic decay length (the "tail" of the deuteron) is:
</p>
$$R_{\text{decay}} = \frac{1}{\gamma} \approx \frac{1}{0.2317\text{ fm}^{-1}} \approx 4.316\text{ fm}$$
<p>
Because the nuclear potential radius is only $R \approx 1.7\text{ to }2.1\text{ fm}$, the probability of finding the nucleons outside the range of their mutual nuclear interaction is:
</p>
$$P(r > R) = \int_R^\infty |u_{II}(r)|^2 dr = \frac{1}{1 + \gamma R} \approx \frac{1}{1 + (0.232)(2.0)} \approx 68\%$$
<p>
Thus, the neutron and proton spend approximately <strong>70% of their time outside the nuclear potential well</strong>, illustrating the exceptionally diffuse, halo-like nature of the deuteron.
</p>

<h3>2. The Non-Existence of Bound Excited States</h3>
<p>
Can the deuteron have bound excited states?
</p>
<ol>
  <li><strong>Higher Radial Nodes ($n = 2, S$-wave):</strong> A second bound state with $L = 0$ requires $k_1 R > \frac{3\pi}{2}$. This would demand a potential depth:
  $$V_0 R^2 \ge \frac{9\pi^2 \hbar^2}{4 M} \approx 9 \times 103\text{ MeV}\cdot\text{fm}^2 \approx 927\text{ MeV}\cdot\text{fm}^2$$
  which is an order of magnitude deeper than the physical nuclear well ($V_0 R^2 \approx 105\text{ MeV}\cdot\text{fm}^2$).</li>
  <li><strong>Orbital Excitations ($L \ge 1$, $P$-states):</strong> For $L = 1$, the effective potential includes a centrifugal barrier:
  $$V_{\text{eff}}(r) = V(r) + \frac{\hbar^2 L(L+1)}{M r^2} = V(r) + \frac{2\hbar^2}{M r^2}$$
  At $r = R \approx 2\text{ fm}$, $\frac{2\hbar^2}{M R^2} \approx \frac{2 \times 41.47}{4} \approx 20.7\text{ MeV}$. This repulsive barrier pushes the ground state energy far above zero, preventing any bound $P$-state.</li>
  <li><strong>Singlet Spin State (${}^1S_0, S=0$):</strong> In the spin-singlet state, the $N$-$N$ interaction is slightly weaker ($V_0^{(s)} \approx 32\text{ MeV}$ compared to $V_0^{(t)} \approx 38\text{ MeV}$). This depth is insufficient to bind: the singlet state is an <strong>unbound virtual state</strong> with energy $E_s \approx -0.066\text{ MeV} = -66\text{ keV}$ (a pole on the second Riemann sheet).</li>
</ol>
<p>
Therefore, the deuteron possesses <strong>no bound excited states whatsoever</strong>—neither radial, orbital, nor spin excitations exist.
</p>
""",
            "simulation": "nuc2-deuteron-wavefunction-sim"
        },
        {
            "id": "sec-1-4",
            "title": "Electric Quadrupole Moment & Departure from Spherical Symmetry",
            "content": r"""
<h3>1. The Classical and Quantum Quadrupole Moment</h3>
<p>
The electric quadrupole moment measures the departure of the nuclear charge distribution from spherical symmetry. Classically, for a charge distribution $\rho_c(\vec{r})$:
</p>
$$Q_{\text{classical}} = \frac{1}{e} \int \rho_c(\vec{r}) \left( 3z^2 - r^2 \right) d^3r = \frac{1}{e} \int \rho_c(\vec{r}) r^2 (3\cos^2\theta - 1) d^3r$$
<p>
In quantum mechanics, the quadrupole operator for a system of nucleons with coordinates $\vec{r}_i$ and charges $e_i$ is:
</p>
$$\hat{Q} = \sum_{i=1}^A \frac{e_i}{e} \left( 3z_i^2 - r_i^2 \right)$$
<p>
For the deuteron, choosing the center of mass as the origin, the proton coordinate is $\vec{r}_p = +\frac{1}{2}\vec{r}$ and the neutron coordinate is $\vec{r}_n = -\frac{1}{2}\vec{r}$. Since the neutron has zero electric charge ($e_n = 0$) and the proton has charge $e_p = e$:
</p>
$$\hat{Q} = 3 z_p^2 - r_p^2 = 3\left(\frac{z}{2}\right)^2 - \left(\frac{r}{2}\right)^2 = \frac{1}{4}\left( 3z^2 - r^2 \right) = \frac{1}{4} r^2 \sqrt{\frac{16\pi}{5}} Y_{20}(\theta, \phi)$$
<p>
The observable quadrupole moment $Q$ is defined as the expectation value in the substate of maximum magnetic projection ($M_J = J = 1$):
</p>
$$Q \equiv \langle \psi_{J=1, M_J=1} | \hat{Q} | \psi_{J=1, M_J=1} \rangle$$

<h3>2. Impossibility of Quadrupole Moment in a Pure S-Wave</h3>
<p>
If the deuteron ground state were a pure $S$-wave ($L = 0$), its spatial wavefunction would be spherically symmetric ($\psi \propto Y_{00}$). Then:
</p>
$$\langle Y_{00} | (3\cos^2\theta - 1) | Y_{00} \rangle = \frac{1}{4\pi} \int_0^{2\pi} d\phi \int_{-1}^1 (3\cos^2\theta - 1) d(\cos\theta) = 0$$
<p>
By parity conservation and Wigner-Eckart selection rules, $\langle L=0 | Y_{20} | L=0 \rangle \equiv 0$.
</p>
<p>
However, high-precision radio-frequency molecular beam spectroscopy (Kellogg, Rabi, Ramsey, Zacharias, 1939) established conclusively that the deuteron has a non-zero quadrupole moment:
</p>
$$Q = +0.002859 \pm 0.000030\text{ b} = +0.2859\text{ fm}^2$$
<p>
The positive sign ($Q > 0$) demonstrates that the deuteron charge distribution is a <strong>prolate spheroid</strong> (cigar-shaped, elongated along the spin vector $\vec{J}$) rather than oblate ($Q < 0$) or spherical ($Q = 0$). This non-spherical deformation provides irrefutable proof that the nuclear force is non-central.
</p>
"""
        },
        {
            "id": "sec-1-5",
            "title": "The Non-Central Tensor Force & D-State Wavefunction Admixture",
            "content": r"""
<h3>1. The Phenomenological Tensor Operator</h3>
<p>
To construct a non-central interaction that satisfies parity conservation ($\pi = +1$), time-reversal invariance, rotational invariance, and isospin symmetry, the interaction must couple the nucleon spin operators $\vec{\sigma}_1, \vec{\sigma}_2$ to the relative spatial coordinate unit vector $\hat{r} = \vec{r}/r$. The unique scalar operator formed from the rank-2 spin tensor and rank-2 spatial coordinate tensor is the <strong>tensor operator</strong>:
</p>
$$S_{12} \equiv 3(\vec{\sigma}_1\cdot\hat{r})(\vec{\sigma}_2\cdot\hat{r}) - \vec{\sigma}_1\cdot\vec{\sigma}_2$$
<p>
Key mathematical properties of $S_{12}$:
</p>
<ul>
  <li><strong>Angle Averaging:</strong> $\int S_{12} d\Omega = 0$. Averaged over all space directions, the tensor force vanishes; it produces no contribution to pure spherically symmetric $S$-states.</li>
  <li><strong>Singlet Annihilation:</strong> For a singlet spin state ($S = 0$), $\vec{\sigma}_1 + \vec{\sigma}_2 = 0 \implies \vec{\sigma}_1\cdot\vec{\sigma}_2 = -3$. It is readily proven that $S_{12}|S=0\rangle \equiv 0$. The tensor force acts <em>only</em> in spin-triplet ($S = 1$) states.</li>
  <li><strong>Orbital Coupling:</strong> $S_{12}$ does not commute with orbital angular momentum $\vec{L}^2$ or spin $\vec{S}^2$, but commutes with total angular momentum $\vec{J} = \vec{L} + \vec{S}$. It can mix states with $\Delta L = 0, \pm 2$.</li>
</ul>

<h3>2. The Admixed Wavefunction: ³S₁ and ³D₁</h3>
<p>
With $J^\pi = 1^+$, the allowed quantum states combining $L$ and $S = 1$ with positive parity ($\pi = (-1)^L = +1$) are:
</p>
<ul>
  <li>$L = 0 \implies {}^3S_1$ (Principal component)</li>
  <li>$L = 2 \implies {}^3D_1$ (Admixed component)</li>
</ul>
<p>
(States with $L = 1$, such as ${}^3P_1$ or ${}^1P_1$, are forbidden because they have odd parity $\pi = (-1)^1 = -1$).
</p>
<p>
Therefore, the general ground-state wavefunction of the deuteron is an exact quantum superposition:
</p>
$$\psi_d(\vec{r}) = \frac{u(r)}{r} \mathcal{Y}_{J=1, M}^{L=0, S=1}(\hat{r}) + \frac{w(r)}{r} \mathcal{Y}_{J=1, M}^{L=2, S=1}(\hat{r})$$
<p>
where $u(r)$ is the radial $S$-wave function and $w(r)$ is the radial $D$-wave function, normalized such that:
</p>
$$\int_0^\infty \left[ u^2(r) + w^2(r) \right] dr = P_S + P_D = 1$$
<p>
Empirical analysis of the quadrupole moment and magnetic moment yields a $D$-state probability of:
</p>
$$P_D = \int_0^\infty w^2(r) dr \approx 4\% \text{ to } 6\%, \quad P_S \approx 94\% \text{ to } 96\%$$
<p>
The asymptotic $D/S$ ratio is denoted $\eta \equiv \lim_{r\to\infty} \frac{w(r)}{u(r)} \approx 0.0256 \pm 0.0004$.
</p>
"""
        },
        {
            "id": "sec-1-6",
            "title": "Magnetic Dipole Moment Discrepancy & Root-Mean-Square Radius",
            "content": r"""
<h3>1. Derivation of the Deuteron Magnetic Moment</h3>
<p>
The magnetic moment operator of the two-nucleon system is given by the sum of orbital and spin contributions:
</p>
$$\vec{\mu} = \vec{\mu}_l + \vec{\mu}_s = \frac{e\hbar}{2 M c} \left( g_l^{(p)} \vec{l}_p + g_l^{(n)} \vec{l}_n + g_s^{(p)} \vec{s}_p + g_s^{(n)} \vec{s}_n \right)$$
<p>
Since $\vec{l}_p = \vec{l}_n = \frac{1}{2}\vec{L}$, $g_l^{(p)} = 1$, and $g_l^{(n)} = 0$, the orbital contribution is $\vec{\mu}_l = \frac{1}{2}\vec{L}\mu_N$. The spin contribution is $\vec{\mu}_s = (\mu_p \vec{\sigma}_p + \mu_n \vec{\sigma}_n)\mu_N = (\mu_p + \mu_n)\vec{S}\mu_N + (\mu_p - \mu_n)(\vec{\sigma}_p - \vec{\sigma}_n)\frac{\mu_N}{2}$.
</p>
<p>
Evaluating the expectation value in the admixed state $\psi = a_S \psi(^3S_1) + a_D \psi(^3D_1)$:
</p>
$$\mu_d = \langle \psi_{J=1, M=1} | \mu_z | \psi_{J=1, M=1} \rangle = (\mu_p + \mu_n) P_S + \left[ \frac{1}{2} - \frac{1}{2}(\mu_p + \mu_n) \right] P_D$$
$$\mu_d = (\mu_p + \mu_n) - \frac{3}{2}\left( \mu_p + \mu_n - \frac{1}{2} \right) P_D$$
<p>
Substituting $\mu_p + \mu_n = 0.879804\text{ }\mu_N$:
</p>
$$\mu_d = 0.879804 - \frac{3}{2}(0.879804 - 0.5) P_D = 0.879804 - 0.5697 P_D$$
<p>
Equating this to the measured value $\mu_d = 0.857438\text{ }\mu_N$:
</p>
$$0.5697 P_D = 0.879804 - 0.857438 = 0.022366 \implies P_D \approx \frac{0.022366}{0.5697} \approx 3.93\%$$
<p>
Relativistic corrections and meson exchange currents (MEC) slightly shift this value, establishing $P_D \approx 4\% \text{ to } 6\%$.
</p>

<h3>2. The Root-Mean-Square Radius of the Deuteron</h3>
<p>
The charge radius of the deuteron is measured via high-energy elastic electron-deuteron scattering ($e + d \to e + d$) and precision laser spectroscopy of muonic deuterium:
</p>
$$\langle r_d^2 \rangle_{\text{ch}}^{1/2} = 2.1413 \pm 0.0025\text{ fm}$$
<p>
The matter root-mean-square radius $R_{\text{matter}}$ (separation between proton and neutron centers of mass) is:
</p>
$$R_{\text{rms}} \equiv \sqrt{\langle r^2 \rangle} = \left[ \int_0^\infty r^2 (u^2(r) + w^2(r)) dr \right]^{1/2} \approx 1.97\text{ to }2.00\text{ fm}$$
<p>
This is substantially larger than heavy atomic nuclei ($R_{\text{Pb}} \approx 1.2 \times 208^{1/3} \approx 7.1\text{ fm}$, but nucleon-nucleon average spacing is $\sim 1.8\text{ fm}$), demonstrating once again the extended spatial extent of the deuteron.
</p>
"""
        },
        {
            "id": "sec-1-7",
            "title": "Photodisintegration of the Deuteron (γ + d → n + p Threshold & Cross-Sections)",
            "content": r"""
<h3>1. Kinematics and Threshold Energy</h3>
<p>
<strong>Photodisintegration</strong> is the electromagnetic breakup of the deuteron by an incident photon:
</p>
$$\gamma + {}^2\text{H} \to n + p$$
<p>
Let $E_\gamma$ be the laboratory photon energy. Conservation of energy and linear momentum:
</p>
$$E_\gamma + M_d c^2 = E_n + E_p, \quad \frac{E_\gamma}{c} = p_n \cos\theta_n + p_p \cos\theta_p$$
<p>
Accounting for the small nuclear recoil energy ($E_{\text{recoil}} = \frac{E_\gamma^2}{2 M_d c^2} \approx 1.3\text{ keV}$), the threshold photon energy in the laboratory frame is:
</p>
$$E_{\gamma,\text{th}} = B\left( 1 + \frac{B}{2 M_d c^2} \right) \approx B = 2.224575\text{ MeV}$$
<p>
For $E_\gamma > B$, the excess energy $E_\gamma - B$ is partitioned equally into center-of-mass kinetic energy of the escaping proton and neutron ($E_{\text{rel}} = E_\gamma - B$).
</p>

<h3>2. Electric Dipole (E1) vs Magnetic Dipole (M1) Cross Sections</h3>
<p>
The transition operator can act via electric dipole ($E1$) or magnetic dipole ($M1$) mechanisms:
</p>
<ol>
  <li><strong>Magnetic Dipole Disintegration ($M1$):</strong> Dominates near the threshold ($E_\gamma - B \le 100\text{ keV}$). The incident gamma ray couples to the spin magnetic moments, flipping the triplet deuteron (${}^3S_1$) into the unbound singlet continuum (${}^1S_0$). The $M1$ cross section is isotropic ($\frac{d\sigma_{M1}}{d\Omega} \propto \text{const}$) and exhibits a sharp threshold peak:
  $$\sigma_{M1} \propto \frac{\sqrt{E_\gamma - B}}{E_\gamma}$$</li>
  <li><strong>Electric Dipole Disintegration ($E1$):</strong> Dominates at energies $E_\gamma \ge 3\text{ MeV}$. The electric field of the photon couples to the proton charge displacement relative to the center of mass. This induces an electric dipole transition from the ${}^3S_1$ ground state to the ${}^3P$ continuum states ($L = 1$). The differential cross section has the characteristic $\sin^2\theta$ dipolar angular distribution:
  $$\frac{d\sigma_{E1}}{d\Omega} = \frac{3}{8\pi} \sigma_{E1} \sin^2\theta$$
  The total $E1$ cross section as a function of relative wavevector $k = \sqrt{M(E_\gamma - B)}/\hbar$ is given by Bethe and Peierls:
  $$\sigma_{E1}(E_\gamma) = \frac{8\pi}{3}\left( \frac{e^2}{\hbar c} \right) \frac{\hbar^2}{M} \frac{\gamma k^3}{(\gamma^2 + k^2)^3} = \frac{8\pi \alpha}{3 M} \frac{\sqrt{B}(E_\gamma - B)^{3/2}}{E_\gamma^3}$$
  This cross section vanishes at threshold ($E_\gamma = B$), rises to a pronounced peak at $E_\gamma = 2 B \approx 4.45\text{ MeV}$ with $\sigma_{\max} \approx 2.5\text{ mb}$, and then decays asymptotically as $E_\gamma^{-3/2}$.</li>
</ol>
<p>
The total photodisintegration differential cross section is parameterized as:
</p>
$$\frac{d\sigma}{d\Omega} = a(E_\gamma) + b(E_\gamma) \sin^2\theta$$
<p>
where $a$ is the $M1$ contribution and $b$ is the $E1$ contribution.
</p>
""",
            "simulation": "nuc2-photodisintegration-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-1-1",
            "title": "Finite Square Well Potential Depth & Range of the Deuteron",
            "statement": r"""Assuming the deuteron ground state can be modeled by a central spherical square well of radius $R = 2.10\text{ fm}$ with binding energy $B = 2.2246\text{ MeV}$, compute:
(a) The wave decay constant $\gamma$ in the exterior region $r > R$.
(b) The interior wavenumber $k_1$.
(c) The exact potential well depth $V_0$ in MeV.
(d) The probability $P_{\text{ext}}$ that the neutron and proton are found at a separation exceeding the potential radius $R$.""",
            "solution": r"""**(a) Exterior Wave Decay Constant $\gamma$:**
Using reduced mass $\mu = M/2$ where $M c^2 = \frac{m_p c^2 + m_n c^2}{2} \approx 938.92\text{ MeV}$:
$$\gamma = \frac{\sqrt{M B}}{\hbar} = \frac{\sqrt{(938.92\text{ MeV})(2.2246\text{ MeV})}}{197.327\text{ MeV}\cdot\text{fm}} = \frac{\sqrt{2088.72}}{197.327} = \frac{45.7026}{197.327} \approx 0.23161\text{ fm}^{-1}$$

**(b) Interior Wavenumber $k_1$:**
From boundary matching at $r = R$:
$$k_1 \cot(k_1 R) = -\gamma$$
Let $\xi = k_1 R$. Then $\cot\xi = -\frac{\gamma R}{\xi} = -\frac{(0.23161)(2.10)}{\xi} = -\frac{0.48638}{\xi}$.
Because the well contains only one bound state, $\frac{\pi}{2} < \xi < \pi$.
Solving transcendental equation $\xi \cot\xi = -0.48638$ numerically:
- Try $\xi = 1.90$: $\cot(1.90) = -0.3664 \implies \xi\cot\xi = -0.696$
- Try $\xi = 1.75$: $\cot(1.75) = -0.1983 \implies \xi\cot\xi = -0.347$
- Try $\xi = 1.815$: $\cot(1.815) = -0.2678 \implies \xi\cot\xi = -0.4861$
Thus $\xi = k_1 R \approx 1.815\text{ rad}$.
$$k_1 = \frac{1.815}{2.10\text{ fm}} \approx 0.8643\text{ fm}^{-1}$$

**(c) Potential Well Depth $V_0$:**
From definition $k_1^2 = \frac{M(V_0 - B)}{\hbar^2}$:
$$V_0 - B = \frac{\hbar^2 k_1^2}{M} = \frac{(197.327)^2 (0.8643)^2}{938.92} = \frac{38938 \times 0.7470}{938.92} \approx 30.98\text{ MeV}$$
$$V_0 = 30.98\text{ MeV} + 2.22\text{ MeV} \approx 33.20\text{ MeV}$$
The potential well depth is **$33.2\text{ MeV}$**.

**(d) Probability Outside the Well ($P_{\text{ext}}$):**
Using normalized wavefunction $u_I(r) = A\sin(k_1 r)$ and $u_{II}(r) = A\sin(k_1 R) e^{-\gamma(r-R)}$:
$$I_1 = \int_0^R \sin^2(k_1 r) dr = \frac{R}{2} - \frac{\sin(2 k_1 R)}{4 k_1} = \frac{2.10}{2} - \frac{\sin(3.630)}{4(0.8643)} = 1.05 - \frac{-0.4623}{3.457} = 1.05 + 0.1337 = 1.1837\text{ fm}$$
$$I_2 = \int_R^\infty \sin^2(k_1 R) e^{-2\gamma(r-R)} dr = \sin^2(1.815) \frac{1}{2\gamma} = (0.9705)^2 \frac{1}{2(0.23161)} = \frac{0.9419}{0.46322} = 2.0334\text{ fm}$$
The total normalization constant is $A^{-2} = I_1 + I_2 = 1.1837 + 2.0334 = 3.2171\text{ fm}$.
$$P_{\text{ext}} = \frac{I_2}{I_1 + I_2} = \frac{2.0334}{3.2171} \approx 0.632 \approx 63.2\%$$
There is a **$63.2\%$ probability** that the neutron and proton are found outside the potential well."""
        },
        {
            "id": "nuc2-prob-1-2",
            "title": "D-State Admixture and the Deuteron Electric Quadrupole Moment",
            "statement": r"""In the tensor force model of the deuteron, the quadrupole moment $Q$ is given in terms of the radial wavefunctions $u(r)$ ($S$-wave) and $w(r)$ ($D$-wave) by:
$$Q = \frac{1}{10}\int_0^\infty r^2 \left( \sqrt{2} u(r) w(r) - \frac{1}{2} w^2(r) \right) dr$$
(a) Explain why the cross-term $u(r)w(r)$ dominates over the pure $D$-state term $w^2(r)$.
(b) Assuming an empirical quadrupole moment $Q = +0.286\text{ fm}^2$ and average radial moment $\langle r^2 \rangle_{SD} \equiv \int_0^\infty r^2 u(r) w(r) dr \approx 2.05\text{ fm}^2$, calculate the approximate $D$-state mixing amplitude $a_D$ and the $D$-state probability $P_D = a_D^2$.
(c) Verify whether the resulting $P_D$ is consistent with the magnetic moment discrepancy $\Delta\mu = -0.0224\text{ }\mu_N$.""",
            "solution": r"""**(a) Dominance of the Cross-Term:**
Since the $D$-state probability $P_D \ll 1$ (typically $4\% \sim 0.04$), the amplitude $a_D = \sqrt{P_D} \approx 0.20$, whereas $a_S \approx \sqrt{0.96} \approx 0.98$.
The cross-term $u(r)w(r)$ is first order in $a_D$ ($\mathcal{O}(a_D)$), whereas the $w^2(r)$ term is second order ($\mathcal{O}(a_D^2)$).
Specifically, $\sqrt{2} u w \sim \sqrt{2}(0.98)(0.20) \approx 0.277$, while $\frac{1}{2} w^2 \sim 0.5(0.04) = 0.020$. The cross-term is more than 13 times larger and fully determines the magnitude and sign of $Q$.

**(b) Calculation of $D$-State Mixing Amplitude $a_D$:**
Neglecting the small $w^2$ term in the first approximation:
$$Q \approx \frac{\sqrt{2}}{10} \int_0^\infty r^2 u(r) w(r) dr$$
Let $w(r) = a_D \tilde{w}(r)$ and $u(r) = a_S \tilde{u}(r) \approx \tilde{u}(r)$, such that $\int_0^\infty r^2 \tilde{u}(r)\tilde{w}(r) dr = \langle r^2 \rangle_{SD} \approx 2.05\text{ fm}^2$:
$$Q \approx \frac{\sqrt{2}}{10} a_D \langle r^2 \rangle_{SD}$$
$$0.286\text{ fm}^2 = \frac{1.4142}{10} a_D (2.05\text{ fm}^2) = 0.2899 a_D$$
$$a_D \approx \frac{0.286}{0.2899} \approx 0.197$$
$$P_D = a_D^2 = (0.197)^2 \approx 0.0388 \approx 3.9\%$$

**(c) Verification via Magnetic Moment Discrepancy:**
The theoretical magnetic dipole moment formula derived in Section 1.6 gives:
$$\Delta\mu = \mu_d - (\mu_p + \mu_n) = -\frac{3}{2}\left( \mu_p + \mu_n - \frac{1}{2} \right) P_D$$
Substituting $\mu_p + \mu_n = 2.792847 - 1.913043 = 0.879804\text{ }\mu_N$:
$$\Delta\mu = -1.5(0.879804 - 0.500000) P_D = -1.5(0.379804) P_D = -0.5697 P_D$$
For $P_D = 0.0388$:
$$\Delta\mu_{\text{calc}} = -0.5697 \times 0.0388 \approx -0.0221\text{ }\mu_N$$
The measured discrepancy is $\Delta\mu_{\text{exp}} = -0.02237\text{ }\mu_N$. The values match to within $1\%$, rigorously confirming that a **$D$-state probability of $\approx 4\%$** simultaneously accounts for both the electric quadrupole moment and the magnetic dipole moment."""
        },
        {
            "id": "nuc2-prob-1-3",
            "title": "Cross Section and Angular Distribution of Deuteron Photodisintegration",
            "statement": r"""A beam of monochromatic $\gamma$-rays of energy $E_\gamma = 6.00\text{ MeV}$ is incident on a deuterium target.
(a) Compute the kinetic energy of the ejected proton and neutron in the center-of-mass frame.
(b) Using the Bethe-Peierls electric dipole ($E1$) cross section formula:
$$\sigma_{E1} = \frac{8\pi \alpha}{3 M c^2} \frac{\sqrt{B}(E_\gamma - B)^{3/2}}{(E_\gamma/c^2)^3}$$
calculate the total electric dipole cross section $\sigma_{E1}$ in millibarns ($1\text{ mb} = 10^{-27}\text{ cm}^2 = 0.1\text{ fm}^2$).
(c) Write down the differential cross section $\frac{d\sigma_{E1}}{d\Omega}(\theta)$ at laboratory angles $\theta = 0^\circ, 45^\circ,$ and $90^\circ$ relative to the photon beam.""",
            "solution": r"""**(a) Center-of-Mass Kinetic Energy:**
The deuteron binding energy is $B = 2.2246\text{ MeV}$.
The total center-of-mass kinetic energy available to the two nucleons is:
$$E_{\text{c.m.}} = E_\gamma - B = 6.00\text{ MeV} - 2.2246\text{ MeV} = 3.7754\text{ MeV}$$
Since $m_p \approx m_n$, this kinetic energy is shared equally:
$$T_p = T_n = \frac{1}{2} E_{\text{c.m.}} = \frac{3.7754}{2} \approx 1.888\text{ MeV}$$

**(b) Total $E1$ Cross Section $\sigma_{E1}$:**
Fine structure constant $\alpha = 1/137.036$, average nucleon mass $M c^2 = 938.92\text{ MeV}$:
$$\sigma_{E1} = \frac{8\pi}{3(137.036)(938.92\text{ MeV})} \frac{\sqrt{2.2246\text{ MeV}} (3.7754\text{ MeV})^{3/2}}{(6.00\text{ MeV})^3} \hbar^2 c^2$$
Using $(\hbar c)^2 = (197.327\text{ MeV}\cdot\text{fm})^2 = 38938\text{ MeV}^2\cdot\text{fm}^2$:
Prefactor:
$$\frac{8\pi \times 38938}{3 \times 137.036 \times 938.92} = \frac{978635}{385994} \approx 2.5354\text{ fm}^2/\text{MeV}$$
Energy dependence factor:
$$\sqrt{B} = \sqrt{2.2246} \approx 1.4915\text{ MeV}^{1/2}$$
$$(E_\gamma - B)^{3/2} = (3.7754)^{1.5} \approx 7.336\text{ MeV}^{3/2}$$
$$E_\gamma^3 = 6.00^3 = 216\text{ MeV}^3$$
$$\frac{(1.4915)(7.336)}{216} = \frac{10.9416}{216} \approx 0.050656\text{ MeV}^{-1}$$
Multiplying:
$$\sigma_{E1} = 2.5354 \times 0.050656 \approx 0.1284\text{ fm}^2$$
Converting to millibarns ($1\text{ fm}^2 = 10\text{ mb} \implies 0.1\text{ fm}^2 = 1\text{ mb}$):
$$\sigma_{E1} = 0.1284 \times 10\text{ mb} \approx 1.284\text{ mb} \approx 1.28\text{ mb}$$
The total electric dipole photodisintegration cross section is **$1.28\text{ mb}$**.

**(c) Differential Cross Section $\frac{d\sigma_{E1}}{d\Omega}(\theta)$:**
For pure electric dipole absorption from an unpolarized beam:
$$\frac{d\sigma_{E1}}{d\Omega} = \frac{3}{8\pi} \sigma_{E1} \sin^2\theta = \frac{3 \times 1.284}{8\pi} \sin^2\theta \approx 0.153 \sin^2\theta\text{ mb/sr}$$
Evaluating at specific angles:
- At $\theta = 0^\circ$ (forward direction along beam): $\sin^2(0) = 0 \implies \frac{d\sigma}{d\Omega} = \mathbf{0\text{ mb/sr}}$.
- At $\theta = 45^\circ$: $\sin^2(45^\circ) = 0.5 \implies \frac{d\sigma}{d\Omega} = 0.153 \times 0.5 \approx \mathbf{0.0766\text{ mb/sr}}$.
- At $\theta = 90^\circ$ (transverse direction): $\sin^2(90^\circ) = 1.0 \implies \frac{d\sigma}{d\Omega} = \mathbf{0.153\text{ mb/sr}}$."""
        }
    ]
}

u2_data = {
    "title": "Two-Body Problems: Nucleon-Nucleon Scattering & Low-Energy Dynamics",
    "subtitle": "Phase Shifts, Scattering Lengths, Effective Range Theory & Ortho/Para-Hydrogen",
    "summary": "Mathematical theory of two-body nucleon-nucleon collisions: partial-wave decomposition for low-energy neutron-proton scattering (l = 0 s-wave dominance), spin-dependence of the nuclear force, triplet (S = 1, weight 3/4) vs singlet (S = 0, weight 1/4) states, phase shifts δ₀, triplet and singlet scattering lengths (a_t = +5.42 fm, a_s = -23.7 fm), Bethe-Schwinger effective range expansion k cot δ₀ = -1/a + 1/2 r₀ k², intermediate/high-energy scattering, repulsive hard-core (r_c ≈ 0.45 fm), dramatic backward charge-exchange peak via virtual charged pion exchange (n + p → p + n), and coherent/incoherent scattering of slow neutrons by ortho- and para-hydrogen.",
    "sections": [
        {
            "id": "sec-2-1",
            "title": "Low-Energy Neutron-Proton Scattering & S-Wave Partial Wave Formulation",
            "content": r"""
<h3>1. Kinematics of Elastic Neutron-Proton Scattering</h3>
<p>
Consider a beam of monoenergetic neutrons with laboratory kinetic energy $E_{\text{lab}}$ incident on a stationary hydrogen target ($m_p \approx m_n \equiv M$). In the center-of-mass (CM) frame, the relative wavevector $k$ and center-of-mass energy $E_{\text{cm}}$ are related to $E_{\text{lab}}$ by:
</p>
$$E_{\text{cm}} = \frac{1}{2} E_{\text{lab}}, \quad k = \frac{\sqrt{M E_{\text{cm}}}}{\hbar} = \frac{\sqrt{M E_{\text{lab}}/2}}{\hbar}$$
<p>
For low incident energies ($E_{\text{lab}} < 10\text{ MeV}$), the de Broglie wavelength of the relative motion is large compared to the range of the nuclear potential ($R \approx 1.5\text{ to }2.0\text{ fm}$):
</p>
$$\lambdabar = \frac{1}{k} = \frac{\hbar}{\sqrt{M E_{\text{lab}}/2}} = \frac{197.3\text{ MeV}\cdot\text{fm}}{\sqrt{938.9 \times E_{\text{lab}}/2}}$$
<p>
For example, at $E_{\text{lab}} = 1\text{ MeV}$, $k \approx 0.11\text{ fm}^{-1}$, yielding $k R \approx (0.11)(2.0) \approx 0.22 \ll 1$. According to the semiclassical impact parameter argument ($l_{\max} \approx k R$), particles with orbital angular momentum $l \ge 1$ cannot penetrate the centrifugal barrier. Therefore, <strong>low-energy $n$-$p$ scattering is governed exclusively by $s$-wave ($l = 0$) partial waves</strong>.
</p>

<h3>2. Partial Wave Analysis for S-Wave Scattering</h3>
<p>
In the asymptotic region ($r > R$) where the nuclear potential vanishes, the radial Schrödinger equation for $l = 0$ is:
</p>
$$\frac{d^2 u_0(r)}{dr^2} + k^2 u_0(r) = 0$$
<p>
The general asymptotic solution with boundary condition $u_0(0) = 0$ is phase-shifted relative to the unperturbed free wave $\sin(kr)$:
</p>
$$u_0(r) = C \sin(k r + \delta_0)$$
<p>
where $\delta_0$ is the <strong>$s$-wave phase shift</strong>.
</p>
<ul>
  <li>If the potential is attractive ($V(r) < 0$), the wavefunction is pulled inward toward the origin, and $\delta_0 > 0$.</li>
  <li>If the potential is repulsive ($V(r) > 0$), the wavefunction is pushed outward, and $\delta_0 < 0$.</li>
</ul>
<p>
The total elastic scattering cross section for pure $s$-wave scattering is:
</p>
$$\sigma = \frac{4\pi}{k^2} \sin^2\delta_0$$
"""
        },
        {
            "id": "sec-2-2",
            "title": "Spin Dependence of the Nucleon-Nucleon Interaction & Triplet/Singlet States",
            "content": r"""
<h3>1. Spin Combinations of the Two-Nucleon System</h3>
<p>
Both the proton and neutron are spin-$1/2$ fermions. Coupling their spins $\vec{s}_1$ and $\vec{s}_2$ yields total spin $\vec{S} = \vec{s}_1 + \vec{s}_2$:
</p>
<ul>
  <li><strong>Spin-Triplet State ($S = 1$):</strong> Three symmetric magnetic sub-states ($M_S = +1, 0, -1$):
  $$|1, 1\rangle = |\!\uparrow\uparrow\rangle, \quad |1, 0\rangle = \frac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle + |\!\downarrow\uparrow\rangle), \quad |1, -1\rangle = |\!\downarrow\downarrow\rangle$$
  Statistical weight $g_t = \frac{2S+1}{(2s_1+1)(2s_2+1)} = \frac{3}{4}$.</li>
  <li><strong>Spin-Singlet State ($S = 0$):</strong> One antisymmetric sub-state ($M_S = 0$):
  $$|0, 0\rangle = \frac{1}{\sqrt{2}}(|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle)$$
  Statistical weight $g_s = \frac{1}{4}$.</li>
</ul>

<h3>2. The Spin-Dependent Total Cross Section</h3>
<p>
Because the nuclear force depends strongly on the relative spin orientation, the phase shifts for the triplet state ($\delta_{0t}$) and singlet state ($\delta_{0s}$) are completely different.
</p>
<p>
For an unpolarized incident neutron beam hitting an unpolarized proton target, the total unpolarized elastic scattering cross section is the statistically weighted sum of triplet and singlet cross sections:
</p>
$$\sigma = \frac{3}{4}\sigma_t + \frac{1}{4}\sigma_s = \frac{3}{4}\left( \frac{4\pi}{k^2}\sin^2\delta_{0t} \right) + \frac{1}{4}\left( \frac{4\pi}{k^2}\sin^2\delta_{0s} \right)$$
<p>
If the nuclear force were spin-independent, then $\delta_{0t} = \delta_{0s}$, and the scattering cross section at zero energy would be determined entirely by the deuteron bound-state parameters:
</p>
$$\sigma_{\text{spin-indep}} = \frac{4\pi}{\gamma^2} = \frac{4\pi \hbar^2}{M B} \approx 4.3\text{ barns}$$
<p>
However, experimental measurements of the low-energy thermal neutron-proton scattering cross section (Wigner, 1935) yielded:
</p>
$$\sigma_{\text{exp}} \approx 20.4\text{ barns}$$
<p>
The enormous factor-of-five discrepancy ($20.4\text{ b} \gg 4.3\text{ b}$) provided direct historical proof that <strong>the nuclear force is strongly spin-dependent</strong> ($\sigma_s \gg \sigma_t$).
</p>
"""
        },
        {
            "id": "sec-2-3",
            "title": "Phase Shift δ₀, Scattering Lengths (a_t, a_s) & Zero-Energy Cross Section",
            "content": r"""
<h3>1. Definition of the Scattering Length $a$</h3>
<p>
In the limit of zero incident kinetic energy ($k \to 0$), the phase shift $\delta_0$ approaches zero proportional to $k$. The <strong>scattering length</strong> $a$ is defined as the negative limit of the ratio:
</p>
$$a \equiv -\lim_{k\to 0} \frac{\tan\delta_0}{k} = -\lim_{k\to 0} \frac{\delta_0}{k}$$
<p>
Geometrically, if the asymptotic zero-energy radial wavefunction $u_0(r) \propto 1 - r/a$ is extrapolated linearly toward the origin, $a$ represents the <strong>intercept of the asymptotic wavefunction on the $r$-axis</strong>:
</p>
$$\lim_{k\to 0} u_0(r) \propto (r - a)$$

<h3>2. Physical Interpretation of Positive vs Negative Scattering Lengths</h3>
<ul>
  <li><strong>Positive Scattering Length ($a > 0$):</strong> The potential is sufficiently attractive to produce a real bound state. The interior wavefunction bends over and has a negative slope at the potential boundary, causing the linear extrapolation to intercept the positive $r$-axis ($a > 0$). This is the case for the triplet $n$-$p$ state:
  $$a_t = +5.424 \pm 0.004\text{ fm}$$
  In the zero-range approximation, $a_t \approx \frac{1}{\gamma} = \frac{\hbar}{\sqrt{M B}} \approx 4.32\text{ fm}$.</li>
  <li><strong>Negative Scattering Length ($a < 0$):</strong> The potential is attractive but not deep enough to form a bound state. The interior wavefunction does not reach a negative slope at $r = R$; it curves toward the origin, causing the linear extrapolation to intercept the negative $r$-axis ($a < 0$). This indicates an <strong>unbound virtual state</strong>. For the singlet $n$-$p$ state:
  $$a_s = -23.740 \pm 0.020\text{ fm}$$
  The colossal negative value of $a_s$ indicates that the singlet state is extraordinarily close to binding (the virtual pole lies at $E_s = -\frac{\hbar^2}{M a_s^2} \approx -66\text{ keV}$).</li>
</ul>

<h3>3. Zero-Energy Cross Section Evaluation</h3>
<p>
In the zero-energy limit $k \to 0$:
</p>
$$\sigma_t = 4\pi a_t^2 = 4\pi (5.424\text{ fm})^2 = 4\pi (29.42\text{ fm}^2) \approx 3.698\times 10^{-24}\text{ cm}^2 = 3.70\text{ b}$$
$$\sigma_s = 4\pi a_s^2 = 4\pi (-23.74\text{ fm})^2 = 4\pi (563.59\text{ fm}^2) \approx 7.082\times 10^{-23}\text{ cm}^2 = 70.82\text{ b}$$
<p>
Weighting the triplet and singlet contributions:
</p>
$$\sigma_0 = \frac{3}{4}\sigma_t + \frac{1}{4}\sigma_s = \frac{3}{4}(3.70\text{ b}) + \frac{1}{4}(70.82\text{ b}) = 2.775\text{ b} + 17.705\text{ b} = 20.48\text{ b}$$
<p>
This matches the experimental value of $20.4\text{ b}$ to within $0.5\%$.
</p>
""",
            "simulation": "nuc2-np-scattering-phaseshift-sim"
        },
        {
            "id": "sec-2-4",
            "title": "Effective Range Theory in Low-Energy n-p Scattering (Bethe-Schwinger)",
            "content": r"""
<h3>1. The Bethe-Schwinger Effective Range Expansion</h3>
<p>
As the neutron energy increases away from zero, the cross section begins to vary with $k$. Hans Bethe and Julian Schwinger developed <strong>effective range theory</strong>, which parameterizes low-energy scattering independently of the specific shape of the nuclear potential.
</p>
<p>
By comparing the true radial wavefunction $u(k, r)$ inside the potential to the asymptotic wavefunction $v(k, r) = \frac{\sin(kr + \delta_0)}{\sin\delta_0}$ extrapolated to all $r$, one derives the exact shape-independent expansion:
</p>
$$k \cot\delta_0 = -\frac{1}{a} + \frac{1}{2} r_0 k^2 - P r_0^3 k^4 + \mathcal{O}(k^6)$$
<p>
where:
</p>
<ul>
  <li>$a$ is the scattering length defined at $k = 0$.</li>
  <li>$r_0$ is the <strong>effective range</strong>, defined by the integral:
  $$r_0 \equiv 2 \int_0^\infty \left[ v_0^2(r) - u_0^2(r) \right] dr$$
  where $u_0(r)$ is the true zero-energy wavefunction and $v_0(r) = 1 - r/a$ is its linear asymptotic continuation.</li>
  <li>$P$ is a dimensionless shape parameter (typically $|P| \le 0.05$).</li>
</ul>

<h3>2. Empirical Values for Triplet and Singlet Channels</h3>
<p>
By measuring $n$-$p$ total scattering cross sections over the energy range $0.1\text{ MeV} \le E_{\text{lab}} \le 10\text{ MeV}$, the parameters are experimentally determined:
</p>
$$\text{Triplet Channel: } a_t = +5.424 \pm 0.004\text{ fm}, \quad r_{0t} = 1.759 \pm 0.005\text{ fm}$$
$$\text{Singlet Channel: } a_s = -23.740 \pm 0.020\text{ fm}, \quad r_{0s} = 2.77 \pm 0.05\text{ fm}$$

<h3>3. Relation to Deuteron Binding Energy</h3>
<p>
In the triplet channel, the effective range expansion can be evaluated at the negative bound-state energy $E = -B$, corresponding to $k = i\gamma$:
</p>
$$i\gamma \cot\delta_t(i\gamma) = -\gamma = -\frac{1}{a_t} + \frac{1}{2} r_{0t} (i\gamma)^2 = -\frac{1}{a_t} - \frac{1}{2} r_{0t} \gamma^2$$
$$\gamma = \frac{1}{a_t} + \frac{1}{2} r_{0t} \gamma^2 \implies \frac{1}{a_t} = \gamma\left( 1 - \frac{1}{2}\gamma r_{0t} \right)$$
<p>
Using $\gamma = 0.2316\text{ fm}^{-1}$ and $r_{0t} = 1.759\text{ fm}$:
</p>
$$\frac{1}{a_t} = 0.2316 \left( 1 - \frac{1}{2}(0.2316)(1.759) \right) = 0.2316(1 - 0.2037) = 0.2316(0.7963) \approx 0.1844\text{ fm}^{-1}$$
$$a_t = \frac{1}{0.1844} \approx 5.42\text{ fm}$$
<p>
This remarkable agreement demonstrates that effective range theory unifies bound-state properties ($B$) and low-energy scattering data ($a_t, r_{0t}$) in a single coherent framework.
</p>
"""
        },
        {
            "id": "sec-2-5",
            "title": "Neutron-Proton Scattering at Intermediate and High Energies & Repulsive Hard Core",
            "content": r"""
<h3>1. Onset of Higher Partial Waves ($P$, $D$, and $F$ Waves)</h3>
<p>
As the laboratory neutron energy increases above $10\text{ MeV}$, the condition $k R \ll 1$ breaks down:
</p>
<ul>
  <li>At $E_{\text{lab}} = 20\text{ MeV}$: $k \approx 0.49\text{ fm}^{-1} \implies k R \approx 1.0$. $P$-waves ($l = 1$) become significant.</li>
  <li>At $E_{\text{lab}} = 100\text{ MeV}$: $k \approx 1.10\text{ fm}^{-1} \implies k R \approx 2.2$. $D$-waves ($l = 2$) and $F$-waves ($l = 3$) contribute substantially.</li>
</ul>
<p>
The differential cross section becomes highly anisotropic and non-spherical:
</p>
$$\frac{d\sigma}{d\Omega} = |f(\theta)|^2 = \left| \frac{1}{k}\sum_{l=0}^\infty (2l+1) e^{i\delta_l} \sin\delta_l P_l(\cos\theta) \right|^2$$

<h3>2. The Repulsive Hard Core</h3>
<p>
Phase-shift analysis of high-energy $p$-$p$ and $n$-$p$ scattering data (Robert Jastrow, 1951) revealed that the $s$-wave phase shift $\delta_0(E)$ decreases with energy, crosses zero at $E_{\text{lab}} \approx 250\text{ to }300\text{ MeV}$, and becomes increasingly <strong>negative at higher energies</strong>.
</p>
<p>
A negative phase shift at high energy is the unmistakable signature of a <strong>short-range repulsive core</strong>. At high incident energies, the de Broglie wavelength is small enough for nucleons to probe the innermost region of the potential:
</p>
$$V(r) = +\infty \quad (\text{or } +1\text{ to }2\text{ GeV}) \quad \text{for } r \le r_c \approx 0.4\text{ to }0.5\text{ fm}$$
<p>
Physical consequences of the hard core:
</p>
<ul>
  <li><strong>Nuclear Saturation:</strong> It prevents nuclei from collapsing under the attractive nuclear forces. Without a repulsive core, the binding energy would scale as $A^2$ rather than $A$.</li>
  <li><strong>Incompressibility of Nuclear Matter:</strong> It establishes the nearly constant interior density of atomic nuclei ($\rho_0 \approx 0.16\text{ nucleons/fm}^3$).</li>
  <li><strong>Origin in QCD:</strong> The hard core originates from the Pauli exclusion principle acting on the constituent quarks and vector meson ($\omega$) exchange.</li>
</ul>
"""
        },
        {
            "id": "sec-2-6",
            "title": "High-Energy Backward Charge-Exchange Peak via Virtual Pion Exchange",
            "content": r"""
<h3>1. The Anomalous U-Shaped Differential Cross Section</h3>
<p>
In classical scattering or ordinary attractive central potential scattering, high-energy collisions produce a strong forward scattering peak ($\theta_{\text{cm}} \approx 0^\circ$) due to diffraction, with the differential cross section dropping monotonically toward backward angles ($\theta_{\text{cm}} \to 180^\circ$).
</p>
<p>
However, high-energy neutron-proton scattering experiments at $E_{\text{lab}} = 90\text{ to }400\text{ MeV}$ (conducted at Berkeley, Rochester, and Harwell) revealed a startling, highly symmetric <strong>U-shaped differential cross section</strong>:
</p>
$$\frac{d\sigma}{d\Omega}(\theta_{\text{cm}}) \text{ has prominent peaks at both } \theta_{\text{cm}} \approx 0^\circ \text{ and } \theta_{\text{cm}} \approx 180^\circ$$
<p>
In fact, the backward cross section at $180^\circ$ is comparable in magnitude to the forward cross section at $0^\circ$!
</p>

<h3>2. Physical Mechanism: Virtual Charged Pion Exchange</h3>
<p>
A neutron scattered backward at $180^\circ$ in the center-of-mass frame appears in the laboratory frame as a high-energy proton continuing forward in the beam direction!
</p>
<p>
This phenomenon is known as <strong>charge-exchange scattering</strong>:
</p>
$$n + p \to p + n$$
<p>
In the language of quantum field theory and Feynman diagrams, this reaction proceeds via the exchange of a virtual charged pion ($\pi^+$ or $\pi^-$):
</p>
$$n \to p + \pi^-, \quad \text{followed by} \quad \pi^- + p \to n$$
<p>
The fast incident neutron emits a virtual $\pi^-$ and transforms into a proton, which continues forward with nearly all of the incident momentum. The target proton absorbs the $\pi^-$ and becomes a slow neutron.
</p>
<p>
In potential scattering, this corresponds to a <strong>Majorana space-exchange potential</strong> $V_M(r) P_r$:
</p>
$$V(r) = V_W(r) + V_M(r) P_r$$
<p>
where $P_r \psi(\vec{r}) = \psi(-\vec{r})$. In partial-wave expansion, $P_r P_l(\cos\theta) = (-1)^l P_l(\cos\theta)$, meaning even-$l$ waves experience $V_W + V_M$ while odd-$l$ waves experience $V_W - V_M$. This alternating sign naturally produces the backward peaking at $\cos\theta = -1$.
</p>
"""
        },
        {
            "id": "sec-2-7",
            "title": "Coherent & Incoherent Scattering of Thermal Neutrons by Ortho- and Para-Hydrogen",
            "content": r"""
<h3>1. Molecular Hydrogen States: Ortho vs Para</h3>
<p>
Molecular hydrogen ($H_2$) exists in two nuclear spin isomers depending on the coupling of the two proton spins:
</p>
<ul>
  <li><strong>Ortho-Hydrogen:</strong> Symmetric nuclear spin triplet ($I_{\text{mol}} = 1$). By the Pauli exclusion principle for identical proton fermions, the rotational wavefunction must be antisymmetric: odd rotational quantum numbers $J_{\text{rot}} = 1, 3, 5, \dots$</li>
  <li><strong>Para-Hydrogen:</strong> Antisymmetric nuclear spin singlet ($I_{\text{mol}} = 0$). Symmetrical rotational wavefunction: even rotational quantum numbers $J_{\text{rot}} = 0, 2, 4, \dots$ At low temperatures ($T < 20\text{ K}$), liquid hydrogen converts almost entirely to the para-ground state ($J_{\text{rot}} = 0$).</li>
</ul>

<h3>2. Coherent and Incoherent Scattering Amplitudes</h3>
<p>
When very slow, sub-thermal neutrons ($\lambda \gg \text{molecular bond length } d \approx 0.74\text{ \AA}$) scatter from an $H_2$ molecule, the scattered neutron waves from the two proton centers interfere coherently.
</p>
<p>
Let $a_t$ and $a_s$ be the triplet and singlet $n$-$p$ scattering lengths. The neutron-proton scattering amplitude operator is:
</p>
$$\hat{f} = -\left( \frac{3a_t + a_s}{4} + \frac{a_t - a_s}{4} \vec{\sigma}_n\cdot\vec{\sigma}_p \right) \equiv -(a_{\text{coh}} + 2 a_{\text{inc}} \vec{\sigma}_n\cdot\vec{s}_p)$$
<p>
The <strong>coherent scattering length</strong> and <strong>incoherent scattering amplitude</strong> are:
</p>
$$a_{\text{coh}} = \frac{3}{4}a_t + \frac{1}{4}a_s = \frac{3(5.42) + (-23.74)}{4} = \frac{16.26 - 23.74}{4} = \frac{-7.48}{4} = -1.87\text{ fm}$$
$$a_{\text{inc}} = \frac{a_t - a_s}{4} = \frac{5.42 - (-23.74)}{4} = \frac{29.16}{4} = +7.29\text{ fm}$$

<h3>3. Extreme Cross-Section Contrast</h3>
<p>
For para-hydrogen ($I_{\text{mol}} = 0$), the total nuclear spin of the molecule is zero. The spin-dependent terms cancel identically, leaving only the coherent amplitude:
</p>
$$\sigma_{\text{para}} = 4\pi |2 a_{\text{coh}}|^2 \left( \frac{M_{\text{red}}}{M} \right)^2 \propto (3a_t + a_s)^2$$
<p>
For ortho-hydrogen ($I_{\text{mol}} = 1$), both coherent and incoherent amplitudes contribute:
</p>
$$\sigma_{\text{ortho}} \propto (3a_t + a_s)^2 + 2(a_t - a_s)^2$$
<p>
Evaluating the ratio: because $3 a_t \approx 16.3\text{ fm}$ is nearly equal in magnitude and opposite in sign to $a_s \approx -23.7\text{ fm}$, the coherent amplitude $3a_t + a_s$ undergoes strong destructive interference:
</p>
$$\sigma_{\text{para}} \approx 3.2\text{ to }4.0\text{ barns}$$
$$\sigma_{\text{ortho}} \approx 125\text{ to }140\text{ barns}$$
<p>
The experimental cross-section ratio is colossal:
</p>
$$\frac{\sigma_{\text{ortho}}}{\sigma_{\text{para}}} \approx 35 \text{ to } 40$$
<p>
This dramatic ratio provided historic verification of the sign and magnitude of the singlet scattering length ($a_s < 0$), establishing that the virtual singlet state is unbound.
</p>
""",
            "simulation": "nuc2-ortho-para-hydrogen-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-2-1",
            "title": "Low-Energy n-p Total Scattering Cross Section from Scattering Lengths",
            "statement": r"""Given the experimental neutron-proton scattering lengths:
$$a_t = +5.424\text{ fm}, \quad a_s = -23.740\text{ fm}$$
(a) Calculate the pure triplet cross section $\sigma_t$ and pure singlet cross section $\sigma_s$ at zero energy in barns.
(b) Calculate the unpolarized total cross section $\sigma_0$.
(c) By what factor does the singlet cross section exceed the triplet cross section?""",
            "solution": r"""**(a) Pure Triplet and Singlet Cross Sections:**
Using $\sigma = 4\pi a^2$ with $1\text{ fm}^2 = 0.01\text{ b} = 10\text{ mb}$:
$$\sigma_t = 4\pi a_t^2 = 4\pi (5.424\text{ fm})^2 = 4\pi (29.4198\text{ fm}^2) \approx 369.70\text{ fm}^2 = \mathbf{3.697\text{ b}}$$
$$\sigma_s = 4\pi a_s^2 = 4\pi (-23.740\text{ fm})^2 = 4\pi (563.588\text{ fm}^2) \approx 7082.3\text{ fm}^2 = \mathbf{70.823\text{ b}}$$

**(b) Unpolarized Total Cross Section $\sigma_0$:**
Weighing by statistical spin factors (triplet weight $3/4$, singlet weight $1/4$):
$$\sigma_0 = \frac{3}{4}\sigma_t + \frac{1}{4}\sigma_s = \frac{3}{4}(3.697\text{ b}) + \frac{1}{4}(70.823\text{ b})$$
$$\sigma_0 = 2.7728\text{ b} + 17.7058\text{ b} = \mathbf{20.479\text{ b}} \approx \mathbf{20.48\text{ b}}$$

**(c) Ratio of Singlet to Triplet Cross Sections:**
$$\frac{\sigma_s}{\sigma_t} = \left(\frac{a_s}{a_t}\right)^2 = \left(\frac{-23.740}{5.424}\right)^2 = (-4.3768)^2 \approx \mathbf{19.16}$$
The singlet scattering cross section is **19.16 times larger** than the triplet scattering cross section, which directly reflects the resonant enhancement caused by the near-zero unbound virtual state ($E_s \approx -66\text{ keV}$)."""
        },
        {
            "id": "nuc2-prob-2-2",
            "title": "Effective Range Theory Calculation of n-p Scattering at 5 MeV",
            "statement": r"""Using effective range theory parameters:
$$\text{Triplet: } a_t = 5.424\text{ fm}, \quad r_{0t} = 1.759\text{ fm}$$
$$\text{Singlet: } a_s = -23.740\text{ fm}, \quad r_{0s} = 2.770\text{ fm}$$
For neutrons of laboratory energy $E_{\text{lab}} = 5.00\text{ MeV}$ scattering elastically from stationary protons:
(a) Determine the center-of-mass relative wavevector $k$ in $\text{fm}^{-1}$.
(b) Calculate the triplet phase shift $\delta_{0t}$ and singlet phase shift $\delta_{0s}$ in degrees.
(c) Compute the total cross section $\sigma(5\text{ MeV})$ in barns and compare it with the zero-energy limit $\sigma_0 \approx 20.48\text{ b}$.""",
            "solution": r"""**(a) Center-of-Mass Relative Wavevector $k$:**
$$E_{\text{cm}} = \frac{1}{2} E_{\text{lab}} = 2.50\text{ MeV}$$
$$k = \frac{\sqrt{M E_{\text{cm}}}}{\hbar} = \frac{\sqrt{(938.92\text{ MeV})(2.50\text{ MeV})}}{197.327\text{ MeV}\cdot\text{fm}} = \frac{\sqrt{2347.3}}{197.327} = \frac{48.449}{197.327} \approx 0.24553\text{ fm}^{-1}$$
$$k^2 = (0.24553)^2 \approx 0.060285\text{ fm}^{-2}$$

**(b) Triplet and Singlet Phase Shifts:**
Using the Bethe-Schwinger effective range expansion:
$$k \cot\delta_0 = -\frac{1}{a} + \frac{1}{2} r_0 k^2$$

*For Triplet:*
$$k \cot\delta_{0t} = -\frac{1}{5.424} + \frac{1}{2}(1.759)(0.060285) = -0.184366 + 0.053021 = -0.131345\text{ fm}^{-1}$$
$$\cot\delta_{0t} = \frac{-0.131345}{k} = \frac{-0.131345}{0.24553} \approx -0.53495$$
$$\delta_{0t} = \text{arccot}(-0.53495) = 180^\circ - \arctan(1/0.53495) = 180^\circ - 61.85^\circ = \mathbf{118.15^\circ}$$

*For Singlet:*
$$k \cot\delta_{0s} = -\frac{1}{-23.740} + \frac{1}{2}(2.770)(0.060285) = +0.042123 + 0.083495 = +0.125618\text{ fm}^{-1}$$
$$\cot\delta_{0s} = \frac{0.125618}{0.24553} \approx +0.51162$$
$$\delta_{0s} = \arctan(1/0.51162) = \arctan(1.9546) = \mathbf{62.91^\circ}$$

**(c) Total Scattering Cross Section $\sigma(5\text{ MeV})$:**
$$\sigma_t = \frac{4\pi}{k^2} \sin^2\delta_{0t} = \frac{4\pi}{0.060285} \sin^2(118.15^\circ) = 208.39 \times (0.8817)^2 = 208.39 \times 0.7774 = 161.99\text{ fm}^2 = 1.620\text{ b}$$
$$\sigma_s = \frac{4\pi}{k^2} \sin^2\delta_{0s} = \frac{4\pi}{0.060285} \sin^2(62.91^\circ) = 208.39 \times (0.8903)^2 = 208.39 \times 0.7926 = 165.17\text{ fm}^2 = 1.652\text{ b}$$
Unpolarized total cross section:
$$\sigma(5\text{ MeV}) = \frac{3}{4}\sigma_t + \frac{1}{4}\sigma_s = \frac{3}{4}(1.620\text{ b}) + \frac{1}{4}(1.652\text{ b}) = 1.215\text{ b} + 0.413\text{ b} = \mathbf{1.628\text{ b}} \approx \mathbf{1.63\text{ b}}$$
At $5\text{ MeV}$, the cross section has dropped dramatically from its zero-energy value of $20.48\text{ b}$ down to **$1.63\text{ b}$** (a 12-fold reduction), in exact agreement with experimental measurements."""
        },
        {
            "id": "nuc2-prob-2-3",
            "title": "Ortho- vs Para-Hydrogen Thermal Neutron Cross Section Ratio",
            "statement": r"""In terms of the coherent scattering length $a_{\text{coh}} = \frac{3}{4}a_t + \frac{1}{4}a_s$ and incoherent scattering amplitude $a_{\text{inc}} = \frac{1}{4}(a_t - a_s)$, the low-temperature thermal neutron cross sections for para- and ortho-hydrogen molecules (reduced mass factor included) satisfy:
$$\sigma_{\text{para}} = \frac{16\pi}{9} (2 a_{\text{coh}})^2, \quad \sigma_{\text{ortho}} = \frac{16\pi}{9} \left[ (2 a_{\text{coh}})^2 + 8 a_{\text{inc}}^2 \right]$$
(a) Evaluate $a_{\text{coh}}$ and $a_{\text{inc}}$ using $a_t = +5.42\text{ fm}$ and $a_s = -23.74\text{ fm}$.
(b) Compute the numerical values of $\sigma_{\text{para}}$ and $\sigma_{\text{ortho}}$ in barns.
(c) Calculate the ratio $\sigma_{\text{ortho}} / \sigma_{\text{para}}$ and explain how this test proves that the singlet state of the deuteron is unbound.""",
            "solution": r"""**(a) Coherent and Incoherent Amplitudes:**
$$a_{\text{coh}} = \frac{3(5.42\text{ fm}) + (-23.74\text{ fm})}{4} = \frac{16.26 - 23.74}{4} = \frac{-7.48}{4} = \mathbf{-1.870\text{ fm}}$$
$$a_{\text{inc}} = \frac{5.42\text{ fm} - (-23.74\text{ fm})}{4} = \frac{29.16}{4} = \mathbf{+7.290\text{ fm}}$$

**(b) Cross Sections in Barns:**
Prefactor $\frac{16\pi}{9} \approx 5.585$:
*For Para-Hydrogen:*
$$(2 a_{\text{coh}})^2 = (2 \times -1.870)^2 = (-3.740)^2 = 13.9876\text{ fm}^2$$
$$\sigma_{\text{para}} = 5.585 \times 13.9876\text{ fm}^2 \approx 78.12\text{ fm}^2 = \mathbf{0.781\text{ b}}$$
(When inter-molecular thermal motion and molecular structure factor are included at $T \approx 20\text{ K}$, $\sigma_{\text{para}} \approx 3.2\text{ to }4.0\text{ b}$).

*For Ortho-Hydrogen:*
$$8 a_{\text{inc}}^2 = 8 \times (7.290)^2 = 8 \times 53.1441 = 425.15\text{ fm}^2$$
$$(2 a_{\text{coh}})^2 + 8 a_{\text{inc}}^2 = 13.9876 + 425.1528 = 439.14\text{ fm}^2$$
$$\sigma_{\text{ortho}} = 5.585 \times 439.14\text{ fm}^2 \approx 2452.6\text{ fm}^2 = \mathbf{24.53\text{ b}}$$
(With finite neutron velocity corrections and molecular rotor excitations, $\sigma_{\text{ortho}} \approx 130\text{ b}$).

**(c) Ratio and Physical Significance:**
$$\frac{\sigma_{\text{ortho}}}{\sigma_{\text{para}}} = \frac{(2 a_{\text{coh}})^2 + 8 a_{\text{inc}}^2}{(2 a_{\text{coh}})^2} = 1 + \frac{8 a_{\text{inc}}^2}{4 a_{\text{coh}}^2} = 1 + 2\left(\frac{a_{\text{inc}}}{a_{\text{coh}}}\right)^2$$
$$\frac{a_{\text{inc}}}{a_{\text{coh}}} = \frac{7.290}{-1.870} \approx -3.898 \implies \left(\frac{a_{\text{inc}}}{a_{\text{coh}}}\right)^2 \approx 15.20$$
$$\frac{\sigma_{\text{ortho}}}{\sigma_{\text{para}}} = 1 + 2(15.20) \approx \mathbf{31.4}$$
**Physical Significance:**
If the singlet state were bound, $a_s$ would be positive ($a_s \approx +23.7\text{ fm}$). Then $a_{\text{coh}} = \frac{3(5.42) + 23.74}{4} = \frac{39.96}{4} \approx +10.0\text{ fm}$, while $a_{\text{inc}} = \frac{5.42 - 23.74}{4} \approx -4.58\text{ fm}$.
In that hypothetical case, $(2 a_{\text{coh}})^2 = 400\text{ fm}^2$ and $8 a_{\text{inc}}^2 = 168\text{ fm}^2$, yielding a ratio $\sigma_{\text{ortho}}/\sigma_{\text{para}} \approx 1.4$.
The observation of an immense ratio $\sim 30\text{ to }40$ requires destructive cancellation in $3 a_t + a_s$, which is only possible if **$a_s$ is negative**, rigorously proving that the singlet deuteron state is **unbound**."""
        }
    ]
}

with open("nuc2_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1_data, f, indent=2, ensure_ascii=False)

with open("nuc2_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2_data, f, indent=2, ensure_ascii=False)

print("nuc2_u1.json and nuc2_u2.json successfully written!")
