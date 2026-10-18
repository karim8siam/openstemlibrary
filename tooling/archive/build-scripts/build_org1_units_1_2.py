# Unit 1 & Unit 2 Content Generator for Organic Chemistry I
# Strict zero course numbers or marks

def get_unit_1():
    return {
        "id": "unit1",
        "unitId": "unit1-org1",
        "number": 1,
        "unitNumber": 1,
        "title": "Unit 1: Foundations of Organic Molecular Structure, Chemical Bonding & Resonance",
        "description": "Rigorous quantum and structural foundations of organic chemistry: atomic electron configurations of carbon, valence bond hybridization theory, Coulson's theorem of hybrid interbond angles, molecular orbital descriptions of sigma and pi bonds, bond polarization and electric dipole moments, resonance theory, curved-arrow electron formalism, and aromatic/allylic delocalization energies.",
        "leadSummary": "Exhaustive exploration of carbon electronic architecture, covalent bond directional properties, orbital hybridization, MO theory, dipole moments, and resonance delocalization frameworks.",
        "simulations": ["sim_chem_organic_hybridization_resonance"],
        "sections": [
            {
                "id": "sec1_1",
                "secNumber": "§1.1",
                "title": "Electronic Structure of Carbon & Quantum Orbitals",
                "heading": "Electronic Structure of Carbon & Quantum Orbitals",
                "content": """Organic chemistry is the chemistry of catenated carbon compounds. The unique versatility of carbon—its ability to form millions of stable, diverse linear, branched, cyclic, and polymeric molecular architectures—originates directly from its central position in the periodic table, intermediate electronegativity ($\\chi_P = 2.55$), small covalent radius ($r_{\\text{cov}} \\approx 77\\text{ pm}$), and tetravalent bonding propensity.

### Quantum Electronic Configuration of Isolated Carbon

In the non-relativistic Schrödinger wave mechanics of multi-electron atoms, an isolated ground-state carbon atom has atomic number $Z = 6$. Its six electrons occupy stationary quantum states governed by the four quantum numbers $(n, l, m_l, m_s)$ according to the fundamental principles of quantum electrodynamics:

1. **The Aufbau Principle**: Orbitals fill in order of increasing energy determined by the $(n + l)$ Madelung rule:
   $$1s < 2s < 2p_x = 2p_y = 2p_z < 3s < \\dots$$
2. **The Pauli Exclusion Principle**: No two electrons within a bound atomic system may share the identical set of four quantum numbers:
   $$\\Delta \\mathbf{q} \\equiv (n_1, l_1, m_{l1}, m_{s1}) \\neq (n_2, l_2, m_{l2}, m_{s2})$$
   Consequently, each spatial atomic orbital $\\psi_{nlm}(\\mathbf{r})$ can accommodate at most two electrons, which must possess antiparallel spin projections ($m_s = +\\frac{1}{2}$ and $m_s = -\\frac{1}{2}$).
3. **Hund's Rule of Maximum Multiplicity**: In degenerate energy subshells (such as the three $2p$ orbitals: $2p_x, 2p_y, 2p_z$), electrons maximize total spin $S = \\sum m_s$ by occupying distinct degenerate spatial orbitals singly with parallel spins before pairing occurs. This configuration minimizes inter-electronic Coulomb repulsion ($J_{ij}$) and maximizes quantum exchange energy ($K_{ij}$):
   $$\\Delta E_{\\text{exchange}} = -\\sum_{i < j} K_{ij}$$

The ground-state electron configuration of the isolated carbon atom is therefore:
$$\\text{C}(Z=6): \\quad 1s^2 \\, 2s^2 \\, 2p_x^1 \\, 2p_y^1 \\, 2p_z^0 \\tag{1.1}$$
The atomic spectroscopic ground state term symbol is ${}^3P_0$, reflecting total orbital angular momentum $L = 1$, total spin $S = 1$ (spin multiplicity $2S+1 = 3$, triplet), and total angular momentum $J = 0$.

### The Tetravalency Paradox & Electronic Promotion

In its ground state $1s^2 2s^2 2p^2$, carbon possesses only **two unpaired electrons** in the degenerate $2p$ subshell, while the $2s$ subshell is fully occupied by a paired singlet electron pair. A naive application of valence theory would predict that carbon should behave as a **divalent species**, forming compounds such as $\\text{CH}_2$ (methylene carbene) with an unshared lone pair, rather than the universal tetravalent architectures ($\text{CH}_4, \\text{CCl}_4, \\text{CO}_2$) observed in stable chemical systems.

To engage in four covalent bonds, carbon undergoes **electronic promotion** from the ground-state configuration to an excited tetravalent valence state:
$$\\text{C}(1s^2 2s^2 2p^2) \\longrightarrow \\text{C}^*(1s^2 2s^1 2p_x^1 2p_y^1 2p_z^1) \\tag{1.2}$$
This promotion requires an investment of excitation energy:
$$\\Delta E_{\\text{promotion}} \\approx 406\\text{ kJ}\\cdot\\text{mol}^{-1} \\quad (4.21\\text{ eV}) \\tag{1.3}$$
Why is this thermodynamically favorable under ambient conditions?
Because promoting an electron allows carbon to form **four covalent bonds** instead of two. In methane ($\\text{CH}_4$), each carbon-hydrogen bond possesses an average bond dissociation enthalpy of:
$$\\text{BDE}(\\text{C}-\\text{H}) \\approx 413\\text{ kJ}\\cdot\\text{mol}^{-1} \\tag{1.4}$$
The formation of four $\\text{C}-\\text{H}$ bonds releases approximately $4 \\times 413 = 1652\\text{ kJ}\\cdot\\text{mol}^{-1}$ of stabilization energy, compared to only $2 \\times 413 = 826\\text{ kJ}\\cdot\\text{mol}^{-1}$ for two bonds in hypothetical divalent carbon. The net thermodynamic enthalpy balance is overwhelmingly exothermic:
$$\\Delta H_{\\text{formation}} = \\Delta E_{\\text{promotion}} - 4 \\cdot \\text{BDE} = +406 - 1652 = -1246\\text{ kJ}\\cdot\\text{mol}^{-1} \\tag{1.5}$$
The immense energetic payoff of forming two additional strong covalent bonds pays the promotion penalty more than three times over.""",
                "simulations": []
            },
            {
                "id": "sec1_2",
                "secNumber": "§1.2",
                "title": "Lewis Electron-Dot Models, Formal Charges & Octet Rules",
                "heading": "Lewis Electron-Dot Models, Formal Charges & Octet Rules",
                "content": """The Lewis model of chemical bonding, formulated by Gilbert N. Lewis in 1916, provides the universal topological foundation for tracking valence electrons, bond orders, formal charges, and non-bonding electron pairs in organic molecules.

### The Lewis Formalism & Formal Charge Equation

In a Lewis structure, valence electrons are classified as either:
1. **Bonding electron pairs (BP)**: Shared between two nuclei to constitute single, double, or triple covalent bonds.
2. **Non-bonding lone pairs (LP)**: Localized on a single atom.

To evaluate the electronic distribution within a polyatomic molecule or polyatomic ion, each atom is assigned a **Formal Charge ($FC$)**. Formal charge represents the difference between the number of valence electrons in the neutral, isolated, unbonded atom ($V$) and the number of valence electrons assigned to that atom in the Lewis structure, assuming perfectly equal sharing of all bonding electron pairs:
$$FC = V - N_{\\text{lone}} - \\frac{1}{2} N_{\\text{bonding}} \\tag{1.6}$$
where:
- $V$ is the group valence electron count of the free neutral atom (Carbon = 4, Nitrogen = 5, Oxygen = 6, Fluorine = 7, Hydrogen = 1).
- $N_{\\text{lone}}$ is the total number of non-bonding lone pair electrons localized on the atom.
- $N_{\\text{bonding}}$ is the total number of shared bonding electrons in all bonds attached to the atom ($2$ per single bond, $4$ per double bond, $6$ per triple bond).

#### Conservation of Charge
The algebraic sum of formal charges over all atoms in a molecule or molecular ion must rigorously equal the net charge $Q_{\\text{net}}$ of the chemical entity:
$$\\sum_{i=1}^{N_{\\text{atoms}}} FC_i = Q_{\\text{net}} \\tag{1.7}$$

### Systematic Algorithm for Constructing Valid Lewis Structures
1. **Calculate Total Valence Electrons ($N_{\\text{val}}$)**:
   $$N_{\\text{val}} = \\sum V_i - Q_{\\text{net}}$$
2. **Assemble the Skeletal Connectivity**: Connect the central atom (the least electronegative element, excluding Hydrogen) to terminal atoms with single two-electron $\\sigma$ bonds.
3. **Distribute Remaining Electrons as Lone Pairs**: Complete the octet of outer electronegative terminal atoms first (Halogens, Oxygen, Nitrogen).
4. **Satisfy Octets via Multiple Bonding**: If the central atom lacks an octet (fewer than 8 electrons), convert lone pairs from adjacent terminal atoms into sharing $\\pi$ bonds.

### Exceptional Cases in Organic Chemistry:
1. **Incomplete Octets (Electron-Deficient Systems)**:
   Boron and aluminum species (such as borane $\\text{BH}_3$, trimethylborane $\\text{B(CH}_3)_3$, and aluminum trichloride $\\text{AlCl}_3$) have only 6 valence electrons around the central atom. They act as potent **Lewis acids** (electrophiles), readily accepting electron pairs from Lewis bases to achieve octet stability.
2. **Carbocations, Radicals & Carbenes**:
   - **Carbocations ($R_3\\text{C}^+$)**: 6 valence electrons, $FC = +1$, empty unhybridized $p_z$ orbital, powerful electrophiles.
   - **Carbon Radicals ($R_3\\text{C}^\\bullet$)**: 7 valence electrons, $FC = 0$, singly occupied $p$ orbital, highly reactive free-radical intermediates.
   - **Carbenes ($R_2\\text{C}:$)**: 6 valence electrons, neutral ($FC = 0$), existing in singlet (${}^1A_1$, paired lone pair in $sp^2$) or triplet (${}^3B_1$, diradical) spin states.""",
                "simulations": []
            },
            {
                "id": "sec1_3",
                "secNumber": "§1.3",
                "title": "Valence Bond Hybridization & Coulson's Theorem",
                "heading": "Valence Bond Hybridization & Coulson's Theorem",
                "content": """Although electron promotion explains tetravalency, it does not explain molecular geometry. If carbon used one spherical $2s$ orbital and three mutually orthogonal $2p_x, 2p_y, 2p_z$ orbitals directly for bonding in methane ($\\text{CH}_4$), the molecule would possess three equivalent bonds at $90^\\circ$ angles and one non-directional bond formed by the $2s$ orbital. 

Experimentally, gas-phase electron diffraction and vibrational spectroscopy prove that methane is a perfect regular tetrahedron ($T_d$ point group) with four strictly identical $\\text{C}-\\text{H}$ bonds of length $108.7\\text{ pm}$ and bond angles of precisely $\\arccos(-1/3) \\approx 109.471^\\circ$.

### Linus Pauling's Orbital Hybridization Theory (1931)

To reconcile quantum wavefunctions with spatial molecular geometry, Linus Pauling introduced the mathematical concept of **orbital hybridization**: the linear combination of atomic orbitals on the same atom to generate a new set of equivalent directional hybrid wavefunctions:

#### 1. $sp^3$ Hybridization (Tetrahedral Geometry)
Combining one $2s$ orbital with three $2p$ orbitals ($2p_x, 2p_y, 2p_z$) produces four orthonormal $sp^3$ hybrid wavefunctions directed toward the vertices of a regular tetrahedron:
$$\\begin{aligned}
\\psi_{h1} &= \\frac{1}{2}\\left( s + p_x + p_y + p_z \\right) \\\\
\\psi_{h2} &= \\frac{1}{2}\\left( s + p_x - p_y - p_z \\right) \\\\
\\psi_{h3} &= \\frac{1}{2}\\left( s - p_x + p_y - p_z \\right) \\\\
\\psi_{h4} &= \\frac{1}{2}\\left( s - p_x - p_y + p_z \\right)
\\end{aligned} \\tag{1.8}$$
Each hybrid possesses $25\\%$ $s$-character and $75\\%$ $p$-character. The inter-orbital angle $\\theta$ is obtained from the scalar product of the direction vectors:
$$\\cos\\theta = -\\frac{1}{3} \\implies \\theta = 109.471^\\circ \\tag{1.9}$$

#### 2. $sp^2$ Hybridization (Trigonal Planar Geometry)
Combining one $2s$ orbital with two $2p$ orbitals ($2p_x, 2p_y$) produces three equivalent hybrid wavefunctions in the $xy$-plane at $120^\\circ$ angles, leaving the $2p_z$ orbital unhybridized:
$$\\begin{aligned}
\\psi_{h1} &= \\frac{1}{\\sqrt{3}} s + \\sqrt{\\frac{2}{3}} p_x \\\\
\\psi_{h2} &= \\frac{1}{\\sqrt{3}} s - \\frac{1}{\\sqrt{6}} p_x + \\frac{1}{\\sqrt{2}} p_y \\\\
\\psi_{h3} &= \\frac{1}{\\sqrt{3}} s - \\frac{1}{\\sqrt{6}} p_x - \\frac{1}{\\sqrt{2}} p_y
\\end{aligned} \\tag{1.10}$$
The unhybridized $2p_z$ orbital lies perpendicular to the molecular plane, ready to form a sideways $\\pi$ bond.

#### 3. $sp$ Hybridization (Linear Geometry)
Combining one $2s$ orbital with one $2p$ orbital ($2p_x$) produces two collinear hybrid wavefunctions at $180^\\circ$ angles:
$$\\psi_{h1} = \\frac{1}{\\sqrt{2}}(s + p_x), \\quad \\psi_{h2} = \\frac{1}{\\sqrt{2}}(s - p_x) \\tag{1.11}$$
Two unhybridized mutually orthogonal $p$-orbitals ($2p_y, 2p_z$) remain to form two independent $\\pi$ bonds.

---

### Coulson's Theorem & Non-Integer Hybridization

In real molecules where substituents are not identical (e.g., chloromethane $\\text{CH}_3\\text{Cl}$, cyclopropane $\\text{C}_3\\text{H}_6$, or water $\\text{H}_2\\text{O}$), hybrid orbitals are not constrained to integer $sp, sp^2, sp^3$ ratios.
C. A. Coulson formulated the generalized hybrid orbital equation:
$$\\psi_i = \\frac{s + \\lambda_i p}{\\sqrt{1 + \\lambda_i^2}} \\tag{1.12}$$
where $\\lambda_i^2$ is the **hybridization parameter** ($sp^{\\lambda_i^2}$):
- Fraction of $s$-character: $f_s(i) = \\frac{1}{1 + \\lambda_i^2}$
- Fraction of $p$-character: $f_p(i) = \\frac{\\lambda_i^2}{1 + \\lambda_i^2}$

For any two hybrid orbitals $\\psi_i$ and $\\psi_j$ originating from the same central atom with interbond angle $\\theta_{ij}$, quantum orthogonality requires:
$$\\langle \\psi_i | \\psi_j \\rangle = 0 \\tag{1.13}$$
Expanding the scalar product:
$$\\left\\langle \\frac{s + \\lambda_i \\mathbf{p}_i}{\\sqrt{1+\\lambda_i^2}} \\;\\middle|\\; \\frac{s + \\lambda_j \\mathbf{p}_j}{\\sqrt{1+\\lambda_j^2}} \\right\\rangle = \\frac{1 + \\lambda_i \\lambda_j (\\hat{\\mathbf{p}}_i \\cdot \\hat{\\mathbf{p}}_j)}{\\sqrt{(1+\\lambda_i^2)(1+\\lambda_j^2)}} = 0$$
Since $\\hat{\\mathbf{p}}_i \\cdot \\hat{\\mathbf{p}}_j = \\cos\\theta_{ij}$, we obtain **Coulson's Theorem**:
$$1 + \\lambda_i \\lambda_j \\cos\\theta_{ij} = 0 \\iff \\cos\\theta_{ij} = -\\frac{1}{\\lambda_i \\lambda_j} \\tag{1.14}$$
For equivalent hybrids ($\\lambda_i = \\lambda_j = \\lambda$):
$$\\cos\\theta = -\\frac{1}{\\lambda^2} \\iff \\lambda^2 = -\\frac{1}{\\cos\\theta} \\tag{1.15}$$
- For $\\theta = 180^\\circ$: $\\cos(180^\\circ) = -1 \\implies \\lambda^2 = 1 \\implies sp^1$
- For $\\theta = 120^\\circ$: $\\cos(120^\\circ) = -0.5 \\implies \\lambda^2 = 2 \\implies sp^2$
- For $\\theta = 109.47^\\circ$: $\\cos(109.47^\\circ) = -1/3 \\implies \\lambda^2 = 3 \\implies sp^3$
- For cyclopropane ($\ ext{C}-\\text{C}-\\text{C}$ interbond angle $\\theta \\approx 60^\\circ$ internally, with bent banana bonds at $\\theta_{\\text{orb}} \\approx 102^\\circ$): the carbon hybrids directed toward carbon have $\\lambda^2 \\approx 4.1$ ($sp^{4.1}$), while those directed toward hydrogen have $\\lambda^2 \\approx 2.2$ ($sp^{2.2}$). This directly explains why the $\\text{C}-\\text{H}$ bonds of cyclopropane are unusually acidic and exhibit elevated $J_{\\text{C}-\\text{H}}$ NMR coupling constants!""",
                "simulations": ["sim_chem_organic_hybridization_resonance"]
            },
            {
                "id": "sec1_4",
                "secNumber": "§1.4",
                "title": "Molecular Orbital Theory: Sigma, Pi, Bonding & Antibonding",
                "heading": "Molecular Orbital Theory: Sigma, Pi, Bonding & Antibonding",
                "content": """While Valence Bond (VB) theory depicts chemical bonds as localized electron pairs between adjacent atoms, **Molecular Orbital (MO) Theory** describes electrons as occupying delocalized wavefunctions extending across the entire molecular framework.

### The LCAO Approximation

In the Linear Combination of Atomic Orbitals (LCAO) approximation, a molecular orbital $\\Psi_j$ is expressed as a linear superposition of atomic basis orbitals $\\phi_i$:
$$\\Psi_j = \\sum_{i=1}^N c_{ji} \\phi_i \\tag{1.16}$$
Applying the Rayleigh-Ritz variational principle to minimize expectation energy $\\langle E \\rangle = \\frac{\\langle \\Psi | \\hat{H} | \\Psi \\rangle}{\\langle \\Psi | \\Psi \\rangle}$ yields the **Roothaan-Hall Secular Equations**:
$$\\sum_{i=1}^N c_{ji} (H_{ki} - E_j S_{ki}) = 0, \\quad k = 1, 2, \\dots, N \\tag{1.17}$$
where:
- $H_{ki} \\equiv \\langle \\phi_k | \\hat{H} | \\phi_i \\rangle$ are Coulomb integrals ($k=i$, representing orbital electronegativity $\\alpha$) and resonance/exchange integrals ($k \\neq i$, representing bond interaction $\\beta$).
- $S_{ki} \\equiv \\langle \\phi_k | \\phi_i \\rangle$ is the spatial overlap integral ($S_{ii} = 1$).

### Diatomic Orbital Interactions: $\\sigma$ vs $\\pi$ Topologies

#### 1. The Sigma ($\\sigma$) Bond Framework
A $\\sigma$ molecular orbital possesses cylindrical rotational symmetry about the internuclear bond axis ($z$-axis). In-phase constructive overlap of two collinear $sp^3, sp^2$, or $s$ orbitals produces a strongly stabilized bonding $\\sigma$ orbital and a destabilized antibonding $\\sigma^*$ orbital:
$$\\Psi_{\\sigma} = \\frac{1}{\\sqrt{2(1+S)}}(\\phi_A + \\phi_B), \\quad \\Psi_{\\sigma^*} = \\frac{1}{\\sqrt{2(1-S)}}(\\phi_A - \\phi_B) \\tag{1.18}$$
The bonding orbital accumulates colossal electron density in the internuclear region between the two positive nuclei, shielding them from mutual Coulomb repulsion and binding them together. The antibonding orbital possesses a nodal plane perpendicular to the internuclear axis where electron probability vanishes ($|\\Psi|^2 = 0$).

#### 2. The Pi ($\\pi$) Bond Framework
A $\\pi$ molecular orbital possesses a nodal plane that coincides with the internuclear axis. Sideways parallel overlap of two $2p_z$ atomic orbitals produces:
$$\\Psi_{\\pi} = \\frac{1}{\\sqrt{2(1+S_{\\pi})}}(\\phi_{2p_z}^A + \\phi_{2p_z}^B), \\quad \\Psi_{\\pi^*} = \\frac{1}{\\sqrt{2(1-S_{\\pi})}}(\\phi_{2p_z}^A - \\phi_{2p_z}^B) \\tag{1.19}$$
Because sideways overlap ($S_\\pi$) is substantially weaker than direct head-on axial overlap ($S_\\sigma$):
$$S_\\pi \\approx 0.2 < S_\\sigma \\approx 0.5 \\tag{1.20}$$
The resulting energy splitting $\\Delta E = E_{\\text{antibonding}} - E_{\\text{bonding}}$ is significantly smaller for $\\pi$ bonds than for $\\sigma$ bonds:
- $\\text{BDE}(\\text{C}-\\text{C} \\;\\sigma) \\approx 348\\text{ kJ}\\cdot\\text{mol}^{-1}$
- $\\text{BDE}(\\text{C}=\\text{C} \\;\\sigma + \\pi) \\approx 614\\text{ kJ}\\cdot\\text{mol}^{-1} \\implies \\text{BDE}(\\pi) \\approx 266\\text{ kJ}\\cdot\\text{mol}^{-1}$
This thermodynamic reality governs all organic reactivity: **$\\pi$ bonds are systematically weaker, higher in energy (HOMO), and far more nucleophilic and chemically reactive than $\\sigma$ bonds**.""",
                "simulations": []
            },
            {
                "id": "sec1_5",
                "secNumber": "§1.5",
                "title": "Polar Bonds, Dipole Moments, Inductive & Field Effects",
                "heading": "Polar Bonds, Dipole Moments, Inductive & Field Effects",
                "content": """When two bonded atoms differ in Pauling electronegativity ($\\Delta \\chi_P = |\\chi_A - \\chi_B| > 0$), the bonding electron cloud is polarized toward the more electronegative atom. This asymmetry creates an electric dipole and generates through-bond inductive and through-space electrostatic field effects.

### Electric Dipole Moment Vectors

The electric dipole moment $\\vec{\\mu}$ of an electric charge distribution is defined as:
$$\\vec{\\mu} = \\int \\rho(\\mathbf{r}) \\mathbf{r} \\, d^3r \\approx \\sum_i q_i \\mathbf{r}_i \\tag{1.21}$$
For a diatomic pair of partial charges $+\\delta$ and $-\\delta$ separated by equilibrium bond distance $d$:
$$\\mu = \\delta \\cdot d \\tag{1.22}$$
In SI units, dipole moments are measured in Coulomb-meters ($\\text{C}\\cdot\\text{m}$). In organic chemistry, the historical **Debye unit (D)** is universally employed:
$$1\\text{ D} \\equiv 3.33564 \\times 10^{-30}\\text{ C}\\cdot\\text{m} \\tag{1.23}$$
For an idealized unit elementary charge ($e = 1.602 \\times 10^{-19}\\text{ C}$) separated by $1.0\\text{ \u00c5} = 10^{-10}\\text{ m}$:
$$\\mu_0 = (1.602 \\times 10^{-19}\\text{ C}) \\times (10^{-10}\\text{ m}) = 1.602 \\times 10^{-29}\\text{ C}\\cdot\\text{m} \\approx 4.80\\text{ D} \\tag{1.24}$$
The percent ionic character of a covalent bond is experimentally extracted via:
$$\\%\\text{ Ionic Character} = \\frac{\\mu_{\\text{experimental}}}{\\mu_{\\text{theoretical fully ionic}}} \\times 100\\% \\tag{1.25}$$

### Molecular Vector Summation & Molecular Symmetry
The overall dipole moment of a polyatomic molecule is the vector sum of all individual bond dipole moments plus lone pair contributions:
$$\\vec{\\mu}_{\\text{net}} = \\sum_{k=1}^{N_{\\text{bonds}}} \\vec{\\mu}_k + \\sum_{m=1}^{N_{\\text{lone}}} \\vec{\\mu}_{LP,m} \\tag{1.26}$$
Because dipole moment is a vector quantity, high geometric symmetry can result in a net dipole moment of zero even in molecules composed of strongly polarized individual bonds:
- Carbon dioxide ($\\text{CO}_2$, linear $D_{\\infty h}$): $\\vec{\\mu}_1 + \\vec{\\mu}_2 = \\mathbf{0} \\implies \\mu_{\\text{net}} = 0.0\\text{ D}$.
- Carbon tetrachloride ($\\text{CCl}_4$, tetrahedral $T_d$): four strong $\\text{C}-\\text{Cl}$ dipoles ($1.87\\text{ D}$ each) cancel vectorially to yield $\\mu_{\\text{net}} = 0.0\\text{ D}$.
- Dichloromethane ($\\text{CH}_2\\text{Cl}_2$, bent $C_{2v}$): vectors reinforce along the $C_2$ symmetry axis, yielding $\\mu_{\\text{net}} = 1.60\\text{ D}$.

### Inductive Effect ($-I$ and $+I$) vs Field Effect
1. **The Inductive Effect ($I$)**:
   The transmission of charge polarization through consecutive $\\sigma$ bonds via electronegativity differences. 
   - Electron-withdrawing groups ($-I$): $-\\text{NO}_2, -\\text{CN}, -\\text{F}, -\\text{Cl}, -\\text{Br}, -\\text{CF}_3, -\\text{OH}$.
   - Electron-donating groups ($+I$): alkyl groups ($-\\text{CH}_3, -\\text{CH}_2\\text{CH}_3$), carbanions.
   Because $\\sigma$-bond electrons are tightly held between nuclei, the inductive effect attenuates exponentially with distance, dropping to negligible levels after three consecutive $\\sigma$ bonds:
   $$\\Delta \\delta_n \\propto e^{-\\kappa n} \\tag{1.27}$$
2. **The Field Effect ($F$)**:
   The through-space transmission of electrostatic polarization across the molecular cavity or solvent medium governed by Coulomb's law:
   $$V_{\\text{field}}(\\mathbf{r}) = \\frac{1}{4\\pi\\varepsilon_0 \\varepsilon_r} \\frac{\\vec{\\mu} \\cdot \\hat{\\mathbf{r}}}{r^2} \\tag{1.28}$$
   This effect does not require intervening chemical bonds, as demonstrated by rigid bicyclic systems (e.g., 4-substituted bicyclo[2.2.2]octane-1-carboxylic acids).""",
                "simulations": []
            },
            {
                "id": "sec1_6",
                "secNumber": "§1.6",
                "title": "Resonance Theory, Curved-Arrow Formalism & Delocalization Energy",
                "heading": "Resonance Theory, Curved-Arrow Formalism & Delocalization Energy",
                "content": """Many organic molecules, radicals, and ions cannot be accurately depicted by any single classical Lewis structure. In such systems, electrons are delocalized across three or more adjacent $p$-orbitals. 

### The Resonance Hypothesis

In Valence Bond theory, the true stationary state wavefunction $\\Psi_{\\text{true}}$ of the molecule is represented as a quantum mechanical linear combination of two or more hypothetical canonical Lewis structures $\\Phi_k$:
$$\\Psi_{\\text{true}} = \\sum_{k=1}^M c_k \\Phi_k \\tag{1.29}$$
The actual molecule is not an oscillating mixture of these structures, but a permanent, static **resonance hybrid** that is lower in energy than any individual contributing canonical structure:
$$E_{\\text{hybrid}} < E[\\Phi_k] \\quad \\forall k \\tag{1.30}$$
The difference in energy between the actual resonance hybrid and the most stable hypothetical canonical contributor is the **Resonance Stabilization Energy (Delocalization Energy)**:
$$E_{\\text{res}} \\equiv E[\\Phi_{\\text{most stable}}] - E_{\\text{hybrid}} > 0 \\tag{1.31}$$

### The Curved-Arrow Formalism (Electron Pushing)

Curved arrows are the universal bookkeeping language of organic mechanisms, introduced by Sir Robert Robinson and Christopher Ingold:
1. **Double-barbed arrow ($\\curvearrowright$)**: Denotes the movement of an electron pair (two electrons) from an electron-rich site (lone pair or $\\pi$ bond) to an electron-deficient site (forming a new bond or localizing as a lone pair).
2. **Single-barbed 'fishhook' arrow ($\\rightharpoonup$)**: Denotes the movement of a single electron in homolytic radical reactions.

#### Fundamental Rules of Resonance:
1. **Nuclei never move**: All canonical contributors must share identical nuclear geometries. Only electron distributions differ.
2. **Total number of paired and unpaired electrons must remain invariant**: Radicals do not convert to closed-shell species in resonance.
3. **The Octet Rule is paramount**: Second-row elements ($\text{C, N, O, F}$) can never possess more than eight valence electrons.
4. **Relative Contributor Stability Hierarchy**:
   - Contributors with complete octets on all atoms are far more significant than electron-deficient contributors.
   - Contributors with minimum formal charge separation contribute more.
   - If formal charges are unavoidable, placing negative charge on the more electronegative atom ($\\text{O, N}$) and positive charge on the more electropositive atom ($\\text{C}$) maximizes stability.
   - Contributors with greater number of covalent bonds are more stable.""",
                "simulations": ["sim_chem_organic_hybridization_resonance"]
            }
        ],
        "problems": [
            {
                "id": "prob1_1",
                "difficulty": "foundational",
                "difficultyLabel": "Foundational Level",
                "title": "Problem 1.1: Lewis Structures, Formal Charges & Resonance in Diazomethane",
                "question": """Diazomethane ($\\text{CH}_2\\text{N}_2$) is an invaluable synthetic reagent for preparing methyl esters from carboxylic acids and generating carbenes upon photolysis.
1. Determine the total valence electron count of diazomethane.
2. Construct all significant resonance contributors for diazomethane, showing all non-bonding lone pairs and formal charges on each atom.
3. Rank the canonical contributors in order of their relative contribution to the resonance hybrid, providing complete theoretical rationales based on octet rules, formal charge magnitudes, and electronegativities.
4. Explain why diazomethane exhibits explosive instability despite its resonance stabilization.""",
                "solution": """### Part 1: Total Valence Electron Count
- Carbon ($V = 4$): $1 \\times 4 = 4$
- Hydrogen ($V = 1$): $2 \\times 1 = 2$
- Nitrogen ($V = 5$): $2 \\times 5 = 10$
$$\\text{Total Valence Electrons } N_{\\text{val}} = 4 + 2 + 10 = \\mathbf{16\\text{ electrons (8 pairs)}} \\tag{1}$$

---

### Part 2: Construction of Resonance Contributors
Connectivity: $\\text{H}_2\\text{C}-\\text{N}-\\text{N}$. 
Distributing 16 electrons:

1. **Contributor A**:
   $$\\text{H}_2\\stackrel{\\ominus}{\\text{C}} - \\stackrel{\\oplus}{\\text{N}} \\equiv \\text{N}:$$
   - Carbon: 2 single C-H bonds, 1 single C-N bond, 1 lone pair.
     $$FC(\\text{C}) = 4 - 2 - \\frac{1}{2}(6) = \\mathbf{-1}$$
   - Central Nitrogen: 1 single C-N bond, 1 triple N≡N bond, 0 lone pairs.
     $$FC(\\text{N}_{\\text{central}}) = 5 - 0 - \\frac{1}{2}(8) = \\mathbf{+1}$$
   - Terminal Nitrogen: 1 triple N≡N bond, 1 lone pair.
     $$FC(\\text{N}_{\\text{terminal}}) = 5 - 2 - \\frac{1}{2}(6) = \\mathbf{0}$$
   - Net Charge: $-1 + 1 + 0 = 0$.

2. **Contributor B**:
   $$\\text{H}_2\\text{C} = \\stackrel{\\oplus}{\\text{N}} = \\stackrel{\\ominus}{\\text{N}}:$$
   - Carbon: 2 C-H bonds, 1 C=N double bond, 0 lone pairs.
     $$FC(\\text{C}) = 4 - 0 - \\frac{1}{2}(8) = \\mathbf{0}$$
   - Central Nitrogen: 1 C=N double bond, 1 N=N double bond, 0 lone pairs.
     $$FC(\\text{N}_{\\text{central}}) = 5 - 0 - \\frac{1}{2}(8) = \\mathbf{+1}$$
   - Terminal Nitrogen: 1 N=N double bond, 2 lone pairs.
     $$FC(\\text{N}_{\\text{terminal}}) = 5 - 4 - \\frac{1}{2}(4) = \\mathbf{-1}$$
   - Net Charge: $0 + 1 - 1 = 0$.

3. **Contributor C (Minor Diradical / Incomplete Octet)**:
   $$\\text{H}_2\\stackrel{\\oplus}{\\text{C}} - \\stackrel{\\text{..}}{\\text{N}} = \\stackrel{\\ominus}{\\text{N}}: \\quad \\text{or} \\quad \\text{H}_2\\stackrel{\\oplus}{\\text{C}} - \\stackrel{\\ominus}{\\text{N}} - \\stackrel{\\oplus}{\\text{N}} \\dots$$
   Contains open-shell carbon with incomplete sextet octet, contributing negligibly ($<1\\%$).

---

### Part 3: Contributor Ranking & Rationale
Both Contributor A and Contributor B satisfy the **Octet Rule on all heavy atoms** ($C$ has 8, central $N$ has 8, terminal $N$ has 8).
- In **Contributor B**, the negative formal charge resides on terminal Nitrogen ($\\chi_P = 3.04$), which is substantially more electronegative than Carbon ($\\chi_P = 2.55$).
- In **Contributor A**, the negative formal charge resides on Carbon.
- However, Contributor A features an ultra-strong $\\text{N}\\equiv\\text{N}$ triple bond (bond energy $\\approx 945\\text{ kJ/mol}$) vs two double bonds in B ($2 \\times 418 = 836\\text{ kJ/mol}$).
- Experimentally and computationally, **Contributors A and B contribute nearly equally** to the hybrid ($\sim 48\\%$ and $\sim 48\\%$), rendering the carbon atom intensely nucleophilic and basic (carbanionic character from A), while the terminal dinitrogen moiety acts as an exceptional thermodynamic leaving group ($N_2$).

---

### Part 4: Explosive Instability
Diazomethane is prone to violent detonation upon physical shock, rough surfaces, or warming:
$$\\text{CH}_2\\text{N}_2(g) \\longrightarrow :\\text{CH}_2(g) + \\text{N}_2(g), \\quad \\Delta H^\\circ = -215\\text{ kJ}\\cdot\\text{mol}^{-1}$$
The liberation of molecular nitrogen ($\\text{N}_2$) generates a triple bond with colossal dissociation energy ($945\\text{ kJ/mol}$) and enormous positive entropy ($\Delta S > 0$), creating an insurmountable thermodynamic driving force."""
            },
            {
                "id": "prob1_2",
                "difficulty": "intermediate",
                "difficultyLabel": "Intermediate Level",
                "title": "Problem 1.2: Coulson Theorem & Hybridization Angle Derivations in Cyclopropane",
                "question": """In cyclopropane ($\\text{C}_3\\text{H}_6$), the carbon skeleton forms an equilateral triangle with internuclear geometric bond angles of $\\alpha = 60^\\circ$.
1. If the carbon-carbon bonding hybrid orbitals were directed precisely along the internuclear lines ($\ ext{C}-\\text{C}$ angle $\\theta = 60^\\circ$), demonstrate using Coulson's theorem why such a hybrid is mathematically impossible using standard $s$ and $p$ basis orbitals.
2. High-level spectroscopic and electron diffraction data demonstrate that the external $\\text{H}-\\text{C}-\\text{H}$ bond angle in cyclopropane is $\\theta_{\\text{HCH}} = 115.2^\\circ$. Using Coulson's orthogonality theorem and the conservation of orbital character, calculate:
   - The hybridization index $\\lambda_{\\text{CH}}^2$ and fractional $s$-character $f_s(\\text{CH})$ of the carbon hybrid orbital directed toward hydrogen.
   - The fractional $s$-character $f_s(\\text{CC})$ and hybridization index $\\lambda_{\\text{CC}}^2$ of the carbon hybrid orbital directed toward carbon.
   - The actual inter-orbital angle $\\theta_{\\text{orb}}$ between the two carbon-carbon hybrid orbitals, proving the existence of 'bent' (banana) bonds.""",
                "solution": """### Part 1: Mathematical Impossibility of $\\theta = 60^\\circ$ Standard Hybrids
From Coulson's theorem for two equivalent hybrids directed along interbond angle $\\theta$:
$$1 + \\lambda^2 \\cos\\theta = 0 \\implies \\lambda^2 = -\\frac{1}{\\cos\\theta}$$
For $\\theta = 60^\\circ$:
$$\\cos(60^\\circ) = +0.5 \\implies \\lambda^2 = -\\frac{1}{+0.5} = -2$$
Since $\\lambda^2 = c_p^2 / c_s^2$, the hybridization parameter must be a strictly non-negative real number ($\lambda^2 \\ge 0$). A negative value ($\\lambda^2 = -2$) is physically and mathematically impossible with real orbital coefficients! 
Therefore, carbon **cannot** form hybrid orbitals that point directly along the internuclear axes in a $60^\\circ$ triangle. The bonds must bend outward.

---

### Part 2: Calculation of Hybridization Parameters

#### 1. Carbon-Hydrogen Hybrids:
Given external angle $\\theta_{\\text{HCH}} = 115.2^\\circ$:
$$\\cos(115.2^\\circ) \\approx -0.42578$$
Applying Coulson's theorem to the two equivalent $\\text{C}-\\text{H}$ hybrids:
$$1 + \\lambda_{\\text{CH}}^2 \\cos(\\theta_{\\text{HCH}}) = 0 \\implies \\lambda_{\\text{CH}}^2 = -\\frac{1}{\\cos(115.2^\\circ)} = -\\frac{1}{-0.42578} \\approx \\mathbf{2.3486}$$
- Hybridization: $\\mathbf{sp^{2.35}}$
- Fractional $s$-character:
  $$f_s(\\text{CH}) = \\frac{1}{1 + \\lambda_{\\text{CH}}^2} = \\frac{1}{1 + 2.3486} = \\frac{1}{3.3486} \\approx \\mathbf{0.2986 \\quad (29.86\\%)}$$

#### 2. Carbon-Carbon Hybrids:
The central carbon atom contributes a total of one $2s$ orbital distributed over its four hybrid orbitals (two $\\text{C}-\\text{H}$ hybrids and two $\\text{C}-\\text{C}$ hybrids):
$$\\sum f_s = 2 \\cdot f_s(\\text{CH}) + 2 \\cdot f_s(\\text{CC}) = 1.00$$
$$2(0.2986) + 2 \\cdot f_s(\\text{CC}) = 1.00 \\implies 2 \\cdot f_s(\\text{CC}) = 1.00 - 0.5972 = 0.4028$$
$$f_s(\\text{CC}) = \\mathbf{0.2014 \\quad (20.14\\%)}$$

Finding the hybridization index $\\lambda_{\\text{CC}}^2$:
$$f_s(\\text{CC}) = \\frac{1}{1 + \\lambda_{\\text{CC}}^2} = 0.2014 \\implies 1 + \\lambda_{\\text{CC}}^2 = \\frac{1}{0.2014} \\approx 4.965$$
$$\\lambda_{\\text{CC}}^2 = 4.965 - 1 = \\mathbf{3.965 \\approx 4.0}$$
The $\\text{C}-\\text{C}$ bonding hybrids are approximately $\\mathbf{sp^4}$!

#### 3. True Inter-Orbital Angle $\\theta_{\\text{orb}}$:
Using Coulson's theorem for the two $\\text{C}-\\text{C}$ hybrids:
$$\\cos(\\theta_{\\text{orb}}) = -\\frac{1}{\\lambda_{\\text{CC}}^2} = -\\frac{1}{3.965} \\approx -0.2522$$
$$\\theta_{\\text{orb}} = \\arccos(-0.2522) \\approx \\mathbf{104.6^\\circ}$$
The orbital vectors point at an angle of $104.6^\\circ$ relative to each other, while the nuclear framework forms an angle of only $60.0^\\circ$. 
Each bond bends outward from the internuclear line by:
$$\\Delta \\phi = \\frac{104.6^\\circ - 60.0^\\circ}{2} = \\mathbf{22.3^\\circ}$$
This quantitative derivation confirms the classic Coulson-Moffitt banana bond model of cyclopropane!"""
            },
            {
                "id": "prob1_3",
                "difficulty": "advanced",
                "difficultyLabel": "Advanced Level",
                "title": "Problem 1.3: Vector Dipole Summation & Conformational Moment in 1,2-Dichloroethane",
                "question": """In 1,2-dichloroethane ($\\text{Cl}-\\text{CH}_2-\\text{CH}_2-\\text{Cl}$), rotation about the central $\\text{C}-\\text{C}$ single bond gives rise to an equilibrium mixture of conformers.
1. Derive an exact mathematical expression for the total molecular electric dipole moment $\\mu(\\phi)$ as a function of the dihedral torsional angle $\\phi$ between the two $\\text{C}-\\text{Cl}$ bonds, assuming the local $\\text{C}-\\text{Cl}$ group moment is $\\mu_0 = 1.90\\text{ D}$ and making angle $\\alpha = 109.5^\\circ$ with the $\\text{C}-\\text{C}$ axis.
2. In the gas phase at $298.15\\text{ K}$, the experimental average dipole moment is measured to be $\\bar{\\mu} = 1.12\\text{ D}$.
   - Given that the anti-conformer ($\\phi = 180^\\circ$) possesses $\\mu_{\\text{anti}} = 0.0\\text{ D}$ and the gauche-conformer ($\\phi = 60^\\circ$) possesses a non-zero dipole moment $\\mu_{\\text{gauche}}$, calculate $\\mu_{\\text{gauche}}$.
   - Determine the mole fraction $x_{\\text{gauche}}$ and $x_{\\text{anti}}$ in the gas phase at equilibrium.
   - Calculate the standard Gibbs free energy difference $\\Delta G^\\circ = G_{\\text{gauche}}^\\circ - G_{\\text{anti}}^\\circ$ between the conformers.""",
                "solution": """### Part 1: Dipole Moment as a Function of Dihedral Angle $\\phi$
Align the central $\\text{C}-\\text{C}$ bond along the $z$-axis. The two carbon atoms lie at $(0, 0, -d/2)$ and $(0, 0, +d/2)$.
Each $\\text{C}-\\text{Cl}$ bond makes an angle $\\theta = 180^\\circ - 109.47^\\circ = 70.53^\\circ$ with the $+z$ or $-z$ axis.
The components of the two bond dipole vectors are:
$$\\vec{\\mu}_1 = \\mu_0 (\\sin\\theta \\cos 0, \\; \\sin\\theta \\sin 0, \\; -\\cos\\theta) = \\mu_0 (\\sin\\theta, \\; 0, \\; -\\cos\\theta)$$
$$\\vec{\\mu}_2 = \\mu_0 (\\sin\\theta \\cos\\phi, \\; \\sin\\theta \\sin\\phi, \\; +\\cos\\theta)$$
Adding the vectors:
$$\\vec{\\mu}_{\\text{net}} = \\mu_0 \\left( \\sin\\theta(1 + \\cos\\phi), \\; \\sin\\theta \\sin\\phi, \\; 0 \\right)$$
Notice that the longitudinal $z$-components ($-\\cos\\theta + \\cos\\theta = 0$) cancel identically for all $\\phi$!
Squaring the net dipole moment:
$$\\mu^2(\\phi) = \\mu_0^2 \\sin^2\\theta \\left[ (1 + \\cos\\phi)^2 + \\sin^2\\phi \\right] = \\mu_0^2 \\sin^2\\theta [1 + 2\\cos\\phi + \\cos^2\\phi + \\sin^2\\phi]$$
$$\\mu^2(\\phi) = 2 \\mu_0^2 \\sin^2\\theta (1 + \\cos\\phi) = 4 \\mu_0^2 \\sin^2\\theta \\cos^2\\left(\\frac{\\phi}{2}\\right)$$
Taking the square root:
$$\\mathbf{\\mu(\\phi) = 2 \\mu_0 \\sin\\theta \\left|\\cos\\left(\\frac{\\phi}{2}\\right)\\right|} \\tag{1}$$

---

### Part 2: Gauche Dipole Moment & Conformational Populations

For tetrahedral carbon, $\\cos(109.47^\\circ) = -1/3 \\implies \\sin\\theta = \\sqrt{1 - (-1/3)^2} = \\sqrt{8/9} = \\frac{2\\sqrt{2}}{3} \\approx 0.9428$.
For the gauche conformer, $\\phi = 60^\\circ \\implies \\phi/2 = 30^\\circ \\implies \\cos(30^\\circ) = \\frac{\\sqrt{3}}{2}$:
$$\\mu_{\\text{gauche}} = 2 \\times (1.90\\text{ D}) \\times \\left(\\frac{2\\sqrt{2}}{3}\\right) \\times \\left(\\frac{\\sqrt{3}}{2}\\right) = 1.90 \\times \\frac{2\\sqrt{6}}{3} \\approx \\mathbf{3.10\\text{ D}}$$

The experimental mean square dipole moment is related to the mole fractions by:
$$\\bar{\\mu}^2 = x_{\\text{anti}} \\mu_{\\text{anti}}^2 + x_{\\text{gauche}} \\mu_{\\text{gauche}}^2$$
Since $\\mu_{\\text{anti}} = 0$ and $x_{\\text{anti}} + x_{\\text{gauche}} = 1$:
$$(1.12)^2 = x_{\\text{gauche}} (3.10)^2$$
$$1.2544 = x_{\\text{gauche}} \\times 9.61 \\implies x_{\\text{gauche}} = \\frac{1.2544}{9.61} \\approx \\mathbf{0.1305 \\quad (13.05\\%)}$$
$$x_{\\text{anti}} = 1 - 0.1305 = \\mathbf{0.8695 \\quad (86.95\\%)}$$

---

### Part 3: Gibbs Free Energy Difference $\\Delta G^\\circ$
Note that the gauche state has statistical degeneracy $g = 2$ (gauche(+) and gauche(-)):
$$K_{\\text{eq}} = \\frac{x_{\\text{gauche}}}{x_{\\text{anti}}} = \\frac{0.1305}{0.8695} \\approx 0.1501$$
$$\\Delta G^\\circ = -RT \\ln K_{\\text{eq}} = - (8.3145\\text{ J/mol K}) \\times (298.15\\text{ K}) \\times \\ln(0.1501)$$
$$\\Delta G^\\circ = - (2478.9) \\times (-1.8965) \\approx +4701\\text{ J/mol} = \\mathbf{+4.70\\text{ kJ/mol}}$$
The anti-conformer is thermodynamically favored by $4.70\\text{ kJ/mol}$ in the gas phase due to the complete minimization of both steric and dipolar repulsions."""
            },
            {
                "id": "prob1_4",
                "difficulty": "honors",
                "difficultyLabel": "Honors / Olympiad Proof",
                "title": "Problem 1.4: Hückel Secular Determinant Proof of Allyl Radical, Cation & Anion",
                "question": """Using Hückel Molecular Orbital (HMO) Theory:
1. Construct the $3 \\times 3$ topological secular determinant for the conjugated allyl system ($\\text{CH}_2=\\text{CH}-\\text{CH}_2$).
2. Solve for the three molecular orbital energy eigenvalues $\\epsilon_1, \\epsilon_2, \\epsilon_3$ in terms of $\\alpha$ and $\\beta$.
3. Compute the normalized orbital coefficients for each of the three molecular orbitals $\\psi_1, \\psi_2, \\psi_3$.
4. Determine the total $\\pi$-electron energy $E_\\pi$ and the resonance delocalization energy $E_{\\text{deloc}}$ for:
   - The Allyl Cation ($\\text{C}_3\\text{H}_5^+$)
   - The Allyl Radical ($\\text{C}_3\\text{H}_5^\\bullet$)
   - The Allyl Anion ($\\text{C}_3\\text{H}_5^-$)
5. Calculate the $\\pi$-electron charge density $q_r$ at each carbon atom for all three species, proving why electrophilic and nucleophilic attack occur exclusively at the terminal C1 and C3 positions.""",
                "solution": """### Part 1: Topological Secular Determinant
The allyl framework consists of three $sp^2$ carbons in a linear chain: $C_1 - C_2 - C_3$.
In Hückel theory:
- $H_{11} = H_{22} = H_{33} = \\alpha$
- $H_{12} = H_{23} = \\beta$, $H_{13} = 0$
- $S_{ij} = \\delta_{ij}$
Setting $x = \\frac{\\alpha - \\epsilon}{\\beta}$, the secular determinant is:
$$\\begin{vmatrix}
x & 1 & 0 \\\\
1 & x & 1 \\\\
0 & 1 & x
\\end{vmatrix} = 0 \\tag{1}$$

---

### Part 2: Energy Eigenvalues
Expanding the determinant along the first row:
$$x(x^2 - 1) - 1(x - 0) = 0 \\implies x(x^2 - 2) = 0$$
Roots:
$$x_1 = -\\sqrt{2}, \\quad x_2 = 0, \\quad x_3 = +\\sqrt{2}$$
Since $\\epsilon = \\alpha - x\\beta$ (recalling $\\beta < 0$):
$$\\begin{aligned}
\\mathbf{\\epsilon_1} &= \\alpha + \\sqrt{2}\\beta \\quad \\text{(Bonding MO, } \\Psi_1\\text{)} \\\\
\\mathbf{\\epsilon_2} &= \\alpha \\quad\\quad\\quad\\quad \\text{(Non-Bonding MO, } \\Psi_2\\text{)} \\\\
\\mathbf{\\epsilon_3} &= \\alpha - \\sqrt{2}\\beta \\quad \\text{(Antibonding MO, } \\Psi_3\\text{)}
\\end{aligned} \\tag{2}$$

---

### Part 3: Normalized MO Coefficients
For each eigenvalue $x_k$, solve:
$$\\begin{pmatrix} x & 1 & 0 \\\\ 1 & x & 1 \\\\ 0 & 1 & x \\end{pmatrix} \\begin{pmatrix} c_1 \\\\ c_2 \\\\ c_3 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\\\ 0 \\end{pmatrix}, \\quad c_1^2 + c_2^2 + c_3^2 = 1$$

1. For $x_1 = -\\sqrt{2}$:
   $-\\sqrt{2}c_1 + c_2 = 0 \\implies c_2 = \\sqrt{2}c_1$.
   $c_1 - \\sqrt{2}c_2 + c_3 = 0 \\implies c_3 = c_1$.
   Normalization: $c_1^2 + 2c_1^2 + c_1^2 = 4c_1^2 = 1 \\implies c_1 = 1/2$.
   $$\\mathbf{\\Psi_1 = \\frac{1}{2}\\phi_1 + \\frac{1}{\\sqrt{2}}\\phi_2 + \\frac{1}{2}\\phi_3} \\tag{3}$$

2. For $x_2 = 0$:
   $0\\cdot c_1 + c_2 = 0 \\implies c_2 = 0$.
   $c_1 + c_3 = 0 \\implies c_3 = -c_1$.
   Normalization: $c_1^2 + 0 + c_1^2 = 2c_1^2 = 1 \\implies c_1 = 1/\\sqrt{2}$.
   $$\\mathbf{\\Psi_2 = \\frac{1}{\\sqrt{2}}\\phi_1 + 0\\cdot\\phi_2 - \\frac{1}{\\sqrt{2}}\\phi_3} \\tag{4}$$
   *Crucial Insight*: $\\Psi_2$ has a **node directly at the central carbon C2** ($c_2 = 0$)!

3. For $x_3 = +\\sqrt{2}$:
   $$\\mathbf{\\Psi_3 = \\frac{1}{2}\\phi_1 - \\frac{1}{\\sqrt{2}}\\phi_2 + \\frac{1}{2}\\phi_3} \\tag{5}$$

---

### Part 4: Total $\\pi$-Energy & Delocalization Energy

An isolated localized reference system consists of an isolated ethylene bond ($2e^-$ in $\\alpha + \\beta$, $E = 2\\alpha + 2\\beta$) plus non-interacting $p$-electrons:

1. **Allyl Cation ($2\\,\\pi$ electrons: $\\Psi_1^2$)**:
   $$E_\\pi = 2(\\alpha + \\sqrt{2}\\beta) = 2\\alpha + 2.828\\beta$$
   $$E_{\\text{deloc}} = E_\\pi - (2\\alpha + 2\\beta) = \\mathbf{0.828\\beta \\approx -62\\text{ kJ/mol}}$$

2. **Allyl Radical ($3\\,\\pi$ electrons: $\\Psi_1^2 \\Psi_2^1$)**:
   $$E_\\pi = 2(\\alpha + \\sqrt{2}\\beta) + 1(\\alpha) = 3\\alpha + 2.828\\beta$$
   $$E_{\\text{deloc}} = E_\\pi - (3\\alpha + 2\\beta) = \\mathbf{0.828\\beta \\approx -62\\text{ kJ/mol}}$$

3. **Allyl Anion ($4\\,\\pi$ electrons: $\\Psi_1^2 \\Psi_2^2$)**:
   $$E_\\pi = 2(\\alpha + \\sqrt{2}\\beta) + 2(\\alpha) = 4\\alpha + 2.828\\beta$$
   $$E_{\\text{deloc}} = E_\\pi - (4\\alpha + 2\\beta) = \\mathbf{0.828\\beta \\approx -62\\text{ kJ/mol}}$$
All three species possess the identical resonance stabilization energy of $0.828|\\beta|$ because the non-bonding orbital $\\Psi_2$ has energy exactly $\\alpha$!

---

### Part 5: Charge Densities & Regiochemical Proof
The $\\pi$-electron charge density at carbon atom $r$ is:
$$q_r = \\sum_{j} n_j c_{jr}^2$$
Net charge: $\\zeta_r = 1 - q_r$.

- **Allyl Cation** ($n_1 = 2, n_2 = 0$):
  $$q_1 = q_3 = 2(1/2)^2 = 0.50 \\implies \\zeta_1 = \\zeta_3 = \\mathbf{+0.50}$$
  $$q_2 = 2(1/\\sqrt{2})^2 = 1.00 \\implies \\zeta_2 = \\mathbf{0.00}$$
  *Proof*: The positive charge of the cation is distributed exclusively between the terminal C1 ($+0.5$) and C3 ($+0.5$) carbons; the central C2 atom bears **zero net charge**! Nucleophiles attack C1/C3.

- **Allyl Anion** ($n_1 = 2, n_2 = 2$):
  $$q_1 = q_3 = 2(1/2)^2 + 2(1/\\sqrt{2})^2 = 0.50 + 1.00 = 1.50 \\implies \\zeta_1 = \\zeta_3 = \\mathbf{-0.50}$$
  $$q_2 = 2(1/\\sqrt{2})^2 + 2(0)^2 = 1.00 + 0 = 1.00 \\implies \\zeta_2 = \\mathbf{0.00}$$
  *Proof*: The negative charge is distributed exclusively between C1 ($-0.5$) and C3 ($-0.5$). Electrophiles react exclusively at C1/C3."""
            }
        ]
    }

def get_unit_2():
    return {
        "id": "unit2",
        "unitId": "unit2-org1",
        "number": 2,
        "unitNumber": 2,
        "title": "Unit 2: Saturated Hydrocarbons: Alkanes, Cycloalkanes, Strain Theory & Conformational Analysis",
        "description": "Exhaustive treatment of saturated hydrocarbons: IUPAC systematic nomenclature, constitutional and stereoisomerism, petroleum refining and octane rating mechanics, free-radical halogenation thermodynamics and Hammond's postulate, carbene C-H insertions, Baeyer angle strain theory, cyclohexane chair conformational equilibria, A-values, and Wurtz coupling organometallic pathways.",
        "leadSummary": "In-depth analysis of alkanes and cycloalkanes, free-radical halogenation energetics, Baeyer strain theory, conformational thermodynamics, cyclohexane chair-flips, and Wurtz synthesis.",
        "simulations": ["sim_chem_cycloalkane_conformational_strain"],
        "sections": [
            {
                "id": "sec2_1",
                "secNumber": "§2.1",
                "title": "Structure, Homology & IUPAC Systematic Nomenclature",
                "heading": "Structure, Homology & IUPAC Systematic Nomenclature",
                "content": """Alkanes (aliphatic saturated hydrocarbons) possess the general molecular formula $\\text{C}_n\\text{H}_{2n+2}$ for acyclic systems and $\\text{C}_n\\text{H}_{2n}$ for monocyclic cycloalkanes. Every carbon atom is $sp^3$ hybridized, forming four localized single $\\sigma$ bonds directed toward the vertices of a tetrahedron.

### Homologous Series & Structural Isomerism

A **homologous series** is a family of compounds differing by successive methylene ($\\text{CH}_2$) increments with uniform chemical reactivities and regular physical property gradations.
As carbon number $n$ increases, the number of **constitutional (structural) isomers**—compounds possessing identical molecular formulas but differing atom-to-atom bonding connectivities—diverges with colossal combinatorial speed:

| Carbon Count ($n$) | Molecular Formula | Number of Constitutional Isomers |
| :---: | :---: | :---: |
| 1 | $\\text{CH}_4$ | 1 |
| 2 | $\\text{C}_2\\text{H}_6$ | 1 |
| 3 | $\\text{C}_3\\text{H}_8$ | 1 |
| 4 | $\\text{C}_4\\text{H}_{10}$ | 2 |
| 5 | $\\text{C}_5\\text{H}_{12}$ | 3 |
| 6 | $\\text{C}_6\\text{H}_{14}$ | 5 |
| 7 | $\\text{C}_7\\text{H}_{16}$ | 9 |
| 8 | $\\text{C}_8\\text{H}_{18}$ | 18 |
| 10 | $\\text{C}_{10}\\text{H}_{22}$ | 75 |
| 20 | $\\text{C}_{20}\\text{H}_{42}$ | 366,319 |
| 30 | $\\text{C}_{30}\\text{H}_{62}$ | 4,111,846,763 |

### IUPAC Systematic Nomenclature Rules (Blue Book Standards)

To provide an unambiguous, universally unique name for every organic molecule, the International Union of Pure and Applied Chemistry (IUPAC) established rigorous hierarchical rules:
1. **Identify the Principal Chain**: Select the longest continuous chain of carbon atoms. If two chains have equal length, choose the chain with the greater number of substituents.
2. **Numbering the Principal Chain**: Number the carbon atoms sequentially from the end that gives the lowest locant set at the first point of difference (e.g., $2,4,5$ is preferred over $2,5,6$).
3. **Assemble Substituents Alphabetically**: Prefixes such as di-, tri-, tetra- and conformational descriptors (sec-, tert-) are ignored in alphabetization, except 'iso' and 'neo' which form part of the alkyl radical name.
4. **Cycloalkanes**: Prefixed by 'cyclo-'. If an acyclic substituent contains more carbons than the ring, the ring is treated as a cycloalkyl substituent.""",
                "simulations": []
            },
            {
                "id": "sec2_2",
                "secNumber": "§2.2",
                "title": "Physical Properties, Combustion & The Octane Number",
                "heading": "Physical Properties, Combustion & The Octane Number",
                "content": """### Physical Properties: Intermolecular Forces & Branching

Alkanes are strictly non-polar molecules ($\\mu = 0$). Intermolecular cohesion is governed exclusively by **London Dispersion Forces** (instantaneous induced-dipole interactions). The attractive dispersion energy between two molecules separated by distance $r$ is described by the London formula:
$$E_{\\text{disp}} = -\\frac{3}{4} \\frac{\\alpha^2 I}{(4\\pi\\varepsilon_0)^2 r^6} \\tag{2.1}$$
where $\\alpha$ is molecular electronic polarizability and $I$ is first ionization energy.
- **Molecular Weight Effect**: As carbon chain length increases, total polarizability $\\alpha$ increases, leading to a monotonic elevation in boiling point (approx. $+20\\text{ to } 30^\\circ\\text{C}$ per $\\text{CH}_2$ unit).
- **Branching Effect**: For constitutional isomers with identical molecular formula, **branching decreases boiling point**. A branched alkane adopts a more compact, spherical geometry with smaller surface area, decreasing intermolecular contact area:
  - $n$-Pentane: $\\text{b.p.} = 36.1^\\circ\\text{C}$
  - Isopentane (2-methylbutane): $\\text{b.p.} = 27.8^\\circ\\text{C}$
  - Neopentane (2,2-dimethylpropane): $\\text{b.p.} = 9.5^\\circ\\text{C}$ (Gas at room temperature!)

---

### Combustion Thermodynamics & Octane Ratings

Alkanes react exothermically with oxygen in combustion reactions:
$$\\text{C}_n\\text{H}_{2n+2} + \\left(\\frac{3n+1}{2}\\right) \\text{O}_2 \\longrightarrow n\\,\\text{CO}_2 + (n+1)\\,\\text{H}_2\\text{O}, \\quad \\Delta H_{\\text{comb}} < 0 \\tag{2.2}$$
In internal combustion engines, rapid compression of the fuel-air mixture can trigger premature auto-ignition before the spark plug fires, producing a shockwave known as **engine knock**.

#### The Octane Rating Scale
The **Research Octane Number (RON)** measures resistance to auto-ignition and engine knock:
- **0 Octane Standard**: $n$-Heptane (straight-chain, highly prone to radical auto-ignition via low-barrier peroxide formation, knocks violently).
- **100 Octane Standard**: 2,2,4-Trimethylpentane ('isooctane', highly branched, forms stable tertiary radicals that resist uncontrolled chain branching).
Highly branched alkanes, cycloalkanes, and aromatic hydrocarbons possess vastly higher octane numbers because their radical intermediates are sterically hindered or stabilized, terminating pre-ignition knock cycles.""",
                "simulations": []
            },
            {
                "id": "sec2_3",
                "secNumber": "§2.3",
                "title": "Free-Radical Halogenation: Energetics, Kinetics & Hammond's Postulate",
                "heading": "Free-Radical Halogenation: Energetics, Kinetics & Hammond's Postulate",
                "content": """Alkanes are notoriously unreactive toward common acids, bases, and nucleophiles at room temperature (historical name *paraffins*, from Latin *parum affinis* = 'little affinity'). However, under photochemical ($\\text{h}\\nu$) or thermal ($\\Delta$) excitation, alkanes undergo homolytic **free-radical halogenation**:
$$\\text{R}-\\text{H} + \\text{X}_2 \\xrightarrow{h\\nu \\text{ or } \\Delta} \\text{R}-\\text{X} + \\text{H}-\\text{X} \\tag{2.3}$$

### The Three-Stage Radical Chain Mechanism

1. **Initiation**: Homolytic fission of the weak halogen-halogen bond by absorption of an ultraviolet photon:
   $$\\text{X}_2 \\xrightarrow{h\\nu} 2\\,\\text{X}^\\bullet, \\quad \\Delta H_1 = +\\text{BDE}(\\text{X}-\\text{X}) \\tag{2.4}$$
2. **Propagation (Chain Carrying)**:
   - *Propagation Step 1 (Hydrogen Abstraction)*:
     $$\\text{R}-\\text{H} + \\text{X}^\\bullet \\longrightarrow \\text{R}^\\bullet + \\text{H}-\\text{X}, \\quad \\Delta H_{p1} = \\text{BDE}(\\text{R}-\\text{H}) - \\text{BDE}(\\text{H}-\\text{X}) \\tag{2.5}$$
   - *Propagation Step 2 (Halogen Atom Transfer)*:
     $$\\text{R}^\\bullet + \\text{X}_2 \\longrightarrow \\text{R}-\\text{X} + \\text{X}^\\bullet, \\quad \\Delta H_{p2} = \\text{BDE}(\\text{X}-\\text{X}) - \\text{BDE}(\\text{R}-\\text{X}) \\tag{2.6}$$
   Notice that the halogen radical $\\text{X}^\\bullet$ regenerated in Step 2 re-enters Step 1, driving a catalytic chain reaction with turnover numbers exceeding $10^4$.
3. **Termination (Radical Recombination)**:
   $$\\text{R}^\\bullet + \\text{X}^\\bullet \\longrightarrow \\text{R}-\\text{X}, \\quad 2\\,\\text{R}^\\bullet \\longrightarrow \\text{R}-\\text{R}, \\quad 2\\,\\text{X}^\\bullet \\longrightarrow \\text{X}_2 \\tag{2.7}$$

---

### Thermodynamic Enthalpy Profile & Halogen Reactivity Hierarchy

| Halogen ($\\text{X}$) | $\\Delta H_{p1}$ (kJ/mol) | $\\Delta H_{p2}$ (kJ/mol) | $\\Delta H_{\\text{net}}$ (kJ/mol) | Practical Outcome |
| :---: | :---: | :---: | :---: | :---: |
| **Fluorine ($\\text{F}$)** | $-130$ | $-300$ | **$-430$** | Explosive, uncontrollable polyfluorination and C-C cleavage |
| **Chlorine ($\\text{Cl}$)** | $-17$ | $-88$ | **$-105$** | Exothermic, fast, low regioselectivity (unselective) |
| **Bromine ($\\text{Br}$)** | $+46$ | $-84$ | **$-38$** | Endothermic abstraction, slow, **exquisite regioselectivity** |
| **Iodine ($\\text{I}$)** | $+140$ | $-70$ | **$+70$** | Strongly endothermic, unfeasible under standard conditions |

### Regioselectivity & Hammond's Postulate

The intrinsic reactivity ratios for hydrogen abstraction per C-H bond at $298\\text{ K}$ are:
- **Chlorination**: $1^\\circ : 2^\\circ : 3^\\circ = 1.0 : 3.8 : 5.0$
- **Bromination**: $1^\\circ : 2^\\circ : 3^\\circ = 1 : 82 : 1600$

Why is bromination 300 times more selective for tertiary C-H bonds than chlorination?
George S. Hammond resolved this in 1955 via **Hammond's Postulate**:
> If two states occurring consecutively along a reaction coordinate have nearly the same energy content, their interconversion will involve only a small reorganization of molecular structures.

1. **Chlorination (Exothermic $\\Delta H_{p1} < 0$)**:
   The transition state is reached **early** along the reaction coordinate. The $\\text{C}-\\text{H}$ bond is barely stretched ($\sim 10\\%$), and little radical character has developed on the carbon atom. The transition state resembles the starting alkane reactants, meaning differences in carboradical stability ($3^\\circ > 2^\\circ > 1^\\circ$) have minimal effect on the activation barrier $\\Delta G^\\ddagger$.
2. **Bromination (Endothermic $\\Delta H_{p1} > 0$)**:
   The transition state is reached **late** along the reaction coordinate. The $\\text{C}-\\text{H}$ bond is extensively broken ($\sim 70\\%$), and substantial radical character has developed on carbon. The transition state strongly resembles the product alkyl radical intermediate, meaning the full thermodynamic stabilization of tertiary radicals ($3^\\circ > 2^\\circ \\gg 1^\\circ$ due to hyperconjugation) dramatically lowers the activation energy $\\Delta G^\\ddagger$ for tertiary abstraction!""",
                "simulations": []
            },
            {
                "id": "sec2_4",
                "secNumber": "§2.4",
                "title": "Carbene Additions & C-H Insertion Chemistry",
                "heading": "Carbene Additions & C-H Insertion Chemistry",
                "content": """Carbenes are neutral, divalent carbon species ($R_2\\text{C}:$) possessing six valence electrons. They exist in two distinct electronic spin configurations:
1. **Singlet Carbene (${}^1A_1$)**:
   The carbon is $sp^2$ hybridized with a pair of electrons in an $sp^2$ non-bonding orbital and an empty unhybridized $2p_z$ orbital. Total spin $S = 0$ (singlet). Generated by photolysis of diazomethane ($\\text{CH}_2\\text{N}_2$) or chloroform $\\alpha$-elimination ($:\\text{CCl}_2$).
2. **Triplet Carbene (${}^3B_1$)**:
   The carbon has two degenerate unpaired electrons with parallel spins ($S = 1$). Triplet carbenes behave as ground-state diradicals.

### C-H Insertion Mechanisms

Singlet methylene ($:\\text{CH}_2$) undergoes concerted three-center insertion directly into unactivated $\\text{C}-\\text{H}$ single bonds:
$$\\text{R}_3\\text{C}-\\text{H} + :\\text{CH}_2 \\longrightarrow \\left[ \\begin{matrix} \\text{R}_3\\text{C} & \\cdots & \\text{H} \\\\ & \\ddots & \\vdots \\\\ & & \\text{CH}_2 \\end{matrix} \\right]^\\ddagger \\longrightarrow \\text{R}_3\\text{C}-\\text{CH}_3 \\tag{2.8}$$
Because singlet insertion is an extremely exothermic, concerted reaction with zero activation barrier, it exhibits virtually **zero selectivity**, inserting into $1^\\circ, 2^\\circ,$ and $3^\\circ$ $\\text{C}-\\text{H}$ bonds purely according to statistical hydrogen ratios!""",
                "simulations": []
            },
            {
                "id": "sec2_5",
                "secNumber": "§2.5",
                "title": "Baeyer Strain Theory & Ring Strain Energetics",
                "heading": "Baeyer Strain Theory & Ring Strain Energetics",
                "content": """In 1885, Adolf von Baeyer proposed that planar cycloalkanes experience **angle strain** because the internal geometric angles of regular polygons deviate from the ideal tetrahedral angle of $\\theta_0 = 109.47^\\circ$.

### The Baeyer Angle Deviation Formulation

For a regular planar polygon with $n$ vertices, the interior angle is:
$$\\alpha_n = \\frac{(n - 2) \\times 180^\\circ}{n} \\tag{2.9}$$
Baeyer defined the **angle deviation per vertex ($d$)** as:
$$d = \\frac{1}{2}(109.47^\\circ - \\alpha_n) \\tag{2.10}$$
- Cyclopropane ($n=3$): $\\alpha = 60^\\circ \\implies d = +24.74^\\circ$
- Cyclobutane ($n=4$): $\\alpha = 90^\\circ \\implies d = +9.74^\\circ$
- Cyclopentane ($n=5$): $\\alpha = 108^\\circ \\implies d = +0.74^\\circ$ (Predicted near-zero strain)
- Cyclohexane ($n=6$): $\\alpha = 120^\\circ \\implies d = -5.26^\\circ$ (Predicted strain)

### Quantitative Experimental Ring Strain from Heat of Combustion
Baeyer's assumption that rings are planar failed completely for $n \\ge 6$. In reality, cycloalkanes pucker into three-dimensional non-planar conformations to relieve torsional strain and angle strain.
Total ring strain is rigorously measured by measuring standard heats of combustion per methylene unit ($\\Delta H_{\\text{comb}} / n$) relative to strain-free unstrained open-chain alkanes ($-658.6\\text{ kJ/mol}$ per $\\text{CH}_2$):
$$\\text{Ring Strain} = -\\Delta H_{\\text{comb}}^{\\circ} - (n \\times 658.6\\text{ kJ/mol}) \\tag{2.11}$$

| Ring Size ($n$) | Interior Angle | Strain / $\\text{CH}_2$ (kJ/mol) | Total Ring Strain (kJ/mol) | Dominant Strain Sources |
| :---: | :---: | :---: | :---: | :--- |
| **Cyclopropane ($C_3$)** | $60^\\circ$ | $38.5$ | **$115.5$** | Colossal angle strain + 6 eclipsed C-H bonds |
| **Cyclobutane ($C_4$)** | $88^\\circ$ (puckered) | $27.6$ | **$110.4$** | Severe angle strain + torsional puckering |
| **Cyclopentane ($C_5$)** | $105^\\circ$ (envelope) | $5.2$ | **$26.0$** | Torsional strain relieved by envelope |
| **Cyclohexane ($C_6$)** | $109.5^\\circ$ (chair) | **$0.0$** | **$0.0$** | **Completely Strain-Free (Ideal Chair)** |
| **Cycloheptane ($C_7$)** | $116^\\circ$ (twist-chair) | $3.7$ | **$26.2$** | Transannular cross-ring steric clashes |
| **Cyclooctane ($C_8$)** | $117^\\circ$ (boat-chair) | $5.1$ | **$41.5$** | Medium ring transannular Prelog strain |""",
                "simulations": []
            },
            {
                "id": "sec2_6",
                "secNumber": "§2.6",
                "title": "Cyclohexane Conformational Analysis & A-Values",
                "heading": "Cyclohexane Conformational Analysis & A-Values",
                "content": """Cyclohexane adopts a non-planar **chair conformation** possessing $D_{3d}$ point group symmetry. In the chair conformation:
1. Every carbon-carbon bond angle is precisely $109.5^\\circ$, resulting in **zero angle strain**.
2. Every adjacent pair of carbon atoms has perfectly staggered $\\text{C}-\\text{H}$ bonds with dihedral angles of $60^\\circ$, resulting in **zero torsional strain**.

### Axial vs Equatorial Orientations

The 12 hydrogen atoms of cyclohexane are split into two stereochemically distinct sets:
1. **6 Axial Hydrogens ($H_{\\text{ax}}$)**: Orient strictly parallel to the $C_3$ molecular symmetry axis (3 pointing straight UP, 3 pointing straight DOWN).
2. **6 Equatorial Hydrogens ($H_{\\text{eq}}$)**: Orient outward along the molecular 'equator', alternating slightly up and down.

---

### The Chair-Chair Inversion (Chair-Flip)

At room temperature, cyclohexane undergoes rapid chair-to-chair conformational interconversion at a frequency of approximately $10^5\\text{ s}^{-1}$:
$$\\text{Chair A} \\rightleftharpoons [\\text{Half-Chair}]^\\ddagger \\rightleftharpoons \\text{Twist-Boat} \\rightleftharpoons [\\text{Half-Chair}]^\\ddagger \\rightleftharpoons \\text{Chair B} \\tag{2.12}$$
During the chair flip:
- All axial bonds invert into equatorial bonds.
- All equatorial bonds invert into axial bonds.
- The activation free energy barrier is $\\Delta G^\\ddagger \\approx 45.2\\text{ kJ}\\cdot\\text{mol}^{-1}$ (governed by the half-chair transition state).

---

### Monosubstituted Cyclohexanes & Conformational A-Values

When a substituent $R$ replaces a hydrogen atom on cyclohexane, the two chair conformers are no longer degenerate:
$$\\text{Axial Conformer} \\rightleftharpoons \\text{Equatorial Conformer}, \\quad K_{\\text{eq}} = \\frac{[\\text{Equatorial}]}{[\\text{Axial}]} \\tag{2.13}$$
The equatorial conformer is universally favored thermodynamically because the axial conformer suffers from severe **1,3-diaxial steric interactions** with the two syn-axial hydrogen atoms at C3 and C5.
The thermodynamic preference is quantified by the **Winstein-Holness A-Value**, defined as:
$$A \\equiv -\\Delta G^\\circ = G_{\\text{axial}}^\\circ - G_{\\text{equatorial}}^\\circ = RT \\ln K_{\\text{eq}} \\tag{2.14}$$

| Substituent ($R$) | A-Value ($-\\Delta G^\\circ$, kJ/mol) | % Equatorial at 298 K | Steric Rationale |
| :---: | :---: | :---: | :--- |
| **$-\\text{H}$** | $0.0$ | $50.0\\%$ | Baseline |
| **$-\\text{F}$** | $1.0$ | $60.0\\%$ | Very small halogen |
| **$-\\text{Cl}$** | $2.2$ | $71.0\\%$ | Longer C-Cl bond reduces diaxial clash |
| **$-\\text{Br}$** | $2.3$ | $72.0\\%$ | Similar to Cl due to longer C-Br bond |
| **$-\\text{OH}$** | $3.9$ | $83.0\\%$ | Moderate 1,3-diaxial clash |
| **$-\\text{CH}_3$** | $7.3$ | **$95.0\\%$** | Equivalent to two gauche butane interactions ($2 \\times 3.8$) |
| **$-\\text{CH}_2\\text{CH}_3$** | $7.5$ | $95.3\\%$ | Ethyl can rotate methyl group away from ring |
| **$-\\text{CH(CH}_3)_2$** | $9.2$ | $97.6\\%$ | Isopropyl hydrogen points toward ring |
| **$-\\text{C(CH}_3)_3$** | **$20.5$** | **$>99.99\\%$** | **Conformational Lock** (tert-butyl frozen equatorial) |""",
                "simulations": ["sim_chem_cycloalkane_conformational_strain"]
            },
            {
                "id": "sec2_7",
                "secNumber": "§2.7",
                "title": "Bicycloalkanes, Bredt's Rule & The Wurtz Coupling",
                "heading": "Bicycloalkanes, Bredt's Rule & The Wurtz Coupling",
                "content": """### Bicyclic Ring Systems

Bicycloalkanes contain two rings sharing two or more common bridgehead carbons:
1. **Fused Rings**: Share two adjacent carbons (e.g., bicyclo[4.4.0]decane / decalin). Decalin exists as trans-decalin (rigid, two fused equatorial bonds, incapable of chair flip) and cis-decalin (flexible, undergoes chair-chair inversion).
2. **Bridged Rings**: Share non-adjacent bridgehead carbons separated by one or more carbons (e.g., bicyclo[2.2.1]heptane / norbornane).
3. **Spiro Rings**: Share a single quaternary carbon atom (e.g., spiro[4.5]decane).

#### Bredt's Rule
In 1924, Julius Bredt established an indispensable stereoelectronic rule:
> A double bond cannot terminate at the bridgehead position of a bridged bicyclic ring system unless the ring containing the double bond is large enough ($n \\ge 8$ atoms) to accommodate a trans-alkene without excessive geometric strain.
Bridgehead double bonds in small bridged systems (such as bicyclo[2.2.1]hept-1-ene) require twisting the $p$-orbitals by nearly $90^\\circ$, extinguishing $\\pi$-orbital overlap and resulting in catastrophic angle and torsional strain.

---

### The Wurtz Reaction: Organometallic & Radical Mechanisms

Discovered by Charles-Adolphe Wurtz in 1855, the reaction couples two alkyl halide molecules using metallic sodium to synthesize symmetrical higher alkanes:
$$2\\,\\text{R}-\\text{X} + 2\\,\\text{Na} \\longrightarrow \\text{R}-\\text{R} + 2\\,\\text{NaX} \\tag{2.15}$$

#### Mechanistic Pathway (Organometallic Intermediates):
1. **Single Electron Transfer (SET)** from sodium metal to alkyl halide generates an alkyl radical:
   $$\\text{R}-\\text{X} + \\text{Na} \\longrightarrow \\text{R}^\\bullet + \\text{Na}^+ + \\text{X}^- \\tag{2.16}$$
2. Second electron transfer to the radical generates an organosodium carbanion:
   $$\\text{R}^\\bullet + \\text{Na} \\longrightarrow \\text{R}^- \\text{Na}^+ \\tag{2.17}$$
3. Nucleophilic substitution ($S_N2$) of the organosodium reagent onto unreacted alkyl halide:
   $$\\text{R}^- + \\text{R}-\\text{X} \\longrightarrow \\text{R}-\\text{R} + \\text{X}^- \\tag{2.18}$$

#### Synthetic Limitations:
1. **Low Yield for Cross-Coupling**: Coupling two different alkyl halides ($\\text{R}_1\\text{X} + \\text{R}_2\\text{X}$) yields a statistical nightmare of three products ($\\text{R}_1-\\text{R}_1, \\text{R}_1-\\text{R}_2, \\text{R}_2-\\text{R}_2$) with nearly identical boiling points that are virtually impossible to separate.
2. **Disproportionation Side-Reactions**: With secondary and tertiary halides, the organosodium carbanion acts as a strong base, causing $E2$ elimination to yield alkene and alkane mixtures.""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob2_1",
                "difficulty": "foundational",
                "difficultyLabel": "Foundational Level",
                "title": "Problem 2.1: Free-Radical Halogenation Product Distributions in 2-Methylbutane",
                "question": """Consider the free-radical halogenation of 2-methylbutane ($\\text{(CH}_3)_2\\text{CH}-\\text{CH}_2-\\text{CH}_3$).
1. Draw and provide the complete IUPAC systematic names for all possible monochlorinated constitutional isomers formed in this reaction.
2. Given the relative kinetic reactivity ratios of hydrogen abstraction by chlorine radicals at $298\\text{ K}$ ($1^\\circ : 2^\\circ : 3^\\circ = 1.0 : 3.8 : 5.0$), calculate the exact theoretical percentage yield of each monochlorinated isomer.
3. If 2-methylbutane is instead subjected to free-radical bromination ($1^\\circ : 2^\\circ : 3^\\circ = 1.0 : 82 : 1600$), calculate the predicted percentage yield of the major monobrominated product. Explain the stark contrast between the two halogenation profiles using Hammond's postulate.""",
                "solution": """### Part 1: Monochlorinated Isomers & Nomenclature
2-Methylbutane contains four distinct types of hydrogen atoms:
1. **C1 Hydrogens ($1^\\circ$)**: Six hydrogens on the two equivalent methyl groups attached to C2.
   - Product: **1-Chloro-2-methylbutane**
2. **C2 Hydrogen ($3^\\circ$)**: One tertiary hydrogen.
   - Product: **2-Chloro-2-methylbutane**
3. **C3 Hydrogens ($2^\\circ$)**: Two secondary hydrogens on the methylene group.
   - Product: **2-Chloro-3-methylbutane** (correct IUPAC: 2-chloro-3-methylbutane)
4. **C4 Hydrogens ($1^\\circ$)**: Three primary hydrogens on the terminal methyl group.
   - Product: **1-Chloro-3-methylbutane**

---

### Part 2: Chlorination Percentage Yield Calculations
Relative rate contribution = $(\\text{Number of Equivalent Hydrogens}) \\times (\\text{Relative Reactivity})$:

1. **1-Chloro-2-methylbutane ($1^\\circ$)**:
   $$R_1 = 6 \\times 1.0 = 6.0$$
2. **2-Chloro-2-methylbutane ($3^\\circ$)**:
   $$R_2 = 1 \\times 5.0 = 5.0$$
3. **2-Chloro-3-methylbutane ($2^\\circ$)**:
   $$R_3 = 2 \\times 3.8 = 7.6$$
4. **1-Chloro-3-methylbutane ($1^\\circ$)**:
   $$R_4 = 3 \\times 1.0 = 3.0$$

Total relative reactivity:
$$R_{\\text{total}} = 6.0 + 5.0 + 7.6 + 3.0 = \\mathbf{21.6}$$

Calculating percentage yields:
- **1-Chloro-2-methylbutane**: $\\frac{6.0}{21.6} \\times 100\\% = \\mathbf{27.8\\%}$
- **2-Chloro-2-methylbutane**: $\\frac{5.0}{21.6} \\times 100\\% = \\mathbf{23.1\\%}$
- **2-Chloro-3-methylbutane**: $\\frac{7.6}{21.6} \\times 100\\% = \\mathbf{35.2\\% \\quad (\\text{Major Product!})}$
- **1-Chloro-3-methylbutane**: $\\frac{3.0}{21.6} \\times 100\\% = \\mathbf{13.9\\%}$

*Critical Discovery*: Despite the tertiary position having the highest intrinsic reactivity ($5.0$), **2-chloro-3-methylbutane is the major product** ($35.2\\%$) due to statistical weighting (two secondary hydrogens vs only one tertiary hydrogen)! Chlorination is synthetically unviable due to this complex mixture.

---

### Part 3: Bromination Percentage Yields & Hammond's Postulate
Relative reactivity ratios for Bromine: $1^\\circ : 2^\\circ : 3^\\circ = 1 : 82 : 1600$:
1. $R_1 = 6 \\times 1 = 6$
2. $R_2 (3^\\circ) = 1 \\times 1600 = 1600$
3. $R_3 (2^\\circ) = 2 \\times 82 = 164$
4. $R_4 = 3 \\times 1 = 3$

Total reactivity:
$$R_{\\text{total}} = 6 + 1600 + 164 + 3 = \\mathbf{1773}$$

Percentage yield of major product (2-bromo-2-methylbutane):
$$\\%(2\\text{-bromo-2-methylbutane}) = \\frac{1600}{1773} \\times 100\\% = \\mathbf{90.24\\% \\approx 90.2\\%}$$

By Hammond's postulate, the endothermic hydrogen abstraction in bromination passes through a **late transition state** that closely resembles the tertiary radical intermediate, allowing hyperconjugative stabilization to govern the barrier. In contrast, exothermic chlorination has an **early transition state** with minimal radical character, making it largely unselective."""
            },
            {
                "id": "prob2_2",
                "difficulty": "intermediate",
                "difficultyLabel": "Intermediate Level",
                "title": "Problem 2.2: Conformational Free Energy & Equilibrium of Disubstituted Cyclohexanes",
                "question": """Consider cis- and trans-isomers of 1-tert-butyl-4-methylcyclohexane.
1. Draw the two chair conformations for *cis*-1-tert-butyl-4-methylcyclohexane and the two chair conformations for *trans*-1-tert-butyl-4-methylcyclohexane.
2. Given the A-values: $A(\\text{t-Bu}) = 20.5\\text{ kJ/mol}$ and $A(\\text{Me}) = 7.3\\text{ kJ/mol}$:
   - Calculate the standard Gibbs free energy difference $\\Delta G^\\circ$ between the two chair conformations of the *cis*-isomer.
   - Determine which conformer of the *cis*-isomer is predominantly populated at $298.15\\text{ K}$, and calculate its exact percentage population.
   - Calculate the standard free energy difference $\\Delta G^\\circ$ between the most stable conformer of the *trans*-isomer and the most stable conformer of the *cis*-isomer, proving which stereoisomer is thermodynamically more stable.""",
                "solution": """### Part 1: Chair Conformations of the Stereoisomers

1. **cis-1-tert-Butyl-4-methylcyclohexane**:
   In a 1,4-cis relationship, one substituent must be axial and the other must be equatorial ($a,e$ or $e,a$):
   - **Conformer A**: tert-Butyl(axial), Methyl(equatorial)
   - **Conformer B**: tert-Butyl(equatorial), Methyl(axial)

2. **trans-1-tert-Butyl-4-methylcyclohexane**:
   In a 1,4-trans relationship, substituents are either diequatorial or diaxial:
   - **Conformer C**: tert-Butyl(equatorial), Methyl(equatorial) [diequatorial]
   - **Conformer D**: tert-Butyl(axial), Methyl(axial) [diaxial]

---

### Part 2: Thermodynamic Calculations for the *cis*-Isomer
Comparing Conformer A vs Conformer B:
- In Conformer A, tert-butyl is axial: steric strain energy $= A(\\text{t-Bu}) = +20.5\\text{ kJ/mol}$.
- In Conformer B, methyl is axial: steric strain energy $= A(\\text{Me}) = +7.3\\text{ kJ/mol}$.

Energy difference (Conformer B relative to Conformer A):
$$\\Delta G^\\circ = G_B^\\circ - G_A^\\circ = +7.3 - (+20.5) = \\mathbf{-13.2\\text{ kJ/mol}}$$
Conformer B (equatorial tert-butyl, axial methyl) is overwhelmingly favored.

Calculating the equilibrium constant $K_{\\text{eq}} = [B]/[A]$ at $298.15\\text{ K}$:
$$K_{\\text{eq}} = \\exp\\left(-\\frac{\\Delta G^\\circ}{RT}\\right) = \\exp\\left( \\frac{13200}{8.3145 \\times 298.15} \\right) = \\exp(5.3248) \\approx \\mathbf{205.4}$$
Percentage of Conformer B:
$$\\%B = \\frac{K_{\\text{eq}}}{1 + K_{\\text{eq}}} \\times 100\\% = \\frac{205.4}{206.4} \\times 100\\% = \\mathbf{99.51\\%}$$

---

### Part 3: Comparison of *trans* vs *cis* Stereoisomer
- **Most stable conformer of trans-isomer (Conformer C)**: Both tert-butyl and methyl are equatorial ($e,e$).
  $$\\text{Steric Strain } = 0.0\\text{ kJ/mol}$$
- **Most stable conformer of cis-isomer (Conformer B)**: tert-butyl is equatorial, but methyl is forced into an axial position ($e,a$).
  $$\\text{Steric Strain } = +7.3\\text{ kJ/mol}$$

Net thermodynamic difference between the stereoisomers:
$$\\Delta G_{\\text{trans} \\rightarrow \\text{cis}}^\\circ = +7.3 - 0.0 = \\mathbf{+7.3\\text{ kJ/mol}}$$
The ***trans*-isomer is thermodynamically more stable than the *cis*-isomer by $7.3\\text{ kJ/mol}$** because it can accommodate both bulky alkyl groups in equatorial positions simultaneously."""
            },
            {
                "id": "prob2_3",
                "difficulty": "advanced",
                "difficultyLabel": "Advanced Level",
                "title": "Problem 2.3: Ring Strain Deconvolution & Combustion Thermochemistry in Cycloalkanes",
                "question": """Standard molar enthalpies of combustion ($\\Delta H_{\\text{comb}}^\\circ$) measured at $298.15\\text{ K}$ for liquid/gaseous cycloalkanes are given below:
- Cyclopropane ($\\text{C}_3\\text{H}_6$, $g$): $\\Delta H_{\\text{comb}}^\\circ = -2091.3\\text{ kJ/mol}$
- Cyclopentane ($\\text{C}_5\\text{H}_{10}$, $g$): $\\Delta H_{\\text{comb}}^\\circ = -3290.8\\text{ kJ/mol}$
- Cyclohexane ($\\text{C}_6\\text{H}_{12}$, $g$): $\\Delta H_{\\text{comb}}^\\circ = -3919.6\\text{ kJ/mol}$

1. Compute the enthalpy of combustion per methylene unit ($-\\Delta H_{\\text{comb}}^\\circ / n$) for each of the three rings.
2. Using the strain-free unstrained methylene reference value of $\\Delta H_{\\text{ref}} = -653.27\\text{ kJ/mol}$ established from long open-chain $n$-alkanes in the gas phase:
   - Calculate the total ring strain energy ($SE$) of cyclopropane, cyclopentane, and cyclohexane.
   - Calculate the strain energy per methylene group for each ring.
3. If the $\\text{C}-\\text{C}$ bond dissociation energy in strain-free $n$-butane is $368\\text{ kJ/mol}$, estimate the effective $\\text{C}-\\text{C}$ single bond strength in cyclopropane. Explain how this manifests in the chemical reactivity of cyclopropane toward catalytic hydrogenation.""",
                "solution": """### Part 1: Enthalpy of Combustion per Methylene Group
1. **Cyclopropane ($n=3$)**:
   $$\\frac{-\\Delta H_{\\text{comb}}^\\circ}{3} = \\frac{2091.3}{3} = \\mathbf{697.10\\text{ kJ/mol}}$$
2. **Cyclopentane ($n=5$)**:
   $$\\frac{-\\Delta H_{\\text{comb}}^\\circ}{5} = \\frac{3290.8}{5} = \\mathbf{658.16\\text{ kJ/mol}}$$
3. **Cyclohexane ($n=6$)**:
   $$\\frac{-\\Delta H_{\\text{comb}}^\\circ}{6} = \\frac{3919.6}{6} = \\mathbf{653.27\\text{ kJ/mol}}$$

Notice that cyclohexane possesses an enthalpy of combustion per methylene unit of precisely $653.27\\text{ kJ/mol}$, identical to unstrained acyclic $n$-alkanes!

---

### Part 2: Total Ring Strain & Strain per $\\text{CH}_2$
$$\\text{Total Strain Energy } SE = -\\Delta H_{\\text{comb}}^\\circ - (n \\times 653.27\\text{ kJ/mol})$$

1. **Cyclopropane ($n=3$)**:
   $$SE = 2091.3 - (3 \\times 653.27) = 2091.3 - 1959.81 = \\mathbf{+131.49\\text{ kJ/mol}}$$
   $$\\text{Strain per } \\text{CH}_2 = \\frac{131.49}{3} = \\mathbf{43.83\\text{ kJ/mol}}$$
2. **Cyclopentane ($n=5$)**:
   $$SE = 3290.8 - (5 \\times 653.27) = 3290.8 - 3266.35 = \\mathbf{+24.45\\text{ kJ/mol}}$$
   $$\\text{Strain per } \\text{CH}_2 = \\frac{24.45}{5} = \\mathbf{4.89\\text{ kJ/mol}}$$
3. **Cyclohexane ($n=6$)**:
   $$SE = 3919.6 - (6 \\times 653.27) = 3919.6 - 3919.62 = \\mathbf{0.00\\text{ kJ/mol}}$$
   $$\\text{Strain per } \\text{CH}_2 = \\mathbf{0.00\\text{ kJ/mol}}$$

---

### Part 3: Effective C-C Bond Strength & Hydrogenation Reactivity
Cyclopropane contains three equivalent $\\text{C}-\\text{C}$ bonds. The total ring strain of $131.5\\text{ kJ/mol}$ weakens each bond by approximately:
$$\\Delta E_{\\text{bond}} = \\frac{131.49}{3} \\approx 43.8\\text{ kJ/mol}$$
Effective $\\text{C}-\\text{C}$ bond dissociation energy:
$$\\text{BDE}_{\\text{eff}}(\\text{C}-\\text{C})_{\\text{cyclopropane}} = 368 - 43.8 = \\mathbf{324.2\\text{ kJ/mol}}$$
Because the C-C bonds are severely bent and weakened, cyclopropane behaves chemically more like an alkene than an alkane. It readily undergoes ring-opening catalytic hydrogenation over nickel at $80^\\circ\\text{C}$:
$$\\text{C}_3\\text{H}_6 + \\text{H}_2 \\xrightarrow{\\text{Ni, } 80^\\circ\\text{C}} \\text{CH}_3\\text{CH}_2\\text{CH}_3, \\quad \\Delta H^\\circ = -157\\text{ kJ/mol}$$
In contrast, cyclohexane is completely inert to catalytic hydrogenation even at $300^\\circ\\text{C}$!"""
            },
            {
                "id": "prob2_4",
                "difficulty": "honors",
                "difficultyLabel": "Honors / Olympiad Proof",
                "title": "Problem 2.4: Mechanistic Discrimination in Wurtz vs Corey-House Synthesis",
                "question": """A synthetic chemist attempts to synthesize 2,3-dimethylbutane and 2-methylpentane.
1. The chemist attempts to synthesize 2,3-dimethylbutane by treating 2-bromopropane with sodium metal in dry diethyl ether (Wurtz reaction).
   - Write the complete balanced chemical equation for the expected product.
   - In addition to the desired alkane, two major volatile hydrocarbon side-products (one alkane and one alkene) are formed in substantial quantities. Write their structures and propose a curved-arrow mechanism for their formation via $\\beta$-hydride elimination of the intermediate organosodium carbanion.
2. The chemist attempts to synthesize unsymmetrical 2-methylpentane by mixing 2-bromopropane and 1-bromopropane in a Wurtz reaction.
   - List all three cross- and self-coupling alkane products formed and calculate their theoretical statistical yield distribution.
3. Formulate an elegant, high-yielding synthetic route to 2-methylpentane using the **Corey-House (Gilman dialkylcuprate)** cross-coupling protocol, showing all reagents, intermediate organocuprate structures, and explaining why this method avoids disproportionation side-reactions.""",
                "solution": """### Part 1: Wurtz Reaction of 2-Bromopropane & Disproportionation Side-Products

#### 1. Expected Coupling Product:
$$2\\,(\\text{CH}_3)_2\\text{CH}-\\text{Br} + 2\\,\\text{Na} \\longrightarrow (\\text{CH}_3)_2\\text{CH}-\\text{CH}(\\text{CH}_3)_2 + 2\\,\\text{NaBr}$$
Product: **2,3-Dimethylbutane**.

#### 2. Disproportionation Side-Products:
During the reaction, single electron transfer creates the isopropylsodium carbanion:
$$(\\text{CH}_3)_2\\text{CH}^- \\text{Na}^+$$
Because isopropyl is a sterically encumbered secondary carbanion, its nucleophilicity toward $S_N2$ displacement is suppressed, and its Brønsted basicity dominates.
Instead of attacking unreacted 2-bromopropane at the carbon, it abstracts a $\\beta$-hydrogen in an **$E2$ elimination pathway**:
$$(\\text{CH}_3)_2\\text{CH}^- + \\text{CH}_3-\\text{CH}(\\text{Br})-\\text{CH}_3 \\longrightarrow \\text{CH}_3-\\text{CH}_2-\\text{CH}_3 + \\text{CH}_2=\\text{CH}-\\text{CH}_3 + \\text{Br}^-$$
- Byproduct 1: **Propane** ($\\text{CH}_3\\text{CH}_2\\text{CH}_3$, alkane)
- Byproduct 2: **Propene** ($\\text{CH}_2=\\text{CH}-\\text{CH}_3$, alkene)
These two disproportionation products often account for $>60\\%$ of the total yield!

---

### Part 2: Statistical Mixture in Cross-Wurtz Reaction
Reactants: 2-Bromopropane ($R_1\\text{Br}$) and 1-Bromopropane ($R_2\\text{Br}$).
The non-selective radical/carbanion coupling yields three distinct products:
1. $R_1 - R_1$: **2,3-Dimethylbutane** (Self-coupling)
2. $R_1 - R_2$: **2-Methylpentane** (Desired cross-coupling)
3. $R_2 - R_2$: **$n$-Hexane** (Self-coupling)

Assuming equal reactivities, statistical distribution is:
$$R_1R_1 : R_1R_2 : R_2R_2 = 1 : 2 : 1$$
- 2,3-Dimethylbutane: $\\mathbf{25\\%}$
- 2-Methylpentane: $\\mathbf{50\\%}$
- $n$-Hexane: $\\mathbf{25\\%}$
All three isomers have boiling points within $8^\\circ\\text{C}$ of each other ($58^\\circ\\text{C}, 60^\\circ\\text{C}, 69^\\circ\\text{C}$), rendering fractional distillation separation practically impossible.

---

### Part 3: Corey-House (Gilman) Synthesis of 2-Methylpentane
The Corey-House cross-coupling employs a Lithium Dialkylcuprate (Gilman reagent) $\\text{R}_2\\text{CuLi}$, which couples selectively with primary alkyl halides via a soft organometallic pathway without basic elimination:

1. **Step 1: Preparation of Organolithium**:
   $$(\\text{CH}_3)_2\\text{CH}-\\text{Br} + 2\\,\\text{Li} \\xrightarrow{\\text{dry pentane}} (\\text{CH}_3)_2\\text{CH}-\\text{Li} + \\text{LiBr}$$
2. **Step 2: Generation of Lithium Diisopropylcuprate**:
   $$2\\,(\\text{CH}_3)_2\\text{CH}-\\text{Li} + \\text{CuI} \\xrightarrow{\\text{dry } \\text{Et}_2\\text{O}, -78^\\circ\\text{C}} [(\\text{CH}_3)_2\\text{CH}]_2\\text{CuLi} + \\text{LiI}$$
3. **Step 3: Cross-Coupling with 1-Bromopropane**:
   $$[(\\text{CH}_3)_2\\text{CH}]_2\\text{CuLi} + \\text{CH}_3\\text{CH}_2\\text{CH}_2-\\text{Br} \\xrightarrow{0^\\circ\\text{C}} \\mathbf{(\\text{CH}_3)_2\\text{CH}-\\text{CH}_2\\text{CH}_2\\text{CH}_3} + (\\text{CH}_3)_2\\text{CH}-\\text{Cu} + \\text{LiBr}$$
   Product: **2-Methylpentane** (isolated yield $>85\\%$).

*Why this succeeds*: Organocuprates are 'soft' nucleophiles that undergo oxidative addition followed by reductive elimination at primary alkyl carbons, completely eliminating competitive $E2$ elimination and self-coupling side-products."""
            }
        ]
    }
