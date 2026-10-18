# -*- coding: utf-8 -*-
"""
Environmental Chemistry - Unit 5 Content Generator
Unit 5: Groundwater Arsenic Geochemistry, Oceanic Pollution & Ecotoxicology
Strictly no marks, no course codes, pure Unix line endings.
"""

import json

def get_unit_5():
    unit = {
        "id": "unit_5",
        "title": "Groundwater Arsenic Geochemistry, Oceanic Pollution & Ecotoxicology",
        "badge": "Unit 05",
        "summary": "Deep geochemical thermodynamics and hydrogeological mechanisms of arsenic in alluvial aquifers; speciation (As(III) vs As(V)), reductive dissolution of iron oxyhydroxides, competitive sorption, and remediation; marine environmental chemistry, ocean salinity gradients, estuarine mixing, and ecotoxicological biomagnification.",
        "simulation": {
            "id": "sim_env_groundwater_arsenic_speciation",
            "title": "Groundwater Arsenic Speciation & Pourbaix (Eh-pH) Geochemical Simulator",
            "type": "canvas",
            "description": "Interactive thermodynamic Pourbaix diagram (Eh vs pH) and iron-oxyhydroxide reductive dissolution model computing As(III)/As(V) speciation ratios, ferrihydrite stability fields, and aqueous arsenic release kinetics."
        },
        "sections": [
            {
                "id": "sec_5_1",
                "title": "Hydrogeochemical Setting of the Bengal Basin & Quaternary Alluvial Aquifers",
                "content": """The Bengal Basin represents the world's most catastrophic natural environmental catastrophe involving geogenic groundwater contamination. Understanding the distribution of arsenic across Bangladesh and West Bengal demands rigorous hydrostratigraphic and sedimentological contextualization.

### Hydrostratigraphy and Geomorphic Architecture

The Bengal Basin comprises vast deltaic and alluvial floodplains deposited by the Ganges, Brahmaputra, and Meghna (GBM) river systems during the Late Pleistocene to Holocene epochs:
1. **Holocene Alluvial Sediments (< 10,000 years BP)**:
   - Typically grey, fine-to-medium sand, silt, and clay capping layers.
   - Characterized by high concentrations of labile solid-phase organic matter (buried peat, plant debris, and marsh sediments) and low redox potential ($E_h < -50\ \\text{mV}$).
   - Host shallow aquifers (typically 10 to 50 meters below ground surface) displaying alarming aqueous arsenic levels exceeding $50\\ \\mu\\text{g}/\\text{L}$ (the national standard of Bangladesh) and frequently surpassing $500\\ \\mu\\text{g}/\\text{L}$, well above the World Health Organization guideline of $10\\ \\mu\\text{g}/\\text{L}$.
2. **Pleistocene Sediments (Pleistocene Dupi Tila and Madhupur Formations)**:
   - Comprise brown, red, or yellowish weathered sands, clays, and gravels.
   - Deposited under oxidizing conditions or subjected to prolonged subaerial weathering and leaching during sea-level lowstands (e.g., Last Glacial Maximum ~20,000 BP).
   - Iron minerals exist as crystalline goethite ($\\alpha\\text{-FeOOH}$) and hematite ($\\alpha\\text{-Fe}_2\\text{O}_3$), which firmly sequester arsenic, resulting in arsenic-safe drinking water ($[\\text{As}] < 10\\ \\mu\\text{g}/\\text{L}$).

### Lithological Controls and Aquifer Confinement
The shallow alluvial aquifers are frequently capped by impermeable or semi-permeable surficial silty-clay aquitards (the 'upper clay layer'). This capping layer restricts the atmospheric diffusion of dissolved oxygen ($O_2$), generating closed-system anoxic hydrochemical environments that promote biogeochemical reducing reactions."""
            },
            {
                "id": "sec_5_2",
                "title": "Arsenic Speciation, Thermodynamics & Redox Equilibria: As(III) vs As(V)",
                "content": """Arsenic is a toxic metalloid (Group 15, atomic number 33) occurring in natural aquatic systems predominantly in two oxidation states: trivalent arsenite [$\\text{As(III)}$] and pentavalent arsenate [$\\text{As(V)}$].

### Inorganic Arsenate [$\\text{As(V)}$] Speciation
Arsenate exists as arsenic acid ($H_3AsO_4$) and its conjugate base oxyanions, exhibiting three stepwise thermodynamic dissociation constants at $298.15\\ \\text{K}$:
\\[
H_3AsO_4 \\rightleftharpoons H_2AsO_4^- + H^+, \\quad pK_{a1} = 2.22
\\]
\\[
H_2AsO_4^- \\rightleftharpoons HAsO_4^{2-} + H^+, \\quad pK_{a2} = 6.98
\\]
\\[
HAsO_4^{2-} \\rightleftharpoons AsO_4^{3-} + H^+, \\quad pK_{a3} = 11.53
\\]
In circumneutral groundwater (pH $6.5 - 8.5$), $\\text{As(V)}$ exists primarily as the negatively charged divalent and monovalent oxyanions $H_2AsO_4^-$ and $HAsO_4^{2-}$. Because of their electrostatic charges, these species bind strongly to positively charged mineral surfaces via inner-sphere complexation.

### Inorganic Arsenite [$\\text{As(III)}$] Speciation
Arsenite exists as arsenous acid ($H_3AsO_3$), an uncharged, neutral pyramidal molecule under normal aquifer pH conditions:
\\[
H_3AsO_3 \\rightleftharpoons H_2AsO_3^- + H^+, \\quad pK_{a1} = 9.22
\\]
\\[
H_2AsO_3^- \\rightleftharpoons HAsO_3^{2-} + H^+, \\quad pK_{a2} = 12.13
\\]
\\[
HAsO_3^{2-} \\rightleftharpoons AsO_3^{3-} + H^+, \\quad pK_{a3} = 13.40
\\]
Because $pK_{a1} = 9.22$, at typical groundwater pH ($6.5 - 8.0$), more than $95\\%$ of $\\text{As(III)}$ exists as the uncharged species $H_3AsO_3^0$. Neutral $H_3AsO_3^0$ does not experience significant Coulombic attraction toward charged mineral edges, rendering arsenite significantly more mobile and difficult to remove by conventional coagulants than arsenate."""
            },
            {
                "id": "sec_5_3",
                "title": "Reductive Dissolution of Iron(III) Oxyhydroxides & Microbial Mediation",
                "content": """Extensive multidisciplinary geochemical research has established that the **microbially mediated reductive dissolution of iron(III) oxyhydroxides** is the primary driver of high dissolved arsenic concentrations in Holocene aquifers of the Bengal Basin.

### The Source of Geogenic Arsenic
Arsenic is not introduced via anthropogenic industrial discharge or pesticide application; rather, it originates in Himalayan metamorphic and ophiolitic headwaters. Fluvial erosion carries arsenic-bearing iron oxyhydroxide colloids downstream, depositing them as coatings on mineral sand grains in the delta plain.

### Biogeochemical Reaction Mechanism
In buried Holocene sediments, buried reactive sedimentary organic matter ($CH_2O$) serves as the primary electron donor for indigenous dissimilatory metal-reducing bacteria (DMRB), notably species from the genera *Geobacter* (e.g., *G. metallireducens*), *Shewanella* (e.g., *S. putrefaciens*), and *Desulfuromonas*:
\\[
4\\text{Fe(OH)}_3\\text{(s)} + \\text{CH}_2\\text{O} + 7\\text{H}^+ \\xrightarrow{\\text{DMRB}} 4\\text{Fe}^{2+} + \\text{HCO}_3^- + 10\\text{H}_2\\text{O}
\\]
As the poorly crystalline hydrous ferric oxide (ferrihydrite, $5\\text{Fe}_2\\text{O}_3 \\cdot 9\\text{H}_2\\text{O}$) dissolves into soluble ferrous iron ($\\text{Fe}^{2+}$), the arsenic adsorbed to its mineral lattice is released into the interstitial porewater:
\\[
\\equiv\\!\\text{FeOH}\\text{--}\\text{AsO}_4^{2-} \\xrightarrow{\\text{Microbial Reduction}} \\text{Fe}^{2+}\\text{(aq)} + H_2\\text{AsO}_4^-\\text{(aq)} / H_3\\text{AsO}_3^0\\text{(aq)}
\\]

### Role of Dissimilatory Arsenate-Reducing Microorganisms (DARM)
Simultaneously, specialized microorganisms equipped with periplasmic arsenate reductase enzymes ($ArrAB$) utilize $\\text{As(V)}$ as a terminal respiratory electron acceptor:
\\[
H_2\\text{AsO}_4^- + \\text{CH}_3\\text{COO}^- \\xrightarrow{\\text{DARM}} H_3\\text{AsO}_3 + 2\\text{HCO}_3^-
\\]
This enzymatic reduction converts sorbed or dissolved arsenate into the far more mobile uncharged arsenite."""
            },
            {
                "id": "sec_5_4",
                "title": "Competitive Oxyanion Sorption & Competitive Displacement",
                "content": """Arsenic mobility in aquifer matrices is heavily governed by surface complexation equilibria on mineral surfaces (iron, aluminum, and manganese oxides, and clay edges). Oxyanions naturally present in groundwater compete directly for available surface coordination sites.

### Competitive Oxyanions: Phosphate ($PO_4^{3-}$), Silicate ($H_4SiO_4$), and Bicarbonate ($HCO_3^-$)
1. **Phosphate ($PO_4^{3-}$)**:
   - Possesses identical tetrahedral coordination geometry and similar thermochemical properties to arsenate ($AsO_4^{3-}$).
   - Forms bidentate binuclear inner-sphere complexes ($\equiv\\!\\text{Fe}_2\\text{O}_2\\text{PO}_2$) with binding constants comparable to or exceeding those of arsenate:
     \\[
     \\equiv\\!\\text{Fe}_2\\text{O}_2\\text{AsO}_2 + \\text{HPO}_4^{2-} \\rightleftharpoons \\equiv\\!\\text{Fe}_2\\text{O}_2\\text{PO}_2 + \\text{HAsO}_4^{2-}
     \\]
   - Elevated dissolved phosphate concentrations (arising from fertilizer runoff or organic matter remineralization) displace arsenate from sediment binding sites, driving arsenic into solution.
2. **Silicate ($H_4SiO_4 / H_3SiO_4^-$)**:
   - Present at high baseline concentrations in alluvial groundwater ($0.2 - 0.7\\ \\text{mmol}/\\text{L}$) due to silicate mineral weathering.
   - Competes moderately for binding sites, decreasing arsenic adsorption capacity across ferrihydrite and goethite surfaces.
3. **Bicarbonate ($HCO_3^-$)**:
   - Generated abundantly during organic matter oxidation (reaching concentrations of $300 - 800\\ \\text{mg}/\\text{L}$).
   - Promotes carbonate complexation and forms secondary iron carbonate minerals (siderite, $\\text{FeCO}_3$), altering the surface charge and available specific surface area."""
            },
            {
                "id": "sec_5_5",
                "title": "Chemical Speciation Modeling, Eh-pH (Pourbaix) Relationships & Geochemical Principles",
                "content": """Thermodynamic stability fields of arsenic species in aquatic systems are quantified using electrochemical potential ($E_h$) and pH relationships, represented visually in Pourbaix diagrams.

### Nernstian Formulation of the As(V)/As(III) Couple
The redox half-reaction connecting the predominant aqueous species at circumneutral pH is:
\\[
H_2AsO_4^- + 3H^+ + 2e^- \\rightleftharpoons H_3AsO_3 + H_2O
\\]
The standard reduction potential at standard conditions ($T = 298.15\\ \\text{K}$, $P = 1\\ \\text{bar}$, activities $a = 1$) is $E^\\circ = +0.658\\ \\text{V}$.

Applying the Nernst equation:
\\[
E_h = E^\\circ - \\frac{2.303 RT}{nF}\\log_{10} \\left( \\frac{a_{H_3AsO_3}}{a_{H_2AsO_4^-} [H^+]^3} \\right)
\\]
Substituting constants $R = 8.314\\ \\text{J}/(\\text{mol}\\cdot\\text{K})$, $T = 298.15\\ \\text{K}$, $F = 96485\\ \\text{C}/\\text{mol}$, and $n = 2$:
\\[
E_h = 0.658 - 0.0887\\ \\text{pH} - 0.0296\\log_{10} \\left( \\frac{a_{H_3AsO_3}}{a_{H_2AsO_4^-}} \\right)
\\]
At equal activities ($a_{H_3AsO_3} = a_{H_2AsO_4^-}$), the phase boundary simplifies to:
\\[
E_h = 0.658 - 0.0887\\ \\text{pH}
\\]
At $\\text{pH} = 7.0$:
\\[
E_h = 0.658 - 0.0887(7.0) = +0.037\\ \\text{V} = +37\\ \\text{mV}
\\]
If the measured groundwater redox potential drops below $+37\\ \\text{mV}$, thermodynamically stable arsenic shifts entirely from $\\text{As(V)}$ to mobile $\\text{As(III)}$.

### Geochemical Speciation Software (PHREEQC)
Modern hydrogeochemistry computes multi-component equilibrium using chemical speciation software (such as USGS PHREEQC), simultaneously solving mass balance, charge balance, activity coefficient corrections via the Davies or B-dot equations, and surface complexation models (Diffuse Double Layer or Generalized Two-Layer Models)."""
            },
            {
                "id": "sec_5_6",
                "title": "Arsenic Remediation Technologies: Coagulation, Adsorption & In-situ Aeration",
                "content": """Engineering interventions to eliminate arsenic from drinking water supplies operate across household, community, and in-situ municipal scales.

### Coagulation-Coprecipitation
The most widespread chemical treatment involves ferric chloride ($\\text{FeCl}_3$) or alum ($\\text{Al}_2(\\text{SO}_4)_3 \\cdot 18\\text{H}_2\\text{O}$) dosing:
1. Ferric ions rapidly hydrolyze to form an amorphous ferric hydroxide precipitate:
   \\[
   \\text{Fe}^{3+} + 3\\text{H}_2\\text{O} \\rightleftharpoons \\text{Fe(OH)}_3\\text{(am)} + 3\\text{H}^+
   \\]
2. $\\text{As(V)}$ oxyanions adsorb strongly onto the floc surface via ligand exchange:
   \\[
   \\equiv\\!\\text{FeOH} + HAsO_4^{2-} \\rightleftharpoons \\equiv\\!\\text{FeAsO}_4^{2-} + \\text{H}_2\\text{O}
   \\]
3. *Pre-oxidation Requirement*: Because uncharged $\\text{As(III)}$ binds poorly to ferric flocs, a pre-oxidation step (using hypochlorite, ozone, or solar Fenton processes) is mandatory to oxidize $\\text{As(III)}$ to $\\text{As(V)}$ prior to coagulation.

### Fixed-Bed Adsorption Columns
Fixed-bed contactors utilize granular ferric hydroxide (GFH), activated alumina ($\\text{Al}_2\\text{O}_3$), or iron-coated sand. Breakthrough curves are governed by the bed volumes treated ($BV$) and the Thomas or Bohart-Adams kinetic transport models:
\\[
\\frac{C_t}{C_0} = \\frac{1}{1 + \\exp\\left( \\frac{k_{Th} q_0 M}{Q} - k_{Th} C_0 t \\right)}
\\]

### Subterranean In-situ Arsenic Remediation (SAR)
In-situ remediation avoids hazardous chemical sludge disposal at the surface. Oxygenated, aerated water is periodically injected down the tubewell into the aquifer surrounding the intake screen. Dissolved oxygen oxidizes naturally present $\\text{Fe}^{2+}$ into insoluble $\\text{Fe(OH)}_3$ coatings on sediment grains:
\\[
4\\text{Fe}^{2+} + \\text{O}_2 + 10\\text{H}_2\\text{O} \\rightarrow 4\\text{Fe(OH)}_3\\text{(s)} + 8\\text{H}^+
\\]
Subsequent groundwater extraction draws water through this newly formed reactive iron-mineral filter, sequestering arsenic in situ within the subterranean formation."""
            },
            {
                "id": "sec_5_7",
                "title": "Marine Environmental Chemistry: Oceanic Chemical Stratification & Estuarine Mixing",
                "content": """The oceans cover $71\\%$ of the Earth's surface and represent the ultimate sink for chemical weathering fluxes. Marine chemistry is governed by conservative vs non-conservative chemical dynamics and density-driven stratification.

### Chemical Composition of Seawater & Marcet's Principle
Seawater has an average practical salinity ($S$) of $35\\ \\text{g}/\\text{kg}$ ($35\\ \\text{PSU}$). Marcet's Principle (the Law of Constant Proportions) establishes that the ratios of major conservative ions ($Cl^-$, $Na^+$, $SO_4^{2-}$, $Mg^{2+}$, $Ca^{2+}$, $K^+$) remain constant throughout the world's open oceans regardless of absolute salinity:
\\[
\\text{Major Ions}: \\quad Cl^- (55.04\\%), \\quad Na^+ (30.61\\%), \\quad SO_4^{2-} (7.68\\%), \\quad Mg^{2+} (3.69\\%), \\quad Ca^{2+} (1.16\\%), \\quad K^+ (1.10\\%)
\\]

### Ocean Water Column Stratification
The oceanic water column is physically partitioned into three distinct vertical zones:
1. **Surface Mixed Layer (0 - 200 m)**: Wind-stirred, photic zone, saturated with $O_2$, depleted in macronutrients ($N, P, Si$) due to phytoplankton uptake.
2. **Pycnocline (Thermocline & Halocline, 200 - 1000 m)**: Zone of rapid density increase, accompanied by a sharp temperature drop (thermocline) and salinity variation (halocline).
3. **Deep Abyssal Layer (> 1000 m)**: Cold ($0 - 4^\\circ\\text{C}$), high-pressure, nutrient-rich water originating from polar deep-water formation (Thermohaline Circulation / Global Conveyor Belt).

### Estuarine Mixing Dynamics
In estuaries, fresh river water ($S \\approx 0$) mixes with saline seawater ($S \\approx 35$). Chemical species are categorized by their behavior across the salinity gradient:
- **Conservative Mixing**: Linear relationship between concentration $C$ and salinity $S$:
  \\[
  C = C_{river} + \\frac{C_{marine} - C_{river}}{S_{marine}} S
  \\]
- **Non-conservative Mixing**: Non-linear profiles exhibiting positive deviation (addition, due to desorption from riverine colloids) or negative deviation (removal, due to flocculation and sedimentation, common for humic acids, iron, and trace metals)."""
            },
            {
                "id": "sec_5_8",
                "title": "Ecotoxicological Pathways, Marine Contaminants & Biomarker Responses",
                "content": """Ecotoxicology evaluates the transport, transformation, biological uptake, and toxicological outcomes of anthropogenic contaminants across marine and aquatic ecosystems.

### Major Marine Contaminant Classes
1. **Trace Heavy Metals ($Hg, Cd, Pb, Cu$)**:
   - Methylmercury ($CH_3Hg^+$) represents the most bioavailable and neurotoxic marine organometal, forming stable covalent complexes with protein sulfhydryl ($-SH$) groups.
2. **Petroleum Hydrocarbons and PAHs**:
   - Polycyclic aromatic hydrocarbons (benzo[a]pyrene, chrysene) induce DNA adduct formation and carcinogenesis via cytochrome P450 monooxygenase enzymatic bioactivation.
3. **Marine Plastics and Microplastics (< 5 mm)**:
   - Act as physical stressors and vector carriers that concentrate hydrophobic toxic chemicals (POPs, phthalates, bisphenol A) by several orders of magnitude relative to surrounding seawater.

### Molecular and Cellular Biomarkers
Biomarkers provide early warning diagnostics of toxic exposure before organismal mortality occurs:
- **Metallothioneins (MTs)**: Low molecular weight, cysteine-rich proteins synthesized in liver/hepatopancreas tissues that chelate toxic divalent metal cations ($Cd^{2+}, Hg^{2+}, Pb^{2+}$).
- **Ethoxyresorufin-O-deethylase (EROD) Induction**: Measures the catalytic activity of the CYP1A enzyme family, serving as a specific biomarker for exposure to coplanar PCBs, dioxins, and PAHs.
- **Acetylcholinesterase (AChE) Inhibition**: Biomarker indicating organophosphate and carbamate neurotoxin contamination."""
            }
        ],
        "problems": [
            {
                "id": "prob_5_1",
                "tier": "Foundational",
                "title": "Arsenic Acid Dissociation & Speciation Fraction at Circumneutral pH",
                "statement": "Groundwater extracted from a tube well in Munshiganj, Bangladesh exhibits a field-measured pH of 7.20. Assuming pure inorganic pentavalent arsenate [As(V)] with acid dissociation constants $pK_{a1} = 2.22$, $pK_{a2} = 6.98$, and $pK_{a3} = 11.53$ at 298.15 K, calculate the exact speciation fractions $\\alpha_1$ ($H_2AsO_4^-$) and $\\alpha_2$ ($HAsO_4^{2-}$).",
                "hints": [
                    "Formulate the polynomial denominator $D = [H^+]^3 + K_{a1}[H^+]^2 + K_{a1}K_{a2}[H^+] + K_{a1}K_{a2}K_{a3}$.",
                    "Compute $[H^+] = 10^{-7.20} = 6.3096 \\times 10^{-8}\\ \\text{M}$.",
                    "Evaluate the dominant terms in the denominator at circumneutral pH."
                ],
                "solution": """**Step 1: Calculate hydrogen ion activity and dissociation constants**
Given $\\text{pH} = 7.20$:
\\[
[H^+] = 10^{-7.20} = 6.3096 \\times 10^{-8}\\ \\text{M}
\\]
The acid dissociation constants are:
\\[
K_{a1} = 10^{-2.22} = 6.0256 \\times 10^{-3}
\\]
\\[
K_{a2} = 10^{-6.98} = 1.0471 \\times 10^{-7}
\\]
\\[
K_{a3} = 10^{-11.53} = 2.9512 \\times 10^{-12}
\\]

**Step 2: Formulate the master speciation polynomial denominator**
\\[
D = [H^+]^3 + K_{a1}[H^+]^2 + K_{a1}K_{a2}[H^+] + K_{a1}K_{a2}K_{a3}
\\]
Let us evaluate each term:
- Term 1: $[H^+]^3 = (6.3096 \\times 10^{-8})^3 = 2.512 \\times 10^{-22}$ (negligible)
- Term 2: $K_{a1}[H^+]^2 = (6.0256 \\times 10^{-3}) \\times (6.3096 \\times 10^{-8})^2 = 2.399 \\times 10^{-17}$
- Term 3: $K_{a1}K_{a2}[H^+] = (6.0256 \\times 10^{-3}) \\times (1.0471 \\times 10^{-7}) \\times (6.3096 \\times 10^{-8}) = 3.981 \\times 10^{-17}$
- Term 4: $K_{a1}K_{a2}K_{a3} = (6.0256 \\times 10^{-3}) \\times (1.0471 \\times 10^{-7}) \\times (2.9512 \\times 10^{-12}) = 1.862 \\times 10^{-21}$ (negligible)

Factoring out the shared pre-factor $K_{a1}[H^+]$:
\\[
\\frac{D}{K_{a1}[H^+]} = [H^+] + K_{a2} = 6.3096 \\times 10^{-8} + 1.0471 \\times 10^{-7} = 1.6781 \\times 10^{-7}\\ \\text{M}
\\]

**Step 3: Calculate the ionization fractions**
For monovalent arsenate ($H_2AsO_4^-$):
\\[
\\alpha_1 = \\frac{K_{a1}[H^+]^2}{D} = \\frac{[H^+]}{[H^+] + K_{a2}} = \\frac{6.3096 \\times 10^{-8}}{1.6781 \\times 10^{-7}} = 0.3760 \\quad (37.60\\%)
\\]
For divalent arsenate ($HAsO_4^{2-}$):
\\[
\\alpha_2 = \\frac{K_{a1}K_{a2}[H^+]}{D} = \\frac{K_{a2}}{[H^+] + K_{a2}} = \\frac{1.0471 \\times 10^{-7}}{1.6781 \\times 10^{-7}} = 0.6240 \\quad (62.40\\%)
\\]

**Conclusion**:
At pH 7.20, dissolved As(V) exists as **37.6% $H_2AsO_4^-$** and **62.4% $HAsO_4^{2-}$**."""
            },
            {
                "id": "prob_5_2",
                "tier": "Foundational",
                "title": "Pourbaix Redox Potential Boundary for As(V)/As(III) at Aquifer Conditions",
                "statement": "An alluvial aquifer in Chandpur has a groundwater pH of 7.00. The standard reduction potential for the half-reaction $H_2AsO_4^- + 3H^+ + 2e^- \\rightleftharpoons H_3AsO_3 + H_2O$ is $E^\\circ = +0.658\\ \\text{V}$ at 298.15 K. Calculate: (a) the equilibrium redox potential ($E_h$) when $[H_2AsO_4^-] = [H_3AsO_3]$, and (b) the resulting $[\\text{As(III)}]/[\\text{As(V)}]$ ratio if field platinum-electrode measurements yield an in-situ redox potential of $E_h = -0.050\\ \\text{V}$ (-50 mV).",
                "hints": [
                    "Use the Nernst equation: $E_h = E^\\circ - \\frac{0.05916}{2} \\log_{10} \\left( \\frac{[H_3AsO_3]}{[H_2AsO_4^-] [H^+]^3} \\right)$.",
                    "Expand the log term: $\\log_{10}([H^+]^{-3}) = 3\\text{pH}$."
                ],
                "solution": """**Step 1: Formulate the Nernst equation**
For the half-reaction:
\\[
H_2AsO_4^- + 3H^+ + 2e^- \\rightleftharpoons H_3AsO_3 + H_2O, \\quad E^\\circ = +0.658\\ \\text{V}
\\]
The Nernst equation at $298.15\\ \\text{K}$ ($2.303 RT / F = 0.05916\\ \\text{V}$):
\\[
E_h = E^\\circ - \\frac{0.05916}{2} \\log_{10} \\left( \\frac{[H_3AsO_3]}{[H_2AsO_4^-] [H^+]^3} \\right)
\\]
Separating the pH term:
\\[
E_h = E^\\circ - 0.02958 \\left( \\log_{10}\\frac{[H_3AsO_3]}{[H_2AsO_4^-]} + 3\\text{pH} \\right)
\\]
\\[
E_h = E^\\circ - 0.08874\\ \\text{pH} - 0.02958\\log_{10}\\frac{[H_3AsO_3]}{[H_2AsO_4^-]}
\\]

**Step 2: Calculate equilibrium $E_h$ for equal activities (Part a)**
Setting $[H_3AsO_3] = [H_2AsO_4^-]$ at $\\text{pH} = 7.00$:
\\[
E_h = 0.658 - 0.08874(7.00) - 0.02958(0) = 0.658 - 0.6212 = +0.0368\\ \\text{V} = +36.8\\ \\text{mV}
\\]

**Step 3: Calculate species ratio at $E_h = -0.050\\ \\text{V}$ (Part b)**
Rearranging for the logarithmic ratio:
\\[
0.02958\\log_{10}\\frac{[H_3AsO_3]}{[H_2AsO_4^-]} = 0.658 - 0.08874(7.00) - E_h = 0.0368 - (-0.050) = 0.0868\\ \\text{V}
\\]
\\[
\\log_{10}\\frac{[H_3AsO_3]}{[H_2AsO_4^-]} = \\frac{0.0868}{0.02958} = 2.9344
\\]
\\[
\\frac{[H_3AsO_3]}{[H_2AsO_4^-]} = 10^{2.9344} = 859.8 \\approx 860
\\]

**Conclusion**:
At $E_h = -50\\ \\text{mV}$ and pH 7.00, trivalent arsenite outnumbers pentavalent arsenate by **860 to 1**, demonstrating complete thermodynamic dominance of mobile As(III)."""
            },
            {
                "id": "prob_5_3",
                "tier": "Foundational",
                "title": "Estuarine Conservative vs Non-conservative Mixing Index and Chemical Flux",
                "statement": "In the Meghna River estuary, riverine freshwater entering with salinity $S_0 = 0.2\\ \\text{PSU}$ has a dissolved iron concentration of $[\\text{Fe}]_{river} = 45.0\\ \\mu\\text{M}$. Open Bay of Bengal seawater has salinity $S_m = 34.0\\ \\text{PSU}$ and $[\\text{Fe}]_{marine} = 0.05\\ \\mu\\text{M}$. (a) Calculate the theoretical conservative concentration of dissolved iron at an estuarine monitoring station where salinity is measured at $S = 12.0\\ \\text{PSU}$. (b) If the actual measured iron concentration at this station is $2.8\\ \\mu\\text{M}$, determine the percentage removal attributable to flocculation and sedimentation.",
                "hints": [
                    "Theoretical conservative mixing equation: $C_{cons} = C_{river} + \\frac{C_{marine} - C_{river}}{S_m - S_0}(S - S_0)$.",
                    "Removal percentage: $\\text{Removal} = \\frac{C_{cons} - C_{meas}}{C_{cons}} \\times 100\\%$."
                ],
                "solution": """**Step 1: Calculate the theoretical conservative iron concentration**
Applying the conservative two-endmember mixing equation:
\\[
C_{cons} = C_{river} + \\left( \\frac{C_{marine} - C_{river}}{S_m - S_0} \\right)(S - S_0)
\\]
Substituting the given parameter values:
\\[
C_{cons} = 45.0 + \\left( \\frac{0.05 - 45.0}{34.0 - 0.2} \\right)(12.0 - 0.2)
\\]
\\[
C_{cons} = 45.0 + \\left( \\frac{-44.95}{33.8} \\right)(11.8) = 45.0 + (-1.3299 \\times 11.8) = 45.0 - 15.69 = 29.31\\ \\mu\\text{M}
\\]

**Step 2: Determine non-conservative removal percentage**
The measured concentration is $C_{meas} = 2.8\\ \\mu\\text{M}$.
The concentration deficit due to non-conservative geochemical removal:
\\[
\\Delta C = C_{cons} - C_{meas} = 29.31 - 2.80 = 26.51\\ \\mu\\text{M}
\\]
The percentage removal is:
\\[
\\text{Removal (\\%)} = \\frac{\\Delta C}{C_{cons}} \\times 100 = \\frac{26.51}{29.31} \\times 100 = 90.45\\%
\\]

**Conclusion**:
The theoretical conservative concentration is **$29.31\\ \\mu\\text{M}$**, and approximately **$90.5\\%$** of riverine dissolved iron is removed by estuarine colloid flocculation and settling."""
            },
            {
                "id": "prob_5_4",
                "tier": "Intermediate",
                "title": "Thermodynamics of Microbial Iron(III) Reduction Coupled to Acetate Oxidation",
                "statement": "Dissimilatory metal-reducing bacteria (e.g. *Geobacter*) drive iron oxyhydroxide dissolution via acetate oxidation: $\\text{CH}_3\\text{COO}^- + 8\\text{Fe(OH)}_3\\text{(s)} + 15\\text{H}^+ \\rightarrow 2\\text{HCO}_3^- + 8\\text{Fe}^{2+} + 20\\text{H}_2\\text{O}$. Given the standard reduction potentials at 298.15 K: (1) $\\text{Fe(OH)}_3\\text{(s)} + 3\\text{H}^+ + e^- \\rightleftharpoons \\text{Fe}^{2+} + 3\\text{H}_2\\text{O}$ ($E^\\circ = +1.060\\ \\text{V}$), and (2) $2\\text{HCO}_3^- + 9\\text{H}^+ + 8e^- \\rightleftharpoons \\text{CH}_3\\text{COO}^- + 4\\text{H}_2\\text{O}$ ($E^\\circ = +0.187\\ \\text{V}$). Calculate: (a) the standard cell electromotive force $\\Delta E^\\circ$ and standard Gibbs free energy change $\\Delta G^\\circ$ for the 8-electron coupled reaction, and (b) the actual Gibbs energy $\\Delta G'$ at physiological/aquifer conditions (pH = 7.0, $[\\text{CH}_3\\text{COO}^-] = 0.10\\ \\text{mM}$, $[\\text{HCO}_3^-] = 5.0\\ \\text{mM}$, $[\\text{Fe}^{2+}] = 0.05\\ \\text{mM}$, $T = 298.15\\ \\text{K}$).",
                "hints": [
                    "Cell potential: $\\Delta E^\\circ = E^\\circ(\\text{cathode}) - E^\\circ(\\text{anode})$.",
                    "Gibbs free energy: $\\Delta G^\\circ = -n F \\Delta E^\\circ$ with $n = 8$ electrons.",
                    "Use $\\Delta G' = \\Delta G^\\circ + RT \\ln Q$, taking care with the reaction quotient $Q = \\frac{[\\text{HCO}_3^-]^2 [\\text{Fe}^{2+}]^8}{[\\text{CH}_3\\text{COO}^-] [H^+]^{15}}$."
                ],
                "solution": """**Step 1: Calculate standard electromotive force $\\Delta E^\\circ$ and $\\Delta G^\\circ$**
Cathodic reduction (Iron):
\\[
\\text{Fe(OH)}_3\\text{(s)} + 3\\text{H}^+ + e^- \\rightleftharpoons \\text{Fe}^{2+} + 3\\text{H}_2\\text{O}, \\quad E^\\circ_{cat} = +1.060\\ \\text{V}
\\]
Anodic oxidation (Acetate):
\\[
\\text{CH}_3\\text{COO}^- + 4\\text{H}_2\\text{O} \\rightleftharpoons 2\\text{HCO}_3^- + 9\\text{H}^+ + 8e^-, \\quad E^\\circ_{an} = +0.187\\ \\text{V}
\\]
The overall standard cell electromotive force:
\\[
\\Delta E^\\circ = E^\\circ_{cat} - E^\\circ_{an} = 1.060\\ \\text{V} - 0.187\\ \\text{V} = +0.873\\ \\text{V}
\\]
The standard Gibbs free energy change for $n = 8$ moles of electrons:
\\[
\\Delta G^\\circ = -n F \\Delta E^\\circ = -(8)(96485\\ \\text{C}/\\text{mol})(0.873\\ \\text{V}) = -673,856\\ \\text{J}/\\text{mol} = -673.86\\ \\text{kJ}/\\text{mol}
\\]

**Step 2: Formulate the reaction quotient $Q$ at aquifer conditions**
Aquifer chemical concentrations:
- $\\text{pH} = 7.00 \\implies [H^+] = 1.0 \\times 10^{-7}\\ \\text{M}$
- $[\\text{CH}_3\\text{COO}^-] = 0.10\\ \\text{mM} = 1.0 \\times 10^{-4}\\ \\text{M}$
- $[\\text{HCO}_3^-] = 5.0\\ \\text{mM} = 5.0 \\times 10^{-3}\\ \\text{M}$
- $[\\text{Fe}^{2+}] = 0.05\\ \\text{mM} = 5.0 \\times 10^{-5}\\ \\text{M}$

The reaction quotient:
\\[
Q = \\frac{[\\text{HCO}_3^-]^2 [\\text{Fe}^{2+}]^8}{[\\text{CH}_3\\text{COO}^-] [H^+]^{15}}
\\]
Evaluating numerator and denominator:
\\[
[\\text{HCO}_3^-]^2 = (5.0 \\times 10^{-3})^2 = 2.5 \\times 10^{-5}
\\]
\\[
[\\text{Fe}^{2+}]^8 = (5.0 \\times 10^{-5})^8 = 3.90625 \\times 10^{-35}
\\]
Numerator $= (2.5 \\times 10^{-5})(3.90625 \\times 10^{-35}) = 9.7656 \\times 10^{-40}$

Denominator:
\\[
[\\text{CH}_3\\text{COO}^-] [H^+]^{15} = (1.0 \\times 10^{-4})(1.0 \\times 10^{-7})^{15} = (1.0 \\times 10^{-4})(1.0 \\times 10^{-105}) = 1.0 \\times 10^{-109}
\\]
Thus:
\\[
Q = \\frac{9.7656 \\times 10^{-40}}{1.0 \\times 10^{-109}} = 9.7656 \\times 10^{69}
\\]

**Step 3: Calculate actual Gibbs energy $\\Delta G'$**
\\[
\\ln Q = \\ln(9.7656 \\times 10^{69}) = \\ln(9.7656) + 69 \\ln(10) = 2.2789 + 158.877 = 161.156
\\]
\\[
RT \\ln Q = (8.3145\\ \\text{J}/(\\text{mol}\\cdot\\text{K}))(298.15\\ \\text{K})(161.156) = 399,504\\ \\text{J}/\\text{mol} = +399.50\\ \\text{kJ}/\\text{mol}
\\]
The actual free energy is:
\\[
\\Delta G' = \\Delta G^\\circ + RT \\ln Q = -673.86 + 399.50 = -274.36\\ \\text{kJ}/\\text{mol}
\\]

**Conclusion**:
The reaction remains strongly exergonic ($\Delta G' = -274.4\ \text{kJ}/\text{mol}$), thermodynamically driving spontaneous microbial iron reduction and arsenic mobilization."""
            },
            {
                "id": "prob_5_5",
                "tier": "Intermediate",
                "title": "Competitive Langmuir Sorption: Arsenate vs Phosphate on Ferrihydrite",
                "statement": "Synthetic ferrihydrite adsorbent in a water treatment column exhibits a maximum total surface adsorption site capacity of $q_{max} = 1.20\\ \\text{mmol}/\\text{g}$. For competitive adsorption between arsenate (As) and phosphate (P), the multicomponent Langmuir isotherm is: $q_{As} = \\frac{q_{max} K_{As} C_{As}}{1 + K_{As} C_{As} + K_P C_P}$. The single-solute Langmuir affinity constants are $K_{As} = 8.50\\ \\text{L}/\\text{mg}$ and $K_P = 5.20\\ \\text{L}/\\text{mg}$. An aqueous feed contains $C_{As} = 0.25\\ \\text{mg}/\\text{L}$ ($250\\ \\mu\\text{g}/\\text{L}$). Calculate: (a) the equilibrium arsenic loading $q_{As}$ in the absence of phosphate ($C_P = 0$), and (b) the remaining arsenic loading and percentage capacity loss when the groundwater contains co-dissolved phosphate at $C_P = 2.00\\ \\text{mg}/\\text{L}$.",
                "hints": [
                    "Evaluate the denominator without phosphate: $1 + K_{As} C_{As}$.",
                    "Evaluate the denominator with phosphate: $1 + K_{As} C_{As} + K_P C_P$.",
                    "Compare the resulting $q_{As}$ values."
                ],
                "solution": """**Step 1: Calculate arsenic loading in the absence of phosphate ($C_P = 0$)**
Given:
- $q_{max} = 1.20\\ \\text{mmol}/\\text{g}$
- $K_{As} = 8.50\\ \\text{L}/\\text{mg}$
- $C_{As} = 0.25\\ \\text{mg}/\\text{L}$

The dimensionless product:
\\[
K_{As} C_{As} = (8.50\\ \\text{L}/\\text{mg})(0.25\\ \\text{mg}/\\text{L}) = 2.125
\\]
In the absence of phosphate:
\\[
q_{As}^{(0)} = \\frac{q_{max} K_{As} C_{As}}{1 + K_{As} C_{As}} = \\frac{(1.20)(2.125)}{1 + 2.125} = \\frac{2.550}{3.125} = 0.8160\\ \\text{mmol}/\\text{g}
\\]

**Step 2: Calculate arsenic loading with competitive phosphate ($C_P = 2.00\\ \\text{mg}/\\text{L}$)**
Given $K_P = 5.20\\ \\text{L}/\\text{mg}$ and $C_P = 2.00\\ \\text{mg}/\\text{L}$:
\\[
K_P C_P = (5.20\\ \\text{L}/\\text{mg})(2.00\\ \\text{mg}/\\text{L}) = 10.40
\\]
The new denominator is:
\\[
D_{comp} = 1 + K_{As} C_{As} + K_P C_P = 1 + 2.125 + 10.40 = 13.525
\\]
The reduced arsenic capacity is:
\\[
q_{As}^{(P)} = \\frac{q_{max} K_{As} C_{As}}{D_{comp}} = \\frac{2.550}{13.525} = 0.1885\\ \\text{mmol}/\\text{g}
\\]

**Step 3: Calculate percentage capacity reduction**
\\[
\\Delta q_{\\%} = \\frac{q_{As}^{(0)} - q_{As}^{(P)}}{q_{As}^{(0)}} \\times 100 = \\frac{0.8160 - 0.1885}{0.8160} \\times 100 = \\frac{0.6275}{0.8160} \\times 100 = 76.89\\%
\\]

**Conclusion**:
Co-occurring phosphate reduces the ferrihydrite arsenic adsorption capacity from **$0.816\\ \\text{mmol}/\\text{g}$** down to **$0.189\\ \\text{mmol}/\\text{g}$**, a staggering **$76.9\\%$ reduction** due to competitive site exclusion."""
            },
            {
                "id": "prob_5_6",
                "tier": "Intermediate",
                "title": "In-situ Subterranean Arsenic Remediation: Oxygen Injection Stoichiometry",
                "statement": "An in-situ Subterranean Arsenic Remediation (SAR) system operates in an alluvial aquifer with a dissolved iron concentration of $[\\text{Fe}^{2+}] = 8.0\\ \\text{mg}/\\text{L}$ and arsenic $[\\text{As}] = 240\\ \\mu\\text{g}/\\text{L}$. The reaction oxidizes $\\text{Fe}^{2+}$ to hydrous ferric oxide according to: $4\\text{Fe}^{2+} + \\text{O}_2 + 10\\text{H}_2\\text{O} \\rightarrow 4\\text{Fe(OH)}_3\\text{(s)} + 8\\text{H}^+$. (a) Determine the theoretical stoichiometric mass of dissolved oxygen ($O_2$ in mg) required to oxidize 1.0 mg of $\\text{Fe}^{2+}$. (b) If $1000\\ \\text{L}$ of aerated water saturated with dissolved oxygen at $9.0\\ \\text{mg}/\\text{L}$ is injected into the aquifer, calculate the total mass of ferrihydrite (as $\\text{Fe(OH)}_3$, molar mass $106.87\\ \\text{g}/\\text{mol}$) deposited. (c) If each gram of precipitated $\\text{Fe(OH)}_3$ adsorbs $3.5\\ \\text{mg}$ of arsenic, calculate the total arsenic removal capacity provided by this single injection cycle.",
                "hints": [
                    "Stoichiometry: 1 mol $O_2$ (32.00 g) oxidizes 4 mol $Fe^{2+}$ (4 x 55.85 g = 223.4 g).",
                    "Mass of oxygen injected: $m_{O2} = V \\times C_{O2}$.",
                    "Compute moles of Fe oxidized, moles of Fe(OH)3 formed, and resulting arsenic adsorption."
                ],
                "solution": """**Step 1: Determine stoichiometric oxygen requirement per mg of $\\text{Fe}^{2+}$**
From the balanced redox reaction:
\\[
4\\text{Fe}^{2+} + \\text{O}_2 + 10\\text{H}_2\\text{O} \\rightarrow 4\\text{Fe(OH)}_3\\text{(s)} + 8\\text{H}^+
\\]
$1\\ \\text{mol of } O_2$ ($32.00\\ \\text{g}$) oxidizes $4\\ \\text{mol of } Fe^{2+}$ ($4 \\times 55.845\\ \\text{g} = 223.38\\ \\text{g}$).
The mass ratio:
\\[
\\frac{\\text{Mass } O_2}{\\text{Mass } Fe^{2+}} = \\frac{32.00}{223.38} = 0.14325\\ \\text{mg } O_2 / \\text{mg } Fe^{2+}
\\]
Thus, **$0.143\\ \\text{mg of } O_2$** is required per $1.0\\ \\text{mg of } \\text{Fe}^{2+}$.

**Step 2: Total mass of $\\text{Fe(OH)}_3$ deposited from $1000\\ \\text{L}$ aerated water**
The injected mass of dissolved oxygen:
\\[
m_{O2} = 1000\\ \\text{L} \\times 9.0\\ \\text{mg}/\\text{L} = 9000\\ \\text{mg } O_2 = 9.00\\ \\text{g } O_2
\\]
Moles of $O_2$ injected:
\\[
n_{O2} = \\frac{9.00\\ \\text{g}}{32.00\\ \\text{g}/\\text{mol}} = 0.28125\\ \\text{mol } O_2
\\]
Moles of $\\text{Fe(OH)}_3$ formed:
\\[
n_{\\text{Fe(OH)}_3} = 4 \\times n_{O2} = 4 \\times 0.28125 = 1.125\\ \\text{mol}
\\]
Mass of $\\text{Fe(OH)}_3$ precipitate ($M = 106.87\\ \\text{g}/\\text{mol}$):
\\[
m_{\\text{Fe(OH)}_3} = 1.125\\ \\text{mol} \\times 106.87\\ \\text{g}/\\text{mol} = 120.23\\ \\text{g}
\\]

**Step 3: Total arsenic removal capacity**
Given an adsorption capacity of $3.5\\ \\text{mg As} / \\text{g } \\text{Fe(OH)}_3$:
\\[
m_{As, removal} = 120.23\\ \\text{g } \\text{Fe(OH)}_3 \\times 3.5\\ \\text{mg As}/\\text{g} = 420.8\\ \\text{mg of As}
\\]
Volume of raw groundwater containing $240\\ \\mu\\text{g}/\\text{L}$ ($0.240\\ \\text{mg}/\\text{L}$) arsenic that can be purified:
\\[
V_{treated} = \\frac{420.8\\ \\text{mg}}{0.240\\ \\text{mg}/\\text{L}} = 1,753\\ \\text{L}
\\]

**Conclusion**:
The injection yields **$120.2\\ \\text{g}$** of freshly precipitated ferrihydrite, capable of stripping **$420.8\\ \\text{mg}$ of arsenic** (purifying over 1,750 liters of contaminated groundwater)."""
            },
            {
                "id": "prob_5_7",
                "tier": "Advanced",
                "title": "Multi-component 1D Reactive Transport with Retardation Factor",
                "statement": "Arsenic transport in an alluvial sandy aquifer is modeled via the 1D Advection-Dispersion-Reaction Equation (ADRE): $\\frac{\\partial C}{\\partial t} = \\frac{D_x}{R_d}\\frac{\\partial^2 C}{\\partial x^2} - \\frac{v_x}{R_d}\\frac{\\partial C}{\\partial x}$, where $R_d = 1 + \\frac{\\rho_b}{\\theta} K_d$ is the retardation factor. The aquifer parameters are: seepage velocity $v_x = 0.25\\ \\text{m}/\\text{day}$, longitudinal hydrodynamic dispersion coefficient $D_x = 0.50\\ \\text{m}^2/\\text{day}$, dry bulk density $\\rho_b = 1.65\\ \\text{g}/\\text{cm}^3$, porosity $\\theta = 0.30$, and linear sorption distribution coefficient $K_d = 4.20\\ \\text{cm}^3/\\text{g}$ ($4.20\\ \\text{L}/\\text{kg}$). (a) Calculate the retardation factor $R_d$ and the retarded plume velocity $v_c$. (b) For a continuous point source of arsenic ($C(0,t) = C_0$), use the Ogata-Banks analytical solution approximation $C(x,t) \\approx \\frac{C_0}{2} \\operatorname{erfc}\\left( \\frac{x - v_c t}{2\\sqrt{(D_x/R_d) t}} \\right)$ to determine the time (in years) required for the $50\\%$ breakthrough front ($C/C_0 = 0.50$) to migrate to a municipal tube well located $x = 150\\ \\text{m}$ downgradient. (c) At that arrival time, evaluate the width of the dispersion zone between $C/C_0 = 0.16$ and $0.84$.",
                "hints": [
                    "Calculate $R_d = 1 + (1.65 / 0.30) \\times 4.20$.",
                    "Retarded velocity $v_c = v_x / R_d$.",
                    "For $C/C_0 = 0.50$, the argument of the erfc is zero, so $x = v_c t$."
                ],
                "solution": """**Step 1: Calculate the retardation factor $R_d$ and retarded velocity $v_c$**
Given:
- $\\rho_b = 1.65\\ \\text{g}/\\text{cm}^3$
- $\\theta = 0.30$
- $K_d = 4.20\\ \\text{cm}^3/\\text{g}$
\\[
R_d = 1 + \\frac{\\rho_b}{\\theta} K_d = 1 + \\left( \\frac{1.65}{0.30} \\right)(4.20) = 1 + (5.50)(4.20) = 1 + 23.10 = 24.10
\\]
The retarded migration velocity:
\\[
v_c = \\frac{v_x}{R_d} = \\frac{0.25\\ \\text{m}/\\text{day}}{24.10} = 0.010373\\ \\text{m}/\\text{day}
\\]
In meters per year ($1\\ \\text{year} = 365.25\\ \\text{days}$):
\\[
v_c = 0.010373 \\times 365.25 = 3.789\\ \\text{m}/\\text{year}
\\]

**Step 2: Calculate migration time to $x = 150\\ \\text{m}$ for $50\\%$ breakthrough**
At $C(x,t)/C_0 = 0.50$, $\\operatorname{erfc}(0) = 1$, which requires $x - v_c t = 0$:
\\[
t_{50} = \\frac{x}{v_c} = \\frac{150\\ \\text{m}}{0.010373\\ \\text{m}/\\text{day}} = 14,460.6\\ \\text{days}
\\]
Converting to years:
\\[
t_{50} = \\frac{14,460.6}{365.25} = 39.59\\ \\text{years} \\approx 39.6\\ \\text{years}
\\]

**Step 3: Evaluate dispersion zone width**
The effective dispersion coefficient is:
\\[
D^* = \\frac{D_x}{R_d} = \\frac{0.50\\ \\text{m}^2/\\text{day}}{24.10} = 0.020747\\ \\text{m}^2/\\text{day}
\\]
The characteristic dispersion length scale $\\sigma_x$ at time $t$ is:
\\[
\\sigma_x = \\sqrt{2 D^* t} = \\sqrt{2 \\times 0.020747\\ \\text{m}^2/\\text{day} \\times 14,460.6\\ \\text{days}} = \\sqrt{599.98} = 24.50\\ \\text{m}
\\]
Since $\\operatorname{erfc}(1/\\sqrt{2}) \\approx 0.317$ and $\\operatorname{erfc}(-1/\\sqrt{2}) \\approx 1.683$, the spatial distance between $C/C_0 = 0.16$ and $C/C_0 = 0.84$ spans approximately $2 \\sigma_x$:
\\[
\\Delta x_{16-84} = 2 \\sigma_x = 2(24.50\\ \\text{m}) = 49.0\\ \\text{m}
\\]

**Conclusion**:
The retardation factor is **24.10**, slowing the plume to **$3.79\\ \\text{m}/\\text{year}$**. The $50\\%$ front requires **$39.6\\ \\text{years}$** to reach the tube well, with a transition dispersion width of **$49.0\\ \\text{m}$**."""
            },
            {
                "id": "prob_5_8",
                "tier": "Advanced",
                "title": "Co-precipitation Efficiency in Iron Coagulation via Surface Complexation",
                "statement": "A municipal coagulation plant treats groundwater containing total arsenic $[\\text{As}]_{tot} = 300\\ \\mu\\text{g}/\\text{L}$ ($4.00\\ \\mu\\text{M}$) entirely pre-oxidized to $H_2AsO_4^-$. Coagulant $\\text{FeCl}_3$ is dosed at $10.0\\ \\text{mg Fe}/\\text{L}$ ($0.179\\ \\text{mM Fe}$), precipitating quantitatively as amorphous hydrous ferric oxide (HFO). The specific site density of HFO is $0.20\\ \\text{mol binding sites} / \\text{mol Fe}$. The surface complexation reaction is $\\equiv\\!\\text{FeOH} + H_2AsO_4^- \\rightleftharpoons \\equiv\\!\\text{FeHAsO}_4^- + \\text{H}_2\\text{O}$ with apparent equilibrium conditional constant $K'_{ads} = \\frac{[\\equiv\\!\\text{FeHAsO}_4^-]}{[\\equiv\\!\\text{FeOH}][H_2AsO_4^-]} = 2.50 \\times 10^5\\ \\text{M}^{-1}$. (a) Calculate the total concentration of available surface sites $[\\equiv\\!\\text{FeOH}]_{tot}$. (b) Calculate the residual dissolved arsenic concentration $[\\text{As}]_{aq}$ in $\\mu\\text{g}/\\text{L}$. (c) Verify whether the effluent satisfies the WHO maximum guideline limit of $10\\ \\mu\\text{g}/\\text{L}$.",
                "hints": [
                    "Total surface sites: $[\\equiv\\!\\text{FeOH}]_{tot} = 0.20 \\times [\\text{Fe}]_{precip}$.",
                    "Mass balances: $[\\equiv\\!\\text{FeOH}]_{tot} = [\\equiv\\!\\text{FeOH}] + [\\equiv\\!\\text{FeHAsO}_4^-]$ and $[\\text{As}]_{tot} = [\\text{As}]_{aq} + [\\equiv\\!\\text{FeHAsO}_4^-]$.",
                    "Since sites are in vast excess of arsenic, $[\\equiv\\!\\text{FeOH}] \\approx [\\equiv\\!\\text{FeOH}]_{tot}$."
                ],
                "solution": """**Step 1: Calculate total surface site concentration**
The molar iron concentration is:
\\[
[\\text{Fe}]_{tot} = 0.179\\ \\text{mM} = 1.79 \\times 10^{-4}\\ \\text{M}
\\]
With a site density of $0.20\\ \\text{mol sites} / \\text{mol Fe}$:
\\[
[\\equiv\\!\\text{FeOH}]_{tot} = 0.20 \\times (1.79 \\times 10^{-4}\\ \\text{M}) = 3.58 \\times 10^{-5}\\ \\text{M} = 35.8\\ \\mu\\text{M}
\\]

**Step 2: Formulate surface complexation equilibrium**
Total arsenic concentration:
\\[
[\\text{As}]_{tot} = 4.00\\ \\mu\\text{M} = 4.00 \\times 10^{-6}\\ \\text{M}
\\]
Since $[\\equiv\\!\\text{FeOH}]_{tot} = 35.8\\ \\mu\\text{M} \\gg [\\text{As}]_{tot} = 4.00\\ \\mu\\text{M}$, surface binding sites are in nearly 9-fold excess.
Let $x = [\\equiv\\!\\text{FeHAsO}_4^-]$ be the adsorbed arsenic concentration.
Then:
\\[
[\\text{As}]_{aq} = [\\text{As}]_{tot} - x
\\]
\\[
[\\equiv\\!\\text{FeOH}] = [\\equiv\\!\\text{FeOH}]_{tot} - x
\\]
Substituting into the equilibrium expression:
\\[
K'_{ads} = \\frac{x}{([\\equiv\\!\\text{FeOH}]_{tot} - x)([\\text{As}]_{tot} - x)}
\\]
To obtain high precision, let us test the excess site approximation $[\\equiv\\!\\text{FeOH}] \\approx [\\equiv\\!\\text{FeOH}]_{tot} - x$:
\\[
x = K'_{ads} ([\\equiv\\!\\text{FeOH}]_{tot} - x) [\\text{As}]_{aq}
\\]
Alternatively, express $[\\text{As}]_{aq}$:
\\[
[\\text{As}]_{aq} = \\frac{[\\text{As}]_{tot}}{1 + K'_{ads} [\\equiv\\!\\text{FeOH}]}
\\]
Let us solve the exact quadratic equation:
\\[
K'_{ads} (S_0 - x)(A_0 - x) = x
\\]
Where $S_0 = 3.58 \\times 10^{-5}\\ \\text{M}$ and $A_0 = 4.00 \\times 10^{-6}\\ \\text{M}$:
\\[
x^2 - (S_0 + A_0 + 1/K'_{ads}) x + S_0 A_0 = 0
\\]
\\[
\\frac{1}{K'_{ads}} = \\frac{1}{2.50 \\times 10^5} = 4.00 \\times 10^{-6}\\ \\text{M}
\\]
\\[
b = S_0 + A_0 + \\frac{1}{K'_{ads}} = 3.58 \\times 10^{-5} + 4.00 \\times 10^{-6} + 4.00 \\times 10^{-6} = 4.38 \\times 10^{-5}\\ \\text{M}
\\]
\\[
c = S_0 A_0 = (3.58 \\times 10^{-5})(4.00 \\times 10^{-6}) = 1.432 \\times 10^{-10}\\ \\text{M}^2
\\]
Applying the quadratic formula:
\\[
x = \\frac{b - \\sqrt{b^2 - 4c}}{2}
\\]
\\[
b^2 = (4.38 \\times 10^{-5})^2 = 1.91844 \\times 10^{-9}
\\]
\\[
4c = 4(1.432 \\times 10^{-10}) = 5.728 \\times 10^{-10}
\\]
\\[
b^2 - 4c = 1.91844 \\times 10^{-9} - 0.5728 \\times 10^{-9} = 1.34564 \\times 10^{-9}
\\]
\\[
\\sqrt{b^2 - 4c} = 3.6683 \\times 10^{-5}\\ \\text{M}
\\]
\\[
x = \\frac{4.38 \\times 10^{-5} - 3.6683 \\times 10^{-5}}{2} = \\frac{7.117 \\times 10^{-6}}{2} = 3.5585 \\times 10^{-6}\\ \\text{M}
\\]

**Step 3: Calculate residual aqueous concentration and compliance**
\\[
[\\text{As}]_{aq} = A_0 - x = 4.00 \\times 10^{-6} - 3.5585 \\times 10^{-6} = 4.415 \\times 10^{-7}\\ \\text{M}
\\]
Converting to mass concentration (molar mass of As = $74.922\\ \\text{g}/\\text{mol}$):
\\[
C_{aq} = (4.415 \\times 10^{-7}\\ \\text{mol}/\\text{L}) \\times (74,922\\ \\text{mg}/\\text{mol}) = 0.03308\\ \\text{mg}/\\text{L} = 33.1\\ \\mu\\text{g}/\\text{L}
\\]

**Compliance Evaluation**:
The residual concentration is **$33.1\\ \\mu\\text{g}/\\text{L}$**. This meets the Bangladesh National Standard ($50\\ \\mu\\text{g}/\\text{L}$), but **exceeds the WHO drinking water guideline of $10\\ \\mu\\text{g}/\\text{L}$**. An increased coagulant dose or two-stage filtration is required to achieve compliance with WHO standards."""
            },
            {
                "id": "prob_5_9",
                "tier": "Advanced",
                "title": "Toxicokinetic-Toxicodynamic Model for Methylmercury in Marine Pelagic Predators",
                "statement": "The bioaccumulation kinetics of methylmercury ($CH_3Hg^+$) in a high-trophic pelagic marine fish (Yellowfin tuna) is described by the dynamic differential equation: $\\frac{dC_{fish}}{dt} = k_u C_w + \\alpha F C_{prey} - (k_e + k_g) C_{fish}$, where: water uptake rate $k_u = 120\\ \\text{L}/(\\text{kg}\\cdot\\text{day})$, aqueous concentration $C_w = 2.5 \\times 10^{-6}\\ \\text{mg}/\\text{L}$ ($2.5\\ \\text{pg}/\\text{L}$), assimilation efficiency $\\alpha = 0.85$, mass-specific feeding rate $F = 0.035\\ \\text{kg}_{prey}/(\\text{kg}_{fish}\\cdot\\text{day})$, prey concentration $C_{prey} = 0.40\\ \\text{mg}/\\text{kg}$, depuration elimination rate constant $k_e = 0.0018\\ \\text{day}^{-1}$, and somatic growth dilution rate constant $k_g = 0.0032\\ \\text{day}^{-1}$. (a) Calculate the steady-state methylmercury concentration $C_{fish}^\\infty$ in $\\text{mg}/\\text{kg}$ wet weight. (b) Determine the relative contributions (percentage of total intake) of aqueous direct gill absorption versus dietary ingestion. (c) Calculate the time in days required for a young fish with $C_{fish}(0) = 0.05\\ \\text{mg}/\\text{kg}$ to reach $90\\%$ of its steady-state body burden.",
                "hints": [
                    "At steady-state: $\\frac{dC_{fish}}{dt} = 0 \\implies C_{fish}^\\infty = \\frac{k_u C_w + \\alpha F C_{prey}}{k_e + k_g}$.",
                    "Compare dietary flux $J_{diet} = \\alpha F C_{prey}$ with respiratory gill flux $J_{water} = k_u C_w$.",
                    "Transient solution: $C(t) = C^\\infty - (C^\\infty - C_0) e^{-(k_e + k_g)t}$."
                ],
                "solution": """**Step 1: Calculate intake fluxes and steady-state concentration**
Intake from aqueous gill respiration:
\\[
J_{water} = k_u C_w = (120\\ \\text{L}/(\\text{kg}\\cdot\\text{day})) \\times (2.5 \\times 10^{-6}\\ \\text{mg}/\\text{L}) = 3.00 \\times 10^{-4}\\ \\text{mg}/(\\text{kg}\\cdot\\text{day})
\\]
Intake from dietary prey consumption:
\\[
J_{diet} = \\alpha F C_{prey} = (0.85) \\times (0.035\\ \\text{day}^{-1}) \\times (0.40\\ \\text{mg}/\\text{kg}) = 0.01190\\ \\text{mg}/(\\text{kg}\\cdot\\text{day})
\\]
Total uptake flux:
\\[
J_{tot} = J_{water} + J_{diet} = 0.00030 + 0.01190 = 0.01220\\ \\text{mg}/(\\text{kg}\\cdot\\text{day})
\\]
Total elimination/dilution rate constant:
\\[
k_T = k_e + k_g = 0.0018 + 0.0032 = 0.0050\\ \\text{day}^{-1}
\\]
Steady-state concentration:
\\[
C_{fish}^\\infty = \\frac{J_{tot}}{k_T} = \\frac{0.01220\\ \\text{mg}/(\\text{kg}\\cdot\\text{day})}{0.0050\\ \\text{day}^{-1}} = 2.440\\ \\text{mg}/\\text{kg}
\\]

**Step 2: Determine relative pathway contributions**
Dietary contribution:
\\[
\\%\\text{Diet} = \\frac{J_{diet}}{J_{tot}} \\times 100 = \\frac{0.01190}{0.01220} \\times 100 = 97.54\\%
\\]
Aqueous gill contribution:
\\[
\\%\\text{Gill} = \\frac{J_{water}}{J_{tot}} \\times 100 = \\frac{0.00030}{0.01220} \\times 100 = 2.46\\%
\\]
This confirms that dietary biomagnification accounts for over $97.5\\%$ of toxic body burden in top marine predators.

**Step 3: Calculate time to reach $90\\%$ steady-state burden**
The transient toxicokinetic equation is:
\\[
C(t) = C^\\infty - (C^\\infty - C_0) e^{-k_T t}
\\]
We seek $t_{90}$ such that $C(t_{90}) = 0.90 C^\\infty = 0.90(2.440) = 2.196\\ \\text{mg}/\\text{kg}$:
\\[
2.196 = 2.440 - (2.440 - 0.05) e^{-0.0050 t}
\\]
\\[
2.390 e^{-0.0050 t} = 2.440 - 2.196 = 0.244
\\]
\\[
e^{-0.0050 t} = \\frac{0.244}{2.390} = 0.10209
\\]
Taking the natural logarithm:
\\[
-0.0050 t = \\ln(0.10209) = -2.2819
\\]
\\[
t_{90} = \\frac{2.2819}{0.0050} = 456.4\\ \\text{days} \\approx 1.25\\ \\text{years}
\\]

**Conclusion**:
The steady-state body burden is **$2.44\\ \\text{mg}/\\text{kg}$** (exceeding human health consumption advisory thresholds of $0.5 - 1.0\\ \\text{mg}/\\text{kg}$), driven **$97.5\\%$ by dietary intake**, taking **456 days** to reach $90\\%$ saturation."""
            }
        ]
    }
    return unit

if __name__ == "__main__":
    u5 = get_unit_5()
    print(f"Unit 5 generated: {len(u5['sections'])} sections, {len(u5['problems'])} problems.")
