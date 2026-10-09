"""
create_supra_u5.py
Creates Unit 5 data dictionary for Supramolecular Chemistry:
Clathrates, Inclusion Compounds & Macrocyclic Cavities
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_5():
    sections = [
        {
            "secNumber": "5.1",
            "title": "Solid-State Inclusion Compounds: Clathrates and Clathrate Hydrates",
            "content": """Inclusion compounds (or adducts) represent supramolecular architectures where one chemical species (the **host**) forms a crystalline lattice or molecular container enclosing cavities, channels, or cages in which a second chemical species (the **guest**) is physically trapped without forming direct covalent bonds.

### Definition of Clathrates
The term **clathrate** (derived from the Latin *clathratus*, meaning "enclosed by a lattice or grating") was introduced by H. M. Powell in 1948. In a true clathrate, guest molecules are enclosed in discrete, isolated polyhedral cages formed by the host crystal lattice:
- The guest cannot escape without dismantling or melting the host crystal framework.
- The host lattice is often thermodynamically unstable in the absence of guest molecules; guest encapsulation stabilizes the empty lattice via dispersion interactions and lattice van der Waals stabilization.

### Gas Hydrates (Clathrate Hydrates)
Clathrate hydrates are non-stoichiometric crystalline water inclusion complexes where hydrogen-bonded water frameworks encage small apolar gas molecules (e.g., $\\text{CH}_4$, $\\text{CO}_2$, $\\text{C}_2\\text{H}_6$, $\\text{Xe}$, $\\text{N}_2$).
Water molecules adopt tetrahedral, four-coordinate, ice-like hydrogen bonding ($d_{\\text{O}\\cdots\\text{O}} \\approx 2.76\\text{ Å}$), but crystallize into polyhedra rather than the hexagonal ice ($\text{I}_h$) lattice:
1. **$5^{12}$ Pentagonal Dodecahedron**: Composed of 12 pentagonal water faces, 20 water vertices, and 30 hydrogen bonds. Average internal cavity radius $r_{\\text{cav}} \\approx 3.95\\text{ Å}$.
2. **$5^{12}6^2$ Tetrakaidecahedron**: 12 pentagonal and 2 hexagonal faces, 24 water vertices. Average cavity radius $r_{\\text{cav}} \\approx 4.33\\text{ Å}$.
3. **$5^{12}6^4$ Hexakaidecahedron**: 12 pentagonal and 4 hexagonal faces, 28 water vertices. Cavity radius $r_{\\text{cav}} \\approx 4.73\\text{ Å}$.

### Crystal Structures of Hydrates
- **Structure I (sI)**: Cubic space group $Pm\\bar{3}n$, unit cell composition $2\\,(5^{12}) + 6\\,(5^{12}6^2) = 46\\,\\text{H}_2\\text{O}$. Traps small guests like methane ($\\text{CH}_4$), ethane, and carbon dioxide. At full cage occupancy, the ideal formula is $8\\,\\text{G}\\cdot 46\\,\\text{H}_2\\text{O} \\approx \\text{G}\\cdot 5.75\\,\\text{H}_2\\text{O}$.
- **Structure II (sII)**: Cubic space group $Fd\\bar{3}m$, unit cell composition $16\\,(5^{12}) + 8\\,(5^{12}6^4) = 136\\,\\text{H}_2\\text{O}$. Traps larger gases like propane, isobutane, and tetrahydrofuran (THF).
- **Structure H (sH)**: Hexagonal space group $P6/mmm$, accommodates both tiny molecules ($\text{CH}_4$) and large cycloalkanes (methylcyclopentane) simultaneously in different cage types."""
        },
        {
            "secNumber": "5.2",
            "title": "Channel Inclusion Hosts: Urea, Thiourea & Dianin's Compound",
            "content": """Unlike clathrates with zero-dimensional discrete zero-void cages, **channel inclusion compounds** possess continuous, one-dimensional open cylindrical tunnels traversing the host crystal lattice.

### Urea Inclusion Compounds
Pure crystalline urea forms a dense, tetragonal crystal lattice ($P\\bar{4}2_1m$) stabilized by planar ribbons of hydrogen bonds. However, in the presence of long-chain linear guests, urea recrystallizes into a hexagonal host lattice ($P6_122$):
- Three interpenetrating spirals of urea molecules form an open hexagonal channel with an internal diameter of approximately $5.0\\text{ to }5.2\\text{ Å}$.
- The channel walls are lined with dense, interlocking networks of $[\\text{N-H}\\cdots\\text{O}=\\text{C}]$ hydrogen bonds, presenting an electrostatic boundary that forces the guest space inside to be completely apolar.
- **Selectivity**: The channel diameter ($5.1\\text{ Å}$) precisely accommodates unbranched, straight-chain $n$-alkanes, $n$-fatty acids, and $\\alpha,\\omega$-disubstituted alkanes in an extended all-*anti* conformation. Branched alkanes (e.g., 2-methylheptane) or aromatic rings are too wide ($>5.6\\text{ Å}$) and are rigorously excluded.

### Thiourea Inclusion Compounds
Replacing the oxygen of urea with sulfur expands the molecular framework:
- The larger covalent radius of sulfur ($r_S \\approx 1.02\\text{ Å}$ vs $r_O \\approx 0.73\\text{ Å}$) expands the hexagonal channel diameter to approximately $6.8\\text{ to }7.1\\text{ Å}$.
- **Reversed Selectivity**: Linear $n$-alkanes are too thin to establish sufficient stabilizing van der Waals contacts with the wide channel walls and fail to template the thiourea lattice. Instead, branched alkanes (e.g., 2,2,4-trimethylpentane), cycloalkanes (cyclohexane, cyclooctane), and globular molecules like adamantane, ferrocene, and carbon tetrachloride form stable inclusion adducts.

### Dianin's Compound
4-(4-Hydroxyphenyl)-2,2,4-trimethylchroman (Dianin's compound) forms hexameric hydrogen-bonded rings consisting of six phenolic hydroxyl groups in a chair-like hexagon:
- Two hexamers stack face-to-face, forming an hourglass-shaped cage with a constriction of $4.2\\text{ Å}$ and central cavities of $6.5\\text{ Å}$.
- Dianin's compound encapsulates a wide spectrum of solvent molecules (chloroform, ethanol, benzene, sulfur dioxide)."""
        },
        {
            "secNumber": "5.3",
            "title": "Werner Complexes & Hofmann-Type Inclusion Compounds",
            "content": """Inorganic and coordination networks also provide robust porous lattices for solid-state molecular inclusion.

### Werner Complexes
Werner clathrates possess the general formula:
\\[
[\\text{M}\\text{X}_2\\text{A}_4] \\cdot n\\,\\text{Guest}
\\]
where:
- $\\text{M}$ is a divalent transition metal cation ($\text{Ni}^{2+}, \\text{Co}^{2+}, \\text{Fe}^{2+}, \\text{Cu}^{2+}, \\text{Mn}^{2+}$).
- $\\text{X}$ is an anionic ligand, most commonly thiocyanate ($\\text{NCS}^-$) or cyanate ($\\text{NCO}^-$).
- $\\text{A}$ is a neutral coordinating aromatic nitrogen base, such as 4-methylpyridine (4-picoline), pyridine, or 1-phenylethylamine.
- The prototypical host is $[\\text{Ni}(\\text{NCS})_2(4\\text{-picoline})_4]$.
The coordination complex adopts an octahedral geometry with two axial trans-thiocyanates and four equatorial picoline ligands arranged in a propeller-like conformation. In the crystalline phase, propeller packing generates interstitial cavities that display extraordinary shape-selectivity for aromatic isomers, famously separating $p$-xylene from $m$-xylene and $o$-xylene with selectivity factors exceeding $\\alpha_{p/m} > 10$.

### Hofmann-Type Clathrates
Hofmann clathrates are two-dimensional and three-dimensional cyanometallate coordination polymers:
- **Hofmann's Classic Adduct**: Formed by reacting ammoniacal nickel(II) solutions with tetracyanonickelate(II) in the presence of benzene:
\\[
\\text{Ni}(\\text{NH}_3)_2\\text{Ni}(\\text{CN})_4 \\cdot 2\\,\\text{C}_6\\text{H}_6
\\]
- The structure consists of planar square-planar $[\\text{Ni}(\\text{CN})_4]^{2-}$ units linked by bridging octahedral $[\\text{Ni}(\\text{NH}_3)_2]^{2+}$ cations, forming infinite two-dimensional square-grid sheets $[\\text{Ni}_2(\\text{CN})_4]_\infty$.
- The axial ammine ligands project above and below each sheet. Intercalated benzene molecules are trapped between parallel coordination layers, held tightly by aromatic $\\pi$-dipole and dispersive interactions.
- Modern analogues replace $\\text{NH}_3$ with bidentate bridging diamines (e.g., 4,4'-bipyridine, pyrazine) to yield 3D porous coordination networks precursor to Metal-Organic Frameworks (MOFs)."""
        },
        {
            "secNumber": "5.4",
            "title": "Cyclodextrins: Structure, Conical Hydrophobic Cavities & Glucopyranose Linkages",
            "content": """**Cyclodextrins (CDs)**, also termed cycloamyloses or Schardinger dextrins, are cyclic oligosaccharides composed of $\\alpha$-D-glucopyranoside units linked by $\\alpha$-(1,4)-glycosidic bonds. They are produced enzymatically from starch by the action of cyclodextrin glucanotransferase (CGTase).

### The Three Native Cyclodextrins
The three industrially and biologically prominent native cyclodextrins are:
1. **$\\alpha$-Cyclodextrin ($\alpha$-CD)**: 6 glucopyranose units ($M_w = 972.8\\text{ g/mol}$).
   - Internal cavity diameter: $4.7\\text{ to }5.3\\text{ Å}$.
   - Cavity volume: $V_{\\text{cav}} \\approx 174\\text{ Å}^3$.
   - Water solubility: $145\\text{ g/L}$ at $25^\\circ\\text{C}$.
2. **$\\beta$-Cyclodextrin ($\beta$-CD)**: 7 glucopyranose units ($M_w = 1135.0\\text{ g/mol}$).
   - Internal cavity diameter: $6.0\\text{ to }6.5\\text{ Å}$.
   - Cavity volume: $V_{\\text{cav}} \\approx 262\\text{ Å}^3$.
   - Water solubility: $18.5\\text{ g/L}$ at $25^\\circ\\text{C}$ (anomalously low due to a rigid, intramolecular circular belt of secondary hydrogen bonds).
3. **$\\gamma$-Cyclodextrin ($\gamma$-CD)**: 8 glucopyranose units ($M_w = 1297.1\\text{ g/mol}$).
   - Internal cavity diameter: $7.5\\text{ to }8.3\\text{ Å}$.
   - Cavity volume: $V_{\\text{cav}} \\approx 427\\text{ Å}^3$.
   - Water solubility: $232\\text{ g/L}$ at $25^\\circ\\text{C}$.

### The Toroidal Truncated-Cone Morphology
Because all $\\text{C}_1$ chairs of the D-glucopyranose units adopt the $^4\\text{C}_1$ conformation, the cyclodextrin ring does not form a flat cylinder; instead, it adopts a **truncated cone (torus)**:
- **Wider Rim (Secondary Rim)**: Lined with the secondary hydroxyl groups ($\text{C}_2-\\text{OH}$ and $\text{C}_3-\\text{OH}$).
- **Narrower Rim (Primary Rim)**: Lined with the primary hydroxyl groups ($\text{C}_6-\\text{OH}$).
- **Interior Cavity Walls**: Lined exclusively by the axial hydrogens ($\text{H}_3$ and $\text{H}_5$) and the ether-like glycosidic oxygen bridges ($\text{C}_1-\\text{O}-\\text{C}_4$).
Consequently, the cavity interior is completely hydrophobic and apolar (dielectric constant $\\epsilon_r \\approx 20 - 30$, resembling ethanol or octanol), while the exterior rims are hydrophilic and fully hydrated in aqueous media."""
        },
        {
            "secNumber": "5.5",
            "title": "Cyclodextrin Inclusion Chemistry: Hydrophobic Effect & Enantioselective Recognition",
            "content": """In aqueous solution, cyclodextrins encapsulate apolar organic molecules, forming non-covalent $1:1$ or $1:2$ inclusion complexes:
\\[
\\text{CD} + \\text{Guest} \\xrightleftharpoons{K_a} \\text{CD}\\cdot\\text{Guest}
\\]

### Thermodynamic Driving Forces: The Hydrophobic Effect & High-Energy Water
The fundamental driving force for cyclodextrin inclusion is not primarily host-guest covalent attraction, but solvent reorganization:
1. **Release of Enthalpically High-Energy Water**:
   The apolar interior cavity cannot satisfy the tetrahedral hydrogen-bonding requirements of liquid water. Water molecules enclosed inside the uncomplexed cavity have reduced hydrogen bonds and unfavorable dipolar orientations ("high-energy water").
   Encapsulation of an apolar guest expels these water molecules into the bulk solvent where they form stable hydrogen bonds ($4\\,\\text{H}_2\\text{O}$ per $\\beta$-CD), yielding a favorable enthalpy change:
   \\[
   \\Delta H_{\\text{water release}} < 0
   \\]
2. **Classical Hydrophobic Effect**:
   Desolvation of the apolar guest disrupts the ordered ice-like water hydration shell surrounding the guest, yielding a favorable entropy of desolvation:
   \\[
   \\Delta S_{\\text{desolv}} > 0
   \\]
3. **van der Waals and Dispersion Interactions**:
   Close geometric contacts between the hydrophobic guest skeleton and the $\\text{C}_3-\\text{H}$ and $\\text{C}_5-\\text{H}$ cavity protons contribute negative enthalpy ($\\Delta H_{\\text{vdW}} < 0$).

### Cavity Sizing Rules
- **$\alpha$-CD**: Accommodates linear aliphatic chains and mono-substituted benzenes ($p$-nitrophenol, toluene).
- **$\beta$-CD**: Perfectly encloses adamantane, naphthalene derivatives, ibuprofen, and cholesterol.
- **$\gamma$-CD**: Accommodates bulky polycyclics, fullerenes ($\text{C}_{60}$), steroid dimers, and can bind two planar aromatic guests simultaneously ($1:2$ complex).

### Chiral Recognition & Pharmaceutical Encapsulation
Because cyclodextrins are constructed from naturally chiral D-glucose, the interior cavity is an asymmetric, chiral microenvironment.
- Enantiomeric guests experience diastereomeric inclusion complexes with distinct free energies ($\\Delta \\Delta G^\circ = \\Delta G_{(R)}^\circ - \\Delta G_{(S)}^\circ \\neq 0$), enabling chiral resolution in HPLC/capillary electrophoresis.
- Pharmaceutical formulation: Enclosing hydrophobic drugs (e.g., piroxicam, itraconazole) in $\\beta$-CD or modified hydroxypropyl-$\\beta$-CD ($\text{HP}-\\beta\\text{-CD}$) boosts water solubility up to 10,000-fold and enhances bioavailability."""
        },
        {
            "secNumber": "5.6",
            "title": "Calixarenes and Resorcinarenes: Conformations & Rim Functionalization",
            "content": """**Calixarenes** are macrocyclic oligomers synthesized by the base-catalyzed condensation of $p$-substituted phenols with formaldehyde, pioneered by Alois Zinke and popularized by C. David Gutsche. The name derives from the Greek *calix* (vase or chalice) and *arene* (aromatic ring).

### Calix[4]arene Conformations
The archetypal member is calix[4]arene (four phenolic rings linked by methylene bridges, $-\\text{CH}_2-$). In solution, restricted rotation around the methylene bridges yields four distinct conformational stereoisomers:
1. **Cone ($C_{4v}$)**: All four phenolic hydroxyl groups point in the same direction (downward toward the lower rim). Stabilized by a cyclic circular belt of four cooperative $[\\text{O-H}\\cdots\\text{O}]$ hydrogen bonds.
2. **Partial Cone ($C_s$)**: Three phenolic hydroxyl groups point down, and one phenolic ring is flipped $180^\\circ$ pointing up.
3. **1,2-Alternate ($C_{2h}$)**: Two adjacent phenolic rings point down, and two adjacent rings point up.
4. **1,3-Alternate ($D_{2d}$)**: Opposite pairs of phenolic rings point in opposite directions (alternating up, down, up, down).

### Dynamic Inversion and Bridging Methylene $^1\text{H}$-NMR Spectroscopy
In unmodified calix[4]arene, thermal inversion between cone conformations occurs rapidly on the NMR timescale at room temperature ($E_a \\approx 63\\text{ kJ/mol}$):
- In the fixed cone conformation, each $-\\text{CH}_2-$ methylene proton experiences an asymmetric environment: one proton is *axial* (pointing into the calix cup) and the other is *equatorial* (pointing outward).
- This produces a characteristic **pair of doublets (AB quartet)** in the $^1\\text{H}$-NMR spectrum with a geminal coupling constant $J_{\\text{gem}} \\approx 12 - 14\\text{ Hz}$.
- If the calixarene adopts a 1,3-alternate conformation, both methylene protons reside in identical plane-symmetric environments, collapsing the signal into a **sharp singlet**.

### Functionalization: Upper vs Lower Rim
- **Lower Rim (Phenolic Oxygen Portal)**: Readily alkylated with alkyl halides, crown ethers (calix-crowns), or esters/amides. Bulky substituents (e.g., propyl or larger) permanently lock the macrocycle into a specific conformation (cone, partial cone, or alternate).
- **Upper Rim (Para Position)**: The $tert$-butyl groups of $p$-$tert$-butylcalix[4]arene are cleanly removed by retro-Friedel-Crafts dealkylation with $\\text{AlCl}_3$ in toluene, allowing introduction of electrophiles ($-\\text{NO}_2$, $-\\text{SO}_3\\text{H}$, $-\\text{CHO}$) to tailor solubility and binding."""
        },
        {
            "secNumber": "5.7",
            "title": "Cucurbit[n]urils: Synthesis, Rigid Carbonyl Portals & Ultra-High Affinity Binding",
            "content": """**Cucurbit[$n$]urils ($\text{CB}[n]$)** are pumpkin-shaped macrocycles composed of $n$ glycoluril units linked by $2n$ methylene bridges, popularized by Kimoon Kim and Lyle Isaacs. The name stems from their resemblance to the pumpkin family *Cucurbitaceae*.

### Synthesis & Homologues
Synthesized by the acid-catalyzed condensation of glycoluril with formaldehyde in concentrated sulfuric acid or hydrochloric acid at $>100^\\circ\\text{C}$:
\\[
n\\,\\text{Glycoluril} + 2n\\,\\text{HCHO} \\xrightarrow{\\text{conc. }\\text{H}_2\\text{SO}_4} \\text{CB}[n] + 2n\\,\\text{H}_2\\text{O}
\\]
Common homologues include $\\text{CB}[5]$, $\\text{CB}[6]$, $\\text{CB}[7]$, $\\text{CB}[8]$, and $\\text{CB}[10]$:
- $\\text{CB}[6]$: Internal volume $164\\text{ Å}^3$, portal diameter $3.9\\text{ Å}$. Accommodates linear diamines ($n$-diaminoalkanes).
- $\\text{CB}[7]$: Internal volume $279\\text{ Å}^3$, portal diameter $5.4\\text{ Å}$. Isomorphic in volume to $\\beta$-CD. Accommodates adamantanes, ferrocene, and drugs.
- $\\text{CB}[8]$: Internal volume $479\\text{ Å}^3$, portal diameter $6.9\\text{ Å}$. Accommodates two guest molecules simultaneously.

### Architecture: Portals vs Cavity
$\text{CB}[n]$ possesses a uniquely rigid structure with two distinct chemical zones:
1. **Carbonyl Portals**: Two identical portals fringed with $n$ carbonyl oxygens. The electronegative carbonyl lone pairs generate an intense negative electrostatic potential, acting as ideal Lewis basic docking sites for positively charged ammonium ($\\text{R-NH}_3^+$) or metal cations.
2. **Hydrophobic Interior Cavity**: Lined entirely with aliphatic $-\\text{CH}-$ and $-\\text{CH}_2-$ protons, devoid of functional groups and completely nonpolar.

### Ultra-High Affinity: The Strongest Non-Covalent Synthetics
$\text{CB}[7]$ forms the tightest non-covalent complexes ever recorded in artificial supramolecular chemistry:
- Complexation of ferrocenylmethylammonium or diamantane diammonium cations in water yields binding constants:
\\[
K_a > 10^{15} - 10^{17}\\text{ M}^{-1}
\\]
rivaling the biological biotin-streptavidin pair ($K_a \\approx 10^{14}\\text{ M}^{-1}$).
- The driving force combines:
  1. Complete expulsion of high-energy cavity water.
  2. Severe electrostatic attraction between cationic ammonium ends and the negatively polarized carbonyl portals.
  3. Perfect van der Waals packing fraction ($PF \\approx 0.55$) of the hydrophobic core."""
        },
        {
            "secNumber": "5.8",
            "title": "Pillar[n]arenes and Deep Cavitands: Hydroquinone Macrocycles & Container Molecules",
            "content": """Beyond classical calixarenes, novel generations of macrocycles and synthetic containers provide unprecedented symmetry and binding capabilities.

### Pillar[n]arenes
Introduced by Tomoki Ogoshi in 2008, **pillar[$n$]arenes** are macrocyclic hosts formed by the condensation of 1,4-dimethoxybenzene (hydroquinone dimethyl ether) with paraformaldehyde catalyzed by Lewis acids (e.g., $\\text{BF}_3\\cdot\\text{OEt}_2$ or $\\text{FeCl}_3$):
- Unlike the conical, tapered shape of calixarenes, pillar[$n$]arenes are linked by methylene bridges at the 2- and 5-positions of the hydroquinone rings, forming a **perfect, symmetrical cylindrical pillar**.
- **Pillar[5]arene**: Symmetrical pentagonal cylinder with an internal cavity diameter of $4.7\\text{ Å}$, matching the diameter of $n$-alkanes and viologens.
- **Pillar[6]arene**: Hexagonal cylinder with cavity diameter $6.7\\text{ Å}$.
- **Symmetry and Ease of Functionalization**: Both upper and lower rims are chemically equivalent and symmetrically decorated with alkoxy groups (e.g., 10 identical groups for pillar[5]arene), permitting straightforward deprotection to poly-phenols or water-soluble carboxylate/ammonium salts.

### Cavitands and Carcerands
Donald J. Cram introduced rigid container molecules constructed from resorcin[4]arenes:
1. **Cavitands**: Resorcinarene hosts in which adjacent phenolic hydroxyls are covalently linked by short bridging units (e.g., $-\\text{O}-\\text{CH}_2-\\text{O}-$ acetal bridges or quinoxaline walls). This rigidifies the bowl into an enforced, permanent cone shape that cannot invert.
2. **Deep Cavitands**: Extending the aromatic walls with benzimidazole or imide groups creates deep hydrophobic pockets capable of enveloping long linear alkanes in coiled conformations or stabilizing reactive intermediates.
3. **Carcerands and Hemicarcerands**:
   - **Carcerand**: Two cavitand bowls fused face-to-face by multiple covalent linkers, permanently trapping guest molecules inside. The entrapped guest cannot escape at any temperature below the covalent thermal breakdown threshold—a state known as **carceplex**.
   - **Hemicarcerand**: Possesses portals large enough that guest molecules can enter and exit at high temperatures through thermal breathing, but remain locked inside at room temperature (**hemicarceplex**). Used by Cram to stabilize otherwise transient species like cyclobutadiene and $o$-benzyne at room temperature."""
        }
    ]

    problems = [
        {
            "probNumber": "5.1",
            "title": "Geometry and Occupancy of Structure I Methane Clathrate Hydrate",
            "difficulty": "Foundational",
            "statement": """A crystalline specimen of Structure I (sI) methane clathrate hydrate possesses a cubic unit cell with edge length $a = 12.00\\text{ Å} = 1.200 \\times 10^{-9}\\text{ m}$.
The unit cell framework contains 46 water molecules organized into two small $5^{12}$ dodecahedral cages and six large $5^{12}6^2$ tetrakaidecahedral cages.
(a) If both the small cages and large cages are $100\\%$ occupied by methane molecules ($\\text{CH}_4$), determine:
    (i) The total number of methane molecules per unit cell,
    (ii) The hydration number $n$ in the stoichiometric formula $\\text{CH}_4 \\cdot n\\,\\text{H}_2\\text{O}$,
    (iii) The theoretical crystal density $\\rho_{\\text{sI}}$ in $\\text{g/cm}^3$.
(b) In a natural deep-sea marine hydrate deposit, thermodynamic equilibrium at $P = 5.0\\text{ MPa}$ and $T = 277\\text{ K}$ yields fractional occupancies of $\\theta_{\\text{small}} = 0.850$ in the small cages and $\\theta_{\\text{large}} = 0.980$ in the large cages. Calculate the actual hydration number $n_{\\text{act}}$ and the STP volume of methane gas ($T_0 = 273.15\\text{ K}, P_0 = 1.00\\text{ bar}$) released by $1.00\\text{ m}^3$ of this natural hydrate upon complete dissociation.""",
            "solution": """### Step 1: Fully Occupied sI Hydrate Properties
1. **Methane Molecules per Unit Cell**:
   Unit cell contains 2 small cages and 6 large cages.
   At $100\\%$ occupancy:
   \\[
   N_{\\text{CH}_4} = 2 + 6 = 8\\text{ molecules per unit cell}
   \\]
2. **Hydration Number $n$**:
   With 46 water molecules:
   \\[
   n = \\frac{N_{\\text{H}_2\\text{O}}}{N_{\\text{CH}_4}} = \\frac{46}{8} = 5.75
   \\]
   The ideal formula is $\\text{CH}_4 \\cdot 5.75\\,\\text{H}_2\\text{O}$.
3. **Theoretical Density**:
   Unit cell volume:
   \\[
   V_{\\text{cell}} = a^3 = (1.200 \\times 10^{-7}\\text{ cm})^3 = 1.728 \\times 10^{-21}\\text{ cm}^3
   \\]
   Total molecular weight in unit cell:
   \\[
   M_{\\text{cell}} = 46 \\times M(\\text{H}_2\\text{O}) + 8 \\times M(\\text{CH}_4) = 46(18.015) + 8(16.042) = 828.69 + 128.34 = 957.03\\text{ g/mol}
   \\]
   Mass per unit cell:
   \\[
   m_{\\text{cell}} = \\frac{957.03\\text{ g/mol}}{6.02214 \\times 10^{23}\\text{ mol}^{-1}} = 1.5892 \\times 10^{-21}\\text{ g}
   \\]
   Density:
   \\[
   \\rho_{\\text{sI}} = \\frac{m_{\\text{cell}}}{V_{\\text{cell}}} = \\frac{1.5892 \\times 10^{-21}\\text{ g}}{1.728 \\times 10^{-21}\\text{ cm}^3} = 0.9197\\text{ g/cm}^3
   \\]

### Step 2: Natural Marine Hydrate with Partial Occupancies
1. **Actual Methane Content**:
   \\[
   N_{\\text{CH}_4}^{\\text{act}} = 2 \\theta_{\\text{small}} + 6 \\theta_{\\text{large}} = 2(0.850) + 6(0.980) = 1.700 + 5.880 = 7.580\\text{ molecules per unit cell}
   \\]
   Actual hydration number:
   \\[
   n_{\\text{act}} = \\frac{46}{7.580} = 6.069 \\approx 6.07
   \\]
   The actual composition is $\\text{CH}_4 \\cdot 6.07\\,\\text{H}_2\\text{O}$.
2. **STP Gas Volume Released per $1.00\\text{ m}^3$ Hydrate**:
   Unit cell volume in $\\text{m}^3$:
   \\[
   V_{\\text{cell}} = (1.200 \\times 10^{-9}\\text{ m})^3 = 1.728 \\times 10^{-27}\\text{ m}^3
   \\]
   Number of unit cells in $1.00\\text{ m}^3$:
   \\[
   N_{\\text{cells}} = \\frac{1.00\\text{ m}^3}{1.728 \\times 10^{-27}\\text{ m}^3} = 5.7870 \\times 10^{26}\\text{ cells}
   \\]
   Total methane molecules in $1.00\\text{ m}^3$:
   \\[
   N_{\\text{CH}_4}^{\\text{total}} = 5.7870 \\times 10^{26} \\times 7.580 = 4.3866 \\times 10^{27}\\text{ molecules}
   \\]
   Moles of methane:
   \\[
   n_{\\text{CH}_4} = \\frac{4.3866 \\times 10^{27}}{6.02214 \\times 10^{23}} = 7{,}284.1\\text{ moles of }\\text{CH}_4
   \\]
   At standard temperature and pressure ($T_0 = 273.15\\text{ K}, P_0 = 1.00\\times 10^5\\text{ Pa}$, molar gas volume $V_m = 22.711\\text{ L/mol} = 0.022711\\text{ m}^3\\text{/mol}$):
   \\[
   V_{\\text{gas}} = 7{,}284.1\\text{ mol} \\times 0.022711\\text{ m}^3/\\text{mol} = 165.42\\text{ m}^3
   \\]
   One cubic meter of natural marine methane hydrate expands to release over $165\\text{ m}^3$ of methane gas at STP."""
        },
        {
            "probNumber": "5.2",
            "title": "Cavity Sizing Tolerance of Alpha, Beta, and Gamma Cyclodextrins",
            "difficulty": "Foundational",
            "statement": """The cross-sectional diameters of three organic guests are:
1. $p$-Xylene: Diameter across methyl groups $\\approx 5.8\\text{ Å}$; thickness $\\approx 3.8\\text{ Å}$.
2. Adamantane: Spherical diameter $d_{\\text{sph}} \\approx 6.4\\text{ Å}$.
3. [60]Fullerene ($\text{C}_{60}$): Outer van der Waals diameter $d_{\\text{vdW}} \\approx 10.1\\text{ Å}$.
The internal cavity diameters of native cyclodextrins are:
- $\\alpha$-CD: $4.7 - 5.3\\text{ Å}$
- $\\beta$-CD: $6.0 - 6.5\\text{ Å}$
- $\\gamma$-CD: $7.5 - 8.3\\text{ Å}$
(a) For each guest, predict which native cyclodextrin provides the highest association constant $K_a$ in aqueous solution, citing steric match and packing fraction principles.
(b) The experimental association constant of adamantane-1-carboxylate with $\\beta$-CD is $K_a = 3.20 \\times 10^5\\text{ M}^{-1}$, but with $\\alpha$-CD it is $K_a < 10\\text{ M}^{-1}$, and with $\\gamma$-CD it is $K_a = 4.50 \\times 10^2\\text{ M}^{-1}$. Calculate the binding selectivity ratios:
    (i) $K_a(\\beta)/K_a(\\alpha)$
    (ii) $K_a(\\beta)/K_a(\\gamma)$
(c) Explain why $\\gamma$-CD binds two molecules of pyrene to form an excimer, whereas $\\beta$-CD forms only a $1:1$ monomer complex.""",
            "solution": """### Step 1: Geometric Match Analysis
1. **$p$-Xylene**:
   - Cross-section of $3.8\\text{ Å} \\times 5.8\\text{ Å}$.
   - Fits snugly inside $\\alpha$-CD ($4.7 - 5.3\\text{ Å}$) with the aromatic ring threaded axially through the torus. $\\beta$-CD can accommodate it but leaves residual void volume (loose fit).
   - Preferred host: **$\\alpha$-CD**.
2. **Adamantane**:
   - Spherical diameter $6.4\\text{ Å}$ matches the interior cavity diameter of $\\beta$-CD ($6.0 - 6.5\\text{ Å}$) with near-ideal van der Waals contact on all faces. Too large to enter $\\alpha$-CD ($<5.3\\text{ Å}$).
   - Preferred host: **$\\beta$-CD**.
3. **[60]Fullerene ($\text{C}_{60}$)**:
   - Outer diameter $10.1\\text{ Å}$. Exceeds the cavity diameter of $\\alpha$-CD and $\\beta$-CD.
   - Fits snugly into a bicapped complex formed by **two $\\gamma$-CD** tori ($7.5 - 8.3\\text{ Å}$ rim) enclosing the equatorial belt of $\\text{C}_{60}$ in a $2:1$ sandwich complex.

### Step 2: Adamantane-1-Carboxylate Selectivity Ratios
Given:
- $K_a(\\beta) = 3.20 \\times 10^5\\text{ M}^{-1}$
- $K_a(\\alpha) < 10\\text{ M}^{-1}$ (take upper bound $10\\text{ M}^{-1}$)
- $K_a(\\gamma) = 4.50 \\times 10^2\\text{ M}^{-1}$

1. **$\\beta / \\alpha$ Selectivity**:
\\[
\\text{Selectivity}(\\beta / \\alpha) = \\frac{K_a(\\beta)}{K_a(\\alpha)} = \\frac{3.20 \\times 10^5}{10} = 3.20 \\times 10^4
\\]
$\\beta$-CD is at least $32{,}000$ times more affine than $\\alpha$-CD due to severe steric clash at the narrow $\\alpha$-CD portal.

2. **$\\beta / \\gamma$ Selectivity**:
\\[
\\text{Selectivity}(\\beta / \\gamma) = \\frac{K_a(\\beta)}{K_a(\\gamma)} = \\frac{3.20 \\times 10^5}{4.50 \\times 10^2} = 711
\\]
$\\beta$-CD binds adamantane $711$ times more strongly than $\\gamma$-CD because the $\\gamma$-CD cavity ($7.5 - 8.3\\text{ Å}$) is excessively large, leaving unfilled space and failing to achieve tight van der Waals contacts with the guest.

### Step 3: Pyrene Excimer Formation in $\\gamma$-CD vs $\\beta$-CD
- Pyrene is a flat, tetracyclic aromatic hydrocarbon with an in-plane width of $\\approx 7.0\\text{ Å}$ and a $\\pi$-thickness of $3.4\\text{ Å}$.
- In $\\beta$-CD (cavity $6.2\\text{ Å}$), a single pyrene molecule intercalates snugly with its long axis along the cavity. The remaining cavity volume is insufficient to accommodate a second pyrene ring; thus only a $1:1$ complex forms, emitting sharp monomer fluorescence.
- In $\\gamma$-CD (cavity $8.0\\text{ Å}$), the wide aperture allows two flat pyrene molecules to co-encapsulate face-to-face in a $\\pi-\\pi$ sandwich ($1:2$ complex, total stacked thickness $2 \\times 3.4 = 6.8\\text{ Å} < 8.0\\text{ Å}$). Photoexcitation produces a bound excited-state dimer (**excimer**), characterized by a broad, structureless, red-shifted fluorescence band at $\\lambda_{\\max} \\approx 470\\text{ nm}$."""
        },
        {
            "probNumber": "5.3",
            "title": "Calix[4]arene Conformational Isomers & 1H-NMR Methylene Splitting",
            "difficulty": "Foundational",
            "statement": """$p$-$tert$-Butylcalix[4]arene was exhaustively alkylated at the lower rim with benzyl bromide in the presence of various bases to yield stereochemically locked tetra-O-benzyl derivatives in different conformations:
1. Conformation I: Cone ($C_{4v}$)
2. Conformation II: Partial Cone ($C_s$)
3. Conformation III: 1,3-Alternate ($D_{2d}$)
(a) For each conformation, analyze the symmetry and determine:
    (i) The number of chemically non-equivalent phenolic rings,
    (ii) The number of non-equivalent $tert$-butyl singlet resonances in the $^1\\text{H}$-NMR spectrum,
    (iii) The splitting pattern (singlet vs AB doublet) and number of signals for the bridging $-\\text{CH}_2-$ methylene protons.
(b) In a recorded $^1\\text{H}$-NMR spectrum of an isolated isomer in $\\text{CDCl}_3$:
    - Two equal-intensity $tert$-butyl singlets appear at $\\delta = 1.30\\text{ ppm}$ and $\\delta = 0.95\\text{ ppm}$ (ratio $1:1$).
    - The methylene region displays a single sharp singlet at $\\delta = 3.75\\text{ ppm}$ (integrating to 8H).
    Identify which conformation corresponds to this spectrum and explain why the methylene protons appear as a singlet.""",
            "solution": """### Step 1: Symmetry and NMR Analysis of Conformations
1. **Conformation I: Cone ($C_{4v}$)**:
   - All four rings point in the same direction. All 4 aromatic units are symmetry-equivalent by the 4-fold rotation axis $C_4$.
   - **$tert$-Butyl groups**: Exactly **one sharp singlet** (integrating to 36H).
   - **Bridging $-\\text{CH}_2-$ groups**: Every methylene group connects two rings that point in the same direction. The two protons on each methylene bridge are diastereotopic (one points *endo* into the cavity, the other *exo* outward). They couple geminally with each other ($J \\approx 13 - 14\\text{ Hz}$), producing an **AB quartet (two doublets)** integrating to 4H each.

2. **Conformation II: Partial Cone ($C_s$)**:
   - Three rings point in one direction, one inverted ring points in the opposite direction.
   - Symmetries: Mirror plane bisecting the inverted ring and the opposite ring.
   - Non-equivalent rings: Three distinct types in a $2:1:1$ ratio (the inverted ring, the ring opposite to it, and the two flanking rings).
   - **$tert$-Butyl groups**: **Three singlets** in a $2:1:1$ intensity ratio (18H, 9H, 9H).
   - **Bridging $-\\text{CH}_2-$ groups**: Two methylene bridges connect parallel rings (yielding an AB doublet), and two connect opposite rings (yielding another AB doublet or complex multiplets).

3. **Conformation III: 1,3-Alternate ($D_{2d}$)**:
   - Alternating up-down-up-down orientation. Possesses an improper $S_4$ rotation axis and two $C_2'$ axes.
   - All four rings are equivalent by symmetry.
   - **$tert$-Butyl groups**: Exactly **one sharp singlet** (36H).
   - **Bridging $-\\text{CH}_2-$ groups**: Every methylene bridge connects two rings pointing in opposite directions (one up, one down). The two protons on each $-\\text{CH}_2-$ lie on a $C_2$ symmetry axis; thus they are enantiotopic/homotopic and chemically equivalent. They do not split each other, appearing as a **single sharp singlet** (integrating to 8H).

### Step 2: Identification of the Unknown Isomer
The unknown isomer exhibits:
- Two $tert$-butyl singlets in a $1:1$ ratio (18H each).
- A single sharp singlet for the bridging $-\\text{CH}_2-$ protons (8H).
- The singlet for $-\\text{CH}_2-$ indicates that adjacent rings point in opposite directions across every bridge.
- The presence of two $tert$-butyl resonances in a $1:1$ ratio indicates that the four rings are divided into two pairs of magnetically distinct environments, as observed in a **1,2-alternate conformation ($C_{2h}$)** with two adjacent rings up and two adjacent rings down, or a dynamically substituted 1,3-alternate derivative with asymmetric lower-rim substitution. For a symmetric tetra-substituted calix[4]arene, an alternating up-down-up-down configuration with two distinct opposing face environments yields two $tert$-butyl singlets while maintaining the $C_2$ bridge symmetry that collapses the methylene into a singlet."""
        },
        {
            "probNumber": "5.4",
            "title": "Thermodynamics of Cyclodextrin Inclusion: ITC Enthalpy-Entropy Compensation",
            "difficulty": "Intermediate",
            "statement": """Isothermal titration calorimetry (ITC) was used to study the complexation of native $\\beta$-cyclodextrin with two guests in aqueous buffer at $T = 298.15\\text{ K}$:
- **Guest 1 (1-adamantanecarboxylate)**:
  $K_{a,1} = 3.20 \\times 10^5\\text{ M}^{-1}$, $\\Delta H_1^\circ = -22.40\\text{ kJ/mol}$.
- **Guest 2 (1-butanol)**:
  $K_{a,2} = 1.65 \\times 10^1\\text{ M}^{-1}$, $\\Delta H_2^\circ = -9.20\\text{ kJ/mol}$.
(a) Calculate $\\Delta G^\circ$, $T\\Delta S^\circ$, and $\\Delta S^\circ$ for both complexation events at $298.15\\text{ K}$.
(b) Determine whether each inclusion process is enthalpy-driven, entropy-driven, or both.
(c) In supramolecular host-guest inclusion, Inoue observed that cyclodextrins conform to a linear enthalpy-entropy compensation relation:
\\[
T\\Delta S^\\circ = \\alpha \\Delta H^\\circ + T\\Delta S_0^\\circ
\\]
Using the experimental values for Guest 1 and Guest 2, calculate the slope $\\alpha$ and intercept $T\\Delta S_0^\circ$. Discuss the physical meaning of $\\alpha \\approx 0.7 - 0.9$ in terms of cavity desolvation and host conformational freezing.""",
            "solution": """### Step 1: Thermodynamic Parameters for Guests 1 and 2
Using $R = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$ and $T = 298.15\\text{ K}$ ($RT = 2.47896\\text{ kJ/mol}$):

1. **Guest 1 (1-adamantanecarboxylate)**:
\\[
\\Delta G_1^\\circ = -RT \\ln K_{a,1} = -2.47896 \\times \\ln(3.20 \\times 10^5) = -2.47896 \\times 12.6761 = -31.424\\text{ kJ/mol}
\\]
With $\\Delta H_1^\\circ = -22.40\\text{ kJ/mol}$:
\\[
T\\Delta S_1^\\circ = \\Delta H_1^\\circ - \\Delta G_1^\\circ = -22.40 - (-31.424) = +9.024\\text{ kJ/mol}
\\]
\\[
\\Delta S_1^\\circ = \\frac{+9{,}024\\text{ J/mol}}{298.15\\text{ K}} = +30.27\\text{ J/(mol}\\cdot\\text{K)}
\\]

2. **Guest 2 (1-butanol)**:
\\[
\\Delta G_2^\\circ = -RT \\ln K_{a,2} = -2.47896 \\times \\ln(16.5) = -2.47896 \\times 2.8034 = -6.949\\text{ kJ/mol}
\\]
With $\\Delta H_2^\\circ = -9.20\\text{ kJ/mol}$:
\\[
T\\Delta S_2^\\circ = \\Delta H_2^\\circ - \\Delta G_2^\\circ = -9.20 - (-6.949) = -2.251\\text{ kJ/mol}
\\]
\\[
\\Delta S_2^\\circ = \\frac{-2{,}251\\text{ J/mol}}{298.15\\text{ K}} = -7.55\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 2: Driving Force Evaluation
- **Guest 1 (Adamantanecarboxylate)**: Both $\\Delta H_1^\\circ < 0$ ($-22.40\\text{ kJ/mol}$) and $T\\Delta S_1^\\circ > 0$ ($+9.02\\text{ kJ/mol}$) contribute favorably to binding. The process is **cooperatively driven by both enthalpy and entropy**, where enthalpy provides $71\\%$ and entropy provides $29\\%$ of the binding free energy.
- **Guest 2 (1-butanol)**: $\\Delta H_2^\\circ < 0$ ($-9.20\\text{ kJ/mol}$) is favorable, but $T\\Delta S_2^\\circ < 0$ ($-2.25\\text{ kJ/mol}$) is unfavorable. The process is **strictly enthalpy-driven**, with binding offset by an unfavorable entropic loss of translational and rotational freedom of the flexible butyl chain upon entrapment.

### Step 3: Enthalpy-Entropy Compensation Parameters
From the two-point linear equation:
\\[
\\alpha = \\frac{T\\Delta S_1^\\circ - T\\Delta S_2^\\circ}{\\Delta H_1^\\circ - \\Delta H_2^\\circ} = \\frac{+9.024 - (-2.251)}{-22.40 - (-9.20)} = \\frac{11.275}{-13.20} = -0.854
\\]
Writing the conventional compensation relation $T\\Delta S^\circ = \\alpha \\Delta H^\circ + T\\Delta S_0^\circ$:
Because more negative enthalpy corresponds to more positive entropy here due to extensive hydrophobic desolvation of high-energy water:
\\[
T\\Delta S_0^\\circ = T\\Delta S_1^\\circ - \\alpha \\Delta H_1^\\circ = 9.024 - (-0.854)(-22.40) = 9.024 - 19.130 = -10.11\\text{ kJ/mol}
\\]
- **Physical Meaning**:
  A slope of $|\\alpha| \\approx 0.85$ indicates that approximately $85\\%$ of any enthalpic gain achieved by optimizing host-guest van der Waals contacts is canceled out by entropic penalties (loss of conformational freedom of the host and guest, and restriction of solvent). The remaining $15\\%$ of free energy represents the net gain that determines the association constant."""
        },
        {
            "probNumber": "5.5",
            "title": "Cucurbit[7]uril Ultra-High Affinity: Femtomolar Binding Mechanics",
            "difficulty": "Intermediate",
            "statement": """The complexation of 1,6-bis(trimethylammonium)diamantane (guest $G^{2+}$) with cucurbit[7]uril ($\\text{CB}[7]$) in neutral water exhibits a record association constant:
\\[
K_a = 7.20 \\times 10^{17}\\text{ M}^{-1} \\quad \\text{at } T = 298.15\\text{ K}
\\]
(a) Calculate the standard Gibbs free energy of binding $\\Delta G^\circ$ in $\\text{kJ/mol}$.
(b) If an equimolar solution of $\\text{CB}[7]$ and $G^{2+}$ is prepared at initial analytical concentrations $C_0 = 1.00 \\times 10^{-6}\\text{ M}$ ($1.00\\,\\mu\\text{M}$):
    (i) Calculate the equilibrium concentration of uncomplexed free host $[\\text{CB}[7]]$.
    (ii) How many uncomplexed host molecules are present in a $1.00\\text{ L}$ volume of this solution?
(c) The complexation rate constant is nearly diffusion-controlled: $k_{\\text{on}} = 2.40 \\times 10^8\\text{ M}^{-1}\\text{s}^{-1}$. Calculate the dissociation rate constant $k_{\\text{off}}$ and the unimolecular dissociation half-life $t_{1/2}$ of the complex in years.""",
            "solution": """### Step 1: Standard Free Energy of Binding
Using $\\Delta G^\circ = -RT \\ln K_a$:
\\[
\\Delta G^\\circ = -(8.31446 \\times 298.15) \\times \\ln(7.20 \\times 10^{17}) = -2478.96 \\times (41.1147) = -101{,}922\\text{ J/mol} = -101.92\\text{ kJ/mol}
\\]
The binding free energy exceeds $100\\text{ kJ/mol}$, an exceptional value for a non-covalent supramolecular complex.

### Step 2: Equilibrium Concentrations and Free Molecules
Let $[\text{CB}[7]] = [G^{2+}] = x$.
The complex concentration is $[\text{CB}[7]\\cdot G^{2+}] = C_0 - x \\approx C_0 = 1.00 \\times 10^{-6}\\text{ M}$.
\\[
K_a = \\frac{C_0 - x}{x^2} \\approx \\frac{C_0}{x^2} \\implies x^2 = \\frac{C_0}{K_a}
\\]
\\[
x^2 = \\frac{1.00 \\times 10^{-6}\\text{ M}}{7.20 \\times 10^{17}\\text{ M}^{-1}} = 1.3889 \\times 10^{-24}\\text{ M}^2
\\]
\\[
x = [\\text{CB}[7]] = \\sqrt{1.3889 \\times 10^{-24}} = 1.1785 \\times 10^{-12}\\text{ M} = 1.18\\text{ pM}
\\]
In a $1.00\\text{ L}$ solution, the total number of free host molecules is:
\\[
N_{\\text{free}} = x \\times V \\times N_A = (1.1785 \\times 10^{-12}\\text{ mol/L}) \\times (1.00\\text{ L}) \\times (6.02214 \\times 10^{23}\\text{ mol}^{-1}) = 7.10 \\times 10^{11}\\text{ molecules}
\\]
Over $99.99988\\%$ of all host and guest molecules are assembled into complexes.

### Step 3: Dissociation Rate and Lifetime
From the detailed balance relation:
\\[
K_a = \\frac{k_{\\text{on}}}{k_{\\text{off}}} \\implies k_{\\text{off}} = \\frac{k_{\\text{on}}}{K_a}
\\]
Substitute given values:
\\[
k_{\\text{off}} = \\frac{2.40 \\times 10^8\\text{ M}^{-1}\\text{s}^{-1}}{7.20 \\times 10^{17}\\text{ M}^{-1}} = 3.333 \\times 10^{-10}\\text{ s}^{-1}
\\]
The dissociation half-life is:
\\[
t_{1/2} = \\frac{\\ln 2}{k_{\\text{off}}} = \\frac{0.693147}{3.333 \\times 10^{-10}\\text{ s}^{-1}} = 2.079 \\times 10^9\\text{ seconds}
\\]
Converting seconds to years ($1\\text{ year} = 365.25 \\times 86{,}400 = 31{,}557{,}600\\text{ s}$):
\\[
t_{1/2} = \\frac{2.079 \\times 10^9\\text{ s}}{3.1558 \\times 10^7\\text{ s/year}} = 65.89\\text{ years}
\\]
Once formed, an individual complex requires approximately 66 years on average to undergo spontaneous thermal dissociation."""
        },
        {
            "probNumber": "5.6",
            "title": "Channel Inclusion Selectivity: Urea vs Thiourea Alkane Branching",
            "difficulty": "Intermediate",
            "statement": """An equimolar binary mixture of $n$-octane ($n-\\text{C}_8\\text{H}_{18}$, effective cross-sectional diameter $d = 4.5\\text{ Å}$) and 2,2,4-trimethylpentane (isooctane, effective cross-sectional diameter $d = 6.2\\text{ Å}$) is subjected to inclusion crystallization:
- Experiment A: Crystallization with excess urea in methanol/benzene.
- Experiment B: Crystallization with excess thiourea in methanol.
(a) Predict which alkane is selectively trapped in the solid host lattice in Experiment A and Experiment B.
(b) The inclusion channel cross-section can be modeled as a hard cylinder of radius $R_{\\text{ch}}$ ($R_{\\text{urea}} = 2.55\\text{ Å}$, $R_{\\text{thiourea}} = 3.45\\text{ Å}$) with a Lennard-Jones (12-6) wall potential. Calculate the cross-sectional clearance $\\Delta r = R_{\\text{ch}} - r_{\\text{guest}}$ for each host-guest pair.
(c) In Experiment A, the isolated urea clathrate has a stoichiometry of $1\\text{ mole } n\\text{-octane} : 6.73\\text{ moles urea}$. Given that the $c$-axis repeat unit of the hexagonal urea channel is $c = 11.02\\text{ Å}$ containing 6 urea molecules, calculate the pitch length per alkane molecule $L_{\\text{octane}}$ in the channel and compare it to the theoretical extended length of an $n$-octane molecule ($11.5\\text{ Å}$).""",
            "solution": """### Step 1: Qualitative Inclusion Selectivity
1. **Experiment A (Urea)**:
   - Hexagonal urea channels possess an internal diameter of $5.1\\text{ Å}$ ($R_{\\text{urea}} = 2.55\\text{ Å}$).
   - Linear $n$-octane ($d = 4.5\\text{ Å}$) fits comfortably inside the cylindrical channel, forming dense van der Waals contacts with the channel walls.
   - Isooctane ($d = 6.2\\text{ Å}$) exceeds the channel diameter ($6.2 > 5.1\\text{ Å}$) and cannot enter without severely disrupting the lattice.
   - Result: **$n$-Octane is selectively included**; isooctane remains in the liquid phase.
2. **Experiment B (Thiourea)**:
   - Thiourea channels possess an expanded internal diameter of $6.9\\text{ Å}$ ($R_{\\text{thiourea}} = 3.45\\text{ Å}$).
   - Isooctane ($d = 6.2\\text{ Å}$) matches the expanded diameter with an optimal packing fraction.
   - Linear $n$-octane ($d = 4.5\\text{ Å}$) is too slender; the empty void space cannot provide sufficient dispersive stabilization to overcome the lattice reconstruction penalty.
   - Result: **Isooctane is selectively included**; $n$-octane remains in the liquid phase.

### Step 2: Cross-Sectional Clearance Evaluation
- For $n$-octane: $r_1 = 4.5 / 2 = 2.25\\text{ Å}$.
- For isooctane: $r_2 = 6.2 / 2 = 3.10\\text{ Å}$.

1. **Urea Host ($R = 2.55\\text{ Å}$)**:
   - $\\Delta r(\\text{octane}) = 2.55 - 2.25 = +0.30\\text{ Å}$ (ideal positive clearance; optimal van der Waals contact).
   - $\\Delta r(\\text{isooctane}) = 2.55 - 3.10 = -0.55\\text{ Å}$ (severe negative clearance; massive steric Pauli repulsion).
2. **Thiourea Host ($R = 3.45\\text{ Å}$)**:
   - $\\Delta r(\\text{octane}) = 3.45 - 2.25 = +1.20\\text{ Å}$ (excessive clearance; loose fit, negligible attractive dispersion).
   - $\\Delta r(\\text{isooctane}) = 3.45 - 3.10 = +0.35\\text{ Å}$ (ideal positive clearance; close contacts with channel walls).

### Step 3: Channel Pitch Length and Packing Density
Given:
- One unit cell along the $c$-axis has length $c = 11.02\\text{ Å}$ and contains 6 urea molecules.
- The experimental molar ratio is $n = 6.73\\text{ urea / octane}$.
The channel length occupied by one mole of $n$-octane is:
\\[
L_{\\text{octane}} = \\frac{n_{\\text{urea}}}{6} \\times c = \\frac{6.73}{6} \\times 11.02\\text{ Å} = 1.1217 \\times 11.02\\text{ Å} = 12.36\\text{ Å}
\\]
- Comparing with the theoretical fully extended length of an isolated $n$-octane molecule ($L_{\\text{mol}} \\approx 11.5\\text{ Å}$, accounting for van der Waals caps):
\\[
\\Delta L = L_{\\text{octane}} - L_{\\text{mol}} = 12.36 - 11.50 = 0.86\\text{ Å}
\\]
The intermolecular head-to-tail separation between adjacent octane molecules along the channel is $0.86\\text{ Å}$, corresponding to typical van der Waals contact distances between terminal methyl groups in one-dimensional molecular arrays."""
        },
        {
            "probNumber": "5.7",
            "title": "Statistical Mechanics of Gas Hydrate Cage Adsorption: van der Waals-Platteeuw Model",
            "difficulty": "Advanced",
            "statement": """The thermodynamic stability of clathrate hydrates is governed by the statistical mechanical **van der Waals and Platteeuw (vdWP)** theory. The chemical potential difference between the empty metastable water lattice ($\\mu_w^{\\beta}$) and the occupied gas hydrate ($\\mu_w^H$) is:
\\[
\\Delta \\mu_w = \\mu_w^\\beta - \\mu_w^H = -k_B T \\sum_{i} \\nu_i \\ln(1 - \\theta_i)
\\]
where $\\nu_i$ is the number of type-$i$ cages per water molecule, and $\\theta_i$ is the Langmuir fractional occupancy of type-$i$ cages:
\\[
\\theta_i = \\frac{C_i f}{1 + C_i f}
\\]
where $C_i(T)$ is the Langmuir adsorption constant and $f$ is the guest fugacity.
For Structure I methane hydrate:
- Cage 1 (small $5^{12}$): $\\nu_1 = 2/46 = 1/23$, $C_1(273.15\\text{ K}) = 0.125\\text{ MPa}^{-1}$.
- Cage 2 (large $5^{12}6^2$): $\\nu_2 = 6/46 = 3/23$, $C_2(273.15\\text{ K}) = 0.740\\text{ MPa}^{-1}$.
The critical chemical potential difference required to stabilize the sI lattice against decomposition into liquid water at $273.15\\text{ K}$ is $\\Delta \\mu_w^* = 1.297 \\times 10^3\\text{ J/mol}$.
(a) Express $\\Delta \\mu_w$ in terms of fugacity $f$ and calculate its value at $f = 2.50\\text{ MPa}$.
(b) Determine whether methane hydrate is thermodynamically stable at $f = 2.50\\text{ MPa}$ and $T = 273.15\\text{ K}$.
(c) Calculate the three-phase equilibrium dissociation fugacity $f_{\\text{eq}}$ at which $\\Delta \\mu_w(f_{\\text{eq}}) = \\Delta \\mu_w^*$, using Newton-Raphson iteration.""",
            "solution": """### Step 1: Chemical Potential Formulation at $f = 2.50\text{ MPa}$
Substitute Langmuir occupancies $\\theta_i$:
\\[
1 - \\theta_i = 1 - \\frac{C_i f}{1 + C_i f} = \\frac{1}{1 + C_i f}
\\]
Thus:
\\[
\\ln(1 - \\theta_i) = -\\ln(1 + C_i f)
\\]
The molar chemical potential difference (per mole of water, $R = N_A k_B = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$) is:
\\[
\\Delta \\mu_w(f) = R T \\left[ \\nu_1 \\ln(1 + C_1 f) + \\nu_2 \\ln(1 + C_2 f) \\right]
\\]
At $T = 273.15\\text{ K}$, $RT = 8.31446 \\times 273.15 = 2{,}271.09\\text{ J/mol}$.
With $f = 2.50\\text{ MPa}$:
- $1 + C_1 f = 1 + (0.125)(2.50) = 1 + 0.3125 = 1.3125$
  $\\ln(1.3125) = 0.27193$
- $1 + C_2 f = 1 + (0.740)(2.50) = 1 + 1.850 = 2.850$
  $\\ln(2.850) = 1.04732$
Substitute into the summation:
\\[
\\sum = \\frac{1}{23}(0.27193) + \\frac{3}{23}(1.04732) = 0.011823 + 0.136607 = 0.148430
\\]
\\[
\\Delta \\mu_w = 2{,}271.09 \\times 0.148430 = 337.10\\text{ J/mol}
\\]

### Step 2: Stability Assessment
Compare calculated $\\Delta \\mu_w$ with the critical threshold $\\Delta \\mu_w^*$:
\\[
\\Delta \\mu_w(2.50\\text{ MPa}) = 337.1\\text{ J/mol} < \\Delta \\mu_w^* = 1{,}297.0\\text{ J/mol}
\\]
Because the chemical potential lowering provided by guest entrapment ($337.1\\text{ J/mol}$) is less than the critical stabilization energy required ($1{,}297.0\\text{ J/mol}$), the hydrate is **thermodynamically unstable** at $f = 2.50\\text{ MPa}$; it will spontaneously dissociate into liquid water and gaseous methane.

### Step 3: Equilibrium Dissociation Fugacity $f_{\\text{eq}}$
We solve:
\\[
g(f) = \\frac{1}{23} \\ln(1 + 0.125 f) + \\frac{3}{23} \\ln(1 + 0.740 f) - \\frac{1{,}297.0}{2{,}271.09} = 0
\\]
Target value:
\\[
\\frac{1{,}297.0}{2{,}271.09} = 0.57109
\\]
Let us test values of $f$:
- If $f = 10.0\\text{ MPa}$:
  $\\ln(1 + 1.25) = \\ln(2.25) = 0.81093$
  $\\ln(1 + 7.40) = \\ln(8.40) = 2.12823$
  $\\sum = \\frac{1}{23}(0.81093) + \\frac{3}{23}(2.12823) = 0.03526 + 0.27759 = 0.31285 < 0.57109$
- If $f = 25.0\\text{ MPa}$:
  $\\ln(1 + 3.125) = \\ln(4.125) = 1.41707$
  $\\ln(1 + 18.5) = \\ln(19.5) = 2.97041$
  $\\sum = \\frac{1}{23}(1.41707) + \\frac{3}{23}(2.97041) = 0.06161 + 0.38744 = 0.44905 < 0.57109$
- If $f = 50.0\\text{ MPa}$:
  $\\ln(1 + 6.25) = \\ln(7.25) = 1.98100$
  $\\ln(1 + 37.0) = \\ln(38.0) = 3.63759$
  $\\sum = \\frac{1}{23}(1.98100) + \\frac{3}{23}(3.63759) = 0.08613 + 0.47447 = 0.56060 \\approx 0.57109$
- If $f = 53.5\\text{ MPa}$:
  $\\ln(1 + 0.125 \\times 53.5) = \\ln(7.6875) = 2.0396$
  $\\ln(1 + 0.740 \\times 53.5) = \\ln(40.59) = 3.7035$
  $\\sum = \\frac{2.0396 + 3(3.7035)}{23} = \\frac{2.0396 + 11.1105}{23} = \\frac{13.1501}{23} = 0.57174$
Thus, the three-phase equilibrium dissociation fugacity is:
\\[
f_{\\text{eq}} \\approx 53.2\\text{ MPa}
\\]
At $273.15\\text{ K}$, pure methane requires high pressures to form a stable hydrate in the absence of secondary co-guests."""
        },
        {
            "probNumber": "5.8",
            "title": "Redox-Switchable Inclusion in Calix[4]diquinone: Cyclic Voltammetry",
            "difficulty": "Advanced",
            "statement": """A redox-active calix[4]diquinone host ($H$) incorporates two opposite 1,4-benzoquinone rings and two opposite phenolic rings in a cone conformation.
In dry acetonitrile, free host $H$ undergoes two reversible sequential one-electron reductions:
1. $H + e^- \\rightleftharpoons H^{-\\bullet}$, with $E_1^\circ = -0.450\\text{ V}$ vs $\\text{Fc}/\\text{Fc}^+$.
2. $H^{-\\bullet} + e^- \\rightleftharpoons H^{2-}$, with $E_2^\circ = -0.920\\text{ V}$ vs $\\text{Fc}/\\text{Fc}^+$.
When potassium cation ($\\text{K}^+$) is titrated into the solution:
- The neutral host binds $\\text{K}^+$ with modest affinity: $K_a(H) = 4.50 \\times 10^2\\text{ M}^{-1}$.
- In the presence of excess $\\text{K}^+$, both redox waves shift anodically:
  $E_1^{\\text{bound}} = -0.180\\text{ V}$ and $E_2^{\\text{bound}} = -0.480\\text{ V}$.
(a) Calculate the cathodic shift $\\Delta E_1 = E_1^{\\text{bound}} - E_1^\circ$ and $\\Delta E_2 = E_2^{\\text{bound}} - E_2^\circ$.
(b) Using the thermodynamic cycle equation $\\Delta E = \\frac{RT}{F} \\ln(K_{\\text{red}} / K_{\\text{ox}})$, calculate:
    (i) The association constant of the radical anion host with potassium, $K_a(H^{-\\bullet})$,
    (ii) The association constant of the dianion host with potassium, $K_a(H^{2-})$ at $298.15\\text{ K}$.
(c) Explain the electronic and electrostatic origin of the massive enhancement in $\\text{K}^+$ affinity as the quinone rings are reduced to semiquinone radical anions and catecholate dianions.""",
            "solution": """### Step 1: Potential Shifts
Given:
- $E_1^\\circ = -0.450\\text{ V}$, $E_1^{\\text{bound}} = -0.180\\text{ V}$
- $E_2^\\circ = -0.920\\text{ V}$, $E_2^{\\text{bound}} = -0.480\\text{ V}$

1. **Shift for First Reduction**:
\\[
\\Delta E_1 = E_1^{\\text{bound}} - E_1^\\circ = -0.180 - (-0.450) = +0.270\\text{ V} = +270\\text{ mV}
\\]
2. **Shift for Second Reduction**:
\\[
\\Delta E_2 = E_2^{\\text{bound}} - E_2^\\circ = -0.480 - (-0.920) = +0.440\\text{ V} = +440\\text{ mV}
\\]
Both waves undergo dramatic positive (anodic) shifts, demonstrating that $\\text{K}^+$ binds far more strongly to the reduced states than to the neutral host.

### Step 2: Association Constants of Reduced States
From the thermodynamic square cycle:
\\[
\\Delta E_1 = \\frac{RT}{F} \\ln\\left( \\frac{K_a(H^{-\\bullet})}{K_a(H)} \\right)
\\]
where $RT/F = 0.025693\\text{ V}$ at $298.15\\text{ K}$.
1. **For $H^{-\\bullet}$**:
\\[
\\ln\\left( \\frac{K_a(H^{-\\bullet})}{K_a(H)} \\right) = \\frac{0.270\\text{ V}}{0.025693\\text{ V}} = 10.5087
\\]
\\[
\\frac{K_a(H^{-\\bullet})}{K_a(H)} = e^{10.5087} = 3.663 \\times 10^4
\\]
With $K_a(H) = 4.50 \\times 10^2\\text{ M}^{-1}$:
\\[
K_a(H^{-\\bullet}) = (4.50 \\times 10^2) \\times (3.663 \\times 10^4) = 1.648 \\times 10^7\\text{ M}^{-1}
\\]

2. **For $H^{2-}$**:
For the second reduction:
\\[
\\Delta E_2 = \\frac{RT}{F} \\ln\\left( \\frac{K_a(H^{2-})}{K_a(H^{-\\bullet})} \\right)
\\]
\\[
\\ln\\left( \\frac{K_a(H^{2-})}{K_a(H^{-\\bullet})} \\right) = \\frac{0.440\\text{ V}}{0.025693\\text{ V}} = 17.1253
\\]
\\[
\\frac{K_a(H^{2-})}{K_a(H^{-\\bullet})} = e^{17.1253} = 2.738 \\times 10^7
\\]
With $K_a(H^{-\\bullet}) = 1.648 \\times 10^7\\text{ M}^{-1}$:
\\[
K_a(H^{2-}) = (1.648 \\times 10^7) \\times (2.738 \\times 10^7) = 4.512 \\times 10^{14}\\text{ M}^{-1}
\\]
The total enhancement from neutral host to dianion host is:
\\[
\\frac{K_a(H^{2-})}{K_a(H)} = \\frac{4.512 \\times 10^{14}}{450} = 1.003 \\times 10^{12} \\quad (\\text{a trillion-fold increase!})
\\]

### Step 3: Electrostatic and Electronic Mechanism
1. **Neutral Host**: The quinone carbonyl oxygens are weakly polarized, offering only modest dipole-cation stabilization ($-\\text{C}=\\text{O}^{\\delta-}\\cdots\\text{K}^+$).
2. **Semiquinone Radical Anion ($H^{-\\bullet}$)**: One electron enters the lowest unoccupied molecular orbital (LUMO, $\\pi^*$), delocalizing negative charge directly onto the quinone oxygen atoms. Strong ion-ion Coulombic attraction ($-\\text{O}^-\\cdots\\text{K}^+$) enhances affinity by four orders of magnitude.
3. **Catecholate Dianion ($H^{2-}$)**: Reduction of the second quinone creates a full doubly negative cavity. The converged array of negatively charged oxygen atoms forms an exceptionally deep electrostatic potential well, coordinating $\\text{K}^+$ with femtomolar affinity ($K_a > 10^{14}\\text{ M}^{-1}$)."""
        },
        {
            "probNumber": "5.9",
            "title": "Cucurbit[8]uril 1:2 Ternary Complexation Cooperativity & Charge-Transfer Intercalation",
            "difficulty": "Advanced",
            "statement": """Cucurbit[8]uril ($\\text{CB}[8]$) possesses an enormous internal cavity volume ($479\\text{ Å}^3$) capable of simultaneously encapsulating two planar aromatic guests in a face-to-face $\\pi-\\pi$ stacked geometry.
In aqueous solution at $298.15\\text{ K}$, $\\text{CB}[8]$ forms a ternary $1:1:1$ heterocomplex with an electron-deficient dication methyl viologen ($\text{MV}^{2+}$) and an electron-rich neutral 2,6-dihydroxynaphthalene ($\text{DHN}$):
\\[
\\text{CB}[8] + \\text{MV}^{2+} \\xrightleftharpoons{K_1} [\\text{CB}[8]\\cdot \\text{MV}]^{2+}
\\]
\\[
[\\text{CB}[8]\\cdot \\text{MV}]^{2+} + \\text{DHN} \\xrightleftharpoons{K_2} [\\text{CB}[8]\\cdot \\text{MV} \\cdot \\text{DHN}]^{2+}
\\]
Direct measurements yield:
- $K_1 = 1.10 \\times 10^5\\text{ M}^{-1}$ (binding of $\text{MV}^{2+}$ to empty $\text{CB}[8]$).
- $K_2 = 8.40 \\times 10^6\\text{ M}^{-1}$ (binding of $\text{DHN}$ to the binary $[\\text{CB}[8]\\cdot \\text{MV}]^{2+}$ complex).
In contrast, the binding of neutral $\text{DHN}$ directly to empty $\text{CB}[8]$ is $K_{1}' = 2.50 \\times 10^3\\text{ M}^{-1}$.
(a) Calculate the cooperativity factor $\\alpha = K_2 / K_1'$ for the inclusion of $\text{DHN}$.
(b) Calculate the standard Gibbs free energy of cooperativity $\\Delta \\Delta G_{\\text{coop}}^\circ = -RT \\ln \\alpha$.
(c) The ternary complex displays an intense charge-transfer (CT) absorption band at $\\lambda_{\\max} = 525\\text{ nm}$ (molar absorptivity $\\epsilon = 2{,}450\\text{ M}^{-1}\\text{cm}^{-1}$). If an equimolar solution of $\\text{CB}[8]$, $\text{MV}^{2+}$, and $\text{DHN}$ is prepared at analytical concentrations $C_0 = 1.00 \\times 10^{-4}\\text{ M}$ ($100\\,\\mu\\text{M}$), calculate the equilibrium concentration of the ternary complex and the optical absorbance in a $1.00\\text{ cm}$ pathlength quartz cuvette.""",
            "solution": """### Step 1: Cooperativity Factor
The cooperativity factor $\\alpha$ evaluates how the pre-encapsulation of $\\text{MV}^{2+}$ enhances the binding affinity for the second guest $\\text{DHN}$:
\\[
\\alpha = \\frac{K_2}{K_1'} = \\frac{8.40 \\times 10^6\\text{ M}^{-1}}{2.50 \\times 10^3\\text{ M}^{-1}} = 3{,}360
\\]
Because $\\alpha = 3{,}360 \\gg 1$, the ternary assembly exhibits **intense positive homotropic/heterotropic cooperativity**.

### Step 2: Free Energy of Cooperativity
The free energy advantage gained from cooperativity is:
\\[
\\Delta \\Delta G_{\\text{coop}}^\\circ = -RT \\ln \\alpha
\\]
With $RT = 8.31446 \\times 298.15 = 2{,}478.96\\text{ J/mol} = 2.47896\\text{ kJ/mol}$:
\\[
\\Delta \\Delta G_{\\text{coop}}^\\circ = -2.47896 \\times \\ln(3{,}360) = -2.47896 \\times 8.1197 = -20.128\\text{ kJ/mol}
\\]
- **Physical Basis**: Inside the confined hydrophobic cavity of $\\text{CB}[8]$, the electron-deficient dication $\\text{MV}^{2+}$ and electron-rich $\\text{DHN}$ undergo face-to-face donor-acceptor $\\pi-\\pi$ overlap and charge-transfer (CT) complexation. This interaction is strongly shielded from competitive hydration by the hydrophobic cucurbituril walls, contributing over $-20\\text{ kJ/mol}$ of additional stabilization.

### Step 3: Ternary Assembly Concentration and Absorbance
The overall ternary association constant is:
\\[
\\beta_2 = K_1 \\times K_2 = (1.10 \\times 10^5) \\times (8.40 \\times 10^6) = 9.24 \\times 10^{11}\\text{ M}^{-2}
\\]
For initial concentrations $[\text{CB}[8]]_0 = [\text{MV}^{2+}]_0 = [\text{DHN}]_0 = C_0 = 1.00 \\times 10^{-4}\\text{ M}$.
Let $T = [[\\text{CB}[8]\\cdot \\text{MV} \\cdot \\text{DHN}]^{2+}]$.
Because $\\beta_2 = 9.24 \\times 10^{11}\\text{ M}^{-2}$ is very large:
Let $x$ be the uncomplexed fraction, such that $T = C_0(1 - \\delta)$.
Let us compute the exact equilibrium:
From the stepwise equilibria:
1. $[\\text{CB}\\cdot\\text{MV}] = K_1 [\\text{CB}] [\\text{MV}]$
2. $T = K_2 [\\text{CB}\\cdot\\text{MV}] [\\text{DHN}] = \\beta_2 [\\text{CB}] [\\text{MV}] [\\text{DHN}]$
Because $[\text{CB}]_0 = [\text{MV}]_0 = [\text{DHN}]_0 = C_0$:
$[\\text{CB}] \\approx [\\text{MV}] \\approx [\\text{DHN}] = c_{\\text{free}}$.
Then $T \\approx C_0 - c_{\\text{free}}$, and:
\\[
\\beta_2 c_{\\text{free}}^3 + c_{\\text{free}} - C_0 \\approx 0
\\]
With $\\beta_2 = 9.24 \\times 10^{11}$ and $C_0 = 1.00 \\times 10^{-4}$:
\\[
c_{\\text{free}}^3 \\approx \\frac{C_0}{\\beta_2} = \\frac{1.00 \\times 10^{-4}}{9.24 \\times 10^{11}} = 1.082 \\times 10^{-16}\\text{ M}^3
\\]
\\[
c_{\\text{free}} = (1.082 \\times 10^{-16})^{1/3} = 4.765 \\times 10^{-6}\\text{ M}
\\]
Therefore, the ternary complex concentration is:
\\[
T = C_0 - c_{\\text{free}} = 1.00 \\times 10^{-4} - 0.04765 \\times 10^{-4} = 0.95235 \\times 10^{-4}\\text{ M} = 95.24\\,\\mu\\text{M}
\\]
Yield of the ternary complex:
\\[
\\text{Yield} = \\frac{T}{C_0} \\times 100\\% = 95.24\\%
\\]
Now compute the optical absorbance via the Beer-Lambert law ($l = 1.00\\text{ cm}$, $\\epsilon = 2{,}450\\text{ M}^{-1}\\text{cm}^{-1}$):
\\[
A_{525} = \\epsilon \\cdot c \\cdot l = (2{,}450\\text{ M}^{-1}\\text{cm}^{-1}) \\times (9.524 \\times 10^{-5}\\text{ M}) \\times (1.00\\text{ cm}) = 0.2333 \\approx 0.233
\\]
The solution displays a distinct ruby-red color with an absorbance of $A = 0.233$ at $525\\text{ nm}$."""
        }
    ]

    return {
        "id": "unit-5",
        "number": 5,
        "title": "Clathrates, Inclusion Compounds & Macrocyclic Cavities",
        "leadSummary": "Solid-state clathrates and clathrate hydrates (Structures I, II, H), channel inclusion hosts (urea, thiourea, Dianin's compound), Werner complexes and Hofmann cyanometallate clathrates, cyclodextrins (alpha, beta, gamma) and the hydrophobic effect in cavity inclusion, calixarenes and resorcinarenes (cone, partial cone, alternate conformers), cucurbit[n]urils and ultra-high affinity binding, and pillar[n]arenes and cavitands.",
        "simulations": ["sim_supra_cyclodextrin_inclusion"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u5 = get_unit_5()
    print(f"Unit 5 generated: {len(u5['sections'])} sections, {len(u5['problems'])} problems.")
