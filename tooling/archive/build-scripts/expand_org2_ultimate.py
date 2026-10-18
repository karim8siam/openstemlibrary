# -*- coding: utf-8 -*-
"""
expand_org2_ultimate.py
Ultimate University Honors Enrichment Module for Organic Chemistry II.
Injects advanced bioorganic, supramolecular, and modern synthetic monographs across all 9 units,
elevating the master curriculum data file to >66,000 words.
Strict zero course numbers or marks.
"""

def inject_ultimate_monographs(units):
    print("Injecting ultimate university honors monographs across all 9 units...")

    # --- UNIT 1: Environmental Toxicology & Bacterial PAH Dioxygenases ---
    units[0]["sections"][6]["content"] += r"""

### Environmental Toxicology, Bioremediation & Bacterial PAH Dioxygenases

Beyond mammalian cytochrome P450 activation, the environmental fate of polycyclic aromatic hydrocarbons is dictated by microbial biodegradation pathways:

```
          Bacterial Aerobic Biodegradation Cascade of Naphthalene:
          Naphthalene (C10H8)
                 |
                 | Naphthalene 1,2-Dioxygenase (NDO) + O2 + 2 [H]
                 v
          cis-(1R,2S)-1,2-Dihydro-1,2-dihydroxynaphthalene
                 |
                 | cis-Dihydrodiol Dehydrogenase (- 2 [H])
                 v
          1,2-Dihydroxynaphthalene (1,2-Naphthalenediol)
                 |
                 | Extradiol Dioxygenase (Meta-Cleavage of Ring)
                 v
          cis-2-Hydroxybenzalpyruvic Acid ===> Salicylic Acid ===> TCA Cycle (CO2 + H2O)
```

1. **Rieske Non-Heme Iron Dioxygenases**:
   - Soil bacteria (*Pseudomonas putida*, *Sphingomonas paucimobilis*) utilize **naphthalene 1,2-dioxygenase (NDO)** to initiate aerobic catabolism.
   - Unlike mammalian CYP450 (which performs monooxygenation forming toxic *trans*-epoxides), bacterial NDO incorporates **both atoms of molecular oxygen ($\text{O}_2$)** stereospecifically into the aromatic ring, generating *cis*-(1R,2S)-1,2-dihydrodiol with $>99\%$ enantiomeric excess.
2. **Atmospheric Photo-Oxidation & Secondary Organic Aerosols (SOAs)**:
   - Gas-phase and particulate-bound PAHs in urban atmospheres react with hydroxyl radicals ($\text{OH}^\bullet$) and nitrate radicals ($\text{NO}_3^\bullet$) under sunlight.
   - Attack on phenanthrene yields 9,10-phenanthrenequinone and nitrophenanthrenes, which partition into airborne particulate matter ($\text{PM}_{2.5}$) with atmospheric residence times of several weeks."""

    # --- UNIT 2: Pyridoxal Phosphate (PLP) Carbonyl Catalysis ---
    units[1]["sections"][3]["content"] += r"""

### Bioorganic Carbonyl Dynamics: Pyridoxal 5'-Phosphate (PLP) Enzyme Cascades

In cellular biochemistry, **pyridoxal 5'-phosphate (PLP)** (the active coenzyme form of vitamin $\text{B}_6$) acts as a versatile biological carbonyl catalyst for transamination, decarboxylation, racemization, and aldol cleavages of amino acids:

```
            PLP Transamination Schiff Base Cascade:
     Enzyme-Lys-Epsilon-NH2 (Internal Aldimine)  +  Amino Acid Substrate
                           |
                           v Transimination (Reversible Imine Exchange)
               Substrate-PLP External Aldimine
                           |
                           v Calpha Proton Deprotonation (Assisted by Pyridine Electron Sink)
               Resonance-Stabilized Quinonoid Intermediate
                           |
                           v Reprotonation at C4' of PLP
               Ketimine Intermediate ===> Hydrolysis yields alpha-Keto Acid + PMP
```

1. **The Pyridine Ring as an Electron Sink**:
   - The formyl carbonyl group of PLP forms an **external aldimine** (Schiff base) with the substrate amino acid.
   - The protonated pyridine nitrogen ($-\text{N}^+\text{H}-$) of the PLP ring acts as a powerful thermodynamic and resonance **electron sink**, stabilizing the developing carbanionic negative charge formed upon bond cleavage at the $\alpha$-carbon.
2. **Dunathan's Stereoelectronic Hypothesis (Harmon Dunathan, 1966)**:
   - The specific reaction catalyzed by a given PLP-dependent enzyme (transamination, decarboxylation, or $\beta$-elimination) is dictated strictly by stereoelectronics:
   - **The bond to be cleaved at the substrate $\alpha$-carbon must align strictly perpendicular ($90^\circ$) to the planar $\pi$-system of the PLP-aldimine complex**, maximizing orbital overlap between the breaking $\sigma$-bond and the conjugated $\pi^*$ electron sink!
   - In transaminases, the $\text{C}_\alpha-\text{H}$ bond aligns perpendicular; in decarboxylases, the $\text{C}_\alpha-\text{COO}^-$ bond aligns perpendicular, demonstrating how active-site geometric orientation dictates exclusive catalytic specificity."""

    # --- UNIT 3: Macrolactonization Kinetics & The Yamaguchi Protocol ---
    units[2]["sections"][4]["content"] += r"""

### Macrolactonization Kinetics: The Yamaguchi & Keck Protocols

Synthesizing large-ring cyclic esters (**macrolactones**, 12- to 24-membered rings found in macrolide antibiotics like erythromycin, clarithromycin, and epothilone) presents severe kinetic and thermodynamic challenges:
- High translational entropy loss favors intermolecular oligomerization over intramolecular cyclization.
- Transannular steric repulsions across the medium/large ring create significant activation enthalpy penalties.

```
       Yamaguchi Macrolactonization Protocol:
       Seco-Acid (Long Hydroxy Acid) + 2,4,6-Trichlorobenzoyl Chloride (TCBC)
              |
              | DMAP / Et3N in toluene (Forms mixed anhydride)
              v
       Sterically Hindered Mixed Anhydride Intermediate
              |
              | Ultra-High Dilution (Slow syringe-pump addition into hot toluene)
              v
       Macrolactone Ring Derivative  +  2,4,6-Trichlorobenzoic Acid Salt
```

1. **The Yamaguchi Protocol (Masaru Yamaguchi, 1979)**:
   - The hydroxy acid (seco-acid) is activated using **2,4,6-trichlorobenzoyl chloride (TCBC)** in the presence of $\text{Et}_3\text{N}$ to form a mixed anhydride.
   - **Regioselective Attack**: The two ortho-chlorine atoms and the para-chlorine atom sterically shield the benzoyl carbonyl carbon while increasing its electron-withdrawing capacity. Consequently, the nucleophilic catalyst 4-dimethylaminopyridine ($\text{DMAP}$) attacks **exclusively at the aliphatic acyl carbonyl**, generating an active acylpyridinium intermediate.
2. **High-Dilution Kinetics**:
   - The solution is added via syringe pump into a large volume of refluxing toluene ($c \approx 10^{-4}\text{ M}$).
   - At this ultralow concentration, the bimolecular intermolecular rate ($\text{Rate}_{\text{inter}} = k_{\text{inter}} [C]^2$) becomes negligible compared to the unimolecular intramolecular cyclization rate ($\text{Rate}_{\text{intra}} = k_{\text{intra}} [C]$), delivering macrocycles in $>85\%$ isolated yields."""

    # --- UNIT 4: Lipid Rafts & Detergent Membrane Solubilization ---
    units[3]["sections"][5]["content"] += r"""

### Lipid Rafts, Liquid-Ordered Domains & Detergent Membrane Solubilization

Biological cell membranes are not homogenous fluid mosaics, but contain dynamic nanoscale microdomains known as **lipid rafts**:

```
       Lipid Raft Bilayer Phase Separation:
       Liquid-Disordered Phase (Ld): Unsaturated phospholipids (kinked chains, fluid, high area/molecule)
       Liquid-Ordered Raft Phase (Lo): Sphingomyelins + Cholesterol (packed, rigid, detergent-resistant)
```

1. **Thermodynamics of Liquid-Ordered ($\text{L}_o$) Phases**:
   - Sphingolipids have long, fully saturated acyl chains that pack tightly together.
   - **Cholesterol** intercalates between sphingolipid chains: its planar, rigid steroid ring aligns parallel to the saturated chains, decreasing chain trans-gauche isomerization and creating a **liquid-ordered ($\text{L}_o$) phase** characterized by high structural order combined with rapid lateral translational diffusion.
2. **Detergent-Resistant Membranes (DRMs)**:
   - Non-ionic detergents (such as Triton X-100 and Brij-96) solubilize cell membranes by partitioning into the bilayer and extracting lipids into mixed micelles.
   - At $4^\circ\text{C}$, Triton X-100 rapidly solubilizes the fluid liquid-disordered ($\text{L}_d$) phase of the membrane, but is completely incapable of disrupting the tightly packed $\text{L}_o$ raft domains.
   - The insoluble residue, termed **detergent-resistant membrane (DRM)** fractions, is enriched in glycosylphosphatidylinositol (GPI)-anchored proteins, caveolin, and signal transduction kinases, confirming the compartmentalization of cell signaling pathways."""

    # --- UNIT 5: Azo Chromophores in Dye-Sensitized Solar Cells ---
    units[4]["sections"][5]["content"] += r"""

### Azo Chromophores in Dye-Sensitized Solar Cells (DSSCs) & Photovoltaics

In modern optoelectronics and renewable solar energy conversion, synthetic azo dyes function as efficient photon harvesters in **dye-sensitized solar cells (DSSCs, Grätzel cells)**:

```
            DSSC Photoinduced Charge-Transfer Dynamic:
    Light (h*nu) ===> D-pi-A Azo Dye absorbs photon (S0 -> S1*)
                     ===> Ultrafast Electron Injection (tau < 50 fs) into TiO2 Conduction Band
                     ===> Electron travels through circuit (Photocurrent)
                     ===> Oxidized Dye(+) reduced by I3(-)/I(-) Liquid Electrolyte
```

1. **Donor-$\pi$-Acceptor (D-$\pi$-A) Chromophore Engineering**:
   - A high-performance photovoltaic dye requires a directional push-pull electronic architecture:
     - **Electron Donor Domain**: A tertiary aromatic amine ($-\text{NAr}_2$) with a high-energy HOMO.
     - **$\pi$-Conjugated Bridge**: An azo unit ($-\text{N}=\text{N}-$) that maintains continuous coplanar $\pi$-overlap.
     - **Electron Acceptor / Anchoring Domain**: Cyanoacrylic acid ($-\text{CH}=\text{C(CN)COOH}$) or phosphonic acid.
2. **Ultrafast Electron Injection**:
   - Photoexcitation from ground state $S_0$ to excited singlet state $S_1^*$ shifts the electron density instantaneously from the donor amine to the anchoring carboxylate group.
   - The LUMO of the dye overlaps with the $3d$ conduction band states of the **titanium dioxide ($\text{TiO}_2$)** semiconductor.
   - Electron injection takes place on an **ultrafast femtosecond timescale ($\tau_{\text{inj}} < 50\text{ fs}$)**, completing orders of magnitude faster than competing non-radiative decay, achieving internal quantum efficiencies exceeding $90\%$."""

    # --- UNIT 6: Chiral Stationary Phase HPLC Thermodynamics ---
    units[5]["sections"][4]["content"] += r"""

### Thermodynamics of Chiral HPLC Enantioseparation on Polysaccharide Phases

In analytical and preparative chiral chromatography, separation of optical enantiomers on polysaccharide-based chiral stationary phases (e.g., amylose tris(3,5-dimethylphenylcarbamate), commercialized as **Chiralpak IA/IB/IC**) is governed by van 't Hoff chromatographic thermodynamics:

$$\ln k' = -\frac{\Delta H^\circ_{\text{ret}}}{RT} + \frac{\Delta S^\circ_{\text{ret}}}{R} + \ln \Phi \tag{6.4a}$$

where:
- $k' = \frac{t_R - t_0}{t_0}$ is the retention factor.
- $\Phi = V_s / V_m$ is the column phase volume ratio.
- $\Delta H^\circ_{\text{ret}}$ and $\Delta S^\circ_{\text{ret}}$ are the standard enthalpy and entropy of solute transfer from mobile phase to chiral stationary phase.

The chromatographic separation factor (selectivity, $\alpha$) between enantiomers 1 and 2 is:

$$\ln \alpha = \ln\left(\frac{k_2'}{k_1'}\right) = -\frac{\Delta(\Delta H^\circ)}{RT} + \frac{\Delta(\Delta S^\circ)}{R} \tag{6.4b}$$

1. **Enthalpic vs Entropic Control**:
   - In enantioselective binding, the more retained enantiomer forms stronger attractive non-covalent interactions (hydrogen bonds, $\pi\text{–}\pi$, dipole), making $\Delta(\Delta H^\circ) = \Delta H_2^\circ - \Delta H_1^\circ < 0$ (enthalpically favored).
   - However, tighter binding restricts conformational freedom, making $\Delta(\Delta S^\circ) < 0$ (entropically disfavored).
2. **The Isoenantioselective Temperature ($T_{\text{iso}}$)**:
   - Plotting $\ln \alpha$ versus $1/T$ (the van 't Hoff plot) yields a straight line with slope $-\Delta(\Delta H^\circ)/R$.
   - The temperature where $\ln \alpha = 0$ ($\alpha = 1.00$, where enantioseparation vanishes completely) is the **isoenantioselective temperature**:
     $$T_{\text{iso}} = \frac{\Delta(\Delta H^\circ)}{\Delta(\Delta S^\circ)} \tag{6.4c}$$
   - Below $T_{\text{iso}}$, chiral separation is enthalpically controlled; above $T_{\text{iso}}$, chiral resolution is lost."""

    # --- UNIT 7: Danishefsky Diene & Hetero-Diels-Alder (HDA) ---
    units[6]["sections"][6]["content"] += r"""

### Asymmetric Hetero-Diels-Alder (HDA) Additions in Alkaloid Total Synthesis

When the dienophile in a [4+2] cycloaddition contains a heteroatom (carbonyl $\text{C}=\text{O}$, imine $\text{C}=\text{N}$, or nitroso $\text{N}=\text{O}$), the reaction is a **Hetero-Diels-Alder (HDA) reaction**, constructing six-membered heterocycles with multiple stereocenters:

```
        Hetero-Diels-Alder Reaction of Danishefsky's Diene:
        Danishefsky's Diene  +  Aldehyde (RCHO)
              |
              | Chiral Lewis Acid Catalyst [e.g., Cr(Salen) or Eu(hfc)3]
              v
        Silyloxy Dihydropyran Adduct
              |
              | Mild Acid Hydrolysis (TFA or 1 M HCl)
              v
        Dihydropyran-4-one Derivative  +  TMS-OH  +  MeOH
```

1. **Frontier Orbital Matching**:
   - Danishefsky's diene (1-methoxy-3-trimethylsilyloxybuta-1,3-diene) has an exceptionally high HOMO ($\epsilon_{\text{HOMO}} \approx -7.8\text{ eV}$).
   - The carbonyl oxygen of the aldehyde is coordinated by a chiral Lewis acid (e.g., Eric Jacobsen's chiral chromium-Salen complex, $\text{Cr(Salen)}^{3+}$), which depresses the carbonyl LUMO energy.
   - The narrow HOMO-LUMO gap accelerates the [4+2] cycloaddition $>10^6$-fold at $-40^\circ\text{C}$.
2. **Regiochemical Control**:
   - The large HOMO coefficient resides at **C4** of Danishefsky's diene.
   - The large LUMO coefficient resides at the **carbonyl carbon** of the aldehyde.
   - Orbital overlap matches C4 of the diene to the carbonyl carbon, producing **2-substituted 2,3-dihydro-4H-pyran-4-ones** with $>98\%$ enantiomeric excess, forming the foundational core of polyketides, macrolides, and carbohydrate natural products."""

    # --- UNIT 8: Antibody-Drug Conjugates (ADCs) & Cleavable Linkers ---
    units[7]["sections"][5]["content"] += r"""

### Antibody-Drug Conjugates (ADCs): Cleavable Linkers & Targeted Chemotherapy

Antibody-Drug Conjugates (ADCs) represent the culmination of Paul Ehrlich's vision of the "magic bullet": combining the exquisite antigen specificity of monoclonal antibodies with the ultra-potent cytotoxicity of synthetic chemotherapeutic payloads:

```
          Molecular Architecture of an Antibody-Drug Conjugate (ADC):
                 [ Monoclonal Antibody (IgG1) ]
                                |
                                | Maleimide-Thiol Conjugation
                                v
                 [ Cathepsin B-Cleavable Val-Cit Linker ]
                                |
                                | Self-Immolative PABC Spacer
                                v
                 [ Ultra-Potent Cytotoxic Payload (MMAE or DM1) ]
```

1. **Targeting & Internalization**:
   - The monoclonal antibody binds to an overexpressed tumor-specific cell surface antigen (e.g., HER2 in breast cancer, CD30 in lymphoma).
   - Receptor-mediated endocytosis internalizes the ADC into the endosomal/lysosomal compartment of the cancer cell.
2. **Enzymatic Linker Cleavage**:
   - The linker contains a **valine-citrulline (Val-Cit) dipeptide** sequence.
   - In systemic circulation, the linker is stable for weeks. Inside the lysosome, the lysosomal cysteine protease **cathepsin B** hydrolyzes the peptide bond between citrulline and the spacer.
3. **Self-Immolative 1,6-Elimination**:
   - Cleavage expels an unstable $p$-aminobenzylcarbamate ($\text{PABC}$) intermediate.
   - Spontaneous, irreversible **1,6-elimination** expels carbon dioxide gas ($\text{CO}_2\uparrow$) and releases the free, unhindered cytotoxic payload:
     $$\text{PABC-Payload} \xrightarrow{-\text{CO}_2\uparrow} \text{Azaquinone Methide} + \mathbf{\text{Free Cytotoxic Payload (MMAE)}} \tag{8.5a}$$
   - The released antimitotic agent (monomethyl auristatin E, MMAE) arrests tubulin polymerization, inducing apoptotic cell death with picomolar potency ($IC_{50} \sim 10^{-11}\text{ M}$) while sparing healthy non-target tissues."""

    # --- UNIT 9: Continuous Flow Chemistry & Heterocyclic API Manufacture ---
    units[8]["sections"][5]["content"] += r"""

### Continuous Flow Chemistry & Process Intensification in Heterocyclic API Manufacture

In modern pharmaceutical manufacturing, batch reactors are increasingly replaced by **continuous flow microreactors**, providing revolutionary advantages in mass transfer, heat exchange, and safety:

```
            Continuous Flow Microreactor Schematic:
    Stream A (Heterocycle Precursor) ===+
                                         |===> Micro-Mixer ===> Temperature-Controlled ===> Inline Quench &
    Stream B (Highly Reactive Reagent) ==+                       Residence Coil (tau)          Crystallization
```

1. **Extreme Thermal Management ($\Delta T \approx 0$)**:
   - Microreactors feature channel diameters on the order of $200\text{–}1000\text{ }\mu\text{m}$, yielding surface-area-to-volume ratios exceeding:
     $$\frac{A}{V} \approx 10,000\text{ to }50,000\text{ m}^2/\text{m}^3 \tag{9.5a}$$
   - This enables near-instantaneous heat dissipation, allowing dangerously exothermic reactions (such as nitrations, organolithium lithiations at $25^\circ\text{C}$ instead of $-78^\circ\text{C}$, and Skraup quinoline annulations) to run safely without thermal runaways.
2. **Handling Hazardous Transient Intermediates**:
   - Unstable, explosive, or toxic intermediates (e.g., diazonium salts, hydrazoic acid, phosgene, diazomethane) are generated *in situ* in microfluidic streams and immediately consumed in the next reactor zone.
   - The total active inventory of hazardous chemicals at any given millisecond is less than a few milligrams, transforming hazardous synthetic methodologies into safe, continuous pharmaceutical production lines."""

    # --- PHYSICAL ORGANIC REFERENCE TABLES ---
    units[0]["sections"][0]["content"] += r"""

### Thermodynamic Heats of Combustion & Clar Sextet Counts of Polybenzenoids

| Polybenzenoid | Formula | Clar Number ($m$) | $\Delta H^\circ_{\text{comb}}$ ($\text{kJ}\cdot\text{mol}^{-1}$) | Resonance Energy ($\text{kJ}\cdot\text{mol}^{-1}$) | Pauling RE per $\pi$-electron ($\text{kJ}\cdot\text{mol}^{-1}$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Benzene** | $\text{C}_6\text{H}_6$ | $1$ | $-3268$ | $152$ | $25.3$ |
| **Naphthalene** | $\text{C}_{10}\text{H}_8$ | $1$ (migrating) | $-5157$ | $255$ | $25.5$ |
| **Anthracene** | $\text{C}_{14}\text{H}_{10}$ | $1$ | $-7062$ | $351$ | $25.1$ |
| **Phenanthrene** | $\text{C}_{14}\text{H}_{10}$ | $2$ (isolated) | $-7032$ | $381$ | $27.2$ |
| **Tetracene** | $\text{C}_{18}\text{H}_{12}$ | $1$ | $-8970$ | $435$ | $24.2$ |
| **Chrysene** | $\text{C}_{18}\text{H}_{12}$ | $2$ | $-8938$ | $485$ | $26.9$ |
| **Triphenylene** | $\text{C}_{18}\text{H}_{12}$ | $3$ (fully benzenoid) | $-8910$ | $510$ | $28.3$ |
| **Pyrene** | $\text{C}_{16}\text{H}_{10}$ | $1$ | $-7900$ | $440$ | $27.5$ |
| **Coronene** | $\text{C}_{24}\text{H}_{12}$ | $3$ (fully benzenoid) | $-11520$ | $625$ | $26.0$ |"""

    units[1]["sections"][2]["content"] += r"""

### Equilibrium Hydration Constants ($K_{\text{hyd}}$) and Thermodynamic Parameters of Carbonyls

$$\text{R}_1\text{COR}_2 + \text{H}_2\text{O} \xrightleftharpoons{K_{\text{hyd}}} \text{R}_1\text{C(OH)}_2\text{R}_2 \quad (25^\circ\text{C})$$

| Carbonyl Molecule | Formula | $K_{\text{hyd}}$ | $\% \text{ Hydrate}$ | $\Delta G^\circ_{\text{hyd}}$ ($\text{kJ}\cdot\text{mol}^{-1}$) | $\Delta H^\circ_{\text{hyd}}$ ($\text{kJ}\cdot\text{mol}^{-1}$) | $-T\Delta S^\circ$ ($\text{kJ}\cdot\text{mol}^{-1}$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Formaldehyde** | $\text{HCHO}$ | $2280$ | $99.96\%$ | $-19.16$ | $-36.8$ | $+17.6$ |
| **Acetaldehyde** | $\text{CH}_3\text{CHO}$ | $1.06$ | $51.5\%$ | $-0.14$ | $-23.4$ | $+23.3$ |
| **Propionaldehyde** | $\text{CH}_3\text{CH}_2\text{CHO}$ | $0.85$ | $46.0\%$ | $+0.40$ | $-22.6$ | $+23.0$ |
| **Isobutyraldehyde** | $(\text{CH}_3)_2\text{CHCHO}$ | $0.51$ | $33.8\%$ | $+1.67$ | $-21.8$ | $+23.5$ |
| **Chloral** | $\text{CCl}_3\text{CHO}$ | $2.8 \times 10^4$ | $99.99\%$ | $-25.37$ | $-46.0$ | $+20.6$ |
| **Acetone** | $\text{CH}_3\text{COCH}_3$ | $1.4 \times 10^{-3}$ | $0.14\%$ | $+16.28$ | $-16.7$ | $+33.0$ |
| **Cyclobutanone** | $\text{C}_4\text{H}_6\text{O}$ | $0.18$ | $15.3\%$ | $+4.24$ | $-21.0$ | $+25.2$ |
| **Cyclopentanone** | $\text{C}_5\text{H}_8\text{O}$ | $1.2 \times 10^{-3}$ | $0.12\%$ | $+16.66$ | $-15.9$ | $+32.6$ |
| **Cyclohexanone** | $\text{C}_6\text{H}_{10}\text{O}$ | $2.3 \times 10^{-2}$ | $2.25\%$ | $+9.35$ | $-18.4$ | $+27.8$ |
| **Hexafluoroacetone** | $\text{CF}_3\text{COCF}_3$ | $1.2 \times 10^6$ | $100.0\%$ | $-34.68$ | $-54.0$ | $+19.3$ |"""

    units[2]["sections"][2]["content"] += r"""

### Thermodynamic Ionization Parameters ($\text{p}K_a, \Delta H^\circ, \Delta S^\circ$) of Carboxylic Acids

Measured in dilute aqueous solution at $298.15\text{ K}$:

| Carboxylic Acid | Formula | $\text{p}K_a$ | $K_a$ ($\text{M}$) | $\Delta G^\circ_{\text{ion}}$ ($\text{kJ}\cdot\text{mol}^{-1}$) | $\Delta H^\circ_{\text{ion}}$ ($\text{kJ}\cdot\text{mol}^{-1}$) | $\Delta S^\circ_{\text{ion}}$ ($\text{J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Formic Acid** | $\text{HCOOH}$ | $3.75$ | $1.78 \times 10^{-4}$ | $+21.4$ | $-0.1$ | $-72.1$ |
| **Acetic Acid** | $\text{CH}_3\text{COOH}$ | $4.76$ | $1.74 \times 10^{-5}$ | $+27.2$ | $-0.4$ | $-92.6$ |
| **Propanoic Acid** | $\text{CH}_3\text{CH}_2\text{COOH}$ | $4.87$ | $1.35 \times 10^{-5}$ | $+27.8$ | $-0.7$ | $-95.6$ |
| **Fluoroacetic Acid** | $\text{CH}_2\text{FCOOH}$ | $2.57$ | $2.69 \times 10^{-3}$ | $+14.7$ | $-3.8$ | $-62.0$ |
| **Chloroacetic Acid** | $\text{CH}_2\text{ClCOOH}$ | $2.86$ | $1.38 \times 10^{-3}$ | $+16.3$ | $-4.6$ | $-70.1$ |
| **Dichloroacetic Acid** | $\text{CHCl}_2\text{COOH}$ | $1.29$ | $5.13 \times 10^{-2}$ | $+7.4$ | $-3.0$ | $-34.9$ |
| **Trichloroacetic Acid** | $\text{CCl}_3\text{COOH}$ | $0.65$ | $2.24 \times 10^{-1}$ | $+3.7$ | $+1.5$ | $-7.4$ |
| **Trifluoroacetic Acid** | $\text{CF}_3\text{COOH}$ | $0.23$ | $5.89 \times 10^{-1}$ | $+1.3$ | $+2.1$ | $+2.7$ |
| **Benzoic Acid** | $\text{C}_6\text{H}_5\text{COOH}$ | $4.20$ | $6.31 \times 10^{-5}$ | $+24.0$ | $+0.4$ | $-79.2$ |
| **Lactic Acid** | $\text{CH}_3\text{CH(OH)COOH}$ | $3.86$ | $1.38 \times 10^{-4}$ | $+22.0$ | $+0.2$ | $-73.1$ |
| **Pyruvic Acid** | $\text{CH}_3\text{COCOOH}$ | $2.49$ | $3.24 \times 10^{-3}$ | $+14.2$ | $-5.9$ | $-67.4$ |"""

    units[3]["sections"][1]["content"] += r"""

### Kinetic Rate Constants for Nucleophilic Acyl Substitution Interconversions

Second-order rate constants ($k_{\text{Nuc}}$ in $\text{L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$) for the reaction of acetyl derivatives ($\text{CH}_3\text{COL}$) with water ($\text{H}_2\text{O}$) and hydroxide ($\text{OH}^-$) in water at $25^\circ\text{C}$:

| Acyl Derivative | Leaving Group ($\text{L}^-$) | Conjugate Acid $\text{p}K_a$ | $k_{\text{H}_2\text{O}}$ ($\text{s}^{-1}$) | $k_{\text{OH}^-}$ ($\text{L}\cdot\text{mol}^{-1}\cdot\text{s}^{-1}$) | Relative Hydrolysis Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Acetyl Chloride** ($\text{CH}_3\text{COCl}$) | $\text{Cl}^-$ | $-7.0$ | $1.2 \times 10^3$ | $>10^7$ | $10^9$ |
| **Acetic Anhydride** ($(\text{CH}_3\text{CO})_2\text{O}$) | $\text{CH}_3\text{COO}^-$ | $+4.8$ | $2.9 \times 10^{-3}$ | $5.8 \times 10^3$ | $10^5$ |
| **Ethyl Thiolacetate** ($\text{CH}_3\text{COSEt}$) | $\text{EtS}^-$ | $+10.5$ | $1.8 \times 10^{-6}$ | $12.0$ | $10^2$ |
| **Ethyl Acetate** ($\text{CH}_3\text{COOEt}$) | $\text{EtO}^-$ | $+16.0$ | $1.5 \times 10^{-8}$ | $0.11$ | $1.0$ |
| **Acetamide** ($\text{CH}_3\text{CONH}_2$) | $\text{NH}_2^-$ | $+38.0$ | $1.2 \times 10^{-11}$ | $2.4 \times 10^{-5}$ | $10^{-4}$ |
| **$N,N$-Dimethylacetamide** | $\text{Me}_2\text{N}^-$ | $+36.0$ | $4.0 \times 10^{-12}$ | $8.0 \times 10^{-6}$ | $10^{-5}$ |
| **Acetate Anion** ($\text{CH}_3\text{COO}^-$) | $\text{O}^{2-}$ | $>50$ | $0.0$ | $0.0$ | $0$ |"""

    units[4]["sections"][1]["content"] += r"""

### Gas-Phase vs Aqueous Solution Basicity Thermodynamic Constants for Amines

Proton affinity ($\text{PA}$ in $\text{kJ}\cdot\text{mol}^{-1}$), aqueous conjugate acid $\text{p}K_a$, and hydration enthalpy ($\Delta H^\circ_{\text{hyd}}$) across primary, secondary, and tertiary amines:

| Amine Molecule | Gas-Phase Proton Affinity ($\text{kJ}\cdot\text{mol}^{-1}$) | Gas Basicity Rank | Aqueous $\text{p}K_a(\text{BH}^+)$ | Aqueous Rank | $\Delta H^\circ_{\text{hyd}}(\text{BH}^+)$ ($\text{kJ}\cdot\text{mol}^{-1}$) | Number of $\text{N}-\text{H}\cdots\text{OH}_2$ H-bonds |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Ammonia ($\text{NH}_3$)** | $853.6$ | $1$ (Least) | $9.24$ | $1$ (Least) | $-440$ | $4$ |
| **Methylamine ($\text{MeNH}_2$)** | $899.0$ | $2$ | $10.64$ | $3$ | $-393$ | $3$ |
| **Dimethylamine ($\text{Me}_2\text{NH}$)** | $929.5$ | $3$ | **$10.73$** | **$4$ (Most)** | $-351$ | $2$ |
| **Trimethylamine ($\text{Me}_3\text{N}$)** | **$948.9$** | **$4$ (Most)** | $9.80$ | $2$ | $-305$ | $1$ |
| **Ethylamine ($\text{EtNH}_2$)** | $912.0$ | $5$ | $10.67$ | $6$ | $-385$ | $3$ |
| **Diethylamine ($\text{Et}_2\text{NH}$)** | $951.4$ | $7$ | **$10.98$** | **$8$ (Most)** | $-339$ | $2$ |
| **Triethylamine ($\text{Et}_3\text{N}$)** | **$981.8$** | **$8$ (Most)** | $10.75$ | $7$ | $-289$ | $1$ |
| **Aniline ($\text{PhNH}_2$)** | $882.5$ | - | $4.60$ | - | $-347$ | $3$ (Resonance deactivation) |"""

    units[5]["sections"][2]["content"] += r"""

### Optical Rotations & Physical Properties of Diastereomeric and Enantiomeric Pairs

| Chiral Substrate | Configuration | Melting Point ($^\circ\text{C}$) | Specific Rotation $[\alpha]_D^{20}$ ($c, \text{ solvent}$) | Water Solubility ($25^\circ\text{C}$) | Absolute CIP Stereodescriptors |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tartaric Acid** | $(+)\text{-(2R,3R)}$ | $170^\circ\text{C}$ | $+12.4^\circ$ ($c=20, \text{H}_2\text{O}$) | $1390\text{ g/L}$ | $(2R,3R)$ (Chiral, $C_2$) |
| **Tartaric Acid** | $(-)\text{-(2S,3S)}$ | $170^\circ\text{C}$ | $-12.4^\circ$ ($c=20, \text{H}_2\text{O}$) | $1390\text{ g/L}$ | $(2S,3S)$ (Chiral, $C_2$) |
| **Tartaric Acid** | *meso* | $140^\circ\text{C}$ | $0.0^\circ$ (Inactive) | $1250\text{ g/L}$ | $(2R,3S)$ (Achiral, $C_s$) |
| **Alanine** | $\text{L-Alanine}$ | $297^\circ\text{C}$ (decomp) | $+14.5^\circ$ ($c=10, 6\text{ M HCl}$) | $166\text{ g/L}$ | $(S)$ (Natural enantiomer) |
| **Alanine** | $\text{D-Alanine}$ | $297^\circ\text{C}$ (decomp) | $-14.5^\circ$ ($c=10, 6\text{ M HCl}$) | $166\text{ g/L}$ | $(R)$ (Bacterial cell walls) |
| **Mandelic Acid** | $(R)\text{-(-)}$ | $133^\circ\text{C}$ | $-158.0^\circ$ ($c=2.5, \text{H}_2\text{O}$) | $160\text{ g/L}$ | $(R)$ |
| **Mandelic Acid** | $(S)\text{-(+)}$ | $133^\circ\text{C}$ | $+158.0^\circ$ ($c=2.5, \text{H}_2\text{O}$) | $160\text{ g/L}$ | $(S)$ |
| **Mandelic Acid** | $(\pm)\text{-Racemate}$ | $120^\circ\text{C}$ | $0.0^\circ$ | $86\text{ g/L}$ | Racemic conglomerate/compound |"""

    units[6]["sections"][1]["content"] += r"""

### Solvent Dependence of Tautomeric Equilibria ($K_T$) in Active Methylenes

Equilibrium enol percentage ($\% \text{ enol}$) and tautomeric equilibrium constant $K_T = [\text{enol}] / [\text{keto}]$ determined by Kurt Meyer titration and high-field $^1\text{H}$ NMR integration at $20^\circ\text{C}$:

| Solvent | Dielectric Constant ($\epsilon_r$) | EAA ($\% \text{ enol}$) | EAA $K_T$ | Acetylacetone ($\% \text{ enol}$) | Acetylacetone $K_T$ | Thermodynamic Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gas Phase** | $1.0$ | **$49.0\%$** | $0.96$ | **$95.0\%$** | $19.0$ | Intramolecular H-bond chelate ring dominates in vacuum |
| **Cyclohexane** | $2.0$ | $15.5\%$ | $0.183$ | $84.0\%$ | $5.25$ | Non-polar solvent cannot hydrogen-bond with keto carbonyls |
| **Carbon Tetrachloride** | $2.2$ | $13.0\%$ | $0.149$ | $82.0\%$ | $4.56$ | Non-polar medium stabilizes chelate |
| **Toluene** | $2.4$ | $11.0\%$ | $0.124$ | $79.0\%$ | $3.76$ | Mild aromatic $\pi$-solvation |
| **Neat Liquid** | - | $8.0\%$ | $0.087$ | $80.0\%$ | $4.00$ | Intermolecular keto-keto dipole alignment |
| **Ethanol** | $24.5$ | $6.5\%$ | $0.070$ | $74.0\%$ | $2.85$ | Protic solvent competes with enol internal H-bond |
| **Methanol** | $32.7$ | $5.0\%$ | $0.053$ | $72.0\%$ | $2.57$ | Strong intermolecular H-bonding to keto carbonyls |
| **Water** | **$78.4$** | **$0.40\%$** | **$0.004$** | **$16.0\%$** | **$0.19$** | Water heavily hydrates keto forms ($\Delta H_{\text{hyd}} \ll 0$), disfavoring enol |"""

    units[7]["sections"][1]["content"] += r"""

### Physicochemical, Pharmacokinetic & Target Profiles of Core Bio-Actives

| Pharmaceutical Active (API) | Molecular Formula & Mass | $\text{p}K_a$ Values | Lipophilicity ($\log P$) | Human Plasma Half-Life ($t_{1/2}$) | Biological Target & Mechanism of Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Aspirin (Acetylsalicylic Acid)** | $\text{C}_9\text{H}_8\text{O}_4 \quad (180.16)$ | $3.5$ (Carboxyl) | $1.19$ | $15\text{–}20\text{ min}$ (Salicylate: $2\text{–}3\text{ h}$) | Covalent acetylation of COX-1 Ser530 and COX-2 Ser516; irreversible antiplatelet |
| **Paracetamol (Acetaminophen)** | $\text{C}_8\text{H}_9\text{NO}_2 \quad (151.16)$ | $9.5$ (Phenol) | $0.46$ | $2.0\text{–}3.0\text{ hours}$ | Selective peroxidase site inhibition of COX in CNS; antipyretic & analgesic |
| **Sulfamethoxazole (SMX)** | $\text{C}_{10}\text{H}_{11}\text{N}_3\text{O}_3\text{S} \quad (253.28)$ | $1.7\ (\text{NH}_3^+), 5.6\ (\text{SO}_2\text{NH})$ | $0.89$ | $10.0\text{ hours}$ | Competitive inhibition of bacterial dihydropteroate synthase (DHPS); PABA mimic |
| **Chloroquine** | $\text{C}_{18}\text{H}_{26}\text{ClN}_3 \quad (319.87)$ | $8.4\ (\text{quinoline}), 10.2\ (\text{amine})$ | $4.63$ | $30\text{–}60\text{ days}$ (Tissue-bound) | Accumulates in acidic food vacuole ($\text{pH } 5.2$); caps hemozoin, poisoning parasite |
| **Phenobarbital** | $\text{C}_{12}\text{H}_{12}\text{N}_2\text{O}_3 \quad (232.24)$ | $7.4$ (Imide) | $1.47$ | $80\text{–}120\text{ hours}$ | Allosteric modulator of neuronal $\text{GABA}_A$ receptor, prolonging channel open bursts |
| **Saccharin** | $\text{C}_7\text{H}_5\text{NO}_3\text{S} \quad (183.18)$ | $1.6$ (Imide) | $0.91$ | Excreted unchanged in urine | Agonist of TAS1R2/TAS1R3 sweet taste GPCR; non-caloric sweetener ($300\times \text{sucrose}$) |"""

    units[8]["sections"][1]["content"] += r"""

### Aromatic Resonance Energies, Dipole Moments & Basicity Constants of Heterocycles

Physical organic constants for five-membered and fused bicyclic heteroaromatics:

| Heterocycle | Ring Class | $\pi$-Electrons | Resonance Energy ($\text{kJ}\cdot\text{mol}^{-1}$) | Dipole Moment ($\mu$ in $\text{D}$) | $\text{p}K_a$ of Conjugate Acid ($\text{BH}^+$) | Predominant Regioselectivity |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Pyrrole** | $5$-Ring ($1\text{ N}$) | $6\pi$ ($\pi$-excessive) | $88\text{ kJ}\cdot\text{mol}^{-1}$ | $1.80\text{ D}$ (towards N) | $-3.8$ (Non-basic, protonates at C2) | EAS exclusively at C2 |
| **Imidazole** | $5$-Ring ($2\text{ N}$) | $6\pi$ (Amphoteric) | $59\text{ kJ}\cdot\text{mol}^{-1}$ | $3.61\text{ D}$ | **$+6.95$** (Basic at N3, forms symmetric ion) | EAS at C4/C5; C2 deprotonation |
| **Pyrazole** | $5$-Ring ($2\text{ N}$) | $6\pi$ | $63\text{ kJ}\cdot\text{mol}^{-1}$ | $2.21\text{ D}$ | $+2.52$ | EAS at C4 |
| **Oxazole** | $5$-Ring ($1\text{ O}, 1\text{ N}$) | $6\pi$ | $42\text{ kJ}\cdot\text{mol}^{-1}$ | $1.50\text{ D}$ | $+0.80$ | Diels-Alder diene; EAS difficult |
| **Thiazole** | $5$-Ring ($1\text{ S}, 1\text{ N}$) | $6\pi$ | $54\text{ kJ}\cdot\text{mol}^{-1}$ | $1.61\text{ D}$ | $+2.50$ | C2 carbene formation (Breslow) |
| **Pyridine** | $6$-Ring ($1\text{ N}$) | $6\pi$ ($\pi$-deficient) | $117\text{ kJ}\cdot\text{mol}^{-1}$ | $2.20\text{ D}$ | $+5.25$ | EAS at C3; NAS at C2/C4 |
| **Indole** | Fused $6\text{-}5$ ($1\text{ N}$) | $10\pi$ | $197\text{ kJ}\cdot\text{mol}^{-1}$ | $2.11\text{ D}$ | $-3.6$ | **EAS exclusively at C3** |
| **Quinoline** | Fused $6\text{-}6$ ($1\text{ N}$) | $10\pi$ | $205\text{ kJ}\cdot\text{mol}^{-1}$ | $2.19\text{ D}$ | $+4.90$ | EAS at C5/C8; NAS at C2/C4 |
| **Isoquinoline** | Fused $6\text{-}6$ ($1\text{ N}$) | $10\pi$ | $205\text{ kJ}\cdot\text{mol}^{-1}$ | $2.73\text{ D}$ | $+5.40$ | EAS at C5/C8; NAS at C1 |"""

    print("Ultimate university honors monographs successfully injected across all 9 units!")
