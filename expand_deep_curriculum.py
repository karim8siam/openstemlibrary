# Python script to build the complete, deep Organic Chemistry I course data
# Targeting ~65,000+ words in the data file to surpass the 2x depth requirement (>80,000 words total)
import json
import re
from expand_all_units import enrich_all

def main():
    print("Building full depth curriculum for Organic Chemistry I...")
    units = enrich_all()

    # Deep expansions for each unit's sections to achieve massive honors-level depth (>65,000 words)
    
    # --- Extra expansion for Unit 1 ---
    u1 = units[0]
    u1["sections"][1]["content"] += """

### Formal Charge vs Oxidation State: A Rigorous Chemical Contrast

A common source of confusion in organic chemistry is the distinction between **Formal Charge ($FC$)** and **Oxidation State ($OS$)**:
1. **Formal Charge**: Assumes perfectly covalent, strictly equal sharing of all electrons in every covalent bond, regardless of electronegativity differences:
   $$FC = V - N_{\\text{lone}} - \\frac{1}{2} N_{\\text{bonding}} \\tag{1.6a}$$
2. **Oxidation State**: Assumes that every covalent bond is completely ionic, assigning all shared electrons in a bond entirely to the more electronegative bonded atom:
   $$OS = V - N_{\\text{lone}} - N_{\\text{assigned ionic}} \\tag{1.6b}$$

#### Comparison Across the C1 Oxidation Series:
Consider the five canonical one-carbon organic compounds:

| Compound | Formula | Lewis Structure Properties | Formal Charge on C | Oxidation State of C |
| :---: | :---: | :---: | :---: | :---: |
| **Methane** | $\\text{CH}_4$ | 4 single $\\text{C}-\\text{H}$ bonds | **$0$** | **$-4$** (Carbon more electronegative than H) |
| **Methanol**| $\\text{CH}_3\\text{OH}$ | 3 $\\text{C}-\\text{H}$, 1 $\\text{C}-\\text{O}$ | **$0$** | **$-2$** (Loses 2 $e^-$ to Oxygen) |
| **Formaldehyde**| $\\text{H}_2\\text{C}=\\text{O}$ | 2 $\\text{C}-\\text{H}$, 1 $\\text{C}=\\text{O}$ | **$0$** | **$0$** |
| **Formic Acid** | $\\text{HCOOH}$ | 1 $\\text{C}-\\text{H}$, 1 $\\text{C}=\\text{O}$, 1 $\\text{C}-\\text{O}$ | **$0$** | **$+2$** |
| **Carbon Dioxide**| $\\text{CO}_2$ | 2 $\\text{C}=\\text{O}$ double bonds | **$0$** | **$+4$** (Fully oxidized carbon) |

Notice that while the formal charge on carbon remains identically **zero ($0$)** across all five neutral compounds, the oxidation state ranges across eight units from **$-4$ in methane to $+4$ in carbon dioxide**.
- Reductions in organic chemistry (e.g., adding $\\text{H}_2$ or hydrides) decrease the oxidation state of carbon.
- Oxidations (e.g., adding oxygen or removing hydrogen) increase the oxidation state of carbon."""

    u1["sections"][4]["content"] += """

### The Debye-Langevin Classical Formulation of Molecular Polarization

In dielectric media, the molar polarization $P_m$ of a gas or dilute solution of polar molecules is described by the **Debye-Langevin Equation**:
$$P_m = \\frac{\\varepsilon_r - 1}{\\varepsilon_r + 2} \\frac{M}{\\rho} = \\frac{N_A}{3\\varepsilon_0} \\left( \\alpha + \\frac{\\mu^2}{3 k_B T} \\right) \\tag{1.28a}$$
where:
- $\\varepsilon_r$ is the relative permittivity (dielectric constant) of the medium.
- $M$ is molar mass, $\\rho$ is mass density, and $N_A$ is Avogadro's constant.
- $\\alpha$ is the temperature-independent electronic and atomic polarizability.
- $\\mu$ is the permanent electric dipole moment of the molecule.
- $k_B T$ is thermal energy, which randomizes dipole orientation against the external electric field.

Plotting experimental molar polarization $P_m$ versus reciprocal absolute temperature ($1/T$) yields a straight line:
$$P_m = A + \\frac{B}{T} \\tag{1.28b}$$
- The $y$-intercept ($A = \\frac{N_A \\alpha}{3\\varepsilon_0}$) yields the intrinsic electronic polarizability $\\alpha$.
- The slope ($B = \\frac{N_A \\mu^2}{9\\varepsilon_0 k_B}$) yields the **exact permanent molecular dipole moment $\\mu$**!

#### Dipole Moments of Substituted Haloethanes & Conformational Gauche Balance:
In 1,2-dichloroethane, the dipole moment in non-polar benzene is temperature dependent:
$$\\bar{\\mu}(T) = \\sqrt{x_{\\text{anti}}(T) \\mu_{\\text{anti}}^2 + x_{\\text{gauche}}(T) \\mu_{\\text{gauche}}^2} \\tag{1.28c}$$
Because $\\mu_{\\text{anti}} = 0.0\\text{ D}$ and $\\mu_{\\text{gauche}} \\approx 3.10\\text{ D}$, measuring $\\bar{\\mu}$ as a function of temperature provides an experimental method to measure the conformational equilibrium constant $K = [\\text{gauche}] / [\\text{anti}]$ and extract the thermodynamic parameters $\\Delta H^\\circ$ and $\\Delta S^\\circ$ directly!"""

    # --- Extra expansion for Unit 2 ---
    u2 = units[1]
    u2["sections"][0]["content"] += """

### Combinatorial Graph Theory of Isomer Enumeration: Pólya's Theorem

The number of constitutional isomers of acyclic alkanes ($\\text{C}_n\\text{H}_{2n+2}$) corresponds mathematically to the number of non-isomorphic rooted and unrooted trees with $n$ vertices of maximal degree 4.
In 1937, Hungarian mathematician George Pólya developed the **Pólya Enumeration Theorem** using cycle indices of permutation groups:
Let $T(x) = \\sum_{n=1}^\\infty t_n x^n$ be the generating function for rooted carbon trees.
By treating the central carbon as a root with four equivalent branch sites under the symmetric group $S_4$:
$$T(x) = x \\cdot Z(S_4; T(x), T(x^2), T(x^3), T(x^4)) + x \\tag{2.1a}$$
where the cycle index of the symmetric group $S_4$ on four objects is:
$$Z(S_4) = \\frac{1}{24} (s_1^4 + 6 s_1^2 s_2 + 8 s_1 s_3 + 3 s_2^2 + 6 s_4) \\tag{2.1b}$$
Substituting and solving recursively yields the exact counts:
- $n = 1$: $1$ (methane)
- $n = 5$: $3$ (pentanes)
- $n = 10$: $75$ (decanes)
- $n = 20$: $366,319$ (eicosanes)
- $n = 30$: $4,111,846,763$
- $n = 40$: $62,481,801,147,341$ (Over sixty-two trillion isomers!)
This exponential combinatorial explosion highlights why rigorous systematic IUPAC nomenclature is essential: without systematic topological rules, communicating organic structures would be impossible."""

    u2["sections"][4]["content"] += """

### Molecular Mechanics Force-Field Parameterization of Ring Strain (MM3)

In computational organic chemistry (Norman Allinger), the total steric strain energy $E_{\\text{strain}}$ of a cyclic hydrocarbon is decomposed into four fundamental potential energy terms:
$$E_{\\text{strain}} = E_{\\text{stretch}} + E_{\\text{bend}} + E_{\\text{torsion}} + E_{\\text{non-bonded}} \\tag{2.10a}$$
1. **Bond Length Stretching ($E_{\\text{stretch}}$)**:
   $$E_{\\text{stretch}} = \\frac{1}{2} \\sum_{\\text{bonds}} k_r (r - r_0)^2 \\tag{2.10b}$$
   where $k_r \\approx 310\\text{ kcal}\\cdot\\text{mol}^{-1}\\cdot\\text{\u00c5}^{-2}$ is the force constant, and $r_0 = 1.538\\text{ \u00c5}$ is the equilibrium $\\text{C}-\\text{C}$ bond length.
2. **Bond Angle Bending ($E_{\\text{bend}}$)**:
   $$E_{\\text{bend}} = \\frac{1}{2} \\sum_{\\text{angles}} k_\\theta (\\theta - \\theta_0)^2 [1 - k'(\\theta - \\theta_0)] \\tag{2.10c}$$
   where $k_\\theta \\approx 0.45\\text{ kcal}\\cdot\\text{mol}^{-1}\\cdot\\text{deg}^{-2}$, and $\\theta_0 = 109.47^\\circ$. In cyclopropane, the internal angle of $60^\\circ$ produces $\\sim 115\\text{ kJ/mol}$ of angle strain.
3. **Torsional (Pitzer) Strain ($E_{\\text{torsion}}$)**:
   $$E_{\\text{torsion}} = \\frac{1}{2} \\sum_{\\text{dihedrals}} V_3 (1 + \\cos 3\\phi) \\tag{2.10d}$$
   Eclipsed $\\text{C}-\\text{H}$ bonds contribute $\\sim 4.0\\text{ kJ/mol}$ each. Cyclopropane has six pairs of fully eclipsed $\\text{C}-\\text{H}$ bonds, adding $6 \\times 4.0 = 24.0\\text{ kJ/mol}$ of torsional strain.
4. **Non-Bonded van der Waals Interactions ($E_{\\text{non-bonded}}$)**:
   Evaluated using the Buckingham (exp-6) or Lennard-Jones potential:
   $$E_{\\text{vdW}} = \\sum_{i < j} \\varepsilon \\left[ \\left(\\frac{r_0}{r_{ij}}\\right)^{12} - 2 \\left(\\frac{r_0}{r_{ij}}\\right)^6 \\right] \\tag{2.10e}$$
   In medium rings ($C_7 - C_{11}$, such as cyclodecane), transannular Prelog strain between cross-ring interior hydrogens contributes $40-60\\text{ kJ/mol}$ of steric destabilization."""

    # --- Extra expansion for Unit 3 ---
    u3 = units[2]
    u3["sections"][1]["content"] += """

### Stereoselective Syn-Eliminations: Chugaev & Cope Pyrolyses

While standard $E2$ elimination strictly requires an anti-periplanar geometry ($\phi = 180^\circ$), certain thermal eliminations proceed with **strict stereospecific syn-periplanar geometry ($\phi = 0^\circ$)** through cyclic pericyclic transition states:

1. **The Chugaev Reaction (Xanthate Pyrolysis)**:
   Discovered by Lev Chugaev in 1899, an alcohol is converted into a methyl xanthate ester, which undergoes thermal syn-elimination upon heating to $120-160^\\circ\\text{C}$:
   $$\\text{R}-\\text{OH} \\xrightarrow{1.\\; \\text{NaH} \\quad 2.\\; \\text{CS}_2 \\quad 3.\\; \\text{CH}_3\\text{I}} \\text{R}-\\text{O}-\\text{C}(=\\text{S})\\text{SCH}_3 \\; (\\text{Xanthate}) \\tag{3.5a}$$
   Heating causes a six-membered cyclic transition state where the thiocarbonyl sulfur abstracts the $\\beta$-hydrogen from the **same face (syn-elimination)**:
   $$\\left[ \\begin{matrix} \\text{C}_\\beta & - & \\text{C}_\\alpha \\\\ \\vert & & \\vert \\\\ \\text{H} & \\cdots & \\text{O} \\\\ \\vdots & & \\vert \\\\ \\text{S} & = & \\text{C}-\\text{SCH}_3 \\end{matrix} \\right]^\\ddagger \\longrightarrow \\text{Alkene} + \\text{COS}(g) + \\text{CH}_3\\text{SH}(g) \\tag{3.5b}$$
   - **Advantage**: Zero carbocation rearrangements; operates under neutral thermal conditions.
2. **The Cope Elimination (Amine Oxide Pyrolysis)**:
   Tertiary amines are oxidized with $\\text{H}_2\\text{O}_2$ or $m$CPBA to amine oxides, which undergo clean syn-elimination at $80-120^\\circ\\text{C}$ through a planar five-membered cyclic transition state:
   $$\\text{R}_2\\text{CH}-\\text{CH}_2-\\text{N}^+(\\text{O}^-)\\text{Me}_2 \\xrightarrow{\\Delta} \\text{R}_2\\text{C}=\\text{CH}_2 + \\text{Me}_2\\text{N-OH} \\tag{3.5c}$$
   Proceeds with exceptional stereochemical fidelity, yielding Hofmann alkenes under mild conditions."""

    u3["sections"][6]["content"] += """

### The Cossee-Arlman Mechanism of Coordination Polymerization

The extraordinary stereochemical control of heterogeneous Ziegler-Natta catalysts ($\\alpha-\\text{TiCl}_3 / \\text{AlEt}_3$) and homogeneous metallocene catalysts ($Cp_2\\text{ZrCl}_2 / \\text{MAO}$) is governed by the **Cossee-Arlman Mechanism**:
1. **Active Site Architecture**: The active catalyst site is an octahedral titanium(III) center anchored to a crystal face, possessing four bridging chloride ligands, one alkyl polymer chain ($\\text{P}$), and one **vacant coordination site ($\square$)**:
   $$[\\text{TiCl}_4(\\text{P})(\\square)] \\tag{3.17a}$$
2. **Alkene Coordination**: The alkene monomer coordinates to the vacant site via its $\\pi$ electrons, forming a $\\pi$-complex with the titanium atom:
   $$[\\text{TiCl}_4(\\text{P})(\\eta^2-\\text{CH}_2=\\text{CHR})] \\tag{3.17b}$$
3. **Migratory Insertion**: The coordinated alkene inserts into the titanium-carbon $\\sigma$ bond via a four-membered cyclic transition state:
   $$\\left[ \\begin{matrix} \\text{Ti} & - & \\text{P} \\\\ \\vert & & \\vdots \\\\ \\text{CH}_2 & = & \\text{CHR} \\end{matrix} \\right]^\\ddagger \\longrightarrow [\\text{TiCl}_4(\\text{CH}_2\\text{CHR}-\\text{P})(\\square)] \\tag{3.17c}$$
   - The growing polymer chain migrates to the coordinated monomer, regenerating a vacant coordination site at the opposite position.
   - In stereospecific $C_2$-symmetric zirconocene catalysts, the chiral ligand framework forces propene to approach exclusively with its *si*-face (or *re*-face), inserting every single monomer with identical stereochemical orientation to produce **isotactic polypropylene** with crystalline melting points exceeding $165^\\circ\\text{C}$!"""

    # --- Extra expansion for Unit 4 ---
    u4 = units[3]
    u4["sections"][0]["content"] += """

### Hückel Orbital Matrices & Bond Orders for Linear Polyenes

For a general linear conjugated polyene with $N$ carbon atoms (e.g., 1,3-butadiene $N=4$; 1,3,5-hexatriene $N=6$), the analytical eigenvalues and normalized eigenvectors are given by:
$$\\epsilon_j = \\alpha + 2\\beta \\cos\\left(\\frac{j\\pi}{N+1}\\right), \\quad j = 1, 2, \\dots, N \\tag{4.2a}$$
$$c_{jr} = \\sqrt{\\frac{2}{N+1}} \\sin\\left(\\frac{j r \\pi}{N+1}\\right), \\quad r = 1, 2, \\dots, N \\tag{4.2b}$$

#### Molecular Orbital Energy Spectrum of 1,3,5-Hexatriene ($N=6$, $6\\pi$ electrons):
1. $j=1$: $\\epsilon_1 = \\alpha + 2\\beta \\cos(\\pi/7) = \\alpha + 1.802\\beta$ (Bonding)
2. $j=2$: $\\epsilon_2 = \\alpha + 2\\beta \\cos(2\\pi/7) = \\alpha + 1.247\\beta$ (Bonding)
3. $j=3$: $\\epsilon_3 = \\alpha + 2\\beta \\cos(3\\pi/7) = \\alpha + 0.445\\beta$ (Bonding, **HOMO**)
4. $j=4$: $\\epsilon_4 = \\alpha + 2\\beta \\cos(4\\pi/7) = \\alpha - 0.445\\beta$ (Antibonding, **LUMO**)
5. $j=5$: $\\epsilon_5 = \\alpha + 2\\beta \\cos(5\\pi/7) = \\alpha - 1.247\\beta$ (Antibonding)
6. $j=6$: $\\epsilon_6 = \\alpha + 2\\beta \\cos(6\\pi/7) = \\alpha - 1.802\\beta$ (Antibonding)

Total $\\pi$-electron energy:
$$E_\\pi = 2(\\epsilon_1 + \\epsilon_2 + \\epsilon_3) = 6\\alpha + 6.988\\beta \\tag{4.2c}$$
Reference: Three isolated double bonds ($6\\alpha + 6\\beta$):
$$E_{\\text{deloc}} = 0.988|\\beta| \\approx 31.6\\text{ kJ}\\cdot\\text{mol}^{-1} \\tag{4.2d}$$

#### Coulson $\\pi$-Bond Orders:
The $\\pi$-bond order $p_{rs}$ between adjacent carbons $r$ and $s$ is:
$$p_{rs} = \\sum_{j=1}^{\\text{occ}} n_j c_{jr} c_{js} \\tag{4.2e}$$
For 1,3-butadiene ($N=4$):
- $p_{12} = p_{34} = 2(0.372)(0.602) + 2(0.602)(0.372) = \\mathbf{0.894}$ (Strong double bond character)
- $p_{23} = 2(0.602)(0.602) + 2(0.372)(-0.372) = \\mathbf{0.447}$ (Significant partial double bond character!)
The theoretical bond length calculated via the Coulson-Saldick formula $R(p) = 1.54 - 0.20 p$ gives $R_{23} = 1.54 - 0.20(0.447) = 1.45\\text{ \u00c5}$, in extraordinary agreement with the experimental electron diffraction value ($1.463\\text{ \u00c5}$)."""

    # --- Extra expansion for Unit 5 ---
    u5 = units[4]
    u5["sections"][4]["content"] += """

### Marcus Electron Transfer Theory of Arenium Ion Formation

In modern physical organic chemistry (J. K. Kochi), the rate-determining step of Electrophilic Aromatic Substitution:
$$\\text{ArH} + \\text{E}^+ \\xrightarrow{k_1} [\\text{Ar}(\\text{H})\\text{E}]^+ \\; (\\sigma\\text{-complex})$$
often proceeds through an initial transient outer-sphere charge-transfer complex ($\\pi$-complex) that undergoes electron transfer:
$$\\text{ArH} + \\text{E}^+ \\xrightleftharpoons[K_{\\pi}]{} [\\text{ArH}, \\text{E}^+]_\\pi \\xrightarrow{k_{\\text{ET}}} [\\text{ArH}^{\\bullet+}, \\text{E}^\\bullet] \\longrightarrow [\\text{Ar}(\\text{H})\\text{E}]^+_\\sigma \\tag{5.8a}$$
Applying the **Marcus Theory of Electron Transfer**:
$$\\Delta G^\\ddagger = \\frac{\\lambda}{4} \\left( 1 + \\frac{\\Delta G^\\circ}{\\lambda} \\right)^2 \\tag{5.8b}$$
where $\\lambda$ is the solvent and inner-sphere reorganization energy, and $\\Delta G^\\circ$ is the standard free energy of electron transfer determined by the ionization potential of the arene ($IP$) and electron affinity of the electrophile ($EA$):
$$\\Delta G^\\circ \\approx IP(\\text{ArH}) - EA(\\text{E}^+) - e^2 / (4\\pi\\varepsilon_0 r) \\tag{5.8c}$$
This electron-transfer framework directly explains why electrophilic reactivity correlates linearly with the **ionization potentials of arenes** ($r^2 > 0.98$) across diverse substituted benzenes and polycyclic aromatic hydrocarbons!"""

    u5["sections"][5]["content"] += """

### The Industrial Cumene Hydroperoxide Process for Phenol Synthesis

Discovered by Heinrich Hock in 1944, over $90\\%$ of global phenol and acetone is manufactured via the **Cumene Process**, an elegant synthesis demonstrating Friedel-Crafts alkylation, free-radical autoxidation, and acid-catalyzed carbocation rearrangement:

1. **Step 1: Friedel-Crafts Alkylation**:
   Benzene is alkylated with propene over solid acid catalysts (zeolite H-ZSM-5) at $200^\\circ\\text{C}$ to synthesize cumene (isopropylbenzene):
   $$\\text{C}_6\\text{H}_6 + \\text{CH}_3\\text{CH}=\\text{CH}_2 \\xrightarrow{\\text{zeolite}} \\text{C}_6\\text{H}_5-\\text{CH}(\\text{CH}_3)_2 \\tag{5.15a}$$
2. **Step 2: Free-Radical Autoxidation**:
   Air is bubbled through cumene at $100^\\circ\\text{C}$. The weak tertiary benzylic $\\text{C}-\\text{H}$ bond ($\text{BDE} \\approx 355\\text{ kJ/mol}$) undergoes radical chain autoxidation to form **cumene hydroperoxide**:
   $$\\text{C}_6\\text{H}_5-\\text{CH}(\\text{CH}_3)_2 + \\text{O}_2 \\longrightarrow \\text{C}_6\\text{H}_5-\\text{C}(\\text{CH}_3)_2-\\text{O}-\\text{O}-\\text{H} \\tag{5.15b}$$
3. **Step 3: The Hock Rearrangement (Acid-Catalyzed Cleavage)**:
   Treatment with dilute sulfuric acid protonates the terminal hydroperoxide oxygen. Loss of water generates an electron-deficient oxygen intermediate ($[\\text{Ph}-\\text{CMe}_2-\\text{O}^+]$).
   - **Phenyl Migration**: The phenyl group migrates with its electron pair from carbon to oxygen with exceptional migratory aptitude:
     $$\\text{Ph}-\\text{C}(\\text{Me})_2-\\text{O}^+ \\longrightarrow \\stackrel{\\oplus}{\\text{C}}(\\text{Me})_2-\\text{O}-\\text{Ph} \\tag{5.15c}$$
   - Hydration by water yields a hemiketal, which collapses into **Phenol** and **Acetone**:
     $$\\text{Hemiketal} \\longrightarrow \\mathbf{\\text{C}_6\\text{H}_5\\text{OH}} + \\mathbf{\\text{CH}_3\\text{COCH}_3} \\tag{5.15d}$$
Both valuable products are co-generated in near quantitative yields with zero halogen waste!"""

    # --- Extra expansion for Unit 6 ---
    u6 = units[5]
    u6["sections"][1]["content"] += """

### Super-Leaving Groups: Triflates, Nonaflates & The $pK_a$ Frontier

While halides ($\\text{Cl}^-, \\text{Br}^-, \\text{I}^-$) are standard leaving groups, modern organic synthesis requires **super-leaving groups** that react up to $10^8$ times faster:
1. **Trifluoromethanesulfonate (Triflate, $-\\text{OTf}$)**:
   $$\\text{CF}_3\\text{SO}_2\\text{O}^- \\quad (pK_a \\approx -14.0) \\tag{6.1a}$$
   Triflate is $10^5$ times more reactive than tosylate ($\\text{OTs}^-$) and $10^6$ times more reactive than bromide. The three strongly electron-withdrawing fluorine atoms pull electron density inductively into the sulfonate moiety, dispersing negative charge across three oxygens and the $\\text{CF}_3$ group.
2. **Nonafluorobutanesulfonate (Nonaflate, $-\\text{ONf}$)**:
   $$\\text{CF}_3\\text{CF}_2\\text{CF}_2\\text{CF}_2\\text{SO}_2\\text{O}^- \\quad (pK_a \\approx -14.5) \\tag{6.1b}$$
3. **Aryl Triflates in Cross-Coupling**:
   While aryl chlorides and bromides are unreactive toward many transitions metals, aryl triflates (prepared effortlessly from phenols: $\\text{ArOH} + \\text{Tf}_2\\text{O} \\xrightarrow{\\text{pyridine}} \\text{ArOTf}$) undergo facile oxidative addition into palladium(0) complexes, serving as indispensable electrophilic partners in Suzuki-Miyaura, Heck, and Stille couplings!"""

    u6["sections"][6]["content"] += """

### The Felkin-Anh Transition State vs Cram's Chelate Model

When chiral $\\alpha$-substituted aldehydes react with organometallic reagents ($\\text{RMgX}$ or $\\text{RLi}$), the stereochemical induction depends critically on whether the $\\alpha$-substituent can coordinate with the metal cation:

1. **Non-Chelating Regime (Felkin-Anh Model)**:
   When the $\\alpha$-substituents are alkyl, aryl, or non-coordinating groups, the reaction proceeds through the open Felkin-Anh transition state:
   - The large group ($L$) is oriented perpendicular to the carbonyl $\\text{C}=\\text{O}$ axis.
   - The nucleophile attacks from the least hindered trajectory along the Bürgi-Dunitz angle ($107^\\circ$) past the Small ($S$) substituent.
2. **Chelating Regime (Cram's Chelation-Controlled Model)**:
   When the $\\alpha$-carbon bears a heteroatom with a coordinating lone pair (such as $-\\text{OCH}_3, -\\text{OBn}, -\\text{NMe}_2$):
   - The bivalent metal cation (e.g., $\\text{Mg}^{2+}$ in $\\text{RMgX}$ or added Lewis acids like $\\text{TiCl}_4, \\text{CeCl}_3$) coordinates simultaneously to the **carbonyl oxygen AND the $\\alpha$-heteroatom**, locking the substrate into a rigid **five-membered chelate ring**:
     $$\\left[ \\begin{matrix} \\text{C}=\\text{O} & \\cdots & \\text{Mg}^{2+} \\\\ \\vert & & \\vdots \\\\ \\text{C}_\\alpha & - & \\text{O}-\\text{CH}_3 \\end{matrix} \\right] \\tag{6.17b}$$
   - This chelate locks the conformation so that the nucleophile must attack from the face opposite the bulkier substituent on the ring, **completely inverting the diastereoselectivity predicted by the Felkin-Anh model**!
   By choosing between coordinating metals ($\\text{Mg}^{2+}, \\text{Ti}^{4+}$) and non-coordinating conditions (organolithiums in coordinating polar solvents like HMPA), chemists achieve complete switchable stereocontrol over chiral center formation."""

    # --- Extra expansion for Unit 7 ---
    u7 = units[6]
    u7["sections"][6]["content"] += """

### Epoxide Cleavages Under Superacidic Conditions (Olah Magic Acid)

Under normal acidic conditions, epoxide ring opening proceeds with anti-stereospecificity through an unsymmetrical oxonium ion.
However, in 1970, George Olah investigated the behavior of epoxides in superacids ($\\text{HSO}_3\\text{F}-\\text{SbF}_5$, 'Magic Acid') at low temperatures ($-78^\\circ\\text{C}$) using cryogenic $^{13}\\text{C}$ and $^1\\text{H}$ NMR:
1. In Magic Acid, the oxygen atom is quantitatively protonated:
   $$\\text{Epoxide} + \\text{HSO}_3\\text{F}-\\text{SbF}_5 \\longrightarrow [\\text{Epoxide-H}]^+ \\tag{7.18a}$$
2. For fully substituted epoxides (tetramethyloxirane / pinacol oxide), the three-membered ring cleaves spontaneously even at $-78^\\circ\\text{C}$ to form a free, open **hydroxy-carbocation**:
   $$\\text{Me}_2\\text{C}(\\stackrel{\\oplus}{\\text{O}}\\text{H})-\\text{CMe}_2 \\longrightarrow \\text{Me}_2\\text{C(OH)}-\\stackrel{\\oplus}{\\text{C}}\\text{Me}_2 \\tag{7.18b}$$
   The carbocation undergoes instantaneous 1,2-methyl migration (pinacol rearrangement) directly inside the NMR tube to yield protonated pinacolone:
   $$\\text{Me}_2\\text{C(OH)}-\\stackrel{\\oplus}{\\text{C}}\\text{Me}_2 \\longrightarrow \\text{Me}-\\text{C}(\\stackrel{\\oplus}{\\text{O}}\\text{H})-\\text{CMe}_3 \\tag{7.18c}$$
This remarkable experiment proved the intimate mechanistic bridge linking epoxide ring-opening, carbocation formation, and pinacol rearrangements!"""

    # --- Extra expansion for Unit 8 ---
    u8 = units[7]
    u8["sections"][1]["content"] += """

### The Knorr Pyrrole Synthesis & Hantzsch Pyridine Synthesis

Beyond the Paal-Knorr reaction, classic name reactions provide targeted routes to densely functionalized heterocycles:

1. **The Knorr Pyrrole Synthesis (Ludwig Knorr, 1884)**:
   Condensation of an $\\alpha$-aminoketone with a $\\beta$-ketoester in glacial acetic acid:
   $$\\text{R}-\\text{CO}-\\text{CH}_2-\\text{NH}_2 + \\text{CH}_3\\text{COCH}_2\\text{COOEt} \\longrightarrow \\text{Substituted Pyrrole-3-carboxylate} + 2\\,\\text{H}_2\\text{O} \\tag{8.5a}$$
   - Because free $\\alpha$-aminoketones self-condense rapidly to dihydropyrazines, they are generated *in situ* by reducing $\\alpha$-oximinoketones ($\\text{R}-\\text{CO}-\\text{C}(=\\text{NOH})\\text{R}'$) with zinc dust in acetic acid.
2. **The Hantzsch Pyridine Synthesis (Arthur Hantzsch, 1882)**:
   A four-component condensation between an aldehyde ($\\text{R}-\\text{CHO}$), two equivalents of a $\\beta$-ketoester (ethyl acetoacetate), and one equivalent of ammonia ($\\text{NH}_3$):
   $$\\text{R}-\\text{CHO} + 2\\,\\text{CH}_3\\text{COCH}_2\\text{COOEt} + \\text{NH}_3 \\longrightarrow \\text{1,4-Dihydropyridine} + 3\\,\\text{H}_2\\text{O} \\tag{8.5b}$$
   - The resulting **1,4-dihydropyridine** (the structural core of commercial cardiovascular calcium channel blockers like nifedipine and amlodipine!) is dehydrogenated with nitric acid or $\\text{DDQ}$ to establish the fully aromatic pyridine ring:
     $$\\text{1,4-Dihydropyridine} + [\\text{O}] \\longrightarrow \\mathbf{\\text{Symmetric 2,6-Dimethylpyridine-3,5-dicarboxylate}} + \\text{H}_2\\text{O} \\tag{8.5c}$$"""

    u8["sections"][6]["content"] += """

### Isotopic Hydride Trapping & Thermochemistry in the Chichibabin Reaction

The elimination of hydride ($H^-$) in the Chichibabin reaction represents a thermodynamic paradox: the hydride ion is among the poorest leaving groups in organic chemistry due to the extreme basicity of $\\text{H}^-$ ($pK_a$ of $\\text{H}_2 \\approx 35$).
Aleksei Chichibabin proved the mechanism by measuring the volumetric liberation of gas:
$$\\text{Pyridine} + \\text{NaNH}_2 \\xrightarrow{110^\\circ\\text{C, toluene}} [\\text{Py-NH}]^- \\text{Na}^+ + \\mathbf{\\text{H}_2\\uparrow} \\tag{8.14a}$$
1. **Gas Stoichiometry**: One mole of molecular hydrogen gas ($\text{H}_2$, $22.4\\text{ L}$ at STP) is quantitatively evolved per mole of pyridine consumed!
2. **Deuterium Tracer Studies**:
   When 2-deuteriopyridine is subjected to Chichibabin amination, the evolved gas is **$\\text{H}-\\text{D}$ (deuterium hydride)** rather than $\\text{H}_2$:
   $$[2\\text{-D-Pyridine}] + \\text{NH}_2^- \\longrightarrow \\text{D}^- + \\text{H}-\\text{NH-Py} \\longrightarrow \\mathbf{\\text{H}-\\text{D}\\uparrow} + [\\text{Py-NH}]^- \\tag{8.14b}$$
   This isotopic experiment conclusively verified that the eliminated hydrogen atom originates specifically from the **C2 carbon undergoing nucleophilic attack**, and is quenched immediately by an amino proton!"""

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
    for idx, u in enumerate(course_data['units'], 1):
        u_words = len(json.dumps(u).split())
        print(f"  Unit {idx}: {len(u['sections'])} sections, {len(u['problems'])} problems (~{u_words:,} words)")

if __name__ == "__main__":
    main()
