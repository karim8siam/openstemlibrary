#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_natural_products_units_4_5_6.py
Builds Units 4, 5, and 6 (Sections 1-7, Solved Problems 1-7) for Chemistry of Natural Products.
Strictly zero course numbers, codes, or marks.
Raw triple quotes used throughout to prevent any escape sequence issues.
"""

def get_units_4_5_6():
    units = []

    # =========================================================================
    # UNIT 4: Carbohydrates I: Monosaccharides, Stereochemistry & Conformation
    # =========================================================================
    u4 = {
        "id": "unit-4",
        "unitNumber": 4,
        "title": "Unit 4: Carbohydrates I: Monosaccharides, Stereochemistry & Conformation",
        "leadSummary": "Comprehensive structural and stereochemical treatment of monosaccharides: Fischer stereochemical conventions, Emil Fischer's classical proof of the configuration of D-glucose, Kiliani-Fischer chain extension, Wohl and Ruff degradations, mutarotation dynamics and anomeric equilibria, pyranose chair conformational energetics ($^4C_1$), the stereoelectronic anomeric effect, and osazone reaction mechanisms.",
        "simulations": ["sim_nat_glucose_mutarotation_chair"],
        "sections": [
            {
                "id": "sec-4-1",
                "secNumber": "4.1",
                "title": "Monosaccharides: Definition, Classification & Stereochemical Nomenclature",
                "content": r"""Monosaccharides are polyhydroxy aldehydes (aldoses) or polyhydroxy ketones (ketoses) with the general stoichiometric formula $(CH_2O)_n$ where $n \ge 3$. They serve as fundamental metabolic fuels and the monomeric units of complex glycans and nucleic acids.

### Stereochemical Nomenclature: The D/L System
The absolute configuration of monosaccharides is defined relative to the reference standard **glyceraldehyde (2,3-dihydroxypropanal)**, established by Emil Fischer and later confirmed crystallographically by Bijvoet:
- In a vertical Fischer projection with the most oxidized carbon (C1 for aldoses) at the top:
  - If the hydroxyl group on the **highest-numbered chiral stereocenter** (C5 in hexoses) points to the **right**, the sugar belongs to the **D-series**.
  - If it points to the **left**, the sugar belongs to the **L-series**.
- The D/L descriptor denotes configurational family only; it does not indicate the sign of optical rotation ($(+)$ dextrorotatory or $(-)$ levorotatory). Natural D-glucose is dextrorotatory ($D-(+)$-glucose), whereas natural D-fructose is strongly levorotatory ($D-(-)$-fructose).

### Epimers and Diastereomers
Aldohexoses possess $n=4$ chiral centers, yielding $2^4 = 16$ stereoisomers (8 enantiomeric pairs of D/L-aldoses).
- **Epimers**: Diastereomers that differ in stereochemical configuration at **exactly one** chiral carbon:
  - D-Mannose is the **C2-epimer** of D-glucose.
  - D-Allose is the **C3-epimer** of D-glucose.
  - D-Galactose is the **C4-epimer** of D-glucose."""
            },
            {
                "id": "sec-4-2",
                "secNumber": "4.2",
                "title": "Emil Fischer's Classical Proof of the Configuration of D-(+)-Glucose",
                "content": r"""Emil Fischer was awarded the 1902 Nobel Prize in Chemistry in large part for his deductive elucidation of the relative configuration of the four chiral centers of D-glucose.

### The Deductive Proof in Four Major Steps
1. **D-Arabinose Yields D-Glucose and D-Mannose (Kiliani-Fischer Extension)**:
   Kiliani-Fischer cyanohydrin chain extension of the aldopentose (-)-arabinose introduces a new stereocenter at C2, producing two aldohexoses: (+)-glucose and (+)-mannose. Therefore, D-glucose and D-mannose must have **identical configurations at C3, C4, and C5**, differing solely at C2.
2. **Nitric Acid Oxidation of Arabinose**:
   Oxidation of D-(-)-arabinose with nitric acid ($\text{HNO}_3$) oxidizes C1 (CHO) and C5 ($\text{CH}_2\text{OH}$) to carboxylic acids, yielding an **optically active aldaric acid** (arabinaric acid).
   - This rules out any configuration that would possess a plane of symmetry ($meso$). Thus, the C2 and C3 hydroxyls of D-arabinose must point in **opposite directions** in the Fischer projection.
3. **Nitric Acid Oxidation of D-Glucose and D-Mannose**:
   Nitric acid oxidation of (+)-glucose yields **D-glucaric acid (saccharic acid)**, which is **optically active**.
   Nitric acid oxidation of (+)-mannose yields **D-mannaric acid**, which is also **optically active**.
   - This proves that neither glucose nor mannose has an aldaric acid with internal plane of symmetry. This eliminates two possible aldohexose pairs (galactose/talose and allose/altrose families).
4. **The End-to-End Inversion Proof (The Fischer Masterstroke)**:
   Fischer synthesized another aldohexose, **L-(+)-gulose**, by interchanging the terminal C1 and C6 functional groups of D-glucose (converting C1 to $\text{CH}_2\text{OH}$ and C6 to $\text{CHO}$).
   - Upon oxidation with nitric acid, both **D-glucose and L-gulose yield the exact same aldaric acid (D-glucaric acid)**!
   - For an aldohexose to yield the same aldaric acid upon end-to-end inversion without being a meso compound, the C4 hydroxyl must reside on the **right** while the C3 hydroxyl resides on the **left**.
   Combined with the D-assignment at C5 (OH on the right), this uniquely establishes the Fischer projection of **D-(+)-glucose**:
   - C2: $-\text{OH}$ on Right
   - C3: $-\text{OH}$ on Left
   - C4: $-\text{OH}$ on Right
   - C5: $-\text{OH}$ on Right"""
            },
            {
                "id": "sec-4-3",
                "secNumber": "4.3",
                "title": "Chain Extension and Degradation Reactions: Kiliani-Fischer, Wohl & Ruff",
                "content": r"""Chemical manipulation of carbohydrate chain lengths enables systematic interconversion between aldoses.

### Kiliani-Fischer Chain Extension
Extends an aldose by one carbon atom:
1. **Cyanohydrin Formation**: Addition of hydrogen cyanide ($\text{HCN}$) to the C1 aldehyde creates a new stereocenter at C2, generating a diastereomeric mixture of cyanohydrins:
   $$\text{R-CHO} + \text{HCN} \to \text{R-CH(OH)-CN} \quad (\text{Diastereomeric pair})$$
2. **Hydrolysis and Lactonization**: Alkaline or acid hydrolysis of the nitrile affords aldonic acids, which spontaneously form 1,4-lactones ($\gamma$-aldonolactones).
3. **Selective Reduction**: Reduction with sodium amalgam ($\text{Na/Hg}$) at $\text{pH } 3–4$ or catalytic hydrogenation over $\text{Pd/BaSO}_4$ reduces the lactone to an aldose without over-reducing to a polyol:
   $$\text{Aldonolactone} \xrightarrow{\text{Na/Hg, H}^+} \text{Extended Aldose}$$

### Wohl Degradation (Chain Shortening)
Removes C1 from an aldose:
1. **Oxime Formation**: Reaction with hydroxylamine ($\text{NH}_2\text{OH}$) converts C1 to an aldoxime: $\text{R-CH}=\text{NOH}$.
2. **Dehydration and Acetylation**: Heating with acetic anhydride ($\text{Ac}_2\text{O}$) dehydrates the oxime to a cyanohydrin acetate while acetylating all hydroxyl groups.
3. **Decyanation**: Treatment with methanolic ammonia ($\text{NH}_3 / \text{MeOH}$) deacetylates the ester groups and triggers retro-cyanohydrin cleavage, releasing $\text{HCN}$ and yielding the shortened aldose.

### Ruff Degradation
1. Oxidation of the aldose with bromine water ($\text{Br}_2 / \text{H}_2\text{O}$) yields the calcium aldonate salt.
2. Oxidative decarboxylation using Fenton's reagent ($\text{Fe}^{3+} / \text{H}_2\text{O}_2$) eliminates C1 as $\text{CO}_2$, yielding the lower aldose:
   $$\text{R-CH(OH)-COO}^- + \text{H}_2\text{O}_2 \xrightarrow{\text{Fe}^{3+}} \text{R-CHO} + \text{CO}_2 + \text{OH}^- + \text{H}_2\text{O}$$"""
            },
            {
                "id": "sec-4-4",
                "secNumber": "4.4",
                "title": "Cyclic Hemiacetal Formations, Pyranose/Furanose Tautomerism & Haworth Formalism",
                "content": r"""In aqueous solution, open-chain monosaccharides exist in dynamic equilibrium with cyclic intramolecular hemiacetals.

### Thermodynamics of Ring Closure
The intramolecular nucleophilic attack of a hydroxyl group onto the electrophilic carbonyl carbon forms stable 5- or 6-membered rings:
- **Pyranose Rings**: Six-membered cyclic hemiacetals formed by reaction of the C5-OH with C1 (analogs of tetrahydropyran).
- **Furanose Rings**: Five-membered cyclic hemiacetals formed by reaction of the C4-OH with C1 (analogs of tetrahydrofuran).
For D-glucose at equilibrium in water at $25^\circ\text{C}$, the distribution is:
$$\text{Pyranose forms } (>99.7\%) \gg \text{Furanose forms } (<0.1\%) \gg \text{Open-chain aldehyde } (0.002\%)$$
The overwhelming thermodynamic stability of the pyranose form arises from the relief of angle strain and optimal staggered conformations accessible in the six-membered chair.

### The Haworth Formalism
Sir Norman Haworth introduced planar projection formulas to represent cyclic sugars:
- The pyranose ring is drawn as a flat hexagon viewed edge-on, with the ring oxygen placed at the upper right.
- Substituents that point to the **right** in a standard Fischer projection point **downward** in the Haworth projection.
- Substituents that point to the **left** in the Fischer projection point **upward** in the Haworth projection.
- For D-sugars, the bulky C6 hydroxymethyl group ($-\text{CH}_2\text{OH}$) points **upward** above the ring plane."""
            },
            {
                "id": "sec-4-5",
                "secNumber": "4.5",
                "title": "Mutarotation: Kinetics, Anomeric Carbon Equilibria & Polarimetry",
                "content": r"""Mutarotation is the spontaneous change in the specific optical rotation of an optically active carbohydrate solution as anomeric epimers equilibrate through the open-chain aldehyde.

### The Anomeric Carbon and Diastereomeric Forms
Cyclization transforms the achiral C1 carbonyl carbon into a new chiral stereocenter, termed the **anomeric carbon**:
- **$\alpha$-Anomer**: The anomeric hydroxyl group ($-\text{OH}$) is **trans** to the C6 $-\text{CH}_2\text{OH}$ group in the Haworth projection (points **downward** for D-glucose).
- **$\beta$-Anomer**: The anomeric hydroxyl group is **cis** to the C6 $-\text{CH}_2\text{OH}$ group in the Haworth projection (points **upward** for D-glucose).

### Optical Rotation Dynamics of D-Glucose
- Pure crystalline $\alpha$-D-glucopyranose exhibits an initial specific rotation of $[\alpha]_D^{20} = +112.2^\circ$.
- Pure crystalline $\beta$-D-glucopyranose exhibits an initial specific rotation of $[\alpha]_D^{20} = +18.7^\circ$.
- When dissolved in water, both solutions spontaneously undergo mutarotation, asymptotically approaching an identical equilibrium value:
  $$[\alpha]_D^{\text{eq}} = \mathbf{+52.7^\circ}$$

### Mechanism and General Acid-Base Catalysis
Mutarotation requires ring opening and re-closure, mediated by amphoteric general acid-base catalysis (e.g., Lowry's classic demonstration that mutarotation stops in pure benzene or pyridine, but proceeds rapidly in a mixture of pyridine and cresol):
$$\alpha\text{-Pyranose} \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} \text{Open-Chain Aldehyde} \underset{k_2}{\overset{k_{-2}}{\rightleftharpoons}} \beta\text{-Pyranose}$$
Because the concentration of the open-chain intermediate is infinitesimal ($[Open] \approx 0.002\%$), applying the Steady-State Approximation yields a pseudo-first-order relaxation rate law:
$$\frac{d[\alpha]}{dt} = -(k_f + k_r) ([\alpha]_t - [\alpha]_{\text{eq}})$$
where $k_{\text{obs}} = k_f + k_r$."""
            },
            {
                "id": "sec-4-6",
                "secNumber": "4.6",
                "title": "Conformational Analysis: Chair States ($^4C_1$), 1,3-Diaxial Strain & The Anomeric Effect",
                "content": r"""While Haworth projections represent ring topology, hexopyranoses adopt puckered **chair conformations** ($^4C_1$ and $^1C_4$) to eliminate torsional strain.

### The $^4C_1$ Conformation of $\beta$-D-Glucopyranose
In the $^4C_1$ chair (carbon-4 above the reference plane, carbon-1 below):
- Every single non-hydrogen substituent (C2-OH, C3-OH, C4-OH, C5-$\text{CH}_2\text{OH}$, and the anomeric C1-OH) resides in an **equatorial position**.
- $\beta$-D-glucopyranose is the **only D-aldohexose** that can orient all five non-hydrogen substituents simultaneously in equatorial positions, minimizing 1,3-diaxial steric interactions and torsional strain. This structural feature explains why D-glucose is the most abundant monosaccharide in nature.

### The Stereoelectronic Anomeric Effect
According to classical steric analysis (Winstein-Holness A-values), equatorial substituents are favored over axial substituents ($\Delta G^\circ < 0$). However, electronegative substituents ($-\text{OMe}, -\text{Cl}, -\text{F}$, and to a lesser extent $-\text{OH}$) at the anomeric C1 position display an anomalous thermodynamic preference for the **axial orientation**:
1. **Dipole Minimization**: In the equatorial conformer, the dipole of the endocyclic ring oxygen and the dipole of the C1-X bond align in parallel directions, creating repulsive dipole-dipole interactions. In the axial conformer, the two dipoles are opposed.
2. **Hyperconjugation ($n \to \sigma^*$ Overlap)**: A non-bonding lone pair of the endocyclic ring oxygen ($n_O$) lies anti-periplanar to the axial $\text{C}1-\text{X}$ $\sigma^*$ antibonding orbital, allowing stabilizing electron delocalization:
   $$n_O \longrightarrow \sigma^*_{\text{C1-X}}$$
   This stereoelectronic overlap shortens the C1-O(ring) bond and stabilizes the axial anomer by $4.0 - 6.5\text{ kJ/mol}$."""
            },
            {
                "id": "sec-4-7",
                "secNumber": "4.7",
                "title": "Osazone Formation: Mechanism, Amadori Rearrangements & Fischer Diagnostics",
                "content": r"""When an aldose or ketose is heated with excess phenylhydrazine ($\text{PhNHNH}_2$, 3 equivalents) in acetic acid buffer, it undergoes a characteristic reaction yielding a yellow crystalline **osazone (diphenylhydrazone)**.

### Stoichiometry and Stepwise Mechanism
The reaction consumes exactly three moles of phenylhydrazine:
$$\text{Aldose} + 3\text{ PhNHNH}_2 \to \text{Osazone} + \text{PhNH}_2 + \text{NH}_3 + 2\text{ H}_2\text{O}$$
1. **Mono-Hydrazone Formation**: The C1 aldehyde condenses with the first equivalent of phenylhydrazine to form an aldo-phenylhydrazone:
   $$\text{R-CH(OH)-CHO} + \text{PhNHNH}_2 \to \text{R-CH(OH)-CH}=\text{N-NHPh} + \text{H}_2\text{O}$$
2. **Internal Redox / Amadori-Type Rearrangement**: Phenylhydrazine tautomerizes to an ene-hydrazine intermediate. An intramolecular oxidation occurs: the C2 secondary alcohol is oxidized to a ketone ($\text{C}=\text{O}$), while the $\text{N-N}$ bond of the hydrazone is reduced, releasing **aniline ($\text{PhNH}_2$)** and **ammonia ($\text{NH}_3$)**.
3. **Double Hydrazone Condensation**: The C2 ketone and C1 imine condense with two additional equivalents of phenylhydrazine to form the bis-phenylhydrazone (**osazone**).
4. **Chelation Stabilization**: Osazone crystals are exceptionally insoluble and stable because they adopt a quasi-aromatic six-membered ring stabilized by an **intramolecular hydrogen bond** between the N-H of the C2 hydrazone and the imine nitrogen of C1.

### Diagnostic Role in Fischer's Proof
Because osazone formation oxidizes C2 into a hydrazone, **all stereochemical information at C2 is erased**.
- D-Glucose, D-Mannose, and D-Fructose yield the **identical osazone (D-glucosazone)** with identical melting point ($208^\circ\text{C}$), crystal morphology (needle-shaped rosettes), and optical rotation.
- This proved that D-glucose and D-mannose are **C2-epimers** and share identical stereocenters at C3, C4, and C5 with D-fructose."""
            }
        ],
        "problems": [
            {
                "id": "prob-4-1",
                "problemNumber": "4.1",
                "title": "Complete Deductive Logic and Proof of Emil Fischer's (+)-Glucose Configuration",
                "difficulty": "Advanced",
                "statement": r"""Reconstruct the mathematical and stereochemical logic used by Emil Fischer to deduce the configuration of D-(+)-glucose:
(a) For an aldohexose ($\text{HOCH}_2-(\text{CHOH})_4-\text{CHO}$), how many possible D-stereoisomers exist?
(b) Given that D-(-)-arabinose on Kiliani-Fischer homologation yields D-(+)-glucose and D-(+)-mannose, and that nitric acid oxidation of D-(-)-arabinose produces an optically active dicarboxylic acid, eliminate the impossible configurations among the eight D-aldohexoses.
(c) Given that oxidation of both D-glucose and D-mannose produces optically active aldaric acids, and that L-gulose (the C1-C6 inverted isomer of D-glucose) yields the identical aldaric acid as D-glucose, show that only one unique stereochemical structure satisfies all data.""",
                "hints": [
                    r"Number of D-aldohexoses = 2^3 = 8 isomers.",
                    r"Draw the two possible configurations for D-arabinose that yield an optically active aldaric acid.",
                    r"Check for planes of symmetry in the aldaric acids of all candidate hexoses."
                ],
                "solution": r"""### Step 1: Enumeration of Candidate D-Aldohexoses
An aldohexose has 4 chiral centers (C2, C3, C4, C5). Fixing C5 in the D-configuration ($-\text{OH}$ on the right) leaves $2^3 = 8$ possible D-aldohexoses:
allose, altrose, glucose, mannose, gulose, idose, galactose, talose.

### Step 2: D-Arabinose Kiliani-Fischer Homologation and Oxidation
1. D-(-)-Arabinose is an aldopentose with 3 chiral centers (C2, C3, C4). C4 is fixed as D ($-\text{OH}$ on right).
2. Nitric acid oxidation of D-arabinose yields **arabinaric acid** ($\text{HOOC}-(\text{CHOH})_3-\text{COOH}$).
   - Arabinaric acid is **optically active**.
   - If C2 and C3 had their $-\text{OH}$ groups on the same side (both right or both left), arabinaric acid would possess an internal mirror plane passing through C3 and be an optically inactive $meso$ compound.
   - Therefore, in D-arabinose, the $-\text{OH}$ groups at C2 and C3 must point in **opposite directions** (one left, one right).
3. Kiliani-Fischer extension of D-arabinose yields D-glucose and D-mannose. Therefore:
   - D-Glucose and D-Mannose differ only at C2.
   - At C3, C4, and C5, both sugars have the exact configurations inherited from D-arabinose: C3-OH and C4-OH must point in opposite directions!
   - This eliminates allose/altrose (where C3 and C4 point in the same direction) and leaves only two structural pairs:
     - **Pair I**: C3-left, C4-right, C5-right (glucose/mannose candidate)
     - **Pair II**: C3-right, C4-left, C5-right (galactose/talose candidate)

### Step 3: Nitric Acid Oxidation of Glucose, Mannose, and Galactose
- Oxidation of Pair II candidates: Galactose yields **galactaric acid (mucic acid)**, which has a plane of symmetry ($meso$) and is optically inactive.
- Experimentally, D-glucaric acid and D-mannaric acid are **both optically active**. This eliminates Pair II and confirms that D-glucose and D-mannose belong to **Pair I** (C3-left, C4-right, C5-right).

### Step 4: End-to-End Inversion (D-Glucose vs L-Gulose)
In Pair I, the two C2-epimers are:
- Isomer A (C2-right): C2-R, C3-L, C4-R, C5-R.
- Isomer B (C2-left): C2-L, C3-L, C4-R, C5-R.
Let us examine the aldaric acid formed by inverting the ends (rotating the Fischer projection by $180^\circ$ in the plane of the paper):
- For Isomer B (mannaric acid): Inverting C1 and C6 yields the exact same molecule (mannaric acid is symmetric under $C_2$ rotational axis).
- For Isomer A (glucaric acid): Inverting C1 and C6 yields an aldaric acid derived from an entirely different sugar, **L-gulose**!
Because D-glucaric acid can be prepared from two distinct aldohexoses (D-glucose and L-gulose), **D-(+)-glucose must be Isomer A**:
$$\mathbf{C2\text{-OH: Right}, \quad C3\text{-OH: Left}, \quad C4\text{-OH: Right}, \quad C5\text{-OH: Right}}$$
This rigorously proves the configuration of D-glucose."""
            },
            {
                "id": "prob-4-2",
                "problemNumber": "4.2",
                "title": "Mutarotation Kinetics and Equilibrium Distribution of D-Glucopyranose",
                "difficulty": "Intermediate",
                "statement": r"""At $25^\circ\text{C}$ in aqueous solution, the specific optical rotation of pure $\alpha$-D-glucopyranose is $[\alpha]_\alpha = +112.2^\circ$, and that of pure $\beta$-D-glucopyranose is $[\alpha]_\beta = +18.7^\circ$. At mutarotational equilibrium, the observed rotation settles at $[\alpha]_{\text{eq}} = +52.7^\circ$.
(a) Assuming that open-chain and furanose forms are negligible at equilibrium, calculate the equilibrium mole fractions $x_\alpha$ and $x_\beta$.
(b) Compute the equilibrium constant $K_{\text{eq}} = [\beta] / [\alpha]$ and the standard free energy difference $\Delta G^\circ = G^\circ_\beta - G^\circ_\alpha$ in $\text{kJ/mol}$.
(c) A fresh solution of $\alpha$-D-glucopyranose undergoes mutarotation with an observed forward relaxation rate constant $k_{\text{obs}} = 0.0240\text{ min}^{-1}$. Calculate the individual forward ($k_1$) and reverse ($k_{-1}$) rate constants for the interconversion: $\alpha \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} \beta$.""",
                "hints": [
                    r"Specific rotation at equilibrium is [\alpha]_{eq} = x_\alpha [\alpha]_\alpha + x_\beta [\alpha]_\beta where x_\alpha + x_\beta = 1.",
                    r"Use \Delta G^\circ = -RT \ln K_{eq}.",
                    r"Remember k_{obs} = k_1 + k_{-1} and K_{eq} = k_1 / k_{-1}."
                ],
                "solution": r"""### Step 1: Equilibrium Mole Fractions
Let $x_\alpha$ and $x_\beta$ be the mole fractions, with $x_\alpha + x_\beta = 1 \implies x_\beta = 1 - x_\alpha$:
$$[\alpha]_{\text{eq}} = x_\alpha [\alpha]_\alpha + (1 - x_\alpha) [\alpha]_\beta$$
$$+52.7^\circ = x_\alpha (112.2) + (1 - x_\alpha) (18.7) = 18.7 + 93.5 x_\alpha$$
$$93.5 x_\alpha = 52.7 - 18.7 = 34.0$$
$$x_\alpha = \frac{34.0}{93.5} = 0.3636 \implies \mathbf{36.4\%}$$
$$x_\beta = 1 - 0.3636 = 0.6364 \implies \mathbf{63.6\%}$$

### Step 2: Equilibrium Constant and Free Energy Difference
The equilibrium constant is:
$$K_{\text{eq}} = \frac{[\beta]}{[\alpha]} = \frac{0.6364}{0.3636} = \mathbf{1.750}$$
The standard free energy difference at $T = 298.15\text{ K}$:
$$\Delta G^\circ = -R T \ln K_{\text{eq}} = -(8.314\text{ J/(mol}\cdot\text{K)})(298.15\text{ K}) \ln(1.750)$$
$$\Delta G^\circ = -2478.9 \times 0.5596 = -1387\text{ J/mol} = \mathbf{-1.39\text{ kJ/mol}}$$
The $\beta$-anomer is thermodynamically favored over the $\alpha$-anomer by $1.39\text{ kJ/mol}$.

### Step 3: Rate Constants Calculation
We have the system of two equations:
1. $k_1 + k_{-1} = k_{\text{obs}} = 0.0240\text{ min}^{-1}$
2. $\frac{k_1}{k_{-1}} = K_{\text{eq}} = 1.750 \implies k_1 = 1.750 k_{-1}$
Substituting:
$$1.750 k_{-1} + k_{-1} = 2.750 k_{-1} = 0.0240\text{ min}^{-1}$$
$$k_{-1} = \frac{0.0240}{2.750} = \mathbf{0.00873\text{ min}^{-1}} \quad (1.45\times 10^{-4}\text{ s}^{-1})$$
$$k_1 = 1.750 \times 0.00873 = \mathbf{0.01527\text{ min}^{-1}} \quad (2.55\times 10^{-4}\text{ s}^{-1})$$"""
            },
            {
                "id": "prob-4-3",
                "problemNumber": "4.3",
                "title": "Hyperconjugation and Dipole Origins of the Anomeric Effect",
                "difficulty": "Advanced",
                "statement": r"""In cyclohexanol, the equatorial conformer is favored over the axial conformer with an A-value of $-\Delta G^\circ = 4.0\text{ kJ/mol}$. However, for D-glucopyranose in water, the equatorial $\beta$-anomer is favored by only $1.39\text{ kJ/mol}$, and in non-polar solvents (e.g., methanol or chloroform with methyl D-glucopyranoside), the axial $\alpha$-anomer becomes the predominant species ($67\%\text{ axial}$).
(a) Deconvolve the experimental free energy difference into the steric steric A-value contribution ($\Delta G^\circ_{\text{steric}}$) and the stereoelectronic anomeric stabilization ($\Delta G^\circ_{\text{anomeric}}$) for D-glucopyranose in water.
(b) Explain the molecular orbital basis of the anomeric effect ($n \to \sigma^*$ delocalization) and why the magnitude of the anomeric effect increases markedly as solvent dielectric constant decreases.""",
                "hints": [
                    r"\Delta G^\circ_{total} = \Delta G^\circ_{steric} + \Delta G^\circ_{anomeric}.",
                    r"The A-value represents the steric penalty of placing an OH group in the axial position.",
                    r"In non-polar solvents, dipole-dipole repulsion in the equatorial conformer is not screened by solvent dielectric constant."
                ],
                "solution": r"""### Step 1: Deconvolution of Free Energy Contributions
For placing an $-\text{OH}$ group at C1 of a pyranose ring:
- In the absence of stereoelectronic effects (pure steric strain), the equatorial anomer is stabilized by the classical A-value:
  $$\Delta G^\circ_{\text{steric}} = G^\circ_{\text{eq}} - G^\circ_{\text{ax}} = -A_{\text{OH}} \approx -4.0\text{ kJ/mol}$$
- The total observed free energy difference in water is:
  $$\Delta G^\circ_{\text{obs}} = G^\circ_\beta - G^\circ_\alpha = -1.39\text{ kJ/mol}$$
- Because $\Delta G^\circ_{\text{obs}} = \Delta G^\circ_{\text{steric}} + \Delta G^\circ_{\text{anomeric}}$:
  $$-1.39 = -4.00 + \Delta G^\circ_{\text{anomeric}}$$
  $$\Delta G^\circ_{\text{anomeric}} = -1.39 - (-4.00) = \mathbf{+2.61\text{ kJ/mol}}$$
This positive term represents the stereoelectronic stabilization that favors the **axial $\alpha$-anomer** over the equatorial $\beta$-anomer, reducing the net preference for the equatorial form from $4.0\text{ kJ/mol}$ down to only $1.39\text{ kJ/mol}$.

### Step 2: Molecular Orbital and Solvent Dielectric Dependence
1. **Hyperconjugation ($n_O \to \sigma^*_{\text{C-O}}$)**:
   In the axial anomer, the non-bonding $2p$ orbital lone pair of the endocyclic ring oxygen ($O_5$) is oriented perfectly anti-periplanar ($180^\circ$ dihedral angle) to the $\sigma^*$ antibonding orbital of the axial $\text{C}1-\text{O}1$ bond. This geometry enables maximum overlap:
   $$\Delta E = -\frac{2 |H_{ij}|^2}{\epsilon_{\sigma^*} - \epsilon_{n}}$$
   In the equatorial anomer, the dihedral angle is approximately $60^\circ$ (gauche), resulting in negligible overlap.
2. **Dielectric Screening of Dipoles**:
   In the equatorial anomer, the bond dipoles of the $C_1-O_1$ bond and the $C_5-O_5$ ring bond point in approximately the same direction, generating electrostatic repulsion.
   - In water ($\epsilon_r = 78.5$), high solvent dielectric polarization screens these dipoles, minimizing electrostatic repulsion.
   - In non-polar solvents ($\text{CHCl}_3, \epsilon_r = 4.8$), dipole screening vanishes. The electrostatic penalty on the equatorial anomer increases sharply, making the axial anomer ($\alpha$) the thermodynamically dominant form."""
            },
            {
                "id": "prob-4-4",
                "problemNumber": "4.4",
                "title": "Malaprade Periodate Cleavage Stoichiometry of Methyl Glycosides vs Free Hexoses",
                "difficulty": "Intermediate",
                "statement": r"""Periodic acid ($\text{HIO}_4$) cleaves vicinal diols, $\alpha$-hydroxy aldehydes, and $\alpha$-hydroxy ketones (Malaprade reaction).
(a) Write the balanced cleavage equation and calculate the moles of $\text{HIO}_4$ consumed and moles of formic acid ($\text{HCOOH}$) and formaldehyde ($\text{HCHO}$) produced per mole of open-chain D-glucose.
(b) Methyl $\alpha$-D-glucopyranoside was treated with excess periodic acid. Calculate the moles of $\text{HIO}_4$ consumed and identify all organic products. Explain why no formaldehyde is formed.""",
                "hints": [
                    r"Each vicinal C-C cleavage consumes 1 mole of HIO4.",
                    r"Primary alcohol -CH2OH gives HCHO; secondary alcohol -CH(OH)- gives HCOOH; terminal aldehyde gives HCOOH.",
                    r"In a pyranoside ring, C1 is an acetal (protected) and C6 is part of the side chain."
                ],
                "solution": r"""### Step 1: Open-Chain D-Glucose Cleavage
Open-chain D-glucose is:
$$\text{CHO}-\text{CHOH}-\text{CHOH}-\text{CHOH}-\text{CHOH}-\text{CH}_2\text{OH}$$
There are 5 vicinal $\text{C-C}$ bonds (C1-C2, C2-C3, C3-C4, C4-C5, C5-C6):
- Cleaving 5 bonds consumes **5 moles of $\text{HIO}_4$**.
- Carbon-1 ($\text{CHO}$) oxidizes to **Formic acid ($\text{HCOOH}$)**: 1 mole.
- Carbons 2, 3, 4, and 5 (internal $-\text{CHOH}-$ groups) each oxidize to **Formic acid ($\text{HCOOH}$)**: 4 moles.
- Carbon-6 ($-\text{CH}_2\text{OH}$) oxidizes to **Formaldehyde ($\text{HCHO}$)**: 1 mole.
$$\text{D-Glucose} + 5\text{ HIO}_4 \to 5\text{ HCOOH} + 1\text{ HCHO} + 5\text{ HIO}_3 + \text{H}_2\text{O}$$
Summary: **$5\text{ HIO}_4$ consumed, $5\text{ HCOOH}$, $1\text{ HCHO}$**.

### Step 2: Methyl $\alpha$-D-Glucopyranoside Cleavage
In methyl $\alpha$-D-glucopyranoside:
- C1 is a protected acetal ($-\text{CH(OMe)}-$), with no free $-\text{OH}$.
- C2, C3, and C4 possess contiguous hydroxyl groups: $-\text{C}^2\text{HOH}-\text{C}^3\text{HOH}-\text{C}^4\text{HOH}-$.
- C5 is involved in the ring oxygen bridge and has no free hydroxyl; C6 is $-\text{CH}_2\text{OH}$ attached to C5.
- Therefore, only two vicinal bonds are cleaved: C2-C3 and C3-C4:
  - This consumes **2 moles of $\text{HIO}_4$**.
  - Carbon-3, having cleaved bonds on both sides, is released as **1 mole of Formic acid ($\text{HCOOH}$)**.
  - Carbons 1, 2, 4, 5, and 6 remain linked as a dialdehyde (a cyclic acetal dialdehyde core).
- **Zero formaldehyde is produced** because C6 is not vicinal to any free hydroxyl group (C5 is an ether carbon)."""
            },
            {
                "id": "prob-4-5",
                "problemNumber": "4.5",
                "title": "Kiliani-Fischer Diastereoselectivity and Aldonolactone Separation",
                "difficulty": "Intermediate",
                "statement": r"""In the Kiliani-Fischer synthesis, nucleophilic addition of cyanide to D-arabinose generates two epimeric aldononitriles: D-glucononitrile and D-mannononitrile in a non-equimolar 65:35 ratio.
(a) Explain why cyanide addition to D-arabinose is diastereoselective, drawing the Felkin-Anh or Cram open-chain conformational model.
(b) After hydrolysis to D-gluconic acid and D-mannonic acid, explain how the two isomers are separated by differential crystallization of their 1,4-lactones ($\gamma$-lactones).""",
                "hints": [
                    r"The aldehyde C1 is prochiral, but carbons C2, C3, C4 of arabinose are chiral, imparting asymmetric induction.",
                    r"In the Felkin-Anh model, the largest group at C2 (the alpha carbon) aligns perpendicular to the carbonyl.",
                    r"Gamma-lactones have different ring conformations and crystallizability."
                ],
                "solution": r"""### Step 1: Diastereoselective Cyanide Addition
The aldehyde carbon (C1) of D-arabinose is planar and prochiral. Nucleophilic attack by cyanide ($\text{CN}^-$) can occur from either the re or si face:
- However, the adjacent $\alpha$-carbon (C2 in arabinose, which becomes C3 in the hexose) possesses a stereocenter with an $-\text{OH}$ group, a proton, and the remaining carbohydrate chain.
- According to the **Felkin-Anh model**:
  - The largest substituent (the polyhydroxyalkyl chain, $-\text{CH(OH)CH(OH)CH}_2\text{OH}$) is placed perpendicular to the carbonyl dipole ($90^\circ$).
  - The nucleophile ($\text{CN}^-$) approaches the carbonyl group along the Bürgi-Dunitz angle ($\approx 107^\circ$) from the least sterically hindered trajectory (past the small hydrogen atom rather than the medium $-\text{OH}$ group).
  - This preferential facial attack favors formation of the glucononitrile diastereomer ($65\%$) over the mannononitrile diastereomer ($35\%$).

### Step 2: Separation via $\gamma$-Lactones
Upon acidic hydrolysis:
- D-Gluconic acid and D-mannonic acid spontaneously dehydrate to form five-membered 1,4-lactones ($\gamma$-aldonolactones).
- In D-mannono-$\gamma$-lactone, the C2 and C3 hydroxyls are on opposite sides, creating a highly rigid, readily crystallizable bicyclic-like conformation with a sharp melting point ($151^\circ\text{C}$).
- In D-glucono-$\gamma$-lactone, the molecular shape favors a six-membered $\delta$-lactone (1,5-lactone) or remains an uncrystallizable syrup under equivalent solvent conditions.
- Fractional crystallization from hot 95% ethanol yields pure crystalline D-mannono-1,4-lactone, leaving D-gluconate in the mother liquor, achieving quantitative preparative separation."""
            },
            {
                "id": "prob-4-6",
                "problemNumber": "4.6",
                "title": "Osazone Reaction Mechanism and Intramolecular Electron-Transfer Stoichiometry",
                "difficulty": "Advanced",
                "statement": r"""The classical mechanism of osazone formation puzzled early chemists because phenylhydrazine ($\text{PhNHNH}_2$) acts simultaneously as a derivatizing agent and as an oxidizing agent.
(a) Provide the complete curved-arrow mechanism for the oxidation of the C2 hydroxyl to a ketone by the first phenylhydrazine moiety, identifying the amine products released.
(b) Explain why osazone formation cleanly stops after the introduction of two phenylhydrazone groups at C1 and C2, and does not continue down the chain to C3, C4, C5, or C6.""",
                "hints": [
                    r"Oxidation involves tautomerization of the hydrazone to an ene-hydrazine.",
                    r"Cleavage of the weak N-N single bond of phenylhydrazine releases aniline (PhNH2).",
                    r"The bis-hydrazone product forms a chelated six-membered hydrogen-bonded ring that protects C3."
                ],
                "solution": r"""### Step 1: Oxidation Mechanism via Ene-Hydrazine Intermediate
1. **Hydrazone Tautomerization**:
   The mono-phenylhydrazone of an aldose ($\text{R-CH(OH)-CH}=\text{N-NHPh}$) undergoes prototropic tautomerization to form an **ene-hydrazine**:
   $$\text{R-C(OH)}=\text{CH}-\text{NH}-\text{NHPh}$$
2. **Intramolecular Redox Cleavage**:
   The electron pair on the hydrazine nitrogen pushes into the system, cleaving the weak $\text{N-N}$ single bond (bond dissociation energy $\approx 160\text{ kJ/mol}$):
   $$\text{R-C}(=\text{O})-\text{CH}=\text{NH} + \text{PhNH}_2 \quad (\mathbf{Aniline\ released})$$
   Concurrently, the C2 enol oxygen is oxidized to a ketone ($\text{C}=\text{O}$).
3. **Condensation with Second and Third Phenylhydrazine**:
   - The C1 imine ($\text{CH}=\text{NH}$) is transiminated by a second molecule of $\text{PhNHNH}_2$, releasing **ammonia ($\text{NH}_3$)** and forming the C1 hydrazone.
   - The C2 ketone condenses with a third molecule of $\text{PhNHNH}_2$, releasing **water ($\text{H}_2\text{O}$)** and forming the **osazone**.

### Step 2: Termination at C2 (Why C3 is Not Oxidized)
The reaction ceases strictly at C2 due to **intramolecular chelation and resonance stabilization**:
- In the formed diphenylosazone, the hydrogen on the C2 hydrazone nitrogen ($\text{N2-H}$) forms an exceptionally strong intramolecular hydrogen bond with the C1 imine nitrogen ($\text{N1}$):
  $$\text{N2}-\text{H}\cdots\text{N1}=\text{C1}$$
- This locks the molecule into a quasi-aromatic six-membered chelate ring.
- In this rigid, resonance-stabilized cyclic conformation:
  - The C2 hydrazone nitrogen is proton-locked and cannot undergo tautomerization to an ene-hydrazine.
  - The C3 hydroxyl is held far from the reactive centers and cannot participate in intramolecular redox cleavage.
  - Consequently, further oxidation of C3 is completely prevented."""
            },
            {
                "id": "prob-4-7",
                "problemNumber": "4.7",
                "title": "Conformational Free Energy Calculation for Hexopyranose Chair Inversion",
                "difficulty": "Intermediate",
                "statement": r"""Using empirical conformational A-values and 1,3-diaxial interaction energies:
- $-\text{OH}$ axial penalty: $4.0\text{ kJ/mol}$
- $-\text{CH}_2\text{OH}$ axial penalty: $6.7\text{ kJ/mol}$
- 1,3-diaxial $[\text{OH} \leftrightarrow \text{OH}]$ repulsion: $8.4\text{ kJ/mol}$
- 1,3-diaxial $[\text{OH} \leftrightarrow \text{CH}_2\text{OH}]$ repulsion: $10.5\text{ kJ/mol}$
- Anomeric effect stabilization for axial $-\text{OH}$ in water: $2.6\text{ kJ/mol}$
(a) Calculate the steric free energy penalty $\Delta G^\circ$ for inverting $\beta$-D-glucopyranose from its native $^4C_1$ chair to the inverted $^1C_4$ chair conformation.
(b) Compute the equilibrium ratio of $[^4C_1] / [^1C_4]$ at $298\text{ K}$.""",
                "hints": [
                    r"In the 4C1 chair of \beta-D-glucopyranose, all 5 substituents are equatorial (steric penalty = 0).",
                    r"In the 1C4 chair, all 5 substituents become axial.",
                    r"Count all individual A-values and add syn-diaxial interactions between 1,3-axial groups."
                ],
                "solution": r"""### Step 1: Conformation Analysis of $\beta$-D-Glucopyranose
1. **Native $^4C_1$ Conformation**:
   - C1-OH: Equatorial
   - C2-OH: Equatorial
   - C3-OH: Equatorial
   - C4-OH: Equatorial
   - C5-$\text{CH}_2\text{OH}$: Equatorial
   - Total steric strain = **$0.0\text{ kJ/mol}$**.
2. **Inverted $^1C_4$ Conformation**:
   Upon chair flip, all equatorial groups become **axial**:
   - Four axial $-\text{OH}$ groups (C1, C2, C3, C4): $4 \times 4.0 = 16.0\text{ kJ/mol}$
   - One axial $-\text{CH}_2\text{OH}$ group (C5): $6.7\text{ kJ/mol}$
   - Syn-diaxial interactions:
     - 1,3-diaxial between axial C1-OH and axial C3-OH: $8.4\text{ kJ/mol}$
     - 1,3-diaxial between axial C3-OH and axial C5-$\text{CH}_2\text{OH}$: $10.5\text{ kJ/mol}$
     - 1,3-diaxial between axial C2-OH and axial C4-OH: $8.4\text{ kJ/mol}$
   - Stereoelectronic anomeric stabilization (since C1-OH is now axial): **$-2.6\text{ kJ/mol}$**.
3. **Total Free Energy Difference**:
   $$\Delta G^\circ = (16.0 + 6.7 + 8.4 + 10.5 + 8.4) - 2.6 = 50.0 - 2.6 = \mathbf{+47.4\text{ kJ/mol}}$$

### Step 2: Equilibrium Ratio $[^4C_1] / [^1C_4]$
Using the Boltzmann relation:
$$\frac{[^4C_1]}{[^1C_4]} = e^{\Delta G^\circ / (R T)} = \exp\left(\frac{47,400}{(8.314)(298.15)}\right) = \exp(19.12) \approx \mathbf{2.0\times 10^8}$$
More than 200 million molecules exist in the $^4C_1$ conformation for every single molecule in the $^1C_4$ state, proving that $\beta$-D-glucopyranose exists exclusively in the all-equatorial $^4C_1$ chair."""
            }
        ]
    }
    units.append(u4)

    # =========================================================================
    # UNIT 5: Carbohydrates II: Disaccharides, Polysaccharides & Glycobiology
    # =========================================================================
    u5 = {
        "id": "unit-5",
        "unitNumber": 5,
        "title": "Unit 5: Carbohydrates II: Disaccharides, Polysaccharides & Glycobiology",
        "leadSummary": "Advanced chemistry of complex carbohydrates: glycosidic linkage determination, non-reducing vs reducing architectures, the structural elucidation of sucrose, kinetics of cane sugar polarimetric inversion, maltose and cellobiose enzymatic selectivity, and the structural glycobiology of starch (amylose $\\alpha$-helices and amylopectin branch points) and crystalline cellulose (intermolecular hydrogen-bonded microfibrils).",
        "simulations": ["sim_nat_sucrose_inversion_polarimetry"],
        "sections": [
            {
                "id": "sec-5-1",
                "secNumber": "5.1",
                "title": "Disaccharides: Structural Classification & Glycosidic Linkage Stereochemistry",
                "content": r"""Disaccharides ($C_{12}H_{22}O_{11}$) are carbohydrates formed by the condensation of two monosaccharide units with elimination of a water molecule, linked via an acetal **glycosidic bond**.

### Classification: Reducing vs Non-Reducing
1. **Reducing Disaccharides**: The glycosidic bond connects the anomeric carbon of one sugar to a non-anomeric hydroxyl group of the second sugar (e.g., C4 or C6):
   - Examples: **Maltose** ($\alpha\text{-D-Glc}-(1\to 4)\text{-D-Glc}$), **Cellobiose** ($\beta\text{-D-Glc}-(1\to 4)\text{-D-Glc}$), **Lactose** ($\beta\text{-D-Gal}-(1\to 4)\text{-D-Glc}$).
   - The second sugar retains a free hemiacetal group at its anomeric carbon, enabling it to open into a free aldehyde in solution.
   - Consequently, reducing disaccharides undergo mutarotation, reduce Fehling's solution and Tollens' reagent, and form mono-osazones.
2. **Non-Reducing Disaccharides**: The glycosidic linkage joins **both anomeric carbons** directly together:
   - Examples: **Sucrose** ($\alpha\text{-D-Glcp}-(1\leftrightarrow 2)\text{-}\beta\text{-D-Fruf}$) and **Trehalose** ($\alpha\text{-D-Glcp}-(1\leftrightarrow 1)\text{-}\alpha\text{-D-Glcp}$).
   - Because both anomeric carbons are locked into acetal/ketal linkages, neither ring can open into a free carbonyl.
   - They do **not** undergo mutarotation, do not reduce Fehling's or Tollens' reagents, and do not form osazones."""
            },
            {
                "id": "sec-5-2",
                "secNumber": "5.2",
                "title": "Structural Elucidation and Stereochemistry of Sucrose",
                "content": r"""Sucrose ($C_{12}H_{22}O_{11}$, table sugar) is the primary transport sugar in photosynthetic plants.

### Rigorous Deductive Proof of Structure
1. **Molecular Formula and Hydrolysis**:
   $C_{12}H_{22}O_{11}$. Acid-catalyzed hydrolysis or enzymatic cleavage with yeast invertase yields an equimolar mixture of D-(+)-glucose and D-(-)-fructose:
   $$\text{C}_{12}\text{H}_{22}\text{O}_{11} + \text{H}_2\text{O} \to \text{C}_6\text{H}_{12}\text{O}_6 \text{ (D-Glucose)} + \text{C}_6\text{H}_{12}\text{O}_6 \text{ (D-Fructose)}$$
2. **Non-Reducing Character**:
   Sucrose fails to reduce Fehling's solution, does not react with Tollens' reagent, does not form an osazone, and displays **no mutarotation**. Therefore, the glycosidic bond must bridge the **C1 anomeric carbon of D-glucose** directly to the **C2 anomeric carbon of D-fructose**.
3. **Ring Sizes via Permethylation Analysis (Haworth)**:
   Exhaustive methylation of sucrose using dimethyl sulfate and sodium hydroxide ($\text{Me}_2\text{SO}_4 / \text{NaOH}$) yields **octa-O-methylsucrose**:
   $$\text{Sucrose} \xrightarrow{\text{Me}_2\text{SO}_4, \text{ NaOH}} \text{Octa-O-methylsucrose}$$
   Mild acid hydrolysis of octa-O-methylsucrose cleaves only the glycosidic bond, yielding two tetra-O-methyl monosaccharides:
   - **2,3,4,6-Tetra-O-methyl-D-glucopyranose**: The unmethylated hydroxyl at C5 proves that glucose was present in the **six-membered pyranose ring**.
   - **1,3,4,6-Tetra-O-methyl-D-fructofuranose**: The unmethylated hydroxyl at C5 proves that fructose was present in the **five-membered furanose ring**.
4. **Configuration of the Glycosidic Linkages**:
   - Hydrolysis by yeast $\alpha$-glucosidase (maltase), which selectively cleaves $\alpha$-D-glucopyranosides, cleaves sucrose.
   - Hydrolysis by yeast invertase ($\beta$-D-fructofuranosidase), which selectively cleaves $\beta$-D-fructofuranosides, also cleaves sucrose.
   Thus, sucrose is definitively **$\alpha$-D-glucopyranosyl-(1$\leftrightarrow$2)-$\beta$-D-fructofuranoside**."""
            },
            {
                "id": "sec-5-3",
                "secNumber": "5.3",
                "title": "Kinetics of Cane Sugar Inversion: Acid Catalysis, Biot Law & Polarimetry",
                "content": r"""The acid-catalyzed hydrolysis of sucrose is historically celebrated as **cane sugar inversion**, the first chemical reaction whose kinetics were monitored quantitatively by polarimetry (Wilhelmy, 1850).

### Origin of the Name 'Inversion'
- Sucrose is dextrorotatory, with a specific optical rotation of $[\alpha]_D^{20} = \mathbf{+66.5^\circ}$.
- Upon complete hydrolysis, the equimolar mixture of products (invert sugar) contains:
  - D-(+)-glucose: $[\alpha]_D^{20} = +52.7^\circ$
  - D-(-)-fructose: $[\alpha]_D^{20} = -92.4^\circ$
- The net specific rotation of the equimolar mixture is:
  $$[\alpha]_D^{\text{invert}} = \frac{+52.7^\circ + (-92.4^\circ)}{2} = \mathbf{-19.85^\circ}$$
Because the optical rotation changes sign ('inverts') from dextrorotatory ($+66.5^\circ$) to levorotatory ($-19.85^\circ$), the process is termed **inversion**.

### Polarimetric Rate Law
The reaction is pseudo-first-order in sucrose concentration when water and acid are in large excess:
$$-\frac{d[\text{Sucrose}]}{dt} = k_{\text{obs}} [\text{Sucrose}]$$
According to Biot's Law, the observed optical rotation $\alpha(t)$ at time $t$ in a cell of path length $l$ is:
$$\alpha(t) = l \left( [\alpha]_{\text{suc}} [\text{Suc}]_t + [\alpha]_{\text{glc}} [\text{Glc}]_t + [\alpha]_{\text{fru}} [\text{Fru}]_t \right)$$
At $t = 0$: $\alpha_0 \propto [\text{Suc}]_0$. At $t \to \infty$: $\alpha_\infty \propto [\text{Suc}]_0 [\alpha]_{\text{invert}}$.
At any time $t$:
$$[\text{Suc}]_t = [\text{Suc}]_0 \left(\frac{\alpha_t - \alpha_\infty}{\alpha_0 - \alpha_\infty}\right)$$
Integrating yields the linear kinetic equation:
$$\ln\left(\frac{\alpha_0 - \alpha_\infty}{\alpha_t - \alpha_\infty}\right) = k_{\text{obs}} t$$"""
            },
            {
                "id": "sec-5-4",
                "secNumber": "5.4",
                "title": "Structural Elucidation of Maltose & Cellobiose: Enzymatic Discrimination",
                "content": r"""Maltose and cellobiose are constitutional isomers ($C_{12}H_{22}O_{11}$) consisting of two D-glucose units connected by a $(1\to 4)$-glycosidic bond, differing exclusively in the anomeric configuration ($\alpha$ vs $\beta$) of that linkage.

### Maltose (from Starch Hydrolysis)
- Formed by the action of $\beta$-amylase on starch.
- **Reducing Property**: Mutarotates ($+112^\circ \to +130.4^\circ$), reduces Fehling's solution, and forms a phenylosazone ($C_{12}H_{20}O_9(=\text{NNHPh})_2$).
- **Permethylation and Hydrolysis**: Exhaustive methylation gives methyl hepta-O-methylmaltoside. Acid hydrolysis yields:
  - 2,3,4,6-Tetra-O-methyl-D-glucose (from the non-reducing terminal ring).
  - 2,3,6-Tri-O-methyl-D-glucose (the free hydroxyl at C4 proves the $(1\to 4)$ linkage; free OH at C1 is the reducing center).
- **Enzymatic Proof**: Maltose is rapidly cleaved by **maltase ($\alpha$-glucosidase)**, but completely resistant to **emulsin ($\beta$-glucosidase)**. Therefore, the linkage is **$\alpha$-(1$\to$4)**:
  $$\mathbf{4-O-(\alpha\text{-D-glucopyranosyl})-D-glucopyranose}$$

### Cellobiose (from Cellulose Hydrolysis)
- Obtained by the partial acetolysis of cellulose using acetic anhydride and sulfuric acid ($\text{Ac}_2\text{O} / \text{H}_2\text{SO}_4$).
- Shows identical chemical degradation products to maltose: forms identical methylation cleavage fragments (2,3,4,6-tetra-O-methyl-D-glucose and 2,3,6-tri-O-methyl-D-glucose).
- **Enzymatic Proof**: Cellobiose is cleaved by **emulsin ($\beta$-glucosidase)**, but completely resistant to **maltase**.
- Therefore, the linkage is **$\beta$-(1$\to$4)**:
  $$\mathbf{4-O-(\beta\text{-D-glucopyranosyl})-D-glucopyranose}$$"""
            },
            {
                "id": "sec-5-5",
                "secNumber": "5.5",
                "title": "Lactose: Chemistry, $\\beta$-Galactosidase Cleavage & Lactose Intolerance",
                "content": r"""Lactose ($C_{12}H_{22}O_{11}$, milk sugar) is the primary carbohydrate found in mammalian milk ($4.5–7.0\%\text{ w/v}$).

### Chemical Architecture and Hydrolysis
1. **Constituent Monomers**:
   Acid-catalyzed hydrolysis or enzymatic digestion with lactase ($\beta$-galactosidase) yields equimolar D-galactose and D-glucose:
   $$\text{Lactose} + \text{H}_2\text{O} \xrightarrow{\text{Lactase}} \text{D-Galactose} + \text{D-Glucose}$$
2. **Reducing Property**:
   Lactose reduces Fehling's solution, undergoes mutarotation ($+85^\circ \to +52.6^\circ$), and forms a crystalline lactosazone. Oxidation with bromine water followed by hydrolysis yields D-galactose and D-gluconic acid, proving that **glucose contains the free reducing hemiacetal**, while galactose contributes the glycosidic anomeric carbon.
3. **Glycosidic Linkage**:
   Permethylation followed by hydrolysis yields 2,3,4,6-tetra-O-methyl-D-galactose and 2,3,6-tri-O-methyl-D-glucose. The linkage is cleaved by $\beta$-galactosidase, confirming a **$\beta$-(1$\to$4) linkage**:
   $$\mathbf{4-O-(\beta\text{-D-galactopyranosyl})-D-glucopyranose}$$

### Biochemical Enzymology and Lactose Intolerance
In mammalian infants, intestinal brush-border lactase-phlorizin hydrolase (LPH) hydrolyzes lactose into absorbable monosaccharides. In adult populations with lactase non-persistence (hypolactasia), unabsorbed lactose passes into the colon, causing osmotic water influx and bacterial fermentation into short-chain fatty acids, $\text{H}_2$, $\text{CO}_2$, and $\text{CH}_4$, inducing gastrointestinal distress."""
            },
            {
                "id": "sec-5-6",
                "secNumber": "5.6",
                "title": "Polysaccharides I: Starch — Amylose Helices, Amylopectin Branches & Iodine Clathrates",
                "content": r"""Starch is the principal energy storage polysaccharide of plants, stored as semicrystalline granules inside chloroplasts and amyloplasts. It consists of two macromolecular glucan fractions: amylose ($20–30\%$) and amylopectin ($70–80\%$).

### Amylose (Linear $\alpha$-(1$\to$4) Glucan)
- Linear chain of D-glucopyranose units linked exclusively by $\alpha$-(1$\to$4)-glycosidic bonds ($DP \sim 300 - 3000$).
- Because of the axial-like geometry of the $\alpha$-(1$\to$4) linkage, the chain does not adopt an extended ribbon conformation; instead, it coils into a left-handed **single helix** with six glucose residues per helical turn (pitch $= 0.80\text{ nm}$, diameter $= 1.30\text{ nm}$).
- **Iodine Inclusion Complex**: The interior cavity of the amylose helix is hydrophobic, accommodating polyiodide anions ($I_3^-, I_5^-$) to form a linear blue clathrate complex with an intense absorption band at $\lambda_{\text{max}} \approx 620 - 650\text{ nm}$.

### Amylopectin (Branched Glucan)
- Highly branched macromolecule ($DP \sim 10^5 - 10^6$, molecular mass $10^7 - 10^8\text{ Da}$).
- Consists of linear $\alpha$-(1$\to$4) chains interrupted every 24 to 30 glucose residues by **$\alpha$-(1$\to$6)-glycosidic branch points**.
- Forms a cluster architecture: tightly packed double helices formed by adjacent branch chains pack into crystalline lamellae, alternating with amorphous branch-point regions."""
            },
            {
                "id": "sec-5-7",
                "secNumber": "5.7",
                "title": "Polysaccharides II: Cellulose — $\\beta$-(1$\to$4) Glucans, Hydrogen Networks & Microfibrils",
                "content": r"""Cellulose is the most abundant biopolymer on Earth, representing over $50\%$ of all organic carbon in the biosphere. It constitutes the primary structural scaffolding of plant cell walls.

### Macromolecular Architecture
- Unbranched homopolymer of D-glucopyranose linked exclusively by **$\beta$-(1$\to$4)-glycosidic bonds** ($DP \sim 2,000 - 15,000$).
- In contrast to the coiled helices of $\alpha$-linked amylose, the $\beta$-(1$\to$4) linkage causes alternating glucose residues to rotate by $180^\circ$ relative to their neighbors. The repeat unit is therefore the disaccharide **cellobiose**.
- This alternating flip produces an extraordinarily rigid, fully extended linear ribbon conformation.

### Hydrogen-Bonding Network and Crystalline Microfibrils
1. **Intramolecular Hydrogen Bonds**:
   - $\text{O}3-\text{H} \cdots \text{O}5^\prime$ (between adjacent pyranose rings along the chain), stiffening the glucan ribbon.
   - $\text{O}2-\text{H} \cdots \text{O}6^\prime$ across the glycosidic bridge.
2. **Intermolecular Hydrogen Bonds**:
   - Hydrogen bonds between the C6 hydroxyls and ring oxygens of adjacent parallel chains ($\text{O}6-\text{H} \cdots \text{O}3^{\prime\prime}$) assemble 36 individual glucan chains into crystalline **microfibrils** (Cellulose $I_\beta$).
   - This dense hydrogen-bonded crystal lattice completely excludes water, rendering native cellulose insolubly resistant to water, dilute acids, and common organic solvents, with a tensile strength exceeding that of structural steel."""
            }
        ],
        "problems": [
            {
                "id": "prob-5-1",
                "problemNumber": "5.1",
                "title": "Permethylation and Acidic Hydrolysis Proof of Sucrose Structure",
                "statement": r"""A pure sample of sucrose ($3.423\text{ g}$, $10.0\text{ mmol}$) was treated with excess dimethyl sulfate and sodium hydroxide in DMF, affording octa-O-methylsucrose in $92\%$ yield. Subsequent mild acid hydrolysis cleaved the glycosidic bond, and the products were separated by preparative gas chromatography.
(a) Write the names, molecular formulas, and structures of the two methylated monosaccharide products.
(b) Explain why oxidation of product A with nitric acid yields a dimethyl dicarboxylic acid, whereas product B is unreactive toward bromine water oxidation.
(c) Deduce from this data why the rings of glucose and fructose in sucrose must be pyranose and furanose, respectively.""",
                "hints": [
                    r"Octa-O-methylsucrose has 8 methyl ether groups (-OMe).",
                    r"Hydrolysis cleaves only the acetal/ketal bond, freeing the OH groups that were involved in the glycosidic bond and ring closures.",
                    r"Product A is 2,3,4,6-tetra-O-methyl-D-glucose; Product B is 1,3,4,6-tetra-O-methyl-D-fructose."
                ],
                "solution": r"""### Step 1: Cleavage Products of Octa-O-Methylsucrose
Exhaustive methylation methylates all free hydroxyl groups:
- Sucrose has 8 free $-\text{OH}$ groups $\to$ 8 $-\text{OCH}_3$ groups.
Mild acid hydrolysis cleaves only the glycosidic bond, leaving all methyl ether linkages intact:
1. **Product A**: **2,3,4,6-Tetra-O-methyl-D-glucopyranose** ($C_{10}H_{20}O_6$):
   - Hydroxyls at C2, C3, C4, C6 are methylated.
   - The hydroxyl at **C1** is free (it formed the glycosidic link).
   - The hydroxyl at **C5** is free because it was involved in the six-membered hemiacetal pyranose ring.
2. **Product B**: **1,3,4,6-Tetra-O-methyl-D-fructofuranose** ($C_{10}H_{20}O_6$):
   - Hydroxyls at C1, C3, C4, C6 are methylated.
   - The hydroxyl at **C2** is free (it formed the glycosidic link).
   - The hydroxyl at **C5** is free because it was involved in the five-membered hemiketal furanose ring.

### Step 2: Oxidation Diagnostics
- **Product A (Glucose derivative)**:
  Product A possesses a free hemiacetal at C1. In aqueous solution, it opens to a free aldehyde ($\text{CHO}$). Oxidation with nitric acid oxidizes C1 (to $-\text{COOH}$) and cleaves the C5-OH to generate a dicarboxylic acid derivative.
- **Product B (Fructose derivative)**:
  Product B possesses a ketal/hemiketal at C2. It cannot open to an aldehyde; ketoses are not oxidized by mild bromine water ($\text{Br}_2 / \text{H}_2\text{O}$), which selectively oxidizes aldoses.

### Step 3: Deduction of Ring Sizes
- In Product A, methylation occurred at C2, C3, C4, and C6. The only hydroxyl not methylated (besides the C1 hemiacetal) was **C5-OH**. This proves that C5-OH was engaged in the ring bridge during methylation: **6-membered pyranose ring**.
- In Product B, methylation occurred at C1, C3, C4, and C6. The only unmethylated hydroxyl (besides C2) was **C5-OH**. This proves that C5-OH was engaged in the ring bridge with C2 during methylation: **5-membered furanose ring**."""
            },
            {
                "id": "prob-5-2",
                "problemNumber": "5.2",
                "title": "Polarimetric Kinetics of Sucrose Inversion and Rate Constant Calculation",
                "difficulty": "Intermediate",
                "statement": r"""The acid-catalyzed inversion of sucrose was monitored polarimetrically in a $2.00\text{ dm}$ polarimeter tube at $25.0^\circ\text{C}$ with $0.50\text{ M HCl}$. The observed optical rotation values at various times were:
- $t = 0\text{ min}$: $\alpha_0 = +24.10^\circ$
- $t = 15.0\text{ min}$: $\alpha_{15} = +17.20^\circ$
- $t = 45.0\text{ min}$: $\alpha_{45} = +6.80^\circ$
- $t \to \infty$: $\alpha_\infty = -7.40^\circ$
(a) Verify that the reaction obeys pseudo-first-order kinetics by calculating the rate constant $k_{\text{obs}}$ at $t = 15.0\text{ min}$ and $t = 45.0\text{ min}$.
(b) Calculate the reaction half-life ($t_{1/2}$) and the time required for the optical rotation to reach exactly $0.00^\circ$ (the inversion point).""",
                "hints": [
                    r"Use the Wilhelmy equation: k = (1/t) * ln((alpha_0 - alpha_inf) / (alpha_t - alpha_inf)).",
                    r"alpha_0 - alpha_inf = 24.10 - (-7.40) = 31.50 degrees.",
                    r"For alpha_t = 0.00, substitute alpha_t into the integrated rate equation."
                ],
                "solution": r"""### Step 1: Verification of Pseudo-First-Order Rate Constant
The integrated first-order polarimetric rate equation is:
$$k = \frac{1}{t} \ln\left(\frac{\alpha_0 - \alpha_\infty}{\alpha_t - \alpha_\infty}\right)$$
Given $\alpha_0 - \alpha_\infty = 24.10 - (-7.40) = 31.50^\circ$:

1. At $t = 15.0\text{ min}$:
   $$\alpha_{15} - \alpha_\infty = 17.20 - (-7.40) = 24.60^\circ$$
   $$k_{15} = \frac{1}{15.0} \ln\left(\frac{31.50}{24.60}\right) = \frac{1}{15.0} \ln(1.2805) = \frac{0.2472}{15.0} = \mathbf{0.01648\text{ min}^{-1}}$$

2. At $t = 45.0\text{ min}$:
   $$\alpha_{45} - \alpha_\infty = 6.80 - (-7.40) = 14.20^\circ$$
   $$k_{45} = \frac{1}{45.0} \ln\left(\frac{31.50}{14.20}\right) = \frac{1}{45.0} \ln(2.2183) = \frac{0.7967}{45.0} = \mathbf{0.01659\text{ min}^{-1}}$$

The rate constants are concordant within $0.6\%$, confirming **pseudo-first-order kinetics** with average rate constant:
$$k_{\text{obs}} = \frac{0.01648 + 0.01659}{2} = \mathbf{0.01654\text{ min}^{-1}} \quad (2.76\times 10^{-4}\text{ s}^{-1})$$

### Step 2: Half-Life and Zero-Rotation Inversion Time
1. **Reaction Half-Life**:
   $$t_{1/2} = \frac{\ln 2}{k_{\text{obs}}} = \frac{0.6931}{0.01654\text{ min}^{-1}} = \mathbf{41.9\text{ min}}$$

2. **Time to Reach $\alpha_t = 0.00^\circ$**:
   $$\alpha_t - \alpha_\infty = 0.00 - (-7.40) = 7.40^\circ$$
   $$t_{\text{inv}} = \frac{1}{k_{\text{obs}}} \ln\left(\frac{31.50}{7.40}\right) = \frac{1}{0.01654} \ln(4.2568) = \frac{1.4485}{0.01654} = \mathbf{87.6\text{ min}}$$
At $t = 87.6\text{ minutes}$, the optical rotation of the hydrolyzing sugar solution drops to zero."""
            },
            {
                "id": "prob-5-3",
                "problemNumber": "5.3",
                "title": "Maltose vs Cellobiose $\\alpha/\\beta$-Linkage Discrimination via Enzyme Selectivity",
                "difficulty": "Intermediate",
                "statement": r"""A researcher is provided with two unlabeled white crystalline disaccharides, Compound X and Compound Y. Both analyze as $C_{12}H_{22}O_{11}$, are reducing sugars, and yield only D-glucose upon acid hydrolysis.
(a) When incubated with maltase (yeast $\alpha$-glucosidase), Compound X is completely hydrolyzed within 10 minutes, while Compound Y is unaffected. When incubated with emulsin (almond $\beta$-glucosidase), Compound Y is hydrolyzed while Compound X is unaffected. Identify X and Y.
(b) Explain why human digestive enzymes can readily metabolize maltose (and starch) but cannot digest cellobiose (and cellulose), and identify the evolutionary significance of rumen symbionts.""",
                "hints": [
                    r"Maltase selectively cleaves alpha-glycosidic bonds.",
                    r"Emulsin selectively cleaves beta-glycosidic bonds.",
                    r"Humans express alpha-amylase and maltase but lack cellulases."
                ],
                "solution": r"""### Step 1: Identification of Compounds X and Y
- **Compound X**:
  - Yields D-glucose upon hydrolysis.
  - Reducing sugar.
  - Specifically hydrolyzed by **maltase ($\alpha$-glucosidase)**, which requires an **$\alpha$-D-glucopyranosyl linkage**.
  - Unaffected by emulsin.
  - Therefore, Compound X is **Maltose (4-O-$\alpha$-D-glucopyranosyl-D-glucopyranose)**.
- **Compound Y**:
  - Yields D-glucose upon hydrolysis.
  - Reducing sugar.
  - Specifically hydrolyzed by **emulsin ($\beta$-glucosidase)**, which requires a **$\beta$-D-glucopyranosyl linkage**.
  - Unaffected by maltase.
  - Therefore, Compound Y is **Cellobiose (4-O-$\beta$-D-glucopyranosyl-D-glucopyranose)**.

### Step 2: Human Digestion vs Ruminant Symbiosis
1. **Stereospecificity of Human Enzymes**:
   Human digestive enzymes ($\alpha$-amylase, maltase-glucoamylase) possess catalytic clefts with precisely oriented carboxylate residues (Asp/Glu) configured to bind and cleave the curved, bent geometry of **$\alpha$-(1$\to$4) linkages**. They cannot accommodate or activate the planar, extended ribbon conformation of **$\beta$-(1$\to$4) linkages**.
2. **Ruminant Symbiosis**:
   Ruminants (cows, sheep) also lack endogenous cellulase genes. However, their specialized multi-chambered stomach (the rumen) harbors anaerobic microbial consortia (*Fibrobacter succinogenes*, *Ruminococcus albus*) that express complex cellulosome complexes and **$\beta$-1,4-endoglucanases**, hydrolyzing cellulose into cellobiose and glucose, which are fermented into volatile fatty acids (acetate, propionate, butyrate) that nourish the host."""
            },
            {
                "id": "prob-5-4",
                "problemNumber": "5.4",
                "title": "Amylopectin Branch Point Quantification via Exhaustive Methylation",
                "difficulty": "Advanced",
                "statement": r"""A sample of purified corn amylopectin ($1.621\text{ g}$, corresponding to $10.0\text{ mmol}$ of anhydroglucose units) was subjected to exhaustive Hakomori methylation using methyl iodide and dimsyl sodium in DMSO. Complete acid hydrolysis of the permethylated polysaccharide yielded:
- 2,3,4,6-Tetra-O-methyl-D-glucose: $0.42\text{ mmol}$
- 2,3,6-Tri-O-methyl-D-glucose: $9.16\text{ mmol}$
- 2,3-Di-O-methyl-D-glucose: $0.42\text{ mmol}$
(a) Identify the structural role of the glucose residues giving rise to each of the three methylated derivatives.
(b) Calculate the average branch chain length (number of glucose residues per branch point) and the percentage of $\alpha$-(1$\to$6) branch linkages in this amylopectin sample.""",
                "hints": [
                    r"Tetra-O-methyl-glucose comes from non-reducing chain ends.",
                    r"Di-O-methyl-glucose comes from branch point residues (carbons 1, 4, and 6 are linked).",
                    r"Tri-O-methyl-glucose comes from linear internal residues (carbons 1 and 4 are linked).",
                    r"Average chain length = Total glucose units / number of branch points."
                ],
                "solution": r"""### Step 1: Structural Origin of Cleavage Fragments
1. **2,3,4,6-Tetra-O-methyl-D-glucose ($0.42\text{ mmol}$)**:
   - All four non-anomeric hydroxyls (C2, C3, C4, C6) are methylated.
   - Originated exclusively from the **non-reducing terminal residues** of the outer branches.
2. **2,3,6-Tri-O-methyl-D-glucose ($9.16\text{ mmol}$)**:
   - C1 and C4 were unmethylated because they participated in the continuous linear **$\alpha$-(1$\to$4)-glycosidic backbone**.
   - Originated from **internal linear glucan residues**.
3. **2,3-Di-O-methyl-D-glucose ($0.42\text{ mmol}$)**:
   - Hydroxyls at C1, C4, and C6 were unmethylated.
   - C1 and C4 carried the linear chain, while C6 carried the branch chain.
   - Originated from the **$\alpha$-(1$\to$6) branch-point residues**.

### Step 2: Calculation of Branching Parameters
1. **Verification of Stoichiometric Balance**:
   Every branch produces exactly one non-reducing end. Therefore, moles of tetra-O-methyl-D-glucose must equal moles of di-O-methyl-D-glucose:
   $$n_{\text{terminal}} = n_{\text{branch}} = 0.42\text{ mmol}$$
   Total glucose residues accounted for:
   $$n_{\text{total}} = 0.42 + 9.16 + 0.42 = 10.00\text{ mmol}$$

2. **Average Chain Length ($\overline{CL}$)**:
   The average number of glucose residues per branch point is:
   $$\overline{CL} = \frac{n_{\text{total}}}{n_{\text{branch}}} = \frac{10.00\text{ mmol}}{0.42\text{ mmol}} = \mathbf{23.8\text{ glucose units}}$$
   There is one branch point for every $\sim 24$ glucose residues.

3. **Percentage of Branch Linkages**:
   $$\% \text{ branching} = \frac{n_{\text{branch}}}{n_{\text{total}}} \times 100\% = \frac{0.42}{10.00} \times 100\% = \mathbf{4.20\%}$$
   Approximately $4.2\%$ of the total glycosidic bonds are $\alpha$-(1$\to$6) branch points."""
            },
            {
                "id": "prob-5-5",
                "problemNumber": "5.5",
                "title": "Intramolecular Hydrogen Bond Cooperativity and Tensile Strength in Cellulose I$\\beta$",
                "difficulty": "Advanced",
                "statement": r"""Crystalline cellulose $I_\beta$ has an experimental crystal density of $\rho = 1.60\text{ g/cm}^3$ and an ultimate tensile strength $\sigma_{\text{ult}} = 1.0\times 10^9\text{ Pa}$ ($1.0\text{ GPa}$).
(a) In a single glucan chain, the intramolecular $\text{O}3-\text{H}\cdots\text{O}5^\prime$ hydrogen bond has an energy of $E_{\text{HB}} \approx 21.0\text{ kJ/mol}$ and a length of $0.275\text{ nm}$. Calculate the linear hydrogen-bond energy density ($\text{J/m}$) along the fiber axis (fiber repeat length $c = 1.038\text{ nm}$ for two glucose residues).
(b) Explain why treating cellulose with aqueous sodium hydroxide ($18\%\text{ NaOH}$, the mercerization process) converts native Cellulose I into Cellulose II, detailing the thermodynamic transition from parallel to antiparallel chain packing.""",
                "hints": [
                    r"Repeat length c = 1.038 nm contains 2 glucose residues, each with an O3-H...O5' hydrogen bond.",
                    r"Mercerization disrupts the native crystal lattice.",
                    r"Cellulose II has antiparallel chains with an inter-sheet hydrogen-bonding network."
                ],
                "solution": r"""### Step 1: Hydrogen Bond Energy Density
In the cellulose repeat unit ($c = 1.038\text{ nm} = 1.038\times 10^{-9}\text{ m}$), there are two cellobiose-linked glucose residues.
- Each glucose residue forms one $\text{O}3-\text{H}\cdots\text{O}5^\prime$ intramolecular hydrogen bond:
  $$N_{\text{HB}} = 2\text{ hydrogen bonds per repeat unit}$$
- Total hydrogen bond energy per repeat unit:
  $$E_{\text{repeat}} = \frac{2 \times 21.0\times 10^3\text{ J/mol}}{6.022\times 10^{23}\text{ mol}^{-1}} = 6.97\times 10^{-20}\text{ J}$$
- Linear energy density along the chain:
  $$u_{\text{HB}} = \frac{E_{\text{repeat}}}{c} = \frac{6.97\times 10^{-20}\text{ J}}{1.038\times 10^{-9}\text{ m}} = \mathbf{6.71\times 10^{-11}\text{ J/m}}$$
This massive cooperative hydrogen bonding stiffens the polymer ribbon, preventing chain bending and yielding a modulus of elasticity ($E \approx 130\text{ GPa}$) rivaling aramid fibers (Kevlar).

### Step 2: Mercerization and Cellulose I $\to$ Cellulose II Transformation
1. **Cellulose I (Native Form)**:
   Synthesized by terminal rosette enzyme complexes in the plant cell membrane, where all glucan chains grow in the **same direction** ($\mathbf{parallel\ packing}$). This is a kinetically trapped metastable crystal form.
2. **Mercerization ($18\%\text{ NaOH}$)**:
   Swelling in concentrated alkali deprotonates the hydroxyl groups ($-\text{O}^-\text{Na}^+$), disrupting all intra- and intermolecular hydrogen bonds.
3. **Regeneration to Cellulose II**:
   Upon washing out the alkali, the solvated chains re-crystallize into the thermodynamically most stable polymorph: **Cellulose II**.
   In Cellulose II, chains pack in an **antiparallel orientation** ($\uparrow\downarrow$), forming extensive three-dimensional hydrogen bonding networks both within sheets and between adjacent sheets. The antiparallel packing is thermodynamically irreversible ($\Delta G^\circ < 0$)."""
            },
            {
                "id": "prob-5-6",
                "problemNumber": "5.6",
                "title": "Lactose Mutarotation Polarimetry and Fehling Titration Stoichiometry",
                "difficulty": "Intermediate",
                "statement": r"""A $5.00\text{ g}$ sample of commercial lactose monohydrate ($C_{12}H_{22}O_{11}\cdot H_2O$, $M = 360.31\text{ g/mol}$) was dissolved in $100.0\text{ mL}$ of water.
(a) Freshly dissolved $\alpha$-lactose monohydrate exhibits $[\alpha]_D^{20} = +85.0^\circ$, while pure $\beta$-lactose exhibits $[\alpha]_D^{20} = +35.0^\circ$. Calculate the equilibrium mole fractions of $\alpha$- and $\beta$-lactose if the final equilibrium rotation is $[\alpha]_D^{\text{eq}} = +52.6^\circ$.
(b) In a quantitative Fehling titration, $1.0\text{ mole}$ of reducing disaccharide reduces exactly $2.0\text{ moles}$ of $\text{Cu}^{2+}$ to red cuprous oxide ($\text{Cu}_2\text{O}$). Calculate the mass of $\text{Cu}_2\text{O}$ ($M = 143.09\text{ g/mol}$) precipitated by a $10.0\text{ mL}$ aliquot of this lactose solution.""",
                "hints": [
                    r"Use [\alpha]_{eq} = x_\alpha [\alpha]_\alpha + (1 - x_\alpha) [\alpha]_\beta.",
                    r"Calculate moles of lactose in 10 mL aliquot.",
                    r"1 mole of lactose produces 1 mole of Cu2O (since 2 Cu(II) -> 1 Cu2O)."
                ],
                "solution": r"""### Step 1: Equilibrium Anomer Distribution
Using Biot's relationship:
$$[\alpha]_{\text{eq}} = x_\alpha [\alpha]_\alpha + (1 - x_\alpha) [\alpha]_\beta$$
$$+52.6 = x_\alpha (85.0) + (1 - x_\alpha) (35.0) = 35.0 + 50.0 x_\alpha$$
$$50.0 x_\alpha = 52.6 - 35.0 = 17.6$$
$$x_\alpha = \frac{17.6}{50.0} = 0.352 \implies \mathbf{35.2\%}$$
$$x_\beta = 1 - 0.352 = 0.648 \implies \mathbf{64.8\%}$$

### Step 2: Fehling Titration Stoichiometry
1. **Molarity of Lactose Solution**:
   $$n_{\text{total}} = \frac{5.00\text{ g}}{360.31\text{ g/mol}} = 0.013877\text{ mol}$$
   $$C = \frac{0.013877\text{ mol}}{0.1000\text{ L}} = 0.13877\text{ M}$$
2. **Moles in $10.0\text{ mL}$ Aliquot**:
   $$n_{\text{aliquot}} = 0.13877\text{ M} \times 0.0100\text{ L} = 1.3877\times 10^{-3}\text{ mol}$$
3. **Cuprous Oxide ($\text{Cu}_2\text{O}$) Precipitated**:
   Reduction of $\text{Cu}^{2+}$:
   $$\text{R-CHO} + 2\text{ Cu}^{2+} + 5\text{ OH}^- \to \text{R-COO}^- + \text{Cu}_2\text{O}(s) + 3\text{ H}_2\text{O}$$
   Stoichiometric ratio: $1\text{ mole lactose} \equiv 1\text{ mole }\text{Cu}_2\text{O}$.
   $$n_{\text{Cu}_2\text{O}} = 1.3877\times 10^{-3}\text{ mol}$$
   $$m_{\text{Cu}_2\text{O}} = (1.3877\times 10^{-3}\text{ mol}) \times 143.09\text{ g/mol} = 0.1986\text{ g} = \mathbf{198.6\text{ mg}}$$
A total of $198.6\text{ mg}$ of brick-red $\text{Cu}_2\text{O}$ precipitate is formed."""
            },
            {
                "id": "prob-5-7",
                "problemNumber": "5.7",
                "title": "Amylose-Triiodide Inclusion Complex Geometry and Electronic Transitions",
                "difficulty": "Advanced",
                "statement": r"""When iodine ($I_2$) is added to an aqueous solution of amylose in the presence of potassium iodide ($KI$), an intense deep blue inclusion complex forms ($\lambda_{\text{max}} = 640\text{ nm}$, $\epsilon \approx 40,000\text{ M}^{-1}\text{cm}^{-1}$).
(a) Describe the supramolecular clathrate architecture of the amylose helix containing the linear pentaiodide ($I_5^-$) or polyiodide ($I_n^-$) chain.
(b) Calculate the transition energy ($\Delta E$ in $\text{eV}$ and $\text{kJ/mol}$) corresponding to the $\lambda_{\text{max}} = 640\text{ nm}$ absorption band. Using the particle-in-a-box model for a conjugated 1D electron gas, explain why shorter amylose chains ($DP < 20$) produce red/brown complexes ($\lambda_{\text{max}} \sim 500\text{ nm}$) while long chains ($DP > 60$) produce deep blue/black complexes.""",
                "hints": [
                    r"\Delta E = h c / \lambda.",
                    r"1 eV = 1.602 x 10^-19 J; 1 mol = 6.022 x 10^23 particles.",
                    r"In particle in a box: \Delta E \propto 1 / L^2, so as box length L increases, \Delta E decreases and wavelength increases."
                ],
                "solution": r"""### Step 1: Transition Energy Calculation
For $\lambda_{\text{max}} = 640\text{ nm} = 640\times 10^{-9}\text{ m}$:
$$\Delta E = \frac{h c}{\lambda} = \frac{(6.626\times 10^{-34}\text{ J}\cdot\text{s})(2.998\times 10^8\text{ m/s})}{640\times 10^{-9}\text{ m}} = 3.104\times 10^{-19}\text{ J}$$
Converting to electron-volts ($\text{eV}$):
$$\Delta E = \frac{3.104\times 10^{-19}\text{ J}}{1.602\times 10^{-19}\text{ J/eV}} = \mathbf{1.938\text{ eV}}$$
Converting to $\text{kJ/mol}$:
$$\Delta E = (3.104\times 10^{-19}\text{ J}) \times (6.022\times 10^{23}\text{ mol}^{-1}) = 186.9\times 10^3\text{ J/mol} = \mathbf{186.9\text{ kJ/mol}}$$

### Step 2: Supramolecular Clathrate and Particle-in-a-Box Model
1. **Supramolecular Geometry**:
   The amylose single helix possesses a hydrophobic internal channel with a diameter of $\approx 0.5\text{ nm}$. Polyiodide anions assemble along the central channel axis as a linear, continuous one-dimensional chain:
   $$\cdots I_3^- \cdots I_2 \cdots I_3^- \cdots \quad \text{or} \quad [I_5^-]_n$$
2. **One-Dimensional Electron Gas Model**:
   The valence electrons of the aligned iodine atoms delocalize along the length $L$ of the polyiodide chain inside the channel.
   According to the 1D quantum particle-in-a-box model:
   $$E_n = \frac{n^2 h^2}{8 m_e L^2}$$
   The transition energy between the highest occupied molecular orbital (HOMO, level $N$) and lowest unoccupied molecular orbital (LUMO, level $N+1$) is:
   $$\Delta E = \frac{(2N + 1) h^2}{8 m_e L^2} \propto \frac{1}{L}$$
   - For short amylose fragments ($DP < 20$), the channel can only accommodate short chains ($I_3^-$ or $I_5^-$), corresponding to a small box length $L$. Thus $\Delta E$ is large, absorbing in the blue/green ($\lambda \sim 480 - 520\text{ nm}$) and appearing **red/brown**.
   - For high-molecular-weight amylose ($DP > 60$), the channel accommodates extended chains of $I_{15}^-$ to $I_{30}^-$. The box length $L$ increases, dramatically compressing the HOMO-LUMO gap. $\Delta E$ shifts into the red region ($\lambda_{\text{max}} \ge 640\text{ nm}$), transmitting deep **blue/indigo** light."""
            }
        ]
    }
    units.append(u5)

    # =========================================================================
    # UNIT 6: Amino Acids, Peptides & Protein Architectures
    # =========================================================================
    u6 = {
        "id": "unit-6",
        "unitNumber": 6,
        "title": "Unit 6: Amino Acids, Peptides & Protein Architectures",
        "leadSummary": "Comprehensive physical organic and biochemical foundations of amino acids, peptides, and proteins: classic and asymmetric chemical syntheses (Strecker, Gabriel, diethyl acetamidomalonate), multi-prototropic equilibria and isoelectric point ($pI$) calculus, amide bond stereodynamics and Ramachandran dihedral landscapes ($\phi, \psi$), Merrifield solid-phase peptide synthesis (SPPS), sequence determination via Edman degradation and tandem mass spectrometry, and the thermodynamics of protein folding.",
        "simulations": ["sim_nat_amino_acid_titration_pi"],
        "sections": [
            {
                "id": "sec-6-1",
                "secNumber": "6.1",
                "title": "Natural $\\alpha$-Amino Acids: Classification, Stereochemistry & Side Chains",
                "content": r"""Amino acids are bifunctional organic compounds containing both an amino group ($-\text{NH}_2$) and a carboxyl group ($-\text{COOH}$). In $\alpha$-amino acids, both groups are bonded to the same $\alpha$-carbon atom:
$$\text{H}_2\text{N}-\text{CH(R)}-\text{COOH}$$

### Stereochemical Configuration: The L-Series
With the exception of glycine (where $\text{R}=\text{H}$, which is achiral), all 19 standard proteinogenic amino acids possess a chiral $\alpha$-carbon:
- In Fischer projections with the $-\text{COOH}$ group at the top and side chain $\text{R}$ at the bottom, the $\alpha$-amino group points to the **left** in all naturally occurring proteinogenic amino acids. Thus, they belong to the **L-configuration**.
- Under the Cahn-Ingold-Prelog $(R/S)$ system, 18 of the 19 chiral L-amino acids are **$(S)$-enantiomers**.
- **L-Cysteine is the sole exception**: Because the sulfur atom in the $-\text{CH}_2\text{SH}$ side chain has a higher atomic number than the oxygen atoms of the carboxyl group, the priority of the side chain exceeds that of $-\text{COOH}$, rendering natural L-cysteine **(R)-cysteine**.

### Classification of the 20 Proteinogenic Side Chains
1. **Non-Polar, Aliphatic**: Glycine (Gly, G), Alanine (Ala, A), Valine (Val, V), Leucine (Leu, L), Isoleucine (Ile, I), Proline (Pro, P, a cyclic secondary imino acid), Methionine (Met, M).
2. **Aromatic**: Phenylalanine (Phe, F), Tyrosine (Tyr, Y), Tryptophan (Trp, W).
3. **Polar, Uncharged**: Serine (Ser, S), Threonine (Thr, T), Cysteine (Cys, C), Asparagine (Asn, N), Glutamine (Gln, Q).
4. **Positively Charged (Basic)**: Lysine (Lys, K, $\epsilon\text{-NH}_3^+$), Arginine (Arg, R, guanidinium), Histidine (His, H, imidazole).
5. **Negatively Charged (Acidic)**: Aspartate (Asp, D, $\beta\text{-COO}^-$), Glutamate (Glu, E, $\gamma\text{-COO}^-$)."""
            },
            {
                "id": "sec-6-2",
                "secNumber": "6.2",
                "title": "Chemical Synthesis of $\\alpha$-Amino Acids: Strecker, Gabriel & Acetamidomalonate",
                "content": r"""Industrial and laboratory syntheses provide racemic or enantiopure amino acids for pharmaceuticals and peptide chemistry.

### The Strecker Synthesis (1850)
One of the oldest multi-component reactions in organic chemistry, converting an aldehyde into an $\alpha$-amino acid:
1. **Imine Formation**: An aldehyde condenses with ammonia to form an imine (or iminium ion):
   $$\text{R-CHO} + \text{NH}_3 \rightleftharpoons \text{R-CH}=\text{NH} + \text{H}_2\text{O}$$
2. **Cyanide Addition**: Nucleophilic attack by cyanide ion ($\text{CN}^-$) affords an $\alpha$-aminonitrile:
   $$\text{R-CH}=\text{NH} + \text{HCN} \to \text{R-CH}(\text{NH}_2)\text{-CN}$$
3. **Acidic Hydrolysis**: Exhaustive hydrolysis of the nitrile with aqueous $\text{HCl}$ yields the racemic $\alpha$-amino acid:
   $$\text{R-CH}(\text{NH}_2)\text{-CN} + 2\text{ H}_2\text{O} + \text{HCl} \to \text{R-CH}(\text{NH}_3^+)\text{-COOH} \cdot \text{Cl}^- + \text{NH}_4\text{Cl}$$

### Gabriel Phthalimide Synthesis
Potassium phthalimide is alkylated with an $\alpha$-halo ester (e.g., ethyl $\alpha$-bromoacetate), followed by hydrazinolysis (Ing-Manske procedure) or acidic hydrolysis to yield pure primary amino acids without over-alkylation to secondary/tertiary amines.

### Diethyl Acetamidomalonate Synthesis
The most general and reliable laboratory protocol for complex amino acids:
1. Deprotonation of diethyl acetamidomalonate with sodium ethoxide generates a resonance-stabilized enolate:
   $$\text{CH}_3\text{CONH-CH}(\text{COOEt})_2 + \text{NaOEt} \to [\text{CH}_3\text{CONH-C}(\text{COOEt})_2]^- \text{Na}^+ + \text{EtOH}$$
2. Nucleophilic $S_N2$ alkylation with an alkyl halide ($\text{R-X}$) introduces the desired side chain:
   $$\to \text{CH}_3\text{CONH-C}(\text{R})(\text{COOEt})_2$$
3. Vigorous refluxing with concentrated aqueous $\text{HCl}$ or $\text{HBr}$ simultaneously hydrolyzes the amide, saponifies both ethyl esters to carboxylic acids, and triggers spontaneous decarboxylation of the geminal dicarboxylic acid, yielding the racemic $\alpha$-amino acid:
   $$\to \text{R-CH}(\text{NH}_3^+)\text{-COOH} + \text{CO}_2 + 2\text{ EtOH} + \text{CH}_3\text{COOH}$$"""
            },
            {
                "id": "sec-6-3",
                "secNumber": "6.3",
                "title": "Acid-Base Properties, Zwitterionic Equilibrium & Isoelectric Point ($pI$) Calculus",
                "content": r"""In both solid state and aqueous solution, amino acids exist predominantly as dipolar internal salts, known as **zwitterions** (German for 'hybrid ions'):
$$\text{H}_3\text{N}^+-\text{CH(R)}-\text{COO}^-$$
This explains their physical properties: high melting points ($>250^\circ\text{C}$ with decomposition), large dipole moments, and high solubility in polar water but insolubility in non-polar organic solvents.

### Multi-Prototropic Speciation
An amino acid with an ionizable side chain undergoes multiple sequential deprotonations:
$$\text{H}_3\text{A}^+ \underset{K_{a1}}{\rightleftharpoons} \text{H}_2\text{A}^{\pm} \underset{K_{a2}}{\rightleftharpoons} \text{HA}^- \underset{K_{a3}}{\rightleftharpoons} \text{A}^{2-}$$
The fractional population $\alpha_i$ of each species is governed by the Henderson-Hasselbalch equation:
$$\text{pH} = pK_a + \log\left(\frac{[\text{Base}]}{[\text{Acid}]}\right)$$

### Rigorous Calculus of the Isoelectric Point ($pI$)
The isoelectric point ($pI$) is the precise pH at which the net electrical charge of the amino acid ensemble is identically zero:
$$\langle z \rangle = \sum z_i \cdot \alpha_i = 0$$
At this pH, the molecule exhibits zero electrophoretic mobility.
1. **Simple Amino Acids (Diprotic, Non-Ionizable Side Chain)**:
   $$pI = \frac{pK_{a1}(\alpha\text{-COOH}) + pK_{a2}(\alpha\text{-NH}_3^+)}{2}$$
2. **Acidic Amino Acids (Aspartate, Glutamate)**:
   The zwitterionic form with net charge zero lies between the two carboxylic acid deprotonations:
   $$pI = \frac{pK_{a1}(\alpha\text{-COOH}) + pK_{aR}(\text{side-chain } -\text{COOH})}{2}$$
3. **Basic Amino Acids (Lysine, Arginine, Histidine)**:
   The neutral zwitterionic form lies between the two basic nitrogen deprotonations:
   $$pI = \frac{pK_{aR}(\text{side-chain}) + pK_{a2}(\alpha\text{-NH}_3^+)}{2}$$"""
            },
            {
                "id": "sec-6-4",
                "secNumber": "6.4",
                "title": "Peptides & The Peptide Bond: Partial Double-Bond Character & Ramachandran Plots",
                "content": r"""A peptide bond is an amide linkage formed by the condensation of the $\alpha$-carboxyl group of one amino acid with the $\alpha$-amino group of another:
$$\text{R}_1\text{-COOH} + \text{H}_2\text{N-R}_2 \to \text{R}_1\text{-CO-NH-R}_2 + \text{H}_2\text{O}$$

### Partial Double-Bond Character and Planarity
Linus Pauling and Robert Corey (1951) deduced the structural constraints of the peptide bond through X-ray crystallography:
- Resonance delocalization between the carbonyl $\pi$-electrons and the nitrogen lone pair creates a significant partial double bond:
  $$\text{O}=\text{C}-\text{N}-\text{H} \longleftrightarrow ^-\text{O}-\text{C}=\text{N}^+-\text{H}$$
- The $\text{C-N}$ bond length is $1.32\text{ \AA}$, intermediate between a standard $\text{C-N}$ single bond ($1.47\text{ \AA}$) and a $\text{C}=\text{N}$ double bond ($1.28\text{ \AA}$), possessing approximately $40\%$ double-bond character.
- The rotational energy barrier about the $\text{C-N}$ bond is substantial ($\Delta G^\ddagger \approx 84\text{ kJ/mol}$), locking the six atoms of the peptide group ($\text{C}_\alpha^i, \text{C}, \text{O}, \text{N}, \text{H}, \text{C}_\alpha^{i+1}$) into a rigid, planar **peptide plane**.
- The **trans conformation** (dihedral angle $\omega = 180^\circ$) is thermodynamically favored over the cis conformation ($\omega = 0^\circ$) by $\sim 10\text{ kJ/mol}$ due to steric clash between adjacent side chains (with proline being a notable exception where $\sim 10-20\%$ adopts cis).

### The Ramachandran Plot ($\phi, \psi$)
Conformational freedom in the protein backbone is restricted to rotation around two single bonds per residue:
- **$\phi$ (Phi)**: Torsion angle around the $\text{N}-\text{C}_\alpha$ bond.
- **$\psi$ (Psi)**: Torsion angle around the $\text{C}_\alpha-\text{C}$ bond.
G. N. Ramachandran calculated sterically allowed regions of $(\phi, \psi)$ space by modeling atoms as hard spheres. Steric clash between carbonyl oxygens, amide hydrogens, and $\text{C}_\beta$ atoms excludes over $75\%$ of conformation space, restricting stable secondary structures to narrow permissible islands:
- Right-handed $\alpha$-helix: $\phi \approx -57^\circ, \psi \approx -47^\circ$
- $\beta$-pleated sheets: $\phi \approx -120^\circ \text{ to } -140^\circ, \psi \approx +135^\circ \text{ to } +150^\circ$
- Left-handed $\alpha$-helix: $\phi \approx +57^\circ, \psi \approx +47^\circ$ (primarily glycine)"""
            },
            {
                "id": "sec-6-5",
                "secNumber": "6.5",
                "title": "Solid-Phase Peptide Synthesis (SPPS): The Merrifield Methodology & Coupling Reagents",
                "content": r"""R. Bruce Merrifield revolutionized protein chemistry in 1963 by inventing Solid-Phase Peptide Synthesis (SPPS, 1984 Nobel Prize), allowing automated, stepwise synthesis of long peptides on an insoluble polymeric resin support.

### The Merrifield Reaction Cycle
1. **Resin Anchoring**: The C-terminal amino acid is covalently attached via its carboxylate to an insoluble chloromethylated polystyrene resin (Merrifield resin) or functionalized Wang/2-chlorotrityl resin.
2. **Deprotection**: The temporary N-terminal protecting group is selectively cleaved:
   - **Boc Strategy**: Cleaved by $50\%$ trifluoroacetic acid (TFA).
   - **Fmoc Strategy (Modern Standard)**: Cleaved by $20\%$ piperidine in DMF via base-catalyzed E1cB elimination.
3. **Coupling**: The incoming amino acid, possessing an Fmoc-protected amino group and activated carboxyl group, is introduced in excess along with a coupling reagent:
   - **Carbodiimides**: DCC or DIC in the presence of HOBt or Oxyma.
   - **Phosphonium / Uronium Salts**: HBTU, HATU, or PyBOP in the presence of DIPEA base.
   These reagents convert the carboxylate into an activated ester that couples rapidly ($>99.5\%$ yield per cycle) without racemization.
4. **Washing**: Excess reagents and soluble byproducts are washed away through a sintered glass filter, eliminating the need for chromatographic purification after each step.
5. **Global Cleavage and Deprotection**: Once the full sequence is assembled, the peptide is cleaved from the resin and permanent side-chain protecting groups ($t\text{Bu}$, Trt, Pbf) are removed simultaneously using concentrated TFA ($95\%$) containing scavengers (triisopropylsilane, EDT, $\text{H}_2\text{O}$)."""
            },
            {
                "id": "sec-6-6",
                "secNumber": "6.6",
                "title": "Protein Sequence Determination: Edman Degradation & Mass Spectrometry",
                "content": r"""Determining the primary amino acid sequence of a polypeptide is essential for structural biology and proteomics.

### The Edman Degradation (Pehr Edman, 1950)
A cyclic, stepwise chemical sequencing method that removes one residue at a time from the unblocked N-terminus:
1. **Coupling**: Phenyl isothiocyanate (PITC, Edman's reagent) reacts with the free N-terminal amino group under mildly alkaline conditions ($\text{pH } 8.5 - 9.0$) to form a **phenylthiocarbamoyl (PTC) peptide**:
   $$\text{Ph-N}=\text{C}=\text{S} + \text{H}_2\text{N-CH(R}_1)\text{-CONH}\cdots \to \text{Ph-NH-CS-NH-CH(R}_1)\text{-CONH}\cdots$$
2. **Cleavage**: Anhydrous trifluoroacetic acid (TFA) protonates the sulfur atom and induces nucleophilic attack of the thiocarbonyl sulfur onto the first peptide carbonyl carbon. The first peptide bond is cleaved under anhydrous conditions, releasing an **anilinothiazolinone (ATZ) amino acid** and leaving the intact remaining peptide chain shortened by one residue.
3. **Conversion**: The unstable ATZ-amino acid is extracted into organic solvent and heated with aqueous acid to rearrange into a stable **phenylthiohydantoin (PTH) amino acid**.
4. **Identification**: The PTH-amino acid is identified by reversed-phase HPLC or LC-MS against calibrated standards. The cycle is repeated sequentially for 30–50 residues.

### Modern Mass Spectrometry: MALDI-TOF & ESI-MS/MS
- **Electrospray Ionization (ESI)** and **Matrix-Assisted Laser Desorption/Ionization (MALDI)** generate intact gas-phase peptide ions without thermal fragmentation.
- **Tandem Mass Spectrometry (MS/MS)**: Selected peptide ions are accelerated into a collision cell containing argon gas (Collision-Induced Dissociation, CID). Cleavage occurs predominantly at peptide backbone amide bonds, generating characteristic **$b$-ions** (retaining the N-terminus) and **$y$-ions** (retaining the C-terminus). The mass differences between successive peaks directly read out the amino acid sequence."""
            },
            {
                "id": "sec-6-7",
                "secNumber": "6.7",
                "title": "Protein Structural Hierarchy: Secondary, Tertiary & Quaternary Folding Landscapes",
                "content": r"""Proteins fold into unique three-dimensional conformations governed by thermodynamic stability and non-covalent interactions.

### The Four Levels of Protein Structure
1. **Primary Structure**: The covalent sequence of amino acids linked by peptide bonds.
2. **Secondary Structure**: Local spatial conformations stabilized by hydrogen bonds between backbone carbonyl oxygens ($\text{C}=\text{O}$) and amide nitrogens ($\text{N}-\text{H}$):
   - **$\alpha$-Helix**: Polypeptide chain coils in a right-handed helix with $3.6$ residues per turn (pitch $= 5.4\text{ \AA}$). Every backbone $\text{C}=\text{O}$ of residue $i$ forms an optimal linear hydrogen bond with the $\text{N}-\text{H}$ of residue $i+4$.
   - **$\beta$-Pleated Sheet**: Extended polypeptide chains aligned side-by-side, forming inter-strand hydrogen bonds. In **antiparallel $\beta$-sheets**, hydrogen bonds are linear and perpendicular ($180^\circ$); in **parallel $\beta$-sheets**, hydrogen bonds are slightly angled and weaker.
3. **Tertiary Structure**: The complete three-dimensional folding of a single polypeptide chain, driven by:
   - **Hydrophobic Effect**: Entropic release of structured water clathrates as non-polar aliphatic and aromatic side chains bury into the anhydrous protein core ($\Delta S_{\text{water}} > 0$).
   - **Electrostatic Interactions (Salt Bridges)**: Attractive ionic bonds between oppositely charged side chains (e.g., $\text{Lys}^+ \cdots \text{Glu}^-$).
   - **Disulfide Bridges**: Covalent $-\text{S}-\text{S}-$ crosslinks formed by the oxidation of two cysteine sulfhydryl groups.
4. **Quaternary Structure**: The assembly of multiple folded polypeptide subunits into a functional oligomeric complex (e.g., hemoglobin $\alpha_2\beta_2$ tetramer)."""
            }
        ],
        "problems": [
            {
                "id": "prob-6-1",
                "problemNumber": "6.1",
                "title": "Strecker Synthesis Mechanism and Asymmetric Synthesis of (S)-Phenylalanine",
                "difficulty": "Intermediate",
                "statement": r"""(a) Write out the complete stepwise mechanism for the synthesis of racemic phenylalanine starting from phenylacetaldehyde ($\text{PhCH}_2\text{CHO}$), ammonium chloride ($\text{NH}_4\text{Cl}$), and sodium cyanide ($\text{NaCN}$).
(b) To prepare enantiomerically pure $(S)$-phenylalanine directly, modern pharmaceutical chemistry employs chiral auxiliaries or chiral organocatalysts. Outline the catalytic asymmetric Strecker reaction using a chiral cyclic guanidine or BINOL-derived catalyst, explaining how facial selectivity is achieved during cyanide addition.""",
                "hints": [
                    r"Phenylacetaldehyde + NH3 -> imine.",
                    r"Cyanide attacks iminium carbon to form alpha-aminonitrile.",
                    r"Hydrolysis of nitrile to carboxylic acid preserves the carbon skeleton."
                ],
                "solution": r"""### Step 1: Classical Strecker Mechanism
1. **Imine Formation**:
   Phenylacetaldehyde reacts with ammonia (from $\text{NH}_4\text{Cl} + \text{NaCN}$ equilibrium):
   $$\text{PhCH}_2\text{CHO} + \text{NH}_3 \rightleftharpoons \text{PhCH}_2\text{CH}=\text{NH} + \text{H}_2\text{O}$$
   Protonation yields the reactive electrophilic iminium ion: $\text{PhCH}_2\text{CH}=\text{NH}_2^+$.
2. **Nucleophilic Cyanide Addition**:
   Cyanide ion ($\text{CN}^-$) attacks the iminium carbon:
   $$\text{PhCH}_2\text{CH}=\text{NH}_2^+ + \text{CN}^- \to \text{PhCH}_2\text{CH}(\text{NH}_2)\text{-CN} \quad (\alpha\text{-Aminonitrile})$$
3. **Acidic Hydrolysis**:
   Refluxing with aqueous $\text{HCl}$ protonates the nitrile nitrogen, followed by nucleophilic addition of water to form the amide intermediate, which hydrolyzes to the carboxylic acid:
   $$\text{PhCH}_2\text{CH}(\text{NH}_2)\text{-CN} + 2\text{ H}_2\text{O} + \text{H}^+ \to \text{PhCH}_2\text{CH}(\text{NH}_3^+)\text{-COOH} + \text{NH}_4^+$$
   This yields **racemic $(\pm)$-phenylalanine**.

### Step 2: Asymmetric Strecker Reaction
1. In an asymmetric organocatalytic Strecker reaction (e.g., Jacobsen chiral thiourea catalyst or chiral BINOL-phosphoric acid):
   - The chiral catalyst forms a dual hydrogen-bonding network with the imine nitrogen and the cyanide nucleophile (e.g., $\text{HCN}$ or $\text{TMSCN}$).
   - The bulky BINOL/thiourea scaffold completely blocks one face of the imine (the si-face).
   - Nucleophilic attack by cyanide is restricted exclusively to the **re-face**.
2. Hydrolysis of the resulting chiral aminonitrile yields **(S)-phenylalanine** in $>95\%$ enantiomeric excess ($ee$) without requiring racemic resolution."""
            },
            {
                "id": "prob-6-2",
                "problemNumber": "6.2",
                "title": "Multi-Prototropic Speciation and Isoelectric Point ($pI$) of Histidine",
                "difficulty": "Advanced",
                "statement": r"""L-Histidine is a triprotic amino acid possessing three ionizable functional groups:
- $\alpha\text{-COOH}$: $pK_{a1} = 1.82$
- Imidazole ring side chain: $pK_{aR} = 6.00$
- $\alpha\text{-NH}_3^+$: $pK_{a2} = 9.17$
(a) Write down the structures and net charges of all four ionic species ($\text{H}_3\text{His}^{2+}, \text{H}_2\text{His}^+, \text{HHis}^0, \text{His}^-$).
(b) Derive the exact mathematical formula for the isoelectric point ($pI$) and calculate its numerical value for histidine.
(c) At physiological $\text{pH } 7.40$, calculate the percentage of histidine molecules that have a positively charged imidazole side chain.""",
                "hints": [
                    r"At pI, the net charge is zero. Identify which two pKa values flank the neutral zwitterion HHis^0.",
                    r"The Henderson-Hasselbalch equation governs the ratio of deprotonated to protonated imidazole: pH = pK_{aR} + log([Im] / [ImH+])."
                ],
                "solution": r"""### Step 1: Speciation and Charges of Histidine
1. $\text{H}_3\text{His}^{2+}$ (at $\text{pH} < 1.82$): $\alpha\text{-COOH}$, protonated imidazole ($-\text{ImH}^+$), $\alpha\text{-NH}_3^+$. Net charge = **$+2$**.
2. $\text{H}_2\text{His}^+$ (at $1.82 < \text{pH} < 6.00$): $\alpha\text{-COO}^-$, protonated imidazole ($-\text{ImH}^+$), $\alpha\text{-NH}_3^+$. Net charge = **$+1$**.
3. $\text{HHis}^0$ (at $6.00 < \text{pH} < 9.17$): $\alpha\text{-COO}^-$, neutral imidazole ($-\text{Im}$), $\alpha\text{-NH}_3^+$. Net charge = **$0$** (Zwitterion).
4. $\text{His}^-$ (at $\text{pH} > 9.17$): $\alpha\text{-COO}^-$, neutral imidazole ($-\text{Im}$), unprotonated $\alpha\text{-NH}_2$. Net charge = **$-1$**.

### Step 2: Derivation and Calculation of $pI$
At the isoelectric point, the concentrations of positively charged species must balance negatively charged species:
$$[\text{H}_2\text{His}^+] + 2[\text{H}_3\text{His}^{2+}] = [\text{His}^-]$$
Near $pI$ (between $6.0$ and $9.2$), $[\text{H}_3\text{His}^{2+}]$ is negligible. Thus:
$$[\text{H}_2\text{His}^+] \approx [\text{His}^-]$$
Expressing both in terms of the neutral zwitterion $[\text{HHis}^0]$:
$$[\text{H}_2\text{His}^+] = \frac{[\text{H}^+] [\text{HHis}^0]}{K_{aR}}, \quad [\text{His}^-] = \frac{K_{a2} [\text{HHis}^0]}{[\text{H}^+]}$$
Equating:
$$\frac{[\text{H}^+] [\text{HHis}^0]}{K_{aR}} = \frac{K_{a2} [\text{HHis}^0]}{[\text{H}^+]}$$
$$[\text{H}^+]^2 = K_{aR} \cdot K_{a2}$$
Taking negative logarithms:
$$pI = \frac{pK_{aR} + pK_{a2}}{2} = \frac{6.00 + 9.17}{2} = \frac{15.17}{2} = \mathbf{7.585} \approx \mathbf{7.59}$$

### Step 3: Imidazole Protonation State at $\text{pH } 7.40$
Using the Henderson-Hasselbalch equation for the imidazole side chain ($pK_{aR} = 6.00$):
$$\text{pH} = pK_{aR} + \log\left(\frac{[\text{Im}]}{[\text{ImH}^+]}\right)$$
$$7.40 = 6.00 + \log\left(\frac{[\text{Im}]}{[\text{ImH}^+]}\right) \implies \log\left(\frac{[\text{Im}]}{[\text{ImH}^+]}\right) = 1.40$$
$$\frac{[\text{Im}]}{[\text{ImH}^+]} = 10^{1.40} = 25.12$$
Fraction protonated ($f_{\text{pos}}$):
$$f_{\text{pos}} = \frac{[\text{ImH}^+]}{[\text{Im}] + [\text{ImH}^+]} = \frac{1}{25.12 + 1} = \frac{1}{26.12} = 0.0383 \implies \mathbf{3.83\%}$$
At physiological pH 7.40, approximately **$3.8\%$** of histidine side chains are protonated/positively charged, making histidine uniquely suited as a versatile general acid-base catalyst in enzyme active sites."""
            },
            {
                "id": "prob-6-3",
                "problemNumber": "6.3",
                "title": "Peptide Bond Rotational Barrier and Double-Bond Resonance Energy",
                "difficulty": "Intermediate",
                "statement": r"""The rotational barrier about the central $\text{C}-\text{N}$ bond in formamide ($\text{HCONH}_2$) and model dipeptides is experimentally determined to be $\Delta G^\ddagger = 84.0\text{ kJ/mol}$ at $300\text{ K}$.
(a) Calculate the rate constant of cis-trans isomerization $k_{\text{iso}}$ using the Eyring equation:
$$k = \frac{k_B T}{h} \exp\left(-\frac{\Delta G^\ddagger}{R T}\right)$$
(b) Explain why peptidyl-prolyl cis-trans isomerases (PPIases) are essential cellular enzymes during nascent protein folding in the endoplasmic reticulum.""",
                "hints": [
                    r"k_B = 1.381 x 10^-23 J/K, h = 6.626 x 10^-34 J*s.",
                    r"R = 8.314 J/(mol*K), T = 300 K.",
                    r"Proline can adopt both cis and trans conformations with comparable energies, making non-catalyzed isomerization slow."
                ],
                "solution": r"""### Step 1: Rate Constant Calculation via Eyring Equation
At $T = 300\text{ K}$:
$$\frac{k_B T}{h} = \frac{(1.381\times 10^{-23}\text{ J/K})(300\text{ K})}{6.626\times 10^{-34}\text{ J}\cdot\text{s}} = 6.25\times 10^{12}\text{ s}^{-1}$$
The exponential factor:
$$\frac{\Delta G^\ddagger}{R T} = \frac{84,000\text{ J/mol}}{(8.314\text{ J/(mol}\cdot\text{K)})(300\text{ K})} = \frac{84,000}{2494.2} = 33.678$$
$$\exp(-33.678) = 2.36\times 10^{-15}$$
The isomerization rate constant is:
$$k_{\text{iso}} = (6.25\times 10^{12}\text{ s}^{-1}) \times (2.36\times 10^{-15}) = \mathbf{1.48\times 10^{-2}\text{ s}^{-1}}$$
The half-life for non-catalyzed cis-trans isomerization is:
$$t_{1/2} = \frac{\ln 2}{k_{\text{iso}}} = \frac{0.6931}{0.0148\text{ s}^{-1}} \approx \mathbf{46.8\text{ seconds}}$$

### Step 2: Biological Role of Peptidyl-Prolyl Isomerases (PPIases)
- In standard amino acids, steric clash forces $>99.9\%$ of peptide bonds into the trans conformation.
- In proline residues, because the pyrrolidine ring bridges back to the nitrogen, the energy difference between cis and trans peptide bonds ($\Delta G^\circ$) is only $4-8\text{ kJ/mol}$, resulting in $10-20\%$ of native prolyl bonds occupying the cis conformation.
- Because spontaneous uncatalyzed isomerization requires nearly a minute ($t_{1/2} \approx 47\text{ s}$), incorrect prolyl isomerization represents a severe kinetic bottleneck in protein folding.
- PPIases (such as cyclophilins and FKBP) accelerate prolyl cis-trans isomerization by lowering the $\text{C-N}$ double-bond barrier, allowing proteins to achieve their native functional tertiary fold on physiological millisecond timescales."""
            },
            {
                "id": "prob-6-4",
                "problemNumber": "6.4",
                "title": "Solid-Phase Peptide Synthesis Yield Compounding and Stepwise Efficiency",
                "difficulty": "Intermediate",
                "statement": r"""A peptide containing $N = 50$ amino acid residues is to be synthesized by automated solid-phase peptide synthesis (SPPS).
(a) The overall yield of the target peptide is given by $Y_{\text{overall}} = (y_{\text{step}})^{N-1}$, where $y_{\text{step}}$ is the average fractional coupling yield per cycle. Calculate the overall yield if $y_{\text{step}} = 95.0\%$, and compare it to an optimized protocol where $y_{\text{step}} = 99.5\%$.
(b) Calculate the maximum chain length $N$ that can be synthesized while maintaining an overall yield of at least $50.0\%$ when the coupling efficiency is $99.2\%$.
(c) Explain the function of acetic anhydride 'capping' in preventing deletion peptides and simplifying chromatographic purification.""",
                "hints": [
                    r"For N = 50, there are N - 1 = 49 coupling steps.",
                    r"Y = y^49. Compute for y = 0.95 and y = 0.995.",
                    r"Set 0.50 = (0.992)^(N-1) and solve for N using logarithms."
                ],
                "solution": r"""### Step 1: Overall Yield for 50-Residue Peptide
For an $N = 50$ residue peptide, exactly $49$ coupling cycles are required:
1. **At $95.0\%$ Coupling Efficiency ($y = 0.950$)**:
   $$Y_{\text{overall}} = (0.950)^{49} = \mathbf{0.081} \implies \mathbf{8.1\%}$$
   Over $91.9\%$ of the resin-bound material consists of truncated or deletion impurities!
2. **At $99.5\%$ Optimized Coupling Efficiency ($y = 0.995$)**:
   $$Y_{\text{overall}} = (0.995)^{49} = \mathbf{0.782} \implies \mathbf{78.2\%}$$
   An increase of just $4.5\%$ in stepwise efficiency produces a nearly **10-fold increase** in the recovery of the target peptide.

### Step 2: Maximum Chain Length for $50\%$ Overall Yield
Given $y = 0.992$ and target $Y \ge 0.50$:
$$(0.992)^{N-1} \ge 0.50$$
Taking natural logarithms:
$$(N - 1) \ln(0.992) \ge \ln(0.50)$$
$$(N - 1) (-0.008032) \ge -0.69315$$
$$N - 1 \le \frac{0.69315}{0.008032} = 86.3$$
$$N \le 87.3 \implies \mathbf{N = 87\text{ residues}}$$

### Step 3: Role of Capping with Acetic Anhydride
If an unreacted amino group fails to couple during cycle $k$, it will remain available to couple in cycle $k+1$, producing a **deletion peptide** missing residue $k$.
- Deletion peptides differ from the full-length target by only a single amino acid, making their chromatographic separation (by HPLC) virtually impossible.
- Treating the resin after each coupling step with acetic anhydride ($\text{Ac}_2\text{O} / \text{pyridine}$) acetylates all unreacted amine termini, permanently terminating their growth.
- These capped, truncated fragments have vastly different molecular weights and retention times, enabling straightforward HPLC purification of the target peptide."""
            },
            {
                "id": "prob-6-5",
                "problemNumber": "6.5",
                "title": "Edman Degradation Phenylthiohydantoin (PTH) Mechanism and Sequence Deduction",
                "difficulty": "Intermediate",
                "statement": r"""A purified pentapeptide isolated from an amphibian skin secretion was subjected to sequential automated Edman degradation. Chromatographic analysis of the released PTH-amino acid derivatives yielded:
- Cycle 1: PTH-Tyr
- Cycle 2: PTH-Gly
- Cycle 3: PTH-Gly
- Cycle 4: PTH-Phe
- Cycle 5: PTH-Leu
(a) State the primary sequence of the pentapeptide. Identify this physiologically active neuropeptide.
(b) Draw the chemical structure and curved-arrow mechanism for the conversion of the anilinothiazolinone (ATZ) intermediate into the stable phenylthiohydantoin (PTH) ring for Cycle 1.""",
                "hints": [
                    r"Edman degradation cleaves from the N-terminus to C-terminus.",
                    r"The sequence is H-Tyr-Gly-Gly-Phe-Leu-OH (Leucine-enkephalin).",
                    r"ATZ rearranges to PTH via ring opening by water followed by recyclization through nitrogen."
                ],
                "solution": r"""### Step 1: Sequence Deduction and Identification
Because the Edman degradation sequentially cleaves residues starting from the free **N-terminus**:
- N-terminus (Residue 1) = **Tyrosine (Tyr)**
- Residue 2 = **Glycine (Gly)**
- Residue 3 = **Glycine (Gly)**
- Residue 4 = **Phenylalanine (Phe)**
- C-terminus (Residue 5) = **Leucine (Leu)**
The primary amino acid sequence is:
$$\mathbf{H_2N-Tyr-Gly-Gly-Phe-Leu-COOH \quad (YGGFL)}$$
This peptide is **[Leu]-Enkephalin**, an endogenous opioid pentapeptide that binds with high affinity to $\mu$- and $\delta$-opioid receptors in the central nervous system.

### Step 2: Mechanism of ATZ $\to$ PTH Conversion
1. **ATZ Structure**:
   Cleavage of the PTC-peptide with anhydrous TFA yields the 5-membered **anilinothiazolinone (ATZ)** intermediate:
   $$\text{ATZ-Tyr contains a sulfur-containing 5-membered ring with a } \text{C}=\text{N-Ph bond and C}=\text{O bond.}$$
2. **Hydrolytic Ring Opening**:
   In aqueous acid ($1.0\text{ M HCl}$ at $80^\circ\text{C}$), water attacks the carbonyl carbon of the ATZ ring, opening it to form the acyclic phenylthiocarbamoyl amino acid intermediate:
   $$\text{ATZ} + \text{H}_2\text{O} \to \text{Ph-NH-CS-NH-CH}(\text{CH}_2\text{C}_6\text{H}_4\text{OH})\text{-COOH}$$
3. **Recyclization through Nitrogen**:
   The aniline nitrogen atom ($\text{Ph-NH}-$) attacks the carboxylic acid carbonyl carbon with elimination of water ($\text{H}_2\text{O}$).
   This closes a stable five-membered **phenylthiohydantoin (PTH)** ring with the sulfur atom remaining exocyclic ($\text{C}=\text{S}$) and the carbonyl oxygen exocyclic ($\text{C}=\text{O}$).
   The resulting **PTH-Tyrosine** is chemically stable, UV-active at $269\text{ nm}$, and readily quantified by reversed-phase HPLC."""
            },
            {
                "id": "prob-6-6",
                "problemNumber": "6.6",
                "title": "Ramachandran Steric Contour Mapping and Dihedral Angle Constraints",
                "difficulty": "Advanced",
                "statement": r"""Consider an L-alanine dipeptide model ($\text{Ac-Ala-NHMe}$).
(a) Define the dihedral angles $\phi$ (Phi), $\psi$ (Psi), and $\omega$ (Omega) by specifying the four consecutive backbone atoms that define each torsion angle.
(b) Explain why the conformation $(\phi = 0^\circ, \psi = 0^\circ)$ is strictly forbidden on the Ramachandran plot, identifying the specific steric clash that occurs.
(c) Why does glycine occupy a much larger permissible area on the Ramachandran plot compared to all other amino acids, and why is proline severely restricted to $\phi \approx -65^\circ \pm 15^\circ$?""",
                "hints": [
                    r"Phi is defined by C(i-1) - N(i) - Calpha(i) - C(i).",
                    r"Psi is defined by N(i) - Calpha(i) - C(i) - N(i+1).",
                    r"Omega is the peptide bond dihedral: Calpha(i) - C(i) - N(i+1) - Calpha(i+1).",
                    r"Glycine has H as its side chain; proline has a covalent ring."
                ],
                "solution": r"""### Step 1: Definition of Backbone Dihedral Angles
1. **$\phi$ (Phi)**: Defined by atoms **$\text{C}_{i-1} - \text{N}_i - \text{C}_{\alpha, i} - \text{C}_i$**. Rotation about the $\text{N}-\text{C}_\alpha$ bond.
2. **$\psi$ (Psi)**: Defined by atoms **$\text{N}_i - \text{C}_{\alpha, i} - \text{C}_i - \text{N}_{i+1}$**. Rotation about the $\text{C}_\alpha-\text{C}$ bond.
3. **$\omega$ (Omega)**: Defined by atoms **$\text{C}_{\alpha, i} - \text{C}_i - \text{N}_{i+1} - \text{C}_{\alpha, i+1}$**. Rotation about the peptide amide bond (constrained by partial double bond to $\omega \approx 180^\circ$ for trans).

### Step 2: The Forbidden $(\phi = 0^\circ, \psi = 0^\circ)$ Conformation
When $\phi = 0^\circ$ and $\psi = 0^\circ$:
- The $\text{C}_{i-1}=\text{O}_{i-1}$ carbonyl group is eclipsed with the $\text{C}_i=\text{O}_i$ carbonyl group.
- The distance between the carbonyl oxygen of residue $i-1$ and the amide nitrogen/hydrogen of residue $i+1$ drops below $1.8\text{ \AA}$, far below the sum of their van der Waals radii ($r_{\text{vdW}}(\text{O}) + r_{\text{vdW}}(\text{N}) \approx 3.0\text{ \AA}$).
- This severe van der Waals overlap generates an enormous steric repulsion penalty ($>100\text{ kJ/mol}$), making $(0^\circ, 0^\circ)$ completely forbidden.

### Step 3: Glycine vs Proline Conformational Flexibility
1. **Glycine**:
   - The side chain of glycine is a single hydrogen atom ($\text{R}=\text{H}$).
   - Lacking a bulky $\text{C}_\beta$ carbon, glycine experiences minimal steric hindrance across almost the entire $(\phi, \psi)$ landscape.
   - Glycine's Ramachandran plot is centrosymmetric, occupying over **$60\%$** of conformational space, allowing it to adopt conformations forbidden to all other residues (e.g., tight turns and left-handed helices).
2. **Proline**:
   - In proline, the aliphatic side chain forms a rigid five-membered pyrrolidine ring that is covalently bonded to the backbone nitrogen atom ($\text{C}_\delta-\text{N}$).
   - This covalent ring locks rotation around the $\text{N}-\text{C}_\alpha$ bond, restricting $\phi$ strictly to **$-65^\circ \pm 15^\circ$**.
   - Consequently, proline acts as a conformational 'helix breaker' and is predominantly found at the initiation of helices or in tight $\beta$-turns."""
            },
            {
                "id": "prob-6-7",
                "problemNumber": "6.7",
                "title": "Protein Thermal Denaturation Thermodynamics and Melting Temperature ($T_m$)",
                "difficulty": "Advanced",
                "statement": r"""A globular protein undergoes reversible two-state thermal unfolding:
$$\text{Native (N)} \rightleftharpoons \text{Denatured (D)}$$
Calorimetric measurements establish a denaturation enthalpy $\Delta H^\circ_{\text{unf}} = +420.0\text{ kJ/mol}$ and a denaturation entropy $\Delta S^\circ_{\text{unf}} = +1.280\text{ kJ/(mol}\cdot\text{K)}$ at the transition midpoint ($T_m$).
(a) Calculate the thermal melting temperature ($T_m$) in degrees Celsius.
(b) Calculate the Gibbs free energy of conformational stability ($\Delta G^\circ_{\text{unf}}$) at physiological temperature $T = 37.0^\circ\text{C}$ ($310.15\text{ K}$), assuming that the change in heat capacity $\Delta C_p$ is negligible over this temperature range.
(c) Calculate the fraction of unfolded protein ($f_D$) present at $37.0^\circ\text{C}$.""",
                "hints": [
                    r"At the melting temperature Tm, \Delta G^\circ = 0, so T_m = \Delta H^\circ / \Delta S^\circ.",
                    r"\Delta G^\circ(T) = \Delta H^\circ - T \Delta S^\circ.",
                    r"K_{unf} = \exp(-\Delta G^\circ / RT) and f_D = K_{unf} / (1 + K_{unf})."
                ],
                "solution": r"""### Step 1: Melting Temperature ($T_m$) Calculation
At the denaturation midpoint ($T_m$), exactly half of the protein is native and half is unfolded ($[\text{N}] = [\text{D}] \implies K_{\text{unf}} = 1$ and $\Delta G^\circ = 0$):
$$\Delta G^\circ = \Delta H^\circ - T_m \Delta S^\circ = 0$$
$$T_m = \frac{\Delta H^\circ_{\text{unf}}}{\Delta S^\circ_{\text{unf}}} = \frac{420.0\text{ kJ/mol}}{1.280\text{ kJ/(mol}\cdot\text{K)}} = 328.125\text{ K}$$
Converting to Celsius:
$$T_m = 328.125 - 273.15 = \mathbf{54.98^\circ\text{C}} \approx \mathbf{55.0^\circ\text{C}}$$

### Step 2: Gibbs Free Energy of Stability at $37.0^\circ\text{C}$
At $T = 310.15\text{ K}$ ($37.0^\circ\text{C}$):
$$\Delta G^\circ_{\text{unf}}(310.15\text{ K}) = \Delta H^\circ_{\text{unf}} - T \Delta S^\circ_{\text{unf}}$$
$$\Delta G^\circ_{\text{unf}} = 420.0\text{ kJ/mol} - (310.15\text{ K} \times 1.280\text{ kJ/(mol}\cdot\text{K)})$$
$$\Delta G^\circ_{\text{unf}} = 420.0 - 396.992 = \mathbf{+23.01\text{ kJ/mol}}$$
At body temperature, the native folded state is favored over the denatured state by $23.0\text{ kJ/mol}$ (the equivalent of approximately 4 to 5 hydrogen bonds).

### Step 3: Fraction of Unfolded Protein ($f_D$)
The unfolding equilibrium constant is:
$$K_{\text{unf}} = \exp\left(-\frac{\Delta G^\circ_{\text{unf}}}{R T}\right) = \exp\left(-\frac{23,010}{(8.314)(310.15)}\right) = \exp(-8.923) = 1.333\times 10^{-4}$$
The fraction unfolded ($f_D$) is:
$$f_D = \frac{K_{\text{unf}}}{1 + K_{\text{unf}}} = \frac{1.333\times 10^{-4}}{1 + 1.333\times 10^{-4}} \approx \mathbf{1.33\times 10^{-4}} \implies \mathbf{0.0133\%}$$
Only about 1 in every 7,500 protein molecules is denatured at physiological temperature."""
            }
        ]
    }
    units.append(u6)

    return units

if __name__ == "__main__":
    u = get_units_4_5_6()
    print(f"Successfully generated Units 4-6. Total units: {len(u)}")
    for unit in u:
        print(f"  {unit['id']}: {len(unit['sections'])} sections, {len(unit['problems'])} problems")
