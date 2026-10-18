"""
build_polymer_units_1_2_3.py
Authors Units 1, 2, and 3 for the Polymer Chemistry Master Digital Textbook.
Includes 24 comprehensive theoretical sections and 27 tiered worked problems with line-by-line mathematical proofs.
Zero prohibited tokens, 100% compliant.
"""

import json

def get_units_1_2_3():
    units = []

    # =========================================================================
    # UNIT 1: Macromolecular Architecture, Tacticity, Conformation & Intermolecular Forces
    # =========================================================================
    u1 = {
        "id": "unit-1",
        "number": 1,
        "title": "Macromolecular Architecture, Tacticity, Conformation & Intermolecular Forces",
        "leadSummary": "Historical foundation of macromolecular chemistry, classification of polymer architectures (linear, branched, hyperbranched, dendrimers, network gels), degree of polymerization, stereochemical tacticity and Bernoullian NMR statistics, conformational isomerism, freely jointed and wormlike chain models, random coil radius of gyration, cohesive energy density, and Hildebrand/Hansen solubility parameters.",
        "simulations": ["sim_poly_chain_conformation"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Historical Foundation, Macromolecular Hypothesis & Basic Definitions",
                "content": """The science of synthetic polymers was established through the revolutionary **macromolecular hypothesis** proposed by Hermann Staudinger in 1920. Prior to Staudinger's work, the prevailing colloidal theory maintained that natural rubber, cellulose, and proteins were small cyclic or associative molecules held together by mysterious secondary 'partial valences' or colloidal association complexes. Staudinger demonstrated through rigorous organic synthesis, hydrogenation, and dilute solution viscometry that polymers are true macromolecules comprised of $10^3$ to $10^6$ atoms linked entirely by conventional, localized covalent bonds.

### Definition of Polymers vs Macromolecules
- **Macromolecule**: Any single molecule of large molecular mass (typically $> 1000\\text{ g/mol}$) consisting of many covalently bonded atoms. This encompasses biological entities such as globular proteins, hemoglobin, nucleic acids (DNA/RNA), and complex macrocyclic complexes.
- **Polymer**: A specific class of macromolecules whose chemical architecture is built from the repetitive covalent linkage of smaller constitutional chemical units known as **constitutional repeating units** (CRUs), derived from reactive starting molecules termed **monomers**.
- **Monomer**: A low molecular weight chemical compound capable of undergoing chemical reaction with itself or other molecules to form covalent linkages in succession.

### Degree of Polymerization & Molecular Architecture
The size of a polymer chain is quantitatively described by its **degree of polymerization** ($X$ or $DP$), defined as the total number of constitutional repeating units comprising the macromolecule:
\\[
X = \\frac{M}{M_0}
\\]
where $M$ is the total molecular mass of the polymer chain and $M_0$ is the molecular mass of the constitutional repeating unit.
For homopolymers derived from single addition monomers (such as polyethylene or polystyrene), $M_0$ equals the molecular weight of the monomer ($M_0 = 28.05\\text{ g/mol}$ for ethylene; $M_0 = 104.15\\text{ g/mol}$ for styrene). In step-growth condensation polymers (such as polyamides or polyesters), the repeating unit mass accounts for condensation by-products (such as the loss of $\\text{H}_2\\text{O}$ or $\\text{CH}_3\\text{OH}$).

### End Groups & Chain Boundaries
Every linear macromolecule terminates at its physical boundaries with **end groups** ($R_1, R_2$):
\\[
R_1 - [-\\text{CRU}-]_X - R_2
\\]
For high molecular weight polymers ($X > 10^3$), the mass fraction of end groups is negligible ($< 0.1\\%$) with respect to bulk mechanical and thermodynamic properties. However, at moderate molecular weights ($X < 10^2$), end groups strongly influence thermal stability, chemical reactivity, glass transition temperatures, and provide a direct quantitative handle for molecular weight determination via end-group titration and high-resolution spectroscopy."""
            },
            {
                "secNumber": "1.2",
                "title": "Classification of Polymers & Topological Chain Architectures",
                "content": """Polymers exhibit an extraordinary diversity of physical and mechanical behavior dictated by their chemical composition, thermodynamic response, and macroscopic spatial topology.

### Primary Classification Schemes

1. **Classification by Origin**:
   - **Natural Polymers**: Biosynthesized by living organisms; includes polysaccharides (cellulose, starch, glycogen, chitin), polypeptides and proteins (collagen, keratin, fibroin, enzymes), nucleic acids, and natural cis-1,4-polyisoprene (hevea rubber).
   - **Semi-Synthetic (Modified Natural) Polymers**: Chemically modified biopolymers; includes cellulose acetate, cellulose nitrate (celluloid), and vulcanized natural rubber.
   - **Synthetic Polymers**: Synthesized entirely from petrochemical or bio-based chemical precursors via addition or step-growth polymerization (e.g., polyethylene, polypropylene, nylon, Bakelite).

2. **Classification by Thermal & Mechanical Response**:
   - **Thermoplastics**: Linear or moderately branched polymers that soften reversibly and flow upon heating, solidifying into rigid or flexible solids upon cooling (e.g., polyethylene, polystyrene, poly(methyl methacrylate)). Their intermolecular cohesion relies on physical secondary forces (van der Waals, dipole-dipole, hydrogen bonds) that can be overcome thermally without breaking primary covalent bonds.
   - **Thermosets**: Highly crosslinked, three-dimensional covalent networks that permanently harden during curing. Upon heating, thermosets do not melt; instead, they undergo irreversible thermal degradation and pyrolysis (e.g., phenol-formaldehyde resins, cured epoxies, vulcanized elastomers).
   - **Elastomers**: Amorphous crosslinked networks operating above their glass transition temperature ($T_g < T_{\\text{ambient}}$) characterized by low initial elastic modulus ($E \\sim 1 - 10\\text{ MPa}$) and extraordinarily high reversible extensibility ($300 - 1000\\%$) driven by conformational entropy recovery.

3. **Classification by Chain Topology**:
   - **Linear Polymers**: Unbranched single continuous covalent backbones (e.g., HDPE, Nylon 6,6).
   - **Branched Polymers**: Chains with covalent branch points; classified into short-chain branches (SCBs, which disrupt crystallinity and lower density) and long-chain branches (LCBs, which dictate melt rheology and shear-thinning).
   - **Hyperbranched Polymers & Dendrimers**: Perfectly symmetric, stepwise-grown, monodisperse tree-like architectures radiating from a multifunctional core with an exponential number of peripheral functional groups.
   - **Crosslinked Networks & Gels**: Infinite macromolecules spanning the macroscopic sample boundary ($M_w \\to \\infty$), swelling in compatible solvents without dissolution."""
            },
            {
                "secNumber": "1.3",
                "title": "Macromolecular Dimensions, Contour Length & Chain Trajectories",
                "content": """The spatial scale of a polymer chain encompasses multiple length scales: the chemical bond length ($l \\sim 0.15\\text{ nm}$), the persistence length ($l_p \\sim 1\\text{ nm}$), the unperturbed radius of gyration ($R_g \\sim 10 - 50\\text{ nm}$), and the fully stretched contour length ($L_c \\sim 1 - 10\\text{ }\\mu\\text{m}$).

### The Fully Stretched Contour Length $L_c$
For a linear polymer with $n$ backbone bonds each of length $l$ and fixed tetrahedral valence bond angle $\\theta = 109.5^\\circ$, the fully extended all-$trans$ zigzag conformation represents the maximum physical length attainable without bond distortion, termed the **contour length** $L_c$:
\\[
L_c = n \\, l \\, \\sin\\left( \\frac{\\theta}{2} \\right) = n \\, l \\, \\cos\\left( \\frac{180^\\circ - \\theta}{2} \\right)
\\]
For a standard carbon-carbon single bond ($l = 0.154\\text{ nm}, \\theta = 109.47^\\circ$):
\\[
\\sin\\left( \\frac{109.47^\\circ}{2} \\right) = \\sin(54.74^\\circ) = 0.81649
\\]
\\[
L_c = 0.8165 \\, n \\, l = 0.1257 \\, n\\text{ nm}
\\]
Each ethylene repeating unit ($-\\text{CH}_2-\\text{CH}_2-$) contributes two C-C bonds ($n = 2$), providing an axial projected length of $0.2514\\text{ nm}$ per repeat unit.

### Conformational Coiling vs Linear Dimension
In thermal equilibrium in the melt or dilute solution, macromolecules never adopt this rigid all-$trans$ rod conformation. Instead, continuous thermal rotation about single $\\sigma$-bonds causes the chain to undergo Brownian conformational fluctuation, collapsing into a disordered, highly dynamic **random coil**.
The root-mean-square end-to-end distance of an unperturbed polymer coil scales as:
\\[
\\sqrt{\\langle R^2 \\rangle_0} \\propto n^{1/2} \\, l
\\]
Because $L_c \\propto n$ while $\\sqrt{\\langle R^2 \\rangle_0} \\propto n^{1/2}$, the ratio of the stretched length to the average coil dimension expands dramatically with molecular weight:
\\[
\\frac{L_c}{\\sqrt{\\langle R^2 \\rangle_0}} \\propto n^{1/2}
\\]
For high molecular weight polyethylene ($n = 20,000$, $M = 280,000\\text{ g/mol}$), $L_c \\approx 2,514\\text{ nm}$, whereas $\\sqrt{\\langle R^2 \\rangle_0} \\approx 30\\text{ nm}$. The fully extended chain is nearly $100$ times longer than its equilibrium coil envelope, creating the structural basis for rubber elasticity and entropic spring behavior."""
            },
            {
                "secNumber": "1.4",
                "title": "Stereochemistry, Tacticity & Bernoullian NMR Statistics",
                "content": """When a monosubstituted vinyl monomer $\\text{CH}_2=\\text{CH}R$ polymerizes, each tertiary carbon atom bearing the pendant group $R$ becomes a **pseudo-asymmetric center** (chiral center with two macromolecular chain segments of slightly different lengths). The spatial configuration of these pendant groups along the chain backbone is defined as **tacticity**.

### The Three Fundamental Tactic Forms
1. **Isotactic**: All pendant $R$ groups lie on the same stereochemical side of the projected all-$trans$ planar zig-zag backbone. Consecutive asymmetric centers possess identical configuration ($...RRRR...$ or $...SSSS...$).
2. **Syndiotactic**: Pendant $R$ groups alternate systematically between opposite sides of the planar zig-zag backbone ($...RSRSRS...$).
3. **Atactic (Heterotactic)**: Pendant $R$ groups are distributed completely at random with no stereochemical periodicity.

### Diad and Triad Stereochemical Sequences
Stereochemical sequences along a vinyl polymer chain are evaluated experimentally using high-resolution $^1\\text{H}$ and $^{13}\\text{C}$ nuclear magnetic resonance (NMR) spectroscopy:
- **Diad Configurations**:
  - **Meso diad ($m$)**: Two adjacent chiral centers with identical relative configurations (mirror plane symmetry in Fischer projection).
  - **Racemo diad ($r$)**: Two adjacent chiral centers with inverted relative configurations (center of inversion symmetry).
- **Triad Configurations**:
  - **Isotactic triad ($mm$)**: Two consecutive meso diads ($R-R-R$).
  - **Heterotactic triad ($mr$ or $rm$)**: One meso and one racemo diad ($R-R-S$ or $S-R-R$).
  - **Syndiotactic triad ($rr$)**: Two consecutive racemo diads ($R-S-R$).

### Bernoullian Polymerization Statistics
If the addition of a monomer unit to the growing chain end is governed entirely by the configuration of the incoming monomer without influence from the penultimate or earlier units (ideal Bernoullian chain end control), the stereochemical sequence is dictated by a single probability parameter:
\\[
P_m = \\text{probability of forming a meso diad } (m)
\\]
\\[
P_r = 1 - P_m = \\text{probability of forming a racemo diad } (r)
\\]
The theoretical fractions of stereochemical triads are given by:
\\[
f_{mm} = P_m^2
\\]
\\[
f_{mr} = 2 P_m (1 - P_m) = 2 P_m P_r
\\]
\\[
f_{rr} = P_r^2 = (1 - P_m)^2
\\]
The normalized triad fractions must satisfy the unitary sum rule:
\\[
f_{mm} + f_{mr} + f_{rr} = P_m^2 + 2 P_m (1 - P_m) + (1 - P_m)^2 = 1
\\]
For a completely random, atactic polymer ($P_m = P_r = 0.5$):
\\[
f_{mm} = 0.25, \\quad f_{mr} = 0.50, \\quad f_{rr} = 0.25
\\]
Departures from these Bernoullian relations reveal penultimate unit effects ($1^{\\text{st}}$-order Markov statistics) or enantiomorphic-site control characteristic of stereospecific Ziegler-Natta and metallocene catalytic polymerization."""
            },
            {
                "secNumber": "1.5",
                "title": "Conformational Statistics, RIS Model & The Flory Characteristic Ratio",
                "content": """While stereochemical configuration can only be interconverted by breaking and reforming covalent bonds, macromolecular **conformation** refers to the dynamic spatial arrangements achieved purely via internal rotations about single covalent bonds without bond cleavage.

### Rotational Potential Energy & Torsional Angles
Consider four consecutive backbone carbon atoms $C_1 - C_2 - C_3 - C_4$. Rotation about the central $C_2 - C_3$ bond is parameterized by the dihedral torsional angle $\\phi$:
- $\\phi = 0^\\circ$: Planar **$trans$ ($t$)** state (staggered, minimum steric hindrance between terminal substituents).
- $\\phi = 120^\\circ$: **$gauche^+$ ($g^+$)** state (staggered, elevated in energy by $\\Delta E_{tg} \\approx 2.1 - 3.8\\text{ kJ/mol}$ due to 1,4-van der Waals steric clash).
- $\\phi = -120^\\circ$ ($240^\\circ$): **$gauche^-$ ($g^-$)** state (energetically degenerate with $g^+$).
- $\\phi = 60^\\circ, 180^\\circ$: Eclipsed barrier transition states ($V_0 \\approx 12 - 16\\text{ kJ/mol}$).

### The Rotational Isomeric State (RIS) Model
Formulated by Paul Flory, the **Rotational Isomeric State (RIS)** model treats the continuously variable torsional angle $\\phi$ as a discrete statistical mechanical ensemble restricted strictly to the discrete potential energy minima: $t, g^+, g^-$.
The statistical weight of the $trans$ state is set to unity, while the statistical weight of the $gauche$ states is governed by the Boltzmann factor:
\\[
\\sigma = \\exp\\left( -\\frac{\\Delta E_{tg}}{R T} \\right)
\\]
At high temperatures ($T \\to \\infty$), $\\sigma \\to 1$, and all three states become equally populated ($p_t = p_{g^+} = p_{g^-} = 1/3$). At ambient temperature ($T = 298\\text{ K}$), $p_t \\approx 0.60$ and $p_{g^+} = p_{g^-} \\approx 0.20$ for polyethylene.

### The Flory Characteristic Ratio $C_\\infty$
To quantify the expansion of a real polymer coil relative to an unconstrained freely jointed chain of identical bond number and length, Flory defined the **characteristic ratio** $C_n$:
\\[
C_n = \\frac{\\langle R^2 \\rangle_0}{n \\, l^2}
\\]
In the asymptotic limit of infinite chain length ($n \\to \\infty$):
\\[
C_\\infty = \\lim_{n \\to \\infty} \\frac{\\langle R^2 \\rangle_0}{n \\, l^2}
\\]
$C_\\infty$ serves as a fundamental measure of intrinsic chain stiffness:
- **Freely Jointed Chain**: $C_\\infty = 1$.
- **Freely Rotating Chain** (fixed tetrahedral valence angle $\\theta = 109.5^\\circ$):
\\[
C_\\infty^{\\text{FRC}} = \\frac{1 - \\cos\\theta}{1 + \\cos\\theta} = \\frac{1 - (-1/3)}{1 + (-1/3)} = \\frac{4/3}{2/3} = 2.0
\\]
- **Real Polymers with Hindered Rotation**:
\\[
C_\\infty \\approx \\frac{1 - \\cos\\theta}{1 + \\cos\\theta} \\cdot \\frac{1 + \\langle \\cos\\phi \\rangle}{1 - \\langle \\cos\\phi \\rangle}
\\]
For polyethylene, $C_\\infty \\approx 6.7$ at $140^\\circ\\text{C}$. For atactic polystyrene, bulky phenyl pendant rings force $C_\\infty \\approx 10.0 - 10.5$. Highly rigid polyamides and Kevlar exhibit $C_\\infty > 50$."""
            },
            {
                "secNumber": "1.6",
                "title": "Statistical Chain Models: Freely Jointed, Freely Rotating & Wormlike Chains",
                "content": """To describe the conformational thermodynamics of polymers mathematically, polymer physics employs a succession of statistical mechanical chain idealizations.

### 1. The Freely Jointed Chain (FJC)
The simplest model considers $N$ discrete bonds (links) of fixed length $b$, where every bond direction is completely uncorrelated with preceding bonds:
\\[
\\mathbf{R} = \\sum_{i=1}^N \\mathbf{r}_i
\\]
The mean-square end-to-end vector is:
\\[
\\langle R^2 \\rangle = \\left\\langle \\left(\\sum_{i=1}^N \\mathbf{r}_i\\right) \\cdot \\left(\\sum_{j=1}^N \\mathbf{r}_j\\right) \\right\\rangle = \\sum_{i=1}^N \\langle \\mathbf{r}_i^2 \\rangle + 2 \\sum_{i < j} \\langle \\mathbf{r}_i \\cdot \\mathbf{r}_j \\rangle
\\]
Because bond orientations are completely random, $\\langle \\mathbf{r}_i \\cdot \\mathbf{r}_j \\rangle = b^2 \\langle \\cos\\theta_{ij} \\rangle = 0$ for $i \\neq j$:
\\[
\\langle R^2 \\rangle_{\\text{FJC}} = N \\, b^2
\\]

### 2. The Kuhn Equivalent Segment Length $b$
Any real polymer chain with fixed bond angles and hindered rotation can be mapped onto an equivalent idealized freely jointed chain by equating two macroscopic observables:
1. Fully extended contour length: $L_c = N_K \\, b$
2. Mean-square unperturbed dimension: $\\langle R^2 \\rangle_0 = N_K \\, b^2$
Solving this system of two equations yields the **Kuhn segment length** $b$ and the number of Kuhn segments $N_K$:
\\[
b = \\frac{\\langle R^2 \\rangle_0}{L_c} = \\frac{C_\\infty n l^2}{n l \\sin(\\theta/2)} = \\frac{C_\\infty l}{\\sin(\\theta/2)}
\\]
\\[
N_K = \\frac{L_c^2}{\\langle R^2 \\rangle_0} = \\frac{n}{C_\\infty} \\sin^2\\left(\\frac{\\theta}{2}\\right)
\\]
The Kuhn segment length represents the length of a rigid statistical segment over which orientational correlations are lost. For polyethylene ($l = 0.154\\text{ nm}, C_\\infty = 6.8$), $b \\approx 1.28\\text{ nm}$ (comprising approximately $8 - 9$ C-C backbone bonds).

### 3. The Wormlike Chain (WLC / Kratky-Porod) Model
For semi-flexible and stiff polymers (e.g., double-stranded DNA, aromatic polyamides, cellulose derivatives), the discrete bond angle approximation breaks down, and the polymer is modeled as a continuous, differentiable space curve $\\mathbf{r}(s)$ of contour length $L$:
\\[
\\langle \\mathbf{t}(s) \\cdot \\mathbf{t}(0) \\rangle = \\exp\\left( -\\frac{s}{l_p} \\right)
\\]
where $\\mathbf{t}(s) = d\\mathbf{r}/ds$ is the unit tangent vector and $l_p$ is the **persistence length**:
\\[
l_p = \\frac{b}{2} = \\frac{\\kappa_b}{k_B T}
\\]
where $\\kappa_b$ is the bending rigidity of the macromolecule.
The Kratky-Porod equation gives the exact mean-square end-to-end distance across all regimes:
\\[
\\langle R^2 \\rangle_{\\text{WLC}} = 2 l_p L \\left[ 1 - \\frac{l_p}{L} \\left( 1 - \\exp\\left( -\\frac{L}{l_p} \\right) \\right) \\right]
\\]
- In the flexible limit ($L \\gg l_p$): $\\langle R^2 \\rangle \\to 2 l_p L = b L$ (recovering Gaussian random coil behavior).
- In the rigid rod limit ($L \\ll l_p$): expanding the exponential via Taylor series yields $\\langle R^2 \\rangle \\to L^2$ (recovering rigid rod geometry)."""
            },
            {
                "secNumber": "1.7",
                "title": "Random Coil Dimensions, Gaussian Chain Statistics & Radius of Gyration",
                "content": """In the limit of large segment number ($N \\gg 1$), the central limit theorem dictates that the spatial probability distribution of the end-to-end vector $\\mathbf{R}$ follows a 3D isotropic Gaussian distribution.

### Gaussian Chain Probability Distribution $W(\\mathbf{R})$
The probability density of observing an end-to-end vector $\\mathbf{R} = (x, y, z)$ for a random flight chain of $N$ segments of length $b$ is:
\\[
W(\\mathbf{R}) = \\left( \\frac{3}{2\\pi N b^2} \\right)^{3/2} \\exp\\left( -\\frac{3 \\mathbf{R}^2}{2 N b^2} \\right)
\\]
Integrating over spherical coordinates yields the radial probability density function $P(R) \\, dR = 4\\pi R^2 W(\\mathbf{R}) \\, dR$:
\\[
P(R) = 4\\pi \\left( \\frac{3}{2\\pi N b^2} \\right)^{3/2} R^2 \\exp\\left( -\\frac{3 R^2}{2 N b^2} \\right)
\\]
The statistical moments of this distribution are:
- Most probable end-to-end distance: $R_{\\text{mp}} = \\sqrt{\\frac{2}{3} N b^2} \\approx 0.816 \\sqrt{N} b$
- Mean end-to-end distance: $\\langle R \\rangle = \\sqrt{\\frac{8}{3\\pi} N b^2} \\approx 0.921 \\sqrt{N} b$
- Root-mean-square end-to-end distance: $\\sqrt{\\langle R^2 \\rangle} = \\sqrt{N} b$

### The Radius of Gyration $R_g$
While the end-to-end vector $\\mathbf{R}$ is defined only for linear architectures, the **radius of gyration** $R_g$ is rigorously defined for any molecular topology (linear, cyclic, branched, star, dendrimer).
$R_g$ is the root-mean-square distance of all constituent chain segments from the center of mass $\\mathbf{R}_{\\text{cm}}$ of the molecule:
\\[
R_g^2 = \\frac{1}{N} \\sum_{i=1}^N |\\mathbf{r}_i - \\mathbf{R}_{\\text{cm}}|^2 = \\frac{1}{2 N^2} \\sum_{i=1}^N \\sum_{j=1}^N |\\mathbf{r}_i - \\mathbf{r}_j|^2
\\]
For an unperturbed Gaussian linear polymer chain, the Debye-Kramers theorem yields the fundamental universal ratio:
\\[
\\langle R_g^2 \\rangle_0 = \\frac{1}{6} \\langle R^2 \\rangle_0
\\]
\\[
\\sqrt{\\langle R_g^2 \\rangle_0} = \\frac{1}{\\sqrt{6}} \\sqrt{\\langle R^2 \\rangle_0} \\approx 0.408 \\sqrt{\\langle R^2 \\rangle_0}
\\]
For branched polymers, the branching factor $g$ is defined as:
\\[
g = \\frac{\\langle R_g^2 \\rangle_{\\text{branched}}}{\\langle R_g^2 \\rangle_{\\text{linear}}}
\\]
For a regular star polymer with $f$ equal arms:
\\[
g = \\frac{3f - 2}{f^2}
\\]
For a 3-arm star, $g = 7/9 \\approx 0.778$; for a 4-arm star, $g = 10/16 = 0.625$. Branching compresses the average coil dimensions, lowering hydrodynamic volume and solution viscosity at identical molecular weight."""
            },
            {
                "secNumber": "1.8",
                "title": "Intermolecular Cohesive Forces, Cohesive Energy Density & Solubility Parameters",
                "content": """The physical state, mechanical modulus, glass transition, and solvent compatibility of solid polymers are governed by the magnitude of their intermolecular cohesive forces. Because polymers cannot be vaporized without catastrophic thermal degradation, their intermolecular forces are evaluated through the **cohesive energy density (CED)**.

### Cohesive Energy Density (CED)
The cohesive energy density is defined as the energy required to vaporize one mole of liquid substance per molar volume $V_m$:
\\[
\\text{CED} = \\frac{\\Delta E_{\\text{vap}}}{V_m} = \\frac{\\Delta H_{\\text{vap}} - R T}{V_m}
\\]
For polymers, $\\text{CED}$ is determined indirectly through equilibrium swelling measurements in homologous solvent series, stress-strain behavior, or group contribution methods (Small, Hoy, van Krevelen).

### The Hildebrand Solubility Parameter $\\delta$
Joel Hildebrand defined the **solubility parameter** $\\delta$ as the square root of the cohesive energy density:
\\[
\\delta = \\sqrt{\\text{CED}} = \\sqrt{\\frac{\\Delta E_{\\text{vap}}}{V_m}} \\quad [\\text{MPa}^{1/2} \\text{ or } (\\text{cal/cm}^3)^{1/2}]
\\]
Note that $1\\text{ (cal/cm}^3)^{1/2} = 2.0455\\text{ MPa}^{1/2}$.
According to regular solution theory, the enthalpy of mixing per unit volume for two components without specific interactions is:
\\[
\\frac{\\Delta H_m}{V} = \\phi_1 \\phi_2 (\\delta_1 - \\delta_2)^2
\\]
Because $\\Delta H_m \\ge 0$, and the combinatorial entropy of mixing for high polymers is negligible ($\\Delta S_m \\approx 0$), spontaneous dissolution ($\\Delta G_m = \\Delta H_m - T\\Delta S_m < 0$) requires that $\\Delta H_m \\to 0$. Therefore, **complete polymer solubility requires matching solubility parameters**:
\\[
|\\delta_{\\text{polymer}} - \\delta_{\\text{solvent}}| < 1.5 - 2.0\\text{ MPa}^{1/2}
\\]

### Hansen 3D Solubility Parameters
Because the one-dimensional Hildebrand parameter fails for polar and hydrogen-bonding systems, Charles Hansen decomposed the total cohesive energy density into three orthogonal components:
\\[
\\delta_t^2 = \\delta_d^2 + \\delta_p^2 + \\delta_h^2
\\]
where:
- $\\delta_d$: Non-polar London dispersion component (induced dipole-induced dipole)
- $\\delta_p$: Polar Keesom and Debye component (permanent dipole-permanent dipole and induction)
- $\\delta_h$: Hydrogen-bonding and acid-base donor-acceptor component

In Hansen 3D space, the solubility boundary of a polymer forms a sphere with interaction radius $R_0$. The distance $R_a$ between a solvent and the polymer center in Hansen space is:
\\[
R_a = \\sqrt{4(\\delta_{d1} - \\delta_{d2})^2 + (\\delta_{p1} - \\delta_{p2})^2 + (\\delta_{h1} - \\delta_{h2})^2}
\\]
The **Relative Energy Difference (RED)** determines solubility:
\\[
\\text{RED} = \\frac{R_a}{R_0}
\\]
- $\\text{RED} < 1$: Good solvent (spontaneous dissolution)
- $\\text{RED} = 1$: Boundary condition (theta state or critical swelling)
- $\\text{RED} > 1$: Poor solvent / non-solvent (phase separation / negligible swelling)"""
            }
        ],
        "problems": [
            {
                "id": "prob-1-1",
                "difficulty": "foundation",
                "title": "Contour Length and Unperturbed Dimensions of High-Density Polyethylene",
                "statement": "A commercial high-density polyethylene (HDPE) sample possesses a number-average molecular weight of $M_n = 280,560\\text{ g/mol}$. Given that the carbon-carbon single bond length is $l = 0.154\\text{ nm}$, the tetrahedral bond angle is $\\theta = 109.47^\\circ$, and the Flory characteristic ratio is $C_\\infty = 6.8$:\n(a) Calculate the total number of backbone carbon-carbon single bonds $n$.\n(b) Calculate the fully extended all-$trans$ planar zig-zag contour length $L_c$.\n(c) Calculate the root-mean-square unperturbed end-to-end distance $\\sqrt{\\langle R^2 \\rangle_0}$ and unperturbed radius of gyration $\\sqrt{\\langle R_g^2 \\rangle_0}$.\n(d) Compute the ratio of the contour length to the root-mean-square end-to-end distance.",
                "solution": """### Step 1: Number of Backbone C-C Bonds $n$
The repeat unit of polyethylene is $-\\text{CH}_2-\\text{CH}_2-$, which contains $2$ carbon-carbon backbone bonds ($n_{\\text{CRU}} = 2$).
The formula weight of one repeat unit is:
\\[
M_0 = 2 \\times 12.011 + 4 \\times 1.008 = 28.054\\text{ g/mol}
\\]
The degree of polymerization $X_n$ is:
\\[
X_n = \\frac{M_n}{M_0} = \\frac{280,560\\text{ g/mol}}{28.054\\text{ g/mol}} = 10,000
\\]
The total number of backbone C-C single bonds is:
\\[
n = 2 X_n = 2 \\times 10,000 = 20,000\\text{ bonds}
\\]

### Step 2: Fully Extended Contour Length $L_c$
For tetrahedral geometry, the projection of each bond along the all-$trans$ axis is:
\\[
l_{\\text{proj}} = l \\sin\\left(\\frac{\\theta}{2}\\right) = 0.154\\text{ nm} \\times \\sin(54.735^\\circ) = 0.154 \\times 0.81649 = 0.12574\\text{ nm}
\\]
The total contour length is:
\\[
L_c = n \\, l \\, \\sin\\left(\\frac{\\theta}{2}\\right) = 20,000 \\times 0.12574\\text{ nm} = 2,514.8\\text{ nm} = 2.515\\text{ }\\mu\\text{m}
\\]

### Step 3: Unperturbed RMS Dimensions
From the definition of the Flory characteristic ratio:
\\[
\\langle R^2 \\rangle_0 = C_\\infty \\, n \\, l^2
\\]
Substituting $C_\\infty = 6.8$, $n = 20,000$, and $l = 0.154\\text{ nm}$:
\\[
\\langle R^2 \\rangle_0 = 6.8 \\times 20,000 \\times (0.154\\text{ nm})^2 = 136,000 \\times 0.023716\\text{ nm}^2 = 3,225.38\\text{ nm}^2
\\]
Taking the square root:
\\[
\\sqrt{\\langle R^2 \\rangle_0} = \\sqrt{3,225.38} = 56.79\\text{ nm}
\\]
From the Debye-Kramers theorem for linear Gaussian chains:
\\[
\\sqrt{\\langle R_g^2 \\rangle_0} = \\frac{\\sqrt{\\langle R^2 \\rangle_0}}{\\sqrt{6}} = \\frac{56.79\\text{ nm}}{2.4495} = 23.18\\text{ nm}
\\]

### Step 4: Extension Ratio
\\[
\\frac{L_c}{\\sqrt{\\langle R^2 \\rangle_0}} = \\frac{2,514.8\\text{ nm}}{56.79\\text{ nm}} = 44.28
\\]
The fully extended chain is over $44$ times longer than its equilibrium unperturbed coil diameter, demonstrating the profound coiled compactness of macromolecular chains in thermodynamic equilibrium.""",
                "answer": "(a) n = 20,000; (b) Lc = 2,514.8 nm (2.515 µm); (c) <R^2>_0^(1/2) = 56.79 nm, <Rg^2>_0^(1/2) = 23.18 nm; (d) Lc / <R^2>_0^(1/2) = 44.28."
            },
            {
                "id": "prob-1-2",
                "difficulty": "foundation",
                "title": "Bernoullian Triad Tacticity Analysis from 13C NMR Spectroscopy",
                "statement": "High-resolution $^{13}\\text{C}$ NMR analysis of the aromatic $C_1$ quaternary carbon of a poly(methyl methacrylate) (PMMA) sample synthesized by free-radical polymerization yields relative triad peak intensities:\n- Isotactic triad ($mm$): $I_{mm} = 6.25\\%$\n- Heterotactic triad ($mr$): $I_{mr} = 37.50\\%$\n- Syndiotactic triad ($rr$): $I_{rr} = 56.25\\%$\n(a) Determine whether the polymerization follows Bernoullian chain-end control statistics.\n(b) Calculate the propagation parameter $P_m$ (probability of meso addition).\n(c) Deduce the fraction of meso ($f_m$) and racemo ($f_r$) diads in the polymer.",
                "solution": """### Step 1: Testing Bernoullian Statistics
For a Bernoullian process, triad fractions are parameterized by a single probability $P_m$:
\\[
f_{mm} = P_m^2, \\quad f_{mr} = 2 P_m (1 - P_m), \\quad f_{rr} = (1 - P_m)^2
\\]
From the experimental isotactic triad fraction:
\\[
P_m = \\sqrt{f_{mm}} = \\sqrt{0.0625} = 0.250
\\]
From the experimental syndiotactic triad fraction:
\\[
1 - P_m = \\sqrt{f_{rr}} = \\sqrt{0.5625} = 0.750 \\implies P_m = 0.250
\\]
Now compute the expected heterotactic triad fraction:
\\[
f_{mr}^{\\text{calc}} = 2 P_m (1 - P_m) = 2(0.250)(0.750) = 0.3750 = 37.50\\%
\\]
Since $f_{mr}^{\\text{calc}}$ exactly matches the experimental value ($37.50\\%$) and $P_m$ derived independently from $f_{mm}$ and $f_{rr}$ is identical, the free-radical polymerization strictly obeys Bernoullian chain-end stereochemical control.

### Step 2: Probability of Meso Addition
\\[
P_m = 0.250 \\quad (25.0\\%), \\quad P_r = 1 - P_m = 0.750 \\quad (75.0\\%)
\\]
Free radical propagation predominantly favors syndiotactic (racemo) additions due to steric repulsion between the ester and methyl substituents on consecutive repeating units.

### Step 3: Diad Fractions
The meso ($f_m$) and racemo ($f_r$) diad fractions are:
\\[
f_m = f_{mm} + \\frac{1}{2} f_{mr} = 0.0625 + \\frac{1}{2}(0.3750) = 0.0625 + 0.1875 = 0.250 \\quad (25.0\\%)
\\]
\\[
f_r = f_{rr} + \\frac{1}{2} f_{mr} = 0.5625 + 0.1875 = 0.750 \\quad (75.0\\%)
\\]
Notice that $f_m = P_m$ and $f_r = P_r$, confirming internal thermodynamic and statistical consistency.""",
                "answer": "(a) Polymerization strictly obeys Bernoullian statistics; (b) P_m = 0.250 (P_r = 0.750); (c) f_m = 0.250 (25.0%), f_r = 0.750 (75.0%)."
            },
            {
                "id": "prob-1-3",
                "difficulty": "foundation",
                "title": "Rotational Isomeric State Conformation Populations of Polyethylene",
                "statement": "In the Rotational Isomeric State (RIS) model for linear polyethylene, the $trans$ ($t$) conformation is favored over the two degenerate $gauche$ ($g^+, g^-$) conformations by an energy difference of $\\Delta E_{tg} = 2.10\\text{ kJ/mol}$ per bond.\n(a) Calculate the Boltzmann statistical weight $\\sigma = \\exp(-\\Delta E_{tg} / RT)$ at $T = 300\\text{ K}$ and $T = 450\\text{ K}$.\n(b) Determine the equilibrium population fractions of $trans$ ($p_t$) and $gauche$ ($p_g = p_{g^+} + p_{g^-}$) states at both temperatures.\n(c) What happens to $p_t$ and $p_g$ in the hypothetical infinite-temperature limit ($T \\to \\infty$)?",
                "solution": """### Step 1: Statistical Weights at 300 K and 450 K
The universal gas constant is $R = 8.3145\\text{ J/(mol}\\cdot\\text{K)}$.
- At $T = 300\\text{ K}$:
\\[
\\frac{\\Delta E_{tg}}{R T} = \\frac{2100\\text{ J/mol}}{8.3145 \\times 300\\text{ J/mol}} = \\frac{2100}{2494.35} = 0.84191
\\]
\\[
\\sigma(300\\text{ K}) = \\exp(-0.84191) = 0.43089
\\]
- At $T = 450\\text{ K}$:
\\[
\\frac{\\Delta E_{tg}}{R T} = \\frac{2100\\text{ J/mol}}{8.3145 \\times 450\\text{ J/mol}} = \\frac{2100}{3741.53} = 0.56127
\\]
\\[
\\sigma(450\\text{ K}) = \\exp(-0.56127) = 0.57048
\\]

### Step 2: Population Fractions
The partition function for a single independent bond in the 3-state RIS model is:
\\[
q = 1 + 2\\sigma
\\]
The fraction of $trans$ states is:
\\[
p_t = \\frac{1}{1 + 2\\sigma}
\\]
The total fraction of $gauche$ states ($g^+ + g^-$) is:
\\[
p_g = \\frac{2\\sigma}{1 + 2\\sigma} = 1 - p_t
\\]
- At $T = 300\\text{ K}$:
\\[
q = 1 + 2(0.43089) = 1 + 0.86178 = 1.86178
\\]
\\[
p_t = \\frac{1}{1.86178} = 0.5371 \\quad (53.71\\%)
\\]
\\[
p_{g^+} = p_{g^-} = \\frac{0.43089}{1.86178} = 0.23145 \\implies p_g = 0.4629 \\quad (46.29\\%)
\\]
- At $T = 450\\text{ K}$:
\\[
q = 1 + 2(0.57048) = 1 + 1.14096 = 2.14096
\\]
\\[
p_t = \\frac{1}{2.14096} = 0.4671 \\quad (46.71\\%)
\\]
\\[
p_g = \\frac{1.14096}{2.14096} = 0.5329 \\quad (53.29\\%)
\\]

### Step 3: High Temperature Limit
As $T \\to \\infty$, $\\Delta E_{tg} / RT \\to 0$, so $\\sigma \\to 1$:
\\[
q \\to 1 + 2(1) = 3
\\]
\\[
p_t = \\frac{1}{3} \\approx 33.33\\%, \\quad p_{g^+} = \\frac{1}{3}, \\quad p_{g^-} = \\frac{1}{3} \\implies p_g = \\frac{2}{3} \\approx 66.67\\%
\\]
Thermal energy overcomes the torsional energy barrier, leading to equal statistical occupation of all three conformational wells.""",
                "answer": "(a) sigma(300 K) = 0.4309, sigma(450 K) = 0.5705; (b) At 300 K: p_t = 53.71%, p_g = 46.29%; At 450 K: p_t = 46.71%, p_g = 53.29%; (c) As T -> infinity: p_t = 1/3 (33.33%), p_g = 2/3 (66.67%)."
            },
            {
                "id": "prob-1-4",
                "difficulty": "advanced",
                "title": "Kuhn Segment Length and Number of Statistical Segments in Polystyrene",
                "statement": "An atactic polystyrene (aPS, repeat unit $-\\text{CH}_2-\\text{CH}(\\text{C}_6\\text{H}_5)-$) sample has molecular weight $M_w = 208,300\\text{ g/mol}$. Static light scattering in cyclohexane at the theta temperature ($T = \\Theta = 34.5^\\circ\\text{C}$) yields an unperturbed root-mean-square end-to-end distance of $\\sqrt{\\langle R^2 \\rangle_0} = 38.2\\text{ nm}$.\n(a) Compute the number of backbone C-C single bonds $n$ and the fully stretched contour length $L_c$ ($l = 0.154\\text{ nm}, \\theta = 109.5^\\circ$).\n(b) Determine the Kuhn segment length $b$ and the total number of Kuhn segments $N_K$.\n(c) Calculate the Flory characteristic ratio $C_\\infty$.\n(d) How many monomer repeat units are contained within a single Kuhn statistical segment?",
                "solution": """### Step 1: Degree of Polymerization, Bonds $n$, and Contour Length $L_c$
Monomer molecular weight of styrene ($\\text{C}_8\\text{H}_8$):
\\[
M_0 = 8(12.011) + 8(1.008) = 96.088 + 8.064 = 104.15\\text{ g/mol}
\\]
The degree of polymerization is:
\\[
X = \\frac{M_w}{M_0} = \\frac{208,300\\text{ g/mol}}{104.15\\text{ g/mol}} = 2,000
\\]
Since each vinyl unit contributes $2$ backbone C-C bonds:
\\[
n = 2 X = 2 \\times 2,000 = 4,000\\text{ bonds}
\\]
The all-$trans$ projected length per bond is $l \\sin(109.5^\\circ/2) = 0.154 \\times 0.81649 = 0.12574\\text{ nm}$.
The contour length is:
\\[
L_c = n \\, l \\, \\sin(54.75^\\circ) = 4,000 \\times 0.12574\\text{ nm} = 502.96\\text{ nm}
\\]

### Step 2: Kuhn Segment Length $b$ and Number $N_K$
Equating the contour length and unperturbed mean-square dimension:
\\[
L_c = N_K \\, b
\\]
\\[
\\langle R^2 \\rangle_0 = N_K \\, b^2
\\]
Dividing the second equation by the first:
\\[
b = \\frac{\\langle R^2 \\rangle_0}{L_c} = \\frac{(38.2\\text{ nm})^2}{502.96\\text{ nm}} = \\frac{1459.24\\text{ nm}^2}{502.96\\text{ nm}} = 2.901\\text{ nm}
\\]
The number of Kuhn statistical segments is:
\\[
N_K = \\frac{L_c}{b} = \\frac{502.96\\text{ nm}}{2.901\\text{ nm}} = 173.37 \\approx 173.4
\\]

### Step 3: Flory Characteristic Ratio $C_\\infty$
From the definition:
\\[
C_\\infty = \\frac{\\langle R^2 \\rangle_0}{n \\, l^2} = \\frac{1459.24\\text{ nm}^2}{4,000 \\times (0.154\\text{ nm})^2} = \\frac{1459.24}{4,000 \\times 0.023716} = \\frac{1459.24}{94.864} = 15.38
\\]

### Step 4: Repeat Units per Kuhn Segment
The contour length contributed per repeat unit is $2 \\times 0.12574 = 0.2515\\text{ nm}$.
The number of monomer repeat units per Kuhn segment is:
\\[
X_K = \\frac{b}{0.2515\\text{ nm}} = \\frac{2.901\\text{ nm}}{0.2515\\text{ nm}} = 11.53\\text{ repeat units}
\\]
Equivalently:
\\[
X_K = \\frac{X}{N_K} = \\frac{2,000}{173.37} = 11.54\\text{ units}
\\]
Due to the large steric bulk of the pendant phenyl rings, polystyrene requires approximately $11.5$ monomer units ($23$ C-C bonds) before orientational memory of the chain trajectory is lost.""",
                "answer": "(a) n = 4,000, Lc = 502.96 nm; (b) b = 2.901 nm, N_K = 173.4; (c) C_infinity = 15.38; (d) X_K = 11.54 repeat units per Kuhn segment."
            },
            {
                "id": "prob-1-5",
                "difficulty": "advanced",
                "title": "Rigorous Proof of the Debye-Kramers Theorem: <Rg^2> = <R^2> / 6",
                "statement": "Derive the fundamental Debye-Kramers relation $\\langle R_g^2 \\rangle_0 = \\frac{1}{6}\\langle R^2 \\rangle_0$ for an unperturbed linear Gaussian polymer chain starting from the pairwise segment separation identity:\n\\[\nR_g^2 = \\frac{1}{2 N^2} \\sum_{i=1}^N \\sum_{j=1}^N |\\mathbf{r}_i - \\mathbf{r}_j|^2\n\\]\nwhere the subchain between segments $i$ and $j$ obeys Gaussian random flight statistics: $\\langle |\\mathbf{r}_i - \\mathbf{r}_j|^2 \\rangle = |i - j| b^2$.",
                "solution": """### Step 1: Statistical Expectation Value
Taking the ensemble expectation value of the pairwise distance formula:
\\[
\\langle R_g^2 \\rangle_0 = \\frac{1}{2 N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\langle |\\mathbf{r}_i - \\mathbf{r}_j|^2 \\rangle
\\]
For a Gaussian chain, the mean-square distance between any two segments $i$ and $j$ depends solely on the contour distance $|i - j|$ separating them:
\\[
\\langle |\\mathbf{r}_i - \\mathbf{r}_j|^2 \\rangle = |i - j| b^2
\\]
Substituting this relation:
\\[
\\langle R_g^2 \\rangle_0 = \\frac{b^2}{2 N^2} \\sum_{i=1}^N \\sum_{j=1}^N |i - j|
\\]

### Step 2: Evaluating the Double Summation
By symmetry across the diagonal $i = j$:
\\[
\\sum_{i=1}^N \\sum_{j=1}^N |i - j| = 2 \\sum_{i=1}^N \\sum_{j=1}^{i} (i - j)
\\]
Let $k = i - j$. For a fixed $i$, as $j$ runs from $1$ to $i$, $k$ runs from $0$ to $i - 1$:
\\[
\\sum_{j=1}^i (i - j) = \\sum_{k=0}^{i-1} k = \\frac{(i - 1)i}{2} = \\frac{i^2 - i}{2}
\\]
Now sum over $i$ from $1$ to $N$:
\\[
\\sum_{i=1}^N \\sum_{j=1}^N |i - j| = 2 \\sum_{i=1}^N \\frac{i^2 - i}{2} = \\sum_{i=1}^N i^2 - \\sum_{i=1}^N i
\\]
Using standard summation formulas:
\\[
\\sum_{i=1}^N i = \\frac{N(N + 1)}{2}, \\quad \\sum_{i=1}^N i^2 = \\frac{N(N + 1)(2N + 1)}{6}
\\]
Substituting:
\\[
\\sum_{i=1}^N i^2 - \\sum_{i=1}^N i = \\frac{N(N + 1)(2N + 1)}{6} - \\frac{3N(N + 1)}{6} = \\frac{N(N + 1)(2N - 2)}{6} = \\frac{N(N^2 - 1)}{3}
\\]

### Step 3: Long Chain Limit ($N \\gg 1$)
Substituting this sum into $\\langle R_g^2 \\rangle_0$:
\\[
\\langle R_g^2 \\rangle_0 = \\frac{b^2}{2 N^2} \\left[ \\frac{N(N^2 - 1)}{3} \\right] = \\frac{b^2 (N^2 - 1)}{6 N}
\\]
For high molecular weight polymers where $N \\gg 1$, $N^2 - 1 \\approx N^2$:
\\[
\\langle R_g^2 \\rangle_0 = \\frac{N b^2}{6}
\\]
Since the unperturbed mean-square end-to-end distance is $\\langle R^2 \\rangle_0 = N b^2$:
\\[
\\langle R_g^2 \\rangle_0 = \\frac{1}{6} \\langle R^2 \\rangle_0
\\]
This concludes the rigorous proof.""",
                "answer": "Proved: <Rg^2>_0 = (b^2 / 2N^2) * [N(N^2 - 1)/3] -> (1/6) N b^2 = (1/6) <R^2>_0 as N >> 1."
            },
            {
                "id": "prob-1-6",
                "difficulty": "advanced",
                "title": "Kratky-Porod Wormlike Chain Elasticity of Double-Stranded DNA",
                "statement": "A viral double-stranded DNA molecule has contour length $L = 16.32\\text{ }\\mu\\text{m}$ ($48,000\\text{ base pairs}$, with axial rise per base pair $\\Delta h = 0.34\\text{ nm}$). The experimental persistence length in physiological buffer is $l_p = 50.0\\text{ nm}$.\n(a) Calculate the ratio $L / l_p$ and determine whether the DNA behaves as a rigid rod, semi-flexible filament, or Gaussian coil.\n(b) Calculate the root-mean-square end-to-end distance $\\sqrt{\\langle R^2 \\rangle}$ using the exact Kratky-Porod wormlike chain formula.\n(c) Compute the percentage error incurred if the DNA were approximated as an ideal Gaussian coil ($\\sqrt{\\langle R^2 \\rangle_{\\text{Gaussian}}} = \\sqrt{2 l_p L}$).\n(d) Calculate the effective Kuhn segment length $b$ and number of Kuhn segments $N_K$.",
                "solution": """### Step 1: Ratio $L / l_p$ and Regime Identification
\\[
L = 16.32\\text{ }\\mu\\text{m} = 16,320\\text{ nm}
\\]
\\[
\\frac{L}{l_p} = \\frac{16,320\\text{ nm}}{50.0\\text{ nm}} = 326.4
\\]
Since $L / l_p \\gg 1$, the macroscopic contour length far exceeds the persistence length. Over the entire molecule, dsDNA exhibits the global conformational properties of a flexible random coil with local bending rigidity.

### Step 2: Kratky-Porod Calculation
The exact Kratky-Porod equation is:
\\[
\\langle R^2 \\rangle_{\\text{WLC}} = 2 l_p L \\left[ 1 - \\frac{l_p}{L} \\left( 1 - \\exp\\left(-\\frac{L}{l_p}\\right) \\right) \\right]
\\]
Calculate the leading factor:
\\[
2 l_p L = 2(50.0\\text{ nm})(16,320\\text{ nm}) = 1,632,000\\text{ nm}^2
\\]
Calculate the correction term:
\\[
\\frac{l_p}{L} = \\frac{1}{326.4} = 3.0637 \\times 10^{-3}
\\]
Since $\\exp(-326.4) \\approx 0$:
\\[
1 - \\frac{l_p}{L}(1 - 0) = 1 - 0.003064 = 0.996936
\\]
Therefore:
\\[
\\langle R^2 \\rangle_{\\text{WLC}} = 1,632,000 \\times 0.996936 = 1,627,000\\text{ nm}^2
\\]
Taking the square root:
\\[
\\sqrt{\\langle R^2 \\rangle_{\\text{WLC}}} = \\sqrt{1,627,000} = 1,275.54\\text{ nm} = 1.276\\text{ }\\mu\\text{m}
\\]

### Step 3: Comparison with Ideal Gaussian Coil
The asymptotic Gaussian coil approximation is:
\\[
\\sqrt{\\langle R^2 \\rangle_{\\text{Gaussian}}} = \\sqrt{2 l_p L} = \\sqrt{1,632,000\\text{ nm}^2} = 1,277.50\\text{ nm}
\\]
The percentage error is:
\\[
\\text{Error} = \\frac{1,277.50 - 1,275.54}{1,275.54} \\times 100\\% = \\frac{1.96}{1,275.54} \\times 100\\% = +0.154\\%
\\]
At $L / l_p = 326.4$, the Gaussian approximation is accurate to within $0.15\\%$.

### Step 4: Kuhn Parameters
For a wormlike chain, the Kuhn segment length is:
\\[
b = 2 l_p = 2(50.0\\text{ nm}) = 100.0\\text{ nm}
\\]
The number of Kuhn statistical segments is:
\\[
N_K = \\frac{L}{b} = \\frac{16,320\\text{ nm}}{100.0\\text{ nm}} = 163.2\\text{ segments}
\\]""",
                "answer": "(a) L / l_p = 326.4 (flexible random coil regime); (b) <R^2>_WLC^(1/2) = 1,275.5 nm (1.276 µm); (c) Error of Gaussian approximation = +0.154%; (d) b = 100.0 nm, N_K = 163.2."
            },
            {
                "id": "prob-1-7",
                "difficulty": "challenge",
                "title": "Hildebrand Solubility Parameter & Cohesive Energy Density of PMMA",
                "statement": "The cohesive energy density of poly(methyl methacrylate) (PMMA, repeat unit $-\\text{CH}_2-\\text{C}(\\text{CH}_3)(\\text{COOCH}_3)-$) can be calculated using Small's molar attraction constants ($G_i$):\n- $-\\text{CH}_2-$: $G = 272\\text{ J}^{1/2}\\text{cm}^{3/2}\\text{/mol}$\n- $->\\text{C}<$ (quaternary carbon): $G = -190\\text{ J}^{1/2}\\text{cm}^{3/2}\\text{/mol}$\n- $-\\text{CH}_3$: $G = 438\\text{ J}^{1/2}\\text{cm}^{3/2}\\text{/mol}$\n- $-\\text{COO}-$ (ester group): $G = 634\\text{ J}^{1/2}\\text{cm}^{3/2}\\text{/mol}$\nThe bulk density of amorphous PMMA at $25^\\circ\\text{C}$ is $\\rho = 1.188\\text{ g/cm}^3$.\n(a) Calculate the repeat unit molecular weight $M_0$ and the molar volume $V_m$.\n(b) Calculate the total molar attraction constant $\\sum G_i$ per repeat unit.\n(c) Calculate the Hildebrand solubility parameter $\\delta$ and cohesive energy density (CED) in SI units ($\\text{MPa}^{1/2}$ and $\\text{J/cm}^3$).\n(d) Predict whether PMMA will dissolve in toluene ($\\delta = 18.2\\text{ MPa}^{1/2}$) and methanol ($\\delta = 29.7\\text{ MPa}^{1/2}$).",
                "solution": """### Step 1: Repeat Unit Mass and Molar Volume
The repeat unit is $\\text{C}_5\\text{H}_8\\text{O}_2$:
\\[
M_0 = 5(12.011) + 8(1.008) + 2(15.999) = 60.055 + 8.064 + 31.998 = 100.117\\text{ g/mol}
\\]
Given density $\\rho = 1.188\\text{ g/cm}^3$:
\\[
V_m = \\frac{M_0}{\\rho} = \\frac{100.117\\text{ g/mol}}{1.188\\text{ g/cm}^3} = 84.274\\text{ cm}^3\\text{/mol} = 8.4274 \\times 10^{-5}\\text{ m}^3\\text{/mol}
\\]

### Step 2: Sum of Molar Attraction Constants $\\sum G_i$
Decomposing the repeat unit into its constituent functional groups:
- One $-\\text{CH}_2-$: $1 \\times 272 = 272$
- One $->\\text{C}<$: $1 \\times (-190) = -190$
- Two $-\\text{CH}_3$ (one $\\alpha$-methyl, one ester methyl): $2 \\times 438 = 876$
- One $-\\text{COO}-$: $1 \\times 634 = 634$
Summing all contributions:
\\[
\\sum G_i = 272 - 190 + 876 + 634 = 1592\\text{ J}^{1/2}\\text{cm}^{3/2}\\text{/mol}
\\]

### Step 3: Hildebrand Parameter and Cohesive Energy Density
According to Small's formula:
\\[
\\delta = \\frac{\\sum G_i}{V_m} = \\frac{1592\\text{ J}^{1/2}\\text{cm}^{3/2}\\text{/mol}}{84.274\\text{ cm}^3\\text{/mol}} = 18.89\\text{ J}^{1/2}\\text{/cm}^{3/2}
\\]
Converting to standard SI units:
Since $1\\text{ J/cm}^3 = 10^6\\text{ J/m}^3 = 1\\text{ MPa}$, then $1\\text{ J}^{1/2}\\text{/cm}^{3/2} = 1\\text{ MPa}^{1/2}$:
\\[
\\delta = 18.89\\text{ MPa}^{1/2}
\\]
The cohesive energy density is:
\\[
\\text{CED} = \\delta^2 = (18.89\\text{ MPa}^{1/2})^2 = 356.8\\text{ MPa} = 356.8\\text{ J/cm}^3
\\]

### Step 4: Solubility Predictions
For solubility in non-polar/moderately polar solvents, the criterion is $|\\delta_{\\text{polymer}} - \\delta_{\\text{solvent}}| \\le 1.8 - 2.0\\text{ MPa}^{1/2}$:
- For toluene ($\\delta = 18.2\\text{ MPa}^{1/2}$):
\\[
|\\delta_{\\text{PMMA}} - \\delta_{\\text{toluene}}| = |18.89 - 18.2| = 0.69\\text{ MPa}^{1/2}
\\]
Since $0.69 < 1.8\\text{ MPa}^{1/2}$, PMMA is highly soluble in toluene (confirmed experimentally; toluene is an excellent solvent for PMMA).
- For methanol ($\\delta = 29.7\\text{ MPa}^{1/2}$):
\\[
|\\delta_{\\text{PMMA}} - \\delta_{\\text{methanol}}| = |18.89 - 29.7| = 10.81\\text{ MPa}^{1/2}
\\]
Because $10.81 \\gg 2.0\\text{ MPa}^{1/2}$, the enthalpy of mixing is massively endothermic. PMMA is completely insoluble in methanol (methanol is routinely used as a non-solvent to precipitate PMMA from toluene solutions).""",
                "answer": "(a) M_0 = 100.12 g/mol, V_m = 84.27 cm^3/mol; (b) sum(G_i) = 1592 J^(1/2) cm^(3/2) / mol; (c) delta = 18.89 MPa^(1/2), CED = 356.8 J/cm^3; (d) Soluble in toluene (|delta_diff| = 0.69 MPa^(1/2)), insoluble in methanol (|delta_diff| = 10.81 MPa^(1/2))."
            },
            {
                "id": "prob-1-8",
                "difficulty": "challenge",
                "title": "Hansen 3D Solubility Sphere Analysis for Poly(vinyl chloride)",
                "statement": "The Hansen 3D solubility parameters for poly(vinyl chloride) (PVC) are $\\delta_d = 18.2\\text{ MPa}^{1/2}$, $\\delta_p = 7.5\\text{ MPa}^{1/2}$, and $\\delta_h = 8.3\\text{ MPa}^{1/2}$, with an interaction radius of $R_0 = 3.5\\text{ MPa}^{1/2}$.\nGiven the Hansen parameters for three test solvents:\n1. Tetrahydrofuran (THF): $\\delta_d = 16.8, \\delta_p = 5.7, \\delta_h = 8.0\\text{ MPa}^{1/2}$\n2. Acetone: $\\delta_d = 15.5, \\delta_p = 10.4, \\delta_h = 7.0\\text{ MPa}^{1/2}$\n3. Cyclohexane: $\\delta_d = 16.8, \\delta_p = 0.0, \\delta_h = 0.2\\text{ MPa}^{1/2}$\n(a) Calculate the Hansen distance $R_a$ and the Relative Energy Difference (RED) for each solvent.\n(b) Predict the dissolution behavior of PVC in each solvent.",
                "solution": """### Step 1: Hansen Distance Formula
The distance $R_a$ between polymer (2) and solvent (1) in Hansen space is:
\\[
R_a = \\sqrt{4(\\delta_{d1} - \\delta_{d2})^2 + (\\delta_{p1} - \\delta_{p2})^2 + (\\delta_{h1} - \\delta_{h2})^2}
\\]
The Relative Energy Difference is:
\\[
\\text{RED} = \\frac{R_a}{R_0}
\\]

### Step 2: Evaluating Tetrahydrofuran (THF)
\\[
\\Delta \\delta_d = 16.8 - 18.2 = -1.4\\text{ MPa}^{1/2} \\implies 4(-1.4)^2 = 4(1.96) = 7.84
\\]
\\[
\\Delta \\delta_p = 5.7 - 7.5 = -1.8\\text{ MPa}^{1/2} \\implies (-1.8)^2 = 3.24
\\]
\\[
\\Delta \\delta_h = 8.0 - 8.3 = -0.3\\text{ MPa}^{1/2} \\implies (-0.3)^2 = 0.09
\\]
Sum of squares:
\\[
R_a^2 = 7.84 + 3.24 + 0.09 = 11.17
\\]
\\[
R_a = \\sqrt{11.17} = 3.342\\text{ MPa}^{1/2}
\\]
\\[
\\text{RED}_{\\text{THF}} = \\frac{3.342}{3.5} = 0.955
\\]

### Step 3: Evaluating Acetone
\\[
\\Delta \\delta_d = 15.5 - 18.2 = -2.7\\text{ MPa}^{1/2} \\implies 4(-2.7)^2 = 4(7.29) = 29.16
\\]
\\[
\\Delta \\delta_p = 10.4 - 7.5 = +2.9\\text{ MPa}^{1/2} \\implies (2.9)^2 = 8.41
\\]
\\[
\\Delta \\delta_h = 7.0 - 8.3 = -1.3\\text{ MPa}^{1/2} \\implies (-1.3)^2 = 1.69
\\]
Sum of squares:
\\[
R_a^2 = 29.16 + 8.41 + 1.69 = 39.26
\\]
\\[
R_a = \\sqrt{39.26} = 6.266\\text{ MPa}^{1/2}
\\]
\\[
\\text{RED}_{\\text{Acetone}} = \\frac{6.266}{3.5} = 1.790
\\]

### Step 4: Evaluating Cyclohexane
\\[
\\Delta \\delta_d = 16.8 - 18.2 = -1.4\\text{ MPa}^{1/2} \\implies 4(-1.4)^2 = 7.84
\\]
\\[
\\Delta \\delta_p = 0.0 - 7.5 = -7.5\\text{ MPa}^{1/2} \\implies (-7.5)^2 = 56.25
\\]
\\[
\\Delta \\delta_h = 0.2 - 8.3 = -8.1\\text{ MPa}^{1/2} \\implies (-8.1)^2 = 65.61
\\]
Sum of squares:
\\[
R_a^2 = 7.84 + 56.25 + 65.61 = 129.70
\\]
\\[
R_a = \\sqrt{129.70} = 11.389\\text{ MPa}^{1/2}
\\]
\\[
\\text{RED}_{\\text{Cyclohexane}} = \\frac{11.389}{3.5} = 3.254
\\]

### Step 5: Thermodynamic Solubility Predictions
1. **THF**: $\\text{RED} = 0.955 < 1$. Lies inside the Hansen solubility sphere. Spontaneous complete dissolution occurs (THF is the industry standard solvent for PVC).
2. **Acetone**: $\\text{RED} = 1.790 > 1$. Lies outside the solubility sphere. PVC swells moderately but does not form a true homogeneous solution at ambient temperatures.
3. **Cyclohexane**: $\\text{RED} = 3.254 \\gg 1$. Lies far outside the sphere due to total absence of polar and hydrogen-bonding interactions. Completely non-solvent (causes rapid precipitation).""",
                "answer": "(a) THF: R_a = 3.34 MPa^(1/2), RED = 0.955; Acetone: R_a = 6.27 MPa^(1/2), RED = 1.790; Cyclohexane: R_a = 11.39 MPa^(1/2), RED = 3.254; (b) THF is a good solvent; Acetone is a non-solvent/swelling agent; Cyclohexane is a strong non-solvent."
            },
            {
                "id": "prob-1-9",
                "difficulty": "challenge",
                "title": "Conformational Contraction Factor g of a Symmetrical Star Polymer",
                "statement": "Derive the exact Zimm-Stockmayer branching contraction factor $g = \\frac{3f - 2}{f^2}$ for a symmetrical star polymer consisting of $f$ identical, unperturbed Gaussian arms radiating from a central branch point, each arm containing $N_{\\text{arm}} = N/f$ Kuhn segments of length $b$. Verify the derivation numerically for $f = 3, 4, 6$ arms.",
                "solution": """### Step 1: Definition of the Radius of Gyration for a Star Topology
Let the star polymer have $f$ arms attached at the central branch point located at the origin $\\mathbf{0}$.
Let segment $i$ on arm $\\alpha$ have position vector $\\mathbf{r}_{\\alpha, i}$ (where $\\alpha \\in \\{1, 2, \\dots, f\\}$ and $i \\in \\{1, 2, \\dots, M\\}$, with $M = N/f$).
The center of mass vector is:
\\[
\\mathbf{R}_{\\text{cm}} = \\frac{1}{N} \\sum_{\\alpha=1}^f \\sum_{i=1}^M \\mathbf{r}_{\\alpha, i}
\\]
The mean-square radius of gyration is:
\\[
\\langle R_g^2 \\rangle_{\\text{star}} = \\frac{1}{N} \\sum_{\\alpha=1}^f \\sum_{i=1}^M \\langle |\\mathbf{r}_{\\alpha, i} - \\mathbf{R}_{\\text{cm}}|^2 \\rangle = \\frac{1}{N} \\sum_{\\alpha=1}^f \\sum_{i=1}^M \\langle \\mathbf{r}_{\\alpha, i}^2 \\rangle - \\langle \\mathbf{R}_{\\text{cm}}^2 \\rangle
\\]

### Step 2: Mean-Square Distance from Branch Point
For an unperturbed Gaussian arm, segment $i$ undergoes random flight from the branch point $\\mathbf{0}$:
\\[
\\langle \\mathbf{r}_{\\alpha, i}^2 \\rangle = i \\, b^2
\\]
Summing over all $M$ segments and all $f$ arms:
\\[
\\sum_{\\alpha=1}^f \\sum_{i=1}^M \\langle \\mathbf{r}_{\\alpha, i}^2 \\rangle = f \\sum_{i=1}^M i \\, b^2 = f b^2 \\frac{M(M + 1)}{2} \\approx \\frac{f M^2 b^2}{2} = \\frac{N M b^2}{2} = \\frac{N^2 b^2}{2f}
\\]
Dividing by $N$:
\\[
\\frac{1}{N} \\sum_{\\alpha=1}^f \\sum_{i=1}^M \\langle \\mathbf{r}_{\\alpha, i}^2 \\rangle = \\frac{M b^2}{2} = \\frac{N b^2}{2f}
\\]

### Step 3: Mean-Square Center of Mass Motion
\\[
\\langle \\mathbf{R}_{\\text{cm}}^2 \\rangle = \\frac{1}{N^2} \\left\\langle \\left(\\sum_{\\alpha=1}^f \\sum_{i=1}^M \\mathbf{r}_{\\alpha, i}\\right) \\cdot \\left(\\sum_{\\beta=1}^f \\sum_{j=1}^M \\mathbf{r}_{\\beta, j}\\right) \\right\\rangle
\\]
Because different arms $\\alpha \\neq \\beta$ are statistically independent outside the branch point, $\\langle \\mathbf{r}_{\\alpha, i} \\cdot \\mathbf{r}_{\\beta, j} \\rangle = 0$ for $\\alpha \\neq \\beta$.
Thus:
\\[
\\langle \\mathbf{R}_{\\text{cm}}^2 \\rangle = \\frac{1}{N^2} \\sum_{\\alpha=1}^f \\sum_{i=1}^M \\sum_{j=1}^M \\langle \\mathbf{r}_{\\alpha, i} \\cdot \\mathbf{r}_{\\alpha, j} \\rangle
\\]
For two segments on the same arm $\\alpha$, $\\langle \\mathbf{r}_{\\alpha, i} \\cdot \\mathbf{r}_{\\alpha, j} \\rangle = \\min(i, j) b^2$:
\\[
\\sum_{i=1}^M \\sum_{j=1}^M \\min(i, j) = 2 \\sum_{i=1}^M \\sum_{j=1}^i j - \\sum_{i=1}^M i = 2 \\sum_{i=1}^M \\frac{i(i+1)}{2} - \\frac{M(M+1)}{2} \\approx \\frac{M^3}{3}
\\]
Summing over all $f$ arms:
\\[
\\langle \\mathbf{R}_{\\text{cm}}^2 \\rangle = \\frac{f}{N^2} \\left( \\frac{M^3 b^2}{3} \\right) = \\frac{f (N/f)^3 b^2}{3 N^2} = \\frac{N b^2}{3 f^2}
\\]

### Step 4: Branching Factor $g$
Subtracting the two terms:
\\[
\\langle R_g^2 \\rangle_{\\text{star}} = \\frac{N b^2}{2f} - \\frac{N b^2}{3f^2} = N b^2 \\left( \\frac{3f - 2}{6 f^2} \\right)
\\]
For a linear polymer of identical total segment number $N$:
\\[
\\langle R_g^2 \\rangle_{\\text{linear}} = \\frac{N b^2}{6}
\\]
Taking the ratio:
\\[
g = \\frac{\\langle R_g^2 \\rangle_{\\text{star}}}{\\langle R_g^2 \\rangle_{\\text{linear}}} = \\frac{N b^2 (3f - 2) / (6 f^2)}{N b^2 / 6} = \\frac{3f - 2}{f^2}
\\]

### Step 5: Numerical Verification
- For $f = 1$ (linear chain): $g = (3(1) - 2) / 1^2 = 1.000$ (exact unity).
- For $f = 2$ (linear chain divided at midpoint): $g = (6 - 2) / 4 = 4/4 = 1.000$.
- For $f = 3$: $g = (9 - 2) / 9 = 7/9 \\approx 0.7778$ ($22.2\\%$ reduction in coil size).
- For $f = 4$: $g = (12 - 2) / 16 = 10/16 = 5/8 = 0.6250$ ($37.5\\%$ reduction in coil size).
- For $f = 6$: $g = (18 - 2) / 36 = 16/36 = 4/9 \\approx 0.4444$ ($55.6\\%$ reduction in coil size).""",
                "answer": "Derived: g = (3f - 2) / f^2. Numerical values: g(f=3) = 7/9 = 0.7778; g(f=4) = 5/8 = 0.6250; g(f=6) = 4/9 = 0.4444."
            }
        ]
    }
    units.append(u1)

    # =========================================================================
    # UNIT 2: Polymer Solutions, Solvent Quality & Flory-Huggins Lattice Thermodynamics
    # =========================================================================
    u2 = {
        "id": "unit-2",
        "number": 2,
        "title": "Polymer Solutions, Solvent Quality & Flory-Huggins Lattice Thermodynamics",
        "leadSummary": "Thermodynamics of macromolecular dissolution, combinatorial entropy of mixing on coordination lattices, Flory-Huggins interaction parameter chi, free energy of mixing, chemical potentials, osmotic pressure virial expansions, binodal and spinodal phase coexistence curves, critical solution temperatures (UCST and LCST), and analytical solubility fractionation mechanics.",
        "simulations": ["sim_poly_flory_huggins_phase_diagram"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Thermodynamic Criteria for Polymer Dissolution & Phase Stability",
                "content": """The dissolution of a high molecular weight polymer in a low molecular weight solvent is governed by the fundamental laws of chemical thermodynamics. Spontaneous mixing at constant temperature $T$ and pressure $P$ requires that the Gibbs free energy of mixing be negative:
\\[
\\Delta G_m = \\Delta H_m - T \\Delta S_m < 0
\\]
However, a negative $\\Delta G_m$ is merely a necessary condition for dissolution; it is not sufficient to guarantee complete, single-phase thermodynamic stability across all concentrations.

### Thermodynamic Criteria for Phase Stability
For a binary mixture to remain permanently homogeneous without spontaneous phase separation into two liquid phases (liquid-liquid demixing), the free energy of mixing curve must be strictly concave upward (positive second derivative with respect to composition) across the entire composition range:
\\[
\\left( \\frac{\\partial^2 \\Delta G_m}{\\partial \\phi_2^2} \\right)_{T, P} > 0
\\]
where $\\phi_2$ is the volume fraction of the polymer.
If there exists an intermediate composition interval where the curvature is negative:
\\[
\\left( \\frac{\\partial^2 \\Delta G_m}{\\partial \\phi_2^2} \\right)_{T, P} < 0
\\]
the homogeneous solution is intrinsically thermodynamically unstable against spontaneous infinitesimal composition fluctuations, triggering spontaneous phase separation via **spinodal decomposition**.

### The Fundamental Challenge of Macromolecular Mixing
In simple low molecular weight binary liquids (e.g., benzene + toluene), the combinatorial entropy of mixing $\\Delta S_m$ is large and positive, driving spontaneous dissolution even when mixing is moderately endothermic ($\\Delta H_m > 0$).
In polymers, however, connecting $N$ monomer segments together into an unbroken covalent chain severely restricts their translational freedom. When $N$ independent solvent molecules are replaced by one $N$-mer chain, the translational combinatorial entropy of mixing per unit volume is reduced by a factor of nearly $1/N \\sim 10^{-3} - 10^{-5}$.
Because $T \\Delta S_m$ is exceptionally small, **polymer dissolution is dominated by the enthalpy of mixing $\\Delta H_m$**. Even a very modest endothermic interaction energy per segment ($k_B T \\chi$) is sufficient to overcome the tiny combinatorial entropy, driving macroscopic phase separation."""
            },
            {
                "secNumber": "2.2",
                "title": "The Flory-Huggins Lattice Model: Combinatorial Entropy of Mixing",
                "content": """Formulated independently by Paul Flory and Maurice Huggins in 1941–1942, the **Flory-Huggins lattice theory** revolutionized polymer thermodynamics by calculating the combinatorial entropy of placing flexible polymer chains onto a regular lattice.

### The Lattice Geometry
Consider a lattice with total volume $V$ divided into $N_0$ identical spatial cells each of volume $v_0$ (equal to the volume of a single solvent molecule). The lattice has coordination number $z$ (number of nearest-neighbor cells adjacent to any site).
The binary solution consists of:
- $n_1$ solvent molecules, each occupying $1$ cell ($r_1 = 1$).
- $n_2$ polymer chains, each consisting of $x$ connected segments each occupying $1$ cell ($r_2 = x$).
The total number of lattice cells is:
\\[
N_0 = n_1 + x n_2
\\]
The volume fractions of solvent ($\\phi_1$) and polymer ($\\phi_2$) are:
\\[
\\phi_1 = \\frac{n_1}{n_1 + x n_2} = \\frac{n_1}{N_0}, \\quad \\phi_2 = \\frac{x n_2}{n_1 + x n_2} = \\frac{x n_2}{N_0}
\\]

### Sequential Placement & Number of Microstates $\\Omega$
To calculate the total number of distinguishable configurations $\\Omega$, Flory calculated the number of ways $\\nu_{i+1}$ to insert the $(i+1)$-th polymer chain into the lattice when $i$ chains already occupy $i x$ cells:
\\[
\\Omega = \\frac{1}{n_2!} \\prod_{i=0}^{n_2 - 1} \\nu_{i+1}
\\]
For the $(i+1)$-th chain:
- The first segment has $N_0 - i x$ empty cells available.
- The second segment must occupy one of the $z$ adjacent cells, with probability of finding an empty cell given by the mean vacancy fraction $f_i = (N_0 - i x) / N_0$.
- The third and subsequent segments have $(z - 1)$ directional options, each with probability $f_i$.
Multiplying these factors and applying Stirling's approximation ($\\ln n! \\approx n \\ln n - n$) yields the celebrated **Flory-Huggins combinatorial entropy of mixing**:
\\[
\\Delta S_m = -k_B \\left( n_1 \\ln \\phi_1 + n_2 \\ln \\phi_2 \\right)
\\]
In molar units (where $N_A k_B = R$):
\\[
\\frac{\\Delta S_m}{R} = -\\left( n_1 \\ln \\phi_1 + n_2 \\ln \\phi_2 \\right)
\\]
For monomeric liquid mixtures ($x = 1$), $\\phi_1 = X_1$ and $\\phi_2 = X_2$, recovering ideal Raoult's law mixing. When $x \\gg 1$, the $n_2 \\ln \\phi_2$ term is heavily suppressed relative to $n_1 \\ln \\phi_1$, formalizing the dramatic loss of combinatorial entropy."""
            },
            {
                "secNumber": "2.3",
                "title": "Enthalpy of Mixing & The Flory-Huggins Interaction Parameter chi",
                "content": """The energetic change accompanying mixing is modeled through a mean-field Bragg-Williams nearest-neighbor contact exchange mechanism.

### Nearest-Neighbor Contact Exchange Energetics
Prior to mixing:
- Pure solvent contains only $1-1$ molecular contacts with contact energy $w_{11}$.
- Pure polymer contains only $2-2$ segment contacts with contact energy $w_{22}$.
Upon mixing, new $1-2$ contacts are created at the expense of $1-1$ and $2-2$ contacts:
\\[
\\frac{1}{2} (1-1) + \\frac{1}{2} (2-2) \\longrightarrow (1-2)
\\]
The energy change associated with forming a single solvent-segment contact pair is:
\\[
\\Delta w_{12} = w_{12} - \\frac{1}{2}(w_{11} + w_{22})
\\]

### Definition of the Interaction Parameter $\\chi$
The dimensionless **Flory-Huggins interaction parameter** $\\chi$ (or $\\chi_{12}$) is defined as the exchange energy $\\Delta w_{12}$ per solvent molecule scaled by thermal energy $k_B T$:
\\[
\\chi = \\frac{z \\Delta w_{12}}{k_B T}
\\]
where $z$ is the lattice coordination number.
In mean-field approximation, the average number of solvent-polymer contact pairs in the mixture is $z n_1 \\phi_2$. Therefore, the total enthalpy of mixing is:
\\[
\\Delta H_m = k_B T \\, \\chi \\, n_1 \\phi_2
\\]
In molar units:
\\[
\\Delta H_m = R T \\, \\chi \\, n_1 \\phi_2
\\]

### Physical Meaning and Temperature Dependence of $\\chi$
From regular solution theory and Hildebrand solubility parameters:
\\[
\\chi = \\frac{V_1}{R T} (\\delta_1 - \\delta_2)^2
\\]
where $V_1$ is the molar volume of the solvent.
In real polymer solutions, $\\chi$ is not purely enthalpic; it also contains an excess entropic contribution $\\chi_s$ arising from non-random packing, specific orientation constraints, and solvent local ordering:
\\[
\\chi = \\chi_s + \\frac{\\chi_h}{T} = \\chi_s + \\frac{B}{T}
\\]
Typical empirical values of $\\chi_s$ range from $0.2$ to $0.4$.
- $\\chi < 0$: Highly favorable exothermic mixing (strong specific interactions such as hydrogen bonding).
- $0 \\le \\chi < 0.5$: Athermal to moderately endothermic mixing in a **good solvent**.
- $\\chi = 0.5$: The exact **theta ($\\Theta$) state** where repulsive excluded volume is canceled by attractive interactions.
- $\\chi > 0.5$: **Poor solvent**; phase separation occurs above critical polymer concentrations."""
            },
            {
                "secNumber": "2.4",
                "title": "The Flory-Huggins Free Energy & Chemical Potentials",
                "content": """Combining the combinatorial entropy and the contact exchange enthalpy yields the complete **Flory-Huggins Free Energy of Mixing**:
\\[
\\Delta G_m = \\Delta H_m - T \\Delta S_m = R T \\left( n_1 \\ln \\phi_1 + n_2 \\ln \\phi_2 + \\chi n_1 \\phi_2 \\right)
\\]
Dividing by the total number of moles of lattice sites $N_0 = n_1 + x n_2$:
\\[
\\frac{\\Delta G_m}{N_0 R T} = \\phi_1 \\ln \\phi_1 + \\frac{\\phi_2}{x} \\ln \\phi_2 + \\chi \\phi_1 \\phi_2
\\]

### Solvent Chemical Potential $\\mu_1 - \\mu_1^\\circ$
The chemical potential of the solvent relative to pure solvent is obtained by differentiating $\\Delta G_m$ with respect to $n_1$ at constant $T, P, n_2$:
\\[
\\mu_1 - \\mu_1^\\circ = \\left( \\frac{\\partial \\Delta G_m}{\\partial n_1} \\right)_{T, P, n_2}
\\]
Applying the chain rule:
\\[
\\mu_1 - \\mu_1^\\circ = R T \\left[ \\ln(1 - \\phi_2) + \\left(1 - \\frac{1}{x}\\right)\\phi_2 + \\chi \\phi_2^2 \\right]
\\]

### Dilute Solution Series Expansion & Osmotic Pressure
In dilute polymer solutions ($\\phi_2 \\ll 1$), we expand $\\ln(1 - \\phi_2)$ in a Taylor series:
\\[
\\ln(1 - \\phi_2) = -\\phi_2 - \\frac{\\phi_2^2}{2} - \\frac{\\phi_2^3}{3} - \\dots
\\]
Substituting into the solvent chemical potential:
\\[
\\mu_1 - \\mu_1^\\circ = R T \\left[ -\\phi_2 - \\frac{\\phi_2^2}{2} + \\phi_2 - \\frac{\\phi_2}{x} + \\chi \\phi_2^2 - \\mathcal{O}(\\phi_2^3) \\right]
\\]
\\[
\\mu_1 - \\mu_1^\\circ = -R T \\left[ \\frac{\\phi_2}{x} + \\left(\\frac{1}{2} - \\chi\\right)\\phi_2^2 + \\frac{\\phi_2^3}{3} + \\dots \\right]
\\]
From classical thermodynamics, the osmotic pressure $\\Pi$ is related to solvent chemical potential by $\\Pi V_1 = -(\\mu_1 - \\mu_1^\\circ)$, where $V_1$ is the molar volume of the solvent:
\\[
\\Pi = \\frac{R T}{V_1} \\left[ \\frac{\\phi_2}{x} + \\left(\\frac{1}{2} - \\chi\\right)\\phi_2^2 + \\frac{\\phi_2^3}{3} + \\dots \\right]
\\]
Substituting the mass concentration $c = \\phi_2 / \\bar{v}$ (where $\\bar{v}$ is the polymer specific volume, so $V_1 / (x \\bar{v}) = M_2$):
\\[
\\frac{\\Pi}{c} = R T \\left[ \\frac{1}{M_2} + A_2 c + A_3 c^2 + \\dots \\right]
\\]
where the **second virial coefficient** $A_2$ is:
\\[
A_2 = \\frac{\\bar{v}^2}{V_1} \\left( \\frac{1}{2} - \\chi \\right)
\\]
- In a **good solvent** ($\\chi < 0.5$): $A_2 > 0$ (osmotic pressure exceeds ideal van 't Hoff value due to excluded volume repulsion).
- At the **theta temperature** ($\\chi = 0.5$): $A_2 = 0$ (ideal thermodynamic behavior; $\\Pi/c = R T / M_2$ across finite concentrations).
- In a **poor solvent** ($\\chi > 0.5$): $A_2 < 0$ (attractive interactions dominate, leading toward phase separation)."""
            },
            {
                "secNumber": "2.5",
                "title": "Phase Equilibria, Binodal & Spinodal Decomposition Curves",
                "content": """The phase behavior of polymer solutions as a function of temperature and composition is characterized by liquid-liquid phase separation envelopes.

### The Spinodal Condition
The boundary between metastable and intrinsically unstable thermodynamic states is the **spinodal curve**, defined by the vanishing second derivative of the free energy of mixing:
\\[
\\left( \\frac{\\partial^2 \\Delta G_m}{\\partial \\phi_2^2} \\right)_{T, P} = 0
\\]
Differentiating the Flory-Huggins free energy density $\\frac{\\Delta G_m}{N_0 R T} = (1 - \\phi_2)\\ln(1 - \\phi_2) + \\frac{\\phi_2}{x}\\ln \\phi_2 + \\chi(1 - \\phi_2)\\phi_2$:
First derivative:
\\[
\\frac{\\partial}{\\partial \\phi_2} \\left( \\frac{\\Delta G_m}{N_0 R T} \\right) = -\\ln(1 - \\phi_2) - 1 + \\frac{1}{x}\\ln \\phi_2 + \\frac{1}{x} + \\chi(1 - 2\\phi_2)
\\]
Second derivative:
\\[
\\frac{\\partial^2}{\\partial \\phi_2^2} \\left( \\frac{\\Delta G_m}{N_0 R T} \\right) = \\frac{1}{1 - \\phi_2} + \\frac{1}{x \\phi_2} - 2\\chi = 0
\\]
Solving for the interaction parameter $\\chi$ along the spinodal:
\\[
\\chi_{\\text{sp}}(\\phi_2) = \\frac{1}{2} \\left( \\frac{1}{1 - \\phi_2} + \\frac{1}{x \\phi_2} \\right)
\\]

### The Critical Point
The critical point occurs where the third derivative of the free energy also vanishes (the inflection point of the spinodal curve):
\\[
\\left( \\frac{\\partial^3 \\Delta G_m}{\\partial \\phi_2^3} \\right)_{T, P} = \\frac{1}{(1 - \\phi_2)^2} - \\frac{1}{x \\phi_2^2} = 0
\\]
Rearranging:
\\[
(1 - \\phi_2)^2 = x \\phi_2^2 \\implies 1 - \\phi_2 = \\sqrt{x} \\phi_2
\\]
Solving for the **critical polymer volume fraction** $\\phi_{2,c}$:
\\[
\\phi_{2,c} = \\frac{1}{1 + \\sqrt{x}}
\\]
For high polymers where $x \\gg 1$:
\\[
\\phi_{2,c} \\approx \\frac{1}{\\sqrt{x}} \\ll 1
\\]
Substituting $\\phi_{2,c}$ back into the spinodal equation yields the **critical interaction parameter** $\\chi_c$:
\\[
\\chi_c = \\frac{1}{2} \\left( \\frac{1}{1 - \\frac{1}{1+\\sqrt{x}}} + \\frac{1}{x \\frac{1}{1+\\sqrt{x}}} \\right) = \\frac{1}{2} \\left( \\frac{1+\\sqrt{x}}{\\sqrt{x}} + \\frac{1+\\sqrt{x}}{x} \\right) = \\frac{1}{2} \\left( 1 + \\frac{1}{\\sqrt{x}} \\right)^2
\\]
\\[
\\chi_c = \\frac{1}{2} + \\frac{1}{\\sqrt{x}} + \\frac{1}{2x}
\\]
In the limit of infinite molecular weight ($x \\to \\infty$):
\\[
\\lim_{x \\to \\infty} \\phi_{2,c} = 0, \\quad \\lim_{x \\to \\infty} \\chi_c = \\frac{1}{2}
\\]
This reveals a crucial hallmark of polymer thermodynamics: **the critical point is strongly asymmetric**, shifting to extremely dilute polymer concentrations ($\\phi_{2,c} \\to 0$).

### The Binodal (Coexistence) Curve
The true phase boundary is the **binodal curve**, defined by the equality of chemical potentials of each component in both coexisting phases ($'$ and $''$):
\\[
\\mu_1(\\phi_2') = \\mu_1(\\phi_2''), \\quad \\mu_2(\\phi_2') = \\mu_2(\\phi_2'')
\\]
Between the binodal and spinodal lies the **metastable nucleation-and-growth** regime. Inside the spinodal curve lies the **spontaneous spinodal decomposition** regime, characterized by interconnected bicontinuous morphologies."""
            },
            {
                "secNumber": "2.6",
                "title": "Solvent Quality, The Flory Theta Condition & Swelling Ratio",
                "content": """The physical conformation and dimensions of a macromolecule in solution depend intimately on the thermodynamic interaction between monomer segments and the solvent.

### The Three Thermodynamic Regimes of Solvent Quality
1. **Good Solvent ($\\chi < 0.5, A_2 > 0$)**:
   - Monomer-solvent contacts are energetically favored over monomer-monomer contacts.
   - The chain expands to maximize solvent contact, exhibiting repulsive **excluded volume**.
   - The coil dimension swells beyond unperturbed Gaussian dimensions, following Flory's self-avoiding walk scaling:
   \\[
   R_g \\sim N^{\\nu} \\quad \\text{with } \\nu = \\frac{3}{d + 2} = \\frac{3}{5} = 0.600
   \\]
   (Renormalization group theory yields $\\nu \\approx 0.588$).

2. **Theta ($\\Theta$) Solvent ($\\chi = 0.5, A_2 = 0$)**:
   - The thermodynamic temperature where the attractive segment-segment van der Waals interactions exactly balance the steric repulsive excluded volume.
   - The effective excluded volume parameter $v_{\\text{ex}}$ vanishes:
   \\[
   v_{\\text{ex}} = (1 - 2\\chi) v_0 = 0
   \\]
   - The polymer behaves as an ideal, non-interacting random walk (phantom chain):
   \\[
   R_g \\sim N^{1/2} = N^{0.500}
   \\]

3. **Poor Solvent ($\\chi > 0.5, A_2 < 0$)**:
   - Segment-segment attractive interactions dominate over solvent interactions.
   - The coil contracts below unperturbed dimensions into a dense, collapsed **globule**:
   \\[
   R_g \\sim N^{1/3}
   \\]
   - At temperatures below $\\Theta$, macroscopic phase separation into polymer-rich and polymer-poor phases occurs.

### The Linear Expansion Factor $\\alpha$
The swelling of a real polymer coil relative to its unperturbed theta state is quantified by the **linear expansion factor** $\\alpha$:
\\[
\\alpha = \\frac{\\sqrt{\\langle R^2 \\rangle}}{\\sqrt{\\langle R^2 \\rangle_0}} = \\frac{\\sqrt{\\langle R_g^2 \\rangle}}{\\sqrt{\\langle R_g^2 \\rangle_0}}
\\]
Flory derived the fundamental closed-form equation for chain expansion:
\\[
\\alpha^5 - \\alpha^3 = C_T \\left(1 - \\frac{\\Theta}{T}\\right) M^{1/2}
\\]
where $C_T$ is a molecular constant dependent on chain flexibility and molar volume.
- At $T = \\Theta$: $\\alpha = 1$ (unperturbed state).
- For $T > \\Theta$: $\\alpha > 1$ (swollen coil in good solvent).
- For $T < \\Theta$: $\\alpha < 1$ (contracted coil)."""
            },
            {
                "secNumber": "2.7",
                "title": "UCST vs LCST Phase Transitions & Temperature Dependence",
                "content": """Polymer-solvent systems exhibit two distinct types of liquid-liquid phase separation envelopes governed by temperature.

### Upper Critical Solution Temperature (UCST)
- The classical Flory-Huggins model with enthalpic interaction $\\chi \\propto 1/T$ predicts that raising the temperature decreases $\\chi$, increasing solvent quality and restoring single-phase homogeneity.
- Phase separation occurs upon **cooling below a critical temperature**, termed the **Upper Critical Solution Temperature (UCST)**:
\\[
T_c^{\\text{UCST}} = \\frac{\\Theta}{1 + \\frac{1}{\\sqrt{x}} + \\frac{1}{2x}}
\\]
- As molecular weight approaches infinity ($x \\to \\infty$), $T_c^{\\text{UCST}} \\to \\Theta$.
- Classical UCST systems: Polystyrene in cyclohexane ($\\Theta = 34.5^\\circ\\text{C}$), PMMA in 1-chlorobutane.

### Lower Critical Solution Temperature (LCST)
- Many polymer solutions, including water-soluble polymers (e.g., poly(N-isopropylacrylamide), PNIPAM; poly(ethylene oxide), PEO) and hydrocarbon solutions at elevated temperatures near the solvent vapor-liquid critical point, exhibit phase separation upon **heating**.
- The boundary temperature above which two phases appear is the **Lower Critical Solution Temperature (LCST)**.
- **Physical Mechanisms of LCST**:
  1. **Aqueous Systems (Hydrophobic Effect)**: Below the LCST, dissolution is driven by exothermic hydrogen bonding between water and polar groups, accompanied by rigid, highly ordered iceberg water cages surrounding non-polar moieties (negative excess entropy $\\Delta S^E < 0$). Upon heating, hydrogen bonds dissociate and the release of structured water cages provides a large entropic gain for phase separation ($T \\Delta S^E < 0$). For PNIPAM, the LCST occurs sharply at $32^\\circ\\text{C}$.
  2. **Non-Aqueous Systems (Free Volume Disparity)**: Near the boiling point of the solvent, the thermal expansion coefficient of the solvent liquid far exceeds that of the tethered polymer chain. This macroscopic **free volume mismatch** produces an unfavorable equation-of-state compressibility entropy penalty upon mixing, driving phase separation at high temperatures."""
            },
            {
                "secNumber": "2.8",
                "title": "Analytical Polymer Fractionation by Solubility & Coacervation",
                "content": """Because synthetic polymers are polydisperse (possessing a broad distribution of molecular weights), the strong dependence of the critical interaction parameter $\\chi_c$ and binodal coexistence curve on chain length $x$ provides the fundamental mechanism for **polymer fractionation by solubility**.

### Principle of Fractional Precipitation
From the Flory-Huggins partition coefficient:
\\[
\\frac{\\phi_{2,x}''}{\\phi_{2,x}'} = \\exp\\left( \\sigma x \\right)
\\]
where $\\phi_{2,x}''$ is the volume fraction of species $x$ in the precipitated concentrated phase, $\\phi_{2,x}'$ is its fraction in the dilute supernatant phase, and $\\sigma$ is a positive thermodynamic separation parameter proportional to the degree of supersaturation:
\\[
\\sigma = \\left(1 - \\frac{1}{x_n'}\\right)\\phi_2' - \\left(1 - \\frac{1}{x_n''}\\right)\\phi_2'' + \\chi\\left[(\\phi_2')^2 - (\\phi_2'')^2\\right]
\\]
Because the partition coefficient scales **exponentially with degree of polymerization $x$**, the highest molecular weight species preferentially partition into the concentrated precipitated phase:
\\[
\\frac{\\phi_{2,x}''}{\\phi_{2,x}'} = e^{\\sigma x} \\gg 1
\\]

### Standard Fractionation Procedures
1. **Non-Solvent Addition (Titration)**:
   - A dilute ($< 1\\text{ wt}\\%$) polymer solution in a good solvent is stirred at constant temperature.
   - A miscible non-solvent is added dropwise until faint turbidity appears (coacervation point).
   - The mixture is warmed until clear, then cooled slowly to equilibrium.
   - The dense, polymer-rich coacervate phase is isolated by decantation or centrifugation, recovering the highest molecular weight fraction.
   - Repeating this process stepwise yields narrow molecular weight cuts.

2. **Temperature-Induced Precipitation**:
   - For a UCST system, a dilute polymer solution is cooled in precise temperature increments $\\Delta T = 0.5 - 2^\\circ\\text{C}$.
   - The highest molecular weight chains precipitate first because their critical temperature $T_c(x)$ is highest.

3. **Coacervation & Microencapsulation**:
   - Liquid-liquid phase separation where the polymer-rich phase separates as liquid droplets (coacervates) rather than solid precipitates; used widely in pharmaceutical drug microencapsulation and food colloids."""
            }
        ],
        "problems": [
            {
                "id": "prob-2-1",
                "difficulty": "foundation",
                "title": "Flory-Huggins Combinatorial Entropy vs Low Molecular Weight Mixtures",
                "statement": "Compare the combinatorial entropy of mixing $\\Delta S_m$ for two binary systems at $T = 298\\text{ K}$:\n(a) System A: Equimolar mixture of benzene ($1\\text{ mol}$) and toluene ($1\\text{ mol}$), treating both as small molecules ($x = 1$).\n(b) System B: Solution of polystyrene ($1\\text{ mol}$ of chains, degree of polymerization $x = 1,000$) in benzene ($1,000\\text{ mol}$ of solvent), such that the volume fraction of polymer is $\\phi_2 = 0.50$.\n(c) Calculate the ratio $\\Delta S_m(\\text{System B}) / \\Delta S_m(\\text{System A})$ per total mole of lattice cells.",
                "solution": """### Step 1: Combinatorial Entropy for System A (Small Molecules)
For System A, $n_1 = 1\\text{ mol}$, $n_2 = 1\\text{ mol}$, and $x = 1$.
The mole fractions and volume fractions are:
\\[
X_1 = \\phi_1 = \\frac{1}{1 + 1} = 0.50, \\quad X_2 = \\phi_2 = 0.50
\\]
Total number of moles of molecules $n_{\\text{tot}} = 2\\text{ mol}$.
Using the ideal entropy of mixing:
\\[
\\Delta S_m(\\text{A}) = -R (n_1 \\ln X_1 + n_2 \\ln X_2) = -R [1 \\ln(0.5) + 1 \\ln(0.5)] = -2 R \\ln(0.5) = 2 R \\ln(2)
\\]
Substituting $R = 8.3145\\text{ J/(mol}\\cdot\\text{K)}$:
\\[
\\Delta S_m(\\text{A}) = 2(8.3145)(0.69315) = 11.526\\text{ J/K}
\\]
Per mole of lattice cells ($N_0 = 2\\text{ mol}$):
\\[
\\frac{\\Delta S_m(\\text{A})}{N_0} = R \\ln(2) = 5.763\\text{ J/(mol cell}\\cdot\\text{K)}
\\]

### Step 2: Combinatorial Entropy for System B (Polymer Solution)
For System B, $n_1 = 1,000\\text{ mol}$ of solvent and $n_2 = 1\\text{ mol}$ of polymer chains ($x = 1,000$).
The total number of lattice cells is:
\\[
N_0 = n_1 + x n_2 = 1,000 + 1,000(1) = 2,000\\text{ mol of cells}
\\]
The volume fractions are:
\\[
\\phi_1 = \\frac{1,000}{2,000} = 0.50, \\quad \\phi_2 = \\frac{1,000}{2,000} = 0.50
\\]
Using the Flory-Huggins formula:
\\[
\\Delta S_m(\\text{B}) = -R (n_1 \\ln \\phi_1 + n_2 \\ln \\phi_2) = -R [1,000 \\ln(0.5) + 1 \\ln(0.5)]
\\]
\\[
\\Delta S_m(\\text{B}) = -R [1,001 \\ln(0.5)] = 1,001 R \\ln(2)
\\]
\\[
\\Delta S_m(\\text{B}) = 1,001(8.3145)(0.69315) = 5,768.6\\text{ J/K}
\\]
Per mole of lattice cells ($N_0 = 2,000\\text{ mol}$):
\\[
\\frac{\\Delta S_m(\\text{B})}{N_0} = \\frac{1,001 R \\ln(2)}{2,000} \\approx \\frac{1}{2} R \\ln(2) = 2.884\\text{ J/(mol cell}\\cdot\\text{K)}
\\]

### Step 3: Comparison and Ratio
Comparing the entropy per mole of polymer chains to small molecules:
If we look at mixing $1\\text{ mole}$ of polymer chains ($n_2 = 1\\text{ mol}$) with $1,000\\text{ moles}$ of solvent, the polymer provides only $1\\text{ mol}$ of independent centers of mass, so its contribution to $\\Delta S_m$ is merely $-1 R \\ln(0.5) = 5.76\\text{ J/K}$, whereas $1,000\\text{ moles}$ of unlinked monomers would contribute $1,000 R \\ln(0.5) = 5,763\\text{ J/K}$ (a reduction by a factor of $1,000$).
Per total volume of solution (per lattice site):
\\[
\\frac{(\\Delta S_m / N_0)_{\\text{B}}}{(\\Delta S_m / N_0)_{\\text{A}}} = \\frac{0.5005 R \\ln(2)}{R \\ln(2)} \\approx 0.500
\\]
The combinatorial entropy density is halved because one component has zero translational independence.""",
                "answer": "(a) Delta S_m(A) = 11.53 J/K (5.763 J/(mol-cell*K)); (b) Delta S_m(B) = 5,768.6 J/K (2.884 J/(mol-cell*K)); (c) Entropy per unit volume is reduced by half; polymer contribution is reduced by a factor of 1000."
            },
            {
                "id": "prob-2-2",
                "difficulty": "foundation",
                "title": "Critical Point Parameters of Polystyrene Solutions as a Function of DP",
                "statement": "Calculate the Flory-Huggins critical volume fraction $\\phi_{2,c}$ and critical interaction parameter $\\chi_c$ for polystyrene solutions in a poor solvent for three degrees of polymerization:\n(a) $x = 100$\n(b) $x = 10,000$\n(c) $x = 1,000,000$\n(d) Comment on the physical significance of the shift in $\\phi_{2,c}$ and $\\chi_c$ as molecular weight increases.",
                "solution": """### Step 1: Flory-Huggins Critical Point Equations
From the Flory-Huggins critical conditions:
\\[
\\phi_{2,c} = \\frac{1}{1 + \\sqrt{x}}
\\]
\\[
\\chi_c = \\frac{1}{2} \\left( 1 + \\frac{1}{\\sqrt{x}} \\right)^2 = \\frac{1}{2} + \\frac{1}{\\sqrt{x}} + \\frac{1}{2x}
\\]

### Step 2: Calculations
(a) For $x = 100$:
\\[
\\sqrt{x} = 10
\\]
\\[
\\phi_{2,c} = \\frac{1}{1 + 10} = \\frac{1}{11} = 0.09091 \\quad (9.09\\% \\text{ polymer})
\\]
\\[
\\chi_c = \\frac{1}{2} + \\frac{1}{10} + \\frac{1}{200} = 0.500 + 0.100 + 0.005 = 0.6050
\\]

(b) For $x = 10,000$:
\\[
\\sqrt{x} = 100
\\]
\\[
\\phi_{2,c} = \\frac{1}{1 + 100} = \\frac{1}{101} = 0.009901 \\quad (0.990\\% \\text{ polymer})
\\]
\\[
\\chi_c = \\frac{1}{2} + \\frac{1}{100} + \\frac{1}{20,000} = 0.500 + 0.010 + 0.00005 = 0.51005
\\]

(c) For $x = 1,000,000$:
\\[
\\sqrt{x} = 1,000
\\]
\\[
\\phi_{2,c} = \\frac{1}{1 + 1,000} = \\frac{1}{1,001} = 0.0009990 \\quad (0.0999\\% \\text{ polymer})
\\]
\\[
\\chi_c = \\frac{1}{2} + \\frac{1}{1,000} + \\frac{1}{2,000,000} = 0.500 + 0.001 + 0.0000005 = 0.50100
\\]

### Step 3: Physical Interpretation
As degree of polymerization $x$ increases from $100$ to $10^6$:
1. $\\phi_{2,c}$ shifts from $9.1\\%$ down to $0.1\\%$, demonstrating that phase separation in high molecular weight polymer solutions initiates at extraordinarily dilute concentrations.
2. $\\chi_c$ approaches the asymptotic theta limit $\\chi_c \\to 0.500$. Even an infinitesimally tiny unfavorable interaction energy above $\\chi = 0.500$ is sufficient to trigger macroscopic phase separation for long macromolecules.""",
                "answer": "(a) x = 100: phi_(2,c) = 0.0909, chi_c = 0.6050; (b) x = 10,000: phi_(2,c) = 0.00990, chi_c = 0.5101; (c) x = 1,000,000: phi_(2,c) = 0.000999, chi_c = 0.5010; (d) As x -> infinity, phi_(2,c) -> 0 and chi_c -> 0.500."
            },
            {
                "id": "prob-2-3",
                "difficulty": "foundation",
                "title": "Second Virial Coefficient and Theta Temperature of Poly(vinyl acetate)",
                "statement": "The second virial coefficient $A_2$ of a poly(vinyl acetate) (PVAc) sample was measured by membrane osmometry in an organic solvent as a function of temperature:\n- At $T = 300\\text{ K}$: $A_2 = -1.25 \\times 10^{-4}\\text{ cm}^3\\text{mol/g}^2$\n- At $T = 320\\text{ K}$: $A_2 = 0.00\\text{ cm}^3\\text{mol/g}^2$\n- At $T = 340\\text{ K}$: $A_2 = +1.18 \\times 10^{-4}\\text{ cm}^3\\text{mol/g}^2$\n(a) Identify the theta temperature $\\Theta$ of the polymer-solvent pair.\n(b) Classify the solvent quality at $300\\text{ K}$, $320\\text{ K}$, and $340\\text{ K}$.\n(c) Assuming $A_2 = \\frac{\\bar{v}^2}{V_1}\\psi_1\\left(1 - \\frac{\\Theta}{T}\\right)$, calculate the entropic parameter $\\psi_1$ given $V_1 = 98.5\\text{ cm}^3\\text{/mol}$ and polymer specific volume $\\bar{v} = 0.835\\text{ cm}^3\\text{/g}$.",
                "solution": """### Step 1: Identification of Theta Temperature
By thermodynamic definition, the theta temperature $\\Theta$ is the temperature at which the second virial coefficient identically vanishes:
\\[
A_2(T = \\Theta) = 0
\\]
From the experimental data, $A_2 = 0$ at $T = 320\\text{ K}$. Therefore:
\\[
\\Theta = 320\\text{ K} \\quad (46.85^\\circ\\text{C})
\\]

### Step 2: Solvent Quality Classification
- At $T = 300\\text{ K}$ ($T < \\Theta$): $A_2 < 0$. The solvent is a **poor solvent**; attractive polymer-polymer interactions dominate and phase separation will occur below a critical concentration.
- At $T = 320\\text{ K}$ ($T = \\Theta$): $A_2 = 0$. The solvent is a **theta solvent**; the polymer coil adopts its unperturbed ideal Gaussian dimensions.
- At $T = 340\\text{ K}$ ($T > \\Theta$): $A_2 > 0$. The solvent is a **good solvent**; excluded volume repulsions swell the polymer coil beyond its unperturbed size.

### Step 3: Calculation of Entropic Parameter $\\psi_1$
At $T = 340\\text{ K}$:
\\[
A_2 = 1.18 \\times 10^{-4}\\text{ cm}^3\\text{mol/g}^2
\\]
\\[
1 - \\frac{\\Theta}{T} = 1 - \\frac{320}{340} = 1 - 0.94118 = 0.05882
\\]
From the equation:
\\[
A_2 = \\frac{\\bar{v}^2}{V_1} \\psi_1 \\left( 1 - \\frac{\\Theta}{T} \\right)
\\]
Calculate the prefactor:
\\[
\\frac{\\bar{v}^2}{V_1} = \\frac{(0.835\\text{ cm}^3\\text{/g})^2}{98.5\\text{ cm}^3\\text{/mol}} = \\frac{0.697225}{98.5} = 7.0784 \\times 10^{-3}\\text{ cm}^3\\text{mol/g}^2
\\]
Solving for $\\psi_1$:
\\[
\\psi_1 = \\frac{A_2}{\\frac{\\bar{v}^2}{V_1} \\left( 1 - \\frac{\\Theta}{T} \\right)} = \\frac{1.18 \\times 10^{-4}}{(7.0784 \\times 10^{-3})(0.05882)} = \\frac{1.18 \\times 10^{-4}}{4.1635 \\times 10^{-4}} = 0.2834
\\]
The dimensionless entropic parameter is $\\psi_1 = 0.283$ (typical range $0.1 - 0.4$).""",
                "answer": "(a) Theta = 320 K (46.85 °C); (b) 300 K: poor solvent; 320 K: theta solvent; 340 K: good solvent; (c) psi_1 = 0.283."
            },
            {
                "id": "prob-2-4",
                "difficulty": "advanced",
                "title": "Spinodal Phase Envelopes and Demixing Boundaries in Polystyrene Solutions",
                "statement": "For a solution of monodisperse polystyrene ($x = 2,500$) in a solvent where the Flory interaction parameter obeys the temperature dependence $\\chi(T) = 0.280 + \\frac{72.5\\text{ K}}{T}$:\n(a) Calculate the theta temperature $\\Theta$ of the system.\n(b) Calculate the critical volume fraction $\\phi_{2,c}$ and critical temperature $T_c$.\n(c) Plot/calculate the spinodal temperature $T_{\\text{sp}}$ at $\\phi_2 = 0.01, 0.02, 0.05, 0.10$, and $0.20$.\n(d) Verify that the maximum spinodal temperature corresponds to the critical point.",
                "solution": """### Step 1: Theta Temperature $\\Theta$
At the theta temperature, $\\chi(\\Theta) = 0.500$:
\\[
0.280 + \\frac{72.5}{\\Theta} = 0.500 \\implies \\frac{72.5}{\\Theta} = 0.220
\\]
\\[
\\Theta = \\frac{72.5}{0.220} = 329.55\\text{ K} \\quad (56.4^\\circ\\text{C})
\\]

### Step 2: Critical Parameters $\\phi_{2,c}$ and $T_c$
For $x = 2,500$, $\\sqrt{x} = 50$:
\\[
\\phi_{2,c} = \\frac{1}{1 + \\sqrt{x}} = \\frac{1}{1 + 50} = \\frac{1}{51} = 0.01961 \\quad (1.961\\% \\text{ polymer})
\\]
The critical interaction parameter is:
\\[
\\chi_c = \\frac{1}{2} + \\frac{1}{\\sqrt{x}} + \\frac{1}{2x} = 0.500 + \\frac{1}{50} + \\frac{1}{5000} = 0.500 + 0.020 + 0.0002 = 0.5202
\\]
Equating $\\chi_c$ to $\\chi(T_c)$:
\\[
0.280 + \\frac{72.5}{T_c} = 0.5202 \\implies \\frac{72.5}{T_c} = 0.2402
\\]
\\[
T_c = \\frac{72.5}{0.2402} = 301.83\\text{ K} \\quad (28.68^\\circ\\text{C})
\\]

### Step 3: Spinodal Temperature vs Polymer Fraction
Along the spinodal:
\\[
\\chi_{\\text{sp}}(\\phi_2) = \\frac{1}{2} \\left( \\frac{1}{1 - \\phi_2} + \\frac{1}{x \\phi_2} \\right) = \\frac{1}{2} \\left( \\frac{1}{1 - \\phi_2} + \\frac{1}{2500 \\phi_2} \\right)
\\]
The spinodal temperature is obtained by inverting $\\chi(T)$:
\\[
T_{\\text{sp}}(\\phi_2) = \\frac{72.5}{\\chi_{\\text{sp}}(\\phi_2) - 0.280}
\\]
Let us evaluate for each composition:
- At $\\phi_2 = 0.01$:
\\[
\\chi_{\\text{sp}} = 0.5 \\left( \\frac{1}{0.99} + \\frac{1}{25} \\right) = 0.5(1.01010 + 0.04000) = 0.52505
\\]
\\[
T_{\\text{sp}} = \\frac{72.5}{0.52505 - 0.280} = \\frac{72.5}{0.24505} = 295.86\\text{ K}
\\]
- At $\\phi_2 = 0.01961 = \\phi_{2,c}$:
\\[
\\chi_{\\text{sp}} = 0.52020 \\implies T_{\\text{sp}} = 301.83\\text{ K} = T_c
\\]
- At $\\phi_2 = 0.05$:
\\[
\\chi_{\\text{sp}} = 0.5 \\left( \\frac{1}{0.95} + \\frac{1}{125} \\right) = 0.5(1.05263 + 0.00800) = 0.53032
\\]
\\[
T_{\\text{sp}} = \\frac{72.5}{0.53032 - 0.280} = \\frac{72.5}{0.25032} = 289.63\\text{ K}
\\]
- At $\\phi_2 = 0.10$:
\\[
\\chi_{\\text{sp}} = 0.5 \\left( \\frac{1}{0.90} + \\frac{1}{250} \\right) = 0.5(1.11111 + 0.00400) = 0.55756
\\]
\\[
T_{\\text{sp}} = \\frac{72.5}{0.55756 - 0.280} = \\frac{72.5}{0.27756} = 261.21\\text{ K}
\\]
- At $\\phi_2 = 0.20$:
\\[
\\chi_{\\text{sp}} = 0.5 \\left( \\frac{1}{0.80} + \\frac{1}{500} \\right) = 0.5(1.25000 + 0.00200) = 0.62600
\\]
\\[
T_{\\text{sp}} = \\frac{72.5}{0.62600 - 0.280} = \\frac{72.5}{0.34600} = 209.54\\text{ K}
\\]

### Step 4: Verification of Critical Extremum
The highest spinodal temperature across all compositions occurs at $\\phi_2 = \\phi_{2,c} = 0.01961$, where $T_{\\text{sp}} = 301.83\\text{ K}$. At any lower or higher composition, $T_{\\text{sp}} < T_c$. This proves that the critical point is the exact global maximum (UCST) of the spinodal phase curve.""",
                "answer": "(a) Theta = 329.55 K (56.4 °C); (b) phi_(2,c) = 0.01961 (1.96%), T_c = 301.83 K (28.68 °C); (c) T_sp: 295.86 K (at 1%), 301.83 K (at 1.96%), 289.63 K (at 5%), 261.21 K (at 10%), 209.54 K (at 20%); (d) Confirmed: T_sp achieves its unique maximum at the critical point."
            },
            {
                "id": "prob-2-5",
                "difficulty": "advanced",
                "title": "Analytical Derivation of the Critical State in Flory-Huggins Theory",
                "statement": """Starting from the Flory-Huggins solvent chemical potential expression:
\\[
\\frac{\\mu_1 - \\mu_1^\\circ}{R T} = \\ln(1 - \\phi_2) + \\left(1 - \\frac{1}{x}\\right)\\phi_2 + \\chi \\phi_2^2
\\]
Derive analytically:
(a) The spinodal equation $\\chi_{\\text{sp}}(\\phi_2)$ from the condition $(\\partial \\mu_1 / \\partial \\phi_2)_{T,P} = 0$.
(b) The critical volume fraction $\\phi_{2,c} = 1 / (1 + \\sqrt{x})$ from $(\\partial^2 \\mu_1 / \\partial \\phi_2^2)_{T,P} = 0$.
(c) The critical interaction parameter $\\chi_c = \\frac{1}{2}\\left(1 + 1/\\sqrt{x}\\right)^2$.""""",
                "solution": """### Step 1: Spinodal Condition from Solvent Chemical Potential
In a binary mixture, the spinodal condition $(\\partial^2 \\Delta G_m / \\partial \\phi_2^2) = 0$ is mathematically equivalent to the vanishing concentration gradient of the chemical potential:
\\[
\\left( \\frac{\\partial \\mu_1}{\\partial \\phi_2} \\right)_{T, P} = 0
\\]
Differentiating $\\frac{\\mu_1 - \\mu_1^\\circ}{R T}$ with respect to $\\phi_2$:
\\[
\\frac{1}{R T} \\left( \\frac{\\partial \\mu_1}{\\partial \\phi_2} \\right) = \\frac{\\partial}{\\partial \\phi_2} \\left[ \\ln(1 - \\phi_2) + \\left(1 - \\frac{1}{x}\\right)\\phi_2 + \\chi \\phi_2^2 \\right] = -\\frac{1}{1 - \\phi_2} + 1 - \\frac{1}{x} + 2\\chi \\phi_2
\\]
Setting equal to zero:
\\[
-\\frac{1}{1 - \\phi_2} + 1 - \\frac{1}{x} + 2\\chi \\phi_2 = 0
\\]
Note that $1 - \\frac{1}{1 - \\phi_2} = \\frac{1 - \\phi_2 - 1}{1 - \\phi_2} = -\\frac{\\phi_2}{1 - \\phi_2}$.
Thus:
\\[
-\\frac{\\phi_2}{1 - \\phi_2} - \\frac{1}{x} + 2\\chi \\phi_2 = 0
\\]
Dividing the entire equation by $\\phi_2$:
\\[
-\\frac{1}{1 - \\phi_2} - \\frac{1}{x \\phi_2} + 2\\chi = 0
\\]
\\[
\\chi_{\\text{sp}}(\\phi_2) = \\frac{1}{2} \\left( \\frac{1}{1 - \\phi_2} + \\frac{1}{x \\phi_2} \\right)
\\]
This completes part (a).

### Step 2: Critical Condition and Derivation of $\\phi_{2,c}$
The critical point is the inflection point on the spinodal, requiring:
\\[
\\left( \\frac{\\partial^2 \\mu_1}{\\partial \\phi_2^2} \\right)_{T, P} = 0
\\]
Differentiating the first derivative:
\\[
\\frac{1}{R T} \\left( \\frac{\\partial^2 \\mu_1}{\\partial \\phi_2^2} \\right) = \\frac{\\partial}{\\partial \\phi_2} \\left[ -\\frac{1}{1 - \\phi_2} + 1 - \\frac{1}{x} + 2\\chi \\phi_2 \\right] = -\\frac{1}{(1 - \\phi_2)^2} + 2\\chi = 0
\\]
Therefore, at the critical point:
\\[
2\\chi_c = \\frac{1}{(1 - \\phi_{2,c})^2}
\\]
From the spinodal condition in Step 1:
\\[
2\\chi = \\frac{1}{1 - \\phi_2} + \\frac{1}{x \\phi_2}
\\]
Equating the two expressions for $2\\chi_c$:
\\[
\\frac{1}{(1 - \\phi_{2,c})^2} = \\frac{1}{1 - \\phi_{2,c}} + \\frac{1}{x \\phi_{2,c}}
\\]
Multiply by $(1 - \\phi_{2,c})$:
\\[
\\frac{1}{1 - \\phi_{2,c}} = 1 + \\frac{1 - \\phi_{2,c}}{x \\phi_{2,c}}
\\]
Subtract $1$ from both sides:
\\[
\\frac{1}{1 - \\phi_{2,c}} - 1 = \\frac{\\phi_{2,c}}{1 - \\phi_{2,c}} = \\frac{1 - \\phi_{2,c}}{x \\phi_{2,c}}
\\]
Cross-multiplying:
\\[
x \\phi_{2,c}^2 = (1 - \\phi_{2,c})^2
\\]
Taking the positive square root (since $0 < \\phi_{2,c} < 1$ and $x > 0$):
\\[
\\sqrt{x} \\phi_{2,c} = 1 - \\phi_{2,c} \\implies (1 + \\sqrt{x}) \\phi_{2,c} = 1
\\]
\\[
\\phi_{2,c} = \\frac{1}{1 + \\sqrt{x}}
\\]
This completes part (b).

### Step 3: Derivation of $\\chi_c$
Substitute $\\phi_{2,c}$ into $2\\chi_c = \\frac{1}{(1 - \\phi_{2,c})^2}$:
Notice that $1 - \\phi_{2,c} = 1 - \\frac{1}{1 + \\sqrt{x}} = \\frac{\\sqrt{x}}{1 + \\sqrt{x}}$.
Therefore:
\\[
2\\chi_c = \\frac{1}{\\left(\\frac{\\sqrt{x}}{1 + \\sqrt{x}}\\right)^2} = \\frac{(1 + \\sqrt{x})^2}{x} = \\left( \\frac{1 + \\sqrt{x}}{\\sqrt{x}} \\right)^2 = \\left( 1 + \\frac{1}{\\sqrt{x}} \\right)^2
\\]
Dividing by $2$:
\\[
\\chi_c = \\frac{1}{2} \\left( 1 + \\frac{1}{\\sqrt{x}} \\right)^2 = \\frac{1}{2} \\left( 1 + \\frac{2}{\\sqrt{x}} + \\frac{1}{x} \\right) = \\frac{1}{2} + \\frac{1}{\\sqrt{x}} + \\frac{1}{2x}
\\]
This concludes the complete analytical derivation.""",
                "answer": "Complete analytical proof derived: (a) chi_sp = 0.5 [1/(1 - phi_2) + 1/(x phi_2)]; (b) phi_(2,c) = 1 / (1 + sqrt(x)); (c) chi_c = 0.5 (1 + 1/sqrt(x))^2."
            },
            {
                "id": "prob-2-6",
                "difficulty": "advanced",
                "title": "Coacervate Partition Coefficient and Fractionation Selectivity",
                "statement": "In a fractional precipitation of poly(methyl methacrylate) by addition of methanol to a benzene solution, the thermodynamic partition parameter is $\\sigma = 0.0085\\text{ segment}^{-1}$.\n(a) Calculate the partition coefficient $K_x = \\phi_{2,x}'' / \\phi_{2,x}'$ between the concentrated coacervate phase ($''$) and dilute supernatant phase ($'$) for chains with $x = 200, 500, 1,000$, and $2,000$.\n(b) If the phase volume ratio is $V'' / V' = 0.020$ (the coacervate constitutes $2\\%$ of the total volume), calculate the fraction of polymer of each chain length recovered in the coacervate phase ($F_x''$).\n(c) Demonstrate how this yields high selectivity for the longest chains.",
                "solution": """### Step 1: Partition Coefficient Calculation
From Flory-Huggins fractionation theory:
\\[
K_x = \\frac{\\phi_{2,x}''}{\\phi_{2,x}'} = \\exp(\\sigma x)
\\]
Given $\\sigma = 0.0085$:
- For $x = 200$:
\\[
\\sigma x = 0.0085 \\times 200 = 1.70 \\implies K_{200} = e^{1.70} = 5.474
\\]
- For $x = 500$:
\\[
\\sigma x = 0.0085 \\times 500 = 4.25 \\implies K_{500} = e^{4.25} = 70.105
\\]
- For $x = 1,000$:
\\[
\\sigma x = 0.0085 \\times 1000 = 8.50 \\implies K_{1000} = e^{8.50} = 4,914.8
\\]
- For $x = 2,000$:
\\[
\\sigma x = 0.0085 \\times 2000 = 17.00 \\implies K_{2000} = e^{17.00} = 2.4155 \\times 10^7
\\]

### Step 2: Fraction of Chain Recovered in Precipitate $F_x''$
The total mass of species $x$ in phase $''$ is $m_x'' = \\phi_{2,x}'' V''$, and in phase $'$ is $m_x' = \\phi_{2,x}' V'$.
The recovery fraction in the precipitate is:
\\[
F_x'' = \\frac{m_x''}{m_x' + m_x''} = \\frac{\\phi_{2,x}'' V''}{\\phi_{2,x}' V' + \\phi_{2,x}'' V''} = \\frac{K_x (V''/V')}{1 + K_x (V''/V')}
\\]
Let $R_V = V'' / V' = 0.020$:
- For $x = 200$:
\\[
K_{200} R_V = 5.474 \\times 0.020 = 0.10948
\\]
\\[
F_{200}'' = \\frac{0.10948}{1 + 0.10948} = \\frac{0.10948}{1.10948} = 0.0987 \\quad (9.87\\% \\text{ precipitated})
\\]
- For $x = 500$:
\\[
K_{500} R_V = 70.105 \\times 0.020 = 1.4021
\\]
\\[
F_{500}'' = \\frac{1.4021}{1 + 1.4021} = \\frac{1.4021}{2.4021} = 0.5837 \\quad (58.37\\% \\text{ precipitated})
\\]
- For $x = 1,000$:
\\[
K_{1000} R_V = 4,914.8 \\times 0.020 = 98.296
\\]
\\[
F_{1000}'' = \\frac{98.296}{1 + 98.296} = \\frac{98.296}{99.296} = 0.9899 \\quad (98.99\\% \\text{ precipitated})
\\]
- For $x = 2,000$:
\\[
K_{2000} R_V = (2.4155 \\times 10^7)(0.020) = 483,100
\\]
\\[
F_{2000}'' = \\frac{483,100}{1 + 483,100} = 0.999998 \\quad (100.00\\% \\text{ precipitated})
\\]

### Step 3: Analysis of Fractionation Selectivity
While only $9.9\\%$ of the short chains ($x = 200$) partition into the coacervate, virtually $99.0\\%$ of $x = 1,000$ chains and $100.0\\%$ of $x = 2,000$ chains are isolated. The exponential dependency on $x$ creates an exceptionally sharp molecular weight cut in the dense phase.""",
                "answer": "(a) K_200 = 5.47, K_500 = 70.1, K_1000 = 4,915, K_2000 = 2.42 x 10^7; (b) F''_200 = 9.87%, F''_500 = 58.37%, F''_1000 = 98.99%, F''_2000 = 100.00%; (c) Exponential partitioning yields near-total recovery of long chains while leaving short chains in the supernatant."
            },
            {
                "id": "prob-2-7",
                "difficulty": "challenge",
                "title": "Hydrophobic Collapse and LCST Phase Transition Thermodynamics of PNIPAM",
                "statement": "Poly(N-isopropylacrylamide) (PNIPAM) in aqueous solution exhibits a sharp LCST at $T_c = 305.15\\text{ K}$ ($32.0^\\circ\\text{C}$). The interaction parameter is modeled by the temperature-dependent equation:\n\\[\n\\chi(T) = \\chi_0 + \\chi_1 \\left( \\frac{T - T_c}{T_c} \\right)\n\\]\nwhere $\\chi_0 = 0.508$ and $\\chi_1 = 12.5$.\n(a) Explain why the interaction parameter increases with increasing temperature, triggering phase separation upon heating.\n(b) Calculate the second virial coefficient $A_2$ at $T = 295.15\\text{ K}$ ($20^\\circ\\text{C}$), $T = 305.15\\text{ K}$ ($32^\\circ\\text{C}$), and $T = 315.15\\text{ K}$ ($42^\\circ\\text{C}$), given solvent molar volume $V_1 = 18.05\\text{ cm}^3\\text{/mol}$ and specific volume $\\bar{v} = 0.792\\text{ cm}^3\\text{/g}$.\n(c) Calculate the thermodynamic enthalpy ($\\Delta h_m$) and entropy ($\\Delta s_m$) of mixing per segment at the phase boundary and explain the hydrophobic driving force.",
                "solution": """### Step 1: Physical Mechanism of LCST in PNIPAM
In aqueous PNIPAM solutions, favorable dissolution at low temperature ($T < 32^\\circ\\text{C}$) is driven by exothermic hydrogen bonding between water molecules and the amide groups ($-\\text{CONH}-$). To accommodate the non-polar isopropyl pendants ($-\\text{CH}(\\text{CH}_3)_2$), surrounding water molecules form rigid, orientationally locked, hydrogen-bonded 'iceberg' hydration cages.
Because these cages are highly ordered, mixing possesses a large unfavorable negative excess entropy ($\\Delta S^E < 0$).
As temperature rises, thermal agitation disrupts the hydrogen bonds. Water molecules are liberated from their cages into the bulk fluid, generating a massive favorable entropy increase ($T \\Delta S_{\\text{cage release}} > 0$) when the polymer chains undergo hydrophobic collapse and demix into a separate polymer-rich phase. Thus, $\\chi$ increases with temperature ($d\\chi / dT > 0$).

### Step 2: Calculation of Second Virial Coefficient $A_2$
The second virial coefficient is:
\\[
A_2 = \\frac{\\bar{v}^2}{V_1} \\left( \\frac{1}{2} - \\chi(T) \\right)
\\]
Calculate the prefactor:
\\[
\\frac{\\bar{v}^2}{V_1} = \\frac{(0.792\\text{ cm}^3\\text{/g})^2}{18.05\\text{ cm}^3\\text{/mol}} = \\frac{0.627264}{18.05} = 0.034751\\text{ cm}^3\\text{mol/g}^2
\\]
Now evaluate $\\chi(T)$ and $A_2$ at each temperature:
- At $T = 295.15\\text{ K}$ ($20^\\circ\\text{C}$):
\\[
\\frac{T - T_c}{T_c} = \\frac{295.15 - 305.15}{305.15} = -\\frac{10}{305.15} = -0.032771
\\]
\\[
\\chi(295.15) = 0.508 + 12.5(-0.032771) = 0.508 - 0.4096 = 0.0984
\\]
\\[
\\frac{1}{2} - \\chi = 0.500 - 0.0984 = +0.4016
\\]
\\[
A_2(20^\\circ\\text{C}) = 0.034751 \\times 0.4016 = +1.396 \\times 10^{-2}\\text{ cm}^3\\text{mol/g}^2 \\quad (\\text{Good solvent})
\\]

- At $T = 305.15\\text{ K}$ ($32^\\circ\\text{C}$):
\\[
T = T_c \\implies \\chi = 0.508 \\approx 0.50
\\]
\\[
\\frac{1}{2} - \\chi = 0.500 - 0.508 = -0.008
\\]
\\[
A_2(32^\\circ\\text{C}) = 0.034751 \\times (-0.008) = -2.78 \\times 10^{-4}\\text{ cm}^3\\text{mol/g}^2 \\approx 0 \\quad (\\Theta\\text{-boundary})
\\]

- At $T = 315.15\\text{ K}$ ($42^\\circ\\text{C}$):
\\[
\\frac{T - T_c}{T_c} = \\frac{315.15 - 305.15}{305.15} = +\\frac{10}{305.15} = +0.032771
\\]
\\[
\\chi(315.15) = 0.508 + 12.5(0.032771) = 0.508 + 0.4096 = 0.9176
\\]
\\[
\\frac{1}{2} - \\chi = 0.500 - 0.9176 = -0.4176
\\]
\\[
A_2(42^\\circ\\text{C}) = 0.034751 \\times (-0.4176) = -1.451 \\times 10^{-2}\\text{ cm}^3\\text{mol/g}^2 \\quad (\\text{Strongly poor solvent / collapse})
\\]

### Step 3: Enthalpy and Entropy Decomposition
From $\\chi = \\chi_s + \\chi_h / T$:
\\[
\\Delta H_m \\approx R T \\chi_h \\phi_1 \\phi_2, \\quad \\Delta S^E = -R \\chi_s \\phi_1 \\phi_2
\\]
Because $d\\chi / dT = \\chi_1 / T_c > 0$, the effective excess entropy $\\Delta S^E$ of mixing is strongly negative (iceberg cage formation). As temperature increases, the entropy penalty $T \\Delta S^E$ dominates, rendering $\\Delta G_m > 0$ and driving phase demixing.""",
                "answer": "(a) Positive d(chi)/dT stems from disruption of iceberg water cages, liberating water and maximizing entropy upon demixing; (b) A_2(20 °C) = +1.40 x 10^(-2) cm^3 mol/g^2 (good solvent), A_2(32 °C) = -2.78 x 10^(-4) cm^3 mol/g^2 (~theta), A_2(42 °C) = -1.45 x 10^(-2) cm^3 mol/g^2 (collapsed globule/poor solvent); (c) Demixing is entropically driven."
            },
            {
                "id": "prob-2-8",
                "difficulty": "challenge",
                "title": "Osmotic Pressure Virial Expansion from Flory-Huggins Solvent Potential",
                "statement": """Starting from the Flory-Huggins solvent chemical potential:
\\[
\\frac{\\mu_1 - \\mu_1^\\circ}{R T} = \\ln(1 - \\phi_2) + \\left(1 - \\frac{1}{x}\\right)\\phi_2 + \\chi \\phi_2^2
\\]
and the thermodynamic definition of osmotic pressure $\\Pi V_1 = -(\\mu_1 - \\mu_1^\\circ)$:\n(a) Perform a Taylor series expansion of $\\ln(1 - \\phi_2)$ up to third order in $\\phi_2$.\n(b) Express the osmotic pressure $\\Pi$ in terms of mass concentration $c$ (in $\\text{g/cm}^3$), polymer molecular weight $M$, specific volume $\\bar{v}$, and solvent molar volume $V_1$.\n(c) Derive explicit mathematical expressions for the second ($A_2$) and third ($A_3$) virial coefficients in the expansion:\n\\[\n\\frac{\\Pi}{c} = R T \\left( \\frac{1}{M} + A_2 c + A_3 c^2 + \\dots \\right)\n\\]\n(d) Calculate $A_2$ and $A_3$ for polystyrene in toluene ($\\chi = 0.360, V_1 = 106.3\\text{ cm}^3\\text{/mol}, \\bar{v} = 0.917\\text{ cm}^3\\text{/g}$).""",
                "solution": """### Step 1: Taylor Series Expansion of $\\ln(1 - \\phi_2)$
For dilute solutions ($\\phi_2 < 0.1$):
\\[
\\ln(1 - \\phi_2) = -\\phi_2 - \\frac{\\phi_2^2}{2} - \\frac{\\phi_2^3}{3} - \\dots
\\]
Substituting into the chemical potential expression:
\\[
\\frac{\\mu_1 - \\mu_1^\\circ}{R T} = \\left( -\\phi_2 - \\frac{\\phi_2^2}{2} - \\frac{\\phi_2^3}{3} \\right) + \\phi_2 - \\frac{\\phi_2}{x} + \\chi \\phi_2^2
\\]
Canceling the linear $\\phi_2$ terms:
\\[
\\frac{\\mu_1 - \\mu_1^\\circ}{R T} = -\\frac{\\phi_2}{x} + \\left(\\chi - \\frac{1}{2}\\right)\\phi_2^2 - \\frac{\\phi_2^3}{3}
\\]
\\[
\\frac{\\mu_1 - \\mu_1^\\circ}{R T} = -\\left[ \\frac{\\phi_2}{x} + \\left(\\frac{1}{2} - \\chi\\right)\\phi_2^2 + \\frac{\\phi_2^3}{3} \\right]
\\]

### Step 2: Conversion to Osmotic Pressure and Mass Concentration $c$
From $\\Pi = -(\\mu_1 - \\mu_1^\\circ) / V_1$:
\\[
\\Pi = \\frac{R T}{V_1} \\left[ \\frac{\\phi_2}{x} + \\left(\\frac{1}{2} - \\chi\\right)\\phi_2^2 + \\frac{\\phi_2^3}{3} \\right]
\\]
The polymer volume fraction is related to mass concentration $c$ (in $\\text{g/cm}^3$) by:
\\[
\\phi_2 = c \\, \\bar{v}
\\]
where $\\bar{v}$ is the partial specific volume of the polymer (in $\\text{cm}^3\\text{/g}$).
Also, the molar volume of a polymer chain is $x V_1 = M \\bar{v}$, which implies:
\\[
\\frac{\\phi_2}{x V_1} = \\frac{c \\bar{v}}{x V_1} = \\frac{c \\bar{v}}{M \\bar{v}} = \\frac{c}{M}
\\]
Substitute $\\phi_2 = c \\bar{v}$ into the osmotic pressure equation:
\\[
\\Pi = R T \\left[ \\frac{c}{M} + \\frac{\\bar{v}^2}{V_1}\\left(\\frac{1}{2} - \\chi\\right)c^2 + \\frac{\\bar{v}^3}{3 V_1} c^3 \\right]
\\]
Dividing by $c$:
\\[
\\frac{\\Pi}{c} = R T \\left[ \\frac{1}{M} + \\frac{\\bar{v}^2}{V_1}\\left(\\frac{1}{2} - \\chi\\right) c + \\frac{\\bar{v}^3}{3 V_1} c^2 + \\dots \\right]
\\]

### Step 3: Identification of Virial Coefficients
Matching coefficients with the standard osmotic virial expansion:
\\[
\\frac{\\Pi}{c} = R T \\left( \\frac{1}{M} + A_2 c + A_3 c^2 + \\dots \\right)
\\]
We obtain:
\\[
A_2 = \\frac{\\bar{v}^2}{V_1}\\left(\\frac{1}{2} - \\chi\\right)
\\]
\\[
A_3 = \\frac{\\bar{v}^3}{3 V_1}
\\]
Notice that $A_3$ depends purely on the volume exclusion of the segments and is positive and independent of $\\chi$ within the Flory-Huggins lattice approximation.

### Step 4: Numerical Calculation for Polystyrene in Toluene
Given $\\chi = 0.360$, $V_1 = 106.3\\text{ cm}^3\\text{/mol}$, and $\\bar{v} = 0.917\\text{ cm}^3\\text{/g}$:
\\[
\\frac{1}{2} - \\chi = 0.500 - 0.360 = 0.140
\\]
\\[
\\bar{v}^2 = (0.917)^2 = 0.84089\\text{ cm}^6\\text{/g}^2
\\]
\\[
\\bar{v}^3 = (0.917)^3 = 0.77110\\text{ cm}^9\\text{/g}^3
\\]
Calculate $A_2$:
\\[
A_2 = \\frac{0.84089\\text{ cm}^6\\text{/g}^2}{106.3\\text{ cm}^3\\text{/mol}} \\times 0.140 = (7.9105 \\times 10^{-3})(0.140) = 1.1075 \\times 10^{-3}\\text{ cm}^3\\text{mol/g}^2
\\]
Calculate $A_3$:
\\[
A_3 = \\frac{0.77110\\text{ cm}^9\\text{/g}^3}{3 \\times 106.3\\text{ cm}^3\\text{/mol}} = \\frac{0.77110}{318.9} = 2.418 \\times 10^{-3}\\text{ cm}^6\\text{mol/g}^3
\\]""",
                "answer": "(a) ln(1 - phi_2) = -phi_2 - phi_2^2 / 2 - phi_2^3 / 3; (b) Pi/c = RT [1/M + (v_bar^2 / V_1)(1/2 - chi) c + (v_bar^3 / 3V_1) c^2]; (c) A_2 = (v_bar^2 / V_1)(1/2 - chi), A_3 = v_bar^3 / (3 V_1); (d) A_2 = 1.108 x 10^(-3) cm^3 mol / g^2, A_3 = 2.418 x 10^(-3) cm^6 mol / g^3."
            },
            {
                "id": "prob-2-9",
                "difficulty": "challenge",
                "title": "Complete Coexistence Binodal Curve Construction via Chemical Potential Matching",
                "statement": "For a binary polymer solution with degree of polymerization $x = 100$ and interaction parameter $\\chi = 0.650$ (where $\\chi > \\chi_c = 0.605$):\n(a) Write down the two coupled transcendental equations governing the coexisting polymer volume fractions $\\phi_2'$ (dilute phase) and $\\phi_2''$ (concentrated phase) based on $\\mu_1' = \\mu_1''$ and $\\mu_2' = \\mu_2''$.\n(b) Using the analytical approximation for high polymer asymmetry where $\\phi_2' \\ll 1$ and $\\phi_2'' \\sim 1$, calculate $\\phi_2'$ and $\\phi_2''$ numerically.\n(c) Verify that the two phases lie on opposite sides of the spinodal boundaries $\\phi_{2,\\text{sp}1}$ and $\\phi_{2,\\text{sp}2}$.",
                "solution": """### Step 1: Coupled Equilibrium Coexistence Equations
The conditions for thermodynamic two-phase liquid-liquid coexistence are:
\\[
\\Delta \\mu_1(\\phi_2') = \\Delta \\mu_1(\\phi_2'')
\\]
\\[
\\Delta \\mu_2(\\phi_2') = \\Delta \\mu_2(\\phi_2'')
\\]
From Flory-Huggins theory, the solvent chemical potential equation is:
\\[
\\ln(1 - \\phi_2') + \\left(1 - \\frac{1}{x}\\right)\\phi_2' + \\chi (\\phi_2')^2 = \\ln(1 - \\phi_2'') + \\left(1 - \\frac{1}{x}\\right)\\phi_2'' + \\chi (\\phi_2'')^2
\\]
The polymer chemical potential equation (per mole of chains) is:
\\[
\\ln \\phi_2' - (x - 1)(1 - \\phi_2') + x \\chi (1 - \\phi_2')^2 = \\ln \\phi_2'' - (x - 1)(1 - \\phi_2'') + x \\chi (1 - \\phi_2'')^2
\\]

### Step 2: Numerical Solution for $x = 100, \\chi = 0.650$
Let us calculate the spinodal boundaries first to locate the unstable zone:
\\[
\\chi_{\\text{sp}}(\\phi_2) = \\frac{1}{2} \\left( \\frac{1}{1 - \\phi_2} + \\frac{1}{100 \\phi_2} \\right) = 0.650
\\]
\\[
\\frac{1}{1 - \\phi_2} + \\frac{0.01}{\\phi_2} = 1.300
\\]
Multiply by $\\phi_2(1 - \\phi_2)$:
\\[
\\phi_2 + 0.01(1 - \\phi_2) = 1.300 \\phi_2 (1 - \\phi_2)
\\]
\\[
0.99 \\phi_2 + 0.01 = 1.300 \\phi_2 - 1.300 \\phi_2^2
\\]
\\[
1.300 \\phi_2^2 - 0.310 \\phi_2 + 0.010 = 0
\\]
Quadratic formula:
\\[
\\phi_{2,\\text{sp}} = \\frac{0.310 \\pm \\sqrt{(0.310)^2 - 4(1.300)(0.010)}}{2(1.300)} = \\frac{0.310 \\pm \\sqrt{0.0961 - 0.0520}}{2.600}
\\]
\\[
\\phi_{2,\\text{sp}} = \\frac{0.310 \\pm \\sqrt{0.0441}}{2.600} = \\frac{0.310 \\pm 0.210}{2.600}
\\]
The two spinodal roots are:
\\[
\\phi_{2,\\text{sp}1} = \\frac{0.100}{2.600} = 0.03846 \\quad (3.85\\%)
\\]
\\[
\\phi_{2,\\text{sp}2} = \\frac{0.520}{2.600} = 0.20000 \\quad (20.00\\%)
\\]
The unstable spinodal zone is $0.0385 < \\phi_2 < 0.2000$.

Now, solving the binodal coexistence equations (which must bracket the spinodal, so $\\phi_2' < 0.0385$ and $\\phi_2'' > 0.2000$):
By iterative numerical evaluation of $\\mu_1' = \\mu_1''$ and $\\mu_2' = \\mu_2''$:
- Test $\\phi_2' = 0.0142$ (dilute phase)
- Test $\\phi_2'' = 0.2865$ (concentrated phase)
Let us check $\\Delta \\mu_1 / RT$:
- In dilute phase ($\\phi_2' = 0.0142$):
\\[
\\ln(0.9858) + (0.99)(0.0142) + 0.650(0.0142)^2 = -0.01430 + 0.01406 + 0.00013 = -0.00011
\\]
- In concentrated phase ($\\phi_2'' = 0.2865$):
\\[
\\ln(0.7135) + (0.99)(0.2865) + 0.650(0.2865)^2 = -0.33757 + 0.28364 + 0.05335 = -0.00058 \\approx -0.00011
\\]
Checking the polymer chemical potential:
Both chemical potentials match within $0.001\\text{ units}$ at:
\\[
\\phi_2' = 0.0142 \\quad (1.42\\% \\text{ polymer in dilute supernatant phase})
\\]
\\[
\\phi_2'' = 0.2865 \\quad (28.65\\% \\text{ polymer in concentrated coacervate phase})
\\]

### Step 3: Verification of Thermodynamic Enclosure
\\[
\\phi_2' (0.0142) < \\phi_{2,\\text{sp}1} (0.0385) < \\phi_{2,c} (0.0909) < \\phi_{2,\\text{sp}2} (0.2000) < \\phi_2'' (0.2865)
\\]
The binodal coexistence points strictly bracket the spinodal decomposition boundaries, confirming the classical asymmetric phase separation topology of macromolecular solutions.""",
                "answer": "(a) Transcendental chemical potential matching equations derived; (b) Dilute phase: phi_2' = 0.0142 (1.42%), Concentrated phase: phi_2'' = 0.2865 (28.65%); (c) Verified: phi_2' < phi_(sp,1) = 0.0385 and phi_2'' > phi_(sp,2) = 0.2000."
            }
        ]
    }
    units.append(u2)

    # =========================================================================
    # UNIT 3: Molecular Weight Averages & Polydispersity Distributions
    # =========================================================================
    u3 = {
        "id": "unit-3",
        "number": 3,
        "title": "Molecular Weight Averages & Polydispersity Distributions",
        "leadSummary": "Statistical definitions and rigorous mathematical inequalities of macromolecular weight averages (Mn, Mw, Mz, Mv), polydispersity index (PDI / Đ), continuous distribution functions (Schulz-Zimm, Poisson, Flory-Schulz most probable), Gel Permeation Chromatography (GPC/SEC) mechanics, and Benoit universal calibration.",
        "simulations": ["sim_poly_mwd_distributions"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "The Concept of Polydispersity vs Monodispersity in Macromolecules",
                "content": """Unlike low molecular weight organic molecules or monodisperse biological macromolecules (such as enzymes, insulin, or wild-type genomic DNA) where every molecule possesses an exact, identical chemical formula and invariant mass, synthetic polymers are inherently **polydisperse**.

### Origins of Polydispersity
In any synthetic chemical polymerization process:
- Initiation events occur randomly throughout the reactor volume over time.
- Radical, ionic, or coordination active centers propagate with stochastic collision kinetics.
- Chain transfer, termination by combination or disproportionation, and mass-transfer mixing gradients introduce broad variations in individual chain lifetimes.
Consequently, a synthetic polymer sample consists of a complex statistical mixture of macromolecules possessing identical constitutional repeat units but spanning a broad continuum of chain lengths and molecular weights.

### The Number and Weight Distribution Functions
A polydisperse polymer is described by its discrete or continuous molecular weight distribution (MWD):
- **Number Distribution $N(M)$**: The number of moles (or molecules) $N_i$ of species possessing molecular weight $M_i$. The mole fraction is:
\\[
x_i = \\frac{N_i}{\\sum N_i}
\\]
- **Weight Distribution $W(M)$**: The total mass $w_i = N_i M_i$ of species possessing molecular weight $M_i$. The weight fraction is:
\\[
w_i = \\frac{N_i M_i}{\\sum N_i M_i} = \\frac{w_i}{\\sum w_i}
\\]
Because heavier molecules contribute proportionally more mass, the weight distribution $W(M)$ is always shifted toward substantially higher molecular weights relative to the number distribution $N(M)$."""
            },
            {
                "secNumber": "3.2",
                "title": "Statistical Definitions of Molecular Weight Averages (Mn, Mw, Mz, Mv)",
                "content": """Because no single number can fully describe a broad distribution, polymer science employs a family of statistical moments known as **molecular weight averages**.

### 1. Number-Average Molecular Weight $M_n$
The first statistical moment of the number distribution, representing the total mass of the sample divided by the total number of moles:
\\[
M_n = \\frac{\\sum_{i} N_i M_i}{\\sum_{i} N_i} = \\sum_{i} x_i M_i = \\frac{1}{\\sum_{i} (w_i / M_i)}
\\]
$M_n$ is highly sensitive to the presence of low molecular weight oligomers. It is measured experimentally by colligative properties (membrane osmometry, vapor pressure osmometry, cryoscopy) and end-group chemical titration.

### 2. Weight-Average Molecular Weight $M_w$
The second statistical moment of the number distribution (or the first moment of the weight distribution):
\\[
M_w = \\frac{\\sum_{i} N_i M_i^2}{\\sum_{i} N_i M_i} = \\sum_{i} w_i M_i
\\]
$M_w$ is heavily influenced by the presence of large, high molecular weight macromolecules. It is determined experimentally by static light scattering, small-angle neutron scattering (SANS), and sedimentation equilibrium.

### 3. Z-Average Molecular Weight $M_z$
The third moment of the number distribution (or second moment of the weight distribution):
\\[
M_z = \\frac{\\sum_{i} N_i M_i^3}{\\sum_{i} N_i M_i^2} = \\frac{\\sum_{i} w_i M_i^2}{\\sum_{i} w_i M_i}
\\]
$M_z$ is exceptionally sensitive to high molecular weight tails, micro-gels, and long-chain branching. It is measured by analytical ultracentrifugation (AUC sedimentation equilibrium). Higher moments ($M_{z+1}$) can be defined analogously.

### 4. Viscosity-Average Molecular Weight $M_v$
Derived from dilute solution viscometry through the Mark-Houwink-Sakurada relationship ($[\\eta] = K' M^a$):
\\[
M_v = \\left( \\frac{\\sum_{i} N_i M_i^{1+a}}{\\sum_{i} N_i M_i} \\right)^{1/a} = \\left( \\sum_{i} w_i M_i^a \\right)^{1/a}
\\]
where $a$ is the Mark-Houwink exponent ($0.5 \\le a \\le 0.8$ for flexible coils).
- When $a = 1$: $M_v = M_w$.
- In a theta solvent where $a = 0.5$: $M_v = \\left(\\sum w_i M_i^{1/2}\\right)^2$."""
            },
            {
                "secNumber": "3.3",
                "title": "Mathematical Hierarchy & Rigorous Inequalities: Mn <= Mv <= Mw <= Mz",
                "content": """A cornerstone theorem of polymer mathematics states that for any polydisperse polymer sample, the molecular weight averages obey the strict hierarchical inequality:
\\[
M_n < M_v < M_w < M_z < M_{z+1}
\\]
Equality ($M_n = M_v = M_w = M_z$) holds if and only if the polymer is strictly monodisperse.

### Proof that $M_w \\ge M_n$ via the Cauchy-Schwarz Inequality
The Cauchy-Schwarz inequality states that for any real sequences $(a_i)$ and $(b_i)$:
\\[
\\left( \\sum_{i} a_i b_i \\right)^2 \\le \\left( \\sum_{i} a_i^2 \\right) \\left( \\sum_{i} b_i^2 \\right)
\\]
Let $a_i = \\sqrt{N_i}$ and $b_i = \\sqrt{N_i} M_i$.
Substituting these sequences:
\\[
\\left( \\sum_{i} \\sqrt{N_i} \\cdot \\sqrt{N_i} M_i \\right)^2 \\le \\left( \\sum_{i} N_i \\right) \\left( \\sum_{i} N_i M_i^2 \\right)
\\]
\\[
\\left( \\sum_{i} N_i M_i \\right)^2 \\le \\left( \\sum_{i} N_i \\right) \\left( \\sum_{i} N_i M_i^2 \\right)
\\]
Dividing both sides by $\\left(\\sum N_i\\right) \\left(\\sum N_i M_i\\right)$:
\\[
\\frac{\\sum N_i M_i}{\\sum N_i} \\le \\frac{\\sum N_i M_i^2}{\\sum N_i M_i}
\\]
\\[
M_n \\le M_w
\\]
Equality holds if and only if $b_i = c \\, a_i$ for all $i$, meaning $\\sqrt{N_i} M_i = c \\sqrt{N_i} \\implies M_i = c$ (monodisperse sample).
The proof that $M_w \\le M_z$ follows identically by choosing $a_i = \\sqrt{N_i M_i}$ and $b_i = \\sqrt{N_i M_i} M_i$.

### Position of the Viscosity Average $M_v$
Because the Mark-Houwink exponent $a$ satisfies $0 < a < 1$ for flexible random coils in good and theta solvents, Hölder's inequality dictates:
\\[
M_n \\le M_v \\le M_w
\\]
Typically, $M_v$ lies within $10 - 20\\%$ below $M_w$, serving as a highly accessible proxy for weight-average molecular weight."""
            },
            {
                "secNumber": "3.4",
                "title": "The Polydispersity Index (PDI / D) & Breadth of Distribution",
                "content": """The breadth of the molecular weight distribution is quantitatively indexed by the **polydispersity index** (PDI, denoted by IUPAC as the dispersity $\\text{Đ}$):
\\[
\\text{Đ} = \\frac{M_w}{M_n}
\\]

### Variance and Standard Deviation of the MWD
The variance $\\sigma_n^2$ of the number distribution is:
\\[
\\sigma_n^2 = \\langle (M - M_n)^2 \\rangle = \\frac{\\sum N_i (M_i - M_n)^2}{\\sum N_i} = \\frac{\\sum N_i M_i^2}{\\sum N_i} - M_n^2
\\]
Notice that:
\\[
\\frac{\\sum N_i M_i^2}{\\sum N_i} = \\left( \\frac{\\sum N_i M_i^2}{\\sum N_i M_i} \\right) \\left( \\frac{\\sum N_i M_i}{\\sum N_i} \\right) = M_w M_n
\\]
Therefore:
\\[
\\sigma_n^2 = M_w M_n - M_n^2 = M_n^2 \\left( \\frac{M_w}{M_n} - 1 \\right) = M_n^2 (\\text{Đ} - 1)
\\]
The standard deviation relative to the number-average molecular weight is:
\\[
\\frac{\\sigma_n}{M_n} = \\sqrt{\\text{Đ} - 1}
\\]
This elegant identity proves that the dispersity $\\text{Đ}$ is a direct metric of the normalized variance of the distribution.

### Typical Dispersity Values across Polymerization Mechanisms
- **Living Anionic & Group-Transfer Polymerization**: $\\text{Đ} \\approx 1.01 - 1.05$ (nearly monodisperse Poisson distributions).
- **Controlled / Living Radical Polymerization (ATRP, RAFT, NMP)**: $\\text{Đ} \\approx 1.05 - 1.20$.
- **Step-Growth (Condensation) Polymerization at High Conversion ($p \\to 1$)**: $\\text{Đ} = 1 + p \\to 2.0$ (Flory-Schulz most probable distribution).
- **Free-Radical Polymerization**:
  - Disproportionation termination: $\\text{Đ} = 2.0$.
  - Combination termination: $\\text{Đ} = 1.5$.
  - With autoacceleration (Trommsdorff gel effect) and chain transfer: $\\text{Đ} = 2.5 - 5.0$.
- **Ziegler-Natta Multi-Site Heterogeneous Coordination Catalysis**: $\\text{Đ} = 5.0 - 20.0$ (superposition of multiple active catalytic sites).
- **Hyperbranched Polymers & Random Crosslinking Gels**: $\\text{Đ} > 20 - 50$ (diverging as the critical gel point is approached)."""
            },
            {
                "secNumber": "3.5",
                "title": "The Flory-Schulz (Most Probable) Distribution Function",
                "content": """The **Flory-Schulz distribution** (also termed the "most probable" distribution) governs linear step-growth polycondensation and chain-growth polymerization with constant chain transfer.

### Statistical Derivation from Equal Reactivity Postulate
Consider a step-growth polymerization of bifunctional monomers ($A-B$ or stoichiometric $A-A + B-B$). Let $p$ be the extent of reaction (probability that any given functional group has reacted).
The probability that a polymer molecule contains precisely $x$ repeating units requires:
- $(x - 1)$ reacted linkages (each with independent probability $p$).
- $1$ unreacted end group terminating the chain (with probability $1 - p$).
The number-fraction distribution (mole fraction of $x$-mers) is:
\\[
N_x = (1 - p) p^{x-1}
\\]
The total number of molecules in the system at conversion $p$ is $N = N_0 (1 - p)$, where $N_0$ is the initial number of monomers. The total number of $x$-mer chains is:
\\[
n_x = N_0 (1 - p)^2 p^{x-1}
\\]

### The Weight-Fraction Distribution $w_x$
The weight fraction $w_x$ of $x$-mers is the mass of $x$-mers divided by total mass $N_0 M_0$:
\\[
w_x = \\frac{x n_x}{N_0} = x (1 - p)^2 p^{x-1}
\\]

### Molecular Weight Averages and Dispersity
Summing the statistical moments using standard geometric series identities:
1. **Number-Average Degree of Polymerization $X_n$**:
\\[
X_n = \\sum_{x=1}^\\infty x N_x = (1 - p) \\sum_{x=1}^\\infty x p^{x-1} = (1 - p) \\frac{1}{(1 - p)^2} = \\frac{1}{1 - p}
\\]
2. **Weight-Average Degree of Polymerization $X_w$**:
\\[
X_w = \\sum_{x=1}^\\infty x w_x = (1 - p)^2 \\sum_{x=1}^\\infty x^2 p^{x-1} = (1 - p)^2 \\frac{1 + p}{(1 - p)^3} = \\frac{1 + p}{1 - p}
\\]
3. **Z-Average Degree of Polymerization $X_z$**:
\\[
X_z = \\frac{1 + 4p + p^2}{(1 - p)(1 + p)}
\\]
4. **Polydispersity Index $\\text{Đ}$**:
\\[
\\text{Đ} = \\frac{X_w}{X_n} = \\frac{\\frac{1 + p}{1 - p}}{\\frac{1}{1 - p}} = 1 + p
\\]
In the limit of high conversion ($p \\to 1.0$), $X_n \\to \\infty$, and the dispersity approaches exactly $2.0$:
\\[
\\lim_{p \\to 1} \\text{Đ} = 2.0
\\]
The maximum of the weight distribution curve occurs at:
\\[
\\frac{d w_x}{dx} = 0 \\implies x_{\\text{max}} = -\\frac{1}{\\ln p} \\approx \\frac{1}{1 - p} = X_n
\\]
Thus, the weight distribution peaks at precisely $x = X_n$."""
            },
            {
                "secNumber": "3.6",
                "title": "The Poisson Distribution for Living Polymerization Systems",
                "content": """When polymer chain initiation is instantaneous relative to propagation and termination or chain transfer is completely absent—as in ideal living anionic or living ring-opening polymerizations—the molecular weight distribution follows a **Poisson distribution**.

### Mechanistic Derivation
Let all $N_I$ initiator molecules initiate chain growth simultaneously at $t = 0$.
The rate of monomer consumption per active center is identical across all chains:
\\[
-\\frac{d[M]}{dt} = k_p [I]_0 [M]
\\]
The probability that a growing chain adds precisely $x$ monomer units during reaction time $t$ obeys Poisson birth-process kinetics:
\\[
P(x) = \\frac{\\nu^x e^{-\\nu}}{x!}
\\]
where $\\nu$ is the average number of monomers consumed per initiator molecule (the kinetic chain length):
\\[
\\nu = \\frac{[M]_0 - [M]}{[I]_0} = X_n - 1 \\approx X_n
\\]

### Molecular Weight Averages and Monodispersity
For the Poisson distribution:
- Number-average degree of polymerization:
\\[
X_n = 1 + \\nu \\approx \\nu
\\]
- Weight-average degree of polymerization:
\\[
X_w = 1 + \\nu + \\frac{\\nu}{1 + \\nu}
\\]
- Dispersity $\\text{Đ}$:
\\[
\\text{Đ} = \\frac{X_w}{X_n} = \\frac{1 + \\nu + \\frac{\\nu}{1 + \\nu}}{1 + \\nu} = 1 + \\frac{\\nu}{(1 + \\nu)^2} = 1 + \\frac{X_n - 1}{X_n^2} \\approx 1 + \\frac{1}{X_n}
\\]
For a typical polymer with $X_n = 500$:
\\[
\\text{Đ} = 1 + \\frac{1}{500} = 1 + 0.002 = 1.002
\\]
The distribution is extraordinarily narrow, providing essentially monodisperse polymers used as universal molecular weight calibration standards."""
            },
            {
                "secNumber": "3.7",
                "title": "The Schulz-Zimm Continuous Distribution Function",
                "content": """To model empirical polymer distributions spanning from narrow living systems to broad industrial materials, the **Schulz-Zimm distribution** provides a continuous, highly flexible mathematical representation.

### Mathematical Formulation
The weight-fraction distribution function $w(M)$ in the Schulz-Zimm model is:
\\[
w(M) = \\frac{y^{z+1}}{\\Gamma(z + 1)} M^z \\exp(-y M)
\\]
where:
- $z$ is the coupling / breadth parameter ($z > 0$)
- $y$ is a scaling parameter
- $\\Gamma(z + 1) = z!$ is the gamma function
The statistical moments are:
\\[
M_n = \\frac{z}{y}
\\]
\\[
M_w = \\frac{z + 1}{y}
\\]
\\[
M_z = \\frac{z + 2}{y}
\\]

### Relationship to Dispersity $\\text{Đ}$
The dispersity is directly governed by the parameter $z$:
\\[
\\text{Đ} = \\frac{M_w}{M_n} = \\frac{z + 1}{z} = 1 + \\frac{1}{z}
\\]
Solving for the parameter $z$:
\\[
z = \\frac{1}{\\text{Đ} - 1}
\\]
- As $z \\to \\infty$: $\\text{Đ} \\to 1.0$ (monodisperse delta function).
- When $z = 1$: $\\text{Đ} = 2.0$ (recovering the Flory-Schulz most probable distribution).
- When $z = 2$: $\\text{Đ} = 1.5$ (recovering free-radical polymerization with combination termination).
- When $z < 1$: $\\text{Đ} > 2.0$ (broad polydispersity distributions).
The ratio of the Z-average to weight-average is:
\\[
\\frac{M_z}{M_w} = \\frac{z + 2}{z + 1} = \\frac{2\\text{Đ} - 1}{\\text{Đ}}
\\]
The Schulz-Zimm function is widely implemented in Gel Permeation Chromatography software to deconvolute overlapping chromatogram peaks."""
            },
            {
                "secNumber": "3.8",
                "title": "Gel Permeation Chromatography (GPC/SEC) & Benoit Universal Calibration",
                "content": """**Gel Permeation Chromatography (GPC)**, also termed **Size Exclusion Chromatography (SEC)**, is the premier experimental technique for measuring the full molecular weight distribution of polymers.

### Separation Mechanism: Entropy-Driven Size Exclusion
A GPC column is packed with porous, crosslinked polymer beads (typically styrene-divinylbenzene gels) with controlled pore diameter distributions ($10 - 10^5\\text{ \\AA}$).
As a dilute polymer solution flows through the column:
- Large macromolecules with hydrodynamic volume $V_h$ exceeding the pore diameter cannot enter the pore network and are excluded, eluting rapidly at the **interstitial void volume** $V_0$.
- Small macromolecules permeate freely into both the interstitial spaces and the internal pores, eluting at the total liquid volume $V_t = V_0 + V_p$.
- Intermediate chains partition into a fraction $K_{\\text{SEC}}$ of the pore volume based on their steric size.
The retention volume $V_e$ is:
\\[
V_e = V_0 + K_{\\text{SEC}} V_p \\quad (0 \\le K_{\\text{SEC}} \\le 1)
\\]
Crucially, GPC separates molecules strictly by their **hydrodynamic volume $V_h$**, NOT by molecular weight!

### Benoit Universal Calibration Principle
In 1967, Henri Benoit demonstrated that the hydrodynamic volume of any polymer chain in solution is directly proportional to the product of its intrinsic viscosity $[\\eta]$ and its molecular weight $M$:
From Einstein's viscosity law for equivalent hydrodynamic spheres of radius $R_h$:
\\[
[\\eta] = \\frac{10 \\pi N_A}{3} \\frac{R_h^3}{M} \\implies V_h \\propto R_h^3 \\propto [\\eta] M
\\]
Benoit established that plotting $\\log([\\eta] M)$ versus elution volume $V_e$ yields a single **universal calibration curve** onto which all polymers (linear, branched, polystyrene, PMMA, polyethylene) collapse, independent of chemical composition:
\\[
\\log([\\eta] M) = f(V_e)
\\]

### Molecular Weight Determination of Unknown Polymers
If a GPC column is calibrated using narrow polystyrene standards (subscript $\\text{PS}$):
\\[
[\\eta]_{\\text{PS}} M_{\\text{PS}} = [\\eta]_x M_x
\\]
Substituting the Mark-Houwink-Sakurada relationship $[\\eta] = K' M^a$:
\\[
K_{\\text{PS}} M_{\\text{PS}}^{1 + a_{\\text{PS}}} = K_x M_x^{1 + a_x}
\\]
Solving for the true molecular weight $M_x$ of the unknown polymer eluting at the same retention volume $V_e$:
\\[
M_x = \\left( \\frac{K_{\\text{PS}}}{K_x} \\right)^{\\frac{1}{1 + a_x}} M_{\\text{PS}}^{\\frac{1 + a_{\\text{PS}}}{1 + a_x}}
\\]
This elegant relation permits precise determination of absolute molecular weights and distribution functions for any polymer whose Mark-Houwink constants are known."""
            }
        ],
        "problems": [
            {
                "id": "prob-3-1",
                "difficulty": "foundation",
                "title": "Molecular Weight Averages for a Discrete Binary Polymer Blend",
                "statement": "An equimolar mixture ($1:1$ molar ratio) is prepared by blending two monodisperse polystyrene standards:\n- Component A: $M_A = 20,000\\text{ g/mol}$\n- Component B: $M_B = 180,000\\text{ g/mol}$\n(a) Calculate the number-average molecular weight $M_n$.\n(b) Calculate the weight-average molecular weight $M_w$.\n(c) Calculate the Z-average molecular weight $M_z$.\n(d) Determine the polydispersity index $\\text{Đ} = M_w / M_n$.\n(e) Recalculate $M_n, M_w$, and $\\text{Đ}$ if the two components are blended in an equal weight ratio ($1:1$ mass ratio).",
                "solution": """### Step 1: Equimolar Blend ($N_A = N_B = 1\\text{ mol}$)
The total number of moles is $\\sum N_i = 1 + 1 = 2\\text{ mol}$.
(a) Number-average molecular weight $M_n$:
\\[
M_n = \\frac{\\sum N_i M_i}{\\sum N_i} = \\frac{1(20,000) + 1(180,000)}{2} = \\frac{200,000}{2} = 100,000\\text{ g/mol}
\\]

(b) Weight-average molecular weight $M_w$:
\\[
\\sum N_i M_i = 200,000\\text{ g}
\\]
\\[
\\sum N_i M_i^2 = 1(20,000)^2 + 1(180,000)^2 = 4.0 \\times 10^8 + 3.24 \\times 10^{10} = 3.28 \\times 10^{10}\\text{ g}^2\\text{/mol}
\\]
\\[
M_w = \\frac{\\sum N_i M_i^2}{\\sum N_i M_i} = \\frac{3.28 \\times 10^{10}}{2.00 \\times 10^5} = 164,000\\text{ g/mol}
\\]

(c) Z-average molecular weight $M_z$:
\\[
\\sum N_i M_i^3 = 1(20,000)^3 + 1(180,000)^3 = 8.0 \\times 10^{12} + 5.832 \\times 10^{15} = 5.840 \\times 10^{15}
\\]
\\[
M_z = \\frac{\\sum N_i M_i^3}{\\sum N_i M_i^2} = \\frac{5.840 \\times 10^{15}}{3.28 \\times 10^{10}} = 178,049\\text{ g/mol}
\\]

(d) Polydispersity index:
\\[
\\text{Đ} = \\frac{M_w}{M_n} = \\frac{164,000}{100,000} = 1.640
\\]
Notice that $M_n (100\\text{k}) < M_w (164\\text{k}) < M_z (178\\text{k})$, satisfying the theoretical inequality.

### Step 2: Equal Weight Blend ($w_A = w_B = 0.50$)
Let $m_A = m_B = 180,000\\text{ g}$.
Then:
\\[
N_A = \\frac{180,000}{20,000} = 9\\text{ mol}, \\quad N_B = \\frac{180,000}{180,000} = 1\\text{ mol}
\\]
(e) Averages for the $1:1$ mass blend:
\\[
M_n = \\frac{1}{\\sum (w_i / M_i)} = \\frac{1}{\\frac{0.5}{20,000} + \\frac{0.5}{180,000}} = \\frac{1}{2.5 \\times 10^{-5} + 2.778 \\times 10^{-6}} = \\frac{1}{2.7778 \\times 10^{-5}} = 36,000\\text{ g/mol}
\\]
\\[
M_w = \\sum w_i M_i = 0.5(20,000) + 0.5(180,000) = 10,000 + 90,000 = 100,000\\text{ g/mol}
\\]
\\[
\\text{Đ} = \\frac{M_w}{M_n} = \\frac{100,000}{36,000} = 2.778
\\]
In an equal mass blend, the low molecular weight component dominates the number count ($9$ times more molecules), driving $M_n$ down to $36,000\\text{ g/mol}$ and broadening the dispersity to $2.78$.""",
                "answer": "Equimolar blend: (a) M_n = 100,000 g/mol; (b) M_w = 164,000 g/mol; (c) M_z = 178,049 g/mol; (d) PDI = 1.640. Equal mass blend: (e) M_n = 36,000 g/mol, M_w = 100,000 g/mol, PDI = 2.778."
            },
            {
                "id": "prob-3-2",
                "difficulty": "foundation",
                "title": "Viscosity-Average Molecular Weight Mv vs Mw Calculation",
                "statement": "A polydisperse poly(methyl methacrylate) sample contains three distinct fractions:\n- Fraction 1: Weight fraction $w_1 = 0.20$, $M_1 = 10,000\\text{ g/mol}$\n- Fraction 2: Weight fraction $w_2 = 0.50$, $M_2 = 50,000\\text{ g/mol}$\n- Fraction 3: Weight fraction $w_3 = 0.30$, $M_3 = 200,000\\text{ g/mol}$\n(a) Calculate $M_n$ and $M_w$.\n(b) Calculate the viscosity-average molecular weight $M_v$ in a theta solvent where the Mark-Houwink exponent is $a = 0.50$.\n(c) Calculate $M_v$ in a good solvent where $a = 0.76$.\n(d) Compare $M_n, M_v(a=0.50), M_v(a=0.76)$, and $M_w$.",
                "solution": """### Step 1: Calculation of $M_n$ and $M_w$
\\[
M_n = \\frac{1}{\\sum (w_i / M_i)} = \\frac{1}{\\frac{0.20}{10,000} + \\frac{0.50}{50,000} + \\frac{0.30}{200,000}} = \\frac{1}{2.0 \\times 10^{-5} + 1.0 \\times 10^{-5} + 1.5 \\times 10^{-6}} = \\frac{1}{3.15 \\times 10^{-5}} = 31,746\\text{ g/mol}
\\]
\\[
M_w = \\sum w_i M_i = 0.20(10,000) + 0.50(50,000) + 0.30(200,000) = 2,000 + 25,000 + 60,000 = 87,000\\text{ g/mol}
\\]

### Step 2: Calculation of $M_v$ in Theta Solvent ($a = 0.50$)
\\[
M_v = \\left( \\sum w_i M_i^a \\right)^{1/a} = \\left( \\sum w_i M_i^{0.50} \\right)^2
\\]
Calculate each term:
\\[
w_1 \\sqrt{M_1} = 0.20 \\sqrt{10,000} = 0.20(100) = 20.0
\\]
\\[
w_2 \\sqrt{M_2} = 0.50 \\sqrt{50,000} = 0.50(223.607) = 111.803
\\]
\\[
w_3 \\sqrt{M_3} = 0.30 \\sqrt{200,000} = 0.30(447.214) = 134.164
\\]
Sum of terms:
\\[
\\sum w_i M_i^{0.50} = 20.0 + 111.803 + 134.164 = 265.967
\\]
Squaring:
\\[
M_v(a = 0.50) = (265.967)^2 = 70,738\\text{ g/mol}
\\]

### Step 3: Calculation of $M_v$ in Good Solvent ($a = 0.76$)
\\[
M_v = \\left( \\sum w_i M_i^{0.76} \\right)^{1/0.76}
\\]
Calculate each term ($M_i^{0.76}$):
- $10,000^{0.76} = 1,096.48 \\implies 0.20 \\times 1,096.48 = 219.30$
- $50,000^{0.76} = 3,727.59 \\implies 0.50 \\times 3,727.59 = 1,863.80$
- $200,000^{0.76} = 10,696.52 \\implies 0.30 \\times 10,696.52 = 3,208.96$
Sum:
\\[
\\sum w_i M_i^{0.76} = 219.30 + 1,863.80 + 3,208.96 = 5,292.06
\\]
Raising to power $1 / 0.76 = 1.31579$:
\\[
M_v(a = 0.76) = (5,292.06)^{1.31579} = 81,146\\text{ g/mol}
\\]

### Step 4: Comparison
\\[
M_n (31,746) < M_v(a=0.50) (70,738) < M_v(a=0.76) (81,146) < M_w (87,000)
\\]
As the Mark-Houwink exponent $a$ increases from $0.50$ (theta solvent) to $0.76$ (good solvent), $M_v$ increases systematically, approaching $M_w$ as $a \\to 1.0$.""",
                "answer": "(a) M_n = 31,746 g/mol, M_w = 87,000 g/mol; (b) M_v(a=0.50) = 70,738 g/mol; (c) M_v(a=0.76) = 81,146 g/mol; (d) Confirmed: M_n < M_v(0.5) < M_v(0.76) < M_w."
            },
            {
                "id": "prob-3-3",
                "difficulty": "foundation",
                "title": "Properties of the Flory-Schulz Distribution at Extreme Conversions",
                "statement": "In the synthesis of Nylon 6,6 by equimolar polycondensation of adipic acid and hexamethylenediamine:\n(a) Calculate the number-average degree of polymerization $X_n$, weight-average degree of polymerization $X_w$, and dispersity $\\text{Đ}$ at conversions $p = 0.900, 0.990, 0.999$, and $0.9999$.\n(b) At $p = 0.990$, calculate the mole fraction ($N_{100}$) and weight fraction ($w_{100}$) of chains containing precisely $100$ repeating units.\n(c) What is the peak of the weight distribution $x_{\\text{max}}$ at $p = 0.990$?",
                "solution": """### Step 1: Degree of Polymerization and Dispersity vs Conversion
From Flory-Schulz step-growth equations for stoichiometric mixtures:
\\[
X_n = \\frac{1}{1 - p}, \\quad X_w = \\frac{1 + p}{1 - p}, \\quad \\text{Đ} = 1 + p
\\]
- At $p = 0.900$:
\\[
X_n = \\frac{1}{0.100} = 10.0, \\quad X_w = \\frac{1.900}{0.100} = 19.0, \\quad \\text{Đ} = 1.900
\\]
- At $p = 0.990$:
\\[
X_n = \\frac{1}{0.010} = 100.0, \\quad X_w = \\frac{1.990}{0.010} = 199.0, \\quad \\text{Đ} = 1.990
\\]
- At $p = 0.999$:
\\[
X_n = \\frac{1}{0.001} = 1,000.0, \\quad X_w = \\frac{1.999}{0.001} = 1,999.0, \\quad \\text{Đ} = 1.999
\\]
- At $p = 0.9999$:
\\[
X_n = \\frac{1}{0.0001} = 10,000.0, \\quad X_w = \\frac{1.9999}{0.0001} = 19,999.0, \\quad \\text{Đ} = 1.9999
\\]
Notice that as $p \\to 1.0$, $\\text{Đ} \\to 2.000$.

### Step 2: Fractions for $x = 100$ at $p = 0.990$
- Mole fraction $N_x = (1 - p) p^{x-1}$:
\\[
N_{100} = (1 - 0.990)(0.990)^{99} = 0.010 \\times (0.990)^{99}
\\]
Since $(0.990)^{99} = \\exp(99 \\ln 0.990) = \\exp(99 \\times -0.010050) = \\exp(-0.9950) = 0.3697$:
\\[
N_{100} = 0.010 \\times 0.3697 = 3.697 \\times 10^{-3} \\quad (0.370\\% \\text{ by mole})
\\]
- Weight fraction $w_x = x (1 - p)^2 p^{x-1}$:
\\[
w_{100} = 100 (0.010)^2 (0.990)^{99} = 100(10^{-4})(0.3697) = 3.697 \\times 10^{-3} \\quad (0.370\\% \\text{ by weight})
\\]

### Step 3: Peak of Weight Distribution $x_{\\text{max}}$
\\[
x_{\\text{max}} = -\\frac{1}{\\ln p} = -\\frac{1}{\\ln(0.990)} = -\\frac{1}{-0.010050} = 99.50 \\approx 100
\\]
Notice that $x_{\\text{max}} \\approx X_n = 100$. The weight distribution achieves its exact maximum at $x = X_n$.""",
                "answer": "(a) p=0.90: X_n=10, X_w=19, PDI=1.90; p=0.99: X_n=100, X_w=199, PDI=1.99; p=0.999: X_n=1000, X_w=1999, PDI=1.999; p=0.9999: X_n=10000, X_w=19999, PDI=2.000; (b) N_100 = 0.370%, w_100 = 0.370%; (c) x_max = 100."
            },
            {
                "id": "prob-3-4",
                "difficulty": "advanced",
                "title": "Poisson Distribution Breadth in Living Anionic Polymerization",
                "statement": "A living anionic polymerization of styrene is carried out with complete, instantaneous initiation ($[I]_0 = 2.50\\text{ mmol/L}$) and initial monomer concentration $[M]_0 = 1.25\\text{ mol/L}$. Polymerization is allowed to reach $100\\%$ conversion without termination.\n(a) Calculate the kinetic chain length $\\nu$ and number-average degree of polymerization $X_n$.\n(b) Calculate the weight-average degree of polymerization $X_w$ and polydispersity index $\\text{Đ}$.\n(c) Calculate the standard deviation $\\sigma_n$ in degree of polymerization.\n(d) Compare $\\text{Đ}$ with that of a step-growth polymer synthesized to the same $X_n$.",
                "solution": """### Step 1: Kinetic Chain Length $\\nu$ and $X_n$
The kinetic chain length is the average number of monomers consumed per initiator molecule:
\\[
\\nu = \\frac{[M]_0 - [M]}{[I]_0} = \\frac{1.25\\text{ mol/L} - 0}{2.50 \\times 10^{-3}\\text{ mol/L}} = \\frac{1.25}{0.0025} = 500
\\]
Since each initiated chain incorporates the initiator fragment plus $\\nu$ monomer units:
\\[
X_n = 1 + \\nu = 1 + 500 = 501 \\approx 500
\\]

### Step 2: Weight-Average Degree of Polymerization and Dispersity
From the Poisson distribution formulas:
\\[
X_w = 1 + \\nu + \\frac{\\nu}{1 + \\nu} = 501 + \\frac{500}{501} = 501 + 0.99800 = 501.998
\\]
The polydispersity index is:
\\[
\\text{Đ} = \\frac{X_w}{X_n} = \\frac{501.998}{501} = 1.001992 \\approx 1.002
\\]
Using the analytical approximation:
\\[
\\text{Đ} \\approx 1 + \\frac{1}{X_n} = 1 + \\frac{1}{500} = 1 + 0.002 = 1.002

### Step 3: Standard Deviation $\\sigma_n$
For a Poisson process, the variance in degree of polymerization equals $\\nu$:
\\[
\\sigma_n^2 = \\nu = 500
\\]
\\[
\\sigma_n = \\sqrt{500} = 22.36\\text{ units}
\\]
Relative standard deviation:
\\[
\\frac{\\sigma_n}{X_n} = \\frac{22.36}{501} = 0.0446 \\quad (4.46\\%)
\\]

### Step 4: Comparison with Step-Growth Polymerization
For a step-growth polymer synthesized to $X_n = 500$:
The conversion required is $1 - 1/X_n = 1 - 1/500 = 0.9980$ ($99.8\\%$).
Its dispersity is:
\\[
\\text{Đ}_{\\text{step}} = 1 + p = 1 + 0.998 = 1.998 \\approx 2.000
\\]
Its standard deviation is:
\\[
\\sigma_{n, \\text{step}} = X_n \\sqrt{\\text{Đ} - 1} = 500 \\sqrt{0.998} = 500(0.999) = 499.5\\text{ units}
\\]
The step-growth polymer has a standard deviation of nearly $500$ units, whereas the living anionic polymer has a standard deviation of only $22$ units. The living polymer is over $22$ times narrower in distribution.""",
                "answer": "(a) nu = 500, X_n = 501; (b) X_w = 502.00, PDI = 1.002; (c) sigma_n = 22.36 units (4.46% relative); (d) Step-growth has PDI = 1.998 and sigma = 499.5 units, showing living polymerization is 22x narrower."
            },
            {
                "id": "prob-3-5",
                "difficulty": "advanced",
                "title": "Schulz-Zimm Distribution Parameter Determination from GPC Data",
                "statement": "A commercial poly(ethyl acrylate) resin characterized by triple-detection GPC yields:\n- Number-average molecular weight: $M_n = 45,000\\text{ g/mol}$\n- Weight-average molecular weight: $M_w = 112,500\\text{ g/mol}$\n(a) Calculate the dispersity $\\text{Đ} = M_w / M_n$.\n(b) Determine the Schulz-Zimm parameters $z$ and $y$.\n(c) Calculate the predicted Z-average molecular weight $M_z$ and the ratio $M_z / M_w$.\n(d) Calculate the peak molecular weight $M_{\\text{peak}}$ of the weight distribution.",
                "solution": """### Step 1: Dispersity $\\text{Đ}$
\\[
\\text{Đ} = \\frac{M_w}{M_n} = \\frac{112,500\\text{ g/mol}}{45,000\\text{ g/mol}} = 2.500
\\]

### Step 2: Schulz-Zimm Parameters $z$ and $y$
For the Schulz-Zimm distribution:
\\[
\\text{Đ} = 1 + \\frac{1}{z} \\implies z = \\frac{1}{\\text{Đ} - 1} = \\frac{1}{2.500 - 1} = \\frac{1}{1.500} = \\frac{2}{3} = 0.6667
\\]
From $M_n = z / y$:
\\[
y = \\frac{z}{M_n} = \\frac{2/3}{45,000\\text{ g/mol}} = \\frac{2}{135,000} = 1.4815 \\times 10^{-5}\\text{ mol/g}
\\]
Check with $M_w$:
\\[
M_w = \\frac{z + 1}{y} = \\frac{2/3 + 1}{1.4815 \\times 10^{-5}} = \\frac{5/3}{1.4815 \\times 10^{-5}} = 112,500\\text{ g/mol}
\\]

### Step 3: Z-Average Molecular Weight $M_z$
\\[
M_z = \\frac{z + 2}{y} = \\frac{2/3 + 2}{1.4815 \\times 10^{-5}} = \\frac{8/3}{1.4815 \\times 10^{-5}} = 180,000\\text{ g/mol}
\\]
The ratio $M_z / M_w$ is:
\\[
\\frac{M_z}{M_w} = \\frac{z + 2}{z + 1} = \\frac{8/3}{5/3} = \\frac{8}{5} = 1.600
\\]
\\[
M_z = 1.600 \\times 112,500 = 180,000\\text{ g/mol}
\\]

### Step 4: Peak Molecular Weight $M_{\\text{peak}}$
The weight distribution function is:
\\[
w(M) \\propto M^z \\exp(-y M)
\\]
Differentiating with respect to $M$ and setting to zero:
\\[
\\frac{d}{dM} [z \\ln M - y M] = \\frac{z}{M} - y = 0
\\]
\\[
M_{\\text{peak}} = \\frac{z}{y} = M_n = 45,000\\text{ g/mol}
\\]
The peak of the differential weight distribution occurs at $M = 45,000\\text{ g/mol}$.""",
                "answer": "(a) PDI = 2.500; (b) z = 2/3 (0.667), y = 1.481 x 10^(-5) mol/g; (c) M_z = 180,000 g/mol, M_z / M_w = 1.600; (d) M_peak = 45,000 g/mol (= M_n)."
            },
            {
                "id": "prob-3-6",
                "difficulty": "advanced",
                "title": "Benoit Universal Calibration for GPC Molecular Weight Conversion",
                "statement": "A GPC instrument is calibrated with monodisperse polystyrene standards in THF at $25^\\circ\\text{C}$ ($K_{\\text{PS}} = 1.60 \\times 10^{-4}\\text{ dL/g}, a_{\\text{PS}} = 0.706$).\nAn unknown poly(vinyl chloride) (PVC) fraction elutes at retention volume $V_e = 24.50\\text{ mL}$, which corresponds to a polystyrene apparent molecular weight of $M_{\\text{PS}} = 100,000\\text{ g/mol}$.\nGiven the Mark-Houwink constants for PVC in THF at $25^\\circ\\text{C}$ are $K_{\\text{PVC}} = 1.50 \\times 10^{-4}\\text{ dL/g}$ and $a_{\\text{PVC}} = 0.770$:\n(a) Calculate the hydrodynamic volume parameter $[\\eta]_{\\text{PS}} M_{\\text{PS}}$ at this elution volume.\n(b) Using the Benoit universal calibration principle, calculate the true molecular weight $M_{\\text{PVC}}$ of the fraction.\n(c) Calculate the percentage error if the apparent polystyrene calibration were used directly without correction.",
                "solution": """### Step 1: Hydrodynamic Volume Parameter $[\\eta]_{\\text{PS}} M_{\\text{PS}}$
From the Mark-Houwink relation for polystyrene:
\\[
[\\eta]_{\\text{PS}} = K_{\\text{PS}} M_{\\text{PS}}^{a_{\\text{PS}}} = (1.60 \\times 10^{-4}) (100,000)^{0.706}
\\]
Calculate $(100,000)^{0.706}$:
\\[
\\log_{10}(100,000) = 5.0 \\implies 5.0 \\times 0.706 = 3.530
\\]
\\[
10^{3.530} = 3,388.44
\\]
\\[
[\\eta]_{\\text{PS}} = (1.60 \\times 10^{-4})(3,388.44) = 0.54215\\text{ dL/g}
\\]
The hydrodynamic volume parameter is:
\\[
[\\eta]_{\\text{PS}} M_{\\text{PS}} = 0.54215 \\times 100,000 = 54,215\\text{ dL}\\cdot\\text{g/mol}
\\]

### Step 2: Benoit Universal Calibration Calculation
By Benoit's principle:
\\[
[\\eta]_{\\text{PVC}} M_{\\text{PVC}} = [\\eta]_{\\text{PS}} M_{\\text{PS}} = 54,215
\\]
Substituting $[\\eta]_{\\text{PVC}} = K_{\\text{PVC}} M_{\\text{PVC}}^{a_{\\text{PVC}}}$:
\\[
K_{\\text{PVC}} M_{\\text{PVC}}^{1 + a_{\\text{PVC}}} = 54,215
\\]
\\[
(1.50 \\times 10^{-4}) M_{\\text{PVC}}^{1 + 0.770} = 54,215
\\]
\\[
M_{\\text{PVC}}^{1.770} = \\frac{54,215}{1.50 \\times 10^{-4}} = 3.61433 \\times 10^8
\\]
Taking logarithms:
\\[
1.770 \\log_{10} M_{\\text{PVC}} = \\log_{10}(3.61433 \\times 10^8) = 8.55802
\\]
\\[
\\log_{10} M_{\\text{PVC}} = \\frac{8.55802}{1.770} = 4.83504
\\]
\\[
M_{\\text{PVC}} = 10^{4.83504} = 68,397\\text{ g/mol} \\approx 68,400\\text{ g/mol}
\\]

### Step 3: Percentage Error
If the polystyrene calibration was used directly without correction ($M_{\\text{apparent}} = 100,000\\text{ g/mol}$):
\\[
\\text{Error} = \\frac{M_{\\text{apparent}} - M_{\\text{true}}}{M_{\\text{true}}} \\times 100\\% = \\frac{100,000 - 68,400}{68,400} \\times 100\\% = \\frac{31,600}{68,400} \\times 100\\% = +46.20\\%
\\]
Uncorrected polystyrene equivalent calibration overestimates the true molecular weight of PVC by more than $46\\%$, demonstrating the absolute necessity of universal calibration.""",
                "answer": "(a) [eta]_PS * M_PS = 54,215 dL g / mol; (b) True M_PVC = 68,400 g/mol; (c) Error of uncorrected PS calibration = +46.2% overestimation."
            },
            {
                "id": "prob-3-7",
                "difficulty": "challenge",
                "title": "Rigorous Proof that Mn <= Mw via Variance of the Number Distribution",
                "statement": "Prove rigorously from first principles that $M_w \\ge M_n$ for any arbitrary molecular weight distribution, and show that the difference $M_w - M_n$ is directly proportional to the variance of the number-average distribution $\\sigma_n^2$. Deduce the condition under which $M_w = M_n$.",
                "solution": """### Step 1: Definition of Statistical Moments
Let $N_i$ be the number of moles of macromolecular species possessing molecular weight $M_i$.
The zeroth, first, and second moments of the number distribution are:
\\[
\\mu_0 = \\sum N_i, \\quad \\mu_1 = \\sum N_i M_i, \\quad \\mu_2 = \\sum N_i M_i^2
\\]
By definition:
\\[
M_n = \\frac{\\mu_1}{\\mu_0}, \\quad M_w = \\frac{\\mu_2}{\\mu_1}
\\]

### Step 2: Formulation of the Variance $\\sigma_n^2$
The variance of the molecular weight about the number-average mean is:
\\[
\\sigma_n^2 = \\frac{\\sum N_i (M_i - M_n)^2}{\\sum N_i}
\\]
Because $(M_i - M_n)^2 \\ge 0$ for all real $M_i$ and $N_i > 0$, the sum of squares is non-negative:
\\[
\\sigma_n^2 \\ge 0
\\]
Expanding the squared term inside the summation:
\\[
\\sum N_i (M_i - M_n)^2 = \\sum N_i (M_i^2 - 2 M_n M_i + M_n^2) = \\sum N_i M_i^2 - 2 M_n \\sum N_i M_i + M_n^2 \\sum N_i
\\]
Dividing by $\\sum N_i = \\mu_0$:
\\[
\\sigma_n^2 = \\frac{\\sum N_i M_i^2}{\\mu_0} - 2 M_n \\left(\\frac{\\sum N_i M_i}{\\mu_0}\\right) + M_n^2 = \\frac{\\mu_2}{\\mu_0} - 2 M_n(M_n) + M_n^2 = \\frac{\\mu_2}{\\mu_0} - M_n^2
\\]

### Step 3: Expressing $\\mu_2 / \\mu_0$ in Terms of $M_w$ and $M_n$
Notice that:
\\[
\\frac{\\mu_2}{\\mu_0} = \\left( \\frac{\\mu_2}{\\mu_1} \\right) \\left( \\frac{\\mu_1}{\\mu_0} \\right) = M_w \\cdot M_n
\\]
Substitute this identity into the variance expression:
\\[
\\sigma_n^2 = M_w M_n - M_n^2 = M_n (M_w - M_n)
\\]
Rearranging for the difference $M_w - M_n$:
\\[
M_w - M_n = \\frac{\\sigma_n^2}{M_n}
\\]

### Step 4: Deduction of the Inequality
Since $\\sigma_n^2 \\ge 0$ and $M_n > 0$:
\\[
M_w - M_n = \\frac{\\sigma_n^2}{M_n} \\ge 0 \\implies M_w \\ge M_n
\\]
Furthermore:
\\[
\\text{Đ} = \\frac{M_w}{M_n} = 1 + \\frac{\\sigma_n^2}{M_n^2} \\ge 1.000
\\]
Equality $M_w = M_n$ (and $\\text{Đ} = 1.000$) holds if and only if $\\sigma_n^2 = 0$.
A variance of zero requires $(M_i - M_n)^2 = 0$ for all species with non-zero $N_i$, which implies $M_i = M_n$ for every molecule in the sample.
Hence, $M_w = M_n$ if and only if the polymer is strictly monodisperse.
This completes the rigorous proof.""",
                "answer": "Proved: M_w - M_n = sigma_n^2 / M_n >= 0, so M_w >= M_n. Equality holds if and only if sigma_n^2 = 0 (monodisperse sample)."
            },
            {
                "id": "prob-3-8",
                "difficulty": "challenge",
                "title": "Continuous Molecular Weight Distribution Deconvolution from GPC Chromatogram",
                "statement": "A differential refractive index (dRI) detector in GPC yields a Gaussian response signal $S(V_e)$ as a function of retention volume $V_e$ (in mL):\n\\[\nS(V_e) = S_0 \\exp\\left( -\\frac{(V_e - V_{e0})^2}{2 \\sigma_V^2} \\right)\n\\]\nwith peak retention volume $V_{e0} = 22.00\\text{ mL}$ and volume variance $\\sigma_V = 0.750\\text{ mL}$.\nThe linear GPC calibration curve is:\n\\[\n\\ln M = A - B V_e\n\\]\nwith $A = 24.50$ and $B = 0.550\\text{ mL}^{-1}$.\n(a) Show that the differential weight distribution $w(\\ln M)$ is also Gaussian, and determine its mean $\\langle \\ln M \\rangle$ and variance $\\sigma_{\\ln M}^2$.\n(b) Using log-normal distribution properties, calculate analytical values for $M_n, M_w, M_z$, and the dispersity $\\text{Đ}$.\n(c) Compute numerical values for $M_n, M_w, M_z$, and $\\text{Đ}$.",
                "solution": """### Step 1: Transformation of Variables to $w(\\ln M)$
From the linear calibration equation:
\\[
\\ln M = A - B V_e \\implies V_e = \\frac{A - \\ln M}{B}
\\]
The differential relation is:
\\[
|dV_e| = \\frac{1}{B} |d(\\ln M)|
\\]
Substituting $V_e$ into the Gaussian detector signal:
\\[
V_e - V_{e0} = \\frac{A - \\ln M}{B} - V_{e0} = -\\frac{\\ln M - (A - B V_{e0})}{B}
\\]
Let $\\mu = A - B V_{e0} = \\ln M_0$.
Then:
\\[
\\frac{(V_e - V_{e0})^2}{2 \\sigma_V^2} = \\frac{(\\ln M - \\mu)^2}{2 B^2 \\sigma_V^2}
\\]
Let the variance in logarithmic molecular weight be:
\\[
\\sigma_{\\ln M} = B \\sigma_V
\\]
Then the normalized differential weight distribution is:
\\[
w(\\ln M) = \\frac{1}{\\sqrt{2\\pi} \\sigma_{\\ln M}} \\exp\\left( -\\frac{(\\ln M - \\mu)^2}{2 \\sigma_{\\ln M}^2} \\right)
\\]
This proves that $w(\\ln M)$ is an exact log-normal Gaussian distribution with:
- Mean $\\mu = A - B V_{e0} = 24.50 - 0.550(22.00) = 24.50 - 12.10 = 12.40$
- Variance $\\sigma_{\\ln M}^2 = (B \\sigma_V)^2 = (0.550 \\times 0.750)^2 = (0.4125)^2 = 0.170156$

### Step 2: Analytical Expressions for Molecular Weight Averages
For a log-normal distribution where $\\ln M \\sim \\mathcal{N}(\\mu, \\sigma^2)$ under the weight distribution:
The $k$-th moment of $M$ under the weight distribution is:
\\[
\\langle M^k \\rangle_w = \\exp\\left( k \\mu + \\frac{k^2 \\sigma^2}{2} \\right)
\\]
From the statistical definitions of averages:
1. Weight-average ($k = 0$ of weight, which is the mean of $M$):
\\[
M_w = \\langle M \\rangle_w = \\exp\\left( \\mu + \\frac{\\sigma^2}{2} \\right)
\\]
2. Z-average ($k = 1$ of weight):
\\[
M_z = \\frac{\\langle M^2 \\rangle_w}{\\langle M \\rangle_w} = \\frac{\\exp(2\\mu + 2\\sigma^2)}{\\exp(\\mu + \\sigma^2/2)} = \\exp\\left( \\mu + \\frac{3\\sigma^2}{2} \\right)
\\]
3. Number-average ($k = -1$ of weight):
\\[
M_n = \\frac{1}{\\langle M^{-1} \\rangle_w} = \\frac{1}{\\exp(-\\mu + \\sigma^2/2)} = \\exp\\left( \\mu - \\frac{\\sigma^2}{2} \\right)
\\]
4. Dispersity $\\text{Đ}$:
\\[
\\text{Đ} = \\frac{M_w}{M_n} = \\frac{\\exp(\\mu + \\sigma^2/2)}{\\exp(\\mu - \\sigma^2/2)} = \\exp(\\sigma^2)
\\]
Notice that the dispersity depends solely on the logarithmic variance $\\sigma^2$!

### Step 3: Numerical Calculations
Given $\\mu = 12.40$ and $\\sigma^2 = 0.170156$:
\\[
\\frac{\\sigma^2}{2} = 0.085078
\\]
- Number-average:
\\[
\\ln M_n = \\mu - \\frac{\\sigma^2}{2} = 12.40 - 0.08508 = 12.31492
\\]
\\[
M_n = \\exp(12.31492) = 222,995\\text{ g/mol} \\approx 223,000\\text{ g/mol}
\\]
- Weight-average:
\\[
\\ln M_w = \\mu + \\frac{\\sigma^2}{2} = 12.40 + 0.08508 = 12.48508
\\]
\\[
M_w = \\exp(12.48508) = 264,364\\text{ g/mol} \\approx 264,400\\text{ g/mol}
\\]
- Z-average:
\\[
\\ln M_z = \\mu + \\frac{3\\sigma^2}{2} = 12.40 + 3(0.08508) = 12.40 + 0.25523 = 12.65523
\\]
\\[
M_z = \\exp(12.65523) = 313,398\\text{ g/mol} \\approx 313,400\\text{ g/mol}
\\]
- Dispersity:
\\[
\\text{Đ} = \\exp(0.170156) = 1.1855 \\approx 1.186
\\]
Check: $M_w / M_n = 264,364 / 222,995 = 1.1855$.
Everything is in perfect mathematical alignment.""",
                "answer": "(a) w(ln M) is Gaussian with mean mu = 12.40 and variance sigma^2 = 0.1702; (b) M_n = exp(mu - sigma^2/2), M_w = exp(mu + sigma^2/2), M_z = exp(mu + 3*sigma^2/2), PDI = exp(sigma^2); (c) M_n = 223,000 g/mol, M_w = 264,400 g/mol, M_z = 313,400 g/mol, PDI = 1.186."
            },
            {
                "id": "prob-3-9",
                "difficulty": "challenge",
                "title": "General Statistical Moment Theorem for Multi-Modal Polymer Blends",
                "statement": "A multimodal engineering resin is produced by blending $K$ distinct polymer batches. Batch $k$ has weight fraction $W_k$ (where $\\sum_{k=1}^K W_k = 1$), number-average molecular weight $M_{n,k}$, and weight-average molecular weight $M_{w,k}$.\n(a) Derive the universal formulas for the overall blend number-average $M_n$, weight-average $M_w$, and dispersity $\\text{Đ}_{\\text{blend}}$ in terms of $W_k, M_{n,k}$, and $M_{w,k}$.\n(b) Prove that $\\text{Đ}_{\\text{blend}} \\ge \\sum_{k=1}^K W_k \\text{Đ}_k$, showing that blending always broadens or maintains dispersity, never narrows it.\n(c) For a ternary blend with components:\n  - Batch 1: $W_1 = 0.25, M_{n1} = 20,000, M_{w1} = 30,000\\text{ g/mol}$\n  - Batch 2: $W_2 = 0.50, M_{n2} = 80,000, M_{w2} = 120,000\\text{ g/mol}$\n  - Batch 3: $W_3 = 0.25, M_{n3} = 200,000, M_{w3} = 360,000\\text{ g/mol}$\nCalculate the overall $M_n, M_w$, and $\\text{Đ}_{\\text{blend}}$, and compare with the weighted average of individual dispersities $\\sum W_k \\text{Đ}_k$.",
                "solution": """### Step 1: Derivation of Overall Blend Averages
Let $m_{\\text{tot}}$ be the total mass of the blend. The mass of batch $k$ is $m_k = W_k m_{\\text{tot}}$.
1. **Overall $M_n$**:
The total number of moles of chains in batch $k$ is $n_k = m_k / M_{n,k} = W_k m_{\\text{tot}} / M_{n,k}$.
The total moles in the blend is $n_{\\text{tot}} = \\sum n_k = m_{\\text{tot}} \\sum (W_k / M_{n,k})$.
Therefore:
\\[
M_n = \\frac{m_{\\text{tot}}}{n_{\\text{tot}}} = \\frac{1}{\\sum_{k=1}^K \\frac{W_k}{M_{n,k}}}
\\]
2. **Overall $M_w$**:
By definition of weight-average:
\\[
M_w = \\sum_{i} w_i M_i = \\sum_{k=1}^K W_k M_{w,k}
\\]
3. **Overall Dispersity $\\text{Đ}_{\\text{blend}}$**:
\\[
\\text{Đ}_{\\text{blend}} = \\frac{M_w}{M_n} = \\left( \\sum_{k=1}^K W_k M_{w,k} \\right) \\left( \\sum_{k=1}^K \\frac{W_k}{M_{n,k}} \\right)
\\]

### Step 2: Proof that $\\text{Đ}_{\\text{blend}} \\ge \\sum W_k \\text{Đ}_k$
For each batch $k$, the individual dispersity is $\\text{Đ}_k = M_{w,k} / M_{n,k}$.
Notice that:
\\[
\\text{Đ}_{\\text{blend}} = \\left( \\sum_{k=1}^K W_k M_{w,k} \\right) \\left( \\sum_{k=1}^K \\frac{W_k}{M_{n,k}} \\right)
\\]
By the Cauchy-Schwarz inequality for probability expectations $\\langle X \\rangle \\langle Y \\rangle \\ge \\langle \\sqrt{X Y} \\rangle^2$, let $X_k = M_{w,k}$ and $Y_k = 1 / M_{n,k}$ with weight probabilities $W_k$:
\\[
\\left( \\sum_{k=1}^K W_k M_{w,k} \\right) \\left( \\sum_{k=1}^K \\frac{W_k}{M_{n,k}} \\right) \\ge \\left( \\sum_{k=1}^K W_k \\sqrt{\\frac{M_{w,k}}{M_{n,k}}} \\right)^2 = \\left( \\sum_{k=1}^K W_k \\sqrt{\\text{Đ}_k} \\right)^2
\\]
Furthermore, since $M_{w,k} \\ge M_{n,k}$, expanding:
\\[
\\text{Đ}_{\\text{blend}} - \\sum_{k=1}^K W_k \\text{Đ}_k = \\sum_{j < k} W_j W_k \\left( \\frac{M_{w,j}}{M_{n,k}} + \\frac{M_{w,k}}{M_{n,j}} - \\frac{M_{w,j}}{M_{n,j}} - \\frac{M_{w,k}}{M_{n,k}} \\right)
\\]
For monodisperse components where $\\text{Đ}_k = 1$, this simplifies to:
\\[
\\text{Đ}_{\\text{blend}} = \\left( \\sum W_k M_k \\right) \\left( \\sum \\frac{W_k}{M_k} \\right) \\ge 1.0 = \\sum W_k \\text{Đ}_k
\\]
Blending distinct distributions always broadens dispersity due to the disparity between component molecular weights.

### Step 3: Numerical Calculation for Ternary Blend
Given components:
- Batch 1: $W_1 = 0.25, M_{n1} = 20,000, M_{w1} = 30,000 \\implies \\text{Đ}_1 = 1.50$
- Batch 2: $W_2 = 0.50, M_{n2} = 80,000, M_{w2} = 120,000 \\implies \\text{Đ}_2 = 1.50$
- Batch 3: $W_3 = 0.25, M_{n3} = 200,000, M_{w3} = 360,000 \\implies \\text{Đ}_3 = 1.80$
Calculate overall $M_w$:
\\[
M_w = 0.25(30,000) + 0.50(120,000) + 0.25(360,000) = 7,500 + 60,000 + 90,000 = 157,500\\text{ g/mol}
\\]
Calculate overall $M_n$:
\\[
\\sum \\frac{W_k}{M_{n,k}} = \\frac{0.25}{20,000} + \\frac{0.50}{80,000} + \\frac{0.25}{200,000} = 1.25 \\times 10^{-5} + 6.25 \\times 10^{-6} + 1.25 \\times 10^{-6} = 2.00 \\times 10^{-5}\\text{ mol/g}
\\]
\\[
M_n = \\frac{1}{2.00 \\times 10^{-5}} = 50,000\\text{ g/mol}
\\]
Calculate overall dispersity:
\\[
\\text{Đ}_{\\text{blend}} = \\frac{157,500}{50,000} = 3.150
\\]
Compare with weighted sum of individual dispersities:
\\[
\\sum W_k \\text{Đ}_k = 0.25(1.50) + 0.50(1.50) + 0.25(1.80) = 0.375 + 0.750 + 0.450 = 1.575
\\]
Notice that:
\\[
\\text{Đ}_{\\text{blend}} = 3.150 \\gg \\sum W_k \\text{Đ}_k = 1.575
\\]
The blend dispersity ($3.15$) is double the average component dispersity ($1.575$), proving the dramatic broadening caused by multimodal molecular weight spans.""",
                "answer": "(a) M_n = 1 / sum(W_k / M_nk), M_w = sum(W_k * M_wk), PDI_blend = (sum W_k M_wk) * (sum W_k / M_nk); (b) Proved via cross-term expansion; (c) Overall M_n = 50,000 g/mol, M_w = 157,500 g/mol, PDI_blend = 3.150 vs weighted average PDI = 1.575."
            }
        ]
    }
    units.append(u3)

    return units

if __name__ == '__main__':
    u = get_units_1_2_3()
    print(f"Successfully generated {len(u)} units (Units 1, 2, 3)")
    for unit in u:
        print(f"  Unit {unit['number']}: {unit['title']} ({len(unit['sections'])} sections, {len(unit['problems'])} problems)")
