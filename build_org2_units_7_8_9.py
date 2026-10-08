# -*- coding: utf-8 -*-
"""
build_org2_units_7_8_9.py
Rigorous honors-level curriculum generator for Units 7, 8, and 9 of Organic Chemistry II.
Strict zero course numbers or marks.
Contains massive depth, comprehensive KaTeX proofs, thermodynamic parameters, reaction tables,
and 7-8 multi-tier solved problems per unit with step-by-step solutions.
"""

def get_unit_7():
    return {
        "id": "unit7",
        "unitId": "unit7-org2",
        "number": 7,
        "unitNumber": 7,
        "title": "Unit 7: Bi-functional Compounds, Active Methylenes & Pericyclic Additions: Tautomerism, Robinson Annulation & Orbital Symmetry",
        "description": "Exhaustive treatment of polyfunctional systems and concerted reactions: keto-enol tautomerism equilibria and thermodynamic driving forces in active methylenes (ethyl acetoacetate and diethyl malonate), ketone vs acid cleavage manifolds; synthetic constructions of mono/dialkyl ketones, carboxylic acids, and alicyclic rings; conjugate 1,4-addition (Michael reaction), the Robinson annulation cascade; and frontier molecular orbital theory of pericyclic reactions (electrocyclizations, Diels-Alder [4+2] cycloadditions, Alder endo rule, secondary orbital overlap, and Woodward-Hoffmann orbital symmetry conservation rules).",
        "leadSummary": "Advanced physical organic analysis of active methylene carbanions, keto-enol tautomerism thermodynamics, Michael conjugate additions, Robinson annulation cascades, and Woodward-Hoffmann pericyclic orbital symmetry frameworks.",
        "simulations": ["sim_chem_michael_robinson_annulation_cascade"],
        "sections": [
            {
                "id": "sec7_1",
                "secNumber": "§7.1",
                "title": "Active Methylene Compounds: Keto-Enol Tautomerism & Thermodynamic Driving Forces",
                "heading": "Active Methylene Compounds: Keto-Enol Tautomerism & Thermodynamic Driving Forces",
                "content": r"""Active methylene compounds contain a central methylene group ($-\text{CH}_2-$) flanked on both sides by strongly electron-withdrawing groups, such as carbonyl, ester, cyano, or nitro groups. The two quintessential archetypes are **ethyl acetoacetate (EAA)** ($\text{CH}_3\text{COCH}_2\text{COOEt}$) and **diethyl malonate (DEM)** ($\text{CH}_2(\text{COOEt})_2$).

### Extraordinary $\alpha$-Acidity
The protons of the central methylene group possess exceptional Brønsted acidity:
- Methane ($\text{CH}_4$): $\text{p}K_a \approx 50$
- Acetone ($\text{CH}_3\text{COCH}_3$): $\text{p}K_a \approx 19.3$
- Ethyl acetate ($\text{CH}_3\text{COOEt}$): $\text{p}K_a \approx 25$
- **Diethyl malonate ($\text{DEM}$)**: **$\text{p}K_a \approx 13.3$**
- **Ethyl acetoacetate ($\text{EAA}$)**: **$\text{p}K_a \approx 10.7$**
- Acetylacetone (pentane-2,4-dione): **$\text{p}K_a \approx 8.9$**

This enhanced acidity ($>10^{39}$-fold relative to methane) arises because deprotonation generates an enolate carbanion where the negative charge is delocalized over **three atoms** (two oxygens and one carbon) through a symmetric three-center four-electron $\pi$ system.

```
Ethyl Acetoacetate Keto-Enol Tautomerism:
     O         O                                O         OH
    //        //                               //        /
 CH3-C - CH2 - C - OEt   <========>         CH3-C = CH - C - OEt
     \       /                                  \_______/
      Keto Form (92%)                        Enol Form (8%, H-Bonded 6-Ring)
```

### Keto-Enol Tautomerism Equilibria & Kurt Meyer Bromine Titration
In ordinary monofunctional ketones like acetone, the enol content at equilibrium is negligible ($K_{\text{enol}} \approx 10^{-7}$, $0.0001\%$ enol).
In contrast, ethyl acetoacetate exhibits a significant enol concentration at room temperature:
- **Neat Liquid**: $K_{\text{enol}} \approx 0.087$ ($8.0\%$ enol, $92.0\%$ keto).
- **In Water**: $K_{\text{enol}} \approx 0.004$ ($0.4\%$ enol, $99.6\%$ keto). Water hydrogen-bonds with the two keto carbonyls, stabilizing the keto form.
- **In Hexane / Gas Phase**: $K_{\text{enol}} \approx 0.90$ ($48\%$ enol!). In non-polar solvents, the enol form dominates.

What provides the immense thermodynamic stabilization of the enol form in active methylenes?
1. **Intramolecular Hydrogen Bonding**: The enol hydroxyl proton forms a quasi-aromatic **six-membered hydrogen-bonded chelate ring** with the ester carbonyl oxygen ($\Delta H^\circ_{\text{H-bond}} \approx -25\text{ kJ}\cdot\text{mol}^{-1}$).
2. **Extended $\pi$-Conjugation**: The newly formed $\text{C}=\text{C}$ double bond is fully conjugated with the remaining carbonyl $\pi$ system.

In 1911, Kurt Meyer developed the **bromine titration method** to quantify enol content: molecular bromine ($\text{Br}_2$) reacts instantaneously at $0^\circ\text{C}$ with the enol form ($\text{C}=\text{C}$ addition), whereas it reacts millions of times slower with the keto form. Immediate quenching with $\beta$-naphthol and iodometric back-titration precisely measures the exact enol fraction.""",
                "simulations": []
            },
            {
                "id": "sec7_2",
                "secNumber": "§7.2",
                "title": "Synthetic Manifolds of Ethyl Acetoacetate: Ketone vs Acid Cleavage",
                "heading": "Synthetic Manifolds of Ethyl Acetoacetate: Ketone vs Acid Cleavage",
                "content": r"""Ethyl acetoacetate (EAA) is one of the most versatile building blocks in organic synthesis because its alkylated derivatives can be cleaved via two completely distinct chemical manifolds:

```
              Ethyl Acetoacetate Synthetic Manifolds:
                         CH3-CO-CH2-COOEt (EAA)
                                  | 1. NaOEt, EtOH
                                  | 2. R-X (SN2)
                         CH3-CO-CH(R)-COOEt
                                /     \
       Dilute aq. NaOH, reflux /       \ Concentrated alcoholic KOH, reflux
       then acidify & warm    /         \ then acidify
                             v           v
                    Ketone Cleavage     Acid Cleavage
                    CH3-CO-CH2-R        R-CH2-COOH  +  CH3-COOH
                    (Substituted Acetone) (Substituted Acetic Acid)
```

### 1. Ketone Cleavage (Dilute Aqueous Acid or Base)
When monoalkylated or dialkylated EAA is hydrolyzed with dilute aqueous sodium hydroxide ($5\%\, \text{NaOH}$) or dilute hydrochloric acid, followed by acidification and gentle heating ($80^\circ\text{–}100^\circ\text{C}$):
- Saponification hydrolyzes the ester group to form the $\beta$-keto acid:
  $$\text{CH}_3\text{CO-CH(R)-COOEt} \xrightarrow{\text{dil. NaOH}} \text{CH}_3\text{CO-CH(R)-COOH} + \text{EtOH}$$
- The $\beta$-keto acid undergoes spontaneous, irreversible pericyclic thermal decarboxylation via a six-membered cyclic transition state to furnish a **substituted acetone (methyl ketone)**:
  $$\text{CH}_3\text{CO-CH(R)-COOH} \xrightarrow{\Delta} \text{CH}_3\text{CO-CH}_2\text{-R} + \text{CO}_2\uparrow \tag{7.1}$$
- Yields: Mono- and dialkylacetones ($\text{CH}_3\text{COCH}_2\text{R}$ and $\text{CH}_3\text{COCHRR}'$).

### 2. Acid Cleavage (Concentrated Alcoholic Alkali)
When alkylated EAA is boiled with **concentrated ethanolic potassium hydroxide** ($40\%\, \text{KOH}$):
- The harsh, nucleophilic ethoxide/hydroxide attacks the keto carbonyl carbon rather than the ester carbon.
- The tetrahedral intermediate undergoes retro-Claisen carbon-carbon bond cleavage, breaking the bond between C2 and C3:
  $$\text{CH}_3\text{CO-CH(R)-COOEt} + \text{OH}^- \longrightarrow \text{CH}_3\text{COO}^- + [\text{R-CH-COOEt}]^- \xrightarrow{\text{H}_2\text{O}} \text{CH}_3\text{COOH} + \text{R-CH}_2\text{COOH} \tag{7.2}$$
- Saponification of the ester yields **two carboxylic acid molecules**: one equivalent of acetic acid and one equivalent of the substituted acetic acid ($\text{R-CH}_2\text{COOH}$).""",
                "simulations": []
            },
            {
                "id": "sec7_3",
                "secNumber": "§7.3",
                "title": "Diethyl Malonate Syntheses: Carboxylic Acids, Dicarboxylic Acids & Alicyclics",
                "heading": "Diethyl Malonate Syntheses: Carboxylic Acids, Dicarboxylic Acids & Alicyclics",
                "content": r"""The **malonic ester synthesis** converts diethyl malonate ($\text{DEM}$) into substituted carboxylic acids, dicarboxylic acids, and alicyclic rings with complete regiochemical control.

### Universal Malonic Ester Sequence
$$\begin{aligned}
\text{Step 1 (Deprotonation)}: &\quad \text{CH}_2(\text{COOEt})_2 + \text{NaOEt} \xrightarrow{\text{EtOH}} \text{Na}^+[\text{CH}(\text{COOEt})_2]^- + \text{EtOH} \\
\text{Step 2 (Alkylation)}: &\quad [\text{CH}(\text{COOEt})_2]^- + \text{R-X} \xrightarrow{S_N2} \text{R-CH}(\text{COOEt})_2 + \text{X}^- \\
\text{Step 3 (Optional 2nd Alkylation)}: &\quad \text{R-CH}(\text{COOEt})_2 \xrightarrow{\text{1. NaOEt} \atop \text{2. R'-X}} \text{RR}'\text{C}(\text{COOEt})_2 \\
\text{Step 4 (Hydrolysis & Decarboxylation)}: &\quad \text{RR}'\text{C}(\text{COOEt})_2 \xrightarrow{\text{aq. HCl, reflux}} [\text{RR}'\text{C}(\text{COOH})_2] \xrightarrow{\Delta, -\text{CO}_2\uparrow} \text{RR}'\text{CH-COOH}
\end{aligned} \tag{7.3}$$

Because geminal dicarboxylic acids ($1,1$-diacids) possess the same six-membered cyclic hydrogen-bonded transition state as $\beta$-keto acids, heating above $140^\circ\text{C}$ smoothly expels one molecule of $\text{CO}_2$, delivering pure monoalkyl or dialkyl acetic acids.

### Synthesis of Alicyclic Rings
When diethyl malonate is reacted with an $\alpha,\omega$-dihaloalkane ($\text{Br}-(\text{CH}_2)_n-\text{Br}$) in the presence of two equivalents of sodium ethoxide, intramolecular cyclization furnishes alicyclic rings:

```
Alicyclic Ring Closure via Diethyl Malonate:
1. DEM + NaOEt + Br-(CH2)n-Br ===> Br-(CH2)n-CH(COOEt)2 (Intermolecular SN2)
2. Br-(CH2)n-CH(COOEt)2 + NaOEt ===> Cycloalkane-1,1-dicarboxylate (Intramolecular SN2)
3. H3O+, heat (- CO2) ===> Cycloalkanecarboxylic Acid
```

- With 1,2-dibromoethane ($n=2$): Yields **cyclopropanecarboxylic acid**.
- With 1,3-dibromopropane ($n=3$): Yields **cyclobutanecarboxylic acid**.
- With 1,4-dibromobutane ($n=4$): Yields **cyclopentanecarboxylic acid**.
- With 1,5-dibromopentane ($n=5$): Yields **cyclohexanecarboxylic acid**.""",
                "simulations": []
            },
            {
                "id": "sec7_4",
                "secNumber": "§7.4",
                "title": "Michael Conjugate 1,4-Addition: Hard vs Soft Nucleophile Dynamics",
                "heading": "Michael Conjugate 1,4-Addition: Hard vs Soft Nucleophile Dynamics",
                "content": r"""$\alpha,\beta$-Unsaturated carbonyl compounds (enones and enals) possess two electrophilic sites:
- **C2 (Carbonyl Carbon)**: Hard electrophilic site, governed by large partial positive charge and electrostatic Coulombic interactions.
- **C4 ($\beta$-Carbon)**: Soft electrophilic site, governed by large frontier orbital LUMO coefficient ($|c_{\text{LUMO},\beta}|^2 > |c_{\text{LUMO},C=O}|^2$).

According to Ralph Pearson's **Hard and Soft Acids and Bases (HSAB) principle**:
- **Hard Nucleophiles** (e.g., organolithiums $\text{RLi}$, Grignard reagents $\text{RMgX}$, $\text{LiAlH}_4$): Attack preferentially at the hard carbonyl carbon (**1,2-addition**).
- **Soft Nucleophiles** (e.g., resonance-stabilized active methylene carbanions, Gilman cuprates $\text{R}_2\text{CuLi}$, thiolates $\text{RS}^-$): Attack preferentially at the soft $\beta$-carbon (**1,4-conjugate addition**, or **Michael addition**).

```
                      Michael Conjugate Addition:
                          O                                      O(-)
                         //                                     /
   CH2(COOEt)2  +   R - CH = CH - C - R'    =====>    (EtO2C)2CH - CH(R) - CH = C - R'
    (Michael Donor)     (Michael Acceptor)                       \
                                                                  v  (Protonation & Enol Tautomerism)
                                                      (EtO2C)2CH - CH(R) - CH2 - CO - R'
                                                               (1,5-Dicarbonyl Adduct)
```

The general Michael reaction couples a **Michael donor** (an active methylene enolate, e.g., malonate, acetoacetate, nitroalkane) with a **Michael acceptor** (an electron-deficient alkene, e.g., methyl vinyl ketone, acrolein, acrylonitrile, diethyl maleate) in the presence of catalytic base ($\text{NaOEt}$ or secondary amine):

$$\text{Michael Donor} + \text{Michael Acceptor} \xrightarrow{\text{cat. base}} \text{1,5-Dicarbonyl Adduct} \tag{7.4}$$

The reaction creates a new carbon-carbon $\sigma$ bond at the $\beta$-position, yielding a versatile **1,5-dicarbonyl compound**.""",
                "simulations": []
            },
            {
                "id": "sec7_5",
                "secNumber": "§7.5",
                "title": "The Robinson Annulation Cascade: Mechanism & Polycyclic Architecture",
                "heading": "The Robinson Annulation Cascade: Mechanism & Polycyclic Architecture",
                "content": r"""Developed by Nobel laureate Sir Robert Robinson in 1935, the **Robinson annulation** is a master cascade reaction for constructing fused six-membered cyclohexenone rings onto existing cyclic ketones. It is the premier synthetic method for constructing the tetracyclic steroid nucleus (cholesterol, cortisone, testosterone) and terpenes.

```
       The Robinson Annulation Cascade:
       Cyclohexanone + Methyl Vinyl Ketone (MVK)
              |
              | Stage 1: Base-catalyzed Michael 1,4-addition
              v
       2-(3-Oxobutyl)cyclohexanone (1,5-Diketone)
              |
              | Stage 2: Intramolecular Aldol Cyclization (forms 6-ring)
              v
       Bicyclic beta-Hydroxy Ketone
              |
              | Stage 3: Base-promoted E1cB Dehydration (- H2O)
              v
       Delta(1,9)-2-Octalone (Fused Bicyclic Enone)
```

### The Three-Stage Cascade Mechanism
The entire sequence occurs in a single reaction vessel under basic catalysis ($\text{KOH, NaOMe}$, or pyrrolidine):

1. **Stage 1: Intermolecular Michael Addition**:
   - Base deprotonates cyclohexanone to form the ketone enolate.
   - The enolate attacks the $\beta$-carbon of **methyl vinyl ketone (MVK)** via a conjugate 1,4-addition.
   - Proton transfer yields a neutral **1,5-diketone** intermediate: 2-(3-oxobutyl)cyclohexanone.
2. **Stage 2: Intramolecular Aldol Addition**:
   - Deprotonation can theoretically occur at four different carbon centers. However, deprotonation at the terminal methyl group of the side chain yields an enolate that attacks the original ring carbonyl.
   - This ring closure forms a thermodynamically stable **six-membered ring** (avoiding strained 4-membered ring alternatives):
     $$\text{Enolate} \xrightarrow{\text{intramolecular aldol}} \text{Bicyclic }\beta\text{-hydroxy ketone}$$
3. **Stage 3: Base-Promoted E1cB Dehydration**:
   - Deprotonation of the $\alpha$-proton adjacent to the ketone carbonyl yields an enolate.
   - Expulsion of hydroxide ($\text{OH}^-$) via the unimolecular conjugate base mechanism ($\text{E1cB}$) eliminates water, driven by the thermodynamic stability of the resulting conjugated enone system.
   - Product: **$\Delta^{1,9}$-2-octalone** (bicyclo[4.4.0]dec-1-en-3-one) in $>80\%$ yield.""",
                "simulations": ["sim_chem_michael_robinson_annulation_cascade"]
            },
            {
                "id": "sec7_6",
                "secNumber": "§7.6",
                "title": "Frontier Molecular Orbital (FMO) Theory of Pericyclic Reactions",
                "heading": "Frontier Molecular Orbital (FMO) Theory of Pericyclic Reactions",
                "content": r"""Pericyclic reactions are concerted chemical transformations that proceed through a continuous cyclic array of overlapping orbitals without discrete carbocation, carbanion, or free-radical intermediates.

The stereochemical outcome of all pericyclic reactions is governed by the **Woodward-Hoffmann rules of orbital symmetry conservation** (Robert Burns Woodward and Roald Hoffmann, 1965), which can be elegantly analyzed using Kenichi Fukui's **Frontier Molecular Orbital (FMO)** method.

### 1. Electrocyclic Reactions
An electrocyclic reaction is the concerted interconversion of a conjugated polyene containing $k$ $\pi$-electrons and a cyclic alkene containing $(k-2)$ $\pi$-electrons and one new $\sigma$ bond:

```
        Woodward-Hoffmann Selection Rules for Electrocyclic Reactions:
        pi Electrons       Thermal Conditions (Delta)      Photochemical (h*nu)
        4n  (e.g., 4 pi)   Conrotatory (Phase-Inversion)   Disrotatory (Suprafacial)
        4n+2 (e.g., 6 pi)  Disrotatory (Suprafacial)        Conrotatory (Phase-Inversion)
```

- **Conrotatory Motion**: Both terminal orbitals rotate in the **same direction** (both clockwise or both counterclockwise).
- **Disrotatory Motion**: The terminal orbitals rotate in **opposite directions** (one clockwise, one counterclockwise).

#### FMO Symmetry Rules:
- Under **thermal conditions ($\Delta$)**, the stereochemistry is determined by the symmetry of the ground-state **HOMO**.
  - In a $4\pi$ system (butadiene, $\psi_2$ is HOMO): The terminal orbital lobes have opposite signs ($C_2$ symmetry). To achieve in-phase constructive bonding overlap ($+ \text{ with } +$), the orbitals must undergo **conrotatory** rotation.
  - In a $6\pi$ system (hexatriene, $\psi_3$ is HOMO): The terminal orbital lobes have identical signs ($m$ symmetry). Constructive overlap requires **disrotatory** rotation.
- Under **photochemical conditions ($h\nu$)**, absorption of a photon promotes an electron to the next orbital ($\psi^*$), inverting the HOMO symmetry and **completely reversing the stereochemical selection rules**!""",
                "simulations": []
            },
            {
                "id": "sec7_7",
                "secNumber": "§7.7",
                "title": "The Diels-Alder [4+2] Cycloaddition: Alder Endo Rule & Secondary Orbital Overlap",
                "heading": "The Diels-Alder [4+2] Cycloaddition: Alder Endo Rule & Secondary Orbital Overlap",
                "content": r"""The **Diels-Alder reaction** is the premier [4+2] cycloaddition, coupling a conjugated diene ($4\pi$ electrons) with a dienophile ($2\pi$ electrons) to form a cyclohexene ring with up to four stereocenters constructed in a single concerted step.

### Orbital Symmetry & Suprafacial Topology
According to the Woodward-Hoffmann rules:
- The thermal $[4_s + 2_s]$ cycloaddition involves suprafacial-suprafacial overlap between the HOMO of the diene and the LUMO of the dienophile (or vice versa in inverse-electron-demand Diels-Alder reactions).
- Because the transition state contains **$6\pi$ electrons**, it is isoelectronic with benzene (aromatic transition state), proceeding with a low activation barrier ($\Delta G^\ddagger \approx 60\text{–}90\text{ kJ}\cdot\text{mol}^{-1}$) and complete stereospecificity.

```
       Diels-Alder Alder Endo Rule & Secondary Orbital Overlap:
                 Diene (Cyclopentadiene)
                    ||       ||
                    \         /
                     \       /
                      \     /
                       \   /
                      /     \
                     /       \
                    ||       ||
                    C ======= C  (Dienophile Alkene)
                    |         |
                    C ======= O  (Carbonyl Group oriented ENDO)
                    \         /
                     Secondary Orbital Overlap (Stabilizes Endo TS by ~12 kJ/mol)
```

### The Alder Endo Rule & Secondary Orbital Overlap
When cyclopentadiene reacts with an unsymmetrical dienophile containing electron-withdrawing carbonyl groups (e.g., maleic anhydride, methyl acrylate), two diastereomeric transition states compete:
1. **Endo Approach**: The electron-withdrawing carbonyl groups of the dienophile point directly underneath the developing cyclohexene ring toward the back-lobes of the diene $\pi$ system.
2. **Exo Approach**: The electron-withdrawing groups point away from the diene ring.

Although the *exo*-product is thermodynamically more stable due to reduced steric congestion in the ground state:
$$\text{Product}: \quad \text{The ENDO diastereomer is formed almost exclusively } (>95\%) \tag{7.5}$$

Why does the *endo* product dominate under kinetic control?
Kurt Alder and Max Stein discovered that in the *endo* transition state, the developing $\pi^*$ orbital of the dienophile's carbonyl groups interacts constructively with the internal $p_z$ orbitals at C2 and C3 of the diene. This **secondary orbital overlap** provides an additional $10\text{–}15\text{ kJ}\cdot\text{mol}^{-1}$ of transition-state resonance stabilization, significantly lowering the activation barrier for *endo* addition:

$$\Delta G^\ddagger(\text{endo}) < \Delta G^\ddagger(\text{exo}) \quad \implies \quad k_{\text{endo}} \gg k_{\text{exo}} \tag{7.6}$$""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob7_1",
                "problemNumber": "7.1",
                "title": "Kurt Meyer Bromine Titration Analysis of Ethyl Acetoacetate Tautomerism",
                "difficulty": "Mastery",
                "statement": r"""A $5.000\text{ g}$ sample of pure ethyl acetoacetate ($\text{EAA}$, molar mass $= 130.14\text{ g/mol}$) is dissolved in $50.0\text{ mL}$ of anhydrous ethanol at $0^\circ\text{C}$. The solution is titrated rapidly by the Kurt Meyer method with a $0.1000\text{ M}$ solution of bromine in ethanol: the enol reacts instantaneously with $\text{Br}_2$, and the excess bromine is immediately quenched with $\beta$-naphthol within 15 seconds before the keto form can enolize. Subsequent addition of potassium iodide ($\text{KI}$) and titration of liberated iodine requires $30.74\text{ mL}$ of $0.1000\text{ M}$ sodium thiosulfate ($\text{Na}_2\text{S}_2\text{O}_3$).
(a) Write the chemical reactions for enol bromination, $\beta$-naphthol quenching, and thiosulfate titration.
(b) Calculate the mass of enol present in the $5.000\text{ g}$ sample and determine the equilibrium enol percentage $(\% \text{ enol})$.
(c) Compute the tautomeric equilibrium constant $K_T = [\text{enol}] / [\text{keto}]$ and the standard Gibbs free energy difference $\Delta G^\circ_T$ for enolization in ethanol at $273.15\text{ K}$.""",
                "hints": ["Each mole of enol consumes exactly 1 mole of Br2.", "$\Delta G^\circ = -RT \ln K_T$."],
                "solution": r"""### (a) Chemical Reactions in Kurt Meyer Titration
1. **Enol Bromination**:
   $$\text{CH}_3\text{-C(OH)}=\text{CH-COOEt} + \text{Br}_2 \xrightarrow{\text{fast, }0^\circ\text{C}} \text{CH}_3\text{-CO-CH(Br)-COOEt} + \text{HBr}$$
   The enol is selectively dibrominated/monobrominated to $\alpha$-bromo-EAA.
2. **$\beta$-Naphthol Quenching**:
   Excess unreacted $\text{Br}_2$ instantly brominates $\beta$-naphthol at C1 to form 1-bromo-2-naphthol, freezing the equilibrium.
3. **Iodometric Titration of $\alpha$-Bromo-EAA**:
   In the presence of $\text{KI}$ and $\text{H}^+$, $\alpha$-bromo-EAA is quantitatively reduced back to EAA, liberating one equivalent of iodine ($\text{I}_2$):
   $$\text{R-CH(Br)-COOEt} + 2\,\text{I}^- + \text{H}^+ \longrightarrow \text{R-CH}_2\text{-COOEt} + \text{I}_2 + \text{Br}^-$$
   The liberated iodine is titrated with sodium thiosulfate:
   $$\text{I}_2 + 2\,\text{S}_2\text{O}_3^{2-} \longrightarrow 2\,\text{I}^- + \text{S}_4\text{O}_6^{2-}$$

### (b) Calculation of Enol Mass and Percentage
1. **Total moles of EAA in sample**:
   $$n_{\text{total}} = \frac{5.000\text{ g}}{130.14\text{ g/mol}} = 0.03842\text{ mol} = 38.42\text{ mmol}$$
2. **Moles of thiosulfate consumed**:
   $$n_{\text{thio}} = 0.03074\text{ L} \times 0.1000\text{ mol/L} = 0.003074\text{ mol} = 3.074\text{ mmol}$$
3. **Moles of enol**:
   Since $1\text{ mol enol} \equiv 1\text{ mol }\text{I}_2 \equiv 2\text{ mol }\text{S}_2\text{O}_3^{2-}$:
   $$n_{\text{enol}} = \frac{n_{\text{thio}}}{2} = \frac{3.074\text{ mmol}}{2} = 1.537\text{ mmol} = 0.001537\text{ mol}$$
4. **Mass of enol**:
   $$m_{\text{enol}} = 0.001537\text{ mol} \times 130.14\text{ g/mol} = 0.2000\text{ g}$$
5. **Percentage enol**:
   $$\% \text{ enol} = \frac{0.2000\text{ g}}{5.000\text{ g}} \times 100\% = \mathbf{4.00\%}$$
   (Percentage keto $= 96.00\%$).

### (c) Equilibrium Constant $K_T$ and $\Delta G^\circ_T$
1. **Tautomeric Constant ($K_T$)**:
   $$K_T = \frac{[\text{enol}]}{[\text{keto}]} = \frac{4.00}{96.00} = \frac{1}{24} \approx 0.04167$$
2. **Gibbs Free Energy ($\Delta G^\circ_T$)**:
   $$\Delta G^\circ_T = -RT \ln K_T$$
   At $T = 273.15\text{ K}$:
   $$\Delta G^\circ_T = -(8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (273.15\text{ K}) \times \ln(0.04167)$$
   $$\ln(0.04167) = -3.178$$
   $$\Delta G^\circ_T = -8.314 \times 273.15 \times (-3.178) = +7217\text{ J}\cdot\text{mol}^{-1} \approx \mathbf{+7.22\text{ kJ}\cdot\text{mol}^{-1}}$$
The keto form is thermodynamically more stable by $7.22\text{ kJ}\cdot\text{mol}^{-1}$ in ethanol at $0^\circ\text{C}$."""
            },
            {
                "id": "prob7_2",
                "problemNumber": "7.2",
                "title": "Synthesis of 3-Methylheptan-2-one via Ethyl Acetoacetate Manifold",
                "difficulty": "Intermediate",
                "statement": r"""Devise an unambiguous chemical synthesis of 3-methylheptan-2-one starting from ethyl acetoacetate.
(a) Provide the complete reaction sequence including all reagents, solvents, and reaction temperatures.
(b) Does the order of alkylation matter (introducing the butyl group first vs the methyl group first)? Justify based on carbanion steric hindrance and monoalkyl vs dialkyl enolate reactivity.
(c) State whether the final cleavage is ketone cleavage or acid cleavage, and write the decarboxylation mechanism.""",
                "hints": ["Target is a methyl ketone: $CH_3-CO-CH(CH_3)-(CH_2)_3CH_3$.", "Introduce the larger alkyl group first when the enolate is less hindered."],
                "solution": r"""### (a) Synthetic Sequence
$$\begin{aligned}
\text{Step 1}: &\quad \text{CH}_3\text{COCH}_2\text{COOEt} + \text{NaOEt} \xrightarrow{\text{EtOH}} \text{Na}^+[\text{CH}_3\text{COCHCOOEt}]^- + \text{EtOH} \\
\text{Step 2}: &\quad \text{Enolate} + \text{CH}_3(\text{CH}_2)_3\text{Br (1-bromobutane)} \xrightarrow{\Delta, S_N2} \text{CH}_3\text{COCH(}n\text{-Bu)COOEt} + \text{NaBr}\downarrow \\
\text{Step 3}: &\quad \text{CH}_3\text{COCH(}n\text{-Bu)COOEt} + \text{NaOEt} \xrightarrow{\text{EtOH}} \text{Na}^+[\text{CH}_3\text{COC(}n\text{-Bu)COOEt}]^- \\
\text{Step 4}: &\quad \text{Dialkyl enolate} + \text{CH}_3\text{I (iodomethane)} \xrightarrow{25^\circ\text{C}, S_N2} \text{CH}_3\text{COC(Me)(}n\text{-Bu)COOEt} + \text{NaI}\downarrow \\
\text{Step 5}: &\quad \text{Dialkylated EAA} \xrightarrow{\text{5\% aq. NaOH, reflux}} \text{Sodium carboxylate salt} \\
\text{Step 6}: &\quad \text{Acidify with dilute }\text{H}_2\text{SO}_4 \text{ and heat to }90^\circ\text{C} \xrightarrow{-\text{CO}_2\uparrow} \text{CH}_3\text{COCH(Me)(}n\text{-Bu)} \quad (\text{3-methylheptan-2-one})
\end{aligned}$$

### (b) Order of Alkylation Rationale
The order of alkylation is **strategically critical**:
- **Introduce the larger group ($n$-butyl) first**: The unsubstituted EAA enolate ($[\text{CH}_3\text{COCHCOOEt}]^-$) is completely unhindered, allowing facile $S_N2$ displacement of primary 1-bromobutane.
- **Introduce the smaller methyl group second**: In the monoalkylated intermediate, the $\alpha$-carbon is now secondary and sterically congested. Methyl iodide ($\text{CH}_3\text{I}$) is the most reactive, least sterically hindered alkylating agent known, easily penetrating the crowded dialkyl enolate without competing E2 elimination.
- If methyl were introduced first, trying to displace 1-bromobutane onto the sterically crowded secondary enolate would result in significant E2 elimination of 1-bromobutane to 1-butene.

### (c) Cleavage Manifold & Decarboxylation
The final step is **ketone cleavage**. Saponification of the ester yields the $\beta$-keto acid:
$$\text{CH}_3-\text{CO}-\text{C(Me)}(n\text{-Bu})-\text{COOH}$$
Upon heating, the carboxyl proton forms an intramolecular hydrogen bond with the keto oxygen. Simultaneous six-electron pericyclic rearrangement expels $\text{CO}_2$, yielding the enol of 3-methylheptan-2-one, which instantly tautomerizes to **3-methylheptan-2-one**."""
            },
            {
                "id": "prob7_3",
                "problemNumber": "7.3",
                "title": "Synthesis of Cyclobutanecarboxylic Acid via Diethyl Malonate",
                "difficulty": "Intermediate",
                "statement": r"""Outline the total laboratory synthesis of cyclobutanecarboxylic acid starting from diethyl malonate and 1,3-dibromopropane.
(a) Provide all reagents and reaction conditions for each step.
(b) Explain why intramolecular cyclization to form a 4-membered ring succeeds in high yield despite the significant Baeyer angle strain ($\sim 110\text{ kJ/mol}$) of the cyclobutane ring.
(c) What product would form if 1,4-dibromobutane were used instead?""",
                "hints": ["Requires two equivalents of sodium ethoxide.", "Consider high dilution conditions to favor intramolecular over intermolecular reaction."],
                "solution": r"""### (a) Reaction Sequence
$$\begin{aligned}
\text{Step 1}: &\quad \text{CH}_2(\text{COOEt})_2 + \text{NaOEt} \xrightarrow{\text{EtOH}} \text{Na}^+[\text{CH}(\text{COOEt})_2]^- + \text{EtOH} \\
\text{Step 2}: &\quad [\text{CH}(\text{COOEt})_2]^- + \text{Br-CH}_2\text{CH}_2\text{CH}_2\text{Br} \longrightarrow \text{Br-CH}_2\text{CH}_2\text{CH}_2\text{-CH}(\text{COOEt})_2 + \text{NaBr}\downarrow \\
\text{Step 3}: &\quad \text{Intermediate} + \text{NaOEt (2nd equiv)} \xrightarrow{\text{high dilution, reflux}} \text{Diethyl cyclobutane-1,1-dicarboxylate} + \text{NaBr}\downarrow \\
\text{Step 4}: &\quad \text{Diester} \xrightarrow{\text{aq. KOH, reflux, then acidify with HCl}} \text{Cyclobutane-1,1-dicarboxylic acid} \\
\text{Step 5}: &\quad \text{Cyclobutane-1,1-dicarboxylic acid} \xrightarrow{\text{heat, }160^\circ\text{C}} \text{Cyclobutanecarboxylic acid} + \text{CO}_2\uparrow
\end{aligned}$$

### (b) Rationale for Successful Four-Membered Ring Closure
Although cyclobutane possesses substantial ring strain ($\sim 110\text{ kJ}\cdot\text{mol}^{-1}$), the intramolecular ring-closure step (Step 3) succeeds for two reasons:
1. **Entropic Advantage (Effective Molarity)**: Once the alkyl chain is attached to the $\alpha$-carbon, the second nucleophilic enolate and the terminal electrophilic $\text{C}-\text{Br}$ group are tethered within the same molecule. The effective concentration (effective molarity) of the intramolecular partner is on the order of $10\text{–}100\text{ M}$, far exceeding the bulk concentration of external reactants.
2. **High-Dilution Conditions**: Performing the reaction under high dilution suppresses bimolecular intermolecular coupling with a second DEM molecule.
Subsequent thermal decarboxylation of the geminal dicarboxylic acid smoothly removes one carboxyl group, delivering cyclobutanecarboxylic acid.

### (c) Reaction with 1,4-Dibromobutane
If 1,4-dibromopropane ($\text{Br}-(\text{CH}_2)_4-\text{Br}$) is used, intramolecular cyclization forms a five-membered ring (**cyclopentanecarboxylic acid**) in even higher yield ($>85\%$), because the five-membered cyclopentane ring has virtually zero angle strain."""
            },
            {
                "id": "prob7_4",
                "problemNumber": "7.4",
                "title": "Complete Mechanistic Proof of the Robinson Annulation Cascade",
                "difficulty": "Mastery",
                "statement": r"""The Robinson annulation of 2-methylcyclohexanone with methyl vinyl ketone (MVK) in the presence of sodium methoxide in methanol yields a single fused bicyclic product.
(a) Draw the complete step-by-step curved-arrow mechanism for all three stages: Michael addition, intramolecular aldol cyclization, and E1cB dehydration.
(b) Why does the thermodynamic enolate of 2-methylcyclohexanone react selectively with MVK?
(c) Identify the exact chemical structure of the final fused bicyclic enone product (including the position of the angular methyl group).""",
                "hints": ["Thermodynamic enolate forms at C2 (more substituted).", "The final product is 4a-methyl-4,4a,5,6,7,8-hexahydronaphthalen-2(3H)-one."],
                "solution": r"""### (a) Step-by-Step Reaction Mechanism
1. **Stage 1 (Michael Addition)**:
   - Deprotonation of 2-methylcyclohexanone by $\text{NaOMe}$ in methanol at room temperature forms the thermodynamic enolate at C2:
     $$\text{Enolate}: \quad \text{1-methyl-2-oxocyclohexan-1-ide (carbanion at C2)}$$
   - Conjugate 1,4-addition of the C2 carbanion to the terminal $\beta$-carbon of MVK ($\text{CH}_2=\text{CH}-\text{CO}-\text{CH}_3$):
     $$\text{C2-carbanion} + \text{CH}_2=\text{CH-COCH}_3 \longrightarrow \text{enolate of MVK}$$
   - Protonation by methanol gives the 1,5-diketone: **2-methyl-2-(3-oxobutyl)cyclohexanone**.
2. **Stage 2 (Intramolecular Aldol Cyclization)**:
   - Base deprotonates the terminal methyl group of the 3-oxobutyl side chain:
     $$\text{Side-chain carbanion}: \quad -\text{CH}_2-\text{CO}-\text{CH}_2^-$$
   - The carbanion attacks the original ring carbonyl carbon (C1) in an intramolecular aldol addition:
     $$\text{Attack}: \quad \text{forms a stable fused 6-membered ring alkoxide}$$
   - Protonation by solvent yields the bicyclic $\beta$-hydroxy ketone intermediate.
3. **Stage 3 ($\text{E1cB}$ Dehydration)**:
   - Base deprotonates the $\alpha$-proton adjacent to the newly formed ketone carbonyl:
     $$\text{Forms a conjugated enolate intermediate}$$
   - Elimination of hydroxide ($\text{OH}^-$) restores carbonyl conjugation, driven by the thermodynamic stability of the $\alpha,\beta$-unsaturated enone system.

### (b) Regioselectivity of the Initial Enolate
Under equilibrating conditions (protic methanol solvent, sodium methoxide base, $25^\circ\text{C}$), proton exchange between ketone molecules is rapid. The thermodynamic enolate (tetrasubstituted double bond at C1-C2) is $\sim 8\text{ kJ}\cdot\text{mol}^{-1}$ more stable than the kinetic enolate (trisubstituted double bond at C1-C6).
Consequently, conjugate addition occurs almost exclusively at **C2**, placing the newly appended side chain at the quaternary carbon.

### (c) Final Product Structure
The product is **4a-methyl-4,4a,5,6,7,8-hexahydronaphthalen-2(3H)-one** (commonly known as **4a-methyl-$\Delta^{1,9}$-2-octalone**).
The methyl group resides as an **angular methyl group** at the bridgehead C4a position, precisely mimicking the C10 angular methyl group of the steroid steroid skeleton (e.g., in progesterone and testosterone)."""
            },
            {
                "id": "prob7_5",
                "problemNumber": "7.5",
                "title": "Woodward-Hoffmann FMO Orbital Symmetry Analysis of Electrocyclic Reactions",
                "difficulty": "Mastery",
                "statement": r"""Consider the thermal and photochemical ring opening and ring closure of (2E,4Z,6E)-octa-2,4,6-triene and (2E,4E)-hexa-2,4-diene.
(a) Predict the stereochemical configuration (cis vs trans) of the 5,6-dimethylcyclohexa-1,3-diene formed by thermal cyclization of (2E,4Z,6E)-octa-2,4,6-triene.
(b) Predict the stereochemical configuration of the 3,4-dimethylcyclobutene formed by thermal cyclization of (2E,4E)-hexa-2,4-diene.
(c) Using orbital symmetry diagrams of $\psi_2$ (for $4\pi$) and $\psi_3$ (for $6\pi$), prove why thermal $4\pi$ electrocyclization is conrotatory while thermal $6\pi$ electrocyclization is disrotatory.""",
                "hints": ["Look at the signs of the terminal orbital lobes in the HOMO.", "In-phase overlap ($+ \text{ with } +$) is required for bond formation."],
                "solution": r"""### (a) Thermal Cyclization of (2E,4Z,6E)-Octa-2,4,6-triene ($6\pi$ System)
- This is a thermal $6\pi$-electron electrocyclic ring closure.
- According to the Woodward-Hoffmann rules, a thermal $(4n+2)$ system ($n=1$) proceeds with **disrotatory** motion.
- In *(2E,4Z,6E)*-octatriene, the two terminal methyl groups point in opposite directions relative to the polyene backbone.
- Disrotatory rotation (one bond rotates clockwise, one counterclockwise) brings the two terminal methyl groups to the same side of the forming ring:
  $$\text{Product}: \quad \mathbf{cis\text{-5,6-dimethylcyclohexa-1,3-diene}}$$

### (b) Thermal Cyclization of (2E,4E)-Hexa-2,4-diene ($4\pi$ System)
- This is a thermal $4\pi$-electron electrocyclic ring closure.
- According to the Woodward-Hoffmann rules, a thermal $4n$ system ($n=1$) proceeds with **conrotatory** motion.
- In *(2E,4E)*-hexadiene, both terminal methyl groups point outward.
- Conrotatory rotation (both rotate clockwise, or both rotate counterclockwise) rotates one methyl group UP and the other methyl group DOWN:
  $$\text{Product}: \quad \mathbf{trans\text{-3,4-dimethylcyclobutene}}$$

### (c) FMO Symmetry Proof
1. **$4\pi$ System (Butadiene / Hexadiene, HOMO is $\psi_2$)**:
   $$\psi_2 = c_1 \chi_1 + c_2 \chi_2 - c_3 \chi_3 - c_4 \chi_4$$
   The terminal coefficients have **opposite signs**:
   $$c_1 > 0 \quad (\text{top lobe is } +), \quad c_4 < 0 \quad (\text{top lobe is } -)$$
   The orbital possesses $C_2$ rotational symmetry.
   To achieve constructive in-phase overlap ($+ \text{ with } +$) between C1 and C4:
   - Rotating C1 clockwise brings the $(+)$ lobe inward.
   - Rotating C4 clockwise brings the $(+)$ lobe (originally bottom) inward.
   Both orbitals rotate in the **same direction (conrotatory)**.
2. **$6\pi$ System (Hexatriene / Octatriene, HOMO is $\psi_3$)**:
   $$\psi_3 = c_1 \chi_1 + c_2 \chi_2 - c_3 \chi_3 - c_4 \chi_4 + c_5 \chi_5 + c_6 \chi_6$$
   The terminal coefficients have **identical signs**:
   $$c_1 > 0 \quad (\text{top lobe is } +), \quad c_6 > 0 \quad (\text{top lobe is } +)$$
   The orbital possesses mirror plane symmetry ($m$).
   To bring both $(+)$ lobes together in-phase:
   - C1 must rotate clockwise (lobe turns right).
   - C6 must rotate counterclockwise (lobe turns left).
   The orbitals rotate in **opposite directions (disrotatory)**.
This rigorously proves the Woodward-Hoffmann selection rules."""
            },
            {
                "id": "prob7_6",
                "problemNumber": "7.6",
                "title": "Secondary Orbital Overlap & Endo Selectivity in the Diels-Alder Reaction",
                "difficulty": "Mastery",
                "statement": r"""Cyclopentadiene reacts with maleic anhydride in benzene at $25^\circ\text{C}$ to give exclusively the endo-cycloadduct ($>99\%$), whereas at $200^\circ\text{C}$ for 24 hours, the exo-cycloadduct predominates ($>80\%$).
(a) Draw three-dimensional representations of the endo and exo transition states.
(b) Using frontier molecular orbital coefficients of the diene HOMO and dienophile LUMO, illustrate the secondary orbital interaction responsible for lowering $\Delta G^\ddagger(\text{endo})$.
(c) Explain why heating to $200^\circ\text{C}$ shifts the product distribution to the exo isomer, calculating the thermodynamic equilibrium parameters.""",
                "hints": ["Exo product is thermodynamically more stable due to lack of steric clash.", "High temperature renders the Diels-Alder reaction reversible."],
                "solution": r"""### (a) Three-Dimensional Transition States
- **Endo Transition State**: Cyclopentadiene sits over maleic anhydride such that the anhydride carbonyl groups ($-\text{C}(=\text{O})-\text{O}-\text{C}(=\text{O})-$) project directly **underneath the developing bicyclic norbornene ring**, oriented toward the internal C2 and C3 carbons of the diene.
- **Exo Transition State**: Maleic anhydride is oriented such that its carbonyl groups project **away** into open space, pointing outward from the norbornene bridgehead.

### (b) Secondary Orbital Overlap Mechanics
In the **endo transition state**:
1. **Primary Overlap (Bond-Forming)**:
   The terminal carbons of cyclopentadiene (C1 and C4) overlap constructively with the alkene carbons of maleic anhydride (C5 and C6):
   $$S_{\text{primary}} = \langle \psi_{\text{HOMO}}(\text{C1, C4}) | \psi_{\text{LUMO}}(\text{C5, C6}) \rangle$$
2. **Secondary Orbital Overlap (Non-Bonding)**:
   Simultaneously, the large $\pi^*$ lobes of the two **carbonyl groups** on maleic anhydride align directly beneath the internal $p_z$ lobes at C2 and C3 of cyclopentadiene:
   $$S_{\text{secondary}} = \langle \psi_{\text{HOMO}}(\text{C2, C3}) | \psi_{\text{LUMO}}(\text{C=O, C=O}) \rangle > 0$$
   This secondary overlap is constructive (in-phase). Although no covalent bond forms between the carbonyls and C2/C3, it provides an additional stabilization energy:
   $$\Delta \Delta H^\ddagger_{\text{secondary}} \approx -12\text{ to }-15\text{ kJ}\cdot\text{mol}^{-1}$$
   This lowers the activation barrier for the endo transition state:
   $$\Delta G^\ddagger(\text{endo}) < \Delta G^\ddagger(\text{exo}) \implies k_{\text{endo}} \gg k_{\text{exo}}$$
   At $25^\circ\text{C}$, the reaction is kinetically controlled, yielding pure *endo*-adduct.

### (c) Thermodynamic Inversion at $200^\circ\text{C}$
In the ground state:
- The *endo*-adduct experiences severe steric congestion between the *endo*-anhydride ring and the *endo*-protons of the norbornene skeleton.
- The *exo*-adduct is sterically unencumbered and thermodynamically more stable by:
  $$\Delta G^\circ_{\text{exo}} < \Delta G^\circ_{\text{endo}} \quad (\text{by }\sim 15\text{ kJ}\cdot\text{mol}^{-1})$$
At $200^\circ\text{C}$ ($473\text{ K}$), the Diels-Alder reaction becomes fully reversible (retro-Diels-Alder operates). The kinetic *endo*-adduct dissociates back to cyclopentadiene and maleic anhydride, eventually equilibrating to the thermodynamically favored **exo-adduct** ($>80\%$)."""
            },
            {
                "id": "prob7_7",
                "problemNumber": "7.7",
                "title": "Synthesis of Bicyclic Terpenes via Michael Addition and Annulation",
                "difficulty": "Intermediate",
                "statement": r"""Wieland-Miescher ketone is a vital chiral building block for the total synthesis of steroids and clerodane diterpenes.
(a) Provide the starting materials and reaction conditions to synthesize Wieland-Miescher ketone.
(b) How does replacing 2-methylcyclohexanone with 2-methylcyclopentane-1,3-dione alter the reaction (the Hajos-Parrish-Eder-Sauer-Wiechert reaction)?
(c) State the organocatalyst utilized to achieve $>95\%$ enantiomeric excess in this asymmetric annulation.""",
                "hints": ["Wieland-Miescher ketone is formed from 2-methylcyclohexane-1,3-dione and MVK.", "L-proline acts as a natural chiral organocatalyst."],
                "solution": r"""### (a) Synthesis of Wieland-Miescher Ketone
Starting materials: **2-methylcyclohexane-1,3-dione** and **methyl vinyl ketone (MVK)**.
$$\begin{aligned}
\text{Step 1 (Michael Addition)}: &\quad \text{2-methylcyclohexane-1,3-dione} + \text{MVK} \xrightarrow{\text{cat. KOH or Et}_3\text{N, H}_2\text{O, }25^\circ\text{C}} \text{Triketone intermediate} \\
\text{Step 2 (Aldol Cyclization)}: &\quad \text{Triketone} \xrightarrow{\text{pyrrolidine, AcOH, benzene, reflux}} \text{Wieland-Miescher ketone} + \text{H}_2\text{O}
\end{aligned}$$
Product: **8a-methyl-3,4,8,8a-tetrahydronaphthalene-1,6(2H,7H)-dione** (racemic Wieland-Miescher ketone).

### (b) The Hajos-Parrish Reaction (Five-Membered Ring)
When **2-methylcyclopentane-1,3-dione** is condensed with MVK:
- The resulting bicyclic core contains a fused 6-5 ring system (indanedione skeleton) known as the **Hajos-Parrish ketone** (7a-methyl-2,3,7,7a-tetrahydro-1H-indene-1,5(6H)-dione).
- This core is identical to the CD-ring system of cholesterol and estradiol.

### (c) Asymmetric Organocatalysis with L-Proline
In 1971, Zoltan Hajos and David Parrish (Hoffmann-La Roche), and independently Rudolf Wiechert (Schering AG), discovered that replacing achiral amines with catalytic natural amino acid **(S)-proline (L-proline, $3\text{ mol}\%$)** in DMF at room temperature performs the intramolecular aldol cyclization with extraordinary enantioselectivity:
$$\text{Enantiomeric Excess } (ee) > 95\% \quad \text{in favor of }(+)\text{-Hajos-Parrish ketone} \tag{7.7}$$
L-Proline acts as a bifunctional organocatalyst:
1. The secondary amine of proline forms an enamine with the side-chain ketone.
2. The carboxylic acid of proline forms a stereodirecting hydrogen bond to one of the ring carbonyl oxygens.
This historic reaction launched the entire field of **asymmetric organocatalysis** (2021 Nobel Prize in Chemistry to Benjamin List and David MacMillan)."""
            }
        ]
    }

def get_unit_8():
    return {
        "id": "unit8",
        "unitId": "unit8-org2",
        "number": 8,
        "unitNumber": 8,
        "title": "Unit 8: Synthesis of Important Organic Pharmaceuticals & Bio-Actives: Sulfa Antibacterials, Analgesics, Antimalarials, Barbiturates & Artificial Sweeteners",
        "description": "Exhaustive medicinal organic synthesis of foundational pharmaceuticals and bio-active molecules: sulfonamide antibacterials (sulfanilamide, sulfathiazole, sulfamethoxazole) and competitive inhibition of bacterial dihydropteroate synthase (DHPS); antipyretics and analgesics (Aspirin, Paracetamol, Phenacetin) and cyclooxygenase (COX-1/COX-2) active-site Ser530 transesterification; antimalarials (Chloroquine, Primaquine, Pamaquine, Quinacrine) quinoline retrosyntheses; barbiturate sedatives (Phenobarbital, Barbital, Pentobarbital) malonic ester condensations with urea; and artificial sweeteners (Saccharin, Cyclamate) syntheses, receptor docking, and structure-activity relationships.",
        "leadSummary": "Comprehensive physical organic treatise on pharmaceutical total syntheses, target active-site docking, enzyme inactivation kinetics, sulfonamide antimetabolite design, COX acetylation mechanisms, and structure-activity relationships.",
        "simulations": ["sim_chem_drug_docking_target_binding"],
        "sections": [
            {
                "id": "sec8_1",
                "secNumber": "§8.1",
                "title": "Sulfonamide Antibacterials: Prontosil, Sulfanilamide & DHPS Inhibition",
                "heading": "Sulfonamide Antibacterials: Prontosil, Sulfanilamide & DHPS Inhibition",
                "content": r"""Sulfonamides represent the first synthetic systemic antibacterial agents discovered in medical history. In 1932, Gerhard Domagk discovered that the red azo dye **Prontosil** protected mice against lethal streptococcal infections (1939 Nobel Prize). In 1935, Jacques and Thérèse Tréfouël at the Pasteur Institute proved that Prontosil itself is biologically inactive *in vitro*; it acts as a **prodrug** metabolically cleaved in the liver by bacterial azo-reductases to release active **sulfanilamide** (4-aminobenzenesulfonamide).

```
                      Prontosil Metabolic Activation:
        H2N                  NH2
          \                /
           [ Benzene Ring ] - N = N - [ Benzene Ring ] - SO2NH2  (Prontosil, Red Dye)
                                |
                                | Hepatic Azo-Reductase (+ 4 [H])
                                v
                   H2N - [ Benzene Ring ] - SO2NH2   (Sulfanilamide, Active Drug)
                                 +
                    Benzene-1,2,4-triamine           (Colorless By-Product)
```

### Molecular Mechanism of Action: Antimetabolite Mimicry
Sulfonamides act as bacteriostatic antimetabolites through structural mimicry of **$p$-aminobenzoic acid (PABA)**:

```
    PABA (Natural Substrate)                 Sulfanilamide (Antimetabolite Drug)
              COOH                                         SO2NH2
                |                                             |
         [ Benzene Ring ]                              [ Benzene Ring ]
                |                                             |
               NH2                                           NH2
      Distance C-N: 6.7 Å                           Distance S-N: 6.9 Å
```

1. **Biosynthetic Pathway**: Bacteria must synthesize folic acid (vitamin B9) *de novo* to produce purine and pyrimidine nucleotides for DNA replication. The enzyme **dihydropteroate synthase (DHPS)** catalyzes the condensation of 6-hydroxymethyl-7,8-dihydropterin pyrophosphate with PABA.
2. **Competitive Inhibition**: Sulfanilamide has nearly identical electronic dimensions to PABA ($d_{\text{C-N}} \approx 6.7\text{ \AA}$ in PABA vs $d_{\text{S-N}} \approx 6.9\text{ \AA}$ in sulfanilamide). Sulfanilamide binds directly into the PABA-binding pocket of DHPS, acting as a potent competitive inhibitor ($K_i \approx 10^{-6}\text{ M}$).
3. **Selective Toxicity**: Mammals lack the DHPS enzyme entirely and obtain folic acid pre-formed from dietary sources via active transport, rendering sulfonamides harmless to human host cells while starving bacterial pathogens of essential folate cofactors.""",
                "simulations": ["sim_chem_drug_docking_target_binding"]
            },
            {
                "id": "sec8_2",
                "secNumber": "§8.2",
                "title": "Second-Generation Sulfas: Sulfathiazole & Sulfamethoxazole Syntheses",
                "heading": "Second-Generation Sulfas: Sulfathiazole & Sulfamethoxazole Syntheses",
                "content": r"""While sulfanilamide revolutionized antibacterial therapy, its low water solubility at acidic urinary $\text{pH}$ caused dangerous crystalluria and renal tubular damage. Second-generation sulfonamides replace the sulfonamide amide proton ($-\text{SO}_2\text{NH}_2$) with heterocyclic rings to lower the sulfonamide $\text{p}K_a$, ensuring high solubility and improved target binding.

### Sulfamethoxazole Synthesis
Sulfamethoxazole (SMX) is the standard component of the synergistic antibiotic **Co-trimoxazole** (combined with trimethoprim):

$$\begin{aligned}
\text{Step 1}: &\quad \text{Aniline} + \text{Ac}_2\text{O} \longrightarrow \text{Acetanilide} \\
\text{Step 2}: &\quad \text{Acetanilide} + 2\,\text{ClSO}_3\text{H} \xrightarrow{60^\circ\text{C}} 4\text{-acetamidobenzenesulfonyl chloride} + \text{H}_2\text{SO}_4 + \text{HCl}\uparrow \\
\text{Step 3}: &\quad 4\text{-acetamidobenzenesulfonyl chloride} + \text{3-amino-5-methylisoxazole} \xrightarrow{\text{pyridine}} N\text{-protected sulfamethoxazole} \\
\text{Step 4}: &\quad N\text{-protected SMX} \xrightarrow{\text{aq. NaOH, reflux, then acidify to pH 5.5}} \text{Sulfamethoxazole (SMX)}
\end{aligned} \tag{8.1}$$

```
                Sulfamethoxazole Structure:
                          N - O
                        //     \
          H2N - C6H4 - SO2 - NH - C     C - CH3
                                   \   //
                                     CH
```

By introducing the electron-withdrawing 5-methylisoxazole ring, the sulfonamide $\text{p}K_a$ drops from $10.4$ in sulfanilamide to **$\text{p}K_a \approx 5.6$** in sulfamethoxazole. At physiological $\text{pH}$ ($7.4$), sulfamethoxazole exists predominantly ($>98\%$) in the ionized, highly soluble sulfonamidate form ($-\text{SO}_2\text{N}^-\text{-R}$), precluding renal crystallization.""",
                "simulations": []
            },
            {
                "id": "sec8_3",
                "secNumber": "§8.3",
                "title": "Antipyretics & Analgesics: Aspirin, Paracetamol & Phenacetin Syntheses",
                "heading": "Antipyretics & Analgesics: Aspirin, Paracetamol & Phenacetin Syntheses",
                "content": r"""Non-steroidal anti-inflammatory drugs (NSAIDs) and antipyretic analgesics constitute the most widely consumed classes of pharmaceuticals worldwide.

### 1. Aspirin (Acetylsalicylic Acid)
Synthesized commercially via the **Kolbe-Schmitt reaction** followed by $O$-acetylation:

$$\begin{aligned}
\text{Stage 1 (Kolbe-Schmitt)}: &\quad \text{Sodium phenoxide} + \text{CO}_2 \xrightarrow{125^\circ\text{C}, 100\text{ atm}} \text{Sodium salicylate} \xrightarrow{\text{H}^+} \text{Salicylic acid} \\
\text{Stage 2 (Acetylation)}: &\quad \text{Salicylic acid} + \text{Ac}_2\text{O} \xrightarrow{\text{cat. }\text{H}_3\text{PO}_4 \text{ or H}_2\text{SO}_4, 85^\circ\text{C}} \text{Aspirin} + \text{CH}_3\text{COOH}
\end{aligned} \tag{8.2}$$

### 2. Paracetamol (Acetaminophen)
Manufactured from $p$-nitrophenol:

$$\begin{aligned}
\text{Stage 1}: &\quad 4\text{-nitrophenol} \xrightarrow{\text{H}_2, \text{Pd/C or Fe / HCl}} 4\text{-aminophenol} \\
\text{Stage 2 (Chemoselective Acetylation)}: &\quad 4\text{-aminophenol} + \text{Ac}_2\text{O} \xrightarrow{\text{aq. buffer, }60^\circ\text{C}} 4\text{-acetamidophenol (Paracetamol)}
\end{aligned} \tag{8.3}$$

Because nitrogen is substantially more nucleophilic than oxygen ($\text{HOMO}_{\text{N}} > \text{HOMO}_{\text{O}}$), acetylation occurs exclusively at the amino nitrogen without touching the phenolic hydroxyl group.

### 3. Phenacetin ($p$-Ethoxyacetanilide)
Prepared from $p$-nitrophenol via Williamson ether synthesis followed by reduction and acetylation:

$$\text{4-nitrophenol} \xrightarrow{\text{EtBr, } \text{K}_2\text{CO}_3} \text{4-ethoxynitrobenzene} \xrightarrow{\text{Sn / HCl}} \text{4-ethoxyaniline (}p\text{-phenetidine)} \xrightarrow{\text{Ac}_2\text{O}} \text{Phenacetin} \tag{8.4}$$""",
                "simulations": []
            },
            {
                "id": "sec8_4",
                "secNumber": "§8.4",
                "title": "Cyclooxygenase (COX-1/COX-2) Active-Site Transesterification Kinetics",
                "heading": "Cyclooxygenase (COX-1/COX-2) Active-Site Transesterification Kinetics",
                "content": r"""The pharmacological mechanism of aspirin was elucidated by Sir John Vane in 1971 (1982 Nobel Prize). Aspirin is the only NSAID that acts as an **irreversible covalent inhibitor** of cyclooxygenase enzymes (COX-1 and COX-2).

### Active-Site Architecture & Ser530 Acetylation
Cyclooxygenase converts arachidonic acid into prostaglandin $\text{H}_2$ ($\text{PGH}_2$), the biosynthetic precursor of proinflammatory prostaglandins and thromboxane $\text{A}_2$.
- The catalytic active site of COX-1 is a narrow, hydrophobic channel $25\text{ \AA}$ long and $8\text{ \AA}$ wide extending deep into the interior of the enzyme.
- At the apex of this channel lies **Serine-530 (Ser530)**, adjacent to the catalytic Tyrosine-385 (Tyr385).

```
          Aspirin Inactivation of Cyclooxygenase (COX-1):
     Hydrophobic Channel                     Aspirin Docking
       |             |                        |             |
       |  Ser530-OH  |   +   Aspirin   ===>   | Ser530-O-Ac |  + Salicylate (Leaves)
       |             |  (Ar-O-COCH3)          |             |
       |  Catalytic  |                        |  CHANNEL    |
       |   Tyr385    |                        |   BLOCKED   |
```

When aspirin enters the channel:
1. The carboxylate group of aspirin forms an electrostatic salt bridge with **Arg120** at the channel constriction.
2. The acetyl ester of aspirin aligns directly with the nucleophilic hydroxyl group of **Ser530**.
3. A transesterification reaction occurs:
   $$\text{COX-Ser530-OH} + \text{Aspirin} \longrightarrow \text{COX-Ser530-O-COCH}_3 + \text{Salicylic acid}\downarrow \tag{8.5}$$
4. The bulky covalently bound acetyl group physically obstructs the channel, permanently preventing arachidonic acid from reaching Tyr385.
5. In blood platelets (which lack nuclei and cannot synthesize new protein), COX-1 acetylation is irreversible, permanently abolishing thromboxane $\text{A}_2$ production for the entire 8- to 10-day lifespan of the platelet, explaining aspirin's cardioprotective antithrombotic efficacy.""",
                "simulations": []
            },
            {
                "id": "sec8_5",
                "secNumber": "§8.5",
                "title": "Antimalarials: Chloroquine, Primaquine & Quinacrine Retrosyntheses",
                "heading": "Antimalarials: Chloroquine, Primaquine & Quinacrine Retrosyntheses",
                "content": r"""Malaria, caused by the protozoan parasite *Plasmodium falciparum*, has spurred some of the most sophisticated heterocyclic drug designs in history.

### Chloroquine Total Retrosynthesis
**Chloroquine** (7-chloro-4-[[4-(diethylamino)-1-methylbutyl]amino]quinoline) consists of a 4-aminoquinoline core coupled to a basic diamine side chain:

```
                      Chloroquine Retrosynthetic Disconnection:
                              Cl
                               \
                                [ Quinoline Core ] - NH - CH(CH3)-(CH2)3-N(Et)2
                                      |
                                      +====== Disconnection (SNAr)
                                     / \
                4,7-Dichloroquinoline   4-Diethylamino-1-methylbutylamine
```

1. **Synthesis of the Side Chain (Novoliamine)**:
   $$\text{CH}_3\text{COCH}_2\text{CH}_2\text{CH}_2\text{Cl} + \text{HNEt}_2 \longrightarrow \text{CH}_3\text{CO(CH}_2)_3\text{NEt}_2 \xrightarrow{\text{NH}_3, \text{H}_2, \text{Ni}} \text{H}_2\text{N-CH(Me)(CH}_2)_3\text{NEt}_2 \tag{8.6}$$
2. **Gould-Jacobs Synthesis of 4,7-Dichloroquinoline**:
   - Condensation of 3-chloroaniline with diethyl ethoxymethylenemalonate ($\text{EMME}$):
     $$m\text{-Cl-C}_6\text{H}_4\text{NH}_2 + \text{EtOCH}=\text{C(COOEt)}_2 \longrightarrow m\text{-Cl-C}_6\text{H}_4\text{NH-CH}=\text{C(COOEt)}_2 + \text{EtOH}$$
   - Thermal cyclization in boiling Dowtherm A ($250^\circ\text{C}$) yields ethyl 7-chloro-4-hydroxyquinoline-3-carboxylate.
   - Saponification and thermal decarboxylation gives 7-chloro-4-hydroxyquinoline.
   - Treatment with phosphorus oxychloride ($\text{POCl}_3$) converts the 4-hydroxy group into 4,7-dichloroquinoline.
3. **Final Coupling**:
   Nucleophilic aromatic substitution ($S_N\text{Ar}$) between 4,7-dichloroquinoline and novoliamine in phenol at $120^\circ\text{C}$ delivers pure **Chloroquine**.

### Primaquine & Quinacrine
- **Primaquine**: An 8-aminoquinoline derivative synthesized from 6-methoxy-8-nitroquinoline. Uniquely active against the dormant liver hypnozoite stage of *Plasmodium vivax*.
- **Quinacrine (Mepacrine)**: An acridine derivative synthesized by Ullmann condensation of 2,4-dichlorobenzoic acid with 4-methoxyaniline, followed by cyclization with $\text{POCl}_3$ to 6,9-dichloro-2-methoxyacridine and displacement with novoliamine.""",
                "simulations": []
            },
            {
                "id": "sec8_6",
                "secNumber": "§8.6",
                "title": "Barbiturate Sedatives: Phenobarbital & Pentobarbital Syntheses",
                "heading": "Barbiturate Sedatives: Phenobarbital & Pentobarbital Syntheses",
                "content": r"""Barbiturates are central nervous system depressants derived from **barbituric acid** (pyrimidine-2,4,6(1H,3H,5H)-trione), first synthesized by Adolf von Baeyer in 1864. Barbituric acid itself lacks central nervous system activity; therapeutic sedative-hypnotic properties require **5,5-disubstitution**.

### Total Synthesis of Barbiturates
Barbiturates are synthesized by the base-promoted condensation of 5,5-disubstituted diethyl malonates with **urea** or **thiourea** in anhydrous ethanol:

$$\text{R}_1\text{R}_2\text{C}(\text{COOEt})_2 + \text{H}_2\text{N-CO-NH}_2 \xrightarrow{\text{NaOEt, EtOH, reflux}} \text{5,5-Disubstituted Barbituric Acid} + 2\,\text{EtOH} \tag{8.7}$$

```
                Barbiturate Core Architecture:
                            O
                           //
                         HN -- C == O
                        /        \
                 O == C           C(R1)(R2)
                        \        /
                         HN -- C == O
                           \\
                            O
```

1. **Barbital (5,5-Diethylbarbituric acid)**: First introduced by Emil Fischer and Joseph von Mering in 1903 (Veronal). Synthesized using diethyl diethylmalonate.
2. **Phenobarbital (5-Ethyl-5-phenylbarbituric acid, Luminal)**:
   - Synthesis of diethyl ethylphenylmalonate requires special strategy because bromobenzene cannot undergo $S_N2$ displacement on malonate.
   - Benzyl cyanide is condensed with diethyl carbonate in the presence of $\text{NaOEt}$ to form ethyl $\alpha$-phenylcyanoacetate, followed by ethylation with ethyl bromide, acidic ethanolysis to diethyl ethylphenylmalonate, and final condensation with urea.
   - Phenobarbital acts as a long-acting anticonvulsant and GABA-A receptor allosteric modulator.
3. **Pentobarbital & Thiopental**:
   - Condensation of diethyl ethyl(1-methylbutyl)malonate with urea yields pentobarbital (Nembutal).
   - Condensation with **thiourea** ($\text{H}_2\text{N-CS-NH}_2$) yields **Thiopental** (Pentothal), an ultra-short-acting intravenous anesthetic whose high lipophilicity allows rapid crossing of the blood-brain barrier followed by rapid redistribution into adipose tissue.""",
                "simulations": []
            },
            {
                "id": "sec8_7",
                "secNumber": "§8.7",
                "title": "Artificial Sweeteners: Saccharin, Cyclamate & Receptor Docking",
                "heading": "Artificial Sweeteners: Saccharin, Cyclamate & Receptor Docking",
                "content": r"""Artificial non-nutritive sweeteners provide intense sweetness without caloric load by binding to the heterodimeric **TAS1R2 / TAS1R3 G-protein coupled sweet taste receptor** on human taste bud cells.

### 1. Saccharin (1,2-Benzisothiazol-3(2H)-one 1,1-dioxide)
Discovered accidentally by Constantin Fahlberg and Ira Remsen at Johns Hopkins University in 1879, saccharin is $\sim 300\text{–}500$ times sweeter than sucrose.

#### Remsen-Fahlberg Industrial Synthesis:
$$\begin{aligned}
\text{Step 1}: &\quad \text{Toluene} + 2\,\text{ClSO}_3\text{H} \longrightarrow o\text{-toluenesulfonyl chloride} + p\text{-toluenesulfonyl chloride} + \text{H}_2\text{SO}_4 \\
\text{Step 2}: &\quad \text{Separate } o\text{-isomer} + \text{NH}_3 \longrightarrow o\text{-toluenesulfonamide} + \text{NH}_4\text{Cl} \\
\text{Step 3}: &\quad o\text{-toluenesulfonamide} \xrightarrow{\text{KMnO}_4, \text{aq. NaOH, }60^\circ\text{C}} o\text{-sulfamoylbenzoic acid} \\
\text{Step 4}: &\quad o\text{-sulfamoylbenzoic acid} \xrightarrow{\text{H}^+, \Delta (-\text{H}_2\text{O})} \text{Saccharin}
\end{aligned} \tag{8.8}$$

```
                Saccharin Structure:
                      O
                     //
                    C
                  /   \
           [ Ar ]       NH  (Acidic proton, pKa = 1.6)
                  \   /
                    S == O
                    \\
                     O
```

Due to the powerful electron withdrawal of both the carbonyl and sulfonyl groups, the imide proton is strongly acidic ($\text{p}K_a \approx 1.6$). It is manufactured as the water-soluble sodium salt (sodium saccharin).

### 2. Sodium Cyclamate (Sodium $N$-Cyclohexylsulfamate)
Synthesized by Michael Sveda in 1937 via sulfonation of cyclohexylamine with chlorosulfonic acid or sulfur trioxide, followed by neutralization with $\text{NaOH}$:

$$\text{C}_6\text{H}_{11}\text{NH}_2 + \text{SO}_3 \longrightarrow \text{C}_6\text{H}_{11}\text{NHSO}_3\text{H} \xrightarrow{\text{NaOH}} \text{C}_6\text{H}_{11}\text{NHSO}_3^-\text{Na}^+ + \text{H}_2\text{O} \tag{8.9}$$

Cyclamate is $\sim 30\text{–}50$ times sweeter than sucrose and displays synergistic sweetness when combined in a $10:1$ ratio with saccharin, masking saccharin's bitter metallic aftertaste.""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob8_1",
                "problemNumber": "8.1",
                "title": "Enzyme Kinetics of Sulfanilamide Competitive Inhibition of DHPS",
                "difficulty": "Mastery",
                "statement": r"""Dihydropteroate synthase (DHPS) follows Michaelis-Menten kinetics with natural substrate PABA:
$$v = \frac{V_{\max} [S]}{K_m \left(1 + \frac{[I]}{K_i}\right) + [S]}$$
In an enzymatic assay with purified bacterial DHPS, the kinetic parameters are:
- $V_{\max} = 120\text{ nmol}\cdot\text{min}^{-1}\cdot\text{mg}^{-1}$
- $K_m(\text{PABA}) = 2.50\text{ }\mu\text{M}$
- $K_i(\text{Sulfanilamide}) = 1.25\text{ }\mu\text{M}$
(a) At a physiological PABA concentration of $[S] = 2.50\text{ }\mu\text{M}$, calculate the uninhibited enzymatic rate $v_0$.
(b) Calculate the inhibited enzymatic rate $v_i$ in the presence of $[I] = 10.0\text{ }\mu\text{M}$ sulfanilamide, and determine the percentage inhibition.
(c) How must the PABA concentration $[S]$ be adjusted to restore $90\%$ of $V_{\max}$ in the presence of $10.0\text{ }\mu\text{M}$ sulfanilamide?""",
                "hints": ["For competitive inhibition, $K_m^{\text{app}} = K_m(1 + [I]/K_i)$.", "$V_{\max}$ is unchanged."],
                "solution": r"""### (a) Uninhibited Reaction Rate ($v_0$)
When $[I] = 0$ and $[S] = K_m = 2.50\text{ }\mu\text{M}$:
$$v_0 = \frac{V_{\max} [S]}{K_m + [S]} = \frac{120 \times 2.50}{2.50 + 2.50} = \frac{120}{2} = \mathbf{60.0\text{ nmol}\cdot\text{min}^{-1}\cdot\text{mg}^{-1}}$$

### (b) Inhibited Reaction Rate ($v_i$) and Percentage Inhibition
1. **Apparent Michaelis Constant ($K_m^{\text{app}}$)**:
   $$K_m^{\text{app}} = K_m \left(1 + \frac{[I]}{K_i}\right) = 2.50 \left(1 + \frac{10.0}{1.25}\right) = 2.50(1 + 8) = 2.50 \times 9 = 22.50\text{ }\mu\text{M}$$
2. **Inhibited Rate ($v_i$)**:
   $$v_i = \frac{V_{\max} [S]}{K_m^{\text{app}} + [S]} = \frac{120 \times 2.50}{22.50 + 2.50} = \frac{300}{25.0} = \mathbf{12.0\text{ nmol}\cdot\text{min}^{-1}\cdot\text{mg}^{-1}}$$
3. **Percentage Inhibition**:
   $$\% \text{ Inhibition} = \frac{v_0 - v_i}{v_0} \times 100\% = \frac{60.0 - 12.0}{60.0} \times 100\% = \frac{48.0}{60.0} \times 100\% = \mathbf{80.0\%}$$
Sulfanilamide reduces the bacterial biosynthetic rate of folic acid by $80\%$.

### (c) PABA Concentration Required to Restore $90\%$ of $V_{\max}$
We require:
$$v = 0.90 \, V_{\max} = 0.90 \times 120 = 108\text{ nmol}\cdot\text{min}^{-1}\cdot\text{mg}^{-1}$$
Using the rate equation:
$$\frac{V_{\max} [S]}{K_m^{\text{app}} + [S]} = 0.90 \, V_{\max} \implies \frac{[S]}{K_m^{\text{app}} + [S]} = 0.90$$
$$[S] = 0.90 (K_m^{\text{app}} + [S]) = 0.90 \, K_m^{\text{app}} + 0.90 [S]$$
$$0.10 [S] = 0.90 \, K_m^{\text{app}} \implies [S] = 9 \times K_m^{\text{app}}$$
With $[I] = 10.0\text{ }\mu\text{M}$, $K_m^{\text{app}} = 22.50\text{ }\mu\text{M}$:
$$[S] = 9 \times 22.50\text{ }\mu\text{M} = \mathbf{202.5\text{ }\mu\text{M}}$$
PABA concentration would have to increase by an enormous factor of $81$ ($202.5 / 2.50$) to overcome sulfanilamide inhibition, explaining why bacteria cannot readily overcome sulfonamides under normal physiological conditions."""
            },
            {
                "id": "prob8_2",
                "problemNumber": "8.2",
                "title": "Chemical Proof of Aspirin Covalent Transesterification of COX-1 Ser530",
                "difficulty": "Mastery",
                "statement": r"""When purified sheep seminal vesicle COX-1 is incubated with acetyl-labeled $^{14}\text{C}$-aspirin ($\text{Ar-O-}^{14}\text{COCH}_3$), radioactivity becomes covalently incorporated into the protein ($1.0\text{ mol of }^{14}\text{C / mol of COX-1 monomer}$). However, when incubated with ring-labeled $^{14}\text{C}$-aspirin ($^{14}\text{C-Ar-O-COCH}_3$), zero radioactivity remains bound to the isolated protein.
(a) Write the chemical mechanism of the reaction between Ser530 and aspirin.
(b) Explain why ring-labeled aspirin leaves zero radioactivity in the enzyme while acetyl-labeled aspirin leaves stoichiometric radioactivity.
(c) Contrast this irreversible inhibition with the reversible competitive inhibition of ibuprofen and explain why low-dose aspirin ($81\text{ mg/day}$) confers long-lasting cardiovascular protection.""",
                "hints": ["Salicylate is the leaving group in transesterification.", "Platelets cannot synthesize new COX-1 enzymes."],
                "solution": r"""### (a) Mechanism of Transesterification at Ser530
1. Nucleophilic attack of the Ser530 hydroxyl oxygen on the ester carbonyl of aspirin:
   $$\text{COX-Ser530-CH}_2-\text{OH} + \text{CH}_3\text{CO-O-C}_6\text{H}_4\text{COOH} \longrightarrow \text{Tetrahedral intermediate}$$
2. Collapse of the tetrahedral intermediate expels the salicylate mono-anion leaving group:
   $$\text{Tetrahedral intermediate} \longrightarrow \text{COX-Ser530-CH}_2-\text{O}-\text{COCH}_3 + \text{Salicylic acid}$$
The serine residue is covalently transformed into an $O$-acetyl ester.

### (b) Isotopic Radioactivity Tracking
- **With $^{14}\text{C-acetyl-labeled aspirin}$ ($\text{Ar-O-}^{14}\text{COCH}_3$)**:
  The radioactive $^{14}\text{C}$ atom resides in the acetyl group. During transesterification, the acetyl group becomes covalently attached to the Ser530 side chain. After gel-filtration or washing, the protein retains $1.0\text{ mol of }^{14}\text{C}$ per mole of enzyme.
- **With $^{14}\text{C-ring-labeled aspirin}$ ($^{14}\text{C-Ar-O-COCH}_3$)**:
  The radioactive label resides in the salicylate ring. The salicylate moiety acts strictly as the leaving group, diffusing away from the enzyme channel. The isolated protein is completely non-radioactive.
This definitively proves **irreversible covalent transesterification** rather than tight non-covalent binding.

### (c) Reversible Ibuprofen vs Irreversible Aspirin Cardioprotection
- **Ibuprofen**: Binds non-covalently via reversible competitive binding. When blood concentration drops as the drug is metabolized ($t_{1/2} \approx 2\text{ hours}$), it dissociates from COX-1, restoring full platelet aggregation activity.
- **Low-Dose Aspirin ($81\text{ mg/day}$)**:
  Blood platelets lack a nucleus and ribosomes; they are completely incapable of *de novo* protein synthesis. Once a platelet's COX-1 is acetylated, it remains **permanently inactivated for the remainder of the platelet's 8- to 10-day lifespan**. Thromboxane $\text{A}_2$ production is abolished, preventing arterial blood clots (thrombi) and protecting against myocardial infarction."""
            },
            {
                "id": "prob8_3",
                "problemNumber": "8.3",
                "title": "Industrial Chemoselective Synthesis of Paracetamol",
                "difficulty": "Intermediate",
                "statement": r"""A process chemist synthesizes paracetamol (4-acetamidophenol) from 4-aminophenol and acetic anhydride.
(a) Write the balanced reaction equation.
(b) Explain why acetic anhydride acylates the amino group selectively over the phenolic hydroxyl group under controlled aqueous conditions ($\text{pH } 5\text{–}6, 60^\circ\text{C}$).
(c) What by-product would form if strong acid ($\text{H}_2\text{SO}_4$) and excess acetic anhydride were used at $100^\circ\text{C}$, and how can it be hydrolyzed back to paracetamol?""",
                "hints": ["Nitrogen is more nucleophilic than oxygen.", "Excess acylation yields 4-acetamidophenyl acetate (diacetylated compound)."],
                "solution": r"""### (a) Balanced Chemical Reaction
$$\text{HO-C}_6\text{H}_4\text{-NH}_2 + (\text{CH}_3\text{CO})_2\text{O} \xrightarrow{\text{aq. buffer, }60^\circ\text{C}} \text{HO-C}_6\text{H}_4\text{-NHCOCH}_3 + \text{CH}_3\text{COOH}$$
Product: **4-acetamidophenol (Paracetamol)**.

### (b) Chemoselectivity Rationale: Amine vs Phenol
Although 4-aminophenol contains both an amino group ($-\text{NH}_2$) and a phenolic hydroxyl group ($-\text{OH}$):
1. **Frontier Orbital Energy**: Nitrogen is less electronegative ($\chi_P = 3.04$) than oxygen ($\chi_P = 3.44$). The nitrogen non-bonding lone pair resides in a substantially higher energy orbital ($\text{HOMO}_{\text{N}} > \text{HOMO}_{\text{O}}$), resulting in a much smaller energy gap with the electrophilic carbonyl LUMO ($\pi^*$).
2. **Nucleophilic Kinetics**: The rate constant for amine acylation is thousands of times faster than phenolic acylation ($k_{\text{N}} \gg 10^3 \times k_{\text{O}}$).
Under mild, buffered conditions ($\text{pH } 5\text{–}6$), the amine is predominantly neutral and unprotonated, reacting rapidly with acetic anhydride before the phenolic group can react.

### (c) Diacetylation Side-Reaction and Selective Hydrolysis
If excess acetic anhydride and strong sulfuric acid catalyst are used at $100^\circ\text{C}$, the phenolic hydroxyl group also undergoes acylation to yield the **diacetylated by-product**:
$$\text{CH}_3\text{COO-C}_6\text{H}_4\text{-NHCOCH}_3 \quad (\text{4-acetamidophenyl acetate})$$
To recover pure paracetamol:
- The reaction mixture is treated with dilute aqueous sodium hydroxide ($1\text{ M NaOH}$) at room temperature.
- Esters ($-\text{OCOCH}_3$) undergo base-catalyzed saponification much faster than amides ($-\text{NHCOCH}_3$) ($k_{\text{ester}} \gg 10^4 \times k_{\text{amide}}$).
- The phenolic ester is selectively hydrolyzed to phenoxide, which upon neutralization with dilute $\text{HCl}$ precipitates pure paracetamol."""
            },
            {
                "id": "prob8_4",
                "problemNumber": "8.4",
                "title": "Gould-Jacobs Quinoline Synthesis: Chloroquine 4,7-Dichloroquinoline Core",
                "difficulty": "Mastery",
                "statement": r"""Detail the Gould-Jacobs quinoline synthesis of 4,7-dichloroquinoline from 3-chloroaniline and diethyl ethoxymethylenemalonate (EMME).
(a) Write the complete reaction sequence including the structures of the anilinomethylene intermediate, the cyclized quinolone ester, and the decarboxylated 4-hydroxyquinoline.
(b) Explain why thermal cyclization of the intermediate can theoretically yield both the 7-chloro and 5-chloro regioisomers, and justify why the 7-chloro isomer is isolated as the major product ($>85\%$).
(c) Show how 7-chloro-4-hydroxyquinoline is converted into 4,7-dichloroquinoline using phosphorus oxychloride ($\text{POCl}_3$).""",
                "hints": ["3-Chloroaniline has two positions ortho to the amino group: C6 (leads to 7-chloro) and C2 (leads to 5-chloro).", "Consider steric hindrance around the chlorine atom."],
                "solution": r"""### (a) Gould-Jacobs Reaction Sequence
$$\begin{aligned}
\text{Step 1 (Addition-Elimination)}: &\quad m\text{-Cl-C}_6\text{H}_4\text{NH}_2 + \text{EtO-CH}=\text{C(COOEt)}_2 \xrightarrow{130^\circ\text{C}, -\text{EtOH}} m\text{-Cl-C}_6\text{H}_4\text{NH-CH}=\text{C(COOEt)}_2 \\
\text{Step 2 (Thermal Cyclization)}: &\quad \text{Intermediate} \xrightarrow{\text{Dowtherm A, }250^\circ\text{C}, -\text{EtOH}} \text{Ethyl 7-chloro-4-oxo-1,4-dihydroquinoline-3-carboxylate} \\
\text{Step 3 (Saponification)}: &\quad \text{Quinolone ester} \xrightarrow{\text{10\% aq. NaOH, reflux}} \text{7-chloro-4-hydroxyquinoline-3-carboxylic acid} \\
\text{Step 4 (Decarboxylation)}: &\quad \text{Carboxylic acid} \xrightarrow{\text{heat, }260^\circ\text{C}, -\text{CO}_2\uparrow} \text{7-chloroquinolin-4-ol (7-chloro-4-hydroxyquinoline)}
\end{aligned}$$

### (b) Regioselectivity: 7-Chloro vs 5-Chloro Quinoline
In 3-chloroaniline, the amino group directs electrophilic cyclization to its *ortho* positions:
1. **Attack at C6 position**: Places the chlorine atom at the **C7 position** of the resulting quinoline ring. The C6 carbon is flanked only by an unhindered hydrogen atom at C5, experiencing minimal steric resistance during ring closure.
2. **Attack at C2 position**: Places the chlorine atom at the **C5 position** of the quinoline ring. The C2 carbon is tightly sandwiched between the amino group and the bulky chlorine atom. Severe steric hindrance in the cyclization transition state heavily penalizes this pathway.
Consequently, ring closure occurs overwhelmingly ($>85\%$) at C6, yielding the desired **7-chloro isomer**.

### (c) Chlorination to 4,7-Dichloroquinoline with $\text{POCl}_3$
$$\text{7-chloroquinolin-4-ol} + \text{POCl}_3 \xrightarrow{\text{reflux, }105^\circ\text{C}} \text{4,7-dichloroquinoline} + \text{HPO}_2\text{Cl}_2$$
**Mechanism**:
The 4-hydroxyquinoline exists predominantly in its 4-quinolone lactam tautomer.
1. The carbonyl oxygen attacks the electrophilic phosphorus atom of $\text{POCl}_3$, expelling chloride ($\text{Cl}^-$) and forming an active phosphorodichloridate leaving group:
   $$\text{Quinoline-4-O-P}(=\text{O})\text{Cl}_2$$
2. The liberated chloride ion attacks the C4 position in an $S_N\text{Ar}$ displacement, expelling the phosphorodichloridate anion to furnish **4,7-dichloroquinoline** in quantitative yield."""
            },
            {
                "id": "prob8_5",
                "problemNumber": "8.5",
                "title": "Total Synthesis of Phenobarbital from Benzyl Cyanide",
                "difficulty": "Mastery",
                "statement": r"""A pharmaceutical manufacturing protocol for phenobarbital (5-ethyl-5-phenylpyrimidine-2,4,6(1H,3H,5H)-trione) begins from benzyl cyanide ($\text{PhCH}_2\text{CN}$).
(a) Why cannot phenobarbital be synthesized simply by reacting diethyl malonate with bromobenzene and sodium ethoxide?
(b) Provide the complete five-stage synthetic sequence from benzyl cyanide to phenobarbital, specifying all reagents.
(c) Explain the allosteric mechanism by which phenobarbital modulates the GABA-A receptor in human neuronal synapses.""",
                "hints": ["Aryl halides do not undergo SN2 substitution with malonate.", "Use diethyl carbonate to form alpha-phenylcyanoacetate."],
                "solution": r"""### (a) Impossibility of Direct Arylation of Malonate
Bromobenzene ($\text{Ph-Br}$) is an aryl halide:
- The $sp^2$-hybridized carbon-bromine bond has partial double-bond character due to resonance with the aromatic ring, making it resistant to heterolysis.
- Backside attack ($S_N2$) is geometrically impossible because the ring carbon is planar and the interior of the aromatic ring sterically blocks nucleophilic approach.
Therefore, sodium diethyl malonate cannot displace bromobenzene to form diethyl phenylmalonate.

### (b) Five-Stage Synthesis of Phenobarbital
$$\begin{aligned}
\text{Stage 1 (Carbethoxylation)}: &\quad \text{PhCH}_2\text{CN} + (\text{EtO})_2\text{C}=\text{O (diethyl carbonate)} \xrightarrow{\text{NaOEt, reflux}} \text{PhCH(CN)COOEt} + \text{EtOH} \\
\text{Stage 2 (Ethylation)}: &\quad \text{PhCH(CN)COOEt} + \text{EtBr} \xrightarrow{\text{NaOEt, EtOH, }50^\circ\text{C}} \text{Ph-C(Et)(CN)COOEt} + \text{NaBr}\downarrow \\
\text{Stage 3 (Alcoholysis / Hydrolysis)}: &\quad \text{Ph-C(Et)(CN)COOEt} + \text{EtOH} + \text{H}_2\text{SO}_4 \xrightarrow{\Delta, -\text{NH}_4\text{HSO}_4} \text{Ph-C(Et)(COOEt)}_2 \quad (\text{diethyl ethylphenylmalonate}) \\
\text{Stage 4 (Condensation with Urea)}: &\quad \text{Ph-C(Et)(COOEt)}_2 + \text{H}_2\text{N-CO-NH}_2 \xrightarrow{\text{NaOEt, anhydrous EtOH, reflux, 12 h}} \text{Sodium phenobarbital salt} \\
\text{Stage 5 (Acidification)}: &\quad \text{Sodium salt} \xrightarrow{\text{dilute HCl, pH 2}} \text{Phenobarbital}\downarrow \quad (\text{crystallizes out})
\end{aligned}$$

### (c) Pharmacological GABA-A Receptor Modulation
In the central nervous system:
1. The **$\text{GABA}_A$ receptor** is a ligand-gated chloride ($\text{Cl}^-$) ion channel.
2. Phenobarbital binds to an **allosteric site** on the $\text{GABA}_A$ receptor complex distinct from the GABA-binding site.
3. Binding **prolongs the duration of channel opening bursts** elicited by the inhibitory neurotransmitter GABA.
4. Increased chloride influx hyperpolarizes the postsynaptic neuronal membrane potential (from $-70\text{ mV}$ to $-85\text{ mV}$), raising the threshold for action potential firing and producing profound sedative, hypnotic, and anticonvulsant therapeutic effects."""
            },
            {
                "id": "prob8_6",
                "problemNumber": "8.6",
                "title": "Total Synthesis & Acidity Dynamics of Saccharin",
                "difficulty": "Intermediate",
                "statement": r"""Saccharin (1,2-benzisothiazol-3(2H)-one 1,1-dioxide) exhibits an unusually low $\text{p}K_a$ of $1.60$, rendering it more acidic than benzoic acid ($\text{p}K_a = 4.20$) and acetic acid ($\text{p}K_a = 4.76$).
(a) Provide the complete Remsen-Fahlberg synthetic sequence starting from toluene and chlorosulfonic acid.
(b) Draw the resonance structures of the saccharin conjugate base (saccharinate anion) and explain why the imide proton is so exceptionally acidic.
(c) Why is commercial saccharin packaged as the sodium salt rather than the neutral free acid?""",
                "hints": ["Deprotonation creates an anion flanked by C=O and SO2.", "Sodium saccharin is hundreds of times more water-soluble."],
                "solution": r"""### (a) Remsen-Fahlberg Synthetic Sequence
$$\begin{aligned}
\text{Step 1}: &\quad \text{PhCH}_3 + 2\,\text{ClSO}_3\text{H} \xrightarrow{0\text{–}5^\circ\text{C}} o\text{-CH}_3\text{C}_6\text{H}_4\text{SO}_2\text{Cl} + p\text{-CH}_3\text{C}_6\text{H}_4\text{SO}_2\text{Cl} + \text{H}_2\text{SO}_4 \\
\text{Step 2}: &\quad \text{Separate liquid } o\text{-isomer by chilling; treat with NH}_3 \longrightarrow o\text{-CH}_3\text{C}_6\text{H}_4\text{SO}_2\text{NH}_2 + \text{NH}_4\text{Cl} \\
\text{Step 3}: &\quad o\text{-CH}_3\text{C}_6\text{H}_4\text{SO}_2\text{NH}_2 + 2\,\text{KMnO}_4 \xrightarrow{\text{aq. NaOH, }60^\circ\text{C}} o\text{-KOOC-C}_6\text{H}_4\text{SO}_2\text{NH}_2 + 2\,\text{MnO}_2\downarrow \\
\text{Step 4}: &\quad \text{Acidify with HCl} \longrightarrow \text{o-carboxysulfonamide intermediate} \xrightarrow{\Delta, -\text{H}_2\text{O}} \text{Saccharin}
\end{aligned}$$

### (b) Resonance Stabilization of the Saccharinate Anion
When saccharin loses its imide proton ($-\text{NH}-$):
$$\text{Saccharin} \xrightleftharpoons{K_a = 2.5 \times 10^{-2}} \text{Saccharinate Anion} + \text{H}^+$$
The resulting conjugate base is stabilized by **three powerful electron sinks**:
1. Delocalization onto the carbonyl oxygen, forming an enolate-like resonance structure:
   $$[\text{O}=\text{C}-\text{N}^--\text{SO}_2] \longleftrightarrow [^-\text{O}-\text{C}=\text{N}-\text{SO}_2]$$
2. Delocalization onto both sulfonyl oxygen atoms:
   $$[\text{C}(=\text{O})-\text{N}^--\text{S}(=\text{O})_2] \longleftrightarrow [\text{C}(=\text{O})-\text{N}=\text{S}(\text{O}^-)=\text{O}]$$
3. Inductive withdrawal from the adjacent ortho-fused benzene ring.
Because the negative charge is distributed over four highly electronegative atoms (one nitrogen, three oxygens), the conjugate base is extraordinarily stable, resulting in an acidic $\text{p}K_a \approx 1.60$.

### (c) Packaging as Sodium Salt
Neutral saccharin has very poor water solubility at room temperature ($S \approx 3.4\text{ g/L}$ at $25^\circ\text{C}$).
In contrast, **sodium saccharin** is an ionic salt with massive aqueous solubility ($S > 1000\text{ g/L}$ in water), dissolving instantaneously in beverages and pharmaceutical formulations."""
            },
            {
                "id": "prob8_7",
                "problemNumber": "8.7",
                "title": "Synthesis & Structure-Activity Relationships of Sodium Cyclamate",
                "difficulty": "Intermediate",
                "statement": r"""Sodium cyclamate ($N$-cyclohexylsulfamate sodium salt) is an artificial sweetener discovered in 1937.
(a) Provide the two-step synthesis of sodium cyclamate from cyclohexylamine and sulfur trioxide / chlorosulfonic acid.
(b) How does the chemical structure of cyclamate compare with saccharin in terms of the TAS1R2/TAS1R3 sweet receptor pharmacophore (AH-B-X model)?
(c) Why does a 10:1 mixture of cyclamate and saccharin produce an enhanced synergistic sweetness profile?""",
                "hints": ["Shallenberger's AH-B model involves a hydrogen-bond donor (AH) and acceptor (B).", "Synergy arises from binding to distinct allosteric receptor sites."],
                "solution": r"""### (a) Two-Step Synthesis of Sodium Cyclamate
$$\begin{aligned}
\text{Step 1 (Sulfamoylation)}: &\quad \text{C}_6\text{H}_{11}\text{NH}_2 + \text{SO}_3\cdot\text{pyridine} \xrightarrow{\text{chloroform, }45^\circ\text{C}} \text{C}_6\text{H}_{11}\text{NHSO}_3\text{H}\cdot\text{pyridine} \\
\text{Step 2 (Neutralization)}: &\quad \text{Cyclamic acid} + \text{NaOH} \longrightarrow \text{C}_6\text{H}_{11}\text{NHSO}_3^-\text{Na}^+ + \text{H}_2\text{O}
\end{aligned}$$
Product: **Sodium cyclamate**.

### (b) Shallenberger-Acree AH-B-X Sweet Taste Pharmacophore
According to the Shallenberger-Kier tripartite model of sweetness:
- **$\text{AH}$ (Hydrogen-bond donor)**: Proton on the sulfonamide nitrogen ($-\text{NH}-$).
- **$\text{B}$ (Hydrogen-bond acceptor)**: The sulfonate oxygen atom ($-\text{SO}_3^-$), positioned approximately $2.8\text{–}3.5\text{ \AA}$ from $\text{AH}$.
- **$\text{X}$ (Hydrophobic binding domain)**: The bulky, non-polar cyclohexyl ring ($\text{C}_6\text{H}_{11}$), which docks into a complementary lipophilic pocket of the TAS1R2 receptor subunit.
In saccharin, the hydrophobic domain is the benzene ring, and the $\text{AH-B}$ unit is formed by the acidic imide and carbonyl/sulfonyl oxygens.

### (c) Synergistic Sweetness Profile (10:1 Formulation)
When combined in a $10:1$ mass ratio:
1. **Complementary Receptor Occupancy**: Cyclamate and saccharin bind to distinct allosteric binding pockets within the dimeric TAS1R2/TAS1R3 receptor complex. Simultaneous binding produces a positive cooperative allosteric effect, triggering receptor activation at substantially lower concentrations than either compound alone.
2. **Bitterness Masking**: At concentrations above $0.1\%$, saccharin activates bitter taste receptors (**hTAS2R31** and **hTAS2R43**), creating an unpleasant metallic aftertaste. Cyclamate acts as a competitive antagonist at these specific bitter receptors, completely suppressing saccharin's bitter aftertaste while delivering a clean, sugar-like sweetness profile."""
            }
        ]
    }

def get_unit_9():
    return {
        "id": "unit9",
        "unitId": "unit9-org2",
        "number": 9,
        "unitNumber": 9,
        "title": "Unit 9: Heterocycles with Multiple Heteroatoms & Fused Ring Systems: Imidazole, Pyrimidine, Purine, Indole & Quinoline",
        "description": "Exhaustive treatment of multi-heteroatom and condensed heterocyclic systems: electronic structure and amphoteric equilibria of 1,3-azoles (imidazole, pyrazole, oxazole, thiazole) and Breslow carbene intermediates; pyrimidine and purine nucleic acid bases (uracil, thymine, cytosine, adenine, guanine), lactam-lactim tautomerism, and hydrogen-bonding networks; indole syntheses (Fischer indole, Madelung) and C3 electrophilic substitution regiocontrol; quinoline syntheses (Skraup, Doebner-Miller, Friedländer) and C5/C8 vs C2/C4 reactivity; and isoquinoline syntheses (Bischler-Napieralski, Pictet-Spengler).",
        "leadSummary": "Advanced physical organic analysis of azole amphoterism, purine/pyrimidine tautomerism, Fischer indole sigmatropic cascades, Skraup quinoline annulations, and Pictet-Spengler isoquinoline constructions.",
        "simulations": ["sim_chem_fused_heterocycle_fischer_skraup"],
        "sections": [
            {
                "id": "sec9_1",
                "secNumber": "§9.1",
                "title": "1,3-Azoles: Imidazole, Pyrazole, Oxazole & Thiazole Electronic Architecture",
                "heading": "1,3-Azoles: Imidazole, Pyrazole, Oxazole & Thiazole Electronic Architecture",
                "content": r"""The 1,3-azoles are five-membered aromatic heterocycles containing one heteroatom with a lone pair contributing to the aromatic $\pi$ sextet (a "pyrrole-like" heteroatom: $\text{NH}, \text{O}, \text{S}$) and a second heteroatom with a localized $sp^2$ lone pair in the ring plane (a "pyridine-like" nitrogen):
- **Imidazole**: 1,3-diazole ($\text{C}_3\text{H}_4\text{N}_2$).
- **Pyrazole**: 1,2-diazole ($\text{C}_3\text{H}_4\text{N}_2$).
- **Oxazole**: 1,3-oxazole ($\text{C}_3\text{H}_3\text{NO}$).
- **Thiazole**: 1,3-thiazole ($\text{C}_3\text{H}_3\text{NS}$).

```
       Imidazole Amphoteric Electronic Architecture:
                        H
                        |
                        N1 (Pyrrole-like, lone pair in 6-pi sextet)
                      /   \
                     C5    C2 (Acidic proton, pKa ~ 33)
                     ||    ||
                     C4 -- N3: (Pyridine-like, localized sp2 lone pair, basic)
```

### Imidazole Amphoterism & The Enzyme Catalytic Triad
Imidazole exhibits extraordinary **amphoteric acid-base properties** that render it unique in biological chemistry:
1. **Basicity ($\text{p}K_a \approx 6.95$)**:
   - Protonation occurs at the pyridine-like **N3 nitrogen**, whose $sp^2$ lone pair is not part of the aromatic $\pi$ system.
   - The resulting imidazolium cation is stabilized by degenerate resonance between N1 and N3:
     $$[\text{HN1}-\text{CH}=\text{CH}-\text{N3}^+\text{H}=\text{CH}] \longleftrightarrow [^+\text{HN1}=\text{CH}-\text{CH}=\text{N3H}-\text{CH}]$$
   - Because its $\text{p}K_a$ ($6.95$) is near physiological $\text{pH}$ ($7.4$), the imidazole side chain of the amino acid **histidine** switches rapidly between protonated and neutral states, acting as an ideal proton shuttle in enzymatic general acid-base catalysis.
2. **Acidity ($\text{p}K_a \approx 14.5$)**:
   - Deprotonation of the pyrrole-like N1 proton by strong base yields the symmetric imidazolate anion ($[\text{C}_3\text{H}_3\text{N}_2]^-$), where the negative charge is delocalized equally across both nitrogen atoms.
3. **The Catalytic Triad**: In serine proteases (chymotrypsin, trypsin, elastase), the imidazole ring of **His57** forms a catalytic triad with **Asp102** and **Ser195**, acting as a general base to deprotonate Ser195, converting it into a potent alkoxide nucleophile.""",
                "simulations": ["sim_chem_fused_heterocycle_fischer_skraup"]
            },
            {
                "id": "sec9_2",
                "secNumber": "§9.2",
                "title": "Thiazole & the Breslow Carbene Intermediate in Umpolung Catalysis",
                "heading": "Thiazole & the Breslow Carbene Intermediate in Umpolung Catalysis",
                "content": r"""Thiazole contains sulfur at C1 and nitrogen at C3. It forms the essential core of **vitamin $\text{B}_1$ (thiamine pyrophosphate, TPP)**, the vital cofactor for enzymatic decarboxylation of pyruvate in cellular respiration.

### The Breslow Intermediate & N-Heterocyclic Carbenes (NHCs)
In 1958, Ronald Breslow discovered that the proton at the **C2 position** of thiazolium salts is extraordinarily acidic ($\text{p}K_a \approx 17\text{–}19$), roughly $10^{14}$ times more acidic than an ordinary aromatic proton:

```
            Thiazolium C2 Deprotonation to Breslow NHC Carbene:
               R1                                    R1
                |                                     |
                N3(+)                                 N3
              /   \          - H(+)                 /   \
             C4    C2 - H   ========>              C4    C2:  <---> [ Singlet Carbene ]
             ||    |                               ||    |
             C5 -- S                               C5 -- S
```

Deprotonation by mild base generates a stable **singlet $N$-heterocyclic carbene (NHC)**:
1. The unshared electron pair occupies a localized $sp^2$ hybrid orbital on C2 in the ring plane.
2. The vacant $p$-orbital is perpendicular to the ring and is stabilized by resonance donation from the adjacent sulfur $3p$ orbital and nitrogen $2p$ orbital.

The thiazolium carbene attacks the carbonyl of pyruvate or aldehydes, inverting the normal electrophilic polarity of the carbonyl carbon (**umpolung**), enabling the **benzoin condensation** and oxidative decarboxylation of $\alpha$-keto acids.""",
                "simulations": []
            },
            {
                "id": "sec9_3",
                "secNumber": "§9.3",
                "title": "Pyrimidines & Purines: Tautomerism & Nucleic Acid Architecture",
                "heading": "Pyrimidines & Purines: Tautomerism & Nucleic Acid Architecture",
                "content": r"""Pyrimidines (1,3-diazines) and purines (imidazo[4,5-d]pyrimidines) constitute the universal molecular alphabet of genetic information in DNA and RNA.

```
       Pyrimidines: Uracil, Thymine, Cytosine
       Purines:     Adenine, Guanine
```

### Lactam-Lactim Tautomerism & Watson-Crick Geometry
Each of the oxygen-bearing nucleobases (uracil, thymine, cytosine, guanine) can theoretically exist in two tautomeric states:
1. **Lactim Form (Hydroxy/Enol)**: $-\text{N}=\text{C}(\text{OH})-$
2. **Lactam Form (Keto/Amide)**: $-\text{NH}-\text{C}(=\text{O})-$

In 1953, James Watson and Francis Crick were able to solve the double-helical structure of DNA only after Jerry Donohue pointed out that quantum chemical calculations and spectroscopic measurements demonstrate that the nucleobases exist overwhelmingly ($>99.99\%$) in the **keto (lactam) form** under physiological conditions:

```
Watson-Crick Hydrogen-Bonding Geometries:
1. Adenine - Thymine Base Pair (2 Hydrogen Bonds):
   A(N1) ::::::::: H-N3(T)     (Distance: 2.82 Å)
   A(N6-H) ::::::: O4(T)       (Distance: 2.84 Å)

2. Guanine - Cytosine Base Pair (3 Hydrogen Bonds):
   G(O6) ::::::::: H-N4(C)     (Distance: 2.91 Å)
   G(N1-H) ::::::: N3(C)       (Distance: 2.95 Å)
   G(N2-H) ::::::: O2(C)       (Distance: 2.86 Å)
```

The lactam tautomers present the precise geometric array of hydrogen-bond donors and acceptors required to form the rigid, planar Watson-Crick base pairs that stabilize the double helix.""",
                "simulations": []
            },
            {
                "id": "sec9_4",
                "secNumber": "§9.4",
                "title": "Indole Chemistry: The Fischer Indole Sigmatropic Cascade & C3 Regiocontrol",
                "heading": "Indole Chemistry: The Fischer Indole Sigmatropic Cascade & C3 Regiocontrol",
                "content": r"""Indole (1H-benzo[b]pyrrole) is a $10\pi$-electron heteroaromatic bicycle comprising a benzene ring fused to a pyrrole ring. It is the core pharmacophore of tryptophan, serotonin (5-HT), melatonin, and indole alkaloids (vincristine, strychnine).

### The Fischer Indole Synthesis
Discovered by Emil Fischer in 1883, the Fischer indole synthesis couples an arylhydrazine with an aldehyde or ketone in the presence of an acid catalyst ($\text{ZnCl}_2, \text{PPA}, \text{AcOH}$):

$$\text{PhNH-NH}_2 + \text{RCH}_2\text{COR}' \xrightarrow{\text{acid, }\Delta} \text{Indole derivative} + \text{NH}_4^+ \tag{9.1}$$

```
       The Fischer Indole Sigmatropic Cascade:
       Arylhydrazine + Ketone ===> Arylhydrazone
              |
              | Acid-catalyzed tautomerization
              v
       Ene-hydrazine Intermediate
              |
              | [3,3]-Sigmatropic Rearrangement (Breaks weak N-N bond)
              v
       Dienimine Intermediate
              |
              | Re-aromatization & Intramolecular Cyclization
              v
       Aminal Intermediate
              |
              | Acid-catalyzed elimination of ammonia (- NH3)
              v
       Substituted Indole Derivative
```

#### Detailed Mechanistic Stages:
1. Hydrazone formation: Condensation yields an arylhydrazone ($\text{PhNH}-\text{N}=\text{C}(\text{R}')\text{CH}_2\text{R}$).
2. Tautomerization: Acid promotes tautomerization into the **ene-hydrazine** ($\text{PhNH}-\text{NH}-\text{C}(\text{R}')=\text{CHR}$).
3. **[3,3]-Sigmatropic Rearrangement**: The core step is a concerted pericyclic rearrangement that breaks the weak $\text{N}-\text{N}$ single bond ($\text{BDE} \approx 160\text{ kJ}\cdot\text{mol}^{-1}$) and forms a strong $\text{C}-\text{C}$ single bond ($\text{BDE} \approx 350\text{ kJ}\cdot\text{mol}^{-1}$), yielding a non-aromatic dienimine.
4. Rearomatization: Protomeric shifts restore the aromaticity of the benzene ring.
5. Cyclization & Deamination: Intramolecular nucleophilic attack of the aromatic amino group onto the imine carbon forms a cyclic aminal, which expels ammonia ($\text{NH}_3\uparrow$) under acid catalysis to furnish the **indole**.

### Electrophilic Substitution at C3 Regiocontrol
Unlike pyrrole (which undergoes electrophilic substitution preferentially at C2), indole undergoes electrophilic aromatic substitution **exclusively at the C3 position**:
- **Attack at C3**: Produces a Wheland carbocation where the positive charge is delocalized onto the adjacent nitrogen atom, while the **benzene ring retains its fully intact benzenoid Clar sextet**:
  $$[\text{C3-Intermediate}]: \quad [\text{Ring A intact benzene}] - [\text{C2}=\text{N}^+\text{H}-] \tag{9.2}$$
- **Attack at C2**: Would require delocalizing the positive charge across the bridgehead into the benzene ring, disrupting its $152\text{ kJ}\cdot\text{mol}^{-1}$ resonance stabilization.
Therefore, nitration, bromination, formylation (Vilsmeier-Haack), and Mannich reactions of indole take place exclusively at **C3**.""",
                "simulations": []
            },
            {
                "id": "sec9_5",
                "secNumber": "§9.5",
                "title": "Quinoline Syntheses: Skraup, Doebner-Miller & Friedländer Reactions",
                "heading": "Quinoline Syntheses: Skraup, Doebner-Miller & Friedländer Reactions",
                "content": r"""Quinoline (benzo[b]pyridine) is a $10\pi$-electron heteroaromatic system consisting of a benzene ring fused to a pyridine ring.

### 1. The Skraup Synthesis
Heating aniline with glycerol, concentrated sulfuric acid, and a mild oxidizing agent (nitrobenzene or $\text{FeSO}_4$) yields quinoline:

$$\text{PhNH}_2 + \text{HOCH}_2\text{CH(OH)CH}_2\text{OH} \xrightarrow{\text{conc. }\text{H}_2\text{SO}_4, \text{PhNO}_2, 140^\circ\text{C}} \text{Quinoline} + 4\,\text{H}_2\text{O} \tag{9.3}$$

```
                The Skraup Reaction Sequence:
1. Glycerol + H2SO4, heat (- 2 H2O) ===> Acrolein (CH2=CH-CHO)
2. Aniline + Acrolein (Michael 1,4-addition) ===> beta-(Phenylamino)propanal
3. Acid-catalyzed intramolecular EAS cyclization ===> 1,2-Dihydroquinoline
4. Oxidation with Nitrobenzene (PhNO2) ===> Quinoline + Aniline
```

- Ferrous sulfate ($\text{FeSO}_4$) is added as a moderator to prevent the violently exothermic reaction from erupting.

### 2. The Doebner-Miller Synthesis
Similar to the Skraup synthesis, but utilizes $\alpha,\beta$-unsaturated aldehydes generated *in situ* from the aldol condensation of two molecules of aldehyde (e.g., acetaldehyde yielding crotonaldehyde, producing 2-methylquinoline / quinaldine).

### 3. The Friedländer Synthesis
Condensation of 2-aminobenzaldehyde with an enolizable aldehyde or ketone in the presence of base or acid provides a mild, regiospecific route to substituted quinolines without harsh oxidizing conditions:

$$o\text{-H}_2\text{N-C}_6\text{H}_4\text{-CHO} + \text{CH}_3\text{COCH}_3 \xrightarrow{\text{aq. NaOH, }60^\circ\text{C}} \text{2-methylquinoline} + 2\,\text{H}_2\text{O} \tag{9.4}$$""",
                "simulations": []
            },
            {
                "id": "sec9_6",
                "secNumber": "§9.6",
                "title": "Quinoline & Isoquinoline Reactivity: C5/C8 vs C2/C4 Manifolds",
                "heading": "Quinoline & Isoquinoline Reactivity: C5/C8 vs C2/C4 Manifolds",
                "content": r"""The chemical reactivity of quinoline and isoquinoline reflects the electronic disparity between the carbocyclic benzene ring and the electron-deficient $\pi$-deficient pyridine ring.

### 1. Electrophilic Aromatic Substitution: C5 and C8 Regioselectivity
Electrophiles attack the **benzene ring** rather than the pyridine ring:
- In acidic media ($\text{HNO}_3/\text{H}_2\text{SO}_4$), the nitrogen is fully protonated into a quinolinium cation ($[\text{C}_9\text{H}_8\text{N}]^+$).
- The positive charge severely deactivates the pyridine ring.
- Nitration at $0^\circ\text{C}$ occurs on the carbocyclic ring, delivering an equimolar mixture of **5-nitroquinoline ($52\%$)** and **8-nitroquinoline ($48\%$)**. Attack at C6 or C7 is negligible.

### 2. Nucleophilic Aromatic Substitution: C2 and C4 Regioselectivity
The pyridine ring is $\pi$-deficient, rendering carbons C2 and C4 electrophilic:
- **Chichibabin Reaction**: Treatment of quinoline with sodium amide ($\text{NaNH}_2$) in liquid ammonia at $100^\circ\text{C}$ yields **2-aminoquinoline**. Attack occurs at C2 because the resulting Meisenheimer-type anionic intermediate delocalizes the negative charge directly onto the electronegative nitrogen atom:
  $$\text{Quinoline} + \text{NaNH}_2 \longrightarrow \text{2-aminoquinoline} + \text{NaH} \tag{9.5}$$
- Organolithium reagents ($\text{RLi}$) add selectively to C2, giving 2-alkylquinolines after oxidation.""",
                "simulations": []
            },
            {
                "id": "sec9_7",
                "secNumber": "§9.7",
                "title": "Isoquinoline Syntheses: Bischler-Napieralski & Pictet-Spengler Reactions",
                "heading": "Isoquinoline Syntheses: Bischler-Napieralski & Pictet-Spengler Reactions",
                "content": r"""Isoquinoline (benzo[c]pyridine) contains nitrogen at the C2 position. It is the core framework of morphine, papaverine, and benzylisoquinoline alkaloids.

### 1. The Bischler-Napieralski Synthesis
Condensation of a $\beta$-phenylethylamine with an acyl chloride or carboxylic acid gives an $N$-phenethylamide, which undergoes cyclodehydration when heated with phosphorus oxychloride ($\text{POCl}_3$) or phosphorus pentoxide ($\text{P}_2\text{O}_5$):

$$\text{PhCH}_2\text{CH}_2\text{NHCOR} \xrightarrow{\text{POCl}_3, \text{toluene, reflux}} \text{3,4-dihydroisoquinoline} \xrightarrow{\text{Pd/C, }\Delta} \text{Isoquinoline} \tag{9.6}$$

```
       Bischler-Napieralski Isoquinoline Synthesis:
       beta-Phenylethylamine + RCOCl ===> N-Phenethylamide
              |
              | POCl3, heat (- H2O) [Forms chloroiminium intermediate]
              v
       3,4-Dihydroisoquinoline Derivative
              |
              | Catalytic dehydrogenation (Pd/C, 250 C, - H2)
              v
       Fully Aromatic Isoquinoline Derivative
```

### 2. The Pictet-Spengler Reaction
Condensation of a $\beta$-arylethylamine (such as tryptamine or dopamine) with an aldehyde in the presence of mild acid ($\text{TFA}, \text{pH } 4\text{–}6$) at room temperature:

$$\text{Ar-CH}_2\text{CH}_2\text{NH}_2 + \text{RCHO} \xrightarrow{\text{cat. H}^+, 25^\circ\text{C}} \text{1,2,3,4-tetrahydroisoquinoline} \tag{9.7}$$

- Imine formation yields an electrophilic iminium ion.
- Intramolecular Mannich-type electrophilic aromatic attack of the electron-rich aromatic ring onto the iminium carbon closes the six-membered ring under physiological conditions.
- The Pictet-Spengler reaction is the universal biosynthetic reaction by which plants synthesize thousands of complex isoquinoline and indole alkaloids.""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob9_1",
                "problemNumber": "9.1",
                "title": "Thermodynamic and Kinetic Regiocontrol in Indole Electrophilic Substitution",
                "difficulty": "Mastery",
                "statement": r"""Indole undergoes electrophilic substitution exclusively at the C3 position under kinetic control, but at C2 when C3 is substituted.
(a) Draw the complete sets of Wheland intermediate resonance contributors for electrophilic attack at C3 versus C2.
(b) Explain why attack at C3 preserves the aromatic Clar sextet of the benzene ring while attack at C2 disrupts it.
(c) When 3-methylindole is brominated, what intermediate forms and why does the bromine atom migrate to C2 in the final product?""",
                "hints": ["Examine the aromaticity of the six-membered ring in both Wheland intermediates.", "3-Substituted indoles form a 3-bromoindolenine intermediate."],
                "solution": r"""### (a) Resonance Contributors for C3 vs C2 Attack
1. **Attack at C3**:
   The electrophile $E^+$ adds to C3, placing the positive charge on C2:
   $$\text{Structure 1}: \quad [\text{C3-}E, \text{C2-carbocation}] \longleftrightarrow \text{Structure 2}: \quad [\text{C3-}E, \text{C2}=\text{N}^+\text{H}-]$$
   In both major contributors, **the benzene ring retains its fully intact $6\pi$ aromatic sextet** ($152\text{ kJ}\cdot\text{mol}^{-1}$ stabilization).
2. **Attack at C2**:
   The electrophile $E^+$ adds to C2, placing the positive charge on C3:
   $$\text{Structure 1}: \quad [\text{C2-}E, \text{C3-carbocation}]$$
   To delocalize this positive charge, electrons must be drawn out of the benzene ring into the pyrrole ring:
   $$\text{Structures 2, 3, 4}: \quad \text{positive charge delocalized onto C4, C6, C8}$$
   Every resonance contributor that delocalizes the positive charge destroys the aromaticity of the benzene ring.

### (b) Energetic Consequences
Because the C3 Wheland intermediate preserves the benzenoid resonance energy:
$$\Delta G^\ddagger(\text{C3}) \ll \Delta G^\ddagger(\text{C2}) \implies k_{\text{C3}} \gg 10^4 \times k_{\text{C2}}$$
Electrophilic aromatic substitution of indole occurs with $>99.9\%$ regioselectivity at the **C3 position**.

### (c) Bromination of 3-Methylindole: Indolenine Rearrangement
When 3-methylindole reacts with $\text{Br}_2$:
1. The electrophile still attacks the more reactive **C3 position**, forming a non-aromatic **3-bromoindolenine intermediate**:
   $$[\text{C3(Me)(Br)}-\text{C2}=\text{N}-\text{Ar}]$$
2. Because C3 already carries a methyl group, it possesses no proton to eliminate to restore aromaticity.
3. The 3-bromoindolenine undergoes a spontaneous acid-catalyzed **[1,2]-bromine shift** from C3 to C2:
   $$\text{3-bromoindolenine} \longrightarrow [\text{C3(Me)}=\text{C2(Br)}-\text{N}^+\text{H}-\text{Ar}]$$
4. Deprotonation restores aromaticity, delivering **2-bromo-3-methylindole** as the final isolated product."""
            },
            {
                "id": "prob9_2",
                "problemNumber": "9.2",
                "title": "Complete Sigmatropic Cascade Mechanism of the Fischer Indole Synthesis",
                "difficulty": "Mastery",
                "statement": r"""Write the complete mechanism of the Fischer indole synthesis of 2-phenylindole from phenylhydrazine and acetophenone in the presence of polyphosphoric acid (PPA).
(a) Identify the hybridization and stereochemistry of the [3,3]-sigmatropic rearrangement step.
(b) Thermodynamically account for why breaking a nitrogen-nitrogen single bond and forming a carbon-carbon single bond provides the fundamental driving force for the rearrangement.
(c) Trace the fate of the two nitrogen atoms: which nitrogen is incorporated into the indole ring and which is expelled as ammonia?""",
                "hints": ["Compare the bond dissociation enthalpies of N-N vs C-C.", "Label the nitrogens N(alpha) and N(beta) to track their fate."],
                "solution": r"""### (a) Step-by-Step Mechanism
$$\begin{aligned}
\text{Step 1 (Hydrazone Formation)}: &\quad \text{PhNH-NH}_2 + \text{PhCOCH}_3 \xrightarrow{-\text{H}_2\text{O}} \text{PhNH-N}=\text{C(Ph)CH}_3 \\
\text{Step 2 (Enamine Tautomerization)}: &\quad \text{PhNH-N}=\text{C(Ph)CH}_3 \xrightleftharpoons{\text{H}^+} \text{PhNH-NH-C(Ph)}=\text{CH}_2 \quad (\text{ene-hydrazine}) \\
\text{Step 3 ([3,3]-Sigmatropic Shift)}: &\quad \text{Concerted pericyclic rearrangement of the ene-hydrazine protonated form} \\
\text{Step 4 (Rearomatization)}: &\quad \text{Dienimine} \longrightarrow \text{Aromatic diamine intermediate} \\
\text{Step 5 (Cyclization & Elimination)}: &\quad \text{Intramolecular attack yields aminal; loss of }\text{NH}_4^+ \text{ yields }\mathbf{\text{2-phenylindole}}
\end{aligned}$$

### (b) Thermodynamic Driving Force: Bond Enthalpy Disparity
The pivotal [3,3]-sigmatropic rearrangement breaks the central $\text{N}-\text{N}$ single bond and creates a new $\text{C}-\text{C}$ single bond:
- Bond dissociation enthalpy of $\text{N}-\text{N}$ single bond: $\text{BDE}(\text{N}-\text{N}) \approx 160\text{ kJ}\cdot\text{mol}^{-1}$
- Bond dissociation enthalpy of $\text{C}-\text{C}$ single bond: $\text{BDE}(\text{C}-\text{C}) \approx 348\text{ kJ}\cdot\text{mol}^{-1}$
The net enthalpic balance for this single elementary step is overwhelmingly exothermic:
$$\Delta H^\circ = \text{BDE}(\text{N}-\text{N}) - \text{BDE}(\text{C}-\text{C}) = +160 - 348 = \mathbf{-188\text{ kJ}\cdot\text{mol}^{-1}}$$
This massive enthalpic driving force of nearly $190\text{ kJ}\cdot\text{mol}^{-1}$ pulls the entire cascade irreversibly forward.

### (c) Isotopic Nitrogen Tracking
Let $\text{N}_\alpha$ be the nitrogen directly bonded to the phenyl ring ($\text{Ph}-\text{N}_\alpha\text{H}-$) and $\text{N}_\beta$ be the terminal hydrazine nitrogen ($-\text{N}_\beta\text{H}_2$):
- In Step 1, the hydrazone is $\text{Ph}-\text{N}_\alpha\text{H}-\text{N}_\beta=\text{C}(\text{Ph})\text{CH}_3$.
- In Step 3, the [3,3]-shift cleaves the $\text{N}_\alpha-\text{N}_\beta$ bond, attaching $\text{N}_\beta$ to the side chain ($-\text{N}_\beta\text{H}=\text{C}(\text{Ph})\text{CH}_2-$).
- In Step 5, the aromatic $\text{N}_\alpha\text{H}_2$ group attacks the imine carbon, and **$\text{N}_\beta$ is expelled as ammonia ($\text{NH}_4^+$)**.
Therefore:
- **$\text{N}_\alpha$ (aniline nitrogen) is retained in the indole ring**.
- **$\text{N}_\beta$ (terminal hydrazine nitrogen) is lost as ammonia**."""
            },
            {
                "id": "prob9_3",
                "problemNumber": "9.3",
                "title": "Skraup Synthesis Mechanism & Regiochemistry of 6-Methylquinoline",
                "difficulty": "Intermediate",
                "statement": r"""A student synthesizes 6-methylquinoline from $p$-toluidine (4-methylaniline) using the Skraup protocol with glycerol, sulfuric acid, and nitrobenzene.
(a) Write the balanced chemical reaction.
(b) Explain why 4-methylaniline gives a single quinoline regioisomer, whereas 3-methylaniline yields a mixture of two isomeric methylquinolines.
(c) State the role of nitrobenzene and identify the hazardous by-product that requires safety moderation with ferrous sulfate.""",
                "hints": ["Look at the symmetry of 4-methylaniline vs 3-methylaniline.", "The reaction is violently exothermic without FeSO4."],
                "solution": r"""### (a) Balanced Chemical Reaction
$$p\text{-CH}_3\text{-C}_6\text{H}_4\text{NH}_2 + \text{C}_3\text{H}_8\text{O}_3 \xrightarrow{\text{conc. }\text{H}_2\text{SO}_4, \text{PhNO}_2, \Delta} \text{6-methylquinoline} + \text{PhNH}_2 + 4\,\text{H}_2\text{O}$$

### (b) Regiochemical Analysis: $p$-Toluidine vs $m$-Toluidine
1. **$p$-Toluidine (4-Methylaniline)**:
   The molecule possesses a vertical plane of symmetry passing through C1 and C4. The two positions *ortho* to the amino group (C2 and C6) are strictly chemically and symmetrically **equivalent**. Electrophilic cyclization at either position yields the identical product: **6-methylquinoline**.
2. **$m$-Toluidine (3-Methylaniline)**:
   The two positions *ortho* to the amino group are constitutionally **non-equivalent**:
   - Cyclization at C6 (less sterically hindered) yields **7-methylquinoline** (major product, $\sim 70\%$).
   - Cyclization at C2 (sandwiched between $-\text{NH}_2$ and $-\text{CH}_3$) yields **5-methylquinoline** (minor product, $\sim 30\%$).

### (c) Role of Nitrobenzene and $\text{FeSO}_4$ Moderation
- **Nitrobenzene ($\text{PhNO}_2$)**: Acts as a stoichiometric **oxidizing agent**. The cyclization step forms 1,2-dihydro-6-methylquinoline. Nitrobenzene oxidizes this dihydro intermediate to the fully aromatic quinoline ring, being reduced in the process to aniline.
- **$\text{FeSO}_4$ Moderator**: Dehydration of glycerol by concentrated sulfuric acid produces **acrolein** ($\text{CH}_2=\text{CHCHO}$), a volatile, toxic lachrymator. The subsequent Michael addition and cyclization are violently exothermic ($\Delta H^\circ \ll -300\text{ kJ}\cdot\text{mol}^{-1}$), capable of causing thermal runaways and explosions. Ferrous sulfate ($\text{FeSO}_4$) moderates the oxidation rate, ensuring a smooth, safe reaction."""
            },
            {
                "id": "prob9_4",
                "problemNumber": "9.4",
                "title": "Bischler-Napieralski vs Pictet-Spengler Isoquinoline Syntheses",
                "difficulty": "Mastery",
                "statement": r"""Compare the syntheses of isoquinoline derivatives via the Bischler-Napieralski and Pictet-Spengler reactions.
(a) Provide the reagents and intermediates for synthesizing 1-methyl-3,4-dihydroisoquinoline from 2-phenylethylamine.
(b) Show how dopamine and acetaldehyde react under Pictet-Spengler conditions to yield salsolinol.
(c) Explain why the Pictet-Spengler reaction operates under mild physiological conditions ($\text{pH } 4\text{–}7, 25^\circ\text{C}$), whereas the Bischler-Napieralski reaction requires harsh dehydrating conditions ($\text{POCl}_3, 110^\circ\text{C}$).""",
                "hints": ["Pictet-Spengler uses an iminium ion which is more electrophilic.", "Bischler-Napieralski must activate an unreactive amide."],
                "solution": r"""### (a) Bischler-Napieralski Route to 1-Methyl-3,4-dihydroisoquinoline
$$\begin{aligned}
\text{Step 1}: &\quad \text{PhCH}_2\text{CH}_2\text{NH}_2 + \text{CH}_3\text{COCl} \xrightarrow{\text{pyridine}} \text{PhCH}_2\text{CH}_2\text{NHCOCH}_3 + \text{Py}\cdot\text{HCl} \\
\text{Step 2}: &\quad \text{PhCH}_2\text{CH}_2\text{NHCOCH}_3 + \text{POCl}_3 \xrightarrow{\text{toluene, reflux, }110^\circ\text{C}} \text{1-methyl-3,4-dihydroisoquinoline} + \text{HPO}_2\text{Cl}_2
\end{aligned}$$
Treatment of the amide with $\text{POCl}_3$ converts the amide oxygen into a dichlorophosphate leaving group, generating a chloroiminium/nitrilium intermediate that undergoes intramolecular electrophilic aromatic attack by the phenyl ring.

### (b) Pictet-Spengler Synthesis of Salsolinol
$$\text{Dopamine} + \text{CH}_3\text{CHO} \xrightarrow{\text{aq. buffer, pH } 6.0, 25^\circ\text{C}} \text{Salsolinol (6,7-dihydroxy-1-methyl-1,2,3,4-tetrahydroisoquinoline)}$$
1. Condensation of the primary amine of dopamine with acetaldehyde forms an imine ($\text{R}-\text{CH}=\text{N}-\text{CH}_2\text{CH}_2-\text{Ar}$).
2. Protonation forms an electrophilic **iminium ion** ($[\text{R}-\text{CH}=\text{N}^+\text{H}-\text{CH}_2\text{CH}_2-\text{Ar}]$).
3. Intramolecular electrophilic attack by the catechol ring (strongly activated by two ortho/para electron-donating $-\text{OH}$ groups) onto the iminium carbon closes the six-membered tetrahydroisoquinoline ring (**salsolinol**).

### (c) Rationale for Mild vs Harsh Reaction Conditions
1. **Electrophilicity of Intermediate**:
   - In the **Pictet-Spengler reaction**, an **iminium cation** ($[\text{C}=\text{N}^+\text{H}-]$) is generated directly. Iminium ions possess an extraordinarily low LUMO and a full positive charge, making them violently electrophilic. When coupled with an electron-rich aromatic ring (like catechol or indole), cyclization proceeds spontaneously at room temperature and neutral $\text{pH}$.
2. **Activation Penalty of Amides**:
   - In the **Bischler-Napieralski reaction**, the starting material is a neutral **carboxamide**. Amides possess $\sim 80\text{ kJ}\cdot\text{mol}^{-1}$ of resonance stabilization. The amide carbonyl is weakly electrophilic and cannot undergo attack by an unactivated phenyl ring without harsh electrophilic activation ($\text{POCl}_3, \text{P}_2\text{O}_5$) at elevated temperatures ($>100^\circ\text{C}$) to force conversion into a reactive nitrilium ion."""
            },
            {
                "id": "prob9_5",
                "problemNumber": "9.5",
                "title": "Chichibabin Amination Mechanism of Quinoline",
                "difficulty": "Intermediate",
                "statement": r"""When quinoline is heated with sodium amide ($\text{NaNH}_2$) in liquid ammonia at $100^\circ\text{C}$ in a sealed autoclave, 2-aminoquinoline is isolated as the exclusive product.
(a) Write the complete step-by-step mechanism showing the Meisenheimer-type anionic intermediate.
(b) Why does nucleophilic addition occur at C2 rather than C4 or the benzene ring?
(c) Identify the gas that is evolved upon aqueous workup.""",
                "hints": ["Pyridine ring is pi-deficient; nitrogen can host negative charge.", "Hydride ion is eliminated as hydrogen gas."],
                "solution": r"""### (a) Step-by-Step Chichibabin Mechanism
$$\begin{aligned}
\text{Step 1 (Nucleophilic Addition)}: &\quad \text{Quinoline} + \text{NH}_2^- \longrightarrow [\text{2-amino-1,2-dihydroquinolin-1-ide}]^- \quad (\text{Meisenheimer intermediate}) \\
\text{Step 2 (Hydride Elimination)}: &\quad [\text{2-amino-1,2-dihydroquinolin-1-ide}]^- \xrightarrow{\Delta} \text{Sodium 2-quinolinamide salt} + \text{H}_2\uparrow \\
\text{Step 3 (Aqueous Workup)}: &\quad \text{Sodium 2-quinolinamide} + \text{H}_2\text{O} \longrightarrow \mathbf{\text{2-aminoquinoline}} + \text{NaOH}
\end{aligned}$$

### (b) Regioselectivity for C2 Attack
1. **Benzene Ring Inertness**: The benzene ring is $\pi$-electron rich and aromatic ($152\text{ kJ}\cdot\text{mol}^{-1}$). Attack on the benzene ring would create an unstable carbocyclic carbanion with no electronegative heteroatom to stabilize the charge.
2. **C2 vs C4 Preference**:
   The pyridine ring is strongly $\pi$-deficient due to the electronegative nitrogen atom.
   - Attack of $\text{NH}_2^-$ at C2 places the negative charge **directly onto the electronegative nitrogen atom**:
     $$[\text{C2-adduct}]: \quad [-\text{N}^--\text{CH}(\text{NH}_2)-]$$
     This canonical contributor places the full formal negative charge on nitrogen ($Z=7, \chi_P = 3.04$), maximizing electrostatic and thermodynamic stability.
   - Attack at C4 can also delocalize onto nitrogen, but the transition state for C2 attack is lower in energy due to proximity to the polarized $\text{C}=\text{N}$ bond.

### (c) Evolved Gas
In Step 2, the leaving group is a **hydride ion ($\text{H}^-$)**, which reacts instantly with an acidic proton from the solvent ($\text{NH}_3$) or amide:
$$\text{H}^- + \text{NH}_3 \longrightarrow \text{H}_2\uparrow + \text{NH}_2^-$$
The evolved gas is **molecular hydrogen ($\text{H}_2\uparrow$)**."""
            },
            {
                "id": "prob9_6",
                "problemNumber": "9.6",
                "title": "Synthesis of Purines: The Traube Purine Synthesis",
                "difficulty": "Mastery",
                "statement": r"""The Traube purine synthesis (Wilhelm Traube, 1900) is the classical industrial pathway to caffeine, theophylline, and adenine.
(a) Detail the chemical steps for synthesizing adenine (6-aminopurine) from 4,5,6-triaminopyrimidine and formic acid.
(b) How is 4,5,6-triaminopyrimidine prepared from malononitrile and thiourea?
(c) Explain the tautomeric equilibrium between the 9H and 7H purine tautomers and state which tautomer is present in DNA nucleotides.""",
                "hints": ["Formic acid provides the single carbon C8 of the imidazole ring.", "Purines in DNA are attached to deoxyribose at N9."],
                "solution": r"""### (a) Traube Synthesis of Adenine
$$\begin{aligned}
\text{Step 1 (Formylation)}: &\quad \text{Pyrimidine-4,5,6-triamine} + \text{HCOOH} \xrightarrow{\Delta} 5\text{-formamido-pyrimidine-4,6-diamine} + \text{H}_2\text{O} \\
\text{Step 2 (Thermal Cyclization)}: &\quad 5\text{-formamido-pyrimidine-4,6-diamine} \xrightarrow{210^\circ\text{C}, -\text{H}_2\text{O}} \mathbf{\text{Adenine (6-aminopurine)}}
\end{aligned}$$
Formic acid ($-\text{COOH}$) provides the single $sp^2$ carbon (C8) of the fused imidazole ring. Dehydration closes the five-membered ring cleanly.

### (b) Synthesis of 4,5,6-Triaminopyrimidine
$$\begin{aligned}
\text{Step 1}: &\quad \text{CH}_2(\text{CN})_2 + \text{H}_2\text{N-CS-NH}_2 \xrightarrow{\text{NaOEt}} \text{4,6-diamino-2-mercaptopyrimidine} \\
\text{Step 2}: &\quad \text{Desulfurization with Raney Ni} \longrightarrow \text{4,6-diaminopyrimidine} \\
\text{Step 3}: &\quad \text{Nitrosation with HNO}_2 \longrightarrow \text{5-nitroso-pyrimidine-4,6-diamine} \\
\text{Step 4}: &\quad \text{Reduction with Na}_2\text{S}_2\text{O}_4 \text{ or H}_2/\text{Pd} \longrightarrow \mathbf{\text{Pyrimidine-4,5,6-triamine}}
\end{aligned}$$

### (c) Purine 9H vs 7H Tautomerism
Unsubstituted purine exists in rapid prototropic equilibrium between two tautomers:
- **9H-Purine**: The imidazole proton is on N9.
- **7H-Purine**: The imidazole proton is on N7.
In aqueous solution at room temperature, the **9H-tautomer** dominates ($93:7$ ratio) because it minimizes dipole repulsion with the pyrimidine ring nitrogens.
In all biological nucleic acids (DNA and RNA), the purine bases (adenine and guanine) are covalently attached via a $\beta$-glycosidic bond to the $\text{C1}'$ carbon of deoxyribose or ribose exclusively at the **N9 position**."""
            },
            {
                "id": "prob9_7",
                "problemNumber": "9.7",
                "title": "Breslow Umpolung Catalysis Mechanism of Vitamin B1 Thiamine Core",
                "difficulty": "Mastery",
                "statement": r"""Ronald Breslow elucidated the mechanism of thiamine pyrophosphate (TPP) catalysis by demonstrating that thiazolium salts catalyze the benzoin condensation without cyanide.
(a) Write the complete catalytic cycle for the thiazolium-catalyzed benzoin condensation of two molecules of benzaldehyde.
(b) Draw the resonance structures of the Breslow intermediate, highlighting the carbanion stabilization.
(c) Explain why thiazolium salts are active catalysts while oxazolium and imidazolium salts are dramatically less effective.""",
                "hints": ["Look at the polarizability and d-orbital/sigma* stabilization of sulfur.", "Breslow intermediate is an enamine-like species."],
                "solution": r"""### (a) Thiazolium Catalytic Cycle
$$\begin{aligned}
\text{Step 1 (Deprotonation)}: &\quad \text{Thiazolium salt} + \text{Base} \rightleftharpoons \text{Thiazol-2-ylidene carbene (NHC)} + \text{Base}\cdot\text{H}^+ \\
\text{Step 2 (Addition)}: &\quad \text{Carbene} + \text{PhCHO} \rightleftharpoons \text{Adduct alkoxide} \\
\text{Step 3 (Proton Transfer)}: &\quad \text{Alkoxide} \rightleftharpoons \mathbf{\text{Breslow Intermediate}} \quad (\alpha\text{-hydroxybenzylidene adduct}) \\
\text{Step 4 (Nucleophilic Attack)}: &\quad \text{Breslow intermediate} + \text{PhCHO} \longrightarrow \text{Adduct of 2nd aldehyde} \\
\text{Step 5 (Product Release)}: &\quad \text{Deprotonation and elimination of carbene catalyst} \longrightarrow \text{Benzoin} + \text{Thiazol-2-ylidene}
\end{aligned}$$

### (b) Structure & Resonance of the Breslow Intermediate
The Breslow intermediate is:
$$[\text{Thiazole-ring}]=\text{C}(\text{OH})\text{Ph} \longleftrightarrow [\text{Thiazolium-ring}]^+-\text{C}^-(\text{OH})\text{Ph}$$
1. The neutral form is an electron-rich **enamine-like species** where the thiazole nitrogen lone pair is delocalized into the exocyclic double bond.
2. The zwitterionic resonance contributor reveals that the carbonyl carbon of the original benzaldehyde has undergone **polarity inversion (umpolung)**: normally an electrophilic $\delta+$ center, it is now a potent nucleophilic **carbanion** capable of attacking a second aldehyde carbonyl.

### (c) Why Thiazolium Is Superior to Oxazolium and Imidazolium
1. **Oxazolium Salts**:
   Oxygen ($\chi_P = 3.44$) is much more electronegative than sulfur. The C2-O bond is susceptible to nucleophilic ring-opening cleavage by water or bases, destroying the catalyst.
2. **Imidazolium Salts**:
   The two nitrogens in imidazolium are strong resonance electron donors. The C2 proton is far less acidic ($\text{p}K_a \approx 23$ vs $17$ for thiazolium), requiring much stronger bases that can destroy aldehyde reactants.
3. **Thiazolium Perfection**:
   - Sulfur ($\chi_P = 2.58$) is large, polarizable, and stable to ring-opening.
   - Sulfur stabilizes the singlet carbene at C2 through hyperconjugative $\sigma^*_{\text{C-S}}$ overlap and polarizability without being overly electron-donating.
   - Thiazolium provides the optimal thermodynamic balance of high C2 acidity, stability, and carbanion nucleophilicity."""
            }
        ]
    }
