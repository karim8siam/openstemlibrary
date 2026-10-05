import json

u3_data = {
    "title": "Nuclear Forces, Meson Exchange Theory & Nucleon-Nucleon Symmetries",
    "subtitle": "Yukawa Potential, One-Boson-Exchange, Symmetries, Isospin & Quarks to Pions",
    "summary": "Comprehensive foundations of the microscopic nucleon-nucleon interaction: phenomenological characteristics (short range, saturation, charge independence, spin/isospin dependence, non-central tensor and spin-orbit forces), fundamental spacetime and internal symmetries (parity, time reversal, generalized Pauli principle (-1)^{L+S+T} = -1), isospin formalism SU(2)_I, from QCD quarks and color confinement to pions and residual nuclear forces, virtual particle exchange and derivation of the Yukawa potential V(r) = -g² e^{-μr}/r, Majorana/Bartlett/Heisenberg/Wigner exchange operators, and the One-Boson-Exchange (OBE) model with π (140 MeV), σ (500 MeV), ρ and ω (782 MeV) vector mesons.",
    "sections": [
        {
            "id": "sec-3-1",
            "title": "Fundamental Properties & Characteristics of the Nuclear Force",
            "content": r"""
<h3>1. Phenomenological Characteristics of the Strong Nuclear Interaction</h3>
<p>
The force binding protons and neutrons together within atomic nuclei is the strongest fundamental interaction in nature, yet it displays intricate characteristics that distinguish it sharply from the inverse-square gravitational and Coulomb forces:
</p>
<ol>
  <li><strong>Short Range ($R \approx 1\text{ to }2\text{ fm}$):</strong> The nuclear force is negligible at inter-nucleon separations $r > 3\text{ fm}$. Its effective range is governed by the mass of the lightest mediating exchange boson (the pion, $\lambdabar_\pi = \hbar/m_\pi c \approx 1.4\text{ fm}$).</li>
  <li><strong>Extremely High Strength:</strong> Within its attractive well ($r \sim 1\text{ fm}$), the nuclear interaction is approximately $100$ times stronger than the electrostatic Coulomb repulsion between two protons and $10^{38}$ times stronger than Newtonian gravity.</li>
  <li><strong>Nuclear Saturation:</strong> The binding energy per nucleon ($B/A$) is approximately constant across all stable nuclei with $A > 16$, hovering near $B/A \approx 8.0 \pm 0.5\text{ MeV/nucleon}$, and the nuclear interior density is constant ($\rho_0 \approx 0.16\text{ nucleons/fm}^3$). If every nucleon interacted with all other $A-1$ nucleons, $B$ would scale as $A(A-1) \approx A^2$. The linear scaling $B \propto A$ demonstrates that a nucleon interacts only with its immediate nearest neighbors—a property termed <strong>saturation</strong>.</li>
  <li><strong>Charge Independence:</strong> Once electromagnetic Coulomb interactions are subtracted, the nuclear force between two protons ($p$-$p$), two neutrons ($n$-$n$), and a proton-neutron pair ($n$-$p$) in the same orbital, spin, and spatial quantum state is identical to within $1\%$:
  $$V_{pp}^{\text{nucl}} \approx V_{nn}^{\text{nucl}} \approx V_{np}^{\text{nucl}} \quad (\text{for identical } L, S, T)$$</li>
  <li><strong>Charge Symmetry:</strong> The interaction between two protons is identical to the interaction between two neutrons ($V_{pp}^{\text{nucl}} = V_{nn}^{\text{nucl}}$). Charge symmetry is a specific subgroup of the broader charge independence.</li>
  <li><strong>Spin and Isospin Dependence:</strong> As demonstrated in the deuteron ($B = 2.22\text{ MeV}$ for $S = 1$, unbound for $S = 0$), the interaction is strongly dependent on the relative spin and isospin alignments.</li>
  <li><strong>Non-Central Tensor Force ($S_{12}$):</strong> The force depends on the spatial orientation of the nucleon spins relative to the inter-nucleon separation vector $\vec{r}$, producing $D$-state mixing and non-zero electric quadrupole moments.</li>
  <li><strong>Velocity-Dependent Spin-Orbit Force ($\vec{L}\cdot\vec{S}$):</strong> At short distances, relativistic meson exchange generates a powerful spin-orbit interaction $\vec{L}\cdot\vec{S}$, which is responsible for the single-particle shell model magic numbers.</li>
  <li><strong>Repulsive Hard Core ($r \le 0.4\text{ to }0.5\text{ fm}$):</strong> At extremely short distances, the potential transitions from strong attraction to an impenetrable repulsive barrier, preventing nuclear collapse.</li>
</ol>
"""
        },
        {
            "id": "sec-3-2",
            "title": "Symmetries in Nuclear Physics: Parity, Time-Reversal & Generalized Pauli Principle",
            "content": r"""
<h3>1. Invariance Principles and Conservation Laws</h3>
<p>
The nuclear Hamiltonian $\hat{H}$ is governed by fundamental spacetime and internal symmetries:
</p>
<ul>
  <li><strong>Translational and Rotational Invariance:</strong> Guarantees conservation of total linear momentum $\vec{P}$ and total angular momentum $\vec{J} = \vec{L} + \vec{S}$. The potential can depend only on the relative separation $r = |\vec{r}_1 - \vec{r}_2|$, relative momentum $\vec{p}$, and relative spins $\vec{s}_1, \vec{s}_2$.</li>
  <li><strong>Space Inversion Invariance (Parity $\hat{P}$):</strong> Strong nuclear interactions strictly conserve parity: $[\hat{H}, \hat{P}] = 0$. Under parity, $\vec{r} \to -\vec{r}$ and $\vec{p} \to -\vec{p}$, while spin vectors are pseudovectors ($\vec{s} \to +\vec{s}$). Consequently, any potential term linear in $\vec{\sigma}\cdot\vec{r}$ or $\vec{\sigma}\cdot\vec{p}$ is parity-violating and strictly excluded from the strong nuclear force. Allowed terms must be scalars under coordinate inversion: $r^2$, $\vec{\sigma}_1\cdot\vec{\sigma}_2$, $\vec{L}\cdot\vec{S}$, and $S_{12}$.</li>
  <li><strong>Time-Reversal Invariance ($\hat{T}$):</strong> Under time reversal, $t \to -t$, $\vec{r} \to +\vec{r}$, $\vec{p} \to -\vec{p}$, $\vec{s} \to -\vec{s}$, and $\vec{L} \to -\vec{L}$. Terms like $(\vec{\sigma}_1\times\vec{\sigma}_2)\cdot\vec{r}$ change sign under $\hat{T}$ and are forbidden in time-reversal invariant nuclear potentials.</li>
</ul>

<h3>2. The Generalized Pauli Principle</h3>
<p>
According to Werner Heisenberg's isospin concept, the proton and neutron are not two distinct particles, but two different charge states of a single entity: the <strong>nucleon</strong> with isospin $I = 1/2$.
</p>
<p>
Because nucleons are fermions with intrinsic spin $1/2$ and isospin $1/2$, the <strong>generalized Pauli exclusion principle</strong> mandates that the total wavefunction of any two-nucleon system must be <strong>antisymmetric</strong> under the simultaneous exchange of all spatial, spin, and isospin coordinates:
</p>
$$\hat{P}_{\text{total}} \Psi(1, 2) = \hat{P}_{\text{space}} \hat{P}_{\text{spin}} \hat{P}_{\text{isospin}} \Psi(1, 2) = -\Psi(1, 2)$$
<p>
Evaluating the eigenvalues of the permutation operators:
</p>
<ul>
  <li><strong>Spatial Exchange ($\hat{P}_{\text{space}}$):</strong> $\hat{P}_r Y_{LM}(\hat{r}) = (-1)^L Y_{LM}(\hat{r})$. Symmetric for even $L$ ($+1$), antisymmetric for odd $L$ ($-1$).</li>
  <li><strong>Spin Exchange ($\hat{P}_{\text{spin}}$):</strong> Triplet ($S=1$) is symmetric ($+1$); singlet ($S=0$) is antisymmetric ($-1$). Eigenvalue: $(-1)^{S+1}$.</li>
  <li><strong>Isospin Exchange ($\hat{P}_{\text{isospin}}$):</strong> Triplet ($I=1$) is symmetric ($+1$); singlet ($I=0$) is antisymmetric ($-1$). Eigenvalue: $(-1)^{I+1}$.</li>
</ul>
<p>
Combining these permutation eigenvalues yields the fundamental selection rule:
</p>
$$(-1)^L \times (-1)^{S+1} \times (-1)^{I+1} = -1 \implies (-1)^{L + S + I} = -1$$
<p>
Thus, for any physically allowed two-nucleon state:
</p>
$$L + S + I = \text{odd integer}$$
<p>
Classification of allowed two-nucleon states:
</p>
<ul>
  <li>If $I = 0$ (like the deuteron): $L + S$ must be <em>odd</em>. If $S = 1$ (triplet), $L$ must be <em>even</em> ($L = 0, 2 \implies {}^3S_1, {}^3D_1$ allowed!). If $S = 0$ (singlet), $L$ must be <em>odd</em> ($L = 1 \implies {}^1P_1$ allowed).</li>
  <li>If $I = 1$ (two protons $pp$, two neutrons $nn$, or $np$ triplet): $L + S$ must be <em>even</em>. If $S = 0$ (singlet), $L$ must be <em>even</em> ($L = 0 \implies {}^1S_0$ allowed!). If $S = 1$ (triplet), $L$ must be <em>odd</em> ($L = 1 \implies {}^3P_{0, 1, 2}$ allowed).</li>
</ul>
"""
        },
        {
            "id": "sec-3-3",
            "title": "Isospin Formalism (SU(2)_I), Charge Independence & Charge Symmetry",
            "content": r"""
<h3>1. The Isospin Operators and Algebra</h3>
<p>
In analogy to ordinary spin-$1/2$ angular momentum, isospin space is a 2D complex vector space spanned by the proton and neutron state vectors:
</p>
$$|p\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad (I_3 = +1/2), \qquad |n\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \quad (I_3 = -1/2)$$
<p>
The isospin vector operator $\vec{I} = \frac{1}{2}\vec{\tau}$ satisfies the standard $SU(2)$ Lie algebra:
</p>
$$[I_i, I_j] = i \epsilon_{ijk} I_k, \quad [\tau_i, \tau_j] = 2i \epsilon_{ijk} \tau_k$$
<p>
where $\tau_x, \tau_y, \tau_z$ are the Pauli matrices in isospin space:
</p>
$$\tau_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \tau_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \tau_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
<p>
The electric charge operator of a nucleon is related to isospin projection by:
</p>
$$\hat{Q} = e\left( I_3 + \frac{1}{2} \right) = e\left( \frac{\tau_z + 1}{2} \right)$$
<p>
For a nucleus of $Z$ protons and $N$ neutrons, the total isospin projection is:
</p>
$$I_3 = \sum_{i=1}^A I_{3,i} = \frac{Z - N}{2}$$

<h3>2. Two-Nucleon Isospin Multiplets</h3>
<p>
Coupling the isospins of two nucleons ($\vec{I} = \vec{I}_1 + \vec{I}_2$):
</p>
<ul>
  <li><strong>Isospin Triplet ($I = 1$):</strong> Symmetrical isospin states:
  $$|1, +1\rangle = |pp\rangle \quad (Q = +2e)$$
  $$|1, 0\rangle = \frac{1}{\sqrt{2}}(|pn\rangle + |np\rangle) \quad (Q = +1e)$$
  $$|1, -1\rangle = |nn\rangle \quad (Q = 0)$$</li>
  <li><strong>Isospin Singlet ($I = 0$):</strong> Antisymmetrical isospin state:
  $$|0, 0\rangle = \frac{1}{\sqrt{2}}(|pn\rangle - |np\rangle) \quad (Q = +1e, \text{ the deuteron})$$</li>
</ul>
<p>
The scalar product $\vec{\tau}_1\cdot\vec{\tau}_2$ has distinct eigenvalues:
</p>
$$\vec{I}^2 = (\vec{I}_1 + \vec{I}_2)^2 = \vec{I}_1^2 + \vec{I}_2^2 + 2\vec{I}_1\cdot\vec{I}_2 = \frac{3}{4} + \frac{3}{4} + \frac{1}{2}\vec{\tau}_1\cdot\vec{\tau}_2 = \frac{3}{2} + \frac{1}{2}\vec{\tau}_1\cdot\vec{\tau}_2$$
$$\vec{\tau}_1\cdot\vec{\tau}_2 = 2 I(I+1) - 3 = \begin{cases} +1, & I = 1 \text{ (triplet)} \\ -3, & I = 0 \text{ (singlet)} \end{cases}$$
<p>
Under exact charge independence, the strong nuclear Hamiltonian commutes with total isospin: $[\hat{H}_{\text{strong}}, \vec{I}] = 0$. Consequently, the three members of the $I = 1$ multiplet (${}^2\text{He}$, ${}^2\text{H}^*$, ${}^2n$) have identical strong interaction energy levels. The tiny observed mass splittings ($\sim \text{few MeV}$) are caused entirely by electromagnetic Coulomb interactions and the small quark mass difference ($m_d - m_u \approx 3\text{ MeV}$).
</p>
"""
        },
        {
            "id": "sec-3-4",
            "title": "From Quarks & Color Confinement to Pions & Residual Nuclear Forces",
            "content": r"""
<h3>1. The Fundamental Theory: Quantum Chromodynamics (QCD)</h3>
<p>
At the deepest fundamental level, nucleons are not point particles, but composite hadrons containing valence quarks bound by massless gauge bosons called <strong>gluons</strong>:
</p>
$$|p\rangle = |uud\rangle, \qquad |n\rangle = |udd\rangle$$
<p>
The fundamental strong interaction is governed by <strong>Quantum Chromodynamics (QCD)</strong>, an $SU(3)_C$ non-Abelian Yang-Mills gauge theory based on color charge (red, green, blue). Gluons themselves carry color charge and undergo self-interactions, leading to two defining features:
</p>
<ol>
  <li><strong>Asymptotic Freedom:</strong> At ultra-high energy scales ($Q^2 \to \infty$) or extremely short distances ($r \ll 0.1\text{ fm}$), the effective strong coupling constant $\alpha_s(Q^2) \to 0$, and quarks behave as quasi-free particles (Gross, Politzer, Wilczek, Nobel Prize 2004).</li>
  <li><strong>Color Confinement:</strong> At low energies / nuclear distance scales ($r \sim 1\text{ fm}$), $\alpha_s \sim \mathcal{O}(1)$. The color flux lines between quarks form a narrow flux tube (string) with constant string tension $\kappa \approx 1\text{ GeV/fm}$. Free color charges cannot be isolated: all observable asymptotic physical particles must be color-singlet states ($\varepsilon_{ijk}q_i q_j q_k$ for baryons, $\delta_{ij} q_i \bar{q}_j$ for mesons).</li>
</ol>

<h3>2. The Nuclear Force as a Residual Interaction</h3>
<p>
Because nucleons are color singlets (color neutral), there is no net long-range color field outside the nucleon boundary, exactly as neutral atoms have no net electric charge.
</p>
<p>
The nuclear force binding protons and neutrons is the <strong>residual strong interaction</strong>, mathematically and physically analogous to the van der Waals molecular force in chemistry:
</p>
$$\text{Color Interaction between Quarks (QCD)} \iff \text{Coulomb Interaction between Nucleus & Electrons (QED)}$$
$$\text{Residual Nuclear Force between Nucleons} \iff \text{Van der Waals Dipole Force between Neutral Molecules}$$
<p>
Due to the spontaneous breaking of chiral symmetry in the QCD vacuum ($SU(2)_L \times SU(2)_R \to SU(2)_V$), the pion ($\pi$) emerges as the pseudo-Goldstone boson. Its exceptionally small mass ($m_\pi \approx 140\text{ MeV} \ll m_N \approx 940\text{ MeV}$) makes virtual pion exchange the dominant mechanism governing the long-range residual force between nucleons.
</p>
"""
        },
        {
            "id": "sec-3-5",
            "title": "Exchange of Virtual Particles & Yukawa Potential Derivation",
            "content": r"""
<h3>1. Relativistic Field Equation for a Massive Scalar Field</h3>
<p>
In 1935, Hideki Yukawa proposed that nuclear forces arise from the exchange of an unknown massive quantum field $\phi(\vec{r}, t)$. A massive scalar particle obeys the relativistic <strong>Klein-Gordon equation</strong>:
</p>
$$\left( \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 + \mu^2 \right) \phi(\vec{r}, t) = -\frac{g}{\varepsilon_0} \rho(\vec{r}, t)$$
<p>
where $\mu \equiv \frac{m c}{\hbar}$ is the inverse Compton wavelength of the mediating boson, $g$ is the strong coupling constant, and $\rho(\vec{r})$ is the nucleon source density.
</p>
<p>
For static interactions ($\frac{\partial\phi}{\partial t} = 0$) generated by a point-like nucleon source at the origin ($\rho(\vec{r}) = \delta(\vec{r})$):
</p>
$$\left( \nabla^2 - \mu^2 \right) \phi(\vec{r}) = 0 \quad (\text{for } r > 0)$$
<p>
In spherically symmetric coordinates:
</p>
$$\frac{1}{r}\frac{d^2}{dr^2}(r\phi) - \mu^2 \phi = 0 \implies \frac{d^2}{dr^2}(r\phi) = \mu^2 (r\phi)$$
<p>
The general solution is:
</p>
$$r\phi(r) = C_1 e^{-\mu r} + C_2 e^{+\mu r}$$
<p>
Requiring that the field vanish as $r \to \infty$ forces $C_2 = 0$. As $r \to 0$, the field must approach the unshielded Coulomb-like source $\lim_{r\to 0}\phi(r) = \frac{g}{4\pi r}$, which fixes $C_1 = \frac{g}{4\pi}$.
</p>

<h3>2. The Classic Yukawa Potential</h3>
<p>
The interaction potential energy $V(r) = -g \phi(r)$ between two nucleons separated by distance $r$ is:
</p>
$$V_{\text{Yukawa}}(r) = -\frac{g^2}{4\pi} \frac{e^{-\mu r}}{r} = -g^2 \frac{e^{-r/R}}{r}$$
<p>
where the range of the nuclear interaction $R$ is:
</p>
$$R = \frac{1}{\mu} = \frac{\hbar}{m c}$$
<p>
Using the experimentally known nuclear force range $R \approx 1.4\text{ fm}$:
</p>
$$m c^2 = \frac{\hbar c}{R} = \frac{197.3\text{ MeV}\cdot\text{fm}}{1.4\text{ fm}} \approx 141\text{ MeV}$$
<p>
Yukawa thus famously predicted the existence of a meson with mass $\approx 270\text{ }m_e$. The discovery of the pion in cosmic rays (Powell, Occhialini, Lattes, 1947) with mass $m_{\pi^\pm} = 139.6\text{ MeV}$ brilliantly confirmed Yukawa's meson exchange hypothesis (Nobel Prize 1949).
</p>
""",
            "simulation": "nuc2-yukawa-meson-exchange-sim"
        },
        {
            "id": "sec-3-6",
            "title": "Exchange Force Operators: Majorana, Bartlett, Heisenberg & Wigner",
            "content": r"""
<h3>1. Phenomenological Exchange Potentials</h3>
<p>
To account for nuclear saturation and the anomalous backward peaking observed in high-energy $n$-$p$ scattering, Eugene Wigner, Ettore Majorana, James Bartlett, and Werner Heisenberg introduced four fundamental exchange operators acting on the two-nucleon wavefunction $\psi(\vec{r}_1, \vec{r}_2, \vec{s}_1, \vec{s}_2)$:
</p>
<ol>
  <li><strong>Wigner Force (Ordinary Non-Exchange Force, $\hat{P}_W = \hat{\mathbf{1}}$):</strong> Leaves spatial and spin coordinates unaltered:
  $$V_W(r) = V_0(r) \hat{\mathbf{1}}$$</li>
  <li><strong>Majorana Force (Space-Exchange Force, $\hat{P}_M \equiv \hat{P}_r$):</strong> Exchanges the spatial coordinates of the two nucleons ($\vec{r}_1 \leftrightarrow \vec{r}_2 \implies \vec{r} \to -\vec{r}$):
  $$\hat{P}_r \psi(\vec{r}) = \psi(-\vec{r}) = (-1)^L \psi(\vec{r})$$
  Its eigenvalue is $+1$ for even $L$ ($S, D$ states) and $-1$ for odd $L$ ($P, F$ states). The Majorana interaction is $V_M(r) \hat{P}_r$.</li>
  <li><strong>Bartlett Force (Spin-Exchange Force, $\hat{P}_B \equiv \hat{P}_\sigma$):</strong> Exchanges the spin states of the two nucleons ($\vec{s}_1 \leftrightarrow \vec{s}_2$):
  $$\hat{P}_\sigma = \frac{1 + \vec{\sigma}_1\cdot\vec{\sigma}_2}{2}$$
  Because $\vec{\sigma}_1\cdot\vec{\sigma}_2 = +1$ for triplet ($S=1$) and $-3$ for singlet ($S=0$):
  $$\hat{P}_\sigma |S=1\rangle = +|S=1\rangle, \qquad \hat{P}_\sigma |S=0\rangle = -|S=0\rangle$$
  Its eigenvalue is $(-1)^{S+1}$. The Bartlett interaction is $V_B(r) \hat{P}_\sigma$.</li>
  <li><strong>Heisenberg Force (Space and Spin Exchange Force, $\hat{P}_H \equiv \hat{P}_r \hat{P}_\sigma$):</strong> Exchanges both spatial and spin coordinates simultaneously:
  $$\hat{P}_H = \hat{P}_r \hat{P}_\sigma = -\hat{P}_\tau$$
  Its eigenvalue is $(-1)^L (-1)^{S+1} = -(-1)^{I+1}$. The Heisenberg interaction is $V_H(r) \hat{P}_H$.</li>
</ol>

<h3>2. The Composite Central Potential</h3>
<p>
The general central nucleon-nucleon potential is a linear combination of all four operators:
</p>
$$V_{\text{central}}(r) = V_W(r) + V_M(r) \hat{P}_r + V_B(r) \hat{P}_\sigma + V_H(r) \hat{P}_r \hat{P}_\sigma$$
<p>
Evaluating the eigenvalues in the four basic two-nucleon spin-parity channels:
</p>
<table>
  <thead>
    <tr>
      <th>State (${}^{2S+1}L_J$)</th>
      <th>$L$ Parity</th>
      <th>Spin $S$</th>
      <th>$\hat{P}_r$</th>
      <th>$\hat{P}_\sigma$</th>
      <th>$\hat{P}_H$</th>
      <th>Effective Potential $V_{\text{eff}}(r)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>${}^3S_1$ (Triplet Even)</td>
      <td>Even ($L=0$)</td>
      <td>1</td>
      <td>$+1$</td>
      <td>$+1$</td>
      <td>$+1$</td>
      <td>$V_W + V_M + V_B + V_H$</td>
    </tr>
    <tr>
      <td>${}^1S_0$ (Singlet Even)</td>
      <td>Even ($L=0$)</td>
      <td>0</td>
      <td>$+1$</td>
      <td>$-1$</td>
      <td>$-1$</td>
      <td>$V_W + V_M - V_B - V_H$</td>
    </tr>
    <tr>
      <td>${}^3P$ (Triplet Odd)</td>
      <td>Odd ($L=1$)</td>
      <td>1</td>
      <td>$-1$</td>
      <td>$+1$</td>
      <td>$-1$</td>
      <td>$V_W - V_M + V_B - V_H$</td>
    </tr>
    <tr>
      <td>${}^1P$ (Singlet Odd)</td>
      <td>Odd ($L=1$)</td>
      <td>0</td>
      <td>$-1$</td>
      <td>$-1$</td>
      <td>$+1$</td>
      <td>$V_W - V_M - V_B + V_H$</td>
    </tr>
  </tbody>
</table>
<p>
Nuclear saturation requires that the nuclear force be repulsive in odd-$L$ states while attractive in even-$L$ states, which is achieved when the Majorana exchange component dominates: $V_M \gg V_W, V_B, V_H$ (Serber force mixture).
</p>
"""
        },
        {
            "id": "sec-3-7",
            "title": "One-Boson-Exchange (OBE) Meson Theory: π, σ, ρ, ω & Modern Potentials",
            "content": r"""
<h3>1. The One-Boson-Exchange (OBE) Model</h3>
<p>
A single pion exchange explains only the long-range tail ($r > 2\text{ fm}$) of the nuclear force. A complete microscopic description requires summing exchanges of all low-lying meson states:
</p>
<ol>
  <li><strong>One-Pion Exchange Potential (OPEP, $r > 2\text{ fm}$):</strong> Pions ($\pi^0, \pi^\pm$) are pseudoscalar mesons ($J^P = 0^-$) with isospin $I = 1$ and mass $m_\pi \approx 138\text{ MeV}$. OPEP produces the tensor force and long-range spin-spin interaction:
  $$V_{\text{OPEP}}(r) = \frac{g_{\pi NN}^2}{12\pi}\left( \frac{m_\pi}{M} \right)^2 (\vec{\tau}_1\cdot\vec{\tau}_2) \left[ (\vec{\sigma}_1\cdot\vec{\sigma}_2) + S_{12}\left(1 + \frac{3}{m_\pi r} + \frac{3}{(m_\pi r)^2}\right) \right] \frac{e^{-m_\pi r}}{r}$$</li>
  <li><strong>Scalar Meson Exchange ($\sigma / f_0(500)$, $0.8\text{ fm} < r < 2.0\text{ fm}$):</strong> A scalar meson ($J^P = 0^+$) with isospin $I = 0$ and broad mass $m_\sigma \approx 500\text{ to }600\text{ MeV}$ (physically representing two correlated pions in an $s$-wave state, $\pi\pi$). It provides the powerful <strong>intermediate-range central attraction</strong> responsible for binding atomic nuclei.</li>
  <li><strong>Vector Meson Exchange ($\rho, \omega$, $r < 0.8\text{ fm}$):</strong>
    <ul>
      <li>$\omega$ meson ($J^P = 1^-, I = 0, m_\omega \approx 782\text{ MeV}$): Yields strong <strong>short-range central repulsion</strong> (generating the repulsive hard core) and a large Thomas-like spin-orbit force $\vec{L}\cdot\vec{S}$.</li>
      <li>$\rho$ meson ($J^P = 1^-, I = 1, m_\rho \approx 770\text{ MeV}$): Provides isospin-dependent vector exchange, modifying the tensor force at short distances with opposite sign to OPEP.</li>
    </ul>
  </li>
</ol>

<h3>2. Modern High-Precision Realistic Potentials</h3>
<p>
State-of-the-art nucleon-nucleon potentials fit thousands of $p$-$p$ and $n$-$p$ scattering data points up to $350\text{ MeV}$ with $\chi^2/\text{datum} \approx 1.0$:
</p>
<ul>
  <li><strong>Argonne $v_{18}$ (AV18):</strong> Contains 18 operator terms, including 14 charge-independent terms (central, tensor, spin-orbit, quadratic spin-orbit) plus 4 charge-dependent and charge-symmetry-breaking terms.</li>
  <li><strong>CD-Bonn:</strong> A non-local relativistic One-Boson-Exchange potential based on covariant Feynman amplitudes.</li>
  <li><strong>Chiral Effective Field Theory ($\chi$EFT):</strong> Modern approach based directly on the symmetries of QCD, expanding the nuclear force systematically in powers of $(Q/\Lambda_\chi)$ (Weinberg, van Kolck, Epelbaum, Machleidt). It naturally predicts three-nucleon forces ($3NF$) at next-to-next-to-leading order (NNLO).</li>
</ul>
""",
            "simulation": "nuc2-isospin-multiplet-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-3-1",
            "title": "Yukawa Potential Range and Boson Mass Estimation",
            "statement": r"""(a) Use the Heisenberg energy-time uncertainty relation $\Delta E \Delta t \ge \hbar$ to derive the approximate relation between the mass $m$ of a virtual exchange meson and the maximum spatial range $R$ of the resulting interaction.
(b) Assuming the effective range of the nuclear interaction is $R = 1.41\text{ fm}$, calculate the rest mass of the mediating particle in $\text{MeV}/c^2$ and compare it with the rest mass of the charged pion ($m_{\pi^\pm} = 139.57\text{ MeV}/c^2$).
(c) What would be the range of the interaction if the mediator were the vector $\omega$ meson ($m_\omega = 782.6\text{ MeV}/c^2$)?""",
            "solution": r"""**(a) Derivation of Mass-Range Relation:**
To create a virtual exchange particle of rest mass $m$, an energy $\Delta E = m c^2$ must be borrowed from the vacuum.
By Heisenberg's uncertainty principle:
$$\Delta t \le \frac{\hbar}{\Delta E} = \frac{\hbar}{m c^2}$$
Traveling at or near the speed of light ($v \le c$), the maximum distance $R$ the virtual particle can travel before being reabsorbed is:
$$R \approx c \Delta t = \frac{\hbar c}{m c^2} = \frac{\hbar}{m c}$$
This distance is precisely the reduced Compton wavelength $\lambdabar$ of the mediating boson.

**(b) Mass of the Pionic Mediator:**
Given $R = 1.41\text{ fm}$ and $\hbar c = 197.327\text{ MeV}\cdot\text{fm}$:
$$m c^2 = \frac{\hbar c}{R} = \frac{197.327\text{ MeV}\cdot\text{fm}}{1.41\text{ fm}} \approx \mathbf{139.95\text{ MeV}}$$
Comparing with the empirical charged pion mass $m_{\pi^\pm} = 139.57\text{ MeV}/c^2$:
$$\text{Discrepancy} = \frac{139.95 - 139.57}{139.57} \times 100\% = +0.27\%$$
The prediction matches the real pion mass to within **$0.3\%$**.

**(c) Range for the Vector $\omega$ Meson:**
For $m_\omega c^2 = 782.6\text{ MeV}$:
$$R_\omega = \frac{\hbar c}{m_\omega c^2} = \frac{197.327\text{ MeV}\cdot\text{fm}}{782.6\text{ MeV}} \approx \mathbf{0.252\text{ fm}}$$
The range of the $\omega$ meson exchange is only **$0.25\text{ fm}$**, which operates at ultra-short distances, precisely explaining the physical origin of the repulsive hard core."""
        },
        {
            "id": "nuc2-prob-3-2",
            "title": "Eigenvalues of Nuclear Exchange Force Operators",
            "statement": r"""A phenomenological central nuclear potential is written as:
$$V(r) = V_0(r) \left[ w + m \hat{P}_r + b \hat{P}_\sigma + h \hat{P}_r \hat{P}_\sigma \right]$$
where $w + m + b + h = 1$.
(a) Find the effective potential $V_{\text{eff}}(r) / V_0(r)$ in each of the four channels: ${}^3S_1$, ${}^1S_0$, ${}^3P_1$, and ${}^1P_1$.
(b) In Serber's exchange mixture, the force vanishes completely in odd-$L$ states and is equally divided between Wigner and Majorana forces in even-$L$ states ($w = m = 0.5$, $b = h = 0$). Calculate the interaction strength in each of the four states.
(c) Explain how Serber's mixture naturally explains why nuclear matter saturates at constant density.""",
            "solution": r"""**(a) Channel-by-Channel Operator Eigenvalues:**
The eigenvalues are $\hat{P}_r = (-1)^L$, $\hat{P}_\sigma = (-1)^{S+1}$, and $\hat{P}_H = \hat{P}_r \hat{P}_\sigma = (-1)^{L+S+1}$.
1. **${}^3S_1$ (Triplet Even, $L=0, S=1$):**
   $\hat{P}_r = +1, \hat{P}_\sigma = +1, \hat{P}_H = +1 \implies \frac{V}{V_0} = \mathbf{w + m + b + h = 1.0}$
2. **${}^1S_0$ (Singlet Even, $L=0, S=0$):**
   $\hat{P}_r = +1, \hat{P}_\sigma = -1, \hat{P}_H = -1 \implies \frac{V}{V_0} = \mathbf{w + m - b - h}$
3. **${}^3P_1$ (Triplet Odd, $L=1, S=1$):**
   $\hat{P}_r = -1, \hat{P}_\sigma = +1, \hat{P}_H = -1 \implies \frac{V}{V_0} = \mathbf{w - m + b - h}$
4. **${}^1P_1$ (Singlet Odd, $L=1, S=0$):**
   $\hat{P}_r = -1, \hat{P}_\sigma = -1, \hat{P}_H = +1 \implies \frac{V}{V_0} = \mathbf{w - m - b + h}$

**(b) Serber Mixture Evaluation ($w = 0.5, m = 0.5, b = 0, h = 0$):**
- In ${}^3S_1$: $\frac{V}{V_0} = 0.5 + 0.5 + 0 + 0 = \mathbf{+1.0}$ (Full attraction)
- In ${}^1S_0$: $\frac{V}{V_0} = 0.5 + 0.5 - 0 - 0 = \mathbf{+1.0}$ (Full attraction)
- In ${}^3P_1$: $\frac{V}{V_0} = 0.5 - 0.5 + 0 - 0 = \mathbf{0.0}$ (Zero interaction)
- In ${}^1P_1$: $\frac{V}{V_0} = 0.5 - 0.5 - 0 + 0 = \mathbf{0.0}$ (Zero interaction)

**(c) Explanation of Nuclear Saturation:**
In a nucleus with $A$ nucleons, the number of nucleon pairs is $\frac{1}{2}A(A-1) \approx \frac{1}{2}A^2$.
Because of the Fermi momentum of nucleons, half of the relative orbital states are even-$L$ and half are odd-$L$.
If the potential were purely non-exchange ($w = 1$), all $A(A-1)/2$ pairs would attract, causing total binding energy to grow as $A^2$ and collapsing the nucleus.
Under Serber's mixture, interactions occur **only in even-$L$ states**, while odd-$L$ interactions vanish. Combined with the Pauli exclusion principle, each nucleon can form attractive even-$L$ states with only a fixed maximum number of close neighbors (at most 4 nucleons with distinct spin-isospin states in the same spatial orbital), leading directly to **linear binding energy saturation $B \propto A$**."""
        },
        {
            "id": "nuc2-prob-3-3",
            "title": "Isospin Clebsch-Gordan Analysis of Pion-Nucleon Cross Section Ratios",
            "statement": r"""Consider pion-nucleon scattering near the $\Delta(1232)$ resonance, which is a pure isospin $I = 3/2$ state.
The physical pion states are $\pi^+ (I_3 = +1)$, $\pi^0 (I_3 = 0)$, $\pi^- (I_3 = -1)$, and nucleons are $p (I_3 = +1/2)$, $n (I_3 = -1/2)$.
(a) Decompose the initial states $|\pi^+ p\rangle$, $|\pi^- p\rangle$, and $|\pi^0 n\rangle$ into total isospin eigenstates $|I, I_3\rangle$ using Clebsch-Gordan coefficients.
(b) Express the scattering amplitudes for:
1. $\pi^+ + p \to \pi^+ + p$
2. $\pi^- + p \to \pi^- + p$ (elastic)
3. $\pi^- + p \to \pi^0 + n$ (charge exchange)
in terms of the pure isospin amplitudes $A_{3/2}$ and $A_{1/2}$.
(c) Assuming the $\Delta$ resonance dominates ($|A_{3/2}| \gg |A_{1/2}|$), calculate the ratio of total cross sections:
$$\sigma(\pi^+ p \to \pi^+ p) : \sigma(\pi^- p \to \pi^- p) : \sigma(\pi^- p \to \pi^0 n)$$""",
            "solution": r"""**(a) Isospin Clebsch-Gordan Decomposition:**
Coupling isospin $I_1 = 1$ (pion) and $I_2 = 1/2$ (nucleon):
1. **$|\pi^+ p\rangle = |1, 1\rangle \otimes |1/2, 1/2\rangle$:**
   Total $I_3 = 1 + 1/2 = +3/2$. Since $I$ can only be $3/2$ or $1/2$, the only state with $I_3 = +3/2$ is:
   $$|\pi^+ p\rangle = |3/2, +3/2\rangle$$
2. **$|\pi^- p\rangle = |1, -1\rangle \otimes |1/2, 1/2\rangle$:**
   Total $I_3 = -1 + 1/2 = -1/2$. Using Clebsch-Gordan coefficients $\langle 1, -1; 1/2, 1/2 | I, -1/2\rangle$:
   $$|\pi^- p\rangle = \sqrt{\frac{1}{3}}|3/2, -1/2\rangle - \sqrt{\frac{2}{3}}|1/2, -1/2\rangle$$
3. **$|\pi^0 n\rangle = |1, 0\rangle \otimes |1/2, -1/2\rangle$:**
   Total $I_3 = 0 - 1/2 = -1/2$. Using Clebsch-Gordan coefficients:
   $$|\pi^0 n\rangle = \sqrt{\frac{2}{3}}|3/2, -1/2\rangle + \sqrt{\frac{1}{3}}|1/2, -1/2\rangle$$

**(b) Scattering Amplitudes:**
By the Wigner-Eckart theorem and isospin conservation, $\langle I', I_3'|\hat{T}|I, I_3\rangle = \delta_{I I'} \delta_{I_3 I_3'} A_I$:
1. $T(\pi^+ p \to \pi^+ p) = \langle 3/2, 3/2|\hat{T}|3/2, 3/2\rangle = \mathbf{A_{3/2}}$
2. $T(\pi^- p \to \pi^- p) = \frac{1}{3} A_{3/2} + \frac{2}{3} A_{1/2}$
3. $T(\pi^- p \to \pi^0 n) = \sqrt{\frac{1}{3}}\sqrt{\frac{2}{3}} A_{3/2} - \sqrt{\frac{2}{3}}\sqrt{\frac{1}{3}} A_{1/2} = \frac{\sqrt{2}}{3}(A_{3/2} - A_{1/2})$

**(c) Cross Section Ratios at the $\Delta(1232)$ Resonance ($A_{1/2} \to 0$):**
Setting $A_{1/2} = 0$:
1. $T(\pi^+ p \to \pi^+ p) = A_{3/2} \implies \sigma_1 \propto |A_{3/2}|^2$
2. $T(\pi^- p \to \pi^- p) = \frac{1}{3} A_{3/2} \implies \sigma_2 \propto \frac{1}{9}|A_{3/2}|^2$
3. $T(\pi^- p \to \pi^0 n) = \frac{\sqrt{2}}{3} A_{3/2} \implies \sigma_3 \propto \frac{2}{9}|A_{3/2}|^2$
Multiplying through by 9:
$$\sigma(\pi^+ p \to \pi^+ p) : \sigma(\pi^- p \to \pi^- p) : \sigma(\pi^- p \to \pi^0 n) = 9 : 1 : 2$$
The total cross-section ratio is **$9 : 1 : 2$**, and the ratio of $\pi^+ p$ to total $\pi^- p$ scattering is:
$$\frac{\sigma(\pi^+ p)}{\sigma(\pi^- p \to \text{all})} = \frac{9}{1 + 2} = \frac{9}{3} = \mathbf{3}$$
This exact factor of 3 was experimentally discovered by Enrico Fermi at Chicago in 1952, definitively confirming that the $\Delta(1232)$ is a pure $I = 3/2$ isobar resonance."""
        }
    ]
}

u4_data = {
    "title": "Interaction of Nuclei with Electromagnetic Radiation & Multipole Transitions",
    "subtitle": "Multipole Selection Rules, Transition Probabilities, Internal Conversion & GDR",
    "summary": "Quantum theory of nuclear electromagnetic radiative transitions: multipole expansion of the vector potential into Electric (Eλ) and Magnetic (Mλ) modes, angular momentum and parity selection rules, strict exclusion of 0⁺ → 0⁺ single-photon decay, Weisskopf single-particle transition rate formulas T_W(Eλ) and T_W(Mλ), reduced transition probabilities B(Eλ) and B(Mλ), two-body radiative capture n + p → d + γ and magnetic dipole M1 dominance, internal conversion (IC) electrodynamics, conversion coefficients α_K, α_L, monopole E0 transitions, nuclear isomerism, and Giant Dipole Resonance (GDR) collective hydrodynamic oscillations.",
    "sections": [
        {
            "id": "sec-4-1",
            "title": "Quantization of the Nuclear Electromagnetic Field & Fermi's Golden Rule",
            "content": r"""
<h3>1. Electromagnetic Interaction Hamiltonian</h3>
<p>
The interaction between an ensemble of nucleons and the quantized electromagnetic radiation field is governed by the minimal coupling Hamiltonian $\vec{p} \to \vec{p} - q\vec{A}$. In the Coulomb gauge ($\nabla\cdot\vec{A} = 0$):
</p>
$$\hat{H}_{\text{int}} = -\int \vec{j}(\vec{r})\cdot\vec{A}(\vec{r}) d^3r - \int \vec{M}(\vec{r})\cdot\vec{B}(\vec{r}) d^3r$$
<p>
where $\vec{j}(\vec{r}) = \sum_{k} \frac{e_k}{2M} (\vec{p}_k \delta(\vec{r}-\vec{r}_k) + \delta(\vec{r}-\vec{r}_k)\vec{p}_k)$ is the convection current density of protons, and $\vec{M}(\vec{r}) = \sum_k \mu_N g_s^{(k)} \vec{s}_k \delta(\vec{r}-\vec{r}_k)$ is the magnetization density due to nucleon intrinsic spins.
</p>

<h3>2. Transition Rates from Fermi's Golden Rule</h3>
<p>
For a nucleus decaying from initial excited state $|i\rangle$ of energy $E_i$ to final state $|f\rangle$ of energy $E_f$ with emission of a photon of energy $\hbar\omega = E_i - E_f$ and wavevector $k = \omega/c$, time-dependent perturbation theory yields <strong>Fermi's Golden Rule</strong>:
</p>
$$\lambda_{fi} = \frac{2\pi}{\hbar} |\langle f; 1_{\vec{k},\epsilon}| \hat{H}_{\text{int}} |i; 0\rangle|^2 \rho(E)$$
<p>
where the density of final photon states in solid angle $d\Omega$ is $\rho(E) = \frac{V \omega^2 d\Omega}{(2\pi)^3 \hbar c^3}$.
</p>
<p>
Because nuclear dimensions ($R \sim 5\text{ fm}$) are vastly smaller than the wavelength of typical gamma rays ($E_\gamma \sim 1\text{ MeV} \implies \lambdabar = \frac{\hbar c}{E_\gamma} \approx 200\text{ fm}$):
</p>
$$k R = \frac{R}{\lambdabar} = \frac{5\text{ fm}}{200\text{ fm}} \approx 0.025 \ll 1$$
<p>
This long-wavelength condition justifies expanding the vector potential $\vec{A}(\vec{r}) \propto e^{i\vec{k}\cdot\vec{r}}$ in spherical multipoles of order $(k r)^\lambda$.
</p>
"""
        },
        {
            "id": "sec-4-2",
            "title": "Classification of Multipole Radiation: Electric (Eλ) and Magnetic (Mλ) Modes",
            "content": r"""
<h3>1. Spherical Multipole Expansion of the Radiation Field</h3>
<p>
The radiation field can be decomposed rigorously into orthogonal vector spherical harmonics carrying definite total angular momentum $\lambda\hbar$ and parity $\pi$:
</p>
<ul>
  <li><strong>Electric Multipole of Order $\lambda$ ($E\lambda$):</strong> Generated by the oscillating nuclear electric charge distribution $\rho(\vec{r})$ and convection currents. The transition operator is:
  $$\hat{\mathcal{M}}(E\lambda, \mu) = \sum_{k=1}^A e_k r_k^\lambda Y_{\lambda\mu}(\theta_k, \phi_k)$$</li>
  <li><strong>Magnetic Multipole of Order $\lambda$ ($M\lambda$):</strong> Generated by the circulating orbital current loops and intrinsic nucleon spin magnetic moments. The transition operator is:
  $$\hat{\mathcal{M}}(M\lambda, \mu) = \mu_N \sum_{k=1}^A \left[ \frac{2}{\lambda+1} g_l^{(k)} \vec{l}_k + g_s^{(k)} \vec{s}_k \right] \cdot \nabla \left( r_k^\lambda Y_{\lambda\mu}(\hat{r}_k) \right)$$</li>
</ul>

<h3>2. Multipolarity Terminology</h3>
<table>
  <thead>
    <tr>
      <th>Order $\lambda$</th>
      <th>Multipolarity Name</th>
      <th>Electric Mode</th>
      <th>Magnetic Mode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$\lambda = 1$</td>
      <td>Dipole</td>
      <td>$E1$</td>
      <td>$M1$</td>
    </tr>
    <tr>
      <td>$\lambda = 2$</td>
      <td>Quadrupole</td>
      <td>$E2$</td>
      <td>$M2$</td>
    </tr>
    <tr>
      <td>$\lambda = 3$</td>
      <td>Octupole</td>
      <td>$E3$</td>
      <td>$M3$</td>
    </tr>
    <tr>
      <td>$\lambda = 4$</td>
      <td>Hexadecapole</td>
      <td>$E4$</td>
      <td>$M4$</td>
    </tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sec-4-3",
            "title": "Angular Momentum & Parity Selection Rules for Multipole Transitions",
            "content": r"""
<h3>1. Angular Momentum Conservation Selection Rule</h3>
<p>
A photon emitted in a multipole mode of order $\lambda$ carries an intrinsic angular momentum of $\lambda\hbar$ (with $\lambda \ge 1$, since photons are transverse vector bosons with helicity $\pm 1$ and cannot exist in a scalar $\lambda = 0$ state).
</p>
<p>
By conservation of angular momentum $\vec{I}_i = \vec{I}_f + \vec{\lambda}$, the triangle inequality requires:
</p>
$$|I_i - I_f| \le \lambda \le I_i + I_f$$
<p>
<strong>Absolute Exclusion of Single-Photon $0 \to 0$ Transitions:</strong>
If $I_i = 0$ and $I_f = 0$, then $|0 - 0| \le \lambda \le 0 + 0 \implies \lambda = 0$. Because there are no longitudinal or scalar photons in free space, <strong>single-photon transitions between two spin-zero states ($0^+ \to 0^+$ or $0^- \to 0^+$) are strictly forbidden</strong> by conservation of angular momentum. Such states decay via internal conversion (IC) or internal pair creation ($e^+ e^-$).
</p>

<h3>2. Parity Selection Rules</h3>
<p>
The electromagnetic multipole operators transform under spatial inversion $\vec{r} \to -\vec{r}$ according to their parity:
</p>
$$\pi(E\lambda) = (-1)^\lambda, \qquad \pi(M\lambda) = (-1)^{\lambda+1}$$
<p>
Therefore, the parity of the nuclear states $\pi_i$ and $\pi_f$ must satisfy:
</p>
$$\text{For Electric Transitions }(E\lambda): \quad \pi_i \pi_f = (-1)^\lambda \implies \Delta\pi = \begin{cases} \text{No parity change}, & \lambda = 2, 4, 6 \dots (E2, E4) \\ \text{Parity change}, & \lambda = 1, 3, 5 \dots (E1, E3) \end{cases}$$
$$\text{For Magnetic Transitions }(M\lambda): \quad \pi_i \pi_f = (-1)^{\lambda+1} \implies \Delta\pi = \begin{cases} \text{No parity change}, & \lambda = 1, 3, 5 \dots (M1, M3) \\ \text{Parity change}, & \lambda = 2, 4, 6 \dots (M2, M4) \end{cases}$$

<h3>3. Summary Decision Matrix</h3>
<table>
  <thead>
    <tr>
      <th>Transition Character</th>
      <th>Parity Change ($\pi_i \pi_f$)</th>
      <th>Allowed Multipoles</th>
      <th>Dominant Mode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$2^+ \to 0^+$</td>
      <td>No ($\Delta\pi = +1$)</td>
      <td>$E2, M3, E4 \dots$</td>
      <td>$E2$</td>
    </tr>
    <tr>
      <td>$1^- \to 0^+$</td>
      <td>Yes ($\Delta\pi = -1$)</td>
      <td>$E1, M2, E3 \dots$</td>
      <td>$E1$</td>
    </tr>
    <tr>
      <td>$2^+ \to 1^+$</td>
      <td>No ($\Delta\pi = +1$)</td>
      <td>$M1, E2, M3 \dots$</td>
      <td>$M1 + E2$ (Mixed)</td>
    </tr>
    <tr>
      <td>$3^- \to 0^+$</td>
      <td>Yes ($\Delta\pi = -1$)</td>
      <td>$E3, M4, E5 \dots$</td>
      <td>$E3$</td>
    </tr>
  </tbody>
</table>
""",
            "simulation": "nuc2-multipole-selection-sim"
        },
        {
            "id": "sec-4-4",
            "title": "Weisskopf Single-Particle Transition Rate Estimates & Reduced Probabilities",
            "content": r"""
<h3>1. Derivation of the Weisskopf Units (W.u.)</h3>
<p>
Victor Weisskopf derived standard baseline transition rates by assuming a single valence proton moves from a single-particle orbital $j_i$ to $j_f$ in a spherical nucleus of radius $R = R_0 A^{1/3}$ ($R_0 \approx 1.2\text{ fm}$), with constant radial wavefunctions:
</p>
$$\langle r^\lambda \rangle \approx \frac{\int_0^R r^\lambda r^2 dr}{\int_0^R r^2 dr} = \frac{3}{\lambda + 3} R^\lambda$$
<p>
The resulting <strong>Weisskopf single-particle transition rates</strong> $\lambda_W = T_W$ in $\text{s}^{-1}$ for photon energy $E_\gamma$ in MeV are:
</p>
$$\lambda_W(E1) = 1.023 \times 10^{14} A^{2/3} E_\gamma^3\text{ s}^{-1}$$
$$\lambda_W(E2) = 7.28 \times 10^7 A^{4/3} E_\gamma^5\text{ s}^{-1}$$
$$\lambda_W(E3) = 3.39 \times 10^1 A^2 E_\gamma^7\text{ s}^{-1}$$
$$\lambda_W(M1) = 3.15 \times 10^{13} E_\gamma^3\text{ s}^{-1}$$
$$\lambda_W(M2) = 2.24 \times 10^7 A^{2/3} E_\gamma^5\text{ s}^{-1}$$
$$\lambda_W(M3) = 1.04 \times 10^1 A^{4/3} E_\gamma^7\text{ s}^{-1}$$

<h3>2. Hierarchy and Multipole Dominance</h3>
<p>
Because $k R \ll 1$, each increase in multipole order $\lambda \to \lambda + 1$ suppresses the transition probability by a colossal factor of $(k R)^2 \sim 10^{-4} \text{ to } 10^{-6}$:
</p>
$$\frac{\lambda_W(E(\lambda+1))}{\lambda_W(E\lambda)} \sim (k R)^2 \approx 10^{-4}$$
$$\frac{\lambda_W(M\lambda)}{\lambda_W(E\lambda)} \approx 10^{-2}$$
<p>
Therefore, in any electromagnetic transition, the lowest allowed multipole completely dominates the decay rate unless hindered by selection rules.
</p>

<h3>3. Physical Significance of Weisskopf Units</h3>
<ul>
  <li>If an experimental transition rate matches $\sim 1\text{ W.u.}$, the transition is confirmed to be an <strong>independent single-particle transition</strong>.</li>
  <li>If $B(E2) \gg 1\text{ W.u.}$ (often $10\text{ to }300\text{ W.u.}$ in deformed rare-earth and actinide nuclei), the transition is <strong>collective</strong>, involving the coherent motion of dozens of nucleons in a rotating or vibrating nuclear core.</li>
  <li>If $B(E1) \ll 1\text{ W.u.}$ ($10^{-3}\text{ to }10^{-6}\text{ W.u.}$), the transition is <strong>strongly hindered</strong>, typically by isospin selection rules ($\Delta I = 0$ in self-conjugate $N=Z$ nuclei) or shape changes.</li>
</ul>
"""
        },
        {
            "id": "sec-4-5",
            "title": "Radiative Capture in the Two-Body System (n + p → d + γ Magnetic Dipole M1)",
            "content": r"""
<h3>1. The Thermal Neutron Radiative Capture Process</h3>
<p>
When thermal neutrons ($E_n \approx 0.025\text{ eV}$) interact with hydrogen, capture occurs via gamma emission:
</p>
$$n + p \to {}^2\text{H} + \gamma \quad (E_\gamma = B = 2.2246\text{ MeV})$$
<p>
The incident thermal neutron has $l = 0$ ($s$-wave), so the initial continuum state has positive parity $\pi_i = +1$. The bound deuteron has $J^\pi = 1^+$.
</p>
<p>
Because there is no change in parity ($\pi_i = \pi_f = +1$), electric dipole radiation ($E1$, which requires $\Delta\pi = -1$) is strictly forbidden. The dominant decay mode is <strong>magnetic dipole radiation ($M1$)</strong>.
</p>

<h3>2. The Spin-Flip Capture Mechanism</h3>
<p>
The transition proceeds from the unbound ${}^1S_0$ continuum state ($J=0, S=0$) to the ${}^3S_1$ component of the deuteron bound state ($J=1, S=1$). The magnetic dipole transition operator is:
</p>
$$\vec{\mathcal{M}}(M1) = \mu_N (g_p \vec{s}_p + g_n \vec{s}_n) = \frac{\mu_N}{2} \left[ (\mu_p + \mu_n)(\vec{\sigma}_p + \vec{\sigma}_n) + (\mu_p - \mu_n)(\vec{\sigma}_p - \vec{\sigma}_n) \right]$$
<p>
The spin-flip transition between singlet ($S=0$) and triplet ($S=1$) is driven by the term proportional to $(\mu_p - \mu_n)$:
</p>
$$\langle {}^3S_1 | (\vec{\sigma}_p - \vec{\sigma}_n) | {}^1S_0 \rangle \ne 0$$
<p>
Because $(\mu_p - \mu_n) = 2.793 - (-1.913) = +4.706\text{ }\mu_N$ is exceptionally large, the transition amplitude is greatly enhanced.
</p>

<h3>3. Cross-Section Discrepancy & Meson Exchange Currents</h3>
<p>
The cross section calculated from the simple single-particle wavefunctions without meson exchange currents is:
</p>
$$\sigma_{\text{calc}}^{(0)} = 302 \pm 4\text{ mb}$$
<p>
However, high-precision thermal neutron capture experiments yield:
</p>
$$\sigma_{\text{exp}} = 334.2 \pm 0.5\text{ mb}$$
<p>
The famous $10\%$ discrepancy ($\Delta\sigma \approx 32\text{ mb}$) is resolved by including <strong>Meson Exchange Currents (MEC)</strong>: during the collision, virtual charged pions ($\pi^\pm$) in flight between the proton and neutron directly couple to the photon field ($\gamma \pi \pi$ and $\gamma N N \pi$ contact vertices), providing conclusive proof of sub-nucleonic meson degrees of freedom in nuclei.
</p>
"""
        },
        {
            "id": "sec-4-6",
            "title": "Internal Conversion (IC), Conversion Coefficients α, and E0 Monopole Decay",
            "content": r"""
<h3>1. The Microscopic Mechanism of Internal Conversion</h3>
<p>
In an excited nucleus, gamma decay is not the only electromagnetic de-excitation mechanism. The oscillating nuclear electromagnetic multipole field extends into the atomic electron cloud. A bound atomic electron (most commonly from the innermost $K$ shell, $n=1$) can undergo direct electromagnetic interaction with the nucleus, being ejected into the continuum:
</p>
$${}^A_Z X^* \to {}^A_Z X^+ + e_{\text{IC}}^-$$
<p>
This process is <strong>Internal Conversion (IC)</strong>.
</p>
<p>
The kinetic energy of the ejected conversion electron is:
</p>
$$T_e = E_\gamma - B_e$$
<p>
where $E_\gamma = E_i - E_f$ is the nuclear transition energy and $B_e$ is the electron atomic binding energy ($B_K, B_L, \dots$). Consequently, conversion electron spectra consist of <strong>discrete, sharp monoenergetic lines</strong>, in stark contrast to continuous beta spectra.
</p>

<h3>2. The Internal Conversion Coefficient (ICC)</h3>
<p>
The internal conversion coefficient $\alpha$ is defined as the ratio of the conversion electron decay rate ($\lambda_e$) to the gamma-ray emission rate ($\lambda_\gamma$):
</p>
$$\alpha \equiv \frac{\lambda_e}{\lambda_\gamma} = \alpha_K + \alpha_{L_I} + \alpha_{L_{II}} + \alpha_{L_{III}} + \alpha_M + \dots$$
<p>
The total transition probability is $\lambda_{\text{total}} = \lambda_\gamma + \lambda_e = \lambda_\gamma (1 + \alpha)$.
</p>
<p>
Parametric dependence of $\alpha$:
</p>
$$\alpha(E\lambda) \propto Z^3 \left( \frac{m_e c^2}{E_\gamma} \right)^{\lambda + 7/2}, \qquad \alpha(M\lambda) \propto Z^3 \left( \frac{m_e c^2}{E_\gamma} \right)^{\lambda + 5/2}$$
<p>
Key physical properties:
</p>
<ul>
  <li><strong>Heavy Nuclei ($Z^3$ Scaling):</strong> IC dominates in heavy elements ($Z \ge 50$) because $K$-shell electrons have wavefunctions strongly concentrated at the nucleus ($\psi_e(0) \propto Z^{3/2}$).</li>
  <li><strong>High Multipolarity ($\lambda \ge 3$):</strong> Because $\lambda_\gamma$ is heavily suppressed for high multipolarities while electron conversion near the origin is less hindered, high-$\lambda$ transitions have massive conversion coefficients ($\alpha \gg 1$).</li>
  <li><strong>Low Transition Energy ($E_\gamma \le 200\text{ keV}$):</strong> Low energy transitions proceed almost entirely via conversion electrons.</li>
</ul>

<h3>3. Electric Monopole ($E0$) Transitions</h3>
<p>
When both the initial and final states have spin-parity $0^+$ (such as in ${}^{16}\text{O}^*(6.05\text{ MeV}) \to {}^{16}\text{O}(\text{g.s.}, 0^+)$ or ${}^{72}\text{Ge}^*(691\text{ keV}) \to {}^{72}\text{Ge}(\text{g.s.}, 0^+)$), single-photon emission is strictly forbidden ($\lambda = 0$).
</p>
<p>
Because the spherically symmetric Coulomb monopole operator $\hat{\mathcal{M}}(E0) = e \sum r_p^2$ can overlap with atomic $s_{1/2}$ electrons entering the nuclear interior, these states de-excite via <strong>pure $E0$ internal conversion</strong> (or electron-positron pair creation if $E_\gamma > 2 m_e c^2 = 1.022\text{ MeV}$).
</p>
"""
        },
        {
            "id": "sec-4-7",
            "title": "Transitions in Highly Excited Nuclei: The Giant Dipole Resonance (GDR)",
            "content": r"""
<h3>1. The Phenomenon of the Giant Dipole Resonance</h3>
<p>
When atomic nuclei are bombarded with high-energy photons ($E_\gamma \approx 10\text{ to }25\text{ MeV}$), the total photoabsorption cross section $\sigma_{\text{abs}}(E_\gamma)$ does not exhibit isolated narrow Breit-Wigner peaks. Instead, it displays a colossal, universal, broad peak known as the <strong>Giant Dipole Resonance (GDR)</strong>:
</p>
<ul>
  <li><strong>Resonance Energy:</strong> Systematically decreases with mass number $A$:
  $$E_{\text{GDR}} \approx 78 A^{-1/3}\text{ MeV} \quad (\text{or } 31.2 A^{-1/3} + 20.6 A^{-1/6}\text{ MeV})$$
  In light nuclei ($A \sim 16$), $E_{\text{GDR}} \approx 22\text{ to }25\text{ MeV}$; in heavy nuclei ($A \sim 208$), $E_{\text{GDR}} \approx 13.5\text{ MeV}$.</li>
  <li><strong>Resonance Width ($\Gamma$):</strong> Typically $\Gamma \approx 4\text{ to }6\text{ MeV}$ in spherical magic nuclei, broadening in deformed nuclei.</li>
  <li><strong>Exhaustion of the TRK Sum Rule:</strong> The integrated photoabsorption cross section exhausts the classical <strong>Thomas-Reiche-Kuhn (TRK) dipole sum rule</strong>:
  $$\int_0^\infty \sigma_{\text{abs}}(E_\gamma) dE_\gamma = \frac{2\pi^2 e^2 \hbar}{M c} \frac{N Z}{A} (1 + \kappa) \approx 60 \frac{N Z}{A}\text{ MeV}\cdot\text{mb}$$
  where $\kappa \approx 0.2\text{ to }0.4$ represents meson exchange current enhancements.</li>
</ul>

<h3>2. Macroscopic Hydrodynamic Models: Goldhaber-Teller vs Steinwedel-Jensen</h3>
<p>
The GDR is a collective macroscopic vibration of all protons against all neutrons:
</p>
<ol>
  <li><strong>Goldhaber-Teller (GT) Model:</strong> The protons are treated as a rigid sphere oscillating out of phase with a rigid neutron sphere against the restoring force of the nuclear symmetry energy. It predicts $E_{\text{GDR}} \propto A^{-1/6}$.</li>
  <li><strong>Steinwedel-Jensen (SJ) Model:</strong> The protons and neutrons form compressible fluids within a fixed spherical nuclear boundary. Acoustic compressional density waves oscillate against each other ($n_p - n_n \ne 0$). It predicts $E_{\text{GDR}} \propto A^{-1/3}$.</li>
</ol>

<h3>3. Resonance Splitting in Deformed Nuclei</h3>
<p>
In deformed, prolate nuclei (such as the rare-earths ${}^{160}\text{Gd}$ or actinides ${}^{238}\text{U}$), the GDR splits into two distinct peaks:
</p>
<ul>
  <li><strong>Low-Energy Peak ($E_a$):</strong> Collective oscillation along the longer major axis ($a$). Since the wavelength is longer, the frequency is lower.</li>
  <li><strong>High-Energy Peak ($E_b$):</strong> Collective oscillation along the shorter minor axes ($b$).</li>
</ul>
<p>
The ratio of peak energies directly yields the nuclear deformation axis ratio: $\frac{E_b}{E_a} \approx \frac{a}{b} = 1 + 0.95 \beta_2$.
</p>
""",
            "simulation": "nuc2-internal-conversion-gdr-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-4-1",
            "title": "Multipole Selection Rules and Weisskopf Half-Life Estimates",
            "statement": r"""A nuclear excited state of spin-parity $I_i^{\pi_i} = 7/2^+$ at excitation energy $E_x = 0.500\text{ MeV}$ in a nucleus with $A = 125$ de-excites to the ground state $I_f^{\pi_f} = 1/2^+$.
(a) Determine all allowed electromagnetic multipoles and identify the dominant radiation mode.
(b) Using the Weisskopf single-particle formulas, calculate the transition probability $\lambda_W$ and estimated half-life $t_{1/2}$ for this transition.
(c) If the next-lowest allowed multipole could compete, estimate the branching ratio between the two modes.""",
            "solution": r"""**(a) Allowed Multipoles and Dominant Mode:**
Initial state: $I_i = 7/2, \pi_i = +1$. Final state: $I_f = 1/2, \pi_f = +1$.
Angular momentum selection rule:
$$|7/2 - 1/2| \le \lambda \le 7/2 + 1/2 \implies 3 \le \lambda \le 4$$
Thus the allowed multipole orders are $\lambda = 3$ and $\lambda = 4$.
Parity selection rule:
No parity change occurs ($\pi_i \pi_f = (+1)(+1) = +1$).
- For $\lambda = 3$: $\Delta\pi(E3) = (-1)^3 = -1$ (forbidden). But $\Delta\pi(M3) = (-1)^{3+1} = +1$ (allowed!).
- For $\lambda = 4$: $\Delta\pi(E4) = (-1)^4 = +1$ (allowed!). $\Delta\pi(M4) = (-1)^{4+1} = -1$ (forbidden).
The allowed modes are **$M3$ and $E4$**.
Because $\lambda = 3 < 4$, the lowest multipole **$M3$ (Magnetic Octupole)** is the dominant radiation mode.

**(b) Weisskopf Transition Rate and Half-Life for $M3$:**
Using $A = 125$ and $E_\gamma = 0.500\text{ MeV}$:
$$\lambda_W(M3) = 1.04 \times 10^1 A^{4/3} E_\gamma^7\text{ s}^{-1}$$
$$A^{4/3} = (125)^{4/3} = (5^3)^{4/3} = 5^4 = 625$$
$$E_\gamma^7 = (0.500)^7 = \frac{1}{128} \approx 0.0078125\text{ MeV}^7$$
$$\lambda_W(M3) = 1.04 \times 10^1 \times 625 \times 0.0078125 \approx 10.4 \times 4.8828 \approx \mathbf{50.78\text{ s}^{-1}}$$
The estimated half-life is:
$$t_{1/2} = \frac{\ln 2}{\lambda_W(M3)} = \frac{0.69315}{50.78\text{ s}^{-1}} \approx \mathbf{0.01365\text{ s}} = \mathbf{13.65\text{ ms}}$$
Because $M3$ is a high-multipolarity transition, the half-life is thousands of times longer than typical nanosecond gamma transitions, forming a nuclear isomer!

**(c) Competition from $E4$:**
$$\lambda_W(E4) = \frac{1.2 \times 10^7}{(2\times 4 + 1)!!^2} \dots \approx 3 \times 10^{-5} A^{8/3} E_\gamma^9\text{ s}^{-1}$$
$$A^{8/3} = (625)^2 = 390625, \quad E_\gamma^9 = (0.5)^9 = 0.001953$$
$$\lambda_W(E4) \approx 3 \times 10^{-5} \times 390625 \times 0.001953 \approx 0.0229\text{ s}^{-1}$$
Branching ratio:
$$\frac{\lambda_W(E4)}{\lambda_W(M3)} \approx \frac{0.0229}{50.78} \approx 4.5 \times 10^{-4} \approx 0.045\%$$
The $E4$ branch represents less than **$0.05\%$** of the decay, confirming $M3$ overwhelming dominance."""
        },
        {
            "id": "nuc2-prob-4-2",
            "title": "Internal Conversion Coefficient and Total De-excitation Half-Life",
            "statement": r"""The first excited state of $^{119}\text{Sn}$ at $E_x = 23.87\text{ keV}$ decays to the ground state via an $M1$ transition.
The experimental $K$-shell and total internal conversion coefficients are:
$$\alpha_K = 4.4, \quad \alpha_{\text{total}} = 5.1$$
The observed total half-life of the state is $t_{1/2} = 17.8\text{ ns}$.
(a) Calculate the partial half-life $t_{1/2}^{(\gamma)}$ for pure gamma-ray emission.
(b) Calculate the partial half-life $t_{1/2}^{(e)}$ for conversion electron emission.
(c) Compute the ratio of the experimentally observed $M1$ gamma transition rate to the single-particle Weisskopf estimate $\lambda_W(M1)$ and interpret the result.""",
            "solution": r"""**(a) Partial Half-Life for Gamma Emission $t_{1/2}^{(\gamma)}$:**
The total decay constant is related to the partial decay constants by:
$$\lambda_{\text{total}} = \lambda_\gamma + \lambda_e = \lambda_\gamma (1 + \alpha_{\text{total}})$$
Since half-life is inversely proportional to decay constant ($t_{1/2} = \frac{\ln 2}{\lambda}$):
$$t_{1/2}^{(\gamma)} = t_{1/2} (1 + \alpha_{\text{total}}) = (17.8\text{ ns})(1 + 5.1) = 17.8 \times 6.1 = \mathbf{108.58\text{ ns}}$$

**(b) Partial Half-Life for Conversion Electron Emission $t_{1/2}^{(e)}$:**
$$\lambda_e = \alpha_{\text{total}} \lambda_\gamma \implies t_{1/2}^{(e)} = \frac{t_{1/2}^{(\gamma)}}{\alpha_{\text{total}}} = \frac{108.58\text{ ns}}{5.1} \approx \mathbf{21.29\text{ ns}}$$
(Alternatively, $t_{1/2}^{(e)} = t_{1/2} \frac{1 + \alpha_{\text{total}}}{\alpha_{\text{total}}} = 17.8 \times \frac{6.1}{5.1} \approx 21.29\text{ ns}$).

**(c) Comparison with the Weisskopf Single-Particle Estimate:**
The experimental gamma decay rate is:
$$\lambda_\gamma = \frac{\ln 2}{t_{1/2}^{(\gamma)}} = \frac{0.69315}{108.58 \times 10^{-9}\text{ s}} \approx 6.384 \times 10^6\text{ s}^{-1}$$
The theoretical Weisskopf single-particle rate for $M1$ with $E_\gamma = 0.02387\text{ MeV}$:
$$\lambda_W(M1) = 3.15 \times 10^{13} E_\gamma^3 = 3.15 \times 10^{13} (0.02387)^3 = 3.15 \times 10^{13} (1.360 \times 10^{-5}) \approx 4.284 \times 10^8\text{ s}^{-1}$$
The hindrance factor is:
$$\frac{\lambda_\gamma}{\lambda_W(M1)} = \frac{6.384 \times 10^6}{4.284 \times 10^8} \approx 0.0149 \approx \frac{1}{67}$$
**Interpretation:**
The gamma transition is hindered by a factor of $\approx 67$ relative to the single-particle estimate. This occurs because the $23.87\text{ keV}$ state is an $s_{1/2} \to d_{3/2}$ transition involving an orbital angular momentum change $\Delta l = 2$ ($l$-forbidden $M1$ transition), which requires core polarization or tensor exchange corrections to proceed."""
        },
        {
            "id": "nuc2-prob-4-3",
            "title": "Thomas-Reiche-Kuhn (TRK) Energy-Weighted Dipole Sum Rule Calculation",
            "statement": r"""The classical Thomas-Reiche-Kuhn (TRK) dipole sum rule for the total integrated nuclear photoabsorption cross section is:
$$\int_0^\infty \sigma_{\text{abs}}(E_\gamma) dE_\gamma = \frac{2\pi^2 e^2 \hbar}{M c} \frac{N Z}{A} \approx 59.74 \frac{N Z}{A}\text{ MeV}\cdot\text{mb}$$
For the doubly-magic nucleus Lead-208 ($^{208}_{82}\text{Pb}_{126}$):
(a) Calculate the classical TRK sum rule integrated cross section in $\text{MeV}\cdot\text{b}$.
(b) The experimental Giant Dipole Resonance in $^{208}\text{Pb}$ is well-fitted by a Lorentzian cross section:
$$\sigma(E) = \frac{\sigma_0 \Gamma^2 E^2}{(E^2 - E_0^2)^2 + \Gamma^2 E^2}$$
with resonance peak energy $E_0 = 13.6\text{ MeV}$, width $\Gamma = 4.0\text{ MeV}$, and peak cross section $\sigma_0 = 640\text{ mb}$.
Compute the integrated cross section under this Lorentzian:
$$\int_0^\infty \sigma(E) dE = \frac{\pi}{2} \sigma_0 \Gamma$$
(c) Determine the enhancement factor $(1 + \kappa)$ and state its physical origin in terms of nuclear forces.""",
            "solution": r"""**(a) Classical TRK Sum Rule for $^{208}\text{Pb}$:**
For $^{208}_{82}\text{Pb}$, $Z = 82$, $N = 126$, $A = 208$:
$$\frac{N Z}{A} = \frac{126 \times 82}{208} = \frac{10332}{208} \approx 49.673$$
The classical sum rule gives:
$$\Sigma_{\text{TRK}} = 59.74 \times 49.673 \approx 2967.5\text{ MeV}\cdot\text{mb} = \mathbf{2.968\text{ MeV}\cdot\text{b}}$$

**(b) Integrated Experimental Lorentzian Cross Section:**
$$\Sigma_{\text{exp}} = \frac{\pi}{2} \sigma_0 \Gamma = \frac{\pi}{2} (640\text{ mb}) (4.0\text{ MeV}) = \frac{\pi}{2} (2560\text{ MeV}\cdot\text{mb}) = 1280 \pi\text{ MeV}\cdot\text{mb}$$
$$\Sigma_{\text{exp}} \approx 4021.2\text{ MeV}\cdot\text{mb} = \mathbf{4.021\text{ MeV}\cdot\text{b}}$$

**(c) Enhancement Factor $(1 + \kappa)$ and Physical Origin:**
$$(1 + \kappa) = \frac{\Sigma_{\text{exp}}}{\Sigma_{\text{TRK}}} = \frac{4.021\text{ MeV}\cdot\text{b}}{2.968\text{ MeV}\cdot\text{b}} \approx \mathbf{1.355} \implies \kappa \approx 0.355$$
The experimental photoabsorption exhausts **$135.5\%$** of the classical sum rule (an enhancement $\kappa \approx 35\%$).
**Physical Origin:**
The classical TRK sum rule assumes velocity-independent, local interactions that commute with the dipole operator $\hat{\vec{D}} = e \sum z_i$.
In real nuclei, the nuclear force contains **space-exchange Majorana forces** $V_M \hat{P}_r$ and momentum-dependent tensor forces that do *not* commute with the nucleon coordinate positions:
$$[\hat{V}_M, \vec{r}_i] \ne 0$$
This non-zero double commutator adds a positive contribution to the double commutator $[[\hat{H}, \hat{D}], \hat{D}]$, which physically represents the absorption of photons by **virtual charged pions ($\pi^\pm$) exchanged between protons and neutrons** during the collective GDR oscillation."""
        }
    ]
}

with open("nuc2_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3_data, f, indent=2, ensure_ascii=False)

with open("nuc2_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4_data, f, indent=2, ensure_ascii=False)

print("nuc2_u3.json and nuc2_u4.json successfully written!")
