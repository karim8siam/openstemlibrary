"""
create_supra_u1.py
Creates Unit 1 data dictionary for Supramolecular Chemistry:
Concepts, Non-Covalent Forces & Molecular Recognition Thermodynamics
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_1():
    sections = [
        {
            "secNumber": "1.1",
            "title": "Historical Evolution & Foundations of Supramolecular Chemistry",
            "content": """Supramolecular chemistry represents the chemistry of molecular assemblies and of the intermolecular bond. While classical molecular chemistry focuses on the covalent bond—linking atoms to form molecules through shared electron pairs—supramolecular chemistry investigates the structures, dynamics, and functions of entities formed by the association of two or more chemical species held together by non-covalent intermolecular forces.

### The Conceptual Emergence: From Molecules to Supermolecules
The roots of supramolecular concepts extend back to the late nineteenth century:
1. **Paul Ehrlich (1906)** formulated the pharmacological principle *corpora non agunt nisi fixum* ("substances do not act unless bound"), introducing the receptor concept where therapeutic agents exert bioactivity by specific binding to cellular targets.
2. **Emil Fischer (1894)** established the lock-and-key model (*Schlüssel-Schloss-Prinzip*) to explain the exquisite stereo-specificity of enzymatic catalysis, asserting that substrate and enzyme must exhibit geometric complementarity.
3. **K. L. Wolf (1937)** coined the term *Übermolekül* ("supermolecule") to describe well-defined polymolecular associations, such as carboxylic acid dimers stabilized by cyclic hydrogen-bonding networks.

The modern discipline was inaugurated by the pioneering syntheses of macrocyclic polyethers by Charles J. Pedersen (1967), macrobicyclic cryptands by Jean-Marie Lehn (1969), and preorganized spherands by Donald J. Cram (1973). In 1987, Pedersen, Lehn, and Cram were jointly awarded the Nobel Prize in Chemistry for their development and use of molecules with structure-specific interactions of high selectivity.

### Lehn's Paradigm: "Chemistry Beyond the Molecule"
Jean-Marie Lehn formalized the definition of supramolecular chemistry as:
\\[
\\text{Supramolecular Chemistry} = \\text{Chemistry of Molecular Assemblies and of the Intermolecular Bond}
\\]
Just as the cell represents the biological superstructure formed from organelles, supramolecular architectures represent macroscopic and nanoscale superstructures built from individual, self-contained molecular components.

A supramolecular system is fundamentally characterized by:
- **Reversibility and Dynamism**: Because non-covalent interactions possess lower activation barriers than covalent bonds ($< 100\\text{ kJ/mol}$ versus $200 - 450\\text{ kJ/mol}$), supramolecular systems can undergo continuous association, dissociation, and error-checking, thermodynamically driving the assembly toward the global free energy minimum.
- **Information Storage and Reading**: The geometric shape, electrostatic charge surface, and hydrogen-bonding array of a molecular receptor constitute molecularly encoded information. Complexation represents the "reading" of this chemical code by a complementary substrate.
- **Multivalency and Cooperativity**: Multiple weak non-covalent interactions operate concurrently, achieving macroscopic stability that exceeds the additive sum of isolated interactions through positive cooperativity."""
        },
        {
            "secNumber": "1.2",
            "title": "The Host-Guest Concept, Molecular Receptors & Lock-and-Key Analogy",
            "content": """At the heart of molecular recognition lies the **host-guest relationship**, formalized by Donald J. Cram. A supramolecular complex consists of at least two molecular components: a **host** and a **guest**.

### Definition of Host and Guest
- **Host**: A molecular entity possessing convergent binding sites (such as Lewis basic lone pairs, hydrogen-bond donors/acceptors, or electron-rich $\\pi$-cavities) directed inward toward an internal cavity or cleft.
- **Guest**: A molecular or ionic species possessing divergent binding sites (such as Lewis acidic metal cations, halides, or hydrogen-bonding functional groups) directed outward from its periphery.

The thermodynamic equilibrium for a $1:1$ host-guest complexation event in solution is expressed as:
\\[
\\text{H} + \\text{G} \\xrightleftharpoons[k_{\\text{off}}]{k_{\\text{on}}} \\text{H}\\cdot\\text{G}
\\]
where the thermodynamic association constant (binding constant) $K_a$ is defined by:
\\[
K_a = \\frac{[\\text{H}\\cdot\\text{G}]}{[\\text{H}][\\text{G}]} = \\frac{k_{\\text{on}}}{k_{\\text{off}}}
\\]
and the dissociation constant is $K_d = K_a^{-1}$.

### From Rigid Lock-and-Key to Induced Fit
While Emil Fischer's classical lock-and-key model assumed rigid, static partners, Daniel Koshland (1958) demonstrated that biological receptors often undergo conformational reorganization upon binding—termed **induced fit**.
- In the lock-and-key regime, the host is statically preorganized into the precise binding conformation prior to substrate encounter. No conformational reorganization penalty is incurred.
- In the induced-fit regime, flexible host segments adjust their spatial geometry to maximize intermolecular contacts with the guest. While this optimizes contact energetics, it incurs an unfavorable entropic and conformational strain penalty:
\\[
\\Delta G_{\\text{overall}}^\\circ = \\Delta G_{\\text{intrinsic}}^\\circ + \\Delta G_{\\text{strain}}^\\circ - T\\Delta S_{\\text{conf}}^\\circ
\\]
where $\\Delta G_{\\text{strain}}^\\circ > 0$ and $-T\\Delta S_{\\text{conf}}^\\circ > 0$ detract from the net binding affinity."""
        },
        {
            "secNumber": "1.3",
            "title": "Nature of Non-Covalent Intermolecular Forces: Energetics & Distance Dependences",
            "content": """Supramolecular architectures are stabilized by a hierarchy of non-covalent interactions whose energetic magnitudes and spatial distance dependences dictate receptor design and recognition fidelity.

### Hierarchy of Non-Covalent Forces

| Interaction Type | Typical Energy ($\\text{kJ/mol}$) | Distance Dependence ($V(r)$) | Directional Character | Physical Example |
| :--- | :--- | :--- | :--- | :--- |
| **Ion-Ion (Coulombic)** | $100 - 350$ | $r^{-1}$ | Non-directional | $\\text{R-NH}_3^+ \\cdots ^-\\text{OOC-R'}$ salt bridge |
| **Ion-Dipole** | $50 - 200$ | $r^{-2}$ | Moderately directional | $\\text{K}^+ \\cdots$ 18-crown-6 polyether oxygen |
| **Dipole-Dipole** | $5 - 50$ | $r^{-3}$ (fixed) / $r^{-6}$ (rotating) | Directional | $\\text{C=O} \\cdots \\text{C=O}$ antiparallel alignment |
| **Hydrogen Bonding** | $4 - 120$ | Complex ($r^{-2} - r^{-4}$) | Highly directional ($180^\\circ$) | $\\text{N-H} \\cdots \\text{O=C}$ amide base pairs |
| **Cation-$\\pi$** | $5 - 80$ | $r^{-n}$ ($n = 2 - 3$) | Moderately directional | $\\text{Na}^+$ or $\\text{NMe}_4^+ \\cdots$ benzene quadrupole |
| **$\\pi-\\pi$ Stacking** | $2 - 20$ | $r^{-6}$ | Face-to-face / edge-to-face | Anthracene-pyrene aromatic interactions |
| **Halogen Bonding** | $5 - 180$ | Complex directional | Highly linear ($180^\\circ$ $\\sigma$-hole) | $\\text{C-I} \\cdots ^-\\text{Cl}$ or $\\text{C-I} \\cdots \\text{N}$ |
| **van der Waals (Dispersion)** | $0.5 - 5$ | $r^{-6}$ (Lennard-Jones) | Non-directional | Alkyl chain interdigitation |
| **Hydrophobic / Solvophobic** | Up to $40$ | Solvent-mediated | Non-directional cavity exclusion | Inclusion of toluene into cyclodextrin cavity |

### Mathematical Formulations of Electrostatic Interactions

1. **Ion-Ion Interaction**:
Governed directly by Coulomb's law:
\\[
V_{\\text{ion-ion}}(r) = \\frac{z_1 z_2 e^2}{4\\pi \\epsilon_0 \\epsilon_r r}
\\]
where $z_1, z_2$ are formal ionic valencies, $e = 1.602 \\times 10^{-19}\\text{ C}$, $\\epsilon_0$ is the vacuum permittivity, and $\\epsilon_r$ is the relative permittivity (dielectric constant) of the surrounding solvent medium. In non-polar solvents ($\\epsilon_r \\approx 2 - 4$), ion-ion attractions can approach covalent bond energies ($> 200\\text{ kJ/mol}$), whereas in water ($\\epsilon_r \\approx 78.4$), strong dielectric screening reduces Coulombic energies to $5 - 15\\text{ kJ/mol}$.

2. **Ion-Dipole Interaction**:
An ion of charge $q = z e$ interacting with a neutral molecule possessing permanent dipole moment $\\boldsymbol{\\mu}$ at angle $\\theta$ between the dipole axis and the ion-dipole vector:
\\[
V_{\\text{ion-dipole}}(r, \\theta) = - \\frac{z e \\mu \\cos\\theta}{4\\pi \\epsilon_0 \\epsilon_r r^2}
\\]
Maximum stabilization occurs at $\\theta = 0^\\circ$ (or $180^\\circ$ for an anion), where the attractive pole points directly toward the ionic charge center.

3. **Cation-$\\pi$ Interactions**:
Aromatic rings possess a significant quadrupole moment $\\Theta_{zz} < 0$ arising from the sandwich of electronegative $\\pi$-electron clouds above and below the electropositive $\\sigma$-framework of the carbon ring. A cation positioned on the primary symmetry axis of benzene at distance $z$ experiences an attractive potential:
\\[
V_{\\text{cat-}\\pi}(z) = - \\frac{z e \\Theta_{zz}}{4\\pi \\epsilon_0 \\epsilon_r z^3} - \\frac{(z e)^2 \\alpha}{8\\pi \\epsilon_0 \\epsilon_r z^4}
\\]
where $\\alpha$ is the molecular polarizability of the aromatic ring."""
        },
        {
            "secNumber": "1.4",
            "title": "Preorganization and Complementarity: Cram's Principles of Molecular Recognition",
            "content": """Donald J. Cram formalized the thermodynamic and structural foundations of supramolecular complexation through two universal principles: **preorganization** and **complementarity**.

### The Principle of Complementarity
> *"To complex, hosts must have binding sites that can simultaneously contact and attract the binding sites of guests without generating destabilizing steric repulsions."*

Complementarity operates across four distinct dimensions:
1. **Geometric/Shape Complementarity**: The convex exterior surface of the guest must nest precisely within the concave binding cavity of the host.
2. **Electronic/Electrostatic Complementarity**: Positive electrostatic potentials on the guest must align with negative electrostatic potentials on the host.
3. **Hydrogen-Bond Donor-Acceptor Complementarity**: Hydrogen-bond donor arrays (D) must align in exact sequence and spatial orientation with acceptor arrays (A), such as the Watson-Crick DNA base-pairing sequences (e.g., Guanine [D-D-A] pairing with Cytosine [A-A-D]).
4. **Hydrophobic/Lipophilic Matching**: Non-polar patches on the guest must contact non-polar aromatic or aliphatic domains of the host, shielding both from the high cohesive energy density of water.

### The Principle of Preorganization
> *"The more highly hosts and guests are preorganized for binding and low solvation prior to complexation, the more stable are the resulting complexes."*

A host is defined as **preorganized** if its lowest-energy ground-state conformation in the uncomplexed state is identical to the conformation it adopts within the supramolecular complex.

Thermodynamically, binding free energy is divided into enthalpic and entropic terms:
\\[
\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ
\\]
When a flexible, non-preorganized host binds a guest:
1. It must freeze numerous internal rotatable bonds (each loss of a rotor incurs $-T\\Delta S \\approx +4\\text{ to } +6\\text{ kJ/mol}$ at room temperature).
2. It must overcome internal strain energy to reorient dipole vectors inward.
3. It must expend desolvation enthalpy to strip off solvent molecules strongly hydrogen-bonded to its exposed polar sites.

In contrast, a rigidly preorganized host (such as a Cram spherand) has its binding atoms held immutably in place by a rigid aromatic scaffold. Upon guest entry, no conformational degrees of freedom are lost ($\Delta S_{\\text{conf}}^\\circ \\approx 0$), producing association constants $10^6$ to $10^{12}$ times higher than those of flexible analogues."""
        },
        {
            "secNumber": "1.5",
            "title": "The Chelate Effect & Macrocyclic Effect: Thermodynamic Origins",
            "content": """The extraordinary thermodynamic stability of cyclic and multidentate supramolecular architectures over acyclic monodentate counterparts is governed by the **chelate effect** and the **macrocyclic effect**.

### The Chelate Effect
Consider the displacement of two monodentate ammonia ligands by one bidentate ethylenediamine ($\\text{en}$) ligand on a nickel(II) center:
\\[
[\\text{Ni}(\\text{NH}_3)_6]^{2+} + 3\\,\\text{en} \\xrightleftharpoons{} [\\text{Ni}(\\text{en})_3]^{2+} + 6\\,\\text{NH}_3
\\]
The overall stability constant $\\beta_3$ for the tris(ethylenediamine) complex is roughly $10^{10}$ times larger than $\\beta_6$ for the hexaammine complex.

Thermodynamic origins of the chelate effect:
1. **Translational Entropy Gain**: Four reactant particles generate seven product particles:
\\[
\\Delta S_{\\text{trans}} > 0
\\]
Releasing multiple ordered solvent or monodentate ligand molecules into bulk solution drives a massive positive entropy change.
2. **Effective Local Concentration**: Once the first donor atom of a polydentate ligand coordinates to the metal, the second donor atom is held in close spatial proximity to the coordination sphere. The effective local concentration $C_{\\text{eff}}$ of the pendant donor is given by:
\\[
C_{\\text{eff}} = \\frac{1}{N_A V_{\\text{local}}} \\approx 1 - 50\\text{ M}
\\]
vastly exceeding typical dilute solution concentrations ($10^{-3}\\text{ M}$).

### The Macrocyclic Effect
Formulated by Margerum and Cabbiness (1969), the **macrocyclic effect** states that a cyclic ligand (such as cyclam or 18-crown-6) forms complexes that are $10^3$ to $10^7$ times more stable than those formed by an open-chain ligand possessing the identical number and type of donor atoms (such as tetraamines or tetraglymes).

Thermodynamic comparison between open-chain and cyclic tetramine complexation:
\\[
\\text{Open-Chain}: \\quad \\Delta G_1^\\circ = \\Delta H_1^\\circ - T\\Delta S_1^\\circ
\\]
\\[
\\text{Macrocyclic}: \\quad \\Delta G_2^\\circ = \\Delta H_2^\\circ - T\\Delta S_2^\\circ
\\]
The enhancement $\\Delta \\Delta G^\\circ = \\Delta G_2^\\circ - \\Delta G_1^\\circ < 0$ arises from:
1. **Lower Entropic Penalty**: The cyclic ligand already has its torsional rotations restricted by covalent ring closure. It forfeits fewer rotational degrees of freedom upon binding ($\\Delta S_2^\\circ \\gg \\Delta S_1^\\circ$).
2. **Desolvation Enthalpy**: An open-chain polyether is extensively hydrated in water because its oxygens point outward into solvent. A pre-formed macrocycle has lower solvation free energy due to steric shielding of its interior, reducing the enthalpy required to desolvate the cavity."""
        },
        {
            "secNumber": "1.6",
            "title": "Spherical & Tetrahedral Recognition Principles",
            "content": """Molecular recognition achieves its highest selectivity when the coordination topology of the host matches the coordination polyhedron of the target guest. Jean-Marie Lehn pioneered the classification of receptor cavities based on coordination dimensionality.

### Spherical Recognition: Macrocycles to Macrobicycles
Spherical substrates—exemplified by monoatomic alkali cations ($\\text{Li}^+, \\text{Na}^+, \\text{K}^+, \\text{Cs}^+$), alkaline earth cations ($\\text{Mg}^{2+}, \\text{Ca}^{2+}, \\text{Ba}^{2+}$), and halide anions ($\\text{F}^-, \\text{Cl}^-, \\text{Br}^-$)—possess isotropic, spherically symmetric electrostatic fields.
1. **Monocyclic Hosts (Crown Ethers)** provide a 2D circular planar ring of donor atoms. While they coordinate the equator of a spherical cation, the axial coordination sites remain exposed to solvent or counteranions:
\\[
\\text{Dimensionality of Recognition} = 2\\text{D}
\\]
2. **Macrobicyclic Hosts (Cryptands)** wrap donor arms in three dimensions, encapsulating the spherical ion inside a 3D cage:
\\[
\\text{Dimensionality of Recognition} = 3\\text{D}
\\]
The macrobicyclic cryptate effect produces association constants up to $10^5$ times greater than those of corresponding crown ethers, along with sharp peak selectivity curves where binding constants drop by 3-4 orders of magnitude if the ionic radius deviates by as little as $0.15\\text{ Å}$ from the cryptand cavity radius.

### Tetrahedral Recognition by Macrotricyclic Cryptands
Substrates possessing tetrahedral symmetry—such as the ammonium cation ($\\text{NH}_4^+$), water ($\\text{H}_2\\text{O}$ as dual donor/acceptor), or methane derivatives—require a host with four binding sites arranged at the vertices of a regular tetrahedron ($T_d$ symmetry).

Lehn designed **macrotricyclic cryptands** consisting of four bridgehead nitrogen atoms situated at the vertices of a tetrahedron, interconnected by six polyether or polyamine strands:
- The four nitrogen lone pairs point toward the center of the tetrahedral cavity.
- In the complex $[\\text{NH}_4^+ \\subset \\text{Macrotricycle}]^+$, the four protons of $\\text{NH}_4^+$ form four linear hydrogen bonds to the four apical nitrogens:
\\[
\\text{N-H} \\cdots \\text{N} \\quad (\\angle \\text{N-H}\\cdots\\text{N} = 180^\\circ)
\\]
- The macrotricycle displays exceptional selectivity for $\\text{NH}_4^+$ over $\\text{K}^+$, despite their nearly identical ionic radii ($r_{\\text{NH}_4^+} = 1.48\\text{ Å}$, $r_{\\text{K}^+} = 1.38\\text{ Å}$), because $\\text{K}^+$ seeks spherical non-directional coordination, whereas $\\text{NH}_4^+$ demands tetrahedral directional hydrogen bonding."""
        },
        {
            "secNumber": "1.7",
            "title": "Thermodynamic vs Kinetic Selectivity of Supramolecular Motifs",
            "content": """In evaluating molecular receptors for sensory, catalytic, or separation applications, two fundamentally different selectivity regimes must be distinguished: **thermodynamic selectivity** and **kinetic selectivity**.

### Thermodynamic Selectivity
Thermodynamic selectivity refers to the ratio of equilibrium association constants for a host $\\text{H}$ interacting with two competing guests $\\text{G}_1$ and $\\text{G}_2$:
\\[
S_{\\text{thermo}} = \\frac{K_a(\\text{G}_1)}{K_a(\\text{G}_2)} = \\exp\\left( -\\frac{\\Delta G_1^\\circ - \\Delta G_2^\\circ}{RT} \\right) = \\exp\\left( -\\frac{\\Delta \\Delta G^\\circ}{RT} \\right)
\\]
Because of the exponential relationship, a difference in binding free energy of just $\\Delta \\Delta G^\\circ = 5.7\\text{ kJ/mol}$ at $298\\text{ K}$ yields a 10-fold preference ($S_{\\text{thermo}} = 10$). A difference of $22.8\\text{ kJ/mol}$ yields a 10,000-fold preference.

Thermodynamic selectivity is dictated strictly by ground-state free energies of the initial and final complex states:
\\[
\\Delta \\Delta G^\\circ = [\\Delta H_1^\\circ - \\Delta H_2^\\circ] - T[\\Delta S_1^\\circ - \\Delta S_2^\\circ]
\\]

### Kinetic Selectivity
Kinetic selectivity refers to the ratio of association or dissociation rate constants:
\\[
S_{\\text{kin, on}} = \\frac{k_{\\text{on}}(\\text{G}_1)}{k_{\\text{on}}(\\text{G}_2)}, \\quad S_{\\text{kin, off}} = \\frac{k_{\\text{off}}(\\text{G}_2)}{k_{\\text{off}}(\\text{G}_1)}
\\]
Governed by transition-state theory (Eyring equation):
\\[
k = \\kappa \\frac{k_B T}{h} \\exp\\left( -\\frac{\\Delta G^\\ddagger}{RT} \\right)
\\]

### Interplay Between Thermodynamics and Kinetics
1. **Crown Ethers**: Exhibit fast association rates approaching the diffusion-controlled limit ($k_{\\text{on}} \\sim 10^8 - 10^9\\text{ M}^{-1}\\text{s}^{-1}$) and rapid decomplexation ($k_{\\text{off}} \\sim 10^3 - 10^5\\text{ s}^{-1}$). Selectivity is controlled primarily by $k_{\\text{off}}$ differences, facilitating rapid dynamic exchange.
2. **Cryptands and Spherands**: Encapsulation requires severe conformational distortion of the bicyclic bridges or entry through a tight portal. Consequently, activation barriers for entry and exit are substantial:
   - For cryptates: $k_{\\text{on}} \\sim 10^4 - 10^6\\text{ M}^{-1}\\text{s}^{-1}$, $k_{\\text{off}} \\sim 10^{-2} - 10^1\\text{ s}^{-1}$.
   - For spherands: $k_{\\text{off}}$ can be as slow as $10^{-6}\\text{ s}^{-1}$ (half-lives of weeks or months), exhibiting **kinetic trapping** where a bound guest cannot escape even if a thermodynamically more stable complex exists."""
        },
        {
            "secNumber": "1.8",
            "title": "Experimental Methods for Determining Ka: NMR Titrations, Job Plots & ITC",
            "content": """The quantitative study of supramolecular chemistry requires precision experimental techniques to determine binding stoichiometry ($n$), association constants ($K_a$), and thermodynamic state functions ($\\Delta H^\\circ, \\Delta S^\\circ$).

### 1. NMR Chemical Shift Titrations
Nuclear magnetic resonance (NMR) spectroscopy exploits changes in the electronic shielding environment of host or guest nuclei upon complexation.
- **Fast-Exchange Regime** (on the NMR timescale: $k_{\\text{ex}} \\gg \\Delta \\nu$): A single, population-weighted average chemical shift $\\delta_{\\text{obs}}$ is observed:
\\[
\\delta_{\\text{obs}} = f_{\\text{free}} \\delta_{\\text{free}} + f_{\\text{bound}} \\delta_{\\text{bound}} = \\delta_{\\text{free}} + \\Delta \\delta_{\\max} \\frac{[\\text{H}\\cdot\\text{G}]}{[\\text{H}]_0}
\\]
where $[\\text{H}]_0$ is total host concentration, and $\\Delta \\delta_{\\max} = \\delta_{\\text{bound}} - \\delta_{\\text{free}}$.
For a $1:1$ complex, mass balance yields:
\\[
[\\text{H}\\cdot\\text{G}] = \\frac{1}{2} \\left( [\\text{H}]_0 + [\\text{G}]_0 + \\frac{1}{K_a} - \\sqrt{\\left([\\text{H}]_0 + [\\text{G}]_0 + \\frac{1}{K_a}\\right)^2 - 4[\\text{H}]_0[\\text{G}]_0} \\right)
\\]
Fitting $\\delta_{\\text{obs}}$ versus added guest concentration via non-linear regression extracts both $K_a$ and $\\Delta \\delta_{\\max}$.

### 2. Job Method of Continuous Variations
Introduced by P. Job (1928), this method determines complex stoichiometry:
- Total concentration is held constant: $[\\text{H}]_0 + [\\text{G}]_0 = C_{\\text{total}} = \\text{constant}$.
- The mole fraction of guest $x_{\\text{G}} = [\\text{G}]_0 / C_{\\text{total}}$ is varied continuously from $0$ to $1$.
- An observable signal proportional to complex concentration (such as absorbance change $\\Delta A$ or chemical shift perturbation $\\Delta \\delta \\cdot [\\text{H}]_0$) is plotted against $x_{\\text{G}}$.
- **The curve reaches a maximum at the stoichiometric ratio**:
\\[
x_{\\text{G},\\max} = \\frac{m}{m + n} \\quad \\text{for complex } \\text{H}_n \\text{G}_m
\\]
  - For a $1:1$ complex ($\\text{H}\\cdot\\text{G}$): peak at $x_{\\text{G}} = 0.50$.
  - For a $1:2$ complex ($\\text{H}\\cdot\\text{G}_2$): peak at $x_{\\text{G}} = 2/(1+2) = 0.67$.
  - For a $2:1$ complex ($\\text{H}_2\\cdot\\text{G}$): peak at $x_{\\text{G}} = 1/(2+1) = 0.33$.

### 3. Isothermal Titration Calorimetry (ITC)
ITC is the gold standard for supramolecular thermodynamics because a single automated titration measures the heat of reaction $q_i$ at each injection:
\\[
q_i = \\Delta H^\\circ \\cdot V_{\\text{cell}} \\cdot \\Delta [\\text{H}\\cdot\\text{G}]_i
\\]
Integration of the thermogram peaks directly delivers:
1. The association constant $K_a$ from the inflection slope.
2. The binding enthalpy $\\Delta H^\\circ$ from the plateau amplitude.
3. The binding stoichiometry $n$ from the midpoint molar ratio.
4. The binding entropy from the Gibbs relation:
\\[
\\Delta S^\\circ = \\frac{\\Delta H^\\circ - \\Delta G^\\circ}{T} = \\frac{\\Delta H^\\circ + RT\\ln K_a}{T}
\\]"""
        }
    ]

    problems = [
        {
            "probNumber": "1.1",
            "title": "Mathematical Derivation of the Job Plot Extrema for Complex Stoichiometries",
            "difficulty": "Foundational",
            "statement": """A supramolecular host $\\text{H}$ and guest $\\text{G}$ form a discrete coordination assembly $\\text{H}_n \\text{G}_m$ according to the equilibrium:
\\[
n\\,\\text{H} + m\\,\\text{G} \\xrightleftharpoons[K_a]{} \\text{H}_n \\text{G}_m
\\]
In a Job continuous variation experiment, the total molar concentration is constrained to a fixed constant:
\\[
[\\text{H}]_0 + [\\text{G}]_0 = C_0
\\]
where $x = [\\text{G}]_0 / C_0$ represents the mole fraction of guest, and $1 - x = [\\text{H}]_0 / C_0$ represents the mole fraction of host.
(a) Assuming weak-to-moderate binding where $[\\text{H}] \\approx [\\text{H}]_0$ and $[\\text{G}] \\approx [\\text{G}]_0$, express the complex concentration $[\\text{H}_n \\text{G}_m]$ as a function of $x, C_0, K_a, n, m$.
(b) Derive the condition $d[\\text{H}_n \\text{G}_m]/dx = 0$ and prove that the maximum of the Job curve occurs strictly at:
\\[
x_{\\max} = \\frac{m}{n + m}
\\]
(c) For a $1:1$ complex and a $1:2$ complex with $C_0 = 1.0\\text{ mM}$, determine the theoretical peak positions $x_{\\max}$ and calculate the ratio $[\\text{H}\\cdot\\text{G}_2]_{x=0.67} / [\\text{H}\\cdot\\text{G}_2]_{x=0.50}$.""",
            "solution": """### Step 1: Formulation of Complex Concentration
From the equilibrium expression:
\\[
K_a = \\frac{[\\text{H}_n \\text{G}_m]}{[\\text{H}]^n [\\text{G}]^m} \\implies [\\text{H}_n \\text{G}_m] = K_a [\\text{H}]^n [\\text{G}]^m
\\]
Under the continuous variation condition:
\\[
[\\text{G}]_0 = x C_0, \\quad [\\text{H}]_0 = (1 - x) C_0
\\]
Assuming small extent of complexation relative to total concentration ($[\\text{H}] \\approx (1-x)C_0$ and $[\\text{G}] \\approx x C_0$):
\\[
[\\text{H}_n \\text{G}_m] = K_a [(1 - x) C_0]^n [x C_0]^m = K_a C_0^{n+m} (1 - x)^n x^m
\\]

### Step 2: Differentiation to Find the Extremum
To find the maximum, take the natural logarithm of $[\\text{H}_n \\text{G}_m]$ and differentiate with respect to $x$:
\\[
\\ln [\\text{H}_n \\text{G}_m] = \\ln(K_a C_0^{n+m}) + n \\ln(1 - x) + m \\ln(x)
\\]
Differentiating with respect to $x$:
\\[
\\frac{d}{dx} \\ln [\\text{H}_n \\text{G}_m] = \\frac{1}{[\\text{H}_n \\text{G}_m]} \\frac{d[\\text{H}_n \\text{G}_m]}{dx} = -\\frac{n}{1 - x} + \\frac{m}{x}
\\]
Setting the derivative equal to zero:
\\[
-\\frac{n}{1 - x} + \\frac{m}{x} = 0 \\implies \\frac{m}{x} = \\frac{n}{1 - x}
\\]
Cross-multiplying:
\\[
m(1 - x) = n x \\implies m - m x = n x \\implies (n + m) x = m
\\]
Solving for $x$:
\\[
x_{\\max} = \\frac{m}{n + m}
\\]
The second derivative confirms this is a maximum:
\\[
\\frac{d^2}{dx^2} \\ln [\\text{H}_n \\text{G}_m] = -\\frac{n}{(1-x)^2} - \\frac{m}{x^2} < 0 \\quad \\forall x \\in (0, 1)
\\]

### Step 3: Calculation of Peak Positions and Ratio
1. **For a $1:1$ complex ($n = 1, m = 1$)**:
\\[
x_{\\max} = \\frac{1}{1 + 1} = 0.50
\\]
2. **For a $1:2$ complex ($n = 1, m = 2$)**:
\\[
x_{\\max} = \\frac{2}{1 + 2} = \\frac{2}{3} \\approx 0.667
\\]
3. **Ratio of concentrations for $1:2$ complex**:
\\[
f(x) = (1 - x)^1 x^2
\\]
At $x = 2/3$:
\\[
f(2/3) = \\left(1 - \\frac{2}{3}\\right) \\left(\\frac{2}{3}\\right)^2 = \\frac{1}{3} \\times \\frac{4}{9} = \\frac{4}{27} \\approx 0.14815
\\]
At $x = 1/2$:
\\[
f(1/2) = \\left(1 - \\frac{1}{2}\\right) \\left(\\frac{1}{2}\\right)^2 = \\frac{1}{2} \\times \\frac{1}{4} = \\frac{1}{8} = 0.12500
\\]
The ratio of complex concentrations is:
\\[
\\frac{[\\text{H}\\cdot\\text{G}_2]_{x=0.67}}{[\\text{H}\\cdot\\text{G}_2]_{x=0.50}} = \\frac{4/27}{1/8} = \\frac{32}{27} \\approx 1.185
\\]
The complex concentration is $18.5\\%$ higher at the true Job maximum ($x = 0.67$) than at the equimolar point ($x = 0.50$)."""
        },
        {
            "probNumber": "1.2",
            "title": "Free Energy Breakdown of Macrocyclic Preorganization: Enthalpic vs Entropic Drivers",
            "content": """The binding of potassium cation ($\\text{K}^+$) by an open-chain pentaglyme podand versus the cyclic polyether 18-crown-6 was studied in methanol at $298.15\\text{ K}$ by isothermal titration calorimetry (ITC):
- **Pentaglyme (Podand)**: $K_a = 1.60 \\times 10^2\\text{ M}^{-1}$, $\\Delta H^^\circ = -18.4\\text{ kJ/mol}$
- **18-Crown-6 (Macrocycle)**: $K_a = 1.15 \\times 10^6\\text{ M}^{-1}$, $\\Delta H^^\circ = -56.1\\text{ kJ/mol}$
(a) Calculate the standard Gibbs free energy of binding $\\Delta G^\\circ$ and the entropic contribution $-T\\Delta S^\\circ$ for both hosts at $298.15\\text{ K}$.
(b) Compute the macrocyclic enhancement factors $\\Delta \\Delta G^\\circ$, $\\Delta \\Delta H^\\circ$, and $-T\\Delta \\Delta S^\\circ$.
(c) Dissect the physical origins of the enhancement: Is the macrocyclic effect in this system primarily enthalpy-driven or entropy-driven? Explain using conformational and desolvation arguments.""",
            "statement": """The binding of potassium cation ($\\text{K}^+$) by an open-chain pentaglyme podand versus the cyclic polyether 18-crown-6 was studied in methanol at $298.15\\text{ K}$ by isothermal titration calorimetry (ITC):
- **Pentaglyme (Podand)**: $K_a = 1.60 \\times 10^2\\text{ M}^{-1}$, $\\Delta H^\\circ = -18.4\\text{ kJ/mol}$
- **18-Crown-6 (Macrocycle)**: $K_a = 1.15 \\times 10^6\\text{ M}^{-1}$, $\\Delta H^\\circ = -56.1\\text{ kJ/mol}$
(a) Calculate the standard Gibbs free energy of binding $\\Delta G^\\circ$ and the entropic contribution $-T\\Delta S^\\circ$ for both hosts at $298.15\\text{ K}$.
(b) Compute the macrocyclic enhancement factors $\\Delta \\Delta G^\\circ$, $\\Delta \\Delta H^\\circ$, and $-T\\Delta \\Delta S^\\circ$.
(c) Dissect the physical origins of the enhancement: Is the macrocyclic effect in this system primarily enthalpy-driven or entropy-driven? Explain using conformational and desolvation arguments.""",
            "solution": """### Step 1: Thermodynamic Calculations for Both Hosts
Using the fundamental relations:
\\[
\\Delta G^\\circ = -RT \\ln K_a, \\quad -T\\Delta S^\\circ = \\Delta G^\\circ - \\Delta H^\\circ
\\]
where $R = 8.3145\\text{ J/(mol}\\cdot\\text{K)}$ and $T = 298.15\\text{ K}$ ($RT = 2.4790\\text{ kJ/mol}$).

1. **For Pentaglyme (Podand)**:
\\[
\\Delta G_{\\text{pod}}^\circ = -(2.4790\\text{ kJ/mol}) \\ln(1.60 \\times 10^2) = -(2.4790)(5.0752) = -12.58\\text{ kJ/mol}
\\]
\\[
-T\\Delta S_{\\text{pod}}^\circ = \\Delta G_{\\text{pod}}^\circ - \\Delta H_{\\text{pod}}^\circ = -12.58 - (-18.40) = +5.82\\text{ kJ/mol}
\\]
\\[
\\Delta S_{\\text{pod}}^\circ = -\\frac{5820}{298.15} = -19.52\\text{ J/(mol}\\cdot\\text{K)}
\\]

2. **For 18-Crown-6 (Macrocycle)**:
\\[
\\Delta G_{\\text{mac}}^\circ = -(2.4790\\text{ kJ/mol}) \\ln(1.15 \\times 10^6) = -(2.4790)(13.9553) = -34.60\\text{ kJ/mol}
\\]
\\[
-T\\Delta S_{\\text{mac}}^\circ = \\Delta G_{\\text{mac}}^\circ - \\Delta H_{\\text{mac}}^\circ = -34.60 - (-56.10) = +21.50\\text{ kJ/mol}
\\]
\\[
\\Delta S_{\\text{mac}}^\circ = -\\frac{21500}{298.15} = -72.11\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 2: Evaluation of Enhancement Factors
The macrocyclic enhancement is:
\\[
\\Delta \\Delta G^\\circ = \\Delta G_{\\text{mac}}^\circ - \\Delta G_{\\text{pod}}^\circ = -34.60 - (-12.58) = -22.02\\text{ kJ/mol}
\\]
Ratio of equilibrium constants:
\\[
\\frac{K_a(\\text{18C6})}{K_a(\\text{pentaglyme})} = \\frac{1.15 \\times 10^6}{1.60 \\times 10^2} = 7.19 \\times 10^3
\\]
Component breakdowns:
\\[
\\Delta \\Delta H^\\circ = \\Delta H_{\\text{mac}}^\circ - \\Delta H_{\\text{pod}}^\circ = -56.10 - (-18.40) = -37.70\\text{ kJ/mol}
\\]
\\[
-T\\Delta \\Delta S^\\circ = -T\\Delta S_{\\text{mac}}^\circ - (-T\\Delta S_{\\text{pod}}^\circ) = +21.50 - (+5.82) = +15.68\\text{ kJ/mol}
\\]

### Step 3: Physical Interpretation of the Macrocyclic Effect
The net free energy gain of $-22.02\\text{ kJ/mol}$ is **entirely enthalpy-driven** ($\\Delta \\Delta H^\\circ = -37.70\\text{ kJ/mol}$), which easily overcomes an unfavorable entropic counter-contribution ($-T\\Delta \\Delta S^\\circ = +15.68\\text{ kJ/mol}$).
1. **Enthalpic Origin**: In 18-crown-6, the cyclic architecture enforces all six oxygen lone pairs to point simultaneously toward the central $\\text{K}^+$ ion upon complexation with optimal geometry, maximizing ion-dipole electrostatic interaction and minimizing inter-lone-pair repulsions. Furthermore, open-chain pentaglyme must expend significant enthalpy to undergo conformational reorganization from its elongated, solvent-stabilized conformer to a pseudo-cyclic wrapping geometry.
2. **Entropic Origin**: The podand loses fewer internal rotatable degrees of freedom than expected because solvent methanol molecules organize into a tightly ordered solvation shell around the compact $[\\text{K} \\subset \\text{18-crown-6}]^+$ complex, producing a more negative overall entropy change for the macrocycle in protic media."""
        },
        {
            "probNumber": "1.3",
            "title": "Cation-pi Interaction Mechanics: Electrostatic Quadrupole Formulation & Distance Scaling",
            "difficulty": "Foundational",
            "statement": """A sodium cation ($\\text{Na}^+$, point charge $q = +e = 1.602 \\times 10^{-19}\\text{ C}$) is positioned along the six-fold symmetry axis of a benzene ring at distance $z$ from the ring center. The permanent quadrupole moment of benzene is $\\Theta_{zz} = -29.0 \\times 10^{-40}\\text{ C}\\cdot\\text{m}^2$, and its average polarizability is $\\alpha = 11.5 \\times 10^{-40}\\text{ C}\\cdot\\text{m}^2/\\text{V}$.
(a) Write the analytical expression for the total electrostatic potential energy $U(z) = U_{\\text{quad}}(z) + U_{\\text{ind}}(z)$ in vacuum ($\\epsilon_r = 1$).
(b) Calculate $U_{\\text{quad}}$ and $U_{\\text{ind}}$ in $\\text{kJ/mol}$ at an equilibrium distance $z = 2.45\\text{ Å} = 2.45 \\times 10^{-10}\\text{ m}$.
(c) Evaluate the percentage contribution of polarization versus permanent quadrupole attraction to the total cation-$\\pi$ binding energy at this distance.""",
            "solution": """### Step 1: Analytical Potential Formulations
The electrostatic potential energy of a charge $q$ interacting with an axially symmetric quadrupole $\\Theta_{zz}$ located at the origin is:
\\[
U_{\\text{quad}}(z) = \\frac{q \\Theta_{zz}}{4\\pi \\epsilon_0 z^3}
\\]
where vacuum permittivity $\\epsilon_0 = 8.8542 \\times 10^{-12}\\text{ F/m}$.
The induced dipole interaction energy arising from polarization of the aromatic ring by the electric field $E(z) = \\frac{q}{4\\pi \\epsilon_0 z^2}$ of the cation is:
\\[
U_{\\text{ind}}(z) = -\\frac{1}{2} \\alpha [E(z)]^2 = -\\frac{1}{2} \\alpha \\left( \\frac{q}{4\\pi \\epsilon_0 z^2} \\right)^2 = - \\frac{\\alpha q^2}{32 \\pi^2 \\epsilon_0^2 z^4}
\\]
The total potential energy is:
\\[
U(z) = \\frac{q \\Theta_{zz}}{4\\pi \\epsilon_0 z^3} - \\frac{\\alpha q^2}{32 \\pi^2 \\epsilon_0^2 z^4}
\\]

### Step 2: Numerical Calculation at $z = 2.45\\text{ \AA}$
Given parameters:
- $q = +1.6022 \\times 10^{-19}\\text{ C}$
- $\\Theta_{zz} = -29.0 \\times 10^{-40}\\text{ C}\\cdot\\text{m}^2$
- $\\alpha = 11.5 \\times 10^{-40}\\text{ C}\\cdot\\text{m}^2/\\text{V}$
- $z = 2.45 \\times 10^{-10}\\text{ m} \\implies z^3 = 1.4706 \\times 10^{-29}\\text{ m}^3, \\quad z^4 = 3.6030 \\times 10^{-39}\\text{ m}^4$
- $4\\pi \\epsilon_0 = 4\\pi (8.8542 \\times 10^{-12}) = 1.11265 \\times 10^{-10}\\text{ F/m}$

1. **Permanent Quadrupole Energy**:
\\[
U_{\\text{quad}} = \\frac{(1.6022 \\times 10^{-19})(-29.0 \\times 10^{-40})}{(1.11265 \\times 10^{-10})(1.4706 \\times 10^{-29})} = \\frac{-4.6464 \\times 10^{-58}}{1.6363 \\times 10^{-39}} = -2.8396 \\times 10^{-19}\\text{ J}
\\]
Converting to molar units ($N_A = 6.0221 \\times 10^{23}\\text{ mol}^{-1}$):
\\[
U_{\\text{quad, molar}} = (-2.8396 \\times 10^{-19}\\text{ J})(6.0221 \\times 10^{23}\\text{ mol}^{-1}) \\times 10^{-3} = -171.0\\text{ kJ/mol}
\\]

2. **Induced Dipole Polarization Energy**:
\\[
E(z) = \\frac{1.6022 \\times 10^{-19}}{(1.11265 \\times 10^{-10})(2.45 \\times 10^{-10})^2} = \\frac{1.6022 \\times 10^{-19}}{6.6787 \\times 10^{-30}} = 2.399 \\times 10^{10}\\text{ V/m}
\\]
\\[
U_{\\text{ind}} = -\\frac{1}{2} (11.5 \\times 10^{-40}\\text{ C}\\cdot\\text{m}^2/\\text{V})(2.399 \\times 10^{10}\\text{ V/m})^2 = -\\frac{1}{2}(11.5 \\times 10^{-40})(5.755 \\times 10^{20}) = -3.309 \\times 10^{-19}\\text{ J}
\\]
In molar units:
\\[
U_{\\text{ind, molar}} = (-3.309 \\times 10^{-19}\\text{ J})(6.0221 \\times 10^{23}\\text{ mol}^{-1}) \\times 10^{-3} = -199.3\\text{ kJ/mol}
\\]

3. **Total Interaction Energy**:
\\[
U_{\\text{total}} = U_{\\text{quad, molar}} + U_{\\text{ind, molar}} = -171.0 - 199.3 = -370.3\\text{ kJ/mol}
\\]

### Step 3: Percentage Contributions
\\[
\\% \\text{ Quadrupole} = \\frac{171.0}{370.3} \\times 100\\% = 46.2\\%
\\]
\\[
\\% \\text{ Polarization} = \\frac{199.3}{370.3} \\times 100\\% = 53.8\\%
\\]
At typical van der Waals contact distances ($2.45\\text{ Å}$), polarization accounts for more than half ($53.8\\%$) of the total binding energy, underscoring that cation-$\\pi$ interactions cannot be modeled purely by fixed electrostatic point-charge/quadrupole models."""
        },
        {
            "probNumber": "1.4",
            "title": "Non-Linear Regression Analysis of NMR Chemical Shift Titration for a 1:1 Complex",
            "difficulty": "Intermediate",
            "statement": """In an $^1\\text{H}$ NMR titration experiment in $\\text{CDCl}_3$ at $298\\text{ K}$, a host receptor $\\text{H}$ with constant initial concentration $[\\text{H}]_0 = 2.00\\text{ mM}$ was titrated with guest $\\text{G}$. The chemical shift $\\delta_{\\text{obs}}$ of a host amide proton (free shift $\\delta_{\\text{free}} = 7.820\\text{ ppm}$) was recorded at three titration points:
1. At $[\\text{G}]_0 = 1.00\\text{ mM}$: $\\delta_{\\text{obs}} = 8.140\\text{ ppm}$
2. At $[\\text{G}]_0 = 2.00\\text{ mM}$: $\\delta_{\\text{obs}} = 8.360\\text{ ppm}$
3. At $[\\text{G}]_0 = 10.00\\text{ mM}$: $\\delta_{\\text{obs}} = 8.780\\text{ ppm}$
Assuming the fully bound chemical shift is $\\delta_{\\text{bound}} = 8.920\\text{ ppm}$:
(a) Determine the complex concentration $[\\text{H}\\cdot\\text{G}]$ at each titration point.
(b) Calculate the equilibrium free host concentration $[\\text{H}]$ and free guest concentration $[\\text{G}]$ for point 2 ($[\\text{G}]_0 = 2.00\\text{ mM}$).
(c) Calculate the association constant $K_a$ at each point and evaluate the mean $K_a$ in $\\text{M}^{-1}$.""",
            "solution": """### Step 1: Complex Concentration from Fast-Exchange Averaging
Under the fast-exchange regime:
\\[
\\delta_{\\text{obs}} = \\delta_{\\text{free}} + \\Delta \\delta_{\\max} \\frac{[\\text{H}\\cdot\\text{G}]}{[\\text{H}]_0}
\\]
The maximum chemical shift perturbation is:
\\[
\\Delta \\delta_{\\max} = \\delta_{\\text{bound}} - \\delta_{\\text{free}} = 8.920 - 7.820 = 1.100\\text{ ppm}
\\]
Rearranging for complex concentration:
\\[
[\\text{H}\\cdot\\text{G}] = [\\text{H}]_0 \\cdot \\frac{\\delta_{\\text{obs}} - \\delta_{\\text{free}}}{\\Delta \\delta_{\\max}} = (2.00\\text{ mM}) \\cdot \\frac{\\delta_{\\text{obs}} - 7.820}{1.100}
\\]

1. **Point 1 ($[\\text{G}]_0 = 1.00\\text{ mM}$)**:
\\[
\\Delta \\delta_1 = 8.140 - 7.820 = 0.320\\text{ ppm}
\\]
\\[
[\\text{H}\\cdot\\text{G}]_1 = 2.00 \\times \\frac{0.320}{1.100} = 0.5818\\text{ mM}
\\]

2. **Point 2 ($[\\text{G}]_0 = 2.00\\text{ mM}$)**:
\\[
\\Delta \\delta_2 = 8.360 - 7.820 = 0.540\\text{ ppm}
\\]
\\[
[\\text{H}\\cdot\\text{G}]_2 = 2.00 \\times \\frac{0.540}{1.100} = 0.9818\\text{ mM}
\\]

3. **Point 3 ($[\\text{G}]_0 = 10.00\\text{ mM}$)**:
\\[
\\Delta \\delta_3 = 8.780 - 7.820 = 0.960\\text{ ppm}
\\]
\\[
[\\text{H}\\cdot\\text{G}]_3 = 2.00 \\times \\frac{0.960}{1.100} = 1.7455\\text{ mM}
\\]

### Step 2: Free Concentrations and Association Constant at Point 2
At Point 2 ($[\\text{H}]_0 = 2.00\\text{ mM}, [\\text{G}]_0 = 2.00\\text{ mM}$):
\\[
[\\text{H}]_2 = [\\text{H}]_0 - [\\text{H}\\cdot\\text{G}]_2 = 2.000 - 0.9818 = 1.0182\\text{ mM} = 1.0182 \\times 10^{-3}\\text{ M}
\\]
\\[
[\\text{G}]_2 = [\\text{G}]_0 - [\\text{H}\\cdot\\text{G}]_2 = 2.000 - 0.9818 = 1.0182\\text{ mM} = 1.0182 \\times 10^{-3}\\text{ M}
\\]
Calculating $K_{a, 2}$:
\\[
K_{a, 2} = \\frac{[\\text{H}\\cdot\\text{G}]_2}{[\\text{H}]_2 [\\text{G}]_2} = \\frac{0.9818 \\times 10^{-3}}{(1.0182 \\times 10^{-3})(1.0182 \\times 10^{-3})} = \\frac{0.9818 \\times 10^{-3}}{1.0367 \\times 10^{-6}} = 947\\text{ M}^{-1}
\\]

### Step 3: Association Constants at Points 1 and 3
1. **Point 1**:
\\[
[\\text{H}]_1 = 2.000 - 0.5818 = 1.4182\\text{ mM}
\\]
\\[
[\\text{G}]_1 = 1.000 - 0.5818 = 0.4182\\text{ mM}
\\]
\\[
K_{a, 1} = \\frac{0.5818 \\times 10^{-3}}{(1.4182 \\times 10^{-3})(0.4182 \\times 10^{-3})} = \\frac{0.5818 \\times 10^{-3}}{5.9309 \\times 10^{-7}} = 981\\text{ M}^{-1}
\\]

2. **Point 3**:
\\[
[\\text{H}]_3 = 2.000 - 1.7455 = 0.2545\\text{ mM}
\\]
\\[
[\\text{G}]_3 = 10.000 - 1.7455 = 8.2545\\text{ mM}
\\]
\\[
K_{a, 3} = \\frac{1.7455 \\times 10^{-3}}{(0.2545 \\times 10^{-3})(8.2545 \\times 10^{-3})} = \\frac{1.7455 \\times 10^{-3}}{2.1008 \\times 10^{-6}} = 831\\text{ M}^{-1}
\\]

Mean association constant:
\\[
\\bar{K}_a = \\frac{981 + 947 + 831}{3} = 920\\text{ M}^{-1} \\quad (\\pm 78\\text{ M}^{-1})
\\]
Standard Gibbs free energy of binding:
\\[
\\Delta G^\\circ = -RT \\ln \\bar{K}_a = -(2.4790\\text{ kJ/mol}) \\ln(920) = -16.91\\text{ kJ/mol}
\\]"""
        },
        {
            "probNumber": "1.5",
            "title": "ITC Thermodynamic Binding Parameters: Deconvolution of Gibbs Energy, Enthalpy and Entropy",
            "difficulty": "Intermediate",
            "statement": """An isothermal titration calorimetry (ITC) experiment was performed by titrating an aqueous solution of $\\beta$-cyclodextrin ($[\\text{H}]_0 = 1.20\\text{ mM}$, cell volume $V_0 = 1.40\\text{ mL}$) with 1-adamantanecarboxylate ($[\\text{G}]_{\\text{syr}} = 15.0\\text{ mM}$) at $298.15\\text{ K}$.
Non-linear regression analysis of the integrated injection heats yielded:
- Stoichiometry: $n = 1.00$
- Association constant: $K_a = (4.80 \\pm 0.25) \\times 10^4\\text{ M}^{-1}$
- Enthalpy of binding: $\\Delta H^\\circ = -22.50 \\pm 0.40\\text{ kJ/mol}$
(a) Calculate the standard Gibbs free energy change $\\Delta G^\\circ$ and the standard entropy change $\\Delta S^\\circ$ of complexation.
(b) Evaluate the entropic term $-T\\Delta S^\\circ$ and state whether the binding is enthalpy-driven, entropy-driven, or both.
(c) The heat measured for the first injection ($\Delta V = 5.0\\text{ }\\mu\\text{L}$ of syringe solution injected into the cell containing pure host) was $q_1 = -1.62\\text{ mJ}$. Calculate the theoretical heat expected assuming complete binding of the injected guest, and compute the fraction of injected guest bound.""",
            "solution": """### Step 1: Standard Gibbs Free Energy and Entropy
From the thermodynamic definition:
\\[
\\Delta G^\\circ = -RT \\ln K_a
\\]
With $R = 8.3145\\text{ J/(mol}\\cdot\\text{K)}$ and $T = 298.15\\text{ K}$ ($RT = 2.4790\\text{ kJ/mol}$):
\\[
\\Delta G^\\circ = -(2.4790\\text{ kJ/mol}) \\ln(4.80 \\times 10^4) = -(2.4790)(10.7789) = -26.72\\text{ kJ/mol}
\\]
The entropy of binding is:
\\[
\\Delta S^\\circ = \\frac{\\Delta H^\\circ - \\Delta G^\\circ}{T} = \\frac{-22.50\\text{ kJ/mol} - (-26.72\\text{ kJ/mol})}{298.15\\text{ K}} = \\frac{+4.22\\text{ kJ/mol}}{298.15\\text{ K}} = +14.15\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 2: Enthalpy vs Entropy Partitioning
The entropic term is:
\\[
-T\\Delta S^\\circ = -(298.15\\text{ K})(0.01415\\text{ kJ/(mol}\\cdot\\text{K)}) = -4.22\\text{ kJ/mol}
\\]
Both terms are negative:
\\[
\\Delta H^\\circ = -22.50\\text{ kJ/mol} \\quad (84.2\\% \\text{ of } \\Delta G^\\circ)
\\]
\\[
-T\\Delta S^\\circ = -4.22\\text{ kJ/mol} \\quad (15.8\\% \\text{ of } \\Delta G^\\circ)
\\]
**Conclusion**: The complexation is predominantly **enthalpy-driven** ($84.2\\%$), with a favorable entropic contribution ($15.8\\%$) originating from the hydrophobic release of high-energy water molecules from the uncomplexed $\\beta$-cyclodextrin cavity into bulk solvent.

### Step 3: Heat Analysis for the First Injection
Number of moles of guest injected:
\\[
n_{\\text{G, inj}} = [\\text{G}]_{\\text{syr}} \\times \\Delta V = (15.0 \\times 10^{-3}\\text{ mol/L})(5.0 \\times 10^{-6}\\text{ L}) = 7.50 \\times 10^{-8}\\text{ mol}
\\]
If $100\\%$ of the injected guest forms complex:
\\[
q_{\\text{theo, max}} = n_{\\text{G, inj}} \\times \\Delta H^\\circ = (7.50 \\times 10^{-8}\\text{ mol})(-22.50 \\times 10^3\\text{ J/mol}) = -1.6875 \\times 10^{-3}\\text{ J} = -1.688\\text{ mJ}
\\]
Fraction of injected guest bound:
\\[
f_{\\text{bound}} = \\frac{q_1}{q_{\\text{theo, max}}} = \\frac{-1.62\\text{ mJ}}{-1.688\\text{ mJ}} = 0.960 \\quad (96.0\\%)
\\]
Because host is in massive excess in the cell ($[\\text{H}]_0 = 1.20\\text{ mM}$ vs injected $[\\text{G}]_{\\text{cell}} = 0.053\\text{ mM}$), $96.0\\%$ of injected guest is immediately bound."""
        },
        {
            "probNumber": "1.6",
            "title": "Electrostatic vs Solvation Free Energy in Ion-Dipole Complexation: Born Solvation & Coulombic Potentials",
            "difficulty": "Intermediate",
            "statement": """A spherical cation of radius $r_+ = 1.38\\text{ Å}$ ($\text{K}^+$) carries charge $q = +e$. It is transferred from bulk water ($\\epsilon_w = 78.4$) into the cavity of 18-crown-6 in water.
(a) According to the Born equation, the electrostatic Gibbs free energy of solvating a spherical ion of radius $r$ in a dielectric medium $\\epsilon_r$ is:
\\[
\\Delta G_{\\text{solv}} = - \\frac{N_A e^2}{8\\pi \\epsilon_0 r} \\left( 1 - \\frac{1}{\\epsilon_r} \\right)
\\]
Calculate the Born hydration free energy of $\\text{K}^+$ in water in $\\text{kJ/mol}$.
(b) Inside the 18-crown-6 cavity, the cation is coordinated by six ether oxygen dipoles at distance $d = 2.80\\text{ Å}$ from the cation center. Each oxygen presents an effective partial charge $\\delta = -0.30 e$. Calculate the direct Coulombic interaction energy $U_{\\text{elec}}$ between the cation and the six oxygens in a low-dielectric cavity environment ($\\epsilon_{\\text{cav}} = 3.0$).
(c) Discuss how the host overcomes the immense desolvation penalty of water to achieve overall spontaneous complexation ($\Delta G_{\\text{bind}}^\circ < 0$).""",
            "solution": """### Step 1: Born Hydration Free Energy of $\\text{K}^+$
Given:
- $r_+ = 1.38\\text{ Å} = 1.38 \\times 10^{-10}\\text{ m}$
- $e = 1.6022 \\times 10^{-19}\\text{ C}$
- $N_A = 6.0221 \\times 10^{23}\\text{ mol}^{-1}$
- $\\epsilon_0 = 8.8542 \\times 10^{-12}\\text{ F/m}$
- $\\epsilon_w = 78.4 \\implies 1 - 1/78.4 = 1 - 0.012755 = 0.987245$

The constant prefactor is:
\\[
\\frac{N_A e^2}{8\\pi \\epsilon_0} = \\frac{(6.0221 \\times 10^{23})(1.6022 \\times 10^{-19})^2}{8\\pi (8.8542 \\times 10^{-12})} = \\frac{1.5459 \\times 10^{-14}}{2.2253 \\times 10^{-10}} = 69.47\\text{ J}\\cdot\\text{m/mol} = 69.47 \\times 10^{-3}\\text{ kJ}\\cdot\\text{m/mol}
\\]
More standardly:
\\[
\\frac{N_A e^2}{8\\pi \\epsilon_0} = 69.47 \\times 10^3\\text{ J}\\cdot\\text{nm/mol} = 69.47\\text{ kJ}\\cdot\\text{nm/mol} = 694.7\\text{ kJ}\\cdot\\text{Å/mol}
\\]
Therefore:
\\[
\\Delta G_{\\text{solv}} = -\\frac{694.7\\text{ kJ}\\cdot\\text{Å/mol}}{1.38\\text{ Å}} \\times (0.98725) = -(503.4) \\times 0.98725 = -497.0\\text{ kJ/mol}
\\]
The experimental hydration free energy of $\\text{K}^+$ is $\\approx -337\\text{ kJ/mol}$ (the simple Born equation slightly overestimates due to dielectric saturation near the ion core, but $-337$ to $-497\\text{ kJ/mol}$ is an immense thermodynamic barrier).

### Step 2: Direct Electrostatic Interaction Inside the Cavity
There are $N = 6$ oxygen atoms carrying charge $q_{\\text{O}} = -0.30 e$ at distance $d = 2.80\\text{ Å} = 2.80 \\times 10^{-10}\\text{ m}$ in medium with $\\epsilon_{\\text{cav}} = 3.0$:
\\[
U_{\\text{elec}} = 6 \\times \\frac{N_A (+e)(-0.30 e)}{4\\pi \\epsilon_0 \\epsilon_{\\text{cav}} d}
\\]
Since $\\frac{N_A e^2}{4\\pi \\epsilon_0} = 1389.4\\text{ kJ}\\cdot\\text{Å/mol}$:
\\[
U_{\\text{elec}} = 6 \\times \\frac{(-0.30)(1389.4)}{3.0 \\times 2.80} = 6 \\times \\frac{-416.82}{8.40} = 6 \\times (-49.62) = -297.7\\text{ kJ/mol}
\\]

### Step 3: Thermodynamic Balance
1. **Desolvation vs Complexation**: Stripping bulk water requires paying the cation desolvation penalty. However, in the 18-crown-6 complex, only a portion of the first coordination sphere is replaced: the equatorial waters are replaced by the six crown oxygens ($U_{\\text{elec}} \\approx -298\\text{ kJ/mol}$ plus polarization and charge-transfer), while two axial water molecules remain coordinated to the $\\text{K}^+$ ion above and below the crown ring.
2. **Entropy of Solvent Release**: Desolvating $\\text{K}^+$ releases roughly 6-8 tightly oriented hydration-shell water molecules into bulk water. The increase in solvent rotational and translational entropy ($\Delta S_{\\text{solvent}} > 0$) provides a crucial thermodynamic driving force that compensates for any residual electrostatic deficit."""
        },
        {
            "probNumber": "1.7",
            "title": "Scatchard Analysis and Cooperativity in Multi-Site Host-Guest Recognition",
            "difficulty": "Advanced",
            "statement": """A ditopic cylindrical macropolycyclic receptor $\\text{H}$ possesses two identical, independent binding sites for silver(I) cation ($\\text{Ag}^+$):
\\[
\\text{H} + \\text{Ag}^+ \\xrightleftharpoons[K_1]{} \\text{H}\\cdot\\text{Ag}^+, \\quad \\text{H}\\cdot\\text{Ag}^+ + \\text{Ag}^+ \\xrightleftharpoons[K_2]{} \\text{H}\\cdot(\\text{Ag}^+)_2
\\]
(a) In the absence of allosteric cooperativity, write the statistical relationship connecting $K_1$ and $K_2$ to the microscopic intrinsic binding constant $k_{\\text{int}}$.
(b) Derive the binding polynomial $P([\\text{Ag}^+])$ and express the average binding saturation $\\bar{\\nu}$ (number of bound $\\text{Ag}^+$ per host molecule) as a function of free $[\\text{Ag}^+]$.
(c) Formulate the Scatchard equation:
\\[
\\frac{\\bar{\\nu}}{[\\text{Ag}^+]} = K_{\\text{app}} (N - \\bar{\\nu})
\\]
and sketch how the Scatchard plot ($\\bar{\\nu}/[\\text{Ag}^+]$ vs $\\bar{\\nu}$) distinguishes between non-cooperative, positively cooperative ($\alpha > 1$), and negatively cooperative ($\alpha < 1$) binding, where $\alpha = 4 K_2 / K_1$ is the cooperativity interaction parameter.""",
            "solution": """### Step 1: Statistical Relationship for Independent Identical Sites
Let $k_{\\text{int}}$ be the microscopic intrinsic association constant for an isolated site.
1. **First Binding Step**: The uncomplexed host has 2 equivalent empty sites, so there are 2 statistical ways for $\\text{Ag}^+$ to bind, and 1 way for it to dissociate:
\\[
K_1 = 2\\, k_{\\text{int}}
\\]
2. **Second Binding Step**: The singly bound host has 1 remaining empty site, and 2 equivalent bound $\\text{Ag}^+$ ions that can dissociate:
\\[
K_2 = \\frac{1}{2}\\, k_{\\text{int}}
\\]
Therefore, in the absence of cooperativity:
\\[
\\frac{K_1}{K_2} = \\frac{2 k_{\\text{int}}}{(1/2) k_{\\text{int}}} = 4 \\implies K_2 = \\frac{1}{4} K_1
\\]
The cooperativity parameter is defined as:
\\[
\\alpha = \\frac{4 K_2}{K_1}
\\]
- $\\alpha = 1$: Statistically independent, non-cooperative sites.
- $\\alpha > 1$: Positive cooperativity (binding of first $\\text{Ag}^+$ enhances affinity for the second).
- $\\alpha < 1$: Negative cooperativity (electrostatic repulsion or conformational distortion lowers affinity for the second).

### Step 2: Derivation of the Binding Polynomial and Saturation Function
The binding polynomial (partition function over all host microstates) is:
\\[
P([\\text{Ag}^+]) = 1 + K_1 [\\text{Ag}^+] + K_1 K_2 [\\text{Ag}^+]^2
\\]
The average number of bound ions per host molecule $\\bar{\\nu}$ is:
\\[
\\bar{\\nu} = \\frac{[\\text{H}\\cdot\\text{Ag}^+] + 2[\\text{H}\\cdot(\\text{Ag}^+)_2]}{[\\text{H}] + [\\text{H}\\cdot\\text{Ag}^+] + [\\text{H}\\cdot(\\text{Ag}^+)_2]} = \\frac{K_1 [\\text{Ag}^+] + 2 K_1 K_2 [\\text{Ag}^+]^2}{1 + K_1 [\\text{Ag}^+] + K_1 K_2 [\\text{Ag}^+]^2}
\\]
In terms of the intrinsic constant $k_{\\text{int}}$ and cooperativity parameter $\\alpha$:
\\[
\\bar{\\nu} = \\frac{2 k_{\\text{int}} [\\text{Ag}^+] + 2 \\alpha k_{\\text{int}}^2 [\\text{Ag}^+]^2}{1 + 2 k_{\\text{int}} [\\text{Ag}^+] + \\alpha k_{\\text{int}}^2 [\\text{Ag}^+]^2}
\\]
For independent sites ($\\alpha = 1$):
\\[
1 + 2 k_{\\text{int}} [\\text{Ag}^+] + k_{\\text{int}}^2 [\\text{Ag}^+]^2 = (1 + k_{\\text{int}} [\\text{Ag}^+])^2
\\]
\\[
\\bar{\\nu} = \\frac{2 k_{\\text{int}} [\\text{Ag}^+] (1 + k_{\\text{int}} [\\text{Ag}^+])}{(1 + k_{\\text{int}} [\\text{Ag}^+])^2} = \\frac{2 k_{\\text{int}} [\\text{Ag}^+]}{1 + k_{\\text{int}} [\\text{Ag}^+]}
\\]

### Step 3: The Scatchard Equation and Cooperativity Diagnostics
Rearranging the independent binding saturation relation $\\bar{\\nu} = \\frac{N k_{\\text{int}} [\\text{Ag}^+]}{1 + k_{\\text{int}} [\\text{Ag}^+]}$ (with $N = 2$ total sites):
\\[
\\bar{\\nu} (1 + k_{\\text{int}} [\\text{Ag}^+]) = N k_{\\text{int}} [\\text{Ag}^+] \\implies \\bar{\\nu} = k_{\\text{int}} [\\text{Ag}^+] (N - \\bar{\\nu})
\\]
Dividing by $[\\text{Ag}^+]$ yields the **Scatchard equation**:
\\[
\\frac{\\bar{\\nu}}{[\\text{Ag}^+]} = k_{\\text{int}} (N - \\bar{\\nu}) = N k_{\\text{int}} - k_{\\text{int}} \\bar{\\nu}
\\]
Plotting $\\frac{\\bar{\\nu}}{[\\text{Ag}^+]}$ on the $y$-axis versus $\\bar{\\nu}$ on the $x$-axis:
1. **Non-Cooperative Sites ($\\alpha = 1$)**: A straight line with slope $-k_{\\text{int}}$, $y$-intercept $N k_{\\text{int}} = 2 k_{\\text{int}}$, and $x$-intercept $N = 2$.
2. **Positively Cooperative Sites ($\\alpha > 1$)**: Downwardly convex (bell-shaped curve with initial positive slope reaching a peak, then dropping to $N = 2$).
3. **Negatively Cooperative Sites ($\\alpha < 1$)**: Upwardly concave (curving downward with steep initial slope, leveling off as it approaches $N = 2$). In ditopic receptors, electrostatic repulsion between two close $\\text{Ag}^+$ ions inevitably produces negative cooperativity ($\alpha < 1$)."""
        },
        {
            "probNumber": "1.8",
            "title": "Kinetic vs Thermodynamic Selectivity: Eyring Barrier Trapping of Supramolecular Isomers",
            "difficulty": "Advanced",
            "statement": """A macrobicyclic cryptand host can bind guest cations $\\text{G}_A$ and $\\text{G}_B$. The thermodynamic and kinetic parameters at $298.15\\text{ K}$ are:
- Guest A: $k_{\\text{on, A}} = 1.0 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}$, $k_{\\text{off, A}} = 1.0 \\times 10^2\\text{ s}^{-1}$
- Guest B: $k_{\\text{on, B}} = 2.0 \\times 10^3\\text{ M}^{-1}\\text{s}^{-1}$, $k_{\\text{off, B}} = 1.0 \\times 10^{-4}\\text{ s}^{-1}$
(a) Compute the thermodynamic association constants $K_{a, A}$ and $K_{a, B}$, and the thermodynamic selectivity ratio $S_{\\text{thermo}} = K_{a, B} / K_{a, A}$.
(b) Calculate the kinetic association selectivity $S_{\\text{kin, on}} = k_{\\text{on, A}} / k_{\\text{on, B}}$ and the complex half-lives $t_{1/2} = \\ln(2) / k_{\\text{off}}$ for both complexes.
(c) In an equimolar competitive mixture ($[\\text{G}_A]_0 = [\\text{G}_B]_0 = 10\\text{ mM}$, $[\\text{H}]_0 = 1.0\\text{ mM}$), which complex forms initially at $t = 1\\text{ ms}$? What is the product distribution at $t = 10\\text{ days}$?""",
            "solution": """### Step 1: Thermodynamic Association Constants and Selectivity
From the principle of detailed balance:
\\[
K_a = \\frac{k_{\\text{on}}}{k_{\\text{off}}}
\\]
1. **For Guest A**:
\\[
K_{a, A} = \\frac{1.0 \\times 10^7\\text{ M}^{-1}\\text{s}^{-1}}{1.0 \\times 10^2\\text{ s}^{-1}} = 1.0 \\times 10^5\\text{ M}^{-1}
\\]
\\[
\\Delta G_A^\\circ = -RT \\ln(1.0 \\times 10^5) = -(2.4790\\text{ kJ/mol})(11.5129) = -28.54\\text{ kJ/mol}
\\]

2. **For Guest B**:
\\[
K_{a, B} = \\frac{2.0 \\times 10^3\\text{ M}^{-1}\\text{s}^{-1}}{1.0 \\times 10^{-4}\\text{ s}^{-1}} = 2.0 \\times 10^7\\text{ M}^{-1}
\\]
\\[
\\Delta G_B^\\circ = -RT \\ln(2.0 \\times 10^7) = -(2.4790\\text{ kJ/mol})(16.8112) = -41.67\\text{ kJ/mol}
\\]

3. **Thermodynamic Selectivity**:
\\[
S_{\\text{thermo}} = \\frac{K_{a, B}}{K_{a, A}} = \\frac{2.0 \\times 10^7}{1.0 \\times 10^5} = 200
\\]
Thermodynamically, Guest B is favored by a factor of $200$ ($\\Delta \\Delta G^\\circ = -13.13\\text{ kJ/mol}$).

### Step 2: Kinetic Selectivity and Lifetimes
1. **Kinetic On-Rate Selectivity**:
\\[
S_{\\text{kin, on}} = \\frac{k_{\\text{on, A}}}{k_{\\text{on, B}}} = \\frac{1.0 \\times 10^7}{2.0 \\times 10^3} = 5000
\\]
Guest A enters the host cavity **5,000 times faster** than Guest B.

2. **Complex Half-Lives ($t_{1/2} = \\frac{\\ln 2}{k_{\\text{off}}}$)**:
- **For Complex A**:
\\[
t_{1/2, A} = \\frac{0.69315}{1.0 \\times 10^2\\text{ s}^{-1}} = 6.93 \\times 10^{-3}\\text{ s} = 6.93\\text{ ms}
\\]
- **For Complex B**:
\\[
t_{1/2, B} = \\frac{0.69315}{1.0 \\times 10^{-4}\\text{ s}^{-1}} = 6931.5\\text{ s} \\approx 1.925\\text{ hours}
\\]

### Step 3: Time Evolution in Competitive Mixture
1. **Short Time Scale ($t = 1\\text{ ms}$)**:
At $t = 1\\text{ ms} = 0.001\\text{ s}$, dissociation has not yet occurred significantly for either complex.
The initial rates of formation are:
\\[
R_A = k_{\\text{on, A}} [\\text{H}] [\\text{G}_A], \\quad R_B = k_{\\text{on, B}} [\\text{H}] [\\text{G}_B]
\\]
Because $[\\text{G}_A]_0 = [\\text{G}_B]_0$:
\\[
\\frac{[\\text{H}\\cdot\\text{G}_A]}{[\\text{H}\\cdot\\text{G}_B]} = \\frac{k_{\\text{on, A}}}{k_{\\text{on, B}}} = 5000
\\]
At $1\\text{ ms}$, the system is under pure **kinetic control**: $99.98\\%$ of the complex is $[\\text{H}\\cdot\\text{G}_A]$, and only $0.02\\%$ is $[\\text{H}\\cdot\\text{G}_B]$.

2. **Long Time Scale ($t = 10\\text{ days} = 864,\\!000\\text{ s}$)**:
Since $t = 864,\\!000\\text{ s} \\gg 125 \\times t_{1/2, B}$, both complexes have undergone hundreds of thousands of reversible association/dissociation cycles. The system has reached complete **thermodynamic equilibrium**:
\\[
\\frac{[\\text{H}\\cdot\\text{G}_B]_{\\text{eq}}}{[\\text{H}\\cdot\\text{G}_A]_{\\text{eq}}} = \\frac{K_{a, B} [\\text{G}_B]}{K_{a, A} [\\text{G}_A]} = 200 \\times 1 = 200
\\]
At equilibrium:
\\[
\\% [\\text{H}\\cdot\\text{G}_B] = \\frac{200}{201} \\times 100\\% = 99.50\\%
\\]
\\[
\\% [\\text{H}\\cdot\\text{G}_A] = \\frac{1}{201} \\times 100\\% = 0.50\\%
\\]
This represents a classic supramolecular kinetic trap transitioning to thermodynamic stability."""
        },
        {
            "probNumber": "1.9",
            "title": "Macrotricyclic Cryptand Cavity Volume & Optimal Ionic Radii Coordination Topology",
            "difficulty": "Advanced",
            "statement": """A spherical macrotricyclic cryptand consists of four tertiary amine bridgeheads positioned at the vertices of a regular tetrahedron of circumradius $R_{\\text{tet}}$, connected by six $-(\\text{CH}_2\\text{CH}_2\\text{O})_2\\text{CH}_2\\text{CH}_2-$ polyether strands.
(a) For a regular tetrahedron of edge length $a$, derive the geometric relationships for the circumradius $R_{\\text{tet}}$ and the radius $r_{\\text{in}}$ of the inscribed sphere inside the tetrahedral cavity.
(b) If the edge length defined by the relaxed polyether bridge conformation is $a = 7.00\\text{ Å}$, and each nitrogen atom has a van der Waals radius $r_{\\text{vdW}}(\\text{N}) = 1.55\\text{ Å}$, calculate the maximum accessible cavity radius $r_{\\text{cav}}$ at the center of the cage.
(c) Ammonium cation ($\\text{NH}_4^+$) has an effective ionic radius of $r_{\\text{ion}} = 1.48\\text{ Å}$ and forms four hydrogen bonds of length $d(\\text{N}\\cdots\\text{N}) = 2.85\\text{ Å}$ to the bridgeheads. Determine whether the cage can accommodate $\\text{NH}_4^+$ with optimal linear hydrogen-bonding geometry, and calculate the edge strain $\\Delta a = a_{\\text{bound}} - a_{\\text{free}}$.""",
            "solution": """### Step 1: Geometric Relationships for a Regular Tetrahedron
For a regular tetrahedron with vertices at $(\\pm 1, \\pm 1, \\pm 1)$ scaled by $a / (2\\sqrt{2})$:
1. **Edge Length $a$**:
The distance between two adjacent vertices is $a$.
2. **Circumradius $R_{\\text{tet}}$** (distance from centroid to each vertex):
In Cartesian coordinates, vertices can be placed at:
\\[
\\mathbf{v}_1 = (1, 1, 1), \\quad \\mathbf{v}_2 = (1, -1, -1), \\quad \\mathbf{v}_3 = (-1, 1, -1), \\quad \\mathbf{v}_4 = (-1, -1, 1)
\\]
The edge length between $\\mathbf{v}_1$ and $\\mathbf{v}_2$ is:
\\[
a_0 = \\sqrt{(0)^2 + (2)^2 + (2)^2} = \\sqrt{8} = 2\\sqrt{2}
\\]
The distance from origin $(0,0,0)$ to any vertex is:
\\[
R_0 = \\sqrt{1^2 + 1^2 + 1^2} = \\sqrt{3}
\\]
Scaling to actual edge length $a$:
\\[
R_{\\text{tet}} = a \\cdot \\frac{R_0}{a_0} = a \\frac{\\sqrt{3}}{2\\sqrt{2}} = a \\frac{\\sqrt{6}}{4} \\approx 0.61237\\, a
\\]
3. **Inscribed Radius $r_{\\text{in}}$** (distance from centroid to center of each face):
The face centroid is at $(1/3, 1/3, -1/3)$ with distance $r_0 = \\sqrt{3 \\times (1/9)} = \\sqrt{3}/3 = 1/\\sqrt{3}$:
\\[
r_{\\text{in}} = a \\frac{r_0}{a_0} = a \\frac{1/\\sqrt{3}}{2\\sqrt{2}} = a \\frac{\\sqrt{6}}{12} = \\frac{1}{3} R_{\\text{tet}} \\approx 0.20412\\, a
\\]

### Step 2: Maximum Accessible Cavity Radius
Given relaxed edge length $a = 7.00\\text{ Å}$:
\\[
R_{\\text{tet}} = 7.00 \\times \\frac{\\sqrt{6}}{4} = 7.00 \\times 0.61237 = 4.2866\\text{ Å}
\\]
The distance from the center of the cavity to the nucleus of each bridgehead nitrogen is $R_{\\text{tet}} = 4.287\\text{ Å}$.
Accounting for the van der Waals radius of nitrogen ($r_{\\text{vdW}}(\\text{N}) = 1.55\\text{ Å}$):
\\[
r_{\\text{cav}} = R_{\\text{tet}} - r_{\\text{vdW}}(\\text{N}) = 4.2866 - 1.5500 = 2.737\\text{ Å}
\\]
The free cavity possesses an internal spherical radius of $\\approx 2.74\\text{ Å}$, ample room to enclose monoatomic cations or tetrahedral ions.

### Step 3: Accommodation and Edge Strain for $\\text{NH}_4^+$
For ammonium cation $\\text{NH}_4^+$ positioned at the center of the tetrahedron:
- The four $\\text{N-H}$ bonds point directly toward the four bridgehead nitrogens.
- The optimum $\\text{N}\\cdots\\text{N}$ hydrogen bond distance is $d(\\text{N}_{\\text{guest}}\\cdots\\text{N}_{\\text{host}}) = 2.85\\text{ Å}$.
Therefore, in the fully bound state:
\\[
R_{\\text{bound}} = d(\\text{N}\\cdots\\text{N}) = 2.850\\text{ Å}
\\]
The required edge length $a_{\\text{bound}}$ to achieve this circumradius is:
\\[
a_{\\text{bound}} = \\frac{4}{\\sqrt{6}} R_{\\text{bound}} = \\frac{4}{2.4495} (2.850\\text{ Å}) = 1.63299 \\times 2.850 = 4.654\\text{ Å}
\\]
Comparing with the relaxed polyether bridge length $a = 7.00\\text{ Å}$:
\\[
\\Delta a = a_{\\text{bound}} - a_{\\text{free}} = 4.654 - 7.000 = -2.346\\text{ Å}
\\]
Because the relaxed polyether strands are flexible, they do not remain straight edges; instead, the six flexible strands bow outward into convex curves, allowing the bridgehead nitrogen atoms to contract inward to $R = 2.85\\text{ Å}$ while the oxygen atoms of the strands coordinate around the periphery, perfectly accommodating $\\text{NH}_4^+$ with zero distortion of the ideal $180^\\circ$ $\\text{N-H}\\cdots\\text{N}$ angle."""
        }
    ]

    return {
        "id": "unit-1",
        "number": 1,
        "title": "Concepts, Non-Covalent Forces & Molecular Recognition Thermodynamics",
        "leadSummary": "Historical development of supramolecular chemistry, host-guest chemistry, lock-and-key and induced-fit models, hierarchy of non-covalent intermolecular forces, Cram's principles of preorganization and complementarity, chelate and macrocyclic effects, spherical and tetrahedral recognition, thermodynamic versus kinetic selectivity, and experimental determination of binding constants via NMR titrations, Job plots, and isothermal titration calorimetry (ITC).",
        "simulations": ["sim_supra_binding_titration_job"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u1 = get_unit_1()
    print(f"Unit 1 generated: {len(u1['sections'])} sections, {len(u1['problems'])} problems.")
