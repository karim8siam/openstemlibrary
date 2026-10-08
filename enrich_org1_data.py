# Enrichment script to expand Organic Chemistry I to exhaustive university honors depth (>65,000 words in data file)
import re

def enrich_unit_1(u1):
    # Expand Section 1.1 with deep quantum foundations, radial wavefunctions, and electronic terms
    sec1 = u1["sections"][0]
    sec1["content"] += """

### Hydrogenic Radial Wavefunctions & Carbon Valence Shell Quantum Nodes

In non-relativistic wave mechanics, the electronic wavefunctions of the carbon valence shell are separable product wavefunctions:
$$\\psi_{nlm}(\\mathbf{r}) = R_{nl}(r) Y_l^m(\\theta, \\phi) \\tag{1.1a}$$
where the radial wavefunctions $R_{nl}(r)$ are expressed via associated Laguerre polynomials $L_{n-l-1}^{2l+1}(\\rho)$ with scaled dimensionless radius $\\rho = \\frac{2 Z_{\\text{eff}} r}{n a_0}$:
$$R_{nl}(r) = -\\left[ \\left(\\frac{2 Z_{\\text{eff}}}{n a_0}\\right)^3 \\frac{(n-l-1)!}{2n [(n+l)!]^3} \\right]^{1/2} e^{-\\rho/2} \\rho^l L_{n-l-1}^{2l+1}(\\rho) \\tag{1.1b}$$
For the carbon $2s$ and $2p$ valence atomic orbitals:
- **Carbon $2s$ Orbital ($n=2, l=0$)**:
  $$R_{2s}(r) = \\frac{1}{2\\sqrt{2}} \\left(\\frac{Z_{\\text{eff}}}{a_0}\\right)^{3/2} \\left( 2 - \\frac{Z_{\\text{eff}} r}{a_0} \\right) e^{-Z_{\\text{eff}} r / (2 a_0)} \\tag{1.1c}$$
  The $2s$ radial wavefunction possesses a **radial node** where $R_{2s}(r) = 0$ at:
  $$r_{\\text{node}} = \\frac{2 a_0}{Z_{\\text{eff}}} \\tag{1.1d}$$
  Inside this radial node ($r < r_{\\text{node}}$), the $2s$ wavefunction exhibits a non-zero inner lobe that penetrates deeply past the $1s$ core electron shell, experiencing the unscreened nuclear charge $Z = +6$. This fundamental **penetration and shielding effect** explains why the $2s$ orbital has substantially lower orbital energy ($\epsilon_{2s} \\approx -19.4\\text{ eV}$) than the $2p$ subshell ($\epsilon_{2p} \\approx -10.7\\text{ eV}$).
- **Carbon $2p$ Orbitals ($n=2, l=1$)**:
  $$R_{2p}(r) = \\frac{1}{2\\sqrt{6}} \\left(\\frac{Z_{\\text{eff}}}{a_0}\\right)^{3/2} \\left( \\frac{Z_{\\text{eff}} r}{a_0} \\right) e^{-Z_{\\text{eff}} r / (2 a_0)} \\tag{1.1e}$$
  Because $l=1$, the $2p$ radial wavefunction has zero radial nodes ($n - l - 1 = 0$), but possesses an **angular nodal plane** where the spherical harmonic $Y_1^0(\\theta, \\phi) \\propto \\cos\\theta = 0$ (the $xy$-plane for $2p_z$).

### Slater's Rules for Carbon Effective Nuclear Charge ($Z_{\\text{eff}}$)

Electrons in the outer valence shell are electrostatically shielded from the $+6e$ nuclear charge by inner core and fellow valence electrons. John C. Slater formulated empirical shielding constants $\\sigma$:
$$Z_{\\text{eff}} = Z - \\sigma = 6 - \\sigma \\tag{1.1f}$$
1. **For a $2p$ electron in Carbon ($1s^2 2s^2 2p^2$)**:
   - The other electron in the $2p$ subshell and the two $2s$ electrons (same shell, principal quantum number $n=2$) each contribute $\\sigma_i = 0.35$:
     $$\\sigma_{n=2} = 3 \\times 0.35 = 1.05$$
   - The two $1s$ core electrons (inner shell, $n-1 = 1$) each contribute $\\sigma_i = 0.85$:
     $$\\sigma_{n=1} = 2 \\times 0.85 = 1.70$$
   - Total shielding: $\\sigma = 1.05 + 1.70 = 2.75$.
   - **Effective Nuclear Charge on Carbon $2p$**:
     $$Z_{\\text{eff}}(2p) = 6 - 2.75 = \\mathbf{3.25} \\tag{1.1g}$$
2. **Clementi-Raimondi Self-Consistent Field (SCF) Values**:
   More rigorous Hartree-Fock calculations yield:
   $$Z_{\\text{eff}}(2s) = 3.217, \\quad Z_{\\text{eff}}(2p) = 3.136 \\tag{1.1h}$$
   This intermediate effective nuclear charge grants carbon its balanced electronegativity: strong enough to form robust, non-polar covalent bonds with hydrogen and other carbons, yet polarizable enough to undergo heterolytic additions and substitutions with diverse heteroatoms."""

    # Expand Section 1.3 with Coulson-Moffitt bent bond derivations and NBO Natural Hybrid Orbitals
    sec3 = u1["sections"][2]
    sec3["content"] += """

### Rigorous Mathematical Proof of Coulson's Theorem

Consider two normalized hybrid wavefunctions $\\psi_i$ and $\\psi_j$ centered on the identical atomic nucleus:
$$\\psi_i = c_{si} \\phi_{2s} + c_{pi} \\mathbf{u}_i \\cdot \\boldsymbol{\\phi}_{2p} \\tag{1.12a}$$
$$\\psi_j = c_{sj} \\phi_{2s} + c_{pj} \\mathbf{u}_j \\cdot \\boldsymbol{\\phi}_{2p} \\tag{1.12b}$$
where $\\mathbf{u}_i$ and $\\mathbf{u}_j$ are unit direction vectors in three-dimensional space, and $\\boldsymbol{\\phi}_{2p} = (\\phi_{2px}, \\phi_{2py}, \\phi_{2pz})^T$.
The angle between the two hybrid orbital axes is $\\theta_{ij}$:
$$\\mathbf{u}_i \\cdot \\mathbf{u}_j = \\cos\\theta_{ij} \\tag{1.12c}$$
Normalization of each hybrid orbital requires:
$$\\langle \\psi_i | \\psi_i \\rangle = c_{si}^2 + c_{pi}^2 = 1 \\tag{1.12d}$$
Defining the hybridization parameters $\\lambda_i$ and $\\lambda_j$ as the ratio of $p$-coefficient to $s$-coefficient:
$$\\lambda_i \\equiv \\frac{c_{pi}}{c_{si}} \\implies c_{si}^2 = \\frac{1}{1 + \\lambda_i^2}, \\quad c_{pi}^2 = \\frac{\\lambda_i^2}{1 + \\lambda_i^2} \\tag{1.12e}$$
Applying quantum orthogonality $\\langle \\psi_i | \\psi_j \\rangle = 0$:
$$\\langle \\psi_i | \\psi_j \\rangle = c_{si} c_{sj} \\langle \\phi_{2s} | \\phi_{2s} \\rangle + c_{pi} c_{pj} (\\mathbf{u}_i \\cdot \\mathbf{u}_j) \\langle \\phi_{2p} | \\phi_{2p} \\rangle = 0 \\tag{1.12f}$$
Since the atomic basis orbitals are orthonormal ($\\langle \\phi_{2s} | \\phi_{2s} \\rangle = 1, \\langle \\phi_{2p} | \\phi_{2p} \\rangle = 1$):
$$c_{si} c_{sj} + c_{pi} c_{pj} \\cos\\theta_{ij} = 0 \\tag{1.12g}$$
Dividing through by $c_{si} c_{sj}$:
$$1 + \\left(\\frac{c_{pi}}{c_{si}}\\right) \\left(\\frac{c_{pj}}{c_{sj}}\\right) \\cos\\theta_{ij} = 0 \\implies \\mathbf{1 + \\lambda_i \\lambda_j \\cos\\theta_{ij} = 0} \\tag{Q.E.D.}$$

### Bent's Rule: Correlation of Hybridization with Electronegativity

Formulated in 1961 by Henry A. Bent, this rule governs the redistribution of $s$ and $p$ character across unsymmetrical molecules:
> **Bent's Rule**:
> Atomic $s$-character concentrates in hybrid orbitals directed toward electropositive substituents, while atomic $p$-character concentrates in hybrid orbitals directed toward electronegative substituents.

#### Physical Rationale via Electron Kinetic & Potential Energy:
1. An atomic $s$-orbital has significantly lower energy than a $p$-orbital ($\sim 8.7\\text{ eV}$ lower in carbon).
2. When carbon forms a bond to a highly electronegative atom (such as fluorine, $\\chi_P = 4.0$), electron density is drawn away from carbon toward fluorine. Carbon 'invests' very little of its precious low-energy $s$-character in a bond where the electrons spend little time near the carbon nucleus!
3. Instead, carbon directs its $s$-character into bonds with more electropositive atoms (such as hydrogen or other carbons) or into non-bonding lone pairs, where the electron density remains close to the carbon nucleus, maximizing electrostatic stabilization.
4. **Structural Consequence in Halomethanes**:
   - In fluoromethane ($\\text{CH}_3\\text{F}$), the $\\text{C}-\\text{F}$ bond uses a hybrid with high $p$-character ($sp^{3.8}$).
   - The three $\\text{C}-\\text{H}$ bonds rehybridize to incorporate greater $s$-character ($sp^{2.7}$).
   - By Coulson's theorem, as $\\lambda_{\\text{CH}}^2$ decreases (higher $s$-character), the $\\text{H}-\\text{C}-\\text{H}$ bond angle opens up:
     $$\\theta_{\\text{HCH}} = 110.2^\\circ > 109.5^\\circ$$
   - The $\\text{H}-\\text{C}-\\text{F}$ angle contracts to $108.8^\\circ$.""";

    # Expand Section 1.6 with Natural Bond Orbital (NBO) hyperconjugation and second-order perturbation
    sec6 = u1["sections"][5]
    sec6["content"] += """

### Natural Bond Orbital (NBO) Analysis & Donor-Acceptor Perturbation

In modern computational quantum chemistry (Frank Weinhold), resonance and hyperconjugation are quantitatively calculated using **Natural Bond Orbital (NBO)** theory.
The stabilization energy $E^{(2)}$ arising from the delocalization of an electron pair from a filled donor orbital $\\sigma_i$ (or lone pair $n_i$) into an empty acceptor orbital $\\sigma_j^*$ (or $\\pi_j^*$) is evaluated using **second-order Møller-Plesset perturbation theory**:
$$E^{(2)} = -q_i \\frac{F_{ij}^2}{\\epsilon_j^* - \\epsilon_i} \\tag{1.32}$$
where:
- $q_i$ is the donor orbital occupancy ($2.0$ for a paired electron bond or lone pair).
- $F_{ij} \\equiv \\langle \\sigma_i | \\hat{F} | \\sigma_j^* \\rangle$ is the Fock matrix element measuring the spatial overlap and Hamiltonian coupling between donor and acceptor orbitals.
- $(\\epsilon_j^* - \\epsilon_i)$ is the energy difference between the empty acceptor orbital and the filled donor orbital.

#### Examples in Fundamental Organic Chemistry:
1. **The Gauche Effect in 1,2-Difluoroethane**:
   Naively, 1,2-difluoroethane should prefer the *anti* conformation to minimize dipolar and steric repulsions. 
   Experimentally, the *gauche* conformation is more stable by $\\sim 3.3\\text{ kJ/mol}$!
   *NBO Explanation*: In the gauche conformation, the two electron-rich $\\sigma_{\\text{C}-\\text{H}}$ donor bonds are aligned precisely anti-periplanar ($\phi = 180^\\circ$) to the empty $\\sigma^*_{\\text{C}-\\text{F}}$ acceptor antibonding orbitals. 
   The hyperconjugative donation $\\sigma_{\\text{C}-\\text{H}} \\to \\sigma^*_{\\text{C}-\\text{F}}$ releases:
   $$E^{(2)} \\approx 2 \\times 22.5\\text{ kJ/mol} = 45.0\\text{ kJ/mol}$$
   This colossal quantum mechanical hyperconjugation overwhelms classical dipole-dipole repulsion, locking the molecule into the gauche conformer.
2. **Carbocation Hyperconjugation**:
   In the ethyl cation ($\\text{CH}_3\\text{CH}_2^+$), the filled $\\sigma_{\\text{C}-\\text{H}}$ orbitals on the methyl group donate into the empty $2p_z$ orbital on the cationic carbon:
   $$\\sigma_{\\text{C}-\\text{H}} \\longrightarrow p_z(\\text{C}^+), \\quad E^{(2)} \\approx 38\\text{ kJ/mol}$$
   This hyperconjugation elongates the $\\text{C}-\\text{H}$ bonds and provides the quantum mechanical foundation for the stability hierarchy: $3^\\circ > 2^\\circ > 1^\\circ > \\text{methyl}$."""
    return u1

def enrich_unit_2(u2):
    # Expand Section 2.6 with full Fourier torsional potential derivation and decalins
    sec6 = u2["sections"][5]
    sec6["content"] += """

### Mathematical Modeling of Torsional Potential Energy Curves

The potential energy of an alkane as a function of the dihedral torsional angle $\\phi$ about a single $\\text{C}-\\text{C}$ bond is mathematically represented by a **truncated Fourier series**:
$$V(\\phi) = \\frac{V_1}{2}(1 - \\cos\\phi) + \\frac{V_2}{2}(1 - \\cos 2\\phi) + \\frac{V_3}{2}(1 - \\cos 3\\phi) \\tag{2.15}$$
where:
- $V_1$ represents the one-fold dipole-dipole and steric repulsion between the terminal methyl groups (distinguishing *anti* at $180^\\circ$ from *syn-periplanar* at $0^\\circ$).
- $V_2$ represents two-fold electronic interactions.
- $V_3$ represents the intrinsic three-fold torsional barrier of the staggered-to-eclipsed ethane-like framework.

#### Energetics of $n$-Butane Conformers:
1. **Anti Conformer ($\phi = 180^\circ$)**: Global energy minimum ($V = 0.0\\text{ kJ/mol}$). Staggered with methyl groups maximally separated.
2. **Gauche Conformers ($\phi = 60^\circ, 300^\circ$)**: Local energy minima ($V = +3.8\\text{ kJ/mol}$). Staggered, but experiences one gauche-butane steric clash between methyl groups.
3. **Eclipsed (H / Me) Conformer ($\phi = 120^\circ, 240^\circ$)**: Energy barrier ($V = +15.9\\text{ kJ/mol}$). Two $\\text{H}/\\text{CH}_3$ eclipsing interactions and one $\\text{H}/\\text{H}$ eclipsing interaction.
4. **Syn-Periplanar (Fully Eclipsed, Me / Me) Conformer ($\phi = 0^\circ$)**: Global energy maximum ($V = +20.9\\text{ kJ/mol}$). Severe van der Waals steric clash between methyl groups directly eclipsing each other.

---

### Stereochemistry and Dynamics of Decalins (Bicyclo[4.4.0]decanes)

Decalin consists of two fused cyclohexane rings sharing two adjacent bridgehead carbons:
1. ***trans*-Decalin**:
   - The two cyclohexane rings are fused via **diequatorial bonds**.
   - Conformationally **rigid and frozen**: it cannot undergo a chair-chair flip because inverting one ring would require the second ring to span across two diaxial positions, which is geometrically impossible without breaking the $\\text{C}-\\text{C}$ bonds!
   - Possesses a center of inversion ($C_i$ symmetry); optically inactive.
   - Enthalpy of formation is lower by **$\\Delta H = 11.3\\text{ kJ/mol}$** than *cis*-decalin.
2. ***cis*-Decalin**:
   - Fused via one equatorial and one axial bond ($e,a$).
   - Conformationally **flexible**: undergoes rapid chair-chair inversion with an activation barrier of $\\sim 42\\text{ kJ/mol}$.
   - Contains three gauche-butane interactions between the two rings that are absent in *trans*-decalin, explaining its $11.3\\text{ kJ/mol}$ higher thermodynamic enthalpy."""
    return u2

def enrich_unit_5(u5):
    # Expand Section 5.2 with Craig's rules and Frost circle exact trigonometry
    sec2 = u5["sections"][1]
    sec2["content"] += """

### Analytical Trigonometric Proof of the Hückel $(4n+2)$ Closed-Shell Condition

From the Frost circle formula $\\epsilon_k = \\alpha + 2\\beta \\cos\\left(\\frac{2\\pi k}{N}\\right)$ (where $\\beta < 0$):
1. **The Lowest Energy State ($k=0$)**:
   $$\\epsilon_0 = \\alpha + 2\\beta \\cos(0) = \\alpha + 2\\beta$$
   This state is strictly **non-degenerate** (holds exactly $2$ electrons).
2. **Intermediate Degenerate Bonding States**:
   For any integer $k$ such that $\\cos\\left(\\frac{2\\pi k}{N}\\right) > 0$, the states with $+k$ and $-k$ (or $N-k$) have identical cosine values:
   $$\\cos\\left(\\frac{2\\pi k}{N}\\right) = \\cos\\left(\\frac{2\\pi(N-k)}{N}\\right)$$
   Every bonding level above $k=0$ occurs in **degenerate pairs**, each accommodating $2 \\times 2 = 4$ electrons!
3. **Total Number of Bonding Electrons**:
   If there are $n$ degenerate pairs of bonding molecular orbitals, the total number of electrons required to fill all bonding levels completely is:
   $$N_{\\pi} = 2 \\; (\\text{from } k=0) + 4n \\; (\\text{from } n \\text{ degenerate pairs}) = \\mathbf{4n + 2} \\tag{Q.E.D.}$$
If a system has $4n$ electrons instead, the highest occupied energy level is a degenerate pair containing only $2$ electrons. By Hund's rule, these two electrons must enter with parallel spins, generating a reactive ground-state **diradical (anti-aromatic system)**."""
    return u5

print("Enrichment modules compiled.")
