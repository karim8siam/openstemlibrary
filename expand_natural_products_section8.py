#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
expand_natural_products_section8.py
Appends Section 8 to all 10 units of Chemistry of Natural Products.
Strictly zero course numbers, codes, or marks.
Raw triple quotes used throughout to prevent any escape sequence issues.
"""

def add_section8_to_units(units):
    sec8_dict = {
        "unit-1": {
            "id": "sec-1-8",
            "secNumber": "1.8",
            "title": "The Polyketide Synthase (PKS) Pathway: Modular Assembly & Macrolide Architectures",
            "content": r"""The polyketide synthase (PKS) pathway assembles one of the most structurally diverse and pharmacologically potent superfamilies of natural products, including macrolide antibiotics (erythromycin), immunosuppressants (rapamycin, FK506), and polyketide polyethers (monensin).

### Mechanistic Principles: Decarboxylative Claisen Condensation
Polyketides are biosynthesized by iterative condensations of simple carboxylic acid thioesters, mimicking fatty acid synthesis:
1. **Starter and Extender Units**:
   - Starter units: Acetyl-CoA, propionyl-CoA, benzoyl-CoA.
   - Extender units: Malonyl-CoA, methylmalonyl-CoA, ethylmalonyl-CoA.
2. **Chain Extension Cycle**:
   The ketoacyl synthase (KS) domain catalyzes a decarboxylative Claisen condensation between the growing polyketide chain tethered to the acyl carrier protein (ACP) and an incoming extender unit:
   $$\text{R-COS-KS} + \text{HOOC-CH(R}^\prime\text{)-COS-ACP} \xrightarrow{\text{KS}} \text{R-CO-CH(R}^\prime\text{)-COS-ACP} + \text{CO}_2 + \text{HS-KS}$$

### Architecture of Modular Type I PKS Enzymes
Type I modular PKSs (e.g., 6-deoxyerythronolide B synthase, DEBS) operate as gigantic, multifunctional molecular assembly lines where each successive elongation cycle is carried out by a dedicated, distinct catalytic **module**:
- **Minimal Core**: Every elongating module contains at least three mandatory domains:
  - **KS (Ketosynthase)**: Catalyzes C-C bond formation.
  - **AT (Acyltransferase)**: Selects and loads the specific extender unit onto the ACP.
  - **ACP (Acyl Carrier Protein)**: Transports the growing intermediate via a phosphopantetheine swinging arm ($20\text{ \AA}$ long).
- **Reductive Modification Loop**: The $\beta$-keto group formed by condensation can undergo programmed, variable reduction:
  - If no reductive domains: The $\beta$-ketone ($\text{C}=\text{O}$) is retained.
  - **KR (Ketoreductase)**: Reduces ketone to a $\beta$-hydroxyl group ($-\text{CH(OH)}-$).
  - **DH (Dehydratase)**: Dehydrates $\beta$-hydroxyacyl to an $\alpha,\beta$-unsaturated trans-alkene ($-\text{CH}=\text{CH}-$).
  - **ER (Enoylreductase)**: Reduces the double bond with NADPH to a fully saturated methylene ($-\text{CH}_2-\text{CH}_2-$).
- **Termination and Cyclization**:
  The final module terminates with a **Thioesterase (TE)** domain, which catalyzes intramolecular nucleophilic attack of a distal hydroxyl group onto the terminal thioester, releasing the polyketide as a macrocyclic lactone (macrolide)."""
        },
        "unit-2": {
            "id": "sec-2-8",
            "secNumber": "2.8",
            "title": "Terpenoid Fragrance Conversions: Citral to Ionones, Vitamin A & Menthol",
            "content": r"""The acyclic monoterpenoid citral serves as an indispensable industrial raw material for fine fragrance aroma chemicals and the total synthesis of vitamins.

### Conversion of Citral to Pseudoionone and Ionones
1. **Base-Catalyzed Condensation**:
   Citral condenses with acetone in aqueous alkali or barium hydroxide to form pseudoionone:
   $$(\text{CH}_3)_2\text{C}=\text{CH}(\text{CH}_2)_2\text{C}(\text{CH}_3)=\text{CH-CHO} + \text{CH}_3\text{COCH}_3 \xrightarrow{\text{OH}^-} \text{Pseudoionone} + \text{H}_2\text{O}$$
2. **Regioselective Acidic Cyclization**:
   Pseudoionone undergoes electrophilic cyclization upon acid treatment:
   - With concentrated sulfuric acid ($\text{H}_2\text{SO}_4$) at $40–50^\circ\text{C}$: Thermodynamically controlled cyclization gives **$\beta$-ionone** ($80\%$), where the double bond is fully conjugated with the side chain enone. $\beta$-Ionone is the key $C_{13}$ building block for **Vitamin A (retinol)** and $\beta$-carotene synthesis (Roche / BASF industrial routes).
   - With dilute phosphoric acid ($\text{H}_3\text{PO}_4$) or boron trifluoride ($\text{BF}_3$): Kinetically controlled cyclization yields **$\alpha$-ionone** ($90\%$), displaying a delicate, natural violet floral odor.

### Synthesis of (-)-Menthol from Citral and Myrcene
Industrial production of $(-)$-menthol ($3,000\text{ tons/year}$) utilizes either:
- **Haarmann & Reimer Route**: m-Cresol is propylated to thymol, followed by catalytic hydrogenation to racemic menthol stereoisomers and fractional distillation.
- **Takasago Asymmetric Route**: Myrcene is converted into $N,N$-diethylgeranylamine, followed by Noyori asymmetric isomerization ($[Rh((S)\text{-BINAP})]^+$, $99\%\text{ ee}$) to $(R)$-citronellal enamine, cyclization with $\text{ZnBr}_2$ to $(-)$-isopulegol, and final catalytic hydrogenation to enantiopure **$(-)$-menthol**."""
        },
        "unit-3": {
            "id": "sec-3-8",
            "secNumber": "3.8",
            "title": "Higher Terpenes: Taxol, Abietic Acid, Lupeol & Carotenoid Photochemistry",
            "content": r"""Higher terpenoids—diterpenes ($C_{20}$), triterpenes ($C_{30}$), and tetraterpenes ($C_{40}$)—exhibit complex architectures and diverse biological functions.

### Diterpenes ($C_{20}$)
1. **Paclitaxel (Taxol)**:
   A complex polyoxygenated diterpene isolated from the Pacific yew (*Taxus brevifolia*). Contains a fused 6-8-6 tricyclic carbon core with a bridgehead oxetane ring and an $N$-benzoylphenylisoserine side chain. Mechanistically, Taxol binds $\beta$-tubulin and stabilizes microtubules against depolymerization, arresting cancer cells in the $G_2/M$ phase of the cell cycle.
2. **Abietic Acid**:
   The primary tricyclic diterpene acid of pine rosin (*Pinus palustris*), possessing a fused phenanthrene-like core with conjugated diene double bonds that undergo Diels-Alder additions with maleic anhydride to yield industrial paper sizing agents.

### Pentacyclic Triterpenes ($C_{30}$): Lupeol and Oleanolic Acid
Derived from squalene via the lupenyl or dammarenyl carbocation intermediate, featuring five fused rings (lupane, oleanane, ursane frameworks). Lupeol exhibits anti-inflammatory, antioxidant, and wound-healing properties by modulating NF-$\kappa$B signaling.

### Tetraterpenes ($C_{40}$): Carotenoid Photochemistry
Formed by tail-to-tail dimerization of two geranylgeranyl pyrophosphate (GGPP) molecules into phytoene, followed by four desaturation steps to lycopene and end-ring cyclization to $\beta$-carotene.
- **Photoprotective Energy Transfer**: The 11 conjugated double bonds absorb strongly in the blue ($\lambda_{\text{max}} = 450 - 480\text{ nm}$).
- They protect the photosynthetic apparatus by intercepting excited triplet chlorophyll ($^3\text{Chl}^*$) and directly quenching singlet oxygen ($^1\text{O}_2$) at diffusion-controlled rates without undergoing chemical degradation."""
        },
        "unit-4": {
            "id": "sec-4-8",
            "secNumber": "4.8",
            "title": "Monosaccharide Reactions: Glycoside Synthesis, Periodate & Bromine Oxidations",
            "content": r"""The multiple hydroxyl groups and latent carbonyl functionality of monosaccharides exhibit distinct chemical reactivities toward selective chemical reagents.

### Glycoside Formation (Fischer Glycosidation)
Refluxing a monosaccharide with an alcohol in the presence of an anhydrous acid catalyst ($\text{HCl}$ gas, $1\%$) converts the hemiacetal into an acetal (**glycoside**):
$$\text{D-Glucose} + \text{MeOH} \xrightarrow{\text{HCl}, \Delta} \text{Methyl }\alpha\text{-D-glucopyranoside} + \text{Methyl }\beta\text{-D-glucopyranoside} + \text{H}_2\text{O}$$
- Glycosides do **not mutarotate** in neutral solution and are resistant to Fehling's/Tollens' oxidation because the anomeric carbon is locked in an acetal bond.
- Glycosidic bonds are stable to alkali, but undergo rapid acid-catalyzed hydrolysis back to the parent monosaccharide.

### Selective Bromine Water Oxidation (Aldoses to Aldonic Acids)
Bromine water ($\text{Br}_2 / \text{H}_2\text{O}$) buffered with sodium carbonate is a selective, mild oxidizing agent that oxidizes aldoses cleanly into **aldonic acids** without affecting ketoses or primary alcohols:
$$\text{R-CHO} + \text{Br}_2 + \text{H}_2\text{O} \to \text{R-COOH} + 2\text{ HBr}$$
Mechanistically, bromine water selectively oxidizes the **$\beta$-pyranose anomer** via axial hydride transfer from C1 to bromine, occurring up to 250 times faster than oxidation of the $\alpha$-anomer.

### Malaprade Periodate Oxidation in Carbohydrate Analysis
Periodic acid ($\text{HIO}_4$) cleaves contiguous carbon-carbon bonds bearing vicinal diols, $\alpha$-hydroxycarbonyls, or amino alcohols. Quantifying periodate consumption, formic acid production, and formaldehyde release establishes:
- The ring size of glycosides (pyranose vs furanose).
- The linkage position in oligosaccharides.
- The degree of polymerization ($DP$) of linear glycans."""
        },
        "unit-5": {
            "id": "sec-5-8",
            "secNumber": "5.8",
            "title": "Structural Glycobiology: Glycogen, Chitin, Heparin & Peptidoglycans",
            "content": r"""Beyond starch and cellulose, complex polysaccharides fulfill vital structural, storage, and anticoagulation functions across biological kingdoms.

### Glycogen: The Animal Energy Reserve
- Homopolymer of D-glucopyranose with $\alpha$-(1$\to$4) backbone and $\alpha$-(1$\to$6) branch points.
- Differs from plant amylopectin by its **much higher degree of branching**: branch points occur every **8 to 12 residues**.
- This branched spherical architecture produces a high surface density of non-reducing ends, allowing glycogen phosphorylase to rapidly release glucose 1-phosphate during muscle exertion or hypoglycemia.

### Chitin: Structural Exoskeleton of Arthropods
- Linear homopolymer of **$N$-acetyl-D-glucosamine (NAG)** linked by **$\beta$-(1$\to$4)-glycosidic bonds**.
- Structurally identical to cellulose, with the C2 hydroxyl replaced by an acetamido group ($-\text{NHCOCH}_3$).
- Forms antiparallel $\alpha$-chitin microfibrils stabilized by intra- and inter-chain hydrogen bonds between amide groups ($\text{N-H}\cdots\text{O}=\text{C}$), providing hardness and mechanical rigidity to crab shells, insect cuticles, and fungal cell walls.

### Heparin and Glycosaminoglycans (GAGs)
- Highly sulfated linear glycosaminoglycan consisting of repeating disaccharide units of sulfated D-glucosamine and D-glucuronic or L-iduronic acid.
- Heparin carries the highest negative charge density of any known biological macromolecule.
- Mechanism: Binds with high affinity to the plasma protease inhibitor **antithrombin III (ATIII)** via a specific pentasaccharide sequence, inducing a conformational change that accelerates antithrombin inhibition of thrombin and factor Xa by $>1,000$-fold, preventing blood clotting."""
        },
        "unit-6": {
            "id": "sec-6-8",
            "secNumber": "6.8",
            "title": "Protein Folding: Anfinsen's Dogma, Disulfide Pairing & Chaperones",
            "content": r"""The spontaneous self-assembly of a linear polypeptide into a biologically functional tertiary structure represents a central triumph of molecular thermodynamics.

### Anfinsen's Dogma (Thermodynamic Hypothesis)
Christian Anfinsen (1972 Nobel Prize) demonstrated using bovine pancreatic ribonuclease A (124 residues, 4 native disulfide bridges) that:
1. Denaturing ribonuclease in $8\text{ M urea}$ containing $\beta$-mercaptoethanol completely unfolds the protein and reduces all 4 disulfide bonds (loss of enzymatic activity).
2. Removing urea and mercaptoethanol by dialysis under aerobic conditions allowed the protein to **spontaneously refold into its native, catalytically active conformation** with $100\%$ recovery of activity.
3. If re-oxidation was conducted in the presence of $8\text{ M urea}$, the 8 cysteine residues paired randomly into 105 possible scrambled disulfide combinations, yielding $<1\%$ enzymatic activity. Subsequent addition of catalytic trace mercaptoethanol restored native folding.
**Anfinsen's Conclusion**: The native three-dimensional conformation of a protein is encoded entirely in its primary amino acid sequence and represents the **global thermodynamic free energy minimum** ($\Delta G^\circ_{\text{fold}} < 0$).

### Levinthal's Paradox and Folding Funnels
Cyrus Levinthal calculated that if an unfolded 100-residue protein sampled all possible conformations randomly ($3^{200} \approx 10^{95}$ states at $10^{-13}\text{ s}$ per state), finding the native state would take $10^{75}$ years!
- Proteins resolve this paradox by folding along a **cooperative energy landscape (folding funnel)**:
- Local secondary structural elements form rapidly ($10^{-6}\text{ s}$), guiding the polypeptide down a funnel of decreasing free energy through molten globule intermediates into the native minimum within milliseconds to seconds.

### Molecular Chaperones
In the crowded cellular cytoplasm ($300\text{ mg/mL}$ protein), exposed hydrophobic patches of nascent folding intermediates risk irreversible aggregation. Heat shock proteins (Hsp70, GroEL/GroES chaperonins) bind exposed hydrophobic surfaces in an ATP-dependent cycle, isolating the folding polypeptide inside a hydrophilic chamber to allow safe folding without aggregation."""
        },
        "unit-7": {
            "id": "sec-7-8",
            "secNumber": "7.8",
            "title": "Chemical Synthesis of Oligonucleotides: Phosphoramidite Technology",
            "content": r"""Modern genomics, PCR diagnostics, and synthetic biology rely on the automated chemical synthesis of defined single-stranded DNA and RNA oligonucleotides via solid-phase phosphoramidite chemistry.

### The Standard Phosphoramidite Cycle
Synthesized in the $3^\prime \to 5^\prime$ direction on controlled-pore glass (CPG) solid support:
1. **Detritylation (Deblocking)**:
   The 5'-dimethoxytrityl (DMT) ether is cleaved with $3\%$ trichloroacetic acid (TCA) in dichloromethane, releasing the orange $\text{DMT}^+$ trityl cation and unmasking the reactive 5'-OH group. Spectrophotometric measurement of $\text{DMT}^+$ at $498\text{ nm}$ provides real-time monitoring of stepwise cycle yields.
2. **Coupling (Chain Elongation)**:
   The incoming monomer (a 5'-DMT-2'-deoxynucleoside-3'-O-($\beta$-cyanoethyl-$N,N$-diisopropyl) phosphoramidite) is mixed with **1H-tetrazole** (or 5-ethylthiotetrazole):
   - Tetrazole protonates the diisopropylamino leaving group.
   - The nucleophilic 5'-OH of the solid-supported chain attacks the activated phosphite phosphorus, forming an internucleotide phosphite triester linkage in $>99.5\%$ yield within 60 seconds.
3. **Capping**:
   Unreacted 5'-OH groups ($<0.5\%$) are acetylated using acetic anhydride and 1-methylimidazole (NMI), terminating failed chains and preventing deletion mutations ($N-1$ sequences).
4. **Oxidation**:
   The unstable trivalent phosphite triester ($\text{P}^{\text{III}}$) is oxidized to a stable pentavalent phosphate triester ($\text{P}^{\text{V}}=\text{O}$) using aqueous iodine in pyridine/THF.

### Final Deprotection and Cleavage
After assembling the desired sequence:
- The oligonucleotide is cleaved from the CPG support and the cyanoethyl protecting groups on phosphate are removed using concentrated aqueous ammonium hydroxide ($28\%\text{ NH}_4\text{OH}$) at $55^\circ\text{C}$.
- Basic treatment also hydrolyzes the exocyclic amino protecting groups (benzoyl on A and C; isobutyryl on G).
- The crude oligonucleotide is purified by reversed-phase HPLC or polyacrylamide gel electrophoresis (PAGE)."""
        },
        "unit-8": {
            "id": "sec-8-8",
            "secNumber": "8.8",
            "title": "Indole & Cinchona Alkaloids: Quinine, Reserpine, Strychnine & Antimalarial Action",
            "content": r"""Complex heterocyclic alkaloids originating from L-tryptophan encompass some of the most intricate molecular architectures and historic pharmacophores known.

### Cinchona Alkaloids: Quinine
Isolated from the bark of the *Cinchona calisaya* tree by Pelletier and Caventou in 1820:
- Contains a quinoline ring linked through a secondary carbinol carbon to a bicyclic **quinuclidine ring**.
- Quinine is the $(8S, 9R)$ stereoisomer; its $(8R, 9S)$ diastereomer is quinidine (a cardiac antiarrhythmic).
- **Mechanism of Antimalarial Action**: The intraerythrocytic malaria parasite (*Plasmodium falciparum*) digests host hemoglobin inside its acidic digestive vacuole, releasing free cytotoxic ferriprotoporphyrin IX (heme). The parasite polymerizes heme into insoluble, non-toxic hemozoin crystals ('malaria pigment'). Quinine caps growing hemozoin crystals, accumulating toxic soluble heme that lyses parasitic membranes.

### Indole Alkaloids: Reserpine and Strychnine
1. **Reserpine**: Isolated from Indian snakeroot (*Rauvolfia serpentina*). A pentacyclic indole alkaloid that irreversibly inhibits the vesicular monoamine transporter 2 (VMAT2), depleting dopamine, norepinephrine, and serotonin in the central nervous system; historically the first major antihypertensive and antipsychotic therapeutic.
2. **Strychnine**: Isolated from seeds of *Strychnos nux-vomica*. A heptacyclic indole alkaloid featuring 6 asymmetric carbons assembled around a cage-like framework. Robert Woodward completed its landmark total synthesis in 1954. Strychnine acts as a potent competitive antagonist of the inhibitory glycine receptor ($GlyR$) in the spinal cord, causing uncontrolled motor neuron firing, violent tetanic convulsions, and respiratory arrest."""
        },
        "unit-9": {
            "id": "sec-9-8",
            "secNumber": "9.8",
            "title": "Steroid Biosynthesis & Hormonal Steroids: Cholesterol to Steroid Hormones",
            "content": r"""In mammals, cholesterol serves as the common biosynthetic progenitor of all steroid hormones, functioning as chemical messengers that regulate electrolyte balance, carbohydrate metabolism, and reproductive physiology.

### Enzymatic Cleavage: Cholesterol to Pregnenolone
The committed, rate-limiting step of all steroid hormone biosynthesis takes place in the inner mitochondrial membrane, catalyzed by **cytochrome P450 side-chain cleavage enzyme (CYP11A1 / P450scc)**:
$$\text{Cholesterol } (C_{27}) + 3\text{ NADPH} + 3\text{ H}^+ + 3\text{ O}_2 \xrightarrow{\text{P450scc}} \text{Pregnenolone } (C_{21}) + \text{Isocaproaldehyde } (C_6) + 3\text{ NADP}^+ + 4\text{ H}_2\text{O}$$
The enzyme carries out two successive hydroxylations at C22 and C20 followed by oxidative C20-C22 carbon-carbon bond cleavage.

### Downstream Biosynthetic Divergence
1. **Progestagens (Progesterone, $C_{21}$)**:
   Oxidation of the $3\beta$-hydroxyl of pregnenolone by $3\beta$-hydroxysteroid dehydrogenase ($3\beta$-HSD) followed by $\Delta^5 \to \Delta^4$ double-bond isomerization affords progesterone, the hormone sustaining pregnancy.
2. **Corticosteroids ($C_{21}$)**:
   - **Mineralocorticoids (Aldosterone)**: Produced in the adrenal zona glomerulosa; regulates renal $\text{Na}^+$ reabsorption and $\text{K}^+$ excretion.
   - **Glucocorticoids (Cortisol)**: Produced in the adrenal zona fasciculata; promotes gluconeogenesis, suppresses inflammatory immune cascades, and mediates stress responses.
3. **Androgens (Testosterone, $C_{19}$)**:
   Progesterone undergoes C17 $\alpha$-hydroxylation and C17-C20 cleavage catalyzed by CYP17A1 (17,20-lyase), followed by $17\beta$-reduction to afford testosterone.
4. **Estrogens (Estradiol, $C_{18}$)**:
   Aromatase (CYP19A1) catalyzes the oxidative loss of the C19 angular methyl group and aromatization of Ring A, converting testosterone into **$17\beta$-estradiol**, characterized by a planar phenolic Ring A."""
        },
        "unit-10": {
            "id": "sec-10-8",
            "secNumber": "10.8",
            "title": "Non-Beta-Lactam Antibiotic Classes: Macrolides, Tetracyclines & Glycopeptides",
            "content": r"""Beyond $\beta$-lactams, natural antibiotics produced by soil actinomycetes target other fundamental bacterial survival machineries.

### 1. Macrolides (Erythromycin, Azithromycin)
- **Structure**: 14- or 15-membered polyketide macrolactone rings substituted with amino and neutral deoxysugars.
- **Target**: Bind reversibly to 23S rRNA in the 50S ribosomal subunit at the nascent peptide exit tunnel.
- **Mechanism**: Physically obstruct the elongation of nascent polypeptide chains, causing premature peptidyl-tRNA drop-off (bacteriostatic).

### 2. Tetracyclines (Chlortetracycline, Doxycycline)
- **Structure**: Polyketides featuring four linearly fused six-membered rings (naphthacene carboxamide core) rich in keto-enol systems that chelate divalent metal ions ($Mg^{2+}, Ca^{2+}$).
- **Target**: Bind to the 30S ribosomal subunit.
- **Mechanism**: Sterically block the access of incoming aminoacyl-tRNA to the ribosomal A-site, arresting translation elongation.

### 3. Aminoglycosides (Streptomycin, Kanamycin, Gentamicin)
- **Structure**: Complex pseudooligosaccharides containing amino-modified cyclitols (streptamine or 2-deoxystreptamine) glycosidically linked to amino sugars.
- **Target**: Bind specifically to the decoding region of 16S rRNA in the 30S ribosomal subunit.
- **Mechanism**: Induce codon-anticodon misreading, generating mistranslated, aberrant proteins that insert into the cell membrane, inducing membrane depolarization and rapid bacterial lysis (bactericidal).

### 4. Glycopeptides (Vancomycin)
- **Structure**: Massive heptapeptide core crosslinked by aryl-aryl and biaryl ether bonds, substituted with disaccharide units.
- **Mechanism**: Unlike $\beta$-lactams which inhibit enzymes, vancomycin binds directly to the **substrate**: it forms a five-point hydrogen-bonding complex with the terminal **$D\text{-Ala}-D\text{-Ala}$** dipeptide of peptidoglycan precursors, sterically blocking transglycosylases and transpeptidases. Vancomycin-resistant enterococci (VRE) mutate the terminal dipeptide to $D\text{-Ala}-D\text{-Lac}$, eliminating a key hydrogen bond and reducing affinity by 1,000-fold."""
        }
    }

    for u in units:
        uid = u["id"]
        if uid in sec8_dict:
            u["sections"].append(sec8_dict[uid])

    return units

if __name__ == "__main__":
    from build_natural_products_units_1_2_3 import get_units_1_2_3
    from build_natural_products_units_4_5_6 import get_units_4_5_6
    from build_natural_products_units_7_8_9_10 import get_units_7_8_9_10

    all_u = get_units_1_2_3() + get_units_4_5_6() + get_units_7_8_9_10()
    add_section8_to_units(all_u)
    print("Verification of Section 8 across all units:")
    for u in all_u:
        print(f"  {u['id']}: total sections = {len(u['sections'])}")
