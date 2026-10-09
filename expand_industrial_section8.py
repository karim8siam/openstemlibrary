# -*- coding: utf-8 -*-
"""
expand_industrial_section8.py
Injects Section 8 across all 10 units of Industrial Chemistry.
Brings total sections from 70 to 80.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def inject_section_8(units):
    sec8_dict = {
        "unit-1-textiles-and-dyes": {
            "id": "sec-1-8",
            "secNumber": "1.8",
            "title": "Dyeing Mechanics, Dye-Fiber Affinity & Textile Wastewater Effluent Treatment",
            "content": r"""Industrial textile coloration is an interfacial mass-transfer process where dissolved dyestuff molecules diffuse from an aqueous dye bath across a stagnant hydrodynamic boundary layer, adsorb onto the fiber surface, and diffuse into the amorphous polymer interior, where they are locked by covalent, ionic, hydrogen, or van der Waals interactions.

### 1. Dye Sorption Thermodynamics & Isotherms
Dye uptake follows three classic thermodynamic adsorption isotherms:
1. **Langmuir Isotherm**: Operates in systems with discrete, saturable ionic binding sites (e.g., acid dyes on cationic protonated ammonium groups of wool and nylon, $-\text{NH}_3^+$):
   $$[D]_f = \frac{[S]_f K_L [D]_s}{1 + K_L [D]_s}$$
   where $[D]_f$ is dye concentration in fiber, $[S]_f$ is saturation capacity of ionic sites, $[D]_s$ is equilibrium dye concentration in solution, and $K_L$ is the Langmuir adsorption equilibrium constant.
2. **Freundlich Isotherm**: Characteristic of non-uniform surfaces and dye aggregation:
   $$[D]_f = K_F [D]_s^{1/n}$$
3. **Nernst Partition Isotherm**: Governs non-ionic disperse dyes dissolving into hydrophobic polyester (PET):
   $$[D]_f = K_D [D]_s$$
   The dye partitions between the aqueous phase and amorphous PET matrix acting as a solid-state hydrophobic solvent.

### 2. Reactive Dye Fixation & Hydrolysis Kinetics
Reactive dyes form covalent bonds with cellulose hydroxyl groups at alkaline $\text{pH}$ ($10.5 - 11.5$):
- **Covalent Fixation Reaction**:
  $$\text{Dye-SO}_2\text{-CH=CH}_2 + \text{Cell-O}^- \overset{k_f}{\longrightarrow} \text{Dye-SO}_2\text{-CH}_2\text{-CH}_2\text{-O-Cell}$$
- **Parasitic Hydrolysis Reaction**:
  $$\text{Dye-SO}_2\text{-CH=CH}_2 + \text{OH}^- \overset{k_h}{\longrightarrow} \text{Dye-SO}_2\text{-CH}_2\text{-CH}_2\text{-OH (Hydrolyzed Inactive Dye)}$$
Fixation efficiency ($T_f$) is given by the kinetic competition ratio:
$$T_f = \frac{k_f [\text{Cell-O}^-]}{k_f [\text{Cell-O}^-] + k_h [\text{OH}^-]}$$
Typically, $15 - 30\%$ of reactive dye hydrolyzes into an unfixable form, requiring intense boiling soap washes and creating highly colored wastewater effluents.

### 3. Textile Wastewater Effluent Remediation
Textile dyeing wastewater exhibits high Chemical Oxygen Demand ($\text{COD} = 1,000 - 3,000\text{ mg/L}$), intense coloration (residual azo, anthraquinone dyes), and high salinity ($30 - 60\text{ g/L NaCl / Na}_2\text{SO}_4$):
- **Advanced Oxidation Processes (AOPs / Fenton Reaction)**:
  Hydrogen peroxide is catalyzed by iron(II) at $\text{pH } 3.0$ to generate non-selective hydroxyl radicals ($\cdot\text{OH}$, redox potential $+2.80\text{ V}$):
  $$\text{Fe}^{2+} + \text{H}_2\text{O}_2 \longrightarrow \text{Fe}^{3+} + \cdot\text{OH} + \text{OH}^-$$
  Hydroxyl radicals rapidly attack conjugated chromophoric azo linkages ($-\text{N=N}-$), decolorizing the wastewater in $< 30\text{ minutes}$.
- **Coagulation-Flocculation**: Polyaluminum chloride ($\text{PAC}$) and polyacrylamide destabilize colloidal dispersed dyestuffs.
- **Biological Treatment (Moving Bed Biofilm Reactor / MBBR)**: Aerobic microbial consortium degrades organic auxochromes and reduces $\text{BOD}_5$ below $30\text{ mg/L}$."""
        },

        "unit-2-fertilizer-industries": {
            "id": "sec-2-8",
            "secNumber": "2.8",
            "title": "Advanced Granulation Engineering, Controlled-Release Fertilizers & Carbon Capture Integration",
            "leadSummary": "Granulation fluid mechanics, slow-release urea coatings, and ammonia plant CO2 capture.",
            "content": r"""Modern fertilizer manufacturing has transitioned from simple prilling towers to high-efficiency fluid-bed granulation and advanced controlled-release formulations engineered to prevent nutrient leaching and greenhouse gas volatilization.

### 1. Fluid-Bed Granulation vs Prilling Tower Aerodynamics
- **Prilling Towers**: Molten urea or ammonium nitrate ($> 99.5\%$ melt) is sprayed through rotating perforated buckets at the top of a $60 - 80\text{ m}$ natural-draft concrete tower. Falling droplets cool and solidify against ascending ambient air. Prills are small ($1.2 - 2.0\text{ mm}$), mechanically fragile, and prone to caking and dusting.
- **Fluid-Bed Granulation**: Seed granules are fluidized on an oscillating perforated deck by conditioned air. Molten urea is atomized through thousands of acoustic spray nozzles, coating the circulating seeds in successive onion-skin layers. Granules achieve $2.5 - 4.5\text{ mm}$ diameter, $3\times$ higher crushing strength ($> 35\text{ N}$ vs $12\text{ N}$ for prills), and generate zero airborne micro-dust emissions.

### 2. Controlled-Release Fertilizers (CRFs) & Nitrification Inhibitors
Standard urea application suffers massive losses: up to $40 - 60\%$ of applied nitrogen is lost to the atmosphere as ammonia gas ($\text{NH}_3$ volatilization) or converted by soil nitrifying bacteria into nitrate ($\text{NO}_3^-$) that leaches into groundwater, alongside nitrous oxide ($\text{N}_2\text{O}$, a greenhouse gas with $298\times$ the global warming potential of $\text{CO}_2$):
- **Polymer-Coated Urea (PCU)**: Urea granules are encapsulated in an ultra-thin ($30 - 50\,\mu\text{m}$) membrane of biodegradable polyurethane or alkyd resin. Water slowly permeates through osmotic pores, dissolving urea, which diffuses out over $90 - 180\text{ days}$ matching crop uptake curves.
- **Urease & Nitrification Inhibitors**: Co-formulating urea with $N\text{-(n-butyl)thiophosphoric triamide}$ ($\text{NBPT}$, urease inhibitor) blocks the rapid enzymatic hydrolysis of urea to ammonium carbonate:
  $$\text{CO(NH}_2)_2 + 2\text{H}_2\text{O} \overset{\text{Urease}}{\longrightarrow} (\text{NH}_4)_2\text{CO}_3$$
  while 2-chloro-6-(trichloromethyl)pyridine (nitrapyrin) selectively suppresses *Nitrosomonas* bacteria, halting nitrate leaching.

### 3. Synergistic $\text{CO}_2$ Integration in Ammonia-Urea Complexes
A world-scale ammonia plant generates pure $\text{CO}_2$ from steam methane reforming:
$$\text{CH}_4 + 2\text{H}_2\text{O} \longrightarrow \text{CO}_2 + 4\text{H}_2$$
This $\text{CO}_2$ is scrubbed in an activated MDEA (methyldiethanolamine) absorption system and compressed directly to $150 - 200\text{ bar}$ to serve as the stoichiometric co-feed for urea synthesis:
$$2\text{NH}_3 + \text{CO}_2 \rightleftharpoons \text{NH}_2\text{COONH}_4 \rightleftharpoons \text{CO(NH}_2)_2 + \text{H}_2\text{O}$$
In a balanced modern complex, over **$85 - 90\%$** of all reformer process $\text{CO}_2$ is sequestered directly into solid urea fertilizer."""
        },

        "unit-3-sugar-and-starch": {
            "id": "sec-3-8",
            "secNumber": "3.8",
            "title": "Simulated Moving Bed (SMB) Chromatography, HFCS-55 & Starch Bioplastics",
            "content": r"""Starch processing extends beyond basic syrups into high-fructose corn syrups (HFCS) and renewable bioplastics that displace petroleum-derived polymers.

### 1. Simulated Moving Bed (SMB) Chromatographic Fructose Enrichment
Enzymatic glucose isomerase converts glucose into an equilibrium mixture containing at most $42\text{ wt}\%$ fructose (HFCS-42). To formulate beverage-grade HFCS-55 ($55\text{ wt}\%$ fructose, matching cane sucrose sweetness), the syrup must be chromatographically enriched:
- **Separation Principle**: Resins functionalized with calcium sulfonate ($\text{Ca}^{2+}$) form weak coordination complexes with fructose oxygen atoms (fructose contains a flexible furanose ring that coordinates strongly with divalent calcium), while glucose passes through unretarded.
- **Simulated Moving Bed Technology**: Continuous counter-current solid-liquid adsorption is achieved without physically moving the solid resin by cyclically shifting the fluid feed, eluent (pure water), extract (pure fructose), and raffinate (pure glucose) ports across $8 - 24$ interconnected packed columns:
  $$u_{\text{port}} = \frac{L_{\text{zone}}}{\Delta t_{\text{switch}}}$$
  The extracted stream yields $90\text{ wt}\%$ pure fructose, which is blended with HFCS-42 to formulate high-purity **HFCS-55**.

### 2. Starch Biopolymer Engineering: Polylactic Acid (PLA)
Starch is an industrial agricultural feedstock for biodegradable polyesters:
1. **Lactic Acid Fermentation**: Starch hydrolysate (pure glucose) is fermented anaerobically by *Lactobacillus delbrueckii* at $45 - 50^\circ\text{C}$ and $\text{pH } 5.5 - 6.5$:
   $$\text{C}_6\text{H}_{12}\text{O}_6 \longrightarrow 2\text{CH}_3\text{-CH(OH)-COOH} \quad (\Delta G^\circ < 0)$$
2. **Lactide Ring Formation**: Lactic acid is pre-polymerized into low-molecular-weight oligomers, then catalytically depolymerized at $200^\circ\text{C}$ under vacuum with tin(II) octoate catalyst to yield cyclic dimer **Lactide**:
   $$2\text{CH}_3\text{-CH(OH)-COOH} \longrightarrow \text{Lactide} + 2\text{H}_2\text{O}$$
3. **Ring-Opening Polymerization (ROP)**: Purified lactide undergoes coordinate-insertion ring-opening polymerization:
   $$n\,(\text{Lactide}) \overset{\text{Sn(Oct)}_2}{\longrightarrow} [-\text{CH(CH}_3)\text{-CO-O-}]_n \quad (\text{PLA}, \bar{M}_w > 100,000\text{ g/mol})$$
PLA exhibits tensile modulus comparable to polystyrene ($E \approx 3.5\text{ GPa}$) and degrades completely into water and $\text{CO}_2$ in industrial composting facilities."""
        },

        "unit-4-cement-and-lime": {
            "id": "sec-4-8",
            "secNumber": "4.8",
            "title": "Decarbonization of Cement: Low-Carbon LC3, Geopolymers & CCUS Integration",
            "content": r"""The cement sector accounts for approximately $7 - 8\%$ of global anthropogenic $\text{CO}_2$ emissions ($0.85\text{ kg CO}_2\text{ / kg OPC clinker}$). Decarbonization requires low-carbon clinker substitutes and carbon capture integration.

### 1. Limestone Calcined Clay Cement ($\text{LC}^3$) Technology
$\text{LC}^3$ replaces up to $50\%$ of ordinary Portland clinker with a ternary blend of calcined clay (metakaolin) and raw uncalcined limestone:
$$\text{LC}^3\text{ Formulation: } 50\%\text{ Clinker} + 30\%\text{ Calcined Clay} + 15\%\text{ Limestone} + 5\%\text{ Gypsum}$$
- **The Metakaolin-Limestone Synergistic Reaction**:
  Calcined kaolinitic clay (dehydroxylated at only $700 - 800^\circ\text{C}$, consuming $< 40\%$ of clinker calcination energy) releases amorphous reactive alumina and silica.
  In the presence of limestone ($\text{CaCO}_3$), reactive alumina reacts with carbonate ions to form monocarboaluminate (AFm phase):
  $$\text{Al}_2\text{O}_3 + \text{CaCO}_3 + 3\text{Ca(OH)}_2 + 11\text{H}_2\text{O} \longrightarrow \text{Ca}_4\text{Al}_2(\text{CO}_3)(\text{OH})_{12}\cdot 5\text{H}_2\text{O}$$
  Monocarboaluminate crystals prevent the decomposition of ettringite, packing interstitial capillary pores and delivering compressive strength equivalent to or exceeding pure OPC at 28 days while slashing embodied carbon by **$40\%$**.

### 2. Alkali-Activated Materials & Geopolymer Binders
Completely clinker-free binders synthesized by activating aluminosilicate industrial wastes (blast furnace slag, coal fly ash Class F) with concentrated aqueous sodium silicate or sodium hydroxide:
$$\text{Aluminosilicate Powder} + \text{Na}^+\text{OH}^- / \text{SiO}_2(aq) \longrightarrow [-\text{Si-O-Al-O-Si-O-}]_n \quad (\text{Sialate Network})$$
Geopolymers cure at ambient or mild temperatures ($40 - 60^\circ\text{C}$), exhibit fire resistance up to $1000^\circ\text{C}$, and reduce $\text{CO}_2$ emissions by up to **$80\%$**.

### 3. Oxy-Fuel Clinker Combustion & Carbon Capture
Because $60\%$ of cement $\text{CO}_2$ originates from limestone calcination ($\text{CaCO}_3 \to \text{CaO} + \text{CO}_2$) rather than fuel combustion, switching fuels cannot eliminate emissions.
In **Oxy-Fuel Clinker Burning**:
- Combustion is executed in pure oxygen diluted with recycled flue gas ($\text{O}_2 / \text{CO}_2$ mixture).
- Flue gas leaving the preheater contains $> 80 - 90\text{ vol}\%\text{ CO}_2$ (dry basis).
- After moisture condensation, high-purity $\text{CO}_2$ is directly compressed and liquified for permanent deep geological sequestration or synthetic e-fuel synthesis."""
        },

        "unit-5-soaps-and-detergents": {
            "id": "sec-5-8",
            "secNumber": "5.8",
            "title": "Green Surfactants, Oleochemical Biorefineries & Enzyme Detergent Formulations",
            "content": r"""The modern detergents industry is shifting toward $100\%$ bio-based renewable carbon surfactants and cold-water multi-enzyme systems:

### 1. Renewable Green Surfactants
1. **Alkyl Polyglycosides (APGs)**:
   Non-ionic surfactants synthesized via the direct Fisher glycosidation of plant fatty alcohols ($\text{C}_8 - \text{C}_{14}$, derived from palm or coconut oil) with renewable glucose (from starch):
   $$\text{C}_{12}\text{H}_{25}\text{OH} + n\,\text{C}_6\text{H}_{12}\text{O}_6 \overset{\text{Acid Cat.}}{\longrightarrow} \text{C}_{12}\text{H}_{25}\text{O-(C}_6\text{H}_{10}\text{O}_5)_n\text{-H} + n\,\text{H}_2\text{O}$$
   APGs exhibit zero aquatic toxicity, instantaneous complete biodegradability, and synergistically boost foam stability when blended with anionic surfactants.
2. **Biosurfactants (Microbial Rhamnolipids & Sophorolipids)**:
   Glycolipid biosurfactants fermented by *Pseudomonas aeruginosa* or *Starmerella bombicola* from vegetable oil waste. They exhibit ultra-low Critical Micelle Concentrations ($\text{CMC} < 20 - 50\text{ mg/L}$) and are $100\%$ bio-derived.

### 2. Multi-Enzyme Detergency Engineering
Modern laundry detergents operate at ambient water temperatures ($20 - 30^\circ\text{C}$), replacing high thermal energy with enzymatic biocatalysis:
- **Proteases (Subtilisin)**: Hydrolyze insoluble peptide bonds in protein stains (blood, egg, grass) into soluble oligopeptides:
  $$\text{R-CO-NH-R}^\prime + \text{H}_2\text{O} \overset{\text{Protease}}{\longrightarrow} \text{R-COOH} + \text{R}^\prime\text{-NH}_2$$
- **Amylases ($\alpha$-Amylase)**: Rapidly cleave $\alpha\text{-(1}\to\text{4)}$ glucosidic bonds in gelatinized food starch (gravy, sauces).
- **Lipases**: Hydrolyze hydrophobic triglyceride grease spots into water-soluble glycerol and mono/diglycerides.
- **Cellulases (Endo-glucanases)**: Selectively shave off damaged, micro-fibrillated cotton pills from fabric surfaces, restoring original color brilliance and fiber softness without chemical fabric softeners."""
        },

        "unit-6-pulp-and-paper": {
            "id": "sec-6-8",
            "secNumber": "6.8",
            "title": "Nanocellulose Engineering, Lignin Valorization & Black Liquor Gasification",
            "content": r"""The contemporary pulp mill has transformed into an integrated forest biorefinery, producing advanced biomaterials and green biofuels alongside traditional paper grades:

### 1. Nanocellulose Engineering (CNF & CNC)
High-purity chemical wood pulps can be dismantled into nanoscale crystalline building blocks:
- **Cellulose Nanofibrils (CNF)**: Produced by enzymatic or chemical pretreatment (TEMPO-mediated oxidation: selective conversion of $\text{C}_6$ primary hydroxyls to carboxylates, $-\text{CH}_2\text{OH} \to -\text{COO}^-$) followed by high-pressure homogenization ($1,000 - 1,500\text{ bar}$). Generates flexible, high-aspect-ratio nanofibrils ($5 - 20\text{ nm}$ diameter, several microns length) forming transparent, highly oxygen-impermeable barrier films.
- **Cellulose Nanocrystals (CNC)**: Concentrated sulfuric acid hydrolysis ($64\text{ wt}\%\text{ H}_2\text{SO}_4$, $45^\circ\text{C}$) selectively digests amorphous cellulose domains, leaving pristine, defect-free crystalline nanorods ($d \approx 5\text{ nm}$, $L \approx 150 - 250\text{ nm}$). CNCs exhibit an axial Young's modulus exceeding **$140 - 150\text{ GPa}$** (comparable to Kevlar and exceeding structural steel on a specific density basis).

### 2. Technical Lignin Valorization
Rather than burning all black liquor lignin for low-grade steam, modern processes (e.g., LignoBoost) precipitate high-purity Kraft lignin:
- Weak or semi-concentrated black liquor is acidified with $\text{CO}_2$ gas to $\text{pH } 9.5 - 10.0$, deprotonating phenolate groups and precipitating solid colloidal lignin.
- The recovered lignin is washed with dilute sulfuric acid and dewatered into dry brown powder ($> 98\%$ purity).
- **High-Value Applications**:
  - Precursors for polyacrylonitrile-free bio-based carbon fibers.
  - Phenol replacement in phenol-formaldehyde wood adhesives.
  - Catalytic depolymerization into bio-vanillin and aromatic BTX chemical commodities.

### 3. Black Liquor Gasification (Chemrec Process)
Pressurized entrained-flow gasification ($950 - 1000^\circ\text{C}$, $30\text{ bar}$) converts concentrated black liquor with pure oxygen into high-quality synthesis gas ($\text{CO} + \text{H}_2$) and molten inorganic smelt. Gasification efficiency exceeds traditional Tomlinson boilers, enabling synthesis of renewable **Bio-DME** and synthetic green biomethanol."""
        },

        "unit-7-glass-and-ceramics": {
            "id": "sec-7-8",
            "secNumber": "7.8",
            "title": "Functional Glass-Ceramics, Phase Separation & Zero-Expansion Cooktops",
            "content": r"""Glass-ceramics are polycrystalline materials produced by controlled, uniform internal crystallization of a precursor glass article, combining the processing ease of glass with the thermal and mechanical properties of crystalline ceramics:

### 1. Controlled Crystallization Thermochemistry
The transformation of an amorphous glass into a fine-grained glass-ceramic requires two distinct heat-treatment stages:
1. **Internal Nucleation ($T_{\text{nuc}} \approx T_g + 50^\circ\text{C}$)**:
   Homogeneous nucleation is impractically slow in viscous silicate melts. Heterogeneous nucleation agents ($\text{TiO}_2, \text{ZrO}_2, \text{P}_2\text{O}_5$, $2 - 5\text{ mol}\%$) are incorporated into the melt:
   - At $T_{\text{nuc}}$, titanate/zirconate sub-nanometer clusters precipitate at densities exceeding $10^{12} - 10^{15}\text{ nuclei/cm}^3$.
2. **Crystal Growth ($T_{\text{cryst}} > T_{\text{nuc}}$)**:
   The article is heated to the maximum growth rate temperature where primary crystal phases crystallize uniformly from the nucleated sites, transforming the material into $70 - 95\%$ crystalline grains ($< 1\,\mu\text{m}$) embedded in a thin residual glassy matrix.

### 2. Lithium Aluminosilicate (LAS) Zero-Expansion Glass-Ceramics
Used in induction cooktops, telescope mirror blanks, and missile radomes:
- Composition: $\text{Li}_2\text{O}-\text{Al}_2\text{O}_3-\text{SiO}_2$ with $\text{TiO}_2/\text{ZrO}_2$ nucleating catalysts.
- Primary Crystalline Phase: High-quartz solid solution ($\beta\text{-quartz ss}$) or $\beta\text{-spodumene}$.
- **Negative Thermal Expansion Mechanism**: The crystal lattice of $\beta$-quartz exhibits anisotropic thermal vibration where certain crystallographic axes contract as temperature increases. Balancing the negative expansion of the crystals against the positive expansion of the residual glass yields a net **Zero Coefficient of Thermal Expansion**:
  $$\alpha \approx (-0.5 \text{ to } +0.5) \times 10^{-7}\text{ K}^{-1} \quad (20 - 700^\circ\text{C})$$
An LAS cooktop plate can be heated to $800^\circ\text{C}$ and plunged directly into ice water without cracking or experiencing measurable dimensional distortion."""
        },

        "unit-8-caustic-chlorine": {
            "id": "sec-8-8",
            "secNumber": "8.8",
            "title": "Oxygen-Depolarized Cathodes (ODC), Green Hydrogen & Zero-Emission Chlor-Alkali",
            "content": r"""The chlor-alkali sector consumes massive electrical energy ($> 2,200\text{ kWh/metric ton NaOH}$). The development of Oxygen-Depolarized Cathode (ODC) technology and hydrogen valorization represents a paradigm shift toward decarbonized heavy chemicals:

### 1. Oxygen-Depolarized Cathode (ODC) Electrochemistry
In conventional membrane cells, hydrogen gas is evolved at the cathode by water reduction:
$$2\text{H}_2\text{O} + 2e^- \longrightarrow \text{H}_2(g) + 2\text{OH}^- \quad (E^\circ = -0.828\text{ V})$$
In an ODC cell, gaseous pure oxygen ($\text{O}_2$) is introduced through a porous gas-diffusion cathode coated with silver or platinum catalysts, depolarizing the cathode reaction into oxygen reduction:
$$\text{O}_2(g) + 2\text{H}_2\text{O} + 4e^- \longrightarrow 4\text{OH}^- \quad (E^\circ = +0.401\text{ V})$$
- **Thermodynamic Voltage Reduction**:
  The cathode standard potential shifts positively by $\Delta E^\circ = 0.401 - (-0.828) = +1.229\text{ V}$.
- **Cell Operating Voltage Drop**:
  Operational cell voltage plummets from $\sim 3.00\text{ V}$ to **$2.00 - 2.10\text{ V}$** at $4 - 5\text{ kA/m}^2$.
- **Energy Conservation**:
  Electrical energy consumption drops from $2,200\text{ kWh/t NaOH}$ to **$1,500 - 1,600\text{ kWh/t NaOH}$**, achieving an extraordinary **$30\%$ reduction in grid power consumption**.

### 2. High-Purity Green Hydrogen Valorization
For conventional membrane plants that continue to produce byproduct hydrogen:
- Chlor-alkali hydrogen is ultra-pure ($> 99.999\%$ after moisture condensation and trace oxygen catalytic deoxidation).
- Rather than combusting hydrogen for low-grade process steam, modern complexes feed this chemical-grade hydrogen into fuel-cell vehicles, direct ammonia synthesis, or green methanol plants, capturing immense clean-energy carbon credits."""
        },

        "unit-9-petroleum-and-fuels": {
            "id": "sec-9-8",
            "secNumber": "9.8",
            "title": "Sustainable Aviation Fuel (SAF), Biofuels & Circular Plastics Pyrolysis",
            "content": r"""Petroleum refineries are evolving into multi-feedstock processing hubs co-processing renewable fats, waste biomass, and post-consumer plastics:

### 1. Sustainable Aviation Fuel (SAF) via HEFA Processing
The dominant commercial pathway for aviation decarbonization is **Hydroprocessed Esters and Fatty Acids (HEFA)**:
- Feedstocks: Used cooking oil (UCO), tallow, and carinata seed oil.
- **Process Chemistry**:
  1. *Hydrodeoxygenation (HDO)*: High-pressure hydrotreating over $\text{Ni-Mo}/\text{Al}_2\text{O}_3$ at $350^\circ\text{C}$ ($60 - 80\text{ bar}$) eliminates oxygen from triglycerides as water, propane, and $\text{CO}_2$, yielding linear paraffinic waxes ($\text{C}_{16} - \text{C}_{18}$ alkanes).
  2. *Hydroisomerization & Selective Hydrocracking*: Paraffins pass over bifunctional noble metal / zeolite catalysts (e.g., $\text{Pt}/\text{SAPO-11}$) to selectively crack and branch straight chains into isoparaffins boiling in the jet fuel range ($\text{C}_9 - \text{C}_{15}$).
  3. *Freezing Point Adjustment*: Isomerization depresses the freezing point below $-47^\circ\text{C}$ (meeting ASTM D7566 Jet A-1 standards), reducing lifecycle aviation carbon emissions by up to **$80\%$**.

### 2. Circular Chemical Recycling: Waste Plastics Pyrolysis
Mechanical recycling cannot process heavily contaminated or multi-layer packaging films.
In **Thermolytic Chemical Pyrolysis**:
- Sorted waste polyolefins (polyethylene, polypropylene) are heated in an inert atmosphere ($450 - 550^\circ\text{C}$) in a fluidized bed or rotary kiln.
- Thermal homolytic scission cleaves synthetic carbon-carbon backbones into a synthetic liquid crude oil ("pyrolysis oil").
- After mild hydrotreating to remove chlorine (from trace PVC) and nitrogen contaminants, the pyrolysis oil is fed directly into refinery FCC risers or steam crackers, yielding virgin-quality circular polymer resins."""
        },

        "unit-10-metallurgy-and-steel": {
            "id": "sec-10-8",
            "secNumber": "10.8",
            "title": "The Green Steel Transition: 100% Hydrogen Shaft DRI & Near-Zero Carbon Steelmaking",
            "content": r"""Ferrous extractive metallurgy is responsible for approximately $7 - 9\%$ of total global $\text{CO}_2$ emissions ($1.85\text{ metric tons CO}_2\text{ / metric ton crude steel}$ via the traditional BF-BOF route). The transition to near-zero carbon steelmaking centers on green hydrogen reduction:

### 1. 100% Pure Hydrogen Direct Reduction (H2-DRI)
Replacing fossil carbon monoxide with renewable electrolytic hydrogen:
$$\text{Fe}_2\text{O}_3(s) + 3\text{H}_2(g) \longrightarrow 2\text{Fe}(s) + 3\text{H}_2\text{O}(g) \quad \Delta H_{298}^\circ = +98.8\text{ kJ/mol}$$
- **Thermodynamic Contrasts with Carbon Monoxide Reduction**:
  - Reduction by $\text{H}_2$ is endothermic ($\Delta H > 0$), whereas reduction by $\text{CO}$ is exothermic ($\Delta H < 0$). Heat must be continuously supplied by electric preheating of the circulating hydrogen gas loop.
  - Molecular hydrogen ($\text{H}_2$) possesses a tiny molecular radius and a gas diffusivity in porous ore pellets approximately $4\times$ faster than $\text{CO}$, accelerating reduction kinetics and permitting smaller reactor shaft volumes.
  - Discharges purely non-polluting water vapor ($\text{H}_2\text{O}$) rather than greenhouse carbon dioxide ($\text{CO}_2$).

### 2. Hybrid Electric Arc Furnace (EAF) Melting & Slag Foaming
The resulting carbon-free Direct Reduced Iron ($\text{H}_2\text{-DRI}$) is transferred hot ($650^\circ\text{C}$) to an Electric Arc Furnace:
- **Carbon Injection for Slag Foaming**: In an EAF, a foamy slag is essential to shield water-cooled furnace walls from radiant arc heat and maximize arc thermal efficiency. Since $\text{H}_2\text{-DRI}$ contains $0\%\text{ C}$, a controlled charge of biogenic carbon (biochar) is injected through lances to generate foamy $\text{CO}$ bubbles ($[\text{C}] + (\text{FeO}) \to \text{Fe} + \text{CO} \uparrow$).
- **Lifecycle Decarbonization**: Pairing renewable solar/wind power with PEM water electrolyzers and $\text{H}_2\text{-DRI-EAF}$ slashes steel lifecycle carbon emissions to **$< 0.05\text{ t CO}_2\text{ / t steel}$** ($> 97\%$ reduction)."""
        }
    }

    # Inject into each unit
    for u in units:
        uid = u["id"]
        if uid in sec8_dict:
            # Check if sec-8 already present
            has_sec8 = any(s["id"] == sec8_dict[uid]["id"] for s in u["sections"])
            if not has_sec8:
                u["sections"].append(sec8_dict[uid])

    return units
