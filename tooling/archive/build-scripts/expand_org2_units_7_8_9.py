# -*- coding: utf-8 -*-
"""
expand_org2_units_7_8_9.py
Enrichment module expanding Units 7, 8, and 9 of Organic Chemistry II to honors depth.
Strict zero course numbers or marks.
Adds deep quantum derivations, extensive physical tables, advanced reaction mechanisms,
and an 8th comprehensive multi-part problem to each unit.
"""

def enrich_units_7_8_9(u7, u8, u9):
    print("Enriching Units 7, 8, and 9 with advanced physical organic content...")

    # --- ENRICH UNIT 7: ACTIVE METHYLENES & PERICYCLIC ADDITIONS ---
    # Section 7.6: The Nazarov Cyclization & Oxy-Cope Rearrangements
    u7["sections"][5]["content"] += r"""

### The Nazarov Cyclization: Conrotatory $4\pi$ Electrocyclization of Divinyl Ketones

The Nazarov cyclization (Ivan Nikolaevich Nazarov, 1942) is an electrocyclic reaction that converts divinyl ketones into cyclopent-2-enones in the presence of strong Lewis or Brønsted acids:

$$\text{Divinyl Ketone} \xrightarrow{\text{Lewis acid (BF}_3\cdot\text{OEt}_2 \text{ or TiCl}_4)} \text{Cyclopent-2-enone} \tag{7.6a}$$

```
       The Nazarov Electrocyclic Cascade:
       Divinyl Ketone + H(+) / Lewis Acid ===> Hydroxypentadienyl Cation (4 pi Cation)
              |
              | Thermal 4 pi Conrotatory Electrocyclization (Woodward-Hoffmann allowed)
              v
       Cyclopentenyl Oxyallyl Carbocation Intermediate
              |
              | Stereospecific loss of proton (- H+)
              v
       Cyclopent-2-enone Derivative
```

1. **Active Intermediate**: Protonation of the divinyl ketone forms a **hydroxypentadienyl cation**, which is isoelectronic with the pentadienyl cation and contains **$4\pi$ electrons**.
2. **Orbital Symmetry**: According to the Woodward-Hoffmann rules, a thermal $4\pi$-electron electrocyclic ring closure proceeds with **conrotatory** stereospecificity.
3. **Torquoselectivity**: In substituted systems, the direction of conrotatory rotation is governed by the electron-donating/withdrawing properties of substituents (torquoselectivity).
4. **Deprotonation**: Loss of a proton from the cyclized oxyallyl carbocation regenerates the acid catalyst, delivering substituted cyclopentenones found in prostaglandins and jasmonates.

### The Anionic Oxy-Cope Rearrangement
While the classical Cope rearrangement of 1,5-hexadienes requires extreme temperatures ($200^\circ\text{–}300^\circ\text{C}$):
- In the **Oxy-Cope rearrangement** (Jerome Berson, 1964), a hydroxyl group is placed at C3.
- In 1975, David A. Evans discovered the **Anionic Oxy-Cope rearrangement**: deprotonation of the C3 hydroxyl group with potassium hydride ($\text{KH}$) in the presence of **18-crown-6** in THF accelerates the [3,3]-sigmatropic rearrangement by a staggering factor of **$10^{10}\text{ to }10^{17}$**!
  $$\text{Acceleration Factor} \sim 10^{12} \implies \text{Reaction occurs instantaneously at } -20^\circ\text{C to } 25^\circ\text{C} \tag{7.6b}$$
- The massive rate enhancement arises because the alkoxide oxygen ($-\text{O}^-$) acts as a powerful electron donor, destabilizing the ground state and dramatically lowering the transition-state barrier."""

    # Section 7.7: The Ireland-Claisen Ester Enolate Rearrangement
    u7["sections"][6]["content"] += r"""

### The Ireland-Claisen Rearrangement: Enolate Geometry Stereocontrol

In 1972, Robert E. Ireland developed the **Ireland-Claisen rearrangement**, converting allyl esters into $\gamma,\delta$-unsaturated carboxylic acids via silyl ketene acetals under mild temperatures ($25^\circ\text{–}65^\circ\text{C}$):

```
       Ireland-Claisen Enolate Stereocontrol:
       Allyl Ester + LDA in THF ====> (E)-Enolate (Chelated TS) ===> anti-gamma,delta-Unsaturated Acid
       Allyl Ester + LDA in THF/HMPA ===> (Z)-Enolate (Solvated TS) ===> syn-gamma,delta-Unsaturated Acid
```

1. **Enolate Stereoselection**:
   - Deprotonation with **LDA in pure THF** favors the **$(E)$-enolate** (chelated cyclic transition state with $\text{Li}^+$).
   - Deprotonation with **LDA in THF / HMPA** (hexamethylphosphoramide) solvates the lithium cation, favoring the **$(Z)$-enolate** (open dipole-minimizing transition state).
2. **Silylation**: Trapping with *tert*-butyldimethylsilyl chloride ($\text{TBSCl}$) locks the enolate geometry as an $(E)$- or $(Z)$-silyl ketene acetal.
3. **[3,3]-Sigmatropic Rearrangement**: The silyl ketene acetal undergoes a concerted [3,3]-sigmatropic shift through a rigid **chair-like transition state**.
4. **Predictable Diastereoselection**: The $(E)$-enolate yields the *anti*-diastereomer with $>95\%$ selectivity, whereas the $(Z)$-enolate yields the *syn*-diastereomer, providing absolute stereocontrol in complex natural product synthesis."""

    # Add Problem 7.8 to Unit 7
    u7["problems"].append({
        "id": "prob7_8",
        "problemNumber": "7.8",
        "title": "Anionic Oxy-Cope Rate Acceleration & Thermodynamic Free Energy Profiles",
        "difficulty": "Mastery",
        "statement": r"""A 1,5-dien-3-ol undergoes thermal oxy-Cope rearrangement with an activation free energy of $\Delta G^\ddagger = 138\text{ kJ}\cdot\text{mol}^{-1}$ ($t_{1/2} \approx 14\text{ hours}$ at $220^\circ\text{C}$). When treated with potassium hydride ($\text{KH}$) and 18-crown-6 in THF at $25^\circ\text{C}$, the reaction is complete in less than 5 minutes ($\Delta G^\ddagger = 79\text{ kJ}\cdot\text{mol}^{-1}$).
(a) Using the Eyring equation, compute the rate acceleration factor $k_{\text{anionic}} / k_{\text{neutral}}$ at $298.15\text{ K}$.
(b) Explain why deprotonation to an alkoxide ($-\text{O}^-$) lowers the activation energy by nearly $60\text{ kJ}\cdot\text{mol}^{-1}$ using frontier orbital perturbation theory.
(c) Why is the inclusion of 18-crown-6 essential to achieve the maximum rate acceleration?""",
        "hints": ["$\Delta(\Delta G^\ddagger) = 138 - 79 = 59\text{ kJ}\cdot\text{mol}^{-1}$.", "Tight ion pairing with potassium retards the reaction; 18-crown-6 creates a 'naked' alkoxide."],
        "solution": r"""### (a) Eyring Rate Acceleration Calculation
$$\Delta(\Delta G^\ddagger) = \Delta G^\ddagger(\text{neutral}) - \Delta G^\ddagger(\text{anionic}) = 138 - 79 = 59\text{ kJ}\cdot\text{mol}^{-1}$$
The rate acceleration factor at $T = 298.15\text{ K}$ is:
$$\frac{k_{\text{anionic}}}{k_{\text{neutral}}} = \exp\left(\frac{\Delta(\Delta G^\ddagger)}{RT}\right)$$
$$RT = (8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (298.15\text{ K}) = 2.4788\text{ kJ}\cdot\text{mol}^{-1}$$
$$\frac{\Delta(\Delta G^\ddagger)}{RT} = \frac{59.0}{2.4788} = 23.80$$
$$\frac{k_{\text{anionic}}}{k_{\text{neutral}}} = \exp(23.80) \approx \mathbf{2.17 \times 10^{10}}$$
The anionic pathway is more than **twenty billion times faster** at room temperature!

### (b) Frontier Orbital Perturbation Theory Rationale
1. **Ground-State Destabilization**: The unshared negative charge on the alkoxide oxygen ($-\text{O}^-$) raises the energy of its non-bonding lone pair ($n_{\text{O}^-}$), making it a massive electron donor.
2. **Weakening of Cleaving Bond**: Strong hyperconjugative donation from $n_{\text{O}^-}$ into the adjacent $\sigma^*_{\text{C3-C4}}$ antibonding orbital significantly weakens the central $\text{C3}-\text{C4}$ single bond:
   $$n_{\text{O}^-} \longrightarrow \sigma^*_{\text{C3-C4}}$$
   This lowers the homolytic/heterolytic bond cleavage barrier in the transition state.
3. **Transition-State Stabilization**: In the transition state, the developing carbonyl $\text{C}=\text{O}$ double bond has substantial bond order. The thermodynamic enthalpy gained by forming a strong carbonyl bond ($\text{BDE} \approx 745\text{ kJ}\cdot\text{mol}^{-1}$) drives the reaction smoothly forward.

### (c) Essential Role of 18-Crown-6
In THF without a crown ether:
- The potassium cation ($\text{K}^+$) forms a tight, contact ion pair with the alkoxide: $[-\text{O}^-\cdots\text{K}^+]$.
- Coordination of $\text{K}^+$ partially neutralizes the negative charge, diminishing electron donation from oxygen into $\sigma^*_{\text{C-C}}$.
- **18-Crown-6** has a cavity diameter of $2.6\text{–}3.2\text{ \AA}$, which matches the ionic diameter of the potassium cation ($2.66\text{ \AA}$) with high affinity ($\log K \approx 6.0$).
- 18-Crown-6 encapsulates $\text{K}^+$, separating it from the alkoxide. This generates a **solvent-separated, "naked" alkoxide anion** with maximal electron density, unlocking the full $10^{10}$-fold rate acceleration."""
    })

    # --- ENRICH UNIT 8: PHARMACEUTICALS & BIO-ACTIVES ---
    # Section 8.3: Green Chemistry Atom Economy of Ibuprofen
    u8["sections"][2]["content"] += r"""

### Green Chemistry Metrics: The Boots vs BHC Catalytic Ibuprofen Syntheses

Ibuprofen (2-(4-isobutylphenyl)propanoic acid) provides the quintessential case study for Green Chemistry and atom economy metrics (1997 Presidential Green Chemistry Challenge Award):

```
Comparison of Industrial Ibuprofen Manufacturing Routes:
1. Boots Classical Route (1960s):
   Isobutylbenzene + Ac2O/AlCl3 ===> Friedel-Crafts Ketone
     ---> ClCH2COOEt / NaOEt (Darzens Condensation) ===> Glycidic Ester
     ---> Hydrolysis & Decarboxylation ===> Aldehyde
     ---> NH2OH ===> Oxime
     ---> Dehydration ===> Nitrile
     ---> Acid Hydrolysis ===> Ibuprofen
   [6 Stoichiometric Steps; Atom Economy = 40.0%; Massive inorganic waste (AlCl3, Na)]

2. BHC Catalytic Route (1990s):
   Isobutylbenzene + Ac2O / HF (Catalytic) ===> 4-Isobutylacetophenone + AcOH
     ---> H2 / Raney Ni (100% Catalytic) ===> 1-(4-Isobutylphenyl)ethanol
     ---> CO / Pd catalyst (Carbonylation) ===> Ibuprofen
   [3 Catalytic Steps; Atom Economy = 77.4% (99% with recycled AcOH); Zero solid waste]
```

#### Atom Economy Mathematical Definition:
$$\text{Atom Economy (AE)} = \frac{\text{Molecular Weight of Desired Product}}{\sum \text{Molecular Weights of All Reactants}} \times 100\% \tag{8.3a}$$

- **Boots Process**: $\text{AE} = \frac{206.28\text{ g/mol}}{514.85\text{ g/mol}} \times 100\% \approx \mathbf{40.0\%}$. Over $60\%$ of the mass of input reagents is converted into unwanted hazardous waste salts ($\text{Al(OH)}_3, \text{NaCl}, \text{NH}_4\text{Cl}$).
- **BHC Process**: $\text{AE} = \frac{206.28\text{ g/mol}}{266.38\text{ g/mol}} \times 100\% = \mathbf{77.4\%}$. When the co-produced acetic acid is recovered and recycled, the effective atom economy reaches **$99\%$**!"""

    # Section 8.5: Artemisinin (Qinghaosu) Mechanism of Action
    u8["sections"][4]["content"] += r"""

### Artemisinin (Qinghaosu): Endoperoxide Architecture & Ferrous Heme Activation

Discovered by Tu Youyou from the sweet wormwood plant *Artemisia annua* (2015 Nobel Prize in Physiology or Medicine), **Artemisinin** is a sesquiterpene lactone containing an unusual **1,2,4-trioxane ring system** featuring a stable 1,2-endoperoxide bridge ($-\text{O}-\text{O}-$).

```
                      Artemisinin Parasiticidal Cascade:
                         [ Artemisinin Trioxane Core ]
                                       |
                                       | Reduced by Fe(2+) (Intraparasitic Heme)
                                       v
                         C4-Centered Oxy Radical Intermediate
                                       |
                                       | [1,5]-Hydrogen Shift / Intramolecular Homolysis
                                       v
                         C-Centered Alkyl Radical Species
                                       |
                                       | Irreversible Covalent Alkylation
                                       v
                    Inactivation of Parasitic PfATP6 & Digestive Vacuole
```

1. **Intraparasitic Activation**: When the malaria parasite digests human hemoglobin, it releases free ferrous iron ($\text{Fe}^{2+}$) in the form of heme in its digestive vacuole.
2. **Homolytic Peroxide Cleavage**: The $\text{Fe}^{2+}$ ion donates a single electron to the weak endoperoxide bridge ($\text{BDE} \approx 140\text{ kJ}\cdot\text{mol}^{-1}$), cleaving the oxygen-oxygen bond to form a transient oxy-radical.
3. **Alkyl Radical Generation**: The oxy-radical undergoes rapid intramolecular rearrangement to form a highly reactive **carbon-centered alkyl radical**.
4. **Target Alkylation**: This carbon-centered radical alkylates the parasite's essential sarco/endoplasmic reticulum $\text{Ca}^{2+}$-ATPase (**PfATP6**) and digestive vacuole membrane lipids, leading to cell death of *Plasmodium falciparum* within hours."""

    # Add Problem 8.8 to Unit 8
    u8["problems"].append({
        "id": "prob8_8",
        "problemNumber": "8.8",
        "title": "Quantitative Atom Economy & E-Factor Comparison: Boots vs BHC Ibuprofen",
        "difficulty": "Mastery",
        "statement": r"""A chemical engineering analysis compares the green chemistry efficiency of the Boots and BHC industrial syntheses of ibuprofen ($\text{C}_{13}\text{H}_{18}\text{O}_2$, molar mass $= 206.28\text{ g/mol}$).
(a) Write the net stoichiometric equations for both the Boots route and the BHC route, identifying all stoichiometric inputs and by-products.
(b) Compute the theoretical atom economy ($\text{AE}$) for both processes.
(c) Given that an industrial Boots plant produced $3500\text{ metric tons}$ of hazardous waste per $1000\text{ metric tons}$ of ibuprofen ($E\text{-factor} = 3.5$), while the BHC plant produces only $100\text{ metric tons}$ of waste per $1000\text{ metric tons}$ of ibuprofen ($E\text{-factor} = 0.1$), quantify the reduction in environmental waste generation achieved by the BHC process.""",
        "hints": ["Atom economy = (MW of product / sum of MW of reactants) * 100%.", "E-factor = Mass of total waste / Mass of product."],
        "solution": r"""### (a) Net Stoichiometric Equations
1. **Boots Classical Route**:
   $$\begin{aligned}
   \text{C}_{10}\text{H}_{14} \text{ (isobutylbenzene)} &+ \text{C}_4\text{H}_6\text{O}_3 \text{ (Ac}_2\text{O)} + \text{C}_4\text{H}_7\text{ClO}_2 \text{ (ethyl chloroacetate)} + \text{C}_2\text{H}_5\text{ONa} + \text{NH}_2\text{OH} + 2\,\text{H}_2\text{O} \\
   &\longrightarrow \text{C}_{13}\text{H}_{18}\text{O}_2 \text{ (Ibuprofen)} + \text{C}_2\text{H}_4\text{O}_2 \text{ (AcOH)} + \text{C}_2\text{H}_6\text{O} \text{ (EtOH)} + \text{NaCl} + \text{NH}_4\text{Cl} + \text{CO}_2
   \end{aligned}$$
   Reactants molar mass sum:
   $$134.22 + 102.09 + 122.55 + 68.05 + 33.03 + 2(18.02) = 514.85\text{ g/mol}$$
2. **BHC Catalytic Route**:
   $$\text{C}_{10}\text{H}_{14} \text{ (isobutylbenzene)} + \text{C}_4\text{H}_6\text{O}_3 \text{ (Ac}_2\text{O)} + \text{H}_2 + \text{CO} \longrightarrow \text{C}_{13}\text{H}_{18}\text{O}_2 \text{ (Ibuprofen)} + \text{C}_2\text{H}_4\text{O}_2 \text{ (AcOH)}$$
   Reactants molar mass sum:
   $$134.22 + 102.09 + 2.02 + 28.01 = 266.34\text{ g/mol}$$

### (b) Atom Economy Calculation
1. **Boots Route Atom Economy**:
   $$\text{AE}(\text{Boots}) = \frac{206.28\text{ g/mol}}{514.85\text{ g/mol}} \times 100\% = \mathbf{40.06\%}$$
2. **BHC Route Atom Economy**:
   $$\text{AE}(\text{BHC}) = \frac{206.28\text{ g/mol}}{266.34\text{ g/mol}} \times 100\% = \mathbf{77.45\%}$$
   When the co-product acetic acid ($\text{AcOH}$) is captured and recycled back to acetic anhydride, the effective atom economy is:
   $$\text{AE}(\text{BHC, recycled}) = \frac{206.28}{134.22 + 2.02 + 28.01 + 42.04} \times 100\% \approx \mathbf{99.9\%}$$

### (c) Environmental Waste Reduction ($E$-Factor)
- For the **Boots process**, $E\text{-factor} = \frac{3500\text{ t}}{1000\text{ t}} = 3.5$.
- For the **BHC process**, $E\text{-factor} = \frac{100\text{ t}}{1000\text{ t}} = 0.1$.
The reduction in hazardous waste generation is:
$$\text{Waste Reduction} = \frac{3.5 - 0.1}{3.5} \times 100\% = \frac{3.4}{3.5} \times 100\% = \mathbf{97.1\%}$$
The BHC catalytic process eliminates **$97\%$ of all chemical waste**, illustrating the power of catalytic reaction engineering."""
    })

    # --- ENRICH UNIT 9: MULTI-HETEROATOM & FUSED SYSTEMS ---
    # Section 9.1: The Paal-Knorr Syntheses
    u9["sections"][0]["content"] += r"""

### The Paal-Knorr Synthesis: Furans, Thiophenes & Pyrroles from 1,4-Diones

The Paal-Knorr synthesis (Carl Paal and Ludwig Knorr, 1884) provides a unified synthetic entry into five-membered heterocycles starting from **1,4-dicarbonyl compounds**:

```
       The Unified Paal-Knorr Heterocyclic Tree:
                  R-CO-CH2-CH2-CO-R (1,4-Diketone)
                               |
              +----------------+----------------+
              |                                 |
              v (Acid: H2SO4 or P2O5)          v (P4S10 or Lawesson's Reagent)
         2,5-Dialkylfuran                  2,5-Dialkylthiophene
              |
              v (Primary Amine: R'-NH2)
         1,2,5-Trialkylpyrrole
```

1. **Synthesis of Furans**: Heated with acid dehydrating agents ($\text{H}_2\text{SO}_4, \text{P}_4\text{O}_{10}$, or $\text{TsOH}$):
   - One ketone carbonyl enolizes to form an enol.
   - The enol oxygen attacks the second carbonyl carbon, closing a five-membered ring.
   - Elimination of water yields the **2,5-dialkylfuran**.
2. **Synthesis of Thiophenes**: Heated with phosphorus pentasulfide ($\text{P}_4\text{S}_{10}$) or Lawesson's reagent:
   - Ketone oxygens are converted into thiones ($-\text{C}=\text{S}$).
   - Cyclization and dehydration expels $\text{H}_2\text{S}$, yielding the **2,5-dialkylthiophene**.
3. **Synthesis of Pyrroles**: Heated with ammonia or primary amines ($\text{R}'\text{NH}_2$):
   - Forms a bis-imine or carbinolamine intermediate.
   - Intramolecular cyclization followed by loss of water delivers the **pyrrole**."""

    # Section 9.5: The Hantzsch Dihydropyridine Synthesis
    u9["sections"][4]["content"] += r"""

### The Hantzsch 1,4-Dihydropyridine Synthesis & Calcium Channel Antagonists

Discovered by Arthur Hantzsch in 1881, this multicomponent condensation combines an aldehyde, two equivalents of a $\beta$-keto ester (such as ethyl acetoacetate), and ammonia:

$$\text{RCHO} + 2\,\text{CH}_3\text{COCH}_2\text{COOEt} + \text{NH}_3 \xrightarrow{\text{EtOH, reflux}} \text{1,4-Dihydropyridine} + 3\,\text{H}_2\text{O} \tag{9.4a}$$

```
                Hantzsch Dihydropyridine Synthesis Cascade:
1. Aldehyde + 1st EAA ===> Knoevenagel Alkylidene [R-CH=C(Ac)COOEt]
2. Ammonia + 2nd EAA  ===> Enamino Ester [CH3-C(NH2)=CH-COOEt]
3. Michael Addition between Enamino Ester and Knoevenagel Adduct
4. Intramolecular Aldol Cyclization & Dehydration ===> 1,4-Dihydropyridine
5. Oxidation with HNO3 or DDQ ===> Fully Aromatic Pyridine Derivative
```

#### Medicinal Pharmacology of 1,4-Dihydropyridines:
1,4-Dihydropyridines are essential **L-type voltage-gated calcium channel blockers** used in treating hypertension and angina:
- **Nifedipine (Procardia)**: Formed using 2-nitrobenzaldehyde.
- **Amlodipine (Norvasc)**: Formed using 2-chlorobenzaldehyde.
These drugs dock into the $\alpha_1$ pore-forming subunit of L-type calcium channels in vascular smooth muscle cells, blocking $\text{Ca}^{2+}$ influx, inducing smooth muscle relaxation, and lowering systemic arterial blood pressure."""

    # Add Problem 9.8 to Unit 9
    u9["problems"].append({
        "id": "prob9_8",
        "problemNumber": "9.8",
        "title": "Total Synthesis & Calcium Channel Docking of Nifedipine",
        "difficulty": "Mastery",
        "statement": r"""Nifedipine (dimethyl 2,6-dimethyl-4-(2-nitrophenyl)-1,4-dihydropyridine-3,5-dicarboxylate) is an essential antihypertensive drug.
(a) Provide the complete Hantzsch condensation sequence to synthesize nifedipine, specifying all three reactant molecules.
(b) Detail the step-by-step mechanism showing the Knoevenagel condensation adduct, the enamino ester intermediate, and the final Michael ring-closure.
(c) Explain why oxidation of nifedipine to the fully aromatic pyridine derivative (e.g., with $\text{HNO}_3$ or exposure to UV light) destroys its calcium channel blocking efficacy.""",
        "hints": ["Reactants are 2-nitrobenzaldehyde, methyl acetoacetate, and ammonia.", "Dihydropyridine has a boat-conformation boat ring; pyridine is flat and planar."],
        "solution": r"""### (a) Reactants for Nifedipine Synthesis
1. **2-Nitrobenzaldehyde** ($1\text{ equivalent}$)
2. **Methyl acetoacetate** ($\text{CH}_3\text{COCH}_2\text{COOMe}$, $2\text{ equivalents}$)
3. **Ammonia** ($\text{NH}_3$, or ammonium acetate, $1\text{ equivalent}$)
Reaction in refluxing methanol or ethanol delivers **nifedipine** in $>85\%$ yield.

### (b) Step-by-Step Reaction Mechanism
$$\begin{aligned}
\text{Component 1 (Knoevenagel Adduct)}: &\quad o\text{-NO}_2\text{-C}_6\text{H}_4\text{CHO} + \text{CH}_3\text{COCH}_2\text{COOMe} \xrightarrow{-\text{H}_2\text{O}} o\text{-NO}_2\text{-C}_6\text{H}_4\text{-CH}=\text{C(Ac)COOMe} \\
\text{Component 2 (Enamino Ester)}: &\quad \text{CH}_3\text{COCH}_2\text{COOMe} + \text{NH}_3 \xrightarrow{-\text{H}_2\text{O}} \text{CH}_3\text{-C(NH}_2)=\text{CH-COOMe} \\
\text{Conjugate Addition}: &\quad \text{Enamino ester attacks Knoevenagel adduct via Michael 1,4-addition} \\
\text{Intramolecular Cyclization}: &\quad \text{Amino group attacks keto carbonyl, closing 6-membered ring} \\
\text{Dehydration}: &\quad \text{Loss of }\text{H}_2\text{O} \text{ yields }\mathbf{\text{Nifedipine (1,4-dihydropyridine)}}
\end{aligned}$$

### (c) Structure-Activity Relationship & Photodecomposition
1. **Bioactive Conformation of Nifedipine**:
   - The 1,4-dihydropyridine ring is **non-planar**, adopting a shallow **boat conformation**.
   - The bulky 2-nitrophenyl ring at C4 is held **strictly perpendicular ($90^\circ$)** to the dihydropyridine ring.
   - In this perpendicular boat geometry, the drug fits precisely into the hydrophobic allosteric binding pocket of the **L-type $\text{Ca}^{2+}$ channel**, with its two ester groups forming essential hydrogen bonds with receptor threonine and glutamine residues.
2. **Aromatization Destroys Activity**:
   - Upon oxidation (or photochemical degradation by ambient UV light in hospital IV lines), nifedipine is converted into the fully aromatic **pyridine derivative**:
     $$\text{Dihydropyridine} \xrightarrow{h\nu \text{ or HNO}_3} \text{Pyridine derivative} + 2\,\text{H}^\bullet$$
   - In the pyridine derivative, the heterocyclic ring becomes completely **flat and planar** ($sp^2$-hybridized throughout).
   - The 2-nitrophenyl ring can no longer maintain the required perpendicular binding orientation, and the hydrogen-bond donor ($-\text{NH}-$) is lost.
   - The oxidized pyridine derivative has **zero affinity for the calcium channel**, completely abolishing therapeutic vasodilation."""
    })

    print("Units 7, 8, and 9 successfully expanded!")
