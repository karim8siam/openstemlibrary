# -*- coding: utf-8 -*-
"""
expand_org2_units_1_2_3.py
Enrichment module expanding Units 1, 2, and 3 of Organic Chemistry II to honors depth.
Strict zero course numbers or marks.
Adds deep quantum derivations, extensive physical tables, advanced reaction mechanisms,
and an 8th comprehensive multi-part problem to each unit.
"""

def enrich_units_1_2_3(u1, u2, u3):
    print("Enriching Units 1, 2, and 3 with advanced physical organic content...")

    # --- ENRICH UNIT 1: POLYNUCLEAR AROMATICS ---
    # Section 1.1: Clar Sextet Graph Theory and Dewar Resonance Energies
    u1["sections"][0]["content"] += r"""

### Clar Sextet Polynomials and Graph-Theoretical Resonance Energy (TRE)

In mathematical chemical graph theory, the distribution of Clar aromatic sextets can be formalized using **Clar sextet polynomials** $C(G, x)$:

$$C(G, x) = 1 + \sum_{k=1}^m c_k \, x^k \tag{1.0a}$$

where $c_k$ represents the number of resonant Clar covers containing exactly $k$ mutually disjoint, independent aromatic sextets, and $m$ is the Clar number (maximum number of simultaneously inscribable sextets):
- **Benzene**: $C(\text{Benzene}, x) = 1 + x$ ($m = 1$).
- **Naphthalene**: $C(\text{Naphthalene}, x) = 1 + 2x$ ($m = 1$, two resonant positions for the migrating sextet).
- **Anthracene**: $C(\text{Anthracene}, x) = 1 + 3x$ ($m = 1$, three resonant positions along the linear row).
- **Phenanthrene**: $C(\text{Phenanthrene}, x) = 1 + 3x + x^2$ ($m = 2$, can host two simultaneous disjoint sextets in rings A and C).
- **Triphenylene**: $C(\text{Triphenylene}, x) = 1 + 4x + 3x^2 + x^3$ ($m = 3$, three simultaneous disjoint sextets, "fully benzenoid").

The **Dewar Resonance Energy (DRE)** and **Topological Resonance Energy (TRE)** quantify aromatic stabilization relative to an acyclic reference structure having identical bond counts:

$$\text{TRE} = \sum_{j=1}^N \left( \epsilon_j - \epsilon_j^{\text{ref}} \right) \tag{1.0b}$$

For phenanthrene, $\text{TRE} = 0.546 \beta$, whereas for anthracene, $\text{TRE} = 0.475 \beta$. Because $1\beta \approx -75\text{ kJ}\cdot\text{mol}^{-1}$, this graph-theoretical energy gap ($0.071 \beta \approx 5.3\text{ kcal}\cdot\text{mol}^{-1}$) rigorously accounts for the observed $30\text{ kJ}\cdot\text{mol}^{-1}$ thermochemical stability of angular phenes over linear acenes."""

    # Section 1.4: Hückel Secular Determinant of Naphthalene
    u1["sections"][3]["content"] += r"""

### Hückel Secular Determinant and Delocalization Energy of Naphthalene

The $10 \times 10$ Hückel secular determinant for the ten $2p_z$ atomic orbitals of naphthalene is:

$$\det(\mathbf{H} - E\mathbf{S}) = \begin{vmatrix}
\alpha - E & \beta & 0 & 0 & 0 & 0 & 0 & 0 & \beta & 0 \\
\beta & \alpha - E & \beta & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & \beta & \alpha - E & \beta & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & \beta & \alpha - E & 0 & 0 & 0 & 0 & 0 & \beta \\
0 & 0 & 0 & 0 & \alpha - E & \beta & 0 & 0 & 0 & \beta \\
0 & 0 & 0 & 0 & \beta & \alpha - E & \beta & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & \beta & \alpha - E & \beta & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & \beta & \alpha - E & \beta & 0 \\
\beta & 0 & 0 & 0 & 0 & 0 & 0 & \beta & \alpha - E & \beta \\
0 & 0 & 0 & \beta & \beta & 0 & 0 & 0 & \beta & \alpha - E
\end{vmatrix} = 0 \tag{1.3a}$$

Solving this determinant yields the ten molecular orbital energy levels:
$$\begin{aligned}
E_1 &= \alpha + 2.303\beta \\
E_2 &= \alpha + 1.618\beta \\
E_3 &= \alpha + 1.303\beta \\
E_4 &= \alpha + 1.000\beta \\
E_5 &= \alpha + 0.618\beta \quad (\text{HOMO}) \\
E_6 &= \alpha - 0.618\beta \quad (\text{LUMO}) \\
E_7 &= \alpha - 1.000\beta \\
E_8 &= \alpha - 1.303\beta \\
E_9 &= \alpha - 1.618\beta \\
E_{10} &= \alpha - 2.303\beta
\end{aligned}$$

The total ground-state $\pi$-electronic energy is:
$$E_\pi = 2(E_1 + E_2 + E_3 + E_4 + E_5) = 10\alpha + 13.683\beta \tag{1.3b}$$
Comparing this to five isolated, localized ethylene units ($5 \times (2\alpha + 2\beta) = 10\alpha + 10.000\beta$):
$$\Delta E_{\text{deloc}} = 13.683\beta - 10.000\beta = 3.683\beta \approx 276\text{ kJ}\cdot\text{mol}^{-1} \tag{1.3c}$$

The HOMO-LUMO gap is:
$$\Delta E_{\text{gap}} = E_6 - E_5 = (\alpha - 0.618\beta) - (\alpha + 0.618\beta) = -1.236\beta \approx 4.0\text{ eV} \tag{1.3d}$$
This corresponds to naphthalene's strong ultraviolet absorption band at $\lambda_{\max} \approx 275\text{ nm}$."""

    # Add Problem 1.8 to Unit 1
    u1["problems"].append({
        "id": "prob1_8",
        "problemNumber": "1.8",
        "title": "Frontier Molecular Orbital Localization Energies ($L_r$) of Naphthalene",
        "difficulty": "Mastery",
        "statement": r"""In physical organic chemistry, the electrophilic localization energy $L_r^+$ is defined as the $\pi$-electron energy difference between the parent aromatic hydrocarbon and the residual $\pi$-system of the Wheland arenium intermediate formed upon electrophilic addition at position $r$:
$$L_r^+ = E_\pi(\text{parent}) - E_\pi(\text{arenium intermediate})$$
For naphthalene:
- Localization at the $\alpha$-position (C1) yields an arenium ion with $E_\pi(\alpha\text{-arenium}) = 8\alpha + 11.384\beta$.
- Localization at the $\beta$-position (C2) yields an arenium ion with $E_\pi(\beta\text{-arenium}) = 8\alpha + 11.191\beta$.
(a) Given $E_\pi(\text{naphthalene}) = 10\alpha + 13.683\beta$, compute $L_1^+$ and $L_2^+$ in units of $\beta$.
(b) Using $\beta \approx -75\text{ kJ}\cdot\text{mol}^{-1}$, compute the activation energy difference $\Delta(\Delta G^\ddagger) \approx \Delta L^+$ between $\alpha$ and $\beta$ electrophilic substitution.
(c) At $25^\circ\text{C}$, compute the theoretical kinetic regioselectivity ratio $k_\alpha / k_\beta$ predicted by the Arrhenius relation.""",
        "hints": ["Remember that $\beta$ is a negative quantity ($\beta < 0$).", "$L_r^+$ measures the energetic penalty required to localize two electrons at carbon $r$."],
        "solution": r"""### (a) Calculation of Localization Energies $L_1^+$ and $L_2^+$
1. **For $\alpha$-attack (C1)**:
   $$L_1^+ = E_\pi(\text{naphthalene}) - [E_\pi(\alpha\text{-arenium}) + 2\alpha]$$
   $$L_1^+ = (10\alpha + 13.683\beta) - (10\alpha + 11.384\beta) = 2.299(-\beta)$$
2. **For $\beta$-attack (C2)**:
   $$L_2^+ = E_\pi(\text{naphthalene}) - [E_\pi(\beta\text{-arenium}) + 2\alpha]$$
   $$L_2^+ = (10\alpha + 13.683\beta) - (10\alpha + 11.191\beta) = 2.492(-\beta)$$

### (b) Energetic Penalty Difference ($\Delta L^+$)
$$\Delta L^+ = L_2^+ - L_1^+ = 2.492(-\beta) - 2.299(-\beta) = 0.193(-\beta)$$
Substituting $\beta \approx -75\text{ kJ}\cdot\text{mol}^{-1}$:
$$\Delta L^+ = 0.193 \times 75\text{ kJ}\cdot\text{mol}^{-1} = \mathbf{14.48\text{ kJ}\cdot\text{mol}^{-1}} \quad (3.46\text{ kcal}\cdot\text{mol}^{-1})$$
The localization energy barrier for $\beta$-attack is $14.5\text{ kJ}\cdot\text{mol}^{-1}$ higher than for $\alpha$-attack.

### (c) Kinetic Regioselectivity Ratio ($k_\alpha / k_\beta$)
Using the Arrhenius-Eyring relationship at $T = 298.15\text{ K}$:
$$\frac{k_\alpha}{k_\beta} = \exp\left(\frac{\Delta L^+}{RT}\right)$$
$$RT = (8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (298.15\text{ K}) = 2.4788\text{ kJ}\cdot\text{mol}^{-1}$$
$$\frac{\Delta L^+}{RT} = \frac{14.48}{2.4788} \approx 5.842$$
$$\frac{k_\alpha}{k_\beta} = \exp(5.842) \approx \mathbf{344}$$
At $25^\circ\text{C}$, the reaction at the $\alpha$-position is predicted to be approximately **340 times faster** than at the $\beta$-position, in outstanding agreement with experimental kinetic nitration and bromination ratios ($>95:5$)."""
    })

    # --- ENRICH UNIT 2: ALDEHYDES AND KETONES ---
    # Section 2.1: Felkin-Anh Polar and Chelation Models with Electronegative Atoms
    u2["sections"][0]["content"] += r"""

### The Felkin-Anh Polar Model for $\alpha$-Heteroatom Carbonyls

When an aldehyde or ketone carries an electronegative heteroatom at the $\alpha$-position (such as $-\text{Cl}, -\text{Br}, -\text{OR}, -\text{NR}_2$), the classic steric classification ($L, M, S$) fails because electronic factors override pure van der Waals radii.

```
       Felkin-Anh Polar Model Transition State:
                    O
                   //
             H --- C            <=== Nucleophile Nu(-) attacks
                  / \                along Bürgi-Dunitz 107° angle
                 C   \
                / \
               R   H
               |
               X (Electronegative atom: Cl, OR)
               [sigma*(C-X) aligns parallel to pi*(C=O) LUMO]
```

In the **Felkin-Anh Polar Model** (formulated by Nguyen Trong Anh in 1976):
1. The electronegative substituent ($\text{X}$) possesses a very low-lying $\sigma^*_{\text{C-X}}$ antibonding orbital.
2. The $\text{C}-\text{X}$ bond **must orient perpendicular ($90^\circ$) to the carbonyl plane**, parallel to the $\pi^*_{\text{C=O}}$ LUMO.
3. Mixing of $\sigma^*_{\text{C-X}}$ with $\pi^*_{\text{C=O}}$ creates a lower-energy frontier LUMO ($\pi^*_{\text{mix}}$), significantly lowering the activation barrier.
4. The incoming nucleophile approaches from the face opposite the electronegative group ($\text{X}$), passing over the smaller hydrogen atom to yield the **polar Felkin-Anh diastereomer** with stereoselectivity exceeding $95:5$."""

    # Section 2.5: The Shapiro Reaction and Bamford-Stevens Manifolds
    u2["sections"][4]["content"] += r"""

### The Shapiro Reaction vs the Bamford-Stevens Reaction

Ketones can be converted regiospecifically into alkenes via arylsulfonylhydrazones (tosylhydrazones or trisylhydrazones):

```
       Tosylhydrazone Elimination Manifolds:
       Ketone + TsNH-NH2 ===> Tosylhydrazone [R-C(=N-NHTs)-CH2-R']
              |
              +--- Strong Base in Aprotic Solv. (2 equiv BuLi, 0 C) ===> Shapiro (Less Substituted Alkene)
              |
              +--- Strong Base in Protic Solv. (NaOEt, DEG, 150 C)  ===> Bamford-Stevens (More Substituted Alkene)
```

1. **The Shapiro Reaction (Organolithium Base, Aprotic Solvent)**:
   - Treatment of a tosylhydrazone or 2,4,6-triisopropylbenzenesulfonylhydrazone (trisylhydrazone) with **two equivalents of $n$-butyllithium ($n\text{-BuLi}$)** at $0^\circ\text{C}$ in anhydrous ether or THF:
     - Equivalent 1 deprotonates the acidic sulfonamide nitrogen ($-\text{NHTs}$).
     - Equivalent 2 deprotonates the **less substituted $\alpha$-carbon** (kinetic deprotonation) to form a dianion.
   - Elimination of the sulfinate anion ($\text{Ts}^-$) generates an alkenyldiazenide intermediate ($[\text{R}-\text{C}(\text{Li})=\text{CH}_2-\text{N}=\text{N}^-]$).
   - Extrusion of dinitrogen ($\text{N}_2\uparrow$) expels an **alkenyllithium carbanion**:
     $$\text{Dianion} \xrightarrow{-\text{Ts}^-, -\text{N}_2\uparrow} \text{R}-\text{C}(\text{Li})=\text{CH}_2 \tag{2.8a}$$
   - Trapping with water yields the **least substituted alkene** (non-Zaitsev). Trapping with electrophiles ($\text{CO}_2, \text{MeI}, \text{RCHO}$) produces $\alpha,\beta$-unsaturated carboxylic acids, alkylated alkenes, or allylic alcohols.
2. **The Bamford-Stevens Reaction (Weak Base, Protic or Aprotic Solvent)**:
   - Heated with sodium ethoxide in diethylene glycol ($150^\circ\text{C}$):
   - In protic solvent, a **diazoalkane** intermediate is formed, which is protonated to an alkyldiazonium ion. Loss of $\text{N}_2$ generates a **carbocation**, which undergoes E1 elimination to yield the **more substituted (Zaitsev) alkene** along with rearranged products."""

    # Add Problem 2.8 to Unit 2
    u2["problems"].append({
        "id": "prob2_8",
        "problemNumber": "2.8",
        "title": "Corey-Chaykovsky Epoxidation vs Cyclopropanation Sulfur Ylide Mechanics",
        "difficulty": "Mastery",
        "statement": r"""Dimethylsulfonium methylide ($\text{Me}_2\text{S}^+-\text{CH}_2^-$) and dimethylsulfoxonium methylide ($\text{Me}_2\text{S}(=\text{O})^+-\text{CH}_2^-$) react differently with $\alpha,\beta$-unsaturated ketones:
- Reaction of 4-phenylbut-3-en-2-one with dimethylsulfonium methylide yields an epoxide (Product A, $>90\%$).
- Reaction of 4-phenylbut-3-en-2-one with dimethylsulfoxonium methylide yields a cyclopropane (Product B, $>90\%$).
(a) Draw the structures of Products A and B.
(b) Explain why the sulfonium ylide undergoes 1,2-addition while the sulfoxonium ylide undergoes 1,4-addition using hard-soft acid-base (HSAB) principles and kinetic vs thermodynamic reversibility.
(c) Draw the intramolecular nucleophilic displacement step that closes the 3-membered ring in each case.""",
        "hints": ["Sulfonium ylide is less stable and more reactive (harder).", "Sulfoxonium ylide is resonance-stabilized by the S=O oxygen (softer and reversible)."],
        "solution": r"""### (a) Structures of Products
- **Product A (Dimethylsulfonium methylide)**: **2-methyl-2-(2-phenylethenyl)oxirane** (an allylic epoxide formed by 1,2-addition to the carbonyl group).
- **Product B (Dimethylsulfoxonium methylide)**: **1-(2-phenylcyclopropyl)ethan-1-one** (a cyclopropyl ketone formed by 1,4-conjugate addition to the alkene double bond).

### (b) HSAB and Kinetic/Thermodynamic Reversibility Rationale
1. **Dimethylsulfonium Methylide ($\text{Me}_2\text{S}^+-\text{CH}_2^-$)**:
   - This ylide lacks an electronegative oxygen atom on sulfur. The carbanion is highly localized and reactive (**hard nucleophile**).
   - It attacks the hard carbonyl carbon via kinetic **1,2-addition** ($k_{1,2} \gg k_{1,4}$).
   - Because dimethyl sulfide ($\text{Me}_2\text{S}$) is an outstanding neutral leaving group, intramolecular nucleophilic displacement by the newly formed alkoxide oxygen is extraordinarily fast ($k_{\text{ring-closure}} > k_{\text{reversal}}$):
     $$[\text{PhCH}=\text{CH}-\text{C}(\text{Me})(\text{O}^-)-\text{CH}_2-\text{S}^+\text{Me}_2] \longrightarrow \text{Epoxide} + \text{Me}_2\text{S}\uparrow$$
   - The reaction is trapped irreversibly as the **oxirane (epoxide)**.
2. **Dimethylsulfoxonium Methylide ($\text{Me}_2\text{S}(=\text{O})^+-\text{CH}_2^-$)**:
   - The carbanion is stabilized by resonance delocalization into the polar $\text{S}=\text{O}$ double bond:
     $$[\text{Me}_2\text{S}(=\text{O})^+-\text{C}^-\text{H}_2 \longleftrightarrow \text{Me}_2\text{S}^+(\text{O}^-)=\text{CH}_2]$$
   - It is significantly more stable, less basic, and constitutes a **soft nucleophile**.
   - Although 1,2-addition may occur reversibly, ring closure to an epoxide is slow because the sulfoxonium leaving group is less prone to depart.
   - The soft ylide adds preferentially via **conjugate 1,4-addition** to the soft $\beta$-carbon of the enone.
   - The resulting enolate oxygen protonates or the $\alpha$-carbanion attacks the methylene carbon, expelling dimethyl sulfoxide ($\text{DMSO}$) to form the **cyclopropane** ring."""
    })

    # --- ENRICH UNIT 3: CARBOXYLIC AND MULTIFUNCTIONAL ACIDS ---
    # Section 3.1: Gas Phase Acidity and Thermodynamic Cycles
    u3["sections"][0]["content"] += r"""

### Gas-Phase Acidities ($\Delta G^\circ_{\text{acid}}$) and Born-Haber Solvation Cycles

In solution, carboxylic acid $\text{p}K_a$ values are profoundly modulated by water solvation enthalpies:

$$\text{RCOOH}(\text{aq}) \xrightleftharpoons{} \text{RCOO}^-(\text{aq}) + \text{H}^+(\text{aq})$$

To isolate the true, unperturbed intramolecular electronic determinants of carboxyl acidity, physical chemists measure the **gas-phase Gibbs free energy of deprotonation** ($\Delta G^\circ_{\text{acid}}$):

$$\text{RCOOH}(\text{g}) \longrightarrow \text{RCOO}^-(\text{g}) + \text{H}^+(\text{g}) \tag{3.1a}$$

$$\Delta H^\circ_{\text{acid}}(\text{g}) = \text{BDE}(\text{O}-\text{H}) + \text{IP}(\text{H}) - \text{EA}(\text{RCOO}^\bullet) \tag{3.1b}$$

where:
- $\text{BDE}(\text{O}-\text{H}) \approx 440\text{ kJ}\cdot\text{mol}^{-1}$ is the homolytic bond dissociation enthalpy.
- $\text{IP}(\text{H}) = 1312\text{ kJ}\cdot\text{mol}^{-1}$ ($13.6\text{ eV}$) is the ionization potential of the hydrogen atom.
- $\text{EA}(\text{RCOO}^\bullet) \approx 320\text{–}380\text{ kJ}\cdot\text{mol}^{-1}$ is the electron affinity of the acyloxy radical.

In the gas phase:
- Formic acid ($\text{HCOOH}$): $\Delta G^\circ_{\text{acid}} = 1428\text{ kJ}\cdot\text{mol}^{-1}$
- Acetic acid ($\text{CH}_3\text{COOH}$): $\Delta G^\circ_{\text{acid}} = 1453\text{ kJ}\cdot\text{mol}^{-1}$
- Propanoic acid ($\text{CH}_3\text{CH}_2\text{COOH}$): $\Delta G^\circ_{\text{acid}} = 1445\text{ kJ}\cdot\text{mol}^{-1}$

Notice that in the gas phase, **propanoic acid is more acidic than acetic acid**! This reversal from the aqueous trend occurs because larger alkyl groups are more polarizable in a vacuum, stabilizing the negative charge on the carboxylate anion through ion-induced dipole interactions, whereas in water, larger alkyl groups disrupt the compact, highly ordered hydration sphere."""

    # Section 3.4: The Arndt-Eistert Homologation
    u3["sections"][3]["content"] += r"""

### The Arndt-Eistert Homologation: Wolff Rearrangement of $\alpha$-Diazoketones

The Arndt-Eistert synthesis (Fritz Arndt and Bernd Eistert, 1935) lengthens a carboxylic acid carbon chain by exactly one methylene unit ($-\text{CH}_2-$) without affecting existing stereocenters:

$$\text{R-COOH} \longrightarrow \text{R-CH}_2\text{-COOH} \tag{3.5a}$$

```
       The Arndt-Eistert Homologation Cascade:
       R-COOH + SOCl2 ===> R-COCl (Acyl Chloride)
              |
              | 2 equiv CH2N2 (Diazomethane, 0 C)
              v
       alpha-Diazoketone [R-CO-CH=N+=N-]  +  CH3Cl  +  N2
              |
              | Wolff Rearrangement: Ag2O or h*nu (- N2)
              v
       Ketenes [R-CH=C=O]
              |
              | H2O (Hydration)
              v
       Homologated Carboxylic Acid [R-CH2-COOH]
```

1. **Step 1: Acyl Chloride Formation**: Carboxylic acid reacts with $\text{SOCl}_2$ to yield $\text{RCOCl}$.
2. **Step 2: Diazoketone Formation**: Treatment with **two equivalents of diazomethane ($\text{CH}_2\text{N}_2$)** at $0^\circ\text{C}$:
   $$\text{RCOCl} + 2\,\text{CH}_2\text{N}_2 \longrightarrow \text{R-CO-CH}=\text{N}^+=\text{N}^- + \text{CH}_3\text{Cl} + \text{N}_2\uparrow$$
   (The second equivalent of diazomethane acts as a base to scavenge $\text{HCl}$).
3. **Step 3: The Wolff Rearrangement**:
   When the $\alpha$-diazoketone is exposed to silver(I) oxide ($\text{Ag}_2\text{O}$) or photolysis ($h\nu$), it undergoes loss of dinitrogen ($\text{N}_2\uparrow$) to yield a transient **acylcarbene**, which undergoes a concerted [1,2]-alkyl migration to form a **ketene**:
   $$\text{R-CO-CH}=\text{N}_2 \xrightarrow{\text{Ag}_2\text{O}, -\text{N}_2\uparrow} [\text{R-CO}-\ddot{\text{C}}\text{H}] \longrightarrow \text{R-CH}=\text{C}=\text{O} \quad (\text{ketene}) \tag{3.5b}$$
   Migration occurs with **100% retention of stereochemistry** at the migrating group $\text{R}$.
4. **Step 4: Nucleophilic Addition**:
   - Addition of water ($\text{H}_2\text{O}$) yields the **homologated carboxylic acid** ($\text{RCH}_2\text{COOH}$).
   - Addition of alcohols ($\text{R}'\text{OH}$) yields esters ($\text{RCH}_2\text{COOR}'$).
   - Addition of amines ($\text{R}'\text{NH}_2$) yields amides ($\text{RCH}_2\text{CONHR}'$)."""

    # Add Problem 3.8 to Unit 3
    u3["problems"].append({
        "id": "prob3_8",
        "problemNumber": "3.8",
        "title": "The Dakin-West Reaction: Mechanism of Amino Acid Conversion to $\alpha$-Amido Ketones",
        "difficulty": "Mastery",
        "statement": r"""The Dakin-West reaction (Henry Drysdale Dakin and Randolph West, 1928) transforms an $\alpha$-amino acid into an $\alpha$-acetamido ketone upon heating with acetic anhydride in pyridine:
$$\text{R-CH(NH}_2)\text{COOH} + 2\,(\text{CH}_3\text{CO})_2\text{O} \xrightarrow{\text{pyridine, }\Delta} \text{R-CH(NHCOCH}_3)\text{-CO-CH}_3 + \text{CO}_2\uparrow + 2\,\text{CH}_3\text{COOH}$$
(a) Draw the complete step-by-step mechanism showing the azlactone (oxazol-5(4H)-one) intermediate.
(b) Explain how the azlactone undergoes C-acylation at the $\alpha$-position.
(c) Identify the elementary step in which carbon dioxide ($\text{CO}_2\uparrow$) is irreversibly expelled, and explain why the original $\alpha$-stereocenter undergoes complete racemization.""",
        "hints": ["Azlactone forms by intramolecular cyclization of the N-acyl amino acid.", "The alpha-proton of the azlactone is highly acidic, forming a mesoionic enolate."],
        "solution": r"""### (a) Step-by-Step Dakin-West Mechanism
$$\begin{aligned}
\text{Step 1 (N-Acetylation)}: &\quad \text{R-CH(NH}_2)\text{COOH} + \text{Ac}_2\text{O} \longrightarrow \text{R-CH(NHAc)COOH} + \text{AcOH} \\
\text{Step 2 (Mixed Anhydride)}: &\quad \text{R-CH(NHAc)COOH} + \text{Ac}_2\text{O} \longrightarrow \text{R-CH(NHAc)COO-Ac} + \text{AcOH} \\
\text{Step 3 (Intramolecular Cyclization)}: &\quad \text{Mixed anhydride} \xrightarrow{\text{pyridine, } -\text{AcOH}} \mathbf{\text{Azlactone (4-alkyl-2-methyloxazol-5(4H)-one)}} \\
\text{Step 4 (Deprotonation & C-Acylation)}: &\quad \text{Azlactone} \xrightarrow{\text{pyridine}} [\text{Mesoionic enolate}]^- \xrightarrow{\text{Ac}_2\text{O}} \text{4-acetylazlactone} + \text{AcO}^- \\
\text{Step 5 (Ring Opening)}: &\quad \text{4-acetylazlactone} + \text{AcOH / H}_2\text{O} \longrightarrow \beta\text{-keto acid intermediate} \\
\text{Step 6 (Decarboxylation)}: &\quad \beta\text{-keto acid} \xrightarrow{-\text{CO}_2\uparrow} \mathbf{\text{R-CH(NHAc)COCH}_3} \quad (\alpha\text{-acetamido ketone})
\end{aligned}$$

### (b) C-Acylation of the Azlactone
In Step 3, the oxygen of the amide attacks the activated mixed anhydride carbonyl, closing a 5-membered **oxazol-5-one (azlactone)** ring.
The proton at C4 (the original $\alpha$-carbon) is flanked by a $\text{C}=\text{O}$ and a $\text{C}=\text{N}$ bond. Its acidity is extraordinarily high ($\text{p}K_a \approx 9\text{–}10$).
Pyridine easily deprotonates this position to generate a resonance-stabilized **aromatic-like mesoionic enolate**:
$$[\text{Azlactone Enolate}]^- + \text{Ac}_2\text{O} \longrightarrow \text{4-acetyl-4-alkyloxazol-5-one} + \text{AcO}^-$$
Nucleophilic attack on acetic anhydride occurs selectively at the $\alpha$-carbon.

### (c) Decarboxylation & Total Racemization
1. **Decarboxylation Step**: Hydrolytic ring opening of the 4-acetylazlactone generates a $\beta$-keto carboxylic acid:
   $$\text{R}-\text{C}(\text{COCH}_3)(\text{NHAc})-\text{COOH}$$
   As demonstrated in Unit 3, $\beta$-keto acids undergo rapid, spontaneous thermal decarboxylation via a 6-membered cyclic transition state, expelling $\text{CO}_2\uparrow$ as a gas.
2. **Loss of Chirality (Complete Racemization)**:
   In Step 4, deprotonation of the azlactone converts the tetrahedral $sp^3$ chiral $\alpha$-carbon into a completely **planar $sp^2$-hybridized enolate** intermediate possessing mirror symmetry. All optical activity is permanently destroyed; the resulting $\alpha$-acetamido ketone is **100% racemic**."""
    })

    print("Units 1, 2, and 3 successfully expanded!")
