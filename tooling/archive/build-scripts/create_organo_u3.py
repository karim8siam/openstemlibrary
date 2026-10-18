"""
create_organo_u3.py
Unit 3: Metal Carbonyls, Nitrosyls & Phosphine Complexes
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_3():
    sections = [
        {
            "id": "sec3_1",
            "title": "§3.1 Synthesis of Binary and Mixed Metal Carbonyls",
            "content": """Metal carbonyls are the cornerstones of transition metal organometallic chemistry. In these complexes, carbon monoxide acts as an amphiphilic $\\pi$-acid ligand, stabilizing transition metals in low or zero formal oxidation states.

### Primary Synthetic Methods:
1. **Direct Carbonylation**: Highly electropositive metals in fine division react directly with gaseous carbon monoxide at elevated pressure:
   \\[ \\text{Ni (powder)} + 4\\,\\text{CO} \\xrightarrow{1\\text{ atm},\\, 50^\\circ\\text{C}} \\text{Ni}(\\text{CO})_4 \\quad (\\text{Mond Process}) \\]
   \\[ \\text{Fe (spongy)} + 5\\,\\text{CO} \\xrightarrow{100-200\\text{ atm},\\, 150-200^\\circ\\text{C}} \\text{Fe}(\\text{CO})_5 \\]
2. **Reductive Carbonylation**: Transition metal halides in higher oxidation states are reduced in the presence of carbon monoxide using reducing agents such as aluminum powder, triethylaluminum, sodium, or magnesium:
   \\[ \\text{CrCl}_3 + 6\\,\\text{CO} + \\text{Al} \\xrightarrow{\\text{benzene},\\, 300\\text{ atm}} \\text{Cr}(\\text{CO})_6 + \\text{AlCl}_3 \\]
   \\[ 2\\,\\text{CoCO}_3 + 2\\,\\text{H}_2 + 8\\,\\text{CO} \\xrightarrow{250\\text{ atm},\\, 150^\\circ\\text{C}} \\text{Co}_2(\\text{CO})_8 + 2\\,\\text{CO}_2 + 2\\,\\text{H}_2\\text{O} \\]
   \\[ \\text{WCl}_6 + 6\\,\\text{CO} + 2\\,\\text{AlEt}_3 \\longrightarrow \\text{W}(\\text{CO})_6 + 2\\,\\text{AlCl}_3 + 3\\,\\text{C}_4\\text{H}_{10} \\]
3. **Photochemical and Thermal Substitution**: Carbon monoxide dissociates photochemically via metal-to-ligand charge transfer (MLCT) or ligand-field excitation, generating coordination-unsaturated intermediates that capture incoming ligands ($L = PR_3$, alkene, solvent):
   \\[ \\text{Cr}(\\text{CO})_6 \\xrightarrow{h\\nu} [\\text{Cr}(\\text{CO})_5] + \\text{CO} \\uparrow \\xrightarrow{L} \\text{Cr}(\\text{CO})_5 L \\]
   \\[ 2\\,\\text{Fe}(\\text{CO})_5 \\xrightarrow{h\\nu, \\text{ glacial acetic acid}} \\text{Fe}_2(\\text{CO})_9 \\downarrow + \\text{CO} \\uparrow \\]"""
        },
        {
            "id": "sec3_2",
            "title": "§3.2 The Dewar-Chatt-Duncanson Bonding Model in Metal Carbonyls",
            "content": """The bonding between a transition metal and carbon monoxide is governed by the synergistic **Dewar-Chatt-Duncanson (DCD) model**, comprising two complementary components:

1. **$\\sigma$-Donation**:
   - The carbon monoxide molecule possesses a filled non-bonding orbital centered primarily on carbon: the $5\\sigma$ molecular orbital (HOMO of CO, possessing weakly antibonding character with respect to the $C-O$ bond).
   - The lone pair in this $5\\sigma$ orbital donates electron density into an empty metal valence orbital of matching $\\sigma$-symmetry (e.g., $d_{z^2}$, $d_{x^2-y^2}$, $s$, or $p$ hybrids):
     \\[ M \\xleftarrow{\\quad\\sigma\\quad} :\\text{C}\\equiv\\text{O} \\]
   - This $\\sigma$-donation polarizes charge toward the metal center, building negative charge on the metal.

2. **$\\pi$-Backbonding ($\\pi$-Backdonation)**:
   - Carbon monoxide possesses two degenerate, empty, low-lying antibonding $\\pi^*$ orbitals: the $2\\pi^*$ molecular orbitals (LUMO of CO).
   - Filled metal valence $d$-orbitals of appropriate $\\pi$-symmetry ($d_{xy}, d_{yz}, d_{xz}$ or $t_{2g}$ in $O_h$) overlap with these empty $2\\pi^*$ orbitals:
     \\[ M \\xrightarrow{\\quad\\pi\\quad} \\text{C}\\equiv\\text{O} \\]
   - Electrons from the metal are backdonated into the ligand $\\pi^*$ LUMO.

### Synergism and Bond Order Consequences:
- $\\sigma$-donation transfers electron density to the metal, increasing the metal's basicity and enhancing its ability to backdonate.
- $\\pi$-backdonation relieves metal electron excess, increasing the Lewis acidity of the metal and facilitating further $\\sigma$-donation.
- **Effect on $M-C$ Bond**: $\\pi$-backbonding increases the $M-C$ bond order toward a double bond ($M=C=\\text{O}$), shortening the $M-C$ distance and strengthening the $M-C$ bond.
- **Effect on $C-O$ Bond**: Populating the $C-O$ antibonding $2\\pi^*$ orbital decreases the $C-O$ bond order from a formal triple bond toward a double bond, lengthening the $C-O$ bond distance and lowering its vibrational stretching frequency $\\nu(CO)$."""
        },
        {
            "id": "sec3_3",
            "title": "§3.3 Infrared Spectroscopy of Carbonyls: $\\nu(CO)$ Vibrational Modes & Cotton-Kraihanzel Force Constants",
            "content": """Infrared (IR) spectroscopy is the most sensitive diagnostic tool for probing the electronic environment of metal carbonyls. The vibrational stretching frequency of free gaseous carbon monoxide is:
\\[ \\nu(CO)_\\text{free} = 2143\\text{ cm}^{-1} \\]

### Electronic Effects of Metal Oxidation State and Charge:
When backbonding increases, electron density in $\\pi^*$ increases, lowering the force constant $k_{CO}$ according to Hooke's Law:
\\[ \\nu = \\frac{1}{2\\pi c} \\sqrt{\\frac{k}{\\mu}} \\]
where $\\mu = \\frac{m_C m_O}{m_C + m_O}$ is the reduced mass.
Consider the isoelectronic hexacarbonyl series ($d^6$ octahedral):
- $[\\text{Mn}(\\text{CO})_6]^+$: $\\nu(CO) = 2090\\text{ cm}^{-1}$ (positive charge contracts $d$-orbitals; weak backbonding)
- $\\text{Cr}(\\text{CO})_6$: $\\nu(CO) = 2000\\text{ cm}^{-1}$ (neutral; balanced $\\sigma$-donation and $\\pi$-backbonding)
- $[\\text{V}(\\text{CO})_6]^-$: $\\nu(CO) = 1860\\text{ cm}^{-1}$ (negative charge expands $d$-orbitals; strong backbonding)
- $[\\text{Ti}(\\text{CO})_6]^{2-}$: $\\nu(CO) = 1750\\text{ cm}^{-1}$ (enormous backbonding; $C-O$ bond approaches double bond)

### Bridging vs. Terminal Carbonyl Coordination Modes:
As carbon monoxide coordinates to more metal centers, each additional metal contributes $\\pi$-backbonding density into the same $2\\pi^*$ LUMO:
- **Terminal $M-\\text{CO}$**: $\\nu(CO) = 2125 - 1850\\text{ cm}^{-1}$
- **Doubly Bridging $\\mu_2-\\text{CO}$**: $\\nu(CO) = 1850 - 1750\\text{ cm}^{-1}$ (ketonic stretch)
- **Triply Bridging $\\mu_3-\\text{CO}$**: $\\nu(CO) = 1730 - 1620\\text{ cm}^{-1}$
- **Four-fold Bridging $\\mu_4-\\text{CO}$**: $\\nu(CO) < 1600\\text{ cm}^{-1}$

### Cotton-Kraihanzel Force Field:
Under the Cotton-Kraihanzel approximation, carbonyl stretching frequencies are modeled by secular equations factoring in the primary $C-O$ stretching force constant $k$ and the interaction force constants $k_c$ (cis-interaction) and $k_t$ (trans-interaction) transmitted through the metal $d$-orbitals."""
        },
        {
            "id": "sec3_4",
            "title": "§3.4 Metal Nitrosyl Complexes: Linear ($\text{NO}^+$) vs. Bent ($\text{NO}^-$) Coordination",
            "content": """Nitric oxide ($\\text{NO}$) is an open-shell radical possessing 15 valence electrons with an unpaired electron residing in its $2\\pi^*$ orbital. Upon binding transition metals, it adopts two distinct, interconvertible coordination geometries:

### 1. Linear Nitrosyl ($M-\\text{N}\\equiv\\text{O}$, angle $\\approx 180^\\circ$):
- **Formalism**: Nitrosyl is formally treated as nitrosonium cation $\\text{NO}^+$ (isoelectronic with $\\text{CO}$, 14 valence electrons).
- **Electron Counting**:
  - In the Covalent Model, linear $\\text{NO}$ is counted as a **3-electron donor** ($LX$-type: 1 electron from radical pairing plus 2 electrons from the nitrogen lone pair).
  - In the Ionic Model, $\\text{NO}^+$ is a **2-electron donor**, and the metal oxidation state is reduced by 1.
- **Bonding**: $sp$ hybridization at nitrogen. One $\\sigma$-dative bond from nitrogen to metal and two degenerate $\\pi$-backbonds from metal $d_{xz}, d_{yz}$ into $\\text{NO}$ $\\pi^*$ orbitals.
- **IR Spectroscopy**: $\\nu(NO) = 1650 - 1900\\text{ cm}^{-1}$ (high stretching frequency due to triple bond character).

### 2. Bent Nitrosyl ($M-\\text{N}=\\text{O}$, angle $\\approx 120^\\circ - 140^\\circ$):
- **Formalism**: Nitrosyl is formally treated as nitroxyl anion $\\text{NO}^-$ (16 valence electrons).
- **Electron Counting**:
  - In the Covalent Model, bent $\\text{NO}$ is counted as a **1-electron donor** ($X$-type: radical single bond).
  - In the Ionic Model, $\\text{NO}^-$ is a **2-electron donor**, but the metal formal oxidation state increases by 1.
- **Bonding**: $sp^2$ hybridization at nitrogen with a localized lone pair residing in the non-bonding $sp^2$ hybrid orbital, causing the bent geometry.
- **IR Spectroscopy**: $\\nu(NO) = 1525 - 1690\\text{ cm}^{-1}$ (lower stretching frequency due to formal double bond).

### The Enemark-Feltham Notation $\{M(\\text{NO})_x\}^n$:
Because assigning formal oxidation states to non-innocent nitrosyl ligands is ambiguous, Enemark and Feltham introduced the notation $\{M(\\text{NO})_x\}^n$, where $n$ is the total number of electrons in the metal $d$-orbitals plus the $\\text{NO}$ $\\pi^*$ orbitals:
\\[ n = d^\\text{electrons} + \\text{electrons in } \\pi^*(\\text{NO}) \\]
For example, in the nitroprusside anion $[\\text{Fe}(\\text{CN})_5(\\text{NO})]^{2-}$, the system is classified as $\{Fe(\\text{NO})\}^6$, adopting an idealized linear geometry."""
        },
        {
            "id": "sec3_5",
            "title": "§3.5 Phosphine Ligands: Electronic Properties, $\\sigma$-Donation and $\\pi$-Acceptance into $\\sigma^*$ Orbitals",
            "content": """Tertiary phosphines ($PR_3$) are premier spectator ligands in homogeneous catalysis, offering exceptional electronic and steric tuneability.

### Dual Bonding Mechanism:
1. **$\\sigma$-Donation**:
   - The phosphorus atom possesses a lone pair residing in an $sp^3$-like hybrid orbital with substantial $3s$ and $3p$ character.
   - This lone pair donates into an empty metal valence orbital, forming a strong $M-P$ $\\sigma$-bond.
   - $\\sigma$-donor strength depends on the electron-donating capability of the $R$ substituents:
     \\[ P(t\\text{-Bu})_3 > \\text{PMe}_3 > \\text{PPh}_3 > \\text{P(OMe)}_3 > \\text{P(OPh)}_3 > \\text{PF}_3 \\]
2. **$\\pi$-Acceptor Capability**:
   - Early models attributed $\\pi$-acceptance in phosphines to vacant, high-energy phosphorus $3d$ orbitals.
   - Modern molecular orbital calculations (Orpen, Connelly, Marynick) reveal that $\\pi$-acceptance occurs via backdonation from filled metal $d$-orbitals into **empty $\\sigma^*(P-R)$ antibonding orbitals** of the phosphine:
     \\[ d_\\pi(M) \\longrightarrow \\sigma^*(P-R) \\]
   - When $R$ is highly electronegative (e.g., $F, OPh, CF_3$), the $\\sigma^*(P-R)$ orbital is stabilized to lower energy and polarized toward phosphorus, maximizing overlap with metal $d$-orbitals.
   - Remarkably, phosphorus trifluoride ($\\text{PF}_3$) is such a potent $\\pi$-acceptor that its bonding properties and electronic spectrum closely match those of carbon monoxide ($CO$)."""
        },
        {
            "id": "sec3_6",
            "title": "§3.6 Tolman Steric Parameter (Cone Angle $\\theta$) and Electronic Parameter (TEP $\chi$)",
            "content": """Chadwick A. Tolman established quantitative steric and electronic metrics that parameterized phosphine behavior across organometallic chemistry.

### Tolman Cone Angle ($\\theta$):
The **Tolman cone angle** measures ligand steric bulk. It is defined as the vertex angle of a cylindrical cone centered at a metal atom situated at a standard distance of $2.28$ Å from the phosphorus atom, whose perimeter encloses the van der Waals radii of all atoms of the three $R$ substituents.
For unsymmetrical phosphines $P R_1 R_2 R_3$:
\\[ \\theta = \\frac{2}{3} \\sum_{i=1}^3 \\frac{\\theta_i}{2} \\]
Representative Cone Angles:
- $\\text{PH}_3$: $87^\\circ$
- $\\text{PF}_3$: $104^\\circ$
- $\\text{PMe}_3$: $118^\\circ$
- $\\text{PEt}_3$: $132^\\circ$
- $\\text{PPh}_3$: $145^\\circ$
- $\\text{P}(i\\text{-Pr})_3$: $160^\\circ$
- $\\text{PCy}_3$: $170^\\circ$
- $\\text{P}(t\\text{-Bu})_3$: $182^\\circ$
- $\\text{P}(o\\text{-tolyl})_3$: $194^\\circ$

### Tolman Electronic Parameter (TEP, $\\chi$):
The electronic donating ability of a phosphine is quantified by measuring the symmetric $A_1$ carbonyl stretching frequency $\\nu(CO)$ in the standard nickel complex $\\text{Ni}(\\text{CO})_3(PR_3)$:
\\[ \\nu(CO)_{A_1} = 2056.1 + \\sum_{i=1}^3 \\chi_i \\quad (\\text{cm}^{-1}) \\]
where $\\chi_i$ is the substituent electronic contribution (defined with $\\chi = 0$ for $t\\text{-Bu}$).
- Electron-rich phosphines (e.g., $\\text{PMe}_3, \\text{P}(t\\text{-Bu})_3$) transfer more electron density to nickel, maximizing $\\pi$-backbonding into the three CO ligands and depressing $\\nu(CO)$ ($\\\\approx 2064\\text{ cm}^{-1}$).
- Poor donor/strong $\\pi$-acceptor phosphines (e.g., $\\text{PF}_3$) compete with CO for metal backdonation, shifting $\\nu(CO)$ to higher frequencies ($2111\\text{ cm}^{-1}$)."""
        },
        {
            "id": "sec3_7",
            "title": "§3.7 Chelating Diphosphines: Natural Bite Angle $\\beta_n$ and Catalytic Selectivity",
            "content": """Bidentate diphosphines ($R_2\\text{P}-\\text{Linker}-\\text{P}R_2$) bind metal centers in a chelating mode, enforcing a specific geometry.

### The Natural Bite Angle ($\\beta_n$):
Introduced by Piet van Leeuwen and Casey, the **natural bite angle ($\\beta_n$)** is defined by molecular mechanics computations as the preferred $P-M-P$ valence angle determined solely by the steric constraints of the diphosphine backbone, with a standard $M-P$ bond length (typically $2.315$ Å) and without electronic ligand field contributions.

Representative Diphosphines and Natural Bite Angles:
- **dppm** ($\text{Ph}_2\\text{PCH}_2\\text{PPh}_2$): $\\beta_n \\approx 72^\\circ$ (often forms bridging rather than chelating complexes)
- **dppe** ($\text{Ph}_2\\text{PCH}_2\\text{CH}_2\\text{PPh}_2$): $\\beta_n \\approx 85^\\circ$ (prefers octahedral and square planar geometries)
- **dppp** ($\text{Ph}_2\\text{P(CH}_2)_3\\text{PPh}_2$): $\\beta_n \\approx 91^\\circ$
- **dppb** ($\text{Ph}_2\\text{P(CH}_2)_4\\text{PPh}_2$): $\\beta_n \\approx 98^\\circ$
- **BINAP** ($2,2'$-bis(diphenylphosphino)-$1,1'$-binaphthyl): $\\beta_n \\approx 93^\\circ$ (chiral $C_2$-symmetric backbone for asymmetric catalysis)
- **dppf** ($1,1'$-bis(diphenylphosphino)ferrocene): $\\beta_n \\approx 99^\\circ$
- **Xantphos** (4,5-bis(diphenylphosphino)-9,9-dimethylxanthene): $\\beta_n \\approx 111^\\circ$

### Impact on Catalytic Rates and Regioselectivity:
1. **Reductive Elimination Acceleration**: A wide bite angle (e.g., Xantphos $\\beta_n \\approx 111^\\circ$) forces the two coupling organic groups closer together, compressing their dihedral angle and accelerating reductive elimination by factors exceeding $10^4$.
2. **Hydroformylation Regioselectivity**: In Rh-catalyzed hydroformylation of 1-alkenes, wide bite angle diphosphines force the two phosphorus atoms to occupy equatorial-equatorial ($ee$) positions in trigonal bipyramidal intermediates, steering the linear-to-branched aldehyde ratio ($l:b$) to $>50:1$."""
        },
        {
            "id": "sec3_8",
            "title": "§3.8 Chemical Reactivity: Nucleophilic Attack, Disproportionation & Collman's Reagent",
            "content": """Metal carbonyl complexes display rich chemical transformations driven by the polarity of coordinated CO:

### 1. Nucleophilic Attack on Coordinated Carbonyls:
Because $\\sigma$-donation and metal-to-ligand backbonding withdraw electron density from the carbonyl carbon atom, coordinated CO is electrophilic:
- **Hydroxide Attack (Water-Gas Shift Intermediate)**:
  \\[ [M-\\text{CO}] + \\text{OH}^- \\longrightarrow [M-\\text{COOH}]^- \\xrightarrow{-\\text{CO}_2} [M-\\text{H}]^- \\]
- **Organolithium Addition (Fischer Carbene Synthesis)**:
  \\[ \\text{Cr}(\\text{CO})_6 + \\text{MeLi} \\longrightarrow [(\\text{OC})_5\\text{Cr}-\\text{C}(=\\text{O})\\text{Me}]^- \\text{Li}^+ \\xrightarrow{[\\text{Me}_3\\text{O}]^+\\text{BF}_4^-} (\\text{OC})_5\\text{Cr}=\\text{C}(\\text{OMe})\\text{Me} \\]

### 2. Disproportionation with Hard Lewis Bases:
Reaction of metal carbonyls with hard, coordinating Lewis bases (e.g., pyridine, ammonia) induces valence disproportionation:
\\[ 3\\,\\text{Mn}_2(\\text{CO})_{10} + 12\\,\\text{py} \\longrightarrow 2\\,[\\text{Mn}(\\text{py})_6]^{2+} + 4\\,[\\text{Mn}(\\text{CO})_5]^- + 10\\,\\text{CO} \\uparrow \\]

### 3. Collman's Reagent: Disodium Tetracarbonylferrate:
Reduction of iron pentacarbonyl with sodium amalgam or sodium naphthalenide yields **Collman's reagent**:
\\[ \\text{Fe}(\\text{CO})_5 + 2\\,\\text{Na} \\xrightarrow{\\text{THF}} \\text{Na}_2[\\text{Fe}(\\text{CO})_4] + \\text{CO} \\uparrow \\]
The ferrate dianion $[\\text{Fe}(\\text{CO})_4]^{2-}$ is a 'super-nucleophile' with an iron oxidation state of $-2$ ($d^{10}$, 18 valence electrons). It reacts cleanly with primary alkyl halides:
\\[ [\\text{Fe}(\\text{CO})_4]^{2-} + R-\\text{X} \\longrightarrow [R-\\text{Fe}(\\text{CO})_4]^- + \\text{X}^- \\xrightarrow{\\text{CO}} [R\\text{CO}-\\text{Fe}(\\text{CO})_4]^- \\xrightarrow{\\text{H}^+} R\\text{CHO} \\]
providing a versatile entry to aldehydes, unsymmetrical ketones, esters, and amides."""
        }
    ]

    problems = [
        {
            "id": "prob3_1",
            "tier": "Foundational",
            "title": "Isoelectronic Carbonyl Series and $\\nu(CO)$ Infrared Frequency Shifts",
            "statement": "The infrared carbonyl stretching frequencies for the octahedral $d^6$ hexacarbonyl series are: $[\\text{Ir}(\\text{CO})_6]^{3+} (2254\\text{ cm}^{-1})$, $[\\text{Os}(\\text{CO})_6]^{2+} (2190\\text{ cm}^{-1})$, $[\\text{Re}(\\text{CO})_6]^+ (2085\\text{ cm}^{-1})$, $\\text{W}(\\text{CO})_6 (1998\\text{ cm}^{-1})$, $[\\text{Ta}(\\text{CO})_6]^- (1850\\text{ cm}^{-1})$, $[\\text{Hf}(\\text{CO})_6]^{2-} (1750\\text{ cm}^{-1})$. (a) Explain the continuous decrease of $\\nu(CO)$ across this series using the Dewar-Chatt-Duncanson model. (b) Explain why $[\\text{Ir}(\\text{CO})_6]^{3+}$ exhibits a $\\nu(CO)$ higher than free gaseous CO ($2143\\text{ cm}^{-1}$) ('non-classical metal carbonyl').",
            "solution": """**Line-by-Line Solution:**

**(a) Physical Origin of Frequency Decrease Across the Series:**
- All species in the series are isoelectronic with an octahedral $d^6$ valence configuration ($t_{2g}^6$).
- As the net charge changes from $+3$ to $-2$:
  \\[ +3 \\longrightarrow +2 \\longrightarrow +1 \\longrightarrow 0 \\longrightarrow -1 \\longrightarrow -2 \\]
  the nuclear charge $Z$ decreases relative to the electron count, and the effective nuclear charge $Z_\\text{eff}$ experienced by the metal valence $d$-electrons decreases precipitously.
- A lower $Z_\\text{eff}$ causes radial expansion of the metal $d_{xy}, d_{yz}, d_{xz}$ ($t_{2g}$) orbitals, raising their energy levels closer to the empty $2\\pi^*$ LUMO of the coordinated carbon monoxide ligands.
- Consequently, metal-to-ligand $\\pi$-backbonding increases enormously:
  \\[ d_\\pi(M) \\xrightarrow{\\text{intense overlap}} \\pi^*(\\text{CO}) \\]
- Population of the $C-O$ antibonding $2\\pi^*$ orbital weakens the carbon-oxygen bond, reducing the $C-O$ bond order and force constant $k_{CO}$.
- According to Hooke's Law:
  \\[ \\nu(CO) = \\frac{1}{2\\pi c} \\sqrt{\\frac{k_{CO}}{\\mu}} \\]
  A lower force constant $k_{CO}$ produces a continuous decrease in $\\nu(CO)$ from $2254\\text{ cm}^{-1}$ down to $1750\\text{ cm}^{-1}$.

**(b) The 'Non-Classical Carbonyl' Phenomenon in $[\\text{Ir}(\\text{CO})_6]^{3+}$:**
- In $[\\text{Ir}(\\text{CO})_6]^{3+}$, the high $+3$ positive charge contracts the iridium $5d$ orbitals so tightly that their energetic match and spatial overlap with CO $2\\pi^*$ are virtually eliminated.
- Consequently, **$\\pi$-backbonding is essentially zero**.
- Bonding consists almost purely of **$\\sigma$-donation** from the $5\\sigma$ HOMO of CO into empty iridium valence orbitals.
- The $5\\sigma$ orbital of carbon monoxide is weakly **antibonding** with respect to the $C-O$ bond (due to polarization toward carbon).
- Donating electron density *out* of this weakly antibonding $5\\sigma$ orbital depopulates antibonding character, slightly strengthening and shortening the $C-O$ bond!
- Furthermore, the strong electric field generated by the tricationic metal center polarizes the $C-O$ electron cloud (electrostatic Stark effect), increasing the force constant $k_{CO}$.
- Therefore, $k_{CO}$ exceeds that of free CO, shifting $\\nu(CO)$ to $2254\\text{ cm}^{-1}$ ($+111\\text{ cm}^{-1}$ above free CO)."""
        },
        {
            "id": "prob3_2",
            "tier": "Foundational",
            "title": "Group Theoretical Prediction of IR-Active Modes in Carbonyl Isomers",
            "statement": "Determine the number of IR-active carbonyl stretching bands for: (a) Octahedral hexacarbonyl $\\text{Cr}(\\text{CO})_6$ ($O_h$ symmetry), (b) *trans*-dicarbonyl complex *trans*-$M(\\text{CO})_2 L_4$ ($D_{4h}$ symmetry), (c) *cis*-dicarbonyl complex *cis*-$M(\\text{CO})_2 L_4$ ($C_{2v}$ symmetry). Use symmetry group representations.",
            "solution": """**Line-by-Line Solution:**

**(a) Chromium Hexacarbonyl $\\text{Cr}(\\text{CO})_6$ ($O_h$ Symmetry):**
1. Define a basis of six $C-O$ stretch vectors $\\Gamma_{CO}$:
   \\[ \\Gamma_{CO}(E) = 6, \\quad \\Gamma_{CO}(C_3) = 0, \\quad \\Gamma_{CO}(C_2) = 0, \\quad \\Gamma_{CO}(C_4) = 2, \\quad \\Gamma_{CO}(C_2') = 0 \\]
   \\[ \\Gamma_{CO}(i) = 0, \\quad \\Gamma_{CO}(S_4) = 0, \\quad \\Gamma_{CO}(S_6) = 0, \\quad \\Gamma_{CO}(\\sigma_h) = 4, \\quad \\Gamma_{CO}(\\sigma_d) = 2 \\]
2. Reducing $\\Gamma_{CO}$ into irreducible representations of $O_h$:
   \\[ \\Gamma_{CO} = A_{1g} + E_g + T_{1u} \\]
3. Selection Rules for IR Activity:
   - In $O_h$, electric dipole moments transform as the Cartesian coordinates $(x,y,z)$, which span the $T_{1u}$ representation.
   - $A_{1g}$ and $E_g$ have gerade ($g$) symmetry and are IR-inactive (centrosymmetric rule of mutual exclusion).
   - Only $T_{1u}$ is ungerade ($u$) and IR-active.
- **Result**: Exactly **one IR-active band** ($T_{1u}$).

**(b) *trans*-$M(\\text{CO})_2 L_4$ ($D_{4h}$ Symmetry):**
1. The two $C-O$ bond vectors lie collinear along the $z$-axis:
   \\[ \\Gamma_{CO} = A_{1g} + A_{2u} \\]
2. Selection Rules in $D_{4h}$:
   - Electric dipole $z$ transforms as $A_{2u}$.
   - $A_{1g}$ is symmetric stretching (no net dipole change, IR-inactive).
- **Result**: Exactly **one IR-active band** ($A_{2u}$, asymmetric stretch).

**(c) *cis*-$M(\\text{CO})_2 L_4$ ($C_{2v}$ Symmetry):**
1. The two $C-O$ bond vectors lie at $90^\\circ$ in the $xz$-plane:
   - Under $E$: both remain fixed $\\implies \\chi(E) = 2$.
   - Under $C_2(z)$: vectors swap $\\implies \\chi(C_2) = 0$.
   - Under $\\sigma_v(xz)$: both remain in plane $\\implies \\chi(\\sigma_v) = 2$.
   - Under $\\sigma_v'(yz)$: vectors swap $\\implies \\chi(\\sigma_v') = 0$.
2. Reducing $\\Gamma_{CO}$:
   \\[ \\Gamma_{CO} = A_1 + B_1 \\]
3. Selection Rules in $C_{2v}$:
   - $z$ transforms as $A_1$ (symmetric stretch, dipole along $z$, IR-active).
   - $x$ transforms as $B_1$ (asymmetric stretch, dipole along $x$, IR-active).
- **Result**: Exactly **two IR-active bands** ($A_1$ and $B_1$). This allows unambiguous spectroscopic differentiation between *cis* and *trans* isomers!"""
        },
        {
            "id": "prob3_3",
            "tier": "Foundational",
            "title": "Tolman Cone Angles and Steric Crowding Calculations",
            "statement": "Rank the following tertiary phosphines in order of increasing Tolman cone angle ($\\theta$): $\\text{PMe}_3, \\text{P}(t\\text{-Bu})_3, \\text{PPh}_3, \\text{PF}_3, \\text{P}(i\\text{-Pr})_3, \\text{P}(o\\text{-tolyl})_3$. Explain why $\\text{P}(o\\text{-tolyl})_3$ has a significantly larger cone angle than $\\text{PPh}_3$ despite having the same aromatic core.",
            "solution": """**Line-by-Line Solution:**

**(a) Ranking of Tolman Cone Angles:**
Based on Chadwick Tolman's experimental measurements:
1. $\\text{PF}_3$: $\\theta = 104^\\circ$
2. $\\text{PMe}_3$: $\\theta = 118^\\circ$
3. $\\text{PPh}_3$: $\\theta = 145^\\circ$
4. $\\text{P}(i\\text{-Pr})_3$: $\\theta = 160^\\circ$
5. $\\text{P}(t\\text{-Bu})_3$: $\\theta = 182^\\circ$
6. $\\text{P}(o\\text{-tolyl})_3$: $\\theta = 194^\\circ$

Order of increasing steric bulk:
\\[ \\text{PF}_3 < \\text{PMe}_3 < \\text{PPh}_3 < \\text{P}(i\\text{-Pr})_3 < \\text{P}(t\\text{-Bu})_3 < \\text{P}(o\\text{-tolyl})_3 \\]

**(b) Steric Comparison Between $\\text{PPh}_3$ and $\\text{P}(o\\text{-tolyl})_3$:**
- Triphenylphosphine $\\text{PPh}_3$ contains three phenyl rings attached to phosphorus. In the coordinated complex, the phenyl rings can twist like propeller blades around the $P-\\text{C}_{ipso}$ bond to minimize steric interference with the metal coordination sphere, yielding an effective cone angle of $145^\\circ$.
- Tri($o$-tolyl)phosphine $\\text{P}(o\\text{-tolyl})_3$ contains a methyl substituent at the *ortho* position of each phenyl ring (adjacent to the coordinating carbon).
- The *ortho*-methyl groups severely hinder free rotation of the aromatic rings around the $P-\\text{C}_{ipso}$ bonds.
- To avoid steric clash between the three methyl groups, the rings are forced into a rigid, splayed conformation where the methyl groups project outward into the coordination sphere of the metal.
- This creates an enormous effective cone angle of **$194^\\circ$**, making $\\text{P}(o\\text{-tolyl})_3$ one of the bulkiest monophosphines, capable of enforcing low coordination numbers (e.g., forming 2-coordinate $\\text{PdL}_2$ complexes)."""
        },
        {
            "id": "prob3_4",
            "tier": "Intermediate",
            "title": "Cotton-Kraihanzel Force Constant Derivation for $cis$- and $trans$-$M(\\text{CO})_4 L_2$",
            "statement": "In the Cotton-Kraihanzel approximation for a *cis*-disubstituted octahedral tetracarbonyl complex *cis*-$M(\\text{CO})_4 L_2$ ($C_{2v}$ symmetry), four IR bands are observed: $A_1^{(1)}, A_1^{(2)}, B_1, B_2$. (a) Formulate the secular equations relating the observed vibrational frequencies to the axial force constant $k_1$, equatorial force constant $k_2$, and trans-interaction force constant $k_t$. (b) For *cis*-$[\\text{Mo}(\\text{CO})_4(\\text{PEt}_3)_2]$, the observed bands are $2015, 1915, 1895, 1880\\text{ cm}^{-1}$. Calculate the force constants $k_1$ and $k_2$.",
            "solution": """**Line-by-Line Solution:**

**(a) Secular Equations in Cotton-Kraihanzel Formulation:**
In *cis*-$M(\\text{CO})_4 L_2$:
- Two CO ligands lie trans to each other along the $z$-axis (axial CO, force constant $k_1$).
- Two CO ligands lie trans to the two $L$ ligands in the $xy$-plane (equatorial CO, force constant $k_2$).
- The trans interaction force constant between mutually trans CO ligands is $k_t$; the cis interaction force constant is $k_c$.

The symmetry coordinates yield four vibrational modes:
1. $B_1$ mode (asymmetric stretch of the two axial trans CO ligands):
   \\[ \\lambda(B_1) = \\mu (k_1 - k_t) \\]
2. $B_2$ mode (asymmetric stretch of the two equatorial CO ligands):
   \\[ \\lambda(B_2) = \\mu (k_2 - k_c) \\]
3. The two $A_1$ modes couple via the secular determinant:
   \\[ \\begin{vmatrix} \\mu(k_1 + k_t) - \\lambda & \\sqrt{2}\\,\\mu k_c \\\\ \\sqrt{2}\\,\\mu k_c & \\mu(k_2 + k_c) - \\lambda \\end{vmatrix} = 0 \\]
where $\\lambda = 4\\pi^2 c^2 \\nu^2$ and $\\mu = \\frac{m_C + m_O}{m_C m_O} = 1.144 \\times 10^{-26}\\text{ kg}^{-1}$. In energy units:
\\[ k = 4.040 \\times 10^{-6} \\nu^2 \\quad (\\text{mdyn/Å with } \\nu \\text{ in cm}^{-1}) \\]

**(b) Force Constant Calculation for *cis*-$[\\text{Mo}(\\text{CO})_4(\\text{PEt}_3)_2]$:**
Observed frequencies:
- $\\nu(A_1^{(1)}) = 2015\\text{ cm}^{-1}$
- $\\nu(B_1) = 1915\\text{ cm}^{-1}$
- $\\nu(A_1^{(2)}) = 1895\\text{ cm}^{-1}$
- $\\nu(B_2) = 1880\\text{ cm}^{-1}$

1. Compute parameter $\\lambda_i$:
   - $\\lambda(B_1) = 4.040 \\times 10^{-6} (1915)^2 = 4.040 \\times 10^{-6} (3.667 \\times 10^6) = 14.815\\text{ mdyn/Å}$
   - $\\lambda(B_2) = 4.040 \\times 10^{-6} (1880)^2 = 4.040 \\times 10^{-6} (3.534 \\times 10^6) = 14.279\\text{ mdyn/Å}$
   - $\\lambda(A_1^{(1)}) = 4.040 \\times 10^{-6} (2015)^2 = 16.403\\text{ mdyn/Å}$
   - $\\lambda(A_1^{(2)}) = 4.040 \\times 10^{-6} (1895)^2 = 14.508\\text{ mdyn/Å}$

2. Trans-interaction constant approximation:
   In metal carbonyls, Cotton and Kraihanzel observed empirically that $k_t \\approx 2 k_c \\approx 0.60-0.75\\text{ mdyn/Å}$.
   Using trace theorem for the $A_1$ secular matrix:
   \\[ \\lambda(A_1^{(1)}) + \\lambda(A_1^{(2)}) = (k_1 + k_t) + (k_2 + k_c) \\]
   Sum: $16.403 + 14.508 = 30.911\\text{ mdyn/Å}$.
   From $B_1$: $k_1 - k_t = 14.815 \\implies k_1 = 14.815 + k_t$.
   Substituting into $(k_1 + k_t)$: $(14.815 + 2k_t)$.
   With standard $k_t \\approx 0.65\\text{ mdyn/Å}$ and $k_c \\approx 0.35\\text{ mdyn/Å}$:
   \\[ k_1 = 14.815 + 0.65 = 15.47\\text{ mdyn/Å} \\]
   \\[ k_2 = 14.279 + 0.35 = 14.63\\text{ mdyn/Å} \\]
- **Physical Interpretation**: $k_1 > k_2$ ($15.47$ vs $14.63\\text{ mdyn/Å}$) reveals that the equatorial CO ligands (trans to the strongly electron-donating $\\text{PEt}_3$ phosphines) receive substantially greater $\\pi$-backdonation from molybdenum than the axial CO ligands (trans to each other), weakening their force constant by $0.84\\text{ mdyn/Å}$."""
        },
        {
            "id": "prob3_5",
            "tier": "Intermediate",
            "title": "Electronic and Structural Ambiguity in Metal Nitrosyl Complexes",
            "statement": "Consider the brown-ring complex $[\\text{Fe}(\\text{H}_2\\text{O})_5(\\text{NO})]^{2+}$. (a) Calculate the Enemark-Feltham notation $\{M(\\text{NO})_x\}^n$ for this species. (b) The complex displays an effective magnetic moment $\\mu_{eff} = 3.90\\ \\mu_B$, and its $\\nu(NO)$ stretch appears at $1780\\text{ cm}^{-1}$. Reconcile these experimental observations with the formal oxidation states $\\text{Fe}(\\text{I})-\\text{NO}^+$ versus $\\text{Fe}(\\text{III})-\\text{NO}^-$.",
            "solution": """**Line-by-Line Solution:**

**(a) Enemark-Feltham Notation:**
- The metal is iron (Group 8, 8 valence electrons).
- Five neutral water ligands: $\\text{H}_2\\text{O}$.
- Net complex charge: $+2$.
- The Enemark-Feltham formula is $\{M(\\text{NO})_x\}^n$ where $n = n_v(M) - q + \\text{electrons in } \\pi^*(\\text{NO})$.
- For iron ($n_v = 8$) with charge $+2$:
  \\[ n = 8 - 2 + 1 = 7 \\]
- **Notation**: **$\\{\\text{Fe}(\\text{NO})\\}^7$**.

**(b) Reconciling Experimental Magnetic and Spectroscopic Data:**
1. **Magnetic Moment Interpretation**:
   - $\\mu_{eff} = 3.90\\ \\mu_B$.
   - The spin-only magnetic moment formula is $\\mu_{so} = \\sqrt{n(n+2)}\\,\\mu_B$.
   - For $n=3$ unpaired electrons: $\\mu_{so} = \\sqrt{3(5)} = \\sqrt{15} \\approx 3.87\\ \\mu_B$.
   - The observed moment of $3.90\\ \\mu_B$ unequivocally corresponds to **$S = 3/2$ (three unpaired electrons)**.
2. **Analysis of the Competing Formalisms**:
   - **Hypothesis 1: $\\text{Fe}(\\text{I})-\\text{NO}^+$**:
     - $\\text{Fe}(\\text{I})$ has a $d^7$ configuration. In a high-spin octahedral weak water field, $t_{2g}^5 e_g^2$ gives $S = 3/2$ (three unpaired electrons).
     - $\\text{NO}^+$ is a closed-shell diamagnetic ligand ($S=0$).
     - The high $\\nu(NO) = 1780\\text{ cm}^{-1}$ indicates significant triple bond character, consistent with linear $\\text{NO}^+$.
   - **Hypothesis 2: $\\text{Fe}(\\text{III})-\\text{NO}^-$**:
     - $\\text{Fe}(\\text{III})$ has a $d^5$ configuration ($S=5/2$, five unpaired electrons in high-spin).
     - $\\text{NO}^-$ has a triplet ground state ($S=1$, two unpaired electrons in $\\pi^*$).
     - Strong antiferromagnetic coupling between the high-spin $\\text{Fe}(\\text{III})$ ($S=5/2$) and the triplet $\\text{NO}^-$ ($S=1$) results in a net spin:
       \\[ S_\\text{total} = \\frac{5}{2} - 1 = \\frac{3}{2} \\]
3. **Mössbauer Spectroscopy and Modern DFT Resolution**:
   - $^{57}\\text{Fe}$ Mössbauer isomer shifts ($\\delta \\approx 0.72\\text{ mm/s}$) show that the electron density at the iron nucleus matches high-spin $\\text{Fe}(\\text{III})$ ($S_1 = 5/2$) antiferromagnetically coupled to an $\\text{NO}^-$ radical anion ($S_2 = 1$).
   - Thus, the physical ground state is best described as high-spin $\\text{Fe}(\\text{III})$ antiferromagnetically exchange-coupled to $\\text{NO}^-$, while historically formulated as $\\text{Fe}(\\text{I})-\\text{NO}^+$."""
        },
        {
            "id": "prob3_6",
            "tier": "Intermediate",
            "title": "Natural Bite Angle Influence on Reductive Elimination Kinetics",
            "statement": "In the reductive elimination of ethane from diphosphine complexes $[(\\text{diphosphine})\\text{Pd}(\\text{CH}_3)_2]$, the relative reaction rates at $25^\\circ\\text{C}$ vary dramatically with the diphosphine backbone: (a) dppm ($\\beta_n = 72^\\circ$): relative rate $= 1$; (b) dppe ($\\beta_n = 85^\\circ$): relative rate $= 10^2$; (c) dppf ($\\beta_n = 99^\\circ$): relative rate $= 6 \\times 10^4$; (d) Xantphos ($\\beta_n = 111^\\circ$): relative rate $= 4 \\times 10^7$. Explain the physical and orbital origins of this $10^7$-fold rate enhancement.",
            "solution": """**Line-by-Line Solution:**

**(a) Geometric Ground-State Destabilization:**
- In the square planar reactant $[(\\text{diphosphine})\\text{Pd}(\\text{CH}_3)_2]$, the ideal unconstrained valence angle around the $d^8$ $\\text{Pd}(\\text{II})$ center is $90^\\circ$.
- The total angular span in the coordination plane must sum to $360^\\circ$:
  \\[ \\angle(P-\\text{Pd}-P) + \\angle(C-\\text{Pd}-C) + 2\\,\\angle(P-\\text{Pd}-C) = 360^\\circ \\]
- When a diphosphine with a wide natural bite angle (e.g., Xantphos, $\\beta_n = 111^\\circ$) is coordinated:
  1. The $P-\\text{Pd}-P$ angle is forced open from $90^\\circ$ to $>105^\\circ$.
  2. This widening exerts a mechanical scissors action on the coordination sphere, compressing the opposite methyl-palladium-methyl angle $\\angle(C-\\text{Pd}-C)$ from $90^\\circ$ down to $<80^\\circ$.
  3. Bringing the two methyl carbons into closer spatial proximity substantially raises the ground-state steric and electronic energy of the reactant, pre-organizing it toward the transition state.

**(b) Frontier Molecular Orbital Overlap in the Transition State:**
- Reductive elimination of ethane ($\text{H}_3\\text{C}-\\text{CH}_3$) requires direct orbital overlap between the two filled $\\sigma(\\text{Pd}-\\text{C})$ bonding orbitals:
  \\[ \\text{HOMO} = c_1 \\sigma_1 + c_2 \\sigma_2 \\]
- As the $C-\\text{Pd}-C$ angle $\\alpha$ decreases toward zero, the spatial overlap integral $S_{CC}$ between the $sp^3$ hybrid orbitals on the two methyl carbons increases exponentially:
  \\[ S_{CC}(\\alpha) \\propto \\exp(-R_{CC} / a_0) \\]
- Simultaneously, widening the $P-\\text{Pd}-P$ bite angle raises the energy of the occupied metal $d_{x^2-y^2}$ and $d_{xy}$ orbitals, facilitating the required two-electron transfer from the $Pd-C$ bonds back into a non-bonding metal $d$-orbital ($\text{Pd}(\\text{II}) \\to \\text{Pd}(0)$).

**(c) Activation Free Energy Reduction:**
- The activation barrier $\\Delta G^\\ddagger$ is the difference between transition state energy and ground state energy:
  \\[ \\Delta G^\\ddagger = G_{TS} - G_{GS} \\]
- Wide bite angle diphosphines simultaneously raise $G_{GS}$ (via ground-state steric strain) and lower $G_{TS}$ (via superior orbital overlap), drastically lowering $\\Delta G^\\ddagger$:
  \\[ \\Delta\\Delta G^\\ddagger = RT \\ln(4 \\times 10^7) = (8.314)(298) \\ln(4 \\times 10^7) \\approx (2478)(17.5) \\approx 43.4\\text{ kJ/mol} \\]
- A reduction of $43.4\\text{ kJ/mol}$ in activation barrier accelerates the reaction by over seven orders of magnitude ($4 \\times 10^7$)."""
        },
        {
            "id": "prob3_7",
            "tier": "Advanced",
            "title": "Quantitative Tolman Electronic Parameter (TEP) Derivation and Carbonyl Coupling",
            "statement": "The symmetric $A_1$ stretching frequency of $\\text{Ni}(\\text{CO})_3 L$ complexes defines the Tolman Electronic Parameter. (a) For $L = \\text{P}(t\\text{-Bu})_3$, $\\nu(CO) = 2056.1\\text{ cm}^{-1}$; for $L = \\text{PMe}_3$, $\\nu(CO) = 2064.1\\text{ cm}^{-1}$; for $L = \\text{PPh}_3$, $\\nu(CO) = 2068.9\\text{ cm}^{-1}$; for $L = \\text{PF}_3$, $\\nu(CO) = 2110.8\\text{ cm}^{-1}$. Calculate the Tolman $\\chi$ parameters for methyl, phenyl, and fluoro substituents. (b) Using second-order perturbation theory, derive the mathematical relationship between the energy of the phosphorus $\\sigma^*(P-R)$ LUMO and the shift in $\\nu(CO)$.",
            "solution": """**Line-by-Line Solution:**

**(a) Calculation of Tolman $\\chi$ Parameters:**
Tolman's formula expresses the $A_1$ frequency of $\\text{Ni}(\\text{CO})_3(P R_1 R_2 R_3)$ as:
\\[ \\nu(CO) = 2056.1 + \\sum_{i=1}^3 \\chi_i \\quad (\\text{cm}^{-1}) \\]
where $\\chi_i$ is the additive contribution of substituent $R_i$, with $\\chi(t\\text{-Bu}) = 0.0\\text{ cm}^{-1}$ by definition.

1. **For $\\text{PMe}_3$ ($R_1 = R_2 = R_3 = \\text{Me}$)**:
   \\[ 2064.1 = 2056.1 + 3\\,\\chi(\\text{Me}) \\]
   \\[ 3\\,\\chi(\\text{Me}) = 2064.1 - 2056.1 = 8.0\\text{ cm}^{-1} \\implies \\chi(\\text{Me}) = \\frac{8.0}{3} \\approx 2.67\\text{ cm}^{-1} \\]

2. **For $\\text{PPh}_3$ ($R_1 = R_2 = R_3 = \\text{Ph}$)**:
   \\[ 2068.9 = 2056.1 + 3\\,\\chi(\\text{Ph}) \\]
   \\[ 3\\,\\chi(\\text{Ph}) = 2068.9 - 2056.1 = 12.8\\text{ cm}^{-1} \\implies \\chi(\\text{Ph}) = \\frac{12.8}{3} \\approx 4.27\\text{ cm}^{-1} \\]

3. **For $\\text{PF}_3$ ($R_1 = R_2 = R_3 = \\text{F}$)**:
   \\[ 2110.8 = 2056.1 + 3\\,\\chi(\\text{F}) \\]
   \\[ 3\\,\\chi(\\text{F}) = 2110.8 - 2056.1 = 54.7\\text{ cm}^{-1} \\implies \\chi(\\text{F}) = \\frac{54.7}{3} \\approx 18.23\\text{ cm}^{-1} \\]

**(b) Perturbation Derivation Connecting $\\sigma^*(P-R)$ LUMO to $\\Delta\\nu(CO)$:**
1. Let $\\epsilon_d$ be the unperturbed energy of the nickel $d$-orbitals, and $\\epsilon_{\\sigma^*}$ be the energy of the phosphine $\\sigma^*(P-R)$ LUMO.
2. The interaction matrix element between metal $d$ and phosphine $\\sigma^*(P-R)$ is $H_{d\\sigma^*}$.
3. By second-order perturbation theory, the stabilization of the metal $d$-electrons due to $\\pi$-backdonation into the phosphine is:
   \\[ \\Delta E_d = -\\frac{|H_{d\\sigma^*}|^2}{\\epsilon_{\\sigma^*} - \\epsilon_d} \\]
4. Lowering the metal $d$-orbital energy by $\\Delta E_d$ decreases the energy match and overlap with the higher-lying CO $2\\pi^*$ LUMO (energy $\\epsilon_{\\pi^*(CO)}$).
5. The fraction of electron density backdonated from nickel into the three CO ligands is proportional to:
   \\[ \\rho_{\\pi^*(CO)} \\approx \\frac{|H_{d\\pi^*}|^2}{\\epsilon_{\\pi^*(CO)} - (\\epsilon_d + \\Delta E_d)} \\approx \\rho_0 \\left(1 - \\frac{|H_{d\\sigma^*}|^2}{(\\epsilon_{\\pi^*(CO)} - \\epsilon_d)(\\epsilon_{\\sigma^*} - \\epsilon_d)}\\right) \\]
6. Because the force constant $k_{CO}$ increases linearly with the decrease in CO $\\pi^*$ population ($k_{CO} = k_0 - C \\rho_{\\pi^*(CO)}$):
   \\[ \\Delta k_{CO} = + C' \\frac{|H_{d\\sigma^*}|^2}{\\epsilon_{\\sigma^*} - \\epsilon_d} \\]
7. Since $\\Delta \\nu \\approx \\frac{\\Delta k_{CO}}{2\\mu \\nu_0}$:
   \\[ \\Delta \\nu(CO) \\propto \\frac{1}{\\epsilon_{\\sigma^*} - \\epsilon_d} \\]
   When electronegative substituents like fluorine lower the energy $\\epsilon_{\\sigma^*}$, the denominator $\\epsilon_{\\sigma^*} - \\epsilon_d$ decreases sharply, causing $\\Delta \\nu(CO)$ to shift to higher wavenumbers."""
        },
        {
            "id": "prob3_8",
            "tier": "Advanced",
            "title": "Synthesis, Mechanism and Organic Transformations of Collman's Reagent",
            "statement": "Disodium tetracarbonylferrate $\\text{Na}_2[\\text{Fe}(\\text{CO})_4]$ reacts with an alkyl halide $R\\text{Br}$ to yield an alkyliron intermediate (A), which upon treatment with triphenylphosphine $\\text{PPh}_3$ converts to an acyliron intermediate (B). Subsequent reaction of (B) with molecular oxygen followed by acidic quench yields a carboxylic acid $R\\text{COOH}$. (a) Determine the formal oxidation state and electron count of iron in $\\text{Na}_2[\\text{Fe}(\\text{CO})_4]$, (A), and (B). (b) Formulate the detailed mechanism for the conversion of (A) to (B), and explain why this is a migratory insertion rather than direct CO addition. (c) Derive why $\\text{Na}_2[\\text{Fe}(\\text{CO})_4]$ is termed a 'super-nucleophile' by evaluating its Pearson Hard-Soft Acid-Base (HSAB) parameters.",
            "solution": """**Line-by-Line Solution:**

**(a) Formal Oxidation State and Electron Count:**
1. **Collman's Reagent $\\text{Na}_2[\\text{Fe}(\\text{CO})_4]$**:
   - CO ligands are neutral ($L_4$). Net charge of dianion is $-2$.
   \\[ OS(\\text{Fe}) = -2 - 0 = -2 \\implies \\text{Fe}(-\\text{II}) \\]
   - Iron is Group 8: $d$-electron count $= 8 - (-2) = 10 \\implies d^{10}$.
   - Total valence electron count: $10 + 4(2) = 18\\text{ electrons}$ (tetrahedral $T_d$).
2. **Alkyliron Intermediate (A) $[R-\\text{Fe}(\\text{CO})_4]^-$**:
   - Alkyl group is an $X$-ligand (formal charge $-1$). Net charge is $-1$.
   \\[ OS(\\text{Fe}) = -1 - (-1) = 0 \\implies \\text{Fe}(0) \\implies d^8 \\]
   - Total valence electron count: $8 + 1 + 4(2) = 17$? No:
     - Neutral model: Fe(8) + R(1) + 4 CO(8) + charge(1) $= 18\\text{ electrons}$ (trigonal bipyramidal $D_{3h}$).
3. **Acyliron Intermediate (B) $[R\\text{CO}-\\text{Fe}(\\text{CO})_3(\\text{PPh}_3)]^-$**:
   - Acyl group $R\\text{CO}$ is an $X$-ligand ($-1$).
   - Three CO ligands ($L_3$) and one $\\text{PPh}_3$ ($L$).
   - Fe oxidation state: $OS = 0 \\implies d^8$.
   - Valence electrons: $8 (\\text{Fe}) + 1 (\\text{acyl}) + 6 (3\\text{CO}) + 2 (\\text{PPh}_3) + 1 (\\text{charge}) = 18\\text{ electrons}$.

**(b) Mechanism of Migratory Insertion ((A) to (B)):**
1. In $[R-\\text{Fe}(\\text{CO})_4]^-$, iron is an 18-electron saturated center. Incoming $\\text{PPh}_3$ cannot directly attack iron without violating the 18e rule.
2. The alkyl group $R$ migrates intramolecularly to the carbon atom of a mutually *cis* coordinated carbonyl ligand:
   \\[ [R-\\text{Fe}(\\text{CO})_4]^- \\xrightarrow{k_1} [(\\text{OC})_3\\text{Fe}-\\text{C}(=\\text{O})R]^- \\quad (16\\text{-electron acyl intermediate}) \\]
3. Migratory insertion generates a coordinatively unsaturated, 16-electron intermediate possessing a vacant coordination site.
4. The incoming triphenylphosphine ligand rapidly coordinates into this vacant site ($k_2 \\gg k_{-1}$):
   \\[ [(\\text{OC})_3\\text{Fe}-\\text{C}(=\\text{O})R]^- + \\text{PPh}_3 \\xrightarrow{k_2} [(\\text{Ph}_3\\text{P})(\\text{OC})_3\\text{Fe}-\\text{C}(=\\text{O})R]^- \\]
5. $^{13}\\text{C}$-labeling experiments confirm that the carbonyl carbon of the newly formed acyl group originates exclusively from one of the original coordinated CO ligands, proving an intramolecular alkyl migration.

**(c) Super-Nucleophilicity and HSAB Analysis:**
- In $[\\text{Fe}(\\text{CO})_4]^{2-}$, iron carries a formal $-2$ oxidation state with a completely filled, spherical $d^{10}$ closed shell.
- Pearson's chemical hardness parameter is defined as:
  \\[ \\eta = \\frac{I - A}{2} \\]
  where $I$ is ionization potential and $A$ is electron affinity.
- The energy of the HOMO (highest occupied metal $d$-orbital) in $[\\text{Fe}(\\text{CO})_4]^{2-}$ is exceptionally high due to the double negative charge.
- The high polarizability and low ionization energy make $[\\text{Fe}(\\text{CO})_4]^{2-}$ an exceptionally **soft, highly polarizable Lewis base**.
- Its Swain-Scott nucleophilicity parameter $n$ exceeds $+14$ (many orders of magnitude greater than classical nucleophiles like iodide or hydroxide).
- Consequently, it undergoes rapid $S_N2$ oxidative addition with primary and secondary alkyl halides with clean inversion of configuration at carbon."""
        },
        {
            "id": "prob3_9",
            "tier": "Advanced",
            "title": "Fluxional Carbonyl Dynamics and Coalescence in $\\text{Fe}_3(\\text{CO})_{12}$",
            "statement": "Triiron dodecacarbonyl $\\text{Fe}_3(\\text{CO})_{12}$ possesses two bridging $\\mu_2-\\text{CO}$ ligands and ten terminal CO ligands in the solid state ($C_{2v}$ symmetry). In solution at room temperature, its $^{13}\\text{C}$ NMR spectrum displays a single sharp singlet down to $-150^\\circ\\text{C}$. (a) Calculate the total valence electron count ($TVE$) and the number of metal-metal bonds for $\\text{Fe}_3(\\text{CO})_{12}$. (b) Explain the 'concerted bridge-opening and closing' mechanism (Cotton dynamic merry-go-round model) that renders all twelve carbonyls chemically equivalent on the NMR timescale. (c) Estimate the upper limit for the activation barrier $\\Delta G^\\ddagger$ of this fluxional process at $-150^\\circ\\text{C}$.",
            "solution": """**Line-by-Line Solution:**

**(a) Total Valence Electron Count and Metal-Metal Bonding:**
1. Iron is in Group 8 ($n_v = 8$):
   \\[ 3 \\times \\text{Fe} = 3 \\times 8 = 24\\text{ valence electrons} \\]
2. Twelve CO ligands donate:
   \\[ 12 \\times 2 = 24\\text{ electrons} \\]
3. Total Valence Electrons ($TVE$):
   \\[ TVE = 24 + 24 = 48\\text{ electrons} \\]
4. Number of Metal-Metal bonds ($m$):
   \\[ m = \\frac{18n - TVE}{2} = \\frac{18(3) - 48}{2} = \\frac{54 - 48}{2} = \\frac{6}{2} = 3 \\]
- **Structure**: The three iron atoms form an equilateral or isosceles triangle containing **3 single $\\text{Fe}-\\text{Fe}$ bonds**.

**(b) Cotton 'Merry-Go-Round' Dynamic Fluxional Mechanism:**
1. In the solid state, one $\\text{Fe}-\\text{Fe}$ edge is bridged by two $\\mu_2-\\text{CO}$ ligands, while the other two iron atoms each carry three terminal CO ligands, and the unique Fe atoms each carry two terminal CO ligands, breaking overall $D_{3h}$ symmetry to $C_{2v}$.
2. In solution, the two bridging carbonyls open simultaneously to terminal positions:
   \\[ \\text{Bridged } C_{2v} \\rightleftharpoons \\text{Unbridged } D_{3h} \\text{ intermediate} \\rightleftharpoons \\text{Re-bridged } C_{2v}' \\]
3. In the unbridged $D_{3h}$ intermediate (analogous to $\\text{Ru}_3(\\text{CO})_{12}$ and $\\text{Os}_3(\\text{CO})_{12}$), all twelve CO ligands are terminal.
4. As the iron triangle rotates within the carbonyl envelope (or equivalently, as the carbonyls migrate along the triangular edges in a concerted 'merry-go-round' motion), pairs of carbonyls continuously open and close across different $\\text{Fe}-\\text{Fe}$ edges.
5. This permutation rapidly exchanges bridging and terminal environments, as well as axial and equatorial sites, averaging the magnetic environment across all twelve $^{13}\\text{C}$ nuclei.

**(c) Upper Limit of Activation Barrier $\\Delta G^\\ddagger$ at $-150^\\circ\\text{C}$:**
1. Temperature: $T = -150^\\circ\\text{C} = 123.15\\text{ K}$.
2. At $-150^\\circ\\text{C}$, the peak remains a single sharp resonance without broadening. This implies that the exchange rate $k$ is still well above the coalescence rate:
   \\[ k > k_c = \\frac{\\pi \\Delta \\nu}{\\sqrt{2}} \\]
   For a typical $^{13}\\text{C}$ chemical shift dispersion between bridging and terminal carbonyls of $\\Delta \\delta \\approx 50\\text{ ppm}$ at a $^{13}\\text{C}$ frequency of $100\\text{ MHz}$:
   \\[ \\Delta \\nu = 50 \\times 100 = 5000\\text{ Hz} \\]
   \\[ k_c = \\frac{\\pi(5000)}{\\sqrt{2}} \\approx 1.11 \\times 10^4\\text{ s}^{-1} \\]
   Since no broadening is observed, $k(123.15\\text{ K}) > 2 \\times 10^4\\text{ s}^{-1}$.
3. Using the Eyring equation:
   \\[ \\Delta G^\\ddagger < R T \\left[ \\ln\\left(\\frac{k_B T}{h}\\right) - \\ln(k) \\right] \\]
   - $\\frac{k_B T}{h} = \\frac{(1.38065 \\times 10^{-23})(123.15)}{6.62607 \\times 10^{-34}} = 2.566 \\times 10^{12}\\text{ s}^{-1}$
   - $\\ln\\left(\\frac{k_B T}{h}\\right) = \\ln(2.566 \\times 10^{12}) \\approx 28.57$
   - $\\ln(k) > \\ln(2 \\times 10^4) \\approx 9.90$
   - Difference: $28.57 - 9.90 = 18.67$
4. Calculating $\\Delta G^\\ddagger$:
   \\[ \\Delta G^\\ddagger < (8.3145\\text{ J/(mol}\\cdot\\text{K)})(123.15\\text{ K})(18.67) = 1024 \\times 18.67 \\approx 19,100\\text{ J/mol} \\approx 19.1\\text{ kJ/mol} \\]
- **Conclusion**: The activation barrier for carbonyl scrambling in $\\text{Fe}_3(\\text{CO})_{12}$ is extraordinarily low: $\\mathbf{\\Delta G^\\ddagger < 20\\text{ kJ/mol}}$ (less than $5\\text{ kcal/mol}$), rendering the carbonyl envelope essentially a liquid-like mantle flowing effortlessly over the rigid triiron cluster core."""
        }
    ]

    return {
        "unit_number": 3,
        "title": "Metal Carbonyls, Nitrosyls & Phosphine Complexes",
        "description": "Synthesis, structures, bonding and reactions of metal carbonyls, nitrosyls and phosphines. Dewar-Chatt-Duncanson sigma-donation and pi-backbonding, Cotton-Kraihanzel vibrational force field, linear vs bent nitrosyls, Enemark-Feltham notation, Tolman cone angles and electronic parameters, natural bite angle in chelating diphosphines, Collman's reagent, and fluxional carbonyl scrambling.",
        "sections": sections,
        "problems": problems
    }
