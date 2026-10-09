"""
create_organo_u8.py
Unit 8: Fundamental Organometallic Reaction Mechanisms
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_8():
    sections = [
        {
            "id": "sec8_1",
            "title": "§8.1 Ligand Substitution Mechanisms: Associative ($A, I_a$) vs. Dissociative ($D, I_d$)",
            "content": """Ligand substitution is the fundamental entry point into every catalytic cycle:
\\[ L_n M-L' + L'' \\longrightarrow L_n M-L'' + L' \\]
The kinetic pathway is categorized by Langford and Gray into dissociative, associative, and interchange mechanisms:

### 1. Dissociative Mechanism ($D$ or $I_d$):
- **Trajectory**: An existing ligand departs first, generating an intermediate of lower coordination number:
  \\[ L_n M-L' \\xrightleftharpoons[k_{-1}]{k_1} [L_n M] + L' \\quad (\\text{Slow, Rate-Determining}) \\]
  \\[ [L_n M] + L'' \\xrightarrow{k_2} L_n M-L'' \\quad (\\text{Fast}) \\]
- **Characteristics**:
  - Predominant for **18-electron saturated complexes** (e.g., $\\text{Cr}(\\text{CO})_6, \\text{Ni}(\\text{CO})_4$).
  - **Rate Law**: First-order in substrate, zero-order in incoming nucleophile:
    \\[ \\text{Rate} = k_1 [L_n M-L'] \\]
  - **Activation Parameters**: Large positive activation entropy ($\\Delta S^\\ddagger > +30\\text{ to }+60\\text{ J/(mol}\\cdot\\text{K)}$) and positive activation volume ($\\Delta V^\\ddagger > +10\\text{ cm}^3\\text{/mol}$), reflecting bond cleavage and increased particle freedom in the transition state.

### 2. Associative Mechanism ($A$ or $I_a$):
- **Trajectory**: The incoming ligand coordinates first, forming an intermediate of higher coordination number:
  \\[ L_n M-L' + L'' \\xrightleftharpoons[k_{-1}]{k_1} [L_n M(L')(L'')] \\quad (\\text{Slow}) \\]
  \\[ [L_n M(L')(L'')] \\xrightarrow{k_2} L_n M-L'' + L' \\quad (\\text{Fast}) \\]
- **Characteristics**:
  - Predominant for **16-electron square planar $d^8$ complexes** (e.g., $\\text{Pt}(\\text{II}), \\text{Pd}(\\text{II}), \\text{Rh}(\\text{I})$) and complexes with flexible polyhapto ligands capable of ring slipping ($\\eta^5 \\to \\eta^3 \\to \\eta^1$).
  - **Rate Law**: Second-order overall:
    \\[ \\text{Rate} = k_2 [L_n M-L'][L''] \\]
  - **Activation Parameters**: Strongly negative activation entropy ($\\Delta S^\\ddagger < -40\\text{ to }-120\\text{ J/(mol}\\cdot\\text{K)}$) and negative activation volume ($\\Delta V^\\ddagger < -10\\text{ cm}^3\\text{/mol}$), reflecting molecular association in the transition state."""
        },
        {
            "id": "sec8_2",
            "title": "§8.2 Kinetic Trans-Effect, Cis-Effect and Thermodynamic Trans-Influence",
            "content": """In square planar substitution reactions (specifically $\\text{Pt}(\\text{II})$ and $\\text{Pd}(\\text{II})$), the nature of the spectator ligand trans to the leaving group governs the substitution rate by up to six orders of magnitude.

### 1. Thermodynamic Trans-Influence (Ground-State Phenomenon):
The **trans-influence** is the extent to which a ligand $T$ weakens and lengthens the metal-ligand bond trans to itself in the **ground state**.
- **Physical Basis**: A strong $\\sigma$-donor ligand donates massive electron density into the metal $p_x/d_{x^2-y^2}$ hybrid orbital, polarizing that orbital away from the trans position. The trans bond is deprived of covalent metal overlap, lengthening the bond and lowering its stretching frequency.
- **Trans-Influence Order**:
  \\[ \\text{Si}R_3 > \\text{H}^- > \\text{CH}_3^- \\approx \\text{PR}_3 > \\text{olefin} > \\text{I}^- > \\text{Br}^- > \\text{Cl}^- > \\text{NH}_3 > \\text{OH}^- \\]

### 2. Kinetic Trans-Effect (Transition-State Phenomenon):
The **trans-effect** is the effect of a spectator ligand $T$ on the **rate of substitution** of the ligand trans to itself.
- **Physical Components**:
  - **$\\sigma$-Component**: A strong $\\sigma$-donor raises the ground-state energy ($G_0$), reducing the activation energy $\\Delta G^\\ddagger$.
  - **$\\pi$-Component**: A strong $\\pi$-acceptor ligand (e.g., $\\text{CO}, \\text{C}_2\\text{H}_4, \\text{CN}^-$) stabilizes the trigonal bipyramidal transition state ($G_{TS}$) by accepting electron density from the metal in the trigonal plane, massively lowering $\\Delta G^\\ddagger$.
- **Trans-Effect Order**:
  \\[ \\text{CO} \\approx \\text{CN}^- \\approx \\text{C}_2\\text{H}_4 > \\text{PR}_3 \\approx \\text{H}^- > \\text{CH}_3^- > \\text{I}^- \\approx \\text{SCN}^- > \\text{Br}^- > \\text{Cl}^- > \\text{py} > \\text{NH}_3 > \\text{H}_2\\text{O} \\]

### Synthetic Application: Controlled Synthesis of Platinum Isomers:
The trans-effect enables the synthesis of specific diastereomers (e.g., *cis*-diamminedichloroplatinum(II), **Cisplatin**):
\\[ [\\text{PtCl}_4]^{2-} + 2\\,\\text{NH}_3 \\longrightarrow \\text{cis}-[\\text{PtCl}_2(\\text{NH}_3)_2] \\quad (\\text{Cisplatin}) \\]
because $\\text{Cl}^-$ has a stronger trans-effect than $\\text{NH}_3$, directing the second ammonia ligand *cis* to the first."""
        },
        {
            "id": "sec8_3",
            "title": "§8.3 Oxidative Addition I: Non-Polar Substrates via Concerted Three-Center Pathways",
            "content": """**Oxidative addition** is an elementary reaction in which a metal complex reacts with a substrate $X-Y$, cleaving the $X-Y$ bond and coordinating both fragments to the metal:
\\[ L_n M^m + X-Y \\longrightarrow L_n M^{m+2}(X)(Y) \\]
- Formal metal oxidation state increases by **$+2$**.
- Total valence electron count ($VEC$) increases by **$+2$**.
- Coordination number increases by **$+2$**.

### Concerted Three-Center Mechanism (Non-Polar Substrates: $\\text{H}_2, \\text{C}-\\text{H}, \\text{Si}-\\text{H}$):
When the substrate has zero or low polarity (e.g., dihydrogen $\\text{H}_2$, silanes $R_3\\text{Si}-\\text{H}$, hydrocarbons $R-\\text{H}$):
1. **Side-on $\\sigma$-Coordination**: The substrate approaches the metal center, forming a transient $\\sigma$-complex ($M-(\\eta^2-\\text{H}_2)$).
2. **Three-Center Transition State**: Simultaneous $\\sigma$-donation from $\\sigma(X-Y)$ to metal and $\\pi$-backdonation from metal $d$ into $\\sigma^*(X-Y)$:
   \\[ M + X-Y \\longrightarrow \\begin{pmatrix} X \\\\ \\vdots \\\\ Y \\end{pmatrix} \\cdots M \\longrightarrow L_n M(X)(Y) \\]
3. **Stereospecificity**:
   Because both fragments are delivered simultaneously from the same face of the metal, the reaction proceeds with **100% *cis*-stereospecificity** and **retention of configuration** at any chiral migrating center."""
        },
        {
            "id": "sec8_4",
            "title": "§8.4 Oxidative Addition II: Polar Substrates via $S_N2$ and Radical Pathways",
            "content": """When the substrate possesses a highly polarized bond and a good leaving group (e.g., alkyl halides $R-\\text{X}$, benzyl halides, $\\alpha$-haloesters), oxidative addition diverges into two alternative mechanisms:

### 1. The Nucleophilic $S_N2$ Pathway:
- The electron-rich, low-valent metal center acts as a classical nucleophile, performing backside attack on the alkyl halide carbon atom:
  \\[ L_n M + R-\\text{X} \\longrightarrow [L_n M-R]^+ \\dots \\text{X}^- \\quad (\\text{Inversion of Configuration at Carbon}) \\]
- The halide anion subsequently coordinates to the cationic metal center, either *trans* or *cis* depending on solvent and electronics.
- **Diagnostic Criteria**:
  - Stereochemistry: **Clean inversion of configuration** at the reacting $sp^3$-carbon.
  - Substrate Reactivity Order: Matches standard $S_N2$ rates:
    \\[ \\text{Me-X} > \\text{Primary } R\\text{-X} \\gg \\text{Secondary } R\\text{-X} \\gg \\text{Tertiary } R\\text{-X} \\text{ (no reaction)} \\]
    \\[ R-\\text{I} > R-\\text{Br} > R-\\text{Cl} \\gg R-\\text{F} \\]
  - Large negative activation entropy ($\\Delta S^\\ddagger = -120\\text{ to }-180\\text{ J/(mol}\\cdot\\text{K)}$) and strong rate acceleration in polar solvents.

### 2. The Radical Pathway:
- Prevalent for tertiary alkyl halides, secondary alkyl iodides, and systems where steric hindrance precludes $S_N2$ backside attack:
  - **Outer-Sphere Single Electron Transfer (SET)**:
    \\[ L_n M + R-\\text{X} \\longrightarrow [L_n M]^+\\!^\\bullet + [R-\\text{X}]^-\\mskip-2mu^\\bullet \\longrightarrow [L_n M]^+\\!^\\bullet + R^\\bullet + \\text{X}^- \\]
    \\[ [L_n M]^+\\!^\\bullet + R^\\bullet + \\text{X}^- \\longrightarrow L_n M(R)(\\text{X}) \\]
  - **Diagnostic Criteria**: Loss of stereochemical fidelity (**complete racemization**), cyclization of radical clock probes (e.g., 5-hexenyl radical forming cyclopentylmethyl), and dramatic inhibition by radical scavengers (galvinoxyl, TEMPO)."""
        },
        {
            "id": "sec8_5",
            "title": "§8.5 Reductive Elimination: Orbital Symmetry, Stereochemistry & Bite-Angle Acceleration",
            "content": """**Reductive elimination** is the microscopic reverse of oxidative addition, cleaving two metal-ligand bonds to form a new organic single bond while reducing the metal:
\\[ L_n M^{m+2}(R)(R') \\longrightarrow L_n M^m + R-R' \\]
- Metal oxidation state decreases by **$-2$**.
- Total valence electron count ($VEC$) decreases by **$-2$**.
- Coordination number decreases by **$-2$**.

### Stereoelectronic and Orbital Constraints:
1. **Mutually *cis* Orientation Requirement**:
   The two eliminating groups $R$ and $R'$ must occupy mutually **cis coordination positions**. Trans ligands cannot eliminate without prior isomerization to a cis geometry.
2. **Orbital Symmetry Conservation (Woodward-Hoffmann)**:
   The concerted elimination involves overlap of the two filled $M-R$ $\\sigma$-bonding orbitals, passing through a three-centered transition state:
   \\[ [R \\cdots M \\cdots R']^\\ddagger \\longrightarrow R-R' + M \\]
   Proceeds with **complete retention of stereochemical configuration** at both carbon centers.
3. **Electronic Driving Force**:
   Favored by **electron-poor metal centers**, bulky ancillary ligands that relieve steric strain upon elimination, and high oxidation states.

### Bite-Angle Acceleration:
Chelating diphosphines with wide natural bite angles (e.g., Xantphos $\\beta_n = 111^\\circ$) compress the cis-$R-M-R'$ angle, pre-organizing the reactants into close spatial proximity and accelerating elimination by up to $10^7$-fold."""
        },
        {
            "id": "sec8_6",
            "title": "§8.6 1,1-Migratory Insertion: Carbon Monoxide Insertion into Metal-Alkyl Bonds",
            "content": """In a **1,1-migratory insertion**, a coordinated unsaturated ligand inserts between the metal atom and an adjacent $\\sigma$-bound ligand, with both metal-ligand bonds ending up attached to the *same* atom of the inserting ligand:
\\[ L_n M(R)(\\text{CO}) \\longrightarrow L_n M-\\text{C}(=\\text{O})R \\quad (\\text{Acyl Complex}) \\]

### Intramolecular Alkyl Migration vs. Carbonyl Insertion:
- Isotopic labeling ($^{13}\\text{CO}$) and stereochemical studies establish that the reaction proceeds predominantly by **intramolecular migration of the alkyl group onto the coordinated CO**, rather than CO inserting into the $M-R$ bond:
  1. The alkyl group moves to an adjacent, mutually *cis* carbonyl ligand.
  2. This migration vacates the coordination site previously occupied by the alkyl group, creating a coordinatively unsaturated 16-electron intermediate.
  3. An incoming ligand ($L = CO, PR_3$) captures this vacant site:
     \\[ \\text{CH}_3\\text{Mn}(\\text{CO})_5 + \\text{CO}^* \\rightleftharpoons \\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4(\\text{CO}^*) \\]
  4. The labeled $\\text{CO}^*$ ends up exclusively in a *cis* position on the manganese center, proving that the acyl carbon originated from the original coordination sphere.

### Driving Force and Rate Acceleration:
- **Lewis Acid Promotion**: Addition of Lewis acids ($\\text{AlCl}_3, \\text{BF}_3$) coordinates the acyl oxygen atom, polarizing the carbonyl and accelerating insertion by factors up to $10^8$.
- **Oxidative Promotion**: One-electron oxidation of the metal center ($18\\text{e} \\to 17\\text{e}$) accelerates alkyl migration by up to $10^{10}$-fold."""
        },
        {
            "id": "sec8_7",
            "title": "§8.7 1,2-Migratory Insertion: Olefin & Alkyne Insertion into Metal-Hydrides and Alkyls",
            "content": """In a **1,2-migratory insertion**, the unsaturated ligand inserts such that the metal and the migrating group attach to *adjacent* atoms of the inserting moiety:
\\[ L_n M(\\text{H})(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}_2) \\longrightarrow L_n M-\\text{CH}_2-\\text{CH}_3 \\]

### Stereoelectronic Requirements:
1. **Coplanar Four-Membered Transition State**:
   The metal, hydride, and two alkene carbons must attain a planar geometry:
   \\[ [M \\cdots \\text{H} \\cdots C_\\beta \\cdots C_\\alpha]^\\ddagger \\]
   The migration proceeds with **100% *syn*-stereospecificity** (both the metal and hydrogen are delivered to the same face of the double bond).
2. **Regioselectivity (Markovnikov vs. Anti-Markovnikov)**:
   - Insertion into $M-\\text{H}$ bonds of unsymmetrical alkenes $R-\\text{CH}=\\text{CH}_2$ can yield linear ($M-\\text{CH}_2\\text{CH}_2 R$) or branched ($M-\\text{CH}(R)\\text{CH}_3$) alkyl complexes.
   - For early transition metals and sterically unhindered hydrides, **anti-Markovnikov (linear) insertion** dominates ($>99\\%$) to minimize steric clash between $R$ and the metal coordination sphere.
3. **Insertion into Metal-Alkyl Bonds**:
   Olefin insertion into $M-\\text{R}$ bonds has a significantly higher activation barrier than into $M-\\text{H}$ bonds (by $30-50\\text{ kJ/mol}$). However, this reaction is the fundamental chain propagation step in the industrial polymerization of ethylene and propylene."""
        },
        {
            "id": "sec8_8",
            "title": "§8.8 $\\beta$-Hydride Elimination, $\\alpha$-Hydride Abstraction & Nucleophilic/Electrophilic Attack",
            "content": """Complementing migratory insertion and oxidative additions are elimination and outer-sphere functionalization reactions:

### 1. $\\beta$-Hydride Elimination:
- The microscopic reverse of 1,2-migratory insertion:
  \\[ L_n M-\\text{CH}_2\\text{CH}_2 R \\rightleftharpoons L_n M(\\text{H})(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}R) \\longrightarrow L_n M-\\text{H} + \\text{alkene} \\uparrow \\]
- Requires an open coordination site, *syn*-coplanar geometry, and an accessible empty $d$-orbital on the metal.

### 2. $\\alpha$-Hydride Abstraction and Elimination (Carbene Formation):
- When $\\beta$-hydrogens are absent (e.g., neopentyl complexes of $\\text{Ta}, \\text{W}$), the metal center abstracts an $\\alpha$-hydrogen atom from an adjacent alkyl group:
  \\[ \\text{Ta}(\\text{CH}_2\\text{CMe}_3)_5 \\xrightarrow{\\Delta} \\text{Ta}(=\\text{CH}t\\text{-Bu})(\\text{CH}_2\\text{CMe}_3)_3 + \\text{CMe}_4 \\uparrow \\quad (\\text{Schrock Carbene}) \\]
  This reaction discovered by Richard Schrock represents the standard route to nucleophilic alkylidene catalysts for olefin metathesis.

### 3. Outer-Sphere Nucleophilic and Electrophilic Attack:
- **Electrophilic Attack on Coordinated Ligands**: Coordinated polyenes can be attacked by electrophiles ($H^+, E^+$), generating cationic allylic or carbocationic intermediates.
- **Nucleophilic Attack on Coordinated $\\pi$-Ligands**: Electron-poor cationic metal fragments activate alkenes, alkynes, and arenes toward external attack by carbanions, amines, and alkoxides without prior coordination."""
        }
    ]

    problems = [
        {
            "id": "prob8_1",
            "tier": "Foundational",
            "title": "Derivation of the Rate Law for Associative vs. Dissociative Substitution",
            "statement": "A transition metal complex $ML_5$ undergoes ligand substitution by nucleophile $Y$ to yield $ML_4 Y + L$. (a) Derive the steady-state rate law for a purely dissociative ($D$) pathway. (b) Derive the rate law for an associative ($A$) pathway. (c) At $298\\text{ K}$, the reaction has activation parameters $\\Delta H^\\ddagger = 125\\text{ kJ/mol}$ and $\\Delta S^\\ddagger = +58\\text{ J/(mol}\\cdot\\text{K)}$. Deduce which mechanism operates.",
            "solution": """**Line-by-Line Solution:**

**(a) Dissociative ($D$) Rate Law Derivation:**
1. Elementary steps:
   \\[ ML_5 \\xrightleftharpoons[k_{-1}]{k_1} ML_4 + L \\]
   \\[ ML_4 + Y \\xrightarrow{k_2} ML_4 Y \\]
2. The rate of product formation is:
   \\[ \\text{Rate} = k_2 [ML_4][Y] \\]
3. Apply the steady-state approximation to the reactive 16e intermediate $[ML_4]$:
   \\[ \\frac{d[ML_4]}{dt} = k_1 [ML_5] - k_{-1} [ML_4][L] - k_2 [ML_4][Y] = 0 \\]
   \\[ [ML_4] = \\frac{k_1 [ML_5]}{k_{-1}[L] + k_2 [Y]} \\]
4. Substitute into the rate equation:
   \\[ \\text{Rate} = \\frac{k_1 k_2 [ML_5][Y]}{k_{-1}[L] + k_2 [Y]} \\]
- **Limiting Case**: In the absence of added free leaving group $[L]$ or when incoming nucleophile is in large excess ($k_2 [Y] \\gg k_{-1}[L]$):
  \\[ \\text{Rate} = k_1 [ML_5] \\quad (\\text{pseudo-first-order, zero-order in } [Y]) \\]

**(b) Associative ($A$) Rate Law Derivation:**
1. Elementary steps:
   \\[ ML_5 + Y \\xrightleftharpoons[k_{-1}]{k_1} ML_5 Y \\]
   \\[ ML_5 Y \\xrightarrow{k_2} ML_4 Y + L \\]
2. Apply the steady-state approximation to the 7-coordinate intermediate $[ML_5 Y]$:
   \\[ \\frac{d[ML_5 Y]}{dt} = k_1 [ML_5][Y] - (k_{-1} + k_2) [ML_5 Y] = 0 \\]
   \\[ [ML_5 Y] = \\frac{k_1 [ML_5][Y]}{k_{-1} + k_2} \\]
3. Product rate:
   \\[ \\text{Rate} = k_2 [ML_5 Y] = \\left(\\frac{k_1 k_2}{k_{-1} + k_2}\\right) [ML_5][Y] = k_A [ML_5][Y] \\]
- **Order**: Strictly **second-order overall** (first order in $[ML_5]$, first order in $[Y]$).

**(c) Mechanism Assignment from Activation Parameters:**
- Given: $\\Delta H^\\ddagger = +125\\text{ kJ/mol}$, $\\Delta S^\\ddagger = +58\\text{ J/(mol}\\cdot\\text{K)}$.
- In an associative pathway, two molecules combine into a single organized transition state, resulting in a large loss of translational and rotational freedom:
  \\[ \\Delta S^\\ddagger_A < -40\\text{ to }-120\\text{ J/(mol}\\cdot\\text{K)} \\]
- In a dissociative pathway, one molecule fragments to break a metal-ligand bond, releasing a leaving group and generating increased disorder in the transition state:
  \\[ \\Delta S^\\ddagger_D > +30\\text{ to }+60\\text{ J/(mol}\\cdot\\text{K)} \\]
- The experimental value of **$\\Delta S^\\ddagger = +58\\text{ J/(mol}\\cdot\\text{K)}$** is strongly positive, unambiguously diagnosing a **purely dissociative ($D$ or $I_d$) substitution mechanism**."""
        },
        {
            "id": "prob8_2",
            "tier": "Foundational",
            "title": "Synthesis of Platinum Geometric Isomers Using the Trans-Effect",
            "statement": "Starting from potassium tetrachloroplatinate(II) $\\text{K}_2[\\text{PtCl}_4]$ and necessary reagents (ammonia $\\text{NH}_3$, chloride $\\text{Cl}^-$, nitrite $\\text{NO}_2^-$): (a) Design a stepwise synthetic route for *cis*-$[\\text{PtCl}(\\text{NO}_2)(\\text{NH}_3)_2]$. (b) Design a stepwise synthetic route for *trans*-$[\\text{PtCl}(\\text{NO}_2)(\\text{NH}_3)_2]$. Use the kinetic trans-effect order: $\\text{NO}_2^- > \\text{Cl}^- > \\text{NH}_3$.",
            "solution": """**Line-by-Line Solution:**

**(a) Synthesis of *cis*-$[\\text{PtCl}(\\text{NO}_2)(\\text{NH}_3)_2]$:**
1. Starting material: $[\\text{PtCl}_4]^{2-}$ (all four ligands are chloride).
2. **Step 1: Introduction of Nitrite**:
   \\[ [\\text{PtCl}_4]^{2-} + \\text{NO}_2^- \\longrightarrow [\\text{PtCl}_3(\\text{NO}_2)]^{2-} + \\text{Cl}^- \\]
   All four positions are equivalent.
3. **Step 2: First Ammonia Substitution**:
   In $[\\text{PtCl}_3(\\text{NO}_2)]^{2-}$, the ligands are three $\\text{Cl}^-$ and one $\\text{NO}_2^-$.
   - Trans-effect order: $\\text{NO}_2^- > \\text{Cl}^-$.
   - The ligand possessing the strongest trans-effect is $\\text{NO}_2^-$.
   - Therefore, the chloride ligand **trans to $\\text{NO}_2^-$** is labilized and substituted first:
   \\[ [\\text{PtCl}_3(\\text{NO}_2)]^{2-} + \\text{NH}_3 \\longrightarrow \\text{trans}-[\\text{PtCl}_2(\\text{NO}_2)(\\text{NH}_3)]^- + \\text{Cl}^- \\]
   Wait, this gives *trans*! To get *cis*, we must add ammonia first!
4. **Corrected Synthesis for *cis*-Isomer**:
   - **Step 1: First Ammonia Substitution on $[\\text{PtCl}_4]^{2-}$**:
     \\[ [\\text{PtCl}_4]^{2-} + \\text{NH}_3 \\longrightarrow [\\text{PtCl}_3(\\text{NH}_3)]^- + \\text{Cl}^- \\]
   - **Step 2: Second Ammonia Substitution**:
     In $[\\text{PtCl}_3(\\text{NH}_3)]^-$, trans-effect of $\\text{Cl}^- > \\text{NH}_3$.
     - The chloride trans to another chloride is more labile than the chloride trans to $\\text{NH}_3$.
     - Substitution yields *cis*-$[\\text{PtCl}_2(\\text{NH}_3)_2]$ (**Cisplatin**).
   - **Step 3: Nitrite Substitution on Cisplatin**:
     In *cis*-$[\\text{PtCl}_2(\\text{NH}_3)_2]$, both chlorides are trans to $\\text{NH}_3$.
     Reaction with 1 equivalent of $\\text{NO}_2^-$ displaces one chloride:
     \\[ \\text{cis}-[\\text{PtCl}_2(\\text{NH}_3)_2] + \\text{NO}_2^- \\longrightarrow \\mathbf{\\text{cis}-[\\text{PtCl}(\\text{NO}_2)(\\text{NH}_3)_2]} + \\text{Cl}^- \\]
     delivering the pure *cis*-isomer.

**(b) Synthesis of *trans*-$[\\text{PtCl}(\\text{NO}_2)(\\text{NH}_3)_2]$:**
1. **Step 1**: React $[\\text{PtCl}_4]^{2-}$ with $\\text{NO}_2^-$ to yield $[\\text{PtCl}_3(\\text{NO}_2)]^{2-}$.
2. **Step 2**: React with $\\text{NH}_3$.
   Because $\\text{NO}_2^-$ has a vastly stronger trans-effect than $\\text{Cl}^-$, ammonia displaces the chloride trans to $\\text{NO}_2^-$:
   \\[ [\\text{PtCl}_3(\\text{NO}_2)]^{2-} + \\text{NH}_3 \\longrightarrow \\text{trans}-[\\text{PtCl}_2(\\text{NO}_2)(\\text{NH}_3)]^- + \\text{Cl}^- \\]
3. **Step 3**: React with second equivalent of $\\text{NH}_3$.
   In $\\text{trans}-[\\text{PtCl}_2(\\text{NO}_2)(\\text{NH}_3)]^-$, the two remaining chlorides are mutually trans. Their trans-effect ($\text{Cl}^- > \\text{NH}_3$) labilizes one of them:
   \\[ \\text{trans}-[\\text{PtCl}_2(\\text{NO}_2)(\\text{NH}_3)]^- + \\text{NH}_3 \\longrightarrow \\mathbf{\\text{trans}-[\\text{PtCl}(\\text{NO}_2)(\\text{NH}_3)_2]} + \\text{Cl}^- \\]
   yielding the pure *trans*-isomer."""
        },
        {
            "id": "prob8_3",
            "tier": "Foundational",
            "title": "Oxidative Addition Kinetics of Vaska's Complex with Alkyl Halides",
            "statement": "Vaska's complex $\\text{trans}-[\\text{IrCl}(\\text{CO})(\\text{PPh}_3)_2]$ reacts with methyl iodide $\\text{CH}_3\\text{I}$ in benzene to form an octahedral $\\text{Ir}(\\text{III})$ adduct. (a) Write the balanced chemical equation, state the change in metal oxidation state, and write the electron count before and after. (b) When optically active $(S)$-2-bromobutane is used, the product is completely inverted at carbon to the $(R)$ configuration. Deduce the reaction mechanism. (c) State the expected kinetic order and effect of solvent polarity.",
            "solution": """**Line-by-Line Solution:**

**(a) Reaction Equation, Oxidation State, and Electron Count:**
\\[ \\text{trans}-[\\text{IrCl}(\\text{CO})(\\text{PPh}_3)_2] + \\text{CH}_3\\text{I} \\longrightarrow [\\text{IrCl}(\\text{I})(\\text{CO})(\\text{PPh}_3)_2(\\text{CH}_3)] \\]
1. **Starting Material**:
   - Iridium oxidation state: $+1$ ($d^8$).
   - Coordination number: 4 (square planar).
   - Valence electron count: $VEC = 9 (\\text{Ir}) + 1 (\\text{Cl}) + 2 (\\text{CO}) + 4 (2\\text{PPh}_3) = \\mathbf{16\\text{ electrons}}$.
2. **Product**:
   - Iridium oxidation state: $+3$ ($d^6$).
   - Coordination number: 6 (octahedral).
   - Valence electron count: $VEC = 9 + 1 (\\text{Cl}) + 1 (\\text{I}) + 2 (\\text{CO}) + 4 (2\\text{PPh}_3) + 1 (\\text{Me}) = \\mathbf{18\\text{ electrons}}$.
- Formal changes: $\\Delta OS = +2, \\Delta CN = +2, \\Delta VEC = +2$.

**(b) Reaction Mechanism from Stereochemical Inversion:**
- The observation of **100% inversion of stereochemical configuration** at the chiral secondary carbon of $(S)$-2-bromobutane is the hallmark of a **classical nucleophilic backside attack ($S_N2$ mechanism)**.
- The electron-rich $5d^8$ iridium center acts as a powerful nucleophile:
  1. Iridium uses its filled $5d_{z^2}$ lone pair to attack the $\\sigma^*(C-Br)$ antibonding orbital from the backside of the carbon-bromine bond.
  2. The bromide leaving group departs with inversion of configuration at carbon, forming a transient ion-pair intermediate:
     \\[ [\\text{Ir}(\\text{sec-butyl})(\\text{Cl})(\\text{CO})(\\text{PPh}_3)_2]^+ \\dots \\text{Br}^- \\]
  3. The free bromide ion then rapidly coordinates into the remaining open axial site on iridium, completing oxidative addition.

**(c) Kinetic Order and Solvent Effects:**
- **Rate Law**: The $S_N2$ pathway obeys strict second-order kinetics:
  \\[ \\text{Rate} = k_2 [\\text{Ir}] [R\\text{X}] \\]
- **Solvent Polarity**: Because the transition state is highly polar and charge-separated ($[\\text{Ir}^{\\delta+} \\dots C \\dots \\text{Br}^{\\delta-}]^\\ddagger$), increasing solvent polarity (e.g., from benzene to acetone or DMF) stabilizes the transition state, accelerating the reaction rate by factors of $10^2$ to $10^3$."""
        },
        {
            "id": "prob8_4",
            "tier": "Intermediate",
            "title": "Migratory Insertion Thermodynamics and Kinetic Solvent Participation",
            "statement": "The carbonylation of methylpentacarbonylmanganese $\\text{CH}_3\\text{Mn}(\\text{CO})_5 + L \\longrightarrow \\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4 L$ was studied in coordinating (THF) and non-coordinating (cyclohexane) solvents. (a) In cyclohexane, the reaction rate is strictly first-order in $[\\text{CH}_3\\text{Mn}(\\text{CO})_5]$ and independent of $[L]$. In THF, the rate constant is $10^4$ times faster. Formulate the steady-state mechanisms in both solvents. (b) Explain why using chiral $(S)$-[$\\alpha$-D]alkylmanganese proceeds with $100\\%$ retention of configuration at carbon.",
            "solution": """**Line-by-Line Solution:**

**(a) Mechanistic Analysis in Non-Coordinating vs. Coordinating Solvents:**

1. **In Cyclohexane (Non-Coordinating Solvent)**:
   - Elementary steps:
     \\[ \\text{CH}_3\\text{Mn}(\\text{CO})_5 \\xrightleftharpoons[k_{-1}]{k_1} [\\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4] \\quad (16\\text{e intermediate, vacant site}) \\]
     \\[ [\\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4] + L \\xrightarrow{k_2} \\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4 L \\]
   - Steady-state on the 16e intermediate:
     \\[ \\text{Rate} = \\frac{k_1 k_2 [\\text{Mn}][L]}{k_{-1} + k_2 [L]} \\]
   - When incoming ligand $L$ captures the vacant site rapidly ($k_2 [L] \\gg k_{-1}$):
     \\[ \\text{Rate} = k_1 [\\text{CH}_3\\text{Mn}(\\text{CO})_5] \\]
     The rate is completely independent of $[L]$ because the rate-determining step is the intrinsic intramolecular migration of the methyl group ($k_1$).

2. **In THF (Coordinating Solvent)**:
   - THF is a coordinating Lewis base that directly intercepts the 16e intermediate:
     \\[ \\text{CH}_3\\text{Mn}(\\text{CO})_5 + \\text{THF} \\xrightleftharpoons[k_{-s}]{k_s} \\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4(\\text{THF}) \\]
   - Coordinating THF stabilizes the vacant coordination site as an 18-electron solvato-complex, lowering the activation free energy barrier $\\Delta G^\\ddagger$ for the migration step by $>25\\text{ kJ/mol}$.
   - Subsequent rapid associative or dissociative displacement of weakly bound THF by incoming ligand $L$ completes the reaction:
     \\[ \\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4(\\text{THF}) + L \\xrightarrow{\\text{fast}} \\text{CH}_3\\text{CO}-\\text{Mn}(\\text{CO})_4 L + \\text{THF} \\]
   - This catalytic solvent assistance accelerates the reaction rate by four orders of magnitude ($10^4$).

**(b) Stereochemical Retention at Migrating Carbon:**
- In the intramolecular 1,1-migratory insertion, the migrating alkyl group moves from the metal atom directly to the adjacent carbonyl carbon atom.
- The carbon-manganese $\\sigma$-bonding pair never breaks homolytically or heterolytically into solution; instead, the $sp^3$ hybrid orbital of the migrating carbon atom smoothly pivots to overlap with the empty $\\pi^*$ orbital of the adjacent coordinated CO ligand.
- Because the migrating carbon's orbital envelope remains continuously bonded to the metal-carbonyl framework throughout the transition state, the migrating center undergoes **100% complete retention of stereochemical configuration**."""
        },
        {
            "id": "prob8_5",
            "tier": "Intermediate",
            "title": "Microscopic Reversibility in Reductive Elimination of Alkanes",
            "statement": "The reductive elimination of methane from hydridomethyl complexes $[L_2\\text{Pt}(\\text{H})(\\text{CH}_3)]$ and the oxidative addition of methane to platinum(0) $[L_2\\text{Pt}]$ are microscopic reverses. (a) Draw the three-center transition state and the intermediate $\\sigma$-methane complex $[L_2\\text{Pt}(\\eta^2-\\text{H}-\\text{CH}_3)]$. (b) Using the principle of microscopic reversibility, explain why the $C-H$ bond of methane is cleaved with complete retention of configuration at carbon during oxidative addition. (c) Given $\\Delta H^\\circ = -42\\text{ kJ/mol}$ for reductive elimination and $E_a = 68\\text{ kJ/mol}$, calculate the activation energy for methane activation (oxidative addition).",
            "solution": """**Line-by-Line Solution:**

**(a) Transition State and $\\sigma$-Methane Complex:**
The complete reaction coordinate proceeds via a double-well profile:
\\[ L_2\\text{Pt}(\\text{H})(\\text{CH}_3) \\rightleftharpoons [L_2\\text{Pt} \\cdots \\text{H} \\cdots \\text{CH}_3]^\\ddagger \\rightleftharpoons L_2\\text{Pt}(\\eta^2-\\text{H}-\\text{CH}_3) \\rightleftharpoons L_2\\text{Pt} + \\text{CH}_4 \\]
1. **Transition State $[L_2\\text{Pt} \\cdots \\text{H} \\cdots \\text{CH}_3]^\\ddagger$**:
   - A triangular three-centered transition state where the $Pt-H$ and $Pt-C$ bonds are partially breaking while the $C-H$ bond is partially forming.
2. **$\\sigma$-Methane Complex $L_2\\text{Pt}(\\eta^2-\\text{H}-\\text{CH}_3)$**:
   - A bound intermediate where intact methane coordinates to the 14-electron platinum(0) center via a $3c-2e$ interaction from its filled $\\sigma(C-H)$ bonding orbital.

**(b) Stereochemical Retention via Microscopic Reversibility:**
- According to the **Principle of Microscopic Reversibility**, the forward and reverse pathways of a reversible reaction must proceed through the exact same transition state along identical potential energy trajectories.
- Reductive elimination of methane is known experimentally to proceed with **100% retention of configuration** at the methyl carbon because the $C-H$ bond forms via concerted three-center orbital overlap.
- Therefore, the reverse reaction—oxidative addition of a $C-H$ bond of an alkane to a transition metal—must also proceed through this exact same three-center transition state.
- Consequently, $\\text{C}-\\text{H}$ bond activation by transition metals proceeds with **100% retention of configuration** at carbon, never via inversion or free radical intermediates!

**(c) Activation Energy for Oxidative Addition:**
From chemical thermodynamics:
\\[ \\Delta H^\\circ = E_{a,\\text{forward}} - E_{a,\\text{reverse}} \\]
For the reductive elimination reaction:
- Forward reaction: Reductive elimination ($E_{a,\\text{RE}} = 68\\text{ kJ/mol}$).
- Enthalpy change: $\\Delta H^\\circ = -42\\text{ kJ/mol}$ (exothermic).
- Reverse reaction: Oxidative addition ($E_{a,\\text{OA}}$).
\\[ -42 = 68 - E_{a,\\text{OA}} \\implies E_{a,\\text{OA}} = 68 - (-42) = 68 + 42 = \\mathbf{110\\text{ kJ/mol}} \\]
- **Conclusion**: The activation barrier for methane oxidative addition is **$110\\text{ kJ/mol}$** ($26.3\\text{ kcal/mol}$), explaining why alkane $\\text{C}-\\text{H}$ activation requires high temperatures or photochemical generation of highly reactive, coordinatively unsaturated metal intermediates."""
        },
        {
            "id": "prob8_6",
            "tier": "Intermediate",
            "title": "Bite-Angle Acceleration in Reductive Elimination of Carbon-Heteroatom Bonds",
            "statement": "In palladium-catalyzed Buchwald-Hartwig amination, the reductive elimination of aryl amines from $[(P-P)\\text{Pd}(\\text{Ar})(\\text{NR}_2)]$ is accelerated by wide bite-angle diphosphines. For dppe ($\\beta_n = 85^\\circ$), the activation barrier is $\\Delta G^\\ddagger = 98\\text{ kJ/mol}$. For Xantphos ($\\beta_n = 111^\\circ$), the barrier drops to $\\Delta G^\\ddagger = 66\\text{ kJ/mol}$. (a) Calculate the rate acceleration factor $k_\\text{Xantphos} / k_\\text{dppe}$ at $350\\text{ K}$. (b) Explain why reductive elimination of carbon-nitrogen bonds is generally more difficult than carbon-carbon bonds, and how wide bite angles overcome this barrier.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of Rate Acceleration Factor at $350\\text{ K}$:**
The difference in activation free energy is:
\\[ \\Delta\\Delta G^\\ddagger = \\Delta G^\\ddagger(\\text{dppe}) - \\Delta G^\\ddagger(\\text{Xantphos}) = 98 - 66 = 32\\text{ kJ/mol} = 32,000\\text{ J/mol} \\]
From transition state theory, the ratio of rate constants is:
\\[ \\frac{k_\\text{Xantphos}}{k_\\text{dppe}} = \\exp\\left( \\frac{\\Delta\\Delta G^\\ddagger}{RT} \\right) \\]
Substitute $T = 350\\text{ K}$ and $R = 8.3145\\text{ J/(mol}\\cdot\\text{K)}$:
\\[ \\frac{\\Delta\\Delta G^\\ddagger}{RT} = \\frac{32,000}{(8.3145)(350)} = \\frac{32,000}{2910.1} \\approx 10.996 \\]
Compute the exponential:
\\[ \\frac{k_\\text{Xantphos}}{k_\\text{dppe}} = \\exp(10.996) \\approx \\mathbf{5.96 \\times 10^4} \\]
- **Result**: The reaction is accelerated by nearly **60,000-fold** at $350\\text{ K}$!

**(b) Why C-N Reductive Elimination is Difficult and Bite-Angle Relief:**
1. **High Activation Barrier for C-N Elimination**:
   - The nitrogen atom of an amido ligand ($\\text{NR}_2^-$) is more electronegative than carbon ($\chi_N = 3.04$ vs $\chi_C = 2.55$).
   - The $Pd-N$ bond is highly polarized toward nitrogen, pulling valence electron density away from the metal and making the amido lone pair unreactive toward coupling.
   - The directional $sp^3$ hybrid orbital on nitrogen is oriented poorly for concerted overlap with the adjacent aryl $sp^2$ carbon orbital.
2. **Bite-Angle Acceleration Mechanism**:
   - Wide bite-angle diphosphines (Xantphos $\\beta_n = 111^\\circ$) force the $P-\\text{Pd}-P$ angle open.
   - This wide angle exerts mechanical compression on the opposite $C-\\text{Pd}-N$ coordination angle, forcing it down from $90^\\circ$ to $<75^\\circ$.
   - Compressing this angle brings the aryl carbon and amido nitrogen into immediate van der Waals contact, forcing orbital overlap between the developing $C-N$ bond.
   - Concurrently, steric repulsion between the diphosphine and the aryl/amido ligands raises the ground state energy, lowering the net activation barrier by $32\\text{ kJ/mol}$."""
        },
        {
            "id": "prob8_7",
            "tier": "Advanced",
            "title": "Non-Adiabatic Quantum Electron Transfer in Radical Oxidative Addition",
            "statement": "The oxidative addition of benzyl halides to $\\text{Cr}^{2+}(\\text{aq})$ proceeds via an outer-sphere Single Electron Transfer (SET) mechanism governed by Marcus theory: $\\text{Cr}^{2+} + \\text{PhCH}_2\\text{Cl} \\longrightarrow [\\text{Cr}^{3+}] + [\\text{PhCH}_2\\text{Cl}]^-\\mskip-2mu^\\bullet \\longrightarrow \\text{CrCl}^{2+} + \\text{PhCH}_2^\\bullet$. (a) Formulate the Marcus rate equation for electron transfer $k_{ET}$ as a function of the reorganization energy $\\lambda$ and standard driving force $\\Delta G^\\circ$. (b) Given $\\lambda = 180\\text{ kJ/mol}$, calculate the electron-transfer activation barrier $\\Delta G^\\ddagger$ for $\\Delta G^\\circ = -40\\text{ kJ/mol}$ versus $\\Delta G^\\circ = -100\\text{ kJ/mol}$. (c) Explain why this radical pathway bypasses the high steric barriers of tertiary alkyl halides.",
            "solution": """**Line-by-Line Solution:**

**(a) Marcus Electron Transfer Formulation:**
In classical Marcus theory for outer-sphere electron transfer, the activation free energy barrier $\\Delta G^\\ddagger$ is related to the total reorganization energy $\\lambda$ and the thermodynamic driving force $\\Delta G^\\circ$ by the parabolic equation:
\\[ \\Delta G^\\ddagger = \\frac{(\\lambda + \\Delta G^\\circ)^2}{4\\lambda} \\]
where:
- $\\lambda = \\lambda_i + \\lambda_o$ is the sum of inner-sphere vibrational and outer-sphere solvent reorganization energies.
- The electron transfer rate constant is:
  \\[ k_{ET} = \\kappa_{el} \\nu_n \\exp\\left(-\\frac{\\Delta G^\\ddagger}{RT}\\right) = \\kappa_{el} \\nu_n \\exp\\left(-\\frac{(\\lambda + \\Delta G^\\circ)^2}{4\\lambda RT}\\right) \\]

**(b) Activation Barrier Calculations:**
Given $\\lambda = 180\\text{ kJ/mol}$:

1. **For $\\Delta G^\\circ = -40\\text{ kJ/mol}$ (Moderate Driving Force)**:
   \\[ \\lambda + \\Delta G^\\circ = 180 - 40 = 140\\text{ kJ/mol} \\]
   \\[ \\Delta G^\\ddagger = \\frac{(140)^2}{4(180)} = \\frac{19,600}{720} = \\mathbf{27.22\\text{ kJ/mol}} \\]

2. **For $\\Delta G^\\circ = -100\\text{ kJ/mol}$ (Strong Driving Force)**:
   \\[ \\lambda + \\Delta G^\\circ = 180 - 100 = 80\\text{ kJ/mol} \\]
   \\[ \\Delta G^\\ddagger = \\frac{(80)^2}{4(180)} = \\frac{6,400}{720} = \\mathbf{8.89\\text{ kJ/mol}} \\]
- **Conclusion**: Increasing the thermodynamic driving force by $60\\text{ kJ/mol}$ drops the activation barrier from $27.2\\text{ kJ/mol}$ to $8.9\\text{ kJ/mol}$, accelerating the electron transfer rate by over three orders of magnitude ($>10^3$).

**(c) Why the Radical SET Pathway Bypasses Steric Congestion:**
- In the concerted or $S_N2$ oxidative addition pathway, the metal center must achieve direct orbital overlap with the $\\sigma^*(C-X)$ orbital, requiring intimate physical contact with the $\\alpha$-carbon atom. In bulky secondary and tertiary alkyl halides, the three alkyl substituents create severe steric crowding that blocks backside approach, raising $E_a$ to $>150\\text{ kJ/mol}$.
- In the outer-sphere SET mechanism:
  1. The electron transfers via long-range quantum tunneling through space (over distances of $3-5$ Å) directly into the $\\sigma^*(C-X)$ orbital of the alkyl halide.
  2. The metal never needs to penetrate the bulky coordination sphere of the alkyl carbon to deliver the electron.
  3. Once the radical anion $[R-\\text{X}]^-\\mskip-2mu^\\bullet$ forms, rapid dissociative cleavage of the carbon-halogen bond releases the planar, unencumbered tertiary alkyl radical $R^\\bullet$, which is captured in a subsequent barrierless diffusion-controlled radical combination step."""
        },
        {
            "id": "prob8_8",
            "tier": "Advanced",
            "title": "Quantum Chemical Transition State Modeling of $\\alpha$-Hydride Elimination vs. $\\beta$-Elimination",
            "statement": "Compare the energetic and orbital selection rules for $\\alpha$-hydride elimination (forming an alkylidene/carbene) versus $\\beta$-hydride elimination (forming an alkene). (a) Construct the four-membered transition state for $\\beta$-hydride elimination and the three-membered transition state for $\\alpha$-hydride elimination. (b) Explain why early transition metals in high oxidation states ($d^0 \\text{ Ta(V), W(VI)}$) favor $\\alpha$-elimination, while late metals ($d^8 \\text{ Pt(II), Pd(II)}$) favor $\\beta$-elimination. (c) Derive the kinetic isotope effect ($k_H / k_D$) for an $\\alpha$-elimination involving a C-H bond stretching frequency of $2950\\text{ cm}^{-1}$ assuming complete loss of zero-point energy in the transition state.",
            "solution": """**Line-by-Line Solution:**

**(a) Transition State Geometries:**
1. **$\\beta$-Hydride Elimination (Four-Membered Transition State)**:
   - Involves the metal, $\\alpha$-carbon, $\\beta$-carbon, and $\\beta$-hydrogen:
     \\[ [M \\cdots \\text{H}_\\beta \\cdots \\text{C}_\\beta \\cdots \\text{C}_\\alpha]^\\ddagger \\]
   - The ring is a puckered or planar **four-membered ring**.
   - Ideal dihedral angle is $0^\\circ$ (*syn*-coplanar).
   - Angle strain is moderate ($\angle(C_\\alpha-C_\\beta-\\text{H}) \\approx 100-110^\\circ$).
2. **$\\alpha$-Hydride Elimination (Three-Membered Transition State)**:
   - Involves only the metal, $\\alpha$-carbon, and $\\alpha$-hydrogen:
     \\[ [M \\cdots \\text{H}_\\alpha \\cdots \\text{C}_\\alpha]^\\ddagger \\]
   - A highly strained **three-membered ring**.
   - The acute $\\angle(M-\\text{H}_\\alpha-\\text{C}_\\alpha)$ angle ($<70^\\circ$) incurs significant geometric strain.

**(b) Electronic and Orbital Rationalization:**
1. **Why Late Transition Metals ($d^8$) Favor $\\beta$-Elimination**:
   - Late transition metals possess filled valence $d$-orbitals.
   - In $\\beta$-elimination, the formed alkene is a powerful $\\pi$-acceptor that readily accepts backdonation from the filled $d$-orbitals of the late metal, providing massive thermodynamic stabilization to the resulting $M(\\text{H})(\\text{alkene})$ intermediate.
   - Conversely, $\\alpha$-elimination would generate an alkylidene $M=\\text{CHR}$ requiring strong metal-to-ligand $\\pi$-bonding, which is disfavored by late electron-rich metals due to lone-pair repulsion.
2. **Why Early Transition Metals ($d^0$) Favor $\\alpha$-Elimination**:
   - Early metals in high oxidation states ($d^0$, such as $\\text{Ta}(\\text{V})$) possess **zero $d$-electrons**.
   - They cannot backdonate into alkene $\\pi^*$ orbitals, making alkene complexes unstable.
   - However, $d^0$ metals have multiple empty, low-lying valence $d$-orbitals.
   - An alkylidene ligand ($=CHR$) acts as a strong $\\sigma$- and $\\pi$-donor, donating 4 electrons directly into the empty metal $d$-orbitals to form a very strong, thermodynamic metal-carbon double bond ($D_0(\\text{Ta}=\\text{C}) > 450\\text{ kJ/mol}$).
   - Therefore, when $\\beta$-hydrogens are absent (as in neopentyl complexes), $d^0$ metals readily undergo $\\alpha$-elimination to form Schrock carbenes.

**(c) Primary Kinetic Isotope Effect Calculation ($k_H / k_D$):**
In transition-state theory, assuming complete loss of the $\\text{C}-\\text{H}$ stretching zero-point energy (ZPE) in the transition state:
\\[ \\frac{k_H}{k_D} = \\exp\\left( \\frac{\\Delta \\text{ZPE}}{RT} \\right) \\]
1. Zero-point energy of the $\\text{C}-\\text{H}$ harmonic oscillator:
   \\[ \\text{ZPE}_H = \\frac{1}{2} h c \\tilde{\\nu}_H \\]
2. For isotopic substitution by deuterium ($m_D \\approx 2 m_H$):
   \\[ \\tilde{\\nu}_D = \\frac{\\tilde{\\nu}_H}{\\sqrt{2}} = \\frac{2950}{\\sqrt{2}} \\approx 2086\\text{ cm}^{-1} \\]
3. Difference in zero-point energies:
   \\[ \\Delta \\tilde{\\nu} = \\tilde{\\nu}_H - \\tilde{\\nu}_D = 2950 - 2086 = 864\\text{ cm}^{-1} \\]
   In energy units:
   \\[ \\Delta \\text{ZPE} = \\frac{1}{2} h c \\Delta \\tilde{\\nu} = \\frac{1}{2} (6.626 \\times 10^{-34})(3.0 \\times 10^{10})(864) = 8.587 \\times 10^{-21}\\text{ J/molecule} \\]
   Per mole:
   \\[ \\Delta \\text{ZPE} = (8.587 \\times 10^{-21})(6.022 \\times 10^{23}) = 5,171\\text{ J/mol} = 5.17\\text{ kJ/mol} \\]
4. Compute the kinetic isotope effect at $298.15\\text{ K}$:
   \\[ \\frac{k_H}{k_D} = \\exp\\left( \\frac{5,171}{(8.3145)(298.15)} \\right) = \\exp\\left( \\frac{5,171}{2478.9} \\right) = \\exp(2.086) \\approx \\mathbf{8.05} \\]
- **Conclusion**: The theoretical maximum primary kinetic isotope effect at room temperature is **$\\approx 8.1$**. Experimental KIE values of $k_H/k_D = 6.5 - 7.5$ confirm rate-determining $\\alpha-\\text{C}-\\text{H}$ bond cleavage in Schrock carbene synthesis."""
        },
        {
            "id": "prob8_9",
            "tier": "Advanced",
            "title": "Stereoelectronic Dynamics of Reductive Elimination in High-Valent Gold(III) Complexes",
            "statement": "The reductive elimination of biaryls from square planar gold(III) complexes *cis*-$[(\\text{PPh}_3)\\text{Au}(\\text{Ar})_2\\text{Cl}]$ follows an associative or dissociative-like pathway. (a) State the oxidation state and electron count of gold before and after reductive elimination. (b) For *trans*-$[(\\text{PPh}_3)\\text{Au}(\\text{Ar})_2\\text{Cl}]$, reductive elimination is completely blocked until geometric isomerization occurs. Formulate the Berry-like pseudorotation mechanism enabling *trans* to *cis* isomerization via a 5-coordinate intermediate. (c) Explain why electron-withdrawing aryl substituents accelerate reductive elimination from gold(III).",
            "solution": """**Line-by-Line Solution:**

**(a) Oxidation State and Electron Count:**
1. **Starting Material *cis*-$[(\\text{PPh}_3)\\text{Au}(\\text{Ar})_2\\text{Cl}]$**:
   - Gold is coordinated to one phosphine ($L$), two aryls ($X_2$), and one chloride ($X$).
   - Net charge $q = 0$.
   \\[ OS(\\text{Au}) = 0 - [2(-1) + (-1)] = +3 \\implies \\mathbf{\\text{Au}(\\text{III}) (d^8)} \\]
   - Total valence electron count:
     \\[ VEC = 11 (\\text{Au}) + 2 (\\text{PPh}_3) + 2 \\times 1 (\\text{Ar}) + 1 (\\text{Cl}) = \\mathbf{16\\text{ valence electrons}} \\]
2. **Products ($[(\\text{PPh}_3)\\text{AuCl}] + \\text{Ar}-\\text{Ar}$)**:
   - Gold is coordinated to one phosphine and one chloride ($LX$).
   \\[ OS(\\text{Au}) = +1 \\implies \\mathbf{\\text{Au}(\\text{I}) (d^{10})} \\]
   - Valence electron count:
     \\[ VEC = 11 + 2 (\\text{PPh}_3) + 1 (\\text{Cl}) = \\mathbf{14\\text{ valence electrons}} \\quad (\\text{linear 2-coordinate}) \\]
- Formal change: $\\Delta OS = -2, \\Delta CN = -2, \\Delta VEC = -2$.

**(b) Trans-to-Cis Isomerization Barrier and Mechanism:**
1. Reductive elimination strictly requires orbital overlap between the two eliminating aryl groups. In the *trans* isomer, the two aryl groups are oriented $180^\\circ$ apart across the gold center; spatial overlap between their $\\sigma(\\text{Au}-\\text{C})$ orbitals is identically zero ($S_{CC} = 0$).
2. Therefore, elimination from the *trans* isomer is **completely forbidden**.
3. **Isomerization Pathway**:
   - Step 1: Phosphine dissociation or associative coordination of an incoming nucleophile/halide forms a 3-coordinate T-shaped $[\\text{Au}(\\text{Ar})_2\\text{Cl}]$ or 5-coordinate intermediate $[(\\text{PPh}_3)\\text{Au}(\\text{Ar})_2\\text{Cl}_2]^-$.
   - Step 2: The intermediate undergoes Berry pseudorotation or in-plane T-shaped inversion, interconverting axial and equatorial positions.
   - Step 3: Re-coordination generates the *cis* isomer *cis*-$[(\\text{PPh}_3)\\text{Au}(\\text{Ar})_2\\text{Cl}]$.
4. Once the *cis* geometry is achieved, the two aryl carbons are situated at $90^\\circ$ in close spatial proximity, enabling rapid, concerted reductive elimination of biaryl $\\text{Ar}-\\text{Ar}$.

**(c) Acceleration by Electron-Withdrawing Substituents:**
1. In reductive elimination from $\\text{Au}(\\text{III})$ to $\\text{Au}(\\text{I})$, two electrons from the $Au-C$ bonding orbitals are returned to the gold atom, populating a metal non-bonding $d$-orbital ($5d^8 \\to 5d^{10}$).
2. The metal center is formally **reduced**.
3. Electron-withdrawing substituents on the aryl rings (e.g., $-\\text{CF}_3, -\\text{NO}_2, -\\text{F}$) stabilize the departing organic moieties as they accumulate partial negative charge in the transition state.
4. Furthermore, electron-withdrawing groups diminish the electron density at the gold-carbon bonds, weakening the $Au-C$ bond strength and dramatically lowering the activation free energy $\\Delta G^\\ddagger$ for bond cleavage."""
        }
    ]

    return {
        "unit_number": 8,
        "title": "Fundamental Organometallic Reaction Mechanisms",
        "description": "Ligand substitution pathways (associative vs dissociative), kinetic trans-effect vs thermodynamic trans-influence in platinum complexes, concerted oxidative addition of non-polar substrates, polar oxidative addition via SN2 and radical pathways, microscopic reversibility in reductive elimination, bite-angle acceleration, 1,1-migratory insertion of carbon monoxide, 1,2-migratory insertion of alkenes into metal hydrides, and alpha- vs beta-hydride elimination mechanisms.",
        "sections": sections,
        "problems": problems
    }
