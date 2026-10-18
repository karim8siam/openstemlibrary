# -*- coding: utf-8 -*-
"""
expand_org2_honors_capstone.py
Honors Capstone Module for Organic Chemistry II.
Injects deep physical organic, kinetic, and structural capstone topics across all 9 units,
bringing the master curriculum data file to >66,000 words.
Strict zero course numbers or marks.
"""

def inject_honors_capstones(units):
    print("Injecting university honors capstone modules across all 9 units...")

    # --- UNIT 1: Circumcoronene, Ovalene & Topological Graph Invariants ---
    units[0]["sections"][7]["content"] += r"""

### Topological Invariants & Graph Theory of Giant Polycyclic Aromatics

In the mathematical chemistry of polycyclic aromatic hydrocarbons (PAHs), benzenoids are classified by topological connectivity:
1. **Cata-Condensed Benzenoids**: Fused ring systems in which no carbon atom belongs to more than two rings (e.g., naphthalene, anthracene, phenanthrene, chrysene). They possess the formula $\text{C}_{4n+2}\text{H}_{2n+4}$ and do not contain any internal carbon atoms shared by three rings.
2. **Peri-Condensed Benzenoids**: Systems containing internal bridgehead vertices shared by three rings (e.g., pyrene, perylene, coronene, ovalene).

```
Topological Graph Invariants of Peri-Condensed Aromatics:
Pyrene (C16H10):       Clar Number = 1 (2 migrating sextets); DRE = 0.598 beta
Coronene (C24H12):     Clar Number = 3 (Fully Benzenoid); DRE = 0.865 beta
Ovalene (C32H14):      Clar Number = 3; Giant Peri-Condensed Disc
Circumcoronene (C54H18): Clar Number = 7; Inner coronene surrounded by 12 outer rings
```

#### Wiener and Randić Topological Indices:
The **Wiener Index** $W(G)$ is the sum of shortest topological path distances between all pairs of carbon vertices in the molecular graph:

$$W(G) = \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N d(v_i, v_j) \tag{1.8a}$$

The Wiener index correlates directly with van der Waals boiling points, chromatographic retention indices, and total $\pi$-electron polarization energies. For large peri-condensed discs like ovalene and circumcoronene, $W(G)$ scales as $N^{2.5}$, reflecting compact, quasi-two-dimensional electronic delocalization approaching the ballistic conduction regime of infinite graphene."""

    # --- UNIT 2: Non-Covalent Interactions & Organocatalytic Trajectories ---
    units[1]["sections"][7]["content"] += r"""

### Non-Covalent Interactions & Kinetic Isotope Effects in Carbonyl Trajectories

In addition to primary frontier orbital overlap, modern physical organic chemistry emphasizes the decisive role of **non-covalent interactions (NCIs)** in governing carbonyl reaction trajectories:

1. **Secondary Kinetic Isotope Effects (KIEs) in the Bürgi-Dunitz Approach**:
   - When a hydride or deuteride donor attacks a carbonyl carbon:
     - The out-of-plane bending vibrational frequency $\nu_{\text{C-H}}$ changes as the carbon atom pyramidalizes from $sp^2$ ($120^\circ$, loose out-of-plane bend $\sim 800\text{ cm}^{-1}$) to tetrahedral $sp^3$ ($109.5^\circ$, stiff $\text{C}-\text{H}$ bend $\sim 1350\text{ cm}^{-1}$).
     - Because zero-point vibrational energy (ZPVE) is higher in the stiffer tetrahedral transition state, deuterium experiences an energetic advantage:
       $$\text{Secondary KIE}: \quad \frac{k_{\text{H}}}{k_{\text{D}}} < 1.0 \quad (\text{inverse KIE, typically } 0.85\text{–}0.92) \tag{2.8a}$$
     - Measuring an inverse secondary KIE provides definitive spectroscopic proof of carbon pyramidalization in the rate-determining transition state.
2. **Dispersion and $\text{CH}-\pi$ Interactions in Asymmetric Enolate Additions**:
   - In enantioselective aldol and alkylation reactions using bulky chiral auxiliaries or catalysts, weak dispersion forces ($\sim 4\text{–}8\text{ kJ}\cdot\text{mol}^{-1}$) between aromatic catalyst walls and alkyl substituents often provide the energetic margin ($\Delta \Delta G^\ddagger \approx 8\text{–}12\text{ kJ}\cdot\text{mol}^{-1}$) that dictates $>98\%$ stereoselectivity, challenging the traditional assumption that steric hindrance is purely repulsive."""

    # --- UNIT 3: Enzymatic Decarboxylation & Acetoacetate Decarboxylase ---
    units[2]["sections"][7]["content"] += r"""

### Enzymatic Decarboxylation Dynamics: Acetoacetate Decarboxylase Active Site Mechanics

In biological systems, the thermal decarboxylation of acetoacetate ($\text{CH}_3\text{COCH}_2\text{COO}^- \to \text{CH}_3\text{COCH}_3 + \text{CO}_2$) is accelerated by the bacterial enzyme **acetoacetate decarboxylase (AADase)** by an astonishing factor of:

$$\text{Enzymatic Acceleration Factor} \approx 10^9\text{-fold} \tag{3.8c}$$

```
    Acetoacetate Decarboxylase Catalytic Cycle:
    Acetoacetate + Lys115 (pKa ~ 6.0 in hydrophobic pocket!)
           |
           v Forms Iminium Cation Intermediate [CH3-C(=N+H-Lys)-CH2-COO-]
           |
           v Rapid Decarboxylation (- CO2): Low Barrier Enamine Formation
           |
           v Enamine Hydrolysis Releases Acetone & Regenerates Free Lys115
```

1. **Perturbed Active-Site $\text{p}K_a$ of Lys115**:
   - In aqueous solution, the $\epsilon$-amino group of lysine has a $\text{p}K_a \approx 10.5$ (fully protonated and non-nucleophilic at neutral $\text{pH}$).
   - In the active site of AADase, **Lys115** is sequestered in a deeply hydrophobic cleft flanked by adjacent Lys116. Electrostatic repulsion between two adjacent positive charges forces Lys115 to depress its $\text{p}K_a$ to **$\text{p}K_a \approx 6.0$**!
   - At physiological $\text{pH}$ ($7.0$), Lys115 is predominantly **unprotonated and neutrally nucleophilic**, allowing rapid Schiff base formation with acetoacetate.
2. **Iminium Electron Sink Mechanics**:
   - Protonation of the Schiff base forms an **iminium cation** ($[\text{C}=\text{N}^+\text{H}-]$).
   - Because nitrogen is positively charged, it acts as a vastly superior electron sink compared to neutral oxygen ($\text{C}=\text{O}$).
   - The activation barrier for $\text{C}-\text{C}$ cleavage drops from $\Delta G^\ddagger \approx 125\text{ kJ}\cdot\text{mol}^{-1}$ down to **$\Delta G^\ddagger \approx 50\text{ kJ}\cdot\text{mol}^{-1}$**, accelerating decarboxylation into the microsecond regime."""

    # --- UNIT 4: Wormlike Micelles & Lyotropic Liquid Crystals ---
    units[3]["sections"][7]["content"] += r"""

### Wormlike Micelles, Rheology & Lyotropic Liquid Crystalline Mesophases

At elevated surfactant concentrations or upon adding screening salts, spherical micelles transition into giant, flexible, polymer-like cylindrical assemblies known as **wormlike micelles (WLMs)**:

```
Surfactant Concentration Regimes:
Monomers (c < CMC)  ===> Spherical Micelles (c > CMC)
                     ===> Wormlike Entangled Micelles (c > c*)
                     ===> Hexagonal Liquid Crystal (Lyotropic)
                     ===> Lamellar Liquid Crystal (Smectic Bilayers)
```

1. **Viscoelasticity and Living Polymers**:
   - Wormlike micelles can grow to contour lengths exceeding several micrometers ($L > 2\text{ }\mu\text{m}$).
   - At concentrations above the overlap concentration ($c^*$), the giant worms entangle into a dynamic network, imparting high zero-shear viscosity and viscoelasticity (characteristic of shampoo and consumer body washes).
   - Unlike covalent synthetic polymers, wormlike micelles are **living polymers**: they continuously break and recombine on a millisecond timescale ($\tau_{\text{break}} \approx 10\text{–}100\text{ ms}$), exhibiting classic Maxwellian stress relaxation:
     $$G(t) = G_0 \exp(-t / \tau_R) \tag{4.14c}$$
2. **Lyotropic Liquid Crystals**:
   - At surfactant concentrations exceeding $30\text{–}50\text{ wt}\%$, the system undergoes thermodynamic self-organization into **lyotropic liquid crystalline phases**:
     - **Hexagonal Phase ($H_1$)**: Cylindrical micelles pack into a two-dimensional hexagonal lattice.
     - **Cubic Phase ($V_1$)**: Bicontinuous cubic network exhibiting zero mean curvature.
     - **Lamellar Phase ($L_\alpha$)**: Alternating parallel bilayers of surfactant and water sheets, forming the structural basis of cell membranes and liposomal pharmaceutical delivery systems."""

    # --- UNIT 5: Femtosecond Azide Photolysis & Staudinger Ligation ---
    units[4]["sections"][7]["content"] += r"""

### Femtosecond Laser Spectroscopy of Azides & Bioorthogonal Staudinger Ligation

#### 1. Ultrafast Photolysis of Aryl Azides
When phenyl azide ($\text{PhN}_3$) is irradiated with an ultraviolet femtosecond laser pulse ($\lambda = 266\text{ nm}$):
1. Dinitrogen is expelled within **$<100\text{ femtoseconds}$**, releasing singlet phenylnitrene ($^1[\text{Ph}\ddot{\text{N}}]$):
   $$\tau_{\text{photolysis}} < 100\text{ fs} \tag{5.20c}$$
2. Singlet phenylnitrene has an extremely short lifetime ($\tau \approx 1\text{ nanosecond}$ in solution at $298\text{ K}$), rapidly undergoing ring expansion to a strained seven-membered cyclic carbodiimide (**1,2,4,6-cycloheptatetraene**):
   $$^1[\text{Ph}\ddot{\text{N}}] \xrightarrow{\Delta G^\ddagger \approx 25\text{ kJ/mol}} \text{1,2,4,6-cycloheptatetraene}$$
3. Nucleophiles (e.g., secondary amines) trap this cyclic ketenimine to furnish **azepines**, providing the fundamental photochemical mechanism of **photoaffinity labeling** in molecular biology.

#### 2. The Bioorthogonal Staudinger Ligation (Carolyn Bertozzi, Nobel 2022)
Hermann Staudinger (1919) discovered that azides react with triarylphosphines to form iminophosphoranes and nitrogen gas:
$$\text{R-N}_3 + \text{PPh}_3 \longrightarrow [\text{R}-\text{N}=\text{PPh}_3] + \text{N}_2\uparrow \xrightarrow{\text{H}_2\text{O}} \text{R-NH}_2 + \text{Ph}_3\text{P}=\text{O}$$
In 2000, Carolyn Bertozzi engineered the **Staudinger Ligation**:
- By equipping the triarylphosphine with an *ortho*-ester electrophilic trap, the intermediate iminophosphorane undergoes intramolecular acyl transfer:
  $$\text{Azido-Biomolecule} + \text{Modified Phosphine} \longrightarrow \mathbf{\text{Stable Amide Conjugate}} + \text{Phosphine Oxide Trap} \tag{5.20d}$$
- Operates under physiological conditions ($\text{pH } 7.4, 37^\circ\text{C}$), completely inert to native cellular proteins and nucleic acids, enabling the fluorescent imaging of cell-surface glycans in living animals."""

    # --- UNIT 6: Vibrational Circular Dichroism & Chiral Nanomaterials ---
    units[5]["sections"][7]["content"] += r"""

### Vibrational Circular Dichroism (VCD) & Chiral Nanomaterial Assemblies

While electronic circular dichroism (ECD) is limited to molecules containing ultraviolet-absorbing chromophores:
1. **Vibrational Circular Dichroism (VCD)**:
   - Measures the differential absorption of left- versus right-circularly polarized light in the **infrared vibrational region** ($4000\text{–}600\text{ cm}^{-1}$):
     $$\Delta A_{\text{IR}} = A_L - A_R \tag{6.8a}$$
   - Because every chemical bond undergoes vibrational stretching and bending transitions, VCD provides a rich, multi-peak stereochemical fingerprint reflecting the absolute three-dimensional solution conformation of the entire molecule.
   - Quantum chemical density functional theory (DFT) calculations of rotational strengths ($R_{01} = \text{Im} \langle 0 | \boldsymbol{\mu} | 1 \rangle \cdot \langle 1 | \mathbf{m} | 0 \rangle$) allow direct, unambiguous assignment of absolute stereocenters without requiring crystallization or chemical derivatization.
2. **Chiral Plasmonic Nanoparticles**:
   - When metal nanoparticles (gold or silver) are arranged into chiral helical superstructures using DNA origami templates, the localized surface plasmon resonance (LSPR) exhibits colossal chiroptical activity, with Kuhn asymmetry factors ($g = \Delta\epsilon / \epsilon$) exceeding $0.1$, opening frontiers in chiral optical metamaterials and ultralow-concentration enantiomer biosensing."""

    # --- UNIT 7: Valence Isomerizations & Dewar Benzene ---
    units[6]["sections"][7]["content"] += r"""

### Pericyclic Valence Isomerizations: Dewar Benzene, Prismane & Quadricyclane

Valence isomerizations are pericyclic transformations that involve only the redistribution of $\sigma$ and $\pi$ bonds without migration of atoms or substituents:

```
             Valence Isomers of Benzene (C6H6):
                 Benzene   <===>   Dewar Benzene   <===>   Prismane
                 (Planar)          (Bicyclo[2.2.0])        (Tetracyclo[2.2.0.0])
```

1. **Dewar Benzene (Bicyclo[2.2.0]hexa-2,5-diene)**:
   - Synthesized by Eugene van Tamelen in 1963.
   - Although it is thermodynamically less stable than benzene by an immense margin:
     $$\Delta H^\circ_{\text{isomerization}} \approx -230\text{ kJ}\cdot\text{mol}^{-1} \quad (55\text{ kcal}\cdot\text{mol}^{-1}) \tag{7.8b}$$
   - Dewar benzene has an unexpectedly long half-life at room temperature ($t_{1/2} \approx 2\text{ days}$ at $25^\circ\text{C}$).
   - Why does it not immediately snap back into benzene?
     Because thermal reversion to benzene requires a **disrotatory ring opening** of the central cyclobutene $\sigma$ bond ($4\pi$ system), which is **Woodward-Hoffmann symmetry-forbidden**! The reaction must proceed via a high-barrier symmetry-forbidden pathway with an activation energy of $\Delta G^\ddagger \approx 105\text{ kJ}\cdot\text{mol}^{-1}$.
2. **Quadricyclane / Norbornadiene Solar Thermal Storage**:
   - Photochemical $[2+2]$ cycloaddition of norbornadiene yields **quadricyclane**:
     $$\text{Norbornadiene} + h\nu \longrightarrow \text{Quadricyclane} \quad (\Delta H^\circ_{\text{stored}} \approx +89\text{ kJ}\cdot\text{mol}^{-1})$$
   - Quadricyclane stores solar energy indefinitely in strained cyclopropane rings until triggered by a catalyst, releasing clean heat upon reversion to norbornadiene."""

    # --- UNIT 8: Modern Targeted Oncology: Kinase Inhibitors & Warheads ---
    units[7]["sections"][7]["content"] += r"""

### Targeted Molecular Oncology: Imatinib & Covalent Acrylamide Inhibitors

The revolution in personalized cancer medicine rests on rationally designed small-molecule kinase inhibitors:

1. **Imatinib (Gleevec, STI-571)**:
   - Approved in 2001 for chronic myeloid leukemia (CML), targeting the oncogenic **BCR-ABL fusion tyrosine kinase**.
   - Acts as a reversible, ATP-competitive inhibitor: docks into the inactive DFG-out conformation of the kinase catalytic domain, locking the activation loop in a catalytically inert state.
   - Resistance mutations, specifically the **T315I gatekeeper mutation** (where threonine is replaced by bulky isoleucine, eliminating a critical hydrogen bond and blocking the binding pocket), spurred the development of second- and third-generation inhibitors (Dasatinib, Nilotinib, Ponatinib).
2. **Covalent Kinase Inhibitors & Michael Warheads: Osimertinib (Tagrisso)**:
   - Designed to overcome the T790M resistance mutation in non-small cell lung cancer (NSCLC) epidermal growth factor receptor (EGFR).
   - Features an **$\alpha,\beta$-unsaturated acrylamide "warhead"** ($-\text{NHCOCH}=\text{CH}_2$):
     - The heterocyclic core docks reversibly into the ATP-binding pocket.
     - The electrophilic acrylamide aligns directly adjacent to the non-catalytic **Cysteine-797 (Cys797)** residue.
     - A targeted, irreversible conjugate 1,4-addition (Michael reaction) occurs:
       $$\text{EGFR-Cys797-SH} + \text{Drug-Acrylamide} \longrightarrow \mathbf{\text{Irreversible Covalent Thioether Adduct}} \tag{8.8c}$$
     - Permanently inactivates the oncogenic kinase with sub-nanomolar potency ($IC_{50} \approx 0.5\text{ nM}$) while sparing wild-type EGFR."""

    # --- UNIT 9: Transition-Metal Cross-Coupling in Heterocyclic Synthesis ---
    units[8]["sections"][7]["content"] += r"""

### Palladium-Catalyzed Cross-Couplings in Heterocyclic Assembly: Suzuki, Heck & Buchwald-Hartwig

Modern industrial manufacturing of heterocyclic pharmaceuticals relies heavily on palladium-catalyzed $\text{C}-\text{C}$ and $\text{C}-\text{N}$ bond construction (2010 Nobel Prize in Chemistry):

```
       Palladium Catalytic Cycle in Heterocyclic Synthesis:
                 Pd(0) Catalyst (Active Species)
                      |
                      | 1. Oxidative Addition (Het-X)
                      v
                 Het - Pd(II) - X
                      |
                      | 2. Transmetallation (R-B(OH)2 in Suzuki)
                      v
                 Het - Pd(II) - R
                      |
                      | 3. Reductive Elimination (Forms Het-R)
                      v
                 Het - R  +  Pd(0) (Regenerated Catalyst)
```

1. **The Suzuki-Miyaura Cross-Coupling**:
   - Couples heterocyclic halides (e.g., bromopyridines, chloroquinolines) with aryl- or heteroarylboronic acids in the presence of base ($\text{K}_2\text{CO}_3$) and catalytic palladium ($[\text{Pd}(\text{PPh}_3)_4]$ or $\text{Pd(dppf)Cl}_2$):
     $$\text{Het-Br} + \text{Ar-B(OH)}_2 \xrightarrow{\text{Pd}(0), \text{base}, 80^\circ\text{C}} \mathbf{\text{Het-Ar}} + \text{B(OH)}_3 + \text{KBr} \tag{9.8c}$$
   - Tolerates aqueous media, physiological functional groups, and diverse heterocycles.
2. **The Buchwald-Hartwig Amination**:
   - Cross-couples aryl halides with primary or secondary amines using bulky, electron-rich phosphine ligands (e.g., XPhos, RuPhos, BINAP):
     $$\text{Het-Cl} + \text{R}_2\text{NH} \xrightarrow{\text{Pd}_2(\text{dba})_3, \text{XPhos}, \text{NaO}t\text{-Bu}, 100^\circ\text{C}} \mathbf{\text{Het-NR}_2} + \text{NaCl} + t\text{-BuOH} \tag{9.8d}$$
   - Overcomes the historical limitation of high-temperature copper-catalyzed Ullmann reactions, permitting the assembly of complex nitrogen heterocycles in minutes."""

    print("Honors capstone modules successfully injected across all 9 units!")
