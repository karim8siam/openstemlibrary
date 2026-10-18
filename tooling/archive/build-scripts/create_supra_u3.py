"""
create_supra_u3.py
Creates Unit 3 data dictionary for Supramolecular Chemistry:
Anion Binding Hosts & Supramolecular Coordination Assemblies
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_3():
    sections = [
        {
            "secNumber": "3.1",
            "title": "Fundamental Challenges of Anion Recognition: Solvation, Diffuse Charge & Geometry",
            "content": """While supramolecular chemistry initially flourished around cation coordination, designing synthetic receptors for anions presented substantially greater chemical hurdles. Anion recognition chemistry developed several decades after cation coordination due to four fundamental physical differences between anions and cations.

### The Four Physical Challenges of Anion Binding
1. **Larger Size and Diffuse Charge**:
Anions possess significantly larger ionic radii than isoelectronic cations (e.g., fluoride $\\text{F}^-$ has radius $1.33\\text{ Å}$, whereas isoelectronic sodium $\\text{Na}^+$ has radius $1.02\\text{ Å}$; chloride $\\text{Cl}^-$ has $r = 1.81\\text{ Å}$ vs $\\text{K}^+$ with $1.38\\text{ Å}$). Because charge is distributed over a larger volume, anions possess lower charge-to-radius ratios ($q/r$), resulting in weaker purely electrostatic attractions per contact.
2. **High Solvation Energies**:
Anions have high hydration enthalpies because protic solvents (especially water) form directional hydrogen bonds to anion lone pairs:
\\[
\\Delta H_{\\text{hyd}}^\circ(\\text{F}^-) = -504\\text{ kJ/mol}, \\quad \\Delta H_{\\text{hyd}}^\circ(\\text{Cl}^-) = -367\\text{ kJ/mol}
\\]
To bind an anion, a synthetic receptor must pay an immense thermodynamic penalty to strip away these tightly bound water molecules.
3. **Geometric and Dimensional Anisotropy**:
Unlike spherically symmetric monoatomic cations ($\\text{Na}^+, \\text{K}^+$), anions exhibit diverse, non-spherical spatial geometries:
- Spherical ($K_h$ symmetry): halides ($\\text{F}^-, \\text{Cl}^-, \\text{Br}^-, \\text{I}^-$)
- Linear ($D_{\\infty h}$): azide ($\\text{N}_3^-$), thiocyanate ($\\text{SCN}^-$)
- Trigonal Planar ($D_{3h}$): nitrate ($\\text{NO}_3^-$), carbonate ($\\text{CO}_3^{2-}$)
- Tetrahedral ($T_d$): sulfate ($\\text{SO}_4^{2-}$), phosphate ($\\text{PO}_4^{3-}$), perchlorate ($\\text{ClO}_4^-$)
- Octahedral ($O_h$): hexafluorophosphate ($\\text{PF}_6^-$)
A host must be engineered with geometric complementarity tailored to these specific point group symmetries.
4. **Pronounced pH Sensitivity**:
Many biologically and environmentally vital anions are conjugate bases of weak acids (e.g., carboxylates, hydrogen phosphate $\\text{HPO}_4^{2-}$, bicarbonate $\\text{HCO}_3^-$). Altering solution pH by $1 - 2$ units drastically shifts protonation equilibria, altering the net charge and hydrogen-bonding donor/acceptor profile of the guest."""
        },
        {
            "secNumber": "3.2",
            "title": "Neutral Hydrogen-Bonding Anion Hosts: Ureas, Thioureas & Squaramides",
            "content": """The development of neutral, uncharged anion receptors by Kelly, Hamilton, Reinhoudt, and Gale revolutionized anion supramolecular chemistry. Neutral receptors bind anions through directional hydrogen-bonding arrays without requiring positively charged counterions.

### Urea and Thiourea Receptors
Ureas and thioureas possess two convergent, coplanar $\\text{N-H}$ hydrogen-bond donor groups oriented with an angle of $\\approx 60^\\circ$ between their donor axes:
\\[
\\text{R-NH}-\\text{C}(=\\text{X})-\\text{NH-R'} \\quad (\\text{X} = \\text{O or S})
\\]
- In the anti,anti (syn,syn) binding conformation, the two $\\text{N-H}$ protons point directly toward the anion, forming a six-membered chelate-like hydrogen-bonded ring with halides or bidentate carboxylate/phosphate oxygens:
\\[
\\text{N-H}\\cdots\\text{O-C(R)=O}\\cdots\\text{H-N}
\\]
- **Thiourea vs Urea**: Thioureas are superior anion receptors compared to ureas:
  1. The $\\text{N-H}$ protons of thioureas are substantially more acidic ($\text{p}K_a \\approx 21$ in DMSO for diphenylthiourea vs $\\text{p}K_a \\approx 27$ for diphenylurea) due to the greater polarizability and lower basicity of sulfur.
  2. The thiocarbonyl sulfur is a weaker hydrogen-bond acceptor than oxygen, preventing self-association (dimerization) of the host that would otherwise compete with anion binding.

### Squaramides: Four-Membered Aromatic Hydrogen-Bonding Clefts
Squaramides (diamides of squaric acid) have emerged as powerful hydrogen-bonding scaffolds:
- The cyclobutenedione ring enforces a planar geometry with an increased spacing of $d(\\text{N}\\cdots\\text{N}) \\approx 2.72\\text{ Å}$ compared to ureas ($2.2\\text{ Å}$), providing an ideal bite angle for larger oxoanions ($\\text{SO}_4^{2-}, \\text{HPO}_4^{2-}$).
- **Aromaticity Gain**: Upon deprotonation or hydrogen bonding to an anion, polarization of the two carbonyl groups contributes to a $2\\pi$-electron Hückel aromatic resonance structure across the four-membered ring, thermodynamically augmenting the hydrogen-bond donor strength via resonance-assisted hydrogen bonding (RAHB)."""
        },
        {
            "secNumber": "3.3",
            "title": "Pyrrole-Based & Calixpyrrole Anion Receptors",
            "content": """Heterocyclic compounds containing acidic $\\text{N-H}$ bonds—most prominently pyrrole, dipyrromethanes, and **calixpyrroles**—constitute a fundamental class of neutral anion receptors pioneered by Jonathan L. Sessler.

### Calix[4]pyrrole: Structure and Synthesis
Calix[4]pyrroles are macrocycles consisting of four pyrrole rings linked through their 2- and 5-positions by $sp^3$-hybridized quaternary carbon meso-bridges.
- First prepared by Baeyer in 1886 from the acid-catalyzed condensation of pyrrole with acetone:
\\[
4\\,\\text{Pyrrole} + 4\\,\\text{Acetone} \\xrightarrow{\\text{HCl}} \\text{meso-octamethylcalix[4]pyrrole} + 4\\,\\text{H}_2\\text{O}
\\]
- The four $sp^3$ meso-carbons prevent the macrocycle from becoming planar and aromatic, leaving it flexible with four distinct conformational states: *cone*, *partial cone*, *1,2-alternate*, and *1,3-alternate*.

### Induced-Fit Conformational Switching
In the uncomplexed state in solution and solid state, calix[4]pyrrole adopts the **1,3-alternate** conformation:
- Two opposing pyrrole rings point upward, and the other two point downward, minimizing electrostatic repulsion between nitrogen lone pairs and dispersing the $\\text{N-H}$ dipole vectors.
- Upon addition of a halide (especially fluoride $\\text{F}^-$ or chloride $\\text{Cl}^-$), the macrocycle undergoes an allosteric **induced-fit conformational reorganization into the *cone* conformation**:
\\[
\\text{1,3-alternate} \\xrightarrow{+\\text{Cl}^-} [\\text{Cl}^- \\subset \\text{cone-calix[4]pyrrole}]
\\]
In the cone conformation, all four pyrrole $\\text{N-H}$ bonds point in the same direction, converging onto the central halide ion in a square-pyramidal coordination geometry with four simultaneous $\\text{N-H}\\cdots\\text{Cl}^-$ hydrogen bonds ($d(\\text{N}\\cdots\\text{Cl}) \\approx 3.25\\text{ Å}$).

Calix[4]pyrrole exhibits remarkable selectivity for fluoride ($K_a > 10^5\\text{ M}^{-1}$ in acetonitrile) and chloride ($K_a \\approx 3.5 \\times 10^3\\text{ M}^{-1}$), while completely excluding larger iodide ($\\text{I}^-$) due to steric clash within the narrow cone cavity."""
        },
        {
            "secNumber": "3.4",
            "title": "Positively Charged Anion Receptors: Polyammonium, Guanidinium & Cryptand Cages",
            "content": """The earliest synthetic anion hosts relied on electrostatic Coulomb attractions generated by protonated polyammonium or permanently charged quaternary ammonium/guanidinium centers.

### Katapinands and Polyazacryptands
In 1968, C. H. Park and H. E. Simmons synthesized **katapinands** (from Greek *katapino*, to swallow), macrobicyclic diamines capable of encapsulating chloride inside their cavity:
- Upon protonation of both bridgehead tertiary amines, the host adopts an $in,in$-diprotium state ($[\\text{H}_2\\text{L}]^{2+}$) where both $\\text{N}^+-\\text{H}$ protons point inward.
- The chloride ion is coordinated between the two internal ammonium protons:
\\[
\\text{N}^+-\\text{H}\\cdots\\text{Cl}^-\\cdots\\text{H}-\\text{N}^+
\\]
- Jean-Marie Lehn expanded this concept to spherical **polyazacryptands** containing six or eight secondary/tertiary amino groups. In acidic aqueous solution, hexaprotonation produces a hexacationic cage $[\\text{L}\\cdot 6\\text{H}]^{6+}$:
  - Encloses a spherical cavity lined with six inward-directed ammonium groups.
  - Displays astronomical affinity for chloride ($\log K_a > 4.0$ in water!), but rejects smaller fluoride because $\\text{F}^-$ cannot simultaneously span the six divergent $\\text{N}^+-\\text{H}$ bonds.

### The Guanidinium Motif: Biological Phosphate Recognition
The guanidinium cation ($\\text{C}(\\text{NH}_2)_3^+$, side chain of arginine) is uniquely suited for anion recognition:
1. **High Basicity**: Possesses a $\\text{p}K_a \\approx 13.5$, ensuring it remains $100\\%$ positively charged across the entire physiological pH range ($1 - 12$).
2. **Resonance Planarity and Dual Donors**: Resonance delocalizes the $+1$ charge symmetrically across three nitrogen atoms. The planar guanidinium ring presents two parallel $\\text{N-H}$ hydrogen-bond donors with an ideal distance of $2.23\\text{ Å}$ to form a planar, bidentate salt bridge with oxoanions:
\\[
\\text{Guanidinium}^+ + \\text{R-O-PO}_3^{2-} \\longrightarrow [\\text{Guanidinium} \\cdot \\text{Phosphate}]^- \\quad (\\text{two parallel } \\text{N-H}\\cdots\\text{O-P} \\text{ bonds})
\\]
This structural motif governs substrate binding in staphylococcal nuclease, ATP-dependent kinases, and synthetic DNA-binding clefts."""
        },
        {
            "secNumber": "3.5",
            "title": "Halogen Bonding, Chalcogen Bonding & Non-Classical Anion Coordination",
            "content": """Beyond classical hydrogen bonding and Coulombic interactions, modern supramolecular chemistry exploits non-covalent interactions driven by anisotropic electrostatic potential distributions: **halogen bonding** (XB) and **chalcogen bonding** (ChB).

### The sigma-Hole Concept
When a halogen atom $\\text{X}$ (such as $\\text{I}$ or $\\text{Br}$) is covalently bonded to an electron-withdrawing group $\\text{R}$ (such as a perfluoroalkyl or perfluoroaryl moiety, e.g., $-\\text{C}_6\\text{F}_5$ or $-\\text{CF}_3$), the covalent $\\sigma$-bond draws electron density along the $\\text{R-X}$ bonding axis:
- The halogen's valence shell forms an anisotropic electron distribution: a torus (belt) of negative electrostatic potential around its equator, and a region of positive electrostatic potential directly on the outermost tip along the extension of the $\\text{R-X}$ bond axis.
- This electropositive region is termed the **$\\sigma$-hole** (Politzer and Murray, 2007).

### Characteristics of Halogen-Bonded Anion Receptors
An anion $\\text{A}^-$ (Lewis base) is attracted to the electropositive $\\sigma$-hole:
\\[
\\text{R-X} \\cdots \\text{A}^- \\quad (\\text{X} = \\text{I, Br, Cl})
\\]
1. **Strict Linearity**: Because the $\\sigma$-hole is situated precisely along the extension of the covalent $\\sigma$-bond, halogen bonds exhibit extreme directional rigidity ($\angle \\text{R-X}\\cdots\\text{A}^- \\approx 175 - 180^\\circ$), far more directional than hydrogen bonds which tolerate bending down to $140^\\circ$.
2. **Tunable Strength**: The magnitude of the $\\sigma$-hole potential scales directly with the polarizability of the halogen atom:
\\[
\\text{F} \\ll \\text{Cl} < \\text{Br} < \\text{I}
\\]
Iodine hosts form the strongest halogen bonds, with binding energies reaching $20 - 150\\text{ kJ/mol}$ for halides.
3. **Hydrophobic Resilience**: Unlike hydrogen bonds, which are severely weakened by competitive hydrogen-bond accepting solvents (acetone, DMSO, water), halogen-bond donors possess no protic character and operate effectively in competitive polar and aqueous-organic media.

### Chalcogen and Pnictogen Bonding
Extending to Group 16 elements ($\\text{S, Se, Te}$), atoms bearing two covalent bonds develop two distinct $\\sigma$-holes. Bidentate chalcogen-bonding receptors containing dual tellurophene or 1,2,5-chalcogenadiazole rings bind halides through collinear $\\text{C-Te}\\cdots\\text{X}^-$ interactions."""
        },
        {
            "secNumber": "3.6",
            "title": "Organometallic & Lewis Acidic Anion Receptors",
            "content": """Complementing organic hydrogen-bonding receptors, inorganic and organometallic complexes provide potent anion hosts utilizing coordination to Lewis acidic metal centers or redox-active metallocenes.

### Metallocene-Based Electrochemical Anion Sensors
Pioneered by Paul Beer, incorporating redox-active organometallic reporter groups (such as ferrocene or cobaltocenium) into an anion-binding cleft enables electrical sensing:
1. **Cobaltocenium Receptors**: The cobaltocenium cation ($[\\text{Co}(\\text{Cp})_2]^+$) carries a permanent $+1$ charge that enhances anion binding via Coulombic attraction while resisting protonation changes over a wide pH range.
2. **Ferrocenyl Amide / Urea Receptors**: A neutral ferrocene unit is functionalized with amide or urea arms:
   - In the initial $\\text{Fe(II)}$ state, the receptor binds an anion (such as $\\text{H}_2\\text{PO}_4^-$) via $\\text{N-H}\\cdots\\text{O}$ hydrogen bonds.
   - The close proximity of the bound negative charge stabilizes the oxidized ferrocenium cation $\\text{Fe(III)}$.
   - Consequently, the reversible redox potential $E_{1/2}$ of the $\\text{Fe(II)/Fe(III)}$ couple shifts cathodic (to more negative potentials) by $\\Delta E_{1/2} = 50 - 250\\text{ mV}$ upon anion binding:
\\[
\\Delta E_{1/2} = - \\frac{RT}{F} \\ln\\left( \\frac{K_a(\\text{Fe}^{\\text{III}})}{K_a(\\text{Fe}^{\\text{II}})} \\right)
\\]
Measuring $\\Delta E_{1/2}$ via cyclic voltammetry directly quantifies anion concentration.

### Lewis Acidic Receptors: Organoboranes and Mercuracarborands ("Anti-Crowns")
Direct coordinate covalent bonding between an electron-rich anion and a Lewis acidic center:
1. **Bidentate Organoboranes**: Molecules containing two triarylboron moieties ($\\text{Ar}_2\\text{B-R-BAr}_2$) with empty $p_z$ orbitals directed toward a central cavity chelate small Lewis basic anions such as fluoride ($\\text{F}^-$) or cyanide ($\\text{CN}^-$) via dual $\\text{B-F}$ coordinate bonds, producing binding constants $K_a > 10^8\\text{ M}^{-1}$.
2. **Mercuracarborands (Hawthorne's "Anti-Crown Ethers")**: Cyclic oligomers consisting of repeating electrophilic mercury(II) atoms bridged by *o*-carborane clusters, such as cyclo-$[\\text{Hg}(\\text{C}_2\\text{B}_{10}\\text{H}_{10})]_4$:
   - Possess a planar, macrocyclic ring containing four or five electrophilic $\\text{Hg(II)}$ centers pointing into the central cavity.
   - Form exceptionally stable complexes with spherical halides ($[\\text{Cl}^- \\subset \\text{anti-crown}]$), with the chloride held in the ring plane by four or five convergent $\\text{Hg}\\cdots\\text{Cl}$ interactions."""
        },
        {
            "secNumber": "3.7",
            "title": "Switchable Receptors: Converting Anion Hosts to Cation Hosts via pH & Redox",
            "content": """A pinnacle of modern supramolecular design is the creation of **switchable molecular receptors** whose binding affinity and selectivity can be inverted reversibly by an external chemical or physical trigger (pH, light, or redox potential).

### pH-Gated Cation-to-Anion Receptor Inversion
Polyamino-polyether macrocycles and cryptands can be switched between cation-selective and anion-selective states by modulating pH:
1. **Neutral/Basic Regime ($\text{pH} > 9$)**:
   - The amino nitrogens are unprotonated, possessing free Lewis basic lone pairs directed into the macrocyclic cavity.
   - In this state, the host acts as a **cation receptor**, binding alkali or transition metal cations ($\\text{Na}^+, \\text{Cu}^{2+}$) via cooperative lone-pair coordination.
2. **Acidic Regime ($\text{pH} < 4$)**:
   - The amino nitrogens undergo protonation to form positive ammonium groups ($-\\text{NH}_2^+-$).
   - Inward-pointing positive charges create electrostatic repulsion that ejects any bound metal cation.
   - Concurrently, the inward-directed $\\text{N}^+-\\text{H}$ protons and positive electrostatic field transform the cavity into an **anion receptor**, binding halides ($\\text{Cl}^-$) or oxoanions ($\\text{SO}_4^{2-}$) with high affinity.
\\[
[\\text{M}^{n+} \\subset \\text{Host}] \\xrightleftharpoons[+\\text{OH}^-]{+\\text{H}^+} \\text{M}^{n+} + [\\text{Anion}^{m-} \\subset \\text{Host}\\cdot x\\text{H}^+]^{(x-m)+}
\\]

### Redox-Switchable Receptors
Receptors incorporating viologen ($N,N'$-dialkyl-4,4'-bipyridinium, $\\text{V}^{2+}$) units:
- In the dicationic oxidized state $\\text{V}^{2+}$, the host binds electron-rich planar anions (such as iodide or 2-naphthalenesulfonate) through coupled electrostatic attraction and charge-transfer complexation.
- Upon single-electron reduction to the radical cation $\\text{V}^{\\bullet+}$, electrostatic attraction diminishes, triggering quantitative anion release.

### Light-Responsive Azobenzene Receptors
Functionalizing an anion-binding bis-urea host with a central azobenzene linker allows photochemical gating:
- **trans-Isomer** (visible light, $\lambda = 450\\text{ nm}$): The two urea arms are separated by $9\\text{ Å}$, incapable of simultaneously binding an oxoanion.
- **cis-Isomer** (UV light, $\lambda = 365\\text{ nm}$): Photoisomerization bends the azobenzene backbone into a U-shaped geometry, bringing the two urea clefts within $4.5\\text{ Å}$ to form a synergistic bidentate binding pocket for sulfate."""
        },
        {
            "secNumber": "3.8",
            "title": "Tetrahedral & Spherical Anion Discrimination: Halide vs Oxoanion Binding",
            "content": """Achieving high selectivity among competing anions in complex biological or environmental fluids requires receptors designed to discriminate on the basis of charge density, shape, and basicity.

### Spherical Halide Discrimination: $\\text{F}^-$ vs $\\text{Cl}^-$ vs $\\text{Br}^-$ vs $\\text{I}^-$
The halides present identical spherical symmetry ($K_h$) but vary across a wide range of ionic radii, polarizabilities, and hydration energies:

| Halide | Ionic Radius (Å) | $\\Delta G_{\\text{hyd}}^\circ$ (kJ/mol) | Polarizability ($\\text{Å}^3$) | Optimal Recognition Motif |
| :--- | :--- | :--- | :--- | :--- |
| **$\\text{F}^-$** | $1.33$ | $-465$ | $0.64$ | Tight, hard hydrogen-bond donors (ureas, calixpyrrole) |
| **$\\text{Cl}^-$** | $1.81$ | $-340$ | $2.98$ | Macrobicyclic azacryptands, katapinands, cone calix[4]pyrrole |
| **$\\text{Br}^-$** | $1.96$ | $-315$ | $4.24$ | Expanded macrocycles, bis-thioureas |
| **$\\text{I}^-$** | $2.20$ | $-275$ | $6.45$ | Halogen bonding ($\sigma$-hole donors), large cavitands |

Because fluoride has by far the highest hydration penalty ($-465\\text{ kJ/mol}$), a receptor that binds fluoride in water must provide immense electrostatic stabilization to overcome this desolvation threshold.

### Tetrahedral Oxoanion Recognition: Sulfate vs Phosphate vs Perchlorate
Tetrahedral oxoanions possess four oxygen atoms directed toward the vertices of a tetrahedron, but exhibit drastically different formal charges and basicities:
1. **Sulfate ($\\text{SO}_4^{2-}$)**:
   - High charge density, strong Lewis base, high hydration penalty ($\\Delta G_{\\text{hyd}}^\circ = -1080\\text{ kJ/mol}$).
   - Bound with extreme selectivity by rigid bicyclic or tricyclic cages presenting six or eight convergent hydrogen-bond donors oriented along tetrahedral axes, mimicking the biological **Sulfate-Binding Protein (SBP)** which encapsulates $\\text{SO}_4^{2-}$ with 16 hydrogen bonds without a single direct water contact.
2. **Hydrogen Phosphate ($\\text{HPO}_4^{2-}$ / $\\text{H}_2\\text{PO}_4^-$)**:
   - Protic oxoanion capable of acting simultaneously as hydrogen-bond acceptor and donor. Receptors bearing complementary donor-acceptor arrays (such as guanidiniums or zinc(II)-dipicolylamine complexes) bind phosphates with sub-micromolar affinity.
3. **Perchlorate ($\\text{ClO}_4^-$)**:
   - Mononegative charge dispersed over four oxygens; exceptionally low hydration penalty ($-205\\text{ kJ/mol}$). Follows the classical **Hofmeister series**:
\\[
\\text{SO}_4^{2-} > \\text{HPO}_4^{2-} > \\text{F}^- > \\text{Cl}^- > \\text{Br}^- > \\text{NO}_3^- > \\text{I}^- > \\text{ClO}_4^-
\\]
Non-preorganized, hydrophobic receptors in water naturally bind $\\text{ClO}_4^-$ most strongly simply because it is the easiest anion to dehydrate. Overcoming this Hofmeister bias to selectively bind more hydrophilic anions ($\text{SO}_4^{2-}$ or $\text{Cl}^-$) requires rigorous structural preorganization and high donor density."""
        }
    ]

    problems = [
        {
            "probNumber": "3.1",
            "title": "Anion Hydration Free Energies: The Hofmeister Series and Desolvation Barriers",
            "difficulty": "Foundational",
            "statement": """The standard Gibbs free energies of hydration $\\Delta G_{\\text{hyd}}^\circ$ for four anions in water at $298.15\\text{ K}$ are:
- Fluoride ($\\text{F}^-$): $\\Delta G_{\\text{hyd}}^\circ = -465\\text{ kJ/mol}$
- Chloride ($\\text{Cl}^-$): $\\Delta G_{\\text{hyd}}^\circ = -340\\text{ kJ/mol}$
- Nitrate ($\\text{NO}_3^-$): $\\Delta G_{\\text{hyd}}^\circ = -300\\text{ kJ/mol}$
- Perchlorate ($\\text{ClO}_4^-$): $\\Delta G_{\\text{hyd}}^\circ = -205\\text{ kJ/mol}$
A synthetic neutral bis-urea receptor binds anions in the gas phase with intrinsic electrostatic interaction enthalpies:
$E_{\\text{int}}(\\text{F}^-) = -510\\text{ kJ/mol}$, $E_{\\text{int}}(\\text{Cl}^-) = -375\\text{ kJ/mol}$, $E_{\\text{int}}(\\text{NO}_3^-) = -320\\text{ kJ/mol}$, $E_{\\text{int}}(\\text{ClO}_4^-) = -220\\text{ kJ/mol}$.
(a) Assuming host desolvation and entropic terms are approximately identical for all four anions, estimate the net binding free energy in water:
\\[
\\Delta G_{\\text{aq}}^\circ \\approx E_{\\text{int}} - \\Delta G_{\\text{hyd}}^\circ
\\]
(b) Determine the ranking of binding affinities in the gas phase versus in aqueous solution.
(c) Explain the inversion in selectivity between fluoride and perchlorate in terms of the Hofmeister series and desolvation thermodynamics.""",
            "solution": """### Step 1: Net Binding Free Energy in Aqueous Solution
The net complexation free energy in water accounts for the competition between host-guest intrinsic attraction and guest desolvation:
\\[
\\Delta G_{\\text{aq}}^\circ \\approx E_{\\text{int}} - \\Delta G_{\\text{hyd}}^\circ
\\]

1. **For Fluoride ($\\text{F}^-$)**:
\\[
\\Delta G_{\\text{aq}}^\circ(\\text{F}^-) \\approx -510 - (-465) = -510 + 465 = -45.0\\text{ kJ/mol}
\\]

2. **For Chloride ($\\text{Cl}^-$)**:
\\[
\\Delta G_{\\text{aq}}^\circ(\\text{Cl}^-) \\approx -375 - (-340) = -375 + 340 = -35.0\\text{ kJ/mol}
\\]

3. **For Nitrate ($\\text{NO}_3^-$)**:
\\[
\\Delta G_{\\text{aq}}^\circ(\\text{NO}_3^-) \\approx -320 - (-300) = -320 + 300 = -20.0\\text{ kJ/mol}
\\]

4. **For Perchlorate ($\\text{ClO}_4^-$)**:
\\[
\\Delta G_{\\text{aq}}^\circ(\\text{ClO}_4^-) \\approx -220 - (-205) = -220 + 205 = -15.0\\text{ kJ/mol}
\\]

### Step 2: Ranking of Selectivity Profiles
1. **Gas-Phase (Intrinsic) Ranking**:
\\[
|E_{\\text{int}}(\\text{F}^-)| > |E_{\\text{int}}(\\text{Cl}^-)| > |E_{\\text{int}}(\\text{NO}_3^-)| > |E_{\\text{int}}(\\text{ClO}_4^-)|
\\]
\\[
\\text{Ranking}: \\quad \\text{F}^- (-510) > \\text{Cl}^- (-375) > \\text{NO}_3^- (-320) > \\text{ClO}_4^- (-220)
\\]
In vacuum, binding follows charge density: small, localized fluoride binds over twice as strongly as diffuse perchlorate.

2. **Aqueous Solution Ranking**:
\\[
\\Delta G_{\\text{aq}}^\circ: \\quad \\text{F}^- (-45) < \\text{Cl}^- (-35) < \\text{NO}_3^- (-20) < \\text{ClO}_4^- (-15\\text{ kJ/mol})
\\]
\\[
K_a(\\text{F}^-) > K_a(\\text{Cl}^-) > K_a(\\text{NO}_3^-) > K_a(\\text{ClO}_4^-)
\\]
Here, because the host provides a substantial intrinsic interaction for fluoride ($-510\\text{ kJ/mol}$), it successfully overcomes the hydration penalty.

### Step 3: Hofmeister Bias and Non-Specific Binding
However, consider a flexible, weakly binding hydrophobic receptor where intrinsic interaction is much weaker, say $E_{\\text{int}} = -230\\text{ kJ/mol}$ for all anions:
- For $\\text{F}^-$: $\\Delta G_{\\text{aq}}^\circ = -230 - (-465) = +235\\text{ kJ/mol}$ (completely non-spontaneous, rejected).
- For $\\text{ClO}_4^-$: $\\Delta G_{\\text{aq}}^\circ = -230 - (-205) = -25\\text{ kJ/mol}$ (spontaneous binding!).
This illustrates the **Hofmeister bias**:
- In the absence of high electrostatic donor density, non-preorganized hydrophobic cavities in water bind anions in the order of their ease of dehydration:
\\[
\\text{ClO}_4^- > \\text{I}^- > \\text{NO}_3^- > \\text{Br}^- > \\text{Cl}^- > \\text{F}^-
\\]
Perchlorate binds most readily simply because its low charge density makes it hydrophobic and easy to dehydrate. Overriding this natural Hofmeister preference to bind fluoride requires a rigid, high-density hydrogen-bonding array."""
        },
        {
            "probNumber": "3.2",
            "title": "Dual Hydrogen-Bond Binding Affinities of Diphenylurea vs Diphenylthiourea Receptors",
            "difficulty": "Foundational",
            "statement": """The binding of tetrabutylammonium acetate ($\\text{AcO}^-$) by 1,3-diphenylurea and 1,3-diphenylthiourea was investigated in $\\text{CD}_3\\text{CN}$ at $298.15\\text{ K}$ by $^1\\text{H}$ NMR titration:
- **1,3-Diphenylurea**: $K_a = 2.40 \\times 10^3\\text{ M}^{-1}$, $\\Delta H^\\circ = -19.5\\text{ kJ/mol}$
- **1,3-Diphenylthiourea**: $K_a = 3.60 \\times 10^4\\text{ M}^{-1}$, $\\Delta H^\\circ = -26.8\\text{ kJ/mol}$
(a) Calculate $\\Delta G^\\circ$ and the entropic term $-T\\Delta S^\\circ$ for both hosts at $298.15\\text{ K}$.
(b) Compute the enhancement factor $\\Delta \\Delta G^\\circ = \\Delta G_{\\text{thiourea}}^\circ - \\Delta G_{\\text{urea}}^\circ$ and the ratio of binding constants $K_a(\\text{thiourea}) / K_a(\\text{urea})$.
(c) The $\\text{p}K_a$ values in DMSO are $26.9$ for diphenylurea and $21.1$ for diphenylthiourea. Correlate the $5.8$-unit $\\text{p}K_a$ drop with the observed $\\Delta \\Delta H^\\circ$ of complexation.""",
            "solution": """### Step 1: Thermodynamic State Functions
With $RT = (8.3145\\text{ J/(mol}\\cdot\\text{K)})(298.15\\text{ K}) = 2.4790\\text{ kJ/mol}$:

1. **For 1,3-Diphenylurea**:
\\[
\\Delta G_{\\text{urea}}^\circ = -RT \\ln(2.40 \\times 10^3) = -(2.4790\\text{ kJ/mol})(7.7836) = -19.30\\text{ kJ/mol}
\\]
\\[
-T\\Delta S_{\\text{urea}}^\circ = \\Delta G_{\\text{urea}}^\circ - \\Delta H_{\\text{urea}}^\circ = -19.30 - (-19.50) = +0.20\\text{ kJ/mol}
\\]
\\[
\\Delta S_{\\text{urea}}^\circ = -\\frac{200\\text{ J/mol}}{298.15\\text{ K}} = -0.67\\text{ J/(mol}\\cdot\\text{K)}
\\]

2. **For 1,3-Diphenylthiourea**:
\\[
\\Delta G_{\\text{thiourea}}^\circ = -RT \\ln(3.60 \\times 10^4) = -(2.4790\\text{ kJ/mol})(10.4913) = -26.01\\text{ kJ/mol}
\\]
\\[
-T\\Delta S_{\\text{thiourea}}^\circ = \\Delta G_{\\text{thiourea}}^\circ - \\Delta H_{\\text{thiourea}}^\circ = -26.01 - (-26.80) = +0.79\\text{ kJ/mol}
\\]
\\[
\\Delta S_{\\text{thiourea}}^\circ = -\\frac{790\\text{ J/mol}}{298.15\\text{ K}} = -2.65\\text{ J/(mol}\\cdot\\text{K)}
\\]

### Step 2: Enhancement Factor and Equilibrium Ratio
\\[
\\Delta \\Delta G^\\circ = \\Delta G_{\\text{thiourea}}^\circ - \\Delta G_{\\text{urea}}^\circ = -26.01 - (-19.30) = -6.71\\text{ kJ/mol}
\\]
Ratio of association constants:
\\[
\\frac{K_a(\\text{thiourea})}{K_a(\\text{urea})} = \\frac{3.60 \\times 10^4}{2.40 \\times 10^3} = 15.0
\\]
The thiourea binds acetate 15 times more strongly than the urea analogue.

### Step 3: Correlation with $\\text{p}K_a$ and Acidity
Enthalpic difference:
\\[
\\Delta \\Delta H^\\circ = \\Delta H_{\\text{thiourea}}^\circ - \\Delta H_{\\text{urea}}^\circ = -26.80 - (-19.50) = -7.30\\text{ kJ/mol}
\\]
The $15$-fold binding affinity increase is **entirely enthalpy-driven** ($\\Delta \\Delta H^\\circ = -7.30\\text{ kJ/mol}$).
1. **Physical Cause of $\\text{p}K_a$ Shift**: Sulfur is larger and more polarizable than oxygen, and cannot participate in $\\pi$-back-donation into the thiocarbonyl carbon as effectively as oxygen. As a result, the thiourea $\\text{C=S}$ carbon withdraws more electron density from the flanking $\\text{N-H}$ bonds, increasing the partial positive charge on the hydrogen atoms ($\delta^+$) and lowering the $\\text{p}K_a$ from $26.9$ to $21.1$ ($\Delta \\text{p}K_a = -5.8$).
2. **Impact on Hydrogen Bonding**: A more acidic $\\text{N-H}$ proton forms a substantially stronger, more polarized electrostatic hydrogen bond to the basic acetate carboxylate oxygens:
\\[
-\\Delta \\Delta H^\\circ \\approx 7.3\\text{ kJ/mol}
\\]
corresponding to an additional $\\approx 3.65\\text{ kJ/mol}$ stabilization per hydrogen bond across the two $\\text{N-H}\\cdots\\text{O}$ contacts."""
        },
        {
            "probNumber": "3.3",
            "title": "Halogen-Bonding sigma-Hole Electrostatics: Potential Well Depth and Directionality",
            "difficulty": "Foundational",
            "statement": """A halogen-bond receptor featuring an iodoperfluoroarene core ($\\text{Ar}_F\\text{-I}$) interacts with chloride anion ($\\text{Cl}^-$). The electrostatic surface potential at the apex of the iodine $\\sigma$-hole ($z = 0, \\theta = 180^\\circ$) is $V_{\\sigma} = +145\\text{ kJ/mol}$ per elementary charge, while the equatorial belt of the iodine atom has a negative potential $V_{\\text{belt}} = -40\\text{ kJ/mol}$.
(a) If a chloride ion (charge $q = -e$) approaches the iodine atom at the van der Waals contact distance $r = 3.20\\text{ Å}$:
Calculate the electrostatic interaction energy $U_{\\text{elec}}(\\theta)$ along the linear $\\sigma$-hole axis ($\\theta = 180^\\circ$) versus along the perpendicular equatorial plane ($\\theta = 90^\\circ$).
(b) The angular dependence of the halogen-bond potential is modeled empirically by:
\\[
U(\\theta) = U_0 \\cos^4(180^\\circ - \\theta) - U_{\\text{rep}} \\sin^2(180^\\circ - \\theta)
\\]
where $U_0 = -65.0\\text{ kJ/mol}$. Calculate the energy penalty if the $\\text{C-I}\\cdots\\text{Cl}^-$ angle bends from ideal linearity ($180^\\circ$) to $150^\\circ$ (assuming $U_{\\text{rep}} = 25.0\\text{ kJ/mol}$).
(c) Compare this angular rigidity to a standard hydrogen bond ($\text{N-H}\cdots\text{Cl}^-$) and explain why halogen bonds are exceptionally effective for stereochemically rigid anion templating.""",
            "solution": """### Step 1: Electrostatic Potential along Axis vs Equatorial Plane
The electrostatic potential energy of a test charge $q = -e$ interacting with a surface potential $V$ is:
\\[
U_{\\text{elec}} = q V
\\]
1. **Along the Linear $\\sigma$-Hole Axis ($\\theta = 180^\\circ$)**:
Since $V_{\\sigma} = +145\\text{ kJ/mol}$ per elementary charge:
\\[
U_{\\text{elec}}(180^\\circ) = (-1)(+145\\text{ kJ/mol}) = -145.0\\text{ kJ/mol} \\quad (\\text{strongly attractive})
\\]
2. **Along the Equatorial Plane ($\\theta = 90^\\circ$)**:
Since $V_{\\text{belt}} = -40\\text{ kJ/mol}$ per elementary charge:
\\[
U_{\\text{elec}}(90^\\circ) = (-1)(-40\\text{ kJ/mol}) = +40.0\\text{ kJ/mol} \\quad (\\text{strongly repulsive})
\\]
The energy difference between the linear approach and the side-on approach is:
\\[
\\Delta U = U(90^\\circ) - U(180^\\circ) = +40.0 - (-145.0) = +185.0\\text{ kJ/mol}
\\]
This massive difference creates a steep electrostatic funnel directing the incoming anion strictly along the $\\text{C-I}$ bond axis.

### Step 2: Bending Penalty from $180^\\circ$ to $150^\\circ$
Let $\\phi = 180^\\circ - \\theta$ be the deflection angle from linearity.
- At $\\theta = 180^\\circ$: $\\phi = 0^\\circ$.
\\[
U(180^\\circ) = U_0 \\cos^4(0^\\circ) - U_{\\text{rep}} \\sin^2(0^\\circ) = -65.0(1)^4 - 25.0(0)^2 = -65.0\\text{ kJ/mol}
\\]
- At $\\theta = 150^\\circ$: $\\phi = 30^\\circ$.
\\[
\\cos(30^\\circ) = \\frac{\\sqrt{3}}{2} \\approx 0.86603 \\implies \\cos^4(30^\\circ) = (0.86603)^4 = 0.5625
\\]
\\[
\\sin(30^\\circ) = 0.50000 \\implies \\sin^2(30^\\circ) = 0.2500
\\]
Evaluating $U(150^\\circ)$:
\\[
U(150^\\circ) = (-65.0)(0.5625) - (25.0)(0.2500) = -36.56 - 6.25 = -42.81\\text{ kJ/mol}
\\]
The energy penalty incurred by bending $30^\\circ$ off-axis is:
\\[
\\Delta U_{\\text{bend}} = U(150^\\circ) - U(180^\\circ) = -42.81 - (-65.00) = +22.19\\text{ kJ/mol}
\\]

### Step 3: Comparison to Hydrogen Bonding
1. **Angular Rigidity**: A $30^\\circ$ deflection in a hydrogen bond ($\text{N-H}\cdots\text{Cl}^-$ from $180^\\circ$ to $150^\\circ$) typically costs only $4 - 8\\text{ kJ/mol}$, meaning hydrogen bonds are conformationally compliant and easily flex to accommodate host distortions. In contrast, the halogen bond loses over $22\\text{ kJ/mol}$ for a $30^\\circ$ bend.
2. **Consequence for Templating**: Because the halogen bond acts as a rigid, directional "rod", halogen-bonded anion receptors enforce exact angular coordinates during self-assembly, suppressing non-specific conformational isomers and generating crystalline frameworks with predictable lattice dimensions."""
        },
        {
            "probNumber": "3.4",
            "title": "Calix[4]pyrrole Halide Affinities: Conformational Equilibrium and Induced-Fit Binding",
            "difficulty": "Intermediate",
            "statement": """In acetonitrile at $298.15\\text{ K}$, uncomplexed meso-octamethylcalix[4]pyrrole exists in an equilibrium between the inactive 1,3-alternate conformation ($\\text{H}_{\\text{alt}}$) and the binding-competent cone conformation ($\\text{H}_{\\text{cone}}$):
\\[
\\text{H}_{\\text{alt}} \\xrightleftharpoons[K_{\\text{conf}}]{} \\text{H}_{\\text{cone}}, \\quad K_{\\text{conf}} = \\frac{[\\text{H}_{\\text{cone}}]}{[\\text{H}_{\\text{alt}}]} = 2.50 \\times 10^{-3}
\\]
The intrinsic binding of chloride to the cone conformation is:
\\[
\\text{H}_{\\text{cone}} + \\text{Cl}^- \\xrightleftharpoons[K_{\\text{int}}]{} [\\text{Cl}^- \\subset \\text{H}_{\\text{cone}}], \\quad K_{\\text{int}} = 1.40 \\times 10^6\\text{ M}^{-1}
\\]
(a) Derive the relationship connecting the apparent experimental association constant $K_{\\text{app}} = \\frac{[\\text{Complex}]}{[\\text{H}]_{\\text{total, free}} [\\text{Cl}^-]}$ to $K_{\\text{conf}}$ and $K_{\\text{int}}$.
(b) Calculate the numerical value of $K_{\\text{app}}$ in $\\text{M}^{-1}$ and compute the conformational free energy penalty $\\Delta G_{\\text{conf}}^\circ$.
(c) Titration with fluoride yields $K_{\\text{app}}(\\text{F}^-) = 1.70 \\times 10^5\\text{ M}^{-1}$, while bromide yields $K_{\\text{app}}(\\text{Br}^-) = 15.0\\text{ M}^{-1}$. Calculate the halide selectivity factors $S(\\text{F}^-/\\text{Cl}^-)$ and $S(\\text{Cl}^-/\\text{Br}^-)$.""",
            "solution": """### Step 1: Derivation of the Apparent Association Constant
Total uncomplexed host concentration is:
\\[
[\\text{H}]_{\\text{total, free}} = [\\text{H}_{\\text{alt}}] + [\\text{H}_{\\text{cone}}]
\\]
From the conformational equilibrium:
\\[
[\\text{H}_{\\text{cone}}] = K_{\\text{conf}} [\\text{H}_{\\text{alt}}] \\implies [\\text{H}]_{\\text{total, free}} = [\\text{H}_{\\text{alt}}] (1 + K_{\\text{conf}})
\\]
Therefore:
\\[
[\\text{H}_{\\text{cone}}] = \\frac{K_{\\text{conf}}}{1 + K_{\\text{conf}}} [\\text{H}]_{\\text{total, free}}
\\]
The complex concentration is:
\\[
[\\text{Complex}] = K_{\\text{int}} [\\text{H}_{\\text{cone}}] [\\text{Cl}^-] = K_{\\text{int}} \\left( \\frac{K_{\\text{conf}}}{1 + K_{\\text{conf}}} \\right) [\\text{H}]_{\\text{total, free}} [\\text{Cl}^-]
\\]
The apparent experimental association constant is:
\\[
K_{\\text{app}} = \\frac{[\\text{Complex}]}{[\\text{H}]_{\\text{total, free}} [\\text{Cl}^-]} = \\frac{K_{\\text{conf}} K_{\\text{int}}}{1 + K_{\\text{conf}}}
\\]
Since $K_{\\text{conf}} = 2.50 \\times 10^{-3} \\ll 1$, the denominator $1 + K_{\\text{conf}} \\approx 1$:
\\[
K_{\\text{app}} \\approx K_{\\text{conf}} \\cdot K_{\\text{int}}
\\]

### Step 2: Calculation of $K_{\\text{app}}$ and Conformational Penalty
Substitute values:
\\[
K_{\\text{app}} = (2.50 \\times 10^{-3})(1.40 \\times 10^6\\text{ M}^{-1}) = 3.50 \\times 10^3\\text{ M}^{-1}
\\]
The intrinsic binding free energy of the cone conformation is:
\\[
\\Delta G_{\\text{int}}^\circ = -RT \\ln K_{\\text{int}} = -(2.4790\\text{ kJ/mol}) \\ln(1.40 \\times 10^6) = -(2.4790)(14.1519) = -35.08\\text{ kJ/mol}
\\]
The conformational free energy penalty paid to reorganize into the cone conformation is:
\\[
\\Delta G_{\\text{conf}}^\circ = -RT \\ln K_{\\text{conf}} = -(2.4790\\text{ kJ/mol}) \\ln(2.50 \\times 10^{-3}) = -(2.4790)(-5.9915) = +14.85\\text{ kJ/mol}
\\]
The apparent binding free energy is:
\\[
\\Delta G_{\\text{app}}^\circ = \\Delta G_{\\text{int}}^\circ + \\Delta G_{\\text{conf}}^\circ = -35.08 + 14.85 = -20.23\\text{ kJ/mol}
\\]
Notice: Over $42\\%$ of the intrinsic binding free energy ($-35.1\\text{ kJ/mol}$) is consumed paying the conformational reorganization penalty ($+14.9\\text{ kJ/mol}$).

### Step 3: Halide Selectivity Factors
Given:
- $K_{\\text{app}}(\\text{F}^-) = 1.70 \\times 10^5\\text{ M}^{-1}$
- $K_{\\text{app}}(\\text{Cl}^-) = 3.50 \\times 10^3\\text{ M}^{-1}$
- $K_{\\text{app}}(\\text{Br}^-) = 15.0\\text{ M}^{-1}$

1. **Selectivity for Fluoride over Chloride**:
\\[
S(\\text{F}^-/\\text{Cl}^-) = \\frac{K_{\\text{app}}(\\text{F}^-)}{K_{\\text{app}}(\\text{Cl}^-)} = \\frac{1.70 \\times 10^5}{3.50 \\times 10^3} = 48.6
\\]
Fluoride binds $48.6$ times more tightly than chloride.

2. **Selectivity for Chloride over Bromide**:
\\[
S(\\text{Cl}^-/\\text{Br}^-) = \\frac{K_{\\text{app}}(\\text{Cl}^-)}{K_{\\text{app}}(\\text{Br}^-)} = \\frac{3.50 \\times 10^3}{15.0} = 233.3
\\]
Chloride binds over $233$ times more tightly than bromide.

Total selectivity factor between fluoride and bromide:
\\[
S(\\text{F}^-/\\text{Br}^-) = \\frac{1.70 \\times 10^5}{15.0} = 11,\\!333
\\]
Calix[4]pyrrole exhibits a remarkable size cutoff: larger bromide ($r = 1.96\\text{ Å}$) cannot squeeze into the four-pyrrole $\\text{N-H}$ focal point without severe steric clashes with the meso-methyl groups."""
        },
        {
            "probNumber": "3.5",
            "title": "pH-Triggered Cation-to-Anion Receptor Switching: Speciation Analysis",
            "difficulty": "Intermediate",
            "statement": """A ditopic macrocyclic diamine-crown ether $\\text{L}$ has two acid-base protonation constants:
\\[
\\text{p}K_{a1} = 8.20, \\quad \\text{p}K_{a2} = 5.40
\\]
- In the neutral, unprotonated form $\\text{L}$, it acts as a **cation host** for $\\text{Cu}^{2+}$, with stability constant $K_{\\text{Cu}} = 6.00 \\times 10^7\\text{ M}^{-1}$.
- In the diprotonated form $\\text{LH}_2^{2+}$, it acts as an **anion host** for $\\text{SO}_4^{2-}$, with stability constant $K_{\\text{SO4}} = 8.50 \\times 10^5\\text{ M}^{-1}$.
- The monoprotonated form $\\text{LH}^+$ binds neither guest strongly.
(a) Write the fractional speciation functions $\\alpha_0(\\text{pH})$, $\\alpha_1(\\text{pH})$, and $\\alpha_2(\\text{pH})$ for the uncomplexed ligand species $\\text{L}$, $\\text{LH}^+$, and $\\text{LH}_2^{2+}$.
(b) Calculate the percentages of $\\text{L}$ and $\\text{LH}_2^{2+}$ at $\\text{pH} = 10.0$ and at $\\text{pH} = 3.5$.
(c) In a solution containing $[\\text{Cu}^{2+}] = 1.0\\text{ mM}$ and $[\\text{SO}_4^{2-}] = 1.0\\text{ mM}$, calculate the apparent binding constants $K_{\\text{Cu, app}} = \\alpha_0 K_{\\text{Cu}}$ and $K_{\\text{SO4, app}} = \\alpha_2 K_{\\text{SO4}}$ at both pH values. Demonstrate quantitative receptor switching.""",
            "solution": """### Step 1: Fractional Speciation Functions
The protonation equilibria are:
\\[
\\text{LH}_2^{2+} \\xrightleftharpoons[K_{a2}]{} \\text{LH}^+ + \\text{H}^+, \\quad \\text{LH}^+ \\xrightleftharpoons[K_{a1}]{} \\text{L} + \\text{H}^+
\\]
where $K_{a1} = 10^{-8.20} = 6.310 \\times 10^{-9}\\text{ M}$, and $K_{a2} = 10^{-5.40} = 3.981 \\times 10^{-6}\\text{ M}$.
The acid-base denominator polynomial is:
\\[
D([\\text{H}^+]) = [\\text{H}^+]^2 + K_{a2} [\\text{H}^+] + K_{a1} K_{a2}
\\]
The mole fractions of the three species are:
\\[
\\alpha_2(\\text{LH}_2^{2+}) = \\frac{[\\text{H}^+]^2}{D([\\text{H}^+])}
\\]
\\[
\\alpha_1(\\text{LH}^+) = \\frac{K_{a2} [\\text{H}^+]}{D([\\text{H}^+])}
\\]
\\[
\\alpha_0(\\text{L}) = \\frac{K_{a1} K_{a2}}{D([\\text{H}^+])}
\\]

### Step 2: Speciation at $\\text{pH} = 10.0$ and $\\text{pH} = 3.5$
1. **At $\\text{pH} = 10.0$** ($[\\text{H}^+] = 10^{-10}\\text{ M}$):
\\[
[\\text{H}^+]^2 = 10^{-20}
\\]
\\[
K_{a2} [\\text{H}^+] = (3.981 \\times 10^{-6})(10^{-10}) = 3.981 \\times 10^{-16}
\\]
\\[
K_{a1} K_{a2} = (6.310 \\times 10^{-9})(3.981 \\times 10^{-6}) = 2.512 \\times 10^{-14}
\\]
\\[
D = 10^{-20} + 3.981 \\times 10^{-16} + 2.512 \\times 10^{-14} \\approx 2.512 \\times 10^{-14}
\\]
Fractions:
\\[
\\alpha_0(\\text{L}) = \\frac{2.512 \\times 10^{-14}}{2.512 \\times 10^{-14}} = 0.9844 \\quad (98.44\\%)
\\]
\\[
\\alpha_2(\\text{LH}_2^{2+}) = \\frac{10^{-20}}{2.512 \\times 10^{-14}} = 3.98 \\times 10^{-7} \\quad (0.00004\\%)
\\]

2. **At $\\text{pH} = 3.5$** ($[\\text{H}^+] = 10^{-3.5} = 3.162 \\times 10^{-4}\\text{ M}$):
\\[
[\\text{H}^+]^2 = (3.162 \\times 10^{-4})^2 = 1.000 \\times 10^{-7}
\\]
\\[
K_{a2} [\\text{H}^+] = (3.981 \\times 10^{-6})(3.162 \\times 10^{-4}) = 1.259 \\times 10^{-9}
\\]
\\[
K_{a1} K_{a2} = 2.512 \\times 10^{-14}
\\]
\\[
D = 1.000 \\times 10^{-7} + 1.259 \\times 10^{-9} + 2.512 \\times 10^{-14} = 1.0126 \\times 10^{-7}
\\]
Fractions:
\\[
\\alpha_2(\\text{LH}_2^{2+}) = \\frac{1.000 \\times 10^{-7}}{1.0126 \\times 10^{-7}} = 0.9876 \\quad (98.76\\%)
\\]
\\[
\\alpha_0(\\text{L}) = \\frac{2.512 \\times 10^{-14}}{1.0126 \\times 10^{-7}} = 2.48 \\times 10^{-7} \\quad (0.00002\\%)
\\]

### Step 3: Apparent Binding Constants and Switching Demonstration
1. **At $\\text{pH} = 10.0$ (Cation Host Mode)**:
\\[
K_{\\text{Cu, app}} = \\alpha_0 K_{\\text{Cu}} = (0.9844)(6.00 \\times 10^7\\text{ M}^{-1}) = 5.91 \\times 10^7\\text{ M}^{-1}
\\]
\\[
K_{\\text{SO4, app}} = \\alpha_2 K_{\\text{SO4}} = (3.98 \\times 10^{-7})(8.50 \\times 10^5\\text{ M}^{-1}) = 0.338\\text{ M}^{-1}
\\]
Ratio $K_{\\text{Cu, app}} / K_{\\text{SO4, app}} = \\frac{5.91 \\times 10^7}{0.338} = 1.75 \\times 10^8$.
At $\\text{pH} = 10.0$, the receptor is an exclusive **cation host** for $\\text{Cu}^{2+}$, completely ignoring sulfate.

2. **At $\\text{pH} = 3.5$ (Anion Host Mode)**:
\\[
K_{\\text{Cu, app}} = \\alpha_0 K_{\\text{Cu}} = (2.48 \\times 10^{-7})(6.00 \\times 10^7\\text{ M}^{-1}) = 14.9\\text{ M}^{-1}
\\]
\\[
K_{\\text{SO4, app}} = \\alpha_2 K_{\\text{SO4}} = (0.9876)(8.50 \\times 10^5\\text{ M}^{-1}) = 8.39 \\times 10^5\\text{ M}^{-1}
\\]
Ratio $K_{\\text{SO4, app}} / K_{\\text{Cu, app}} = \\frac{8.39 \\times 10^5}{14.9} = 5.63 \\times 10^4$.
At $\\text{pH} = 3.5$, the receptor inverts its function entirely, releasing $\\text{Cu}^{2+}$ and acting as a high-affinity **anion host** for $\\text{SO}_4^{2-}$."""
        },
        {
            "probNumber": "3.6",
            "title": "Organometallic Ferrocenyl Amide Anion Sensing: Electrochemical Peak Shift Analysis",
            "difficulty": "Intermediate",
            "statement": """A redox-active 1,1'-bis(amide)ferrocene receptor $\\text{Fc}$ binds dihydrogen phosphate ($\\text{H}_2\\text{PO}_4^-$) in acetonitrile at $298.15\\text{ K}$.
The uncomplexed receptor exhibits a reversible one-electron oxidation wave at $E_{1/2}^0 = +480\\text{ mV}$ (vs $\\text{Fc/Fc}^+$).
Upon addition of excess $\\text{H}_2\\text{PO}_4^-$, the oxidation wave shifts cathodically to $E_{1/2}^{\\text{bound}} = +310\\text{ mV}$.
The association constant for the neutral $\\text{Fe(II)}$ state was measured independently by $^1\\text{H}$ NMR titration:
$K_a(\\text{Fe}^{\\text{II}}) = 2.80 \\times 10^3\\text{ M}^{-1}$.
(a) Formulate the thermodynamic square cycle connecting $\\text{Fc}$, $\\text{Fc}^+$, $[\\text{Fc}\\cdot\\text{H}_2\\text{PO}_4^-]$, and $[\\text{Fc}^+\\cdot\\text{H}_2\\text{PO}_4^-]$.
(b) Derive the Nernst-based relationship relating the electrochemical potential shift $\\Delta E_{1/2} = E_{1/2}^{\\text{bound}} - E_{1/2}^0$ to the ratio of association constants $K_a(\\text{Fe}^{\\text{III}}) / K_a(\\text{Fe}^{\\text{II}})$.
(c) Calculate the association constant of the oxidized ferrocenium cation for the anion $K_a(\\text{Fe}^{\\text{III}})$ and evaluate the enhancement factor.""",
            "solution": """### Step 1: Thermodynamic Square Cycle
Consider the oxidation and complexation processes:
\\[
\\begin{matrix}
\\text{Fc} & \\xrightarrow{\\quad -e^-, \\, E_{1/2}^0 \\quad} & \\text{Fc}^+ \\\\
\\quad \\Big\\downarrow K_a(\\text{Fe}^{\\text{II}}) & & \\quad \\Big\\downarrow K_a(\\text{Fe}^{\\text{III}}) \\\\
[\\text{Fc}\\cdot\\text{A}^-] & \\xrightarrow{\\quad -e^-, \\, E_{1/2}^{\\text{bound}} \\quad} & [\\text{Fc}^+\\cdot\\text{A}^-]
\\end{matrix}
\\]
where $\\text{A}^- = \\text{H}_2\\text{PO}_4^-$.

### Step 2: Derivation of the Potential Shift
Applying the conservation of free energy around the cycle:
\\[
\\Delta G^\\circ(\\text{top}) + \\Delta G^\\circ(\\text{right}) = \\Delta G^\\circ(\\text{left}) + \\Delta G^\\circ(\\text{bottom})
\\]
The electrochemical free energies of oxidation are:
\\[
\\Delta G_{\\text{ox}}^0 = F E_{1/2}^0, \\quad \\Delta G_{\\text{ox}}^{\\text{bound}} = F E_{1/2}^{\\text{bound}}
\\]
The complexation free energies are:
\\[
\\Delta G_{\\text{II}}^\circ = -RT \\ln K_a(\\text{Fe}^{\\text{II}}), \\quad \\Delta G_{\\text{III}}^\circ = -RT \\ln K_a(\\text{Fe}^{\\text{III}})
\\]
Equating both paths:
\\[
F E_{1/2}^0 - RT \\ln K_a(\\text{Fe}^{\\text{III}}) = -RT \\ln K_a(\\text{Fe}^{\\text{II}}) + F E_{1/2}^{\\text{bound}}
\\]
Rearranging:
\\[
F (E_{1/2}^{\\text{bound}} - E_{1/2}^0) = -RT \\ln K_a(\\text{Fe}^{\\text{III}}) + RT \\ln K_a(\\text{Fe}^{\\text{II}}) = -RT \\ln\\left( \\frac{K_a(\\text{Fe}^{\\text{III}})}{K_a(\\text{Fe}^{\\text{II}})} \\right)
\\]
Dividing by Faraday's constant $F$:
\\[
\\Delta E_{1/2} = E_{1/2}^{\\text{bound}} - E_{1/2}^0 = - \\frac{RT}{F} \\ln\\left( \\frac{K_a(\\text{Fe}^{\\text{III}})}{K_a(\\text{Fe}^{\\text{II}})} \\right)
\\]

### Step 3: Calculation of $K_a(\\text{Fe}^{\\text{III}})$
Given:
- $E_{1/2}^0 = +480\\text{ mV} = +0.480\\text{ V}$
- $E_{1/2}^{\\text{bound}} = +310\\text{ mV} = +0.310\\text{ V}$
- $\\Delta E_{1/2} = 310 - 480 = -170\\text{ mV} = -0.170\\text{ V}$
- $T = 298.15\\text{ K} \\implies \\frac{RT}{F} = \\frac{(8.3145)(298.15)}{96485} = 0.02569\\text{ V} = 25.69\\text{ mV}$
- $K_a(\\text{Fe}^{\\text{II}}) = 2.80 \\times 10^3\\text{ M}^{-1}$

Substitute $\\Delta E_{1/2}$:
\\[
-0.170\\text{ V} = -0.02569\\text{ V} \\times \\ln\\left( \\frac{K_a(\\text{Fe}^{\\text{III}})}{K_a(\\text{Fe}^{\\text{II}})} \\right)
\\]
\\[
\\ln\\left( \\frac{K_a(\\text{Fe}^{\\text{III}})}{K_a(\\text{Fe}^{\\text{II}})} \\right) = \\frac{-0.170}{-0.02569} = 6.6174
\\]
Exponentiating:
\\[
\\frac{K_a(\\text{Fe}^{\\text{III}})}{K_a(\\text{Fe}^{\\text{II}})} = e^{6.6174} = 747.9
\\]
The enhancement factor is $748$.
The binding constant of the oxidized ferrocenium host is:
\\[
K_a(\\text{Fe}^{\\text{III}}) = 747.9 \\times (2.80 \\times 10^3\\text{ M}^{-1}) = 2.094 \\times 10^6\\text{ M}^{-1} \\approx 2.1 \\times 10^6\\text{ M}^{-1}
\\]
The generated positive charge on the $\\text{Fe(III)}$ iron center adds a powerful through-space Coulombic attraction to the bound phosphate anion, amplifying binding by nearly three orders of magnitude."""
        },
        {
            "probNumber": "3.7",
            "title": "Sulfate vs Nitrate Selectivity: Macrobicyclic Hexa-ammonium Cage Binding Mechanics",
            "difficulty": "Advanced",
            "statement": """A macrobicyclic hexa-azacryptand forms a hexaprotonated cage $[\\text{H}_6\\text{L}]^{6+}$ in water at $\\text{pH} = 3.0$.
The cage contains six internal ammonium groups directed into a cavity of diameter $D_{\\text{cav}} = 4.80\\text{ Å}$.
It binds divalent sulfate ($\\text{SO}_4^{2-}$, tetrahedral, thermochemical radius $r_{\\text{therm}} = 2.40\\text{ Å}$) and monovalent nitrate ($\\text{NO}_3^-$, trigonal planar, thermochemical radius $r_{\\text{therm}} = 1.89\\text{ Å}$).
The standard hydration free energies are:
$\\Delta G_{\\text{hyd}}^\circ(\\text{SO}_4^{2-}) = -1080\\text{ kJ/mol}$, $\\Delta G_{\\text{hyd}}^\circ(\\text{NO}_3^-) = -300\\text{ kJ/mol}$.
Inside the cage, the host provides six linear $\\text{N}^+-\\text{H}\\cdots\\text{O}$ hydrogen-bond salt bridges:
- Each hydrogen-bond salt bridge with sulfate releases $\\Delta H_{\\text{HB}}(\\text{SO}_4^{2-}) = -220\\text{ kJ/mol}$.
- Each hydrogen-bond salt bridge with nitrate releases $\\Delta H_{\\text{HB}}(\\text{NO}_3^-) = -75\\text{ kJ/mol}$ (and planar nitrate can only engage three of the six bridgehead protons simultaneously).
(a) Compute the total host-guest interaction enthalpy $\\Delta H_{\\text{host}}$ for both anions inside the cage.
(b) Estimating the net binding free energy in water as $\\Delta G_{\\text{aq}}^\circ \\approx \\Delta H_{\\text{host}} - \\Delta G_{\\text{hyd}}^\circ + \\Delta G_{\\text{cavity}}$, where cavity desolvation $\\Delta G_{\\text{cavity}} \\approx -35\\text{ kJ/mol}$, calculate $\\Delta G_{\\text{aq}}^\circ$ for both complexes.
(c) Compute the selectivity ratio $S(\\text{SO}_4^{2-}/\\text{NO}_3^-) = K_a(\\text{SO}_4^{2-}) / K_a(\\text{NO}_3^-)$ at $298.15\\text{ K}$ and explain how the cage overcomes the enormous $1080\\text{ kJ/mol}$ sulfate hydration barrier.""",
            "solution": """### Step 1: Total Host-Guest Interaction Enthalpies Inside the Cage
1. **For Tetrahedral Sulfate ($\\text{SO}_4^{2-}$)**:
Sulfate presents four tetrahedral oxygen atoms. The six bridgehead $\\text{N}^+-\\text{H}$ groups form six convergent salt bridges bridging the edges and vertices of the sulfate tetrahedron:
\\[
\\Delta H_{\\text{host}}(\\text{SO}_4^{2-}) = 6 \\times (-220\\text{ kJ/mol}) = -1320.0\\text{ kJ/mol}
\\]
2. **For Trigonal Planar Nitrate ($\\text{NO}_3^-$)**:
Planar nitrate possesses only three oxygen atoms. In a 3D spheroidal cage, it can geometrically contact at most three of the six inward-directed protons simultaneously:
\\[
\\Delta H_{\\text{host}}(\\text{NO}_3^-) = 3 \\times (-75\\text{ kJ/mol}) = -225.0\\text{ kJ/mol}
\\]

### Step 2: Net Binding Free Energies in Aqueous Solution
Using $\\Delta G_{\\text{aq}}^\circ \\approx \\Delta H_{\\text{host}} - \\Delta G_{\\text{hyd}}^\circ + \\Delta G_{\\text{cavity}}$ with $\\Delta G_{\\text{cavity}} = -35\\text{ kJ/mol}$:

1. **For Sulfate ($\\text{SO}_4^{2-}$)**:
\\[
\\Delta G_{\\text{aq}}^\circ(\\text{SO}_4^{2-}) = -1320.0 - (-1080.0) + (-35.0) = -1320.0 + 1080.0 - 35.0 = -275.0\\text{ kJ/mol}
\\]
2. **For Nitrate ($\\text{NO}_3^-$)**:
\\[
\\Delta G_{\\text{aq}}^\circ(\\text{NO}_3^-) = -225.0 - (-300.0) + (-35.0) = -225.0 + 300.0 - 35.0 = +40.0\\text{ kJ/mol}
\\]
Notice that for nitrate, $\\Delta G_{\\text{aq}}^\circ > 0$, meaning nitrate cannot displace water from the cage!

### Step 3: Selectivity Ratio and Mechanistic Analysis
The difference in binding free energy is:
\\[
\\Delta \\Delta G^\\circ = \\Delta G_{\\text{aq}}^\circ(\\text{SO}_4^{2-}) - \\Delta G_{\\text{aq}}^\circ(\\text{NO}_3^-) = -275.0 - (+40.0) = -315.0\\text{ kJ/mol}
\\]
At $298.15\\text{ K}$ ($RT = 2.4790\\text{ kJ/mol}$):
\\[
S(\\text{SO}_4^{2-}/\\text{NO}_3^-) = \\exp\\left( -\\frac{\\Delta \\Delta G^\\circ}{RT} \\right) = \\exp\\left( \\frac{315.0}{2.4790} \\right) = \\exp(127.1) > 10^{55}
\\]
The selectivity for sulfate over nitrate is essentially infinite.

**Mechanistic Insight**:
How does the cage conquer the colossal $-1080\\text{ kJ/mol}$ hydration barrier of sulfate?
1. **Multivalent Electrostatic Matching**: Divalent sulfate carries twice the charge of nitrate and four oxygen centers. The six inward-directed ammonium groups deliver a combined electrostatic stabilization of $-1320\\text{ kJ/mol}$, surpassing the $-1080\\text{ kJ/mol}$ dehydration cost by $240\\text{ kJ/mol}$.
2. **Topological Mismatch for Nitrate**: Monovalent nitrate releases only $-225\\text{ kJ/mol}$ of binding enthalpy, failing to compensate for its $-300\\text{ kJ/mol}$ hydration penalty.
3. This illustrates the principle of **charge-density amplification**: multivalent cages with high positive charge densities exclusively extract divalent and trivalent oxoanions from water."""
        },
        {
            "probNumber": "3.8",
            "title": "Anti-Crown Mercuracarborand Chloride Complexation: Macrocyclic Lewis Acid Energetics",
            "difficulty": "Advanced",
            "statement": """Hawthorne's cyclic trimeric mercuracarborand host $[\\text{Hg}(\\text{C}_2\\text{B}_{10}\\text{H}_{10})]_3$ ("anti-crown") acts as a planar macrocyclic Lewis acid:
\\[
\\text{Host} + \\text{Cl}^- \\xrightleftharpoons[K_1]{} [\\text{Cl}^- \\subset \\text{Host}]^-
\\]
Inside the ring, three electrophilic mercury centers coordinate the central chloride ion in a planar trigonal $D_{3h}$ geometry ($d(\\text{Hg}\\cdots\\text{Cl}) = 2.75\\text{ Å}$).
The association constant in dry acetonitrile at $298\\text{ K}$ is $K_1 = 4.50 \\times 10^7\\text{ M}^{-1}$.
Upon addition of a second chloride ion, a sandwich complex forms:
\\[
[\\text{Cl}^- \\subset \\text{Host}]^- + \\text{Cl}^- \\xrightleftharpoons[K_2]{} [(\\text{Cl}^-)_2 \\subset \\text{Host}]^{2-}
\\]
with $K_2 = 1.20 \\times 10^2\\text{ M}^{-1}$.
(a) Calculate $\\Delta G_1^\\circ$ and $\\Delta G_2^\\circ$ in $\\text{kJ/mol}$.
(b) Evaluate the ratio $K_1 / K_2$ and explain why $K_2$ is more than five orders of magnitude smaller than $K_1$.
(c) In an extraction experiment, $10.0\\text{ mL}$ of a $1.00\\text{ mM}$ solution of the anti-crown in 1,2-dichloroethane is equilibrated with $10.0\\text{ mL}$ of an aqueous solution containing $50.0\\text{ mM}$ $\\text{NaCl}$. If the biphasic extraction constant is $K_{\\text{ex}} = 1.80 \\times 10^3\\text{ M}^{-1}$, calculate the percentage of macrocycle converted into the lipophilic $[\\text{Cl}^- \\subset \\text{Host}]^-$ complex.""",
            "solution": """### Step 1: Standard Free Energies of Stepwise Binding
With $RT = (8.3145\\text{ J/(mol}\\cdot\\text{K)})(298.15\\text{ K}) = 2.4790\\text{ kJ/mol}$:

1. **For First Chloride Binding ($K_1 = 4.50 \\times 10^7\\text{ M}^{-1}$)**:
\\[
\\Delta G_1^\\circ = -RT \\ln(4.50 \\times 10^7) = -(2.4790\\text{ kJ/mol})(17.6222) = -43.69\\text{ kJ/mol}
\\]
2. **For Second Chloride Binding ($K_2 = 1.20 \\times 10^2\\text{ M}^{-1}$)**:
\\[
\\Delta G_2^\\circ = -RT \\ln(1.20 \\times 10^2) = -(2.4790\\text{ kJ/mol})(4.7875) = -11.87\\text{ kJ/mol}
\\]

### Step 2: Analysis of the $K_1 / K_2$ Ratio
The ratio of stepwise constants is:
\\[
\\frac{K_1}{K_2} = \\frac{4.50 \\times 10^7}{1.20 \\times 10^2} = 3.75 \\times 10^5
\\]
Free energy difference:
\\[
\\Delta \\Delta G^\\circ = \\Delta G_2^\\circ - \\Delta G_1^\\circ = -11.87 - (-43.69) = +31.82\\text{ kJ/mol}
\\]
Physical reasons why $K_2 \\ll K_1$:
1. **Electrostatic Coulomb Repulsion**: The first complex is already a monovalent anion $[\\text{Cl}^- \\subset \\text{Host}]^-$. Bringing in a second negatively charged $\\text{Cl}^-$ ion requires overcoming intense like-charge Coulombic repulsion.
2. **Loss of Planar Cavity Chelation**: The first chloride sits ideally at the center of the planar macrocycle, coordinating all three $\\text{Hg}$ atoms in-plane ($D_{3h}$). A second chloride cannot enter the cavity and must sit perched above the plane in an axial position, resulting in elongated, weaker $\\text{Hg}\\cdots\\text{Cl}$ coordinate bonds.
3. **Diminished Lewis Acidity**: Coordination of the first chloride donates significant electron density into the empty $6p$ orbitals of the three mercury centers, neutralizing their Lewis acidity and drastically reducing their electrophilic affinity for a second ligand.

### Step 3: Biphasic Extraction Calculation
The extraction equilibrium is:
\\[
\\text{Na}^+(\\text{aq}) + \\text{Cl}^-(\\text{aq}) + \\text{Host}(\\text{org}) \\xrightleftharpoons[K_{\\text{ex}}]{} [\\text{Na}^+(\\text{org}) \\cdots \\text{Cl}^- \\subset \\text{Host}](\\text{org})
\\]
Given:
- $[\text{NaCl}]_{\\text{aq}} = 50.0\\text{ mM} = 0.050\\text{ M}$
- Because $[\text{NaCl}]_{\\text{aq}} \\gg [\\text{Host}]_0 = 1.00\\text{ mM}$, the aqueous concentrations remain constant:
  $[\\text{Na}^+]_{\\text{aq}} = 0.050\\text{ M}$, $[\\text{Cl}^-]_{\\text{aq}} = 0.050\\text{ M}$.
- $K_{\\text{ex}} = 1800\\text{ M}^{-1}$

The extraction expression is:
\\[
K_{\\text{ex}} = \\frac{[\\text{Complex}]_{\\text{org}}}{[\\text{Cl}^-]_{\\text{aq}} [\\text{Host}]_{\\text{free, org}}}
\\]
Let fraction extracted be $\\theta = [\\text{Complex}]_{\\text{org}} / [\\text{Host}]_0$.
Then:
\\[
\\frac{\\theta}{1 - \\theta} = K_{\\text{ex}} [\\text{Cl}^-]_{\\text{aq}} = (1800\\text{ M}^{-1})(0.050\\text{ M}) = 90.0
\\]
Solving for $\\theta$:
\\[
\\theta = \\frac{90.0}{1 + 90.0} = \\frac{90.0}{91.0} = 0.9890 \\quad (98.9\\%)
\\]
The macrocyclic Lewis acid anti-crown extracts **$98.9\\%$** of the macrocycle into the lipophilic chloride-bound complex, effectively pulling inorganic sodium chloride into non-polar 1,2-dichloroethane."""
        },
        {
            "probNumber": "3.9",
            "title": "Competitive Titration & Indicator Displacement Assays (IDA) for Anion Sensing",
            "difficulty": "Advanced",
            "statement": """An optical Indicator Displacement Assay (IDA) is designed to quantify pyrophosphate ($\\text{PPi}^{4-}$) in buffered water at $\\text{pH} = 7.4$.
The assay uses a bis-zinc(II) dipicolylamine receptor $\\text{R}$ and a fluorescent indicator $\\text{I}$ (pyrocatechol violet).
The host-indicator complexation is:
\\[
\\text{R} + \\text{I} \\xrightleftharpoons[K_I]{} \\text{R}\\cdot\\text{I}, \\quad K_I = 2.50 \\times 10^5\\text{ M}^{-1}
\\]
When free, indicator $\\text{I}$ has an absorbance at $\\lambda = 440\\text{ nm}$ with $\\epsilon_{\\text{free}} = 1.80 \\times 10^4\\text{ M}^{-1}\\text{cm}^{-1}$, and complex $\\text{R}\\cdot\\text{I}$ has $\\epsilon_{\\text{bound}} = 2.20 \\times 10^3\\text{ M}^{-1}\\text{cm}^{-1}$.
Upon adding pyrophosphate guest $\\text{G}$, competitive displacement occurs:
\\[
\\text{R}\\cdot\\text{I} + \\text{G} \\xrightleftharpoons[K_{\\text{disp}}]{} \\text{R}\\cdot\\text{G} + \\text{I}
\\]
where $K_G = [\\text{R}\\cdot\\text{G}] / ([\\text{R}][\\text{G}]) = 1.80 \\times 10^7\\text{ M}^{-1}$.
(a) Express the displacement equilibrium constant $K_{\\text{disp}}$ in terms of $K_G$ and $K_I$, and compute its numerical value.
(b) A sensing cuvette ($1.0\\text{ cm}$ pathlength) is prepared with initial concentrations $[\\text{R}]_0 = 20.0\\text{ }\\mu\\text{M}$ and $[\\text{I}]_0 = 20.0\\text{ }\\mu\\text{M}$. Calculate the initial free indicator $[\\text{I}]$ and absorbance $A_0$ at $440\\text{ nm}$ prior to adding analyte.
(c) Addition of pyrophosphate until $[\\text{G}]_{\\text{total}} = 20.0\\text{ }\\mu\\text{M}$ displaces the indicator. Calculate the resulting absorbance $A$ at $440\\text{ nm}$ and evaluate the total absorbance change $\\Delta A$.""",
            "solution": """### Step 1: Displacement Equilibrium Constant $K_{\\text{disp}}$
Consider the two competitive equilibria:
1. $\\text{R} + \\text{I} \\xrightleftharpoons[K_I]{} \\text{R}\\cdot\\text{I} \\implies [\\text{R}\\cdot\\text{I}] = K_I [\\text{R}][\\text{I}]$
2. $\\text{R} + \\text{G} \\xrightleftharpoons[K_G]{} \\text{R}\\cdot\\text{G} \\implies [\\text{R}\\cdot\\text{G}] = K_G [\\text{R}][\\text{G}]$

The displacement reaction is:
\\[
\\text{R}\\cdot\\text{I} + \\text{G} \\xrightleftharpoons[K_{\\text{disp}}]{} \\text{R}\\cdot\\text{G} + \\text{I}
\\]
Its equilibrium constant is:
\\[
K_{\\text{disp}} = \\frac{[\\text{R}\\cdot\\text{G}][\\text{I}]}{[\\text{R}\\cdot\\text{I}][\\text{G}]} = \\frac{K_G [\\text{R}][\\text{G}] \\cdot [\\text{I}]}{K_I [\\text{R}][\\text{I}] \\cdot [\\text{G}]} = \\frac{K_G}{K_I}
\\]
Given:
- $K_G = 1.80 \\times 10^7\\text{ M}^{-1}$
- $K_I = 2.50 \\times 10^5\\text{ M}^{-1}$
\\[
K_{\\text{disp}} = \\frac{1.80 \\times 10^7}{2.50 \\times 10^5} = 72.0 \\quad (\\text{dimensionless})
\\]
Because $K_{\\text{disp}} = 72.0 \\gg 1$, pyrophosphate readily displaces the indicator from the receptor.

### Step 2: Initial State Before Adding Analyte
In the sensing ensemble with $[\\text{R}]_0 = 20.0\\text{ }\\mu\\text{M} = 2.00 \\times 10^{-5}\\text{ M}$ and $[\\text{I}]_0 = 20.0\\text{ }\\mu\\text{M} = 2.00 \\times 10^{-5}\\text{ M}$:
Let $x = [\\text{R}\\cdot\\text{I}]$.
Then $[\\text{R}] = [\\text{I}] = (2.00 \\times 10^{-5}) - x$.
\\[
K_I = \\frac{x}{((2.00 \\times 10^{-5}) - x)^2} = 2.50 \\times 10^5\\text{ M}^{-1}
\\]
Expanding:
\\[
2.50 \\times 10^5 (4.00 \\times 10^{-10} - 4.00 \\times 10^{-5} x + x^2) = x
\\]
\\[
1.00 \\times 10^{-4} - 10.0 x + 2.50 \\times 10^5 x^2 = x
\\]
\\[
2.50 \\times 10^5 x^2 - 11.0 x + 1.00 \\times 10^{-4} = 0
\\]
Solving via the quadratic formula:
\\[
x = \\frac{11.0 - \\sqrt{11.0^2 - 4(2.50 \\times 10^5)(1.00 \\times 10^{-4})}}{2(2.50 \\times 10^5)} = \\frac{11.0 - \\sqrt{121.0 - 100.0}}{5.00 \\times 10^5} = \\frac{11.0 - \\sqrt{21.0}}{5.00 \\times 10^5} = \\frac{11.0 - 4.5826}{5.00 \\times 10^5} = 1.2835 \\times 10^{-5}\\text{ M}
\\]
So:
- Bound complex: $[\\text{R}\\cdot\\text{I}]_0 = 12.84\\text{ }\\mu\\text{M}$
- Free indicator: $[\\text{I}]_0 = 20.0 - 12.84 = 7.16\\text{ }\\mu\\text{M} = 7.16 \\times 10^{-6}\\text{ M}$

Initial absorbance at $440\\text{ nm}$ ($l = 1.0\\text{ cm}$):
\\[
A_0 = \\epsilon_{\\text{free}} [\\text{I}]_0 + \\epsilon_{\\text{bound}} [\\text{R}\\cdot\\text{I}]_0
\\]
\\[
A_0 = (1.80 \\times 10^4)(7.16 \\times 10^{-6}) + (2.20 \\times 10^3)(1.284 \\times 10^{-5}) = 0.1289 + 0.0282 = 0.1571
\\]

### Step 3: Addition of Pyrophosphate Analyte ($[\\text{G}]_{\\text{total}} = 20.0\\text{ }\\mu\\text{M}$)
Since $K_G = 1.80 \\times 10^7\\text{ M}^{-1}$ is exceptionally large and $K_{\\text{disp}} = 72$:
Pyrophosphate binds almost quantitatively to the receptor:
Let the displaced state have $[\\text{R}\\cdot\\text{G}] \\approx 1.82 \\times 10^{-5}\\text{ M}$.
Solving the coupled mass action equations:
The remaining $[\\text{R}\\cdot\\text{I}]$ drops to $1.95\\text{ }\\mu\\text{M} = 1.95 \\times 10^{-6}\\text{ M}$.
The released free indicator concentration rises to:
\\[
[\\text{I}] = [\\text{I}]_0 - [\\text{R}\\cdot\\text{I}] = 20.0\\text{ }\\mu\\text{M} - 1.95\\text{ }\\mu\\text{M} = 18.05\\text{ }\\mu\\text{M} = 1.805 \\times 10^{-5}\\text{ M}
\\]
The new absorbance is:
\\[
A = (1.80 \\times 10^4)(1.805 \\times 10^{-5}) + (2.20 \\times 10^3)(1.95 \\times 10^{-6}) = 0.3249 + 0.0043 = 0.3292
\\]
The total absorbance increase is:
\\[
\\Delta A = A - A_0 = 0.3292 - 0.1571 = +0.1721
\\]
The absorbance at $440\\text{ nm}$ more than doubles ($\Delta A / A_0 = +110\\%$), providing a high-sensitivity colorimetric readout for pyrophosphate detection."""
        }
    ]

    return {
        "id": "unit-3",
        "number": 3,
        "title": "Anion Binding Hosts & Supramolecular Coordination Assemblies",
        "leadSummary": "Fundamental challenges of anion recognition (solvation barriers, diffuse charge, geometric anisotropy), neutral hydrogen-bonding hosts (ureas, thioureas, squaramides), pyrrole and calixpyrrole receptors, positively charged polyammonium and guanidinium hosts, halogen and chalcogen bonding via electropositive sigma-holes, organometallic and Lewis acidic receptors (ferrocene, cobaltocenium, mercuracarborands), switchable pH/redox hosts, and indicator displacement assays (IDA).",
        "simulations": ["sim_supra_anion_recognition_ph_switch"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u3 = get_unit_3()
    print(f"Unit 3 generated: {len(u3['sections'])} sections, {len(u3['problems'])} problems.")
