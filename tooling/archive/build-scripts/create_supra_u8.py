"""
create_supra_u8.py
Creates Unit 8 data dictionary for Supramolecular Chemistry:
Amphiphiles, Surfactants, Micelles & Vesicular Aggregates
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_8():
    sections = [
        {
            "secNumber": "8.1",
            "title": "Surface Activity & The Gibbs Adsorption Isotherm",
            "content": """**Amphiphiles** (from the Greek *amphi*, meaning "both", and *philos*, meaning "loving") are molecules possessing two distinct regions of opposite affinity within a single covalent framework: a hydrophilic, polar "headgroup" and a hydrophobic, non-polar hydrocarbon "tail".

### Surface Activity and Surface Tension Reduction
Water possesses an anomalously high surface tension ($\\gamma_0 \\approx 72.8\\text{ mN/m}$ at $20^\\circ\\text{C}$) due to cohesive hydrogen-bonding networks among bulk water molecules.
- When an amphiphile is dissolved in water, the hydrophobic tail disrupts liquid water's hydrogen bonds, creating an unfavorable cavity free energy penalty ($+T\\Delta S_{\\text{cav}}$).
- To minimize free energy, amphiphilic molecules spontaneously adsorb at the air-water interface, orienting their polar heads into the aqueous subphase while projecting their hydrophobic tails into the gas phase.
- Adsorption replaces high-energy water-air contacts with lower-energy hydrocarbon-air contacts, causing a sharp decrease in surface tension $\\gamma$. Substances that produce this surface tension reduction are termed **surfactants** (surface-active agents).

### The Gibbs Adsorption Isotherm
Josiah Willard Gibbs derived the fundamental thermodynamic equation relating surface tension depression to the surface concentration of adsorbed solute:
\\[
-d\\gamma = \\sum_i \\Gamma_i d\\mu_i
\\]
where $\\Gamma_i$ is the **surface excess concentration** (moles of component $i$ per unit area of interface, in $\\text{mol/m}^2$) and $\\mu_i = \\mu_i^\circ + RT \\ln a_i$ is the chemical potential.
For a dilute solution of a non-ionic surfactant or an ionic surfactant with excess inert background electrolyte:
\\[
\\Gamma = -\\frac{1}{RT} \\left( \\frac{\\partial \\gamma}{\\partial \\ln C} \\right)_T = -\\frac{C}{RT} \\left( \\frac{\\partial \\gamma}{\\partial C} \\right)_T
\\]
For a $1:1$ ionic surfactant (e.g., sodium dodecyl sulfate, SDS) in pure water in the absence of added salt, both the surfactant ion and its counterion must adsorb simultaneously to maintain electroneutrality:
\\[
\\Gamma = -\\frac{1}{2 RT} \\left( \\frac{\\partial \\gamma}{\\partial \\ln C} \\right)_T
\\]
At high concentrations near the critical micelle concentration, the interface reaches saturation coverage ($\\Gamma_{\\max}$), from which the **effective cross-sectional area per molecule** at the interface, $a_0$, is directly obtained:
\\[
a_0 = \\frac{1}{N_A \\Gamma_{\\max}}
\\]"""
        },
        {
            "secNumber": "8.2",
            "title": "Classification of Surfactants: Anionic, Cationic, Zwitterionic & Geminis",
            "content": """Surfactants are classified into four major taxonomic groups based on the electrical nature of their hydrophilic headgroup, plus modern dimeric architectures.

### 1. Anionic Surfactants
The polar headgroup carries a net negative formal charge.
- **Alkyl Sulfates**: Sodium dodecyl sulfate (SDS, $\\text{C}_{12}\\text{H}_{25}\\text{OSO}_3^-\\text{Na}^+$). Widely used in biochemical protein denaturation and detergents.
- **Alkyl Carboxylates (Soaps)**: Sodium stearate, potassium oleate. Sensitive to precipitation by divalent cations ($\text{Ca}^{2+}, \\text{Mg}^{2+}$, "hard water").
- **Linear Alkylbenzene Sulfonates (LAS)**: Sodium dodecylbenzenesulfonate (SDBS). Dominant industrial laundry surfactant.

### 2. Cationic Surfactants
The polar headgroup carries a net positive formal charge.
- **Quaternary Ammonium Salts**: Cetyltrimethylammonium bromide (CTAB, $\\text{C}_{16}\\text{H}_{33}\\text{N}^+(\\text{CH}_3)_3\\text{Br}^-$), benzalkonium chloride.
- Adsorb strongly to negatively charged biological surfaces (cell walls, hair, skin), functioning as potent antiseptics, antimicrobial bactericides, and fabric softeners.

### 3. Non-Ionic Surfactants
The polar headgroup possesses no formal electrical charge, deriving water solubility from dense hydrogen bonding with polyether or polyol motifs.
- **Polyoxyethylene Alkyl Ethers ($\text{C}_n\\text{E}_m$)**: Pentaethylene glycol monododecyl ether ($\text{C}_{12}\\text{E}_5$). Exhibit a lower critical solution temperature (LCST), becoming cloudy upon heating above their **cloud point**.
- **Alkyl Polyglycosides (APGs)** and **Triton X-100**: Non-denaturing surfactants used for membrane protein extraction.

### 4. Zwitterionic (Amphoteric) Surfactants
Contain both positive and negative charges on the same molecule across physiological $\\text{pH}$.
- **Betaines**: Cocamidopropyl betaine (CAPB). Highly mild to biological tissues, low eye irritation.
- **Lecithins (Phosphatidylcholines)**: Natural phospholipids of cell membranes containing a cationic choline and an anionic phosphate diester.

### 5. Gemini (Dimeric) Surfactants
Consist of two conventional amphiphilic moieties (two hydrophobic tails and two polar heads) chemically linked at or near the headgroups by a rigid or flexible spacer group:
\\[
\\text{Tail}_1-\\text{Head}_1-\\text{Spacer}-\\text{Head}_2-\\text{Tail}_2
\\]
- Exhibit critical micelle concentrations $10\\text{ to }100$ times lower than their monomeric equivalents.
- Dramatically higher surface efficiency and superior rheological thickening properties."""
        },
        {
            "secNumber": "8.3",
            "title": "The Critical Micelle Concentration (CMC): Experimental Determination",
            "content": """When the concentration of an amphiphile in aqueous solution exceeds a well-defined threshold, the air-water interface becomes fully saturated with surfactant molecules. Additional surfactant can no longer dissolve as free monomers without severe thermodynamic penalty; instead, the monomers spontaneously assemble into colloidal aggregates termed **micelles**. This threshold is the **Critical Micelle Concentration (CMC)**.

### Physical Manifestation at the CMC
Virtually every physical property of the solution displays an abrupt discontinuity or slope change at the CMC:
1. **Surface Tension ($\\gamma$)**: Drops linearly with $\\ln C$ up to the CMC, where it abruptly levels off to an essentially constant plateau ($\gamma \\approx \\text{constant}$), because the chemical potential of free monomer is pinned.
2. **Specific Conductivity ($\\kappa$)**: For ionic surfactants, $\\kappa$ increases steeply below the CMC (due to fully dissociated mobile ions). Above the CMC, the slope drops sharply because counterions condense onto the highly charged micellar surface, reducing net ionic mobility.
3. **Osmotic Pressure ($\Pi$)**: Rises linearly below the CMC, then flattens above it because adding monomer increases the aggregate count by only $1/N_{\\text{agg}}$ units.
4. **Turbidity and Light Scattering**: Negligible below the CMC, then increases rapidly above the CMC due to Rayleigh scattering from micellar colloids.

### Pyrene Fluorescence Probe Spectroscopy
Kalyanasundaram and Thomas developed a sensitive fluorometric method to determine CMC using the solvatochromic probe **pyrene**:
- In the emission spectrum of pyrene, the ratio of the intensity of the first vibronic 0-0 band ($I_1$ at $\\lambda \\approx 373\\text{ nm}$) to the third vibronic band ($I_3$ at $\\lambda \\approx 384\\text{ nm}$) is exquisitely sensitive to local dielectric polarity:
  - In polar water: $I_1 / I_3 \\approx 1.80 - 1.90$.
  - In non-polar hydrocarbon environments: $I_1 / I_3 \\approx 0.60 - 0.90$.
- Below the CMC, pyrene senses bulk water ($I_1 / I_3 \\approx 1.85$).
- At the CMC, pyrene partitions into the newly formed hydrophobic hydrocarbon cores of the micelles, causing $I_1 / I_3$ to plummet sharply to $\\approx 1.1 - 1.3$.
- Plotting $I_1 / I_3$ versus surfactant concentration yields a sharp sigmoidal transition whose inflection point precisely marks the CMC."""
        },
        {
            "secNumber": "8.4",
            "title": "Thermodynamics of Micellization: Mass-Action & Phase-Separation Models",
            "content": """Two primary thermodynamic models describe the micellization equilibrium: the **phase-separation model** and the **mass-action model**.

### 1. Phase-Separation Model
Treats micelles of aggregation number $N$ as a distinct pseudo-phase separated from the aqueous solution.
- For a **non-ionic surfactant**, micellization represents phase condensation:
\\[
\\Delta G_{\\text{mic}}^\circ = RT \\ln(\\text{CMC})
\\]
where CMC is expressed as a mole fraction $X_{\\text{CMC}} = \\text{CMC} / [\\text{H}_2\\text{O}] = \\text{CMC} / 55.5\\text{ M}$.
- For a **$1:1$ ionic surfactant**, where a fraction $\\beta$ of counterions are condensed onto the micellar Stern layer:
\\[
\\Delta G_{\\text{mic}}^\circ = (1 + \\beta) RT \\ln X_{\\text{CMC}}
\\]
where $\\beta$ (the degree of counterion binding) typically ranges from $0.60\\text{ to }0.85$.

### 2. Mass-Action Model
Treats micellization as a dynamic multiple chemical equilibrium:
\\[
N\\,\\text{S}^- + m\\,\\text{M}^+ \\xrightleftharpoons{K_{\\text{mic}}} [\\text{S}_N \\text{M}_m]^{(N-m)-}
\\]
where $N$ is the aggregation number, $m$ is the number of bound counterions, and $\\beta = m / N$.
The equilibrium constant is:
\\[
K_{\\text{mic}} = \\frac{[\\text{Micelle}]}{[\\text{S}^-]^N [\\text{M}^+]^m}
\\]
Taking the $N$-th root yields the free energy per mole of surfactant monomer, which converges identically to the phase-separation expression in the limit of large aggregation number ($N > 50$).

### Enthalpic and Entropic Components
From the Gibbs-Helmholtz relation:
\\[
\\Delta H_{\\text{mic}}^\circ = -T^2 \\left( \\frac{\\partial (\\Delta G_{\\text{mic}}^\circ / T)}{\\partial T} \\right)_P = -R T^2 \\left( \\frac{\\partial \\ln X_{\\text{CMC}}}{\\partial T} \\right)_P
\\]
- At room temperature ($25^\\circ\\text{C}$), micellization of hydrocarbon surfactants in water is **predominantly entropy-driven**:
\\[
\\Delta H_{\\text{mic}}^\circ \\approx 0 \\text{ to } +5\\text{ kJ/mol}, \\quad \\Delta S_{\\text{mic}}^\circ > +50\\text{ J/(mol}\\cdot\\text{K)}
\\]
The driving force is the hydrophobic release of structured ice-like water clathrate cages surrounding the hydrocarbon tails.
- As temperature increases, $\\Delta H_{\\text{mic}}^\circ$ becomes increasingly negative, reflecting a large negative heat capacity of micellization ($\\Delta C_p^{\\text{mic}} < 0$)."""
        },
        {
            "secNumber": "8.5",
            "title": "The Israelachvili Critical Packing Parameter: Geometric Control",
            "content": """The equilibrium geometry of self-assembled amphiphilic aggregates (spheres, cylinders, vesicles, planar bilayers, inverted phases) is dictated by the **Critical Packing Parameter ($P$)**, introduced by Jacob Israelachvili, David Mitchell, and Barry Ninham in 1976.

### Definition of the Packing Parameter
The dimensionless packing parameter $P$ is defined by:
\\[
P = \\frac{v}{a_0 \\, l_c}
\\]
where:
- **$v$**: The effective volume of the hydrophobic hydrocarbon chain ($v \\approx [27.4 + 26.9 \\, n_c]\\text{ Å}^3$ for an $n_c$-carbon alkane tail).
- **$a_0$**: The optimal equilibrium surface area occupied per polar headgroup at the aggregate interface. Governed by a balance between repulsive forces (electrostatic repulsion, steric clash, hydration) and attractive forces (interfacial tension $\\gamma$).
- **$l_c$**: The maximum effective length of the fully extended hydrocarbon chain (Tanford formula: $l_c \\approx [1.5 + 1.265 \\, n_c]\\text{ Å}$).

### Aggregate Morphology as a Function of $P$
The magnitude of $P$ reflects the effective geometric shape of the amphiphile:
1. **$P < 1/3$ (Truncated Cone with Wide Base)**:
   - Headgroup area $a_0$ is very large compared to tail volume.
   - Aggregate: **Spherical Micelles** (e.g., SDS in dilute salt-free water, single-chain lysophospholipids).
2. **$1/3 < P < 1/2$ (Truncated Cone)**:
   - Moderate headgroup repulsion.
   - Aggregate: **Cylindrical or Wormlike Micelles** (e.g., SDS in $0.5\\text{ M }\\text{NaCl}$, CTAB with sodium salicylate).
3. **$1/2 < P < 1$ (Truncated Wedge)**:
   - Smaller headgroup area or two hydrophobic chains.
   - Aggregate: **Flexible Bilayers and Vesicles / Liposomes** (e.g., dialkyl surfactants, dimyristoylphosphatidylcholine, DMPC).
4. **$P \\approx 1$ (Cylinder)**:
   - Headgroup area matches the cross-sectional area of the tail.
   - Aggregate: **Planar Lamellar Bilayers ($L_\\alpha$)** (e.g., dipalmitoylphosphatidylcholine, DPPC).
5. **$P > 1$ (Inverted Truncated Cone)**:
   - Hydrophobic tail is bulkier than the headgroup.
   - Aggregate: **Inverted Micelles and Reversed Hexagonal Phases ($H_{\\text{II}}$)** (e.g., phosphatidylethanolamine, AOT in isooctane)."""
        },
        {
            "secNumber": "8.6",
            "title": "Micelles, Wormlike Micelles, Lamellar Bilayers & Vesicles (Liposomes)",
            "content": """Self-assembled aggregates adopt distinct nanoscopic structures dictated by thermodynamics and the Israelachvili packing parameter.

### Spherical Micelles
- Small, globular aggregates with aggregation numbers $N_{\\text{agg}} \\approx 50 - 100$ and radii equal to the extended surfactant length $l_c$ ($R \\approx 1.5 - 2.5\\text{ nm}$).
- **Structure**:
  - **Hydrophobic Core**: Liquid-like hydrocarbon center completely devoid of water.
  - **Stern Layer (for ionic micelles)**: Compact layer of hydrated ionic headgroups and condensed counterions (thickness $\\approx 0.2 - 0.4\\text{ nm}$).
  - **Gouy-Chapman Diffuse Double Layer**: Region of mobile diffuse counterions extending several nanometers into the bulk solution.

### Wormlike (Giant) Micelles
When counterion screening or organic salts (e.g., sodium salicylate) reduce $a_0$, the packing parameter increases into the range $1/3 < P < 1/2$:
- Spherical micelles grow by one-dimensional elongation into flexible, thread-like cylindrical micelles with contour lengths exceeding several micrometers.
- These cylindrical aggregates entangle like polymer chains, imparting **viscoelasticity** to the fluid ("living polymers" that continuously break and recombine reversibly on millisecond timescales).

### Vesicles and Liposomes
A **vesicle** (or liposome when constructed from biological lipids) is a spherical shell enclosed by one or more concentric amphiphilic bilayers, encapsulating an internal aqueous compartment:
- **Small Unilamellar Vesicles (SUVs)**: Diameter $20 - 50\\text{ nm}$, single bilayer wall. High curvature strain.
- **Large Unilamellar Vesicles (LUVs)**: Diameter $100 - 500\\text{ nm}$. Ideal for pharmaceutical nanomedicine.
- **Multilamellar Vesicles (MLVs)**: Onion-like nested bilayers (diameter $1 - 10\\,\\mu\\text{m}$).
Liposomes are prepared by thin-film lipid hydration followed by probe sonication or polycarbonate membrane extrusion."""
        },
        {
            "secNumber": "8.7",
            "title": "Emulsions and Microemulsions: Bancroft's Rule & Winsor Phase Transitions",
            "content": """Mixtures of immiscible liquids (oil and water) stabilized by surfactants form emulsions or microemulsions.

### Macroemulsions vs Microemulsions
1. **Macroemulsions**:
   - Thermodynamically unstable; kinetic dispersions of droplets with droplet diameters $d \\approx 1 - 20\\,\\mu\\text{m}$.
   - Turbid/milky appearance. Eventually separate into macroscopic oil and water layers via creaming, flocculation, and coalescence.
2. **Microemulsions**:
   - **Thermodynamically stable**, optically transparent, isotropic single phases.
   - Droplet diameters $d \\approx 5 - 50\\text{ nm}$.
   - Form spontaneously when the interfacial tension is driven to near-zero values ($\\gamma \\le 10^{-2} - 10^{-4}\\text{ mN/m}$) using co-surfactants (e.g., medium-chain alcohols).

### Bancroft's Rule
Wilder Dwight Bancroft (1913) formulated the empirical rule:
\\[
\\text{"The phase in which the surfactant is more soluble constitutes the continuous external phase."}
\\]
- If a surfactant is predominantly water-soluble (high HLB), it stabilizes **oil-in-water (O/W)** emulsions.
- If a surfactant is predominantly oil-soluble (low HLB), it stabilizes **water-in-oil (W/O)** emulsions.

### Winsor Phase Transitions
P. A. Winsor (1948) classified the four fundamental thermodynamic phase equilibria of surfactant-oil-water systems:
- **Winsor I (Two-Phase)**: Lower O/W microemulsion phase in equilibrium with an upper excess oil phase ($R < 1$).
- **Winsor II (Two-Phase)**: Upper W/O microemulsion phase in equilibrium with a lower excess water phase ($R > 1$).
- **Winsor III (Three-Phase)**: Middle bicontinuous microemulsion phase in simultaneous equilibrium with both an excess upper oil phase and a lower aqueous phase ($R \\approx 1$, ultralow interfacial tension).
- **Winsor IV (Single-Phase)**: A single, homogeneous, isotropic microemulsion phase formed at high surfactant concentration."""
        },
        {
            "secNumber": "8.8",
            "title": "Biomedical & Nanotechnological Applications: Liposomal Delivery & MCM-41",
            "content": """Amphiphilic self-assembly serves as an indispensable technology across modern nanomedicine, pharmaceutical formulation, and materials science.

### Liposomal Nanomedicine & Drug Delivery
Vesicular aggregates provide unique dual-compartment drug carrier capabilities:
- **Hydrophilic Therapeutics**: Entrapped inside the central aqueous lumen (e.g., doxorubicin in Doxil).
- **Hydrophobic Therapeutics**: Intercalated within the hydrophobic core of the bilayer membrane (e.g., paclitaxel).
- **PEGylation (Stealth Liposomes)**: Grafting polyethylene glycol ($\text{PEG}_{2000}$) chains to the vesicle surface creates a steric hydration barrier that repels plasma opsonins, reducing macrophage clearance by the reticuloendothelial system and extending systemic circulation half-life from 30 minutes to over 45 hours.
- **Enhanced Permeability and Retention (EPR) Effect**: Sub-150 nm liposomes selectively extravasate through the fenestrated vasculature of solid tumors, achieving targeted drug accumulation.

### Template Synthesis of Mesoporous Materials: MCM-41
In 1992, Mobil scientists pioneered **surfactant-templated sol-gel synthesis** to fabricate ordered mesoporous materials:
1. **Liquid Crystal Templating (LCT)**: Cationic cetyltrimethylammonium bromide (CTAB) self-assembles into long cylindrical micelles packed into a 2D hexagonal liquid crystal array ($P6mm$).
2. **Silica Condensation**: Soluble silica precursors (tetraethyl orthosilicate, TEOS, or sodium silicate) coordinate electrostatically to the cationic headgroups at the micellar periphery ($S^+ I^-$ mechanism) and undergo polycondensation.
3. **Surfactant Removal**: Calcination at $550^\\circ\\text{C}$ or solvent extraction burns away the organic surfactant template, leaving a rigid, monolithic inorganic silica framework (**MCM-41**):
   - Uniform, non-intersecting hexagonal cylindrical mesopores (pore diameter $2 - 10\\text{ nm}$).
   - Exceptionally high specific surface area ($S_{\\text{BET}} > 1{,}000\\text{ m}^2/\\text{g}$) and pore volumes $> 1.0\\text{ cm}^3/\\text{g}$.
   - Widely utilized in heterogeneous catalysis, enzyme immobilization, and controlled-release drug delivery."""
        }
    ]

    problems = [
        {
            "probNumber": "8.1",
            "title": "Gibbs Adsorption Isotherm: Surface Excess and Area per Molecule",
            "difficulty": "Foundational",
            "statement": """The surface tension $\\gamma$ of aqueous solutions of a non-ionic surfactant, $\\text{C}_{12}\\text{E}_6$ (hexaethylene glycol monododecyl ether), was measured as a function of concentration $C$ at $T = 298.15\\text{ K}$:
In the concentration range $5.00 \\times 10^{-5}\\text{ M} \\le C \\le 8.50 \\times 10^{-5}\\text{ M}$ (just below the CMC), the surface tension decreases linearly with $\\ln C$ according to:
\\[
\\gamma(C) = 52.40 - 15.60 \\ln(C / C_0) \\quad [\\text{mN/m}]
\\]
where $C_0 = 1.00 \\times 10^{-5}\\text{ M}$.
(a) Using the Gibbs adsorption isotherm for a non-ionic surfactant, derive the expression for the maximum surface excess $\\Gamma_{\\max}$ and calculate its numerical value in $\\text{mol/m}^2$ and in $\\mu\\text{mol/m}^2$.
(b) Calculate the minimum cross-sectional area occupied per surfactant molecule at the saturated air-water interface, $a_0$, in $\\text{Å}^2$ and in $\\text{nm}^2$.
(c) If the clean water surface tension is $\\gamma_0 = 72.00\\text{ mN/m}$ and the surface tension at the CMC ($C = 8.70 \\times 10^{-5}\\text{ M}$) is $\\gamma_{\\text{CMC}} = 31.20\\text{ mN/m}$, calculate the surface pressure $\\Pi_{\\text{CMC}} = \\gamma_0 - \\gamma_{\\text{CMC}}$.""",
            "solution": """### Step 1: Maximum Surface Excess Calculation
For a non-ionic surfactant, the Gibbs adsorption isotherm is:
\\[
\\Gamma = -\\frac{1}{RT} \\left( \\frac{\\partial \\gamma}{\\partial \\ln C} \\right)_T
\\]
From the given empirical equation:
\\[
\\frac{\\partial \\gamma}{\\partial \\ln C} = -15.60\\text{ mN/m} = -15.60 \\times 10^{-3}\\text{ N/m}
\\]
Substitute into Gibbs isotherm with $R = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$ and $T = 298.15\\text{ K}$ ($RT = 2478.96\\text{ J/mol}$):
\\[
\\Gamma_{\\max} = -\\frac{-15.60 \\times 10^{-3}\\text{ N/m}}{2478.96\\text{ J/mol}} = \\frac{15.60 \\times 10^{-3}}{2478.96} = 6.2930 \\times 10^{-6}\\text{ mol/m}^2
\\]
In micromoles per square meter:
\\[
\\Gamma_{\\max} = 6.293\\,\\mu\\text{mol/m}^2
\\]

### Step 2: Minimum Area per Surfactant Molecule ($a_0$)
The area per molecule is:
\\[
a_0 = \\frac{1}{N_A \\Gamma_{\\max}}
\\]
With Avogadro's constant $N_A = 6.02214 \\times 10^{23}\\text{ mol}^{-1}$:
\\[
a_0 = \\frac{1}{(6.02214 \\times 10^{23}\\text{ mol}^{-1}) \\times (6.2930 \\times 10^{-6}\\text{ mol/m}^2)} = \\frac{1}{3.7897 \\times 10^{18}\\text{ molecules/m}^2}
\\]
\\[
a_0 = 2.6387 \\times 10^{-19}\\text{ m}^2 = 0.2639\\text{ nm}^2
\\]
In square angstroms ($1\\text{ nm}^2 = 100\\text{ Å}^2$):
\\[
a_0 = 26.39\\text{ Å}^2
\\]
At interface saturation, each $\\text{C}_{12}\\text{E}_6$ molecule occupies $26.4\\text{ Å}^2$ of area.

### Step 3: Surface Pressure at CMC
The surface pressure $\\Pi$ measures the reduction in surface tension:
\\[
\\Pi_{\\text{CMC}} = \\gamma_0 - \\gamma_{\\text{CMC}} = 72.00\\text{ mN/m} - 31.20\\text{ mN/m} = 40.80\\text{ mN/m}
\\]
The adsorbed surfactant film exerts a two-dimensional lateral surface pressure of $40.8\\text{ mN/m}$ against the interface."""
        },
        {
            "probNumber": "8.2",
            "title": "Conductometric Determination of Ionic Surfactant CMC and Counterion Binding",
            "difficulty": "Foundational",
            "statement": """The specific electrical conductivity $\\kappa$ (in $\\mu\\text{S/cm}$) of aqueous solutions of sodium dodecyl sulfate (SDS, $M_w = 288.38\\text{ g/mol}$) was measured as a function of molar concentration $C$ at $T = 298.15\\text{ K}$:
- Below CMC ($C < \\text{CMC}$): $\\kappa(C) = 71.50 \\times C + 1.20 \\quad [\\mu\\text{S/cm}]$, where $C$ is in $\\text{mM}$.
- Above CMC ($C > \\text{CMC}$): $\\kappa(C) = 24.30 \\times C + 387.20 \\quad [\\mu\\text{S/cm}]$.
(a) Determine the critical micelle concentration (CMC) in $\\text{mM}$ and in $\\text{mol/L}$ from the intersection of the two linear conductivity segments.
(b) The slope below the CMC ($S_1 = 71.50$) represents the molar conductivity of fully dissociated free $\\text{Na}^+$ and $\\text{DS}^-$ ions, whereas the slope above the CMC ($S_2 = 24.30$) represents micellar transport.
Calculate the degree of micellar counterion dissociation $\\alpha = S_2 / S_1$ and the degree of counterion binding $\\beta = 1 - \\alpha$.
(c) If a spherical SDS micelle has an aggregation number $N_{\\text{agg}} = 62$, calculate:
    (i) The number of bound $\\text{Na}^+$ counterions in the Stern layer,
    (ii) The effective net micellar charge $Z_{\\text{mic}}$.""",
            "solution": """### Step 1: CMC from Conductivity Intersection
At the critical micelle concentration, both linear equations yield identical conductivity:
\\[
\\kappa_{\\text{pre}}(C) = \\kappa_{\\text{post}}(C)
\\]
\\[
71.50 \\times C_{\\text{CMC}} + 1.20 = 24.30 \\times C_{\\text{CMC}} + 387.20
\\]
\\[
(71.50 - 24.30) \\times C_{\\text{CMC}} = 387.20 - 1.20
\\]
\\[
47.20 \\times C_{\\text{CMC}} = 386.00
\\]
\\[
C_{\\text{CMC}} = \\frac{386.00}{47.20} = 8.178\\text{ mM} \\approx 8.18\\text{ mM}
\\]
In molarity:
\\[
\\text{CMC} = 8.18 \\times 10^{-3}\\text{ M}
\\]
This matches the literature CMC of pure SDS in water ($8.2\\text{ mM}$).

### Step 2: Degree of Counterion Dissociation and Binding
From Evans' conductometric method:
1. **Fraction of Dissociated Counterions ($\alpha$)**:
\\[
\\alpha = \\frac{S_2}{S_1} = \\frac{24.30}{71.50} = 0.33986 \\approx 0.340
\\]
2. **Degree of Counterion Binding ($\beta$)**:
\\[
\\beta = 1 - \\alpha = 1 - 0.33986 = 0.66014 \\approx 0.660 \\implies 66.0\\%
\\]
Approximately $66\\%$ of the sodium counterions are bound in the Stern layer.

### Step 3: Bound Counterions and Net Charge for $N_{\text{agg}} = 62$
1. **Number of Bound $\\text{Na}^+$ Counterions ($m$)**:
\\[
m = \\beta \\times N_{\\text{agg}} = 0.66014 \\times 62 = 40.93 \\approx 41\\text{ bound }\\text{Na}^+\\text{ ions}
\\]
2. **Effective Net Micellar Charge ($Z_{\\text{mic}}$)**:
Each dodecyl sulfate carries $-1$, and 41 bound sodium ions contribute $+41$:
\\[
Z_{\\text{mic}} = -(N_{\\text{agg}} - m) = -(62 - 41) = -21
\\]
The micelle carries an effective net charge of $-21$ in solution."""
        },
        {
            "probNumber": "8.3",
            "title": "Critical Packing Parameter for SDS vs Dipalmitoylphosphatidylcholine",
            "difficulty": "Foundational",
            "statement": """The Israelachvili critical packing parameter is $P = \\frac{v}{a_0 \\, l_c}$.
Hydrocarbon chain properties are calculated using Tanford's formulas:
- Chain volume: $v = 27.4 + 26.9 \\, n_c\\text{ [Å}^3\\text{]}$
- Maximum chain length: $l_c = 1.5 + 1.265 \\, n_c\\text{ [Å]}$
Evaluate $P$ and predict the aggregate morphology for two surfactants:
1. **Sodium Dodecyl Sulfate (SDS)**:
   Single alkyl tail with $n_c = 12$ carbons, headgroup area $a_0 = 62.0\\text{ Å}^2$ in dilute electrolyte.
2. **Dipalmitoylphosphatidylcholine (DPPC)**:
   Two alkyl tails with $n_c = 16$ carbons each ($2 \\times 16$), headgroup area $a_0 = 65.0\\text{ Å}^2$.
(a) Calculate $v$, $l_c$, and $P$ for SDS. Predict its aggregate shape.
(b) Calculate $v_{\\text{total}}$, $l_c$, and $P$ for DPPC. Predict its aggregate shape.
(c) What happens to the morphology of SDS when $0.5\\text{ M }\\text{NaCl}$ is added, causing electrostatic screening to contract $a_0$ to $38.0\\text{ Å}^2$?""",
            "solution": """### Step 1: SDS Packing Parameter
For $n_c = 12$:
- Volume:
\\[
v = 27.4 + (26.9 \\times 12) = 27.4 + 322.8 = 350.2\\text{ Å}^3
\\]
- Maximum length:
\\[
l_c = 1.5 + (1.265 \\times 12) = 1.5 + 15.18 = 16.68\\text{ Å}
\\]
- Given $a_0 = 62.0\\text{ Å}^2$:
\\[
P_{\\text{SDS}} = \\frac{v}{a_0 l_c} = \\frac{350.2\\text{ Å}^3}{(62.0\\text{ Å}^2) \\times (16.68\\text{ Å})} = \\frac{350.2}{1034.16} = 0.3386 \\approx 0.34
\\]
- **Morphology Prediction**:
  Because $P \\approx 1/3$ ($P \\le 0.339$), SDS forms **spherical micelles** with aggregation number $N_{\\text{agg}} = 4\\pi l_c^3 / (3 v) \\approx 55 - 65$.

### Step 2: DPPC Packing Parameter
For DPPC: two $n_c = 16$ hydrocarbon tails.
- Volume per chain: $v_1 = 27.4 + (26.9 \\times 16) = 27.4 + 430.4 = 457.8\\text{ Å}^3$.
  Total hydrocarbon volume:
\\[
v_{\\text{total}} = 2 \\times 457.8 = 915.6\\text{ Å}^3
\\]
- Maximum chain length (determined by the length of a single chain, $n_c = 16$):
\\[
l_c = 1.5 + (1.265 \\times 16) = 1.5 + 20.24 = 21.74\\text{ Å}
\\]
- Given $a_0 = 65.0\\text{ Å}^2$:
\\[
P_{\\text{DPPC}} = \\frac{v_{\\text{total}}}{a_0 l_c} = \\frac{915.6\\text{ Å}^3}{(65.0\\text{ Å}^2) \\times (21.74\\text{ Å})} = \\frac{915.6}{1413.1} = 0.6479 \\approx 0.65
\\]
- **Morphology Prediction**:
  Because $1/2 < P < 1$ ($P = 0.65$), DPPC forms **vesicles (liposomes) and flexible lamellar bilayers**. Two tails double the hydrophobic volume while the zwitterionic phosphocholine headgroup maintains a compact area, preventing spherical micelle closure.

### Step 3: Effect of High Salt on SDS
When $0.5\\text{ M }\\text{NaCl}$ is added:
Added salt screens electrostatic repulsions between the negative sulfate heads, reducing the optimal headgroup area to $a_0 = 38.0\\text{ Å}^2$:
\\[
P_{\\text{salt}} = \\frac{350.2\\text{ Å}^3}{(38.0\\text{ Å}^2) \\times (16.68\\text{ Å})} = \\frac{350.2}{633.84} = 0.5524 \\approx 0.55
\\]
- **Morphology Transition**:
  Because $P$ shifts from $0.34$ into the range $0.5 < P < 1$, the aggregates transition from spherical micelles into **giant wormlike (cylindrical) micelles** and ultimately into **lamellar sheets/vesicles**, causing a massive increase in solution viscosity."""
        },
        {
            "probNumber": "8.4",
            "title": "Thermodynamics of Micellization: Temperature Dependence & Enthalpy Compensation",
            "difficulty": "Intermediate",
            "statement": """The critical micelle concentration of a non-ionic surfactant ($\text{C}_{10}\\text{E}_5$) was measured in water as a function of temperature:
- At $T_1 = 288.15\\text{ K}$ ($15^\\circ\\text{C}$): $\\text{CMC}_1 = 9.20 \\times 10^{-4}\\text{ M}$
- At $T_2 = 298.15\\text{ K}$ ($25^\\circ\\text{C}$): $\\text{CMC}_2 = 7.50 \\times 10^{-4}\\text{ M}$
- At $T_3 = 313.15\\text{ K}$ ($40^\\circ\\text{C}$): $\\text{CMC}_3 = 6.40 \\times 10^{-4}\\text{ M}$
(a) Express the standard state mole fraction $X_{\\text{CMC}} = \\text{CMC} / 55.5\\text{ M}$ and calculate the standard Gibbs free energy of micellization $\\Delta G_{\\text{mic}}^\circ = RT \\ln X_{\\text{CMC}}$ at all three temperatures.
(b) Using the numerical derivative between $T_1$ and $T_3$, calculate the standard enthalpy of micellization $\\Delta H_{\\text{mic}}^\circ$ and the standard entropy of micellization $\\Delta S_{\\text{mic}}^\circ$ at $T = 298.15\\text{ K}$.
(c) Calculate the heat capacity change of micellization $\\Delta C_{p,\\text{mic}}^\circ = \\frac{\\partial \\Delta H_{\\text{mic}}^\circ}{\\partial T}$ and explain why hydrophobic hydration leads to a large negative heat capacity change.""",
            "solution": """### Step 1: Mole Fractions and Gibbs Free Energies
With $[\\text{H}_2\\text{O}] = 55.50\\text{ M}$:
1. **At $T_1 = 288.15\\text{ K}$**:
\\[
X_1 = \\frac{9.20 \\times 10^{-4}}{55.50} = 1.6577 \\times 10^{-5}
\\]
\\[
\\Delta G_1^\\circ = (8.31446 \\times 288.15) \\times \\ln(1.6577 \\times 10^{-5}) = 2395.81 \\times (-11.0074) = -26{,}371\\text{ J/mol} = -26.37\\text{ kJ/mol}
\\]
2. **At $T_2 = 298.15\\text{ K}$**:
\\[
X_2 = \\frac{7.50 \\times 10^{-4}}{55.50} = 1.3514 \\times 10^{-5}
\\]
\\[
\\Delta G_2^\\circ = (8.31446 \\times 298.15) \\times \\ln(1.3514 \\times 10^{-5}) = 2478.96 \\times (-11.2114) = -27{,}793\\text{ J/mol} = -27.79\\text{ kJ/mol}
\\]
3. **At $T_3 = 313.15\\text{ K}$**:
\\[
X_3 = \\frac{6.40 \\times 10^{-4}}{55.50} = 1.1532 \\times 10^{-5}
\\]
\\[
\\Delta G_3^\\circ = (8.31446 \\times 313.15) \\times \\ln(1.1532 \\times 10^{-5}) = 2603.67 \\times (-11.3702) = -29{,}604\\text{ J/mol} = -29.60\\text{ kJ/mol}
\\]

### Step 2: Enthalpy and Entropy of Micellization at $298.15\text{ K}$
From the van 't Hoff relation:
\\[
\\Delta H_{\\text{mic}}^\circ = -R \\left( \\frac{\\partial \\ln X_{\\text{CMC}}}{\\partial (1/T)} \\right)
\\]
Between $T_1 = 288.15\\text{ K}$ and $T_3 = 313.15\\text{ K}$:
\\[
\\Delta(1/T) = \\frac{1}{313.15} - \\frac{1}{288.15} = 3.19336 \\times 10^{-3} - 3.47041 \\times 10^{-3} = -2.7705 \\times 10^{-4}\\text{ K}^{-1}
\\]
\\[
\\Delta \\ln X = \\ln X_3 - \\ln X_1 = -11.3702 - (-11.0074) = -0.3628
\\]
\\[
\\Delta H_{\\text{mic}}^\circ = -8.31446 \\times \\frac{-0.3628}{-2.7705 \\times 10^{-4}} = -8.31446 \\times 1309.51 = -10{,}888\\text{ J/mol} = -10.89\\text{ kJ/mol}
\\]
The entropy of micellization at $T_2 = 298.15\\text{ K}$ is:
\\[
\\Delta S_{\\text{mic}}^\circ = \\frac{\\Delta H_{\\text{mic}}^\circ - \\Delta G_2^\circ}{T_2} = \\frac{-10{,}888 - (-27{,}793)}{298.15} = \\frac{+16{,}905}{298.15} = +56.70\\text{ J/(mol}\\cdot\\text{K)}
\\]
At $25^\\circ\\text{C}$, the micellization is heavily favored by positive entropy ($+56.7\\text{ J/(mol}\\cdot\\text{K)}$).

### Step 3: Heat Capacity Change ($\Delta C_{p,\text{mic}}^\circ$)
Using the temperature dependence of $\\Delta H_{\\text{mic}}^\circ$:
Direct measurement yields $\\Delta H_1^\circ \\approx -2.5\\text{ kJ/mol}$ and $\\Delta H_3^\circ \\approx -18.5\\text{ kJ/mol}$:
\\[
\\Delta C_{p,\\text{mic}}^\circ = \\frac{\\Delta H_3^\circ - \\Delta H_1^\circ}{T_3 - T_1} = \\frac{-18{,}500 - (-2{,}500)}{313.15 - 288.15} = \\frac{-16{,}000}{25.0} = -640.0\\text{ J/(mol}\\cdot\\text{K)}
\\]
- **Origin of Large Negative Heat Capacity**:
  Dissolving an apolar hydrocarbon tail in water forms an ordered, ice-like clathrate solvation shell with high heat capacity ($C_p$). Upon micelle formation, these ordered water molecules melt into bulk liquid water, destroying the clathrate structure. This massive structural relaxation produces a pronounced negative heat capacity change ($\\Delta C_p < 0$)."""
        },
        {
            "probNumber": "8.5",
            "title": "Pyrene Vibronic Fluorescence Ratio for Micellar Polarity & Partitioning",
            "difficulty": "Intermediate",
            "statement": """Pyrene fluorescence emission was recorded in a series of surfactant solutions at $T = 298.15\\text{ K}$.
The emission intensity ratio of the first to third vibronic peaks, $R = I_1 / I_3$, was measured as a function of surfactant concentration $C$:
- In pure water: $R_w = 1.84$.
- Inside the saturated hydrophobic micellar core: $R_m = 1.15$.
The observed ratio in an intermediate micellar solution conforms to a two-state partition model:
\\[
R_{\\text{obs}} = \\frac{R_w [\\text{Pyr}]_w + R_m [\\text{Pyr}]_m}{[\\text{Pyr}]_w + [\\text{Pyr}]_m} = (1 - f_m) R_w + f_m R_m
\\]
where $f_m = [\\text{Pyr}]_m / [\\text{Pyr}]_{\\text{total}}$ is the fraction of pyrene solubilized inside the micelles.
The partition coefficient between the micellar pseudophase and aqueous water is defined by:
\\[
K_x = \\frac{X_m}{X_w} = \\frac{[\\text{Pyr}]_m / [\\text{Micellar Hydrocarbon}]}{[\\text{Pyr}]_w / [\\text{H}_2\\text{O}]}
\\]
(a) For a solution with $R_{\\text{obs}} = 1.32$, calculate the fraction $f_m$ of pyrene residing inside micelles.
(b) If the solution contains total surfactant concentration $C = 25.0\\text{ mM}$ and the surfactant has $\\text{CMC} = 8.20\\text{ mM}$, calculate the concentration of micellized surfactant $C_{\\text{mic}} = C - \\text{CMC}$.
(c) Given that each micellized surfactant molecule contributes a partial molar volume of $V_m = 0.250\\text{ L/mol}$, determine the partition coefficient $K_x$ and the standard free energy of transfer $\\Delta G_{\\text{trans}}^\circ = -RT \\ln K_x$ from water to the micelle interior.""",
            "solution": """### Step 1: Fraction of Micelle-Bound Pyrene ($f_m$)
From the linear combination formula:
\\[
R_{\\text{obs}} = (1 - f_m) R_w + f_m R_m = R_w - f_m(R_w - R_m)
\\]
Rearranging for $f_m$:
\\[
f_m = \\frac{R_w - R_{\\text{obs}}}{R_w - R_m}
\\]
Substitute values:
\\[
f_m = \\frac{1.84 - 1.32}{1.84 - 1.15} = \\frac{0.52}{0.69} = 0.7536 \\implies 75.36\\%
\\]
Over $75\\%$ of the pyrene probes are partitioned inside the hydrophobic micellar cores.

### Step 2: Micellized Surfactant Concentration
Given:
- $C = 25.0\\text{ mM} = 25.0 \\times 10^{-3}\\text{ M}$
- $\\text{CMC} = 8.20\\text{ mM} = 8.20 \\times 10^{-3}\\text{ M}$
The micellized surfactant concentration is:
\\[
C_{\\text{mic}} = C - \\text{CMC} = 25.0 - 8.20 = 16.80\\text{ mM} = 1.680 \\times 10^{-2}\\text{ M}
\\]

### Step 3: Partition Coefficient and Free Energy of Transfer
The ratio of bound to free pyrene is:
\\[
\\frac{[\\text{Pyr}]_m}{[\\text{Pyr}]_w} = \\frac{f_m}{1 - f_m} = \\frac{0.7536}{1 - 0.7536} = \\frac{0.7536}{0.2464} = 3.0584
\\]
The volume fraction of the micellar phase is:
\\[
\\phi_{\\text{mic}} = C_{\\text{mic}} \\times V_m = (1.680 \\times 10^{-2}\\text{ mol/L}) \\times (0.250\\text{ L/mol}) = 4.20 \\times 10^{-3}
\\]
The molar concentration of water is $[\\text{H}_2\\text{O}] = 55.50\\text{ M}$.
The partition coefficient $K_x$ is:
\\[
K_x = \\left( \\frac{[\\text{Pyr}]_m}{[\\text{Pyr}]_w} \\right) \\times \\left( \\frac{[\\text{H}_2\\text{O}]}{C_{\\text{mic}}} \\right) = 3.0584 \\times \\left( \\frac{55.50}{1.680 \\times 10^{-2}} \\right) = 3.0584 \\times 3{,}303.57 = 1.0104 \\times 10^4
\\]
The standard free energy of transfer at $T = 298.15\\text{ K}$ is:
\\[
\\Delta G_{\\text{trans}}^\\circ = -RT \\ln K_x = -(8.31446 \\times 298.15) \\times \\ln(1.0104 \\times 10^4)
\\]
\\[
\\Delta G_{\\text{trans}}^\\circ = -2478.96 \\times 9.2207 = -22{,}858\\text{ J/mol} = -22.86\\text{ kJ/mol}
\\]
Transferring pyrene from water into the micellar core is exergonic by nearly $-23\\text{ kJ/mol}$ due to the hydrophobic effect."""
        },
        {
            "probNumber": "8.6",
            "title": "Microemulsion Phase Inversion: Winsor Transitions and Salinity Tuning",
            "difficulty": "Intermediate",
            "statement": """An oil-water-surfactant formulation consists of equal volumes of brine ($\\text{H}_2\\text{O} + \\text{NaCl}$) and $n$-octane with an anionic surfactant (sodium di-2-ethylhexyl sulfosuccinate, AOT) at $T = 298.15\\text{ K}$.
As the salinity $S$ (weight percent $\\text{NaCl}$) is increased, the system undergoes a Winsor I $\\rightarrow$ Winsor III $\\rightarrow$ Winsor II phase transition sequence:
- At low salinity ($S < 0.80\\text{ wt}\\%$): Winsor I (O/W microemulsion in equilibrium with excess oil).
- At optimal salinity ($S^* = 1.35\\text{ wt}\\%$): Winsor III (middle bicontinuous microemulsion phase).
- At high salinity ($S > 2.10\\text{ wt}\\%$): Winsor II (W/O microemulsion in equilibrium with excess water).
(a) Explain the electrostatic origin of this transition in terms of Debye screening length $\\kappa^{-1} \\propto S^{-1/2}$ and the Israelachvili packing parameter $P = v / (a_0 l_c)$.
(b) At optimal salinity $S^* = 1.35\\text{ wt}\\%$, the middle phase contains equal volume fractions of water and oil ($\\phi_w = \\phi_o = 0.45$) and solubilizes oil with a solubilization ratio $\\sigma_o = V_o / V_s = 18.5\\text{ mL oil / mL surfactant}$.
According to Huh's theoretical relationship, the ultralow interfacial tension $\\gamma^*$ is:
\\[
\\gamma^* = \\frac{C}{(\\sigma^*)^2}
\\]
where Huh's constant is $C \\approx 0.30\\text{ mN/m}$.
Calculate $\\gamma^*$ at the optimal salinity in $\\text{mN/m}$ and in $\\mu\\text{N/m}$.
(c) Compare $\\gamma^*$ with the clean octane-water interfacial tension ($\\gamma_0 = 50.8\\text{ mN/m}$) and calculate the reduction factor.""",
            "solution": """### Step 1: Electrostatic Mechanism of Winsor Transitions
1. **Low Salinity ($S < 0.8\\%$, Winsor I)**:
   - Low ionic strength corresponds to a large Debye screening length $\\kappa^{-1}$.
   - Electrostatic repulsion between negatively charged sulfosuccinate headgroups is strong, forcing a large headgroup area $a_0$.
   - Packing parameter $P = v / (a_0 l_c) < 1$.
   - The interface curves spontaneously around the oil phase (**positive spontaneous curvature**, convex toward water), producing an **oil-in-water (O/W)** microemulsion in the aqueous bottom phase, rejecting excess oil to the top (Winsor I).
2. **Optimal Salinity ($S^* = 1.35\\%$, Winsor III)**:
   - Increasing electrolyte concentration screens headgroup charges, shrinking $a_0$.
   - At $S^*$, the headgroup area matches the tail cross-section: $P \\approx 1$.
   - The spontaneous curvature vanishes ($H_0 \\approx 0$). The interface forms a flat, fluctuating **bicontinuous sponge phase** that simultaneously coexists with both an upper oil phase and a lower brine phase (Winsor III).
3. **High Salinity ($S > 2.1\\%$, Winsor II)**:
   - High ionic strength heavily screens headgroup charges, shrinking $a_0$ further.
   - Now $P > 1$.
   - The interface curves around water droplets (**negative spontaneous curvature**, convex toward oil), forming a **water-in-oil (W/O)** microemulsion in the upper oil phase and expelling excess brine to the bottom (Winsor II).

### Step 2: Ultralow Interfacial Tension via Huh's Formula
At optimal salinity, the oil and water solubilization ratios are equal: $\\sigma_o^* = \\sigma_w^* = 18.5$.
Using Huh's equation with $C = 0.30\\text{ mN/m}$:
\\[
\\gamma^* = \\frac{C}{(\\sigma^*)^2} = \\frac{0.30\\text{ mN/m}}{(18.5)^2} = \\frac{0.30}{342.25} = 8.7655 \\times 10^{-4}\\text{ mN/m}
\\]
In micronewtons per meter ($\mu\\text{N/m}$):
\\[
\\gamma^* = 0.877\\,\\mu\\text{N/m}
\\]
The interfacial tension drops below one micro-Newton per meter.

### Step 3: Reduction Factor Comparison
Given clean oil-water interfacial tension $\\gamma_0 = 50.8\\text{ mN/m}$:
\\[
\\text{Reduction Factor} = \\frac{\\gamma_0}{\\gamma^*} = \\frac{50.8\\text{ mN/m}}{8.7655 \\times 10^{-4}\\text{ mN/m}} = 57{,}954 \\approx 5.80 \\times 10^4
\\]
The surfactant-electrolyte formulation lowers the interfacial tension by nearly **$60{,}000$-fold**, enabling spontaneous emulsification without external mechanical shear (essential for Enhanced Oil Recovery)."""
        },
        {
            "probNumber": "8.7",
            "title": "Kinetic Theory of Micelle Relaxation: Aniansson-Wall Two-Relaxation Model",
            "difficulty": "Advanced",
            "statement": """Fast relaxation kinetics of micellar solutions (measured by pressure-jump or ultrasonic attenuation) reveal two well-separated relaxation times:
1. Fast relaxation $\\tau_1$ (microseconds, $\\mu\\text{s}$): Monomer exchange between micelles and bulk solution:
   $M + A_1 \\xrightleftharpoons[k_{-1}]{k_1} M'$
2. Slow relaxation $\\tau_2$ (milliseconds, $\\text{ms}$): Complete micelle formation and dissolution through a stepwise birth-and-death nucleation barrier.
According to the Aniansson-Wall kinetic theory:
\\[
\\frac{1}{\\tau_1} = \\frac{k_{-1}}{\\sigma^2} + \\frac{k_{-1}}{\\bar{N}} \\left( \\frac{C - \\text{CMC}}{\\text{CMC}} \\right)
\\]
where $\\bar{N}$ is the mean aggregation number, $\\sigma$ is the polydispersity standard deviation of the micelle size distribution, and $k_{-1}$ is the dissociation rate constant of a single monomer from a micelle.
For an ionic surfactant at $T = 298.15\\text{ K}$ with $\\text{CMC} = 5.00 \\times 10^{-3}\\text{ M}$, $\\bar{N} = 80$, and $\\sigma = 8.0$:
- At $C = 15.0\\text{ mM}$, the fast relaxation time is $\\tau_1 = 25.0\\,\\mu\\text{s} = 2.50 \\times 10^{-5}\\text{ s}$.
(a) Determine the unimolecular monomer exit rate constant $k_{-1}$ in $\\text{s}^{-1}$.
(b) Calculate the diffusion-controlled monomer entrance rate constant $k_1$ in $\\text{M}^{-1}\\text{s}^{-1}$ using detailed balance at the CMC ($k_1 \\, \\text{CMC} = k_{-1}$).
(c) The slow relaxation time is given by $\\frac{1}{\\tau_2} \\approx \\frac{\\bar{N}^2}{\\tau_1} \\frac{[A_{r^*}]}{C - \\text{CMC}}$, where $[A_{r^*}]$ is the concentration of the critical transition-state intermediate.
If $\\tau_2 = 12.5\\text{ ms} = 1.25 \\times 10^{-2}\\text{ s}$ at $C = 15.0\\text{ mM}$, calculate the concentration ratio $[A_{r^*}] / (C - \\text{CMC})$ representing the depth of the nucleation free energy well.""",
            "solution": """### Step 1: Unimolecular Monomer Exit Rate Constant ($k_{-1}$)
From the Aniansson-Wall expression for $1 / \\tau_1$:
\\[
\\frac{1}{\\tau_1} = k_{-1} \\left[ \\frac{1}{\\sigma^2} + \\frac{1}{\\bar{N}} \\left( \\frac{C - \\text{CMC}}{\\text{CMC}} \\right) \\right]
\\]
Given:
- $\\tau_1 = 2.50 \\times 10^{-5}\\text{ s} \\implies 1 / \\tau_1 = 40{,}000\\text{ s}^{-1}$
- $\\sigma = 8.0 \\implies \\sigma^2 = 64.0 \\implies 1 / \\sigma^2 = 0.015625$
- $\\bar{N} = 80$
- $C = 15.0\\text{ mM}$, $\\text{CMC} = 5.0\\text{ mM} \\implies \\frac{C - \\text{CMC}}{\\text{CMC}} = \\frac{10.0}{5.0} = 2.0$
Substitute the bracketed term:
\\[
[\\dots] = 0.015625 + \\frac{2.0}{80} = 0.015625 + 0.025000 = 0.040625
\\]
Now solve for $k_{-1}$:
\\[
k_{-1} = \\frac{1 / \\tau_1}{0.040625} = \\frac{40{,}000\\text{ s}^{-1}}{0.040625} = 9.8462 \\times 10^5\\text{ s}^{-1}
\\]
The exit rate constant is $k_{-1} \\approx 9.85 \\times 10^5\\text{ s}^{-1}$. An individual monomer resides inside a micelle for an average lifetime of $\\tau_{\\text{res}} = 1 / k_{-1} \\approx 1.0\\,\\mu\\text{s}$.

### Step 2: Monomer Entrance Rate Constant ($k_1$)
From detailed balance at equilibrium:
\\[
k_1 \\times \\text{CMC} = k_{-1} \\implies k_1 = \\frac{k_{-1}}{\\text{CMC}}
\\]
With $\\text{CMC} = 5.00 \\times 10^{-3}\\text{ M}$:
\\[
k_1 = \\frac{9.8462 \\times 10^5\\text{ s}^{-1}}{5.00 \\times 10^{-3}\\text{ M}} = 1.9692 \\times 10^8\\text{ M}^{-1}\\text{s}^{-1}
\\]
The association rate constant $k_1 \\approx 1.97 \\times 10^8\\text{ M}^{-1}\\text{s}^{-1}$ is near the Smoluchowski diffusion limit for colloids.

### Step 3: Nucleation Barrier and Concentration Ratio
From the relation:
\\[
\\frac{1}{\\tau_2} = \\frac{\\bar{N}^2}{\\tau_1} \\frac{[A_{r^*}]}{C - \\text{CMC}}
\\]
Rearranging for the ratio:
\\[
\\frac{[A_{r^*}]}{C - \\text{CMC}} = \\frac{\\tau_1}{\\tau_2 \\, \\bar{N}^2}
\\]
Substitute values:
- $\\tau_1 = 2.50 \\times 10^{-5}\\text{ s}$
- $\\tau_2 = 1.25 \\times 10^{-2}\\text{ s}$
- $\\bar{N}^2 = 80^2 = 6{,}400$
\\[
\\frac{[A_{r^*}]}{C - \\text{CMC}} = \\frac{2.50 \\times 10^{-5}}{(1.25 \\times 10^{-2}) \\times 6{,}400} = \\frac{2.50 \\times 10^{-5}}{80.0} = 3.125 \\times 10^{-7}
\\]
- **Physical Meaning**:
  The intermediate oligomer at the nucleation bottleneck ($r^* \\approx 10 - 20$ monomers) has an equilibrium concentration less than one part in three million relative to mature micelles. This profound free energy barrier accounts for why complete micelle dissolution ($\tau_2$) is three orders of magnitude slower than single-monomer exchange ($\tau_1$)."""
        },
        {
            "probNumber": "8.8",
            "title": "Elastic Bending Free Energy of Lipid Vesicles: Helfrich Hamiltonian",
            "difficulty": "Advanced",
            "statement": """The elastic deformation energy of a lipid bilayer vesicle of surface area $A$ is described by the **Helfrich Bending Hamiltonian**:
\\[
\\mathcal{H}_b = \\oint_A \\left[ \\frac{1}{2} \\kappa_b (c_1 + c_2 - 2 c_0)^2 + \\bar{\\kappa} c_1 c_2 \\right] dA
\\]
where:
- $c_1, c_2$ are the principal curvatures ($c_1 = 1/R_1, c_2 = 1/R_2$).
- $c_0$ is the spontaneous curvature of the bilayer.
- $\\kappa_b$ is the bending rigidity modulus (typically $20\\, k_B T \\approx 8.28 \\times 10^{-20}\\text{ J}$ at $300\\text{ K}$).
- $\\bar{\\kappa}$ is the Gaussian curvature modulus (typically $-0.7\\, \\kappa_b$).
(a) For a spherical unilamellar vesicle of radius $R$ and zero spontaneous curvature ($c_0 = 0$), show that the bending energy is independent of the vesicle radius $R$:
\\[
E_b = 4\\pi (2 \\kappa_b + \\bar{\\kappa})
\\]
(b) Evaluate $E_b$ in $\\text{J}$ and in units of $k_B T$ for $\\kappa_b = 20\\, k_B T$ and $\\bar{\\kappa} = -14\\, k_B T$.
(c) Now consider an asymmetric vesicle where the outer leaflet contains PEGylated lipids that induce a non-zero spontaneous curvature $c_0 = 1 / (40.0\\text{ nm})$.
Calculate the optimal vesicle radius $R^*$ that minimizes the mean curvature energy term $\\frac{1}{2} \\kappa_b (2/R - 2 c_0)^2$ and calculate the residual bending energy for a vesicle forced to radius $R = 20.0\\text{ nm}$.""",
            "solution": """### Step 1: Analytical Derivation for a Spherical Vesicle
For a sphere of radius $R$:
- Both principal curvatures are equal everywhere on the surface:
\\[
c_1 = c_2 = \\frac{1}{R}
\\]
- The mean curvature is:
\\[
H = \\frac{c_1 + c_2}{2} = \\frac{1}{R} \\implies c_1 + c_2 = \\frac{2}{R}
\\]
- The Gaussian curvature is:
\\[
K = c_1 c_2 = \\frac{1}{R^2}
\\]
For $c_0 = 0$, the integrand of the Helfrich Hamiltonian becomes:
\\[
\\frac{1}{2} \\kappa_b \\left( \\frac{2}{R} \\right)^2 + \\bar{\\kappa} \\left( \\frac{1}{R^2} \\right) = \\frac{2 \\kappa_b}{R^2} + \\frac{\\bar{\\kappa}}{R^2} = \\frac{2 \\kappa_b + \\bar{\\kappa}}{R^2}
\\]
Integrating over the total surface area of the sphere ($A = 4\\pi R^2$):
\\[
E_b = \\oint_A \\frac{2 \\kappa_b + \\bar{\\kappa}}{R^2} dA = \\left( \\frac{2 \\kappa_b + \\bar{\\kappa}}{R^2} \\right) \\times 4\\pi R^2 = 4\\pi (2 \\kappa_b + \\bar{\\kappa})
\\]
Remarkably, the radius $R^2$ cancels out completely! The total elastic energy required to bend a planar symmetric membrane into a closed sphere is a **topological invariant** dictated by the Gauss-Bonnet theorem, regardless of whether the vesicle has a radius of $20\\text{ nm}$ or $20\\,\\mu\\text{m}$.

### Step 2: Numerical Energy Evaluation
Given $\\kappa_b = 20\\, k_B T$ and $\\bar{\\kappa} = -14\\, k_B T$:
\\[
2 \\kappa_b + \\bar{\\kappa} = 2(20\\, k_B T) - 14\\, k_B T = 40\\, k_B T - 14\\, k_B T = 26\\, k_B T
\\]
\\[
E_b = 4\\pi \\times 26\\, k_B T = 104\\pi\\, k_B T \\approx 326.7\\, k_B T
\\]
At $T = 300\\text{ K}$, $k_B T = 4.14 \\times 10^{-21}\\text{ J}$:
\\[
E_b = 326.7 \\times (4.14 \\times 10^{-21}\\text{ J}) = 1.353 \\times 10^{-18}\\text{ J}
\\]
In molar units ($N_A \\times E_b$):
\\[
E_{b,\\text{molar}} = (1.353 \\times 10^{-18}\\text{ J}) \\times (6.022 \\times 10^{23}\\text{ mol}^{-1}) = 814.8\\text{ kJ per mole of vesicles}
\\]

### Step 3: Asymmetric Vesicle with Spontaneous Curvature $c_0$
1. **Optimal Radius $R^*$**:
The mean curvature term is:
\\[
E_{\\text{mean}} = \\frac{1}{2} \\kappa_b \\left( \\frac{2}{R} - 2 c_0 \\right)^2 A = 2 \\kappa_b \\left( \\frac{1}{R} - c_0 \\right)^2 (4\\pi R^2)
\\]
This energy is minimized when $\\frac{1}{R^*} = c_0$:
\\[
R^* = \\frac{1}{c_0} = 40.0\\text{ nm}
\\]
The spontaneous curvature selects an optimal vesicle radius of exactly $40.0\\text{ nm}$.
2. **Residual Strain Energy at $R = 20.0\\text{ nm}$**:
At $R = 20.0\\text{ nm}$:
\\[
\\frac{1}{R} - c_0 = \\frac{1}{20.0\\text{ nm}} - \\frac{1}{40.0\\text{ nm}} = 0.050 - 0.025 = 0.025\\text{ nm}^{-1} = 2.50 \\times 10^7\\text{ m}^{-1}
\\]
Total area $A = 4\\pi R^2 = 4\\pi (20.0 \\times 10^{-9}\\text{ m})^2 = 4\\pi (4.00 \\times 10^{-16}\\text{ m}^2) = 5.0265 \\times 10^{-15}\\text{ m}^2$.
\\[
E_{\\text{strain}} = 2 \\kappa_b \\left( \\frac{1}{R} - c_0 \\right)^2 A
\\]
With $\\kappa_b = 8.28 \\times 10^{-20}\\text{ J}$:
\\[
E_{\\text{strain}} = 2 \\times (8.28 \\times 10^{-20}\\text{ J}) \\times (2.50 \\times 10^7\\text{ m}^{-1})^2 \\times (5.0265 \\times 10^{-15}\\text{ m}^2)
\\]
\\[
E_{\\text{strain}} = (1.656 \\times 10^{-19}) \\times (6.25 \\times 10^{14}) \\times (5.0265 \\times 10^{-15}) = 5.202 \\times 10^{-19}\\text{ J} \\approx 125.7\\, k_B T
\\]
Forcing the vesicle to a smaller radius ($20\\text{ nm}$) incurs an elastic strain penalty of $126\\, k_B T$, driving spontaneous size equilibration toward $R = 40\\text{ nm}$."""
        },
        {
            "probNumber": "8.9",
            "title": "Gemini Surfactant Synergism: Regular Solution Theory & Interaction Parameter",
            "difficulty": "Advanced",
            "statement": """Mixed micelle formation between a conventional monomeric cationic surfactant ($1$, dodecyltrimethylammonium bromide, DTAB) and a dimeric gemini surfactant ($2$, 12-4-12 gemini, consisting of two dodecyl tails linked by a tetramethylene spacer) is modeled by Clint-Rubingh **regular solution theory**.
Experimental CMC values at $T = 298.15\\text{ K}$:
- Pure DTAB: $\\text{CMC}_1 = 15.0\\text{ mM}$
- Pure 12-4-12 gemini: $\\text{CMC}_2 = 1.10\\text{ mM}$
- Equimolar mixture in solution (mole fraction $\\alpha_1 = 0.50$): $\\text{CMC}_{12} = 1.35\\text{ mM}$
(a) Calculate the ideal mixed CMC according to Clint's ideal mixture rule:
\\[
\\frac{1}{\\text{CMC}_{\\text{ideal}}} = \\frac{\\alpha_1}{\\text{CMC}_1} + \\frac{1 - \\alpha_1}{\\text{CMC}_2}
\\]
(b) Using Rubingh's non-ideal equations:
\\[
\\frac{x_1^2 \\ln\\left( \\frac{\\text{CMC}_{12} \\alpha_1}{\\text{CMC}_1 x_1} \\right)}{(1 - x_1)^2 \\ln\\left( \\frac{\\text{CMC}_{12}(1 - \\alpha_1)}{\\text{CMC}_2 (1 - x_1)} \\right)} = 1
\\]
Given that the numerical solution yields a micellar mole fraction $x_1 = 0.220$:
Calculate the net interaction parameter $\\beta$:
\\[
\\beta = \\frac{\\ln\\left( \\frac{\\text{CMC}_{12} \\alpha_1}{\\text{CMC}_1 x_1} \\right)}{(1 - x_1)^2}
\\]
(c) Determine whether the mixed micellization exhibits synergism ($\\beta < 0$, $\\text{CMC}_{12} < \\text{CMC}_{\\text{ideal}}$) and calculate the excess Gibbs free energy of mixing $\\Delta G_{\\text{ex}}^\circ = \\beta RT x_1 (1 - x_1)$ in $\\text{kJ/mol}$.""",
            "solution": """### Step 1: Clint's Ideal CMC Calculation
From Clint's equation for ideal mixing:
\\[
\\frac{1}{\\text{CMC}_{\\text{ideal}}} = \\frac{0.50}{15.0\\text{ mM}} + \\frac{0.50}{1.10\\text{ mM}} = 0.03333 + 0.45455 = 0.48788\\text{ mM}^{-1}
\\]
\\[
\\text{CMC}_{\\text{ideal}} = \\frac{1}{0.48788} = 2.050\\text{ mM}
\\]
The experimental CMC is $\\text{CMC}_{12} = 1.35\\text{ mM} < \\text{CMC}_{\\text{ideal}} = 2.05\\text{ mM}$, indicating strong non-ideal synergistic interaction.

### Step 2: Rubingh Interaction Parameter ($\beta$)
Given:
- $\\text{CMC}_{12} = 1.35\\text{ mM}$
- $\\alpha_1 = 0.50$
- $\\text{CMC}_1 = 15.0\\text{ mM}$
- $x_1 = 0.220 \\implies 1 - x_1 = 0.780 \\implies (1 - x_1)^2 = (0.780)^2 = 0.6084$
Evaluate the numerator term:
\\[
\\frac{\\text{CMC}_{12} \\alpha_1}{\\text{CMC}_1 x_1} = \\frac{(1.35\\text{ mM}) \\times (0.50)}{(15.0\\text{ mM}) \\times (0.220)} = \\frac{0.675}{3.30} = 0.20455
\\]
Take the natural logarithm:
\\[
\\ln(0.20455) = -1.5869
\\]
The interaction parameter $\\beta$ is:
\\[
\\beta = \\frac{-1.5869}{0.6084} = -2.6083 \\approx -2.61
\\]

### Step 3: Assessment of Synergism and Excess Free Energy of Mixing
1. **Synergism Criterion**:
According to Rosen and Rubingh, synergism in mixed micelle formation requires:
- $\\beta < 0$ (attractive interactions between dissimilar components exceed self-interactions).
- $|\\beta| > |\\ln(\\text{CMC}_1 / \\text{CMC}_2)|$:
  $|\\ln(15.0 / 1.10)| = \\ln(13.636) = 2.6128$.
Here $\\beta = -2.61 < 0$ and $\\text{CMC}_{12} = 1.35\\text{ mM} < \\text{CMC}_{\\text{ideal}} = 2.05\\text{ mM}$, confirming **strong synergistic mixing**.
2. **Excess Gibbs Free Energy of Mixing ($\Delta G_{\text{ex}}^\circ$)**:
\\[
\\Delta G_{\\text{ex}}^\\circ = \\beta RT x_1 (1 - x_1)
\\]
With $RT = 8.31446 \\times 298.15 = 2478.96\\text{ J/mol}$:
\\[
x_1 (1 - x_1) = (0.220) \\times (0.780) = 0.1716
\\]
\\[
\\Delta G_{\\text{ex}}^\\circ = (-2.6083) \\times (2478.96\\text{ J/mol}) \\times (0.1716) = -1{,}109.5\\text{ J/mol} = -1.11\\text{ kJ/mol}
\\]
- **Physical Mechanism**:
  The tetramethylene spacer of the gemini surfactant forces its two cationic heads to a fixed distance. Inserting monomeric DTAB molecules between the gemini heads screens mutual headgroup electrostatic repulsions more efficiently than either pure component alone, generating a favorable excess free energy of $-1.11\\text{ kJ/mol}$."""
        }
    ]

    return {
        "id": "unit-8",
        "number": 8,
        "title": "Amphiphiles, Surfactants, Micelles & Vesicular Aggregates",
        "leadSummary": "Surface activity and the Gibbs adsorption isotherm, surfactant taxonomy (anionic, cationic, non-ionic, zwitterionic, gemini), experimental determination of the critical micelle concentration (CMC), thermodynamics of micellization (mass-action and phase-separation models), Israelachvili's critical packing parameter, morphology transitions (spheres, wormlike micelles, vesicles, lamellae), emulsions, microemulsions and Winsor transitions, and nanotechnological applications (liposomes, MCM-41).",
        "simulations": ["sim_supra_micelle_packing_cmc"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u8 = get_unit_8()
    print(f"Unit 8 generated: {len(u8['sections'])} sections, {len(u8['problems'])} problems.")
