"""
create_organo_u6.py
Unit 6: pi-Complexes II: Dienes, Polyenes, Metallocenes & Fluxionality
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_6():
    sections = [
        {
            "id": "sec6_1",
            "title": "§6.1 Transition Metal 1,3-Diene Complexes: Cisoid vs. Transoid Coordination & $\\text{Fe}(\\text{CO})_3(\\text{diene})$",
            "content": """Conjugated 1,3-dienes ($\text{C}_4\text{H}_6$) act as 4-electron $\\pi$-donors ($L_2$-type). In the free state, butadiene exists predominantly in the planar *s-trans* conformation (which is $\\approx 12\\text{ kJ/mol}$ lower in energy than the *s-cis* conformer).

### Coordination Geometry and Isomerism:
1. **The *s-cis* (Cisoid) Coordination Mode**:
   - The overwhelming majority of transition metal diene complexes adopt the *s-cis* geometry, coordinating both double bonds to a single metal center.
   - Example: ($\\eta^4-s-\\text{cis-1,3-butadiene})\\text{Fe}(\\text{CO})_3$, prepared by thermal or photochemical reaction of butadiene with $\\text{Fe}(\\text{CO})_5$.
   - The metal $d$-orbitals interact with all four carbon $2p_z$ orbitals:
     - $\\psi_1$ ($1a$): $\\sigma$-donation into empty metal $d_{z^2}/s$.
     - $\\psi_2$ ($1b$): $\\pi$-donation into metal $d_{xz}/p_x$.
     - $\\psi_3$ ($2a$): accepts $\\pi$-backdonation from filled metal $d_{yz}$.
   - Extensive backdonation into $\\psi_3$ shortens the central $C_2-C_3$ bond and lengthens the terminal $C_1-C_2$ and $C_3-C_4$ bonds, yielding structural intermediate character between a neutral $\\eta^4$-diene and a $\\sigma^2,\\pi$-metallacyclopentene.
2. **The *s-trans* (Transoid) Coordination Mode**:
   - Extremely rare; observed primarily for early transition metals with large covalent radii ($\text{Zr}, \\text{Hf}$) or bridging two distinct metal centers:
     \\[ Cp_2\\text{Zr}(\\eta^4-s-\\text{trans-butadiene}) \\]
   - The *s-cis* and *s-trans* isomers interconvert via an envelope inversion mechanism."""
        },
        {
            "id": "sec6_2",
            "title": "§6.2 Discovery, Structure and Molecular Orbital Theory of Ferrocene",
            "content": """Ferrocene, bis(cyclopentadienyl)iron $\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_5)_2$, was discovered in 1951 by Kealy and Pauson and independently by Miller. Its revolutionary sandwich architecture—elucidated by Geoffrey Wilkinson and Ernst Otto Fischer—established the foundation of modern organometallic bonding theory.

### Molecular Orbital Construction under $D_{5d}$ (Staggered) Symmetry:
Let the $z$-axis coincide with the fivefold rotational axis passing through the iron atom and the centers of both $Cp$ rings.
1. **Cyclopentadienyl Ligand Group Orbitals (LGOs)**:
   The ten carbon $2p_z$ orbitals of the two parallel $Cp$ rings combine into pairs of in-phase (gerade, $g$) and out-of-phase (ungerade, $u$) LGOs spanning:
   - $a_{1g} + a_{2u}$: zero nodal planes (symmetric combination of ring $\\psi_1$).
   - $e_{1g} + e_{1u}$: one nodal plane (combinations of degenerate ring $\\psi_2, \\psi_3$).
   - $e_{2g} + e_{2u}$: two nodal planes (combinations of ring $\\psi_4, \\psi_5$).
2. **Iron Valence Orbitals**:
   - $4s$ transforms as $a_{1g}$.
   - $4p_z$ transforms as $a_{2u}$; $4p_x, 4p_y$ transform as $e_{1u}$.
   - $3d_{z^2}$ transforms as $a_{1g}$.
   - $3d_{xz}, 3d_{yz}$ transform as $e_{1g}$.
   - $3d_{xy}, 3d_{x^2-y^2}$ transform as $e_{2g}$.
3. **Orbital Mixing and Valence MO Energy Sequence**:
   - **Strongly Bonding MOs**:
     - $1a_{1g}$: overlap of iron $4s/3d_{z^2}$ with $a_{1g}$ LGO.
     - $1a_{2u}$: overlap of iron $4p_z$ with $a_{2u}$ LGO.
     - $1e_{1u}$: overlap of iron $4p_x, 4p_y$ with $e_{1u}$ LGO (twofold degenerate).
     - $1e_{1g}$: overlap of iron $3d_{xz}, 3d_{yz}$ with $e_{1g}$ LGO (twofold degenerate, strongly bonding).
     These six bonding MOs accommodate 12 electrons (ligand-derived).
   - **Frontier MOs**:
     - $a_{1g}'$ ($3d_{z^2}$): largely non-bonding on iron; slightly stabilized or destabilized.
     - $e_{2g}$ ($3d_{xy}, 3d_{x^2-y^2}$): weakly bonding due to overlap with $e_{2g}$ LGOs.
     - The HOMO of ferrocene is $a_{1g}'$ or $e_{2g}$ (depending on ring-metal distance).
     - The LUMO is $e_{1g}^*$, the strongly antibonding counterpart to $1e_{1g}$.
4. **Electronic Saturation**:
   With $\\text{Fe}(\\text{II})$ ($d^6$) and two $Cp^-$ ($6\\pi$ electrons each), exactly **18 valence electrons** populate the six bonding and three non-bonding/weakly bonding orbitals:
   \\[ (1a_{1g})^2 (1a_{2u})^2 (1e_{1u})^4 (1e_{1g})^4 \\; [12\\text{e}] \\; (e_{2g})^4 (a_{1g}')^2 \\; [6\\text{e}] \\]
   The large energy gap to the empty $e_{1g}^*$ LUMO explains the extraordinary chemical stability, diamagnetism, and resistance to oxidation of ferrocene."""
        },
        {
            "id": "sec6_3",
            "title": "§6.3 Electronic Structures of Other Metallocenes: Cobaltocene, Nickelocene & Chromocene",
            "content": """First-row transition metals from vanadium to nickel form neutral bis(cyclopentadienyl) complexes $Cp_2 M$, whose physical properties are governed by electron population within the ferrocene molecular orbital manifold:

1. **Chromocene ($Cp_2\\text{Cr}$, 16 Valence Electrons)**:
   - Chromium is Group 6 ($d^4$). Total electrons: $4 + 2(6) = 16$.
   - Configuration: $(e_{2g})^3 (a_{1g}')^1$.
   - By Hund's rule, two unpaired electrons occupy the degenerate $e_{2g}$ and $a_{1g}'$ levels, giving a **triplet ground state ($S = 1, \\mu_{eff} \\approx 2.8\\ \\mu_B$)**. Highly air-sensitive.
2. **Manganocene ($Cp_2\\text{Mn}$, 17 Valence Electrons)**:
   - Manganese is Group 7 ($d^5$). Total electrons: 17.
   - Ground state displays spin crossover: in non-polar media, it is high-spin ($S = 5/2, \\mu_{eff} \\approx 5.9\\ \\mu_B$) with ionic bonding character, forming a zigzag polymer in the solid state.
3. **Cobaltocene ($Cp_2\\text{Co}$, 19 Valence Electrons)**:
   - Cobalt is Group 9 ($d^7$). Total electrons: $7 + 12 = 19$.
   - The 19th electron must occupy the strongly metal-ring antibonding $e_{1g}^*$ orbital:
     \\[ \\text{Configuration: } \\dots (e_{2g})^4 (a_{1g}')^2 (e_{1g}^*)^1 \\]
   - Paramagnetic ($S = 1/2, \\mu_{eff} = 1.73\\ \\mu_B$).
   - Extremely easily oxidized ($E_{1/2} = -1.33\\text{ V}$ vs $\\text{Fc}^+/\\text{Fc}$) to the stable, diamagnetic 18-electron cobaltocenium cation $[Cp_2\\text{Co}]^+$.
4. **Nickelocene ($Cp_2\\text{Ni}$, 20 Valence Electrons)**:
   - Nickel is Group 10 ($d^8$). Total electrons: $8 + 12 = 20$.
   - Two electrons occupy the degenerate $e_{1g}^*$ antibonding orbitals:
     \\[ \\text{Configuration: } \\dots (e_{2g})^4 (a_{1g}')^2 (e_{1g}^*)^2 \\]
   - Triplet ground state ($S = 1, \\mu_{eff} = 2.83\\ \\mu_B$).
   - Population of two antibonding electrons weakens and lengthens the $Ni-Cp$ bond ($2.18$ Å vs $2.06$ Å in ferrocene), making nickelocene kinetically labile and susceptible to ring displacement reactions."""
        },
        {
            "id": "sec6_4",
            "title": "§6.4 Bent Metallocenes of Early Transition Metals: Titanocene & Zirconocene Dichloride",
            "content": """Early transition metals (Groups 4 and 5) cannot accommodate parallel sandwich geometry with additional ligands without exceeding spatial and electronic limits. Instead, they form **bent metallocenes**:
\\[ Cp_2 M X_2 \\quad (M = \\text{Ti, Zr, Hf};\\, X = \\text{halide, alkyl, hydride}) \\]

### Electronic and Geometric Structure:
- The two $Cp$ rings are tilted away from parallel by a centroid-metal-centroid angle of **$\\theta \\approx 130^\\circ - 136^\\circ$**.
- Tilted rings open a coordination wedge on the opposite side of the metal with three frontier molecular orbitals directed into the open wedge:
  - $1a_1$: lowest in energy, strongly interacting with the two $X$ ligands.
  - $b_2$: in-plane orbital, interacts with the out-of-phase combination of $X$ orbitals.
  - $2a_1$: empty non-bonding orbital pointing directly into the equatorial wedge.
- In **zirconocene dichloride** $Cp_2\\text{ZrCl}_2$:
  - Zirconium is in formal oxidation state $+4$ ($d^0$).
  - Total valence electrons: $4 (\\text{Zr}) + 2 \\times 5 (Cp) + 2 \\times 1 (\\text{Cl}) = \\mathbf{16\\text{ electrons}}$.
  - The $2a_1$ orbital remains completely vacant, functioning as a powerful Lewis acidic site that coordinates olefins during polymerization catalysis.

### Schwartz's Reagent: $Cp_2\\text{Zr}(\\text{H})\\text{Cl}$:
Zirconocene hydridochloride undergoes **hydrozirconation** across alkenes and alkynes with $>99\\%$ *syn*-stereospecificity, rapidly isomerizing internal alkenes to the sterically least hindered terminal alkylzirconium species."""
        },
        {
            "id": "sec6_5",
            "title": "§6.5 Aromaticity and Chemical Reactivity of Ferrocene: EAS & Redox Chemistry",
            "content": """Ferrocene is an exceptionally electron-rich aromatic system, undergoing **Electrophilic Aromatic Substitution (EAS)** at rates $3 \\times 10^6$ times faster than benzene.

### Aromatic Transformations:
1. **Friedel-Crafts Acylation**:
   \\[ Cp_2\\text{Fe} + \\text{CH}_3\\text{COCl} \\xrightarrow{\\text{AlCl}_3} (\\eta^5-\\text{C}_5\\text{H}_5)\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_4\\text{COCH}_3) + \\text{HCl} \\]
   Because the acyl group is electron-withdrawing, a second acylation occurs exclusively on the **other unfunctionalized ring**, yielding $1,1'$-diacetylferrocene.
2. **Mannich Reaction (Aminomethylation)**:
   \\[ Cp_2\\text{Fe} + \\text{HCHO} + \\text{HNMe}_2 \\xrightarrow{\\text{HOAc}} Cp\\text{Fe}(\\text{C}_5\\text{H}_4\\text{CH}_2\\text{NMe}_2) \\quad (\\text{dimethylaminomethylferrocene}) \\]
3. **Lithiation**:
   Reaction with $n$-butyllithium and TMEDA cleanly deprotonates the $Cp$ rings to generate monolithioferrocene or $1,1'$-dilithioferrocene, key precursors for phosphine ligands like dppf ($1,1'$-bis(diphenylphosphino)ferrocene).

### Reversible One-Electron Electrochemistry:
Ferrocene undergoes an ideal, chemically reversible one-electron oxidation:
\\[ Cp_2\\text{Fe} \\rightleftharpoons [Cp_2\\text{Fe}]^+ + e^- \\quad (E^\\circ = +0.40\\text{ V vs. NHE}) \\]
The resulting blue ferrocenium cation $[Cp_2\\text{Fe}]^+$ is a stable 17-electron radical ($S = 1/2$). Because of its ideal electrochemical reversibility and solvent independence, the ferrocene/ferrocenium couple is recommended by IUPAC as the international reference standard for redox potentials in non-aqueous electrochemistry."""
        },
        {
            "id": "sec6_6",
            "title": "§6.6 Transition Metal Arene Complexes: $(\eta^6-\\text{Benzene})\\text{Cr}(\\text{CO})_3$ & Nucleophilic Addition",
            "content": """Transition metal arene complexes feature a neutral aromatic hydrocarbon bound in a hexahapto mode ($\eta^6-\\text{arene}$), donating 6 $\\pi$-electrons ($L_3$-type).

### Synthesis of Arene Complexes:
1. **Fischer-Hafner Synthesis**: Reaction of metal halides with aromatics in the presence of $\\text{AlCl}_3$ and aluminum powder:
   \\[ 3\\,\\text{CrCl}_3 + 2\\,\\text{Al} + \\text{AlCl}_3 + 6\\,\\text{C}_6\\text{H}_6 \\longrightarrow 3\\,[(\\eta^6-\\text{C}_6\\text{H}_6)_2\\text{Cr}]^+ [\\text{AlCl}_4]^- \\xrightarrow{\\text{dithionite}} (\\eta^6-\\text{C}_6\\text{H}_6)_2\\text{Cr} \\]
   Bis(benzene)chromium is a sandwich complex possessing 18 valence electrons ($6 + 2 \\times 6 = 18$).
2. **Direct Thermal Ligand Substitution**:
   \\[ \\text{Cr}(\\text{CO})_6 + \\text{C}_6\\text{H}_6 \\xrightarrow{\\Delta} (\\eta^6-\\text{C}_6\\text{H}_6)\\text{Cr}(\\text{CO})_3 + 3\\,\\text{CO} \\uparrow \\]

### Chemical Reactivity Modulation of Coordinated Arenes:
Coordination of benzene to the strongly electron-withdrawing $\\text{Cr}(\\text{CO})_3$ fragment completely alters its reactivity:
1. **Enhanced Carbon Acidity**: The $\\text{p}K_a$ of benzene protons drops by $\\approx 10$ units, permitting clean deprotonation by $n\\text{-BuLi}$ at low temperature to yield $(\\eta^6-\\text{phenyllithium})\\text{Cr}(\\text{CO})_3$.
2. **Nucleophilic Aromatic Addition**: Coordinated arenes are strongly electrophilic. Carbon nucleophiles (e.g., alkyllithiums, enolates) attack the ring to generate an anionic $(\\eta^5-\\text{cyclohexadienyl})$ complex:
   \\[ (\\eta^6-\\text{Ar})\\text{Cr}(\\text{CO})_3 + R^- \\longrightarrow [(\\eta^5-\\text{Ar}-R)\\text{Cr}(\\text{CO})_3]^- \\xrightarrow{\\text{I}_2} R-\\text{Ar} + \\text{Cr}^{3+} \\]
   Oxidation with iodine demetallates the complex, delivering alkylated aromatic compounds."""
        },
        {
            "id": "sec6_7",
            "title": "§6.7 Dynamic Fluxionality and Stereochemical Non-Rigidity: Berry Pseudorotation",
            "content": """Many organometallic complexes undergo rapid, intramolecular degenerate rearrangements where atoms or groups permute among non-equivalent structural sites without bond cleavage, a phenomenon termed **stereochemical non-rigidity** or **fluxionality**.

### Berry Pseudorotation in 5-Coordinate Carbonyls:
In trigonal bipyramidal ($D_{3h}$) complexes such as iron pentacarbonyl $\\text{Fe}(\\text{CO})_5$:
- Static geometry contains two axial CO ligands ($180^\\circ$ apart) and three equatorial CO ligands ($120^\\circ$ apart) in a $2:3$ ratio.
- However, at all temperatures down to $-100^\\circ\\text{C}$, the $^{13}\\text{C}$ NMR spectrum displays a single sharp resonance.
- **R. Stephen Berry's Mechanism**:
  1. One equatorial ligand acts as a 'pivot' while the other two equatorial ligands and the two axial ligands bend concertedly.
  2. The axial-metal-axial angle compresses from $180^\\circ$ to $120^\\circ$, while the equatorial-metal-equatorial angle opens from $120^\\circ$ to $180^\\circ$.
  3. The molecule passes through a square pyramidal ($C_{4v}$) transition state:
     \\[ \\text{TBP } (D_{3h}) \\rightleftharpoons \\text{Square Pyramidal } (C_{4v})^\\ddagger \\rightleftharpoons \\text{TBP } (D_{3h})' \\]
  4. The formerly axial ligands become equatorial, and the formerly equatorial ligands become axial.
  5. The activation barrier is extraordinarily low: $\\Delta G^\\ddagger < 8\\text{ kJ/mol}$, making site exchange occur over $10^9$ times per second at room temperature.

### Turnstile Rotation:
An alternative degenerate exchange mechanism involving the concerted rotation of a pair of ligands relative to a trio of ligands around a local threefold axis."""
        },
        {
            "id": "sec6_8",
            "title": "§6.8 Ring-Whizzing Dynamics in $(\eta^1-\\text{Cp})$ Complexes & NMR Coalescence Analysis",
            "content": """When a cyclopentadienyl ring is bound in a monohapto mode ($\eta^1-\\text{Cp}$), the complex exhibits dynamic **ring-whizzing** (metallotropic rearrangement).

### Prototypical Case: $(\\eta^1-\\text{Cp})(\\eta^5-\\text{Cp})\\text{Fe}(\\text{CO})_2$:
- The $\\eta^5-Cp$ ring is locked in pentahapto coordination, appearing as a sharp $5\\text{H}$ singlet at $\\delta \\approx 4.4\\text{ ppm}$.
- The $\\eta^1-Cp$ ring is a localized diene attached by a single $M-\\text{C}$ $\\sigma$-bond. In the static low-temperature limit ($-100^\\circ\\text{C}$):
  - H1 ($\alpha$-proton): $1\\text{H}$ at $\\delta \\approx 3.5\\text{ ppm}$.
  - H2, H5 ($\beta$-protons): $2\\text{H}$ at $\\delta \\approx 6.0\\text{ ppm}$.
  - H3, H4 ($\gamma$-protons): $2\\text{H}$ at $\\delta \\approx 6.3\\text{ ppm}$.
- As temperature rises, the metal atom migrates rapidly around the perimeter of the 5-membered ring:
  \\[ M-\\text{C}1 \\longrightarrow M-\\text{C}2 \\longrightarrow M-\\text{C}3 \\longrightarrow M-\\text{C}4 \\longrightarrow M-\\text{C}5 \\]
  At room temperature, the three signals coalesce into a single sharp $5\\text{H}$ singlet at $\\delta \\approx 5.7\\text{ ppm}$.

### Discrimination Between [1,2]-Shift and [1,3]-Shift:
1. **[1,2]-Metallotropic Shift Mechanism**:
   The metal migrates to an adjacent carbon atom. In variable-temperature line-shape analysis, the $\\beta$- and $\\gamma$-resonances broaden at **different rates** because a [1,2]-shift exchanges H1 with H2 faster than with H3.
2. **[1,3]-Metallotropic Shift Mechanism**:
   The metal jumps across the ring. This would exchange H1 with H3 first.
- Careful line-shape simulation and Eyring analysis (Cotton, Whitesides) proved that ring-whizzing proceeds exclusively via a **least-motion [1,2]-shift** with an activation barrier of $\\Delta G^\\ddagger \\approx 42-50\\text{ kJ/mol}$."""
        }
    ]

    problems = [
        {
            "id": "prob6_1",
            "tier": "Foundational",
            "title": "Molecular Orbital Symmetry Analysis of Ferrocene",
            "statement": "In the staggered ($D_{5d}$) conformation of ferrocene $\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_5)_2$: (a) Classify the nine valence atomic orbitals of iron into their irreducible representations under $D_{5d}$. (b) Identify the ligand group orbitals (LGOs) that match each iron orbital. (c) Identify which iron $d$-orbitals form the highest occupied molecular orbitals (HOMO) and which forms the lowest unoccupied molecular orbital (LUMO).",
            "solution": """**Line-by-Line Solution:**

**(a) Symmetry Classification of Iron Valence Orbitals in $D_{5d}$:**
Under $D_{5d}$ point group symmetry:
1. **$4s$ orbital**: Totally symmetric with respect to all operations $\\implies \\mathbf{a_{1g}}$.
2. **$4p$ orbitals**:
   - $4p_z$ lies along the $C_5$ axis, antisymmetric to inversion $i$ $\\implies \\mathbf{a_{2u}}$.
   - $4p_x, 4p_y$ lie in the perpendicular plane $\\implies \\mathbf{e_{1u}}$ (twofold degenerate).
3. **$3d$ orbitals**:
   - $3d_{z^2}$ is symmetric with respect to $C_5$ and inversion $i$ $\\implies \\mathbf{a_{1g}}$.
   - $3d_{xz}, 3d_{yz}$ have one nodal plane containing the $z$-axis, symmetric to inversion $\\implies \\mathbf{e_{1g}}$ (twofold degenerate).
   - $3d_{xy}, 3d_{x^2-y^2}$ have two nodal planes, symmetric to inversion $\\implies \\mathbf{e_{2g}}$ (twofold degenerate).

**(b) Symmetry-Matched Ligand Group Orbitals (LGOs):**
The ten carbon $2p_z$ orbitals from two $Cp$ rings span:
\\[ \\Gamma_\\text{LGO} = a_{1g} + a_{2u} + e_{1g} + e_{1u} + e_{2g} + e_{2u} \\]
Matching pairs:
- Iron $4s$ and $3d_{z^2}$ ($a_{1g}$) $\\longleftrightarrow a_{1g}$ LGO (strongly bonding $\\sigma$).
- Iron $4p_z$ ($a_{2u}$) $\\longleftrightarrow a_{2u}$ LGO.
- Iron $4p_x, 4p_y$ ($e_{1u}$) $\\longleftrightarrow e_{1u}$ LGO.
- Iron $3d_{xz}, 3d_{yz}$ ($e_{1g}$) $\\longleftrightarrow e_{1g}$ LGO (strongly bonding $\\pi$).
- Iron $3d_{xy}, 3d_{x^2-y^2}$ ($e_{2g}$) $\\longleftrightarrow e_{2g}$ LGO (weakly bonding $\\delta$).
- The $e_{2u}$ LGO has no matching metal valence orbital and remains non-bonding ligand-centered.

**(c) Frontier Molecular Orbitals (HOMO and LUMO):**
- **HOMO**: The metal $3d$ orbitals that do not engage in strong $\\sigma$- or $\\pi$-bonding are:
  - $a_{1g}'$ (predominantly $3d_{z^2}$, non-bonding).
  - $e_{2g}$ (predominantly $3d_{xy}, 3d_{x^2-y^2}$, weakly bonding).
  - Both levels are completely occupied by the 6 valence electrons of $\\text{Fe}(\\text{II})$ ($d^6$).
  - In gas-phase photoelectron spectroscopy and high-level DFT calculations, the HOMO is the degenerate **$e_{2g}$** level (or closely spaced with $a_{1g}'$).
- **LUMO**: The lowest unoccupied molecular orbital is the **$e_{1g}^*$ level**, which is the strongly antibonding partner formed from iron $3d_{xz}, 3d_{yz}$ and the $e_{1g}$ LGO.
- The large HOMO-LUMO gap between $a_{1g}'/e_{2g}$ and $e_{1g}^*$ accounts for ferrocene's closed-shell 18e stability."""
        },
        {
            "id": "prob6_2",
            "tier": "Foundational",
            "title": "Electrophilic Aromatic Substitution Regiochemistry in Ferrocene",
            "statement": "When ferrocene is reacted with excess acetic anhydride in the presence of phosphoric acid: (a) Identify the major monoacylated product and the major diacylated product. (b) Explain why the second acylation occurs exclusively on the unfunctionalized ring ($1,1'$-diacetylferrocene) rather than the already substituted ring ($1,2$- or $1,3$-diacetylferrocene). (c) State why ferrocene cannot be directly nitrated with nitric acid/sulfuric acid.",
            "solution": """**Line-by-Line Solution:**

**(a) Identification of Products:**
1. **Monoacylated Product**: Acetylferrocene, $(\\eta^5-\\text{C}_5\\text{H}_5)\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_4\\text{COCH}_3)$.
2. **Diacylated Product**: $1,1'$-Diacetylferrocene, $\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_4\\text{COCH}_3)_2$, where each cyclopentadienyl ring carries exactly one acetyl group.

**(b) Regiochemical Rationale for $1,1'$-Substitution:**
1. The acetyl group ($-\\text{COCH}_3$) is a strong **electron-withdrawing group** via both resonance ($-M$) and induction ($-I$).
2. In the monoacetylated product $(\\text{C}_5\\text{H}_5)\\text{Fe}(\\text{C}_5\\text{H}_4\\text{COCH}_3)$, introduction of the acetyl group withdraws electron density from the functionalized $Cp$ ring, deactivating it toward further electrophilic attack.
3. Although the metal center transmits some inductive deactivation across to the opposite ring, the second unfunctionalized cyclopentadienyl ring retains substantially greater electron density than the deactivated ring:
   \\[ \\rho_\\text{elec}(\\text{unfunctionalized ring}) \\gg \\rho_\\text{elec}(\\text{acetylated ring}) \\]
4. Therefore, the incoming acetyl cation electrophile $\\text{CH}_3\\text{C}\\equiv\\text{O}^+$ attacks the second, more nucleophilic $Cp$ ring exclusively, yielding **$1,1'$-diacetylferrocene** as the sole diacylated isomer ($>99\\%$).

**(c) Failure of Direct Nitration with Nitric/Sulfuric Acid:**
- The standard nitrating mixture ($\\text{HNO}_3/\\text{H}_2\\text{SO}_4$) contains the powerful oxidizing agent $\\text{NO}_2^+$ and strong acid.
- Because ferrocene possesses a low oxidation potential ($E_{1/2} = +0.40\\text{ V}$), it undergoes rapid, instantaneous **one-electron oxidation** to the blue ferrocenium cation $[Cp_2\\text{Fe}]^+$ rather than electrophilic substitution:
  \\[ Cp_2\\text{Fe} + \\text{HNO}_3 \\longrightarrow [Cp_2\\text{Fe}]^+ + \\text{NO}_2 + \\text{H}_2\\text{O} \\]
- The resulting ferrocenium cation carries a full positive charge and is a 17-electron open-shell species, completely deactivated toward electrophilic attack. Prolonged exposure to oxidizing acids destroys the metallocene, precipitating iron(III) oxide."""
        },
        {
            "id": "prob6_3",
            "tier": "Foundational",
            "title": "Berry Pseudorotation Mechanism and Dynamic NMR of $\\text{Fe}(\\text{CO})_5$",
            "statement": "Iron pentacarbonyl $\\text{Fe}(\\text{CO})_5$ adopts a trigonal bipyramidal ($D_{3h}$) ground-state structure. (a) State the ideal coordination numbers and symmetry-distinct environments for CO ligands in this structure. (b) Explain why only a single $^{13}\\text{C}$ NMR resonance is observed down to $-100^\\circ\\text{C}$. (c) Describe the geometric coordinate transformation during Berry pseudorotation.",
            "solution": """**Line-by-Line Solution:**

**(a) Ideal Static Structure ($D_{3h}$ Symmetry):**
- In trigonal bipyramidal $\\text{Fe}(\\text{CO})_5$:
  - Two **axial carbonyls** ($\text{CO}_\\text{ax}$): Collinear along the threefold principal $z$-axis with $\\angle(\\text{C}_\\text{ax}-\\text{Fe}-\\text{C}_\\text{ax}) = 180^\\circ$.
  - Three **equatorial carbonyls** ($\text{CO}_\\text{eq}$): Reside in the horizontal mirror plane with $\\angle(\\text{C}_\\text{eq}-\\text{Fe}-\\text{C}_\\text{eq}) = 120^\\circ$.
- The two environments are chemically non-equivalent, with an expected integration ratio of **$2 : 3$** (two distinct NMR signals).

**(b) Single $^{13}\\text{C}$ Resonance Down to $-100^\\circ\\text{C}$:**
- The molecule is **stereochemically non-rigid (fluxional)**.
- At all accessible temperatures in solution, the rate of intramolecular exchange between axial and equatorial sites $k_\\text{exchange}$ is vastly greater than the NMR chemical shift frequency separation $\\Delta \\nu$:
  \\[ k_\\text{exchange} \\gg \\Delta \\nu \\]
- Because exchange occurs faster than the NMR timescale ($>10^8\\text{ s}^{-1}$ even at $-100^\\circ\\text{C}$), the spectrometer records a single time-averaged resonance reflecting the weighted average chemical shift:
  \\[ \\delta_\\text{avg} = \\frac{2}{5}\\delta_\\text{ax} + \\frac{3}{5}\\delta_\\text{eq} \\approx 209\\text{ ppm} \\]

**(c) Geometric Coordinate Transformation of Berry Pseudorotation:**
1. Choose one equatorial carbonyl ligand as the fixed **pivot ligand**.
2. The remaining two equatorial ligands and the two axial ligands participate in a concerted, pairwise vibration:
   - The two axial ligands bend toward each other in their plane, closing their bond angle from $180^\\circ$ down to $120^\\circ$.
   - Simultaneously, the two non-pivot equatorial ligands open their bond angle from $120^\\circ$ up to $180^\\circ$.
3. At the halfway point, the molecule attains a **square pyramidal ($C_{4v}$) transition state** with the pivot ligand at the apex.
4. Continuing through this vibrational coordinate produces a new trigonal bipyramid rotated by $90^\\circ$ relative to the original, wherein the formerly axial ligands now occupy equatorial positions, and the formerly equatorial ligands occupy axial positions.
5. The activation barrier for this motion is remarkably low ($\\Delta G^\\ddagger < 8\\text{ kJ/mol}$), rendering the process barrier-free under ambient conditions."""
        },
        {
            "id": "prob6_4",
            "tier": "Intermediate",
            "title": "Thermodynamics and Spin Crossover in Manganocene ($Cp_2\\text{Mn}$)",
            "statement": "Manganocene $Cp_2\\text{Mn}$ exhibits an effective magnetic moment of $\\mu_{eff} = 5.90\\ \\mu_B$ at $300\\text{ K}$, which drops sharply to $1.85\\ \\mu_B$ in the presence of dimethylphosphinoethane (dmpe) or in coordinating matrices. (a) Calculate the number of unpaired electrons corresponding to both magnetic states. (b) Rationalize the high-spin ground state of uncoordinated $Cp_2\\text{Mn}$ versus the low-spin ground state of ferrocene using ligand field theory and the mean pairing energy $P$. (c) Explain why $Cp_2\\text{Mn}$ reacts instantly with water to release cyclopentadiene while ferrocene is completely inert.",
            "solution": """**Line-by-Line Solution:**

**(a) Unpaired Electrons for Both Magnetic States:**
The spin-only magnetic moment is given by:
\\[ \\mu_{so} = \\sqrt{n(n+2)}\\,\\mu_B = 2\\sqrt{S(S+1)}\\,\\mu_B \\]
1. **For $\\mu_{eff} = 5.90\\ \\mu_B$**:
   \\[ 5.90 = \\sqrt{n(n+2)} \\implies n(n+2) \\approx 34.8 \\implies n = 5 \\]
   Corresponds to **$S = 5/2$ (five unpaired electrons)**, high-spin $d^5$ configuration ($a_{1g}^1 e_{2g}^2 e_{1g}^{*2}$).
2. **For $\\mu_{eff} = 1.85\\ \\mu_B$**:
   \\[ 1.85 = \\sqrt{n(n+2)} \\implies n(n+2) \\approx 3.42 \\implies n = 1 \\]
   Corresponds to **$S = 1/2$ (one unpaired electron)**, low-spin $d^5$ configuration ($a_{1g}^1 e_{2g}^4 e_{1g}^{*0}$).

**(b) Ligand Field Splitting ($\\Delta$) vs. Pairing Energy ($P$):**
- In metallocenes, the orbital splitting between the non-bonding $a_{1g}'/e_{2g}$ manifold and the antibonding $e_{1g}^*$ manifold defines the effective ligand field parameter $\\Delta$.
- In $\\text{Fe}(\\text{II})$ ($Cp_2\\text{Fe}$):
  - Iron has higher nuclear charge ($Z=26$), pulling $3d$-orbitals closer, yielding strong covalent overlap with $Cp$ $e_{1g}$ LGOs.
  - This generates a massive splitting $\\Delta \\approx 26,000\\text{ cm}^{-1}$.
  - Because $\\Delta \\gg P$ (pairing energy $\\approx 15,000\\text{ cm}^{-1}$), ferrocene is forced into a **low-spin, diamagnetic closed-shell state ($S=0$)**.
- In $\\text{Mn}(\\text{II})$ ($Cp_2\\text{Mn}$):
  - Manganese has lower nuclear charge ($Z=25$), larger ionic radius, and a half-filled $d^5$ shell.
  - The $Mn-Cp$ covalent interaction is significantly weaker, yielding a smaller splitting: $\\Delta \\approx 12,000\\text{ cm}^{-1}$.
  - Because $\\Delta < P$, the complex minimizes electron-electron repulsion by populating all five $d$-orbitals singly, adopting a **high-spin configuration ($S = 5/2$)**.

**(c) Instant Hydrolysis of Manganocene vs. Inertness of Ferrocene:**
- In ferrocene, the 18 valence electrons completely fill strongly bonding and non-bonding orbitals, creating a tightly held covalent framework with zero vacant orbitals and high activation energy toward ligand substitution.
- In manganocene, two electrons reside in strongly antibonding $e_{1g}^*$ orbitals, and the bonding is predominantly **electrostatic/ionic** ($[\\text{Mn}^{2+}][(Cp^-)_2]$).
- In polar/protic media, water coordinates readily to the high-spin $\\text{Mn}^{2+}$ ion, displacing the ionic $Cp^-$ rings.
- Rapid proton transfer yields insoluble manganese(II) hydroxide and free cyclopentadiene:
  \\[ Cp_2\\text{Mn} + 2\\,\\text{H}_2\\text{O} \\longrightarrow \\text{Mn}(\\text{OH})_2 \\downarrow + 2\\,\\text{C}_5\\text{H}_6 \\uparrow \\]"""
        },
        {
            "id": "prob6_5",
            "tier": "Intermediate",
            "title": "Kinetics of Metallotropic Ring-Whizzing in $(\\eta^1-\\text{Cp})$ Complexes",
            "statement": "In $(\\eta^1-\\text{C}_5\\text{H}_5)(\\eta^5-\\text{C}_5\\text{H}_5)\\text{Fe}(\\text{CO})_2$, the $\\alpha$-proton (H1) and $\\beta$-protons (H2, H5) of the $\\eta^1-Cp$ ring have a chemical shift difference of $\\Delta \\nu = 420\\text{ Hz}$ at $100\\text{ MHz}$ at $-80^\\circ\\text{C}$. Coalescence occurs at $T_c = -25^\\circ\\text{C} (248.15\\text{ K})$. (a) Calculate the rate constant of ring-whizzing $k_c$ at coalescence. (b) Calculate the activation free energy $\\Delta G^\\ddagger$ for the [1,2]-metallotropic shift. (c) Explain why a [1,2]-shift is symmetry-allowed under Woodward-Hoffmann rules as a suprafacial sigmatropic shift.",
            "solution": """**Line-by-Line Solution:**

**(a) Rate Constant at Coalescence ($k_c$):**
For an exchange between sites of unequal intensity or coupled multiplet systems, the classic Gutowsky-Holm approximation gives:
\\[ k_c = \\frac{\\pi \\Delta \\nu}{\\sqrt{2}} \\]
Given $\\Delta \\nu = 420\\text{ Hz}$:
\\[ k_c = \\frac{3.14159 \\times 420}{1.4142} = \\frac{1319.47}{1.4142} \\approx 933.0\\text{ s}^{-1} \\]

**(b) Activation Free Energy ($\\Delta G^\\ddagger$):**
Using the Eyring equation at $T_c = 248.15\\text{ K}$:
\\[ \\Delta G^\\ddagger = R T_c \\left[ \\ln\\left(\\frac{k_B T_c}{h}\\right) - \\ln(k_c) \\right] \\]
Constants:
- $\\frac{k_B T_c}{h} = \\frac{(1.38065 \\times 10^{-23})(248.15)}{6.62607 \\times 10^{-34}} = 5.170 \\times 10^{12}\\text{ s}^{-1}$
- $\\ln\\left(\\frac{k_B T_c}{h}\\right) = \\ln(5.170 \\times 10^{12}) \\approx 29.274$
- $\\ln(k_c) = \\ln(933.0) \\approx 6.838$
- Difference: $29.274 - 6.838 = 22.436$

Compute $\\Delta G^\\ddagger$:
\\[ \\Delta G^\\ddagger = (8.3145\\text{ J/(mol}\\cdot\\text{K)})(248.15\\text{ K})(22.436) = 2063.2 \\times 22.436 = 46,290\\text{ J/mol} \\approx 46.3\\text{ kJ/mol} \\]
- **Conclusion**: The activation barrier for ring-whizzing is **$46.3\\text{ kJ/mol}$** ($11.1\\text{ kcal/mol}$), fully consistent with a rapid intramolecular process.

**(c) Woodward-Hoffmann Symmetry Analysis:**
- A [1,2]-shift of a transition metal fragment across a cyclopentadienyl ring is classified as a **[1,5]-sigmatropic shift** from the perspective of the diene $\\pi$-system:
  \\[ [\\sigma 2_s + \\pi 4_s] \\]
- The highest occupied molecular orbital of the dienyl system has $4\\pi$ electrons.
- Under orbital symmetry rules, a [1,5]-sigmatropic migration involving a hydrogen atom or a metal center proceeding with retention of configuration at the migrating center is **thermally allowed suprafacially**.
- The metal atom utilizes an orbital of appropriate symmetry to interact simultaneously with C1 and C2 in a low-energy transition state without inverting its own stereocenter, enabling seamless ring-whizzing."""
        },
        {
            "id": "prob6_6",
            "tier": "Intermediate",
            "title": "Nucleophilic Addition to Coordinated Arenes in $(\\eta^6-\\text{Arene})\\text{Cr}(\\text{CO})_3$",
            "statement": "Benzene coordinates to chromium in $(\\eta^6-\\text{C}_6\\text{H}_6)\\text{Cr}(\\text{CO})_3$. (a) Calculate the formal oxidation state of chromium and electron count. (b) Explain why treatment with 2-lithio-2-methylpropionitrile $\\text{Li}[\\text{C}(\\text{Me})_2\\text{CN}]$ in THF yields a cyclohexadienyl intermediate (A). (c) When (A) is treated with iodine ($\\text{I}_2$), the organic product is 2-methyl-2-phenylpropanenitrile. Explain the role of iodine.",
            "solution": """**Line-by-Line Solution:**

**(a) Formal Oxidation State and Electron Count:**
- Benzene is a neutral 6-electron $L_3$ donor.
- Three carbonyl ligands are neutral 2-electron $L$ donors.
- Complex is uncharged: $q = 0$.
\\[ OS(\\text{Cr}) = 0 - 0 = 0 \\implies \\text{Cr}(0) \\implies d^6 \\]
- Valence electron count ($VEC$):
  \\[ VEC = 6 (\\text{Cr}) + 6 (\\text{benzene}) + 3 \\times 2 (\\text{CO}) = \\mathbf{18\\text{ valence electrons}} \\]

**(b) Formation of the Cyclohexadienyl Intermediate (A):**
1. Although free benzene is an electron-rich aromatic nucleophile that never reacts with carbanions, coordination to the tricarbonylchromium fragment changes its electronics.
2. The three CO ligands are powerful $\\pi$-acceptors that withdraw electron density from the chromium center, which in turn withdraws $\\sigma$- and $\\pi$-electron density from the benzene ring.
3. This net electron depletion confers electrophilic character to the coordinated benzene carbons.
4. The carbanion $[\\text{C}(\\text{Me})_2\\text{CN}]^-$ attacks an arene carbon atom directly from the face **opposite to chromium** (exo-attack):
   \\[ (\\eta^6-\\text{C}_6\\text{H}_6)\\text{Cr}(\\text{CO})_3 + [\\text{C}(\\text{Me})_2\\text{CN}]^- \\longrightarrow [(\\eta^5-\\text{C}_6\\text{H}_6-\\text{C}(\\text{Me})_2\\text{CN})\\text{Cr}(\\text{CO})_3]^- \\]
5. The attacked carbon rehybridizes to $sp^3$, converting the $\\eta^6$-arene into an anionic 18-electron **$\\eta^5$-cyclohexadienyl** complex (A).

**(c) Role of Iodine ($\\text{I}_2$) in Oxidative Demetallation:**
1. Intermediate (A) contains an added nucleophile and an $sp^3$ hydrogen atom at the attacked carbon. To restore aromaticity, formal hydride loss and metal cleavage must occur.
2. Iodine acts as a two-electron oxidant:
   \\[ \\text{Cr}(0) + \\text{I}_2 \\longrightarrow \\text{Cr}(\\text{II}) + 2\\,\\text{I}^- \\]
3. Oxidation of the metal center severely weakens chromium-carbon $\\pi$-bonding, labilizing the cyclohexadienyl ligand.
4. Concurrently, loss of the endo-hydrogen atom as a proton (or hydride abstraction by the oxidized metal) restores the fully conjugated $6\\pi$ aromatic sextet.
5. The final product is the substituted aromatic compound **2-methyl-2-phenylpropanenitrile**, isolated in high yield with complete regiocontrol."""
        },
        {
            "id": "prob6_7",
            "tier": "Advanced",
            "title": "Rotational Barrier Calculation in Bent Metallocene Olefin Complexes",
            "statement": "In zirconocene alkene complexes $[Cp_2\\text{Zr}(\\text{PMe}_3)(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}_2)]$, the coordinated ethylene ligand can adopt two orientations in the open wedge: parallel to the $Cp$ centroid-metal-centroid plane or perpendicular to it. (a) Construct the qualitative molecular orbital diagram of the $Cp_2\\text{Zr}$ bent metallocene fragment in the $yz$-plane. (b) Explain why the ethylene double bond aligns strictly in the equatorial wedge plane ($yz$) in the ground state. (c) Derive the angular potential energy function $V(\\phi) = \\frac{V_2}{2}(1 - \\cos 2\\phi)$ for ethylene rotation, and estimate $V_2$ given an experimental rotational coalescence barrier of $\\Delta G^\\ddagger = 75\\text{ kJ/mol}$.",
            "solution": """**Line-by-Line Solution:**

**(a) Molecular Orbitals of the $Cp_2\\text{Zr}$ Bent Metallocene Fragment:**
When two parallel $Cp$ rings are tilted to angle $\\theta \\approx 130^\\circ$ (defining the $yz$-plane as the mirror plane bisecting the wedge):
1. The metal $d$-orbitals split into three frontier orbitals in the equatorial coordination wedge:
   - **$1a_1$**: Low-energy hybrid orbital formed from $d_{z^2}, d_{y^2}$, and $s$, directed along the central axis of the wedge.
   - **$b_2$**: High-energy orbital formed from $d_{yz}$, antisymmetric with respect to the $xz$ bisecting plane, directed sideways within the wedge.
   - **$2a_1$**: Highest orbital formed from $d_{x^2-y^2}$, pointing directly out along the equatorial symmetry axis.
2. In a $d^2$ zirconocene(II) complex $[Cp_2\\text{Zr}(\\text{PMe}_3)]$, the two valence electrons occupy the $1a_1$ orbital.

**(b) In-Plane Orientation of Coordinated Ethylene:**
1. Ethylene coordinates in the wedge:
   - The $\\sigma$-bonding $\\pi_{CC}$ orbital donates into the empty $2a_1$ metal orbital.
   - For $\\pi$-backbonding, filled metal valence density must donate into the empty ethylene $\\pi_{CC}^*$ orbital.
2. The filled metal orbital available for backbonding is $1a_1$ (or $b_2$ if hybridized).
3. If the ethylene $C=C$ axis lies **in the equatorial wedge plane ($yz$)**:
   - The ethylene $\\pi_{CC}^*$ orbital projects perpendicular to the $C=C$ axis and lies directly in the plane of the filled metal $b_2/1a_1$ orbitals.
   - This provides maximum spatial and symmetry overlap for $\\pi$-backdonation:
     \\[ \\langle d_{yz} | \\pi_{CC}^* \\rangle = \\text{Maximum} \\]
4. If the ethylene rotates by $90^\\circ$ (perpendicular to the wedge):
   - The $\\pi_{CC}^*$ orbital projects along the $x$-axis, where the metal has no matching filled orbitals. Backbonding drops to zero, and steric clash with the $Cp$ rings increases.
5. Therefore, the in-plane orientation is the definitive electronic ground state.

**(c) Angular Potential Function and Barrier Estimation:**
1. The twofold rotational potential is:
   \\[ V(\\phi) = \\frac{V_2}{2}(1 - \\cos 2\\phi) \\]
   where $\\phi = 0^\\circ$ is the ground state ($V(0) = 0$) and $\\phi = 90^\\circ$ is the perpendicular transition state:
   \\[ V(90^\\circ) = \\frac{V_2}{2}(1 - \\cos 180^\\circ) = \\frac{V_2}{2}(1 - (-1)) = V_2 \\]
2. Thus, the barrier height $V_2$ corresponds directly to the activation energy for internal rotation:
   \\[ V_2 = \\Delta G^\\ddagger_\\text{rot} = 75\\text{ kJ/mol} \\]
- **Physical Interpretation**: The $75\\text{ kJ/mol}$ barrier represents the net energy lost when metal-to-olefin $\\pi$-backbonding is completely broken at the orthogonal transition state geometry."""
        },
        {
            "id": "prob6_8",
            "tier": "Advanced",
            "title": "Electronic Coupling and Mixed-Valence Classes in Biferrocenyl Cations",
            "statement": "The mixed-valence monocation of biferrocene $[\\text{Fc}-\\text{Fc}]^+$ consists of an $\\text{Fe}(\\text{II})$ center linked to an $\\text{Fe}(\\text{III})$ center. (a) Classify this system according to the Robin-Day scheme (Class I, Class II, Class III). (b) In the near-infrared (NIR) spectrum, an intervalence charge-transfer (IVCT) absorption band appears at $\\nu_\\text{max} = 5200\\text{ cm}^{-1}$ with molar absorptivity $\\epsilon_\\text{max} = 1800\\text{ M}^{-1}\\text{cm}^{-1}$ and half-height bandwidth $\\Delta \\nu_{1/2} = 1200\\text{ cm}^{-1}$. Using Hush theory, calculate the electronic coupling matrix element $H_{AB}$ given an iron-iron internuclear distance of $R = 5.1$ Å. (c) Calculate the reorganization energy $\\lambda$.",
            "solution": """**Line-by-Line Solution:**

**(a) Robin-Day Classification:**
- **Class I**: Zero electronic coupling ($H_{AB} = 0$). The two valences are completely localized with no spectroscopic interaction.
- **Class II**: Moderate electronic coupling ($0 < H_{AB} < \\lambda/2$). The electron is localized on one center in the ground state with a small activation barrier for electron transfer, displaying an intervalence charge-transfer (IVCT) band in the near-infrared.
- **Class III**: Strong electronic coupling ($H_{AB} \\ge \\lambda/2$). The valences are completely delocalized; the complex has a single potential minimum with half-integral oxidation states ($\text{Fe}^{2.5+}-\\text{Fe}^{2.5+}$).
- For $[\\text{Fc}-\\text{Fc}]^+$, experimental Mössbauer and IR spectra show distinct $\\text{Fe}(\\text{II})$ and $\\text{Fe}(\\text{III})$ sites at low temperature that undergo thermally activated electron transfer.
- **Classification**: **Robin-Day Class II** (moderately coupled, valence-trapped).

**(b) Calculation of Electronic Coupling Matrix Element $H_{AB}$ (Hush Theory):**
Hush's formula for Class II mixed-valence systems is:
\\[ H_{AB} = \\frac{2.06 \\times 10^{-2} \\sqrt{\\nu_\\text{max} \\, \\epsilon_\\text{max} \\, \\Delta \\nu_{1/2}}}{R} \\quad (\\text{in cm}^{-1}) \\]
where:
- $\\nu_\\text{max} = 5200\\text{ cm}^{-1}$
- $\\epsilon_\\text{max} = 1800\\text{ M}^{-1}\\text{cm}^{-1}$
- $\\Delta \\nu_{1/2} = 1200\\text{ cm}^{-1}$
- $R = 5.1$ Å (internuclear distance between the two iron nuclei)

1. Compute the product inside the square root:
   \\[ P = \\nu_\\text{max} \\times \\epsilon_\\text{max} \\times \\Delta \\nu_{1/2} = (5200)(1800)(1200) = 1.1232 \\times 10^{10} \\]
2. Compute the square root:
   \\[ \\sqrt{P} = \\sqrt{1.1232 \\times 10^{10}} \\approx 1.0598 \\times 10^5 \\]
3. Substitute into Hush formula:
   \\[ H_{AB} = \\frac{(2.06 \\times 10^{-2})(1.0598 \\times 10^5)}{5.1} = \\frac{2183.2}{5.1} \\approx 428\\text{ cm}^{-1} \\]
In energy units:
\\[ H_{AB} = (428\\text{ cm}^{-1})(0.01196\\text{ kJ/mol per cm}^{-1}) \\approx 5.12\\text{ kJ/mol} \\]

**(c) Reorganization Energy ($\\lambda$):**
In classical Hush theory for symmetric mixed-valence complexes with zero driving force ($\\Delta G^\\circ = 0$):
\\[ h \\nu_\\text{max} = \\lambda \\]
Therefore:
\\[ \\lambda = 5200\\text{ cm}^{-1} = (5200)(0.01196) \\approx 62.2\\text{ kJ/mol} \\]
Verification of Robin-Day Class II boundary condition:
\\[ \\frac{\\lambda}{2} = \\frac{5200}{2} = 2600\\text{ cm}^{-1} \\]
Since $H_{AB} = 428\\text{ cm}^{-1} \\ll 2600\\text{ cm}^{-1}$, the condition $0 < H_{AB} < \\lambda/2$ is strictly satisfied, confirming the Class II assignment."""
        },
        {
            "id": "prob6_9",
            "tier": "Advanced",
            "title": "Quantum Mechanics of the Hapticity Inversion Barrier in Metallocenes",
            "statement": "The thermal interconversion between staggered ($D_{5d}$) and eclipsed ($D_{5h}$) ferrocene has an experimental rotational barrier of $V_0 \\approx 3.8\\text{ kJ/mol}$ in the gas phase. (a) Formulate the rotational Schrödinger equation for the relative torsional angle $\\phi$ of the two cyclopentadienyl rings with potential $V(\\phi) = \\frac{V_0}{2}(1 - \\cos 5\\phi)$. (b) Explain why the eclipsed conformation is lower in energy than the staggered conformation in the gas phase. (c) Calculate the zero-point torsional vibrational frequency $\\omega_0$.",
            "solution": """**Line-by-Line Solution:**

**(a) Rotational Schrödinger Equation:**
Let $\\phi$ be the relative torsional dihedral angle between the two five-membered rings.
The Hamiltonian operator for relative internal ring rotation is:
\\[ \\hat{H} = -\\frac{\\hbar^2}{2 I_\\text{red}} \\frac{d^2}{d\\phi^2} + V(\\phi) \\]
where $I_\\text{red} = \\frac{I_1 I_2}{I_1 + I_2} = \\frac{I_0}{2}$ is the reduced moment of inertia of the two identical $Cp$ rings about the fivefold axis ($I_0 = 5 m_C r_C^2 \\approx 1.8 \\times 10^{-45}\\text{ kg}\\cdot\\text{m}^2$).
The fivefold periodic potential energy function is:
\\[ V(\\phi) = \\frac{V_0}{2}(1 - \\cos 5\\phi) \\]
The stationary-state Schrödinger equation is:
\\[ -\\frac{\\hbar^2}{2 I_\\text{red}} \\frac{d^2 \\psi(\\phi)}{d\\phi^2} + \\frac{V_0}{2}(1 - \\cos 5\\phi) \\psi(\\phi) = E \\psi(\\phi) \\]
This differential equation is a classic **Mathieu equation**.

**(b) Energetic Preference for the Eclipsed ($D_{5h}$) Conformation in Gas Phase:**
1. In classical organic chemistry, staggered conformations are usually favored to minimize steric repulsion between vicinal C-H bonds (as in ethane).
2. However, in ferrocene:
   - The iron-to-ring distance is relatively large ($1.66$ Å), placing the two rings at a separation of **$3.32$ Å**.
   - At this large internuclear distance, steric repulsion between hydrogen atoms on opposite rings is negligible.
3. Instead, electronic bonding dominates:
   - In the eclipsed ($D_{5h}$) conformation, the $e_{1''}$ and $e_{2''}$ LGOs overlap with metal $d$-orbitals with marginally superior phase alignment.
   - High-level ab initio relativistic quantum calculations show that electrostatic attraction between the positively charged iron center ($\text{Fe}^{\\delta+}$) and the carbanionic ring carbon atoms ($\text{C}^{\\delta-}$) slightly favors the eclipsed $D_{5h}$ geometry by **$3.8\\text{ kJ/mol}$** ($0.9\\text{ kcal/mol}$).
4. In the solid state, crystal packing forces easily overcome this tiny barrier, and ferrocene crystallizes in either monoclinic (staggered) or orthorhombic (eclipsed) lattices depending on temperature.

**(c) Zero-Point Torsional Vibrational Frequency ($\\omega_0$):**
For small displacements near the minimum ($\phi \\approx 0$):
\\[ \\cos 5\\phi \\approx 1 - \\frac{(5\\phi)^2}{2} = 1 - \\frac{25 \\phi^2}{2} \\]
Substitute into the potential:
\\[ V(\\phi) \\approx \\frac{V_0}{2} \\left[ 1 - \\left(1 - \\frac{25 \\phi^2}{2}\\right) \\right] = \\frac{25 V_0}{4} \\phi^2 = \\frac{1}{2} k_\\text{tor} \\phi^2 \\]
where the torsional harmonic force constant is:
\\[ k_\\text{tor} = \\frac{25 V_0}{2} \\]
Given $V_0 = 3.8\\text{ kJ/mol} = 3800 / (6.022 \\times 10^{23}) = 6.31 \\times 10^{-21}\\text{ J/molecule}$:
\\[ k_\\text{tor} = \\frac{25(6.31 \\times 10^{-21})}{2} = 7.89 \\times 10^{-20}\\text{ J/rad}^2 \\]
Reduced moment of inertia:
\\[ I_\\text{red} = \\frac{I_0}{2} = 0.9 \\times 10^{-45}\\text{ kg}\\cdot\\text{m}^2 \\]
The classical harmonic frequency $\\omega_0$ is:
\\[ \\omega_0 = \\sqrt{\\frac{k_\\text{tor}}{I_\\text{red}}} = \\sqrt{\\frac{7.89 \\times 10^{-20}}{0.9 \\times 10^{-45}}} = \\sqrt{8.77 \\times 10^{25}} \\approx 9.36 \\times 10^{12}\\text{ rad/s} \\]
In spectroscopic wavenumbers:
\\[ \\tilde{\\nu} = \\frac{\\omega_0}{2\\pi c} = \\frac{9.36 \\times 10^{12}}{2\\pi (3.0 \\times 10^{10}\\text{ cm/s})} = \\frac{9.36 \\times 10^{12}}{1.885 \\times 10^{11}} \\approx \\mathbf{49.7\\text{ cm}^{-1}} \\]
- **Conclusion**: The torsional zero-point oscillation of the cyclopentadienyl rings occurs at **$\\approx 50\\text{ cm}^{-1}$**, directly matching the low-frequency acoustic lattice mode observed by far-infrared spectroscopy."""
        }
    ]

    return {
        "unit_number": 6,
        "title": "pi-Complexes II: Dienes, Polyenes, Metallocenes & Fluxionality",
        "description": "Transition metal diene complexes, cisoid vs transoid coordination, molecular orbital theory and symmetry of ferrocene under D5d, electronic structures of chromocene, cobaltocene, and nickelocene, bent metallocenes of early transition metals, aromatic substitution and reversible electrochemistry of ferrocene, arene-chromium complexes, Berry pseudorotation, and ring-whizzing metallotropic rearrangements.",
        "sections": sections,
        "problems": problems
    }
