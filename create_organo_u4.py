"""
create_organo_u4.py
Unit 4: sigma-Bound Ligands: Alkyls, Aryls, Hydrides & Agostic Interactions
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_4():
    sections = [
        {
            "id": "sec4_1",
            "title": "§4.1 Transition Metal-Carbon $\\sigma$-Bonds: Thermodynamic Stability vs. Kinetic Lability",
            "content": """Historically, transition metal-carbon $\\sigma$-bonds ($M-\\text{C}$) were presumed intrinsically unstable because early synthetic attempts yielded rapid decomposition at or below room temperature. Thermochemical calorimetric studies (Halpern, Connor, Marks) disproved this misconception, revealing that transition metal-alkyl bond dissociation energies ($D_0(M-\\text{C}) \\approx 120-350\\text{ kJ/mol}$) are comparable to, or greater than, main group $M-\\text{C}$ bonds and carbon-carbon single bonds ($D_0(\\text{C}-\\text{C}) \\approx 350\\text{ kJ/mol}$).

### Distinction Between Thermodynamic Stability and Kinetic Lability:
- **Thermodynamic Stability**: Refers to the standard enthalpy and Gibbs free energy of the bond:
  \\[ M-\\text{C} \\longrightarrow M^\\bullet + \\text{C}^\\bullet \\quad (\\Delta H = D_0(M-\\text{C})) \\]
  Transition metal-alkyl bonds are thermodynamically stable with substantial homolytic bond dissociation enthalpies.
- **Kinetic Lability**: Refers to the activation energy barrier $\\Delta G^\\ddagger$ for decomposition pathways.
  Because transition metals possess accessible valence $d$-orbitals, low-energy coordination sites, and variable oxidation states, metal-alkyls decompose via rapid, concerted intramolecular pathways characterized by very low activation barriers ($\\Delta G^\\ddagger < 60-80\\text{ kJ/mol}$).
  Unstabilized transition metal-alkyls undergo decomposition in fractions of a second at ambient temperature.

### Primary Synthetic Routes:
1. **Alkylation via Transmetallation**: Reaction of transition metal halides with main group alkylating agents:
   \\[ L_n M-\\text{Cl} + R\\text{Li} \\longrightarrow L_n M-R + \\text{LiCl} \\downarrow \\]
   \\[ L_n M-\\text{Cl} + R\\text{MgX} \\longrightarrow L_n M-R + \\text{MgXCl} \\downarrow \\]
2. **Oxidative Addition**: Low-valent, electron-rich metal centers insert into carbon-halogen bonds:
   \\[ L_n M^m + R-\\text{X} \\longrightarrow L_n M^{m+2}(R)(\\text{X}) \\]
3. **Migratory Insertion of Alkenes into Metal-Hydrides**:
   \\[ L_n M-\\text{H} + \\text{H}_2\\text{C}=\\text{CH}_2 \\rightleftharpoons L_n M-\\text{CH}_2\\text{CH}_3 \\]
4. **Nucleophilic Attack on Coordinated $\\pi$-Ligands**:
   \\[ [L_n M(\\eta^2-\\text{C}_2\\text{H}_4)]^+ + \\text{Nu}^- \\longrightarrow L_n M-\\text{CH}_2\\text{CH}_2\\text{Nu} \\]"""
        },
        {
            "id": "sec4_2",
            "title": "§4.2 Decomposition Pathways of Metal Alkyls: The $\\beta$-Hydride Elimination Mechanism",
            "content": """The dominant, ubiquitous decomposition pathway of transition metal alkyls containing $\\beta$-hydrogen atoms is **$\\beta$-hydride elimination**.

### Mechanism and Stereoelectronic Prerequisites:
In an alkyl complex $L_n M-\\text{CH}_2\\text{CH}_2 R$:
1. **Coplanar Transition State**: The metal center, $\\alpha$-carbon, $\\beta$-carbon, and $\\beta$-hydrogen must achieve a planar, four-membered transition state:
   \\[ M-\\text{C}_\\alpha-\\text{C}_\\beta-\\text{H}_\\beta \\longrightarrow [M \\cdots \\text{H}_\\beta \\cdots \\text{C}_\\beta \\cdots \\text{C}_\\alpha]^\\ddagger \\longrightarrow L_n M(\\text{H})(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}R) \\]
   The dihedral angle $\\theta(M-\\text{C}_\\alpha-\\text{C}_\\beta-\\text{H}_\\beta)$ must be strictly $0^\\circ$ (*syn*-coplanar).
2. **Vacant Coordination Site Requirement**: The metal center must possess an accessible, empty coordination orbital cis to the alkyl group to accept the transferring hydride. 
   - 18-electron saturated complexes cannot undergo $\\beta$-hydride elimination until a spectator ligand dissociates to create a 16-electron intermediate:
     \\[ L_n M-R (18\\text{e}) \\xrightleftharpoons{-\\,L} [L_{n-1} M-R] (16\\text{e}) \\xrightarrow{k_\\beta} [L_{n-1} M(\\text{H})(\\text{alkene})] (16\\text{e}) \\]
3. **Alkene Dissociation**: The coordinated alkene dissociates to release free olefin and a metal-hydride:
   \\[ L_{n-1} M(\\text{H})(\\text{alkene}) \\rightleftharpoons L_{n-1} M-\\text{H} + \\text{alkene} \\uparrow \\]
4. **Subsequent Decomposition**: The metal hydride decomposes via bimolecular reductive elimination with another alkyl complex, yielding alkane and metal precipitation:
   \\[ L_n M-\\text{H} + L_n M-R \\longrightarrow 2\\,L_n M + R-\\text{H} \\]

### Microscopic Reversibility:
By the principle of microscopic reversibility, the reverse of $\\beta$-hydride elimination is **migratory insertion of an alkene into a metal-hydride bond**, which represents the key propagation step in olefin hydrogenation, hydroformylation, and polymerization."""
        },
        {
            "id": "sec4_3",
            "title": "§4.3 Stabilization Strategies for Metal Alkyls: Lack of $\\beta$-Hydrogens & Steric Shielding",
            "content": """Understanding $\\beta$-hydride elimination allows the rational design of thermally robust, isolable transition metal alkyls:

### 1. Alkyl Ligands Lacking $\\beta$-Hydrogens:
Substituents that possess no hydrogen atoms at the $\\beta$-position cannot undergo $\\beta$-hydride elimination:
- **Methyl ($\\text{CH}_3$)**: Possesses only $\\alpha$-hydrogens. Examples: hexamethyltungsten $\\text{W}(\\text{CH}_3)_6$ (stable red solid), tetramethyltitanium $\\text{Ti}(\\text{CH}_3)_4$.
- **Neopentyl ($\\text{CH}_2\\text{C}(\\text{CH}_3)_3$)**: $\\beta$-carbon is quaternary (no $\\beta$-H). Example: $\\text{Cr}(\\text{CH}_2\\text{CMe}_3)_4$ (stable up to $150^\\circ\\text{C}$).
- **Trimethylsilylmethyl ($\\text{CH}_2\\text{SiMe}_3$)**: Silicon has no attached hydrogens. Example: $\\text{V}(\\text{CH}_2\\text{SiMe}_3)_4$.
- **Benzyl ($\\text{CH}_2\\text{C}_6\\text{H}_5$)**: $\\beta$-positions are $sp^2$ aromatic carbons. $\\beta$-elimination would generate high-energy *o*-quinodimethane.
- **Trifluoromethyl ($\\text{CF}_3$) and Perfluoroalkyls**: Fluorine elimination ($\beta$-fluoride elimination) is thermodynamically disfavored due to the immense strength of $C-F$ bonds ($D_0 \\approx 485\\text{ kJ/mol}$).

### 2. Geometrically Constrained Alkyls (Bredt's Rule Protection):
- **1-Norbornyl ($\\text{C}_7\\text{H}_{11}$)**: Possesses a bridgehead $\\beta$-hydrogen atom. $\\beta$-hydride elimination would form a double bond at a bridgehead position of a bicyclic system, violating **Bredt's rule** and requiring excessive ring strain ($>200\\text{ kJ/mol}$).
- Compounds such as tetrakis(1-norbornyl)cobalt $\\text{Co}(\\text{norbornyl})_4$ and $\\text{Fe}(\\text{norbornyl})_4$ are stable to air, water, and heat up to $100^\\circ\\text{C}$ despite low coordination numbers.

### 3. Electronic and Coordination Saturation:
- Maintaining 18 valence electrons prevents $\\beta$-elimination by denying the metal center an empty orbital for hydride transfer."""
        },
        {
            "id": "sec4_4",
            "title": "§4.4 Metal-Aryl, Vinyl & Alkynyl Complexes: $sp^2$ and $sp$ Hybridization Effects",
            "content": """Transition metal complexes with $sp^2$- and $sp$-hybridized carbon ligands exhibit greater thermal stability and stronger $M-\\text{C}$ bonds than simple $sp^3$-alkyl analogs:

### 1. Metal-Aryl Complexes ($M-\\text{Ar}$):
- **Hybridization & Electronegativity**: The $sp^2$-hybridized carbon has $33\\%$ $s$-character (versus $25\\%$ in $sp^3$), making the carbon atom more electronegative and drawing electron density closer to the nucleus.
- **Bond Length & Strength**: $M-\\text{C}_{sp^2}$ bonds are $0.05-0.10$ Å shorter and $40-60\\text{ kJ/mol}$ stronger than $M-\\text{C}_{sp^3}$ bonds.
- **$\\pi$-Interaction**: In electron-rich metal centers, filled metal $d$-orbitals can overlap with empty $\\pi^*$ orbitals of the aromatic ring, conferring partial double-bond character.
- **Suppression of $\\beta$-Elimination**: $\\beta$-hydride elimination would require generating benzyne ($o$-didehydrobenzene), which carries a colossal ring strain penalty ($\\approx 440\\text{ kJ/mol}$).

### 2. Metal-Vinyl Complexes ($M-\\text{CH}=\\text{CH}_2$):
- Planar coordination with rotation barriers around the $M-\\text{C}$ bond of $40-80\\text{ kJ/mol}$ due to $d_\\pi-\\pi^*$ conjugation.
- $\\beta$-elimination would yield free acetylene; however, the $M-\\text{C}$ bond is sufficiently strong that migratory insertion or reductive elimination usually predominates.

### 3. Metal-Alkynyl Complexes ($M-\\text{C}\\equiv\\text{C}R$):
- $sp$-hybridized carbon ($50\\%$ $s$-character) yields a short, rigid, cylindrical rod-like $M-\\text{C}$ bond.
- Alkynyl ligands act as strong $\\sigma$-donors and moderate $\\pi$-acceptors via orthogonal sets of $\\pi^*$ orbitals.
- Alkynyl complexes are impervious to $\\beta$-elimination (no $\\beta$-H possible) and form 1D organometallic molecular wires and polymers."""
        },
        {
            "id": "sec4_5",
            "title": "§4.5 Transition Metal Hydrides: Synthesis, Bonding & Acidic vs. Hydridic Reactivity",
            "content": """Transition metal hydrides ($M-\\text{H}$) feature direct bonds between a transition metal and a hydrogen atom, serving as essential reactive intermediates across hydrogenation, hydroformylation, and isomerisation catalysis.

### Synthesis of Metal Hydrides:
1. **Oxidative Addition of Dihydrogen**:
   \\[ L_n M^m + \\text{H}_2 \\rightleftharpoons L_n M^{m+2}(\\text{H})_2 \\quad (\\text{e.g., Vaska's complex, Wilkinson's catalyst}) \\]
2. **Reaction with Main Group Hydrides**:
   \\[ L_n M-\\text{Cl} + \\text{NaBH}_4 \\longrightarrow L_n M-\\text{H} + \\text{NaCl} + \\text{BH}_3 \\]
   \\[ L_n M-\\text{Cl} + \\text{LiAlH}_4 \\longrightarrow L_n M-\\text{H} + \\text{LiCl} + \\text{AlH}_3 \\]
3. **$\\beta$-Hydride Elimination from Alkoxides or Alkyls**:
   \\[ L_n M-\\text{OCH}(\\text{CH}_3)_2 \\xrightarrow{\\Delta} L_n M-\\text{H} + \\text{O}=\\text{C}(\\text{CH}_3)_2 \\]
4. **Protonation of Low-Valent Anionic Metal Centers**:
   \\[ [\\text{Co}(\\text{CO})_4]^- + \\text{H}^+ \\longrightarrow \\text{HCo}(\\text{CO})_4 \\]

### Amphiphilic Reactivity: Hydridic vs. Acidic:
The polarity of the $M-\\text{H}$ bond varies across a continuous spectrum depending on metal oxidation state and coligand electronics:
- **Hydridic ($M^{\\delta+} - \\text{H}^{\\delta-}$)**:
  Electron-rich metal centers with strong donor ligands (e.g., phosphines, alkyls) polarize electron density onto hydrogen. They react with electrophiles ($\text{H}^+, \text{R}^+$) to release $\text{H}_2$ or alkane:
  \\[ Cp_2\\text{Zr}(\\text{H})\\text{Cl} + \\text{H}^+ \\longrightarrow [Cp_2\\text{ZrCl}]^+ + \\text{H}_2 \\uparrow \\]
  Hydride donor ability is quantified by **hydricity** $\\Delta G_{\\text{H}^-}^\\circ$.
- **Acidic ($M^{\\delta-} - \\text{H}^{\\delta+}$)**:
  Electron-deficient metal centers with strong $\\pi$-acceptor ligands (carbonyls) withdraw electron density from hydrogen.
  - Tetracarbonylhydridocobalt $\\text{HCo}(\\text{CO})_4$ has a $\\text{p}K_a \\approx -1$ in water, behaving as a **strong mineral acid** comparable to $\\text{HCl}$!
  - Pentacarbonylhydridomanganese $\\text{HMn}(\\text{CO})_5$ has a $\\text{p}K_a \\approx 7$ in acetonitrile."""
        },
        {
            "id": "sec4_6",
            "title": "§4.6 Nuclear Magnetic Resonance Spectroscopy of Transition Metal Hydrides",
            "content": """The hydrogen atom coordinated to a transition metal displays a unique spectroscopic fingerprint in $^1\\text{H}$ NMR spectroscopy:

### Unprecedented High-Field Chemical Shifts:
- In classical organic compounds, protons resonate between $\\delta = 0\\text{ ppm}$ and $+12\\text{ ppm}$.
- Transition metal hydrides resonate at **extreme high fields (negative chemical shifts)**, typically between:
  \\[ \\delta = -5\\text{ ppm} \\quad \\text{to} \\quad -40\\text{ ppm} \\]
  (e.g., $[\\text{IrH}(\\text{CO})(\\text{PPh}_3)_3]$ at $\\delta = -10.5\\text{ ppm}$, $[\\text{HRh}(\\text{CN})_5]^{3-}$ at $\\delta = -10.7\\text{ ppm}$, and $[(\\text{PCy}_3)_2\\text{IrH}_5]$ up to $\\delta = -50\\text{ ppm}$).

### Quantum Chemical Origin of Negative Chemical Shifts (Buckingham-Stephens Theory):
The total magnetic shielding constant $\\sigma$ comprises diamagnetic ($\\sigma_d$) and paramagnetic ($\\sigma_p$) components:
\\[ \\sigma = \\sigma_d + \\sigma_p \\]
- Protons lack valence $p$-electrons, so their local paramagnetic term $\\sigma_p^\\text{local} \\approx 0$.
- However, the coordinated proton sits directly in the valence coordination sphere of the transition metal atom, in immediate proximity to the metal's filled non-bonding $d$-orbitals ($t_{2g}$).
- Under the applied external magnetic field $B_0$, mixing between ground-state filled metal $d$-orbitals and low-lying empty $d$-orbitals induces a circular circulation of valence electrons on the metal center.
- This induced electronic circulation generates an intense **long-range paramagnetic shielding current at the metal center** that produces a large secondary magnetic field opposing $B_0$ at the adjacent hydride position.
- This creates an enormous positive shielding contribution ($\\Delta \\sigma > +10-40\\text{ ppm}$), driving the observed resonance to extreme negative chemical shifts.

### Spin-Spin Coupling Signatures:
- **Trans-$J(P-H)$ Coupling**: When trans to a phosphine ligand ($PR_3$), the $^2J(\\text{P}-\\text{H})_\\text{trans}$ coupling constant is characteristically large ($90-160\\text{ Hz}$).
- **Cis-$J(P-H)$ Coupling**: For cis phosphines, $^2J(\\text{P}-\\text{H})_\\text{cis}$ is small ($10-30\\text{ Hz}$).
- This difference provides unambiguous determination of coordination stereochemistry."""
        },
        {
            "id": "sec4_7",
            "title": "§4.7 Dihydrogen Complexes ($M-(\eta^2-\\text{H}_2)$) vs. Classical Dihydrides",
            "content": """Prior to 1984, all complexes containing hydrogen atoms were assumed to be classical hydrides ($M-\\text{H}$) with cleaved $H-H$ bonds. In 1984, Gregory Kubas isolated and crystallized the first non-classical **dihydrogen complex**:
\\[ \\text{W}(\\text{CO})_3(\\text{P}(i\\text{-Pr})_3)_2(\\eta^2-\\text{H}_2) \\]
demonstrating that molecular dihydrogen can coordinate intact to a transition metal center without oxidative cleavage.

### Bonding Mechanism (Dewar-Chatt-Duncanson Framework):
1. **$\\sigma$-Donation**: The filled $\\sigma(H-H)$ bonding orbital of $\\text{H}_2$ donates electron density into an empty metal $d$-orbital of $\\sigma$-symmetry:
   \\[ M \\xleftarrow{\\quad\\sigma\\quad} (\\eta^2-\\text{H}_2) \\]
2. **$\\pi$-Backdonation**: A filled metal $d$-orbital of $\\pi$-symmetry ($d_{xz}$) backdonates into the empty $\\sigma^*(H-H)$ antibonding orbital of dihydrogen:
   \\[ d_\\pi(M) \\xrightarrow{\\quad\\pi\\quad} \\sigma^*(H-H) \\]
- If $\\pi$-backbonding is **moderate**, the $H-H$ bond lengthens from $0.74$ Å (free $\\text{H}_2$) to $0.82-1.00$ Å, forming a stable **non-classical dihydrogen complex**.
- If $\\pi$-backbonding is **strong**, electron population of $\\sigma^*(H-H)$ cleaves the $H-H$ bond completely ($d(H-H) > 1.60$ Å), yielding a **classical dihydride** $M(\\text{H})_2$.

### Experimental Differentiation Criteria:
1. **$H-D$ Spin-Spin Coupling Constant ($^1J_{HD}$)**:
   - In classical hydrides, $^1J_{HD} < 2\\text{ Hz}$ because the hydrogen atoms are uncoupled or separated by metal.
   - In dihydrogen complexes with intact $H-D$ bonds, $^1J_{HD} = 20 - 34\\text{ Hz}$.
2. **Spin-Lattice Relaxation Time ($T_1$)**:
   - Because $T_1$ relaxation is dominated by direct dipole-dipole interaction between the two adjacent protons ($1/T_1 \\propto r_{HH}^{-6}$), non-classical dihydrogen complexes with $r_{HH} < 1.0$ Å exhibit exceptionally short relaxation times ($T_1 < 50\\text{ ms}$ at $400\\text{ MHz}$), whereas classical dihydrides display $T_1 > 300-1000\\text{ ms}$."""
        },
        {
            "id": "sec4_8",
            "title": "§4.8 Agostic Interactions ($3c-2e$ $\\text{C}-\\text{H}\\cdots M$): Signatures & C-H Activation",
            "content": """Coined by Malcolm Green and Maurice Brookhart, the term **agostic interaction** (from Greek *agostos*, meaning 'to hold close') describes a 3-center 2-electron ($3c-2e$) bonding interaction where a coordinated transition metal center interacts with the electrons of an otherwise unactivated carbon-hydrogen single bond:
\\[ M \\cdots \\text{H}-\\text{C} \\]

### Orbital Description:
- The filled $\\sigma(\\text{C}-\\text{H})$ bonding orbital donates its two electrons into a vacant metal valence orbital of an electron-deficient metal center (typically 14- or 16-electron early or late metals).
- Weak backbonding from a filled metal $d$-orbital into the empty $\\sigma^*(\text{C}-\\text{H})$ orbital further stabilizes the interaction.
- The interaction acts as an intramolecular equivalent of a $\\sigma$-complex, representing a frozen intermediate along the reaction coordinate for oxidative $\\text{C}-\\text{H}$ bond cleavage.

### Spectroscopic Diagnostic Criteria:
1. **$^1\\text{H}$ NMR Chemical Shift**: Agostic protons shift significantly upfield ($\\delta = -5\\text{ ppm}$ to $-15\\text{ ppm}$), reflecting partial hydride character.
2. **Reduced $C-H$ Coupling Constant ($^1J_{CH}$)**:
   - Normal $sp^3$ $C-H$ bond: $^1J_{CH} = 125-140\\text{ Hz}$.
   - Agostic $C-H$ bond: $^1J_{CH}$ decreases to **$60-90\\text{ Hz}$**, reflecting a reduced bond order.
3. **Infrared Stretching Frequency ($\\nu(CH)$)**:
   - Normal $C-H$ stretch: $\\nu(CH) = 2850-3000\\text{ cm}^{-1}$.
   - Agostic $C-H$ stretch: shifts to **$2300-2700\\text{ cm}^{-1}$** with substantial broadening.
4. **Neutron Diffraction Geometry**:
   - The $C-H$ distance lengthens to $1.15-1.25$ Å (normal $1.09$ Å).
   - The $M-H$ distance is short ($1.8-2.2$ Å), and the $M-\\text{H}-\\text{C}$ angle is acute ($90^\\circ-140^\\circ$).

Agostic interactions play a decisive role as ground-state stabilizing interactions in Ziegler-Natta living catalysts ($[Cp_2\\text{Zr-R}]^+$) and direct precursors to catalytic $\\text{C}-\\text{H}$ functionalization."""
        }
    ]

    problems = [
        {
            "id": "prob4_1",
            "tier": "Foundational",
            "title": "Thermodynamics of Transition Metal-Alkyl Homolytic Bond Dissociation",
            "statement": "The gas-phase homolytic bond dissociation enthalpy of the $\\text{Mn}-\\text{CH}_3$ bond in $\\text{CH}_3\\text{Mn}(\\text{CO})_5$ is $\\Delta H_0^\\circ = 155\\text{ kJ/mol}$, whereas the $\\text{C}-\\text{C}$ bond in ethane is $377\\text{ kJ/mol}$. (a) Calculate the equilibrium constant for homolysis $K_\\text{hom}$ for both bonds at $298\\text{ K}$ assuming an entropy change of $\\Delta S^\\circ \\approx +125\\text{ J/(mol}\\cdot\\text{K)}$. (b) Based on these calculations, explain why unstabilized metal-alkyls decompose rapidly in solution while ethane is indefinitely stable.",
            "solution": """**Line-by-Line Solution:**

**(a) Equilibrium Constant for Homolysis at $298\\text{ K}$:**

1. **For $\\text{CH}_3\\text{Mn}(\\text{CO})_5$**:
   - $\\Delta H^\\circ = +155\\text{ kJ/mol} = 155,000\\text{ J/mol}$
   - $\\Delta S^\\circ = +125\\text{ J/(mol}\\cdot\\text{K)}$
   \\[ \\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ = 155,000 - (298.15)(125) = 155,000 - 37,269 = +117,731\\text{ J/mol} \\]
   \\[ K_\\text{hom} = \\exp\\left(-\\frac{\\Delta G^\\circ}{RT}\\right) = \\exp\\left(-\\frac{117,731}{(8.3145)(298.15)}\\right) = \\exp(-47.49) \\approx 2.37 \\times 10^{-21} \\]

2. **For Ethane ($\\text{CH}_3-\\text{CH}_3$)**:
   - $\\Delta H^\\circ = +377\\text{ kJ/mol} = 377,000\\text{ J/mol}$
   \\[ \\Delta G^\\circ = 377,000 - 37,269 = +339,731\\text{ J/mol} \\]
   \\[ K_\\text{hom} = \\exp\\left(-\\frac{339,731}{(8.3145)(298.15)}\\right) = \\exp(-137.05) \\approx 2.74 \\times 10^{-60} \\]

**(b) Physical Explanation of Kinetic Lability vs. Thermodynamic Stability:**
- Both complexes have extremely small equilibrium constants for homolysis ($K_\\text{hom} \\ll 10^{-20}$), meaning neither undergoes spontaneous homolytic cleavage at room temperature at an observable rate.
- However, transition metal-alkyls decompose **not by homolysis**, but through **low-barrier concerted pathways** such as $\\beta$-hydride elimination or reductive elimination, where $\\Delta G^\\ddagger < 60-80\\text{ kJ/mol}$.
- In contrast, ethane has no vacant low-energy orbitals or accessible oxidation states; its only decomposition pathway is homolytic cleavage, which possesses an insurmountable activation barrier ($E_a \\approx 377\\text{ kJ/mol}$).
- Therefore, transition metal-alkyls are thermodynamically stable with respect to homolysis, but kinetically labile due to concerted intramolecular reaction channels."""
        },
        {
            "id": "prob4_2",
            "tier": "Foundational",
            "title": "Predicting Rates of $\\beta$-Hydride Elimination Across Alkyl Ligands",
            "statement": "Rank the following transition metal alkyl complexes in order of increasing kinetic stability toward $\\beta$-hydride elimination: (a) $L_n M-\\text{CH}_2\\text{CH}_3$, (b) $L_n M-\\text{CH}_2\\text{C}(\\text{CH}_3)_3$, (c) $L_n M-\\text{CH}_3$, (d) $L_n M-\\text{CH}_2\\text{Si}(\\text{CH}_3)_3$, (e) $L_n M-\\text{CH}(\\text{CH}_3)_2$, (f) $L_n M-\\text{C}_7\\text{H}_{11}$ (1-norbornyl). Provide explicit structural justifications.",
            "solution": """**Line-by-Line Solution:**

**(a) Evaluation of $\\beta$-Hydrogen Availability and Geometry:**

1. **$L_n M-\\text{CH}(\\text{CH}_3)_2$ (isopropyl)**:
   - Possesses **six $\\beta$-hydrogens** attached to two primary carbons.
   - Secondary alkyl group with high steric congestion and multiple pathways for *syn*-coplanar alignment.
   - Extremely rapid $\\beta$-elimination; least stable.

2. **$L_n M-\\text{CH}_2\\text{CH}_3$ (ethyl)**:
   - Possesses **three $\\beta$-hydrogens** on a primary carbon.
   - Undergoes smooth, rapid $\\beta$-elimination via a low-energy planar four-membered transition state.

3. **$L_n M-\\text{C}_7\\text{H}_{11}$ (1-norbornyl)**:
   - Possesses bridgehead $\\beta$-hydrogens.
   - $\\beta$-elimination would generate a double bond at a bridgehead carbon, violating **Bredt's rule** and incurring severe ring strain.
   - Highly stable; decomposes only at elevated temperatures.

4. **$L_n M-\\text{CH}_2\\text{C}(\\text{CH}_3)_3$ (neopentyl)**:
   - The $\\beta$-carbon is quaternary; **zero $\\beta$-hydrogens**.
   - $\\beta$-elimination is chemically impossible.

5. **$L_n M-\\text{CH}_2\\text{Si}(\\text{CH}_3)_3$ (trimethylsilylmethyl)**:
   - Silicon occupies the $\\beta$-position; **zero $\\beta$-hydrogens**.
   - Thermally robust.

6. **$L_n M-\\text{CH}_3$ (methyl)**:
   - No $\\beta$-carbon; **zero $\\beta$-hydrogens**.
   - Highly stable toward $\\beta$-elimination.

**(b) Ranking of Increasing Kinetic Stability:**
\\[ L_n M-\\text{CH}(\\text{CH}_3)_2 < L_n M-\\text{CH}_2\\text{CH}_3 \\ll L_n M-\\text{C}_7\\text{H}_{11} < L_n M-\\text{CH}_2\\text{CMe}_3 \\approx L_n M-\\text{CH}_2\\text{SiMe}_3 \\approx L_n M-\\text{CH}_3 \\]
The first two undergo rapid $\\beta$-elimination, while the remaining four are kinetically robust."""
        },
        {
            "id": "prob4_3",
            "tier": "Foundational",
            "title": "Stereochemical Assignment of Hydride Coordination via $^2J(P-H)$ Coupling",
            "statement": "An octahedral rhodium hydride complex $[\\text{RhH}(\\text{CO})(\\text{PPh}_3)_2\\text{Cl}_2]$ exhibits a $^1\\text{H}$ NMR hydride resonance at $\\delta = -14.2\\text{ ppm}$. The signal splits into a doublet of triplets with coupling constants $^1J(\\text{Rh}-\\text{H}) = 28\\text{ Hz}$ and $^2J(\\text{P}-\\text{H}) = 14\\text{ Hz}$. (a) Deduce whether the two triphenylphosphine ligands are mutually *cis* or *trans* to the hydride. (b) Explain why $^2J(\\text{P}-\\text{H})_\\text{trans}$ is substantially larger than $^2J(\\text{P}-\\text{H})_\\text{cis}$ using the Fermi contact term.",
            "solution": """**Line-by-Line Solution:**

**(a) Structural Assignment from Coupling Constants:**
1. Rhodium-103 is a $100\\%$ abundant spin-$1/2$ nucleus ($I = 1/2$). Coupling to $^{103}\\text{Rh}$ splits the hydride resonance into a doublet with $^1J(\\text{Rh}-\\text{H}) = 28\\text{ Hz}$.
2. The two equivalent phosphorus-31 nuclei ($I = 1/2$) further split the signal into a triplet with $^2J(\\text{P}-\\text{H}) = 14\\text{ Hz}$.
3. In transition metal coordination chemistry:
   - Trans phosphine-hydride coupling: $^2J(\\text{P}-\\text{H})_\\text{trans} = 90 - 160\\text{ Hz}$.
   - Cis phosphine-hydride coupling: $^2J(\\text{P}-\\text{H})_\\text{cis} = 10 - 30\\text{ Hz}$.
4. The observed value of $^2J(\\text{P}-\\text{H}) = 14\\text{ Hz}$ falls directly within the **cis-coupling range**.
- **Conclusion**: Both triphenylphosphine ligands occupy positions **mutually *cis* to the hydride ligand**."""
        },
        {
            "id": "prob4_4",
            "tier": "Intermediate",
            "title": "Quantum Mechanics of Buckingham-Stephens Magnetic Shielding in Metal Hydrides",
            "statement": "In the Ramsey equation for magnetic shielding, $\\sigma = \\sigma_d + \\sigma_p$. Transition metal hydrides resonate at anomalous negative chemical shifts ($\\delta = -5$ to $-40\\text{ ppm}$). (a) Derive why the diamagnetic term $\\sigma_d$ of the isolated hydride anion fails to account for this shift. (b) Formulate the second-order perturbation expression for the temperature-independent paramagnetic term $\\sigma_p$ originating from the metal valence $d$-orbitals, and show why it produces a strong positive shielding contribution at the hydride nucleus.",
            "solution": """**Line-by-Line Solution:**

**(a) Failure of the Diamagnetic Term $\\sigma_d$:**
1. The Lamb formula for the diamagnetic shielding of an $s$-electron at distance $r$ from a nucleus is:
   \\[ \\sigma_d = \\frac{\\mu_0 e^2}{12\\pi m_e} \\left\\langle \\frac{1}{r} \\right\\rangle \\]
2. For an isolated hydrogen atom with a $1s$ electron ($a_0 = 0.529$ Å):
   \\[ \\sigma_d(1s) \\approx 17.8\\text{ ppm} \\]
3. Even for a hypothetical free hydride ion $\\text{H}^-$ with two electrons, the maximum diamagnetic shielding cannot exceed $\\approx 26\\text{ ppm}$ relative to a bare proton.
4. Relative to the standard reference TMS (tetramethylsilane, which has $\\sigma \\approx 31\\text{ ppm}$), a shift of $\\delta = -40\\text{ ppm}$ corresponds to an absolute shielding of:
   \\[ \\sigma_\\text{hydride} = \\sigma_\\text{TMS} - \\delta = 31 - (-40) = +71\\text{ ppm} \\]
5. Because $\\sigma_d$ from the hydrogen electron cloud is at most $26\\text{ ppm}$, diamagnetic shielding of the proton itself is completely incapable of explaining shifts below $\\delta = 0\\text{ ppm}$.

**(b) Buckingham-Stephens Paramagnetic Shielding Formulation:**
1. The transition metal center possesses filled non-bonding $d$-orbitals (e.g., $t_{2g}$ in $O_h$, such as $d_{xy}, d_{yz}, d_{xz}$) at energy $E_0$ and low-lying empty $d$-orbitals (e.g., $e_g^*$ or $p_z$) at energy $E_n$.
2. An external magnetic field $B_0$ directed along the $z$-axis mixes the ground state $|0\\rangle$ with excited states $|n\\rangle$ via the angular momentum operator $\\hat{L}_z$:
   \\[ |0'\\rangle = |0\\rangle - \\sum_{n} \\frac{\\langle n | \\hat{L}_z B_0 | 0 \\rangle}{E_n - E_0} |n\\rangle \\]
3. This magnetic mixing induces a circular current of electrons within the metal $d$-orbitals around the metal center, generating an orbital magnetic dipole moment $\\boldsymbol{\\mu}_M$ at the metal atom:
   \\[ \\boldsymbol{\\mu}_M = -\\chi_{vv} \\mathbf{B}_0 \\]
   where $\\chi_{vv}$ is the van Vleck paramagnetic susceptibility of the metal center.
4. The dipolar magnetic field produced by this metal-centered magnetic moment at the adjacent hydride proton (located at distance $R$ along the $z$-axis) is given by the classical dipole field equation:
   \\[ \\mathbf{B}_\\text{secondary} = \\frac{\\mu_0}{4\\pi} \\left[ \\frac{3(\\boldsymbol{\\mu}_M \\cdot \\hat{\\mathbf{r}})\\hat{\\mathbf{r}} - \\boldsymbol{\\mu}_M}{R^3} \\right] \\]
5. For a hydride ligand situated along the $z$-axis ($z = R$), the induced secondary magnetic field at the proton is:
   \\[ B_z^\\text{sec} = \\frac{\\mu_0}{4\\pi} \\frac{2 \\mu_M}{R^3} \\]
   Because the orbital current is paramagnetic with respect to the metal, $\\boldsymbol{\\mu}_M$ is oriented to produce an opposing magnetic field in the local equatorial plane, but an **enforcing positive shielding field** directly along the bond axis.
6. The resulting long-range shielding constant at the hydride nucleus is:
   \\[ \\sigma_p(H) = + \\frac{\\mu_0 e^2 \\hbar^2}{6\\pi m_e^2 R^3} \\sum_n \\frac{|\\langle 0 | \\hat{L}_M | n \\rangle|^2}{E_n - E_0} \\]
   Because $E_n - E_0 > 0$, this contribution is **strictly positive** and inversely proportional to $R^3$.
7. Because the $M-\\text{H}$ bond distance is exceptionally short ($R \\approx 1.5 - 1.7$ Å), $1/R^3$ is very large, contributing $+15$ to $+45\\text{ ppm}$ of positive magnetic shielding to the proton, producing the extreme negative chemical shifts observed experimentally."""
        },
        {
            "id": "prob4_5",
            "tier": "Intermediate",
            "title": "Kinetics of Alkene $\\beta$-Hydride Elimination vs. Phosphine Dissociation",
            "statement": "The thermal decomposition of $(\\text{PPh}_3)_2\\text{Pt}(\\text{CH}_2\\text{CH}_3)_2$ in benzene at $60^\\circ\\text{C}$ obeys the rate law: $-\\frac{d[\\text{Pt}]}{dt} = \\frac{k_1 [\\text{Pt}]}{1 + K [\\text{PPh}_3]}$. (a) Propose a detailed mechanism accounting for this rate law. (b) Explain why adding excess triphenylphosphine suppresses decomposition. (c) Deduce the stoichiometry of the platinum-containing and organic products.",
            "solution": """**Line-by-Line Solution:**

**(a) Elementary Reaction Mechanism:**
1. Starting complex: $(\\text{PPh}_3)_2\\text{Pt}(\\text{Et})_2$ is a 16-electron square planar $d^8$ $\\text{Pt}(\\text{II})$ complex.
2. Although it possesses only 16 electrons, square planar geometry has all 4 in-plane coordination sites occupied. For the ethyl group to achieve a *syn*-coplanar four-membered transition state, the Pt center requires an open coordination site in the coordination plane.
3. **Step 1: Reversible Dissociation of Phosphine**:
   \\[ (\\text{PPh}_3)_2\\text{Pt}(\\text{Et})_2 \\xrightleftharpoons[k_{-1}]{k_1} (\\text{PPh}_3)\\text{Pt}(\\text{Et})_2 + \\text{PPh}_3 \\]
   generating a 14-electron, 3-coordinate T-shaped intermediate $[(\\text{PPh}_3)\\text{Pt}(\\text{Et})_2]$.
4. **Step 2: $\\beta$-Hydride Elimination**:
   \\[ (\\text{PPh}_3)\\text{Pt}(\\text{Et})_2 \\xrightarrow{k_2} (\\text{PPh}_3)\\text{Pt}(\\text{H})(\\text{Et})(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}_2) \\]
5. **Step 3: Reductive Elimination of Ethane**:
   \\[ (\\text{PPh}_3)\\text{Pt}(\\text{H})(\\text{Et})(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}_2) \\xrightarrow{k_3} (\\text{PPh}_3)\\text{Pt}(\\eta^2-\\text{H}_2\\text{C}=\\text{CH}_2) + \\text{CH}_3\\text{CH}_3 \\uparrow \\]

Applying the steady-state approximation to the 14-electron intermediate:
\\[ \\frac{d[\\text{Pt}_{14}]}{dt} = k_1 [\\text{Pt}_{16}] - k_{-1} [\\text{Pt}_{14}][\\text{PPh}_3] - k_2 [\\text{Pt}_{14}] = 0 \\]
\\[ [\\text{Pt}_{14}] = \\frac{k_1 [\\text{Pt}_{16}]}{k_2 + k_{-1}[\\text{PPh}_3]} \\]
The overall rate of decomposition is:
\\[ \\text{Rate} = k_2 [\\text{Pt}_{14}] = \\frac{k_1 k_2 [\\text{Pt}_{16}]}{k_2 + k_{-1}[\\text{PPh}_3]} = \\frac{k_1 [\\text{Pt}_{16}]}{1 + \\left(\\frac{k_{-1}}{k_2}\\right)[\\text{PPh}_3]} \\]
This matches the empirical rate law with $K = \\frac{k_{-1}}{k_2}$.

**(b) Inhibition by Excess Triphenylphosphine:**
- Excess $\\text{PPh}_3$ drives the equilibrium back toward the 4-coordinate 16-electron complex via Le Chatelier's principle ($k_{-1}[\\text{PPh}_3] \\gg k_2$).
- Denying the complex a vacant coordination site completely halts the $\\beta$-hydride elimination pathway.

**(c) Stoichiometry of Products:**
\\[ (\\text{PPh}_3)_2\\text{Pt}(\\text{CH}_2\\text{CH}_3)_2 \\longrightarrow \\text{Pt}(0)(\\text{PPh}_3)_2 + \\text{H}_2\\text{C}=\\text{CH}_2 \\uparrow + \\text{CH}_3\\text{CH}_3 \\uparrow \\]
- Products: exactly **one equivalent of ethene gas**, **one equivalent of ethane gas**, and platinum(0) species."""
        },
        {
            "id": "prob4_6",
            "tier": "Intermediate",
            "title": "Differentiation Between Dihydrogen and Dihydride Complexes via $T_1$ and $J_{HD}$",
            "statement": "A newly synthesized ruthenium complex $[(\\text{dppe})_2\\text{Ru}(\\text{H})_2]$ could formulate as a non-classical dihydrogen complex $[(\\text{dppe})_2\\text{Ru}(\\eta^2-\\text{H}_2)]$ or a classical dihydride *cis*-$[(\\text{dppe})_2\\text{Ru}(\\text{H})_2]$. (a) The monodeuterated isotopologue exhibits $^1J(\\text{H}-\\text{D}) = 29.5\\text{ Hz}$. Assign the structure unambiguously. (b) The spin-lattice relaxation time $T_1$ reaches a minimum of $T_{1,\\text{min}} = 18\\text{ ms}$ at $250\\text{ K}$ on a $500\\text{ MHz}$ spectrometer. Using the dipole-dipole relaxation formula $r_{HH} = 5.815 \\left(\\frac{T_{1,\\text{min}}}{\\nu}\\right)^{1/6}$ Å (where $\\nu$ is in MHz and $T_{1,\\text{min}}$ in seconds), calculate the internuclear $H-H$ distance $r_{HH}$.",
            "solution": """**Line-by-Line Solution:**

**(a) Unambiguous Structural Assignment from $^1J(H-D)$:**
1. In classical metal dihydrides, the two hydrogen atoms are bonded directly to the metal center and not to each other ($d(H-H) > 1.6$ Å). Spin-spin coupling between the two sites through the metal center is small:
   \\[ ^1J(\\text{H}-\\text{D})_\\text{classical} < 2\\text{ Hz} \\]
2. In non-classical dihydrogen complexes, the $H-D$ single bond remains intact ($d(H-D) \\approx 0.8-1.0$ Å). In free $\\text{HD}$ gas, $^1J(\\text{H}-\\text{D}) = 43.2\\text{ Hz}$.
3. Coordinated dihydrogen complexes characteristically display:
   \\[ ^1J(\\text{H}-\\text{D})_\\text{dihydrogen} = 20 - 34\\text{ Hz} \\]
4. The observed value of $^1J(\\text{H}-\\text{D}) = 29.5\\text{ Hz}$ represents unequivocal proof that the hydrogen-deuterium bond is intact.
- **Assignment**: The complex is a **non-classical dihydrogen complex**, $[(\\text{dppe})_2\\text{Ru}(\\eta^2-\\text{H}_2)]$.

**(b) Internuclear $H-H$ Distance Calculation from $T_{1,\\text{min}}$:**
Given:
- $T_{1,\\text{min}} = 18\\text{ ms} = 0.018\\text{ s}$
- Spectrometer frequency $\\nu = 500\\text{ MHz}$

Substitute into the dipole-dipole relaxation formula:
\\[ r_{HH} = 5.815 \\left(\\frac{T_{1,\\text{min}}}{\\nu}\\right)^{1/6} \\]
1. Compute the ratio:
   \\[ \\frac{T_{1,\\text{min}}}{\\nu} = \\frac{0.018}{500} = 3.60 \\times 10^{-5} \\]
2. Compute the sixth root:
   \\[ (3.60 \\times 10^{-5})^{1/6} \\]
   Let $y = 3.60 \\times 10^{-5}$:
   - $\\ln(y) = \\ln(3.60) + \\ln(10^{-5}) = 1.2809 - 11.5129 = -10.232$
   - $\\frac{\\ln(y)}{6} = \\frac{-10.232}{6} \\approx -1.7053$
   - $\\exp(-1.7053) \\approx 0.1817$
3. Compute $r_{HH}$:
   \\[ r_{HH} = 5.815 \\times 0.1817 = 1.056\\text{ Å} \\approx 1.06\\text{ Å} \\]
- **Conclusion**: The internuclear distance is **$r_{HH} = 1.06$ Å**. This is elongated relative to free $\\text{H}_2$ ($0.74$ Å) due to $\\pi$-backbonding, but well within the non-classical dihydrogen regime ($r_{HH} < 1.15$ Å), confirming the non-classical coordination mode."""
        },
        {
            "id": "prob4_7",
            "tier": "Advanced",
            "title": "Spectroscopic and Structural Characterization of Agostic Interactions",
            "statement": "The titanium alkyl complex $[\\text{TiCl}_3(\\text{CH}_2\\text{CH}_3)]$ adopts an agostic ground state $[\\text{TiCl}_3(\\eta^2-\\text{C}_2\\text{H}_5)]$. (a) State the electron count of the titanium center with and without the agostic interaction. (b) Explain the observed changes in infrared spectroscopy ($\\Delta \\nu(CH) = -450\\text{ cm}^{-1}$) and NMR ($^1J_{CH} = 65\\text{ Hz}$ vs $140\\text{ Hz}$ in ethane) using a molecular orbital interaction diagram. (c) Derive why agostic interactions lower the activation barrier for subsequent migratory olefin insertion in Ziegler-Natta polymerization.",
            "solution": """**Line-by-Line Solution:**

**(a) Electron Counting:**
- Titanium is in Group 4 ($n_v = 4$).
- Oxidation state: Three chlorides ($-3$) and one ethyl ($-1$) $\\implies \\text{Ti}(\\text{IV}) (d^0)$.
- **Without Agostic Interaction**:
  - $VEC = 4 (\\text{Ti}) + 3 \\times 1 (\\text{Cl}) + 1 (\\text{Et}) = 8$ valence electrons (drastically sub-octet, highly electron-deficient).
- **With Agostic $\\text{C}-\\text{H}\\cdots\\text{Ti}$ Interaction**:
  - The $\\beta$-$\\text{C}-\\text{H}$ bond acts as a 2-electron donor into a vacant titanium $d$-orbital ($L$-type):
  - $VEC = 8 + 2 = \\mathbf{10\\text{ valence electrons}}$.
  - The agostic interaction partially alleviates the extreme electronic deficiency of the $d^0$ metal.

**(b) Molecular Orbital Origin of Spectroscopic Signatures:**
1. **Three-Center Two-Electron ($3c-2e$) Orbital Overlap**:
   - The filled $\\sigma(\\text{C}-\\text{H})$ bonding orbital donates into the empty $d_{z^2}/d_{xz}$ hybrid orbital of $\\text{Ti}(\\text{IV})$.
   - This dative interaction depopulates electron density from the $\\text{C}-\\text{H}$ internuclear bonding region.
2. **Bond Order Depletion**:
   - The formal $\\text{C}-\\text{H}$ bond order drops from $1.0$ to $\\approx 0.5-0.6$.
   - Depletion of $\\sigma(\\text{C}-\\text{H})$ electron density weakens the force constant $k_{CH}$, shifting the stretching frequency from $2950\\text{ cm}^{-1}$ down to $2500\\text{ cm}^{-1}$ ($\\Delta \\nu = -450\\text{ cm}^{-1}$).
3. **Reduction in $^1J_{CH}$**:
   - The Fermi contact term for spin-spin coupling between carbon-13 and proton is directly proportional to the $s$-electron density at both nuclei and the $C-H$ bond order:
     \\[ ^1J_{CH} \\propto |\\psi_{2s,C}(0)|^2 |\\psi_{1s,H}(0)|^2 P_{CH} \\]
   - Transferring electron density out of the $\\sigma(\\text{C}-\\text{H})$ orbital reduces the effective bond order $P_{CH}$, decreasing the coupling constant from $140\\text{ Hz}$ to **$65\\text{ Hz}$**.

**(c) Reduction of Activation Barrier in Ziegler-Natta Insertion:**
1. Migratory insertion requires coordinating an incoming ethylene molecule and migrating the alkyl chain onto ethylene via a four-centered transition state.
2. The agostic interaction pre-organizes the alkyl ligand into an orientation where the $\\alpha$- and $\\beta$-carbons are already bent toward the metal coordination plane ($\angle(\\text{Ti}-\\text{C}-\\text{C}) \\approx 85-95^\\circ$ instead of tetrahedral $109.5^\\circ$).
3. When ethylene coordinates, the weak agostic interaction (bond energy $\\approx 40-60\\text{ kJ/mol}$) is displaced easily without requiring ligand dissociation.
4. During the migration step, the developing transition state is stabilized by a continuous agostic interaction between the metal and the migrating carbon's hydrogen atom, smoothing the electronic potential energy surface and reducing the activation energy $\\Delta G^\\ddagger$ by $20-35\\text{ kJ/mol}$."""
        },
        {
            "id": "prob4_8",
            "tier": "Advanced",
            "title": "Thermodynamics and Hydricity Scales of Transition Metal Hydrides",
            "statement": "Hydricity (hydride-donating ability $\\Delta G_{\\text{H}^-}^\\circ$) measures the free energy for hydride release: $[M-\\text{H}]^{n} \\rightleftharpoons M^{n+1} + \\text{H}^-$. (a) Construct a thermodynamic cycle relating hydricity $\\Delta G_{\\text{H}^-}^\\circ$ to the acidity $\\text{p}K_a$ of $[M-\\text{H}]^n$ and the standard reduction potentials $E^\\circ(M^{n+1}/M^n)$ and $E^\\circ(M^n/M^{n-1})$. (b) Given $\\text{p}K_a = 22.0$ for a cobalt hydride in acetonitrile, $E^\\circ(\\text{Co}^{II}/\\text{Co}^I) = -0.80\\text{ V}$, and the standard heterolytic free energy of dihydrogen in acetonitrile is $\\Delta G_\\text{het}^\\circ(\\text{H}_2) = 318\\text{ kJ/mol}$, calculate the absolute hydricity $\\Delta G_{\\text{H}^-}^\\circ$.",
            "solution": """**Line-by-Line Solution:**

**(a) Thermodynamic Cycle for Hydricity:**
Consider the following thermodynamic steps in solution:
1. **Deprotonation of the Hydride**:
   \\[ [M-\\text{H}]^n \\rightleftharpoons M^{n-1} + \\text{H}^+ \\quad (\\Delta G_1^\circ = 1.37\\,\\text{p}K_a\\text{ kcal/mol} = 2.303 RT\\,\\text{p}K_a) \\]
2. **Two-Electron Oxidation of the Conjugate Base**:
   \\[ M^{n-1} \\rightleftharpoons M^{n+1} + 2\\,e^- \\quad (\\Delta G_2^\circ = 2 F E_{1/2}^\circ) \\]
3. **Formation of Hydride Ion from Proton and Electrons**:
   \\[ \\text{H}^+ + 2\\,e^- \\rightleftharpoons \\text{H}^- \\quad (\\Delta G_3^\circ = \\Delta G_f^\circ(\\text{H}^-)) \\]

Summing steps 1, 2, and 3 yields the net hydride dissociation:
\\[ [M-\\text{H}]^n \\rightleftharpoons M^{n+1} + \\text{H}^- \\]
The absolute hydricity $\\Delta G_{\\text{H}^-}^\\circ$ is:
\\[ \\Delta G_{\\text{H}^-}^\\circ = 2.303 RT\\,\\text{p}K_a + 2 F E_{\\text{avg}}^\circ + \\Delta G_f^\\circ(\\text{H}^-) \\]
where $E_{\\text{avg}}^\circ = \\frac{E^\circ(M^{n+1}/M^n) + E^\circ(M^n/M^{n-1})}{2}$.

**(b) Numerical Calculation of Absolute Hydricity in Acetonitrile:**
In acetonitrile solvent:
- Free energy contribution from acidity:
  \\[ \\Delta G_\\text{acid}^\circ = 2.303 R T \\times \\text{p}K_a = 5.708 \\times 22.0 = 125.6\\text{ kJ/mol} \\]
- Using the standard thermodynamic benchmark established by Daniel DuBois:
  \\[ \\Delta G_{\\text{H}^-}^\\circ = 1.37\\,\\text{p}K_a + 46.1 E^\\circ + 79.6 \\quad (\\text{in kcal/mol}) \\]
  In SI units ($\text{kJ/mol}$):
  \\[ \\Delta G_{\\text{H}^-}^\\circ = 5.71\\,\\text{p}K_a + 192.9 E^\\circ + 333.0 \\]
Given:
- $\\text{p}K_a = 22.0$
- $E^\\circ = -0.80\\text{ V}$

Compute:
\\[ \\Delta G_{\\text{H}^-}^\\circ = 5.71(22.0) + 192.9(-0.80) + 333.0 \\]
\\[ \\Delta G_{\\text{H}^-}^\\circ = 125.62 - 154.32 + 333.0 = 304.3\\text{ kJ/mol} \\]
- **Conclusion**: The absolute hydricity of the cobalt complex is **$\\mathbf{304.3\\text{ kJ/mol}}$** ($\\approx 72.7\\text{ kcal/mol}$). Lower values of $\\Delta G_{\\text{H}^-}^\\circ$ denote stronger hydride donors; this complex is a potent hydride donor capable of reducing carbon dioxide ($\Delta G_{\text{H}^-}^\circ(\\text{HCOO}^-) = 314\\text{ kJ/mol}$) to formate."""
        },
        {
            "id": "prob4_9",
            "tier": "Advanced",
            "title": "Quantum Mechanical Double-Well Potential in Kubas Dihydrogen Complexes",
            "statement": "The potential energy surface connecting a non-classical dihydrogen complex $M(\\eta^2-\\text{H}_2)$ and a classical dihydride $M(\\text{H})_2$ can be modeled as a symmetric or asymmetric double-well potential $V(r) = a r^4 - b r^2 + c r$. (a) Determine the equilibrium internuclear separations for $r_1$ (dihydrogen) and $r_2$ (dihydride) as functions of the potential coefficients. (b) Explain how temperature-dependent inelastic neutron scattering (INS) and coherent rotational quantum tunneling of the $\\text{H}_2$ rotor differentiate between a single minimum and a double well. (c) Derive the tunneling splitting frequency $\\Omega$ using the WKB semiclassical approximation.",
            "solution": """**Line-by-Line Solution:**

**(a) Equilibrium Positions from Potential Minimization:**
The potential energy function along the $H-H$ internuclear separation coordinate $r$ is:
\\[ V(r) = a r^4 - b r^2 + c r \\quad (a > 0, b > 0) \\]
Equilibrium points correspond to the roots of the first derivative:
\\[ \\frac{dV}{dr} = 4 a r^3 - 2 b r + c = 0 \\]
For a symmetric double well ($c = 0$):
\\[ 4 a r^3 - 2 b r = 0 \\implies r(4 a r^2 - 2 b) = 0 \\]
The roots are:
- $r_0 = 0$ (unstable local maximum: transition state barrier separating the two states).
- $r_1, r_2 = \\pm \\sqrt{\\frac{b}{2a}}$.
Taking the physical branch $r > 0$, when an asymmetric term $c \\ne 0$ is introduced (representing electronic bias toward one state):
- Minimum 1 ($r_1 \\approx 0.85$ Å): Non-classical dihydrogen complex.
- Minimum 2 ($r_2 \\approx 1.65$ Å): Classical dihydride complex.
- The barrier height between the two states is:
  \\[ V_0 \\approx \\frac{b^2}{4a} \\]

**(b) Inelastic Neutron Scattering (INS) and Rotational Tunneling:**
1. Dihydrogen coordinated side-on ($M-\\eta^2-\\text{H}_2$) acts as a **two-dimensional quantum rotor** hindered by a twofold or fourfold potential barrier $V(\\phi) = \\frac{V_2}{2}(1 - \\cos 2\\phi)$.
2. Because neutrons have wavelengths comparable to molecular bond lengths ($1-2$ Å) and possess zero charge, they scatter directly off atomic nuclei without selection rules.
3. If the potential is a single well (pure dihydrogen), INS spectra exhibit discrete rotational transitions between quantized rotor states ($J=0 \\to J=1$, para-to-ortho hydrogen transition) at low energy ($0.5 - 5\\text{ meV}$).
4. If a low-barrier double well exists, coherent quantum tunneling between the two wells splits each degenerate vibrational level into a doublet with an energy separation $\\hbar \\Omega$ that is extraordinarily sensitive to isotopic substitution ($H/D$).

**(c) WKB Semiclassical Tunneling Splitting Derivation:**
Under the Wentzel-Kramers-Brillouin (WKB) approximation, the tunneling probability $P$ through the potential barrier $V(r)$ between classical turning points $r_a$ and $r_b$ is:
\\[ P = \\exp\\left( -\\frac{2}{\\hbar} \\int_{r_a}^{r_b} \\sqrt{2\\mu [V(r) - E]}\\, dr \\right) \\]
where $\\mu = \\frac{m_H}{2}$ is the reduced mass of the $\\text{H}_2$ oscillator.
The quantum tunneling frequency $\\Omega$ (and corresponding energy splitting $\\Delta E = \\hbar \\Omega$) is given by:
\\[ \\Omega = \\frac{\\omega_0}{\\pi} \\exp\\left( -\\frac{1}{\\hbar} \\int_{r_a}^{r_b} \\sqrt{2\\mu [V(r) - E]}\\, dr \\right) \\]
where $\\omega_0$ is the classical attempt frequency within the well.
- **Isotope Effect on Tunneling**:
  Because $\\mu_D = 2\\mu_H$, the exponent increases by $\\sqrt{2} \\approx 1.414$.
  Consequently:
  \\[ \\frac{\\Omega_H}{\\Omega_D} = \\exp\\left[ (\\sqrt{2} - 1) \\frac{1}{\\hbar} \\int \\sqrt{2\\mu_H (V-E)}\\, dr \\right] \\gg 10 - 100 \\]
  This colossal quantum tunneling isotope effect observed in low-temperature INS unambiguously verifies the double-well topology of the dihydrogen-to-dihydride reaction coordinate."""
        }
    ]

    return {
        "unit_number": 4,
        "title": "sigma-Bound Ligands: Alkyls, Aryls, Hydrides & Agostic Interactions",
        "description": "Transition metal-carbon sigma-bonds, thermodynamic stability vs kinetic lability, beta-hydride elimination mechanisms and microscopic reversibility, stabilizing ligands lacking beta-hydrogens, Bredt's rule protection, metal aryls, vinyls and alkynyls, metal hydrides, Ramsey Buckingham-Stephens high-field NMR shielding, Kubas non-classical dihydrogen complexes, and agostic 3c-2e C-H...M interactions.",
        "sections": sections,
        "problems": problems
    }
