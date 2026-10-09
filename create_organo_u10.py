"""
create_organo_u10.py
Unit 10: Industrial Catalytic Processes: Polymerization, Carbonylation & Syngas Chemistry
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_10():
    sections = [
        {
            "id": "sec10_1",
            "title": "§10.1 Ziegler-Natta Catalysis: Heterogeneous Titanium Catalysts & The Cossee-Arlman Mechanism",
            "content": """Discovered in 1953 by Karl Ziegler and Giulio Natta (Nobel Prize in Chemistry, 1963), **Ziegler-Natta catalysis** enabled the stereospecific coordination polymerization of ethylene and $\\alpha$-olefins (propylene) under ambient pressure and temperature, founding the modern plastics industry.

### Catalyst Formulation:
Classical heterogeneous Ziegler-Natta catalysts combine a transition metal halide in a sub-maximal oxidation state with an organoaluminum main-group alkylating agent:
\\[ \\alpha\\text{-TiCl}_3 + \\text{Al}(\\text{C}_2\\text{H}_5)_3 \\quad \\text{or} \\quad \\text{TiCl}_4 + \\text{AlEt}_3 / \\text{MgCl}_2 \\text{ (supported)} \\]
Alkylation by triethylaluminum generates an octahedral titanium(III) active center on the surface of the $\\text{TiCl}_3$ crystal lattice possessing an alkyl group and a **vacant coordination site** ($\square$).

### The Cossee-Arlman Mechanism (1964):
P. Cossee and E.J. Arlman formulated the monometallic mechanism for coordination polymerization:
1. **$\pi$-Complexation**: An incoming ethylene or propylene molecule coordinates datively into the vacant coordination site adjacent to the growing titanium-polymer chain ($R$):
   \\[ [(\\text{Cl})_4\\text{Ti}(R)(\\square)] + \\text{H}_2\\text{C}=\\text{CH}_2 \\rightleftharpoons [(\\text{Cl})_4\\text{Ti}(R)(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}_2)] \\]
2. **Four-Centered Migratory Insertion**:
   The growing polymer chain migrates onto the coordinated alkene via a coplanar four-centered transition state:
   \\[ [(\\text{Cl})_4\\text{Ti}(R)(\\eta^2-\\text{C}_2\\text{H}_4)] \\longrightarrow \\begin{pmatrix} \\text{Ti} & - & R \\\\ \\vert & & \\vert \\\\ \\text{CH}_2 & - & \\text{CH}_2 \\end{pmatrix}^\\ddagger \\longrightarrow [(\\text{Cl})_4\\text{Ti}(\\square)(\\text{CH}_2\\text{CH}_2 R)] \\]
3. **Chain Migration and Site Inversion**:
   Migratory insertion elongates the polymer chain by one monomer unit and vacates the site previously occupied by the chain.
4. **Back-Skip (Migration) vs. Direct Alternate Insertion**:
   In propylene polymerization, the growing chain migrates back to its original site (site epimerization) or continues inserting at the newly vacated site, dictating tacticity."""
        },
        {
            "id": "sec10_2",
            "title": "§10.2 Homogeneous Metallocene & Post-Metallocene Polymerization: Kaminsky Catalysts",
            "content": """In 1980, Walter Kaminsky and Hansjörg Sinn discovered that adding methylaluminoxane (MAO) to group 4 metallocene dichlorides ($Cp_2\\text{ZrCl}_2$) creates homogeneous catalysts with activities exceeding $10^7\\text{ g polymer / (mol Zr}\\cdot\\text{h)}$.

### Activation and Structure of the Active Cation:
1. **Methylation**: MAO first alkylates the metallocene dichloride to form $Cp_2\\text{ZrMeCl}$ and $Cp_2\\text{ZrMe}_2$.
2. **Chloride/Methyl Abstraction**: MAO acts as a powerful Lewis acidic cage, abstracting a methide ($Me^-$) to generate a separated ion pair:
   \\[ Cp_2\\text{ZrMe}_2 + \\text{MAO} \\rightleftharpoons [Cp_2\\text{ZrMe}]^+ [\\text{Me-MAO}]^- \\]
3. **Electronic State of the Cation**:
   The active catalyst is the cationic 14-electron $d^0$ zirconium species $[Cp_2\\text{ZrMe}]^+$.
   - Possesses two vacant coordination orbitals in the equatorial wedge.
   - The formal positive charge drastically lowers the LUMO energy, accelerating olefin coordination.
   - The activation barrier for ethylene migratory insertion into the $[\\text{Zr-Me}]^+$ bond is only $\\Delta G^\\ddagger \\approx 20-30\\text{ kJ/mol}$, enabling thousands of monomer insertions per second.

### Constrained Geometry Catalysts (CGC):
Developed by Dow Chemical and Exxon, half-sandwich amido-cyclopentadienyl complexes ($[\\eta^5-\\text{C}_5\\text{Me}_4-\\text{SiMe}_2-\\eta^1-\\text{N}t\\text{-Bu}]\\text{TiCl}_2$) feature an open coordination wedge ($102^\\circ$), allowing the incorporation of bulky comonomers (1-octene) into linear low-density polyethylene (LLDPE)."""
        },
        {
            "id": "sec10_3",
            "title": "§10.3 Stereocontrol in Polypropylene: Isotactic, Syndiotactic & Atactic Polymers",
            "content": """Because propylene ($\\text{H}_2\\text{C}=\\text{CH}-\\text{CH}_3$) is a prochiral monomer, each insertion generates a new tertiary stereocenter along the polymer backbone, yielding distinct stereochemical architectures (**tacticity**):

1. **Isotactic Polypropylene (i-PP)**:
   - All methyl groups reside on the **same side** of the extended zigzag carbon backbone (all $(R)$ or all $(S)$ configurations).
   - Highly crystalline, rigid thermoplastic with high melting point ($T_m \\approx 165^\\circ\\text{C}$).
   - **Catalyst Symmetry**: Synthesized using chiral, $C_2$-symmetric ansa-metallocenes (e.g., *rac*-[$\\text{Me}_2\\text{Si}(\\text{Indenyl})_2\\text{ZrCl}_2$]).
   - **Mechanism: Site Control (Enantiomorphic Site Control)**: The two coordination sites in a $C_2$-symmetric metallocene are homotopic. The monomer always approaches with the same prochiral face (*re* or *si*), enforcing stereochemical fidelity even after an occasional mistake.
2. **Syndiotactic Polypropylene (s-PP)**:
   - Methyl groups alternate regularly between opposite sides of the chain ($R, S, R, S, \\dots$).
   - Crystalline polymer ($T_m \\approx 130^\\circ\\text{C}$).
   - **Catalyst Symmetry**: Synthesized using $C_s$-symmetric ansa-metallocenes (e.g., $[\\text{Me}_2\\text{C}(\\text{Fluorenyl})(Cp)\\text{ZrCl}_2]$).
   - **Mechanism**: The two coordination sites are enantiotopic. Alternating insertion between the two sites alternates the facial approach of propylene.
3. **Atactic Polypropylene (a-PP)**:
   - Methyl groups are randomly distributed along the chain.
   - Amorphous, tacky, rubber-like material with no crystalline melting point ($T_g \\approx -10^\\circ\\text{C}$).
   - Produced by achiral, $C_{2v}$-symmetric catalysts (unbridged $Cp_2\\text{ZrCl}_2$)."""
        },
        {
            "id": "sec10_4",
            "title": "§10.4 Carbonylation of Methanol: The Industrial Monsanto Acetic Acid Process",
            "content": """Developed in 1968 by Monsanto, the rhodium-catalyzed carbonylation of methanol produces acetic acid under mild conditions ($150-200^\\circ\\text{C}, 30-60\\text{ bar}$):
\\[ \\text{CH}_3\\text{OH} + \\text{CO} \\xrightarrow{\\text{Rh cat.},\\, \\text{HI}} \\text{CH}_3\\text{COOH} \\]
The process operates with $>99\\%$ selectivity toward acetic acid.

### Synergistic Organic-Inorganic Dual Cycles:
1. **The Organic Iodide Cycle**:
   Methanol is converted to methyl iodide by hydroiodic acid:
   \\[ \\text{CH}_3\\text{OH} + \\text{HI} \\rightleftharpoons \\text{CH}_3\\text{I} + \\text{H}_2\\text{O} \\]
2. **The Rhodium Organometallic Cycle**:
   - **Active Catalyst**: Square planar, 16-electron rhodium(I) dicarbonyldiiodide $[\\text{cis}-\\text{Rh}(\\text{CO})_2\\text{I}_2]^-$.
   - **Step 1: Oxidative Addition (Rate-Determining Step)**:
     Methyl iodide undergoes nucleophilic $S_N2$ oxidative addition to $[\\text{Rh}(\\text{CO})_2\\text{I}_2]^-$, forming an octahedral 18-electron rhodium(III) methyl complex:
     \\[ [\\text{Rh}(\\text{CO})_2\\text{I}_2]^- + \\text{CH}_3\\text{I} \\xrightarrow{k_1 \\text{ (RDS)}} [(\\text{CH}_3)\\text{Rh}(\\text{CO})_2\\text{I}_3]^- \\quad (18\\text{e}) \\]
   - **Step 2: 1,1-Migratory Insertion**:
     Rapid migration of the methyl group onto an adjacent CO ligand forms a 16-electron acyl complex:
     \\[ [(\\text{CH}_3)\\text{Rh}(\\text{CO})_2\\text{I}_3]^- \\longrightarrow [(\\text{CH}_3\\text{CO})\\text{Rh}(\\text{CO})\\text{I}_3]^- \\quad (16\\text{e}) \\]
   - **Step 3: CO Coordination**:
     Carbon monoxide coordinates into the vacant site:
     \\[ [(\\text{CH}_3\\text{CO})\\text{Rh}(\\text{CO})\\text{I}_3]^- + \\text{CO} \\longrightarrow [(\\text{CH}_3\\text{CO})\\text{Rh}(\\text{CO})_2\\text{I}_3]^- \\quad (18\\text{e}) \\]
   - **Step 4: Reductive Elimination**:
     Concerted reductive elimination releases acetyl iodide and regenerates the active rhodium(I) catalyst:
     \\[ [(\\text{CH}_3\\text{CO})\\text{Rh}(\\text{CO})_2\\text{I}_3]^- \\longrightarrow \\text{CH}_3\\text{COI} + [\\text{Rh}(\\text{CO})_2\\text{I}_2]^- \\]
3. **Hydrolysis Step**:
   Acetyl iodide is rapidly hydrolyzed by water to produce acetic acid and regenerate $\\text{HI}$:
   \\[ \\text{CH}_3\\text{COI} + \\text{H}_2\\text{O} \\longrightarrow \\text{CH}_3\\text{COOH} + \\text{HI} \\]"""
        },
        {
            "id": "sec10_5",
            "title": "§10.5 The BP Cativa Acetic Acid Process: Iridium Catalysis & Ruthenium Promotion",
            "content": """In 1996, BP Chemicals commercialized the **Cativa process**, replacing rhodium with an iridium-based catalytic system promoted by ruthenium:
\\[ \\text{CH}_3\\text{OH} + \\text{CO} \\xrightarrow{[\\text{Ir}(\\text{CO})_2\\text{I}_2]^-,\\, [\\text{Ru}(\\text{CO})_3\\text{I}_3]^-,\\, \\text{HI}} \\text{CH}_3\\text{COOH} \\]

### Mechanistic Differences Between Rhodium and Iridium:
1. **Oxidative Addition**:
   - In iridium, the $5d$ orbitals are higher in energy and more nucleophilic. Oxidative addition of $\\text{CH}_3\\text{I}$ to $[\\text{Ir}(\\text{CO})_2\\text{I}_2]^-$ is **150 times faster** than with rhodium!
2. **The Turn-Over Bottleneck**:
   - However, the subsequent migratory insertion of the methyl group into CO is **$10^5$ times slower** on iridium than on rhodium.
   - The hexacoordinate 18-electron intermediate $[(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^-$ accumulates as the catalyst resting state.
   - Migratory insertion cannot occur until an iodide ligand dissociates to create an open coordination site, which is thermodynamically unfavorable.

### The Role of the Ruthenium Promoter:
BP discovered that adding co-catalytic ruthenium (e.g., $[\\text{Ru}(\\text{CO})_3\\text{I}_3]^-$) accelerates the reaction dramatically:
- The ruthenium species acts as a **halide sponge**, abstracting an iodide ligand from the resting state:
  \\[ [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^- + [\\text{Ru}(\\text{CO})_3\\text{I}_2] \\rightleftharpoons [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2] + [\\text{Ru}(\\text{CO})_3\\text{I}_3]^- \\]
- Halide abstraction creates the neutral, highly reactive 5-coordinate intermediate $[(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2]$, which undergoes rapid CO insertion and reductive elimination.
- **Industrial Benefits**: Cativa operates at lower water content ($2-5\\%$ vs $14-15\\%$ in Monsanto), reducing the water-gas shift side reaction ($CO + H_2O \\to CO_2 + H_2$), minimizing separation costs, and lowering capital investment by $30\\%$."""
        },
        {
            "id": "sec10_6",
            "title": "§10.6 The Water-Gas Shift Reaction (WGSR): Homogeneous & Heterogeneous Pathways",
            "content": """The **Water-Gas Shift Reaction (WGSR)** is an essential industrial transformation for hydrogen production and adjusting syngas $\\text{H}_2/\\text{CO}$ ratios:
\\[ \\text{CO} + \\text{H}_2\\text{O} \\rightleftharpoons \\text{CO}_2 + \\text{H}_2 \\quad (\\Delta H_{298}^\\circ = -41.2\\text{ kJ/mol}) \\]

### Thermodynamics:
Because the reaction is moderately exothermic, low temperatures favor high equilibrium conversion to $\\text{H}_2$ and $\\text{CO}_2$:
\\[ \\ln K_p = \\frac{41,200}{RT} + \\frac{\\Delta S^\\circ}{R} \\]
Industrial plants operate in two stages:
1. **High-Temperature Shift (HTS)**: $350 - 450^\\circ\\text{C}$ over $\\text{Fe}_3\\text{O}_4-\\text{Cr}_2\\text{O}_3$ (fast kinetics).
2. **Low-Temperature Shift (LTS)**: $200 - 250^\\circ\\text{C}$ over $\\text{Cu/ZnO/Al}_2\\text{O}_3$ (thermodynamic conversion).

### Homogeneous Organometallic WGSR Mechanism:
Homogeneous catalysts (e.g., $[\\text{Fe}(\\text{CO})_5], [\\text{Ru}_3(\\text{CO})_{12}], [\\text{Rh}_2(\\text{CO})_4\\text{I}_4]^{2-}$) operate at $100-150^\\circ\\text{C}$ in basic media:
1. **Nucleophilic Attack of Hydroxide on Coordinated Carbonyl**:
   \\[ [L_n M-\\text{CO}] + \\text{OH}^- \\longrightarrow [L_n M-\\text{COOH}]^- \\quad (\\text{Hydroxycarbonyl / Metallocarboxylic Acid}) \\]
2. **Decarboxylation**:
   Intramolecular $\\beta$-elimination releases carbon dioxide and generates a metal hydride:
   \\[ [L_n M-\\text{COOH}]^- \\longrightarrow [L_n M-\\text{H}]^- + \\text{CO}_2 \\uparrow \\]
3. **Protonation and Dihydrogen Release**:
   Protonation of the hydride releases molecular dihydrogen and regenerates the empty coordination site:
   \\[ [L_n M-\\text{H}]^- + \\text{H}_2\\text{O} \\longrightarrow [L_n M] + \\text{H}_2 \\uparrow + \\text{OH}^- \\]
4. **Carbonylation**:
   Binding of carbon monoxide regenerates $[L_n M-\\text{CO}]$, completing the closed cycle."""
        },
        {
            "id": "sec10_7",
            "title": "§10.7 Fischer-Tropsch Synthesis: Syngas Conversion to Liquid Hydrocarbons",
            "content": """Developed in 1925 by Franz Fischer and Hans Tropsch, the **Fischer-Tropsch (FT) synthesis** converts synthesis gas (syngas, $\\text{CO} + \\text{H}_2$) into liquid synthetic fuels (synfuels), diesel, and chemical feedstocks:
\\[ (2n + 1)\\,\\text{H}_2 + n\\,\\text{CO} \\xrightarrow{\\text{Fe or Co cat.}} \\text{C}_n\\text{H}_{2n+2} + n\\,\\text{H}_2\\text{O} \\quad (\\Delta H^\\circ \\approx -165\\text{ kJ/mol per CH}_2) \\]

### Competing Mechanistic Paradigms:
1. **The Carbide (Surface Methylidene) Mechanism (Fischer-Tropsch / Biloen)**:
   - Carbon monoxide dissociates dissociatively on the metal surface into surface carbon ($C_\\text{ad}$) and oxygen ($O_\\text{ad}$):
     \\[ \\text{CO} \\longrightarrow \\text{C}_\\text{ad} + \\text{O}_\\text{ad} \\]
   - Stepwise hydrogenation yields surface methylene monomers ($=\\text{CH}_{2,\\text{ad}}$):
     \\[ \\text{C}_\\text{ad} \\xrightarrow{+\\text{H}} \\text{CH}_\\text{ad} \\xrightarrow{+\\text{H}} \\text{CH}_{2,\\text{ad}} \\]
   - Chain growth proceeds by successive insertion of surface methylene fragments into surface alkyl chains ($M-\\text{R} + \\text{CH}_2 \\to M-\\text{CH}_2\\text{R}$).
2. **The CO-Insertion (Alkyl-Acyl) Mechanism (Pichler-Schulz)**:
   - Undissociated CO undergoes migratory insertion into a metal-alkyl bond, followed by hydrogenation of the acyl oxygen to release water and advance the chain by one methylene unit.

Industrial operations utilize precipitated **iron catalysts** (Sasol High-Temperature Fischer-Tropsch, $320-350^\\circ\\text{C}$ for gasoline and $\\alpha$-olefins) or supported **cobalt catalysts** (Low-Temperature Fischer-Tropsch, $200-240^\\circ\\text{C}$ for high-cetane diesel and waxes)."""
        },
        {
            "id": "sec10_8",
            "title": "§10.8 The Anderson-Schulz-Flory (ASF) Distribution & Future Catalytic Horizons",
            "content": """Because Fischer-Tropsch chain growth proceeds via stepwise statistical polymerization, the distribution of hydrocarbon chain lengths is governed by the **Anderson-Schulz-Flory (ASF) distribution**.

### Mathematical Derivation of the ASF Model:
Let $\\alpha$ be the chain propagation probability:
\\[ \\alpha = \\frac{R_p}{R_p + R_t} \\]
where $R_p$ is the rate of chain propagation (methylene insertion) and $R_t$ is the rate of chain termination (hydrogenation to alkane or $\\beta$-elimination to alkene).
- The mole fraction of a hydrocarbon of chain length $n$ ($x_n$) is:
  \\[ x_n = (1 - \\alpha) \\alpha^{n-1} \\]
- The weight fraction ($w_n$) of chain length $n$ is:
  \\[ w_n = n (1 - \\alpha)^2 \\alpha^{n-1} \\]
Taking the natural logarithm of the weight fraction equation:
\\[ \\ln\\left(\\frac{w_n}{n}\\right) = n \\ln(\\alpha) + \\ln\\left( \\frac{(1 - \\alpha)^2}{\\alpha} \\right) \\]
A plot of $\\ln(w_n/n)$ versus carbon number $n$ yields a straight line with slope $\\ln(\\alpha)$, allowing experimental determination of the propagation probability.

### Theoretical Maxima of Hydrocarbon Cuts:
- Methane ($n=1$): $100\\%$ at $\\alpha = 0$.
- Gasoline cut ($C_5 - C_{11}$): Theoretical maximum is only **$48\\text{ wt}\\%$** (at $\\alpha \\approx 0.76$).
- Diesel cut ($C_{12} - C_{18}$): Theoretical maximum is only **$30\\text{ wt}\\%$** (at $\\alpha \\approx 0.88$).

Because the ASF distribution imposes rigid mathematical limits on direct synfuel selectivity, modern refineries operate cobalt FT at high $\\alpha > 0.90$ to maximize heavy waxes ($C_{20+}$), followed by mild hydrocracking to produce $100\\%$ diesel and jet fuel."""
        }
    ]

    problems = [
        {
            "id": "prob10_1",
            "tier": "Foundational",
            "title": "Kinetics of the Monsanto Acetic Acid Catalytic Cycle",
            "statement": "In the Monsanto process, the overall reaction rate is given by: $\\text{Rate} = k_1 [\\text{Rh}][\\text{CH}_3\\text{I}]$, completely independent of $[\\text{CO}]$ and $[\\text{CH}_3\\text{OH}]$. (a) Explain why the rate is zero-order in $\\text{CO}$ and methanol. (b) Identify the catalyst resting state (CRS) and the turnover-limiting step (TLS). (c) Given $k_1 = 3.5 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}$ at $180^\\circ\\text{C}$, calculate the rate of acetic acid production in a $500\\text{ L}$ reactor containing $2.0\\text{ mM}$ rhodium catalyst and $0.40\\text{ M}$ methyl iodide.",
            "solution": """**Line-by-Line Solution:**

**(a) Physical Origin of Zero-Order Kinetics in CO and Methanol:**
1. In the Monsanto catalytic cycle, methanol does not react directly with the rhodium catalyst; it reacts with $\\text{HI}$ in a rapid, separate organic pre-equilibrium to produce methyl iodide:
   \\[ \\text{CH}_3\\text{OH} + \\text{HI} \\xrightleftharpoons{\\text{fast}} \\text{CH}_3\\text{I} + \\text{H}_2\\text{O} \\]
   Because this organic reaction maintains a steady concentration of $\\text{CH}_3\\text{I}$, variations in $[\\text{CH}_3\\text{OH}]$ do not affect the rate-determining organometallic step.
2. Carbon monoxide coordinates and undergoes migratory insertion in rapid elementary steps following oxidative addition.
3. Because oxidative addition of methyl iodide to $[\\text{Rh}(\\text{CO})_2\\text{I}_2]^-$ is the slowest elementary step ($k_1 \\ll k_2, k_3, k_4$), all downstream steps involving carbon monoxide are kinetically fast.
4. Therefore, the overall catalytic rate is completely independent of $[\\text{CO}]$ and $[\\text{CH}_3\\text{OH}]$ (zero-order in both).

**(b) Identification of Catalyst Resting State and Turnover-Limiting Step:**
- **Turnover-Limiting Step (TLS)**: The nucleophilic $S_N2$ oxidative addition of methyl iodide:
  \\[ [\\text{Rh}(\\text{CO})_2\\text{I}_2]^- + \\text{CH}_3\\text{I} \\xrightarrow{k_1} [(\\text{CH}_3)\\text{Rh}(\\text{CO})_2\\text{I}_3]^- \\]
- **Catalyst Resting State (CRS)**: Because oxidative addition is rate-determining, virtually all rhodium in the reactor sits waiting in the preceding square-planar rhodium(I) form:
  \\[ \\mathbf{\\text{CRS} = [\\text{cis-Rh}(\\text{CO})_2\\text{I}_2]^-} \\quad (16\\text{e, } \\text{Rh(I)}) \\]
  This species constitutes $>99\\%$ of total rhodium under steady-state operating conditions.

**(c) Production Rate Calculation:**
Given:
- Reactor volume $V = 500\\text{ L}$
- $[\\text{Rh}] = 2.0\\text{ mM} = 2.0 \\times 10^{-3}\\text{ M}$
- $[\\text{CH}_3\\text{I}] = 0.40\\text{ M}$
- $k_1 = 3.5 \\times 10^{-3}\\text{ M}^{-1}\\text{s}^{-1}$

1. Volumetric Reaction Rate:
   \\[ r = k_1 [\\text{Rh}] [\\text{CH}_3\\text{I}] = (3.5 \\times 10^{-3})(2.0 \\times 10^{-3})(0.40) \\]
   \\[ r = 2.80 \\times 10^{-6}\\text{ mol/(L}\\cdot\\text{s)} \\]
2. Total Reaction Rate:
   \\[ R_\\text{total} = r \\times V = (2.80 \\times 10^{-6}\\text{ mol/(L}\\cdot\\text{s)})(500\\text{ L}) = 1.40 \\times 10^{-3}\\text{ mol/s} \\]
3. Acetic Acid Production per Hour:
   \\[ R_\\text{hour} = (1.40 \\times 10^{-3}\\text{ mol/s}) \\times 3600\\text{ s/h} = 5.04\\text{ mol/h} \\]
   Molar mass of acetic acid $= 60.05\\text{ g/mol}$:
   \\[ \\text{Mass rate} = 5.04\\text{ mol/h} \\times 60.05\\text{ g/mol} \\approx \\mathbf{302.7\\text{ g/h}} \\approx \\mathbf{0.303\\text{ kg/h}} \\]"""
        },
        {
            "id": "prob10_2",
            "tier": "Foundational",
            "title": "Mathematical Evaluation of the Anderson-Schulz-Flory (ASF) Distribution",
            "statement": "In a cobalt Fischer-Tropsch reactor, the chain propagation probability is $\\alpha = 0.85$. (a) Calculate the mole fraction $x_n$ and weight fraction $w_n$ of methane ($n=1$), propane ($n=3$), and octane ($n=8$). (b) Calculate the carbon number $n_\\text{max}$ that corresponds to the peak of the weight distribution. (c) Calculate the maximum theoretical weight fraction $w(n_\\text{max})$ achievable at this $\\alpha$.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of Mole Fractions ($x_n$) and Weight Fractions ($w_n$):**
Formulas:
\\[ x_n = (1 - \\alpha) \\alpha^{n-1} \\]
\\[ w_n = n (1 - \\alpha)^2 \\alpha^{n-1} \\]
Given $\\alpha = 0.85$:
- $(1 - \\alpha) = 0.15$
- $(1 - \\alpha)^2 = (0.15)^2 = 0.0225$

1. **For Methane ($n = 1$)**:
   - $x_1 = (0.15)(0.85)^0 = \\mathbf{0.150}$ ($15.0\\%$ by mole)
   - $w_1 = (1)(0.0225)(0.85)^0 = \\mathbf{0.0225}$ ($2.25\\%$ by weight)

2. **For Propane ($n = 3$)**:
   - $\\alpha^{3-1} = (0.85)^2 = 0.7225$
   - $x_3 = (0.15)(0.7225) = \\mathbf{0.1084}$ ($10.84\\%$ by mole)
   - $w_3 = 3(0.0225)(0.7225) = \\mathbf{0.0488}$ ($4.88\\%$ by weight)

3. **For Octane ($n = 8$)**:
   - $\\alpha^{8-1} = (0.85)^7 \\approx 0.32057$
   - $x_8 = (0.15)(0.32057) = \\mathbf{0.0481}$ ($4.81\\%$ by mole)
   - $w_8 = 8(0.0225)(0.32057) = \\mathbf{0.0577}$ ($5.77\\%$ by weight)

**(b) Peak Carbon Number $n_\\text{max}$:**
To find the maximum of $w_n = n (1-\\alpha)^2 \\alpha^{n-1}$, treat $n$ as a continuous variable and differentiate:
\\[ \\frac{dw_n}{dn} = (1-\\alpha)^2 \\left[ \\alpha^{n-1} + n \\alpha^{n-1} \\ln(\\alpha) \\right] = 0 \\]
\\[ 1 + n \\ln(\\alpha) = 0 \\implies n_\\text{max} = -\\frac{1}{\\ln(\\alpha)} \\]
Given $\\alpha = 0.85$:
\\[ \\ln(0.85) \\approx -0.16252 \\]
\\[ n_\\text{max} = -\\frac{1}{-0.16252} \\approx \\mathbf{6.15} \\implies n_\\text{max} = \\mathbf{6} \\text{ (Hexane)} \\]

**(c) Maximum Theoretical Weight Fraction:**
For $n = 6$:
\\[ w_6 = 6 (0.0225) (0.85)^5 \\]
- $(0.85)^5 \\approx 0.4437$
\\[ w_6 = 6(0.0225)(0.4437) = 0.135 \\times 0.4437 \\approx \\mathbf{0.0599} \\approx \\mathbf{5.99\\%\\text{ by weight}} \\]
- **Conclusion**: The weight fraction peaks at carbon number 6, where hexane constitutes at most $\\approx 6.0\\%$ of the total hydrocarbons produced."""
        },
        {
            "id": "prob10_3",
            "tier": "Foundational",
            "title": "Thermodynamics of the Water-Gas Shift Reaction (WGSR)",
            "statement": "For the Water-Gas Shift Reaction $\\text{CO}(\\text{g}) + \\text{H}_2\\text{O}(\\text{g}) \\rightleftharpoons \\text{CO}_2(\\text{g}) + \\text{H}_2(\\text{g})$: (a) Given $\\Delta H_{298}^\\circ = -41.2\\text{ kJ/mol}$ and $\\Delta S_{298}^\\circ = -42.4\\text{ J/(mol}\\cdot\\text{K)}$, calculate the equilibrium constant $K_p$ at $473\\text{ K} (200^\\circ\\text{C})$ and $723\\text{ K} (450^\\circ\\text{C})$ using the van 't Hoff equation. (b) Explain why industrial plants operate the shift reaction in two distinct temperature stages.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of $K_p$ at $473\\text{ K}$ and $723\\text{ K}$:**
The Gibbs free energy change is:
\\[ \\Delta G^\\circ(T) = \\Delta H^\\circ - T\\Delta S^\\circ \\]

1. **At $T_1 = 473\\text{ K} (200^\\circ\\text{C})$ [Low-Temperature Shift]**:
   \\[ \\Delta G^\\circ(473) = -41,200 - (473)(-42.4) = -41,200 - (-20,055) = -41,200 + 20,055 = -21,145\\text{ J/mol} \\]
   \\[ K_p(473) = \\exp\\left(-\\frac{\\Delta G^\\circ}{RT}\\right) = \\exp\\left(-\\frac{-21,145}{(8.3145)(473)}\\right) = \\exp\\left(\\frac{21,145}{3932.8}\\right) = \\exp(+5.376) \\approx \\mathbf{216.2} \\]

2. **At $T_2 = 723\\text{ K} (450^\\circ\\text{C})$ [High-Temperature Shift]**:
   \\[ \\Delta G^\\circ(723) = -41,200 - (723)(-42.4) = -41,200 - (-30,655) = -41,200 + 30,655 = -10,545\\text{ J/mol} \\]
   \\[ K_p(723) = \\exp\\left(-\\frac{-10,545}{(8.3145)(723)}\\right) = \\exp\\left(\\frac{10,545}{6011.4}\\right) = \\exp(+1.754) \\approx \\mathbf{5.78} \\]

**(b) Industrial Rationale for Two-Stage Shift Operation:**
1. **The Kinetic-Thermodynamic Compromise**:
   - The reaction is exothermic ($\\Delta H^\\circ < 0$). Le Chatelier's principle dictates that high temperature suppresses equilibrium conversion ($K_p$ drops from $216$ down to $5.8$).
   - However, chemical reaction rates follow Arrhenius kinetics, dropping exponentially at lower temperatures.
2. **First Stage: High-Temperature Shift (HTS, $350-450^\\circ\\text{C}$)**:
   - Operates over robust $\\text{Fe}_3\\text{O}_4-\\text{Cr}_2\\text{O}_3$ catalyst.
   - High temperature provides rapid chemical reaction rates, converting the bulk of carbon monoxide from $\\approx 12\\%$ down to $\\approx 3\\%$.
3. **Second Stage: Low-Temperature Shift (LTS, $200-250^\\circ\\text{C}$)**:
   - Operates over highly active $\\text{Cu/ZnO/Al}_2\\text{O}_3$ catalyst.
   - Takes advantage of the high equilibrium constant ($K_p = 216$) to drive remaining CO down to $<0.2\\%$, maximizing pure $\\text{H}_2$ yield for ammonia synthesis and fuel cells."""
        },
        {
            "id": "prob10_4",
            "tier": "Intermediate",
            "title": "Symmetry and Tacticity Control in Propylene Polymerization Metallocenes",
            "statement": "Ansa-metallocene catalysts of group 4 metals enforce tacticity through point group symmetry. (a) For $C_2$-symmetric *rac*-[$\\text{Me}_2\\text{Si}(\\text{Indenyl})_2\\text{ZrCl}_2$], show why the two coordination sites are homotopic and derive why it yields isotactic polypropylene. (b) For $C_s$-symmetric $[\\text{Me}_2\\text{C}(\\text{Flu})(Cp)\\text{ZrCl}_2]$, show why the two coordination sites are enantiotopic and derive why it yields syndiotactic polypropylene. (c) Explain the origin of stereo-errors (isolated vs. block errors).",
            "solution": """**Line-by-Line Solution:**

**(a) $C_2$-Symmetric Metallocenes and Isotactic Control:**
1. A chiral *ansa*-zirconocene with $C_2$ symmetry possesses a twofold rotational axis passing through zirconium and bisecting the two coordination sites in the equatorial wedge.
2. Under a $C_2$ rotation, coordination site A rotates directly into coordination site B:
   \\[ C_2 \\cdot \\text{Site A} = \\text{Site B} \\]
   Therefore, the two coordination sites are **strictly homotopic** (chemically and chiral-topologically identical).
3. The growing polymer chain occupies one site and is oriented into a specific chiral conformation by the bulky indenyl benzo-rings.
4. When propylene coordinates into the open site, steric repulsion between the propylene methyl group and the chiral ligand framework forces propylene to present exclusively its **re-face** (or exclusively *si*-face).
5. Migratory insertion shifts the chain to the second site. Because the second site is homotopic to the first, propylene coordination again occurs with the exact same facial stereochemistry!
6. This **enantiomorphic site control** enforces identical stereocenters at every monomer addition, delivering **isotactic polypropylene (i-PP)**.

**(b) $C_s$-Symmetric Metallocenes and Syndiotactic Control:**
1. In $[\\text{Me}_2\\text{C}(\\text{Flu})(Cp)\\text{ZrCl}_2]$, the complex possesses a single mirror plane $\\sigma$ bisecting the cyclopentadienyl and fluorenyl ligands ($C_s$ symmetry).
2. Reflection through $\\sigma$ exchanges site A with site B:
   \\[ \\sigma \\cdot \\text{Site A} = \\text{Site B} \\]
   Therefore, the two coordination sites are **enantiotopic** (mirror images of each other).
3. Site A has a chiral environment that favors coordination of propylene through its *re*-face.
4. Migratory insertion shifts the growing chain to Site B. Because Site B is the mirror image of Site A, it favors coordination of propylene through the opposite **si-face**!
5. As the growing polymer chain alternates between Site A and Site B with each insertion step:
   \\[ \\text{Site A } (re) \\longrightarrow \\text{Site B } (si) \\longrightarrow \\text{Site A } (re) \\longrightarrow \\text{Site B } (si) \\]
   the facial addition alternates regularly, yielding **syndiotactic polypropylene (s-PP)**.

**(c) Stereo-Error Signatures:**
1. **Enantiomorphic Site Control ($C_2$-Catalyst)**:
   - If an occasional mis-insertion occurs (e.g., *si* instead of *re*), the chiral ligand site immediately forces the next monomer back to the correct *re*-face.
   - Produces an **isolated stereo-error**: $\\dots R R R R S R R R R \\dots$ (pentad signature: $mmmm$ with isolated $mrrm$).
2. **Chain-End Control (Achiral $C_{2v}$-Catalyst)**:
   - Stereochemistry is directed by the asymmetric center of the last inserted monomer unit.
   - If a mistake occurs, the newly inverted chain end now directs future insertions according to the new stereocenter, producing a **propagating block error**: $\\dots R R R R S S S S \\dots$."""
        },
        {
            "id": "prob10_5",
            "tier": "Intermediate",
            "title": "Mechanistic Kinetics of Ruthenium Promotion in the BP Cativa Process",
            "statement": "In the BP Cativa process, the resting state is $[(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^-$. In the absence of promoter, the reaction rate is inhibited by iodide ions: $\\text{Rate} \\propto [\\text{I}^-]^{-1}$. (a) Derive the steady-state rate law demonstrating why iodide dissociation is required for migratory CO insertion. (b) Formulate the equilibrium expression for ruthenium promoter halide abstraction: $[(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^- + [\\text{Ru}(\\text{CO})_3\\text{I}_2] \\xrightleftharpoons{K_p} [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2] + [\\text{Ru}(\\text{CO})_3\\text{I}_3]^-$. (c) Explain how this eliminates iodide inhibition and accelerates the net catalytic cycle.",
            "solution": """**Line-by-Line Solution:**

**(a) Rate Law for Unpromoted Iridium Carbonylation:**
1. The resting state is the 18-electron hexacoordinate complex $[(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^-$.
2. Migratory insertion of the methyl group onto CO requires a vacant coordination site cis to both ligands. Because the complex is coordination saturated (18e), an open site must be generated by ligand dissociation.
3. The carbonyl ligands are held tightly by strong $\\pi$-backbonding; therefore, the leaving group is an iodide anion:
   \\[ [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^- \\xrightleftharpoons[k_{-1}]{k_1} [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2] + \\text{I}^- \\quad (16\\text{e intermediate}) \\]
4. The 16e intermediate undergoes rapid migratory insertion:
   \\[ [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2] \\xrightarrow{k_2} [(\\text{CH}_3\\text{CO})\\text{Ir}(\\text{CO})\\text{I}_2] \\]
5. Applying the steady-state approximation:
   \\[ [\\text{Ir}_{16}] = \\frac{k_1 [\\text{Ir}_{18}]}{k_{-1}[\\text{I}^-] + k_2} \\]
   Because iodide recapture is fast ($k_{-1}[\\text{I}^-] \\gg k_2$):
   \\[ [\\text{Ir}_{16}] \\approx \\frac{k_1 [\\text{Ir}_{18}]}{k_{-1}[\\text{I}^-]} = K_1 \\frac{[\\text{Ir}_{18}]}{[\\text{I}^-]} \\]
   The catalytic rate is:
   \\[ \\text{Rate} = k_2 [\\text{Ir}_{16}] = \\frac{k_2 K_1 [\\text{Ir}]_{0}}{[\\text{I}^-]} \\]
   The reaction rate is strictly inversely proportional to $[\\text{I}^-]$ (inhibited by free iodide).

**(b) Equilibrium Expression for Ruthenium Halide Abstraction:**
Adding the ruthenium promoter $[\\text{Ru}(\\text{CO})_3\\text{I}_2]$ establishes the reversible halogen transfer:
\\[ [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^- + [\\text{Ru}(\\text{CO})_3\\text{I}_2] \\xrightleftharpoons{K_p} [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2] + [\\text{Ru}(\\text{CO})_3\\text{I}_3]^- \\]
The equilibrium constant is:
\\[ K_p = \\frac{[(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2] [\\text{Ru}(\\text{CO})_3\\text{I}_3]^-}{[(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_3]^- [\\text{Ru}(\\text{CO})_3\\text{I}_2]} \\]

**(c) Elimination of Iodide Inhibition and Catalytic Acceleration:**
1. The ruthenium complex acts as an **iodide sponge**: instead of relying on thermal dissociation of a bare $\\text{I}^-$ ion into solution (which has a large solvation and charge-separation free energy penalty $\\Delta G^\\circ > 70\\text{ kJ/mol}$), the iodide is transferred directly to the vacant coordination site of the neutral ruthenium complex.
2. The concentration of the reactive neutral 5-coordinate intermediate is:
   \\[ [(\\text{CH}_3)\\text{Ir}(\\text{CO})_2\\text{I}_2] = K_p [\\text{Ir}_{18}] \\frac{[\\text{Ru}_\\text{neutral}]}{[\\text{Ru}_\\text{anionic}]} \\]
3. This completely bypasses the dependence on free solvated $[\\text{I}^-]$, raising the steady-state concentration of the reactive 16e iridium intermediate by several orders of magnitude.
4. Consequently, the rate-limiting migratory insertion proceeds smoothly at low water concentrations, providing the Cativa process with higher rates and lower side-reaction losses."""
        },
        {
            "id": "prob10_6",
            "tier": "Intermediate",
            "title": "Deactivation Mechanisms of Metallocene Olefin Polymerization Catalysts",
            "statement": "The active species in metallocene polymerization $[Cp_2\\text{Zr-R}]^+$ undergoes thermal deactivation via unimolecular and bimolecular pathways. (a) Formulate the intramolecular $\\text{C-H}$ activation pathway (dormant cyclopentadienyl-alkylidene complex formation). (b) Formulate the bimolecular dormant dimer formation $[(Cp_2\\text{Zr-R})_2(\\mu-\\text{Cl})]^+$. (c) Explain why adding trimethylaluminum (TMA) scavenges impurities but causes reversible chain transfer.",
            "solution": """**Line-by-Line Solution:**

**(a) Intramolecular $\\text{C}-\\text{H}$ Activation (Dormant Fulvene/Alkylidene Formation):**
1. The 14-electron cationic catalyst $[Cp_2\\text{Zr-CH}_2\\text{CH}_2 R]^+$ is highly electrophilic and coordination unsaturated.
2. In the absence of monomer, the zirconium center activates an adjacent $C-H$ bond:
   - Either through $\\beta$-hydride elimination to release an alkene and form $[Cp_2\\text{Zr-H}]^+$.
   - Or through intramolecular activation of a $C-H$ bond of one of the cyclopentadienyl rings:
     \\[ [(\\eta^5-\\text{C}_5\\text{H}_5)_2\\text{Zr-R}]^+ \\longrightarrow [(\\eta^5-\\text{C}_5\\text{H}_5)(\\eta^5:\\eta^1-\\text{C}_5\\text{H}_4)\\text{Zr}]^+ + R-\\text{H} \\uparrow \\]
   This generates a bridging fulvene complex that is catalytically dormant and resistant to olefin insertion.

**(b) Bimolecular Dormant Dimer Formation:**
1. Residual chloride or alkyl species can bridge two metallocene centers:
   \\[ [Cp_2\\text{Zr-R}]^+ + Cp_2\\text{ZrCl}_2 \\rightleftharpoons [Cp_2\\text{Zr}(R)-(\\mu-\\text{Cl})-\\text{Zr}(R)Cp_2]^+ \\]
2. The resulting dinuclear species coordinates both zirconium atoms in a saturated, sterically shielded coordination envelope, blocking incoming ethylene monomer from accessing either metal center.

**(c) Role of Trimethylaluminum (TMA): Scavenging vs. Chain Transfer:**
1. **Scavenger Role**:
   Trace impurities in industrial reactor feeds (water, oxygen, carbon dioxide) act as catalyst poisons. TMA reacts instantly with water to form methane and active aluminoxanes:
   \\[ \\text{AlMe}_3 + \\text{H}_2\\text{O} \\longrightarrow \\text{Me}_2\\text{AlOH} + \\text{CH}_4 \\uparrow \\]
   protecting the zirconium catalyst from hydrolytic deactivation.
2. **Reversible Chain Transfer to Aluminum**:
   TMA undergoes transmetallation with the active growing zirconium-polymer chain:
   \\[ [Cp_2\\text{Zr-Polymer}]^+ + \\text{AlMe}_3 \\rightleftharpoons [Cp_2\\text{Zr-Me}]^+ + \\text{Me}_2\\text{Al-Polymer} \\]
   - The growing polymer chain is transferred to aluminum, terminating chain growth on zirconium and capping the polymer with an aluminum end-group.
   - The methyl-zirconium cation $[Cp_2\\text{Zr-Me}]^+$ re-initiates a new polymer chain.
   - This chain transfer to aluminum lowers the number-average molecular weight ($M_n$) of the produced polymer and broadens the molecular weight distribution."""
        },
        {
            "id": "prob10_7",
            "tier": "Advanced",
            "title": "Comprehensive Kinetic Model of Fischer-Tropsch Chain Growth and Desorption",
            "statement": "Formulate a rigorous kinetic model for the surface reactions in cobalt Fischer-Tropsch synthesis. Let $\\theta_*$ be the fraction of vacant surface sites, $\\theta_{\\text{CH}_2}$ be surface methylene coverage, and $\\theta_n$ be the coverage of surface alkyl chains with carbon number $n$. Chain propagation occurs with rate constant $k_p$: $M-\\text{R}_n + M-\\text{CH}_2 \\xrightarrow{k_p} M-\\text{R}_{n+1} + M$. Chain termination occurs via hydrogenation ($k_{t,H}$) to form $n$-alkane ($P_n$) or $\\beta$-elimination ($k_{t,\\beta}$) to form $\\alpha$-olefin ($O_n$). (a) Formulate the steady-state equations for $\\theta_n$. (b) Prove that the chain propagation probability $\\alpha = \\frac{k_p \\theta_{\\text{CH}_2}}{k_p \\theta_{\\text{CH}_2} + k_{t,H} \\theta_H + k_{t,\\beta}}$ is independent of chain length $n$ (Flory's equal reactivity principle). (c) Derive the exact Anderson-Schulz-Flory mass distribution equation $w_n = n (1-\\alpha)^2 \\alpha^{n-1}$.",
            "solution": """**Line-by-Line Solution:**

**(a) Steady-State Equations for Surface Alkyl Coverage $\\theta_n$:**
For an alkyl chain of length $n$ ($n \\ge 2$):
1. **Rate of Formation**:
   Formed exclusively by propagation from an alkyl chain of length $n-1$:
   \\[ R_f(n) = k_p \\theta_{n-1} \\theta_{\\text{CH}_2} \\]
2. **Rate of Consumption**:
   Consumed by further propagation to chain length $n+1$ and by termination:
   \\[ R_c(n) = k_p \\theta_n \\theta_{\\text{CH}_2} + k_{t,H} \\theta_n \\theta_H + k_{t,\\beta} \\theta_n \\theta_* \\]
3. Under the steady-state approximation ($R_f(n) = R_c(n)$):
   \\[ k_p \\theta_{n-1} \\theta_{\\text{CH}_2} = \\theta_n \\left( k_p \\theta_{\\text{CH}_2} + k_{t,H} \\theta_H + k_{t,\\beta} \\theta_* \\right) \\]

**(b) Proof of Chain Length Independence of $\\alpha$:**
1. Solving the steady-state equation for the ratio $\\theta_n / \\theta_{n-1}$:
   \\[ \\frac{\\theta_n}{\\theta_{n-1}} = \\frac{k_p \\theta_{\\text{CH}_2}}{k_p \\theta_{\\text{CH}_2} + k_{t,H} \\theta_H + k_{t,\\beta} \\theta_*} \\equiv \\alpha \\]
2. According to **Flory's Principle of Equal Reactivity**, the chemical reactivity of the terminal carbon-metal bond is independent of the length of the attached hydrocarbon tail ($n \\ge 3$).
3. Because the elementary rate constants $k_p, k_{t,H}$, and $k_{t,\\beta}$ and the surface coverages $\\theta_{\\text{CH}_2}, \\theta_H, \\theta_*$ are identical for all chains, the ratio $\\theta_n / \\theta_{n-1}$ is a **constant parameter $\\alpha$** independent of carbon number $n$:
   \\[ \\theta_n = \\alpha \\theta_{n-1} = \\alpha^2 \\theta_{n-2} = \\dots = \\alpha^{n-1} \\theta_1 \\]

**(c) Derivation of the ASF Weight Fraction Distribution ($w_n$):**
1. The total rate of production of hydrocarbons of length $n$ (alkane $+$ alkene) is:
   \\[ r_n = (k_{t,H} \\theta_H + k_{t,\\beta} \\theta_*) \\theta_n \\]
2. Since $k_{t,H} \\theta_H + k_{t,\\beta} \\theta_* = k_p \\theta_{\\text{CH}_2} \\left(\\frac{1 - \\alpha}{\\alpha}\\right)$:
   \\[ r_n = k_p \\theta_{\\text{CH}_2} \\left(\\frac{1 - \\alpha}{\\alpha}\\right) \\alpha^{n-1} \\theta_1 = k_p \\theta_{\\text{CH}_2} \\theta_1 (1 - \\alpha) \\alpha^{n-2} \\]
3. The mole fraction $x_n$ is the production rate of chain length $n$ divided by total production:
   \\[ x_n = \\frac{r_n}{\\sum_{j=1}^\\infty r_j} = \\frac{(1 - \\alpha) \\alpha^{n-1}}{\\sum_{j=1}^\\infty (1 - \\alpha) \\alpha^{j-1}} \\]
   Since $\\sum_{j=1}^\\infty \\alpha^{j-1} = \\frac{1}{1 - \\alpha}$:
   \\[ x_n = (1 - \\alpha) \\alpha^{n-1} \\]
4. The weight of a molecule of chain length $n$ is proportional to its carbon number: $M_n = n M_0$ (where $M_0 \\approx 14\\text{ g/mol}$ is the mass of a $\\text{CH}_2$ unit).
5. The weight fraction $w_n$ is:
   \\[ w_n = \\frac{n x_n}{\\sum_{j=1}^\\infty j x_j} \\]
   Evaluate the sum in the denominator:
   \\[ \\sum_{j=1}^\\infty j x_j = (1 - \\alpha) \\sum_{j=1}^\\infty j \\alpha^{j-1} = (1 - \\alpha) \\frac{d}{d\\alpha} \\left( \\sum_{j=0}^\\infty \\alpha^j \\right) = (1 - \\alpha) \\frac{d}{d\\alpha} \\left(\\frac{1}{1 - \\alpha}\\right) = (1 - \\alpha) \\frac{1}{(1 - \\alpha)^2} = \\frac{1}{1 - \\alpha} \\]
6. Substitute into $w_n$:
   \\[ w_n = \\frac{n (1 - \\alpha) \\alpha^{n-1}}{\\frac{1}{1 - \\alpha}} = \\mathbf{n (1 - \\alpha)^2 \\alpha^{n-1}} \\]
- This completes the exact mathematical derivation of the Anderson-Schulz-Flory distribution."""
        },
        {
            "id": "prob10_8",
            "tier": "Advanced",
            "title": "Quantum Mechanical Modeling of the Agostic Transition State in Ziegler-Natta Insertion",
            "statement": "In the Cossee-Arlman migratory insertion of ethylene into $[Cp_2\\text{Zr-CH}_3]^+$, the transition state features an $\\alpha$-agostic interaction: $[Cp_2\\text{Zr} \\cdots \\text{H}_\\alpha-\\text{CH}_2 \\cdots \\text{C}_2\\text{H}_4]^\\ddagger$. (a) Construct the orbital interaction diagram illustrating the role of the $\\alpha$-agostic bond. (b) Explain why an $\\alpha$-agostic interaction lowers the activation energy by $\\approx 15-20\\text{ kJ/mol}$, whereas a $\\beta$-agostic interaction inhibits insertion. (c) Derive the kinetic isotope effect ($k_H / k_D$) observed when using deuterated methyl $[Cp_2\\text{Zr-CD}_3]^+$.",
            "solution": """**Line-by-Line Solution:**

**(a) Orbital Interaction of the $\\alpha$-Agostic Transition State:**
1. In the cationic 14-electron $[Cp_2\\text{Zr-CH}_3]^+$ fragment, zirconium has two empty frontier orbitals in the equatorial wedge ($1a_1$ and $2a_1$).
2. During ethylene coordination into $1a_1$, the migrating methyl group begins transferring onto the ethylene carbon.
3. In the four-centered transition state, the $\\alpha$-carbon tilts toward the metal center, allowing one of its three $\\text{C}_\\alpha-\\text{H}_\\alpha$ bonding orbitals to donate into the second vacant metal orbital ($2a_1$):
   \\[ \\sigma(\\text{C}_\\alpha-\\text{H}_\\alpha) \\longrightarrow 2a_1(\\text{Zr}) \\]
4. This forms a **three-center two-electron ($3c-2e$) $\\alpha$-agostic bond** in the transition state.

**(b) Why $\\alpha$-Agostic Accelerates vs. $\\beta$-Agostic Inhibits Insertion:**
1. **Accelerating Role of $\\alpha$-Agostic Interaction**:
   - As the methyl carbon transfers to ethylene, it undergoes rehybridization from tetrahedral $sp^3$ toward a planar $sp^2$-like geometry at the transition state.
   - The $\\alpha$-agostic interaction assists this planarization by stabilizing the developing electron deficiency at the migrating carbon.
   - It donates 2 electrons into the empty zirconium $2a_1$ orbital, stabilizing the transition state by **$15-20\\text{ kJ/mol}$** without requiring any ligand dissociation.
2. **Inhibiting Role of $\\beta$-Agostic Interaction**:
   - In alkyl chains longer than methyl (e.g., ethyl, propyl), a $\\beta$-agostic interaction can form in the **ground state**: $[Cp_2\\text{Zr}(\\eta^2-\\text{H}_\\beta-\\text{CH}_2\\text{CH}_2)]^+$.
   - A ground-state $\\beta$-agostic bond occupies the vacant coordination site required by incoming ethylene, stabilizing the reactant ground state and requiring an energy penalty of $40-50\\text{ kJ/mol}$ to break the agostic bond before ethylene can coordinate.
   - Therefore, ground-state $\\beta$-agostic interactions raise the overall activation barrier for polymerization.

**(c) Kinetic Isotope Effect ($k_H / k_D$):**
1. Because the $\\alpha-\\text{C}-\\text{H}$ bond participates directly in the transition state via agostic bonding, its vibrational frequency is significantly perturbed.
2. In the ground state, $\\nu(\\text{C}-\\text{H}) = 2950\\text{ cm}^{-1}$.
3. In the $\\alpha$-agostic transition state, $\\nu^\\ddagger(\\text{C}-\\text{H})$ drops to $\\approx 2550\\text{ cm}^{-1}$ ($\\Delta \\nu = -400\\text{ cm}^{-1}$).
4. The secondary kinetic isotope effect is given by:
   \\[ \\frac{k_H}{k_D} = \\exp\\left( \\frac{hc (\\Delta \\tilde{\\nu}_H - \\Delta \\tilde{\\nu}_D)}{2 RT} \\right) \\]
   Since $\\Delta \\tilde{\\nu}_D \\approx \\frac{\\Delta \\tilde{\\nu}_H}{\\sqrt{2}} = \\frac{-400}{1.414} = -283\\text{ cm}^{-1}$:
   \\[ \\Delta \\tilde{\\nu}_H - \\Delta \\tilde{\\nu}_D = -400 - (-283) = -117\\text{ cm}^{-1} \\]
5. Compute the exponent at $298\\text{ K}$:
   \\[ \\Delta \\text{ZPE} = \\frac{1}{2} (6.626 \\times 10^{-34})(3.0 \\times 10^{10})(-117)(6.022 \\times 10^{23}) \\approx -700\\text{ J/mol} \\]
   \\[ \\frac{k_H}{k_D} = \\exp\\left( -\\frac{-700}{(8.314)(298)} \\right) = \\exp(+0.282) \\approx \\mathbf{1.33} \\]
- **Conclusion**: A normal secondary kinetic isotope effect of **$k_H/k_D \\approx 1.25 - 1.35$** is observed, serving as experimental proof of the $\\alpha$-agostic interaction in the Cossee-Arlman transition state."""
        },
        {
            "id": "prob10_9",
            "tier": "Advanced",
            "title": "Thermodynamics of Green Carbonylation and Direct Carbon Dioxide Hydrogenation",
            "statement": "The direct hydrogenation of carbon dioxide to formic acid/formate $\\text{CO}_2 + \\text{H}_2 \\rightleftharpoons \\text{HCOOH}$ is an emerging green organometallic process. (a) In the gas phase, standard enthalpy $\\Delta H_{298}^\\circ = -31.2\\text{ kJ/mol}$ and standard entropy $\\Delta S_{298}^\\circ = -115.5\\text{ J/(mol}\\cdot\\text{K)}$. Calculate $\\Delta G^\\circ$ at $298\\text{ K}$ and explain why the gas-phase reaction is thermodynamically unfavorable. (b) In aqueous solution with an organic amine base ($NEt_3$), the reaction forms triethylammonium formate $[\\text{Et}_3\\text{NH}]^+ [\\text{HCOO}]^-$, with $\\Delta G_\\text{aq}^\\circ = -35.6\\text{ kJ/mol}$. Construct the thermodynamic cycle showing how base and solvation drive this reaction. (c) Propose a ruthenium-phosphine catalytic cycle for this transformation.",
            "solution": """**Line-by-Line Solution:**

**(a) Gas-Phase Thermodynamics at $298\\text{ K}$:**
The standard Gibbs free energy change in the gas phase is:
\\[ \\Delta G^\\circ(298) = \\Delta H^\\circ - T\\Delta S^\\circ \\]
Given:
- $\\Delta H^\\circ = -31.2\\text{ kJ/mol} = -31,200\\text{ J/mol}$ (exothermic)
- $\\Delta S^\\circ = -115.5\\text{ J/(mol}\\cdot\\text{K)}$ (entropically unfavorable due to $2 \\to 1$ gas mole reduction)
\\[ \\Delta G^\\circ(298) = -31,200 - (298.15)(-115.5) = -31,200 - (-34,436) = -31,200 + 34,436 = \\mathbf{+3,236\\text{ J/mol}} = \\mathbf{+3.24\\text{ kJ/mol}} \\]
The equilibrium constant is:
\\[ K_p = \\exp\\left(-\\frac{3,236}{(8.3145)(298.15)}\\right) = \\exp(-1.305) \\approx \\mathbf{0.27} \\]
- **Conclusion**: In the gas phase, $\\Delta G^\\circ > 0$. The reaction is thermodynamically uphill and unfavorable because the entropic penalty of combining two gas molecules into one liquid/condensed molecule outweighs the modest exothermic enthalpy of hydrogenation.

**(b) Solution-Phase Thermodynamic Driving Cycle:**
In aqueous solution in the presence of triethylamine $\\text{NEt}_3$:
1. **Solvation of Reactants and Product**:
   Hydration of gaseous formic acid releases massive solvation free energy:
   \\[ \\text{HCOOH}(\\text{g}) \\longrightarrow \\text{HCOOH}(\\text{aq}) \\quad (\\Delta G_\\text{solv}^\circ \\approx -26\\text{ kJ/mol}) \\]
2. **Acid-Base Neutralization**:
   Formic acid is a moderately strong carboxylic acid ($\\text{p}K_a = 3.75$), while triethylamine is a basic amine ($\\text{p}K_a(\\text{Et}_3\\text{NH}^+) = 10.75$).
   The proton-transfer reaction:
   \\[ \\text{HCOOH}(\\text{aq}) + \\text{NEt}_3(\\text{aq}) \\rightleftharpoons [\\text{Et}_3\\text{NH}]^+ + [\\text{HCOO}]^- \\]
   has an equilibrium constant:
   \\[ K_\\text{acid-base} = 10^{\\text{p}K_a(\\text{Et}_3\\text{NH}^+) - \\text{p}K_a(\\text{HCOOH})} = 10^{10.75 - 3.75} = 10^7 \\]
   Free energy release of neutralization:
   \\[ \\Delta G_\\text{neutralization}^\circ = -2.303 RT \\log(10^7) = -5.708 \\times 7 = -39.95\\text{ kJ/mol} \\]
3. Summing the thermodynamic steps:
   \\[ \\Delta G_\\text{net}^\circ = \\Delta G_\\text{gas}^\circ + \\Delta G_\\text{solv}^\circ + \\Delta G_\\text{neutralization}^\circ \\approx +3.24 - 26 - 40 \\approx \\mathbf{-62.7\\text{ kJ/mol}} \\]
- Base capture and aqueous solvation provide a combined thermodynamic driving force of over $60\\text{ kJ/mol}$, pulling the unfavorable gas-phase equilibrium into a completely downhill, spontaneous reaction.

**(c) Catalytic Cycle for $\\text{CO}_2$ Hydrogenation (Ruthenium-Phosphine):**
1. **Step 1: Dihydrogen Cleavage**:
   Active catalyst $[L_n\\text{Ru}(\\text{H})_2]$ or heterolytic cleavage of $\\text{H}_2$ by base and $[L_n\\text{RuCl}]$:
   \\[ [L_n\\text{Ru}] + \\text{H}_2 + \\text{NEt}_3 \\longrightarrow [L_n\\text{Ru}-\\text{H}]^- + [\\text{Et}_3\\text{NH}]^+ \\]
2. **Step 2: $\\text{CO}_2$ Insertion into Ru-H Bond**:
   Carbon dioxide coordinates into the ruthenium coordination sphere and inserts into the nucleophilic $Ru-H$ bond via 1,2-migratory insertion:
   \\[ [L_n\\text{Ru}-\\text{H}]^- + \\text{O}=\\text{C}=\\text{O} \\longrightarrow [L_n\\text{Ru}-\\text{O}-\\text{C}(=\\text{O})\\text{H}]^- \\quad (\\text{Formatoruthenium intermediate}) \\]
3. **Step 3: Formate Release and Catalyst Regeneration**:
   Reaction with $\\text{H}_2$ (or base displacement) releases formate anion $[\\text{HCOO}]^-$ and regenerates $[L_n\\text{Ru}-\\text{H}]$, closing the catalytic cycle with turnover frequencies exceeding $10^5\\text{ h}^{-1}$."""
        }
    ]

    return {
        "unit_number": 10,
        "title": "Industrial Catalytic Processes: Polymerization, Carbonylation & Syngas Chemistry",
        "description": "Ziegler-Natta heterogeneous polymerization, the Cossee-Arlman insertion mechanism, homogeneous metallocene Kaminsky catalysts and MAO activation, stereocontrol in polypropylene (isotactic, syndiotactic, atactic), the Monsanto acetic acid process, the BP Cativa process with ruthenium promotion, the Water-Gas Shift Reaction (WGSR), Fischer-Tropsch synthesis, the Anderson-Schulz-Flory (ASF) distribution, and green CO2 hydrogenation.",
        "sections": sections,
        "problems": problems
    }
