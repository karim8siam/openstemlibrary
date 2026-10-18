# -*- coding: utf-8 -*-
"""
build_org2_units_4_5_6.py
Rigorous honors-level curriculum generator for Units 4, 5, and 6 of Organic Chemistry II.
Strict zero course numbers or marks.
Contains massive depth, comprehensive KaTeX proofs, thermodynamic parameters, reaction tables,
and 7-8 multi-tier solved problems per unit with step-by-step solutions.
"""

def get_unit_4():
    return {
        "id": "unit4",
        "unitId": "unit4-org2",
        "number": 4,
        "unitNumber": 4,
        "title": "Unit 4: Carboxylic Acid Derivatives, Nitriles, Soaps & Detergents",
        "description": "Exhaustive mechanistic analysis of carboxylic acid derivatives: nucleophilic acyl substitution (S_NAc) tetrahedral intermediate matrices, leaving group pKa scales, interconversion hierarchies, acidic (A_AC2) and basic (B_AC2) ester hydrolysis kinetics, amide resonance barriers and restricted rotation, nitrile transformations, and the physical chemistry of amphiphilic soaps, synthetic detergents, critical micelle concentration (CMC) thermodynamics, and hard-water sequestration.",
        "leadSummary": "Comprehensive physical organic treatise on tetrahedral intermediate dynamics, nucleophilic acyl substitution hierarchies, ester/amide kinetics, nitrile syntheses, surfactant self-assembly thermodynamics, and colloidal micelle mechanics.",
        "simulations": ["sim_chem_carboxylic_derivative_tetrahedral_matrix"],
        "sections": [
            {
                "id": "sec4_1",
                "secNumber": "§4.1",
                "title": "Nucleophilic Acyl Substitution ($S_N\text{Ac}$): The Tetrahedral Intermediate Matrix",
                "heading": "Nucleophilic Acyl Substitution ($S_N\text{Ac}$): The Tetrahedral Intermediate Matrix",
                "content": r"""Unlike aldehydes and ketones—which undergo nucleophilic addition to yield stable or protonated tetrahedral adducts—carboxylic acid derivatives ($\text{R}-\text{C}(=\text{O})-\text{L}$) undergo **nucleophilic acyl substitution** ($S_N\text{Ac}$). The presence of a heteroatomic leaving group ($\text{L}$) allows the tetrahedral intermediate to collapse, regenerating the thermodynamically stabilized $\text{C}=\text{O}$ double bond.

```
       Nucleophilic Acyl Substitution (S_NAc) Coordinate:
               O                             O(-)                         O
              //                            /                            //
           R-C     +  :Nu(-)   <===>     R-C-L       =====>           R-C     +  :L(-)
              \                             \                            \
               L                             Nu                           Nu
        Planar sp2                  Tetrahedral sp3              Planar sp2
        Reactant                    Intermediate                 Product
```

### The Two-Stage Addition-Elimination Mechanism
The universal $S_N\text{Ac}$ pathway proceeds in two discrete stages:
1. **Stage 1 (Nucleophilic Addition)**: The nucleophile attacks the carbonyl carbon along the Bürgi-Dunitz angle ($\sim 107^\circ$), converting the planar $sp^2$ carbonyl carbon into a tetrahedral $sp^3$-hybridized alkoxide intermediate:
   $$\text{R}-\text{CO}-\text{L} + \text{Nu}^- \xrightleftharpoons[k_{-1}]{k_1} [\text{R}-\text{C}(\text{O}^-)(\text{L})(\text{Nu})] \tag{4.1}$$
2. **Stage 2 (Elimination / Expulsion)**: The alkoxide oxygen reforms the $\text{C}=\text{O}$ $\pi$ bond, expelling the group with the highest leaving group ability (lowest conjugate acid $\text{p}K_a$):
   $$[\text{R}-\text{C}(\text{O}^-)(\text{L})(\text{Nu})] \xrightarrow{k_2} \text{R}-\text{CO}-\text{Nu} + \text{L}^- \tag{4.2}$$

### The Universal Reactivity Hierarchy & $\text{p}K_a$ Correlation
The rate of nucleophilic acyl substitution depends on two factors:
1. The electrophilicity of the carbonyl carbon (dictated by the $-I$ vs $+M$ balance of substituent $\text{L}$).
2. The leaving group ability of $\text{L}^-$, which is directly proportional to the acidity of its conjugate acid ($\text{H}-\text{L}$):

$$\text{Leaving Group Ability} \propto \frac{1}{\text{p}K_a(\text{HL})} \tag{4.3}$$

| Derivative Class | Formula | Leaving Group ($\text{L}^-$) | Conjugate Acid ($\text{HL}$) | $\text{p}K_a(\text{HL})$ | Relative $S_N\text{Ac}$ Rate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Acyl Halides** | $\text{R-COCl}$ | $\text{Cl}^-$ | $\text{HCl}$ | **$-7.0$** | $10^8$ (Violent hydrolysis) |
| **Acid Anhydrides** | $(\text{RCO})_2\text{O}$ | $\text{RCOO}^-$ | $\text{RCOOH}$ | **$+4.8$** | $10^5$ (Rapid hydrolysis) |
| **Esters** | $\text{R-COOR}'$ | $\text{R'O}^-$ | $\text{R'OH}$ | **$+16.0$** | $1.0$ (Requires catalysis) |
| **Amides** | $\text{R-CONH}_2$ | $\text{NH}_2^-$ | $\text{NH}_3$ | **$+38.0$** | $10^{-4}$ (Requires prolonged reflux) |
| **Carboxylate Anions** | $\text{R-COO}^-$ | $\text{O}^{2-}$ | $\text{OH}^-$ | **$>50$** | $0$ (Unreactive toward nucleophiles) |

This hierarchy establishes the **fundamental rule of acyl interconversion**: A more reactive carboxylic acid derivative can be converted cleanly into a less reactive derivative, but the reverse transformation is thermodynamically impossible without an activating agent (such as $\text{SOCl}_2, \text{PCl}_5$, or coupling reagents like $\text{DCC}$).""",
                "simulations": ["sim_chem_carboxylic_derivative_tetrahedral_matrix"]
            },
            {
                "id": "sec4_2",
                "secNumber": "§4.2",
                "title": "Acyl Halides & Acid Anhydrides: Syntheses, Kinetics & Chemoselectivity",
                "heading": "Acyl Halides & Acid Anhydrides: Syntheses, Kinetics & Chemoselectivity",
                "content": r"""Acyl halides ($\text{RCOCl}$) and acid anhydrides ($(\text{RCO})_2\text{O}$) are the premier reactive acylating agents in laboratory synthesis.

### Preparation of Acyl Chlorides: Thionyl Chloride vs Oxalyl Chloride
1. **Thionyl Chloride ($\text{SOCl}_2$)**:
   $$\text{RCOOH} + \text{SOCl}_2 \xrightarrow{\text{cat. DMF}} \text{RCOCl} + \text{SO}_2\uparrow + \text{HCl}\uparrow \tag{4.4}$$
   The reaction is driven to completion by the irreversible evolution of two gaseous by-products ($\text{SO}_2$ and $\text{HCl}$), leaving pure acyl chloride without aqueous extraction. The Vilsmeier-Haack chloroiminium intermediate generated by catalytic dimethylformamide ($\text{DMF}$) accelerates conversion $>100$-fold.
2. **Oxalyl Chloride ($(\text{COCl})_2$)**:
   $$\text{RCOOH} + (\text{COCl})_2 \xrightarrow{\text{cat. DMF, DCM, }0^\circ\text{C}} \text{RCOCl} + \text{CO}\uparrow + \text{CO}_2\uparrow + \text{HCl}\uparrow \tag{4.5}$$
   Operates under extraordinarily mild neutral conditions, preserving acid-sensitive stereocenters and protecting groups.

### Syntheses and Reactions of Acid Anhydrides
- **Cyclic Anhydrides**: Dicarboxylic acids with 4 or 5 carbon chain lengths (succinic acid, glutaric acid, phthalic acid) undergo facile thermal dehydration at $150^\circ\text{–}180^\circ\text{C}$ to form stable five- and six-membered cyclic anhydrides.
- **Nucleophilic Cleavage**: Anhydrides react with alcohols in the presence of pyridine or 4-dimethylaminopyridine ($\text{DMAP}$, Steglich catalysis) to furnish one equivalent of ester and one equivalent of carboxylic acid salt:
  $$\text{RCO-O-COR} + \text{R}'\text{OH} \xrightarrow{\text{DMAP}} \text{RCOOR}' + \text{RCOOH} \tag{4.6}$$
  DMAP acts as a nucleophilic catalyst by attacking the anhydride to form a resonance-stabilized $N$-acylpyridinium salt with a dramatically elevated LUMO electrophilicity.""",
                "simulations": []
            },
            {
                "id": "sec4_3",
                "secNumber": "§4.3",
                "title": "Esters & Lactones: Ingold Mechanisms of Hydrolysis ($B_{\text{AC}}2$ vs $A_{\text{AC}}2$ vs $A_{\text{AL}}1$)",
                "heading": "Esters & Lactones: Ingold Mechanisms of Hydrolysis ($B_{\text{AC}}2$ vs $A_{\text{AC}}2$ vs $A_{\text{AL}}1$)",
                "content": r"""Sir Christopher Ingold classified the mechanisms of ester hydrolysis based on three structural criteria:
- **Catalysis**: Base-catalyzed ($B$) or Acid-catalyzed ($A$).
- **Bond Cleavage**: Acyl-oxygen cleavage ($\text{AC}$) or Alkyl-oxygen cleavage ($\text{AL}$).
- **Kinetic Molecularity**: Unimolecular ($1$) or Bimolecular ($2$).

### 1. Basic Hydrolysis / Saponification ($B_{\text{AC}}2$)
The universal mechanism for base-promoted ester hydrolysis is **$B_{\text{AC}}2$** (Base-catalyzed, Acyl-oxygen cleavage, Bimolecular):

$$\text{RCOOR}' + \text{OH}^- \xrightarrow{k_1} [\text{R}-\text{C}(\text{O}^-)(\text{OH})(\text{OR}')] \xrightarrow{k_2} \text{RCOOH} + \text{R}'\text{O}^- \xrightarrow{\text{fast}} \text{RCOO}^- + \text{R}'\text{OH} \tag{4.7}$$

- **Kinetic Order**: Second-order overall: $\text{Rate} = k_2 [\text{ester}][\text{OH}^-]$.
- **Irreversibility**: The final proton transfer from the newly formed carboxylic acid ($\text{p}K_a \approx 4.8$) to alkoxide ($\text{p}K_a \approx 16$) is completely irreversible ($\Delta G^\circ \approx -65\text{ kJ}\cdot\text{mol}^{-1}$), pulling the entire sequence to completion. Saponification therefore consumes stoichiometric hydroxide rather than being catalytic.
- **Stereochemical Proof**: Hydrolysis of an ester possessing a chiral alcohol group (e.g., $(R)\text{-2-octyl acetate}$) in $^{18}\text{O}$-labeled water yields $(R)\text{-2-octanol}$ with **100% retention of configuration** and zero $^{18}\text{O}$ incorporation into the alcohol, demonstrating that the alkyl-oxygen bond never breaks.

### 2. Acid-Catalyzed Hydrolysis ($A_{\text{AC}}2$)
Under acidic conditions with ordinary primary or secondary alkyl groups, hydrolysis proceeds via the reversible **$A_{\text{AC}}2$** mechanism:
1. Protonation of carbonyl oxygen: $\text{RCOOR}' + \text{H}^+ \rightleftharpoons \text{RC}(=\text{O}^+\text{H})\text{OR}'$.
2. Reversible addition of $\text{H}_2\text{O}$ to form tetrahedral $[\text{RC}(\text{OH})_2(\text{O}^+\text{H}\text{R}')]$.
3. Proton transfer to the alkoxyl oxygen: $[\text{RC}(\text{OH})_2(\text{OH}\text{R}')^+]$.
4. Expulsion of $\text{R}'\text{OH}$ to yield protonated acid $[\text{RC}(\text{OH})_2]^+$.
5. Deprotonation yields carboxylic acid $\text{RCOOH}$ and regenerates the $\text{H}^+$ catalyst.
Every step is fully reversible; the reverse pathway represents Fischer esterification.

### 3. Sterically Hindered Cleavage ($A_{\text{AL}}1$)
Esters of tertiary alcohols (e.g., *tert*-butyl acetate) hydrolyze in acid via the **$A_{\text{AL}}1$** mechanism (Acid-catalyzed, Alkyl-oxygen cleavage, Unimolecular):
1. Protonation of the ether oxygen: $\text{RCOOCMe}_3 + \text{H}^+ \rightleftharpoons \text{RCOO}^+-\text{CMe}_3$.
2. Heterolytic cleavage of the alkyl-oxygen bond yields neutral carboxylic acid and a stable tertiary carbocation:
   $$\text{RCOO}^+-\text{CMe}_3 \xrightarrow{\text{slow}} \text{RCOOH} + [\text{CMe}_3]^+ \tag{4.8}$$
3. Rapid trapping of the carbocation by water gives *tert*-butanol, or elimination gives isobutylene gas. This mechanism provides the foundation for the acid-cleavable Boc and *t*-butyl ester protecting groups.""",
                "simulations": []
            },
            {
                "id": "sec4_4",
                "secNumber": "§4.4",
                "title": "Amides & Peptides: Resonance Stabilization, Restricted Rotation & Planarity",
                "heading": "Amides & Peptides: Resonance Stabilization, Restricted Rotation & Planarity",
                "content": r"""Amides ($\text{RCONR}_2'$) are the most stable carboxylic acid derivatives and form the chemical foundation of all proteins and synthetic polyamides (Nylon).

### The Amide Resonance Dipole & Pauling Model
The exceptional thermodynamic stability of amides arises from powerful resonance donation of the nitrogen lone pair into the adjacent carbonyl $\pi^*$ system:

```
Amide Dipolar Resonance:
       O                              O(-)
      //                             /
   R-C        <============>      R-C
      \                              \\
       N-R'                           N(+)-R'
        \                              \
         R''                            R''
   Major Neutral (60%)            Major Zwitterionic (40%)
```

This resonance interaction has dramatic structural consequences:
1. **Bond Length Shortening**: The $\text{C}-\text{N}$ bond distance in formamide is $1.325\text{ \AA}$, substantially shorter than an aliphatic $\text{C}-\text{N}$ single bond ($1.47\text{ \AA}$) and approaching an isolated $\text{C}=\text{N}$ double bond ($1.28\text{ \AA}$).
2. **$sp^2$ Planarity**: The nitrogen atom adopts nearly pure $sp^2$ hybridization with trigonal planar geometry ($120^\circ$ bond angles) rather than pyramidal $sp^3$ geometry ($109.5^\circ$), maximizing $2p_z\text{–}2p_z$ parallel $\pi$-orbital overlap.
3. **Elevated Dipole Moment**: The zwitterionic contributor contributes $\sim 40\%$ to the ground state, producing large molecular dipole moments ($\mu \approx 3.8\text{ D}$) and exceptionally high boiling points.

### The Barrier to Internal Rotation ($\Delta G^\ddagger$)
Because the $\text{C}-\text{N}$ bond possesses approximately $40\%$ double-bond character, rotation about the central carbon-nitrogen bond is severely restricted:

$$\Delta G^\ddagger_{\text{rotation}} \approx 75\text{–}88\text{ kJ}\cdot\text{mol}^{-1} \quad (18\text{–}21\text{ kcal}\cdot\text{mol}^{-1}) \tag{4.9}$$

In $N,N$-dimethylformamide ($\text{DMF}$), this barrier causes the two methyl groups (one *cis* to carbonyl oxygen, one *trans*) to reside in distinct chemical environments at room temperature.
- At $25^\circ\text{C}$, $^1\text{H}$ NMR spectroscopy shows two sharp singlets for the methyl groups at $\delta = 2.79\text{ ppm}$ and $\delta = 2.94\text{ ppm}$.
- Upon heating above the **coalescence temperature** ($T_c \approx 120^\circ\text{C}$), thermal energy overcomes the rotational barrier:
  $$k_{\text{rot}} = \frac{\pi (\Delta \nu)}{\sqrt{2}} \approx \frac{\pi (45\text{ Hz})}{1.414} \approx 100\text{ s}^{-1} \tag{4.10}$$
  The two peaks coalesce into a single, time-averaged singlet, verifying the dynamic rotational exchange.""",
                "simulations": []
            },
            {
                "id": "sec4_5",
                "secNumber": "§4.5",
                "title": "Nitrile Chemistry: Structure, Electrophilicity, Hydrolysis & the Ritter Reaction",
                "heading": "Nitrile Chemistry: Structure, Electrophilicity, Hydrolysis & the Ritter Reaction",
                "content": r"""Nitriles ($\text{R}-\text{C}\equiv\text{N}$) contain a carbon-nitrogen triple bond ($1.16\text{ \AA}$) consisting of one $\sigma$ bond formed by collinear $sp-sp$ overlap and two orthogonal $\pi$ bonds.

### Synthetic Access: Halide Substitution & Amide Dehydration
1. **$S_N2$ Cyanation**: Reaction of primary or secondary alkyl halides with sodium cyanide in polar aprotic solvents ($\text{DMSO, DMF}$):
   $$\text{R-CH}_2\text{-Br} + \text{NaCN} \xrightarrow{\text{DMSO}} \text{R-CH}_2\text{-C}\equiv\text{N} + \text{NaBr}$$
2. **Dehydration of Primary Amides**: Heating primary amides with phosphorus pentoxide ($\text{P}_4\text{O}_{10}$) or thionyl chloride:
   $$\text{R-CONH}_2 + \text{SOCl}_2 \xrightarrow{\Delta} \text{R-C}\equiv\text{N} + \text{SO}_2\uparrow + 2\,\text{HCl}\uparrow$$

### Chemical Transformations
- **Hydrolysis**: Stepwise hydrolysis via protonated/deprotonated nitrilium species yields primary amides, which hydrolyze rapidly to carboxylic acids.
- **Reduction**: Catalytic hydrogenation over Raney nickel or treatment with $\text{LiAlH}_4$ reduces nitriles to primary amines ($\text{RCH}_2\text{NH}_2$). Selective reduction with diisobutylaluminium hydride ($\text{DIBAL-H}$) at $-78^\circ\text{C}$ affords aldehydes ($\text{RCHO}$) via imine intermediate trapping.
- **The Ritter Reaction**: Reaction of nitriles with secondary or tertiary carbocations (generated from alcohols or alkenes in concentrated $\text{H}_2\text{SO}_4$) yields $N$-alkylamides:
  $$\text{Me}_3\text{C-OH} + \text{H}_2\text{SO}_4 \longrightarrow [\text{Me}_3\text{C}]^+ \xrightarrow{:\text{N}\equiv\text{C-R}} [\text{Me}_3\text{C}-\text{N}^+\equiv\text{C-R}] \xrightarrow{\text{H}_2\text{O}} \text{RCONH-CMe}_3 \tag{4.11}$$
  This reaction provides an indispensable industrial pathway to bulky *tert*-alkyl amides.""",
                "simulations": []
            },
            {
                "id": "sec4_6",
                "secNumber": "§4.6",
                "title": "Soaps & Saponification: Triacylglycerols, Micelles & Surface Chemistry",
                "heading": "Soaps & Saponification: Triacylglycerols, Micelles & Surface Chemistry",
                "content": r"""Soaps are sodium or potassium salts of long-chain fatty acids ($\text{C}_{12}\text{–}\text{C}_{18}$), manufactured by the alkaline hydrolysis (**saponification**) of naturally occurring fats and oils (triacylglycerols).

### Triacylglycerol Saponification
Natural fats consist of triesters of glycerol (propane-1,2,3-triol) with unbranched aliphatic carboxylic acids:

$$\begin{aligned}
\text{Triacylglycerol} + 3\,\text{NaOH} &\xrightarrow{\Delta, \text{H}_2\text{O}} \text{Glycerol} + 3\,\text{R-COO}^-\text{Na}^+ \\
\text{CH}_2(\text{OOCR}_1)-\text{CH}(\text{OOCR}_2)-\text{CH}_2(\text{OOCR}_3) + 3\,\text{NaOH} &\longrightarrow \text{C}_3\text{H}_8\text{O}_3 + \sum_{i=1}^3 \text{R}_i\text{COONa}
\end{aligned} \tag{4.12}$$

Common fatty acids include saturated palmitic acid ($\text{C}_{15}\text{H}_{31}\text{COOH}$), stearic acid ($\text{C}_{17}\text{H}_{35}\text{COOH}$), and monounsaturated oleic acid (*cis*-9-octadecenoic acid, $\text{C}_{17}\text{H}_{33}\text{COOH}$).

### Amphiphilic Architecture & Micelle Self-Assembly
A soap molecule possesses a split chemical personality (**amphiphilic** or **amphipathic**):
1. **Hydrophobic Tail**: A long, non-polar hydrocarbon chain ($-\text{C}_{15}\text{H}_{31}$) that cannot engage in hydrogen bonding with water.
2. **Hydrophilic Head**: An ionic, highly solvated carboxylate group ($-\text{COO}^-\text{Na}^+$) that forms strong ion-dipole interactions with aqueous solvent.

```
       Spherical Micelle Cross-Section:
                 Aqueous Polar Solution
                  \   \   |   /   /
                 ( -COO- Na+ ) Heads
                /   |   |   |   |   \
               /  ~~~~~~~~~~~~~~~~~  \
              |   Non-Polar Hydrocarbon |
              |      Hydrophobic Core   |
              |   (Solubilizes Grease)  |
               \  ~~~~~~~~~~~~~~~~~  /
                \   |   |   |   |   /
                 ( -COO- Na+ ) Heads
```

When dissolved in water above a characteristic concentration known as the **critical micelle concentration (CMC)**:
- Individual soap monomers aggregate into spherical colloidal assemblies called **micelles** containing 50 to 100 amphiphilic molecules.
- The hydrophobic hydrocarbon tails cluster together in the interior of the micelle, shielded completely from contact with water.
- The charged carboxylate heads form an outer shell projecting into the aqueous phase, stabilized by an electrical double layer (Stern layer) of hydrated sodium counterions.
- Non-polar dirt, oils, and grease are sequestered inside the hydrophobic interior core of the micelle, allowing them to be washed away as a stable colloidal emulsion.""",
                "simulations": []
            },
            {
                "id": "sec4_7",
                "secNumber": "§4.7",
                "title": "Synthetic Detergents: CMC Thermodynamics, Hard Water & Sequestration",
                "heading": "Synthetic Detergents: CMC Thermodynamics, Hard Water & Sequestration",
                "content": r"""While traditional soaps are effective cleansers in soft water, they suffer from a severe chemical limitation in **hard water** containing divalent cations ($\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Fe}^{3+}$):

$$2\,\text{RCOO}^-\text{Na}^+ (\text{aq}) + \text{Ca}^{2+} (\text{aq}) \longrightarrow (\text{RCOO})_2\text{Ca}\downarrow (\text{s}) + 2\,\text{Na}^+ (\text{aq}) \tag{4.13}$$

Insoluble calcium and magnesium carboxylate precipitates ("soap scum" or curd) form instantly, inactivating the soap and staining fabrics.

### Structural Classes of Synthetic Detergents (Syndets)
To eliminate curdling, synthetic detergents utilize head groups whose alkaline-earth metal salts are completely water-soluble:

```
        Synthetic Surfactant Classifications:
        1. Anionic:   CH3(CH2)11-C6H4-SO3(-) Na(+)   (Linear Alkylbenzene Sulfonate, LAS)
        2. Cationic:  [CH3(CH2)15-N(CH3)3](+) Cl(-)   (Cetyltrimethylammonium Chloride)
        3. Non-Ionic: CH3(CH2)11-(OCH2CH2)n-OH       (Polyethylene Glycol Ether)
```

1. **Anionic Detergents**: Sodium linear alkylbenzene sulfonates ($\text{LAS}$, e.g., sodium 4-dodecylbenzenesulfonate, $\text{C}_{12}\text{H}_{25}\text{C}_6\text{H}_4\text{SO}_3^-\text{Na}^+$). Calcium sulfonates are water-soluble ($K_{\text{sp}} \gg 10^{-3}$).
2. **Cationic Detergents**: Quaternary ammonium salts (e.g., cetyltrimethylammonium bromide, $[\text{C}_{16}\text{H}_{33}\text{N}(\text{CH}_3)_3]^+\text{Br}^-$). Possess strong antimicrobial properties and act as fabric softeners.
3. **Non-Ionic Detergents**: Polyoxyethylene esters and ethers (e.g., polyoxyethylene lauryl ether, $\text{C}_{12}\text{H}_{25}\text{O}(\text{CH}_2\text{CH}_2\text{O})_n\text{H}$). Because they carry zero net formal charge, they are completely insensitive to polyvalent cations and foam minimally.

### Thermodynamics of Micelle Formation
The Gibbs free energy of micellization is governed by the hydrophobic effect:

$$\Delta G^\circ_{\text{mic}} = \Delta H^\circ_{\text{mic}} - T\Delta S^\circ_{\text{mic}} = RT \ln(\text{CMC}) \tag{4.14}$$

At room temperature ($298\text{ K}$), micellization is overwhelmingly **driven by entropy**:
$$\Delta H^\circ_{\text{mic}} \approx 0 \text{ to } +5\text{ kJ}\cdot\text{mol}^{-1}, \quad \Delta S^\circ_{\text{mic}} \approx +50\text{ to }+80\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$$
When individual hydrophobic tails are dispersed in water, water molecules are forced to organize into highly ordered, hydrogen-bonded "iceberg" clathrate cages around the non-polar chains. Clustering the tails inside the micelle core collapses these clathrate cages, liberating hundreds of water molecules into the bulk solvent with a massive gain in translational and rotational entropy ($\Delta S^\circ > 0$).""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob4_1",
                "problemNumber": "4.1",
                "title": "Kinetic Derivation of the $B_{\text{AC}}2$ Ester Saponification Mechanism",
                "difficulty": "Mastery",
                "statement": r"""The base-promoted saponification of ethyl acetate in aqueous solution follows the $B_{\text{AC}}2$ mechanism:
$$\text{CH}_3\text{COOEt} + \text{OH}^- \xrightleftharpoons[k_{-1}]{k_1} [\text{CH}_3\text{C}(\text{O}^-)(\text{OH})(\text{OEt})] \xrightarrow{k_2} \text{CH}_3\text{COOH} + \text{EtO}^- \xrightarrow{k_3} \text{CH}_3\text{COO}^- + \text{EtOH}$$
(a) Applying the steady-state approximation to the tetrahedral intermediate $[\text{T}^-]$, derive the symbolic expression for the overall second-order rate constant $k_{\text{obs}}$.
(b) Given that the forward collapse step to products ($k_2$) is substantially faster than backward reversion to reactants ($k_{-1}$), simplify the rate expression and identify the rate-determining step.
(c) When ethyl acetate is hydrolyzed in $\text{H}_2^{18}\text{O}$, what fraction of the $^{18}\text{O}$ label appears in ethanol versus acetic acid?""",
                "hints": ["Apply $\frac{d[T^-]}{dt} = 0$.", "Review which oxygen atom is expelled in the tetrahedral collapse."],
                "solution": r"""### (a) Steady-State Derivation for Intermediate $[\text{T}^-]$
Let $\text{E} = \text{CH}_3\text{COOEt}$ and $[\text{T}^-] = [\text{CH}_3\text{C}(\text{O}^-)(\text{OH})(\text{OEt})]$.
The rates of formation and consumption of $[\text{T}^-]$ are:
$$\frac{d[\text{T}^-]}{dt} = k_1 [\text{E}][\text{OH}^-] - k_{-1}[\text{T}^-] - k_2[\text{T}^-] = 0$$
Solving for the steady-state concentration of $[\text{T}^-]$:
$$[\text{T}^-] = \frac{k_1 [\text{E}][\text{OH}^-]}{k_{-1} + k_2}$$
The rate of formation of products is:
$$\text{Rate} = k_2 [\text{T}^-] = \left(\frac{k_1 k_2}{k_{-1} + k_2}\right) [\text{E}][\text{OH}^-]$$
Therefore, the observed second-order rate constant is:
$$k_{\text{obs}} = \frac{k_1 k_2}{k_{-1} + k_2}$$

### (b) Rate-Determining Step Simplification
The leaving group ability of $\text{EtO}^-$ ($\text{p}K_a \approx 16$) is comparable to or slightly better than $\text{OH}^-$ ($\text{p}K_a \approx 15.7$). More importantly, the irreversible exothermic proton transfer ($k_3 [\text{CH}_3\text{COOH}][\text{EtO}^-]$, $\Delta G^\circ \approx -65\text{ kJ}\cdot\text{mol}^{-1}$) rapidly traps the product:
$$k_2 \gg k_{-1} \implies \frac{k_2}{k_{-1} + k_2} \approx 1$$
Substituting this into $k_{\text{obs}}$:
$$k_{\text{obs}} \approx k_1$$
$$\text{Rate} = k_1 [\text{CH}_3\text{COOEt}][\text{OH}^-]$$
The rate-determining step is the **initial nucleophilic attack of hydroxide on the carbonyl carbon** ($k_1$).

### (c) Isotopic $^{18}\text{O}$ Distribution
In $\text{H}_2^{18}\text{O}$ with $^{18}\text{OH}^-$, the labeled oxygen attacks the carbonyl carbon to form:
$$[\text{CH}_3-\text{C}(\text{O}^-)(^{18}\text{OH})(\text{OEt})]$$
Collapse expels the ethoxide ion ($\text{EtO}^-$), leaving the $^{18}\text{O}$ atom covalently bound to the carbonyl carbon:
$$\text{CH}_3-\text{C}(=\text{O})-^{18}\text{OH} \longrightarrow \text{CH}_3-\text{C}(=\text{O})-^{18}\text{O}^-$$
- Acetic acid / acetate contains **100% of the $^{18}\text{O}$ label**.
- Ethanol contains **0% of the $^{18}\text{O}$ label**, definitively proving acyl-oxygen cleavage ($B_{\text{AC}}2$) rather than alkyl-oxygen cleavage ($S_N2$)."""
            },
            {
                "id": "prob4_2",
                "problemNumber": "4.2",
                "title": "Rotational Barrier & NMR Coalescence Kinetics of $N,N$-Dimethylformamide",
                "difficulty": "Advanced",
                "statement": r"""In the $^1\text{H}$ NMR spectrum of $N,N$-dimethylformamide ($\text{DMF}$) recorded on a $400\text{ MHz}$ spectrometer at $25^\circ\text{C}$, the two methyl groups appear as two sharp singlets separated by $\Delta \nu = 60\text{ Hz}$. As the sample is heated, the signals broaden and coalesce at a coalescence temperature of $T_c = 118^\circ\text{C}$ ($391.15\text{ K}$).
(a) Calculate the rate constant of internal rotation $k_c$ at the coalescence temperature.
(b) Using the Eyring-Polanyi equation, compute the Gibbs free energy of activation $\Delta G^\ddagger$ for $\text{C}-\text{N}$ bond rotation at $T_c$.
(c) Explain what factors lower the rotational barrier when the carbonyl oxygen is replaced by sulfur ($N,N$-dimethylthioformamide).""",
                "hints": ["Use Gutowsky-Holm formula: $k_c = \frac{\pi \Delta \nu}{\sqrt{2}}$.", "Eyring equation: $k = \frac{k_B T}{h} \exp(-\Delta G^\ddagger / RT)$."],
                "solution": r"""### (a) Rate Constant at Coalescence ($k_c$)
According to the Gutowsky-Holm formula for two uncoupled exchanging singlets of equal intensity:
$$k_c = \frac{\pi \Delta \nu}{\sqrt{2}} = \frac{3.14159 \times 60\text{ s}^{-1}}{1.4142} \approx 133.3\text{ s}^{-1}$$

### (b) Gibbs Free Energy of Activation ($\Delta G^\ddagger$)
The Eyring-Polanyi transition-state equation is:
$$k_c = \kappa \frac{k_B T_c}{h} \exp\left(-\frac{\Delta G^\ddagger}{R T_c}\right)$$
Assuming transmission coefficient $\kappa = 1.0$:
$$\Delta G^\ddagger = R T_c \ln\left(\frac{k_B T_c}{h \, k_c}\right)$$
Constants:
$$R = 8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$$
$$T_c = 391.15\text{ K}$$
$$k_B = 1.3806 \times 10^{-23}\text{ J}\cdot\text{K}^{-1}$$
$$h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$$
$$\frac{k_B T_c}{h} = \frac{1.3806 \times 10^{-23} \times 391.15}{6.626 \times 10^{-34}} = 8.150 \times 10^{12}\text{ s}^{-1}$$
$$\frac{k_B T_c}{h \, k_c} = \frac{8.150 \times 10^{12}}{133.3} = 6.114 \times 10^{10}$$
$$\ln(6.114 \times 10^{10}) = 24.836$$
$$\Delta G^\ddagger = (8.314) \times (391.15) \times (24.836) = 80,768\text{ J}\cdot\text{mol}^{-1} \approx 80.8\text{ kJ}\cdot\text{mol}^{-1} \quad (19.3\text{ kcal}\cdot\text{mol}^{-1})$$

### (c) Comparison with $N,N$-Dimethylthioformamide
In thioformamide ($\text{HCSNMe}_2$), sulfur is larger ($3p$) and less electronegative than oxygen ($2p$). The polar zwitterionic resonance contributor $[\text{H}-\text{C}(\text{S}^-)=\text{N}^+\text{Me}_2]$ is actually **more stable** because sulfur stabilizes a negative charge more effectively via polarizability and lower charge density.
Consequently, the $\text{C}-\text{N}$ double-bond character is higher, raising the rotational barrier:
$$\Delta G^\ddagger(\text{thioamide}) \approx 92\text{–}100\text{ kJ}\cdot\text{mol}^{-1} > \Delta G^\ddagger(\text{amide}) \approx 80.8\text{ kJ}\cdot\text{mol}^{-1}$$
Coalescence occurs at an even higher temperature."""
            },
            {
                "id": "prob4_3",
                "problemNumber": "4.3",
                "title": "Thermodynamics of Surfactant Micellization and CMC Determination",
                "difficulty": "Intermediate",
                "statement": r"""The critical micelle concentration of sodium dodecyl sulfate (SDS, $\text{C}_{12}\text{H}_{25}\text{SO}_4^-\text{Na}^+$) in water at $298\text{ K}$ is $\text{CMC} = 8.2 \times 10^{-3}\text{ mol}\cdot\text{L}^{-1}$. Calorimetric measurements reveal a standard enthalpy of micelle formation of $\Delta H^\circ_{\text{mic}} = +1.8\text{ kJ}\cdot\text{mol}^{-1}$.
(a) Calculate the standard Gibbs free energy of micellization $\Delta G^\circ_{\text{mic}}$ using the charged pseudophase separation model: $\Delta G^\circ_{\text{mic}} \approx 2 RT \ln(\text{CMC})$ (accounting for counterion binding fraction $\beta \approx 0.5$).
(b) Calculate the standard entropy of micellization $\Delta S^\circ_{\text{mic}}$.
(c) Explain why $\Delta S^\circ_{\text{mic}}$ is large and positive, and predict what happens to the CMC upon adding $0.1\text{ M NaCl}$.""",
                "hints": ["Express CMC as mole fraction or molar concentration as defined in the model.", "Recall the hydrophobic effect and clathrate cage disruption."],
                "solution": r"""### (a) Gibbs Free Energy of Micellization
Using the charged surfactant model with molar concentration:
$$\Delta G^\circ_{\text{mic}} \approx 2 RT \ln(\text{CMC})$$
At $T = 298.15\text{ K}$:
$$RT = 8.314 \times 298.15 = 2.4788\text{ kJ}\cdot\text{mol}^{-1}$$
$$\ln(8.2 \times 10^{-3}) = -4.8036$$
$$\Delta G^\circ_{\text{mic}} = 2 \times 2.4788 \times (-4.8036) = -23.81\text{ kJ}\cdot\text{mol}^{-1}$$
The negative value verifies that micelle self-assembly is thermodynamically spontaneous.

### (b) Entropy of Micellization ($\Delta S^\circ_{\text{mic}}$)
$$\Delta G^\circ_{\text{mic}} = \Delta H^\circ_{\text{mic}} - T \Delta S^\circ_{\text{mic}}$$
$$\Delta S^\circ_{\text{mic}} = \frac{\Delta H^\circ_{\text{mic}} - \Delta G^\circ_{\text{mic}}}{T} = \frac{+1800 - (-23810)}{298.15} = \frac{25610\text{ J}\cdot\text{mol}^{-1}}{298.15\text{ K}} = +85.9\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$$

### (c) Physical Interpretation and Salt Effect
1. **Entropic Driving Force**: The large positive entropy change ($\Delta S^\circ = +85.9\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$) demonstrates that micelle formation is **entropy-driven** (the hydrophobic effect). When dispersed monomeric hydrocarbon chains aggregate into the micelle core, structured water clathrate cages collapse, releasing ordered water molecules into the bulk solvent with a massive net gain in entropy.
2. **Effect of Added $\text{NaCl}$**:
   Adding $0.1\text{ M NaCl}$ increases the concentration of $\text{Na}^+$ counterions in solution. These counterions screen the electrostatic repulsion between the negatively charged sulfate head groups ($-\text{SO}_4^-$) on the micelle surface, dramatically stabilizing the micelle and lowering the free energy barrier. Consequently, the **$\text{CMC}$ decreases significantly** (from $8.2\text{ mM}$ to $\sim 1.5\text{ mM}$)."""
            },
            {
                "id": "prob4_4",
                "problemNumber": "4.4",
                "title": "Chemoselective Peptide Coupling: DCC and HOBt Mechanism",
                "difficulty": "Mastery",
                "statement": r"""In peptide synthesis, coupling of $N$-protected alanine ($\text{Boc-Ala-OH}$) with glycine methyl ester ($\text{H-Gly-OMe}$) using dicyclohexylcarbodiimide (DCC) alone often suffers from racemization and formation of an unreactive $N$-acylurea side-product. Adding 1-hydroxybenzotriazole (HOBt) suppresses both side-reactions and produces the dipeptide Boc-Ala-Gly-OMe in $>95\%$ yield.
(a) Draw the mechanism of DCC activation forming the $O$-acylisourea intermediate.
(b) Mechanistically illustrate how the $O$-acylisourea rearranges via an intramolecular $O \to N$ acyl transfer to form the unreactive $N$-acylurea by-product.
(c) Explain how HOBt traps the $O$-acylisourea as an active ester, suppressing $N$-acylurea formation and preventing racemization via oxazolone formation.""",
                "hints": ["$O$-acylisourea is a potent electrophile, but intramolecular transfer competes with intermolecular amine attack.", "HOBt forms an OBt active ester."],
                "solution": r"""### (a) DCC Activation & $O$-Acylisourea Formation
1. Proton transfer: The carboxylic acid of $\text{Boc-Ala-OH}$ protonates one of the basic diimide nitrogens of $\text{DCC}$ ($\text{Cy-N}=\text{C}=\text{N-Cy}$):
   $$\text{RCOOH} + \text{Cy-N}=\text{C}=\text{N-Cy} \rightleftharpoons \text{RCOO}^- + [\text{Cy-NH}^+=\text{C}=\text{N-Cy}]$$
2. Nucleophilic attack: The carboxylate oxygen attacks the central carbodiimide carbon:
   $$\text{RCOO}^- + [\text{Cy-NH}^+=\text{C}=\text{N-Cy}] \longrightarrow \text{R-C}(=\text{O})-\text{O}-\text{C}(=\text{N-Cy})-\text{NH-Cy}$$
This species is the **$O$-acylisourea** intermediate. Because the dicyclohexylurea moiety is an outstanding leaving group, the carbonyl carbon is strongly activated toward nucleophilic attack.

### (b) Intramolecular $O \to N$ Acyl Shift ($N$-Acylurea Side-Reaction)
If the amine nucleophile ($\text{H-Gly-OMe}$) is slow to attack due to steric crowding or dilute conditions, the $O$-acylisourea undergoes an intramolecular rearrangement via a cyclic four-membered transition state:
$$\text{R-C}(=\text{O})-\text{O}-\text{C}(=\text{N-Cy})-\text{NH-Cy} \xrightarrow{\text{intramolecular}} \text{Cy}-\text{N}(\text{COR})-\text{C}(=\text{O})-\text{NH-Cy} \quad (\text{N-acylurea})$$
The resulting $N$-acylurea is chemically inert, irreversibly consuming the starting amino acid and decreasing yield.

### (c) The Role of HOBt (1-Hydroxybenzotriazole)
1. **Active Ester Formation**: $\text{HOBt}$ is a potent, non-basic oxygen nucleophile ($\text{p}K_a \approx 4.6$). It attacks the $O$-acylisourea much faster than the amine can:
   $$\text{O-acylisourea} + \text{HOBt} \xrightarrow{\text{very fast}} \text{R-CO-OBt (active ester)} + \text{DCU}\downarrow$$
   Insoluble dicyclohexylurea ($\text{DCU}$) precipitates out, driving the reaction forward and preventing $N$-acylurea rearrangement.
2. **Suppression of Racemization**: The activated $O$-acylisourea can undergo base-promoted intramolecular cyclization to an oxazolone (azlactone), which rapidly racemizes via aromatic-like enolization. The $\text{OBt}$ ester undergoes rapid, clean aminolysis with $\text{H-Gly-OMe}$ without forming an oxazolone, preserving **$>99.9\%$ optical purity**."""
            },
            {
                "id": "prob4_5",
                "problemNumber": "4.5",
                "title": "Mechanistic Distinction: $A_{\text{AC}}2$ vs $A_{\text{AL}}1$ in Tert-Butyl Ester Cleavage",
                "difficulty": "Intermediate",
                "statement": r"""Methyl benzoate and *tert*-butyl benzoate were each dissolved in concentrated sulfuric acid containing $^{18}\text{O}$-enriched water ($\text{H}_2^{18}\text{O}$) and heated to $60^\circ\text{C}$.
(a) Write the chemical structures of all products formed from each reaction.
(b) Predict which compound incorporates $^{18}\text{O}$ into the benzoic acid product and which incorporates $^{18}\text{O}$ into the alcohol product.
(c) Justify your predictions using the $A_{\text{AC}}2$ vs $A_{\text{AL}}1$ mechanistic classifications.""",
                "hints": ["Which ester cleaves the acyl-oxygen bond?", "Which ester cleaves the alkyl-oxygen bond via a stable tertiary carbocation?"],
                "solution": r"""### (a) Product Identification
1. **Methyl Benzoate**:
   $$\text{PhCOOMe} + \text{H}_2^{18}\text{O} \xrightarrow{\text{H}_2\text{SO}_4} \text{PhCO}^{18}\text{OH} + \text{MeOH}$$
   Products: **Benzoic acid-$^{18}\text{O}$** and unlabeled **methanol**.
2. ***tert*-Butyl Benzoate**:
   $$\text{PhCOOCMe}_3 + \text{H}_2^{18}\text{O} \xrightarrow{\text{H}_2\text{SO}_4} \text{PhCOOH} + \text{Me}_3\text{C}-^{18}\text{OH} \quad (\text{or isobutylene} + \text{H}_2^{18}\text{O})$$
   Products: Unlabeled **benzoic acid** and **$^{18}\text{O}$-labeled *tert*-butanol**.

### (b) Isotopic $^{18}\text{O}$ Fate
- For **methyl benzoate**, $^{18}\text{O}$ resides exclusively in the **benzoic acid**.
- For ***tert*-butyl benzoate**, $^{18}\text{O}$ resides exclusively in the ***tert*-butanol**.

### (c) Mechanistic Rationale
1. **Methyl Benzoate ($A_{\text{AC}}2$)**:
   Primary methyl carbocations are energetically inaccessible. Hydrolysis proceeds via acid-catalyzed **acyl-oxygen cleavage**:
   $$\text{Ph-C}(=^{18}\text{O}^+\text{H})-\text{OMe} + \text{H}_2^{18}\text{O} \rightleftharpoons \text{Ph-C}(^{18}\text{OH})_2(\text{OMe}) \longrightarrow \text{Ph-C}(=\text{O})-^{18}\text{OH} + \text{MeOH}$$
   Water attacks the acyl carbon, leaving the label in the carboxylic acid.
2. ***tert*-Butyl Benzoate ($A_{\text{AL}}1$)**:
   The *tert*-butyl group can form a highly stable tertiary carbocation ($[\text{CMe}_3]^+$). Protonation occurs on the ether oxygen, followed by unimolecular rate-determining **alkyl-oxygen heterolysis**:
   $$\text{Ph-CO}-\text{O}^+(\text{H})-\text{CMe}_3 \xrightarrow{\text{slow}} \text{Ph-COOH} + [\text{CMe}_3]^+$$
   Benzoic acid departs with its original oxygen atoms. The carbocation $[\text{CMe}_3]^+$ is trapped by solvent $\text{H}_2^{18}\text{O}$, placing the isotopic label into *tert*-butanol."""
            },
            {
                "id": "prob4_6",
                "problemNumber": "4.6",
                "title": "Industrial Saponification Value and Molecular Weight Determination",
                "difficulty": "Intermediate",
                "statement": r"""A pure sample of a homogeneous triacylglycerol ($2.500\text{ g}$) was saponified with $50.00\text{ mL}$ of $0.5000\text{ M}$ ethanolic $\text{KOH}$ under reflux for 2 hours. The excess unreacted $\text{KOH}$ required $21.50\text{ mL}$ of $0.5000\text{ M HCl}$ for neutral titration.
(a) Define Saponification Value (SV) and calculate its value for this fat sample (expressed in $\text{mg KOH / g fat}$).
(b) Calculate the molar mass of the triacylglycerol.
(c) Deduce the molecular identity and fatty acid composition of the triacylglycerol.""",
                "hints": ["Saponification value is the mg of KOH required to saponify 1 g of fat.", "Each mole of triacylglycerol consumes exactly 3 moles of KOH."],
                "solution": r"""### (a) Calculation of Saponification Value (SV)
1. **Total moles of $\text{KOH}$ added**:
   $$n_{\text{KOH, initial}} = 0.05000\text{ L} \times 0.5000\text{ mol/L} = 0.02500\text{ mol} = 25.00\text{ mmol}$$
2. **Moles of unreacted excess $\text{KOH}$**:
   $$n_{\text{HCl}} = 0.02150\text{ L} \times 0.5000\text{ mol/L} = 0.01075\text{ mol} = 10.75\text{ mmol}$$
3. **Moles of $\text{KOH}$ consumed by saponification**:
   $$n_{\text{KOH, consumed}} = 25.00 - 10.75 = 14.25\text{ mmol} = 0.01425\text{ mol}$$
4. **Mass of $\text{KOH}$ consumed** ($M_{\text{KOH}} = 56.106\text{ g/mol}$):
   $$m_{\text{KOH}} = 0.01425\text{ mol} \times 56,106\text{ mg/mol} = 799.5\text{ mg}$$
5. **Saponification Value (SV)**:
   $$\text{SV} = \frac{799.5\text{ mg KOH}}{2.500\text{ g fat}} = 319.8\text{ mg KOH / g fat}$$

### (b) Molar Mass of the Triacylglycerol
Because 1 mole of triacylglycerol reacts with 3 moles of $\text{KOH}$:
$$n_{\text{fat}} = \frac{n_{\text{KOH, consumed}}}{3} = \frac{0.01425\text{ mol}}{3} = 0.00475\text{ mol}$$
The molar mass $M_{\text{fat}}$ is:
$$M_{\text{fat}} = \frac{2.500\text{ g}}{0.00475\text{ mol}} \approx 526.3\text{ g/mol}$$

### (c) Deduction of Triacylglycerol Identity
The formula of a simple triacylglycerol is $\text{C}_3\text{H}_5(\text{OOCR})_3$:
$$M_{\text{glycerol backbone}}(\text{C}_3\text{H}_5) = 41.07\text{ g/mol}$$
$$M_{\text{three carboxylate groups}}(3 \times \text{COO}) = 3 \times 44.01 = 132.03\text{ g/mol}$$
Mass of the three alkyl chains:
$$3 M_R = 526.3 - (41.07 + 132.03) = 526.3 - 173.1 = 353.2\text{ g/mol}$$
$$M_R = \frac{353.2}{3} \approx 117.7\text{ g/mol}$$
For a saturated alkyl group $\text{C}_n\text{H}_{2n+1}$:
$$14.027 n + 1.008 = 117.7 \implies 14.027 n = 116.7 \implies n \approx 8.3$$
This corresponds to a mixture of caprylic ($\text{C}_8$) and capric ($\text{C}_{10}$) triglycerides, characteristic of coconut oil fractionated medium-chain triglycerides (MCT)."""
            },
            {
                "id": "prob4_7",
                "problemNumber": "4.7",
                "title": "Stereoselective Synthesis of Tertiary Amides via the Ritter Reaction",
                "difficulty": "Mastery",
                "statement": r"""Devise a chemical synthesis of $N$-(tert-butyl)acetamide starting from isobutylene and acetonitrile.
(a) Provide the complete curved-arrow reaction mechanism showing all intermediate species.
(b) Identify the nitrilium ion intermediate and explain why the nitrogen atom acts as the nucleophile while the carbon atom later acts as the electrophile.
(c) Predict the product if (1R,2S,4R)-borneol is subjected to Ritter reaction conditions with acetonitrile and concentrated $\text{H}_2\text{SO}_4$, taking Wagner-Meerwein carbocation rearrangements into account.""",
                "hints": ["Generate the tertiary carbocation with sulfuric acid.", "Nitrogen lone pair attacks carbocation, followed by hydration."],
                "solution": r"""### (a) Mechanism of the Ritter Reaction
$$\begin{aligned}
\text{Step 1 (Carbocation Generation)}: &\quad \text{CH}_2=\text{C(CH}_3)_2 + \text{H}_2\text{SO}_4 \rightleftharpoons [(\text{CH}_3)_3\text{C}]^+ + \text{HSO}_4^- \\
\text{Step 2 (Nitrilium Ion Formation)}: &\quad [(\text{CH}_3)_3\text{C}]^+ + :\text{N}\equiv\text{C-CH}_3 \rightleftharpoons [(\text{CH}_3)_3\text{C}-\text{N}^+\equiv\text{C-CH}_3] \\
\text{Step 3 (Nucleophilic Water Addition)}: &\quad [(\text{CH}_3)_3\text{C}-\text{N}^+\equiv\text{C-CH}_3] + \text{H}_2\text{O} \rightleftharpoons [(\text{CH}_3)_3\text{C}-\text{N}=\text{C}(\text{O}^+\text{H}_2)\text{CH}_3] \\
\text{Step 4 (Deprotonation to Imidic Acid)}: &\quad [(\text{CH}_3)_3\text{C}-\text{N}=\text{C}(\text{O}^+\text{H}_2)\text{CH}_3] \xrightarrow{-\text{H}^+} (\text{CH}_3)_3\text{C}-\text{N}=\text{C(OH)CH}_3 \\
\text{Step 5 (Tautomerization to Amide)}: &\quad (\text{CH}_3)_3\text{C}-\text{N}=\text{C(OH)CH}_3 \xrightleftharpoons{} (\text{CH}_3)_3\text{C}-\text{NH}-\text{CO}-\text{CH}_3
\end{aligned}$$
The product is **$N$-(tert-butyl)acetamide**.

### (b) Nitrilium Ion Dual Electronic Character
In **Step 2**, the unshared lone pair of $sp$-hybridized nitrogen attacks the empty $p$-orbital of the *tert*-butyl carbocation, forming the linear **nitrilium cation**:
$$[(\text{CH}_3)_3\text{C}-\text{N}^+\equiv\text{C}-\text{CH}_3 \longleftrightarrow (\text{CH}_3)_3\text{C}-\text{N}=\text{C}^+-\text{CH}_3]$$
The formal positive charge is delocalized onto the central $sp$-hybridized carbon atom, rendering it violently electrophilic. In **Step 3**, water acts as a nucleophile, attacking this carbon to complete the hydration.

### (c) Ritter Reaction on Borneol: Wagner-Meerwein Rearrangement
When borneol is treated with concentrated sulfuric acid:
1. Protonation and loss of water from the C2 position generates the secondary bornyl carbocation.
2. The strained bicyclic bornyl cation undergoes a spontaneous **Wagner-Meerwein [1,2]-carbon shift**, relieving bridgehead ring strain and forming the tertiary **isobornyl carbocation**.
3. Trapping by acetonitrile occurs stereoselectively from the less hindered *exo* face:
   $$\text{Isobornyl Cation} + \text{CH}_3\text{CN} + \text{H}_2\text{O} \longrightarrow \text{N-(exo-isobornyl)acetamide}$$
The exclusive product is the rearranged *exo*-isobornyl derivative."""
            }
        ]
    }

def get_unit_5():
    return {
        "id": "unit5",
        "unitId": "unit5-org2",
        "number": 5,
        "unitNumber": 5,
        "title": "Unit 5: Amines, Arenediazonium Salts & Nitro Compounds: Pyramidal Inversion, Diazotization & Azo Color Chemistry",
        "description": "Comprehensive physical organic treatise on nitrogen systems: amine pyramidal inversion dynamics and quantum tunneling barriers, gas-phase vs aqueous solvation basicity scales, synthetic methodologies (Gabriel phthalimide, Curtius rearrangement, Hofmann degradation), Hofmann exhaustive methylation and anti-Zaitsev E2 elimination, Hinsberg testing; nitrous acid diazotization kinetics, Sandmeyer, Schiemann, and Gattermann substitution manifolds, azo coupling thermodynamics and chromophore electronics; and nitroalkane aci-tautomerism, Nef reactions, and selective nitroarene reductions.",
        "leadSummary": "Advanced physical organic analysis of nitrogen stereodynamics, solvation-controlled basicity, Curtius/Hofmann rearrangements, arenediazonium radical and ionic substitution cascades, azo dye color chemistry, and nitro compound reduction manifolds.",
        "simulations": ["sim_chem_amine_inversion_hofmann_elimination", "sim_chem_diazonium_coupling_color_engine"],
        "sections": [
            {
                "id": "sec5_1",
                "secNumber": "§5.1",
                "title": "Nitrogen Stereodynamics: Pyramidal Inversion & Quantum Tunneling",
                "heading": "Nitrogen Stereodynamics: Pyramidal Inversion & Quantum Tunneling",
                "content": r"""Amines ($\text{R}_3\text{N}$) possess a trivalent nitrogen atom with tetrahedral geometry ($sp^3$ hybridization) containing three bonded substituents and one unshared lone pair. If the three substituents are distinct ($\text{R}_1 \neq \text{R}_2 \neq \text{R}_3$), the nitrogen atom is a stereogenic center with formal chirality.

However, simple tertiary amines cannot be resolved into stable enantiomers at room temperature due to rapid **nitrogen pyramidal inversion** (the "umbrella inversion"):

```
            Amine Pyramidal Inversion Double-Well:
              R1                 R1                 R1
               |   sp3            |  Planar sp2      |   sp3
               N:     <=====>     N:      <=====>   :N
             /   \              /   \              /   \
           R2     R3          R2     R3          R3     R2
          (R)-Enantiomer       Transition State     (S)-Enantiomer
```

### Double-Well Potential & Inversion Kinetics
The inversion coordinate corresponds to a double-well potential separated by a planar $sp^2$-hybridized transition state where the nitrogen lone pair occupies a pure unhybridized $2p_z$ atomic orbital:

$$\Delta G^\ddagger_{\text{inversion}} \approx 25\text{ kJ}\cdot\text{mol}^{-1} \quad (6.0\text{ kcal}\cdot\text{mol}^{-1}) \tag{5.1}$$

The inversion rate constant given by the Eyring equation at $298\text{ K}$ is:

$$k_{\text{inv}} \approx 2.5 \times 10^{10}\text{ s}^{-1} \quad (25\text{ GHz}) \tag{5.2}$$

Because inversion occurs billions of times per second, the enantiomers racemize instantaneously. Furthermore, in ammonia ($\text{NH}_3$), the light hydrogen atoms undergo **quantum mechanical tunneling** through the barrier, giving rise to the famous $23.8\text{ GHz}$ microwave inversion absorption used in atomic ammonia masers.

### Chiral Nitrogen Systems: Suppressing Inversion
Enantiomerically stable chiral nitrogen centers can only be isolated when pyramidal inversion is structurally suppressed:
1. **Quaternary Ammonium Salts**: Quaternization ($[\text{R}_1\text{R}_2\text{R}_3\text{R}_4\text{N}]^+\text{X}^-$) removes the unshared lone pair. Inversion is fundamentally impossible without breaking covalent bonds. Salts such as ethylmethylpropylphenylammonium iodide were resolved into pure enantiomers by William Jackson Pope in 1899.
2. **Bridgehead Nitrogen in Bicyclic Cages**: In rigid bicyclic cages such as **Tröger's base** or quinuclidine, the nitrogen atom is locked into a rigid bridgehead. Pyramidal inversion would require passing through an impossible planar transition state with extreme angle strain ($\Delta G^\ddagger > 170\text{ kJ}\cdot\text{mol}^{-1}$), allowing Tröger's base to be resolved into stable enantiomers.
3. **Three-Membered Aziridine Rings**: In aziridines with electronegative substituents (e.g., $N$-chloroaziridines), the strained $60^\circ$ ring angle severely destabilizes the $120^\circ$ planar transition state, elevating the inversion barrier to $\Delta G^\ddagger \approx 85\text{–}115\text{ kJ}\cdot\text{mol}^{-1}$ and permitting resolution at room temperature.""",
                "simulations": ["sim_chem_amine_inversion_hofmann_elimination"]
            },
            {
                "id": "sec5_2",
                "secNumber": "§5.2",
                "title": "Basicity Scales: The Gas-Phase vs Aqueous Solution Paradox",
                "heading": "Basicity Scales: The Gas-Phase vs Aqueous Solution Paradox",
                "content": r"""The basicity of amines ($\text{R}_3\text{N} + \text{H}_2\text{O} \rightleftharpoons \text{R}_3\text{NH}^+ + \text{OH}^-$) reveals one of the most profound illustrations of solvation thermodynamics in physical organic chemistry.

### The Gas-Phase Basicity Order
In the gas phase (measured by high-pressure mass spectrometry and ion cyclotron resonance), where solvent molecules are absent:

$$\text{Gas-Phase Basicity}: \quad \text{NH}_3 < \text{MeNH}_2 < \text{Me}_2\text{NH} < \text{Me}_3\text{N} \tag{5.3}$$

This order reflects pure intrinsic electronic effects: each additional alkyl methyl group is polarizable and donates electron density through $+I$ inductive effects and hyperconjugation, stabilizing the forming positive charge on the ammonium cation $[\text{R}_n\text{NH}_{4-n}]^+$.

### The Aqueous Solution Paradox
In aqueous solution, however, the experimentally measured $\text{p}K_b$ values (or $\text{p}K_a$ of conjugate acids) display an anomalous non-monotonic order:

$$\text{Aqueous Basicity}: \quad \text{NH}_3 < \text{Me}_3\text{N} < \text{MeNH}_2 < \text{Me}_2\text{NH} \tag{5.4}$$

$$\begin{aligned}
\text{NH}_3: &\quad \text{p}K_a(\text{NH}_4^+) = 9.24 \\
\text{Me}_3\text{N} (3^\circ): &\quad \text{p}K_a(\text{Me}_3\text{NH}^+) = 9.80 \\
\text{MeNH}_2 (1^\circ): &\quad \text{p}K_a(\text{MeNH}_3^+) = 10.64 \\
\text{Me}_2\text{NH} (2^\circ): &\quad \text{p}K_a(\text{Me}_2\text{NH}_2^+) = 10.73
\end{aligned}$$

Why does trimethylamine ($3^\circ$) drop to being a weaker base than methylamine ($1^\circ$) in water?

```
Aqueous Hydration Enthalpies of Ammonium Cations:
1° Cation [RNH3+]:    Three H-bonds to H2O  ===> Delta H(hyd) = -393 kJ/mol
2° Cation [R2NH2+]:   Two H-bonds to H2O    ===> Delta H(hyd) = -351 kJ/mol
3° Cation [R3NH+]:    Only ONE H-bond to H2O ===> Delta H(hyd) = -305 kJ/mol
```

The explanation lies in the competition between **inductive stabilization** and **hydration enthalpy**:
- As alkyl groups replace hydrogens on nitrogen, the number of acidic protons available to form strong hydrogen bonds with surrounding water molecules decreases from three in $[\text{RNH}_3]^+$ to only **one** in $[\text{R}_3\text{NH}]^+$.
- Furthermore, three bulky methyl groups physically shield the positive nitrogen center, preventing close approach of solvating water dipoles (steric hindrance to solvation).
- Secondary amines ($\text{Me}_2\text{NH}$) hit the perfect thermodynamic compromise: they possess two inductive $+I$ alkyl groups while retaining two acidic protons for strong aqueous hydration stabilization.""",
                "simulations": []
            },
            {
                "id": "sec5_3",
                "secNumber": "§5.3",
                "title": "Synthetic Routes: Gabriel Phthalimide, Curtius & Hofmann Rearrangements",
                "heading": "Synthetic Routes: Gabriel Phthalimide, Curtius & Hofmann Rearrangements",
                "content": r"""Direct alkylation of ammonia with alkyl halides invariably leads to polyalkylation (mixtures of $1^\circ, 2^\circ, 3^\circ$ amines and $4^\circ$ quaternary salts). Clean synthesis of pure primary amines requires specialized synthetic methodologies:

### 1. The Gabriel Phthalimide Synthesis
Phthalimide ($\text{p}K_a \approx 8.3$) is deprotonated by $\text{KOH}$ to form potassium phthalimide:

$$\begin{aligned}
\text{Step 1}: &\quad \text{Phthalimide} + \text{KOH} \longrightarrow \text{Potassium phthalimide} + \text{H}_2\text{O} \\
\text{Step 2}: &\quad \text{Phthalimide}^-\text{K}^+ + \text{R-CH}_2\text{-X} \xrightarrow{\text{DMF, }S_N2} N\text{-alkylphthalimide} + \text{KX}\downarrow \\
\text{Step 3}: &\quad N\text{-alkylphthalimide} + \text{NH}_2\text{NH}_2 \xrightarrow{\Delta, \text{EtOH (Ing-Manske)}} \text{R-CH}_2\text{-NH}_2 + \text{Phthalhydrazide}\downarrow
\end{aligned} \tag{5.5}$$

Because the $N$-alkylphthalimide lacks unshared electron density on nitrogen capable of undergoing a second alkylation (resonance with two carbonyls delocalizes the lone pair), polyalkylation is strictly prevented. Cleavage with hydrazine (**Ing-Manske procedure**) isolates pure primary amine in minutes.

### 2. The Hofmann Rearrangement of Primary Amides
Treatment of primary amides with bromine in aqueous sodium hydroxide produces primary amines with the loss of one carbon atom:

$$\text{R-CONH}_2 + \text{Br}_2 + 4\,\text{NaOH} \longrightarrow \text{R-NH}_2 + \text{Na}_2\text{CO}_3 + 2\,\text{NaBr} + 2\,\text{H}_2\text{O} \tag{5.6}$$

- Deprotonation and bromination gives $N$-bromoamide: $\text{RCONHBr}$.
- Second deprotonation gives the bromoamide anion: $[\text{R-CO-N-Br}]^-$.
- Elimination of bromide induces **concerted [1,2]-migration of group R** with retention of stereochemistry to yield an **isocyanate**:
  $$[\text{R-CO-N-Br}]^- \xrightarrow{-\text{Br}^-} \text{R-N}=\text{C}=\text{O} \quad (\text{alkyl isocyanate}) \tag{5.7}$$
- Hydrolysis of the isocyanate yields an unstable carbamic acid ($\text{RNHCOOH}$), which spontaneously decarboxylates to give the primary amine $\text{RNH}_2$.

### 3. The Curtius Rearrangement of Acyl Azides
Acyl chlorides react with sodium azide ($\text{NaN}_3$) to form acyl azides, which undergo thermal rearrangement:

$$\text{RCOCl} + \text{NaN}_3 \longrightarrow \text{R-CO-N}_3 \xrightarrow{\Delta, -\text{N}_2\uparrow} \text{R-N}=\text{C}=\text{O} \xrightarrow{\text{H}_2\text{O}} \text{R-NH}_2 + \text{CO}_2\uparrow \tag{5.8}$$

Trapping the intermediate isocyanate with alcohols yields stable carbamates (urethanes), which form the basis of the Cbz and Boc amine protection methodologies.""",
                "simulations": []
            },
            {
                "id": "sec5_4",
                "secNumber": "§5.4",
                "title": "Hofmann Elimination vs Cope Elimination: Stereoelectronic Principles",
                "heading": "Hofmann Elimination vs Cope Elimination: Stereoelectronic Principles",
                "content": r"""The base-induced elimination of quaternary ammonium hydroxides and amine $N$-oxides demonstrates how stereoelectronic orbital alignment governs alkene regioselectivity.

### Hofmann Exhaustive Methylation & Elimination
When an amine is treated with excess methyl iodide, it is converted into a quaternary ammonium iodide, which is transformed into the hydroxide salt with silver(I) oxide:

$$\text{R-CH}_2\text{-CH}_2\text{-NH}_2 \xrightarrow{3\,\text{CH}_3\text{I}} \text{R-CH}_2\text{-CH}_2\text{-N}^+(\text{CH}_3)_3\,\text{I}^- \xrightarrow{\text{Ag}_2\text{O, H}_2\text{O}} \text{R-CH}_2\text{-CH}_2\text{-N}^+(\text{CH}_3)_3\,\text{OH}^- + \text{AgI}\downarrow \tag{5.9}$$

Upon thermal heating ($100^\circ\text{–}150^\circ\text{C}$), the quaternary hydroxide undergoes an E2 elimination with **Hofmann regioselectivity**:
$$\text{Product}: \quad \text{The least substituted, least stable alkene dominates} \quad (>90\%) \tag{5.10}$$

```
Hofmann E2 Anti-Periplanar Conformation:
       H         H
        \       /
         C --- C
        /       \
      CH3        N+(Me)3   <--- Bulky leaving group forces
                                anti-periplanar alignment with
                                least hindered beta-proton
```

Why does Hofmann elimination yield the least substituted alkene, reversing Zaitsev's rule?
1. **Steric Crowding**: The trimethylammonium group ($-\text{N}^+(\text{CH}_3)_3$) is exceptionally bulky. In the staggered Newman projection required for *anti*-periplanar E2 elimination ($\theta = 180^\circ$), placing the bulky leaving group adjacent to an alkyl substituent creates severe gauche steric repulsions. Deprotonation at the less hindered terminal methyl group avoids this clash.
2. **Carbanion Character in the Transition State**: The positively charged nitrogen exerts powerful $-I$ electron withdrawal. The developing transition state has substantial **carbanion character** at the $\beta$-carbon. Primary carbanions are far more stable than secondary or tertiary carbanions:
   $$\text{Carbanion Stability}: \quad \text{primary} > \text{secondary} > \text{tertiary}$$

### The Cope Elimination (Syn-Elimination)
Tertiary amine $N$-oxides, prepared by oxidizing tertiary amines with $\text{H}_2\text{O}_2$ or $m\text{CPBA}$, undergo thermal elimination at mild temperatures ($80^\circ\text{–}100^\circ\text{C}$):

$$\text{R-CH}_2\text{-CH}_2\text{-N}^+(\text{O}^-)(\text{Me})_2 \xrightarrow{80^\circ\text{-}100^\circ\text{C}} \text{R-CH}=\text{CH}_2 + \text{Me}_2\text{N-OH} \tag{5.11}$$

- Proceeding through a concerted **five-membered planar cyclic transition state**, the oxygen atom abstracts the $\beta$-proton from the **same face** (*syn*-coplanar elimination).
- Because no external base is required and conditions are neutral, the Cope elimination is uniquely suited for base-sensitive molecules.""",
                "simulations": []
            },
            {
                "id": "sec5_5",
                "secNumber": "§5.5",
                "title": "Arenediazonium Salts: Diazotization Kinetics & Substitution Manifolds",
                "heading": "Arenediazonium Salts: Diazotization Kinetics & Substitution Manifolds",
                "content": r"""Primary aromatic amines react with nitrous acid ($\text{HNO}_2$) in cold aqueous mineral acid ($0^\circ\text{–}5^\circ\text{C}$) to form **arenediazonium salts** ($[\text{Ar}-\text{N}\equiv\text{N}]^+\text{X}^-$).

### Diazotization Mechanism & Nitrous Acid Kinetics
Nitrous acid is generated *in situ* from sodium nitrite ($\text{NaNO}_2$) and excess hydrochloric acid:

$$\text{NaNO}_2 + \text{HCl} \rightleftharpoons \text{HNO}_2 + \text{NaCl} \tag{5.12}$$

1. In strong acid, nitrous acid is protonated and loses water to form the active electrophile, the **nitrosonium ion** ($\text{NO}^+$):
   $$\text{H}-\text{O}-\text{N}=\text{O} + \text{H}^+ \rightleftharpoons \text{H}_2\text{O}^+-\text{N}=\text{O} \rightleftharpoons \text{N}\equiv\text{O}^+ + \text{H}_2\text{O} \tag{5.13}$$
2. Nucleophilic attack by aniline: $\text{ArNH}_2 + \text{NO}^+ \rightleftharpoons [\text{ArNH}_2-\text{NO}]^+$.
3. Proton loss yields $N$-nitrosoaniline: $\text{ArNH-NO}$.
4. Tautomerization (proton transfer from N to O): $\text{Ar-N}=\text{N-OH}$ (diazoic acid).
5. Protonation of oxygen and loss of water:
   $$\text{Ar-N}=\text{N-O}^+\text{H}_2 \xrightarrow{-\text{H}_2\text{O}} [\text{Ar}-\text{N}\equiv\text{N}]^+ \quad (\text{arenediazonium cation}) \tag{5.14}$$

Aromatic diazonium salts are stabilized by resonance delocalization into the phenyl ring, allowing them to remain stable in cold aqueous solution at $0^\circ\text{–}5^\circ\text{C}$. (Aliphatic diazonium salts spontaneously decompose at $-78^\circ\text{C}$ to give unstable carbocations and nitrogen gas).

### Substitution Manifolds of Arenediazonium Salts
Arenediazonium salts act as versatile synthetic hubs for introducing substituents that cannot be installed via direct electrophilic aromatic substitution:

```
              Arenediazonium Substitution Hub:
                           Ar-Cl  (CuCl, Sandmeyer)
                         /
                       /   Ar-Br  (CuBr, Sandmeyer)
                     /
                   /       Ar-CN  (CuCN, Sandmeyer)
                 /
  [Ar-N2+] X-  ----------> Ar-I   (KI, room temp)
                 \
                   \       Ar-F   (HBF4, heat, Schiemann)
                     \
                       \   Ar-OH  (H2O, H2SO4, 100 C)
                         \
                           Ar-H   (H3PO2, hypophosphorous acid)
```

1. **Sandmeyer Reactions**: Catalyzed by copper(I) salts ($\text{CuCl}, \text{CuBr}, \text{CuCN}$). Proceeds via single-electron transfer (SET) generating an aryl radical ($\text{Ar}^\bullet$) and $\text{N}_2\uparrow$.
2. **Schiemann Fluorination**: Precipitation with fluoroboric acid yields insoluble $[\text{ArN}_2]^+\text{BF}_4^-$. Gentle thermal decomposition ($120^\circ\text{C}$) delivers pure fluoroarenes ($\text{Ar-F} + \text{N}_2\uparrow + \text{BF}_3\uparrow$).
3. **Iodination**: Simply treating the diazonium solution with potassium iodide ($\text{KI}$) without any catalyst yields aryl iodides ($\text{Ar-I}$) via an electron-transfer radical mechanism.
4. **Deamination**: Hypophosphorous acid ($\text{H}_3\text{PO}_2$) reduces the diazonium group to a hydrogen atom ($\text{Ar-H}$), allowing the amino group to serve as a temporary directing and activating group in synthesis.""",
                "simulations": []
            },
            {
                "id": "sec5_6",
                "secNumber": "§5.6",
                "title": "Azo Coupling Dynamics & Chromophore Electronics in Dye Chemistry",
                "heading": "Azo Coupling Dynamics & Chromophore Electronics in Dye Chemistry",
                "content": r"""Arenediazonium cations ($[\text{ArN}_2]^+$) are weak electrophiles that react with strongly activated aromatic substrates (phenols and tertiary aromatic amines) via electrophilic aromatic substitution to produce intensely colored **azo compounds** ($\text{Ar}-\text{N}=\text{N}-\text{Ar}'$).

### Mechanistic Dynamics & Optimal $\text{pH}$ Windows
The rate of azo coupling displays acute sensitivity to solution $\text{pH}$:

$$\text{Rate} = k_2 [\text{ArN}_2^+] [\text{Substrate}] \tag{5.15}$$

```
                Azo Coupling pH Optimization:
1. Coupling with Phenols (Optimal pH 9-10):
   Phenol (inactive)  <===>  Phenoxide Ar-O(-) (Violently Active Nucleophile)
   [At pH > 11, ArN2+ converts to unreactive diazotate Ar-N=N-O(-)]

2. Coupling with Aromatic Amines (Optimal pH 4-7):
   Anilinium Ar-NH3(+) (inactive) <===> Free Amine Ar-NR2 (Active Nucleophile)
   [At pH < 3, amine is fully protonated; at pH > 8, diazonium hydrolyzes]
```

- **Coupling with Phenols**: Optimum at **$\text{pH } 9\text{–}10$**. Deprotonation converts phenol into the strongly activated phenoxide anion ($\text{ArO}^-$), which attacks the terminal diazonium nitrogen. At $\text{pH} > 11$, the diazonium cation is converted into the unreactive diazotate ion ($\text{Ar-N}=\text{N-O}^-$).
- **Coupling with Amines**: Optimum at **$\text{pH } 4\text{–}7$**. The free amine ($\text{ArNR}_2$) is the active nucleophile. At $\text{pH} < 3$, the amine is completely protonated into an unreactive anilinium cation ($-\text{NHR}_2^+$).

### Chromophore Electronics & Industrial Dyes
The intense color of azo dyes arises from extended $\pi$-conjugation across the azo bridge ($-\text{N}=\text{N}-$):
- The chromophore features a donor-acceptor (push-pull) architecture: an electron-donating auxochrome ($-\text{NR}_2$ or $-\text{OH}$) on one ring and an electron-withdrawing group ($-\text{SO}_3^-$, $-\text{NO}_2$) on the other.
- Conjugation lowers the $\pi \to \pi^*$ HOMO-LUMO gap from the UV region into the visible spectrum ($400\text{–}700\text{ nm}$).

#### Methyl Orange ($\text{pH}$ Indicator)
Prepared by coupling diazotized sulfanilic acid with $N,N$-dimethylaniline:
- At $\text{pH} > 4.4$ (basic form): Exists as the yellow azo anion ($\lambda_{\max} \approx 460\text{ nm}$).
- At $\text{pH} < 3.1$ (acidic form): Protonation occurs at the azo nitrogen, forming a resonance-stabilized red quinonoid cation ($\lambda_{\max} \approx 510\text{ nm}$). The bathochromic red-shift ($50\text{ nm}$) causes the visible color change from yellow to red.""",
                "simulations": ["sim_chem_diazonium_coupling_color_engine"]
            },
            {
                "id": "sec5_7",
                "secNumber": "§5.7",
                "title": "Nitro Compounds: Aci-Tautomerism, Nef Reaction & Selective Reductions",
                "heading": "Nitro Compounds: Aci-Tautomerism, Nef Reaction & Selective Reductions",
                "content": r"""Nitro compounds contain a nitro group ($-\text{NO}_2$) characterized by a formal positive charge on nitrogen and equivalent $-0.5$ partial charges on the two oxygen atoms.

### Aliphatic Nitro Compounds & Aci-Nitro Tautomerism
Protons on the $\alpha$-carbon of primary and secondary nitroalkanes are remarkably acidic ($\text{p}K_a \approx 10$ for nitromethane):

$$\text{R-CH}_2\text{-NO}_2 + \text{OH}^- \rightleftharpoons [\text{R-CH}=\text{N}^+(\text{O}^-)\text{O}^-] + \text{H}_2\text{O} \tag{5.16}$$

Upon acidification, protonation can occur on oxygen rather than carbon, yielding the acidic **aci-nitro tautomer** (nitronic acid):

$$\text{R-CH}_2\text{-NO}_2 \longleftrightarrow \text{R-CH}=\text{N}(\text{OH})=\text{O} \quad (\text{aci-form}) \tag{5.17}$$

### The Nef Reaction
Treatment of primary or secondary nitroalkane salts with cold aqueous sulfuric acid hydrolyzes the aci-nitro species to yield **aldehydes or ketones**:

$$\text{R}_2\text{C}=\text{NO}_2^-\text{Na}^+ + 2\,\text{H}_2\text{SO}_4 + \text{H}_2\text{O} \longrightarrow \text{R}_2\text{C}=\text{O} + \text{N}_2\text{O}\uparrow + 2\,\text{NaHSO}_4 \tag{5.18}$$

The Nef reaction provides an essential synthetic link between Henry nitroaldol additions and carbonyl construction.

### Selective Reduction of Nitroarenes
Aromatic nitro groups undergo diverse reductions depending on the chemical conditions:
1. **Exhaustive Reduction to Primary Amines**:
   $$\text{Ar-NO}_2 \xrightarrow{\text{Fe / HCl or Sn / HCl or H}_2, \text{Pd/C}} \text{Ar-NH}_2$$
2. **Selective Reduction of Dinitroarenes (Zinin Reduction)**:
   When 1,3-dinitrobenzene is treated with sodium sulfide ($\text{Na}_2\text{S}$) or ammonium polysulfide ($(\text{NH}_4)_2\text{S}_x$), only **one** of the two nitro groups is reduced, yielding 3-nitroaniline in high yield:
   $$m\text{-C}_6\text{H}_4(\text{NO}_2)_2 + 3\,(\text{NH}_4)_2\text{S} \longrightarrow m\text{-O}_2\text{N-C}_6\text{H}_4\text{-NH}_2 + 6\,\text{NH}_3 + 3\,\text{S}\downarrow + 2\,\text{H}_2\text{O} \tag{5.19}$$
3. **Controlled Partial Reductions in Neutral / Alkaline Media**:
   - With zinc dust and aqueous ammonium chloride ($\text{Zn / NH}_4\text{Cl}$): Nitrobenzene is reduced to **$N$-phenylhydroxylamine** ($\text{PhNHOH}$).
   - With zinc dust in alkaline $\text{NaOH}$: Coupling yields **hydrazobenzene** ($\text{PhNH-NHPh}$), which undergoes the benzidine rearrangement in acid to form 4,4'-diaminobiphenyl.""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob5_1",
                "problemNumber": "5.1",
                "title": "Quantum Tunneling & Inversion Barrier Dynamics in Ammonia vs Trimethylamine",
                "difficulty": "Mastery",
                "statement": r"""The inversion barrier of ammonia ($\text{NH}_3$) is $\Delta E_{\text{inv}} = 24.2\text{ kJ}\cdot\text{mol}^{-1}$ ($2020\text{ cm}^{-1}$), resulting in a tunneling splitting of the ground vibrational state of $\Delta \nu_0 = 23.786\text{ GHz}$ ($\lambda \approx 1.26\text{ cm}$).
(a) Using the de Broglie wavelength and WKB tunneling approximation $P \approx \exp\left(-\frac{2}{\hbar}\int \sqrt{2m(V(x)-E)}\, dx\right)$, explain why substituting hydrogen with methyl groups (yielding $\text{NMe}_3$, $\Delta E_{\text{inv}} \approx 35.6\text{ kJ}\cdot\text{mol}^{-1}$) completely suppresses quantum tunneling.
(b) Calculate the classical inversion frequency $k_{\text{cl}}$ for trimethylamine at $298\text{ K}$ using the Eyring equation.
(c) Explain why 1-chloro-2,2-dimethylaziridine can be resolved into stable optical enantiomers at room temperature.""",
                "hints": ["Consider the mass of three protons versus three methyl groups ($m_{\text{eff}}$).", "Strained 3-membered rings have severe angle strain in planar transition states."],
                "solution": r"""### (a) WKB Quantum Tunneling Suppression
The tunneling probability $P$ across a potential barrier $V(x)$ depends exponentially on the effective mass $m$ of the inverting atoms:
$$P \propto \exp\left(-\frac{2}{\hbar} \sqrt{2 m \Delta V} \cdot a\right)$$
where $a$ is the barrier width.
- In **ammonia ($\text{NH}_3$)**, the inverting particles are three light protons ($m \approx 1\text{ amu}$). The light mass permits significant wavefunction penetration through the barrier, generating measurable quantum tunneling splitting ($\Delta \nu_0 = 23.8\text{ GHz}$).
- In **trimethylamine ($\text{NMe}_3$)**, inversion requires synchronous displacement of three heavy methyl groups ($\text{CH}_3$, mass $= 15\text{ amu}$). The effective mass increases by a factor of 15:
  $$\sqrt{m_{\text{NMe}_3} / m_{\text{NH}_3}} \approx \sqrt{15} \approx 3.87$$
  Because the tunneling probability decreases exponentially with mass ($e^{-3.87 \times \text{factor}} \to 0$), quantum tunneling is attenuated by $>10^8$-fold, making inversion purely classical.

### (b) Classical Inversion Rate of Trimethylamine
Using the Eyring equation:
$$k_{\text{inv}} = \frac{k_B T}{h} \exp\left(-\frac{\Delta G^\ddagger}{RT}\right)$$
Given $\Delta G^\ddagger \approx 35.6\text{ kJ}\cdot\text{mol}^{-1}$ at $T = 298.15\text{ K}$:
$$\frac{k_B T}{h} = 6.212 \times 10^{12}\text{ s}^{-1}$$
$$\frac{\Delta G^\ddagger}{RT} = \frac{35,600}{(8.314) \times (298.15)} = \frac{35,600}{2478.8} = 14.36$$
$$\exp(-14.36) = 5.79 \times 10^{-7}$$
$$k_{\text{inv}} = (6.212 \times 10^{12}) \times (5.79 \times 10^{-7}) \approx 3.6 \times 10^6\text{ s}^{-1}$$
Trimethylamine still inverts several million times per second at $25^\circ\text{C}$, preventing resolution of simple acyclic amines.

### (c) Enantiomer Resolution in 1-Chloro-2,2-dimethylaziridine
In this aziridine:
1. **Angle Strain**: The three-membered ring locks the ground-state $\text{C}-\text{N}-\text{C}$ bond angle at $\sim 60^\circ$ ($sp^3$ hybridized). To invert, the nitrogen must adopt a planar $sp^2$ transition state where the ideal bond angle is $120^\circ$. Forcing a $120^\circ$ angle into a rigid $60^\circ$ ring imposes severe Baeyer angle strain ($\Delta E_{\text{strain}} > 60\text{ kJ}\cdot\text{mol}^{-1}$).
2. **Electronegative Chlorine**: The chlorine atom exerts strong inductive withdrawal ($-I$) and lone-pair/lone-pair repulsion with the nitrogen lone pair in the planar transition state.
Together, these factors elevate the inversion barrier to $\Delta G^\ddagger \approx 110\text{ kJ}\cdot\text{mol}^{-1}$. At room temperature, this corresponds to an inversion half-life of months, permitting resolution of pure enantiomers."""
            },
            {
                "id": "prob5_2",
                "problemNumber": "5.2",
                "title": "Stereoselective Hofmann vs Zaitsev Elimination in 2-Aminobutane",
                "difficulty": "Intermediate",
                "statement": r"""2-Aminobutane is converted into its quaternary ammonium hydroxide salt and heated to $130^\circ\text{C}$.
(a) Provide the complete reaction steps for exhaustive methylation and silver oxide conversion.
(b) Identify the major and minor alkene products formed upon elimination, and give their quantitative ratio.
(c) Using Newman projections, explain why 1-butene is formed rather than 2-butene, contrasting this with the dehydrohalogenation of 2-bromobutane with sodium ethoxide.""",
                "hints": ["Exhaustive methylation uses 3 equivalents of methyl iodide.", "Look at the steric bulk of the trimethylammonium group in the Newman projections."],
                "solution": r"""### (a) Synthetic Sequence
$$\begin{aligned}
\text{Step 1}: &\quad \text{CH}_3\text{CH}_2\text{CH(NH}_2)\text{CH}_3 + 3\,\text{CH}_3\text{I} \longrightarrow \text{CH}_3\text{CH}_2\text{CH}[\text{N}^+(\text{CH}_3)_3]\text{CH}_3\,\text{I}^- + 2\,\text{HI} \\
\text{Step 2}: &\quad \text{Quaternary iodide} + \text{Ag}_2\text{O} + \text{H}_2\text{O} \longrightarrow \text{CH}_3\text{CH}_2\text{CH}[\text{N}^+(\text{CH}_3)_3]\text{CH}_3\,\text{OH}^- + \text{AgI}\downarrow
\end{aligned}$$

### (b) Alkene Product Distribution
Upon heating to $130^\circ\text{C}$:
- **Major Product**: **1-Butene** ($\sim 95\%$, Hofmann product).
- **Minor Product**: **2-Butene** (*cis* + *trans*, $\sim 5\%$, Zaitsev product).

### (c) Newman Projection Rationale
1. **Hofmann Elimination (Bulky $-\text{N}^+\text{Me}_3$)**:
   - To eliminate across C2-C3 (forming 2-butene), a $\beta$-hydrogen at C3 must adopt an *anti*-periplanar geometry ($180^\circ$) with the $-\text{N}^+\text{Me}_3$ group. In this conformation, the bulky $-\text{N}^+\text{Me}_3$ group is forced into severe **gauche steric clash** with the C4 methyl group.
   - To eliminate across C2-C1 (forming 1-butene), the base abstracts a proton from the terminal C1 methyl group. The Newman projection reveals that the $-\text{N}^+\text{Me}_3$ group can align *anti* to a C1 proton while avoiding any gauche steric overlap with other alkyl groups.
   - Furthermore, the strong $-I$ inductive pull of $-\text{N}^+\text{Me}_3$ stabilizes developing negative charge, making the less substituted primary C1 carbanion far more stable than the secondary C3 carbanion.
2. **Dehydrohalogenation of 2-Bromobutane (Small $-\text{Br}$)**:
   In contrast, when 2-bromobutane reacts with $\text{NaOEt}$, the bromide leaving group is compact. Product distribution is dictated strictly by the thermodynamic stability of the forming alkene double bond (hyperconjugation). The disubstituted **2-butene** dominates ($81\%$, Zaitsev product) over 1-butene ($19\%$)."""
            },
            {
                "id": "prob5_3",
                "problemNumber": "5.3",
                "title": "Diazotization Kinetics & Sandmeyer Synthesis of 4-Bromobenzonitrile",
                "difficulty": "Mastery",
                "statement": r"""Devise an efficient multi-step synthesis of 4-bromobenzonitrile starting from benzene.
(a) Detail all reagents, temperatures, and intermediate structures.
(b) Explain why bromination cannot be performed directly on benzonitrile.
(c) Detail the mechanism of the Sandmeyer substitution with copper(I) cyanide, identifying the oxidation state of copper and the radical intermediates involved.""",
                "hints": ["Nitrate first, reduce to aniline, brominate with activating group, then diazotize.", "Sandmeyer proceeds via single-electron transfer (SET)."],
                "solution": r"""### (a) Multi-Step Synthetic Route
$$\begin{aligned}
\text{Step 1}: &\quad \text{Benzene} \xrightarrow{\text{HNO}_3, \text{H}_2\text{SO}_4, 55^\circ\text{C}} \text{Nitrobenzene} \\
\text{Step 2}: &\quad \text{Nitrobenzene} \xrightarrow{\text{Fe, HCl, reflux, then NaOH}} \text{Aniline} \\
\text{Step 3}: &\quad \text{Aniline} \xrightarrow{\text{Ac}_2\text{O, AcOH}} \text{Acetanilide (protect amino group to prevent tribromination)} \\
\text{Step 4}: &\quad \text{Acetanilide} \xrightarrow{\text{Br}_2, \text{AcOH, }25^\circ\text{C}} \text{4-Bromoacetanilide} \\
\text{Step 5}: &\quad \text{4-Bromoacetanilide} \xrightarrow{\text{aq. NaOH, reflux}} \text{4-Bromoaniline} \\
\text{Step 6}: &\quad \text{4-Bromoaniline} \xrightarrow{\text{NaNO}_2, \text{conc. HCl, }0\text{–}5^\circ\text{C}} \text{4-Bromobenzenediazonium chloride} \\
\text{Step 7}: &\quad \text{4-Bromobenzenediazonium chloride} \xrightarrow{\text{CuCN, KCN, }50^\circ\text{C}} \text{4-Bromobenzonitrile} + \text{N}_2\uparrow
\end{aligned}$$

### (b) Failure of Direct Bromination of Benzonitrile
The cyano group ($-\text{C}\equiv\text{N}$) is a powerful meta-directing, strongly deactivating substituent. Electrophilic bromination of benzonitrile ($\text{Br}_2/\text{FeBr}_3$) would direct bromine exclusively to the **meta position**, yielding 3-bromobenzonitrile rather than the desired 4-bromo isomer.

### (c) Sandmeyer Radical Mechanism with $\text{CuCN}$
1. **Single-Electron Transfer (SET)**: The diazonium cation accepts an electron from $\text{Cu}^{\text{I}}$:
   $$[\text{Ar}-\text{N}\equiv\text{N}]^+ + \text{Cu}^{\text{I}}\text{CN} \longrightarrow [\text{Ar}-\text{N}=\text{N}^\bullet] + [\text{Cu}^{\text{II}}\text{CN}]^+$$
2. **Dinitrogen Extrusion**: Spontaneous, irreversible loss of dinitrogen generates an aryl radical:
   $$[\text{Ar}-\text{N}=\text{N}^\bullet] \longrightarrow \text{Ar}^\bullet + \text{N}_2\uparrow$$
3. **Ligand Transfer / Re-oxidation**: The aryl radical attacks the copper(II) species, abstracting the cyanide group:
   $$\text{Ar}^\bullet + [\text{Cu}^{\text{II}}(\text{CN})_2] \longrightarrow \text{Ar-CN} + \text{Cu}^{\text{I}}\text{CN}$$
Copper acts as a true redox catalyst ($\text{Cu}^{\text{I}} \rightleftharpoons \text{Cu}^{\text{II}}$), cleanly installing the cyano functionality."""
            },
            {
                "id": "prob5_4",
                "problemNumber": "5.4",
                "title": "pH-Dependent Coupling Kinetics & Bathochromic Shift in Methyl Orange",
                "difficulty": "Mastery",
                "statement": r"""Methyl orange is synthesized by coupling diazotized sulfanilic acid with $N,N$-dimethylaniline.
(a) Write the balanced reaction equation and derive why the optimal reaction $\text{pH}$ is maintained strictly between $4.0$ and $5.0$.
(b) Explain the chemical equilibrium responsible for the color change of methyl orange from red ($\lambda_{\max} \approx 510\text{ nm}$) in acid to yellow ($\lambda_{\max} \approx 460\text{ nm}$) in base.
(c) Using particle-in-a-box / frontier orbital theory, calculate the reduction in excitation energy $\Delta E = h c / \lambda$ corresponding to the $50\text{ nm}$ bathochromic shift.""",
                "hints": ["Coupling requires free unprotonated amine and electrophilic diazonium cation.", "Protonation in acid forms a quinonoid resonance structure."],
                "solution": r"""### (a) Reaction and $\text{pH}$ Optimization
Reaction:
$$[4\text{-}^-\text{O}_3\text{S-C}_6\text{H}_4\text{-N}_2^+] + \text{PhNMe}_2 \xrightarrow{\text{pH }4\text{–}5} 4\text{-}^-\text{O}_3\text{S-C}_6\text{H}_4\text{-N}=\text{N-C}_6\text{H}_4\text{-NMe}_2 + \text{H}^+$$
**$\text{pH}$ Optimization ($4.0\text{–}5.0$)**:
- **At $\text{pH} < 3.0$**: The amine nucleophile is protonated into an unreactive ammonium cation ($[\text{PhNHMe}_2]^+$). The unshared lone pair on nitrogen is tied up, preventing nucleophilic attack.
- **At $\text{pH} > 8.0$**: The diazonium cation reacts with hydroxide to form unreactive diazotate salts ($[\text{Ar-N}=\text{N-O}]^-$).
- Only in the narrow window of **$\text{pH } 4.0\text{–}5.0$** does a high equilibrium concentration of both the electrophilic diazonium cation and the unprotonated free amine coexist simultaneously.

### (b) Chromophore Quinonoid Resonance in Acid
- **Basic Form (Yellow, $\text{pH} > 4.4$, $\lambda_{\max} = 460\text{ nm}$)**:
  Existed as the neutral azo structure:
  $$^-\text{O}_3\text{S}-\text{C}_6\text{H}_4-\text{N}=\text{N}-\text{C}_6\text{H}_4-\text{NMe}_2$$
- **Acidic Form (Red, $\text{pH} < 3.1$, $\lambda_{\max} = 510\text{ nm}$)**:
  Protonation occurs selectively on the azo nitrogen adjacent to the sulfonate ring. A powerful **quinonoid resonance contributor** forms:
  $$^-\text{O}_3\text{S}-\text{C}_6\text{H}_4-\text{NH}-\text{N}=\text{C}_6\text{H}_4=\text{N}^+\text{Me}_2 \longleftrightarrow \text{Quinonoid dication form}$$
  This quinonoid form features continuous, unbroken polyene delocalization across both aromatic rings and both nitrogen atoms, dramatically extending the effective conjugation length.

### (c) Calculation of the Bathochromic Energy Gap ($\Delta \Delta E$)
$$\Delta E = \frac{h c}{\lambda}$$
Constants:
$$h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}, \quad c = 2.998 \times 10^8\text{ m/s}$$
$$h c = 1.986 \times 10^{-25}\text{ J}\cdot\text{m} = 1.2398 \times 10^{-6}\text{ eV}\cdot\text{m}$$

1. **For Yellow Form ($\lambda_1 = 460\text{ nm} = 4.60 \times 10^{-7}\text{ m}$)**:
   $$\Delta E_1 = \frac{1.986 \times 10^{-25}}{4.60 \times 10^{-7}} = 4.317 \times 10^{-19}\text{ J} \approx 2.70\text{ eV} \quad (260.0\text{ kJ}\cdot\text{mol}^{-1})$$

2. **For Red Form ($\lambda_2 = 510\text{ nm} = 5.10 \times 10^{-7}\text{ m}$)**:
   $$\Delta E_2 = \frac{1.986 \times 10^{-25}}{5.10 \times 10^{-7}} = 3.894 \times 10^{-19}\text{ J} \approx 2.43\text{ eV} \quad (234.5\text{ kJ}\cdot\text{mol}^{-1})$$

The decrease in the HOMO-LUMO excitation gap upon protonation is:
$$\Delta(\Delta E) = 260.0 - 234.5 = 25.5\text{ kJ}\cdot\text{mol}^{-1} \quad (0.27\text{ eV})$$
This reduction in the HOMO-LUMO gap shifts the absorption into the green region, causing the reflected transmitted light to appear red."""
            },
            {
                "id": "prob5_5",
                "problemNumber": "5.5",
                "title": "Regioselective Zinin Reduction of 1,3-Dinitrobenzene",
                "difficulty": "Intermediate",
                "statement": r"""When 1,3-dinitrobenzene is treated with sodium hydrogen sulfide ($\text{NaHS}$) in boiling aqueous ethanol, 3-nitroaniline is isolated in $85\%$ yield, while catalytic hydrogenation over $\text{Pd/C}$ yields benzene-1,3-diamine exclusively.
(a) Write the balanced stoichiometric redox equation for the Zinin reduction.
(b) Mechanistically explain why sulfide reduces only one nitro group and stops cleanly, whereas catalytic hydrogenation reduces both.
(c) How does the reduction of the first nitro group to an amino group electronically deactivate the remaining nitro group toward further sulfide reduction?""",
                "hints": ["Sulfide is an electron donor; the nitro group is electron-withdrawing.", "Amino group is a powerful electron donor."],
                "solution": r"""### (a) Balanced Stoichiometric Redox Equation
$$m\text{-C}_6\text{H}_4(\text{NO}_2)_2 + 3\,\text{NaHS} + \text{H}_2\text{O} \longrightarrow m\text{-O}_2\text{N-C}_6\text{H}_4\text{-NH}_2 + 3\,\text{S}\downarrow + 3\,\text{NaOH}$$
Sulfur is oxidized from $\text{S}^{2-}$ in $\text{HS}^-$ to elemental sulfur $\text{S}^0$ (oxidation state $0$). Nitrogen in one nitro group is reduced from $+3$ to $-3$ in the amino group (6-electron reduction).

### (b) Mechanistic Basis of Monoreduction
The Zinin reduction is an **outer-sphere single-electron transfer (SET)** from sulfide to the $\pi^*$ orbital of the nitro group:
$$\text{Ar-NO}_2 + \text{HS}^- \longrightarrow [\text{Ar-NO}_2]^{\bullet-} + \text{HS}^\bullet$$
- In **1,3-dinitrobenzene**, the two nitro groups are mutually electron-withdrawing. The lowest unoccupied molecular orbital (LUMO) of the dinitroarene is very low in energy ($\sim -2.5\text{ eV}$), making it an exceptionally strong electron acceptor that reacts readily with sulfide.
- In **catalytic hydrogenation ($\text{H}_2/\text{Pd}$)**, the reaction occurs heterogeneously on the metal catalyst surface where hydride addition is driven by strong chemisorption. Both nitro groups are rapidly and non-selectively hydrogenated to yield $m$-phenylenediamine.

### (c) Electronic Deactivation after First Reduction
Once the first nitro group is reduced to an amino group ($-\text{NH}_2$):
- The amino group is a powerful resonance electron-donor ($+M$).
- Resonance donation of the amino lone pair pushes extensive electron density into the benzene ring and directly into the remaining nitro group.
- This raises the LUMO energy of 3-nitroaniline by $>1.2\text{ eV}$, rendering it far too electron-rich to accept an electron from sulfide under these conditions. The reduction ceases cleanly after one nitro group."""
            },
            {
                "id": "prob5_6",
                "problemNumber": "5.6",
                "title": "Stereospecificity of the Curtius vs Hofmann Rearrangement",
                "difficulty": "Advanced",
                "statement": r"""Optically active (S)-2-methylbutanoic acid ($[\alpha]_D^{25} = +17.6^\circ$) is converted into 2-butylamine via two different pathways:
- Pathway A: Conversion to (S)-2-methylbutanoyl chloride, reaction with $\text{NaN}_3$, thermal Curtius rearrangement, and acidic hydrolysis.
- Pathway B: Conversion to (S)-2-methylbutanamide, reaction with $\text{Br}_2/\text{NaOH}$ (Hofmann rearrangement).
(a) Determine the absolute stereochemical configuration (R or S) and optical purity of the 2-butylamine produced by each pathway.
(b) Mechanistically justify why both rearrangements proceed with $100\%$ retention of configuration at the migrating stereocenter.
(c) State why free carbocations or free radical intermediates can be ruled out definitively.""",
                "hints": ["Migration occurs in a concerted manner on the same face.", "Assign CIP priorities to (S)-2-methylbutanoic acid vs 2-butylamine."],
                "solution": r"""### (a) Stereochemical Configuration & Optical Purity
Both pathways yield **(S)-2-butylamine** with **$100\%$ optical purity** ($>99.9\%$ enantiomeric excess):
- **Pathway A (Curtius)**: Yields (S)-2-butylamine with complete retention.
- **Pathway B (Hofmann)**: Yields (S)-2-butylamine with complete retention.
Let us verify CIP priority at the stereocenter:
- In *(S)*-2-methylbutanoic acid: C1 is $-\text{COOH}$ (priority 1), C3 is $-\text{CH}_2\text{CH}_3$ (priority 2), C4 is $-\text{CH}_3$ (priority 3), and H is 4.
- In *(S)*-2-butylamine: C1 is $-\text{NH}_2$ (priority 1), C3 is $-\text{CH}_2\text{CH}_3$ (priority 2), C4 is $-\text{CH}_3$ (priority 3), and H is 4.
Because the priority ranking order of substituents around the chiral carbon is identically preserved, retention of configuration retains the **(S)** stereodescriptor.

### (b) Mechanistic Proof of Complete Retention
In both the Curtius and Hofmann rearrangements, migration of the chiral alkyl group from the carbonyl carbon to the electron-deficient nitrogen atom occurs via a **concerted [1,2]-sigmatropic shift**:
$$\text{Transition State}: \quad \left[ \text{O}=\text{C} \cdots \underset{\text{chiral C}}{\text{R}} \cdots \text{N} \cdots \text{X} \right]^\ddagger$$
- The migrating $\text{C}-\text{C}$ $\sigma$-bonding electron pair attacks the empty orbital on nitrogen simultaneously with departure of the leaving group ($\text{N}_2$ in Curtius, $\text{Br}^-$ in Hofmann).
- Migration takes place exclusively through a three-center two-electron ($3c\text{–}2e$) frontside transition state.
- The chiral center never detaches from the molecular framework, guaranteeing $100\%$ retention of spatial geometry.

### (c) Exclusion of Radical or Carbocation Intermediates
If a free planar carbocation ($[\text{R}]^+$) or free alkyl radical ($\text{R}^\bullet$) were generated:
1. The $sp^2$-hybridized radical or carbocation would possess a planar geometry with a horizontal symmetry plane.
2. Trapping by the nitrogen atom would occur with equal probability from the *top* and *bottom* faces, leading to complete or extensive racemization (loss of optical activity).
Because zero racemization is observed experimentally ($[\alpha]_D$ corresponds to 100% enantiomeric excess), free radical and carbocation intermediates are ruled out conclusively."""
            },
            {
                "id": "prob5_7",
                "problemNumber": "5.7",
                "title": "Synthesis of Sulfanilamide via Protected Diazotization Chemistry",
                "difficulty": "Intermediate",
                "statement": r"""Sulfanilamide (4-aminobenzenesulfonamide) is the parent member of the sulfa drug family.
(a) Outline the total synthesis of sulfanilamide starting from aniline.
(b) Why must aniline first be protected as acetanilide before chlorosulfonation with chlorosulfonic acid ($\text{ClSO}_3\text{H}$)?
(c) Write the reaction equations for chlorosulfonation, amination with ammonia, and final deprotection.""",
                "hints": ["Direct chlorosulfonation of free aniline results in salt formation and uncontrolled polysulfonation.", "Acetanilide moderates reactivity and protects the amino group."],
                "solution": r"""### (a) Multi-Step Total Synthesis
$$\begin{aligned}
\text{Step 1 (Acetylation Protection)}: &\quad \text{Aniline} + \text{Ac}_2\text{O} \xrightarrow{\text{AcOH}} \text{Acetanilide} + \text{AcOH} \\
\text{Step 2 (Chlorosulfonation)}: &\quad \text{Acetanilide} + 2\,\text{ClSO}_3\text{H} \xrightarrow{60^\circ\text{C}} 4\text{-acetamidobenzenesulfonyl chloride} + \text{H}_2\text{SO}_4 + \text{HCl}\uparrow \\
\text{Step 3 (Sulfonamide Formation)}: &\quad 4\text{-acetamidobenzenesulfonyl chloride} + 2\,\text{NH}_3 \longrightarrow 4\text{-acetamidobenzenesulfonamide} + \text{NH}_4\text{Cl} \\
\text{Step 4 (Selective Deprotection)}: &\quad 4\text{-acetamidobenzenesulfonamide} \xrightarrow{\text{dilute HCl, reflux, then neutralize}} \text{Sulfanilamide} + \text{AcOH}
\end{aligned}$$

### (b) Rationale for Acetylation Protection
Free aniline cannot be chlorosulfonated directly:
1. **Acid-Base Neutralization**: The strongly acidic chlorosulfonic acid ($\text{ClSO}_3\text{H}$) protonates the basic amino group of aniline, converting it into the strongly deactivated anilinium cation ($-\text{NH}_3^+$). This directs electrophilic substitution to the *meta* position rather than the required *para* position.
2. **Violent Side Reactions**: Unprotected amino groups react directly with the sulfonyl chloride functionality of other molecules, resulting in uncontrolled polymerization and poly-chlorosulfonation.
Converting aniline to **acetanilide** tempers the activating power of nitrogen through resonance with the acetyl carbonyl, maintains *ortho/para* directing ability without protonation, and protects the amino group.

### (c) Selective Hydrolysis Step
In Step 4, the molecule possesses both an **amide** group ($-\text{NHCOCH}_3$) and a **sulfonamide** group ($-\text{SO}_2\text{NH}_2$).
Carboxamides are dramatically more susceptible to acid-catalyzed hydrolysis ($k_{\text{carboxamide}} \gg 10^3 \times k_{\text{sulfonamide}}$) because the carbonyl carbon has a lower LUMO and forms a tetrahedral intermediate readily. Dilute aqueous $\text{HCl}$ at $100^\circ\text{C}$ selectively cleaves the acetyl protecting group without affecting the sulfonamide bond, delivering pure sulfanilamide."""
            }
        ]
    }

def get_unit_6():
    return {
        "id": "unit6",
        "unitId": "unit6-org2",
        "number": 6,
        "unitNumber": 6,
        "title": "Unit 6: Stereochemistry: Optical Activity, Dissymmetry, Axial/Planar Chirality & Asymmetric Induction",
        "description": "Exhaustive treatment of modern stereochemistry: symmetry operations and group theoretical criteria for chirality (lack of improper rotation axes S_n), Biot's law and polarimetry instrumentation; stereoisomerism taxonomies (enantiomers, diastereomers, meso forms, pseudoasymmetry); chirality without stereocenters (allenes, atropisomerism in ortho-substituted biphenyls, BINAP, cyclophanes, trans-cyclooctene, helicenes); racemization dynamics and optical resolution protocols; and asymmetric synthesis models (Cram, Felkin-Anh open-chain transition states, and Evans chiral auxiliaries).",
        "leadSummary": "Advanced physical organic analysis of molecular dissymmetry, symmetry operations, polarimetric optics, axial/planar/helical chirality, atropisomeric biaryls, resolution thermodynamics, and Felkin-Anh asymmetric induction models.",
        "simulations": ["sim_chem_optical_activity_polarimeter_3d"],
        "sections": [
            {
                "id": "sec6_1",
                "secNumber": "§6.1",
                "title": "Symmetry Operations, Point Groups & Group-Theoretical Criteria for Chirality",
                "heading": "Symmetry Operations, Point Groups & Group-Theoretical Criteria for Chirality",
                "content": r"""In modern stereochemistry, chirality is defined not merely by the presence of an asymmetric $sp^3$ carbon atom, but by the fundamental geometric symmetry of the molecular point group.

### The Group-Theoretical Criterion of Chirality
A molecule is chiral (dissymmetric) if and only if it **cannot be superimposed onto its mirror image** by any combination of proper rotations ($C_n$).
In rigorous group theory, a molecule is **achiral** if its equilibrium point group contains at least one **improper rotation axis ($S_n$)**:

$$\text{Chirality Criterion}: \quad \text{Point Group does NOT contain } S_n \quad (n \ge 1) \tag{6.1}$$

The improper rotation operation $S_n$ consists of a proper rotation by an angle $\theta = \frac{360^\circ}{n}$ followed by reflection through a plane perpendicular to the rotation axis:

$$S_n \equiv \sigma_h \cdot C_n \tag{6.2}$$

Special cases of improper rotation axes include:
1. **$S_1 \equiv \sigma$ (Plane of Symmetry)**: Rotation by $360^\circ$ followed by reflection is identical to simple reflection through a plane. Any molecule possessing an internal plane of symmetry ($\sigma$) is achiral (e.g., *meso*-tartaric acid).
2. **$S_2 \equiv i$ (Center of Inversion)**: Rotation by $180^\circ$ followed by reflection through the perpendicular plane is identical to inversion through a central point ($i$):
   $$(x, y, z) \xrightarrow{S_2} (-x, -y, -z) \tag{6.3}$$
   Any molecule possessing an inversion center ($i$) is strictly achiral, even if it contains multiple chiral centers (e.g., $(1R,2S,3R,4S)$-1,3-dichloro-2,4-difluorocyclobutane).
3. **Higher Alternating Axes ($S_4, S_6$)**: A molecule can lack both a plane of symmetry ($\sigma$) and an inversion center ($i$) and yet remain completely achiral if it possesses an alternating axis of symmetry $S_4$! A classic example is 3,4,8,9-tetramethylspiro[5.5]undecane-1,7-dione, which belongs to the achiral point group $D_{2d}$ and possesses zero optical activity despite lacking $\sigma$ and $i$.

Chiral molecules belong exclusively to the **chiral point groups**: $C_1$ (completely asymmetric), $C_n$ (dissymmetric with proper rotation axis, e.g., tartaric acid with $C_2$ symmetry), and $D_n$ (e.g., twisted biphenyls with $D_2$ symmetry).""",
                "simulations": ["sim_chem_optical_activity_polarimeter_3d"]
            },
            {
                "id": "sec6_2",
                "secNumber": "§6.2",
                "title": "Optical Activity, Biot's Law & Polarimetry Instrumentation",
                "heading": "Optical Activity, Biot's Law & Polarimetry Instrumentation",
                "content": r"""Chiral molecules interact differently with left- and right-circularly polarized light, rotating the plane of plane-polarized light—a macroscopic physical phenomenon termed **optical activity**.

```
                Laurent Polarimeter Optical Train:
Monochromatic    Polarizer       Sample Tube       Analyzer         Half-Shade
Light Source  (Nicol Prism)   (Chiral Solution)  (Nicol Prism)      Detector
   [Na-D]   ===>  [ | ]   =====>  [ (alpha) ]  =====>  [ / ]  =====>  [Eyes/PMT]
  589.3 nm      Linear Pol.       Rotated Plane      Adjustable     Zero-Balance
```

### Wave Optics & Circular Birefringence
Plane-polarized light can be resolved into two coherent, orthogonal circularly polarized components of equal amplitude rotating in opposite directions:
- Left-circularly polarized light ($\mathbf{E}_L$)
- Right-circularly polarized light ($\mathbf{E}_R$)

When plane-polarized light passes through an isotropic solution of chiral molecules, the refractive indices for left- and right-circularly polarized light differ ($n_L \neq n_R$), a property known as **circular birefringence**:

$$\Delta n = n_L - n_R \tag{6.4}$$

Because the two circular waves travel through the medium at different phase velocities ($v = c / n$), they accumulate a phase difference $\Delta \theta$, causing the resultant linear polarization plane to rotate by an angle $\alpha$:

$$\alpha = \frac{\pi}{\lambda} \, l \, (n_L - n_R) \tag{6.5}$$

### Biot's Law and Specific Rotation
Formulated by Jean-Baptiste Biot in 1815, **Biot's law** states that the observed optical rotation $\alpha$ (in degrees) is directly proportional to the path length $l$ and the concentration $c$ of the chiral solute:

$$[\alpha]_\lambda^T = \frac{\alpha}{l \cdot c} \tag{6.6}$$

where:
- $[\alpha]_\lambda^T$ is the **specific rotation** at temperature $T$ and wavelength $\lambda$ (typically the sodium D line, $\lambda = 589.3\text{ nm}$).
- $\alpha$ is the observed angle of rotation in degrees ($^\circ$).
- $l$ is the optical path length in **decimeters** ($1\text{ dm} = 10\text{ cm}$).
- $c$ is the concentration in **grams per milliliter** ($\text{g}\cdot\text{mL}^{-1}$ or $\text{g}\cdot\text{cm}^{-3}$). For neat liquids, concentration is replaced by density $\rho$ ($\text{g}\cdot\text{mL}^{-1}$).

Molar optical rotation is defined as:

$$[\Phi] = \frac{M \cdot [\alpha]}{100} \tag{6.7}$$

where $M$ is the molecular mass in $\text{g}\cdot\text{mol}^{-1}$.""",
                "simulations": []
            },
            {
                "id": "sec6_3",
                "secNumber": "§6.3",
                "title": "Stereoisomerism Taxonomy: Enantiomers, Diastereomers & Pseudoasymmetry",
                "heading": "Stereoisomerism Taxonomy: Enantiomers, Diastereomers & Pseudoasymmetry",
                "content": r"""The stereochemical classification of molecules with multiple stereocenters follows precise mathematical and geometric taxonomies.

### Enantiomers, Diastereomers & Meso Forms
For a molecule containing $n$ constitutionally distinct stereocenters, the theoretical maximum number of stereoisomers is given by the van 't Hoff rule:

$$N_{\max} = 2^n \tag{6.8}$$

1. **Enantiomers**: Non-superimposable mirror-image stereoisomers. All chiral centers have opposite configurations ($(R,R)$ vs $(S,S)$). Enantiomers possess identical scalar physical properties (melting point, boiling point, density, refractive index, NMR chemical shifts in achiral media) and equal but opposite specific rotations:
   $$[\alpha]_D^{(+)} = -[\alpha]_D^{(-)}$$
2. **Diastereomers**: Stereoisomers that are not mirror images of one another. At least one stereocenter has the same configuration while at least one is inverted ($(R,R)$ vs $(R,S)$). Diastereomers possess different physical and thermodynamic properties (distinct melting points, solubilities, dipole moments, free energies).
3. **Meso Compounds**: Achiral stereoisomers possessing multiple stereocenters and an internal symmetry element ($\sigma$ or $i$). In tartaric acid ($n=2$):
   - $(2R,3R)$-tartaric acid ($[\alpha]_D = +12.4^\circ$, dextrorotatory)
   - $(2S,3S)$-tartaric acid ($[\alpha]_D = -12.4^\circ$, levorotatory)
   - $(2R,3S)$-tartaric acid: Features an internal mirror plane ($\sigma$), identical to $(2S,3R)$. It is an optically inactive **meso form** ($[\alpha]_D = 0^\circ$).

### Pseudoasymmetric Centers ($r / s$ Descriptors)
In symmetric molecules such as 2,3,4-trihydroxyglutaric acid:
$$\text{HOOC}-\text{CH(OH)}-\text{CH(OH)}-\text{CH(OH)}-\text{COOH}$$
The central carbon atom (C3) is bonded to two constitutionally identical chiral ligands:
$$-\text{CH(OH)COOH} \quad (\text{at C2}) \quad \text{and} \quad -\text{CH(OH)COOH} \quad (\text{at C4})$$
- When C2 is $(R)$ and C4 is $(S)$, the two ligands are enantiomorphic (mirror images).
- C3 now resides on a plane of symmetry, but its spatial orientation creates two distinct diastereomers depending on whether $-\text{OH}$ is oriented *cis* or *trans* to the flanking groups!
Such a center is termed **pseudoasymmetric**. It is designated using lower-case CIP stereodescriptors: **$(r)$** or **$(s)$** (by convention, the $(R)$-configured ligand takes priority over the $(S)$-configured ligand). Inversion of a pseudoasymmetric center converts one meso diastereomer into another meso diastereomer without generating optical activity.""",
                "simulations": []
            },
            {
                "id": "sec6_4",
                "secNumber": "§6.4",
                "title": "Chirality Without Stereocenters: Axial, Planar & Helical Chirality",
                "heading": "Chirality Without Stereocenters: Axial, Planar & Helical Chirality",
                "content": r"""A central tenet of modern stereochemistry is that molecular chirality does **not** require an asymmetric carbon atom. Chirality can arise from a chiral axis, a chiral plane, or a chiral helix.

### 1. Axial Chirality: Allenes & Atropisomerism
Axial chirality occurs when four groups are held in a rigid non-planar arrangement about an axis:

#### A. Allenes ($\text{C}=\text{C}=\text{C}$)
The central carbon of an allene is $sp$-hybridized with two mutually perpendicular unhybridized $2p$ orbitals ($2p_y$ and $2p_z$). Consequently, the $\pi$ bonds to the terminal $sp^2$ carbons are orthogonal ($90^\circ$ twist):
- The two substituents on C1 lie in a vertical plane.
- The two substituents on C3 lie in a horizontal plane.
If each terminal carbon bears two different substituents ($\text{abC}=\text{C}=\text{Cab}$), the molecule lacks both a plane of symmetry ($\sigma$) and an inversion center ($i$), belonging to the chiral point group $C_2$ (or $C_1$ if $\text{abC}=\text{C}=\text{Ccd}$). The enantiomers are designated using axial CIP rules ($aR / aS$ or $R_a / S_a$).

```
        Axial Chirality in Allenes and Ortho-Substituted Biphenyls:
               a                          O2N             NO2
                \   |                      \   \       /   /
                 C = C = C                  [ Ring A ]-[ Ring B ]
                /         \                /   /       \   \
               b           b             HOOC             COOH
           Vertical     Horizontal       Steric clash prevents coplanar rotation:
           Plane        Plane            Atropisomers isolable at 25 C (Delta G > 100 kJ/mol)
```

#### B. Atropisomerism in Biphenyls
In *ortho*-substituted biphenyls (such as 6,6'-dinitrobiphenyl-2,2'-dicarboxylic acid), rotation about the central $\text{C1}-\text{C1}'$ single bond is severely hindered by steric collision of the bulky *ortho* substituents:
- The planar transition state ($\theta = 0^\circ$ or $180^\circ$) requires bulky groups to pass each other, imposing a massive rotational barrier:
  $$\Delta G^\ddagger_{\text{rotation}} > 100\text{–}120\text{ kJ}\cdot\text{mol}^{-1} \quad (24\text{–}29\text{ kcal}\cdot\text{mol}^{-1}) \tag{6.9}$$
- The rotational half-life at room temperature exceeds thousands of years ($t_{1/2} > 10^4\text{ years}$), allowing the non-planar enantiomers (**atropisomers**, from the Greek *a-tropos*, "not turning") to be resolved into optically pure bottles.
- A prominent modern application is **BINAP** (2,2'-bis(diphenylphosphino)-1,1'-binaphthyl), an axially chiral $C_2$-symmetric ligand used in Ryoji Noyori's Nobel Prize-winning asymmetric hydrogenation catalysis.

### 2. Planar Chirality: Cyclophanes & *trans*-Cyclooctene
Planar chirality arises when a molecule contains an achiral plane (the chiral plane) with a substituent held rigidly out of that plane:
- ***trans*-Cyclooctene**: The smallest stable cycloalkene with a *trans* double bond. The eight-membered carbon chain is forced to loop over one face of the double bond, destroying mirror symmetry. It exists as stable $(pR)$ and $(pS)$ enantiomers ($[\alpha]_D = \pm 420^\circ$) with an exceptionally high racemization barrier ($\Delta G^\ddagger \approx 149\text{ kJ}\cdot\text{mol}^{-1}$).
- **Metallocenes & Cyclophanes**: Substituted ferrocenes with two different substituents on one cyclopentadienyl ring lack mirror symmetry and exhibit planar chirality.

### 3. Helical Chirality: Helicenes
Helicenes are polycyclic aromatic hydrocarbons in which benzene rings are angularly fused into a non-planar continuous spiral:
- In **[6]helicene (hexahelicene)** ($\text{C}_{26}\text{H}_{16}$), the terminal rings (rings 1 and 6) clash sterically, forcing the molecule into a rigid three-dimensional helix.
- Left-handed helices are designated **$(M)$** (minus); right-handed helices are designated **$(P)$** (plus).
- Hexahelicene exhibits extraordinary optical activity: $[\alpha]_D = \pm 3700^\circ$!""",
                "simulations": []
            },
            {
                "id": "sec6_5",
                "secNumber": "§6.5",
                "title": "Racemization Mechanisms & Thermodynamic Resolution Protocols",
                "heading": "Racemization Mechanisms & Thermodynamic Resolution Protocols",
                "content": r"""The physical separation of a 50:50 racemic mixture into its constituent pure enantiomers is known as **optical resolution**.

### Racemization Pathways
Racemization is the irreversible thermodynamic transformation of an optically active sample into an optically inactive racemate ($\Delta G^\circ_{\text{mix}} = -RT \ln 2 \approx -1.72\text{ kJ}\cdot\text{mol}^{-1}$ at $298\text{ K}$):
1. **Reversible Enolization**: Carbonyl compounds with $\alpha$-stereocenters undergo base- or acid-catalyzed enolization. The planar $sp^2$ enol intermediate loses chiral information, reprotonating equally from both faces.
2. **Reversible Carbocation Formation ($S_N1$)**: Solvolysis of chiral alkyl halides generating planar carbocations.
3. **Thermal Pyramidal Inversion or Radical Homolysis**: Homolytic cleavage of weak bonds followed by rapid radical recombination.

### Resolution Methodologies
Because enantiomers possess identical boiling points, melting points, and solubilities in achiral environments, they cannot be separated by standard fractional distillation or recrystallization. Modern resolution relies on four principal strategies:

```
               Resolution Methodologies Matrix:
1. Diastereomeric Salt Crystallization (Pasteur):
   (±)-Acid + (+)-Chiral Base  ===>  [(+)-Acid / (+)-Base] (Crystallizes)
                                     [(-)-Acid / (+)-Base] (Stays in solution)

2. Enzymatic Kinetic Resolution (EKR):
   (±)-Ester  --Lipase (Candida antarctica)--> (R)-Alcohol + (S)-Unreacted Ester

3. Chiral Stationary Phase HPLC (Pirkle CSPs):
   Differential three-point binding (Delta Delta G > 1 kJ/mol)

4. Chiral Auxiliaries (Evans Oxazolidinones):
   Enantioselective bond construction (de > 98%)
```

1. **Diastereomeric Salt Formation (Classical Pasteur Resolution)**:
   Reaction of a racemic acid ($(\pm)\text{-A}$) with an enantiomerically pure chiral base ($(+)\text{-B}$, such as brucine, strychnine, quinine, or $(R)\text{-}\alpha\text{-phenylethylamine}$) converts the mixture into **diastereomeric salts**:
   $$(\pm)\text{-A} + (+)\text{-B} \longrightarrow [(+)\text{-A}\cdot(+)\text{-B}] + [(-)\text{-A}\cdot(+)\text{-B}] \tag{6.10}$$
   Because diastereomers possess different lattice energies and solubilities, one salt crystallizes selectively upon cooling. Acidification recovers the pure enantiomer.
2. **Enzymatic Kinetic Resolution (EKR)**:
   Exploits the stereospecificity of enzymes (such as *Candida antarctica* lipase B, CALB). The enzyme catalyzes the hydrolysis of one enantiomer with an enzymatic rate constant $k_R \gg k_S$. Quenching at exactly $50\%$ conversion leaves the slow-reacting enantiomer unaltered while converting the fast-reacting enantiomer into a chemically distinct product with high enantiomeric excess ($ee > 99\%$).
3. **Chiral Stationary Phase (CSP) Chromatography**:
   Separation on HPLC columns packed with chiral selectors (e.g., cyclodextrins, amylose tris(3,5-dimethylphenylcarbamate), Pirkle-type brush phases). Enantiomers are resolved based on the **three-point interaction model** (Easson-Stedman hypothesis): one enantiomer forms three simultaneous attractive interactions (hydrogen bonding, $\pi\text{–}\pi$, steric clash) with the stationary phase, while the other forms only two, causing differential retention times.""",
                "simulations": []
            },
            {
                "id": "sec6_6",
                "secNumber": "§6.6",
                "title": "Asymmetric Synthesis & Felkin-Anh Stereochemical Models",
                "heading": "Asymmetric Synthesis & Felkin-Anh Stereochemical Models",
                "content": r"""Rather than synthesizing a racemic mixture and discarding $50\%$ of the material via resolution, **asymmetric synthesis** constructs chiral centers with stereocontrol.

### Evolution of Carbonyl Addition Models
When a nucleophile attacks a chiral aldehyde or ketone possessing an $\alpha$-stereocenter, two diastereomeric transition states compete:

#### 1. Cram's Open-Chain Rule (Donald Cram, 1952)
Cram classified the substituents on the $\alpha$-chiral carbon into Large ($L$), Medium ($M$), and Small ($S$). In Cram's model, the carbonyl oxygen is oriented *anti* to the Large group ($L$) to minimize steric clash. The nucleophile attacks from the side of the Small group ($S$).

#### 2. The Felkin-Anh Model (Hugh Felkin, 1968; Nguyen Trong Anh, 1976)
Anh performed frontier molecular orbital *ab initio* calculations and demonstrated that Cram's conformation is incorrect because it ignores orbital overlap and the Bürgi-Dunitz trajectory.

```
                  The Felkin-Anh Transition State:
                          O
                         //
                   H --- C             <==== Nucleophile Nu(-) attacks
                        / \                  along Bürgi-Dunitz 107° trajectory
                       C   \                 from face of Small group (S)
                      / \
                     M   S
                     |
                     L (Perpendicular to C=O to overlap with pi*)
```

The **Felkin-Anh transition state** is governed by three fundamental principles:
1. **Orbital Alignment**: The Large substituent ($L$) must be oriented **perpendicular ($90^\circ$) to the carbonyl plane**, parallel to the $\pi$ and $\pi^*$ orbitals. This allows the low-lying $\sigma^*$ orbital of the $\text{C}-L$ bond (especially if $L$ is electronegative, like $-\text{Cl}, -\text{OR}$) to overlap with the carbonyl $\pi^*$ LUMO, lowering the activation energy through $\sigma^*\text{–}\pi^*$ hyperconjugative stabilization.
2. **Bürgi-Dunitz Approach**: The nucleophile attacks at an angle of $\sim 107^\circ$ relative to the $\text{C}=\text{O}$ axis.
3. **Steric Minimization**: Between the two possible perpendicular conformations for $L$, the nucleophile attacks from the face containing the **Small substituent ($S$)** rather than the Medium substituent ($M$):
   $$\Delta \Delta G^\ddagger = \Delta G^\ddagger(M\text{-face}) - \Delta G^\ddagger(S\text{-face}) \approx 8\text{–}15\text{ kJ}\cdot\text{mol}^{-1} \tag{6.11}$$
   This predicts diastereomeric ratios exceeding $95:5$ in favor of the Felkin-Anh product.

#### 3. The Cram Chelate Model
When the $\alpha$-substituent contains a heteroatom capable of coordinating a Lewis acid metal cation (e.g., $-\text{OMe}, -\text{OBn}, -\text{SMe}$ with $\text{Mg}^{2+}, \text{Ti}^{4+}, \text{Zn}^{2+}$), the molecule adopts a rigid **five-membered bidentate chelate ring**:

$$\text{Transition State}: \quad [\text{C}_{\alpha}-\text{O} \cdots \text{M}^{n+} \cdots \text{O}=\text{C}_{\text{carbonyl}}] \tag{6.12}$$

This locks the conformation, forcing the nucleophile to attack from the side opposite the Medium/Large group, completely reversing the diastereoselectivity (**anti-Felkin / Chelation-Controlled product**).""",
                "simulations": []
            },
            {
                "id": "sec6_7",
                "secNumber": "§6.7",
                "title": "Chiral Auxiliaries: Evans Oxazolidinone Stereocontrol",
                "heading": "Chiral Auxiliaries: Evans Oxazolidinone Stereocontrol",
                "content": r"""A **chiral auxiliary** is an enantiomerically pure chiral molecule temporarily attached to an achiral substrate to direct the stereochemical outcome of a reaction, after which it is cleaved and recycled without loss of optical purity.

### David Evans' Oxazolidinones
Developed by David A. Evans at Harvard University in 1981, chiral oxazolidinones derived from natural amino acids (such as $(4S)\text{-benzyl-1,3-oxazolidin-2-one}$ from L-phenylalanine, and $(4R,5S)\text{-4-methyl-5-phenyl-2-oxazolidinone}$ from norephedrine) represent the premier methodology for asymmetric enolate alkylation and aldol additions.

```
Evans Oxazolidinone Asymmetric Alkylation Cascade:
1. Achiral Acyl Chloride + Chiral Oxazolidinone (Aux) ===> Chiral Imide
2. Deprotonation with Bu2BOTf / Et3N ===> Rigid Z-Enolate Boron Chelate
3. Electrophile R'-X approaches exclusively from unshielded face ===> >99% de
4. Mild Hydrolytic Cleavage (LiOH, H2O2) ===> Pure (S)-alpha-Alkyl Carboxylic Acid + Recycled Aux
```

### Mechanistic Principles of Evans Stereocontrol:
1. **Acylation**: The achiral acyl chloride ($\text{RCH}_2\text{COCl}$) is coupled to the deprotonated oxazolidinone to yield a chiral imide.
2. **Stereospecific Chelation to $(Z)$-Enolate**: Treatment of the imide with dibutylboron triflate ($\text{Bu}_2\text{BOTf}$) and triethylamine ($\text{Et}_3\text{N}$) forms a **rigid boron enolate**:
   - The boron atom coordinates bidentately to both the enolate oxygen and the oxazolidinone carbonyl oxygen, locking the molecule into a rigid planar $(Z)$-enolate conformation.
3. **Face-Selective Alkylation**: The bulky benzyl substituent at C4 of the oxazolidinone projects outward, sterically blocking the entire *bottom* face of the enolate.
4. **Electrophile Approach**: Incoming alkyl halides ($\text{R}'-\text{X}$) attack exclusively from the unhindered *top* face, delivering the $\alpha$-alkylated product with diastereomeric excess:
   $$\text{diastereomeric excess } (de) > 98\% \tag{6.13}$$
5. **Mild Cleavage**: Treatment with lithium hydroperoxide ($\text{LiOH} / \text{H}_2\text{O}_2$) cleaves the auxiliary selectively via nucleophilic attack of the peroxy anion ($\text{HOO}^-$) on the exocyclic carbonyl, yielding the enantiomerically pure **$\alpha$-chiral carboxylic acid** while recovering the oxazolidinone auxiliary in $>95\%$ yield for reuse.""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob6_1",
                "problemNumber": "6.1",
                "title": "Biot's Law & Enantiomeric Excess Calculation of Chiral 2-Butanol",
                "difficulty": "Intermediate",
                "statement": r"""A sample of synthetic 2-butanol ($1.850\text{ g}$) was dissolved in ethanol to prepare $25.00\text{ mL}$ of solution. The optical rotation was measured in a $2.00\text{ dm}$ polarimeter sample tube at $20^\circ\text{C}$ using the sodium D line, giving an observed rotation of $\alpha = +1.68^\circ$. The specific rotation of pure, optically pure $(S)\text{-(+)-2-butanol}$ under identical conditions is $[\alpha]_D^{20} = +13.50^\circ$.
(a) Calculate the specific rotation $[\alpha]_D^{20}$ of the synthetic sample.
(b) Calculate the enantiomeric excess ($ee$) and the optical purity of the sample.
(c) Determine the percentage composition of the $(S)$ and $(R)$ enantiomers in the mixture.""",
                "hints": ["Use $[\alpha] = \alpha / (l \cdot c)$.", "Concentration $c$ must be in $\text{g/mL}$."],
                "solution": r"""### (a) Specific Rotation Calculation
1. **Concentration of solution ($c$)**:
   $$c = \frac{1.850\text{ g}}{25.00\text{ mL}} = 0.0740\text{ g/mL}$$
2. **Specific rotation ($[\alpha]_D^{20}$)**:
   $$[\alpha]_D^{20} = \frac{\alpha}{l \cdot c} = \frac{+1.68^\circ}{(2.00\text{ dm}) \times (0.0740\text{ g/mL})} = \frac{+1.68}{0.148} = +11.35^\circ$$

### (b) Enantiomeric Excess ($ee$)
$$\text{Optical Purity} = \frac{[\alpha]_{\text{sample}}}{[\alpha]_{\text{pure}}} \times 100\% = \frac{+11.35^\circ}{+13.50^\circ} \times 100\% \approx 84.07\%$$
Because optical purity is experimentally identical to enantiomeric excess ($ee$):
$$ee = 84.1\%$$
The $(S)$ enantiomer is in excess since the sign of rotation is positive ($+$).

### (c) Enantiomer Percentage Composition
Let $x$ be the fraction of $(S)$ and $y$ be the fraction of $(R)$:
$$x - y = 0.8407$$
$$x + y = 1.0000$$
Adding the two equations:
$$2x = 1.8407 \implies x = 0.92035 \approx 92.0\%$$
$$y = 1.0000 - 0.9204 = 0.0796 \approx 8.0\%$$
- **(S)-2-butanol**: **$92.0\%$**
- **(R)-2-butanol**: **$8.0\%$**
(Racemic portion = $16.0\%$, enantiomeric excess = $84.0\%$)."""
            },
            {
                "id": "prob6_2",
                "problemNumber": "6.2",
                "title": "Rotational Barrier & Atropisomerism in Ortho-Substituted Biphenyls",
                "difficulty": "Mastery",
                "statement": r"""Consider 6,6'-dinitrobiphenyl-2,2'-dicarboxylic acid.
(a) Draw the two non-superimposable atropisomeric enantiomers and state their molecular point group.
(b) The activation energy for thermal racemization of this compound in ethanol at $25^\circ\text{C}$ is $\Delta G^\ddagger = 108.5\text{ kJ}\cdot\text{mol}^{-1}$. Compute the rate constant of racemization $k_{\text{rac}}$ and the half-life $t_{1/2}$ of optical activity.
(c) Predict whether 2,2'-difluorobiphenyl can be resolved into stable atropisomers at room temperature, justifying based on the van der Waals radii of fluorine vs the nitro and carboxyl groups.""",
                "hints": ["Use the Eyring equation: $k = (k_B T / h) \exp(-\Delta G^\ddagger / RT)$.", "$t_{1/2} = \ln 2 / (2 k)$ for racemization."],
                "solution": r"""### (a) Atropisomeric Enantiomers & Point Group
The two phenyl rings are held perpendicular to each other ($\theta \approx 90^\circ$ dihedral angle) to avoid steric collision between the bulky ortho substituents ($-\text{NO}_2$ and $-\text{COOH}$).
- Ring 1 carries $-\text{NO}_2$ at C6 and $-\text{COOH}$ at C2.
- Ring 2 carries $-\text{NO}_2$ at C6' and $-\text{COOH}$ at C2'.
Because the molecule possesses a $C_2$ proper rotation axis perpendicular to the central biphenyl bond but lacks any plane of symmetry ($\sigma$) or inversion center ($i$), it belongs to the **chiral point group $C_2$**.
The two non-superimposable mirror images represent stable **$(aR)$ and $(aS)$ atropisomers**.

### (b) Racemization Kinetics and Half-Life
Using the Eyring equation at $T = 298.15\text{ K}$:
$$k = \frac{k_B T}{h} \exp\left(-\frac{\Delta G^\ddagger}{RT}\right)$$
Constants:
$$\frac{k_B T}{h} = 6.212 \times 10^{12}\text{ s}^{-1}$$
$$RT = (8.314) \times (298.15) = 2478.8\text{ J}\cdot\text{mol}^{-1} = 2.4788\text{ kJ}\cdot\text{mol}^{-1}$$
$$\frac{\Delta G^\ddagger}{RT} = \frac{108.5}{2.4788} = 43.77$$
$$\exp(-43.77) = 9.816 \times 10^{-20}$$
$$k_{\text{inv}} = (6.212 \times 10^{12}) \times (9.816 \times 10^{-20}) \approx 6.10 \times 10^{-7}\text{ s}^{-1}$$
For racemization ($R \rightleftharpoons S$), $k_{\text{rac}} = 2 k_{\text{inv}} = 1.22 \times 10^{-6}\text{ s}^{-1}$.
The half-life for loss of optical activity is:
$$t_{1/2} = \frac{\ln 2}{k_{\text{rac}}} = \frac{0.69315}{1.22 \times 10^{-6}\text{ s}^{-1}} \approx 5.68 \times 10^5\text{ seconds} \approx 6.57\text{ days}$$
The enantiomers are stable enough to be stored in the dark at room temperature for days, and indefinitely in a freezer (where $t_{1/2} > 100\text{ years}$).

### (c) 2,2'-Difluorobiphenyl Comparison
Fluorine has an extraordinarily small van der Waals radius ($r_{\text{vdW}}(\text{F}) = 1.47\text{ \AA}$), only slightly larger than hydrogen ($1.20\text{ \AA}$).
In contrast, the effective radii of the substituents in 6,6'-dinitrobiphenyl-2,2'-dicarboxylic acid are:
$$r_{\text{eff}}(-\text{NO}_2) \approx 2.4\text{ \AA}, \quad r_{\text{eff}}(-\text{COOH}) \approx 2.4\text{ \AA}$$
In 2,2'-difluorobiphenyl, the two small fluorine atoms can easily slide past each other and past ortho-hydrogens in the planar transition state. The rotational barrier is only $\Delta G^\ddagger \approx 35\text{–}40\text{ kJ}\cdot\text{mol}^{-1}$, resulting in an inversion frequency of millions of times per second. **2,2'-Difluorobiphenyl cannot be resolved at room temperature**."""
            },
            {
                "id": "prob6_3",
                "problemNumber": "6.3",
                "title": "Diastereoselective Addition: Felkin-Anh vs Chelation-Controlled Models",
                "difficulty": "Mastery",
                "statement": r"""Predict the major diastereomeric product when (R)-2-phenylpropanal is reacted with methylmagnesium bromide under two different experimental conditions:
- Condition 1: Methylmagnesium bromide in anhydrous diethyl ether at $-78^\circ\text{C}$ (Felkin-Anh control).
- Condition 2: Methylmagnesium bromide in the presence of 1.0 equivalent of anhydrous titanium tetrachloride ($\text{TiCl}_4$) or magnesium bromide ($\text{MgBr}_2$) in dichloromethane at $-78^\circ\text{C}$ (Chelation control).
(a) Draw the Felkin-Anh Newman projection for Condition 1 and identify the major diastereomer ($(2R,3R)$ vs $(2R,3S)$).
(b) Draw the rigid chelate transition state for Condition 2 and identify the resulting product.
(c) Explain why $\text{TiCl}_4$ reverses the diastereoselectivity.""",
                "hints": ["In (R)-2-phenylpropanal, the alpha-substituents are Phenyl (Large), Methyl (Medium), and Hydrogen (Small).", "Chelation requires a Lewis-basic heteroatom; examine if chelation is possible without a heteroatom."],
                "solution": r"""### (a) Condition 1: Felkin-Anh Addition Model
Substituents on the $\alpha$-chiral carbon (C2) of (R)-2-phenylpropanal:
- **Large ($L$)**: Phenyl ring ($-\text{Ph}$)
- **Medium ($M$)**: Methyl group ($-\text{Me}$)
- **Small ($S$)**: Hydrogen atom ($-\text{H}$)

#### Felkin-Anh Conformation:
1. The Large group ($-\text{Ph}$) aligns perpendicular ($90^\circ$) to the carbonyl double bond ($\text{C}=\text{O}$) to maximize $\sigma^*_{\text{C-Ph}}\text{–}\pi^*_{\text{C=O}}$ hyperconjugative stabilization.
2. The carbonyl oxygen is oriented toward the Medium group ($-\text{Me}$).
3. The nucleophile ($\text{Me}^-$ from $\text{MeMgBr}$) approaches along the Bürgi-Dunitz trajectory ($107^\circ$) from the side of the **Small substituent ($-\text{H}$)** to minimize steric clash.
4. Attack on the *si*-face creates a new stereocenter at C1. Assigning CIP priorities to the resulting (2R,3R)- vs (2R,3S)-3-phenylbutan-2-ol:
   The major product is **(2S,3R)-3-phenylbutan-2-ol** (Cram/Felkin-Anh diastereomer, $>90:10$ ratio).

### (b) & (c) Chelation Control Analysis with Heteroatom Substrates
- In (R)-2-phenylpropanal, there is **no $\alpha$-heteroatom** (only carbon and hydrogen). The phenyl ring cannot act as a strong bidentate Lewis base to form a rigid chelate with $\text{Mg}^{2+}$ or $\text{Ti}^{4+}$. Therefore, Condition 1 operates purely under Felkin-Anh open-chain control.
- If the substrate were an $\alpha$-alkoxy aldehyde, such as **(R)-2-methoxy-2-phenylacetaldehyde**:
  1. The bidentate Lewis acid ($\text{TiCl}_4$ or $\text{MgBr}_2$) coordinates simultaneously to the carbonyl oxygen and the $\alpha$-methoxy oxygen ($-\text{OMe}$), forming a rigid **five-membered chelate ring**.
  2. The Large phenyl group is locked on one face of the ring.
  3. The nucleophile is forced to attack from the opposite face (**anti-Felkin product**), reversing the diastereomeric ratio from $15:85$ to $>98:2$."""
            },
            {
                "id": "prob6_4",
                "problemNumber": "6.4",
                "title": "Axial Chirality Stereodescriptor Assignment in Allenes & BINAP",
                "difficulty": "Intermediate",
                "statement": r"""Apply the Cahn-Ingold-Prelog (CIP) sequence rules for axially chiral molecules to assign the absolute configuration ($aR$ vs $aS$ or $R_a$ vs $S_a$) to:
(a) Penta-2,3-diene: with $(H, CH_3)$ on the front vertical carbon and $(H, CH_3)$ on the rear horizontal carbon, where the front top group is $CH_3$ and the rear right group is $CH_3$.
(b) (R)-BINAP (2,2'-bis(diphenylphosphino)-1,1'-binaphthyl).
Detail the viewing axis, prioritization rules (near groups precede far groups), and the path from priority 1 to 2 to 3.""",
                "hints": ["In axial CIP rules, substituents closer to the observer take precedence over distant substituents.", "Trace path $1 \to 2 \to 3$: clockwise is $aR$, counterclockwise is $aS$."],
                "solution": r"""### (a) Penta-2,3-diene Configuration
1. **Viewing Axis**: View down the $\text{C2}=\text{C3}=\text{C4}$ allene axis from front (C2) to back (C4).
2. **Prioritization Rules**:
   - Near substituents (on C2) have priority over far substituents (on C4), regardless of atomic number!
   - On C2 (front): $-\text{CH}_3$ (priority 1) > $-\text{H}$ (priority 2).
   - On C4 (rear): $-\text{CH}_3$ (priority 3) > $-\text{H}$ (priority 4).
3. **Trace Path**:
   - Priority 1 is at Front-Top ($12\text{ o'clock}$).
   - Priority 2 is at Front-Bottom ($6\text{ o'clock}$).
   - Priority 3 is at Rear-Right ($3\text{ o'clock}$).
   Following the path $1 \to 2 \to 3$: From 12 o'clock down to 6 o'clock, then turning to 3 o'clock is a **counterclockwise** turn.
   Therefore, the absolute configuration is **$aS$** (or **$S_a$**).

### (b) BINAP (2,2'-bis(diphenylphosphino)-1,1'-binaphthyl)
1. **Viewing Axis**: View along the central $\text{C1}-\text{C1}'$ naphthyl-naphthyl pivot bond.
2. **Prioritization Rules**:
   - On the front naphthalene ring: The diphenylphosphino group ($-\text{PPh}_2$, phosphorus atom, $Z = 15$) takes priority over the aromatic carbon C8a ($Z = 6$):
     $$\text{Front Ring}: \quad -\text{PPh}_2 \text{ (Priority 1)}, \quad \text{C8a (Priority 2)}$$
   - On the rear naphthalene ring:
     $$\text{Rear Ring}: \quad -\text{PPh}_2 \text{ (Priority 3)}, \quad \text{C8a' (Priority 4)}$$
3. **Path Trace**:
   In the $(aR)$-enantiomer of BINAP:
   Tracing from priority 1 ($-\text{PPh}_2$ front) to priority 2 (front ring carbon) to priority 3 ($-\text{PPh}_2$ rear) describes a **clockwise** progression.
   Thus, the descriptor is **$(aR)\text{-BINAP}$** (commonly designated **$(R)\text{-BINAP}$**)."""
            },
            {
                "id": "prob6_5",
                "problemNumber": "6.5",
                "title": "Evans Chiral Auxiliary Asymmetric Alkylation Mechanism",
                "difficulty": "Mastery",
                "statement": r"""A chemist requires enantiomerically pure (S)-2-methylpentanoic acid with $>98\%$ enantiomeric excess.
(a) Outline the complete five-step synthetic sequence using (4S)-4-benzyl-1,3-oxazolidin-2-one (Evans auxiliary).
(b) Draw the rigid boron enolate intermediate formed upon treatment of the propionyloxazolidinone with $\text{Bu}_2\text{BOTf}$ and triethylamine, indicating the coordination geometry around boron.
(c) Explain which face of the enolate is attacked by 1-iodopropane and how the Evans auxiliary is cleaved without racemization.""",
                "hints": ["Boron forms a rigid bidentate 6-membered chelate.", "Lithium hydroperoxide (LiOOH) cleaves the imide chemoselectively."],
                "solution": r"""### (a) Synthetic Sequence
$$\begin{aligned}
\text{Step 1}: &\quad (4S)\text{-4-benzyloxazolidin-2-one} + \text{EtCOCl} \xrightarrow{n\text{-BuLi, THF, }-78^\circ\text{C}} \text{Chiral } N\text{-propionyloxazolidinone} \\
\text{Step 2}: &\quad N\text{-propionyloxazolidinone} \xrightarrow{\text{Bu}_2\text{BOTf, Et}_3\text{N, DCM, }0^\circ\text{C}} \text{Rigid boron }(Z)\text{-enolate} \\
\text{Step 3}: &\quad \text{Boron enolate} + \text{CH}_3\text{CH}_2\text{CH}_2\text{I (1-iodopropane)} \xrightarrow{-78^\circ\text{C to }0^\circ\text{C}} (4S)\text{-4-benzyl-3-[(2S)-2-methylpentanoyl]oxazolidin-2-one} \\
\text{Step 4}: &\quad \text{Alkylated imide} \xrightarrow{\text{LiOH, }30\%\,\text{H}_2\text{O}_2\text{, THF/H}_2\text{O, }0^\circ\text{C}} (S)\text{-2-methylpentanoic acid} + (4S)\text{-auxiliary} \\
\text{Step 5}: &\quad \text{Separate pure (S)-acid by extraction; recrystallize and recycle auxiliary }(>95\% \text{ recovery}).
\end{aligned}$$

### (b) Boron Enolate Chelate Structure
Treatment with $\text{Bu}_2\text{BOTf}$ and $\text{Et}_3\text{N}$ selectively generates the **$(Z)$-enolate**:
- The boron atom adopts tetrahedral geometry, coordinated bidentately to the enolate oxygen and the exocyclic oxazolidinone carbonyl oxygen.
- This creates a rigid planar **six-membered chelate ring**:
  $$[\text{B}(\text{Bu})_2 \cdots \text{O}=\text{C}_{\text{oxaz}} \cdots \text{N}-\text{C}(\text{O}^-)=\text{CHCH}_3]$$
- Dipole-dipole repulsion between the two carbonyls is minimized, locking the enolate in a single conformation.

### (c) Face Selectivity and Cleavage
1. **Diastereoselective Attack**:
   The $(4S)$-benzyl substituent projects into the lower hemisphere (*si*-face), sterically blocking approach of electrophiles from the bottom. The 1-iodopropane electrophile approaches exclusively from the unhindered upper hemisphere (*re*-face), establishing the $(2S)$ absolute configuration with $>98\%$ diastereomeric excess ($de$).
2. **Chemoselective Hydrolysis**:
   Treatment with lithium hydroperoxide ($\text{LiOOH}$, generated *in situ* from $\text{LiOH}$ and $\text{H}_2\text{O}_2$) exploits the enhanced nucleophilicity of the hydroperoxide anion ($\text{HOO}^-$) via the **$\alpha$-effect**. The peroxy anion attacks exclusively at the exocyclic acyl carbonyl rather than the endocyclic carbamate carbonyl. Subsequent protonation yields the peroxy acid, which is rapidly reduced to **(S)-2-methylpentanoic acid** without touching the newly formed stereocenter, guaranteeing **$>99\%$ optical purity**."""
            },
            {
                "id": "prob6_6",
                "problemNumber": "6.6",
                "title": "Resolution Thermodynamics: Enantiomeric Salt Solubility Ratios",
                "difficulty": "Mastery",
                "statement": r"""A chemist resolves racemic 2-chloropropanoic acid ($(\pm)\text{-A}$, $10.85\text{ g}$, $0.100\text{ mol}$) using optically pure (R)-1-phenylethylamine ($(+)\text{-B}$, $12.12\text{ g}$, $0.100\text{ mol}$) in $100.0\text{ mL}$ of boiling ethanol.
The solubilities of the two diastereomeric salts at $20^\circ\text{C}$ are:
- $S[(+)\text{-A}\cdot(+)\text{-B}] = 1.20\text{ g / 100 mL}$
- $S[(-)\text{-A}\cdot(+)\text{-B}] = 8.50\text{ g / 100 mL}$
(Molar mass of salt $= 229.7\text{ g/mol}$).
(a) Calculate the theoretical mass of $[(+)\text{-A}\cdot(+)\text{-B}]$ salt that crystallizes upon cooling to $20^\circ\text{C}$.
(b) Calculate the mass of $[(-)\text{-A}\cdot(+)\text{-B}]$ salt that co-crystallizes, and determine the diastereomeric excess ($de$) of the first crop of crystals.
(c) How many recrystallizations are required to obtain $[(+)\text{-A}\cdot(+)\text{-B}]$ with $de > 99.5\%$?""",
                "hints": ["Total initial moles of each diastereomeric salt = 0.050 mol.", "Mass of salt crystallized = Initial mass - Mass remaining dissolved at 20 °C."],
                "solution": r"""### (a) Mass of Pure $[(+)\text{-A}\cdot(+)\text{-B}]$ Crystallized
1. **Initial mass of each salt**:
   $$n = \frac{0.100\text{ mol}}{2} = 0.050\text{ mol}$$
   $$\text{Mass}_{\text{initial}} = 0.050\text{ mol} \times 229.7\text{ g/mol} = 11.485\text{ g of each salt}$$
2. **Mass remaining in solution at $20^\circ\text{C}$**:
   In $100\text{ mL}$ of ethanol:
   $$m_{\text{dissolved}}[(+)\text{-A}\cdot(+)\text{-B}] = 1.20\text{ g}$$
3. **Mass of $[(+)\text{-A}\cdot(+)\text{-B}]$ crystallized**:
   $$m_{\text{cryst}}[(+)\text{-A}\cdot(+)\text{-B}] = 11.485 - 1.20 = 10.285\text{ g}$$

### (b) Co-crystallization and Diastereomeric Excess ($de$)
1. **Mass of $[(-)\text{-A}\cdot(+)\text{-B}]$ remaining in solution**:
   $$m_{\text{dissolved}}[(-)\text{-A}\cdot(+)\text{-B}] = 8.50\text{ g}$$
2. **Mass of $[(-)\text{-A}\cdot(+)\text{-B}]$ co-crystallized**:
   $$m_{\text{cryst}}[(-)\text{-A}\cdot(+)\text{-B}] = 11.485 - 8.50 = 2.985\text{ g}$$
3. **Total mass of first crystal crop**:
   $$M_{\text{total}} = 10.285 + 2.985 = 13.27\text{ g}$$
4. **Diastereomeric excess ($de$)**:
   $$de = \frac{10.285 - 2.985}{10.285 + 2.985} \times 100\% = \frac{7.300}{13.27} \times 100\% \approx 55.0\%$$

### (c) Number of Recrystallizations Required
In the second recrystallization:
The $13.27\text{ g}$ of crystals contains $10.285\text{ g}$ of $(+)$ salt and $2.985\text{ g}$ of $(-)$ salt.
Dissolving in $50\text{ mL}$ of boiling ethanol and cooling to $20^\circ\text{C}$:
- Solubility of $(-)$ salt in $50\text{ mL} = 0.5 \times 8.50 = 4.25\text{ g}$.
Because $2.985\text{ g} < 4.25\text{ g}$, the entire $(-)\text{-A}\cdot(+)\text{-B}$ salt remains **completely dissolved** in the mother liquor!
- Mass of $(+)$ salt crystallized $= 10.285 - (0.5 \times 1.20) = 10.285 - 0.60 = 9.685\text{ g}$.
- Diastereomeric excess of the second crop:
  $$de = \frac{9.685 - 0}{9.685 + 0} \times 100\% = \mathbf{100.0\%} > 99.5\%$$
**Exactly two crystallization steps** (one initial resolution + one recrystallization) yield the salt in $>99.5\%$ diastereomeric purity."""
            },
            {
                "id": "prob6_7",
                "problemNumber": "6.7",
                "title": "Chirality in Planar and Helical Systems: *trans*-Cyclooctene and [6]Helicene",
                "difficulty": "Mastery",
                "statement": r"""(a) Explain why cis-cyclooctene is achiral and exists as a flexible conformer, whereas trans-cyclooctene is dissymmetric and exhibits stable planar chirality at room temperature.
(b) Detail the racemization mechanism of trans-cyclooctene and state why its barrier is exceptionally high ($\Delta G^\ddagger \approx 149\text{ kJ}\cdot\text{mol}^{-1}$).
(c) Account for the enormous optical rotation of [6]helicene ($[\alpha]_D = +3700^\circ$) based on helical electron delocalization.""",
                "hints": ["Look at the polymethylene chain looping across the double bond.", "Racemization of trans-cyclooctene requires swinging the chain through the ring."],
                "solution": r"""### (a) Planar Chirality in *trans*-Cyclooctene
- ***cis*-Cyclooctene**: The double bond has *cis* geometry. The eight-membered ring can adopt a boat-chair conformation with an internal plane of symmetry ($\sigma$). Interconversion of conformers occurs with an activation barrier $<35\text{ kJ}\cdot\text{mol}^{-1}$, rendering it achiral and optically inactive.
- ***trans*-Cyclooctene**: In *trans*-cyclooctene, the two vinyl hydrogens point in opposite directions across the double bond. To close the eight-membered ring, the polymethylene chain ($-\text{CH}_2\text{CH}_2\text{CH}_2\text{CH}_2-$) must loop **over one face** of the double bond. This loop breaks all symmetry elements ($\sigma, i, S_n$), giving the molecule chiral $C_2$ symmetry. The two non-superimposable enantiomers are designated $(p R)$ and $(p S)$.

### (b) Racemization Mechanism and Barrier of *trans*-Cyclooctene
To interconvert the $(p R)$ and $(p S)$ enantiomers:
1. The polymethylene chain must rotate around the double bond, passing the $-\text{CH}_2-$ units **through the center of the ring**.
2. This motion forces the trans double bond into extreme, planar torsional strain while compressing the internal methylene hydrogens within the van der Waals radii of the vinyl hydrogens.
3. The activation barrier is:
   $$\Delta G^\ddagger_{\text{racemization}} \approx 149\text{ kJ}\cdot\text{mol}^{-1} \quad (35.6\text{ kcal}\cdot\text{mol}^{-1})$$
4. At $25^\circ\text{C}$, this barrier corresponds to a racemization half-life of **millions of years** ($t_{1/2} > 10^7\text{ years}$), making *trans*-cyclooctene one of the most conformationally robust planar chiral hydrocarbons known.

### (c) Extraordinary Specific Rotation of [6]Helicene
Hexahelicene possesses an immense specific rotation of $[\alpha]_D = +3700^\circ$ ($[\Phi]_D \approx 12,000^\circ$).
This massive chiroptical response originates from:
1. **Helical Conjugation**: The six fused benzene rings form a continuous, non-planar chiral spiral. The $26\pi$ electron system is delocalized along a helical solenoid.
2. **Circular Birefringence & Cotton Effect**: When circular polarized light propagates along the helical axis, the transition electric dipole moment ($\boldsymbol{\mu}$) and transition magnetic dipole moment ($\mathbf{m}$) for the $\pi \to \pi^*$ electronic transition are parallel:
   $$\text{Rotational Strength } R_{0a} = \text{Im} \langle \psi_0 | \boldsymbol{\mu} | \psi_a \rangle \cdot \langle \psi_a | \mathbf{m} | \psi_0 \rangle \gg 0$$
   Because both moments are oriented along the helix axis with large scalar product, the rotational strength is hundreds of times larger than that of a conventional molecule with localized chiral centers, generating colossal optical rotation."""
            }
        ]
    }
