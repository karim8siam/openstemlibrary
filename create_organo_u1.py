"""
create_organo_u1.py
Unit 1: Fundamentals of Organometallic Chemistry & Electron Counting
8 sections, 9 tiered problems (3 Foundational, 3 Intermediate, 3 Advanced)
"""

def get_unit_1():
    sections = [
        {
            "id": "sec1_1",
            "title": "§1.1 Definition, Historical Milestones & Scope of Organometallic Chemistry",
            "content": """Organometallic chemistry occupies the fertile intellectual frontier between classical inorganic coordination chemistry and organic synthesis. By rigorous IUPAC definition, an **organometallic compound** contains at least one direct, covalent, polar-covalent, or multicenter bond between a metal atom (including transition metals, lanthanides, actinides, and main group elements) and a carbon atom of an organic moiety ($M-C$ bond). Coordination compounds featuring exclusively metal-heteroatom linkages (such as metal alkoxides $M-OR$, amides $M-NR_2$, or carboxylates $M-O_2CR$) are excluded from this classification, regardless of organic substituent content.

The discipline developed through landmark milestones:
1. **Zeise's Salt (1827)**: William Christopher Zeise synthesized $\\text{K}[\\text{PtCl}_3(\\eta^2-\\text{C}_2\\text{H}_4)]\\cdot\\text{H}_2\\text{O}$ by boiling platinum tetrachloride in ethanol, representing the first recognized transition metal $\\pi$-complex, though its structure remained unexplained for over a century.
2. **Frankland's Dialkylzinc Reagents (1849)**: Edward Frankland isolated diethylzinc $\\text{Zn}(\\text{C}_2\\text{H}_5)_2$ while attempting to generate ethyl free radicals, demonstrating organometallic bond formation and foundational concepts of chemical valency.
3. **Mond Carbonyl Process (1890)**: Ludwig Mond discovered nickel tetracarbonyl $\\text{Ni}(\\text{CO})_4$, demonstrating that carbon monoxide forms volatile, homoleptic metal complexes at moderate temperatures, establishing the metal carbonyl field.
4. **Grignard Reagents (1900)**: Victor Grignard synthesized organomagnesium halides $R\\text{MgX}$ in diethyl ether, revolutionizing organic nucleophilic carbon-carbon bond forming transformations.
5. **Ferrocene Discovery (1951)**: T.J. Kealy and P.L. Pauson (and independently S.A. Miller) synthesized bis(cyclopentadienyl)iron $\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_5)_2$. The sandwich structure elucidated by Geoffrey Wilkinson and Ernst Otto Fischer inaugurated modern organometallic bonding theory and the Nobel Prize in Chemistry (1973).

Organometallics are categorized by bond polarity and electronic configuration into **Main Group Organometallics** (governed by octet constraints, formal electronegativity differentials, and localized $\\sigma$- or multicenter bonding) and **Transition Metal Organometallics** (governed by valence $d$-orbitals, coordinate $\\pi$-backbonding, variable oxidation states, and the 18-electron rule)."""
        },
        {
            "id": "sec1_2",
            "title": "§1.2 Classification of Organic Ligands: The Covalent (Neutral) vs. Ionic Counting Models",
            "content": """Accurate electron counting requires systematic classification of ligands. Two self-consistent formalisms exist: the **Covalent (Neutral Ligand) Model** and the **Ionic (Dative) Model**. Both yield identical total valence electron counts but partition electrons differently between metal oxidation states and ligand formal charges.

### The Covalent (Neutral) Model
Every ligand is removed as a neutral radical or molecule, regardless of electronegativity:
- **X-type Ligands**: Neutral radical fragments providing 1 electron to the metal-ligand bond. Examples include hydride ($\\text{H}^\\bullet$), alkyl ($\\text{CH}_3^\\bullet$), halide ($\\text{Cl}^\\bullet$), aryl ($\\text{C}_6\\text{H}_5^\\bullet$), and cyanide ($\\text{CN}^\\bullet$).
- **L-type Ligands**: Neutral 2-electron lone-pair donors that coordinate datively without changing the metal formal charge. Examples include phosphines ($:PR_3$), carbon monoxide ($:CO$), alkenes ($\\eta^2-\\text{C}_2\\text{H}_4$), amines ($:NR_3$), ethers ($:OR_2$), and solvent molecules.
- **Z-type Ligands**: Zero-electron Lewis acidic acceptors that accept an electron pair from the metal center (e.g., $:BR_3$).

### The Ionic Model
Ligands are removed with filled valence shells (closed-shell octets), assigning formal charges reflecting electronegativity:
- Halides, alkyls, and hydrides depart as anions ($X^-$: 2-electron donors). The metal center oxidation state increases accordingly.
- Neutral donors remain 2-electron donors ($L$: 2 electrons, neutral).

The general formula under the Green **CBC (Covalent Bond Classification)** framework represents any complex as:
\\[ [M L_l X_x Z_z]^z \\]
The formal oxidation state ($OS$) of the metal center is given by:
\\[ OS = x + z - q \\]
where $q$ is the overall molecular charge of the complex.

The total valence electron count ($VEC$) in the Neutral Model is:
\\[ VEC = n_v + 2l + x - q \\]
where $n_v$ is the group number of the neutral transition metal atom (number of valence $(n)s + (n-1)d$ electrons). In the Ionic Model:
\\[ d^n = n_v - OS, \\quad VEC = d^n + 2(l + x) \\]
Both formalisms arrive at identical $VEC$ values."""
        },
        {
            "id": "sec1_3",
            "title": "§1.3 Polyhapto & Multidentate Ligand Donor Classifications",
            "content": """The hapticity (denoted by Greek letter $\\eta^n$) defines the number of contiguous atoms of an organic ligand simultaneously bound to a central metal atom within bonding distance.

Common polyhapto ligands and their electron counts (Neutral Model):
- **Alkynes ($\\eta^2-\\text{C}_2R_2$)**: 2-electron donors via the filled bonding $\\pi$-orbital. In electron-deficient or low-valent systems with backdonation into $\\pi^*$, alkynes can act as 4-electron donors using their orthogonal $\\pi$-system ($LX$-type).
- **$\\eta^3$-Allyl ($\\text{C}_3\\text{H}_5$)**: Acts as an $LX$ ligand (3-electron donor in neutral model, 4-electron donor as allyl anion $\\text{C}_3\\text{H}_5^-$).
- **$\\eta^4$-Dienes (e.g., 1,3-butadiene)**: Two conjugated $\\pi$-bonds donate 4 electrons ($L_2$-type).
- **$\\eta^5$-Cyclopentadienyl ($Cp$, $\\text{C}_5\\text{H}_5$)**: Provides 5 electrons as a neutral radical ($L_2X$) or 6 electrons as the aromatic cyclopentadienyl anion ($Cp^-$).
- **$\\eta^6$-Arenes (e.g., Benzene $\\text{C}_6\\text{H}_6$)**: Donates 6 electrons ($L_3$-type) from the three degenerate occupied $\\pi$-orbitals.
- **$\\eta^7$-Cycloheptatrienyl ($\text{C}_7\text{H}_7$)**: $L_3X$ 7-electron donor (neutral) or 6-electron donor as tropylium cation $\\text{C}_7\\text{H}_7^+$.

Variable hapticity is central to organometallic reactivity, enabling associative ligand substitution without exceeding 18 valence electrons via hapticity shifts (e.g., $\\eta^5-Cp \\rightleftharpoons \\eta^3-Cp \\rightleftharpoons \\eta^1-Cp$, ring slipping)."""
        },
        {
            "id": "sec1_4",
            "title": "§1.4 Derivation and Molecular Orbital Basis of the 18-Electron Rule",
            "content": """The **18-electron rule** (Noble Gas Rule for transition metals) posits that thermodynamically stable, diamagnetic organotransition metal complexes possess 18 valence electrons, filling all available valence orbitals: one $(n)s$, three $(n)p$, and five $(n-1)d$ orbitals ($1 + 3 + 5 = 9$ valence orbitals $\\times 2 = 18$ electrons).

### Molecular Orbital Origin in Octahedral ($O_h$) Complexes
Consider an octahedral complex $ML_6$ with pure $\\sigma$-donor ligands:
1. **Metal Valence Orbitals**:
   - $s$ orbital transform as $a_{1g}$
   - $p_x, p_y, p_z$ transform as $t_{1u}$
   - $d_{z^2}, d_{x^2-y^2}$ transform as $e_g$
   - $d_{xy}, d_{yz}, d_{xz}$ transform as $t_{2g}$
2. **Ligand Group Orbitals (LGOs)**: Six ligand lone pairs span representations:
   \\[ \\Gamma_{\\sigma} = a_{1g} + e_g + t_{1u} \\]
3. **Orbital Interactions & MO Diagram**:
   - The $a_{1g}$ ($s$), $t_{1u}$ ($p$), and $e_g$ ($d_{z^2}, d_{x^2-y^2}$) metal orbitals overlap with ligand LGOs to generate 6 strongly bonding MOs ($1a_{1g}, 1t_{1u}, 1e_g$) and 6 strongly antibonding MOs ($2a_{1g}^*, 2t_{1u}^*, 2e_g^*$).
   - The metal $t_{2g}$ orbitals ($d_{xy}, d_{yz}, d_{xz}$) possess no $\\sigma$-symmetry match among LGOs and remain strictly non-bonding in a pure $\\sigma$-framework.
4. **Consequence of Strong $\\pi$-Acceptor Ligands (e.g., CO, Phosphines)**:
   - When ligands possess low-lying empty $\\pi^*$ orbitals (as in carbon monoxide), these LGOs transform as $t_{2g}$.
   - Interaction between the metal $t_{2g}$ and ligand $\\pi^*$ stabilizes the bonding $t_{2g}$ MO and raises the antibonding $t_{2g}^*$, drastically increasing the octahedral ligand field splitting parameter $\\Delta_o$:
   \\[ \\Delta_o = E(e_g^*) - E(t_{2g}) \\]
5. **Electronic Saturation**:
   - The 6 bonding MOs host 12 electrons (ligand-derived).
   - The 3 bonding/stabilized $t_{2g}$ MOs host up to 6 electrons (metal-derived).
   - Total electrons filling bonding and non-bonding orbitals without populating strongly antibonding $e_g^*$ orbitals equals $12 + 6 = 18$ electrons. Any electron added beyond 18 must occupy destabilizing $e_g^*$ orbitals, while complexes with fewer than 18 electrons possess unoccupied non-bonding or weakly bonding levels."""
        },
        {
            "id": "sec1_5",
            "title": "§1.5 Sub-18-Electron Complexes: 16-Electron Square Planar $d^8$ Systems",
            "content": """The 18-electron rule is not universal; significant classes of stable complexes systematically violate it:

### The 16-Electron $d^8$ Square Planar Complex Class
Late transition metal ions in low oxidation states with $d^8$ configurations—specifically $\\text{Rh}(\\text{I})$, $\\text{Ir}(\\text{I})$, $\\text{Pd}(\\text{II})$, and $\\text{Pt}(\\text{II})$—predominantly adopt 4-coordinate square planar geometry with 16 valence electrons.

Under $D_{4h}$ symmetry:
- The metal $d$-orbitals split into four distinct energy levels:
  - $e_g$ ($d_{xz}, d_{yz}$): strongly stabilized, non-bonding.
  - $a_{1g}$ ($d_{z^2}$): weakly stabilized or weakly antibonding due to ligand axial interactions.
  - $b_{2g}$ ($d_{xy}$): in-plane non-bonding or weakly $\\pi$-antibonding.
  - $b_{1g}^*$ ($d_{x^2-y^2}$): points directly along the $M-L$ bond vectors, strongly antibonding.
- The energy separation $\\Delta_{sp} = E(b_{1g}^*) - E(b_{2g})$ is exceptionally large for late transition metals, especially for $4d$ and $5d$ elements where ligand field splitting parameters are 40-75% larger than in $3d$ analogs.
- Filling the four lower MOs requires $4 \\times 2 = 8$ $d$-electrons. The 4 $\\sigma$-bonds contribute 8 electrons, yielding exactly 16 valence electrons:
  \\[ \\text{Total } VEC = 8 \\text{ (ligands)} + 8 \\text{ (}d^8\\text{)} = 16 \\]
- Placing 2 additional electrons into the strongly antibonding $b_{1g}^*$ ($d_{x^2-y^2}$) orbital is energetically unfavorable, making 16-electron square planar geometries thermodynamically stable and electronically saturated for $d^8$ centers.
- Prototypical examples include **Vaska's Complex** $\\text{IrCl}(\\text{CO})(\\text{PPh}_3)_2$ and **Wilkinson's Catalyst** $\\text{RhCl}(\\text{PPh}_3)_3$."""
        },
        {
            "id": "sec1_6",
            "title": "§1.6 Early Transition Metal Sub-18e Systems & Sterically Protected Complexes",
            "content": """Early transition metals (Groups 3, 4, 5: $\\text{Sc}, \\text{Ti}, \\text{Zr}, \\text{Hf}, \\text{V}, \\text{Nb}, \\text{Ta}$) frequently form stable organometallic complexes with 10 to 16 valence electrons. 

### Drivers for Sub-18-Electron Character in Early Metals:
1. **Small $d$-Electron Counts**: Early metals possess few valence $d$-electrons ($d^0$ to $d^3$). To achieve 18 electrons, an early metal would require 7 to 9 coordinated ligands.
2. **Steric Crowding & Coordination Number Limits**: Transition metals have finite covalent radii. Coordinating 7 or more bulky organic ligands incurs prohibitive steric congestion. For instance, hexamethyltungsten $\\text{W}(\\text{CH}_3)_6$ has a $d^0$ electron configuration and 6 $\\sigma$-alkyl ligands:
   \\[ VEC = 6 \\text{ (W group 6)} + 6 \\times 1 \\text{ (Me)} = 12 \\text{ electrons} \\]
   Despite having only 12 valence electrons, $\\text{W}(\\text{CH}_3)_6$ is a stable, isolable monomer adopting a trigonal prismatic geometry because adding more ligands is sterically impossible.
3. **Small Ligand Field Splitting ($\\Delta_o$)**: For early metals in high oxidation states, $\\Delta_o$ is moderate, and empty $d$-orbitals remain at accessible energy levels. Stabilization often occurs through intramolecular $\\pi$-donation from heteroatoms ($M=O, M=NR, M-OR$) or agostic interactions ($C-H \\cdots M$).
4. **Titanocene Dichloride**: $\\text{Cp}_2\\text{TiCl}_2$ features $\\text{Ti}(\\text{IV})$ ($d^0$). Counting electrons:
   \\[ VEC = 4 \\text{ (Ti)} + 2 \\times 5 \\text{ (Cp)} + 2 \\times 1 \\text{ (Cl)} = 16 \\text{ electrons} \\]
   It is fully stable as a 16-electron species and serves as an olefin polymerization precatalyst."""
        },
        {
            "id": "sec1_7",
            "title": "§1.7 Super-18-Electron Systems & Radicals (17e and 19e Intermediates)",
            "content": """Species possessing 17 or 19 valence electrons are open-shell radical complexes that play pivotal roles as reactive intermediates in electron-transfer-catalyzed organometallic transformations.

### 17-Electron Metalloradicals
A 17-electron complex has an open-shell configuration with a single unpaired electron residing in a non-bonding or weakly antibonding orbital.
- **Example: Vanadium Hexacarbonyl $\\text{V}(\\text{CO})_6$**:
  Vanadium belongs to Group 5 ($n_v = 5$). With six 2-electron CO ligands:
  \\[ VEC = 5 + 6 \\times 2 = 17 \\text{ electrons} \\]
  $\\text{V}(\\text{CO})_6$ is a paramagnetic, black-green crystalline solid. Unlike other metal carbonyls, it does not dimerize to $\\text{V}_2(\\text{CO})_{12}$ at room temperature because vanadium's ionic radius is too small to accommodate seven-coordination without prohibitive steric clash between the 12 carbonyl ligands. However, it readily undergoes one-electron reduction to form the closed-shell 18-electron anion $[\\text{V}(\\text{CO})_6]^-$.
- **Manganese Pentacarbonyl Radical $\\text{Mn}(\\text{CO})_5^\\bullet$**:
  Manganese (Group 7) yields $7 + 5 \\times 2 = 17$ electrons. It rapidly dimerizes via metal-metal bond formation to yield the 18-electron dimer $\\text{Mn}_2(\\text{CO})_{10}$.

### 19-Electron Species & Radical Chain Mechanisms
19-electron complexes place their extra electron into a high-energy, metal-ligand antibonding orbital ($e_g^*$ or $a_{1g}^*$). Consequently, they are potent one-electron reducing agents with very low oxidation potentials.
- Reduction of cobaltocene ($Cp_2\\text{Co}$, 19e, with one unpaired electron in $e_{1g}^*$) demonstrates high thermodynamic reducing power ($E_{1/2} = -1.33\\text{ V}$ vs ferrocene/ferrocenium).
- 17e and 19e intermediates accelerate ligand substitution rates by factors of $10^6$ to $10^9$ through **Electron Transfer Chain (ETC)** catalysis, lowering activation barriers relative to substitution at diamagnetic 18-electron centers."""
        },
        {
            "id": "sec1_8",
            "title": "§1.8 Systematic Electron Counting: Metal-Metal Bonds and Bridging Ligands",
            "content": """Complexes containing metal-metal bonds and bridging ligands require rigorous counting rules.

### Metal-Metal ($M-M$) Bonds
Under the Covalent Model:
- A single $M-M$ bond contributes **1 electron to each connected metal center**.
- A double $M=M$ bond contributes **2 electrons to each metal center**.
- A triple $M \\equiv M$ bond contributes **3 electrons to each metal center**.
- A quadruple $M \\equiv M$ bond contributes **4 electrons to each metal center**.

### Bridging Ligands ($\\mu_n-L$)
A ligand bridging $n$ metal centers is denoted by $\\mu_n$ (or simply $\\mu$ for $n=2$):
- **Bridging Hydride ($\\mu_2-\\text{H}$)**: Donates 1 electron total to the two metals ($\\frac{1}{2}$ electron per metal on average, or treated as a 2-center 3-electron bond where $H$ donates 1 electron and the $M-H$ bond coordinates datively to the second metal).
- **Bridging Halide ($\\mu_2-\\text{Cl}$)**: Donates 1 electron as a $\\sigma$-radical to one metal and 2 electrons via a lone pair to the second metal (3 electrons total shared across two centers).
- **Bridging Carbonyl ($\\mu_2-\\text{CO}$)**: Donates 2 electrons total (1 electron to each metal center).
- **Triply Bridging Carbonyl ($\\mu_3-\\text{CO}$)**: Donates 2 electrons total distributed among three metal atoms.

### Systematic Formula for Dinuclear Complexes
For a dinuclear complex $M_2 L_k$:
\\[ \\text{Total Valence Electrons } (TVE) = 2 n_v + \\sum \\text{ligand electrons} - q \\]
The predicted number of metal-metal bonds ($m$) necessary to satisfy the 18-electron rule for both metal centers is:
\\[ m = \\frac{18 \\times 2 - TVE}{2} = \\frac{36 - TVE}{2} \\]
For a cluster containing $n$ metal centers:
\\[ m = \\frac{18n - TVE}{2} \\]
where $m$ is the total count of localized 2-center 2-electron metal-metal bonds."""
        }
    ]

    problems = [
        {
            "id": "prob1_1",
            "tier": "Foundational",
            "title": "Electron Counting of Homoleptic Binary Metal Carbonyls",
            "statement": "Determine the valence electron count ($VEC$) for the following monomeric metal carbonyl complexes using both the Covalent and Ionic models: (a) $\\text{Cr}(\\text{CO})_6$, (b) $\\text{Fe}(\\text{CO})_5$, (c) $\\text{Ni}(\\text{CO})_4$. State whether each complex satisfies the 18-electron rule.",
            "solution": """**Line-by-Line Solution:**

**(a) Chromium Hexacarbonyl $\\text{Cr}(\\text{CO})_6$:**
- **Covalent Model**:
  - Chromium is in Group 6: $n_v = 6$.
  - CO is a neutral 2-electron donor ($L$-type): $6 \\times 2 = 12$ electrons.
  - Overall charge $q = 0$.
  \\[ VEC = 6 + 12 = 18 \\text{ electrons} \\]
- **Ionic Model**:
  - CO ligands are neutral ($L$); formal charge on ligand is 0.
  - Oxidation state of Cr: $OS = 0 - 0 = 0 \\implies d^6$.
  - Total electrons: $6 + (6 \\times 2) = 18$ electrons.
- **Rule Assessment**: Satisfies the 18-electron rule.

**(b) Iron Pentacarbonyl $\\text{Fe}(\\text{CO})_5$:**
- **Covalent Model**:
  - Iron is in Group 8: $n_v = 8$.
  - CO ligands donate: $5 \\times 2 = 10$ electrons.
  \\[ VEC = 8 + 10 = 18 \\text{ electrons} \\]
- **Ionic Model**:
  - $OS = 0 \\implies d^8$.
  - $VEC = 8 + (5 \\times 2) = 18$ electrons.
- **Rule Assessment**: Satisfies the 18-electron rule.

**(c) Nickel Tetracarbonyl $\\text{Ni}(\\text{CO})_4$:**
- **Covalent Model**:
  - Nickel is in Group 10: $n_v = 10$.
  - CO ligands donate: $4 \\times 2 = 8$ electrons.
  \\[ VEC = 10 + 8 = 18 \\text{ electrons} \\]
- **Ionic Model**:
  - $OS = 0 \\implies d^{10}$.
  - $VEC = 10 + (4 \\times 2) = 18$ electrons.
- **Rule Assessment**: Satisfies the 18-electron rule."""
        },
        {
            "id": "prob1_2",
            "tier": "Foundational",
            "title": "Valence Electron Count of Metallocene Systems",
            "statement": "Calculate the total valence electron count ($VEC$) for the following metallocene complexes: (a) Ferrocene $\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_5)_2$, (b) Cobaltocene $\\text{Co}(\\eta^5-\\text{C}_5\\text{H}_5)_2$, (c) Nickelocene $\\text{Ni}(\\eta^5-\\text{C}_5\\text{H}_5)_2$. Identify which are closed-shell and which are paramagnetic radicals.",
            "solution": """**Line-by-Line Solution:**

**(a) Ferrocene $\\text{Fe}(\\eta^5-\\text{C}_5\\text{H}_5)_2$:**
- Group number of $\\text{Fe}$: $n_v = 8$.
- Each $\\eta^5-\\text{C}_5\\text{H}_5$ ($Cp$) ring contributes 5 electrons in the neutral model ($L_2X$): $2 \\times 5 = 10$ electrons.
\\[ VEC = 8 + 10 = 18 \\text{ electrons} \\]
- Closed-shell, 18-electron diamagnetic complex. Highly stable ($T_m = 173^\\circ\\text{C}$).

**(b) Cobaltocene $\\text{Co}(\\eta^5-\\text{C}_5\\text{H}_5)_2$:**
- Group number of $\\text{Co}$: $n_v = 9$.
- Two $Cp$ rings donate $2 \\times 5 = 10$ electrons.
\\[ VEC = 9 + 10 = 19 \\text{ electrons} \\]
- Possesses 19 valence electrons; the 19th electron resides in an antibonding $e_{1g}^*$ orbital.
- Open-shell paramagnetic radical (1 unpaired electron, $\\mu_{eff} \\approx 1.73\\ \\mu_B$). Potent 1-electron reducing agent.

**(c) Nickelocene $\\text{Ni}(\\eta^5-\\text{C}_5\\text{H}_5)_2$:**
- Group number of $\\text{Ni}$: $n_v = 10$.
- Two $Cp$ rings donate $2 \\times 5 = 10$ electrons.
\\[ VEC = 10 + 10 = 20 \\text{ electrons} \\]
- Possesses 20 valence electrons; 2 electrons reside in degenerate $e_{1g}^*$ antibonding orbitals.
- Triplet ground state with 2 unpaired electrons (paramagnetic, $\\mu_{eff} \\approx 2.83\\ \\mu_B$). Readily oxidized or cleaved by acids."""
        },
        {
            "id": "prob1_3",
            "tier": "Foundational",
            "title": "Electron Counting in Square Planar Complexes",
            "statement": "For Vaska's complex $\\text{trans}-[\\text{IrCl}(\\text{CO})(\\text{PPh}_3)_2]$, calculate: (a) metal oxidation state, (b) $d$-electron count, (c) total valence electron count ($VEC$), and (d) explain why this 16-electron complex does not spontaneously coordinate a fifth ligand at room temperature.",
            "solution": """**Line-by-Line Solution:**

**(a) Oxidation State of Iridium:**
- Chloride ($\\text{Cl}$) is a monoanionic $X$-ligand (formal charge $-1$).
- $\\text{CO}$ is a neutral $L$-ligand (formal charge $0$).
- $\\text{PPh}_3$ are neutral $L$-ligands (formal charge $0$).
- Overall complex charge $q = 0$.
\\[ OS = 0 - (-1) = +1 \\implies \\text{Ir}(\\text{I}) \\]

**(b) $d$-Electron Count:**
- Iridium is in Group 9 ($n_v = 9$).
\\[ d^n = n_v - OS = 9 - 1 = 8 \\implies d^8 \\]

**(c) Total Valence Electron Count ($VEC$):**
- $\\text{Ir}(\\text{I})$: 8 electrons.
- $\\text{Cl}^-$: 2 electrons (ionic model) or 1 electron (covalent model).
- $\\text{CO}$: 2 electrons.
- Two $\\text{PPh}_3$: $2 \\times 2 = 4$ electrons.
\\[ VEC = 8 + 2 + 2 + 4 = 16 \\text{ electrons} \\]

**(d) Stability of the 16e Configuration:**
- For a $5d^8$ metal center in square planar geometry ($D_{4h}$ symmetry), the crystal field splitting parameter $\\Delta_{sp}$ between the highest occupied non-bonding $d_{xy}$ orbital and the strongly antibonding empty $d_{x^2-y^2}$ orbital ($b_{1g}^*$) is exceptionally large.
- Coordinating a fifth ligand to form a 5-coordinate 18-electron adduct requires extensive reorganization of the ligand field and significant steric accommodation of bulky triphenylphosphine ligands. The 16e square planar geometry is electronically stable."""
        },
        {
            "id": "prob1_4",
            "tier": "Intermediate",
            "title": "Predicting Metal-Metal Bond Orders in Dinuclear Carbonyls",
            "statement": "Apply the 18-electron rule to determine the number of formal metal-metal bonds ($M-M$) in the following homoleptic dinuclear complexes: (a) $\\text{Mn}_2(\\text{CO})_{10}$, (b) $\\text{Fe}_2(\\text{CO})_9$, (c) $\\text{Co}_2(\\text{CO})_8$. Provide complete electron accounting for each metal center.",
            "solution": """**Line-by-Line Solution:**

**(a) Decacarbonyldimanganese $\\text{Mn}_2(\\text{CO})_{10}$:**
- Total Valence Electrons ($TVE$):
  - $2 \\times \\text{Mn}$ (Group 7): $2 \\times 7 = 14$
  - $10 \\times \\text{CO}$ ($L$-donor): $10 \\times 2 = 20$
  \\[ TVE = 14 + 20 = 34 \\]
- Metal-Metal Bond Formula:
  \\[ m = \\frac{18 \\times 2 - TVE}{2} = \\frac{36 - 34}{2} = 1 \\]
- **Conclusion**: Exactly one $\\text{Mn}-\\text{Mn}$ single bond exists ($m = 1$). No bridging carbonyls are present in the ground state ($D_{4d}$ staggered structure). Each Mn has: $7 + (5 \\times 2) + 1 (\\text{Mn-Mn}) = 18\\text{e}$.

**(b) Nonacarbonyldiiron $\\text{Fe}_2(\\text{CO})_9$:**
- Total Valence Electrons:
  - $2 \\times \\text{Fe}$ (Group 8): $2 \\times 8 = 16$
  - $9 \\times \\text{CO}$: $9 \\times 2 = 18$
  \\[ TVE = 16 + 18 = 34 \\]
- Metal-Metal Bond Formula:
  \\[ m = \\frac{36 - 34}{2} = 1 \\]
- **Conclusion**: Exactly one $\\text{Fe}-\\text{Fe}$ single bond exists ($m = 1$). The complex possesses three bridging $\\mu_2-\\text{CO}$ ligands and six terminal CO ligands ($(\\text{OC})_3\\text{Fe}(\\mu-\\text{CO})_3\\text{Fe}(\\text{CO})_3$).
- Per Fe electron count: $8 (\\text{Fe}) + 3 \\times 2 (\\text{terminal CO}) + 3 \\times 1 (\\mu-\\text{CO}) + 1 (\\text{Fe-Fe}) = 18\\text{e}$.

**(c) Octacarbonyldicobalt $\\text{Co}_2(\\text{CO})_8$:**
- Total Valence Electrons:
  - $2 \\times \\text{Co}$ (Group 9): $2 \\times 9 = 18$
  - $8 \\times \\text{CO}$: $8 \\times 2 = 16$
  \\[ TVE = 18 + 16 = 34 \\]
- Metal-Metal Bond Formula:
  \\[ m = \\frac{36 - 34}{2} = 1 \\]
- **Conclusion**: Exactly one $\\text{Co}-\\text{Co}$ single bond exists ($m = 1$). In the solid state, it exists as a bridged isomer with two $\\mu_2-\\text{CO}$ and six terminal CO ligands: per Co count $= 9 + 3 \\times 2 + 2 \\times 1 + 1 = 18\\text{e}$."""
        },
        {
            "id": "prob1_5",
            "tier": "Intermediate",
            "title": "Electron Counting with Ambidentate and Bridging Halide Ligands",
            "statement": "The dimer $[(\\eta^6-\\text{C}_6\\text{H}_6)\\text{RuCl}_2]_2$ is a widely utilized synthetic precursor in catalysis. (a) Determine the formal oxidation state of ruthenium. (b) Calculate the valence electron count ($VEC$) per ruthenium atom assuming bridging chlorides. (c) Predict whether the complex possesses a metal-metal bond.",
            "solution": """**Line-by-Line Solution:**

**(a) Formal Oxidation State of Ruthenium:**
- Benzene ($\\eta^6-\\text{C}_6\\text{H}_6$) is a neutral 6-electron $L_3$ ligand.
- Four chloride ligands are present across the dimer. As $X$-ligands, each carries a formal $-1$ charge.
- Overall complex charge $q = 0$.
\\[ 2 \\times OS(\\text{Ru}) + 4(-1) = 0 \\implies OS(\\text{Ru}) = +2 \\]
- The metal centers are $\\text{Ru}(\\text{II})$ ($d^6$).

**(b) Valence Electron Count per Ruthenium Center:**
- Structure: Each ruthenium is coordinated to one $\\eta^6-\\text{C}_6\\text{H}_6$ ring and bridged by two chloride ligands (or shared equally).
- Under the Covalent Model per Ru atom:
  - $\\text{Ru}$ (Group 8): 8 electrons
  - $\\eta^6-\\text{C}_6\\text{H}_6$: 6 electrons
  - Two terminal/bridging $\\text{Cl}$ atoms: each bridging chloride donates 1 electron via a $\\sigma$-covalent bond to one Ru and 2 electrons via a dative lone pair to the second Ru. Across the dimer, two bridging chlorides donate $2 \\times 3 = 6$ electrons total, or 3 electrons per Ru center.
  - Plus one terminal chloride per Ru: 1 electron.
  - Total electrons per Ru:
    \\[ VEC = 8 (\\text{Ru}) + 6 (\\text{benzene}) + 2 \\times 1.5 (\\mu-\\text{Cl}) + 1 (\\text{terminal Cl}) \\]
  - Wait, in $[(\\eta^6-\\text{C}_6\\text{H}_6)\\text{Ru}(\\mu-\\text{Cl})_2]_2$, there are four chlorides total, all four are bridging $\\mu_2-\\text{Cl}$!
  - Let's check stoichiometry: $[(\\text{benzene})\\text{RuCl}_2]_2 = \\text{Ru}_2(\\text{benzene})_2\\text{Cl}_4$.
  - In the solid state, it is $[(\\eta^6-\\text{C}_6\\text{H}_6)\\text{Ru}(\\mu-\\text{Cl})_2\\text{Cl}]$? No, it forms a piano-stool dimer with two bridging chlorides and two terminal chlorides: $[(\\eta^6-\\text{C}_6\\text{H}_6)\\text{RuCl}(\\mu-\\text{Cl})]_2$.
  - Let's count per Ru:
    - Ru(II) core: 8 valence electrons (covalent)
    - $\\eta^6-\\text{C}_6\\text{H}_6$: 6 electrons
    - Terminal $\\text{Cl}$: 1 electron
    - Bridging $\\mu-\\text{Cl}$ (donor of 3e across two Ru): 1.5 electrons on average, or 1e ($\sigma$) + 2e (dative) $= 3$ electrons from the two bridging ligands.
    - Total per Ru: $8 + 6 + 1 + (1 + 2) = 18$ electrons!

**(c) Metal-Metal Bond Assessment:**
- Total Valence Electrons ($TVE$) of the dimer:
  \\[ TVE = 2 \\times 8 (\\text{Ru}) + 2 \\times 6 (\\text{arene}) + 4 \\times 1 (\\text{Cl}) = 16 + 12 + 4 = 32 \\text{ (covalent model: } 4 \\text{ Cl radicals } = 4\\text{e} + 2 \\text{ lone pairs from 2 bridging Cl} = 4\\text{e}) \\implies TVE = 36 \\]
- Let's verify: per Ru $VEC = 18$, so $2 \\times 18 = 36$.
- Number of $M-M$ bonds:
  \\[ m = \\frac{36 - TVE}{2} = \\frac{36 - 36}{2} = 0 \\]
- **Conclusion**: There is **no metal-metal bond** ($m = 0$). The complex is fully saturated at 18 valence electrons per Ru purely through bridging chloride coordination."""
        },
        {
            "id": "prob1_6",
            "tier": "Intermediate",
            "title": "Hapticity Shifts and Electron Counting During Ligand Substitution",
            "statement": "The reaction of indenyl complex $(\\eta^5-\\text{C}_9\\text{H}_7)\\text{Rh}(\\text{CO})_2$ with triethylphosphine $\\text{P(Et)}_3$ occurs $10^8$ times faster than the corresponding cyclopentadienyl complex $(\\eta^5-\\text{C}_5\\text{H}_5)\\text{Rh}(\\text{CO})_2$. (a) Calculate the $VEC$ of $(\\eta^5-\\text{C}_9\\text{H}_7)\\text{Rh}(\\text{CO})_2$. (b) Explain the kinetic origin of the 'indenyl effect' by tracking electron counts during associative substitution.",
            "solution": """**Line-by-Line Solution:**

**(a) Valence Electron Count of Starting Complex:**
- Rhodium is in Group 9: $n_v = 9$.
- $\\eta^5-\\text{C}_9\\text{H}_7$ (indenyl) is a 5-electron donor ($L_2X$): 5 electrons.
- Two CO ligands: $2 \\times 2 = 4$ electrons.
\\[ VEC = 9 + 5 + 4 = 18 \\text{ electrons} \\]
- The starting complex is an 18-electron saturated complex.

**(b) Kinetic Origin of the Indenyl Effect:**
1. **Associative Mechanism Requirement**:
   - Because the complex has 18 electrons, attack by incoming nucleophile $\\text{PEt}_3$ must proceed through an associative pathway to avoid high-energy dissociative CO loss.
   - Associative attack on an 18e center would generate a 20e intermediate unless an existing ligand reduces its donor count.
2. **Hapticity Ring Slipping**:
   - To accommodate incoming $\\text{PEt}_3$ (a 2e donor) while maintaining an 18e count:
   \\[ \\eta^5-\\text{indenyl (5e)} + \\text{PEt}_3 (2\\text{e}) \\longrightarrow \\eta^3-\\text{indenyl (3e)} \\text{ intermediate (18e)} \\]
   - The ring slips from pentahapto ($\\eta^5$) to trihapto ($\\eta^3$).
3. **Aromatic Resonance Driving Force**:
   - For cyclopentadienyl ($Cp$), slipping from $\\eta^5$ to $\\eta^3$ disrupts the $6\\pi$-electron aromatic sextet of the ring, creating an allylic anion fragment with high thermodynamic loss of aromatic stabilization energy ($\\approx 110\\text{ kJ/mol}$).
   - For indenyl ($\\text{C}_9\\text{H}_7$), slipping from $\\eta^5$ to $\\eta^3$ restores a fully aromatic benzene sextet ($6\\pi$ electrons) in the fused benzo ring!
   - This aromatic restoration compensates for the loss of metal-ring bonding, drastically lowering the activation energy barrier $\\Delta G^\\ddagger$ for ring slipping.
   - Consequently, associative substitution in indenyl complexes is accelerated by up to eight orders of magnitude ($10^8$)."""
        },
        {
            "id": "prob1_7",
            "tier": "Advanced",
            "title": "Formal Molecular Orbital Derivation of the 18e Rule for $ML_6$ Complexes",
            "statement": "Derive the mathematical expression for the total stabilization energy of an octahedral $ML_6$ complex with $\\sigma$-donor and strong $\\pi$-acceptor ligands. Prove why 18 electrons represents the absolute global electronic thermodynamic minimum, and show why populating the 19th electron incurs a severe energetic penalty quantified by $\\Delta_o$.",
            "solution": """**Line-by-Line Solution:**

**1. Symmetry-Adapted Linear Combinations (SALCs) and Overlap:**
Under octahedral point group $O_h$, the nine metal valence orbitals span:
\\[ \\Gamma_{\\text{metal}} = a_{1g} (s) + t_{1u} (p_x, p_y, p_z) + e_g (d_{z^2}, d_{x^2-y^2}) + t_{2g} (d_{xy}, d_{yz}, d_{xz}) \\]
The six ligand $\\sigma$-lone pairs form LGOs spanning:
\\[ \\Gamma_\\sigma = a_{1g} + e_g + t_{1u} \\]
The twelve ligand $\\pi^*$ antibonding orbitals span:
\\[ \\Gamma_{\\pi^*} = t_{1g} + t_{2g} + t_{1u} + t_{2u} \\]

**2. Secular Determinant & Eigenvalue Equations:**
For each irreducible representation $\\Gamma_i$, the molecular orbital energies $E_i$ are solutions to:
\\[ \\det \\begin{pmatrix} H_{MM} - E & H_{ML} - E S_{ML} \\\\ H_{ML} - E S_{ML} & H_{LL} - E \\end{pmatrix} = 0 \\]
From second-order perturbation theory, assuming weak overlap $S_{ML} \\ll 1$:
- For $a_{1g}$: $\\epsilon(1a_{1g}) = H_{LL} - \\frac{|H_{ML}(a_{1g})|^2}{H_{MM}(s) - H_{LL}}$
- For $t_{1u}$: $\\epsilon(1t_{1u}) = H_{LL} - \\frac{|H_{ML}(t_{1u})|^2}{H_{MM}(p) - H_{LL}}$ (threefold degenerate)
- For $e_g$: $\\epsilon(1e_g) = H_{LL} - \\frac{|H_{ML}(e_g)|^2}{H_{MM}(d) - H_{LL}}$ (twofold degenerate)
These six bonding MOs accommodate $2 \\times (1 + 3 + 2) = 12$ electrons.

**3. The $t_{2g}$ $\\pi$-Backbonding Interaction:**
The metal $d_{xy}, d_{yz}, d_{xz}$ orbitals ($t_{2g}$) interact with the empty $\\pi^*$ LGOs of $t_{2g}$ symmetry:
\\[ \\epsilon(t_{2g}) = H_{MM}(d) - \\frac{|H_{M\\pi}(t_{2g})|^2}{E(\\pi^*) - H_{MM}(d)} \\]
Because $E(\\pi^*) > H_{MM}(d)$, the denominator is positive, depressing the $t_{2g}$ orbital by energy $\\delta_{\\pi}$:
\\[ \\epsilon(t_{2g}) = \\epsilon_d^0 - \\delta_\\pi \\]
Simultaneously, the ligand $\\sigma$-antibonding $e_g^*$ orbital is elevated:
\\[ \\epsilon(e_g^*) = H_{MM}(d) + \\frac{|H_{ML}(e_g)|^2}{H_{MM}(d) - H_{LL}} = \\epsilon_d^0 + \\delta_\\sigma \\]

**4. Total Electronic Energy as a Function of Electron Count $N$:**
The ligand field splitting is:
\\[ \\Delta_o = \\epsilon(e_g^*) - \\epsilon(t_{2g}) = \\delta_\\sigma + \\delta_\\pi \\]
For $N \\le 18$, the total electronic energy is:
\\[ E(N) = \\sum_{i=1}^6 2 \\epsilon(\\sigma_i) + (N - 12) \\epsilon(t_{2g}) \\]
Since $\\epsilon(t_{2g}) < 0$ relative to isolated metal ions, each electron added from $N = 13$ to $N = 18$ stabilizes the complex by $\\epsilon(t_{2g})$.
At $N = 18$, the $t_{2g}$ level is fully populated with 6 electrons, and all 9 bonding/stabilized orbitals are completely filled:
\\[ E(18) = E_\\sigma + 6(\\epsilon_d^0 - \\delta_\\pi) \\]

**5. Energy Penalty for Populating Beyond 18 Electrons:**
For $N = 19$, the extra electron must occupy the strongly antibonding $e_g^*$ orbital:
\\[ E(19) = E(18) + \\epsilon(e_g^*) = E(18) + \\epsilon(t_{2g}) + \\Delta_o \\]
The difference in electronic addition energy is:
\\[ \\Delta E_{\\text{add}} = E(19) - E(18) = \\epsilon_d^0 + \\delta_\\sigma \\gg 0 \\]
Because $\\Delta_o$ for strong $\\pi$-acceptors like $\\text{CO}$ exceeds $250\\text{ kJ/mol}$ ($> 20,000\\text{ cm}^{-1}$), the addition of a 19th electron destabilizes the complex by $\\Delta_o$, making 18 electrons the definitive thermodynamic boundary."""
        },
        {
            "id": "prob1_8",
            "tier": "Advanced",
            "title": "Electronic Structure and Stability of Paramagnetic Vanadium Hexacarbonyl",
            "statement": "Vanadium hexacarbonyl $\\text{V}(\\text{CO})_6$ is a rare isolable 17-electron homoleptic metal carbonyl. (a) Provide its exact electron configuration under octahedral symmetry. (b) Explain why Jahn-Teller distortion occurs in $\\text{V}(\\text{CO})_6$. (c) Derive why $\\text{V}(\\text{CO})_6$ does not dimerize to form $\\text{V}_2(\\text{CO})_{12}$, while $\\text{Mn}(\\text{CO})_5$ spontaneously forms $\\text{Mn}_2(\\text{CO})_{10}$.",
            "solution": """**Line-by-Line Solution:**

**(a) Electron Configuration:**
- Vanadium has atomic number 23 (Group 5, $n_v = 5$).
- In $\\text{V}(\\text{CO})_6$, vanadium is in formal oxidation state $0$ ($d^5$).
- In an octahedral field with strong-field $\\text{CO}$ ligands, $\\Delta_o \\gg P$ (pairing energy).
- The low-spin configuration is:
  \\[ (a_{1g})^2 (t_{1u})^6 (e_g)^4 \\; [\\text{ligand-based } 12\\text{e}] \\; (t_{2g})^5 \\; (e_g^*)^0 \\]
- Metal $d$-electron configuration: $t_{2g}^5$.
- Total valence electrons: $12 + 5 = 17$ electrons.
- Unpaired electrons: exactly 1 in the $t_{2g}$ manifold, yielding $S = 1/2$ and $\\mu_{eff} = \\sqrt{1(3)} \\mu_B = 1.73\\ \\mu_B$.

**(b) Jahn-Teller Distortion:**
- The ground electronic state is $^2T_{2g}$, which is orbitally degenerate (threefold degenerate ground term arising from an odd hole in the $t_{2g}$ subshell).
- According to the Jahn-Teller theorem, any non-linear molecule with an orbitally degenerate electronic ground state undergoes spontaneous geometric distortion to lower its symmetry and remove the degeneracy.
- In $\\text{V}(\\text{CO})_6$, a tetragonal elongation or compression along the $z$-axis occurs ($O_h \\to D_{4h}$), splitting $t_{2g}$ into $e_g$ ($d_{xz}, d_{yz}$) and $b_{2g}$ ($d_{xy}$).
- The hole localizes in the higher-energy split orbital, lowering the net electronic ground-state energy. High-resolution gas-phase electron diffraction confirms a small dynamic Jahn-Teller tetragonal distortion of $\\approx 0.05$ Å in the $\\text{V}-\\text{C}$ bond lengths.

**(c) Thermodynamic Resistance to Dimerization:**
- Dimerization of $\\text{Mn}(\\text{CO})_5$ ($17\\text{e}$) to $\\text{Mn}_2(\\text{CO})_{10}$ ($18\\text{e}$ per Mn) proceeds smoothly because $\\text{Mn}(\\text{CO})_5$ is 5-coordinate. Dimerization produces a 6-coordinate octahedral geometry around each Mn, which easily fits within the steric coordination envelope of manganese (covalent radius $\\approx 1.39$ Å).
- For $\\text{V}(\\text{CO})_6$, dimerization to $\\text{V}_2(\\text{CO})_{12}$ would require each vanadium atom to become **7-coordinate** (either by forming an unsupported $\\text{V}-\\text{V}$ bond between two pentagonal bipyramidal centers or through bridging carbonyls).
- The covalent radius of vanadium is $1.34$ Å. Packing seven ligands (including bulky carbonyl groups) around a small $3d$ transition metal ion produces prohibitive steric repulsion:
  \\[ \\Delta G_{\\text{dimer}} = \\Delta H_{\\text{bond}} - T\\Delta S_{\\text{dimer}} + \\Delta G_{\\text{steric}} > 0 \\]
  The steric repulsion penalty $\\Delta G_{\\text{steric}}$ exceeds the bond enthalpy gain of the single $\\text{V}-\\text{V}$ bond ($\\approx 100-130\\text{ kJ/mol}$). Therefore, $\\text{V}(\\text{CO})_6$ remains monomeric."""
        },
        {
            "id": "prob1_9",
            "tier": "Advanced",
            "title": "Multi-Center Bonding and Electron Counting in Bridging Alkyl Dimers",
            "statement": "Trimethylaluminum $\\text{Al}_2(\\text{CH}_3)_6$ is a dimer at room temperature exhibiting 3-center 2-electron ($3c-2e$) bonds. (a) Deduce the valence electron count for each aluminum atom in the monomer $\\text{Al}(\\text{CH}_3)_3$ versus the dimer $\\text{Al}_2(\\text{CH}_3)_6$. (b) Construct the molecular orbital linear combinations for the $\\text{Al}-(\\mu-\\text{CH}_3)-\\text{Al}$ bridging unit and show how two electrons achieve bonding stability across three atomic nuclei. (c) Derive the thermodynamic equilibrium constant expression for dimer dissociation.",
            "solution": """**Line-by-Line Solution:**

**(a) Valence Electron Counting for Monomer vs. Dimer:**
- **Monomer $\\text{Al}(\\text{CH}_3)_3$**:
  - Aluminum is a Group 13 element: 3 valence electrons ($3s^2 3p^1$).
  - Three methyl radicals donate 1 electron each: $3 \\times 1 = 3$ electrons.
  \\[ VEC(\\text{monomer}) = 3 + 3 = 6 \\text{ electrons} \\]
  - The monomer is a planar, electron-deficient Lewis acid with a vacant $3p_z$ orbital, possessing an open sextet (sub-octet).
- **Dimer $\\text{Al}_2(\\text{CH}_3)_6$**:
  - Contains two terminal methyl groups per Al atom and two bridging methyl groups: $(\\text{H}_3\\text{C})_2\\text{Al}(\\mu-\\text{CH}_3)_2\\text{Al}(\\text{CH}_3)_2$.
  - Each terminal $\\text{Al}-\\text{CH}_3$ is a standard 2-center 2-electron ($2c-2e$) bond.
  - The two bridging methyl carbons form two $3c-2e$ bonds with both Al atoms.
  - Each bridging methyl donates 1 electron shared across the two Al atoms.
  - Per Aluminum atom:
    - 3 valence electrons from Al
    - $2 \\times 1 = 2$ electrons from terminal methyls
    - Two bridging methyls contribute 1 electron each to the shared bridge system: $2 \\times 1 = 2$ electrons (from Al perspective, 4 electrons total in two $3c-2e$ bonds shared equally $= 2$ electrons per Al).
    - Plus one coordination pair from the bridge:
    - Formal octet count per Al:
    \\[ VEC(\\text{dimer}) = 2 \\times 2 (\\text{terminal}) + 2 \\times 2 (\\text{bridges}) = 8 \\text{ electrons} \\]
  - Both aluminum centers achieve closed-shell octet configurations!

**(b) Molecular Orbital Construction of the $3c-2e$ $\\text{Al}_2\\text{C}$ Bridge:**
- Let the two aluminum atoms have directed $sp^3$ hybrid orbitals $\\phi_{\\text{Al1}}$ and $\\phi_{\\text{Al2}}$ pointing toward the bridging carbon.
- The bridging carbon atom provides an $sp^3$ hybrid orbital $\\phi_{\\text{C}}$ directed between the two Al atoms.
- Three molecular orbitals are constructed from these three basis orbitals:
  1. **Bonding MO ($\\psi_1$)**:
     \\[ \\psi_1 = c_1 \\phi_{\\text{C}} + c_2 (\\phi_{\\text{Al1}} + \\phi_{\\text{Al2}}) \\quad (c_1 > 0, c_2 > 0) \\]
     This MO is strongly bonding across all three centers with no nodal planes between Al and C.
  2. **Non-Bonding MO ($\\psi_2$)**:
     \\[ \\psi_2 = \\frac{1}{\\sqrt{2}} (\\phi_{\\text{Al1}} - \\phi_{\\text{Al2}}) \\]
     Possesses a nodal plane passing through the carbon atom; non-bonding with respect to C.
  3. **Antibonding MO ($\\psi_3$)**:
     \\[ \\psi_3 = c_3 \\phi_{\\text{C}} - c_4 (\\phi_{\\text{Al1}} + \\phi_{\\text{Al2}}) \\]
     Possesses nodal planes between C and both Al centers.
- **Electron Population**: The bridging methyl contributes 1 electron, and the aluminum atoms contribute 1 electron collectively to each bridge, giving **exactly 2 electrons** per $\\text{Al}_2\\text{C}$ unit.
- These two electrons fully occupy the strongly bonding $\\psi_1$ MO.
- Net result: A net bonding interaction binding three atomic nuclei together with only two electrons ($3c-2e$ bond), yielding an acute $\\text{Al}-\\text{C}-\\text{Al}$ angle of $\\approx 75^\\circ$.

**(c) Thermodynamic Dimer Dissociation Equilibrium:**
For the gas-phase or solution equilibrium:
\\[ \\text{Al}_2(\\text{CH}_3)_6 \\rightleftharpoons 2\\, \\text{Al}(\\text{CH}_3)_3 \\]
Let $C_0$ be initial concentration of dimer and $\\alpha$ be the degree of dissociation:
\\[ [\\text{Al}_2(\\text{CH}_3)_6] = C_0 (1 - \\alpha), \\quad [\\text{Al}(\\text{CH}_3)_3] = 2 C_0 \\alpha \\]
The equilibrium constant is:
\\[ K_d = \\frac{[\\text{Al}(\\text{CH}_3)_3]^2}{[\\text{Al}_2(\\text{CH}_3)_6]} = \\frac{4 C_0^2 \\alpha^2}{C_0(1 - \\alpha)} = \\frac{4 C_0 \\alpha^2}{1 - \\alpha} \\]
Solving for $\\alpha$:
\\[ 4 C_0 \\alpha^2 + K_d \\alpha - K_d = 0 \\implies \\alpha = \\frac{-K_d + \\sqrt{K_d^2 + 16 C_0 K_d}}{8 C_0} \\]
Experimentally in benzene at $298\\text{ K}$, $\\Delta H_d^\\circ \\approx +84\\text{ kJ/mol}$ and $\\Delta S_d^\\circ \\approx +130\\text{ J/(mol}\\cdot\\text{K)}$, confirming that dimerization is strongly enthalpically favored by the formation of two $3c-2e$ bridge bonds ($2 \\times 42\\text{ kJ/mol}$)."""
        }
    ]

    return {
        "unit_number": 1,
        "title": "Fundamentals of Organometallic Chemistry & Electron Counting",
        "description": "Historical development of organometallic chemistry, definitions and bond types, covalent (neutral) and ionic ligand classification models, the CBC framework, molecular orbital derivation of the 18-electron rule, sub-18-electron and super-18-electron complexes, 16-electron square planar d8 systems, electron counting in dinuclear clusters with metal-metal bonds and bridging ligands, and 3-center 2-electron bonding.",
        "sections": sections,
        "problems": problems
    }
