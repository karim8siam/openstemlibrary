# expand_org1_part4.py
# Deep academic enrichment for Unit 7 and Unit 8 of Organic Chemistry I
# Alcohols, Phenols, Ethers, Epoxides, Sulfides, and Fundamental Heterocycles

def expand_unit7(u7):
    # Deepen Section 2: Conversion of Alcohols to Halides & SNi Mechanism
    u7["sections"][1]["content"] += r"""

### The $S_N\text{i}$ Mechanism with Thionyl Chloride: Retention vs Inversion

The reaction of alcohols with thionyl chloride ($\text{SOCl}_2$) exhibits remarkable stereochemical divergence that depends critically on the solvent:

#### 1. Reaction in Dioxane or Ether (Retention via $S_N\text{i}$):
$$\text{R}-\text{OH} + \text{SOCl}_2 \longrightarrow \mathbf{\text{R}-\text{O}-\text{SOCl}} \text{ (Chlorosulfite Ester)} + \text{HCl} \tag{7.4a}$$
- The chlorosulfite ester ionizes internally within the solvent cage to form an **intimate ion pair**:
  $$\text{R}-\text{O}-\text{SOCl} \longrightarrow [\text{R}^+ \; ^-\text{O}-\text{SOCl}] \tag{7.4b}$$
- The chlorosulfite anion spontaneously collapses, expelling $\text{SO}_2$ gas and delivering chloride directly to the **front face** of the carbocation from which the leaving group departed:
  $$[\text{R}^+ \; ^-\text{O}-\text{SOCl}] \longrightarrow \left[ \begin{matrix} \text{R}^+ \\ \vdots \\ \text{Cl}-\text{SO}_2^- \end{matrix} \right] \longrightarrow \mathbf{\text{R}-\text{Cl (Retention of Configuration)}} + \mathbf{\text{SO}_2\uparrow} \tag{7.4c}$$
- This internal nucleophilic substitution ($S_N\text{i}$, Substitution Nucleophilic internal) proceeds with **clean retention of stereochemical configuration**!

#### 2. Reaction in Pyridine (Inversion via $S_N2$):
When pyridine is added to the reaction mixture:
- Pyridine acts as a nucleophilic catalyst and acid scavenger, reacting with the chlorosulfite ester to form a pyridinium chlorosulfite salt:
  $$\text{R}-\text{O}-\text{SOCl} + \text{Py} \longrightarrow [\text{R}-\text{O}-\text{SO}-\text{Py}]^+ \, \text{Cl}^- \tag{7.4d}$$
- The liberated free chloride ion ($\text{Cl}^-$) attacks the substrate from the **backside** in a classic $S_N2$ displacement, expelling $\text{SO}_2$ and pyridine:
  $$\text{Cl}^- + \text{R}-\text{O}-\text{SO}-\text{Py}^+ \longrightarrow \mathbf{\text{R}-\text{Cl (Inversion of Configuration)}} + \text{SO}_2 + \text{Py} \tag{7.4e}$$
By simply choosing between dioxane and pyridine, synthetic chemists achieve complete control over retention versus inversion!"""

    # Deepen Section 3: Oxidation of Alcohols & Swern Mechanism
    u7["sections"][2]["content"] += r"""

### Detailed Multistep Swern Oxidation Mechanism

Developed by Daniel Swern in 1978, the Swern oxidation cleanly converts primary alcohols to aldehydes and secondary alcohols to ketones under mild conditions without heavy metal toxicity:

```
    O   O
    ||  ||               -60 deg C
    C - C   +  Me2S=O  ------------> [ Me2S+-Cl ] Cl-  +  CO  +  CO2
   /     \                            (Activated Complex)
  Cl     Cl
(Oxalyl Chloride)
         |
         | + R2CH-OH
         v
    [ Me2S+-O-CHR2 ] Cl-  (Alkoxysulfonium Intermediate)
         |
         | + Et3N (Base)
         v
    [ H2C=S+(Me)-O-CHR2 <-> -CH2-S+(Me)-O-CHR2 ] (Sulfur Ylide)
         |
         | Cyclic 5-Membered Intramolecular Proton Transfer
         v
    R2C=O (Carbonyl Product)  +  Me2S (Dimethyl Sulfide)  +  Et3NH+ Cl-
```

#### Line-by-Line Reaction Steps:
1. **Activation of DMSO**: At $-60^\circ\text{C}$ in dichloromethane, dimethyl sulfoxide ($\text{Me}_2\text{SO}$) attacks oxalyl chloride ($(\text{COCl})_2$). Spontaneous fragmentation expels carbon monoxide ($\text{CO}$), carbon dioxide ($\text{CO}_2$), and generates the highly reactive **chlorodimethylsulfonium cation** ($[\text{Me}_2\text{S}^+-\text{Cl}]\text{Cl}^-$).
2. **Alcohol Coordination**: Addition of the alcohol displaces chloride from sulfur to form the **alkoxysulfonium intermediate** ($[\text{Me}_2\text{S}^+-\text{O}-\text{CH}\text{R}_2]$).
3. **Ylide Formation**: Addition of triethylamine ($\text{Et}_3\text{N}$) deprotonates one of the methyl groups attached to sulfur, forming a neutral **sulfur ylide** ($^-\text{CH}_2-\text{S}^+(\text{Me})-\text{O}-\text{CH}\text{R}_2$).
4. **Intramolecular Fragmentation**: The ylide undergoes an irreversible, cyclic five-membered intramolecular elimination: the carbanion abstracts the $\alpha$-proton from the alcohol carbon, cleaving the $\text{S}-\text{O}$ bond to generate the desired **aldehyde or ketone**, volatile **dimethyl sulfide ($\text{Me}_2\text{S}$)**, and triethylammonium chloride!"""

    # Deepen Section 4: Pinacol-Pinacolone & Periodate Cleavages
    u7["sections"][3]["content"] += r"""

### Migratory Aptitude & Thermodynamic Driving Force of the Pinacol Rearrangement

When a vicinal 1,2-diol (glycol) is treated with strong mineral or Lewis acid, it undergoes dehydration accompanied by 1,2-rearrangement to yield an aldehyde or ketone:

$$\text{R}_2\text{C(OH)}-\text{C(OH)}\text{R}_2 \xrightarrow{\text{H}^+} \mathbf{\text{R}-\text{CO}-\text{CR}_3} + \text{H}_2\text{O} \tag{7.10a}$$

#### Thermodynamic Driving Force: Oxocarbenium Resonance Stabilization:
- In the starting open carbocation intermediate, the positive charge is localized on a trivalent carbon:
  $$\text{R}_2\text{C(OH)}-\stackrel{\oplus}{\text{C}}\text{R}_2 \quad (6 \text{ valence electrons on carbocation})$$
- Following 1,2-migration of an R group, the positive charge resides on the carbon atom directly bonded to the hydroxyl oxygen:
  $$\text{R}_2\stackrel{\oplus}{\text{C}}-\text{O}-\text{H} \longleftrightarrow \mathbf{\text{R}_2\text{C}=\stackrel{\oplus}{\text{O}}-\text{H}} \quad (8 \text{ valence electrons on ALL atoms!}) \tag{7.10b}$$
- The resulting **oxocarbenium ion** resonance contributor satisfies the octet rule for every atom, providing over **$80\text{ kJ/mol}$ of thermodynamic stabilization energy** that drives the rearrangement irreversibly forward!

#### Quantitative Migratory Aptitudes in Unsymmetrical Pinacols:
When different groups can migrate, the migratory aptitude reflects their ability to stabilize positive charge in the bridged phenonium or three-center transition state:
$$\mathbf{p\text{-Anisyl } (500) > p\text{-Tolyl } (15) > \text{Phenyl } (1.0) \gg \text{tert-Butyl} > \text{Isopropyl} > \text{Ethyl} > \text{Methyl } (0.001)} \tag{7.10c}$$
Electron-rich aromatic rings migrate with extraordinary preference because resonance donation from the methoxy group stabilizes the bridged phenonium intermediate."""

    # Deepen Section 5: Phenol Name Reactions
    u7["sections"][4]["content"] += r"""

### Mechanistic Deep Dive: Kolbe-Schmitt Carboxylation & Reimer-Tiemann Formylation

Phenols possess extraordinary nucleophilicity due to the strong resonance donation of the phenoxide oxyanion, enabling electrophilic attack by weak electrophiles:

#### 1. The Kolbe-Schmitt Carboxylation (Aspirin Synthesis Core):
Industrial synthesis of salicylic acid involves heating sodium phenoxide with carbon dioxide under pressure:
$$\text{C}_6\text{H}_5\text{O}^-\text{Na}^+ + \text{CO}_2 \xrightarrow{125^\circ\text{C}, \; 100\text{ atm}} \mathbf{\text{o-HOC}_6\text{H}_4\text{COO}^-\text{Na}^+} \tag{7.13a}$$
- **Sodium Chelation Control**: The sodium cation forms a cyclic, planar six-membered coordination complex bridging the phenoxide oxygen and carbon dioxide:
  $$\left[ \begin{matrix} \text{O}^- & \cdots & \text{Na}^+ \\ \vert & & \vdots \\ \text{C}_{\text{ortho}} & \cdots & \text{C}(=\text{O})_2 \end{matrix} \right]^\ddagger \tag{7.13b}$$
- This chelate holds $\text{CO}_2$ rigidly over the **ortho position**, yielding exclusively ortho-salicylate ($>90\%$). In contrast, substituting potassium phenoxide ($\text{K}^+$, which has a larger ionic radius and weaker chelation) shifts the product ratio predominantly to the para-hydroxybenzoate!

#### 2. The Reimer-Tiemann Reaction:
Reaction of phenol with chloroform and aqueous sodium hydroxide yields salicylaldehyde:
$$\text{C}_6\text{H}_5\text{OH} + \text{CHCl}_3 + 3\,\text{NaOH} \xrightarrow{60^\circ\text{C}} \mathbf{\text{o-HOC}_6\text{H}_4\text{CHO}} + 3\,\text{NaCl} + 2\,\text{H}_2\text{O} \tag{7.13c}$$
- **Carbene Generation**: Hydroxide abstracts the acidic proton of chloroform ($\alpha$-elimination) to generate the neutral, highly electrophilic **dichlorocarbene**:
  $$\text{CHCl}_3 + \text{OH}^- \rightleftharpoons ^-:\text{CCl}_3 + \text{H}_2\text{O} \xrightarrow{-\text{Cl}^-} \mathbf{:\text{CCl}_2} \tag{7.13d}$$
- **Electrophilic Attack**: Phenoxide attacks $:\text{CCl}_2$ at the ortho position to yield a non-aromatic cyclohexadienone anion bearing a $-\text{CHCl}_2$ moiety.
- **Tautomerization & Hydrolysis**: Deprotonation restores aromaticity. The dichloromethyl group ($-\text{CHCl}_2$) hydrolyzes via gem-diol intermediate to the aldehyde ($-\text{CHO}$)."""

    # Deepen Section 7: Epoxide Ring Opening Regiochemistry & Crown Ethers
    u7["sections"][6]["content"] += r"""

### Stereoelectronic Regiochemistry: Epoxide Ring-Opening Regimes

The regiochemical outcome of unsymmetrical epoxide ring-opening is completely governed by the reaction regime:

#### 1. Basic / Nucleophilic Regime ($S_N2$ Regiocontrol):
$$\text{R}-\text{CH}-\!\!\!\!\!\!^{\text{O}}\backslash\text{CH}_2 + \text{Nu}^- \longrightarrow \mathbf{\text{R}-\text{CH(OH)}-\text{CH}_2-\text{Nu}} \tag{7.17a}$$
- In basic media (e.g., $\text{NaOCH}_3, \text{NaN}_3, \text{LiAlH}_4, \text{RMgX}$), the neutral epoxide is attacked directly by the strong nucleophile.
- **Steric Dominance**: Backside attack proceeds along the Bürgi-Dunitz trajectory at the **less sterically hindered carbon** (C1 in 1,2-epoxypropane).
- **Stereochemistry**: Complete inversion of configuration at the attacked carbon.

#### 2. Acidic Regime ($S_N1$-like Regiocontrol with $S_N2$ Stereospecificity):
$$\text{R}-\text{CH}-\!\!\!\!\!\!^{\text{O}}\backslash\text{CH}_2 + \text{H}^+ \rightleftharpoons [\text{R}-\text{CH}-\!\!\!\!\!\!^{\stackrel{\oplus}{\text{O}}\text{H}}\backslash\text{CH}_2] \xrightarrow{+\text{H}_2\text{O}} \mathbf{\text{R}-\text{CH(OH)}-\text{CH}_2\text{OH}} \tag{7.17b}$$
- Protonation creates an oxonium ion with full positive formal charge on oxygen.
- **Electronic Charge Distribution**: The more substituted carbon (C2) can significantly better stabilize the developing positive partial charge ($\delta^+$) via hyperconjugation from the R group.
- Consequently, the $\text{C}2-\text{O}$ bond is much longer and weaker than the $\text{C}1-\text{O}$ bond:
  $$r(\text{C}2-\text{O}) \approx 1.58\text{ \AA} \quad \gg \quad r(\text{C}1-\text{O}) \approx 1.45\text{ \AA} \tag{7.17c}$$
- The weak nucleophile attacks almost exclusively at the **more substituted, more positive C2 carbon**, while still maintaining **anti-stereospecific backside attack**!

#### 3. Supramolecular Host-Guest Chelation of Crown Ethers:
Synthesized by Charles Pedersen in 1967, cyclic polyethers selectively encapsulate alkali metal cations within their central polar cavity:
- **12-Crown-4**: Cavity diameter $1.2 - 1.5\text{ \AA}$, binds **$\text{Li}^+$** (ionic diameter $1.52\text{ \AA}$).
- **15-Crown-5**: Cavity diameter $1.7 - 2.2\text{ \AA}$, binds **$\text{Na}^+$** (ionic diameter $2.04\text{ \AA}$).
- **18-Crown-6**: Cavity diameter $2.6 - 3.2\text{ \AA}$, binds **$\text{K}^+$** (ionic diameter $2.76\text{ \AA}$).
- **Phase-Transfer & Anion Activation**: When 18-crown-6 encapsulates $\text{K}^+$ in benzene, the accompanying anion ($\text{MnO}_4^-$ or $\text{F}^-$) is stripped of its solvation shell, creating a "naked" anion with extreme nucleophilic reactivity ("Purple Benzene")!"""
    return u7


def expand_unit8(u8):
    # Deepen Section 1: Heterocycle Diversity & Aromaticity
    u8["sections"][0]["content"] += r"""

### Hantzsch-Widman Systematic Heterocyclic Nomenclature & MO Stability

Monocyclic heterocycles are named systematically using the IUPAC Hantzsch-Widman system by combining prefixes indicating heteroatom type with stems indicating ring size and saturation:

#### 1. Prefixes (Order of Precedence):
$$\text{Oxa- (Oxygen)} > \text{Thia- (Sulfur)} > \text{Selena- (Selenium)} > \text{Aza- (Nitrogen)} > \text{Phospha- (Phosphorus)} \tag{8.1a}$$

#### 2. Ring-Size Stems:
- 3-membered: Unsaturated `-irene`, Saturated `-irane` (e.g., Oxirane)
- 4-membered: Unsaturated `-ete`, Saturated `-etane` (e.g., Oxetane, Azetidine)
- 5-membered: Unsaturated `-ole`, Saturated `-olane` (e.g., Pyrrole, Oxolane/THF)
- 6-membered: Unsaturated `-ine`, Saturated `-inane` (e.g., Pyridine, Piperidine)
- 7-membered: Unsaturated `-epine`, Saturated `-epane` (e.g., Azepine)

#### 3. Quantitative Resonance Energy Comparison:
The resonance stabilization energy of heterocycles reflects the electronegativity and orbital size mismatch of the heteroatom:

$$\text{Benzene } (152\text{ kJ/mol}) > \text{Thiophene } (121\text{ kJ/mol}) > \text{Pyrrole } (88\text{ kJ/mol}) > \text{Furan } (67\text{ kJ/mol}) \tag{8.1b}$$
- **Thiophene**: Has the highest resonance energy among five-membered rings because the sulfur atom has lower electronegativity ($\chi = 2.58$) and polarizable $3p$ orbitals that delocalize electron density effectively into the ring.
- **Pyrrole**: Moderate resonance energy ($88\text{ kJ/mol}$). Nitrogen's lone pair is fully integrated into the aromatic sextet.
- **Furan**: Lowest resonance energy ($67\text{ kJ/mol}$). Oxygen's extreme electronegativity ($\chi = 3.44$) causes it to hold its lone pairs tightly, reducing delocalization and giving furan diene-like reactivity."""

    # Deepen Section 2: Pyrrole vs Pyridine Basicity
    u8["sections"][1]["content"] += r"""

### Molecular Orbital Analysis of Heterocyclic Basicity: Pyrrole vs Pyridine

A profound contrast in heterocyclic chemistry is the difference in Brønsted-Lowry basicity between pyrrole and pyridine:

$$\text{Pyridine} \quad (pK_a \text{ of conjugate acid} = 5.25) \quad \gg \quad \text{Pyrrole} \quad (pK_a \text{ of conjugate acid} = -3.8) \tag{8.3a}$$
This difference of **nine orders of magnitude ($10^9$)** in proton affinity is explained by orbital orientation:

```
      PYRIDINE (Basic)                        PYRROLE (Non-Basic)
         
            N                                         H - N
          /   \                                      /     \
         |  o  |                                    |   o   |
          \   /                                      \     /
            
   * Lone pair in sp2 hybrid                * Lone pair in unhybridized 2pz
   * In plane of ring, orthogonal to pi      * PART OF THE 6-pi AROMATIC SEXTET!
   * Protonation PRESERVES aromaticity!      * Protonation DESTROYS aromaticity!
```

#### 1. Pyridine:
- The nitrogen atom is $sp^2$ hybridized.
- Its unhybridized $2p_z$ orbital contributes **one electron** to the six-electron aromatic $\pi$ system.
- The lone pair occupies an **$sp^2$ hybrid orbital that lies entirely in the plane of the ring**, completely orthogonal ($90^\circ$) to the $\pi$ system!
- **Protonation**: Addition of a proton to the $sp^2$ lone pair forms the pyridinium cation ($[\text{C}_5\text{H}_5\text{NH}]^+$), leaving the aromatic $\pi$ system completely intact ($6\pi$ electrons, aromatic)!

#### 2. Pyrrole:
- The nitrogen atom is $sp^2$ hybridized.
- Its unhybridized $2p_z$ orbital holds **both electrons of the lone pair**, which are required to complete the $(4n+2) = 6\pi$ aromatic sextet!
- **Protonation**:
  - Protonating the nitrogen atom forces the nitrogen into an $sp^3$ tetrahedral geometry.
  - This removes the lone pair from the $\pi$ system, **completely destroying the aromatic sextet** and sacrificing $88\text{ kJ/mol}$ of resonance stabilization!
  - Therefore, pyrrole is non-basic ($pK_a = -3.8$). In strong acids, protonation occurs instead at **C2** to form a non-aromatic cation that rapidly polymerizes to an insoluble red polymer ("pyrrole red")."""

    # Deepen Section 3: EAS Regiochemistry in Five-Membered Heterocycles
    u8["sections"][2]["content"] += r"""

### Wheland Intermediate Canonical Forms: C2 vs C3 EAS Regiochemistry

When electrophilic aromatic substitution occurs on pyrrole, furan, or thiophene, attack occurs with overwhelming selectivity at the **C2 position ($\alpha$-position)** over the C3 position ($\beta$-position):

#### 1. Electrophilic Attack at C2 ($\alpha$-attack):
$$\text{Heterocycle} + \text{E}^+ \longrightarrow [\text{C2-Wheland Intermediate}]^\ddagger$$
Generating the Wheland intermediate at C2 yields **THREE canonical resonance structures**:
1. Carbocation at C3: $[ \text{X}-\text{CH}(\text{E})-\stackrel{\oplus}{\text{C}}\text{H}-\text{CH}=\text{CH} ]$
2. Carbocation at C5: $[ \text{X}-\text{CH}(\text{E})-\text{CH}=\text{CH}-\stackrel{\oplus}{\text{C}}\text{H} ]$
3. **Octet-Complete Imonium/Oxonium/Sulfonium form**: $[ \stackrel{\oplus}{\text{X}}=\text{CH}-\text{CH}=\text{CH}-\text{CH}(\text{E}) ]$ (Every heavy atom has an octet!)

#### 2. Electrophilic Attack at C3 ($\beta$-attack):
$$\text{Heterocycle} + \text{E}^+ \longrightarrow [\text{C3-Wheland Intermediate}]^\ddagger$$
Generating the Wheland intermediate at C3 yields **ONLY TWO canonical resonance structures**:
1. Carbocation at C2: $[ \stackrel{\oplus}{\text{C}}\text{H}-\text{CH}(\text{E})-\text{CH}=\text{CH}-\text{X} ]$
2. Octet-Complete Onium form: $[ \stackrel{\oplus}{\text{X}}=\text{CH}-\text{CH}(\text{E})-\text{CH}=\text{CH} ]$

Because attack at C2 produces **three resonance contributors** compared to only **two contributors** for attack at C3, the transition state for C2 substitution is lower in activation free energy by $\Delta \Delta G^\ddagger \approx 15-25\text{ kJ/mol}$, resulting in **$>99\%$ regioselectivity for the C2 isomer**!"""

    # Deepen Section 5: Pyridine EAS Deactivation & N-Oxide Strategy
    u8["sections"][4]["content"] += r"""

### The Pyridine N-Oxide Umpolung Activation Strategy

Pyridine is extraordinarily resistant to electrophilic aromatic substitution because the electronegative ring nitrogen withdraws electron density, and strong acidic electrophiles protonate nitrogen to form the positively charged pyridinium ion ($[\text{PyH}]^+$), which repels incoming electrophiles.

In 1940, Eiji Ochiai discovered an ingenious strategy to circumvent this extreme deactivation: **Pyridine $N$-Oxide Activation**:

```
           Pyridine
              |
              | mCPBA or H2O2 / AcOH  (Oxidation)
              v
       Pyridine N-Oxide  [ +N - O- <-> N = O ]
              |
              | HNO3 / H2SO4 at 90 deg C  (FACILE EAS AT C4!)
              v
       4-Nitropyridine N-Oxide
              |
              | PCl3 or PPh3  (Deoxygenation)
              v
       4-Nitropyridine  (Pure Product, >80% Overall Yield!)
```

#### Resonance Origin of Activation:
In pyridine $N$-oxide, the formal negative charge on oxygen donates electron density back into the ring via resonance:
$$[:\stackrel{-}{\text{O}}-\stackrel{+}{\text{N}}=\text{C}-\text{C}=\text{C} \longleftrightarrow \text{O}=\stackrel{+}{\text{N}}-\text{C}=\text{C}-\stackrel{-}{\text{C}}:] \tag{8.9a}$$
- This resonance donation places negative charge density specifically at the **C2 and C4 positions**, completely overcoming inductive deactivation!
- Electrophiles attack smoothly at the **C4 position** under mild conditions ($90^\circ\text{C}$ vs $300^\circ\text{C}$ for unsubstituted pyridine).
- Reduction with phosphorus trichloride ($\text{PCl}_3$) removes the oxygen atom as phosphoryl chloride ($\text{POCl}_3$), affording the previously inaccessible 4-substituted pyridine in high yield!"""
    return u8
