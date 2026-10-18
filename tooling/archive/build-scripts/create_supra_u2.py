"""
create_supra_u2.py
Creates Unit 2 data dictionary for Supramolecular Chemistry:
Cation-Binding Macrocycles: Crown Ethers, Cryptands & Spherands
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_2():
    sections = [
        {
            "secNumber": "2.1",
            "title": "Crown Ethers: Discovery, Nomenclature, Ring Geometries & Conformational Ensembles",
            "content": """The inception of modern supramolecular chemistry traces to 1967, when Charles J. Pedersen of DuPont inadvertently isolated dibenzo-18-crown-6 during an attempted synthesis of a bis-phenol ligand. Upon treating the reaction mixture with methanol, he observed that the insoluble white byproduct dissolved readily in the presence of sodium salts, revealing a new class of cyclic polyethers capable of binding alkali cations.

### Nomenclature of Crown Ethers
Pedersen devised an intuitive shorthand nomenclature system:
\\[
[\\text{Substituents}]\\text{-}[\\text{Total Ring Atoms}]\\text{-crown-}[\\text{Number of Oxygen Atoms}]
\\]
- **12-crown-4 (12C4)**: 1,4,7,10-tetraoxacyclododecane (12-membered ring with 4 oxygens).
- **15-crown-5 (15C5)**: 1,4,7,10,13-pentaoxacyclopentadecane (15-membered ring with 5 oxygens).
- **18-crown-6 (18C6)**: 1,4,7,10,13,16-hexaoxacyclooctadecane (18-membered ring with 6 oxygens).
- **Dibenzo-18-crown-6 (DB18C6)**: Two fused catechol aromatic rings flanking an 18-membered hexaether core.

### Conformational Ensembles and Cavity Geometries
The uncomplexed 18-crown-6 macrocycle in solution does not adopt an open, circular $D_{3d}$ conformation. Instead, to minimize electrostatic repulsion between neighboring oxygen lone pairs and alleviate gauche steric repulsions among methylene units:
- **Free 18-Crown-6**: Adopts an elliptical, pseudo-rectangular $C_i$ conformation in which two oxygen lone pairs turn outward into solvent and two turn inward, self-closing the central cavity.
- **Complexed 18-Crown-6**: Upon binding a complementary cation (such as $\\text{K}^+$), the macrocycle reorganizes into a highly symmetric crown-like $D_{3d}$ conformation. All six oxygen atoms become coplanar, directing their partial negative charges inward to form a circular cavity of diameter $2.6 - 3.2\\text{ Å}$, perfectly coordinating the equatorial perimeter of the cation."""
        },
        {
            "secNumber": "2.2",
            "title": "Synthetic Methodologies: The Kinetic and Thermodynamic Metal Template Effect",
            "content": """The synthesis of macrocyclic compounds represents a challenging organic problem because linear bifunctional precursors naturally favor intermolecular polycondensation into polymers over intramolecular cyclization. Pedersen and subsequent synthetic chemists overcame this by exploiting the **metal template effect**.

### The High-Dilution Technique (Ruggli-Ziegler Principle)
In the absence of a templating agent, cyclization requires extreme dilution:
- Intramolecular cyclization rate is first-order:
\\[
v_{\\text{intra}} = k_1 [\\text{A-B}]
\\]
- Intermolecular oligomerization rate is second-order:
\\[
v_{\\text{inter}} = k_2 [\\text{A-B}]^2
\\]
The ratio of rates is:
\\[
\\frac{v_{\\text{intra}}}{v_{\\text{inter}}} = \\frac{k_1}{k_2 [\\text{A-B}]}
\\]
As the initial precursor concentration $[\\text{A-B}] \\to 0$, intramolecular cyclization dominates. However, high-dilution syntheses require immense solvent volumes, slow addition rates via syringe pumps ($10^{-4}\\text{ M}$), and suffer from low volumetric efficiency.

### The Metal Ion Template Effect
Introducing an alkali or transition metal cation during Williamson etherification or Schiff base condensation transforms reaction kinetics and equilibria:
1. **Kinetic Template Effect**: The metal ion acts as an organizing center, binding the donor atoms of the open-chain precursor through ion-dipole or coordinate bonds. This wraps the reactive terminal functional groups into close spatial proximity, vastly increasing the effective local concentration $C_{\\text{eff}}$ for the final ring-closing nucleophilic substitution.
2. **Thermodynamic Template Effect**: The metal cation shifts a complex reversible reaction equilibrium (such as imine condensation) toward the cyclic product by forming an exceptionally stable, thermodynamically favored coordination complex, precipitating or isolating the macrocyclic product from the dynamic covalent pool.

For example, synthesizing 18-crown-6 from triethylene glycol and 1,2-bis(2-chloroethoxy)ethane in the presence of $\\text{K}^+$ yields $70 - 80\\%$ cyclic product, whereas using $\\text{Li}^+$ or $\\text{NMe}_4^+$ as the base cation drops the yield to $< 5\\%$."""
        },
        {
            "secNumber": "2.3",
            "title": "Podands, Lariat Ethers & Crown Ether Solubility Thermodynamics",
            "content": """The conceptual progression from flexible open-chain polyethers to macrocycles and three-dimensional cryptands gave rise to two structurally vital classes of cation receptors: **podands** and **lariat ethers**.

### Podands: Acyclic Polyether Hosts
Coined by Fritz Vögtle, **podands** (from Greek *pous*, foot) are open-chain analogues of crown ethers, such as oligoethylene glycol dimethyl ethers (glymes) or rigid aromatic polyethers terminated by bulky or coordinating end-groups (e.g., quinoline, anisole).
- **Thermodynamic Characteristics**: Podands exhibit lower binding constants ($10^2 - 10^4\\text{ M}^{-1}$) compared to crown ethers ($10^5 - 10^7\\text{ M}^{-1}$) due to the loss of conformational degrees of freedom upon wrapping around the guest.
- **Kinetic Characteristics**: Podands exhibit exceptionally fast association and dissociation rates, making them ideal for dynamic membrane transport where rapid guest release at the receiving interface is essential.

### Lariat Ethers: Macrobicyclic Topology on a Monocyclic Core
Introduced by George Gokel, **lariat ethers** ("lasso" ethers) combine the high stability of a macrocyclic ring with the rapid dynamics of a flexible pendant coordinating arm.
- Consist of a crown ether ring bearing one or two dynamic side arms containing donor atoms (e.g., $-\\text{CH}_2\\text{CH}_2\\text{OCH}_3$ or $-\\text{CH}_2\\text{CH}_2\\text{NH}_2$).
- The crown ring provides 2D equatorial preorganization, while the lariat arm folds over the axial face, providing a 3D cap that mimics the encapsulation of a cryptand while maintaining rapid ligand-exchange kinetics.

### Solubility and "Naked Anion" Reactivity
Crown ethers are lipophilic on their exterior aliphatic/aromatic surface while polar in their interior cavity. This unique amphiphilic architecture gives them remarkable solubility in non-polar organic solvents (benzene, toluene, $\\text{CH}_2\\text{Cl}_2$):
- In the presence of a crown ether, ionic salts such as $\\text{KMnO}_4$ or $\\text{KOH}$ dissolve readily in benzene, forming "purple benzene".
- Because the crown ether completely sequesters the $\\text{K}^+$ cation, the accompanying counteranion ($\\text{MnO}_4^-$ or $\\text{OH}^-$) is stripped of its hydration shell and lacks direct contact ion-pairing in the non-polar solvent. These **"naked anions"** possess extraordinarily elevated nucleophilicity and basicity, accelerating organic transformations by factors of $10^3$ to $10^6$."""
        },
        {
            "secNumber": "2.4",
            "title": "Bipyridine & Terpyridine Ligands: Syntheses, Redox Mechanics & Metal Coordination",
            "content": """Chelating polypyridyl ligands—most notably 2,2'-bipyridine ($\\text{bpy}$) and 2,2':6',2''-terpyridine ($\\text{tpy}$)—serve as premier building blocks in supramolecular chemistry, metallosupramolecular self-assembly, and artificial photosynthesis.

### Structure and Synthesis of 2,2'-Bipyridine
Uncoordinated 2,2'-bipyridine prefers an anti-coplanar conformation in the gas phase and solution to minimize electrostatic repulsion between the two nitrogen lone pairs.
- **Synthesis**:
  - Raney nickel catalyzed oxidative dimerization of pyridine at elevated temperatures.
  - Modern transition-metal-catalyzed cross-coupling: Ullmann coupling of 2-bromopyridine using activated copper, or Suzuki-Miyaura coupling of 2-pyridylboronic acid with 2-halopyridines.
- **Coordination Binding**: Upon coordination to a transition metal center, bipyridine undergoes an $anti \\to syn$ conformational rotation of $180^\\circ$ around the inter-ring $\\text{C2-C2'}$ single bond, forming a planar five-membered chelate ring with bite angle $\\theta_{\\text{bite}} \\approx 75 - 80^\\circ$.

### Electronic Structure: sigma-Donor and pi-Acceptor Mechanics
Bipyridine is a neutral bidentate ligand possessing both:
1. **$\\sigma$-Donor Character**: The two $sp^2$-hybridized nitrogen lone pairs donate electron density into empty metal $d$-orbitals.
2. **$\\pi$-Acceptor Character**: The low-lying unoccupied $\\pi^*$ antibonding molecular orbitals of the aromatic pyridine rings accept electron density from filled metal $d$-orbitals via **$\\pi$-backbonding** ($d_\\pi \\to \\pi^*$).

This synergistic bonding stabilizes low oxidation states and produces intense visible light absorption through **Metal-to-Ligand Charge Transfer (MLCT)** transitions. The prototypical complex $[\\text{Ru}(\\text{bpy})_3]^{2+}$ exhibits:
\\[
\\text{MLCT}: \\quad [\\text{Ru}^{\\text{II}}(\\text{bpy})_3]^{2+} + h\\nu \\longrightarrow [\\text{Ru}^{\\text{III}}(\\text{bpy})_2(\\text{bpy}^{\\bullet-})]^{2+*}
\\]
producing an excited state with a microsecond luminescence lifetime and potent dual oxidant/reductant redox properties.

### 2,2':6',2''-Terpyridine
Terpyridine is a meridional tridentate ligand coordinating three facial or equatorial sites with two contiguous five-membered chelate rings ($\theta_{\\text{bite}} \\approx 160^\\circ$ overall). Complexes of the type $[\\text{M}(\\text{tpy})_2]^{n+}$ exhibit strictly linear, non-chiral $D_{2d}$ rod-like topologies, making them ideal rigid directional linkers for 1D and 2D metallosupramolecular polymers and molecular wires."""
        },
        {
            "secNumber": "2.5",
            "title": "Cryptands and Macrobicyclic Hosts: Lehn's 3D Cavities",
            "content": """In 1969, Jean-Marie Lehn synthesized **cryptands** (from Greek *kryptos*, hidden), extending the 2D planar coordination of crown ethers into three-dimensional macrobicyclic cages.

### Structure and Nomenclature of Cryptands
Cryptands consist of two bridgehead tertiary nitrogen atoms connected by three oligoethylene glycol strands $-(\\text{CH}_2\\text{CH}_2\\text{O})_n\\text{CH}_2\\text{CH}_2-$. Lehn introduced a bracket notation reflecting the number of ether oxygens in each bridge:
- **[1.1.1] Cryptand**: One oxygen atom in each of the three bridges (4,7,13,18-tetraoxa-1,10-diazabicyclo[8.5.5]eicosane).
- **[2.1.1] Cryptand**: Bridges contain 2, 1, and 1 oxygen atoms.
- **[2.2.1] Cryptand**: Bridges contain 2, 2, and 1 oxygen atoms.
- **[2.2.2] Cryptand**: Two oxygen atoms in each bridge (4,7,13,16,21,24-hexaoxa-1,10-diazabicyclo[8.8.8]hexacosane).

### Inversion Isomerism of Bridgehead Nitrogens
Because bridgehead tertiary amines undergo nitrogen pyramidal inversion, cryptands exist in three distinct topological diastereomers:
1. **$out-out$ ($exo-exo$)**: Both nitrogen lone pairs point outward into solvent.
2. **$in-out$ ($endo-exo$)**: One lone pair points inward toward the cavity, and one points outward.
3. **$in-in$ ($endo-endo$)**: Both nitrogen lone pairs point directly into the central cavity.
The $in-in$ conformation is the thermodynamically active binding state, directing all eight donor atoms (two nitrogens and six oxygens in [2.2.2]) inward to form a spheroidal 3D coordination cage.

### The Macrobicyclic Cryptate Effect
When an alkali cation penetrates the cavity, it forms a **cryptate** complex $[\\text{M}^+ \\subset \\text{cryptand}]$:
- The cation is completely encapsulated, isolated from counteranions and bulk solvent molecules.
- Association constants are astronomically high: for $\\text{K}^+$ with [2.2.2] cryptand in water, $\\log K_a = 5.4$, and in $95\\%$ methanol, $\\log K_a = 10.5$ (compared to $\\log K_a = 6.1$ for 18-crown-6).
- Cryptands display sharp **peak selectivity curves**: [2.1.1] binds $\\text{Li}^+$ ($r = 0.76\\text{ Å}$) with maximum affinity, [2.2.1] selectively encapsulates $\\text{Na}^+$ ($r = 1.02\\text{ Å}$), and [2.2.2] binds $\\text{K}^+$ ($r = 1.38\\text{ Å}$) with a selectivity factor exceeding $10^4$ over $\\text{Na}^+$ and $\\text{Cs}^+$."""
        },
        {
            "secNumber": "2.6",
            "title": "Spherands, Cavitands & Carcerands: Cram's Rigid Preorganized Arenes",
            "content": """Donald J. Cram pushed the thermodynamic principle of preorganization to its ultimate limit by developing host architectures based on rigid aromatic backbones: **spherands**, **cavitands**, and **carcerands**.

### Spherands: Complete Structural Preorganization
Synthesized by Cram in 1979, spherands consist of rigid cyclic arrays of six or eight ortho-linked benzene rings (e.g., sexiphenylene) bearing inward-directed methoxy ($-\\text{OCH}_3$) groups:
- In the uncomplexed state, the rigid biphenyl steric clashes force the six methoxy oxygen atoms into an octahedral geometry around an empty spherical cavity of diameter $d = 1.62\\text{ Å}$.
- **Lone-Pair Repulsion**: In the free host, the six unshared electron pairs are held in forced proximity in a vacuum-like cavity, creating immense electrostatic repulsion.
- Upon complexation with $\\text{Li}^+$ or $\\text{Na}^+$, the cation directly neutralizes these congested electron pairs. No conformational rearrangement occurs ($\Delta S_{\\text{conf}}^\\circ \\approx 0$).
- As a consequence, spherands bind $\\text{Li}^+$ and $\\text{Na}^+$ with association constants exceeding $K_a > 10^{14}\\text{ M}^{-1}$ in non-polar solvents, vastly surpassing crown ethers and cryptands. Spherands reject $\\text{K}^+$ entirely because $\\text{K}^+$ ($d = 2.76\\text{ Å}$) is too large to enter the non-expandable rigid cavity.

### Cavitands: Open Enforced Molecular Bowls
Cavitands are synthetic organic hosts possessing enforced concave cavities capable of housing small organic molecules or ions. Built from resorcinol-aldehyde condensation products (resorcinarenes) bridged by methylene or dialkylsilyl groups:
- The four aromatic rings are locked into an immovable upright bowl (cone) conformation.
- The depth and rim functionalities of cavitands can be tailored to bind complementary guests such as chloroform, acetonitrile, or choline.

### Carcerands and Carceplexes: Molecular Imprisonment
By linking two cavitand bowls rim-to-rim via covalent spacers, Cram synthesized **carcerands**—closed spherical molecular containers with no portals large enough for trapped guests to escape without breaking covalent bonds:
\\[
\\text{Carcerand} + \\text{Guest} \\xrightarrow{\\text{covalent closure}} [\\text{Guest} \\subset \\text{Carcerand}] \\quad (\\text{Carceplex})
\\]
Guests trapped inside carceplexes (such as cyclobutadiene, a normally unstable antiaromatic intermediate) are permanently stabilized at room temperature because reactive external reagents cannot penetrate the protective aromatic shell."""
        },
        {
            "secNumber": "2.7",
            "title": "Cation Selectivity Curves & Enthalpy-Entropy Compensation",
            "content": """The hallmark of crown ether and cryptand host-guest chemistry is cation-size selectivity, quantitatively described by stability constant profiles plotted against ionic radii.

### The Hole-Size Matching Rule
The classical "hole-size matching rule" asserts that maximum complex stability is achieved when the ionic diameter of the guest cation ($2 r_{\\text{ion}}$) matches the internal cavity diameter of the macrocyclic host ($D_{\\text{cav}}$):

| Host Macrocycle | Cavity Diameter ($D_{\\text{cav}}$, Å) | Optimal Cation | Cation Diameter ($2 r_{\\text{ion}}$, Å) | $\\log K_a$ (in MeOH) |
| :--- | :--- | :--- | :--- | :--- |
| **12-crown-4** | $1.20 - 1.50$ | $\\text{Li}^+$ | $1.52$ | $3.1$ |
| **15-crown-5** | $1.70 - 2.20$ | $\\text{Na}^+$ | $2.04$ | $4.3$ |
| **18-crown-6** | $2.60 - 3.20$ | $\\text{K}^+$ | $2.76$ | $6.1$ |
| **Dibenzo-24-crown-8** | $4.00 - 5.00$ | $\\text{Cs}^+$ | $3.34$ | $3.8$ |

When a cation is too small for the cavity (e.g., $\\text{Na}^+$ in 18-crown-6), the macrocycle must distort into an elliptical geometry to contact the cation, paying a conformational strain penalty. When a cation is too large (e.g., $\\text{Cs}^+$ in 18-crown-6), the cation cannot enter the plane of the oxygens and sits perched above the macrocycle in a "nesting" or "sandwich" geometry ($1:2$ complex $[\\text{Cs}(\\text{18C6})_2]^+$).

### Enthalpy-Entropy Compensation (EEC)
Across hundreds of crown ether and cryptand thermodynamic measurements, a universal linear relationship is observed between binding enthalpy and entropy:
\\[
T\\Delta S^\\circ = \\alpha \\Delta H^\\circ + T\\Delta S_0^\\circ
\\]
where the slope $\\alpha$ typically ranges from $0.70$ to $0.95$.
- As the host binding sites coordinate more tightly with the cation (producing a more negative, favorable $\\Delta H^\\circ$), the entire host-guest complex and surrounding solvent shell become more structurally rigid and restricted in motion (producing a more negative, unfavorable $\\Delta S^\\circ$).
- Consequently, gains in binding enthalpy are substantially offset by entropic penalties:
\\[
\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ = (1 - \\alpha) \\Delta H^\\circ - T\\Delta S_0^\\circ
\\]
This fundamental thermodynamic compensation limits the net free energy gain achievable through simple electrostatic tuning."""
        },
        {
            "secNumber": "2.8",
            "title": "Phase Transfer Catalysis & Biological Ionophore Mimicry",
            "content": """The synthetic and biological utility of cation-binding macrocycles spans industrial synthesis, separation science, and molecular medicine.

### Phase Transfer Catalysis (PTC)
In synthetic chemistry, many nucleophilic substitutions involve an inorganic water-soluble salt (e.g., $\\text{KCN}, \\text{KF}, \\text{KMnO}_4$) reacting with an organic substrate dissolved in an immiscible organic solvent (e.g., alkyl halides in toluene):
- Without catalyst, reaction is impossible due to phase separation.
- Adding catalytic quantities of a crown ether (e.g., 18-crown-6 or dicyclohexano-18-crown-6) initiates catalytic transfer:
\\[
\\text{K}^+ \\text{X}^- (\\text{aq}) + \\text{Crown} (\\text{org}) \\xrightleftharpoons{} [\\text{K} \\subset \\text{Crown}]^+ \\text{X}^- (\\text{org})
\\]
- The lipophilic crown encapsulates $\\text{K}^+$ and pulls the inorganic anion $\\text{X}^-$ across the liquid-liquid phase boundary into the organic phase as a non-solvated ion pair.
- The "naked" anion $\\text{X}^-$ attacks the organic substrate at high velocity:
\\[
[\\text{K} \\subset \\text{Crown}]^+ \\text{X}^- (\\text{org}) + \\text{R-Cl} \\longrightarrow \\text{R-X} + [\\text{K} \\subset \\text{Crown}]^+ \\text{Cl}^-
\\]
- The crown ether shuttles back to the interface, exchanging $\\text{Cl}^-$ for a fresh $\\text{X}^-$, completing the catalytic cycle.

### Biological Ionophores: Valinomycin and Gramicidin
Crown ethers serve as synthetic models for natural antibiotic **ionophores** (ion carriers):
- **Valinomycin**: A cyclic depsipeptide consisting of twelve alternating amino acid and hydroxy acid residues:
\\[
\\text{cyclo-}[(\\text{D-Val}-\\text{L-Lac}-\\text{L-Val}-\\text{D-Hyi})_3]
\\]
In non-polar lipid membranes, valinomycin folds into a tennis-ball seam conformation where six ester carbonyl oxygens point inward to form an octahedral cavity of diameter $2.76\\text{ Å}$, perfectly matching $\\text{K}^+$ with a selectivity ratio of $K_a(\\text{K}^+) / K_a(\\text{Na}^+) > 10,\\!000$. Its lipophilic isopropyl and methyl side chains face outward, allowing it to traverse the hydrophobic interior of bacterial membranes, dissipating potassium electrochemical gradients and killing the cell."""
        }
    ]

    problems = [
        {
            "probNumber": "2.1",
            "title": "Cavity-to-Cation Size Matching: Quantitative Radius Ratios for Crown Ethers",
            "difficulty": "Foundational",
            "statement": """The effective ionic radii ($r_{\\text{ion}}$) of alkali metal cations and the internal cavity radii ($r_{\\text{cav}}$) of three crown ethers are:
- Cations: $\\text{Li}^+$ ($r = 0.76\\text{ Å}$), $\\text{Na}^+$ ($r = 1.02\\text{ Å}$), $\\text{K}^+$ ($r = 1.38\\text{ Å}$), $\\text{Cs}^+$ ($r = 1.67\\text{ Å}$)
- Crown Ethers: 12-crown-4 ($r_{\\text{cav}} = 0.65\\text{ Å}$), 15-crown-5 ($r_{\\text{cav}} = 0.95\\text{ Å}$), 18-crown-6 ($r_{\\text{cav}} = 1.35\\text{ Å}$)
(a) Compute the radius ratio $\\rho = r_{\\text{ion}} / r_{\\text{cav}}$ for all twelve cation-macrocycle pairings.
(b) Define the criteria for "ideal planar nesting" ($0.95 \\le \\rho \\le 1.08$), "rattling/cavity distortion" ($\\rho < 0.90$), and "perched/sandwich complexation" ($\\rho > 1.15$). Classify all 12 combinations.
(c) The complexation of $\\text{Cs}^+$ with 18-crown-6 forms both $1:1$ and $1:2$ ($[\\text{Cs}(\\text{18C6})_2]^+$) complexes with stepwise constants $K_1 = 1.20 \\times 10^3\\text{ M}^{-1}$ and $K_2 = 3.50 \\times 10^2\\text{ M}^{-1}$ in methanol. Calculate the percentage of total cesium present as the $1:2$ sandwich complex when $[\\text{18C6}]_0 = 50.0\\text{ mM}$ and $[\\text{Cs}^+]_0 = 1.00\\text{ mM}$.""",
            "solution": """### Step 1: Calculation of Radius Ratios $\\rho = r_{\\text{ion}} / r_{\\text{cav}}$

| Cation ($r_{\\text{ion}}$) | 12-Crown-4 ($r_{\\text{cav}} = 0.65\\text{ Å}$) | 15-Crown-5 ($r_{\\text{cav}} = 0.95\\text{ Å}$) | 18-Crown-6 ($r_{\\text{cav}} = 1.35\\text{ Å}$) |
| :--- | :--- | :--- | :--- |
| **$\\text{Li}^+$ ($0.76\\text{ Å}$)** | $\\rho = 0.76/0.65 = 1.17$ | $\\rho = 0.76/0.95 = 0.80$ | $\\rho = 0.76/1.35 = 0.56$ |
| **$\\text{Na}^+$ ($1.02\\text{ Å}$)** | $\\rho = 1.02/0.65 = 1.57$ | $\\rho = 1.02/0.95 = 1.07$ | $\\rho = 1.02/1.35 = 0.76$ |
| **$\\text{K}^+$ ($1.38\\text{ Å}$)** | $\\rho = 1.38/0.65 = 2.12$ | $\\rho = 1.38/0.95 = 1.45$ | $\\rho = 1.38/1.35 = 1.02$ |
| **$\\text{Cs}^+$ ($1.67\\text{ Å}$)** | $\\rho = 1.67/0.65 = 2.57$ | $\\rho = 1.67/0.95 = 1.76$ | $\\rho = 1.67/1.35 = 1.24$ |

### Step 2: Classification of Binding Regimes
1. **Ideal Planar Nesting ($0.95 \\le \\rho \\le 1.08$)**:
   - $\\text{Na}^+$ in 15-crown-5 ($\\rho = 1.07$)
   - $\\text{K}^+$ in 18-crown-6 ($\\rho = 1.02$)
   In these complexes, the cation sits precisely in the plane of the polyether oxygens.
2. **Rattling / Macrocyclic Distortion ($\\rho < 0.90$)**:
   - $\\text{Li}^+$ in 15-crown-5 ($\\rho = 0.80$)
   - $\\text{Li}^+$ in 18-crown-6 ($\\rho = 0.56$)
   - $\\text{Na}^+$ in 18-crown-6 ($\\rho = 0.76$)
   The ring must buckle into an elliptical, non-planar conformation to coordinate the smaller cation.
3. **Perched / Sandwich Complexation ($\\rho > 1.15$)**:
   - $\\text{Li}^+$ in 12-crown-4 ($\\rho = 1.17$, slightly perched / $1:2$ sandwich)
   - $\\text{Na}^+$, $\\text{K}^+$, $\\text{Cs}^+$ in 12-crown-4 ($\\rho = 1.57 - 2.57$, completely perched)
   - $\\text{K}^+$, $\\text{Cs}^+$ in 15-crown-5 ($\\rho = 1.45 - 1.76$, forms stable $1:2$ sandwiches)
   - $\\text{Cs}^+$ in 18-crown-6 ($\\rho = 1.24$, sits $1.0\\text{ Å}$ above the plane, coordinates second crown).

### Step 3: Cesium Sandwich Complex Speciation
Given:
- $[\\text{Cs}^+]_0 = 1.00\\text{ mM}$
- $[\\text{18C6}]_0 = 50.0\\text{ mM} \\gg [\\text{Cs}^+]_0 \\implies [\\text{18C6}]_{\\text{free}} \\approx 50.0\\text{ mM} = 0.050\\text{ M}$
- $K_1 = 1200\\text{ M}^{-1}$, $K_2 = 350\\text{ M}^{-1}$

The equilibrium relations are:
\\[
[\\text{Cs}\\cdot\\text{18C6}] = K_1 [\\text{Cs}^+] [\\text{18C6}] = (1200)(0.050) [\\text{Cs}^+] = 60.0 [\\text{Cs}^+]
\\]
\\[
[\\text{Cs}\\cdot(\\text{18C6})_2] = K_2 [\\text{Cs}\\cdot\\text{18C6}] [\\text{18C6}] = (350)(0.050) [\\text{Cs}\\cdot\\text{18C6}] = 17.5 [\\text{Cs}\\cdot\\text{18C6}]
\\]
Substituting $[\\text{Cs}\\cdot\\text{18C6}]$:
\\[
[\\text{Cs}\\cdot(\\text{18C6})_2] = 17.5 \\times (60.0 [\\text{Cs}^+]) = 1050 [\\text{Cs}^+]
\\]
Total cesium mass balance:
\\[
[\\text{Cs}]_{\\text{total}} = [\\text{Cs}^+] + [\\text{Cs}\\cdot\\text{18C6}] + [\\text{Cs}\\cdot(\\text{18C6})_2] = [\\text{Cs}^+] (1 + 60.0 + 1050) = 1111 [\\text{Cs}^+]
\\]
Percentage of cesium present as $1:2$ sandwich complex:
\\[
\\% [\\text{Cs}\\cdot(\\text{18C6})_2] = \\frac{1050 [\\text{Cs}^+]}{1111 [\\text{Cs}^+]} \\times 100\\% = \\frac{1050}{1111} \\times 100\\% = 94.5\\%
\\]
Percentage as $1:1$ complex:
\\[
\\% [\\text{Cs}\\cdot\\text{18C6}] = \\frac{60.0}{1111} \\times 100\\% = 5.4\\%
\\]
Percentage uncomplexed free $\\text{Cs}^+$:
\\[
\\% [\\text{Cs}^+] = \\frac{1}{1111} \\times 100\\% = 0.09\\%
\\]
At $50\\text{ mM}$ crown ether concentration, $94.5\\%$ of all cesium exists as the $1:2$ sandwich."""
        },
        {
            "probNumber": "2.2",
            "title": "Crown Ether Template Effect: Yield Enhancement Derivation in Williamson Polyetherification",
            "difficulty": "Foundational",
            "statement": """In the Williamson macrocyclization synthesis of 18-crown-6 from tetraethylene glycol and bis(2-chloroethyl) ether:
\\[
\\text{HO(CH}_2\\text{CH}_2\\text{O)}_4\\text{H} + \\text{Cl(CH}_2\\text{CH}_2\\text{O)}_2\\text{Cl} + 2\\,\\text{MOH} \\longrightarrow \\text{18-crown-6} + 2\\,\\text{MCl} + 2\\,\\text{H}_2\\text{O}
\\]
The reaction involves an initial mono-substitution forming an acyclic open intermediate $\\text{I}$, followed by competitive pathways:
1. Intramolecular cyclization to 18-crown-6: rate $r_{\\text{cyc}} = k_{\\text{intra}} [\\text{I}]$
2. Intermolecular polymerization to linear polymer: rate $r_{\\text{poly}} = k_{\\text{inter}} [\\text{I}] [\\text{Precursor}]$
When $\\text{KOH}$ is used as the base, $\\text{K}^+$ coordinates to intermediate $\\text{I}$ with binding constant $K_{\\text{temp}} = 450\\text{ M}^{-1}$, preorganizing it and increasing the effective local concentration so that $k_{\\text{intra}}(\\text{K}^+) = 85 \\times k_{\\text{intra}}(\\text{free})$.
When $\\text{NMe}_4\\text{OH}$ is used, no template binding occurs ($K_{\\text{temp}} = 0$).
(a) Derive the expression for the instantaneous cyclization selectivity (fraction of intermediate forming macrocycle) $\\phi = \\frac{r_{\\text{cyc}}}{r_{\\text{cyc}} + r_{\\text{poly}}}$.
(b) For $[\\text{Precursor}] = 0.10\\text{ M}$ and $k_{\\text{intra}}(\\text{free}) / k_{\\text{inter}} = 0.020\\text{ M}$, calculate the selectivity $\\phi$ in the absence of template ($\text{NMe}_4^+$).
(c) Assuming $90\\%$ of intermediate $\\text{I}$ is template-coordinated in the presence of $\\text{K}^+$, calculate the templated selectivity $\\phi_{\\text{temp}}$ and the yield enhancement factor.""",
            "solution": """### Step 1: Formulation of Cyclization Selectivity
The instantaneous fraction of intermediate $\\text{I}$ that converts to cyclic product rather than linear polymer is:
\\[
\\phi = \\frac{r_{\\text{cyc}}}{r_{\\text{cyc}} + r_{\\text{poly}}} = \\frac{k_{\\text{intra}} [\\text{I}]}{k_{\\text{intra}} [\\text{I}] + k_{\\text{inter}} [\\text{I}] [\\text{Precursor}]}
\\]
Dividing numerator and denominator by $k_{\\text{inter}} [\\text{I}]$:
\\[
\\phi = \\frac{\\frac{k_{\\text{intra}}}{k_{\\text{inter}}}}{\\frac{k_{\\text{intra}}}{k_{\\text{inter}}} + [\\text{Precursor}]}
\\]
The parameter $C_{\\text{eff}} = \\frac{k_{\\text{intra}}}{k_{\\text{inter}}}$ has dimensions of concentration ($\text{M}$) and represents the **effective concentration** of the reacting end-groups for intramolecular ring closure.

### Step 2: Non-Templated Selectivity ($\text{NMe}_4^+$ Base)
In the absence of a templating cation:
\\[
C_{\\text{eff, free}} = \\frac{k_{\\text{intra}}(\\text{free})}{k_{\\text{inter}}} = 0.020\\text{ M}
\\]
Given precursor concentration $[\\text{Precursor}] = 0.10\\text{ M}$:
\\[
\\phi_{\\text{non-temp}} = \\frac{0.020\\text{ M}}{0.020\\text{ M} + 0.10\\text{ M}} = \\frac{0.020}{0.120} = \\frac{1}{6} \\approx 0.1667 \\quad (16.7\\%)
\\]
Without a template, only $16.7\\%$ of the intermediate forms crown ether; $83.3\\%$ polycondenses into useless linear oligomers and polymers.

### Step 3: Templated Selectivity ($\text{K}^+$ Base)
With $\\text{K}^+$ present:
- Fraction of intermediate in templated state: $f_{\\text{temp}} = 0.90$
- Fraction in free state: $f_{\\text{free}} = 0.10$
The templated intramolecular rate constant is $k_{\\text{intra}}(\\text{temp}) = 85 \\times k_{\\text{intra}}(\\text{free})$.
The apparent effective rate constant is:
\\[
k_{\\text{intra, app}} = f_{\\text{free}} k_{\\text{intra}}(\\text{free}) + f_{\\text{temp}} k_{\\text{intra}}(\\text{temp}) = [0.10 + 0.90(85)] k_{\\text{intra}}(\\text{free}) = [0.10 + 76.5] k_{\\text{intra}}(\\text{free}) = 76.6\\, k_{\\text{intra}}(\\text{free})
\\]
The effective concentration under templated conditions becomes:
\\[
C_{\\text{eff, temp}} = 76.6 \\times C_{\\text{eff, free}} = 76.6 \\times 0.020\\text{ M} = 1.532\\text{ M}
\\]
The templated selectivity is:
\\[
\\phi_{\\text{temp}} = \\frac{1.532\\text{ M}}{1.532\\text{ M} + 0.10\\text{ M}} = \\frac{1.532}{1.632} = 0.9387 \\quad (93.9\\%)
\\]
Yield enhancement factor:
\\[
\\text{Enhancement} = \\frac{\\phi_{\\text{temp}}}{\\phi_{\\text{non-temp}}} = \\frac{0.9387}{0.1667} = 5.63
\\]
The $\\text{K}^+$ template boosts the cyclization selectivity from $16.7\\%$ to $93.9\\%$, enabling high-yield macrocyclization without needing ultra-dilute conditions."""
        },
        {
            "probNumber": "2.3",
            "title": "High-Dilution Kinetics: Intramolecular Ring Closure vs Intermolecular Oligomerization Rates",
            "difficulty": "Foundational",
            "statement": """A bifunctional precursor $\\text{X-R-Y}$ undergoes competition between first-order intramolecular cyclization to macrocycle $\\text{C}$ ($k_1 = 2.40 \\times 10^{-2}\\text{ s}^{-1}$) and second-order intermolecular dimerization to linear dimer $\\text{D}$ ($k_2 = 1.50\\text{ M}^{-1}\\text{s}^{-1}$):
\\[
\\text{X-R-Y} \\xrightarrow{k_1} \\text{C}, \\quad 2\\,\\text{X-R-Y} \\xrightarrow{k_2} \\text{X-R-R-Y}
\\]
(a) Define and compute the effective concentration $C_{\\text{eff}} = k_1 / k_2$ in $\\text{mM}$.
(b) If the reaction is run in batch at initial concentration $[\\text{A}]_0 = 100.0\\text{ mM}$, calculate the initial fraction of precursor undergoing cyclization $\\phi_0$.
(c) To achieve an initial cyclization selectivity of $\\phi_0 \\ge 95.0\\%$, what maximum concentration $[\\text{A}]_{\\max}$ must be maintained in the reaction vessel using a continuous-feed syringe pump?""",
            "solution": """### Step 1: Calculation of Effective Concentration
The effective concentration is:
\\[
C_{\\text{eff}} = \\frac{k_1}{k_2} = \\frac{2.40 \\times 10^{-2}\\text{ s}^{-1}}{1.50\\text{ M}^{-1}\\text{s}^{-1}} = 0.0160\\text{ M} = 16.0\\text{ mM}
\\]
Physical meaning: When the precursor concentration equals $C_{\\text{eff}} = 16.0\\text{ mM}$, intramolecular cyclization and intermolecular dimerization proceed at identical initial rates.

### Step 2: Selectivity at $[\\text{A}]_0 = 100.0\\text{ mM}$
The initial rates are:
\\[
r_1 = k_1 [\\text{A}]_0 = (2.40 \\times 10^{-2}\\text{ s}^{-1})(0.100\\text{ M}) = 2.40 \\times 10^{-3}\\text{ M/s}
\\]
\\[
r_2 = 2 k_2 [\\text{A}]_0^2 = 2 (1.50\\text{ M}^{-1}\\text{s}^{-1})(0.100\\text{ M})^2 = 3.00 \\times 10^{-2}\\text{ M/s}
\\]
(accounting for 2 molecules of precursor consumed per dimer formation event).
The fraction of precursor consumed by the unimolecular cyclization pathway is:
\\[
\\phi_0 = \\frac{r_1}{r_1 + r_2} = \\frac{k_1 [\\text{A}]_0}{k_1 [\\text{A}]_0 + 2 k_2 [\\text{A}]_0^2} = \\frac{k_1}{k_1 + 2 k_2 [\\text{A}]_0} = \\frac{C_{\\text{eff}}}{C_{\\text{eff}} + 2 [\\text{A}]_0}
\\]
Substitute values:
\\[
\\phi_0 = \\frac{16.0\\text{ mM}}{16.0\\text{ mM} + 2(100.0\\text{ mM})} = \\frac{16.0}{216.0} = 0.0741 \\quad (7.41\\%)
\\]
At $100\\text{ mM}$, over $92.5\\%$ of precursor is lost to dimerization and polymerization.

### Step 3: Determining Maximum Concentration for $\\phi_0 \\ge 95.0\\%$
We require:
\\[
\\frac{C_{\\text{eff}}}{C_{\\text{eff}} + 2 [\\text{A}]_{\\max}} \\ge 0.950
\\]
Inverting both sides:
\\[
\\frac{C_{\\text{eff}} + 2 [\\text{A}]_{\\max}}{C_{\\text{eff}}} \\le \\frac{1}{0.950} = 1.05263
\\]
\\[
1 + \\frac{2 [\\text{A}]_{\\max}}{C_{\\text{eff}}} \\le 1.05263 \\implies \\frac{2 [\\text{A}]_{\\max}}{C_{\\text{eff}}} \\le 0.05263
\\]
Solving for $[\\text{A}]_{\\max}$:
\\[
[\\text{A}]_{\\max} \\le \\frac{0.05263 \\times C_{\\text{eff}}}{2} = \\frac{0.05263 \\times 16.0\\text{ mM}}{2} = 0.421\\text{ mM} = 4.21 \\times 10^{-4}\\text{ M}
\\]
To achieve $\\ge 95\\%$ cyclization selectivity, a high-dilution syringe pump must maintain the steady-state unreacted precursor concentration below $0.42\\text{ mM}$ in the reactor."""
        },
        {
            "probNumber": "2.4",
            "title": "Thermodynamic Analysis of the Macrobicyclic Cryptate Effect: Comparing [2.2.2] with 18-Crown-6",
            "difficulty": "Intermediate",
            "statement": """The complexation thermodynamics of potassium cation ($\\text{K}^+$) with 18-crown-6 (monocycle) and [2.2.2] cryptand (bicycle) were measured in water at $298.15\\text{ K}$ by potentiometric and calorimetric titration:
- **18-Crown-6 (Monocycle)**: $\\log K_a = 2.06$, $\\Delta H^\\circ = -26.0\\text{ kJ/mol}$
- **[2.2.2] Cryptand (Bicycle)**: $\\log K_a = 5.40$, $\\Delta H^\\circ = -48.0\\text{ kJ/mol}$
(a) Compute $\\Delta G^\\circ$ and the entropic terms $\\Delta S^\\circ$ and $-T\\Delta S^\\circ$ for both complexes at $298.15\\text{ K}$.
(b) Evaluate the macrobicyclic cryptate enhancement parameters $\\Delta \\Delta G^\\circ$, $\\Delta \\Delta H^\\circ$, and $-T\\Delta \\Delta S^\\circ$.
(c) In $95\\%$ methanol-water, the stability constants are $\\log K_a = 6.10$ for 18-crown-6 and $\\log K_a = 10.50$ for [2.2.2] cryptand. Explain why both constants increase drastically in methanol, and why the cryptand remains $10^{4.4}$ times more stable in both solvent media.""",
            "solution": """### Step 1: Thermodynamic State Functions in Water ($298.15\\text{ K}$)
With $RT = (8.3145\\text{ J/(mol}\\cdot\\text{K)})(298.15\\text{ K}) = 2.4790\\text{ kJ/mol}$:
\\[
\\Delta G^\\circ = -2.3026 RT \\log K_a = -(5.7081\\text{ kJ/mol}) \\log K_a
\\]

1. **For 18-Crown-6**:
\\[
\\Delta G_{\\text{18C6}}^\circ = -(5.7081)(2.06) = -11.76\\text{ kJ/mol}
\\]
\\[
-T\\Delta S_{\\text{18C6}}^\circ = \\Delta G_{\\text{18C6}}^\circ - \\Delta H_{\\text{18C6}}^\circ = -11.76 - (-26.00) = +14.24\\text{ kJ/mol}
\\]
\\[
\\Delta S_{\\text{18C6}}^\circ = -\\frac{14240\\text{ J/mol}}{298.15\\text{ K}} = -47.76\\text{ J/(mol}\\cdot\\text{K)}
\\]

2. **For [2.2.2] Cryptand**:
\\[
\\Delta G_{\\text{crypt}}^\circ = -(5.7081)(5.40) = -30.82\\text{ kJ/mol}
\\]
\\[
-T\\Delta S_{\\text{crypt}}^\circ = \\Delta G_{\\text{crypt}}^\circ - \\Delta H_{\\text{crypt}}^\circ = -30.82 - (-48.00) = +17.18\\text{ kJ/mol}
\\]
\\[
\\Delta S_{\\text{crypt}}^\circ = -\\frac{17180\\text{ J/mol}}{298.15\\text{ K}} = -57.62\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 2: Macrobicyclic Cryptate Enhancements
\\[
\\Delta \\Delta G^\\circ = \\Delta G_{\\text{crypt}}^\circ - \\Delta G_{\\text{18C6}}^\circ = -30.82 - (-11.76) = -19.06\\text{ kJ/mol}
\\]
Ratio of association constants in water:
\\[
\\frac{K_a(\\text{crypt})}{K_a(\\text{18C6})} = 10^{5.40 - 2.06} = 10^{3.34} = 2190
\\]
Enthalpic and entropic breakdowns:
\\[
\\Delta \\Delta H^\\circ = \\Delta H_{\\text{crypt}}^\circ - \\Delta H_{\\text{18C6}}^\circ = -48.00 - (-26.00) = -22.00\\text{ kJ/mol}
\\]
\\[
-T\\Delta \\Delta S^\\circ = -T\\Delta S_{\\text{crypt}}^\circ - (-T\\Delta S_{\\text{18C6}}^\circ) = +17.18 - (+14.24) = +2.94\\text{ kJ/mol}
\\]
**Conclusion**: The cryptate effect in water is **overwhelmingly enthalpy-driven** ($\\Delta \\Delta H^\\circ = -22.00\\text{ kJ/mol}$). The bicyclic [2.2.2] framework provides eight convergent donor atoms (6 oxygens + 2 nitrogens) providing 3D spherical coordination that wraps $\\text{K}^+$ from all spatial octants, whereas 18-crown-6 only provides planar equatorial coordination (6 oxygens), leaving top and bottom faces weakly solvated.

### Step 3: Solvent Effect in $95\\%$ Methanol
1. **Magnitude Increase**: In water ($\\epsilon_r = 78.4$), $\\text{K}^+$ is strongly hydrated ($\\Delta G_{\\text{hyd}} \\approx -337\\text{ kJ/mol}$). In $95\\%$ methanol ($\\epsilon_r \\approx 33$), the solvation free energy of $\\text{K}^+$ is significantly less negative ($\approx -290\\text{ kJ/mol}$). Consequently, the desolvation penalty paid by the cation upon entering the cavity is reduced by over $40\\text{ kJ/mol}$, elevating $K_a$ by 4 orders of magnitude for both hosts:
   - 18C6: $\\log K_a = 2.06 \\to 6.10$ ($\Delta \\log K_a = +4.04$)
   - [2.2.2]: $\\log K_a = 5.40 \\to 10.50$ ($\Delta \\log K_a = +5.10$)
2. **Persistence of Cryptate Effect**: The selectivity factor between cryptand and crown remains virtually identical:
\\[
\\frac{K_a(\\text{crypt})}{K_a(\\text{18C6})} = 10^{10.50 - 6.10} = 10^{4.40} = 25,\\!100
\\]
The intrinsic structural advantage of 3D spherical encapsulation over 2D planar wrapping is an intrinsic topological property that operates independently of dielectric media."""
        },
        {
            "probNumber": "2.5",
            "title": "Enthalpy-Entropy Compensation in Crown Ether Complexation: Solvent Reorganization",
            "difficulty": "Intermediate",
            "statement": """A thermodynamic study of alkali cation complexation by 18-crown-6 across eight different non-aqueous solvents yielded the following linear enthalpy-entropy compensation (EEC) relationship at $298.15\\text{ K}$:
\\[
T\\Delta S^\\circ = 0.820 \\,\\Delta H^\\circ + 12.50\\text{ kJ/mol}
\\]
(a) Substitute this compensation equation into the Gibbs-Helmholtz relation $\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ$ to derive an expression for $\\Delta G^\\circ$ solely as a function of $\\Delta H^\\circ$.
(b) If a synthetic modification of the crown ether (e.g., adding electron-donating side arms) improves the binding enthalpy by $\\Delta(\\Delta H^\\circ) = -20.0\\text{ kJ/mol}$, what is the actual net improvement in binding free energy $\\Delta(\\Delta G^\\circ)$?
(c) Calculate the percentage of the enthalpic enhancement that is canceled out by entropic compensation. Explain the molecular mechanism of this solvent-mediated cancellation.""",
            "solution": """### Step 1: Derivation of $\\Delta G^\\circ$ as a Function of $\\Delta H^\\circ$
The fundamental definition of Gibbs free energy is:
\\[
\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ
\\]
Substitute the empirical compensation equation $T\\Delta S^\\circ = 0.820\\, \\Delta H^\\circ + 12.50\\text{ kJ/mol}$:
\\[
\\Delta G^\\circ = \\Delta H^\\circ - (0.820\\, \\Delta H^\\circ + 12.50)
\\]
\\[
\\Delta G^\\circ = (1 - 0.820) \\Delta H^\\circ - 12.50 = 0.180\\, \\Delta H^\\circ - 12.50\\text{ kJ/mol}
\\]

### Step 2: Evaluation of Net Improvement in Binding Free Energy
Differentiating $\\Delta G^\\circ$ with respect to $\\Delta H^\\circ$:
\\[
\\Delta(\\Delta G^\\circ) = 0.180 \\times \\Delta(\\Delta H^\\circ)
\\]
Given an enthalpic improvement $\\Delta(\\Delta H^\\circ) = -20.0\\text{ kJ/mol}$:
\\[
\\Delta(\\Delta G^\\circ) = 0.180 \\times (-20.0\\text{ kJ/mol}) = -3.60\\text{ kJ/mol}
\\]
Even though the bond enthalpy improved by $-20.0\\text{ kJ/mol}$, the net Gibbs free energy improves by only $-3.60\\text{ kJ/mol}$.

### Step 3: Compensation Percentage and Molecular Mechanism
1. **Percentage Canceled**:
\\[
\\% \\text{ Canceled} = \\frac{-20.0 - (-3.60)}{-20.0} \\times 100\\% = \\frac{-16.40}{-20.0} \\times 100\\% = 82.0\\%
\\]
Exactly $82.0\\%$ of the enthalpic gain is completely neutralized by an unfavorable entropic loss ($\\Delta(-T\\Delta S^\\circ) = +16.40\\text{ kJ/mol}$).

2. **Molecular Mechanism**:
- **Solvent Reorganization**: A tighter, more exothermic ion-dipole interaction polarizes the donor atoms more strongly and contracts the coordination sphere. This forces the surrounding solvent molecules in the second coordination shell to pack more tightly and freeze their rotational/translational modes, reducing solvent entropy.
- **Conformational Freezing**: Stronger host-guest bonding restricts low-frequency vibrational and torsional motions of the macrocyclic ring segments (freezing of breathing modes), incurring an internal vibrational/conformational entropy penalty.
- This thermodynamic feedback loop demonstrates why designing ultra-high affinity receptors requires preorganization (minimizing internal host entropy loss) rather than relying solely on stronger electrostatic charges."""
        },
        {
            "probNumber": "2.6",
            "title": "Spherand Preorganization Free Energy: Quantifying the Penalty of Lone-Pair Repulsion Relief",
            "difficulty": "Intermediate",
            "statement": """Donald J. Cram measured the binding of sodium cation ($\\text{Na}^+$) by three hosts possessing six coordinating oxygen atoms in $\\text{CDCl}_3$ saturated with $\\text{D}_2\\text{O}$ at $298.15\\text{ K}$:
1. **Pentaglyme (Acyclic Podand)**: $\\log K_a = 2.0$, $\\Delta G^\\circ = -11.4\\text{ kJ/mol}$
2. **18-Crown-6 (Monocycle)**: $\\log K_a = 6.7$, $\\Delta G^\\circ = -38.2\\text{ kJ/mol}$
3. **Hexaspherand (Rigid Spherand)**: $\\log K_a = 14.1$, $\\Delta G^\\circ = -80.5\\text{ kJ/mol}$
(a) Compute the macrocyclic enhancement $\\Delta \\Delta G_{\\text{macro}}^\\circ = \\Delta G_{\\text{crown}}^\circ - \\Delta G_{\\text{podand}}^\circ$ and the spherand preorganization enhancement $\\Delta \\Delta G_{\\text{spherand}}^\circ = \\Delta G_{\\text{spherand}}^\circ - \\Delta G_{\\text{crown}}^\circ$.
(b) How many orders of magnitude is $\\text{Na}^+$ bound more tightly by the spherand compared to 18-crown-6?
(c) The uncomplexed hexaspherand is destabilized by internal repulsion among its six inward-directed oxygen lone pairs, estimated at $E_{\\text{rep}} \\approx +75\\text{ kJ/mol}$. Explain how this ground-state destabilization paradoxically acts as an immense thermodynamic driving force for cation binding.""",
            "solution": """### Step 1: Calculation of Enhancement Free Energies
1. **Macrocyclic Enhancement**:
\\[
\\Delta \\Delta G_{\\text{macro}}^\circ = \\Delta G_{\\text{crown}}^\circ - \\Delta G_{\\text{podand}}^\circ = -38.2 - (-11.4) = -26.8\\text{ kJ/mol}
\\]
2. **Spherand Preorganization Enhancement**:
\\[
\\Delta \\Delta G_{\\text{spherand}}^\circ = \\Delta G_{\\text{spherand}}^\circ - \\Delta G_{\\text{crown}}^\circ = -80.5 - (-38.2) = -42.3\\text{ kJ/mol}
\\]
Total preorganization advantage over open-chain podand:
\\[
\\Delta \\Delta G_{\\text{total}}^\circ = -80.5 - (-11.4) = -69.1\\text{ kJ/mol}
\\]

### Step 2: Orders of Magnitude Comparison
The ratio of binding constants between spherand and 18-crown-6 is:
\\[
\\frac{K_a(\\text{spherand})}{K_a(\\text{18C6})} = 10^{14.1 - 6.7} = 10^{7.4} = 2.51 \\times 10^7
\\]
The spherand binds sodium cation **$25$ million times more tightly** than 18-crown-6!
Compared to the acyclic podand:
\\[
\\frac{K_a(\\text{spherand})}{K_a(\\text{podand})} = 10^{14.1 - 2.0} = 10^{12.1} = 1.26 \\times 10^{12}
\\]
Over **one trillion times** more tightly!

### Step 3: The Paradox of Ground-State Destabilization
Why does a destabilized uncomplexed host bind a guest with record-breaking affinity?
1. **Ground-State Elevation**: In the free spherand, the rigid sexiphenylene framework holds the six methoxy oxygens forced together in an octahedral cluster, compressing their non-bonding electron lone pairs against each other. This creates severe electrostatic repulsion ($E_{\\text{rep}} \\approx +75\\text{ kJ/mol}$), raising the enthalpy of the uncomplexed host to a high energy level $H_{\\text{free}}$.
2. **Relief of Repulsion**: When a positive $\\text{Na}^+$ ion enters the cavity, its concentrated positive charge immediately neutralizes the repulsive negative lone pairs, turning mutual oxygen-oxygen repulsion into powerful oxygen-sodium electrostatic attraction.
3. **No Conformational Penalty**: Because the spherand's rigid skeleton is already fixed in the exact octahedral geometry of the complex, zero work is expended on conformational reorganization ($\Delta S_{\\text{conf}} \\approx 0$, $\\Delta H_{\\text{strain}} \\approx 0$).
Thus, releasing the stored ground-state electrostatic strain provides an enormous additional driving force ($-\\Delta H_{\\text{relief}} < 0$) that propels the association constant to astronomical levels."""
        },
        {
            "probNumber": "2.7",
            "title": "Phase Transfer Catalytic Kinetics: Crown-Assisted Permanganate Oxidation in Benzene",
            "difficulty": "Advanced",
            "statement": """A two-phase liquid-liquid oxidation of trans-stilbene ($[\\text{Sub}] = 0.20\\text{ M}$) in benzene is catalyzed by dicyclohexano-18-crown-6 (DC18C6) in contact with an aqueous potassium permanganate layer ($[\\text{KMnO}_4]_{\\text{aq}} = 1.0\\text{ M}$).
The phase transfer extraction equilibrium is:
\\[
\\text{K}^+(\\text{aq}) + \\text{MnO}_4^-(\\text{aq}) + \\text{Crown}(\\text{org}) \\xrightleftharpoons[K_{\\text{ex}}]{} [\\text{K} \\subset \\text{Crown}]^+\\text{MnO}_4^-(\\text{org})
\\]
with extraction constant $K_{\\text{ex}} = 8.50 \\times 10^2\\text{ M}^{-2}$.
In the organic phase, the naked permanganate reacts with trans-stilbene via a second-order rate law:
\\[
r = k_{\\text{org}} [\\text{Sub}] [[\\text{K} \\subset \\text{Crown}]^+\\text{MnO}_4^-]
\\]
where $k_{\\text{org}} = 4.20 \\times 10^1\\text{ M}^{-1}\\text{s}^{-1}$.
(a) If the total crown ether concentration in benzene is $[\\text{Crown}]_0 = 10.0\\text{ mM}$, calculate the steady-state concentration of active $[\\text{K} \\subset \\text{Crown}]^+\\text{MnO}_4^-$ in the benzene phase.
(b) Calculate the initial oxidation reaction rate $r$ in $\\text{M/s}$ and in $\\text{mol}\\cdot\\text{L}^{-1}\\text{min}^{-1}$.
(c) In the absence of crown ether, the solubility of $\\text{KMnO}_4$ in benzene is $C_{\\text{blank}} = 1.20 \\times 10^{-6}\\text{ M}$. Calculate the catalytic acceleration factor achieved by the crown ether.""",
            "solution": """### Step 1: Extraction Equilibrium in Benzene Phase
The extraction equilibrium constant is defined by:
\\[
K_{\\text{ex}} = \\frac{[[\\text{K} \\subset \\text{Crown}]^+\\text{MnO}_4^-]_{(\\text{org})}}{[\\text{K}^+]_{(\\text{aq})} [\\text{MnO}_4^-]_{(\\text{aq})} [\\text{Crown}]_{\\text{free}, (\\text{org})}}
\\]
Given:
- $[\\text{K}^+]_{(\\text{aq})} = 1.0\\text{ M}$, $[\\text{MnO}_4^-]_{(\\text{aq})} = 1.0\\text{ M}$
- $K_{\\text{ex}} = 850\\text{ M}^{-2}$
- $[\\text{Crown}]_0 = 10.0\\text{ mM} = 0.0100\\text{ M}$

Let $x = [[\\text{K} \\subset \\text{Crown}]^+\\text{MnO}_4^-]_{(\\text{org})}$.
Then $[\\text{Crown}]_{\\text{free}, (\\text{org})} = [\\text{Crown}]_0 - x = 0.0100 - x$.
Substituting into the equilibrium expression:
\\[
850 = \\frac{x}{(1.0)(1.0)(0.0100 - x)}
\\]
Rearranging:
\\[
850 (0.0100 - x) = x \\implies 8.50 - 850 x = x \\implies 851 x = 8.50
\\]
Solving for $x$:
\\[
x = \\frac{8.50}{851} = 9.988 \\times 10^{-3}\\text{ M} = 9.99\\text{ mM}
\\]
Notice that $x / [\\text{Crown}]_0 = 9.99 / 10.0 = 99.88\\%$. Almost the entire crown ether inventory in the benzene phase is loaded with active potassium permanganate ion pairs!

### Step 2: Reaction Rate Calculation
The organic phase reaction rate is:
\\[
r = k_{\\text{org}} [\\text{Sub}] [[\\text{K} \\subset \\text{Crown}]^+\\text{MnO}_4^-]
\\]
Given $[\\text{Sub}] = 0.20\\text{ M}$ and $k_{\\text{org}} = 42.0\\text{ M}^{-1}\\text{s}^{-1}$:
\\[
r = (42.0\\text{ M}^{-1}\\text{s}^{-1})(0.20\\text{ M})(9.988 \\times 10^{-3}\\text{ M}) = 8.39 \\times 10^{-2}\\text{ M/s}
\\]
In units of $\\text{mol}\\cdot\\text{L}^{-1}\\text{min}^{-1}$:
\\[
r_{\\text{min}} = (8.39 \\times 10^{-2}\\text{ M/s}) \\times 60\\text{ s/min} = 5.034\\text{ mol}\\cdot\\text{L}^{-1}\\text{min}^{-1}
\\]

### Step 3: Catalytic Acceleration Factor
In the uncatalyzed blank system, the active permanganate concentration in benzene is strictly limited by its solubility:
\\[
[\\text{MnO}_4^-]_{\\text{blank}} = 1.20 \\times 10^{-6}\\text{ M}
\\]
The uncatalyzed rate is:
\\[
r_{\\text{blank}} = (42.0)(0.20)(1.20 \\times 10^{-6}) = 1.008 \\times 10^{-5}\\text{ M/s}
\\]
The acceleration factor is:
\\[
\\text{Acceleration} = \\frac{r}{r_{\\text{blank}}} = \\frac{[[\\text{K} \\subset \\text{Crown}]^+\\text{MnO}_4^-]}{[\\text{MnO}_4^-]_{\\text{blank}}} = \\frac{9.988 \\times 10^{-3}\\text{ M}}{1.20 \\times 10^{-6}\\text{ M}} = 8323
\\]
The crown ether accelerates the phase transfer oxidation by a factor of over **$8,300$**, converting an unreactive two-phase slurry into an instantaneous homogeneous oxidation."""
        },
        {
            "probNumber": "2.8",
            "title": "Schiff Base Template Macrocyclization: Derivation of Equilibrium Matrix",
            "difficulty": "Advanced",
            "statement": """The templated condensation of 2,6-diacetylpyridine with diethylenetriamine in methanol in the presence of alkaline earth metal perchlorate $\\text{M}(\\text{ClO}_4)_2$ forms a 15-membered pentaaza macrocyclic complex $[\\text{M}\\cdot\\text{L}]^{2+}$.
In the absence of metal template, the equilibrium constant for macrocyclic imine closure is $K_{\\text{free}} = 1.20 \\times 10^{-2}$.
In the presence of metal ion $\\text{M}^{2+}$, the open precursor intermediate $\\text{Int}$ coordinates the metal with stability constant $K_{\\text{int}} = 3.50 \\times 10^3\\text{ M}^{-1}$, and the final cyclic macrocycle coordinates $\\text{M}^{2+}$ with stability constant $K_{\\text{complex}} = 4.80 \\times 10^7\\text{ M}^{-1}$.
(a) Construct the thermodynamic square cycle relating the four species: $\\text{Int}$, $\\text{L}$, $[\\text{M}\\cdot\\text{Int}]^{2+}$, and $[\\text{M}\\cdot\\text{L}]^{2+}$.
(b) Derive the relationship connecting the templated cyclization constant $K_{\\text{temp}} = [[\\text{M}\\cdot\\text{L}]^{2+}] / [[\\text{M}\\cdot\\text{Int}]^{2+}]$ to $K_{\\text{free}}, K_{\\text{int}}$, and $K_{\\text{complex}}$.
(c) Calculate $K_{\\text{temp}}$ and evaluate the thermodynamic template shifting factor $\\Lambda = K_{\\text{temp}} / K_{\\text{free}}$.""",
            "solution": """### Step 1: Thermodynamic Square Cycle
Consider the four species participating in the macrocyclization equilibrium:
\\[
\\begin{matrix}
\\text{Int} & \\xrightarrow{\\quad K_{\\text{free}} \\quad} & \\text{L} \\\\
\\quad \\Big\\downarrow K_{\\text{int}} & & \\quad \\Big\\downarrow K_{\\text{complex}} \\\\
[\\text{M}\\cdot\\text{Int}]^{2+} & \\xrightarrow{\\quad K_{\\text{temp}} \\quad} & [\\text{M}\\cdot\\text{L}]^{2+}
\\end{matrix}
\\]
The equilibria are:
1. Top horizontal: $\\text{Int} \\xrightleftharpoons[K_{\\text{free}}]{} \\text{L}$
2. Bottom horizontal: $[\\text{M}\\cdot\\text{Int}]^{2+} \\xrightleftharpoons[K_{\\text{temp}}]{} [\\text{M}\\cdot\\text{L}]^{2+}$
3. Left vertical: $\\text{Int} + \\text{M}^{2+} \\xrightleftharpoons[K_{\\text{int}}]{} [\\text{M}\\cdot\\text{Int}]^{2+}$
4. Right vertical: $\\text{L} + \\text{M}^{2+} \\xrightleftharpoons[K_{\\text{complex}}]{} [\\text{M}\\cdot\\text{L}]^{2+}$

### Step 2: Derivation of the Templated Equilibrium Constant
Because free energy is a state function, traveling from $\\text{Int} + \\text{M}^{2+}$ to $[\\text{M}\\cdot\\text{L}]^{2+}$ along the top-right path must equal the free energy along the left-bottom path:
\\[
\\Delta G_{\\text{top-right}}^\circ = \\Delta G_{\\text{free}}^\circ + \\Delta G_{\\text{complex}}^\circ
\\]
\\[
\\Delta G_{\\text{left-bottom}}^\circ = \\Delta G_{\\text{int}}^\circ + \\Delta G_{\\text{temp}}^\circ
\\]
Equating both paths:
\\[
\\Delta G_{\\text{free}}^\circ + \\Delta G_{\\text{complex}}^\circ = \\Delta G_{\\text{int}}^\circ + \\Delta G_{\\text{temp}}^\circ
\\]
In terms of equilibrium constants ($\\Delta G^\circ = -RT\\ln K$):
\\[
-RT \\ln(K_{\\text{free}} K_{\\text{complex}}) = -RT \\ln(K_{\\text{int}} K_{\\text{temp}})
\\]
Exponentiating both sides:
\\[
K_{\\text{free}} \\cdot K_{\\text{complex}} = K_{\\text{int}} \\cdot K_{\\text{temp}}
\\]
Solving for the templated cyclization constant $K_{\\text{temp}}$:
\\[
K_{\\text{temp}} = K_{\\text{free}} \\cdot \\frac{K_{\\text{complex}}}{K_{\\text{int}}}
\\]

### Step 3: Calculation of $K_{\\text{temp}}$ and Shifting Factor $\\Lambda$
Given values:
- $K_{\\text{free}} = 1.20 \\times 10^{-2}$
- $K_{\\text{int}} = 3.50 \\times 10^3\\text{ M}^{-1}$
- $K_{\\text{complex}} = 4.80 \\times 10^7\\text{ M}^{-1}$

Substitute into the formula:
\\[
K_{\\text{temp}} = (1.20 \\times 10^{-2}) \\times \\frac{4.80 \\times 10^7}{3.50 \\times 10^3} = (1.20 \\times 10^{-2}) \\times (1.3714 \\times 10^4) = 164.6
\\]
The thermodynamic template shifting factor $\\Lambda$ is:
\\[
\\Lambda = \\frac{K_{\\text{temp}}}{K_{\\text{free}}} = \\frac{K_{\\text{complex}}}{K_{\\text{int}}} = \\frac{4.80 \\times 10^7}{3.50 \\times 10^3} = 13,\\!714
\\]
In the absence of template, $K_{\\text{free}} = 0.012$, meaning only $\\approx 1.2\\%$ of intermediate exists as macrocycle at equilibrium. In the presence of $\\text{M}^{2+}$, $K_{\\text{temp}} = 164.6$, meaning over $99.4\\%$ of the intermediate is cyclized to $[\\text{M}\\cdot\\text{L}]^{2+}$. The metal template shifts the thermodynamic equilibrium toward the macrocycle by a factor of over **$13,700$**."""
        },
        {
            "probNumber": "2.9",
            "title": "Lariat Ether Dynamic Arm Coordination: Kinetic Relaxation and Two-Step Insertion Rate Laws",
            "difficulty": "Advanced",
            "statement": """A lariat ether consisting of a diaza-18-crown-6 core bearing a pendant 2-methoxyethyl coordinating arm ($-\\text{CH}_2\\text{CH}_2\\text{OCH}_3$) binds sodium cation ($\\text{Na}^+$) through a sequential two-step mechanism:
\\[
\\text{Host} + \\text{Na}^+ \\xrightleftharpoons[k_{-1}]{k_1} [\\text{Host}\\cdot\\text{Na}^+]_{\\text{monocyclic}} \\xrightleftharpoons[k_{-2}]{k_2} [\\text{Host}\\cdot\\text{Na}^+]_{\\text{lariat-capped}}
\\]
where step 1 represents fast equatorial insertion into the crown ring, and step 2 represents conformational arm-capping over the axial face.
Kinetic constants at $298\\text{ K}$ are:
- $k_1 = 4.50 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}, \\quad k_{-1} = 1.50 \\times 10^4\\text{ s}^{-1}$
- $k_2 = 8.00 \\times 10^4\\text{ s}^{-1}, \\quad k_{-2} = 2.00 \\times 10^3\\text{ s}^{-1}$
(a) Calculate the equilibrium constants $K_1 = k_1 / k_{-1}$ and $K_2 = k_2 / k_{-2}$, and evaluate the overall association constant $K_{\\text{overall}} = [\\text{Total Bound}] / ([\\text{Host}] [\\text{Na}^+])$.
(b) Applying the steady-state approximation to the intermediate monocyclic complex, derive the apparent second-order forward rate constant $k_{\\text{on, app}}$ and first-order reverse rate constant $k_{\\text{off, app}}$.
(c) In a temperature-jump (T-jump) relaxation experiment with $[\\text{Na}^+]_0 \\gg [\\text{Host}]_0$, write the characteristic relaxation times $\\tau_1$ and $\\tau_2$ assuming fast step 1 pre-equilibration, and compute $\\tau_2$ at $[\\text{Na}^+] = 10.0\\text{ mM}$.""",
            "solution": """### Step 1: Equilibrium Constants and Overall Affinity
1. **First Step Constant**:
\\[
K_1 = \\frac{k_1}{k_{-1}} = \\frac{4.50 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}}{1.50 \\times 10^4\\text{ s}^{-1}} = 3000\\text{ M}^{-1}
\\]
2. **Second Step Constant (Intramolecular Capping)**:
\\[
K_2 = \\frac{k_2}{k_{-2}} = \\frac{8.00 \\times 10^4\\text{ s}^{-1}}{2.00 \\times 10^3\\text{ s}^{-1}} = 40.0 \\quad (\\text{dimensionless})
\\]
3. **Overall Association Constant**:
The total bound host concentration is:
\\[
[\\text{Bound}] = [\\text{H}\\cdot\\text{Na}^+]_{\\text{mono}} + [\\text{H}\\cdot\\text{Na}^+]_{\\text{cap}} = K_1 [\\text{H}][\\text{Na}^+] + K_1 K_2 [\\text{H}][\\text{Na}^+] = K_1 (1 + K_2) [\\text{H}][\\text{Na}^+]
\\]
Therefore:
\\[
K_{\\text{overall}} = K_1 (1 + K_2) = (3000\\text{ M}^{-1})(1 + 40.0) = 3000 \\times 41.0 = 1.23 \\times 10^5\\text{ M}^{-1}
\\]
The pendant lariat arm amplifies the overall binding constant by a factor of $41$ ($K_2 + 1$).

### Step 2: Steady-State Apparent Rate Constants
Let intermediate be $\\text{C}_1 = [\\text{H}\\cdot\\text{Na}^+]_{\\text{mono}}$ and product be $\\text{C}_2 = [\\text{H}\\cdot\\text{Na}^+]_{\\text{cap}}$.
The rate of product formation is:
\\[
\\frac{d[\\text{C}_2]}{dt} = k_2 [\\text{C}_1] - k_{-2} [\\text{C}_2]
\\]
Applying the steady-state approximation to $\\text{C}_1$:
\\[
\\frac{d[\\text{C}_1]}{dt} = k_1 [\\text{H}][\\text{Na}^+] - (k_{-1} + k_2)[\\text{C}_1] + k_{-2}[\\text{C}_2] = 0
\\]
\\[
[\\text{C}_1] = \\frac{k_1 [\\text{H}][\\text{Na}^+] + k_{-2}[\\text{C}_2]}{k_{-1} + k_2}
\\]
Substituting into the rate equation:
\\[
\\frac{d[\\text{C}_2]}{dt} = \\frac{k_1 k_2}{k_{-1} + k_2} [\\text{H}][\\text{Na}^+] - \\left( k_{-2} - \\frac{k_2 k_{-2}}{k_{-1} + k_2} \\right) [\\text{C}_2] = \\frac{k_1 k_2}{k_{-1} + k_2} [\\text{H}][\\text{Na}^+] - \\frac{k_{-1} k_{-2}}{k_{-1} + k_2} [\\text{C}_2]
\\]
Thus:
\\[
k_{\\text{on, app}} = \\frac{k_1 k_2}{k_{-1} + k_2} = \\frac{(4.50 \\times 10^7)(8.00 \\times 10^4)}{1.50 \\times 10^4 + 8.00 \\times 10^4} = \\frac{3.60 \\times 10^{12}}{9.50 \\times 10^4} = 3.789 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}
\\]
\\[
k_{\\text{off, app}} = \\frac{k_{-1} k_{-2}}{k_{-1} + k_2} = \\frac{(1.50 \\times 10^4)(2.00 \\times 10^3)}{9.50 \\times 10^4} = \\frac{3.00 \\times 10^7}{9.50 \\times 10^4} = 315.8\\text{ s}^{-1}
\\]
Checking detailed balance:
\\[
\\frac{k_{\\text{on, app}}}{k_{\\text{off, app}}} = \\frac{3.789 \\times 10^7}{315.8} = 1.20 \\times 10^5\\text{ M}^{-1} \\approx K_1 K_2
\\]

### Step 3: Relaxation Time $\\tau_2$ in T-Jump Experiment
Because step 1 is much faster than step 2 ($k_1 [\\text{Na}^+] + k_{-1} \\gg k_2 + k_{-2}$), step 1 acts as a rapidly pre-equilibrated fast relaxation mode $\\tau_1$:
\\[
\\frac{1}{\\tau_1} \\approx k_1 [\\text{Na}^+] + k_{-1}
\\]
For the slower second relaxation mode (lariat arm capping):
\\[
\\frac{1}{\\tau_2} = k_{-2} + k_2 \\frac{K_1 [\\text{Na}^+]}{1 + K_1 [\\text{Na}^+]}
\\]
Given $[\\text{Na}^+] = 10.0\\text{ mM} = 0.010\\text{ M}$ and $K_1 = 3000\\text{ M}^{-1}$:
\\[
K_1 [\\text{Na}^+] = (3000\\text{ M}^{-1})(0.010\\text{ M}) = 30.0
\\]
\\[
\\frac{K_1 [\\text{Na}^+]}{1 + K_1 [\\text{Na}^+]} = \\frac{30.0}{1 + 30.0} = \\frac{30.0}{31.0} = 0.9677
\\]
Calculating $1/\\tau_2$:
\\[
\\frac{1}{\\tau_2} = 2000\\text{ s}^{-1} + (80,\\!000\\text{ s}^{-1})(0.9677) = 2000 + 77,\\!419 = 79,\\!419\\text{ s}^{-1}
\\]
The slow relaxation time is:
\\[
\\tau_2 = \\frac{1}{79,\\!419\\text{ s}^{-1}} = 1.259 \\times 10^{-5}\\text{ s} = 12.6\\text{ }\\mu\\text{s}
\\]
The lariat arm caps the macrocycle within $12.6$ microseconds, demonstrating that lariat ethers combine high thermodynamic affinity with microsecond dynamic responsiveness."""
        }
    ]

    return {
        "id": "unit-2",
        "number": 2,
        "title": "Cation-Binding Macrocycles: Crown Ethers, Cryptands & Spherands",
        "leadSummary": "Pedersen crown ether discovery and nomenclature, kinetic and thermodynamic template effects, podands and lariat ethers, polypyridyl bipyridine/terpyridine coordination, Lehn's macrobicyclic cryptands, Cram's rigid spherands, cavitands, carcerands, cation selectivity hole-size matching rules, enthalpy-entropy compensation (EEC), phase transfer catalysis (PTC), and biological ionophore mimicry.",
        "simulations": ["sim_supra_crown_ether_selectivity"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u2 = get_unit_2()
    print(f"Unit 2 generated: {len(u2['sections'])} sections, {len(u2['problems'])} problems.")
