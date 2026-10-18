#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_natural_products_units_7_8_9_10.py
Builds Units 7, 8, 9, and 10 (Sections 1-7, Solved Problems 1-7) for Chemistry of Natural Products.
Strictly zero course numbers, codes, or marks.
Raw triple quotes used throughout to prevent any escape sequence issues.
"""

def get_units_7_8_9_10():
    units = []

    # =========================================================================
    # UNIT 7: Purines, Pyrimidines & Nucleic Acid Biochemistry
    # =========================================================================
    u7 = {
        "id": "unit-7",
        "unitNumber": 7,
        "title": "Unit 7: Purines, Pyrimidines & Nucleic Acid Biochemistry",
        "leadSummary": "Heterocyclic and biophysical chemistry of purines, pyrimidines, and nucleic acids: Traube purine synthesis, oxidative degradations of uric acid (alloxan, allantoin), beta-N-glycosidic bond stereodynamics, Watson-Crick B-DNA geometry, cooperative thermal melting thermodynamics (Tm calculus), and high-fidelity enzymatic replication.",
        "simulations": ["sim_nat_dna_double_helix_melting"],
        "sections": [
            {
                "id": "sec-7-1",
                "secNumber": "7.1",
                "title": "Purine and Pyrimidine Bases: Nomenclature, Aromaticity & Tautomerism",
                "content": r"""Nucleic acids store and transmit genetic information using heterocyclic nitrogenous bases derived from two parent aromatic scaffolds: **purine** (fused pyrimidine-imidazole bicycle) and **pyrimidine** (six-membered diazine).

### The Canonical Bases
1. **Purines (Fused 9-Membered Bicycle)**:
   - **Adenine (A)**: 6-Aminopurine ($C_5H_5N_5$)
   - **Guanine (G)**: 2-Amino-6-oxopurine ($C_5H_5N_5O$)
2. **Pyrimidines (6-Membered Monocycle)**:
   - **Cytosine (C)**: 4-Amino-pyrimidin-2(1H)-one ($C_4H_5N_3O$)
   - **Uracil (U, in RNA)**: Pyrimidine-2,4(1H,3H)-dione ($C_4H_4N_2O_2$)
   - **Thymine (T, 5-methyluracil, in DNA)**: 5-Methylpyrimidine-2,4(1H,3H)-dione ($C_5H_6N_2O_2$)

### Aromaticity and UV Absorption
Purines and pyrimidines possess extensive delocalized $\pi$-systems obeying Hückel's $(4n+2)\pi$-electron rule ($10\pi$-electrons for purine, $6\pi$-electrons for pyrimidine). The electronic transitions ($\pi \to \pi^*$) give rise to strong ultraviolet absorption spectra with characteristic absorption maxima around **$\lambda_{\text{max}} \approx 260\text{ nm}$** ($\epsilon \sim 7,000 - 15,000\text{ M}^{-1}\text{cm}^{-1}$).

### Prototropic Tautomerism and Mutational Implications
Under physiological conditions, bases exist in dynamic prototropic equilibria:
- **Keto (Lactam) vs Enol (Lactim)**: Guanine, thymine, and uracil exist predominantly ($>99.99\%$) in the **keto (lactam)** tautomeric form.
- **Amino vs Imino**: Adenine and cytosine exist predominantly in the **amino** tautomeric form.
Transient shifts to the rare enol or imino tautomers (equilibrium constant $K_T \sim 10^{-4} - 10^{-5}$) alter the hydrogen-bonding donor/acceptor pattern:
- The rare imino form of adenine pairs aberrantly with cytosine instead of thymine ($A^* \cdot C$).
- The rare enol form of thymine pairs with guanine ($T^* \cdot G$).
These transient tautomeric shifts represent an intrinsic chemical source of spontaneous transition mutations during DNA replication."""
            },
            {
                "id": "sec-7-2",
                "secNumber": "7.2",
                "title": "Chemical Synthesis of Purines: The Traube Purine Synthesis",
                "content": r"""Wilhelm Traube developed the classical, robust synthetic methodology (1900) for constructing purines from simple acyclic precursors, which remains the primary industrial and laboratory route.

### The Traube Synthesis of Guanine
1. **Condensation to Pyrimidine**:
   Guanidine condenses with ethyl cyanoacetate in ethanolic sodium ethoxide:
   $$\text{H}_2\text{N-C}(=\text{NH})\text{-NH}_2 + \text{NC-CH}_2\text{-COOEt} \xrightarrow{\text{EtONa}} \text{2,4-diamino-6-hydroxypyrimidine}$$
2. **Nitrosation**:
   Treatment with nitrous acid ($\text{HNO}_2$) introduces a nitroso group at the nucleophilic C5 position:
   $$\to \text{2,4-diamino-5-nitroso-6-hydroxypyrimidine (a deep purple nitroso compound)}$$
3. **Reduction to 4,5-Diamine**:
   Catalytic hydrogenation or reduction with sodium dithionite ($\text{Na}_2\text{S}_2\text{O}_4$) or ammonium sulfide reduces the nitroso group to an amine, yielding **2,4,5-triamino-6-hydroxypyrimidine**.
4. **Ring Closure with C1 Donors (Formylation and Imidazole Ring Closure)**:
   Heating the 4,5-diaminopyrimidine with formic acid ($\text{HCOOH}$) or formamide introduces a formyl group ($-\text{CHO}$) at the C5-amino group.
   Subsequent heating above $200^\circ\text{C}$ or treatment with alkali induces intramolecular cyclodehydration between the formamide carbonyl and the C4 amino group, closing the 5-membered imidazole ring to afford **guanine**."""
            },
            {
                "id": "sec-7-3",
                "secNumber": "7.3",
                "title": "Uric Acid: Occurrence, Degradative Structural Elucidation & Oxidation Reactions",
                "content": r"""Uric acid (2,6,8-trioxypurine, $C_5H_4N_4O_3$) is the primary end-product of purine metabolism in birds, reptiles, and humans. Overproduction or impaired excretion causes hyperuricemia, leading to the deposition of monosodium urate crystals in joints (gout).

### Structural Proof through Classical Oxidative Degradation (Baeyer and Emil Fischer)
Uric acid was structurally elucidated by dissecting it with targeted oxidizing agents:
1. **Nitric Acid Oxidation (Cleavage of Imidazole Ring)**:
   Treatment of uric acid with concentrated nitric acid ($\text{HNO}_3$) selectively oxidizes and cleaves the five-membered imidazole ring, releasing **alloxan (mesoxalylurea)** and **urea**:
   $$\text{C}_5\text{H}_4\text{N}_4\text{O}_3 + [\text{O}] + \text{H}_2\text{O} \xrightarrow{\text{HNO}_3} \text{Alloxan } (C_4H_2N_2O_4) + \text{Urea } (CH_4N_2O)$$
   Alloxan is pyrimidine-2,4,5,6-tetraone. Reduction of alloxan with $\text{H}_2\text{S}$ yields dialuric acid; condensation of equimolar alloxan and dialuric acid yields the purple ammonium salt **murexide**, the basis of the diagnostic **murexide test** for uric acid.
2. **Alkaline Potassium Permanganate Oxidation (Cleavage of Pyrimidine Ring)**:
   Oxidation of uric acid with cold alkaline $\text{KMnO}_4$ selectively oxidizes the six-membered pyrimidine ring, cleaving it with loss of $\text{CO}_2$ to yield **allantoin** ($C_4H_6N_4O_3$):
   $$\text{C}_5\text{H}_4\text{N}_4\text{O}_3 + [\text{O}] + \text{H}_2\text{O} \xrightarrow{\text{KMnO}_4, \text{OH}^-} \text{Allantoin } (C_4H_6N_4O_3) + \text{CO}_2$$
   Further alkaline hydrolysis of allantoin cleaves it into **allantoic acid**, which hydrolyzes to **glyoxylic acid ($\text{CHO-COOH}$)** and **two equivalents of urea**.
These two complementary degradations—one isolating the intact pyrimidine ring (alloxan) and the other isolating the intact imidazole derivative (allantoin)—rigorously established the 2,6,8-trioxypurine constitution of uric acid."""
            },
            {
                "id": "sec-7-4",
                "secNumber": "7.4",
                "title": "Nucleosides and Nucleotides: $\\beta$-N-Glycosidic Bonds & Hydrolysis Mechanics",
                "content": r"""Nucleosides and nucleotides are the monomeric subunits of nucleic acids and vital biochemical cofactors (ATP, NAD+, CoA).

### Architecture and Nomenclature
- **Nucleoside**: A purine or pyrimidine base linked via a covalent **$\beta$-N-glycosidic bond** to the C1' carbon of a pentose sugar:
  - Ribose in ribonucleosides (Adenosine, Guanosine, Cytidine, Uridine).
  - 2'-Deoxyribose in 2'-deoxyribonucleosides (dA, dG, dC, dT).
  - Attachment point: Linked to **N9** of purines or **N1** of pyrimidines.
- **Nucleotide**: A nucleoside phosphorylated at one of its sugar hydroxyl groups (typically C5', C3', or C2'):
  - E.g., Adenosine 5'-monophosphate (AMP), adenosine 5'-triphosphate (ATP).

### Conformational Dynamics: Syn vs Anti
Rotation around the $\beta$-N-glycosidic bond ($\chi$ torsion angle) is restricted by steric interactions:
- **Anti Conformation**: The bulky Watson-Crick face of the base points **away** from the pentose sugar ring ($\chi \approx 180^\circ$ to $-120^\circ$).
- **Syn Conformation**: The base points directly **over** the furanose ring ($\chi \approx 0^\circ \pm 90^\circ$).
In canonical B-DNA and RNA duplexes, all bases adopt the **anti conformation** to permit unhindered Watson-Crick base pairing. Left-handed Z-DNA is a notable exception where alternating purines adopt the syn conformation.

### Hydrolysis Mechanics: RNA vs DNA
- **DNA is highly resistant to alkaline hydrolysis**: Because 2'-deoxyribose lacks a 2'-hydroxyl group, the phosphodiester backbone of DNA remains intact in $1\text{ M NaOH}$ for months.
- **RNA is rapidly cleaved in alkali**: The 2'-hydroxyl group ($-\text{OH}$) is deprotonated by base ($-\text{O}^-$), which attacks the adjacent phosphorus atom in an intramolecular nucleophilic substitution, forming a strained **2',3'-cyclic phosphate intermediate** that hydrolyzes randomly to 2'- and 3'-monophosphates, fragmenting the RNA chain within minutes."""
            },
            {
                "id": "sec-7-5",
                "secNumber": "7.5",
                "title": "Primary and Secondary Structure of DNA: Watson-Crick B-DNA Double Helix",
                "content": r"""In 1953, James Watson and Francis Crick elucidated the double-helical structure of deoxyribonucleic acid (B-DNA), incorporating Rosalind Franklin's Photo 51 X-ray fiber diffraction data and Erwin Chargaff's rules of base equivalence.

### Watson-Crick B-DNA Geometric Parameters
1. **Right-Handed Antiparallel Strands**: Two polynucleotide chains wind around a central axis in a right-handed helix, running in opposite directions ($5^\prime \to 3^\prime$ and $3^\prime \to 5^\prime$).
2. **Helical Dimensions**:
   - Diameter of duplex: $2.0\text{ nm}$ ($20\text{ \AA}$).
   - Helical pitch (one complete turn): $3.4\text{ nm}$ ($34\text{ \AA}$).
   - Base pairs per turn: $10.5\text{ bp}$ in solution ($10.0\text{ bp}$ in fiber crystal).
   - Axial rise per base pair ($h$): $0.34\text{ nm}$ ($3.4\text{ \AA}$).
3. **Major and Minor Grooves**: Because the glycosidic bonds do not emanate at $180^\circ$ directly opposite each other, helical twisting creates two unequal surface indentations:
   - **Major Groove**: Wide ($12\text{ \AA}$) and deep ($8.5\text{ \AA}$), presenting sequence-specific arrays of hydrogen-bond donors, acceptors, and methyl groups that enable recognition by transcription factors and restriction enzymes.
   - **Minor Groove**: Narrow ($6\text{ \AA}$) and deep ($7.5\text{ \AA}$).

### Thermodynamic Stability: Base Stacking vs Hydrogen Bonding
While complementary Watson-Crick base pairing ($\text{A}=\text{T}$ with 2 hydrogen bonds; $\text{G}\equiv\text{C}$ with 3 hydrogen bonds) provides strict genetic specificity, the primary thermodynamic driving force stabilizing the double helix is **hydrophobic $\pi$-$\pi$ base stacking**:
$$\Delta G^\circ_{\text{duplex}} = \sum \Delta G^\circ_{\text{stacking}} + \sum \Delta G^\circ_{\text{H-bonds}} + \Delta G^\circ_{\text{electrostatic}}$$
Aromatic base rings stack planar surfaces at van der Waals contact distance ($3.4\text{ \AA}$), burying hydrophobic surfaces and displacing organized water molecules into bulk solvent."""
            },
            {
                "id": "sec-7-6",
                "secNumber": "7.6",
                "title": "Thermal Denaturation of DNA: Hyperchromism, Melting Curves & $T_m$ Calculus",
                "content": r"""Thermal denaturation (DNA melting) is the reversible, cooperative separation of the double-stranded helix into two random-coil single strands upon heating.

### The Hyperchromic Effect
- In native double-stranded DNA, the closely stacked aromatic base pairs align their transition dipoles in parallel arrays, resulting in mutual dipole shielding and **hypochromicity** (suppression of UV absorption at $260\text{ nm}$).
- Upon denaturation into unstacked single strands, electronic transition dipoles become uncoupled, causing a **$30–40\%$ increase in UV absorbance at $260\text{ nm}$**, termed the **hyperchromic effect**.

### Melting Temperature ($T_m$)
The melting temperature ($T_m$) is the temperature at which exactly $50\%$ of the helical structure is denatured ($f_{\text{denatured}} = 0.50$).
1. **Dependence on GC Content**:
   Each $\text{G}\equiv\text{C}$ base pair contributes three hydrogen bonds and stronger base stacking compared to two hydrogen bonds in an $\text{A}=\text{T}$ pair. For long DNA duplexes in $1\text{ M Na}^+$ (Marmur-Doty equation):
   $$T_m = 69.3^\circ\text{C} + 0.41 \times (\% \text{GC})$$
2. **Dependence on Ionic Strength**:
   The negatively charged phosphate diester groups ($-\text{O}-\text{PO}_2^--\text{O}-$) along the sugar-phosphate backbones repel each other across the minor and major grooves. Divalent ($Mg^{2+}$) and monovalent ($Na^+$) cations screen these electrostatic repulsions, dramatically stabilizing the helix and raising $T_m$:
   $$T_m = 81.5 + 16.6 \log_{10}[\text{Na}^+] + 0.41(\% \text{GC}) - \frac{675}{L}$$
   where $L$ is the length of the duplex in base pairs."""
            },
            {
                "id": "sec-7-7",
                "secNumber": "7.7",
                "title": "RNA Architectures & Enzymatic Functions: mRNA, tRNA, Ribozymes & Replication",
                "content": r"""Unlike double-stranded DNA, ribonucleic acid (RNA) molecules typically exist as single strands that fold into intricate three-dimensional tertiary architectures capable of catalytic function (ribozymes).

### Structural Diversity of Cellular RNAs
1. **Messenger RNA (mRNA)**: Transmits coding sequence from genomic DNA to the ribosome. Eukaryotic mRNAs feature a $5^\prime\text{-m}^7\text{GpppN}$ cap and a $3^\prime\text{-poly(A)}$ tail.
2. **Transfer RNA (tRNA)**: Molecular adaptors (76–90 nucleotides) translating triplet codons into amino acids.
   - **Secondary Structure**: Classical cloverleaf with acceptor stem, D-loop, anticodon loop, and T$\psi$C-loop.
   - **Tertiary Structure**: Coaxial stacking folds the cloverleaf into an **L-shaped architecture** with the anticodon at one tip and the 3'-CCA-OH aminoacyl attachment site at the other, $75\text{ \AA}$ apart.
3. **Ribosomal RNA (rRNA)**: Structural and catalytic core of the ribosome. Thomas Steitz and coworkers proved that the peptidyl transferase center of the 50S large subunit is composed purely of 23S rRNA with zero protein side chains within $18\text{ \AA}$, establishing that the ribosome is a **ribozyme**.

### Catalytic RNAs (Ribozymes)
Discovered by Thomas Cech (self-splicing group I intron of *Tetrahymena*) and Sidney Altman (RNase P), ribozymes utilize coordinated divalent metal ions ($Mg^{2+}$) and active-site nucleobases with shifted $pK_a$ values to catalyze phosphodiester transesterifications and cleavages with rate enhancements exceeding $10^{11}$-fold."""
            }
        ],
        "problems": [
            {
                "id": "prob-7-1",
                "problemNumber": "7.1",
                "title": "Traube Synthesis Route and Stepwise Stoichiometry of Adenine",
                "statement": r"""Outline the complete Traube synthesis of adenine ($C_5H_5N_5$) starting from thiourea ($\text{H}_2\text{N-CS-NH}_2$) and malononitrile ($\text{CH}_2(\text{CN})_2$):
(a) Write the balanced equations for the initial condensation to 4,6-diamino-2-mercaptopyrimidine and subsequent nitrosation.
(b) Outline the reduction of the nitroso group, formylation, and imidazole ring closure.
(c) How is the mercapto group at C2 removed to furnish pure adenine?""",
                "hints": [
                    r"Thiourea condenses with malononitrile in base to form a pyrimidine with sulfur at C2.",
                    r"Nitrosation adds -NO at C5.",
                    r"Raney nickel desulfurization cleaves C-S bonds to form C-H."
                ],
                "solution": r"""### Step 1: Condensation and Nitrosation
1. **Pyrimidine Ring Formation**:
   Thiourea condenses with malononitrile in ethanolic sodium ethoxide:
   $$\text{H}_2\text{N-CS-NH}_2 + \text{NC-CH}_2\text{-CN} \xrightarrow{\text{EtONa}} \text{4,6-diamino-2-mercaptopyrimidine}$$
2. **Nitrosation at C5**:
   Reaction with nitrous acid ($\text{NaNO}_2 / \text{HCl}$) introduces a nitroso group at the electron-rich C5 carbon:
   $$\to \text{4,6-diamino-2-mercapto-5-nitrosopyrimidine}$$

### Step 2: Reduction, Formylation, and Cyclization
1. **Reduction**:
   The nitroso group is reduced with sodium dithionite ($\text{Na}_2\text{S}_2\text{O}_4$) or catalytic hydrogenation over Pd/C:
   $$\to \text{2-mercapto-4,5,6-triaminopyrimidine}$$
2. **Formylation and Imidazole Closure**:
   Refluxing with concentrated formic acid ($\text{HCOOH}$) formylates the C5 amino group. Subsequent heating at $220^\circ\text{C}$ dehydrates the formamide, closing the imidazole ring to afford **6-amino-2-mercaptopurine (2-mercaptoadenine)**.

### Step 3: Desulfurization to Adenine
The mercapto ($-\text{SH}$) group at C2 is reductively cleaved by stirring with **Raney nickel (Raney Ni)** in boiling aqueous ethanol:
$$\text{2-Mercaptoadenine} \xrightarrow{\text{Raney Ni, } \Delta} \text{Adenine } (C_5H_5N_5) + \text{NiS}$$
This oxidative/reductive sequence cleanly furnishes pure adenine in high overall yield."""
            },
            {
                "id": "prob-7-2",
                "problemNumber": "7.2",
                "title": "Uric Acid Oxidation Mechanism to Alloxan and Dialuric Acid",
                "statement": r"""When uric acid is treated with warm concentrated nitric acid, it decomposes into alloxan and urea:
(a) Provide the curved-arrow mechanism for the nitric acid oxidation of the 7,8-double bond/carbonyl of the imidazole ring, showing how urea is expelled.
(b) Reduction of alloxan with hydrogen sulfide ($\text{H}_2\text{S}$) yields dialuric acid. Write the structure of dialuric acid and explain how condensation of dialuric acid with alloxan produces the purpurate dye ammonium purpurate (murexide).""",
                "hints": [
                    r"Uric acid has a 2,6,8-trioxo structure.",
                    r"Nitric acid oxidizes C4-C5 to diols, opening the imidazole ring.",
                    r"Alloxan is pyrimidine-2,4,5,6-tetraone; dialuric acid is 5-hydroxybarbituric acid."
                ],
                "solution": r"""### Step 1: Oxidation Mechanism to Alloxan
1. **Electrophilic Addition across C4-C5**:
   Nitric acid adds two hydroxyl equivalents across the central C4=C5 bridge of uric acid, generating **4,5-dihydroxy-4,5-dihydrouric acid (uric acid glycol)**.
2. **Ring Cleavage**:
   The electron pairs on the C4 and C5 hydroxyl groups push into carbonyl $\pi$-bonds, cleaving the two $\text{C-N}$ bonds linking C4 and C5 to the N7 and N9 nitrogens of the imidazole ring:
   $$\text{Uric acid glycol} \to \text{Alloxan} + \text{H}_2\text{N-CO-NH}_2 \quad (\mathbf{Urea})$$
   Alloxan is isolated as alloxan monohydrate (pyrimidine-2,4,6-trione with a geminal diol at C5).

### Step 2: Reduction to Dialuric Acid and Murexide Formation
1. **Reduction with $\text{H}_2\text{S}$**:
   Reduction of alloxan with $\text{H}_2\text{S}$ reduces the C5 carbonyl to a secondary alcohol, yielding **dialuric acid (5-hydroxybarbituric acid)**:
   $$\text{Alloxan} + \text{H}_2\text{S} \to \text{Dialuric acid} + \text{S}(s)$$
2. **Murexide (Ammonium Purpurate) Synthesis**:
   Condensation of dialuric acid with alloxan in the presence of ammonia proceeds through an amino intermediate to form the bis-pyrimidine anion **purpurate**:
   $$\text{Dialuric acid} + \text{Alloxan} + \text{NH}_3 \to \text{Ammonium Purpurate (Murexide)}$$
   In the purpurate anion, two barbiturate rings are linked by a central nitrogen atom ($=\text{N}-$). Extensive delocalization across the symmetric conjugated chromophore creates an intense purple-violet color ($\lambda_{\text{max}} = 530\text{ nm}$), confirming the presence of uric acid."""
            },
            {
                "id": "prob-7-3",
                "problemNumber": "7.3",
                "title": "Tautomeric Equilibrium Constant ($K_T$) of Uracil and Mutagenic Mis-Pairing",
                "statement": r"""At $298\text{ K}$, the tautomeric equilibrium constant between the rare enol (lactim) and dominant keto (lactam) tautomers of 5-bromouracil (5-BU) is $K_T = [\text{enol}] / [\text{keto}] = 2.0\times 10^{-3}$, compared to $K_T = 1.0\times 10^{-5}$ for normal thymine.
(a) Calculate the standard free energy difference $\Delta G^\circ_T$ for the keto $\to$ enol tautomerization of thymine vs 5-bromouracil.
(b) Explain why 5-bromouracil is a potent chemical mutagen, diagramming how its enol form base-pairs with guanine to cause $AT \to GC$ transition mutations during rounds of replication.""",
                "hints": [
                    r"\Delta G^\circ = -RT \ln K_T.",
                    r"The normal keto form of 5-BU pairs with adenine.",
                    r"The enol form presents a hydrogen bond donor at O4 and acceptor at N3, mirroring cytosine."
                ],
                "solution": r"""### Step 1: Free Energy Calculation of Tautomerization
Using $\Delta G^\circ_T = -R T \ln K_T$ at $T = 298.15\text{ K}$ ($R T = 2.4789\text{ kJ/mol}$):
1. **For Thymine ($K_T = 1.0\times 10^{-5}$)**:
   $$\Delta G^\circ_T = -2.4789 \ln(1.0\times 10^{-5}) = -2.4789 \times (-11.513) = \mathbf{+28.54\text{ kJ/mol}}$$
2. **For 5-Bromouracil ($K_T = 2.0\times 10^{-3}$)**:
   $$\Delta G^\circ_T = -2.4789 \ln(2.0\times 10^{-3}) = -2.4789 \times (-6.2146) = \mathbf{+15.41\text{ kJ/mol}}$$
The electron-withdrawing bromine atom at C5 stabilizes the enolate resonance form, lowering the free energy penalty by $13.1\text{ kJ/mol}$ and increasing the enol population by a factor of **200-fold**.

### Step 2: Mutagenic Mechanism of 5-Bromouracil
1. **First Replication Round (Incorporation)**:
   In its predominant keto form, 5-BU pairs correctly with Adenine (A), incorporating into the nascent DNA strand opposite A:
   $$\text{A} \cdot \text{5-BU(keto)}$$
2. **Second Replication Round (Mis-pairing)**:
   When the DNA is replicated, if 5-BU shifts into its rare enol tautomer:
   - The enol group at C4 ($-\text{OH}$) acts as a hydrogen-bond donor.
   - The ring nitrogen N3 loses its proton and acts as a hydrogen-bond acceptor.
   - This donor-acceptor array is structurally identical to cytosine and forms three stable Watson-Crick hydrogen bonds with **Guanine (G)**:
     $$\text{5-BU(enol)} \equiv \text{G}$$
3. **Third Replication Round (Fixation of Mutation)**:
   The newly incorporated Guanine pairs with Cytosine (C) in subsequent replication:
   $$\text{G} \equiv \text{C}$$
The original $\mathbf{A\cdot T}$ base pair is permanently converted to a $\mathbf{G\cdot C}$ base pair (an **$AT \to GC$ transition mutation**)."""
            },
            {
                "id": "prob-7-4",
                "problemNumber": "7.4",
                "title": "DNA Melting Temperature ($T_m$) Calculus across Ionic Strength and %GC",
                "statement": r"""A PCR diagnostic primer duplex has a length of $L = 24\text{ base pairs}$ with the sequence:
$$5^\prime\text{-CCG GAT CGC CTA TCG ATC GGC CTA-}3^\prime$$
(a) Count the number of GC and AT base pairs and calculate the percentage GC content (%GC).
(b) Using the empirical nearest-neighbor/salt-adjusted melting temperature formula:
$$T_m = 81.5 + 16.6 \log_{10}[\text{Na}^+] + 0.41(\% \text{GC}) - \frac{675}{L}$$
Calculate $T_m$ at $[\text{Na}^+] = 0.050\text{ M}$ ($50\text{ mM}$) and at $[\text{Na}^+] = 1.00\text{ M}$. Explain the physical cause of the $T_m$ shift.""",
                "hints": [
                    r"Count G+C in the 24-mer sequence.",
                    r"%GC = (N_{GC} / L) * 100%.",
                    r"Compute \log_{10}(0.050) = -1.301; \log_{10}(1.00) = 0."
                ],
                "solution": r"""### Step 1: Sequence Composition and %GC
Analyzing the 24-nucleotide sequence:
- Guanine (G) count: 6
- Cytosine (C) count: 9
- Total $N_{\text{GC}} = 6 + 9 = 15$
- Total $N_{\text{AT}} = 24 - 15 = 9$
$$\% \text{GC} = \frac{15}{24} \times 100\% = \mathbf{62.5\%}$$

### Step 2: Melting Temperature at $[\text{Na}^+] = 0.050\text{ M}$
$$\log_{10}(0.050) = -1.3010$$
$$T_m = 81.5 + 16.6(-1.3010) + 0.41(62.5) - \frac{675}{24}$$
$$T_m = 81.5 - 21.60 + 25.625 - 28.125 = \mathbf{57.4^\circ\text{C}}$$

### Step 3: Melting Temperature at $[\text{Na}^+] = 1.00\text{ M}$
$$\log_{10}(1.00) = 0.000$$
$$T_m = 81.5 + 16.6(0) + 25.625 - 28.125 = 81.5 - 2.50 = \mathbf{79.0^\circ\text{C}}$$

### Step 4: Physical Origin of the $\Delta T_m = +21.6^\circ\text{C}$ Shift
Each nucleotide of the DNA backbone carries a formal negative charge of $-1$ on its phosphate group ($-\text{O}-\text{PO}_2^--\text{O}-$). In the duplex, these charges are spaced closely along the double helix ($r \approx 10 - 20\text{ \AA}$), generating strong inter-strand electrostatic repulsion that favors strand separation into random coils.
- At low salt ($50\text{ mM Na}^+$), the Debye screening length is large ($\kappa^{-1} \approx 13.6\text{ \AA}$), allowing substantial charge repulsion that destabilizes the duplex ($T_m = 57.4^\circ\text{C}$).
- At high salt ($1.0\text{ M Na}^+$), sodium cations form a tight condensation counterion atmosphere around the polyanion backbone, screening negative charges ($\kappa^{-1} \approx 3.0\text{ \AA}$). This eliminates repulsive electrostatic energy, raising $T_m$ by over $21^\circ\text{C}$."""
            },
            {
                "id": "prob-7-5",
                "problemNumber": "7.5",
                "title": "Alkaline Hydrolysis Resistance of DNA vs RNA Cleavage via 2',3'-Cyclic Phosphate",
                "statement": r"""When treated with $0.10\text{ M NaOH}$ at $100^\circ\text{C}$:
- RNA is completely cleaved into a mixture of 2'- and 3'-mononucleotides within 30 minutes.
- DNA remains fully intact without detectable cleavage of phosphodiester bonds.
(a) Draw the curved-arrow mechanism for the base-catalyzed hydrolysis of RNA, detailing the formation of the pentacoordinate phosphorane transition state and the 2',3'-cyclic phosphate intermediate.
(b) Explain why DNA is completely resistant to this intramolecular pathway and calculate the pseudo-first-order half-life for uncatalyzed DNA phosphodiester bond hydrolysis in neutral water at $25^\circ\text{C}$ (given $k \approx 3.0\times 10^{-16}\text{ s}^{-1}$).""",
                "hints": [
                    r"RNA has a 2'-OH; DNA has 2'-H.",
                    r"Deprotonated 2'-O(-) attacks the adjacent 3'-phosphorus atom.",
                    r"Use t_{1/2} = ln(2) / k for DNA uncatalyzed hydrolysis."
                ],
                "solution": r"""### Step 1: RNA Hydrolysis Mechanism via 2',3'-Cyclic Phosphate
1. **Deprotonation of 2'-Hydroxyl**:
   Hydroxide ion abstracts the proton from the 2'-hydroxyl group of the ribose ring:
   $$\text{Ribose-2'-OH} + \text{OH}^- \rightleftharpoons \text{Ribose-2'-O}^- + \text{H}_2\text{O}$$
2. **Intramolecular Nucleophilic Attack**:
   The resulting alkoxide oxygen ($\text{O2}^\prime$) is in close spatial proximity to the adjacent 3'-phosphodiester group. It attacks the phosphorus atom in an intramolecular $S_N2(\text{P})$ reaction:
   - Forms a trigonal bipyramidal pentacoordinate phosphorane transition state.
3. **Chain Cleavage**:
   Collapse of the phosphorane expels the 5'-hydroxyl group of the adjacent downstream nucleotide ($\text{RO}^-$ leaving group):
   - This cleaves the RNA phosphodiester backbone.
   - The upstream nucleotide is converted into a **2',3'-cyclic phosphate diester**.
4. **Ring Opening**:
   Water/hydroxide attacks the strained cyclic phosphate, hydrolyzing it into a mixture of **nucleoside 2'-monophosphate** and **nucleoside 3'-monophosphate**.

### Step 2: DNA Resistance and Kinetic Half-Life
1. **Absence of 2'-OH in DNA**:
   DNA contains 2'-deoxyribose, which possesses only hydrogen atoms at C2' ($-\text{CH}_2-$). It lacks a nucleophilic 2'-hydroxyl group to initiate intramolecular cyclization. Cleavage of DNA requires intermolecular attack by external hydroxide, which is electrostatically repelled by the $-1$ charge of the phosphodiester anion.
2. **Kinetic Half-Life of DNA**:
   With $k \approx 3.0\times 10^{-16}\text{ s}^{-1}$:
   $$t_{1/2} = \frac{\ln 2}{k} = \frac{0.6931}{3.0\times 10^{-16}\text{ s}^{-1}} = 2.31\times 10^{15}\text{ s}$$
   Converting to years ($1\text{ year} = 3.154\times 10^7\text{ s}$):
   $$t_{1/2} = \frac{2.31\times 10^{15}\text{ s}}{3.154\times 10^7\text{ s/year}} \approx \mathbf{73\text{ million years}}$$
DNA is exceptionally stable, which is an absolute evolutionary requirement for long-term genomic integrity."""
            },
            {
                "id": "prob-7-6",
                "problemNumber": "7.6",
                "title": "Thermodynamics of Base Stacking vs Hydrogen Bonding in DNA Helices",
                "statement": r"""Experimental thermodynamic measurements for the association of a self-complementary hexamer duplex at $298\text{ K}$ yield:
$$\Delta H^\circ_{\text{duplex}} = -180.0\text{ kJ/mol}, \quad \Delta S^\circ_{\text{duplex}} = -480.0\text{ J/(mol}\cdot\text{K)}$$
(a) Compute $\Delta G^\circ_{\text{duplex}}$ at $298\text{ K}$ and the duplex association equilibrium constant $K_a$.
(b) In non-aqueous polar solvents (e.g., anhydrous formamide or DMSO), base pairing hydrogen bonds are stronger or comparable to water, yet the DNA double helix completely denatures. Explain this phenomenon in terms of the hydrophobic effect and $\pi$-$\pi$ base stacking enthalpy/entropy.""",
                "hints": [
                    r"\Delta G^\circ = \Delta H^\circ - T \Delta S^\circ.",
                    r"K_a = \exp(-\Delta G^\circ / RT).",
                    r"Water drives the hydrophobic association of aromatic rings. Formamide solubilizes hydrophobic bases."
                ],
                "solution": r"""### Step 1: Free Energy and Association Constant Calculation
At $T = 298.15\text{ K}$:
$$\Delta G^\circ_{\text{duplex}} = \Delta H^\circ - T \Delta S^\circ$$
$$\Delta G^\circ_{\text{duplex}} = -180,000\text{ J/mol} - (298.15\text{ K})(-480.0\text{ J/(mol}\cdot\text{K)})$$
$$\Delta G^\circ_{\text{duplex}} = -180,000 + 143,112 = -36,888\text{ J/mol} = \mathbf{-36.89\text{ kJ/mol}}$$
The association equilibrium constant is:
$$K_a = \exp\left(-\frac{\Delta G^\circ}{R T}\right) = \exp\left(\frac{36,888}{(8.314)(298.15)}\right) = \exp(14.881) = \mathbf{2.90\times 10^6\text{ M}^{-1}}$$

### Step 2: Role of Non-Aqueous Solvents and Base Stacking
- In aqueous solution, the hydrophobic planar surfaces of purine and pyrimidine rings force adjacent water molecules into highly ordered hydrogen-bonded clathrate cages ($\Delta S < 0$).
- When two bases stack on top of each other in the double helix:
  - Hydrophobic surface area is buried.
  - Ordered water molecules are released into bulk solution, providing an entropic driving force ($\Delta S_{\text{solv}} > 0$).
  - London dispersion forces between delocalized $\pi$-systems provide substantial negative enthalpy ($\Delta H_{\text{stack}} \approx -15\text{ to } -35\text{ kJ/mol}$).
- In polar organic solvents such as formamide ($\text{HCONH}_2$) or DMSO:
  - Formamide interacts favorably with the aromatic nucleobases via dipole-$\pi$ and van der Waals interactions, eliminating the hydrophobic driving force for stacking ($\Delta G^\circ_{\text{stack}} \to 0$).
  - Formamide also competes aggressively as a hydrogen-bond donor and acceptor against the Watson-Crick amino and carbonyl groups.
  - Without base-stacking stabilization, the entropic penalty of bringing two rigid strands together ($\Delta S^\circ_{\text{conformational}} \ll 0$) dominates, causing the DNA duplex to spontaneously melt at room temperature."""
            },
            {
                "id": "prob-7-7",
                "problemNumber": "7.7",
                "title": "Phosphoramidite Coupling Mechanism and Stepwise Oligonucleotide Synthesis Yield",
                "statement": r"""Chemical synthesis of custom DNA oligonucleotides is performed on controlled-pore glass (CPG) solid support using $\beta$-cyanoethyl phosphoramidite chemistry (Caruthers methodology).
(a) Outline the four chemical steps of one elongation cycle: (1) Detritylation, (2) Coupling with 1H-tetrazole, (3) Capping, and (4) Oxidation with iodine.
(b) A 100-mer oligonucleotide is synthesized with an average coupling efficiency of $99.0\%$ per cycle. Calculate the overall percentage yield of full-length product, and determine the improvement if the efficiency is enhanced to $99.7\%$.""",
                "hints": [
                    r"Step 1: DMT removal with TCA.",
                    r"Step 2: Activation of phosphoramidite with tetrazole and attack by 5'-OH.",
                    r"Step 3: Acetic anhydride capping.",
                    r"Step 4: Oxidation of P(III) phosphite to P(V) phosphate with I2/pyridine/H2O.",
                    r"Overall yield for N-mer: Y = y^(N-1)."
                ],
                "solution": r"""### Step 1: The Four-Step Phosphoramidite Cycle
1. **Detritylation (Deprotection)**:
   The 5'-dimethoxytrityl (DMT) protecting group on the growing solid-supported chain is removed with $3\%$ trichloroacetic acid (TCA) in dichloromethane:
   $$\text{DMT-O-Oligo} \xrightarrow{\text{TCA}} \text{HO-Oligo} + \text{DMT}^+ \quad (\text{Bright orange cation, } \lambda_{\text{max}} = 498\text{ nm})$$
2. **Coupling (Activation and Nucleophilic Attack)**:
   The incoming 5'-DMT-nucleoside-3'-O-($\beta$-cyanoethyl-$N,N$-diisopropyl) phosphoramidite is mixed with **1H-tetrazole** (or 5-ethylthiotetrazole):
   - Tetrazole protonates the diisopropylamine group, converting it into a leaving group.
   - The free 5'-OH of the support-bound oligomer attacks the activated phosphite center, forming a **trivalent phosphite triester linkage** ($P^{\text{III}}$).
3. **Capping**:
   Unreacted 5'-OH groups are permanently capped with acetic anhydride and 1-methylimidazole (NMI) to prevent one-base deletion sequences.
4. **Oxidation**:
   The unstable trivalent phosphite triester ($P^{\text{III}}$) is oxidized to the stable pentavalent phosphate triester ($P^{\text{V}}$) using iodine in aqueous pyridine/THF:
   $$\text{P(III)} + \text{I}_2 + \text{H}_2\text{O} \to \text{P(V)}=\text{O} + 2\text{ HI}$$

### Step 2: Stepwise Efficiency Compounding for a 100-mer
For a 100-mer oligonucleotide, there are $N - 1 = 99$ coupling cycles:
1. **At $99.0\%$ Coupling Efficiency ($y = 0.990$)**:
   $$Y_{99.0\%} = (0.990)^{99} = \mathbf{0.369} \implies \mathbf{36.9\%}$$
2. **At $99.7\%$ Coupling Efficiency ($y = 0.997$)**:
   $$Y_{99.7\%} = (0.997)^{99} = \mathbf{0.742} \implies \mathbf{74.2\%}$$
An improvement of just $0.7\%$ in cycle efficiency **doubles the final yield** of the 100-mer from $36.9\%$ to $74.2\%$, demonstrating why coupling efficiencies exceeding $99.5\%$ are mandatory in automated oligonucleotide synthesis."""
            }
        ]
    }
    units.append(u7)

    # =========================================================================
    # UNIT 8: Alkaloids: Structural Elucidation, Degradation & Bioactive Classes
    # =========================================================================
    u8 = {
        "id": "unit-8",
        "unitNumber": 8,
        "title": "Unit 8: Alkaloids: Structural Elucidation, Degradation & Bioactive Classes",
        "leadSummary": "Comprehensive physical organic, degradative, and biosynthetic chemistry of alkaloids: classical precipitation tests, acid-base partitioning, Hofmann exhaustive methylation mechanics, Emde reduction, von Braun cyanogen bromide degradation, zinc dust distillation, and complete structural elucidations and total syntheses of ephedrine, atropine (Robinson's biomimetic tropinone synthesis), and morphine.",
        "simulations": ["sim_nat_hofmann_exhaustive_methylation"],
        "sections": [
            {
                "id": "sec-8-1",
                "secNumber": "8.1",
                "title": "Alkaloids: Definition, Physiological Activity & Taxonomic Classification",
                "content": r"""Alkaloids are basic, nitrogenous organic secondary metabolites, predominantly produced by plants (and select fungi, amphibians, and marine invertebrates), that exhibit pronounced physiological and pharmacological activities in animals.

### Defining Criteria
A natural compound is classified as an alkaloid if it fulfills three criteria:
1. It contains at least one **nitrogen atom** in a negative oxidation state.
2. It exhibits basic character (forming crystalline, water-soluble salts with mineral acids: $\text{Alk-H}^+ \text{Cl}^-$).
3. It exerts marked pharmacodynamic activity on the central or autonomic nervous system.

### Classification Systems
1. **True Alkaloids**: Derived directly from proteinogenic amino acids and containing the nitrogen atom embedded inside a **heterocyclic ring** (e.g., morphine, atropine, nicotine, quinine).
2. **Protoalkaloids**: Derived from amino acids, but the nitrogen atom resides in an **acyclic side chain** rather than a ring (e.g., ephedrine, mescaline, capsaicin).
3. **Pseudoalkaloids**: Nitrogen is incorporated into a heterocyclic or carbocyclic framework, but the carbon skeleton is **not derived from amino acids**; instead, it originates from terpenes or polyketides (e.g., caffeine from purines; solanidine and conessine from steroids; aconitine from diterpenes)."""
            },
            {
                "id": "sec-8-2",
                "secNumber": "8.2",
                "title": "Extraction and Isolation of Alkaloids: Acid-Base Partitioning & Reagents",
                "content": r"""Because alkaloids exist naturally as salts of organic acids (citric, malic, oxalic, meconic acid) or bound to tannins, their isolation exploits their pH-dependent partition equilibria.

### Acid-Base Liquid-Liquid Partitioning Protocol
1. **Acidic Digestion**: Dried botanical biomass is pulverized and extracted with dilute aqueous acid ($1–2\%\text{ HCl}$ or $\text{H}_2\text{SO}_4$). Basic alkaloids are protonated into water-soluble ammonium cations ($\text{R}_3\text{N} + \text{H}^+ \to \text{R}_3\text{NH}^+$), while neutral lipids, waxes, and terpenes remain insoluble.
2. **Defatting**: The acidic aqueous extract is washed with non-polar organic solvent (hexane or pet ether) to strip trace lipophilic impurities.
3. **Basification**: The aqueous layer is rendered alkaline ($\text{pH } 9–11$) with aqueous ammonia ($\text{NH}_4\text{OH}$) or sodium carbonate ($\text{Na}_2\text{CO}_3$). Deprotonation converts the alkaloids back into neutral, lipophilic free bases:
   $$\text{R}_3\text{NH}^+ + \text{OH}^- \to \text{R}_3\text{N} + \text{H}_2\text{O}$$
4. **Organic Extraction**: The free alkaloid bases are extracted into chloroform ($\text{CHCl}_3$), dichloromethane ($\text{CH}_2\text{Cl}_2$), or ethyl acetate, leaving water-soluble sugars and inorganic salts in the aqueous layer.

### Classical Alkaloid Precipitation Reagents
- **Mayer's Reagent**: Potassium mercuric iodide ($\text{K}_2[\text{HgI}_4]$), yields a white/cream precipitate.
- **Dragendorff's Reagent**: Potassium bismuth iodide ($\text{K}[\text{BiI}_4]$), yields an orange-red precipitate.
- **Wagner's Reagent**: Iodine in potassium iodide ($I_2 / KI$), yields a reddish-brown precipitate.
- **Hager's Reagent**: Saturated picric acid solution, forms crystalline yellow alkaloid picrates with sharp melting points."""
            },
            {
                "id": "sec-8-3",
                "secNumber": "8.3",
                "title": "Structural Elucidation I: Hofmann Exhaustive Methylation Mechanism & Ring Cleavage",
                "content": r"""August Wilhelm von Hofmann (1851) introduced the definitive chemical method for determining the connectivity and ring size of nitrogen heterocycles in alkaloids.

### Reaction Principles and Sequence
Hofmann exhaustive methylation systematically converts a cyclic amine into an open-chain diene:
1. **Quaternization**: The alkaloid amine is treated with excess methyl iodide ($\text{CH}_3\text{I}$) until all basic nitrogens are converted into quaternary ammonium iodides:
   $$\text{R}_3\text{N} + \text{CH}_3\text{I} \to \text{R}_3\text{N}^+(\text{CH}_3) \text{I}^-$$
2. **Conversion to Hydroxide**: The quaternary iodide is treated with moist silver oxide ($\text{Ag}_2\text{O} / \text{H}_2\text{O}$) to precipitate silver iodide, leaving the quaternary ammonium hydroxide:
   $$2\text{ R}_4\text{N}^+\text{I}^- + \text{Ag}_2\text{O} + \text{H}_2\text{O} \to 2\text{ R}_4\text{N}^+\text{OH}^- + 2\text{ AgI}(s)$$
3. **Thermal Hofmann Elimination ($\Delta$)**: Pyrolysis of the quaternary ammonium hydroxide ($100–150^\circ\text{C}$) induces an E2 elimination:
   - The basic hydroxide ion abstracts a $\beta$-hydrogen.
   - The $\text{C}-\text{N}^+$ bond cleaves, eliminating the nitrogen as a neutral amine and creating a carbon-carbon double bond:
   $$\text{HO}^- + \text{H}-\text{C}_\beta-\text{C}_\alpha-\text{N}^+\text{R}_3 \xrightarrow{\Delta} \text{H}_2\text{O} + \text{C}=\text{C} + \text{N}\text{R}_3$$
4. **Hofmann Regiochemistry Rule**: Unlike E2 eliminations with neutral halides (which follow Zaitsev's rule favoring the more substituted alkene), Hofmann elimination of quaternary ammonium salts selectively abstracts the **least hindered $\beta$-proton**, yielding the **least substituted (terminal) alkene**.

### Diagnostic Ring Rules
- If the nitrogen atom is **monocyclic**:
  - The first Hofmann cycle opens the ring, producing an unsaturated open-chain tertiary amine (the nitrogen remains attached to the carbon chain).
  - A second Hofmann cycle eliminates the nitrogen completely as trimethylamine ($\text{NMe}_3$), leaving an unconjugated or conjugated diene.
  - **Rule**: If complete elimination of nitrogen requires **two Hofmann cycles**, the nitrogen was part of **one ring**.
- If the nitrogen is a **bridgehead in a bicyclic ring**: Complete nitrogen extrusion requires **three successive Hofmann cycles**."""
            },
            {
                "id": "sec-8-4",
                "secNumber": "8.4",
                "title": "Structural Elucidation II: Emde Degradation, von Braun Reaction & Zinc Dust Distillation",
                "content": r"""When Hofmann elimination fails due to the absence of $\beta$-hydrogens or unfavorable anti-periplanar stereochemistry, alternative degradative tools are employed.

### The Emde Degradation (1909)
Emde discovered that quaternary ammonium halides that fail to undergo Hofmann elimination can be cleaved by nascent hydrogen reduction:
$$\text{R}_4\text{N}^+\text{Cl}^- + 2\text{ [H]} \xrightarrow{\text{Na/Hg, H}_2\text{O}} \text{R-H} + \text{R}_3\text{N} + \text{NaCl}$$
Sodium amalgam ($\text{Na/Hg}$) or catalytic hydrogenation reduces a benzylic, allylic, or strained $\text{C}-\text{N}^+$ bond, breaking the ring without requiring a $\beta$-hydrogen.

### The von Braun Degradation (Cyanogen Bromide)
Tertiary amines react with cyanogen bromide ($\text{BrCN}$) to yield a cyanamide and an alkyl bromide:
$$\text{R}_3\text{N} + \text{BrCN} \to [\text{R}_3\text{N}^+-\text{CN}] \text{Br}^- \to \text{R}_2\text{N-CN} + \text{R-Br}$$
In cyclic amines, nucleophilic bromide attacks the less hindered ring carbon, opening the ring to yield an $\omega$-bromoalkyl cyanamide.

### Zinc Dust Distillation
Vigorous pyrolysis of alkaloids mixed with zinc dust at $400–500^\circ\text{C}$ strips oxygen atoms and dehydrogenates hydroaromatic ring systems into fully aromatic parent hydrocarbons:
- Pyrolysis of morphine over zinc dust yields **phenanthrene**.
- Pyrolysis of cinchonine yields **quinoline**.
- Pyrolysis of papaverine yields **isoquinoline**.
This historical method immediately identified the fundamental aromatic core of complex natural alkaloids."""
            },
            {
                "id": "sec-8-5",
                "secNumber": "8.5",
                "title": "Phenylalkylamine Alkaloids: Ephedrine — Structure, Stereochemistry & Synthesis",
                "content": r"""Ephedrine ($C_{10}H_{15}NO$) is a protoalkaloid isolated from the Chinese medicinal herb Ma Huang (*Ephedra sinica*), acting as a powerful sympathomimetic $\alpha$- and $\beta$-adrenergic receptor agonist.

### Structural Elucidation
1. **Molecular Formula and Functional Groups**:
   $C_{10}H_{15}NO$. Forms a monohydrochloride salt, reacts with nitrous acid to form an $N$-nitroso derivative (confirming a **secondary amine**, $-\text{NHMe}$), and reacts with acetyl chloride to form a diacetyl derivative ($C_{10}H_{13}NO(\text{OAc})_2$), proving the presence of **one hydroxyl group** and **one secondary amino group**.
2. **Degradation**:
   - Oxidation with alkaline potassium permanganate yields **benzoic acid ($\text{PhCOOH}$)**, proving the presence of an unsubstituted benzene ring attached to an aliphatic carbon chain.
   - Oxidation with sodium periodate ($\text{NaIO}_4$) or alkaline hypoiodite cleaves the molecule into benzaldehyde, acetaldehyde, and methylamine:
   $$\text{Ephedrine} \xrightarrow{[\text{O}]} \text{PhCHO} + \text{CH}_3\text{CHO} + \text{CH}_3\text{NH}_2$$
   This proves the carbon connectivity: **$\text{Ph}-\text{CH(OH)}-\text{CH(NHCH}_3)-\text{CH}_3$** (1-phenyl-2-(methylamino)propan-1-ol).

### Stereochemistry: Ephedrine vs Pseudoephedrine
Ephedrine possesses two chiral centers: C1 (carbinol) and C2 (amine), yielding $2^2 = 4$ stereoisomers:
- **$(-)$-Ephedrine**: Natural active isomer, $(1R, 2S)$-configuration. In Fischer projection, both the $-\text{OH}$ and $-\text{NHMe}$ groups point to the **same side** (erythro-like).
- **$(+)$-Pseudoephedrine**: Natural isomer from *Ephedra*, $(1S, 2S)$-configuration. The $-\text{OH}$ and $-\text{NHMe}$ groups point in **opposite directions** (threo-like).
- Heating $(-)$-ephedrine with $25\%\text{ HCl}$ induces epimerization at C1 via a benzylic carbocation, producing the thermodynamically more stable $(+)$-pseudoephedrine.

### Total Synthesis (Nagai Route)
Benzaldehyde condenses with nitroethane in the presence of base (Henry nitroaldol reaction):
$$\text{PhCHO} + \text{CH}_3\text{CH}_2\text{NO}_2 \xrightarrow{\text{Base}} \text{Ph}-\text{CH(OH)}-\text{CH(NO}_2)-\text{CH}_3$$
Catalytic reduction of the nitro group followed by monomethylation of the primary amine yields racemic ephedrine/pseudoephedrine, resolved with $(+)$-tartaric acid."""
            },
            {
                "id": "sec-8-6",
                "secNumber": "8.6",
                "title": "Tropane Alkaloids: Atropine, Tropine & Robinson's Biomimetic Synthesis",
                "content": r"""Atropine (racemic DL-hyoscyamine, $C_{17}H_{23}NO_3$) is an anticholinergic tropane alkaloid isolated from deadly nightshade (*Atropa belladonna*).

### Hydrolysis and Structural Proof
Hydrolysis of atropine with baryta water ($\text{Ba(OH)}_2$) or dilute acid cleaves the ester bond into two components:
$$\text{Atropine } (C_{17}H_{23}NO_3) + \text{H}_2\text{O} \to \text{Tropine } (C_8H_{15}NO) + (\pm)\text{-Tropic acid } (C_9H_{10}O_3)$$
1. **Tropic Acid**: Elucidated as 3-hydroxy-2-phenylpropanoic acid ($\text{PhCH(CH}_2\text{OH)COOH}$).
2. **Tropine**: A bicyclic amino alcohol containing a fused **8-methyl-8-azabicyclo[3.2.1]octane** (tropane) core with an endo-hydroxyl group at C3:
   - Oxidation of tropine with chromic acid yields the ketone **tropinone** ($C_8H_{13}NO$).
   - Reduction of tropinone yields tropine (endo-OH) and its stereoisomer pseudotropine (exo-OH).

### Sir Robert Robinson's Classic Biomimetic Tropinone Synthesis (1917)
Willstätter's original total synthesis of tropinone (1901) required 15 laborious steps with an overall yield of under $1\%$.
In 1917, Sir Robert Robinson achieved the landmark synthesis of organic chemistry by assembling tropinone in a **single step at room temperature in aqueous solution at physiological pH**:
$$\text{Succindialdehyde} + \text{Methylamine} + \text{Acetonedicarboxylic acid} \xrightarrow{\text{pH } 7.0, \text{ 25}^\circ\text{C}} \text{Tropinone} + 2\text{ CO}_2 + 2\text{ H}_2\text{O}$$
### Stepwise Mechanism
1. Succindialdehyde condenses with methylamine ($\text{MeNH}_2$) to form a cyclic pyrrolidine iminium cation.
2. The iminium cation undergoes Mannich nucleophilic attack by the enol of acetonedicarboxylic acid.
3. A second intramolecular condensation between the newly formed secondary amine and the remaining aldehyde closes the piperidine ring.
4. Spontaneous double $\beta$-decarboxylation of the $\beta$-keto dicarboxylic acid releases two moles of $\text{CO}_2$, furnishing **tropinone** in $>90\%$ yield."""
            },
            {
                "id": "sec-8-7",
                "secNumber": "8.7",
                "title": "Morphine & Codeine: Functional Groups, Phenanthrene Degradation & Biosynthesis",
                "content": r"""Morphine ($C_{17}H_{19}NO_3$) is the principal alkaloid of opium (*Papaver somniferum*) and the gold-standard narcotic analgesic. Codeine ($C_{18}H_{21}NO_3$) is its $O^3$-methyl ether.

### Functional Group Characterization
1. **Nitrogen Function**: Forms mono-quaternary ammonium salts and reacts with nitrous acid to yield no reaction, proving it is a **tertiary amine** bearing an $N$-methyl group ($-\text{N}-\text{CH}_3$).
2. **Oxygen Functions**:
   - Reacts with aqueous $\text{NaOH}$ to form a water-soluble sodium phenolate, proving the presence of one **phenolic hydroxyl group** at C3. (Codeine does not dissolve in $\text{NaOH}$ because its C3 hydroxyl is methylated: $-\text{OCH}_3$).
   - Acetylation with acetic anhydride gives diacetylmorphine (**heroin**, $C_{17}H_{17}NO(\text{OAc})_2$), proving two esterifiable hydroxyls: one phenolic (C3) and one **secondary allylic alcohol** (C6).
   - The third oxygen atom is unreactive toward acylating agents and base; it is an inert **ether bridge** (furan ring) between C4 and C5.

### Degradative Structural Proof
1. **Zinc Dust Distillation**:
   Pyrolysis of morphine with zinc dust affords **phenanthrene**, proving the presence of a fused phenanthrene carbon skeleton.
2. **Hofmann Degradation to Phenanthrene Derivatives**:
   Methylation of morphine to codeine followed by conversion to codeine methiodide and heating with alkali induces Hofmann elimination. The nitrogen bridge cleaves, and elimination yields **morphol (3,4-dihydroxyphenanthrene)** and **methylmorphol (4-hydroxy-3-methoxyphenanthrene)**.
This confirmed the landmark **Robinson-Gulland structure (1925)**: a fused pentacyclic framework consisting of a benzene ring (A), an ether ring (B), a cyclohexenyl ring (C), a piperidine ring (D), and an ethanamine bridge.

### Biosynthesis from L-Tyrosine
Morphine is biosynthesized via stereoselective condensation of dopamine and 4-hydroxyphenylacetaldehyde to form $(S)$-norcoclaurine, which converts to $(S)$-reticuline. Inversion of configuration yields $(R)$-reticuline, which undergoes phenol-oxidative coupling catalyzed by the cytochrome P450 enzyme salutaridine synthase, forming the morphinan skeleton without carbon skeleton rearrangement."""
            }
        ],
        "problems": [
            {
                "id": "prob-8-1",
                "problemNumber": "8.1",
                "title": "Hofmann Exhaustive Methylation Stepwise Cleavage of Coniine",
                "statement": r"""Coniine ($C_8H_{17}N$) is the toxic alkaloid of hemlock (*Conium maculatum*) responsible for the death of Socrates.
(a) Coniine is treated with excess methyl iodide to form a quaternary ammonium salt, which is stirred with moist $\text{Ag}_2\text{O}$ and pyrolyzed at $120^\circ\text{C}$ (First Hofmann cycle). The product is an unsaturated tertiary amine ($C_{10}H_{21}N$, dimethylconhydrine).
(b) Dimethylconhydrine is subjected to a second Hofmann cycle, yielding trimethylamine ($\text{NMe}_3$) and a branched, unconjugated octadiene ($C_8H_{14}$, conylene).
(c) Write down the complete chemical structures and curved-arrow mechanisms for each step, and explain why coniine is deduced to be 2-propylpiperidine.""",
                "hints": [
                    r"Coniine is a secondary amine.",
                    r"First quaternization adds two methyl groups to form a quaternary salt with -N+(Me)2.",
                    r"Hofmann elimination abstracts the least hindered beta-proton.",
                    r"Second cycle expels NMe3 completely."
                ],
                "solution": r"""### Step 1: First Hofmann Elimination Cycle
1. **Quaternization**:
   Coniine is a secondary amine: $\text{R}_2\text{NH}$. Reaction with 2 equivalents of $\text{CH}_3\text{I}$ gives the quaternary ammonium iodide:
   $$\text{Coniine} + 2\text{ CH}_3\text{I} \xrightarrow{\text{K}_2\text{CO}_3} \text{Coniine dimethiodide } [\text{C}_8\text{H}_{16}\text{N}^+(\text{CH}_3)_2] \text{I}^-$$
2. **Silver Oxide Treatment**:
   Stirring with moist $\text{Ag}_2\text{O}$ precipitates $\text{AgI}$, forming the quaternary hydroxide.
3. **Pyrolysis (E2 Elimination)**:
   The piperidine ring has two $\beta$-carbons relative to nitrogen: C3 (carrying the propyl group) and C5.
   Hydroxide abstracts a $\beta$-proton from C6/C5, cleaving the $\text{C}2-\text{N}$ or $\text{C}6-\text{N}$ bond:
   - Cleavage of the $\text{C}6-\text{N}$ bond yields an open-chain unsaturated tertiary amine:
     $$\mathbf{CH_2=CH-CH_2-CH_2-CH(Pr)-N(CH_3)_2 \quad (\text{Dimethylconhydrine}, C_{10}H_{21}N)}$$

### Step 2: Second Hofmann Elimination Cycle
1. **Quaternization**:
   Dimethylconhydrine reacts with 1 equivalent of $\text{CH}_3\text{I}$ to form the trimethylammonium iodide:
   $$\to [\text{CH}_2=\text{CH}-\text{CH}_2-\text{CH}_2-\text{CH}(\text{Pr})-\text{N}^+(\text{CH}_3)_3] \text{I}^-$$
2. **Thermal Elimination**:
   Pyrolysis of the hydroxide abstracts the $\beta$-proton from the propyl-bearing carbon (C4):
   $$\to \text{CH}_2=\text{CH}-\text{CH}_2-\text{CH}=\text{CH}-\text{CH}_2-\text{CH}_2-\text{CH}_3 + \mathbf{N(CH_3)_3 \quad (\text{Trimethylamine})}$$
   The resulting hydrocarbon is **octa-1,4-diene (conylene)**, $C_8H_{14}$.

### Step 3: Structural Deduction
- Total carbons = 8.
- Exactly **two Hofmann cycles** were required to liberate nitrogen as $\text{NMe}_3$. This proves that the nitrogen was originally embedded in a **single saturated ring**.
- The isolation of octa-1,4-diene proves that the ring was a 6-membered **piperidine ring** bearing a **propyl group** at C2: **2-propylpiperidine**."""
            },
            {
                "id": "prob-8-2",
                "problemNumber": "8.2",
                "title": "Emde Reduction Mechanism on Hofmann-Resistant Quaternary Salts",
                "statement": r"""When 1,1,2-trimethyl-1,2,3,4-tetrahydroisoquinolinium iodide is subjected to classical thermal Hofmann degradation, it fails to eliminate because it lacks an anti-periplanar $\beta$-hydrogen that can be abstracted without destroying the aromaticity of the fused benzene ring.
(a) Explain why the presence of the aromatic ring blocks the normal E2 pathway.
(b) When this salt is treated with sodium amalgam ($\text{Na/Hg}$) in aqueous alcohol (the Emde reduction), the heterocyclic ring cleaves cleanly to give an open-chain tertiary amine. Provide the electron-transfer mechanism for this reductive cleavage.""",
                "hints": [
                    r"The beta-hydrogens are either aromatic protons (cannot be eliminated) or constrained by ring geometry.",
                    r"Sodium amalgam is a source of single electrons (dissolving metal reduction).",
                    r"A benzylic C-N bond is cleaved because the resulting benzylic radical/carbanion is resonance stabilized."
                ],
                "solution": r"""### Step 1: Failure of Classical Hofmann Elimination
In 1,2,3,4-tetrahydroisoquinoline derivatives:
- The nitrogen is bonded to C1 (a benzylic carbon) and C3.
- The $\beta$-carbons to nitrogen are:
  1. The aromatic ring carbon C9: It has no $\beta$-hydrogen; abstracting a proton would break benzene aromaticity.
  2. Carbon C4 (benzylic $\text{CH}_2$): In the rigid fused bicyclic geometry, the $\text{C}4-\text{H}$ bond cannot achieve an anti-periplanar dihedral angle ($180^\circ$) relative to the $\text{C}3-\text{N}^+$ bond.
- Thermal heating results only in nucleophilic demethylation (re-forming methyl iodide and the tertiary amine) rather than ring cleavage.

### Step 2: Mechanism of the Emde Reduction
The Emde reduction proceeds via single-electron transfer (SET) from sodium amalgam:
1. **First Electron Transfer**:
   A single electron is transferred from sodium to the lowest unoccupied molecular orbital (LUMO, $\sigma^*_{\text{C-N}}$) of the quaternary ammonium cation:
   $$[\text{R}_3\text{N}^+-\text{CH}_2\text{Ar}] + e^- \to [\text{R}_3\text{N}\cdots\text{CH}_2\text{Ar}]^{\bullet}$$
2. **Selective Bond Cleavage**:
   The benzylic $\text{C}1-\text{N}^+$ bond cleaves preferentially because the departing benzyl fragment forms a resonance-stabilized neutral benzyl radical:
   $$\to \text{R}_3\text{N} + \text{Ar}-\text{CH}_2^{\bullet}$$
3. **Second Electron Transfer and Protonation**:
   The benzyl radical accepts a second electron to form a benzylic carbanion:
   $$\text{Ar}-\text{CH}_2^{\bullet} + e^- \to \text{Ar}-\text{CH}_2^-$$
   Protonation by water yields the cleaved hydrocarbon:
   $$\text{Ar}-\text{CH}_2^- + \text{H}_2\text{O} \to \text{Ar}-\text{CH}_3 + \text{OH}^-$$
The heterocyclic ring is cleaved, affording **2-(2-methylaminoethyl)toluene** in high yield."""
            },
            {
                "id": "prob-8-3",
                "problemNumber": "8.3",
                "title": "Periodate and Alkaline Degradation Stoichiometry of Ephedrine",
                "statement": r"""A pure sample of $(-)$-ephedrine ($1.652\text{ g}$, $10.0\text{ mmol}$) was treated with sodium periodate ($\text{NaIO}_4$) in aqueous buffer at room temperature.
(a) Write the balanced chemical equation and calculate the theoretical mass of benzaldehyde ($M = 106.12\text{ g/mol}$) formed.
(b) Explain why $(-)$-ephedrine reacts rapidly with periodate, whereas $(+)$-pseudoephedrine reacts at a distinctly different kinetic rate. Relate this to the five-membered cyclic periodate diester intermediate.""",
                "hints": [
                    r"Ephedrine is a 1,2-amino alcohol: Ph-CH(OH)-CH(NHMe)-Me.",
                    r"Periodate cleaves 1,2-amino alcohols similarly to 1,2-diols.",
                    r"The erythro isomer can adopt a conformation with syn-periplanar OH and NHR groups with less steric clash than the threo isomer."
                ],
                "solution": r"""### Step 1: Balanced Cleavage Equation and Benzaldehyde Yield
Periodate oxidatively cleaves 1,2-amino alcohols:
$$\text{PhCH(OH)-CH(NHMe)-CH}_3 + \text{NaIO}_4 \to \text{PhCHO} + \text{CH}_3\text{CHO} + \text{CH}_3\text{NH}_2 + \text{NaIO}_3$$
1. **Stoichiometric Ratio**:
   $1.0\text{ mole ephedrine} \implies 1.0\text{ mole benzaldehyde}$.
   $$n_{\text{PhCHO}} = 10.0\text{ mmol} = 0.0100\text{ mol}$$
2. **Mass of Benzaldehyde**:
   $$m_{\text{PhCHO}} = 0.0100\text{ mol} \times 106.12\text{ g/mol} = 1.061\text{ g} = \mathbf{1.06\text{ g}}$$

### Step 2: Kinetic Discrimination (Ephedrine vs Pseudoephedrine)
1. **Cyclic Intermediate Requirement**:
   Periodate oxidation requires the formation of a five-membered cyclic periodate diester-monoamide transition state bridging the oxygen and nitrogen atoms:
   $$\text{C}-\text{O}\cdots\text{I}\cdots\text{N}-\text{C}$$
   For cyclic coordination, the $-\text{OH}$ and $-\text{NHMe}$ groups must adopt a **gauche (syn-clinal) conformation** with a dihedral angle near $0–60^\circ$.
2. **Conformational Steric Analysis**:
   - In $(-)$-ephedrine ($(1R, 2S)$, erythro configuration): when the $-\text{OH}$ and $-\text{NHMe}$ groups are positioned gauche for chelation, the bulky phenyl ($\text{Ph}$) and methyl ($\text{Me}$) groups orient anti to each other, minimizing steric strain. Chelation is facile, resulting in **rapid oxidation kinetics**.
   - In $(+)$-pseudoephedrine ($(1S, 2S)$, threo configuration): bringing the $-\text{OH}$ and $-\text{NHMe}$ groups into the gauche chelation geometry forces the bulky phenyl and methyl groups into an eclipsed/gauche steric clash. This raises $\Delta G^\ddagger$, making periodate cleavage of pseudoephedrine significantly slower."""
            },
            {
                "id": "prob-8-4",
                "problemNumber": "8.4",
                "title": "Robinson Tropinone Biomimetic Synthesis: Retrosynthesis and Atom Economy",
                "statement": r"""In 1917, Sir Robert Robinson reported the one-pot synthesis of tropinone from succindialdehyde, methylamine, and acetonedicarboxylic acid.
(a) Perform a formal retrosynthetic disconnection on tropinone, demonstrating how two successive Mannich-type disconnections reveal the three starting materials.
(b) Calculate the theoretical atom economy ($AE\%$) for the reaction:
$$\text{C}_4\text{H}_6\text{O}_2 + \text{CH}_5\text{N} + \text{C}_5\text{H}_6\text{O}_5 \to \text{C}_8\text{H}_{13}\text{NO} + 2\text{ CO}_2 + 2\text{ H}_2\text{O}$$
Given molar masses: Succindialdehyde = $86.09$, Methylamine = $31.06$, Acetonedicarboxylic acid = $146.10$, Tropinone = $139.19\text{ g/mol}$.""",
                "hints": [
                    r"Tropinone has a C=O flanked by two CH2 groups that can be disconnected as an acetone equivalent.",
                    r"Atom economy = (Molar mass of desired product / Sum of molar masses of all reactants) * 100%."
                ],
                "solution": r"""### Step 1: Retrosynthetic Analysis
1. **First Disconnection**:
   Disconnect the C2-C3 bond of tropinone (a $\beta$-aminoketone):
   - Retro-Mannich reveals a nucleophilic enol donor ($-\text{CH}_2-\text{CO}-\text{CH}_2-$) and an electrophilic iminium ion.
2. **Second Disconnection**:
   Disconnect the C4-C5 bond (the second $\beta$-aminoketone linkage):
   - Retro-Mannich reveals the second enol addition site.
3. **Precursor Identification**:
   - The central four-carbon fragment ($C_1, C_7, C_6, C_5$) is **succindialdehyde ($\text{OHC-CH}_2\text{-CH}_2\text{-CHO}$)**.
   - The nitrogen atom originates from **methylamine ($\text{MeNH}_2$)**.
   - The acetone synthon is supplied by **acetonedicarboxylic acid ($\text{HOOC-CH}_2\text{-CO-CH}_2\text{-COOH}$)**, where the $\beta$-carboxylic acid groups enhance enolization at physiological pH and spontaneously decarboxylate upon ring formation.

### Step 2: Atom Economy Calculation
1. **Molecular Mass of Reactants**:
   $$M_{\text{reactants}} = M_{\text{succindialdehyde}} + M_{\text{methylamine}} + M_{\text{acetonedicarboxylic acid}}$$
   $$M_{\text{reactants}} = 86.09 + 31.06 + 146.10 = 263.25\text{ g/mol}$$
2. **Molecular Mass of Product (Tropinone)**:
   $$M_{\text{tropinone}} = 139.19\text{ g/mol}$$
3. **Atom Economy ($AE\%$)**:
   $$AE\% = \frac{M_{\text{desired}}}{M_{\text{reactants}}} \times 100\% = \frac{139.19}{263.25} \times 100\% = \mathbf{52.87\%}$$
The remaining $47.13\%$ of mass is lost as environmentally benign, non-toxic byproducts: $2\text{ CO}_2$ ($88.02\text{ g/mol}$) and $2\text{ H}_2\text{O}$ ($36.03\text{ g/mol}$), making this one of the most elegant green, biomimetic transformations in total synthesis history."""
            },
            {
                "id": "prob-8-5",
                "problemNumber": "8.5",
                "title": "Morphine Dehydration to Apomorphine and Phenanthrene Core Formation",
                "statement": r"""When morphine is heated with concentrated hydrochloric acid at $140^\circ\text{C}$ in a sealed tube, it undergoes a deep skeletal rearrangement accompanied by dehydration, affording **apomorphine** ($C_{17}H_{17}NO_2$), a potent dopamine $D_2$ receptor agonist.
(a) Provide the curved-arrow mechanism for the conversion of morphine to apomorphine, identifying the carbocation intermediate, the 1,2-shift, and the cleavage of the furan-ether bridge.
(b) Explain why zinc dust distillation of either morphine or apomorphine yields **phenanthrene** rather than anthracene.""",
                "hints": [
                    r"Protonation of the C6-OH initiates loss of water, forming an allylic carbocation.",
                    r"Wagner-Meerwein rearrangement shifts the quaternary carbon-carbon bond.",
                    r"The four rings A, B, C, D reorganize into a fused phenanthrene core with an attached aporphine ring."
                ],
                "solution": r"""### Step 1: Rearrangement Mechanism to Apomorphine
1. **Protonation and Allylic Ionization**:
   The secondary allylic alcohol at C6 is protonated by acid ($\text{H}^+$). Departure of water ($\text{H}_2\text{O}$) generates a resonance-stabilized allylic carbocation in ring C.
2. **Wagner-Meerwein Pinacol-Type Shift**:
   The quaternary C13 center is adjacent to the carbocation. The $\text{C}12-\text{C}13$ bond migrates to C14, accompanied by the opening of the 4,5-epoxy (furan) ether bridge:
   - Cleavage of the ether oxygen generates the second phenolic hydroxyl group at C4.
3. **Aromatization of Ring C**:
   Loss of a proton from the rearranged intermediate yields a fully aromatic catechol-type ring.
   The resulting tetracyclic product is **apomorphine** (containing an aporphine ring system with two phenolic hydroxyls at C10 and C11).

### Step 2: Phenanthrene Formation in Zinc Dust Distillation
- In morphine, the carbon skeleton consists of three fused carbocycles: ring A (benzene), ring B (cyclohexyl core), and ring C (cyclohexenyl), arranged in an angular **phenanthrene (1,2-benzophenanthrene)** topology, not a linear anthracene geometry.
- During high-temperature pyrolysis with zinc dust ($450^\circ\text{C}$):
  - Zinc acts as a vigorous deoxygenating and reducing agent, cleaving the C4-C5 ether bridge and abstracting the phenolic and alcoholic oxygens as zinc oxide ($\text{ZnO}$).
  - Dehydrogenation aromatizes rings B and C into fully conjugated aromatic rings.
  - The ethanamine bridge is thermally extruded.
- Because the carbon framework is angularly fused, the fully aromatized product is **phenanthrene** ($C_{14}H_{10}$) with zero anthracene formed."""
            },
            {
                "id": "prob-8-6",
                "problemNumber": "8.6",
                "title": "The von Braun Reaction Mechanism on N-Methylpiperidine with Cyanogen Bromide",
                "statement": r"""$N$-Methylpiperidine was treated with cyanogen bromide ($\text{BrCN}$) in dry ether at $0^\circ\text{C}$.
(a) Write the complete two-stage mechanism, showing the quaternary cyanoammonium intermediate and the subsequent nucleophilic ring opening by bromide.
(b) Identify the organic product and explain why nucleophilic bromide attack occurs at the ring methylene carbon ($\text{C}2$) rather than the exocyclic methyl group, contrasting this with open-chain tertiary amines.""",
                "hints": [
                    r"Nitrogen attacks the electrophilic carbon of BrCN to form a quaternary ammonium ion with release of Br-.",
                    r"Bromide acts as a nucleophile in an SN2 displacement.",
                    r"Compare the relief of ring strain and steric factors for ring opening vs exocyclic demethylation."
                ],
                "solution": r"""### Step 1: Stepwise Mechanism
1. **Electrophilic Cyanation (Quaternization)**:
   The lone pair of the tertiary amine nitrogen attacks the electrophilic carbon of cyanogen bromide ($\text{Br-C}\equiv\text{N}$), displacing bromide ion:
   $$\text{C}_5\text{H}_{10}\text{N-CH}_3 + \text{Br-CN} \to [\text{C}_5\text{H}_{10}\text{N}^+(\text{CH}_3)-\text{CN}] \text{Br}^-$$
   This generates an unstable quaternary cyanoammonium bromide intermediate.
2. **Nucleophilic Displacements ($S_N2$)**:
   Bromide ion ($\text{Br}^-$) attacks one of the carbon atoms attached to the quaternary nitrogen:
   - **Path A (Ring Opening)**: Bromide attacks the $\alpha$-ring carbon ($\text{C}2$), breaking the ring $\text{C}-\text{N}$ bond:
     $$\to \mathbf{Br-CH_2-CH_2-CH_2-CH_2-CH_2-N(CH_3)-CN \quad (\text{5-bromopentyl(methyl)cyanamide})}$$
   - **Path B (Demethylation)**: Bromide attacks the exocyclic methyl group, releasing methyl bromide and retaining the intact piperidine ring:
     $$\to \text{C}_5\text{H}_{10}\text{N-CN} + \text{CH}_3\text{Br}$$

### Step 2: Selectivity Analysis
- For simple acyclic tertiary amines, attack on methyl groups is preferred because methyl carbons are less sterically hindered in $S_N2$ displacements.
- However, for cyclic amines, the cyanoammonium intermediate suffers significant ring strain and steric congestion within the piperidine chair. Nucleophilic attack at the ring carbon (Path A) is accelerated by the relief of steric congestion upon ring opening.
- Depending on solvent polarity and temperature, both pathways occur, with ring opening yielding $\omega$-bromoalkyl cyanamides, which are hydrolyzed with acid to primary-secondary diamines, providing structural proof of ring connectivity."""
            },
            {
                "id": "prob-8-7",
                "problemNumber": "8.7",
                "title": "Stereochemical Epimerization Energetics of (-)-Ephedrine and (+)-Pseudoephedrine",
                "statement": r"""When $(-)$-ephedrine ($(1R, 2S)$) is refluxed in $25\%\text{ HCl}$ for 12 hours, it reaches an equilibrium mixture containing $62\%$ $(+)$-pseudoephedrine ($(1S, 2S)$) and $38\%$ $(-)$-ephedrine.
(a) Calculate the equilibrium constant $K_{\text{eq}} = [\text{pseudoephedrine}] / [\text{ephedrine}]$ and the standard free energy difference $\Delta G^\circ$ at $T = 373\text{ K}$ ($100^\circ\text{C}$).
(b) Provide the carbocation mechanism for this acid-catalyzed benzylic epimerization, and explain why the $(1S, 2S)$ pseudoephedrine diastereomer is thermodynamically more stable than the $(1R, 2S)$ ephedrine diastereomer.""",
                "hints": [
                    r"K_{eq} = 0.62 / 0.38.",
                    r"\Delta G^\circ = -RT \ln K_{eq}.",
                    r"Protonation of C1-OH followed by water loss forms a planar benzylic carbocation.",
                    r"Examine the Newman projection of the ground-state conformers."
                ],
                "solution": r"""### Step 1: Equilibrium Constant and Free Energy Difference
1. **Equilibrium Constant ($K_{\text{eq}}$)**:
   $$K_{\text{eq}} = \frac{[\text{Pseudoephedrine}]}{[\text{Ephedrine}]} = \frac{0.62}{0.38} = \mathbf{1.632}$$
2. **Standard Free Energy Difference at $373.15\text{ K}$**:
   $$\Delta G^\circ = -R T \ln K_{\text{eq}} = -(8.314\text{ J/(mol}\cdot\text{K)})(373.15\text{ K}) \ln(1.632)$$
   $$\Delta G^\circ = -3102.4 \times 0.4898 = -1519\text{ J/mol} = \mathbf{-1.52\text{ kJ/mol}}$$
Pseudoephedrine is thermodynamically favored over ephedrine by $1.52\text{ kJ/mol}$.

### Step 2: Mechanism of Epimerization
1. **Protonation and Benzylic Ionization**:
   The C1 hydroxyl group is protonated by acid: $\text{Ph-CH(OH}_2^+)\text{-CH(NHMe)-Me}$.
   Departure of water generates a resonance-stabilized **planar benzylic carbocation**:
   $$\text{Ph}-\text{CH}^+-\text{CH(NHMe)}-\text{Me}$$
2. **Re-addition of Water**:
   Water can attack the planar $sp^2$ benzylic carbocation from either face:
   - Attack from the original face regenerates $(-)$-ephedrine ($(1R, 2S)$).
   - Attack from the opposite face inverts the configuration at C1, generating $(+)$-pseudoephedrine ($(1S, 2S)$).

### Step 3: Conformational Stability Rationale
Examine the lowest-energy staggered Newman projections looking down the $\text{C}1-\text{C}2$ bond:
- In $(+)$-pseudoephedrine ($(1S, 2S)$, threo), the two largest groups—the phenyl ring at C1 and the methyl group at C2—can orient **anti** to each other while simultaneously placing the $-\text{OH}$ and $-\text{NHMe}$ groups in favorable hydrogen-bonding gauche orientations.
- In $(-)$-ephedrine ($(1R, 2S)$, erythro), placing the phenyl and methyl groups anti forces a more severe gauche steric clash between the phenyl and methylamino groups.
Consequently, $(+)$-pseudoephedrine has lower ground-state conformational enthalpy, driving the equilibrium toward $62\%$ pseudoephedrine."""
            }
        ]
    }
    units.append(u8)

    # =========================================================================
    # UNIT 9: Lipids & Steroids: Saponification, Cholesterol Architecture & Glycosides
    # =========================================================================
    u9 = {
        "id": "unit-9",
        "unitNumber": 9,
        "title": "Unit 9: Lipids & Steroids: Saponification, Cholesterol Architecture & Glycosides",
        "leadSummary": "Comprehensive physical organic, analytical, and structural chemistry of lipids and steroids: fatty acid unsaturation and trans-isomerism, saponification and iodine value analytics, lipoprotein cardiovascular transport, stereochemistry of the cyclopentanoperhydrophenanthrene (CPPP) sterane skeleton, dehydrogenation to Diels' hydrocarbon, functional group and angular methyl elucidation of cholesterol (Barbier-Wieland degradation, Blanc's rule), and cardiotonic steroidal glycosides.",
        "simulations": ["sim_nat_steroid_ring_conformation_diels"],
        "sections": [
            {
                "id": "sec-9-1",
                "secNumber": "9.1",
                "title": "Lipids: Fatty Acids, Unsaturation, Cis/Trans Isomerism & Membranes",
                "content": r"""Lipids are water-insoluble, hydrophobic or amphiphilic biomolecules soluble in non-polar organic solvents (chloroform, ether).

### Fatty Acid Structure and Unsaturation
Fatty acids are monocarboxylic acids with long unbranched hydrocarbon chains ($C_4$ to $C_{28}$):
1. **Saturated Fatty Acids**: Possess zero double bonds (e.g., palmitic acid $C_{16:0}$, stearic acid $C_{18:0}$). Chains adopt fully extended all-trans zigzag conformations that pack densely into crystal lattices, yielding high melting points ($>60^\circ\text{C}$).
2. **Unsaturated Fatty Acids**: Contain one or more double bonds:
   - **Oleic acid ($C_{18:1}, \Delta^9$, cis)**: A single cis-double bond introduces a rigid $30^\circ$ kink into the hydrocarbon chain, disrupting dense van der Waals packing and dramatically depressing the melting point to $+13^\circ\text{C}$ (liquid oil at room temperature).
   - **Polyunsaturated Fatty Acids (PUFAs)**: E.g., Linoleic acid ($C_{18:2}, \Delta^{9,12}$, omega-6) and $\alpha$-linolenic acid ($C_{18:3}, \Delta^{9,12,15}$, omega-3). Double bonds in natural PUFAs are strictly separated by a non-conjugated methylene bridge ($-\text{CH}=\text{CH}-\text{CH}_2-\text{CH}=\text{CH}-$, 'methylene-interrupted dienes').
3. **Trans Fatty Acids**: Formed by partial catalytic hydrogenation of vegetable oils (e.g., elaidic acid, trans-$\Delta^9-C_{18:1}$). Trans double bonds maintain an extended, linear zigzag shape resembling saturated fats, raising melting points, packing into rigid membrane domains, and increasing cardiovascular disease risk by elevating LDL while depressing HDL."""
            },
            {
                "id": "sec-9-2",
                "secNumber": "9.2",
                "title": "Chemical Analysis of Fats and Oils: Saponification, Iodine & Acid Values",
                "content": r"""Standard chemical titrations characterize the purity, chain length, unsaturation level, and free fatty acid content of industrial and edible fats.

### 1. Saponification Value ($SV$)
The mass of potassium hydroxide (in milligrams) required to saponify completely one gram of fat or oil:
$$SV = \frac{3 \times 56,106\text{ mg/mol}}{M_{\text{TAG}}} = \frac{168,318}{M_{\text{TAG}}}$$
Because three moles of $\text{KOH}$ ($M = 56.11\text{ g/mol}$) are consumed per mole of triacylglycerol (TAG):
- $SV$ is **inversely proportional** to the average molecular weight ($M_{\text{TAG}}$) and average fatty acyl chain length.
- Coconut oil (rich in short-chain lauric acid $C_{12:0}$) has a high $SV \approx 250 - 260\text{ mg KOH/g}$.
- Olive oil (rich in long-chain oleic acid $C_{18:1}$) has a lower $SV \approx 190 - 195\text{ mg KOH/g}$.

### 2. Iodine Value ($IV$)
The mass of iodine (in grams) consumed by 100 grams of fat or oil:
- Measures the **degree of unsaturation**.
- Quantified via the **Hanus method** (iodine monobromide, $IBr$) or **Wijs method** (iodine monochloride, $ICl$):
  $$-\text{CH}=\text{CH}- + \text{ICl} \to -\text{CH(I)}-\text{CH(Cl)}-$$
  Unreacted $ICl$ oxidizes iodide to free iodine, which is back-titrated with standardized sodium thiosulfate ($\text{Na}_2\text{S}_2\text{O}_3$).
- Saturated fats (butter, coconut oil) exhibit low $IV < 35$.
- Drying oils (linseed oil, rich in linolenic acid) exhibit high $IV > 170$, undergoing oxidative crosslinking upon exposure to air.

### 3. Acid Value ($AV$) and Ester Value ($EV$)
- **Acid Value ($AV$)**: Milligrams of $\text{KOH}$ needed to neutralize free fatty acids in 1 gram of fat (measures hydrolytic rancidity).
- **Ester Value ($EV$)**: $EV = SV - AV$, measuring the saponifiable ester bonds."""
            },
            {
                "id": "sec-9-3",
                "secNumber": "9.3",
                "title": "Lipoproteins & Cardiovascular Transport: Chylomicrons, LDL, HDL & Plaque Dynamics",
                "content": r"""Because hydrophobic lipids (triacylglycerols, cholesteryl esters) cannot dissolve in aqueous bloodstream, they are packaged into macromolecular spherical assemblies termed **lipoproteins**.

### Structural Architecture of Lipoproteins
A spherical core of hydrophobic lipids (triacylglycerols and cholesteryl esters) surrounded by an amphipathic monolayer of phospholipids, unesterified cholesterol, and specialized proteins called **apolipoproteins** (e.g., ApoB-100, ApoA-I) that target cell-surface receptors.

### Major Classes and Density Hierarchy
1. **Chylomicrons**: Largest ($75–1200\text{ nm}$), lowest density ($\rho < 0.95\text{ g/mL}$), assembled in enterocytes to transport dietary lipids from the intestine via lymph into circulation.
2. **Very Low-Density Lipoproteins (VLDL)**: Synthesized in the liver to export endogenous triacylglycerols to peripheral tissues.
3. **Low-Density Lipoproteins (LDL, 'Bad Cholesterol')**: Density $1.019–1.063\text{ g/mL}$, rich in cholesteryl esters. Transports cholesterol to peripheral tissues via receptor-mediated endocytosis (LDL receptor recognizes ApoB-100). Excess circulating LDL penetrates arterial endothelial walls, undergoes oxidative modification (oxLDL), is engulfed by macrophages to form foam cells, and initiates atherosclerotic plaque formation.
4. **High-Density Lipoproteins (HDL, 'Good Cholesterol')**: Smallest ($5–12\text{ nm}$), highest density ($\rho = 1.063–1.210\text{ g/mL}$), containing ApoA-I. Mediates **reverse cholesterol transport**, scavenging excess cholesterol from peripheral arterial walls and returning it to the liver for excretion as bile acids."""
            },
            {
                "id": "sec-9-4",
                "secNumber": "9.4",
                "title": "Steroids: The Cyclopentanoperhydrophenanthrene Framework & Diels' Hydrocarbon",
                "content": r"""Steroids are modified triterpenoids characterized by a tetracyclic carbon framework: the **cyclopentanoperhydrophenanthrene (CPPP)** ring system, also designated the **sterane** nucleus.

### Ring Nomenclature and Stereochemistry
The four fused rings are designated **A**, **B**, **C**, and **D**:
- Rings A, B, and C form a perhydrophenanthrene (three fused cyclohexanes).
- Ring D is a five-membered cyclopentane ring.
- Carbons are numbered 1 to 17 on the ring framework, with angular methyl groups at C10 (C19) and C13 (C18), and an aliphatic side chain at C17 (carbons 20 to 27 in cholesterol).
- **Ring Fusions**:
  - In naturally occurring cholesterol and bile acids, the B/C and C/D ring junctions are **trans-fused**, establishing a rigid, planar conformational core.
  - The A/B ring fusion can be either **trans** (as in $5\alpha$-cholestanol, where the A/B junction is trans-fused and rings A and B adopt extended chair-chair conformations) or **cis** (as in $5\beta$-coprostanol, where ring A folds downward at a $90^\circ$ angle relative to ring B).

### Dehydrogenation to Diels' Hydrocarbon (1927)
Otto Diels discovered that heating cholesterol or other steroids with selenium metal at $320–360^\circ\text{C}$ induces dehydrogenation, aromatization, and cleavage of angular methyl groups, yielding a characteristic aromatic hydrocarbon:
$$\text{Cholesterol} \xrightarrow{\text{Se}, 360^\circ\text{C}} \mathbf{C_{18}H_{16} \quad (\text{Diels' Hydrocarbon})}$$
Diels' hydrocarbon was elucidated by total synthesis as **3'-methyl-1,2-cyclopentenophenanthrene**. The isolation of Diels' hydrocarbon provided the first definitive chemical proof that all steroids share the identical fused cyclopentanophenanthrene carbon skeleton."""
            },
            {
                "id": "sec-9-5",
                "secNumber": "9.5",
                "title": "Cholesterol I: Functional Groups ($3\\beta$-OH, 5,6-Double Bond & $C_{17}$ Octyl Side Chain)",
                "content": r"""Cholesterol ($C_{27}H_{46}O$) is the prototype animal sterol, isolated from gallstones by Poulletier de la Salle in 1769.

### Stepwise Elucidation of Functional Groups
1. **Molecular Formula and Rings**:
   Elemental analysis and HRMS establish $C_{27}H_{46}O$.
   $$\text{IHD} = 27 + 1 - \frac{46}{2} = 5$$
   Complete catalytic hydrogenation yields the saturated alcohol cholestanol ($C_{27}H_{48}O$, $\text{IHD} = 4$). Because the fully saturated alcohol has 4 degrees of unsaturation, **cholesterol possesses four fused rings and one double bond**.
2. **The Hydroxyl Group ($3\beta$-OH)**:
   - Forms a monoacetate ($C_{27}H_{45}OAc$) with acetic anhydride and a monobenzoate with benzoyl chloride, confirming a **single secondary alcohol**.
   - Oxidation with chromic acid ($\text{CrO}_3$) converts cholesterol into the $\alpha,\beta$-unsaturated ketone **cholestenone** ($C_{27}H_{44}O$), proving that the hydroxyl group resides on a secondary carbon and is allylic to the double bond.
   - Cholesterol forms an insoluble crystalline precipitate with digitonin (a steroidal saponin), a specific reaction requiring a **$3\beta$-hydroxyl group** (trans to the angular methyl at C10).
3. **The Carbon-Carbon Double Bond ($\Delta^5$)**:
   - Cholesterol adds one molar equivalent of bromine ($\text{Br}_2$) to form crystalline cholesterol dibromide ($C_{27}H_{46}O\text{Br}_2$), which can be smoothly debrominated back to cholesterol with zinc dust.
   - Ozonolysis or peracid cleavage locates the double bond between **C5 and C6**.
4. **The $C_{17}$ Aliphatic Side Chain**:
   Vigorous oxidation of cholestane (the fully saturated parent hydrocarbon) with chromic acid cleaves the side chain, yielding **acetone** ($C_3$) and **6-methylheptan-2-one** ($C_8$). This proves that the side chain attached at C17 is the 8-carbon branched group **$-\text{CH(CH}_3)\text{-CH}_2\text{-CH}_2\text{-CH}_2\text{-CH(CH}_3)_2$**."""
            },
            {
                "id": "sec-9-6",
                "secNumber": "9.6",
                "title": "Cholesterol II: Angular Methyls, Barbier-Wieland Degradation & Blanc's Rule",
                "content": r"""Determining the position of angular methyl groups and ring sizes in the steroid skeleton required precision chemical degradation by Adolf Windaus and Heinrich Wieland (Nobel Prizes in Chemistry, 1927 and 1928).

### The Barbier-Wieland Degradation
A classical stepwise chemical procedure that shortens a carboxylic acid chain by **exactly one carbon atom** at a time:
1. An ester of the bile acid or steroid side chain is treated with excess phenylmagnesium bromide ($\text{PhMgBr}$):
   $$\text{R-CH}_2\text{-COOMe} + 2\text{ PhMgBr} \to \text{R-CH}_2\text{-C(OH)Ph}_2$$
2. Dehydration with acetic anhydride or acid yields a 1,1-diphenylethylene derivative:
   $$\text{R-CH}_2\text{-C(OH)Ph}_2 \xrightarrow{-\text{H}_2\text{O}} \text{R-CH}=\text{CPh}_2$$
3. Oxidative cleavage of the double bond with chromic acid ($\text{CrO}_3$) cleaves the olefin, releasing benzophenone ($\text{Ph}_2\text{CO}$) and yielding the shortened carboxylic acid:
   $$\text{R-CH}=\text{CPh}_2 \xrightarrow{\text{CrO}_3} \text{R-COOH} + \text{Ph}_2\text{C}=\text{O}$$
By repeating this sequence three successive times on cholanic acid derivatives, the side chain was systematically shortened until further reaction yielded a ketone instead of a carboxylic acid, proving that the side chain was attached to a **secondary/tertiary ring carbon (C17)**.

### Blanc's Rule and Ring Size Determination
Blanc's Rule states that when a dicarboxylic acid is heated with acetic anhydride:
- **1,4- and 1,5-Dicarboxylic acids** (succinic and glutaric acids) undergo dehydrative cyclization to form stable **cyclic anhydrides** without loss of $\text{CO}_2$.
- **1,6- and 1,7-Dicarboxylic acids** (adipic and pimelic acids) undergo decarboxylative cyclization to form stable **cyclic ketones** with loss of $\text{CO}_2$.
When bile acid rings were oxidatively opened to dicarboxylic acids and pyrolyzed:
- Cleavage of rings A, B, and C yielded cyclic ketones with loss of $\text{CO}_2$, proving that **rings A, B, and C are six-membered rings**.
- Cleavage of ring D yielded a cyclic anhydride without loss of $\text{CO}_2$, proving that **ring D is a five-membered cyclopentane ring**."""
            },
            {
                "id": "sec-9-7",
                "secNumber": "9.7",
                "title": "Steroidal Glycosides: Cardiotonic Steroids & Steroidal Saponins",
                "content": r"""Steroidal glycosides consist of a steroid aglycone (genin) covalently linked through its $3\beta$-hydroxyl group to one or more specialized carbohydrate moieties.

### Cardiotonic Glycosides (Cardiac Glycosides)
Used for centuries in the treatment of congestive heart failure and cardiac arrhythmias (e.g., extracts of *Digitalis purpurea*, purple foxglove):
1. **Structural Features of the Aglycone**:
   - Stereochemistry: Fused rings A/B and C/D are **cis-fused** (giving a characteristic U-shaped conformation), while B/C is trans-fused.
   - Hydroxyl groups: Possesses a $3\beta$-hydroxyl group and a critical **$14\beta$-hydroxyl group**.
   - Unsaturated Lactone at C17:
     - **Cardenolides** (plant origin, e.g., digitoxigenin, digoxin): Possess a five-membered $\alpha,\beta$-unsaturated $\gamma$-lactone ring (butenolide) at $C17\beta$. Gives a positive **Legal's test** (red-orange with sodium nitroprusside in alkaline pyridine).
     - **Bufadienolides** (amphibian origin, e.g., bufalin from toad venom): Possess a six-membered doubly unsaturated $\alpha$-pyrone ring at $C17\beta$.
2. **Mechanism of Action**:
   Cardiotonic steroids specifically bind and inhibit the extracellular face of the **$\text{Na}^+/\text{K}^+$-ATPase** sodium pump in cardiac myocytes. Inhibition elevates intracellular $[\text{Na}^+]$, which slows the $\text{Na}^+/\text{Ca}^{2+}$ exchanger (NCX), driving an accumulation of intracellular $[\text{Ca}^{2+}]$ that enhances myocardial contractile force (positive inotropic effect).

### Steroidal Saponins (Diosgenin)
Steroidal saponins form stable soap-like foams in water. Their aglycones (spirostanes, e.g., **diosgenin** from wild yams, *Dioscorea*) contain fused heterocyclic ketal rings E and F attached to C16 and C17. Diosgenin serves as the vital industrial starting material for the Marker degradation, enabling the multi-ton commercial synthesis of progesterone, testosterone, and corticosteroid anti-inflammatory drugs."""
            }
        ],
        "problems": [
            {
                "id": "prob-9-1",
                "problemNumber": "9.1",
                "title": "Saponification Value and Molecular Weight Calculation of Triacylglycerols",
                "statement": r"""A $2.000\text{ g}$ sample of a pure synthetic triacylglycerol (TAG) was completely saponified with $50.00\text{ mL}$ of $0.5000\text{ M}$ ethanolic $\text{KOH}$. The unreacted alkali required $28.40\text{ mL}$ of $0.5000\text{ M HCl}$ for complete neutralization in a phenolphthalein back-titration. A blank titration without fat required $49.80\text{ mL}$ of $0.5000\text{ M HCl}$.
(a) Calculate the Saponification Value ($SV$) of the triacylglycerol in $\text{mg KOH/g}$.
(b) Determine the average molecular weight ($M_{\text{TAG}}$) of the triacylglycerol.
(c) If the fat is a simple triglyceride (all three fatty acyl chains are identical saturated acids), identify the fatty acid.""",
                "hints": [
                    r"SV = [56.11 * (V_blank - V_sample) * M_HCl] / mass_sample in grams.",
                    r"M_TAG = (3 * 56,106) / SV.",
                    r"M_TAG = M_glycerol_backbone + 3 * M_fatty_acyl."
                ],
                "solution": r"""### Step 1: Saponification Value ($SV$) Calculation
The volume difference of standard acid is:
$$\Delta V = V_{\text{blank}} - V_{\text{sample}} = 49.80\text{ mL} - 28.40\text{ mL} = 21.40\text{ mL}$$
The moles of $\text{KOH}$ consumed by the $2.000\text{ g}$ fat sample:
$$n_{\text{KOH}} = 21.40\times 10^{-3}\text{ L} \times 0.5000\text{ mol/L} = 0.01070\text{ mol}$$
Mass of $\text{KOH}$ consumed ($M_{\text{KOH}} = 56.106\text{ g/mol}$):
$$m_{\text{KOH}} = 0.01070\text{ mol} \times 56,106\text{ mg/mol} = 600.33\text{ mg}$$
The Saponification Value per gram of fat:
$$SV = \frac{600.33\text{ mg}}{2.000\text{ g}} = \mathbf{300.2\text{ mg KOH/g}}$$

### Step 2: Molecular Weight of the Triacylglycerol
Because 3 moles of $\text{KOH}$ saponify 1 mole of triacylglycerol:
$$M_{\text{TAG}} = \frac{3 \times 56,106\text{ mg/mol}}{SV} = \frac{168,318}{300.2} = \mathbf{560.7\text{ g/mol}}$$

### Step 3: Identification of the Fatty Acid
A triacylglycerol consists of glycerol condensed with three fatty acids:
$$\text{TAG} = \text{C}_3\text{H}_5(\text{OOCR})_3 \implies M_{\text{TAG}} = M(\text{C}_3\text{H}_5) + 3 \times M(\text{RCOO})$$
$$M(\text{C}_3\text{H}_5) = 3(12.011) + 5(1.008) = 41.07\text{ g/mol}$$
Total mass of the three fatty acyl carboxylate groups:
$$3 \times M(\text{RCOO}) = 560.7 - 41.07 = 519.63\text{ g/mol}$$
$$M(\text{RCOO}) = \frac{519.63}{3} = 173.21\text{ g/mol}$$
For a saturated fatty acid, $\text{R} = C_n H_{2n+1}$:
$$\text{RCOO} = \text{C}_n\text{H}_{2n+1}\text{COO} \implies 12.011 n + 1.008(2n+1) + 12.011 + 32.00 = 173.21$$
$$14.027 n + 45.02 = 173.21 \implies 14.027 n = 128.19$$
$$n = \frac{128.19}{14.027} = 9.14 \approx 9$$
Total carbons in the fatty acid = $n + 1 = 9 + 1 = \mathbf{10\text{ carbons}}$.
The fatty acid is **capric acid (decanoic acid, $C_{10:0}$)**, and the triacylglycerol is **tricaprin (glyceryl tridecanoate)** ($M = 554.8\text{ g/mol}$)."""
            },
            {
                "id": "prob-9-2",
                "problemNumber": "9.2",
                "title": "Hanus/Wijs Iodine Value Titration Calculus for Polyunsaturated Fatty Acids",
                "statement": r"""A $0.2500\text{ g}$ sample of pure linseed oil was dissolved in $20\text{ mL}$ of chloroform, treated with $25.00\text{ mL}$ of Wijs iodine monochloride ($ICl$) solution, and allowed to stand in the dark for 30 minutes. Potassium iodide solution ($20\text{ mL of } 10\%$) was added, and the liberated iodine was titrated with $0.1000\text{ M Na}_2\text{S}_2\text{O}_3$, requiring $14.20\text{ mL}$ to reach the starch end point. A blank titration without oil required $48.60\text{ mL}$ of $0.1000\text{ M Na}_2\text{S}_2\text{O}_3$.
(a) Calculate the Iodine Value ($IV$) of the linseed oil in $\text{g I}_2 / 100\text{ g fat}$.
(b) Assuming the linseed oil triacylglycerol has an average molecular weight of $M = 878\text{ g/mol}$, calculate the average number of carbon-carbon double bonds ($\overline{n}_{\text{db}}$) per triacylglycerol molecule.""",
                "hints": [
                    r"IV = [12.69 * (V_blank - V_sample) * M_thiosulfate] / mass_sample in grams.",
                    r"Each double bond consumes 1 mole of I2 = 253.8 g/mol.",
                    r"\overline{n}_{db} = (IV * M_TAG) / (100 * 253.8)."
                ],
                "solution": r"""### Step 1: Iodine Value Calculation
The volume of thiosulfate equivalent to the iodine consumed:
$$\Delta V = V_{\text{blank}} - V_{\text{sample}} = 48.60\text{ mL} - 14.20\text{ mL} = 34.40\text{ mL}$$
The moles of thiosulfate consumed:
$$n_{\text{thio}} = 34.40\times 10^{-3}\text{ L} \times 0.1000\text{ mol/L} = 3.440\times 10^{-3}\text{ mol}$$
Because $1\text{ mole of } \text{I}_2$ reacts with $2\text{ moles of } \text{S}_2\text{O}_3^{2-}$:
$$n_{\text{I}_2} = \frac{n_{\text{thio}}}{2} = \frac{3.440\times 10^{-3}}{2} = 1.720\times 10^{-3}\text{ mol}$$
Mass of iodine absorbed ($M_{\text{I}_2} = 253.81\text{ g/mol}$):
$$m_{\text{I}_2} = (1.720\times 10^{-3}\text{ mol}) \times 253.81\text{ g/mol} = 0.43655\text{ g}$$
The Iodine Value ($IV$) per $100\text{ g}$ of oil:
$$IV = \frac{0.43655\text{ g }\text{I}_2}{0.2500\text{ g fat}} \times 100 = \mathbf{174.6\text{ g I}_2 / 100\text{ g oil}}$$

### Step 2: Average Number of Double Bonds ($\overline{n}_{\text{db}}$)
In $1.0\text{ mole of oil}$ ($878\text{ g}$), the mass of iodine absorbed is:
$$m_{\text{I}_2, \text{mol}} = \frac{IV \times M_{\text{TAG}}}{100} = \frac{174.6 \times 878}{100} = 1533\text{ g }\text{I}_2$$
The moles of $\text{I}_2$ absorbed per mole of TAG:
$$\overline{n}_{\text{db}} = \frac{1533\text{ g}}{253.81\text{ g/mol}} = \mathbf{6.04} \approx \mathbf{6\text{ double bonds}}$$
Each triacylglycerol molecule contains an average of **6 double bonds** (corresponding to, for example, two linoleic acid chains with 2 double bonds each and one oleic acid chain with 1 double bond, or two linolenic acid chains with 3 double bonds each), typical of highly unsaturated drying oils."""
            },
            {
                "id": "prob-9-3",
                "problemNumber": "9.3",
                "title": "Selenium Dehydrogenation of Cholesterol to Diels' Hydrocarbon ($C_{18}H_{16}$)",
                "statement": r"""Pyrolysis of cholesterol with powdered selenium metal at $340^\circ\text{C}$ affords Diels' hydrocarbon ($C_{18}H_{16}$) as the principal crystalline product.
(a) Draw the structural formula of Diels' hydrocarbon, identifying the phenanthrene nucleus and the cyclopentene ring.
(b) Account for the loss of 9 carbon atoms and oxygen during the pyrolytic conversion of cholesterol ($C_{27}H_{46}O$) into Diels' hydrocarbon ($C_{18}H_{16}$).
(c) Explain why selenium dehydrogenation preserves the angular methyl group at C13 (which migrates to C17) but eliminates the angular methyl group at C10.""",
                "hints": [
                    r"Cholesterol has 27 carbons; Diels' hydrocarbon has 18 carbons.",
                    r"The 8-carbon side chain at C17 is thermally cleaved (27 - 8 = 19).",
                    r"One of the angular methyls is eliminated to allow full aromaticity of the central phenanthrene ring."
                ],
                "solution": r"""### Step 1: Structure of Diels' Hydrocarbon
Diels' hydrocarbon ($C_{18}H_{16}$) is **3'-methyl-1,2-cyclopentenophenanthrene**:
- It consists of a fully aromatic phenanthrene ring system (rings A, B, and C) fused to a five-membered cyclopentene ring (ring D) at carbons 1 and 2 of the phenanthrene framework.
- A single methyl group resides at the 3'-position of the five-membered cyclopentene ring.

### Step 2: Mass and Carbon Balance
Cholesterol has formula $C_{27}H_{46}O$ ($27\text{ carbons}$):
1. **Side-Chain Extrusion ($-8\text{ carbons}$)**:
   Thermal homolysis of the $\text{C}17-\text{C}20$ single bond eliminates the 8-carbon octyl side chain ($-\text{C}_8\text{H}_{17}$) as volatile iso-octane/octene fragments:
   $$27 - 8 = 19\text{ carbons}$$
2. **Deoxygenation**:
   The $3\beta$-hydroxyl group is dehydrated to a double bond and lost as water ($\text{H}_2\text{O}$) or hydrogen selenide ($\text{H}_2\text{Se}$).
3. **Aromatization and Methyl Extrusion ($-1\text{ carbon}$)**:
   Aromatization of rings A and B forces the extrusion of the angular methyl group at **C10** as methane ($\text{CH}_4$), because an aromatic ring cannot accommodate a quaternary $sp^3$ angular methyl group:
   $$19 - 1 = \mathbf{18\text{ carbons}}$$
The product has formula $\mathbf{C_{18}H_{16}}$.

### Step 3: Fate of the C13 Angular Methyl Group
During the vigorous high-temperature selenium dehydrogenation:
- Ring C undergoes aromatization. To permit aromatization of C13 and C14, the quaternary angular methyl group at C13 undergoes a **Wagner-Meerwein-type 1,2-migration** onto the adjacent five-membered ring D (moving to C17, which becomes C3' of the cyclopentenophenanthrene ring).
- This 1,2-shift preserves the methyl group on the cyclopentene ring while allowing the three six-membered rings (A, B, C) to attain complete, planar phenanthrene aromatic resonance."""
            },
            {
                "id": "prob-9-4",
                "problemNumber": "9.4",
                "title": "Barbier-Wieland Degradation Stepwise Calculus on Cholanic Acid",
                "statement": r"""Cholanic acid ($C_{24}H_{40}O_2$) was subjected to three successive cycles of the Barbier-Wieland degradation:
(a) Write out the reagents and intermediates for Cycle 1, showing the formation of the 1,1-diphenylalkene and the resulting shortened acid (norcholanic acid, $C_{23}H_{38}O_2$).
(b) Cycle 2 shortens norcholanic acid to bisnorcholanic acid ($C_{22}H_{36}O_2$).
(c) Cycle 3 shortens bisnorcholanic acid to a compound that fails to yield a carboxylic acid upon chromic acid cleavage, producing instead the ketone **etiomonoethyl ketone** and **pregnan-20-one** ($C_{21}H_{34}O$).
Deduce the exact constitution of the side chain attached to C17 of cholanic acid.""",
                "hints": [
                    r"Cycle 1: Esterification with MeOH -> PhMgBr -> H+ dehydration -> CrO3 cleavage -> loses 1 carbon.",
                    r"Cycle 2: Loses second carbon.",
                    r"Cycle 3: Cleavage produces a ketone, which means the carbon remaining has no alpha-hydrogen (it is a secondary/tertiary carbon)."
                ],
                "solution": r"""### Step 1: Cycle 1 Transformation
1. **Esterification**:
   $$\text{Cholanic acid } (C_{24}) \xrightarrow{\text{MeOH, H}^+} \text{Methyl cholanoate}$$
2. **Double Grignard Addition**:
   $$\text{Methyl cholanoate} + 2\text{ PhMgBr} \to \text{Diphenyl carbinol } (\text{R-CH}_2\text{-C(OH)Ph}_2)$$
3. **Dehydration**:
   $$\text{R-CH}_2\text{-C(OH)Ph}_2 \xrightarrow{\text{Ac}_2\text{O}, \Delta} \text{R-CH}=\text{CPh}_2 + \text{H}_2\text{O}$$
4. **Oxidative Cleavage**:
   $$\text{R-CH}=\text{CPh}_2 \xrightarrow{\text{CrO}_3} \mathbf{\text{Norcholanic acid } (C_{23}H_{38}O_2)} + \text{Ph}_2\text{C}=\text{O}$$
Exactly **one methylene carbon ($\text{CH}_2$)** is excised.

### Step 2: Cycle 2 and Cycle 3 Degradations
- **Cycle 2**:
  Repeating the sequence on norcholanic acid ($C_{23}$) excises a second methylene carbon:
  $$\text{Norcholanic acid } (C_{23}) \xrightarrow{\text{BW cycle}} \mathbf{\text{Bisnorcholanic acid } (C_{22}H_{36}O_2)} + \text{Ph}_2\text{CO}$$
- **Cycle 3**:
  Bisnorcholanic acid ($C_{22}$) is converted to its 1,1-diphenylalkene derivative:
  $$\text{R}^\prime\text{-C(CH}_3)=\text{CPh}_2$$
  Upon chromic acid oxidation, cleavage of this alkene does **not** yield a carboxylic acid; instead, it yields **pregnan-20-one (a methyl ketone, $\text{R}^\prime-\text{COCH}_3$, $C_{21}$)**!

### Step 3: Deduction of Side-Chain Structure
- Cycle 1 removed a $-\text{CH}_2-$ group $\implies -\text{CH}_2-\text{COOH}$.
- Cycle 2 removed a second $-\text{CH}_2-$ group $\implies -\text{CH}_2-\text{CH}_2-\text{COOH}$.
- Cycle 3 yielded a methyl ketone ($-\text{COCH}_3$), which proves that the carbon attached to the second methylene group carried a **methyl branch**: $-\text{CH(CH}_3)-$.
- Connecting to the steroid nucleus at C17 establishes the side chain:
  $$\mathbf{-CH(CH_3)-CH_2-CH_2-COOH}$$
This proved that cholanic acid has a 5-carbon branched side chain attached to C17."""
            },
            {
                "id": "prob-9-5",
                "problemNumber": "9.5",
                "title": "Blanc's Rule Application to Steroid Ring Cleavages",
                "statement": r"""Adolf Windaus subjected the four rings of the sterol cholestanol to sequential oxidative ring opening to determine their ring sizes using Blanc's Rule:
(a) State Blanc's Rule, specifying the carbon chain lengths that form cyclic anhydrides vs cyclic ketones upon heating with acetic anhydride.
(b) Nitric acid oxidation of Ring A opens it to a dicarboxylic acid ($C_{27}H_{46}O_4$, a diacid). Heating this diacid with acetic anhydride yields a cyclic ketone with evolution of $\text{CO}_2$. What is the ring size of Ring A?
(c) Oxidation of Ring D opens it to a dicarboxylic acid. Heating this diacid with acetic anhydride yields a cyclic anhydride with no evolution of $\text{CO}_2$. What is the ring size of Ring D?""",
                "hints": [
                    r"Blanc's rule: 1,4- and 1,5-dicarboxylic acids (succinic, glutaric) form cyclic anhydrides.",
                    r"1,6- and 1,7-dicarboxylic acids (adipic, pimelic) form cyclic ketones with loss of CO2.",
                    r"Count how ring size relates to the dicarboxylic acid chain length."
                ],
                "solution": r"""### Step 1: Formulation of Blanc's Rule
When a dicarboxylic acid is heated with acetic anhydride ($\text{Ac}_2\text{O}$) at $150–200^\circ\text{C}$:
1. **1,4-Dicarboxylic acids** (e.g., succinic acid, 4 carbons between carboxyls inclusive) and **1,5-dicarboxylic acids** (e.g., glutaric acid, 5 carbons) dehydrate to form stable **5-membered or 6-membered cyclic anhydrides** ($\mathbf{no\ CO_2\ loss}$):
   $$\text{HOOC}-(\text{CH}_2)_3-\text{COOH} \xrightarrow{\text{Ac}_2\text{O}} \text{Glutaric anhydride} + \text{H}_2\text{O}$$
2. **1,6-Dicarboxylic acids** (e.g., adipic acid, 6 carbons) and **1,7-dicarboxylic acids** (e.g., pimelic acid, 7 carbons) undergo pyrolytic decarboxylative cyclization to form stable **5-membered or 6-membered cyclic ketones** with release of carbon dioxide ($\mathbf{CO_2\ evolved}$):
   $$\text{HOOC}-(\text{CH}_2)_4-\text{COOH} \xrightarrow{\text{Ac}_2\text{O}, \Delta} \text{Cyclopentanone} + \text{CO}_2 + \text{H}_2\text{O}$$

### Step 2: Ring A Determination
- Cleavage of a ring carbon-carbon bond in Ring A produces two carboxyl groups.
- Because Ring A is a six-membered cyclohexane ring, its oxidative opening yields a **1,6-dicarboxylic acid (adipic acid analog)**.
- Heating this 1,6-diacid with acetic anhydride yields a **cyclic ketone with release of $\text{CO}_2$**.
- This definitively proves that **Ring A is a six-membered ring**.

### Step 3: Ring D Determination
- Cleavage of Ring D produces two carboxyl groups.
- If Ring D were a six-membered ring, it would form a 1,6-diacid and eliminate $\text{CO}_2$.
- Experimentally, the dicarboxylic acid derived from Ring D dehydration yields a **cyclic anhydride with zero $\text{CO}_2$ evolution**.
- According to Blanc's Rule, forming a cyclic anhydride without loss of $\text{CO}_2$ proves that the cleavage product is a **1,5-dicarboxylic acid (glutaric acid analog)**.
- A 1,5-dicarboxylic acid originates from the cleavage of a **five-membered ring**.
- This established that **Ring D is a five-membered cyclopentane ring**."""
            },
            {
                "id": "prob-9-6",
                "problemNumber": "9.6",
                "title": "Digitalis Cardenolide $\\gamma$-Lactone Ring Reaction with Legal's Reagent",
                "statement": r"""Cardiotonic steroids of the cardenolide family (such as digitoxin and ouabain) give a characteristic deep red color when treated with sodium nitroprusside in alkaline pyridine (Legal's test).
(a) Draw the structural formula of the $C17\beta$-lactone ring of cardenolides and identify the acidic $\alpha$-proton responsible for carbanion formation.
(b) Explain the chemical basis of the Legal test, outlining the condensation between the cardenolide carbanion and the nitroprusside iron-nitrosyl complex ($[\text{Fe(CN)}_5\text{NO}]^{2-}$).
(c) Explain why bufadienolides (such as scillaren A) do not give a positive Legal test.""",
                "hints": [
                    r"Cardenolides have a five-membered alpha,beta-unsaturated gamma-lactone ring.",
                    r"The CH2 group in the lactone ring is acidic because the enolate is conjugated.",
                    r"Bufadienolides have a six-membered alpha-pyrone ring with two conjugated double bonds and no reactive acidic CH2."
                ],
                "solution": r"""### Step 1: Structure of the Cardenolide Lactone Ring
The cardenolide aglycone bears a five-membered **$\alpha,\beta$-unsaturated $\gamma$-lactone (but-2-en-4-olide)** ring attached at $C17\beta$:
- The double bond is between C20 and C22 ($\alpha,\beta$).
- The carbonyl is at C23.
- Carbon-21 is a ring methylene group ($-\text{CH}_2-$) adjacent to both the ring oxygen and the conjugated double bond.
- The protons on **C21** are acidic ($pK_a \approx 13 - 15$) because deprotonation generates an extensively resonance-delocalized carbanion/enolate across the lactone $\pi$-system.

### Step 2: Mechanism of Legal's Test
1. **Carbanion Formation**:
   In alkaline pyridine solution, base abstracts a proton from C21 of the cardenolide lactone ring:
   $$\text{Lactone} + \text{OH}^- \rightleftharpoons \text{Lactone}^- + \text{H}_2\text{O}$$
2. **Nucleophilic Addition to Nitroprusside**:
   The carbanion attacks the electrophilic nitrogen atom of the coordinated nitrosyl ($\text{NO}^+$) ligand of the sodium nitroprusside complex ($[\text{Fe(CN)}_5\text{NO}]^{2-}$):
   $$\text{Lactone}^- + [\text{Fe(CN)}_5\text{NO}]^{2-} \to [\text{Fe(CN)}_5\text{N}(=\text{O})-\text{Lactone}]^{3-}$$
3. **Chromophore Generation**:
   Intramolecular electron transfer from iron(II) to the coordinated nitrosoalkene ligand creates an intense, deep red-orange charge-transfer absorption band ($\lambda_{\text{max}} \approx 490 - 510\text{ nm}$), confirming the presence of the active cardenolide butenolide ring.

### Step 3: Bufadienolides Lack Legal Test Activity
- Bufadienolides (e.g., scillaren A, bufalin) possess a six-membered **$\alpha$-pyrone ring** containing two conjugated double bonds:
  $$-\text{C}(=\text{O})-\text{CH}=\text{CH}-\text{CH}=\text{CH}-$$
- All carbons in the six-membered pyrone ring are $sp^2$ hybridized.
- They lack an isolated $sp^3$ methylene group ($-\text{CH}_2-$) adjacent to the lactone oxygen; therefore, they cannot form the requisite carbanion at room temperature and **give a negative Legal's test**."""
            },
            {
                "id": "prob-9-7",
                "problemNumber": "9.7",
                "title": "Conformational Rigidity of $5\\alpha$-Cholestanol vs $5\\beta$-Coprostanol",
                "statement": r"""Compare the three-dimensional shapes and conformational dynamics of $5\alpha$-cholestanol and $5\beta$-coprostanol:
(a) Draw the chair conformational representations of rings A and B for both stereoisomers, indicating the configuration of the A/B ring junction.
(b) In $5\alpha$-cholestanol, is the $3\beta$-hydroxyl group equatorial or axial? In $5\beta$-coprostanol, is the $3\beta$-hydroxyl group equatorial or axial?
(c) Explain why $5\alpha$-cholestanol precipitates quantitatively with digitonin, whereas $5\beta$-coprostanol does not.""",
                "hints": [
                    r"5alpha has trans-A/B fusion (trans-decalin type).",
                    r"5beta has cis-A/B fusion (cis-decalin type).",
                    r"In 5alpha, 3beta-OH is equatorial; in 5beta, 3beta-OH is axial."
                ],
                "solution": r"""### Step 1: Ring Fusion Architecture
1. **$5\alpha$-Cholestanol (Trans-A/B Fusion)**:
   - The C5 hydrogen atom is **$\alpha$** (trans to the C10 angular methyl group, which is $\beta$).
   - Rings A and B are **trans-fused** (analogs of trans-decalin).
   - Both rings A and B adopt rigid chair conformations lying in the same planar orientation.
   - The entire steroid framework is an extended, flat, planar ribbon: **trans-anti-trans-anti-trans**.
2. **$5\beta$-Coprostanol (Cis-A/B Fusion)**:
   - The C5 hydrogen atom is **$\beta$** (cis to the C10 angular methyl group).
   - Rings A and B are **cis-fused** (analogs of cis-decalin).
   - Ring A folds sharply downward at an angle of approximately **$90^\circ$** relative to the mean plane of rings B, C, and D, producing a distinctly bent, L-shaped or U-shaped three-dimensional architecture.

### Step 2: Orientation of the $3\beta$-Hydroxyl Group
- In **$5\alpha$-cholestanol**:
  - The $3\beta$-hydroxyl group is oriented upwards on the chair of Ring A.
  - In a trans-A/B ring system, a $3\beta$-substituent is **equatorial**.
- In **$5\beta$-coprostanol**:
  - Because of the cis-fusion flip of Ring A, a $3\beta$-hydroxyl group becomes **axial**!

### Step 3: Digitonin Precipitation Selectivity
- **Digitonin** is a steroidal saponin that forms highly insoluble 1:1 molecular inclusion complexes with sterols.
- Formation of the insoluble complex requires:
  1. A planar, unbent steroid ring framework (flat lipophilic surface).
  2. An **equatorial $3\beta$-hydroxyl group** pointing coplanar with the ring.
- In $5\alpha$-cholestanol, the planar trans-A/B core and equatorial $3\beta$-OH fit into the digitonin binding pocket, forming an insoluble crystalline digitonide.
- In $5\beta$-coprostanol, the bent $90^\circ$ cis-A/B geometry and the axial orientation of the $3\beta$-OH sterically prevent complexation, resulting in **zero precipitation with digitonin**."""
            }
        ]
    }
    units.append(u9)

    # =========================================================================
    # UNIT 10: Antibiotics & Natural Chemotherapeutics: Beta-Lactams & Chloramphenicol
    # =========================================================================
    u10 = {
        "id": "unit-10",
        "unitNumber": 10,
        "title": "Unit 10: Antibiotics & Natural Chemotherapeutics: Beta-Lactams & Chloramphenicol",
        "leadSummary": "Comprehensive physical organic, degradative, and medicinal chemistry of major natural antibiotics: the discovery and structural elucidation of Penicillin G, the strained 6-aminopenicillanic acid (6-APA) fused thiazolidine-beta-lactam core, acidic and basic degradation cascades, DD-transpeptidase suicide inhibition mechanisms, beta-lactamase resistance and clavulanic acid synergy, and the complete stereochemical elucidation and total synthesis of chloramphenicol.",
        "simulations": ["sim_nat_penicillin_beta_lactam_inhibition"],
        "sections": [
            {
                "id": "sec-10-1",
                "secNumber": "10.1",
                "title": "Antibiotics: Discovery, Classification & Cellular Targets",
                "content": r"""Antibiotics are secondary metabolites produced by microorganisms (fungi, actinomycetes, bacteria) that kill (bactericidal) or inhibit the growth of (bacteriostatic) competing microbial species at low concentrations.

### Historical Evolution
1. **Alexander Fleming (1928)**: Discovered that colonies of the mold *Penicillium notatum* lysing *Staphylococcus aureus* secreted a diffusible bactericidal substance, which he named **penicillin**.
2. **Florey, Chain, and Heatley (1939–1941)**: Developed surface and submerged fermentation, solvent extraction, and freeze-drying protocols at Oxford, achieving the first successful human clinical treatments and enabling mass industrial production during World War II (1945 Nobel Prize).
3. **Selman Waksman (1943)**: Isolated **streptomycin** from the soil actinomycete *Streptomyces griseus*, establishing the term 'antibiotic' and providing the first effective cure for tuberculosis.

### Major Mechanistic Classes of Antibiotics
1. **Bacterial Cell Wall Synthesis Inhibitors**: Target peptidoglycan crosslinking (e.g., $\beta$-lactams: penicillins, cephalosporins, carbapenems; glycopeptides: vancomycin).
2. **Bacterial Protein Synthesis Inhibitors**: Bind bacterial ribosomal subunits:
   - 30S Subunit: Aminoglycosides (gentamicin, streptomycin) cause codon misreading; Tetracyclines block aminoacyl-tRNA binding.
   - 50S Subunit: Macrolides (erythromycin, azithromycin) block nascent peptide translocation; Chloramphenicol inhibits peptidyl transferase.
3. **Bacterial Nucleic Acid Synthesis Inhibitors**: Quinolones (ciprofloxacin) inhibit DNA gyrase; Rifamycins inhibit DNA-directed RNA polymerase.
4. **Antimetabolites**: Sulfonamides and trimethoprim block folate biosynthesis."""
            },
            {
                "id": "sec-10-2",
                "secNumber": "10.2",
                "title": "The Penicillins: 6-APA Core, Strained $\\beta$-Lactam Architecture & Spectroscopy",
                "content": r"""The penicillins are bicyclic secondary metabolites produced by *Penicillium chrysogenum*, characterized by a common bicyclic core: **6-aminopenicillanic acid (6-APA)**.

### The Fused Bicyclic Core Architecture
The penicillin nucleus consists of two fused rings:
- A four-membered **$\beta$-lactam ring** (azetidin-2-one).
- A five-membered **thiazolidine ring** containing a sulfur atom, two methyl groups at C2, and a carboxylic acid at C3.
- The two rings are fused across C5 and C6 in a rigid, non-planar **cis-configuration**:
  $$\text{Fused 4-5 Bicyclic System (Bicyclo[3.2.0]heptane derivative)}$$

### Strain Energy and Suppression of Amide Resonance
In normal planar amides, resonance delocalization between the nitrogen lone pair and the carbonyl group confers $\sim 40\%$ double-bond character:
$$\text{O}=\text{C}-\text{N} \longleftrightarrow ^-\text{O}-\text{C}=\text{N}^+ \quad (\Delta G^\circ_{\text{res}} \approx 84\text{ kJ/mol})$$
In the penicillin $\beta$-lactam ring:
1. **Angle Strain**: The four-membered ring forces the internal bond angles to contract from ideal $120^\circ$ ($sp^2$) or $109.5^\circ$ ($sp^3$) down to approximately **$90^\circ$**.
2. **Pyramidal Nitrogen Geometry**: The nitrogen atom (N4) is located at the bridgehead of the fused 4-membered and 5-membered rings. The dihedral angle between the two rings is approximately $115^\circ$, forcing N4 into a puckered, pyramidal geometry.
3. **Loss of Resonance Overlap**: The lone pair of N4 cannot achieve parallel $p$-orbital overlap with the carbonyl $\pi$-system.
Consequently, **amide resonance is almost entirely suppressed**. The $\beta$-lactam carbonyl behaves chemically like an extraordinarily reactive, electrophilic **acid chloride or anhydride**, with an infrared stretching frequency shifted to an anomalous **$\nu_{\text{C}=\text{O}} \approx 1780 - 1790\text{ cm}^{-1}$** (compared to $1650 - 1680\text{ cm}^{-1}$ for normal amides)."""
            },
            {
                "id": "sec-10-3",
                "secNumber": "10.3",
                "title": "Chemical Degradation of Penicillins: Acid & Alkaline Inactivations",
                "content": r"""The extreme chemical reactivity and ring strain of the penicillin $\beta$-lactam core makes it acutely sensitive to chemical degradation.

### 1. Acid-Catalyzed Inactivation (Penillic Acid Formation)
At $\text{pH} < 3$ (such as gastric acid), natural Penicillin G (benzylpenicillin) decomposes rapidly:
1. **Protonation**: The side-chain amide carbonyl oxygen is protonated.
2. **Intramolecular Attack**: The side-chain amide oxygen attacks the electrophilic $\beta$-lactam carbonyl carbon at C7, forming an oxazolone intermediate while opening the strained four-membered $\beta$-lactam ring.
3. **Rearrangement**: Subsequent ring opening of the thiazolidine ring and complex recyclization affords **penillic acid** (an optically active dicarboxylic acid) or **penillic aldehyde** and **penicillamine (3-mercaptovaline, $C_5H_{11}NO_2S$)**:
   $$\text{Penicillin G} \xrightarrow{\text{H}^+, \text{pH } 2} \text{Penillic acid} \to \text{Penicillamine} + \text{Benzylpenaldic acid}$$
Because Penicillin G is destroyed by stomach acid, it cannot be administered orally and must be given by intramuscular or intravenous injection.

### 2. Alkaline and Enzymatic Hydrolysis (Penicilloic Acid Formation)
In dilute aqueous alkali ($\text{pH} > 9$) or upon incubation with bacterial **$\beta$-lactamase (penicillinase)**:
- Hydroxide ion or catalytic water attacks the electrophilic $\beta$-lactam carbonyl carbon (C7).
- The $\text{C}7-\text{N}4$ bond cleaves irreversibly, opening the four-membered ring while leaving the thiazolidine ring intact.
- This produces **penicilloic acid** (a biologically inactive dicarboxylic acid):
  $$\text{Penicillin} + \text{H}_2\text{O} \xrightarrow{\text{OH}^- \text{ or } \beta\text{-lactamase}} \mathbf{\text{Penicilloic acid}}$$
Subsequent treatment of penicilloic acid with mercuric chloride ($\text{HgCl}_2$) precipitates mercuric mercaptide, releasing **D-penicillamine**."""
            },
            {
                "id": "sec-10-4",
                "secNumber": "10.4",
                "title": "Biochemical Mechanism of Action: DD-Transpeptidase Suicide Inhibition",
                "content": r"""Penicillins are mechanism-based bactericidal agents that disrupt the synthesis of the peptidoglycan layer of the bacterial cell wall.

### Peptidoglycan Architecture and Crosslinking
The bacterial cell wall consists of alternating linear glycan chains of $N$-acetylglucosamine (NAG) and $N$-acetylmuramic acid (NAM) crosslinked by short peptide chains.
In Gram-positive bacteria, crosslinking is catalyzed by membrane-bound **DD-transpeptidase enzymes** (also termed **Penicillin-Binding Proteins, PBPs**):
- The terminal peptide of the uncrosslinked wall is **$-L\text{-Ala}-D\text{-Glu}-L\text{-Lys}-D\text{-Ala}-D\text{-Ala}$**.
- The DD-transpeptidase active site utilizes a catalytic serine residue ($\text{Ser-OH}$) to attack the peptide bond between the two terminal D-alanines, forming an acyl-enzyme intermediate while releasing the terminal D-alanine.
- The amine group of an adjacent peptide pentaglycine crossbridge attacks the acyl-enzyme intermediate, regenerating the active serine and forming the crosslink that confers tensile strength against osmotic lysis.

### Mechanism-Based 'Suicide' Inactivation
Tipper and Strominger (1965) discovered that **penicillin is a stereochemical and structural mimic of the natural acyl-D-Ala-D-Ala substrate**:
1. The distance between the side-chain carbonyl and the C3 carboxylate in penicillin matches the conformation of the D-Ala-D-Ala dipeptide backbone.
2. The active-site catalytic serine ($\text{Ser-OH}$) attacks the reactive $\beta$-lactam carbonyl carbon, opening the four-membered ring and forming a covalent **penicilloyl-serine ester bond**:
   $$\text{PBP-Ser-OH} + \text{Penicillin} \to \mathbf{\text{PBP-Ser-O-CO-Penicilloate} \quad (\text{Dead-end acyl-enzyme})}$$
3. Because the bulky thiazolidine ring is covalently tethered to the serine ester, it sterically blocks the approach of water or nucleophilic amine crossbridges. The deacylation rate constant is infinitesimal ($k_{\text{deacyl}} < 10^{-6}\text{ s}^{-1}$, half-life $>24\text{ hours}$).
4. The transpeptidase is irreversibly trapped in an inactive, dead-end state, halting cell wall biosynthesis. Osmotic pressure causes the bacterial cell to burst (lysis)."""
            },
            {
                "id": "sec-10-5",
                "secNumber": "10.5",
                "title": "Resistance Mechanisms & Semi-Synthetic Penicillins: $\\beta$-Lactamases & Clavulanate",
                "content": r"""Bacterial pathogens rapidly evolve resistance against natural penicillins through two primary mechanisms:
1. **Production of $\beta$-Lactamase Enzymes**: Secreted enzymes that hydrolyze the $\beta$-lactam ring to inactive penicilloic acid before the drug can reach PBPs.
2. **Alteration of Target PBPs**: Acquisition of mutant PBPs with drastically reduced binding affinity for $\beta$-lactams (e.g., PBP2a in Methicillin-Resistant *Staphylococcus aureus*, MRSA).

### Semi-Synthetic Penicillin Generations
By enzymatically cleaving the benzyl side chain of Penicillin G using penicillin acylase, chemists obtained large quantities of the free **6-APA** core, which was acylated with synthetic acyl chlorides:
1. **Acid-Resistant Penicillins (Oral Administration)**:
   Introducing an electron-withdrawing group at the $\alpha$-position of the acyl side chain (e.g., **Penicillin V** with a phenoxymethyl side chain, $-\text{OCH}_2\text{Ph}$, or **Ampicillin** with an $\alpha$-amino group, $-\text{CH}(\text{NH}_2)\text{Ph}$):
   - The electron-withdrawing substituent decreases the nucleophilicity of the side-chain carbonyl oxygen, preventing intramolecular attack on the $\beta$-lactam ring and conferring resistance to stomach acid.
2. **$\beta$-Lactamase-Resistant Penicillins**:
   Introducing bulky, sterically hindered aromatic rings directly adjacent to the side-chain carbonyl (e.g., **Methicillin**, 2,6-dimethoxyphenyl; **Oxacillin**):
   - The bulky ortho substituents sterically shield the $\beta$-lactam carbonyl from approaching $\beta$-lactamase active sites while still fitting into the active site of native PBPs.
3. **Broad-Spectrum Penicillins**:
   E.g., **Amoxicillin** and **Ticarcillin**, possessing polar side chains that facilitate passage through outer-membrane porin channels in Gram-negative bacteria.

### Clavulanic Acid: Mechanism-Based $\beta$-Lactamase Inhibitor
Clavulanic acid is an oxapenam secondary metabolite isolated from *Streptomyces clavuligerus* lacking an acylamino side chain at C6:
- It acts as an irreversible **'suicide' inhibitor** of bacterial serine $\beta$-lactamases.
- When cleaved by the $\beta$-lactamase active-site serine, the oxapenam ring opens and undergoes a secondary chemical rearrangement, forming a tethered imine that alkylates a second nucleophilic residue in the enzyme active site.
- Combining amoxicillin with clavulanate (**Augmentin**) restores clinical efficacy against $\beta$-lactamase-producing bacteria."""
            },
            {
                "id": "sec-10-6",
                "secNumber": "10.6",
                "title": "Chloramphenicol: Structural Elucidation, Nitro Group & Dichloroacetamide Core",
                "content": r"""Chloramphenicol ($C_{11}H_{12}\text{Cl}_2\text{N}_2\text{O}_5$) is a broad-spectrum antibiotic originally isolated in 1947 by Paul Burkholder from the actinomycete *Streptomyces venezuelae*.

### Structural Elucidation
1. **Molecular Formula and Heteroatoms**:
   Elemental analysis and HRMS establish $C_{11}H_{12}\text{Cl}_2\text{N}_2\text{O}_5$.
   - Contains two chlorine atoms, two nitrogen atoms, and five oxygen atoms.
   - It was the **first natural product discovered containing an aromatic nitro group ($-\text{NO}_2$)** and a **dichloroacetyl group ($-\text{CO-CHCl}_2$)**.
2. **Identification of the Aromatic Nitro Group**:
   - UV-Visible spectrum exhibits a strong absorption band at $\lambda_{\text{max}} = 278\text{ nm}$ ($\epsilon \approx 9,800$), characteristic of a nitrobenzene chromophore.
   - Reduction with tin and hydrochloric acid ($\text{Sn/HCl}$) reduces the nitro group to an aromatic primary amine, which on diazotization and coupling with $\beta$-naphthol yields an intense orange-red azo dye.
   - Vigorous oxidation with chromic acid yields **$p$-nitrobenzoic acid ($\text{O}_2\text{N-C}_6\text{H}_4\text{COOH}$)**, proving a **para-substituted nitrobenzene ring**.
3. **Identification of the Dichloroacetamide and Propanediol Backbone**:
   - Acidic or alkaline hydrolysis cleaves chloramphenicol into **dichloroacetic acid ($\text{CHCl}_2\text{COOH}$)** and an optically active aminodiol base ($C_9H_{12}N_2O_4$):
     $$\text{Chloramphenicol} + \text{H}_2\text{O} \to \text{CHCl}_2\text{COOH} + \text{Aminodiol base}$$
   - Reaction of the aminodiol base with periodic acid ($\text{HIO}_4$) consumes one mole of $\text{HIO}_4$, producing $p$-nitrobenzaldehyde ($\text{O}_2\text{N-C}_6\text{H}_4\text{CHO}$), formaldehyde ($\text{HCHO}$), and ammonia ($\text{NH}_3$).
   - This proves that the aminodiol is **2-amino-1-(4-nitrophenyl)propane-1,3-diol**:
     $$\text{O}_2\text{N}-\text{C}_6\text{H}_4-\text{CH(OH)}-\text{CH(NH}_2)-\text{CH}_2\text{OH}$$
Recombining with dichloroacetic acid establishes chloramphenicol as:
$$\mathbf{2,2-dichloro-N-[(1R,2R)-1,3-dihydroxy-1-(4-nitrophenyl)propan-2-yl]acetamide}$$"""
            },
            {
                "id": "sec-10-7",
                "secNumber": "10.7",
                "title": "Stereochemistry and Total Chemical Synthesis of Chloramphenicol",
                "content": r"""Chloramphenicol contains two contiguous chiral centers: C1 (benzylic secondary alcohol) and C2 (amide-bearing carbon), giving rise to $2^2 = 4$ stereoisomers (two diastereomeric enantiomeric pairs: D/L-erythro and D/L-threo).

### Stereochemical Configuration
- Natural chloramphenicol is exclusively the **$(1R, 2R)-(-)$-threo** stereoisomer.
- The other three stereoisomers ($(1S, 2S)\text{-(+)-threo}$, $(1R, 2S)\text{-erythro}$, and $(1S, 2R)\text{-erythro}$) are biologically inactive or possess $<1\%$ of the antimicrobial potency of the natural $(1R, 2R)$ isomer, proving that the ribosomal peptidyl transferase binding pocket is exquisitely stereospecific.

### Industrial Chemical Synthesis (Long-Troutman Route)
Because fermentation yields are modest, chloramphenicol was the first antibiotic manufactured exclusively by chemical total synthesis:
1. **Starting Material**: Condensation of $p$-nitroacetophenone with bromine yields $p$-nitro-$\alpha$-bromoacetophenone.
2. **Hexamethylenetetramine (Delepine Reaction)**: Reaction with hexamethylenetetramine followed by ethanolic $\text{HCl}$ hydrolysis affords $p$-nitro-$\alpha$-aminoacetophenone hydrochloride.
3. **Acetylation and Hydroxymethylation**:
   - The amino group is protected with acetic anhydride.
   - Aldol condensation with formaldehyde ($\text{HCHO}$) in the presence of sodium bicarbonate introduces the hydroxymethyl group at C2:
     $$\text{O}_2\text{N-Ar-COCH}(\text{NHAc})\text{-CH}_2\text{OH}$$
4. **Meerwein-Ponndorf-Verley (MPV) Reduction**:
   Reduction of the ketone with aluminum isopropoxide ($\text{Al(O-}i\text{Pr)}_3$) in isopropanol reduces the carbonyl to an alcohol:
   - The MPV reduction proceeds through a cyclic six-membered transition state that selectively affords the **threo-diastereomer** ($(\pm)$-threo-base) over the erythro isomer.
5. **Resolution and Dichloroacetylation**:
   - Hydrolysis removes the acetate group, yielding racemic $(\pm)$-threo-1-(4-nitrophenyl)-2-aminopropane-1,3-diol.
   - Racemic resolution with **$D$-camphorsulfonic acid** or $L-(+)$-tartaric acid isolates the bioactive $(1R, 2R)$ enantiomer.
   - Selective $N$-acylation of the primary amine with methyl dichloroacetate ($\text{CHCl}_2\text{COOMe}$) furnishes pure **(1R,2R)-(-)-chloramphenicol**."""
            }
        ],
        "problems": [
            {
                "id": "prob-10-1",
                "problemNumber": "10.1",
                "title": "Acidic Hydrolysis Mechanism of Penicillin G to Penillic Acid and Penicillamine",
                "statement": r"""When Penicillin G (benzylpenicillin, $C_{16}H_{18}N_2O_4S$) is kept in dilute aqueous hydrochloric acid at $\text{pH } 2.0$:
(a) Provide the detailed curved-arrow mechanism for the formation of the oxazolone intermediate, showing how the side-chain benzylcarbonyl group attacks the $\beta$-lactam ring.
(b) Show the subsequent rearrangement yielding crystalline penillic acid.
(c) Treatment of the acid-degraded mixture with mercuric chloride ($\text{HgCl}_2$) precipitates mercuric mercaptide and releases D-penicillamine. Write the structural formula of D-penicillamine and assign its $(R/S)$ configuration.""",
                "hints": [
                    r"Protonation occurs on the side-chain amide oxygen or beta-lactam nitrogen.",
                    r"Intramolecular attack by side-chain oxygen forms an oxazolone and cleaves the strained 4-membered ring.",
                    r"D-Penicillamine is 3-mercaptovaline: (CH3)2C(SH)-CH(NH2)-COOH."
                ],
                "solution": r"""### Step 1: Oxazolone Intermediate Formation
1. **Protonation**:
   In aqueous acid ($\text{pH } 2$), protonation occurs preferentially at the side-chain benzylamide carbonyl oxygen or the strained $\beta$-lactam nitrogen:
   $$\text{PhCH}_2-\text{CO}-\text{NH}-\cdots + \text{H}^+ \rightleftharpoons \text{PhCH}_2-\text{C}^+(\text{OH})-\text{NH}-\cdots$$
2. **Nucleophilic Attack by Side-Chain Oxygen**:
   The side-chain carbonyl oxygen is positioned in close proximity to the strained four-membered ring carbonyl carbon (C7). It attacks C7:
   - Closes a five-membered **oxazolone ring**.
   - Concurrently, the $\text{C}7-\text{N}4$ bond of the strained $\beta$-lactam ring cleaves.
   - The relief of $\sim 105\text{ kJ/mol}$ of ring strain provides a massive thermodynamic driving force.

### Step 2: Rearrangement to Penillic Acid
1. **Thiazolidine Ring Opening**:
   The opening of the $\beta$-lactam ring creates a transient iminium intermediate. The sulfur atom of the thiazolidine ring participates in an intramolecular rearrangement, cleaving the $\text{C}5-\text{S}$ bond.
2. **Recyclization to Imidazole Derivative**:
   The nitrogen atom attacks the oxazolone carbon, opening the oxazolone and closing a new, highly stable five-membered imidazole ring:
   - This forms **penillic acid** ($C_{16}H_{18}N_2O_4S$), which possesses two free carboxylic acid groups (at C3 and the newly generated carboxylate from the $\beta$-lactam).

### Step 3: D-Penicillamine Structure and $(R/S)$ Configuration
Treatment of the degradate with $\text{HgCl}_2$ cleaves the remaining thiazolidine-derived fragments, releasing **D-penicillamine (3-mercapto-D-valine)**:
$$\mathbf{(CH_3)_2C(SH)-CH(NH_2)-COOH}$$
- Chiral center is at C2:
  - Priority 1: $-\text{NH}_2$
  - Priority 2: $-\text{COOH}$
  - Priority 3: $-\text{C(SH)(CH}_3)_2$ (carbon bonded to sulfur)
  - Priority 4: $-\text{H}$
Assigning Cahn-Ingold-Prelog priorities reveals that natural D-penicillamine possesses the **(2S)-configuration** (derived from natural L-cysteine in the biosynthesis of the ACV tripeptide)."""
            },
            {
                "id": "prob-10-2",
                "problemNumber": "10.2",
                "title": "Strain Energy and Infrared Carbonyl Frequency Calculus in Penicillin",
                "statement": r"""In a standard planar secondary amide (such as $N$-methylacetamide), the infrared stretching frequency of the amide carbonyl is $\nu_{\text{C}=\text{O}} \approx 1650\text{ cm}^{-1}$ and the barrier to rotation is $\Delta G^\ddagger \approx 84\text{ kJ/mol}$. In penicillin G, the $\beta$-lactam carbonyl absorbs at $\nu_{\text{C}=\text{O}} \approx 1785\text{ cm}^{-1}$.
(a) Using Hooke's Law for a harmonic oscillator ($\nu = \frac{1}{2\pi c}\sqrt{k/\mu}$), calculate the ratio of the effective force constants $k_{\beta\text{-lactam}} / k_{\text{amide}}$.
(b) Explain why the dramatic increase in carbonyl stretching frequency directly reflects the loss of amide resonance energy and accounts for the high acylating reactivity toward transpeptidase enzymes.""",
                "hints": [
                    r"Hooke's law: nu is proportional to sqrt(k) if reduced mass mu is constant.",
                    r"(nu_1 / nu_2)^2 = k_1 / k_2.",
                    r"Greater double-bond character in the carbonyl increases the force constant k."
                ],
                "solution": r"""### Step 1: Force Constant Ratio Calculation
Hooke's law for the vibrational frequency of a diatomic harmonic oscillator:
$$\nu = \frac{1}{2\pi c} \sqrt{\frac{k}{\mu}}$$
Assuming the reduced mass $\mu$ of the $\text{C}=\text{O}$ unit ($\mu = \frac{m_C m_O}{m_C + m_O}$) is identical in both systems:
$$\frac{k_{\beta\text{-lactam}}}{k_{\text{amide}}} = \left(\frac{\nu_{\beta\text{-lactam}}}{\nu_{\text{amide}}}\right)^2$$
Substituting the experimental frequencies $\nu_{\beta\text{-lactam}} = 1785\text{ cm}^{-1}$ and $\nu_{\text{amide}} = 1650\text{ cm}^{-1}$:
$$\frac{k_{\beta\text{-lactam}}}{k_{\text{amide}}} = \left(\frac{1785}{1650}\right)^2 = (1.0818)^2 = \mathbf{1.170}$$
The effective force constant of the $\beta$-lactam carbonyl is **$17.0\%$ stiffer** than that of a standard amide.

### Step 2: Physical Organic Rationale
1. **Suppression of Resonance Delocalization**:
   In a normal amide, strong resonance delocalization ($-\text{C}(=\text{O})-\text{N}-\longleftrightarrow -\text{C}(\text{O}^-)=\text{N}^+-$) reduces the bond order of the $\text{C}=\text{O}$ bond from $2.0$ to $\approx 1.6$, lengthening the bond and lowering the stretching frequency to $\sim 1650\text{ cm}^{-1}$.
2. **Pyramidalization and Strain**:
   In penicillin, the bridgehead nitrogen N4 is forced into a pyramidal geometry by the fused 4-5 bicyclic ring system. Because its lone pair cannot overlap with the carbonyl $\pi^*$ orbital, amide resonance is virtually abolished.
3. **Consequences for Reactivity**:
   The $\beta$-lactam $\text{C}=\text{O}$ bond retains full, unmitigated double-bond character (bond order $\approx 2.0$, $\nu = 1785\text{ cm}^{-1}$), rendering the carbonyl carbon extraordinarily electrophilic.
   Combined with $\sim 105\text{ kJ/mol}$ of four-membered ring strain, penicillin acts as an ultra-reactive acylating agent that rapidly transfers its penicilloyl moiety onto the catalytic serine of bacterial DD-transpeptidases."""
            },
            {
                "id": "prob-10-3",
                "problemNumber": "10.3",
                "title": "Kinetic Suicide Inactivation of DD-Transpeptidase by Penicillin",
                "statement": r"""The irreversible inactivation of bacterial DD-transpeptidase (E) by penicillin (I) proceeds according to the two-step mechanism:
$$\text{E} + \text{I} \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} \text{E}\cdot\text{I} \xrightarrow{k_{\text{inact}}} \text{E-I}^* \xrightarrow{k_{\text{deacyl}}} \text{E} + \text{Products}$$
where $\text{E}\cdot\text{I}$ is the reversible Michaelis complex, $\text{E-I}^*$ is the covalent penicilloyl-enzyme intermediate, and $K_I = k_{-1} / k_1$.
(a) For a clinical strain of *S. aureus*, $K_I = 1.5\times 10^{-5}\text{ M}$, $k_{\text{inact}} = 12.0\text{ s}^{-1}$, and $k_{\text{deacyl}} = 8.0\times 10^{-7}\text{ s}^{-1}$. Calculate the second-order acylation rate constant (acylation efficiency, $k_{\text{inact}} / K_I$) in $\text{M}^{-1}\text{s}^{-1}$.
(b) Calculate the half-life ($t_{1/2}$) of the covalent acyl-enzyme complex $\text{E-I}^*$ in hours, and explain why this value classifies penicillin as a suicide inactivator.""",
                "hints": [
                    r"Acylation efficiency = k_inact / K_I.",
                    r"t_{1/2} = ln(2) / k_deacyl.",
                    r"Convert seconds to hours (1 h = 3600 s)."
                ],
                "solution": r"""### Step 1: Acylation Efficiency Calculation
The second-order rate constant of enzyme inactivation is:
$$\frac{k_{\text{inact}}}{K_I} = \frac{12.0\text{ s}^{-1}}{1.5\times 10^{-5}\text{ M}} = \mathbf{8.0\times 10^5\text{ M}^{-1}\text{s}^{-1}}$$
This high rate constant ($>10^5\text{ M}^{-1}\text{s}^{-1}$) indicates that penicillin rapidly and efficiently captures the transpeptidase active site even at sub-micromolar drug concentrations.

### Step 2: Half-Life of the Covalent Acyl-Enzyme Complex
The recovery of active enzyme requires hydrolysis of the covalent ester bond, governed by the deacylation rate constant $k_{\text{deacyl}}$:
$$t_{1/2} = \frac{\ln 2}{k_{\text{deacyl}}} = \frac{0.69315}{8.0\times 10^{-7}\text{ s}^{-1}} = 866,434\text{ s}$$
Converting to hours:
$$t_{1/2} = \frac{866,434\text{ s}}{3600\text{ s/hour}} = \mathbf{240.7\text{ hours}} \approx \mathbf{10.0\text{ days}}$$

### Step 3: Classification as a Suicide Inactivator
A suicide (mechanism-based) inactivator is an unreactive compound that binds to an enzyme active site as a normal substrate, is chemically converted by the enzyme's own catalytic mechanism into a reactive species, and irreversibly covalently traps the enzyme.
Because the half-life of the penicilloyl-transpeptidase intermediate is **over 10 days**—far exceeding the lifetime of the bacterial cell (generation time $\sim 20 - 30\text{ minutes}$)—the enzyme is irreversibly inactivated for all practical biological purposes, permanently halting cell wall crosslinking."""
            },
            {
                "id": "prob-10-4",
                "problemNumber": "10.4",
                "title": "Periodate Degradation Stoichiometry and Structural Proof of Chloramphenicol",
                "statement": r"""A $0.323\text{ g}$ sample of pure chloramphenicol ($M = 323.13\text{ g/mol}$, $1.00\text{ mmol}$) was hydrolyzed in boiling $2\text{ M HCl}$. The neutralized hydrolysate was treated with excess sodium periodate ($\text{NaIO}_4$) at room temperature.
(a) Calculate the molar equivalents of periodate consumed and write the chemical structures of all products formed.
(b) If the periodate cleavage product mixture is treated with 2,4-dinitrophenylhydrazine (2,4-DNP), calculate the mass of the resulting yellow-orange hydrazone precipitate ($M_{\text{DNP}} = 331.24\text{ g/mol}$).""",
                "hints": [
                    r"Hydrolysis yields dichloroacetic acid and 2-amino-1-(4-nitrophenyl)propane-1,3-diol.",
                    r"Periodate cleaves vicinal amino alcohols: R-CH(OH)-CH(NH2)-CH2OH.",
                    r"Periodate consumes 2 moles of HIO4 to produce p-nitrobenzaldehyde, formaldehyde, and ammonia.",
                    r"p-Nitrobenzaldehyde reacts with 2,4-DNP to form a hydrazone."
                ],
                "solution": r"""### Step 1: Hydrolysis and Periodate Cleavage Stoichiometry
1. **Acid Hydrolysis**:
   $$\text{Chloramphenicol } (1.00\text{ mmol}) + \text{H}_2\text{O} \to \text{CHCl}_2\text{COOH } (1.00\text{ mmol}) + \text{Aminodiol base } (1.00\text{ mmol})$$
   The aminodiol base is $\text{O}_2\text{N-C}_6\text{H}_4-\text{C}^1\text{H(OH)}-\text{C}^2\text{H(NH}_2)-\text{C}^3\text{H}_2\text{OH}$.
2. **Periodate Cleavage**:
   The aminodiol possesses two contiguous vicinal oxidizable bonds: C1-C2 (amino alcohol) and C2-C3 (amino alcohol):
   - Cleavage of both bonds consumes **2.0 molar equivalents of $\text{NaIO}_4$** ($2.00\text{ mmol}$).
   - Carbon-1 ($\text{Ar-CH(OH)}-$): Oxidized to **$p$-nitrobenzaldehyde ($\text{O}_2\text{N-C}_6\text{H}_4\text{CHO}$)**: $1.00\text{ mmol}$.
   - Carbon-2 ($-\text{CH(NH}_2)-$): Released as **formic acid ($\text{HCOOH}$)** and **ammonia ($\text{NH}_3$)**: $1.00\text{ mmol}$ each.
   - Carbon-3 ($-\text{CH}_2\text{OH}$): Oxidized to **formaldehyde ($\text{HCHO}$)**: $1.00\text{ mmol}$.

### Step 2: Mass of 2,4-DNP Hydrazone Precipitate
$p$-Nitrobenzaldehyde ($1.00\text{ mmol}$) reacts quantitatively with 2,4-dinitrophenylhydrazine to form the crystalline hydrazone:
$$\text{O}_2\text{N-C}_6\text{H}_4\text{CHO} + \text{H}_2\text{N-NH-C}_6\text{H}_3(\text{NO}_2)_2 \to \text{O}_2\text{N-C}_6\text{H}_4\text{CH}=\text{N-NH-C}_6\text{H}_3(\text{NO}_2)_2 + \text{H}_2\text{O}$$
Molar mass of $p$-nitrobenzaldehyde 2,4-dinitrophenylhydrazone:
$$M = 331.24\text{ g/mol}$$
Mass of precipitate:
$$m = 1.00\times 10^{-3}\text{ mol} \times 331.24\text{ g/mol} = 0.3312\text{ g} = \mathbf{331.2\text{ mg}}$$
Isolation of $331.2\text{ mg}$ of this hydrazone provides quantitative proof of the $p$-nitrophenyl group and the contiguous propanediol backbone."""
            },
            {
                "id": "prob-10-5",
                "problemNumber": "10.5",
                "title": "Total Synthesis of Chloramphenicol: MPV Reduction Stereoselectivity",
                "statement": r"""In the Long-Troutman commercial synthesis of chloramphenicol, the key stereocenter-generating step is the Meerwein-Ponndorf-Verley (MPV) reduction of $p$-nitro-$\alpha$-acetamido-$\beta$-hydroxypropiophenone:
$$\text{O}_2\text{N-C}_6\text{H}_4\text{-CO-CH(NHAc)-CH}_2\text{OH} \xrightarrow{\text{Al(O-}i\text{Pr)}_3, \text{ } i\text{PrOH}} (\pm)\text{-threo product } (80\%) + (\pm)\text{-erythro product } (20\%)$$
(a) Draw the six-membered cyclic transition state for the MPV reduction, showing the coordination of the aluminum atom to both the ketone carbonyl and the adjacent functional group.
(b) Explain why the cyclic transition state selectively favors the threo diastereomer over the erythro diastereomer.""",
                "hints": [
                    r"MPV reduction proceeds via a chair-like six-membered cyclic transition state.",
                    r"Aluminum coordinates to the carbonyl oxygen and isopropoxide hydride donor.",
                    r"Chelation with the acetamido or hydroxymethyl group locks the conformation."
                ],
                "solution": r"""### Step 1: Six-Membered Cyclic Transition State
In the Meerwein-Ponndorf-Verley (MPV) reduction:
1. The Lewis acidic aluminum atom of $\text{Al(O-}i\text{Pr)}_3$ coordinates simultaneously to the ketone carbonyl oxygen and the adjacent $\alpha$-acetamido carbonyl/hydroxymethyl oxygen in a stable bidentate chelate complex.
2. A six-membered chair-like transition state is established involving the ketone carbon, ketone oxygen, aluminum atom, isopropoxide oxygen, isopropoxide $\alpha$-carbon, and the migrating hydride:
   $$\text{C}_{\text{ketone}} - \text{O} - \text{Al} - \text{O} - \text{C}_{i\text{Pr}} - \text{H} \cdots \text{C}_{\text{ketone}}$$

### Step 2: Rationale for Threo Diastereoselectivity
1. **Facial Hydride Transfer**:
   Hydride ($H^-$) is transferred directly from the isopropoxide $\alpha$-carbon to the ketone carbon within the rigid chelate.
2. **Steric Minimization**:
   In the competing chair-like transition states:
   - In the **threo-forming transition state**, the bulky $p$-nitrophenyl group ($\text{Ar}$) and the $\alpha$-acetamido group ($-\text{NHAc}$) orient into **equatorial-like, pseudo-trans positions**, minimizing 1,3-diaxial steric repulsions with the remaining bulky isopropoxide ligands on aluminum.
   - In the erythro-forming transition state, the bulky aryl group is forced into a sterically congested pseudo-axial orientation, resulting in severe steric clash.
3. **Outcome**:
   Hydride transfer occurs preferentially from the face that produces the **$(\pm)$-threo diastereomer in an 80:20 ratio**, allowing efficient industrial access to the natural antibiotic framework."""
            },
            {
                "id": "prob-10-6",
                "problemNumber": "10.6",
                "title": "Clavulanic Acid Mechanism-Based Suicide Inhibition of Serine $\\beta$-Lactamases",
                "statement": r"""Clavulanic acid is an oxapenam secondary metabolite produced by *Streptomyces clavuligerus*.
(a) Compare the structure of clavulanic acid to penicillin G, highlighting the three key differences in the ring heteroatoms and substitution.
(b) Write the mechanism-based suicide inhibition cascade when clavulanic acid is attacked by the active-site serine of a class A $\beta$-lactamase (TEM-1), showing:
1. Acylation of Ser70 and $\beta$-lactam ring opening.
2. Transient oxazolidine ring opening and generation of a reactive conjugated imine.
3. Secondary irreversible nucleophilic trapping by an active-site crosslinking residue.""",
                "hints": [
                    r"Clavulanic acid has an oxygen in place of sulfur (oxapenam).",
                    r"It lacks an acylamino side chain at C6.",
                    r"It has an exocyclic hydroxyethylidene double bond at C2.",
                    r"Oxazolidine ring opening forms an alpha,beta-unsaturated imine that covalently crosslinks."
                ],
                "solution": r"""### Step 1: Structural Comparison (Clavulanic Acid vs Penicillin G)
1. **Heteroatom Replacement**: Clavulanic acid contains an **oxygen atom** in the five-membered ring instead of sulfur (an **oxapenam** rather than a penam core).
2. **Absence of C6 Side Chain**: Clavulanic acid has **zero acylamino side chain at C6** (only a hydrogen atom).
3. **Exocyclic Double Bond**: In place of the gem-dimethyl groups of penicillin at C2, clavulanic acid possesses a $(2R, 5R)$-configured ring with an **exocyclic hydroxyethylidene substituent** ($=\text{CH-CH}_2\text{OH}$).

### Step 2: Inactivation Mechanism of TEM-1 $\beta$-Lactamase
1. **Initial Acylation**:
   The catalytic Ser70 nucleophile attacks the $\beta$-lactam carbonyl carbon, opening the 4-membered ring to form the standard acyl-enzyme intermediate:
   $$\text{Enz-Ser70-O-CO}-\cdots$$
2. **Oxazolidine Ring Opening and Imine Formation**:
   Because oxygen is more electronegative than sulfur and a better leaving group, the five-membered oxapenam ring spontaneously opens:
   - The ring oxygen departs as an enolate/alkoxide.
   - This unmasks a highly reactive **conjugated $\alpha,\beta$-unsaturated imine intermediate** covalently tethered to Ser70.
3. **Irreversible Crosslinking and Trapping**:
   The conjugated imine is a powerful Michael acceptor. An adjacent active-site nucleophile (such as the amino group of Lys73 or Ser130) attacks the imine carbon in an irreversible secondary addition:
   - This crosslinks the inhibitor covalently between two separate catalytic residues of the $\beta$-lactamase active site.
   - The enzyme is permanently inactivated (suicide inhibition), protecting co-administered amoxicillin from hydrolysis."""
            },
            {
                "id": "prob-10-7",
                "problemNumber": "10.7",
                "title": "Macrolide Lactone Ring Conformation and Ribosomal 50S Peptidyl Transferase Binding",
                "statement": r"""Erythromycin A ($C_{37}H_{67}NO_{13}$) is a 14-membered macrolide antibiotic produced by *Saccharopolyspora erythraea*.
(a) Describe the chemical structure of erythromycin A, identifying the aglycone (erythronolide A, a 14-membered macrolactone ring) and the two glycosidically linked sugars (desosamine and cladinose).
(b) Cryo-EM and X-ray crystallographic studies demonstrate that erythromycin binds to the 23S rRNA in the nascent peptide exit tunnel (NPET) of the bacterial 50S ribosomal subunit. The dissociation constant is $K_d = 1.0\times 10^{-8}\text{ M}$ at $310\text{ K}$. Calculate the standard Gibbs free energy of binding $\Delta G^\circ_{\text{bind}}$.
(c) Explain why methylation of adenine A2058 in 23S rRNA by the Erm methyltransferase confers high-level macrolide resistance.""",
                "hints": [
                    r"\Delta G^\circ = RT \ln K_d.",
                    r"Desosamine is an amino sugar; cladinose is a neutral sugar.",
                    r"Methylation of A2058 introduces steric clash with the desosamine dimethylamino group."
                ],
                "solution": r"""### Step 1: Structural Anatomy of Erythromycin A
1. **Aglycone (Erythronolide A)**:
   A 14-membered polyketide **macrolactone ring** containing 10 stereocenters, synthesized by a modular Type I polyketide synthase (6 modules, DEBS).
2. **Sugar Substituents**:
   - Linked at C3: **L-Cladinose** (a neutral, methylated deoxysugar).
   - Linked at C5: **D-Desosamine** (a basic 3-dimethylamino-3,4,6-trideoxyhexose). The basic dimethylamino group ($-\text{NMe}_2$) confers amphiphilic character and is protonated at physiological pH.

### Step 2: Gibbs Free Energy of Ribosomal Binding
At $T = 310.15\text{ K}$ ($37^\circ\text{C}$):
$$\Delta G^\circ_{\text{bind}} = -R T \ln K_a = +R T \ln K_d$$
Given $K_d = 1.0\times 10^{-8}\text{ M}$:
$$\Delta G^\circ_{\text{bind}} = (8.314\text{ J/(mol}\cdot\text{K)})(310.15\text{ K}) \ln(1.0\times 10^{-8})$$
$$\Delta G^\circ_{\text{bind}} = 2578.6 \times (-18.4207) = -47,499\text{ J/mol} = \mathbf{-47.5\text{ kJ/mol}}$$
The binding is strongly spontaneous, equivalent to $\approx 8 - 10$ cooperative hydrogen bonds and hydrophobic contact interactions.

### Step 3: Molecular Mechanism of Erm Resistance
1. **Binding Geometry**:
   Inside the nascent peptide exit tunnel (NPET), erythromycin binds adjacent to the peptidyl transferase center. The basic desosamine sugar forms critical hydrogen bonds with the $N6$ and $N1$ positions of nucleotide **A2058** of 23S rRNA.
2. **Erm Methylation**:
   Erm (erythromycin ribosome methylation) methyltransferases catalyze mono- or di-methylation of the exocyclic $N6$-amino group of adenine **A2058**:
   $$\text{A2058} \xrightarrow{\text{Erm, SAM}} N6,N6\text{-dimethyl-A2058}$$
3. **Steric Clash**:
   The two bulky methyl groups on the $N6$ of A2058 project directly into the tunnel cavity, creating a severe steric clash with the desosamine sugar of erythromycin.
   This decreases macrolide binding affinity by over **10,000-fold** ($K_d > 10^{-4}\text{ M}$), rendering the bacterium completely resistant to all macrolides, lincosamides, and streptogramin B antibiotics ($MLS_B$ phenotype)."""
            }
        ]
    }
    units.append(u10)

    return units

if __name__ == "__main__":
    u = get_units_7_8_9_10()
    print(f"Successfully generated Units 7-10. Total units: {len(u)}")
    for unit in u:
        print(f"  {unit['id']}: {len(unit['sections'])} sections, {len(unit['problems'])} problems")
