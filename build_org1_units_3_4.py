# Unit 3 & Unit 4 Content Generator for Organic Chemistry I
# Strict zero course numbers or marks

def get_unit_3():
    return {
        "id": "unit3",
        "unitId": "unit3-org1",
        "number": 3,
        "unitNumber": 3,
        "title": "Unit 3: Unsaturated Hydrocarbons: Alkenes, Elimination Stereochemistry & Addition Mechanisms",
        "description": "Rigorous treatment of alkenes: Degree of unsaturation, E/Z stereochemical configuration, bimolecular and unimolecular elimination mechanics, electrophilic additions, cyclic halonium stereospecificity, oxymercuration vs hydroboration regiochemistry, Criegee ozonolysis mechanism, epoxidation, and coordination polymerization.",
        "leadSummary": "Comprehensive study of alkene structure, E/Z stereodescriptors, E2/E1 elimination pathways, electrophilic addition mechanisms, stereospecific anti-bromination, hydration methodologies, oxidative cleavages, and polymerizations.",
        "simulations": ["sim_chem_alkene_addition_stereochemistry"],
        "sections": [
            {
                "id": "sec3_1",
                "secNumber": "§3.1",
                "title": "Structure, Degree of Unsaturation & E/Z Stereochemistry",
                "heading": "Structure, Degree of Unsaturation & E/Z Stereochemistry",
                "content": """Alkenes (olefins) are acyclic hydrocarbons containing at least one carbon-carbon double bond ($\\text{C}=\\text{C}$), corresponding to the general molecular formula $\\text{C}_n\\text{H}_{2n}$. Each double-bonded carbon is $sp^2$ hybridized, with three coplanar $sp^2$ hybrid orbitals forming strong $\\sigma$ bonds at angles of approximately $120^\\circ$ and one unhybridized $2p_z$ orbital oriented strictly perpendicular to the molecular plane. Parallel sideways overlap of the two $2p_z$ orbitals establishes a $\\pi$ molecular bond.

### The Index of Hydrogen Deficiency (IHD / Degree of Unsaturation)

The **Degree of Unsaturation** specifies the total sum of rings and $\\pi$ bonds present in a molecule. For a general organic formula $\\text{C}_c\\text{H}_h\\text{N}_n\\text{O}_o\\text{X}_x$ (where $\\text{X} = \\text{F, Cl, Br, I}$):
$$\\text{IHD} = c - \\frac{h}{2} - \\frac{x}{2} + \\frac{n}{2} + 1 \\tag{3.1}$$
- Oxygen and sulfur atoms do not alter the saturated hydrogen count and are omitted from Eq. (3.1).
- Halogens replace one hydrogen atom (subtracted as $x/2$).
- Nitrogen atoms introduce an additional trivalent bond (added as $n/2$).
- An IHD of 1 corresponds to either one double bond or one ring; an IHD of 4 strongly suggests an aromatic benzene ring (3 $\\pi$ bonds + 1 ring).

---

### The Barrier to Rotation & Geometric Stereoisomerism

In alkanes, rotation about $\\text{C}-\\text{C}$ single $\\sigma$ bonds is rapid under ambient conditions (torsional barrier in ethane is only $\\sim 12\\text{ kJ/mol}$). In alkenes, rotation about the $\\text{C}=\\text{C}$ double bond requires twisting the $2p_z$ orbitals out of parallel alignment, breaking the $\\pi$ bond completely:
$$\\Delta G^\\ddagger_{\\text{rotation}} = \\text{BDE}(\\pi) \\approx 260 - 270\\text{ kJ}\\cdot\\text{mol}^{-1} \\tag{3.2}$$
This colossal energy barrier prevents spontaneous rotation at temperatures below $400^\\circ\\text{C}$, freezing substituents into rigid, non-interconverting **geometric stereoisomers**.

#### The Cahn-Ingold-Prelog (CIP) $E/Z$ Priority Rules
While historical *cis/trans* terminology suffices for disubstituted alkenes, it fails for tri- and tetra-substituted systems. The CIP system assigns priority to the two substituents on each carbon:
1. **Rule 1: Atomic Number**: Higher atomic number takes precedence ($\\text{I} > \\text{Br} > \\text{Cl} > \\text{S} > \\text{F} > \\text{O} > \\text{N} > \\text{C} > \\text{H} > \\text{lone pair}$).
2. **Rule 2: Subsequent Shells**: If the bonded atoms are identical, compare the atoms attached to them in order of decreasing atomic number until a point of difference is reached.
3. **Rule 3: Multiple Bonds**: Multiply-bonded atoms are duplicated or triplicated (e.g., $-\\text{CH}=\\text{O}$ is treated as carbon bonded to $(\\text{O, O, H})$).
- If the two highest-priority groups lie on the same side of the double bond: ***(Z)*** (from German *zusammen* = together).
- If the two highest-priority groups lie on opposite sides of the double bond: ***(E)*** (from German *entgegen* = opposite).""",
                "simulations": []
            },
            {
                "id": "sec3_2",
                "secNumber": "§3.2",
                "title": "Synthesis of Alkenes: E2 and E1 Elimination Mechanics",
                "heading": "Synthesis of Alkenes: E2 and E1 Elimination Mechanics",
                "content": """Alkenes are synthesized via $\\beta$-elimination of alkyl halides or alcohols:
$$\\text{H}-\\text{C}_\\beta-\\text{C}_\\alpha-\\text{X} + \\text{Base} \\longrightarrow \\text{C}=\\text{C} + \\text{H-Base}^+ + \\text{X}^- \\tag{3.3}$$

### The Bimolecular Elimination ($E2$) Mechanism

The $E2$ pathway is a concerted, single-step bimolecular reaction exhibiting second-order kinetics:
$$\\text{Rate} = k_2 [\\text{R}-\\text{X}] [\\text{Base}] \\tag{3.4}$$
The base abstracts the $\\beta$-proton simultaneously with the expulsion of the leaving group and formation of the $\\text{C}=\\text{C}$ $\\pi$ bond.

#### Strict Stereoelectronic Requirement: Anti-Periplanar Geometry
Quantum mechanical overlap requires that the $\\text{C}_\\beta-\\text{H}$ $\\sigma$ bonding orbital and the $\\text{C}_\\alpha-\\text{X}$ $\\sigma^*$ antibonding orbital lie in the **same plane with a dihedral angle of $\\phi = 180^\\circ$ (anti-periplanar)**:
$$\\sigma(\\text{C}-\\text{H}) \\longrightarrow \\sigma^*(\\text{C}-\\text{X}) \\tag{3.5}$$
This allows smooth continuous electron flow from the breaking $\\text{C}-\\text{H}$ bond into the empty $\\sigma^*$ orbital of the leaving group, transforming directly into the new $\\pi$ bond with minimal electronic reorganization.

---

### Regiochemical Control: Zaitsev vs Hofmann Elimination

1. **Zaitsev's Rule (Thermodynamic Control)**:
   When dehydrohalogenation is carried out with small, unhindered bases (such as $\\text{NaOCH}_3, \\text{NaOCH}_2\\text{CH}_3, \\text{NaOH}$), the major product is the **most substituted, thermodynamically most stable alkene**:
   $$\\text{Tetrasubstituted} > \\text{Trisubstituted} > \\text{Disubstituted} > \\text{Monosubstituted}$$
   Stabilization originates from $\\sigma_{\\text{C}-\\text{H}} \\to \\pi^*$ **hyperconjugation** and stronger $sp^2-sp^3$ $\\sigma$ bonds.
2. **Hofmann's Rule (Steric / Kinetic Control)**:
   When dehydrohalogenation is carried out with sterically encumbered bases (such as potassium tert-butoxide, $\\text{KO}t\\text{-Bu}$, or lithium diisopropylamide, $\\text{LDA}$), or with substrates bearing poor leaving groups (such as quaternary ammonium hydroxides $-\\text{N}^+\\text{R}_3$ or sulfonium $-\\text{S}^+\\text{R}_2$):
   Steric clash prevents the bulky base from accessing crowded interior $\\beta$-hydrogens. The base abstracts the **least hindered primary hydrogen**, yielding the **least substituted alkene** as the major product.""",
                "simulations": []
            },
            {
                "id": "sec3_3",
                "secNumber": "§3.3",
                "title": "Electrophilic Additions: Markovnikov's Rule & Carbocation Rearrangements",
                "heading": "Electrophilic Additions: Markovnikov's Rule & Carbocation Rearrangements",
                "content": """The hallmark reaction of alkenes is **electrophilic addition**. Because the $\\pi$ electron cloud lies above and below the nuclear plane and has a high-energy HOMO, it acts as an electron-rich Lewis base (nucleophile), reacting readily with electrophiles ($E^+$):
$$\\text{C}=\\text{C} + \\text{E}-\\text{Y} \\longrightarrow -\\text{C}(\\text{E})-\\text{C}(\\text{Y})- \\tag{3.6}$$

### The Stepwise Carbocation Mechanism & Markovnikov's Rule

When a hydrogen halide ($HX$, where $X = \\text{Cl, Br, I}$) adds across an unsymmetrical alkene:
1. **Rate-Determining Step (RDS)**: The $\\pi$ electrons attack the electrophilic proton ($H^+$), generating a carbocation intermediate:
   $$\\text{R}-\\text{CH}=\\text{CH}_2 + \\text{H}-\\text{X} \\xrightarrow{\\text{slow}} \\text{R}-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}_3 + \\text{X}^- \\tag{3.7}$$
2. **Fast Trapping**: The halide nucleophile ($X^-$) captures the carbocation:
   $$\\text{R}-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}_3 + \\text{X}^- \\xrightarrow{\\text{fast}} \\text{R}-\\text{CH}(\\text{X})-\\text{CH}_3 \\tag{3.8}$$

#### Vladimir Markovnikov's Rule (1869)
> In the addition of an unsymmetrical protic acid $HX$ to an unsymmetrical alkene, the acid hydrogen attaches to the carbon atom that already possesses the greater number of hydrogen atoms, while the halogen attaches to the more substituted carbon.

#### Modern Mechanistic Basis: Carbocation Stability
The reaction proceeds through the lowest activation energy barrier $\\Delta G^\\ddagger$, which by Hammond's postulate is governed by the relative thermodynamic stability of the carbocation intermediates:
$$\\text{Tertiary } (3^\\circ) > \\text{Secondary } (2^\\circ) \\gg \\text{Primary } (1^\\circ) \\gg \\text{Methyl } (\\text{CH}_3^+)$$
- **Hyperconjugation**: Overlap of adjacent $\\sigma_{\\text{C}-\\text{H}}$ and $\\sigma_{\\text{C}-\\text{C}}$ bonds with the empty unhybridized $2p_z$ orbital of the cationic carbon delocalizes the positive charge. Each attached alkyl group contributes stabilizing hyperconjugative interactions.
- **Inductive Electron Donation**: Alkyl groups are polarizable and release electron density ($+I$) toward the electron-deficient positive center.

---

### Carbocation Skeletal Rearrangements (1,2-Shifts)

Because carbocations are high-energy reactive intermediates with planar $sp^2$ geometry, they undergo rapid unimolecular isomerization whenever a 1,2-shift converts a less stable carbocation into a more stable one:
1. **1,2-Hydride Shift**: A hydrogen atom migrates with its bonding pair of electrons:
   $$\\text{CH}_3-\\text{CH}(\\text{CH}_3)-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}_3 \\; (2^\\circ) \\longrightarrow (\\text{CH}_3)_2\\stackrel{\\oplus}{\\text{C}}-\\text{CH}_2-\\text{CH}_3 \\; (3^\\circ) \\tag{3.9}$$
2. **1,2-Alkyl (Methyl) Shift**: A methyl or alkyl group migrates with its bonding pair:
   $$(\\text{CH}_3)_3\\text{C}-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}_3 \\; (2^\\circ) \\longrightarrow (\\text{CH}_3)_2\\stackrel{\\oplus}{\\text{C}}-\\text{CH}(\\text{CH}_3)_2 \\; (3^\\circ) \\tag{3.10}$$
These rearrangements frequently produce unexpected structural isomers in acid-catalyzed additions.""",
                "simulations": ["sim_chem_alkene_addition_stereochemistry"]
            },
            {
                "id": "sec3_4",
                "secNumber": "§3.4",
                "title": "Stereospecific Halogenation & The Cyclic Halonium Intermediate",
                "heading": "Stereospecific Halogenation & The Cyclic Halonium Intermediate",
                "content": """When an alkene reacts with elemental bromine ($\\text{Br}_2$) or chlorine ($\\text{Cl}_2$) in non-nucleophilic solvents (such as $\\text{CH}_2\\text{Cl}_2$ or $\\text{CCl}_4$), the reaction does **not** proceed through an open carbocation. Instead, it proceeds with **strict stereospecific anti-addition**.

### The Cyclic Bromonium Ion Mechanism (Kimball & Roberts, 1937)

1. **Electrophilic Attack & Ring Closure**:
   As the non-polar $\\text{Br}_2$ molecule approaches the electron-rich alkene, its polarizable electron cloud is induced into a dipole ($^{\\delta+}\\text{Br}-\\text{Br}^{\\delta-}$). The $\\pi$ electrons attack the electrophilic bromine atom while the bromine lone pair simultaneously back-donates into the developing empty orbital on carbon, displacing bromide ($\\text{Br}^-$):
   $$\\text{C}=\\text{C} + \\text{Br}_2 \\longrightarrow \\begin{matrix} \\text{C} & - & \\text{C} \\\\ & \\backslash \\;\\stackrel{\\oplus}{\\text{Br}} \\;/ & \\end{matrix} + \\text{Br}^- \\tag{3.11}$$
   This generates a **cyclic three-membered bromonium ion intermediate**.
2. **Stereospecific Backside Attack ($S_N2$)**:
   The three-membered ring shields the face on which it formed. The liberated bromide ion ($\\text{Br}^-$) can only attack from the **opposite face (backside attack)**, opening the ring with complete inversion of configuration at the attacked carbon:
   $$\\text{Bromonium Ion} + \\text{Br}^- \\longrightarrow \\text{trans-1,2-dibromoalkane} \\tag{3.12}$$

#### Proof of Stereospecificity:
- Addition of $\\text{Br}_2$ to *(E)*-2-butene yields exclusively the optically inactive ***meso*-2,3-dibromobutane**.
- Addition of $\\text{Br}_2$ to *(Z)*-2-butene yields exclusively the **racemic pair $(\\pm)$-2,3-dibromobutane** ($50\\% \\; (2R,3R)$ and $50\\% \\; (2S,3S)$).
If an open carbocation were formed, free rotation about the $\\text{C}-\\text{C}$ single bond would have produced a mixture of *meso* and racemic diastereomers from both alkenes!""",
                "simulations": ["sim_chem_alkene_addition_stereochemistry"]
            },
            {
                "id": "sec3_5",
                "secNumber": "§3.5",
                "title": "Alkene Hydration: Acid Catalysis, Oxymercuration & Hydroboration",
                "heading": "Alkene Hydration: Acid Catalysis, Oxymercuration & Hydroboration",
                "content": """The addition of water across an alkene converts it into an alcohol. Modern organic chemistry possesses three complementary methods with distinct regiochemical and stereochemical controls:

### 1. Acid-Catalyzed Hydration
- **Reagent**: Dilute aqueous sulfuric acid ($\\text{H}_2\\text{SO}_4 / \\text{H}_2\\text{O}$).
- **Mechanism**: Stepwise addition via open carbocation intermediate.
- **Regioselectivity**: **Markovnikov**.
- **Major Limitation**: Severely prone to **carbocation rearrangements** (1,2-hydride and methyl shifts), giving low yields of the unrearranged product whenever branching is present.

---

### 2. Oxymercuration-Demercuration (Markovnikov without Rearrangement)
- **Reagents**: 
  1. Mercury(II) acetate in aqueous THF: $\\text{Hg(OAc)}_2, \\text{H}_2\\text{O}$.
  2. Sodium borohydride in basic media: $\\text{NaBH}_4, \\text{NaOH}$.
- **Mechanism**:
  - Reaction of the alkene with $\\text{Hg(OAc)}^+$ forms a stable, three-membered **mercurinium ion intermediate**, locking the carbon skeleton and completely preventing carbocation rearrangements.
  - Water attacks the mercurinium ion at the **more substituted, more electrophilic carbon** (partial carbocation character).
  - In step 2, $\\text{NaBH}_4$ replaces the mercury moiety with hydrogen via radical demercuration.
- **Outcome**: **Markovnikov alcohol in high yield without skeletal rearrangement**.

---

### 3. Hydroboration-Oxidation (Herbert C. Brown, Nobel Prize 1979)
- **Reagents**:
  1. Borane-THF complex: $\\text{BH}_3 \\cdot \\text{THF}$.
  2. Alkaline hydrogen peroxide: $\\text{H}_2\\text{O}_2, \\text{NaOH}$.
- **Mechanism**:
  - Boron is electron-deficient (empty $2p$ orbital) and acts as the electrophile. Borane adds to the alkene in a **concerted, four-membered cyclic square transition state**:
    $$\\left[ \\begin{matrix} \\text{R}-\\text{CH} & = & \\text{CH}_2 \\\\ \\vdots & & \\vdots \\\\ \\text{H} & \\cdots & \\text{BH}_2 \\end{matrix} \\right]^\\ddagger \\longrightarrow \\text{R}-\\text{CH}_2-\\text{CH}_2-\\text{BH}_2 \\tag{3.13}$$
  - **Steric Factor**: Boron ($-\\text{BH}_2$) is sterically bulkier than hydrogen, attaching preferentially to the less crowded, less substituted terminal carbon.
  - **Electronic Factor**: Partial positive charge develops on the more substituted carbon in the transition state, stabilizing the developing charge.
  - **Oxidation**: Treatment with alkaline $\\text{H}_2\\text{O}_2$ oxidizes the trialkylborane via hydroperoxide anion addition and 1,2-alkyl migration with **complete retention of stereochemical configuration**.
- **Outcome**: **Anti-Markovnikov, stereospecific syn-addition of water**.""",
                "simulations": ["sim_chem_alkene_addition_stereochemistry"]
            },
            {
                "id": "sec3_6",
                "secNumber": "§3.6",
                "title": "Oxidative Cleavages: Ozonolysis, Epoxidation & Syn-Dihydroxylation",
                "heading": "Oxidative Cleavages: Ozonolysis, Epoxidation & Syn-Dihydroxylation",
                "content": """### 1. Ozonolysis (The Criegee Mechanism)
Ozone ($\\text{O}_3$, a 1,3-dipole) oxidatively cleaves both the $\\sigma$ and $\\pi$ bonds of an alkene:
1. **1,3-Dipolar Cycloaddition**: Ozone adds across the $\\text{C}=\\text{C}$ double bond to form an unstable **primary ozonide (molozonide)**.
2. **Retro-Cycloaddition**: The molozonide fragments into a carbonyl compound and a carbonyl oxide zwitterion (Criegee intermediate).
3. **Recombination**: The fragments recombine to form a stable **secondary ozonide (trioxolane)**.
4. **Workup**:
   - **Reductive Workup** ($\\text{Zn} / \\text{CH}_3\\text{COOH}$ or dimethyl sulfide, $\\text{(CH}_3)_2\\text{S}$): Cleaves the ozonide to aldehydes and ketones without further oxidation.
   - **Oxidative Workup** ($\\text{H}_2\\text{O}_2$): Converts aldehydes into carboxylic acids.

---

### 2. Epoxidation (The Prilezhaev Reaction)
Peroxycarboxylic acids (such as meta-chloroperoxybenzoic acid, **$m$CPBA**) react with alkenes to form **epoxides (oxiranes)** via a concerted 'butterfly' transition state:
$$\\text{C}=\\text{C} + \\text{R}-\\text{CO}_3\\text{H} \\longrightarrow \\text{Epoxide} + \\text{R}-\\text{CO}_2\\text{H} \\tag{3.14}$$
The reaction is strictly **stereospecific syn-addition**: a *cis*-alkene produces a *cis*-disubstituted epoxide, while a *trans*-alkene produces a *trans*-disubstituted epoxide.

---

### 3. Syn-Dihydroxylation: Potassium Permanganate & Osmium Tetroxide
Alkenes react with cold, dilute, alkaline $\\text{KMnO}_4$ (Baeyer's Test) or catalytic $\\text{OsO}_4$ with $N$-methylmorpholine $N$-oxide (NMO, Upjohn dihydroxylation) to form **vicinal syn-diols (glycols)**:
$$\\text{C}=\\text{C} + \\text{OsO}_4 \\longrightarrow \\begin{matrix} \\text{C} & - & \\text{C} \\\\ \\vert & & \\vert \\\\ \\text{O} & - & \\text{O} \\\\ & \\backslash \\;\\text{OsO}_2 \\;/ & \\end{matrix} \\xrightarrow{\\text{NMO, } \\text{H}_2\\text{O}} -\\text{C}(\\text{OH})-\\text{C}(\\text{OH})- + \\text{OsO}_4 \\tag{3.15}$$
Because both oxygen atoms are delivered simultaneously from the same face of the planar cyclic osmate ester intermediate, the addition is strictly **stereospecific syn**.""",
                "simulations": []
            },
            {
                "id": "sec3_7",
                "secNumber": "§3.7",
                "title": "Alkene Polymerizations: Radical, Ionic & Coordination (Ziegler-Natta)",
                "heading": "Alkene Polymerizations: Radical, Ionic & Coordination (Ziegler-Natta)",
                "content": """Polymerization of alkenes converts thousands of monomeric units into high-molecular-weight macromolecules:
$$n\\,\\text{CH}_2=\\text{CHR} \\longrightarrow -[\\text{CH}_2-\\text{CHR}]_n- \\tag{3.16}$$

### 1. Free-Radical Polymerization
- **Initiators**: Organic peroxides (benzoyl peroxide, AIBN) that undergo homolytic cleavage.
- **Propagation**: Radicals add to the terminal methylene of alkene monomers.
- **Consequence**: Produces **Low-Density Polyethylene (LDPE)** containing extensive short- and long-chain branching caused by intramolecular 'backbiting' hydrogen abstraction.

### 2. Ionic Polymerization
- **Cationic Polymerization**: Initiated by Lewis acids ($\\text{BF}_3, \\text{AlCl}_3$ + traces of $\\text{H}_2\\text{O}$) for monomers with electron-donating groups (isobutylene $\\to$ polyisobutylene / butyl rubber).
- **Anionic Polymerization**: Initiated by strong nucleophiles ($n\\text{-BuLi}, \\text{NaNH}_2$) for monomers bearing electron-withdrawing groups (acrylonitrile, methyl methacrylate). Operates as **living polymerization** with zero spontaneous chain termination.

### 3. Ziegler-Natta Coordination Polymerization (Nobel Prize 1963)
Karl Ziegler and Giulio Natta introduced heterogeneous catalysts consisting of titanium tetrachloride and triethylaluminum:
$$\\text{TiCl}_4 + \\text{Al(CH}_2\\text{CH}_3)_3 \\tag{3.17}$$
- **Cossee-Arlman Mechanism**: The alkene coordinates to an open coordination site on the octahedral titanium center and inserts into the titanium-carbon $\\sigma$ bond.
- **Stereochemical Control**: Enables the synthesis of strictly linear **High-Density Polyethylene (HDPE)** and **isotactic polypropylene** (all methyl groups arranged on the identical side of the backbone), yielding polymers with superior tensile strength and high melting points.""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob3_1",
                "difficulty": "foundational",
                "difficultyLabel": "Foundational Level",
                "title": "Problem 3.1: CIP Stereodescriptors & Bromination Stereospecificity of 2-Butene",
                "question": """1. Assign the complete IUPAC stereodescriptor (E or Z) to each of the following alkenes, showing the priority ranking of all four substituents according to Cahn-Ingold-Prelog rules:
   - Compound 1: $\\text{Cl(CH}_3)\\text{C}=\\text{C(H)CH}_2\\text{CH}_3$
   - Compound 2: $\\text{(CH}_3)_2\\text{CH(Br)C}=\\text{C(Cl)CH}_2\\text{OCH}_3$
2. Pure *(E)*-2-butene is treated with bromine ($\\text{Br}_2$) in carbon tetrachloride.
   - Draw the cyclic bromonium ion intermediate.
   - Show the backside nucleophilic attack of bromide ion at both carbons.
   - Identify whether the resulting product is a *meso* compound or a racemic mixture, providing complete $(R/S)$ configurations at each stereocenter.
3. Repeat the analysis for the bromination of *(Z)*-2-butene.""",
                "solution": """### Part 1: Cahn-Ingold-Prelog Priority Assignments

#### Compound 1: $\\text{Cl(CH}_3)\\text{C}=\\text{C(H)CH}_2\\text{CH}_3$
- **Left Carbon (C2)**:
  - $-\\text{Cl}$ (atomic number $Z = 17$): **Priority 1**
  - $-\\text{CH}_3$ (atomic number $Z = 6$): **Priority 2**
- **Right Carbon (C3)**:
  - $-\\text{CH}_2\\text{CH}_3$ (carbon $Z = 6$): **Priority 1**
  - $-\\text{H}$ (hydrogen $Z = 1$): **Priority 2**
- Relationship: Priority 1 groups ($-\\text{Cl}$ and $-\\text{CH}_2\\text{CH}_3$) are on opposite sides of the double bond.
- **Stereodescriptor**: ***(2E)*** $\\implies$ **(2E)-2-Chloropent-2-ene**.

#### Compound 2: $\\text{(CH}_3)_2\\text{CH(Br)C}=\\text{C(Cl)CH}_2\\text{OCH}_3$
- **Left Carbon**:
  - $-\\text{Br}$ ($Z = 35$): **Priority 1**
  - $-\\text{CH(CH}_3)_2$ ($Z = 6$): **Priority 2**
- **Right Carbon**:
  - $-\\text{Cl}$ ($Z = 17$): **Priority 1**
  - $-\\text{CH}_2\\text{OCH}_3$ ($Z = 6$): **Priority 2**
- Relationship: Priority 1 groups ($-\\text{Br}$ and $-\\text{Cl}$) are on the same side.
- **Stereodescriptor**: ***(Z)***.

---

### Part 2: Bromination of *(E)*-2-Butene
*(E)*-2-Butene has anti methyl groups.
1. **Bromonium Ion Formation**: Addition of $\\text{Br}^+$ to either face generates a symmetric cyclic bromonium ion with trans methyl groups.
2. **Backside Ring Opening by $\\text{Br}^-$**:
   - Attack at C2: inverts configuration at C2, leaving C3 with retention.
   - Attack at C3: inverts configuration at C3, leaving C2 with retention.
3. Both attack pathways produce the identical product:
   $$(2R, 3S)\\text{-2,3-dibromobutane}$$
   Because the molecule possesses an internal plane of symmetry ($\\sigma$), it is an optically inactive ***meso* compound**!

---

### Part 3: Bromination of *(Z)*-2-Butene
*(Z)*-2-Butene has syn methyl groups.
1. Addition of $\\text{Br}^+$ yields a *cis*-bromonium ion.
2. Backside attack of $\\text{Br}^-$:
   - Attack at C2 produces $(2R, 3R)$-2,3-dibromobutane ($50\\%$).
   - Attack at C3 produces $(2S, 3S)$-2,3-dibromobutane ($50\\%$).
3. The product is a **racemic pair $(\\pm)$-2,3-dibromobutane** ($50:50$ enantiomer mixture) that is optically inactive through external compensation."""
            },
            {
                "id": "prob3_2",
                "difficulty": "intermediate",
                "difficultyLabel": "Intermediate Level",
                "title": "Problem 3.2: Hydration Regiochemical & Skeletal Divergence in 3,3-Dimethyl-1-butene",
                "question": """3,3-Dimethyl-1-butene (neohexene, $(\\text{CH}_3)_3\\text{C}-\\text{CH}=\\text{CH}_2$) is subjected to three distinct hydration protocols:
- Reaction A: $50\\% \\; \\text{H}_2\\text{SO}_4 / \\text{H}_2\\text{O}$ at $60^\\circ\\text{C}$
- Reaction B: 1. $\\text{Hg(OAc)}_2, \\text{H}_2\\text{O}$ / THF  2. $\\text{NaBH}_4, \\text{NaOH}$
- Reaction C: 1. $\\text{BH}_3 \\cdot \\text{THF}$  2. $\\text{H}_2\\text{O}_2, \\text{NaOH}$

1. Draw the skeletal structure and provide the IUPAC systematic name of the major alcohol product formed in each of the three reactions.
2. For Reaction A, write the complete step-by-step mechanism with curved arrows, detailing the formation of the initial secondary carbocation, the driving force for the subsequent 1,2-methyl shift, and the nucleophilic trapping step.
3. Explain why Reaction B avoids skeletal rearrangement despite generating a Markovnikov alcohol product.""",
                "solution": """### Part 1: Major Alcohol Products & Systematic Names

1. **Reaction A (Acid-Catalyzed Hydration)**:
   - Product: **2,3-Dimethylbutan-2-ol** (Rearranged tertiary alcohol)
   - Structure: $(\\text{CH}_3)_2\\text{C(OH)}-\\text{CH}(\\text{CH}_3)_2$
2. **Reaction B (Oxymercuration-Demercuration)**:
   - Product: **3,3-Dimethylbutan-2-ol** (Unrearranged Markovnikov secondary alcohol)
   - Structure: $(\\text{CH}_3)_3\\text{C}-\\text{CH(OH)}-\\text{CH}_3$
3. **Reaction C (Hydroboration-Oxidation)**:
   - Product: **3,3-Dimethylbutan-1-ol** (Anti-Markovnikov primary alcohol)
   - Structure: $(\\text{CH}_3)_3\\text{C}-\\text{CH}_2-\\text{CH}_2\\text{OH}$

---

### Part 2: Mechanism of Reaction A (Acid-Catalyzed Rearrangement)
1. **Protonation**:
   The $\\pi$ electrons of neohexene attack $\\text{H}_3\\text{O}^+$, protonating the terminal methylene carbon:
   $$(\\text{CH}_3)_3\\text{C}-\\text{CH}=\\text{CH}_2 + \\text{H}^+ \\longrightarrow (\\text{CH}_3)_3\\text{C}-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}_3 + \\text{H}_2\\text{O}$$
   Forms a secondary ($2^\\circ$) carbocation with 6 hyperconjugative $\\alpha$-hydrogens.
2. **1,2-Methyl (Wagner-Meerwein) Shift**:
   The adjacent quaternary carbon bears three methyl groups. One methyl group migrates with its bonding pair of electrons to the cationic center:
   $$(\\text{CH}_3)_3\\text{C}-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}_3 \\longrightarrow (\\text{CH}_3)_2\\stackrel{\\oplus}{\\text{C}}-\\text{CH}(\\text{CH}_3)_2$$
   *Driving Force*: Converts an energetic $2^\\circ$ carbocation into an immensely stable tertiary ($3^\\circ$) carbocation stabilized by 7 hyperconjugative $\\alpha$-hydrogens.
3. **Nucleophilic Attack & Deprotonation**:
   Water captures the $3^\\circ$ carbocation:
   $$(\\text{CH}_3)_2\\stackrel{\\oplus}{\\text{C}}-\\text{CH}(\\text{CH}_3)_2 + \\text{H}_2\\text{O} \\longrightarrow (\\text{CH}_3)_2\\text{C}(\\stackrel{\\oplus}{\\text{O}}\\text{H}_2)-\\text{CH}(\\text{CH}_3)_2 \\xrightarrow{-\\text{H}^+} (\\text{CH}_3)_2\\text{C(OH)}-\\text{CH}(\\text{CH}_3)_2$$

---

### Part 3: Why Reaction B Avoids Rearrangement
In oxymercuration, electrophilic attack by $\\text{Hg(OAc)}^+$ produces a **cyclic mercurinium ion** (a bridged three-membered ring). 
Because the mercury atom shares its lone pair with both carbons, the system never forms a free, open carbocation with an empty $p$-orbital. The activation barrier for a 1,2-methyl shift in a bridged cyclic halonium/mercurinium system is prohibitively high ($>100\\text{ kJ/mol}$), forcing water to attack the secondary carbon directly."""
            },
            {
                "id": "prob3_3",
                "difficulty": "advanced",
                "difficultyLabel": "Advanced Level",
                "title": "Problem 3.3: Ozonolysis Structure Elucidation of Bicyclic Natural Products",
                "question": """A natural monoterpene hydrocarbon **A** ($\\text{C}_{10}\\text{H}_{16}$) is isolated from pine oil.
1. Calculate the Degree of Unsaturation (IHD) of Compound **A**.
2. Catalytic hydrogenation of **A** over platinum absorbs exactly one mole of $\\text{H}_2$ to yield hydrocarbon **B** ($\\text{C}_{10}\\text{H}_{18}$). What does this reveal about the rings and double bonds in **A**?
3. Ozonolysis of **A** followed by reductive workup with dimethyl sulfide yields a single dialdehyde-ketone compound **C** with molecular formula $\\text{C}_{10}\\text{H}_{16}\\text{O}_2$. Treatment of Compound **C** with Tollens' reagent produces a silver mirror, confirming an aldehyde group, and spectroscopic analysis shows it contains a cyclopentane ring with a methyl ketone and an ethanal side-chain.
   - Deduce the complete structure of Compound **A** ($\alpha$-pinene vs $\beta$-pinene vs sabinene vs camphene).
   - Write the complete balanced reaction sequence for the ozonolysis of Compound **A**.""",
                "solution": """### Part 1: Degree of Unsaturation of Compound A
Formula: $\\text{C}_{10}\\text{H}_{16}$.
$$\\text{IHD} = c - \\frac{h}{2} + 1 = 10 - \\frac{16}{2} + 1 = 10 - 8 + 1 = \\mathbf{3}$$
Compound **A** possesses 3 degrees of unsaturation (sum of rings and $\\pi$ bonds = 3).

---

### Part 2: Hydrogenation Analysis
Compound **A** absorbs exactly **one mole of $\\text{H}_2$** to give $\\text{C}_{10}\\text{H}_{18}$ (IHD = $10 - 9 + 1 = 2$).
- Number of $\\pi$ bonds = **1**
- Total degrees of unsaturation = 3
- Number of rings = $3 - 1 = \\mathbf{2}$
Compound **A** is a **bicyclic alkene** containing two fused or bridged rings and one double bond!

---

### Part 3: Ozonolysis Analysis & Structure Identification
Ozonolysis followed by reductive cleavage cleaves the double bond into two carbonyl groups.
Notice that the product **C** has the formula $\\text{C}_{10}\\text{H}_{16}\\text{O}_2$:
- The carbon count is still **10**! The molecule was **not cleaved into two separate fragments**.
- This proves unequivocally that the double bond is **internal to a ring** (an endocyclic double bond).
- If the double bond were exocyclic (as in $\\beta$-pinene), ozonolysis would have cleaved off formaldehyde ($\\text{CH}_2\\text{O}$), reducing the main product to $\\text{C}_9$.

The endocyclic bicyclic terpene with formula $\\text{C}_{10}\\text{H}_{16}$ containing a 4-membered bridge and a 6-membered ring is **$\\alpha$-Pinene** (2,6,6-trimethylbicyclo[3.1.1]hept-2-ene).
Ozonolysis cleaves the endocyclic double bond of $\\alpha$-pinene to generate **pinonic aldehyde** (2-(4-acetyl-2,2-dimethylcyclobutyl)ethanal), retaining all 10 carbons with one keto and one aldehydo functional group.
- **Identity of Compound A**: **$\\alpha$-Pinene**."""
            },
            {
                "id": "prob3_4",
                "difficulty": "honors",
                "difficultyLabel": "Honors / Olympiad Proof",
                "title": "Problem 3.4: Stereoelectronic Proof of Anti-Elimination in Menthyl vs Neomenthyl Chlorides",
                "question": """Menthyl chloride and Neomenthyl chloride are diastereomeric 2-isopropyl-5-methylcyclohexyl chlorides.
- **Menthyl Chloride**: $(1R, 2S, 5R)$-2-isopropyl-5-methylchlorocyclohexane. In its most stable chair conformation, all three substituents (isopropyl at C2, methyl at C5, and chloro at C1) occupy **equatorial positions**.
- **Neomenthyl Chloride**: $(1S, 2S, 5R)$-2-isopropyl-5-methylchlorocyclohexane. In its most stable chair conformation, the bulky isopropyl and methyl groups are equatorial, while the chloro group is **axial**.

Both diastereomers are subjected to $E2$ dehydrohalogenation using sodium ethoxide in ethanol at $80^\\circ\\text{C}$.
1. Neomenthyl chloride reacts rapidly ($t_{1/2} \\approx 10\\text{ minutes}$) to yield predominantly 2-menthene ($75\\%$, Zaitsev product) and 3-menthene ($25\\%$).
2. Menthyl chloride reacts exceedingly slowly ($t_{1/2} \\approx 40\\text{ hours}$, 240× slower!) and yields exclusively 2-menthene ($100\\%$, Hofmann product), with **zero formation of 3-menthene**.
Using chair conformations and Newman projections, provide a complete stereoelectronic proof explaining:
- Why menthyl chloride must flip into an energetically unfavorable diaxial chair to eliminate.
- Why menthyl chloride forms exclusively the less-substituted Hofmann alkene.
- Why neomenthyl chloride reacts 240× faster and obeys Zaitsev's rule.""",
                "solution": """### Stereoelectronic Proof of E2 Elimination in Menthyl Diastereomers

The fundamental requirement of the $E2$ mechanism is a strict **anti-periplanar alignment** between the $\\beta$-hydrogen and the leaving group ($\\text{H}-\\text{C}_\\beta-\\text{C}_\\alpha-\\text{Cl}$ dihedral angle $\\phi = 180^\\circ$).
In a cyclohexane ring, an anti-periplanar relationship between adjacent carbons can occur **only when both the leaving group and the $\\beta$-hydrogen are DIAXIAL (trans-diaxial)**. An equatorial leaving group can NEVER achieve a $180^\\circ$ dihedral angle with any $\\beta$-hydrogen!

---

### Case 1: Neomenthyl Chloride (Fast, Zaitsev Product)
In neomenthyl chloride, the chlorine atom is **axial** in the global minimum chair conformation:
- C1: Chlorine is **axial** (pointing down).
- C2: Isopropyl is **equatorial** (pointing up). The $\\beta$-hydrogen at C2 is **axial** (pointing up).
- C6: One $\\beta$-hydrogen at C6 is **axial** (pointing up).

Notice that in this predominant chair conformation:
1. The axial chlorine at C1 is trans-diaxial to the tertiary $\\beta$-hydrogen at C2 ($\phi = 180^\\circ$).
2. The axial chlorine at C1 is also trans-diaxial to the secondary axial $\\beta$-hydrogen at C6 ($\phi = 180^\\circ$).

Because an anti-periplanar hydrogen is immediately available at the more substituted C2 position, elimination proceeds directly from the major ground-state conformer with an exceptionally low activation barrier, forming the more substituted, thermodynamically stable **3-menthene (Zaitsev product, $75\\%$)** rapidly ($t_{1/2} \\sim 10\\text{ min}$)!

---

### Case 2: Menthyl Chloride (Slow, Hofmann Product)
In menthyl chloride, all three substituents are **equatorial** in the ground-state chair:
- The chlorine atom is **equatorial**.
- Because chlorine is equatorial, **zero trans-diaxial eliminations can take place from this conformation**!

To react, menthyl chloride must undergo a high-energy chair-flip into an inverted chair conformer where:
- The chlorine becomes **axial**.
- Both the bulky isopropyl group and the methyl group are forced into **axial** positions!
The thermodynamic penalty for this diaxial flipping is:
$$\\Delta G^\\circ_{\\text{flip}} \\approx A(\\text{i-Pr}) + A(\\text{Me}) + A(\\text{Cl}) = 9.2 + 7.3 + 2.2 = \\mathbf{+18.7\\text{ kJ/mol}}$$
By the Boltzmann distribution, less than $0.05\\%$ of the molecules exist in this reactive chair conformation at any instant!

Furthermore, in this inverted reactive conformer:
- At C2: The isopropyl group is axial (pointing down). Therefore, the hydrogen at C2 is **equatorial**! 
- Dihedral angle between C1 axial chlorine and C2 equatorial hydrogen is $\\phi = 60^\\circ$ (gauche).
- **Anti-periplanar elimination toward C2 is strictly stereoelectronically forbidden!**
- At C6: The only anti-periplanar $\\beta$-hydrogen resides at C6 (axial, pointing up).

Therefore:
1. Elimination can proceed **only toward C6**, generating exclusively the less-substituted **2-menthene (Hofmann product, $100\\%$)**!
2. The reaction is **240× slower** because the effective reactant population is suppressed by the $+18.7\\text{ kJ/mol}$ conformational flipping barrier.
This is one of the most famous and definitive stereoelectronic proofs in physical organic chemistry!"""
            }
        ]
    }

def get_unit_4():
    return {
        "id": "unit4",
        "unitId": "unit4-org1",
        "number": 4,
        "unitNumber": 4,
        "title": "Unit 4: Conjugated Systems, Dienes, Pericyclic Reactivity & Alkynes",
        "description": "Rigorous exploration of conjugated dienes, kinetic vs thermodynamic addition control, Diels-Alder [4+2] cycloaddition FMO theory, Alder endo rule, diene elastomers, alkyne electronic structure and acidity, terminal acetylide alkylations, hydration tautomerism, and stereoselective reductions.",
        "leadSummary": "Comprehensive coverage of conjugated dienes, 1,2- vs 1,4-electrophilic additions, Diels-Alder pericyclic reactions, FMO symmetry, alkyne synthesis, organocopper Corey-House couplings, and reduction stereochemistry.",
        "simulations": ["sim_chem_diels_alder_fmo_cycloaddition"],
        "sections": [
            {
                "id": "sec4_1",
                "secNumber": "§4.1",
                "title": "Conjugated Dienes: Orbital Overlap & Resonance Energy",
                "heading": "Conjugated Dienes: Orbital Overlap & Resonance Energy",
                "content": """Dienes are hydrocarbons containing two carbon-carbon double bonds. They are categorized into three structurally distinct classes:
1. **Isolated Dienes**: Double bonds separated by two or more $sp^3$ carbons (e.g., 1,4-pentadiene). The $\\pi$ bonds act as independent, non-interacting chromophores.
2. **Cumulated Dienes (Allenes)**: Double bonds share a central $sp$ carbon (e.g., propadiene, $\\text{CH}_2=\\text{C}=\\text{CH}_2$). The two $\\pi$ bonds lie in mutually perpendicular planes ($90^\\circ$), generating axial chirality in suitably substituted allenes.
3. **Conjugated Dienes**: Double bonds separated by a single $sp^2-sp^2$ $\\sigma$ bond (e.g., 1,3-butadiene). The four contiguous $2p_z$ orbitals overlap continuously across all four carbon atoms.

### The Special Properties of 1,3-Butadiene
- **Shortened Central C-C Bond**: The central $\\text{C}_2-\\text{C}_3$ single bond measures only $146.3\\text{ pm}$, compared to $153.8\\text{ pm}$ in ethane. This contraction arises from overlap between $sp^2-sp^2$ hybrids (higher $s$-character) and partial $\\pi$ double-bond character.
- **Resonance Stabilization Energy**: Measured from heat of hydrogenation data:
  $$\\Delta H_{\\text{hydro}}^\\circ(1\\text{-butene}) = -126.8\\text{ kJ/mol}$$
  For two isolated double bonds, one expects $2 \\times (-126.8) = -253.6\\text{ kJ/mol}$.
  The experimental heat of hydrogenation for 1,3-butadiene is only $-238.9\\text{ kJ/mol}$.
  The difference represents **resonance stabilization energy**:
  $$E_{\\text{res}} = -238.9 - (-253.6) = \\mathbf{+14.7\\text{ kJ}\\cdot\\text{mol}^{-1}} \\tag{4.1}$$

---

### Hückel Molecular Orbitals of 1,3-Butadiene

Linear combination of the four $2p_z$ atomic orbitals produces four delocalized molecular orbitals:
$$\\begin{aligned}
\\Psi_1 &= 0.372\\phi_1 + 0.602\\phi_2 + 0.602\\phi_3 + 0.372\\phi_4 \\quad (E = \\alpha + 1.618\\beta, \\; 0\\text{ nodes}) \\\\
\\Psi_2 &= 0.602\\phi_1 + 0.372\\phi_2 - 0.372\\phi_3 - 0.602\\phi_4 \\quad (E = \\alpha + 0.618\\beta, \\; 1\\text{ node, HOMO}) \\\\
\\Psi_3 &= 0.602\\phi_1 - 0.372\\phi_2 - 0.372\\phi_3 + 0.602\\phi_4 \\quad (E = \\alpha - 0.618\\beta, \\; 2\\text{ nodes, LUMO}) \\\\
\\Psi_4 &= 0.372\\phi_1 - 0.602\\phi_2 + 0.602\\phi_3 - 0.372\\phi_4 \\quad (E = \\alpha - 1.618\\beta, \\; 3\\text{ nodes})
\\end{aligned} \\tag{4.2}$$
The four $\\pi$ electrons occupy $\\Psi_1^2 \\Psi_2^2$, resulting in a total $\\pi$ energy of $E_\\pi = 4\\alpha + 4.472\\beta$, yielding an exact Hückel delocalization energy of $0.472|\\beta| \\approx 15\\text{ kJ/mol}$.""",
                "simulations": []
            },
            {
                "id": "sec4_2",
                "secNumber": "§4.2",
                "title": "Electrophilic Addition to Dienes: 1,2- vs 1,4-Regiochemistry",
                "heading": "Electrophilic Addition to Dienes: 1,2- vs 1,4-Regiochemistry",
                "content": """When 1,3-butadiene reacts with hydrogen chloride ($\\text{HCl}$) or bromine ($\\text{Br}_2$), two isomeric addition products are formed:
$$\\text{CH}_2=\\text{CH}-\\text{CH}=\\text{CH}_2 + \\text{HBr} \\longrightarrow \\text{CH}_3-\\text{CH(Br)}-\\text{CH}=\\text{CH}_2 \\; (1,2) + \\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_2\\text{Br} \\; (1,4) \\tag{4.3}$$

### Mechanism: The Resonance-Delocalized Allylic Cation

1. Protonation occurs at the terminal carbon (C1) to form a resonance-stabilized **allylic carbocation**:
   $$\\text{CH}_3-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}=\\text{CH}_2 \\longleftrightarrow \\text{CH}_3-\\text{CH}=\\text{CH}-\\stackrel{\\oplus}{\\text{C}}\\text{H}_2 \\tag{4.4}$$
2. The bromide nucleophile can attack at either C2 (yielding the 1,2-adduct) or C4 (yielding the 1,4-adduct).

---

### Kinetic vs Thermodynamic Control

The product distribution is exceptionally sensitive to reaction temperature:
- **At $-80^\\circ\\text{C}$ (Kinetic Control)**: The **1,2-adduct** dominates ($80\\%$ 1,2 vs $20\\%$ 1,4).
- **At $+40^\\circ\\text{C}$ (Thermodynamic Control)**: The **1,4-adduct** dominates ($15\\%$ 1,2 vs $85\\%$ 1,4).

#### Physical Rationale:
1. **Kinetic Control**: At low temperatures, molecules do not possess sufficient thermal energy to overcome high reverse activation barriers; reactions are irreversible. The 1,2-adduct forms faster because the bromide ion is generated directly adjacent to C2 (proximity effect / ion-pair proximity), and C2 bears greater partial positive charge in the unsymmetrical allylic cation.
2. **Thermodynamic Control**: At elevated temperatures, the addition becomes reversible ($E_a$ for ionization of allylic bromide is accessible). An equilibrium is established between the two products. The **1,4-adduct is an internal, disubstituted alkene**, which is thermodynamically more stable than the terminal, monosubstituted 1,2-adduct by approximately $12\\text{ kJ/mol}$. Under equilibrium conditions, the thermodynamically most stable product predominates.""",
                "simulations": []
            },
            {
                "id": "sec4_3",
                "secNumber": "§4.3",
                "title": "The Diels-Alder [4+2] Cycloaddition: FMO Theory & The Endo Rule",
                "heading": "The Diels-Alder [4+2] Cycloaddition: FMO Theory & The Endo Rule",
                "content": """Discovered in 1928 by Otto Diels and Kurt Alder (Nobel Prize 1950), the Diels-Alder reaction is a concerted $[4+2]$ pericyclic cycloaddition between a conjugated diene ($4\\pi$ electrons) and an alkene/alkyne (**dienophile**, $2\\pi$ electrons) to form a six-membered cyclohexene ring:
$$\\text{Diene} + \\text{Dienophile} \\xrightarrow{\\Delta} \\text{Cyclohexene} \\tag{4.5}$$

### Essential Structural & Mechanistic Principles

1. **Mandatory $s$-cis Conformation**:
   The diene must adopt the **$s$-cis conformation** (dihedral angle $0^\\circ$) to bring the terminal C1 and C4 $p$-orbitals close enough ($< 3.0\\text{ \u00c5}$) to interact simultaneously with the dienophile. Dienes permanently locked in the $s$-cis conformation (such as cyclopentadiene) react with lightning speed, whereas dienes locked in the $s$-trans conformation (such as $(2E,4E)$-hexadiene) are completely unreactive.
2. **Frontier Molecular Orbital (FMO) Symmetry**:
   In a normal-electron-demand Diels-Alder reaction, electron flow occurs from the **HOMO of the electron-rich diene** to the **LUMO of the electron-poor dienophile**:
   - Diene HOMO ($\\Psi_2$): Terminal lobes at C1 and C4 have opposite signs ($+ - - +$).
   - Dienophile LUMO ($\\pi^*$): Lobes have opposite signs ($+ -$).
   As shown in the simulation, bringing the reactants together in a suprafacial-suprafacial approach produces **constructive, in-phase orbital overlap at both termini simultaneously**, making the reaction thermally allowed by the Woodward-Hoffmann rules.
3. **The Alder Endo Rule**:
   When a dienophile bears an electron-withdrawing carbonyl or unsaturated group (such as maleic anhydride), two transition states are stereochemically possible:
   - **Endo Approach**: The substituent points toward the developing cyclohexene $\\pi$ bond.
   - **Exo Approach**: The substituent points away from the diene.
   The **endo isomer is formed as the major kinetic product** because **secondary orbital overlap** between the $\\pi^*$ orbitals of the electron-withdrawing carbonyl group and the interior C2/C3 carbons of the diene lowers the activation energy of the endo transition state.""",
                "simulations": ["sim_chem_diels_alder_fmo_cycloaddition"]
            },
            {
                "id": "sec4_4",
                "secNumber": "§4.4",
                "title": "1,3-Diene Polymerizations & Synthetic Elastomers",
                "heading": "1,3-Diene Polymerizations & Synthetic Elastomers",
                "content": """Polymerization of conjugated dienes produces commercially crucial synthetic rubbers and elastomers:
$$n\\,\\text{CH}_2=\\text{C(R)}-\\text{CH}=\\text{CH}_2 \\longrightarrow -[\\text{CH}_2-\\text{C(R)}=\\text{CH}-\\text{CH}_2]_n- \\tag{4.6}$$

### 1,4-cis vs 1,4-trans Stereoisomers
- **Natural Rubber (*cis*-1,4-polyisoprene)**: Isolated from *Hevea brasiliensis*. Because all double bonds have the *cis* configuration, the polymer chains adopt kinked, coiling conformations that prevent close crystal packing. When stretched, chains align, and when released, entropy ($\Delta S > 0$) snaps them back into coiled states (**elasticity**).
- **Gutta-Percha (*trans*-1,4-polyisoprene)**: All double bonds have the rigid *trans* configuration. The linear chains pack tightly into crystalline domains, producing a hard, non-elastic thermoplastic historically used to insulate undersea telegraph cables and for dental root canals.
- **Neoprene (Polychloroprene)**: Polymerization of 2-chloro-1,3-butadiene generates a synthetic elastomer highly resistant to gasoline, oil, and ozone degradation.""",
                "simulations": []
            },
            {
                "id": "sec4_5",
                "secNumber": "§4.5",
                "title": "Alkynes: Electronic Structure, $sp$ Acidity & Synthesis",
                "heading": "Alkynes: Electronic Structure, $sp$ Acidity & Synthesis",
                "content": """Alkynes contain a carbon-carbon triple bond ($\\text{C}\\equiv\\text{C}$), corresponding to the molecular formula $\\text{C}_n\\text{H}_{2n-2}$. Each alkyne carbon is $sp$ hybridized, forming one collinear $\\sigma$ bond along the internuclear axis and utilizing two mutually orthogonal $2p_y$ and $2p_z$ orbitals to establish a cylindrical sheath of $\\pi$ electron density.

### The Extraordinary Acidity of Terminal Alkynes

Hydrocarbons are typically extraordinarily weak Brønsted acids:
- Ethane ($\\text{CH}_3\\text{CH}_3$, $sp^3$): $pK_a \\approx 50$
- Ethylene ($\\text{CH}_2=\\text{CH}_2$, $sp^2$): $pK_a \\approx 44$
- **Acetylene ($\\text{HC}\\equiv\\text{CH}$, $sp$)**: **$pK_a \\approx 25$**

Acetylene is $10^{25}$ times more acidic than ethane!
**Quantum Explanation**: The conjugate base (an **acetylide carbanion**, $\\text{R}-\\text{C}\\equiv\\text{C}:^-$) houses its non-bonding lone pair in an $sp$ hybrid orbital possessing $50\\%$ $s$-character, compared to $33\\%$ in $sp^2$ and $25\\%$ in $sp^3$. Because $s$-orbitals have non-zero probability density at the nucleus, electrons in $sp$ hybrids are held significantly closer to the positive nuclear charge, stabilizing the conjugate base.

#### Synthetic Utility of Sodium Acetylides
Terminal alkynes are quantitatively deprotonated by strong bases such as sodium amide in liquid ammonia:
$$\\text{R}-\\text{C}\\equiv\\text{C}-\\text{H} + \\text{NaNH}_2 \\xrightarrow{\\text{liq. } \\text{NH}_3} \\text{R}-\\text{C}\\equiv\\text{C}^- \\text{Na}^+ + \\text{NH}_3 \\tag{4.7}$$
The resulting sodium acetylide is a powerful nucleophile that attacks primary alkyl halides via $S_N2$ displacement to construct longer carbon chains:
$$\\text{R}-\\text{C}\\equiv\\text{C}^- + \\text{R}'-\\text{CH}_2-\\text{Br} \\longrightarrow \\text{R}-\\text{C}\\equiv\\text{C}-\\text{CH}_2\\text{R}' + \\text{Br}^- \\tag{4.8}$$""",
                "simulations": []
            },
            {
                "id": "sec4_6",
                "secNumber": "§4.6",
                "title": "Reactions of Alkynes: Hydration, Tautomerism & Hydroboration",
                "heading": "Reactions of Alkynes: Hydration, Tautomerism & Hydroboration",
                "content": """### 1. Mercury(II)-Catalyzed Hydration (Markovnikov Addition)
- **Reagents**: Aqueous sulfuric acid and mercury(II) sulfate ($\\text{H}_2\\text{SO}_4, \\text{HgSO}_4, \\text{H}_2\\text{O}$).
- **Mechanism**: Electrophilic addition of $\\text{Hg}^{2+}$ generates a mercurinium intermediate, which is attacked by water according to Markovnikov's rule to yield an **enol (alkenyl alcohol)**.
- **Keto-Enol Tautomerism**: The enol rapidly isomerizes into a **methyl ketone**:
  $$\\text{R}-\\text{C}\\equiv\\text{CH} + \\text{H}_2\\text{O} \\xrightarrow{\\text{Hg}^{2+}, \\text{H}^+} \\left[ \\text{R}-\\text{C(OH)}=\\text{CH}_2 \\right] \\rightleftharpoons \\text{R}-\\text{C}(=\\text{O})-\\text{CH}_3 \\tag{4.9}$$
  The equilibrium overwhelmingly favors the ketone ($\\Delta G^\\circ \\approx -50\\text{ kJ/mol}$) due to the colossal thermodynamic strength of the carbonyl $\\text{C}=\\text{O}$ double bond ($745\\text{ kJ/mol}$) relative to the $\\text{C}=\\text{C}$ bond ($614\\text{ kJ/mol}$).

---

### 2. Hydroboration-Oxidation of Terminal Alkynes (Anti-Markovnikov)
To prevent double hydroboration across the triple bond, hindered dialkylboranes such as **disiamylborane (Sia$_2$BH)** or **9-BBN** are employed:
1. Addition of Sia$_2$BH places boron regioselectively at the less-hindered terminal carbon to form an alkenylborane.
2. Alkaline hydrogen peroxide oxidation produces an aldehyde enol, which immediately tautomerizes into an **aldehyde**:
   $$\\text{R}-\\text{C}\\equiv\\text{CH} \\xrightarrow{1.\\; \\text{Sia}_2\\text{BH} \\quad 2.\\; \\text{H}_2\\text{O}_2, \\text{NaOH}} \\left[ \\text{R}-\\text{CH}=\\text{CH}-\\text{OH} \\right] \\rightleftharpoons \\text{R}-\\text{CH}_2-\\text{CH}=\\text{O} \\tag{4.10}$$""",
                "simulations": []
            },
            {
                "id": "sec4_7",
                "secNumber": "§4.7",
                "title": "Stereoselective Reductions & Organocopper Cross-Coupling",
                "heading": "Stereoselective Reductions & Organocopper Cross-Coupling",
                "content": """Alkynes can be selectively reduced to either *(cis)*- or *(trans)*-alkenes using orthogonal chemical reagents:

### 1. Syn-Reduction to *(Z)*-Alkenes: The Lindlar Catalyst
- **Reagent**: Palladium deposited on calcium carbonate poisoned with lead acetate and quinoline ($\\text{H}_2, \\text{Pd/CaCO}_3, \\text{Pb(OAc)}_2$).
- **Mechanism**: Heterogeneous catalytic hydrogenation requires both hydrogen atoms to be delivered simultaneously from the metallic surface to the same face of the coordinated alkyne.
- **Outcome**: **Stereospecific synthesis of *(Z)*-alkenes (cis-alkenes)**.

---

### 2. Anti-Reduction to *(E)*-Alkenes: Dissolving Metal Reduction
- **Reagent**: Sodium or lithium metal in liquid ammonia ($\\text{Na / liq. } \\text{NH}_3$) at $-33^\\circ\\text{C}$.
- **Mechanism (Single Electron Transfer)**:
  1. Solvated electrons ($e^-_{\\text{am}}$) reduce the alkyne to a radical anion.
  2. The radical anion inverts rapidly into the **trans-radical anion** to minimize mutual Coulomb repulsion between the lone pair and radical lobe.
  3. Protonation by ammonia yields a trans-alkenyl radical.
  4. Second electron transfer and protonation yield the trans-alkene.
- **Outcome**: **Stereospecific synthesis of *(E)*-alkenes (trans-alkenes)**.

---

### Chemistry of Alkenyl Halides & Corey-House Coupling
Alkenyl halides ($\\text{R}-\\text{CH}=\\text{CH}-\\text{X}$) are inert to standard $S_N2$ displacement due to $sp^2$ steric and electronic shielding. However, they couple smoothly with lithium dialkylcuprates (Gilman reagents, $\\text{R}'_2\\text{CuLi}$) with **complete retention of alkene stereochemistry**:
$$\\text{R}-\\text{CH}=\\text{CH}-\\text{I} \\; (E) + \\text{R}'_2\\text{CuLi} \\longrightarrow \\text{R}-\\text{CH}=\\text{CH}-\\text{R}' \\; (E) + \\text{R}'\\text{Cu} + \\text{LiI} \\tag{4.11}$$""",
                "simulations": []
            }
        ],
        "problems": [
            {
                "id": "prob4_1",
                "difficulty": "foundational",
                "difficultyLabel": "Foundational Level",
                "title": "Problem 4.1: Kinetic vs Thermodynamic Control in 1,3-Butadiene Hydrobromination",
                "question": """1,3-Butadiene is treated with one equivalent of anhydrous hydrogen bromide ($\\text{HBr}$).
1. Write the structures of the 1,2-addition and 1,4-addition products.
2. At $-80^\\circ\\text{C}$, the reaction yields $80\\%$ 3-bromobut-1-ene (1,2-adduct) and $20\\%$ 1-bromobut-2-ene (1,4-adduct). At $+40^\\circ\\text{C}$, the distribution shifts to $15\\%$ 3-bromobut-1-ene and $85\\%$ 1-bromobut-2-ene.
   - Construct a fully labeled reaction coordinate diagram showing both pathways from the intermediate allylic carbocation.
   - Explain why the 1,2-adduct has a lower activation barrier $\\Delta G^\\ddagger$.
   - Explain why the 1,4-adduct has a lower standard free energy $G^\\circ$.
3. When pure 3-bromobut-1-ene is warmed to $+40^\\circ\\text{C}$ in the presence of trace acid, it isomerizes into an $85:15$ mixture favoring 1-bromobut-2-ene. Prove that this demonstrates microscopic reversibility and thermodynamic control.""",
                "solution": """### Part 1: Addition Product Structures
- **1,2-Adduct**: **3-Bromobut-1-ene** ($\\text{CH}_3-\\text{CH(Br)}-\\text{CH}=\\text{CH}_2$)
- **1,4-Adduct**: **1-Bromobut-2-ene** ($\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_2\\text{Br}$)

---

### Part 2: Reaction Coordinate Energetics

#### 1. Why the 1,2-adduct has lower activation energy ($\Delta G^\ddagger_{1,2} < \Delta G^\ddagger_{1,4}$):
Protonation of 1,3-butadiene produces an allylic carbocation with an intimate bromide counter-ion:
$$[\\text{CH}_3-\\stackrel{\\oplus}{\\text{C}}\\text{H}-\\text{CH}=\\text{CH}_2 \\longleftrightarrow \\text{CH}_3-\\text{CH}=\\text{CH}-\\stackrel{\\oplus}{\\text{C}}\\text{H}_2] \\; \\text{Br}^-$$
- **Proximity Effect**: The proton adds to C1, leaving the $\\text{Br}^-$ ion immediately adjacent to C2. Trapping at C2 requires minimal diffusion, proceeding with a very low activation barrier.
- **Charge Density**: In the unsymmetrical allylic cation, the secondary C2 position bears greater partial positive charge ($q \\approx +0.7$) than the primary C4 position ($q \\approx +0.3$). Electrostatic attraction directs the bromide faster to C2.

#### 2. Why the 1,4-adduct has lower thermodynamic free energy ($G^\circ_{1,4} < G^\circ_{1,2}$):
- The 1,2-adduct possesses a **terminal, monosubstituted alkene** (one alkyl substituent attached to the double bond).
- The 1,4-adduct possesses an **internal, disubstituted alkene** (two alkyl substituents attached to the double bond).
Because internal, substituted alkenes are thermodynamically stabilized by hyperconjugation and greater $sp^2-sp^3$ bond strength, the 1,4-adduct is more stable by approximately $\\Delta G^\\circ \\approx 12\\text{ kJ/mol}$.

---

### Part 3: Microscopic Reversibility & Thermal Equilibrium
At $+40^\\circ\\text{C}$, the thermal energy $k_B T$ is sufficient to overcome the activation barrier for the reverse ionization:
$$\\text{3-Bromobut-1-ene} \\rightleftharpoons [\\text{Allylic Cation}] + \\text{Br}^- \\rightleftharpoons \\text{1-Bromobut-2-ene}$$
Because ionization is reversible, the product distribution ceases to depend on the rates of formation and becomes strictly governed by the thermodynamic equilibrium constant:
$$K_{\\text{eq}} = \\frac{[1,4\\text{-adduct}]}{[1,2\\text{-adduct}]} = \\frac{85}{15} \\approx 5.67$$
$$\\Delta G^\\circ = -RT \\ln K_{\\text{eq}} = -(8.314) \\times (313.15) \\times \\ln(5.67) \\approx \\mathbf{-4.5\\text{ kJ/mol}}$$
Warming either pure isomer yields the identical $85:15$ equilibrium mixture, proving thermodynamic control."""
            },
            {
                "id": "prob4_2",
                "difficulty": "intermediate",
                "difficultyLabel": "Intermediate Level",
                "title": "Problem 4.2: Regiochemistry & Alder Endo Stereospecificity in Diels-Alder Additions",
                "question": """Consider the Diels-Alder cycloaddition of 2-methoxy-1,3-butadiene with methyl acrylate ($\\text{CH}_2=\\text{CH}-\\text{COOCH}_3$).
1. Deduce the major constitutional regioisomer (1,4-disubstituted vs 1,3-disubstituted cyclohexene) using resonance and partial charge analysis of both reactants.
2. When cyclopentadiene reacts with maleic anhydride at room temperature, only one diastereomer is isolated in $>99\\%$ yield.
   - Draw the 3D structures of the endo and exo transition states.
   - Explain the physical origin of the Alder endo rule using secondary orbital overlap arguments.
   - If the resulting endo adduct is heated to $200^\\circ\\text{C}$ for several hours, it equilibrates to predominantly the exo adduct. Explain this transformation.""",
                "solution": """### Part 1: Regiochemical Analysis

1. **Diene: 2-Methoxy-1,3-butadiene**:
   The methoxy group ($-\\text{OCH}_3$) is an electron-donating group ($+M$ by resonance). Resonance delocalization donates the oxygen lone pair into the diene $\\pi$-system:
   $$\\text{CH}_2=\\text{C(OCH}_3)-\\text{CH}=\\text{CH}_2 \\longleftrightarrow \\stackrel{\\ominus}{\\text{C}}\\text{H}_2-\\text{C}(\\stackrel{\\oplus}{\\text{O}}\\text{CH}_3)=\\text{CH}-\\text{CH}_2 \\longleftrightarrow \\text{CH}_2=\\text{C}(\\stackrel{\\oplus}{\\text{O}}\\text{CH}_3)-\\text{CH}-\\stackrel{\\ominus}{\\text{C}}\\text{H}_2$$
   The terminal C1 position bears substantial partial negative charge (larger HOMO coefficient).
2. **Dienophile: Methyl Acrylate**:
   The ester group ($-\\text{COOCH}_3$) is an electron-withdrawing group ($-M$). Resonance withdraws electron density onto the carbonyl oxygen:
   $$\\text{CH}_2=\\text{CH}-\\text{COOCH}_3 \\longleftrightarrow \\stackrel{\\oplus}{\\text{C}}\\text{H}_2-\\text{CH}=\\text{C(O}^-\\text{)OCH}_3$$
   The terminal $\\beta$-carbon bears substantial partial positive charge (larger LUMO coefficient).
3. **Matching Orbital Coefficients & Charges**:
   The nucleophilic C1 of the diene ($^{\\delta-}$ / large HOMO) bonds to the electrophilic $\\beta$-carbon of the dienophile ($^{\\delta+}$ / large LUMO).
   - This joins C1 of the diene to the terminal carbon of acrylate, placing the methoxy group at C1 and the carbomethoxy group at C4 of the cyclohexene ring.
   - **Major Regioisomer**: **Methyl 4-methoxycyclohex-3-enecarboxylate** (**1,4-disubstituted**, 'para'-like product).

---

### Part 2: The Alder Endo Rule & Secondary Orbital Overlap
In the reaction between cyclopentadiene and maleic anhydride:
- **Endo Transition State**: The anhydride carbonyl groups lie directly underneath the developing $\\pi$ bond of the cyclopentadiene framework.
- **Secondary Orbital Interaction**: The empty $\\pi^*$ orbitals of the carbonyl groups overlap constructively with the $p$-orbitals of the interior C2 and C3 carbons of the diene. Although no covalent bonds are formed between these atoms, this favorable secondary orbital overlap lowers the activation energy of the transition state by $\\sim 8 - 12\\text{ kJ/mol}$.
- **Exo Transition State**: The carbonyl groups point away into empty space, experiencing zero secondary orbital stabilization.
Consequently, the **endo adduct forms with $>99\\%$ kinetic selectivity** at room temperature.

---

### Part 3: Thermal Equilibration to Exo Product
At $200^\\circ\\text{C}$, the Diels-Alder reaction becomes **reversible (retro-Diels-Alder)**.
The endo adduct dissociates back into cyclopentadiene and maleic anhydride. In the endo adduct, the bulky anhydride ring suffers severe steric clash with the methylene bridge of the bicyclic norbornene framework. The exo adduct is free of this steric clash and is **thermodynamically more stable by $\\sim 6\\text{ kJ/mol}$**. Under prolonged heating, the system reaches thermodynamic equilibrium, accumulating the exo isomer."""
            },
            {
                "id": "prob4_3",
                "difficulty": "advanced",
                "difficultyLabel": "Advanced Level",
                "title": "Problem 4.3: Retrosynthetic Strategy & Alkyne-Based Multistep Synthesis",
                "question": """Devise an efficient multistep synthetic route to prepare *(2E,6Z)*-nona-2,6-diene starting exclusively from acetylene (ethyne), alkyl halides containing three or fewer carbons, and common inorganic reagents.
1. Perform a retrosynthetic disconnection of the target molecule back to alkyne and alkyl halide precursors.
2. Outline the forward synthesis step by step, specifying all reagents, reaction conditions, and intermediate structures.
3. Detail how the specific *(E)* and *(Z)* double-bond stereocenters are introduced with 100% stereocontrol.""",
                "solution": """### Part 1: Retrosynthetic Disconnection
Target: *(2E,6Z)*-Nona-2,6-diene (a 9-carbon diene with one trans and one cis double bond).
$$\\text{CH}_3-\\text{CH}\\stackrel{(E)}{=}\\text{CH}-\\text{CH}_2-\\text{CH}_2-\\text{CH}\\stackrel{(Z)}{=}\\text{CH}-\\text{CH}_2\\text{CH}_3$$

- **Disconnection 1**: The *(6Z)* double bond can be derived stereospecifically from a triple bond via **Lindlar catalytic hydrogenation** ($\\text{H}_2, \\text{Pd/CaCO}_3$).
- **Disconnection 2**: The *(2E)* double bond can be derived stereospecifically from a triple bond via **dissolving metal reduction** ($\\text{Na / liq. } \\text{NH}_3$).
- **Disconnection 3**: Carbon-carbon bond construction via sequential acetylide alkylation.

---

### Part 2: Step-by-Step Forward Synthesis

#### Phase 1: Construction of the internal diyne backbone
1. **Mono-alkylation of Acetylene**:
   $$\\text{H}-\\text{C}\\equiv\\text{C}-\\text{H} + \\text{NaNH}_2 \\xrightarrow{\\text{liq. } \\text{NH}_3} \\text{H}-\\text{C}\\equiv\\text{C}^- \\text{Na}^+$$
   $$\\text{H}-\\text{C}\\equiv\\text{C}^- \\text{Na}^+ + \\text{CH}_3\\text{CH}_2-\\text{Br} \\longrightarrow \\text{H}-\\text{C}\\equiv\\text{C}-\\text{CH}_2\\text{CH}_3 \\; (\\text{1-pentyne})$$
2. **Selective Hydrogenation to (Z)-Alkene**:
   $$\\text{H}-\\text{C}\\equiv\\text{C}-\\text{CH}_2\\text{CH}_3 \\dots$$
   *Alternative optimal route*: Build the 6Z bond first as a terminal building block:
   Treat 1-bromo-2-butyne (prepared from propyne alkylation) or couple 1-bromopropane:
   
Let's assemble systematically:
1. $\\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{H} + \\text{NaNH}_2 \\longrightarrow \\text{CH}_3-\\text{C}\\equiv\\text{C}^- \\text{Na}^+$
2. Treat with 1-bromo-3-chloropropane:
   $$\\text{CH}_3-\\text{C}\\equiv\\text{C}^- + \\text{Br}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-\\text{Cl} \\longrightarrow \\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-\\text{Cl}$$
3. Convert primary chloride to iodide via Finkelstein reaction ($\\text{NaI / acetone}$), then couple with sodium ethylacetylide:
   $$\\text{CH}_3\\text{CH}_2-\\text{C}\\equiv\\text{C}^- \\text{Na}^+ + \\text{I}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-\\text{C}\\equiv\\text{C}-\\text{CH}_3 \\longrightarrow \\text{CH}_3\\text{CH}_2-\\text{C}\\equiv\\text{C}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-\\text{C}\\equiv\\text{C}-\\text{CH}_3$$
4. **Differential Reduction**:
   - To differentiate the two triple bonds, synthesize the *(E)* fragment first:
     Reduce $\\text{CH}_3-\\text{C}\\equiv\\text{C}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-\\text{Cl}$ with $\\text{Na / liq. } \\text{NH}_3$ to generate the pure *(E)*-alkenyl chloride:
     $$\\text{CH}_3-\\text{CH}\\stackrel{(E)}{=}\\text{CH}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-\\text{Cl}$$
   - Convert to iodide with $\\text{NaI}$, then alkylate with sodium 1-butynyl carbanion:
     $$\\text{CH}_3-\\text{CH}\\stackrel{(E)}{=}\\text{CH}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-\\text{C}\\equiv\\text{C}-\\text{CH}_2\\text{CH}_3$$
   - Finally, perform stereoselective syn-reduction of the remaining triple bond using Lindlar catalyst:
     $$\\text{H}_2, \\text{Pd/CaCO}_3, \\text{quinoline} \\longrightarrow \\mathbf{\\text{CH}_3-\\text{CH}\\stackrel{(E)}{=}\\text{CH}-\\text{CH}_2\\text{CH}_2-\\text{CH}\\stackrel{(Z)}{=}\\text{CH}-\\text{CH}_2\\text{CH}_3}$$
   Target achieved with $100\\%$ stereocontrol!"""
            },
            {
                "id": "prob4_4",
                "difficulty": "honors",
                "difficultyLabel": "Honors / Olympiad Proof",
                "title": "Problem 4.4: Woodward-Hoffmann Orbital Correlation Proof for [4+2] vs [2+2] Cycloadditions",
                "question": """Using the Woodward-Hoffmann Conservation of Orbital Symmetry:
1. Construct the Frontier Molecular Orbital (FMO) symmetry correlation diagram for the thermal $[4+2]$ cycloaddition between ethylene and 1,3-butadiene.
   - Specify the symmetry planes preserved throughout the reaction path ($C_s$ or $C_{2v}$).
   - Prove that the ground-state electron configuration of the reactants correlates directly with the ground-state electron configuration of the product cyclohexene, proving why $[\\pi 4_s + \\pi 2_s]$ is thermally allowed.
2. Construct the corresponding orbital correlation diagram for the dimerization of two ethylene molecules to form cyclobutane ($[\\pi 2_s + \\pi 2_s]$).
   - Show why a thermal $[2+2]$ cycloaddition requires crossing an orbital symmetry barrier into an excited state, explaining why thermal $[2+2]$ is symmetry-forbidden.
   - Prove why photochemical excitation ($h\\nu$) renders $[2+2]$ cycloaddition symmetry-allowed.""",
                "solution": """### Part 1: Orbital Symmetry Proof for Thermal $[4+2]$ Cycloaddition

Consider the suprafacial-suprafacial approach of 1,3-butadiene and ethylene in the Diels-Alder reaction.
The reaction preserves a vertical **mirror plane of symmetry ($\\sigma$)** bisecting both the diene $\\text{C}_2-\\text{C}_3$ bond and the ethylene $\\text{C}-\\text{C}$ bond throughout the reaction coordinate:

#### Orbital Symmetries under Reflection $\\sigma$:
1. **Reactants**:
   - Diene $\\Psi_1$: Symmetric ($S$)
   - Diene $\\Psi_2$ (HOMO): Antisymmetric ($A$)
   - Ethylene $\\pi$: Symmetric ($S$)
   - Total reactant ground-state configuration: $S^2 A^2 S^2$ (or in ordered symmetry: $S^4 A^2$)
2. **Product (Cyclohexene)**:
   - Forms two new $\\sigma$ bonds (one symmetric $\\sigma_1$, one antisymmetric $\\sigma_2$) and one new $\\pi$ bond (symmetric $\\pi$):
   - $\\sigma_1$ ($S$), $\\sigma_2$ ($A$), $\\pi$ ($S$)
   - Product ground-state configuration: $\\sigma_1^2 \\pi^2 \\sigma_2^2 \\implies S^4 A^2$

#### Correlation:
- Diene $\\Psi_1(S) \\longrightarrow \\sigma_1(S)$
- Ethylene $\\pi(S) \\longrightarrow \\pi(S)$
- Diene $\\Psi_2(A) \\longrightarrow \\sigma_2(A)$

**Conclusion**: Every bonding orbital of the ground-state reactants correlates smoothly with a bonding orbital of the ground-state product with zero crossing of the Fermi level.
Therefore, the **$[\\pi 4_s + \\pi 2_s]$ cycloaddition is thermally allowed** with a low activation barrier.

---

### Part 2: Orbital Symmetry Proof for $[2+2]$ Cycloaddition

Consider the face-to-face approach of two ethylene molecules forming cyclobutane.
The system possesses two mutually orthogonal planes of symmetry: $\\sigma_1$ (bisecting the $\\text{C}-\\text{C}$ bonds) and $\\sigma_2$ (parallel to the internuclear axes):

#### Reactant Orbitals:
- $\\pi_1 + \\pi_2$: Symmetric-Symmetric ($SS$)
- $\\pi_1 - \\pi_2$: Symmetric-Antisymmetric ($SA$)
- $\\pi_1^* + \\pi_2^*$: Antisymmetric-Symmetric ($AS$)
- $\\pi_1^* - \\pi_2^*$: Antisymmetric-Antisymmetric ($AA$)
Reactant ground-state: $(SS)^2 (SA)^2$.

#### Product Cyclobutane Orbitals:
- $\\sigma_1 + \\sigma_2$: ($SS$)
- $\\sigma_1 - \\sigma_2$: ($AS$)
- $\\sigma_1^* + \\sigma_2^*$: ($SA$)
- $\\sigma_1^* - \\sigma_2^*$: ($AA$)
Product ground-state: $(SS)^2 (AS)^2$.

#### The Symmetry Breakdown:
Notice the correlation:
- The filled reactant orbital $(SA)^2$ correlates with the high-energy **antibonding** product orbital $(\\sigma_1^* + \\sigma_2^*)(SA)^2$!
- The empty reactant orbital $(AS)^0$ correlates with the bonding product orbital $(AS)^2$.

**Thermal Prohibition**: To form ground-state cyclobutane thermally, an electron pair from the occupied $(SA)$ orbital would have to cross an enormous energy barrier into an excited state. Therefore, **thermal $[\\pi 2_s + \\pi 2_s]$ is strictly symmetry-forbidden**.

#### Photochemical Activation ($h\\nu$):
Absorption of a photon promotes one electron:
$$\\text{Reactant State: } (SS)^2 (SA)^1 (AS)^1$$
Now, the singly occupied $(SA)$ orbital and singly occupied $(AS)$ orbital correlate directly with the first excited state of cyclobutane:
$$\\text{Product State: } (SS)^2 (AS)^1 (SA)^1$$
Zero symmetry crossing occurs! The reaction proceeds smoothly and rapidly under UV irradiation (**photochemically allowed**)."""
            }
        ]
    }
