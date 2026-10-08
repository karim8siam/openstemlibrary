# Comprehensive expansion script for Organic Chemistry I master textbook
# Ensures total word count across units exceeds 65,000 words with rigorous theoretical depth

from build_org1_units_1_2 import get_unit_1, get_unit_2
from build_org1_units_3_4 import get_unit_3, get_unit_4
from build_org1_units_5_6 import get_unit_5, get_unit_6
from build_org1_units_7_8 import get_unit_7, get_unit_8
import json
import re

def enrich_all():
    print("Executing comprehensive academic enrichment...")
    u1 = get_unit_1()
    u2 = get_unit_2()
    u3 = get_unit_3()
    u4 = get_unit_4()
    u5 = get_unit_5()
    u6 = get_unit_6()
    u7 = get_unit_7()
    u8 = get_unit_8()

    # --- UNIT 1 ENRICHMENT ---
    u1["sections"][0]["content"] += """

### Advanced Quantum Foundations: Hydrogenic Radial Distributions & Nodal Topology

In non-relativistic wave mechanics, the electronic wavefunctions of carbon valence orbitals are separable product wavefunctions:
$$\\psi_{nlm}(\\mathbf{r}) = R_{nl}(r) Y_l^m(\\theta, \\phi) \\tag{1.1a}$$
where the radial wavefunctions $R_{nl}(r)$ are expressed via associated Laguerre polynomials $L_{n-l-1}^{2l+1}(\\rho)$ with scaled dimensionless radius $\\rho = \\frac{2 Z_{\\text{eff}} r}{n a_0}$:
$$R_{nl}(r) = -\\left[ \\left(\\frac{2 Z_{\\text{eff}}}{n a_0}\\right)^3 \\frac{(n-l-1)!}{2n [(n+l)!]^3} \\right]^{1/2} e^{-\\rho/2} \\rho^l L_{n-l-1}^{2l+1}(\\rho) \\tag{1.1b}$$
For the carbon $2s$ and $2p$ valence atomic orbitals:
- **Carbon $2s$ Orbital ($n=2, l=0$)**:
  $$R_{2s}(r) = \\frac{1}{2\\sqrt{2}} \\left(\\frac{Z_{\\text{eff}}}{a_0}\\right)^{3/2} \\left( 2 - \\frac{Z_{\\text{eff}} r}{a_0} \\right) e^{-Z_{\\text{eff}} r / (2 a_0)} \\tag{1.1c}$$
  The $2s$ radial wavefunction possesses a **radial node** where $R_{2s}(r) = 0$ at:
  $$r_{\\text{node}} = \\frac{2 a_0}{Z_{\\text{eff}}} \\tag{1.1d}$$
  Inside this radial node ($r < r_{\\text{node}}$), the $2s$ wavefunction exhibits a non-zero inner lobe that penetrates deeply past the $1s$ core electron shell, experiencing the unscreened nuclear charge $Z = +6$. This fundamental penetration and shielding effect explains why the $2s$ orbital has substantially lower orbital energy ($\epsilon_{2s} \\approx -19.4\\text{ eV}$) than the $2p$ subshell ($\epsilon_{2p} \\approx -10.7\\text{ eV}$).
- **Carbon $2p$ Orbitals ($n=2, l=1$)**:
  $$R_{2p}(r) = \\frac{1}{2\\sqrt{6}} \\left(\\frac{Z_{\\text{eff}}}{a_0}\\right)^{3/2} \\left( \\frac{Z_{\\text{eff}} r}{a_0} \\right) e^{-Z_{\\text{eff}} r / (2 a_0)} \\tag{1.1e}$$
  Because $l=1$, the $2p$ radial wavefunction has zero radial nodes ($n - l - 1 = 0$), but possesses an angular nodal plane where the spherical harmonic vanishes.

### Slater's Rules & Self-Consistent Field Screening Mechanics

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

    u1["sections"][2]["content"] += """

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
   - The $\\text{H}-\\text{C}-\\text{F}$ angle contracts to $108.8^\\circ$."""

    u1["sections"][3]["content"] += """

### Symmetry-Adapted Linear Combinations (SALC) for Methane ($T_d$)

In tetrahedral methane ($\\text{CH}_4$, point group $T_d$), the carbon valence orbitals transform as:
- $2s$ orbital: transforms as the totally symmetric representation **$a_1$**.
- $2p_x, 2p_y, 2p_z$ orbitals: transform as the triply degenerate representation **$t_2$**.

The four hydrogen $1s$ basis orbitals form a reducible representation $\\Gamma_{\\text{H}} = a_1 + t_2$.
Applying projection operators yields the Symmetry-Adapted Linear Combinations (SALCs):
$$\\begin{aligned}
\\phi(a_1) &= \\frac{1}{2}(s_1 + s_2 + s_3 + s_4) \\\\
\\phi(t_{2x}) &= \\frac{1}{2}(s_1 - s_2 + s_3 - s_4) \\\\
\\phi(t_{2y}) &= \\frac{1}{2}(s_1 + s_2 - s_3 - s_4) \\\\
\\phi(t_{2z}) &= \\frac{1}{2}(s_1 - s_2 - s_3 + s_4)
\\end{aligned} \\tag{1.20a}$$
Overlapping carbon orbitals with hydrogen SALCs of matching symmetry produces:
1. One non-degenerate bonding orbital $1a_1$ with binding energy of $-23.0\\text{ eV}$.
2. Three degenerate bonding orbitals $1t_2$ with binding energy of $-14.0\\text{ eV}$.

#### Photoelectron Spectroscopy (PES) Experimental Validation:
Classical valence bond theory predicts that all four bonds in methane are identical, implying a single ionization peak in photoelectron spectroscopy.
In reality, the experimental gas-phase UV photoelectron spectrum of methane exhibits **two distinct ionization bands**:
- An ionization peak at **$14.0\\text{ eV}$** (ejection of an electron from the $1t_2$ triply degenerate bonding orbitals).
- An ionization peak at **$23.0\\text{ eV}$** (ejection of an electron from the deeper $1a_1$ orbital).
This famous experiment provides conclusive proof of the Molecular Orbital framework over localized static hybridization models!"""

    u1["sections"][5]["content"] += """

### Natural Bond Orbital (NBO) Analysis & Donor-Acceptor Perturbation

In modern computational quantum chemistry (Frank Weinhold), resonance and hyperconjugation are quantitatively calculated using **Natural Bond Orbital (NBO)** theory.
The stabilization energy $E^{(2)}$ arising from the delocalization of an electron pair from a filled donor orbital $\\sigma_i$ (or lone pair $n_i$) into an empty acceptor orbital $\\sigma_j^*$ (or $\\pi_j^*$) is evaluated using **second-order Møller-Plesset perturbation theory**:
$$E^{(2)} = -q_i \\frac{F_{ij}^2}{\\epsilon_j^* - \\epsilon_i} \\tag{1.32a}$$
where:
- $q_i$ is the donor orbital occupancy ($2.0$ for a paired electron bond or lone pair).
- $F_{ij} \\equiv \\langle \\sigma_i | \\hat{F} | \\sigma_j^* \\rangle$ is the Fock matrix element measuring spatial overlap and Hamiltonian coupling between donor and acceptor orbitals.
- $(\\epsilon_j^* - \\epsilon_i)$ is the energy difference between the empty acceptor orbital and filled donor orbital.

#### The Gauche Effect in 1,2-Difluoroethane:
Naively, 1,2-difluoroethane should prefer the *anti* conformation to minimize dipolar and steric repulsions. 
Experimentally, the *gauche* conformation is more stable by $\\sim 3.3\\text{ kJ/mol}$!
*NBO Explanation*: In the gauche conformation, the two electron-rich $\\sigma_{\\text{C}-\\text{H}}$ donor bonds are aligned precisely anti-periplanar ($\phi = 180^\\circ$) to the empty $\\sigma^*_{\\text{C}-\\text{F}}$ acceptor antibonding orbitals. 
The hyperconjugative donation $\\sigma_{\\text{C}-\\text{H}} \\to \\sigma^*_{\\text{C}-\\text{F}}$ releases:
$$E^{(2)} \\approx 2 \\times 22.5\\text{ kJ/mol} = 45.0\\text{ kJ/mol}$$
This colossal quantum mechanical hyperconjugation overwhelms classical dipole-dipole repulsion, locking the molecule into the gauche conformer."""

    # --- UNIT 2 ENRICHMENT ---
    u2["sections"][2]["content"] += """

### Bell-Evans-Polanyi Principle & Transition-State Coordinate Geometry

The relationship between activation energy ($E_a$) and reaction enthalpy ($\\Delta H^\circ$) in free-radical hydrogen abstractions is formalized by the **Bell-Evans-Polanyi (BEP) Principle**:
$$E_a = E_0 + \\alpha \\, \\Delta H^\\circ \\tag{2.7a}$$
where $E_0$ is the intrinsic activation barrier for an ergoneutral reaction, and $\\alpha$ ($0 < \\alpha < 1$) is the transfer coefficient.
- **For Exothermic Chlorination ($\\Delta H^\circ < 0$)**:
  The transition state occurs very early on the reaction coordinate ($\\alpha \\approx 0.15$). The $\\text{C}-\\text{H}$ bond is barely perturbed:
  $$d_{\\text{C}-\\text{H}}^\\ddagger \\approx 1.12\\text{ \u00c5} \\quad (\\text{equilibrium } 1.09\\text{ \u00c5})$$
  Because the $\\text{C}-\\text{H}$ bond is not significantly broken, differences in radical stabilization energies among primary, secondary, and tertiary sites have negligible leverage over $E_a$.
- **For Endothermic Bromination ($\\Delta H^\circ > 0$)**:
  The transition state occurs late ($\\alpha \\approx 0.85$). The $\\text{C}-\\text{H}$ bond is extensively stretched:
  $$d_{\\text{C}-\\text{H}}^\\ddagger \\approx 1.45\\text{ \u00c5} \\quad (\\sim 33\\% \\text{ elongated})$$
  The forming $\\text{H}-\\text{Br}$ bond is nearly complete ($d_{\\text{H}-\\text{Br}}^\\ddagger \\approx 1.48\\text{ \u00c5}$). Almost a full unit of radical character has developed on the carbon atom, allowing tertiary radical hyperconjugation to maximally lower the late transition state energy."""

    u2["sections"][5]["content"] += """

### Torsional Potential Modeling via Truncated Fourier Series

The potential energy of an alkane as a function of the dihedral torsional angle $\\phi$ about a single $\\text{C}-\\text{C}$ bond is mathematically represented by a **truncated Fourier series**:
$$V(\\phi) = \\frac{V_1}{2}(1 - \\cos\\phi) + \\frac{V_2}{2}(1 - \\cos 2\\phi) + \\frac{V_3}{2}(1 - \\cos 3\\phi) \\tag{2.14a}$$
where:
- $V_1$ represents one-fold dipole-dipole and steric repulsion between terminal methyl groups.
- $V_2$ represents two-fold electronic interactions.
- $V_3$ represents the intrinsic three-fold torsional barrier of the staggered-to-eclipsed framework.

#### Energetics of $n$-Butane Conformers:
1. **Anti Conformer ($\phi = 180^\circ$)**: Global energy minimum ($V = 0.0\\text{ kJ/mol}$). Staggered with methyl groups maximally separated.
2. **Gauche Conformers ($\phi = 60^\circ, 300^\circ$)**: Local energy minima ($V = +3.8\\text{ kJ/mol}$). Staggered, but experiences one gauche-butane steric clash.
3. **Eclipsed (H / Me) Conformer ($\phi = 120^\circ, 240^\circ$)**: Energy barrier ($V = +15.9\\text{ kJ/mol}$). Two $\\text{H}/\\text{CH}_3$ eclipsing interactions and one $\\text{H}/\\text{H}$ eclipsing interaction.
4. **Syn-Periplanar (Fully Eclipsed, Me / Me) Conformer ($\phi = 0^\circ$)**: Global energy maximum ($V = +20.9\\text{ kJ/mol}$). Severe van der Waals steric clash between methyl groups directly eclipsing each other.

### Dynamics and Stereochemistry of Decalins (Bicyclo[4.4.0]decanes)

Decalin consists of two fused cyclohexane rings sharing two adjacent bridgehead carbons:
1. ***trans*-Decalin**:
   - The two cyclohexane rings are fused via **diequatorial bonds**.
   - Conformationally **rigid and frozen**: cannot undergo a chair-chair flip because inverting one ring would require the second ring to span across two diaxial positions, which is geometrically impossible without breaking covalent bonds!
   - Possesses a center of inversion ($C_i$ symmetry); optically inactive.
   - Enthalpy of formation is lower by **$\\Delta H = 11.3\\text{ kJ/mol}$** than *cis*-decalin.
2. ***cis*-Decalin**:
   - Fused via one equatorial and one axial bond ($e,a$).
   - Conformationally **flexible**: undergoes rapid chair-chair inversion with an activation barrier of $\\sim 42\\text{ kJ/mol}$.
   - Contains three gauche-butane interactions between the two rings that are absent in *trans*-decalin, explaining its $11.3\\text{ kJ/mol}$ higher thermodynamic enthalpy."""

    # --- UNIT 3 ENRICHMENT ---
    u3["sections"][3]["content"] += """

### Quantum Nature of the Cyclic Bromonium Ion & Non-Classical Delocalization

The cyclic bromonium ion is an asymmetric three-membered ring whose electronic structure is best described as a closed three-center two-electron (3c-2e) $\\sigma$ bonding system supplemented by back-donation from the bromine $4p$ lone pairs into the empty $p$-orbitals of the two carbons.
The molecular orbital representation of the bromiranium ring consists of three orbitals formed by the linear combination of the two carbon $2p$ lobes and one bromine $4p$ orbital:
$$\\begin{aligned}
\\Psi_1 &= c_1(\\phi_{\\text{C}1} + \\phi_{\\text{C}2}) + c_2\\phi_{\\text{Br}} \\quad (\\text{Strongly bonding}) \\\\
\\Psi_2 &= c_3(\\phi_{\\text{C}1} - \\phi_{\\text{C}2}) \\quad\\quad\\quad\\quad (\\text{Non-bonding / weakly antibonding}) \\\\
\\Psi_3 &= c_4(\\phi_{\\text{C}1} + \\phi_{\\text{C}2}) - c_5\\phi_{\\text{Br}} \\quad (\\text{Strongly antibonding})
\\end{aligned} \\tag{3.12a}$$
The two bonding electrons occupy $\\Psi_1$, concentrating negative charge on bromine while spreading partial positive charge over the two carbon atoms.
In an unsymmetrical alkene (such as propene or 2-methylpropene), the $\\text{C}-\\text{Br}$ bond to the **more substituted carbon is significantly longer ($d \\approx 2.25\\text{ \u00c5}$)** than the bond to the primary carbon ($d \\approx 2.05\\text{ \u00c5}$).
Consequently, the more substituted carbon bears substantial partial positive charge ($^{\\delta+}\\text{C}$), which directs nucleophilic attack by external nucleophiles (such as water or alcohols in halohydrin synthesis) exclusively to the more substituted position with **$100\\%$ stereospecific inversion**."""

    u3["sections"][5]["content"] += """

### Isotopic $^{18}\\text{O}$ Tracing & The Complete Criegee Mechanism of Ozonolysis

The mechanism of ozonolysis was definitively elucidated by Rudolf Criegee using oxygen-18 ($^{18}\\text{O}$) isotopic labeling experiments:
1. **Primary Cycloaddition**: Ozone adds across the alkene double bond in a concerted $[3+2]$ cycloaddition to form the **primary ozonide (1,2,3-trioxolane / molozonide)**.
2. **Cycloreversion**: The molozonide is thermodynamically unstable due to the weak $\\text{O}-\\text{O}$ peroxo linkages. It undergoes an immediate retro-$[3+2]$ cycloreversion, cleaving both the central $\\text{C}-\\text{C}$ $\\sigma$ bond and an $\\text{O}-\\text{O}$ bond to generate:
   - A neutral **carbonyl compound** (aldehyde or ketone).
   - A zwitterionic **carbonyl oxide (Criegee intermediate)**:
     $$\\text{R}_2\\stackrel{\\oplus}{\\text{C}}-\\text{O}-\\stackrel{\\ominus}{\\text{O}} \\longleftrightarrow \\text{R}_2\\text{C}=\\stackrel{\\oplus}{\\text{O}}-\\stackrel{\\ominus}{\\text{O}} \\tag{3.15a}$$
3. **Recombination**: In non-participating solvents, the carbonyl oxide flips orientation and undergoes a second $[3+2]$ cycloaddition with the carbonyl fragment, forming the **secondary ozonide (1,2,4-trioxolane)**.
4. **Isotopic Proof**: When ozonolysis of an alkene is performed in the presence of an added aldehyde enriched with $^{18}\\text{O}$ at the carbonyl oxygen, the resulting 1,2,4-trioxolane incorporates the $^{18}\\text{O}$ label specifically into the ether bridge of the trioxolane ring. This confirmed that the original $\\text{C}-\\text{C}$ bond is completely severed during the cycloreversion step, ruling out any direct intramolecular migration!"""

    # --- UNIT 4 ENRICHMENT ---
    u4["sections"][2]["content"] += """

### Perturbational Molecular Orbital (PMO) Analysis of Diels-Alder Lewis Acid Catalysis

Under uncatalyzed conditions, the Diels-Alder reaction between 1,3-butadiene and methyl acrylate requires heating to $140^\\circ\\text{C}$ for 18 hours.
In the presence of catalytic aluminum trichloride ($\\text{AlCl}_3$) or boron trifluoride etherate ($\\text{BF}_3 \\cdot \\text{OEt}_2$), the reaction proceeds smoothly at **$0^\\circ\\text{C}$ in under 15 minutes**!

#### Frontier Molecular Orbital Analysis:
The reaction rate is inversely proportional to the energy gap between the interacting frontier orbitals:
$$\\text{Rate} \\propto \\frac{1}{E_{\\text{LUMO}}(\\text{dienophile}) - E_{\\text{HOMO}}(\\text{diene})} \\tag{4.4a}$$
1. **Coordination to Lewis Acid**: The Lewis acid coordinates to the carbonyl oxygen lone pair:
   $$\\text{CH}_2=\\text{CH}-\\text{C}(=\\text{O}\\cdots\\text{AlCl}_3)\\text{OMe} \\tag{4.4b}$$
2. **LUMO Lowering**: Coordination introduces strong positive polarization, pulling electron density out of the $\\pi$-system. The LUMO energy of the dienophile drops by an astonishing **$1.6\\text{ eV}$**!
3. **Orbital Gap Contraction**:
   $$\\Delta E_{\\text{gap}} = E_{\\text{LUMO}} - E_{\\text{HOMO}} \\; \\text{contracts from } 8.2\\text{ eV} \\to 6.6\\text{ eV} \\tag{4.4c}$$
   This dramatic narrowing of the FMO gap increases orbital overlap and reduces the activation energy barrier $\\Delta G^\\ddagger$ by $\\sim 35\\text{ kJ/mol}$, accelerating the reaction rate by more than six orders of magnitude ($10^6\\times$)!
4. **Regiochemical Enhancement**: Coordination also amplifies the asymmetry of the LUMO coefficients at the terminal carbon, boosting regioselectivity from an $80:20$ mixture to $>98:2$!"""

    # --- UNIT 5 ENRICHMENT ---
    u5["sections"][1]["content"] += """

### Analytical Trigonometric Proof of Hückel $(4n+2)$ Aromaticity

From the Frost circle formula $\\epsilon_k = \\alpha + 2\\beta \\cos\\left(\\frac{2\\pi k}{N}\\right)$ (recalling $\\beta < 0$):
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

    u5["sections"][6]["content"] += """

### The Dual-Parameter Swain-Lupton Equation

To deconvolve the inductive and resonance contributions of substituents, C. Gardner Swain and Elmer C. Lupton resolved the Hammett equation into independent **Field ($F$)** and **Resonance ($R$)** parameters:
$$\\log\\left(\\frac{k}{k_0}\\right) = f F + r R \\tag{5.19}$$
where:
- $F$ measures the pure through-space field / through-bond inductive electron withdrawal.
- $R$ measures the pure through-conjugation $\\pi$-resonance capability.
- $f$ and $r$ are sensitivity factors weighting the two effects in a specific reaction.

| Substituent | Field Constant ($F$) | Resonance Constant ($R$) | Net Electronic Directing |
| :---: | :---: | :---: | :---: |
| **$-\\text{NO}_2$** | $+0.65$ | $+0.13$ | Strong Deactivating, *meta* |
| **$-\\text{CN}$** | $+0.51$ | $+0.15$ | Strong Deactivating, *meta* |
| **$-\\text{CF}_3$** | $+0.38$ | $+0.16$ | Strong Deactivating, *meta* |
| **$-\\text{OCH}_3$** | $+0.29$ | **$-0.56$** | Activating, *ortho/para* (Resonance dominates) |
| **$-\\text{NH}_2$** | $+0.08$ | **$-0.74$** | Strong Activating, *ortho/para* |
| **$-\\text{CH}_3$** | $-0.01$ | $-0.14$ | Weak Activating, *ortho/para* |
| **$-\\text{F}$** | $+0.45$ | $-0.39$ | Deactivating, *ortho/para* (Field > Resonance) |
| **$-\\text{Cl}$** | $+0.42$ | $-0.19$ | Deactivating, *ortho/para* (Field > Resonance) |

Notice that for halogens ($\\text{F, Cl, Br}$), $F > |R|$: the positive field parameter dominates the ground-state electron density, causing deactivation, but the negative resonance parameter operates during arenium ion formation, directing substitution to *ortho* and *para*!"""

    # --- UNIT 6 ENRICHMENT ---
    u6["sections"][2]["content"] += """

### The Winstein Four-Stage Solvolysis Spectrum

In 1956, Saul Winstein formulated the comprehensive ion-pair solvolysis scheme to explain stereochemical outcomes in $S_N1$ and $E1$ reactions:
$$\\text{R}-\\text{X} \\xrightleftharpoons[k_{-1}]{k_1} [\\text{R}^+ \\, \\text{X}^-] \\xrightleftharpoons[k_{-2}]{k_2} [\\text{R}^+ \\| \\text{X}^-] \\xrightleftharpoons[k_{-3}]{k_3} \\text{R}^+ + \\text{X}^- \\tag{6.7a}$$
1. **Intimate (Contact) Ion Pair ($[\\text{R}^+ \\, \\text{X}^-]$)**:
   The covalent bond is severed, but the two ions remain in direct van der Waals contact inside a single solvent cage.
   - Attack by nucleophile at this stage occurs exclusively from the back face, resulting in **$100\\%$ inversion of configuration**.
   - Internal return ($k_{-1}$) can cause racemization of the starting alkyl halide without substitution!
2. **Solvent-Separated Ion Pair ($[\\text{R}^+ \\| \\text{X}^-]$)**:
   One or more solvent molecules have inserted between the carbocation and the leaving group.
   - Frontside attack is now partially possible, yielding **inversion with significant retention**.
3. **Free Solvated Ions ($\\text{R}^+ + \\text{X}^-$)**:
   The ions have diffused apart beyond mutual Coulomb attraction.
   - Attack is completely symmetrical from both faces, resulting in **complete racemization ($50:50$ enantiomer ratio)**.

#### The Special Salt Effect:
Adding non-nucleophilic lithium perchlorate ($\\text{LiClO}_4$) traps the solvent-separated ion pair:
$$[\\text{R}^+ \\| \\text{X}^-] + \\text{ClO}_4^- \\longrightarrow [\\text{R}^+ \\| \\text{ClO}_4^-] + \\text{X}^- \\tag{6.7b}$$
Perchlorate is a non-nucleophilic counter-ion, shutting down internal return ($k_{-2}$) and accelerating the rate of solvolysis. This 'special salt effect' confirmed Winstein's multi-stage ionization spectrum!"""

    u6["sections"][6]["content"] += """

### Stereochemical Models of Carbonyl Addition: Felkin-Anh Transition State

When a nucleophile or Grignard reagent attacks a chiral carbonyl compound possessing an adjacent stereocenter with substituents categorized by size (Large $L$, Medium $M$, Small $S$):
$$\\text{R}-\\text{CH}(L, M, S)-\\text{CHO} + \\text{R}'\\text{MgX} \\longrightarrow \\text{Chiral Alcohol} \\tag{6.17a}$$
The stereochemical outcome is governed by the **Felkin-Anh Model** (1968, 1976):
1. **Conformational Alignment**: The largest group ($L$) aligns perpendicular ($90^\\circ$) to the carbonyl $\\text{C}=\\text{O}$ double bond to maximize $\\sigma^*_{\\text{C}-L} \\to \\pi^*_{\\text{C}=\\text{O}}$ hyperconjugative stabilization.
2. **Bürgi-Dunitz Angle of Attack**: The incoming nucleophile approaches the carbonyl carbon at an obtuse angle of **$\\alpha_{\\text{BD}} \\approx 107^\\circ$** to maximize overlap with the $\\pi^*_{\\text{C}=\\text{O}}$ LUMO while minimizing repulsion with the oxygen lone pairs.
3. **Steric Trajectory**: The nucleophile attacks from the face bearing the **Small ($S$) substituent** rather than the Medium ($M$) substituent.
This transition-state model accurately predicts the diastereomeric ratio and absolute configuration of major alcohol products across hundreds of complex natural product syntheses!"""

    # --- UNIT 7 ENRICHMENT ---
    u7["sections"][3]["content"] += """

### The Claisen Rearrangement of Allyl Aryl Ethers ([3,3]-Sigmatropic Shift)

Discovered in 1912 by Ludwig Claisen, heating an allyl aryl ether ($\\text{Ar}-\\text{O}-\\text{CH}_2-\\text{CH}=\\text{CH}_2$) to $200^\\circ\\text{C}$ in the absence of any catalyst induces a clean unimolecular transformation to an **ortho-allylphenol**:
$$\\text{C}_6\\text{H}_5-\\text{O}-\\text{CH}_2-\\text{CH}=\\text{CH}_2 \\xrightarrow{200^\\circ\\text{C}} o\\text{-}\\text{Allylphenol} \\tag{7.9a}$$

#### Complete Mechanism:
1. **Concerted [3,3]-Sigmatropic Shift**: The reaction proceeds through a cyclic, six-membered **chair-like pericyclic transition state**:
   $$\\left[ \\begin{matrix} \\text{C}_6 & - & \\text{C}_1 \\\\ \\vert & & \\vert \\\\ \\text{O} & \\cdots & \\text{C}_\\gamma \\\\ \\vert & & \\vert \\\\ \\text{C}_\\alpha & = & \\text{C}_\\beta \\end{matrix} \\right]^\\ddagger \\tag{7.9b}$$
   Simultaneous cleavage of the $\\text{O}-\\text{C}_\\alpha$ $\\sigma$ bond and formation of a new $\\text{C}_{\\text{ortho}}-\\text{C}_\\gamma$ $\\sigma$ bond occurs with complete inversion of the allyl fragment (the terminal $\\gamma$-carbon attaches to the ring).
2. **Formation of 6-Allylcyclohexadienone**: The pericyclic shift generates a non-aromatic ketone intermediate:
   $$\\text{Cyclohexa-2,4-dien-1-one}$$
3. **Rapid Enolization / Rearomatization**: The keto intermediate undergoes rapid tautomerization (loss of the *ortho*-proton to oxygen), driven by the restoration of aromatic resonance energy ($151\\text{ kJ/mol}$), yielding pure **2-allylphenol** in $>90\\%$ yield.
If both *ortho* positions are blocked by substituents (e.g., in 2,6-dimethylphenyl allyl ether), the 6-allyl intermediate cannot enolize; it undergoes a **second [3,3]-sigmatropic shift** from the *ortho* carbon to the *para* carbon, followed by enolization to yield the **para-allylphenol**!"""

    # --- UNIT 8 ENRICHMENT ---
    u8["sections"][2]["content"] += """

### Quantitative Frontier Molecular Orbital (FMO) Coefficients of Pyrrole

Applying Hückel Molecular Orbital theory with heteroatom parameters for nitrogen ($\\alpha_{\\text{N}} = \\alpha + 1.5\\beta, \\; \\beta_{\\text{C}-\\text{N}} = 0.8\\beta$):
The Highest Occupied Molecular Orbital (HOMO, $\\Psi_3$) and Lowest Unoccupied Molecular Orbital (LUMO, $\\Psi_4$) have the following orbital coefficients across the ring atoms:

| Atom | HOMO Coefficient ($c_r$) | $\\pi$-Electron Charge ($q_r$) | Wheland Energy $\\Delta E^\\ddagger$ (kJ/mol) |
| :---: | :---: | :---: | :---: |
| **N1** | $0.000$ | $1.64$ | N/A |
| **C2 ($\\alpha$)**| **$0.602$** | **$1.09$** | **$48.2$ (Lowest Barrier, Favored)** |
| **C3 ($\\beta$)** | $0.372$ | $1.04$ | $74.5$ (Higher Barrier) |
| **C4 ($\\beta$)** | $-0.372$ | $1.04$ | $74.5$ |
| **C5 ($\\alpha$)**| **$-0.602$** | **$1.09$** | **$48.2$ (Favored)** |

Notice that the **HOMO coefficient at C2 ($0.602$) is vastly larger than at C3 ($0.372$)**.
Because the electrophile interacts with the HOMO of the $\\pi$-excessive ring, the second-order perturbation interaction energy is proportional to the square of the orbital coefficient:
$$\\Delta E_{\\text{HOMO}} \\propto c_r^2 \\implies \\frac{(0.602)^2}{(0.372)^2} = \\frac{0.362}{0.138} \\approx \\mathbf{2.62} \\tag{8.9a}$$
Frontier orbital overlap favors electrophilic attack at C2 by nearly a factor of three over C3, reinforcing the thermodynamic stability of the three-contributor Wheland intermediate!"""

    u8["sections"][5]["content"] += """

### Complete Hückel Secular Determinant & Charge Distribution of Pyridine

For pyridine, nitrogen is more electronegative than carbon, parameterized in Hückel theory by:
$$\\alpha_{\\text{N}} = \\alpha + 0.5\\beta, \\quad \\beta_{\\text{C}-\\text{N}} = \\beta \\tag{8.13a}$$
Solving the $6 \\times 6$ secular determinant yields the $\\pi$-electron charge densities at each carbon:
$$q(\\text{N1}) = 1.20, \\quad q(\\text{C2, C6}) = 0.92, \\quad q(\\text{C3, C5}) = 1.01, \\quad q(\\text{C4}) = 0.94 \\tag{8.13b}$$
Subtracting $1.0$ from each atom gives the net $\\pi$-charge:
- **N1**: $-0.20$ (Excess electron density)
- **C2 & C6 ($\\alpha$)**: **$+0.08$** (Electron deficient)
- **C3 & C5 ($\\beta$)**: $-0.01$ (Nearly neutral)
- **C4 ($\\gamma$)**: **$+0.06$** (Electron deficient)

#### Fundamental Discoveries:
1. **Why EAS Avoids C2 and C4**: C2 and C4 possess positive net $\\pi$-charges ($+0.08$ and $+0.06$). Electrophiles ($E^+$) are repelled electrostatically from these positions. C3 is the only carbon with zero positive charge.
2. **Why Nucleophiles Attack C2 and C4**: In the Chichibabin amination and organolithium additions, nucleophiles ($\\text{Nu}^-$) attack the carbons bearing **maximum partial positive charge (C2 and C4)**!"""

    print("All units deeply enriched.")
    return [u1, u2, u3, u4, u5, u6, u7, u8]

if __name__ == "__main__":
    units = enrich_all()
    
    course_data = {
        "courseCode": "",
        "courseTitle": "Organic Chemistry I: Molecular Architecture, Hydrocarbons, Haloalkanes, Oxygen/Sulfur Systems & Fundamental Heterocycles",
        "courseSubtitle": "Quantum Electronic Structure of Carbon, Hybridization & Coulson's Theorem, Alkane & Cycloalkane Conformational Dynamics, Alkene Stereospecific Additions & Criegee Cleavages, Conjugated Dienes & Diels-Alder FMO Theory, Aromaticity & Wheland EAS Regiochemistry, Nucleophilic Substitutions & Eliminations, Oxygen/Sulfur Functionalities, and Fundamental Heteroaromatics",
        "credits": 4,
        "lectureHours": 60,
        "prerequisites": "General Chemistry, Chemical Bonding Foundations & Introductory Reaction Energetics",
        "description": "Comprehensive university honors master digital textbook on Organic Chemistry I: quantum electronic configuration of carbon, valence bond hybridization, Coulson's theorem, molecular orbital theory of sigma and pi bonds, bond polarization, electric dipole moments, resonance delocalization, and curved-arrow formalisms; alkanes and cycloalkanes, constitutional isomerism, combustion thermodynamics, octane ratings, free-radical halogenation energetics, Hammond's postulate, carbene insertions, Baeyer angle strain theory, cyclohexane chair conformational equilibria, Winstein-Holness A-values, 1,3-diaxial interactions, bicycloalkanes, Bredt's rule, and Wurtz coupling; alkenes, index of hydrogen deficiency, Cahn-Ingold-Prelog E/Z priority rules, E2 and E1 elimination mechanisms, Zaitsev and Hofmann regioselectivity, electrophilic additions, Markovnikov's rule, carbocation rearrangements, stereospecific anti-bromination via cyclic bromonium ions, hydration protocols (acid-catalyzed, oxymercuration-demercuration, hydroboration-oxidation), Criegee ozonolysis mechanism, peracid epoxidation, syn-dihydroxylation, and coordination polymerization; conjugated dienes, 1,2- vs 1,4-additions under kinetic vs thermodynamic control, frontier molecular orbital theory, Diels-Alder [4+2] cycloaddition, Alder endo rule, secondary orbital overlap, diene elastomers, alkynes, sp hybridization acidity, acetylide alkylations, keto-enol tautomerism, and stereoselective reductions (Lindlar vs dissolving metal); benzene structure, resonance stabilization energy, Hückel (4n+2) pi-electron rule, Frost circle polygon mnemonics, annulenes, aromatic ions, non-benzenoid aromatics, electrophilic aromatic substitution, Wheland arenium sigma-complex intermediates, halogenation, nitration, sulfonation, Friedel-Crafts alkylation and acylation, substituent directing and activating effects, and Hammett linear free-energy relationships; alkyl and aryl halides, leaving group ability, SN2 bimolecular kinetics, Walden inversion, SN1 unimolecular solvolysis, ion pairs, E2 anti-periplanar elimination, E1 and E1cB mechanisms, competitive reaction decision matrices, SNAr addition-elimination via Meisenheimer complexes, elimination-addition via benzyne intermediates, and Grignard organometallic reagents; alcohols, phenols, ethers, epoxides, and sulfides, hydrogen bonding, acid-base amphoterism, phenol resonance stabilization, conversion to halides via SNi, oxidation levels, Pinacol-Pinacolone rearrangements, Malaprade periodate glycol cleavage, Kolbe-Schmitt carboxylation, Reimer-Tiemann formylation, Bakelite polymers, Williamson ether synthesis, crown ether supramolecular cation complexation, and acidic vs basic epoxide ring opening regiochemistry; and fundamental heterocycles, heteroaromaticity criteria, pi-excessive vs pi-deficient classifications, Paal-Knorr syntheses, pyrrole, furan, and thiophene electronic structures and C2 vs C3 EAS regioselectivity, pyridine electronic structure and basicity, extreme electrophilic deactivation, nucleophilic Chichibabin amination, and pyridine N-oxide synthetic activation. Features 8 interactive 60 FPS Canvas simulations and 32 tiered solved problems with complete line-by-line mathematical and mechanistic proofs.",
        "units": units
    }

    json_str = json.dumps(course_data, indent=2)
    js_content = f"// Organic Chemistry I Master Textbook Data File\n// STRICT CONSTRAINT: ZERO PROHIBITED CODES PERMITTED\nwindow.COURSE_DATA = {json_str};\n"

    # Strict compliance check for banned patterns
    banned_patterns = [
        r'\bchem\s*\d+',
        r'70\s*\+\s*20\s*\+\s*10',
        r'\b\d+\s*Marks\b',
        r'100\s*Marks',
        r'exam(ination)?\s+marks',
        r'\bgrades?\s*=\s*\d+'
    ]
    
    for pat in banned_patterns:
        matches = re.findall(pat, js_content, re.IGNORECASE)
        if matches:
            print(f"WARNING: Prohibited course number or marks pattern '{pat}': {matches[:5]}")
            assert False, f"Banned pattern found: {matches}"

    output_filename = "organic-chemistry-1-data.js"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully generated {output_filename}")
    words = len(js_content.split())
    chars = len(js_content)
    print(f"Data file stats: {words:,} words | {chars:,} characters | {len(course_data['units'])} units")
