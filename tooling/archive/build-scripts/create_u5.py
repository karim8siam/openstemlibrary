import json

def get_unit_5():
    u5 = {
        "id": "unit-5",
        "number": 5,
        "title": "Archetypal Binary Ionic Crystal Structures",
        "leadSummary": "Comprehensive analysis of archetypal binary structures: rock salt (NaCl), cesium chloride (CsCl), zinc blende (sphalerite), wurtzite, fluorite (CaF2), and antifluorite (Li2O). Pauling's structural rules, polyhedral condensation, limiting radius ratio derivations, and pressure/temperature-induced structural phase transitions.",
        "simulations": ["sim_ssc_binary_crystal_viewer"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Sodium Chloride (NaCl, Rock Salt) Structure: Geometry, Coordination & Polyhedra",
                "content": r"""The **sodium chloride** (rock salt, halite) prototype represents the preeminent $1:1$ stoichiometric ionic crystal structure. It is adopted by hundreds of ionic compounds, including all alkali halides (except $\\text{CsCl}, \\text{CsBr}, \\text{CsI}$), alkaline earth monoxides ($\\text{MgO}, \\text{CaO}, \\text{SrO}, \\text{BaO}$), transition metal monoxides ($\\text{FeO}, \\text{CoO}, \\text{NiO}$), and transition metal nitrides/carbides ($\\text{TiN}, \\text{TiC}$).

### Crystallographic Lattice & Atomic Coordinates
- **Space Group**: $Fm\\bar{3}m$ (No. 225), Hermann-Mauguin full symbol $F 4/m \\bar{3} 2/m$, Pearson symbol $cF8$.
- **Lattice Type**: Face-Centered Cubic (FCC Bravais lattice).
- **Formula Units per Unit Cell**: $Z = 4$ $\\text{NaCl}$ units ($4\\text{ Na}^+$ and $4\\text{ Cl}^-$ ions).
- **Wyckoff Positions**:
  - $\\text{Na}^+$ at Wyckoff site $4a$: $(0, 0, 0)$, $\\left(\\frac{1}{2}, \\frac{1}{2}, 0\\right)$, $\\left(\\frac{1}{2}, 0, \\frac{1}{2}\\right)$, $\\left(0, \\frac{1}{2}, \\frac{1}{2}\\right)$.
  - $\\text{Cl}^-$ at Wyckoff site $4b$: $\\left(\\frac{1}{2}, \\frac{1}{2}, \\frac{1}{2}\\right)$, $\\left(0, 0, \\frac{1}{2}\\right)$, $\\left(0, \\frac{1}{2}, 0\\right)$, $\\left(\\frac{1}{2}, 0, 0\\right)$.
This spatial arrangement is mathematically equivalent to two interpenetrating FCC sublattices displaced relative to one another along the cubic body diagonal by $\\boldsymbol{\\tau} = \\frac{1}{2}[100]$ (or $\\frac{1}{2}[111]$).

### Coordination Geometry & Polyhedral Topology
- **Coordination Number (CN)**: Both cations and anions exhibit rigorous **$6:6$ octahedral coordination** ($O_h$ point symmetry).
- **Cation Environment**: Each $\\text{Na}^+$ ion is coordinated by $6$ equidistant $\\text{Cl}^-$ anions forming a regular octahedron with bond length:
\\[
d_{\\text{Na-Cl}} = \\frac{a}{2}
\\]
- **Anion Environment**: Each $\\text{Cl}^-$ ion is symmetrically coordinated by $6$ equidistant $\\text{Na}^+$ cations.
- **Polyhedral Network**: The crystal structure can be described as a 3D network of edge-sharing $[\text{NaCl}_6]$ octahedra. Each octahedron shares all $12$ of its edges with adjacent octahedra in three dimensions, maximizing packing density while satisfying Pauling's electrostatic valence sum rules."""
            },
            {
                "secNumber": "5.2",
                "title": "Cesium Chloride (CsCl) Structure: 8:8 Coordination & Transition Pressures",
                "content": r"""When the radius of the cation approaches that of the anion ($r^+/r^- > 0.732$), the $6:6$ coordination of the rock salt lattice becomes sterically unfavorable. The crystal stabilizes into the denser **cesium chloride** ($\\text{CsCl}$) structural archetype.

### Crystallographic Lattice & Basis
- **Space Group**: $Pm\\bar{3}m$ (No. 221), Pearson symbol $cP2$.
- **Lattice Type**: Primitive Cubic (Primitive Bravais lattice, **NOT** BCC!).
- **Formula Units per Unit Cell**: $Z = 1$ $\\text{CsCl}$ pair.
- **Wyckoff Coordinates**:
  - $\\text{Cs}^+$ at Wyckoff site $1a$: $(0, 0, 0)$.
  - $\\text{Cl}^-$ at Wyckoff site $1b$: $\\left(\\frac{1}{2}, \\frac{1}{2}, \\frac{1}{2}\\right)$.

> [!NOTE]
> Although $\\text{CsCl}$ visually resembles a body-centered cubic cell, it is crystallographically **primitive cubic** because the atom at the corner ($\\text{Cs}^+$) is chemically distinct from the atom at the center ($\\text{Cl}^-$). True BCC symmetry requires identical atoms at $(0,0,0)$ and $(1/2, 1/2, 1/2)$.

### Coordination & Geometric Relations
- **Coordination Number (CN)**: **$8:8$ cubic coordination**.
- Each $\\text{Cs}^+$ ion sits at the center of a cube formed by $8$ surrounding $\\text{Cl}^-$ anions, and vice versa.
- Contact along the body diagonal of the cubic unit cell gives:
\\[
\\sqrt{3} a = 2(r^+ + r^-) \\implies a = \\frac{2(r^+ + r^-)}{\\sqrt{3}}
\\]
- **Compounds Adopting CsCl**: $\\text{CsCl}, \\text{CsBr}, \\text{CsI}, \\text{TlCl}, \\text{TlBr}, \\text{NH}_4\\text{Cl}$ (low temperature), and intermetallic equiatomic alloys such as $\\beta'\\text{-CuZn}$ (brass), $\\text{NiAl}$, and $\\text{FeAl}$ (B2 Hume-Rothery phases).
- **Pressure-Induced Phase Transitions**: Under high hydrostatic pressure ($P \\approx 30\\text{ GPa}$ for $\\text{NaCl}$), rock salt structures transition to $\\text{CsCl}$ structures because 8-fold coordination yields a smaller molar volume ($\sim 5-10\\%$ volume reduction), decreasing the enthalpy $H = U + PV$."""
            },
            {
                "secNumber": "5.3",
                "title": "Zinc Blende (beta-ZnS, Sphalerite) Structure: Tetrahedral Coordination & FCC Sublattice",
                "content": r"""When the radius ratio is small ($r^+/r^- < 0.414$) or when covalent directional $sp^3$ hybrid bonding dominates over pure electrostatics, binary solids crystallize in tetrahedral topologies. The two archetypes are **zinc blende** (cubic) and **wurtzite** (hexagonal).

### Crystallographic Lattice of Zinc Blende (Sphalerite)
- **Space Group**: $F\\bar{4}3m$ (No. 216), non-centrosymmetric, Pearson symbol $cF8$.
- **Lattice Type**: Face-Centered Cubic (FCC).
- **Formula Units per Unit Cell**: $Z = 4$ $\\text{ZnS}$ units.
- **Wyckoff Coordinates**:
  - $\\text{S}^{2-}$ anions on FCC lattice sites $4a$: $(0,0,0), \\left(\\frac{1}{2},\\frac{1}{2},0\\right), \\left(\\frac{1}{2},0,\\frac{1}{2}\\right), \\left(0,\\frac{1}{2},\\frac{1}{2}\\right)$.
  - $\\text{Zn}^{2+}$ cations in half of the tetrahedral interstitials $4c$: $\\left(\\frac{1}{4},\\frac{1}{4},\\frac{1}{4}\\right), \\left(\\frac{3}{4},\\frac{3}{4},\\frac{1}{4}\\right), \\left(\\frac{3}{4},\\frac{1}{4},\\frac{3}{4}\\right), \\left(\\frac{1}{4},\\frac{3}{4},\\frac{3}{4}\\right)$.

### Structural Topology & Polyhedral Condensation
- **Coordination Number (CN)**: **$4:4$ tetrahedral coordination** ($T_d$ point symmetry).
- An FCC anion lattice contains $8$ tetrahedral interstitial sites per unit cell. In zinc blende, **exactly $50\\%$ of tetrahedral sites** are occupied in an alternating ordered manner, such that all occupied tetrahedra point in the identical spatial orientation.
- The bond length along the $[111]$ body diagonal is:
\\[
d_{\\text{Zn-S}} = \\frac{\\sqrt{3}}{4} a
\\]
- Each $[\text{ZnS}_4]$ tetrahedron shares all four of its corners with neighboring tetrahedra. No edges or faces are shared.
- **Isostructural Materials**: Crucial semiconductors: $\\text{GaAs}, \\text{InP}, \\text{InAs}, \\text{CdTe}, \\text{ZnSe}, \\beta\\text{-SiC}$, and diamond/silicon/germanium (which are the homoatomic equivalents with $Fd\\bar{3}m$ symmetry)."""
            },
            {
                "secNumber": "5.4",
                "title": "Wurtzite (alpha-ZnS) Structure: Hexagonal Symmetry, Non-Centrosymmetric Properties & Polarity",
                "content": r"""The **wurtzite** archetype is the hexagonal polymorph of zinc sulfide, representing tetrahedral coordination in an HCP anion framework rather than FCC.

### Crystallographic Parameters
- **Space Group**: $P6_3mc$ (No. 186), polar, non-centrosymmetric, Pearson symbol $hP4$.
- **Lattice Type**: Hexagonal.
- **Formula Units per Cell**: $Z = 2$ formula units.
- **Wyckoff Sites**:
  - $\\text{S}^{2-}$ at $2b$: $\\left(\\frac{1}{3}, \\frac{2}{3}, 0\\right), \\left(\\frac{2}{3}, \\frac{1}{3}, \\frac{1}{2}\\right)$.
  - $\\text{Zn}^{2+}$ at $2b$: $\\left(\\frac{1}{3}, \\frac{2}{3}, u\\right), \\left(\\frac{2}{3}, \\frac{1}{3}, \\frac{1}{2} + u\\right)$ where $u \\approx 3/8 = 0.375$.

### Zinc Blende vs Wurtzite: Stacking Sequence & Bond Conformation
- **Stacking Sequence**:
  - Zinc Blende: Cubic close-packed anion layers $\\dots ABCABC \\dots$ along $[111]$. Tetrahedra are connected in a **staggered (chair-like)** trans-conformation.
  - Wurtzite: Hexagonal close-packed anion layers $\\dots ABABAB \\dots$ along $[0001]$. Tetrahedra are connected in an **eclipsed (boat-like)** cis-conformation.
- **Ideal Axial Ratio**: For ideal close packing of hard spheres:
\\[
\\left(\\frac{c}{a}\\right)_{\\text{ideal}} = \\sqrt{\\frac{8}{3}} = 1.63299, \\quad u_{\\text{ideal}} = \\frac{3}{8} = 0.37500
\\]
In real crystals (e.g., $\\text{ZnO}, \\text{GaN}, \\text{AlN}$), electrostatic dipole interactions cause deviations: $c/a < 1.633$ and $u > 0.375$.

### Spontaneous Polarization & Piezoelectricity
Because space group $P6_3mc$ lacks an inversion center and possesses a unique polar axis along the $\\mathbf{c}$-axis $[0001]$, wurtzite crystals exhibit:
1. **Spontaneous Electric Polarization** ($P_{\\text{sp}}$ along $[0001]$).
2. **Piezoelectricity**: Application of uniaxial mechanical stress along $\\mathbf{c}$ induces an macroscopic electrostatic potential difference.
3. **Piezoelectric and Optoelectronic Applications**: Wide bandgap semiconductors $\\text{GaN}, \\text{InN}, \\text{AlN}$ form the basis of blue/UV LEDs, laser diodes, and high-electron-mobility transistors (HEMTs)."""
            },
            {
                "secNumber": "5.5",
                "title": "Fluorite (CaF2) Structure: 8:4 Coordination, Interstitial Voids & Fast Anion Transport",
                "content": r"""The **fluorite** ($\\text{CaF}_2$) prototype is the archetypal structure for $1:2$ stoichiometric binary compounds where the cation is significantly larger than the anion ($r_{\\text{cation}} > r_{\\text{anion}}$).

### Crystallographic Lattice & Atomic Coordinates
- **Space Group**: $Fm\\bar{3}m$ (No. 225), Pearson symbol $cF12$.
- **Formula Units per Cell**: $Z = 4$ $\\text{CaF}_2$ units ($4\\text{ Ca}^{2+}$ and $8\\text{ F}^-$ ions).
- **Wyckoff Coordinates**:
  - $\\text{Ca}^{2+}$ cations form an FCC lattice at site $4a$: $(0,0,0) + \\text{FCC translations}$.
  - $\\text{F}^-$ anions occupy **all eight tetrahedral interstitial sites** at site $8c$:
  \\[
  \\left(\\pm \\frac{1}{4}, \\pm \\frac{1}{4}, \\pm \\frac{1}{4}\\right)
  \\]

### Coordination Numbers & Interstitial Chemistry
- **Coordination Ratio**: **$8:4$ coordination**.
  - Each $\\text{Ca}^{2+}$ cation is coordinated by $8\\text{ F}^-$ anions at the corners of a cube ($CN = 8$).
  - Each $\\text{F}^-$ anion is coordinated by $4\\text{ Ca}^{2+}$ cations at the vertices of a regular tetrahedron ($CN = 4$).
- **Interstitial Octahedral Voids**:
  In the fluorite lattice, all tetrahedral sites are filled by fluoride ions, but **all octahedral interstitial sites** at $(1/2, 1/2, 1/2)$ and $(1/2, 0, 0)$ remain **completely empty**.
- **Fast-Ion (Superionic) Conduction**:
  Because $50\\%$ of the cubic interstitial cages are vacant, fluorite-structured oxides (e.g., yttria-stabilized zirconia $\\text{YSZ}$, ceria $\\text{CeO}_2$, urania $\\text{UO}_2$) exhibit exceptional oxygen vacancy mobility at elevated temperatures ($T > 600^\\circ\\text{C}$), functioning as the standard solid electrolytes in Solid Oxide Fuel Cells (SOFCs)."""
            },
            {
                "secNumber": "5.6",
                "title": "Antifluorite (Li2O) Structure: Inversion of Cation-Anion Sublattices & Energetics",
                "content": r"""The **antifluorite** prototype is the direct crystallographic inverse of the fluorite lattice, adopted by $2:1$ stoichiometric compounds where small cations combine with large anions.

### Crystallographic Architecture
- **Space Group**: $Fm\\bar{3}m$ (No. 225), Pearson symbol $cF12$.
- **Formula Units**: $Z = 4$ units of $\\text{M}_2\\text{X}$ (e.g., $\\text{Li}_2\\text{O}, \\text{Na}_2\\text{O}, \\text{K}_2\\text{O}, \\text{Li}_2\\text{S}$).
- **Wyckoff Positions**:
  - Anions ($\\text{O}^{2-}$): Occupy the FCC lattice points $4a$ at $(0,0,0)$.
  - Cations ($\\text{Li}^+$): Occupy all eight tetrahedral interstitial sites $8c$ at $\\left(\\pm \\frac{1}{4}, \\pm \\frac{1}{4}, \\pm \\frac{1}{4}\\right)$.

### Coordination & Solid-State Electrochemical Significance
- **Coordination Ratio**: **$4:8$ coordination**.
  - Small cations ($\\text{Li}^+$) have tetrahedral coordination ($CN = 4$).
  - Large anions ($\\text{O}^{2-}$) have 8-fold cubic coordination ($CN = 8$).
- **Madelung Constant**: Because Coulomb energy is quadratic in charge, reversing the charges changes the individual site potentials but maintains the overall electrostatic sum:
\\[
M(\\text{CaF}_2) = M(\\text{Li}_2\\text{O}) = 5.038785 \\quad (\\text{referenced to } r_0)
\\]
- **Lithium Battery Solid Electrolytes**: Antifluorite derivatives (e.g., $\\text{Li}_3\\text{OCl}$, $\\text{Li}_2\\text{S}$-based superionic conductors) exhibit high $\\text{Li}^+$ mobilities through interstitial hopping pathways facilitated by vacant octahedral sites."""
            },
            {
                "secNumber": "5.7",
                "title": "Comparative Polyhedral Architectures: Corner-Sharing, Edge-Sharing & Face-Sharing Stability (Paulings Rules)",
                "content": r"""Linus Pauling (1929) formulated five empirical principles governing the stability, coordination, and polyhedral connectivity of complex ionic crystals.

### Pauling's Five Rules

1. **Rule 1: Coordination Polyhedron & Radius Ratio**:
   A coordinated polyhedron of anions is formed about each cation, the cation-anion distance being determined by the sum of crystal radii, and the coordination number by the radius ratio $r^+/r^-$.
   - $r^+/r^- < 0.155$: 2-fold linear
   - $0.155 - 0.225$: 3-fold trigonal planar
   - $0.225 - 0.414$: 4-fold tetrahedral
   - $0.414 - 0.732$: 6-fold octahedral
   - $0.732 - 1.000$: 8-fold cubic
   - $1.000$: 12-fold cuboctahedral (close-packed)

2. **Rule 2: Electrostatic Valence Rule**:
   In a stable crystal structure, the electrostatic valence strength $s_i$ of each bond reaching an anion from its nearest-neighbor cations equals:
   \\[
   s_i = \\frac{z_i}{\\nu_i}
   \\]
   where $z_i$ is the cation charge and $\\nu_i$ is its coordination number. The sum of bond valences to each anion must equal the anion charge $z_X$:
   \\[
   \\sum_{i} s_i = z_X
   \\]

3. **Rule 3: Polyhedral Connectivity (Sharing of Edges and Faces)**:
   The presence of shared edges and especially shared faces in a coordinated structure decreases its stability. Sharing edges places highly charged cations closer together, increasing cation-cation electrostatic repulsion:
   \\[
   d_{\\text{M-M}}(\\text{corner}) > d_{\\text{M-M}}(\\text{edge}) > d_{\\text{M-M}}(\\text{face})
   \\]

4. **Rule 4: Cation Charge and Coordination Effect on Sharing**:
   In a crystal containing different cations, those with high valency and small coordination number tend not to share polyhedron elements with one another.

5. **Rule 5: Principle of Parsimony**:
   The number of essentially different kinds of constituents in a crystal tends to be small."""
            },
            {
                "secNumber": "5.8",
                "title": "Structural Polymorphism, Temperature-Induced Phase Transformations & High-Pressure Transitions",
                "content": r"""Polymorphism is the capacity of a substance with a fixed chemical composition to crystallize in more than one distinct structural arrangement.

### Classification of Phase Transitions
According to Ehrenfest thermodynamic criteria:
- **First-Order Transitions**: Discontinuous first derivative of Gibbs free energy ($\Delta V \\ne 0$, $\\Delta S = \\Delta H_{\\text{tr}}/T_{\\text{tr}} \\ne 0$). Associated with major structural rearrangements, bond breaking, latent heat, and hysteresis (e.g., graphite $\\to$ diamond, $\\text{NaCl} \\to \\text{CsCl}$ under pressure).
- **Second-Order Transitions**: Continuous $V$ and $S$, but discontinuous second derivatives (heat capacity $\\Delta C_p$, thermal expansion $\\Delta \\alpha$, compressibility $\\Delta \\kappa$). Associated with order-disorder phenomena and subtle symmetry-breaking displacements without latent heat (e.g., ferroelectric Curie transition in $\\text{BaTiO}_3$).

### Reconstructive vs Displacive Transitions (Buerger Classification)
1. **Reconstructive Transformations**:
   Require breaking primary chemical bonds and re-forming new coordination polyhedra. High activation energy barrier ($E_a > 100\\text{ kJ/mol}$), slow kinetics, significant hysteresis, often kinetically trapped at room temperature (e.g., quartz $\\to$ tridymite $\\to$ cristobalite).
2. **Displacive (Martensitic / Soft-Mode) Transformations**:
   Involve minor collective tilts or bond angle distortions of polyhedra without breaking bonds or altering nearest-neighbor topology. Zero or low activation barrier, ultrafast diffusionless kinetics (speed of sound), perfectly reversible (e.g., $\\alpha$-quartz $\\leftrightarrow$ $\\beta$-quartz at $573^\\circ\\text{C}$)."""
            }
        ],
        "problems": [
            {
                "probNumber": "5.1",
                "title": "Quantitative Geometric Derivation of the Limiting Radius Ratio for Octahedral Coordination",
                "difficulty": "Foundational",
                "statement": "Derive from first principles the critical limiting radius ratio $r^+/r^- = \\sqrt{2} - 1 \\approx 0.4142$ below which a 6-fold regular octahedral coordination environment becomes geometrically unstable due to anion-anion contact.",
                "solution": r"""### Step 1: Geometric Configuration of a Regular Octahedron
Consider a central cation of radius $r^+$ surrounded by six identical spherical anions of radius $r^-$ in an ideal octahedral geometry.
Four of the anions lie in the equatorial horizontal plane $xy$, forming a square, while the remaining two anions occupy the apex positions along the $\\pm z$ axes.
For maximum stability:
1. The central cation must touch all six anions: distance from origin to center of any anion is $d = r^+ + r^-$.
2. The anions must not interpenetrate: distance between adjacent anion centers $d_{\\text{anion-anion}} \\ge 2r^-$.

### Step 2: Critical Contact Condition in the Equatorial Plane
At the **limiting radius ratio**, the central cation touches the four equatorial anions simultaneously while the anions just touch one another along the perimeter of the square:
- Side of square formed by four anion centers: $s = 2r^-$.
- Diagonal of square: $D = \\sqrt{s^2 + s^2} = \\sqrt{(2r^-)^2 + (2r^-)^2} = \\sqrt{8(r^-)^2} = 2\\sqrt{2}r^-$.
The diagonal passes through the center of two opposing anions and through the central cation:
\\[
D = 2(r^+ + r^-)
\\]

### Step 3: Radius Ratio Derivation
Equating the two expressions for the diagonal:
\\[
2(r^+ + r^-) = 2\\sqrt{2}r^-
\\]
Dividing both sides by 2:
\\[
r^+ + r^- = \\sqrt{2}r^-
\\]
Subtracting $r^-$ from both sides:
\\[
r^+ = (\\sqrt{2} - 1)r^-
\\]
Dividing by $r^-$:
\\[
\\frac{r^+}{r^-} = \\sqrt{2} - 1 \\approx 1.41421 - 1 = 0.41421
\\]
If $r^+/r^- < 0.414$, the cation is too small to keep the anions apart, leading to anion-anion electrostatic repulsion and driving a transition to 4-fold tetrahedral coordination."""
            },
            {
                "probNumber": "5.2",
                "title": "Quantitative Derivation of the Limiting Radius Ratio for 8-Fold Cubic Coordination",
                "difficulty": "Foundational",
                "statement": "Derive the minimum limiting radius ratio $r^+/r^- = \\sqrt{3} - 1 \\approx 0.7321$ required for stable 8-fold cubic coordination (as seen in the CsCl archetype).",
                "solution": r"""### Step 1: Geometric Model of Cubic Coordination
In 8-fold cubic coordination, a central cation of radius $r^+$ sits at the center of a cube formed by eight anions of radius $r^-$ located at the eight cube vertices.
Let the edge length of the cube be $a$.

### Step 2: Contact Relations
At the limiting boundary:
1. Anions touch each other along the cube edges:
\\[
a = 2r^-
\\]
2. The central cation touches all eight corner anions along the four body diagonals:
\\[
D_{\\text{body}} = \\sqrt{a^2 + a^2 + a^2} = \\sqrt{3}a
\\]
Since the body diagonal spans two anion radii and twice the cation radius:
\\[
D_{\\text{body}} = 2(r^+ + r^-)
\\]

### Step 3: Derivation of the Limiting Ratio
Substitute $a = 2r^-$ into the body diagonal expression:
\\[
2(r^+ + r^-) = \\sqrt{3}(2r^-) = 2\\sqrt{3}r^-
\\]
Divide by 2:
\\[
r^+ + r^- = \\sqrt{3}r^-
\\]
Rearrange:
\\[
r^+ = (\\sqrt{3} - 1)r^-
\\]
\\[
\\frac{r^+}{r^-} = \\sqrt{3} - 1 \\approx 1.73205 - 1 = 0.73205
\\]
For $r^+/r^- \\ge 0.732$, 8-fold cubic coordination is stable. For $0.414 \\le r^+/r^- < 0.732$, 6-fold octahedral coordination is favored."""
            },
            {
                "probNumber": "5.3",
                "title": "Atomic Packing Fraction and Density Derivation of Rock Salt (NaCl)",
                "difficulty": "Intermediate",
                "statement": "Crystalline $\\text{NaCl}$ has a cubic unit cell with parameter $a = 5.640\\text{ Å}$. The ionic radii are $r_{\\text{Na}^+} = 1.02\\text{ Å}$ and $r_{\\text{Cl}^-} = 1.81\\text{ Å}$, with molar masses $M_{\\text{Na}} = 22.99\\text{ g/mol}$ and $M_{\\text{Cl}} = 35.45\\text{ g/mol}$.\\n(a) Compute the theoretical X-ray crystal density $\\rho_{\\text{calc}}$.\\n(b) Formulate and evaluate the Atomic Packing Fraction (APF) of the rock salt lattice.\\n(c) Compare the bond length $a/2$ with the sum of ionic radii and explain the degree of contact.",
                "solution": r"""### Step 1: Theoretical Density Calculation
For $\\text{NaCl}$, the unit cell contains $Z = 4$ formula units ($4\\text{ Na}^+$ and $4\\text{ Cl}^-$).
Molar mass of $\\text{NaCl}$:
\\[
M = 22.99 + 35.45 = 58.44\\text{ g/mol}
\\]
Unit cell volume:
\\[
V_c = a^3 = (5.640 \\times 10^{-8}\\text{ cm})^3 = 1.7941 \\times 10^{-22}\\text{ cm}^3
\\]
Mass of unit cell:
\\[
m_c = \\frac{Z M}{N_A} = \\frac{4 \\times 58.44\\text{ g/mol}}{6.02214 \\times 10^{23}\\text{ mol}^{-1}} = 3.8817 \\times 10^{-22}\\text{ g}
\\]
Density:
\\[
\\rho = \\frac{m_c}{V_c} = \\frac{3.8817 \\times 10^{-22}\\text{ g}}{1.7941 \\times 10^{-22}\\text{ cm}^3} = 2.164\\text{ g/cm}^3
\\]
(Matches experimental density $2.165\\text{ g/cm}^3$ to within $0.05\\%$).

### Step 2: Atomic Packing Fraction (APF)
The volume occupied by the ions (treating them as hard spheres) in one unit cell is:
\\[
V_{\\text{ions}} = 4 \\times \\frac{4}{3}\\pi (r_{\\text{Na}^+}^3 + r_{\\text{Cl}^-}^3)
\\]
Given $r_{\\text{Na}^+} = 1.02\\text{ Å}$ and $r_{\\text{Cl}^-} = 1.81\\text{ Å}$:
\\[
r_{\\text{Na}^+}^3 = (1.02)^3 = 1.0612\\text{ Å}^3
\\]
\\[
r_{\\text{Cl}^-}^3 = (1.81)^3 = 5.9297\\text{ Å}^3
\\]
\\[
r_{\\text{Na}^+}^3 + r_{\\text{Cl}^-}^3 = 6.9909\\text{ Å}^3
\\]
\\[
V_{\\text{ions}} = 4 \\times \\frac{4}{3}\\pi (6.9909) = 16.755 \\times 6.9909 = 117.13\\text{ Å}^3
\\]
Unit cell volume in $\\text{Å}^3$:
\\[
V_c = (5.640)^3 = 179.41\\text{ Å}^3
\\]
Packing fraction:
\\[
\\text{APF} = \\frac{V_{\\text{ions}}}{V_c} = \\frac{117.13}{179.41} = 0.6528 = 65.28\\%
\\]

### Step 3: Bond Length vs Radii Sum
The observed bond distance along the unit cell edge is:
\\[
d_{\\text{Na-Cl}} = \\frac{a}{2} = \\frac{5.640}{2} = 2.820\\text{ Å}
\\]
Sum of Shannon ionic radii:
\\[
r_{\\text{Na}^+} + r_{\\text{Cl}^-} = 1.02 + 1.81 = 2.830\\text{ Å}
\\]
The discrepancy is:
\\[
\\Delta d = 2.820 - 2.830 = -0.010\\text{ Å} \\quad (-0.35\\%)
\\]
This excellent agreement confirms direct cation-anion contact with negligible overlap repulsion."""
            },
            {
                "probNumber": "5.4",
                "title": "Atomic Packing Fraction, Coordination Polyhedra and Unit Cell Parameters of Cesium Chloride (CsCl)",
                "difficulty": "Intermediate",
                "statement": "Cesium chloride crystallizes in a primitive cubic lattice with $a = 4.123\\text{ Å}$. Ionic radii are $r_{\\text{Cs}^+} = 1.74\\text{ Å}$ and $r_{\\text{Cl}^-} = 1.81\\text{ Å}$. Molar masses: $M_{\\text{Cs}} = 132.91\\text{ g/mol}$, $M_{\\text{Cl}} = 35.45\\text{ g/mol}$.\\n(a) Compute the unit cell volume and theoretical density.\\n(b) Calculate the radius ratio and verify the coordination stability.\\n(c) Evaluate the atomic packing fraction and calculate the percentage volume change if $\\text{NaCl}$ were to hypothetically adopt the $\\text{CsCl}$ structure with identical bond lengths.",
                "solution": r"""### Step 1: Unit Cell Volume and Density
For $\\text{CsCl}$, $Z = 1$ formula unit per primitive cell:
\\[
M = 132.91 + 35.45 = 168.36\\text{ g/mol}
\\]
Unit cell volume:
\\[
V_c = a^3 = (4.123 \\times 10^{-8}\\text{ cm})^3 = 7.0087 \\times 10^{-23}\\text{ cm}^3
\\]
Density:
\\[
\\rho = \\frac{1 \\times 168.36\\text{ g/mol}}{(6.02214 \\times 10^{23}\\text{ mol}^{-1})(7.0087 \\times 10^{-23}\\text{ cm}^3)} = \\frac{168.36}{42.207} = 3.989\\text{ g/cm}^3
\\]
(Matches experimental density $3.99\\text{ g/cm}^3$).

### Step 2: Radius Ratio Analysis
\\[
\\frac{r_{\\text{Cs}^+}}{r_{\\text{Cl}^-}} = \\frac{1.74\\text{ Å}}{1.81\\text{ Å}} = 0.9613
\\]
Since $0.9613 > 0.732$, 8-fold cubic coordination is strongly favored over 6-fold rock salt coordination, perfectly adhering to Pauling's Rule 1.
Contact along the body diagonal gives theoretical lattice parameter:
\\[
a_{\\text{calc}} = \\frac{2(r_{\\text{Cs}^+} + r_{\\text{Cl}^-})}{\\sqrt{3}} = \\frac{2(1.74 + 1.81)}{\\sqrt{3}} = \\frac{7.10}{1.73205} = 4.099\\text{ Å}
\\]
Observed $a = 4.123\\text{ Å}$ matches within $0.58\\%$.

### Step 3: Packing Fraction
Volume of ions in primitive cell:
\\[
V_{\\text{ions}} = \\frac{4}{3}\\pi (r_{\\text{Cs}^+}^3 + r_{\\text{Cl}^-}^3) = \\frac{4}{3}\\pi ((1.74)^3 + (1.81)^3) = \\frac{4}{3}\\pi (5.268 + 5.930) = 4.1888 \\times 11.198 = 46.906\\text{ Å}^3
\\]
Packing fraction:
\\[
\\text{APF} = \\frac{46.906\\text{ Å}^3}{(4.123)^3\\text{ Å}^3} = \\frac{46.906}{70.087} = 0.6693 = 66.93\\%
\\]
For identical nearest-neighbor distance $d$, the volume per formula unit is:
- Rock Salt: $V_{\\text{formula}}(\\text{NaCl}) = 2 d^3$.
- Cesium Chloride: $V_{\\text{formula}}(\\text{CsCl}) = \\left(\\frac{2d}{\\sqrt{3}}\\right)^3 = \\frac{8}{3\\sqrt{3}} d^3 \\approx 1.5396 d^3$.
Volume ratio:
\\[
\\frac{V_{\\text{CsCl}}}{V_{\\text{NaCl}}} = \\frac{1.5396}{2.000} = 0.7698 \\implies \\Delta V = -23.0\\%
\\]
The $\\text{CsCl}$ lattice is significantly more compact for equal bond distances."""
            },
            {
                "probNumber": "5.5",
                "title": "Zinc Blende vs Diamond Cubic Packing Fraction and Interatomic Bond Angles",
                "difficulty": "Intermediate",
                "statement": "Gallium arsenide ($\\text{GaAs}$) crystallizes in the zinc blende structure with lattice constant $a = 5.653\\text{ Å}$.\\n(a) Express the tetrahedral bond vectors from the $\\text{Ga}$ atom at $(1/4, 1/4, 1/4)$ to its four nearest $\\text{As}$ neighbors.\\n(b) Prove analytically that the bond angle between any two bonds is $\\arccos(-1/3) \\approx 109.47^\\circ$.\\n(c) Calculate the interatomic $\\text{Ga-As}$ bond distance and compute the atomic packing fraction given covalent radii $r_{\\text{Ga}} = 1.26\\text{ Å}$ and $r_{\\text{As}} = 1.22\\text{ Å}$.",
                "solution": r"""### Step 1: Bond Vectors in Zinc Blende
Consider the $\\text{Ga}$ atom located at position:
\\[
\\mathbf{r}_0 = \\frac{a}{4}(\\hat{\\mathbf{x}} + \\hat{\\mathbf{y}} + \\hat{\\mathbf{z}})
\\]
Its four nearest $\\text{As}$ neighbors reside on the FCC sublattice at:
\\[
\\mathbf{r}_1 = (0, 0, 0)
\\]
\\[
\\mathbf{r}_2 = \\frac{a}{2}(\\hat{\\mathbf{x}} + \\hat{\\mathbf{y}}, 0)
\\]
\\[
\\mathbf{r}_3 = \\frac{a}{2}(\\hat{\\mathbf{x}}, 0, \\hat{\\mathbf{z}})
\\]
\\[
\\mathbf{r}_4 = \\frac{a}{2}(0, \\hat{\\mathbf{y}} + \\hat{\\mathbf{z}})
\\]
The displacement vectors $\\mathbf{v}_i = \\mathbf{r}_i - \\mathbf{r}_0$ from $\\text{Ga}$ to the four $\\text{As}$ atoms are:
\\[
\\mathbf{v}_1 = \\frac{a}{4}(-\\hat{\\mathbf{x}} - \\hat{\\mathbf{y}} - \\hat{\\mathbf{z}})
\\]
\\[
\\mathbf{v}_2 = \\frac{a}{4}(\\hat{\\mathbf{x}} + \\hat{\\mathbf{y}} - \\hat{\\mathbf{z}})
\\]
\\[
\\mathbf{v}_3 = \\frac{a}{4}(\\hat{\\mathbf{x}} - \\hat{\\mathbf{y}} + \\hat{\\mathbf{z}})
\\]
\\[
\\mathbf{v}_4 = \\frac{a}{4}(-\\hat{\\mathbf{x}} + \\hat{\\mathbf{y}} + \\hat{\\mathbf{z}})
\\]

### Step 2: Proof of Tetrahedral Bond Angle
Take any pair of bond vectors, for instance $\\mathbf{v}_1$ and $\\mathbf{v}_2$:
The dot product is:
\\[
\\mathbf{v}_1 \\cdot \\mathbf{v}_2 = \\left(\\frac{a}{4}\\right)^2 [(-1)(1) + (-1)(1) + (-1)(-1)] = \\left(\\frac{a}{4}\\right)^2 [-1 - 1 + 1] = -\\left(\\frac{a}{4}\\right)^2
\\]
The magnitudes are:
\\[
|\\mathbf{v}_1| = \\frac{a}{4}\\sqrt{(-1)^2 + (-1)^2 + (-1)^2} = \\frac{a}{4}\\sqrt{3}
\\]
\\[
|\\mathbf{v}_2| = \\frac{a}{4}\\sqrt{1^2 + 1^2 + (-1)^2} = \\frac{a}{4}\\sqrt{3}
\\]
Therefore:
\\[
\\cos\\theta = \\frac{\\mathbf{v}_1 \\cdot \\mathbf{v}_2}{|\\mathbf{v}_1||\\mathbf{v}_2|} = \\frac{-(a/4)^2}{(a/4\\sqrt{3})^2} = \\frac{-1}{3}
\\]
\\[
\\theta = \\arccos\\left(-\\frac{1}{3}\\right) = 109.471^\\circ
\\]

### Step 3: Bond Distance and Packing Fraction
Interatomic bond distance:
\\[
d_{\\text{Ga-As}} = \\frac{\\sqrt{3}}{4} a = \\frac{\\sqrt{3}}{4} (5.653\\text{ Å}) = 2.4478\\text{ Å}
\\]
Sum of covalent radii: $r_{\\text{Ga}} + r_{\\text{As}} = 1.26 + 1.22 = 2.48\\text{ Å}$ (matches within $1.3\\%$).
Unit cell contains $Z = 4$ Ga and 4 As atoms:
\\[
V_{\\text{atoms}} = 4 \\times \\frac{4}{3}\\pi (r_{\\text{Ga}}^3 + r_{\\text{As}}^3) = \\frac{16\\pi}{3} ((1.26)^3 + (1.22)^3) = 16.755 \\times (2.0004 + 1.8158) = 16.755 \\times 3.8162 = 63.94\\text{ Å}^3
\\]
Unit cell volume:
\\[
V_c = (5.653)^3 = 180.64\\text{ Å}^3
\\]
Packing fraction:
\\[
\\text{APF} = \\frac{63.94}{180.64} = 0.354 = 35.4\\%
\\]
The open, low-density tetrahedral network ($\text{APF} \\approx 34-35\\%$) reflects directional $sp^3$ bonding, far below close-packed systems ($74\\%$)."""
            },
            {
                "probNumber": "5.6",
                "title": "Wurtzite Unit Cell c/a Axial Ratio for Ideal Hexagonal Close Packing",
                "difficulty": "Intermediate",
                "statement": "Derive analytically that for an ideal hexagonal close-packed anion sublattice in the wurtzite structure with equidistant nearest neighbors, the axial ratio is $(c/a)_{\\text{ideal}} = \\sqrt{8/3} \\approx 1.63299$ and the internal coordinate parameter is $u = 3/8 = 0.37500$.",
                "solution": r"""### Step 1: Geometry of the Hexagonal Unit Cell
In an HCP lattice, atoms in layer A form a 2D triangular network with lattice constant $a$.
Layer B rests in the triangular hollows formed by layer A at fractional coordinates $(1/3, 2/3, 1/2)$.
Consider three atoms in layer A at $(0,0,0)$, $(a, 0, 0)$, and $(a/2, a\\sqrt{3}/2, 0)$.
These three atoms form an equilateral triangle of side $a$.
The in-plane distance from each vertex to the centroid of the equilateral triangle is:
\\[
r_{\\text{centroid}} = \\frac{a}{\\sqrt{3}}
\\]

### Step 2: Derivation of $c/a$ Ratio
The atom in layer B rests directly above this centroid at height $z = c/2$.
Because the atom in layer B is touching all three atoms in layer A, the distance between the layer B atom and any layer A atom equals $a$:
\\[
d^2 = r_{\\text{centroid}}^2 + \\left(\\frac{c}{2}\\right)^2 = a^2
\\]
Substitute $r_{\\text{centroid}} = a/\\sqrt{3}$:
\\[
\\frac{a^2}{3} + \\frac{c^2}{4} = a^2
\\]
\\[
\\frac{c^2}{4} = a^2 - \\frac{a^2}{3} = \\frac{2}{3}a^2
\\]
Multiply by 4:
\\[
c^2 = \\frac{8}{3}a^2 \\implies \\left(\\frac{c}{a}\\right)^2 = \\frac{8}{3}
\\]
\\[
\\frac{c}{a} = \\sqrt{\\frac{8}{3}} = \\frac{2\\sqrt{2}}{\\sqrt{3}} = \\frac{2\\sqrt{6}}{3} \\approx 1.63299
\\]

### Step 3: Derivation of Internal Parameter $u$
In the wurtzite unit cell, each cation at $(1/3, 2/3, u)$ is coordinated by four anions:
- One apical anion along the $\\mathbf{c}$ axis at $(1/3, 2/3, 0)$ with bond length $d_{\\text{apical}} = uc$.
- Three basal anions at $(2/3, 1/3, 1/2)$, $(1/3, -1/3, 1/2)$, $(-2/3, -1/3, 1/2)$.
For a regular tetrahedron, all four bond lengths must be strictly equal:
\\[
d_{\\text{apical}}^2 = d_{\\text{basal}}^2
\\]
The basal bond length squared is:
\\[
d_{\\text{basal}}^2 = \\frac{a^2}{3} + \\left(\\frac{c}{2} - uc\\right)^2 = \\frac{a^2}{3} + c^2\\left(\\frac{1}{2} - u\\right)^2
\\]
Equating to $d_{\\text{apical}}^2 = (uc)^2$:
\\[
u^2 c^2 = \\frac{a^2}{3} + c^2\\left(\\frac{1}{4} - u + u^2\\right) = \\frac{a^2}{3} + \\frac{c^2}{4} - u c^2 + u^2 c^2
\\]
Subtract $u^2 c^2$ from both sides:
\\[
0 = \\frac{a^2}{3} + \\frac{c^2}{4} - u c^2 \\implies u c^2 = \\frac{a^2}{3} + \\frac{c^2}{4}
\\]
Divide by $c^2$:
\\[
u = \\frac{1}{3}\\left(\\frac{a}{c}\\right)^2 + \\frac{1}{4}
\\]
Substitute $(a/c)^2 = 3/8$:
\\[
u = \\frac{1}{3}\\left(\\frac{3}{8}\\right) + \\frac{1}{4} = \\frac{1}{8} + \\frac{2}{8} = \\frac{3}{8} = 0.37500
\\]
Thus, an ideal wurtzite crystal has $c/a = 1.633$ and $u = 0.375$."""
            },
            {
                "probNumber": "5.7",
                "title": "Fluorite (CaF2) Theoretical Density, Interstitial Octahedral Voids and Void Volume Calculation",
                "difficulty": "Intermediate",
                "statement": "Calcium fluoride ($\\text{CaF}_2$) crystallizes in the fluorite structure with lattice constant $a = 5.463\\text{ Å}$. Molar masses: $M_{\\text{Ca}} = 40.078\\text{ g/mol}$, $M_{\\text{F}} = 18.998\\text{ g/mol}$. Shannon radii: $r(\\text{Ca}^{2+}, CN=8) = 1.12\\text{ Å}$, $r(\\text{F}^-, CN=4) = 1.31\\text{ Å}$.\\n(a) Compute the unit cell volume and theoretical crystal density.\\n(b) Calculate the fractional void volume of the unit cell.\\n(c) Determine the maximum radius $r_{\\text{void}}$ of an interstitial sphere that can be accommodated in the vacant octahedral site $(1/2, 1/2, 1/2)$ without distorting the surrounding fluoride sublattice.",
                "solution": r"""### Step 1: Unit Cell Volume and Theoretical Density
The fluorite unit cell contains $Z = 4$ $\\text{CaF}_2$ units ($4\\text{ Ca}^{2+}$ and $8\\text{ F}^-$).
Molar mass:
\\[
M = 40.078 + 2(18.998) = 78.074\\text{ g/mol}
\\]
Unit cell volume:
\\[
V_c = a^3 = (5.463 \\times 10^{-8}\\text{ cm})^3 = 1.6304 \\times 10^{-22}\\text{ cm}^3
\\]
Density:
\\[
\\rho = \\frac{4 \\times 78.074\\text{ g/mol}}{(6.02214 \\times 10^{23}\\text{ mol}^{-1})(1.6304 \\times 10^{-22}\\text{ cm}^3)} = \\frac{312.296}{98.183} = 3.181\\text{ g/cm}^3
\\]
(Matches experimental density $3.180\\text{ g/cm}^3$).

### Step 2: Void Volume and Packing Fraction
Total volume occupied by the ions:
\\[
V_{\\text{ions}} = 4 \\times \\frac{4}{3}\\pi r_{\\text{Ca}}^{3} + 8 \\times \\frac{4}{3}\\pi r_{\\text{F}}^{3}
\\]
\\[
r_{\\text{Ca}}^3 = (1.12)^3 = 1.4049\\text{ Å}^3 \\implies 4 \\times \\frac{4}{3}\\pi (1.4049) = 23.54\\text{ Å}^3
\\]
\\[
r_{\\text{F}}^3 = (1.31)^3 = 2.2481\\text{ Å}^3 \\implies 8 \\times \\frac{4}{3}\\pi (2.2481) = 75.34\\text{ Å}^3
\\]
\\[
V_{\\text{ions}} = 23.54 + 75.34 = 98.88\\text{ Å}^3
\\]
Volume of unit cell:
\\[
V_c = (5.463)^3 = 163.04\\text{ Å}^3
\\]
Atomic packing fraction:
\\[
\\text{APF} = \\frac{98.88}{163.04} = 0.6065 = 60.65\\%
\\]
Void volume fraction:
\\[
f_{\\text{void}} = 1 - 0.6065 = 0.3935 = 39.35\\%
\\]

### Step 3: Radius of the Interstitial Vacant Octahedral Void
In $\\text{CaF}_2$, the vacant site at $(1/2, 1/2, 1/2)$ is coordinated by $6\\text{ F}^-$ anions at distances:
Distance from $(1/2, 1/2, 1/2)$ to an adjacent tetrahedral fluoride at $(1/4, 1/4, 1/4)$ is along the body diagonal of a subcube of size $a/2$:
\\[
d_{\\text{void-F}} = \\sqrt{\\left(\\frac{a}{4}\\right)^2 + \\left(\\frac{a}{4}\\right)^2 + \\left(\\frac{a}{4}\\right)^2} = \\frac{\\sqrt{3}}{4} a
\\]
\\[
d_{\\text{void-F}} = \\frac{\\sqrt{3}}{4}(5.463\\text{ Å}) = 2.3655\\text{ Å}
\\]
Since $d_{\\text{void-F}} = r_{\\text{void}} + r_{\\text{F}^-}$:
\\[
r_{\\text{void}} = d_{\\text{void-F}} - r_{\\text{F}^-} = 2.3655 - 1.310 = 1.055\\text{ Å}
\\]
This large empty interstitial cage ($r_{\\text{void}} \\approx 1.06\\text{ Å}$) allows easy transport of fluoride and oxide interstitials, explaining why fluorite structures act as outstanding fast-ion conductors."""
            },
            {
                "probNumber": "5.8",
                "title": "Application of Pauling's Electrostatic Valence Rule to Binary Oxides and Halides",
                "difficulty": "Intermediate",
                "statement": "Apply Pauling's second rule (Electrostatic Valence Rule, $\\sum s_i = z_{\\text{anion}}$) to evaluate the bond valences and structural stability of:\\n(a) Rock salt $\\text{NaCl}$ ($z_{\\text{Na}} = +1, CN = 6$) and $\\text{MgO}$ ($z_{\\text{Mg}} = +2, CN = 6$).\\n(b) Fluorite $\\text{CaF}_2$ ($z_{\\text{Ca}} = +2, CN = 8$) and Rutile $\\text{TiO}_2$ ($z_{\\text{Ti}} = +4, CN = 6$).\\n(c) Explain why an imaginary structure where $\\text{Ti}^{4+}$ has tetrahedral coordination ($CN = 4$) in an oxide with 3-fold coordinated oxygen violates Pauling's Rule 2.",
                "solution": r"""### Step 1: Bond Valence Strength Formulation
Pauling's electrostatic bond valence $s$ is:
\\[
s = \\frac{z_{\\text{cation}}}{CN_{\\text{cation}}}
\\]
For a stable crystal, the sum of bond strengths reaching each anion must satisfy:
\\[
\\sum_{i=1}^{CN_{\\text{anion}}} s_i = |z_{\\text{anion}}|
\\]

### Step 2: Evaluation of Test Structures
1. **Rock Salt $\\text{NaCl}$**:
   - $s = \\frac{+1}{6} = \\frac{1}{6}$
   - Each $\\text{Cl}^-$ is coordinated by $6\\text{ Na}^+$:
   \\[
   \\sum s = 6 \\times \\left(\\frac{1}{6}\\right) = 1.000 = |z_{\\text{Cl}}|
   \\]
   *Strictly satisfied.*

2. **Periclase $\\text{MgO}$**:
   - $s = \\frac{+2}{6} = \\frac{1}{3}$
   - Each $\\text{O}^{2-}$ is coordinated by $6\\text{ Mg}^{2+}$:
   \\[
   \\sum s = 6 \\times \\left(\\frac{1}{3}\\right) = 2.000 = |z_{\\text{O}}|
   \\]
   *Strictly satisfied.*

3. **Fluorite $\\text{CaF}_2$**:
   - $s = \\frac{+2}{8} = \\frac{1}{4}$
   - Each $\\text{F}^-$ is coordinated by $4\\text{ Ca}^{2+}$:
   \\[
   \\sum s = 4 \\times \\left(\\frac{1}{4}\\right) = 1.000 = |z_{\\text{F}}|
   \\]
   *Strictly satisfied.*

4. **Rutile $\\text{TiO}_2$**:
   - $s = \\frac{+4}{6} = \\frac{2}{3}$
   - Each $\\text{O}^{2-}$ is coordinated by $3\\text{ Ti}^{4+}$:
   \\[
   \\sum s = 3 \\times \\left(\\frac{2}{3}\\right) = 2.000 = |z_{\\text{O}}|
   \\]
   *Strictly satisfied.*

### Step 3: Analysis of Hypothetical Case
If $\\text{Ti}^{4+}$ had $CN = 4$ in an oxide where oxygen is 3-fold coordinated:
- Bond strength: $s = \\frac{+4}{4} = 1.0$.
- Oxygen coordination sum:
\\[
\\sum s = 3 \\times 1.0 = 3.0 \\ne 2.0 = |z_{\\text{O}}|
\\]
This creates a severe overbonding of $+1.0$ valence units on oxygen ($50\\%$ excess positive charge), which is electrostatically unviable according to Pauling's second rule."""
            },
            {
                "probNumber": "5.9",
                "title": "Thermodynamics of the NaCl to CsCl Pressure-Induced First-Order Phase Transition",
                "difficulty": "Advanced",
                "statement": "At room temperature, crystalline $\\text{KCl}$ undergoes a first-order polymorphic phase transition from the rock salt structure (B1) to the cesium chloride structure (B2) at hydrostatic pressure $P_{\\text{tr}} = 1.95\\text{ GPa}$.\\n- Molar volume of B1 phase at transition: $V_{\\text{B1}} = 37.50\\text{ cm}^3/\\text{mol}$.\\n- Molar volume of B2 phase at transition: $V_{\\text{B2}} = 33.38\\text{ cm}^3/\\text{mol}$.\\n(a) Calculate the volume discontinuity $\\Delta V_{\\text{tr}}$ and volume strain $\\Delta V/V_{\\text{B1}}$.\\n(b) Compute the mechanical transition work $P \\Delta V_{\\text{tr}}$ in $\\text{kJ/mol}$.\\n(c) Given that the standard internal lattice energy difference is $\\Delta U_{\\text{tr}} = U_{\\text{B2}} - U_{\\text{B1}} = +8.03\\text{ kJ/mol}$, calculate the Gibbs free energy change $\\Delta G_{\\text{tr}}$ at $P = 0$ and at $P = P_{\\text{tr}}$ (assuming negligible $T\\Delta S$).",
                "solution": r"""### Step 1: Volume Discontinuity
Molar volumes:
\\[
V_{\\text{B1}} = 37.50\\text{ cm}^3/\\text{mol} = 3.750 \\times 10^{-5}\\text{ m}^3/\\text{mol}
\\]
\\[
V_{\\text{B2}} = 33.38\\text{ cm}^3/\\text{mol} = 3.338 \\times 10^{-5}\\text{ m}^3/\\text{mol}
\\]
Volume change:
\\[
\\Delta V_{\\text{tr}} = V_{\\text{B2}} - V_{\\text{B1}} = 33.38 - 37.50 = -4.12\\text{ cm}^3/\\text{mol} = -4.12 \\times 10^{-6}\\text{ m}^3/\\text{mol}
\\]
Relative volume collapse:
\\[
\\frac{\\Delta V_{\\text{tr}}}{V_{\\text{B1}}} = \\frac{-4.12}{37.50} = -0.1099 = -10.99\\%
\\]

### Step 2: Mechanical Work Term
The work done by the applied pressure during the collapse is:
\\[
P_{\\text{tr}} \\Delta V_{\\text{tr}} = (1.95 \\times 10^9\\text{ Pa})(-4.12 \\times 10^{-6}\\text{ m}^3/\\text{mol}) = -8034\\text{ J/mol} = -8.034\\text{ kJ/mol}
\\]

### Step 3: Gibbs Free Energy Evaluation
The Gibbs free energy is defined as $G = U + PV - TS$.
For this solid-state phase transition at constant $T$, $\\Delta G = \\Delta U + P\\Delta V - T\\Delta S$.
Assuming negligible entropy change ($T\\Delta S \\approx 0$ for high-pressure reconstructive structural transitions):
\\[
\\Delta G(P) \\approx \\Delta U + P \\Delta V
\\]
1. **At Zero Pressure ($P = 0$)**:
\\[
\\Delta G(0) = \\Delta U = +8.03\\text{ kJ/mol} > 0
\\]
Since $\\Delta G > 0$, the B1 (rock salt) phase is thermodynamically stable at ambient pressure.

2. **At Transition Pressure ($P = P_{\\text{tr}} = 1.95\\text{ GPa}$)**:
\\[
\\Delta G(P_{\\text{tr}}) = \\Delta U + P_{\\text{tr}} \\Delta V_{\\text{tr}} = +8.034\\text{ kJ/mol} + (-8.034\\text{ kJ/mol}) = 0.00\\text{ kJ/mol}
\\]
The two phases are in exact thermodynamic equilibrium ($G_{\\text{B1}} = G_{\\text{B2}}$).
Above $1.95\\text{ GPa}$, $P|\\Delta V| > \\Delta U$, rendering $\\Delta G < 0$, which makes the denser B2 ($\\text{CsCl}$) phase the thermodynamically favored ground state."""
            }
        ]
    }
    return u5

if __name__ == '__main__':
    u5 = get_unit_5()
    print("Unit 5 successfully generated:")
    print("Title:", u5["title"])
    print("Sections:", len(u5["sections"]))
    print("Problems:", len(u5["problems"]))
