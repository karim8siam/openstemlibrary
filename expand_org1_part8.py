# expand_org1_part8.py
# Deep academic enrichment: Subsections §6.9, §7.9, §8.9
# and Graduate/Honors Solved Problems for Units 6, 7, and 8.

def expand_units_6_7_8(units):
    u1, u2, u3, u4, u5, u6, u7, u8 = units

    # ==========================================
    # UNIT 6: Advanced Section & Honors Problems
    # ==========================================
    u6["sections"].append({
        "id": "sec6_9",
        "secNumber": "6.9",
        "title": "§6.9 Organoboron, Organosilicon & Zinc Carbenoid Stereoselective Syntheses",
        "heading": "Organoboron, Organosilicon & Zinc Carbenoid Stereoselective Syntheses",
        "simulations": ["sim_chem_sn1_sn2_e1_e2_mechanism_matrix"],
        "content": r"""### Organoboron Precursors: Miyaura Borylation & Pinacol Boronates

Aryl and alkyl boronic esters serve as the indispensable organometallic partners for Suzuki-Miyaura cross-couplings:

$$\text{Ar}-\text{X} + \text{B}_2\text{pin}_2 \xrightarrow{\text{PdCl}_2(\text{dppf}), \; \text{KOAc}, \; \text{dioxane}, \; 80^\circ\text{C}} \mathbf{\text{Ar}-\text{Bpin}} + \text{pinB}-\text{OAc} + \text{KX} \tag{6.19a}$$

```
   MIYAURA BORYLATION CATALYTIC CYCLE:
          Pd(0)L2
             |
       OA    | Ar-X (Aryl Halide)
             v
        Ar-Pd(II)L2-X
             |
       Ligand| KOAc (Displaces Halide by Acetate)
       Exch. v
        Ar-Pd(II)L2-OAc
             |
       TM    | B2pin2 (Bis(pinacolato)diboron)
             v
        Ar-Pd(II)L2-Bpin  +  AcO-Bpin
             |
       RE    v (Arylboronate Ar-Bpin Released)
          Pd(0)L2 (Regenerated)
```

#### Why Potassium Acetate ($\text{KOAc}$) is Essential:
- If a strong base like $\text{K}_2\text{CO}_3$ or $\text{KOH}$ is used, the generated $\text{Ar}-\text{Bpin}$ product undergoes premature Suzuki cross-coupling with remaining unreacted $\text{Ar}-\text{X}$, forming unwanted biaryl dimers ($\text{Ar}-\text{Ar}$).
- Potassium acetate is weakly basic enough to facilitate transmetalation of $\text{B}_2\text{pin}_2$ while completely suppressing subsequent Suzuki coupling, ensuring $>90\%$ isolated yields of pure boronic esters!

### The Simmons-Smith Reaction & Zinc Carbenoids

Discovered by Howard Simmons and Ronald Smith in 1958, the reaction of alkenes with diiodomethane and zinc-copper couple ($\text{Zn(Cu)}$) cleanly synthesizes cyclopropanes with **strict stereospecific syn-addition**:

$$\text{Alkene} + \text{CH}_2\text{I}_2 + \text{Zn(Cu)} \xrightarrow{\text{Et}_2\text{O}} \mathbf{\text{Cyclopropane}} + \text{ZnI}_2 \tag{6.19b}$$

#### The Active Reagent: Iodomethylzinc Iodide ($\text{ICH}_2\text{ZnI}$):
- Does NOT generate free carbene ($:\text{CH}_2$).
- Exists as an organozinc **carbenoid** where zinc coordinates both iodine and carbon.
- **Diastereoselective Directed Cyclopropanation**:
  When an allylic alcohol is cyclopropanated, the zinc atom coordinates to the hydroxyl oxygen prior to delivering the methylene group:
  $$\left[ \begin{matrix} \text{C}=\text{C} & \cdots & \text{CH}_2 \\ \vert & & \vert \\ \text{C}-\text{O}-\text{H} & \cdots & \text{ZnI} \end{matrix} \right]^\ddagger \tag{6.19c}$$
  This internal chelation delivers methylene **exclusively to the same face as the hydroxyl group ($>99\%$ diastereoselectivity)**!"""
    })

    u6["problems"].extend([
        {
            "id": "p6_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Quantitative Evaluation of Winstein-Grunwald Solvent Ionizing Power Y in Solvolysis",
            "question": "The rate constant for the unimolecular solvolysis of tert-butyl chloride is measured in various binary solvent mixtures at 25°C. According to the Grunwald-Winstein equation: log(k / k_0) = m * Y, where k_0 is the solvolysis rate in 80% aqueous ethanol (defined as Y = 0.00) and m is the substrate sensitivity parameter (defined as m = 1.00 for t-BuCl). In pure water, Y = +3.49; in 50% aqueous ethanol, Y = +1.65; in pure ethanol, Y = -2.03; and in pure trifluoroethanol (CF3CH2OH), Y = +1.80. (1) Calculate the ratio of the solvolysis rate constant in pure water compared to pure ethanol. (2) Explain why trifluoroethanol has a high positive Y value despite being a poorly nucleophilic alcohol. (3) What does this reveal about transition-state charge stabilization in the SN1 pathway?",
            "solution": r"""#### Part 1: Rate Ratio Calculation (Water vs Ethanol)
Using the Grunwald-Winstein equation:
$$\log\left(\frac{k}{k_0}\right) = m Y \implies k = k_0 \cdot 10^{m Y} \tag{1}$$
Given $m = 1.00$ for tert-butyl chloride:
- In pure water: $Y_{\text{water}} = +3.49 \implies \log(k_{\text{water}} / k_0) = 3.49$
- In pure ethanol: $Y_{\text{EtOH}} = -2.03 \implies \log(k_{\text{EtOH}} / k_0) = -2.03$

The ratio of the rate constants is:
$$\log\left(\frac{k_{\text{water}}}{k_{\text{EtOH}}}\right) = \log\left(\frac{k_{\text{water}}}{k_0}\right) - \log\left(\frac{k_{\text{EtOH}}}{k_0}\right) = 3.49 - (-2.03) = \mathbf{+5.52} \tag{2}$$
$$\frac{k_{\text{water}}}{k_{\text{EtOH}}} = 10^{5.52} \approx \mathbf{3.31 \times 10^5}$$
Solvolysis occurs over **$330,000$ times faster in pure water than in pure ethanol**!

#### Part 2: High Ionizing Power of 2,2,2-Trifluoroethanol (TFE)
1. **Electronegative Fluorine Atoms**:
   - The three fluorine atoms in $-\text{CF}_3$ exert a massive electron-withdrawing inductive effect ($-I$).
   - This dramatically polarizes the hydroxyl group, making the hydroxyl proton unusually acidic ($pK_a = 12.4$ vs $15.9$ for ethanol).
2. **Superior Anion Solvation via Hydrogen Bonding**:
   - In the $S_N1$ transition state, negative charge accumulates on the departing chloride ion ($[\text{R}^{\delta+} \cdots \text{Cl}^{\delta-}]^\ddagger$).
   - TFE's highly polarized $\text{O}-\text{H}$ protons form exceptionally strong hydrogen bonds with the departing chloride anion:
     $$\text{CF}_3\text{CH}_2\text{O}-\text{H} \cdots \text{Cl}^{\delta-} \tag{3}$$
   - This provides over $30\text{ kJ/mol}$ of transition-state stabilization, accelerating ionization even though TFE itself is an extremely poor nucleophile (due to low oxygen electron density).

#### Part 3: Physical Organic Insights
- This experiment proves that **ionizing power ($Y$) measures the solvent's ability to pull off the leaving group via anion solvation**, completely independently of its nucleophilicity!
- In an $S_N1$ reaction, the rate-determining step requires zero nucleophilic attack; it is driven entirely by electrophilic solvation of the departing anion by the solvent's hydrogen-bond donor network."""
        },
        {
            "id": "p6_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Meisenheimer Complex Resonance Delocalization & Fluorine Reactivity in SNAr",
            "question": "In the nucleophilic aromatic substitution (SNAr) of 1-halo-2,4-dinitrobenzene by sodium methoxide: (1) The relative reaction rates at 25°C are: Fluoride (k_rel = 3300), Chloride (k_rel = 4.3), Bromide (k_rel = 4.3), Iodide (k_rel = 1.0). Explain why fluoride is by far the most reactive leaving group in SNAr, in complete reversal of its behavior in SN2 and SN1 reactions. (2) Draw all major canonical resonance structures of the Meisenheimer intermediate. (3) Prove that nucleophilic attack, and NOT leaving group departure, is the rate-determining step.",
            "solution": r"""#### Part 1: Reversal of Leaving Group Hierarchy in $S_N\text{Ar}$
1. **In $S_N2$ and $S_N1$ (Aliphatic Systems)**:
   - The rate-determining step involves cleavage of the carbon-halogen bond.
   - Bond dissociation energy and leaving-group $pK_a$ dictate the rate: $\text{I}^- (pK_a -10) > \text{Br}^- (pK_a -9) > \text{Cl}^- (pK_a -7) \gg \text{F}^- (pK_a +3.2)$. Fluoride is an extremely poor leaving group.
2. **In $S_N\text{Ar}$ (Aromatic Systems)**:
   - The reaction proceeds via a two-step addition-elimination mechanism:
     $$\text{Ar}-\text{X} + \text{MeO}^- \xrightarrow{k_1} [\text{Meisenheimer Intermediate}]^- \xrightarrow{k_2} \text{Ar}-\text{OMe} + \text{X}^- \tag{1}$$
   - **Step 1 ($k_1$, nucleophilic addition)** is the **rate-determining step** ($k_1 \ll k_2$).
   - Fluorine is the most electronegative element in the periodic table ($\chi = 3.98$).
   - By strong inductive withdrawal ($-I$), fluorine polarizes the ipso-carbon ($\text{C}_1$), creating a massive partial positive charge ($\delta^+$) that accelerates nucleophilic attack by methoxide.
   - Consequently, $k_1(\text{F}) \gg k_1(\text{Cl}) \approx k_1(\text{Br}) > k_1(\text{I})$, resulting in fluoride reacting **$3300$ times faster than iodide**!

#### Part 2: Canonical Resonance Structures of the Meisenheimer Intermediate
When methoxide attacks C1 of 1-fluoro-2,4-dinitrobenzene:
The ipso-carbon re-hybridizes from $sp^2$ to $sp^3$, forming a non-aromatic cyclohexadienyl carbanion:
1. Negative charge at C2 (delocalized into ortho-nitro group):
   $$[\text{Ring}-\text{C}_2=\text{N}^+(\text{O}^-)_2] \quad (\text{Nitro octet-complete contributor})$$
2. Negative charge at C6:
   $$[\text{Ring carbanion at C6}]$$
3. Negative charge at C4 (delocalized into para-nitro group):
   $$[\text{Ring}-\text{C}_4=\text{N}^+(\text{O}^-)_2] \quad (\text{Nitro octet-complete contributor})$$
Both the ortho- and para-nitro groups stabilize the negative charge via direct conjugation into their oxygen atoms, lowering the activation energy barrier by over $70\text{ kJ/mol}$!

#### Part 3: Proof that Step 1 is Rate-Determining
- If Step 2 (carbon-halogen bond cleavage) were rate-determining ($k_2 \ll k_1$), the rate would be proportional to $k_2$, and the reaction rate would track leaving group ability: $\text{I} > \text{Br} > \text{Cl} \gg \text{F}$.
- Because the experimental rate order is **$\text{F} \gg \text{Cl} \approx \text{Br} \approx \text{I}$**, carbon-halogen bond breaking has zero influence on the overall reaction rate.
- Step 1 (nucleophilic attack forming the Meisenheimer intermediate) is rigorously confirmed as the **sole rate-determining step**!"""
        }
    ])

    # ==========================================
    # UNIT 7: Advanced Section & Honors Problems
    # ==========================================
    u7["sections"].append({
        "id": "sec7_9",
        "secNumber": "7.9",
        "title": "§7.9 Supramolecular Host-Guest Macrocycles & Green Catalytic Oxidations",
        "heading": "Supramolecular Host-Guest Macrocycles & Green Catalytic Oxidations",
        "simulations": ["sim_chem_epoxide_ring_opening_pinacol"],
        "content": r"""### Calixarenes, Cyclodextrins, and Supramolecular Cavitands

Supramolecular chemistry (1987 Nobel Prize: Pedersen, Cram, Lehn) investigates structures held together by non-covalent intermolecular forces:

#### 1. Calix[n]arenes (C. David Gutsche):
Cyclic oligomers prepared by the base-catalyzed condensation of $p$-tert-butylphenol with formaldehyde:
$$n\,(p\text{-}t\text{-BuC}_6\text{H}_4\text{OH}) + n\,\text{CH}_2\text{O} \xrightarrow{\text{NaOH, } \Delta} \mathbf{\text{Calix}[n]\text{arene}} + n\,\text{H}_2\text{O} \tag{7.20a}$$
- **Calix[4]arene**: Adopts a rigid **cone conformation** stabilized by a circular array of four intramolecular cooperative hydrogen bonds among the lower-rim phenolic hydroxyl groups ($\Delta H^\circ \approx -60\text{ kJ/mol}$).
- The upper rim forms a hydrophobic hydrophobic cavity with a diameter of $\sim 3.0\text{ \AA}$, capable of encapsulating small neutral organic guests (such as chloroform or toluene).

#### 2. Cyclodextrins ($\alpha, \beta, \gamma$):
Toroidal cyclic oligosaccharides of $\alpha$-D-glucopyranose produced by enzymatic degradation of starch:
- **$\alpha$-Cyclodextrin** (6 glucose units): Cavity diameter $4.7 - 5.3\text{ \AA}$
- **$\beta$-Cyclodextrin** (7 glucose units): Cavity diameter $6.0 - 6.5\text{ \AA}$ (ideal for encapsulating aromatic drugs like ibuprofen)
- **$\gamma$-Cyclodextrin** (8 glucose units): Cavity diameter $7.5 - 8.3\text{ \AA}$
- The interior of the cavity is lined with glycosidic oxygen bridges and $\text{C}-\text{H}$ bonds, making it hydrophobic, while the exterior displays primary and secondary hydroxyl groups, rendering it water-soluble.
- Dissolving hydrophobic drugs inside cyclodextrins enhances their aqueous bioavailability by factors of $10^2 - 10^4$!

### Green Catalytic Oxidations: TEMPO & Dess-Martin Periodinane

Modern industrial and medicinal chemistry replaces stoichiometric heavy-metal oxidants ($\text{CrO}_3, \text{KMnO}_4$) with catalytic, environmentally benign protocols:

#### 1. The TEMPO / Bleach Catalytic Cycle:
$$\text{R}-\text{CH}_2\text{OH} + \text{NaOCl} \xrightarrow{\text{catalytic TEMPO}, \; \text{KBr}, \; \text{pH } 9.5} \mathbf{\text{R}-\text{CHO}} + \text{NaCl} + \text{H}_2\text{O} \tag{7.20b}$$
- **Active Oxidant**: The stable nitroxyl radical (2,2,6,6-tetramethylpiperidine-1-oxyl, TEMPO) is oxidized by hypochlorite ($\text{OCl}^-$) to an **oxoammonium cation**:
  $$[\text{TEMPO}]^\bullet \xrightarrow{+\text{OCl}^-} [\text{TEMPO}=\text{O}]^+ \tag{7.20c}$$
- The oxoammonium ion oxidizes primary alcohols to aldehydes selectively within minutes, reducing back to the hydroxylamine ($\text{TEMPO}-\text{OH}$), which is re-oxidized in catalytic cycles!
- Generates non-toxic aqueous sodium chloride as the sole byproduct.

#### 2. Dess-Martin Periodinane (DMP):
Synthesized from 2-iodobenzoic acid and potassium bromate followed by treatment with acetic anhydride:
$$\text{R}_2\text{CHOH} + \text{DMP} \longrightarrow \mathbf{\text{R}_2\text{C}=\text{O}} + \text{Iodoxybenzoic Acid} + 2\,\text{AcOH} \tag{7.20d}$$
- Operates under neutral conditions at $25^\circ\text{C}$, tolerating acid- and base-sensitive functional groups (silyl ethers, acetals, epoxides, sulfoxides) with quantitative yields."""
    })

    u7["problems"].extend([
        {
            "id": "p7_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Migratory Aptitude & Carbocation Thermodynamics in Unsymmetrical Pinacols",
            "question": "When 1,1-diphenyl-2-methylpropane-1,2-diol (pinacol derivative A) is treated with cold concentrated sulfuric acid, a single rearrangement product is formed in 95% yield. (1) Predict which hydroxyl group is protonated and lost as water to generate the initial carbocation intermediate. Support your prediction with gas-phase heats of formation and resonance arguments. (2) Determine which substituent (phenyl vs methyl) undergoes 1,2-migration. (3) Draw the complete line-by-line mechanism showing all formal charges and oxocarbenium resonance contributors, and name the final product.",
            "solution": r"""#### Part 1: Selectivity of Carbocation Generation
The substrate is:
$$\text{Ph}_2\text{C(OH)}-\text{C(OH)}(\text{CH}_3)_2 \tag{1}$$
Two possible carbocation intermediates can be formed upon protonation and loss of water:
1. **Path A (Loss of OH from C1)**:
   - Generates carbocation at C1: $[\text{Ph}_2\stackrel{\oplus}{\text{C}}-\text{C(OH)}(\text{CH}_3)_2]$
   - This carbocation is **doubly benzylic and tertiary**, stabilized by resonance delocalization into **TWO full phenyl rings**:
     $$\Delta H_f^\circ(\text{doubly benzylic carbocation}) \ll \Delta H_f^\circ(\text{aliphatic } 3^\circ \text{ carbocation})$$
   - It possesses over **$60\text{ kJ/mol}$ greater thermodynamic stability** than a simple tertiary aliphatic carbocation.
2. **Path B (Loss of OH from C2)**:
   - Generates carbocation at C2: $[\text{Ph}_2\text{C(OH)}-\stackrel{\oplus}{\text{C}}(\text{CH}_3)_2]$
   - This carbocation is merely a tertiary alkyl carbocation, stabilized only by hyperconjugation from two methyl groups.
3. **Conclusion**:
   Protonation and loss of water occurs **exclusively at C1** to generate the resonance-stabilized doubly benzylic carbocation!

#### Part 2: Migratory Step
From the intermediate $[\text{Ph}_2\stackrel{\oplus}{\text{C}}-\text{C(OH)}(\text{CH}_3)_2]$:
- The carbocation is at C1.
- The adjacent carbon (C2) bears a hydroxyl group ($-\text{OH}$) and two methyl groups ($-\text{CH}_3$).
- Because C2 bears NO phenyl groups, **a methyl group MUST migrate** from C2 to C1!
- (Note: Phenyl would have had a higher intrinsic migratory aptitude than methyl, but the phenyl groups are located on the carbocation carbon itself, not on the adjacent hydroxyl-bearing carbon!)

#### Part 3: Line-by-Line Mechanism & Final Product
1. **1,2-Methide Shift**:
   A methyl group migrates with its electron pair from C2 to C1:
   $$\text{Ph}_2\stackrel{\oplus}{\text{C}}-\text{C(OH)}(\text{CH}_3)_2 \xrightarrow{1,2\text{-shift of Me}} \left[ \text{Ph}_2\text{C(CH}_3)-\stackrel{\oplus}{\text{C}}(\text{OH})(\text{CH}_3) \right] \tag{2}$$
2. **Oxocarbenium Ion Stabilization**:
   The resulting carbocation is directly adjacent to oxygen and is stabilized by resonance:
   $$\text{Ph}_2\text{C(Me)}-\stackrel{\oplus}{\text{C}}(\text{OH})(\text{Me}) \longleftrightarrow \mathbf{\text{Ph}_2\text{C(Me)}-\text{C}(\stackrel{\oplus}{\text{O}}\text{H})(\text{Me})} \tag{3}$$
   Every atom achieves a complete valence octet!
3. **Deprotonation**:
   Loss of proton to solvent yields the neutral product:
   $$\mathbf{3,3\text{-diphenylbutan-2-one}} \quad (\text{Ph}_2\text{C}(\text{CH}_3)-\text{CO}-\text{CH}_3) \tag{4}$$
   Formed in $>95\%$ isolated yield!"""
        },
        {
            "id": "p7_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Stereospecific Malaprade Glycol Cleavage: Cyclic Periodate Ester Kinetics",
            "question": "The oxidative cleavage of vicinal diols by periodic acid (HIO4) proceeds through a cyclic periodate ester intermediate. The cleavage rate of cis-cyclohexane-1,2-diol is measured to be k_rel = 10,000, whereas trans-cyclohexane-1,2-diol reacts sluggishly with k_rel = 1.0. (1) Write the balanced stoichiometry and rate equation for the Malaprade reaction. (2) Explain using conformational stereochemistry why the cis-diol reacts 10,000 times faster than the trans-diol. (3) Predict the oxidation products and stoichiometric consumption of periodate for glycerol (propane-1,2,3-triol).",
            "solution": r"""#### Part 1: Stoichiometry and Rate Law
The Malaprade cleavage of a vicinal 1,2-diol:
$$\text{R}_2\text{C(OH)}-\text{C(OH)}\text{R}'_2 + \text{HIO}_4 \longrightarrow \mathbf{\text{R}_2\text{C}=\text{O}} + \mathbf{\text{R}'_2\text{C}=\text{O}} + \text{HIO}_3 + \text{H}_2\text{O} \tag{1}$$
The reaction follows second-order kinetics:
$$v = k [\text{Diol}][\text{HIO}_4] \tag{2}$$
The rate-determining step is the formation of a five-membered cyclic **periodate monoester**:
$$\left[ \begin{matrix} \text{C} & - & \text{O} \\ \vert & & \vert \\ \text{C} & - & \text{O} \end{matrix} \right] \text{I}(=\text{O})_2(\text{OH}) \tag{3}$$

#### Part 2: Conformational Stereoelectronic Explanation of the $10^4$ Rate Ratio
1. **cis-Cyclohexane-1,2-diol**:
   - In its chair conformation, the two hydroxyl groups occupy **axial-equatorial ($a,e$)** positions.
   - The dihedral angle between the two $\text{C}-\text{O}$ bonds is $\phi \approx 60^\circ$.
   - This dihedral angle easily twists to $0-30^\circ$ without prohibitive ring strain, allowing both oxygen atoms to coordinate simultaneously to the iodine atom to form the coplanar five-membered cyclic periodate ester.
   - Consequently, cyclic ester formation is extremely rapid, and subsequent concerted two-electron pericyclic fragmentation yields adipaldehyde (hexanedial) with $k_{\text{rel}} = 10,000$!
2. **trans-Cyclohexane-1,2-diol**:
   - In its most stable diequatorial ($e,e$) chair conformation, the dihedral angle is $\phi \approx 60^\circ$, but the two oxygens point in opposite directions across the ring edge.
   - In its diaxial ($a,a$) conformation, the dihedral angle is $\phi = 180^\circ$ (anti-periplanar); the oxygens are separated by over $3.6\text{ \AA}$!
   - To form a cyclic five-membered periodate ester, the cyclohexane ring is forced to undergo severe distortion into a high-energy boat conformation to bring both oxygens close enough to bind a single iodine atom.
   - This introduces massive angle and torsional strain ($\Delta \Delta G^\ddagger \approx 23\text{ kJ/mol}$), slowing the rate by **four orders of magnitude ($10^4$)**!

#### Part 3: Periodate Oxidation of Glycerol ($\text{Propane-1,2,3-triol}$)
$$\text{HOCH}_2-\text{CH(OH)}-\text{CH}_2\text{OH} + 2\,\text{HIO}_4 \longrightarrow \mathbf{2\,\text{HCHO (Formaldehyde)}} + \mathbf{\text{HCOOH (Formic Acid)}} + 2\,\text{HIO}_3 + \text{H}_2\text{O} \tag{4}$$
- The central secondary alcohol carbon is cleaved from both adjacent primary carbons, consuming **two equivalents of periodic acid ($\text{HIO}_4$)**.
- The two terminal carbons are oxidized to **two equivalents of Formaldehyde ($\text{HCHO}$)**.
- The central carbon is oxidized to **one equivalent of Formic Acid ($\text{HCOOH}$)**.
- Measuring the moles of periodate consumed ($2.0\text{ mol}$) and formic acid produced ($1.0\text{ mol}$) provides a definitive quantitative diagnostic for triols and carbohydrate aldoses!"""
        }
    ])

    # ==========================================
    # UNIT 8: Advanced Section & Honors Problems
    # ==========================================
    u8["sections"].append({
        "id": "sec8_9",
        "secNumber": "8.9",
        "title": "§8.9 Diazines, Purines, Porphyrins & Biological Heterocyclic Cofactors",
        "heading": "Diazines, Purines, Porphyrins & Biological Heterocyclic Cofactors",
        "simulations": ["sim_chem_heterocycle_aromaticity_eas"],
        "content": r"""### The Diazines: Pyridazine, Pyrimidine & Pyrazine

Six-membered aromatic heterocycles containing two nitrogen atoms exhibit profound deactivation toward electrophiles and extreme susceptibility toward nucleophiles:

```
      PYRIDAZINE (1,2-Diazine)     PYRIMIDINE (1,3-Diazine)     PYRAZINE (1,4-Diazine)
               N                            N                            N
             /   \                        /   \                        /   \
            N     |                      |     N                      |     |
            \   /                        \   /                        \   /
                                                                         N
      * Dipole moment = 4.14 D     * Dipole moment = 2.33 D     * Dipole moment = 0.0 D
      * bp = 208 deg C             * bp = 124 deg C             * mp = 52 deg C (Symmetric)
      * pKa = 2.24                 * pKa = 1.30                 * pKa = 0.65
```

#### 1. Lactam-Lactim Tautomerism in DNA & RNA Nucleobases:
The pyrimidines cytosine, uracil, and thymine exist almost exclusively in the **keto / lactam tautomeric form** in aqueous physiological environments:
$$\text{Lactam Form (Keto: } -\text{NH}-\text{C}(=\text{O})-) \xrightleftharpoons[K > 10^4]{\quad} \text{Lactim Form (Enol: } -\text{N}=\text{C}(\text{OH})-) \tag{8.20a}$$
- This equilibrium is critical: the Watson-Crick hydrogen bonding that encodes the genetic code in the DNA double helix (A-T and G-C base pairs) strictly depends on the precise placement of hydrogen-bond donors ($-\text{NH}-$) and acceptors ($=\text{O}$) in the **lactam form**.
- Rare transient shifts to the minor lactim form ($1 \text{ in } 10^5$) cause spontaneous point mutations (transition mutations) during DNA replication!

### Porphyrins, Corrin Rings, and Biochemical Hydride Transfer

1. **Porphyrin Architecture (Heme & Chlorophyll)**:
   - A planar macrocycle composed of four pyrrole rings joined by four methine ($=\text{CH}-$) bridges.
   - Contains a fully conjugated ring system of $26\pi$ electrons, of which **$18\pi$ electrons form a continuous delocalized aromatic perimeter** according to Hückel's $(4n+2)$ rule ($n=4$).
   - Aromatic resonance stabilization is enormous ($\sim 840\text{ kJ/mol}$).
   - The central cavity possesses a diameter of $\sim 2.0\text{ \AA}$, perfectly tailored to coordinate divalent transition metals ($\text{Fe}^{2+}$ in heme hemoglobin, $\text{Mg}^{2+}$ in chlorophyll, $\text{Co}^{3+}$ in vitamin B12 corrin ring).
2. **Hydride Transfer Mechanisms in $\text{NAD}^+ / \text{NADH}$**:
   - Nicotinamide adenine dinucleotide ($\text{NAD}^+$) relies on its **pyridinium ring** to catalyze biological oxidations.
   - Enzymatic reduction delivers a stereospecific hydride ion ($:\text{H}^-$) to the **C4 position** of the pyridinium ring, converting it into the neutral 1,4-dihydropyridine ($\text{NADH}$):
     $$[\text{NAD}]^+ + \text{H}^- \longrightarrow \mathbf{\text{NADH}} \tag{8.20b}$$
   - Because 1,4-dihydropyridine is non-aromatic, it stores $\sim 88\text{ kJ/mol}$ of reduction potential, allowing $\text{NADH}$ to act as the universal cellular reducing agent driving ATP synthesis!"""
    })

    u8["problems"].extend([
        {
            "id": "p8_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Chichibabin Amination of 4-Methylpyridine: Mechanistic & Deuterium Isotope Verification",
            "question": "When 4-methylpyridine (gamma-picoline) is heated with sodium amide (NaNH2) in toluene at 110°C followed by quenching with D2O: (1) Predict the regiochemical site of amination (C2 vs C3) and justify using Wheland-Meisenheimer resonance contributors. (2) Track the evolution of molecular gas during the reaction and identify its chemical formula when 2-deutero-4-methylpyridine is used. (3) Deduce the final structure of the isolated product after D2O workup.",
            "solution": r"""#### Part 1: Regiochemical Site of Amination
1. **Electrophilic Character of the Pyridine Ring**:
   - The ring nitrogen is strongly electronegative ($\chi = 3.04$), withdrawing electron density inductively and via resonance.
   - Carbons C2, C4, and C6 possess substantial partial positive charge ($\delta^+$), while C3 and C5 are relatively electron-neutral.
   - Because C4 is blocked by the methyl group ($-\text{CH}_3$), nucleophilic attack by amide ion ($\text{NH}_2^-$) occurs selectively at the equivalent **C2 (or C6) positions**.
2. **Resonance Stabilization of the Meisenheimer Intermediate**:
   Attack at C2 generates an anionic intermediate where the negative charge is delocalized directly onto the electronegative ring nitrogen atom:
   $$\left[ \text{Py-C}_2(\text{NH}_2)(\text{H}) - \bar{\text{N}} \longleftrightarrow \text{Py-C}_2(\text{NH}_2)(\text{H}) = \text{N}^- \right] \tag{1}$$
   This octet-complete nitrogen contributor provides overwhelming thermodynamic stabilization that is completely absent for hypothetical attack at C3!

#### Part 2: Gas Stoichiometry & Deuterium Isotope Verification
1. **Hydride Elimination**:
   The intermediate must eliminate hydride ($H^-$) to restore the aromatic pyridine ring.
   The departing hydride abstracts a proton from the newly introduced amino group ($-\text{NH}_2$):
   $$\text{H}^- + \text{H}-\text{NH}-\text{Py} \longrightarrow \mathbf{\text{H}_2\uparrow} + [\text{Py-NH}]^- \text{Na}^+ \tag{2}$$
   One mole of molecular hydrogen gas ($\text{H}_2$) is evolved per mole of pyridine consumed.
2. **Isotopic Labeling**:
   When 2-deutero-4-methylpyridine is used, the eliminated species is a deuteride ion ($\text{D}^-$):
   $$\text{D}^- + \text{H}-\text{NH}-\text{Py} \longrightarrow \mathbf{\text{H}-\text{D}\uparrow} + [\text{Py-NH}]^- \text{Na}^+ \tag{3}$$
   Mass spectrometry confirms quantitative liberation of **HD (deuterium hydride gas, $m/z = 3$)**, proving that the eliminated hydrogen originates exclusively from C2!

#### Part 3: Structure of the Isolated Product after $\text{D}_2\text{O}$ Quench
Quenching the sodium salt $[\text{Py-NH}]^-\text{Na}^+$ with heavy water ($\text{D}_2\text{O}$) protonates the exocyclic nitrogen with deuterium:
$$\mathbf{2\text{-amino-4-methylpyridine-N,N-d}_2} \quad (\text{4-methylpyridin-2-yl-ND}_2) \tag{4}$$
isolated in $>85\%$ yield!"""
        },
        {
            "id": "p8_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Molecular Orbital Symmetry & Relative Reactivity in the Paal-Knorr Synthesis",
            "question": "In the Paal-Knorr synthesis of five-membered heterocycles from hexane-2,5-dione: (1) Treatment with P4S10 yields 2,5-dimethylthiophene; treatment with P2O5 yields 2,5-dimethylfuran; and treatment with benzylamine (PhCH2NH2) yields 1-benzyl-2,5-dimethylpyrrole. Draw the complete curved-arrow mechanism for the formation of 2,5-dimethylfuran. (2) Contrast the ease of cyclization and relative aromatic stabilization energies of the three products (thiophene vs pyrrole vs furan). (3) Explain why thiophene can be sulfonated with concentrated H2SO4 at 30°C without decomposition, whereas furan undergoes catastrophic polymerization unless a mild sulfur trioxide-pyridine complex is used.",
            "solution": r"""#### Part 1: Mechanism of Paal-Knorr Furan Synthesis
1. **Keto-Enol Tautomerism**:
   Hexane-2,5-dione undergoes acid-catalyzed enolization to form the bis-enol (or mono-enol) tautomer:
   $$\text{CH}_3-\text{CO}-\text{CH}_2-\text{CH}_2-\text{CO}-\text{CH}_3 \xrightleftharpoons[\text{H}^+]{} \text{CH}_3-\text{C(OH)}=\text{CH}-\text{CH}_2-\text{CO}-\text{CH}_3 \tag{1}$$
2. **Intramolecular Nucleophilic Attack**:
   The enolic hydroxyl oxygen attacks the protonated carbonyl carbon of the second ketone through a favorable 5-exo-trig cyclization:
   $$\left[ \begin{matrix} \text{CH}_3-\text{C}=\text{CH} \\ \quad \vert \qquad \vert \\ \text{O} \cdots \text{C}(\text{OH})-\text{CH}_3 \end{matrix} \right] \longrightarrow \text{2,5-dimethyl-2,3-dihydrofuran-2-ol} \tag{2}$$
3. **Dehydration**:
   Acid-catalyzed loss of water ($\text{H}_2\text{O}$) establishes the second double bond, generating the aromatic **2,5-dimethylfuran** ($6\pi$ electrons, aromatic)!

#### Part 2: Aromatic Stabilization & Cyclization Energetics
1. **Resonance Stabilization Energies ($RE$)**:
   $$\text{Thiophene } (121\text{ kJ/mol}) > \text{Pyrrole } (88\text{ kJ/mol}) > \text{Furan } (67\text{ kJ/mol})$$
   - Thiophene derives exceptional stabilization from the polarizable sulfur $3p$ orbital and low electronegativity ($\chi = 2.58$).
   - Furan has the lowest resonance energy because oxygen ($\chi = 3.44$) strongly resists sharing its second lone pair into the aromatic sextet.
2. **Driving Force for Cyclization**:
   The synthesis of thiophene ($\Delta H^\circ_{\text{form}} \ll 0$) is thermodynamically the most favored, followed by pyrrole and furan.

#### Part 3: Acid Sensitivity: Thiophene vs Furan
1. **Thiophene**:
   - Possesses high aromatic resonance energy ($121\text{ kJ/mol}$).
   - The sulfur atom has low basicity; protonation does not occur readily.
   - It behaves like a stabilized aromatic ring (similar to benzene), reacting cleanly with electrophilic $\text{SO}_3$ or $\text{H}_2\text{SO}_4$ to form thiophene-2-sulfonic acid in $>90\%$ yield at room temperature.
2. **Furan**:
   - Possesses low aromatic resonance energy ($67\text{ kJ/mol}$).
   - It behaves largely like an electron-rich cyclic conjugated diene / cyclic enol ether.
   - In strong mineral acids ($\text{H}_2\text{SO}_4$), protonation occurs readily at the $\alpha$-carbon (C2) to form an allylic oxocarbenium ion.
   - This highly electrophilic intermediate is attacked immediately by unprotonated furan molecules, triggering a catastrophic runaway cationic polymerization that converts the reaction into an intractable, insoluble black polymer!
   - Therefore, furan can only be sulfonated using the **mild, non-acidic pyridine-$\text{SO}_3$ complex** in neutral solvents at $0-20^\circ\text{C}$!"""
        }
    ])

    return units
