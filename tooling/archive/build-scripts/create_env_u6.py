# -*- coding: utf-8 -*-
"""
Environmental Chemistry - Unit 6 Content Generator
Unit 6: Environmental Toxicants: Pesticides, Organohalogens & Bioaccumulation
Strictly no marks, no course codes, pure Unix line endings.
"""

import json

def get_unit_6():
    unit = {
        "id": "unit_6",
        "title": "Environmental Toxicants: Pesticides, Organohalogens & Bioaccumulation",
        "badge": "Unit 06",
        "summary": "Chemical classification, neurotoxic modes of action, and degradation kinetics of agrochemicals; persistence, lipophilicity, and global transport of POPs; dioxins, furans, PCBs, and TEQ calculations; multimedia fugacity modeling (Mackay Levels I to IV); quantitative bioconcentration, bioaccumulation, and trophic biomagnification dynamics.",
        "simulation": {
            "id": "sim_env_pesticide_bioaccumulation_foodweb",
            "title": "Aquatic Food Web Bioaccumulation & Trophic Magnification Simulator",
            "type": "canvas",
            "description": "Multi-compartment 4-trophic level ecotoxicological simulator modeling chemical uptake, octanol-water partitioning (log Kow), somatic growth dilution, depuration kinetics, and trophic magnification factors (TMF)."
        },
        "sections": [
            {
                "id": "sec_6_1",
                "title": "Classification, Chemical Architecture & Physicochemical Properties of Pesticides",
                "content": """Pesticides encompass a chemically heterogeneous array of synthetic and naturally derived organic compounds formulated to suppress, repel, or eradicate target pest populations. Understanding their environmental fate demands analyzing their fundamental molecular architectures and thermodynamic partition coefficients.

### Structural Taxonomies of Major Pesticide Classes
1. **Organochlorines (OCs)**:
   - Polychlorinated hydrocarbons characterized by high chemical stability, minimal aqueous solubility ($S_w < 1\\ \\text{mg}/\\text{L}$), extreme octanol-water partition coefficients ($\\log K_{ow} > 5.0$), and prolonged environmental persistence (half-lives measured in years to decades).
   - *Archetypes*: Dichlorodiphenyltrichloroethane (DDT), hexachlorocyclohexane (lindane, $\\gamma\\text{-HCH}$), cyclodienes (aldrin, dieldrin, endrin, chlordane, heptachlor).
2. **Organophosphates (OPs)**:
   - Synthetic esters, amides, or thiol derivatives of phosphoric ($H_3PO_4$), phosphonic, or phosphorothioic ($H_3PO_3S$) acids.
   - Characterized by moderate water solubility, lower lipophilicity ($\\log K_{ow} \\approx 2 - 4$), rapid susceptibility to abiotic and microbial alkaline hydrolysis, but acute neurotoxicity.
   - *Archetypes*: Parathion, malathion, chlorpyrifos, diazinon.
3. **Carbamates**:
   - Synthetic esters of carbamic acid ($H_2NCOOH$) substituted with $N$-methyl or $N$-aryl moieties (e.g., carbaryl, carbofuran, aldicarb).
   - Display moderate aqueous solubility and reversible neurotoxic enzyme binding.
4. **Synthetic Pyrethroids**:
   - Synthetic structural analogues of natural pyrethrins extracted from *Chrysanthemum cinerariifolium* blossoms, featuring cyclopropanecarboxylate esters.
   - High lipophilicity ($\\log K_{ow} \\approx 5 - 7$), exceptional insecticidal potency, rapid aquatic toxicity to fish, but rapid soil photolysis.
   - *Archetypes*: Permethrin, cypermethrin, deltamethrin.
5. **Neonicotinoids**:
   - Systemic nitroguanidine or cyanoamidine neurotoxins possessing high water solubility and environmental mobility, acting selectively as agonists at insect nicotinic acetylcholine receptors (nAChR).
   - *Archetypes*: Imidacloprid, clothianidin, thiamethoxam."""
            },
            {
                "id": "sec_6_2",
                "title": "Organochlorines: Persistence, Lipophilicity & Environmental Transport",
                "content": """Organochlorine pesticides represent the classic persistent pollutants that catalyzed the modern environmental science and regulatory movement.

### Chemical Structure and Stereochemistry of DDT
Dichlorodiphenyltrichloroethane (specifically $1,1,1\\text{-trichloro-}2,2\\text{-bis}(p\\text{-chlorophenyl})\\text{ethane}$, or $p,p'\\text{-DDT}$) features a central ethanic core bonded to two chlorophenyl rings and a trichloromethyl group. Its high molar mass ($354.49\\ \\text{g}/\\text{mol}$), lack of hydrogen-bonding donors, and low polarizability yield an exceptionally low aqueous solubility ($S_w = 0.0055\\ \\text{mg}/\\text{L}$ at $25^\\circ\\text{C}$) and a high lipophilicity ($\\log K_{ow} = 6.91$).

### Environmental Transformation Pathways
In natural soils and aquatic sediments, DDT undergoes two major microbially mediated metabolic branchings:
1. **Reductive Dechlorination (Anaerobic)**:
   - In flooded, anoxic soils, anaerobic consortia substitute a chlorine atom on the aliphatic ethanic carbon with hydrogen, yielding DDD ($1,1\\text{-dichloro-}2,2\\text{-bis}(p\\text{-chlorophenyl})\\text{ethane}$):
   \\[
   p,p'\\text{-DDT} + 2e^- + \\text{H}^+ \\rightarrow p,p'\\text{-DDD} + \\text{Cl}^-
   \\]
2. **Dehydrochlorination (Aerobic & Abiotic)**:
   - Under aerobic conditions or basic abiotic catalysis, elimination of hydrogen chloride ($HCl$) yields the chemically hyper-stable metabolite DDE ($1,1\\text{-dichloro-}2,2\\text{-bis}(p\\text{-chlorophenyl})\\text{ethylene}$):
   \\[
   p,p'\\text{-DDT} \\xrightarrow{-HCl} p,p'\\text{-DDE}
   \\]
   - DDE's planar olefinic backbone resists further enzymatic cleavage, persisting in tissues and sediment for centuries."""
            },
            {
                "id": "sec_6_3",
                "title": "Organophosphates & Carbamates: Neurotoxicity & Hydrolysis Kinetics",
                "content": """Both organophosphates and carbamates exert their acute insecticidal and vertebrate toxicity through the disruption of central and peripheral synaptic neurotransmission.

### Molecular Mode of Action: Acetylcholinesterase (AChE) Inhibition
Acetylcholinesterase ($EC\\ 3.1.1.7$) is a serine hydrolase that terminates synaptic signaling by cleaving the neurotransmitter acetylcholine ($ACh$) into acetate and choline at rates exceeding $25,000\\ \\text{molecules}/\\text{second}$:
1. **Catalytic Triad Structure**: The active site features a catalytic triad consisting of Serine-203, Histidine-440, and Glutamate-327 (numbering in human AChE).
2. **Phosphorylation**: The nucleophilic hydroxyl group of Ser-203 attacks the electrophilic phosphorus atom of the organophosphate (e.g. oxon forms such as paraoxon or chlorpyrifos-oxon), forming a stable covalent phosphoester bond and ejecting the leaving group ($LG$):
   \\[
   \\text{E--OH} + \\text{(RO)}_2\\text{P(O)LG} \\xrightarrow{k_1/k_{-1}} [\\text{E--OH} \\cdots \\text{Inh}] \\xrightarrow{k_2} \\text{E--O--P(O)(OR)}_2 + \\text{LG}
   \\]
3. **Aging Phenomenon**: Over time, spontaneous dealkylation of one alkoxy ($-OR$) group occurs, generating an anionic phosphodiester adduct ($\\text{E--O--P(O)(O}^-\\text{)(OR)}$). Electrostatic repulsion prevents nucleophilic reactivation by oxime antidotes (e.g., pralidoxime / 2-PAM), rendering the enzyme permanently inactivated.

### Environmental Degradation: Abiotic Hydrolysis Kinetics
In aquatic environments, organophosphates degrade via pseudo-first-order alkaline hydrolysis:
\\[
-\\frac{d[OP]}{dt} = k_{obs}[OP], \\quad k_{obs} = k_N + k_A[H^+] + k_B[OH^-]
\\]
In natural waters (pH $7 - 9$), the base-catalyzed term dominates ($k_{obs} \\approx k_B[OH^-]$). As a result, increasing the water pH by 1 unit increases the degradation rate constant by a factor of 10, dramatically shortening the half-life ($t_{1/2} = \\frac{\\ln 2}{k_{obs}}$)."""
            },
            {
                "id": "sec_6_4",
                "title": "Synthetic Pyrethroids, Neonicotinoids & Emerging Agro-contaminants",
                "content": """Modern agricultural pesticide formulations emphasize high target-species selectivity and reduced mammalian toxicity, but introduce novel environmental vulnerabilities.

### Synthetic Pyrethroids: Axonal Sodium Channel Modulators
Pyrethroids prolong the open state of voltage-gated sodium channels ($VGSC$) in neuronal membranes, causing repetitive axonal discharges, depolarization block, and paralysis:
- **Type I (e.g., Permethrin)**: Lack an $\\alpha\\text{-cyano}$ moiety; induce tremors (T-syndrome).
- **Type II (e.g., Deltamethrin, Cypermethrin)**: Contain an $\\alpha\\text{-cyano-}3\\text{-phenoxybenzyl}$ ester; induce choreoathetosis and salivation (CS-syndrome).
- *Aquatic Ecotoxicity*: Pyrethroids exhibit extreme acute toxicity to teleost fish and aquatic macroinvertebrates ($LC_{50} < 1\\ \\mu\\text{g}/\\text{L}$), as aquatic species lack efficient carboxylesterase and CYP450 detoxification pathways.

### Neonicotinoids: Systemic Agronomic Vectors
Neonicotinoids are systemic pesticides absorbed by plant roots and translocated acropetally through xylem tissue to foliage, nectar, and pollen:
- **Agonism at nAChR**: Bind irreversibly to post-synaptic nicotinic acetylcholine receptors in insects, causing continuous neuronal excitation.
- **Environmental Concerns**: High water solubility ($S_w \\approx 0.6\\ \\text{g}/\\text{L}$ for imidacloprid) promotes widespread leaching into surface streams and groundwater. Sub-lethal ppb-level concentrations impair foraging navigation, memory, and immune defenses in honeybees (*Apis mellifera*) and solitary pollinators."""
            },
            {
                "id": "sec_6_5",
                "title": "Persistent Organic Pollutants (POPs) & The Stockholm Convention",
                "content": """The **Stockholm Convention on Persistent Organic Pollutants (2001)** represents a legally binding multilateral environmental agreement to eliminate or severely restrict chemicals meeting four criteria under Annex D:
1. **Chemical Persistence**: Half-life $> 2\\ \\text{months}$ in water, or $> 6\\ \\text{months}$ in soil/sediment.
2. **Bioaccumulation**: Bioconcentration factor ($\\text{BCF}$) $> 5000\\ \\text{L}/\\text{kg}$ or $\\log K_{ow} > 5.0$.
3. **Potential for Long-Range Environmental Transport (LRET)**: Evidence of atmospheric transport over transboundary distances.
4. **Adverse Toxicological Effects**: Documented toxicity to human health or wildlife.

### The Original 'Dirty Dozen'
- *Organochlorine Pesticides (8)*: Aldrin, Chlordane, DDT, Dieldrin, Endrin, Heptachlor, Mirex, Toxaphene.
- *Industrial Chemicals (2)*: Polychlorinated Biphenyls (PCBs), Hexachlorobenzene (HCB).
- *Unintentional By-products (2)*: Polychlorinated dibenzo-p-dioxins (PCDDs), Polychlorinated dibenzofurans (PCDFs).

### Global Fractionation & The Grasshopper Effect
Volatile and semi-volatile POPs emitted in tropical and temperate regions evaporate into the atmosphere. Prevailing atmospheric circulation transports them poleward. As air masses cool, chemicals condense and deposit onto sub-polar and arctic soils and ice packs:
\\[
\\text{Vapor Phase} \\xrightarrow{\\text{Equatorial Heat}} \\text{Atmospheric Advection} \\xrightarrow{\\text{Polar Cooling}} \\text{Cold Condensation}
\\]
Compounds with higher vapor pressures undergo multiple cycles of evaporation, transport, and deposition (the *grasshopper effect*), concentrating selectively in Arctic ecosystems and indigenous food webs."""
            },
            {
                "id": "sec_6_6",
                "title": "PCBs, Dioxins (PCDDs) & Furans (PCDFs): Congener Chemistry & TEQ",
                "content": """Polychlorinated biphenyls, dioxins, and furans are ubiquitous halogenated aromatic contaminants exhibiting severe chronic toxicity.

### Chemical Architectures
1. **Polychlorinated Biphenyls (PCBs)**:
   - Formed by chlorinated biphenyl rings: $C_{12}H_{10-n}Cl_n$ ($n = 1$ to $10$), yielding exactly 209 individual structural congeners.
   - *Coplanar (Dioxin-like) PCBs*: Congeners lacking chlorine substitutions at the ortho-positions ($2, 2', 6, 6'$) can rotate into a flat, coplanar conformation (e.g., PCB 77, 126, 169), fitting precisely into cellular aryl hydrocarbon receptors.
2. **PCDDs and PCDFs**:
   - Dibenzo-p-dioxins consist of two benzene rings linked by two ether oxygen bridges. Dibenzofurans contain two benzene rings joined by a single oxygen atom and a direct carbon-carbon bond.
   - The most toxic congener is $2,3,7,8\\text{-tetrachlorodibenzo-}p\\text{-dioxin}$ ($2,3,7,8\\text{-TCDD}$).

### Mechanism of Toxicity: Aryl Hydrocarbon Receptor (AhR) Activation
Lipophilic planar planar molecules pass through the plasma membrane and bind to the cytosolic **Aryl Hydrocarbon Receptor (AhR)**. The ligand-bound AhR dissociates from heat shock proteins, translocates into the nucleus, and heterodimerizes with the Aryl Hydrocarbon Receptor Nuclear Translocator (ARNT). The AhR-ARNT complex binds Xenobiotic Response Elements (XRE) in DNA, hyper-inducing CYP1A1 transcription and triggering oxidative stress, teratogenesis, and chloracne.

### Toxic Equivalency Factor (TEF) and TEQ Methodology
To evaluate the collective risk of complex environmental mixtures, the World Health Organization (WHO) assigns Toxic Equivalency Factors relative to $2,3,7,8\\text{-TCDD}$ (assigned $\\text{TEF} = 1.0$):
\\[
\\text{TEQ} = \\sum_{i=1}^{N} \\left( C_i \\times \\text{TEF}_i \\right)
\\]
where $C_i$ is the concentration of the $i$-th congener and $\\text{TEF}_i$ is its toxic weight."""
            },
            {
                "id": "sec_6_7",
                "title": "Fugacity Modeling of Multimedia Toxicant Partitioning (Mackay Levels I to IV)",
                "content": """Multimedia environmental modeling quantifies how organic chemicals distribute among air, water, soil, and aquatic sediment compartments. Donald Mackay formulated fugacity ($f$, in units of Pascals, Pa) as an equilibrium surrogate for chemical potential.

### Fundamental Fugacity Formulation
For any environmental phase $i$:
\\[
C_i = Z_i \\cdot f_i
\\]
where:
- $C_i$ is the chemical concentration in phase $i$ ($\\text{mol}/\\text{m}^3$).
- $Z_i$ is the fugacity capacity of phase $i$ ($\\text{mol}/(\\text{m}^3\\cdot\\text{Pa})$).
- $f_i$ is the fugacity in phase $i$ ($\\text{Pa}$).

### Fugacity Capacities ($Z$-values) for Environmental Phases
1. **Air Phase ($i = a$)**:
   \\[
   Z_a = \\frac{1}{RT}
   \\]
2. **Water Phase ($i = w$)**:
   \\[
   Z_w = \\frac{1}{H} = \\frac{C_w^{sat}}{P^{sat}}
   \\]
   where $H$ is the Henry's law constant ($\\text{Pa}\\cdot\\text{m}^3/\\text{mol}$).
3. **Soil / Sediment Phases ($i = s$)**:
   \\[
   Z_s = \\frac{\\rho_s K_d}{H} = \\frac{\\rho_s f_{oc} K_{oc}}{H}
   \\]
   where $\\rho_s$ is bulk density, $f_{oc}$ is organic carbon fraction, and $K_{oc}$ is the organic carbon partition coefficient.

### Hierarchy of Mackay Models
- **Level I**: Evaluates equilibrium, closed system, no degradation, no advection ($f_a = f_w = f_s = f_{eq}$):
  \\[
  f_{eq} = \\frac{M_{tot}}{\\sum_i (V_i Z_i)}
  \\]
- **Level II**: Equilibrium, open system with continuous emissions, advective inflow/outflow, and first-order reaction sinks.
- **Level III**: Steady-state, non-equilibrium with inter-media transport resistances ($f_a \\neq f_w \\neq f_s$).
- **Level IV**: Unsteady, dynamic non-equilibrium system solving coupled differential equations over time."""
            },
            {
                "id": "sec_6_8",
                "title": "Quantitative Bioaccumulation, Biomagnification & Trophic Transfer",
                "content": """Contaminant accumulation in living organisms follows quantitative thermodynamic and kinetic rate processes.

### Definitions of Accumulation Metrics
1. **Bioconcentration Factor (BCF)**:
   - Ratio of chemical concentration in aquatic biota tissue ($C_{biota}$) to that in ambient water ($C_w$) resulting exclusively from respiratory (gill/dermal) absorption in laboratory settings:
     \\[
     \\text{BCF} = \\frac{C_{biota}}{C_w} = \\frac{k_1}{k_2} \\quad (\\text{L}/\\text{kg})
     \\]
     where $k_1$ is the uptake rate constant and $k_2$ is the depuration rate constant.
2. **Bioaccumulation Factor (BAF)**:
   - Field ratio of organism concentration to ambient water concentration including all uptake routes (gills, skin, and dietary food ingestion):
     \\[
     \\text{BAF} = \\frac{C_{biota}}{C_w} \\quad (\\text{L}/\\text{kg})
     \\]
3. **Biomagnification Factor (BMF)**:
   - Ratio of lipid-normalized chemical concentration in a predator organism to that in its dietary prey:
     \\[
     \\text{BMF} = \\frac{C_{predator, lipid}}{C_{prey, lipid}}
     \\]
     If $\\text{BMF} > 1$, biomagnification occurs across the trophic link.

### Trophic Magnification Factor (TMF)
Across an entire ecological food web, trophic position ($TP$) is quantified using stable nitrogen isotope ratios ($\delta^{15}\\text{N}$):
\\[
TP = 2 + \\frac{\\delta^{15}\\text{N}_{organism} - \\delta^{15}\\text{N}_{baseline}}{\\Delta^{15}\\text{N}}
\\]
where $\\Delta^{15}\\text{N} \\approx 3.4\\‰$ per trophic level.
Plotting $\\ln(C_{lipid})$ against trophic position yields the linear regression:
\\[
\\ln(C_{lipid}) = a + b \\cdot TP
\\]
The **Trophic Magnification Factor (TMF)** is:
\\[
\\text{TMF} = \\exp(b)
\\]
A value of $\\text{TMF} > 1$ proves statistically that the contaminant biomagnifies across the food web."""
            }
        ],
        "problems": [
            {
                "id": "prob_6_1",
                "tier": "Foundational",
                "title": "Octanol-Water Partition Coefficient and BCF Estimation via QSARs",
                "statement": "An emerging agrochemical herbicide exhibits an experimental octanol-water partition coefficient of $\\log K_{ow} = 4.85$. (a) Calculate the exact equilibrium ratio $K_{ow}$. (b) Using the classical Veith empirical quantitative structure-activity relationship (QSAR) for aquatic teleost fish, $\\log_{10}(\\text{BCF}) = 0.85\\log_{10}(K_{ow}) - 0.70$, calculate the predicted bioconcentration factor $\\text{BCF}$ in $\\text{L}/\\text{kg}$. (c) If the herbicide concentration in an agricultural drainage ditch is $4.5\\ \\mu\\text{g}/\\text{L}$, calculate the steady-state concentration in whole fish tissue in $\\text{mg}/\\text{kg}$ wet weight.",
                "hints": [
                    "Compute $K_{ow} = 10^{4.85}$.",
                    "Compute $\\log_{10}(\\text{BCF}) = 0.85(4.85) - 0.70$.",
                    "Tissue concentration $C_{fish} = \\text{BCF} \\times C_w$."
                ],
                "solution": """**Step 1: Calculate $K_{ow}$**
Given $\\log_{10} K_{ow} = 4.85$:
\\[
K_{ow} = 10^{4.85} = 70,794.6 \\approx 70,800
\\]

**Step 2: Calculate predicted BCF using the Veith QSAR**
\\[
\\log_{10}(\\text{BCF}) = 0.85 \\log_{10}(K_{ow}) - 0.70 = 0.85(4.85) - 0.70 = 4.1225 - 0.70 = 3.4225
\\]
Taking the antilogarithm:
\\[
\\text{BCF} = 10^{3.4225} = 2,645.5\\ \\text{L}/\\text{kg} \\approx 2,650\\ \\text{L}/\\text{kg}
\\]

**Step 3: Calculate steady-state concentration in fish tissue**
The aqueous concentration is:
\\[
C_w = 4.5\\ \\mu\\text{g}/\\text{L} = 0.0045\\ \\text{mg}/\\text{L}
\\]
The resulting concentration in fish tissue:
\\[
C_{fish} = \\text{BCF} \\times C_w = (2,645.5\\ \\text{L}/\\text{kg}) \\times (0.0045\\ \\text{mg}/\\text{L}) = 11.905\\ \\text{mg}/\\text{kg}
\\]

**Conclusion**:
The herbicide has $K_{ow} = 70,800$, a predicted BCF of **$2,650\\ \\text{L}/\\text{kg}$**, and concentrates in fish tissue to **$11.9\\ \\text{mg}/\\text{kg}$**."""
            },
            {
                "id": "prob_6_2",
                "tier": "Foundational",
                "title": "Toxic Equivalency Factor and WHO Total TEQ for a Dioxin/Furan Mixture",
                "statement": "An analysis of incinerator fly ash reveals the following mass concentrations of chlorinated dibenzo-p-dioxin and furan congeners: (1) 2,3,7,8-TCDD: $15.0\\ \\text{ng}/\\text{kg}$ ($\\text{TEF} = 1.0$), (2) 1,2,3,7,8-PeCDD: $45.0\\ \\text{ng}/\\text{kg}$ ($\\text{TEF} = 1.0$), (3) 1,2,3,4,7,8-HxCDD: $120.0\\ \\text{ng}/\\text{kg}$ ($\\text{TEF} = 0.10$), (4) 2,3,7,8-TCDF: $80.0\\ \\text{ng}/\\text{kg}$ ($\\text{TEF} = 0.10$), (5) 2,3,4,7,8-PeCDF: $60.0\\ \\text{ng}/\\text{kg}$ ($\\text{TEF} = 0.30$), and (6) Octachlorodibenzo-p-dioxin (OCDD): $2500.0\\ \\text{ng}/\\text{kg}$ ($\\text{TEF} = 0.0003$). Calculate: (a) the individual Toxic Equivalent (TEQ) contribution for each congener, and (b) the total WHO-TEQ of the ash in $\\text{ng}/\\text{kg}$.",
                "hints": [
                    "Multiply each congener's analytical concentration by its respective TEF.",
                    "Sum all individual TEQ contributions to determine total TEQ."
                ],
                "solution": """**Step 1: Compute individual TEQ contributions**
The individual congener toxic equivalents are computed as $\\text{TEQ}_i = C_i \\times \\text{TEF}_i$:

1. **2,3,7,8-TCDD**:
   \\[
   \\text{TEQ}_1 = 15.0\\ \\text{ng}/\\text{kg} \\times 1.0 = 15.00\\ \\text{ng}/\\text{kg}
   \\]
2. **1,2,3,7,8-PeCDD**:
   \\[
   \\text{TEQ}_2 = 45.0\\ \\text{ng}/\\text{kg} \\times 1.0 = 45.00\\ \\text{ng}/\\text{kg}
   \\]
3. **1,2,3,4,7,8-HxCDD**:
   \\[
   \\text{TEQ}_3 = 120.0\\ \\text{ng}/\\text{kg} \\times 0.10 = 12.00\\ \\text{ng}/\\text{kg}
   \\]
4. **2,3,7,8-TCDF**:
   \\[
   \\text{TEQ}_4 = 80.0\\ \\text{ng}/\\text{kg} \\times 0.10 = 8.00\\ \\text{ng}/\\text{kg}
   \\]
5. **2,3,4,7,8-PeCDF**:
   \\[
   \\text{TEQ}_5 = 60.0\\ \\text{ng}/\\text{kg} \\times 0.30 = 18.00\\ \\text{ng}/\\text{kg}
   \\]
6. **OCDD**:
   \\[
   \\text{TEQ}_6 = 2500.0\\ \\text{ng}/\\text{kg} \\times 0.0003 = 0.75\\ \\text{ng}/\\text{kg}
   \\]

**Step 2: Calculate total WHO-TEQ**
Summing all six congener contributions:
\\[
\\text{TEQ}_{tot} = 15.00 + 45.00 + 12.00 + 8.00 + 18.00 + 0.75 = 98.75\\ \\text{ng}/\\text{kg}
\\]

**Insight**:
Notice that while OCDD constitutes over $88\\%$ of the total mass ($2500\\ \\text{ng}/\\text{kg}$ out of $2820\\ \\text{ng}/\\text{kg}$ total), its toxic contribution is less than $1\\%$. Conversely, 1,2,3,7,8-PeCDD accounts for nearly $46\\%$ of total toxicity."""
            },
            {
                "id": "prob_6_3",
                "tier": "Foundational",
                "title": "pH-Dependent Alkaline Hydrolysis Kinetics and Half-Life of Chlorpyrifos",
                "statement": "The abiotic degradation of the organophosphate pesticide chlorpyrifos in sterile natural water at 25 °C follows pseudo-first-order kinetics with $k_{obs} = k_N + k_B [OH^-]$, where the neutral hydrolysis rate constant is $k_N = 1.20 \\times 10^{-7}\\ \\text{s}^{-1}$ and the base-catalyzed second-order rate constant is $k_B = 1.85 \\times 10^{-2}\\ \\text{M}^{-1}\\text{s}^{-1}$. (a) Calculate the observed pseudo-first-order rate constant $k_{obs}$ and the hydrolysis half-life (in days) at $\\text{pH} = 7.00$. (b) Calculate $k_{obs}$ and the half-life at an alkaline river water $\\text{pH} = 9.00$. (Take $K_w = 1.00 \\times 10^{-14}$).",
                "hints": [
                    "At pH 7.00: $[OH^-] = 10^{-(14-7)} = 1.00 \\times 10^{-7}\\ \\text{M}$.",
                    "At pH 9.00: $[OH^-] = 10^{-(14-9)} = 1.00 \\times 10^{-5}\\ \\text{M}$.",
                    "Half-life: $t_{1/2} = \\frac{\\ln 2}{k_{obs}}$ converted from seconds to days."
                ],
                "solution": """**Step 1: Calculate kinetics at pH 7.00**
At $\\text{pH} = 7.00$:
\\[
[OH^-] = \\frac{K_w}{[H^+]} = \\frac{1.00 \\times 10^{-14}}{1.00 \\times 10^{-7}} = 1.00 \\times 10^{-7}\\ \\text{M}
\\]
The observed rate constant:
\\[
k_{obs} = k_N + k_B [OH^-] = (1.20 \\times 10^{-7}) + (1.85 \\times 10^{-2})(1.00 \\times 10^{-7})
\\]
\\[
k_{obs} = 1.20 \\times 10^{-7} + 0.0185 \\times 10^{-7} = 1.2185 \\times 10^{-7}\\ \\text{s}^{-1}
\\]
The half-life in seconds:
\\[
t_{1/2} = \\frac{\\ln 2}{k_{obs}} = \\frac{0.69315}{1.2185 \\times 10^{-7}\\ \\text{s}^{-1}} = 5,688,550\\ \\text{s}
\\]
Converting to days ($1\\ \\text{day} = 86,400\\ \\text{s}$):
\\[
t_{1/2} = \\frac{5,688,550}{86,400} = 65.84\\ \\text{days} \\approx 65.8\\ \\text{days}
\\]

**Step 2: Calculate kinetics at pH 9.00**
At $\\text{pH} = 9.00$:
\\[
[OH^-] = 1.00 \\times 10^{-5}\\ \\text{M}
\\]
The base-catalyzed term dominates:
\\[
k_{obs} = (1.20 \\times 10^{-7}) + (1.85 \\times 10^{-2})(1.00 \\times 10^{-5})
\\]
\\[
k_{obs} = 1.20 \\times 10^{-7} + 1.85 \\times 10^{-7} = 3.05 \\times 10^{-7}\\ \\text{s}^{-1}
\\]
The half-life:
\\[
t_{1/2} = \\frac{0.69315}{3.05 \\times 10^{-7}\\ \\text{s}^{-1}} = 2,272,620\\ \\text{s} = \\frac{2,272,620}{86,400} = 26.30\\ \\text{days} \\approx 26.3\\ \\text{days}
\\]

**Conclusion**:
Increasing pH from 7.0 to 9.0 increases the degradation rate significantly, reducing the aquatic half-life from **65.8 days** down to **26.3 days**."""
            },
            {
                "id": "prob_6_4",
                "tier": "Intermediate",
                "title": "Acetylcholinesterase Inhibition Kinetics: Aldridge-Main Equation",
                "statement": "The inhibition of electric eel acetylcholinesterase ($E$) by paraoxon ($I$) proceeds via the two-step mechanism: $E + I \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} E \\cdot I \\xrightarrow{k_2} EI' + P$, characterized by the dissociation constant $K_a = k_{-1}/k_1$, phosphorylation rate constant $k_2$, and bimolecular rate constant $k_i = k_2 / K_a$. Under pseudo-first-order conditions ($[I] \\gg [E]$), the apparent first-order inhibition rate constant is $k_{app} = \\frac{k_2 [I]}{K_a + [I]}$. In an in vitro assay, initial rates yield the following values: at $[I] = 2.0\\ \\mu\\text{M}$, $k_{app} = 0.0150\\ \\text{s}^{-1}$; at $[I] = 10.0\\ \\mu\\text{M}$, $k_{app} = 0.0500\\ \\text{s}^{-1}$. (a) Determine the affinity constant $K_a$ (in $\\mu\\text{M}$) and the phosphorylation rate constant $k_2$ (in $\\text{s}^{-1}$). (b) Calculate the bimolecular inhibition rate constant $k_i$ (in $\\text{M}^{-1}\\text{s}^{-1}$). (c) Calculate the time required for $99\\%$ enzyme inactivation at a pesticide spill concentration of $[I] = 5.0\\ \\mu\\text{M}$.",
                "hints": [
                    "Linearize using double-reciprocal form: $\\frac{1}{k_{app}} = \\frac{K_a}{k_2}\\frac{1}{[I]} + \\frac{1}{k_2}$.",
                    "Compute $1/k_{app}$ for both concentrations and solve the 2x2 linear system.",
                    "For $99\\%$ inactivation: $[E]/[E]_0 = 0.01 \\implies t = \\frac{\\ln 100}{k_{app}}$."
                ],
                "solution": """**Step 1: Set up the Lineweaver-Burk / Kitz-Wilson linear system**
The reciprocal equation is:
\\[
\\frac{1}{k_{app}} = \\frac{K_a}{k_2} \\left( \\frac{1}{[I]} \\right) + \\frac{1}{k_2}
\\]
Let $y = 1/k_{app}$ and $x = 1/[I]$:
- Point 1: $[I]_1 = 2.0\\ \\mu\\text{M} \\implies x_1 = 0.50\\ \\mu\\text{M}^{-1}$, $y_1 = \\frac{1}{0.0150} = 66.667\\ \\text{s}$
- Point 2: $[I]_2 = 10.0\\ \\mu\\text{M} \\implies x_2 = 0.10\\ \\mu\\text{M}^{-1}$, $y_2 = \\frac{1}{0.0500} = 20.000\\ \\text{s}$

The slope of the line:
\\[
\\text{Slope} = \\frac{y_1 - y_2}{x_1 - x_2} = \\frac{66.667 - 20.000}{0.50 - 0.10} = \\frac{46.667}{0.40} = 116.667\\ \\text{s}\\cdot\\mu\\text{M}
\\]
The y-intercept:
\\[
\\text{Intercept} = y_2 - \\text{Slope} \\cdot x_2 = 20.000 - (116.667 \\times 0.10) = 20.000 - 11.667 = 8.333\\ \\text{s}
\\]

**Step 2: Calculate $k_2$, $K_a$, and $k_i$**
Since $\\text{Intercept} = 1/k_2$:
\\[
k_2 = \\frac{1}{8.333\\ \\text{s}} = 0.120\\ \\text{s}^{-1}
\\]
Since $\\text{Slope} = K_a / k_2$:
\\[
K_a = \\text{Slope} \\times k_2 = 116.667\\ \\text{s}\\cdot\\mu\\text{M} \\times 0.120\\ \\text{s}^{-1} = 14.00\\ \\mu\\text{M}
\\]
The bimolecular inhibition constant:
\\[
k_i = \\frac{k_2}{K_a} = \\frac{0.120\\ \\text{s}^{-1}}{14.00 \\times 10^{-6}\\ \\text{M}} = 8,571.4\\ \\text{M}^{-1}\\text{s}^{-1} \\approx 8.57 \\times 10^3\\ \\text{M}^{-1}\\text{s}^{-1}
\\]

**Step 3: Calculate time for $99\\%$ inactivation at $[I] = 5.0\\ \\mu\\text{M}$**
At $[I] = 5.0\\ \\mu\\text{M}$:
\\[
k_{app} = \\frac{k_2 [I]}{K_a + [I]} = \\frac{(0.120)(5.0)}{14.0 + 5.0} = \\frac{0.600}{19.0} = 0.03158\\ \\text{s}^{-1}
\\]
For $99\\%$ inactivation, remaining active enzyme is $1\\%$ ($[E]/[E]_0 = 0.01$):
\\[
\\ln(0.01) = -k_{app} t \\implies t_{99\\%} = \\frac{\\ln 100}{k_{app}} = \\frac{4.6052}{0.03158\\ \\text{s}^{-1}} = 145.8\\ \\text{s} \\approx 2.43\\ \\text{minutes}
\\]

**Conclusion**:
The kinetic constants are $K_a = 14.0\\ \\mu\\text{M}$, $k_2 = 0.120\\ \\text{s}^{-1}$, and $k_i = 8.57 \\times 10^3\\ \\text{M}^{-1}\\text{s}^{-1}$. At $5.0\\ \\mu\\text{M}$, $99\\%$ of synaptic AChE is knocked out in less than **2.5 minutes**."""
            },
            {
                "id": "prob_6_5",
                "tier": "Intermediate",
                "title": "Mackay Level I Multimedia Fugacity Model for PCB-153",
                "statement": "An environmental model unit area ($100\\ \\text{km}^2$) contains four compartments at $25^\\circ\\text{C}$ ($T = 298.15\\ \\text{K}$, $R = 8.314\\ \\text{Pa}\\cdot\\text{m}^3/(\\text{mol}\\cdot\\text{K})$):\\n1. Air: $V_a = 1.00 \\times 10^{11}\\ \\text{m}^3$\\n2. Water: $V_w = 2.00 \\times 10^8\\ \\text{m}^3$\\n3. Soil: $V_s = 1.50 \\times 10^7\\ \\text{m}^3$, $\\rho_s = 1500\\ \\text{kg}/\\text{m}^3$, organic carbon fraction $f_{oc,s} = 0.02$\\n4. Sediment: $V_{sed} = 1.00 \\times 10^6\\ \\text{m}^3$, $\\rho_{sed} = 1300\\ \\text{kg}/\\text{m}^3$, $f_{oc,sed} = 0.04$\\nFor the persistent toxicant PCB-153 ($2,2',4,4',5,5'\\text{-hexachlorobiphenyl}$, $M = 360.88\\ \\text{g}/\\text{mol}$): Henry's constant $H = 28.5\\ \\text{Pa}\\cdot\\text{m}^3/\\text{mol}$, and organic carbon partition coefficient $\\log K_{oc} = 6.20$ ($K_{oc} = 1.585 \\times 10^6\\ \\text{L}/\\text{kg} = 1.585 \\times 10^3\\ \\text{m}^3/\\text{kg}$). A total mass of $M_{tot} = 100.0\\ \\text{kg}$ of PCB-153 is introduced. Calculate: (a) the fugacity capacity ($Z$-value) and total capacity ($V_i Z_i$) for each compartment, (b) the equilibrium system fugacity $f_{eq}$ in Pascals, and (c) the percentage of total PCB mass residing in each compartment.",
                "hints": [
                    "Air: $Z_a = 1/(RT)$.",
                    "Water: $Z_w = 1/H$.",
                    "Soil: $Z_s = \\rho_s f_{oc,s} K_{oc} / H$.",
                    "Sediment: $Z_{sed} = \\rho_{sed} f_{oc,sed} K_{oc} / H$.",
                    "Equilibrium fugacity: $f_{eq} = n_{tot} / \\sum(V_i Z_i)$ where $n_{tot} = 100,000\\ \\text{g} / 360.88\\ \\text{g}/\\text{mol}$."
                ],
                "solution": """**Step 1: Calculate $Z$-values for all four compartments**
Given:
- $RT = (8.314)(298.15) = 2478.8\\ \\text{Pa}\\cdot\\text{m}^3/\\text{mol}$
- $H = 28.5\\ \\text{Pa}\\cdot\\text{m}^3/\\text{mol}$
- $K_{oc} = 1.585 \\times 10^3\\ \\text{m}^3/\\text{kg}$

1. **Air**:
   \\[
   Z_a = \\frac{1}{RT} = \\frac{1}{2478.8} = 4.034 \\times 10^{-4}\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})
   \\]
2. **Water**:
   \\[
   Z_w = \\frac{1}{H} = \\frac{1}{28.5} = 3.509 \\times 10^{-2}\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})
   \\]
3. **Soil**:
   The soil sorption coefficient $K_d = f_{oc,s} K_{oc} = 0.02 \\times 1.585 \\times 10^3 = 31.70\\ \\text{m}^3/\\text{kg}$:
   \\[
   Z_s = \\frac{\\rho_s K_d}{H} = \\frac{(1500\\ \\text{kg}/\\text{m}^3)(31.70\\ \\text{m}^3/\\text{kg})}{28.5\\ \\text{Pa}\\cdot\\text{m}^3/\\text{mol}} = \\frac{47,550}{28.5} = 1,668.4\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})
   \\]
4. **Sediment**:
   $K_d = f_{oc,sed} K_{oc} = 0.04 \\times 1.585 \\times 10^3 = 63.40\\ \\text{m}^3/\\text{kg}$:
   \\[
   Z_{sed} = \\frac{\\rho_{sed} K_d}{H} = \\frac{(1300\\ \\text{kg}/\\text{m}^3)(63.40\\ \\text{m}^3/\\text{kg})}{28.5} = \\frac{82,420}{28.5} = 2,891.9\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})
   \\]

**Step 2: Calculate total compartment capacities ($V_i Z_i$)**
- Air: $V_a Z_a = (1.00 \\times 10^{11}) \\times (4.034 \\times 10^{-4}) = 4.034 \\times 10^7\\ \\text{mol}/\\text{Pa}$
- Water: $V_w Z_w = (2.00 \\times 10^8) \\times (3.509 \\times 10^{-2}) = 7.018 \\times 10^6\\ \\text{mol}/\\text{Pa}$
- Soil: $V_s Z_s = (1.50 \\times 10^7) \\times (1668.4) = 2.5026 \\times 10^{10}\\ \\text{mol}/\\text{Pa}$
- Sediment: $V_{sed} Z_{sed} = (1.00 \\times 10^6) \\times (2891.9) = 2.8919 \\times 10^9\\ \\text{mol}/\\text{Pa}$

Summing all compartments:
\\[
\\sum (V_i Z_i) = 4.034 \\times 10^7 + 0.0070 \\times 10^{10} + 2.5026 \\times 10^{10} + 0.2892 \\times 10^{10} = 2.7958 \\times 10^{10}\\ \\text{mol}/\\text{Pa}
\\]

**Step 3: Calculate equilibrium fugacity $f_{eq}$ and mass distribution**
Total moles of PCB-153:
\\[
n_{tot} = \\frac{100,000\\ \\text{g}}{360.88\\ \\text{g}/\\text{mol}} = 277.10\\ \\text{mol}
\\]
The system equilibrium fugacity:
\\[
f_{eq} = \\frac{n_{tot}}{\\sum (V_i Z_i)} = \\frac{277.10\\ \\text{mol}}{2.7958 \\times 10^{10}\\ \\text{mol}/\\text{Pa}} = 9.911 \\times 10^{-9}\\ \\text{Pa}
\\]

Mass percentage in each compartment (since $m_i \\propto V_i Z_i$):
- **Soil**: $\\frac{2.5026 \\times 10^{10}}{2.7958 \\times 10^{10}} \\times 100 = 89.51\\%$ ($89.51\\ \\text{kg}$)
- **Sediment**: $\\frac{0.2892 \\times 10^{10}}{2.7958 \\times 10^{10}} \\times 100 = 10.34\\%$ ($10.34\\ \\text{kg}$)
- **Air**: $\\frac{4.034 \\times 10^7}{2.7958 \\times 10^{10}} \\times 100 = 0.144\\%$ ($0.144\\ \\text{kg}$)
- **Water**: $\\frac{7.018 \\times 10^6}{2.7958 \\times 10^{10}} \\times 100 = 0.025\\%$ ($0.025\\ \\text{kg}$)

**Conclusion**:
Over **$99.8\\%$** of environmental PCB-153 partitions into the organic-rich soil and sediment solid phases, with only traces remaining free in the air and water."""
            },
            {
                "id": "prob_6_6",
                "tier": "Intermediate",
                "title": "Mackay Level II Open Fugacity Model with Advection and Reaction",
                "statement": "An open lake system with volume $V = 5.00 \\times 10^7\\ \\text{m}^3$ and fugacity capacity $Z = 0.040\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})$ receives a constant chemical input of $E = 2.50\\ \\text{mol}/\\text{h}$. Water flows through the lake at advection rate $G = 2.00 \\times 10^4\\ \\text{m}^3/\\text{h}$. The chemical undergoes in-situ biodegradation with first-order rate constant $k = 3.50 \\times 10^{-3}\\ \\text{h}^{-1}$. (a) Calculate the advective D-value ($D_A = G Z$) and the reactive D-value ($D_R = V Z k$) in $\\text{mol}/(\\text{h}\\cdot\\text{Pa})$. (b) Determine the steady-state lake fugacity $f_{ss}$ (in Pa) and aqueous concentration $C$ (in $\\mu\\text{mol}/\\text{m}^3$). (c) Calculate the overall residence time $\\tau$ of the chemical in the lake and the fraction removed via biodegradation.",
                "hints": [
                    "$D_A = G \\cdot Z$ and $D_R = V \\cdot Z \\cdot k$.",
                    "Mass balance: $E = f_{ss}(D_A + D_R) \\implies f_{ss} = E / (D_A + D_R)$.",
                    "Concentration: $C = f_{ss} \\cdot Z$."
                ],
                "solution": """**Step 1: Calculate $D$-values for advection and reaction**
Given:
- $V = 5.00 \\times 10^7\\ \\text{m}^3$
- $Z = 0.040\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})$
- $G = 2.00 \\times 10^4\\ \\text{m}^3/\\text{h}$
- $k = 3.50 \\times 10^{-3}\\ \\text{h}^{-1}$

1. **Advective transport parameter ($D_A$)**:
   \\[
   D_A = G \\cdot Z = (2.00 \\times 10^4\\ \\text{m}^3/\\text{h})(0.040\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})) = 800.0\\ \\text{mol}/(\\text{h}\\cdot\\text{Pa})
   \\]
2. **Reactive transformation parameter ($D_R$)**:
   \\[
   D_R = V \\cdot Z \\cdot k = (5.00 \\times 10^7\\ \\text{m}^3)(0.040\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa}))(3.50 \\times 10^{-3}\\ \\text{h}^{-1})
   \\]
   \\[
   D_R = 2.00 \\times 10^6 \\times 3.50 \\times 10^{-3} = 7,000.0\\ \\text{mol}/(\\text{h}\\cdot\\text{Pa})
   \\]
Total system D-value:
\\[
D_T = D_A + D_R = 800.0 + 7,000.0 = 7,800.0\\ \\text{mol}/(\\text{h}\\cdot\\text{Pa})
\\]

**Step 2: Calculate steady-state fugacity and aqueous concentration**
Given emission rate $E = 2.50\\ \\text{mol}/\\text{h}$:
\\[
f_{ss} = \\frac{E}{D_T} = \\frac{2.50\\ \\text{mol}/\\text{h}}{7,800.0\\ \\text{mol}/(\\text{h}\\cdot\\text{Pa})} = 3.205 \\times 10^{-4}\\ \\text{Pa}
\\]
The steady-state aqueous concentration:
\\[
C = Z \\cdot f_{ss} = (0.040\\ \\text{mol}/(\\text{m}^3\\cdot\\text{Pa})) \\times (3.205 \\times 10^{-4}\\ \\text{Pa}) = 1.282 \\times 10^{-5}\\ \\text{mol}/\\text{m}^3 = 12.82\\ \\mu\\text{mol}/\\text{m}^3
\\]

**Step 3: Calculate residence time and biodegradation fraction**
Total chemical inventory in the lake:
\\[
M = V \\cdot C = (5.00 \\times 10^7\\ \\text{m}^3)(1.282 \\times 10^{-5}\\ \\text{mol}/\\text{m}^3) = 641.0\\ \\text{mol}
\\]
Overall residence time $\\tau$:
\\[
\\tau = \\frac{M}{E} = \\frac{641.0\\ \\text{mol}}{2.50\\ \\text{mol}/\\text{h}} = 256.4\\ \\text{hours} \\approx 10.68\\ \\text{days}
\\]
Fraction of chemical degraded biologically:
\\[
\\%\\text{Biodegraded} = \\frac{D_R}{D_T} \\times 100 = \\frac{7000.0}{7800.0} \\times 100 = 89.74\\%
\\]

**Conclusion**:
The steady-state fugacity is **$3.21 \\times 10^{-4}\\ \\text{Pa}$**, the chemical residence time is **10.7 days**, and **$89.7\\%$** is eliminated via biodegradation rather than hydraulic outflow."""
            },
            {
                "id": "prob_6_7",
                "tier": "Advanced",
                "title": "Global Fractionation: Junge-Pankow Adsorption and Grasshopper Effect",
                "statement": "The atmospheric gas-particle partitioning of hexachlorobenzene (HCB) is governed by the Junge-Pankow model: $\\phi = \\frac{c_J \\theta}{P_L^\\circ + c_J \\theta}$, where $\\phi$ is the fraction bound to aerosol particles, $\\theta = 1.50 \\times 10^{-7}\\ \\text{m}^2/\\text{m}^3$ is aerosol surface area per unit air volume, and $c_J = 1.72 \\times 10^{-2}\\ \\text{Pa}\\cdot\\text{m}$. The sub-cooled liquid vapor pressure $P_L^\\circ$ follows the Clausius-Clapeyron equation: $\\ln(P_L^\\circ/\\text{Pa}) = -\\frac{\\Delta H_{vap}}{R}\\left(\\frac{1}{T} - \\frac{1}{T_0}\\right) + \\ln(P_{L,0}^\\circ)$, where $\\Delta H_{vap} = 72.0\\ \\text{kJ}/\\text{mol}$ and $P_L^\\circ(298.15\\ \\text{K}) = 0.230\\ \\text{Pa}$. (a) Calculate $P_L^\\circ$ and the particle-bound fraction $\\phi$ at tropical temperatures ($T = +30^\\circ\\text{C} = 303.15\\ \\text{K}$). (b) Calculate $P_L^\\circ$ and $\\phi$ under Arctic conditions ($T = -30^\\circ\\text{C} = 243.15\\ \\text{K}$). (c) Discuss how this thermal shift drives the planetary 'cold condensation' deposition of HCB.",
                "hints": [
                    "Calculate $c_J \\theta = (1.72 \\times 10^{-2})(1.50 \\times 10^{-7}) = 2.58 \\times 10^{-9}\\ \\text{Pa}\\cdot\\text{m}$.",
                    "Use $\\ln(P_L^\\circ) = \\ln(0.230) - \\frac{72000}{8.314}(1/T - 1/298.15)$.",
                    "Evaluate $\\phi = \\frac{2.58 \\times 10^{-9}}{P_L^\\circ + 2.58 \\times 10^{-9}}$ at both temperatures."
                ],
                "solution": """**Step 1: Compute constant product $c_J \\theta$**
\\[
c_J \\theta = (1.72 \\times 10^{-2}\\ \\text{Pa}\\cdot\\text{m}) \\times (1.50 \\times 10^{-7}\\ \\text{m}^2/\\text{m}^3) = 2.58 \\times 10^{-9}\\ \\text{Pa}
\\]

**Step 2: Evaluate tropical conditions ($T = 303.15\\ \\text{K}$)**
Using the Clausius-Clapeyron relation with $R = 8.314\\ \\text{J}/(\\text{mol}\\cdot\\text{K})$:
\\[
\\frac{\\Delta H_{vap}}{R} = \\frac{72,000}{8.314} = 8,660.1\\ \\text{K}
\\]
\\[
\\frac{1}{303.15} - \\frac{1}{298.15} = 0.0032987 - 0.0033540 = -5.532 \\times 10^{-5}\\ \\text{K}^{-1}
\\]
\\[
\\ln(P_L^\\circ) = \\ln(0.230) - (8660.1)(-5.532 \\times 10^{-5}) = -1.4697 + 0.4791 = -0.9906
\\]
\\[
P_L^\\circ(303.15\\ \\text{K}) = e^{-0.9906} = 0.3713\\ \\text{Pa}
\\]
Particle-bound fraction:
\\[
\\phi_{tropical} = \\frac{2.58 \\times 10^{-9}}{0.3713 + 2.58 \\times 10^{-9}} \\approx \\frac{2.58 \\times 10^{-9}}{0.3713} = 6.95 \\times 10^{-9} \\quad (0.0000007\\%)
\\]
In the tropics, $99.999999\\%$ of HCB exists in the gaseous vapor phase, freely subject to long-range atmospheric wind advection.

**Step 3: Evaluate Arctic conditions ($T = 243.15\\ \\text{K}$)**
\\[
\\frac{1}{243.15} - \\frac{1}{298.15} = 0.0041127 - 0.0033540 = +7.5866 \\times 10^{-4}\\ \\text{K}^{-1}
\\]
\\[
\\ln(P_L^\\circ) = \\ln(0.230) - (8660.1)(7.5866 \\times 10^{-4}) = -1.4697 - 6.5701 = -8.0398
\\]
\\[
P_L^\\circ(243.15\\ \\text{K}) = e^{-8.0398} = 3.224 \\times 10^{-4}\\ \\text{Pa}
\\]
Particle-bound fraction:
\\[
\\phi_{arctic} = \\frac{2.58 \\times 10^{-9}}{3.224 \\times 10^{-4} + 2.58 \\times 10^{-9}} \\approx 8.00 \\times 10^{-6}
\\]
While still primarily gaseous, the particle partitioning increases by over **3 orders of magnitude** ($1150\\times$), facilitating scavenging by snow crystals and dry aerosol deposition. For heavier POPs with higher $\\Delta H_{vap}$, $\\phi$ jumps from near $0$ to $>90\\%$, precipitating massive 'cold condensation' washouts over polar ice sheets."""
            },
            {
                "id": "prob_6_8",
                "tier": "Advanced",
                "title": "Dynamic Trophic Bioaccumulation: Ingestion and Elimination Rates",
                "statement": "A multi-pathway bioaccumulation model for a predatory salmon feeding in Lake Superior is described by: $\\frac{dC}{dt} = k_1 C_w + \\alpha F C_f - (k_2 + k_g) C$, where: water uptake rate $k_1 = 350\\ \\text{L}/(\\text{kg}\\cdot\\text{day})$, aqueous DDE concentration $C_w = 1.20 \\times 10^{-7}\\ \\text{mg}/\\text{L}$ ($0.12\\ \\text{ng}/\\text{L}$), prey assimilation efficiency $\\alpha = 0.75$, feeding rate $F = 0.020\\ \\text{kg}_{prey}/(\\text{kg}_{fish}\\cdot\\text{day})$, prey concentration $C_f = 0.150\\ \\text{mg}/\\text{kg}$, depuration rate constant $k_2 = 0.0012\\ \\text{day}^{-1}$, and growth rate constant $k_g = 0.0028\\ \\text{day}^{-1}$. (a) Calculate the steady-state body concentration $C^\\infty$ in $\\text{mg}/\\text{kg}$. (b) Calculate the Bioaccumulation Factor (BAF) and the Biomagnification Factor (BMF). (c) If emissions cease and the lake water and prey become pristine ($C_w = 0, C_f = 0$), calculate the biological half-life of DDE in the fish (both with and without growth dilution).",
                "hints": [
                    "At steady-state: $C^\\infty = \\frac{k_1 C_w + \\alpha F C_f}{k_2 + k_g}$.",
                    "$\\text{BAF} = C^\\infty / C_w$ and $\\text{BMF} = C^\\infty / C_f$.",
                    "Biological half-life with growth: $t_{1/2} = \\frac{\\ln 2}{k_2 + k_g}$; without growth: $t_{1/2} = \\frac{\\ln 2}{k_2}$."
                ],
                "solution": """**Step 1: Calculate intake rates and steady-state concentration**
Respiratory gill uptake flux:
\\[
J_{water} = k_1 C_w = (350\\ \\text{L}/(\\text{kg}\\cdot\\text{day})) \\times (1.20 \\times 10^{-7}\\ \\text{mg}/\\text{L}) = 4.20 \\times 10^{-5}\\ \\text{mg}/(\\text{kg}\\cdot\\text{day})
\\]
Dietary intake flux:
\\[
J_{diet} = \\alpha F C_f = (0.75)(0.020\\ \\text{day}^{-1})(0.150\\ \\text{mg}/\\text{kg}) = 2.25 \\times 10^{-3}\\ \\text{mg}/(\\text{kg}\\cdot\\text{day})
\\]
Total uptake flux:
\\[
J_{tot} = 4.20 \\times 10^{-5} + 2.25 \\times 10^{-3} = 2.292 \\times 10^{-3}\\ \\text{mg}/(\\text{kg}\\cdot\\text{day})
\\]
Total elimination/dilution rate constant:
\\[
k_T = k_2 + k_g = 0.0012 + 0.0028 = 0.0040\\ \\text{day}^{-1}
\\]
Steady-state fish body concentration:
\\[
C^\\infty = \\frac{J_{tot}}{k_T} = \\frac{2.292 \\times 10^{-3}}{0.0040} = 0.573\\ \\text{mg}/\\text{kg}
\\]

**Step 2: Calculate BAF and BMF**
\\[
\\text{BAF} = \\frac{C^\\infty}{C_w} = \\frac{0.573\\ \\text{mg}/\\text{kg}}{1.20 \\times 10^{-7}\\ \\text{mg}/\\text{L}} = 4.775 \\times 10^6\\ \\text{L}/\\text{kg} \\approx 4.78 \\times 10^6\\ \\text{L}/\\text{kg}
\\]
\\[
\\text{BMF} = \\frac{C^\\infty}{C_f} = \\frac{0.573\\ \\text{mg}/\\text{kg}}{0.150\\ \\text{mg}/\\text{kg}} = 3.82
\\]
Since $\\text{BMF} = 3.82 > 1$, significant trophic biomagnification is verified.

**Step 3: Biological elimination half-lives**
1. **Effective half-life with somatic growth dilution**:
   \\[
   t_{1/2, eff} = \\frac{\\ln 2}{k_2 + k_g} = \\frac{0.69315}{0.0040\\ \\text{day}^{-1}} = 173.3\\ \\text{days} \\approx 0.47\\ \\text{years}
   \\]
2. **True chemical depuration half-life without growth dilution ($k_g = 0$)**:
   \\[
   t_{1/2, chem} = \\frac{\\ln 2}{k_2} = \\frac{0.69315}{0.0012\\ \\text{day}^{-1}} = 577.6\\ \\text{days} \\approx 1.58\\ \\text{years}
   \\]

**Conclusion**:
The fish accumulates DDE to **$0.573\\ \\text{mg}/\\text{kg}$**, yielding an extraordinary BAF of **$4.78 \\times 10^6\\ \\text{L}/\\text{kg}$** and a BMF of **3.82**, with a depuration half-life of **1.58 years**."""
            },
            {
                "id": "prob_6_9",
                "tier": "Advanced",
                "title": "Aqueous Photolysis Kinetics and Quantum Yield of 2,3,7,8-TCDD",
                "statement": "The direct photochemical degradation of $2,3,7,8\\text{-TCDD}$ dissolved in surface water exposed to noon summer sunlight is described by the first-order rate equation: $-\\frac{dC}{dt} = k_p C$, where $k_p = 2.303 \\Phi \\sum (\\epsilon_\\lambda I_\\lambda)$. Over the actinic spectral window ($290 - 330\\ \\text{nm}$), integrated solar irradiance and molar absorptivity data yield a solar actinic overlap integral of $\\sum (\\epsilon_\\lambda I_\\lambda) = 3.65 \\times 10^{-4}\\ \\text{einstein}/(\\text{L}\\cdot\\text{s})$. In an organic-cosolvent sensitized solution, the primary photochemical quantum yield is $\\Phi = 2.40 \\times 10^{-4}\\ \\text{mol}/\\text{einstein}$. (a) Calculate the photolysis rate constant $k_p$ in $\\text{s}^{-1}$ and $\\text{day}^{-1}$ (assuming 12 equivalent sunlight hours per day). (b) Calculate the photochemical half-life $t_{1/2}$ in days under continuous solar irradiation. (c) If aquatic natural organic matter (NOM) acts as an optical filter, attenuating $85\\%$ of actinic photons before they reach the contaminant, calculate the revised environmental half-life in the turbid natural water body.",
                "hints": [
                    "$k_p = 2.303 \\times \\Phi \\times \\sum (\\epsilon_\\lambda I_\\lambda)$.",
                    "Convert from per-second to per-day: $k_p(\\text{day}^{-1}) = k_p(\\text{s}^{-1}) \\times (12 \\times 3600\\ \\text{s})$.",
                    "Optical screening: Effective rate is $k'_{p} = k_p \\times (1 - 0.85) = 0.15 k_p$."
                ],
                "solution": """**Step 1: Calculate the direct photolysis rate constant $k_p$**
Given:
- Overlap integral: $\\sum (\\epsilon_\\lambda I_\\lambda) = 3.65 \\times 10^{-4}\\ \\text{einstein}/(\\text{L}\\cdot\\text{s})$
- Quantum yield: $\\Phi = 2.40 \\times 10^{-4}\\ \\text{mol}/\\text{einstein}$

The first-order rate constant:
\\[
k_p = 2.303 \\times \\Phi \\times \\sum (\\epsilon_\\lambda I_\\lambda)
\\]
\\[
k_p = 2.303 \\times (2.40 \\times 10^{-4}) \\times (3.65 \\times 10^{-4}) = 2.0175 \\times 10^{-7}\\ \\text{s}^{-1}
\\]
Converting to daylight hours ($12\\ \\text{hours/day} = 12 \\times 3600\\ \\text{s} = 43,200\\ \\text{s/day}$):
\\[
k_{p, day} = 2.0175 \\times 10^{-7}\\ \\text{s}^{-1} \\times 43,200\\ \\text{s/day} = 8.7156 \\times 10^{-3}\\ \\text{day}^{-1}
\\]

**Step 2: Calculate unattenuated photochemical half-life**
\\[
t_{1/2} = \\frac{\\ln 2}{k_{p, day}} = \\frac{0.69315}{8.7156 \\times 10^{-3}\\ \\text{day}^{-1}} = 79.53\\ \\text{days} \\approx 79.5\\ \\text{days}
\\]

**Step 3: Calculate half-life with $85\\%$ NOM light screening**
When natural organic matter attenuates $85\\%$ of incident actinic photons, the transmitted photon flux is only $15\\%$ ($0.15$):
\\[
k'_{p, day} = 0.15 \\times k_{p, day} = 0.15 \\times (8.7156 \\times 10^{-3}) = 1.3073 \\times 10^{-3}\\ \\text{day}^{-1}
\\]
The revised environmental half-life is:
\\[
t'_{1/2} = \\frac{0.69315}{1.3073 \\times 10^{-3}\\ \\text{day}^{-1}} = 530.2\\ \\text{days} \\approx 1.45\\ \\text{years}
\\]

**Conclusion**:
In clear surface water, 2,3,7,8-TCDD undergoes direct photolysis with a half-life of **79.5 days**. However, dissolved humic light attenuation extends this half-life to **1.45 years** (530 days), explaining its extreme persistence in turbid aquatic ecosystems."""
            }
        ]
    }
    return unit

if __name__ == "__main__":
    u6 = get_unit_6()
    print(f"Unit 6 generated: {len(u6['sections'])} sections, {len(u6['problems'])} problems.")
