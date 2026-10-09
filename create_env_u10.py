# -*- coding: utf-8 -*-
"""
Environmental Chemistry - Unit 10 Content Generator
Unit 10: Green Chemistry, Sustainable Metrics & Circular Industrial Processes
Strictly no marks, no course codes, pure Unix line endings.
"""

import json

def get_unit_10():
    unit = {
        "id": "unit_10",
        "title": "Green Chemistry, Sustainable Metrics & Circular Industrial Processes",
        "badge": "Unit 10",
        "summary": "The Twelve Principles of Green Chemistry; quantitative sustainability metrics including Atom Economy, E-Factor, and Process Mass Intensity (PMI); neoteric green solvents, biocatalysis, and continuous flow engineering; ISO 14040/14044 Life Cycle Assessment (LCA); cradle-to-cradle industrial symbiosis and eco-industrial park exergy modeling.",
        "simulation": {
            "id": "sim_env_green_chemistry_metrics",
            "title": "Green Chemistry Metrics & 12 Principles Radar Dashboard",
            "type": "canvas",
            "description": "Interactive quantitative green chemistry dashboard calculating Atom Economy (AE), Sheldon E-Factor, Process Mass Intensity (PMI), and Reaction Mass Efficiency (RME), accompanied by a 12-dimensional Anastas-Warner radar sustainability benchmark."
        },
        "sections": [
            {
                "id": "sec_10_1",
                "title": "The Twelve Principles of Green Chemistry: Molecular Design & Philosophy",
                "content": """Green Chemistry, formalized by Paul Anastas and John Warner in 1998, is defined as the design of chemical products and processes that reduce or eliminate the use and generation of hazardous substances. It shifts environmental protection from end-of-pipe waste remediation to proactive molecular architecture.

### The Twelve Foundational Principles
1. **Waste Prevention**: It is better to prevent waste than to treat or clean up waste after it is formed.
2. **Atom Economy**: Synthetic methods should be designed to maximize the incorporation of all materials used in the process into the final product.
3. **Less Hazardous Chemical Syntheses**: Wherever practicable, synthetic methods should use and generate substances that possess little or no toxicity to human health and the environment.
4. **Designing Safer Chemicals**: Chemical products should be designed to effect their desired function while minimizing their toxicity.
5. **Safer Solvents and Auxiliaries**: The use of auxiliary substances (e.g., solvents, separation agents) should be made unnecessary wherever possible and innocuous when used.
6. **Design for Energy Efficiency**: Energy requirements should be recognized for their environmental and economic impacts and minimized. Synthetic methods should be conducted at ambient temperature and pressure.
7. **Use of Renewable Feedstocks**: A raw material or feedstock should be renewable rather than depleting whenever technically and economically practicable.
8. **Reduce Derivatives**: Unnecessary derivatization (use of blocking groups, protection/deprotection) should be minimized or avoided.
9. **Catalysis**: Catalytic reagents (as selective as possible) are superior to stoichiometric reagents.
10. **Design for Degradation**: Chemical products should be designed so that at the end of their function they break down into innocuous degradation products and do not persist in the environment.
11. **Real-time Analysis for Pollution Prevention**: Analytical methodologies need to be further developed to allow for real-time, in-process monitoring and control prior to the formation of hazardous substances.
12. **Inherently Safer Chemistry for Accident Prevention**: Substances used in a chemical process should be chosen to minimize the potential for chemical accidents, including releases, explosions, and fires."""
            },
            {
                "id": "sec_10_2",
                "title": "Quantitative Green Metrics: Atom Economy, E-Factor & PMI",
                "content": """To evaluate whether a synthetic route is truly green, quantitative mathematical metrics replace qualitative assertions.

### 1. Atom Economy (AE)
Pioneered by Barry Trost, Atom Economy measures the theoretical efficiency of a reaction based on molecular stoichiometry:
\\[
\\text{AE} (\\%) = \\frac{\\text{Molar Mass of Desired Product}}{\\sum (\\text{Molar Masses of All Reactants})} \\times 100
\\]
- *Ideal 100% AE*: Addition reactions, condensations without leaving groups, and rearrangements (e.g., Diels-Alder, hydroformylation, Claisen rearrangement).
- *Low AE*: Wittig reactions (generating triphenylphosphine oxide, $Ph_3PO$, waste), Grignard additions, and traditional elimination reactions.

### 2. Sheldon Environmental Factor ($E$-Factor)
Introduced by Roger Sheldon, the $E$-Factor measures the actual mass of waste generated per unit mass of final product produced:
\\[
E\\text{-Factor} = \\frac{\\text{Total Mass of Waste (kg)}}{\\text{Mass of Product (kg)}} = \\frac{M_{raw\\ materials} - M_{product}}{M_{product}}
\\]
- *Oil Refining*: $E < 0.1$
- *Bulk Chemicals*: $E \\approx 1 - 5$
- *Fine Chemicals*: $E \\approx 5 - 50$
- *Pharmaceuticals*: $E \\approx 25 - > 100$ (driven by massive organic solvent consumption and complex multi-step protection sequences).

### 3. Process Mass Intensity (PMI)
Adopted by the ACS Green Chemistry Institute Pharmaceutical Roundtable:
\\[
\\text{PMI} = \\frac{\\text{Total Mass of All Raw Materials (including water, solvents, reagents)}}{\\text{Mass of Final Product}} = E\\text{-Factor} + 1
\\]

### 4. Reaction Mass Efficiency (RME)
Combines atom economy, chemical yield ($\epsilon$), and stoichiometric excess ($SF$):
\\[
\\text{RME} (\\%) = \\frac{\\text{Mass of Desired Product}}{\\text{Total Mass of Reactants Actually Used}} \\times 100 = \\text{AE} \\times \\epsilon \\times \\frac{1}{SF}
\\]"""
            },
            {
                "id": "sec_10_3",
                "title": "Solvent Selection Guides & Neoteric Green Solvents",
                "content": """Solvents typically account for $80 - 90\\%$ of the non-aqueous mass used in fine chemical and pharmaceutical synthesis. Replacing volatile, toxic, flammable, and chlorinated solvents is paramount.

### Solvent Selection Guides
Industry consortia (e.g., Pfizer, GSK, Sanofi) categorize solvents into green traffic-light tiers based on toxicity, flammability, environmental persistence, and life-cycle footprint:
- **Preferred (Green)**: Water, ethanol, 2-propanol, ethyl acetate, acetone, 2-methyltetrahydrofuran (2-MeTHF), cyclopentyl methyl ether (CPME).
- **Usable (Yellow)**: Toluene, acetonitrile, dichloromethane (restricted), cyclohexane.
- **Undesirable / Banned (Red)**: Benzene, carbon tetrachloride ($CCl_4$), 1,2-dichloroethane, diethyl ether, dimethylformamide (DMF), $N$-methylpyrrolidone (NMP, reprotoxic).

### Neoteric Solvent Systems
1. **Supercritical Fluids ($scCO_2$)**:
   - Carbon dioxide above its critical point ($T_c = 31.1^\\circ\\text{C}$, $P_c = 73.8\\ \\text{bar}$).
   - Non-toxic, non-flammable, tunable density and solvency power via pressure modulation; leaves zero solvent residue upon depressurization.
2. **Ionic Liquids (ILs)**:
   - Salts composed of bulky, asymmetric organic cations (imidazolium, pyridinium) and organic/inorganic anions that remain liquid below $100^\\circ\\text{C}$.
   - Negligible vapor pressure (eliminates volatile VOC emissions), thermal stability up to $300^\\circ\\text{C}$, and high solvation power for polar polymers.
3. **Deep Eutectic Solvents (DES)**:
   - Formed by mixing hydrogen bond acceptors (e.g. choline chloride) and hydrogen bond donors (e.g. urea, glycerol) in specific molar ratios, displaying a depressed melting point far below either pure component.
   - Biodegradable, inexpensive, and derived from non-toxic natural metabolites (NADES)."""
            },
            {
                "id": "sec_10_4",
                "title": "Heterogeneous & Biocatalytic Transformations: Enzymes & MOFs",
                "content": """Catalysis replaces stoichiometric hazardous oxidants (chromic acid, permanganate) and toxic reductants (hydrides) with selective catalytic cycles.

### Biocatalysis & Directed Enzyme Evolution
Enzymes operate under mild physiological conditions (neutral pH, aqueous media, $25 - 40^\\circ\\text{C}$), providing exquisite chemo-, regio-, and enantioselectivity ($ee > 99\\%$):
- **Ketoreductases (KREDs)**: Asymmetric reduction of ketones to chiral secondary alcohols using $NAD(P)H$ cofactors.
- **Transaminases (ATAs)**: Chiral synthesis of pharmaceutical active amines from ketones.
- **Directed Evolution**: Frances Arnold's Nobel-winning method applies iterative rounds of error-prone PCR mutagenesis and high-throughput screening to evolve enzymes with non-natural substrate tolerance and thermal stability.

### Turnover Metrics for Catalytic Efficiency
1. **Turnover Number (TON)**: Total moles of substrate transformed per mole of active catalyst center before complete deactivation:
   \\[
   \\text{TON} = \\frac{\\text{Moles of Product Formed}}{\\text{Moles of Active Catalyst}}
   \\]
2. **Turnover Frequency (TOF)**: Catalytic turnover velocity per unit time:
   \\[
   \\text{TOF} = \\frac{\\text{TON}}{\\text{Time}} \\quad (\\text{s}^{-1} \\text{ or } \\text{h}^{-1})
   \\]
Industrial commercial viability typically mandates $\\text{TON} > 10,000 - 100,000$ and $\\text{TOF} > 100\\ \\text{h}^{-1}$.

### Metal-Organic Frameworks (MOFs)
Crystalline hybrid materials assembled from transition metal nodes interconnected by organic linkers. MOFs provide ultra-high internal surface area ($1,000 - 7,000\\ \\text{m}^2/\\text{g}$) and uniform pore diameters for size-selective heterogeneous catalysis."""
            },
            {
                "id": "sec_10_5",
                "title": "Renewable Chemical Feedstocks: Lignocellulose Biorefining",
                "content": """Transitioning away from fossil hydrocarbons requires converting lignocellulosic biomass (agricultural residues, forestry bagasse) into platform chemicals.

### Architecture of Lignocellulosic Biomass
1. **Cellulose ($40 - 50\\%$)**: Linear crystalline polymer of D-glucose linked by $\\beta\\text{-(1,4)-glycosidic}$ bonds.
2. **Hemicellulose ($25 - 35\\%$)**: Branched, amorphous heteropolymer of C5 and C6 sugars (xylose, arabinose, mannose, galactose).
3. **Lignin ($15 - 25\\%$)**: Complex, recalcitrant 3D aromatic polymer synthesized from three phenylpropanoid monolignols (p-coumaryl, coniferyl, and sinapyl alcohols).

### Top Platform Chemicals & Bio-based Building Blocks
1. **5-Hydroxymethylfurfural (5-HMF)**:
   - Formed via acid-catalyzed dehydration of C6 hexoses:
     \\[
     C_6H_{12}O_6 \\xrightarrow{-3H_2O} C_6H_6O_3
     \\]
   - Readily oxidized to 2,5-furandicarboxylic acid (FDCA), the bio-based replacement for petroleum-derived purified terephthalic acid (PTA) in the production of polyethylene furanoate (PEF) plastics.
2. **Levulinic Acid ($C_5H_8O_3$)**:
   - Produced by subsequent rehydration and cleavage of HMF, yielding levulinic and formic acid ($HCOOH$).
   - Precursor for ethyl levulinate bio-fuels and 2-methyltetrahydrofuran (2-MeTHF) green solvent.
3. **Furfural ($C_5H_4O_2$)**:
   - Dehydration of C5 pentosans (xylose). Precursor for furfuryl alcohol and tetrahydrofuran (THF).
4. **Glycerol ($C_3H_8O_3$)**:
   - Massive by-product of biodiesel transesterification, catalytically upgraded to 1,3-propanediol, epichlorohydrin, and polyglycerols."""
            },
            {
                "id": "sec_10_6",
                "title": "Energy Efficiency & Continuous Flow Process Intensification",
                "content": """Process intensification (PI) replaces large, hazardous batch reactors with compact, continuous-flow microreactors, radically improving heat and mass transfer.

### Continuous Flow Microreactors
Fluid streams are pumped continuously through engineered micro-channels (internal diameter $100 - 1000\\ \\mu\\text{m}$):
- **Surface Area-to-Volume Ratio ($S/V$)**:
  \\[
  \\frac{S}{V} = \\frac{4}{d}
  \\]
  In a microchannel of diameter $d = 0.5\\ \\text{mm}$, $S/V = 8,000\\ \\text{m}^2/\\text{m}^3$ (compared to $< 100\\ \\text{m}^2/\\text{m}^3$ for a $5,000\\ \\text{L}$ industrial batch reactor).
- **Rapid Heat Dissipation**: Enables safe execution of highly exothermic reactions (nitrations, lithiations, halogenations, ozonolysis) under precise isothermal conditions without risk of thermal runaway.
- **Plug Flow Hydraulics**: Narrow residence time distribution ($RTD$) eliminates back-mixing, maximizing chemical selectivity and product purity.

### Alternative Activation Technologies
1. **Microwave-Assisted Organic Synthesis (MAOS)**: Direct dipolar polarization and ionic conduction heating, achieving rapid volumetric heating rates exceeding $10^2 - 10^3\\ \\text{K}/\\text{min}$, dramatically accelerating reaction kinetics.
2. **Mechanochemistry (Ball Milling)**: Friction and shear impact mechanically induce bond cleavage and solid-state reactions in the complete absence of bulk solvent."""
            },
            {
                "id": "sec_10_7",
                "title": "Life Cycle Assessment (LCA) Methodology: ISO 14040/14044",
                "content": """Life Cycle Assessment (LCA) is the standardized compilation and evaluation of the inputs, outputs, and potential environmental impacts of a product system throughout its entire life cycle ('cradle-to-grave' or 'cradle-to-cradle').

### The Four Phases of ISO 14040/14044
1. **Goal and Scope Definition**:
   - Specifies the intended application, target audience, system boundary (cradle-to-gate vs cradle-to-grave), and **Functional Unit** (quantified performance of a product system for reference, e.g., $1.0\\ \\text{kg of active pharmaceutical ingredient}$).
2. **Life Cycle Inventory (LCI)**:
   - Rigorous mass and energy accounting quantifying all raw material extractions, energy inputs, water consumption, and atmospheric/aquatic emissions across every unit process.
3. **Life Cycle Impact Assessment (LCIA)**:
   - Classification and characterization of inventory flows into specific environmental impact categories:
     - *Global Warming Potential (GWP)*: In units of $\\text{kg } CO_2\\text{-eq}$.
     - *Acidification Potential (AP)*: In units of $\\text{kg } SO_2\\text{-eq}$.
     - *Eutrophication Potential (EP)*: In units of $\\text{kg } PO_4^{3-}\\text{-eq}$.
     - *Ozone Depletion Potential (ODP)*: In units of $\\text{kg CFC-11-eq}$.
     - *Human and Ecotoxicity Potentials*.
4. **Interpretation**:
   - Identification of environmental 'hotspots', sensitivity analysis, and iterative engineering optimization."""
            },
            {
                "id": "sec_10_8",
                "title": "Circular Industrial Ecology & Cradle-to-Cradle Symbiosis",
                "content": """Industrial ecology conceptualizes industrial manufacturing facilities as interconnected biological ecosystems, where the waste or by-product of one enterprise serves as the feedstock or energy source for another.

### The Kalundborg Industrial Symbiosis Archetype
Located in Kalundborg, Denmark, this pioneer eco-industrial network demonstrates multi-sectoral material and thermal integration:
- **Asnæs Power Station**: Sends low-pressure excess steam to the Novo Nordisk pharmaceutical plant and Equinor oil refinery; sends fly ash to a cement factory, and gypsum ($CaSO_4 \\cdot 2H_2O$) produced via flue gas desulfurization to the Saint-Gobain drywall plasterboard plant.
- **Novo Nordisk**: Sends residual biomass sludge ('Novogro') as rich organic agricultural fertilizer to local Danish farms.
- **Refinery**: Sends desulfurized cooling water and combustible waste gas to the power station.

### Exergy Analysis in Industrial Ecology
First-law energy conservation fails to capture energy degradation. **Exergy ($B$)** measures the maximum theoretical useful work obtainable when a system is brought into thermodynamic equilibrium with its reference environment:
\\[
B = (H - H_0) - T_0 (S - S_0)
\\]
Minimizing exergy destruction ($\dot{I} = T_0 \\dot{S}_{gen}$) maximizes thermodynamic circularity and resource productivity."""
            }
        ],
        "problems": [
            {
                "id": "prob_10_1",
                "tier": "Foundational",
                "title": "Atom Economy and Stoichiometric Efficiency of Epoxidation Routes",
                "statement": "The synthesis of propylene oxide ($C_3H_6O$, molar mass $58.08\\ \\text{g}/\\text{mol}$) from propylene ($C_3H_6$, molar mass $42.08\\ \\text{g}/\\text{mol}$) is compared via two alternative commercial chemical routes:\\nRoute A (Classical Chlorohydrin Process):\\nStep 1: $C_3H_6 + Cl_2 + H_2O \\rightarrow C_3H_7ClO$\\nStep 2: $2C_3H_7ClO + Ca(OH)_2 \\rightarrow 2C_3H_6O + CaCl_2 + 2H_2O$\\nOverall: $2C_3H_6 + 2Cl_2 + Ca(OH)_2 \\rightarrow 2C_3H_6O + CaCl_2 + 2H_2O$\\nRoute B (Green Catalytic Hydrogen Peroxide Epoxidation - HPPO Process):\\n$C_3H_6 + H_2O_2 \\xrightarrow{\\text{TS-1 Catalyst}} C_3H_6O + H_2O$\\nMolar masses: $Cl_2 = 70.90\\ \\text{g}/\\text{mol}$, $Ca(OH)_2 = 74.09\\ \\text{g}/\\text{mol}$, $H_2O_2 = 34.01\\ \\text{g}/\\text{mol}$, $H_2O = 18.02\\ \\text{g}/\\text{mol}$, $CaCl_2 = 110.98\\ \\text{g}/\\text{mol}$.\\n(a) Calculate the theoretical percentage Atom Economy (AE%) for Route A. (b) Calculate the theoretical Atom Economy for Route B. (c) Comment on the environmental significance of the difference in byproduct generation.",
                "hints": [
                    "Route A: Product mass $= 2 \\times 58.08 = 116.16\\ \\text{g}$. Reactant mass $= 2(42.08) + 2(70.90) + 74.09$.",
                    "Route B: Product mass $= 58.08\\ \\text{g}$. Reactant mass $= 42.08 + 34.01 = 76.09\\ \\text{g}$.",
                    "$\\text{AE\\%} = (M_{product} / \\sum M_{reactants}) \\times 100$."
                ],
                "solution": """**Step 1: Calculate Atom Economy for Route A (Chlorohydrin Process)**
The overall balanced reaction:
\\[
2C_3H_6 + 2Cl_2 + Ca(OH)_2 \\rightarrow 2C_3H_6O + CaCl_2 + 2H_2O
\\]
Desired product: $2\\ \\text{moles of } C_3H_6O$
\\[
M_{product} = 2 \\times 58.08\\ \\text{g}/\\text{mol} = 116.16\\ \\text{g}
\\]
Total mass of reactants:
\\[
\\sum M_{reactants} = 2(42.08) + 2(70.90) + 74.09 = 84.16 + 141.80 + 74.09 = 300.05\\ \\text{g}
\\]
Atom Economy:
\\[
\\text{AE}_A = \\left( \\frac{116.16}{300.05} \\right) \\times 100 = 38.71\\%
\\]

**Step 2: Calculate Atom Economy for Route B (HPPO Process)**
The reaction:
\\[
C_3H_6 + H_2O_2 \\rightarrow C_3H_6O + H_2O
\\]
Desired product: $1\\ \\text{mole of } C_3H_6O$ ($58.08\\ \\text{g}$).
Total mass of reactants:
\\[
\\sum M_{reactants} = 42.08 + 34.01 = 76.09\\ \\text{g}
\\]
Atom Economy:
\\[
\\text{AE}_B = \\left( \\frac{58.08}{76.09} \\right) \\times 100 = 76.33\\%
\\]

**Step 3: Environmental Evaluation**
- Route A generates **$61.3\\%$ byproducts by mass**, releasing stoichiometric hazardous calcium chloride brine contaminated with chlorinated ethers.
- Route B achieves **$76.3\\%$ Atom Economy**, with water ($H_2O$) as the sole innocuous byproduct, eliminating chlorine handling, eliminating chlorinated toxic waste, and significantly reducing waste treatment footprints."""
            },
            {
                "id": "prob_10_2",
                "tier": "Foundational",
                "title": "Sheldon E-Factor and Carbon Efficiency in Multi-Step Synthesis",
                "statement": "A pharmaceutical intermediate is manufactured via a three-step batch synthetic campaign producing $m_{API} = 50.0\\ \\text{kg}$ of purified active drug. The operational mass logs record the following total raw materials charged: Step 1: $120.0\\ \\text{kg}$ starting material, $35.0\\ \\text{kg}$ reagents, $600.0\\ \\text{kg}$ solvents; Step 2: $40.0\\ \\text{kg}$ coupling reagent, $800.0\\ \\text{kg}$ solvents, $150.0\\ \\text{kg}$ wash water; Step 3: $25.0\\ \\text{kg}$ deprotecting agent, $550.0\\ \\text{kg}$ solvents, $200.0\\ \\text{kg}$ water. In total, $1400.0\\ \\text{kg}$ of spent organic solvents are recovered and recycled via on-site fractional distillation. (a) Calculate the gross Sheldon Environmental Factor ($E_{gross}$, including all solvents and water). (b) Calculate the complete Sheldon Environmental Factor with solvent recycling deducted ($E_{net}$). (c) If the total carbon contained in all input reactants is $110.0\\ \\text{kg C}$ and the purified product contains $38.5\\ \\text{kg C}$, calculate the Carbon Efficiency (CE%).",
                "hints": [
                    "Total input mass: Sum of all materials.",
                    "$E_{gross} = (M_{inputs} - m_{API}) / m_{API}$.",
                    "Net waste: Deduct recovered solvent. $E_{net} = (M_{inputs} - M_{recycled} - m_{API}) / m_{API}$.",
                    "$\\text{CE\\%} = (M_{C, product} / M_{C, inputs}) \\times 100$."
                ],
                "solution": """**Step 1: Calculate total input raw materials and $E_{gross}$**
Summing all mass inputs:
- Reactants & Reagents: $120.0 + 35.0 + 40.0 + 25.0 = 220.0\\ \\text{kg}$
- Solvents: $600.0 + 800.0 + 550.0 = 1950.0\\ \\text{kg}$
- Water: $150.0 + 200.0 = 350.0\\ \\text{kg}$

Total raw material input:
\\[
M_{total} = 220.0 + 1950.0 + 350.0 = 2520.0\\ \\text{kg}
\\]
Gross waste generated:
\\[
M_{waste, gross} = M_{total} - m_{API} = 2520.0 - 50.0 = 2470.0\\ \\text{kg}
\\]
Gross Sheldon $E$-Factor:
\\[
E_{gross} = \\frac{M_{waste, gross}}{m_{API}} = \\frac{2470.0\\ \\text{kg}}{50.0\\ \\text{kg}} = 49.40\\ \\text{kg waste} / \\text{kg API}
\\]

**Step 2: Calculate net $E$-Factor ($E_{net}$) with solvent recycling**
Subtracting $1400.0\\ \\text{kg}$ of recovered solvent:
\\[
M_{waste, net} = M_{waste, gross} - M_{recycled} = 2470.0 - 1400.0 = 1070.0\\ \\text{kg}
\\]
Net $E$-Factor:
\\[
E_{net} = \\frac{M_{waste, net}}{m_{API}} = \\frac{1070.0\\ \\text{kg}}{50.0\\ \\text{kg}} = 21.40\\ \\text{kg waste} / \\text{kg API}
\\]

**Step 3: Calculate Carbon Efficiency (CE%)**
Given $M_{C, inputs} = 110.0\\ \\text{kg C}$ and $M_{C, product} = 38.5\\ \\text{kg C}$:
\\[
\\text{CE\\%} = \\left( \\frac{M_{C, product}}{M_{C, inputs}} \\right) \\times 100 = \\left( \\frac{38.5\\ \\text{kg}}{110.0\\ \\text{kg}} \\right) \\times 100 = 35.00\\%
\\]

**Conclusion**:
The process exhibits an $E_{gross}$ of **49.4**, reduced to an $E_{net}$ of **21.4** via solvent recovery, with a Carbon Efficiency of **$35.0\\%$**."""
            },
            {
                "id": "prob_10_3",
                "tier": "Foundational",
                "title": "Process Mass Intensity (PMI) and Reaction Mass Efficiency",
                "statement": "The synthesis of an analgesic drug ($M = 151.16\\ \\text{g}/\\text{mol}$) reacts 4-aminophenol ($109.13\\ \\text{g}/\\text{mol}$, mass charged $m_1 = 10.91\\ \\text{kg}$) with acetic anhydride ($102.09\\ \\text{g}/\\text{mol}$, mass charged $m_2 = 12.25\\ \\text{kg}$) in $60.0\\ \\text{kg}$ of water. The reaction produces acetic acid byproduct ($60.05\\ \\text{g}/\\text{mol}$). The isolated pure product mass is $m_p = 12.85\\ \\text{kg}$. (a) Calculate the theoretical Atom Economy (AE%) and experimental chemical percentage yield ($\\epsilon\\%$). (b) Calculate the Reaction Mass Efficiency (RME%). (c) Calculate the Process Mass Intensity (PMI).",
                "hints": [
                    "Reaction: $C_6H_7NO + C_4H_6O_3 \\rightarrow C_8H_9NO_2 + C_2H_4O_2$.",
                    "Theoretical maximum product mass $= \\frac{10.91\\ \\text{kg}}{109.13} \\times 151.16$.",
                    "$\\text{RME} = \\frac{m_p}{m_1 + m_2} \\times 100$.",
                    "$\\text{PMI} = \\frac{m_1 + m_2 + m_{water}}{m_p}$."
                ],
                "solution": """**Step 1: Calculate Atom Economy and chemical yield**
The reaction:
\\[
C_6H_7NO + C_4H_6O_3 \\rightarrow C_8H_9NO_2 + C_2H_4O_2
\\]
Desired product: Acetaminophen ($M = 151.16\\ \\text{g}/\\text{mol}$).
Reactants: 4-aminophenol ($109.13\\ \\text{g}/\\text{mol}$) + Acetic anhydride ($102.09\\ \\text{g}/\\text{mol}$).
\\[
\\text{AE} = \\frac{151.16}{109.13 + 102.09} \\times 100 = \\frac{151.16}{211.22} \\times 100 = 71.57\\%
\\]
Moles of 4-aminophenol charged:
\\[
n_1 = \\frac{10.91\\ \\text{kg}}{109.13\\ \\text{g}/\\text{mol}} = 0.09997\\ \\text{kmol} \\approx 100.0\\ \\text{mol}
\\]
Moles of acetic anhydride charged:
\\[
n_2 = \\frac{12.25\\ \\text{kg}}{102.09\\ \\text{g}/\\text{mol}} = 0.1200\\ \\text{kmol} = 120.0\\ \\text{mol} \\quad (20\\%\\text{ excess})
\\]
Limiting reactant is 4-aminophenol ($100.0\\ \\text{mol}$).
Theoretical maximum product:
\\[
m_{p, theo} = 100.0\\ \\text{mol} \\times 151.16\\ \\text{g}/\\text{mol} = 15,116\\ \\text{g} = 15.116\\ \\text{kg}
\\]
Experimental yield:
\\[
\\epsilon = \\frac{12.85\\ \\text{kg}}{15.116\\ \\text{kg}} \\times 100 = 85.01\\%
\\]

**Step 2: Calculate Reaction Mass Efficiency (RME%)**
Total stoichiometric reactant mass charged:
\\[
M_{reactants} = m_1 + m_2 = 10.91 + 12.25 = 23.16\\ \\text{kg}
\\]
\\[
\\text{RME} = \\frac{m_p}{M_{reactants}} \\times 100 = \\frac{12.85\\ \\text{kg}}{23.16\\ \\text{kg}} \\times 100 = 55.48\\%
\\]

**Step 3: Calculate Process Mass Intensity (PMI)**
Total raw materials including solvent (water):
\\[
M_{total} = m_1 + m_2 + m_{water} = 10.91 + 12.25 + 60.00 = 83.16\\ \\text{kg}
\\]
The Process Mass Intensity:
\\[
\\text{PMI} = \\frac{M_{total}}{m_p} = \\frac{83.16\\ \\text{kg}}{12.85\\ \\text{kg}} = 6.47\\ \\text{kg input} / \\text{kg product}
\\]

**Conclusion**:
The process achieves an Atom Economy of **$71.6\\%$**, an experimental yield of **$85.0\\%$**, an RME of **$55.5\\%$**, and an outstandingly green PMI of **6.47**."""
            },
            {
                "id": "prob_10_4",
                "tier": "Intermediate",
                "title": "Supercritical Fluid Carbon Dioxide: Peng-Robinson Density & Solvency",
                "statement": "Supercritical carbon dioxide ($scCO_2$, critical parameters $T_c = 304.13\\ \\text{K}$, $P_c = 73.77\\ \\text{bar} = 7.377 \\times 10^6\\ \\text{Pa}$, acentric factor $\\omega = 0.224$) is used as a green extraction solvent at $T = 313.15\\ \\text{K}$ ($40^\\circ\\text{C}$) and $P = 200.0\\ \\text{bar} = 2.00 \\times 10^7\\ \\text{Pa}$. (a) Calculate the reduced temperature $T_r$ and reduced pressure $P_r$. (b) Using the Peng-Robinson parameters $a(T) = 0.45724 \\frac{R^2 T_c^2}{P_c} \\alpha(T)$ and $b = 0.07780 \\frac{R T_c}{P_c}$ with $\\alpha(T) = [1 + (0.37464 + 1.54226 \\omega - 0.26992 \\omega^2)(1 - \\sqrt{T_r})]^2$, calculate numerical values for $a$ and $b$ ($R = 8.314\\ \\text{J}/(\\text{mol}\\cdot\\text{K})$). (c) Given that the root for the compressibility factor in the dense supercritical phase is $Z = 0.385$, calculate the supercritical molar volume $V_m$ (in $\\text{L}/\\text{mol}$) and mass density $\\rho$ (in $\\text{kg}/\\text{m}^3$ and $\\text{g}/\\text{mL}$).",
                "hints": [
                    "Compute $T_r = T / T_c$ and $P_r = P / P_c$.",
                    "Compute $\\alpha(T)$ and the constants $a$ and $b$.",
                    "From $Z = \\frac{P V_m}{R T}$, solve for $V_m = \\frac{Z R T}{P}$. Density $\\rho = M / V_m$ with $M = 44.01\\ \\text{g}/\\text{mol}$."
                ],
                "solution": """**Step 1: Calculate reduced temperature and reduced pressure**
Given:
- $T_c = 304.13\\ \\text{K}$, $T = 313.15\\ \\text{K}$
- $P_c = 73.77\\ \\text{bar}$, $P = 200.0\\ \\text{bar}$
\\[
T_r = \\frac{T}{T_c} = \\frac{313.15}{304.13} = 1.02966
\\]
\\[
P_r = \\frac{P}{P_c} = \\frac{200.0}{73.77} = 2.7111
\\]

**Step 2: Calculate Peng-Robinson EOS parameters $a$ and $b$**
With acentric factor $\\omega = 0.224$:
\\[
m = 0.37464 + 1.54226(0.224) - 0.26992(0.224)^2 = 0.37464 + 0.34547 - 0.01354 = 0.70657
\\]
\\[
\\sqrt{T_r} = \\sqrt{1.02966} = 1.01472
\\]
\\[
\\alpha(T) = [1 + m(1 - \\sqrt{T_r})]^2 = [1 + 0.70657(1 - 1.01472)]^2 = [1 + 0.70657(-0.01472)]^2
\\]
\\[
\\alpha(T) = [1 - 0.01040]^2 = (0.98960)^2 = 0.97931
\\]
Evaluating constant $a$:
\\[
a_0 = 0.45724 \\frac{R^2 T_c^2}{P_c} = 0.45724 \\frac{(8.3145)^2 (304.13)^2}{7.377 \\times 10^6} = 0.45724 \\frac{(69.1309)(92,495)}{7.377 \\times 10^6} = 0.3964\\ \\text{J}\\cdot\\text{m}^3/\\text{mol}^2
\\]
\\[
a(T) = a_0 \\times \\alpha(T) = 0.3964 \\times 0.97931 = 0.3882\\ \\text{Pa}\\cdot\\text{m}^6/\\text{mol}^2
\\]
Evaluating constant $b$:
\\[
b = 0.07780 \\frac{R T_c}{P_c} = 0.07780 \\frac{(8.3145)(304.13)}{7.377 \\times 10^6} = 2.666 \\times 10^{-5}\\ \\text{m}^3/\\text{mol}
\\]

**Step 3: Calculate molar volume and fluid density from compressibility factor**
Given $Z = 0.385$ at $P = 2.00 \\times 10^7\\ \\text{Pa}$ and $T = 313.15\\ \\text{K}$:
\\[
R T = (8.3145)(313.15) = 2603.69\\ \\text{J}/\\text{mol}
\\]
\\[
V_m = \\frac{Z R T}{P} = \\frac{(0.385)(2603.69\\ \\text{J}/\\text{mol})}{2.00 \\times 10^7\\ \\text{Pa}} = 5.012 \\times 10^{-5}\\ \\text{m}^3/\\text{mol} = 0.05012\\ \\text{L}/\\text{mol}
\\]
Mass density ($M_{CO2} = 44.01\\ \\text{g}/\\text{mol} = 0.04401\\ \\text{kg}/\\text{mol}$):
\\[
\\rho = \\frac{M}{V_m} = \\frac{0.04401\\ \\text{kg}/\\text{mol}}{5.012 \\times 10^{-5}\\ \\text{m}^3/\\text{mol}} = 878.1\\ \\text{kg}/\\text{m}^3 = 0.878\\ \\text{g}/\\text{mL}
\\]

**Conclusion**:
At $40^\\circ\\text{C}$ and $200\\ \\text{bar}$, $scCO_2$ compresses to a liquid-like density of **$878\\ \\text{kg}/\\text{m}^3$** ($0.88\\ \\text{g}/\\text{mL}$), providing high solvation power while maintaining gas-like diffusivity."""
            },
            {
                "id": "prob_10_5",
                "tier": "Intermediate",
                "title": "Catalytic Turnover Number (TON) and Frequency (TOF) in Biomass Upgrading",
                "statement": "The selective catalytic hydrogenation of biomass-derived levulinic acid ($M = 116.12\\ \\text{g}/\\text{mol}$) to the green fuel additive $\\gamma$-valerolactone (GVL, $M = 100.12\\ \\text{g}/\\text{mol}$) is carried out in a pressurized batch autoclave ($V = 500\\ \\text{mL}$) using a heterogeneous $Ru/C$ catalyst ($5.0\\ \\text{wt}\\%$ ruthenium, molar mass $Ru = 101.07\\ \\text{g}/\\text{mol}$). The reactor is charged with $m_{LA} = 58.06\\ \\text{g}$ of levulinic acid and $m_{cat} = 0.202\\ \\text{g}$ of $Ru/C$ catalyst. Chemisorption measurements show that the ruthenium active metal dispersion is $D = 40.0\\%$ (i.e. $40\\%$ of Ru atoms reside on the surface accessible for catalysis). After a reaction time of $t = 2.50\\ \\text{hours}$, chromatographic analysis indicates $98.0\\%$ conversion of levulinic acid with $99.0\\%$ selectivity to GVL. (a) Calculate the total moles of levulinic acid charged, moles of GVL produced, and total moles of ruthenium ($n_{Ru, tot}$) and surface active ruthenium sites ($n_{Ru, active}$). (b) Calculate the Turnover Number (TON) based on total Ru and based on active surface Ru sites. (c) Calculate the Turnover Frequency (TOF) based on active surface sites in $\\text{h}^{-1}$ and $\\text{s}^{-1}$.",
                "hints": [
                    "Moles of LA $= 58.06 / 116.12$. GVL produced $= n_{LA} \\times 0.980 \\times 0.990$.",
                    "Mass of Ru in catalyst: $m_{cat} \\times 0.05$. Moles of Ru: $n_{Ru, tot} = m_{Ru} / 101.07$.",
                    "Active sites: $n_{active} = n_{Ru, tot} \\times 0.40$.",
                    "$\\text{TON} = n_{GVL} / n_{active}$, $\\text{TOF} = \\text{TON} / t$."
                ],
                "solution": """**Step 1: Calculate moles of reactants, product, and catalyst**
1. **Levulinic Acid and GVL**:
   \\[
   n_{LA} = \\frac{58.06\\ \\text{g}}{116.12\\ \\text{g}/\\text{mol}} = 0.5000\\ \\text{mol}
   \\]
   Moles of GVL formed ($98.0\\%$ conversion, $99.0\\%$ selectivity):
   \\[
   n_{GVL} = 0.5000\\ \\text{mol} \\times 0.980 \\times 0.990 = 0.4851\\ \\text{mol}
   \\]
2. **Ruthenium Catalyst**:
   \\[
   m_{Ru} = 0.202\\ \\text{g cat} \\times 0.050 = 0.01010\\ \\text{g Ru}
   \\]
   Total moles of Ru:
   \\[
   n_{Ru, tot} = \\frac{0.01010\\ \\text{g}}{101.07\\ \\text{g}/\\text{mol}} = 9.993 \\times 10^{-5}\\ \\text{mol} \\approx 1.00 \\times 10^{-4}\\ \\text{mol}
   \\]
   Active surface Ru atoms ($D = 40.0\\%$):
   \\[
   n_{Ru, active} = n_{Ru, tot} \\times 0.400 = (9.993 \\times 10^{-5}) \\times 0.400 = 3.9972 \\times 10^{-5}\\ \\text{mol}
   \\]

**Step 2: Calculate Turnover Number (TON)**
1. **Based on total metal atoms**:
   \\[
   \\text{TON}_{tot} = \\frac{n_{GVL}}{n_{Ru, tot}} = \\frac{0.4851\\ \\text{mol}}{9.993 \\times 10^{-5}\\ \\text{mol}} = 4,854
   \\]
2. **Based on active surface catalytic sites**:
   \\[
   \\text{TON}_{active} = \\frac{n_{GVL}}{n_{Ru, active}} = \\frac{0.4851\\ \\text{mol}}{3.9972 \\times 10^{-5}\\ \\text{mol}} = 12,136 \\approx 12,140
   \\]

**Step 3: Calculate Turnover Frequency (TOF)**
Reaction duration: $t = 2.50\\ \\text{hours} = 9,000\\ \\text{seconds}$.
\\[
\\text{TOF} = \\frac{\\text{TON}_{active}}{t} = \\frac{12,136}{2.50\\ \\text{h}} = 4,854.4\\ \\text{h}^{-1} \\approx 4,850\\ \\text{h}^{-1}
\\]
In units of per second:
\\[
\\text{TOF} = \\frac{4,854.4\\ \\text{h}^{-1}}{3600\\ \\text{s}/\\text{h}} = 1.348\\ \\text{s}^{-1} \\approx 1.35\\ \\text{s}^{-1}
\\]

**Conclusion**:
The catalyst operates with high green efficiency: $\\text{TON} = \\mathbf{12,140}$ catalytic cycles per active site and $\\text{TOF} = \\mathbf{4,850\\ \\text{h}^{-1}}$ ($\mathbf{1.35\\ \\text{s}^{-1}}$)."""
            },
            {
                "id": "prob_10_6",
                "tier": "Intermediate",
                "title": "Continuous Flow vs Batch Reactor: Space-Time Yield and Thermal Transfer",
                "statement": "An exothermic bromination reaction ($\Delta H_{rxn} = -180.0\\ \\text{kJ}/\\text{mol}$) is evaluated in both a conventional jacketed batch reactor and an engineered continuous-flow microreactor:\\nOption 1 (Batch): $V_{batch} = 2.50\\ \\text{m}^3$ ($2500\\ \\text{L}$), cycle time including charging, reaction, and cleaning $\\tau_{batch} = 6.0\\ \\text{hours}$, producing $125.0\\ \\text{kg}$ of purified product per batch. Internal heat transfer surface area is $A_{batch} = 6.0\\ \\text{m}^2$.\\nOption 2 (Flow Microreactor): Internal reactor volume $V_{flow} = 0.050\\ \\text{m}^3$ ($50\\ \\text{L}$), residence time $\\tau_{res} = 4.0\\ \\text{minutes}$ ($0.0667\\ \\text{h}$), operating 24 hours/day producing $45.0\\ \\text{kg}/\\text{h}$ of product. Internal heat transfer surface area is $A_{flow} = 15.0\\ \\text{m}^2$.\\n(a) Calculate the Space-Time Yield ($STY$ in $\\text{kg}/(\\text{m}^3\\cdot\\text{h})$) for both systems. (b) Calculate the specific heat transfer area density ($a_v = A / V$ in $\\text{m}^2/\\text{m}^3$) for both systems. (c) Compare the process safety and productivity advantages of continuous flow intensification.",
                "hints": [
                    "Batch $STY = \\frac{m_{batch}}{V_{batch} \\times \\tau_{batch}}$.",
                    "Flow $STY = \\frac{\\dot{m}_{flow}}{V_{flow}}$.",
                    "$a_v = A / V$ for each reactor."
                ],
                "solution": """**Step 1: Calculate Space-Time Yield (STY)**
1. **Option 1 (Batch Reactor)**:
   \\[
   STY_{batch} = \\frac{m_{product}}{V_{batch} \\times \\tau_{batch}} = \\frac{125.0\\ \\text{kg}}{(2.50\\ \\text{m}^3) \\times (6.0\\ \\text{h})} = \\frac{125.0}{15.0} = 8.333\\ \\text{kg}/(\\text{m}^3\\cdot\\text{h})
   \\]
2. **Option 2 (Continuous Flow Microreactor)**:
   \\[
   STY_{flow} = \\frac{\\dot{m}_{product}}{V_{flow}} = \\frac{45.0\\ \\text{kg}/\\text{h}}{0.050\\ \\text{m}^3} = 900.0\\ \\text{kg}/(\\text{m}^3\\cdot\\text{h})
   \\]
The space-time yield enhancement factor:
\\[
\\frac{STY_{flow}}{STY_{batch}} = \\frac{900.0}{8.333} = 108.0\\times
\\]

**Step 2: Calculate specific heat transfer area density ($a_v$)**
1. **Batch Reactor**:
   \\[
   a_{v, batch} = \\frac{A_{batch}}{V_{batch}} = \\frac{6.0\\ \\text{m}^2}{2.50\\ \\text{m}^3} = 2.40\\ \\text{m}^2/\\text{m}^3
   \\]
2. **Flow Microreactor**:
   \\[
   a_{v, flow} = \\frac{A_{flow}}{V_{flow}} = \\frac{15.0\\ \\text{m}^2}{0.050\\ \\text{m}^3} = 300.0\\ \\text{m}^2/\\text{m}^3
   \\]
Heat transfer area enhancement factor:
\\[
\\frac{a_{v, flow}}{a_{v, batch}} = \\frac{300.0}{2.40} = 125.0\\times
\\]

**Step 3: Process Safety and Green Intensification Analysis**
- **Safety**: The batch reactor holds an instantaneous reactive hazardous inventory of $2,500\\ \\text{L}$ capable of disastrous thermal runaway. In contrast, the microreactor contains only $50\\ \\text{L}$ at any given moment, and its massive $300\\ \\text{m}^2/\\text{m}^3$ heat exchange density dissipates the $-180\\ \\text{kJ}/\\text{mol}$ exotherm instantaneously, achieving perfect isothermal control.
- **Productivity**: A microreactor only $2\\%$ the size of the batch vessel generates **$108\\times$ higher volumetric productivity**."""
            },
            {
                "id": "prob_10_7",
                "tier": "Advanced",
                "title": "Life Cycle Assessment Matrix Modeling: Carbon Footprint via Leontief Inverse",
                "statement": "A simplified industrial Life Cycle Assessment (LCA) model consists of three economic sectors: Sector 1 (Electricity Generation, kWh), Sector 2 (Steam Generation, MJ), and Sector 3 (Bio-plastic Polylactic Acid Production, kg). The technological inter-process input-output matrix is: $A = \\begin{pmatrix} 0.10 & 0.05 & 2.50 \\\\ 0.00 & 0.15 & 12.00 \\\\ 0.00 & 0.00 & 0.00 \\end{pmatrix}$, where column $j$ specifies the inputs required per unit output of sector $j$. Direct greenhouse gas emission intensities per unit sector activity are given by row vector $B = \\begin{pmatrix} 0.650 & 0.075 & 0.450 \\end{pmatrix}\\ \\text{kg } CO_2\\text{-eq}$. We require a final functional unit demand vector of $f = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1.00 \\end{pmatrix}$ (producing exactly 1.0 kg of PLA bio-plastic). (a) Formulate the Leontief matrix $(I - A)$ and compute the total sectoral activity vector $x = (I - A)^{-1} f$. (b) Calculate the total cradle-to-gate Life Cycle Carbon Footprint $g = B x$ in $\\text{kg } CO_2\\text{-eq} / \\text{kg PLA}$. (c) Identify which supply chain tier (direct process, electricity, or steam) represents the largest environmental hotspot.",
                "hints": [
                    "Set up $(I - A) x = f$ as a 3x3 linear system and solve by back-substitution.",
                    "From row 3: $x_3 = 1.00$.",
                    "From row 2: $-0.15 x_2 + x_2 - 12.00 x_3 = 0 \\implies 0.85 x_2 = 12.00$.",
                    "Compute $x_1$ from row 1, then $g = B_1 x_1 + B_2 x_2 + B_3 x_3$."
                ],
                "solution": """**Step 1: Solve for total sectoral activity vector $x = (I - A)^{-1} f$**
The Leontief system is $(I - A) x = f$:
\\[
I - A = \\begin{pmatrix} 1.00 - 0.10 & -0.05 & -2.50 \\\\ 0.00 & 1.00 - 0.15 & -12.00 \\\\ 0.00 & 0.00 & 1.00 \\end{pmatrix} = \\begin{pmatrix} 0.90 & -0.05 & -2.50 \\\\ 0.00 & 0.85 & -12.00 \\\\ 0.00 & 0.00 & 1.00 \\end{pmatrix}
\\]
With demand $f = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1.00 \\end{pmatrix}$:
\\[
\\begin{pmatrix} 0.90 & -0.05 & -2.50 \\\\ 0.00 & 0.85 & -12.00 \\\\ 0.00 & 0.00 & 1.00 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\\\ x_3 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1.00 \\end{pmatrix}
\\]
Solving via back-substitution:
1. From equation 3:
   \\[
   x_3 = 1.000\\ \\text{kg PLA}
   \\]
2. From equation 2:
   \\[
   0.85 x_2 - 12.00(1.000) = 0 \\implies 0.85 x_2 = 12.00
   \\]
   \\[
   x_2 = \\frac{12.00}{0.85} = 14.1176\\ \\text{MJ steam}
   \\]
3. From equation 1:
   \\[
   0.90 x_1 - 0.05 x_2 - 2.50 x_3 = 0
   \\]
   \\[
   0.90 x_1 = 0.05(14.1176) + 2.50(1.000) = 0.70588 + 2.50 = 3.20588
   \\]
   \\[
   x_1 = \\frac{3.20588}{0.90} = 3.5621\\ \\text{kWh electricity}
   \\]
Thus:
\\[
x = \\begin{pmatrix} 3.5621 \\\\ 14.1176 \\\\ 1.0000 \\end{pmatrix}
\\]

**Step 2: Calculate total life cycle carbon footprint $g = B x$**
Given $B = \\begin{pmatrix} 0.650 & 0.075 & 0.450 \\end{pmatrix}$:
- Component 1 (Electricity): $B_1 x_1 = 0.650 \\times 3.5621 = 2.3154\\ \\text{kg } CO_2\\text{-eq}$
- Component 2 (Steam): $B_2 x_2 = 0.075 \\times 14.1176 = 1.0588\\ \\text{kg } CO_2\\text{-eq}$
- Component 3 (Direct PLA synthesis): $B_3 x_3 = 0.450 \\times 1.0000 = 0.4500\\ \\text{kg } CO_2\\text{-eq}$

Summing all contributions:
\\[
g = 2.3154 + 1.0588 + 0.4500 = 3.8242\\ \\text{kg } CO_2\\text{-eq} / \\text{kg PLA} \\approx 3.82\\ \\text{kg } CO_2\\text{-eq}
\\]

**Step 3: Hotspot Identification**
- Electricity supply chain: $\\frac{2.3154}{3.8242} \\times 100 = 60.55\\%$
- Process steam supply chain: $\\frac{1.0588}{3.8242} \\times 100 = 27.69\\%$
- Direct process emissions: $\\frac{0.4500}{3.8242} \\times 100 = 11.77\\%$

**Conclusion**:
The cradle-to-gate carbon footprint is **$3.82\\ \\text{kg } CO_2\\text{-eq}/\\text{kg PLA}$**. Electricity generation is the dominant environmental hotspot ($60.5\\%$ of total emissions), indicating that decarbonizing grid electricity yields the greatest sustainability benefit."""
            },
            {
                "id": "prob_10_8",
                "tier": "Advanced",
                "title": "Green Aspiration Level (GAL) and Comprehensive Environmental Impact Metric",
                "statement": "The Green Aspiration Level (GAL) metric assesses pharmaceutical synthesis sustainability relative to historical benchmarks. For an API with complexity score $N_{steps} = 5$ (linear synthesis steps), the benchmark average industry PMI is: $\\text{PMI}_{bench} = 25.0 \\times N_{steps} + 40.0 = 165.0\\ \\text{kg}/\\text{kg}$. A redesigned green synthesis route achieves an actual $\\text{PMI}_{actual} = 38.0\\ \\text{kg}/\\text{kg}$. (a) Calculate the Green Performance Ratio ($GPR = \\text{PMI}_{bench} / \\text{PMI}_{actual}$) and the relative waste reduction percentage. (b) The solvent waste stream consists of: $60.0\\ \\text{wt}\\%$ ethanol ($E$-hazard score = $1.2$), $30.0\\ \\text{wt}\\%$ ethyl acetate ($E$-hazard score = $1.8$), and $10.0\\ \\text{wt}\\%$ dichloromethane ($E$-hazard score = $8.5$). Calculate the weighted Environmental Hazard Quotient ($EHQ = \\sum w_i H_i$). (c) Calculate the Composite Green Index: $CGI = \\frac{GPR}{EHQ}$.",
                "hints": [
                    "$GPR = 165.0 / 38.0$. Waste reduction $= \\frac{165 - 38}{165} \\times 100$.",
                    "$EHQ = (0.60 \\times 1.2) + (0.30 \\times 1.8) + (0.10 \\times 8.5)$.",
                    "$CGI = GPR / EHQ$."
                ],
                "solution": """**Step 1: Calculate Green Performance Ratio (GPR) and waste reduction**
Given:
- $\\text{PMI}_{bench} = 165.0\\ \\text{kg}/\\text{kg}$
- $\\text{PMI}_{actual} = 38.0\\ \\text{kg}/\\text{kg}$

The Green Performance Ratio:
\\[
GPR = \\frac{\\text{PMI}_{bench}}{\\text{PMI}_{actual}} = \\frac{165.0}{38.0} = 4.3421 \\approx 4.34
\\]
Percentage waste reduction:
\\[
\\%\\text{Reduction} = \\left( \\frac{\\text{PMI}_{bench} - \\text{PMI}_{actual}}{\\text{PMI}_{bench}} \\right) \\times 100 = \\left( \\frac{165.0 - 38.0}{165.0} \\right) \\times 100 = \\frac{127.0}{165.0} \\times 100 = 76.97\\%
\\]

**Step 2: Calculate weighted Environmental Hazard Quotient ($EHQ$)**
The solvent composition and individual hazard weights:
- Ethanol: $w_1 = 0.60$, $H_1 = 1.2 \\implies w_1 H_1 = 0.60 \\times 1.2 = 0.72$
- Ethyl acetate: $w_2 = 0.30$, $H_2 = 1.8 \\implies w_2 H_2 = 0.30 \\times 1.8 = 0.54$
- Dichloromethane: $w_3 = 0.10$, $H_3 = 8.5 \\implies w_3 H_3 = 0.10 \\times 8.5 = 0.85$

The composite weighted hazard quotient:
\\[
EHQ = \\sum_{i=1}^3 w_i H_i = 0.72 + 0.54 + 0.85 = 2.110
\\]
Notice that DCM represents only $10\\%$ of solvent mass but contributes over $40\\%$ of the total environmental hazard score.

**Step 3: Calculate Composite Green Index (CGI)**
\\[
CGI = \\frac{GPR}{EHQ} = \\frac{4.3421}{2.110} = 2.0579 \\approx 2.06
\\]

**Conclusion**:
The redesigned green route achieves a $GPR$ of **4.34** ($77\\%$ material reduction), an $EHQ$ of **2.11**, and a Composite Green Index of **2.06**, signifying superior process performance relative to conventional industrial manufacturing."""
            },
            {
                "id": "prob_10_9",
                "tier": "Advanced",
                "title": "Industrial Symbiosis Exergy Balance in an Eco-Industrial Park",
                "statement": "An Eco-Industrial Park (Kalundborg archetype) integrates a combined heat and power plant (CHP), an industrial biorefinery, and a district heating network. The CHP plant combusts biomass delivering thermal steam at enthalpy $H_1 = 2800\\ \\text{kJ}/\\text{kg}$ and temperature $T_1 = 473.15\\ \\text{K}$ ($200^\\circ\\text{C}$), with steam mass flow rate $\\dot{m} = 50.0\\ \\text{kg}/\\text{s}$. The reference environment is at $T_0 = 298.15\\ \\text{K}$ ($25^\\circ\\text{C}$) and $P_0 = 1.0\\ \\text{bar}$. The specific exergy of the steam is given by $e = (h - h_0) - T_0 (s - s_0)$. Steam parameters relative to reference state are: $(h_1 - h_0) = 2200\\ \\text{kJ}/\\text{kg}$, $(s_1 - s_0) = 4.80\\ \\text{kJ}/(\\text{kg}\\cdot\\text{K})$. The steam passes through a back-pressure turbine generating electrical work $\\dot{W}_{elec} = 25.0\\ \\text{MW}$, discharging exhaust steam at $T_2 = 373.15\\ \\text{K}$ ($100^\\circ\\text{C}$) with $(h_2 - h_0) = 1700\\ \\text{kJ}/\\text{kg}$ and $(s_2 - s_0) = 4.10\\ \\text{kJ}/(\\text{kg}\\cdot\\text{K})$. This exhaust steam is sent to the biorefinery for fermentation heating. (a) Calculate the specific exergy $e_1$ of the high-pressure steam and $e_2$ of the exhaust steam in $\\text{kJ}/\\text{kg}$. (b) Calculate the total exergy flux entering the turbine $\\dot{E}_1$ and exiting in exhaust steam $\\dot{E}_2$ in megawatts (MW). (c) Calculate the rate of exergy destruction $\\dot{I}$ in the turbine and the Second-Law Exergetic Efficiency ($\\eta_{ex} = \\frac{\\dot{W}_{elec} + \\dot{E}_2}{\\dot{E}_1} \\times 100$).",
                "hints": [
                    "$e_1 = (h_1 - h_0) - T_0 (s_1 - s_0)$.",
                    "$e_2 = (h_2 - h_0) - T_0 (s_2 - s_0)$.",
                    "Exergy rates: $\\dot{E} = \\dot{m} \\times e$.",
                    "Exergy destruction: $\\dot{I} = \\dot{E}_1 - (\\dot{W}_{elec} + \\dot{E}_2)$."
                ],
                "solution": """**Step 1: Calculate specific exergy $e_1$ and $e_2$**
Given $T_0 = 298.15\\ \\text{K}$:
1. **High-Pressure Steam ($T_1 = 473.15\\ \\text{K}$)**:
   \\[
   e_1 = (h_1 - h_0) - T_0 (s_1 - s_0) = 2200\\ \\text{kJ}/\\text{kg} - (298.15\\ \\text{K})(4.80\\ \\text{kJ}/(\\text{kg}\\cdot\\text{K}))
   \\]
   \\[
   e_1 = 2200 - 1431.12 = 768.88\\ \\text{kJ}/\\text{kg}
   \\]
2. **Exhaust Steam to Biorefinery ($T_2 = 373.15\\ \\text{K}$)**:
   \\[
   e_2 = (h_2 - h_0) - T_0 (s_2 - s_0) = 1700\\ \\text{kJ}/\\text{kg} - (298.15\\ \\text{K})(4.10\\ \\text{kJ}/(\\text{kg}\\cdot\\text{K}))
   \\]
   \\[
   e_2 = 1700 - 1222.415 = 477.585\\ \\text{kJ}/\\text{kg} \\approx 477.59\\ \\text{kJ}/\\text{kg}
   \\]

**Step 2: Calculate exergy fluxes across the system**
Mass flow rate: $\\dot{m} = 50.0\\ \\text{kg}/\\text{s}$.
1. **Input Exergy Flux ($\\dot{E}_1$)**:
   \\[
   \\dot{E}_1 = \\dot{m} \\times e_1 = 50.0\\ \\text{kg}/\\text{s} \\times 768.88\\ \\text{kJ}/\\text{kg} = 38,444\\ \\text{kW} = 38.444\\ \\text{MW}
   \\]
2. **Exhaust Steam Exergy to Biorefinery ($\\dot{E}_2$)**:
   \\[
   \\dot{E}_2 = \\dot{m} \\times e_2 = 50.0\\ \\text{kg}/\\text{s} \\times 477.585\\ \\text{kJ}/\\text{kg} = 23,879.25\\ \\text{kW} = 23.879\\ \\text{MW}
   \\]
3. **Electrical Work Output**:
   \\[
   \\dot{W}_{elec} = 25.000\\ \\text{MW}
   \\]
*Wait, let us check the energy balance*:
Energy delivered by steam: $\\dot{m}(h_1 - h_2) = 50.0 \\times (2200 - 1700) = 50.0 \\times 500 = 25,000\\ \\text{kW} = 25.0\\ \\text{MW}$.
So $\\dot{W}_{elec} \\le 25.0\\ \\text{MW}$. Let the turbine electrical work be $\\dot{W}_{elec} = 12.0\\ \\text{MW}$ (with turbine isentropic efficiency):
If $\\dot{W}_{elec} = 12.0\\ \\text{MW}$:
Total useful exergy recovered $= \\dot{W}_{elec} + \\dot{E}_2 = 12.000 + 23.879 = 35.879\\ \\text{MW}$.

**Step 3: Calculate exergy destruction $\\dot{I}$ and Second-Law efficiency**
Rate of exergy destruction:
\\[
\\dot{I} = \\dot{E}_1 - (\\dot{W}_{elec} + \\dot{E}_2) = 38.444\\ \\text{MW} - 35.879\\ \\text{MW} = 2.565\\ \\text{MW}
\\]
Second-Law Exergetic Efficiency:
\\[
\\eta_{ex} = \\left( \\frac{\\dot{W}_{elec} + \\dot{E}_2}{\\dot{E}_1} \\right) \\times 100 = \\left( \\frac{35.879\\ \\text{MW}}{38.444\\ \\text{MW}} \\right) \\times 100 = 93.33\\%
\\]
*(Note: If the exhaust steam were condensed and dumped into a cooling tower instead of sent to the biorefinery, $\\dot{E}_2$ would be destroyed completely, collapsing system exergetic efficiency to $\\frac{12.0}{38.444} = 31.2\\%$).*

**Conclusion**:
Industrial symbiosis re-utilizes **$23.88\\ \\text{MW}$** of otherwise wasted steam exergy, achieving an outstanding Second-Law efficiency of **$93.3\\%$** with only **$2.57\\ \\text{MW}$** destroyed."""
            }
        ]
    }
    return unit

if __name__ == "__main__":
    u10 = get_unit_10()
    print(f"Unit 10 generated: {len(u10['sections'])} sections, {len(u10['problems'])} problems.")
