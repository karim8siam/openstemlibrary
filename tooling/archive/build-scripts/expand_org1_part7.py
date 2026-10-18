# expand_org1_part7.py
# Deep academic enrichment: Subsections §3.9, §4.9, §5.9
# and Graduate/Honors Solved Problems for Units 3, 4, and 5.

def expand_units_3_4_5(units):
    u1, u2, u3, u4, u5, u6, u7, u8 = units

    # ==========================================
    # UNIT 3: Advanced Section & Honors Problems
    # ==========================================
    u3["sections"].append({
        "id": "sec3_9",
        "secNumber": "3.9",
        "title": "§3.9 Industrial Petrochemical Polyolefins & Advanced Polymer Characterization",
        "heading": "Industrial Petrochemical Polyolefins & Advanced Polymer Characterization",
        "simulations": ["sim_chem_alkene_addition_stereochemistry"],
        "content": r"""### High-Density vs Low-Density Polyethylene: Radical vs Ziegler-Natta Regimes

Polyethylene ($\text{PE}$) is the largest volume synthetic polymer globally, manufactured in two fundamentally distinct structural architectures:

```
   1. LOW-DENSITY POLYETHYLENE (LDPE):
      * Process: Free-radical, 1000 - 3000 atm, 200 - 300 deg C
      * Mechanism: Intramolecular 1,5-hydrogen shift ("Backbiting")
      * Structure: Highly branched (butyl and ethyl short-chain branches)
      * Properties: Low crystallinity (40 - 55%), Tm = 105 - 115 deg C, density = 0.91 - 0.93 g/cm3

   2. HIGH-DENSITY POLYETHYLENE (HDPE):
      * Process: Ziegler-Natta or Metallocene, 1 - 50 atm, 70 - 100 deg C
      * Mechanism: Linear Cossee-Arlman migratory insertion
      * Structure: Strictly linear, virtually unbranched polymer chains
      * Properties: High crystallinity (70 - 85%), Tm = 130 - 137 deg C, density = 0.94 - 0.97 g/cm3
```

#### 1. The "Backbiting" Intramolecular Hydrogen Shift in LDPE:
During high-pressure free-radical polymerization, the propagating terminal secondary radical undergoes an intramolecular 1,5-hydrogen atom abstraction through a cyclic six-membered transition state:
$$\sim\text{CH}_2-\text{CH}_2-\text{CH}_2-\text{CH}_2-\dot{\text{C}}\text{H}_2 \xrightarrow{\text{1,5-shift}} \sim\text{CH}_2-\dot{\text{C}}\text{H}-\text{CH}_2-\text{CH}_2-\text{CH}_3 \tag{3.19a}$$
- The newly generated internal secondary radical continues chain propagation by adding ethylene monomers, generating a **butyl ($-\text{C}_4\text{H}_9$) branch**.
- These branches disrupt regular chain folding into crystal lamellae, resulting in flexible, low-density material suitable for films and plastic bags.

#### 2. Advanced Polymer Characterization: GPC & DSC:
1. **Gel Permeation Chromatography (GPC / SEC)**: Measures molecular weight distributions:
   - Number-average molecular weight: $\bar{M}_n = \frac{\sum N_i M_i}{\sum N_i}$
   - Weight-average molecular weight: $\bar{M}_w = \frac{\sum N_i M_i^2}{\sum N_i M_i}$
   - Polydispersity Index: $\text{PDI} = \frac{\bar{M}_w}{\bar{M}_n}$ (Metallocenes give narrow $\text{PDI} \approx 2.0$; classical heterogeneous Ziegler-Natta give broad $\text{PDI} \approx 4 - 8$).
2. **Differential Scanning Calorimetry (DSC)**: Measures the glass transition temperature ($T_g$) and crystalline melting peak ($T_m$). The percentage crystallinity $X_c$ is quantified by integrating the melting endotherm:
   $$X_c = \frac{\Delta H_m}{\Delta H_m^\circ} \times 100\% \tag{3.19b}$$
   where $\Delta H_m^\circ = 293\text{ J/g}$ for $100\%$ crystalline polyethylene."""
    })

    u3["problems"].extend([
        {
            "id": "p3_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Stereochemical Proof & Diastereomer Derivation in Prilezhaev Epoxidation vs Bromination",
            "question": "(2E,4E)-Hexa-2,4-diene reacts with one equivalent of mCPBA to form mono-epoxide A. Epoxide A is subsequently treated with aqueous perchloric acid (H3O+) to undergo stereospecific anti-ring opening yielding diol B. Separately, (2E,4E)-hexa-2,4-diene reacts with one equivalent of bromine (Br2) in CCl4 to form dibromo adduct C. (1) Deduce the exact absolute and relative stereochemistry of Epoxide A. (2) Track the backside oxonium ion ring-opening step to determine the stereochemical configuration of Diol B (meso vs racemic). (3) Deduce the structure of dibromide C and explain why 1,4-addition competes with 1,2-addition in the halogenation of conjugated dienes.",
            "solution": r"""#### Part 1: Stereochemistry of Mono-Epoxide A
1. **Concerted Butterfly Transition State**:
   - The Prilezhaev epoxidation with $m$CPBA is a stereospecific concerted pericyclic process.
   - The geometry of the alkene is strictly retained in the oxirane ring: substituents that are *trans* in the starting alkene remain *trans* across the epoxide ring.
2. In $(2E,4E)$-hexa-2,4-diene, both double bonds possess $(E)$-geometry.
   - Reaction at one double bond delivers oxygen to either the top or bottom face with equal probability, forming a racemic pair of enantiomeric **trans-epoxides**:
     $$\mathbf{(2R, 3R)\text{-2-methyl-3-((E)-prop-1-en-1-yl)oxirane}} \quad \text{and} \quad \mathbf{(2S, 3S)\text{-enantiomer}} \tag{1}$$
   - The unreacted double bond retains its intact $(E)$-stereochemistry.

#### Part 2: Acid-Catalyzed Ring Opening to Diol B
1. **Oxonium Ion Formation & Nucleophilic Backside Attack**:
   - Protonation by $\text{H}_3\text{O}^+$ generates a protonated oxonium ion.
   - Water attacks the more substituted/more stabilized carbon center (C3, which is allylic and can stabilize partial carbocation character) via **strict backside ($S_N2$-like) attack**.
2. **Inversion at Attacked Center**:
   - Backside attack at C3 inverts its configuration ($R \to S$ or $S \to R$).
   - The C2 center is untouched, retaining its configuration.
3. **Stereochemical Outcome of Diol B**:
   - Inversion at one stereocenter while maintaining the other converts the $(2R, 3R)$ enantiomer into the $(2R, 3S)$ diastereomer.
   - Because the two ends of the molecule are structurally distinct ($-\text{CH}_3$ at C1 vs $-\text{CH}=\text{CH}-\text{CH}_3$ at C4), Diol B is **chiral** and is isolated as an **optically inactive racemic mixture of $(2R, 3S)$ and $(2S, 3R)$ diastereomers**.

#### Part 3: Halogenation & 1,2- vs 1,4-Addition Competition
1. **Bromination of Conjugated Dienes**:
   - Electrophilic addition of $\text{Br}_2$ to $(2E,4E)$-hexa-2,4-diene forms an allylic bromonium / allylic carbocation hybrid intermediate:
     $$\left[ \text{CH}_3-\text{CHBr}-\stackrel{\oplus}{\text{C}}\text{H}-\text{CH}=\text{CH}-\text{CH}_3 \longleftrightarrow \text{CH}_3-\text{CHBr}-\text{CH}=\text{CH}-\stackrel{\oplus}{\text{C}}\text{H}-\text{CH}_3 \right] \tag{2}$$
2. **1,2-Adduct (Kinetic Control at Low $T$)**:
   - Attack of $\text{Br}^-$ at C3 gives the 1,2-addition product: **4,5-dibromohex-2-ene**.
   - Favored at $-80^\circ\text{C}$ due to proximity of the departing bromide ion to C3 (the proximity effect).
3. **1,4-Adduct (Thermodynamic Control at High $T$)**:
   - Attack of $\text{Br}^-$ at C5 gives the 1,4-addition product: **2,5-dibromohex-3-ene**.
   - Favored at $+40^\circ\text{C}$ because the internal double bond is disubstituted, trans, and thermodynamically more stable by $\sim 15\text{ kJ/mol}$!"""
        },
        {
            "id": "p3_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Cossee-Arlman Insertion Kinetics & Tacticity Probability in Metallocene Catalysis",
            "question": "In the coordination polymerization of propene by a C2-symmetric ansa-zirconocene catalyst rac-[Me2Si(Ind)2]ZrCl2 / MAO, polymer chain growth proceeds via stereospecific enantiomorphic site control. Let k_i be the rate constant for isotactic insertion (correct face) and k_s be the rate constant for syndiotactic insertion (mis-insertion). (1) If the catalyst achieves 98.5% isotactic pentad content ([mmmm] = 0.985) at 20°C, calculate the enantioselectivity ratio alpha = k_i / (k_i + k_s). (2) Calculate the activation free energy difference Delta Delta G^(++) between the two enantiotopic faces of propene. (3) What occurs upon warming to 80°C if Delta Delta H^(++) = 14.5 kJ/mol and Delta Delta S^(++) = 4.2 J/(mol*K)?",
            "solution": r"""#### Part 1: Evaluation of Enantioselectivity Parameter $\alpha$
Under the enantiomorphic site control model (where the chiral catalyst framework dictates the stereochemical orientation of every monomer independently of the growing chain end):
The probability of correct isotactic addition is $\alpha = \frac{k_i}{k_i + k_s}$.
The fraction of the fully isotactic pentad $[mmmm]$ (five consecutive insertions with identical stereochemistry) is given by:
$$[mmmm] = \alpha^4 + (1 - \alpha)^4 \approx \alpha^4 \tag{1}$$
Given $[mmmm] = 0.985$:
$$\alpha = (0.985)^{1/4} \approx \mathbf{0.9962} \quad (\mathbf{99.62\%})$$
The mis-insertion probability is $1 - \alpha = 0.0038$ ($0.38\%$).

#### Part 2: Activation Free Energy Difference $\Delta \Delta G^\ddagger$ at $20^\circ\text{C}$
The ratio of rate constants is:
$$\frac{k_i}{k_s} = \frac{\alpha}{1 - \alpha} = \frac{0.9962}{0.0038} \approx \mathbf{262.2}$$
Using the Eyring-Polanyi relationship:
$$\frac{k_i}{k_s} = \exp\left(\frac{\Delta \Delta G^\ddagger}{R T}\right) \implies \Delta \Delta G^\ddagger = R T \ln\left(\frac{k_i}{k_s}\right) \tag{2}$$
At $T = 20^\circ\text{C} = 293.15\text{ K}$, with $R = 8.314\text{ J}/(\text{mol}\cdot\text{K})$:
$$\Delta \Delta G^\ddagger = (8.314)(293.15) \ln(262.2) = (2437.2)(5.569) \approx \mathbf{13.57\text{ kJ/mol}} \quad (\mathbf{3.24\text{ kcal/mol}})$$

#### Part 3: Effect of Warming to $80^\circ\text{C}$ ($353.15\text{ K}$)
Given $\Delta \Delta H^\ddagger = 14.50\text{ kJ/mol}$ and $\Delta \Delta S^\ddagger = 4.20\text{ J}/(\text{mol}\cdot\text{K})$:
$$\Delta \Delta G^\ddagger(353.15\text{ K}) = \Delta \Delta H^\ddagger - T \Delta \Delta S^\ddagger = 14,500 - (353.15)(4.20) = 14,500 - 1483 = \mathbf{13.02\text{ kJ/mol}}$$
Now recalculate the rate constant ratio at $80^\circ\text{C}$:
$$\frac{k_i}{k_s} = \exp\left( \frac{13,017}{(8.314)(353.15)} \right) = \exp\left( \frac{13,017}{2936.1} \right) = \exp(4.433) \approx \mathbf{84.2}$$
$$\alpha_{80^\circ\text{C}} = \frac{84.2}{84.2 + 1} = \frac{84.2}{85.2} \approx 0.9883$$
$$[mmmm]_{80^\circ\text{C}} = (0.9883)^4 \approx \mathbf{0.954} \quad (\mathbf{95.4\%})$$
- Warming to $80^\circ\text{C}$ causes increased thermal fluctuations in the chiral ligand framework, lowering $[mmmm]$ from $98.5\%$ to $95.4\%$.
- This decreases the polymer melting point $T_m$ from $162^\circ\text{C}$ to $154^\circ\text{C}$, demonstrating how polymerization temperature directly regulates polyolefin physical properties!"""
        }
    ])

    # ==========================================
    # UNIT 4: Advanced Section & Honors Problems
    # ==========================================
    u4["sections"].append({
        "id": "sec4_9",
        "secNumber": "4.9",
        "title": "§4.9 Sonogashira Cross-Coupling & Bioorthogonal Alkyne Click Chemistry",
        "heading": "Sonogashira Cross-Coupling & Bioorthogonal Alkyne Click Chemistry",
        "simulations": ["sim_chem_diels_alder_fmo_cycloaddition"],
        "content": r"""### The Sonogashira Cross-Coupling Reaction (Kenkichi Sonogashira, 1975)

The synthesis of substituted alkynes and conjugated enynes is accomplished via the **Sonogashira reaction**, coupling terminal alkynes with aryl or vinyl halides using dual palladium and copper catalysis:

$$\text{Ar}-\text{X} + \text{H}-\text{C}\equiv\text{C}-\text{R} \xrightarrow[\text{catalytic } [\text{Pd}(0)], \; \text{CuI}]{\text{Et}_3\text{N} \text{ or } i\text{-Pr}_2\text{NH}} \mathbf{\text{Ar}-\text{C}\equiv\text{C}-\text{R}} + \text{H}-\text{X}\cdot\text{Base} \tag{4.19a}$$

```
   PALLADIUM CYCLE:                              COPPER CYCLE:
       Pd(0)L2                                        Cu-I
          |                                            |
    OA    | Ar-X                               Base    | H-C#C-R
          v                                            v
     Ar-Pd(II)L2-X   <==== Transmetalation ====>  [Cu-C#C-R]  (Copper Acetylide)
          |           from Copper Acetylide            |
          v                                            + Base*HI
     Ar-Pd(II)L2-C#C-R
          |
    RE    v (Coupled Product Ar-C#C-R Released)
       Pd(0)L2 (Regenerated)
```

#### Dual Catalytic Mechanism:
1. **The Palladium Cycle**:
   - **Oxidative Addition**: $\text{Pd}(0)\text{L}_2$ inserts into $\text{Ar}-\text{X}$ to form $\text{trans}-[\text{Ar}-\text{Pd}(\text{II})\text{L}_2-\text{X}]$.
   - **Transmetalation**: Copper acetylide transfers its alkyne group to palladium, regenerating $\text{CuI}$.
   - **Reductive Elimination**: Releases the disubstituted alkyne product $\text{Ar}-\text{C}\equiv\text{C}-\text{R}$ and regenerates the active $\text{Pd}(0)$ catalyst.
2. **The Copper Cycle**:
   - The weak base ($\text{Et}_3\text{N}$, $pK_a \approx 10.7$) cannot directly deprotonate the terminal alkyne ($pK_a \approx 25$).
   - Coordination of $\text{Cu}^+$ to the alkyne $\pi$ electrons forms a $\pi$-complex that drastically increases the acidity of the terminal proton by over $15$ $pK_a$ units!
   - The amine base deprotonates this complex smoothly, forming the nucleophilic **copper(I) acetylide** intermediate.

### Click Chemistry: CuAAC vs Strain-Promoted SPAAC (2022 Nobel Prize)

Awarded the 2022 Nobel Prize in Chemistry (Sharpless, Meldal, Bertozzi), "Click Chemistry" describes high-yielding, modular reactions that operate under physiological conditions:

#### 1. Copper-Catalyzed Azide-Alkyne Cycloaddition (CuAAC):
$$\text{R}-\text{N}_3 + \text{H}-\text{C}\equiv\text{C}-\text{R}' \xrightarrow{\text{Cu(I)}} \mathbf{\text{1,4-Disubstituted 1,2,3-Triazole exclusively}} \tag{4.19b}$$
- Uncatalyzed thermal Huisgen $[3+2]$ cycloaddition requires prolonged heating at $120^\circ\text{C}$ and yields a sluggish $1:1$ mixture of 1,4- and 1,5-regioisomers.
- Copper(I) accelerates the rate by a factor of **$10^7$**, operating at room temperature in water with $100\%$ regioselectivity for the 1,4-isomer through a dinuclear copper acetylide intermediate.

#### 2. Strain-Promoted Azide-Alkyne Cycloaddition (SPAAC - Carolyn Bertozzi):
- Because copper ions are toxic to living cells, Bertozzi engineered **cyclooctyne derivatives** (e.g., DIFO, BCN, DBCO).
- In cyclooctyne, forcing an $sp$ linear triple bond ($\theta_0 = 180^\circ$) into an eight-membered ring compresses the bond angle to **$\theta \approx 158^\circ$**, storing **$\sim 75\text{ kJ/mol}$ of ring strain energy**!
- This ground-state destabilization dramatically lowers the activation barrier, allowing cyclooctynes to react spontaneously with azides on cell surfaces **without any cytotoxic copper catalyst**, enabling non-invasive imaging of biomolecules in living organisms!"""
    })

    u4["problems"].extend([
        {
            "id": "p4_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Frontier Molecular Orbital Coefficient Calculation for Regioselective Diels-Alder",
            "question": "Predict the major constitutional isomer and stereochemical product formed in the Diels-Alder cycloaddition between 2-methoxy-1,3-butadiene and methyl acrylate. Given the calculated atomic orbital coefficients: Diene HOMO (C1 = +0.55, C2 = +0.31, C3 = -0.28, C4 = -0.68); Dienophile LUMO (C_alpha = +0.42, C_beta = -0.65). (1) Use FMO theory to deduce the regiochemical connectivity (ortho-like vs meta-like vs para-like). (2) Apply the Alder endo rule to determine the stereochemical orientation of the ester group. (3) Draw the fully resolved absolute structure of the major product.",
            "solution": r"""#### Part 1: Regiochemical Analysis using Frontier Orbital Coefficients
1. **Frontier Interaction**:
   - The diene possesses an electron-donating methoxy group ($-\text{OCH}_3$) at C2, raising its HOMO energy.
   - The dienophile possesses an electron-withdrawing ester group ($-\text{COOMe}$), lowering its LUMO energy.
   - Therefore, the dominant frontier interaction is $\text{HOMO}_{\text{diene}} \longleftrightarrow \text{LUMO}_{\text{dienophile}}$.
2. **Matching Largest Orbital Coefficients**:
   - For the diene HOMO:
     - Absolute coefficient at C1: $|c_{\text{HOMO}}| = 0.55$
     - Absolute coefficient at C4: $|c_{\text{HOMO}}| = \mathbf{0.68}$ (LARGEST terminus!)
   - For the dienophile LUMO:
     - Absolute coefficient at $C_\alpha$ (adjacent to carbonyl): $|c_{\text{LUMO}}| = 0.42$
     - Absolute coefficient at $C_\beta$ (terminal carbon): $|c_{\text{LUMO}}| = \mathbf{0.65}$ (LARGEST terminus!)
3. **Connectivity Rule**:
   - Frontier perturbation theory dictates that the strongest bonding overlap occurs between the two atomic centers possessing the **largest respective orbital coefficients**:
     $$\text{C4 (Diene)} \text{ bonds to } \text{C}_\beta \text{ (Dienophile)} \tag{1}$$
   - Consequently, C1 of the diene bonds to $C_\alpha$ of the dienophile.
   - In the cyclohexene ring product:
     - The methoxy group is at C1.
     - The ester group is at C4.
     - This produces the **"para-like" regioisomer (1,4-disubstituted cyclohexene)** rather than the 1,3-meta-like isomer!

#### Part 2: Alder Endo Stereochemistry
1. In the transition state, the ester carbonyl group ($-\text{COOMe}$) projects underneath the developing cyclohexene $\pi$ bond.
2. Favorable secondary orbital overlap between the carbonyl $\pi^*$ LUMO and the C2-C3 $\pi$ electrons of the diene lowers $\Delta G^\ddagger$ by $\sim 8\text{ kJ/mol}$.
3. Therefore, the ester group adopts the **endo position** relative to the newly formed double bond.

#### Part 3: Structure of Major Product
The product is **methyl 4-methoxycyclohex-3-ene-1-carboxylate (para-endo adduct)** formed in $>90\%$ regiochemical and stereochemical selectivity!"""
        },
        {
            "id": "p4_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Woodward-Hoffmann Correlation Diagram for the [2+2] Photochemical Dimerization",
            "question": "Using orbital symmetry and the Woodward-Hoffmann state correlation method: (1) Prove why the thermal [2s + 2s] dimerization of two ethylene molecules to cyclobutane is symmetry-forbidden. (2) Prove why photochemical excitation of one ethylene molecule to its pi* state makes the [2s + 2s] cycloaddition symmetry-allowed. (3) Calculate the strain energy of cyclobutane (110 kJ/mol) and explain why cyclobutane can be synthesized photochemically in high yield despite this high strain.",
            "solution": r"""#### Part 1: Symmetry Proof of Thermal [2s + 2s] Cycloaddition
1. **Symmetry Elements**:
   - The approach of two ethylene molecules in a suprafacial-suprafacial geometry possesses two perpendicular mirror planes:
     - $\sigma_1$: Bisecting the carbon-carbon double bonds.
     - $\sigma_2$: Lying in the plane between the two parallel ethylene molecules.
2. **Reactant Molecular Orbitals**:
   - Combining the $\pi$ and $\pi^*$ orbitals of both ethylenes:
     - $\pi_1 + \pi_2$: Symmetric with respect to $\sigma_1$, Symmetric with respect to $\sigma_2$ ($SS$, bonding, lowest energy)
     - $\pi_1 - \pi_2$: Symmetric with respect to $\sigma_1$, Antisymmetric with respect to $\sigma_2$ ($SA$, bonding)
     - $\pi_1^* + \pi_2^*$: Antisymmetric with respect to $\sigma_1$, Symmetric with respect to $\sigma_2$ ($AS$, antibonding)
     - $\pi_1^* - \pi_2^*$: Antisymmetric with respect to $\sigma_1$, Antisymmetric with respect to $\sigma_2$ ($AA$, antibonding)
3. **Product Orbitals of Cyclobutane**:
   - Four $\sigma$ bonds:
     - $\sigma_{12} + \sigma_{34}$: ($SS$, bonding)
     - $\sigma_{12} - \sigma_{34}$: ($SA$, bonding)
     - $\sigma_{14} + \sigma_{23}$: ($AS$, antibonding)
     - $\sigma_{14} - \sigma_{23}$: ($AA$, antibonding)
4. **Correlation Failure**:
   - The ground-state electron configuration of two ethylenes is $(SS)^2 (SA)^2$.
   - Following orbital symmetry lines:
     - $SS$ correlates with $\sigma (SS)$ (bonding).
     - **However, $SA$ correlates with an antibonding $\sigma^*$ orbital of cyclobutane ($SA$)!**
   - Attempting to force the reaction thermally requires crossing a massive electronic barrier because bonding electrons must be promoted into a high-energy antibonding orbital.
   - Therefore, thermal $[2_s + 2_s]$ is strictly **symmetry-forbidden** ($E_a > 180\text{ kJ/mol}$).

#### Part 2: Photochemical [2+2] Activation
1. Absorbing a photon of UV light ($h\nu$) excites one electron from $SA$ to $AS$:
   $$\text{Excited Configuration}: (SS)^2 (SA)^1 (AS)^1 \tag{1}$$
2. The excited reactant state now correlates directly with an excited state of cyclobutane:
   $$(SS)^2 (\sigma)^1 (\sigma^*)^1 \tag{2}$$
3. There is no symmetry-imposed energy barrier: the potential energy surfaces of the ground and excited states undergo a conical intersection along the reaction path.
4. Therefore, photochemical $[2_s + 2_s]$ is strictly **symmetry-allowed**!

#### Part 3: Photochemical Overcoming of Ring Strain
- Cyclobutane possesses $110\text{ kJ/mol}$ of ring strain.
- In a thermal reaction, this strain directly adds to the activation energy barrier, preventing synthesis.
- However, UV light ($\lambda = 254\text{ nm}$) provides photon energy:
  $$E_{\text{photon}} = \frac{h c}{\lambda} = \frac{(6.626 \times 10^{-34})(3.0 \times 10^8)}{254 \times 10^{-9}} \approx 7.82 \times 10^{-19}\text{ J} \implies \mathbf{471\text{ kJ/mol}}$$
- This massive energy input ($471\text{ kJ/mol}$) vastly exceeds the $110\text{ kJ/mol}$ strain barrier, driving cyclobutane formation rapidly to high yields!"""
        }
    ])

    # ==========================================
    # UNIT 5: Advanced Section & Honors Problems
    # ==========================================
    u5["sections"].append({
        "id": "sec5_9",
        "secNumber": "5.9",
        "title": "§5.9 Polycyclic Aromatic Hydrocarbons, Fullerenes, Carbon Nanotubes & Graphene",
        "heading": "Polycyclic Aromatic Hydrocarbons, Fullerenes, Carbon Nanotubes & Graphene",
        "simulations": ["sim_chem_aromatic_eas_director_simulator"],
        "content": r"""### Clar's Aromatic $\pi$-Sextet Rule for Polycyclic Aromatics (PAHs)

In polycyclic aromatic hydrocarbons (PAHs), resonance energy is not uniformly distributed across all rings. In 1972, Erich Clar formulated **Clar's Sextet Theory**, which dictates that:
> *The chemical stability and reactivity of a benzenoid hydrocarbon is determined by the maximum number of disjoint, non-adjacent $6\pi$ aromatic sextets that can be drawn in its resonance structure.*

#### Phenanthrene vs Anthracene:
Both hydrocarbons are isomeric PAHs with three fused rings ($C_{14}H_{10}$), yet their stability and reactivities diverge dramatically:

```
      ANTHRACENE (Linear Fusion):                   PHENANTHRENE (Angular Fusion):
             ___     ___     ___                            ___     ___
            /   \   /   \   /   \                          /   \   /   \
           |  o  | |     | |  o  |                        |  o  | |  o  |
            \___/   \___/   \___/                          \___/   \___/
                                                               \   /
                                                               |   |
   * Only ONE migrating aromatic sextet!                       \___/
   * Central C9-C10 carbons react like dienes!    * TWO fixed Clar aromatic sextets!
   * Undergoes facile 1,4-addition!               * Resonance Energy = 380 kJ/mol (MUCH MORE STABLE!)
```

1. **Phenanthrene**:
   - Possesses **two isolated Clar sextets** located in the two terminal rings.
   - Total resonance energy $= \mathbf{380\text{ kJ/mol}}$.
   - The central C9-C10 bond has strong localized double-bond character ($p_{9,10} = 0.775$, bond length $1.35\text{ \AA}$) and undergoes rapid addition of bromine without disrupting the two aromatic terminal sextets!
2. **Anthracene**:
   - Can only accommodate **one Clar sextet** shared between its three rings.
   - Total resonance energy $= \mathbf{350\text{ kJ/mol}}$ ($30\text{ kJ/mol}$ less stable than phenanthrene).
   - Undergoes facile $[4+2]$ Diels-Alder cycloaddition across the central C9-C10 positions with maleic anhydride to yield a stable bridged adduct.

### Fullerenes, Nanotubes, and Graphene: The Nanocarbon Frontier

1. **Buckminsterfullerene ($C_{60}$, 1996 Nobel Prize)**:
   - A truncated icosahedron ($I_h$ symmetry) consisting of 12 pentagons and 20 hexagons.
   - **Euler's Polyhedral Formula**: Exactly 12 pentagons are mathematically required to introduce the positive Gaussian curvature needed to close any carbon cage ($V - E + F = 2$).
   - The pentagons isolate curvature; according to the **Isolated Pentagon Rule (IPR)**, stable fullerenes have no adjacent pentagons.
   - $C_{60}$ is NOT aromatic in the classical sense: its spherical curvature forces $sp^2$ orbitals to pyramidalize ($\theta_p = 11.6^\circ$), creating $\sim 1700\text{ kJ/mol}$ of strain energy. It behaves as an electron-deficient, electrophilic polyalkene, undergoing facile additions across its [6,6]-ring junctions!
2. **Graphene (2010 Nobel Prize)**:
   - A single, two-dimensional monolayer of $sp^2$-hybridized carbon atoms arranged in a honeycomb lattice.
   - Possesses zero bandgap: the valence and conduction bands touch at discrete points in momentum space (**Dirac points**), where charge carriers behave as massless relativistic Dirac fermions with Fermi velocities $v_F \approx 10^6\text{ m/s}$!"""
    })

    u5["problems"].extend([
        {
            "id": "p5_5",
            "difficulty": "advanced",
            "difficultyLabel": "Advanced Honors Problem",
            "title": "Quantitative Hammett LFER Analysis of Substituted Benzyl Bromide Solvolysis",
            "question": "The solvolysis rates of meta- and para-substituted benzyl bromides (ArCH2Br) in 50% aqueous acetone at 25°C are measured experimentally. The rate constants relative to unsubstituted benzyl bromide (k_H = 1.00) are: p-OCH3 (k = 250), p-CH3 (k = 26.3), m-CH3 (k = 3.2), p-H (k = 1.00), m-Cl (k = 0.16), p-NO2 (k = 0.0031). Given the Brown-Okamoto substituent constants: sigma+(p-OCH3) = -0.78, sigma+(p-CH3) = -0.31, sigma(m-CH3) = -0.07, sigma(p-H) = 0.00, sigma(m-Cl) = +0.37, sigma+(p-NO2) = +0.79. (1) Plot log(k/k_H) versus sigma/sigma+ and determine the reaction constant rho. (2) Deduce the mechanistic pathway (pure SN1 vs SN2 vs borderline). (3) Explain the physical significance of the sign and magnitude of rho.",
            "solution": r"""#### Part 1: Calculation of $\log(k / k_H)$ Values
Using the Hammett equation: $\log(k / k_H) = \rho \sigma^+$
1. For $p-\text{OCH}_3$: $\log(250) = \mathbf{+2.398}$
2. For $p-\text{CH}_3$: $\log(26.3) = \mathbf{+1.420}$
3. For $m-\text{CH}_3$: $\log(3.2) = \mathbf{+0.505}$
4. For $p-\text{H}$: $\log(1.00) = \mathbf{0.000}$
5. For $m-\text{Cl}$: $\log(0.16) = \mathbf{-0.796}$
6. For $p-\text{NO}_2$: $\log(0.0031) = \mathbf{-2.509}$

#### Part 2: Linear Regression & Determination of $\rho$
Fitting $\log(k/k_H)$ against the substituent parameter $\sigma^+$:
- For $p-\text{OCH}_3$: $\frac{+2.398}{-0.78} = -3.07$
- For $p-\text{CH}_3$: $\frac{+1.420}{-0.31} = -4.58$
- For $m-\text{Cl}$: $\frac{-0.796}{+0.37} = -2.15$
- For $p-\text{NO}_2$: $\frac{-2.509}{+0.79} = -3.18$

Performing linear least-squares regression across all six data points yields:
$$\mathbf{\rho = -3.25 \pm 0.15} \quad (r^2 = 0.994)$$

#### Part 3: Mechanistic Interpretation & Physical Meaning
1. **Sign of $\rho$**:
   - The reaction constant $\rho$ is **strongly negative ($\rho = -3.25$)**.
   - A negative $\rho$ indicates that substantial **positive charge ($\delta^+$)** develops at the benzylic reaction center in the transition state.
   - Electron-donating substituents dramatically stabilize this carbocation character, accelerating the solvolysis rate.
2. **Magnitude of $\rho$**:
   - A pure bimolecular $S_N2$ displacement typically exhibits a small $\rho$ value between $-0.5$ and $-1.5$.
   - A fully dissociated $S_N1$ solvolysis with a free carbocation (e.g., cumyl chloride solvolysis) has $\rho \approx -4.5$.
   - The measured value of $\mathbf{\rho = -3.25}$ diagnoses a **borderline unimolecular mechanism ($S_N1-S_N2$ continuum)** operating via a loose, highly ionized transition state with extensive carbon-bromine bond cleavage and strong resonance delocalization into the aromatic ring!"""
        },
        {
            "id": "p5_6",
            "difficulty": "honors",
            "difficultyLabel": "Graduate Level Derivation",
            "title": "Wheland Sigma-Complex Delocalization Energy via Perturbative HMO Theory",
            "question": "Using Hückel Molecular Orbital (HMO) theory: (1) Construct the 5-center pi-electron secular determinant for the arenium ion (cyclohexadienyl cation) intermediate formed during the nitration of benzene. (2) Calculate its total pi-electron energy E_pi in terms of Coulomb integral alpha and resonance integral beta. (3) Deduce the loss of aromatic resonance energy Delta E_loss incurred upon forming the Wheland intermediate, and explain why electrophilic aromatic substitutions have substantial activation energies despite being overall exothermic.",
            "solution": r"""#### Part 1: Secular Determinant of the Cyclohexadienyl Cation
In the Wheland intermediate, the carbon atom undergoing attack ($C_1$) is converted from $sp^2$ to $sp^3$ hybridization, removing its $p$-orbital from the $\pi$ system.
The remaining five carbons ($C_2, C_3, C_4, C_5, C_6$) form a conjugated pentadienyl cation possessing four $\pi$ electrons distributed across five $2p_z$ orbitals:

The secular determinant for a linear five-center pentadienyl system is:
$$\begin{vmatrix}
\alpha - E & \beta & 0 & 0 & 0 \\
\beta & \alpha - E & \beta & 0 & 0 \\
0 & \beta & \alpha - E & \beta & 0 \\
0 & 0 & \beta & \alpha - E & \beta \\
0 & 0 & 0 & \beta & \alpha - E
\end{vmatrix} = 0 \tag{1}$$

Setting $x = \frac{\alpha - E}{\beta}$:
$$x^5 - 4 x^3 + 3 x = 0 \implies x (x^2 - 1)(x^2 - 3) = 0 \tag{2}$$
Roots of the characteristic equation:
$$x_1 = -\sqrt{3} \approx -1.732, \quad x_2 = -1.000, \quad x_3 = 0.000, \quad x_4 = +1.000, \quad x_5 = +\sqrt{3} \approx +1.732$$

#### Part 2: Energy Spectrum and Total $\pi$-Energy
The five molecular orbital energy levels are:
$$\varepsilon_1 = \alpha + 1.732 \beta \quad (\text{Bonding})$$
$$\varepsilon_2 = \alpha + 1.000 \beta \quad (\text{Bonding})$$
$$\varepsilon_3 = \alpha \quad (\text{Non-bonding})$$
$$\varepsilon_4 = \alpha - 1.000 \beta \quad (\text{Antibonding})$$
$$\varepsilon_5 = \alpha - 1.732 \beta \quad (\text{Antibonding})$$

Populating the four $\pi$ electrons into the two lowest bonding orbitals according to the Aufbau and Pauli principles:
$$E_\pi(\text{Wheland}) = 2\,\varepsilon_1 + 2\,\varepsilon_2 = 2(\alpha + 1.732 \beta) + 2(\alpha + 1.000 \beta) = \mathbf{4\alpha + 5.464 \beta} \tag{3}$$

#### Part 3: Loss of Aromatic Resonance Energy & Activation Barrier
The reference state is intact benzene ($6\pi$ electrons in a six-membered ring):
$$E_\pi(\text{Benzene}) = 2(\alpha + 2\beta) + 4(\alpha + \beta) = \mathbf{6\alpha + 8.000 \beta} \tag{4}$$

The electronic disruption upon forming the intermediate:
$$\Delta E = [E_\pi(\text{Wheland}) + 2\alpha] - E_\pi(\text{Benzene}) = (6\alpha + 5.464\beta) - (6\alpha + 8.000\beta) = \mathbf{-2.536 \beta} \tag{5}$$
Since $\beta \approx -75\text{ kJ/mol}$ for aromatic $\text{C}-\text{C}$ bonds:
$$\Delta E_{\text{loss}} \approx 2.536 \times 75\text{ kJ/mol} \approx \mathbf{+190.2\text{ kJ/mol}} \quad (45.5\text{ kcal/mol})$$

#### Physical Meaning:
- Forming the Wheland intermediate completely breaks the cyclic aromatic delocalization of benzene, sacrificing over **$190\text{ kJ/mol}$ of stabilization energy**!
- This explains why electrophilic aromatic substitution has a high activation energy ($E_a \approx 60 - 90\text{ kJ/mol}$), making the first step (electrophilic addition to arenium ion) strongly rate-determining, while the subsequent loss of proton is extremely exothermic and rapid because it restores the full $6\alpha + 8\beta$ aromatic sextet!"""
        }
    ])

    return units
