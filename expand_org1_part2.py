# expand_org1_part2.py
# Deep academic enrichment for Unit 3 and Unit 4 of Organic Chemistry I
# Alkenes, Additions, Polymerization, Conjugated Dienes, Diels-Alder & Alkynes

def expand_unit3(u3):
    # Deepen Section 1: Alkene Structure & CIP Hierarchy
    u3["sections"][0]["content"] += r"""

### Cahn-Ingold-Prelog (CIP) Sequence Algorithm & Heats of Hydrogenation

The Cahn-Ingold-Prelog (CIP) priority rules establish an unambiguous, mathematical tree-traversal algorithm for assigning $(E)/(Z)$ descriptors to alkenes and $(R)/(S)$ descriptors to stereocenters:

#### 1. CIP Hierarchical Tree Traversal Rules:
1. **Rule 1 (Atomic Number)**: Higher atomic number precedes lower atomic number at the first point of difference along the ligand bond path:
   $$\text{I} (53) > \text{Br} (35) > \text{Cl} (17) > \text{S} (16) > \text{F} (9) > \text{O} (8) > \text{N} (7) > \text{C} (6) > \text{H} (1) > \text{lone pair} (0) \tag{3.1a}$$
2. **Rule 2 (Isotopic Mass)**: If atomic numbers are identical, heavier isotopes precede lighter isotopes:
   $$\text{T} (^3\text{H}) > \text{D} (^2\text{H}) > \text{H} (^1\text{H}); \quad ^{13}\text{C} > ^{12}\text{C} \tag{3.1b}$$
3. **Rule 3 (Successive Sphere Comparison)**: If atoms at distance 1 are identical, construct an ordered list of atoms bonded to them in descending priority order. Compare the lists atom-by-atom at the first point of difference.
4. **Rule 4 (Multiple Bonds - The Phantom Atom Rule)**: Multiply bonded atoms are duplicated by duplicating or triplicating them with phantom atoms (represented in parentheses with zero valence):
   $$-\text{CH}=\text{O} \equiv -\text{CH}(\text{O})-(\text{O}); \quad -\text{C}\equiv\text{N} \equiv -\text{C}(\text{N})_3 \tag{3.1c}$$

#### 2. Heats of Hydrogenation & Thermodynamic Stability Benchmarks:
The catalytic addition of $\text{H}_2$ across an alkene to yield an alkane is strongly exothermic.
Because all isomeric alkenes hydrogenate to the identical alkane, differences in standard heats of hydrogenation ($\Delta H_{\text{hydrog}}^\circ$) reflect the relative thermodynamic stability of the starting alkenes:

| Alkene Class | Example | Heats of Hydrogenation ($\Delta H_{\text{hydrog}}^\circ$) | Relative Thermodynamic Stability |
| :---: | :---: | :---: | :---: |
| **Monosubstituted** | 1-Butene | $\mathbf{-127\text{ kJ/mol}}$ ($-30.3\text{ kcal/mol}$) | Least stable |
| **gem-Disubstituted** | 2-Methylpropene | $\mathbf{-119\text{ kJ/mol}}$ ($-28.4\text{ kcal/mol}$) | Intermediate |
| **cis-Disubstituted** | cis-2-Butene | $\mathbf{-120\text{ kJ/mol}}$ ($-28.6\text{ kcal/mol}$) | Intermediate (steric clash) |
| **trans-Disubstituted** | trans-2-Butene | $\mathbf{-115\text{ kJ/mol}}$ ($-27.6\text{ kcal/mol}$) | Stable |
| **Trisubstituted** | 2-Methyl-2-butene | $\mathbf{-113\text{ kJ/mol}}$ ($-26.9\text{ kcal/mol}$) | Highly stable |
| **Tetrasubstituted** | 2,3-Dimethyl-2-butene | $\mathbf{-111\text{ kJ/mol}}$ ($-26.6\text{ kcal/mol}$) | Most stable |

- **Physical Origin of Stability**: Increasing alkyl substitution stabilizes alkenes through:
  1. **Hyperconjugation**: Overlap between filled $\sigma_{\text{C-H}}$ and $\sigma_{\text{C-C}}$ bonds of alkyl substituents and the empty $\pi^*$ antibonding orbital of the double bond ($\sigma \to \pi^*$).
  2. **Bond Strength**: An $sp^2-sp^3$ $\text{C}-\text{C}$ single bond is shorter and stronger ($D \approx 360\text{ kJ/mol}$) than an $sp^3-sp^3$ single bond ($D \approx 347\text{ kJ/mol}$)."""

    # Deepen Section 2: Alkene Syntheses & Stereospecific E2 Eliminations
    u3["sections"][1]["content"] += r"""

### Stereospecific Anti-Periplanar E2 Elimination in Cyclohexyl Systems

The base-promoted $E2$ elimination requires a strict **anti-periplanar transition state** ($\text{H}-\text{C}-\text{C}-\text{X}$ dihedral angle $\phi = 180^\circ$) to maximize overlap between the breaking $\sigma_{\text{C-H}}$ bonding orbital, the forming $\pi$ bond, and the departing $\sigma^*_{\text{C-X}}$ antibonding orbital.

#### Menthyl Chloride vs Neomenthyl Chloride:
This stereoelectronic requirement is demonstrated by the diastereomeric pair **menthyl chloride** and **neomenthyl chloride**:

1. **Neomenthyl Chloride (Chlorine is Axial in Most Stable Chair)**:
   - In its ground-state chair conformation, the bulky isopropyl group (A-value $= 2.15$) and methyl group (A-value $= 1.74$) occupy equatorial positions, placing the chlorine atom in the **axial position** at C3.
   - The axial chlorine has two anti-periplanar axial hydrogens available on adjacent carbons: $\text{H}_{\text{ax}}$ at C2 (tertiary carbon) and $\text{H}_{\text{ax}}$ at C4 (secondary carbon).
   - Elimination occurs rapidly upon treatment with ethoxide ($k_{\text{rel}} = 200$) to yield the more substituted, thermodynamic **3-menthene** as the major Zaitsev product ($75\%$) alongside 2-menthene ($25\%$).

2. **Menthyl Chloride (Chlorine is Equatorial in Most Stable Chair)**:
   - In its ground-state chair conformation, chlorine is equatorial alongside isopropyl and methyl.
   - In the equatorial position, chlorine has zero anti-periplanar hydrogens ($\phi \approx 60^\circ$).
   - Elimination cannot occur from the ground state! The molecule must undergo an unfavorable chair-flip to a high-energy conformer where all three substituents become axial.
   - In this diaxial conformer, the only available anti-periplanar hydrogen is at C4; the tertiary hydrogen at C2 is equatorial and cannot participate!
   - Consequently, reaction rate is over **200 times slower**, and the reaction exclusively produces the less-substituted **2-menthene** ($100\%$), completely violating Zaitsev's rule due to absolute stereoelectronic anti-periplanar control!"""

    # Deepen Section 3: Electrophilic Additions & Rearrangements
    u3["sections"][2]["content"] += r"""

### Wagner-Meerwein Rearrangements & The Peroxide Kharasch Effect

Electrophilic additions that generate open carbocation intermediates are subject to instantaneous 1,2-shifts if a more stable carbocation can be produced:

#### 1. Wagner-Meerwein 1,2-Hydride & 1,2-Alkyl Shifts:
Consider the addition of $\text{HCl}$ to 3,3-dimethyl-1-butene (neopentylethylene):
$$\text{CH}_2=\text{CH}-\text{C}(\text{CH}_3)_3 + \text{H}^+ \longrightarrow \left[ \text{CH}_3-\stackrel{\oplus}{\text{CH}}-\text{C}(\text{CH}_3)_3 \right] \quad (2^\circ \text{ Carbocation}) \tag{3.9a}$$
- The secondary carbocation possesses an empty $p$-orbital adjacent to the bulky quaternary center.
- A methyl group migrates with its electron pair (1,2-methide shift) through a three-center two-electron bridge:
  $$\left[ \text{CH}_3-\stackrel{\oplus}{\text{CH}}-\text{C}(\text{CH}_3)_3 \right] \xrightarrow{1,2\text{-methyl shift}} \left[ \text{CH}_3-\text{CH}(\text{CH}_3)-\stackrel{\oplus}{\text{C}}(\text{CH}_3)_2 \right] \quad (3^\circ \text{ Carbocation}) \tag{3.9b}$$
- Nucleophilic trapping by chloride yields **2-chloro-2,3-dimethylbutane** as the major rearranged product ($85\%$) alongside unrearranged 3-chloro-2,2-dimethylbutane ($15\%$).

#### 2. The Kharasch Peroxide Effect: Radical Mechanism of Anti-Markovnikov $\text{HBr}$ Addition:
In 1933, Morris Kharasch discovered that while addition of $\text{HBr}$ to alkenes in purified solvents gives Markovnikov products, traces of peroxides ($\text{ROOR}$) invert the regiochemistry to **anti-Markovnikov**:
1. **Initiation**: $\text{ROOR} \xrightarrow{\Delta \text{ or } h\nu} 2\,\text{RO}^\bullet \xrightarrow{+\text{HBr}} \text{ROH} + \mathbf{\text{Br}^\bullet}$
2. **Propagation 1 (Regioselective Radical Attack)**:
   $$\text{R}-\text{CH}=\text{CH}_2 + \text{Br}^\bullet \longrightarrow \mathbf{\text{R}-\stackrel{\bullet}{\text{C}}\text{H}-\text{CH}_2\text{Br}} \tag{3.9c}$$
   - The bromine radical attacks the **less substituted terminal carbon** because this generates the significantly more stable secondary radical rather than an unstable primary radical ($E_a \approx 8\text{ kJ/mol}$).
3. **Propagation 2 (Hydrogen Abstraction)**:
   $$\text{R}-\stackrel{\bullet}{\text{C}}\text{H}-\text{CH}_2\text{Br} + \text{HBr} \longrightarrow \mathbf{\text{R}-\text{CH}_2-\text{CH}_2\text{Br}} + \text{Br}^\bullet \tag{3.9d}$$

#### Why the Peroxide Effect is Strictly Unique to $\text{HBr}$:
- For $\text{HCl}$: Propagation 2 ($\text{R}^\bullet + \text{HCl} \to \text{RH} + \text{Cl}^\bullet$) is strongly endothermic ($\Delta H^\circ \approx +35\text{ kJ/mol}$) due to the high $\text{H}-\text{Cl}$ bond energy ($431\text{ kJ/mol}$), halting the chain.
- For $\text{HI}$: Propagation 1 ($\text{I}^\bullet + \text{alkene} \to \text{radical}$) is endothermic ($\Delta H^\circ \approx +22\text{ kJ/mol}$) due to the weak $\text{C}-\text{I}$ bond ($222\text{ kJ/mol}$), making addition reversible.
- Only for $\text{HBr}$ are **both propagation steps exothermic** ($\Delta H_1^\circ = -42\text{ kJ/mol}$, $\Delta H_2^\circ = -46\text{ kJ/mol}$), allowing self-sustaining radical chain catalysis!"""

    # Deepen Section 4: Halogenation & Halonium Ions
    u3["sections"][3]["content"] += r"""

### Stereochemical Outcomes of Bromination: Meso vs Racemic Mixtures

The electrophilic addition of bromine ($\text{Br}_2$) to alkenes proceeds via a three-membered cyclic **bromonium ion** intermediate, enforcing strict **anti-stereospecificity**:

#### Stereochemical Proof via (E)- and (Z)-2-Butene:
1. **Addition to trans-2-Butene ((E)-isomer)**:
   - Bromine attacks trans-2-butene to form an achiral meso-bromonium ion with a $C_{2v}$ plane of symmetry.
   - Subsequent backside attack by bromide ion ($\text{Br}^-$) with equal probability at C2 or C3 produces:
     $$\text{trans-2-Butene} + \text{Br}_2 \longrightarrow \mathbf{meso\text{-2,3-dibromobutane (Optically Inactive, Single Diastereomer)}} \tag{3.12a}$$
2. **Addition to cis-2-Butene ((Z)-isomer)**:
   - Bromine attacks cis-2-butene to form a chiral pair of enantiomeric bromonium ions.
   - Backside attack by bromide at either carbon inverts that center, yielding an equimolar mixture of $(2R, 3R)$ and $(2S, 3S)$ enantiomers:
     $$\text{cis-2-Butene} + \text{Br}_2 \longrightarrow \mathbf{(\pm)\text{-2,3-dibromobutane (Racemic Mixture, Optically Inactive by External Compensation)}} \tag{3.12b}$$

#### Isolation of Stable Bromonium Ions:
In 1969, Strating, Bolster, and Wynne isolated and crystal-analyzed the first stable bromonium triflate salt using **adamantylideneadamantane**. The bulky adamantyl cages steric shield both faces of the three-membered ring, preventing nucleophilic attack by bromide and allowing single-crystal X-ray diffraction that conclusively proved the symmetric $\text{C}-\text{Br}-\text{C}$ three-membered ring geometry ($r_{\text{C}-\text{Br}} = 2.11\text{ \AA}$, $\angle \text{C}-\text{Br}-\text{C} = 65.8^\circ$)!"""

    # Deepen Section 5: Hydration Protocols
    u3["sections"][4]["content"] += r"""

### Stereochemical Retention in the Hydroboration-Oxidation Mechanism

The hydroboration-oxidation sequence converts alkenes into alcohols with anti-Markovnikov regiochemistry and syn-stereospecificity. The alkaline peroxide oxidation step demonstrates an extraordinary stereochemical phenomenon: **complete retention of configuration at carbon**:

#### Line-by-Line Mechanistic Sequence of Oxidation:
$$\text{R}_3\text{B} + \text{HOO}^- \longrightarrow [\text{R}_3\text{B}-\text{O}-\text{O}-\text{H}]^- \tag{3.15a}$$
1. **Nucleophilic Addition**: The hydroperoxide anion ($\text{HOO}^-$, generated by $\text{H}_2\text{O}_2 + \text{OH}^-$) coordinates to the vacant $p$-orbital of boron, forming a tetrahedral borate complex.
2. **1,2-Alkyl Migration with Retention**:
   An alkyl group migrates with its bonding pair from boron to the adjacent oxygen atom, displacing hydroxide ion:
   $$[\text{R}_2\text{B}(\text{R})-\text{O}-\text{OH}]^- \xrightarrow{\text{1,2-shift}} \text{R}_2\text{B}-\text{O}-\text{R} + \text{OH}^- \tag{3.15b}$$
   - **Stereochemical Preservation**: The migrating carbon atom interacts with oxygen from the *same face* as its bond to boron via a three-center two-electron $[B-C-O]$ transition state.
   - The carbon center never becomes detached as a free carbocation or radical; therefore, **its stereochemical configuration is preserved with $100\%$ retention**!
3. **Repeated Migration & Hydrolysis**:
   The migration repeats twice more until all three alkyl groups are converted to an orthoborate ester $\text{B}(\text{OR})_3$. Basic hydrolysis then quantitatively yields three equivalents of alcohol and sodium borate:
   $$\text{B}(\text{OR})_3 + 3\,\text{OH}^- \longrightarrow 3\,\mathbf{\text{R-OH}} + \text{BO}_3^{3-} \tag{3.15c}$$"""

    # Deepen Section 6: Alkene Oxidations & Criegee Ozonolysis
    u3["sections"][5]["content"] += r"""

### Detailed Multistep Criegee Mechanism of Ozonolysis

Ozonolysis provides a diagnostic method for locating the position of double bonds through oxidative cleavage. The complete mechanism, elucidated by Rudolf Criegee in 1953, proceeds through three distinct pericyclic steps:

```
                O             O-O                              O-O
                ||    [3+2]   /  \    Retro-[3+2]             /   \
   R2C = CR2 +  O-O  ------> R2C--CR2 -----------> R2C=O +  R2C    O
                             (Molozonide)                   \_____/
                                                         (Criegee Zwitterion)
                                                                |
                                                                | [3+2]
                                                                v
                                                             O-O
                                                            /   \
                                                          R2C    CR2
                                                           \  O  /
                                                            \___/
                                                          (Secondary Ozonide)
```

1. **Step 1: 1,3-Dipolar Cycloaddition to Molozonide**:
   Ozone ($:\stackrel{-}{\text{O}}-\stackrel{+}{\text{O}}=\text{O}$) undergoes a concerted $[3+2]$ cycloaddition across the alkene $\pi$ bond to form an unstable primary ozonide (**molozonide** or 1,2,3-trioxolane).
2. **Step 2: Retro-[3+2] Cycloaddition**:
   The weak $\text{O}-\text{O}$ single bonds and strained ring induce spontaneous cycloreversion, cleaving both the $\text{C}-\text{C}$ $\sigma$-bond and one $\text{O}-\text{O}$ bond to generate a **carbonyl compound** and a **carbonyl oxide** (Criegee zwitterion / 1,3-dipole):
   $$\text{Molozonide} \longrightarrow \text{R}_2\text{C}=\text{O} + [\text{R}_2\stackrel{+}{\text{C}}-\text{O}-\text{O}^- \longleftrightarrow \text{R}_2\text{C}=\stackrel{+}{\text{O}}-\text{O}^-] \tag{3.16a}$$
3. **Step 3: Recombination to Secondary Ozonide (1,2,4-Trioxolane)**:
   The carbonyl oxide flips orientation and undergoes a second $[3+2]$ dipolar cycloaddition across the carbonyl group, forming the stable **secondary ozonide** (1,2,4-trioxolane).
4. **Workup Regimes**:
   - **Reductive Workup ($\text{Me}_2\text{S}$ or $\text{Zn} / \text{AcOH}$)**: Reduces the trioxolane to aldehydes and ketones without over-oxidation:
     $$\text{Secondary Ozonide} + \text{Me}_2\text{S} \longrightarrow 2\,\text{Carbonyls} + \text{Me}_2\text{SO} \tag{3.16b}$$
   - **Oxidative Workup ($\text{H}_2\text{O}_2 / \text{NaOH}$)**: Any aldehydes are oxidized to carboxylic acids:
     $$\text{R-CHO} + \text{H}_2\text{O}_2 \longrightarrow \mathbf{\text{R-COOH}} + \text{H}_2\text{O} \tag{3.16c}$$"""
    return u3


def expand_unit4(u4):
    # Deepen Section 1: Conjugated Dienes & Woodward-Fieser Rules
    u4["sections"][0]["content"] += r"""

### Woodward-Fieser Empirical UV-Vis Rules for Conjugated Systems

In conjugated polyenes, absorption of ultraviolet light promotes an electron from the Highest Occupied Molecular Orbital (HOMO) to the Lowest Unoccupied Molecular Orbital (LUMO) via a $\pi \to \pi^*$ transition.
In 1941, Robert Burns Woodward and Louis Fieser established empirical rules to predict the wavelength of maximum absorption ($\lambda_{\text{max}}$) with remarkable accuracy ($\pm 2-3\text{ nm}$):

#### Base Values:
- Acyclic conjugated diene or heteroannular diene: $\mathbf{214\text{ nm}}$
- Homoannular diene (both double bonds in the same ring): $\mathbf{253\text{ nm}}$

#### Increments for Substituents and Structural Features:
- Extended conjugation (each additional conjugated double bond): $\mathbf{+30\text{ nm}}$
- Alkyl substituent or ring residue: $\mathbf{+5\text{ nm}}$
- Exocyclic double bond (double bond attached to a ring carbon): $\mathbf{+5\text{ nm}}$
- Polar Auxochromes:
  - $-\text{O-Acyl}$: $\mathbf{0\text{ nm}}$
  - $-\text{O-Alkyl}$: $\mathbf{+6\text{ nm}}$
  - $-\text{S-Alkyl}$: $\mathbf{+30\text{ nm}}$
  - $-\text{Cl}, -\text{Br}$: $\mathbf{+5\text{ nm}}$
  - $-\text{NR}_2$: $\mathbf{+60\text{ nm}}$

#### Diagnostic Calculation Example:
Consider cholesta-3,5-diene:
- Base value (heteroannular diene): $214\text{ nm}$
- Three ring residues attached to conjugated carbons ($3 \times 5\text{ nm}$): $+15\text{ nm}$
- One exocyclic double bond at C3: $+5\text{ nm}$
$$\lambda_{\text{calc}} = 214 + 15 + 5 = \mathbf{234\text{ nm}} \quad (\text{Observed experimental value: } 235\text{ nm})$$"""

    # Deepen Section 2: Diels-Alder FMO & Alder Endo Rule
    u4["sections"][1]["content"] += r"""

### Frontier Molecular Orbital (FMO) Theory & Secondary Orbital Overlap

The Diels-Alder reaction is a thermally allowed $[4_s + 2_s]$ cycloaddition between a conjugated diene ($4\pi$ electrons) and a dienophile ($2\pi$ electrons).

#### 1. FMO Orbital Symmetry Analysis:
Under normal electron demand:
- **Diene acts as electron donor**: The relevant orbital is its $\text{HOMO} (\psi_2)$, which has a nodal plane between C2 and C3. The terminal coefficients at C1 and C4 have **opposite phases**:
  $$\psi_2 = 0.602\,\phi_1 + 0.372\,\phi_2 - 0.372\,\phi_3 - 0.602\,\phi_4 \tag{4.4a}$$
- **Dienophile acts as electron acceptor**: The relevant orbital is its $\text{LUMO} (\pi^*)$, which has a nodal plane between the two carbons and **opposite phases**:
  $$\pi^* = 0.707\,\phi_5 - 0.707\,\phi_6 \tag{4.4b}$$
- Matching phases at the terminals allows simultaneous bonding overlap at both ends in a **suprafacial-suprafacial geometry**, establishing that $[4_s + 2_s]$ is thermally allowed with a small activation barrier.

#### 2. The Alder Endo Rule & Secondary Orbital Interactions:
When a substituted dienophile with a conjugated electron-withdrawing group (such as maleic anhydride or methyl acrylate) reacts with a cyclic diene (such as cyclopentadiene), two diastereomeric transition states are possible:
1. **Endo Transition State**: The dienophile's activating substituent ($-\text{C}=\text{O}$ or $-\text{C}\equiv\text{N}$) is oriented **underneath the diene $\pi$ system**.
2. **Exo Transition State**: The substituent is oriented **away from the diene $\pi$ system**.

Although the endo product is often thermodynamically less stable due to steric congestion in the product:
- In the **endo transition state**, the $\pi^*$ orbital of the carbonyl group overlaps favorably with the developing $\pi$ bond between C2 and C3 of the diene.
- This **secondary orbital overlap** provides an additional $6-12\text{ kJ/mol}$ of transition-state electronic stabilization, lowering $\Delta G^\ddagger_{\text{endo}}$ and making the **endo adduct the kinetically favored product by $>95\%$** at low temperatures!"""

    # Deepen Section 4: Alkynes & Acidity
    u4["sections"][3]["content"] += r"""

### Thermodynamic Acidity of Hydrocarbons: Hybridization & Anion Solvation

The Brønsted-Lowry acidity of hydrocarbons depends decisively on the hybridization of the carbon atom bearing the acidic proton:

$$\text{CH}_3\text{CH}_3 \quad (pK_a \approx 50) \quad \ll \quad \text{CH}_2=\text{CH}_2 \quad (pK_a \approx 44) \quad \ll \quad \text{H}-\text{C}\equiv\text{C}-\text{H} \quad (pK_a \approx 25) \tag{4.7a}$$

#### Quantum Physical Explanation:
1. **$s$-Character Concentration**:
   - In ethane ($sp^3$), the lone pair of the conjugate base resides in an orbital with $25\% s$-character.
   - In ethene ($sp^2$), the carbanion lone pair resides in an orbital with $33.3\% s$-character.
   - In ethyne ($sp$), the acetylide carbanion lone pair resides in an orbital with **$50\% s$-character**.
2. **Radial Proximity to Positive Nucleus**:
   Because $s$-orbitals penetrate close to the nucleus without angular nodes, electrons with higher $s$-character experience a substantially higher effective nuclear attraction.
   The acetylide lone pair is held tightly close to the positively charged carbon nucleus, dramatically stabilizing the conjugate base ($\text{R}-\text{C}\equiv\text{C}^-$) relative to alkyl or vinyl carbanions.
3. **Deprotonation Regimes**:
   - Hydroxide ion ($\text{OH}^-$, conjugate acid $pK_a = 15.7$) or alkoxides ($\text{RO}^-$, $pK_a \approx 16$) are insufficiently basic to deprotonate terminal alkynes:
     $$K_{\text{eq}} = 10^{15.7 - 25} = 10^{-9.3} \tag{4.7b}$$
   - Strong bases whose conjugate acids have $pK_a > 30$ are required, such as **sodium amide ($\text{NaNH}_2$) in liquid ammonia** ($pK_a \approx 38$, $K_{\text{eq}} = 10^{13}$) or **n-butyllithium ($\text{n-BuLi}$)** ($pK_a \approx 50$, $K_{\text{eq}} = 10^{25}$)."""

    # Deepen Section 7: Reduction of Alkynes
    u4["sections"][6]["content"] += r"""

### Stereoselective Reductions: Lindlar Hydrogenation vs Birch Dissolving Metal

Terminal and internal alkynes can be reduced with complete, switchable stereocontrol to synthesize either pure $(Z)$-alkenes or pure $(E)$-alkenes:

#### 1. Stereospecific Syn-Reduction to (Z)-Alkenes (Lindlar Catalyst):
$$\text{R}-\text{C}\equiv\text{C}-\text{R}' + \text{H}_2 \xrightarrow{\text{Pd}/\text{CaCO}_3, \;\text{Pb(OAc)}_2, \;\text{quinoline}} \mathbf{\text{cis-(Z)-Alkene}} \tag{4.16a}$$
- **Poisoning Mechanism**: Metallic palladium is supported on calcium carbonate and intentionally poisoned with lead acetate ($\text{Pb(OAc)}_2$) and quinoline.
- The poison selectively blocks the most reactive palladium terrace sites that catalyze alkene hydrogenation, while leaving open step sites that can only reduce alkynes ($\Delta G^\ddagger_{\text{alkene hydrog}} \gg \Delta G^\ddagger_{\text{alkyne hydrog}}$).
- Both hydrogen atoms are delivered simultaneously from the **metallic catalyst surface to the same face** of the adsorbed alkyne, yielding $(Z)$-alkenes with $>98\%$ stereochemical purity.

#### 2. Stereoselective Anti-Reduction to (E)-Alkenes (Dissolving Metal Birch Reduction):
$$\text{R}-\text{C}\equiv\text{C}-\text{R}' + 2\,\text{Na} + 2\,\text{NH}_3 \xrightarrow{-33^\circ\text{C}} \mathbf{\text{trans-(E)-Alkene}} + 2\,\text{NaNH}_2 \tag{4.16b}$$
- **Step 1: Single Electron Transfer (SET)**:
  Sodium dissolves in liquid ammonia to form solvated electrons ($e^-_{\text{am}}$), creating an intense deep blue solution. A solvated electron transfers to the alkyne $\pi^*$ orbital to form a radical anion:
  $$\text{R}-\text{C}\equiv\text{C}-\text{R}' + e^-_{\text{am}} \longrightarrow [\text{R}-\dot{\text{C}}=\bar{\text{C}}-\text{R}']^\bullet \tag{4.16c}$$
- **Step 2: Rapid Radical Inversion to Anti-Conformation**:
  The radical anion exists in equilibrium between cis and trans geometries. The **trans-radical anion** is thermodynamically favored by $20-30\text{ kJ/mol}$ due to minimized steric repulsion between bulky R groups and minimized Coulombic repulsion between the lone pair and radical lobe.
- **Step 3: Protonation**:
  The trans-radical anion abstracts a proton from ammonia solvent ($pK_a = 38$) to generate a trans-vinyl radical:
  $$[\text{trans-R}-\dot{\text{C}}=\bar{\text{C}}-\text{R}']^\bullet + \text{NH}_3 \longrightarrow \text{trans-R}-\dot{\text{C}}=\text{CH}-\text{R}' + \text{NH}_2^- \tag{4.16d}$$
- **Step 4: Second SET & Protonation**:
  A second solvated electron reduces the trans-vinyl radical to a trans-vinyl anion, which is quenched by ammonia to yield exclusively the **trans-(E)-alkene**!"""
    return u4
