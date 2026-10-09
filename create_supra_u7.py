"""
create_supra_u7.py
Creates Unit 7 data dictionary for Supramolecular Chemistry:
Supramolecular Self-Assembly, Helicates & Coordination Cages
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_7():
    sections = [
        {
            "secNumber": "7.1",
            "title": "Principles of Supramolecular Self-Assembly vs Self-Organization",
            "content": """**Self-assembly** is the autonomous, spontaneous association of two or more pre-existing molecular components into organized, well-defined architectures governed strictly by non-covalent interactions and reversible dynamic bonds without external human guidance.

### Self-Assembly vs Self-Organization
In supramolecular science, Whitesides and Lehn established a fundamental distinction between static self-assembly and dynamic self-organization:
1. **Static Self-Assembly**:
   - The system evolves toward a global thermodynamic free energy minimum ($\\Delta G = 0$ at equilibrium).
   - Once the assembled structure forms, no continuous input of energy or fuel is required to maintain its structural integrity.
   - Examples include the formation of coordination cages, molecular crystals, liquid crystal mesophases, and virus capsids (e.g., tobacco mosaic virus).
2. **Dynamic Self-Organization (Dissipative Systems)**:
   - The organized state exists only far from thermodynamic equilibrium in an open system.
   - Continuous dissipation of external energy (e.g., chemical fuel such as ATP, light flux, or electrical potential) is strictly required to sustain the ordered structure.
   - Ceasing fuel consumption causes the structure to relax spontaneously into an unassembled equilibrium ground state.
   - Examples include biological microtubules, actin filaments, metabolic oscillations, and synthetic fuel-driven dissipative gels.

### Thermodynamic Driving Forces: Enthalpy vs Entropy
The spontaneous formation of a discrete supramolecular assembly from $N$ individual building blocks is dictated by:
\\[
\\Delta G_{\\text{assembly}}^\circ = \\Delta H_{\\text{assembly}}^\circ - T\\Delta S_{\\text{assembly}}^\circ < 0
\\]
- **Entropic Penalty**: Bringing $N$ independent molecules together into a single rigid aggregate results in a severe loss of translational and rotational entropy:
\\[
\\Delta S_{\\text{trans+rot}}^\circ \\approx -(N - 1) \\times (100 - 150\\text{ J/(mol}\\cdot\\text{K)}) \\ll 0
\\]
- **Enthalpic Driving Force**: Spontaneity requires that the sum of new non-covalent bonds (metal-ligand coordination, hydrogen bonding, $\\pi-\\pi$ stacking) release sufficient enthalpy to overcome this entropic barrier:
\\[
|\\Delta H_{\\text{assembly}}^\circ| > |T\\Delta S_{\\text{assembly}}^\circ|
\\]
- **Solvation Entropy Compensation**: Desolvation of coordinated metal ions and organic ligands expels dozens of structured solvent molecules into the bulk phase, providing a massive positive solvent entropy gain ($\\Delta S_{\\text{solv}}^\circ > 0$) that partially offsets translational loss."""
        },
        {
            "secNumber": "7.2",
            "title": "Metallo-Helicates: Lehn's Helicates, Stereochemical Induction & Self-Sorting",
            "content": """A **helicate** is a discrete supramolecular coordination complex composed of one or more polydentate linear organic strands wrapped helically around a central linear axis of two or more transition metal ions. The term was coined by Jean-Marie Lehn in 1987 (derived from the Greek *helix*).

### Lehn's Double and Triple Helicates
1. **Double-Stranded Helicates**:
   Formed when two oligobipyridine or oligophenanthroline strands wrap around tetrahedral metal ions (such as $\\text{Cu}^I$ or $\\text{Ag}^I$):
   \\[
   2\\,\\text{strand} + n\\,\\text{Cu}^I \\longrightarrow [\\text{Cu}_n(\\text{strand})_2]^{n+}
   \\]
   - Each $\\text{Cu}^I$ center coordinates two bidentate bipyridine units in a perpendicular tetrahedral geometry ($\angle \\approx 90^\\circ$).
   - To satisfy the coordination requirements of successive metal ions along the chain, the two flexible strands are forced to twist around each other, generating a double-helical architecture isomorphic to double-stranded DNA.
2. **Triple-Stranded Helicates**:
   Formed when three bis- or tris-bidentate strands coordinate to octahedral metal ions (such as $\\text{Fe}^{II}, \\text{Co}^{II}, \\text{Ni}^{II}, \\text{Ga}^{III}$):
   \\[
   3\\,\\text{strand} + n\\,\\text{M}^{n+} \\longrightarrow [\\text{M}_n(\\text{strand})_3]^{m+}
   \\]
   Three strands wind helically around the metal centers, providing six coordination sites per octahedral metal ion.

### Helical Chirality: Right-Handed (P) vs Left-Handed (M)
Helicates are inherently chiral due to their screw axis:
- **Right-handed helix**: Designated **$P$** (plus) or $\\Delta$ configuration at the metal vertices.
- **Left-handed helix**: Designated **$M$** (minus) or $\\Lambda$ configuration.
When prepared from achiral strands, helicates crystallize as a racemic mixture of $P$ and $M$ enantiomers.
- **Stereochemical Induction**: Attaching chiral stereocenters (e.g., chiral $\\alpha$-phenylethylamine) to the strand termini breaks the thermodynamic degeneracy, inducing diastereoselective self-assembly into a single helical hand ($>99\\%\\text{ de}$).

### Self-Sorting Phenomena
When mixtures of different strands and metal ions are combined in a single solution:
- **Narcissistic Self-Sorting**: Strands assemble exclusively with identical partners to form homoleptic complexes ($[\\text{M}A_n]$ and $[\\text{M}B_n]$) with zero cross-contamination ($[\\text{M}A_x B_y] = 0$).
- **Social Self-Sorting**: Strands specifically recognize and assemble only with distinct, complementary partners to form strictly heteroleptic complexes."""
        },
        {
            "secNumber": "7.3",
            "title": "The Directional Bonding Approach: Fujita Coordination Cages & Squares",
            "content": """The **directional bonding approach** is a rational design strategy for constructing discrete, two- and three-dimensional polyhedral coordination cages by matching the fixed coordination angles of transition metal vertices with the rigid bite angles of multidentate organic bridging ligands.

### Makoto Fujita's Molecular Squares: $[M_4 L_4]^{8+}$
In 1990, Makoto Fujita demonstrated the prototypical self-assembly of a discrete molecular square:
- **Metal Vertex**: A cis-protected square-planar metal precursor, typically $[(\\text{en})\\text{Pd}(\\text{NO}_3)_2]$ or $[(\\text{en})\\text{Pt}(\\text{NO}_3)_2]$, where ethylenediamine (en) blocks two cis coordination sites, enforcing a rigid **$90^\\circ$ coordination angle**.
- **Bridging Ligand**: A rigid, linear ditopic bridging ligand, 4,4'-bipyridine (4,4'-bpy), with a **$180^\\circ$ bite angle**.
When mixed in an exact $1:1$ stoichiometric ratio in water at $T = 80^\\circ\\text{C}$:
\\[
4\\,[(\\text{en})\\text{Pd}]^{2+} + 4\\,(4,4'\\text{-bpy}) \\longrightarrow [(\\text{en})_4\\text{Pd}_4(4,4'\\text{-bpy})_4]^{8+}
\\]
- Thermodynamics cleanly favors the discrete cyclic tetramer over infinite coordination polymers due to **enthalpic ring closure**: all coordination sites are fully satisfied without dangling uncoordinated pyridines.
- The resulting molecular square has internal dimensions of $8.0\\text{ Å} \\times 8.0\\text{ Å}$, enclosing a hydrophilic cavity capable of binding neutral aromatic guests.

### Fujita's Octahedral Coordination Cage: $[M_6 L_4]^{12+}$
In 1995, Fujita extended the directional bonding concept to three dimensions by reacting six cis-protected palladium(II) vertices ($90^\\circ$ bite angle) with four rigid, planar tritopic ligands: 2,4,6-tris(4-pyridyl)-1,3,5-triazine (TPT):
\\[
6\\,[(\\text{en})\\text{Pd}]^{2+} + 4\\,\\text{TPT} \\longrightarrow [(\\text{en})_6\\text{Pd}_6(\\text{TPT})_4]^{12+}
\\]
- The structure forms a hollow, truncated octahedron where the 6 Pd(II) ions occupy the vertices and the 4 planar triazine ligands occupy four alternating faces of the octahedron.
- The cage encloses a large hydrophobic cavity ($V_{\\text{cav}} \\approx 300 - 400\\text{ Å}^3$) accessible via four open triangular windows."""
        },
        {
            "secNumber": "7.4",
            "title": "Stang Molecular Polygons & Polyhedra: Symmetry Rules & Vertex Angles",
            "content": """Peter J. Stang systematized the mathematical and geometric foundations of the directional bonding approach into a general predictive framework based on Euclidean geometry and point group symmetry.

### Geometric Matching Rules for 2D Polygons
A regular polygon with $n$ vertices has an interior vertex angle:
\\[
\\theta = \\frac{(n - 2) \\times 180^\\circ}{n} = 180^\\circ - \\frac{360^\\circ}{n}
\\]
To synthesize a discrete regular polygon $M_n L_n$:
1. **Molecular Triangles ($n = 3$, $\\theta = 60^\\circ$)**:
   - Requires a $60^\\circ$ metal vertex combined with a linear $180^\\circ$ ligand, or a $90^\\circ$ vertex paired with an obtuse $120^\\circ$ ligand.
2. **Molecular Squares ($n = 4$, $\\theta = 90^\\circ$)**:
   - $90^\\circ$ cis-metal acceptor $+ 180^\\circ$ linear donor.
3. **Molecular Pentagons ($n = 5$, $\\theta = 108^\\circ$)**:
   - Metal units with $108^\\circ$ bite angles (e.g., ferrocene-derived diphosphines) paired with linear bridges.
4. **Molecular Hexagons ($n = 6$, $\\theta = 120^\\circ$)**:
   - $120^\\circ$ bent metal units (e.g., trans-coordinated angles or bite angles of bipyridyls) paired with linear dipyridyl linkers.

### 3D Polyhedra: Platonic and Archimedean Solids
For three-dimensional polyhedral cages ($M_m L_n$):
- **Molecular Tetrahedron ($T_d$)**: 4 vertices, 6 edges, 4 faces.
  Synthesized using 4 tritopic $C_3$-symmetric vertices combined with 6 linear ditopic edges, or 4 trivalent metal ions (e.g., $\\text{Ga}^{III}$ or $\\text{Fe}^{III}$) coordinated by 6 bis-catecholate or bis-bipyridine ligands ($M_4 L_6$).
- **Molecular Cubes and Octahedra ($O_h$)**:
  8 vertices and 12 edges for a cube ($M_8 L_{12}$); 6 vertices and 8 faces for an octahedron ($M_6 L_4$ or $M_6 L_8$).
- **Molecular Dodecahedron ($I_h$)**:
  Stang and co-workers assembled a cuboctahedron ($M_{12} L_{24}$) from 12 cis-capped palladium vertices and 24 bent dipyridyl ligands, as well as an enormous dodecahedron containing 20 metal centers and 30 bridging ligands ($M_{20} L_{30}$) with diameters exceeding $5\\text{ nm}$."""
        },
        {
            "secNumber": "7.5",
            "title": "Host-Guest Chemistry in Cages: Catalysis & Ship-in-a-Bottle Reactions",
            "content": """The hollow interior cavities of supramolecular coordination cages serve as **molecular flasks** or nanoreactors, isolating reactive guests and dramatically altering chemical reactivity and selectivity.

### The Hydrophobic Cavity Effect in Water
In Fujita's $[(\\text{en})_6\\text{Pd}_6(\\text{TPT})_4]^{12+}$ cage, the twelve positive charges reside on the external periphery, surrounded by a shell of hydrated nitrate counterions.
- The interior cavity is lined with the aromatic triazine and pyridine rings, presenting a purely hydrophobic microenvironment.
- In aqueous solution, apolar organic molecules are driven into the cavity by hydrophobic exclusion.
- Large polycyclic aromatic hydrocarbons such as four molecules of pyrene, two molecules of perylene, or fullerenes ($\text{C}_{60}$) encapsulate quantitatively inside a single cage.

### Cavity-Promoted Catalysis and Stereoselectivity
1. **Accelerated Diels-Alder Cycloaddition**:
   Fujita demonstrated that anthracenes and maleimides undergo rapid $[4+2]$ Diels-Alder cycloaddition inside $[(\\text{en})_6\\text{Pd}_6(\\text{TPT})_4]^{12+}$:
   - In bulk solution, anthracene reacts exclusively across the 9,10-positions (central ring) to yield the thermodynamic bridgehead adduct.
   - Inside the cage, spatial confinement forces anthracene and maleimide into an unusual stacked orientation that restricts reaction to the 1,4-positions (terminal ring), yielding an **otherwise inaccessible 1,4-Diels-Alder adduct** in $>95\\%$ regioselectivity.
2. **Raymond's $[\\text{Ga}_4 L_6]^{12-}$ Tetrahedral Cages**:
   Kenneth Raymond developed water-soluble anionic tetrahedral cages assembled from 4 $\\text{Ga}^{III}$ centers and 6 bis-catecholate ligands:
   - Encloses a hydrophobic cavity with an intense negative electrostatic potential.
   - Encapsulates and stabilizes normally unstable reactive carbocations and phosphonium cations.
   - Catalyzes the unimolecular Aza-Cope rearrangement of allyl ammonium cations with rate accelerations exceeding $k_{\\text{cat}} / k_{\\text{uncat}} > 10^6$, exhibiting true enzyme-like Michaelis-Menten kinetics and product inhibition.

### Ship-in-a-Bottle Synthesis
Molecules too large to pass through the cage apertures can be synthesized inside the cavity from small precursors that enter freely:
- Once coupled covalently inside the cage, the bulky product is permanently trapped—a supramolecular **ship-in-a-bottle** complex."""
        },
        {
            "secNumber": "7.6",
            "title": "Dynamic Covalent Polymers & Quadruple Hydrogen-Bonded Arrays (UPy)",
            "content": """**Supramolecular polymers** are macromolecular arrays composed of monomeric repeating units held together by reversible, highly directional non-covalent interactions rather than covalent bonds.

### Quadruple Hydrogen-Bonding Arrays: The UPy System
In 1997, E. W. "Bert" Meijer introduced the **2-ureido-4[1H]-pyrimidinone (UPy)** motif, which revolutionized supramolecular materials:
- UPy self-assembles into a planar homodimer held by an array of **four cooperative hydrogen bonds**.
- The dimerization sequence is **DDAA** (Donor-Donor-Acceptor-Acceptor):
  - Two $\\text{N-H}$ hydrogen-bond donors.
  - Two carbonyl/pyrimidine hydrogen-bond acceptors.
- **Secondary Electrostatic Interactions (Jorgensen Effect)**:
  In a DDAA $\\cdot$ AADD array, secondary cross-interactions between adjacent dipoles are predominantly attractive ($++$ and $--$ diagonal repulsions are minimized, while $+-$ attractions are maximized):
  \\[
  K_{\\text{dim}}(\\text{UPy}) > 6.0 \\times 10^7\\text{ M}^{-1} \\quad \\text{in chloroform at } 298\\text{ K}
  \\]
- This dimer binding constant is five orders of magnitude higher than that of a DAD-ADA array (e.g., diaminopyridine-uracil, $K_{\\text{dim}} \\approx 10^2\\text{ M}^{-1}$).

### Supramolecular Polymer Properties
When bifunctional monomers are synthesized with UPy units at both ends ($\text{UPy-Spacer-UPy}$):
- In dilute solution, the monomers remain as small oligomers.
- Above a critical concentration, the reversible association links thousands of monomers into high-molecular-weight linear chains ($M_n > 10^6\\text{ g/mol}$).
- **Stimuli-Responsive Dynamics**:
  At room temperature, the material behaves like a tough elastomer or ductile plastic. Heating disrupts the hydrogen bonds, causing dramatic viscosity drops of several orders of magnitude into a low-viscosity liquid that flows effortlessly for molding.
- **Self-Healing**: If cleaved or scratched, reconnecting the surfaces allows the dynamic hydrogen bonds to re-form across the interface, fully restoring mechanical tensile strength within minutes."""
        },
        {
            "secNumber": "7.7",
            "title": "Supramolecular Polymerization: Isodesmic vs Cooperative Mechanisms",
            "content": """Supramolecular polymerizations proceed via two fundamentally distinct thermodynamic growth pathways: the **isodesmic** (equal-affinity) model and the **cooperative** (nucleation-elongation) model.

### The Isodesmic Model (Equal-K Model)
In an isodesmic polymerization, every addition of a monomer $M$ to a growing chain $M_n$ has an identical thermodynamic association constant:
\\[
M_n + M \\xrightleftharpoons{K} M_{n+1} \\quad \\text{for all } n \\ge 1
\\]
- The standard free energy of addition $\\Delta G^\circ = -RT \\ln K$ is independent of chain length.
- The weight-average and number-average degree of polymerization grow smoothly and continuously with total monomer concentration $C_{\\text{tot}}$:
\\[
\\langle DP_n \\rangle = \\frac{1}{\\sqrt{1 - 4 K C_{\\text{tot}}}} \\quad \\text{or} \\quad \\langle DP_n \\rangle \\approx \\sqrt{K C_{\\text{tot}}} \\quad (\\text{for } K C_{\\text{tot}} \\gg 1)
\\]
- The aggregate size distribution follows an exponential Flory-Schulz distribution; no critical concentration exists.

### The Cooperative Model (Nucleation-Elongation)
In cooperative supramolecular polymerization, association occurs in two distinct thermodynamic phases:
1. **Nucleation Phase**:
   Formation of an initial small nucleus (oligomer of size $s$) is thermodynamically unfavorable:
   \\[
   M + M \\xrightleftharpoons{K_n} M_2, \\quad \\dots, \\quad M_{s-1} + M \\xrightleftharpoons{K_n} M_s
   \\]
   with nucleation constant $K_n$.
2. **Elongation Phase**:
   Once the critical nucleus $M_s$ is formed, subsequent addition of monomer proceeds with a much higher association constant $K_e$:
   \\[
   M_n + M \\xrightleftharpoons{K_e} M_{n+1} \\quad (n \\ge s), \\quad K_e \\gg K_n
   \\]
- The **cooperativity factor** is defined as $\\sigma = K_n / K_e \\ll 1$ (typically $10^{-3}$ to $10^{-6}$).

### Critical Concentration and Thermal Signatures
Cooperative polymerization displays sharp threshold behavior:
- **Critical Polymerization Concentration ($C_p$)**:
  Below $C_p = 1 / K_e$, virtually only unassociated monomers exist. Above $C_p$, added monomer converts almost exclusively into long supramolecular polymers.
- **Elongation Temperature ($T_e$)**:
  In cooling experiments, cooperative systems remain monomeric until cooling to a critical elongation temperature $T_e$, where a sharp, sigmoidal transition abruptly triggers macroscopic polymerization, resembling a first-order phase transition."""
        },
        {
            "secNumber": "7.8",
            "title": "Minimal Self-Replicating Systems & Template-Directed Autocatalysis",
            "content": """The origin of life requires molecular self-replication—the ability of a chemical species to catalyze its own formation from simpler building blocks. Supramolecular chemistry has created synthetic minimal self-replicating systems that operate on pure non-covalent template effects.

### Rebek's Minimal Synthetic Self-Replicating System
In 1990, Julius Rebek Jr. reported the first fully synthetic self-replicator using an amino-adenosine derivative and an active ester:
- **Reagent A**: An aminoadenosine derivative bearing an adenine recognition base.
- **Reagent B**: A pentafluorophenyl ester derivative bearing an imide cleft complementary to adenine.
- **Template T**: The covalent coupling product formed by condensation of A and B:
\\[
A + B \\longrightarrow T + \\text{PFP-OH}
\\]
- **Autocatalytic Template Cycle**:
  The product $T$ contains both the adenine base and the imide cleft on the same molecule:
  1. Template $T$ binds Reagent A and Reagent B simultaneously through complementary $[\\text{N-H}\\cdots\\text{N}]$ and $[\\text{N-H}\\cdots\\text{O}]$ hydrogen bonds, forming a ternary ternary complex $[A \\cdot B \\cdot T]$.
  2. Inside this complex, the amine of $A$ and the activated ester of $B$ are positioned in close reactive proximity, accelerating amide bond formation.
  3. The reaction yields a homodimer of templates $[T \\cdot T]$.
  4. Dissociation of the dimer releases two active template molecules ($2\\,T$), each ready to catalyze another cycle.

### The Parabolic Law: Product Inhibition in Self-Replication
In ideal biological replication (such as PCR under linear phases), replication is exponential ($d[T]/dt \\propto [T]$). However, in synthetic supramolecular replicators, the duplex $[T \\cdot T]$ is held by the same strong non-covalent forces that stabilize the reactive ternary complex:
\\[
T + T \\xrightleftharpoons{K_{\\text{dim}}} T_2
\\]
If the dimerization constant $K_{\\text{dim}}$ is large, the majority of product is trapped as inactive dimer $T_2$:
\\[
[T]_{\\text{free}} \\approx \\sqrt{\\frac{[T]_{\\text{total}}}{2 K_{\\text{dim}}}}
\\]
Consequently, the rate of autocatalytic product formation follows the **square-root (parabolic) rate law**:
\\[
\\frac{d[T]}{dt} = k_{\\text{uncat}} [A][B] + k_{\\text{cat}} [A][B] [T]^{1/2}
\\]
The product concentration grows quadratically with time ($[T] \\propto t^2$) rather than exponentially, a universal constraint known as **product inhibition in artificial self-replication**."""
        }
    ]

    problems = [
        {
            "probNumber": "7.1",
            "title": "Self-Assembly Thermodynamics: Enthalpy-Entropy Trade-Off in a Closed Polyhedron",
            "difficulty": "Foundational",
            "statement": """A discrete octahedral coordination cage, $[M_6 L_4]^{12+}$, self-assembles in aqueous solution from 6 divalent metal cations ($M^{2+}$) and 4 neutral tritopic planar ligands ($L$):
\\[
6\\,M^{2+} + 4\\,L \\xrightleftharpoons{\\beta_{6,4}} [M_6 L_4]^{12+}
\\]
At $T = 298.15\\text{ K}$:
- The standard enthalpy of assembly is $\\Delta H_{\\text{assembly}}^\circ = -385.0\\text{ kJ/mol}$.
- The total standard entropy of assembly is $\\Delta S_{\\text{assembly}}^\circ = -640.0\\text{ J/(mol}\\cdot\\text{K)}$.
(a) Calculate the standard Gibbs free energy of assembly $\\Delta G_{\\text{assembly}}^\circ$ in $\\text{kJ/mol}$ and the cumulative association constant $\\beta_{6,4}$ at $298.15\\text{ K}$.
(b) The entropy change consists of two opposing terms: the translational entropic loss of bringing 10 particles into 1 particle ($\\Delta S_{\\text{trans}}^\circ = -1{,}150.0\\text{ J/(mol}\\cdot\\text{K)}$) and the desolvation entropy of water release ($\\Delta S_{\\text{solv}}^\circ$). Calculate $\\Delta S_{\\text{solv}}^\circ$ in $\\text{J/(mol}\\cdot\\text{K)}$.
(c) Calculate the temperature $T_{\\text{decomp}}$ above which the coordination cage spontaneously dissociates into free components ($\Delta G_{\\text{assembly}}^\circ > 0$), assuming $\\Delta H^\circ$ and $\\Delta S^\circ$ remain constant.""",
            "solution": """### Step 1: Gibbs Free Energy and Association Constant
From $\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ$:
- $\\Delta H_{\\text{assembly}}^\\circ = -385.0\\text{ kJ/mol} = -385{,}000\\text{ J/mol}$
- $T\\Delta S_{\\text{assembly}}^\\circ = 298.15\\text{ K} \\times (-640.0\\text{ J/(mol}\\cdot\\text{K)}) = -190{,}816\\text{ J/mol} = -190.82\\text{ kJ/mol}$
\\[
\\Delta G_{\\text{assembly}}^\\circ = -385.0 - (-190.816) = -194.184\\text{ kJ/mol} \\approx -194.18\\text{ kJ/mol}
\\]
The association constant $\\beta_{6,4}$ is:
\\[
\\beta_{6,4} = \\exp\\left( -\\frac{\\Delta G^\\circ}{RT} \\right) = \\exp\\left( \\frac{194{,}184}{8.31446 \\times 298.15} \\right) = \\exp\\left( \\frac{194{,}184}{2478.96} \\right) = e^{78.3329}
\\]
\\[
\\beta_{6,4} = 1.048 \\times 10^{34}\\text{ M}^{-9}
\\]
The colossal association constant drives virtually complete cage assembly in dilute solution.

### Step 2: Solvation Entropy Component
The total entropy change is the sum of translational loss and desolvation gain:
\\[
\\Delta S_{\\text{assembly}}^\\circ = \\Delta S_{\\text{trans}}^\\circ + \\Delta S_{\\text{solv}}^\\circ
\\]
\\[
-640.0 = -1{,}150.0 + \\Delta S_{\\text{solv}}^\\circ
\\]
\\[
\\Delta S_{\\text{solv}}^\\circ = -640.0 - (-1{,}150.0) = +510.0\\text{ J/(mol}\\cdot\\text{K)}
\\]
Desolvation of the hydrophobic ligands and metal ions releases dozens of tightly bound water molecules into the bulk phase, contributing $+510.0\\text{ J/(mol}\\cdot\\text{K)}$ of favorable entropy that offsets nearly half of the massive translational entropy deficit.

### Step 3: Thermal Decomposition Temperature ($T_{\\text{decomp}}$)
Dissociation occurs when $\\Delta G_{\\text{assembly}}^\\circ = 0$:
\\[
\\Delta H_{\\text{assembly}}^\\circ - T_{\\text{decomp}} \\Delta S_{\\text{assembly}}^\\circ = 0 \\implies T_{\\text{decomp}} = \\frac{\\Delta H_{\\text{assembly}}^\\circ}{\\Delta S_{\\text{assembly}}^\\circ}
\\]
Substitute values:
\\[
T_{\\text{decomp}} = \\frac{-385{,}000\\text{ J/mol}}{-640.0\\text{ J/(mol}\\cdot\\text{K)}} = 601.56\\text{ K} = 328.4^\\circ\\text{C}
\\]
Under normal solution conditions (below $100^\\circ\\text{C}$ in water), the cage is thermodynamically stable against thermal disassembly."""
        },
        {
            "probNumber": "7.2",
            "title": "Helicate Pitch, Twist Angle & Coordination Stereochemistry: Lambda vs Delta",
            "difficulty": "Foundational",
            "statement": """A dinuclear double-stranded helicate $[\\text{Cu}_2 L_2]^{2+}$ consists of two bis-bidentate ligands coordinated to two copper(I) centers separated by an intermetallic distance $d_{\\text{Cu}\\cdots\\text{Cu}} = 3.85\\text{ Å}$.
The coordination geometry around each $\\text{Cu}^I$ is tetrahedral with an orthogonal bite angle $\\theta = 90.0^\\circ$ between the two bipyridine units.
The helical twist per metal center is $\\Delta \\phi = 72.0^\\circ$.
(a) Calculate the helical pitch $P$ (the translational distance corresponding to a full $360^\\circ$ turn of the double helix) in angstroms ($\\text{Å}$).
(b) Determine whether a single pitch turn contains an integer or non-integer number of metal centers.
(c) The complex exists as an equimolar racemic mixture of two enantiomeric helicates: $(P)-[\\text{Cu}_2 L_2]^{2+}$ (right-handed) and $(M)-[\\text{Cu}_2 L_2]^{2+}$ (left-handed). If a chiral tartrate counterion ($R,R$-tartrate) is introduced, the circular dichroism (CD) spectrum shows an induced Cotton effect at $\\lambda = 320\\text{ nm}$ with molar circular dichroism $\\Delta \\epsilon = +24.5\\text{ M}^{-1}\\text{cm}^{-1}$.
Given that the pure $(P)$ enantiomer has $\\Delta \\epsilon_0 = +35.0\\text{ M}^{-1}\\text{cm}^{-1}$, calculate the diastereomeric excess ($\\text{de}$) and the percentage fraction of the $(P)$ helicate.""",
            "solution": """### Step 1: Helical Pitch Calculation
The twist angle between the two metal centers is $\\Delta \\phi = 72.0^\\circ$, and the axial distance between them is $d_{\\text{Cu}\\cdots\\text{Cu}} = 3.85\\text{ Å}$.
The axial translation per degree of helical twist is:
\\[
\\frac{\\Delta z}{\\Delta \\phi} = \\frac{3.85\\text{ Å}}{72.0^\\circ} = 0.053472\\text{ Å/degree}
\\]
The pitch $P$ corresponds to a full revolution of $\\phi = 360^\\circ$:
\\[
P = 360^\\circ \\times \\left( \\frac{\\Delta z}{\\Delta \\phi} \\right) = 360^\\circ \\times 0.053472\\text{ Å/degree} = 19.25\\text{ Å}
\\]
The helical pitch is $19.25\\text{ Å}$.

### Step 2: Number of Metal Centers per Turn
The number of metal steps per complete $360^\\circ$ pitch turn is:
\\[
N_{\\text{turn}} = \\frac{360^\\circ}{\\Delta \\phi} = \\frac{360^\\circ}{72.0^\\circ} = 5.00
\\]
Exactly 5 metal centers complete a full $360^\\circ$ helical period (a five-fold helical screw symmetry).

### Step 3: Diastereomeric Excess and Enantiomer Distribution
The observed molar circular dichroism $\\Delta \\epsilon$ is proportional to the diastereomeric excess:
\\[
\\text{de} = \\frac{\\Delta \\epsilon}{\\Delta \\epsilon_0} \\times 100\\% = \\frac{+24.5\\text{ M}^{-1}\\text{cm}^{-1}}{+35.0\\text{ M}^{-1}\\text{cm}^{-1}} \\times 100\\% = 70.0\\%
\\]
The diastereomeric excess is $70.0\\%$ in favor of the right-handed $(P)$ helicate.
Mole fractions:
\\[
\\text{de} = f_P - f_M = 0.700, \\quad f_P + f_M = 1.000
\\]
\\[
2 f_P = 1.700 \\implies f_P = 0.850 \\implies 85.0\\%
\\]
\\[
f_M = 1.000 - 0.850 = 0.150 \\implies 15.0\\%
\\]
Chiral tartrate induces stereoselective assembly, producing $85.0\\%$ of the right-handed $(P)$ helicate."""
        },
        {
            "probNumber": "7.3",
            "title": "Directional Bonding Angle Constraints: Molecular Squares vs Octahedra",
            "difficulty": "Foundational",
            "statement": """In the directional bonding approach, a metal vertex $M$ with an enforced coordination bite angle $\\alpha$ is reacted with a bridging ligand $L$ with a rigid divergence angle $\\beta$:
(a) For a planar polygon $M_n L_n$ to form without angle strain, the sum of internal angles must satisfy $(n - 2) \\times 180^\\circ$. Show that for alternating metal vertices (angle $\\alpha$) and ligand vertices (angle $\\beta$), the geometric closure condition is:
\\[
\\alpha + \\beta = \\frac{2(n - 2) \\times 180^\\circ}{n} = 360^\\circ - \\frac{720^\\circ}{n}
\\]
(b) Evaluate the required ligand angle $\\beta$ when a cis-protected square-planar metal vertex ($\\alpha = 90.0^\\circ$) is used to construct:
    (i) A molecular square ($n = 4$),
    (ii) A molecular triangle ($n = 3$),
    (iii) A molecular hexagon ($n = 6$).
(c) Explain why reacting $[(\\text{en})\\text{Pd}]^{2+}$ ($\\alpha = 90^\\circ$) with 4,4'-bipyridine ($\\beta = 180^\\circ$) produces exclusively the molecular square ($n = 4$) with zero detectable triangle ($n = 3$) or pentagon ($n = 5$).""",
            "solution": """### Step 1: Derivation of the Closure Condition
A polygon composed of $n$ metal centers and $n$ bridging ligands has $2n$ total vertices.
The sum of all interior angles of a $2n$-gon is:
\\[
\\Sigma = (2n - 2) \\times 180^\\circ
\\]
Because there are $n$ metal angles of size $\\alpha$ and $n$ ligand angles of size $\\beta$:
\\[
n \\alpha + n \\beta = (2n - 2) \\times 180^\\circ
\\]
Divide both sides by $n$:
\\[
\\alpha + \\beta = \\frac{2n - 2}{n} \\times 180^\\circ = \\left( 2 - \\frac{2}{n} \\right) 180^\\circ = 360^\\circ - \\frac{360^\\circ}{n/2} = 360^\\circ - \\frac{720^\\circ}{n}
\\]
This is the fundamental closure criterion for an $M_n L_n$ metallacycle.

### Step 2: Evaluation for $n = 4, 3, 6$ with $\alpha = 90^\circ$
1. **Molecular Square ($n = 4$)**:
\\[
\\alpha + \\beta = 360^\\circ - \\frac{720^\\circ}{4} = 360^\\circ - 180^\\circ = 180^\\circ
\\]
With $\\alpha = 90.0^\\circ$:
\\[
\\beta = 180.0^\\circ - 90.0^\\circ = 90.0^\\circ \\quad \\text{if defined as an internal vertex}
\\]
If the ligand is a straight edge with bite angle $\\beta_{\\text{ext}} = 180^\\circ$ (linear rod), each corner angle $\\alpha = 90^\\circ$ directly provides all the turning angle (total turning angle $= 4 \\times 90^\\circ = 360^\\circ$).

2. **Molecular Triangle ($n = 3$)**:
\\[
\\alpha + \\beta = 360^\\circ - \\frac{720^\\circ}{3} = 360^\\circ - 240^\\circ = 120^\\circ
\\]
With $\\alpha = 90.0^\\circ$:
\\[
\\beta = 120.0^\\circ - 90.0^\\circ = 30.0^\\circ
\\]
Requires a ligand with an acute $30^\\circ$ angle, or a linear ligand with $60^\\circ$ metal vertices.

3. **Molecular Hexagon ($n = 6$)**:
\\[
\\alpha + \\beta = 360^\\circ - \\frac{720^\\circ}{6} = 360^\\circ - 120^\\circ = 240^\\circ
\\]
With $\\alpha = 90.0^\\circ$:
\\[
\\beta = 240.0^\\circ - 90.0^\\circ = 150.0^\\circ
\\]
Requires an obtuse bent ligand with a $150^\\circ$ angle.

### Step 3: Exclusive Formation of the Molecular Square
When 4,4'-bipyridine is used as the ligand, its two coordinating pyridyl nitrogen lone pairs point in antiparallel directions along a collinear axis ($\beta = 180.0^\\circ$).
- To close a ring, the total turning angle must equal $360^\\circ$:
  \\[
  \\sum \\text{Turn} = n \\times (180^\\circ - \\alpha) = n \\times (180^\\circ - 90^\\circ) = n \\times 90^\\circ = 360^\\circ \\implies n = 4
  \\]
- For a triangle ($n = 3$), the three $90^\\circ$ corners provide only $3 \\times 90^\\circ = 270^\\circ$ of turn, leaving a $90^\\circ$ angular deficit that would impose severe bending strain on the rigid aromatic rings ($>150\\text{ kJ/mol}$).
- For a pentagon ($n = 5$), five corners provide $450^\\circ$, overshooting closure.
- The molecular square ($n = 4$) satisfies the angular requirement with exactly zero angle strain, making it the unique global thermodynamic product."""
        },
        {
            "probNumber": "7.4",
            "title": "Isodesmic vs Cooperative Supramolecular Polymerization: Degree of Polymerization",
            "difficulty": "Intermediate",
            "statement": """A bifunctional discotic monomer $M$ undergoes 1D supramolecular polymerization in methylcyclohexane at $T = 298.15\\text{ K}$ through $\\pi-\\pi$ stacking and hydrogen bonding.
Two distinct molecular designs are investigated:
- **System A (Isodesmic)**: Association is governed by an identical equilibrium constant $K = 4.50 \\times 10^4\\text{ M}^{-1}$ for all addition steps:
  $M_n + M \\xrightleftharpoons{K} M_{n+1}$.
- **System B (Cooperative)**: Association follows a nucleation-elongation model with nucleation constant $K_n = 4.50\\text{ M}^{-1}$ and elongation constant $K_e = 4.50 \\times 10^4\\text{ M}^{-1}$ (cooperativity factor $\\sigma = K_n / K_e = 1.00 \\times 10^{-4}$).
(a) For System A, derive the expression for the number-average degree of polymerization $\\langle DP_n \\rangle$ as a function of total concentration $C_{\\text{tot}}$ and calculate $\\langle DP_n \\rangle$ at $C_{\\text{tot}} = 1.00 \\times 10^{-3}\\text{ M}$ ($1.00\\text{ mM}$).
(b) For System B, calculate the critical polymerization concentration $C_p = 1 / K_e$ and the fraction of monomer assembled into polymers, $\\alpha_{\\text{poly}}$, at:
    (i) $C_{\\text{tot}} = 0.50\\, C_p$,
    (ii) $C_{\\text{tot}} = 5.00\\, C_p$.
(c) Calculate $\\langle DP_n \\rangle$ for System B at $C_{\\text{tot}} = 1.00 \\times 10^{-3}\\text{ M}$ using the Goldstein-Stryer relation $\\langle DP_n \\rangle \\approx 1 / \\sqrt{\\sigma}$ at the transition point.""",
            "solution": """### Step 1: System A (Isodesmic) Degree of Polymerization
In an isodesmic polymerization:
The total concentration of molecules (chains) is $C_{\\text{chains}} = \\sum_{n=1}^\\infty [M_n] = \\frac{[M]_1}{1 - K [M]_1}$.
The total concentration of monomer units is $C_{\\text{tot}} = \\sum_{n=1}^\\infty n [M_n] = \\frac{[M]_1}{(1 - K [M]_1)^2}$.
The number-average degree of polymerization is:
\\[
\\langle DP_n \\rangle = \\frac{C_{\\text{tot}}}{C_{\\text{chains}}} = \\frac{1}{1 - K [M]_1}
\\]
Solving for $[M]_1$ in terms of $C_{\\text{tot}}$:
\\[
C_{\\text{tot}} = \\frac{[M]_1}{(1 - K [M]_1)^2} \\implies K C_{\\text{tot}} = \\frac{K [M]_1}{(1 - K [M]_1)^2}
\\]
Using the quadratic identity $1 - K[M]_1 = \\frac{2}{1 + \\sqrt{1 + 4 K C_{\\text{tot}}}}$:
\\[
\\langle DP_n \\rangle = \\frac{1 + \\sqrt{1 + 4 K C_{\\text{tot}}}}{2} \\approx \\frac{1}{2} + \\sqrt{K C_{\\text{tot}}} \\quad (\\text{for } K C_{\\text{tot}} \\gg 1)
\\]
Given $K = 4.50 \\times 10^4\\text{ M}^{-1}$ and $C_{\\text{tot}} = 1.00 \\times 10^{-3}\\text{ M}$:
\\[
K C_{\\text{tot}} = (4.50 \\times 10^4) \\times (1.00 \\times 10^{-3}) = 45.0
\\]
\\[
4 K C_{\\text{tot}} = 180.0
\\]
\\[
\\langle DP_n \\rangle = \\frac{1 + \\sqrt{1 + 180.0}}{2} = \\frac{1 + \\sqrt{181.0}}{2} = \\frac{1 + 13.4536}{2} = \\frac{14.4536}{2} = 7.23
\\]
In the isodesmic system, the average chain length is only $\\approx 7$ monomer units.

### Step 2: System B (Cooperative) Threshold and Fractions
1. **Critical Polymerization Concentration**:
\\[
C_p = \\frac{1}{K_e} = \\frac{1}{4.50 \\times 10^4\\text{ M}^{-1}} = 2.222 \\times 10^{-5}\\text{ M} = 22.22\\,\\mu\\text{M}
\\]
2. **At $C_{\\text{tot}} = 0.50\\, C_p = 1.111 \\times 10^{-5}\\text{ M}$**:
Because $C_{\\text{tot}} < C_p$, the system is in the pre-nucleation regime.
With cooperativity factor $\\sigma = 1.00 \\times 10^{-4} \\ll 1$:
The fraction converted to polymers is negligible:
\\[
\\alpha_{\\text{poly}} \\approx 0.00\\% \\quad (\\text{essentially } 100\\% \\text{ free monomer})
\\]
3. **At $C_{\\text{tot}} = 5.00\\, C_p = 1.111 \\times 10^{-4}\\text{ M}$**:
Above $C_p$, the concentration of free monomer is pinned at $C_p = 1 / K_e$:
\\[
[M]_{\\text{free}} \\approx C_p
\\]
The polymer fraction is:
\\[
\\alpha_{\\text{poly}} = \\frac{C_{\\text{tot}} - [M]_{\\text{free}}}{C_{\\text{tot}}} = \\frac{5.00 C_p - C_p}{5.00 C_p} = \\frac{4.00}{5.00} = 0.800 \\implies 80.0\\%
\\]
$80\\%$ of all monomers are incorporated into long polymer fibers.

### Step 3: Degree of Polymerization in Cooperative Assembly
At $C_{\\text{tot}} = 1.00 \\times 10^{-3}\\text{ M}$ ($C_{\\text{tot}} / C_p = 45.0$):
In cooperative polymerization well above $C_p$:
\\[
\\langle DP_n \\rangle \\approx \\frac{1}{\\sqrt{\\sigma}} \\sqrt{\\frac{C_{\\text{tot}} - C_p}{C_p}}
\\]
With $\\sigma = 1.00 \\times 10^{-4} \\implies 1 / \\sqrt{\\sigma} = 1 / 0.010 = 100$:
\\[
\\sqrt{\\frac{C_{\\text{tot}} - C_p}{C_p}} = \\sqrt{45.0 - 1.0} = \\sqrt{44.0} = 6.633
\\]
\\[
\\langle DP_n \\rangle \\approx 100 \\times 6.633 = 663.3 \\approx 663
\\]
While the isodesmic system formed short oligomers ($\\langle DP_n \\rangle = 7$), the cooperative system assembles into giant polymers averaging over **660 repeating units**, illustrating the power of nucleation-elongation cooperativity."""
        },
        {
            "probNumber": "7.5",
            "title": "UPy Quadruple Hydrogen-Bonding Dimerization Thermodynamics",
            "difficulty": "Intermediate",
            "statement": """The 2-ureido-4[1H]-pyrimidinone (UPy) motif forms a homodimer through a self-complementary DDAA $\\cdot$ AADD array of four hydrogen bonds:
\\[
2\\,\\text{UPy} \\xrightleftharpoons{K_{\\text{dim}}} (\\text{UPy})_2
\\]
In deuterated chloroform ($\\text{CDCl}_3$) at $T = 298.15\\text{ K}$, the dimerization constant is $K_{\\text{dim}} = 6.00 \\times 10^7\\text{ M}^{-1}$.
(a) Calculate the standard Gibbs free energy of dimerization $\\Delta G_{\\text{dim}}^\circ$ in $\\text{kJ/mol}$.
(b) In a $C_{\\text{tot}} = 1.00 \\times 10^{-2}\\text{ M}$ ($10.0\\text{ mM}$) solution of UPy in $\\text{CDCl}_3$:
    (i) Calculate the equilibrium concentration of free monomer $[\\text{UPy}]$,
    (ii) Calculate the molar percentage of UPy molecules assembled into dimers.
(c) According to Jorgensen's model of secondary electrostatic interactions:
    - Each primary hydrogen bond contributes $\\Delta G_{\\text{prim}} \\approx -8.0\\text{ kJ/mol}$.
    - Each attractive cross-interaction ($+-$) contributes $\\Delta G_{\\text{sec}} \\approx -3.0\\text{ kJ/mol}$.
    - Each repulsive cross-interaction ($++$ or $--$) contributes $\\Delta G_{\\text{sec}} \\approx +3.0\\text{ kJ/mol}$.
    Diagram the secondary interactions for the DDAA $\\cdot$ AADD array and compare the theoretical electrostatic sum with an alternating DADA $\\cdot$ ADAD array.""",
            "solution": """### Step 1: Standard Free Energy of Dimerization
Using $\\Delta G_{\\text{dim}}^\circ = -RT \\ln K_{\\text{dim}}$:
\\[
\\Delta G_{\\text{dim}}^\\circ = -(8.31446 \\times 298.15) \\times \\ln(6.00 \\times 10^7) = -2478.96 \\times (17.9099) = -44{,}398\\text{ J/mol} = -44.40\\text{ kJ/mol}
\\]
The dimerization releases $44.40\\text{ kJ/mol}$ of free energy.

### Step 2: Monomer Concentration and Fraction Dimerized
Let $x = [\\text{UPy}]$ be the free monomer concentration.
Then the dimer concentration is $[(\\text{UPy})_2] = K_{\\text{dim}} x^2$.
Conservation of mass:
\\[
C_{\\text{tot}} = x + 2 K_{\\text{dim}} x^2
\\]
\\[
2 K_{\\text{dim}} x^2 + x - C_{\\text{tot}} = 0
\\]
With $2 K_{\\text{dim}} = 2 \\times (6.00 \\times 10^7) = 1.20 \\times 10^8\\text{ M}^{-1}$ and $C_{\\text{tot}} = 1.00 \\times 10^{-2}\\text{ M}$:
\\[
(1.20 \\times 10^8) x^2 + x - 0.010 = 0
\\]
Because $2 K_{\\text{dim}} C_{\\text{tot}} = 1.20 \\times 10^6 \\gg 1$, $x \\approx \\sqrt{C_{\\text{tot}} / (2 K_{\\text{dim}})}$:
\\[
x = \\sqrt{\\frac{0.010}{1.20 \\times 10^8}} = \\sqrt{8.333 \\times 10^{-11}} = 9.129 \\times 10^{-6}\\text{ M} = 9.13\\,\\mu\\text{M}
\\]
The percentage of UPy molecules assembled into dimers is:
\\[
\\%\\text{ Dimerized} = \\frac{C_{\\text{tot}} - x}{C_{\\text{tot}}} \\times 100\\% = \\left( 1 - \\frac{9.129 \\times 10^{-6}}{1.00 \\times 10^{-2}} \\right) \\times 100\\% = (1 - 0.000913) \\times 100\\% = 99.91\\%
\\]
Over $99.9\\%$ of all monomers are assembled into dimers.

### Step 3: Jorgensen Secondary Electrostatic Analysis
In a four-hydrogen-bond array:
1. **DDAA $\\cdot$ AADD Array (UPy)**:
   - Primary interactions: 4 hydrogen bonds $\\implies 4 \\times (-8.0) = -32.0\\text{ kJ/mol}$.
   - Adjacent diagonal cross-interactions:
     Pair 1-2: Donor 1 interacts with Acceptor 2 (attractive $+-$) $\\implies -3.0\\text{ kJ/mol}$.
     Pair 2-3: Donor 2 interacts with Donor 3 (repulsive $++$) $\\implies +3.0\\text{ kJ/mol}$.
     Pair 3-4: Acceptor 3 interacts with Donor 4 (attractive $+-$) $\\implies -3.0\\text{ kJ/mol}$.
   - Next-nearest neighbors (distance 2):
     Pair 1-3: Donor 1 with Donor 3 (repulsive) $\\approx +1.5\\text{ kJ/mol}$.
     Pair 2-4: Donor 2 with Acceptor 4 (attractive) $\\approx -1.5\\text{ kJ/mol}$.
   - Net secondary interactions: Mostly cancel or net attractive ($-3.0\\text{ kJ/mol}$).
   - Total predicted energy: $\\Delta G \\approx -35.0\\text{ to } -42.0\\text{ kJ/mol}$, closely matching the experimental $-44.4\\text{ kJ/mol}$.
2. **DADA $\\cdot$ ADAD Array (Alternating)**:
   - Primary interactions: 4 hydrogen bonds $\\implies -32.0\\text{ kJ/mol}$.
   - Adjacent cross-interactions: Every single diagonal neighbor is between like charges ($D\\cdots D$ or $A\\cdots A$):
     Six repulsive cross-interactions!
     $\\Delta G_{\\text{sec}} = +6 \\times (+3.0) = +18.0\\text{ kJ/mol}$.
   - Total predicted energy: $\\Delta G \\approx -32.0 + 18.0 = -14.0\\text{ kJ/mol}$.
   - Resulting $K_{\\text{dim}} \\approx 10^2\\text{ M}^{-1}$.
Grouping donors together (DDAA) rather than alternating them (DADA) enhances the association constant by **five orders of magnitude** purely through secondary electrostatic dipole alignment."""
        },
        {
            "probNumber": "7.6",
            "title": "Cavity-Promoted Diels-Alder Catalysis in Fujita's Coordination Cage",
            "difficulty": "Intermediate",
            "statement": """Fujita's octahedral coordination cage, $[(\\text{en})_6\\text{Pd}_6(\\text{TPT})_4]^{12+}$ ($C$), encapsulates 9-hydroxymethylanthracene ($A$) and $N$-cyclohexylmaleimide ($M$) inside its hydrophobic cavity in aqueous solution at $T = 298.15\\text{ K}$, catalyzing their Diels-Alder cycloaddition:
\\[
C + A + M \\xrightleftharpoons{K_{\\text{ternary}}} [A \\cdot M \\subset C] \\xrightarrow{k_{\\text{intra}}} [P \\subset C] \\xrightleftharpoons{K_{\\text{prod}}} C + P
\\]
- The ternary association constant is $K_{\\text{ternary}} = 1.25 \\times 10^5\\text{ M}^{-2}$.
- The first-order intracomplex cycloaddition rate constant is $k_{\\text{intra}} = 3.60 \\times 10^{-3}\\text{ s}^{-1}$.
- In uncatalyzed aqueous solution outside the cage, the second-order rate constant is $k_{\\text{uncat}} = 2.40 \\times 10^{-5}\\text{ M}^{-1}\\text{s}^{-1}$.
(a) Calculate the effective molarity ($EM = k_{\\text{intra}} / k_{\\text{uncat}}$) achieved inside the cage cavity.
(b) Under conditions where cage $C$ is at $[C]_0 = 2.00 \\times 10^{-3}\\text{ M}$ and reactants are at $[A] = [M] = 1.00 \\times 10^{-2}\\text{ M}$:
    (i) Calculate the concentration of the pre-assembled ternary complex $[A \\cdot M \\subset C]$ at steady state.
    (ii) Calculate the initial rate of catalyzed product formation $v_{\\text{cat}}$ in $\\text{M/s}$.
(c) Calculate the initial rate of uncatalyzed reaction $v_{\\text{uncat}}$ in the same solution volume and find the overall catalytic rate enhancement $v_{\\text{cat}} / v_{\\text{uncat}}$.""",
            "solution": """### Step 1: Effective Molarity Calculation
The effective molarity represents the apparent local concentration of reactants inside the confined nanospace of the cage:
\\[
EM = \\frac{k_{\\text{intra}}}{k_{\\text{uncat}}} = \\frac{3.60 \\times 10^{-3}\\text{ s}^{-1}}{2.40 \\times 10^{-5}\\text{ M}^{-1}\\text{s}^{-1}} = 150\\text{ M}
\\]
Confinement inside the cage cavity forces the two reactants into an effective local concentration of $150\\text{ M}$, far exceeding the solubility limit of either organic compound in water.

### Step 2: Ternary Complex Concentration and Catalyzed Rate
Given:
- $[C]_0 = 2.00 \\times 10^{-3}\\text{ M}$
- $[A] = 1.00 \\times 10^{-2}\\text{ M}$, $[M] = 1.00 \\times 10^{-2}\\text{ M}$
- $K_{\\text{ternary}} = 1.25 \\times 10^5\\text{ M}^{-2}$

Let $T = [A \\cdot M \\subset C]$.
\\[
T = K_{\\text{ternary}} [C]_{\\text{free}} [A] [M]
\\]
Since $[A]$ and $[M]$ are in excess relative to $[C]_0$:
\\[
[C]_0 = [C]_{\\text{free}} + T = [C]_{\\text{free}} \\left( 1 + K_{\\text{ternary}} [A][M] \\right)
\\]
Calculate saturation factor:
\\[
K_{\\text{ternary}} [A][M] = (1.25 \\times 10^5\\text{ M}^{-2}) \\times (1.00 \\times 10^{-2}\\text{ M}) \\times (1.00 \\times 10^{-2}\\text{ M}) = 1.25 \\times 10^5 \\times 1.00 \\times 10^{-4} = 12.50
\\]
Thus:
\\[
[C]_{\\text{free}} = \\frac{[C]_0}{1 + 12.50} = \\frac{2.00 \\times 10^{-3}\\text{ M}}{13.50} = 1.481 \\times 10^{-4}\\text{ M}
\\]
The concentration of the encapsulated reactive ternary complex is:
\\[
T = [C]_0 - [C]_{\\text{free}} = 2.00 \\times 10^{-3} - 0.1481 \\times 10^{-3} = 1.852 \\times 10^{-3}\\text{ M}
\\]
The initial rate of the catalyzed reaction is:
\\[
v_{\\text{cat}} = k_{\\text{intra}} \\times T = (3.60 \\times 10^{-3}\\text{ s}^{-1}) \\times (1.852 \\times 10^{-3}\\text{ M}) = 6.667 \\times 10^{-6}\\text{ M/s}
\\]

### Step 3: Uncatalyzed Rate and Overall Rate Enhancement
The uncatalyzed background rate in bulk solution is:
\\[
v_{\\text{uncat}} = k_{\\text{uncat}} [A][M] = (2.40 \\times 10^{-5}\\text{ M}^{-1}\\text{s}^{-1}) \\times (1.00 \\times 10^{-2}\\text{ M}) \\times (1.00 \\times 10^{-2}\\text{ M})
\\]
\\[
v_{\\text{uncat}} = (2.40 \\times 10^{-5}) \\times (1.00 \\times 10^{-4}) = 2.40 \\times 10^{-9}\\text{ M/s}
\\]
The catalytic rate enhancement is:
\\[
\\frac{v_{\\text{cat}}}{v_{\\text{uncat}}} = \\frac{6.667 \\times 10^{-6}\\text{ M/s}}{2.40 \\times 10^{-9}\\text{ M/s}} = 2{,}778 \\approx 2.78 \\times 10^3
\\]
In the presence of only $2.0\\text{ mM}$ coordination cage, the Diels-Alder reaction proceeds nearly $2{,}800$ times faster than in cage-free aqueous solution."""
        },
        {
            "probNumber": "7.7",
            "title": "Minimal Autocatalytic Self-Replicating System: Parabolic Kinetics",
            "difficulty": "Advanced",
            "statement": """In Rebek's minimal artificial self-replicating system, template $T$ catalyzes its own formation from precursors $A$ and $B$:
\\[
A + B \\xrightarrow{k_0} T \\quad (\\text{uncatalyzed background})
\\]
\\[
A + B + T \\xrightarrow{k_{\\text{cat}}} 2\\,T \\quad (\\text{templated pathway})
\\]
Because product $T$ self-dimerizes into an unreactive homodimer $T_2$ with large dimerization constant $K_d = [T_2] / [T_{\\text{free}}]^2 = 5.00 \\times 10^5\\text{ M}^{-1}$, the free active template is in rapid pre-equilibrium with inactive dimer:
\\[
[T_{\\text{free}}] \\approx \\left( \\frac{[T]}{2 K_d} \\right)^{1/2}
\\]
where $[T]$ is total produced template.
(a) Derive the differential rate equation for total template production $\\frac{d[T]}{dt}$ as a function of $[A]$, $[B]$, and $[T]$.
(b) Assuming large excess of precursors $[A] \\approx [A]_0 = 0.050\\text{ M}$ and $[B] \\approx [B]_0 = 0.050\\text{ M}$ (pseudo-steady conditions), and negligible uncatalyzed background ($k_0 \\approx 0$):
    Show that $[T](t)$ grows according to the parabolic law $[T](t) = \\left( \\frac{1}{2} k_{\\text{app}} t + \\sqrt{[T]_0} \\right)^2$.
(c) Given $k_{\\text{cat}} = 1.40 \\times 10^2\\text{ M}^{-2}\\text{s}^{-1}$, $[T]_0 = 1.00 \\times 10^{-5}\\text{ M}$ at $t = 0$:
    Calculate the time required to produce $[T] = 1.00 \\times 10^{-3}\\text{ M}$ ($1.00\\text{ mM}$) of template.""",
            "solution": """### Step 1: Derivation of the Rate Equation
Total rate of template formation:
\\[
\\frac{d[T]}{dt} = k_0 [A][B] + k_{\\text{cat}} [A][B] [T_{\\text{free}}]
\\]
Substitute $[T_{\\text{free}}] = \\left( \\frac{[T]}{2 K_d} \\right)^{1/2}$:
\\[
\\frac{d[T]}{dt} = k_0 [A][B] + \\frac{k_{\\text{cat}}}{\\sqrt{2 K_d}} [A][B] [T]^{1/2}
\\]
This is the celebrated **square-root (parabolic) rate law** of non-enzymatic self-replication.

### Step 2: Integration of the Parabolic Rate Law
Under constant $[A] = [A]_0$ and $[B] = [B]_0$, and neglecting $k_0$:
\\[
\\frac{d[T]}{dt} = k_{\\text{app}} [T]^{1/2}
\\]
where:
\\[
k_{\\text{app}} = \\frac{k_{\\text{cat}}}{\\sqrt{2 K_d}} [A]_0 [B]_0
\\]
Separate variables:
\\[
\\frac{d[T]}{[T]^{1/2}} = k_{\\text{app}} dt
\\]
Integrate from $t = 0$ ($[T] = [T]_0$) to $t$:
\\[
\\int_{[T]_0}^{[T]} [T]^{-1/2} d[T] = k_{\\text{app}} \\int_0^t dt
\\]
\\[
2 \\left( \\sqrt{[T]} - \\sqrt{[T]_0} \\right) = k_{\\text{app}} t
\\]
\\[
\\sqrt{[T]} = \\sqrt{[T]_0} + \\frac{1}{2} k_{\\text{app}} t
\\]
Squaring both sides yields the parabolic growth profile:
\\[
[T](t) = \\left( \\sqrt{[T]_0} + \\frac{1}{2} k_{\\text{app}} t \\right)^2
\\]

### Step 3: Numerical Time Calculation
Given:
- $k_{\\text{cat}} = 1.40 \\times 10^2\\text{ M}^{-2}\\text{s}^{-1}$
- $K_d = 5.00 \\times 10^5\\text{ M}^{-1} \\implies \\sqrt{2 K_d} = \\sqrt{1.00 \\times 10^6} = 1{,}000\\text{ M}^{-1/2}$
- $[A]_0 = 0.050\\text{ M}, [B]_0 = 0.050\\text{ M} \\implies [A]_0 [B]_0 = 2.50 \\times 10^{-3}\\text{ M}^2$

Calculate $k_{\\text{app}}$:
\\[
k_{\\text{app}} = \\frac{1.40 \\times 10^2}{1{,}000} \\times (2.50 \\times 10^{-3}) = (0.140) \\times (2.50 \\times 10^{-3}) = 3.50 \\times 10^{-4}\\text{ M}^{1/2}\\text{s}^{-1}
\\]
Target concentrations:
- $[T]_0 = 1.00 \\times 10^{-5}\\text{ M} \\implies \\sqrt{[T]_0} = 3.1623 \\times 10^{-3}\\text{ M}^{1/2}$
- $[T] = 1.00 \\times 10^{-3}\\text{ M} \\implies \\sqrt{[T]} = 3.1623 \\times 10^{-2}\\text{ M}^{1/2}$
Difference:
\\[
\\sqrt{[T]} - \\sqrt{[T]_0} = (3.1623 - 0.31623) \\times 10^{-2} = 2.8461 \\times 10^{-2}\\text{ M}^{1/2}
\\]
Solve for time $t$:
\\[
t = \\frac{2 \\left( \\sqrt{[T]} - \\sqrt{[T]_0} \\right)}{k_{\\text{app}}} = \\frac{2 \\times (2.8461 \\times 10^{-2}\\text{ M}^{1/2})}{3.50 \\times 10^{-4}\\text{ M}^{1/2}\\text{s}^{-1}} = \\frac{5.6922 \\times 10^{-2}}{3.50 \\times 10^{-4}} = 162.63\\text{ s} \\approx 2.71\\text{ minutes}
\\]
The system produces a 100-fold amplification of template in $2.7$ minutes via parabolic autocatalysis."""
        },
        {
            "probNumber": "7.8",
            "title": "Statistical Mechanics of Nucleation-Elongation: Goldstein-Stryer Model",
            "difficulty": "Advanced",
            "statement": """In the Goldstein-Stryer statistical thermodynamic model of cooperative supramolecular polymerization, aggregate sizes follow a grand canonical partition function with cooperativity parameter $\\sigma = K_n / K_e \\ll 1$:
The fraction of monomer converted to polymer aggregates, $\\alpha(T)$, as a function of temperature $T$ near the elongation temperature $T_e$ is given by:
\\[
\\alpha(T) = 1 - \\exp\\left[ -\\frac{h_e}{R T_e^2} (T_e - T) \\right] \\quad (\\text{for } T < T_e)
\\]
where $h_e = -\\Delta H_e^\circ > 0$ is the enthalpy of elongation per monomer addition.
For an oligo(p-phenylenevinylene) derivative in methylcyclohexane:
- $T_e = 325.0\\text{ K}$ ($51.85^\\circ\\text{C}$)
- $\\Delta H_e^\circ = -65.0\\text{ kJ/mol} \\implies h_e = +65{,}000\\text{ J/mol}$
- $\\sigma = 2.50 \\times 10^{-4}$
(a) Calculate the transition steepness parameter $\\gamma = \\frac{h_e}{R T_e^2}$ in $\\text{K}^{-1}$.
(b) Calculate the temperature interval $\\Delta T_{10-90} = T_{10\\%} - T_{90\\%}$ over which the polymer fraction transitions from $\\alpha = 0.10$ to $\\alpha = 0.90$.
(c) The average aggregate size at the elongation temperature $T_e$ is given by $\\langle DP_n \\rangle(T_e) = \\sigma^{-1/3}$. Calculate $\\langle DP_n \\rangle$ at $T_e$ and explain why cooperative polymerizations exhibit a sharp thermal transition mimicking a first-order phase transition.""",
            "solution": """### Step 1: Steepness Parameter Calculation
Given:
- $h_e = 65{,}000\\text{ J/mol}$
- $T_e = 325.0\\text{ K} \\implies T_e^2 = 105{,}625\\text{ K}^2$
- $R = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$
\\[
\\gamma = \\frac{h_e}{R T_e^2} = \\frac{65{,}000\\text{ J/mol}}{(8.31446\\text{ J/(mol}\\cdot\\text{K)}) \\times (105{,}625\\text{ K}^2)} = \\frac{65{,}000}{878{,}215} = 0.074014\\text{ K}^{-1}
\\]

### Step 2: Temperature Interval for 10% to 90% Transition
Rearrange the Goldstein-Stryer relation for $(T_e - T)$:
\\[
1 - \\alpha = \\exp(-\\gamma (T_e - T)) \\implies \\gamma (T_e - T) = -\\ln(1 - \\alpha) \\implies T_e - T = -\\frac{\\ln(1 - \\alpha)}{\\gamma}
\\]
1. **For $\\alpha = 0.10$**:
\\[
T_e - T_{10\\%} = -\\frac{\\ln(0.90)}{0.074014} = \\frac{0.10536}{0.074014} = 1.4235\\text{ K}
\\]
\\[
T_{10\\%} = 325.0 - 1.4235 = 323.58\\text{ K}
\\]

2. **For $\\alpha = 0.90$**:
\\[
T_e - T_{90\\%} = -\\frac{\\ln(0.10)}{0.074014} = \\frac{2.30259}{0.074014} = 31.1102\\text{ K}
\\]
\\[
T_{90\\%} = 325.0 - 31.1102 = 293.89\\text{ K}
\\]
The temperature width of the transition is:
\\[
\\Delta T_{10-90} = T_{10\\%} - T_{90\\%} = 323.58 - 293.89 = 29.69\\text{ K}
\\]

### Step 3: Aggregate Size at $T_e$ and Physical Interpretation
At the critical elongation threshold $T = T_e$:
\\[
\\langle DP_n \\rangle(T_e) = \\sigma^{-1/3} = (2.50 \\times 10^{-4})^{-1/3} = (4{,}000)^{1/3} = 15.87 \\approx 16
\\]
- **Physical Interpretation**:
  In an isodesmic process, chains grow monomer-by-monomer across a broad temperature span ($>100\\text{ K}$).
  In contrast, in the cooperative model ($\sigma = 2.50 \\times 10^{-4} \\ll 1$), forming small nuclei is thermodynamically heavily penalized. Once temperature drops below $T_e$, the favorable elongation enthalpy ($-65\\text{ kJ/mol}$) suddenly overcomes this nucleation resistance. The existing nuclei instantly trigger rapid elongation, consuming free monomers in an avalanche-like cooperative condensation that sharply mirrors a classical first-order phase transition (such as freezing or crystallization)."""
        },
        {
            "probNumber": "7.9",
            "title": "Self-Sorting in Multi-Component Libraries: Social vs Narcissistic Sorting",
            "difficulty": "Advanced",
            "statement": """A dynamic library contains two distinct ditopic bipyridine ligands, $L_A$ (length $1.20\\text{ nm}$) and $L_B$ (length $1.80\\text{ nm}$), mixed with equimolar $[(\\text{en})\\text{Pd}]^{2+}$ ($M$) in a $1:1:2$ molar ratio ($[L_A]_0 = [L_B]_0 = 1.00\\text{ mM}$, $[M]_0 = 2.00\\text{ mM}$).
The system can form:
1. Two homoleptic molecular squares: $[M_4 (L_A)_4]$ ($A_4$) and $[M_4 (L_B)_4]$ ($B_4$) (**narcissistic self-sorting**).
2. Heteroleptic mixed squares: $[M_4 (L_A)_3 (L_B)_1]$, $[M_4 (L_A)_2 (L_B)_2]$, $[M_4 (L_A)_1 (L_B)_3]$ (**social mixing**).
In an unconstrained statistical library with zero enthalpy difference, the statistical distribution of $A_n B_{4-n}$ conforms to binomial coefficients: $\\binom{4}{n} / 16$.
(a) Calculate the purely statistical mole fractions of homoleptic ($A_4 + B_4$) versus heteroleptic ($A_3 B + A_2 B_2 + A B_3$) assemblies.
(b) Due to geometric length mismatch ($\Delta L = 0.60\\text{ nm}$), inserting both $L_A$ and $L_B$ into the same cyclic square introduces ring strain of $\\Delta H_{\\text{strain}}^\circ = +18.50\\text{ kJ/mol}$ per heteroleptic junction.
At $T = 298.15\\text{ K}$, calculate the Boltzmann suppression factor $e^{-\\Delta H_{\\text{strain}}^\circ / RT}$ for heteroleptic species.
(c) Calculate the equilibrium fidelity of narcissistic self-sorting, defined as the percentage of all assembled squares that are purely homoleptic ($A_4$ and $B_4$).""",
            "solution": """### Step 1: Statistical Distribution in the Absence of Strain
In an equimolar mixture ($[L_A] = [L_B]$) with zero energy bias, the distribution of tetrameric squares $A_n B_{4-n}$ is governed by the binomial expansion $(1/2 + 1/2)^4$:
- $A_4$: $\\binom{4}{4} (1/2)^4 = 1/16 = 6.25\\%$
- $A_3 B_1$: $\\binom{4}{3} (1/2)^4 = 4/16 = 25.00\\%$
- $A_2 B_2$: $\\binom{4}{2} (1/2)^4 = 6/16 = 37.50\\%$
- $A_1 B_3$: $\\binom{4}{1} (1/2)^4 = 4/16 = 25.00\\%$
- $B_4$: $\\binom{4}{0} (1/2)^4 = 1/16 = 6.25\\%$

1. **Total Statistical Homoleptic Fraction**:
\\[
f_{\\text{homo}}^{\\text{stat}} = f(A_4) + f(B_4) = 6.25\\% + 6.25\\% = 12.50\\%
\\]
2. **Total Statistical Heteroleptic Fraction**:
\\[
f_{\\text{hetero}}^{\\text{stat}} = 25.00\\% + 37.50\\% + 25.00\\% = 87.50\\%
\\]
In the absence of geometric constraints, $87.5\\%$ of the products are scrambled heteroleptic mixtures.

### Step 2: Boltzmann Suppression Factor
Given $\\Delta H_{\\text{strain}}^\circ = +18.50\\text{ kJ/mol} = +18{,}500\\text{ J/mol}$ per heteroleptic square:
At $T = 298.15\\text{ K}$, $RT = 8.31446 \\times 298.15 = 2{,}478.96\\text{ J/mol}$:
\\[
\\frac{\\Delta H_{\\text{strain}}^\\circ}{RT} = \\frac{18{,}500}{2{,}478.96} = 7.4628
\\]
The Boltzmann suppression factor for each heteroleptic state is:
\\[
\\kappa = e^{-\\Delta H_{\\text{strain}}^\\circ / RT} = e^{-7.4628} = 5.7405 \\times 10^{-4}
\\]

### Step 3: Equilibrium Narcissistic Self-Sorting Fidelity
The statistical weights of the five states are modified by the Boltzmann factor:
- Weight of $A_4$: $w_0 = 1$
- Weight of $A_3 B$: $w_1 = 4 \\times \\kappa = 4 \\times (5.7405 \\times 10^{-4}) = 2.2962 \\times 10^{-3}$
- Weight of $A_2 B_2$: $w_2 = 6 \\times \\kappa = 6 \\times (5.7405 \\times 10^{-4}) = 3.4443 \\times 10^{-3}$
- Weight of $A B_3$: $w_3 = 4 \\times \\kappa = 4 \\times (5.7405 \\times 10^{-4}) = 2.2962 \\times 10^{-3}$
- Weight of $B_4$: $w_4 = 1$

Sum of all partition weights:
\\[
W_{\\text{total}} = 1 + 2.2962 \\times 10^{-3} + 3.4443 \\times 10^{-3} + 2.2962 \\times 10^{-3} + 1
\\]
\\[
W_{\\text{total}} = 2.0000 + 0.008037 = 2.008037
\\]
The total homoleptic weight is $w_0 + w_4 = 2.0000$.
The narcissistic self-sorting fidelity is:
\\[
\\text{Fidelity} = \\frac{w_0 + w_4}{W_{\\text{total}}} \\times 100\\% = \\frac{2.0000}{2.008037} \\times 100\\% = 99.60\\%
\\]
Geometric mismatch eliminates over $99.6\\%$ of all heteroleptic side products, causing the mixture to cleanly self-sort into purely homoleptic $[M_4(L_A)_4]$ and $[M_4(L_B)_4]$ with near-perfect fidelity."""
        }
    ]

    return {
        "id": "unit-7",
        "number": 7,
        "title": "Supramolecular Self-Assembly, Helicates & Coordination Cages",
        "leadSummary": "Static self-assembly vs dissipative dynamic self-organization, Lehn double and triple metallo-helicates, helical chirality and self-sorting, the directional bonding approach to coordination cages (Fujita squares, octahedra), Stang symmetry matching rules for 2D/3D polyhedra, host-guest catalysis in confined molecular flasks, UPy quadruple hydrogen-bonded polymers, isodesmic vs cooperative polymerization mechanisms, and minimal artificial self-replicating systems.",
        "simulations": ["sim_supra_helicate_cage_assembly"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u7 = get_unit_7()
    print(f"Unit 7 generated: {len(u7['sections'])} sections, {len(u7['problems'])} problems.")
