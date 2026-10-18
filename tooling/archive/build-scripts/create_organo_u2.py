"""
create_organo_u2.py
Unit 2: Main Group Organometallics: Groups 13, 14 & 15
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_2():
    sections = [
        {
            "id": "sec2_1",
            "title": "§2.1 Classification & General Synthetic Routes to Main Group Organometallics",
            "content": """Main group organometallics are compounds containing bonds between carbon and $s$- or $p$-block elements. Unlike transition metal organometallics—which utilize valence $(n-1)d$ orbitals for coordinate $\\pi$-bonding—main group species rely exclusively on valence $ns$ and $np$ orbitals, obeying the Lewis octet rule and displaying reactivity dictated by the carbon-metal electronegativity difference:
\\[ \\Delta \\chi = \\chi_\\text{C} - \\chi_\\text{M} \\]
Because carbon has an Allred-Rochow electronegativity of $2.55$, bonds to electropositive elements like lithium ($\\chi = 0.98$), magnesium ($\\chi = 1.31$), and aluminum ($\\chi = 1.61$) possess polar-covalent or ionic character with partial carbanionic character ($M^{\\delta+} - C^{\\delta-}$). As one moves rightward and downward across the periodic table through Groups 14 ($\\text{Si, Ge, Sn, Pb}$) and 15 ($\\text{P, As, Sb, Bi}$), $\\Delta \\chi$ narrows, yielding covalent, non-polar bonds.

### Primary Synthetic Methods:
1. **Oxidative Addition (Direct Synthesis)**: Elemental metal reacts directly with an organic halide:
   \\[ R-\\text{X} + 2\\,\\text{M} \\longrightarrow R-\\text{M} + \\text{M}\\text{X} \\quad (\\text{e.g., } R\\text{Li}) \\]
   \\[ R-\\text{X} + \\text{Mg} \\xrightarrow{\\text{Et}_2\\text{O}} R-\\text{MgX} \\quad (\\text{Grignard reagent}) \\]
2. **Transmetallation**: A more electropositive metal displaces a less electropositive metal from an organometallic precursor driven by the thermodynamic free energy differential:
   \\[ R-\\text{M} + \\text{M}'\\text{X} \\longrightarrow R-\\text{M}' + \\text{M}\\text{X} \\quad (\\chi_\\text{M} < \\chi_{\\text{M}'}) \\]
   For example, organolithium reagents cleanly transmetallate with zinc, copper, or tin halides:
   \\[ 4\\,R\\text{Li} + \\text{SnCl}_4 \\longrightarrow R_4\\text{Sn} + 4\\,\\text{LiCl} \\downarrow \\]
3. **Metal-Halogen Exchange**: A rapid, low-temperature equilibrium driven by carbanion thermodynamic stability:
   \\[ R-\\text{Li} + R'-\\text{X} \\rightleftharpoons R-\\text{X} + R'-\\text{Li} \\]
   The equilibrium shifts quantitatively toward the organolithium species featuring the more stable (more $s$-character or stabilized) carbanion ($sp > sp^2 > sp^3$).
4. **Hydrometallation**: Addition of an element-hydrogen bond across an alkene or alkyne:
   \\[ R_2\\text{M}-\\text{H} + \\text{H}_2\\text{C}=\\text{CH}R' \\longrightarrow R_2\\text{M}-\\text{CH}_2\\text{CH}_2R' \\]
   Exemplified by hydroboration ($B-H$), hydroalumination ($Al-H$), hydrosilylation ($Si-H$), and hydrostannylation ($Sn-H$)."""
        },
        {
            "id": "sec2_2",
            "title": "§2.2 Structure, Bonding & Solution Aggregation in Organolithium and Grignard Reagents",
            "content": """Organolithium ($R\\text{Li}$) and Grignard ($R\\text{MgX}$) reagents are premier nucleophilic carbon synthons. Their solution chemistry is governed by dynamic molecular aggregation.

### Organolithium Aggregation
Alkyllithiums aggregate extensively into oligomers stabilized by multi-center bonding between lithium and $\\alpha$-carbon atoms:
- In hydrocarbon solvents, **$n$-butyllithium** exists as an octahedral hexamer $(n\\text{-BuLi})_6$.
- **$t$-butyllithium** and **methyllithium** form tetrahedral tetramers $(R\\text{Li})_4$. In the tetramer $(Me\\text{Li})_4$, four lithium atoms occupy the vertices of a regular tetrahedron, while four methyl groups cap the four triangular $\\text{Li}_3$ faces.
- Each face involves a **4-center 2-electron ($4c-2e$) bond** formed by the overlap of three lithium $2sp^3$ hybrid orbitals and one carbon $sp^3$ hybrid orbital.
- Addition of coordinating Lewis bases (e.g., tetrahydrofuran THF, $N,N,N',N'$-tetramethylethylenediamine TMEDA) deaggregates tetramers into dimers or reactive monomers, accelerating nucleophilic addition rates by orders of magnitude:
  \\[ (n\\text{-BuLi})_6 \\xrightarrow{\\text{THF}} 3\\,(n\\text{-BuLi})_2 \\xrightarrow{\\text{TMEDA}} 6\\,(n\\text{-BuLi}\\cdot\\text{TMEDA}) \\]

### The Schlenk Equilibrium in Grignard Reagents
In ethereal solutions, organomagnesium halides participate in the dynamic **Schlenk equilibrium**:
\\[ 2\\,R\\text{MgX} \\cdot 2\\text{S} \\rightleftharpoons R_2\\text{Mg}\\cdot 2\\text{S} + \\text{MgX}_2\\cdot 2\\text{S} \\]
where $S$ represents a coordinating solvent molecule (e.g., $\\text{Et}_2\\text{O}$ or THF).
Addition of 1,4-dioxane precipitates insoluble $\\text{MgX}_2\\cdot\\text{dioxane}$, shifting the Schlenk equilibrium quantitatively to yield pure dialkylmagnesium $R_2\\text{Mg}$ in solution."""
        },
        {
            "id": "sec2_3",
            "title": "§2.3 Organoaluminum Chemistry: Trialkylaluminums, Dimeric Aggregates & MAO Cocatalysts",
            "content": """Organoaluminum compounds ($R_3\\text{Al}$) are powerful Lewis acids characterized by electron deficiency. Monomeric $R_3\\text{Al}$ possesses 6 valence electrons and a vacant $3p_z$ orbital on aluminum, adopting trigonal planar geometry ($D_{3h}$).

### Dimerization and $3c-2e$ Bonding in $\\text{Al}_2 R_6$
To alleviate electron deficiency, trialkylaluminums with unhindered alkyl groups (e.g., methyl, ethyl) dimerize into $\\text{Al}_2 R_6$:
- Trimethylaluminum exists as the dimer $\\text{Al}_2(\\text{CH}_3)_6$, containing two terminal methyls per Al and two bridging methyls in an $\\text{Al}_2(\\mu-\\text{CH}_3)_2$ core.
- The bridging $\\text{Al}-\\text{C}-\\text{Al}$ angles are acute ($75.7^\\circ$), with $\\text{Al}-\\text{C}_\\text{bridge}$ distances ($2.14$ Å) substantially longer than $\\text{Al}-\\text{C}_\\text{terminal}$ bonds ($1.97$ Å).
- Triisobutylaluminum $\\text{Al}(i\\text{-Bu})_3$ and trimesitylaluminum $\\text{Al}(\\text{Mes})_3$ remain monomeric due to steric clash between bulky groups.

### Hydroalumination with DIBAL-H
Diisobutylaluminum hydride ($[(i\\text{-Bu})_2\\text{AlH}]_n$, DIBAL-H) undergoes stereoselective *syn*-addition across alkynes and alkenes, delivering $(E)$-alkenylaluminums. At low temperature ($-78^\\circ\\text{C}$), DIBAL-H cleanly reduces esters to aldehydes by forming a stable, tetrahedral hemiacetal aluminum intermediate that resists over-reduction until aqueous quench.

### Methylaluminoxane (MAO) in Ziegler-Natta Catalysis
Controlled partial hydrolysis of $\\text{AlMe}_3$ with water:
\\[ n\\,\\text{AlMe}_3 + n\\,\\text{H}_2\\text{O} \\longrightarrow [-\\text{Al}(\\text{Me})-\\text{O}-]_n + 2n\\,\\text{CH}_4 \\uparrow \\]
yields **methylaluminoxane (MAO)**, an oligomeric cage-like Lewis acid cocatalyst. In metallocene olefin polymerization ($Cp_2\\text{ZrCl}_2$), MAO abstracts a chloride to generate the active, cationic 14-electron catalyst $[Cp_2\\text{ZrMe}]^+ [\\text{Me-MAO}]^-$, enabling polymerization activities exceeding millions of grams of polymer per mole of catalyst per hour."""
        },
        {
            "id": "sec2_4",
            "title": "§2.4 Organoboron Chemistry: Hydroboration, Organoboranes & Suzuki-Miyaura Precursors",
            "content": """Organoboranes ($R_3\\text{B}$) are neutral, monomeric Lewis acids. Boron's small covalent radius ($0.84$ Å) prevents dimerization via $3c-2e$ alkyl bridges as observed in aluminum; instead, boranes remain strictly monomeric and planar ($sp^2$, $D_{3h}$).

### Mechanism and Stereochemistry of Hydroboration
Discovered by Herbert C. Brown, hydroboration involves the concerted addition of a $B-H$ bond across an alkene:
1. **Regioselectivity**: The electrophilic boron atom adds to the less sterically hindered, less substituted carbon, while hydrogen adds to the more substituted carbon (anti-Markovnikov orientation). Sterically hindered boranes (e.g., 9-BBN, disiamylborane $\\text{Sia}_2\\text{BH}$) achieve $>99.9\\%$ regiocontrol.
2. **Stereospecificity**: Addition proceeds through a four-membered planar or puckered transition state with concerted bond formation, dictating **100% *syn*-stereospecificity**.
3. **Oxidation**: Alkaline hydrogen peroxide oxidizes organoboranes with complete retention of stereochemical configuration at carbon, yielding alcohols:
   \\[ R_3\\text{B} + 3\\,\\text{H}_2\\text{O}_2 + 3\\,\\text{NaOH} \\longrightarrow 3\\,R-\\text{OH} + \\text{Na}_3\\text{BO}_3 + 3\\,\\text{H}_2\\text{O} \\]

### Boronic Acids and Esters in Suzuki-Miyaura Cross-Coupling
Organoboronic acids $R-\\text{B}(\\text{OH})_2$ and boronate esters $R-\\text{B}(\\text{OR}')_2$ (e.g., pinacol boronates $R-\\text{Bpin}$) are thermally stable, bench-tolerant, air- and moisture-stable reagents.
In the palladium-catalyzed **Suzuki-Miyaura cross-coupling**:
\\[ R-\\text{B}(\\text{OH})_2 + R'-\\text{X} \\xrightarrow{\\text{Pd(0) cat.}, \\text{ Base}} R-R' + \\text{B}(\\text{OH})_3 + \\text{X}^- \\]
Base (e.g., $\\text{K}_2\\text{CO}_3$, $\\text{Cs}_2\\text{CO}_3$) coordinates the Lewis acidic boron atom to form a tetrahedral 'ate' complex $[R-\\text{B}(\\text{OH})_3]^-$. This coordination enhances the nucleophilicity of the organic group $R$, facilitating transmetallation to the $L_2\\text{Pd}(R')\\text{X}$ intermediate."""
        },
        {
            "id": "sec2_5",
            "title": "§2.5 Organosilicon Chemistry: $\\beta$-Silicon Effect, Silyl Ethers & Peterson Olefination",
            "content": """Silicon occupies Group 14 directly beneath carbon. With a Pauling electronegativity of $1.90$ (vs. carbon's $2.55$), the $\\text{Si}-\\text{C}$ bond is polarized $\\text{C}^{\\delta-} - \\text{Si}^{\\delta+}$, conferring nucleophilic character to carbon and electrophilic character to silicon.

### The $\\beta$-Silicon Effect
Carbocations possessing a silicon atom $\\beta$ to the positive charge are stabilized by $130-160\\text{ kJ/mol}$ relative to simple alkyl carbocations.
- **Physical Mechanism**: Hyperconjugative overlap between the filled $\\sigma(\\text{C}-\\text{Si})$ bonding orbital and the empty, orthogonal $p$-orbital of the adjacent carbocation carbon:
  \\[ \\sigma(\\text{C}-\\text{Si}) \\longrightarrow p(\\text{C}^+) \\]
- Because silicon is more electropositive than carbon, the $\\sigma(\\text{C}-\\text{Si})$ orbital has a higher energetic level and greater electron density localized on carbon, maximizing orbital overlap.
- This effect directs the regiochemistry of electrophilic additions to allylsilanes and vinylsilanes (**Hosomi-Sakurai reaction**).

### Silyl Protecting Groups
Silicon forms an exceptionally strong bond with oxygen ($D_0(\\text{Si}-\\text{O}) \\approx 530\\text{ kJ/mol}$) and fluorine ($D_0(\\text{Si}-\\text{F}) \\approx 580\\text{ kJ/mol}$). Silyl ethers ($\text{RO}-\\text{Si}R_3$) protect alcohols against harsh reagents:
- Trimethylsilyl (TMS), Triethylsilyl (TES), $t$-Butyldimethylsilyl (TBS/TBDMS), Triisopropylsilyl (TIPS), $t$-Butyldiphenylsilyl (TBDPS).
- Deprotection is driven by the thermodynamic formation of the ultra-strong $\\text{Si}-\\text{F}$ bond using fluoride donors such as tetra-$n$-butylammonium fluoride (TBAF).

### Peterson Olefination
Reaction of $\\alpha$-silyl carbanions with aldehydes or ketones yields $\\beta$-hydroxysilanes, which undergo stereospecific elimination:
- **Acidic Conditions ($H_2SO_4$)**: Anti-periplanar elimination yields $(E)$- or $(Z)$-alkenes.
- **Basic Conditions (NaH, KH)**: Intramolecular attack of oxyanion on silicon forms a four-membered siladioxetane ring, undergoing concerted *syn*-elimination with inversion of the relative stereocenter."""
        },
        {
            "id": "sec2_6",
            "title": "§2.6 Organotin Chemistry: Hydrostannylation, Radicals & Stille Cross-Coupling",
            "content": """Organotin (organostannane) compounds contain direct $\\text{Sn}-\\text{C}$ bonds. Tin has a larger covalent radius ($1.40$ Å) and a weak $\\text{Sn}-\\text{H}$ bond dissociation energy ($D_0 \\approx 310\\text{ kJ/mol}$), making organotin hydrides exceptional free radical reagents.

### Radical Dehalogenation with Tributyltin Hydride
Tri-$n$-butyltin hydride ($n\\text{-Bu}_3\\text{SnH}$, TBTH) combined with azobisisobutyronitrile (AIBN) reduces alkyl halides via a radical chain mechanism:
1. **Initiation**: AIBN thermally decomposes to 2-cyanoprop-2-yl radicals, which abstract hydrogen from $n\\text{-Bu}_3\\text{SnH}$ to generate the tributylstannyl radical $n\\text{-Bu}_3\\text{Sn}^\\bullet$.
2. **Propagation Step 1**: The stannyl radical abstracts halogen from $R-\\text{X}$, forming an alkyl radical $R^\\bullet$ and the strong tin-halogen bond:
   \\[ n\\text{-Bu}_3\\text{Sn}^\\bullet + R-\\text{X} \\longrightarrow n\\text{-Bu}_3\\text{Sn}-\\text{X} + R^\\bullet \\]
3. **Propagation Step 2**: The alkyl radical $R^\\bullet$ abstracts hydrogen from another molecule of $n\\text{-Bu}_3\\text{SnH}$:
   \\[ R^\\bullet + n\\text{-Bu}_3\\text{SnH} \\longrightarrow R-\\text{H} + n\\text{-Bu}_3\\text{Sn}^\\bullet \\]
The high selectivity arises because the rate of halogen abstraction by tin radicals exceeds hydrogen abstraction by orders of magnitude ($k \\approx 10^7 - 10^9\\text{ M}^{-1}\\text{s}^{-1}$).

### Stille Cross-Coupling
Organostannanes $R-\\text{Sn}(n\\text{-Bu})_3$ or $R-\\text{SnMe}_3$ cross-couple with organic halides/triflates under palladium catalysis:
\\[ R-\\text{SnR}'_3 + R''-\\text{X} \\xrightarrow{\\text{Pd(0)}} R-R'' + R'_3\\text{SnX} \\]
Stille couplings operate under neutral conditions compatible with sensitive functional groups (esters, aldehydes, amines). The chief industrial and pharmacological drawback is the high toxicity and bioaccumulation of organotin residues, prompting the modern preference for organoboron analogs."""
        },
        {
            "id": "sec2_7",
            "title": "§2.7 Organophosphorus & Organoarsenic Chemistry: Ylides, Wittig Reaction & Arbuzov Rearrangement",
            "content": """Group 15 organometallics feature trivalent and pentavalent oxidation states, with valence $p$- and $d$-orbital participation.

### Phosphonium Ylides and the Wittig Reaction
Reaction of triphenylphosphine $\\text{PPh}_3$ with an alkyl halide yields a phosphonium salt, which is deprotonated by strong base to yield a **phosphorus ylide** (phosphorane):
\\[ \\text{Ph}_3\\text{P} + R\\text{CH}_2\\text{X} \\longrightarrow [\\text{Ph}_3\\text{P}^+-\\text{CH}_2R]\\,\\text{X}^- \\xrightarrow{\\text{Base}} \\text{Ph}_3\\text{P}=\\text{CHR} \\longleftrightarrow \\text{Ph}_3\\text{P}^+-\\text{C}^-\\text{HR} \\]
The ylide reacts with aldehydes or ketones:
1. Nucleophilic addition forms a zwitterionic betaine or directly delivers a four-membered **oxaphosphetane** intermediate via a $[2+2]$ cycloaddition.
2. Cycloreversion driven by the enormous thermodynamic strength of the phosphorus-oxygen double bond ($D_0(\\text{P}=\\text{O}) \\approx 540\\text{ kJ/mol}$) yields an alkene and triphenylphosphine oxide $\\text{Ph}_3\\text{P}=\\text{O}$:
   \\[ \\text{Ph}_3\\text{P}=\\text{CHR} + R'\\text{CHO} \\longrightarrow \\text{Oxaphosphetane} \\longrightarrow R'\\text{CH}=\\text{CHR} + \\text{Ph}_3\\text{P}=\\text{O} \\]
Non-stabilized ylides yield predominantly $(Z)$-alkenes under kinetic control, while stabilized ylides yield $(E)$-alkenes via thermodynamic equilibration.

### The Michaelis-Arbuzov Reaction
Trialkyl phosphites $\\text{P}(\\text{OR})_3$ react with alkyl halides $R'\\text{X}$ via an associative nucleophilic displacement to generate phosphonate esters:
\\[ \\text{P}(\\text{OR})_3 + R'-\\text{X} \\longrightarrow [R'-\\text{P}^+(\\text{OR})_3]\\,\\text{X}^- \\longrightarrow R'-\\text{P}(=\\text{O})(\\text{OR})_2 + R-\\text{X} \\]
The resulting alkylphosphonates serve as Horner-Wadsworth-Emmons (HWE) reagents for $(E)$-selective olefination."""
        },
        {
            "id": "sec2_8",
            "title": "§2.8 Comparative Reactivity, Polarity Inversion (Umpolung) & Synthesis",
            "content": """The synthetic power of main group organometallics stems from **Umpolung** (polarity inversion). While alkyl halides feature electrophilic carbon centers ($C^{\\delta+}-X^{\\delta-}$), transmetallation or oxidative addition produces nucleophilic carbon centers ($C^{\\delta-}-M^{\\delta+}$).

### Periodic Reactivity Trends across Groups 13, 14, 15:
1. **Lewis Acidity vs. Lewis Basicity**:
   - Group 13 compounds ($R_3\\text{B}, R_3\\text{Al}$) are electron-deficient Lewis acids with empty $p$-orbitals.
   - Group 14 compounds ($R_4\\text{Si}, R_4\\text{Sn}$) are octet-complete, coordination-saturated Lewis acids that require hypervalent expansion to coordinate nucleophiles.
   - Group 15 compounds ($R_3\\text{P}, R_3\\text{As}$) are Lewis bases possessing an active lone pair, functioning as nucleophiles and ligands.
2. **Thermal Stability and Bond Dissociation Energies**:
   - Bond dissociation energy ($D_0(M-C)$) decreases systematically down every group:
     \\[ D_0(\\text{B}-\\text{C}) > D_0(\\text{Al}-\\text{C}) > D_0(\\text{Ga}-\\text{C}) \\]
     \\[ D_0(\\text{Si}-\\text{C}) > D_0(\\text{Ge}-\\text{C}) > D_0(\\text{Sn}-\\text{C}) > D_0(\\text{Pb}-\\text{C}) \\]
   - Consequently, organolead ($R_4\\text{Pb}$) and organobismuth ($R_3\\text{Bi}$) compounds decompose readily at modest temperatures via homolytic cleavage to generate organic radicals.
3. **Synthetic Synergies**:
   Combining reagents from different main groups enables complex molecular synthesis without transition metals, culminating in frustration-free Lewis pair (FLP) hydrogenations, radical cascade cyclizations, and enantioselective organocatalysis."""
        }
    ]

    problems = [
        {
            "id": "prob2_1",
            "tier": "Foundational",
            "title": "Bond Polarity and Electronegativity Differentials in Main Group Organometallics",
            "statement": "Using Allred-Rochow electronegativities ($\\chi_\\text{C} = 2.55, \\chi_\\text{Li} = 0.98, \\chi_\\text{Mg} = 1.31, \\chi_\\text{Al} = 1.61, \\chi_\\text{Si} = 1.90, \\chi_\\text{Sn} = 1.96$), calculate: (a) The electronegativity difference $\\Delta \\chi$ and percentage ionic character (using Hannay-Smith equation: $\\% \\text{ionic} = 16|\\Delta\\chi| + 3.5|\\Delta\\chi|^2$) for $C-Li, C-Mg, C-Al, C-Si$, and $C-Sn$ bonds. (b) Rank the bonds in order of increasing nucleophilicity of the attached carbon atom.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of $\\Delta \\chi$ and Percentage Ionic Character:**

The Hannay-Smith empirical formula for percentage ionic character is:
\\[ \\% \\text{ionic} = 16 |\\Delta \\chi| + 3.5 |\\Delta \\chi|^2 \\]

1. **Carbon-Lithium bond ($C-\\text{Li}$)**:
   - $\\Delta \\chi = 2.55 - 0.98 = 1.57$
   - $\\% \\text{ionic} = 16(1.57) + 3.5(1.57)^2 = 25.12 + 3.5(2.4649) = 25.12 + 8.63 = 33.75\\%$

2. **Carbon-Magnesium bond ($C-\\text{Mg}$)**:
   - $\\Delta \\chi = 2.55 - 1.31 = 1.24$
   - $\\% \\text{ionic} = 16(1.24) + 3.5(1.24)^2 = 19.84 + 3.5(1.5376) = 19.84 + 5.38 = 25.22\\%$

3. **Carbon-Aluminum bond ($C-\\text{Al}$)**:
   - $\\Delta \\chi = 2.55 - 1.61 = 0.94$
   - $\\% \\text{ionic} = 16(0.94) + 3.5(0.94)^2 = 15.04 + 3.5(0.8836) = 15.04 + 3.09 = 18.13\\%$

4. **Carbon-Silicon bond ($C-\\text{Si}$)**:
   - $\\Delta \\chi = 2.55 - 1.90 = 0.65$
   - $\\% \\text{ionic} = 16(0.65) + 3.5(0.65)^2 = 10.40 + 3.5(0.4225) = 10.40 + 1.48 = 11.88\\%$

5. **Carbon-Tin bond ($C-\\text{Sn}$)**:
   - $\\Delta \\chi = 2.55 - 1.96 = 0.59$
   - $\\% \\text{ionic} = 16(0.59) + 3.5(0.59)^2 = 9.44 + 3.5(0.3481) = 9.44 + 1.22 = 10.66\\%$

**(b) Ranking of Carbon Nucleophilicity:**
Nucleophilicity correlates directly with partial negative charge $\\delta^-$ at carbon and percentage ionic character:
\\[ C-\\text{Sn} < C-\\text{Si} < C-\\text{Al} < C-\\text{Mg} < C-\\text{Li} \\]
- $C-\\text{Li}$ is the most nucleophilic (most carbanionic), reacting violently with protic solvents and air.
- $C-\\text{Sn}$ and $C-\\text{Si}$ are largely covalent, bench-stable, and require activation (fluoride or transition-metal catalysts) to undergo C-C coupling."""
        },
        {
            "id": "prob2_2",
            "tier": "Foundational",
            "title": "Schlenk Equilibrium Thermodynamics in Grignard Solutions",
            "statement": "In a $0.50\\text{ M}$ solution of methylmagnesium bromide $\\text{MeMgBr}$ in diethyl ether at $298\\text{ K}$, the Schlenk equilibrium constant is $K_S = \\frac{[\\text{Me}_2\\text{Mg}][\\text{MgBr}_2]}{[\\text{MeMgBr}]^2} = 0.040$. Calculate the equilibrium concentrations of $\\text{MeMgBr}, \\text{Me}_2\\text{Mg}$, and $\\text{MgBr}_2$.",
            "solution": """**Line-by-Line Solution:**

**1. Equilibrium Equation:**
\\[ 2\\,\\text{MeMgBr} \\rightleftharpoons \\text{Me}_2\\text{Mg} + \\text{MgBr}_2 \\]

**2. Concentration Expressions:**
Let the initial concentration of $\\text{MeMgBr}$ be $C_0 = 0.50\\text{ M}$.
Let $2x$ be the concentration of $\\text{MeMgBr}$ consumed at equilibrium:
- $[\\text{MeMgBr}] = C_0 - 2x = 0.50 - 2x$
- $[\\text{Me}_2\\text{Mg}] = x$
- $[\\text{MgBr}_2] = x$

**3. Mass Action Law:**
\\[ K_S = \\frac{[\\text{Me}_2\\text{Mg}][\\text{MgBr}_2]}{[\\text{MeMgBr}]^2} = \\frac{x^2}{(0.50 - 2x)^2} \\]
Taking the square root of both sides (since all quantities are positive):
\\[ \\sqrt{K_S} = \\frac{x}{0.50 - 2x} \\]
Given $K_S = 0.040$:
\\[ \\sqrt{0.040} \\approx 0.20 \\]
\\[ \\frac{x}{0.50 - 2x} = 0.20 \\]

**4. Algebraic Solution for $x$:**
\\[ x = 0.20(0.50 - 2x) = 0.10 - 0.40x \\]
\\[ 1.40x = 0.10 \\implies x = \\frac{0.10}{1.40} \\approx 0.0714\\text{ M} \\]

**5. Final Equilibrium Concentrations:**
- $[\\text{Me}_2\\text{Mg}] = x = 0.071\\text{ M}$
- $[\\text{MgBr}_2] = x = 0.071\\text{ M}$
- $[\\text{MeMgBr}] = 0.50 - 2(0.0714) = 0.50 - 0.143 = 0.357\\text{ M}$
Thus, the monoalkyl Grignard species $\\text{MeMgBr}$ constitutes $\\approx 71.4\\%$ of the total magnesium species in diethyl ether."""
        },
        {
            "id": "prob2_3",
            "tier": "Foundational",
            "title": "Regioselectivity and Stereospecificity of Alkene Hydroboration",
            "statement": "When 1-methylcyclopentene undergoes hydroboration with $\\text{BH}_3\\cdot\\text{THF}$ followed by alkaline hydrogen peroxide oxidation: (a) Draw the structural formula and state the IUPAC name of the major product. (b) Explain why the reaction is 100% *trans*-diastereoselective despite the hydroboration being *syn*-stereospecific. (c) Account for the regiochemical preference of boron for C2 rather than C1.",
            "solution": """**Line-by-Line Solution:**

**(a) Major Product Identification:**
- Starting alkene: 1-methylcyclopentene (a trisubstituted cyclic alkene with a methyl substituent at C1).
- Hydroboration-oxidation adds $H$ and $OH$ across the double bond.
- **Major Product**: *trans*-2-methylcyclopentan-1-ol (specifically the enantiomeric pair $(1R,2R)$ and $(1S,2S)$-2-methylcyclopentanol).

**(b) Stereochemical Rationale:**
1. **Concerted *syn*-Addition**: The $B-H$ bond of the borane adds concertedly to the double bond from the same face of the cyclopentene ring through a four-centered transition state:
   \\[ B-H + C1=C2 \\longrightarrow \\text{Four-membered TS} \\longrightarrow \\text{*syn*-adduct} \\]
   Therefore, hydrogen adds to C1 and the boryl group ($\\text{BH}_2$) adds to C2 on the **same face** of the ring (*syn* orientation).
2. **Relative Orientation to Methyl Group**: Because the methyl group at C1 occupies one face of the double bond, the incoming borane approaches predominantly from the less hindered opposite face. Thus, the incoming $H$ at C1 and the methyl group at C1 end up *trans* to each other.
3. **Retention of Configuration in Oxidation**: Alkaline oxidation with $\\text{H}_2\\text{O}_2/\\text{NaOH}$ replaces the $B-C$ bond with an $O-C$ bond with **complete retention of stereochemical configuration** via an intramolecular 1,2-migration:
   \\[ R-B + \\text{OOH}^- \\longrightarrow R-B-\\text{OOH} \\longrightarrow R-O-B + \\text{OH}^- \\]
4. **Final Diastereomer**: Because $H$ and $OH$ were delivered *syn* to each other, the resulting hydroxyl group at C2 and the original methyl group at C1 reside on opposite faces of the ring, producing the **trans-2-methylcyclopentanol** diastereomer.

**(c) Regiochemical Origin:**
- C1 is a tertiary, disubstituted alkene carbon; C2 is a secondary, monosubstituted alkene carbon.
- **Steric Factor**: The bulky boryl group approaches the less hindered, secondary C2 position to minimize van der Waals repulsion with the methyl group.
- **Electronic Factor**: The partial positive charge in the polarized four-membered transition state is stabilized by the more substituted tertiary C1 carbon ($C1^{\\delta+} \\cdots C2^{\\delta-}$ with $H^{\\delta-} \\cdots B^{\\delta+}$)."""
        },
        {
            "id": "prob2_4",
            "tier": "Intermediate",
            "title": "Kinetics and Eyring Activation Parameters of Alkyl Exchange in Trimethylaluminum Dimer",
            "statement": "At $-65^\\circ\\text{C}$ in toluene-$d_8$, the $^1\\text{H}$ NMR spectrum of $\\text{Al}_2(\\text{CH}_3)_6$ displays two sharp singlets with an integration ratio of $2:1$. At room temperature ($+25^\\circ\\text{C}$), coalescence occurs to a single sharp peak. (a) Assign the two low-temperature peaks and calculate their theoretical chemical shift difference if the coalescence temperature is $T_c = -20^\\circ\\text{C}$ with exchange rate $k_c = 120\\text{ s}^{-1}$. (b) Calculate the Gibbs free energy of activation $\\Delta G^\\ddagger$ for the bridge-terminal methyl exchange using the Eyring equation. (c) Propose the detailed mechanism of the exchange.",
            "solution": """**Line-by-Line Solution:**

**(a) Peak Assignment and Chemical Shift Difference:**
- In $\\text{Al}_2(\\text{CH}_3)_6$, there are 4 terminal methyl groups and 2 bridging methyl groups ($(\\text{Me}_\\text{term})_2\\text{Al}(\\mu-\\text{Me}_\\text{bridge})_2\\text{Al}(\\text{Me}_\\text{term})_2$).
- The integration ratio is $4:2 = 2:1$.
- **Peak at high field ($\\\\approx -0.6\\text{ ppm}$)**: 2 bridging methyl groups ($6\\text{H}$).
- **Peak at lower field ($\\\\approx -0.3\\text{ ppm}$)**: 4 terminal methyl groups ($12\\text{H}$).
- At coalescence for an uncoupled two-site exchange with equal lifetimes:
  \\[ k_c = \\frac{\\pi \\Delta \\nu}{\\sqrt{2}} \\implies \\Delta \\nu = \\frac{\\sqrt{2}\\,k_c}{\\pi} \\]
  Given $k_c = 120\\text{ s}^{-1}$:
  \\[ \\Delta \\nu = \\frac{\\sqrt{2}(120)}{\\pi} = \\frac{1.4142 \\times 120}{3.1416} = \\frac{169.7}{3.1416} \\approx 54.0\\text{ Hz} \\]
  On a $400\\text{ MHz}$ spectrometer:
  \\[ \\Delta \\delta = \\frac{54.0\\text{ Hz}}{400\\text{ MHz}} = 0.135\\text{ ppm} \\]

**(b) Gibbs Free Energy of Activation ($\\Delta G^\\ddagger$):**
Using the Eyring-Polanyi equation at coalescence temperature $T_c = -20^\\circ\\text{C} = 253.15\\text{ K}$:
\\[ k_c = \\frac{\\kappa k_B T_c}{h} \\exp\\left(-\\frac{\\Delta G^\\ddagger}{R T_c}\\right) \\]
Taking $\\kappa = 1$ (transmission coefficient):
\\[ \\Delta G^\\ddagger = R T_c \\left[ \\ln\\left(\\frac{k_B T_c}{h}\\right) - \\ln(k_c) \\right] \\]
Constants:
- $k_B = 1.38065 \\times 10^{-23}\\text{ J/K}$
- $h = 6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$
- $\\frac{k_B T_c}{h} = \\frac{(1.38065 \\times 10^{-23})(253.15)}{6.62607 \\times 10^{-34}} = 5.275 \\times 10^{12}\\text{ s}^{-1}$
- $\\ln\\left(\\frac{k_B T_c}{h}\\right) = \\ln(5.275 \\times 10^{12}) \\approx 29.293$
- $\\ln(k_c) = \\ln(120) \\approx 4.787$
- Difference: $29.293 - 4.787 = 24.506$
Now compute $\\Delta G^\\ddagger$:
\\[ \\Delta G^\\ddagger = (8.3145\\text{ J/(mol}\\cdot\\text{K)})(253.15\\text{ K})(24.506) = 2104.8 \\times 24.506 = 51,580\\text{ J/mol} \\approx 51.6\\text{ kJ/mol} \\]

**(c) Mechanism of Exchange:**
The exchange can occur via two competing pathways:
1. **Dissociative Monomer-Dimer Mechanism**:
   \\[ \\text{Al}_2(\\text{CH}_3)_6 \\rightleftharpoons 2\\,\\text{Al}(\\text{CH}_3)_3 \\]
   In the monomer, all three methyl groups are equivalent ($D_{3h}$). Recombination scrambles bridging and terminal positions. However, concentration-dependent kinetic studies show the reaction rate is concentration-independent at low concentration, pointing toward an intramolecular process.
2. **Intramolecular Bridge-Opening Mechanism**:
   One of the two $3c-2e$ $\\text{Al}-(\\mu-\\text{Me})-\\text{Al}$ bonds cleaves to yield a singly bridged intermediate $[(\\text{Me})_2\\text{Al}-\\mu-\\text{Me}-\\text{Al}(\\text{Me})_3]$. Rotation around the remaining bridge followed by re-closure scrambles terminal and bridge positions with an activation barrier of $\\approx 52\\text{ kJ/mol}$."""
        },
        {
            "id": "prob2_5",
            "tier": "Intermediate",
            "title": "Quantum Mechanical Basis of the $\\beta$-Silicon Hyperconjugation Effect",
            "statement": "The rate of solvolysis of $\\beta$-trimethylsilylethyl chloride $\\text{Me}_3\\text{Si}-\\text{CH}_2\\text{CH}_2\\text{Cl}$ in aqueous ethanol is $10^{12}$ times greater than that of ethyl chloride $\\text{CH}_3\\text{CH}_2\\text{Cl}$. (a) Use molecular orbital perturbation theory to explain this $10^{12}$-fold rate acceleration. (b) Explain why the orientation of the $\\text{C}-\\text{Si}$ bond relative to the developing carbocation $p$-orbital is strictly stereoelectronic. (c) Deduce the final product of this solvolysis.",
            "solution": """**Line-by-Line Solution:**

**(a) Molecular Orbital Perturbation Theory of the $\\beta$-Silicon Effect:**
1. **Energy Level Alignment**:
   In the solvolysis transition state, ionization of the $C-Cl$ bond generates a developing vacant $p$-orbital at the $\\alpha$-carbon ($C_\\alpha^+$).
   - In ethyl chloride, the adjacent bonding orbital is $\\sigma(\\text{C}-\\text{H})$, which lies at a very low energy level ($H_{ii} \\approx -14\\text{ eV}$).
   - In $\\beta$-silyl systems, the adjacent bonding orbital is $\\sigma(\\text{C}_\\beta-\\text{Si})$. Because silicon is much more electropositive than hydrogen or carbon ($\\chi_\\text{Si} = 1.90$ vs $\\chi_\\text{C} = 2.55$), the $\\sigma(\\text{C}-\\text{Si})$ orbital is higher in energy ($H_{ii} \\approx -10.5\\text{ eV}$) and has a large coefficient at carbon.
2. **Perturbation Stabilization Energy ($\\Delta E$):**
   From second-order perturbation theory:
   \\[ \\Delta E = \\frac{|\\langle \\sigma(\\text{C}-\\text{Si}) | \\hat{H} | p(\\text{C}^+) \\rangle|^2}{\\epsilon(p(\\text{C}^+)) - \\epsilon(\\sigma(\\text{C}-\\text{Si}))} \\]
   Because $\\epsilon(\\sigma(\\text{C}-\\text{Si}))$ is closer in energy to the empty $p(\\text{C}^+)$ orbital, the energy denominator is significantly smaller, while the overlap integral in the numerator is substantially larger.
3. **Activation Barrier Reduction**:
   This hyperconjugation lowers the activation barrier $\\Delta G^\\ddagger$ by $\\approx 68\\text{ kJ/mol}$:
   \\[ \\frac{k_\\text{Si}}{k_\\text{H}} = \\exp\\left(\\frac{\\Delta\\Delta G^\\ddagger}{RT}\\right) = \\exp\\left(\\frac{68,000}{(8.314)(298)}\\right) \\approx \\exp(27.4) \\approx 8 \\times 10^{11} \\approx 10^{12} \\]

**(b) Stereoelectronic Geometry Requirement:**
- Hyperconjugation requires parallel orbital symmetry: the $\\sigma(\\text{C}_\\beta-\\text{Si})$ bonding orbital must be coplanar with the empty $p(\\text{C}_\\alpha^+)$ orbital (dihedral angle $\\theta = 0^\\circ$ or $180^\\circ$, anti-periplanar).
- If the $\\text{C}-\\text{Si}$ bond is held orthogonal to the empty $p$-orbital ($\theta = 90^\\circ$), the overlap integral is strictly zero by symmetry:
  \\[ S = S_0 \\cos(\\theta) = S_0 \\cos(90^\\circ) = 0 \\]
  Under this orthogonal geometry, the $\\beta$-silicon acceleration completely vanishes!

**(c) Final Solvolysis Product:**
- Loss of chloride generates the hyperconjugatively stabilized $\\beta$-silicon carbocation:
  \\[ \\text{Me}_3\\text{Si}-\\text{CH}_2-\\text{CH}_2^+ \\longleftrightarrow \\text{Me}_3\\text{Si}^+ \\; (\\text{H}_2\\text{C}=\\text{CH}_2) \\]
- Nucleophilic solvent ($\text{H}_2\\text{O}$ or $\text{EtOH}$) attacks the silicon atom rather than carbon, cleaving the weak $\\text{Si}-\\text{C}$ bond and releasing **ethene gas** $\\text{H}_2\\text{C}=\\text{CH}_2$ and $\\text{Me}_3\\text{SiOH}$ (or $\\text{Me}_3\\text{SiOSiMe}_3$)."""
        },
        {
            "id": "prob2_6",
            "tier": "Intermediate",
            "title": "Stereochemical Divergence in Peterson Olefination Pathways",
            "statement": "Starting from a pure diastereomer of $\\beta$-hydroxysilane $(1R,2S)$-1,2-diphenyl-2-(trimethylsilyl)ethan-1-ol: (a) Predict the alkene product formed upon treatment with sodium hydride ($\\text{NaH}$) in THF. (b) Predict the alkene product formed upon treatment with concentrated sulfuric acid ($\\text{H}_2\\text{SO}_4$). (c) Draw Newman projections rationalizing the stereochemical divergence (*syn* vs *anti* elimination).",
            "solution": """**Line-by-Line Solution:**

**(a) Basic Conditions ($\text{NaH}$ in THF):**
- **Alkene Product**: $(Z)$-1,2-diphenylethene (cis-stilbene).
- **Mechanism**:
  1. Deprotonation by $\\text{NaH}$ generates the alkoxide ion $\\text{R-O}^-$.
  2. The alkoxide oxygen performs an intramolecular nucleophilic attack on the adjacent silicon atom, forming a four-membered **1,2-oxasilethane** ring intermediate.
  3. Because the four-membered ring forces the oxygen and silicon atoms to be on the **same face** of the carbon-carbon bond, elimination must proceed with **concerted *syn*-stereospecificity**.
  4. In the $(1R,2S)$ diastereomer, placing the $O^-$ and $\\text{SiMe}_3$ groups *syn* (eclipsed in the transition state) forces both bulky phenyl groups to reside on the same side of the resulting double bond, yielding $(Z)$-stilbene.

**(b) Acidic Conditions ($\text{H}_2\text{SO}_4$):**
- **Alkene Product**: $(E)$-1,2-diphenylethene (trans-stilbene).
- **Mechanism**:
  1. Protonation of the hydroxyl group by sulfuric acid generates the excellent leaving group $-\\text{OH}_2^+$.
  2. Elimination occurs via an **E2-like *anti*-periplanar transition state** where the departing $\\text{H}_2\\text{O}$ molecule and the electropositive $\\text{SiMe}_3$ group are oriented $180^\\circ$ apart (anti-coplanar).
  3. Rotating the $(1R,2S)$ diastereomer so that the $-\\text{OH}_2^+$ and $-\\text{SiMe}_3$ groups are anti-periplanar places the two phenyl rings in an anti orientation relative to each other.
  4. Concomitant loss of water and desilylation by nucleophilic attack on silicon yields $(E)$-stilbene.

**(c) Stereochemical Divergence Summary:**
- Basic Peterson: *syn*-elimination $\\implies (Z)$-alkene.
- Acidic Peterson: *anti*-elimination $\\implies (E)$-alkene.
The Peterson olefination is completely stereochemically programmable: a single enantiopure $\\beta$-hydroxysilane precursor can be directed to either geometric isomer with $>98\\%$ diastereoselectivity simply by switching the reaction pH!"""
        },
        {
            "id": "prob2_7",
            "tier": "Advanced",
            "title": "Radical Chain Kinetics and Rate Laws of Tri-n-butyltin Hydride Dehalogenation",
            "statement": "The radical reduction of 1-bromobutane ($R\\text{Br}$) by tributyltin hydride ($n\\text{-Bu}_3\\text{SnH}$) initiated by AIBN follows a chain mechanism. (a) Write down the elementary reactions for initiation, propagation ($k_1$ and $k_2$), and termination ($k_t$). (b) Apply the steady-state approximation (SSA) to both the tributylstannyl radical $\\text{Sn}^\\bullet$ and the alkyl radical $R^\\bullet$ to derive the overall rate law for the disappearance of $R\\text{Br}$. (c) Derive the kinetic chain length $\\Lambda$.",
            "solution": """**Line-by-Line Solution:**

**(a) Elementary Reaction Mechanism:**
1. **Initiation**:
   \\[ \\text{In}_2 \\xrightarrow{k_d} 2\\,\\text{In}^\\bullet \\quad (\\text{AIBN decomposition}) \\]
   \\[ \\text{In}^\\bullet + \\text{Bu}_3\\text{SnH} \\xrightarrow{k_i} \\text{InH} + \\text{Bu}_3\\text{Sn}^\\bullet \\]
   Rate of initiation: $R_i = 2 f k_d [\\text{In}_2]$, where $f$ is the initiator efficiency factor.
2. **Propagation**:
   - Step 1 (Halogen Abstraction):
     \\[ \\text{Bu}_3\\text{Sn}^\\bullet + R\\text{Br} \\xrightarrow{k_1} \\text{Bu}_3\\text{SnBr} + R^\\bullet \\]
   - Step 2 (Hydrogen Abstraction):
     \\[ R^\\bullet + \\text{Bu}_3\\text{SnH} \\xrightarrow{k_2} R\\text{H} + \\text{Bu}_3\\text{Sn}^\\bullet \\]
3. **Termination**:
   Depending on relative concentrations, termination occurs primarily by bimolecular combination of the more persistent radical. At typical substrate concentrations ($[\\text{Bu}_3\\text{SnH}] \\ge [R\\text{Br}]$), radical recombination between two stannyl radicals dominates:
   \\[ 2\\,\\text{Bu}_3\\text{Sn}^\\bullet \\xrightarrow{2k_{t1}} \\text{Bu}_3\\text{Sn}-\\text{SnBu}_3 \\]
   Alternatively, cross-termination:
   \\[ \\text{Bu}_3\\text{Sn}^\\bullet + R^\\bullet \\xrightarrow{k_{t2}} \\text{Bu}_3\\text{Sn}-R \\]
   Or self-termination of alkyl radicals:
   \\[ 2\\,R^\\bullet \\xrightarrow{2k_{t3}} R-R \\]
   Assuming termination is dominated by the stannyl radical self-combination ($2k_{t1}$):
   \\[ R_t = 2 k_{t1} [\\text{Bu}_3\\text{Sn}^\\bullet]^2 \\]

**(b) Steady-State Approximation (SSA) and Rate Law Derivation:**
1. Set rate of initiation equal to rate of termination:
   \\[ R_i = R_t \\implies 2 f k_d [\\text{In}_2] = 2 k_{t1} [\\text{Bu}_3\\text{Sn}^\\bullet]^2 \\]
   Solving for $[\\text{Bu}_3\\text{Sn}^\\bullet]$:
   \\[ [\\text{Bu}_3\\text{Sn}^\\bullet] = \\sqrt{\\frac{f k_d [\\text{In}_2]}{k_{t1}}} \\]
2. The rate of disappearance of $R\\text{Br}$ is determined by the first propagation step:
   \\[ -\\frac{d[R\\text{Br}]}{dt} = k_1 [\\text{Bu}_3\\text{Sn}^\\bullet] [R\\text{Br}] \\]
3. Substituting $[\\text{Bu}_3\\text{Sn}^\\bullet]$:
   \\[ -\\frac{d[R\\text{Br}]}{dt} = k_1 \\left(\\frac{f k_d [\\text{In}_2]}{k_{t1}}\\right)^{1/2} [R\\text{Br}] \\]
- **Order of Reaction**: First order with respect to alkyl halide $[R\\text{Br}]$, half-order with respect to initiator $[\\text{In}_2]$, and zero order with respect to tin hydride $[\\text{Bu}_3\\text{SnH}]$.

**(c) Kinetic Chain Length ($\\Lambda$):**
The kinetic chain length is the average number of propagation cycles completed per initiating radical:
\\[ \\Lambda = \\frac{R_p}{R_i} = \\frac{k_1 [\\text{Bu}_3\\text{Sn}^\\bullet] [R\\text{Br}]}{2 f k_d [\\text{In}_2]} = \\frac{k_1 [R\\text{Br}] \\sqrt{\\frac{f k_d [\\text{In}_2]}{k_{t1}}}}{2 f k_d [\\text{In}_2]} = \\frac{k_1 [R\\text{Br}]}{2 \\sqrt{f k_d k_{t1} [\\text{In}_2]}} \\]
For typical conditions ($[R\\text{Br}] = 0.1\\text{ M}, [\\text{In}_2] = 0.005\\text{ M}, k_1 \\approx 10^7\\text{ M}^{-1}\\text{s}^{-1}$), $\\Lambda > 10^3$, indicating that a single radical initiator molecule converts thousands of alkyl halide molecules into hydrocarbon products."""
        },
        {
            "id": "prob2_8",
            "tier": "Advanced",
            "title": "Frontier Molecular Orbital Analysis of the Wittig Reaction Transition States",
            "statement": "Analyze the stereochemical mechanism of the Wittig reaction for non-stabilized versus stabilized ylides using Frontier Molecular Orbital (FMO) theory. (a) Construct the HOMO and LUMO representations of a phosphorus ylide $\\text{Ph}_3\\text{P}=\\text{CH}R$ and an aldehyde $R'\\text{CHO}$. (b) Explain why the $[2+2]$ cycloaddition forming the oxaphosphetane is thermally allowed under Woodward-Hoffmann rules via a $[\\pi 2_s + \\pi 2_a]$ or puckered pathway. (c) Derive why non-stabilized ylides kinetically favor the $(Z)$-alkene, while stabilized ylides yield the $(E)$-alkene.",
            "solution": """**Line-by-Line Solution:**

**(a) Frontier Molecular Orbitals of Ylide and Carbonyl:**
1. **Phosphorus Ylide $\\text{Ph}_3\\text{P}^+-\\text{C}^-\\text{HR}$**:
   - The HOMO is localized predominantly on the carbanionic $\\alpha$-carbon as a high-energy $2p$ lone pair ($\pi$-type).
   - The LUMO is predominantly $\\sigma^*(\text{P}-\\text{C})$ and phosphorus $3d$/$\sigma^*$ orbitals.
2. **Aldehyde $R'\\text{CHO}$**:
   - The LUMO is the $\\pi^*(\text{C}=\\text{O})$ antibonding orbital, with the largest atomic orbital coefficient at the carbonyl carbon atom.
   - The HOMO is the non-bonding oxygen lone pair $n_O$.
3. **Primary Orbital Interaction**:
   - The primary stabilizing interaction is $\\text{HOMO}_\\text{ylide} (C_\\alpha) \\longrightarrow \\text{LUMO}_\\text{carbonyl} (C_\\text{carbonyl}=\\text{O})$.

**(b) Woodward-Hoffmann Analysis of the $[2+2]$ Cycloaddition:**
- A concerted $[\\pi 2_s + \\pi 2_s]$ cycloaddition between two parallel $\\pi$-systems is symmetry-forbidden in the ground state because the HOMO-LUMO overlap leads to an antibonding phase clash.
- However, the Wittig addition proceeds either:
  1. Via an asynchronous, orthogonal $[\\pi 2_s + \\pi 2_a]$ approach where the ylide $p$-orbital approaches the carbonyl $\\pi^*$ orbital at a right angle ($90^\\circ$ geometry), which is **symmetry-allowed**.
  2. Via an early, puckered four-membered transition state involving nucleophilic attack of the ylide carbon on the carbonyl carbon accompanied by concomitant dative coordination of the oxygen lone pair into vacant/polarizable phosphorus orbitals ($\text{P}-\text{O}$ dative bond formation).
- Density functional theory (DFT) calculations confirm that oxaphosphetane formation occurs via a low-barrier, concerted asynchronous $[2+2]$ addition without discrete betaine intermediates in non-polar solvents.

**(c) Stereochemical Divergence (Non-Stabilized vs. Stabilized Ylides):**
1. **Non-Stabilized Ylides ($R = \\text{alkyl}$)**:
   - The ylide carbon is highly nucleophilic and electron-rich; cycloaddition is fast, irreversible, and kinetically controlled.
   - In the orthogonal transition state, the ylide $R$ group and the aldehyde $R'$ group orient themselves to minimize steric clash with the bulky triphenylphosphine ligands ($\\text{PPh}_3$).
   - The lowest-energy transition state ($TS_Z$) places the two $R$ and $R'$ groups *cis* in the oxaphosphetane to avoid steric conflict with the phenyl rings of $\\text{PPh}_3$.
   - Rapid cycloreversion of this *cis*-oxaphosphetane delivers the **$(Z)$-alkene** as the kinetic product ($>95\\%$ $(Z)$).
2. **Stabilized Ylides ($R = \\text{CO}_2\\text{Et}, \\text{CN}, \\text{COR}$)**:
   - The ylide negative charge is delocalized into the electron-withdrawing group, diminishing nucleophilicity.
   - The activation barrier is higher, and oxaphosphetane formation becomes **reversible**.
   - The *cis*- and *trans*-oxaphosphetanes equilibrate back to starting materials.
   - Because the *trans*-oxaphosphetane (with $R$ and $R'$ on opposite faces) is thermodynamically more stable by $\\approx 15-25\\text{ kJ/mol}$, cycloreversion occurs predominantly from the *trans* isomer, yielding the **$(E)$-alkene** ($>95\\%$ $(E)$)."""
        },
        {
            "id": "prob2_9",
            "tier": "Advanced",
            "title": "Frustrated Lewis Pair (FLP) Thermodynamics and Dihydrogen Heterolysis",
            "statement": "Bulky organoboranes combined with bulky phosphines form Frustrated Lewis Pairs (FLPs) that heterolytically split dihydrogen $\\text{H}_2$. For the system $\\text{P}(t\\text{-Bu})_3 + \\text{B}(\\text{C}_6\\text{F}_5)_3 + \\text{H}_2 \\rightleftharpoons [\\text{HP}(t\\text{-Bu})_3]^+ [\\text{HB}(\\text{C}_6\\text{F}_5)_3]^-$: (a) Explain why steric frustration prevents adduct formation $\\text{R}_3\\text{P}-\\text{B}\\text{Ar}_3$. (b) Derive the thermodynamic cycle relating the gas-phase heterolytic cleavage free energy of $\\text{H}_2$ to the proton affinity ($PA$) of the phosphine and the hydride affinity ($HA$) of the borane. (c) Calculate $\\Delta G^\\circ$ for the net reaction given $HA(\\text{B}(\\text{C}_6\\text{F}_5)_3) = 320\\text{ kJ/mol}$, $PA(\\text{P}(t\\text{-Bu})_3) = 985\\text{ kJ/mol}$, and the heterolytic bond dissociation energy of $\\text{H}_2$ is $\\Delta G_\\text{het}^\\circ(\\text{H}_2) = 1530\\text{ kJ/mol}$ in solution (taking solvation energy into account $\\Delta G_\\text{solv} = -280\\text{ kJ/mol}$).",
            "solution": """**Line-by-Line Solution:**

**(a) Steric Frustration and Adduct Prevention:**
- In an unhindered system (e.g., $\\text{PMe}_3 + \\text{BMe}_3$), the Lewis base donor lone pair overlaps with the empty $2p_z$ orbital of the Lewis acid to form a strong, classical dative adduct $\\text{Me}_3\\text{P}-\\text{BMe}_3$ with bond dissociation energy $\\approx 80-120\\text{ kJ/mol}$.
- When sterically encumbered substituents are introduced:
  - $\\text{P}(t\\text{-Bu})_3$ has a Tolman cone angle of $\\theta = 182^\\circ$.
  - $\\text{B}(\\text{C}_6\\text{F}_5)_3$ has three bulky perfluorophenyl rings shielding the boron center.
- Direct $P-B$ bond formation would force the bulky $t$-butyl groups and $\\text{C}_6\\text{F}_5$ rings into catastrophic van der Waals overlap:
  \\[ \\Delta G_{\\text{adduct}} = \\Delta H_{\\text{dative}} + \\Delta G_{\\text{steric}} > 0 \\]
- Because steric repulsion $\\Delta G_{\\text{steric}}$ exceeds the electronic bonding energy, classical adduct formation is prevented. The unquenched Lewis acidic boron ($2p_z$) and Lewis basic phosphorus (lone pair) sites remain exposed in solution—creating a 'frustrated' pair.

**(b) Thermodynamic Born-Haber Cycle for $\\text{H}_2$ Heterolysis:**
The heterolytic activation of $\\text{H}_2$ by an FLP:
\\[ \\text{Base} + \\text{Acid} + \\text{H}_2 \\rightleftharpoons [\\text{Base}-\\text{H}]^+ + [\\text{Acid}-\\text{H}]^- \\]
can be broken down into three fundamental thermodynamic steps:
1. **Heterolysis of Dihydrogen**:
   \\[ \\text{H}_2 \\longrightarrow \\text{H}^+ + \\text{H}^- \\quad (\\Delta G_1 = \\Delta G_\\text{het}^\\circ(\\text{H}_2)) \\]
2. **Protonation of the Lewis Base**:
   \\[ \\text{Base} + \\text{H}^+ \\longrightarrow [\\text{Base}-\\text{H}]^+ \\quad (\\Delta G_2 = -PA(\\text{Base})) \\]
3. **Hydride Addition to the Lewis Acid**:
   \\[ \\text{Acid} + \\text{H}^- \\longrightarrow [\\text{Acid}-\\text{H}]^- \\quad (\\Delta G_3 = -HA(\\text{Acid})) \\]
Summing the thermodynamic steps:
\\[ \\Delta G_\\text{rxn}^\\circ = \\Delta G_\\text{het}^\\circ(\\text{H}_2) - PA(\\text{Base}) - HA(\\text{Acid}) + \\Delta G_\\text{solv} \\]

**(c) Numerical Calculation of $\\Delta G^\\circ$:**
Given:
- $\\Delta G_\\text{het}^\\circ(\\text{H}_2) = +1530\\text{ kJ/mol}$
- $PA(\\text{P}(t\\text{-Bu})_3) = 985\\text{ kJ/mol}$
- $HA(\\text{B}(\\text{C}_6\\text{F}_5)_3) = 320\\text{ kJ/mol}$
- $\\Delta G_\\text{solv} = -280\\text{ kJ/mol}$ (stabilization of resulting ion pair by dichloromethane solvent)

Substitute into the thermodynamic cycle:
\\[ \\Delta G^\\circ = 1530 - 985 - 320 + (-280) \\]
\\[ \\Delta G^\\circ = 1530 - 1585 = -55\\text{ kJ/mol} \\]
- **Conclusion**: The heterolytic splitting of dihydrogen is thermodynamically favorable by $\\mathbf{-55\\text{ kJ/mol}}$. The enormous combined driving force of proton affinity at phosphorus and hydride affinity at boron, augmented by favorable ion-pair electrostatic solvation, drives the spontaneous, metal-free splitting of dihydrogen at room temperature."""
        }
    ]

    return {
        "unit_number": 2,
        "title": "Main Group Organometallics: Groups 13, 14 & 15",
        "description": "Classification, synthesis, structure and bonding of main group organometallics. Multi-center bonding in organolithium aggregates and organoaluminum dimers, the Schlenk equilibrium in Grignard reagents, hydroboration stereochemistry and Suzuki coupling precursors, organosilicon chemistry and the beta-silicon effect, Peterson olefination, organotin radical chemistry, Wittig ylides and Arbuzov reactions, and Frustrated Lewis Pairs.",
        "sections": sections,
        "problems": problems
    }
