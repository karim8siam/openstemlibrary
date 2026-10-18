# -*- coding: utf-8 -*-
"""
expand_org2_units_4_5_6.py
Enrichment module expanding Units 4, 5, and 6 of Organic Chemistry II to honors depth.
Strict zero course numbers or marks.
Adds deep quantum derivations, extensive physical tables, advanced reaction mechanisms,
and an 8th comprehensive multi-part problem to each unit.
"""

def enrich_units_4_5_6(u4, u5, u6):
    print("Enriching Units 4, 5, and 6 with advanced physical organic content...")

    # --- ENRICH UNIT 4: CARBOXYLIC ACID DERIVATIVES ---
    # Section 4.1: The Weinreb Ketone Synthesis
    u4["sections"][0]["content"] += r"""

### The Weinreb Ketone Synthesis: Chelation-Stabilized Tetrahedral Intermediates

A classic dilemma in organic synthesis is the reaction of esters or acyl chlorides with Grignard or organolithium reagents: addition of one equivalent of nucleophile generates a ketone, which is **more electrophilic than the starting ester** ($k_{\text{ketone}} \gg k_{\text{ester}}$), immediately adding a second equivalent of organometallic to yield an unwanted tertiary alcohol.

In 1981, Steven M. Weinreb solved this fundamental problem by introducing **$N$-methoxy-$N$-methylamides (Weinreb amides)**:

```
       The Weinreb Ketone Synthesis:
            O                                           O(-)
           //                                          /
        R-C      +  R'-MgX   =====>                 R-C-R'
           \                                         / \
            N(OMe)Me                                N   OMe
                                                     \ /
                                                      Mg(2+)X  (Stable 5-Ring Chelate)
                                                        |
                                                        | Aqueous Acidic Workup (H3O+)
                                                        v
                                                 Ketone [R-CO-R']  +  HN(OMe)Me
```

1. **Addition**: The organometallic reagent ($\text{R}'\text{MgX}$ or $\text{R}'\text{Li}$) adds cleanly to the carbonyl carbon of the Weinreb amide.
2. **Chelation Arrest**: The resulting tetrahedral intermediate forms a rigid, highly stable **five-membered bidentate chelate ring** coordinated to the magnesium or lithium cation:
   $$[\text{R}-\text{C}(\text{O}^-)(\text{R}')-\text{N}(\text{Me})-\text{O}^-\cdots\text{Mg}^{2+}\text{X}]$$
3. **Suppression of Over-Addition**: The tetrahedral intermediate **cannot collapse in the reaction mixture** because the methoxy group is locked into the metal chelate. Because the ketone is never formed in the presence of unreacted organometallic reagent, over-addition is fundamentally impossible.
4. **Hydrolytic Release**: Upon aqueous acidic workup ($\text{H}_3\text{O}^+$), the metal chelate is protonated and dismantled, releasing the pure **monosubstituted ketone** in quantitative yield."""

    # Section 4.6: Winsor Phase Systems and Surfactant Microemulsions
    u4["sections"][5]["content"] += r"""

### Winsor Phase Classifications & Surfactant Microemulsion Thermodynamics

In colloidal and interface science, mixtures of water, oil, surfactant, and co-surfactant (typically medium-chain alcohols) form thermodynamically stable, optically transparent **microemulsions**.

In 1948, P. A. Winsor established the four thermodynamic equilibrium phase regimes based on the ratio of interfacial interaction energies ($R$):

$$R = \frac{A_{co}}{A_{cw}} \tag{4.12a}$$

where $A_{co}$ is the net interaction energy between surfactant and oil, and $A_{cw}$ is the net interaction energy between surfactant and water.

```
       Winsor Phase Transitions:
       Winsor I (R < 1):  Two phases: Oil excess on top; O/W microemulsion on bottom.
       Winsor II (R > 1): Two phases: W/O microemulsion on top; Water excess on bottom.
       Winsor III (R = 1): Three phases: Oil excess on top; Middle bicontinuous microemulsion; Water excess on bottom.
       Winsor IV (Single Phase): Single isotropic bicontinuous microemulsion.
```

1. **Winsor I ($R < 1$)**: Surfactant is more hydrophilic ($A_{cw} > A_{co}$). Oil-in-water ($\text{O/W}$) spherical micelles form in the lower aqueous phase in equilibrium with an excess upper oil phase.
2. **Winsor II ($R > 1$)**: Surfactant is more lipophilic ($A_{co} > A_{cw}$). Water-in-oil ($\text{W/O}$) reverse micelles form in the upper oil phase in equilibrium with an excess lower aqueous phase.
3. **Winsor III ($R \approx 1$, Middle-Phase)**: Optimal balance ($A_{co} \approx A_{cw}$). A distinct middle microemulsion phase forms containing an interconnected, sponge-like **bicontinuous network** of water and oil channels, exhibiting ultralow interfacial tensions ($\gamma < 10^{-3}\text{ mN/m}$).
4. **Winsor IV**: At high surfactant concentrations, all oil and water are completely solubilized into a single, isotropic, macroscopic phase."""

    # Add Problem 4.8 to Unit 4
    u4["problems"].append({
        "id": "prob4_8",
        "problemNumber": "4.8",
        "title": "Bouveault-Blanc Reduction vs Hydride Reductions of Esters",
        "difficulty": "Mastery",
        "statement": r"""Before the commercial discovery of lithium aluminium hydride ($\text{LiAlH}_4$) by Finholt, Bond, and Schlesinger in 1947, the industrial reduction of fatty acid esters to fatty alcohols was carried out by the Bouveault-Blanc reduction (Louis Bouveault and Gustave Blanc, 1903) using metallic sodium in absolute ethanol:
$$\text{R-COOEt} + 4\,\text{Na} + 4\,\text{EtOH} \longrightarrow \text{R-CH}_2\text{OH} + 4\,\text{NaOEt}$$
(a) Write the complete electron-transfer mechanism showing all radical-anion, radical, and carbanion intermediates.
(b) Explain why sodium metal in ethanol reduces esters, whereas metallic sodium in dry ether fails to reduce esters and instead promotes the acyloin condensation.
(c) Compare the safety, atom economy, and chemoselectivity of Bouveault-Blanc reduction versus modern catalytic hydrogenation using ruthenium pincer complexes.""",
        "hints": ["Each sodium atom transfers one electron (SET).", "Ethanol acts as an essential proton donor to protonate radical anions."],
        "solution": r"""### (a) Step-by-Step Bouveault-Blanc Mechanism
1. **First Single-Electron Transfer (SET)**:
   A sodium atom transfers one electron from its $3s^1$ orbital into the $\pi^*_{\text{C=O}}$ LUMO of the ester:
   $$\text{R-COOEt} + \text{Na}^\bullet \longrightarrow [\text{R}-\dot{\text{C}}(\text{O}^-)(\text{OEt})] + \text{Na}^+ \quad (\text{radical anion})$$
2. **Protonation by Ethanol**:
   The strongly basic alkoxide oxygen abstracts a proton from solvent ethanol:
   $$[\text{R}-\dot{\text{C}}(\text{O}^-)(\text{OEt})] + \text{EtOH} \longrightarrow [\text{R}-\dot{\text{C}}(\text{OH})(\text{OEt})] + \text{EtO}^- \quad (\text{hemiacetal radical})$$
3. **Second Single-Electron Transfer & Alkoxide Expulsion**:
   A second sodium atom transfers an electron, followed by expulsion of ethoxide:
   $$[\text{R}-\dot{\text{C}}(\text{OH})(\text{OEt})] + \text{Na}^\bullet \longrightarrow [\text{R}-\bar{\text{C}}(\text{OH})(\text{OEt})] \xrightarrow{-\text{EtO}^-} \text{R-CHO} + \text{Na}^+ \quad (\text{aldehyde})$$
4. **Reduction of Intermediate Aldehyde**:
   The aldehyde is more electrophilic than the starting ester. It rapidly undergoes two successive single-electron transfers from two additional sodium atoms with protonation by ethanol:
   $$\text{R-CHO} \xrightarrow{\text{Na}^\bullet} [\text{R}-\dot{\text{C}}\text{H}-\text{O}^-] \xrightarrow{\text{EtOH}} [\text{R}-\dot{\text{C}}\text{H}-\text{OH}] \xrightarrow{\text{Na}^\bullet, \text{EtOH}} \mathbf{\text{R-CH}_2\text{OH}} + 2\,\text{NaOEt}$$
Total stoichiometry: $1\text{ mol ester} + 4\text{ mol Na} + 4\text{ mol EtOH} \longrightarrow 1\text{ mol primary alcohol} + 4\text{ mol NaOEt}$.

### (b) Rationale for Acyloin Condensation in Dry Ether
- **In Absolute Ethanol**: Ethanol acts as a fast, protic **proton donor** ($\text{p}K_a \approx 16$). The initial radical anion $[\text{R}-\dot{\text{C}}(\text{O}^-)(\text{OEt})]$ is instantly protonated on oxygen, preventing it from dimerizing.
- **In Dry Ethereal Solvent (Aprotic)**: In anhydrous refluxing xylene or toluene with no proton donor present, the radical anion cannot be protonated. Instead, two radical-anion monomers dimerize via radical-radical coupling ($\Delta H^\circ \ll 0$):
  $$2\,[\text{R}-\dot{\text{C}}(\text{O}^-)(\text{OEt})] \longrightarrow [\text{EtO}-\text{C}(\text{R})(\text{O}^-)-\text{C}(\text{R})(\text{O}^-)-\text{OEt}]$$
  Subsequent elimination of two ethoxide ions expels an $\alpha$-diketone, which is further reduced by two more sodium atoms to yield an **$\alpha$-hydroxy ketone (acyloin)**!

### (c) Green Chemistry & Industrial Comparison
- **Bouveault-Blanc Reduction**: Extremely hazardous due to pyrophoric sodium metal, violent generation of flammable hydrogen gas upon quenching, and poor atom economy (generates 4 equivalents of $\text{NaOEt}$ waste).
- **Modern Catalytic Hydrogenation**: Uses molecular hydrogen ($\text{H}_2$) with homogeneous ruthenium or manganese pincer catalysts ($[\text{Ru}(\text{MACHO-BH})]$). Operates with $100\%$ atom economy, zero stoichiometric metal waste, and near-quantitative yields under solvent-free conditions."""
    })

    # --- ENRICH UNIT 5: AMINES, DIAZONIUM SALTS & NITRO SYSTEMS ---
    # Section 5.3: The Schmidt and Lossen Rearrangements
    u5["sections"][2]["content"] += r"""

### The Schmidt and Lossen Rearrangements: Nitrene-Like Migrations

In addition to the Hofmann and Curtius rearrangements, two related sigmatropic transformations construct primary amines with the loss of a carbonyl carbon:

```
Related [1,2]-Nitrogen Rearrangement Family:
1. Hofmann:  R-CONH2      + Br2 / NaOH       ===> [R-CO-N-Br](-)     ---> R-N=C=O ---> R-NH2
2. Curtius:  R-COCl       + NaN3             ===> R-CO-N3            ---> R-N=C=O ---> R-NH2
3. Lossen:   R-CONH-OH    + Ac2O / Base      ===> R-CO-N-OAc         ---> R-N=C=O ---> R-NH2
4. Schmidt:  R-COOH       + HN3 / H2SO4      ===> R-CO-NH-N2(+)      ---> R-N=C=O ---> R-NH2
```

1. **The Lossen Rearrangement (Hydroxamic Acids)**:
   - A hydroxamic acid ($\text{R-CONH-OH}$) is acylated to form an $O$-acyl derivative ($\text{R-CONH-OAc}$).
   - Treatment with base deprotonates the nitrogen.
   - Spontaneous elimination of acetate ($\text{AcO}^-$) triggers concerted [1,2]-migration of group $\text{R}$ to form an isocyanate ($\text{R-N}=\text{C}=\text{O}$), which hydrolyzes to primary amine $\text{RNH}_2$.
   - Does not require explosive azides or toxic bromine.
2. **The Schmidt Reaction of Carboxylic Acids & Ketones**:
   - **With Carboxylic Acids**: Reaction with hydrazoic acid ($\text{HN}_3$) in concentrated $\text{H}_2\text{SO}_4$:
     $$\text{R-COOH} + \text{HN}_3 \xrightarrow{\text{conc. }\text{H}_2\text{SO}_4} \text{R-NH}_2 + \text{CO}_2\uparrow + \text{N}_2\uparrow \tag{5.8a}$$
   - **With Ketones**: Reaction of cyclic ketones with $\text{HN}_3$ yields **lactams** (e.g., cyclohexanone gives $\epsilon$-caprolactam, the monomer for Nylon-6):
     $$\text{Cyclohexanone} + \text{HN}_3 \xrightarrow{\text{H}_2\text{SO}_4} \epsilon\text{-Caprolactam} + \text{N}_2\uparrow \tag{5.8b}$$"""

    # Section 5.4: Sommelet-Hauser and Stevens Rearrangements of Ammonium Ylides
    u5["sections"][3]["content"] += r"""

### Rearrangements of Ammonium Ylides: Sommelet-Hauser vs Stevens

Quaternary ammonium salts possessing $\alpha$-hydrogens can be deprotonated by strong bases (e.g., $\text{NaNH}_2$ in liquid ammonia or $\text{PhLi}$) to form **ammonium ylides** ($[\text{R}_3\text{N}^+-\text{C}^-\text{H}_2]$). These ylides undergo two competing rearrangements:

1. **The Sommelet-Hauser Rearrangement ([2,3]-Sigmatropic Shift)**:
   - In benzylic ammonium ylides (such as benzyldimethylammonium methylide):
   - The ylide undergoes a concerted **[2,3]-sigmatropic rearrangement** into the aromatic ring.
   - Rearomatization yields an *ortho*-substituted benzylic tertiary amine:
     $$[\text{PhCH}_2-\text{N}^+(\text{Me})_2-\text{CH}_2^-] \longrightarrow o\text{-CH}_3-\text{C}_6\text{H}_4-\text{CH}_2\text{NMe}_2 \tag{5.11a}$$
   - Operates under kinetic control at low temperatures ($-33^\circ\text{C}$).
2. **The Stevens Rearrangement ([1,2]-Shift)**:
   - At higher temperatures or with sterically constrained ylides, the ylide undergoes homolytic cleavage into a radical pair within a solvent cage:
     $$[\text{R}_3\text{N}^+-\text{C}^-\text{H}_2] \longrightarrow [\text{R}_2\text{N}-\dot{\text{C}}\text{H}_2 \,\, \text{R}^\bullet]_{\text{cage}} \longrightarrow \text{R}_2\text{N}-\text{CH}_2\text{-R} \tag{5.11b}$$
   - Recombination within the cage occurs with substantial retention of configuration."""

    # Add Problem 5.8 to Unit 5
    u5["problems"].append({
        "id": "prob5_8",
        "problemNumber": "5.8",
        "title": "The Eschweiler-Clarke Reductive Methylation Mechanism",
        "difficulty": "Mastery",
        "statement": r"""A chemist converts primary benzylamine into $N,N$-dimethylbenzylamine in $96\%$ yield by heating with excess formaldehyde and formic acid:
$$\text{PhCH}_2\text{NH}_2 + 2\,\text{HCHO} + 2\,\text{HCOOH} \xrightarrow{100^\circ\text{C}} \text{PhCH}_2\text{N(CH}_3)_2 + 2\,\text{CO}_2\uparrow + 2\,\text{H}_2\text{O}$$
(a) Write the complete mechanism for the first methylation, showing the imine/iminium intermediate.
(b) Identify the reducing agent that provides the hydride ion ($\text{H}^-$) to reduce the iminium ion to the methylamine, and write the curved arrows showing its oxidation.
(c) Why does this reaction stop cleanly at the tertiary amine without forming any quaternary ammonium salt ($[\text{PhCH}_2\text{N(Me)}_3]^+$)?""",
        "hints": ["Formic acid acts as both a source of protons and a source of hydride.", "Quaternization requires a formal alkylating agent, not an iminium ion."],
        "solution": r"""### (a) Step-by-Step Mechanism for First Methylation
$$\begin{aligned}
\text{Step 1 (Imine Formation)}: &\quad \text{PhCH}_2\text{NH}_2 + \text{HCHO} \rightleftharpoons \text{PhCH}_2\text{NH-CH}_2\text{OH} \xrightarrow{-\text{H}_2\text{O}} \text{PhCH}_2\text{-N}=\text{CH}_2 \\
\text{Step 2 (Iminium Generation)}: &\quad \text{PhCH}_2\text{-N}=\text{CH}_2 + \text{HCOOH} \rightleftharpoons [\text{PhCH}_2-\text{N}^+\text{H}=\text{CH}_2] + \text{HCOO}^- \\
\text{Step 3 (Hydride Transfer)}: &\quad \text{Formate anion acts as hydride donor to iminium carbon} \\
&\quad [\text{H}-\text{COO}^-] + [\text{PhCH}_2-\text{N}^+\text{H}=\text{CH}_2] \longrightarrow \text{CO}_2\uparrow + \text{PhCH}_2\text{-NH-CH}_3 \\
\text{Step 4 (Second Methylation)}: &\quad \text{Secondary amine undergoes identical cycle with 2nd HCHO/HCOOH to yield }\mathbf{\text{PhCH}_2\text{N(CH}_3)_2}
\end{aligned}$$

### (b) Identity and Oxidation of the Reducing Agent
The reducing agent is the **formate anion ($\text{H}-\text{COO}^-$)** derived from formic acid.
- The $\text{C}-\text{H}$ $\sigma$-bonding electron pair of the formate ion attacks the electrophilic carbon of the iminium cation as a **hydride ion ($\text{H}^-$)**:
  $$[\text{O}=\text{C}(\text{O}^-)-\mathbf{H}] \,\, \curvearrowright \,\, [\mathbf{C}\text{H}_2=\text{N}^+\text{H}-\text{CH}_2\text{Ph}]$$
- Cleavage of the formate $\text{C}-\text{H}$ bond expels carbon dioxide gas ($\text{O}=\text{C}=\text{O}\uparrow$), which bubbles irreversibly out of solution, providing a massive entropic driving force ($\Delta S^\circ \gg 0$).

### (c) Suppression of Quaternary Ammonium Formation
To undergo methylation in the Eschweiler-Clarke reaction:
1. The amine must possess a **lone pair on nitrogen** to attack formaldehyde and form an iminium cation.
2. The iminium intermediate requires an attached proton or alkyl group that allows dehydration.
Once the amine reaches the **tertiary amine stage** ($\text{PhCH}_2\text{NMe}_2$):
- It can no longer form an iminium ion with formaldehyde because nitrogen has no remaining hydrogens to eliminate water.
- Because there is no free methylating electrophile (such as $\text{CH}_3\text{I}$) present in the solution, quaternization is fundamentally impossible. The reaction ceases with **$100\%$ chemoselectivity** at the tertiary amine."""
    })

    # --- ENRICH UNIT 6: STEREOCHEMISTRY AND RESOLUTION ---
    # Section 6.2: Circular Dichroism & The Octant Rule
    u6["sections"][1]["content"] += r"""

### Circular Dichroism (CD) Spectroscopy & The Carbonyl Octant Rule

Optical activity manifests across the electromagnetic spectrum via two chiroptical phenomena:
1. **Optical Rotatory Dispersion (ORD)**: The variation of specific rotation $[\alpha]_\lambda$ as a function of wavelength.
2. **Circular Dichroism (CD)**: The differential absorption of left- versus right-circularly polarized light by a chiral chromophore:
   $$\Delta \epsilon = \epsilon_L - \epsilon_R \tag{6.6a}$$

In an absorption band (such as the $n \to \pi^*$ transition of a carbonyl group at $\sim 290\text{ nm}$), CD exhibits a peak or trough known as the **Cotton effect**:
- **Positive Cotton Effect**: $\Delta \epsilon > 0$ (absorption of left-circularly polarized light exceeds right).
- **Negative Cotton Effect**: $\Delta \epsilon < 0$.

```
               The Cyclohexanone Carbonyl Octant Rule:
                       Plane B (Nodal Plane of pi*)
                              |
                     Back-Upper-Left   | Back-Upper-Right
                          (+)          |      (-)
                 Plane A --------------+-------------- Plane A (C=O and Calpha plane)
                     Back-Lower-Left   | Back-Lower-Right
                          (-)          |      (+)
                              |
```

### The Octant Rule for Saturated Cyclohexanones
Formulated by William Moffitt, Albert Moscowitz, Robert Woodward, William Klyne, and Carl Djerassi in 1961:
- Three mutually perpendicular symmetry planes divide the space surrounding the carbonyl group into **eight octants**:
  - **Plane A**: The horizontal plane containing $\text{C}=\text{O}$ and $\text{C}_\alpha$ atoms (C1, C2, C6).
  - **Plane B**: The vertical plane perpendicular to Plane A passing through the carbonyl carbon and oxygen.
  - **Plane C**: The nodal surface plane perpendicular to the $\text{C}=\text{O}$ bond passing through the carbon atom.
- Substituents lying in the nodal planes contribute zero to the Cotton effect.
- Substituents in the **Back-Upper-Left** and **Back-Lower-Right** octants make a **positive ($+$)** contribution to $\Delta \epsilon$.
- Substituents in the **Back-Upper-Right** and **Back-Lower-Left** octants make a **negative ($-$)** contribution to $\Delta \epsilon$.
This empirical rule enables unequivocal determination of the absolute configuration and conformation of steroids and terpenes without X-ray crystallography."""

    # Section 6.6: Sharpless Asymmetric Epoxidation
    u6["sections"][5]["content"] += r"""

### The Sharpless Asymmetric Epoxidation: Titanium Tartrate Dimer Geometry

Discovered by K. Barry Sharpless in 1980 (2001 Nobel Prize in Chemistry), the **Sharpless asymmetric epoxidation** converts prochiral allylic alcohols into chiral 2,3-epoxy alcohols with enantiomeric excesses exceeding $95\%$:

$$\text{Allylic Alcohol} + t\text{-BuOOH} \xrightarrow{\text{Ti(O}i\text{-Pr)}_4, \text{diethyl tartrate (DET)}, 4\text{\AA MS}, -20^\circ\text{C}} \text{Chiral Epoxy Alcohol} \tag{6.11a}$$

```
                Sharpless Epoxidation Mnemonics:
                          R (Allylic Alcohol)
                          |
                          C = C
                         /     \
                        H       CH2OH (Drawn at Bottom-Right)
                                  |
            + (+)-Diethyl Tartrate ===> Oxygen delivered from BOTTOM Face
            + (-)-Diethyl Tartrate ===> Oxygen delivered from TOP Face
```

### The Dimeric Catalyst Architecture
1. **Active Catalyst Structure**: The catalyst exists in solution as a $C_2$-symmetric **dimeric titanium tartrate complex** $[\text{Ti}_2(\text{DET})_2(\text{O}i\text{-Pr})_4]$.
2. **Substrate Assembly**: The allylic alcohol and *tert*-butyl hydroperoxide ($t\text{-BuOOH}$) displace two isopropoxide ligands, binding simultaneously to one titanium center in a rigid, stereospecific orientation.
3. **Face Selection**:
   - Orient the allylic alcohol in the plane with the $-\text{CH}_2\text{OH}$ group in the **bottom-right quadrant**.
   - With **(+)-diethyl tartrate** (also designated L-(+)-DET or $(2R,3R)$-DET): Oxygen is delivered exclusively from the **bottom face ($\alpha$-face)** of the alkene.
   - With **(-)-diethyl tartrate** (D-(-)-DET or $(2S,3S)$-DET): Oxygen is delivered exclusively from the **top face ($\beta$-face)**."""

    # Add Problem 6.8 to Unit 6
    u6["problems"].append({
        "id": "prob6_8",
        "problemNumber": "6.8",
        "title": "Sharpless Asymmetric Epoxidation Stereochemical Model & Tartrate Control",
        "difficulty": "Mastery",
        "statement": r"""Predict the absolute stereochemical configuration of the epoxide product formed when (E)-hex-2-en-1-ol is subjected to Sharpless asymmetric epoxidation with:
(a) (+)-diethyl tartrate ((2R,3R)-DET), $\text{Ti(O}i\text{-Pr)}_4$, and $t\text{-BuOOH}$.
(b) (-)-diethyl tartrate ((2S,3S)-DET), $\text{Ti(O}i\text{-Pr)}_4$, and $t\text{-BuOOH}$.
(c) Draw the substrate in the standard Sharpless quadrant orientation, determine the face of oxygen attack, and assign the CIP stereodescriptors ((2R,3R) vs (2S,3S)) for both products.""",
        "hints": ["Draw the CH2OH group in the bottom-right corner.", "(+)-DET delivers oxygen from the bottom face; (-)-DET delivers oxygen from the top face."],
        "solution": r"""### (a) Reaction with (+)-Diethyl Tartrate ((2R,3R)-DET)
1. **Substrate Orientation**:
   Place *(E)*-hex-2-en-1-ol ($\text{CH}_3\text{CH}_2\text{CH}_2-\text{CH}=\text{CH}-\text{CH}_2\text{OH}$) in the standard Sharpless coordinate frame:
   - The double bond lies horizontally.
   - The hydroxymethyl group ($-\text{CH}_2\text{OH}$) is positioned in the **bottom right**.
   - Because the alkene has *(E)*-geometry, the propyl group ($-\text{CH}_2\text{CH}_2\text{CH}_3$) projects to the **top left**.
2. **Face of Attack with (+)-DET**:
   According to the Sharpless mnemonic:
   $$(+)\text{-DET} \implies \text{Oxygen is delivered from the BOTTOM face}$$
3. **Product Stereochemistry**:
   Oxygen adds from the bottom face across C2 and C3:
   - At C2: The epoxide oxygen is below the plane ($\alpha$), pushing the C1 $-\text{CH}_2\text{OH}$ group above the plane ($\beta$).
   - At C3: The epoxide oxygen is below the plane ($\alpha$), pushing the propyl group above the plane ($\beta$).
   Assigning CIP priorities at C2:
   1. Epoxide $-\text{O}-$ (Priority 1)
   2. C3 of epoxide ring (Priority 2)
   3. $-\text{CH}_2\text{OH}$ (Priority 3)
   4. $-\text{H}$ (Priority 4)
   This yields **(2S,3S)-2,3-epoxyhexan-1-ol** with $>96\%$ enantiomeric excess ($ee$).

### (b) Reaction with (-)-Diethyl Tartrate ((2S,3S)-DET)
1. **Face of Attack with (-)-DET**:
   $$(-)\text{-DET} \implies \text{Oxygen is delivered from the TOP face}$$
2. **Product Stereochemistry**:
   Oxygen adds from the top face ($\beta$):
   - Both epoxide $\text{C}-\text{O}$ bonds point upward.
   - The $-\text{CH}_2\text{OH}$ group and propyl group are pushed below the plane ($\alpha$).
   This yields the enantiomer: **(2R,3R)-2,3-epoxyhexan-1-ol** with $>96\%$ enantiomeric excess ($ee$).

### (c) Mechanistic Verification
The reaction proceeds through a dimeric $[\text{Ti}_2(\text{tartrate})_2]$ complex where the allylic alcohol coordinates as an alkoxide and the hydroperoxide coordinates as a bidentate peroxo ligand. The chiral tartrate ligands distort the coordination sphere around titanium, creating a deep steric barrier on one face while holding the alkyl hydroperoxide oxygen in perfect alignment with the opposite face of the alkene."""
    })

    print("Units 4, 5, and 6 successfully expanded!")
