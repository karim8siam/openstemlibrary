# -*- coding: utf-8 -*-
"""
expand_org2_monograph.py
Honors Monograph & Deep Physical Organic Theory Module for Organic Chemistry II.
Injects comprehensive theoretical monographs, kinetic isotope effects,
Zimmerman-Traxler transition state models, Thorpe-Ingold conformational dynamics,
Woodward-Hoffmann orbital correlation diagrams, and structure-based drug design.
Brings the master data file to >66,000 words.
Strict zero course numbers or marks.
"""

def inject_monographs(units):
    print("Injecting advanced university honors monographs across all 9 units...")

    # --- UNIT 1: Clar Sextet Topology in Graphenes & Nanoribbons ---
    units[0]["sections"][2]["content"] += r"""

### Advanced Clar Sextet Topology in Higher Polyacenes & Graphene Nanoribbons

As fused benzenoid systems expand beyond three rings, the competition between delocalized benzenoid resonance and localized biradical character intensifies:

```
Higher Acenes (Tetracene, Pentacene, Hexacene):
Tetracene (4 Rings):   HOMO-LUMO Gap = 2.7 eV (Bright Orange, Photodimerizes)
Pentacene (5 Rings):   HOMO-LUMO Gap = 2.1 eV (Deep Violet, Singlet Fission Solar Cell Material)
Hexacene (6 Rings):    HOMO-LUMO Gap = 1.8 eV (Unstable, Open-Shell Singlet Biradicaloid)
```

1. **The Polyacene Narrowing Gap**:
   - In linear acenes, each additional fused ring adds only formal localized diene units while the total Clar sextet count remains **fixed at exactly one migrating sextet**:
     $$C(\text{Acene}_n, x) = 1 + n \, x$$
   - Consequently, the HOMO-LUMO gap closes monotonically:
     $$\Delta E_{\text{gap}}(n) \approx \frac{\pi \beta}{2(n + 1)} \tag{1.2a}$$
   - For heptacene ($n=7$) and nonacene ($n=9$), the frontier gap becomes so narrow ($<1.2\text{ eV}$) that thermal energy at room temperature can populate the triplet state, converting the molecule into a reactive **open-shell singlet biradical**.
2. **Angular Benzenoids: Perylene, Coronene & Kekulene**:
   - **Coronene ($\text{C}_{24}\text{H}_{12}$)**: A $D_{6h}$ symmetric disc containing 6 peripheral fused rings around a central hexagon. Clar's rule shows it possesses **three simultaneous, mutually disjoint Clar sextets** ($1 + 6x + 9x^2 + 3x^3$). Coronene is extraordinarily stable ($T_m = 438^\circ\text{C}$, $\text{RE} \approx 625\text{ kJ}\cdot\text{mol}^{-1}$).
   - **Kekulene ($\text{C}_{48}\text{H}_{24}$)**: A large macrocyclic polybenzenoid ring synthesized by Heinz Staab in 1978. Theoretical debate questioned whether it was an inner-and-outer $[18]\text{annulene} + [30]\text{annulene}$ super-aromatic ring or a collection of isolated Clar sextets. High-resolution $^{1}\text{H}$ NMR and bond lengths proved it exists strictly as **twelve localized benzenoid Clar sextets** connected by formal single bonds.
3. **Graphene Nanoribbons (GNRs)**:
   - Graphene sheets cut into narrow quasi-1D strips exhibit electronic properties governed strictly by peripheral edge geometry:
     - **Armchair GNRs (AGNRs)**: Possess semiconducting bandgaps determined by ribbon width.
     - **Zigzag GNRs (ZGNRs)**: Host spin-polarized localized edge states with ferromagnetically coupled electrons, forming the foundation of molecular spintronics."""

    # --- UNIT 2: Zimmerman-Traxler Transition States & Mukaiyama Aldol ---
    units[1]["sections"][6]["content"] += r"""

### The Zimmerman-Traxler Model & Stereoselective Aldol Additions

In 1957, Howard E. Zimmerman and Marjorie D. Traxler demonstrated that metal enolate additions to aldehydes proceed through rigid, chair-like **six-membered cyclic transition states**:

```
          Zimmerman-Traxler Chair Transition State:
                 R_ald (Equatorial)
                    \
                     C --------- O
                   /   \       /   \
                  H     \     /     M (Metal: Li, B, Ti)
                         \   /     /
                          \ /     /
                           C === C
                          /       \
                        R_enolate   H
```

The absolute stereochemical outcome of the newly formed $\beta$-hydroxy carbonyl stereocenters (syn vs anti) is governed by the geometry of the starting enolate:

1. **$(Z)$-Enolates Exclusively Yield Syn-Aldols**:
   - When a $(Z)$-enolate (where the enolate oxygen and the $\alpha$-alkyl group reside on the same side) enters the Zimmerman-Traxler chair:
   - The aldehyde substituent ($\text{R}_{\text{ald}}$) preferentially adopts the **equatorial orientation** to avoid 1,3-diaxial steric repulsions with the axial ligands on the metal.
   - Collapse of the chair transition state positions the $\alpha$-alkyl and $\beta$-hydroxyl groups *syn* to one another:
     $$(Z)\text{-Enolate} \xrightarrow{\text{Zimmerman-Traxler Chair}} \mathbf{syn\text{-}\beta\text{-hydroxy carbonyl}} \quad (>98\% \text{ syn}) \tag{2.9c}$$
2. **$(E)$-Enolates Yield Anti-Aldols**:
   - In an $(E)$-enolate, the $\alpha$-alkyl group projects pseudo-axial in the Zimmerman-Traxler chair.
   - The reaction proceeds to furnish the **$anti$-$\beta$-hydroxy carbonyl** product.
3. **Boron Enolates**: Because boron possesses shorter covalent bond distances ($r_{\text{B-O}} \approx 1.4\text{ \AA}$ vs $r_{\text{Li-O}} \approx 1.9\text{ \AA}$), the boron Zimmerman-Traxler chair is extraordinarily compact and rigid, delivering near-perfect stereoselection ($syn/anti > 99:1$).

### The Mukaiyama Aldol Reaction
Discovered by Teruaki Mukaiyama in 1973, this reaction couples a stable **silyl enol ether** ($\text{R}-\text{C}(\text{OTMS})=\text{CH}_2$) with an aldehyde in the presence of a Lewis acid ($\text{TiCl}_4, \text{BF}_3\cdot\text{OEt}_2$):
- Because silyl enol ethers are neutral and stable, self-condensation of the carbonyl partner is completely suppressed.
- The reaction proceeds via an **open-chain transition state** rather than a cyclic chair, allowing the stereochemical outcome to be tuned using chiral Lewis acid catalysts (e.g., chiral bis-oxazoline copper complexes, $\text{Cu(BOX)}^{2+}$)."""

    # --- UNIT 3: Thorpe-Ingold Effect & Carboxylic Catalysis ---
    units[2]["sections"][4]["content"] += r"""

### The Thorpe-Ingold Effect (Gem-Dimethyl Effect) in Ring Closures

When examining the rate of intramolecular cyclization of bifunctional carboxylic acids (such as hydroxy acids, amino acids, and dicarboxylic acids), replacing methylene hydrogens ($-\text{CH}_2-$) along the intervening carbon chain with alkyl substituents (e.g., $-\text{C}(\text{CH}_3)_2-$) produces an astonishing rate acceleration:

$$\text{Rate Acceleration Factor} \sim 10^2\text{ to }10^5\text{-fold} \tag{3.6a}$$

This phenomenon is designated the **Thorpe-Ingold effect** (Jocelyn Field Thorpe and Christopher Ingold, 1915):

```
       Thorpe-Ingold Conformational Compression:
       Unsubstituted:      H - C - H angle = 109.5°  ===> Chain carbons C - C - C angle = 109.5°
       Gem-Dimethyl:       Me - C - Me angle = 112.5° ===> Chain carbons C - C - C angle = 105°!
       [Compresses the ends of the chain closer together in three-dimensional space]
```

#### Physical Chemical Origins:
1. **Enthalpic Angle Compression**: Bulky methyl groups repel each other, widening the $\text{Me}-\text{C}-\text{Me}$ angle to $\sim 112.5^\circ$. To compensate, the internal $\text{C}-\text{C}-\text{C}$ chain angle is squeezed down to $\sim 105^\circ$. This brings the terminal reactive functional groups ($-\text{OH}$ and $-\text{COOH}$) closer in space.
2. **Entropic Rotamer Population**: In an unsubstituted hydrocarbon chain, the stable *anti* conformer places the chain ends far apart ($180^\circ$ dihedral). The reactive *gauche* conformation is higher in energy by $\sim 3.8\text{ kJ}\cdot\text{mol}^{-1}$ per bond.
   Introducing *gem*-dimethyl substituents creates unfavorable gauche methyl-chain interactions in the extended conformer. The gauche conformations become degenerate in energy with the anti conformer. Consequently, the equilibrium population of folded, cyclization-ready conformations increases from $<5\%$ to **$>75\%$**, eliminating the entropic activation penalty ($\Delta S^\ddagger$)."""

    # --- UNIT 4: Tetrahedral Lifetime & Cryo-TEM Micelle Dynamics ---
    units[3]["sections"][6]["content"] += r"""

### Ultrafast Lifetimes of Tetrahedral Intermediates & Surfactant Packing Parameters

#### 1. Nanosecond Lifetimes of Tetrahedral Intermediates
For decades, physical organic chemists debated whether the tetrahedral species in nucleophilic acyl substitution was a true **intermediate** (a local minimum on the potential energy surface) or merely a **transition state** (a saddle point).
- Using picosecond laser flash photolysis and high-resolution vibrational sum-frequency spectroscopy, John P. Richard and co-workers measured the actual physical lifetime ($\tau$) of tetrahedral intermediates in water:
  $$\tau_{\text{tetrahedral}} \approx 10^{-9}\text{ to }10^{-11}\text{ seconds} \quad (10\text{ ps to } 1\text{ ns}) \tag{4.13a}$$
- Because a molecular vibration takes approximately $10^{-13}\text{ seconds}$ ($100\text{ fs}$), a lifetime of $10^{-10}\text{ s}$ means the tetrahedral intermediate undergoes hundreds of bond vibrations and solvent collisions before collapsing, proving definitively that it is a **true chemical intermediate**.

#### 2. The Israelachvili Surfactant Packing Parameter ($P$)
The geometric morphology of colloidal self-assembled surfactant structures (spherical micelles, cylindrical wormlike micelles, flat bilayers, or reverse micelles) is predicted by Jacob Israelachvili's dimensionless **critical packing parameter** ($P$):

$$P = \frac{v}{a_0 \, l_c} \tag{4.13b}$$

where:
- $v$ is the hydrophobic tail volume ($\approx (27.4 + 26.9 n_{\text{C}}) \times 10^{-3}\text{ nm}^3$).
- $a_0$ is the effective cross-sectional area of the hydrophilic head group.
- $l_c$ is the maximum extended chain length of the hydrophobic tail ($\approx (0.154 + 0.1265 n_{\text{C}})\text{ nm}$).

| Packing Parameter Range | Predicted Colloidal Morphology | Physical Surfactant System |
| :--- | :--- | :--- |
| **$P < \frac{1}{3}$** | **Spherical Micelles** | Dilute ionic soaps (sodium palmitate, SDS) |
| **$\frac{1}{3} < P < \frac{1}{2}$** | **Cylindrical / Wormlike Micelles** | Cetyltrimethylammonium bromide (CTAB) + salt |
| **$\frac{1}{2} < P < 1$** | **Vesicles & Liposomes (Bilayers)** | Phospholipids (phosphatidylcholine, cell membranes) |
| **$P \approx 1$** | **Planar Lamellar Bilayer Sheets** | Saturated double-chain synthetic lipids |
| **$P > 1$** | **Reverse Inverted Micelles (W/O)** | Aerosol-OT (AOT) in organic non-polar solvents |"""

    # --- UNIT 5: Hammett Analysis of Diazonium Decomposition & Gomberg-Bachmann ---
    units[4]["sections"][4]["content"] += r"""

### Linear Free-Energy Analysis of Diazonium Heterolysis & The Gomberg-Bachmann Reaction

#### 1. First-Order Unimolecular Diazonium Heterolysis
In aqueous mineral acid at temperatures above $10^\circ\text{C}$, arenediazonium cations decompose via clean **first-order unimolecular kinetics** ($S_N1\text{-Ar}$):

$$\text{Ar}-\text{N}_2^+ \xrightarrow{k_1} [\text{Ar}^+] + \text{N}_2\uparrow \xrightarrow{\text{H}_2\text{O, fast}} \text{Ar-OH} + \text{H}^+ \tag{5.14a}$$

- **Kinetic Molecularity**: $\text{Rate} = k_1 [\text{ArN}_2^+]$, independent of the concentration or nature of added nucleophiles!
- **Phenyl Cation Intermediate**: The intermediate is a highly unstable **aryl cation** ($[\text{Ar}^+]$), where the positive charge resides in an unhybridized $sp^2$ orbital in the ring plane, orthogonal to the aromatic $\pi$ system.
- **Hammett $\sigma\text{–}\rho$ Correlation**: Substituents in the *meta* and *para* positions exhibit a dramatic effect on heterolysis rate:
  - Strong electron donors ($p\text{-OCH}_3, p\text{-NMe}_2$) donate electron density into the $\text{C}-\text{N}$ bond, slowing heterolysis and stabilizing the diazonium salt.
  - Electron-withdrawing groups ($m\text{-Cl}, p\text{-NO}_2$) accelerate radical reduction but destabilize the phenyl cation.

#### 2. The Gomberg-Bachmann Biaryl Coupling
When an arenediazonium salt is treated with an excess aromatic substrate (e.g., benzene) in the presence of aqueous sodium hydroxide ($40\%\, \text{NaOH}$):

$$\text{Ar-N}_2^+\text{Cl}^- + \text{C}_6\text{H}_6 + \text{NaOH} \longrightarrow \mathbf{\text{Ar}-\text{C}_6\text{H}_5} + \text{N}_2\uparrow + \text{NaCl} + \text{H}_2\text{O} \tag{5.14b}$$

- The basic conditions convert diazonium ion into **diazoanhydride** ($\text{Ar-N}=\text{N}-\text{O}-\text{N}=\text{N-Ar}$), which undergoes homolytic cleavage to generate **free aryl radicals ($\text{Ar}^\bullet$)**.
- The aryl radical attacks neutral benzene to form a phenylcyclohexadienyl radical, which is oxidized by diazonium species to yield the substituted **biaryl** product."""

    # --- UNIT 6: Asymmetric Catalysis by Knowles, Noyori & MacMillan ---
    units[5]["sections"][6]["content"] += r"""

### Pillars of Catalytic Asymmetric Synthesis: From Transition Metals to Organocatalysis

#### 1. Transition-Metal Asymmetric Hydrogenation (Knowles & Noyori, Nobel 2001)
- **William Knowles (Monsanto, 1970s)**: Developed the industrial synthesis of **L-DOPA** (frontline treatment for Parkinson's disease) using a chiral rhodium-DIPAMP catalyst, achieving $96\%$ enantiomeric excess in the asymmetric hydrogenation of an enamide precursor.
- **Ryoji Noyori (1980s)**: Developed **BINAP-ruthenium(II)** catalysts. The axial chirality of $(R)$- or $(S)$-BINAP creates a rigid, dissymmetric chiral pocket around ruthenium, hydrogenating functionalized ketones (such as $\beta$-keto esters) with $>99\%$ enantiomeric excess and turnover numbers exceeding $10^5$.

#### 2. Organocatalytic Asymmetric Activation (List & MacMillan, Nobel 2021)
- **Iminium Activation (David MacMillan)**: Chiral secondary amines (imidazolidinones, MacMillan catalysts) condense with $\alpha,\beta$-unsaturated aldehydes to form chiral **iminium cations**:
  - The iminium nitrogen lowers the LUMO energy of the enal by $>1.5\text{ eV}$, drastically accelerating Diels-Alder cycloadditions, Friedel-Crafts alkylations, and Michael additions at room temperature.
  - Bulky benzyl or *tert*-butyl groups on the imidazolidinone ring shield one face of the $\pi$ system, achieving enantiomeric excesses $>95\%$.
- **Enamine Activation (Benjamin List)**: Natural L-proline activates ketones via enamine intermediates for asymmetric intermolecular aldol, Mannich, and $\alpha$-amination reactions without requiring heavy metal cofactors."""

    # --- UNIT 7: Woodward-Hoffmann Correlation Diagrams & Danishefsky Diene ---
    units[6]["sections"][5]["content"] += r"""

### State and Orbital Correlation Diagrams & Danishefsky's Diene

#### 1. The Woodward-Hoffmann Orbital Correlation Diagram for $[4_s + 2_s]$ Cycloaddition
To rigorously prove why the thermal Diels-Alder reaction is symmetry-allowed while $[2_s + 2_s]$ is symmetry-forbidden, Woodward and Hoffmann constructed **orbital correlation diagrams**:
- The reacting system maintains a vertical plane of symmetry ($\sigma$) bisecting both the diene and dienophile throughout the reaction coordinate.
- The molecular orbitals of reactants and products are classified as Symmetric ($S$) or Antisymmetric ($A$) with respect to this symmetry plane:
  - Reactant orbitals: $\psi_1 (S), \psi_2 (A), \pi (S), \pi^* (A), \psi_3 (S), \psi_4 (A)$.
  - Product cyclohexene orbitals: $\sigma_1 (S), \sigma_2 (A), \pi (S), \pi^* (A), \sigma_1^* (S), \sigma_2^* (A)$.
- Every occupied bonding orbital of the reactants correlates smoothly with an **occupied bonding orbital of the ground-state product**:
  $$\psi_1 (S) \to \sigma_1 (S), \quad \psi_2 (A) \to \sigma_2 (A), \quad \pi (S) \to \pi (S) \tag{7.6c}$$
- No ground-state electron pair is forced into a high-energy antibonding orbital. The reaction is **thermally symmetry-allowed with zero orbital symmetry barrier**.
- In contrast, in $[2_s + 2_s]$ cycloaddition of two ethylenes, one occupied bonding orbital ($SA$) correlates directly with a high-energy unoccupied antibonding orbital ($\sigma_2^*, SA$). Crossing the barrier requires an immense investment of energy ($>200\text{ kJ}\cdot\text{mol}^{-1}$), rendering thermal $[2+2]$ cycloaddition **strictly symmetry-forbidden**.

#### 2. Danishefsky's Diene in Regioselective Synthesis
Synthesized by Samuel Danishefsky in 1974, **trans-1-methoxy-3-(trimethylsilyloxy)buta-1,3-diene** contains two powerful electron-donating groups:
- The methoxy group ($-\text{OMe}$) at C1 and the silyloxy group ($-\text{OTMS}$) at C3 massively elevate the HOMO energy and polarize the frontier orbital coefficients:
  $$|c_{\text{HOMO}}(\text{C4})|^2 \gg |c_{\text{HOMO}}(\text{C1})|^2$$
- In Diels-Alder cycloadditions with unsymmetrical dienophiles, Danishefsky's diene reacts with complete regiochemical control and enormous rate accelerations, furnishing substituted cyclohexenones after mild acid hydrolysis of the silyl enol ether."""

    # --- UNIT 8: SBDD, Molecular Docking & PROTACs ---
    units[7]["sections"][6]["content"] += r"""

### Structure-Based Drug Design (SBDD), Free Energy Perturbation & PROTACs

#### 1. Thermodynamics of Drug-Receptor Binding
The binding affinity of a small-molecule drug ($D$) to its macromolecular biological receptor ($R$) is governed by the equilibrium association constant ($K_a = 1/K_d$):

$$\Delta G^\circ_{\text{bind}} = -RT \ln K_a = \Delta H^\circ_{\text{bind}} - T\Delta S^\circ_{\text{bind}} \tag{8.7a}$$

- **Enthalpic Component ($\Delta H^\circ$)**: Favorable interactions include direct hydrogen bonds ($\sim -10\text{ to }-25\text{ kJ}\cdot\text{mol}^{-1}$ per bond), salt bridges ($\sim -20\text{ to }-40\text{ kJ}\cdot\text{mol}^{-1}$), and cation-$\pi$ interactions.
- **Entropic Component ($\Delta S^\circ$)**:
  - Unfavorable: Freezing conformational rotational degrees of freedom of the flexible drug ($-\Delta S_{\text{conf}} \approx +1.5\text{ to }+2.5\text{ kJ}\cdot\text{mol}^{-1}$ per rotatable bond).
  - Favorable: The **hydrophobic effect**—displacement of ordered water molecules from the lipophilic binding pocket into bulk solvent releases immense translational and rotational entropy ($T\Delta S_{\text{desolv}} > 0$).
- **Free Energy Perturbation (FEP)**: Modern computational chemistry uses molecular dynamics and thermodynamic integration to calculate the free energy difference $\Delta \Delta G_{\text{bind}}$ between drug analogues with sub-kilocalorie accuracy prior to laboratory chemical synthesis.

#### 2. Proteolysis Targeting Chimeras (PROTACs)
PROTACs represent a paradigm shift in pharmacology from traditional *inhibition* to **targeted protein degradation**:
- A PROTAC is a bifunctional heterobivalent molecule comprising:
  1. A small-molecule ligand that binds specifically to a pathogenic target protein (e.g., an oncogenic kinase).
  2. A flexible chemical linker ($\text{PEG}$ or polymethylene chain).
  3. A ligand that recruits an **E3 ubiquitin ligase** (e.g., VHL or Cereblon).
- The PROTAC brings the target protein into proximity with the E3 ligase, inducing polyubiquitination of target lysine residues.
- The 26S proteasome recognizes the ubiquitin chain and completely degrades the target protein. Because the PROTAC acts catalytically (dissociating after ubiquitination to destroy hundreds of target molecules), it overcomes drug resistance and "undruggable" binding sites."""

    # --- UNIT 9: Pauson-Khand, Multicomponent Biginelli & Allopurinol ---
    units[8]["sections"][6]["content"] += r"""

### Modern Heterocyclic Annulations & Purine Metabolic Inhibition

#### 1. The Pauson-Khand Reaction
The Pauson-Khand reaction (Peter Pauson and Ihsan Khand, 1973) is a cobalt-mediated $[2+2+1]$ cycloaddition coupling an alkyne, an alkene, and carbon monoxide:

$$\text{Alkyne} + \text{Alkene} + \text{CO} \xrightarrow{\text{Co}_2(\text{CO})_8, \Delta} \mathbf{\text{Cyclopentenone}} \tag{9.7a}$$

- Converts three separate acyclic building blocks into a functionalized cyclopentenone ring with up to three contiguous stereocenters.
- Intramolecular versions using enynes construct fused bicyclic ring systems (such as [3.3.0] and [4.3.0] cores) found in sesquiterpenes.

#### 2. The Biginelli Multicomponent Dihydropyrimidine Synthesis
Pietro Biginelli (1893) discovered the acid-catalyzed condensation of an aromatic aldehyde, a $\beta$-keto ester (such as ethyl acetoacetate), and urea to yield **3,4-dihydropyrimidin-2(1H)-ones (DHPMs)**:

$$\text{ArCHO} + \text{CH}_3\text{COCH}_2\text{COOEt} + \text{H}_2\text{N-CO-NH}_2 \xrightarrow{\text{cat. HCl or FeCl}_3, \text{EtOH, reflux}} \mathbf{\text{DHPM}} + 2\,\text{H}_2\text{O} \tag{9.7b}$$

DHPMs exhibit diverse biological activities, including kinesin Eg5 motor protein inhibition (Monastrol, targeted mitotic spindle cancer therapeutics) and $\alpha_{1A}$-adrenergic receptor antagonism.

#### 3. Allopurinol: Suicide Inhibition of Purine Catabolism
In human purine metabolism:
- Hypoxanthine is oxidized to xanthine, and xanthine is oxidized to **uric acid** by the molybdenum-containing enzyme **xanthine oxidase**.
- Hyperuricemia causes precipitation of insoluble monosodium urate crystals in synovial joints, producing excruciating inflammatory **gout**.
- **Allopurinol** (1H-pyrazolo[3,4-d]pyrimidin-4-ol) is an isomer of hypoxanthine.
- Xanthine oxidase oxidizes allopurinol to **oxypurinol** (alloxanthine). Oxypurinol coordinates tightly to the reduced molybdenum($\text{IV}$) ion at the active site, acting as a **mechanism-based suicide inhibitor** that permanently inactivates the enzyme ($K_i \approx 5 \times 10^{-10}\text{ M}$), slashing uric acid levels and curing gout."""

    print("Monographs successfully injected across all 9 units!")
