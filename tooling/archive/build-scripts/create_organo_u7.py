"""
create_organo_u7.py
Unit 7: Metal Clusters & Wade-Mingos Electron Counting Rules
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_7():
    sections = [
        {
            "id": "sec7_1",
            "title": "§7.1 Definition and Classification of Metal Clusters: Low-Nuclearity vs. High-Nuclearity",
            "content": """By the classic definition formulated by F. Albert Cotton, a **metal cluster** is a molecular or solid-state compound containing a finite group of metal atoms held together entirely, mainly, or at least to a significant extent by direct **metal-metal bonds** ($M-M$). Complexes where metal atoms are held together exclusively by bridging heteroatom ligands without formal metal-metal bonding are excluded from cluster classification.

### Fundamental Categories of Metal Clusters:
1. **Low-Valent Organometallic Carbonyl Clusters**:
   - Metals reside in low formal oxidation states ($-1$ to $+2$), stabilized by $\\pi$-acceptor ligands like carbon monoxide, phosphines, nitrosyls, and cyclopentadienyl rings.
   - Dominated by Groups 7-10 (e.g., $\\text{Mn}, \\text{Fe}, \\text{Ru}, \\text{Os}, \\text{Co}, \\text{Rh}, \\text{Ir}, \\text{Pt}$).
   - Bonding is characterized by delocalized multi-center metal-metal framework bonding governed by Polyhedral Skeletal Electron Pair Theory (PSEPT).
2. **High-Valent Halide/Chalcogenide Clusters (Chevrel Phases & Early Metal Halides)**:
   - Metals reside in intermediate oxidation states ($+2$ to $+3$), coordinated to $\\pi$-donor ligands (halides, alkoxides, chalcogenides).
   - Dominated by early $4d$ and $5d$ metals (e.g., $[\\text{Mo}_6\\text{Cl}_8]^{4+}, [\\text{Nb}_6\\text{Cl}_{12}]^{2+}, [\\text{Re}_3\\text{Cl}_{12}]^{3-}$).
3. **Classification by Nuclearity**:
   - **Low-Nuclearity Metal Clusters (LMCs)**: Contain 3 to 6 metal atoms forming simple geometric polyhedra (triangles, tetrahedra, octahedra).
   - **High-Nuclearity Metal Clusters (HMCs)**: Contain $>12$ metal atoms, forming close-packed metal cores (cuboctahedra, icosahedra, capped polyhedra) that bridge the molecular-solid interface, modeling heterogeneous metal surface physics and quantum size effects."""
        },
        {
            "id": "sec7_2",
            "title": "§7.2 Trimetallic Dodecacarbonyls: Synthesis, Structures & Isomerism of $\\text{Fe}_3$, $\\text{Ru}_3$, and $\\text{Os}_3$",
            "content": """The homoleptic Group 8 trimetallic dodecacarbonyls $M_3(\\text{CO})_{12}$ ($M = \\text{Fe, Ru, Os}$) are the fundamental benchmarks of transition metal cluster chemistry.

### Synthesis:
1. **Triiron Dodecacarbonyl $\\text{Fe}_3(\\text{CO})_{12}$**:
   Prepared by alkaline oxidation/disproportionation of $\\text{Fe}(\\text{CO})_5$ followed by acidification:
   \\[ \\text{Fe}(\\text{CO})_5 + 3\\,\\text{NaOH} \\longrightarrow \\text{Na}[\\text{HFe}(\\text{CO})_4] + \\text{Na}_2\\text{CO}_3 + \\text{H}_2\\text{O} \\]
   \\[ 3\\,[\\text{HFe}(\\text{CO})_4]^- + 3\\,\\text{MnO}_2 + 3\\,\\text{H}^+ \\longrightarrow \\text{Fe}_3(\\text{CO})_{12} + 3\\,\\text{Mn}^{2+} + 6\\,\\text{H}_2\\text{O} \\]
2. **Triruthenium Dodecacarbonyl $\\text{Ru}_3(\\text{CO})_{12}$**:
   Synthesized by reductive carbonylation of ruthenium(III) chloride:
   \\[ 3\\,\\text{RuCl}_3 \\cdot x\\text{H}_2\\text{O} + 12\\,\\text{CO} \\xrightarrow{\\text{MeOH},\\, 65\\text{ atm},\\, 125^\\circ\\text{C}} \\text{Ru}_3(\\text{CO})_{12} \\quad (\\text{bright orange crystals}) \\]
3. **Triosmium Dodecacarbonyl $\\text{Os}_3(\\text{CO})_{12}$**:
   Synthesized by high-pressure carbonylation of osmium tetroxide:
   \\[ 3\\,\\text{OsO}_4 + 24\\,\\text{CO} \\xrightarrow{75\\text{ atm},\\, 160^\\circ\\text{C}} \\text{Os}_3(\\text{CO})_{12} + 12\\,\\text{CO}_2 \\uparrow \\quad (\\text{bright yellow crystals}) \\]

### Structural Divergence and Carbonyl Isomerism:
All three clusters have a total valence electron count ($TVE$) of **48 electrons**, requiring **three 2-center 2-electron ($2c-2e$) metal-metal bonds** ($m = (54 - 48)/2 = 3$) arranged in a triangle:
- **$\\text{Ru}_3(\\text{CO})_{12}$ and $\\text{Os}_3(\\text{CO})_{12}$**:
  Adopt an idealized **$D_{3h}$ symmetry structure** with **all 12 carbonyl ligands terminal**. Each metal center bears two axial CO ligands perpendicular to the $M_3$ plane and two equatorial CO ligands in the $M_3$ plane.
- **$\\text{Fe}_3(\\text{CO})_{12}$**:
  Adopts a lower-symmetry **$C_{2v}$ structure** featuring **two bridging $\\mu_2-\\text{CO}$ ligands** across one $\\text{Fe}-\\text{Fe}$ edge and ten terminal CO ligands.
- **Physical Rationale**: Iron has a smaller covalent radius ($1.32$ Å) than ruthenium ($1.46$ Å) or osmium ($1.47$ Å). Packing 12 terminal carbonyls around a smaller triiron triangle incurs severe van der Waals steric clash between adjacent equatorial ligands. Bridging two carbonyls pulls them inward, relieving steric strain."""
        },
        {
            "id": "sec7_3",
            "title": "§7.3 Reactivity of Trimetallic Clusters: Fragmentation vs. Intact Substitution",
            "content": """The reactivity of trimetallic clusters exhibits a dramatic kinetic dichotomy down Group 8 governed by metal-metal bond strengths:
\\[ D_0(\\text{Fe}-\\text{Fe}) \\approx 100\\text{ kJ/mol} \\ll D_0(\\text{Ru}-\\text{Ru}) \\approx 155\\text{ kJ/mol} < D_0(\\text{Os}-\\text{Os}) \\approx 200\\text{ kJ/mol} \\]

### 1. Cluster Fragmentation vs. Framework Retention:
- **$\\text{Fe}_3(\\text{CO})_{12}$**: Weak $\\text{Fe}-\\text{Fe}$ bonds mean reaction with incoming nucleophiles (phosphines, alkynes, halides) typically results in **cluster fragmentation**, yielding mononuclear or dinuclear complexes:
  \\[ \\text{Fe}_3(\\text{CO})_{12} + 3\\,\\text{PPh}_3 \\longrightarrow 3\\,\\text{Fe}(\\text{CO})_4(\\text{PPh}_3) \\]
- **$\\text{Ru}_3(\\text{CO})_{12}$**: Moderate $\\text{Ru}-\\text{Ru}$ bonds permit thermal ligand substitution with retention of the triangle core under controlled conditions, though aggressive nucleophiles still cause fragmentation.
- **$\\text{Os}_3(\\text{CO})_{12}$**: Robust $\\text{Os}-\\text{Os}$ bonds ($200\\text{ kJ/mol}$) preserve the trimetallic core through extreme chemical transformations, establishing triosmium clusters as ideal models for organometallic cluster reactivity.

### 2. Reactions with Molecular Hydrogen:
- Reaction of $\\text{Os}_3(\\text{CO})_{12}$ with $\\text{H}_2$ at $120^\\circ\\text{C}$ generates **triosmium dihydride**:
  \\[ \\text{Os}_3(\\text{CO})_{12} + \\text{H}_2 \\longrightarrow \\text{H}_2\\text{Os}_3(\\text{CO})_{10} + 2\\,\\text{CO} \\uparrow \\]
  This purple complex contains **46 valence electrons**, making it formally electron-deficient (unsaturated).
  To satisfy the 18e rule, it features a formal **metal-metal double bond** ($\\text{Os}=\\text{Os}$) bridged by two $\\mu_2-\\text{H}$ hydride ligands, displaying exceptional reactivity toward olefins, alkynes, and nitriles at room temperature.

### 3. Reactions with Nitriles and Phosphines:
- Activation of organonitriles $R\\text{CN}$ by $\\text{Ru}_3(\\text{CO})_{12}$ proceeds with $\\text{C-H}$ bond activation to form bridging iminyl or amido clusters: $[\\text{Ru}_3(\\mu-\\text{H})(\\mu-\\eta^2-\\text{N}=\\text{CH}R)(\\text{CO})_{10}]$.
- Use of trimethylamine $N$-oxide ($\\text{Me}_3\\text{NO}$) cleanly oxidizes one CO ligand to $\\text{CO}_2$, generating the reactive solvated cluster $\\text{Os}_3(\\text{CO})_{11}(\\text{NCMe})$ under mild conditions."""
        },
        {
            "id": "sec7_4",
            "title": "§7.4 Tetranuclear Metal Carbonyl Clusters: $\\text{Co}_4$, $\\text{Rh}_4$, and $\\text{Ir}_4(\\text{CO})_{12}$",
            "content": """The Group 9 tetranuclear dodecacarbonyls $M_4(\\text{CO})_{12}$ ($M = \\text{Co, Rh, Ir}$) adopt tetrahedral geometries.

### Electron Counting and Metal-Metal Bonding:
- Cobalt, rhodium, and iridium are in Group 9 ($n_v = 9$):
  \\[ 4 \\times 9 = 36\\text{ metal valence electrons} \\]
- Twelve carbonyl ligands donate:
  \\[ 12 \\times 2 = 24\\text{ electrons} \\]
- Total Valence Electrons ($TVE$):
  \\[ TVE = 36 + 24 = \\mathbf{60\\text{ electrons}} \\]
- Number of localized $2c-2e$ metal-metal bonds ($m$):
  \\[ m = \\frac{18n - TVE}{2} = \\frac{18(4) - 60}{2} = \\frac{72 - 60}{2} = \\frac{12}{2} = \\mathbf{6\\text{ bonds}} \\]
- A four-vertex polyhedron with 6 edges is a **tetrahedron**. Each metal atom forms 3 metal-metal bonds and achieves an 18-electron valence shell:
  \\[ 9 (M) + 3 \\times 2 (\\text{terminal CO}) + 3 \\times 1 (M-M) = 18\\text{e} \\]

### Carbonyl Bridging Structural Isomerism:
Just as in the Group 8 trimetallic series, the Group 9 tetrametallic series displays a systematic shift in carbonyl bridging:
- **$\\text{Ir}_4(\\text{CO})_{12}$**: Adopts **$T_d$ symmetry** with **all 12 carbonyl ligands terminal** (three terminal CO per Ir atom).
- **$\\text{Co}_4(\\text{CO})_{12}$ and $\\text{Rh}_4(\\text{CO})_{12}$**: Adopt **$C_{3v}$ symmetry** featuring **three bridging $\\mu_2-\\text{CO}$ ligands** capping the three edges of the basal triangular face, and nine terminal CO ligands.
- **Physical Reason**: The smaller ionic radii of $\\text{Co}$ ($1.25$ Å) and $\\text{Rh}$ ($1.35$ Å) cannot accommodate twelve terminal carbonyls around a small tetrahedron without severe ligand-ligand repulsion."""
        },
        {
            "id": "sec7_5",
            "title": "§7.5 Wade's Rules & Polyhedral Skeletal Electron Pair Theory (PSEPT) for Boranes",
            "content": """In 1971, Kenneth Wade formulated the **Polyhedral Skeletal Electron Pair Theory (PSEPT)**, rationalizing the geometries of electron-deficient boron hydrides (boranes) and carboranes.

### Core Principles of Wade's Rules:
In a polyhedral cluster containing $n$ skeletal vertices:
1. Each vertex atom uses three valence orbitals for skeletal cluster bonding (one radial orbital pointing inward toward the cluster centroid, and two tangential orbitals tangential to the polyhedral surface).
2. The remaining valence orbital is directed outward as an exo-orbital (used for bonding to an exo-terminal ligand, e.g., $B-H$ or $M-L$).
3. The $n$ radial orbitals combine to yield **1 bonding orbital** (totally symmetric $a_{1g}$) and $n-1$ antibonding orbitals.
4. The $2n$ tangential orbitals combine to yield **$n$ bonding orbitals** and $n$ antibonding orbitals.
5. Consequently, any closed deltahedral cage with $n$ vertices possesses exactly **$n + 1$ skeletal bonding molecular orbitals**.

### Skeletal Electron Pair (SEP) Counting:
- A closed deltahedron (a polyhedron whose faces are all triangles) requires **$n + 1$ Skeletal Electron Pairs (SEPs)** ($2n + 2$ skeletal electrons):
  \\[ \\mathbf{\\text{Closo Framework}}: \\quad n \\text{ vertices, } n + 1 \\text{ SEPs } (2n + 2\\text{ electrons}) \\]
- Removing one vertex from a closo parent polyhedron generates a **Nido** cage:
  \\[ \\mathbf{\\text{Nido Framework}}: \\quad n \\text{ vertices, } n + 2 \\text{ SEPs } (2n + 4\\text{ electrons}) \\]
- Removing two vertices from a closo parent generates an **Arachno** cage:
  \\[ \\mathbf{\\text{Arachno Framework}}: \\quad n \\text{ vertices, } n + 3 \\text{ SEPs } (2n + 6\\text{ electrons}) \\]
- Removing three vertices generates a **Hypho** cage:
  \\[ \\mathbf{\\text{Hypho Framework}}: \\quad n \\text{ vertices, } n + 4 \\text{ SEPs } (2n + 8\\text{ electrons}) \\]
- Removing four vertices generates a **Klado** cage:
  \\[ \\mathbf{\\text{Klado Framework}}: \\quad n \\text{ vertices, } n + 5 \\text{ SEPs } (2n + 10\\text{ electrons}) \\]"""
        },
        {
            "id": "sec7_6",
            "title": "§7.6 The Mingos Extension of PSEPT to Transition Metal Clusters",
            "content": """In 1972, D. Michael P. Mingos extended Wade's rules to transition metal carbonyl clusters. 

### Transition Metal Fragment Skeletal Electron Contributions:
A transition metal atom has 9 valence orbitals (one $s$, three $p$, five $d$).
- To bond in a cluster, a metal fragment $M L_k$ reserves **6 valence orbitals** for its own non-bonding core and coordination to exo-ligands:
  - 3 $t_{2g}$-like metal non-bonding $d$-orbitals (which hold 6 electrons).
  - 3 exo-bonding orbitals directed toward external ligands $L_k$.
- This leaves **3 orbitals** for skeletal cluster bonding (one radial, two tangential)—identical in symmetry to a main group $B-H$ or $C-H$ fragment!
- Consequently, the number of electrons donated by a transition metal fragment to the cluster skeletal bonding is:
  \\[ \\text{Skeletal Electrons per } M L_k \\text{ fragment} = v + x - 12 \\]
  where $v$ is the group number of the transition metal and $x$ is the total number of electrons donated by the attached ligands $L_k$.

### Total Skeletal Electron Pair Formula for Transition Metal Clusters:
For a transition metal cluster with $n$ vertices and Total Valence Electrons ($TVE$):
\\[ \\text{Total Skeletal Electrons } (TSE) = TVE - 12n \\]
\\[ \\text{Skeletal Electron Pairs } (SEP) = \\frac{TSE}{2} = \\frac{TVE - 12n}{2} \\]

### Classification Table:
| Framework Type | Skeletal Electron Pairs ($SEP$) | Total Valence Electrons ($TVE$) | Geometric Architecture |
| :--- | :--- | :--- | :--- |
| **Closo** | $n + 1$ | $14n + 2$ | Complete $n$-vertex deltahedron (octahedron, etc.) |
| **Nido** | $n + 2$ | $14n + 4$ | $n$-vertex cage missing 1 vertex from $(n+1)$ closo |
| **Arachno** | $n + 3$ | $14n + 6$ | $n$-vertex cage missing 2 vertices from $(n+2)$ closo |
| **Hypho** | $n + 4$ | $14n + 8$ | $n$-vertex cage missing 3 vertices from $(n+3)$ closo |"""
        },
        {
            "id": "sec7_7",
            "title": "§7.7 Capping Rules, Polyhedral Condensation Algorithms & High-Nuclearity Geometries",
            "content": """Beyond simple closo/nido/arachno polyhedra, complex transition metal clusters adopt condensed and capped structures governed by Mingos capping algorithms:

### 1. The Capping Principle:
- **Rule**: Capping a triangular face of a closo polyhedron adds **one vertex** without changing the number of skeletal electron pairs required by the parent cage:
  \\[ \\text{SEPs for a Capped Polyhedron} = \\text{SEPs of Parent Polyhedron} \\]
- A monocapped closo polyhedron with $n$ vertices has a parent closo cage with $n-1$ vertices. It requires $(n-1) + 1 = n$ SEPs.
- A bicapped closo polyhedron with $n$ vertices requires $(n-2) + 1 = n-1$ SEPs.
- **Example: Osmium Cluster $\\text{Os}_6(\\text{CO})_{18}$**:
  - $n = 6$ vertices.
  - $TVE = 6(8) + 18(2) = 48 + 36 = 84\\text{ electrons}$.
  - $SEP = (84 - 12 \\times 6)/2 = (84 - 72)/2 = 6\\text{ pairs}$.
  - For $n = 6$, $SEP = 6$ corresponds to $n$ pairs, which represents a **monocapped trigonal bipyramid** (parent closo trigonal bipyramid with $n-1=5$ vertices requiring $5+1=6$ SEPs).
  - In contrast, the octahedral cluster $[\\text{Ru}_6(\\text{CO})_{18}]^{2-}$ has $TVE = 86$, giving $SEP = (86-72)/2 = 7 = n+1$ pairs $\\implies$ **pure closo octahedron**!

### 2. Polyhedral Condensation:
When two polyhedral cages share a common vertex, edge, or face:
\\[ TVE(\\text{condensed}) = TVE(\\text{Cluster 1}) + TVE(\\text{Cluster 2}) - TVE(\\text{Shared Unit}) \\]
- Sharing a single metal vertex: subtract 18 electrons.
- Sharing a metal-metal edge ($M_2$): subtract 34 electrons.
- Sharing a triangular face ($M_3$): subtract 48 electrons."""
        },
        {
            "id": "sec7_8",
            "title": "§7.8 Roald Hoffmann's Isolobal Analogy: Bridging Organic and Organometallic Clusters",
            "content": """In 1976, Roald Hoffmann introduced the **isolobal analogy**, a unifying conceptual bridge connecting organic, inorganic, and organometallic chemistry (Nobel Prize in Chemistry, 1981).

### Rigorous Definition of Isolobality:
Two molecular fragments are defined as **isolobal** (symbolized by a two-headed arrow with a half-orbital: $\\longleftrightarrow$ with a lobe, or $\\def\\iso{\\longleftrightarrow\\hskip-1.1em\\circ\\hskip0.6em}\\iso$) if the number, symmetry properties, approximate energy, and spatial orientation of their frontier valence orbitals, and the number of electrons occupying them, are similar.

### The $18 - n$ vs. $8 - n$ Matching Rule:
A transition metal fragment $M L_k$ possessing $m$ valence electrons is isolobal to a main group fragment $A X_j$ possessing $p$ valence electrons if:
\\[ 18 - m = 8 - p \\]
where $18 - m$ is the electron deficiency of the metal fragment relative to the 18e rule, and $8 - p$ is the electron deficiency of the main group fragment relative to the octet rule.

### Master Isolobal Series:
1. **$d^7-M L_5$ Fragments $\\iso \\text{CH}_3$ (1 Frontier Orbital, 1 Electron)**:
   - Group 7: $\\text{Mn}(\\text{CO})_5$ ($17\\text{e}$, missing 1e)
   - Group 9: $\\text{Co}(\\text{CN})_5^{3-}$ ($17\\text{e}$)
   - Group 8: $Cp\\text{Fe}(\\text{CO})_2$ ($17\\text{e}$)
   - Main Group: $\\text{CH}_3^\\bullet$, $\\text{NH}_2^\\bullet$, $\\text{OH}^\\bullet$, $\\text{F}^\\bullet$
   - *Direct consequence*: Just as two $\\text{CH}_3$ radicals dimerize to ethane $\\text{H}_3\\text{C}-\\text{CH}_3$, two $\\text{Mn}(\\text{CO})_5$ fragments dimerize to $\\text{Mn}_2(\\text{CO})_{10}$, and mixed coupling yields $\\text{H}_3\\text{C}-\\text{Mn}(\\text{CO})_5$.

2. **$d^8-M L_4$ Fragments $\\iso \\text{CH}_2$ (2 Frontier Orbitals, 2 Electrons)**:
   - Group 8: $\\text{Fe}(\\text{CO})_4$ ($16\\text{e}$, missing 2e)
   - Group 6: $\\text{Cr}(\\text{CO})_5$? No: $\\text{Cr}(\\text{CO})_5$ is $d^6-ML_5 \\iso \\text{CH}_3^+$.
   - Group 9: $Cp\\text{Co}(\\text{CO})$ ($16\\text{e}$)
   - Main Group: $:CH_2$ (carbene), $:SiH_2$, $:NH$
   - *Direct consequence*: $\\text{Fe}_3(\\text{CO})_{12}$ can be conceptualized as cyclopropane $(\\text{CH}_2)_3$ where every $:CH_2$ is replaced by an isolobal $\\text{Fe}(\\text{CO})_4$ vertex!

3. **$d^9-M L_3$ Fragments $\\iso \\text{CH}$ (3 Frontier Orbitals, 3 Electrons)**:
   - Group 9: $\\text{Co}(\\text{CO})_3$ ($15\\text{e}$, missing 3e)
   - Group 8: $Cp\\text{Fe}$ ($13\\text{e}$)? $Cp\\text{Fe}$ is $d^7 \\iso CH$.
   - Group 6: $Cp\\text{Mo}(\\text{CO})_2$ ($15\\text{e}$)
   - Main Group: $\\equiv \\text{CH}$ (carbyne), $\\equiv \\text{P}$
   - *Direct consequence*: Tetrahedrane $(\\text{CH})_4$ is directly isolobal to $\\text{Co}_4(\\text{CO})_{12}$, wherein the four $\\text{CH}$ vertices are replaced by four $\\text{Co}(\\text{CO})_3$ units!"""
        }
    ]

    problems = [
        {
            "id": "prob7_1",
            "tier": "Foundational",
            "title": "Skeletal Electron Counting in Polyhedral Boranes Using Wade's Rules",
            "statement": "Determine the Skeletal Electron Pairs ($SEP$) and predict the polyhedral cage geometry for the following borane and carborane clusters using Wade's rules: (a) $[\\text{B}_6\\text{H}_6]^{2-}$, (b) $\\text{B}_5\\text{H}_9$, (c) $\\text{B}_4\\text{H}_{10}$, (d) $1,2-\\text{C}_2\\text{B}_{10}\\text{H}_{12}$ (*o*-carborane).",
            "solution": """**Line-by-Line Solution:**

**1. Wade's Counting Methodology for Boranes:**
- Each $B-H$ vertex contributes **2 skeletal electrons** (Boron has 3 valence electrons, 1 is used for the terminal exo-$B-H$ bond, leaving 2 for the cage).
- Each $C-H$ vertex contributes **3 skeletal electrons** (Carbon has 4 valence electrons, 1 is used for exo-$C-H$, leaving 3 for the cage).
- Each additional bridging hydrogen ($\\mu-\\text{H}$) contributes **1 skeletal electron**.
- Each negative charge adds **1 skeletal electron**.

**(a) $[\\text{B}_6\\text{H}_6]^{2-}$:**
- Number of vertices: $n = 6$.
- Six $B-H$ units: $6 \\times 2 = 12\\text{ electrons}$.
- Charge $-2$: $2\\text{ electrons}$.
- Total skeletal electrons ($TSE$): $12 + 2 = 14\\text{ electrons}$.
- Skeletal Electron Pairs ($SEP$):
  \\[ SEP = \\frac{14}{2} = 7 \\text{ pairs} = n + 1 \\]
- **Classification**: **Closo framework**.
- **Geometry**: Regular **Octahedron** (6 vertices, 8 triangular faces).

**(b) $\\text{B}_5\\text{H}_9$:**
- Number of vertices: $n = 5$.
- Five $B-H$ units: $5 \\times 2 = 10\\text{ electrons}$.
- Four bridging hydrogens ($4 \\times \\mu-\\text{H}$): $4 \\times 1 = 4\\text{ electrons}$.
- Total skeletal electrons: $10 + 4 = 14\\text{ electrons}$.
- Skeletal Electron Pairs:
  \\[ SEP = \\frac{14}{2} = 7 \\text{ pairs} = n + 2 \\]
- **Classification**: **Nido framework** (derived from a 6-vertex octahedral parent).
- **Geometry**: **Square Pyramid** (one vertex of octahedron missing; four bridging hydrogens span the open basal edges).

**(c) $\\text{B}_4\\text{H}_{10}$:**
- Number of vertices: $n = 4$.
- Four $B-H$ units: $4 \\times 2 = 8\\text{ electrons}$.
- Six bridging hydrogens (or 2 endo-H + 4 bridging-H): $6 \\times 1 = 6\\text{ electrons}$.
- Total skeletal electrons: $8 + 6 = 14\\text{ electrons}$.
- Skeletal Electron Pairs:
  \\[ SEP = \\frac{14}{2} = 7 \\text{ pairs} = n + 3 \\]
- **Classification**: **Arachno framework** (derived from a 6-vertex octahedral parent missing two vertices).
- **Geometry**: **Butterfly / puckered quadrilateral** cage.

**(d) $1,2-\\text{C}_2\\text{B}_{10}\\text{H}_{12}$ (*ortho*-carborane):**
- Number of vertices: $n = 12$ ($2\\text{C} + 10\\text{B}$).
- Two $C-H$ units: $2 \\times 3 = 6\\text{ electrons}$.
- Ten $B-H$ units: $10 \\times 2 = 20\\text{ electrons}$.
- Charge: $0$.
- Total skeletal electrons: $6 + 20 = 26\\text{ electrons}$.
- Skeletal Electron Pairs:
  \\[ SEP = \\frac{26}{2} = 13 \\text{ pairs} = n + 1 \\]
- **Classification**: **Closo framework**.
- **Geometry**: Regular **Icosahedron** (12 vertices, 20 triangular faces)."""
        },
        {
            "id": "prob7_2",
            "tier": "Foundational",
            "title": "Application of the Mingos PSEPT to Hexanuclear Metal Carbonyl Clusters",
            "statement": "For the following hexanuclear clusters: (a) $[\\text{Ru}_6(\\text{CO})_{18}]^{2-}$, (b) $\\text{Rh}_6(\\text{CO})_{16}$, (c) $\\text{Os}_6(\\text{CO})_{18}$. Calculate the total valence electron count ($TVE$), skeletal electron pairs ($SEP$), and predict their polyhedral cluster geometries.",
            "solution": """**Line-by-Line Solution:**

**(a) $[\\text{Ru}_6(\\text{CO})_{18}]^{2-}$:**
1. Number of vertices: $n = 6$.
2. Valence electron accounting:
   - Six Ru atoms (Group 8): $6 \\times 8 = 48\\text{ electrons}$.
   - Eighteen CO ligands: $18 \\times 2 = 36\\text{ electrons}$.
   - Charge $-2$: $2\\text{ electrons}$.
   \\[ TVE = 48 + 36 + 2 = \\mathbf{86\\text{ electrons}} \\]
3. Skeletal Electron Pairs ($SEP$):
   \\[ SEP = \\frac{TVE - 12n}{2} = \\frac{86 - 12(6)}{2} = \\frac{86 - 72}{2} = \\frac{14}{2} = \\mathbf{7\\text{ pairs}} \\]
4. Since $SEP = n + 1 = 6 + 1 = 7$:
- **Classification**: **Closo framework**.
- **Geometry**: Regular **Octahedron** ($O_h$ symmetry).

**(b) $\\text{Rh}_6(\\text{CO})_{16}$:**
1. Number of vertices: $n = 6$.
2. Valence electron accounting:
   - Six Rh atoms (Group 9): $6 \\times 9 = 54\\text{ electrons}$.
   - Sixteen CO ligands: $16 \\times 2 = 32\\text{ electrons}$.
   \\[ TVE = 54 + 32 = \\mathbf{86\\text{ electrons}} \\]
3. Skeletal Electron Pairs:
   \\[ SEP = \\frac{86 - 72}{2} = 7\\text{ pairs} = n + 1 \\]
- **Classification**: **Closo framework**.
- **Geometry**: Regular **Octahedron** ($O_h$ core with 4 face-capping $\\mu_3-\\text{CO}$ and 12 terminal CO ligands).

**(c) $\\text{Os}_6(\\text{CO})_{18}$:**
1. Number of vertices: $n = 6$.
2. Valence electron accounting:
   - Six Os atoms (Group 8): $6 \\times 8 = 48\\text{ electrons}$.
   - Eighteen CO ligands: $18 \\times 2 = 36\\text{ electrons}$.
   \\[ TVE = 48 + 36 = \\mathbf{84\\text{ electrons}} \\]
3. Skeletal Electron Pairs:
   \\[ SEP = \\frac{84 - 72}{2} = \\frac{12}{2} = \\mathbf{6\\text{ pairs}} \\]
4. For $n = 6$, $SEP = 6 = n$.
   According to the Mingos capping rule:
   - A cluster with $n$ vertices and $n$ SEPs is derived from a parent closo polyhedron with $n-1 = 5$ vertices (which requires $5+1 = 6$ SEPs) that has one triangular face capped by the 6th metal atom!
- **Classification**: **Capped Closo (Monocapped Trigonal Bipyramid)**."""
        },
        {
            "id": "prob7_3",
            "tier": "Foundational",
            "title": "Constructing Isolobal Fragments: Organic to Organometallic Analogies",
            "statement": "Identify the transition metal fragment containing only $\\text{CO}$ ligands that is isolobal to each of the following organic or main group fragments: (a) Methyl radical $\\text{CH}_3^\\bullet$, (b) Methylene carbene $:CH_2$, (c) Methylidyne carbyne $\\equiv \\text{CH}$, (d) Silicium fragment $:SiH_2$.",
            "solution": """**Line-by-Line Solution:**

**General Principle of the Isolobal Analogy:**
An organometallic fragment $M(\\text{CO})_k$ is isolobal to a main group fragment with electron deficiency $\\Delta n_e$ if:
\\[ 18 - VEC(M(\\text{CO})_k) = 8 - VEC(\\text{main group}) \\]

**(a) Methyl Radical $\\text{CH}_3^\\bullet$:**
- Valence electron count: Carbon has 4 valence electrons $+$ 3 from $H = 7$ electrons.
- Electron deficiency: $8 - 7 = \\mathbf{1\\text{ electron}}$ (1 frontier orbital with 1 electron).
- Required transition metal fragment valence count: $18 - 1 = \\mathbf{17\\text{ electrons}}$.
- Candidate: Manganese pentacarbonyl **$\\text{Mn}(\\text{CO})_5$**:
  - Manganese (Group 7): 7 electrons $+$ five CO ($5 \\times 2 = 10$) $= 17$ electrons.
  - Geometry: $C_{4v}$ pseudo-octahedral with one vacant coordination site pointing along the $z$-axis.
- **Isolobal Pair**: $\\mathbf{\\text{CH}_3 \\iso \\text{Mn}(\\text{CO})_5}$ (also $\\text{Re}(\\text{CO})_5, \\text{Co}(\\text{CO})_4$).

**(b) Methylene Carbene $:CH_2$:**
- Valence electron count: $4 + 2 = 6$ electrons.
- Electron deficiency: $8 - 6 = \\mathbf{2\\text{ electrons}}$ (2 frontier orbitals with 2 electrons).
- Required transition metal fragment valence count: $18 - 2 = \\mathbf{16\\text{ electrons}}$.
- Candidate: Iron tetracarbonyl **$\\text{Fe}(\\text{CO})_4$**:
  - Iron (Group 8): 8 electrons $+$ four CO ($4 \\times 2 = 8$) $= 16$ electrons.
  - Geometry: $C_{2v}$ disphenoidal fragment with two empty/singly occupied frontier orbitals pointing toward the equatorial coordination sites.
- **Isolobal Pair**: $\\mathbf{:CH_2 \\iso \\text{Fe}(\\text{CO})_4}$ (also $\\text{Ru}(\\text{CO})_4, \\text{Os}(\\text{CO})_4$).

**(c) Methylidyne Carbyne $\\equiv \\text{CH}$:**
- Valence electron count: $4 + 1 = 5$ electrons.
- Electron deficiency: $8 - 5 = \\mathbf{3\\text{ electrons}}$ (3 frontier orbitals with 3 electrons).
- Required transition metal fragment valence count: $18 - 3 = \\mathbf{15\\text{ electrons}}$.
- Candidate: Cobalt tricarbonyl **$\\text{Co}(\\text{CO})_3$**:
  - Cobalt (Group 9): 9 electrons $+$ three CO ($3 \\times 2 = 6$) $= 15$ electrons.
  - Geometry: $C_{3v}$ conical fragment with three hybrid frontier orbitals directed in a tripod.
- **Isolobal Pair**: $\\mathbf{\\equiv \\text{CH} \\iso \\text{Co}(\\text{CO})_3}$ (also $\\text{Rh}(\\text{CO})_3, \\text{Ir}(\\text{CO})_3$).

**(d) Silylene Fragment $:SiH_2$:**
- Silicon belongs to Group 14, identical in valence configuration to carbon: 6 valence electrons, missing 2 electrons.
- **Isolobal Pair**: $\\mathbf{:SiH_2 \\iso :CH_2 \\iso \\text{Fe}(\\text{CO})_4}$."""
        },
        {
            "id": "prob7_4",
            "tier": "Intermediate",
            "title": "Synthesis, Structure and Reactivity of Unsaturated $\\text{H}_2\\text{Os}_3(\\text{CO})_{10}$",
            "statement": "When $\\text{Os}_3(\\text{CO})_{12}$ is refluxed in octane under dihydrogen $\\text{H}_2$, dihydridotriosmium decacarbonyl $\\text{H}_2\\text{Os}_3(\\text{CO})_{10}$ is formed. (a) Calculate the total valence electron count ($TVE$) and explain why this complex is formally described as an 'electron-deficient unsaturated cluster'. (b) Describe the bridging hydride geometry and state the formal metal-metal bond order for all three $\\text{Os}-\\text{Os}$ edges. (c) The cluster reacts instantly at $25^\\circ\\text{C}$ with ethylene without requiring CO dissociation. Formulate the reaction equation and explain this exceptional reactivity.",
            "solution": """**Line-by-Line Solution:**

**(a) Total Valence Electron Count ($TVE$):**
1. Three osmium atoms (Group 8): $3 \\times 8 = 24\\text{ valence electrons}$.
2. Ten carbonyl ligands donate: $10 \\times 2 = 20\\text{ electrons}$.
3. Two hydride ligands donate: $2 \\times 1 = 2\\text{ electrons}$.
\\[ TVE = 24 + 20 + 2 = \\mathbf{46\\text{ electrons}} \\]
- A saturated trinuclear transition metal cluster obeying the 18e rule requires:
  \\[ TVE_\\text{sat} = 3 \\times 18 - 3(2) = 54 - 6 = 48\\text{ electrons} \\]
- $\\text{H}_2\\text{Os}_3(\\text{CO})_{10}$ possesses **46 valence electrons**—two electrons fewer than the saturated 48-electron requirement.
- It is therefore classified as an **electron-deficient (coordinatively unsaturated) cluster**, functioning as an inorganic/organometallic analog of an alkene!

**(b) Hydride Bridging Geometry and Metal-Metal Bond Orders:**
- Single-crystal neutron diffraction reveals:
  - Two of the $\\text{Os}-\\text{Os}$ edges are unbridged single bonds ($d(\\text{Os}-\\text{Os}) = 2.86$ Å, bond order $= 1$).
  - The third unique $\\text{Os}-\\text{Os}$ edge is bridged by both hydride ligands: $\\text{Os}(\\mu-\\text{H})_2\\text{Os}$.
  - This unique bridged $\\text{Os}-\\text{Os}$ distance is significantly shorter: **$2.68$ Å**.
- To satisfy the 18-electron rule for all three osmium centers:
  \\[ m = \\frac{18(3) - 46}{2} = \\frac{54 - 46}{2} = \\frac{8}{2} = \\mathbf{4\\text{ bonds}} \\]
- Across the three edges of the triangle, four metal-metal bonds must be partitioned:
  - Edge 1: 1 bond ($\text{Os}-\\text{Os}$)
  - Edge 2: 1 bond ($\text{Os}-\\text{Os}$)
  - Edge 3 (hydride-bridged): **formal metal-metal double bond ($\\text{Os}=\\text{Os}$)**!
- The two bridging hydrides participate in two 3-center 2-electron ($3c-2e$) $\\text{Os}-\\text{H}-\\text{Os}$ bonds across the formal double bond.

**(c) Instant Reaction with Ethylene at $25^\\circ\\text{C}$:**
1. In saturated 48-electron clusters (e.g., $\\text{Os}_3(\\text{CO})_{12}$), reaction with incoming ligands is strictly **dissociative**: it requires thermal or photochemical dissociation of a CO ligand ($E_a > 130\\text{ kJ/mol}$), requiring temperatures above $120^\\circ\\text{C}$.
2. Because $\\text{H}_2\\text{Os}_3(\\text{CO})_{10}$ has an accessible, low-lying LUMO associated with its $\\text{Os}=\\text{Os}$ double bond, incoming ethylene coordinates directly and **associatively** at room temperature without ligand loss:
   \\[ \\text{H}_2\\text{Os}_3(\\text{CO})_{10} + \\text{H}_2\\text{C}=\\text{CH}_2 \\longrightarrow \\text{H}\\text{Os}_3(\\mu-\\text{CH}_2\\text{CH}_3)(\\text{CO})_{10} \\]
3. Coordination is followed by rapid migratory insertion of ethylene into one of the bridging $\\text{Os}-\\text{H}$ bonds to yield a 48-electron saturated cluster containing a bridging ethyl group."""
        },
        {
            "id": "prob7_5",
            "tier": "Intermediate",
            "title": "Application of the Condensation Algorithm to High-Nuclearity Platinum Clusters",
            "statement": "The Chini cluster $[\\text{Pt}_3(\\text{CO})_6]_n^{2-}$ forms stacks of triangular $\\text{Pt}_3$ units. For the hexanuclear dianion $[\\text{Pt}_6(\\text{CO})_{12}]^{2-}$: (a) Determine the structure as two face-sharing or prismatically stacked $\\text{Pt}_3$ triangles. (b) Use the Mingos polyhedral condensation rule to calculate its theoretical $TVE$. (c) Compare the calculated value with the experimental electron count, and explain the physical basis of electron deficiency in platinum carbonyl clusters.",
            "solution": """**Line-by-Line Solution:**

**(a) Polyhedral Architecture:**
- The hexanuclear dianion $[\\text{Pt}_6(\\text{CO})_{12}]^{2-}$ consists of two parallel triangular $\\text{Pt}_3(\\text{CO})_6$ units stacked on top of each other in an eclipsed or staggered trigonal prismatic orientation ($D_{3h}$ or $D_{3d}$ symmetry), bound by three inter-layer $\\text{Pt}-\\text{Pt}$ bonds.

**(b) Mingos Polyhedral Condensation Calculation:**
1. Each triangular $\\text{Pt}_3$ unit possesses:
   \\[ 3 \\times \\text{Pt} (d^{10}) + 6 \\times \\text{CO} (2\\text{e}) + \\text{charge contribution} \\]
2. For an isolated triangular cluster obeying the 18e rule: $TVE = 3(18) - 3(2) = 48\\text{ electrons}$.
3. When two clusters condense by face-to-face interaction across an entire triangular $M_3$ face:
   \\[ TVE(\\text{condensed}) = TVE_1 + TVE_2 - TVE(\\text{shared interface}) \\]
4. However, in $[\\text{Pt}_6(\\text{CO})_{12}]^{2-}$, the two $\\text{Pt}_3$ layers are connected by three inter-layer bonds rather than complete vertex fusion.
   Under the general formula for stacked trigonal prismatic clusters:
   \\[ TVE = 42n + 2 \\quad (\\text{for } n \\text{ stacked layers}) \\]
   For $n = 2$ layers:
   \\[ TVE = 42(2) + 2 = \\mathbf{86\\text{ electrons}} \\]

**(c) Comparison with Experimental Electron Count:**
1. Let us compute the experimental valence electron count:
   - Six platinum atoms (Group 10): $6 \\times 10 = 60\\text{ electrons}$.
   - Twelve carbonyl ligands: $12 \\times 2 = 24\\text{ electrons}$.
   - Charge dianion $-2$: $2\\text{ electrons}$.
   \\[ TVE_\\text{exp} = 60 + 24 + 2 = \\mathbf{86\\text{ electrons}} \\]
2. The experimental count matches the predicted value of **86 electrons**.
3. **Physical Origin of Electron Deficiency**:
   - In late transition metal clusters ($\text{Pt}, \\text{Au}$), platinum favors square planar 16-electron coordination ($5d^8-5d^{10}$).
   - The empty $6p_z$ orbitals on platinum remain high in energy and do not participate in skeletal bonding, reducing the required electron count per triangle from 48 down to 42 electrons ($3 \\times 16 - 3(2) = 42$).
   - This confers exceptional stability to infinite one-dimensional molecular 'wires' formed by $[\\text{Pt}_3(\\text{CO})_6]_n^{2-}$ stacks."""
        },
        {
            "id": "prob7_6",
            "tier": "Intermediate",
            "title": "Skeletal Electron Counting in Heteroboranes and Metallaboranes",
            "statement": "The metallaborane complex $[(\\eta^5-\\text{C}_5\\text{H}_5)\\text{Co}\\text{B}_4\\text{H}_8]$ contains four boron atoms and one cobalt atom. (a) Determine the skeletal electron contribution of the $Cp\\text{Co}$ fragment. (b) Calculate the total skeletal electron pairs ($SEP$) of the cluster. (c) Predict its polyhedral cage geometry using Wade's rules.",
            "solution": """**Line-by-Line Solution:**

**(a) Skeletal Contribution of the $Cp\\text{Co}$ Fragment:**
1. Cobalt is in Group 9 ($n_v = 9$).
2. Cyclopentadienyl ($Cp$) donates 5 electrons in the neutral model.
3. Total valence electrons in the $Cp\\text{Co}$ fragment:
   \\[ VEC(Cp\\text{Co}) = 9 + 5 = 14\\text{ electrons} \\]
4. According to the Mingos formula, the skeletal electron contribution of a transition metal fragment is:
   \\[ \\text{Skeletal Electrons} = VEC - 12 = 14 - 12 = \\mathbf{2\\text{ electrons}} \\]
- Thus, the $Cp\\text{Co}$ fragment contributes **2 skeletal electrons**, making it strictly isolobal to a $B-H$ vertex ($3 - 1 = 2\\text{e}$)!

**(b) Total Skeletal Electron Pairs ($SEP$):**
- Number of cluster vertices: $n = 1 (\\text{Co}) + 4 (\\text{B}) = 5\\text{ vertices}$.
- One $Cp\\text{Co}$ vertex: $2\\text{ electrons}$.
- Four $B-H$ vertices: $4 \\times 2 = 8\\text{ electrons}$.
- Four bridging hydrogens ($4 \\times \\mu-\\text{H}$): $4 \\times 1 = 4\\text{ electrons}$.
- Total skeletal electrons ($TSE$):
  \\[ TSE = 2 + 8 + 4 = 14\\text{ electrons} \\]
- Skeletal Electron Pairs ($SEP$):
  \\[ SEP = \\frac{14}{2} = \\mathbf{7\\text{ pairs}} \\]

**(c) Polyhedral Geometry Prediction:**
1. Total vertices $n = 5$.
2. Number of SEPs $= 7$.
3. Since $SEP = n + 2$ ($7 = 5 + 2$):
- **Classification**: **Nido framework**.
- **Parent Polyhedron**: 6-vertex Octahedron ($SEP = 6 + 1 = 7$).
- **Cluster Geometry**: **Square Pyramid** (missing one apex of an octahedron).
- The cobalt atom occupies the apex or a basal position, with the four bridging hydrogens situated around the open basal perimeter, directly matching the geometry of pentaborane(9) $\\text{B}_5\\text{H}_9$."""
        },
        {
            "id": "prob7_7",
            "tier": "Advanced",
            "title": "Molecular Orbital Proof of the $n+1$ Skeletal Electron Pair Rule in Octahedral Clusters",
            "statement": "Derive from first principles the molecular orbital secular determinant for an octahedral $M_6$ cluster using three basis orbitals per vertex (one radial $r$, two tangential $t_1, t_2$). Prove that the cluster generates exactly $n + 1 = 7$ bonding molecular orbitals and $2n - 1 = 11$ antibonding molecular orbitals.",
            "solution": """**Line-by-Line Solution:**

**1. Basis Orbitals and Symmetry Representation in $O_h$:**
Let the six metal vertices occupy the vertices of a regular octahedron ($n = 6$).
Each vertex provides:
- One radial orbital ($r$) pointing toward the cluster centroid ($r$-basis).
- Two mutually perpendicular tangential orbitals ($t_x, t_y$) lying on the polyhedral surface ($t$-basis).

**2. Radial Orbital Manifold:**
The six radial orbitals transform under $O_h$ point group symmetry as:
\\[ \\Gamma_r = A_{1g} + E_g + T_{1u} \\]
- **$A_{1g}$ MO (Totally Symmetric)**:
  All six radial lobes point inward with identical positive phases:
  \\[ \\psi(A_{1g}) = \\frac{1}{\\sqrt{6}} \\sum_{i=1}^6 r_i \\]
  This orbital exhibits purely constructive, in-phase bonding overlap in the interior of the cage. It is **strongly bonding** with energy:
  \\[ E(A_{1g}) = \\alpha_r + 4\\beta_{rr} \\]
- **$T_{1u}$ and $E_g$ MOs**:
  These combinations possess nodal planes passing through the cluster centroid. Their overlap within the cage is destructive, rendering them antibonding or non-bonding with respect to the core.

**3. Tangential Orbital Manifold:**
The twelve tangential orbitals transform under $O_h$ as:
\\[ \\Gamma_t = T_{1g} + T_{2g} + T_{1u} + T_{2u} \\]
- On the surface of the octahedron, adjacent tangential orbitals overlap in a $\\sigma$- and $\\pi$-fashion along the twelve edges.
- Group theory and Hückel matrix diagonalization reveal:
  - **$T_{1u}$ Tangential MOs**: Threefold degenerate bonding combinations that match the symmetry of the radial $T_{1u}$ set. Mixing between radial and tangential $T_{1u}$ orbitals yields **3 strongly bonding MOs**.
  - **$T_{2g}$ Tangential MOs**: Threefold degenerate bonding combinations with strong in-phase overlap along octahedral edges, yielding **3 strongly bonding MOs**.
  - The remaining tangential combinations ($T_{1g}, T_{2u}$) are strictly antibonding on the surface.

**4. Summation of Bonding MOs:**
Summing all bonding representations:
\\[ \\text{Bonding MOs} = 1\\,(A_{1g}) + 3\\,(T_{1u}) + 3\\,(T_{2g}) = \\mathbf{7\\text{ bonding MOs}} \\]
For an $n$-vertex deltahedron with $n = 6$:
\\[ n + 1 = 6 + 1 = \\mathbf{7\\text{ Skeletal Bonding MOs}} \\]

**5. Total Orbital Accounting:**
- Total basis orbitals: $3n = 3(6) = 18$ orbitals.
- Number of bonding MOs: $n + 1 = 7$.
- Number of antibonding/non-bonding MOs: $18 - 7 = 11 = 2n - 1$.
- To achieve maximum thermodynamic stability without populating antibonding levels, the cluster must host exactly:
  \\[ 2 \\times (n + 1) = 2(7) = \\mathbf{14\\text{ skeletal electrons (7 Skeletal Electron Pairs)}} \\]
- Adding $12n = 72$ electrons for the localized core and exo-bonds yields:
  \\[ TVE = 72 + 14 = \\mathbf{86\\text{ valence electrons}} \\]
  proving Mingos's theorem for closo octahedral clusters."""
        },
        {
            "id": "prob7_8",
            "tier": "Advanced",
            "title": "Cluster Electron Counting in Carbido and Interstitial Heteroatom Clusters",
            "statement": "The octahedral ruthenium cluster $[\\text{Ru}_6\\text{C}(\\text{CO})_{16}]^{2-}$ encapsulates an interstitial carbon atom at the center of the $\\text{Ru}_6$ octahedron. (a) State the electron contribution of the interstitial carbon atom. (b) Calculate the $TVE$ and $SEP$ of the cluster, and confirm whether it satisfies Wade-Mingos rules. (c) Explain using molecular orbital theory how encapsulation of a main-group atom stabilizes the cluster framework.",
            "solution": """**Line-by-Line Solution:**

**(a) Electron Contribution of Interstitial Carbon:**
- An interstitial heteroatom encapsulated inside a metal cluster cavity donates **all of its valence electrons** into the skeletal bonding manifold of the surrounding metal cage.
- Carbon has atomic number 6 with valence configuration $2s^2 2p^2$.
- The interstitial carbon atom donates **4 electrons** ($E = 4$).

**(b) Valence Electron Count and Skeletal Pair Calculation:**
1. Six ruthenium atoms (Group 8): $6 \\times 8 = 48\\text{ electrons}$.
2. Sixteen carbonyl ligands: $16 \\times 2 = 32\\text{ electrons}$.
3. One interstitial carbon atom: $4\\text{ electrons}$.
4. Dianion charge $-2$: $2\\text{ electrons}$.
\\[ TVE = 48 + 32 + 4 + 2 = \\mathbf{86\\text{ electrons}} \\]
2. Total Skeletal Electrons ($TSE$):
   \\[ TSE = TVE - 12n = 86 - 12(6) = 86 - 72 = 14\\text{ electrons} \\]
3. Skeletal Electron Pairs ($SEP$):
   \\[ SEP = \\frac{14}{2} = \\mathbf{7\\text{ pairs}} = n + 1 \\]
- **Conclusion**: The cluster has $n = 6$ vertices and $n+1 = 7$ SEPs, precisely satisfying Wade's rule for a **closo octahedron**.

**(c) Molecular Orbital Stabilization by Interstitial Encapsulation:**
1. In an empty $M_6$ octahedron, the radial $A_{1g}$ bonding orbital is centered at the cluster centroid, while the threefold degenerate radial $T_{1u}$ orbitals have nodes at the center with lobes pointing inward.
2. The interstitial carbon atom sits precisely at the centroid:
   - Its spherically symmetric $2s$ orbital has $A_{1g}$ symmetry, perfectly matching the cluster $A_{1g}$ radial MO.
   - Its three orthogonal $2p_x, 2p_y, 2p_z$ orbitals have $T_{1u}$ symmetry, perfectly matching the cluster $T_{1u}$ radial MOs!
3. Strong covalent mixing occurs:
   \\[ \\langle 2s_C | \\psi(A_{1g})_M \\rangle > 0, \\quad \\langle 2p_C | \\psi(T_{1u})_M \\rangle > 0 \\]
4. This interaction lowers the energies of both the $A_{1g}$ and $T_{1u}$ skeletal bonding MOs by $>200\\text{ kJ/mol}$, pulling the metal atoms closer together and compressing the cage.
5. Consequently, carbido-clusters exhibit vastly enhanced thermal and chemical stability compared to empty analogs, resisting cluster fragmentation during catalysis."""
        },
        {
            "id": "prob7_9",
            "tier": "Advanced",
            "title": "Thermodynamics and Fragmentation Kinetics of Tetranuclear Carbonyls",
            "statement": "The thermal decomposition of dodecacarbonyltetracobalt $\\text{Co}_4(\\text{CO})_{12}$ to octacarbonyldicobalt $\\text{Co}_2(\\text{CO})_8$ under carbon monoxide pressure follows the equilibrium: $\\text{Co}_4(\\text{CO})_{12} + 4\\,\\text{CO} \\rightleftharpoons 2\\,\\text{Co}_2(\\text{CO})_8$. (a) Given standard enthalpy $\\Delta H^\\circ = +54.8\\text{ kJ/mol}$ and standard entropy $\\Delta S^\\circ = +142\\text{ J/(mol}\\cdot\\text{K)}$, calculate the equilibrium constant $K_p$ at $350\\text{ K}$ and $450\\text{ K}$. (b) Calculate the partial pressure of CO required to maintain a $50\\%$ conversion of $\\text{Co}_4$ to $\\text{Co}_2$ at $400\\text{ K}$. (c) Connect this equilibrium to the active catalyst resting state in the industrial hydroformylation of 1-alkenes.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of Equilibrium Constant $K_p$ at $350\\text{ K}$ and $450\\text{ K}$:**
The equilibrium expression is:
\\[ K_p = \\frac{P(\\text{Co}_2(\\text{CO})_8)^2}{P(\\text{Co}_4(\\text{CO})_{12}) \\cdot P(\\text{CO})^4} \\]
The standard Gibbs free energy change is:
\\[ \\Delta G^\\circ(T) = \\Delta H^\\circ - T\\Delta S^\\circ \\]

1. **At $T_1 = 350\\text{ K}$**:
   \\[ \\Delta G^\\circ(350) = 54,800 - (350)(142) = 54,800 - 49,700 = +5,100\\text{ J/mol} \\]
   \\[ K_p(350) = \\exp\\left(-\\frac{5,100}{(8.3145)(350)}\\right) = \\exp(-1.7525) \\approx \\mathbf{0.173\\text{ bar}^{-3}} \\]

2. **At $T_2 = 450\\text{ K}$**:
   \\[ \\Delta G^\\circ(450) = 54,800 - (450)(142) = 54,800 - 63,900 = -9,100\\text{ J/mol} \\]
   \\[ K_p(450) = \\exp\\left(-\\frac{-9,100}{(8.3145)(450)}\\right) = \\exp(+2.432) \\approx \\mathbf{11.38\\text{ bar}^{-3}} \\]

**(b) Partial Pressure of CO at $50\\%$ Conversion at $400\\text{ K}$:**
1. At $T = 400\\text{ K}$:
   \\[ \\Delta G^\\circ(400) = 54,800 - (400)(142) = 54,800 - 56,800 = -2,000\\text{ J/mol} \\]
   \\[ K_p(400) = \\exp\\left(-\\frac{-2,000}{(8.3145)(400)}\\right) = \\exp(+0.6014) \\approx 1.825\\text{ bar}^{-3} \\]
2. At $50\\%$ molar conversion, let $P(\\text{Co}_4) = 1.0\\text{ bar}$, then $P(\\text{Co}_2) = 2.0\\text{ bar}$:
   \\[ K_p = \\frac{(2.0)^2}{(1.0) \\cdot P(\\text{CO})^4} = \\frac{4.0}{P(\\text{CO})^4} = 1.825 \\]
3. Solve for $P(\\text{CO})$:
   \\[ P(\\text{CO})^4 = \\frac{4.0}{1.825} \\approx 2.192 \\]
   \\[ P(\\text{CO}) = (2.192)^{1/4} \\approx \\mathbf{1.22\\text{ bar}} \\]

**(c) Relevance to Industrial Hydroformylation:**
- In the industrial high-pressure oxo process for olefin hydroformylation (operating at $140-180^\\circ\\text{C}$ and $200-300\\text{ bar}$ of syngas $\\text{CO}/\\text{H}_2$), the active catalytic species is the mononuclear hydride $\\text{HCo}(\\text{CO})_4$.
- At lower CO pressures or elevated temperatures, $\\text{Co}_2(\\text{CO})_8$ dissociates and condenses to the inactive tetranuclear cluster $\\text{Co}_4(\\text{CO})_{12}$, which eventually deposits metallic cobalt on reactor walls.
- Maintaining a high partial pressure of carbon monoxide ($P(\\text{CO}) > 100\\text{ bar}$) pushes the equilibrium toward $\\text{Co}_2(\\text{CO})_8$, which subsequently hydrogenates to the active monomeric catalyst $\\text{HCo}(\\text{CO})_4$, ensuring catalyst longevity and high turnover frequency."""
        }
    ]

    return {
        "unit_number": 7,
        "title": "Metal Clusters & Wade-Mingos Electron Counting Rules",
        "description": "Definition and classification of metal clusters, low- vs high-nuclearity systems, trimetallic dodecacarbonyls Fe3, Ru3, Os3 synthesis, structures, and carbonyl isomerism, cluster fragmentation vs substitution, unsaturated clusters H2Os3(CO)10, tetranuclear M4(CO)12 clusters, Wade's rules for polyhedral boranes, Mingos extension of PSEPT to transition metals, capping and condensation algorithms, and Roald Hoffmann's isolobal analogy.",
        "sections": sections,
        "problems": problems
    }
