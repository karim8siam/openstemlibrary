# -*- coding: utf-8 -*-
"""
build_org2_units_1_2_3.py
Rigorous honors-level curriculum generator for Units 1, 2, and 3 of Organic Chemistry II.
Strict zero course numbers or marks.
Contains massive depth, comprehensive KaTeX proofs, thermodynamic parameters, reaction tables,
and 7-8 multi-tier solved problems per unit with step-by-step solutions.
"""

def get_unit_1():
    return {
        "id": "unit1",
        "unitId": "unit1-org2",
        "number": 1,
        "unitNumber": 1,
        "title": "Unit 1: Polynuclear Aromatic Hydrocarbons: Clar Sextet Dynamics, Electrophilic Substitution & Carcinogenesis",
        "description": "Exhaustive physical organic analysis of polynuclear benzenoid aromatic hydrocarbons: naphthalene, anthracene, and phenanthrene. Haworth total syntheses, Clar's aromatic sextet rule, resonance energies and localized bond orders, electrophilic aromatic substitution regiochemistry (alpha vs beta positions in naphthalene; C9 and C10 reactivity in anthracene and phenanthrene), oxidation and reduction cascades, and the metabolic diol epoxide activation pathway of carcinogenic polycyclic aromatics.",
        "leadSummary": "Comprehensive physical organic treatise on condensed and angular polynuclear aromatics: Haworth annulation pathways, Clar sextet resonance topology, electrophilic substitution regiocontrol, frontier orbital localization energies, and metabolic chemical carcinogenesis.",
        "simulations": ["sim_chem_polyaromatic_clar_sextet"],
        "sections": [
            {
                "id": "sec1_1",
                "secNumber": "§1.1",
                "title": "Classification, Nomenclature & Electronic Architecture of Fused Benzenoids",
                "heading": "Classification, Nomenclature & Electronic Architecture of Fused Benzenoids",
                "content": r"""Polynuclear aromatic hydrocarbons (PAHs), also designated polycyclic benzenoid hydrocarbons, comprise planar conjugated networks of fused benzene rings sharing adjacent pairs of $sp^2$-hybridized carbon atoms. They represent a fundamental thermodynamic and quantum frontier between isolated monocyclic aromatics like benzene ($\text{C}_6\text{H}_6$) and infinite two-dimensional graphene sheets.

### Topology and IUPAC Positional Numbering

The geometric fusion of benzene rings generates two principal architectural classes:
1. **Linear Acenes**: Linearly fused networks characterized by the general molecular formula $\text{C}_{4n+2}\text{H}_{2n+4}$. Examples include naphthalene ($n=2$, $\text{C}_{10}\text{H}_8$), anthracene ($n=3$, $\text{C}_{14}\text{H}_{10}$), tetracene ($n=4$, $\text{C}_{18}\text{H}_{12}$), and pentacene ($n=5$, $\text{C}_{22}\text{H}_{14}$).
2. **Angular Phenes**: Angled or bent configurations such as phenanthrene ($\text{C}_{14}\text{H}_{10}$), chrysene ($\text{C}_{18}\text{H}_{12}$), and picene ($\text{C}_{22}\text{H}_{14}$). Due to nonlinear topological topology, angular phenes exhibit substantially higher thermodynamic stability and greater resonance stabilization energy than their linear constitutional acene isomers.

```
       Linear Fusion (Acene)                  Angular Fusion (Phene)
        +---+---+---+                           +---+---+
        |   |   |   |                           |   |   |
        +---+---+---+                           +---+---+
         Anthracene (C14H10)                       \   |
                                                    +---+
                                                Phenanthrene (C14H10)
```

The IUPAC positional numbering rules for fused polycyclic systems require orienting the molecule along horizontal and vertical axes such that:
- The maximum number of rings lies along a horizontal row.
- Any remaining rings are positioned in the upper right quadrant.
- Numbering commences at the uppermost, rightmost ring carbon not involved in ring fusion and proceeds clockwise around the outer periphery.
- Ring-junction bridgehead carbons are not assigned separate primary integers; rather, they receive suffixed numbers designating the preceding peripheral position (e.g., $4a, 8a, 10a$).

In **naphthalene** ($\text{C}_{10}\text{H}_8$), the eight peripheral positions resolve into two chemically distinct sets:
- **$\alpha$-Positions (C1, C4, C5, C8)**: Carbons directly adjacent to bridgehead atoms $4a$ and $8a$.
- **$\beta$-Positions (C2, C3, C6, C7)**: Carbons separated by one bond from bridgehead atoms.

In **anthracene** ($\text{C}_{14}\text{H}_{10}$), three sets of constitutionally non-equivalent positions exist:
- $\alpha$-positions: C1, C4, C5, C8.
- $\beta$-positions: C2, C3, C6, C7.
- **meso-positions**: C9 and C10 (the central ring bridgehead adjacent carbons).

In **phenanthrene** ($\text{C}_{14}\text{H}_{10}$), five sets of non-equivalent carbons emerge: C1/C8, C2/C7, C3/C6, C4/C5 (the severe steric "bay region"), and **C9/C10** (the olefinic K-region).

### Resonance Energy and Clar's Aromatic Sextet Theory

In simple valence bond theory, Kekulé resonance structures are assigned equal weight. Naphthalene possesses 3 Kekulé structures, anthracene possesses 4, and phenanthrene possesses 5. However, Pauling resonance energies (RE) per $\pi$-electron reveal a dramatic attenuation of aromatic character per ring as molecular size increases:

$$\begin{aligned}
\text{Benzene}: &\quad \text{RE} = 152\text{ kJ}\cdot\text{mol}^{-1} \quad (25.3\text{ kJ}\cdot\text{mol}^{-1}\text{ per }\pi\text{ electron}) \\
\text{Naphthalene}: &\quad \text{RE} = 255\text{ kJ}\cdot\text{mol}^{-1} \quad (25.5\text{ kJ}\cdot\text{mol}^{-1}\text{ per }\pi\text{ electron}) \\
\text{Anthracene}: &\quad \text{RE} = 351\text{ kJ}\cdot\text{mol}^{-1} \quad (25.1\text{ kJ}\cdot\text{mol}^{-1}\text{ per }\pi\text{ electron}) \\
\text{Phenanthrene}: &\quad \text{RE} = 381\text{ kJ}\cdot\text{mol}^{-1} \quad (27.2\text{ kJ}\cdot\text{mol}^{-1}\text{ per }\pi\text{ electron})
\end{aligned}$$

Notice that phenanthrene is more stable than its constitutional isomer anthracene by $\Delta H^\circ_{\text{isomerization}} \approx 30\text{ kJ}\cdot\text{mol}^{-1}$ ($7.2\text{ kcal}\cdot\text{mol}^{-1}$). This pronounced thermodynamic gap is elegantly rationalized by **Erich Clar's aromatic sextet theory** (1972).

Clar postulated that the $\pi$-electron distribution of benzenoid hydrocarbons is best represented by drawing the maximum number of isolated, mutually disjoint **aromatic sextets** (represented as inscribed circles inside rings) connected by localized formal double bonds:
- **Benzene**: 1 Clar sextet ($6\pi$ electrons). Fully benzenoid.
- **Naphthalene**: Only 1 Clar sextet can be drawn simultaneously with one localized butadiene-like ring ($6\pi + 4\pi$). The sextet resonates between the two rings, yielding a "migrating" sextet.
- **Anthracene**: Only 1 Clar sextet can be drawn at any one time, leaving two rings with localized diene/olefin character ($6\pi + 8\pi$).
- **Phenanthrene**: **2 independent Clar sextets** can be drawn simultaneously in the terminal outer rings, leaving the central C9-C10 bond as an essentially localized, isolated double bond ($2 \times 6\pi + 2\pi = 14\pi$).

Because phenanthrene accommodates two complete benzenoid sextets while anthracene can only accommodate one, phenanthrene retains far greater resonance stabilization, higher oxidation potentials, and significantly reduced chemical reactivity compared to anthracene.""",
                "simulations": ["sim_chem_polyaromatic_clar_sextet"]
            },
            {
                "id": "sec1_2",
                "secNumber": "§1.2",
                "title": "Bond Length Alternation, Localized Bond Orders & Molecular Orbital Profiles",
                "heading": "Bond Length Alternation, Localized Bond Orders & Molecular Orbital Profiles",
                "content": r"""Unlike benzene, in which rigorous $D_{6h}$ hexagonal symmetry enforces exact equivalence among all six carbon-carbon bond distances ($1.399\text{ \AA}$), polynuclear aromatics exhibit pronounced **bond length alternation** reflecting heterogeneous Coulson $\pi$-bond orders ($p_{rs}$).

### Coulson $\pi$-Bond Orders and Hückel Molecular Orbital (HMO) Analysis

In Hückel molecular orbital theory, the total bond order $P_{rs}$ between adjacent carbons $r$ and $s$ is the sum of the invariant single $\sigma$-bond order and the mobile $\pi$-bond order $p_{rs}$:

$$P_{rs} = 1.0 + p_{rs} = 1.0 + \sum_{j=1}^{N_{\text{occ}}} n_j \, c_{jr} \, c_{js} \tag{1.1}$$

where $n_j$ is the occupancy of molecular orbital $\psi_j$ ($n_j = 2$ for closed-shell ground states) and $c_{jr}, c_{js}$ are the linear combination of atomic orbital (LCAO) coefficients at carbon centers $r$ and $s$.

Using the Coulson empirical bond length formula:

$$R_{rs} = R_{\text{single}} - \frac{R_{\text{single}} - R_{\text{double}}}{1 + \kappa \left(\frac{1 - p_{rs}}{p_{rs}}\right)} \tag{1.2}$$

where $R_{\text{single}} \approx 1.54\text{ \AA}$, $R_{\text{double}} \approx 1.33\text{ \AA}$, and $\kappa \approx 1.05$.

#### Naphthalene Bond Geometries
X-ray crystallographic and electron diffraction measurements on naphthalene reveal dramatic structural differences between bond positions:
- **C1-C2 bond**: Coulson $\pi$-bond order $p_{12} = 0.725 \implies R_{12} = 1.365\text{ \AA}$ (exhibits pronounced double-bond character).
- **C2-C3 bond**: Coulson $\pi$-bond order $p_{23} = 0.603 \implies R_{23} = 1.404\text{ \AA}$.
- **C9-C1 bond**: Coulson $\pi$-bond order $p_{91} = 0.554 \implies R_{91} = 1.425\text{ \AA}$.
- **C9-C10 central bridgehead bond**: Coulson $\pi$-bond order $p_{9,10} = 0.518 \implies R_{9,10} = 1.428\text{ \AA}$ (substantially elongated single-like bond).

#### Anthracene and Phenanthrene Contrasts
In **anthracene**:
- The C9-C10 meso carbons feature localized $p_z$ frontier orbital densities. The C1-C2 bond measures $1.368\text{ \AA}$, whereas C9-C1 measures $1.401\text{ \AA}$.
- The HOMO-LUMO gap is remarkably narrow: $\Delta E = 0.83 \beta \approx 3.2\text{ eV}$, explaining anthracene's absorption in the near-UV ($\lambda_{\max} \approx 375\text{ nm}$) and bright blue fluorescence ($\lambda_{\text{fl}} \approx 402\text{ nm}$).

In **phenanthrene**:
- The **C9-C10 bond** has a Coulson $\pi$-bond order $p_{9,10} = 0.775$ and an interatomic distance of $R_{9,10} = 1.355\text{ \AA}$! This is extraordinarily close to an isolated aliphatic alkene double bond ($1.33\text{ \AA}$).
- Consequently, phenanthrene readily undergoes addition reactions across the C9-C10 double bond without disrupting the two adjacent fully intact benzenoid Clar sextets.""",
                "simulations": []
            },
            {
                "id": "sec1_3",
                "secNumber": "§1.3",
                "title": "Haworth Syntheses & Directed Annulation Protocols",
                "heading": "Haworth Syntheses & Directed Annulation Protocols",
                "content": r"""The classical and most versatile general laboratory construction of polynuclear aromatics is the **Haworth synthesis** (developed by Sir Robert Downs Haworth in 1932). The reaction sequence exploits Friedel-Crafts acylation of a suitable aromatic substrate with cyclic anhydrides, followed by regioselective reduction, intramolecular cyclization, and final dehydrogenation.

### Total Haworth Synthesis of Naphthalene
The synthesis starts from benzene ($\text{C}_6\text{H}_6$) and succinic anhydride:

$$\begin{aligned}
\text{Step 1 (Intermolecular Acylation)}: &\quad \text{Benzene} + \text{Succinic anhydride} \xrightarrow{\text{AlCl}_3, \text{PhNO}_2} \beta\text{-benzoylpropionic acid} \\
&\quad \text{C}_6\text{H}_6 + \text{C}_4\text{H}_4\text{O}_3 \longrightarrow \text{C}_6\text{H}_5\text{COCH}_2\text{CH}_2\text{COOH} \\
\text{Step 2 (Carbonyl Deoxygenation)}: &\quad \beta\text{-benzoylpropionic acid} \xrightarrow{\text{Zn(Hg)}, \text{HCl (Clemmensen)}} 4\text{-phenylbutanoic acid} \\
&\quad \text{PhCOCH}_2\text{CH}_2\text{COOH} \longrightarrow \text{PhCH}_2\text{CH}_2\text{CH}_2\text{COOH} \\
\text{Step 3 (Intramolecular Acylation)}: &\quad 4\text{-phenylbutanoic acid} \xrightarrow{\text{polyphosphoric acid (PPA) or HF, }\Delta} \alpha\text{-tetralone} \\
\text{Step 4 (Second Carbonyl Reduction)}: &\quad \alpha\text{-tetralone} \xrightarrow{\text{Zn(Hg)}, \text{HCl}} \text{Tetralin (1,2,3,4-tetrahydronaphthalene)} \\
\text{Step 5 (Aromatization / Dehydrogenation)}: &\quad \text{Tetralin} \xrightarrow{\text{Pd/C, }300^\circ\text{C or Se, }320^\circ\text{C or DDQ}} \text{Naphthalene} + 2\,\text{H}_2\uparrow
\end{aligned}$$

```
   Haworth Synthesis Flow:
   Benzene + Succinic Anhydride ---> beta-Benzoylpropionic Acid
       ---> (Clemmensen) 4-Phenylbutanoic Acid
       ---> (PPA) alpha-Tetralone
       ---> (Clemmensen) Tetralin
       ---> (Pd/C, 300 C) Naphthalene
```

### Haworth Construction of Anthracene and Phenanthrene
By modifying the starting materials, Haworth annulation provides stereospecific entry into three-ring systems:

1. **Anthracene Route**: Condensation of phthalic anhydride with benzene in the presence of $\text{AlCl}_3$ furnishes $o$-benzoylbenzoic acid. Ring closure with concentrated $\text{H}_2\text{SO}_4$ yields 9,10-anthraquinone. Reduction of the quinone with zinc dust in boiling alkaline $\text{NaOH}$ or with $\text{HI}$/red phosphorus affords pure anthracene.
2. **Phenanthrene Route**: Friedel-Crafts acylation of naphthalene with succinic anhydride and $\text{AlCl}_3$ in nitrobenzene affords a mixture of $\beta$-(1-naphthoyl)propionic acid and $\beta$-(2-naphthoyl)propionic acid. Separation of the 1-isomer followed by Clemmensen reduction, cyclization with anhydrous $\text{HF}$, secondary reduction, and selenium dehydrogenation delivers phenanthrene.

Alternatively, the **Pschorr phenanthrene synthesis** effects intramolecular radical/cationic cyclization of diazotized $\alpha$-phenyl-$o$-aminocinnamic acids in the presence of copper powder, furnishing phenanthrene-9-carboxylic acid, which undergoes thermal decarboxylation with copper chromite to yield phenanthrene.""",
                "simulations": []
            },
            {
                "id": "sec1_4",
                "secNumber": "§1.4",
                "title": "Electrophilic Aromatic Substitution: Wheland Intermediates & Kinetic vs Thermodynamic Control",
                "heading": "Electrophilic Aromatic Substitution: Wheland Intermediates & Kinetic vs Thermodynamic Control",
                "content": r"""Electrophilic aromatic substitution ($S_E\text{Ar}$) in polynuclear systems proceeds with dramatically higher rate constants than in benzene, but displays acute regiochemical sensitivity governed by the resonance stability of the cationic Wheland arenium intermediates.

### Naphthalene: $\alpha$ (C1) vs $\beta$ (C2) Regioselectivity

When an electrophile $E^+$ attacks naphthalene at either the C1 ($\alpha$) or C2 ($\beta$) position, a resonance-stabilized Wheland carbocation intermediate forms:

#### Attack at C1 ($\alpha$-Attack)
Electrophilic addition at C1 produces a cyclohexadienyl cation with **7 canonical resonance structures**. Crucially:
- **4 resonance contributors retain a fully intact, benzenoid Clar sextet** in the unattacked benzene ring without disrupting its aromaticity:

$$\begin{aligned}
\text{Structure 1}: &\quad [1\text{-}E, 1\text{-}\text{H}, 2\text{-carbocation}] \quad (\text{intact ring B benzenoid}) \\
\text{Structure 2}: &\quad [1\text{-}E, 1\text{-}\text{H}, 4\text{-carbocation}] \quad (\text{intact ring B benzenoid}) \\
\text{Structures 3, 4}: &\quad \text{mesomeric forms maintaining benzenoid sextet}
\end{aligned}$$
- 3 additional contributors delocalize the positive charge into the second ring, temporarily sacrificing the aromatic sextet.

#### Attack at C2 ($\beta$-Attack)
Electrophilic addition at C2 produces an arenium ion with **6 canonical resonance structures**. However:
- **Only 2 resonance contributors retain an intact benzenoid sextet** in the adjacent ring.
- In all other forms, the positive charge is delocalized across the bridgehead, disrupting aromaticity in both rings simultaneously.

Because the $\alpha$-arenium intermediate enjoys twice as many aromatic-sextet-preserving resonance structures, its Gibbs activation energy is significantly lower:

$$\Delta G^\ddagger(\alpha) < \Delta G^\ddagger(\beta) \quad \implies \quad k_\alpha \gg k_\beta \tag{1.3}$$

Under **kinetic control**, electrophilic substitution takes place almost exclusively at the $\alpha$-position (C1).

| Electrophilic Reaction | Conditions | Major Product | Kinetic vs Thermodynamic Control |
| :--- | :--- | :--- | :--- |
| **Nitration** | $\text{HNO}_3 / \text{H}_2\text{SO}_4, 50^\circ\text{C}$ | 1-Nitronaphthalene ($>95\%$) | Kinetic control ($\Delta G^\ddagger_\alpha \ll \Delta G^\ddagger_\beta$) |
| **Bromination** | $\text{Br}_2 / \text{CCl}_4, 25^\circ\text{C}$ | 1-Bromonaphthalene ($>90\%$) | Kinetic control |
| **Low-Temp Sulfonation** | $\text{H}_2\text{SO}_4, 80^\circ\text{C}$ | Naphthalene-1-sulfonic acid | Kinetic control |
| **High-Temp Sulfonation** | $\text{H}_2\text{SO}_4, 160^\circ\text{C}$ | Naphthalene-2-sulfonic acid | **Thermodynamic control** |

### Thermodynamic Control: The Sulfonation Inversion
The sulfonation of naphthalene provides a textbook demonstration of reaction coordinate equilibria:
- At $80^\circ\text{C}$, the forward rate constant $k_\alpha$ dominates because $\Delta G^\ddagger_\alpha \approx 78\text{ kJ}\cdot\text{mol}^{-1}$ compared to $\Delta G^\ddagger_\beta \approx 92\text{ kJ}\cdot\text{mol}^{-1}$. Naphthalene-1-sulfonic acid precipitates out as the major kinetic product ($96\%$).
- However, the sulfonic acid group ($-\text{SO}_3\text{H}$) at C1 experiences severe **peri-steric strain** with the hydrogen atom at the C8 position (interatomic distance $d_{\text{S}\cdots\text{H8}} \approx 2.4\text{ \AA}$, well within their sum of van der Waals radii):

$$\Delta H^\circ_{\text{peri-strain}} \approx 18.5\text{ kJ}\cdot\text{mol}^{-1}$$

- At $160^\circ\text{C}$, sulfonation becomes fully reversible ($k_{-\alpha}$ is large). The sterically unencumbered naphthalene-2-sulfonic acid is thermodynamically more stable by $\sim 15\text{ kJ}\cdot\text{mol}^{-1}$. As equilibration proceeds, the 1-sulfonic acid isomerizes via protodesulfonation back to naphthalene, which is irreversibly trapped as the $\beta$-isomer (85% yield at $160^\circ\text{C}$).""",
                "simulations": []
            },
            {
                "id": "sec1_5",
                "secNumber": "§1.5",
                "title": "Anthracene & Phenanthrene: C9/C10 Localization & Reactivity",
                "heading": "Anthracene & Phenanthrene: C9/C10 Localization & Reactivity",
                "content": r"""The reactivity profiles of anthracene and phenanthrene differ profoundly from monocyclic aromatics. In both molecules, electrophilic attack occurs preferentially at the **C9 and C10 positions**, but via distinct mechanistic pathways dictated by the conservation of aromatic sextets.

### Anthracene C9/C10 Meso Reactivity
In anthracene, attack of an electrophile $E^+$ at C9 yields a carbocation in which **both outer rings (rings A and C) retain fully intact benzenoid Clar sextets**:

$$\text{Anthracene} + E^+ \longrightarrow [\text{C9-Wheland Intermediate}]^+ \tag{1.4}$$

The loss of resonance energy upon transforming anthracene into its 9-arenium intermediate is only:

$$\Delta E_{\text{loss}} = \text{RE}(\text{anthracene}) - 2 \times \text{RE}(\text{benzene}) = 351 - 2(152) = 47\text{ kJ}\cdot\text{mol}^{-1}$$

Compare this with attack at C1 or C2, which would destroy one sextet and leave a naphthalene system, requiring an energetic penalty $>90\text{ kJ}\cdot\text{mol}^{-1}$. Consequently:
- **Bromination**: Treatment of anthracene with $\text{Br}_2$ in $\text{CS}_2$ at $0^\circ\text{C}$ does *not* immediately undergo substitution; instead, it undergoes **trans-9,10-addition** to furnish 9,10-dibromo-9,10-dihydroanthracene! Upon gentle warming, spontaneous elimination of $\text{HBr}$ restores the central ring conjugation, delivering 9-bromoanthracene.
- **Diels-Alder Reactivity**: Because the C9 and C10 atoms possess localized frontier orbital coefficients ($c_{\text{HOMO},9} = c_{\text{HOMO},10} = 0.440$), anthracene acts as a conjugated diene in [4+2] cycloadditions across positions 9 and 10. Reaction with maleic anhydride in refluxing xylene affords a bicyclic bridged endo-adduct with quantitative yield, preserving two independent benzenoid rings.

### Phenanthrene C9/C10 K-Region Reactivity
Phenanthrene's C9-C10 bond behaves as a localized alkene flanked by two independent Clar sextets:
- Reaction of phenanthrene with $\text{Br}_2$ in $\text{CCl}_4$ yields **9,10-dibromo-9,10-dihydrophenanthrene** via stereospecific *anti*-addition:

$$\text{Phenanthrene} + \text{Br}_2 \xrightarrow{\text{CCl}_4} \text{trans-9,10-dibromo-9,10-dihydrophenanthrene} \tag{1.5}$$

Refluxing this addition adduct in alcoholic $\text{KOH}$ promotes E2 dehydrobromination, furnishing 9-bromophenanthrene in $92\%$ yield.
- Catalytic hydrogenation over $\text{Cu/Cr}_2\text{O}_3$ at $150^\circ\text{C}$ and $100\text{ atm}$ selectively reduces the C9-C10 bond to yield 9,10-dihydrophenanthrene, preserving $304\text{ kJ}\cdot\text{mol}^{-1}$ of biphenyl-like resonance energy.""",
                "simulations": []
            },
            {
                "id": "sec1_6",
                "secNumber": "§1.6",
                "title": "Oxidation, Reduction & Quinone Cascades",
                "heading": "Oxidation, Reduction & Quinone Cascades",
                "content": r"""The susceptibility of fused benzenoids to chemical oxidation and reduction correlates directly with their localization energies and lowest unoccupied molecular orbital (LUMO) energy levels.

### Controlled Oxidation Pathways

1. **Naphthalene**:
   - Treatment with chromium trioxide ($\text{CrO}_3$) in glacial acetic acid at $25^\circ\text{C}$ oxidizes the $\alpha$-rich positions to yield **1,4-naphthoquinone** ($40\%$).
   - Vigorous oxidation with vanadium pentoxide ($\text{V}_2\text{O}_5$) and molecular oxygen at $400^\circ\text{C}$ cleaves one ring entirely, producing **phthalic anhydride** and carbon dioxide:
   $$\text{C}_{10}\text{H}_8 + \frac{9}{2}\,\text{O}_2 \xrightarrow{\text{V}_2\text{O}_5, 400^\circ\text{C}} \text{C}_8\text{H}_4\text{O}_3 (\text{phthalic anhydride}) + 2\,\text{CO}_2 + 2\,\text{H}_2\text{O}$$

2. **Anthracene**:
   - Rapid oxidation with sodium dichromate ($\text{Na}_2\text{Cr}_2\text{O}_7$) in aqueous sulfuric acid attacks the activated C9 and C10 meso carbons, yielding **9,10-anthraquinone** with $>90\%$ selectivity:
   $$\text{C}_{14}\text{H}_{10} + \text{Cr}_2\text{O}_7^{2-} + 8\,\text{H}^+ \longrightarrow \text{C}_{14}\text{H}_8\text{O}_2 + 2\,\text{Cr}^{3+} + 5\,\text{H}_2\text{O}$$
   9,10-Anthraquinone is the industrial precursor for alizarin (1,2-dihydroxyanthraquinone) and vat dyes.

3. **Phenanthrene**:
   - Oxidation with $\text{CrO}_3$ in acetic acid attacks the C9-C10 bond, delivering **9,10-phenanthrenequinone**. Further oxidation with alkaline potassium permanganate ($\text{KMnO}_4$) or hydrogen peroxide cleaves the central bond to form **diphenic acid** (biphenyl-2,2'-dicarboxylic acid).

### Reduction Cascades
- **Birch Reduction**: Naphthalene reacts with sodium in liquid ammonia in the presence of ethanol to produce **1,4-dihydronaphthalene**. At higher temperatures or with sodium in boiling amyl alcohol, reduction yields **tetralin** (1,2,3,4-tetrahydronaphthalene). Exhaustive catalytic hydrogenation over Raney nickel at $200^\circ\text{C}$ yields **decalin** (bicyclo[4.4.0]decane), which exists as separable *cis* and *trans* diastereomers.""",
                "simulations": []
            },
            {
                "id": "sec1_7",
                "secNumber": "§1.7",
                "title": "Polycyclic Carcinogenesis & Diol Epoxide Metabolic Activation",
                "heading": "Polycyclic Carcinogenesis & Diol Epoxide Metabolic Activation",
                "content": r"""Many high-molecular-weight angular polycyclic hydrocarbons, notably **benzo[a]pyrene** ($\text{C}_{20}\text{H}_{12}$), **7,12-dimethylbenz[a]anthracene (DMBA)**, and **chrysene**, are potent chemical procarcinogens found in tobacco smoke, coal tar, and charbroiled foods. The molecular mechanism of their biological mutagenicity represents a classic intersection of physical organic chemistry and molecular toxicology.

### The Bay-Region Diol Epoxide Theory
Formulated by Donald Jerina and Alan Conney, the **bay-region theory** explains how chemically inert polyaromatic hydrocarbons are metabolically converted by hepatic enzymes into electrophilic mutagens that alkylate genomic DNA.

```
                  Metabolic Activation Cascade:
                  Benzo[a]pyrene
                       |  Cytochrome P450 1A1
                       v
                  (+)-Benzo[a]pyrene 7,8-oxide
                       |  Epoxide Hydrolase (EH)
                       v
                  (-)-Benzo[a]pyrene-7,8-dihydrodiol
                       |  Cytochrome P450 1A1
                       v
                  (+)-anti-Benzo[a]pyrene-7,8-dihydrodiol-9,10-epoxide (BPDE)
                       |  DNA Guanine N2 Attack
                       v
                  Covalent DNA Adduct (Guanine-N2-BPDE) ---> Transversion Mutation (G -> T)
```

The enzymatic activation cascade proceeds in three distinct stages:
1. **Initial Epoxidation**: Hepatic cytochrome P450 monooxygenase (specifically CYP1A1) stereoselectively oxidizes the terminal ring to yield **(+)-benzo[a]pyrene-7,8-oxide**.
2. **Hydrolysis**: Microsomal epoxide hydrolase catalyzes *anti*-diaxial addition of water, opening the oxirane to yield **(-)-benzo[a]pyrene-7,8-dihydrodiol**.
3. **Second Epoxidation**: CYP1A1 oxidizes the adjacent olefin at the C9-C10 position to generate **(+)-anti-benzo[a]pyrene-7,8-dihydrodiol-9,10-epoxide (BPDE)**.

### Exceptional Electrophilic Reactivity of BPDE
Why is the 9,10-epoxide in the bay region extraordinarily reactive toward cellular nucleophiles, resisting enzymatic hydrolysis?
The opening of the epoxide oxirane ring at C10 generates a carbocation that is stabilized by **benzylic conjugation** with the adjacent polycyclic pyrene core:

$$\Delta G^\ddagger_{\text{ring-opening}} \ll 65\text{ kJ}\cdot\text{mol}^{-1}$$

Furthermore, steric congestion inside the angular "bay region" between C10 and the C11 proton forces the oxirane ring into an electronically strained conformation.

When the benzylic carbocation forms, the exocyclic amino group of **deoxyguanosine ($N^2$)** in cellular DNA attacks C10 stereospecifically:

$$\text{BPDE} + \text{DNA(Guanine-}N^2\text{)} \longrightarrow \text{DNA-BPDE covalent adduct} \tag{1.6}$$

This covalent adduct distorts the DNA double helix, evades nucleotide excision repair enzymes, and causes critical $\text{G} \to \text{T}$ transversion mutations in codons 12, 13, and 61 of the *KRAS* oncogene and hotspot codons 157, 248, and 273 of the *TP53* tumor suppressor gene, initiating neoplastic transformation.""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob1_1",
                "problemNumber": "1.1",
                "title": "Thermodynamic Disparity in Anthracene vs Phenanthrene Clar Sextets",
                "difficulty": "Advanced",
                "statement": r"""Calculate the theoretical resonance stabilization energies of anthracene and phenanthrene using Clar's aromatic sextet model and empirical benzenoid increments. Given that the empirical resonance stabilization energy of an isolated benzene ring is $E_{\text{sextet}} = 152\text{ kJ}\cdot\text{mol}^{-1}$ and that of an isolated localized conjugated double bond is $\Delta E_{\text{alkene}} = 12\text{ kJ}\cdot\text{mol}^{-1}$, quantify the difference in resonance enthalpy $\Delta(\Delta H^\circ_{\text{res}})$ between the two $\text{C}_{14}\text{H}_{10}$ constitutional isomers and explain why phenanthrene displays a much lower enthalpy of combustion.""",
                "hints": ["Determine the maximum number of simultaneously disjoint benzenoid sextets each isomer can possess according to Clar's rule.", "Count the remaining formal double bonds not included in sextets."],
                "solution": r"""### 1. Conceptual Framework & Clar Topological Graph
According to Clar's rule of aromatic sextets:
- **Anthracene**: Possesses three fused rings in a linear row. Only **one Clar sextet** can be inscribed at any one time without sharing adjacent $\pi$-electrons across rings. The remaining 8 $\pi$-electrons are distributed as 4 localized formal double bonds:
  $$E_{\text{res}}(\text{Anthracene}) = 1 \times E_{\text{sextet}} + 4 \times \Delta E_{\text{alkene}}$$
- **Phenanthrene**: Possesses an angular phene geometry. Clar topology permits **two independent, mutually disjoint Clar sextets** to be inscribed simultaneously in the terminal outer rings (Rings A and C). The remaining 2 $\pi$-electrons form one localized formal double bond at the central C9-C10 K-region:
  $$E_{\text{res}}(\text{Phenanthrene}) = 2 \times E_{\text{sextet}} + 1 \times \Delta E_{\text{alkene}}$$

### 2. Numerical Calculation of Theoretical Resonance Energies
Using the empirical values provided:
$$\begin{aligned}
E_{\text{res}}(\text{Anthracene}) &= 1(152\text{ kJ}\cdot\text{mol}^{-1}) + 4(12\text{ kJ}\cdot\text{mol}^{-1}) \\
&= 152 + 48 = 200\text{ kJ}\cdot\text{mol}^{-1} \\
E_{\text{res}}(\text{Phenanthrene}) &= 2(152\text{ kJ}\cdot\text{mol}^{-1}) + 1(12\text{ kJ}\cdot\text{mol}^{-1}) \\
&= 304 + 12 = 316\text{ kJ}\cdot\text{mol}^{-1}
\end{aligned}$$

The theoretical difference in resonance stabilization between phenanthrene and anthracene is:
$$\Delta E_{\text{res}} = E_{\text{res}}(\text{Phenanthrene}) - E_{\text{res}}(\text{Anthracene}) = 316 - 200 = 116\text{ kJ}\cdot\text{mol}^{-1}$$

In experimental thermochemical measurements (calorimetric heats of combustion), the difference in total stabilization enthalpy is:
$$\Delta H^\circ_{\text{combustion}}(\text{Anthracene}) = -7062\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta H^\circ_{\text{combustion}}(\text{Phenanthrene}) = -7032\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta H^\circ_{\text{isomerization}} = \Delta H^\circ_{\text{comb}}(\text{Phenanthrene}) - \Delta H^\circ_{\text{comb}}(\text{Anthracene}) = -30\text{ kJ}\cdot\text{mol}^{-1}$$

### 3. Physical Conclusion
Phenanthrene releases $30\text{ kJ}\cdot\text{mol}^{-1}$ less energy upon combustion because it is thermodynamically more stable. Its two fully localized aromatic sextets retain true benzenoid character, rendering it chemically far less reactive than anthracene toward addition and oxidation."""
            },
            {
                "id": "prob1_2",
                "problemNumber": "1.2",
                "title": "Regioselective Kinetic vs Thermodynamic Sulfonation of Naphthalene",
                "difficulty": "Mastery",
                "statement": r"""A reaction mixture of naphthalene and concentrated sulfuric acid is maintained at $80^\circ\text{C}$ for 30 minutes, yielding Product A ($>95\%$). When the reaction is heated to $160^\circ\text{C}$ for 4 hours, Product B is isolated as the predominant species ($85\%$). 
(a) Draw the complete structures of Products A and B.
(b) Construct a reaction coordinate energy diagram illustrating the activation energies ($\Delta G^\ddagger_\alpha$ vs $\Delta G^\ddagger_\beta$) and standard Gibbs free energies of reaction ($\Delta G^\circ_\alpha$ vs $\Delta G^\circ_\beta$).
(c) Mechanistically justify the thermodynamic instability of Product A by calculating the steric van der Waals overlap distance between peri-substituents.""",
                "hints": ["Review the arenium ion resonance contributors for $\alpha$ vs $\beta$ attack.", "Recall the spatial distance between C1 and C8 in the rigid naphthalene bicyclic frame."],
                "solution": r"""### (a) Identification of Products
- **Product A (Low temperature, $80^\circ\text{C}$)**: **Naphthalene-1-sulfonic acid** ($\alpha$-isomer, kinetic product).
- **Product B (High temperature, $160^\circ\text{C}$)**: **Naphthalene-2-sulfonic acid** ($\beta$-isomer, thermodynamic product).

### (b) Reaction Coordinate Energetics
1. **Arenium Ion Stability**: Electrophilic attack by $\text{SO}_3$ at the C1 position produces a Wheland intermediate with 4 resonance contributors retaining an intact benzenoid ring, compared to only 2 contributors for attack at C2. Consequently:
   $$\Delta G^\ddagger_\alpha \approx 78\text{ kJ}\cdot\text{mol}^{-1} < \Delta G^\ddagger_\beta \approx 92\text{ kJ}\cdot\text{mol}^{-1}$$
   At $80^\circ\text{C}$, the reaction is kinetically controlled, and the formation of the $\alpha$-isomer is roughly 50 times faster ($k_\alpha \gg k_\beta$).
2. **Reversibility and Thermodynamic Stability**: Sulfonation is reversible in the presence of hydronium ions via protodesulfonation:
   $$\text{Ar-SO}_3\text{H} + \text{H}_3\text{O}^+ \rightleftharpoons \text{Ar-H} + \text{H}_2\text{SO}_4 + \text{H}^+$$
   At $160^\circ\text{C}$, thermal energy exceeds the barrier for desulfonation ($\Delta G^\ddagger_{\text{desulf}}$). Equilibrium is established:
   $$\Delta G^\circ_\beta < \Delta G^\circ_\alpha \quad (\text{by }\sim 15\text{ kJ}\cdot\text{mol}^{-1})$$

### (c) Peri-Steric Repulsion Geometry
In naphthalene-1-sulfonic acid, the sulfur atom is covalently bonded to C1 at a distance of $r_{\text{C1-S}} \approx 1.76\text{ \AA}$. The bulky, tetrahedral $-\text{SO}_3\text{H}$ group projects into the space occupied by the peri-hydrogen at C8 ($r_{\text{C8-H}} \approx 1.09\text{ \AA}$).
Given the fixed C1-C9-C8 ring geometry with bond angles of $120^\circ$:
$$d_{\text{peri}}(\text{S}\cdots\text{H8}) \approx 2.42\text{ \AA}$$
The sum of the van der Waals radii of oxygen/sulfur and hydrogen is:
$$r_{\text{vdW}}(\text{O}) + r_{\text{vdW}}(\text{H}) = 1.52 + 1.20 = 2.72\text{ \AA}$$
Because $2.42\text{ \AA} < 2.72\text{ \AA}$, significant van der Waals overlap occurs, generating severe steric strain ($\Delta H^\circ_{\text{strain}} \approx 18.5\text{ kJ}\cdot\text{mol}^{-1}$). In the $\beta$-isomer (C2), the $-\text{SO}_3\text{H}$ group projects away into open space flanked only by C1-H and C3-H at standard $120^\circ$ angles ($d > 2.85\text{ \AA}$), completely relieving peri-repulsion."""
            },
            {
                "id": "prob1_3",
                "problemNumber": "1.3",
                "title": "Haworth Synthesis Sequence: Tetralin to Naphthalene Aromatization",
                "difficulty": "Intermediate",
                "statement": r"""Provide the complete five-step chemical sequence for the total synthesis of 1-methylnaphthalene from benzene and succinic anhydride. Specify all required reagents, reaction conditions, and intermediate structures. At which step is the methyl group introduced, and what side-product would form if Clemmensen reduction were attempted on an acid chloride?""",
                "hints": ["Where can an organometallic Grignard reagent be introduced before final aromatization?", "Acid chlorides react violently with aqueous acidic zinc amalgam."],
                "solution": r"""### 1. Step-by-Step Synthetic Sequence
$$\begin{aligned}
\text{Step 1}: &\quad \text{Benzene} + \text{Succinic anhydride} \xrightarrow{\text{AlCl}_3, \text{PhNO}_2} \text{4-phenyl-4-oxobutanoic acid} \\
\text{Step 2}: &\quad \text{4-phenyl-4-oxobutanoic acid} \xrightarrow{\text{Zn(Hg)}, \text{conc. HCl, reflux}} \text{4-phenylbutanoic acid} \\
\text{Step 3}: &\quad \text{4-phenylbutanoic acid} \xrightarrow{\text{polyphosphoric acid (PPA)}, 90^\circ\text{C}} \alpha\text{-tetralone} \\
\text{Step 4}: &\quad \alpha\text{-tetralone} \xrightarrow{\text{1. }\text{CH}_3\text{MgBr, diethyl ether} \atop \text{2. }\text{H}_3\text{O}^+, \Delta (-\text{H}_2\text{O})} \text{1-methyl-3,4-dihydronaphthalene} \\
\text{Step 5}: &\quad \text{1-methyl-3,4-dihydronaphthalene} \xrightarrow{\text{Pd/C (10\%) or Se}, 300^\circ\text{C}} \text{1-methylnaphthalene} + \text{H}_2\uparrow
\end{aligned}$$

### 2. Strategic Rationale
The methyl group is introduced at **Step 4** by nucleophilic addition of methylmagnesium bromide to the ketone carbonyl of $\alpha$-tetralone, followed by acid-catalyzed dehydration.

### 3. Chemical Precaution with Acid Chlorides
If an acid chloride ($\text{RCOCl}$) were subjected to Clemmensen conditions ($\text{Zn(Hg)}/\text{aqueous HCl}$), the acyl chloride would undergo rapid competitive solvolytic hydrolysis to the carboxylic acid, and the nascent hydrogen and zinc amalgam could reduce the chloride to an aldehyde or uncyclized alkane without selective deoxygenation."""
            },
            {
                "id": "prob1_4",
                "problemNumber": "1.4",
                "title": "Diels-Alder Cycloaddition Frontier Orbital Analysis of Anthracene",
                "difficulty": "Advanced",
                "statement": r"""Anthracene acts as a diene in Diels-Alder reactions across its C9 and C10 meso positions when treated with maleic anhydride, whereas phenanthrene fails to undergo cycloaddition under identical conditions.
(a) Write the balanced chemical reaction including the three-dimensional stereochemistry of the bridged product.
(b) Using frontier molecular orbital (FMO) coefficients, calculate why the reaction occurs specifically at C9/C10 rather than C1/C4.
(c) Explain why phenanthrene does not react with maleic anhydride.""",
                "hints": ["Analyze the aromatic sextet count of the cycloadduct in anthracene vs phenanthrene.", "Anthracene loses only one Clar sextet, creating two intact benzene rings."],
                "solution": r"""### (a) Reaction and Stereochemistry
Anthracene reacts with maleic anhydride in refluxing toluene ($110^\circ\text{C}$) to form the bridged bicyclic adduct:
$$\text{Anthracene} + \text{Maleic anhydride} \longrightarrow \text{9,10-dihydroanthracene-9,10-endo-}\alpha,\beta\text{-succinic anhydride}$$
The product features a rigid 9,10-ethanoanthracene skeleton where the anhydride ring adopts the *endo* stereochemical orientation due to secondary orbital overlap between the carbonyl $\pi^*$ orbitals of maleic anhydride and the back-lobes of the bridging C11/C12 carbon atoms.

### (b) FMO and Resonance Localization Analysis
In anthracene's highest occupied molecular orbital ($\psi_7$, HOMO):
$$c_{\text{HOMO}}(\text{C9}) = +0.440, \quad c_{\text{HOMO}}(\text{C10}) = -0.440$$
In contrast, the coefficients at the outer carbons are much smaller: $c_{\text{HOMO}}(\text{C1}) = 0.220$. The orbital overlap with the LUMO of maleic anhydride ($\pi^*$) is maximized at the C9 and C10 positions.
Crucially, cycloaddition across C9 and C10 converts the central ring from $sp^2$ to $sp^3$, yielding **two completely independent, fully benzenoid rings** (stabilization energy: $2 \times 152 = 304\text{ kJ}\cdot\text{mol}^{-1}$). The net energetic penalty for loss of anthracene's conjugation is only:
$$\Delta E_{\text{resonance penalty}} = 351 - 304 = 47\text{ kJ}\cdot\text{mol}^{-1}$$

### (c) Phenanthrene Inertness
If phenanthrene were to undergo [4+2] cycloaddition across C9 and C10, it would require destroying one of its two existing intact Clar sextets, converting the molecule to a system with only one intact benzene ring and a biphenyl core:
$$\Delta E_{\text{resonance penalty}}(\text{Phenanthrene}) \approx 381 - 152 = 229\text{ kJ}\cdot\text{mol}^{-1}$$
This massive activation penalty of $>220\text{ kJ}\cdot\text{mol}^{-1}$ renders the Diels-Alder reaction of phenanthrene thermodynamically disfavored and kinetically inaccessible under standard thermal conditions."""
            },
            {
                "id": "prob1_5",
                "problemNumber": "1.5",
                "title": "Metabolic Epoxidation Kinetics & Bay-Region Carbocation Stabilization",
                "difficulty": "Mastery",
                "statement": r"""The mutagenic potency of polycyclic aromatic hydrocarbons correlates with the ease of heterolytic cleavage of the bay-region epoxide ring.
(a) Contrast the solvolytic reactivity of benzo[a]pyrene-7,8-dihydrodiol-9,10-epoxide (BPDE) with an ordinary non-aromatic aliphatic epoxide (e.g., cyclohexene oxide).
(b) Derive the resonance structures for the benzylic carbocation intermediate formed at C10 of BPDE and explain why alkylation occurs at C10 rather than C9.
(c) Identify the exact atom of the DNA guanine base that attacks C10 and state the stereochemical consequence (retention vs inversion).""",
                "hints": ["Look at the benzylic position relative to the pyrene core.", "The amino group of guanine is an ambident nucleophile; identify the most nucleophilic neutral nitrogen."],
                "solution": r"""### (a) Solvolytic Reactivity Comparison
- **Cyclohexene Oxide**: Cleavage of an aliphatic epoxide requires strong acid activation ($\text{pH} < 2$) because the forming secondary carbocation is highly unstable ($\Delta G^\ddagger > 115\text{ kJ}\cdot\text{mol}^{-1}$). In neutral aqueous buffer ($\text{pH} = 7.4$), the half-life is weeks.
- **BPDE**: Under physiological conditions ($\text{pH} = 7.4, 37^\circ\text{C}$), BPDE spontaneously undergoes heterolytic $\text{C10}-\text{O}$ bond cleavage with a half-life of only $t_{1/2} \approx 8\text{ minutes}$. This extreme acceleration ($>10^6$-fold) occurs because opening the oxirane at C10 creates a **benzylic carbocation** directly conjugated to the entire four-ring pyrene aromatic system.

### (b) Benzylic Carbocation Stabilization at C10 vs C9
Heterolysis of the $\text{C10}-\text{O}$ bond places a full positive charge on C10:
$$\text{BPDE} \longrightarrow [\text{BPDE-C10}]^+ + \text{OH}^- \tag{\text{or coordinated }\text{H}_2\text{O}}$$
C10 is directly adjacent to the aromatic ring system (benzylic position). The empty $p$-orbital on C10 overlaps with the $\pi$-system of the pyrene core, delocalizing the carbocation across at least **9 canonical resonance contributors**.
In contrast, if heterolysis occurred at C9, the positive charge would reside on a non-benzylic carbon separated from the aromatic ring by an $sp^3$-hybridized C8 center bearing a hydroxyl group. Thus, cleavage occurs exclusively at C10.

### (c) DNA Adduct Formation
The nucleophile in genomic DNA is the **exocyclic amino group of guanine ($N^2$)**:
$$\text{DNA-Guanine-}N^2\text{H}_2 + [\text{BPDE-C10}]^+ \longrightarrow \text{DNA-Guanine-}N^2\text{-BPDE} + \text{H}^+$$
Because the reactive intermediate possesses substantial carbocation character with a long life-time in the hydrophobic intercalation pocket of DNA, nucleophilic attack occurs predominantly via an $S_N1$-like pathway with preferential *trans*-addition (net inversion of stereochemistry at C10 relative to the original epoxide), forming the $(+)\text{-}anti\text{-BPDE-}N^2\text{-dG}$ adduct."""
            },
            {
                "id": "prob1_6",
                "problemNumber": "1.6",
                "title": "Oxidative Cleavage of Phenanthrene: Synthesis of Diphenic Acid",
                "difficulty": "Intermediate",
                "statement": r"""Devise an efficient two-stage chemical synthesis of diphenic acid (biphenyl-2,2'-dicarboxylic acid) starting from commercial phenanthrene.
(a) Provide all reagents and reaction conditions for each step.
(b) What intermediate is formed during the first stage, and what is its oxidation state?
(c) When diphenic acid is heated with acetic anhydride, it readily forms a cyclic anhydride. What does this reveal about the rotational freedom and dihedral angle of the biphenyl rings?""",
                "hints": ["Oxidize the reactive K-region first to a 1,2-dione.", "Diphenic anhydride has a 7-membered ring."],
                "solution": r"""### (a) Two-Stage Synthetic Route
$$\begin{aligned}
\text{Stage 1}: &\quad \text{Phenanthrene} \xrightarrow{\text{CrO}_3, \text{glacial AcOH, }70^\circ\text{C}} \text{9,10-Phenanthrenequinone} \\
\text{Stage 2}: &\quad \text{9,10-Phenanthrenequinone} \xrightarrow{\text{1. }30\%\, \text{H}_2\text{O}_2, \text{AcOH, }80^\circ\text{C} \atop \text{2. Acidify with HCl}} \text{Diphenic acid (biphenyl-2,2'-dicarboxylic acid)}
\end{aligned}$$
Alternatively, direct one-pot oxidation can be achieved using alkaline $\text{KMnO}_4$ under reflux:
$$\text{Phenanthrene} + 4\,\text{KMnO}_4 \xrightarrow{\text{NaOH, }\Delta} \text{Diphenic acid} + 4\,\text{MnO}_2\downarrow$$

### (b) Intermediate Analysis
The intermediate is **9,10-phenanthrenequinone**, an orange-yellow crystalline ortho-dione. The oxidation state of carbons C9 and C10 changes from $+0$ in phenanthrene (each bonded to one H, one C, and double-bonded to C) to $+2$ in the quinone (each double-bonded to oxygen and single-bonded to two carbons).

### (c) Conformational Implications of Diphenic Anhydride
When diphenic acid is heated with acetic anhydride:
$$\text{Diphenic acid} \xrightarrow{\text{Ac}_2\text{O}, \Delta} \text{Diphenic anhydride} + \text{AcOH}$$
It forms a stable **seven-membered cyclic anhydride**. In unconstrained biphenyl-2,2'-dicarboxylic acid, steric repulsion between the bulky ortho-carboxyl groups forces the two phenyl rings into a non-coplanar, mutually twisted chiral conformation with a dihedral angle $\theta \approx 60^\circ\text{–}70^\circ$. Formation of the cyclic anhydride locks the two phenyl rings into a constrained dihedral angle ($\theta \approx 45^\circ$), demonstrating that rotation about the central C1-C1' biphenyl bond is sterically restricted."""
            },
            {
                "id": "prob1_7",
                "problemNumber": "1.7",
                "title": "Quantitative Coulson $\pi$-Bond Orders in Naphthalene",
                "difficulty": "Mastery",
                "statement": r"""Using the Hückel molecular orbital secular equations for naphthalene, the mobile $\pi$-bond orders between adjacent carbon atoms are determined as:
$$p_{12} = 0.725, \quad p_{23} = 0.603, \quad p_{91} = 0.554, \quad p_{9,10} = 0.518$$
(a) Using Coulson's empirical relation $R_{rs} = 1.54 - \frac{0.21}{1 + 1.05 \left(\frac{1 - p_{rs}}{p_{rs}}\right)}$, compute the theoretical bond lengths $R_{12}, R_{23}, R_{91},$ and $R_{9,10}$.
(b) Compare these calculated bond distances to the experimental X-ray crystallographic values ($R_{12}^{\text{exp}} = 1.365\text{ \AA}, R_{23}^{\text{exp}} = 1.404\text{ \AA}$).
(c) Explain why electrophilic addition of bromine to naphthalene in cold non-polar solvent occurs selectively across C1-C2 rather than C2-C3.""",
                "hints": ["Substitute each $p_{rs}$ into the given algebraic formula.", "Higher $\pi$-bond order corresponds to greater localized double-bond character."],
                "solution": r"""### (a) Numerical Computation of Bond Distances
Coulson's formula is:
$$R_{rs} = 1.54 - \frac{0.21}{1 + 1.05 \left(\frac{1 - p_{rs}}{p_{rs}}\right)}$$

1. **For C1-C2 bond ($p_{12} = 0.725$)**:
   $$\frac{1 - 0.725}{0.725} = \frac{0.275}{0.725} = 0.3793$$
   $$1 + 1.05(0.3793) = 1 + 0.3983 = 1.3983$$
   $$R_{12} = 1.54 - \frac{0.21}{1.3983} = 1.54 - 0.1502 = 1.3898\text{ \AA} \approx 1.390\text{ \AA}$$
   *(With refined $\kappa=0.81$ empirical parameter, $R_{12} = 1.368\text{ \AA}$)*.

2. **For C2-C3 bond ($p_{23} = 0.603$)**:
   $$\frac{1 - 0.603}{0.603} = \frac{0.397}{0.603} = 0.6584$$
   $$1 + 1.05(0.6584) = 1 + 0.6913 = 1.6913$$
   $$R_{23} = 1.54 - \frac{0.21}{1.6913} = 1.54 - 0.1242 = 1.4158\text{ \AA} \approx 1.416\text{ \AA}$$

3. **For C9-C1 bond ($p_{91} = 0.554$)**:
   $$\frac{1 - 0.554}{0.554} = \frac{0.446}{0.554} = 0.8051 \implies 1 + 1.05(0.8051) = 1.8453$$
   $$R_{91} = 1.54 - \frac{0.21}{1.8453} = 1.54 - 0.1138 = 1.4262\text{ \AA} \approx 1.426\text{ \AA}$$

4. **For C9-C10 central bond ($p_{9,10} = 0.518$)**:
   $$\frac{1 - 0.518}{0.518} = \frac{0.482}{0.518} = 0.9305 \implies 1 + 1.05(0.9305) = 1.9770$$
   $$R_{9,10} = 1.54 - \frac{0.21}{1.9770} = 1.54 - 0.1062 = 1.4338\text{ \AA} \approx 1.434\text{ \AA}$$

### (b) Experimental Correlation
The calculation reproduces the experimental trend:
$$R_{12} (1.365\text{ \AA}) < R_{23} (1.404\text{ \AA}) < R_{91} (1.425\text{ \AA}) \approx R_{9,10} (1.428\text{ \AA})$$
This verifies that naphthalene is NOT an isotropic aromatic ring like benzene, but possesses marked bond fixation.

### (c) Mechanistic Regioselectivity
Because the C1-C2 bond possesses the highest $\pi$-electron density ($p_{12} = 0.725$) and the shortest interatomic distance, electrophilic attack by $\text{Br}^+$ occurs selectively at C1, forming a cyclic bromonium or arenium ion spanning C1-C2. This preserves the aromatic sextet in the adjacent ring B and gives the lowest activation barrier."""
            }
        ]
    }

def get_unit_2():
    return {
        "id": "unit2",
        "unitId": "unit2-org2",
        "number": 2,
        "unitNumber": 2,
        "title": "Unit 2: Aldehydes and Ketones: Nucleophilic Addition Dynamics, Carbonyl Condensations & Stereocontrol",
        "description": "Rigorous physical organic and mechanistic exploration of carbonyl chemistry: electronic polarization and Bürgi-Dunitz 107° nucleophilic trajectory, reversible hydration and acetal thermodynamics, irreversible organometallic additions, imine/enamine equilibria, deoxygenation protocols (Wolff-Kishner, Clemmensen, Mozingo), Baeyer-Villiger migratory aptitudes, enol-enolate equilibria, and aldol, Claisen-Schmidt, Cannizzaro, Benzoin, Perkin, and Knoevenagel condensation cascades.",
        "leadSummary": "Exhaustive treatment of carbonyl orbital interactions, Bürgi-Dunitz trajectory, protecting group strategies, oxidation-reduction mechanisms, enol/enolate stereocontrol, and multi-component base/acid-catalyzed condensation cascades.",
        "simulations": ["sim_chem_carbonyl_addition_burgi_dunitz", "sim_chem_aldol_condensation_equilibria"],
        "sections": [
            {
                "id": "sec2_1",
                "secNumber": "§2.1",
                "title": "Carbonyl Orbital Polarization & the Bürgi-Dunitz 107° Trajectory",
                "heading": "Carbonyl Orbital Polarization & the Bürgi-Dunitz 107° Trajectory",
                "content": r"""The carbonyl group ($\text{C}=\text{O}$) is the central functional group of organic synthesis. Its reactivity is governed by strong orbital polarization resulting from the Pauling electronegativity disparity between carbon ($\chi_P = 2.55$) and oxygen ($\chi_P = 3.44$).

### Frontier Molecular Orbitals of the Carbonyl Group
In molecular orbital theory, the carbonyl $\pi$ bond arises from the overlap of an $sp^2$-hybridized orbital on carbon with a $2p$ orbital on oxygen:

$$\psi_\pi = c_{\text{C}} \, 2p_{z,\text{C}} + c_{\text{O}} \, 2p_{z,\text{O}} \quad (c_{\text{O}} > c_{\text{C}}) \tag{2.1}$$
$$\psi_{\pi^*} = c'_{\text{C}} \, 2p_{z,\text{C}} - c'_{\text{O}} \, 2p_{z,\text{O}} \quad (|c'_{\text{C}}| > |c'_{\text{O}}|) \tag{2.2}$$

- **HOMO**: Corresponds to the oxygen non-bonding lone pairs ($n_{\text{O}}$), oriented in the plane of the carbonyl group.
- **LUMO**: Corresponds to the antibonding $\pi^*$ orbital. Crucially, because oxygen is more electronegative, the bonding $\pi$ orbital is polarized toward oxygen, while the antibonding $\pi^*$ orbital is polarized toward **carbon** ($|c'_{\text{C}}|^2 \approx 0.70$, $|c'_{\text{O}}|^2 \approx 0.30$).

Consequently, nucleophilic attack ($E_{\text{HOMO, Nuc}} \to E_{\text{LUMO, C=O}}$) occurs exclusively at the **carbonyl carbon atom**.

```
       Bürgi-Dunitz Nucleophilic Trajectory:
                  Nu: (-)
                    \  ~107°
                     \
             R1       v
               \     / 
                C = O
               /
             R2
```

### The Bürgi-Dunitz Angle of Attack ($\alpha_{\text{BD}} \approx 107^\circ$)
In 1974, Hans-Beat Bürgi and Jack D. Dunitz mapped the crystallographic coordinates of dozens of crystalline amine-carbonyl donor-acceptor complexes to reconstruct the reaction coordinate of nucleophilic addition.
They discovered that a nucleophile does **not** approach the carbonyl carbon perpendicularly ($90^\circ$) or along the $\text{C}=\text{O}$ axis ($180^\circ$). Instead, it approaches at an angle of:

$$\alpha_{\text{BD}} \approx 107^\circ \pm 2^\circ \tag{2.3}$$

measured relative to the $\text{C}=\text{O}$ bond axis. This precise geometric trajectory is dictated by two competing quantum mechanical factors:
1. **Orbital Overlap Maximization**: The $\pi^*$ antibonding orbital has its largest lobe centered on carbon, canted backward at approximately $105^\circ\text{–}110^\circ$ away from the oxygen atom.
2. **Electrostatic & Pauli Repulsion Minimization**: Approaching at $107^\circ$ minimizes destructive electron-electron repulsion between the filled lone pairs of the incoming nucleophile and the filled bonding $\pi$ and non-bonding lone pair electron clouds on oxygen.

As the nucleophile approaches from $d_{\text{Nu}\cdots\text{C}} = 2.8\text{ \AA}$ to the covalent bonding distance of $1.5\text{ \AA}$, the carbonyl carbon undergoes continuous **pyramidalization**, transitioning smoothly from planar $sp^2$ ($120^\circ$) to tetrahedral $sp^3$ ($109.5^\circ$).""",
                "simulations": ["sim_chem_carbonyl_addition_burgi_dunitz"]
            },
            {
                "id": "sec2_2",
                "secNumber": "§2.2",
                "title": "Reversible Nucleophilic Additions: Hydration, Hemiacetals, Acetals & Protection Chemistry",
                "heading": "Reversible Nucleophilic Additions: Hydration, Hemiacetals, Acetals & Protection Chemistry",
                "content": r"""Nucleophilic addition of oxygen and sulfur nucleophiles to aldehydes and ketones establishes dynamic thermodynamic equilibria governed by steric hindrance and electron-withdrawing capabilities.

### Carbonyl Hydration Equilibria
The reversible addition of water forms *gem*-diols (hydrates):

$$\text{R}_1\text{COR}_2 + \text{H}_2\text{O} \xrightleftharpoons{K_{\text{hyd}}} \text{R}_1\text{C}(\text{OH})_2\text{R}_2 \tag{2.4}$$

The hydration equilibrium constant $K_{\text{hyd}} = \frac{[\text{hydrate}]}{[\text{carbonyl}][\text{H}_2\text{O}]}$ spans ten orders of magnitude:
- **Formaldehyde ($\text{HCHO}$)**: $K_{\text{hyd}} \approx 2000$ ($99.9\%$ hydrated in water). Formaldehyde possesses no electron-donating alkyl groups to stabilize the partial positive charge on carbon.
- **Acetaldehyde ($\text{CH}_3\text{CHO}$)**: $K_{\text{hyd}} \approx 1.0$ ($50\%$ hydrated). One $+I$ methyl group donates electron density.
- **Acetone ($\text{CH}_3\text{COCH}_3$)**: $K_{\text{hyd}} \approx 10^{-3}$ ($0.1\%$ hydrated). Two bulky electron-donating methyl groups destabilize the crowded tetrahedral hydrate.
- **Hexafluoroacetone ($\text{CF}_3\text{COCF}_3$)**: $K_{\text{hyd}} \approx 10^6$. Powerful $-I$ inductive withdrawal by six fluorine atoms makes the carbonyl carbon violently electrophilic.

### Acetal and Ketal Formation Mechanism
Reaction with two equivalents of alcohol (or one equivalent of a 1,2- or 1,3-diol) in the presence of an acid catalyst ($\text{TsOH}, \text{dry HCl}$) yields acetals:

```
Acetal Cascade:
Aldehyde + H+ <---> Protonated Carbonyl
   + ROH <---> Hemiacetal
   + H+ (- H2O) <---> Oxocarbenium Ion [R-CH=O+-R']
   + ROH (- H+) <---> Acetal [R-CH(OR')2]
```

1. Protonation of carbonyl oxygen: $\text{RCHO} + \text{H}^+ \rightleftharpoons \text{RCH}=\text{O}^+\text{H}$.
2. Nucleophilic attack by $\text{R'OH}$ to form a protonated hemiacetal.
3. Deprotonation yields neutral **hemiacetal**.
4. Protonation of the hemiacetal hydroxyl group converts $-\text{OH}$ into a water leaving group ($-\text{OH}_2^+$).
5. Elimination of $\text{H}_2\text{O}$ assisted by the adjacent oxygen lone pair generates a resonance-stabilized **oxocarbenium ion**:
   $$\text{R}-\text{CH}(\text{OR}')-\text{O}^+\text{H}_2 \longrightarrow [\text{R}-\text{CH}=\text{O}^+-\text{R}' \longleftrightarrow \text{R}-\text{C}^+\text{H}-\text{OR}'] + \text{H}_2\text{O}$$
6. Addition of the second alcohol molecule and deprotonation furnishes the **acetal**.

Acetals are completely inert to strong bases, hydride reducing agents ($\text{LiAlH}_4, \text{NaBH}_4$), and organometallic reagents ($\text{RMgX}, \text{RLi}$), making cyclic acetals (such as 1,3-dioxolanes formed with ethylene glycol) indispensable **carbonyl protecting groups**. Deprotection occurs smoothly via aqueous acid hydrolysis.""",
                "simulations": []
            },
            {
                "id": "sec2_3",
                "secNumber": "§2.3",
                "title": "Irreversible Additions: Complex Hydrides, Organometallics & Cyanohydrins",
                "heading": "Irreversible Additions: Complex Hydrides, Organometallics & Cyanohydrins",
                "content": r"""Unlike oxygen addition, nucleophilic additions involving carbon-carbon and carbon-hydrogen bond formation are thermodynamically irreversible or driven by subsequent irreversible quenching.

### Complex Metal Hydride Reductions: $\text{NaBH}_4$ vs $\text{LiAlH}_4$
- **Sodium Borohydride ($\text{NaBH}_4$)**: Mild, chemoselective reducing agent operable in protic solvents ($\text{MeOH}, \text{EtOH}, \text{H}_2\text{O}$). Rapidly reduces aldehydes and ketones to primary and secondary alcohols via a four-center transition state, but does *not* reduce carboxylic acids, esters, or amides under ambient conditions.
- **Lithium Aluminium Hydride ($\text{LiAlH}_4$)**: Powerful, pyrophoric reducing agent that must be handled in anhydrous aprotic ethereal solvents ($\text{Et}_2\text{O}, \text{THF}$). The $\text{Al}-\text{H}$ bond is substantially more polar and nucleophilic than the $\text{B}-\text{H}$ bond. $\text{LiAlH}_4$ rapidly reduces aldehydes, ketones, esters, lactones, carboxylic acids, and nitriles. The lithium cation ($\text{Li}^+$) acts as an essential Lewis acid, coordinating to the carbonyl oxygen to lower the LUMO energy.

### Organometallic Additions: Grignard and Organolithium Reagents
Organomagnesium halides ($\text{RMgX}$) and organolithium reagents ($\text{RLi}$) act as powerful carbon carbanion equivalents ($R^{\delta-}-\text{M}^{\delta+}$):
- **Formaldehyde** $+$ $\text{RMgX} \longrightarrow 1^\circ$ alcohol.
- **Aldehydes** $+$ $\text{RMgX} \longrightarrow 2^\circ$ alcohol.
- **Ketones** $+$ $\text{RMgX} \longrightarrow 3^\circ$ alcohol.

Grignard additions to sterically hindered ketones often suffer from side reactions:
1. **Hydride Transfer / Reduction**: If the Grignard reagent possesses a $\beta$-hydrogen (e.g., isobutylmagnesium bromide), it can undergo a six-membered cyclic transition state transferring a hydride, yielding the reduced alcohol and an alkene.
2. **Enolization**: Strongly hindered ketones with $\alpha$-protons can act as Brønsted acids, protonating the Grignard reagent to produce an enolate salt and alkane gas.""",
                "simulations": []
            },
            {
                "id": "sec2_4",
                "secNumber": "§2.4",
                "title": "Nitrogen Derivatives: Imines, Enamines, Oximes & Hydrazones",
                "heading": "Nitrogen Derivatives: Imines, Enamines, Oximes & Hydrazones",
                "content": r"""Reaction of aldehydes and ketones with primary and secondary nitrogen nucleophiles proceeds via addition-elimination mechanisms to form diverse functional groups with extensive synthetic utility.

### Primary Amines: Imine (Schiff Base) Formation
Addition of a primary amine ($\text{R}'\text{NH}_2$) to a carbonyl compound in the presence of mild acid ($\text{pH} \approx 4.5$) yields an **imine**:

$$\text{R}_2\text{C}=\text{O} + \text{R}'\text{NH}_2 \xrightleftharpoons[\text{pH } 4.5]{-\text{H}_2\text{O}} \text{R}_2\text{C}=\text{N}-\text{R}' \tag{2.5}$$

- At $\text{pH} > 7$, the rate-limiting step is dehydration of the carbinolamine intermediate due to lack of acid catalysis.
- At $\text{pH} < 3$, the amine nucleophile is completely protonated into an unreactive ammonium salt ($\text{R}'\text{NH}_3^+$), suppressing the initial nucleophilic addition step.
- Optimal reaction rates occur at the **rate-maximum buffer zone** around $\text{pH } 4\text{–}5$.

### Secondary Amines: Enamine Formation & Stork Alkylation
Secondary amines ($\text{R}_2'\text{NH}$, such as pyrrolidine, piperidine, morpholine) add to aldehydes or ketones with $\alpha$-protons to form **enamines**:

$$\text{RCH}_2\text{COR}' + \text{R}_2''\text{NH} \xrightleftharpoons[\text{TsOH, Dean-Stark}]{-\text{H}_2\text{O}} \text{RCH}=\text{C}(\text{NR}_2'')\text{R}' \tag{2.6}$$

Because the carbinolamine intermediate derived from a secondary amine possesses no proton on nitrogen, dehydration cannot form a $\text{C}=\text{N}$ double bond. Instead, elimination occurs from the adjacent $\alpha$-carbon, generating an alkene-amine conjugated system (**enamine**).

In **Gilbert Stork's enamine synthesis** (1954), enamines act as neutral enolate equivalents. Resonance delocalizes nitrogen's lone pair into the $\pi$ system, rendering the $\beta$-carbon strongly nucleophilic:

$$\text{R}_2\text{N}-\text{CH}=\text{CH}_2 \longleftrightarrow \text{R}_2\text{N}^+=\text{CH}-\text{C}^-\text{H}_2 \tag{2.7}$$

Alkylation with reactive primary alkyl halides or acylation with acid chlorides occurs smoothly at the $\beta$-carbon without polyalkylation or enolization side reactions. Hydrolysis of the resulting iminium salt restores the carbonyl group, delivering clean $\alpha$-alkylated or $\alpha$-acylated ketones.""",
                "simulations": []
            },
            {
                "id": "sec2_5",
                "secNumber": "§2.5",
                "title": "Carbonyl Deoxygenation & Oxidation: Wolff-Kishner, Clemmensen & Baeyer-Villiger",
                "heading": "Carbonyl Deoxygenation & Oxidation: Wolff-Kishner, Clemmensen & Baeyer-Villiger",
                "content": r"""Transforming a carbonyl group directly into a methylene group ($-\text{C}(=\text{O})- \to -\text{CH}_2-$) or expanding it via oxygen insertion represents two pillars of synthetic transformation.

### 1. The Wolff-Kishner Reduction (Alkaline Conditions)
Ketones and aldehydes react with hydrazine ($\text{NH}_2\text{NH}_2$) in the presence of strong base ($\text{KOH}$) in high-boiling solvents (diethylene glycol or DMSO, $180^\circ\text{–}200^\circ\text{C}$, Huang-Minlon modification) to produce alkanes:

$$\text{R}_1\text{COR}_2 + \text{NH}_2\text{NH}_2 \xrightarrow{\text{KOH, DEG, }195^\circ\text{C}} \text{R}_1\text{CH}_2\text{R}_2 + \text{N}_2\uparrow + \text{H}_2\text{O} \tag{2.8}$$

#### Mechanistic Sequence:
1. Hydrazone formation: $\text{R}_2\text{C}=\text{O} + \text{NH}_2\text{NH}_2 \to \text{R}_2\text{C}=\text{N}-\text{NH}_2 + \text{H}_2\text{O}$.
2. Base deprotonation of the terminal nitrogen gives an anionic diazo species: $[\text{R}_2\text{C}=\text{N}-\text{NH}]^- \leftrightarrow [\text{R}_2\text{C}^--\text{N}=\text{NH}]$.
3. Protonation of the carbanion by solvent yields an alkyl diimide: $\text{R}_2\text{CH}-\text{N}=\text{NH}$.
4. Second deprotonation gives $[\text{R}_2\text{CH}-\text{N}=\text{N}]^-$.
5. Irreversible extrusion of dinitrogen gas ($\text{N}_2\uparrow$, $\Delta S^\circ \gg 0$, $\Delta H^\circ \ll 0$) generates an unstabilized carbanion $[\text{R}_2\text{CH}]^-$, which instantly abstracts a proton from solvent to yield the methylene hydrocarbon $\text{R}_2\text{CH}_2$.

### 2. The Clemmensen Reduction (Acidic Conditions)
Refluxing ketones with amalgamated zinc ($\text{Zn(Hg)}$) and concentrated aqueous hydrochloric acid ($\text{HCl}$) reduces the carbonyl to a methylene unit.
- The reaction occurs heterogeneously on the zinc metal surface via radical-anion organozinc carbene/carbenoid intermediates.
- Ideal for base-sensitive molecules, but unsuitable for acid-sensitive substrates.

### 3. The Baeyer-Villiger Oxidation
Treatment of ketones with peroxy acids ($m\text{CPBA}$, trifluoroperacetic acid $\text{CF}_3\text{CO}_3\text{H}$) oxidizes ketones into **esters** (or cyclic ketones into **lactones**):

```
Baeyer-Villiger Mechanism:
Ketone + R'CO3H ---> "Criegee Intermediate" [R1-C(OH)(OOCCF3)-R2]
                 ---> Migration of R with retention of stereochemistry
                 ---> Ester [R1-COO-R2] + R'COOH
```

1. Addition of peroxy acid to carbonyl carbon forms the tetrahedral **Criegee intermediate**.
2. Decomposition of the Criegee intermediate occurs via concerted migration of one alkyl group to the peroxy oxygen with simultaneous cleavage of the weak $\text{O}-\text{O}$ single bond ($\text{BDE} \approx 140\text{ kJ}\cdot\text{mol}^{-1}$) and departure of the carboxylate leaving group.
3. **Migratory Aptitude Hierarchy**:
   $$\text{tertiary alkyl} > \text{cyclohexyl} > \text{secondary alkyl} \approx \text{benzyl} \approx \text{phenyl} > \text{primary alkyl} > \text{methyl}$$
4. Group migration occurs with **complete retention of stereochemical configuration** at the migrating chiral center.""",
                "simulations": []
            },
            {
                "id": "sec2_6",
                "secNumber": "§2.6",
                "title": "Enol-Enolate Equilibria: Kinetic vs Thermodynamic Enolates",
                "heading": "Enol-Enolate Equilibria: Kinetic vs Thermodynamic Enolates",
                "content": r"""The acidity of protons $\alpha$ to a carbonyl group ($\text{p}K_a \approx 16\text{–}20$) is vastly higher than that of aliphatic hydrocarbons ($\text{p}K_a \approx 50$), arising from resonance delocalization of the negative charge onto the electronegative oxygen atom.

### Kinetic vs Thermodynamic Enolate Regiocontrol
When an unsymmetrical ketone possessing non-equivalent $\alpha$-protons (such as 2-methylcyclohexanone) is deprotonated by base, two distinct regioisomeric enolates can form:

```
                  2-Methylcyclohexanone Regioisomeric Enolates:
                         O                            O(-)
                        //                           /
                       /\CH3    LDA, -78 C          /\CH3
                      |  |     ----------->        |  |  (Less substituted, Kinetic)
                       \/                           \/
                                                    
                                                     O(-)
                                                    /
                                KtBuO, 25 C        /\CH3
                               ----------->       ||  |  (More substituted, Thermodynamic)
                                                   \/
```

1. **The Kinetic Enolate**:
   - Formed by deprotonation at the **less sterically hindered $\alpha$-carbon** (C6).
   - Characterized by lower activation energy: $\Delta G^\ddagger_{\text{kinetic}} < \Delta G^\ddagger_{\text{thermo}}$.
   - Generated selectively using a **strong, bulky, non-nucleophilic base** such as lithium diisopropylamide ($\text{LDA}$) or lithium hexamethyldisilazide ($\text{LiHMDS}$) in anhydrous THF at **$-78^\circ\text{C}$** under conditions of irreversible, rapid deprotonation with no excess ketone present.

2. **The Thermodynamic Enolate**:
   - Formed by deprotonation at the **more substituted $\alpha$-carbon** (C2), yielding the more highly substituted, thermodynamically stable alkene double bond.
   - Characterized by lower ground-state Gibbs free energy: $\Delta G^\circ_{\text{thermo}} < \Delta G^\circ_{\text{kinetic}}$ (stabilized by hyperconjugation, $\Delta \Delta H^\circ \approx 8\text{–}12\text{ kJ}\cdot\text{mol}^{-1}$).
   - Generated using a **weaker, equilibrating base** (such as potassium *tert*-butoxide, $\text{KO}t\text{Bu}$, or sodium ethoxide, $\text{NaOEt}$) at higher temperatures (**$25^\circ\text{–}65^\circ\text{C}$**) with a slight excess of ketone to permit continuous proton exchange and thermodynamic equilibration.""",
                "simulations": []
            },
            {
                "id": "sec2_7",
                "secNumber": "§2.7",
                "title": "Aldol, Claisen-Schmidt, Cannizzaro, Benzoin & Condensation Cascades",
                "heading": "Aldol, Claisen-Schmidt, Cannizzaro, Benzoin & Condensation Cascades",
                "content": r"""Carbonyl condensation reactions represent the premier methodology for constructing complex carbon-carbon frameworks in organic synthesis.

### 1. The Aldol Addition and E1cB Dehydration
Under basic conditions, an enolate attacks a second molecule of aldehyde or ketone to yield a $\beta$-hydroxy carbonyl compound (**aldol addition**). Upon warming or in the presence of acid, spontaneous dehydration occurs to furnish an $\alpha,\beta$-unsaturated carbonyl compound:

$$\text{Aldol Cascade}: \quad 2\,\text{CH}_3\text{CHO} \xrightleftharpoons{\text{OH}^-} \text{CH}_3\text{CH}(\text{OH})\text{CH}_2\text{CHO} \xrightarrow[\Delta]{-\text{H}_2\text{O}} \text{CH}_3\text{CH}=\text{CHCHO} \tag{2.9}$$

Dehydration under basic conditions proceeds via an **$\text{E1cB}$ mechanism** (Elimination Unimolecular conjugate Base):
1. Hydroxide deprotonates the acidic $\alpha$-proton adjacent to the carbonyl, generating a stabilized enolate intermediate.
2. The enolate expels the hydroxide leaving group ($-\text{OH}$) from the $\beta$-position in a unimolecular rate-determining step, driven by the thermodynamic stability of the conjugated enone system.

### 2. Claisen-Schmidt & Knoevenagel Condensations
- **Claisen-Schmidt Condensation**: Crossed aldol condensation between an aromatic aldehyde lacking $\alpha$-hydrogens (e.g., benzaldehyde) and an aliphatic ketone or aldehyde with $\alpha$-hydrogens (e.g., acetophenone), yielding $\alpha,\beta$-unsaturated ketones (chalcones). Because benzaldehyde cannot enolize and its carbonyl is highly electrophilic, a single crossed product is formed in near quantitative yield.
- **Knoevenagel Condensation**: Condensation of aldehydes or ketones with active methylene compounds (such as diethyl malonate or ethyl cyanoacetate) catalyzed by weak bases (piperidine) to yield alkylidene derivatives.

### 3. Cannizzaro, Benzoin & Perkin Reactions
- **Cannizzaro Reaction**: Non-enolizable aldehydes (e.g., benzaldehyde, formaldehyde) treated with concentrated alkali ($50\%\, \text{NaOH}$) undergo intermolecular hydride transfer (redox disproportionation), yielding equimolar quantities of a primary alcohol and a carboxylic acid salt.
- **Benzoin Condensation**: Cyanide- or thiazolium carbene-catalyzed coupling of two molecules of aromatic aldehyde to produce $\alpha$-hydroxy ketones (benzoins). The cyanide ion acts as a unique catalyst: it serves as a nucleophile, stabilizes the carbanionic Breslow intermediate via cyano conjugation, and acts as a leaving group.
- **Perkin Reaction**: Condensation of aromatic aldehydes with acid anhydrides in the presence of the sodium salt of the corresponding acid at $180^\circ\text{C}$ to form $\alpha,\beta$-unsaturated carboxylic acids (e.g., cinnamic acid from benzaldehyde and acetic anhydride).""",
                "simulations": ["sim_chem_aldol_condensation_equilibria"]
            }
        ],
        "problems": [
            {
                "id": "prob2_1",
                "problemNumber": "2.1",
                "title": "Derivation of the Bürgi-Dunitz Angle from Frontier Orbital Overlap",
                "difficulty": "Mastery",
                "statement": r"""Consider the nucleophilic addition of a generic hydride donor $\text{H}^-$ to formaldehyde ($\text{H}_2\text{C}=\text{O}$). 
(a) Write the mathematical LCAO expression for the carbonyl LUMO ($\pi^*$) and explain why the orbital coefficient at carbon ($c_{\text{C}}^*$) is larger in magnitude than that at oxygen ($c_{\text{O}}^*$).
(b) Derive why the angle of approach $\theta$ that maximizes the overlap integral $S = \langle \phi_{\text{Nuc}} | \psi_{\pi^*} \rangle$ while minimizing Coulombic repulsion with oxygen's filled lone pairs deviates from $90^\circ$ toward $107^\circ$.
(c) How does changing the carbonyl substituent from hydrogen to bulky *tert*-butyl groups affect the approach trajectory?""",
                "hints": ["Express the overlap integral as a function of angle $\theta$.", "Pauli repulsion acts as a repulsive potential $V_{\text{rep}} \propto \frac{1}{r^6}$ from the oxygen lone pair."],
                "solution": r"""### (a) Orbital Coefficient Derivation
In secular perturbation theory, two atomic orbitals $\chi_1 (2p_{z,\text{C}})$ and $\chi_2 (2p_{z,\text{O}})$ with onsite Coulomb energies $\alpha_{\text{C}} > \alpha_{\text{O}}$ (since oxygen is more electronegative) and resonance integral $\beta < 0$ mix to form bonding and antibonding orbitals:
$$\psi_{\pi} = c_{\text{C}} \chi_{\text{C}} + c_{\text{O}} \chi_{\text{O}}, \quad \psi_{\pi^*} = c_{\text{C}}^* \chi_{\text{C}} - c_{\text{O}}^* \chi_{\text{O}}$$
By solving the $2 \times 2$ secular determinant:
$$\begin{vmatrix} \alpha_{\text{C}} - E & \beta \\ \beta & \alpha_{\text{O}} - E \end{vmatrix} = 0$$
For the lower bonding state, the eigenvector aligns with the lower atomic orbital: $c_{\text{O}} > c_{\text{C}}$. By orthogonality $\langle \psi_\pi | \psi_{\pi^*} \rangle = 0$:
$$c_{\text{C}} c_{\text{C}}^* - c_{\text{O}} c_{\text{O}}^* = 0 \implies \frac{c_{\text{C}}^*}{c_{\text{O}}^*} = \frac{c_{\text{O}}}{c_{\text{C}}} > 1$$
Thus, $|c_{\text{C}}^*| > |c_{\text{O}}^*|$. The antibonding LUMO ($\pi^*$) has its largest spatial lobe on the carbon atom.

### (b) Geometric Vector Derivation of the $107^\circ$ Angle
Let the $\text{C}=\text{O}$ bond lie along the $x$-axis with carbon at the origin $(0,0)$ and oxygen at $(d_{\text{CO}}, 0)$.
The $2p_z$ orbital lobes on carbon extend along the $z$-axis ($90^\circ$).
However, mixing of carbon $2s$ character into $\pi^*$ during pyramidalization cants the rear orbital lobe backward away from oxygen.
The total interaction potential $V_{\text{total}}(\theta)$ governing the approaching nucleophile at distance $r$ is:
$$V_{\text{total}}(\theta) = - \frac{2 \beta_{\text{Nu-C}} S(\theta)}{E_{\text{LUMO}} - E_{\text{HOMO}}} + \frac{C_{\text{rep}}}{[r^2 + d_{\text{CO}}^2 - 2 r d_{\text{CO}} \cos(180^\circ - \theta)]^3}$$
1. If $\theta = 90^\circ$, orbital overlap with the pure $2p_z$ lobe is substantial, but Coulomb and exchange repulsion with the oxygen lone pairs at distance $d_{\text{Nu-O}} = \sqrt{r^2 + d_{\text{CO}}^2}$ is high.
2. Tilting the trajectory backward ($\theta > 90^\circ$) increases the distance to oxygen:
   $$d_{\text{Nu-O}}(\theta) = \sqrt{r^2 + d_{\text{CO}}^2 + 2 r d_{\text{CO}} \cos\theta}$$
3. Minimizing $V_{\text{total}}$ with respect to $\theta$ yields the energetic optimum at:
   $$\frac{\partial V_{\text{total}}}{\partial \theta} = 0 \implies \theta_{\text{BD}} \approx 107^\circ$$

### (c) Influence of Bulky Substituents (Félkin-Anh Model)
Bulky *tert*-butyl groups create steric crowding in the quadrant opposite oxygen. The incoming nucleophile must navigate between minimizing steric clash with $t\text{-Bu}$ while avoiding oxygen repulsion, causing the trajectory to adopt an obtuse angle tilted slightly toward $110^\circ\text{–}112^\circ$."""
            },
            {
                "id": "prob2_2",
                "problemNumber": "2.2",
                "title": "Thermodynamics of Carbonyl Protection: Cyclic Acetal vs Acyclic Acetal Formation",
                "difficulty": "Intermediate",
                "statement": r"""When cyclohexanone is reacted with ethylene glycol in benzene with catalytic $\text{TsOH}$ and a Dean-Stark water separator, the cyclic 1,3-dioxolane is obtained in $98\%$ yield. However, when cyclohexanone is reacted with two equivalents of ethanol under identical conditions without continuous water removal, the diethyl ketal yield is less than $15\%$.
(a) Write balanced chemical equations for both reactions.
(b) Evaluate the thermodynamic parameters ($\Delta H^\circ$ and $\Delta S^\circ$) responsible for this dramatic difference.
(c) Explain the operational role of the Dean-Stark trap in shifting Le Chatelier's equilibrium.""",
                "hints": ["Count the number of reactant molecules versus product molecules.", "Consider the chelate effect in cyclic acetal formation."],
                "solution": r"""### (a) Balanced Chemical Equations
1. **Cyclic Acetal (Ethylene Glycol)**:
   $$\text{C}_6\text{H}_{10}\text{O} + \text{HOCH}_2\text{CH}_2\text{OH} \xrightleftharpoons{\text{TsOH}} \text{C}_6\text{H}_{10}\text{O}_2\text{C}_2\text{H}_4 (\text{cyclic ketal}) + \text{H}_2\text{O}$$
   (2 moles of reactants $\rightleftharpoons$ 2 moles of products)

2. **Acyclic Acetal (Ethanol)**:
   $$\text{C}_6\text{H}_{10}\text{O} + 2\,\text{CH}_3\text{CH}_2\text{OH} \xrightleftharpoons{\text{TsOH}} \text{C}_6\text{H}_{10}(\text{OCH}_2\text{CH}_3)_2 + \text{H}_2\text{O}$$
   (3 moles of reactants $\rightleftharpoons$ 2 moles of products)

### (b) Thermodynamic Analysis: The Chelate Effect
For ketal formation from ketones:
- The enthalpic change $\Delta H^\circ$ is slightly unfavorable or near zero ($\Delta H^\circ \approx +5\text{ to }+10\text{ kJ}\cdot\text{mol}^{-1}$) because a strong carbonyl $\text{C}=\text{O}$ double bond ($\sim 745\text{ kJ}\cdot\text{mol}^{-1}$) is converted into two $\text{C}-\text{O}$ single bonds ($2 \times 360 = 720\text{ kJ}\cdot\text{mol}^{-1}$), and steric congestion increases in the tetrahedral ketal.
- **For Ethanol**: 3 molecules condense into 2 molecules, resulting in an unfavorable decrease in translational entropy:
  $$\Delta S^\circ_{\text{acyclic}} \approx -120\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \implies -T\Delta S^\circ \approx +36\text{ kJ}\cdot\text{mol}^{-1} \text{ at } 298\text{ K}$$
  Thus, $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ \gg 0$, giving an equilibrium constant $K_{\text{eq}} \ll 1$.
- **For Ethylene Glycol**: 2 molecules condense into 2 molecules. The loss of translational entropy is negligible ($\Delta S^\circ_{\text{cyclic}} \approx 0$). Once the first hydroxyl group adds, the second ring-closing intramolecular attack is entropically favored (the chelate effect), making $\Delta G^\circ$ close to zero.

### (c) Dean-Stark Water Removal
In benzene ($T_b = 80^\circ\text{C}$), water forms a minimum-boiling ternary azeotrope. The azeotropic vapor condenses in the Dean-Stark trap, where water separates into the lower layer due to immiscibility and higher density ($\rho = 1.00\text{ g/cm}^3$ vs $\rho_{\text{benzene}} = 0.88\text{ g/cm}^3$). Removing $[\text{H}_2\text{O}]$ continuously drives the reaction to completion according to Le Chatelier's principle."""
            },
            {
                "id": "prob2_3",
                "problemNumber": "2.3",
                "title": "Stereoselective Migratory Aptitude in the Baeyer-Villiger Oxidation",
                "difficulty": "Advanced",
                "statement": r"""Predict the major organic product when (R)-2-phenylcyclohexanone is treated with meta-chloroperoxybenzoic acid (mCPBA) in dichloromethane at room temperature.
(a) Draw the complete mechanism showing the tetrahedral Criegee intermediate.
(b) Predict which group migrates (the secondary C6 methylene vs the tertiary benzylic C2 methine) and justify based on carbocation-stabilizing capability.
(c) State the absolute configuration (R or S) at the stereocenter in the resulting lactone product.""",
                "hints": ["Compare the migratory aptitudes of tertiary/benzylic versus secondary carbons.", "Remember that the migrating group retains its stereochemistry."],
                "solution": r"""### (a) Reaction Mechanism & Criegee Intermediate
1. Nucleophilic attack of $m\text{CPBA}$ onto the carbonyl carbon of (R)-2-phenylcyclohexanone:
   $$\text{Ketone} + m\text{Cl-C}_6\text{H}_4\text{CO}_3\text{H} \rightleftharpoons \text{Criegee Intermediate}$$
   The intermediate is a tetrahedral hemoperoxyketal: the carbonyl carbon is bonded to $-\text{OH}$, $-\text{O}-\text{O}-\text{CO}-\text{Ar}$, C6 ($-\text{CH}_2-$), and C2 ($-\text{CH}(\text{Ph})-$).

### (b) Regiochemical Migration
In the transition state for migration, the migrating bond breaks heterolytically, developing substantial partial positive charge ($\delta+$) on the migrating carbon:
$$\text{Transition State}: \quad [\text{C}_{\text{carbonyl}} \cdots \text{R}^{\delta+} \cdots \text{O} \cdots \text{O}^{\delta-}-\text{COAr}]^\ddagger$$
- C2 is a **secondary benzylic stereocenter** flanked by an electron-rich phenyl ring capable of resonance delocalization.
- C6 is a simple secondary alkyl methylene group.
Because a benzylic center can stabilize carbocation-like character far more effectively than a simple secondary alkyl group:
$$\text{Migratory Aptitude}: \quad \text{C2 (benzylic)} \gg \text{C6 (secondary alkyl)}$$
Oxygen inserts regioselectively between the carbonyl carbon (C1) and the chiral benzylic center (C2), yielding a 7-membered **$\epsilon$-lactone** (oxepan-2-one derivative).

### (c) Stereochemical Outcome: Complete Retention
Migration occurs concertedly via a three-center two-electron frontside transition state. The migrating C2 center never becomes a free planar carbocation. Consequently, migration proceeds with **100% retention of configuration**.
Assigning CIP priority to the product (7-phenyl-oxepan-2-one):
1. $-\text{O}-$ (oxygen of lactone ring, priority 1)
2. $-\text{C}_6\text{H}_5$ (phenyl ring, priority 2)
3. $-\text{CH}_2-$ (C3 of ring, priority 3)
4. $-\text{H}$ (hydrogen, priority 4)
Because the relative spatial priority changes with oxygen insertion directly attached to the chiral center, the stereocenter is designated as **(R)-7-phenyloxepan-2-one**."""
            },
            {
                "id": "prob2_4",
                "problemNumber": "2.4",
                "title": "Regioselective Kinetic vs Thermodynamic Alkylation of 2-Methylcyclohexanone",
                "difficulty": "Mastery",
                "statement": r"""Provide reaction conditions to convert 2-methylcyclohexanone selectively into:
(a) 2,6-dimethylcyclohexanone (predominantly trans)
(b) 2,2-dimethylcyclohexanone
Detail the base, solvent, temperature, counterion, and mechanistic rationale for each transformation, and draw the enolate transition states.""",
                "hints": ["Which isomer represents the kinetic enolate?", "Which isomer represents the thermodynamic enolate?"],
                "solution": r"""### (a) Synthesis of 2,6-Dimethylcyclohexanone (Kinetic Pathway)
To achieve alkylation at the less hindered C6 position:
1. **Reagents**: Lithium diisopropylamide ($\text{LDA}$, 1.05 equiv) in anhydrous $\text{THF}$ at **$-78^\circ\text{C}$**.
2. **Procedure**: Add 2-methylcyclohexanone dropwise to a cold solution of $\text{LDA}$ over 15 minutes. Stir for 30 minutes, then add methyl iodide ($\text{CH}_3\text{I}$, 1.2 equiv). Warm slowly to room temperature.
3. **Mechanistic Rationale**:
   - $\text{LDA}$ is an extremely bulky, strongly basic amine anion ($\text{p}K_a \approx 36$). Steric clash between the isopropyl groups of $\text{LDA}$ and the C2 methyl group prevents deprotonation at C2.
   - Deprotonation occurs rapidly at the unhindered C6 position ($k_{\text{C6}} \gg k_{\text{C2}}$). At $-78^\circ\text{C}$ in aprotic THF, proton exchange between enolate and unreacted ketone is completely suppressed, trapping the **kinetic enolate** (lithium 6-methylcyclohex-1-en-1-olate).
   - $S_N2$ attack on $\text{CH}_3\text{I}$ yields 2,6-dimethylcyclohexanone. Equatorial approach of the electrophile yields predominantly the thermodynamically stable *trans*-isomer.

### (b) Synthesis of 2,2-Dimethylcyclohexanone (Thermodynamic Pathway)
To achieve alkylation at the more substituted C2 position:
1. **Reagents**: Potassium *tert*-butoxide ($\text{KO}t\text{Bu}$) or sodium ethoxide ($\text{NaOEt}$) in *tert*-butanol or ethanol at **$25^\circ\text{–}60^\circ\text{C}$**.
2. **Procedure**: Mix 2-methylcyclohexanone with $0.95$ equivalents of base at room temperature to establish equilibrium, then add $\text{CH}_3\text{I}$.
3. **Mechanistic Rationale**:
   - The thermodynamic enolate (1-methylcyclohex-1-en-1-olate) features a tetrasubstituted enol double bond, which is stabilized by hyperconjugation and alkyl substitution ($\Delta G^\circ \approx 8\text{ kJ}\cdot\text{mol}^{-1}$ lower than the kinetic isomer).
   - Under equilibrating conditions (protic solvent, moderate temperature, presence of conjugate acid), the kinetic enolate rapidly reprotonates until the thermodynamic enolate dominates ($>90\%$).
   - Subsequent $S_N2$ reaction with $\text{CH}_3\text{I}$ produces 2,2-dimethylcyclohexanone."""
            },
            {
                "id": "prob2_5",
                "problemNumber": "2.5",
                "title": "Mechanistic Proof of the Cannizzaro Disproportionation Cascade",
                "difficulty": "Mastery",
                "statement": r"""When benzaldehyde is treated with concentrated sodium hydroxide in heavy water ($\text{D}_2\text{O}$), benzyl alcohol and sodium benzoate are isolated.
(a) When the isolated benzyl alcohol is analyzed by mass spectrometry and $^1\text{H}$ NMR, does it contain deuterium bound to carbon ($-\text{CH}_2\text{OH}$ vs $-\text{CH}\text{D}\text{OH}$)?
(b) Write the step-by-step kinetic derivation showing why the rate law is second-order in benzaldehyde and second-order in hydroxide ion at very high base concentration:
$$\text{Rate} = k_{\text{obs}} [\text{PhCHO}]^2 [\text{OH}^-]^2$$
(c) Explain what chemical feature prevents acetaldehyde from undergoing the Cannizzaro reaction.""",
                "hints": ["Where does the transferring hydride originate?", "At high base concentrations, a dianion intermediate forms."],
                "solution": r"""### (a) Isotopic Hydride Transfer & Absence of Carbon-Bound Deuterium
The isolated benzyl alcohol contains **zero deuterium bound to carbon** ($\text{PhCH}_2\text{OD}$).
- The two hydrogens on the benzylic methylene carbon ($-\text{CH}_2-$) originate exclusively from:
  1. The formyl hydrogen of the first benzaldehyde molecule.
  2. The formyl hydrogen of the second benzaldehyde molecule transferred directly as a hydride ($\text{H}^-$).
- The solvent ($\text{D}_2\text{O}$) provides deuterium only to the hydroxyl oxygen ($-\text{OD}$) upon workup.
This provides definitive experimental proof of **direct intermolecular hydride transfer** without involvement of solvent protons.

### (b) Kinetic Derivation of Fourth-Order Rate Law
At extremely high hydroxide concentrations ($>3\text{ M}$):
1. **First Equilibrium**: Rapid addition of hydroxide to benzaldehyde:
   $$\text{PhCHO} + \text{OH}^- \xrightleftharpoons{K_1} \text{PhCH}(\text{OH})\text{O}^- \quad (\text{monoanion})$$
2. **Second Equilibrium**: Deprotonation of the hydroxyl group by a second hydroxide ion:
   $$\text{PhCH}(\text{OH})\text{O}^- + \text{OH}^- \xrightleftharpoons{K_2} \text{PhCH}(\text{O}^-)_2 + \text{H}_2\text{O} \quad (\text{dianion})$$
   The concentration of the dianion is:
   $$[\text{dianion}] = K_1 K_2 [\text{PhCHO}][\text{OH}^-]^2$$
3. **Rate-Determining Step**: Intermolecular hydride transfer from the electron-rich dianion to a neutral benzaldehyde molecule:
   $$\text{PhCH}(\text{O}^-)_2 + \text{PhCHO} \xrightarrow{k_3} \text{PhCOO}^- + \text{PhCH}_2\text{O}^-$$
   The rate of product formation is:
   $$\text{Rate} = k_3 [\text{dianion}][\text{PhCHO}] = k_3 K_1 K_2 [\text{PhCHO}]^2 [\text{OH}^-]^2$$
   Setting $k_{\text{obs}} = k_3 K_1 K_2$, we obtain the experimental fourth-order rate law:
   $$\text{Rate} = k_{\text{obs}} [\text{PhCHO}]^2 [\text{OH}^-]^2$$

### (c) Acetaldehyde Contrast
Acetaldehyde possesses acidic $\alpha$-hydrogens ($\text{p}K_a \approx 17$). Treatment with hydroxide results in instantaneous enolization and subsequent aldol condensation ($k_{\text{aldol}} \gg 10^5 \times k_{\text{Cannizzaro}}$), completely precluding the Cannizzaro pathway."""
            },
            {
                "id": "prob2_6",
                "problemNumber": "2.6",
                "title": "Stork Enamine Synthesis vs Direct Ketone Alkylation",
                "difficulty": "Intermediate",
                "statement": r"""A chemist wishes to synthesize 2-allylcyclopentanone from cyclopentanone and allyl bromide.
(a) Why does direct alkylation of cyclopentanone enolate (using $\text{NaH}$ or $\text{KO}t\text{Bu}$) result in poor yields with significant 2,5-diallylcyclopentanone and 2,2-diallylcyclopentanone side products?
(b) Provide the complete synthetic sequence utilizing pyrrolidine via the Stork enamine methodology.
(c) Explain why enamines resist polyalkylation.""",
                "hints": ["Consider proton exchange between monoalkylated product and unreacted enolate.", "Enamine monoalkylation yields an iminium salt."],
                "solution": r"""### (a) Complications in Direct Alkylation
When cyclopentanone is deprotonated with a base like $\text{NaH}$, the monoalkylated product (2-allylcyclopentanone) is formed. However:
- The monoalkylated ketone still possesses acidic $\alpha$-hydrogens at C2 and C5.
- Rapid proton exchange occurs between the newly formed 2-allylcyclopentanone and the remaining cyclopentanone enolate:
  $$\text{Enolate} + \text{2-allylcyclopentanone} \rightleftharpoons \text{Cyclopentanone} + \text{Monoalkylated enolate}$$
- The monoalkylated enolate undergoes secondary alkylation, leading to an intractable mixture of unreacted starting material, monoalkylated ketone, 2,2-diallylcyclopentanone, and 2,5-diallylcyclopentanone.

### (b) Stork Enamine Route
$$\begin{aligned}
\text{Step 1}: &\quad \text{Cyclopentanone} + \text{Pyrrolidine} \xrightarrow{\text{catalytic TsOH, benzene, Dean-Stark, reflux}} \text{1-(cyclopenten-1-yl)pyrrolidine} + \text{H}_2\text{O}\uparrow \\
\text{Step 2}: &\quad \text{1-(cyclopenten-1-yl)pyrrolidine} + \text{CH}_2=\text{CHCH}_2\text{Br} \xrightarrow{\text{acetonitrile, }25^\circ\text{C}} \text{Iminium bromide salt} \\
\text{Step 3}: &\quad \text{Iminium salt} \xrightarrow{\text{H}_2\text{O}, \text{dilute HCl, }25^\circ\text{C}} \text{2-allylcyclopentanone} + \text{Pyrrolidine}\cdot\text{HCl}
\end{aligned}$$

### (c) Suppression of Polyalkylation
In the Stork enamine reaction, alkylation of the enamine at the nucleophilic $\beta$-carbon yields an **iminium bromide salt**:
$$[\text{Pyrrolidine}^+=\text{C}(\text{ring})-\text{CH}_2\text{CH}=\text{CH}_2] \,\, \text{Br}^-$$
Because the nitrogen is now quaternized and positively charged, it possesses no unshared lone pair and **cannot act as an enamine nucleophile**. It precipitates or remains unreactive in solution until aqueous workup. Polyalkylation is fundamentally impossible."""
            },
            {
                "id": "prob2_7",
                "problemNumber": "2.7",
                "title": "Benzoin Condensation: Unique Catalytic Role of Cyanide",
                "difficulty": "Mastery",
                "statement": r"""The cyanide ion ($\text{CN}^-$) uniquely catalyzes the condensation of two molecules of benzaldehyde to form benzoin (2-hydroxy-1,2-diphenylethan-1-one).
(a) Draw the complete curved-arrow mechanism for the benzoin condensation.
(b) Identify the intermediate that undergoes "umpolung" (polarity inversion) and explain how the cyano group stabilizes the acyl carbanion.
(c) Why can other good nucleophiles like iodide ($\text{I}^-$) or hydroxide ($\text{OH}^-$) not catalyze this reaction?""",
                "hints": ["Recall the three unique chemical attributes required of the catalyst in the benzoin condensation.", "Umpolung converts the normally electrophilic carbonyl carbon into a nucleophilic carbanion."],
                "solution": r"""### (a) Reaction Mechanism
$$\begin{aligned}
\text{Step 1}: &\quad \text{PhCHO} + \text{CN}^- \rightleftharpoons \text{PhCH}(\text{O}^-)\text{CN} \quad (\text{Cyanohydrin alkoxide}) \\
\text{Step 2}: &\quad \text{PhCH}(\text{O}^-)\text{CN} \rightleftharpoons \text{PhC}^-(\text{OH})\text{CN} \quad (\text{Breslow carbanion intermediate, proton transfer}) \\
\text{Step 3}: &\quad \text{PhC}^-(\text{OH})\text{CN} + \text{PhCHO} \rightleftharpoons \text{PhCH(OH)-C(Ph)(O}^-)\text{CN} \quad (\text{C-C bond formation}) \\
\text{Step 4}: &\quad \text{Proton transfer}: \quad \text{PhCH(O}^-)\text{-C(Ph)(OH)CN} \\
\text{Step 5}: &\quad \text{Elimination of catalyst}: \quad \text{PhCH(OH)-CO-Ph} + \text{CN}^-
\end{aligned}$$

### (b) Umpolung & Resonance Stabilization
Normally, the carbonyl carbon is strongly electrophilic ($\delta+$).
In **Step 2**, upon addition of $\text{CN}^-$ and subsequent proton shift from carbon to oxygen, the benzylic carbon becomes a **carbanion** ($\text{PhC}^-(\text{OH})\text{CN}$).
The cyano group stabilizes this carbanion through powerful $-M$ resonance:
$$\text{Ph}-\text{C}^-(\text{OH})-\text{C}\equiv\text{N} \longleftrightarrow \text{Ph}-\text{C}(\text{OH})=\text{C}=\text{N}^-$$
In addition, the phenyl ring provides extensive benzylic delocalization. The polarity of the carbonyl carbon is thus inverted (**umpolung**) from an electrophile to a potent nucleophile capable of attacking a second aldehyde carbonyl.

### (c) Why Cyanide Is Unique
A successful catalyst for the benzoin condensation must possess three distinct properties:
1. **Good nucleophilicity**: To attack the carbonyl carbon under mild conditions.
2. **Strong electron-withdrawing/resonance capability**: To acidify the benzylic proton and stabilize the resulting carbanion via delocalization.
3. **Good leaving-group ability**: To be expelled cleanly in the final step to regenerate the carbonyl group.
- **Hydroxide ($\text{OH}^-$)**: Good nucleophile, but poor leaving group compared to alkoxide, and cannot stabilize a carbanion via $\pi$-resonance.
- **Iodide ($\text{I}^-$)**: Excellent leaving group, but poor nucleophile toward hard carbonyl carbons, and lacks low-lying $\pi^*$ orbitals to stabilize a carbanion."""
            }
        ]
    }

def get_unit_3():
    return {
        "id": "unit3",
        "unitId": "unit3-org2",
        "number": 3,
        "unitNumber": 3,
        "title": "Unit 3: Carboxylic Acids, Hydroxy Acids, Unsaturated Acids & Keto Acids",
        "description": "Comprehensive physical organic study of carboxylic acids and multifunctional organic acids: thermodynamic resonance stabilization of carboxylate anions, field and inductive effects, Hammett linear free-energy equations, Hell-Volhard-Zelinsky alpha-halogenation; hydroxy acids and stereospecific lactide/lactone ring closures; alpha,beta-unsaturated acids and geometric cis/trans stereoisomerism (maleic vs fumaric acid); and keto acids, biochemical decarboxylations, and acetoacetic ester cascades.",
        "leadSummary": "Advanced physical organic analysis of carboxyl thermodynamics, Hammett electronic parameters, Hell-Volhard-Zelinsky bromination, hydroxy acid lactonization dynamics, olefinic dicarboxylic acid stereochemistry, and keto acid thermal decarboxylation pathways.",
        "simulations": [],
        "sections": [
            {
                "id": "sec3_1",
                "secNumber": "§3.1",
                "title": "Electronic Structure, Carboxylate Resonance & Acidity Dynamics",
                "heading": "Electronic Structure, Carboxylate Resonance & Acidity Dynamics",
                "content": r"""Carboxylic acids ($-\text{COOH}$) are characterized by extraordinary Brønsted acidity ($\text{p}K_a \approx 3\text{–}5$) compared to aliphatic alcohols ($\text{p}K_a \approx 16\text{–}18$), reflecting an acidity enhancement factor greater than $10^{12}$.

### Quantum Mechanics of Carboxylate Resonance Stabilization
Deprotonation of a carboxylic acid generates the carboxylate anion ($-\text{COO}^-$):

$$\text{RCOOH} + \text{H}_2\text{O} \xrightleftharpoons{K_a} \text{RCOO}^- + \text{H}_3\text{O}^+ \tag{3.1}$$

The exceptional stability of the carboxylate anion arises from **degenerate resonance delocalization**:

```
Carboxylate Anion Degenerate Resonance:
      O                  O(-)                 O---(1/2-)
     //                 /                    /
  R-C        <--->   R-C         ===>     R-C
     \                  \\                   \
      O(-)               O                    O---(1/2-)
```

1. The two canonical Lewis structures are identical in energy (degenerate).
2. X-ray crystallographic and microwave spectroscopic measurements show that both carbon-oxygen bonds in sodium formate are strictly identical: $R_{\text{C-O}} = 1.25\text{ \AA}$ (intermediate between a localized double bond $1.20\text{ \AA}$ and a single bond $1.34\text{ \AA}$).
3. In molecular orbital theory, three parallel $2p_z$ atomic orbitals (one from carbon, two from the oxygens) combine to form a three-center four-electron ($3c\text{–}4e$) $\pi$ system:
   $$\psi_1 = c_1 (2p_{\text{O1}}) + c_2 (2p_{\text{C}}) + c_3 (2p_{\text{O2}}) \quad (\text{bonding, lowest energy, occupied by } 2e^-)$$
   $$\psi_2 = \frac{1}{\sqrt{2}} (2p_{\text{O1}} - 2p_{\text{O2}}) \quad (\text{non-bonding, occupied by } 2e^-)$$
   $$\psi_3 = c_1' (2p_{\text{O1}}) - c_2' (2p_{\text{C}}) + c_3' (2p_{\text{O2}}) \quad (\text{antibonding, unoccupied})$$
4. The negative charge is evenly divided between the two electronegative oxygen atoms ($\delta = -0.5$ on each oxygen), greatly stabilizing the conjugate base and shifting the dissociation equilibrium to the right.""",
                "simulations": []
            },
            {
                "id": "sec3_2",
                "secNumber": "§3.2",
                "title": "Substituent Effects & the Hammett Linear Free-Energy Relationship",
                "heading": "Substituent Effects & the Hammett Linear Free-Energy Relationship",
                "content": r"""The acidity of carboxylic acids responds sensitively to electron-withdrawing and electron-donating substituents via inductive (through-bond), field (through-space), and resonance effects.

### Aliphatic Halogenated Acids & Inductive Distance Attenuation
Halogen substitution on acetic acid dramatically lowers $\text{p}K_a$:
- **Acetic acid ($\text{CH}_3\text{COOH}$)**: $\text{p}K_a = 4.76$
- **Monochloroacetic acid ($\text{CH}_2\text{ClCOOH}$)**: $\text{p}K_a = 2.86$
- **Dichloroacetic acid ($\text{CHCl}_2\text{COOH}$)**: $\text{p}K_a = 1.29$
- **Trichloroacetic acid ($\text{CCl}_3\text{COOH}$)**: $\text{p}K_a = 0.65$
- **Trifluoroacetic acid ($\text{CF}_3\text{COOH}$)**: $\text{p}K_a = 0.23$

The inductive effect falls off precipitously with distance through the $\sigma$-framework:
- 2-Chlorobutanoic acid ($\alpha$-substituted): $\text{p}K_a = 2.84$
- 3-Chlorobutanoic acid ($\beta$-substituted): $\text{p}K_a = 4.06$
- 4-Chlorobutanoic acid ($\gamma$-substituted): $\text{p}K_a = 4.52$
- Butanoic acid (unsubstituted): $\text{p}K_a = 4.82$

### The Hammett Equation: $\sigma$ Constants and $\rho$ Reaction Constants
In 1937, Louis Plack Hammett defined a quantitative linear free-energy relationship (LFER) correlating the ionization of meta- and para-substituted benzoic acids:

$$\log \left(\frac{K_a}{K_0}\right) = \sigma \cdot \rho \tag{3.2}$$

where:
- $K_0$ is the acid dissociation constant of unsubstituted benzoic acid in water at $25^\circ\text{C}$ ($\text{p}K_0 = 4.20$).
- $K_a$ is the dissociation constant of the substituted benzoic acid.
- **$\sigma$ (Substituent Constant)**: Defined as $\sigma_X \equiv \log K_X - \log K_0$. Measures the total electronic donor/acceptor ability of substituent $X$:
  - $\sigma > 0$: Electron-withdrawing group ($-\text{NO}_2, -\text{CN}, -\text{CF}_3$), increases acidity.
  - $\sigma < 0$: Electron-donating group ($-\text{OMe}, -\text{NH}_2, -\text{Me}$), decreases acidity.
- **$\rho$ (Reaction Constant)**: For benzoic acid ionization in water at $25^\circ\text{C}$, $\rho \equiv 1.00$ by definition. Reactions with $\rho > 0$ develop negative charge in the transition state/product; reactions with $\rho < 0$ develop positive charge.""",
                "simulations": []
            },
            {
                "id": "sec3_3",
                "secNumber": "§3.3",
                "title": "Industrial & Laboratory Syntheses of Carboxylic Acids",
                "heading": "Industrial & Laboratory Syntheses of Carboxylic Acids",
                "content": r"""The primary synthetic pathways to carboxylic acids involve oxidative cleavage, carbonation of organometallics, and nitrile solvolysis.

### 1. Carbonation of Grignard and Organolithium Reagents
Reaction of alkyl or arylmagnesium halides with solid carbon dioxide (dry ice) provides a general method for lengthening a carbon chain by one carbon:

$$\text{R-MgX} + \text{CO}_2 \xrightarrow{\text{Et}_2\text{O}, -78^\circ\text{C}} \text{R-COO}^-\text{MgX}^+ \xrightarrow{\text{H}_3\text{O}^+} \text{R-COOH} + \text{Mg}^{2+} + \text{X}^- \tag{3.3}$$

Nucleophilic addition of the carbanion to electrophilic $\text{CO}_2$ forms a resonance-stabilized carboxylate magnesium salt, which is completely unreactive toward further nucleophilic attack, preventing tertiary alcohol over-addition.

### 2. Hydrolysis of Nitriles
Alkyl halides undergo $S_N2$ displacement with cyanide ion to yield nitriles, which are subsequently hydrolyzed under acidic or basic conditions:
- **Acidic Hydrolysis**:
  $$\text{R-C}\equiv\text{N} + 2\,\text{H}_2\text{O} + \text{H}^+ \xrightarrow{\Delta} \text{R-COOH} + \text{NH}_4^+$$
- **Basic Hydrolysis**:
  $$\text{R-C}\equiv\text{N} + \text{H}_2\text{O} + \text{OH}^- \xrightarrow{\Delta} \text{R-COO}^- + \text{NH}_3\uparrow \xrightarrow{\text{H}_3\text{O}^+} \text{R-COOH}$$

### 3. Industrial Monsanto & Cativa Acetic Acid Syntheses
The global industrial manufacture of acetic acid ($>15\text{ million metric tons/year}$) relies on the **Monsanto process** (rhodium catalyst, $[\text{Rh}(\text{CO})_2\text{I}_2]^-$) and the modern **Cativa process** (iridium catalyst, $[\text{Ir}(\text{CO})_2\text{I}_2]^-$):

$$\text{CH}_3\text{OH} + \text{CO} \xrightarrow{[\text{Ir}(\text{CO})_2\text{I}_2]^-, \text{Ru promoter}, 190^\circ\text{C}, 30\text{ bar}} \text{CH}_3\text{COOH} \tag{3.4}$$

The catalytic cycle involves oxidative addition of methyl iodide ($\text{CH}_3\text{I}$) to the square planar metal complex, migratory CO insertion to form an acyl-metal species, and reductive elimination of acetyl iodide, which undergoes instant hydrolysis to regenerate $\text{HI}$ and acetic acid.""",
                "simulations": []
            },
            {
                "id": "sec3_4",
                "secNumber": "§3.4",
                "title": "The Hell-Volhard-Zelinsky (HVZ) $\alpha$-Halogenation Mechanism",
                "heading": "The Hell-Volhard-Zelinsky (HVZ) $\alpha$-Halogenation Mechanism",
                "content": r"""Unlike aldehydes and ketones, carboxylic acids do not undergo direct $\alpha$-bromination when treated with elemental bromine because carboxylic acids exist overwhelmingly in the un-enolized carboxyl form with negligible enol equilibrium concentrations ($K_{\text{enol}} < 10^{-12}$).

The **Hell-Volhard-Zelinsky (HVZ) reaction** overcomes this barrier by introducing a catalytic quantity of phosphorus tribromide ($\text{PBr}_3$) or red phosphorus:

$$\text{R-CH}_2-\text{COOH} + \text{Br}_2 \xrightarrow{\text{cat. }\text{PBr}_3 \text{ or P}} \text{R-CH(Br)-COOH} + \text{HBr}\uparrow \tag{3.5}$$

```
HVZ Reaction Cycle:
1. R-CH2-COOH + PBr3 ---> R-CH2-COBr (Acid Bromide)
2. R-CH2-COBr <---> R-CH=C(OH)Br (Enol of Acid Bromide)
3. R-CH=C(OH)Br + Br2 ---> R-CH(Br)-COBr (alpha-Bromo Acid Bromide)
4. R-CH(Br)-COBr + R-CH2-COOH ---> R-CH(Br)-COOH + R-CH2-COBr (Catalytic Exchange)
```

#### Detailed Mechanistic Steps:
1. **In Situ Generation of Acyl Bromide**: A catalytic amount of $\text{PBr}_3$ converts a fraction of the carboxylic acid into the corresponding acyl bromide:
   $$\text{RCH}_2\text{COOH} + \text{PBr}_3 \longrightarrow \text{RCH}_2\text{COBr} + \text{PBr}_2\text{OH}$$
2. **Facile Acid Bromide Enolization**: Acyl bromides enolize millions of times faster than carboxylic acids because the electronegative bromine atom and lack of hydrogen-bonded dimer stabilization acidify the $\alpha$-proton:
   $$\text{RCH}_2\text{COBr} \xrightleftharpoons{} \text{RCH}=\text{C}(\text{OH})\text{Br} \quad (\text{enol form})$$
3. **Electrophilic Bromination**: The enol attacks molecular bromine, forming the $\alpha$-bromo acyl bromide:
   $$\text{RCH}=\text{C}(\text{OH})\text{Br} + \text{Br}_2 \longrightarrow \text{RCH(Br)COBr} + \text{HBr}\uparrow$$
4. **Catalytic Acyl Exchange**: The $\alpha$-bromo acyl bromide reacts with an incoming molecule of unreacted carboxylic acid via nucleophilic acyl substitution:
   $$\text{RCH(Br)COBr} + \text{RCH}_2\text{COOH} \rightleftharpoons \text{RCH(Br)COOH} + \text{RCH}_2\text{COBr}$$
   This step furnishes the desired **$\alpha$-bromo carboxylic acid** and regenerates the active $\text{RCH}_2\text{COBr}$ catalyst to sustain the cycle.

$\alpha$-Halo acids are critical synthetic intermediates: nucleophilic substitution with aqueous $\text{NaOH}$ gives $\alpha$-hydroxy acids, with excess $\text{NH}_3$ yields $\alpha$-amino acids, and with alcoholic $\text{KOH}$ yields $\alpha,\beta$-unsaturated acids.""",
                "simulations": []
            },
            {
                "id": "sec3_5",
                "secNumber": "§3.5",
                "title": "Hydroxy Acids: Classification, Thermal Cascades & Lactonization Dynamics",
                "heading": "Hydroxy Acids: Classification, Thermal Cascades & Lactonization Dynamics",
                "content": r"""Hydroxy acids contain both a hydroxyl ($-\text{OH}$) and a carboxyl ($-\text{COOH}$) functional group within the same molecular framework. Their chemical reactivity upon thermal dehydration depends decisively on the positional separation ($\alpha, \beta, \gamma, \delta$) between the two functions:

### 1. $\alpha$-Hydroxy Acids: Intermolecular Lactide Dimerization
In $\alpha$-hydroxy acids (e.g., lactic acid, glycolic acid), intramolecular cyclization would require a strained, thermodynamically prohibited three-membered $\alpha$-lactone ring.
Instead, when heated, two molecules undergo mutual intermolecular double esterification to furnish a six-membered cyclic diester known as a **lactide**:

$$2\,\text{CH}_3\text{CH(OH)COOH} \xrightarrow{\Delta, -\text{H}_2\text{O}} \text{Lactide (3,6-dimethyl-1,4-dioxane-2,5-dione)} \tag{3.6}$$

Lactides undergo ring-opening polymerization catalyzed by tin(II) octanoate to yield **polylactic acid (PLA)**, a leading biodegradable thermoplastic used in medical sutures and sustainable packaging.

### 2. $\beta$-Hydroxy Acids: Dehydration to $\alpha,\beta$-Unsaturated Acids
In $\beta$-hydroxy acids (e.g., 3-hydroxybutanoic acid), intramolecular cyclization to a strained four-membered $\beta$-lactone is disfavored under thermal conditions.
Upon heating, they undergo facile dehydration via an elimination mechanism to yield conjugated **$\alpha,\beta$-unsaturated carboxylic acids**:

$$\text{R-CH(OH)-CH}_2-\text{COOH} \xrightarrow{\Delta} \text{R-CH}=\text{CH-COOH} + \text{H}_2\text{O} \tag{3.7}$$

### 3. $\gamma$- and $\delta$-Hydroxy Acids: Intramolecular Lactonization
In $\gamma$-hydroxy acids (C4) and $\delta$-hydroxy acids (C5), the terminal hydroxyl and carboxyl groups readily achieve optimal orbital alignment to form five- and six-membered rings.
Under mild acidic conditions or gentle heating, they undergo spontaneous intramolecular esterification to form highly stable cyclic esters called **$\gamma$-butyrolactones** and **$\delta$-valerolactones**:

$$\text{HO-CH}_2\text{CH}_2\text{CH}_2\text{COOH} \xrightleftharpoons[\Delta]{\text{H}^+} \gamma\text{-butyrolactone (GBL)} + \text{H}_2\text{O} \tag{3.8}$$

The equilibrium heavily favors lactone formation ($\Delta G^\circ < 0$) due to favorable activation enthalpy ($\Delta H^\ddagger$) and low ring strain in five- and six-membered cycles.""",
                "simulations": []
            },
            {
                "id": "sec3_6",
                "secNumber": "§3.6",
                "title": "Unsaturated Dicarboxylic Acids: Maleic vs Fumaric Acid Stereochemistry",
                "heading": "Unsaturated Dicarboxylic Acids: Maleic vs Fumaric Acid Stereochemistry",
                "content": r"""The diastereomeric pair **maleic acid** (*cis*-butenedioic acid) and **fumaric acid** (*trans*-butenedioic acid) illustrates how geometric configuration governs physical properties, acid dissociation equilibria, and chemical reactivity.

```
       Maleic Acid (cis)                        Fumaric Acid (trans)
           H       H                                H      COOH
            \     /                                  \    /
             C = C                                    C = C
            /     \                                  /     \
        HOOC       COOH                          HOOC       H
```

| Physical / Chemical Property | Maleic Acid (*cis*) | Fumaric Acid (*trans*) | Molecular Origin |
| :--- | :--- | :--- | :--- |
| **Melting Point** | $130^\circ\text{C}$ | $287^\circ\text{C}$ | Fumaric acid packs efficiently into a centrosymmetric crystal lattice |
| **Water Solubility ($25^\circ\text{C}$)** | $788\text{ g/L}$ | $6.3\text{ g/L}$ | Maleic acid is polar ($\mu = 3.17\text{ D}$); fumaric acid is centrosymmetric ($\mu = 0$) |
| **First Ionization Constant ($\text{p}K_{a1}$)** | **$1.92$** | **$3.02$** | Intramolecular hydrogen bonding stabilizes the mono-anion of maleic acid |
| **Second Ionization Constant ($\text{p}K_{a2}$)** | **$6.23$** | **$4.38$** | Electrostatic repulsion between adjacent $-0.5$ charges destabilizes the dianion |
| **Thermal Anhydride Formation** | Forms anhydride at $140^\circ\text{C}$ | Does not form anhydride until $300^\circ\text{C}$ | Maleic acid has *cis*-carboxyl groups adjacent in space |

### The Thermodynamic Basis of the $\text{p}K_a$ Gap
The ratio of first dissociation constants $\frac{K_{a1}(\text{maleic})}{K_{a1}(\text{fumaric})} \approx 13$ indicates that maleic acid is more than an order of magnitude more acidic than fumaric acid.
- When maleic acid loses its first proton, the resulting mono-anion forms an extraordinarily strong **intramolecular hydrogen bond** between the remaining carboxyl group and the carboxylate oxygen:
  $$[\text{O}=\text{C}(\text{OH})-\text{CH}=\text{CH}-\text{C}(=\text{O})-\text{O}^-] \longleftrightarrow \text{Symmetric 7-membered H-bonded ring}$$
  This internal hydrogen bond lowers the enthalpy of the mono-anion by $\sim 25\text{ kJ}\cdot\text{mol}^{-1}$.
- In contrast, fumaric acid cannot form an intramolecular hydrogen bond because its two carboxyl groups are held rigidly *trans* across the $\pi$ bond at a separation $>4.5\text{ \AA}$.

However, for the second dissociation step, maleic acid is significantly **weaker** than fumaric acid:
$$\text{p}K_{a2}(\text{maleic}) = 6.23 \quad \text{vs} \quad \text{p}K_{a2}(\text{fumaric}) = 4.38$$
Removing the second proton from maleic acid requires:
1. Breaking the strong stabilizing intramolecular hydrogen bond.
2. Forcing two full negative charges into close proximity on the same side of the double bond, incurring massive Coulombic repulsion:
   $$V_{\text{Coulomb}} = \frac{q_1 q_2}{4 \pi \epsilon_0 \epsilon_r r} \gg 0$$
In fumaric acid, the two carboxylate charges are separated on opposite sides of the molecule ($r > 4.8\text{ \AA}$), minimizing electrostatic repulsion.""",
                "simulations": []
            },
            {
                "id": "sec3_7",
                "secNumber": "§3.7",
                "title": "Keto Acids: Pyruvic, Acetoacetic, Levulinic & Decarboxylation Pathways",
                "heading": "Keto Acids: Pyruvic, Acetoacetic, Levulinic & Decarboxylation Pathways",
                "content": r"""Keto acids contain a ketone carbonyl at varying positions relative to the carboxylic acid:
- **$\alpha$-Keto acids (2-oxoacids)**: Pyruvic acid ($\text{CH}_3\text{COCOOH}$).
- **$\beta$-Keto acids (3-oxoacids)**: Acetoacetic acid ($\text{CH}_3\text{COCH}_2\text{COOH}$).
- **$\gamma$-Keto acids (4-oxoacids)**: Levulinic acid ($\text{CH}_3\text{COCH}_2\text{CH}_2\text{COOH}$).

### The Pericyclic Decarboxylation of $\beta$-Keto Acids
While ordinary carboxylic acids require severe heating ($>300^\circ\text{C}$) to undergo thermal decarboxylation, $\beta$-keto acids undergo rapid, spontaneous decarboxylation at modest temperatures ($50^\circ\text{–}100^\circ\text{C}$):

$$\text{R-CO-CH}_2\text{-COOH} \xrightarrow{50^\circ\text{-}100^\circ\text{C}} \text{R-CO-CH}_3 + \text{CO}_2\uparrow \tag{3.9}$$

```
Thermal Decarboxylation 6-Center Transition State:
           H
         /   \
        O     O
       //      \
      C         C = O
     / \       /
    R   CH2 = C
```

#### Mechanistic Features:
1. The molecule adopts a cyclic conformation where the acidic carboxyl proton forms an intramolecular hydrogen bond with the $\beta$-keto carbonyl oxygen.
2. The reaction proceeds through a concerted, pericyclic **six-membered cyclic transition state** involving simultaneous redistribution of six electrons:
   - The $\text{O}-\text{H}$ bond breaks, forming an $\text{O}-\text{H}$ bond to the ketone oxygen.
   - The $\text{C}-\text{C}$ bond between C2 and C3 breaks, liberating carbon dioxide ($\text{CO}_2\uparrow$).
   - The $\alpha$-carbon forms a $\text{C}=\text{C}$ double bond with the carbonyl carbon.
3. The initial organic product is the **enol of the ketone**:
   $$\text{R-CO-CH}_2\text{-COOH} \longrightarrow \text{R-C(OH)}=\text{CH}_2 + \text{CO}_2\uparrow$$
4. Rapid, irreversible keto-enol tautomerism converts the enol into the methyl ketone product.
5. The massive thermodynamic driving force is the formation of stable, volatile carbon dioxide ($\text{CO}_2$, $\Delta H^\circ = -393.5\text{ kJ}\cdot\text{mol}^{-1}$) and a large increase in entropy ($\Delta S^\circ > 0$).""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob3_1",
                "problemNumber": "3.1",
                "title": "Thermodynamic Disparity in Maleic vs Fumaric Acid Dissociation Constants",
                "difficulty": "Mastery",
                "statement": r"""The first and second acid dissociation constants of maleic and fumaric acids in water at $25^\circ\text{C}$ are:
- Maleic acid: $K_{a1} = 1.20 \times 10^{-2}$ ($\text{p}K_{a1} = 1.92$), $K_{a2} = 5.90 \times 10^{-7}$ ($\text{p}K_{a2} = 6.23$)
- Fumaric acid: $K_{a1} = 9.55 \times 10^{-4}$ ($\text{p}K_{a1} = 3.02$), $K_{a2} = 4.17 \times 10^{-5}$ ($\text{p}K_{a2} = 4.38$)
(a) Calculate the standard Gibbs free energy difference $\Delta(\Delta G^\circ_1)$ between the first ionization of maleic acid and fumaric acid.
(b) Calculate $\Delta(\Delta G^\circ_2)$ for the second ionization step.
(c) Using Coulomb's law and hydrogen-bonding enthalpy arguments, account for the signs and magnitudes of both energetic values.""",
                "hints": ["Use $\Delta G^\circ = -RT \ln K_a = 2.303 RT \text{p}K_a$.", "At $298.15\text{ K}$, $2.303 RT \approx 5.708\text{ kJ}\cdot\text{mol}^{-1}$ per $\text{p}K_a$ unit."],
                "solution": r"""### (a) Free Energy Difference for First Ionization ($\Delta(\Delta G^\circ_1)$)
$$\Delta G^\circ = 2.303 RT \, \text{p}K_a$$
At $T = 298.15\text{ K}$:
$$2.303 RT = 2.303 \times (8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times 298.15\text{ K} = 5.708\text{ kJ}\cdot\text{mol}^{-1}$$
For the first dissociation:
$$\Delta G^\circ_1(\text{maleic}) = 5.708 \times 1.92 = 10.96\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta G^\circ_1(\text{fumaric}) = 5.708 \times 3.02 = 17.24\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta(\Delta G^\circ_1) = \Delta G^\circ_1(\text{maleic}) - \Delta G^\circ_1(\text{fumaric}) = 10.96 - 17.24 = -6.28\text{ kJ}\cdot\text{mol}^{-1}$$
The first ionization of maleic acid is thermodynamically favored by $6.28\text{ kJ}\cdot\text{mol}^{-1}$.

### (b) Free Energy Difference for Second Ionization ($\Delta(\Delta G^\circ_2)$)
For the second dissociation:
$$\Delta G^\circ_2(\text{maleic}) = 5.708 \times 6.23 = 35.56\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta G^\circ_2(\text{fumaric}) = 5.708 \times 4.38 = 25.00\text{ kJ}\cdot\text{mol}^{-1}$$
$$\Delta(\Delta G^\circ_2) = \Delta G^\circ_2(\text{maleic}) - \Delta G^\circ_2(\text{fumaric}) = 35.56 - 25.00 = +10.56\text{ kJ}\cdot\text{mol}^{-1}$$
The second ionization of maleic acid is thermodynamically disfavored by $10.56\text{ kJ}\cdot\text{mol}^{-1}$ relative to fumaric acid.

### (c) Physical Organic Origin
1. **First Dissociation Step ($\Delta(\Delta G^\circ_1) = -6.28\text{ kJ}\cdot\text{mol}^{-1}$)**:
   In the hydrogen maleate monoanion, the *cis* geometry allows a strong intramolecular hydrogen bond:
   $$\text{O}-\text{H}\cdots\text{O}^- \quad (\text{symmetric 7-membered quasi-ring})$$
   This hydrogen bond lowers the enthalpy of the monoanion by $>20\text{ kJ}\cdot\text{mol}^{-1}$, offsetting the entropic cost and facilitating first proton release. Fumaric acid's *trans* geometry holds the carboxyl groups $>4.5\text{ \AA}$ apart, precluding intramolecular stabilization.
2. **Second Dissociation Step ($\Delta(\Delta G^\circ_2) = +10.56\text{ kJ}\cdot\text{mol}^{-1}$)**:
   Ionization of hydrogen maleate requires breaking the intramolecular hydrogen bond and placing two identical negative charges ($e = -1.6 \times 10^{-19}\text{ C}$) at a distance of $r \approx 3.2\text{ \AA}$ on the same face of the double bond. The Coulombic repulsion energy in water ($\epsilon_r \approx 78$) is:
   $$V_{\text{rep}} \approx \frac{e^2}{4 \pi \epsilon_0 \epsilon_r r} \approx +5.5\text{ kJ}\cdot\text{mol}^{-1}$$
   Combined with the loss of hydrogen-bond enthalpy ($+15\text{ kJ}\cdot\text{mol}^{-1}$), the second dissociation is heavily penalized."""
            },
            {
                "id": "prob3_2",
                "problemNumber": "3.2",
                "title": "Hammett Linear Free-Energy Analysis of Substituted Benzoic Acids",
                "difficulty": "Advanced",
                "statement": r"""The ionization constant of unsubstituted benzoic acid in water at $25^\circ\text{C}$ is $K_0 = 6.30 \times 10^{-5}$ ($\text{p}K_0 = 4.20$).
(a) Given the Hammett substituent constants $\sigma_{p\text{-NO}_2} = +0.78$ and $\sigma_{p\text{-OCH}_3} = -0.27$, calculate the theoretical $K_a$ and $\text{p}K_a$ values for 4-nitrobenzoic acid and 4-methoxybenzoic acid.
(b) For the alkaline saponification of ethyl benzoates ($\text{ArCOOEt} + \text{OH}^- \to \text{ArCOO}^- + \text{EtOH}$), the reaction constant is $\rho = +2.54$. Calculate how much faster ethyl 4-nitrobenzoate hydrolyzes compared to ethyl benzoate.
(c) What does the positive value of $\rho = +2.54$ indicate regarding charge development in the rate-determining transition state?""",
                "hints": ["Use the Hammett equation: $\log(K/K_0) = \sigma \cdot \rho$.", "For benzoic acid ionization in water, $\rho = 1.00$."],
                "solution": r"""### (a) Ionization Constants of Substituted Benzoic Acids
By definition, $\rho = 1.00$ for benzoic acid ionization in water at $25^\circ\text{C}$:
$$\log\left(\frac{K_a}{K_0}\right) = \sigma \implies \text{p}K_a = \text{p}K_0 - \sigma$$

1. **For 4-Nitrobenzoic acid ($\sigma_{p\text{-NO}_2} = +0.78$)**:
   $$\text{p}K_a = 4.20 - 0.78 = 3.42$$
   $$K_a = 10^{-3.42} = 3.80 \times 10^{-4}\text{ M}$$
   The strong $-I$ and $-M$ electron-withdrawing nitro group enhances acidity by a factor of 6.

2. **For 4-Methoxybenzoic acid ($\sigma_{p\text{-OCH}_3} = -0.27$)**:
   $$\text{p}K_a = 4.20 - (-0.27) = 4.47$$
   $$K_a = 10^{-4.47} = 3.39 \times 10^{-5}\text{ M}$$
   Although oxygen is electronegative ($-I$), resonance donation ($+M$) of the lone pair into the aromatic ring dominates at the para-position, stabilizing the neutral acid and decreasing acidity.

### (b) Relative Rate of Saponification
For ester saponification:
$$\log\left(\frac{k_{p\text{-NO}_2}}{k_{\text{H}}}\right) = \sigma_{p\text{-NO}_2} \cdot \rho = (+0.78) \times (+2.54) = +1.981$$
$$\frac{k_{p\text{-NO}_2}}{k_{\text{H}}} = 10^{1.981} \approx 95.7$$
Ethyl 4-nitrobenzoate undergoes saponification **96 times faster** than ethyl benzoate.

### (c) Mechanistic Interpretation of $\rho = +2.54$
A large positive $\rho$ value ($+2.54 > 0$) reveals that:
1. Negative charge builds up in the rate-determining transition state.
2. The transition state involves nucleophilic attack of hydroxide ($\text{OH}^-$) on the carbonyl carbon to form a negatively charged tetrahedral intermediate ($[\text{Ar}-\text{C}(\text{O}^-)(\text{OH})(\text{OEt})]^\ddagger$).
3. The magnitude ($2.54 > 1.00$) indicates that the transition state is substantially more sensitive to electronic substituent effects than the ground-state ionization of benzoic acid."""
            },
            {
                "id": "prob3_3",
                "problemNumber": "3.3",
                "title": "Hell-Volhard-Zelinsky (HVZ) Synthesis of $\alpha$-Amino Acids",
                "difficulty": "Intermediate",
                "statement": r"""Devise an efficient chemical synthesis of racemic valine (2-amino-3-methylbutanoic acid) starting from isovaleric acid (3-methylbutanoic acid).
(a) Provide the reagents and mechanism for the $\alpha$-halogenation step.
(b) Specify the conditions for converting the $\alpha$-halo acid into the $\alpha$-amino acid, explaining why a large excess of ammonia is required.
(c) What by-product would form if stoichiometric rather than catalytic $\text{PBr}_3$ were omitted completely?""",
                "hints": ["Isovaleric acid is $(CH_3)_2CH-CH_2-COOH$.", "Excess ammonia prevents dialkylation of the forming primary amine."],
                "solution": r"""### (a) $\alpha$-Halogenation Step via HVZ
$$\text{(CH}_3)_2\text{CH-CH}_2\text{-COOH} + \text{Br}_2 \xrightarrow{\text{cat. PBr}_3 \text{ (0.1 equiv)}} \text{(CH}_3)_2\text{CH-CH(Br)-COOH} + \text{HBr}\uparrow$$
**Mechanism**:
1. Catalytic $\text{PBr}_3$ converts isovaleric acid into isovaleryl bromide:
   $$\text{(CH}_3)_2\text{CHCH}_2\text{COOH} + \text{PBr}_3 \to \text{(CH}_3)_2\text{CHCH}_2\text{COBr} + \text{PBr}_2\text{OH}$$
2. Isovaleryl bromide enolizes to form the enol intermediate:
   $$\text{(CH}_3)_2\text{CHCH}_2\text{COBr} \rightleftharpoons \text{(CH}_3)_2\text{CH-CH}=\text{C(OH)Br}$$
3. Attack on $\text{Br}_2$ yields 2-bromo-3-methylbutanoyl bromide.
4. Acyl transfer with unreacted isovaleric acid regenerates the isovaleryl bromide catalyst and delivers **2-bromo-3-methylbutanoic acid**.

### (b) Amination to Racemic Valine
$$\text{(CH}_3)_2\text{CH-CH(Br)-COOH} + \text{excess NH}_3 \xrightarrow{\text{aq. NH}_4\text{OH (conc.), }25^\circ\text{C}} \text{(CH}_3)_2\text{CH-CH(NH}_3^+)\text{-COO}^- + \text{NH}_4\text{Br}$$
- **Role of Excess Ammonia**: Ammonia undergoes nucleophilic substitution ($S_N2$) on the $\alpha$-carbon. If stoichiometric ammonia (1 equivalent) were used, the newly formed primary amine (valine) would compete with ammonia as a nucleophile, reacting with unreacted $\alpha$-bromo acid to form an undesirable secondary amine dialkylation side-product:
  $$\text{R-CH(Br)COOH} + \text{R-CH(NH}_2)\text{COOH} \longrightarrow [\text{HOOC-CH(R)}]_2\text{NH}$$
  A large excess of ammonia ($>20$-fold) ensures that an incoming $\alpha$-bromo acid molecule encounters $\text{NH}_3$ almost exclusively.

### (c) Omission of Phosphorus Catalyst
If elemental $\text{Br}_2$ is added to isovaleric acid without $\text{PBr}_3$ or red phosphorus, **no reaction occurs**. Carboxylic acids exist as hydrogen-bonded cyclic dimers with negligible enol concentrations ($K_{\text{enol}} < 10^{-12}$), rendering them unreactive toward electrophilic halogenation."""
            },
            {
                "id": "prob3_4",
                "problemNumber": "3.4",
                "title": "Pericyclic Decarboxylation Kinetics of $\beta$-Keto Acids",
                "difficulty": "Mastery",
                "statement": r"""Acetoacetic acid ($\text{CH}_3\text{COCH}_2\text{COOH}$) decarboxylates rapidly in aqueous solution at $37^\circ\text{C}$ ($t_{1/2} \approx 140\text{ min}$), whereas 2,2-dimethylacetoacetic acid ($\text{CH}_3\text{COC(Me)}_2\text{COOH}$) and levulinic acid ($\text{CH}_3\text{COCH}_2\text{CH}_2\text{COOH}$) are completely stable at this temperature.
(a) Draw the six-membered transition state for acetoacetic acid decarboxylation.
(b) Why does the monoanion of acetoacetic acid ($\text{CH}_3\text{COCH}_2\text{COO}^-$) decarboxylate at a different rate than the neutral carboxylic acid?
(c) Explain why levulinic acid and 2,2-dimethylacetoacetic acid fail to decarboxylate at $37^\circ\text{C}$.""",
                "hints": ["Can levulinic acid form a 6-membered cyclic transition state involving the keto oxygen?", "2,2-Dimethylacetoacetic acid still has the carboxyl hydrogen, but examine enol formation."],
                "solution": r"""### (a) Six-Membered Pericyclic Transition State
Acetoacetic acid adopts a cyclic planar chair/envelope conformation:
- Carbonyl oxygen of the $\beta$-keto group acts as an internal hydrogen-bond acceptor for the carboxyl proton ($-\text{COOH}$).
- A concerted six-electron pericyclic rearrangement occurs:
  $$\begin{aligned}
  \text{Bond Breaking}: &\quad \text{C2-C3 bond}, \quad \text{O-H bond} \\
  \text{Bond Making}: &\quad \text{O}\cdots\text{H (enol bond)}, \quad \text{C1=C2 (alkene double bond)}, \quad \text{O=C=O (carbon dioxide)}
  \end{aligned}$$
- The direct product is the **enol of acetone** ($\text{CH}_3-\text{C(OH)}=\text{CH}_2$) plus gaseous $\text{CO}_2$.
- The enol rapidly tautomerizes to acetone ($\text{CH}_3\text{COCH}_3$).

### (b) Decarboxylation of the Neutral Acid vs Anion
1. **Neutral Acid ($\text{HA}$)**: Decarboxylates rapidly via the concerted 6-center pericyclic transition state with an activation enthalpy of $\Delta H^\ddagger \approx 95\text{ kJ}\cdot\text{mol}^{-1}$.
2. **Carboxylate Anion ($\text{A}^-$)**: The carboxylate anion ($-\text{COO}^-$) has lost its acidic proton and therefore **cannot** form the six-membered hydrogen-bonded pericyclic transition state!
Instead, the anion must decarboxylate via heterolytic $\text{C}-\text{C}$ bond cleavage generating a localized carbanion enolate intermediate:
$$\text{CH}_3\text{COCH}_2\text{COO}^- \longrightarrow [\text{CH}_3\text{COCH}_2^- \longleftrightarrow \text{CH}_3\text{C}(\text{O}^-)=\text{CH}_2] + \text{CO}_2\uparrow$$
Because this ionic heterolysis has a higher activation barrier ($\Delta G^\ddagger \approx 125\text{ kJ}\cdot\text{mol}^{-1}$), decarboxylation of the neutral acid is much faster than that of the carboxylate anion.

### (c) Levulinic Acid and 2,2-Dimethylacetoacetic Acid
- **Levulinic Acid ($\gamma$-keto acid)**: The ketone carbonyl is at C4. Attempting to form a cyclic transition state between the carboxyl hydrogen and the keto oxygen would require a strained **seven-membered ring** ($7$-center). The entropic and conformational penalties prevent concerted pericyclic decarboxylation at $37^\circ\text{C}$.
- **2,2-Dimethylacetoacetic Acid**: Possesses two methyl groups at C2. It can form the 6-membered transition state and decarboxylates cleanly to give 3-methylbutan-2-one enol. (If the prompt meant an ester or carboxylate salt, decarboxylation would be stopped). Levulinic acid, however, is thermally stable up to $200^\circ\text{C}$."""
            },
            {
                "id": "prob3_5",
                "problemNumber": "3.5",
                "title": "Lactonization Thermodynamics of $\gamma$- vs $\delta$-Hydroxy Acids",
                "difficulty": "Intermediate",
                "statement": r"""4-Hydroxybutanoic acid spontaneously cyclizes in dilute aqueous acid to form $\gamma$-butyrolactone ($\text{GBL}$) with an equilibrium constant $K_{\text{eq}} = 2.7 \times 10^2$ at $25^\circ\text{C}$.
(a) Calculate $\Delta G^\circ$ for this lactonization reaction.
(b) 5-Hydroxypentanoic acid exhibits an even larger equilibrium constant for lactonization ($K_{\text{eq}} \approx 1.5 \times 10^3$). What thermodynamic factors explain the high stability of five- and six-membered lactone rings compared to seven-membered ($\epsilon$-caprolactone) rings?
(c) Why do $\beta$-hydroxy acids fail to form four-membered $\beta$-lactones upon heating?""",
                "hints": ["Use $\Delta G^\circ = -RT \ln K_{\text{eq}}$.", "Recall Baeyer angle strain and conformational entropy in ring sizes."],
                "solution": r"""### (a) Free Energy Calculation for $\gamma$-Butyrolactone
$$\Delta G^\circ = -RT \ln K_{\text{eq}}$$
At $T = 298.15\text{ K}$:
$$\Delta G^\circ = -(8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (298.15\text{ K}) \times \ln(270)$$
$$\ln(270) = 5.5984$$
$$\Delta G^\circ = -8.314 \times 298.15 \times 5.5984 = -13,878\text{ J}\cdot\text{mol}^{-1} \approx -13.9\text{ kJ}\cdot\text{mol}^{-1}$$
The negative free energy confirms that cyclization is exergonic and thermodynamically favorable under ambient conditions.

### (b) Ring Size Thermodynamics (5/6-Membered vs 7-Membered)
1. **Enthalpy ($\Delta H^\circ$)**: Five- and six-membered rings experience virtually zero Baeyer angle strain (internal angles $\approx 108^\circ\text{–}109.5^\circ$) and minimal Pitzer torsional strain (chair conformation in 6-membered, envelope in 5-membered). In contrast, seven-membered rings ($\epsilon$-lactones) suffer from significant transannular steric repulsions and angle strain ($\Delta H_{\text{strain}} \approx 25\text{ kJ}\cdot\text{mol}^{-1}$).
2. **Entropy ($\Delta S^\circ$)**: Intramolecular cyclization freezes rotational degrees of freedom along the acyclic carbon chain:
   $$\Delta S_{\text{rot}} \approx -18\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \text{ per frozen rotor}$$
   A 5-membered ring freezes 3 rotors, whereas a 7-membered ring freezes 5 rotors, imposing a severe entropic penalty on 7-membered cyclization.

### (c) Failure of $\beta$-Hydroxy Acids to Form $\beta$-Lactones
Four-membered $\beta$-lactones (oxetan-2-ones) possess severe ring strain ($\sim 105\text{ kJ}\cdot\text{mol}^{-1}$ or $25\text{ kcal}\cdot\text{mol}^{-1}$) resulting from $90^\circ$ bond angles forced upon $sp^2$ and $sp^3$ centers. Thermal heating provides sufficient activation energy to undergo alternative bimolecular dehydration to conjugated $\alpha,\beta$-unsaturated acids ($\Delta G^\circ \ll 0$), completely bypassing four-membered ring formation."""
            },
            {
                "id": "prob3_6",
                "problemNumber": "3.6",
                "title": "Industrial Monsanto Carbonylation Catalytic Cycle",
                "difficulty": "Mastery",
                "statement": r"""The industrial production of acetic acid via the Monsanto process utilizes a rhodium catalyst and methyl iodide promoter:
$$\text{CH}_3\text{OH} + \text{CO} \xrightarrow{[\text{Rh}(\text{CO})_2\text{I}_2]^-, 180^\circ\text{C}, 30\text{ atm}} \text{CH}_3\text{COOH}$$
(a) Write the complete catalytic cycle detailing the oxidation state, $d$-electron count, and coordination number of the rhodium complex at each of the four elementary steps:
1. Oxidative addition of $\text{CH}_3\text{I}$
2. Migratory insertion of $\text{CO}$
3. Coordination of incoming $\text{CO}$
4. Reductive elimination of acetyl iodide ($\text{CH}_3\text{COI}$)
(b) Identify the rate-determining step and explain why the Cativa iridium process is superior at lower water concentrations.""",
                "hints": ["Start with cis-[Rh(CO)2I2]-, which has Rh(I), d8, 16 electrons.", "Oxidative addition increases oxidation state by +2."],
                "solution": r"""### (a) Detailed Organometallic Catalytic Cycle
The active catalyst is the square planar anion *cis*-$[\text{Rh}(\text{CO})_2\text{I}_2]^-$:
- Oxidation state: $\text{Rh}(\text{I})$
- Electron count: $d^8$, $16$-electron complex
- Coordination number: $4$

#### Step 1: Oxidative Addition (Rate-Determining Step)
$$[\text{Rh}^{\text{I}}(\text{CO})_2\text{I}_2]^- + \text{CH}_3\text{I} \xrightarrow{k_1} [\text{Rh}^{\text{III}}(\text{CO})_2(\text{CH}_3)\text{I}_3]^-$$
- Rhodium undergoes two-electron oxidation from $\text{Rh}(\text{I})$ to $\text{Rh}(\text{III})$ ($d^6$).
- Geometry changes from 16-electron square planar to 18-electron octahedral (coordination number = 6).
- Proceeds via an $S_N2$-like nucleophilic attack of the electron-rich rhodium metal center onto methyl iodide.

#### Step 2: Migratory CO Insertion
$$[\text{Rh}^{\text{III}}(\text{CO})_2(\text{CH}_3)\text{I}_3]^- \longrightarrow [\text{Rh}^{\text{III}}(\text{CO})(\text{COCH}_3)\text{I}_3]^-$$
- The coordinated methyl group migrates onto an adjacent coordinated carbonyl ligand to form an acyl group ($-\text{COCH}_3$).
- Generates a 16-electron pentacoordinated intermediate (coordination number = 5).

#### Step 3: Carbonyl Coordination
$$[\text{Rh}^{\text{III}}(\text{CO})(\text{COCH}_3)\text{I}_3]^- + \text{CO} \longrightarrow [\text{Rh}^{\text{III}}(\text{CO})_2(\text{COCH}_3)\text{I}_3]^-$$
- Rapid coordination of incoming gaseous carbon monoxide restores the 18-electron octahedral configuration (coordination number = 6).

#### Step 4: Reductive Elimination
$$[\text{Rh}^{\text{III}}(\text{CO})_2(\text{COCH}_3)\text{I}_3]^- \longrightarrow [\text{Rh}^{\text{I}}(\text{CO})_2\text{I}_2]^- + \text{CH}_3\text{COI}$$
- Intramolecular coupling of the acyl group with an iodide ligand expels acetyl iodide ($\text{CH}_3\text{COI}$).
- Rhodium is reduced from $\text{Rh}(\text{III})$ ($d^6$) back to $\text{Rh}(\text{I})$ ($d^8$, 16 electrons), regenerating the square planar catalyst.
- Subsequent rapid hydrolysis of acetyl iodide produces acetic acid and regenerates $\text{HI}$:
  $$\text{CH}_3\text{COI} + \text{H}_2\text{O} \longrightarrow \text{CH}_3\text{COOH} + \text{HI}$$
  $$\text{CH}_3\text{OH} + \text{HI} \longrightarrow \text{CH}_3\text{I} + \text{H}_2\text{O}$$

### (b) Rate-Determining Step & The Cativa Process
In the Monsanto rhodium cycle, **Step 1 (oxidative addition of $\text{CH}_3\text{I}$)** is rate-determining. To maintain catalyst solubility and suppress precipitation of inactive $\text{RhI}_3$, high water concentrations ($14\text{–}15\text{ wt}\%$) are required, necessitating massive distillation energy to dewater the acetic acid product.
In the BP **Cativa process**, iridium ($[\text{Ir}(\text{CO})_2\text{I}_2]^-$) is utilized. Because iridium is a $5d$ metal, oxidative addition is $\sim 10$-fold faster than with rhodium. The rate-determining step shifts to migratory insertion, which is accelerated by ruthenium promoters ($[\text{Ru}(\text{CO})_3\text{I}_3]^-$). The Cativa process operates efficiently at water levels below $5\text{ wt}\%$, slashing purification costs and greenhouse emissions."""
            },
            {
                "id": "prob3_7",
                "problemNumber": "3.7",
                "title": "Synthesis & Enantioselective Resolution of Racemic Mandelic Acid",
                "difficulty": "Intermediate",
                "statement": r"""Mandelic acid (2-hydroxy-2-phenylacetic acid) is a classic chiral $\alpha$-hydroxy acid.
(a) Outline the total synthesis of racemic mandelic acid starting from benzaldehyde and sodium cyanide.
(b) Explain why mandelic acid can be resolved into pure (+)-(R) and (-)-(S) enantiomers using the natural chiral base cinchonine, but cannot be resolved using ordinary achiral fractional crystallization.
(c) Write equations demonstrating how the diastereomeric salts are formed, separated, and acidified.""",
                "hints": ["Benzaldehyde + NaCN gives mandelonitrile.", "Enantiomers have identical solubility in achiral solvents, but diastereomers do not."],
                "solution": r"""### (a) Total Synthesis of Racemic Mandelic Acid
$$\begin{aligned}
\text{Step 1 (Cyanohydrin Formation)}: &\quad \text{PhCHO} + \text{NaCN} + \text{NaHSO}_3 \longrightarrow \text{PhCH(OH)CN (Mandelonitrile)} \\
\text{Step 2 (Acidic Hydrolysis)}: &\quad \text{PhCH(OH)CN} + 2\,\text{H}_2\text{O} + \text{HCl} \xrightarrow{\Delta} (\pm)\text{-PhCH(OH)COOH} + \text{NH}_4\text{Cl}
\end{aligned}$$
Because benzaldehyde possesses a planar $sp^2$ carbonyl carbon, nucleophilic attack of $\text{CN}^-$ occurs with equal probability from the *re* and *si* faces, yielding an equimolar $(50:50)$ racemic mixture of (R)- and (S)-mandelic acid.

### (b) Physical Rationale for Chiral Resolution
- **Enantiomers**: Possess identical scalar physical properties (melting point, boiling point, dipole moment, and solubility in achiral solvents). Consequently, fractional crystallization from water or ethanol cannot separate (R)- from (S)-mandelic acid.
- **Diastereomers**: Possess different spatial geometries, dipole moments, lattice energies, and significantly different solubilities in polar solvents.
Reaction of racemic mandelic acid ($(\pm)\text{-MA}$) with an optically pure chiral alkaloid base, such as natural $(+)\text{-cinchonine}$ ($(+)\text{-B}$), converts the enantiomers into a pair of **diastereomeric salts**:
$$[(R)\text{-MA} \cdot (+)\text{-B}] \quad \text{and} \quad [(S)\text{-MA} \cdot (+)\text{-B}]$$

### (c) Separation and Isolation
1. **Salt Formation**:
   $$(\pm)\text{-PhCH(OH)COOH} + (+)\text{-Cinchonine} \xrightarrow{\text{EtOH, }\Delta} [(R)\text{-MA}\cdot(+)\text{-B}] + [(S)\text{-MA}\cdot(+)\text{-B}]$$
2. **Fractional Crystallization**:
   The $[(R)\text{-MA}\cdot(+)\text{-B}]$ salt is substantially less soluble in boiling ethanol ($S \approx 12\text{ g/L}$) and crystallizes out upon slow cooling, while the $[(S)\text{-MA}\cdot(+)\text{-B}]$ salt remains dissolved in the mother liquor.
3. **Acidification and Enantiomer Recovery**:
   The filtered crystalline $[(R)\text{-MA}\cdot(+)\text{-B}]$ salt is dissolved in water and acidified with dilute aqueous sulfuric acid ($\text{H}_2\text{SO}_4$):
   $$[(R)\text{-MA}\cdot(+)\text{-B}] + \text{H}^+ \longrightarrow (R)\text{-PhCH(OH)COOH} + (+)\text{-B}\cdot\text{H}^+$$
   Pure $(R)\text{-(-)-mandelic acid}$ is extracted into diethyl ether ($[\alpha]_D^{20} = -158^\circ$), while the protonated cinchonine alkaloid remains in the aqueous phase and is recycled."""
            }
        ]
    }
