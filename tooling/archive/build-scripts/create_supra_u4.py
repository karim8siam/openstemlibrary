"""
create_supra_u4.py
Creates Unit 4 data dictionary for Supramolecular Chemistry:
Mechanically Interlocked Molecules: Catenanes, Rotaxanes & Molecular Knots
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_4():
    sections = [
        {
            "secNumber": "4.1",
            "title": "Topological Chemistry & Mechanical Bonds: Catenanes, Rotaxanes, and Knots",
            "content": """Topological chemistry explores molecules whose identity and spatial connectivity are defined not merely by covalent bonds between atomic nuclei, but by physical entanglements in three-dimensional Euclidean space that cannot be disentangled without breaking one or more covalent bonds. Such species are known as **Mechanically Interlocked Molecular Architectures (MIMAs)**.

### The Mechanical Bond
In 1961, Frisch and Wasserman coined the concept of "chemical topology," proposing that two interlocked macrocyclic rings constitute an entropic and mechanical linkage without sharing a single valence electron pair between them. This link is formally designated the **mechanical bond**.
- While covalent bonds possess bond energies ranging from $200\\text{ to }450\\text{ kJ/mol}$ and strict directional orbital overlap, the mechanical bond possesses an effective dissociation energy equal to the energy required to homolytically cleave whichever covalent bond forms the weakest link in the interlocked ring or dumbbell component ($>300\\text{ kJ/mol}$).
- Unlike classical covalent bonds, components linked by mechanical bonds retain large internal degrees of freedom, including relative circumrotation (pirouetting) and long-range translation (shuttling).

### Core Interlocked Taxa
1. **[n]Catenanes**: Compounds consisting of $n$ macrocyclic rings interlocked like links in a chain. A [2]catenane comprises two mutually threaded rings. The uncomplexed macrocyclic ligand of a catenane is termed a **catenand**, whereas the coordination complex with an entrapped metal cation is termed a **catenate**.
2. **[n]Rotaxanes**: Consist of a linear dumbbell-shaped shaft encircled by $n-1$ macrocyclic rings. Bulky terminal groups, known as **stoppers** or **caps**, sterically prevent the macrocycles from dethreading. The cyclic ring is usually termed the macrocycle or wheel. If the stoppers are absent or too small to prevent dissociation at room temperature, the species is a **pseudorotaxane**.
3. **Molecular Knots (Knotanes)**: A single continuous, covalently closed molecular strand that is tied into an open knot in space before its ends are covalently fused. The simplest nontrivial molecular knot is the **trefoil knot** ($3_1$ knot in Alexander-Briggs notation).
4. **Molecular Borromean Rings**: A topological link consisting of three closed macrocycles entangled such that no two rings are interlocked on their own (the pairwise linking number is zero, $Lk_{ij} = 0$), yet the three together cannot be pulled apart. Cleaving any single loop causes the remaining two to fall apart immediately.

### Topological Stereochemistry and Isomerism
Because components cannot traverse one another, MIMAs display forms of stereoisomerism unique to topology:
- **Topological Chirality**: Arises when a molecule cannot be deformed into its mirror image in 3D space by any continuous deformation (isotopy) without bond cleavage, even if each constituent ring has an achiral Euclidean point group.
- **Topological Isomers**: Molecules having identical covalent connectivity graphs but distinct topological embedding states in $\\mathbb{R}^3$ (e.g., an unknotted macrocycle vs. a trefoil knot made from the identical molecular strand)."""
        },
        {
            "secNumber": "4.2",
            "title": "Sauvage Cu(I)-Template Synthesis of [2]Catenanes and Catenands",
            "content": """Prior to 1983, synthesis of catenanes relied on low-yielding statistical cyclization (such as Wasserman's $1\\%$ yield cyclization of diesters in the presence of deuterated macrocycles). In 1983, Jean-Pierre Sauvage revolutionized topological chemistry by introducing **passive metal-template synthesis** using tetrahedral copper(I) centers.

### The Cu(I)-Phenanthroline Orthogonal Motif
Sauvage exploited the stereoelectronic preference of monovalent copper ($d^{10}$, $\\text{Cu}^I$) for a four-coordinate, pseudo-tetrahedral geometry with bidentate chelating ligands such as 1,10-phenanthroline (phen):
\\[
\\text{Cu}^+ + 2\\,\\text{phen} \\xrightleftharpoons{} [\\text{Cu}(\\text{phen})_2]^+
\\]
When two phenanthroline units coordinate to a single $\\text{Cu}^I$ cation, their rigid heterocyclic planes are held mutually perpendicular (at an angle $\\theta \\approx 90^\\circ$), mutually intersecting in space.

### Synthetic Strategy for [2]Catenanes
1. **Pre-organization of Pseudorotaxane**: A macrocyclic ring containing a 1,10-phenanthroline moiety (e.g., a 30-membered crown-type diether ring) is reacted with $[\\text{Cu}(\\text{MeCN})_4]^+$ and an open-chain phenanthroline thread bearing terminal phenolic hydroxyl groups:
\\[
\\text{Macrocycle} + \\text{Thread} + \\text{Cu}^I \\longrightarrow [\\text{Cu}(\\text{Macrocycle})(\\text{Thread})]^+
\\]
Due to the high thermodynamic stability of the bis-chelate complex ($\\log \\beta_2 \\approx 12 - 15$), the open thread is quantitatively threaded through the interior aperture of the preformed macrocycle.
2. **Ring Closure (Clipping)**: The two terminal hydroxyl groups of the threaded phenanthroline lie on opposite faces of the macrocycle. Reaction with an $\\alpha,\\omega$-diiodo polyether linker (e.g., pentaethylene glycol diiodide) in the presence of $\\text{Cs}_2\\text{CO}_3$ in DMF effects an intramolecular Williamson ether macrocyclization:
\\[
[\\text{Cu}(\\text{Macrocycle})(\\text{Thread})]^+ + \\text{I}-(CH_2CH_2O)_4-CH_2CH_2-\\text{I} \\xrightarrow{\\text{Cs}_2\\text{CO}_3} [\\text{Cu}(\\text{[2]catenand})]^+
\\]
This template-directed clipping achieves yields of $[\\text{Cu}(\\text{[2]catenand})]^+$ (the **catenate**) exceeding $42\\%$, a four-hundred-fold increase over statistical methods.
3. **Demetallation**: The coordinated copper(I) template ion is removed by treatment with excess potassium cyanide ($\\text{KCN}$) or EDTA in aqueous acetonitrile:
\\[
[\\text{Cu}(\\text{[2]catenand})]^+ + 4\\,\\text{CN}^- \\longrightarrow \\text{[2]catenand} + [\\text{Cu}(\\text{CN})_4]^{3-}
\\]
The metal-free **[2]catenand** is liberated. In the catenand, the two interlocking rings are completely free to circumrotate through each other's interior cavity."""
        },
        {
            "secNumber": "4.3",
            "title": "Stoddart Donor-Acceptor pi-Stacking Templates & Cyclobis(paraquat-p-phenylene)",
            "content": """In 1989, J. Fraser Stoddart developed a complementary, metal-free synthetic paradigm governed by donor-acceptor (D-A) aromatic $\\pi-\\pi$ stacking, electrostatic interactions, and $[\text{C-H}\\cdots\\text{O}]$ hydrogen bonding.

### The Blue Box: Cyclobis(paraquat-p-phenylene) ($\text{CBPQT}^{4+}$)
The cornerstone of Stoddart's methodology is the tetracationic cyclophane **cyclobis(paraquat-$p$-phenylene)**, commonly abbreviated $\\text{CBPQT}^{4+}$ or the "Blue Box":
- It consists of two electron-deficient 4,4'-bipyridinium (paraquat) units linked at each end by two $p$-xylylene spacers.
- The four positive formal charges render the bipyridinium rings strong $\\pi$-electron acceptors.
- The rectangular internal cavity measures approximately $7.2\\text{ Å} \\times 10.3\\text{ Å}$, ideally suited to intercalate flat, electron-rich aromatic guest systems.

### Complementary Electron-Rich Donors
Ideal $\\pi$-donors include:
1. **Hydroquinone (HQ)** or 1,4-dimethoxybenzene derivatives.
2. **1,5-Dioxynaphthalene (DNP)**: A fused bicyclic polyether derivative with an exceptionally high $\\pi$-electron density, yielding association constants with $\\text{CBPQT}^{4+}$ of $K_a \\approx 3 \\times 10^4\\text{ M}^{-1}$ in acetonitrile.
3. **Tetrathiafulvalene (TTF)**: An outstanding two-electron reversible redox donor.

### Three Primary Synthetic Methodologies for Rotaxanes
1. **Threading-and-Capping**: A linear dumbbell precursor containing the recognition site (e.g., DNP) is mixed with the macrocycle (e.g., $\\text{CBPQT}^{4+}$) to establish a dynamic equilibrium with the pseudorotaxane. Bulky stoichiometric stoppers (e.g., triisopropylsilyl or tetraarylmethane halides) are reacted with the termini to permanently trap the ring.
2. **Clipping**: An open-chain precursor (such as a bis-quaternary salt) is mixed with the preformed dumbbell carrying the electron-rich station. The thread acts as a template, aligning the precursors so that a bis-alkylation cyclization with $\\alpha,\\alpha'$-dibromo-$p$-xylene closes the ring directly around the shaft.
3. **Slipping**: A preformed macrocycle and preformed stoppered dumbbell with borderline steric stoppers are heated. Thermal activation allows the macrocycle to transiently stretch and slip over the bulky stopper. Upon cooling to room temperature, the system is kinetically trapped as the rotaxane."""
        },
        {
            "secNumber": "4.4",
            "title": "Active Metal Template (AMT) Synthesis and Covalent Templating Strategies",
            "content": """While passive template synthesis (Sauvage, Stoddart) uses the template solely as a geometric organizing scaffold, Leigh introduced the **Active Metal Template (AMT)** strategy in 2006. In AMT, the metal ion acts concurrently as:
1. The **geometric organizing template** that holds the macrocyclic and linear components in an interlocked pseudo-rotaxane orientation.
2. The **catalytic engine** that directly mediates the covalent bond-forming reaction between thread fragments within the macrocyclic cavity.

### The CuAAC Active Metal Template Mechanism
The classic AMT reaction utilizes copper(I)-catalyzed azide-alkyne cycloaddition (CuAAC "click" chemistry):
1. **Endo-Cavity Coordination**: A macrocycle bearing an internal coordination site (e.g., a pyridine-containing macrocycle or an endo-functionalized phenanthroline macrocycle) coordinates a $\\text{Cu}^I$ ion inside its central aperture.
2. **Assembly of Reactive Intermediates**: An alkyne-bearing half-thread and an azide-bearing half-thread (each already capped at one terminus by a bulky stopper) coordinate to the internal $\\text{Cu}^I$ center:
\\[
\\text{Ring}\\cdot\\text{Cu}^I + \\text{R}_1-\\text{C}\\equiv\\text{CH} + \\text{N}_3-\\text{R}_2 \\longrightarrow [\\text{Ring}\\cdot\\text{Cu}^I(\\text{C}\\equiv\\text{C}-\\text{R}_1)(\\text{N}_3-\\text{R}_2)]
\\]
3. **Intra-Cavity Cycloaddition**: The 1,3-dipolar cycloaddition proceeds strictly *through* the cavity of the macrocycle, forming a 1,4-disubstituted 1,2,3-triazole ring that bridges the two stoppers.
4. **Mechanical Trapping**: The newly forged covalent triazole link is too large to dethread through the macrocycle, and the terminal stoppers prevent slip-off. The $\\text{Cu}^I$ catalyst dissociates and is turned over into subsequent catalytic cycles:
\\[
\\text{Yield} > 95\\%, \\quad \\text{Turnover Number (TON)} > 100
\\]

### Covalent Templating Strategies
In covalent templating, interlocked rings are formed by assembling a single temporary covalent scaffold:
- Two macrocyclic rings are joined together through temporary covalent acetal, ether, or ester bonds.
- A ring-closing metathesis (RCM) or macrocyclization yields a fused bicyclic or bicyclo-spiro framework.
- Selective chemical cleavage of the temporary bridging covalent bond releases the two interlocked rings, providing the [2]catenane. Although conceptually elegant, multi-step synthetic complexity has largely yielded primacy to coordination-driven and AMT methods."""
        },
        {
            "secNumber": "4.5",
            "title": "Molecular Shuttles, Degenerate and Non-Degenerate Translational Isomerism",
            "content": """A **molecular shuttle** is a rotaxane in which the macrocycle can undergo translational Brownian motion along the linear shaft between two or more discrete recognition sites, termed **stations**.

### Degenerate Shuttling
In a **degenerate [2]rotaxane**, the two stations along the shaft are chemically and magnetically identical (e.g., two hydroquinone units separated by a flexible polyether linker, encircled by $\\text{CBPQT}^{4+}$):
\\[
\\text{Station}_1 \\xrightleftharpoons[k_{\\text{shuttle}}]{k_{\\text{shuttle}}} \\text{Station}_2
\\]
- Because both stations are identical, the free energy difference between the two positional states is zero: $\\Delta G^\circ = 0$, giving an equilibrium constant $K_{\\text{eq}} = 1$.
- Shuttling occurs as thermal Brownian motion across the intervening barrier $\\Delta G^\\ddagger$.
- The rate of degenerate shuttling $k_{\\text{shuttle}}$ can be directly quantified by variable-temperature dynamic nuclear magnetic resonance ($^1\\text{H}$ VT-NMR). At the coalescence temperature $T_c$:
\\[
k_c = \\frac{\\pi \\Delta \\nu}{\\sqrt{2}} \\approx 2.22 \\,\\Delta \\nu
\\]
where $\\Delta \\nu$ is the peak separation in Hertz between the free and occupied station resonances in the slow-exchange limit.
- Typical activation barriers for polyether shafts range from $\\Delta G^\\ddagger = 50\\text{ to }70\\text{ kJ/mol}$, corresponding to hopping frequencies of $100\\text{ to }100{,}000\\text{ s}^{-1}$ at $298\\text{ K}$.

### Non-Degenerate Translational Isomers (Co-Conformers)
In a **non-degenerate [2]rotaxane**, the two stations have differing chemical structures (e.g., Station 1 = TTF, Station 2 = DNP).
- The state where the ring resides on Station 1 has free energy $G_1$, while Station 2 has $G_2$.
- The equilibrium distribution is governed by the Boltzmann distribution:
\\[
K_{\\text{shuttle}} = \\frac{[\\text{State}_2]}{[\\text{State}_1]} = \\exp\\left( -\\frac{\\Delta G^\circ}{RT} \\right) = \\exp\\left( -\\frac{G_2 - G_1}{RT} \\right)
\\]
- The fraction occupied at Station 1 is:
\\[
f_1 = \\frac{1}{1 + K_{\\text{shuttle}}} = \\frac{1}{1 + e^{-\\Delta G^\\circ / RT}}
\\]
If the affinity of Station 1 exceeds that of Station 2 by $15\\text{ kJ/mol}$ at $298\\text{ K}$, $f_1 > 99.7\\%$, locking the ring almost exclusively at Station 1 under ambient conditions."""
        },
        {
            "secNumber": "4.6",
            "title": "Stimuli-Responsive Bistable Molecular Switches: Redox, Photochemical, and pH Gating",
            "content": """A **bistable molecular switch** is a non-degenerate rotaxane or catenane whose ground-state co-conformation can be reversibly toggled between two distinct stations by the application of external stimuli.

### Redox-Switchable Rotaxanes
Consider a rotaxane with an electron-rich tetrathiafulvalene ($\text{TTF}$) station and a 1,5-dioxynaphthalene ($\text{DNP}$) station, encircled by $\\text{CBPQT}^{4+}$:
1. **Neutral State**: TTF is a significantly stronger $\\pi$-donor than DNP ($\\Delta G^\circ \\approx -12\\text{ kJ/mol}$). The ring resides $>99\\%$ on the TTF station.
2. **One-Electron Oxidation**: Applying an electrochemical potential ($E_{1/2}^{(1)} \\approx +0.35\\text{ V}$ vs SCE) oxidizes TTF to its radical cation $\\text{TTF}^{+\\bullet}$. Strong electrostatic repulsion between $\\text{TTF}^{+\\bullet}$ and the tetracationic $\\text{CBPQT}^{4+}$ ring drives the ring to shuttle to the neutral DNP station:
\\[
[\\text{CBPQT}^{4+} \\subset \\text{TTF}^{+\\bullet}-\\text{DNP}] \\xrightarrow{\\text{fast}} [\\text{TTF}^{+\\bullet}-\\text{DNP} \\supset \\text{CBPQT}^{4+}]
\\]
3. **Chemical/Electrochemical Reduction**: Reducing $\\text{TTF}^{+\\bullet}$ back to neutral TTF restores the initial thermodynamic landscape, and the macrocycle shuttles back to TTF.

### Photochemically Gated Switches
Incorporating a photoisomerizable azobenzene unit into the shaft creates light-gated shuttles:
- **Trans-Azobenzene**: Planar, apolar, easily slips through or interacts with cyclodextrin ($\alpha$-CD) rings ($K_a \\approx 10^4\\text{ M}^{-1}$).
- **Cis-Azobenzene**: Formed upon UV irradiation ($\\lambda = 365\\text{ nm}$). Non-planar, bulky, with a high dipole moment. The $\\alpha$-CD ring is sterically ejected or compelled to migrate to an adjacent alkyl or oligoethylene glycol station.
- Visible light ($\\lambda = 450\\text{ nm}$) or thermal relaxation restores the *trans* isomer, causing the ring to return.

### pH-Switched Ammonium/Amine and Cryptand Systems
Stoddart and Leigh developed ammonium/triazolium or ammonium/crown shuttles:
- In the protonated state, secondary dialkylammonium $-\\text{CH}_2\\text{NH}_2^+\\text{CH}_2-$ forms strong hydrogen bonds to dibenzo-24-crown-8 (DB24C8) ($K_a > 10^5\\text{ M}^{-1}$).
- Addition of base ($\text{Et}_3\text{N}$ or phosphazene) deprotonates the ammonium to neutral amine ($-\\text{CH}_2\\text{NHCH}_2-$), abolishing the charge-assisted hydrogen bonds ($K_a < 10\\text{ M}^{-1}$). The DB24C8 ring immediately shuttles to a secondary station (e.g., a bipyridinium or triazolium unit).
- Re-addition of acid ($\\text{CF}_3\\text{COOH}$) reprotonates the amine, pulling the crown ether back."""
        },
        {
            "secNumber": "4.7",
            "title": "Molecular Knots and Borromean Rings",
            "content": """Molecular topology reaches its zenith in **molecular knots** and **Borromean rings**, where multi-component self-assembly and topology intertwine.

### Molecular Knots (Knotanes)
In knot theory, a knot is an embedding of a single circle $S^1$ in three-dimensional space $\\mathbb{R}^3$.
- **The Trefoil Knot ($3_1$)**: The simplest non-trivial knot, possessing three alternating crossings in its minimal planar projection. It exists as two non-superimposable topological enantiomers: right-handed (plus) and left-handed (minus).
- **Sauvage Double-Stranded Metallo-Helicate Precursor**:
  Sauvage synthesized the first molecular trefoil knot in 1989 using a double-helical dinuclear copper(I) complex:
  \\[
  2\\,\\text{Cu}^I + 2\\,\\text{bis(phenanthroline) ligand} \\longrightarrow [\\text{Cu}_2(\\text{ligand})_2]^{2+}
  \\]
  The two linear strands cross over one another twice at the copper centers. By designing an appropriate length for the terminal linkers, cross-connection of the terminal hydroxyl groups across opposite sides of the helix forces a third topological crossing.
  Subsequent demetallation with cyanide yields the stable, single-strand trefoil knotane.

### Leigh's Pentafoil Knot ($5_1$) and Composite Knots
In 2012, David Leigh synthesized a **pentafoil knot** ($5_1$ knot, 5 crossings) using a circular helicate of five iron(II) or zinc(II) ions coordinated to five bis-bidentate pyridyl-imine ligands. Ring-closing olefin metathesis (RCM) joined the 10 strand ends, creating a single closed loop of 160 atoms with five alternating mechanical crossings.

### Molecular Borromean Rings
In 2004, Stoddart and co-workers accomplished the rational self-assembly of **molecular Borromean rings**:
- Utilizing a dynamic covalent template, 6 equivalents of 2,6-diformylpyridine, 6 equivalents of 4,4'-diaminobiphenyl, and 6 zinc(II) cations undergo clean self-assembly in a 24-component single-pot reaction:
\\[
6\\,\\text{dialdehyde} + 6\\,\\text{diamine} + 6\\,\\text{Zn}^{2+} \\longrightarrow [\\text{Zn}_6(\\text{Borromeate})]^{12+} + 12\\,\\text{H}_2\\text{O}
\\]
- The structure contains three interlocked macrocyclic rings formed by 12 imine bonds.
- Removal of the zinc ions with cyanide yields the pure organic Borromean link. Cleaving any single ring breaks the mechanical entanglement of the other two."""
        },
        {
            "secNumber": "4.8",
            "title": "Artificial Molecular Machines & Nanomotors: 2016 Nobel Prize Concepts",
            "content": """The 2016 Nobel Prize in Chemistry was awarded jointly to **Jean-Pierre Sauvage, Sir J. Fraser Stoddart, and Ben L. Feringa** "for the design and synthesis of molecular machines." A molecular machine is defined as an assembly of molecular components capable of performing directional mechanical motion in response to specific energy inputs (chemical fuel, photons, or electrons).

### Physics of the Nanoworld: The Low Reynolds Number Regime
Molecular machines operate in a regime drastically distinct from macroscopic engines:
- **Zero Inertia**: At the nanoscale, the Reynolds number is extremely small ($Re = \\rho v L / \\eta \\ll 10^{-4}$), meaning inertial forces are utterly negligible compared to viscous drag. Movement stops the instant driving forces cease ($v \\propto F$).
- **Thermal Brownian Noise**: Molecular components are subject to continuous, chaotic thermal fluctuations ($k_B T \\approx 4.1 \\times 10^{-21}\\text{ J}$ at $300\\text{ K}$).
- **Brownian Ratchets**: Directional motion cannot be achieved simply by "pushing"; rather, it requires rectifying random thermal Brownian fluctuations via kinetic or energy ratchets (Feynman-Smoluchowski ratchet principle).

### Molecular Muscles, Lifts, and Rotary Motors
1. **Sauvage's Contractile Molecular Muscle**:
   A daisy-chain dimer of [2]rotaxanes that switches reversibly between an extended state (length $8.5\\text{ nm}$) when coordinated to $\\text{Zn}^{2+}$ (five-coordinate terpy/phen) and a contracted state (length $6.5\\text{ nm}$) when coordinated to $\\text{Cu}^I$ (four-coordinate bis-phen), producing a $24\\%$ macroscopic length change.
2. **Stoddart's Molecular Elevator**:
   A platform consisting of a tripod host with three macrocyclic crown rings threaded on a three-legged rig. Reversible acid-base titration lowers and raises the platform between two distinct height levels with an operating force of $\\approx 200\\text{ pN}$.
3. **Feringa's Light-Driven Rotary Motor**:
   Sterically overcrowded alkenes featuring a rotor and stator connected by a central $\\text{C}=\\text{C}$ double bond. A four-step cycle combines photochemical *cis-trans* isomerizations with thermal helix inversions, enforcing strict $360^\\circ$ unidirectional continuous rotation at frequencies up to $10^7\\text{ Hz}$.

### Chemical Fuel-Driven Autonomous Pumps
Modern synthetic nanomachines (Leigh, Stoddart) consume chemical fuels (such as carbodiimides or activated esters) in out-of-equilibrium dissipative cycles, pumping macrocycles from solution onto high-energy storage stations against thermodynamic gradients."""
        }
    ]

    problems = [
        {
            "probNumber": "4.1",
            "title": "Topological Invariants: Gauss Linking Number in [2]Catenanes and Catenands",
            "difficulty": "Foundational",
            "statement": """In molecular topology, the entanglement of two oriented closed curves $\\gamma_1$ and $\\gamma_2$ in $\\mathbb{R}^3$ is rigorously classified by the **Gauss Linking Number** $Lk(\\gamma_1, \\gamma_2) \\in \\mathbb{Z}$.
The classical integral formula is given by:
\\[
Lk(\\gamma_1, \\gamma_2) = \\frac{1}{4\\pi} \\oint_{\\gamma_1} \\oint_{\\gamma_2} \\frac{\\mathbf{r}_1 - \\mathbf{r}_2}{|\\mathbf{r}_1 - \\mathbf{r}_2|^3} \\cdot (d\\mathbf{r}_1 \\times d\\mathbf{r}_2)
\\]
(a) For a planar projection with oriented crossings, state the combinatorial formula for $Lk(\\gamma_1, \\gamma_2)$ in terms of the sign of crossings $\\epsilon(p)$ between the two rings.
(b) Evaluate the linking number $Lk$ for:
    (i) An unlinked pair of macrocycles,
    (ii) A standard [2]catenane (Hopf link),
    (iii) The pairwise linking numbers $Lk(R_i, R_j)$ ($i \\neq j$) for the three components of a Borromean ring system.
(c) Explain why demetallation of $[\\text{Cu}(\\text{[2]catenand})]^+$ to yield metal-free [2]catenand preserves the linking number invariant, whereas unthreading a pseudorotaxane does not.""",
            "solution": """### Step 1: Combinatorial Formulation of the Linking Number
In a regular two-dimensional projection of two oriented, directed closed curves $\\gamma_1$ and $\\gamma_2$:
- We consider only the **heterogeneous crossings** $p \\in \\gamma_1 \\cap \\gamma_2$ where an arc of $\\gamma_1$ crosses over or under an arc of $\\gamma_2$.
- Each crossing $p$ is assigned a sign $\\epsilon(p) = +1$ or $-1$ using the right-hand rule:
  - If the over-crossing strand must be rotated counter-clockwise by an angle $< 180^\\circ$ to align with the under-crossing strand, $\\epsilon(p) = +1$ (right-handed).
  - If rotated clockwise, $\\epsilon(p) = -1$ (left-handed).
The combinatorial linking number is:
\\[
Lk(\\gamma_1, \\gamma_2) = \\frac{1}{2} \\sum_{p \\in \\gamma_1 \\cap \\gamma_2} \\epsilon(p)
\\]

### Step 2: Evaluation for Topological Systems
1. **Unlinked Pair of Macrocycles**:
   No alternating crossings exist, or any apparent crossings in projection can be eliminated by continuous Reidemeister moves without crossing strands.
   \\[
   Lk(\\gamma_1, \\gamma_2) = 0
   \\]
2. **Standard [2]Catenane (Hopf Link)**:
   The minimal regular projection features exactly two heterogeneous crossings. If oriented consistently, both crossings have identical sign (either both $+1$ or both $-1$):
   \\[
   Lk(\\gamma_1, \\gamma_2) = \\frac{1}{2} (\\epsilon_1 + \\epsilon_2) = \\frac{1}{2} (\\pm 1 \\pm 1) = \\pm 1
   \\]
   The absolute linking number is $|Lk| = 1$. The non-zero integer proves that the two rings are topologically entangled and cannot be separated in $\\mathbb{R}^3$ without covalent bond rupture.
3. **Borromean Rings**:
   For any pair of rings $(R_i, R_j)$ in the Borromean architecture, inspecting the two rings in isolation shows that each ring lies on one side of the other; every over-crossing is paired with an under-crossing of opposite sign:
   \\[
   Lk(R_1, R_2) = Lk(R_2, R_3) = Lk(R_3, R_1) = 0
   \\]
   Pairwise, the rings have zero linking number. Their mechanical interlocking is a higher-order ternary topological invariant (the Massey triple product $\\langle R_1, R_2, R_3 \\rangle \\neq 0$).

### Step 3: Topological Invariance Under Demetallation vs Pseudorotaxane
- **Demetallation of $[\\text{Cu}(\\text{[2]catenand})]^+$**: Demetallation breaks coordination bonds between the copper ion and the phenanthroline nitrogen ligands. However, both macrocyclic rings remain covalently intact, continuous, closed 1-spheres ($S^1$). Ambient thermal deformations are continuous isotopies of $\\mathbb{R}^3 \\setminus \\gamma_2$. Because $Lk$ is an ambient isotopy invariant of closed loops, $|Lk| = 1$ remains strictly invariant.
- **Pseudorotaxane**: A pseudorotaxane lacks terminal covalent stoppers. The thread is an open 1-interval homeomorphic to $[0, 1]$, not a closed circle $S^1$. The open thread can translate along its axis until its terminus exits the macrocyclic interior, completely dissociating into separate species without cleaving any bond. Hence, pseudorotaxanes possess no non-trivial topological invariant."""
        },
        {
            "probNumber": "4.2",
            "title": "Two-State Boltzmann Equilibrium in a Symmetrical Molecular Shuttle",
            "difficulty": "Foundational",
            "statement": """A non-degenerate [2]rotaxane features a macrocycle shuttling between two distinct stations, Station A (monopyrrolotetrathiafulvalene, MP-TTF) and Station B (1,5-dioxynaphthalene, DNP), on a flexible dumbbell shaft.
At $T = 298.15\\text{ K}$, isothermal titration and VT-NMR measurements reveal that the standard enthalpy difference between the two positional states is $\\Delta H^\circ = H_B^\circ - H_A^\circ = +18.40\\text{ kJ/mol}$, and the standard entropy difference is $\\Delta S^\circ = S_B^\circ - S_A^\circ = +12.50\\text{ J/(mol}\\cdot\\text{K)}$.
(a) Calculate the standard Gibbs free energy difference $\\Delta G^\circ = G_B^\circ - G_A^\circ$ at $298.15\\text{ K}$.
(b) Determine the equilibrium shuttling constant $K_{\\text{shuttle}} = [\\text{State B}] / [\\text{State A}]$ and the molar percentage fraction of the macrocycle residing on Station A ($f_A$) versus Station B ($f_B$).
(c) At what temperature $T_{\\text{equi}}$ would the macrocycle distribute equally between both stations ($f_A = f_B = 50\\%$), assuming $\\Delta H^\circ$ and $\\Delta S^\circ$ are temperature-independent?""",
            "solution": """### Step 1: Gibbs Free Energy Calculation
Using the fundamental thermodynamic relation:
\\[
\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ
\\]
Substitute the given values at $T = 298.15\\text{ K}$:
- $\\Delta H^\\circ = +18.40\\text{ kJ/mol} = +18{,}400\\text{ J/mol}$
- $T\\Delta S^\\circ = 298.15\\text{ K} \\times 12.50\\text{ J/(mol}\\cdot\\text{K)} = +3{,}726.88\\text{ J/mol} = +3.727\\text{ kJ/mol}$
\\[
\\Delta G^\\circ = 18.40 - 3.727 = +14.673\\text{ kJ/mol}
\\]

### Step 2: Shuttling Equilibrium Constant and Populations
The equilibrium constant is given by:
\\[
K_{\\text{shuttle}} = \\frac{[\\text{State B}]}{[\\text{State A}]} = \\exp\\left( -\\frac{\\Delta G^\\circ}{RT} \\right)
\\]
With $R = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$:
\\[
\\frac{\\Delta G^\\circ}{RT} = \\frac{14{,}673}{8.31446 \\times 298.15} = \\frac{14{,}673}{2{,}478.96} = 5.9190
\\]
\\[
K_{\\text{shuttle}} = e^{-5.9190} = 2.688 \\times 10^{-3}
\\]
The mole fractions are:
\\[
f_A = \\frac{1}{1 + K_{\\text{shuttle}}} = \\frac{1}{1 + 0.002688} = \\frac{1}{1.002688} = 0.99732 \\implies 99.73\\%
\\]
\\[
f_B = 1 - f_A = 0.27\\%
\\]
At room temperature, the macrocycle resides $99.73\\%$ on the electron-rich MP-TTF station (State A).

### Step 3: Temperature for Equal Distribution ($T_{\\text{equi}}$)
Equal distribution occurs when $[\\text{State A}] = [\\text{State B}]$, meaning $K_{\\text{shuttle}} = 1$ and $\\Delta G^\\circ = 0$:
\\[
\\Delta H^\\circ - T_{\\text{equi}}\\Delta S^\\circ = 0 \\implies T_{\\text{equi}} = \\frac{\\Delta H^\\circ}{\\Delta S^\\circ}
\\]
Substitute the parameters:
\\[
T_{\\text{equi}} = \\frac{18{,}400\\text{ J/mol}}{12.50\\text{ J/(mol}\\cdot\\text{K)}} = 1{,}472\\text{ K}
\\]
Because $T_{\\text{equi}} = 1{,}472\\text{ K}$ far exceeds the thermal decomposition temperature of the organic rotaxane ($> 550\\text{ K}$), thermal switching alone cannot equilibrate the population; an external stimulus (such as chemical oxidation or light) is required."""
        },
        {
            "probNumber": "4.3",
            "title": "Coordination Geometry & Entropic Cooperativity in Sauvage Cu(I) Pseudorotaxanes",
            "difficulty": "Foundational",
            "statement": """In the Sauvage [2]catenane synthesis, copper(I) binds two 1,10-phenanthroline ligands in a stepwise coordination process:
1. $\\text{Cu}^+ + \\text{phen} \\xrightleftharpoons{K_1} [\\text{Cu}(\\text{phen})]^+$, with $\\log K_1 = 6.20$.
2. $[\\text{Cu}(\\text{phen})]^+ + \\text{phen} \\xrightleftharpoons{K_2} [\\text{Cu}(\\text{phen})_2]^+$, with $\\log K_2 = 9.60$.
(a) Calculate the overall stability constant $\\beta_2 = K_1 K_2$ and the total standard free energy of complexation $\\Delta G_{\\text{overall}}^\circ$ in acetonitrile at $298.15\\text{ K}$.
(b) Explain why $K_2 > K_1$ (an inverted stepwise stability sequence, unusual in coordination chemistry where typically $K_1 > K_2$).
(c) If a 30-membered macrocyclic phenanthroline host ($H$) is mixed with equimolar thread ($T$) and $[\\text{Cu}(\\text{MeCN})_4]^+$ at an initial concentration of $C_0 = 1.00 \\times 10^{-3}\\text{ M}$, calculate the percentage of assembled pseudorotaxane $[\\text{Cu}(H)(T)]^+$ at equilibrium, assuming $\\beta_2 = 10^{15.80}\\text{ M}^{-2}$.""",
            "solution": """### Step 1: Overall Stability Constant and Free Energy
The overall cumulative stability constant $\\beta_2$ is:
\\[
\\beta_2 = K_1 \\times K_2 = 10^{6.20} \\times 10^{9.60} = 10^{6.20 + 9.60} = 10^{15.80} = 6.310 \\times 10^{15}\\text{ M}^{-2}
\\]
The standard Gibbs free energy of overall complexation at $298.15\\text{ K}$ is:
\\[
\\Delta G^\\circ = -RT \\ln \\beta_2 = -(8.31446 \\times 298.15) \\times (15.80 \\times \\ln 10)
\\]
\\[
\\Delta G^\\circ = -2{,}478.96 \\times 36.3807 = -90{,}186\\text{ J/mol} = -90.19\\text{ kJ/mol}
\\]

### Step 2: Explanation of Inverted Stability Sequence ($K_2 > K_1$)
In typical Werner coordination complexes, $K_1 > K_2$ due to statistical factors (fewer available coordination sites) and electrostatic repulsions. For $\\text{Cu}^I$ ($d^{10}$) and 1,10-phenanthroline:
1. **Solvation Shell Disruption**: In acetonitrile, free $\\text{Cu}^I$ exists as $[\\text{Cu}(\\text{MeCN})_4]^+$. Binding the first phenanthroline displaces two MeCN molecules to form $[\\text{Cu}(\\text{phen})(\\text{MeCN})_2]^+$, but leaves two MeCN ligands coordinated in a distorted environment.
2. **Steric and Geometric Completion**: $\\text{Cu}^I$ strongly prefers a closed, tetrahedral four-coordinate geometry. Coordination of the second phenanthroline allows complete tetrahedral encapsulation $[\\text{Cu}(\\text{phen})_2]^+$, accompanied by favorable inter-ligand $\\pi-\\pi$ interactions between the phenanthroline backbones and the release of all coordinated solvent molecules. This cooperative geometric stabilization makes the second binding event far more exergonic ($K_2 \\gg K_1$).

### Step 3: Yield of Assembled Pseudorotaxane
Let $P = [\\text{Cu}(H)(T)]^+$. The reaction is:
\\[
\\text{Cu}^+ + H + T \\xrightleftharpoons{\\beta_2} P
\\]
Initially, $[\text{Cu}^+]_0 = [H]_0 = [T]_0 = C_0 = 1.00 \\times 10^{-3}\\text{ M}$.
Let the equilibrium concentration of pseudorotaxane be $x = [P]$.
Then $[\text{Cu}^+] = [H] = [T] = C_0 - x$.
\\[
\\beta_2 = \\frac{x}{(C_0 - x)^3} = 6.31 \\times 10^{15}
\\]
Because $\\beta_2$ is enormous ($10^{15.8}$), the reaction is virtually quantitative ($x \\approx C_0$).
Let $\\delta = C_0 - x$:
\\[
\\frac{C_0}{\\delta^3} \\approx \\beta_2 \\implies \\delta^3 = \\frac{C_0}{\\beta_2} = \\frac{1.00 \\times 10^{-3}}{6.31 \\times 10^{15}} = 1.585 \\times 10^{-19}\\text{ M}^3
\\]
\\[
\\delta = (1.585 \\times 10^{-19})^{1/3} = 5.41 \\times 10^{-7}\\text{ M}
\\]
The pseudorotaxane concentration is:
\\[
x = 1.00 \\times 10^{-3} - 5.41 \\times 10^{-7} = 0.99946 \\times 10^{-3}\\text{ M}
\\]
\\[
\\text{Yield} = \\frac{x}{C_0} \\times 100\\% = \\left(1 - \\frac{5.41 \\times 10^{-7}}{1.00 \\times 10^{-3}}\\right) \\times 100\\% = (1 - 0.000541) \\times 100\\% = 99.95\\%
\\]
The pseudorotaxane assembles quantitatively in solution."""
        },
        {
            "probNumber": "4.4",
            "title": "Thermodynamics and Kinetics of a Chemically Gated Bistable [2]Rotaxane",
            "difficulty": "Intermediate",
            "statement": """A bistable [2]rotaxane features a dibenzo-24-crown-8 (DB24C8) macrocycle shuttling between a secondary ammonium station ($-\\text{CH}_2\\text{NH}_2^+-\\text{CH}_2-$, Station 1) and a 4,4'-bipyridinium station ($\text{BIPY}^{2+}$, Station 2).
In neutral acetonitrile at $298\\text{ K}$:
- Binding affinity of DB24C8 to Station 1 is $K_1 = 4.20 \\times 10^4\\text{ M}^{-1}$.
- Binding affinity of DB24C8 to Station 2 is $K_2 = 1.50 \\times 10^2\\text{ M}^{-1}$.
Upon addition of excess base (diisopropylethylamine, DIPEA), Station 1 is deprotonated to neutral tertiary/secondary amine ($-\\text{CH}_2\\text{NH}-\\text{CH}_2-$), causing its affinity for DB24C8 to drop to $K_1' = 1.20\\text{ M}^{-1}$.
(a) Calculate the ratio of populations $[\\text{State 1}] / [\\text{State 2}]$ in the protonated and deprotonated states.
(b) Calculate the change in Gibbs free energy for the shuttling transition $\\text{State 1} \\rightarrow \\text{State 2}$ before and after deprotonation: $\\Delta G_{\\text{shuttle}} = -RT \\ln(K_2 / K_1)$ and $\\Delta G_{\\text{shuttle}}' = -RT \\ln(K_2 / K_1')$.
(c) If the forward shuttling rate constant after deprotonation is $k_{\\text{fwd}} = 85.0\\text{ s}^{-1}$, calculate the relaxation half-life $t_{1/2}$ for the macrocycle to reach its new equilibrium at Station 2.""",
            "solution": """### Step 1: Population Ratios in Protonated and Deprotonated States
The intramolecular partitioning of the macrocycle between the two stations is directly proportional to their intrinsic association constants:
\\[
\\frac{[\\text{State 1}]}{[\\text{State 2}]} = \\frac{K_1}{K_2}
\\]
1. **Protonated State**:
\\[
\\left(\\frac{[\\text{State 1}]}{[\\text{State 2}]}\\right)_{\\text{prot}} = \\frac{4.20 \\times 10^4}{1.50 \\times 10^2} = 280
\\]
Fraction on Station 1:
\\[
f_1 = \\frac{280}{1 + 280} = \\frac{280}{281} = 0.9964 \\implies 99.64\\%
\\]
The ring is localized almost exclusively at the ammonium station.

2. **Deprotonated State**:
\\[
\\left(\\frac{[\\text{State 1}]}{[\\text{State 2}]}\\right)_{\\text{deprot}} = \\frac{K_1'}{K_2} = \\frac{1.20}{1.50 \\times 10^2} = 8.00 \\times 10^{-3}
\\]
Fraction on Station 2:
\\[
f_2' = \\frac{1}{1 + 0.0080} = \\frac{1}{1.0080} = 0.9921 \\implies 99.21\\%
\\]
Deprotonation triggers a quantitative translocation of the macrocycle from Station 1 to Station 2.

### Step 2: Gibbs Free Energy Changes
For the shuttling process $\\text{State 1} \\rightleftharpoons \\text{State 2}$:
\\[
K_{\\text{shuttle}} = \\frac{[\\text{State 2}]}{[\\text{State 1}]} = \\frac{K_2}{K_1}
\\]
\\[
\\Delta G_{\\text{shuttle}} = -RT \\ln K_{\\text{shuttle}} = -RT \\ln\\left( \\frac{K_2}{K_1} \\right)
\\]
1. **Before Deprotonation**:
\\[
K_{\\text{shuttle}} = \\frac{1}{280} = 3.571 \\times 10^{-3}
\\]
\\[
\\Delta G_{\\text{shuttle}} = -(8.31446 \\times 298.15) \\times \\ln(0.003571) = -2478.96 \\times (-5.6348) = +13{,}968\\text{ J/mol} = +13.97\\text{ kJ/mol}
\\]
The process is endergonic, favoring State 1.

2. **After Deprotonation**:
\\[
K_{\\text{shuttle}}' = \\frac{K_2}{K_1'} = \\frac{150}{1.20} = 125
\\]
\\[
\\Delta G_{\\text{shuttle}}' = -2478.96 \\times \\ln(125) = -2478.96 \\times 4.8283 = -11{,}969\\text{ J/mol} = -11.97\\text{ kJ/mol}
\\]
The process becomes strongly exergonic by $-11.97\\text{ kJ/mol}$, driving shuttling to State 2.

### Step 3: Relaxation Half-Life
For a reversible first-order two-state relaxation:
\\[
\\text{State 1} \\xrightleftharpoons[k_{\\text{rev}}]{k_{\\text{fwd}}} \\text{State 2}
\\]
where $k_{\\text{rev}} = k_{\\text{fwd}} / K_{\\text{shuttle}}' = 85.0 / 125 = 0.680\\text{ s}^{-1}$.
The observed relaxation rate constant $k_{\\text{obs}}$ is:
\\[
k_{\\text{obs}} = k_{\\text{fwd}} + k_{\\text{rev}} = 85.0 + 0.680 = 85.68\\text{ s}^{-1}
\\]
The relaxation half-life is:
\\[
t_{1/2} = \\frac{\\ln 2}{k_{\\text{obs}}} = \\frac{0.69315}{85.68\\text{ s}^{-1}} = 8.09 \\times 10^{-3}\\text{ s} = 8.09\\text{ ms}
\\]
The macroscopic shuttling response completes in approximately 8 milliseconds."""
        },
        {
            "probNumber": "4.5",
            "title": "Slipping Kinetics & Arrhenius Activation Barrier in Rotaxane Trapping",
            "difficulty": "Intermediate",
            "statement": """In the slipping synthesis of a [2]rotaxane, a preformed macrocycle ($\text{CBPQT}^{4+}$) slips over a moderately bulky 3,5-di-$tert$-butylphenyl stopper of a dumbbell shaft in acetonitrile. The slipping rate constant $k_{\\text{slip}}$ was measured as a function of temperature:
- At $T_1 = 313.15\\text{ K}$ ($40^\\circ\\text{C}$): $k_{\\text{slip}}(T_1) = 1.45 \\times 10^{-5}\\text{ s}^{-1}$
- At $T_2 = 333.15\\text{ K}$ ($60^\\circ\\text{C}$): $k_{\\text{slip}}(T_2) = 2.10 \\times 10^{-4}\\text{ s}^{-1}$
(a) Using the two-point Arrhenius equation, determine the activation energy $E_a$ and the pre-exponential factor $A$.
(b) Using Eyring transition state theory, calculate the enthalpy of activation $\\Delta H^\\ddagger$, the entropy of activation $\\Delta S^\\ddagger$, and the Gibbs free energy of activation $\\Delta G^\\ddagger$ at $298.15\\text{ K}$.
(c) Estimate the shelf-life $t_{10\\%}$ (time required for $10\\%$ of preformed rotaxanes to dethread via slipping) at storage temperature $T = 273.15\\text{ K}$ ($0^\\circ\\text{C}$).""",
            "solution": """### Step 1: Arrhenius Activation Energy and Pre-Exponential Factor
The Arrhenius equation is:
\\[
\\ln\\left( \\frac{k_2}{k_1} \\right) = -\\frac{E_a}{R} \\left( \\frac{1}{T_2} - \\frac{1}{T_1} \\right) = \\frac{E_a}{R} \\left( \\frac{T_2 - T_1}{T_1 T_2} \\right)
\\]
Given:
- $k_1 = 1.45 \\times 10^{-5}\\text{ s}^{-1}$, $T_1 = 313.15\\text{ K}$
- $k_2 = 2.10 \\times 10^{-4}\\text{ s}^{-1}$, $T_2 = 333.15\\text{ K}$
\\[
\\ln\\left( \\frac{2.10 \\times 10^{-4}}{1.45 \\times 10^{-5}} \\right) = \\ln(14.4828) = 2.6730
\\]
\\[
\\frac{T_2 - T_1}{T_1 T_2} = \\frac{20.0}{313.15 \\times 333.15} = \\frac{20.0}{104{,}325.9} = 1.91707 \\times 10^{-4}\\text{ K}^{-1}
\\]
Thus:
\\[
E_a = \\frac{R \\times 2.6730}{1.91707 \\times 10^{-4}} = \\frac{8.31446 \\times 2.6730}{1.91707 \\times 10^{-4}} = \\frac{22.2245}{1.91707 \\times 10^{-4}} = 115{,}929\\text{ J/mol} = 115.93\\text{ kJ/mol}
\\]
Now find $A$:
\\[
\\ln A = \\ln k_1 + \\frac{E_a}{R T_1} = \\ln(1.45 \\times 10^{-5}) + \\frac{115{,}929}{8.31446 \\times 313.15} = -11.1413 + 44.5262 = 33.3849
\\]
\\[
A = e^{33.3849} = 3.154 \\times 10^{14}\\text{ s}^{-1}
\\]

### Step 2: Eyring Transition State Parameters
In solution, the enthalpy of activation is:
\\[
\\Delta H^\\ddagger = E_a - RT = 115{,}929 - (8.31446 \\times 298.15) = 115{,}929 - 2{,}479 = 113{,}450\\text{ J/mol} = 113.45\\text{ kJ/mol}
\\]
From the Eyring equation:
\\[
k = \\frac{k_B T}{h} \\exp\\left( \\frac{\\Delta S^\\ddagger}{R} \\right) \\exp\\left( -\\frac{\\Delta H^\\ddagger}{RT} \\right)
\\]
At $T_1 = 313.15\\text{ K}$, $k_B T_1 / h = (1.38065 \\times 10^{-23} \\times 313.15) / (6.62607 \\times 10^{-34}) = 6.5248 \\times 10^{12}\\text{ s}^{-1}$:
\\[
\\frac{\\Delta S^\\ddagger}{R} = \\ln\\left( \\frac{k_1 h}{k_B T_1} \\right) + \\frac{\\Delta H^\\ddagger}{R T_1} = \\ln\\left( \\frac{1.45 \\times 10^{-5}}{6.5248 \\times 10^{12}} \\right) + \\frac{113{,}450}{8.31446 \\times 313.15}
\\]
\\[
\\frac{\\Delta S^\\ddagger}{R} = \\ln(2.2223 \\times 10^{-18}) + 43.574 = -40.650 + 43.574 = +2.924
\\]
\\[
\\Delta S^\\ddagger = 2.924 \\times 8.31446 = +24.31\\text{ J/(mol}\\cdot\\text{K)}
\\]
The Gibbs free energy of activation at $298.15\\text{ K}$ is:
\\[
\\Delta G^\\ddagger = \\Delta H^\\ddagger - T\\Delta S^\\ddagger = 113.45 - (298.15 \\times 0.02431) = 113.45 - 7.25 = 106.20\\text{ kJ/mol}
\\]
The positive entropy of activation reflects significant desolvation and distortion of the macrocyclic ring as it deforms over the stopper.

### Step 3: Shelf-Life at $0^\circ\text{C}$ ($273.15\text{ K}$)
Calculate $k_{\\text{slip}}$ at $273.15\\text{ K}$:
\\[
k_{\\text{slip}}(273.15\\text{ K}) = A \\exp\\left( -\\frac{E_a}{R \\times 273.15} \\right)
\\]
\\[
\\frac{E_a}{R \\times 273.15} = \\frac{115{,}929}{2{,}271.1} = 51.045
\\]
\\[
k_{\\text{slip}}(273.15\\text{ K}) = (3.154 \\times 10^{14}) \\times e^{-51.045} = (3.154 \\times 10^{14}) \\times (6.799 \\times 10^{-23}) = 2.145 \\times 10^{-8}\\text{ s}^{-1}
\\]
For first-order unthreading, $10\\%$ unthreading corresponds to:
\\[
\\frac{[\\text{Rotaxane}]}{[\\text{Rotaxane}]_0} = 0.90 \\implies t_{10\\%} = -\\frac{\\ln(0.90)}{k} = \\frac{0.10536}{2.145 \\times 10^{-8}\\text{ s}^{-1}} = 4.912 \\times 10^6\\text{ s}
\\]
Converting to days:
\\[
t_{10\\%} = \\frac{4.912 \\times 10^6}{86{,}400} \\approx 56.85\\text{ days} \\approx 1.9\\text{ months}
\\]
At $0^\\circ\\text{C}$, the mechanically locked state is stable for nearly two months with less than $10\\%$ leakage."""
        },
        {
            "probNumber": "4.6",
            "title": "Cyclic Voltammetry of a Redox-Driven TTF/DNP [2]Rotaxane",
            "difficulty": "Intermediate",
            "statement": """A bistable [2]rotaxane contains a TTF station and a DNP station threaded by a $\\text{CBPQT}^{4+}$ ring. In cyclic voltammetry experiments (acetonitrile, $0.1\\text{ M }\\text{TBAPF}_6$, scan rate $v = 100\\text{ mV/s}$ at $298\\text{ K}$):
- For free, uncomplexed TTF: First oxidation $E_{1/2}^{\\text{free}}(\\text{TTF}^{0/+\\bullet}) = +0.330\\text{ V}$ vs SCE.
- When encapsulated inside the $\\text{CBPQT}^{4+}$ ring in the ground-state rotaxane: First oxidation shifts anodically to $E_{1/2}^{\\text{bound}} = +0.585\\text{ V}$ vs SCE.
(a) Calculate the anodic potential shift $\\Delta E_{1/2} = E_{1/2}^{\\text{bound}} - E_{1/2}^{\\text{free}}$.
(b) Using the Nernst-derived square thermodynamic cycle equation:
\\[
\\Delta E_{1/2} = \\frac{RT}{F} \\ln\\left( \\frac{K_a(\\text{TTF}^0)}{K_a(\\text{TTF}^{+\\bullet})} \\right)
\\]
calculate the ratio of binding constants $K_a(\\text{TTF}^0) / K_a(\\text{TTF}^{+\\bullet})$ at $298.15\\text{ K}$.
(c) If the association constant of neutral TTF with $\\text{CBPQT}^{4+}$ is $K_a(\\text{TTF}^0) = 2.50 \\times 10^4\\text{ M}^{-1}$, calculate the binding constant of the radical cation $K_a(\\text{TTF}^{+\\bullet})$ and interpret the electrostatic origin of this change.""",
            "solution": """### Step 1: Anodic Potential Shift
The potential shift is:
\\[
\\Delta E_{1/2} = E_{1/2}^{\\text{bound}} - E_{1/2}^{\\text{free}} = +0.585\\text{ V} - (+0.330\\text{ V}) = +0.255\\text{ V} = +255\\text{ mV}
\\]
The positive (anodic) shift demonstrates that TTF is significantly harder to oxidize when encapsulated inside the tetracationic macrocycle, indicating that the neutral state is stabilized relative to the radical cation state.

### Step 2: Thermodynamic Ratio of Association Constants
From the square thermodynamic cycle relating redox potentials to binding equilibria:
\\[
\\Delta E_{1/2} = \\frac{RT}{F} \\ln\\left( \\frac{K_a(\\text{TTF}^0)}{K_a(\\text{TTF}^{+\\bullet})} \\right)
\\]
where $RT/F = (8.31446 \\times 298.15) / 96{,}485 = 0.025693\\text{ V} = 25.693\\text{ mV}$.
Rearranging:
\\[
\\ln\\left( \\frac{K_a(\\text{TTF}^0)}{K_a(\\text{TTF}^{+\\bullet})} \\right) = \\frac{\\Delta E_{1/2}}{RT/F} = \\frac{0.255\\text{ V}}{0.025693\\text{ V}} = 9.92488
\\]
Taking the exponential:
\\[
\\frac{K_a(\\text{TTF}^0)}{K_a(\\text{TTF}^{+\\bullet})} = e^{9.92488} = 20{,}432 \\approx 2.04 \\times 10^4
\\]
The binding affinity of $\\text{CBPQT}^{4+}$ drops by a factor of over $20{,}000$ upon one-electron oxidation of the TTF station.

### Step 3: Binding Constant of Radical Cation and Physical Origin
Given $K_a(\\text{TTF}^0) = 2.50 \\times 10^4\\text{ M}^{-1}$:
\\[
K_a(\\text{TTF}^{+\\bullet}) = \\frac{2.50 \\times 10^4\\text{ M}^{-1}}{20{,}432} = 1.22\\text{ M}^{-1}
\\]
- **Electrostatic Origin**: In the neutral state, TTF is an electron-rich planar donor ($\pi$-donor) that engages in strong charge-transfer and dispersion interactions with the four pyridinium rings of $\\text{CBPQT}^{4+}$.
- Upon one-electron oxidation to $\\text{TTF}^{+\\bullet}$, the station acquires a net positive charge ($+1$). Placing a $+1$ monocation directly inside the cavity of a $+4$ tetracation results in intense Coulombic repulsion:
\\[
U_{\\text{Coulomb}} \\propto \\frac{q_{\\text{ring}} q_{\\text{station}}}{4\\pi \\epsilon r} > 0
\\]
This electrostatic destabilization overcomes any residual charge-transfer stabilization, expelling the macrocycle and driving it to shuttle to the alternate neutral DNP station."""
        },
        {
            "probNumber": "4.7",
            "title": "Statistical Mechanics of Non-Equilibrium Brownian Ratchets in Artificial Nanomotors",
            "difficulty": "Advanced",
            "statement": """Consider an artificial molecular rotary motor (Feringa-type) or linear Brownian ratchet governed by an asymmetric periodic potential energy landscape $U(x) = U(x + L)$ with period $L = 2.0\\text{ nm}$. The potential consists of an asymmetric saw-tooth with a barrier height $\\Delta U = 12.0\\, k_B T$ at $x_p = 0.35\\, L$ and a minimum at $x = 0$.
The system is subjected to external flashing (photochemical or chemical fuel cycles) between two potential states:
- State 1 (Potential ON): Asymmetric landscape $U_1(x)$ active for duration $\\tau_{\\text{on}}$.
- State 2 (Potential OFF): Completely flat landscape $U_2(x) = 0$ active for duration $\\tau_{\\text{off}}$ during which the motor undergoes pure Brownian diffusion with diffusion coefficient $D = 1.50 \\times 10^{-11}\\text{ m}^2/\\text{s}$.
(a) Calculate the optimal diffusion duration $\\tau_{\\text{off}}^*$ that maximizes directional translocation toward the shallow slope (positive $x$-direction) without allowing excessive backward diffusion beyond $-0.65\\, L$.
(b) Using the 1D diffusion probability distribution $P(x, t) = \\frac{1}{\\sqrt{4\\pi D t}} \\exp\\left( -\\frac{x^2}{4Dt} \\right)$, calculate the net directional probability flux per flashing cycle $\\Delta P = P(x > 0) - P(x < 0)$ at $\\tau_{\\text{off}} = 2.0\\times 10^{-8}\\text{ s}$.
(c) If the motor operates at a flashing frequency $\\nu = 1.0 \\times 10^6\\text{ Hz}$, compute the resulting macroscopic drift velocity $v_{\\text{drift}}$ and the thermodynamic stall force $F_{\\text{stall}}$ against an opposing mechanical load.""",
            "solution": """### Step 1: Optimal Flashing Off-Duration
In an asymmetric saw-tooth potential:
- Steep barrier slope extends from $-x_b = -(L - x_p) = -0.65\\, L = -1.30\\text{ nm}$ to $0$.
- Shallow barrier slope extends from $0$ to $+x_p = +0.35\\, L = +0.70\\text{ nm}$.
During the "OFF" phase ($U_2 = 0$), particles initialized at the potential minimum $x = 0$ diffuse freely according to Einstein diffusion:
\\[
\\langle x^2 \\rangle = 2 D t
\\]
To maximize forward ratcheting into the next well ($x > +0.70\\text{ nm}$) while minimizing backward ratcheting into the previous well ($x < -1.30\\text{ nm}$), the mean diffusion distance should equal the forward distance $x_p = 0.70\\text{ nm} = 0.70 \\times 10^{-9}\\text{ m}$:
\\[
x_p = \\sqrt{2 D \\tau_{\\text{off}}^*} \\implies \\tau_{\\text{off}}^* = \\frac{x_p^2}{2D}
\\]
Substitute values:
\\[
\\tau_{\\text{off}}^* = \\frac{(0.70 \\times 10^{-9}\\text{ m})^2}{2 \\times (1.50 \\times 10^{-11}\\text{ m}^2/\\text{s})} = \\frac{4.90 \\times 10^{-19}}{3.00 \\times 10^{-11}} = 1.633 \\times 10^{-8}\\text{ s} = 16.33\\text{ ns}
\\]

### Step 2: Net Directional Probability Flux at $\\tau_{\\text{off}} = 20\\text{ ns}$
At $\\tau_{\\text{off}} = 2.0 \\times 10^{-8}\\text{ s}$:
\\[
\\sigma = \\sqrt{2 D \\tau_{\\text{off}}} = \\sqrt{2 \\times (1.50 \\times 10^{-11}) \\times (2.0 \\times 10^{-8})} = \\sqrt{6.00 \\times 10^{-19}} = 7.746 \\times 10^{-10}\\text{ m} = 0.7746\\text{ nm}
\\]
When the potential flashes back ON:
- Any particle at $x > +x_p = +0.70\\text{ nm}$ falls forward into the basin at $x = +L$.
  Fraction falling forward:
  \\[
  P_{\\text{fwd}} = \\frac{1}{2} \\operatorname{erfc}\\left( \\frac{x_p}{\\sigma \\sqrt{2}} \\right) = \\frac{1}{2} \\operatorname{erfc}\\left( \\frac{0.70}{0.7746 \\times 1.4142} \\right) = \\frac{1}{2} \\operatorname{erfc}\\left( \\frac{0.70}{1.0954} \\right) = \\frac{1}{2} \\operatorname{erfc}(0.6390)
  \\]
  Using the standard error function value $\\operatorname{erf}(0.6390) \\approx 0.6341 \\implies \\operatorname{erfc}(0.6390) = 0.3659$:
  \\[
  P_{\\text{fwd}} = \\frac{1}{2} (0.3659) = 0.18295 \\implies 18.30\\%
  \\]
- Any particle at $x < -1.30\\text{ nm}$ falls backward into the basin at $x = -L$:
  \\[
  P_{\\text{bwd}} = \\frac{1}{2} \\operatorname{erfc}\\left( \\frac{1.30}{1.0954} \\right) = \\frac{1}{2} \\operatorname{erfc}(1.1868)
  \\]
  With $\\operatorname{erf}(1.1868) \\approx 0.9069 \\implies \\operatorname{erfc}(1.1868) = 0.0931$:
  \\[
  P_{\\text{bwd}} = \\frac{1}{2} (0.0931) = 0.04655 \\implies 4.66\\%
  \\]
The net directional probability flux per flashing cycle is:
\\[
\\Delta P = P_{\\text{fwd}} - P_{\\text{bwd}} = 0.18295 - 0.04655 = 0.1364 \\implies 13.64\\%
\\]
Each cycle transports a net $13.64\\%$ of the molecular population forward by one period $L$.

### Step 3: Macroscopic Drift Velocity and Stall Force
1. **Drift Velocity**:
With cycle frequency $\\nu = 1.0 \\times 10^6\\text{ Hz}$ and step size $L = 2.0\\text{ nm} = 2.0 \\times 10^{-9}\\text{ m}$:
\\[
v_{\\text{drift}} = \\Delta P \\times L \\times \\nu = 0.1364 \\times (2.0 \\times 10^{-9}\\text{ m}) \\times (1.0 \\times 10^6\\text{ s}^{-1}) = 2.728 \\times 10^{-4}\\text{ m/s} = 0.273\\text{ mm/s}
\\]
2. **Stall Force**:
An opposing mechanical force $F_{\\text{load}}$ tilts the potential landscape by $-F_{\\text{load}} x$. Stall occurs when the work done against the load across period $L$ matches the net free energy rectification per cycle:
\\[
W = F_{\\text{stall}} L = k_B T \\ln\\left( \\frac{P_{\\text{fwd}}}{P_{\\text{bwd}}} \\right)
\\]
At $T = 300\\text{ K}$, $k_B T = 4.14 \\times 10^{-21}\\text{ J}$:
\\[
\\ln\\left( \\frac{P_{\\text{fwd}}}{P_{\\text{bwd}}} \\right) = \\ln\\left( \\frac{0.18295}{0.04655} \\right) = \\ln(3.930) = 1.3687
\\]
\\[
F_{\\text{stall}} = \\frac{k_B T \\times 1.3687}{L} = \\frac{(4.14 \\times 10^{-21}\\text{ J}) \\times 1.3687}{2.0 \\times 10^{-9}\\text{ m}} = \\frac{5.666 \\times 10^{-21}}{2.0 \\times 10^{-9}} = 2.833 \\times 10^{-12}\\text{ N} = 2.83\\text{ pN}
\\]
The motor can exert a maximum stall force of $2.83\\text{ piconewtons}$, directly comparable to biological motor proteins such as kinesin and myosin."""
        },
        {
            "probNumber": "4.8",
            "title": "Trefoil Knot Topology: Minimal Crossing Energy and Coordinate Chirality",
            "difficulty": "Advanced",
            "statement": """A molecular trefoil knot ($3_1$ knot) is assembled from a single continuous covalently closed macrocyclic loop consisting of $N = 72$ carbon-carbon bonds.
In knot theory and polymer statistical mechanics, an unknotted loop (unknot $0_1$) has an equilibrium conformational entropy $S_0$, whereas a knotted loop is topologically constrained to a subspace of non-self-intersecting configurations with restricted conformational entropy $S_{\\text{knot}}$.
(a) According to the ropelength model, the ideal ropelength $\\lambda = L / D$ (where $L$ is total contour length and $D$ is the hard-core tube diameter) for the $3_1$ knot is $\\lambda_{\\min} \\approx 16.37$. If the effective steric diameter of the alkane chain is $D = 4.60\\text{ Å}$, calculate the minimal contour length $L_{\\min}$ and compare with the contour length of the 72-bond strand ($d_{\\text{C-C}} = 1.54\\text{ Å}$, tetrahedral angle $\\theta = 109.5^\\circ$).
(b) Des Cloizeaux theory states that the probability of forming a knot in a random walk of $N$ statistical segments scales as $P_{\\text{knot}}(N) \\approx 1 - \\exp(-N / N_0)$, where $N_0 \\approx 3.5 \\times 10^4$ for random unconstrained chains. Calculate the topological entropic penalty $\\Delta S_{\\text{topo}} = k_B \\ln P_{\\text{knot}}$ for statistical cyclization of an unconstrained chain of $N = 72$ segments.
(c) Explain how Sauvage's dinuclear $\\text{Cu}^I$ bis-phenanthroline helical template overcomes this colossal entropic barrier to achieve a $42\\%$ isolated chemical yield.""",
            "solution": """### Step 1: Ideal Ropelength vs Contour Length
For the trefoil knot $3_1$:
\\[
\\lambda_{\\min} = \\frac{L_{\\min}}{D} = 16.37
\\]
With hard-core diameter $D = 4.60\\text{ Å}$:
\\[
L_{\\min} = 16.37 \\times 4.60\\text{ Å} = 75.30\\text{ Å}
\\]
For an all-*anti* extended zigzag polymethylene chain of $N = 72$ bonds:
- The projection length per bond is:
\\[
\\Delta z = d_{\\text{C-C}} \\sin(\\theta / 2) = 1.54\\text{ Å} \\times \\sin(54.75^\\circ) = 1.54 \\times 0.8166 = 1.258\\text{ Å}
\\]
- The maximum extended contour length is:
\\[
L_{\\text{ext}} = 72 \\times 1.258\\text{ Å} = 90.58\\text{ Å}
\\]
Because $L_{\\text{ext}} = 90.58\\text{ Å} > L_{\\min} = 75.30\\text{ Å}$, the 72-bond chain is physically long enough to form a trefoil knot without steric self-intersection. The excess length ($90.58 - 75.30 = 15.28\\text{ Å}$) allows necessary conformational flexibility.

### Step 2: Topological Entropic Penalty in Statistical Cyclization
For an unconstrained chain with $N = 72$ segments and $N_0 = 35{,}000$:
\\[
N / N_0 = \\frac{72}{35{,}000} = 2.057 \\times 10^{-3} \\ll 1
\\]
Using the Taylor expansion $1 - e^{-x} \\approx x$:
\\[
P_{\\text{knot}}(N) \\approx \\frac{N}{N_0} = 2.057 \\times 10^{-3}
\\]
The topological entropic penalty per mole of cyclizing chains is:
\\[
\\Delta S_{\\text{topo}} = R \\ln P_{\\text{knot}} = 8.31446 \\times \\ln(2.057 \\times 10^{-3}) = 8.31446 \\times (-6.1865) = -51.44\\text{ J/(mol}\\cdot\\text{K)}
\\]
At $T = 298.15\\text{ K}$, this corresponds to an unfavorable free energy barrier:
\\[
-T\\Delta S_{\\text{topo}} = -(298.15) \\times (-51.44) = +15{,}337\\text{ J/mol} = +15.34\\text{ kJ/mol}
\\]
In random solution, fewer than 2 chains in 1,000 would form a knot upon unguided cyclization; over $99.8\\%$ form unknots or oligomeric macrocycles.

### Step 3: Template-Directed Entropic Overcoming
Sauvage's dinuclear copper(I) double-stranded helicate $[\\text{Cu}_2(\\text{ligand})_2]^{2+}$ circumvents this statistical impossibility:
1. **Enthalpic Pre-organization**: Coordination of two bis-chelating phenanthroline ligands to two $\\text{Cu}^I$ ions provides $\\approx 180\\text{ kJ/mol}$ of favorable coordination enthalpy, strictly locking the two strands into a double-helical crossing geometry with two permanent crossings pre-arranged.
2. **Geometric Constraints on Chain Ends**: The coordination complex positions the four reactive terminal hydroxyl groups at exact spatial coordinates such that top-to-bottom cross-linking is geometrically favored over unknotted intra-strand ring closure.
3. **Effective Molarity**: The template elevates the effective local concentration of complementary reactive chain ends to $EM > 10\\text{ M}$, converting a low-probability trimolecular random search into a highly favorable pseudointramolecular ring closure, achieving a $42\\%$ isolated yield."""
        },
        {
            "probNumber": "4.9",
            "title": "Thermodynamics of Multivalent Borromean Ring Assembly",
            "difficulty": "Advanced",
            "statement": """In the single-pot template synthesis of molecular Borromean rings (Stoddart et al.):
\\[
6\\,\\text{dialdehyde} (D) + 6\\,\\text{diamine} (A) + 6\\,\\text{Zn}^{2+} (M) \\xrightleftharpoons{\\beta_{\\text{BR}}} [\\text{Zn}_6(\\text{BR})]^{12+} + 12\\,\\text{H}_2\\text{O}
\\]
A total of 18 separate chemical building blocks assemble into a single supramolecular complex held by 12 dynamic imine bonds and 6 bis-terpyridine-like octahedral zinc(II) coordination centers.
(a) Write the mathematical expression for the overall association constant $\\beta_{\\text{BR}}$ in terms of equilibrium concentrations.
(b) In anhydrous/low-water solvent, suppose the effective binding free energy per zinc-diimine chelate center is $\\Delta G_{\\text{unit}}^\circ = -28.50\\text{ kJ/mol}$. If the multivalent assembly exhibits an entropic penalty for bringing 18 particles together of $\\Delta S_{\\text{trans}}^\circ = -1.45\\text{ kJ/(mol}\\cdot\\text{K)}$ at $T = 333.15\\text{ K}$ ($60^\\circ\\text{C}$):
    (i) Calculate the total net free energy of assembly $\\Delta G_{\\text{assembly}}^\circ = 6\\,\\Delta G_{\\text{unit}}^\circ - T\\Delta S_{\\text{trans}}^\circ$.
    (ii) Compute $\\beta_{\\text{BR}}$ at $333.15\\text{ K}$.
(c) Using dynamic covalent chemistry principles, explain why Borromean ring synthesis yields a single thermodynamic product in $>85\\%$ yield despite the existence of thousands of possible statistical oligomeric and macrocyclic side products.""",
            "solution": """### Step 1: Overall Equilibrium Expression
The assembly equilibrium is:
\\[
6 D + 6 A + 6 M^{2+} \\xrightleftharpoons{\\beta_{\\text{BR}}} [\\text{Zn}_6(\\text{BR})]^{12+} + 12\\,\\text{H}_2\\text{O}
\\]
The thermodynamic association constant $\\beta_{\\text{BR}}$ is expressed as:
\\[
\\beta_{\\text{BR}} = \\frac{[[\\text{Zn}_6(\\text{BR})]^{12+}] [\\text{H}_2\\text{O}]^{12}}{[D]^6 [A]^6 [M^{2+}]^6}
\\]

### Step 2: Free Energy and Stability Constant Calculation
1. **Total Free Energy**:
The assembly comprises 6 structural coordination/condensation units:
\\[
\\Delta G_{\\text{units}}^\circ = 6 \\times \\Delta G_{\\text{unit}}^\circ = 6 \\times (-28.50\\text{ kJ/mol}) = -171.0\\text{ kJ/mol}
\\]
The translational entropic cost at $T = 333.15\\text{ K}$ is:
\\[
-T\\Delta S_{\\text{trans}}^\circ = -(333.15\\text{ K}) \\times (-1.45\\text{ kJ/(mol}\\cdot\\text{K)}) = +483.07\\text{ kJ/mol}
\\]
However, the formation of 12 equivalents of water released into the solvent contributes a large favorable translational entropy:
\\[
\\Delta S_{\\text{release}}^\circ = +12 \\times (0.055\\text{ kJ/(mol}\\cdot\\text{K)}) = +0.660\\text{ kJ/(mol}\\cdot\\text{K)}
\\]
\\[
-T\\Delta S_{\\text{release}}^\circ = -(333.15) \\times (+0.660) = -219.88\\text{ kJ/mol}
\\]
The net Gibbs free energy of assembly is:
\\[
\\Delta G_{\\text{assembly}}^\circ = -171.0 + 483.07 - 219.88 = +92.19\\text{ kJ/mol} \\quad \\text{uncorrected}
\\]
In the presence of optimal chelate cooperativity and internal $\\pi-\\pi$ stacking between aromatic rings (additional $\\Delta G_{\\pi-\\pi}^\circ = -180.0\\text{ kJ/mol}$ across the 12 overlapping rings):
\\[
\\Delta G_{\\text{assembly, net}}^\circ = -171.0 - 180.0 + 483.07 - 219.88 = -87.81\\text{ kJ/mol}
\\]
2. **Cumulative Constant $\\beta_{\\text{BR}}$**:
\\[
\\beta_{\\text{BR}} = \\exp\\left( -\\frac{\\Delta G_{\\text{assembly, net}}^\circ}{RT} \\right) = \\exp\\left( \\frac{87{,}810}{8.31446 \\times 333.15} \\right) = \\exp\\left( \\frac{87{,}810}{2{,}769.96} \\right) = e^{31.70} \\approx 5.86 \\times 10^{13}
\\]

### Step 3: Thermodynamic Error Correction in Dynamic Covalent Assembly
The high isolated yield ($>85\\%$) emerges from **dynamic covalent chemistry (DCC)** and **thermodynamic self-sorting**:
1. **Reversibility and Proofreading**: Imine condensation ($\text{C}=\text{N}$) and $\text{Zn}^{2+}-\text{N}$ coordination are fully reversible under the reaction conditions (refluxing methanol/acetonitrile). Any mismatched oligomers, small misfolded macrocycles, or irregular polymers form with residual strain and uncoordinated or unbonded functional groups.
2. **Thermodynamic Sink**: The Borromean ring architecture satisfies every single hydrogen-bonding, coordination, and covalent valency:
   - All 12 aldehydes and 12 amines form closed imines (no dangling ends).
   - All 6 $\\text{Zn}^{2+}$ ions achieve ideal octahedral bis-terpyridine-like coordination geometry.
   - All 6 aromatic spacers participate in inter-ring $\\pi-\\pi$ stacking.
Because the Borromean ring resides in a deep global thermodynamic free energy minimum, continuous disassembly and reassembly of kinetic intermediates thermodynamically drives the entire chemical library into this single topological product."""
        }
    ]

    return {
        "id": "unit-4",
        "number": 4,
        "title": "Mechanically Interlocked Molecules: Catenanes, Rotaxanes & Molecular Knots",
        "leadSummary": "Molecular topology, the mechanical bond, Sauvage passive copper(I)-template synthesis of catenanes, Stoddart donor-acceptor cyclobis(paraquat-p-phenylene) rotaxanes, active metal template (AMT) catalytic synthesis, degenerate vs non-degenerate shuttles, bistable molecular switches, higher topological knots (trefoil, pentafoil, Borromean rings), and artificial molecular machines of the 2016 Nobel Prize.",
        "simulations": ["sim_supra_rotaxane_molecular_shuttle"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u4 = get_unit_4()
    print(f"Unit 4 generated: {len(u4['sections'])} sections, {len(u4['problems'])} problems.")
