import json

def get_unit_6():
    u6 = {
        "id": "unit-6",
        "number": 6,
        "title": "Complex & Layered Ionic Topologies",
        "leadSummary": "Higher-order structural topologies: rutile (TiO2), nickel arsenide (NiAs), cadmium halides (CdI2/CdCl2), perovskites (ABO3), spinels (AB2O4), 2D van der Waals materials, intercalation compounds (LiCoO2, GICs), and microporous frameworks (zeolites and MOFs).",
        "simulations": ["sim_ssc_perovskite_spinel_architectures"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Rutile (TiO2) Structure: Edge-Sharing and Corner-Sharing Octahedra",
                "content": r"""The **rutile** ($\\text{TiO}_2$) archetype is the predominant crystal structure for $1:2$ stoichiometric compounds where the cation-to-anion radius ratio ($0.414 < r^+/r^- < 0.732$) mandates octahedral coordination of the cation, rather than the 8-fold cubic coordination of fluorite.

### Crystallographic Lattice & Symmetry
- **Space Group**: $P4_2/mnm$ (No. 136), Pearson symbol $tP6$.
- **Crystal System**: Tetragonal ($a = b \\ne c, \\alpha = \\beta = \\gamma = 90^\\circ$).
- **Formula Units per Cell**: $Z = 2$ $\\text{TiO}_2$ units.
- **Wyckoff Coordinates**:
  - $\\text{Ti}^{4+}$ at site $2a$: $(0, 0, 0)$ and $\\left(\\frac{1}{2}, \\frac{1}{2}, \\frac{1}{2}\\right)$.
  - $\\text{O}^{2-}$ at site $4f$: $\\pm (u, u, 0)$ and $\\pm \\left(\\frac{1}{2} + u, \\frac{1}{2} - u, \\frac{1}{2}\\right)$, where the internal positional parameter $u \\approx 0.305$.

### Coordination Polyhedra & Topological Connectivity
- **Coordination Ratio**: **$6:3$ coordination**.
  - Each $\\text{Ti}^{4+}$ cation is coordinated by $6$ oxygen anions forming a distorted $[\\text{TiO}_6]$ octahedron (four equatorial bonds at $d_1 = 1.946\\text{ Å}$ and two apical bonds at $d_2 = 1.984\\text{ Å}$).
  - Each $\\text{O}^{2-}$ anion is coordinated by $3$ titanium cations in an approximately planar trigonal configuration ($CN = 3$).
- **Octahedral Chains**:
  - Parallel to the tetragonal $\\mathbf{c}$-axis, $[\\text{TiO}_6]$ octahedra share **opposing edges** to form linear 1D chains.
  - These infinite 1D edge-sharing chains are cross-linked in the $xy$-plane by sharing **corners (vertices)**.
- **Isostructural Materials**: Many transition metal dioxides and difluorides crystallize in the rutile archetype: $\\text{SnO}_2$ (cassiterite), $\\text{RuO}_2$ (metallic oxide catalyst), $\\text{IrO}_2$, $\\text{VO}_2$ (high-temperature metallic phase), $\\text{MgF}_2, \\text{MnF}_2, \\text{FeF}_2, \\text{CoF}_2, \\text{NiF}_2, \\text{ZnF}_2$."""
            },
            {
                "secNumber": "6.2",
                "title": "Nickel Arsenide (NiAs) Structure: HCP Anion Array & Metallic Bonding Tendencies",
                "content": r"""The **nickel arsenide** ($\\text{NiAs}$) prototype is a fundamental structure for compounds formed between transition metals and heavy group 15/16 pnictogens or chalcogenides (e.g., $\\text{NiAs}, \\text{FeS}, \\text{CoS}, \\text{NiS}, \\text{FeSe}, \\text{CrSb}$).

### Crystallographic Parameters
- **Space Group**: $P6_3/mmc$ (No. 194), Pearson symbol $hP4$.
- **Lattice Type**: Hexagonal ($a = b \\ne c, \\gamma = 120^\\circ$).
- **Formula Units per Cell**: $Z = 2$ formula units.
- **Wyckoff Sites**:
  - Anions ($\\text{As}$): Form an ideal **hexagonal close-packed (HCP)** array at site $2c$: $\\left(\\frac{1}{3}, \\frac{2}{3}, \\frac{1}{4}\\right)$ and $\\left(\\frac{2}{3}, \\frac{1}{3}, \\frac{3}{4}\\right)$.
  - Cations ($\\text{Ni}$): Occupy **all octahedral interstitial sites** at site $2a$: $(0, 0, 0)$ and $\\left(0, 0, \\frac{1}{2}\\right)$.

### Coordination Geometry: Octahedral vs Trigonal Prismatic
- **Cation Environment**: Each $\\text{Ni}$ atom is coordinated by $6\\text{ As}$ atoms at the vertices of a regular octahedron ($CN = 6$).
- **Anion Environment**: Each $\\text{As}$ atom is coordinated by $6\\text{ Ni}$ atoms arranged at the vertices of a **trigonal prism** ($CN = 6$).
- **Direct Cation-Cation Bonding**:
  Along the hexagonal $\\mathbf{c}$-axis, $[\text{NiAs}_6]$ octahedra share **opposing triangular faces**.
  This face-sharing forces adjacent $\\text{Ni}$ cations into close spatial proximity:
  \\[
  d_{\\text{Ni-Ni}} = \\frac{c}{2}
  \\]
  For typical transition metal arsenides, this cation-cation separation ($2.5 - 2.8\\text{ Å}$) is short enough to permit direct overlap of partially filled $d$-orbitals (specifically $d_{z^2}$ orbitals pointing along $\\mathbf{c}$). Consequently, compounds adopting the $\\text{NiAs}$ structure exhibit **metallic electrical conductivity, narrow band gaps, and Pauli paramagnetism or itinerant ferromagnetism**, rather than classical ionic insulator behavior."""
            },
            {
                "secNumber": "6.3",
                "title": "Cadmium Halide Layered Structures: CdI2 and CdCl2 with Van der Waals Gaps",
                "content": r"""When the polarization of the anion by a polarizing cation becomes substantial (Fajans' rules), 3D isotropic ionic bonding collapses into anisotropic **two-dimensional layered architectures**. The archetypes are cadmium iodide ($\\text{CdI}_2$) and cadmium chloride ($\\text{CdCl}_2$).

### Cadmium Iodide (CdI2) Structure: Hexagonal Layer Stacking
- **Space Group**: $P\\bar{3}m1$ (No. 164), Pearson symbol $hP3$.
- **Anion Arrangement**: Iodide ions form an **HCP** layer array ($\dots ABABAB \dots$).
- **Cation Filling**: Cadmium cations occupy **half of the octahedral voids**, but in an ordered layered fashion: all octahedral sites between alternating iodide sheets are filled, leaving every second inter-sheet gap completely vacant.
- **Layer Stacking Sequence**:
  \\[
  \\dots A-\\gamma-B \\quad [\\text{vdW gap}] \\quad A-\\gamma-B \\quad [\\text{vdW gap}] \\quad A-\\gamma-B \\dots
  \\]
  where $A, B$ are iodide layers and $\\gamma$ represents the cadmium layer.
  This produces three-atom-thick sandwich sheets of $\\text{I-Cd-I}$ held internally by strong covalent/ionic bonds, while adjacent sandwich sheets are held together purely by weak **London dispersion (van der Waals) forces**.

### Cadmium Chloride (CdCl2) Structure: Cubic Layer Stacking
- **Space Group**: $R\\bar{3}m$ (No. 166), Pearson symbol $hR3$.
- **Anion Arrangement**: Chloride ions form a **Cubic Close-Packed (CCP / FCC)** array ($\dots ABCABC \dots$).
- **Layer Stacking Sequence**:
  \\[
  \\dots A-\\gamma-B \\quad [\\text{gap}] \\quad C-\\alpha-A \\quad [\\text{gap}] \\quad B-\\beta-C \\dots
  \\]
  The fundamental individual sandwich layer ($\text{Cl-Cd-Cl}$) is identical to that in $\text{CdI}_2$, but the 3-layer rhombohedral repeat gives a 3-layer repeat cycle along $\mathbf{c}$."""
            },
            {
                "secNumber": "6.4",
                "title": "The Perovskite Architecture (ABO3): Cubic Framework, Tolerance Factor & Tilting",
                "content": r"""The **perovskite** archetype, named after the Russian mineralogist L. A. Perovski, possesses the general chemical formula $\\text{ABX}_3$ (where $\\text{A}$ is a large cation, $\\text{B}$ is a smaller octahedrally coordinated transition metal, and $\\text{X}$ is typically $\\text{O}^{2-}, \\text{F}^-$, or a halide). It is the most versatile structural family in solid-state chemistry, hosting ferroelectricity, piezoelectricity, colossal magnetoresistance, ionic conductivity, and high-temperature superconductivity.

### The Ideal Cubic Perovskite Lattice
- **Space Group**: $Pm\\bar{3}m$ (No. 221), Pearson symbol $cP5$.
- **Cubic Unit Cell Parameter**: $a \\approx 3.9 - 4.2\\text{ Å}$.
- **Wyckoff Coordinates**:
  - $\\text{A}$-cation at corner site $1a$: $(0, 0, 0)$.
  - $\\text{B}$-cation at body center site $1b$: $\\left(\\frac{1}{2}, \\frac{1}{2}, \\frac{1}{2}\\right)$.
  - $\\text{O}$-anions at edge center sites $3c$: $\\left(\\frac{1}{2}, 0, 0\\right), \\left(0, \\frac{1}{2}, 0\\right), \\left(0, 0, \\frac{1}{2}\\right)$.
Alternatively, with $\\text{B}$ at the origin: $\\text{B}$ at $(0,0,0)$, $\\text{A}$ at $(1/2, 1/2, 1/2)$, and $\\text{O}$ at face centers $(1/2, 1/2, 0)$.

### Coordination Polyhedra
- $\\text{B}$-site cation: Coordinated by $6$ oxygen anions forming a regular $[\\text{BO}_6]$ octahedron ($CN = 6$). The octahedra are connected exclusively by **sharing corners** in all three dimensions ($\text{B-O-B}$ bond angle $= 180^\\circ$).
- $\\text{A}$-site cation: Sits within the 12-coordinate cuboctahedral cavity created by eight surrounding $[\\text{BO}_6]$ octahedra ($CN = 12$).
- Oxygen anion: Coordinated by $2\\text{ B}$ cations (linear) and $4\\text{ A}$ cations.

### The Goldschmidt Tolerance Factor ($t$)
Victor Goldschmidt (1926) established the geometric stability criterion for perovskites based on rigid ionic spheres:
Contact along the cube edge gives:
\\[
a = 2(r_B + r_O)
\\]
Contact along the face diagonal for the 12-coordinate $\\text{A}$-site gives:
\\[
\\sqrt{2}a = 2(r_A + r_O) \\implies a = \\sqrt{2}(r_A + r_O)
\\]
Equating these two expressions:
\\[
2(r_B + r_O) = \\sqrt{2}(r_A + r_O) \\implies \\frac{r_A + r_O}{\\sqrt{2}(r_B + r_O)} = 1
\\]
The **Goldschmidt Tolerance Factor** $t$ is defined as:
\\[
t = \\frac{r_A + r_O}{\\sqrt{2}(r_B + r_O)}
\\]
- **$t > 1.0$ (Large A-site)**: Octahedra are compressed; stabilized by non-centrosymmetric ferroelectric distortions (e.g., tetragonal $\\text{BaTiO}_3$, $t \\approx 1.06$) or hexagonal stacking polymorphs ($\\text{BaNiO}_3$).
- **$0.90 \\le t \\le 1.00$**: Ideal cubic perovskite (e.g., $\\text{SrTiO}_3$, $t \\approx 1.002$).
- **$0.71 \\le t < 0.90$ (Small A-site)**: $\\text{A}$ is too small for the cavity. To optimize $\\text{A-O}$ bond lengths, $[\\text{BO}_6]$ octahedra undergo rigid cooperative rotations (**Glazer octahedral tilting**), lowering symmetry to orthorhombic ($Pbnm$) or rhombohedral ($R\\bar{3}c$), as in $\\text{GdFeO}_3$ ($t \\approx 0.81$).
- **$t < 0.71$**: Perovskite framework collapses into the ilmenite ($\\text{FeTiO}_3$) structure."""
            },
            {
                "secNumber": "6.5",
                "title": "Ferroelectricity and Piezoelectricity in Perovskites (BaTiO3, PZT)",
                "content": r"""Barium titanate ($\\text{BaTiO}_3$) is the quintessential perovskite ferroelectric. Above its Curie temperature ($T_C = 120^\\circ\\text{C}$), it exists as a centrosymmetric cubic paraelectric phase ($Pm\\bar{3}m$).

### The Displacive Ferroelectric Phase Transition
Upon cooling below $T_C = 120^\\circ\\text{C}$:
- The crystal undergoes a displacive phase transition from cubic to **tetragonal** ($P4mm$, non-centrosymmetric).
- The unit cell expands along $\\mathbf{c}$ and contracts along $\\mathbf{a}$ ($c/a \\approx 1.01$).
- The central $\\text{Ti}^{4+}$ cation shifts along the $+z$-axis by approximately $0.06\\text{ Å}$ relative to the oxygen octahedron, while the apical oxygen shifts slightly in the opposite direction.
- This spatial separation of positive and negative charge centers generates a macroscopic **spontaneous electric polarization** ($P_s \\approx 26\\text{ }\\mu\\text{C/cm}^2$).
- Upon further cooling, it transitions to an orthorhombic phase ($Amm2$ at $T < 5^\\circ\\text{C}$) and a rhombohedral phase ($R3m$ at $T < -90^\\circ\\text{C}$), where polarization directs along $[110]$ and $[111]$ respectively.

### Soft Phonon Mode Mechanism (Cochran Model)
The microscopic driver is a transverse optical (TO) lattice phonon mode that becomes dynamically unstable (**soft mode**):
\\[
\\omega_{\\text{TO}}^2(T) = A(T - T_C)
\\]
As $T \\to T_C^+$, the restoring force against titanium displacement softens to zero ($\\omega \\to 0$). The dynamic vibration freezes into a static structural displacement.

### Lead Zirconate Titanate (PZT) & The Morphotropic Phase Boundary
Solid solutions of $\\text{Pb}(\\text{Zr}_x\\text{Ti}_{1-x})\\text{O}_3$ (PZT) exhibit maximum piezoelectric coefficients ($d_{33} > 500\\text{ pC/N}$) near the **Morphotropic Phase Boundary (MPB)** at $x \\approx 0.52$. At this composition, tetragonal and rhombohedral phases coexist with nearly identical free energies, enabling effortless reorientation of ferroelectric domains under external electric fields."""
            },
            {
                "secNumber": "6.6",
                "title": "The Spinel Architecture (AB2O4): Normal vs Inverse Spinels and CFSE",
                "content": r"""The **spinel** archetype, based on the mineral $\\text{MgAl}_2\\text{O}_4$, is the structural foundation for magnetic ferrites ($\\text{Fe}_3\\text{O}_4$, $\\text{NiFe}_2\\text{O}_4$), battery cathode materials ($\\text{LiMn}_2\\text{O}_4$), and transparent conductors.

### Crystallographic Parameters
- **Space Group**: $Fd\\bar{3}m$ (No. 227), Pearson symbol $cF56$.
- **Formula**: $\\text{AB}_2\\text{O}_4$ ($Z = 8$ formula units per cubic unit cell, total 56 atoms: 32 oxygen, 8 A cations, 16 B cations).
- **Oxygen Framework**: 32 oxygen anions form an approximate **face-centered cubic (FCC)** close-packed lattice.
- An FCC unit cell of 32 oxygen anions contains:
  - $64$ tetrahedral ($T_d$) interstitial sites.
  - $32$ octahedral ($O_h$) interstitial sites.
- In the spinel structure, **$1/8$ of tetrahedral sites (8 sites)** and **$1/2$ of octahedral sites (16 sites)** are occupied by cations.

### Normal vs Inverse Spinels
The distribution of divalent cations ($A^{2+}$) and trivalent cations ($B^{3+}$) between tetrahedral and octahedral sites defines two structural extremes:

1. **Normal Spinel**:
   - $A^{2+}$ cations occupy tetrahedral sites: $[A]_{\\text{tet}}$.
   - $B^{3+}$ cations occupy octahedral sites: $[B_2]_{\\text{oct}}$.
   - Formula: $(A)[B_2]\\text{O}_4$.
   - Examples: $\\text{MgAl}_2\\text{O}_4, \\text{FeCr}_2\\text{O}_4, \\text{ZnFe}_2\\text{O}_4, \\text{Mn}_3\\text{O}_4$.

2. **Inverse Spinel**:
   - Tetrahedral sites are occupied by half of the $B^{3+}$ cations: $[B]_{\\text{tet}}$.
   - Octahedral sites are occupied randomly by all $A^{2+}$ cations and the remaining half of $B^{3+}$: $[A, B]_{\\text{oct}}$.
   - Formula: $(B)[A, B]\\text{O}_4$.
   - Examples: Magnetite $\\text{Fe}_3\\text{O}_4 = (\\text{Fe}^{3+})[\\text{Fe}^{2+}, \\text{Fe}^{3+}]\\text{O}_4$, $\\text{NiFe}_2\\text{O}_4, \\text{CoFe}_2\\text{O}_4, \\text{MgFe}_2\\text{O}_4$.

### Crystal Field Stabilization Energy (CFSE) & Inversion Parameter
The distribution is governed by the **Octahedral Site Stabilization Energy (OSSE)**:
\\[
\\text{OSSE} = \\text{CFSE}_{\\text{oct}} - \\text{CFSE}_{\\text{tet}}
\\]
- For $\\text{Fe}_3\\text{O}_4$: $\\text{Fe}^{3+}$ is high-spin $d^5$ ($t_{2g}^3 e_g^2$), so its $\\text{CFSE} = 0$ in both geometries. $\\text{Fe}^{2+}$ is high-spin $d^6$ ($t_{2g}^4 e_g^2$ with $\\text{CFSE}_{\\text{oct}} = 0.4\\Delta_o$, $\\text{CFSE}_{\\text{tet}} = 0.6\\Delta_t \\approx 0.27\\Delta_o$). Because $\\text{OSSE}(\\text{Fe}^{2+}) > 0$, $\\text{Fe}^{2+}$ preferentially occupies octahedral sites, driving $\\text{Fe}_3\\text{O}_4$ into an **inverse spinel**.
- For $\\text{FeCr}_2\\text{O}_4$: $\\text{Cr}^{3+}$ is $d^3$ ($t_{2g}^3$ with huge $\\text{CFSE}_{\\text{oct}} = 1.2\\Delta_o$). $\\text{Cr}^{3+}$ strongly prefers octahedral sites, forcing $\\text{Fe}^{2+}$ into tetrahedral sites $\\implies$ **normal spinel**."""
            },
            {
                "secNumber": "6.7",
                "title": "Two-Dimensional Layered Materials, Intercalation Chemistry & GICs",
                "content": r"""Layered materials feature strong in-plane covalent/ionic bonds and weak out-of-plane van der Waals interactions across empty 2D gaps (**van der Waals gaps**).

### Intercalation Chemistry
Intercalation is the reversible insertion of guest atomic or molecular species into the host van der Waals gap without disrupting the integrity of the host's 2D covalent network:
\\[
\\text{Host} + x\\text{ Guest} \\rightleftharpoons \\text{Guest}_x\\text{Host}
\\]
Topochemical intercalation is driven by:
1. **Host Reduction/Oxidation**: Electron transfer between guest (electron donor like $\\text{Li}, \\text{K}$) and host conduction bands.
2. **Steric Dilation**: Elastic expansion of the interlayer distance $c$ ($c$-axis swelling).

### Archetypal Intercalation Systems
1. **Graphite Intercalation Compounds (GICs)**:
   - Donor GICs: Insertion of alkali metals (e.g., potassium $\\text{KC}_8$, lithium $\\text{LiC}_6$).
   - Staging: GICs uniquely exhibit periodic **staging** phenomena, where guest layers are separated by a well-defined integer number $n$ of host graphene sheets (Stage 1: $\\dots G-K-G-K \\dots$; Stage 2: $\\dots G-G-K-G-G-K \\dots$).
2. **Lithium Cobalt Oxide (LiCoO2)**:
   - Formally adopts the layered $\\alpha\\text{-NaFeO}_2$ structure (ordered rock salt derivative, space group $R\\bar{3}m$).
   - Co and Li ions occupy alternating $(111)$ octahedral planes of an FCC oxygen array.
   - During charging of a lithium-ion battery, lithium deintercalates reversibly:
   \\[
   \\text{LiCoO}_2 \\rightleftharpoons \\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}^+ + x e^- \\quad (0 \\le x \\le 0.5)
   \\]
3. **Transition Metal Dichalcogenides (TMDs)**:
   - $\\text{MoS}_2, \\text{WS}_2, \\text{TiS}_2$: Semiconducting or metallic monolayers exfoliable down to single unit cell thickness, hosting 2D exciton physics."""
            },
            {
                "secNumber": "6.8",
                "title": "Zeolites and Metal-Organic Frameworks (MOFs): Microporous Topologies",
                "content": r"""Microporous crystalline materials possess permanent, three-dimensional, interconnected pore channels with pore diameters ranging from $0.3\\text{ nm}$ to $3.0\\text{ nm}$.

### Zeolites: Aluminosilicate Framework Topologies
Zeolites are crystalline, hydrated aluminosilicates with open three-dimensional frameworks constructed of corner-sharing $[\\text{SiO}_4]^{4-}$ and $[\\text{AlO}_4]^{5-}$ tetrahedra:
- **Löwenstein's Rule**: In aluminosilicate frameworks, $\\text{Al-O-Al}$ linkages are strictly forbidden; $[\\text{AlO}_4]$ tetrahedra must only link to $[\\text{SiO}_4]$ tetrahedra ($Si/Al \\ge 1.0$).
- **Charge Balancing**: Replacing neutral $[\\text{SiO}_4]^0$ with $[\\text{AlO}_4]^-$ introduces net negative framework charges that are balanced by extra-framework exchangeable cations ($\\text{Na}^+, \\text{K}^+, \\text{Ca}^{2+}, \\text{H}^+$) located inside the aqueous pore channels.
- **Molecular Sieving & Catalysis**: Pores have molecular dimensions (e.g., Linde Type A has $4.1\\text{ Å}$ windows, Faujasite/Zeolite Y has $7.4\\text{ Å}$ cages), enabling shape-selective hydrocarbon catalysis and water softening ion exchange.

### Metal-Organic Frameworks (MOFs)
MOFs are hybrid crystalline networks composed of metal ion or cluster nodes (Secondary Building Units, SBUs) bridged by polytopic organic linkers:
- **MOF-5 Prototype**: $\\text{Zn}_4\\text{O}(\\text{BDC})_3$ where $\\text{BDC} = 1,4\\text{-benzenedicarboxylate}$.
  - Node: An inorganic $\\text{Zn}_4\\text{O}$ tetrahedron where four $\\text{Zn}^{2+}$ share a central $\\mu_4$-oxo oxygen.
  - Linker: Linear ditopic terephthalate dianions linking the SBUs into a cubic net with primitive cell parameter $a = 25.88\\text{ Å}$.
- **Unprecedented Surface Area**: MOFs feature void volume fractions $> 80\\%$ and Brunauer-Emmett-Teller (BET) specific surface areas exceeding $7000\\text{ m}^2/\\text{g}$, finding critical applications in hydrogen storage, carbon capture, and toxic gas sequestration."""
            }
        ],
        "problems": [
            {
                "probNumber": "6.1",
                "title": "Goldschmidt Tolerance Factor and Octahedral Factor Calculations",
                "difficulty": "Foundational",
                "statement": "Using Shannon ionic radii: $r(\\text{O}^{2-}) = 1.40\\text{ Å}$, $r(\\text{Sr}^{2+}, CN=12) = 1.44\\text{ Å}$, $r(\\text{Ba}^{2+}, CN=12) = 1.61\\text{ Å}$, $r(\\text{Gd}^{3+}, CN=12) = 1.27\\text{ Å}$, $r(\\text{Ti}^{4+}, CN=6) = 0.605\\text{ Å}$, and $r(\\text{Fe}^{3+}, CN=6) = 0.645\\text{ Å}$.\\n(a) Compute the Goldschmidt tolerance factor $t$ and octahedral factor $R = r_B/r_O$ for $\\text{SrTiO}_3$, $\\text{BaTiO}_3$, and $\\text{GdFeO}_3$.\\n(b) Predict the crystal system and room-temperature structural distortion (ideal cubic, ferroelectric tetragonal, or tilted orthorhombic) for each compound.\\n(c) Explain why $\\text{SrTiO}_3$ remains cubic down to $105\\text{ K}$ while $\\text{BaTiO}_3$ distorts to a ferroelectric tetragonal phase at $393\\text{ K}$.",
                "solution": r"""### Step 1: Tolerance Factor Formula and Calculations
The Goldschmidt tolerance factor is:
\\[
t = \\frac{r_A + r_O}{\\sqrt{2}(r_B + r_O)}
\\]
The octahedral factor is:
\\[
R = \\frac{r_B}{r_O}
\\]

1. **For $\\text{SrTiO}_3$**:
   - $r_A + r_O = 1.44 + 1.40 = 2.84\\text{ Å}$
   - $r_B + r_O = 0.605 + 1.40 = 2.005\\text{ Å}$
   \\[
   t = \\frac{2.84}{\\sqrt{2}(2.005)} = \\frac{2.84}{2.8355} = 1.0016 \\approx 1.002
   \\]
   \\[
   R = \\frac{0.605}{1.40} = 0.4321
   \\]

2. **For $\\text{BaTiO}_3$**:
   - $r_A + r_O = 1.61 + 1.40 = 3.01\\text{ Å}$
   - $r_B + r_O = 0.605 + 1.40 = 2.005\\text{ Å}$
   \\[
   t = \\frac{3.01}{\\sqrt{2}(2.005)} = \\frac{3.01}{2.8355} = 1.0615 \\approx 1.062
   \\]
   \\[
   R = \\frac{0.605}{1.40} = 0.4321
   \\]

3. **For $\\text{GdFeO}_3$**:
   - $r_A + r_O = 1.27 + 1.40 = 2.67\\text{ Å}$
   - $r_B + r_O = 0.645 + 1.40 = 2.045\\text{ Å}$
   \\[
   t = \\frac{2.67}{\\sqrt{2}(2.045)} = \\frac{2.67}{2.8921} = 0.9232 \\approx 0.923
   \\]
   (Using 8-coordinate Gd radius $1.053\\text{ Å}$ gives $t = 0.81$).
   \\[
   R = \\frac{0.645}{1.40} = 0.4607
   \\]

### Step 2: Structural Predictions
- $\\text{SrTiO}_3$: $t = 1.002 \\approx 1.000$ and $R = 0.432 > 0.414$. Both cations fit their coordination polyhedra perfectly. **Predicted**: Ideal cubic perovskite ($Pm\\bar{3}m$).
- $\\text{BaTiO}_3$: $t = 1.062 > 1.0$. The $\\text{Ba}^{2+}$ cation is oversized, causing tension on the $\\text{Ti-O}$ bonds and rattling of $\\text{Ti}^{4+}$ in its octahedron. **Predicted**: Ferroelectric tetragonal distortion ($P4mm$).
- $\\text{GdFeO}_3$: $t \\approx 0.81 - 0.92 < 1.0$. The $\\text{Gd}^{3+}$ cation is too small for the 12-coordinate cuboctahedral cavity. The $[\\text{FeO}_6]$ octahedra must tilt and buckle to close down the cage around Gd. **Predicted**: Orthorhombic perovskite with tilted octahedra (space group $Pbnm$).

### Step 3: Phase Stability Discussion
In $\\text{SrTiO}_3$, $t$ is virtually unity, so the $\\text{Ti-O}$ bond length matches the equilibrium cavity size, maintaining cubic paraelectric symmetry at room temperature. In $\\text{BaTiO}_3$, the larger $\\text{Ba}^{2+}$ ion stretches the unit cell, leaving the $[\\text{TiO}_6]$ octahedron slightly dilated. To optimize $d\\text{-}p\\pi$ orbital hybridization (Jahn-Teller-like second-order effect), the $\\text{Ti}^{4+}$ ion displaces off-center toward one apical oxygen, stabilizing the tetragonal ferroelectric phase at room temperature."""
            },
            {
                "probNumber": "6.2",
                "title": "Spinel Cation Distribution Calculation using Octahedral Site Stabilization Energy (OSSE)",
                "difficulty": "Intermediate",
                "statement": "Determine the preferred cation distribution (Normal vs Inverse) for nickel ferrite ($\\text{NiFe}_2\\text{O}_4$) and magnetite ($\\text{Fe}_3\\text{O}_4$).\\n(a) Write the high-spin electronic configurations of $\\text{Fe}^{3+}$ ($d^5$), $\\text{Fe}^{2+}$ ($d^6$), and $\\text{Ni}^{2+}$ ($d^8$).\\n(b) Calculate the crystal field stabilization energy (CFSE) in octahedral ($O_h$) and tetrahedral ($T_d$) fields (assuming $\\Delta_t = \\frac{4}{9}\\Delta_o$).\\n(c) Compute the Octahedral Site Stabilization Energy (OSSE) for each ion in units of $\\Delta_o$ and deduce the structural ground state.",
                "solution": r"""### Step 1: High-Spin Electronic Configurations
Oxide ions are weak-field ligands, ensuring high-spin states:
1. $\\text{Fe}^{3+}$ ($3d^5$):
   - Octahedral ($O_h$): $t_{2g}^3 e_g^2$.
   - Tetrahedral ($T_d$): $e^2 t_2^3$.
2. $\\text{Fe}^{2+}$ ($3d^6$):
   - Octahedral ($O_h$): $t_{2g}^4 e_g^2$.
   - Tetrahedral ($T_d$): $e^3 t_2^3$.
3. $\\text{Ni}^{2+}$ ($3d^8$):
   - Octahedral ($O_h$): $t_{2g}^6 e_g^2$.
   - Tetrahedral ($T_d$): $e^4 t_2^4$.

### Step 2: CFSE Calculations
Recall that $\\text{CFSE}(O_h) = -0.4 n(t_{2g}) + 0.6 n(e_g)$ in units of $\\Delta_o$, and $\\text{CFSE}(T_d) = -0.6 n(e) + 0.4 n(t_2)$ in units of $\\Delta_t = \\frac{4}{9}\\Delta_o$.

1. **For $\\text{Fe}^{3+}$ ($d^5$)**:
   - $\\text{CFSE}(O_h) = [-0.4(3) + 0.6(2)]\\Delta_o = (-1.2 + 1.2)\\Delta_o = 0$
   - $\\text{CFSE}(T_d) = [-0.6(2) + 0.4(3)]\\Delta_t = (-1.2 + 1.2)\\Delta_t = 0$
   - $\\text{OSSE}(\\text{Fe}^{3+}) = 0 - 0 = 0$

2. **For $\\text{Fe}^{2+}$ ($d^6$)**:
   - $\\text{CFSE}(O_h) = [-0.4(4) + 0.6(2)]\\Delta_o = (-1.6 + 1.2)\\Delta_o = -0.400\\Delta_o$ (stabilization of $+0.400\\Delta_o$).
   - $\\text{CFSE}(T_d) = [-0.6(3) + 0.4(3)]\\Delta_t = (-1.8 + 1.2)\\Delta_t = -0.600\\Delta_t = -0.600\\left(\\frac{4}{9}\\Delta_o\\right) = -0.267\\Delta_o$.
   - $\\text{OSSE}(\\text{Fe}^{2+}) = 0.400\\Delta_o - 0.267\\Delta_o = +0.133\\Delta_o$

3. **For $\\text{Ni}^{2+}$ ($d^8$)**:
   - $\\text{CFSE}(O_h) = [-0.4(6) + 0.6(2)]\\Delta_o = (-2.4 + 1.2)\\Delta_o = -1.200\\Delta_o$ (stabilization of $+1.200\\Delta_o$).
   - $\\text{CFSE}(T_d) = [-0.6(4) + 0.4(4)]\\Delta_t = (-2.4 + 1.6)\\Delta_t = -0.800\\Delta_t = -0.800\\left(\\frac{4}{9}\\Delta_o\\right) = -0.356\\Delta_o$.
   - $\\text{OSSE}(\\text{Ni}^{2+}) = 1.200\\Delta_o - 0.356\\Delta_o = +0.844\\Delta_o$

### Step 3: Spinel Distribution Assignment
1. **For $\\text{Fe}_3\\text{O}_4$ ($(\\text{Fe}^{2+})(\\text{Fe}^{3+})_2\\text{O}_4$)**:
   $\\text{OSSE}(\\text{Fe}^{2+}) = +0.133\\Delta_o$ while $\\text{OSSE}(\\text{Fe}^{3+}) = 0$.
   $\\text{Fe}^{2+}$ has a stronger thermodynamic driving force to occupy octahedral sites than $\\text{Fe}^{3+}$.
   Therefore, $\\text{Fe}^{2+}$ enters octahedral sites, leaving half of $\\text{Fe}^{3+}$ in tetrahedral sites:
   \\[
   (\\text{Fe}^{3+})[\\text{Fe}^{2+}, \\text{Fe}^{3+}]\\text{O}_4 \\implies \\textbf{Inverse Spinel}
   \\]

2. **For $\\text{NiFe}_2\\text{O}_4$ ($(\\text{Ni}^{2+})(\\text{Fe}^{3+})_2\\text{O}_4$)**:
   $\\text{OSSE}(\\text{Ni}^{2+}) = +0.844\\Delta_o \\gg \\text{OSSE}(\\text{Fe}^{3+}) = 0$.
   $\\text{Ni}^{2+}$ has an overwhelmingly high preference for octahedral coordination ($d^8$ oct stability).
   Therefore, $\\text{Ni}^{2+}$ occupies octahedral sites exclusively:
   \\[
   (\\text{Fe}^{3+})[\\text{Ni}^{2+}, \\text{Fe}^{3+}]\\text{O}_4 \\implies \\textbf{Inverse Spinel}
   \\]"""
            },
            {
                "probNumber": "6.3",
                "title": "Rutile Structure: Geometric Analysis of the c/a Ratio and Internal Parameter u",
                "difficulty": "Intermediate",
                "statement": "In the rutile prototype ($\\text{TiO}_2$, tetragonal $P4_2/mnm$), experimental lattice parameters are $a = 4.593\\text{ Å}$, $c = 2.959\\text{ Å}$, and internal coordinate $u = 0.305$.\\n(a) Calculate the unit cell volume and theoretical crystal density ($M = 79.866\\text{ g/mol}$).\\n(b) Formulate the exact expressions for the equatorial and apical $\\text{Ti-O}$ bond lengths in terms of $a, c, u$, and compute both distances.\\n(c) Compute the percentage distortion of the $[\\text{TiO}_6]$ octahedron.",
                "solution": r"""### Step 1: Unit Cell Volume and Density
For rutile, $Z = 2$ formula units per tetragonal unit cell:
\\[
V_c = a^2 c = (4.593 \\times 10^{-8}\\text{ cm})^2 (2.959 \\times 10^{-8}\\text{ cm}) = (2.1096 \\times 10^{-15})(2.959 \\times 10^{-8}) = 6.2423 \\times 10^{-23}\\text{ cm}^3
\\]
Density:
\\[
\\rho = \\frac{2 \\times 79.866\\text{ g/mol}}{(6.02214 \\times 10^{23}\\text{ mol}^{-1})(6.2423 \\times 10^{-23}\\text{ cm}^3)} = \\frac{159.732}{37.592} = 4.249\\text{ g/cm}^3
\\]
(Matches experimental density $4.250\\text{ g/cm}^3$).

### Step 2: Derivation of $\\text{Ti-O}$ Bond Distances
Consider the titanium atom at $(0,0,0)$.
Surrounding oxygen atoms:
- Four equatorial oxygens lie in the $(110)$ family of planes at $\\pm(u, u, 0)$ and $\\pm(1-u, 1-u, 0)$ translated:
Displacement to $(u, u, 0)$:
\\[
d_{\\text{eq}} = \\sqrt{(ua)^2 + (ua)^2} = \\sqrt{2} u a
\\]
- Two apical oxygens lie at $\\left(\\frac{1}{2}-u, u-\\frac{1}{2}, \\frac{1}{2}\\right)$ with displacement:
\\[
d_{\\text{ap}} = \\sqrt{2\\left(\\frac{1}{2} - u\\right)^2 a^2 + \\left(\\frac{c}{2}\\right)^2}
\\]

Substitute $a = 4.593\\text{ Å}$, $c = 2.959\\text{ Å}$, $u = 0.305$:
1. Equatorial bond length:
\\[
d_{\\text{eq}} = \\sqrt{2}(0.305)(4.593\\text{ Å}) = 1.41421 \\times 1.4009 = 1.981\\text{ Å}
\\]
2. Apical bond length:
\\[
\\frac{1}{2} - u = 0.500 - 0.305 = 0.195
\\]
\\[
2(0.195)^2 a^2 = 2(0.038025)(4.593)^2 = 2(0.038025)(21.096) = 1.6044\\text{ Å}^2
\\]
\\[
\\left(\\frac{c}{2}\\right)^2 = \\left(\\frac{2.959}{2}\\right)^2 = (1.4795)^2 = 2.1889\\text{ Å}^2
\\]
\\[
d_{\\text{ap}} = \\sqrt{1.6044 + 2.1889} = \\sqrt{3.7933} = 1.948\\text{ Å}
\\]

### Step 3: Octahedral Distortion
The two bond lengths are:
- $d_{\\text{eq}} = 1.981\\text{ Å}$ (four bonds)
- $d_{\\text{ap}} = 1.948\\text{ Å}$ (two bonds)
The bond length difference is:
\\[
\\Delta d = 1.981 - 1.948 = 0.033\\text{ Å}
\\]
Percentage distortion:
\\[
\\frac{\\Delta d}{d_{\\text{avg}}} = \\frac{0.033}{(1.981 \\times 4 + 1.948 \\times 2)/6} = \\frac{0.033}{1.970} \\times 100\\% = 1.68\\%
\\]
The $[\\text{TiO}_6]$ octahedron undergoes a slight axial compression along apical axes due to edge-sharing constraints."""
            },
            {
                "probNumber": "6.4",
                "title": "Nickel Arsenide Cation-Cation Distance, d-Orbital Overlap, and Electrical Transport",
                "difficulty": "Intermediate",
                "statement": "Nickel arsenide ($\\text{NiAs}$) crystallizes in space group $P6_3/mmc$ with lattice parameters $a = 3.619\\text{ Å}$ and $c = 5.034\\text{ Å}$.\\n(a) Compute the unit cell volume and theoretical density ($M = 133.61\\text{ g/mol}$).\\n(b) Calculate the direct $\\text{Ni-Ni}$ cation-cation separation along the hexagonal $\\mathbf{c}$-axis and compare it to the interatomic distance in pure metallic nickel ($d_{\\text{Ni-Ni}}^{\\text{metal}} = 2.492\\text{ Å}$).\\n(c) Explain why this structural feature imparts metallic conductivity rather than Mott insulating behavior.",
                "solution": r"""### Step 1: Volume and Theoretical Density
For a hexagonal unit cell:
\\[
V_c = a^2 c \\sin(60^\\circ) = \\frac{\\sqrt{3}}{2} a^2 c
\\]
With $a = 3.619\\text{ Å}$ and $c = 5.034\\text{ Å}$:
\\[
a^2 = (3.619)^2 = 13.097\\text{ Å}^2
\\]
\\[
V_c = \\frac{\\sqrt{3}}{2} (13.097)(5.034) = 0.86603 \\times 65.931 = 57.098\\text{ Å}^3 = 5.7098 \\times 10^{-23}\\text{ cm}^3
\\]
Unit cell contains $Z = 2$ formula units:
\\[
\\rho = \\frac{2 \\times 133.61\\text{ g/mol}}{(6.02214 \\times 10^{23}\\text{ mol}^{-1})(5.7098 \\times 10^{-23}\\text{ cm}^3)} = \\frac{267.22}{34.385} = 7.771\\text{ g/cm}^3
\\]

### Step 2: Cation-Cation Separation
In $\\text{NiAs}$, $\\text{Ni}$ atoms occupy positions $(0,0,0)$ and $(0,0,1/2)$.
The nearest $\\text{Ni-Ni}$ distance along the face-sharing octahedral chain is:
\\[
d_{\\text{Ni-Ni}} = \\frac{c}{2} = \\frac{5.034\\text{ Å}}{2} = 2.517\\text{ Å}
\\]
In pure metallic nickel (FCC, $a = 3.524\\text{ Å}$):
\\[
d_{\\text{metal}} = \\frac{a}{\\sqrt{2}} = \\frac{3.524}{\\sqrt{2}} = 2.492\\text{ Å}
\\]
Comparison:
\\[
\\Delta d = 2.517 - 2.492 = +0.025\\text{ Å} \\quad (+1.0\\%)
\\]
The $\\text{Ni-Ni}$ distance in $\\text{NiAs}$ is virtually identical to that in pure nickel metal!

### Step 3: Physical Explanation of Transport Behavior
Because the octahedra share triangular faces perpendicular to $\\mathbf{c}$, the $\\text{Ni}$ atoms are forced into direct contact.
The $3d_{z^2}$ orbitals of adjacent $\\text{Ni}$ atoms point directly toward one another along $\\mathbf{c}$.
Because $d_{\\text{Ni-Ni}} = 2.517\\text{ Å}$ is less than the critical Goodenough distance ($R_c \\approx 2.9\\text{ Å}$), the direct $d$-$d$ transfer integral $t$ exceeds the on-site Coulomb repulsion energy $U$ ($W > U$).
Consequently, a broad, partially filled 1D $d$-band is formed along $\\mathbf{c}$, giving rise to **Pauli paramagnetism and metallic conductivity** rather than localized antiferromagnetic insulating behavior."""
            },
            {
                "probNumber": "6.5",
                "title": "Cadmium Iodide vs Cadmium Chloride Stacking Sequences and Polytypism",
                "difficulty": "Intermediate",
                "statement": "Cadmium iodide ($\\text{CdI}_2$) crystallizes in a 1T hexagonal polytype ($a = 4.24\\text{ Å}, c = 6.84\\text{ Å}$), while cadmium chloride ($\\text{CdCl}_2$) crystallizes in a 3R rhombohedral polytype ($a_{\\text{hex}} = 3.85\\text{ Å}, c_{\\text{hex}} = 17.46\\text{ Å}$).\\n(a) State the stacking sequence of anion and cation layers for both materials.\\n(b) Calculate the single sandwich layer thickness $t_{\\text{layer}}$ for both crystals.\\n(c) Explain why $\\text{CdI}_2$ exhibits extensive polytypism (hundreds of stacking modifications) while $\\text{CdCl}_2$ does not.",
                "solution": r"""### Step 1: Stacking Sequences
1. **$\\text{CdI}_2$ (1T polytype)**:
   - Anion packing: Hexagonal Close-Packed (HCP) $\\dots ABABAB \\dots$
   - Layer sequence:
   \\[
   (A - \\gamma - B) \\quad [\\text{van der Waals gap}] \\quad (A - \\gamma - B)
   \\]
   where uppercase letters ($A, B$) are iodide layers and greek letters ($\\gamma$) are cadmium layers.
   - Repeat period: $1$ sandwich layer per unit cell ($c = 6.84\\text{ Å}$).

2. **$\\text{CdCl}_2$ (3R polytype)**:
   - Anion packing: Cubic Close-Packed (CCP) $\\dots ABCABC \\dots$
   - Layer sequence:
   \\[
   (A - \\gamma - B) \\quad [\\text{vdW}] \\quad (C - \\alpha - A) \\quad [\\text{vdW}] \\quad (B - \\beta - C) \\dots
   \\]
   - Repeat period: $3$ sandwich layers per hexagonal unit cell ($c_{\\text{hex}} = 17.46\\text{ Å}$).

### Step 2: Single Sandwich Layer Thickness
1. **For $\\text{CdI}_2$**:
   Since $Z = 1$ sandwich layer per unit cell:
   \\[
   t_{\\text{layer}}(\\text{CdI}_2) = c = 6.84\\text{ Å}
   \\]

2. **For $\\text{CdCl}_2$**:
   Since there are $3$ sandwich layers in the hexagonal cell:
   \\[
   t_{\\text{layer}}(\\text{CdCl}_2) = \\frac{c_{\\text{hex}}}{3} = \\frac{17.46\\text{ Å}}{3} = 5.82\\text{ Å}
   \\]
   The larger layer thickness in $\\text{CdI}_2$ reflects the substantially larger ionic radius of iodide ($2.16\\text{ Å}$) compared to chloride ($1.81\\text{ Å}$).

### Step 3: Origin of Polytypism in $\\text{CdI}_2$
Polytypism is a special 1D polymorphism where identical 2D sheets stack in different periodic sequences along the normal direction.
- In $\\text{CdI}_2$, the highly polarizable iodide ions experience strong covalent polarization toward the cadmium plane. Across the van der Waals gap, iodide ions interact exclusively via very weak dispersion forces.
- The energy difference between hexagonal stacking ($\dots A\\gamma B \\cdot A\\gamma B \dots$) and cubic stacking variants ($\dots A\\gamma B \\cdot C\alpha A \dots$) is minuscule ($\\Delta E < 0.1\\text{ kJ/mol}$).
- Spiral growth around screw dislocations during crystal precipitation readily introduces random stacking faults that propagate indefinitely, creating over 200 distinct polytypes (e.g., 2H, 4H, 6H, 12R, 20H). In contrast, the less polarizable chloride ions in $\\text{CdCl}_2$ retain higher partial electrostatic charges that favor 3R close-packing."""
            },
            {
                "probNumber": "6.6",
                "title": "High-Temperature Superconducting Cuprate Perovskite Architecture",
                "difficulty": "Advanced",
                "statement": "The high-temperature superconductor $\\text{YBa}_2\\text{Cu}_3\\text{O}_7$ (YBCO, $T_c = 93\\text{ K}$) crystallizes in an oxygen-deficient triple-perovskite superstructure with orthorhombic parameters $a = 3.823\\text{ Å}$, $b = 3.886\\text{ Å}$, $c = 11.684\\text{ Å}$.\\n(a) Demonstrate that the $c$-axis is approximately three times the cubic perovskite cell parameter ($c \\approx 3a_{\\text{perov}}$).\\n(b) Describe the distribution of $\\text{Y}^{3+}$ and $\\text{Ba}^{2+}$ cations along $\\mathbf{c}$ and explain why the $\\text{Y}$ layer is completely devoid of oxygen.\\n(c) Calculate the formal copper oxidation states in fully oxygenated $\\text{YBa}_2\\text{Cu}_3\\text{O}_7$ and reduced insulating $\\text{YBa}_2\\text{Cu}_3\\text{O}_6$.",
                "solution": r"""### Step 1: Triple-Perovskite Superstructure
In an ideal cubic perovskite, $a_{\\text{perov}} \\approx 3.9\\text{ Å}$.
For YBCO:
\\[
\\frac{c}{3} = \\frac{11.684\\text{ Å}}{3} = 3.895\\text{ Å}
\\]
This matches the average in-plane parameters $\\bar{a} = (3.823 + 3.886)/2 = 3.855\\text{ Å}$ within $1.0\\%$.
Thus, the unit cell consists of three perovskite subcells stacked vertically along $\\mathbf{c}$ with sequence:
\\[
[\\text{BaO}] - [\\text{CuO}_2] - [\\text{Y}] - [\\text{CuO}_2] - [\\text{BaO}] - [\\text{CuO}]
\\]

### Step 2: Cation Ordering and Oxygen Vacancy Ordering
1. **Cation Stacking**:
   The large $\\text{Ba}^{2+}$ ($r = 1.61\\text{ Å}$) and smaller $\\text{Y}^{3+}$ ($r = 1.02\\text{ Å}$) order along $\\mathbf{c}$ in a $1:2$ sequence: $\\dots -\\text{Ba}-\\text{Y}-\\text{Ba}-\\text{Ba}-\\text{Y}-\\text{Ba}- \\dots$
2. **Yttrium Layer Depletion**:
   A stoichiometric triple perovskite $(\\text{YBa}_2\\text{Cu}_3\\text{O}_9)$ would contain 9 oxygens per formula unit.
   In $\\text{YBa}_2\\text{Cu}_3\\text{O}_7$, exactly two oxygen atoms are removed:
   - One full oxygen atom is missing from the central yttrium plane $z = 1/2$. Because $\\text{Y}^{3+}$ has a small ionic radius, an 8-fold square prismatic coordination environment is energetically preferred over 12-fold coordination. Hence, the yttrium layer contains **zero oxygen atoms**, separating two planar $[\\text{CuO}_2]$ superconducting sheets.
   - The second oxygen is partially removed from the basal copper layer, forming 1D $[\\text{CuO}]$ chains running along the $\\mathbf{b}$-axis ($y$-direction). This breaks tetragonal symmetry, producing the observed orthorhombic distortion ($b > a$).

### Step 3: Copper Valence Calculations
Assigning standard oxidation states: $\\text{Y}^{3+}$, $\\text{Ba}^{2+}$, $\\text{O}^{2-}$.
1. **For $\\text{YBa}_2\\text{Cu}_3\\text{O}_7$**:
   Total positive charge from non-copper cations:
   \\[
   (+3) + 2(+2) = +7
   \\]
   Total negative charge:
   \\[
   7(-2) = -14
   \\]
   Charge neutrality:
   \\[
   +7 + 3 V_{\\text{Cu}} - 14 = 0 \\implies 3 V_{\\text{Cu}} = +7 \\implies V_{\\text{Cu}} = +\\frac{7}{3} = +2.333
   \\]
   This corresponds to a mixed valence of two $\\text{Cu}^{2+}$ ions (in the $[\\text{CuO}_2]$ planes) and one $\\text{Cu}^{3+}$ ion (in the $[\\text{CuO}]$ chains), injecting $0.167$ mobile holes per copper site into the superconducting planes.

2. **For $\\text{YBa}_2\\text{Cu}_3\\text{O}_6$**:
   Total negative charge:
   \\[
   6(-2) = -12
   \\]
   \\[
   +7 + 3 V_{\\text{Cu}} - 12 = 0 \\implies 3 V_{\\text{Cu}} = +5 \\implies V_{\\text{Cu}} = +\\frac{5}{3} = +1.667
   \\]
   Here, chain copper is completely reduced to linearly coordinated $\\text{Cu}^+$, while planar copper remains $\\text{Fe}^{2+}$/$\\text{Cu}^{2+}$ ($d^9$) Mott insulating with zero hole carriers ($T_c = 0\\text{ K}$, antiferromagnetic insulator)."""
            },
            {
                "probNumber": "6.7",
                "title": "Intercalation Thermodynamics and Electrochemical Potential in LiCoO2",
                "difficulty": "Advanced",
                "statement": "In a commercial lithium-ion battery, lithium deintercalates from $\\text{LiCoO}_2$ according to $\\text{LiCoO}_2 \\rightleftharpoons \\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}^+ + x e^-$.\\n(a) Formulate the thermodynamic relationship connecting the cell open-circuit voltage $V_{\\text{OCV}}(x)$ to the chemical potential of lithium $\\mu_{\\text{Li}}(x)$.\\n(b) If the open-circuit voltage against metallic lithium is $V = 3.95\\text{ V}$ at $x = 0.5$, calculate the partial molar Gibbs free energy $\\Delta \\bar{G}_{\\text{Li}}$ of lithium in the cathode relative to pure lithium metal.\\n(c) Compute the theoretical specific charge capacity $Q_{\\text{theo}}$ of $\\text{LiCoO}_2$ in $\\text{mAh/g}$ for full deintercalation ($x = 1.0$) given $M = 97.87\\text{ g/mol}$.",
                "solution": r"""### Step 1: Open-Circuit Voltage and Chemical Potential
The cell electrochemical reaction between the cathode and a metallic lithium anode is:
\\[
\\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}_{\\text{metal}} \\rightleftharpoons \\text{LiCoO}_2
\\]
By the Nernst-Planck relation, the electrical work done by transporting $z = 1$ electron per lithium ion across potential difference $V_{\\text{OCV}}$ equals the change in lithium chemical potential:
\\[
-e V_{\\text{OCV}}(x) = \\mu_{\\text{Li}}^{\\text{cathode}}(x) - \\mu_{\\text{Li}}^{\\text{metal}}
\\]
Multiplying by Avogadro's number:
\\[
V_{\\text{OCV}}(x) = -\\frac{\\mu_{\\text{Li}}(x) - \\mu_{\\text{Li}}^0}{F} = -\\frac{\\Delta \\bar{G}_{\\text{Li}}(x)}{F}
\\]
where $F = 96485.3\\text{ C/mol}$ is the Faraday constant.

### Step 2: Partial Molar Gibbs Free Energy
At $x = 0.5$, $V_{\\text{OCV}} = 3.95\\text{ V}$:
\\[
\\Delta \\bar{G}_{\\text{Li}} = -F V_{\\text{OCV}} = -(96485.3\\text{ C/mol})(3.95\\text{ J/C}) = -381,\\!117\\text{ J/mol} = -381.1\\text{ kJ/mol}
\\]
The negative sign indicates that lithium insertion into $\\text{Li}_{0.5}\\text{CoO}_2$ is strongly exergonic, stabilizing the intercalated host by $381.1\\text{ kJ}$ per mole of lithium.

### Step 3: Theoretical Specific Capacity
The theoretical capacity represents the total electric charge released per unit mass of pristine $\\text{LiCoO}_2$:
\\[
Q_{\\text{theo}} = \\frac{n F}{M}
\\]
For $n = 1$ electron per formula unit ($M = 97.87\\text{ g/mol}$):
\\[
Q_{\\text{theo}} = \\frac{1 \\times 96485.3\\text{ C/mol}}{97.87\\text{ g/mol}} = 985.85\\text{ C/g}
\\]
Converting Coulombs to milliampere-hours ($1\\text{ mAh} = 10^{-3}\\text{ A} \\times 3600\\text{ s} = 3.6\\text{ C}$):
\\[
Q_{\\text{theo}} = \\frac{985.85\\text{ C/g}}{3.6\\text{ C/mAh}} = 273.85\\text{ mAh/g}
\\]
In practical cells, deintercalation is restricted to $x \\le 0.5$ ($Q_{\\text{prac}} \\approx 140\\text{ mAh/g}$) to prevent structural collapse from the hexagonal $\\text{O3}$ to the monoclinic $\\text{H1-3}$ phase."""
            },
            {
                "probNumber": "6.8",
                "title": "Pauling's Rules Assessment of Complex Silicate Topologies",
                "difficulty": "Intermediate",
                "statement": "Evaluate the connectivity and stability of the following silicate topologies using Pauling's electrostatic rules:\\n(a) Nesosilicates (orthosilicates, e.g., forsterite $\\text{Mg}_2\\text{SiO}_4$).\\n(b) Inosilicates (single-chain silicates, e.g., enstatite $\\text{MgSiO}_3$).\\n(c) Tectosilicates (framework silicates, e.g., quartz $\\text{SiO}_2$).\\nDetermine the number of shared corners per $[\\text{SiO}_4]$ tetrahedron and the effective bridging vs non-bridging oxygen charges in each class.",
                "solution": r"""### Step 1: Fundamental Building Unit
In all silicates, silicon has valence $z_{\\text{Si}} = +4$ and forms a regular $[\\text{SiO}_4]$ tetrahedron ($CN = 4$).
The electrostatic bond valence strength is:
\\[
s = \\frac{z_{\\text{Si}}}{CN} = \\frac{+4}{4} = +1.0
\\]
Oxygen has formal charge $z_{\\text{O}} = -2$.

### Step 2: Evaluation of Silicate Classes
1. **Nesosilicates (Isolated Tetrahedra, $\\text{SiO}_4^{4-}$)**:
   - Shared corners: $0$ (tetrahedra are completely isolated).
   - Each oxygen receives $s = +1.0$ from one central $\\text{Si}$.
   - Remaining $-1.0$ valence is satisfied by coordinating to external metal cations (e.g., in $\\text{Mg}_2\\text{SiO}_4$, each oxygen is coordinated to three $\\text{Mg}^{2+}$ with $s_{\\text{Mg}} = 2/6 = 1/3$; sum $= 1.0 + 3(1/3) = 2.0$, perfectly satisfying Rule 2).

2. **Inosilicates (Single Chains, $[\text{SiO}_3^{2-}]_n$)**:
   - Each tetrahedron shares $2$ corners with adjacent tetrahedra along the 1D chain.
   - **Bridging Oxygens ($O_{\\text{br}}$)**: Shared between two silicons. Receives $s = 1.0 + 1.0 = 2.0$. The valence is $100\\%$ satisfied by silicon alone; $O_{\\text{br}}$ does not bond to metal cations.
   - **Non-Bridging Oxygens ($O_{\\text{nbr}}$)**: Coordinated to only one silicon. Receives $s = +1.0$. Remaining $-1.0$ is satisfied by coordinating to $\\text{Mg}^{2+}$ cations.
   - Formula: $\\text{Si} + 2(O_{1/2}) + 2(O^-) = \\text{SiO}_3^{2-}$.

3. **Tectosilicates (3D Framework, $\\text{SiO}_2$)**:
   - Every tetrahedron shares all $4$ corners with neighboring tetrahedra.
   - Every single oxygen is a bridging oxygen ($O_{\\text{br}}$) shared between exactly two silicons:
   \\[
   \\sum s_i = 1.0 + 1.0 = 2.0 = |z_{\\text{O}}|
   \\]
   - Pauling's Rule 2 is satisfied completely by Si-O network alone without needing any extra cations. Formula is $\\text{SiO}_{4/2} = \\text{SiO}_2$."""
            },
            {
                "probNumber": "6.9",
                "title": "MOF-5 Pore Window Geometry, Void Fraction, and Theoretical Surface Area Determination",
                "difficulty": "Advanced",
                "statement": "The metal-organic framework MOF-5 ($\\text{Zn}_4\\text{O}(\\text{BDC})_3$) crystallizes in a face-centered cubic lattice ($Fm\\bar{3}m$) with lattice constant $a = 25.885\\text{ Å}$. Each unit cell contains $Z = 8$ formula units ($M = 770.87\\text{ g/mol}$).\\n(a) Compute the unit cell volume and theoretical crystal density $\\rho_{\\text{cryst}}$.\\n(b) If the framework skeleton occupies a van der Waals solid volume of $V_{\\text{frame}} = 3680\\text{ Å}^3$ per unit cell, compute the fractional pore void volume $f_{\\text{void}}$.\\n(c) Calculate the theoretical gravimetric surface area $S_{\\text{BET}}$ in $\\text{m}^2/\\text{g}$ approximating the framework as a spherical cage of internal diameter $D = 15.2\\text{ Å}$ accessible to guest molecules.",
                "solution": r"""### Step 1: Unit Cell Volume and Density
Unit cell volume:
\\[
V_c = a^3 = (25.885 \\times 10^{-8}\\text{ cm})^3 = 1.7344 \\times 10^{-21}\\text{ cm}^3 = 17344\\text{ Å}^3
\\]
Molar mass of unit cell contents ($Z = 8$ formula units):
\\[
M_{\\text{cell}} = 8 \\times 770.87\\text{ g/mol} = 6166.96\\text{ g/mol}
\\]
Density:
\\[
\\rho = \\frac{M_{\\text{cell}}}{N_A V_c} = \\frac{6166.96\\text{ g/mol}}{(6.02214 \\times 10^{23}\\text{ mol}^{-1})(1.7344 \\times 10^{-21}\\text{ cm}^3)} = \\frac{6166.96}{1044.48} = 0.5904\\text{ g/cm}^3
\\]
(Extremely low density, nearly $40\\%$ less dense than liquid water!).

### Step 2: Fractional Void Volume
Total volume: $V_c = 17344\\text{ Å}^3$.
Framework volume: $V_{\\text{frame}} = 3680\\text{ Å}^3$.
Empty pore volume:
\\[
V_{\\text{pore}} = V_c - V_{\\text{frame}} = 17344 - 3680 = 13664\\text{ Å}^3
\\]
Void fraction:
\\[
f_{\\text{void}} = \\frac{V_{\\text{pore}}}{V_c} = \\frac{13664}{17344} = 0.7878 = 78.78\\%
\\]
Nearly $79\\%$ of the crystal volume is empty space.

### Step 3: Theoretical Surface Area
In MOF-5, there are $8$ main spherical cages per unit cell with internal diameter $D = 15.2\\text{ Å}$ ($R = 7.6\\text{ Å}$).
Surface area per cage:
\\[
A_{\\text{cage}} = 4\\pi R^2 = 4\\pi (7.6\\text{ Å})^2 = 4\\pi (57.76) = 725.83\\text{ Å}^2
\\]
Total internal surface area per unit cell:
\\[
A_{\\text{cell}} = 8 \\times A_{\\text{cage}} = 8 \\times 725.83\\text{ Å}^2 = 5806.6\\text{ Å}^2 = 5.8066 \\times 10^{-17}\\text{ m}^2
\\]
Mass of one unit cell:
\\[
m_{\\text{cell}} = \\frac{M_{\\text{cell}}}{N_A} = \\frac{6166.96\\text{ g/mol}}{6.02214 \\times 10^{23}\\text{ mol}^{-1}} = 1.0240 \\times 10^{-20}\\text{ g}
\\]
Specific surface area:
\\[
S_{\\text{theo}} = \\frac{A_{\\text{cell}}}{m_{\\text{cell}}} = \\frac{5.8066 \\times 10^{-17}\\text{ m}^2}{1.0240 \\times 10^{-20}\\text{ g}} = 5670\\text{ m}^2/\\text{g}
\\]
(Matches nitrogen gas adsorption BET measurements, which range between $2900 - 3800\\text{ m}^2/\\text{g}$ with geometric surface models predicting $\\sim 3500 - 4500\\text{ m}^2/\\text{g}$)."""
            }
        ]
    }
    return u6

if __name__ == '__main__':
    u6 = get_unit_6()
    print("Unit 6 successfully generated:")
    print("Title:", u6["title"])
    print("Sections:", len(u6["sections"]))
    print("Problems:", len(u6["problems"]))
