"""
create_supra_u10.py
Creates Unit 10 data dictionary for Supramolecular Chemistry:
Metallomesogens & Optoelectronic Supramolecular Materials
8 sections, 9 problems. Zero prohibited tokens, KaTeX math formatting.
"""

def get_unit_10():
    sections = [
        {
            "secNumber": "10.1",
            "title": "Introduction to Metallomesogens: Metal Complexes as Liquid Crystals",
            "content": """**Metallomesogens** (metal-containing liquid crystals) are metal coordination complexes or organometallic compounds that exhibit liquid crystalline mesophases. Coined by José Luis Serrano in the late 1980s, the term unites coordination chemistry with soft matter physics.

### Why Introduce Metal Centers into Liquid Crystals?
Conventional purely organic mesogens are governed primarily by dielectric and optical anisotropies, typically displaying electrical insulating properties and diamagnetism.
Incorporating transition metals, lanthanides, or main-group metals into the mesogenic architecture introduces distinct physical phenomena:
1. **Paramagnetism and Magnetic Anisotropy**: Open-shell $d$- and $f$-electron configurations impart large permanent magnetic moments and anisotropic magnetic susceptibilities ($\\Delta\\chi = \\chi_\\parallel - \\chi_\\perp$), allowing macroscopic director reorientation using modest external magnetic fields ($B < 1\\text{ T}$).
2. **Polarizability and Birefringence**: Heavily polarizable metal atoms and metal-to-ligand/ligand-to-metal charge-transfer (MLCT/LMCT) transitions impart optical birefringence ($\\Delta n > 0.40$) and deep, vivid colors.
3. **One-Dimensional Electronic Conductivity**: Co-axial metal-metal interactions ($d_{z^2}-d_{z^2}$ overlap) along self-assembled columnar stacks create quasi-one-dimensional molecular wires for electronic charge and energy transport.
4. **Luminescence and Phosphorescence**: Heavy-atom spin-orbit coupling promotes efficient intersystem crossing ($S_1 \\rightarrow T_1$), enabling room-temperature phosphorescence and polarized emission for Organic Light-Emitting Diodes (OLEDs)."""
        },
        {
            "secNumber": "10.2",
            "title": "Coordination Geometries & Thermal Stability in Metallomesogens",
            "content": """The primary challenge in designing metallomesogens is that the preferred coordination geometries of metal ions (square-planar, tetrahedral, octahedral, square-pyramidal) tend to disrupt the shape anisotropy required for mesophase generation. Successful molecular design requires strategic geometric coordination.

### Classification by Ligand Denticity
1. **Monodentate Ligands**:
   Linear gold(I) and silver(I) complexes:
   \\[
   \\text{R-C}_6\\text{H}_4-\\text{C}\\equiv\\text{C}-\\text{Au}-\\text{C}\\equiv\\text{N}-\\text{C}_6\\text{H}_4-\\text{R}'
   \\]
   The two-coordinate linear geometry ($\angle \\text{C-Au-N} = 180^\\circ$) maintains calamitic rod-like geometry, stabilizing nematic and smectic A mesophases.
2. **Bidentate Chelates**:
   - **Bis($\beta$-diketonates)**: Square-planar complexes $[\\text{M}(\\beta\\text{-diketonate})_2]$ ($\text{Cu}^{II}, \\text{Ni}^{II}, \\text{Pd}^{II}, \\text{Pt}^{II}$).
   - **Bis(salicylaldiminates) / Schiff Bases**: Condensation products of 4-alkoxysalicylaldehydes with 4-alkoxyanilines. Form rigid, planar central cores that support both calamitic and discotic phases.
   - **Dithiolenes**: $[\\text{M}(\\text{S}_2\\text{C}_2\\text{R}_2)_2]$ complexes exhibiting planar geometries and reversible multi-electron redox chemistry.
3. **Polydentate Macrocycles**:
   Tetradentate phthalocyanines and porphyrins coordinating divalent metal ions ($\text{Cu}^{II}, \\text{Ni}^{II}, \\text{Zn}^{II}, \\text{Pt}^{II}$) into flat discs that generate discotic columnar phases.

### Thermal Mesophase Stability
The clearing temperature $T_{\\text{clearing}}$ and mesophase range $\\Delta T = T_{\\text{clearing}} - T_m$ depend critically on the central metal ion:
- **Square-Planar ($\text{Pd}^{II}, \\text{Pt}^{II}, \\text{Ni}^{II}$)**: Highly planar cores maximize $\\pi-\\pi$ stacking and lateral intermolecular cohesion, yielding broad mesophase ranges.
- **Tetrahedral ($\text{Zn}^{II}, \\text{Cu}^I$)**: Non-planar orthogonal geometries disrupt parallel packing, depressing clearing temperatures or completely extinguishing mesomorphism."""
        },
        {
            "secNumber": "10.3",
            "title": "Calamitic Metallomesogens: beta-Diketonates & Schiff Bases",
            "content": """Calamitic metallomesogens are elongated, rod-like coordination complexes that form nematic, smectic A, and smectic C mesophases.

### Bis(salicylaldiminato) Copper(II) and Palladium(II) Complexes
The archetypal calamitic metallomesogens are bis(salicylaldiminates):
\\[
[\\text{M}(\\text{salen-type})_2], \\quad \\text{M} = \\text{Cu}^{II}, \\text{Pd}^{II}, \\text{Ni}^{II}
\\]
- Synthesized by reacting 4-alkoxy-substituted salicylaldehydes with 4-alkyl- or 4-alkoxyanilines, followed by metallation with metal acetates.
- The two bidentate ligands coordinate in a *trans* square-planar geometry, yielding a centrosymmetric lath-like molecule with an aspect ratio $L / D > 4$.
- Long terminal alkoxy chains ($-\\text{OC}_n\\text{H}_{2n+1}$, $n = 6 - 16$) depress the crystalline melting point, producing enantiotropic SmA and SmC phases across broad temperature windows (e.g., $100^\\circ\\text{C} \\le T \\le 180^\\circ\\text{C}$).

### Bis($\beta$-diketonate) Metallomesogens
Complexes of 1,3-diphenylpropane-1,3-diones with copper(II) or palladium(II):
- Symmetrical tetra-substituted derivatives form stable calamitic nematic and smectic phases.
- The open coordination sites above and below the square-planar $[\\text{M}\\text{O}_4]$ core permit weak axial intermolecular metal-metal interactions ($d_{\\text{M}\\cdots\\text{M}} \\approx 3.4 - 3.8\\text{ Å}$) or axial coordination by solvent molecules, allowing reversible thermochromic and solvatochromic switching.

### Ferroelectric Metallomesogens
Incorporating chiral branched tails (e.g., $(S)$-2-octyloxy or $(S)$-citronellyl) into polar Schiff-base complexes yields **ferroelectric chiral smectic C* ($\text{SmC}^*$) metallomesogens**:
- Combine permanent spontaneous electric polarization ($P_s > 100\\text{ nC/cm}^2$) with paramagnetic $d^9\\,\\text{Cu}^{II}$ ($S = 1/2$) centers, creating multiferroic soft materials responsive to both electric and magnetic fields."""
        },
        {
            "secNumber": "10.4",
            "title": "Discotic Metallomesogens: Metallophthalocyanines & 1D Conducting Columns",
            "content": """Discotic metallomesogens consist of a flat, disc-shaped metallic core surrounded by six, eight, or more flexible paraffinic side chains. They self-assemble into long, cylindrical columnar stacks that arrange into 2D lattices.

### Octasubstituted Metallophthalocyanines ($\text{MPc}$)
Synthesized by the cyclotetramerization of 4,5-dialkoxyphthalonitriles in the presence of metal salts:
\\[
4\\,(4,5\\text{-di(alkoxy)phthalonitrile}) + \\text{M}^{2+} \\xrightarrow{\\text{reflux}} [\\text{M}\\{\\text{Pc}(\\text{OR})_8\\}]
\\]
- The central phthalocyanine macrocycle forms an extremely rigid, aromatic square-planar core ($18\\,\\pi$-electron conjugated system) coordinated to $\\text{Cu}^{II}, \\text{Ni}^{II}, \\text{Zn}^{II}, \\text{Co}^{II}$, or $\\text{Pt}^{II}$.
- Eight peripheral flexible alkyl chains ($-\\text{C}_8\\text{H}_{17}$ to $-\\text{C}_{12}\\text{H}_{25}$) encircle the rigid core.
- **Columnar Hexagonal Phase ($Col_h$)**:
  In the mesophase, the macrocyclic discs stack face-to-face with an intracolumnar separation $d_a \\approx 3.4 - 3.6\\text{ Å}$.
  The flexible aliphatic chains melt into a continuous disordered liquid-like paraffinic mantle that insulates each column from neighboring columns ($d_{\\text{inter}} \\approx 20 - 30\\text{ Å}$).

### 1D Quasi-One-Dimensional Electronic Conduction
The co-axial stacking of aromatic $\\pi$-systems and square-planar metal orbitals creates exceptional anisotropic electrical transport:
- **Intracolumnar Overlap**: Direct overlap between adjacent macrocyclic $\\pi$-orbitals and metal $d_{z^2}$ orbitals forms a continuous 1D electronic conduction band along the column axis.
- **Electrical Anisotropy**: The electrical conductivity parallel to the columns ($\sigma_\\parallel$) is **four to six orders of magnitude higher** than the conductivity perpendicular to the columns ($\sigma_\\perp$):
\\[
\\frac{\\sigma_\\parallel}{\\sigma_\\perp} > 10^4 - 10^6
\\]
- Oxidative chemical doping (with iodine, $\\text{I}_2$, or $\\text{NOBF}_4$) partially oxidizes the metal or phthalocyanine ring, generating delocalized radical cations (polarons) that elevate 1D room-temperature conductivity to $\\sigma_\\parallel > 10^{-1} - 10^1\\text{ S/cm}$—functioning as self-healing molecular coaxial cables."""
        },
        {
            "secNumber": "10.5",
            "title": "Supramolecular Gels: LMWGs, Metallogels & Self-Assembled Networks",
            "content": """A **supramolecular gel** is a semi-solid colloidal material consisting of a liquid phase entrapped within a three-dimensional, self-assembled fibrillar network of low-molecular-weight gelators (**LMWGs**, typically $M_w < 2{,}000\\text{ g/mol}$) held together strictly by non-covalent forces.

### The Self-Assembled Fibrillar Network (SAFIN)
Unlike chemical gels (e.g., crosslinked polyacrylamide) where polymer chains are permanently joined by covalent crosslinks:
1. **1D Primary Aggregation**: Small gelator molecules undergo highly anisotropic, one-dimensional self-assembly driven by directional interactions (hydrogen bonding, $\\pi-\\pi$ stacking, solvophobic exclusion, or metal coordination), growing into long nanoscale fibers or ribbons (width $5 - 50\\text{ nm}$, length tens of micrometers).
2. **Secondary Network Formation**: The 1D fibers intertwine, branch, and entangle into a continuous three-dimensional **Self-Assembled Fibrillar Network (SAFIN)**.
3. **Liquid Entrapment**: The SAFIN immobilizes vast quantities of solvent through capillary forces and surface tension, often gelling at minimum gelator concentrations below **$0.1\\text{ wt}\\%$** (a single gelator molecule can immobilize over $100{,}000$ solvent molecules!).

### Metallogels: Coordination-Driven Supramolecular Gels
In a **metallogel**, metal-ligand coordination bonds serve as the primary organizing force or crosslinking junctions:
- **Ligand Scaffolds**: Polytopic ligands such as bis(pyridyl)alkanes, terpyridine-terminated telechelic polymers, or cholesterol-tethered bipyridines.
- **Metal Crosslinkers**: Divalent and trivalent transition metals ($\text{Fe}^{II}, \\text{Ru}^{II}, \\text{Co}^{II}, \\text{Zn}^{II}, \\text{Eu}^{III}$).
- **Multi-Stimuli Responsiveness**:
  Because metal-ligand coordination is reversible, metallogels respond to a wide array of environmental triggers:
  - **Thermal**: Reversible gel-to-sol transition at $T_{\\text{gel}}$.
  - **Mechanical**: Shear-thinning (thixotropy) where mechanical stress liquefies the gel, but removing stress allows the coordination network to recover immediately (self-healing).
  - **Chemical / Redox**: Adding competitive ligands (EDTA) or altering the metal oxidation state ($\text{Fe}^{II} \\rightarrow \\text{Fe}^{III}$) instantly dissolves or triggers gelation.
  - **Optical**: Lanthanide-containing metallogels ($\text{Eu}^{III}, \\text{Tb}^{III}$) display intense, polarized photoluminescence."""
        },
        {
            "secNumber": "10.6",
            "title": "Stimuli-Responsive Supramolecular Polymers: Self-Healing Materials",
            "content": """Stimuli-responsive supramolecular polymers exploit the dynamic reversibility of non-covalent bonds to create adaptive, smart materials that change their macroscopic properties in response to environmental cues.

### Mechanisms of Stimuli-Responsiveness
1. **Thermoreversibility**:
   Heating shifts the non-covalent polymerization equilibrium toward dissociated monomers, causing drastic viscosity drops ($>10^4$-fold) that facilitate melt processing, recycling, and injection molding. Cooling restores high-molecular-weight polymer chains without degradation.
2. **Mechanochemistry and Mechanophores**:
   Under excessive mechanical shear or tensile stress, dynamic non-covalent junctions dissociate reversibly before covalent bonds rupture. This sacrificial bond dissipation imparts exceptional toughness and crack resistance.
3. **Photochemical Responsiveness**:
   Incorporating photo-switchable units (such as azobenzene, spiropyran, or diarylethene) allows light to trigger conformational changes (*trans* $\\rightarrow$ *cis*), disrupting hydrogen-bonding or $\\pi$-stacking arrays to induce isothermal gel-sol transitions or macroscopic mechanical contraction.

### Autonomous Self-Healing Materials
In classical polymers, mechanical fracture permanently severs covalent bonds.
In supramolecular elastomers (e.g., Leibler's fatty-acid-derived oligomers crosslinked by multiple hydrogen bonds):
- When a material is cut in two, the severed faces are covered with exposed, unpartnered hydrogen-bond donors and acceptors.
- Because the glass transition temperature is well below room temperature ($T_g < 0^\\circ\\text{C}$), the chains remain fluid and mobile at the fracture interface.
- Bringing the cut surfaces into physical contact allows the dynamic hydrogen bonds to re-mate spontaneously across the interface without requiring heat, solvent, or catalyst.
- Tensile strength is restored to $>90\\%$ of its original value within minutes at room temperature."""
        },
        {
            "secNumber": "10.7",
            "title": "Optoelectronic Supramolecular Devices: OFETs, OPVs & OLEDs",
            "content": """Supramolecular architectures provide the nanoscale structural control required to fabricate next-generation organic electronic, optoelectronic, and energy conversion devices.

### 1. Organic Field-Effect Transistors (OFETs)
OFET performance depends on the field-effect charge carrier mobility $\\mu_{\\text{FET}}$ of the semiconducting channel:
- Supramolecular columnar discotics (e.g., hexabenzocoronenes, phthalocyanines) and liquid crystalline polythiophenes (e.g., P3HT) self-align into homeotropic or planar domains.
- Extended co-facial $\\pi-\\pi$ overlap eliminates inter-grain trap states, elevating charge mobility to $\\mu > 1 - 10\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$, matching amorphous silicon.

### 2. Organic Photovoltaics (OPVs) and Bulk Heterojunctions
In organic solar cells, light absorption generates tightly bound electron-hole pairs (**Frenkel excitons**, binding energy $E_b \\approx 0.3 - 0.5\\text{ eV}$):
- Excitons must diffuse to an interface between an electron donor and an electron acceptor within their finite diffusion lifetime (exciton diffusion length $L_D \\approx 10 - 20\\text{ nm}$).
- **Bulk Heterojunction (BHJ)**: Supramolecular phase separation of donor polymers and non-fullerene acceptors into bicontinuous nanoscale interpenetrating networks with $15\\text{ nm}$ domain sizes ensures that all generated excitons reach a dissociating interface, pushing power conversion efficiencies (PCE) beyond **$19\\%$**.

### 3. Organic Light-Emitting Diodes (OLEDs) and TADF
- Supramolecular coordination emitters utilizing square-planar platinum(II) or gold(III) complexes exhibit planar architectures that suppress non-radiative concentration quenching.
- **Thermally Activated Delayed Fluorescence (TADF)**: Supramolecular engineering minimizes the singlet-triplet energy gap ($\\Delta E_{\\text{ST}} < 0.1\\text{ eV}$), enabling $100\\%$ internal quantum efficiency by harvesting both singlet and triplet excitons without expensive iridium dopants."""
        },
        {
            "secNumber": "10.8",
            "title": "Frontiers of Supramolecular Technology: Dynamic Libraries & Nanoscale Logic",
            "content": """Supramolecular chemistry is transforming into an information-driven science capable of autonomous molecular decision-making, adaptive evolution, and biomimetic computation.

### Dynamic Combinatorial Chemistry (DCC)
Dynamic Combinatorial Chemistry, pioneered by Jean-Marie Lehn and Jeremy Sanders, generates constitutional dynamic libraries (CDLs) of interconverting building blocks connected by reversible bonds (imines, hydrazones, disulfides):
\\[
\\text{Library of Building Blocks} \\xrightleftharpoons{\\text{dynamic exchange}} \\{ A_1 B_1, A_1 B_2, A_2 B_1, A_2 B_2, \\dots \\}
\\]
- **Template-Induced Selection (Amplification)**:
  When a target biomacromolecule (enzyme, DNA duplex) or synthetic guest is introduced into the library, the constituent that binds the template with highest affinity is thermodynamically pulled from the equilibrium.
  According to Le Chatelier's principle, the entire library re-equilibrates to **amplify** the best-binding receptor, effectively performing molecular Darwinian selection to discover high-affinity drugs and catalysts.

### Nanoscale Molecular Logic Gates
Individual supramolecular hosts execute Boolean logic operations by coupling multiple independent chemical or optical inputs to distinct spectroscopic outputs:
- **Two-Input AND Gate**: A fluorescent crown ether receptor with both a tertiary amine (proton input) and a crown ether cavity (sodium ion input). Photoinduced electron transfer (PET) quenches fluorescence unless **both** $\\text{H}^+$ and $\\text{Na}^+$ are bound simultaneously, producing optical emission only for the $(1, 1)$ state.
- **Half-Adders and Sub-Nanometer Processing**: Combining complementary AND, XOR, and INHIBIT supramolecular switches allows synthetic systems to execute basic arithmetic computations at the single-molecule scale, heralding the advent of chemical informatics."""
        }
    ]

    problems = [
        {
            "probNumber": "10.1",
            "title": "Molecular Geometry & Dipole Moments in Calamitic Schiff-Base Metallomesogens",
            "difficulty": "Foundational",
            "statement": """A calamitic Schiff-base coordination complex, bis[4-(4-decyloxybenzoyloxy)salicylaldiminato]metal(II), can adopt either a *trans* or a *cis* square-planar coordination geometry at the central metal ion:
- Each individual bidentate salicylaldiminate ligand possesses an in-plane electric dipole moment $\\boldsymbol{\\mu}_0 = 4.20\\text{ D}$ oriented at an angle $\\alpha = 45.0^\\circ$ relative to the long molecular axis.
(a) For the *trans* isomer (centrosymmetric, point group $C_{2h}$):
    (i) Show that the net molecular dipole moment vanishes: $\\boldsymbol{\\mu}_{\\text{trans}} = 0$.
    (ii) Explain why the *trans* isomer exhibits an enantiotropic nematic mesophase with high thermal clearing stability ($T_{\\text{NI}} = 165^\\circ\\text{C}$).
(b) For the *cis* isomer (non-centrosymmetric, point group $C_{2v}$):
    (i) Calculate the net molecular dipole moment $\\boldsymbol{\\mu}_{\\text{cis}}$ in Debye ($\text{D}$) and in Coulomb-meters ($\text{C}\\cdot\\text{m}$, with $1\\text{ D} = 3.33564 \\times 10^{-30}\\text{ C}\\cdot\\text{m}$).
    (ii) Explain why the *cis* isomer exhibits a bent-core morphology with depressed clearing temperature ($T_{\\text{NI}} = 110^\\circ\\text{C}$) but forms polar smectic phases.""",
            "solution": """### Step 1: Trans Isomer Dipole Moment and Nematic Stability
1. **Net Dipole Moment of Trans Isomer**:
In the *trans* square-planar geometry, the coordination center possesses an inversion center ($i$).
The two coordinated ligands lie on opposite sides of the metal center with their individual dipole vectors oriented in exactly opposite directions:
\\[
\\boldsymbol{\\mu}_1 = -\\boldsymbol{\\mu}_2
\\]
The vector sum of the dipoles is:
\\[
\\boldsymbol{\\mu}_{\\text{trans}} = \\boldsymbol{\\mu}_1 + \\boldsymbol{\\mu}_2 = \\boldsymbol{\\mu}_1 - \\boldsymbol{\\mu}_1 = 0\\text{ D}
\\]
The net molecular dipole moment is exactly zero.
2. **Thermal Stability of the Nematic Mesophase**:
In the *trans* geometry, the two terminal decyloxy chains extend collinearly in opposite directions along a common axis, producing a linear, rod-like molecule with an aspect ratio exceeding $L / D > 4.5$.
Because the molecule is strictly linear, molecules pack efficiently into parallel orientational arrays without steric frustration, stabilizing the nematic mesophase up to a high clearing point ($T_{\\text{NI}} = 165^\\circ\\text{C}$).

### Step 2: Cis Isomer Dipole Moment and Bent Morphology
1. **Net Dipole Moment of Cis Isomer**:
In the *cis* square-planar geometry, the two bidentate ligands coordinate adjacent to each other.
The two dipole vectors $\\boldsymbol{\\mu}_1$ and $\\boldsymbol{\\mu}_2$ are oriented at an angle $\\phi = 90.0^\\circ$ relative to each other:
\\[
|\\boldsymbol{\\mu}_{\\text{cis}}| = \\sqrt{\\mu_0^2 + \\mu_0^2 + 2 \\mu_0^2 \\cos(90^\\circ)} = \\sqrt{2 \\mu_0^2} = \\mu_0 \\sqrt{2}
\\]
With $\\mu_0 = 4.20\\text{ D}$:
\\[
|\\boldsymbol{\\mu}_{\\text{cis}}| = 4.20 \\times 1.41421 = 5.940\\text{ D} \\approx 5.94\\text{ D}
\\]
Converting to Coulomb-meters:
\\[
|\\boldsymbol{\\mu}_{\\text{cis}}| = (5.940\\text{ D}) \\times (3.33564 \\times 10^{-30}\\text{ C}\\cdot\\text{m/D}) = 1.981 \\times 10^{-29}\\text{ C}\\cdot\\text{m}
\\]
The *cis* isomer possesses a large transverse dipole moment of $5.94\\text{ D}$.
2. **Bent-Core Morphology and Mesophase Properties**:
In the *cis* configuration, the two long terminal alkoxy chains project at an angle of $\\approx 90^\\circ - 120^\\circ$ relative to each other, creating a bent "banana-like" architecture.
- This bent shape disrupts the parallel alignment required for the linear nematic phase, lowering the clearing point from $165^\\circ\\text{C}$ to $110^\\circ\\text{C}$.
- However, the large permanent transverse dipole ($1.98 \\times 10^{-29}\\text{ C}\\cdot\\text{m}$) drives close lateral packing into close-packed smectic layers with polar alignment, stabilizing polar and ferroelectric smectic phases."""
        },
        {
            "probNumber": "10.2",
            "title": "1D Intracolumnar Conductivity in Discotic Metallophthalocyanines: Arrhenius Model",
            "difficulty": "Foundational",
            "statement": """An iodine-doped octakis(octyloxy)phthalocyaninato-copper(II) complex, $[\\text{Cu}\\{\\text{Pc}(\\text{OC}_8\\text{H}_{17})_8\\}](\\text{I}_3)_{0.33}$, self-assembles into a columnar hexagonal mesophase ($Col_h$).
The 1D electrical conductivity along the column axis ($\sigma_\\parallel$) was measured as a function of temperature:
- At $T_1 = 300.0\\text{ K}$ ($26.85^\\circ\\text{C}$): $\\sigma_\\parallel(T_1) = 0.450\\text{ S/cm}$
- At $T_2 = 360.0\\text{ K}$ ($86.85^\\circ\\text{C}$): $\\sigma_\\parallel(T_2) = 1.850\\text{ S/cm}$
The perpendicular conductivity across the insulating alkyl mantle at $300\\text{ K}$ is $\\sigma_\\perp = 2.20 \\times 10^{-6}\\text{ S/cm}$.
(a) Calculate the electrical conductivity anisotropy ratio $\\sigma_\\parallel / \\sigma_\\perp$ at $300.0\\text{ K}$.
(b) Assuming thermally activated hopping conductivity following the Arrhenius law $\\sigma(T) = \\sigma_0 \\exp(-E_a / (k_B T))$, determine the activation energy $E_a$ in $\\text{eV}$ and in $\\text{kJ/mol}$, and calculate the pre-exponential factor $\\sigma_0$.
(c) Calculate the expected 1D conductivity $\\sigma_\\parallel$ at an elevated operating temperature $T = 400.0\\text{ K}$.""",
            "solution": """### Step 1: Electrical Conductivity Anisotropy
Given $\\sigma_\\parallel = 0.450\\text{ S/cm}$ and $\\sigma_\\perp = 2.20 \\times 10^{-6}\\text{ S/cm}$ at $300.0\\text{ K}$:
\\[
\\text{Anisotropy} = \\frac{\\sigma_\\parallel}{\\sigma_\\perp} = \\frac{0.450\\text{ S/cm}}{2.20 \\times 10^{-6}\\text{ S/cm}} = 204{,}545 \\approx 2.05 \\times 10^5
\\]
The conductivity along the 1D columnar wires is over $200{,}000$ times higher than across the surrounding hydrocarbon mantle, confirming quasi-one-dimensional coaxial conduction.

### Step 2: Arrhenius Activation Energy and Pre-Factor
From the Arrhenius relation:
\\[
\\ln\\left( \\frac{\\sigma_2}{\\sigma_1} \\right) = -\\frac{E_a}{k_B} \\left( \\frac{1}{T_2} - \\frac{1}{T_1} \\right) = \\frac{E_a}{k_B} \\left( \\frac{T_2 - T_1}{T_1 T_2} \\right)
\\]
Given:
- $\\sigma_1 = 0.450\\text{ S/cm}$, $T_1 = 300.0\\text{ K}$
- $\\sigma_2 = 1.850\\text{ S/cm}$, $T_2 = 360.0\\text{ K}$
- $k_B = 8.61733 \\times 10^{-5}\\text{ eV/K}$
\\[
\\ln\\left( \\frac{1.850}{0.450} \\right) = \\ln(4.1111) = 1.4137
\\]
\\[
\\frac{T_2 - T_1}{T_1 T_2} = \\frac{60.0}{300.0 \\times 360.0} = \\frac{60.0}{108{,}000} = 5.5556 \\times 10^{-4}\\text{ K}^{-1}
\\]
Solve for $E_a$:
\\[
E_a = \\frac{k_B \\times 1.4137}{5.5556 \\times 10^{-4}} = \\frac{(8.61733 \\times 10^{-5}\\text{ eV/K}) \\times 1.4137}{5.5556 \\times 10^{-4}} = \\frac{1.2182 \\times 10^{-4}}{5.5556 \\times 10^{-4}} = 0.21927\\text{ eV} \\approx 0.219\\text{ eV}
\\]
In $\\text{kJ/mol}$ ($1\\text{ eV} = 96.485\\text{ kJ/mol}$):
\\[
E_a = 0.21927 \\times 96.485 = 21.16\\text{ kJ/mol}
\\]
Now compute $\\sigma_0$:
\\[
\\ln \\sigma_0 = \\ln \\sigma_1 + \\frac{E_a}{k_B T_1} = \\ln(0.450) + \\frac{0.21927}{8.61733 \\times 10^{-5} \\times 300.0} = -0.7985 + \\frac{0.21927}{0.025852} = -0.7985 + 8.4817 = 7.6832
\\]
\\[
\\sigma_0 = e^{7.6832} = 2{,}171.5\\text{ S/cm}
\\]

### Step 3: Conductivity at $T = 400.0\text{ K}$
At $T = 400.0\\text{ K}$:
\\[
k_B T = (8.61733 \\times 10^{-5}\\text{ eV/K}) \\times 400.0\\text{ K} = 0.034469\\text{ eV}
\\]
\\[
\\frac{E_a}{k_B T} = \\frac{0.21927}{0.034469} = 6.3614
\\]
\\[
\\sigma_\\parallel(400\\text{ K}) = \\sigma_0 \\exp(-6.3614) = (2{,}171.5\\text{ S/cm}) \\times (1.7270 \\times 10^{-3}) = 3.750\\text{ S/cm}
\\]
Heating to $400\\text{ K}$ increases 1D conductivity to $3.75\\text{ S/cm}$ due to thermally activated polaron hopping."""
        },
        {
            "probNumber": "10.3",
            "title": "Rheology of Supramolecular Metallogels: Storage Modulus & Gelation Point",
            "difficulty": "Foundational",
            "statement": """An oscillatory shear rheological test was conducted on a supramolecular metallogel formed by a terpyridine-functionalized polymer and iron(II) ions in acetonitrile at frequency $\\omega = 10.0\\text{ rad/s}$.
As temperature $T$ is increased:
- Below the gelation temperature ($T < T_{\\text{gel}}$): The material behaves as an elastic solid where the storage modulus $G'$ exceeds the loss modulus $G''$ ($G' > G''$).
- At room temperature ($T = 295.15\\text{ K}$): $G' = 4.80 \\times 10^3\\text{ Pa}$ and $G'' = 3.20 \\times 10^2\\text{ Pa}$.
- The loss factor is defined as $\\tan\\delta = G'' / G'$.
- At the gel-to-sol transition temperature $T_{\\text{gel}} = 335.15\\text{ K}$ ($62.0^\\circ\\text{C}$), the moduli cross over according to the Winter-Chambon criterion: $G'(T_{\\text{gel}}) = G''(T_{\\text{gel}}) = 6.50 \\times 10^2\\text{ Pa}$.
(a) Calculate the loss factor $\\tan\\delta$ at $295.15\\text{ K}$ and confirm that the material meets the rheological definition of a true gel.
(b) Calculate the complex shear modulus $|G^*| = \\sqrt{(G')^2 + (G'')^2}$ and the dynamic viscosity $\\eta^* = |G^*| / \\omega$ at $295.15\\text{ K}$.
(c) The crosslink density $\\nu_e$ (moles of active elastically effective chains per unit volume) can be estimated from the affine rubber elasticity equation $G' \\approx \\nu_e R T$.
Calculate $\\nu_e$ in $\\text{mol/m}^3$ and in $\\text{mol/L}$ at $T = 295.15\\text{ K}$.""",
            "solution": """### Step 1: Loss Factor Evaluation at $295.15\text{ K}$
Given $G' = 4.80 \\times 10^3\\text{ Pa}$ and $G'' = 3.20 \\times 10^2\\text{ Pa}$:
\\[
\\tan\\delta = \\frac{G''}{G'} = \\frac{3.20 \\times 10^2\\text{ Pa}}{4.80 \\times 10^3\\text{ Pa}} = 0.06667 \\approx 0.067
\\]
- **Gel Criterion**:
  A true physical gel requires:
  1. $G' > G''$ across several frequency decades.
  2. $\\tan\\delta = G'' / G' \\ll 1$ (typically $\\tan\\delta < 0.10$).
  Here $\\tan\\delta = 0.067 \\ll 1$, confirming that elastic energy storage heavily dominates viscous dissipation ($93.7\\%$ elastic storage), satisfying the rigorous rheological definition of a gel.

### Step 2: Complex Modulus and Dynamic Viscosity
1. **Complex Modulus ($|G^*|$)**:
\\[
|G^*| = \\sqrt{(G')^2 + (G'')^2} = \\sqrt{(4.80 \\times 10^3)^2 + (3.20 \\times 10^2)^2}
\\]
\\[
|G^*| = \\sqrt{2.304 \\times 10^7 + 1.024 \\times 10^5} = \\sqrt{2.31424 \\times 10^7} = 4.8107 \\times 10^3\\text{ Pa}
\\]
2. **Dynamic Viscosity ($\eta^*$)**:
With angular frequency $\\omega = 10.0\\text{ rad/s}$:
\\[
\\eta^* = \\frac{|G^*|}{\\omega} = \\frac{4.8107 \\times 10^3\\text{ Pa}}{10.0\\text{ rad/s}} = 481.07\\text{ Pa}\\cdot\\text{s}
\\]
The zero-shear dynamic viscosity is approximately $481\\text{ Pa}\\cdot\\text{s}$, over $400{,}000$ times higher than pure acetonitrile solvent ($\eta_{\\text{solvent}} \\approx 0.35\\text{ mPa}\\cdot\\text{s}$).

### Step 3: Elastically Effective Crosslink Density ($\nu_e$)
From affine network elasticity theory:
\\[
G' = \\nu_e R T \\implies \\nu_e = \\frac{G'}{R T}
\\]
With $R = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$ and $T = 295.15\\text{ K}$ ($RT = 2454.01\\text{ J/mol}$):
\\[
\\nu_e = \\frac{4.80 \\times 10^3\\text{ Pa}}{2454.01\\text{ J/mol}} = 1.9560\\text{ mol/m}^3
\\]
In moles per liter ($1\\text{ m}^3 = 1000\\text{ L}$):
\\[
\\nu_e = 1.956 \\times 10^{-3}\\text{ mol/L} = 1.96\\text{ mM}
\\]
The metallogel contains $1.96\\text{ mM}$ of elastically effective coordination crosslinks immobilizing the fluid network."""
        },
        {
            "probNumber": "10.4",
            "title": "Photoisomerization Kinetics of Azobenzene-Doped Metallomesogenic Switches",
            "difficulty": "Intermediate",
            "statement": """A photo-switchable nematic metallomesogen contains a coordinated azobenzene ligand. Under UV illumination ($\\lambda = 365\\text{ nm}$), planar *trans*-azobenzene ($T$) photoisomerizes to non-planar *cis*-azobenzene ($C$):
\\[
T \\xrightleftharpoons[k_{\\text{therm}} + k_{\\text{vis}}]{k_{\\text{UV}}} C
\\]
Under continuous UV irradiation at $T = 298.15\\text{ K}$:
- Forward photochemical rate constant: $k_{\\text{UV}} = 0.120\\text{ s}^{-1}$.
- Reverse photochemical and thermal rate constant: $k_{\\text{rev}} = k_{\\text{therm}} + k_{\\text{vis}} = 0.0150\\text{ s}^{-1}$.
(a) Derive the rate equation for the mole fraction of *cis* isomer, $x_C(t)$, starting from pure *trans* ($x_C(0) = 0$).
(b) Calculate the photostationary state (PSS) mole fraction $x_C^{\\text{PSS}}$ and the relaxation time constant $\\tau$.
(c) The clearing point of the nematic metallomesogen decreases linearly with *cis* content according to:
\\[
T_{\\text{NI}}(x_C) = T_{\\text{NI}}^0 - \\beta x_C
\\]
where $T_{\\text{NI}}^0 = 340.0\\text{ K}$ ($66.85^\\circ\\text{C}$) and $\\beta = 65.0\\text{ K}$.
Determine whether the material undergoes an isothermal nematic-to-isotropic phase transition upon UV irradiation at an operating temperature $T_{\\text{op}} = 300.0\\text{ K}$ ($26.85^\\circ\\text{C}$).""",
            "solution": """### Step 1: Derivation of the Photoisomerization Kinetics
Let $x_T$ and $x_C$ be the mole fractions of the *trans* and *cis* isomers ($x_T + x_C = 1$).
The rate of change of the *cis* fraction is:
\\[
\\frac{dx_C}{dt} = k_{\\text{UV}} x_T - k_{\\text{rev}} x_C = k_{\\text{UV}} (1 - x_C) - k_{\\text{rev}} x_C = k_{\\text{UV}} - (k_{\\text{UV}} + k_{\\text{rev}}) x_C
\\]
Let $k_{\\text{total}} = k_{\\text{UV}} + k_{\\text{rev}}$:
\\[
\\frac{dx_C}{dt} + k_{\\text{total}} x_C = k_{\\text{UV}}
\\]
Integrating with initial condition $x_C(0) = 0$:
\\[
x_C(t) = \\frac{k_{\\text{UV}}}{k_{\\text{total}}} \\left( 1 - e^{-k_{\\text{total}} t} \\right) = x_C^{\\text{PSS}} \\left( 1 - e^{-t / \\tau} \\right)
\\]

### Step 2: Photostationary State (PSS) and Time Constant
Given $k_{\\text{UV}} = 0.120\\text{ s}^{-1}$ and $k_{\\text{rev}} = 0.0150\\text{ s}^{-1}$:
\\[
k_{\\text{total}} = 0.120 + 0.0150 = 0.1350\\text{ s}^{-1}
\\]
The photostationary state fraction of *cis* isomer is:
\\[
x_C^{\\text{PSS}} = \\frac{k_{\\text{UV}}}{k_{\\text{total}}} = \\frac{0.120\\text{ s}^{-1}}{0.1350\\text{ s}^{-1}} = 0.8889 \\implies 88.89\\%
\\]
The relaxation time constant is:
\\[
\\tau = \\frac{1}{k_{\\text{total}}} = \\frac{1}{0.1350\\text{ s}^{-1}} = 7.407\\text{ s}
\\]
The system reaches $95\\%$ of its photostationary state in $3 \\tau \\approx 22.2\\text{ seconds}$.

### Step 3: Isothermal Phase Transition Assessment
At the PSS with $x_C^{\\text{PSS}} = 0.8889$:
\\[
T_{\\text{NI}}(x_C^{\\text{PSS}}) = T_{\\text{NI}}^0 - \\beta x_C^{\\text{PSS}} = 340.0\\text{ K} - (65.0\\text{ K}) \\times 0.8889 = 340.0 - 57.78 = 282.22\\text{ K} = 9.07^\\circ\\text{C}
\\]
Now compare with the operating temperature $T_{\\text{op}} = 300.0\\text{ K}$ ($26.85^\\circ\\text{C}$):
- Before UV irradiation ($x_C = 0$):
  $T_{\\text{op}} = 300.0\\text{ K} < T_{\\text{NI}}^0 = 340.0\\text{ K} \\implies$ The material is in the ordered **nematic mesophase**.
- At PSS under UV irradiation ($x_C = 0.8889$):
  $T_{\\text{op}} = 300.0\\text{ K} > T_{\\text{NI}}(\\text{PSS}) = 282.22\\text{ K} \\implies$ The clearing temperature has been driven below the ambient temperature!
- **Conclusion**:
  UV light triggers an **isothermal nematic-to-isotropic phase transition**.
  The bent *cis* isomers disrupt the nematic order parameter ($S \\rightarrow 0$), melting the anisotropic birefringent mesophase into a clear isotropic liquid at room temperature within seconds."""
        },
        {
            "probNumber": "10.5",
            "title": "Marcus Theory of Charge Transfer in Columnar Metalloporphyrin Wires",
            "difficulty": "Intermediate",
            "statement": """Self-assembled columnar stacks of zinc(II) octaethylporphyrin act as 1D hole conductors.
The intermolecular charge transfer rate between adjacent porphyrin rings (interplanar spacing $d = 3.40\\text{ Å}$) is governed by non-adiabatic **Marcus electron transfer theory**:
\\[
k_{\\text{ET}} = \\frac{2\\pi}{\\hbar} \\frac{|V|^2}{\\sqrt{4\\pi \\lambda k_B T}} \\exp\\left( -\\frac{(\\Delta G^\circ + \\lambda)^2}{4\\lambda k_B T} \\right)
\\]
For self-exchange hole hopping between identical neutral and radical cation porphyrins ($\text{ZnP} + \\text{ZnP}^{+\\bullet} \\rightleftharpoons \\text{ZnP}^{+\\bullet} + \\text{ZnP}$), the standard free energy of reaction is $\\Delta G^\circ = 0$.
At $T = 298.15\\text{ K}$:
- Electronic coupling matrix element: $|V| = 0.0520\\text{ eV} = 8.331 \\times 10^{-21}\\text{ J}$
- Total reorganization energy: $\\lambda = 0.220\\text{ eV} = 3.525 \\times 10^{-20}\\text{ J}$
- Thermal energy: $k_B T = 0.02569\\text{ eV} = 4.116 \\times 10^{-21}\\text{ J}$
(a) Calculate the Marcus activation barrier $\\Delta G^\\ddagger = \\lambda / 4$ in $\\text{eV}$ and in $\\text{kJ/mol}$.
(b) Calculate the pre-exponential factor $\\nu_{\\text{el}} = \\frac{2\\pi}{\\hbar} \\frac{|V|^2}{\\sqrt{4\\pi \\lambda k_B T}}$ in $\\text{s}^{-1}$.
(c) Calculate the hole transfer rate constant $k_{\\text{ET}}$ and the theoretical 1D hole mobility $\\mu_h = \\frac{e d^2 k_{\\text{ET}}}{k_B T}$ in $\\text{cm}^2/(\\text{V}\\cdot\\text{s})$.""",
            "solution": """### Step 1: Marcus Activation Barrier
For symmetric self-exchange ($\\Delta G^\circ = 0$):
\\[
\\Delta G^\\ddagger = \\frac{(\\Delta G^\\circ + \\lambda)^2}{4\\lambda} = \\frac{\\lambda^2}{4\\lambda} = \\frac{\\lambda}{4}
\\]
With $\\lambda = 0.220\\text{ eV}$:
\\[
\\Delta G^\\ddagger = \\frac{0.220\\text{ eV}}{4} = 0.0550\\text{ eV}
\\]
In $\\text{kJ/mol}$ ($1\\text{ eV} = 96.485\\text{ kJ/mol}$):
\\[
\\Delta G^\\ddagger = 0.0550 \\times 96.485 = 5.307\\text{ kJ/mol}
\\]
The barrier is small ($5.3\\text{ kJ/mol}$), readily overcome by thermal fluctuations at room temperature.

### Step 2: Pre-Exponential Factor ($\nu_{\text{el}}$)
Calculate the denominator:
\\[
4\\pi \\lambda k_B T = 4\\pi \\times (3.525 \\times 10^{-20}\\text{ J}) \\times (4.116 \\times 10^{-21}\\text{ J}) = 1.8233 \\times 10^{-39}\\text{ J}^2
\\]
\\[
\\sqrt{4\\pi \\lambda k_B T} = \\sqrt{1.8233 \\times 10^{-39}} = 4.2700 \\times 10^{-20}\\text{ J}
\\]
Electronic coupling squared:
\\[
|V|^2 = (8.331 \\times 10^{-21}\\text{ J})^2 = 6.9406 \\times 10^{-41}\\text{ J}^2
\\]
With $\\hbar = 1.05457 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$:
\\[
\\nu_{\\text{el}} = \\frac{2\\pi}{1.05457 \\times 10^{-34}\\text{ J}\\cdot\\text{s}} \\times \\frac{6.9406 \\times 10^{-41}\\text{ J}^2}{4.2700 \\times 10^{-20}\\text{ J}}
\\]
\\[
\\nu_{\\text{el}} = (5.9580 \\times 10^{34}\\text{ J}^{-1}\\text{s}^{-1}) \\times (1.6254 \\times 10^{-21}\\text{ J}) = 9.684 \\times 10^{13}\\text{ s}^{-1}
\\]

### Step 3: Rate Constant and Charge Carrier Mobility
1. **Exponential Boltzmann Factor**:
\\[
\\frac{\\Delta G^\\ddagger}{k_B T} = \\frac{0.0550\\text{ eV}}{0.02569\\text{ eV}} = 2.1409
\\]
\\[
\\exp(-2.1409) = 0.11755
\\]
Rate constant:
\\[
k_{\\text{ET}} = \\nu_{\\text{el}} \\exp(-2.1409) = (9.684 \\times 10^{13}\\text{ s}^{-1}) \\times 0.11755 = 1.1384 \\times 10^{13}\\text{ s}^{-1}
\\]
The hopping frequency is over $11\\text{ THz}$.

2. **1D Hole Mobility ($\mu_h$)**:
Given $d = 3.40\\text{ Å} = 3.40 \\times 10^{-10}\\text{ m} \\implies d^2 = 1.156 \\times 10^{-19}\\text{ m}^2$:
\\[
\\mu_h = \\frac{e d^2 k_{\\text{ET}}}{k_B T} = \\frac{(1.60218 \\times 10^{-19}\\text{ C}) \\times (1.156 \\times 10^{-19}\\text{ m}^2) \\times (1.1384 \\times 10^{13}\\text{ s}^{-1})}{4.116 \\times 10^{-21}\\text{ J}}
\\]
\\[
\\mu_h = \\frac{2.1084 \\times 10^{-24}}{4.116 \\times 10^{-21}} = 5.122 \\times 10^{-4}\\text{ m}^2/(\\text{V}\\cdot\\text{s})
\\]
Convert to $\\text{cm}^2/(\\text{V}\\cdot\\text{s})$ ($1\\text{ m}^2 = 10^4\\text{ cm}^2$):
\\[
\\mu_h = 5.122\\text{ cm}^2/(\\text{V}\\cdot\\text{s}) \\approx 5.12\\text{ cm}^2/(\\text{V}\\cdot\\text{s})
\\]
The 1D columnar zinc porphyrin stack displays a high hole mobility of $5.12\\text{ cm}^2/(\\text{V}\\cdot\\text{s})$, matching state-of-the-art organic single crystals."""
        },
        {
            "probNumber": "10.6",
            "title": "Dynamic Combinatorial Library Amplification: Thermodynamic Selection",
            "difficulty": "Intermediate",
            "statement": """A Dynamic Combinatorial Library (DCL) is generated by reversible hydrazone exchange between a dialdehyde core ($A$) and two competing hydrazide building blocks ($B_1$ and $B_2$) in aqueous solution at $T = 298.15\\text{ K}$.
The library generates three macrocyclic bis-hydrazones:
- Homodimer 1: $M_{11} = [A(B_1)_2]$
- Heterodimer: $M_{12} = [A(B_1)(B_2)]$
- Homodimer 2: $M_{22} = [A(B_2)_2]$
In the absence of a template, dynamic exchange reaches statistical equilibrium where all three macrocycles have identical formation free energies:
\\[
[M_{11}]_0 : [M_{12}]_0 : [M_{22}]_0 = 1 : 2 : 1 \\quad (25\\% : 50\\% : 25\\%)
\\]
A biological guest template ($T$) is introduced at concentration $[T] = 1.00\\text{ mM}$, which binds selectively to $M_{11}$ with association constant $K_1 = 5.00 \\times 10^4\\text{ M}^{-1}$, but does not bind $M_{12}$ or $M_{22}$ ($K_{12} = K_{22} = 0$).
(a) According to Le Chatelier's principle, explain how binding of $T$ shifts the entire dynamic equilibrium toward the generation of $M_{11}$.
(b) The effective equilibrium constant for $M_{11}$ in the presence of template is $K_{\\text{eff}} = K_0 (1 + K_1 [T])$. Calculate the amplification factor $\\alpha = 1 + K_1 [T]$.
(c) If the total pool of $A$ is $C_A = 1.00\\text{ mM}$, calculate the new equilibrium percentage fraction of $M_{11}$ in the presence of template.""",
            "solution": """### Step 1: Thermodynamic Basis of Template Amplification
In a Dynamic Combinatorial Library (DCL), all macrocyclic species are connected by dynamic reversible covalent bonds (hydrazone metathesis):
\\[
M_{22} + 2\\,B_1 \\xrightleftharpoons{} M_{12} + B_1 + B_2 \\xrightleftharpoons{} M_{11} + 2\\,B_2
\\]
When template $T$ is introduced:
- $T$ binds selectively to $M_{11}$ to form complex $[M_{11}\\cdot T]$.
- Complexation removes free $M_{11}$ from the exchange equilibrium.
- According to Le Chatelier's principle, the chemical equilibrium responds by consuming the other macrocycles ($M_{12}$ and $M_{22}$) and re-allocating building block $B_1$ to synthesize more $M_{11}$.
- The library autonomously "evolves" to amplify the best-binding receptor from the mixture.

### Step 2: Amplification Factor Calculation
Given $K_1 = 5.00 \\times 10^4\\text{ M}^{-1}$ and $[T] = 1.00\\text{ mM} = 1.00 \\times 10^{-3}\\text{ M}$:
\\[
\\alpha = 1 + K_1 [T] = 1 + (5.00 \\times 10^4\\text{ M}^{-1}) \\times (1.00 \\times 10^{-3}\\text{ M}) = 1 + 50.0 = 51.0
\\]
The apparent thermodynamic stability of $M_{11}$ is enhanced by a factor of $51.0$.

### Step 3: New Equilibrium Fraction of $M_{11}$
In the unperturbed library, the statistical weights are:
- $w(M_{11}) = 1$
- $w(M_{12}) = 2$
- $w(M_{22}) = 1$
Total weight $= 1 + 2 + 1 = 4$.
In the presence of the selective template, the statistical weight of $M_{11}$ is multiplied by $\\alpha = 51.0$:
- $w'(M_{11}) = 1 \\times 51.0 = 51.0$
- $w'(M_{12}) = 2$
- $w'(M_{22}) = 1$
The new total statistical weight is:
\\[
W_{\\text{total}}' = 51.0 + 2.0 + 1.0 = 54.0
\\]
The new percentage fraction of $M_{11}$ (free + bound) is:
\\[
\\% M_{11} = \\frac{w'(M_{11})}{W_{\\text{total}}'} \\times 100\\% = \\frac{51.0}{54.0} \\times 100\\% = 94.44\\%
\\]
The template drives the library from its initial statistical abundance of $25\\%$ to an overwhelming **$94.4\\%$** purity, illustrating the power of template-directed dynamic combinatorial selection."""
        },
        {
            "probNumber": "10.7",
            "title": "Exciton Diffusion Length in Supramolecular Donor-Acceptor Heterojunctions",
            "difficulty": "Advanced",
            "statement": """In a bulk heterojunction organic solar cell, supramolecular self-assembly organizes an electron-donor hexabenzocoronene (HBC) and an electron-acceptor perylenediimide (PDI) into interpenetrating 1D columnar nanodomains.
A photo-generated singlet exciton in the HBC donor domain has a fluorescence lifetime $\\tau_{\\text{fl}} = 1.20\\text{ ns} = 1.20 \\times 10^{-9}\\text{ s}$.
Energy transfer occurs by Förster Resonance Energy Transfer (FRET) with an exciton hopping diffusion coefficient $D_{\\text{exc}} = 3.60 \\times 10^{-3}\\text{ cm}^2/\\text{s} = 3.60 \\times 10^{-7}\\text{ m}^2/\\text{s}$.
(a) Calculate the 1D and 3D exciton diffusion lengths:
    $L_{D,1\\text{D}} = \\sqrt{2 D_{\\text{exc}} \\tau_{\\text{fl}}}$ and $L_{D,3\\text{D}} = \\sqrt{6 D_{\\text{exc}} \\tau_{\\text{fl}}}$.
(b) The exciton harvesting efficiency $\\eta_{\\text{ED}}$ in a cylindrical donor domain of radius $R$ is given by the steady-state diffusion equation:
\\[
\\eta_{\\text{ED}} = 1 - \\frac{2 L_D}{R} \\frac{I_1(R / L_D)}{I_0(R / L_D)}
\\]
where $I_0$ and $I_1$ are modified Bessel functions. For $R \\ll L_D$, $\\eta_{\\text{ED}} \\approx 1 - \\frac{R^2}{8 L_D^2}$.
If the target harvesting efficiency is $\\eta_{\\text{ED}} \\ge 95\\%$, calculate the maximum allowable donor domain radius $R_{\\max}$.
(c) Explain why unguided macro-phase separation ($R > 100\\text{ nm}$) causes severe photovoltaic performance failure, whereas supramolecular nanophase separation achieves high efficiency.""",
            "solution": """### Step 1: Exciton Diffusion Lengths
Given $D_{\\text{exc}} = 3.60 \\times 10^{-7}\\text{ m}^2/\\text{s}$ and $\\tau_{\\text{fl}} = 1.20 \\times 10^{-9}\\text{ s}$:
\\[
D_{\\text{exc}} \\tau_{\\text{fl}} = (3.60 \\times 10^{-7}\\text{ m}^2/\\text{s}) \\times (1.20 \\times 10^{-9}\\text{ s}) = 4.320 \\times 10^{-16}\\text{ m}^2
\\]
1. **1D Diffusion Length**:
\\[
L_{D,1\\text{D}} = \\sqrt{2 D_{\\text{exc}} \\tau_{\\text{fl}}} = \\sqrt{2 \\times 4.320 \\times 10^{-16}} = \\sqrt{8.640 \\times 10^{-16}} = 2.939 \\times 10^{-8}\\text{ m} = 29.39\\text{ nm}
\\]
2. **3D Diffusion Length**:
\\[
L_{D,3\\text{D}} = \\sqrt{6 D_{\\text{exc}} \\tau_{\\text{fl}}} = \\sqrt{6 \\times 4.320 \\times 10^{-16}} = \\sqrt{2.592 \\times 10^{-15}} = 5.091 \\times 10^{-8}\\text{ m} = 50.91\\text{ nm}
\\]
A singlet exciton can diffuse approximately $29.4\\text{ nm}$ along the column before radiative or non-radiative decay occurs.

### Step 2: Maximum Domain Radius for $95\%$ Harvesting
Given $\\eta_{\\text{ED}} \\ge 0.95$:
\\[
1 - \\frac{R^2}{8 L_D^2} \\ge 0.95 \\implies \\frac{R^2}{8 L_D^2} \\le 0.050
\\]
\\[
R^2 \\le 0.050 \\times 8 L_D^2 = 0.400 \\, L_D^2
\\]
\\[
R \\le \\sqrt{0.400} \\, L_D = 0.63245 \\, L_D
\\]
With $L_D = 29.39\\text{ nm}$:
\\[
R_{\\max} = 0.63245 \\times 29.39\\text{ nm} = 18.59\\text{ nm}
\\]
To harvest at least $95\\%$ of all photo-generated excitons, the donor domain radius must not exceed $18.6\\text{ nm}$ (domain diameter $\\le 37\\text{ nm}$).

### Step 3: Mechanism of Photovoltaic Failure in Macro-Phase Separation
- In macroscopic phase separation ($R > 100\\text{ nm}$), excitons generated in the interior of the donor domains must travel $>100\\text{ nm}$ to find a donor-acceptor interface.
- Because $R \\gg L_D$ ($100\\text{ nm} \\gg 29.4\\text{ nm}$), over $90\\%$ of excitons decay radiatively (fluorescence) or heat up non-radiatively before ever reaching the interface, yielding near-zero charge separation ($PCE < 1\\%$).
- In contrast, supramolecular self-assembly organizes the donor and acceptor into interpenetrating bicontinuous networks with domain sizes precisely matching the nanoscale exciton diffusion length ($15 - 25\\text{ nm}$), allowing $>95\\%$ of all excitons to dissociate into free charge carriers."""
        },
        {
            "probNumber": "10.8",
            "title": "Viscoelasticity and Stress Relaxation in Reversible Networks: Maxwell-Green Model",
            "difficulty": "Advanced",
            "statement": """A supramolecular telechelic polymer network is held by reversible metal-bis(terpyridine) coordination junctions ($M^{2+}-\\text{terpy}_2$).
The viscoelastic stress relaxation following a step shear strain $\\gamma_0$ is described by the **Maxwell model**:
\\[
\\sigma(t) = G_0 \\, \\gamma_0 \\exp(-t / \\tau_R)
\\]
where $G_0$ is the instantaneous plateau shear modulus and $\\tau_R$ is the terminal structural relaxation time.
In transient network theory (Green-Tobolsky model), $\\tau_R$ is governed by the unimolecular dissociation rate of the coordination crosslinks:
\\[
\\tau_R = \\frac{1}{k_{\\text{off}}} = \\frac{1}{A} \\exp\\left( \\frac{E_a}{R T} \\right)
\\]
For a zinc(II) metallopolymer network:
- Arrhenius parameters: $A = 1.00 \\times 10^{13}\\text{ s}^{-1}$, $E_a = 78.50\\text{ kJ/mol}$.
- Plateau modulus: $G_0 = 1.25 \\times 10^5\\text{ Pa}$.
(a) Calculate the dissociation rate constant $k_{\\text{off}}$ and the relaxation time $\\tau_R$ at $T = 298.15\\text{ K}$.
(b) Calculate the zero-shear dynamic viscosity $\\eta_0 = G_0 \\tau_R$ in $\\text{Pa}\\cdot\\text{s}$.
(c) At what temperature $T_{\\text{fast}}$ does the relaxation time accelerate to $\\tau_R = 1.00\\text{ ms} = 1.00 \\times 10^{-3}\\text{ s}$, allowing rapid self-healing or liquid processing?""",
            "solution": """### Step 1: Dissociation Rate and Relaxation Time at $298.15\text{ K}$
Given $E_a = 78.50\\text{ kJ/mol} = 78{,}500\\text{ J/mol}$ and $A = 1.00 \\times 10^{13}\\text{ s}^{-1}$:
At $T = 298.15\\text{ K}$, $RT = 8.31446 \\times 298.15 = 2478.96\\text{ J/mol}$:
\\[
\\frac{E_a}{RT} = \\frac{78{,}500\\text{ J/mol}}{2478.96\\text{ J/mol}} = 31.6665
\\]
The dissociation rate constant is:
\\[
k_{\\text{off}} = A \\exp\\left( -\\frac{E_a}{RT} \\right) = (1.00 \\times 10^{13}\\text{ s}^{-1}) \\times e^{-31.6665}
\\]
\\[
e^{-31.6665} = 1.7677 \\times 10^{-14}
\\]
\\[
k_{\\text{off}} = (1.00 \\times 10^{13}) \\times (1.7677 \\times 10^{-14}) = 0.17677\\text{ s}^{-1}
\\]
The terminal relaxation time is:
\\[
\\tau_R = \\frac{1}{k_{\\text{off}}} = \\frac{1}{0.17677\\text{ s}^{-1}} = 5.657\\text{ s}
\\]
At room temperature, the coordination junctions open once every $5.66\\text{ seconds}$.

### Step 2: Zero-Shear Viscosity Calculation
The zero-shear viscosity for a Maxwell fluid is:
\\[
\\eta_0 = G_0 \\, \\tau_R = (1.25 \\times 10^5\\text{ Pa}) \\times (5.657\\text{ s}) = 7.071 \\times 10^5\\text{ Pa}\\cdot\\text{s}
\\]
The zero-shear viscosity is over $700{,}000\\text{ Pa}\\cdot\\text{s}$, giving the material the macroscopic mechanical consistency of a stiff rubber.

### Step 3: Temperature for $\tau_R = 1.00\text{ ms}$
Target condition:
\\[
\\tau_R = 1.00 \\times 10^{-3}\\text{ s} \\implies k_{\\text{off}} = \\frac{1}{1.00 \\times 10^{-3}\\text{ s}} = 1{,}000\\text{ s}^{-1}
\\]
From the Arrhenius equation:
\\[
1{,}000 = A \\exp\\left( -\\frac{E_a}{R T_{\\text{fast}}} \\right) \\implies \\exp\\left( \\frac{E_a}{R T_{\\text{fast}}} \\right) = \\frac{1.00 \\times 10^{13}}{1{,}000} = 1.00 \\times 10^{10}
\\]
Take natural logarithm:
\\[
\\frac{E_a}{R T_{\\text{fast}}} = \\ln(1.00 \\times 10^{10}) = 10 \\times \\ln(10) = 23.0259
\\]
Solve for $T_{\\text{fast}}$:
\\[
T_{\\text{fast}} = \\frac{E_a}{R \\times 23.0259} = \\frac{78{,}500\\text{ J/mol}}{(8.31446\\text{ J/(mol}\\cdot\\text{K)}) \\times 23.0259} = \\frac{78{,}500}{191.447} = 410.03\\text{ K} = 136.88^\\circ\\text{C}
\\]
Heating the supramolecular elastomer to $137^\\circ\\text{C}$ accelerates the bond exchange rate to $1{,}000\\text{ s}^{-1}$, dropping the relaxation time to 1 millisecond and allowing the material to melt and flow like a low-viscosity liquid for thermal recycling and molding."""
        },
        {
            "probNumber": "10.9",
            "title": "Supramolecular Logic Gates: Reversible Two-Input AND Gate Photophysics",
            "difficulty": "Advanced",
            "statement": """A fluorescent supramolecular sensor consists of an anthracene fluorophore ($F$) covalently tethered between a benzo-15-crown-5 ether ($C$, Input 1: $\\text{Na}^+$) and a tertiary aliphatic amine ($N$, Input 2: $\\text{H}^+$).
The sensor operates as a two-input molecular **AND logic gate**:
- In the absence of inputs (state $(0, 0)$): Both the crown ether oxygen lone pairs and the amine nitrogen lone pair quench anthracene fluorescence via independent Photoinduced Electron Transfer (PET):
  $k_{\\text{PET},1} = 4.50 \\times 10^9\\text{ s}^{-1}$ (from crown), $k_{\\text{PET},2} = 6.00 \\times 10^9\\text{ s}^{-1}$ (from amine).
- Natural radiative decay of anthracene is $k_r = 2.00 \\times 10^7\\text{ s}^{-1}$, and internal non-radiative decay is $k_{\\text{nr}} = 8.00 \\times 10^7\\text{ s}^{-1}$.
- Binding $\\text{Na}^+$ to the crown completely blocks $k_{\\text{PET},1}$ ($k_{\\text{PET},1} = 0$).
- Protonating the amine with $\\text{H}^+$ completely blocks $k_{\\text{PET},2}$ ($k_{\\text{PET},2} = 0$).
(a) The fluorescence quantum yield is $\\Phi_F = \\frac{k_r}{k_r + k_{\\text{nr}} + k_{\\text{PET},1} + k_{\\text{PET},2}}$.
Calculate $\\Phi_F$ for the four input states:
    (i) State $(0, 0)$: No inputs
    (ii) State $(1, 0)$: High $\\text{Na}^+$, Low $\\text{H}^+$
    (iii) State $(0, 1)$: Low $\\text{Na}^+$, High $\\text{H}^+$
    (iv) State $(1, 1)$: High $\\text{Na}^+$, High $\\text{H}^+$
(b) Calculate the fluorescence enhancement switching ratio $\\Phi_F(1, 1) / \\Phi_F(0, 0)$.
(c) Construct the Boolean truth table for this system with threshold $\\Phi_{\\text{th}} = 0.10$ and confirm that it functions as a digital AND gate.""",
            "solution": """### Step 1: Fluorescence Quantum Yields for the Four States
The natural decay rate without PET is:
\\[
k_0 = k_r + k_{\\text{nr}} = 2.00 \\times 10^7\\text{ s}^{-1} + 8.00 \\times 10^7\\text{ s}^{-1} = 1.00 \\times 10^8\\text{ s}^{-1}
\\]
With $k_r = 2.00 \\times 10^7\\text{ s}^{-1}$:
\\[
\\Phi_F = \\frac{2.00 \\times 10^7}{k_0 + k_{\\text{PET},1} + k_{\\text{PET},2}}
\\]

1. **State $(0, 0)$ (Neither Input Present)**:
$k_{\\text{PET},1} = 4.50 \\times 10^9\\text{ s}^{-1}$, $k_{\\text{PET},2} = 6.00 \\times 10^9\\text{ s}^{-1}$.
Total decay rate:
\\[
k_{\\text{total}} = 1.00 \\times 10^8 + 4.50 \\times 10^9 + 6.00 \\times 10^9 = 1.060 \\times 10^{10}\\text{ s}^{-1}
\\]
\\[
\\Phi_F(0, 0) = \\frac{2.00 \\times 10^7}{1.060 \\times 10^{10}} = 1.8868 \\times 10^{-3} \\approx 0.0019 \\implies 0.19\\%
\\]
Fluorescence is deeply quenched.

2. **State $(1, 0)$ ($\text{Na}^+$ Present, $\text{H}^+$ Absent)**:
$k_{\\text{PET},1} = 0$, $k_{\\text{PET},2} = 6.00 \\times 10^9\\text{ s}^{-1}$.
Total decay rate:
\\[
k_{\\text{total}} = 1.00 \\times 10^8 + 6.00 \\times 10^9 = 6.100 \\times 10^9\\text{ s}^{-1}
\\]
\\[
\\Phi_F(1, 0) = \\frac{2.00 \\times 10^7}{6.100 \\times 10^9} = 3.2787 \\times 10^{-3} \\approx 0.0033 \\implies 0.33\\%
\\]
Fluorescence remains quenched by the amine PET pathway.

3. **State $(0, 1)$ ($\text{Na}^+$ Absent, $\text{H}^+$ Present)**:
$k_{\\text{PET},1} = 4.50 \\times 10^9\\text{ s}^{-1}$, $k_{\\text{PET},2} = 0$.
Total decay rate:
\\[
k_{\\text{total}} = 1.00 \\times 10^8 + 4.50 \\times 10^9 = 4.600 \\times 10^9\\text{ s}^{-1}
\\]
\\[
\\Phi_F(0, 1) = \\frac{2.00 \\times 10^7}{4.600 \\times 10^9} = 4.3478 \\times 10^{-3} \\approx 0.0043 \\implies 0.43\\%
\\]
Fluorescence remains quenched by the crown ether PET pathway.

4. **State $(1, 1)$ (Both $\text{Na}^+$ and $\text{H}^+$ Present)**:
Both PET pathways are completely shut off: $k_{\\text{PET},1} = k_{\\text{PET},2} = 0$.
Total decay rate:
\\[
k_{\\text{total}} = k_0 = 1.00 \\times 10^8\\text{ s}^{-1}
\\]
\\[
\\Phi_F(1, 1) = \\frac{2.00 \\times 10^7}{1.00 \\times 10^8} = 0.2000 \\implies 20.0\\%
\\]
Fluorescence turns brightly ON!

### Step 2: Fluorescence Switching Ratio
The switching on-off ratio is:
\\[
\\text{Ratio} = \\frac{\\Phi_F(1, 1)}{\\Phi_F(0, 0)} = \\frac{0.2000}{1.8868 \\times 10^{-3}} = 106.0
\\]
Binding both inputs enhances the fluorescence intensity by a factor of $106$.

### Step 3: Boolean Truth Table
With output threshold $\\Phi_{\\text{th}} = 0.10$ ($10\\%$ quantum yield):
| Input 1 ($\text{Na}^+$) | Input 2 ($\text{H}^+$) | $\Phi_F$ | Output Signal |
| :---: | :---: | :---: | :---: |
| 0 | 0 | $0.0019 < 0.10$ | **0 (OFF)** |
| 1 | 0 | $0.0033 < 0.10$ | **0 (OFF)** |
| 0 | 1 | $0.0043 < 0.10$ | **0 (OFF)** |
| 1 | 1 | $0.2000 > 0.10$ | **1 (ON)** |

The output is $1$ if and only if both inputs are simultaneously $1$.
The supramolecular complex operates as a true digital **AND logic gate** at the single-molecule scale."""
        }
    ]

    return {
        "id": "unit-10",
        "number": 10,
        "title": "Metallomesogens & Optoelectronic Supramolecular Materials",
        "leadSummary": "Metal complexes as liquid crystalline materials, coordination geometry and mesophase stability, calamitic Schiff-base and beta-diketonate metallomesogens, discotic metallophthalocyanines and 1D coaxial electronic conduction, supramolecular gels (LMWGs and metallogels), stimuli-responsive and self-healing supramolecular polymers, optoelectronic applications (OFETs, OPVs, OLEDs), and frontiers of supramolecular technology (dynamic combinatorial libraries and molecular logic gates).",
        "simulations": ["sim_supra_metallomesogen_columnar"],
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u10 = get_unit_10()
    print(f"Unit 10 generated: {len(u10['sections'])} sections, {len(u10['problems'])} problems.")
