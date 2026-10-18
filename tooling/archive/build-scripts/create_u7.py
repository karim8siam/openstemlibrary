import json

def get_unit_7():
    u7 = {
        "id": "unit-7",
        "number": 7,
        "title": "Electronic Band Theory of Solids",
        "leadSummary": "Quantum mechanical foundation of electrons in periodic crystal potentials: Sommerfeld free electron gas, Bloch's theorem, nearly free electron approximation, Kronig-Penney dispersion model, tight-binding LCAO formulation, band classifications (conductors, semiconductors, insulators), intrinsic/extrinsic semiconductor statistics, and controlled valency.",
        "simulations": ["sim_ssc_band_structure_kronig_penney"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Free Electron Fermi Gas Model: Sommerfeld Quantum Model & Density of States",
                "content": r"""The electronic behavior of metallic solids was first addressed quantum mechanically by Arnold Sommerfeld (1928), who combined the classical Drude free-electron gas with Pauli's exclusion principle and Fermi-Dirac statistics.

### Quantum Particle-in-a-Box State Counting
Consider $N$ non-interacting conduction electrons confined within a macroscopic cubic crystal of volume $V = L^3$. The time-independent Schrödinger equation for a free electron is:
\\[
-\\frac{\\hbar^2}{2m} \\nabla^2 \\psi(\\mathbf{r}) = E \\psi(\\mathbf{r})
\\]
Imposing periodic Born-von Kármán boundary conditions $\\psi(x+L, y, z) = \\psi(x, y, z)$ gives plane-wave eigenstates:
\\[
\\psi_\\mathbf{k}(\\mathbf{r}) = \\frac{1}{\\sqrt{V}} e^{i \\mathbf{k} \\cdot \\mathbf{r}}, \\quad \\mathbf{k} = \\left( \\frac{2\\pi n_x}{L}, \\frac{2\\pi n_y}{L}, \\frac{2\\pi n_z}{L} \\right) \\quad (n_x, n_y, n_z \\in \\mathbb{Z})
\\]
The parabolic dispersion relation is:
\\[
E(\\mathbf{k}) = \\frac{\\hbar^2 k^2}{2m} = \\frac{\\hbar^2 (k_x^2 + k_y^2 + k_z^2)}{2m}
\\]

### Fermi Sphere, Fermi Energy & Density of States
At absolute zero ($T = 0\\text{ K}$), electrons occupy the lowest available energy levels up to the **Fermi energy** $E_F$. In reciprocal $\\mathbf{k}$-space, occupied states form a sphere of radius $k_F$ (the **Fermi wavevector**).
Each $\\mathbf{k}$-state occupies a volume of $(2\\pi/L)^3 = 8\\pi^3/V$. Including spin degeneracy ($g_s = 2$):
\\[
N = 2 \\times \\frac{\\frac{4}{3}\\pi k_F^3}{(2\\pi/L)^3} = \\frac{V k_F^3}{3\\pi^2} \\implies k_F = (3\\pi^2 n)^{1/3}
\\]
where $n = N/V$ is the conduction electron number density.
The Fermi energy is:
\\[
E_F = \\frac{\\hbar^2 k_F^2}{2m} = \\frac{\\hbar^2}{2m} (3\\pi^2 n)^{2/3}
\\]
The three-dimensional **Density of States (DOS)** $g(E)$, defined such that $g(E)dE$ is the number of electron states per unit volume between $E$ and $E+dE$, is derived from $n(E) = \\frac{1}{3\\pi^2}\\left(\\frac{2mE}{\\hbar^2}\\right)^{3/2}$:
\\[
g(E) = \\frac{dn}{dE} = \\frac{1}{2\\pi^2} \\left(\\frac{2m}{\\hbar^2}\\right)^{3/2} E^{1/2} = \\frac{3}{2} \\frac{n}{E_F} \\left(\\frac{E}{E_F}\\right)^{1/2}
\\]

### Fermi-Dirac Distribution Function
At non-zero temperature ($T > 0\\text{ K}$), the thermal occupation probability of an orbital at energy $E$ is dictated by the Fermi-Dirac distribution:
\\[
f(E, T) = \\frac{1}{e^{(E - \\mu)/k_B T} + 1}
\\]
where $\\mu$ is the chemical potential (which satisfies $\\mu(0) = E_F$ and $\\mu(T) \\approx E_F [1 - \\frac{\\pi^2}{12}(k_B T/E_F)^2]$). Only electrons within an energy window of approximately $\\sim k_B T$ around $E_F$ participate in thermal conduction, electrical transport, and Pauli paramagnetism."""
            },
            {
                "secNumber": "7.2",
                "title": "Periodic Potentials, Bloch's Theorem & The First Brillouin Zone",
                "content": r"""The Sommerfeld model fails to explain why some materials are insulators or semiconductors, why Hall coefficients are sometimes positive, and why electrons can travel thousands of atomic spacings without scattering. The resolution lies in the periodic crystal potential $V(\\mathbf{r} + \\mathbf{R}) = V(\\mathbf{r})$, where $\\mathbf{R}$ is any direct lattice translation vector.

### Bloch's Theorem
Felix Bloch (1928) proved that the stationary wavefunctions of a single electron moving in a spatially periodic potential take the form of a plane wave modulated by a function having the periodicity of the Bravais lattice:
\\[
\\psi_{\\mathbf{k}}(\\mathbf{r}) = e^{i \\mathbf{k} \\cdot \\mathbf{r}} u_{\\mathbf{k}}(\\mathbf{r})
\\]
where the periodic Bloch function $u_{\\mathbf{k}}(\\mathbf{r})$ satisfies:
\\[
u_{\\mathbf{k}}(\\mathbf{r} + \\mathbf{R}) = u_{\\mathbf{k}}(\\mathbf{r}) \\quad \\forall \\mathbf{R} \\in \\text{Lattice}
\\]
An equivalent formulation of Bloch's theorem is the phase-shift relation:
\\[
\\psi_{\\mathbf{k}}(\\mathbf{r} + \\mathbf{R}) = e^{i \\mathbf{k} \\cdot \\mathbf{R}} \\psi_{\\mathbf{k}}(\\mathbf{r})
\\]

### Physical Implications of Bloch's Theorem
1. **Crystal Momentum $\\hbar\\mathbf{k}$**: The wavevector $\\mathbf{k}$ is not the true physical momentum (the electron experiences forces from the lattice), but a quantum number called **crystal momentum**.
2. **Translation Operator Invariance**: If $\\mathbf{G}$ is any reciprocal lattice vector, $e^{i \\mathbf{G} \\cdot \\mathbf{R}} = 1$. Consequently, wavevectors differing by $\\mathbf{G}$ are physically identical:
\\[
\\psi_{\\mathbf{k} + \\mathbf{G}}(\\mathbf{r}) = \\psi_{\\mathbf{k}}(\\mathbf{r}), \\quad E_n(\\mathbf{k} + \\mathbf{G}) = E_n(\\mathbf{k})
\\]
3. **The First Brillouin Zone (1BZ)**:
   Because $E(\\mathbf{k})$ is strictly periodic in reciprocal space, all unique energy eigenvalues are completely contained within the **First Brillouin Zone**, defined as the Wigner-Seitz primitive cell of the reciprocal lattice centered at $\\mathbf{k} = \\mathbf{0}$ ($\Gamma$ point). High-symmetry points inside the 1BZ (such as $\\Gamma, X, L, K$ in FCC or $\\Gamma, H, P, N$ in BCC) define the band dispersion curves."""
            },
            {
                "secNumber": "7.3",
                "title": "The Nearly Free Electron Model & Opening of Energy Band Gaps",
                "content": r"""To understand how energy band gaps arise at zone boundaries, consider a weak periodic perturbation potential acting on free electrons:
\\[
V(x) = 2 V_1 \\cos\\left(\\frac{2\\pi x}{a}\\right) = V_1 \\left( e^{i G x} + e^{-i G x} \right)
\\]
where $G = 2\\pi/a$ is the shortest 1D reciprocal lattice vector.

### Bragg Reflection & Standing Waves at Zone Boundaries
For electron wavevectors far from the zone boundary ($k \\ll \\pi/a$), the perturbation has negligible effect, and $E(k) \\approx \\hbar^2 k^2 / 2m$.
However, as $k$ approaches the first Brillouin zone boundary:
\\[
k = \\pm \\frac{G}{2} = \\pm \\frac{\\pi}{a}
\\]
the electron satisfies the Bragg condition for diffraction:
\\[
2 d \\sin\\theta = \\lambda \\implies 2 a (1) = \\frac{2\\pi}{k} \\implies k = \\frac{\\pi}{a}
\\]
At this boundary, the forward-propagating plane wave $e^{i \\pi x/a}$ and the backscattered wave $e^{-i \\pi x/a}$ interfere coherently, forming two stationary standing waves:
\\[
\\psi_+(x) = \\frac{1}{\\sqrt{2}} (e^{i \\pi x/a} + e^{-i \\pi x/a}) = \\sqrt{2} \\cos\\left(\\frac{\\pi x}{a}\\right)
\\]
\\[
\\psi_-(x) = \\frac{1}{i\\sqrt{2}} (e^{i \\pi x/a} - e^{-i \\pi x/a}) = \\sqrt{2} \\sin\\left(\\frac{\\pi x}{a}\\right)
\\]

### Energy Splitting and the Band Gap $E_g$
The probability densities of these two standing waves are:
- $\\rho_+(x) = |\\psi_+(x)|^2 = 2 \\cos^2(\\pi x / a) = 1 + \\cos(2\\pi x / a)$
- $\\rho_-(x) = |\\psi_-(x)|^2 = 2 \\sin^2(\\pi x / a) = 1 - \\cos(2\\pi x / a)$

For attractive atomic potentials, the potential energy $V(x)$ has negative minima located at the atomic cores ($x = 0, \\pm a, \\dots$):
- $\\psi_+$ piles up electron charge directly onto the positively charged atomic nuclei ($x = 0$), lowering its electrostatic energy:
\\[
E_+ = E_0 + \\langle \\psi_+ | V(x) | \\psi_+ \\rangle = E_0 - |V_1|
\\]
- $\\psi_-$ concentrates electron charge between the nuclei ($x = \\pm a/2$), raising its electrostatic energy:
\\[
E_- = E_0 + \\langle \\psi_- | V(x) | \\psi_- \\rangle = E_0 + |V_1|
\\]
This creates an energy discontinuity—the **fundamental band gap** $E_g$—at the Brillouin zone boundary:
\\[
E_g = E_- - E_+ = 2 |V_1|
\\]
No traveling electron waves can propagate through the crystal with energies inside this forbidden interval."""
            },
            {
                "secNumber": "7.4",
                "title": "The Kronig-Penney Model: Analytical Dispersion Relation & Band Solutions",
                "content": r"""Ralph Kronig and William Penney (1931) introduced an analytically solvable 1D model that demonstrates how periodic square potential wells naturally generate continuous energy bands and discrete forbidden band gaps.

### Formulation of the 1D Kronig-Penney Potential
The periodic potential consists of a regular array of square barriers of height $V_0$ and width $b$, separated by wells of width $a$ (lattice period $d = a + b$):
\\[
V(x) = \\begin{cases} 0 & 0 < x < a \\\\ V_0 & -b < x < 0 \\end{cases}, \\quad V(x + d) = V(x)
\\]
For energies $0 < E < V_0$, the Schrödinger solutions in the two regions are:
- Region 1 ($0 < x < a$, $V = 0$):
  \\[
  \\psi_1(x) = A e^{i \\alpha x} + B e^{-i \\alpha x}, \\quad \\alpha = \\frac{\\sqrt{2mE}}{\\hbar}
  \\]
- Region 2 ($-b < x < 0$, $V = V_0$):
  \\[
  \\psi_2(x) = C e^{\\beta x} + D e^{-\\beta x}, \\quad \\beta = \\frac{\\sqrt{2m(V_0 - E)}}{\\hbar}
  \\]
Applying Bloch's theorem $\\psi(x + d) = e^{i k d} \\psi(x)$ along with wavefunction and derivative continuity boundary conditions at $x = 0$ and $x = a$ generates a $4 \\times 4$ secular determinant for coefficients $A, B, C, D$.

### The Dirac Delta Comb Limit
In the limiting case where the barrier width vanishes ($b \\to 0$) while barrier height approaches infinity ($V_0 \\to \\infty$) such that the barrier strength $P = \\lim \\frac{m V_0 b a}{\\hbar^2}$ remains finite, the secular determinant reduces to the celebrated **Kronig-Penney dispersion relation**:
\\[
P \\frac{\\sin(\\alpha a)}{\\alpha a} + \\cos(\\alpha a) = \\cos(k a)
\\]
where:
- $\\alpha = \\sqrt{2mE}/\\hbar$
- $P$ is the dimensionless barrier strength parameter
- $k$ is the electron Bloch wavevector in the 1BZ ($-\\pi/a \\le k \\le +\\pi/a$).

### Physical Interpretation of Kronig-Penney Solutions
Because the right-hand side is strictly bounded by $[-1, +1]$:
\\[
-1 \\le P \\frac{\\sin(\\alpha a)}{\\alpha a} + \\cos(\\alpha a) \\le +1
\\]
- **Allowed Energy Bands**: Values of $\\alpha a$ (and therefore energy $E = \\hbar^2 \\alpha^2 / 2m$) for which the left-hand function lies between $-1$ and $+1$ yield real wavevectors $k$, forming continuous bands.
- **Forbidden Band Gaps**: Regions where $\\left|P \\frac{\\sin(\\alpha a)}{\\alpha a} + \\cos(\\alpha a)\\right| > 1$ require complex $k$, corresponding to decaying evanescent waves that cannot propagate through the lattice.
- **Limits**:
  - As $P \\to 0$ (free electrons): $\\cos(\\alpha a) = \\cos(ka) \\implies \\alpha = k \\implies E = \\hbar^2 k^2 / 2m$ (single continuous parabolic band).
  - As $P \\to \\infty$ (infinitely bound isolated atoms): $\\sin(\\alpha a) = 0 \\implies \\alpha a = n\\pi \\implies E_n = \\frac{n^2 \\pi^2 \\hbar^2}{2m a^2}$ (discrete bound states)."""
            },
            {
                "secNumber": "7.5",
                "title": "Tight-Binding Approximation (LCAO): 1D Chain, Bandwidth & Transfer Integrals",
                "content": r"""While the nearly free electron model begins from free electrons slightly perturbed by a lattice, the **tight-binding approximation** (Linear Combination of Atomic Orbitals, LCAO) approaches the solid from the opposite limit: isolated atomic orbitals perturbed by neighboring atoms.

### Mathematical Formulation
Let $\\phi_m(\\mathbf{r} - \\mathbf{R}_n)$ be an atomic orbital centered at lattice site $\\mathbf{R}_n$. The Bloch-adapted crystal wavefunction is:
\\[
\\psi_{\\mathbf{k}}(\\mathbf{r}) = \\frac{1}{\\sqrt{N}} \\sum_{n=1}^{N} e^{i \\mathbf{k} \\cdot \\mathbf{R}_n} \\phi(\\mathbf{r} - \\mathbf{R}_n)
\\]
The expectation value of the crystal Hamiltonian $\\hat{H} = -\\frac{\\hbar^2}{2m}\\nabla^2 + V_{\\text{crystal}}(\\mathbf{r})$ is:
\\[
E(\\mathbf{k}) = \\frac{\\langle \\psi_{\\mathbf{k}} | \\hat{H} | \\psi_{\\mathbf{k}} \\rangle}{\\langle \\psi_{\\mathbf{k}} | \\psi_{\\mathbf{k}} \\rangle}
\\]
Assuming orthogonalized Wannier/atomic orbitals ($\\langle \\phi(\\mathbf{r} - \\mathbf{R}_n) | \\phi(\\mathbf{r} - \\mathbf{R}_{n'}) \\rangle = \\delta_{n,n'}$):
\\[
E(\\mathbf{k}) = \\frac{1}{N} \\sum_{n, n'} e^{i \\mathbf{k} \\cdot (\\mathbf{R}_{n'} - \\mathbf{R}_n)} \\int \\phi^*(\\mathbf{r} - \\mathbf{R}_n) \\hat{H} \\phi(\\mathbf{r} - \\mathbf{R}_{n'}) d^3\\mathbf{r}
\\]

### Derivation for a 1D Monatomic Chain
Consider a 1D chain with lattice constant $a$. Retaining only on-site and nearest-neighbor interactions:
- **On-site Coulomb integral** ($\alpha$ or $\\varepsilon_0$):
  \\[
  \\varepsilon_0 = \\int \\phi^*(x) \\hat{H} \\phi(x) dx
  \\]
- **Nearest-neighbor transfer integral (hopping parameter)** ($-t$ or $-\\beta$):
  \\[
  -t = \\int \\phi^*(x) \\hat{H} \\phi(x \\pm a) dx
  \\]
The energy dispersion reduces to:
\\[
E(k) = \\varepsilon_0 - t e^{i k a} - t e^{-i k a} = \\varepsilon_0 - 2t \\cos(ka)
\\]
where $-\\pi/a \\le k \\le +\\pi/a$.

### Band Properties: Bandwidth and Effective Mass
1. **Total Bandwidth $W$**:
   - Minimum energy: at $k = 0$, $E_{\\min} = \\varepsilon_0 - 2t$.
   - Maximum energy: at $k = \\pm \\pi/a$, $E_{\\max} = \\varepsilon_0 + 2t$.
   \\[
   W = E_{\\max} - E_{\\min} = 4t
   \\]
   The bandwidth is directly proportional to the hopping integral $t$: stronger orbital overlap broadens the band.
2. **Effective Mass $m^*$**:
   Expanding $E(k)$ near the band bottom ($k \\approx 0$):
   \\[
   E(k) \\approx \\varepsilon_0 - 2t \\left(1 - \\frac{k^2 a^2}{2}\\right) = (\\varepsilon_0 - 2t) + t a^2 k^2
   \\]
   Comparing with $E(k) = E_{\\min} + \\frac{\\hbar^2 k^2}{2m^*}$:
   \\[
   \\frac{1}{m^*} = \\frac{1}{\\hbar^2} \\frac{d^2E}{dk^2} = \\frac{2t a^2}{\\hbar^2} \\implies m^* = \\frac{\\hbar^2}{2t a^2}
   \\]
   Stronger orbital overlap (larger $t$) results in lighter, more mobile charge carriers."""
            },
            {
                "secNumber": "7.6",
                "title": "Conductors, Semiconductors & Insulators: Band Filling & Fermi Level",
                "content": r"""The fundamental distinction between electrical conductors, semiconductors, and insulators is determined by the degree of band filling and the magnitude of the band gap at the Fermi energy $E_F$.

### Classification by Electronic Band Topology
1. **Metals (Conductors)**:
   - Possess a **partially filled band** at $T = 0\\text{ K}$ (e.g., monovalent alkali metals $\\text{Na}, \\text{Cu}$ where the valence $s$-band is half-filled).
   - Alternatively, exhibit **band overlap** where the top of a filled valence band lies higher in energy than the bottom of an empty conduction band (e.g., divalent alkaline earths $\\text{Mg}, \\text{Ca}$ with overlapping $s$- and $p$-bands).
   - Because empty electronic states are infinitesimally close to occupied states ($g(E_F) > 0$), applying an infinitesimal electric field shifts electron momentum, generating high electrical conductivity ($\\sigma \\sim 10^7\\text{ S/m}$) that decreases with temperature ($d\\sigma/dT < 0$) due to phonon scattering.

2. **Insulators**:
   - Possess a completely filled **valence band** separated from an entirely empty **conduction band** by a large forbidden band gap:
   \\[
   E_g > 4.0\\text{ eV}
   \\]
   - Examples: Diamond ($E_g = 5.47\\text{ eV}$), quartz $\\text{SiO}_2$ ($E_g = 9.0\\text{ eV}$), sapphire $\\text{Al}_2\\text{O}_3$ ($E_g = 8.8\\text{ eV}$).
   - Thermal excitation across $E_g$ at room temperature is negligible ($k_B T \\approx 0.0259\\text{ eV} \\ll E_g$). Electrical conductivity is practically zero ($\sigma < 10^{-12}\\text{ S/m}$).

3. **Semiconductors**:
   - Possess the same electronic topology as insulators (completely filled valence band at $0\\text{ K}$), but with a **moderate band gap**:
   \\[
   0.1\\text{ eV} < E_g < 3.5\\text{ eV}
   \\]
   - Examples: $\\text{Ge}$ ($0.66\\text{ eV}$), $\\text{Si}$ ($1.12\\text{ eV}$), $\\text{GaAs}$ ($1.42\\text{ eV}$), $\\text{GaN}$ ($3.44\\text{ eV}$).
   - Significant thermal promotion of electrons into the conduction band occurs at ambient temperatures, yielding measurable conductivity ($\\sigma \\sim 10^{-4} - 10^2\\text{ S/m}$) that increases exponentially with temperature ($d\\sigma/dT > 0$).

4. **Semimetals**:
   - Possess a very small overlap between valence and conduction bands, or point touching at Dirac points with zero density of states at $E_F$ (e.g., bismuth $\\text{Bi}$, graphite, and graphene)."""
            },
            {
                "secNumber": "7.7",
                "title": "Intrinsic Semiconductors: Carrier Statistics, Effective Mass & Chemical Potential",
                "content": r"""In a pure, undoped intrinsic semiconductor, thermal excitation generates equal concentrations of conduction-band electrons ($n$) and valence-band holes ($p$):
\\[
n = p = n_i
\\]

### Effective Density of States
Near the extrema of isotropic parabolic bands:
- Conduction band bottom ($E_c$): $E(k) = E_c + \\frac{\\hbar^2 k^2}{2m_e^*}$.
- Valence band top ($E_v$): $E(k) = E_v - \\frac{\\hbar^2 k^2}{2m_h^*}$.
The density of states in the conduction and valence bands are:
\\[
g_c(E) = \\frac{1}{2\\pi^2} \\left(\\frac{2m_e^*}{\\hbar^2}\\right)^{3/2} \\sqrt{E - E_c}, \\quad g_v(E) = \\frac{1}{2\\pi^2} \\left(\\frac{2m_h^*}{\\hbar^2}\\right)^{3/2} \\sqrt{E_v - E}
\\]
Integrating the Maxwell-Boltzmann approximation of the Fermi-Dirac distribution:
\\[
n = \\int_{E_c}^{\\infty} g_c(E) e^{-(E - E_F)/k_B T} dE = N_c \\exp\\left(-\\frac{E_c - E_F}{k_B T}\\right)
\\]
\\[
p = \\int_{-\\infty}^{E_v} g_v(E) e^{-(E_F - E)/k_B T} dE = N_v \\exp\\left(-\\frac{E_F - E_v}{k_B T}\\right)
\\]
where $N_c$ and $N_v$ are the **effective density of states**:
\\[
N_c = 2 \\left( \\frac{2\\pi m_e^* k_B T}{h^2} \\right)^{3/2}, \\quad N_v = 2 \\left( \\frac{2\\pi m_h^* k_B T}{h^2} \\right)^{3/2}
\\]

### The Law of Mass Action & Intrinsic Carrier Concentration
The product $np$ is strictly independent of the Fermi level $E_F$:
\\[
np = n_i^2 = N_c N_v \\exp\\left(-\\frac{E_c - E_v}{k_B T}\\right) = N_c N_v \\exp\\left(-\\frac{E_g}{k_B T}\\right)
\\]
\\[
n_i = \\sqrt{N_c N_v} \\exp\\left(-\\frac{E_g}{2k_B T}\\right)
\\]
The carrier concentration exhibits an Arrhenius temperature dependence with effective activation energy equal to half the band gap ($E_g/2$).

### The Intrinsic Fermi Level ($E_i$)
Equating $n = p$ and solving for the Fermi level:
\\[
N_c e^{-(E_c - E_i)/k_B T} = N_v e^{-(E_i - E_v)/k_B T}
\\]
\\[
E_i = \\frac{E_c + E_v}{2} + \\frac{3}{4} k_B T \\ln\\left( \\frac{m_h^*}{m_e^*} \\right)
\\]
At $T = 0\\text{ K}$, the intrinsic Fermi level lies exactly at the center of the band gap ($E_g/2$). As temperature increases, if $m_h^* > m_e^*$, $E_i$ shifts slightly upward toward the conduction band to maintain carrier equality."""
            },
            {
                "secNumber": "7.8",
                "title": "Controlled Valence and Doped Semiconductors: Donor/Acceptor Regimes",
                "content": r"""The electrical conductivity of semiconductors and transition metal oxides can be tuned over ten orders of magnitude through the controlled introduction of chemical impurities (**doping** and **controlled valency**).

### Extrinsic Semiconductors: Donors and Acceptors
1. **$n$-type Semiconductors**:
   - Formed by substituting host atoms (e.g., tetravalent $\\text{Si}$) with pentavalent donors (e.g., $\\text{P}, \\text{As}, \\text{Sb}$).
   - The fifth valence electron is loosely bound in a hydrogen-like orbit below the conduction band edge with binding energy:
   \\[
   E_d = \\frac{m_e^*}{m_0} \\frac{1}{\\varepsilon_r^2} E_H \\approx 10 - 50\\text{ meV}
   \\]
   Because $E_d \\sim k_B T$, all donors are ionized at room temperature, making $n \\approx N_d^+$.
2. **$p$-type Semiconductors**:
   - Formed by trivalent acceptors (e.g., $\\text{B}, \\text{Al}, \\text{Ga}$). Accepts an electron from the valence band, generating a hole with shallow binding energy $E_a \\approx 10 - 50\\text{ meV}$.

### Temperature Regimes of Extrinsic Carriers
As temperature increases, carrier concentration passes through three regimes:
1. **Freeze-out Regime** ($T < 100\\text{ K}$): Thermal energy is insufficient to ionize dopants; carriers remain trapped ($n \\propto e^{-E_d/2k_B T}$).
2. **Extrinsic (Saturation/Exhaustion) Regime** ($100\\text{ K} < T < 500\\text{ K}$): All dopants are fully ionized ($n = N_d = \\text{constant}$).
3. **Intrinsic Regime** ($T > 600\\text{ K}$): Thermally generated intrinsic carriers swamp the dopant concentration ($n_i \\gg N_d$), and $n(T)$ resumes exponential $e^{-E_g/2k_B T}$ growth.

### Principle of Controlled Valency (Verwey Principle)
In transition metal oxides, stoichiometric monoxides (such as pure $\\text{NiO}$) are insulating antiferromagnetic Mott insulators ($d^8$). Evert Verwey (1950) demonstrated that substituting monovalent $\\text{Li}^+$ for divalent $\\text{Ni}^{2+}$ forces an equivalent number of neighboring nickel cations to oxidize from $\\text{Ni}^{2+}$ to $\\text{Ni}^{3+}$ to maintain charge neutrality:
\\[
\\text{Li}_x\\text{Ni}_{1-x}\\text{O} = \\text{Li}_x^+ \\text{Ni}_{1-2x}^{2+} \\text{Ni}_x^{3+} \\text{O}^{2-}
\\]
Conduction occurs via small-polaron hopping of electrons between adjacent $\\text{Ni}^{2+}$ and $\\text{Ni}^{3+}$ centers with activation energy $E_h$:
\\[
\\sigma(T) = \\frac{\\sigma_0}{T} \\exp\\left(-\\frac{E_h}{k_B T}\\right)
\\]
This transform pure insulating $\\text{NiO}$ ($\\sigma < 10^{-13}\\text{ S/cm}$) into a $p$-type semiconductor with $\\sigma > 1\\text{ S/cm}$."""
            }
        ],
        "problems": [
            {
                "probNumber": "7.1",
                "title": "Fermi Energy, Fermi Velocity, and Density of States in Copper",
                "difficulty": "Foundational",
                "statement": "Metallic copper (FCC, $a = 3.615\\text{ Å}$) has one conduction electron per atom ($Z = 1$).\\n(a) Calculate the conduction electron number density $n$ in $\\text{m}^{-3}$.\\n(b) Compute the Fermi wavevector $k_F$, Fermi energy $E_F$ (in $\\text{eV}$), and Fermi velocity $v_F$.\\n(c) Calculate the Density of States at the Fermi energy $g(E_F)$ per unit volume in $\\text{J}^{-1}\\text{m}^{-3}$ and in $\\text{eV}^{-1}\\text{cm}^{-3}$.",
                "solution": r"""### Step 1: Conduction Electron Density
Copper has an FCC crystal structure with $4$ atoms per unit cell. Since each copper atom contributes $1$ conduction electron, $N_{\\text{cell}} = 4$ electrons.
Unit cell volume:
\\[
V_c = a^3 = (3.615 \\times 10^{-10}\\text{ m})^3 = 4.7243 \\times 10^{-29}\\text{ m}^3
\\]
Electron number density:
\\[
n = \\frac{4}{4.7243 \\times 10^{-29}\\text{ m}^3} = 8.4668 \\times 10^{28}\\text{ m}^{-3}
\\]

### Step 2: Fermi Parameters
1. **Fermi wavevector $k_F$**:
\\[
k_F = (3\\pi^2 n)^{1/3} = (3\\pi^2 \\times 8.4668 \\times 10^{28})^{1/3} = (2.5072 \\times 10^{30})^{1/3} = 1.3585 \\times 10^{10}\\text{ m}^{-1} = 1.359\\text{ Å}^{-1}
\\]

2. **Fermi energy $E_F$**:
\\[
E_F = \\frac{\\hbar^2 k_F^2}{2m_e} = \\frac{(1.05457 \\times 10^{-34}\\text{ J}\\cdot\\text{s})^2 (1.3585 \\times 10^{10}\\text{ m}^{-1})^2}{2(9.10938 \\times 10^{-31}\\text{ kg})}
\\]
\\[
E_F = \\frac{(1.11212 \\times 10^{-68})(1.8455 \\times 10^{20})}{1.82188 \\times 10^{-30}} = \\frac{2.0524 \\times 10^{-48}}{1.82188 \\times 10^{-30}} = 1.1265 \\times 10^{-18}\\text{ J}
\\]
Converting to $\\text{eV}$:
\\[
E_F = \\frac{1.1265 \\times 10^{-18}\\text{ J}}{1.60218 \\times 10^{-19}\\text{ J/eV}} = 7.031\\text{ eV}
\\]

3. **Fermi velocity $v_F$**:
\\[
v_F = \\frac{\\hbar k_F}{m_e} = \\frac{(1.05457 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(1.3585 \\times 10^{10}\\text{ m}^{-1})}{9.10938 \\times 10^{-31}\\text{ kg}} = 1.573 \\times 10^6\\text{ m/s}
\\]
(Approximately $0.5\\%$ of the speed of light!).

### Step 3: Density of States at $E_F$
Using the relationship $g(E_F) = \\frac{3}{2} \\frac{n}{E_F}$:
\\[
g(E_F) = \\frac{3}{2} \\frac{8.4668 \\times 10^{28}\\text{ m}^{-3}}{1.1265 \\times 10^{-18}\\text{ J}} = 1.1274 \\times 10^{47}\\text{ J}^{-1}\\text{m}^{-3}
\\]
Converting to $\\text{eV}^{-1}\\text{cm}^{-3}$:
\\[
g(E_F) = 1.1274 \\times 10^{47} \\times (1.60218 \\times 10^{-19}\\text{ J/eV}) \\times (10^{-6}\\text{ m}^3/\\text{cm}^3) = 1.806 \\times 10^{22}\\text{ eV}^{-1}\\text{cm}^{-3}
\\]"""
            },
            {
                "probNumber": "7.2",
                "title": "Analytical Derivation of the Kronig-Penney Dispersion Relation in the Delta Limit",
                "difficulty": "Advanced",
                "statement": "In the Kronig-Penney delta-comb potential $V(x) = \\frac{\\hbar^2 P}{m a} \\sum_{n=-\\infty}^{\\infty} \\delta(x - na)$:\\n(a) Integrate the 1D Schrödinger equation across the infinitesimal interval $[-\\varepsilon, +\\varepsilon]$ around $x = 0$ to derive the boundary condition for the derivative discontinuity $\\psi'(0^+) - \\psi'(0^-)$.\\n(b) Using the free-particle wavefunction $\\psi(x) = A e^{i \\alpha x} + B e^{-i \\alpha x}$ on $(0, a)$ and Bloch's condition $\\psi(x) = e^{i ka} \\psi(x - a)$, derive the transcendental dispersion relation:\\n\\[ P \\frac{\\sin(\\alpha a)}{\\alpha a} + \\cos(\\alpha a) = \\cos(ka) \\]\\n(c) For $P = 3\\pi/2$, compute whether the state $\\alpha a = \\pi$ is in an allowed band or a forbidden band gap.",
                "solution": r"""### Step 1: Derivative Discontinuity Boundary Condition
The Schrödinger equation is:
\\[
-\\frac{\\hbar^2}{2m} \\frac{d^2\\psi}{dx^2} + \\frac{\\hbar^2 P}{ma} \\delta(x) \\psi(x) = E \\psi(x)
\\]
Integrating from $-\\varepsilon$ to $+\\varepsilon$ and taking the limit $\\varepsilon \\to 0$:
\\[
-\\frac{\\hbar^2}{2m} \\int_{-\\varepsilon}^{+\\varepsilon} \\frac{d^2\\psi}{dx^2} dx + \\frac{\\hbar^2 P}{ma} \\int_{-\\varepsilon}^{+\\varepsilon} \\delta(x) \\psi(x) dx = E \\int_{-\\varepsilon}^{+\\varepsilon} \\psi(x) dx
\\]
\\[
-\\frac{\\hbar^2}{2m} \\left[ \\psi'(0^+) - \\psi'(0^-) \\right] + \\frac{\\hbar^2 P}{ma} \\psi(0) = 0
\\]
Multiplying by $-\\frac{2m}{\\hbar^2}$:
\\[
\\psi'(0^+) - \\psi'(0^-) = \\frac{2P}{a} \\psi(0)
\\]
Furthermore, the wavefunction itself is continuous: $\\psi(0^+) = \\psi(0^-) = \\psi(0)$.

### Step 2: Derivation of the Dispersion Relation
In the open interval $0 < x < a$, the potential is zero:
\\[
\\psi(x) = A \\sin(\\alpha x) + B \\cos(\\alpha x)
\\]
where $\\alpha = \\sqrt{2mE}/\\hbar$.
At $x = 0$: $\\psi(0^+) = B$, and $\\psi'(0^+) = \\alpha A$.
By Bloch's theorem, for the region just to the left of the origin ($-a < x < 0$):
\\[
\\psi(x) = e^{-ika} \\psi(x + a)
\\]
Thus:
\\[
\\psi(0^-) = e^{-ika} \\psi(a) = e^{-ika} [A \\sin(\\alpha a) + B \\cos(\\alpha a)]
\\]
\\[
\\psi'(0^-) = e^{-ika} \\psi'(a) = e^{-ika} \\alpha [A \\cos(\\alpha a) - B \\sin(\\alpha a)]
\\]
1. Continuity of $\\psi$:
\\[
B = e^{-ika} [A \\sin(\\alpha a) + B \\cos(\\alpha a)] \\implies B (e^{ika} - \\cos(\\alpha a)) = A \\sin(\\alpha a)
\\]
2. Derivative jump:
\\[
\\alpha A - e^{-ika} \\alpha [A \\cos(\\alpha a) - B \\sin(\\alpha a)] = \\frac{2P}{a} B
\\]
Multiply by $e^{ika}$:
\\[
\\alpha [A e^{ika} - A \\cos(\\alpha a) + B \\sin(\\alpha a)] = \\frac{2P}{a} B e^{ika}
\\]
Substitute $A \\sin(\\alpha a) = B (e^{ika} - \\cos(\\alpha a))$ into the determinant of the linear system:
Setting the secular determinant to zero yields:
\\[
\\cos(ka) = \\cos(\\alpha a) + \\frac{P}{\\alpha a} \\sin(\\alpha a)
\\]
This completes the exact analytical derivation.

### Step 3: Evaluation at $\\alpha a = \\pi$
Substitute $\\alpha a = \\pi$ and $P = \\frac{3\\pi}{2}$:
\\[
f(\\pi) = P \\frac{\\sin\\pi}{\\pi} + \\cos\\pi = P \\frac{0}{\\pi} + (-1) = -1.000
\\]
Since $f(\\pi) = -1 = \\cos(ka)$, this yields $\\cos(ka) = -1 \\implies ka = \\pm \\pi$.
This state lies precisely at the **Brillouin zone boundary** ($k = \\pi/a$).
Now evaluate slightly above $\\alpha a = \\pi$: let $\\alpha a = \\pi + \\delta$:
\\[
\\sin(\\pi + \\delta) \\approx -\\delta, \\quad \\cos(\\pi + \\delta) \\approx -1 + \\frac{\\delta^2}{2}
\\]
\\[
f(\\pi + \\delta) \\approx -1 - \\frac{P}{\\pi}\\delta < -1
\\]
Because $|f(\\pi + \\delta)| > 1$, all energies immediately above $\\alpha a = \\pi$ have $|f| > 1$, confirming the opening of an **unoccupied forbidden band gap** starting at the zone boundary!"""
            },
            {
                "probNumber": "7.3",
                "title": "Tight-Binding Band Dispersion, Bandwidth, and Effective Mass for a 1D Monatomic Chain",
                "difficulty": "Intermediate",
                "statement": "For a 1D chain of atoms with lattice constant $a = 3.00\\text{ Å}$, the tight-binding dispersion relation is $E(k) = \\varepsilon_0 - 2t \\cos(ka)$, where $\\varepsilon_0 = -8.50\\text{ eV}$ and nearest-neighbor hopping energy $t = 1.25\\text{ eV}$.\\n(a) Determine the total electronic bandwidth $W$ and the energies at the center ($k=0$) and edge ($k=\\pi/a$) of the Brillouin zone.\\n(b) Formulate the analytical expression for the effective mass $m^*(k)$ and evaluate $m^*$ at $k = 0$, $k = \\pi/(2a)$, and $k = \\pi/a$ in units of the free electron rest mass $m_0$.\\n(c) Calculate the group velocity $v_g(k)$ at $k = \\pi/(2a)$.",
                "solution": r"""### Step 1: Bandwidth and Band Extrema
The dispersion relation is:
\\[
E(k) = -8.50\\text{ eV} - 2(1.25\\text{ eV}) \\cos(ka) = -8.50 - 2.50 \\cos(ka) \\text{ eV}
\\]
1. **At $k = 0$ (zone center $\\Gamma$)**:
\\[
\\cos(0) = 1 \\implies E(0) = -8.50 - 2.50(1) = -11.00\\text{ eV} \\quad (\\text{band minimum})
\\]
2. **At $k = \\pi/a$ (zone boundary $X$)**:
\\[
\\cos(\\pi) = -1 \\implies E(\\pi/a) = -8.50 - 2.50(-1) = -6.00\\text{ eV} \\quad (\\text{band maximum})
\\]
3. **Total Bandwidth**:
\\[
W = E_{\\max} - E_{\\min} = -6.00 - (-11.00) = 5.00\\text{ eV} = 4t
\\]

### Step 2: Effective Mass Analysis
The effective mass is given by:
\\[
\\frac{1}{m^*(k)} = \\frac{1}{\\hbar^2} \\frac{d^2E}{dk^2}
\\]
Differentiating $E(k)$:
\\[
\\frac{dE}{dk} = 2t a \\sin(ka)
\\]
\\[
\\frac{d^2E}{dk^2} = 2t a^2 \\cos(ka)
\\]
Thus:
\\[
m^*(k) = \\frac{\\hbar^2}{2t a^2 \\cos(ka)}
\\]
Evaluate the prefactor:
\\[
t = 1.25\\text{ eV} = 1.25 \\times 1.60218 \\times 10^{-19}\\text{ J} = 2.0027 \\times 10^{-19}\\text{ J}
\\]
\\[
a = 3.00 \\times 10^{-10}\\text{ m} \\implies a^2 = 9.00 \\times 10^{-20}\\text{ m}^2
\\]
\\[
2t a^2 = 2(2.0027 \\times 10^{-19})(9.00 \\times 10^{-20}) = 3.6049 \\times 10^{-38}\\text{ J}\\cdot\\text{m}^2
\\]
\\[
m^*(0) = \\frac{\\hbar^2}{2t a^2} = \\frac{(1.05457 \\times 10^{-34})^2}{3.6049 \\times 10^{-38}} = \\frac{1.11212 \\times 10^{-68}}{3.6049 \\times 10^{-38}} = 3.085 \\times 10^{-31}\\text{ kg}
\\]
Ratio to free electron mass:
\\[
\\frac{m^*(0)}{m_0} = \\frac{3.085 \\times 10^{-31}\\text{ kg}}{9.10938 \\times 10^{-31}\\text{ kg}} = +0.3387 \\approx +0.339
\\]
- **At $k = 0$**: $m^* = +0.339 m_0$ (positive, electron-like).
- **At $k = \\pi/(2a)$**: $\\cos(\\pi/2) = 0 \\implies m^* \\to \\infty$ (inflection point, zero curvature).
- **At $k = \\pi/a$**: $\\cos(\\pi) = -1 \\implies m^* = -0.339 m_0$ (negative, hole-like behavior near the top of the band).

### Step 3: Group Velocity at $k = \\pi/(2a)$
The group velocity is:
\\[
v_g(k) = \\frac{1}{\\hbar} \\frac{dE}{dk} = \\frac{2t a}{\\hbar} \\sin(ka)
\\]
At $k = \\pi/(2a)$, $\\sin(\\pi/2) = 1$:
\\[
v_g\\left(\\frac{\\pi}{2a}\\right) = \\frac{2(2.0027 \\times 10^{-19}\\text{ J})(3.00 \\times 10^{-10}\\text{ m})}{1.05457 \\times 10^{-34}\\text{ J}\\cdot\\text{s}} = \\frac{1.2016 \\times 10^{-28}}{1.05457 \\times 10^{-34}} = 1.139 \\times 10^6\\text{ m/s}
\\]"""
            },
            {
                "probNumber": "7.4",
                "title": "Intrinsic Carrier Concentration and Fermi Level in Silicon",
                "difficulty": "Intermediate",
                "statement": "Silicon has an indirect bandgap of $E_g = 1.12\\text{ eV}$ at $T = 300\\text{ K}$. The effective masses of electrons and holes are $m_e^* = 1.08 m_0$ and $m_h^* = 0.56 m_0$.\\n(a) Compute the effective density of states $N_c$ and $N_v$ in $\\text{cm}^{-3}$ at $300\\text{ K}$.\\n(b) Calculate the intrinsic carrier concentration $n_i$ at $300\\text{ K}$.\\n(c) Calculate the shift of the intrinsic Fermi level $E_i$ relative to the midgap energy $(E_c + E_v)/2$ in $\\text{meV}$.",
                "solution": r"""### Step 1: Effective Density of States
The formula for effective density of states is:
\\[
N_c = 2 \\left( \\frac{2\\pi m_e^* k_B T}{h^2} \\right)^{3/2} = 2.5094 \\times 10^{19} \\left(\\frac{m_e^*}{m_0}\\right)^{3/2} \\left(\\frac{T}{300}\\right)^{3/2} \\text{ cm}^{-3}
\\]
Given $T = 300\\text{ K}$:
1. **For $N_c$** ($m_e^* = 1.08 m_0$):
\\[
(1.08)^{3/2} = 1.1224
\\]
\\[
N_c = 2.5094 \\times 10^{19} \\times 1.1224 = 2.817 \\times 10^{19}\\text{ cm}^{-3}
\\]
2. **For $N_v$** ($m_h^* = 0.56 m_0$):
\\[
(0.56)^{3/2} = 0.4191
\\]
\\[
N_v = 2.5094 \\times 10^{19} \\times 0.4191 = 1.052 \\times 10^{19}\\text{ cm}^{-3}
\\]

### Step 2: Intrinsic Carrier Concentration
Thermal energy at $300\\text{ K}$:
\\[
k_B T = 0.025852\\text{ eV}
\\]
The intrinsic concentration is:
\\[
n_i = \\sqrt{N_c N_v} \\exp\\left(-\\frac{E_g}{2 k_B T}\\right)
\\]
\\[
\\sqrt{N_c N_v} = \\sqrt{(2.817 \\times 10^{19})(1.052 \\times 10^{19})} = \\sqrt{2.9635 \\times 10^{38}} = 1.7215 \\times 10^{19}\\text{ cm}^{-3}
\\]
Exponent factor:
\\[
\\frac{E_g}{2 k_B T} = \\frac{1.12\\text{ eV}}{2(0.025852\\text{ eV})} = \\frac{1.12}{0.051704} = 21.6618
\\]
\\[
\\exp(-21.6618) = 3.9026 \\times 10^{-10}
\\]
Intrinsic concentration:
\\[
n_i = (1.7215 \\times 10^{19}\\text{ cm}^{-3})(3.9026 \\times 10^{-10}) = 6.72 \\times 10^9\\text{ cm}^{-3}
\\]
(Experimental benchmark: $n_i \\approx 1.0 \\times 10^{10}\\text{ cm}^{-3}$, in excellent agreement).

### Step 3: Fermi Level Shift from Midgap
The intrinsic Fermi level is given by:
\\[
E_i - E_{\\text{midgap}} = \\frac{3}{4} k_B T \\ln\\left( \\frac{m_h^*}{m_e^*} \\right)
\\]
Substitute the values:
\\[
\\frac{m_h^*}{m_e^*} = \\frac{0.56}{1.08} = 0.5185
\\]
\\[
\\ln(0.5185) = -0.6568
\\]
\\[
E_i - E_{\\text{midgap}} = \\frac{3}{4}(25.852\\text{ meV})(-0.6568) = (19.389\\text{ meV})(-0.6568) = -12.73\\text{ meV}
\\]
The Fermi level lies $12.7\\text{ meV}$ below the exact center of the bandgap because the effective mass of electrons exceeds that of holes."""
            },
            {
                "probNumber": "7.5",
                "title": "Extrinsic Carrier Concentration and Ionization Fraction of Phosphorus-Doped Silicon",
                "difficulty": "Intermediate",
                "statement": "A silicon wafer is uniformly doped with phosphorus at donor density $N_d = 2.0 \\times 10^{16}\\text{ cm}^{-3}$ with donor ionization energy $E_c - E_d = 45\\text{ meV}$.\\n(a) At $T = 300\\text{ K}$, show that the semiconductor is in the complete ionization regime and compute electron density $n$, hole density $p$, and Fermi level position $E_c - E_F$ (use $N_c = 2.8 \\times 10^{19}\\text{ cm}^{-3}$ and $n_i = 1.0 \\times 10^{10}\\text{ cm}^{-3}$).\\n(b) At low temperature $T = 77\\text{ K}$ (liquid nitrogen), compute $k_B T$, $N_c(77\\text{ K})$, and determine the fraction of ionized donors $N_d^+/N_d$ in the freeze-out regime.",
                "solution": r"""### Step 1: Room Temperature ($300\\text{ K}$) Extrinsic State
At $300\\text{ K}$, $k_B T = 25.85\\text{ meV}$, which is comparable to $E_d = 45\\text{ meV}$. Because $N_c \\gg N_d$, entropy drives full ionization:
\\[
n \\approx N_d = 2.0 \\times 10^{16}\\text{ cm}^{-3}
\\]
By the law of mass action ($np = n_i^2$):
\\[
p = \\frac{n_i^2}{n} = \\frac{(1.0 \\times 10^{10}\\text{ cm}^{-3})^2}{2.0 \\times 10^{16}\\text{ cm}^{-3}} = 5.0 \\times 10^3\\text{ cm}^{-3}
\\]
The electron density exceeds hole density by a factor of $4 \\times 10^{12}$!
The Fermi level position:
\\[
n = N_c \\exp\\left(-\\frac{E_c - E_F}{k_B T}\\right) \\implies E_c - E_F = k_B T \\ln\\left(\\frac{N_c}{n}\\right)
\\]
\\[
E_c - E_F = (0.02585\\text{ eV}) \\ln\\left( \\frac{2.8 \\times 10^{19}}{2.0 \\times 10^{16}} \\right) = 0.02585 \\ln(1400) = 0.02585 \\times 7.244 = 0.187\\text{ eV} = 187\\text{ meV}
\\]
The Fermi level sits $187\\text{ meV}$ below the conduction band edge.

### Step 2: Low-Temperature Freeze-out at $77\\text{ K}$
At $T = 77\\text{ K}$:
\\[
k_B T = (8.6173 \\times 10^{-5}\\text{ eV/K})(77\\text{ K}) = 0.006635\\text{ eV} = 6.635\\text{ meV}
\\]
Effective density of states scales as $T^{3/2}$:
\\[
N_c(77\\text{ K}) = N_c(300\\text{ K}) \\left(\\frac{77}{300}\\right)^{3/2} = 2.8 \\times 10^{19} \\times (0.2567)^{3/2} = 2.8 \\times 10^{19} \\times 0.1300 = 3.64 \\times 10^{18}\\text{ cm}^{-3}
\\]
In the freeze-out regime, charge neutrality $n = N_d^+$ yields:
\\[
n = \\sqrt{\\frac{N_c N_d}{2}} \\exp\\left(-\\frac{E_c - E_d}{2 k_B T}\\right)
\\]
Exponent factor:
\\[
\\frac{E_c - E_d}{2 k_B T} = \\frac{45\\text{ meV}}{2(6.635\\text{ meV})} = \\frac{45}{13.27} = 3.391
\\]
\\[
\\exp(-3.391) = 0.03367
\\]
Prefactor:
\\[
\\sqrt{\\frac{N_c N_d}{2}} = \\sqrt{\\frac{(3.64 \\times 10^{18})(2.0 \\times 10^{16})}{2}} = \\sqrt{3.64 \\times 10^{34}} = 1.908 \\times 10^{17}\\text{ cm}^{-3}
\\]
Carrier concentration:
\\[
n = (1.908 \\times 10^{17})(0.03367) = 6.42 \\times 10^{15}\\text{ cm}^{-3}
\\]
Ionization fraction:
\\[
\\frac{N_d^+}{N_d} = \\frac{n}{N_d} = \\frac{6.42 \\times 10^{15}}{2.0 \\times 10^{16}} = 0.321 = 32.1\\%
\\]
Nearly $68\\%$ of conduction electrons have frozen back into donor states."""
            },
            {
                "probNumber": "7.6",
                "title": "Density of States Derivation in 1D, 2D, and 3D Quantum Confined Systems",
                "difficulty": "Intermediate",
                "statement": "Derive the mathematical functional form of the electronic density of states $g(E)$ as a function of energy $E$ for parabolic dispersion $E(k) = \\frac{\\hbar^2 k^2}{2m^*}$ in:\\n(a) 3D bulk material: show that $g_{\\text{3D}}(E) \\propto E^{1/2}$.\\n(b) 2D quantum well: show that $g_{\\text{2D}}(E) = \\text{constant}$ (step function).\\n(c) 1D quantum wire: show that $g_{\\text{1D}}(E) \\propto E^{-1/2}$ (Van Hove singularity).",
                "solution": r"""### Step 1: General State Counting in $d$-Dimensions
For a system of linear dimension $L$ in $d$ dimensions with volume $V = L^d$, periodic boundary conditions yield a density of allowed $\\mathbf{k}$-points in reciprocal space of:
\\[
\\rho_k = 2 \\times \\left(\\frac{L}{2\\pi}\\right)^d = \\frac{2V}{(2\\pi)^d}
\\]
where the factor of $2$ accounts for electron spin degeneracy.
The number of states with wavevector less than $k$ is $N(k) = \\rho_k \\Omega_d(k)$, where $\\Omega_d(k)$ is the volume of the $k$-space Fermi sphere/disk/line.

### Step 2: Proof for 3D Bulk
In 3D, $\\Omega_3(k) = \\frac{4}{3}\\pi k^3$:
\\[
N_{\\text{3D}}(k) = \\frac{2V}{8\\pi^3} \\left(\\frac{4}{3}\\pi k^3\\right) = \\frac{V k^3}{3\\pi^2}
\\]
Using $k = \\left(\\frac{2m^*E}{\\hbar^2}\\right)^{1/2}$:
\\[
n_{\\text{3D}}(E) = \\frac{N(E)}{V} = \\frac{1}{3\\pi^2} \\left(\\frac{2m^*}{\\hbar^2}\\right)^{3/2} E^{3/2}
\\]
Differentiating with respect to $E$:
\\[
g_{\\text{3D}}(E) = \\frac{dn_{\\text{3D}}}{dE} = \\frac{1}{2\\pi^2} \\left(\\frac{2m^*}{\\hbar^2}\\right)^{3/2} E^{1/2} \\propto E^{1/2}
\\]

### Step 3: Proof for 2D Quantum Well
In 2D, the $k$-space area is $\\Omega_2(k) = \\pi k^2$:
\\[
N_{\\text{2D}}(k) = \\frac{2A}{(2\\pi)^2} (\\pi k^2) = \\frac{A k^2}{2\\pi}
\\]
Using $k^2 = \\frac{2m^*E}{\\hbar^2}$:
\\[
n_{\\text{2D}}(E) = \\frac{N(E)}{A} = \\frac{1}{2\\pi} \\left(\\frac{2m^*E}{\\hbar^2}\\right) = \\frac{m^*}{\\pi \\hbar^2} E
\\]
Differentiating with respect to $E$:
\\[
g_{\\text{2D}}(E) = \\frac{dn_{\\text{2D}}}{dE} = \\frac{m^*}{\\pi \\hbar^2} = \\text{constant}
\\]
The 2D density of states is completely independent of energy, resulting in a staircase profile $\\sum_n \\Theta(E - E_n)$ with each subband.

### Step 4: Proof for 1D Quantum Wire
In 1D, the $k$-space line length is $\\Omega_1(k) = 2k$ (from $-k$ to $+k$):
\\[
N_{\\text{1D}}(k) = \\frac{2L}{2\\pi} (2k) = \\frac{2L k}{\\pi}
\\]
Using $k = \\left(\\frac{2m^*E}{\\hbar^2}\\right)^{1/2}$:
\\[
n_{\\text{1D}}(E) = \\frac{N(E)}{L} = \\frac{2}{\\pi} \\left(\\frac{2m^*}{\\hbar^2}\\right)^{1/2} E^{1/2}
\\]
Differentiating with respect to $E$:
\\[
g_{\\text{1D}}(E) = \\frac{dn_{\\text{1D}}}{dE} = \\frac{1}{\\pi} \\left(\\frac{2m^*}{\\hbar^2}\\right)^{1/2} E^{-1/2} \\propto \\frac{1}{\\sqrt{E}}
\\]
The density of states diverges at the subband edge $E \\to 0$, producing a **Van Hove singularity**."""
            },
            {
                "probNumber": "7.7",
                "title": "Controlled Valence Principle: Mixed Valency and Hopping Conduction in Li_x Ni_{1-x} O",
                "difficulty": "Intermediate",
                "statement": "Stoichiometric nickel monoxide ($\\text{NiO}$) is an insulator with resistivity $\\rho > 10^{13}\\text{ }\\Omega\\cdot\\text{cm}$. Doping with $2.0\\text{ mol}\\%$ $\\text{Li}_2\\text{O}$ yields $\\text{Li}_{0.04}\\text{Ni}_{0.96}\\text{O}$ with room-temperature conductivity $\\sigma = 0.15\\text{ S/cm}$.\\n(a) Write the chemical formula in terms of discrete ionic valencies and calculate the concentration of $\\text{Ni}^{3+}$ hole states per $\\text{cm}^3$ (given unit cell volume of rock-salt cell $V_c = 72.8\\text{ Å}^3$ with $Z = 4$).\\n(b) Using the hopping conductivity relation $\\sigma = \\frac{n e^2 a^2 \\nu_0}{k_B T} \\exp(-E_h/k_B T)$ with attempt frequency $\\nu_0 = 1.0 \\times 10^{13}\\text{ s}^{-1}$ and nearest-neighbor hopping distance $a = 2.95\\text{ Å}$, compute the hopping activation energy $E_h$ in $\\text{eV}$.",
                "solution": r"""### Step 1: Formal Valence and Carrier Density
In $\\text{Li}_{0.04}\\text{Ni}_{0.96}\\text{O}$, each monovalent $\\text{Li}^+$ substituting on a divalent $\\text{Ni}^{2+}$ site induces one neighboring $\\text{Ni}^{2+}$ to oxidize to $\\text{Ni}^{3+}$ to maintain electrical neutrality:
\\[
\\text{Li}_{0.04}^+ \\text{Ni}_{0.92}^{2+} \\text{Ni}_{0.04}^{3+} \\text{O}^{2-}
\\]
The rock salt unit cell contains $Z = 4$ formula units.
Volume of unit cell: $V_c = 72.8\\text{ Å}^3 = 7.28 \\times 10^{-23}\\text{ cm}^3$.
Number of formula units per $\\text{cm}^3$:
\\[
N_{\\text{fu}} = \\frac{4}{7.28 \\times 10^{-23}\\text{ cm}^3} = 5.4945 \\times 10^{22}\\text{ cm}^{-3}
\\]
Concentration of $\\text{Ni}^{3+}$ carrier hopping centers:
\\[
n = 0.04 \\times N_{\\text{fu}} = 0.04 \\times 5.4945 \\times 10^{22} = 2.1978 \\times 10^{21}\\text{ cm}^{-3} = 2.198 \\times 10^{27}\\text{ m}^{-3}
\\]

### Step 2: Hopping Activation Energy
The small-polaron hopping conductivity expression is:
\\[
\\sigma = \\frac{n e^2 a^2 \\nu_0}{k_B T} \\exp\\left(-\\frac{E_h}{k_B T}\\right) = \\sigma_0 \\exp\\left(-\\frac{E_h}{k_B T}\\right)
\\]
Evaluate the pre-exponential factor $\\sigma_0$ at $T = 300\\text{ K}$:
- $n = 2.1978 \\times 10^{27}\\text{ m}^{-3}$
- $e = 1.60218 \\times 10^{-19}\\text{ C}$
- $a = 2.95 \\times 10^{-10}\\text{ m} \\implies a^2 = 8.7025 \\times 10^{-20}\\text{ m}^2$
- $\\nu_0 = 1.0 \\times 10^{13}\\text{ s}^{-1}$
- $k_B T = 1.38065 \\times 10^{-23} \\times 300 = 4.14195 \\times 10^{-21}\\text{ J}$

Numerator:
\\[
n e^2 a^2 \\nu_0 = (2.1978 \\times 10^{27})(2.5670 \\times 10^{-38})(8.7025 \\times 10^{-20})(1.0 \\times 10^{13}) = 4.9097 \\times 10^{-17}
\\]
Prefactor:
\\[
\\sigma_0 = \\frac{4.9097 \\times 10^{-17}}{4.14195 \\times 10^{-21}} = 1.1854 \\times 10^4\\text{ S/m} = 118.54\\text{ S/cm}
\\]
Now solve for $E_h$:
\\[
\\frac{\\sigma}{\\sigma_0} = \\frac{0.15\\text{ S/cm}}{118.54\\text{ S/cm}} = 0.001265
\\]
\\[
-\\frac{E_h}{k_B T} = \\ln(0.001265) = -6.6725
\\]
\\[
E_h = 6.6725 \\times k_B T = 6.6725 \\times (0.025852\\text{ eV}) = 0.1725\\text{ eV} = 172.5\\text{ meV}
\\]
This activation energy of $0.17\\text{ eV}$ represents the lattice polaron distortion barrier that must be overcome for an electron to hop between adjacent $\\text{Ni}^{2+}$ and $\\text{Ni}^{3+}$ sites."""
            },
            {
                "probNumber": "7.8",
                "title": "Sommerfeld Low-Temperature Electronic Heat Capacity Derivation",
                "difficulty": "Advanced",
                "statement": "At temperatures far below the Fermi temperature ($T \\ll T_F$), only electrons within an energy range $\\sim k_B T$ around $E_F$ can absorb thermal energy.\\n(a) Derive the Sommerfeld formula for electronic molar heat capacity $C_{el} = \\gamma T$, where $\\gamma = \\frac{\\pi^2}{3} k_B^2 g(E_F) N_A$.\\n(b) Express $\\gamma$ in terms of the gas constant $R$ and the Fermi temperature $T_F = E_F/k_B$.\\n(c) For copper ($E_F = 7.03\\text{ eV}$), compute the Sommerfeld coefficient $\\gamma$ in $\\text{mJ/(mol}\\cdot\\text{K}^2\\text{)}$ and calculate the temperature $T^*$ at which the electronic heat capacity equals the Debye lattice heat capacity $C_{\\text{lat}} = \\frac{12\\pi^4}{5} R (T/\\Theta_D)^3$ (given Debye temperature $\\Theta_D = 343\\text{ K}$).",
                "solution": r"""### Step 1: Sommerfeld Expansion for Heat Capacity
The internal thermal energy of the free electron gas per unit volume is:
\\[
U(T) = \\int_0^\\infty E g(E) f(E, T) dE
\\]
Expanding the integral using the Sommerfeld lemma for $k_B T \\ll E_F$:
\\[
U(T) = U(0) + \\frac{\\pi^2}{6} (k_B T)^2 g(E_F) + \\mathcal{O}(T^4)
\\]
Differentiating with respect to temperature gives the volumetric electronic heat capacity:
\\[
c_{el} = \\frac{dU}{dT} = \\frac{\\pi^2}{3} k_B^2 g(E_F) T
\\]
For one mole of monovalent metal ($N_A$ electrons), replacing $g(E_F)$ with molar density of states:
\\[
C_{el} = \\gamma T \\quad \\text{where} \\quad \\gamma = \\frac{\\pi^2}{3} k_B^2 g(E_F) N_A
\\]

### Step 2: Expression in terms of $R$ and $T_F$
For a 3D parabolic band, $g(E_F) = \\frac{3}{2} \\frac{N}{E_F}$.
Substituting this:
\\[
\\gamma = \\frac{\\pi^2}{3} k_B^2 \\left( \\frac{3 N_A}{2 E_F} \\right) = \\frac{\\pi^2}{2} \\frac{N_A k_B^2}{E_F} = \\frac{\\pi^2}{2} R \\left( \\frac{k_B}{E_F} \\right) = \\frac{\\pi^2 R}{2 T_F}
\\]
where $R = N_A k_B = 8.3145\\text{ J/(mol}\\cdot\\text{K)}$.

### Step 3: Numerical Calculations for Copper
1. **Fermi temperature $T_F$**:
\\[
T_F = \\frac{E_F}{k_B} = \\frac{7.031\\text{ eV}}{8.6173 \\times 10^{-5}\\text{ eV/K}} = 81,\\!590\\text{ K}
\\]
2. **Sommerfeld coefficient $\\gamma$**:
\\[
\\gamma = \\frac{\\pi^2 (8.3145\\text{ J/(mol}\\cdot\\text{K)})}{2(81590\\text{ K})} = \\frac{82.062}{163180} = 5.029 \\times 10^{-4}\\text{ J/(mol}\\cdot\\text{K}^2) = 0.503\\text{ mJ/(mol}\\cdot\\text{K}^2)
\\]
(Experimental value: $\\gamma_{\\text{exp}} = 0.695\\text{ mJ/(mol}\\cdot\\text{K}^2)$; difference is due to electron-phonon mass enhancement $m^*/m_0 \\approx 1.38$).

3. **Crossover Temperature $T^*$**:
Setting $C_{el} = C_{\\text{lat}}$:
\\[
\\gamma T^* = \\frac{12\\pi^4}{5} R \\frac{(T^*)^3}{\\Theta_D^3} = A (T^*)^3 \\implies (T^*)^2 = \\frac{\\gamma}{A}
\\]
Prefactor $A$:
\\[
A = \\frac{12\\pi^4}{5} \\frac{8.3145}{(343)^3} = \\frac{2337.8 \\times 8.3145}{4.0354 \\times 10^7} = \\frac{19438}{4.0354 \\times 10^7} = 4.817 \\times 10^{-4}\\text{ J/(mol}\\cdot\\text{K}^4)
\\]
Equating:
\\[
(T^*)^2 = \\frac{\\gamma}{A} = \\frac{6.95 \\times 10^{-4}\\text{ J/(mol}\\cdot\\text{K}^2)}{4.817 \\times 10^{-4}\\text{ J/(mol}\\cdot\\text{K}^4)} = 1.4428\\text{ K}^2
\\]
\\[
T^* = \\sqrt{1.4428} = 1.20\\text{ K}
\\]
Below $T^* \\approx 1.2\\text{ K}$, the electronic heat capacity dominates over the lattice vibrational heat capacity."""
            },
            {
                "probNumber": "7.9",
                "title": "Semiconductor Optical Bandgap Determination via Tauc Plot Analysis",
                "difficulty": "Advanced",
                "statement": "The optical absorption coefficient $\\alpha(h\\nu)$ near the band edge obeys the Tauc power law $(\\alpha h\\nu)^{1/n} = A (h\\nu - E_g)$, where $n = 1/2$ for direct allowed transitions and $n = 2$ for indirect allowed transitions.\\nSpectrophotometric absorption data for an unknown semiconductor film yields:\\n- At $h\\nu = 1.60\\text{ eV}$: $\\alpha = 1.20 \\times 10^3\\text{ cm}^{-1}$\\n- At $h\\nu = 1.80\\text{ eV}$: $\\alpha = 8.50 \\times 10^3\\text{ cm}^{-1}$\\n- At $h\\nu = 2.00\\text{ eV}$: $\\alpha = 2.10 \\times 10^4\\text{ cm}^{-1}$\\n- At $h\\nu = 2.20\\text{ eV}$: $\\alpha = 3.85 \\times 10^4\\text{ cm}^{-1}$\\n(a) Test whether the transition is direct ($(\\alpha h\\nu)^2$ vs $h\\nu$) or indirect ($(\\alpha h\\nu)^{1/2}$ vs $h\\nu$) by calculating correlation linearity.\\n(b) From the linear fit, extrapolate the optical bandgap $E_g$ of the material.\\n(c) Explain physically why phonon absorption/emission is required for indirect optical transitions.",
                "solution": r"""### Step 1: Data Preparation for Tauc Analysis
Calculate photon energy $h\\nu$, absorption product $\\alpha h\\nu$, $(\\alpha h\\nu)^2$ (Direct test), and $(\\alpha h\\nu)^{1/2}$ (Indirect test):

| $h\\nu$ (eV) | $\\alpha$ ($\text{cm}^{-1}$) | $\\alpha h\\nu$ ($\text{eV}\cdot\text{cm}^{-1}$) | $(\\alpha h\\nu)^2$ ($10^8$) | $(\\alpha h\\nu)^{1/2}$ |
| :--- | :--- | :--- | :--- | :--- |
| $1.60$ | $1200$ | $1920$ | $0.0369$ | $43.82$ |
| $1.80$ | $8500$ | $15300$ | $2.3409$ | $123.69$ |
| $2.00$ | $21000$ | $42000$ | $17.640$ | $204.94$ |
| $2.20$ | $38500$ | $84700$ | $71.741$ | $291.03$ |

### Step 2: Linearity Testing
1. **Direct Plot $(h\\nu \\text{ vs } (\\alpha h\\nu)^2)$**:
   - The values of $(\\alpha h\\nu)^2$ are $0.037, 2.34, 17.64, 71.74$.
   - Successive slope ratios: $\\Delta y / \\Delta x$:
     - Between $1.6$ and $1.8$: $(2.34 - 0.04)/0.2 = 11.5$
     - Between $1.8$ and $2.0$: $(17.64 - 2.34)/0.2 = 76.5$
     - Between $2.0$ and $2.2$: $(71.74 - 17.64)/0.2 = 270.5$
   Highly non-linear (strong quadratic upward curvature). The transition is **NOT direct**.

2. **Indirect Plot $(h\\nu \\text{ vs } (\\alpha h\\nu)^{1/2})$**:
   - The values of $y = (\\alpha h\\nu)^{1/2}$ are $43.82, 123.69, 204.94, 291.03$.
   - Differences:
     - $123.69 - 43.82 = 79.87$
     - $204.94 - 123.69 = 81.25$
     - $291.03 - 204.94 = 86.09$
   The slope $\\Delta y / \\Delta x \\approx 80 / 0.2 = 400\\text{ eV}^{-1/2}\\text{cm}^{-1/2}$ is exceptionally constant ($R^2 > 0.999$)!
   This proves the material possesses an **indirect bandgap**.

### Step 3: Extrapolation of $E_g$
Perform linear regression on $y = (\\alpha h\\nu)^{1/2} = m(h\\nu) + c$:
- Slope $m$:
\\[
m = \\frac{291.03 - 43.82}{2.20 - 1.60} = \\frac{247.21}{0.60} = 412.0\\text{ eV}^{-1/2}\\text{cm}^{-1/2}
\\]
- Intercept with horizontal axis $y = 0$:
\\[
0 = m(E_g) + c \\implies E_g = h\\nu_1 - \\frac{y_1}{m} = 1.60 - \\frac{43.82}{412.0} = 1.60 - 0.106 = 1.494\\text{ eV} \\approx 1.50\\text{ eV}
\\]
The optical bandgap is $E_g = 1.50\\text{ eV}$.

### Step 4: Physical Mechanism of Indirect Transitions
In an indirect bandgap semiconductor (such as silicon or germanium), the valence band maximum (at $\\Gamma$, $\\mathbf{k} = \\mathbf{0}$) and conduction band minimum (at $X$ or $L$, $\\mathbf{k} = \\mathbf{k}_0 \\ne \\mathbf{0}$) occur at different locations in reciprocal space.
Because photons carry negligible momentum ($q_{\\text{photon}} = 2\\pi/\\lambda \\sim 10^7\\text{ m}^{-1} \\ll k_{\\text{BZ}} \\sim 10^{10}\\text{ m}^{-1}$), direct vertical optical absorption cannot conserve crystal momentum alone.
Therefore, the optical transition must proceed as a second-order quantum perturbation process involving simultaneous absorption/emission of a lattice **phonon** of momentum $\\hbar\\mathbf{q} \\approx \\hbar\\mathbf{k}_0$:
\\[
E_{\\text{photon}} = E_g \\pm \\hbar\\omega_{\\text{phonon}}
\\]
This requirement reduces the transition probability by several orders of magnitude compared to direct bandgap semiconductors."""
            }
        ]
    }
    return u7

if __name__ == '__main__':
    u7 = get_unit_7()
    print("Unit 7 successfully generated:")
    print("Title:", u7["title"])
    print("Sections:", len(u7["sections"]))
    print("Problems:", len(u7["problems"]))
