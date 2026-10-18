# expand_org1_part10.py
# Problem 8 (Advanced Retrosynthetic Analysis & Multi-Step Total Synthesis) for all 8 units
# Brings organic-chemistry-1-data.js to >66,000 words!

def expand_retrosynthesis_mastery(units):
    u1, u2, u3, u4, u5, u6, u7, u8 = units

    # Unit 1 Problem 8
    u1["problems"].append({
        "id": "p1_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Quantum Resonance Energy of the Cyclopentadienyl Cation vs Tropylium Cation",
        "question": "Calculate and contrast the total pi-electron energy E_pi and aromatic stabilization/destabilization of: (1) The cyclopentadienyl cation (C5H5+, 4 pi electrons) using the Frost circle polygon method. (2) The cycloheptatrienyl cation (tropylium, C7H7+, 6 pi electrons). (3) Explain why cycloheptatriene has a pKa of 36, whereas cyclopentadiene has a pKa of 16 (a difference of 20 orders of magnitude!), inverting normal hydrocarbon acidity patterns.",
        "solution": r"""#### Part 1: Frost Circle Calculation for Cyclopentadienyl Cation ($C_5H_5^+$)
Using the Frost circle inscribed inside a circle of radius $2|\beta|$ with a vertex pointing down:
1. The five molecular orbital energy levels are given by:
   $$\varepsilon_k = \alpha + 2\beta \cos\left(\frac{2\pi k}{5}\right), \quad k = 0, 1, 2, 3, 4 \tag{1}$$
   - $k=0$: $\varepsilon_0 = \alpha + 2\beta \cos(0) = \alpha + 2.000\beta$ (Bonding)
   - $k=1, 4$: $\varepsilon_1 = \varepsilon_4 = \alpha + 2\beta \cos(72^\circ) = \alpha + 0.618\beta$ (Bonding, degenerate pair)
   - $k=2, 3$: $\varepsilon_2 = \varepsilon_3 = \alpha + 2\beta \cos(144^\circ) = \alpha - 1.618\beta$ (Antibonding, degenerate pair)
2. Populating the four $\pi$ electrons according to Hund's rule:
   - Two electrons in $\varepsilon_0$: $2(\alpha + 2.000\beta)$
   - One electron in $\varepsilon_1$ and one electron in $\varepsilon_4$ with parallel spins (triplet ground state!):
     $$E_\pi(\text{C}_5\text{H}_5^+) = 2(\alpha + 2.000\beta) + 2(\alpha + 0.618\beta) = \mathbf{4\alpha + 5.236\beta} \tag{2}$$
3. Reference: Two isolated double bonds ($4\alpha + 4.000\beta$):
   $$\text{Delocalization Energy} = 1.236\beta$$
   However, planar $D_{5h}$ geometry suffers from open-shell diradical character, undergoing first-order **Jahn-Teller distortion** to break degeneracy, resulting in severe **antiaromatic destabilization**!

#### Part 2: Frost Circle Calculation for Tropylium Cation ($C_7H_7^+$)
Inscribing a regular heptagon with a vertex down:
1. Energy levels: $\varepsilon_k = \alpha + 2\beta \cos(2\pi k / 7)$
   - $k=0$: $\varepsilon_0 = \alpha + 2.000\beta$ (Bonding)
   - $k=1, 6$: $\varepsilon_1 = \varepsilon_6 = \alpha + 2\beta \cos(51.43^\circ) = \alpha + 1.247\beta$ (Bonding, degenerate pair)
   - $k=2, 5$: $\varepsilon_2 = \varepsilon_5 = \alpha - 0.445\beta$ (Antibonding, degenerate pair)
   - $k=3, 4$: $\varepsilon_3 = \varepsilon_4 = \alpha - 1.802\beta$ (Antibonding, degenerate pair)
2. Populating the six $\pi$ electrons:
   $$E_\pi(\text{C}_7\text{H}_7^+) = 2(\alpha + 2.000\beta) + 4(\alpha + 1.247\beta) = \mathbf{6\alpha + 8.988\beta} \tag{3}$$
   - Delocalization energy exceeds three isolated double bonds ($6\alpha + 6\beta$) by **$+2.988|\beta| \approx 225\text{ kJ/mol}$**!
   - Possesses a closed-shell electronic configuration with $6\pi$ electrons ($n=1$), satisfying Hückel's rule with exceptional **aromatic stabilization**. Tropylium bromide ($\text{C}_7\text{H}_7^+\text{Br}^-$) is a stable, water-soluble salt with a melting point of $205^\circ\text{C}$!

#### Part 3: The Acidity Inversion ($pK_a = 16$ vs $36$)
- **Cyclopentadiene ($pK_a \approx 16$)**:
  Deprotonation removes a proton ($\text{H}^+$) to generate the **cyclopentadienyl anion ($\text{C}_5\text{H}_5^-$)**, which possesses **$6\pi$ electrons** ($4\times\text{alkene} + 2\times\text{lone pair}$). This achieves the ultra-stable Hückel aromatic sextet ($RE \approx 115\text{ kJ/mol}$), making cyclopentadiene more acidic than water!
- **Cycloheptatriene ($pK_a \approx 36$)**:
  Deprotonation would generate the cycloheptatrienyl anion ($\text{C}_7\text{H}_7^-$), which has **$8\pi$ electrons ($4n, n=2$)**—a severely destabilized antiaromatic system!
  Consequently, cycloheptatriene violently resists deprotonation ($pK_a \approx 36$), but readily undergoes hydride loss ($\text{H}^-$) to form the aromatic tropylium cation!"""
    })

    # Unit 2 Problem 8
    u2["problems"].append({
        "id": "p2_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Retrosynthetic Analysis & Cage Symmetry of Adamantane (Tricyclo[3.3.1.1^3,7]decane)",
        "question": "Adamantane (C10H16) is a rigid, strain-free diamondoid hydrocarbon possessing tetrahedral Td point group symmetry: (1) Prove using Newman projections that all ten carbon-carbon bonds in adamantane are locked into perfectly staggered chair cyclohexane conformations with zero angle and zero torsional strain. (2) Track Paul von Ragué Schleyer's historic 1957 one-step Lewis-acid catalyzed synthesis of adamantane from endo-tetrahydrodicyclopentadiene. (3) Why does the thermodynamic cascade yield adamantane in over 70% yield despite requiring dozens of carbocation rearrangements?",
        "solution": r"""#### Part 1: Diamondoid Symmetry and Zero Strain
1. **Cage Architecture**:
   - Adamantane consists of four fused cyclohexane rings arranged in a three-dimensional cage resembling the crystal lattice of diamond.
   - It possesses four bridgehead tertiary ($\text{C}-\text{H}$) carbons and six secondary ($-\text{CH}_2-$) carbons.
2. **Conformational Analysis**:
   - Sighting down every single $\text{C}-\text{C}$ bond reveals a **perfectly staggered dihedral angle ($\phi = 60^\circ$)**.
   - Every carbon atom has an internuclear bond angle of $\theta = 109.5^\circ$, exactly matching the ideal tetrahedral angle.
   - Consequently, **both angle strain and torsional strain are identically zero**!
   - Its standard enthalpy of formation ($\Delta H_f^\circ = -134.6\text{ kJ/mol}$) confirms it is the most thermodynamically stable $\text{C}_{10}\text{H}_{16}$ isomer in existence.

#### Part 2: Schleyer's Catalyzed Rearrangement
In 1957, Paul von Ragué Schleyer discovered that hydrogenating dicyclopentadiene yields *endo*-tetrahydrodicyclopentadiene:
$$\text{endo-Tetrahydrodicyclopentadiene} \xrightarrow{\text{catalytic } \text{AlCl}_3 \text{ or } \text{AlBr}_3, \; 150^\circ\text{C}} \mathbf{\text{Adamantane}} \tag{1}$$
- **Mechanistic Cascade**:
  1. The strong Lewis acid $\text{AlCl}_3$ abstracts a hydride ion ($\text{H}^-$) from the strained precursor to initiate a cascade of carbocation generation.
  2. The carbocation traverses a labyrinth of over **twenty consecutive Wagner-Meerwein 1,2-alkyl and 1,2-hydride shifts**.
  3. Every intermediate carbocation exists in dynamic equilibrium with other ring systems.

#### Part 3: Thermodynamic Driving Force (The "Thermodynamic Sink")
- Because all reversible carbocation shifts are in rapid dynamic equilibrium under strong Lewis acidic conditions, the reaction is entirely governed by **thermodynamic control**.
- The starting material *endo*-tetrahydrodicyclopentadiene contains substantial ring strain ($\sim 45\text{ kJ/mol}$).
- Adamantane represents the absolute **global potential energy minimum** on the $\text{C}_{10}\text{H}_{16}$ potential energy surface.
- Once a molecule rearranges into the strain-free adamantyl skeleton, it drains into an irrecoverable thermodynamic energy well and crystallizes from the reaction mixture ($mp = 270^\circ\text{C}$ in a sealed capillary), pulling the entire equilibrium cascade forward into **$>70\%$ isolated yield**!"""
    })

    # Unit 3 Problem 8
    u3["problems"].append({
        "id": "p3_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Retrosynthetic Stereocontrol: Corey-Nicolaou Macrolactonization via (E)-Alkene Precursors",
        "question": "In the stereoselective total synthesis of the 14-membered macrolide antibiotic erythronolide B, a key precursor contains a trisubstituted (E)-alkene adjacent to two chiral stereocenters: (1) Devise a stereospecific retrosynthetic disconnection using the Julia-Lythgoe olefination. (2) Contrast the stereochemical outcome of the Julia-Lythgoe olefination (producing strictly trans-(E)-alkenes) with the Horner-Wadsworth-Emmons (HWE) and Wittig reactions. (3) Detail the role of sodium amalgam (Na/Hg) reduction in enforcing the trans-alkene geometry.",
        "solution": r"""#### Part 1: Retrosynthetic Julia-Lythgoe Disconnection
1. **Disconnection**:
   Disconnect the trisubstituted $(E)$-alkene of the macrolide precursor into an alkyl phenyl sulfone and an aldehyde:
   $$\text{Target } (E)\text{-Alkene} \Longrightarrow \text{R}-\text{CH}_2-\text{SO}_2\text{Ph} \quad + \quad \text{R}'-\text{CHO} \tag{1}$$
2. **Forward Sequence**:
   - Deprotonate the phenyl sulfone with $n$-BuLi to generate an $\alpha$-sulfonyl carbanion: $[\text{R}-\bar{\text{C}}\text{H}-\text{SO}_2\text{Ph}]$.
   - Nucleophilic addition to aldehyde $\text{R}'-\text{CHO}$ yields a $\beta$-hydroxy sulfone ($\text{R}-\text{CH}(\text{SO}_2\text{Ph})-\text{CH(OH)}-\text{R}'$).
   - Acylate the hydroxyl group with acetic anhydride or benzoyl chloride to produce a $\beta$-acetoxy sulfone.
   - Reductive elimination with sodium amalgam ($\text{Na(Hg)}$) in methanol at $-20^\circ\text{C}$ delivers the **pure $(E)$-alkene with $>98:2$ diastereoselectivity**!

#### Part 2: Comparison with Wittig and Horner-Wadsworth-Emmons (HWE)
- **Classic Wittig (Non-Stabilized Ylides)**: Reaction of $\text{Ph}_3\text{P}=\text{CHR}$ with aldehydes proceeds under kinetic control via an oxaphosphetane intermediate to yield predominantly **cis-(Z)-alkenes** ($Z:E > 90:10$).
- **Horner-Wadsworth-Emmons (HWE)**: Reaction of phosphonate esters ($(\text{EtO})_2\text{P}(=\text{O})\text{CH}_2\text{COOMe}$) with aldehydes proceeds via reversible addition under thermodynamic control to yield **trans-(E)-$\alpha,\beta$-unsaturated esters**, but is limited primarily to carbonyl-conjugated alkenes.
- **Julia-Lythgoe Olefination**: Couples unfunctionalized, sterically hindered aliphatic fragments with **uncompromising $(E)$-stereospecificity**, making it the premier choice in complex macrolide polyketide synthesis!

#### Part 3: Mechanistic Origin of (E)-Stereospecificity in $\text{Na(Hg)}$ Reduction
- Single-electron transfer from sodium amalgam into the sulfone moiety cleaves the $\text{C}-\text{S}$ bond to generate a $\beta$-acetoxy radical intermediate:
  $$[\text{R}-\dot{\text{C}}\text{H}-\text{CH}(\text{OAc})-\text{R}'] \tag{2}$$
- Rapid second electron transfer generates a $\beta$-acetoxy carbanion.
- The carbanion undergoes rapid conformational equilibration around the $\text{C}-\text{C}$ single bond before elimination occurs.
- The **anti-periplanar conformer** with the bulky R and R' groups oriented trans to each other minimizes steric clash and is lower in free energy by $\Delta G^\circ \approx 18\text{ kJ/mol}$.
- Anti-elimination of the acetoxy group ($\text{AcO}^-$) from this favored conformer produces **strictly the trans-(E)-alkene**!"""
    })

    # Unit 4 Problem 8
    u4["problems"].append({
        "id": "p4_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Tandem Electrocyclization-Diels-Alder Cascade in the Total Synthesis of Endiandric Acid A",
        "question": "In K. C. Nicolaou's landmark 1982 biomimetic total synthesis of endiandric acid A (a polycyclic natural product containing four rings and eight chiral centers): (1) Track the sequence of three consecutive pericyclic reactions starting from an acyclic conjugated octa-1,3,5,7-tetraene: an 8pi conrotatory electrocyclization, a 6pi disrotatory electrocyclization, and an intramolecular Diels-Alder cycloaddition. (2) Prove using the Woodward-Hoffmann rules why the 8pi electrocyclization must be conrotatory under thermal conditions. (3) Explain why this non-enzymatic cascade occurs spontaneously with 100% diastereospecificity in near-quantitative yield.",
        "solution": r"""#### Part 1: The Three-Step Biomimetic Pericyclic Cascade
Nicolaou synthesized the fully conjugated acyclic precursor:
$$\text{R}-\text{CH}=\text{CH}-\text{CH}=\text{CH}-\text{CH}=\text{CH}-\text{CH}=\text{CH}-\text{R}' \quad (\text{trans, cis, cis, trans-Conjugated Tetraene}) \tag{1}$$

1. **Reaction 1: Thermal $8\pi$ Electrocyclic Ring Closure**:
   - The acyclic tetraene undergoes concerted thermal $8\pi$ electrocyclization to form a **cis-disubstituted cycloocta-1,3,5-triene**.
   - By Woodward-Hoffmann rules for $4n$ systems ($8\pi$), the thermal mode is **conrotatory**.
2. **Reaction 2: Thermal $6\pi$ Electrocyclic Ring Closure**:
   - The resulting cycloocta-1,3,5-triene contains a conjugated $6\pi$ cyclohexatriene sub-framework.
   - It undergoes instantaneous thermal $6\pi$ electrocyclization to form a **bicyclo[4.2.0]octa-2,4-diene** intermediate.
   - For $4n+2$ systems ($6\pi$), the thermal mode is **disrotatory**.
3. **Reaction 3: Intramolecular Diels-Alder Cycloaddition**:
   - The bicyclo[4.2.0]octadiene possesses a conjugated diene in the six-membered ring and a pendant terminal alkene dienophile.
   - It folds into an endo-transition state and undergoes a spontaneous intramolecular $[4_s + 2_s]$ Diels-Alder cycloaddition to forge the complete **tetracyclic endiandric acid A framework**!

#### Part 2: Woodward-Hoffmann Proof for Thermal $8\pi$ Conrotatory Mode
- For an $8\pi$-electron system, the HOMO in the electronic ground state is $\psi_4$.
- The fourth orbital of a linear polyene has **three internal nodes**, meaning its terminal lobes at C1 and C8 have **opposite mathematical phase signs**:
  $$\psi_4(+ \text{ at C1}, \; - \text{ at C8}) \tag{2}$$
- To bring like phases ($+$ with $+$) into constructive bonding overlap to form the new $\sigma$-bond, both terminal $p$-orbitals must rotate in the **same direction (conrotatory)**.
- Disrotatory motion would bring opposite phases into contact, resulting in a symmetry-forbidden antibonding interaction. Thus, thermal $8\pi$ electrocyclization is **strictly conrotatory**!

#### Part 3: Diastereospecificity & Thermodynamic Driving Force
- **Zero Byproducts**: All three steps are pericyclic and concerted, traversing well-defined aromatic transition states without generating any reactive ionic or radical intermediates.
- **Relief of Conformational Entropy**: The initial $8\pi$ conrotatory ring closure locks the stereochemistry of the two ring-junction hydrogens. The subsequent $6\pi$ disrotatory closure forces the two cyclobutane hydrogens into a strict *cis* geometry.
- **Rigid Intramolecular Docking**: In the bicyclo[4.2.0] intermediate, the pendant dienophile is held rigidly above the diene face, leaving only one sterically and orbitally accessible trajectory for cycloaddition.
- Consequently, all **eight chiral centers** are assembled in a single reaction vessel with **$100\%$ relative stereocontrol and $>80\%$ isolated chemical yield**, proving David Black's hypothesis that nature synthesizes endiandric acids via non-enzymatic pericyclic cascades!"""
    })

    # Unit 5 Problem 8
    u5["problems"].append({
        "id": "p5_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Retrosynthesis of the Non-Steroidal Anti-Inflammatory Drug Ibuprofen via Green Catalytic EAS",
        "question": "The industrial synthesis of the pharmaceutical blockbuster Ibuprofen (2-(4-isobutylphenyl)propanoic acid) was revolutionized by the BHC (Boots-Hoechst-Celanese) green process: (1) Contrast the classic six-step Boots synthesis (atom economy = 40%) with the modern three-step BHC catalytic synthesis (atom economy = 77%, or 99% with recovered acetic acid). (2) Detail the mechanism of the catalytic Friedel-Crafts acylation of isobutylbenzene using anhydrous HF catalyst. (3) Explain why acylation yields 100% para-regioselectivity without any meta or ortho contamination.",
        "solution": r"""#### Part 1: Atom Economy Comparison (Boots vs BHC Process)
1. **Classic Boots Synthesis (1960s)**:
   - Isobutylbenzene undergoes Friedel-Crafts acylation with $\text{AcCl} / \text{AlCl}_3$, followed by Darzens glycidic ester condensation with ethyl chloroacetate, hydrolysis, decarboxylation to aldehyde, oxime formation, and nitrile dehydration/hydrolysis.
   - Generates massive stoichiometric waste ($\text{AlCl}_3\cdot\text{H}_2\text{O}$ sludge, $\text{NaCl}$, chlorinated byproducts).
   - **Theoretical Atom Economy**: $\mathbf{40.0\%}$ ($60\%$ of all reactant mass is discarded as hazardous waste!).
2. **Modern BHC Catalytic Synthesis (1992 Presidential Green Chemistry Award)**:
   - Step 1: Catalytic Friedel-Crafts acylation with acetic anhydride and recyclable $\text{HF}$ ($100\%$ conversion, $\text{HF}$ distilled and reused).
   - Step 2: Heterogeneous catalytic hydrogenation of 4-isobutylacetophenone over Raney $\text{Ni}$ to 1-(4-isobutylphenyl)ethanol.
   - Step 3: Palladium-catalyzed carbonylation ($\text{CO} + \text{H}_2\text{O}$) to Ibuprofen.
   - **Theoretical Atom Economy**: $\mathbf{77.4\%}$ (and $\mathbf{99.9\%}$ when the byproduct acetic acid from Step 1 is recovered and sold)!

#### Part 2: Catalytic Acylation Mechanism in Anhydrous $\text{HF}$
$$\text{Isobutylbenzene} + \text{Ac}_2\text{O} \xrightarrow{\text{liquid HF, } 50^\circ\text{C}} \mathbf{4\text{-Isobutylacetophenone}} + \text{AcOH} \tag{1}$$
1. Anhydrous liquid $\text{HF}$ serves simultaneously as solvent and strong Brønsted acid catalyst.
2. Protonation of acetic anhydride generates the resonance-stabilized acylium ion:
   $$\text{Ac}_2\text{O} + 2\,\text{HF} \rightleftharpoons \mathbf{\text{CH}_3-\stackrel{\oplus}{\text{C}}=\text{O}} + \text{AcOH} + 2\,\text{F}^- \tag{2}$$
3. The electrophilic acylium ion attacks isobutylbenzene to form a Wheland intermediate, followed by fast proton transfer to regenerate the $\text{HF}$ catalyst!

#### Part 3: Origin of $100\%$ Para-Regioselectivity
- **Inductive / Hyperconjugative Activation**: The isobutyl group ($-\text{CH}_2\text{CH}(\text{CH}_3)_2$) is an ortho/para director.
- **Steric Exclusion at the Ortho Position**:
  The isobutyl group is branched and bulky. Sighting down the benzylic carbon reveals that its two methyl groups project into the steric space flanking the ortho-hydrogens.
- Furthermore, the incoming electrophile in liquid $\text{HF}$ is a solvated acylium ion complex with a large effective van der Waals radius.
- Steric clash between the isobutyl group and the solvated acylium ion completely blocks both ortho positions ($\Delta \Delta G^\ddagger_{\text{ortho}} > 18\text{ kJ/mol}$).
- Substitution occurs **exclusively at the unhindered para position ($>99.8\%$ regioselectivity)**, eliminating expensive chromatographic purification!"""
    })

    # Unit 6 Problem 8
    u6["problems"].append({
        "id": "p6_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Chiral Auxiliary-Directed Enantioselective Alkylation: The Evans Oxazolidinone Protocol",
        "question": "In the asymmetric total synthesis of polyketide natural products, David A. Evans introduced chiral oxazolidinones to achieve near-perfect stereocontrol in enolate alkylations: (1) Show how (S)-valinol is converted into the Evans oxazolidinone auxiliary. (2) Draw the rigid (Z)-boron enolate intermediate formed upon treatment of an N-propionyl oxazolidinone with dibutylboron triflate (Bu2BOTf) and triethylamine. (3) Predict the absolute stereochemistry (2R vs 2S) of the alkylated product formed upon reaction with benzyl bromide, and explain how the isopropyl group enforces complete diastereofacial selectivity.",
        "solution": r"""#### Part 1: Synthesis of the Evans Chiral Auxiliary
1. Naturally occurring, inexpensive $(S)$-valine is reduced with $\text{LiAlH}_4$ or $\text{NaBH}_4 / \text{I}_2$ to the chiral $\beta$-amino alcohol **$(S)$-valinol**.
2. Condensation of $(S)$-valinol with diethyl carbonate ($(\text{EtO})_2\text{C}=\text{O}$) or phosgene in the presence of potassium carbonate yields the enantiopure **$(4S)$-4-isopropyloxazolidin-2-one**:
   $$\text{(S)-Valinol} + (\text{EtO})_2\text{C}=\text{O} \xrightarrow{\text{K}_2\text{CO}_3, \Delta} \mathbf{(4S)\text{-4-isopropyloxazolidin-2-one}} + 2\,\text{EtOH} \tag{1}$$
3. Deprotonation with $n$-BuLi followed by acylation with propionyl chloride ($\text{CH}_3\text{CH}_2\text{COCl}$) affords the $N$-propionyl oxazolidinone substrate.

#### Part 2: Stereoselective Formation of the Rigid (Z)-Boron Enolate
$$\text{Substrate} + \text{Bu}_2\text{BOTf} + \text{Et}_3\text{N} \xrightarrow{\text{CH}_2\text{Cl}_2, -78^\circ\text{C}} \mathbf{\text{(Z)-Boron Enolate exclusively}} \tag{2}$$
- **Why Dibutylboron Triflate?**:
  - The short boron-oxygen bond length ($r_{\text{B}-\text{O}} \approx 1.45\text{ \AA}$ vs $2.1\text{ \AA}$ for lithium) forces a compact transition state.
  - In the Ireland transition state, 1,3-diaxial steric interactions between the enolate methyl group and the butyl ligands on boron overwhelmingly favor the **$(Z)$-enolate** over the $(E)$-enolate by $>100:1$!
- **Dipole Minimization & Chelation**:
  The two carbonyl oxygens (oxazolidinone $\text{C}=\text{O}$ and enolate $\text{C}=\text{O}$) orient anti-coplanar to minimize dipole-dipole repulsion, locking the entire auxiliary-enolate framework into a rigid planar geometry!

#### Part 3: Diastereofacial Enantioselection & Product Configuration
1. **Facial Shielding by the Isopropyl Group**:
   - In the $(4S)$-auxiliary, the bulky isopropyl group at C4 projects outward into the **top face ($\beta$-face)** of the molecule.
   - This isopropyl group creates a massive steric blockade across the entire $\beta$-face of the enolate double bond.
2. **Electrophilic Approach**:
   - The incoming electrophile (benzyl bromide, $\text{BnBr}$) is completely blocked from attacking the $\beta$-face.
   - It is forced to approach exclusively from the **unhindered bottom face ($\alpha$-face / si-face)**!
3. **Product Stereochemistry**:
   - Alkylation delivers the benzyl group from the bottom face, generating the new stereocenter with **$(2R)$ absolute stereochemistry** in $>99:1$ diastereomeric ratio ($dr$):
     $$\mathbf{(2R)\text{-2-methyl-3-phenylpropanoyl adduct}} \tag{3}$$
4. **Mild Cleavage**:
   Treatment with lithium hydroperoxide ($\text{LiOOH} = \text{LiOH} + \text{H}_2\text{O}_2$) hydrolyzes the chiral auxiliary with complete preservation of stereochemistry, affording enantiopure **$(2R)$-2-methyl-3-phenylpropanoic acid** while recovering the valuable chiral oxazolidinone auxiliary in $>95\%$ yield!"""
    })

    # Unit 7 Problem 8
    u7["problems"].append({
        "id": "p7_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Sharpless Asymmetric Dihydroxylation Retrosynthesis of the Taxol Side Chain",
        "question": "The blockbuster anti-cancer drug Taxol (paclitaxel) features a complex diterpene core coupled to an essential chiral phenylisoserine side chain ((2R,3S)-3-benzamido-2-hydroxy-3-phenylpropanoic acid): (1) Design a stereoselective retrosynthetic route to this side chain using Sharpless asymmetric dihydroxylation of methyl cinnamate. (2) Determine whether AD-mix-alpha or AD-mix-beta must be selected to install the (2R,3R)-diol with correct absolute stereochemistry. (3) Detail the subsequent stereospecific conversion of the diol into the (2R,3S)-amino alcohol via cyclic sulfite/sulfate intermediates.",
        "solution": r"""#### Part 1: Retrosynthetic Disconnection via Sharpless AD
$$\text{Taxol Side Chain} \Longrightarrow (2R, 3S)\text{-Methyl 3-amino-2-hydroxy-3-phenylpropanoate} \Longrightarrow (2R, 3R)\text{-Diol} \Longrightarrow \mathbf{\text{Methyl Cinnamate}} \tag{1}$$
- Starting material: Inexpensive, bench-stable methyl cinnamate ($trans-\text{PhCH}=\text{CHCOOMe}$).
- Key transformation: Catalytic asymmetric dihydroxylation across the $(E)$-alkene installs two adjacent oxygen stereocenters simultaneously.

#### Part 2: Selection of AD-Mix Reagent
1. **Sharpless Facial Selection Mnemonic**:
   - Draw the trans-alkene with the phenyl group ($\text{Ph}$) in the top-left quadrant and the ester group ($-\text{COOMe}$) in the bottom-right quadrant.
2. **Face Assignment**:
   - **AD-mix-$\beta$** (containing $(\text{DHQD})_2\text{PHAL}$) delivers both hydroxyl groups from the **top ($\beta$) face**.
   - Attack of $\text{OsO}_4$ from the top face of methyl cinnamate produces the **$(2R, 3R)$-diol**:
     $$\text{Methyl Cinnamate} + \text{AD-mix-}\beta \xrightarrow{t\text{-BuOH/H}_2\text{O}, 0^\circ\text{C}} \mathbf{\text{Methyl (2R, 3R)-2,3-dihydroxy-3-phenylpropanoate}} \tag{2}$$
     in $>99\%$ yield and $98\%$ enantiomeric excess ($ee$)!

#### Part 3: Cyclic Sulfate Chemistry & Stereospecific Inversion
To convert the $(2R, 3R)$-diol into the desired $(2R, 3S)$-amino alcohol:
1. **Cyclic Sulfate Formation**:
   - Reaction of the diol with thionyl chloride ($\text{SOCl}_2$) in $\text{CH}_2\text{Cl}_2$ yields a five-membered cyclic sulfite ester.
   - Catalytic oxidation with $\text{RuCl}_3 / \text{NaIO}_4$ converts the sulfite into a **cyclic sulfate**:
     $$\text{Diol} \xrightarrow{1.\; \text{SOCl}_2 \quad 2.\; \text{RuCl}_3/\text{NaIO}_4} \mathbf{\text{Cyclic Sulfate Intermediate}} \tag{3}$$
2. **Regioselective Nucleophilic Ring Opening with Inversion**:
   - Sodium azide ($\text{NaN}_3$) in DMF attacks the cyclic sulfate.
   - **Regioselectivity**: The C3 position is benzylic and possesses higher electrophilicity (greater partial carbocation character in the transition state) than C2 (adjacent to the electron-withdrawing ester). Attack occurs with **$>95:5$ selectivity at C3**!
   - **Stereochemistry**: Backside attack by azide inverts the C3 stereocenter from $(3R)$ to **$(3S)$**.
   - The C2 stereocenter remains untouched, preserving its **$(2R)$** configuration.
3. **Hydrolysis & Reduction**:
   - Acidic hydrolysis cleaves the remaining sulfate monoester at C2, liberating the free hydroxyl group.
   - Catalytic hydrogenation ($\text{H}_2 / \text{Pd-C}$) reduces the C3 azide ($-\text{N}_3$) to the amine ($-\text{NH}_2$).
   - Benzoylation with benzoyl chloride ($\text{PhCOCl}$) delivers the pure **Taxol phenylisoserine side chain**, which is coupled to Baccatin III to complete the total synthesis of Taxol!"""
    })

    # Unit 8 Problem 8
    u8["problems"].append({
        "id": "p8_8",
        "difficulty": "honors",
        "difficultyLabel": "Retrosynthesis & Physical Analysis",
        "title": "Retrosynthetic Synthesis of the Anti-Ulcer Drug Omeprazole via Pyridine-Benzimidazole Coupling",
        "question": "Omeprazole (Prilosec), the world's most prescribed proton pump inhibitor, is a chiral sulfoxide linking a substituted pyridine ring to a benzimidazole core: (1) Formulate a convergent retrosynthetic disconnection yielding two functionalized heterocyclic building blocks. (2) Track the synthesis of 2-chloromethyl-3,5-dimethyl-4-methoxypyridine using the pyridine N-oxide activation strategy. (3) Detail the catalytic enantioselective Kagan oxidation of the prochiral sulfide into the optically active drug esomeprazole (Nexium).",
        "solution": r"""#### Part 1: Convergent Retrosynthetic Disconnection
$$\text{Omeprazole} \Longrightarrow \mathbf{\text{Pyridine-CH}_2-\text{S-Benzimidazole}} \Longrightarrow \text{Py-CH}_2\text{Cl} \quad + \quad \text{HS-Benzimidazole} \tag{1}$$
- Disconnect the central sulfoxide ($-\text{SO}-$) via late-stage chemoselective oxidation of a sulfide ($\text{Ar}-\text{CH}_2-\text{S}-\text{Het}$).
- Disconnect the thioether bond via nucleophilic substitution between **2-(chloromethyl)-3,5-dimethyl-4-methoxypyridine** and **5-methoxy-1H-benzo[d]imidazole-2-thiol**.

#### Part 2: Synthesis of the Pyridine Building Block via N-Oxide Activation
Starting from 2,3,5-trimethylpyridine:
1. **$N$-Oxidation**: Oxidation with peracetic acid ($\text{CH}_3\text{COOOH}$) yields 2,3,5-trimethylpyridine $N$-oxide.
2. **Regioselective Nitration**: Nitration with $\text{HNO}_3 / \text{H}_2\text{SO}_4$ at $90^\circ\text{C}$ introduces a nitro group selectively at the **C4 position** activated by resonance donation from the $N$-oxide oxygen:
   $$\text{2,3,5-Trimethylpyridine } N\text{-oxide} \xrightarrow{\text{HNO}_3/\text{H}_2\text{SO}_4} \mathbf{4\text{-nitro-2,3,5-trimethylpyridine }} N\text{-oxide} \tag{2}$$
3. **Nucleophilic Methoxylation**: Nucleophilic aromatic substitution ($S_N\text{Ar}$) with sodium methoxide ($\text{NaOCH}_3$) in methanol displaces the nitro group cleanly, installing the 4-methoxy substituent.
4. **Boekelheide Rearrangement**:
   Heating with acetic anhydride ($\text{Ac}_2\text{O}$) causes an intramolecular $[3,3]$-rearrangement of the $N$-oxide, functionalizing the C2-methyl group to a 2-acetoxymethyl group ($\text{Py}-\text{CH}_2\text{OAc}$).
5. Hydrolysis and chlorination with thionyl chloride ($\text{SOCl}_2$) affords pure **2-(chloromethyl)-3,5-dimethyl-4-methoxypyridine**!

#### Part 3: Asymmetric Sulfoxidation to Esomeprazole (Nexium)
The coupled prochiral sulfide ($\text{Py}-\text{CH}_2-\text{S}-\text{Benzimidazole}$) is oxidized to the sulfoxide:
$$\text{Sulfide} + \text{Cumene Hydroperoxide} \xrightarrow{\text{Ti(O-}i\text{-Pr)}_4, \; (S,S)\text{-DET}, \; \text{H}_2\text{O}, \; 30^\circ\text{C}} \mathbf{(S)\text{-Omeprazole (Esomeprazole)}} \tag{3}$$
- **The Kagan Modification of Sharpless Epoxidation**:
  Henri Kagan discovered that adding exactly **one equivalent of water** to the $\text{Ti(O-}i\text{-Pr)}_4 / \text{diethyl tartrate}$ complex forms a chiral titanium oxo-bridged oligomer.
- This modified catalyst coordinates the prochiral sulfur lone pairs with exceptional chiral discrimination, oxidizing sulfur with cumene hydroperoxide to produce $(S)$-omeprazole in **$>94\%$ enantiomeric excess ($ee$)**!
- Esomeprazole binds covalently to the $\text{H}^+/\text{K}^+$-ATPase enzyme in stomach parietal cells, revolutionizing the treatment of acid reflux and peptic ulcers!"""
    })

    return units
