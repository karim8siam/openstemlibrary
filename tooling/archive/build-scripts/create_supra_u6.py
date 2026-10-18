"""
create_supra_u6.py
Creates Unit 6 data dictionary for Supramolecular Chemistry:
Bioinorganic & Bioorganic Supramolecular Model Systems
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_6():
    sections = [
        {
            "secNumber": "6.1",
            "title": "Bioinorganic Supramolecular Mimicry: Entatic States & Microenvironments",
            "content": """Biological metalloenzymes achieve catalytic rates and chemical selectivities that macroscopic industrial catalysts struggle to match. Supramolecular bioinorganic chemistry seeks to design low-molecular-weight synthetic model complexes that reproduce the active site structure, spectroscopic properties, and catalytic mechanisms of native metalloenzymes.

### The Entatic State Hypothesis
In 1968, Vallee and Williams formulated the **entatic state** hypothesis (from the Greek *entasis*, meaning "tension" or "strain"):
- In classical inorganic coordination complexes, metal ions adopt ground-state geometries dictated by their $d$-electron count and ligand-field stabilization energy (LFSE)—such as square-planar for $d^8\\,\\text{Ni}^{II}$, regular octahedral for $d^6\\,\\text{Co}^{III}$, or regular tetrahedral for $d^{10}\\,\\text{Zn}^{II}$.
- In metalloenzymes, the tertiary and quaternary folding of the polypeptide scaffold forces the coordinating amino acid side chains (histidines, cysteines, aspartates) into an unnatural, geometrically constrained coordination sphere.
- The metal ion is trapped in an energetically strained state that closely resembles the **transition state** of the catalytic reaction rather than an unreactive thermodynamic ground state.
- For example, the blue copper protein plastocyanin coordinates $\\text{Cu}^{II}$ in a distorted trigonal pyramidal/tetrahedral geometry intermediate between the preferred tetrahedral geometry of $\\text{Cu}^I$ and the preferred tetragonal/octahedral geometry of $\\text{Cu}^{II}$. Consequently, the reorganization energy $\\lambda$ for electron transfer is minimal ($\\lambda < 0.6\\text{ eV}$), enabling ultra-fast electron transfer ($k_{\\text{ET}} > 10^6\\text{ s}^{-1}$).

### Secondary Coordination Sphere and Hydrogen-Bond Networks
Synthetic bioinorganic models must mimic not only the primary coordination sphere (first-shell ligands directly coordinated to the metal) but also the **secondary coordination sphere**:
- Hydrogen-bond donors and acceptors positioned around the binding pocket stabilize coordinated substrates (such as oxy, peroxy, or hydroxo intermediates).
- Hydrophobic clefts exclude bulk water, suppressing spontaneous hydrolytic decomposition or bimolecular radical quenching.
- Dielectric confinement creates local dielectric constants as low as $\\epsilon_r \\approx 4 - 10$, dramatically elevating electrostatic interactions and ligand-metal charge transfer."""
        },
        {
            "secNumber": "6.2",
            "title": "Biomimetic Ionophores: Valinomycin & Synthetic Transmembrane Channels",
            "content": """Ionophores are lipid-soluble supramolecular agents that facilitate the transport of inorganic cations across hydrophobic biological membranes.

### Valinomycin: Nature's $\text{K}^+$-Selective Carrier
**Valinomycin** is a cyclic dodecadepsipeptide antibiotic produced by *Streptomyces fulvissimus*. It consists of alternating amino acids and hydroxy acids:
\\[
\\text{cyclo-}[\\text{-D-Val-L-Lac-L-Val-D-Hyi-}]_3
\\]
where Lac is L-lactic acid and Hyi is D-hydroxyisovaleric acid.
- **Conformational Architecture**:
  In non-polar membrane environments, valinomycin folds into a compact "tennis-ball" or bracelet conformation stabilized by six internal intramolecular $[\\text{N-H}\\cdots\\text{O}=\\text{C}]$ hydrogen bonds between the amide groups.
  - All twelve hydrophobic methyl and isopropyl side chains are projected outward toward the lipid bilayer, creating a lipophilic hydrocarbon exterior.
  - Six ester carbonyl oxygens point inward toward the center, forming an octahedral coordination cavity with an effective radius $r_{\\text{cav}} \\approx 1.33\\text{ to }1.40\\text{ Å}$.
- **Exquisite $\\text{K}^+ / \\text{Na}^+$ Selectivity**:
  Valinomycin exhibits an extraordinary transport selectivity for potassium over sodium exceeding **$10{,}000 : 1$**:
  - The ionic radius of $\\text{K}^+$ ($r = 1.38\\text{ Å}$) perfectly matches the rigid oxygen octahedron, allowing complete desolvation and optimal coordination.
  - The smaller $\\text{Na}^+$ ion ($r = 1.02\\text{ Å}$) is too small to touch all six carbonyl oxygens simultaneously. Because the rigid hydrogen-bonded backbone resists contraction, the entropic/enthalpic gain of binding $\\text{Na}^+$ cannot compensate for the high dehydration energy of $\\text{Na}^+$ ($\\Delta H_{\\text{hyd}}^\circ = -405\\text{ kJ/mol}$ vs $-321\\text{ kJ/mol}$ for $\\text{K}^+$).

### Channel-Forming Ionophores: Gramicidin A and Synthetic Channels
- **Gramicidin A**: A linear 15-residue pentadecapeptide that dimerizes head-to-head in lipid bilayers to form a continuous transmembrane $\\beta^{6.3}$-helical channel (length $\\approx 26\\text{ Å}$, pore diameter $\\approx 4.0\\text{ Å}$). It transports monovalent cations at rates exceeding $10^7\\text{ ions/second}$, approaching diffusion limits.
- **Synthetic Ion Channels (Crown-Ethers & Peptide Nanotubes)**:
  Supramolecular chemists (e.g., Gokel, Fyles, Matile) construct artificial channels using stacked crown ethers, tubular calixarenes, or self-assembled peptide barrels that insert into artificial liposomes to mediate selective ion transport."""
        },
        {
            "secNumber": "6.3",
            "title": "Porphyrins, Metalloporphyrins, Corrins & Phthalocyanines",
            "content": """Tetrapyrrolic macrocycles form the prosthetic cores of essential bioenergetic and catalytic proteins, including hemoglobin, myoglobin, cytochromes, chlorophylls, and vitamin $\\text{B}_{12}$.

### Structural Classes
1. **Porphyrin (Porphine Core)**:
   A fully conjugated, planar macrocycle composed of four pyrrole rings connected by four methine ($=\\text{CH}-$) bridges.
   - It possesses an 18-electron $[4n+2]$ aromatic delocalization pathway following Hückel's rule (with two cross-conjugated peripheral double bonds).
   - The central dianionic $\\text{N}_4$ cavity has a radius of approximately $2.01\\text{ to }2.05\\text{ Å}$, ideal for binding first-row divalent and trivalent transition metals ($\text{Fe}^{II/III}, \\text{Zn}^{II}, \\text{Ni}^{II}, \\text{Cu}^{II}, \\text{Co}^{II/III}$).
2. **Corrins**:
   The macrocyclic core of cobalamin (vitamin $\\text{B}_{12}$). A direct link connects two pyrrolic rings (rings A and D) without an intervening methine bridge. As a result, the macrocycle is smaller, more flexible, and non-planar, stabilizing low-valent cobalt ($\text{Co}^I, \\text{Co}^{II}, \\text{Co}^{III}$).
3. **Phthalocyanines**:
   Synthetic tetrapyrrolic analogues where the four methine bridges are replaced by meso-nitrogen ($-\\text{N}=$) atoms and benzene rings are fused to the pyrrole peripheries. Characterized by intense blue/green colors and chemical inertness.

### Optical Spectroscopy: Soret and Q Bands
The electronic absorption spectra of porphyrins are interpreted using Martin Gouterman's **Four-Orbital Model**:
- The frontier orbitals consist of two highest occupied molecular orbitals ($a_{1u}$ and $a_{2u}$) and two degenerate lowest unoccupied molecular orbitals ($e_g$).
- Electronic transitions between these levels generate two configuration-mixed states:
  1. **Soret Band (B band)**: A very intense allowed electronic transition in the near-UV/blue region ($\\lambda \\approx 400 - 430\\text{ nm}$, molar absorptivity $\\epsilon > 10^5\\text{ M}^{-1}\\text{cm}^{-1}$).
  2. **Q Bands**: Weaker, quasi-forbidden transitions in the visible region ($\\lambda \\approx 500 - 650\\text{ nm}$, $\\epsilon \\approx 10^3 - 10^4\\text{ M}^{-1}\\text{cm}^{-1}$).
  - Free-base porphyrins ($D_{2h}$ symmetry) display four Q bands due to splitting by the two central inner protons.
  - Metallated porphyrins ($D_{4h}$ symmetry) display only two Q bands ($\alpha$ and $\beta$) due to restored four-fold degeneracy."""
        },
        {
            "secNumber": "6.4",
            "title": "Myoglobin and Hemoglobin Models: The mu-Oxo Dimerization Problem",
            "content": """Hemoglobin and myoglobin function as reversible dioxygen carriers in aerobic organisms. Their active site consists of a protoheme (iron(II) protoporphyrin IX) coordinated axially by an imidazole nitrogen from an invariant histidine residue (the "proximal histidine", His F8).

### The Challenge of Simple Iron(II) Porphyrins in Solution
When an unhindered synthetic iron(II) porphyrin, such as $\\text{Fe}^{II}(\\text{TPP})$ (tetraphenylporphyrin), is exposed to molecular oxygen ($\text{O}_2$) in solution at room temperature, it undergoes rapid, irreversible autoxidation rather than reversible oxygenation:
\\[
\\text{Fe}^{II}(\\text{porph}) + \\text{O}_2 \\xrightleftharpoons{} \\text{Fe}^{III}(\\text{porph})-\\text{O}_2^{-\\bullet} \\quad (\\text{superoxo complex})
\\]
In the absence of a protective protein pocket, the superoxo intermediate attacks a second uncoordinated $\\text{Fe}^{II}(\\text{porph})$ molecule:
\\[
\\text{Fe}^{III}(\\text{porph})-\\text{O}_2^{-\\bullet} + \\text{Fe}^{II}(\\text{porph}) \\xrightleftharpoons{} \\text{Fe}^{III}(\\text{porph})-\\text{O}-\\text{O}-\\text{Fe}^{III}(\\text{porph}) \\quad (\\mu\\text{-peroxo dimer})
\\]
The $\\mu$-peroxo intermediate undergoes rapid homolytic $\\text{O-O}$ bond cleavage:
\\[
\\text{Fe}^{III}-\\text{O}-\\text{O}-\\text{Fe}^{III} \\longrightarrow 2\\,\\text{Fe}^{IV}(\\text{porph})=\\text{O} \\quad (\\text{ferryl intermediate})
\\]
The ferryl species reacts rapidly with remaining $\\text{Fe}^{II}$ porphyrin to produce the thermodynamically inert, catalytically dead **$\\mu$-oxo dimer**:
\\[
\\text{Fe}^{IV}(\\text{porph})=\\text{O} + \\text{Fe}^{II}(\\text{porph}) \\longrightarrow \\text{Fe}^{III}(\\text{porph})-\\text{O}-\\text{Fe}^{III}(\\text{porph}) \\quad (\\mu\\text{-oxo dimer})
\\]
The overall bimolecular dimerization produces an extremely stable $\\text{Fe-O-Fe}$ linear bridge (antiferromagnetically coupled, $S = 0$), completely quenching reversible $\\text{O}_2$ binding.

### Nature's Solution: The Globin Fold
In native myoglobin, the polypeptide backbone isolates the heme group in a deep hydrophobic cleft, physically preventing two heme centers from approaching each other within the distance required to form a $\\mu$-peroxo bridge ($d_{\\text{Fe}\\cdots\\text{Fe}} \\approx 4.0\\text{ Å}$)."""
        },
        {
            "secNumber": "6.5",
            "title": "Collman's Picket-Fence Porphyrin: Design & Reversible Oxygen Binding",
            "content": """To prevent bimolecular $\\mu$-oxo dimerization without a macromolecular protein matrix, James P. Collman designed the celebrated **"picket-fence" porphyrin** in 1974.

### Molecular Architecture
Collman synthesized *meso*-tetra($\alpha,\alpha,\alpha,\alpha$-$o$-pivalamidophenyl)porphyrin:
- Four *ortho*-amino groups on the four meso-phenyl rings were positioned exclusively on the **same face** of the porphyrin plane ($\alpha,\alpha,\alpha,\alpha$ atropisomer).
- Acylation with pivaloyl chloride ($tert$-butylcarbonyl chloride) created four rigid, bulky pivalamide "pickets" protruding perpendicularly above one face of the porphyrin ring.
- These pickets form a protected hydrophobic enclosure approximately $5.0\\text{ Å}$ deep with an open aperture directly above the central metal coordination site.

### Mechanism of Protection
1. **Steric Encapsulation**: The four $tert$-butyl pickets are sufficiently bulky to physically prevent a second metalloporphyrin from approaching close enough to form a $\\mu$-peroxo bridge ($\text{Fe-O-O-Fe}$).
2. **Axial Base Discrimination**: Bulky axial ligands (e.g., 1,2-dimethylimidazole) are sterically excluded from the picket-protected face and must coordinate exclusively to the unhindered lower face, creating a five-coordinate iron(II) complex with a vacant binding pocket on the upper face.
3. **Reversible $\\text{O}_2$ Binding**: Small diatomic molecules ($\text{O}_2$, $\text{CO}$) easily enter the picket enclosure. Exposure to oxygen produces a stable, crystalline $1:1$ dioxygen complex:
\\[
\\text{Fe}(\\text{TpivPP})(\\text{1,2-Me}_2\\text{Im}) + \\text{O}_2 \\xrightleftharpoons{K_{\\text{O}_2}} \\text{Fe}(\\text{TpivPP})(\\text{1,2-Me}_2\\text{Im})(\\text{O}_2)
\\]
- The complex exhibits an end-on bent coordination geometry ($\angle \\text{Fe-O-O} \\approx 115^\\circ - 120^\\circ$), matching native oxyhemoglobin.
- Internal $[\\text{N-H}\\cdots\\text{O}_2]$ hydrogen bonding between the pivalamide amide protons and the coordinated oxygen atom further stabilizes the complex against dissociation."""
        },
        {
            "secNumber": "6.6",
            "title": "Biomimetic Copper Complexes: Hemocyanin & Multicopper Centers",
            "content": """Copper ions serve critical roles in biological respiration and oxidation. Biomimetic supramolecular chemistry has successfully replicated the active sites of copper proteins.

### Hemocyanin: Non-Heme Reversible Oxygen Carrier
Hemocyanin is a massive copper-containing respiratory protein found in mollusks and arthropods that turns blue upon oxygenation.
- **Deoxyhemocyanin**: Contains two copper(I) ions ($d^{10}$, colorless, diamagnetic) separated by a distance $d_{\\text{Cu}\\cdots\\text{Cu}} \\approx 4.6\\text{ Å}$. Each $\\text{Cu}^I$ is coordinated by three histidine imidazole nitrogens in a trigonal planar geometry.
- **Oxyhemocyanin**: Reversible binding of $\\text{O}_2$ oxidizes both metal centers to copper(II) ($d^9$), reducing dioxygen to peroxide ($\text{O}_2^{2-}$):
\\[
[\\text{Cu}^I \\cdots \\text{Cu}^I] + \\text{O}_2 \\xrightleftharpoons{} [\\text{Cu}^{II}(\\mu\\text{-}\eta^2:\\eta^2\\text{-O}_2)\\text{Cu}^{II}]
\\]
- **Side-On Bridging Peroxo Geometry**:
  The peroxide ion coordinates in an unprecedented **side-on bridging $\\mu\\text{-}\eta^2:\\eta^2$** geometry. The two copper ions and two oxygen atoms form a planar $\\text{Cu}_2\\text{O}_2$ rhomboid with $d_{\\text{Cu}\\cdots\\text{Cu}} = 3.6\\text{ Å}$ and $d_{\\text{O-O}} = 1.41\\text{ Å}$.
- **Magnetic Properties**: Despite having two $d^9\\,\\text{Cu}^{II}$ ions ($S = 1/2$), oxyhemocyanin is completely diamagnetic at room temperature due to colossal antiferromagnetic superexchange coupling through the bridging peroxide ($|2J| > 600\\text{ cm}^{-1}$).

### Kitajima's Synthetic Hemocyanin Model
In 1989, Nobumasa Kitajima achieved the definitive synthetic biomimetic proof by preparing a dinuclear copper complex using sterically hindered tris(pyrazolyl)borate ligands:
\\[
[\\text{Cu}(\\text{HB}(3,5\\text{-}i\\text{Pr}_2\\text{pz})_3)]_2(\\mu\\text{-}\eta^2:\\eta^2\\text{-O}_2)
\\]
X-ray crystallography verified the identical side-on bridging $\\mu\\text{-}\eta^2:\\eta^2$ geometry, matching the UV-Vis absorption band at $\\lambda = 345\\text{ nm}$ ($\epsilon \\approx 20{,}000\\text{ M}^{-1}\\text{cm}^{-1}$) and the resonance Raman $\\nu(\\text{O-O})$ stretch at $745\\text{ cm}^{-1}$ seen in native hemocyanin."""
        },
        {
            "secNumber": "6.7",
            "title": "Artificial Metalloenzymes: Carbonic Anhydrase & Hydrolytic Catalysts",
            "content": """**Carbonic anhydrase** is one of the fastest enzymes known, catalyzing the reversible hydration of carbon dioxide with turnover frequencies exceeding $k_{\\text{cat}} > 10^6\\text{ s}^{-1}$:
\\[
\\text{CO}_2 + \\text{H}_2\\text{O} \\xrightleftharpoons{k_{\\text{cat}}} \\text{HCO}_3^- + \\text{H}^+
\\]

### Native Active Site & The Zinc-Hydroxide Mechanism
- The active site features a single $\\text{Zn}^{II}$ cation coordinated tetrahedrally to three histidine imidazoles (His 94, His 96, His 119) and a coordinated water molecule:
\\[
[\\text{His}_3\\text{Zn}-\\text{OH}_2]^{2+} \\xrightleftharpoons{K_a} [\\text{His}_3\\text{Zn}-\\text{OH}]^+ + \\text{H}^+
\\]
- Coordination to the Lewis acidic $\\text{Zn}^{II}$ ion polarizes the coordinated water, dramatically lowering its $\\text{p}K_a$ from $15.7$ (bulk water) to **$7.0$** in the enzyme.
- At physiological $\\text{pH} = 7.4$, the enzyme is pre-organized into a potent nucleophilic $[\\text{Zn}-\\text{OH}]^+$ form, which directly attacks the electrophilic carbon of incoming $\\text{CO}_2$.

### Synthetic Biomimetic Models: Kimura's Zinc-Cyclen
Eiichi Kimura developed synthetic macrocyclic models of carbonic anhydrase using **[12]aneN$_4$ (cyclen)**:
- In $[\\text{Zn}(\\text{cyclen})(\\text{OH}_2)]^{2+}$, four secondary nitrogen atoms coordinate in the equatorial plane, leaving one apical site for water coordination.
- The $\\text{p}K_a$ of the zinc-bound water is perturbed to **$7.3$**, closely reproducing the native enzyme.
- The deprotonated complex $[\\text{Zn}(\\text{cyclen})(\\text{OH})]^+$ rapidly hydrates $\\text{CO}_2$ and hydrolyzes activated esters (e.g., $p$-nitrophenyl acetate, PNPA) and phosphate diesters (DNA/RNA model compounds) with rate accelerations of $>10^3$ over uncatalyzed background reactions.
- Dinuclear and trinuclear zinc complexes further accelerate phosphate cleavage through cooperative double-Lewis-acid activation."""
        },
        {
            "secNumber": "6.8",
            "title": "Bioorganic Enzyme Mimics: Cyclodextrin Artificial Esterases & Catalytic Clefts",
            "content": """Beyond metal-based active sites, supramolecular organic hosts mimic the substrate binding, proximity effect, and stereospecificity of enzymes using purely non-covalent cavity interactions.

### Ronald Breslow's Cyclodextrin Artificial Enzymes
Ronald Breslow pioneered the field of **artificial enzymes** using modified cyclodextrins:
1. **Binding Step**: The hydrophobic cyclodextrin cavity serves as the substrate-binding cleft (apoenzyme), selectively capturing aromatic substrates via the hydrophobic effect with high affinity ($K_s = K_d$).
2. **Catalytic Acceleration via Proximity**:
   Native $\\beta$-cyclodextrin accelerates the alkaline hydrolysis of $m$-tert-butylphenyl acetate by a factor of over **$300$** relative to bulk alkaline hydrolysis:
   - The *tert*-butylphenyl group intercalates into the hydrophobic cavity.
   - This inclusion forces the ester carbonyl into direct contact with a secondary hydroxyl group ($\text{C}_2-\\text{OH}$) on the rim.
   - Intramolecular transesterification occurs to form an acyl-cyclodextrin intermediate, followed by hydrolytic deacylation.
3. **Transition-State Geometry and Selectivity**:
   Breslow showed that $m$-substituted phenyl esters are hydrolyzed up to $100$ times faster than $p$-substituted isomers because the meta-ester carbonyl is steered directly toward the rim hydroxyls, whereas the para-ester carbonyl projects away into solution.

### Multi-Functional Artificial Metallo-Esterases
Attaching catalytic functional groups to the cyclodextrin rim creates multi-functional biomimetic catalysts:
- **Bis-Imidazole Cyclodextrins (Ribonuclease Mimics)**: Two imidazole groups attached to diametrically opposite positions of the $\\beta$-CD rim act cooperatively as general acid and general base, mimicking the catalytic mechanism of ribonuclease A (His 12 / His 119) and cleaving RNA phosphodiester bonds with strict regioselectivity.
- **Pyridoxamine Cyclodextrins (Transaminase Mimics)**: A pyridoxamine co-factor tethered to the rim effects enantioselective transamination of keto acids into chiral $\\alpha$-amino acids with enantiomeric excesses exceeding $95\\%\\text{ ee}$."""
        }
    ]

    problems = [
        {
            "probNumber": "6.1",
            "title": "Valinomycin Potassium-to-Sodium Selectivity: Octahedral Coordination vs Hydration",
            "difficulty": "Foundational",
            "statement": """The transport of monovalent alkali metal cations through a lipid bilayer mediated by valinomycin (Val) is governed by the extraction equilibrium:
\\[
\\text{M}^+(\\text{aq}) + \\text{Val}(\\text{lipid}) \\xrightleftharpoons{K_{\\text{ext}}} [\\text{M} \\subset \\text{Val}]^+(\\text{lipid})
\\]
In methanol/lipid media at $298.15\\text{ K}$, the measured extraction constants are:
- $K_{\\text{ext}}(\\text{K}^+) = 2.50 \\times 10^6\\text{ M}^{-1}$
- $K_{\\text{ext}}(\\text{Na}^+) = 1.45 \\times 10^2\\text{ M}^{-1}$
(a) Calculate the selectivity factor $S_{\\text{K/Na}} = K_{\\text{ext}}(\\text{K}^+) / K_{\\text{ext}}(\\text{Na}^+)$ and the difference in extraction free energy $\\Delta \\Delta G_{\\text{ext}}^\circ = \\Delta G_{\\text{ext}}^\circ(\\text{K}^+) - \\Delta G_{\\text{ext}}^\circ(\\text{Na}^+)$.
(b) The standard gas-phase hydration enthalpies of the cations are $\\Delta H_{\\text{hyd}}^\circ(\\text{Na}^+) = -405\\text{ kJ/mol}$ and $\\Delta H_{\\text{hyd}}^\circ(\\text{K}^+) = -321\\text{ kJ/mol}$.
Calculate the difference in dehydration penalty $\\Delta \\Delta H_{\\text{dehyd}} = \\Delta H_{\\text{dehyd}}(\\text{Na}^+) - \\Delta H_{\\text{dehyd}}(\\text{K}^+)$.
(c) Explain why the valinomycin cavity, which contains six carbonyl oxygens with an optimal radius of $1.38\\text{ Å}$, cannot contract to compensate for the higher dehydration penalty of $\\text{Na}^+$.""",
            "solution": """### Step 1: Extraction Selectivity and Free Energy Difference
The potassium-over-sodium selectivity factor is:
\\[
S_{\\text{K/Na}} = \\frac{K_{\\text{ext}}(\\text{K}^+)}{K_{\\text{ext}}(\\text{Na}^+)} = \\frac{2.50 \\times 10^6\\text{ M}^{-1}}{1.45 \\times 10^2\\text{ M}^{-1}} = 17{,}241 \\approx 1.72 \\times 10^4
\\]
Valinomycin exhibits an extraction preference for $\\text{K}^+$ exceeding $17{,}000 : 1$.
The free energy difference at $T = 298.15\\text{ K}$ is:
\\[
\\Delta \\Delta G_{\\text{ext}}^\\circ = -RT \\ln S_{\\text{K/Na}} = -(8.31446 \\times 298.15) \\times \\ln(17{,}241)
\\]
\\[
\\Delta \\Delta G_{\\text{ext}}^\\circ = -2478.96 \\times 9.7550 = -24{,}182\\text{ J/mol} = -24.18\\text{ kJ/mol}
\\]
Binding and extracting $\\text{K}^+$ is favored by $24.18\\text{ kJ/mol}$ over $\\text{Na}^+$.

### Step 2: Dehydration Enthalpy Penalty Difference
Dehydration is the reverse of hydration ($\\Delta H_{\\text{dehyd}} = -\\Delta H_{\\text{hyd}}$):
- For $\\text{Na}^+$: $\\Delta H_{\\text{dehyd}}(\\text{Na}^+) = -(-405) = +405\\text{ kJ/mol}$.
- For $\\text{K}^+$: $\\Delta H_{\\text{dehyd}}(\\text{K}^+) = -(-321) = +321\\text{ kJ/mol}$.
The excess dehydration penalty for $\\text{Na}^+$ is:
\\[
\\Delta \\Delta H_{\\text{dehyd}} = 405 - 321 = +84\\text{ kJ/mol}
\\]
It costs $84\\text{ kJ/mol}$ more energy to strip water from $\\text{Na}^+$ than from $\\text{K}^+$ due to the higher charge density of sodium ($r = 1.02\\text{ Å}$ vs $1.38\\text{ Å}$).

### Step 3: Steric Inability of the Valinomycin Cavity to Contract
To overcome the $+84\\text{ kJ/mol}$ dehydration deficit, a host must coordinate $\\text{Na}^+$ with much shorter, stronger bond distances.
However, in valinomycin:
1. **Hydrogen-Bond Locked Framework**: The peptide backbone is locked into an invariant bracelet shape by six internal $[\\text{N-H}\\cdots\\text{O}=\\text{C}]$ hydrogen bonds between the valine amide groups.
2. **Cavity Rigidity**: Contracting the internal cavity from $r = 1.38\\text{ Å}$ down to $r = 1.02\\text{ Å}$ would require stretching and breaking these six structural hydrogen bonds, incurring a severe conformational strain penalty ($>60\\text{ kJ/mol}$).
3. **Steric Contact Deficit**: Consequently, inside the unyielding $1.38\\text{ Å}$ cavity, the smaller $\\text{Na}^+$ ion "rattles" and cannot establish simultaneous van der Waals contacts with all six ester carbonyl oxygens. The ligand-ion electrostatic interaction is drastically diminished, leaving the huge dehydration penalty uncompensated and preventing sodium extraction."""
        },
        {
            "probNumber": "6.2",
            "title": "Electronic Spectroscopy of Porphyrin Axial Coordination: Soret & Q-Band Shifts",
            "difficulty": "Foundational",
            "statement": """An iron(III) tetraphenylporphyrin chloride complex, $[\\text{Fe}^{III}(\\text{TPP})\\text{Cl}]$, exists as a five-coordinate high-spin ($S = 5/2$) complex in dichloromethane, displaying a Soret band at $\\lambda_{\\max} = 416\\text{ nm}$ ($\\epsilon = 1.15 \\times 10^5\\text{ M}^{-1}\\text{cm}^{-1}$).
Upon addition of excess 1-methylimidazole (1-MeIm), a six-coordinate low-spin ($S = 1/2$) bis-imidazole complex $[\\text{Fe}^{III}(\\text{TPP})(1\\text{-MeIm})_2]^+$ forms:
- The Soret band bathochromically shifts to $\\lambda_{\\max} = 428\\text{ nm}$ ($\\epsilon = 1.30 \\times 10^5\\text{ M}^{-1}\\text{cm}^{-1}$).
- A single isosbestic point is observed at $\\lambda_{\\text{iso}} = 421\\text{ nm}$ with $\\epsilon_{\\text{iso}} = 9.80 \\times 10^4\\text{ M}^{-1}\\text{cm}^{-1}$.
(a) Calculate the red shift in transition energy $\\Delta E = E_{\\text{final}} - E_{\\text{initial}}$ in $\\text{eV}$ and in $\\text{kJ/mol}$.
(b) In an intermediate titration solution, the measured optical absorbance at the starting wavelength $\\lambda = 416\\text{ nm}$ in a $1.00\\text{ cm}$ pathlength cuvette drops from an initial value of $A_0 = 1.150$ to $A_{\\text{obs}} = 0.520$. Given that the molar absorptivity of the final bis-imidazole complex at $416\\text{ nm}$ is $\\epsilon_2(416) = 4.20 \\times 10^4\\text{ M}^{-1}\\text{cm}^{-1}$, calculate:
    (i) The molar fraction $\\alpha$ of the complex converted to the six-coordinate form,
    (ii) The expected absorbance at the isosbestic point $\\lambda = 421\\text{ nm}$.
(c) Explain the origin of the Soret band red shift in terms of Gouterman's four-orbital model upon transition from high-spin to low-spin iron(III).""",
            "solution": """### Step 1: Transition Energy Red Shift
Initial transition energy ($\lambda_1 = 416\\text{ nm} = 4.16 \\times 10^{-7}\\text{ m}$):
\\[
E_1 = \\frac{h c}{\\lambda_1} = \\frac{(6.62607 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(2.99792 \\times 10^8\\text{ m/s})}{4.16 \\times 10^{-7}\\text{ m}} = \\frac{1.98644 \\times 10^{-25}}{4.16 \\times 10^{-7}} = 4.7751 \\times 10^{-19}\\text{ J}
\\]
Converting to $\\text{eV}$ ($1\\text{ eV} = 1.60218 \\times 10^{-19}\\text{ J}$):
\\[
E_1 = \\frac{4.7751 \\times 10^{-19}}{1.60218 \\times 10^{-19}} = 2.9804\\text{ eV}
\\]
Final transition energy ($\lambda_2 = 428\\text{ nm} = 4.28 \\times 10^{-7}\\text{ m}$):
\\[
E_2 = \\frac{1.98644 \\times 10^{-25}}{4.28 \\times 10^{-7}} = 4.6412 \\times 10^{-19}\\text{ J} = 2.8968\\text{ eV}
\\]
The change in transition energy is:
\\[
\\Delta E = E_2 - E_1 = 2.8968 - 2.9804 = -0.0836\\text{ eV}
\\]
In $\\text{kJ/mol}$ ($N_A \\times \\Delta E$):
\\[
\\Delta E = (-0.0836\\text{ eV}) \\times (96.485\\text{ kJ/(mol}\\cdot\\text{eV)}) = -8.066\\text{ kJ/mol}
\\]

### Step 2: Molar Conversion Fraction and Isosbestic Absorbance
Initial absorbance:
\\[
A_0 = \\epsilon_1(416) \\cdot C_0 \\cdot l \\implies C_0 = \\frac{1.150}{1.15 \\times 10^5 \\times 1.00} = 1.00 \\times 10^{-5}\\text{ M}
\\]
In the mixture containing mole fraction $(1 - \\alpha)$ of initial species and $\\alpha$ of final species:
\\[
A_{\\text{obs}}(416) = \\left[ (1 - \\alpha) \\epsilon_1(416) + \\alpha \\epsilon_2(416) \\right] C_0 \\cdot l
\\]
Substitute values:
\\[
0.520 = \\left[ (1 - \\alpha)(1.15 \\times 10^5) + \\alpha(0.42 \\times 10^5) \\right] (1.00 \\times 10^{-5})
\\]
\\[
52{,}000 = 115{,}000 - 115{,}000 \\alpha + 42{,}000 \\alpha = 115{,}000 - 73{,}000 \\alpha
\\]
\\[
73{,}000 \\alpha = 115{,}000 - 52{,}000 = 63{,}000
\\]
\\[
\\alpha = \\frac{63{,}000}{73{,}000} = 0.8630 \\implies 86.30\\%
\\]
- **Absorbance at Isosbestic Point ($\lambda = 421\text{ nm}$)**:
At an isosbestic point, the molar absorptivity is independent of the conversion fraction: $\\epsilon_{\\text{iso}} = 9.80 \\times 10^4\\text{ M}^{-1}\\text{cm}^{-1}$.
\\[
A(421) = \\epsilon_{\\text{iso}} \\cdot C_0 \\cdot l = (9.80 \\times 10^4\\text{ M}^{-1}\\text{cm}^{-1}) \\times (1.00 \\times 10^{-5}\\text{ M}) \\times (1.00\\text{ cm}) = 0.980
\\]
The absorbance remains constant at $0.980$ at all stages of the titration.

### Step 3: Electronic Origin of the Red Shift
In five-coordinate high-spin $\\text{Fe}^{III}$ ($S = 5/2$), the high-spin iron ion has electrons in the antibonding $d_{x^2-y^2}$ and $d_{z^2}$ orbitals. Its ionic radius is large ($r \\approx 0.645\\text{ Å}$), displacing the iron atom $0.50\\text{ Å}$ out of the porphyrin $\\text{N}_4$ plane toward the chloride ligand.
Upon coordination of two strong-field imidazole ligands to form six-coordinate low-spin $\\text{Fe}^{III}$ ($S = 1/2$):
1. The $d_{x^2-y^2}$ orbital is vacated ($t_{2g}^5 e_g^0$).
2. The smaller low-spin iron atom contracts into the exact plane of the porphyrin macrocycle (out-of-plane displacement $\\approx 0\\text{ Å}$).
3. In-plane planarization enhances $\\pi$-conjugation and metal-to-ligand backbonding ($d_\\pi \\rightarrow e_g^*$).
4. This stabilizes the unoccupied $e_g(\\pi^*)$ LUMO relative to the $a_{1u}/a_{2u}$ HOMO, narrowing the HOMO-LUMO energy gap and shifting the allowed Soret transition to a longer wavelength."""
        },
        {
            "probNumber": "6.3",
            "title": "Bimolecular Dimerization Kinetics of Unhindered Iron(II) Porphyrins",
            "difficulty": "Foundational",
            "statement": """An unhindered synthetic iron(II) porphyrin, $\\text{Fe}^{II}(\\text{TPP})$, is exposed to dioxygen in dry toluene at $T = 298.15\\text{ K}$ with an initial porphyrin concentration $[\\text{Fe}]_0 = 5.00 \\times 10^{-4}\\text{ M}$.
The mechanism follows the classic four-step sequence:
1. $\\text{Fe}^{II} + \\text{O}_2 \\xrightleftharpoons[k_{-1}]{k_1} \\text{Fe}(\\text{O}_2)$ (rapid pre-equilibrium, $K_1 = k_1 / k_{-1} = 3.20 \\times 10^2\\text{ M}^{-1}$)
2. $\\text{Fe}(\\text{O}_2) + \\text{Fe}^{II} \\xrightarrow{k_2} \\text{Fe}-\\text{O-O}-\\text{Fe}$ (rate-determining bimolecular step, $k_2 = 1.40 \\times 10^4\\text{ M}^{-1}\\text{s}^{-1}$)
3. $\\text{Fe}-\\text{O-O}-\\text{Fe} \\xrightarrow{\\text{fast}} 2\\,\\text{Fe}^{IV}=\\text{O}$
4. $\\text{Fe}^{IV}=\\text{O} + \\text{Fe}^{II} \\xrightarrow{\\text{fast}} \\text{Fe}^{III}-\\text{O}-\\text{Fe}^{III}$
(a) Derive the steady-state rate law for the disappearance of active iron(II) porphyrin, $-\\frac{d[\\text{Fe}^{II}]}{dt}$, in terms of $[\\text{Fe}^{II}]$, $[\\text{O}_2]$, $K_1$, and $k_2$.
(b) In toluene saturated with oxygen under $P_{\\text{O}_2} = 1.00\\text{ atm}$ ($[\\text{O}_2] = 9.10 \\times 10^{-3}\\text{ M}$), calculate the initial rate of dimerization $r_0$ in $\\text{M/s}$.
(c) Calculate the time $t_{90\\%}$ required for $90\\%$ of the iron(II) porphyrin to be converted into the catalytically inactive $\\mu$-oxo dimer under pseudo-second-order conditions.""",
            "solution": """### Step 1: Derivation of the Rate Law
From the reaction sequence:
Step 2 consumes two iron atoms: one as $\\text{Fe}(\\text{O}_2)$ and one as $\\text{Fe}^{II}$.
Then Step 3 generates two $\\text{Fe}^{IV}=\\text{O}$, and Step 4 consumes two more $\\text{Fe}^{II}$.
Total stoichiometry: $4\\,\\text{Fe}^{II} + \\text{O}_2 \\longrightarrow 2\\,\\text{Fe}^{III}-\\text{O}-\\text{Fe}^{III}$.
Rate of the rate-determining step:
\\[
r_{\\text{RDS}} = k_2 [\\text{Fe}(\\text{O}_2)] [\\text{Fe}^{II}]
\\]
Because Step 1 is a rapid pre-equilibrium:
\\[
[\\text{Fe}(\\text{O}_2)] = K_1 [\\text{Fe}^{II}] [\\text{O}_2]
\\]
Substitute into $r_{\\text{RDS}}$:
\\[
r_{\\text{RDS}} = k_2 K_1 [\\text{O}_2] [\\text{Fe}^{II}]^2
\\]
Since 4 molecules of $\\text{Fe}^{II}$ are consumed per turnover of the rate-determining step:
\\[
-\\frac{d[\\text{Fe}^{II}]}{dt} = 4 k_2 K_1 [\\text{O}_2] [\\text{Fe}^{II}]^2 = k_{\\text{obs}} [\\text{Fe}^{II}]^2
\\]
where the apparent second-order rate constant is $k_{\\text{obs}} = 4 k_2 K_1 [\\text{O}_2]$.

### Step 2: Initial Rate Calculation
Given:
- $K_1 = 3.20 \\times 10^2\\text{ M}^{-1}$
- $k_2 = 1.40 \\times 10^4\\text{ M}^{-1}\\text{s}^{-1}$
- $[\\text{O}_2] = 9.10 \\times 10^{-3}\\text{ M}$
- $[\\text{Fe}^{II}]_0 = 5.00 \\times 10^{-4}\\text{ M}$

Calculate $k_{\\text{obs}}$:
\\[
k_{\\text{obs}} = 4 \\times (1.40 \\times 10^4) \\times (3.20 \\times 10^2) \\times (9.10 \\times 10^{-3})
\\]
\\[
k_{\\text{obs}} = 4 \\times (4.48 \\times 10^6) \\times (9.10 \\times 10^{-3}) = 1.792 \\times 10^7 \\times 9.10 \\times 10^{-3} = 1.6307 \\times 10^5\\text{ M}^{-1}\\text{s}^{-1}
\\]
Initial rate:
\\[
r_0 = k_{\\text{obs}} [\\text{Fe}^{II}]_0^2 = (1.6307 \\times 10^5\\text{ M}^{-1}\\text{s}^{-1}) \\times (5.00 \\times 10^{-4}\\text{ M})^2
\\]
\\[
r_0 = (1.6307 \\times 10^5) \\times (2.50 \\times 10^{-7}) = 4.077 \\times 10^{-2}\\text{ M/s} = 40.77\\text{ mM/s}
\\]

### Step 3: Time for $90\%$ Degradation ($t_{90\%}$)
Under constant $[\\text{O}_2]$, the decay follows second-order kinetics:
\\[
\\frac{1}{[\\text{Fe}^{II}](t)} - \\frac{1}{[\\text{Fe}^{II}]_0} = k_{\\text{obs}} t
\\]
For $90\\%$ conversion, $[\\text{Fe}^{II}](t) = 0.10 [\\text{Fe}^{II}]_0$:
\\[
\\frac{1}{0.10 [\\text{Fe}^{II}]_0} - \\frac{1}{[\\text{Fe}^{II}]_0} = \\frac{10 - 1}{[\\text{Fe}^{II}]_0} = \\frac{9}{[\\text{Fe}^{II}]_0}
\\]
Thus:
\\[
t_{90\\%} = \\frac{9}{k_{\\text{obs}} [\\text{Fe}^{II}]_0} = \\frac{9}{(1.6307 \\times 10^5\\text{ M}^{-1}\\text{s}^{-1}) \\times (5.00 \\times 10^{-4}\\text{ M})}
\\]
\\[
t_{90\\%} = \\frac{9}{81.536\\text{ s}^{-1}} = 0.1104\\text{ s} = 110\\text{ ms}
\\]
In unhindered iron porphyrin solutions at room temperature, over $90\\%$ of the active iron is irreversibly destroyed in just 110 milliseconds, proving why steric protection (picket fences or globin cavities) is strictly essential for reversible oxygenation."""
        },
        {
            "probNumber": "6.4",
            "title": "Thermodynamics of Reversible O2 Binding in Collman's Picket-Fence Porphyrin",
            "difficulty": "Intermediate",
            "statement": """Collman's picket-fence iron(II) complex, $\\text{Fe}(\\text{TpivPP})(1,2\\text{-Me}_2\\text{Im})$, binds molecular oxygen reversibly in solid-state and non-coordinating solvents (toluene) without forming $\\mu$-oxo dimers:
\\[
\\text{Fe} + \\text{O}_2 \\xrightleftharpoons{K_{\\text{O}_2}} \\text{Fe}(\\text{O}_2)
\\]
The partial pressure of oxygen required for half-saturation ($P_{1/2}$) was determined at two temperatures:
- At $T_1 = 293.15\\text{ K}$ ($20^\\circ\\text{C}$): $P_{1/2} = 38.0\\text{ torr}$
- At $T_2 = 273.15\\text{ K}$ ($0^\\circ\\text{C}$): $P_{1/2} = 5.20\\text{ torr}$
(a) Using $K_{\\text{O}_2} = (P_{1/2})^{-1}$, calculate $K_{\\text{O}_2}$ in $\\text{torr}^{-1}$ and in $\\text{atm}^{-1}$ at both temperatures ($1\\text{ atm} = 760\\text{ torr}$).
(b) Using the van 't Hoff equation, determine the standard enthalpy of oxygenation $\\Delta H^\circ$ (in $\\text{kJ/mol}$) and standard entropy of oxygenation $\\Delta S^\circ$ (in $\\text{J/(mol}\\cdot\\text{K)}$ with standard state $P^\circ = 1\\text{ atm}$).
(c) Compare these synthetic thermodynamic parameters with native human myoglobin ($\\Delta H^\circ = -62\\text{ kJ/mol}$, $\\Delta S^\circ = -138\\text{ J/(mol}\\cdot\\text{K)}$) and discuss the role of the picket-fence hydrogen bonds in mimicking the globin pocket.""",
            "solution": """### Step 1: Equilibrium Association Constants
1. **At $T_1 = 293.15\\text{ K}$**:
\\[
K_1 = \\frac{1}{P_{1/2}} = \\frac{1}{38.0\\text{ torr}} = 0.026316\\text{ torr}^{-1}
\\]
In $\\text{atm}^{-1}$:
\\[
K_1 = 0.026316 \\times 760 = 20.00\\text{ atm}^{-1}
\\]
2. **At $T_2 = 273.15\\text{ K}$**:
\\[
K_2 = \\frac{1}{5.20\\text{ torr}} = 0.192308\\text{ torr}^{-1}
\\]
In $\\text{atm}^{-1}$:
\\[
K_2 = 0.192308 \\times 760 = 146.15\\text{ atm}^{-1}
\\]

### Step 2: Enthalpy and Entropy of Oxygenation
From the two-point van 't Hoff equation:
\\[
\\ln\\left( \\frac{K_2}{K_1} \\right) = -\\frac{\\Delta H^\\circ}{R} \\left( \\frac{1}{T_2} - \\frac{1}{T_1} \\right)
\\]
Substitute values:
\\[
\\ln\\left( \\frac{146.15}{20.00} \\right) = \\ln(7.3075) = 1.9889
\\]
\\[
\\frac{1}{T_2} - \\frac{1}{T_1} = \\frac{1}{273.15} - \\frac{1}{293.15} = 3.66099 \\times 10^{-3} - 3.41122 \\times 10^{-3} = 2.4977 \\times 10^{-4}\\text{ K}^{-1}
\\]
Thus:
\\[
\\Delta H^\\circ = -\\frac{R \\times 1.9889}{2.4977 \\times 10^{-4}} = -\\frac{8.31446 \\times 1.9889}{2.4977 \\times 10^{-4}} = -\\frac{16.5366}{2.4977 \\times 10^{-4}} = -66{,}207\\text{ J/mol} = -66.21\\text{ kJ/mol}
\\]
Now compute $\\Delta S^\circ$ (standard state $P^\circ = 1\\text{ atm}$):
At $T_1 = 293.15\\text{ K}$, $\\Delta G_1^\circ = -RT_1 \\ln K_1$:
\\[
\\Delta G_1^\\circ = -(8.31446 \\times 293.15) \\times \\ln(20.00) = -2{,}437.38 \\times 2.99573 = -7{,}301.8\\text{ J/mol} = -7.302\\text{ kJ/mol}
\\]
\\[
\\Delta S^\\circ = \\frac{\\Delta H^\\circ - \\Delta G_1^\\circ}{T_1} = \\frac{-66{,}207 - (-7{,}302)}{293.15} = \\frac{-58{,}905}{293.15} = -200.94\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 3: Comparison with Native Myoglobin
- **Enthalpy Match**: The synthetic picket-fence porphyrin exhibits $\\Delta H^\circ = -66.2\\text{ kJ/mol}$, remarkably close to native myoglobin ($-62\\text{ kJ/mol}$). This demonstrates that the iron-dioxygen coordination bond energy in the synthetic picket enclosure is virtually identical to that within the biological protein active site.
- **Entropy Differences**: The entropy loss in the model system ($-201\\text{ J/(mol}\\cdot\\text{K)}$) is more negative than in myoglobin ($-138\\text{ J/(mol}\\cdot\\text{K)}$). In the protein, the pre-organized tertiary globin matrix already restricts conformational mobility and traps water, mitigating the net entropic loss upon $\\text{O}_2$ capture, whereas the synthetic picket-fence pivalamide pickets experience a slight decrease in internal vibrational/rotational freedom upon binding $\\text{O}_2$."""
        },
        {
            "probNumber": "6.5",
            "title": "Distal Steric Hindrance & CO/O2 Partition Ratio in Biomimetic Porphyrins",
            "difficulty": "Intermediate",
            "statement": """Carbon monoxide binds with high affinity to unhindered iron(II) porphyrins because the $\\text{Fe-C}\\equiv\\text{O}$ coordination geometry prefers a strictly linear perpendicular orientation ($\angle \\text{Fe-C-O} = 180^\\circ$). In contrast, $\\text{Fe}-\\text{O}_2$ binding occurs naturally in a bent geometry ($\angle \\text{Fe-O-O} \\approx 115^\\circ - 120^\\circ$).
The relative affinity is quantified by the partition coefficient $M$:
\\[
M = \\frac{K_{\\text{CO}}}{K_{\\text{O}_2}} = \\frac{P_{1/2}(\\text{O}_2)}{P_{1/2}(\\text{CO})}
\\]
- For an unhindered flat model complex (flat porphyrin + 1-methylimidazole in benzene):
  $K_{\\text{CO}} = 1.20 \\times 10^8\\text{ atm}^{-1}$ and $K_{\\text{O}_2} = 4.80 \\times 10^3\\text{ atm}^{-1}$.
- In a "strapped" or "pocket" porphyrin model with a short distal hydrocarbon strap that physically impedes perpendicular linear binding at a height $h < 4.0\\text{ Å}$ above the iron center:
  $K_{\\text{CO}} = 8.50 \\times 10^4\\text{ atm}^{-1}$ and $K_{\\text{O}_2} = 4.25 \\times 10^3\\text{ atm}^{-1}$.
(a) Calculate the partition coefficient $M$ for the unhindered model versus the strapped pocket model.
(b) Calculate the discrimination factor $D = M_{\\text{unhindered}} / M_{\\text{strapped}}$.
(c) If blood or a biomimetic carrier is exposed to an ambient gas mixture containing trace carbon monoxide ($P_{\\text{CO}} = 1.00 \\times 10^{-4}\\text{ atm}$) and normal oxygen ($P_{\\text{O}_2} = 0.200\\text{ atm}$), calculate the fractional saturation of the iron sites with $\\text{CO}$ ($Y_{\\text{CO}}$) for both the unhindered and strapped systems.""",
            "solution": """### Step 1: Partition Coefficient Calculation
1. **Unhindered Model**:
\\[
M_{\\text{unhindered}} = \\frac{K_{\\text{CO}}}{K_{\\text{O}_2}} = \\frac{1.20 \\times 10^8\\text{ atm}^{-1}}{4.80 \\times 10^3\\text{ atm}^{-1}} = 25{,}000
\\]
In the unhindered system, carbon monoxide binds $25{,}000$ times more tightly than dioxygen.

2. **Strapped Pocket Model**:
\\[
M_{\\text{strapped}} = \\frac{K_{\\text{CO}}}{K_{\\text{O}_2}} = \\frac{8.50 \\times 10^4\\text{ atm}^{-1}}{4.25 \\times 10^3\\text{ atm}^{-1}} = 20.0
\\]
In the strapped model, the carbon monoxide preference is reduced to a factor of only $20$.

### Step 2: Discrimination Factor
The discrimination factor achieved by distal steric hindrance is:
\\[
D = \\frac{M_{\\text{unhindered}}}{M_{\\text{strapped}}} = \\frac{25{,}000}{20.0} = 1{,}250
\\]
The strapped distal pocket discriminates against carbon monoxide by a factor of $1{,}250$.
- **Structural Origin**: The rigid hydrocarbon strap forces incoming ligands to bend. Because dioxygen binds naturally in a bent geometry ($\angle \\text{Fe-O-O} = 115^\\circ$), it slips beneath the strap with virtually zero steric penalty (affinity decreases by only $11\\%$, from $4.80 \\times 10^3$ to $4.25 \\times 10^3\\text{ atm}^{-1}$). In contrast, carbon monoxide strongly prefers linear geometry ($\angle \\text{Fe-C-O} = 180^\\circ$); bending it or distorting the porphyrin core incurs a huge steric energy penalty, dropping $K_{\\text{CO}}$ by a factor of over $1{,}400$.

### Step 3: Fractional Saturation with CO
In the presence of both $\\text{CO}$ and $\\text{O}_2$, competitive binding yields:
\\[
Y_{\\text{CO}} = \\frac{K_{\\text{CO}} P_{\\text{CO}}}{1 + K_{\\text{CO}} P_{\\text{CO}} + K_{\\text{O}_2} P_{\\text{O}_2}}
\\]
Given: $P_{\\text{CO}} = 1.00 \\times 10^{-4}\\text{ atm}$, $P_{\\text{O}_2} = 0.200\\text{ atm}$.

1. **Unhindered Model**:
- $K_{\\text{CO}} P_{\\text{CO}} = (1.20 \\times 10^8) \\times (1.00 \\times 10^{-4}) = 12{,}000$
- $K_{\\text{O}_2} P_{\\text{O}_2} = (4.80 \\times 10^3) \\times 0.200 = 960$
\\[
Y_{\\text{CO}} = \\frac{12{,}000}{1 + 12{,}000 + 960} = \\frac{12{,}000}{12{,}961} = 0.9258 \\implies 92.58\\%
\\]
The unhindered model is poisoned: over $92.5\\%$ of all iron centers are locked by trace $\\text{CO}$.

2. **Strapped Pocket Model**:
- $K_{\\text{CO}} P_{\\text{CO}} = (8.50 \\times 10^4) \\times (1.00 \\times 10^{-4}) = 8.50$
- $K_{\\text{O}_2} P_{\\text{O}_2} = (4.25 \\times 10^3) \\times 0.200 = 850$
\\[
Y_{\\text{CO}} = \\frac{8.50}{1 + 8.50 + 850} = \\frac{8.50}{859.50} = 0.00989 \\implies 0.99\\%
\\]
Under identical atmospheric conditions, less than $1\\%$ of the strapped model is poisoned by $\\text{CO}$, demonstrating how distal steric control enables survival in environments containing trace carbon monoxide."""
        },
        {
            "probNumber": "6.6",
            "title": "Biomimetic Carbonic Anhydrase Catalysis: Zinc(II)-Hydroxide Kinetics",
            "difficulty": "Intermediate",
            "statement": """A synthetic carbonic anhydrase mimic, $[\\text{Zn}^{II}(\\text{cyclen})]^{2+}$, catalyzes the hydration of dissolved carbon dioxide in aqueous solution at $T = 298.15\\text{ K}$:
\\[
[\\text{Zn}(\\text{cyclen})(\\text{OH}_2)]^{2+} \\xrightleftharpoons{K_a} [\\text{Zn}(\\text{cyclen})(\\text{OH})]^+ + \\text{H}^+ \\quad (\\text{p}K_a = 7.30)
\\]
The deprotonated monohydroxo form is the active nucleophile, attacking $\\text{CO}_2$ with a second-order rate constant $k_2 = 2.80 \\times 10^3\\text{ M}^{-1}\\text{s}^{-1}$:
\\[
[\\text{Zn}(\\text{cyclen})(\\text{OH})]^+ + \\text{CO}_2 \\xrightarrow{k_2} [\\text{Zn}(\\text{cyclen})(\\text{HCO}_3)]^+
\\]
(a) Calculate the fraction of active zinc-hydroxide complex, $\\alpha_{\\text{OH}}$, as a function of $\\text{pH}$ at:
    (i) $\\text{pH} = 6.00$,
    (ii) $\\text{pH} = 7.30$,
    (iii) $\\text{pH} = 8.00$.
(b) Calculate the effective pseudo-first-order rate constant $k_{\\text{obs}} = k_2 \\alpha_{\\text{OH}} [\\text{Zn}]_{\\text{total}}$ at $\\text{pH} = 7.30$ and $[\\text{Zn}]_{\\text{total}} = 5.00 \\times 10^{-3}\\text{ M}$.
(c) The uncatalyzed hydration of $\\text{CO}_2$ has a rate constant $k_0 = 3.70 \\times 10^{-2}\\text{ s}^{-1}$. Calculate the catalytic acceleration factor $\\text{Rate}_{\\text{cat}} / \\text{Rate}_{\\text{uncat}}$ under the conditions of part (b).""",
            "solution": """### Step 1: Fraction of Active Zinc-Hydroxide Species
From the acid dissociation equilibrium:
\\[
\\alpha_{\\text{OH}} = \\frac{[\\text{Zn}-\\text{OH}^+]}{[\\text{Zn}]_{\\text{total}}} = \\frac{K_a}{K_a + [\\text{H}^+]} = \\frac{1}{1 + 10^{\\text{p}K_a - \\text{pH}}}
\\]
With $\\text{p}K_a = 7.30$:

1. **At $\\text{pH} = 6.00$**:
\\[
\\text{p}K_a - \\text{pH} = 7.30 - 6.00 = +1.30
\\]
\\[
\\alpha_{\\text{OH}}(6.00) = \\frac{1}{1 + 10^{1.30}} = \\frac{1}{1 + 19.95} = \\frac{1}{20.95} = 0.04773 \\implies 4.77\\%
\\]

2. **At $\\text{pH} = 7.30$**:
\\[
\\text{p}K_a - \\text{pH} = 0.00
\\]
\\[
\\alpha_{\\text{OH}}(7.30) = \\frac{1}{1 + 1} = 0.5000 \\implies 50.00\\%
\\]

3. **At $\\text{pH} = 8.00$**:
\\[
\\text{p}K_a - \\text{pH} = 7.30 - 8.00 = -0.70
\\]
\\[
\\alpha_{\\text{OH}}(8.00) = \\frac{1}{1 + 10^{-0.70}} = \\frac{1}{1 + 0.1995} = \\frac{1}{1.1995} = 0.8337 \\implies 83.37\\%
\\]

### Step 2: Pseudo-First-Order Rate Constant at $\text{pH} = 7.30$
Given:
- $k_2 = 2.80 \\times 10^3\\text{ M}^{-1}\\text{s}^{-1}$
- $\\alpha_{\\text{OH}} = 0.5000$
- $[\\text{Zn}]_{\\text{total}} = 5.00 \\times 10^{-3}\\text{ M}$
The effective pseudo-first-order rate constant for $\\text{CO}_2$ disappearance is:
\\[
k_{\\text{obs}} = k_2 \\alpha_{\\text{OH}} [\\text{Zn}]_{\\text{total}} = (2.80 \\times 10^3\\text{ M}^{-1}\\text{s}^{-1}) \\times (0.5000) \\times (5.00 \\times 10^{-3}\\text{ M})
\\]
\\[
k_{\\text{obs}} = (1.40 \\times 10^3) \\times (5.00 \\times 10^{-3}) = 7.00\\text{ s}^{-1}
\\]

### Step 3: Catalytic Acceleration Factor
The uncatalyzed rate is governed by $k_0 = 3.70 \\times 10^{-2}\\text{ s}^{-1}$.
The catalytic acceleration factor is:
\\[
\\frac{\\text{Rate}_{\\text{cat}}}{\\text{Rate}_{\\text{uncat}}} = \\frac{k_{\\text{obs}}}{k_0} = \\frac{7.00\\text{ s}^{-1}}{3.70 \\times 10^{-2}\\text{ s}^{-1}} = 189.2 \\approx 189
\\]
At $5.0\\text{ mM}$ concentration at neutral $\\text{pH}$, Kimura's zinc-cyclen complex accelerates carbon dioxide hydration by a factor of 189 over the uncatalyzed background rate."""
        },
        {
            "probNumber": "6.7",
            "title": "Dinuclear Copper Hemocyanin Model: Antiferromagnetic Exchange Coupling",
            "difficulty": "Advanced",
            "statement": """Kitajima's synthetic oxyhemocyanin model, $[\\{\\text{Cu}^{II}(\\text{HB}(3,5\\text{-}i\\text{Pr}_2\\text{pz})_3)\\}_2(\\mu\\text{-}\eta^2:\\eta^2\\text{-O}_2)]$, contains two copper(II) ions ($S_1 = 1/2, S_2 = 1/2$) bridged by a peroxide dianion in a side-on planar rhombus.
The magnetic interaction between the two copper centers is modeled by the isotropic Heisenberg-Dirac-van Vleck (HDVV) spin Hamiltonian:
\\[
\\hat{H} = -2J (\\hat{\\mathbf{S}}_1 \\cdot \\hat{\\mathbf{S}}_2)
\\]
where $J$ is the exchange coupling constant. The total spin states are singlet ($S = 0$) and triplet ($S = 1$).
(a) Determine the energy separation $\\Delta E = E(S = 1) - E(S = 0)$ between the triplet and singlet states in terms of $J$.
(b) Using the Bleaney-Bowers equation for molar magnetic susceptibility $\\chi_M$:
\\[
\\chi_M(T) = \\frac{2 N_A g^2 \\mu_B^2}{k_B T \\left[ 3 + \\exp\\left( -\\frac{2J}{k_B T} \\right) \\right]}
\\]
derive the expression for the effective magnetic moment $\\mu_{\\text{eff}} = \\sqrt{8 \\chi_M T}$ (in Bohr magnetons, $\\mu_B$).
(c) Magnetic susceptibility measurements indicate that at $T = 300\\text{ K}$, the complex is completely diamagnetic with $\\chi_M \\approx 0$ and an experimental upper bound on magnetic moment $\\mu_{\\text{eff}} < 0.10\\,\\mu_B$ (with $g = 2.10$).
Calculate the lower limit of the antiferromagnetic coupling constant $|-2J|$ in $\\text{cm}^{-1}$ and in $\\text{kJ/mol}$.""",
            "solution": """### Step 1: Energy Separation from Spin Hamiltonian
For two interacting spins $S_1 = 1/2$ and $S_2 = 1/2$:
Total spin $\\mathbf{S} = \\mathbf{S}_1 + \\mathbf{S}_2$ can take values $S = 0$ (singlet) and $S = 1$ (triplet).
Using the identity:
\\[
\\hat{\\mathbf{S}}^2 = \\hat{\\mathbf{S}}_1^2 + \\hat{\\mathbf{S}}_2^2 + 2(\\hat{\\mathbf{S}}_1 \\cdot \\hat{\\mathbf{S}}_2) \\implies 2(\\hat{\\mathbf{S}}_1 \\cdot \\hat{\\mathbf{S}}_2) = \\hat{\\mathbf{S}}^2 - \\hat{\\mathbf{S}}_1^2 - \\hat{\\mathbf{S}}_2^2
\\]
The energy eigenvalues are:
\\[
E(S) = -J [S(S + 1) - S_1(S_1 + 1) - S_2(S_2 + 1)] = -J \\left[ S(S + 1) - \\frac{3}{4} - \\frac{3}{4} \\right] = -J \\left[ S(S + 1) - \\frac{3}{2} \\right]
\\]
- For singlet state ($S = 0$):
  \\[
  E(0) = -J \\left( 0 - \\frac{3}{2} \\right) = +\\frac{3}{2} J
  \\]
- For triplet state ($S = 1$):
  \\[
  E(1) = -J \\left( 2 - \\frac{3}{2} \\right) = -\\frac{1}{2} J
  \\]
The energy separation is:
\\[
\\Delta E = E(1) - E(0) = -\\frac{1}{2} J - \\left( +\\frac{3}{2} J \\right) = -2J
\\]
For antiferromagnetic coupling, $J < 0$, meaning the singlet ground state is lower in energy than the triplet by $|2J| = -2J$.

### Step 2: Bleaney-Bowers Expression for Effective Magnetic Moment
From $\\mu_{\\text{eff}} = \\sqrt{8 \\chi_M T}$:
\\[
\\chi_M T = \\frac{2 N_A g^2 \\mu_B^2}{k_B \\left[ 3 + \\exp\\left( \\frac{-2J}{k_B T} \\right) \\right]}
\\]
Using the constant $N_A \\mu_B^2 / k_B = 0.12505\\text{ cm}^3\\cdot\\text{K/mol}$:
\\[
\\mu_{\\text{eff}}^2 = 8 \\chi_M T = \\frac{16 \\times 0.12505 \\times g^2}{3 + \\exp(-2J / k_B T)} = \\frac{2 g^2}{3 + \\exp(-2J / k_B T)}
\\]
\\[
\\mu_{\\text{eff}} = g \\sqrt{\\frac{2}{3 + \\exp(-2J / k_B T)}}
\\]

### Step 3: Lower Bound on Coupling Constant $|-2J|$
Given $\\mu_{\\text{eff}} < 0.10\\,\\mu_B$ at $T = 300\\text{ K}$ with $g = 2.10$:
\\[
\\frac{\\mu_{\\text{eff}}}{g} = \\frac{0.10}{2.10} = 0.047619
\\]
\\[
\\left( \\frac{\\mu_{\\text{eff}}}{g} \\right)^2 = (0.047619)^2 = 2.2676 \\times 10^{-3}
\\]
\\[
\\frac{2}{3 + \\exp(-2J / k_B T)} < 2.2676 \\times 10^{-3}
\\]
\\[
3 + \\exp(-2J / k_B T) > \\frac{2}{2.2676 \\times 10^{-3}} = 882.0
\\]
\\[
\\exp(-2J / k_B T) > 879.0
\\]
Taking the natural logarithm:
\\[
-\\frac{2J}{k_B T} > \\ln(879.0) = 6.7788
\\]
At $T = 300\\text{ K}$, $k_B T = (0.69503\\text{ cm}^{-1}\\text{/K}) \\times 300\\text{ K} = 208.51\\text{ cm}^{-1}$:
\\[
|-2J| > 6.7788 \\times 208.51\\text{ cm}^{-1} = 1{,}413\\text{ cm}^{-1}
\\]
Converting $\\text{cm}^{-1}$ to $\\text{kJ/mol}$ ($1\\text{ cm}^{-1} = 0.011963\\text{ kJ/mol}$):
\\[
|-2J| > 1{,}413 \\times 0.011963 = 16.91\\text{ kJ/mol}
\\]
The antiferromagnetic exchange coupling constant satisfies $|-2J| > 1{,}400\\text{ cm}^{-1}$, confirming why the complex is completely diamagnetic at room temperature due to colossal superexchange through the bridging peroxide $\\pi^*$ orbitals."""
        },
        {
            "probNumber": "6.8",
            "title": "Kinetics of Cyclodextrin Artificial Esterases: Acylation vs Deacylation",
            "difficulty": "Advanced",
            "statement": """A modified $\\beta$-cyclodextrin host ($H$) functionalized with a single imidazole ring at the primary rim acts as an artificial esterase, catalyzing the hydrolysis of $m$-nitrophenyl acetate ($S$):
\\[
H + S \\xrightleftharpoons{K_s} H\\cdot S \\xrightarrow{k_2} \\text{Acyl-}H + P_1 \\xrightarrow{k_3 [\\text{H}_2\\text{O}]} H + P_2
\\]
where:
- $K_s = [H][S] / [H\\cdot S]$ is the dissociation constant of the inclusion complex.
- $k_2$ is the first-order intracomplex acylation rate constant.
- $k_3$ is the pseudo-first-order deacylation rate constant regenerator.
- $P_1$ is $m$-nitrophenolate (chromophore monitored at $\\lambda = 400\\text{ nm}$) and $P_2$ is acetate.
Under steady-state conditions where $[S] \\gg [H]_0$, the observed initial rate of $P_1$ release follows Michaelis-Menten kinetics:
\\[
v_0 = \\frac{k_{\\text{cat}} [H]_0 [S]}{K_M + [S]}
\\]
(a) Express $k_{\\text{cat}}$ and $K_M$ in terms of elementary parameters $K_s$, $k_2$, and $k_3$.
(b) In an experiment at $\\text{pH} = 8.00$ and $T = 298.15\\text{ K}$ with $[H]_0 = 1.00 \\times 10^{-4}\\text{ M}$:
    - Lineweaver-Burk double reciprocal analysis yields $K_M = 2.40 \\times 10^{-3}\\text{ M}$ and $V_{\\max} = 1.80 \\times 10^{-5}\\text{ M/s}$.
    - In a rapid-flow pre-steady-state burst experiment, the acylation rate constant is measured directly as $k_2 = 1.20\\text{ s}^{-1}$.
    Determine $k_{\\text{cat}}$, $k_3$, and $K_s$.
(c) The second-order rate constant for uncatalyzed alkaline hydrolysis by imidazole in bulk solution is $k_{\\text{bim}} = 0.250\\text{ M}^{-1}\\text{s}^{-1}$. Calculate the effective molarity ($EM = k_2 / k_{\\text{bim}}$) of the intracomplex reaction.""",
            "solution": """### Step 1: Derivation of $k_{\text{cat}}$ and $K_M$
Applying the steady-state approximation to the acyl-host intermediate $[\text{Acyl-}H]$:
\\[
\\frac{d[\\text{Acyl-}H]}{dt} = k_2 [H\\cdot S] - k_3 [\\text{Acyl-}H] = 0 \\implies [\\text{Acyl-}H] = \\frac{k_2}{k_3} [H\\cdot S]
\\]
Conservation of total host:
\\[
[H]_0 = [H] + [H\\cdot S] + [\\text{Acyl-}H] = [H] + [H\\cdot S] \\left( 1 + \\frac{k_2}{k_3} \\right)
\\]
With rapid pre-equilibrium $[H] = K_s [H\\cdot S] / [S]$:
\\[
[H]_0 = [H\\cdot S] \\left[ \\frac{K_s}{[S]} + \\frac{k_2 + k_3}{k_3} \\right] = [H\\cdot S] \\left[ \\frac{K_s k_3 + (k_2 + k_3)[S]}{k_3 [S]} \\right]
\\]
Thus:
\\[
[H\\cdot S] = \\frac{k_3 [H]_0 [S]}{K_s k_3 + (k_2 + k_3)[S]}
\\]
The steady-state rate of product formation $v = k_2 [H\\cdot S]$:
\\[
v = \\frac{k_2 k_3 [H]_0 [S]}{K_s k_3 + (k_2 + k_3)[S]} = \\frac{\\left( \\frac{k_2 k_3}{k_2 + k_3} \\right) [H]_0 [S]}{\\frac{K_s k_3}{k_2 + k_3} + [S]}
\\]
Matching to standard Michaelis-Menten form $v = \\frac{k_{\\text{cat}} [H]_0 [S]}{K_M + [S]}$:
\\[
k_{\\text{cat}} = \\frac{k_2 k_3}{k_2 + k_3}
\\]
\\[
K_M = K_s \\left( \\frac{k_3}{k_2 + k_3} \\right) = K_s \\left( \\frac{k_{\\text{cat}}}{k_2} \\right)
\\]

### Step 2: Evaluation of Elementary Constants
1. **$k_{\\text{cat}}$**:
Given $[H]_0 = 1.00 \\times 10^{-4}\\text{ M}$ and $V_{\\max} = 1.80 \\times 10^{-5}\\text{ M/s}$:
\\[
k_{\\text{cat}} = \\frac{V_{\\max}}{[H]_0} = \\frac{1.80 \\times 10^{-5}\\text{ M/s}}{1.00 \\times 10^{-4}\\text{ M}} = 0.180\\text{ s}^{-1}
\\]

2. **$k_3$ (Deacylation Rate Constant)**:
From $\\frac{1}{k_{\\text{cat}}} = \\frac{1}{k_2} + \\frac{1}{k_3}$:
\\[
\\frac{1}{k_3} = \\frac{1}{k_{\\text{cat}}} - \\frac{1}{k_2} = \\frac{1}{0.180\\text{ s}^{-1}} - \\frac{1}{1.20\\text{ s}^{-1}} = 5.5556 - 0.8333 = 4.7222\\text{ s}
\\]
\\[
k_3 = \\frac{1}{4.7222\\text{ s}} = 0.2118\\text{ s}^{-1} \\approx 0.212\\text{ s}^{-1}
\\]
Deacylation ($k_3 = 0.212\\text{ s}^{-1}$) is slower than acylation ($k_2 = 1.20\\text{ s}^{-1}$) and represents the rate-limiting turnover step.

3. **$K_s$ (Intrinsic Binding Constant)**:
\\[
K_s = K_M \\left( \\frac{k_2}{k_{\\text{cat}}} \\right) = (2.40 \\times 10^{-3}\\text{ M}) \\times \\left( \\frac{1.20\\text{ s}^{-1}}{0.180\\text{ s}^{-1}} \\right) = (2.40 \\times 10^{-3}) \\times 6.6667 = 1.60 \\times 10^{-2}\\text{ M}
\\]

### Step 3: Effective Molarity ($EM$)
The effective molarity measures the catalytic advantage gained by pre-assembling the substrate inside the cavity:
\\[
EM = \\frac{k_2}{k_{\\text{bim}}} = \\frac{1.20\\text{ s}^{-1}}{0.250\\text{ M}^{-1}\\text{s}^{-1}} = 4.80\\text{ M}
\\]
The intramolecular juxtaposition of the substrate against the rim imidazole produces an effective local imidazole concentration of $4.80\\text{ M}$, delivering high catalytic rate enhancement under dilute solution conditions."""
        },
        {
            "probNumber": "6.9",
            "title": "Nernst-Planck Electrodiffusion in Synthetic Gramicidin Biomimetic Channels",
            "difficulty": "Advanced",
            "statement": """A synthetic cylindrical ion channel mimics gramicidin A, spanning a lipid bilayer of thickness $L = 3.0\\text{ nm} = 3.0 \\times 10^{-9}\\text{ m}$.
The channel carries monovalent cations ($z = +1$) across the membrane under an applied transmembrane electric potential difference $\\Delta V = V(0) - V(L) = +100\\text{ mV} = 0.100\\text{ V}$ at $T = 298.15\\text{ K}$.
The intra-channel ionic flux $J$ (in $\\text{mol}/(\\text{m}^2\\cdot\\text{s})$) is governed by the 1D **Nernst-Planck electrodiffusion equation**:
\\[
J = -D \\left( \\frac{dC}{dx} + \\frac{z F C}{RT} \\frac{d\\phi}{dx} \\right)
\\]
Assuming a constant electric field across the membrane ($\frac{d\\phi}{dx} = -\\frac{\\Delta V}{L}$), intra-channel diffusion coefficient $D = 2.00 \\times 10^{-10}\\text{ m}^2/\\text{s}$, and boundary concentrations at the channel mouths $C(0) = C_1 = 0.150\\text{ M} = 150\\text{ mol/m}^3$ and $C(L) = C_2 = 0.0150\\text{ M} = 15.0\\text{ mol/m}^3$:
(a) Integrate the Nernst-Planck equation to find the analytical expression for the flux $J$.
(b) Calculate the dimensionless potential $\\xi = \\frac{z F \\Delta V}{RT}$ and evaluate the flux $J$ in $\\text{mol}/(\\text{m}^2\\cdot\\text{s})$.
(c) If the effective cross-sectional area of the channel pore is $A = \\pi r^2 = \\pi (0.20 \\times 10^{-9}\\text{ m})^2 = 1.257 \\times 10^{-19}\\text{ m}^2$, calculate the single-channel electrical current $I$ in picoamperes ($\\text{pA}$) and the number of ions traversing the channel per second.""",
            "solution": """### Step 1: Analytical Integration of the Nernst-Planck Equation
With constant field $E = -\\frac{d\\phi}{dx} = \\frac{\\Delta V}{L}$:
\\[
J = -D \\left( \\frac{dC}{dx} - \\frac{z F \\Delta V}{RT L} C \\right)
\\]
Let the dimensionless potential parameter be:
\\[
\\xi = \\frac{z F \\Delta V}{RT}
\\]
Then:
\\[
\\frac{dC}{dx} - \\frac{\\xi}{L} C = -\\frac{J}{D}
\\]
Multiply by integrating factor $e^{-\\xi x / L}$:
\\[
\\frac{d}{dx} \\left[ C(x) e^{-\\xi x / L} \\right] = -\\frac{J}{D} e^{-\\xi x / L}
\\]
Integrate from $x = 0$ to $x = L$:
\\[
C(L) e^{-\\xi} - C(0) = -\\frac{J}{D} \\int_0^L e^{-\\xi x / L} dx = -\\frac{J}{D} \\left[ -\\frac{L}{\\xi} e^{-\\xi x / L} \\right]_0^L = \\frac{J L}{D \\xi} (e^{-\\xi} - 1)
\\]
Rearranging for $J$:
\\[
J = \\frac{D \\xi}{L} \\left( \\frac{C_1 - C_2 e^{-\\xi}}{1 - e^{-\\xi}} \\right)
\\]
which is the Goldman-Hodgkin-Katz (GHK) flux equation.

### Step 2: Evaluation of Dimensionless Potential and Flux
At $T = 298.15\\text{ K}$, $RT/F = 0.025693\\text{ V}$.
With $z = +1$ and $\\Delta V = 0.100\\text{ V}$:
\\[
\\xi = \\frac{1 \\times 0.100\\text{ V}}{0.025693\\text{ V}} = 3.8921
\\]
Calculate exponential factor:
\\[
e^{-\\xi} = e^{-3.8921} = 0.02040
\\]
\\[
1 - e^{-\\xi} = 1 - 0.02040 = 0.97960
\\]
With boundary concentrations $C_1 = 150\\text{ mol/m}^3$ and $C_2 = 15.0\\text{ mol/m}^3$:
\\[
C_1 - C_2 e^{-\\xi} = 150 - (15.0)(0.02040) = 150 - 0.306 = 149.694\\text{ mol/m}^3
\\]
Prefactor:
\\[
\\frac{D \\xi}{L} = \\frac{(2.00 \\times 10^{-10}\\text{ m}^2/\\text{s}) \\times 3.8921}{3.0 \\times 10^{-9}\\text{ m}} = \\frac{7.7842 \\times 10^{-10}}{3.0 \\times 10^{-9}} = 0.25947\\text{ m/s}
\\]
The flux is:
\\[
J = (0.25947\\text{ m/s}) \\times \\left( \\frac{149.694}{0.97960}\\text{ mol/m}^3 \\right) = 0.25947 \\times 152.811 = 39.65\\text{ mol}/(\\text{m}^2\\cdot\\text{s})
\\]

### Step 3: Single-Channel Current and Translocation Frequency
1. **Single-Channel Current**:
With pore area $A = 1.257 \\times 10^{-19}\\text{ m}^2$ and Faraday constant $F = 96{,}485\\text{ C/mol}$:
\\[
I = z F J A = (1) \\times (96{,}485\\text{ C/mol}) \\times (39.65\\text{ mol}/(\\text{m}^2\\cdot\\text{s})) \\times (1.257 \\times 10^{-19}\\text{ m}^2)
\\]
\\[
I = (3.8256 \\times 10^6\\text{ C}/(\\text{m}^2\\cdot\\text{s})) \\times (1.257 \\times 10^{-19}\\text{ m}^2) = 4.809 \\times 10^{-13}\\text{ A} = 0.481\\text{ pA}
\\]
2. **Ion Translocation Frequency $\\Phi_{\\text{ion}}$**:
\\[
\\Phi_{\\text{ion}} = \\frac{I}{e} = \\frac{4.809 \\times 10^{-13}\\text{ C/s}}{1.60218 \\times 10^{-19}\\text{ C/ion}} = 3.001 \\times 10^6\\text{ ions/second}
\\]
Over $3.0$ million cations traverse each single synthetic channel per second, closely matching the conductance of native gramicidin A."""
        }
    ]

    return {
        "id": "unit-6",
        "number": 6,
        "title": "Bioinorganic & Bioorganic Supramolecular Model Systems",
        "leadSummary": "Bioinorganic mimicry, the entatic state hypothesis, biomimetic ionophores (valinomycin, gramicidin), porphyrins, metalloporphyrins and electronic spectroscopy, the mu-oxo dimerization problem in myoglobin/hemoglobin models, Collman's picket-fence porphyrin, biomimetic copper proteins (hemocyanin), carbonic anhydrase active site models (Kimura zinc-cyclen), and cyclodextrin artificial esterases.",
        "simulations": ["sim_supra_picket_fence_porphyrin"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u6 = get_unit_6()
    print(f"Unit 6 generated: {len(u6['sections'])} sections, {len(u6['problems'])} problems.")
