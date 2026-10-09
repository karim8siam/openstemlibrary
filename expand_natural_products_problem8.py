#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
expand_natural_products_problem8.py
Appends Problem 8 to all 10 units of Chemistry of Natural Products.
Strictly zero course numbers, codes, or marks.
Raw triple quotes used throughout to prevent any escape sequence issues.
"""

def add_problem8_to_units(units):
    prob8_dict = {
        "unit-1": {
            "id": "prob-1-8",
            "problemNumber": "1.8",
            "title": "Modular PKS Domain Stoichiometry and Chain Assembly of 6-Deoxyerythronolide B",
            "difficulty": "Advanced",
            "statement": r"""6-Deoxyerythronolide B (6-dEB), the macrolide precursor of erythromycin A, is biosynthesized by the multi-enzyme complex 6-deoxyerythronolide B synthase (DEBS). DEBS comprises three polypeptide subunits (DEBS1, DEBS2, DEBS3) containing a loading module and six successive extender modules.
(a) 6-dEB is constructed from one propionyl-CoA starter unit and six (2S)-methylmalonyl-CoA extender units. Write down the complete balanced stoichiometric equation for the formation of 6-dEB ($C_{21}H_{38}O_5$), including the consumption of NADPH and ATP-derived equivalents.
(b) Count the exact number of enzymatic domains (KS, AT, ACP, KR, DH, ER, TE) present across the entire DEBS assembly line, and explain why only one module contains a dehydratase (DH) domain while zero modules contain an enoylreductase (ER) domain.""",
            "hints": [
                r"Propionyl-CoA (3 carbons) + 6 x Methylmalonyl-CoA (6 x 3 carbons incorporated) = 21 carbons.",
                r"Analyze the oxidation state of each carbon in 6-dEB to identify how many KR and DH domains are active.",
                r"6-dEB is a saturated polyketide with hydroxyls and methyls, but no double bonds."
            ],
            "solution": r"""### Step 1: Balanced Stoichiometric Equation
The synthesis of 6-dEB ($C_{21}H_{38}O_5$) involves:
1. **Starter and Extenders**:
   - 1 Propionyl-CoA (starter, $C_3$)
   - 6 (2S)-Methylmalonyl-CoA (extenders, $6\times C_3 = C_{18}$ incorporated, with loss of $6\text{ CO}_2$)
2. **Reductive Cofactors**:
   Examination of 6-dEB reveals five hydroxyl groups and zero carbon-carbon double bonds:
   - Module 1: Contains KR (1 NADPH consumed).
   - Module 2: Contains KR (1 NADPH consumed).
   - Module 3: Lacks reductive domains (ketone retained, 0 NADPH).
   - Module 4: Contains KR, DH, and ER (reduces keto to methylene: 2 NADPH consumed, $1\text{ H}_2\text{O}$ lost).
   - Module 5: Contains KR (1 NADPH consumed).
   - Module 6: Contains KR (1 NADPH consumed).
   - Total NADPH consumed: $1 + 1 + 0 + 2 + 1 + 1 = 6\text{ NADPH}$.
3. **Balanced Equation**:
   $$\text{Propionyl-CoA} + 6\text{ (2S)-Methylmalonyl-CoA} + 6\text{ NADPH} + 6\text{ H}^+ \to \mathbf{6\text{-dEB } (C_{21}H_{38}O_5)} + 7\text{ CoASH} + 6\text{ CO}_2 + 6\text{ NADP}^+ + \text{H}_2\text{O}$$

### Step 2: Domain Inventory across the DEBS Complex
- **Loading Module**: $\text{AT}_L - \text{ACP}_L$ (2 domains).
- **Module 1**: $\text{KS}_1 - \text{AT}_1 - \text{KR}_1 - \text{ACP}_1$ (4 domains).
- **Module 2**: $\text{KS}_2 - \text{AT}_2 - \text{KR}_2 - \text{ACP}_2$ (4 domains).
- **Module 3**: $\text{KS}_3 - \text{AT}_3 - \text{ACP}_3$ (3 domains).
- **Module 4**: $\text{KS}_4 - \text{AT}_4 - \text{DH}_4 - \text{ER}_4 - \text{KR}_4 - \text{ACP}_4$ (6 domains).
- **Module 5**: $\text{KS}_5 - \text{AT}_5 - \text{KR}_5 - \text{ACP}_5$ (4 domains).
- **Module 6 + TE**: $\text{KS}_6 - \text{AT}_6 - \text{KR}_6 - \text{ACP}_6 - \text{TE}$ (5 domains).
Total domains in the complex = $2 + 4 + 4 + 3 + 6 + 4 + 5 = \mathbf{28\text{ enzymatic domains}}$.
Only Module 4 fully reduces the $\beta$-keto group to a saturated methylene ($-\text{CH}_2-$ at C7), which uniquely requires the sequential action of **KR, DH, and ER** domains within that specific module, demonstrating the colinearity rule of modular PKSs."""
        },
        "unit-2": {
            "id": "prob-2-8",
            "problemNumber": "2.8",
            "title": "Fragrance Chemistry: Acid-Catalyzed Cyclization Kinetics of Pseudoionone",
            "difficulty": "Intermediate",
            "statement": r"""In the industrial synthesis of ionones, pseudoionone undergoes cyclization in the presence of strong acid:
(a) Draw the carbocation intermediate formed upon protonation of the terminal double bond of pseudoionone and show the subsequent electrocyclic ring closure.
(b) Explain why concentrated sulfuric acid ($\text{H}_2\text{SO}_4$) at $50^\circ\text{C}$ gives an $80:20$ ratio in favor of $\beta$-ionone, whereas boron trifluoride etherate ($\text{BF}_3\cdot\text{OEt}_2$) or phosphoric acid ($\text{H}_3\text{PO}_4$) at $20^\circ\text{C}$ yields $>85\%$ $\alpha$-ionone.
(c) Calculate the difference in activation free energy $\Delta(\Delta G^\ddagger) = \Delta G^\ddagger_\beta - \Delta G^\ddagger_\alpha$ under kinetic control at $293\text{ K}$ given an $85:15$ ratio of $\alpha$- to $\beta$-ionone.""",
            "hints": [
                r"Protonation occurs at the terminal alkene to yield a tertiary carbocation.",
                r"Ring closure forms a cyclohexyl tertiary carbocation.",
                r"Use \Delta(\Delta G^\ddagger) = -RT \ln(k_\alpha / k_\beta) for kinetic product distribution."
            ],
            "solution": r"""### Step 1: Cyclization Mechanism
1. **Protonation**:
   Protonation of the terminal double bond ($C7=C8$) by $\text{H}^+$ creates a tertiary carbocation at C7:
   $$(\text{CH}_3)_2\text{C}^+-\text{CH}_2-\text{CH}_2-\text{C}(\text{CH}_3)=\text{CH}-\text{CH}=\text{CH}-\text{COCH}_3$$
2. **Ring Closure**:
   The electrons of the C3=C4 double bond attack the C7 carbocation, forming a six-membered cyclohexyl ring and generating a new tertiary carbocation at C3 (the **ionyl carbocation**).

### Step 2: Rationale for Acid-Dependent Regioselectivity
From the ionyl carbocation:
- **$\alpha$-Ionone Formation (Kinetic Control)**:
  Abstraction of the proton from the adjacent methyl/methine carbon (C2) is sterically less hindered:
  - Weaker acids like $\text{H}_3\text{PO}_4$ or Lewis acid complexes ($\text{BF}_3\cdot\text{OEt}_2$) have bulky counterions that preferentially abstract the more accessible proton, giving **$\alpha$-ionone**.
- **$\beta$-Ionone Formation (Thermodynamic Control)**:
  Abstraction of the proton from C4 generates a tetrasubstituted double bond that is fully conjugated with the side-chain polyenone system:
  - Strong acid ($\text{H}_2\text{SO}_4$) at elevated temperature allows reversible protonation, driving the mixture toward the lowest-energy thermodynamic sink: **$\beta$-ionone**.

### Step 3: Activation Energy Difference under Kinetic Control
Under kinetic control at $T = 293.15\text{ K}$:
$$\frac{[\alpha\text{-ionone}]}{[\beta\text{-ionone}]} = \frac{k_\alpha}{k_\beta} = \frac{85}{15} = 5.667$$
$$\Delta(\Delta G^\ddagger) = -R T \ln\left(\frac{k_\alpha}{k_\beta}\right) = -(8.314\text{ J/(mol}\cdot\text{K)})(293.15\text{ K}) \ln(5.667)$$
$$\Delta(\Delta G^\ddagger) = -2437.2 \times 1.7346 = -4228\text{ J/mol} = \mathbf{-4.23\text{ kJ/mol}}$$
The transition state leading to $\alpha$-ionone is favored by **$4.23\text{ kJ/mol}$** over that leading to $\beta$-ionone under kinetic conditions."""
        },
        "unit-3": {
            "id": "prob-3-8",
            "problemNumber": "3.8",
            "title": "Retrosynthetic Disconnection and Semisynthesis of Paclitaxel (Taxol)",
            "difficulty": "Advanced",
            "statement": r"""Paclitaxel (Taxol, $C_{47}H_{51}NO_{14}$) is a diterpene antitumor agent originally isolated from the bark of *Taxus brevifolia* in low yield ($0.01\%$). Because stripping the bark kills the slow-growing tree, Robert Holton developed a sustainable semisynthesis starting from **10-deacetylbaccatin III (10-DAB)**, extracted renewably from the needles of the European yew (*Taxus baccata*).
(a) Perform a retrosynthetic disconnection on the C13 ester linkage of Taxol, identifying the tetracyclic baccatin core and the chiral phenylisoserine side chain.
(b) Outline the Ojima-Holton $\beta$-lactam coupling method used to attach the protected side chain to C13-OH of baccatin III in high yield without epimerization.""",
            "hints": [
                r"Disconnect the ester at C13 into baccatin III and (2R,3S)-N-benzoyl-3-phenylisoserine.",
                r"Direct coupling of the carboxylic acid with the hindered C13-OH gives low yield and epimerization.",
                r"A chiral beta-lactam acts as an activated cyclic acyl donor."
            ],
            "solution": r"""### Step 1: Retrosynthetic Disconnection
1. **Target Disconnection**:
   Taxol consists of an intricate tetracyclic diterpene core linked via an ester bond at C13 to an $N$-benzoylphenylisoserine side chain:
   $$\text{Taxol} \xrightarrow{\text{C13 ester disconnection}} \text{Baccatin III} + (2R, 3S)\text{-}N\text{-benzoyl-3-phenylisoserine}$$
2. **Baccatin III ($C_{31}H_{38}O_{11}$)**:
   Contains the fused 6-8-6 ring system, the strained four-membered oxetane ring at C4-C5, bridgehead methyl groups, and free tertiary/secondary hydroxyl groups. It is prepared in two steps from renewable **10-DAB** by selective acetylation at C10.

### Step 2: The Ojima-Holton $\beta$-Lactam Coupling
Direct esterification of the sterically hindered C13 hydroxyl of baccatin III using carbodiimides (DCC/DMAP) yields $<15\%$ coupling and causes epimerization of the $\alpha$-chiral center of phenylisoserine.
Holton and Ojima solved this using a **chiral $\beta$-lactam (cis-3-triethylsilyloxy-4-phenylazetidin-2-one)**:
1. **Activation of Baccatin III**:
   The secondary C13-OH of 7-O-(triethylsilyl)baccatin III is deprotonated with a strong base (sodium hexamethyldisilazide, NaHMDS) at $-40^\circ\text{C}$ to form an alkoxide:
   $$\text{Bacc-C13-O}^- \text{Na}^+$$
2. **Nucleophilic Ring-Opening of the $\beta$-Lactam**:
   The C13 alkoxide nucleophilically attacks the carbonyl carbon of the chiral $\beta$-lactam:
   - The strained 4-membered $\beta$-lactam ring opens cleanly.
   - The ring opening forms the desired C13 ester bond in **$>95\%$ yield** with **$100\%$ stereoretention**.
3. **Deprotection and Benzoylation**:
   Removal of the triethylsilyl (TES) protecting groups with mild aqueous acid ($\text{HF/pyridine}$) followed by benzoylation of the free amino group delivers pure **paclitaxel (Taxol)**."""
        },
        "unit-4": {
            "id": "prob-4-8",
            "problemNumber": "4.8",
            "title": "Selective Bromine Water Oxidation Kinetics of Glucose Anomers",
            "difficulty": "Intermediate",
            "statement": r"""In the mild oxidation of D-glucopyranose with aqueous bromine water ($\text{Br}_2 / \text{H}_2\text{O}$), the reaction rate for pure $\beta$-D-glucopyranose is substantially faster than that for pure $\alpha$-D-glucopyranose:
$$k_\beta / k_\alpha \approx 250$$
(a) Provide the curved-arrow mechanism for the oxidation of $\beta$-D-glucopyranose to D-glucono-$\delta$-lactone by molecular bromine, identifying the role of water and the departing bromide ion.
(b) Explain why the reaction is over 200-fold faster for the $\beta$-anomer based on stereoelectronic alignment of the C1 hydrogen and the ring oxygen lone pair.""",
            "hints": [
                r"Bromine oxidizes the hemiacetal to a lactone (cyclic ester).",
                r"In beta-D-glucopyranose, C1-OH is equatorial and C1-H is axial.",
                r"In alpha-D-glucopyranose, C1-OH is axial and C1-H is equatorial."
            ],
            "solution": r"""### Step 1: Oxidation Mechanism to D-Glucono-$\delta$-lactone
1. **Hypobromite Formation**:
   The anomeric C1-OH oxygen attacks molecular bromine ($\text{Br}_2$), displacing bromide ion:
   $$\text{R-CH(OH)} + \text{Br}_2 \rightleftharpoons \text{R-CH(O-Br)} + \text{H}^+ + \text{Br}^-$$
   This forms an anomeric hypobromite intermediate.
2. **Base-Assisted Hydride Elimination**:
   Water acts as a general base, abstracting the C1 proton ($\text{C}1-\text{H}$):
   $$\text{H}_2\text{O} + \text{H}-\text{C}1(\text{OBr})- \to \text{H}_3\text{O}^+ + \text{C}1=\text{O} + \text{Br}^-$$
   The $\text{C}1-\text{H}$ bond electrons push in to form the carbonyl double bond ($\text{C}=\text{O}$), expelling bromide ion ($\text{Br}^-$).
   The product is **D-glucono-1,5-lactone ($\delta$-lactone)**, which subsequently hydrolyzes slowly in water to open-chain D-gluconic acid.

### Step 2: Stereoelectronic Rationale for $k_\beta / k_\alpha \approx 250$
- In **$\beta$-D-glucopyranose**:
  - The C1-OH is equatorial, which places the **$\text{C}1-\text{H}$ proton in a strictly axial orientation**.
  - In this chair conformation, the axial $\text{C}1-\text{H}$ bond is oriented **anti-periplanar** to an axial non-bonding lone pair on the endocyclic ring oxygen (O5).
  - This anti-periplanar geometry allows simultaneous push of electrons from the ring oxygen lone pair as the $\text{C}1-\text{H}$ bond breaks, stabilizing the transition state via stereoelectronic delocalization ($n_O \to \sigma^*_{\text{C-H}}$).
- In **$\alpha$-D-glucopyranose**:
  - The C1-OH is axial, forcing the **$\text{C}1-\text{H}$ proton into an equatorial orientation**.
  - The equatorial $\text{C}1-\text{H}$ bond cannot achieve anti-periplanar overlap with any oxygen lone pair.
  - Consequently, cleavage of the equatorial $\text{C}-\text{H}$ bond experiences a much higher activation energy barrier ($\Delta G^\ddagger_\alpha \gg \Delta G^\ddagger_\beta$), rendering the oxidation 250-fold slower."""
        },
        "unit-5": {
            "id": "prob-5-8",
            "problemNumber": "5.8",
            "title": "Antithrombin III Pentasaccharide Complex: Heparin Electrostatic Thermodynamics",
            "difficulty": "Advanced",
            "statement": r"""Unfractionated heparin exerts its clinical anticoagulant activity by binding to antithrombin III (ATIII) via a unique pentasaccharide sequence ($\text{DEFGH}$).
(a) Draw the schematic structure of the pentasaccharide sequence, identifying the essential 3-O-sulfate group on the central glucosamine unit.
(b) The dissociation constant for the heparin pentasaccharide-ATIII complex at $25^\circ\text{C}$ in $0.15\text{ M NaCl}$ is $K_d = 5.0\times 10^{-8}\text{ M}$. Calculate $\Delta G^\circ_{\text{bind}}$.
(c) When the salt concentration is increased from $0.15\text{ M}$ to $0.50\text{ M NaCl}$, $K_d$ weakens to $2.0\times 10^{-5}\text{ M}$. Using the Record-Lohman polyelectrolyte theory ($\log K_d = \log K_{d,0} - z \log[\text{Na}^+]$), calculate the number of ionic salt bridges ($z$) participating in the binding interface.""",
            "hints": [
                r"\Delta G^\circ = RT \ln K_d.",
                r"Slope of log(K_d) vs log[Na+] gives the number of counterions released, which corresponds to the number of ionic pairs z.",
                r"log10(5.0 x 10^-8) = -7.301; log10(2.0 x 10^-5) = -4.699."
            ],
            "solution": r"""### Step 1: Pentasaccharide Architecture
The unique ATIII-binding pentasaccharide comprises five residues:
$$\text{GlcNAc/NS(6S)} - \text{GlcA} - \text{GlcNS(3S,6S)} - \text{IdoA(2S)} - \text{GlcNS(6S)}$$
- The central residue (**GlcNS(3S,6S)**) carries a rare **3-O-sulfate group**. This specific sulfate group is absolutely essential: its removal reduces binding affinity to ATIII by over $1,000$-fold.

### Step 2: Gibbs Free Energy of Binding
At $T = 298.15\text{ K}$ ($25^\circ\text{C}$):
$$\Delta G^\circ_{\text{bind}} = R T \ln K_d = (8.314\text{ J/(mol}\cdot\text{K)})(298.15\text{ K}) \ln(5.0\times 10^{-8})$$
$$\Delta G^\circ_{\text{bind}} = 2478.9 \times (-16.811) = -41,673\text{ J/mol} = \mathbf{-41.67\text{ kJ/mol}}$$

### Step 3: Salt Dependence and Ionic Salt Bridges ($z$)
According to Record-Lohman polyelectrolyte theory, the dependence of the equilibrium dissociation constant on monovalent salt concentration reflects the release of counterions ($Na^+$) condensed on the polyanion:
$$\frac{\Delta \log_{10} K_d}{\Delta \log_{10}[\text{Na}^+]} = z$$
Given:
- At $[\text{Na}^+]_1 = 0.15\text{ M}$: $\log_{10}[\text{Na}^+]_1 = -0.8239$; $\log_{10} K_{d1} = -7.3010$
- At $[\text{Na}^+]_2 = 0.50\text{ M}$: $\log_{10}[\text{Na}^+]_2 = -0.3010$; $\log_{10} K_{d2} = -4.6990$
$$\Delta \log_{10} K_d = -4.6990 - (-7.3010) = +2.6020$$
$$\Delta \log_{10}[\text{Na}^+] = -0.3010 - (-0.8239) = +0.5229$$
The effective number of salt bridges is:
$$z = \frac{2.6020}{0.5229} = \mathbf{4.98} \approx \mathbf{5\text{ salt bridges}}$$
Exactly **5 ionic salt bridges** are formed between the sulfate/carboxylate groups of the pentasaccharide and conserved basic residues (Arg46, Arg47, Lys11, Lys114, Lys125) on antithrombin III."""
        },
        "unit-6": {
            "id": "prob-6-8",
            "problemNumber": "6.8",
            "title": "Anfinsen's Ribonuclease A: Disulfide Pairing Combinatorics and Folding Yield",
            "difficulty": "Advanced",
            "statement": r"""Bovine pancreatic ribonuclease A contains 124 amino acid residues including 8 cysteine residues that form 4 specific native disulfide crosslinks: Cys26-Cys84, Cys40-Cys95, Cys58-Cys110, and Cys65-Cys72.
(a) Calculate the total number of mathematically possible, distinct pairings of 8 cysteines into 4 disulfide bonds.
(b) If unfolded ribonuclease is re-oxidized under denaturing conditions (8 M urea), what is the theoretical probability of randomly forming the exact native set of 4 disulfide bonds?
(c) When catalytic trace amounts of $\beta$-mercaptoethanol are added in the absence of urea, the scrambled inactive protein converts quantitatively into active ribonuclease A. Explain the thermodynamic driving force.""",
            "hints": [
                r"Number of ways to pair 2n objects into n pairs is (2n-1)!! = 7 x 5 x 3 x 1.",
                r"Probability of the unique native pairing = 1 / total ways.",
                r"Trace thiol enables disulfide exchange (reshuffling) until the global free energy minimum is reached."
            ],
            "solution": r"""### Step 1: Combinatorial Pairing Calculation
For $2n = 8$ cysteine residues to form $n = 4$ disulfide bonds:
- The first cysteine can pair with any of the remaining $7$ cysteines ($7$ choices).
- The next available cysteine can pair with any of the remaining $5$ cysteines ($5$ choices).
- The next can pair with any of the remaining $3$ cysteines ($3$ choices).
- The last two must pair together ($1$ choice).
The total number of distinct pairings is:
$$N = (2n - 1)!! = 7 \times 5 \times 3 \times 1 = \mathbf{105\text{ possible disulfide isomers}}$$
Alternatively, using factorials:
$$N = \frac{8!}{2^4 \times 4!} = \frac{40,320}{16 \times 24} = \frac{40,320}{384} = \mathbf{105}$$

### Step 2: Random Probability in Urea
If oxidation occurs in $8\text{ M urea}$, the polypeptide chain has zero secondary/tertiary structure preference and behaves as a random coil. Each disulfide isomer forms with equal statistical probability:
$$P(\text{native}) = \frac{1}{105} \approx 0.00952 \implies \mathbf{0.95\%}$$
Less than $1\%$ of the scrambled protein possesses enzymatic activity.

### Step 3: Thiol-Catalyzed Reshuffling and Thermodynamic Minimum
In native buffer without denaturant:
- Addition of a catalytic trace of reducing thiol ($\text{R-SH}$, e.g., $\beta$-mercaptoethanol or protein disulfide isomerase, PDI) initiates reversible **thiol-disulfide exchange**:
  $$\text{Protein-S-S-Protein} + \text{R-S}^- \rightleftharpoons \text{Protein-S-S-R} + \text{Protein-S}^-$$
- This allows mismatched non-native disulfides to break and reform reversibly.
- As the polypeptide explores conformational space, non-covalent interactions (hydrophobic burial, salt bridges, hydrogen bonds) stabilize the native tertiary fold.
- Once the native pairing forms, it is locked inside the rigid tertiary structure where cysteines are shielded from further reduction.
Because the native fold represents the **global thermodynamic free energy minimum** ($\Delta G^\circ < 0$), the entire scrambled population is thermodynamically pulled into the $100\%$ active native state."""
        },
        "unit-7": {
            "id": "prob-7-8",
            "problemNumber": "7.8",
            "title": "Trityl Colorimetric Assay and Stepwise Coupling Yield in DNA Synthesizers",
            "difficulty": "Intermediate",
            "statement": r"""In automated solid-phase DNA synthesis, the cleavage of the 5'-dimethoxytrityl (DMT) group during each deprotection step releases the orange $\text{DMT}^+$ carbocation. The effluent from the synthesis column is diluted to $10.0\text{ mL}$ with $0.1\text{ M}$ toluenesulfonic acid in dichloromethane, and the absorbance is measured at $\lambda = 498\text{ nm}$ ($\epsilon = 70,000\text{ M}^{-1}\text{cm}^{-1}$, path length $l = 1.00\text{ cm}$).
(a) For a $1.00\text{ \mu mol}$ scale synthesis of a 20-mer oligonucleotide:
- After Step 1 deprotection: $A_{498} = 6.86$ (diluted 1:10).
- After Step 19 deprotection: $A_{498} = 6.22$ (diluted 1:10).
Calculate the initial micromoles of DMT released in Step 1 and Step 19.
(b) Compute the average stepwise coupling efficiency ($y_{\text{step}}$) across the 18 intervening coupling cycles and determine the overall yield of the 20-mer.""",
            "hints": [
                r"Beer-Lambert law: A = \epsilon * c * l.",
                r"Total moles = c * V * dilution_factor.",
                r"y_step = (moles_19 / moles_1)^(1 / 18)."
            ],
            "solution": r"""### Step 1: Micromoles of DMT Released
Using the Beer-Lambert law ($A = \epsilon \cdot c \cdot l$):
1. **At Step 1**:
   $$c_1 = \frac{A_1}{\epsilon \cdot l} = \frac{6.86}{70,000\text{ M}^{-1}\text{cm}^{-1} \times 1.00\text{ cm}} = 9.80\times 10^{-5}\text{ M}$$
   Accounting for the 1:10 dilution and $10.0\text{ mL}$ ($0.0100\text{ L}$) total volume:
   $$n_1 = c_1 \times 10 \times 0.0100\text{ L} = 9.80\times 10^{-5} \times 0.100 = 9.80\times 10^{-7}\text{ mol} = \mathbf{0.980\text{ \mu mol}}$$

2. **At Step 19**:
   $$c_{19} = \frac{A_{19}}{\epsilon \cdot l} = \frac{6.22}{70,000} = 8.886\times 10^{-5}\text{ M}$$
   $$n_{19} = 8.886\times 10^{-5} \times 0.100 = 8.886\times 10^{-7}\text{ mol} = \mathbf{0.8886\text{ \mu mol}}$$

### Step 2: Stepwise Coupling Efficiency Calculation
The decay in yield across 18 coupling steps obeys:
$$n_{19} = n_1 \times (y_{\text{step}})^{18}$$
$$\frac{n_{19}}{n_1} = \frac{0.8886}{0.980} = 0.9067$$
$$(y_{\text{step}})^{18} = 0.9067$$
Taking the 18th root:
$$y_{\text{step}} = (0.9067)^{1/18} = \mathbf{0.9946} \implies \mathbf{99.46\%}$$
The synthesizer operates with an outstanding average stepwise coupling efficiency of **$99.46\%$ per cycle**.
The overall yield of full-length 20-mer across all 19 couplings is:
$$Y_{\text{overall}} = (0.9946)^{19} = \mathbf{0.9018} \implies \mathbf{90.2\%}$$"""
        },
        "unit-8": {
            "id": "prob-8-8",
            "problemNumber": "8.8",
            "title": "Quinine Acid-Base Equilibria and Heme Biomineralization Inhibition",
            "difficulty": "Intermediate",
            "statement": r"""Quinine ($C_{20}H_{24}N_2O_2$) possesses two basic nitrogen atoms: the quinuclidine tertiary aliphatic nitrogen ($N1^\prime$, $pK_{a1} = 8.52$) and the quinoline aromatic nitrogen ($N1$, $pK_{a2} = 4.13$).
(a) The food vacuole of the malaria parasite *Plasmodium falciparum* maintains an internal $\text{pH } 5.20$, whereas host blood plasma is at $\text{pH } 7.40$. Using the Henderson-Hasselbalch equation, calculate the ratio of uncharged, membrane-permeable neutral quinine ($\text{Q}^0$) in blood plasma vs inside the parasite vacuole.
(b) Explain why quinine accumulates inside the acidic food vacuole by ion trapping, and compute the theoretical vacuolar accumulation concentration factor at equilibrium.""",
            "hints": [
                r"At pH 7.40, N1' is largely protonated but a fraction of neutral Q^0 exists.",
                r"Only neutral Q^0 can passively diffuse across lipid bilayer membranes.",
                r"Inside the vacuole (pH 5.20), virtually all quinine is protonated to QH+ and QH2(2+), preventing back-diffusion."
            ],
            "solution": r"""### Step 1: Protonation States in Plasma vs Vacuole
1. **In Blood Plasma ($\text{pH } 7.40$)**:
   - For quinuclidine nitrogen ($pK_{a1} = 8.52$):
     $$\text{pH} = pK_{a1} + \log\left(\frac{[\text{Q}^0]}{[\text{QH}^+]}\right) \implies 7.40 - 8.52 = -1.12$$
     $$\frac{[\text{Q}^0]}{[\text{QH}^+]} = 10^{-1.12} = 0.07586$$
   - For quinoline nitrogen ($pK_{a2} = 4.13$): At $\text{pH } 7.40$, it is virtually $100\%$ unprotonated.
   - The fraction of neutral, membrane-permeable quinine in plasma is:
     $$f_{\text{neutral, plasma}} \approx \frac{0.07586}{1 + 0.07586} = \mathbf{0.0705} \implies \mathbf{7.05\%}$$

2. **Inside Parasite Digestive Vacuole ($\text{pH } 5.20$)**:
   - For quinuclidine nitrogen ($pK_{a1} = 8.52$):
     $$\frac{[\text{Q}^0]}{[\text{QH}^+]} = 10^{5.20 - 8.52} = 10^{-3.32} = 4.786\times 10^{-4}$$
   - For quinoline nitrogen ($pK_{a2} = 4.13$):
     $$\frac{[\text{QH}^+]}{[\text{QH}_2^{2+}]} = 10^{5.20 - 4.13} = 10^{1.07} = 11.75$$
   - The fraction of uncharged neutral quinine inside the vacuole drops to:
     $$f_{\text{neutral, vac}} \approx 4.786\times 10^{-4} \times \frac{11.75}{12.75} = \mathbf{4.41\times 10^{-4}} \implies \mathbf{0.044\%}$$

### Step 2: Ion Trapping and Accumulation Factor
Only uncharged neutral quinine ($\text{Q}^0$) can cross the parasite membrane by passive non-ionic diffusion. At steady-state equilibrium:
$$[\text{Q}^0]_{\text{plasma}} = [\text{Q}^0]_{\text{vac}}$$
The total concentration of quinine in a compartment is $[\text{Q}]_{\text{total}} = [\text{Q}^0] / f_{\text{neutral}}$.
The concentration accumulation ratio is:
$$\frac{[\text{Q}]_{\text{total, vac}}}{[\text{Q}]_{\text{total, plasma}}} = \frac{f_{\text{neutral, plasma}}}{f_{\text{neutral, vac}}} = \frac{0.0705}{4.41\times 10^{-4}} \approx \mathbf{160\text{-fold}}$$
Driven purely by the trans-vacuolar pH gradient, quinine concentrates over **160-fold** inside the parasite digestive vacuole. This localized millimolar accumulation caps hemozoin crystal growth, killing the parasite with toxic free heme."""
        },
        "unit-9": {
            "id": "prob-9-8",
            "problemNumber": "9.8",
            "title": "Cytochrome P450scc Mechanism of Cholesterol Side-Chain Cleavage",
            "difficulty": "Advanced",
            "statement": r"""The initial and rate-determining step in the biosynthesis of all steroid hormones is catalyzed by mitochondrial Cytochrome P450 side-chain cleavage enzyme (CYP11A1 / P450scc):
$$\text{Cholesterol} + 3\text{ NADPH} + 3\text{ H}^+ + 3\text{ O}_2 \xrightarrow{\text{P450scc}} \text{Pregnenolone} + \text{Isocaproaldehyde} + 3\text{ NADP}^+ + 4\text{ H}_2\text{O}$$
(a) Identify the two consecutive hydroxylated intermediates formed in the enzyme active site prior to carbon-carbon bond cleavage.
(b) Outline the mechanism of the final oxidative cleavage of the C20-C22 bond, showing how the third equivalent of oxygen and NADPH generates the ketone group of pregnenolone and the aldehyde group of isocaproaldehyde without releasing toxic reactive oxygen species.""",
            "hints": [
                r"First hydroxylation is at C22 (22R-hydroxycholesterol).",
                r"Second hydroxylation is at C20 (20alpha,22R-dihydroxycholesterol).",
                r"Third step is oxidative glycol cleavage via an iron-peroxo species."
            ],
            "solution": r"""### Step 1: Sequential Hydroxylation Intermediates
CYP11A1 operates in the inner mitochondrial membrane, receiving electrons from NADPH via adrenodoxin reductase and the iron-sulfur protein adrenodoxin:
1. **First Monooxygenation**:
   Hydroxylation at C22 consumes 1 NADPH and $1\text{ O}_2$, generating **(22R)-22-hydroxycholesterol**.
2. **Second Monooxygenation**:
   Hydroxylation at C20 consumes a second NADPH and $1\text{ O}_2$, generating **(20R, 22R)-20,22-dihydroxycholesterol** (a vicinal 1,2-diol).
Both hydroxylated intermediates remain tightly bound inside the hydrophobic active-site pocket of CYP11A1 without dissociating into the matrix.

### Step 2: C20-C22 Oxidative Bond Cleavage Mechanism
The third step consumes the third equivalent of $\text{O}_2$ and NADPH:
1. Reduction of the ferric heme iron ($\text{Fe}^{\text{III}}$) by the incoming electron creates a ferrous-dioxygen complex that protonates to an **iron-peroxo intermediate ($\text{Fe}^{\text{III}}-\text{O}-\text{O}^-$)**.
2. The nucleophilic terminal peroxo oxygen attacks the C22 carbon or abstracts a proton from the vicinal diol, coordinating to the C20-C22 glycol.
3. Intramolecular electron transfer cleaves the central $\text{C}20-\text{C}22$ single bond:
   - The C20 carbon retains the steroid nucleus and is oxidized to the ketone of **pregnenolone ($C_{21}H_{32}O_2$)**.
   - The C22 carbon of the departing 6-carbon aliphatic side chain is oxidized to the aldehyde of **isocaproaldehyde (4-methylpentanal, $C_6H_{12}O$)**.
   - The heme iron returns to its resting resting $\text{Fe}^{\text{III}}$ state with release of water.
This enzyme-bound three-step cascade ensures 100% conversion to pregnenolone with zero escape of hazardous radical or peroxide byproducts."""
        },
        "unit-10": {
            "id": "prob-10-8",
            "problemNumber": "10.8",
            "title": "Thermodynamics of Vancomycin Binding to D-Ala-D-Ala vs D-Ala-D-Lac Mutants",
            "difficulty": "Advanced",
            "statement": r"""The glycopeptide antibiotic vancomycin binds to the peptidoglycan cell wall precursor terminal peptide $-L\text{-Lys}-D\text{-Ala}-D\text{-Ala}$ through a network of 5 cooperative hydrogen bonds. The association constant at $298\text{ K}$ is $K_a = 1.0\times 10^6\text{ M}^{-1}$.
(a) Compute the standard Gibbs free energy of binding $\Delta G^\circ_{\text{bind}}$ for vancomycin to $-D\text{-Ala}-D\text{-Ala}$.
(b) In vancomycin-resistant enterococci (VRE), the terminal dipeptide is modified by the VanA ligase to $-D\text{-Ala}-D\text{-Lac}$ (ester linkage instead of amide linkage). This single substitution replaces one $\text{N}-\text{H}\cdots\text{O}=\text{C}$ hydrogen bond with an oxygen-oxygen lone pair repulsion ($\text{O}\cdots\text{O}=\text{C}$). The binding constant plummets to $K_a = 1.0\times 10^3\text{ M}^{-1}$.
Calculate the thermodynamic destabilization $\Delta(\Delta G^\circ)$ caused by this single atom replacement, and explain why this 1,000-fold drop completely abolishes antibiotic efficacy.""",
            "hints": [
                r"\Delta G^\circ = -RT \ln K_a.",
                r"\Delta(\Delta G^\circ) = \Delta G^\circ(Lac) - \Delta G^\circ(Ala) = -RT \ln(K_a(Lac) / K_a(Ala)).",
                r"Clinical peak vancomycin concentration is typically 20-40 mg/L (15-30 \mu M)."
            ],
            "solution": r"""### Step 1: Gibbs Free Energy of Native Binding
At $T = 298.15\text{ K}$:
$$\Delta G^\circ_{\text{bind}}(D\text{-Ala-}D\text{-Ala}) = -R T \ln K_a$$
$$\Delta G^\circ_{\text{bind}} = -(8.314\text{ J/(mol}\cdot\text{K)})(298.15\text{ K}) \ln(1.0\times 10^6)$$
$$\Delta G^\circ_{\text{bind}} = -2478.9 \times 13.8155 = -34,247\text{ J/mol} = \mathbf{-34.25\text{ kJ/mol}}$$

### Step 2: Thermodynamic Destabilization by the $D\text{-Ala-}D\text{-Lac}$ Mutation
For the resistant mutant ($K_a = 1.0\times 10^3\text{ M}^{-1}$):
$$\Delta G^\circ_{\text{bind}}(D\text{-Ala-}D\text{-Lac}) = -2478.9 \ln(1.0\times 10^3) = -2478.9 \times 6.9078 = -17,124\text{ J/mol} = -17.12\text{ kJ/mol}$$
The loss in binding free energy is:
$$\Delta(\Delta G^\circ) = \Delta G^\circ(D\text{-Lac}) - \Delta G^\circ(D\text{-Ala}) = -17.12 - (-34.25) = \mathbf{+17.13\text{ kJ/mol}}$$
Replacing a single amide nitrogen ($-\text{NH}-$) with an ester oxygen ($-\text{O}-$) introduces a thermodynamic penalty of **$17.1\text{ kJ/mol}$**.
This consists of:
1. Loss of an attractive hydrogen bond ($\approx 12 - 15\text{ kJ/mol}$).
2. Electrostatic repulsion between the lone pairs of the ester oxygen and the vancomycin carbonyl oxygen ($\approx 3 - 5\text{ kJ/mol}$).

### Step 3: Pharmacological Abolition of Activity
In clinical practice:
- Therapeutic serum concentrations of vancomycin are maintained at $15 - 30\text{ \mu M}$ ($20 - 40\text{ mg/L}$).
- For wild-type bacteria ($K_d = 1 / K_a = 1.0\text{ \mu M}$), a drug concentration of $25\text{ \mu M}$ achieves $>96\%$ target receptor saturation, shutting down cell wall synthesis.
- For VRE mutants ($K_d = 1.0\text{ mM}$), a $25\text{ \mu M}$ drug concentration achieves only **$2.4\%$ receptor saturation**. The bacteria synthesize cell walls normally and grow uninhibited, rendering vancomycin clinically useless against VRE."""
        }
    }

    for u in units:
        uid = u["id"]
        if uid in prob8_dict:
            u["problems"].append(prob8_dict[uid])

    return units

if __name__ == "__main__":
    from build_natural_products_units_1_2_3 import get_units_1_2_3
    from build_natural_products_units_4_5_6 import get_units_4_5_6
    from build_natural_products_units_7_8_9_10 import get_units_7_8_9_10

    all_u = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    add_problem8_to_units(all_u)
    print("Verification of Problem 8 across all units:")
    for u in all_u:
        print(f"  {u['id']}: total problems = {len(u['problems'])}")
