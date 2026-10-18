"""
create_organo_u5.py
Unit 5: pi-Complexes I: Alkenes, Alkynes & eta3-Allyl Complexes
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_5():
    sections = [
        {
            "id": "sec5_1",
            "title": "§5.1 The Dewar-Chatt-Duncanson Model for Alkene Coordination: Zeise's Salt",
            "content": """The coordination of unsaturated carbon-carbon double bonds to transition metals was historically established by Zeise's salt, potassium trichloro(ethene)platinate(II) monohydrate:
\\[ \\text{K}[\\text{PtCl}_3(\\eta^2-\\text{C}_2\\text{H}_4)]\\cdot\\text{H}_2\\text{O} \\]
The structure and bonding remained enigmatic until Michael J.S. Dewar (1951) and Joseph Chatt and L.A. Duncanson (1953) formulated the **Dewar-Chatt-Duncanson (DCD) model**:

### Dual Bonding Components:
1. **$\\sigma$-Donation**:
   - The filled bonding $\\pi$-orbital of the alkene ($\pi_{CC}$, HOMO) overlaps with an empty metal valence orbital of matching $\\sigma$-symmetry (e.g., platinum $5d_{x^2-y^2}/6s/6p$ hybrid orbital):
     \\[ M \\xleftarrow{\\quad\\sigma\\quad} (\\eta^2-\\text{C}=\\text{C}) \\]
   - This interaction transfers electron density from the alkene $\\pi$-bond to the metal center.
2. **$\\pi$-Backbonding**:
   - A filled metal $d$-orbital of $\\pi$-symmetry ($5d_{xz}$ or $5d_{yz}$) overlaps with the empty antibonding $\\pi^*$ orbital of the alkene ($\pi_{CC}^*$, LUMO):
     \\[ d_\\pi(M) \\xrightarrow{\\quad\\pi\\quad} \\pi_{CC}^* \\]
   - This interaction backdonates electron density from the metal into the alkene $\\pi^*$ level.

### Geometric Consequences in Zeise's Salt:
- In uncoordinated ethylene, the $C=C$ double bond length is $1.337$ Å, with planar $sp^2$ geometry and all four hydrogens coplanar with the carbon nuclei (dihedral angle $0^\\circ$).
- In Zeise's salt, neutron diffraction reveals:
  - The $C=C$ bond is oriented perpendicular to the $\\text{PtCl}_3$ square plane.
  - The $C-C$ bond lengthens to **$1.375$ Å** due to electron population of the $\\pi^*$ LUMO.
  - The four hydrogen atoms bend back away from the platinum atom by an angle of **$\\alpha \\approx 32.5^\\circ$**, reflecting partial rehybridization of the carbon atoms from $sp^2$ toward $sp^3$."""
        },
        {
            "id": "sec5_2",
            "title": "§5.2 The Continuum from Weak Alkene $\\pi$-Complex to Metallacyclopropane",
            "content": """Alkene-metal bonding does not represent a static, single structural archetype; it spans a continuous spectrum between two limiting resonance extremes:

### 1. The Pure $\\pi$-Complex Limit (Weak Backbonding):
- Prevalent for transition metals in high formal oxidation states, metals with few $d$-electrons, or late metals coordinated to electron-withdrawing coligands (e.g., $\\text{Ag}(\\text{I})$, $\\text{Pd}(\\text{II})$).
- $\\sigma$-donation dominates; $\\pi$-backbonding is minimal.
- The alkene retains essentially planar $sp^2$ geometry; the $C-C$ bond length is only marginally lengthened ($1.34 - 1.37$ Å).
- The metal oxidation state remains unchanged: $M^n(\\eta^2-\\text{alkene})$.

### 2. The Metallacyclopropane Limit (Extense Backbonding):
- Prevalent for electron-rich, low-valent transition metals ($d^8$ or $d^{10}$ centers like $\\text{Pt}(0)$, $\\text{Ni}(0)$, $\\text{Fe}(0)$) or when the alkene bears strongly electron-withdrawing substituents (e.g., tetracyanoethylene TCNE, maleic anhydride).
- Metal-to-alkene $\\pi$-backdonation into $\\pi^*$ is so extensive that the original $C=C$ double bond order drops toward a single bond ($1.48 - 1.52$ Å).
- The two carbon atoms rehybridize completely to **$sp^3$**.
- Two localized, covalent $M-\\text{C}$ $\\sigma$-bonds form, creating a three-membered ring: a **metallacyclopropane**.
- The formal oxidation state of the metal center increases by **$+2$** (e.g., $\\text{Pt}(0) \\to \\text{Pt}(\\text{II})$).

### Quantitative Spectroscopic Indicators:
- **Carbon-13 NMR**: In free ethylene, $\\delta(^{13}\\text{C}) = 123.3\\text{ ppm}$. In $\\text{Pt}(\\text{PPh}_3)_2(\\text{C}_2\\text{H}_4)$, the carbon resonance shifts upfield to **$\\delta = 39.6\\text{ ppm}$**, directly matching the $sp^3$ chemical shift regime of cyclopropane."""
        },
        {
            "id": "sec5_3",
            "title": "§5.3 Dynamic Barriers to Alkene Rotation Around the Metal-Olefin Bond",
            "content": """Coordinated alkenes undergo dynamic internal rotation about the metal-alkene axis ($M-\\text{centroid}$ vector). This rotation is an activated process whose barrier height directly reflects the magnitude of $\\pi$-backbonding.

### Orbital Mechanism of Alkene Rotation:
- Consider an alkene coordinated in the $xy$-plane of a square planar complex.
- **Ground State**: The $C=C$ axis lies perpendicular to the coordination plane ($z$-axis). The alkene $\\pi^*$ orbital is aligned with the filled metal $d_{xz}$ orbital, maximizing $\\pi$-backbonding overlap.
- **Transition State**: Rotating the alkene by $90^\\circ$ aligns the $C=C$ axis parallel to the coordination plane.
  - In this rotated orientation, the alkene $\\pi^*$ orbital can no longer overlap with the $d_{xz}$ orbital.
  - It must instead interact with the metal $d_{xy}$ orbital, which is often involved in in-plane $\\sigma$-bonding to other ligands and lies at a lower energy level, or has inferior overlap.
- Consequently, during the $90^\\circ$ rotation, **$\\pi$-backbonding is severely disrupted**.

### Quantification of Rotational Barriers:
The activation free energy $\\Delta G^\\ddagger_\\text{rot}$ correlates directly with the metal-olefin $\\pi$-backbonding strength:
- In Zeise's salt $[\\text{PtCl}_3(\\text{C}_2\\text{H}_4)]^-$: $\\Delta G^\\ddagger_\\text{rot} \\approx 40-50\\text{ kJ/mol}$ (fast rotation on the NMR timescale at room temperature).
- In electron-rich platinum(0) complexes $[\\text{Pt}(\\text{PPh}_3)_2(\\text{C}_2\\text{H}_4)]$: $\\Delta G^\\ddagger_\\text{rot} > 85\\text{ kJ/mol}$ (rotation is slow at room temperature, yielding distinct, frozen NMR signals).
- In complexes with strongly electron-withdrawing alkenes (e.g., $\\text{Fe}(\\text{CO})_4(\\text{TCNE})$): $\\Delta G^\\ddagger_\\text{rot} > 130\\text{ kJ/mol}$ (rotation is completely locked up to decomposition)."""
        },
        {
            "id": "sec5_4",
            "title": "§5.4 Alkyne Complexes: 2-Electron vs. 4-Electron Donors & Metallacyclopropenes",
            "content": """Alkynes ($R-\\text{C}\\equiv\\text{C}-R$) possess two mutually orthogonal sets of $\\pi$-orbitals: $\\pi_\\parallel$ (parallel to the coordination plane) and $\\pi_\\perp$ (perpendicular to the coordination plane), along with two corresponding sets of antibonding orbitals: $\\pi_\\parallel^*$ and $\\pi_\\perp^*$.

### Coordination Modes:
1. **2-Electron Donor ($L$-type)**:
   - The alkyne donates its $\\pi_\\parallel$ bonding pair to an empty metal $\\sigma$-orbital, while a filled metal $d_\\pi$-orbital backdonates into $\\pi_\\parallel^*$.
   - The orthogonal $\\pi_\\perp$ system remains non-bonding and unperturbed.
   - Example: $[\\text{Pt}(\\text{PPh}_3)_2(Ph\\text{C}\\equiv\\text{C}Ph)]$ (16e or 18e center).
2. **4-Electron Donor ($L_2$- or $LX$-type)**:
   - In electron-deficient early transition metal or high-oxidation state complexes (e.g., $d^0 - d^2$ complexes of $\\text{Mo}, \\text{W}, \\text{Re}$), the metal center possesses **two empty valence orbitals** of appropriate symmetry.
   - The alkyne donates both its $\\pi_\\parallel$ pair and its orthogonal $\\pi_\\perp$ pair into the metal center:
     \\[ M \\xleftarrow{\\quad\\sigma_1\\quad} \\pi_\\parallel \\quad \\text{and} \\quad M \\xleftarrow{\\quad\\sigma_2\\quad} \\pi_\\perp \\]
   - Example: $[\\text{W}(\\text{CO})(Ph\\text{C}\\equiv\\text{C}Ph)_3]$ where each alkyne donates 4 electrons, yielding an 18-electron tungsten center ($6 + 2 + 3 \\times 4 = 20$? No: W(6) + CO(2) + 2(4e alkyne) + 1(2e alkyne) = 18e!).

### Bend-Back Angles and Metallacyclopropene Character:
Upon coordination, the $R-\\text{C}\\equiv\\text{C}$ bond angles bend back from linear ($180^\\circ$) to $130^\\circ-145^\\circ$. Extensive backdonation produces a **metallacyclopropene** intermediate with significant $M-\\text{C}$ double bond character."""
        },
        {
            "id": "sec5_5",
            "title": "§5.5 Synthesis and Electronic Structure of $\\eta^3$-Allyl Complexes",
            "content": """The allyl ligand ($\\text{C}_3\\text{H}_5$) can coordinate in a monohapto mode ($\\eta^1-\\text{allyl}$, 1-electron $X$-donor) or a trihapto mode ($\\eta^3-\\text{allyl}$, 3-electron $LX$-donor).

### Molecular Orbitals of the Free Allyl Fragment:
The three $2p_z$ orbitals of the planar trimethine chain combine into three molecular orbitals:
1. $\\psi_1$ (Bonding, zero nodes): $\\psi_1 = \\frac{1}{2} p_1 + \\frac{1}{\\sqrt{2}} p_2 + \\frac{1}{2} p_3$ (donates to metal $s, p_z, d_{z^2}$).
2. $\\psi_2$ (Non-bonding, one node at C2): $\\psi_2 = \\frac{1}{\\sqrt{2}} p_1 - \\frac{1}{\\sqrt{2}} p_3$ (donates to metal $p_x, d_{xz}$).
3. $\\psi_3$ (Antibonding, two nodes): $\\psi_3 = \\frac{1}{2} p_1 - \\frac{1}{\\sqrt{2}} p_2 + \\frac{1}{2} p_3$ (accepts backdonation from metal $d_{yz}$).

### Primary Synthetic Methods:
1. **Oxidative Addition to Allylic Halides**:
   \\[ \\text{Ni}(\\text{CO})_4 + \\text{H}_2\\text{C}=\\text{CH}-\\text{CH}_2\\text{Cl} \\longrightarrow \\frac{1}{2}\\,[(\\eta^3-\\text{C}_3\\text{H}_5)\\text{Ni}(\\mu-\\text{Cl})]_2 + 4\\,\\text{CO} \\uparrow \\]
   \\[ \\text{PdCl}_2 + \\text{allyl alcohol} \\xrightarrow{\\text{CO, MeOH}} [(\\eta^3-\\text{C}_3\\text{H}_5)\\text{Pd}(\\mu-\\text{Cl})]_2 \\]
2. **Nucleophilic Attack on 1,3-Dienes**:
   \\[ [(\\eta^4-\\text{butadiene})\\text{Co}(\\text{CO})_3]^+ + \\text{H}^- \\longrightarrow (\\eta^3-\\text{crotyl})\\text{Co}(\\text{CO})_3 \\]
3. **Deprotonation of Alkene Complexes**:
   \\[ [L_n M(\\eta^2-\\text{propene})]^+ + \\text{Base} \\longrightarrow L_n M(\\eta^3-\\text{allyl}) + \\text{H-Base}^+ \\]"""
        },
        {
            "id": "sec5_6",
            "title": "§5.6 Dynamic Fluxionality in Allyl Complexes: Syn-Anti Isomerism & Ring Slipping",
            "content": """Coordinated $\\eta^3$-allyl ligands display dynamic stereochemical fluxionality that can be monitored by variable-temperature $^1\\text{H}$ NMR spectroscopy.

### Structural Non-Equivalence in Static $\\eta^3$-Allyl:
In a static $\\eta^3$-allyl complex ($C_s$ local symmetry):
- The central proton ($H_c$ at C2) resonates at $\\delta = 4.5-5.5\\text{ ppm}$ ($1\\text{H}$, multiplet).
- The two terminal *syn*-protons ($H_s$, pointing toward the central proton) resonate at $\\delta = 3.5-4.5\\text{ ppm}$ ($2\\text{H}$, doublet).
- The two terminal *anti*-protons ($H_a$, pointing away from the central proton) resonate at $\\delta = 2.0-3.0\\text{ ppm}$ ($2\\text{H}$, doublet).
- The three environments are chemically and magnetically distinct ($1:2:2$ integration ratio).

### Dynamic Exchange Mechanisms:
At elevated temperatures, the *syn*- and *anti*-resonances broaden and coalesce into a single $4\\text{H}$ doublet via two primary mechanisms:

1. **$\\eta^3 \\rightleftharpoons \\eta^1 \\rightleftharpoons \\eta^3$ Mechanism ($\\pi-\\sigma-\\pi$ Exchange)**:
   - One terminal $M-\\text{C}$ bond dissociates, generating a transient 16-electron $\\sigma$-allyl ($\eta^1$-allyl) intermediate.
   - Rapid rotation of $180^\\circ$ occurs around the resulting carbon-carbon single bond ($C_\\alpha-C_\\beta$):
     \\[ \\eta^3-\\text{allyl} \\xrightleftharpoons[k_{-1}]{k_1} [\\eta^1-\\text{allyl}] \\xrightarrow{\\text{rotation}} [\\eta^1-\\text{allyl}]' \\xrightleftharpoons[k_1]{k_{-1}} (\\eta^3-\\text{allyl})' \\]
   - Re-coordination into the $\\eta^3$-mode exchanges the *syn* and *anti* positions.
   - This process is accelerated by coordinating Lewis bases (e.g., phosphines, solvent) that stabilize the 16e $\\eta^1$-intermediate.

2. **Apparent Allyl Inversion via Metal Rotation**:
   - Rotation of the $\\eta^3$-allyl ligand around the metal-centroid axis interconverts the two coordination faces."""
        },
        {
            "id": "sec5_7",
            "title": "§5.7 Nucleophilic Attack on Coordinated $\\pi$-Ligands & Davies-Green-Mingos (DGM) Rules",
            "content": """Coordinating an unsaturated organic ligand to a cationic or electron-deficient transition metal center withdraws electron density, inverting its chemical reactivity from nucleophilic to strongly electrophilic.

### The Davies-Green-Mingos (DGM) Rules:
Steve Davies, Malcolm Green, and Michael Mingos formulated empirical stereoelectronic rules predicting the site of nucleophilic attack on polyene complexes:

1. **Rule 1: Even vs. Odd Hapticity**:
   - Nucleophilic attack occurs preferentially at **even-numbered polyenes** ($\eta^2, \eta^4, \eta^6$) rather than odd-numbered polyenes ($\eta^3, \eta^5, \eta^7$):
     \\[ \\text{Even } (\\eta^{2n}) > \\text{Odd } (\\eta^{2n+1}) \\]
   - *Example*: In $[(\\eta^5-\\text{Cp})(\\eta^6-\\text{benzene})\\text{Fe}]^+$, attack occurs exclusively on the even $\\eta^6$-benzene ring, yielding an $(\\eta^5-\\text{cyclohexadienyl})$ complex.

2. **Rule 2: Open vs. Closed Polyenes**:
   - For ligands of the same hapticity, nucleophilic attack occurs preferentially at **open (acyclic) polyenes** rather than closed (cyclic) polyenes:
     \\[ \\text{Open polyenes} > \\text{Closed polyenes} \\]
   - *Example*: In an 18e complex containing an open $\\eta^5$-pentadienyl and a closed $\\eta^5$-cyclopentadienyl, attack occurs exclusively at the open pentadienyl ligand.

3. **Rule 3: Terminal vs. Internal Attack**:
   - For even, open polyenes, attack occurs at the **terminal carbon atom**:
     \\[ \\text{Terminal position} > \\text{Internal position} \\]
   - For odd, open polyenes, attack occurs at the terminal carbon only if the metal complex is strongly electron-withdrawing; otherwise, internal attack is observed."""
        },
        {
            "id": "sec5_8",
            "title": "§5.8 The Tsuji-Trost Allylic Alkylation: Mechanism and Stereocontrol",
            "content": """The **Tsuji-Trost reaction** is a premier carbon-carbon bond forming reaction in organic synthesis, involving palladium-catalyzed substitution of allylic esters, carbonates, or halides by soft nucleophiles:
\\[ \\text{R-CH}=\\text{CH}-\\text{CH}_2\\text{OAc} + \\text{Nu}^- \\xrightarrow{\\text{Pd(0) cat.},\\, L_2} \\text{R-CH(Nu)}-\\text{CH}=\\text{CH}_2 + \\text{AcO}^- \\]

### Catalytic Cycle and Stereochemical Trajectory:
1. **$\\eta^2$-Olefin Coordination**: The palladium(0) catalyst $L_2\\text{Pd}(0)$ coordinates the allylic double bond.
2. **Ionization (Oxidative Addition)**:
   - Palladium attacks the allylic system from the face **opposite to the leaving group** (inversion of configuration at carbon).
   - Departure of the leaving group ($-\\text{OAc}^-$) yields a cationic $[(\\eta^3-\\text{allyl})\\text{Pd}L_2]^+$ intermediate.
3. **Nucleophilic Attack**:
   - **Soft Nucleophiles ($\\text{p}K_a < 25$, e.g., malonates, amines, $\\beta$-ketoesters)**:
     Attack occurs directly at the allyl carbon from the face **opposite to palladium** (*anti*-attack, outer-sphere mechanism). This incurs a second **inversion of configuration**.
     - Overall Stereochemical Outcome: **Retention of Configuration** (Inversion $+$ Inversion $=$ Net Retention).
   - **Hard Nucleophiles (e.g., organolithiums, Grignard reagents)**:
     Attack occurs first directly at the palladium center (transmetallation, inner-sphere mechanism), followed by reductive elimination onto the allyl ligand.
     - Overall Stereochemical Outcome: **Net Inversion of Configuration** (Inversion $+$ Retention $=$ Net Inversion).

Enantioselective Tsuji-Trost alkylations employ chiral diphosphine ligands (e.g., the Trost ligand), achieving $>99\\%$ enantiomeric excess."""
        }
    ]

    problems = [
        {
            "id": "prob5_1",
            "tier": "Foundational",
            "title": "Structural and Geometric Analysis of Zeise's Salt",
            "statement": "In Zeise's salt $\\text{K}[\\text{PtCl}_3(\\eta^2-\\text{C}_2\\text{H}_4)]\\cdot\\text{H}_2\\text{O}$: (a) Calculate the formal oxidation state, $d$-electron count, and total valence electron count ($VEC$) of platinum. (b) Explain why the ethylene ligand coordinates with its $C=C$ axis perpendicular to the $\\text{PtCl}_3$ square plane. (c) Account for the observed bending back of the four hydrogens ($\\alpha = 32.5^\\circ$) using hybridization changes.",
            "solution": """**Line-by-Line Solution:**

**(a) Formal Oxidation State and Electron Count:**
1. Ligand charges: Three chloride ligands ($-1$ each) and one neutral ethylene ligand ($L$, formal charge $0$).
2. The complex anion is $[\\text{PtCl}_3(\\text{C}_2\\text{H}_4)]^-$ with net charge $q = -1$.
\\[ OS(\\text{Pt}) = -1 - [3(-1) + 0] = -1 - (-3) = +2 \\implies \\text{Pt}(\\text{II}) \\]
3. Platinum is in Group 10 ($n_v = 10$):
\\[ d^n = n_v - OS = 10 - 2 = 8 \\implies d^8 \\]
4. Total valence electron count ($VEC$):
   - $\\text{Pt}(\\text{II})$: 8 electrons
   - Three $\\text{Cl}^-$: $3 \\times 2 = 6$ electrons
   - One $\\eta^2-\\text{C}_2\\text{H}_4$: 2 electrons
\\[ VEC = 8 + 6 + 2 = 16\\text{ electrons} \\]
- A classic 16-electron square planar $d^8$ transition metal complex.

**(b) Orientation of the $C=C$ Axis Perpendicular to the Square Plane:**
1. In a square planar $d^8$ complex in the $xy$-plane, the empty metal orbital accepting the $\\sigma$-dative pair from the alkene $\\pi$-orbital is a $5d/6s/6p$ hybrid pointing along an in-plane coordination vector (say, along the $x$-axis).
2. For $\\pi$-backbonding, the metal must utilize a filled $d$-orbital directed toward the alkene $\\pi^*$ LUMO.
3. If the $C=C$ bond lies in the $xy$-plane (parallel):
   - The metal orbital of matching $\\pi$-symmetry would have to be $d_{xy}$.
   - However, $d_{xy}$ is directed between the four in-plane ligands, experiencing strong steric and electrostatic repulsion with the cis chlorides.
4. If the $C=C$ bond is oriented **perpendicular to the plane (along the $z$-axis)**:
   - The alkene $\\pi^*$ LUMO lies in the $xz$-plane.
   - It overlaps with the filled metal $5d_{xz}$ orbital, which projects above and below the coordination plane into empty space.
   - This orientation provides maximum orbital overlap for $\\pi$-backbonding and minimizes steric clash with the adjacent cis chloride ligands.

**(c) Bending Back of the Hydrogen Atoms:**
1. In uncoordinated ethylene, the carbons are $sp^2$ hybridized with $120^\\circ$ planar geometry.
2. As metal-to-ligand $\\pi$-backdonation populates the $\\pi^*$ LUMO, electron density between the two carbon nuclei drops, while electron density in the $Pt-C$ bonding region increases.
3. The carbon atoms rehybridize from $sp^2$ toward **$sp^3$**.
4. To attain tetrahedral-like geometry around each carbon atom, the four hydrogen substituents bend away from the platinum atom.
5. In Zeise's salt, the observed dihedral bend-back angle is **$\\alpha = 32.5^\\circ$**, corresponding to intermediate character between planar ethylene ($0^\\circ$) and fully $sp^3$ metallacyclopropane ($109.5^\\circ - 90^\\circ \\approx 54^\\circ$)."""
        },
        {
            "id": "prob5_2",
            "tier": "Foundational",
            "title": "NMR Distinction and Coordination Modes of Allyl Ligands",
            "statement": "An allyl complex of formula $[\\text{Pd}(\\text{C}_3\\text{H}_5)(\\text{PPh}_3)\\text{Cl}]$ exists as two distinct coordination isomers. (a) State the hapticity and electron count of the allyl ligand in the $\\eta^1$-mode versus the $\\eta^3$-mode. (b) Predict the number of $^1\\text{H}$ NMR signals and their relative intensities for both isomers in a low-temperature static limit. (c) State which isomer is thermodynamically preferred for palladium(II).",
            "solution": """**Line-by-Line Solution:**

**(a) Hapticity and Electron Counting:**
- **$\\eta^1-\\text{Allyl}$ (monohapto)**:
  - Bound through a single $M-\\text{C}$ $\\sigma$-bond.
  - Acts as a **1-electron donor** in the neutral model ($X$-type) or 2-electron donor as allyl anion ($\text{C}_3\text{H}_5^-$).
  - The remaining two carbons form an uncoordinated pendant $C=C$ double bond.
- **$\\eta^3-\\text{Allyl}$ (trihapto)**:
  - Bound through all three contiguous carbon atoms.
  - Acts as a **3-electron donor** in the neutral model ($LX$-type) or 4-electron donor as allyl anion.

**(b) Low-Temperature Static $^1\\text{H}$ NMR Spectral Prediction:**
1. **For the $\\eta^1-\\text{Allyl}$ Isomer ($M-\\text{CH}_2-\\text{CH}=\\text{CH}_2$)**:
   - Contains a localized $\\sigma$-alkyl methylene group and a vinyl group.
   - Shows three sets of protons:
     - Methylene protons ($-\\text{CH}_2-M$): $2\\text{H}$ at $\\delta \\approx 2.0-2.5\\text{ ppm}$
     - Internal vinyl proton ($-\\text{CH}=$): $1\\text{H}$ at $\\delta \\approx 5.8-6.2\\text{ ppm}$
     - Terminal vinyl protons ($=\\text{CH}_2$): $2\\text{H}$ (split into cis/trans) at $\\delta \\approx 4.8-5.2\\text{ ppm}$
   - **Total**: 3 distinct signals (or 4 if terminal vinyl protons are diastereotopic) with integration ratio **$2 : 1 : 2$**.
2. **For the $\\eta^3-\\text{Allyl}$ Isomer**:
   - Exhibits $C_s$ mirror plane symmetry passing through the central carbon and the metal atom.
   - Shows three distinct signals:
     - Central proton ($H_c$ at C2): $1\\text{H}$ multiplet at $\\delta \\approx 4.8-5.5\\text{ ppm}$
     - Two *syn*-protons ($H_s$ at C1, C3): $2\\text{H}$ doublet at $\\delta \\approx 3.8-4.2\\text{ ppm}$
     - Two *anti*-protons ($H_a$ at C1, C3): $2\\text{H}$ doublet at $\\delta \\approx 2.8-3.2\\text{ ppm}$
   - **Total**: Exactly **3 signals** with integration ratio **$1 : 2 : 2$**.

**(c) Thermodynamic Preference for $\\text{Pd}(\\text{II})$:**
- In $[\\text{Pd}(\\eta^1-\\text{C}_3\\text{H}_5)(\\text{PPh}_3)\\text{Cl}]$, palladium is 3-coordinate and possesses only:
  \\[ VEC = 8 (\\text{Pd}^{II}) + 2 (\\text{Cl}^-) + 2 (\\text{PPh}_3) + 2 (\\eta^1-\\text{allyl}) = 14\\text{ valence electrons} \\]
- In $[\\text{Pd}(\\eta^3-\\text{C}_3\\text{H}_5)(\\text{PPh}_3)\\text{Cl}]$, the $\\eta^3$-allyl donates 4 electrons (ionic model):
  \\[ VEC = 8 + 2 + 2 + 4 = 16\\text{ valence electrons} \\]
- 16 valence electrons represents the closed-shell, thermodynamically stable configuration for square planar $d^8$ $\\text{Pd}(\\text{II})$.
- Therefore, the **$\\eta^3-\\text{allyl}$ isomer is overwhelmingly favored thermodynamically** by $>60\\text{ kJ/mol}$."""
        },
        {
            "id": "prob5_3",
            "tier": "Foundational",
            "title": "Application of the Davies-Green-Mingos (DGM) Rules",
            "statement": "Predict the exact site of nucleophilic attack by methoxide ($\\text{MeO}^-$) on the following cationic complexes using the Davies-Green-Mingos rules: (a) $[(\\eta^5-\\text{C}_5\\text{H}_5)(\\eta^6-\\text{C}_6\\text{H}_6)\\text{Fe}]^+$, (b) $[(\\eta^5-\\text{C}_5\\text{H}_5)(\\eta^4-\\text{C}_4\\text{H}_6)\\text{Fe}(\\text{CO})]^+$, (c) $[(\\eta^5-\\text{C}_5\\text{H}_5)\\text{Mo}(\\text{CO})_2(\\eta^3-\\text{C}_3\\text{H}_5)]^+$.",
            "solution": """**Line-by-Line Solution:**

**(a) $[(\\eta^5-\\text{C}_5\\text{H}_5)(\\eta^6-\\text{C}_6\\text{H}_6)\\text{Fe}]^+$:**
- Ligands present: $\\eta^5-\\text{cyclopentadienyl}$ (odd, closed) and $\\eta^6-\\text{benzene}$ (even, closed).
- **Apply Rule 1**: Nucleophiles attack **even** polyenes preferentially over **odd** polyenes:
  \\[ \\text{Even } (\\eta^6) > \\text{Odd } (\\eta^5) \\]
- Attack occurs exclusively on the **$\\eta^6-\\text{benzene}$ ring**, converting it into an uncharged neutral $\\eta^5-\\text{cyclohexadienyl}$ complex:
  \\[ [(\\eta^5-\\text{Cp})(\\eta^6-\\text{C}_6\\text{H}_6)\\text{Fe}]^+ + \\text{MeO}^- \\longrightarrow (\\eta^5-\\text{Cp})(\\eta^5-\\text{C}_6\\text{H}_6\\text{OMe})\\text{Fe} \\]

**(b) $[(\\eta^5-\\text{C}_5\\text{H}_5)(\\eta^4-\\text{C}_4\\text{H}_6)\\text{Fe}(\\text{CO})]^+$:**
- Ligands present: $\\eta^5-\\text{Cp}$ (odd, closed) and $\\eta^4-\\text{butadiene}$ (even, open).
- **Apply Rule 1**: Attack occurs at the **even** polyene ($\eta^4-\\text{butadiene}$) rather than the odd polyene ($\eta^5-\\text{Cp}$).
- **Apply Rule 3**: For even, open polyenes, attack occurs preferentially at the **terminal carbon** (C1 or C4):
  \\[ \\text{Terminal position } (C1) > \\text{Internal position } (C2) \\]
- Attack delivers a neutral $\\eta^3-\\text{allyl}$ complex: $(\\eta^5-\\text{Cp})\\text{Fe}(\\text{CO})(\\eta^3-\\text{CH}_2\\text{CHCHCH}_2\\text{OMe})$.

**(c) $[(\\eta^5-\\text{C}_5\\text{H}_5)\\text{Mo}(\\text{CO})_2(\\eta^3-\\text{C}_3\\text{H}_5)]^+$:**
- Both polyene ligands are odd: $\\eta^5-\\text{Cp}$ (odd, closed) and $\\eta^3-\\text{allyl}$ (odd, open).
- **Apply Rule 2**: Between ligands of comparable parity, attack occurs at the **open polyene** rather than the closed polyene:
  \\[ \\text{Open } (\\eta^3-\\text{allyl}) > \\text{Closed } (\\eta^5-\\text{Cp}) \\]
- **Apply Rule 3**: Attack occurs at a **terminal carbon** of the allyl ligand, generating a neutral $\\eta^2-\\text{alkene}$ complex:
  \\[ (\\eta^5-\\text{Cp})\\text{Mo}(\\text{CO})_2(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}-\\text{CH}_2\\text{OMe}) \\]"""
        },
        {
            "id": "prob5_4",
            "tier": "Intermediate",
            "title": "Variable-Temperature NMR Kinetics of Alkene Rotation",
            "statement": "The square planar complex $[\\text{PtCl}_2(\\text{PEt}_3)(\\eta^2-\\text{C}_2\\text{Me}_4)]$ possesses a coordinated tetramethylethylene ligand. At $-50^\\circ\\text{C}$, the four methyl groups appear as two distinct $^1\\text{H}$ singlets separated by $\\Delta \\nu = 48\\text{ Hz}$ due to frozen rotation. At coalescence temperature $T_c = +10^\\circ\\text{C}$, the two peaks merge into a single broad singlet. (a) Calculate the rate constant of alkene rotation $k_c$ at coalescence. (b) Calculate the activation enthalpy $\\Delta H^\\ddagger$ and activation entropy $\\Delta S^\\ddagger$ if $\\Delta G^\\ddagger = 61.2\\text{ kJ/mol}$ at $T_c$ and the rate at $-20^\\circ\\text{C}$ is $k = 18\\text{ s}^{-1}$.",
            "solution": """**Line-by-Line Solution:**

**(a) Rate Constant at Coalescence ($k_c$):**
For an uncoupled two-site exchange with equal population probabilities:
\\[ k_c = \\frac{\\pi \\Delta \\nu}{\\sqrt{2}} \\]
Given $\\Delta \\nu = 48\\text{ Hz}$:
\\[ k_c = \\frac{3.14159 \\times 48}{1.4142} = \\frac{150.80}{1.4142} \\approx 106.6\\text{ s}^{-1} \\]

**(b) Eyring Activation Parameters ($\\Delta H^\\ddagger$ and $\\Delta S^\\ddagger$):**
Given:
- $T_1 = -20^\\circ\\text{C} = 253.15\\text{ K}$, with $k_1 = 18\\text{ s}^{-1}$.
- $T_c = +10^\\circ\\text{C} = 283.15\\text{ K}$, with $k_c = 106.6\\text{ s}^{-1}$.

From the linear Eyring formulation:
\\[ \\ln\\left(\\frac{k}{T}\\right) = \\ln\\left(\\frac{k_B}{h}\\right) + \\frac{\\Delta S^\\ddagger}{R} - \\frac{\\Delta H^\\ddagger}{R T} \\]
Let $Y = \\ln(k/T)$ and $X = 1/T$:
- At $T_1 = 253.15\\text{ K}$:
  \\[ X_1 = \\frac{1}{253.15} = 3.9502 \\times 10^{-3}\\text{ K}^{-1} \\]
  \\[ Y_1 = \\ln\\left(\\frac{18}{253.15}\\right) = \\ln(0.07110) = -2.6436 \\]
- At $T_c = 283.15\\text{ K}$:
  \\[ X_2 = \\frac{1}{283.15} = 3.5317 \\times 10^{-3}\\text{ K}^{-1} \\]
  \\[ Y_2 = \\ln\\left(\\frac{106.6}{283.15}\\right) = \\ln(0.37648) = -0.9769 \\]

1. Compute Slope:
   \\[ \\text{Slope} = \\frac{Y_2 - Y_1}{X_2 - X_1} = \\frac{-0.9769 - (-2.6436)}{(3.5317 - 3.9502) \\times 10^{-3}} = \\frac{+1.6667}{-0.4185 \\times 10^{-3}} = -3982.6\\text{ K} \\]
2. Compute Activation Enthalpy:
   \\[ -\\frac{\\Delta H^\\ddagger}{R} = \\text{Slope} \\implies \\Delta H^\\ddagger = -R \\times \\text{Slope} \\]
   \\[ \\Delta H^\\ddagger = -(8.3145\\text{ J/(mol}\\cdot\\text{K)})(-3982.6\\text{ K}) = +33,113\\text{ J/mol} \\approx 33.1\\text{ kJ/mol} \\]
3. Compute Activation Entropy:
   From $\\Delta G^\\ddagger = \\Delta H^\\ddagger - T\\Delta S^\\ddagger$ at $T_c = 283.15\\text{ K}$:
   \\[ \\Delta S^\\ddagger = \\frac{\\Delta H^\\ddagger - \\Delta G^\\ddagger}{T_c} = \\frac{33,113 - 61,200}{283.15} = \\frac{-28,087}{283.15} \\approx -99.2\\text{ J/(mol}\\cdot\\text{K)} \\]
- **Physical Interpretation**: The negative activation entropy ($\\Delta S^\\ddagger \\approx -99\\text{ J/(mol}\\cdot\\text{K)}$) indicates an ordered transition state where solvent and ancillary phosphine ethyl groups become restricted during the $90^\\circ$ rotation."""
        },
        {
            "id": "prob5_5",
            "tier": "Intermediate",
            "title": "Stereochemical Double-Inversion Trajectory in the Tsuji-Trost Reaction",
            "statement": "An enantiomerically pure allylic acetate $(R,E)$-1,3-diphenylallyl acetate is treated with dimethyl sodiomalonate in the presence of $1\\text{ mol}\\%$ $[(\\eta^3-\\text{C}_3\\text{H}_5)\\text{PdCl}]_2$ and $(R,R)$-chiraphos. (a) Trace the stereochemical configuration of the palladium-allyl intermediate. (b) Predict the absolute stereochemistry of the alkylated product. (c) Explain why using a hard alkyl Grignard reagent ($Me\\text{MgBr}$) yields the inverted enantiomer.",
            "solution": """**Line-by-Line Solution:**

**(a) Stereochemistry of the Palladium-Allyl Intermediate:**
1. Starting material: $(R,E)$-1,3-diphenylallyl acetate. The acetate leaving group ($-\\text{OAc}$) resides on one defined face of the allylic plane.
2. In the oxidative addition step, the palladium(0) catalyst coordinates the double bond and performs a nucleophilic displacement on the acetate-bearing carbon.
3. This displacement occurs via an **outer-sphere inversion pathway**: palladium attacks from the face **opposite** to the leaving acetate group:
   \\[ \\text{Step 1: Inversion of Stereochemical Configuration at Carbon} \\]
4. The resulting cationic $[(\\eta^3-\\text{1,3-diphenylallyl})\\text{Pd}(\\text{chiraphos})]^+]$ intermediate has the palladium atom located exclusively on the face opposite to the original acetate.

**(b) Absolute Stereochemistry with Soft Nucleophile (Dimethyl Malonate):**
1. Dimethyl sodiomalonate is a stabilized carbanion ($\\text{p}K_a \\approx 13$, soft nucleophile).
2. Soft nucleophiles attack coordinated $\\eta^3$-allyl ligands via an **outer-sphere mechanism**:
   - The malonate anion attacks the allylic carbon directly from the solution side, on the face **opposite to the palladium atom**.
   - This nucleophilic addition proceeds with **inversion of configuration at carbon**:
     \\[ \\text{Step 2: Second Inversion of Stereochemical Configuration} \\]
3. Summing the two elementary steps:
   \\[ \\text{Net Stereochemical Trajectory} = \\text{Inversion} + \\text{Inversion} = \\mathbf{Net\\ Retention} \\]
4. The product retains the original $(R)$ absolute configuration: $(R,E)$-dimethyl 2-(1,3-diphenylallyl)malonate.

**(c) Stereochemical Divergence with Hard Nucleophile ($Me\\text{MgBr}$):**
1. Methylmagnesium bromide is a hard, localized carbanion.
2. Hard nucleophiles cannot perform outer-sphere attack on the external face of the allyl ligand.
3. Instead, $Me\\text{MgBr}$ attacks the electropositive **palladium metal center** directly via **transmetallation**:
   \\[ [(\\eta^3-\\text{allyl})\\text{Pd}L_2]^+ + Me\\text{MgBr} \\longrightarrow [(\\eta^3-\\text{allyl})\\text{Pd}(Me)L_2] + \\text{MgBr}^+ \\]
4. The methyl group then undergoes intramolecular **reductive elimination** onto the allyl carbon from the **same face as the palladium atom** (retention in the elimination step).
5. Net Stereochemical Trajectory with Hard Nucleophile:
   \\[ \\text{Inversion (Oxidative Addition)} + \\text{Retention (Reductive Elimination)} = \\mathbf{Net\\ Inversion} \\]
- Thus, the reaction with $Me\\text{MgBr}$ yields the opposite $(S)$ enantiomer!"""
        },
        {
            "id": "prob5_6",
            "tier": "Intermediate",
            "title": "Alkyne Coordination as 2-Electron vs. 4-Electron Donors in Tungsten Complexes",
            "statement": "The tungsten complex $[\\text{W}(\\text{CO})(\\text{S}_2\\text{CNEt}_2)_2(\\text{RC}\\equiv\\text{CR})]$ is diamagnetic and stable. (a) Determine the formal oxidation state of tungsten assuming the alkyne acts as a 2-electron donor vs a 4-electron donor. (b) Calculate the total valence electron count ($VEC$) for both models, and prove which donor mode satisfies the 18-electron rule. (c) Predict the effect on the $^{13}\\text{C}$ NMR chemical shift of the alkyne carbons.",
            "solution": """**Line-by-Line Solution:**

**(a) Ligand Classifications and Oxidation States:**
- $\\text{CO}$ is a neutral 2-electron $L$-ligand (formal charge $0$).
- Diethyldithiocarbamate $\\text{S}_2\\text{CNEt}_2^-$ is a bidentate monoanionic ligand ($L X$-type, donating 4 electrons per ligand, charge $-1$).
- Two dithiocarbamate ligands carry a total charge of $-2$.
- Overall complex charge $q = 0$.
- Tungsten is in Group 6 ($n_v = 6$).
- **Model 1: Alkyne as 2-Electron Donor ($L$-type, charge $0$)**:
  \\[ OS = 0 - [2(-1) + 0 + 0] = +2 \\implies \\text{W}(\\text{II}) (d^4) \\]
- **Model 2: Alkyne as 4-Electron Donor ($L_2$-type or $C^2-$ metallacyclopropene, charge $0$ or $-2$)**:
  - Under covalent CBC model: alkyne is $L_2$, formal charge is $0$. Metal oxidation state remains $+2$ ($d^4$).

**(b) Total Valence Electron Count ($VEC$):**
- **Under the 2-Electron Donor Hypothesis**:
  - Tungsten (Group 6): 6 electrons
  - CO: 2 electrons
  - Two dithiocarbamates: $2 \\times 3\\text{e}$ (neutral model: $S^\\bullet + S: = 3\\text{e}$ each) $= 6$ electrons
  - Alkyne (2e): 2 electrons
  \\[ VEC = 6 + 2 + 6 + 2 = 16\\text{ valence electrons} \\]
  Under this model, the tungsten center is sub-18e (16 electrons), leaving an empty valence orbital.
- **Under the 4-Electron Donor Hypothesis**:
  - Both orthogonal $\\pi$-systems ($\pi_\\parallel$ and $\\pi_\\perp$) donate into tungsten:
  \\[ VEC = 6 + 2 + 6 + 4 = \\mathbf{18\\text{ valence electrons}} \\]
- **Conclusion**: To achieve electronic saturation and satisfy the 18-electron rule, the alkyne **must act as a 4-electron donor** ($L_2$).

**(c) $^{13}\\text{C}$ NMR Chemical Shift Prediction:**
- For free alkynes, $sp$-hybridized carbons resonate at $\\delta = 70 - 90\\text{ ppm}$.
- In a 2-electron alkyne complex, carbons shift downfield to $\\delta = 110 - 150\\text{ ppm}$.
- In a 4-electron donor alkyne complex, both $\\pi$-orbitals donate heavily into the metal, while the metal backdonates into $\\pi^*$. The $C-C$ bond order approaches a single bond, and the carbons experience extreme downfield deshielding:
  \\[ \\delta(^{13}\\text{C}) = \\mathbf{200 - 240\\text{ ppm}} \\]
  This downfield shift (in the range typical of carbenes and metal-alkylidynes) is the definitive spectroscopic signature of a 4-electron donating alkyne."""
        },
        {
            "id": "prob5_7",
            "tier": "Advanced",
            "title": "Frontier Molecular Orbital Derivation of the DGM Rules for Cyclic Polyenes",
            "statement": "Prove Rule 1 of the Davies-Green-Mingos theory using perturbation molecular orbital theory. Show mathematically why an incoming nucleophile interacts more favorably with the LUMO of an even polyene complex $[M(\\eta^{2n}-\\text{C}_{2n}\\text{H}_{2n})]^{+m}$ than an odd polyene complex $[M(\\eta^{2n+1}-\\text{C}_{2n+1}\\text{H}_{2n+1})]^{+m}$.",
            "solution": """**Line-by-Line Solution:**

**1. Perturbation Energy for Nucleophilic Attack:**
According to Klopman-Salem frontier molecular orbital theory, the stabilization energy $\\Delta E$ upon interaction between a nucleophile ($\text{Nu}$) and a coordinated polyene complex is:
\\[ \\Delta E = \\frac{q_\\text{Nu} q_i}{\\epsilon R} + 2 \\frac{|c_\\text{Nu} c_i \\beta|^2}{E_\\text{LUMO}(\\text{complex}) - E_\\text{HOMO}(\\text{Nu})} \\]
where the second term represents the frontier orbital charge-transfer interaction.

**2. Frontier Orbital Energy of Coordinated Polyenes:**
Consider the Hückel $\\pi$-orbital levels of even ($2n$) versus odd ($2n+1$) polyenes:
- **Even Closed Polyenes (e.g., Benzene, $2n = 6$)**:
  - Ground-state neutral benzene has 6 electrons completely filling the three bonding MOs ($a_{1g}, e_{1g}$).
  - Coordination to a transition metal in an 18-electron complex involves donation from $a_{1g}$ and $e_{1g}$ into empty metal orbitals, and backdonation from metal $d$ into the degenerate $e_{2u}$ LUMO.
  - However, because the complex bears a formal positive charge ($+m$), the entire orbital manifold is depressed to low energy.
  - The lowest unoccupied molecular orbital (LUMO) of the complex has substantial amplitude localized on the ligand carbon atoms with a low orbital energy $E_\\text{LUMO}$, producing a small denominator $E_\\text{LUMO} - E_\\text{HOMO}(\\text{Nu})$ and a large orbital interaction $\\Delta E$.
- **Odd Polyenes (e.g., Cyclopentadienyl $Cp$, $2n+1 = 5$)**:
  - The cyclopentadienyl ligand is formally a $6\\pi$ aromatic system as $Cp^-$ ($e_{1g}$ completely filled).
  - Its LUMO is $e_{2u}^*$, which lies at an exceptionally high energy level ($> +3\\text{ eV}$ higher than benzene $e_{2u}$).
  - Even upon coordination to a cationic metal center, the $Cp$ $e_{2u}^*$ orbital remains at a prohibitive energy level.
  - Instead, the LUMO of the complex is primarily **metal-centered** ($d_{z^2}^*$ or $e_g^*$), with negligible atomic orbital coefficients $c_i$ on the cyclopentadienyl carbon atoms ($c_i \\approx 0$).

**3. Comparison of Atomic Orbital Coefficients ($c_i$):**
- In even polyene complexes ($\\eta^6-\\text{benzene}$, $\\eta^4-\\text{diene}$), the LUMO has large coefficients at the carbon atoms ($|c_i| \\approx 0.4 - 0.6$).
- In odd polyene complexes ($\\eta^5-\\text{Cp}$), the LUMO is metal-localized ($c_\\text{carbon} \\approx 0.05$).
- Consequently:
  \\[ |c_\\text{Nu} c_\\text{even} \\beta|^2 \\gg |c_\\text{Nu} c_\\text{odd} \\beta|^2 \\]
- Therefore, nucleophilic attack on even polyenes is favored both electrostatically and by frontier orbital overlap by factors exceeding $10^5$, establishing the theoretical foundation of DGM Rule 1."""
        },
        {
            "id": "prob5_8",
            "tier": "Advanced",
            "title": "Quantum Mechanics of the $\\pi-\\sigma-\\pi$ Dynamic Fluxional Exchange in $\\eta^3$-Allyls",
            "statement": "The dynamic exchange of *syn* and *anti* protons in $[(\\eta^3-\\text{C}_3\\text{H}_5)\\text{Pd}(\\text{PR}_3)\\text{Cl}]$ follows the $\\pi-\\sigma-\\pi$ pathway. (a) Derive the steady-state kinetic expression for the exchange rate $k_\\text{obs}$ in the presence of an added Lewis base $L$. (b) Explain why the reaction is first-order in $[L]$ at low base concentration and approaches zero-order saturation at high $[L]$. (c) Construct the orbital correlation diagram connecting $\\eta^3-\\text{allyl}$ to the 16e $\\eta^1-\\text{allyl}$ intermediate.",
            "solution": """**Line-by-Line Solution:**

**(a) Kinetic Derivation of $\\pi-\\sigma-\\pi$ Exchange with Added Base $L$:**
1. Let the starting 16-electron complex be $\\text{Pd}_{\\eta^3}$.
2. **Step 1: Associative Attack of Base $L$**:
   Incoming base $L$ coordinates to palladium, inducing an $\\eta^3 \\to \\eta^1$ hapticity ring slip:
   \\[ \\text{Pd}_{\\eta^3} + L \\xrightleftharpoons[k_{-1}]{k_1} \\text{Pd}_{\\eta^1}-L \\quad (16\\text{-electron } \\sigma\\text{-allyl intermediate}) \\]
3. **Step 2: Carbon-Carbon Single Bond Rotation**:
   In the 16-electron $\\sigma$-allyl intermediate, rotation around the $C_\\alpha-C_\\beta$ bond occurs with rate constant $k_\\text{rot}$:
   \\[ \\text{Pd}_{\\eta^1}-L \\xrightleftharpoons[k_\\text{rot}]{k_\\text{rot}} (\\text{Pd}_{\\eta^1}-L)' \\]
4. **Step 3: Dissociation of $L$ and Re-coordination**:
   \\[ (\\text{Pd}_{\\eta^1}-L)' \\xrightarrow{k_{-1}} \\text{Pd}_{\\eta^3}' + L \\]

Applying the steady-state approximation to the intermediate $[\\text{Pd}_{\\eta^1}-L]$:
\\[ \\frac{d[\\text{Pd}_{\\eta^1}-L]}{dt} = k_1 [\\text{Pd}_{\\eta^3}][L] - (k_{-1} + k_\\text{rot}) [\\text{Pd}_{\\eta^1}-L] = 0 \\]
\\[ [\\text{Pd}_{\\eta^1}-L] = \\frac{k_1 [\\text{Pd}_{\\eta^3}][L]}{k_{-1} + k_\\text{rot}} \\]
The observed rate of exchange of *syn/anti* protons is:
\\[ R_\\text{exchange} = k_\\text{rot} [\\text{Pd}_{\\eta^1}-L] = \\frac{k_1 k_\\text{rot} [L]}{k_{-1} + k_\\text{rot}} [\\text{Pd}_{\\eta^3}] \\]
Thus, the apparent pseudo-first-order rate constant is:
\\[ k_\\text{obs} = \\frac{k_1 k_\\text{rot} [L]}{k_{-1} + k_\\text{rot}} \\]

**(b) Saturation Kinetic Regimes:**
1. **At Low Base Concentration or Fast Rotation ($k_{-1} \\gg k_\\text{rot}$)**:
   \\[ k_\\text{obs} \\approx \\left(\\frac{k_1 k_\\text{rot}}{k_{-1}}\\right) [L] = K_1 k_\\text{rot} [L] \\]
   The exchange rate depends linearly on $[L]$ (first-order kinetics).
2. **At High Base Concentration ($k_\\text{rot} \\gg k_{-1}$ or rapid pre-equilibrium)**:
   When coordination of $L$ is quantitative, the rate-determining step becomes the intrinsic single-bond rotation $k_\\text{rot}$:
   \\[ k_\\text{obs} \\to k_\\text{rot} \\]
   The exchange rate becomes **independent of $[L]$ (zero-order saturation)**.

**(c) Orbital Correlation Diagram ($\eta^3 \\to \\eta^1$):**
- In $\\eta^3-\\text{allyl}$, the three carbon $p$-orbitals form $\\psi_1, \\psi_2, \\psi_3$. Both $\\psi_1$ (symmetric) and $\\psi_2$ (antisymmetric) overlap with metal $d$-orbitals, donating 4 electrons.
- As one terminal carbon $C_3$ pulls away:
  - $\\psi_1$ and $\\psi_2$ re-hybridize into a localized $C_1-M$ $\\sigma$-bonding orbital and a localized $C_2=C_3$ $\\pi$-bonding orbital.
  - The metal $d$-orbital previously bonded to $C_3$ becomes vacant, receiving the electron pair from the incoming base $L$.
- The $C_1-C_2$ bond becomes a pure $\\sigma$-single bond, allowing barrier-free rotation ($E_a \\approx 25-35\\text{ kJ/mol}$) before reverse slip regenerates $\\eta^3$ with exchanged proton environments."""
        },
        {
            "id": "prob5_9",
            "tier": "Advanced",
            "title": "Electronic and Bite-Angle Control of Regioselectivity in Asymmetric Allylic Alkylation",
            "statement": "In the Tsuji-Trost allylic alkylation of an unsymmetrical substrate $[(\\eta^3-\\text{1-methylallyl})\\text{Pd}(P-P)]^+$, attack by dimethyl malonate can occur at C1 (branched product) or C3 (linear product). (a) Explain why steric effects favor attack at C3, whereas electronic ground-state trans-influence favors attack at C1. (b) For an unsymmetrical bidentate ligand where $P_1$ is a strong $\\sigma$-donor (alkylphosphine) and $P_2$ is a strong $\\pi$-acceptor (phosphite), predict the major regioisomer. (c) Derive the mathematical relation between the enantiomeric excess ($ee$) and the difference in transition-state activation free energies $\\Delta\\Delta G^\\ddagger$.",
            "solution": """**Line-by-Line Solution:**

**(a) Steric vs. Electronic Regiocontrol:**
1. **Steric Factor**:
   - C1 bears a methyl substituent; C3 bears only hydrogen atoms.
   - Bulky nucleophiles or sterically encumbered diphosphine ligands favor attack at the **less hindered, unsubstituted terminus C3**, yielding the **linear product** ($E$-alkene).
2. **Electronic Ground-State Trans-Influence**:
   - The methyl group at C1 is an electron-releasing inductive substituent ($+I$), which stabilizes the partial positive charge developing in the transition state.
   - Furthermore, according to the trans-influence, the carbon terminus trans to the stronger trans-influence ligand experiences greater $Pd-C$ bond lengthening and higher carbocationic character, directing nucleophilic attack to that site.

**(b) Regiochemical Outcome with Unsymmetrical $P_1-P_2$ Ligand:**
- $P_1$ is a strong $\\sigma$-donor (e.g., $\\text{PMe}_3$, alkylphosphine).
- $P_2$ is a strong $\\pi$-acceptor (e.g., $\\text{P(OPh)}_3$, phosphite).
1. In square planar $[(\\eta^3-\\text{allyl})\\text{Pd}(P_1)(P_2)]^+$, one allyl terminus is trans to $P_1$, and the other is trans to $P_2$.
2. The strong $\\sigma$-donor $P_1$ exerts a large trans-influence: it directs electron density into the metal, weakening and lengthening the trans $Pd-\\text{C}$ bond.
3. However, the strong $\\pi$-acceptor $P_2$ withdraws electron density from the metal. The allyl carbon **trans to $P_2$** receives significantly less backdonation, rendering it more electrophilic (more carbocationic).
4. Nucleophilic attack by soft carbanions (dimethyl malonate) occurs preferentially at the **allyl terminus trans to the stronger $\\pi$-acceptor ($P_2$)**.
5. By designing ligands where the more sterically accessible or substituted carbon aligns trans to the $\\pi$-acceptor, the reaction can be steered selectively toward either the linear or branched product with $>95:5$ regiocontrol.

**(c) Mathematical Derivation of Enantiomeric Excess ($ee$):**
In an asymmetric catalytic reaction where two enantiomeric pathways proceed through transition states $TS_R$ and $TS_S$ with activation free energies $\\Delta G_R^\\ddagger$ and $\\Delta G_S^\\ddagger$:
1. According to transition-state theory:
   \\[ k_R = \\frac{k_B T}{h} \\exp\\left(-\\frac{\\Delta G_R^\\ddagger}{RT}\\right), \\quad k_S = \\frac{k_B T}{h} \\exp\\left(-\\frac{\\Delta G_S^\\ddagger}{RT}\\right) \\]
2. The enantiomeric ratio ($er$) is:
   \\[ er = \\frac{[R]}{[S]} = \\frac{k_R}{k_S} = \\exp\\left(-\\frac{\\Delta G_R^\\ddagger - \\Delta G_S^\\ddagger}{RT}\\right) = \\exp\\left(\\frac{\\Delta\\Delta G^\\ddagger}{RT}\\right) \\]
   where $\\Delta\\Delta G^\\ddagger = \\Delta G_S^\\ddagger - \\Delta G_R^\\ddagger > 0$ (assuming $R$ is favored).
3. The enantiomeric excess ($ee$) is defined as:
   \\[ ee = \\frac{[R] - [S]}{[R] + [S]} = \\frac{\\frac{[R]}{[S]} - 1}{\\frac{[R]}{[S]} + 1} = \\frac{er - 1}{er + 1} \\]
4. Substituting $er = \\exp\\left(\\frac{\\Delta\\Delta G^\\ddagger}{RT}\\right)$:
   \\[ ee = \\frac{\\exp\\left(\\frac{\\Delta\\Delta G^\\ddagger}{RT}\\right) - 1}{\\exp\\left(\\frac{\\Delta\\Delta G^\\ddagger}{RT}\\right) + 1} = \\tanh\\left(\\frac{\\Delta\\Delta G^\\ddagger}{2RT}\\right) \\]
- **Numerical Benchmark at $298\\text{ K}$**:
  - For $90\\%\\ ee$: $er = 19:1 \\implies \\Delta\\Delta G^\\ddagger = RT \\ln(19) = (8.314)(298)(2.944) = 7.3\\text{ kJ/mol}$ ($1.74\\text{ kcal/mol}$).
  - For $99\\%\\ ee$: $er = 199:1 \\implies \\Delta\\Delta G^\\ddagger = RT \\ln(199) = 13.1\\text{ kJ/mol}$ ($3.13\\text{ kcal/mol}$).
  A difference of just $3\\text{ kcal/mol}$ in transition state free energy delivers near-perfect enantioselectivity!"""
        }
    ]

    return {
        "unit_number": 5,
        "title": "pi-Complexes I: Alkenes, Alkynes & eta3-Allyl Complexes",
        "description": "Dewar-Chatt-Duncanson bonding model for alkene coordination, Zeise's salt, metallacyclopropanes, dynamic rotational barriers around metal-olefin bonds, 2-electron vs 4-electron alkyne donors, synthesis and electronic structure of eta3-allyl complexes, dynamic fluxionality and syn-anti exchange mechanisms, Davies-Green-Mingos (DGM) rules, and the Tsuji-Trost asymmetric allylic alkylation.",
        "sections": sections,
        "problems": problems
    }
