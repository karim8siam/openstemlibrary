"""
create_organo_u9.py
Unit 9: Homogeneous Catalysis: Hydrogenation, Hydroformylation & Olefin Metathesis
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_9():
    sections = [
        {
            "id": "sec9_1",
            "title": "§9.1 Principles of Homogeneous Catalysis: Cycles, TON, TOF & Catalyst Deactivation",
            "content": """A **homogeneous catalyst** operates in the same phase (typically liquid solution) as the reactants, offering atomic dispersion, molecularly well-defined active sites, tunable coordination spheres, and mild operating temperatures and pressures.

### Fundamental Catalytic Metrics:
1. **Turnover Number (TON)**:
   The total number of moles of substrate converted into product per mole of catalyst before the catalyst completely loses its activity:
   \\[ \\text{TON} = \\frac{n_\\text{product}}{n_\\text{catalyst}} \\]
2. **Turnover Frequency (TOF)**:
   The turnover number achieved per unit time, reflecting the intrinsic catalytic rate:
   \\[ \\text{TOF} = \\frac{\\text{TON}}{t} = \\frac{1}{n_\\text{catalyst}} \\frac{dn_\\text{product}}{dt} \\quad (\\text{units: h}^{-1} \\text{ or s}^{-1}) \\]
3. **Catalytic Cycle Dynamics**:
   - **Catalyst Resting State (CRS)**: The thermodynamic ground state intermediate that accumulates in the largest concentration in solution (detectable spectroscopically).
   - **Turnover-Limiting Step (TLS)**: The elementary step possessing the highest transition state energy relative to the resting state (governs the net reaction rate).
   - **Catalyst Deactivation**: Pathways that permanently siphon active metal species out of the catalytic loop, including bimolecular cluster dimerization, ligand degradation, or metal precipitation."""
        },
        {
            "id": "sec9_2",
            "title": "§9.2 Homogeneous Hydrogenation by Wilkinson's Catalyst $\\text{RhCl}(\\text{PPh}_3)_3$",
            "content": """Discovered in 1965 by Sir Geoffrey Wilkinson, chlorotris(triphenylphosphine)rhodium(I) $\\text{RhCl}(\\text{PPh}_3)_3$ is the prototypical homogeneous hydrogenation catalyst for unhindered alkenes and alkynes.

### The Catalytic Cycle (The Dihydride Pathway):
1. **Initiation (Phosphine Dissociation)**:
   In solution, the 16-electron square planar precursor undergoes reversible dissociation of one bulky triphenylphosphine ligand ($\\theta = 145^\\circ$):
   \\[ \\text{RhCl}(\\text{PPh}_3)_3 \\xrightleftharpoons[k_{-1}]{k_1} [\\text{RhCl}(\\text{PPh}_3)_2] + \\text{PPh}_3 \\quad (14\\text{e intermediate}) \\]
2. **Oxidative Addition of $\\text{H}_2$**:
   Rapid, concerted oxidative addition of molecular dihydrogen yields a 16-electron cis-dihydride:
   \\[ [\\text{RhCl}(\\text{PPh}_3)_2] + \\text{H}_2 \\xrightarrow{k_2} [\\text{RhCl}(\\text{H})_2(\\text{PPh}_3)_2] \\quad (16\\text{e, } \\text{Rh(III)}) \\]
3. **Alkene Coordination**:
   The alkene coordinates to the open site, generating an 18-electron dihydride-olefin complex:
   \\[ [\\text{RhCl}(\\text{H})_2(\\text{PPh}_3)_2] + \\text{alkene} \\xrightleftharpoons[k_{-3}]{k_3} [\\text{RhCl}(\\text{H})_2(\\text{PPh}_3)_2(\\eta^2-\\text{alkene})] \\quad (18\\text{e}) \\]
4. **Migratory Insertion (Rate-Determining Step)**:
   Intramolecular 1,2-migratory insertion of the alkene into a mutually *cis* rhodium-hydride bond generates a 16-electron alkyl-hydride intermediate:
   \\[ [\\text{RhCl}(\\text{H})_2(\\text{PPh}_3)_2(\\eta^2-\\text{alkene})] \\xrightarrow{k_4} [\\text{RhCl}(\\text{H})(R)(\\text{PPh}_3)_2] \\quad (16\\text{e}) \\]
5. **Reductive Elimination (Product Release)**:
   Concerted reductive elimination of alkane regenerates the active 14-electron $[\\text{RhCl}(\\text{PPh}_3)_2]$ catalyst:
   \\[ [\\text{RhCl}(\\text{H})(R)(\\text{PPh}_3)_2] \\xrightarrow{k_5} [\\text{RhCl}(\\text{PPh}_3)_2] + R-\\text{H} \\uparrow \\]

### Substrate Selectivity:
Because the transition states are sterically crowded, hydrogenation rates follow:
\\[ \\text{Terminal alkenes} > \\text{Disubstituted alkenes} \\gg \\text{Trisubstituted alkenes} > \\text{Tetrasubstituted (inert)} \\]"""
        },
        {
            "id": "sec9_3",
            "title": "§9.3 Asymmetric Homogeneous Hydrogenation: Knowles, Noyori & Chiral Diphosphines",
            "content": """Asymmetric hydrogenation revolutionized pharmaceutical synthesis, converting prochiral alkenes into single enantiomers with $>99\\%$ enantiomeric excess (Nobel Prize in Chemistry, 2001 to William S. Knowles and Ryoji Noyori).

### Milestone Catalytic Systems:
1. **Knowles' DIPAMP Catalyst**:
   Utilized chiral-at-phosphorus bidentate ligands for the industrial synthesis of **L-DOPA** (treatment for Parkinson's disease):
   \\[ \\text{Enamide Precursor} + \\text{H}_2 \\xrightarrow{[\\text{Rh}(\\text{DIPAMP})]^+ \\text{BF}_4^-} \\text{L-DOPA Precursor} \\quad (>95\\%\\ ee) \\]
2. **Noyori's BINAP-Ruthenium Catalysts**:
   Utilized axially chiral, atropisomeric $2,2'$-bis(diphenylphosphino)-$1,1'$-binaphthyl (**BINAP**):
   - $[\\text{Ru}(\\text{BINAP})(\\text{OAc})_2]$ hydrogenates $\\alpha,\\beta$-unsaturated carboxylic acids (e.g., $(S)$-naproxen at $>97\\%\\ ee$).
   - Noyori's bifunctional ruthenium-diamine catalysts $[\\text{RuCl}_2(\\text{BINAP})(\\text{DAIPEN})]$ hydrogenate simple ketones via a non-classical metal-ligand bifunctional outer-sphere mechanism without substrate coordination to the metal!

### The Halpern 'Minor-Isomer' Mechanism:
Jack Halpern demonstrated by low-temperature NMR that the catalyst binds a prochiral enamide to form two diastereomeric complexes in a rapid pre-equilibrium:
\\[ [\\text{Rh}(\\text{chiral})]^+\\! + \\text{alkene} \\xrightleftharpoons{K_\\text{maj}} [\\text{Complex}_\\text{major}] \\quad (95\\%) \\]
\\[ [\\text{Rh}(\\text{chiral})]^+\\! + \\text{alkene} \\xrightleftharpoons{K_\\text{min}} [\\text{Complex}_\\text{minor}] \\quad (5\\%) \\]
Counter-intuitively, oxidative addition of dihydrogen into the **minor diastereomer** is $10^3$ to $10^4$ times faster than into the major diastereomer:
\\[ k_{\\text{H}_2,\\text{minor}} \\gg k_{\\text{H}_2,\\text{major}} \\]
Therefore, the **minor, less stable diastereomer delivers $>99\\%$ of the final enantiomeric product**!"""
        },
        {
            "id": "sec9_4",
            "title": "§9.4 Hydroformylation (The Oxo Process): Cobalt vs. Rhodium Catalysis",
            "content": """Discovered in 1938 by Otto Roelen, **hydroformylation** converts alkenes, carbon monoxide, and dihydrogen (syngas) into aldehydes:
\\[ R-\\text{CH}=\\text{CH}_2 + \\text{CO} + \\text{H}_2 \\xrightarrow{\\text{Catalyst}} R-\\text{CH}_2\\text{CH}_2\\text{CHO} \\text{ (linear)} + R-\\text{CH}(\\text{CHO})\\text{CH}_3 \\text{ (branched)} \\]
It is the largest-volume homogeneous catalytic process in the global chemical industry ($>15$ million metric tons annually).

### Comparison of Industrial Catalyst Systems:
| Metric | Unmodified Cobalt | Phosphine-Modified Cobalt | Rhodium-Phosphine (Low-Pressure Oxo) |
| :--- | :--- | :--- | :--- |
| **Active Catalyst** | $\\text{HCo}(\\text{CO})_4$ | $\\text{HCo}(\\text{CO})_3(\\text{PBu}_3)$ | $\\text{HRh}(\\text{CO})(\\text{PPh}_3)_2$ |
| **Temperature** | $140 - 180^\\circ\\text{C}$ | $160 - 200^\\circ\\text{C}$ | $85 - 110^\\circ\\text{C}$ |
| **Pressure** | $200 - 300\\text{ bar}$ | $50 - 100\\text{ bar}$ | $15 - 30\\text{ bar}$ |
| **Activity** | Moderate | Low | Extremely High ($10^3 \\times \\text{Co}$) |
| **Linear:Branched ($l:b$)** | $3:1 - 4:1$ | $7:1 - 9:1$ | **$15:1 - 50:1$** |
| **Byproduct Hydrogenation** | Minimal | High (alcohols formed) | Negligible |

The modern Low-Pressure Oxo (LPO) process developed by Union Carbide / Davy Powergas employs rhodium with excess triphenylphosphine, operating under exceptionally mild conditions and delivering premium linear aldehydes."""
        },
        {
            "id": "sec9_5",
            "title": "§9.5 Regioselectivity Control in Hydroformylation: Linear vs. Branched Aldehydes",
            "content": """In industrial hydroformylation of terminal alkenes, the linear aldehyde ($n$-aldehyde) is preferred for plasticizer alcohols (e.g., 2-ethylhexanol) and biodegradable detergents.

### Origin of Regioselectivity:
Regioselectivity is established during the **1,2-migratory insertion of the alkene into the metal-hydride bond**:
1. **Anti-Markovnikov Insertion**:
   - The hydride transfers to the internal secondary carbon (C2), while the metal attaches to the terminal primary carbon (C1):
     \\[ M-\\text{H} + R-\\text{CH}=\\text{CH}_2 \\longrightarrow M-\\text{CH}_2\\text{CH}_2 R \\quad (\\text{Linear Alkyl}) \\]
   - Subsequent CO insertion and hydrogenolysis delivers the **linear aldehyde**.
2. **Markovnikov Insertion**:
   - The hydride transfers to the terminal carbon (C1), while the metal attaches to C2:
     \\[ M-\\text{H} + R-\\text{CH}=\\text{CH}_2 \\longrightarrow M-\\text{CH}(R)\\text{CH}_3 \\quad (\\text{Branched Alkyl}) \\]
   - Delivers the **branched aldehyde**.

### Steric Engineering of the Ligand Sphere:
In the rhodium-catalyzed cycle, the active intermediate is the trigonal bipyramidal complex $\\text{HRh}(\\text{CO})_2 L_2$:
- When bulky phosphines (e.g., triphenylphosphine or wide bite-angle diphosphines like Xantphos) coordinate:
  - Steric repulsion between the bulky phosphine ligands and the alkyl substituent $R$ destabilizes the transition state for Markovnikov insertion.
  - The alkene is forced to direct its $R$ group away from the coordination sphere, locking the system into anti-Markovnikov insertion.
  - Using Xantphos ($\\beta_n = 111^\\circ$) raises the linear-to-branched ratio to **$l:b > 50:1$** with $>98\\%$ selectivity."""
        },
        {
            "id": "sec9_6",
            "title": "§9.6 Olefin Metathesis: Historical Evolution & The Chauvin Mechanism",
            "content": """**Olefin metathesis** (from Greek *metathesis*, meaning 'transposition') is a chemical transformation in which carbon-carbon double bonds are cleaved and reformed through the redistribution of alkylidene fragments:
\\[ R_1-\\text{CH}=\\text{CH}-R_1 + R_2-\\text{CH}=\\text{CH}-R_2 \\xrightleftharpoons{\\text{Catalyst}} 2\\,R_1-\\text{CH}=\\text{CH}-R_2 \\]

### The Chauvin Mechanism (1971):
Yves Chauvin proposed that the active catalyst is a **transition metal alkylidene (carbene)** $M=\\text{CHR}$, and that the reaction proceeds through alternating $[2+2]$ cycloadditions and cycloreversions:
1. **$[2+2]$ Cycloaddition**:
   The metal alkylidene coordinates an alkene and undergoes a concerted, symmetry-allowed $[2+2]$ cycloaddition to form a four-membered **metallacyclobutane** intermediate:
   \\[ [M=\\text{CH}R_1] + \\text{H}_2\\text{C}=\\text{CH}R_2 \\rightleftharpoons \\begin{pmatrix} M & = & \\text{CH}R_1 \\\\ \\vert & & \\vert \\\\ \\text{CH}_2 & - & \\text{CH}R_2 \\end{pmatrix} \\]
2. **$[2+2]$ Cycloreversion**:
   The metallacyclobutane cleaves across the perpendicular coordinate, regenerating a new metal alkylidene and releasing a new alkene:
   \\[ \\text{Metallacyclobutane} \\rightleftharpoons [M=\\text{CH}R_2] + \\text{H}_2\\text{C}=\\text{CH}R_1 \\]
3. **Equilibrium and Driving Force**:
   Because every elementary step in the Chauvin cycle is reversible, metathesis of unstrained acyclic alkenes is an equilibrium under thermoneutral enthalpy control (driven entropically by the volatilization of ethylene gas $\\text{H}_2\\text{C}=\\text{CH}_2 \\uparrow$)."""
        },
        {
            "id": "sec9_7",
            "title": "§9.7 Evolution of Metathesis Catalysts: Schrock vs. Grubbs Systems",
            "content": """The development of well-defined metathesis catalysts transformed the field (Nobel Prize in Chemistry, 2005 to Yves Chauvin, Richard R. Schrock, and Robert H. Grubbs):

### 1. Schrock Molybdenum and Tungsten Alkylidenes:
- **Structure**: High-valent $d^0$ complexes $[\\text{Mo}(=\\text{CH}R)(=\\text{NAr})(\\text{OR}')_2]$ featuring an imido ligand ($=\\text{NAr}$) and electron-withdrawing alkoxides (e.g., $-\\text{OCMe}(\\text{CF}_3)_2$).
- **Properties**: Exceptional catalytic activity; capable of metathesizing sterically hindered and electron-deficient alkenes.
- **Drawback**: Extremely sensitive to air, water, and protic functional groups (alcohols, acids).

### 2. Grubbs Ruthenium Alkylidenes:
- **Grubbs 1st Generation (1995)**:
  - Structure: $[(\\text{PCy}_3)_2\\text{Cl}_2\\text{Ru}=\\text{CHPh}]$.
  - Low-valent $d^6$ ruthenium(II) center.
  - Remarkable air- and moisture-tolerance, compatible with alcohols, water, and carboxylic acids. Moderate activity.
- **Grubbs 2nd Generation (1999)**:
  - Structure: Replace one $\\text{PCy}_3$ with an $N$-heterocyclic carbene (**NHC**, $\\text{H}_2\\text{IMes}$ or $\\text{IMes}$).
  - NHCs are superior $\\sigma$-donors that do not dissociate, accelerating the rate of phosphine dissociation and stabilizing the 14-electron ruthenacyclobutane intermediate.
  - Activity matches Schrock catalysts while maintaining full functional group tolerance.
- **Hoveyda-Grubbs 2nd Generation (2000)**:
  - Replaces the phosphine entirely with a chelating *ortho*-isopropoxybenzylidene ligand, yielding exceptional bench-stability and recyclability."""
        },
        {
            "id": "sec9_8",
            "title": "§9.8 Synthetic Variations of Metathesis: RCM, ROMP, CM and Stereocontrol",
            "content": """Olefin metathesis encompasses several major synthetic variations:

1. **Ring-Closing Metathesis (RCM)**:
   - Converts an $\\alpha,\\omega$-diene into a cyclic alkene with extrusion of ethylene gas:
     \\[ \\text{H}_2\\text{C}=\\text{CH}-(CH_2)_n-\\text{CH}=\\text{CH}_2 \\xrightarrow{\\text{Grubbs cat.}} \\text{Cycloalkene} + \\text{H}_2\\text{C}=\\text{CH}_2 \\uparrow \\]
   - Powerful methodology for synthesizing 5- to 8-membered rings as well as macrocyclic lactones and natural products (e.g., epothilones).
2. **Ring-Opening Metathesis Polymerization (ROMP)**:
   - Driven by the release of ring strain from cyclic alkenes (e.g., norbornene $\\Delta H_\\text{strain} \\approx 110\\text{ kJ/mol}$, dicyclopentadiene):
     \\[ \\text{Norbornene} \\xrightarrow{\\text{ROMP}} [-\\text{CH}=\\text{CH}-\\text{C}_5\\text{H}_8-]_n \\quad (\\text{Polynorbornene}) \\]
   - Produces living polymers with controlled molecular weights and narrow polydispersity ($PDI < 1.1$).
3. **Cross-Metathesis (CM)**:
   - Intermolecular coupling of two different acyclic alkenes. Regulated by Grubbs' classification of olefins into Type I through Type IV based on their rates of homodimerization and homocoupling.
4. **$Z$-Selective Metathesis**:
   - Modern cyclometallated ruthenium and Schrock molybdenum catalysts enforce formation of thermodynamically less stable **$(Z)$-alkenes** with $>95\\%\\ Z$-selectivity, critical for pheromone and drug manufacturing."""
        }
    ]

    problems = [
        {
            "id": "prob9_1",
            "tier": "Foundational",
            "title": "Turnover Number (TON) and Turnover Frequency (TOF) Calculations",
            "statement": "In a homogeneous hydrogenation reaction, $2.5\\text{ mg}$ of Wilkinson's catalyst $\\text{RhCl}(\\text{PPh}_3)_3$ (molar mass $925.2\\text{ g/mol}$) is dissolved with $5.0\\text{ g}$ of cyclohexene (molar mass $82.14\\text{ g/mol}$) in $50\\text{ mL}$ of benzene under $1.0\\text{ bar}$ of $\\text{H}_2$. After $45\\text{ minutes}$, GC analysis shows $94\\%$ conversion to cyclohexane. (a) Calculate the moles of catalyst and substrate. (b) Calculate the turnover number (TON) and turnover frequency (TOF) in $\\text{h}^{-1}$ and $\\text{s}^{-1}$.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of Moles of Catalyst and Substrate:**
1. **Moles of Wilkinson's Catalyst**:
   \\[ n_\\text{cat} = \\frac{2.5 \\times 10^{-3}\\text{ g}}{925.2\\text{ g/mol}} = 2.702 \\times 10^{-6}\\text{ mol} = 2.702\\ \\mu\\text{mol} \\]
2. **Moles of Cyclohexene Substrate**:
   \\[ n_\\text{sub} = \\frac{5.0\\text{ g}}{82.14\\text{ g/mol}} = 0.06087\\text{ mol} = 60.87\\text{ mmol} \\]
3. **Moles of Product Formed at $94\\%$ Conversion**:
   \\[ n_\\text{product} = 0.94 \\times 0.06087 = 0.05722\\text{ mol} \\]

**(b) Calculation of TON and TOF:**
1. **Turnover Number (TON)**:
   \\[ \\text{TON} = \\frac{n_\\text{product}}{n_\\text{cat}} = \\frac{0.05722\\text{ mol}}{2.702 \\times 10^{-6}\\text{ mol}} \\approx \\mathbf{21,177} \\]
2. **Turnover Frequency (TOF)**:
   Reaction time: $t = 45\\text{ minutes} = 0.75\\text{ hours} = 2700\\text{ seconds}$.
   - In units of $\\text{h}^{-1}$:
     \\[ \\text{TOF} = \\frac{\\text{TON}}{t_\\text{hours}} = \\frac{21,177}{0.75\\text{ h}} \\approx \\mathbf{28,236\\text{ h}^{-1}} \\]
   - In units of $\\text{s}^{-1}$:
     \\[ \\text{TOF} = \\frac{\\text{TON}}{t_\\text{seconds}} = \\frac{21,177}{2700\\text{ s}} \\approx \\mathbf{7.84\\text{ s}^{-1}} \\]
- **Conclusion**: The catalyst achieves a TON of $\\approx 2.12 \\times 10^4$ and turns over at a frequency of $\\approx 7.8\\text{ catalytic cycles per second}$."""
        },
        {
            "id": "prob9_2",
            "tier": "Foundational",
            "title": "Substrate Regioselectivity and Chemoselectivity with Wilkinson's Catalyst",
            "statement": "Predict the major organic product when each of the following polyunsaturated substrates is hydrogenated with 1 equivalent of dihydrogen in the presence of Wilkinson's catalyst: (a) Limonene (1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene), (b) 2-Methylbuta-1,3-diene (isoprene), (c) Methyl cinnamate (methyl 3-phenylprop-2-enoate) vs cinnamaldehyde.",
            "solution": """**Line-by-Line Solution:**

**(a) Limonene Hydrogenation:**
1. Structure of limonene:
   - Contains an **endocyclic trisubstituted double bond** in the cyclohexene ring.
   - Contains an **exocyclic disubstituted terminal isopropenyl double bond** ($-\\text{C}(\\text{CH}_3)=\\text{CH}_2$).
2. In Wilkinson's hydrogenation, the rate-determining migratory insertion occurs within a sterically congested coordination sphere. Steric congestion dictates the rate order:
   \\[ \\text{Monosubstituted} > \\text{Disubstituted (terminal)} > \\text{Disubstituted (internal)} \\gg \\text{Trisubstituted} \\]
3. The catalyst coordinates and hydrogenates the less sterically hindered **exocyclic isopropenyl double bond** selectively:
   \\[ \\text{Major Product}: \\mathbf{p\\text{-menth-1-ene}} \\text{ (carvomenthene)} \\]
   leaving the endocyclic trisubstituted double bond intact.

**(b) Isoprene (2-Methylbuta-1,3-diene):**
1. Isoprene contains two double bonds: a monosubstituted terminal double bond (C3=C4) and a 1,1-disubstituted double bond (C1=C2).
2. Coordination occurs preferentially at the less hindered monosubstituted C3=C4 bond.
3. Hydrogenation of C3=C4 with 1 equivalent of $\\text{H}_2$ yields:
   \\[ \\text{Major Product}: \\mathbf{2\\text{-methylbut-1-ene}} \\text{ (and 2-methylbut-2-ene via isomerisation)} \\]

**(c) Methyl Cinnamate vs. Cinnamaldehyde:**
1. Wilkinson's catalyst hydrogenates carbon-carbon double bonds rapidly, while aldehydes and esters are completely inert under standard conditions (carbonyl groups do not coordinate strongly to $\\text{Rh}(\\text{I})$).
2. For cinnamaldehyde ($\\text{PhCH}=\\text{CH}-\\text{CHO}$):
   - Chemoselective reduction of the $C=C$ double bond occurs, leaving the aldehyde group intact:
   \\[ \\text{Major Product}: \\mathbf{3\\text{-phenylpropanal}} \\text{ (hydrocinnamaldehyde)} \\]"""
        },
        {
            "id": "prob9_3",
            "tier": "Foundational",
            "title": "Chauvin Cycle Metathesis Product Prediction",
            "statement": "Predict the initial metathesis products (including the volatile byproduct that drives the reaction to completion) for: (a) Ring-closing metathesis of diethyl diallylmalonate catalyzed by Grubbs 1st generation catalyst. (b) Cross-metathesis between allylbenzene and excess *cis*-1,4-diacetoxybut-2-ene. (c) Ring-opening metathesis polymerization (ROMP) of cyclopentene.",
            "solution": """**Line-by-Line Solution:**

**(a) Ring-Closing Metathesis (RCM) of Diethyl Diallylmalonate:**
1. Substrate structure: $(\\text{EtO}_2\\text{C})_2\\text{C}(\\text{CH}_2-\\text{CH}=\\text{CH}_2)_2$ (a 1,6-diene).
2. The ruthenium carbene coordinates one terminal alkene, forms a ruthenacyclobutane, and transfers the alkylidene onto the substrate.
3. Intramolecular $[2+2]$ cycloaddition with the second terminal alkene closes a cyclopentene ring:
   \\[ \\text{Organic Product}: \\mathbf{\\text{Diethyl cyclopent-3-ene-1,1-dicarboxylate}} \\]
4. Byproduct: The two terminal methylene ($=\\text{CH}_2$) groups combine to release **ethene gas** $\\mathbf{\\text{H}_2\\text{C}=\\text{CH}_2 \\uparrow}$, which bubbles out of solution, shifting the equilibrium quantitatively to $100\\%$ conversion.

**(b) Cross-Metathesis (CM) of Allylbenzene:**
1. Reactants: Allylbenzene $\\text{PhCH}_2-\\text{CH}=\\text{CH}_2$ and symmetric *cis*-1,4-diacetoxybut-2-ene $\\text{AcOCH}_2-\\text{CH}=\\text{CH}-\\text{CH}_2\\text{OAc}$.
2. Transposition of the alkylidene fragments cleaves the terminal alkene and exchanges fragments:
   \\[ \\text{Major Product}: \\mathbf{(E)\\text{-4-phenylbut-2-en-1-yl acetate}} \\; (\\text{PhCH}_2-\\text{CH}=\\text{CH}-\\text{CH}_2\\text{OAc}) \\]
3. Volatile byproduct: **Ethene gas** $\\text{H}_2\\text{C}=\\text{CH}_2 \\uparrow$.

**(c) Ring-Opening Metathesis Polymerization (ROMP) of Cyclopentene:**
1. Cyclopentene is a cyclic alkene possessing low-to-moderate ring strain ($\approx 28\\text{ kJ/mol}$).
2. Coordination to the ruthenium carbene and $[2+2]$ cycloaddition forms a bicyclic ruthenacyclobutane.
3. Cycloreversion opens the five-membered ring, regenerating an active propagating alkylidene chain end:
   \\[ \\text{Polymer Product}: \\mathbf{\\text{Polypentenamer}} \\; [-\\text{CH}=\\text{CH}-\\text{CH}_2\\text{CH}_2\\text{CH}_2-]_n \\]
   containing repeating pentamethylene units with alternating double bonds."""
        },
        {
            "id": "prob9_4",
            "tier": "Intermediate",
            "title": "Derivation of the Rate Law for Wilkinson's Hydrogenation",
            "statement": "The rate of homogeneous hydrogenation of cyclohexene catalyzed by Wilkinson's catalyst follows the empirical equation: $\\text{Rate} = \\frac{k K_1 K_2 [\\text{H}_2][\\text{olefin}][\\text{Rh}]_0}{1 + K_1 [\\text{H}_2] + K_2 [\\text{olefin}] + K_3 [\\text{PPh}_3]}$. Derive this rate equation from the dihydride catalytic cycle using the steady-state approximation and mass balance on rhodium.",
            "solution": """**Line-by-Line Solution:**

**1. Catalytic Reaction Sequence (The Dihydride Route):**
- Let $P = \\text{PPh}_3$. The precursor $[\\text{RhCl}P_3]$ undergoes dissociation:
  \\[ \\text{RhCl}P_3 \\xrightleftharpoons{K_d} [\\text{RhCl}P_2] + P \\]
- The 14e species $[\\text{RhCl}P_2]$ undergoes oxidative addition of $\\text{H}_2$:
  \\[ [\\text{RhCl}P_2] + \\text{H}_2 \\xrightleftharpoons{K_1} [\\text{RhCl}(\\text{H})_2 P_2] \\]
- Coordination of olefin ($O$):
  \\[ [\\text{RhCl}(\\text{H})_2 P_2] + O \\xrightleftharpoons{K_2} [\\text{RhCl}(\\text{H})_2(O)P_2] \\]
- Alternatively, direct coordination of olefin to $[\\text{RhCl}P_2]$:
  \\[ [\\text{RhCl}P_2] + O \\xrightleftharpoons{K_O} [\\text{RhCl}(O)P_2] \\]
- The turnover-limiting step is the migratory insertion and subsequent fast reductive elimination:
  \\[ [\\text{RhCl}(\\text{H})_2(O)P_2] \\xrightarrow{k} [\\text{RhCl}P_2] + \\text{alkane} \\]

**2. Rate of Hydrogenation:**
\\[ \\text{Rate} = k [\\text{RhCl}(\\text{H})_2(O)P_2] = k K_2 [\\text{RhCl}(\\text{H})_2 P_2] [O] = k K_1 K_2 [\\text{RhCl}P_2] [\\text{H}_2] [O] \\]

**3. Total Rhodium Mass Balance:**
The total rhodium catalyst concentration $[\\text{Rh}]_0$ is distributed among all rhodium-containing species in solution:
\\[ [\\text{Rh}]_0 = [\\text{RhCl}P_2] + [\\text{RhCl}P_3] + [\\text{RhCl}(\\text{H})_2 P_2] + [\\text{RhCl}(O)P_2] + [\\text{RhCl}(\\text{H})_2(O)P_2] \\]
Expressing each species in terms of $[\\text{RhCl}P_2]$:
- $[\\text{RhCl}P_3] = \\frac{[P]}{K_d} [\\text{RhCl}P_2] = K_3' [P] [\\text{RhCl}P_2]$
- $[\\text{RhCl}(\\text{H})_2 P_2] = K_1 [\\text{H}_2] [\\text{RhCl}P_2]$
- $[\\text{RhCl}(O)P_2] = K_O [O] [\\text{RhCl}P_2]$
- $[\\text{RhCl}(\\text{H})_2(O)P_2] = K_1 K_2 [\\text{H}_2][O] [\\text{RhCl}P_2]$ (typically negligible in the resting state balance under low olefin concentration)

Factoring $[\\text{RhCl}P_2]$:
\\[ [\\text{Rh}]_0 = [\\text{RhCl}P_2] \\left( 1 + K_1 [\\text{H}_2] + K_O [O] + K_3' [P] \\right) \\]
\\[ [\\text{RhCl}P_2] = \\frac{[\\text{Rh}]_0}{1 + K_1 [\\text{H}_2] + K_O [O] + K_3' [P]} \\]

**4. Final Rate Law:**
Substitute $[\\text{RhCl}P_2]$ into the rate equation:
\\[ \\text{Rate} = \\frac{k K_1 K_2 [\\text{H}_2][O][\\text{Rh}]_0}{1 + K_1 [\\text{H}_2] + K_O [O] + K_3' [P]} \\]
- **Order Analysis**:
  - At low $[\\text{H}_2]$, the rate is first-order in $[\\text{H}_2]$; at high $[\\text{H}_2]$, it approaches zero-order.
  - Adding excess triphenylphosphine $[P]$ increases the denominator, inhibiting the reaction rate ($-\\text{order}$ in $[\\text{PPh}_3]$)."""
        },
        {
            "id": "prob9_5",
            "tier": "Intermediate",
            "title": "Stereochemical Kinetic Analysis of the Halpern Mechanism",
            "statement": "In the asymmetric hydrogenation of methyl 2-acetamidoacrylate catalyzed by $[\\text{Rh}((R,R)-\\text{DIPAMP})]^+$, the major catalyst-substrate complex $C_\\text{maj}$ constitutes $95\\%$ of the resting state, while the minor complex $C_\\text{min}$ constitutes $5\\%$ ($K_\\text{eq} = [C_\\text{maj}]/[C_\\text{min}] = 19$). Oxidative addition of $\\text{H}_2$ occurs with rate constants $k_\\text{maj} = 0.15\\text{ M}^{-1}\\text{s}^{-1}$ and $k_\\text{min} = 950\\text{ M}^{-1}\\text{s}^{-1}$. (a) Calculate the ratio of rates of product formation via the minor pathway versus the major pathway. (b) Calculate the resulting enantiomeric excess ($ee$). (c) Explain why decreasing $\\text{H}_2$ pressure increases the enantiomeric excess.",
            "solution": """**Line-by-Line Solution:**

**(a) Ratio of Product Formation Rates:**
1. The rate of product formation from each diastereomeric pathway is:
   \\[ R_\\text{maj} = k_\\text{maj} [C_\\text{maj}] [\\text{H}_2] \\]
   \\[ R_\\text{min} = k_\\text{min} [C_\\text{min}] [\\text{H}_2] \\]
2. The ratio of rates is:
   \\[ \\frac{R_\\text{min}}{R_\\text{maj}} = \\frac{k_\\text{min} [C_\\text{min}]}{k_\\text{maj} [C_\\text{maj}]} = \\left( \\frac{k_\\text{min}}{k_\\text{maj}} \\right) \\left( \\frac{[C_\\text{min}]}{[C_\\text{maj}]} \\right) \\]
3. Substitute the given kinetic and equilibrium values:
   - $\\frac{k_\\text{min}}{k_\\text{maj}} = \\frac{950}{0.15} \\approx 6333.3$
   - $\\frac{[C_\\text{min}]}{[C_\\text{maj}]} = \\frac{1}{19} \\approx 0.05263$
   \\[ \\frac{R_\\text{min}}{R_\\text{maj}} = 6333.3 \\times \\frac{1}{19} = \\frac{6333.3}{19} \\approx \\mathbf{333.3} \\]
- **Conclusion**: Product formation via the **minor diastereomer is 333 times faster** than via the major diastereomer!

**(b) Calculation of Enantiomeric Excess ($ee$):**
1. The minor diastereomer produces the $(S)$-enantiomer, and the major diastereomer produces the $(R)$-enantiomer:
   \\[ \\text{Ratio of enantiomers } \\frac{[S]}{[R]} = 333.3 \\]
2. Compute $ee$:
   \\[ ee = \\frac{[S] - [R]}{[S] + [R]} \\times 100\\% = \\frac{333.3 - 1}{333.3 + 1} \\times 100\\% = \\frac{332.3}{334.3} \\times 100\\% \\approx \\mathbf{99.4\\%\\ ee} \\]
- **Result**: The reaction delivers $(S)$-product with **$99.4\\%$ enantiomeric excess**!

**(c) Pressure Dependence of Enantiomeric Excess:**
1. The Halpern mechanism relies on **rapid pre-equilibrium** between $C_\\text{maj}$ and $C_\\text{min}$ compared to the rate of oxidative addition of dihydrogen:
   \\[ k_\\text{interconversion} \\gg k_\\text{min} [\\text{H}_2] \\]
2. If the partial pressure of dihydrogen $P(\\text{H}_2)$ is raised to high levels, the rate of oxidative addition $k_\\text{min} [\\text{H}_2]$ increases linearly.
3. At very high $\\text{H}_2$ pressure, oxidative addition begins to compete with the interconversion rate between $C_\\text{maj}$ and $C_\\text{min}$ (Curtin-Hammett breakdown).
4. As interconversion becomes non-equilibrating, more product is forced to form through the slower but predominantly present major complex $C_\\text{maj}$, which produces the undesired $(R)$-enantiomer.
5. Therefore, **low $\\text{H}_2$ pressure preserves the rapid pre-equilibrium**, maximizing the Curtin-Hammett kinetic partitioning through the fast minor pathway and increasing the enantiomeric excess."""
        },
        {
            "id": "prob9_6",
            "tier": "Intermediate",
            "title": "Thermodynamics and Regioselectivity in Industrial Hydroformylation",
            "statement": "In the rhodium-catalyzed hydroformylation of 1-hexene to heptanal (linear) and 2-methylhexanal (branched): (a) The standard enthalpies of reaction are $\\Delta H_\\text{lin}^\\circ = -118\\text{ kJ/mol}$ and $\\Delta H_\\text{br}^\\circ = -115\\text{ kJ/mol}$, with standard entropies $\\Delta S_\\text{lin}^\\circ = -195\\text{ J/(mol}\\cdot\\text{K)}$ and $\\Delta S_\\text{br}^\\circ = -188\\text{ J/(mol}\\cdot\\text{K)}$. Calculate $\\Delta G^\\circ$ for both pathways at $373\\text{ K}$. (b) Explain why industrial regioselectivity ($l:b = 30:1$) is kinetically controlled rather than thermodynamically controlled.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of $\\Delta G^\\circ$ at $373\\text{ K}$:**
\\[ \\Delta G^\\circ(T) = \\Delta H^\\circ - T\\Delta S^\\circ \\]

1. **For the Linear Product (Heptanal)**:
   - $\\Delta H_\\text{lin}^\\circ = -118,000\\text{ J/mol}$
   - $\\Delta S_\\text{lin}^\\circ = -195\\text{ J/(mol}\\cdot\\text{K)}$
   \\[ \\Delta G_\\text{lin}^\\circ(373) = -118,000 - (373)(-195) = -118,000 - (-72,735) = -118,000 + 72,735 = \\mathbf{-45,265\\text{ J/mol}} \\approx -45.3\\text{ kJ/mol} \\]

2. **For the Branched Product (2-Methylhexanal)**:
   - $\\Delta H_\\text{br}^\\circ = -115,000\\text{ J/mol}$
   - $\\Delta S_\\text{br}^\\circ = -188\\text{ J/(mol}\\cdot\\text{K)}$
   \\[ \\Delta G_\\text{br}^\\circ(373) = -115,000 - (373)(-188) = -115,000 - (-70,124) = -115,000 + 70,124 = \\mathbf{-44,876\\text{ J/mol}} \\approx -44.9\\text{ kJ/mol} \\]

3. **Thermodynamic Free Energy Difference**:
   \\[ \\Delta\\Delta G^\\circ = \\Delta G_\\text{br}^\\circ - \\Delta G_\\text{lin}^\\circ = -44,876 - (-45,265) = +389\\text{ J/mol} \\]
   The thermodynamic equilibrium ratio at $373\\text{ K}$ would be:
   \\[ \\left(\\frac{[\text{lin}]}{[\text{br}]}\\right)_\\text{thermo} = \\exp\\left(\\frac{\\Delta\\Delta G^\\circ}{RT}\\right) = \\exp\\left(\\frac{389}{(8.3145)(373)}\\right) = \\exp(0.125) \\approx \\mathbf{1.13 : 1} \\]

**(b) Kinetic Origin of Industrial $l:b$ Selectivity ($30:1$):**
- Thermodynamic control would predict an almost equimolar $l:b$ ratio of **$1.13 : 1$** (only $53\\%$ linear).
- However, the industrial process routinely achieves **$l:b = 30:1$ to $50:1$** ($>97\\%$ linear).
- This proves that hydroformylation is **strictly kinetically controlled**:
  1. Once the alkene undergoes irreversible 1,2-migratory insertion and CO insertion, the resulting acyl intermediates do not equilibrate back to alkene under low-pressure rhodium conditions.
  2. The activation energy barrier for anti-Markovnikov insertion is lower than for Markovnikov insertion by $\\Delta\\Delta G^\\ddagger \\approx 10-12\\text{ kJ/mol}$ due to steric repulsion between the alkene's alkyl tail and the bulky equatorial phosphine ligands ($\text{PPh}_3$ or diphosphines).
  3. This difference in activation energy dictates the high observed linear regioselectivity."""
        },
        {
            "id": "prob9_7",
            "tier": "Advanced",
            "title": "Quantum Mechanics of the Chauvin Metallacyclobutane Intermediate Stability",
            "statement": "The four-membered metallacyclobutane intermediate $[L_n M(\\text{C}_3\\text{H}_6)]$ in olefin metathesis can adopt planar or puckered geometries. (a) Construct the orbital interaction diagram between a $d^2$ metal alkylidene $[L_n M=\\text{CH}_2]$ and ethylene. (b) Explain why electron-donating $N$-heterocyclic carbenes (NHCs) in Grubbs 2nd generation catalysts stabilize the 14-electron ruthenacyclobutane transition state. (c) Explain why early transition metal metallacyclobutanes (titanium, tantalum) are isolable ground states (e.g., Tebbe's reagent), while ruthenium analogs are short-lived reactive intermediates.",
            "solution": """**Line-by-Line Solution:**

**(a) Orbital Interaction Diagram of $[2+2]$ Cycloaddition:**
1. **Metal Alkylidene $L_n M=\\text{CH}_2$**:
   - The $M=C$ double bond consists of a $\\sigma$-bonding orbital (HOMO$-1$) and a localized $\\pi(M=C)$ bonding orbital (HOMO).
   - The LUMO is the low-lying $\\pi^*(M=C)$ antibonding orbital, polarized heavily toward the metal atom (significant $d_\\pi$ character).
2. **Alkene $\\text{H}_2\\text{C}=\\text{CH}_2$**:
   - The HOMO is the bonding $\\pi_{CC}$ orbital.
   - The LUMO is the antibonding $\\pi_{CC}^*$ orbital.
3. **Concerted $[2+2]$ Orbital Mixing**:
   - Primary interaction 1: Alkene $\\pi_{CC}$ (HOMO) donates into the empty metal alkylidene $\\pi^*(M=C)$ (LUMO).
   - Primary interaction 2: Filled alkylidene $\\pi(M=C)$ (HOMO) backdonates into the empty alkene $\\pi_{CC}^*$ (LUMO).
   - Because the transition metal provides an accessible $d$-orbital that changes oxidation state ($M^n \\rightleftharpoons M^{n+2}$), the orbital symmetry restrictions that forbid organic $[\\pi 2_s + \\pi 2_s]$ cycloadditions are completely lifted!

**(b) Role of $N$-Heterocyclic Carbenes (NHCs) in Grubbs 2nd Generation Catalysts:**
1. In Grubbs 1st generation $[(\\text{PCy}_3)_2\\text{Cl}_2\\text{Ru}=\\text{CHPh}]$, the catalyst must dissociate one $\\text{PCy}_3$ phosphine to generate the active 14-electron intermediate:
   \\[ [(\\text{PCy}_3)_2\\text{Cl}_2\\text{Ru}=\\text{CHPh}] \\xrightleftharpoons{-\\text{PCy}_3} [(\\text{PCy}_3)\\text{Cl}_2\\text{Ru}=\\text{CHPh}] \\quad (14\\text{e}) \\]
2. Phosphine dissociation is slow ($k_1 \\approx 10^{-2}\\text{ s}^{-1}$), and the empty coordination site is readily recaptured by free $\\text{PCy}_3$ ($k_{-1} \\gg k_\\text{olefin}$).
3. In Grubbs 2nd generation catalysts $[(\\text{NHC})(\\text{PCy}_3)\\text{Cl}_2\\text{Ru}=\\text{CHPh}]$:
   - The NHC ligand is an extraordinarily powerful **$\\sigma$-donor** with negligible $\\pi$-acceptor ability.
   - Its massive electron donation exerts a strong trans-effect that accelerates phosphine dissociation.
   - More crucially, the electron-rich NHC ligand stabilizes the resulting electron-deficient 14-electron ruthenacyclobutane intermediate by $\\sigma$-electron donation, lowering the activation barrier for the $[2+2]$ cycloaddition step by over $25\\text{ kJ/mol}$ and boosting overall metathesis activity by $>10^4$.

**(c) Isolability of Titanium (Tebbe) vs. Lability of Ruthenium Metallacyclobutanes:**
1. **Titanium Metallacyclobutanes (e.g., Grubbs' Titanacyclobutanes from Tebbe's Reagent)**:
   - Titanium is in a high formal oxidation state $\\text{Ti}(\\text{IV})$ ($d^0$).
   - It possesses strong, covalent, localized $\\text{Ti}-\\text{C}$ $\\sigma$-bonds with high bond enthalpies ($D_0 \\approx 330\\text{ kJ/mol}$).
   - Because $\\text{Ti}(\\text{IV})$ is $d^0$, there are no filled $d$-electrons to initiate reductive cycloreversion back to a low-valent titanium(II) species.
   - Consequently, titanacyclobutanes sit in a deep thermodynamic energy well and can be isolated as bench-stable crystalline solids.
2. **Ruthenium Metallacyclobutanes**:
   - Ruthenium resides in the $\\text{Ru}(\\text{IV})$ oxidation state ($d^4$).
   - The metal center has accessible $d$-electrons that readily participate in orbital-assisted retro-$[2+2]$ cycloreversion back to the thermodynamically favored $\\text{Ru}(\\text{II})$ ($d^6$) alkylidene.
   - The ruthenacyclobutane represents a shallow, transient intermediate on the potential energy surface, turning over millions of times per second."""
        },
        {
            "id": "prob9_8",
            "tier": "Advanced",
            "title": "Thermodynamics and Living Polymerization Kinetics in ROMP",
            "statement": "Norbornene undergoes Ring-Opening Metathesis Polymerization (ROMP) with a 2nd generation Grubbs catalyst to yield polynorbornene. (a) Given ring strain enthalpy $\\Delta H_\\text{strain} = -110\\text{ kJ/mol}$ and standard polymerization entropy $\\Delta S^\\circ = -85\\text{ J/(mol}\\cdot\\text{K)}$, calculate the ceiling temperature $T_c$ of norbornene polymerization at $[M]_0 = 1.0\\text{ M}$. (b) If polymerization follows living kinetics where $k_p = 140\\text{ M}^{-1}\\text{s}^{-1}$ and $[\\text{Ru}]_0 = 1.0 \\times 10^{-4}\\text{ M}$, calculate the time required for $99\\%$ monomer conversion. (c) Derive the theoretical Polydispersity Index (PDI) for a Poisson distribution with degree of polymerization $\\overline{X}_n = 500$.",
            "solution": """**Line-by-Line Solution:**

**(a) Ceiling Temperature Calculation:**
At the thermodynamic ceiling temperature $T_c$:
\\[ \\Delta G_p^\\circ(T_c) = \\Delta H_p^\\circ - T_c \\Delta S_p^\\circ = 0 \\implies T_c = \\frac{\\Delta H_p^\\circ}{\\Delta S_p^\\circ} \\]
Given:
- $\\Delta H_p^\\circ \\approx \\Delta H_\\text{strain} = -110\\text{ kJ/mol} = -110,000\\text{ J/mol}$
- $\\Delta S_p^\\circ = -85\\text{ J/(mol}\\cdot\\text{K)}$ (standard state $[M] = 1.0\\text{ M}$)
\\[ T_c = \\frac{-110,000\\text{ J/mol}}{-85\\text{ J/(mol}\\cdot\\text{K)}} \\approx \\mathbf{1294\\text{ K}} \\approx 1021^\\circ\\text{C} \\]
- **Conclusion**: Because of the colossal ring strain of the bicyclo[2.2.1]heptene skeleton ($110\\text{ kJ/mol}$), the ceiling temperature is over $1000^\\circ\\text{C}$. At all normal processing temperatures ($-20^\\circ\\text{C}$ to $100^\\circ\\text{C}$), ROMP of norbornene is completely irreversible and driven to $100\\%$ conversion.

**(b) Reaction Time for $99\\%$ Monomer Conversion:**
For an ideal living polymerization with instantaneous initiation ($k_i \\ge k_p$):
\\[ -\\frac{d[M]}{dt} = k_p [\\text{Ru}]_0 [M] \\]
Integrating from $t = 0$ to $t$:
\\[ \\ln\\left( \\frac{[M]_0}{[M]} \\right) = k_p [\\text{Ru}]_0 t \\]
For $99\\%$ conversion ($[M] / [M]_0 = 0.01$):
\\[ \\ln(100) = k_p [\\text{Ru}]_0 t \\]
Given:
- $k_p = 140\\text{ M}^{-1}\\text{s}^{-1}$
- $[\\text{Ru}]_0 = 1.0 \\times 10^{-4}\\text{ M}$
- Apparent rate constant $k_\\text{app} = k_p [\\text{Ru}]_0 = (140)(1.0 \\times 10^{-4}) = 0.014\\text{ s}^{-1}$
- $\\ln(100) \\approx 4.6052$

Solve for time $t$:
\\[ t = \\frac{4.6052}{0.014\\text{ s}^{-1}} \\approx \\mathbf{328.9\\text{ seconds}} \\approx \\mathbf{5.48\\text{ minutes}} \\]
- The polymerization reaches $99\\%$ conversion in under $5.5\\text{ minutes}$.

**(c) Polydispersity Index (PDI) for Living Poisson Distribution:**
In a living polymerization free of chain transfer and termination, the molecular weight distribution obeys a Poisson distribution:
- Number-average degree of polymerization: $\\overline{X}_n = 500$.
- Weight-average degree of polymerization:
  \\[ \\overline{X}_w = \\overline{X}_n + 1 - \\frac{1}{\\overline{X}_n} \\]
- The Polydispersity Index (PDI, $\\text{Đ}$) is:
  \\[ \\text{PDI} = \\frac{\\overline{X}_w}{\\overline{X}_n} = 1 + \\frac{1}{\\overline{X}_n} - \\frac{1}{\\overline{X}_n^2} \\approx 1 + \\frac{1}{\\overline{X}_n} \\]
For $\\overline{X}_n = 500$:
\\[ \\text{PDI} = 1 + \\frac{1}{500} = 1 + 0.002 = \\mathbf{1.002} \\]
- **Result**: The polymer possesses near-monodisperse architecture with a theoretical PDI of **1.002**."""
        },
        {
            "id": "prob9_9",
            "tier": "Advanced",
            "title": "Stereoselective $Z$-Alkene Synthesis via Cyclometallated Ruthenium Catalysts",
            "statement": "Conventional Grubbs catalysts produce thermodynamically favored $(E)$-alkenes during cross-metathesis. Modern cyclometallated $Z$-selective catalysts (Grubbs-Hoveyda $Z$-catalysts) invert this preference to deliver $(Z)$-alkenes with $>95\\%$ selectivity. (a) Draw the ruthenacyclobutane transition state for conventional $(E)$-selective metathesis versus $Z$-selective metathesis. (b) Explain the steric shielding mechanism of the bulky, bidentate $N$-arylamido or cyclometallated NHC ligand that forces both alkylidene substituents into a *cis* orientation. (c) Derive why $(Z)$-selectivity drops at high conversion if the catalyst is not completely stereoretentive.",
            "solution": """**Line-by-Line Solution:**

**(a) Ruthenacyclobutane Transition States:**
1. **Conventional $(E)$-Selective Metathesis (All-Trans TS)**:
   - In unconstrained ruthenacyclobutanes, the four-membered ring adopts a puckered or planar geometry where the two substituents $R_1$ and $R_2$ orient themselves in a **trans-diequatorial** arrangement (pointing away from each other on opposite faces of the ring).
   - This minimizes 1,2-steric repulsion between the substituents, cycloreverting to release the thermodynamically favored **$(E)$-alkene**.
2. **$Z$-Selective Metathesis (All-Cis TS)**:
   - The ruthenacyclobutane forces both substituents $R_1$ and $R_2$ to reside on the **same face** of the four-membered ring (*cis*-conformation).
   - Cycloreversion of this *cis*-metallacyclobutane delivers the **$(Z)$-alkene**.

**(b) Steric Shielding Mechanism of Cyclometallated $Z$-Catalysts:**
1. In modern $Z$-selective catalysts, one of the $N$-aryl groups of the NHC ligand is replaced by a sterically massive, cyclometallated adamantly, mesityl, or nitrato chelate that reaches directly over the ruthenium center.
2. This creates an asymmetric, deep steric pocket:
   - One quadrant of the metal coordination sphere is completely blocked by the bulky, rigid ligand architecture.
   - The other quadrant remains open.
3. When the two alkene fragments coordinate and form the ruthenacyclobutane:
   - Orienting one substituent trans would force it to point directly into the heavily congested, blocked quadrant, incurring catastrophic steric clash ($>80\\text{ kJ/mol}$).
   - To avoid this clash, both substituents are forced to point together out of the **open quadrant**.
   - Consequently, the only accessible transition state is the one where both $R_1$ and $R_2$ are *cis* to each other.
   - Cycloreversion delivers the kinetically controlled **$(Z)$-alkene** with $>95\\%$ stereocontrol.

**(c) Secondary Metathesis and Degradation of $(Z)$-Selectivity at High Conversion:**
1. The desired $(Z)$-alkene is the **kinetically controlled product**, but it is thermodynamically less stable than the $(E)$-alkene by $\\Delta G^\\circ \\approx 4 - 8\\text{ kJ/mol}$ due to steric clash between the cis alkyl groups.
2. Once the starting terminal alkene is depleted at high conversion ($>95\\%$):
   - The active catalyst can coordinate the newly formed $(Z)$-alkene product.
   - This initiates **secondary metathesis** (cross-metathesis with itself or ethylene).
3. If the catalyst undergoes minor decomposition or if non-stereospecific cycloreversion occurs even $1\\%$ of the time, the $(Z)$-alkene will be isomerized irreversibly into the thermodynamically downhill $(E)$-alkene:
   \\[ (Z)\\text{-Alkene} \\xrightleftharpoons{\\text{Secondary Metathesis}} (E)\\text{-Alkene} \\quad (\\Delta G^\\circ < 0) \\]
4. Therefore, to preserve $>95\\%\\ Z$-selectivity, reactions must be halted before complete monomer depletion, or run with ultra-active catalysts under strict kinetic quenching."""
        }
    ]

    return {
        "unit_number": 9,
        "title": "Homogeneous Catalysis: Hydrogenation, Hydroformylation & Olefin Metathesis",
        "description": "Principles of homogeneous catalysis, turnover numbers and turnover frequencies, Wilkinson's catalyst hydrogenation mechanism and kinetics, asymmetric hydrogenation by Knowles and Noyori, the Halpern minor-isomer mechanism, industrial hydroformylation (the Oxo process) with cobalt and rhodium catalysts, regioselectivity engineering (linear vs branched), the Chauvin metallacyclobutane metathesis mechanism, Schrock vs Grubbs catalysts, RCM, ROMP, CM, and Z-selective metathesis.",
        "sections": sections,
        "problems": problems
    }
