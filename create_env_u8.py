# -*- coding: utf-8 -*-
"""
Environmental Chemistry - Unit 8 Content Generator
Unit 8: Industrial Effluent Treatment & Advanced Wastewater Engineering
Strictly no marks, no course codes, pure Unix line endings.
"""

import json

def get_unit_8():
    unit = {
        "id": "unit_8",
        "title": "Industrial Effluent Treatment & Advanced Wastewater Engineering",
        "badge": "Unit 08",
        "summary": "Physicochemical and organic profiling of textile, tannery, and chemical industrial effluents; primary physical-chemical operations, Lawrence-McCarty activated sludge bioreactor design, UASB anaerobic digestion, Advanced Oxidation Processes (AOPs), cross-flow membrane separations (UF, NF, RO), and Zero Liquid Discharge (ZLD) engineering.",
        "simulation": {
            "id": "sim_env_activated_sludge_effluent_treatment",
            "title": "Activated Sludge Bioreactor & Effluent Treatment Plant (ETP) Simulator",
            "type": "canvas",
            "description": "Continuous Lawrence-McCarty activated sludge model calculating hydraulic retention time (HRT), mean cell residence time (MCRT / theta_c), food-to-microorganism (F/M) ratio, substrate degradation, and secondary clarifier sludge settling."
        },
        "sections": [
            {
                "id": "sec_8_1",
                "title": "Characterization of Industrial Effluents: Textile, Tannery & Pharmaceutical",
                "content": """Industrial manufacturing generates wastewater streams exhibiting extreme variations in chemical composition, pH, temperature, toxicity, and recalcitrance. Effective treatment facility design requires precise characterization of sector-specific contaminants.

### Sectoral Effluent Profiles
1. **Textile Dyeing and Finishing Effluents**:
   - Characterized by deep chromophoric coloration (synthetic reactive, azo, disperse, and vat dyes), elevated temperatures ($40 - 60^\\circ\\text{C}$), alkaline pH ($9 - 11$), high chemical oxygen demand (COD: $1,500 - 4,000\\ \\text{mg}/\\text{L}$), and high salinity (total dissolved solids, TDS: $5,000 - 15,000\\ \\text{mg}/\\text{L}$) driven by sodium chloride ($NaCl$) and sodium sulfate ($Na_2SO_4$) used as dye exhaustion exhausting electrolytes.
   - Low biodegradability ratio ($\text{BOD}_5 / \\text{COD} \\approx 0.15 - 0.25$), rendering conventional single-stage biological treatment insufficient.
2. **Tannery Effluents**:
   - Beamhouse operations (liming, dehairing, fleshing) release enormous concentrations of dissolved sulfides ($S^{2-}$), proteins, ammonium, and total suspended solids (TSS: $3,000 - 8,000\\ \\text{mg}/\\text{L}$).
   - Tanyard operations discharge acidic effluents laden with toxic basic chromium(III) sulfate ($Cr(OH)SO_4$), requiring segregated physicochemical treatment.
3. **Pharmaceutical & Specialty Chemical Effluents**:
   - Contain recalcitrant Active Pharmaceutical Ingredients (APIs), antibiotics, heterocyclic solvents, and high organohalogen content, frequently displaying acute microbial biocidal activity."""
            },
            {
                "id": "sec_8_2",
                "title": "Primary Treatment Engineering: Equalization, DAF & Coagulation",
                "content": """Primary wastewater operations mitigate hydraulic shock loads, remove coarse suspended solids, and destabilize colloidal organic dispersion before biological processing.

### Flow Equalization Basins
Industrial batch operations cause erratic volumetric flow rates and pollutant surges. Equalization basins operate as completely stirred tanks providing adequate hydraulic retention time ($HRT = 8 - 24\\ \\text{hours}$) to dampen peak loadings:
\\[
V_{eq} = \\int_0^{24} |Q(t) - \\bar{Q}|\\ dt
\\]

### Dissolved Air Flotation (DAF)
DAF separates low-density suspended solids, emulsified oils, and grease ($O\\&G$):
1. A portion of clarified effluent is pressurized to $4 - 6\\ \\text{bar}$ in a retention tank saturated with dissolved air.
2. Pressure release across an injection nozzle nucleates micro-bubbles ($20 - 50\\ \\mu\\text{m}$ diameter) into the contact chamber.
3. Micro-bubbles adhere to hydrophobic flocs, reducing apparent particle density below that of water:
   \\[
   v_t = \\frac{g d_p^2 (\\rho_w - \\rho_p)}{18 \\mu}
   \\]
   The aggregate rises rapidly to the surface according to Stokes' Law, where mechanical scrapers skim off the concentrated float sludge.

### Chemical Coagulation-Flocculation Mechanisms
Colloidal wastewater particles remain suspended due to mutually repulsive electrostatic zeta potentials (typically $-15$ to $-35\\ \\text{mV}$). Chemical coagulant dosing destabilizes colloids via four primary mechanisms:
1. **Double Layer Compression**: High ionic strength suppresses the electrostatic Debye length.
2. **Charge Neutralization**: Cationic multivalent hydrolyzing metal complexes (e.g. $[Al_{13}O_4(OH)_{24}(H_2O)_{12}]^{7+}$ in polyaluminum chloride, PAC) adsorb specifically onto negatively charged colloids, neutralizing net charge.
3. **Enmeshment (Sweep Flocculation)**: Massive hydroxide precipitation ($Fe(OH)_3, Al(OH)_3$) traps non-reactive particles within a dense settling floc blanket.
4. **Inter-particle Bridging**: Long-chain anionic or cationic polyacrylamide polymers anchor simultaneously to multiple flocs, building large macro-flocs."""
            },
            {
                "id": "sec_8_3",
                "title": "Secondary Biological Treatment: Lawrence-McCarty Activated Sludge Design",
                "content": """Secondary treatment relies on a dynamic suspension of heterotrophic microorganisms (activated sludge) in an aerobic bioreactor to oxidize dissolved organic carbon into carbon dioxide and microbial biomass.

### Lawrence-McCarty Steady-State Kinetic Formulation
The system couples Monod microbial growth kinetics with mass balance conservation across a completely mixed aeration basin and secondary clarifier:
1. **Substrate Degradation (Effluent Soluble Substrate, $S$)**:
   \\[
   S = \\frac{K_s (1 + b \\theta_c)}{\\theta_c (Y k - b) - 1}
   \\]
   where:
   - $\\theta_c$: Mean cell residence time / sludge age ($\\text{days}$).
   - $Y$: Biomass synthesis yield coefficient ($\\text{g VSS} / \\text{g substrate}$).
   - $k$: Maximum specific substrate utilization rate ($\\text{day}^{-1}$).
   - $K_s$: Half-velocity constant ($\\text{mg}/\\text{L}$).
   - $b$: Endogenous biomass decay coefficient ($\\text{day}^{-1}$).
   *Fundamental Principle*: Effluent soluble substrate concentration $S$ is strictly governed by sludge age $\\theta_c$, completely independent of influent substrate concentration $S_0$ or hydraulic retention time $\\theta$.
2. **Bioreactor Biomass Concentration ($X$, Mixed Liquor Volatile Suspended Solids, MLVSS)**:
   \\[
   X = \\left( \\frac{\\theta_c}{\\theta} \\right) \\left[ \\frac{Y (S_0 - S)}{1 + b \\theta_c} \\right]
   \\]
   where $\\theta = V / Q$ is hydraulic retention time ($HRT$).
3. **Food-to-Microorganism ($F/M$) Ratio**:
   \\[
   F/M = \\frac{Q \\cdot S_0}{V \\cdot X} = \\frac{S_0}{\\theta \\cdot X} \\quad (\\text{g BOD} / (\\text{g MLVSS} \\cdot \\text{day}))
   \\]
   Typical conventional activated sludge operations maintain $F/M$ between $0.2$ and $0.5\\ \\text{day}^{-1}$ to ensure dense bio-flocculation and prevent filamentous sludge bulking."""
            },
            {
                "id": "sec_8_4",
                "title": "Anaerobic Digestion: UASB Reactors, Methanogenesis & Biogas",
                "content": """Anaerobic biological treatment is ideally suited for high-strength industrial wastewaters ($\text{COD} > 2,000 - 30,000\\ \\text{mg}/\\text{L}$), converting organic pollution directly into combustible methane without requiring expensive electrical aeration energy.

### Multi-Stage Anaerobic Microbial Trophic Cascade
Organic macromolecules undergo sequential bioconversion across four phylogenetically distinct bacterial and archaeal guilds:
1. **Hydrolysis**: Extracellular enzymes (cellulases, proteases, lipases) hydrolyze insoluble polymers into soluble monomers (glucose, amino acids, fatty acids).
2. **Acidogenesis**: Fermentative bacteria convert monomers into volatile fatty acids (VFAs: propionate, butyrate, valerate), lactic acid, alcohols, $H_2$, and $CO_2$.
3. **Acetogenesis**: Syntrophic obligate hydrogen-producing acetogenic bacteria oxidize VFAs into acetate, carbon dioxide, and hydrogen:
   \\[
   \\text{CH}_3\\text{CH}_2\\text{COO}^- + 2\\text{H}_2\\text{O} \\rightleftharpoons \\text{CH}_3\\text{COO}^- + \\text{CO}_2 + 3\\text{H}_2, \\quad \\Delta G^{\\circ'} = +48.1\\ \\text{kJ}/\\text{mol}
   \\]
   *Thermodynamic constraint*: This endergonic reaction proceeds only when hydrogen-consuming methanogens maintain extremely low hydrogen partial pressures ($P_{H2} < 10^{-4}\\ \\text{atm}$).
4. **Methanogenesis**: Strictly anaerobic Euryarchaeota produce methane via two parallel metabolic pathways:
   - *Acetoclastic Methanogenesis* (*Methanosarcina, Methanosaeta*): Cleaves acetate ($70\\%$ of global biogas):
     \\[
     \\text{CH}_3\\text{COOH} \\rightarrow \\text{CH}_4 + \\text{CO}_2
     \\]
   - *Hydrogenotrophic Methanogenesis* (*Methanobacterium*): Reduces $CO_2$ with $H_2$ ($30\\%$ of biogas):
     \\[
     \\text{CO}_2 + 4\\text{H}_2 \\rightarrow \\text{CH}_4 + 2\\text{H}_2\\text{O}
     \\]

### Upflow Anaerobic Sludge Blanket (UASB) Architecture
UASB reactors introduce influent through bottom distribution manifolds, flowing upward through a dense blanket of self-immobilized anaerobic granular sludge (settling velocity $> 30\\ \\text{m}/\\text{h}$). A top three-phase separator (gas-liquid-solid / GLS separator) disengages biogas bubbles, allows clarified effluent discharge, and returns settled granules directly to the sludge bed without requiring mechanical recycling."""
            },
            {
                "id": "sec_8_5",
                "title": "Advanced Oxidation Processes (AOPs): Fenton, Photo-Fenton & Photocatalysis",
                "content": """Advanced Oxidation Processes (AOPs) destroy recalcitrant, non-biodegradable, or toxic xenobiotics by generating the non-selective **hydroxyl radical** ($\\cdot OH$), one of the strongest chemical oxidants known ($E^\\circ = +2.80\\ \\text{V}$ vs SHE).

### The Classical Fenton Reaction
Discovered by H.J.H. Fenton in 1894, the reaction relies on ferrous iron catalyzing hydrogen peroxide decomposition under acidic conditions:
\\[
\\text{Fe}^{2+} + \\text{H}_2\\text{O}_2 \\xrightarrow{k_1} \\text{Fe}^{3+} + \\cdot\\text{OH} + \\text{OH}^-, \\quad k_1 \\approx 76\\ \\text{M}^{-1}\\text{s}^{-1}
\\]
Regeneration of ferrous iron occurs slowly via reduction by hydrogen peroxide:
\\[
\\text{Fe}^{3+} + \\text{H}_2\\text{O}_2 \\xrightarrow{k_2} \\text{Fe}^{2+} + \\text{HO}_2^\\cdot + \\text{H}^+, \\quad k_2 \\approx 0.01\\ \\text{M}^{-1}\\text{s}^{-1}
\\]
Because $k_1 \\gg k_2$, ferric iron accumulates. The system operates optimally in the strict range of **pH 2.8 to 3.2**. At $\\text{pH} > 3.5$, ferric iron hydrolyzes and precipitates as inactive $\\text{Fe(OH)}_3$ sludge; at $\\text{pH} < 2.5$, proton scavenging of hydroxyl radicals ($\cdot\\text{OH} + \\text{H}^+ + e^- \\rightarrow \\text{H}_2\\text{O}$) and formation of stable $[\\text{Fe(H}_2\\text{O})_6]^{3+}$ complexes suppresses radical generation.

### Photo-Fenton Catalysis
Irradiation with near-UV / visible light ($\lambda < 580\\ \\text{nm}$) dramatically accelerates oxidation by inducing photochemical reduction of aqueous ferric complexes:
\\[
[\\text{Fe(OH)}]^{2+} + h\\nu \\rightarrow \\text{Fe}^{2+} + \\cdot\\text{OH}
\\]
This photo-reduction regenerates active $\\text{Fe}^{2+}$ while producing an additional mole of hydroxyl radical.

### Heterogeneous Photocatalysis ($TiO_2/UV$)
When titanium dioxide semiconductor particles are irradiated with UV light exceeding their bandgap energy ($E_g = 3.2\\ \\text{eV}$ for anatase, $\lambda \\le 387\\ \\text{nm}$), electrons are promoted from the valence band ($VB$) to the conduction band ($CB$):
\\[
\\text{TiO}_2 + h\\nu \\rightarrow e^-_{CB} + h^+_{VB}
\\]
The valence band holes ($h^+_{VB}$) possess extreme oxidizing potential ($+2.7\\ \\text{V}$), directly oxidizing surface-adsorbed water and hydroxide ions into hydroxyl radicals:
\\[
h^+_{VB} + \\text{H}_2\\text{O}_{ads} \\rightarrow \\cdot\\text{OH} + \\text{H}^+
\\]"""
            },
            {
                "id": "sec_8_6",
                "title": "Membrane Separation Technologies: MF, UF, NF & Reverse Osmosis",
                "content": """Pressure-driven membrane processes separate solute species across engineered semi-permeable polymeric or ceramic barriers based on molecular size exclusion, steric hindrance, and electrostatic Donnan exclusion.

### Membrane Classification Spectrum
1. **Microfiltration (MF)**:
   - Pore size: $0.1 - 10\\ \\mu\\text{m}$, Operating pressure: $0.1 - 2.0\\ \\text{bar}$.
   - Removes suspended solids, protozoa, and large bacteria; zero salt or color rejection.
2. **Ultrafiltration (UF)**:
   - Pore size: $0.005 - 0.1\\ \\mu\\text{m}$ (Molecular Weight Cut-Off, MWCO: $1,000 - 100,000\\ \\text{Da}$), Pressure: $1 - 5\\ \\text{bar}$.
   - Retains colloidal matter, viruses, proteins, and macro-polymers; serves as critical pretreatment for RO.
3. **Nanofiltration (NF)**:
   - Pore size: $0.001 - 0.005\\ \\mu\\text{m}$ (MWCO: $200 - 1,000\\ \\text{Da}$), Pressure: $3 - 15\\ \\text{bar}$.
   - Negatively charged surface; preferentially rejects multivalent divalent ions ($SO_4^{2-}, Ca^{2+}, Mg^{2+}$) via Donnan exclusion while passing monovalent salts ($NaCl$).
4. **Reverse Osmosis (RO)**:
   - Dense non-porous polyamide thin-film composite (TFC) skin layer, Operating pressure: $15 - 80\\ \\text{bar}$.
   - Rejects $> 99.5\\%$ of all dissolved inorganic ionic species and organic micropollutants.

### Transport Models: Solution-Diffusion
Solvent water flux ($J_w$) across an RO membrane is governed by net driving pressure:
\\[
J_w = A (\\Delta P - \\Delta \\pi)
\\]
where $A$ is the pure water permeability coefficient ($\\text{L}/(\\text{m}^2\\cdot\\text{h}\\cdot\\text{bar})$), $\\Delta P$ is the applied transmembrane hydrostatic pressure, and $\\Delta \\pi = \\pi_{feed} - \\pi_{permeate}$ is osmotic pressure differential, computed via the van 't Hoff equation:
\\[
\\pi = i C R T
\\]
Solute flux ($J_s$) is driven purely by concentration gradient, completely independent of hydraulic pressure:
\\[
J_s = B (C_{feed} - C_{permeate})
\\]
where $B$ is the solute permeability coefficient."""
            },
            {
                "id": "sec_8_7",
                "title": "Chromium Geochemistry in Tannery Effluents: Cr(VI) vs Cr(III)",
                "content": """Tanning chemistry utilizes chromium for cross-linking collagen triple helices, generating effluent streams with high chromium concentrations.

### Oxidation States & Toxicological Divergence
Chromium exists predominantly in two oxidation states exhibiting diametrically opposing environmental properties:
- **Trivalent Chromium [Cr(III)]**:
  - Exists as the hard Lewis acid aqua-cation $[Cr(H_2O)_6]^{3+}$.
  - Readily forms insoluble amorphous hydroxide precipitates ($Cr(OH)_3$) above pH 6.0 ($K_{sp} \\approx 6.3 \\times 10^{-31}$).
  - Low cellular membrane permeability; essential trace nutrient in micro-quantities.
- **Hexavalent Chromium [Cr(VI)]**:
  - Exists as soluble oxyanions: chromate ($CrO_4^{2-}$) and dichromate ($Cr_2O_7^{2-}$):
    \\[
    2CrO_4^{2-} + 2H^+ \\rightleftharpoons Cr_2O_7^{2-} + H_2O, \\quad K = 4.2 \\times 10^{14}
    \\]
  - Structural analogue to sulfate ($SO_4^{2-}$); actively transported through cellular sulfate permease channels.
  - Potent mutagen, teratogen, and Class 1 human carcinogen, inducing intracellular DNA cross-linking.

### Chemical Reduction and Precipitation Engineering
To remediate chromium-laden tannery wastewater, any incidental or deliberate $\\text{Cr(VI)}$ must be chemically reduced to $\\text{Cr(III)}$ prior to alkaline neutralization:
1. **Acidification**: Effluent is acidified to $\\text{pH } 2.0 - 2.5$ using sulfuric acid ($H_2SO_4$).
2. **Chemical Reduction**: Ferrous sulfate ($\\text{FeSO}_4$) or sodium metabisulfite ($\\text{Na}_2\\text{S}_2\\text{O}_5$) is added:
   \\[
   \\text{Cr}_2\\text{O}_7^{2-} + 6\\text{Fe}^{2+} + 14\\text{H}^+ \\rightarrow 2\\text{Cr}^{3+} + 6\\text{Fe}^{3+} + 7\\text{H}_2\\text{O}
   \\]
   \\[
   2\\text{Cr}_2\\text{O}_7^{2-} + 3\\text{S}_2\\text{O}_5^{2-} + 10\\text{H}^+ \\rightarrow 4\\text{Cr}^{3+} + 6\\text{SO}_4^{2-} + 5\\text{H}_2\\text{O}
   \\]
3. **Alkaline Neutralization and Precipitation**: Lime ($\\text{Ca(OH)}_2$) or caustic soda ($\\text{NaOH}$) is dosed to adjust pH to $8.5 - 9.0$:
   \\[
   \\text{Cr}^{3+} + 3\\text{OH}^- \\rightarrow \\text{Cr(OH)}_3\\text{(s)} \\downarrow
   \\]
   The settled hydroxide cake is dewatered via filter presses and stabilized in hazardous landfill facilities or recycled back into chromium tanning liquor via acid digestion."""
            },
            {
                "id": "sec_8_8",
                "title": "Zero Liquid Discharge (ZLD) Systems & Industrial Water Reclamation",
                "content": """Zero Liquid Discharge (ZLD) represents the pinnacle of industrial wastewater sustainability, eliminating all liquid effluent discharge while recovering $> 95 - 98\\%$ of purified water for manufacturing reuse.

### Comprehensive ZLD Process Flowsheet Architecture
A state-of-the-art textile or chemical ZLD facility integrates physical, biological, membrane, and thermal operations:
1. **Biological Pre-treatment**: Membrane Bioreactor (MBR) combining activated sludge aeration with submerged microfiltration membranes, achieving complete TSS removal and COD reduction down to $< 50\\ \\text{mg}/\\text{L}$.
2. **Polishing & Color Removal**: Fixed-bed granular activated carbon (GAC) or ozone contactors eliminate trace residual refractory organics, protecting downstream reverse osmosis membranes from organic fouling.
3. **Multi-Stage High-Recovery RO System**:
   - Primary and Secondary Brackish Water RO (BWRO) units operating at recoveries of $75 - 85\\%$.
   - High-Pressure RO (HPRO / Disc-Tube RO) operating up to $120\\ \\text{bar}$ concentrating the brine up to $100,000 - 140,000\\ \\text{mg}/\\text{L}$ TDS.
4. **Thermal Brine Concentration**:
   - **Mechanical Vapor Recompression (MVR) Brine Falling Film Evaporators**: Compresses evaporated steam mechanically to elevate its saturation temperature, reusing latent heat of vaporization to concentrate brine to near saturation ($250,000 - 300,000\\ \\text{mg}/\\text{L}$ TDS).
5. **Crystallization & Solid Salt Recovery**:
   - Forced circulation crystallizers precipitate sodium sulfate ($Na_2SO_4$) and sodium chloride ($NaCl$) crystals.
   - Centrifuges and drying ovens produce high-purity dry industrial salt cakes suitable for reuse in textile dyeing baths, closing the material loop."""
            }
        ],
        "problems": [
            {
                "id": "prob_8_1",
                "tier": "Foundational",
                "title": "Equalization Basin Volume and Peak COD Dampening Integration",
                "statement": "A textile dyeing mill operates over an 8-hour shift producing fluctuating wastewater flows and COD loadings recorded hourly: Hour 1: $60\\ \\text{m}^3/\\text{h}$, $2500\\ \\text{mg}/\\text{L}$; Hour 2: $90\\ \\text{m}^3/\\text{h}$, $3200\\ \\text{mg}/\\text{L}$; Hour 3: $120\\ \\text{m}^3/\\text{h}$, $3800\\ \\text{mg}/\\text{L}$; Hour 4: $140\\ \\text{m}^3/\\text{h}$, $4000\\ \\text{mg}/\\text{L}$; Hour 5: $110\\ \\text{m}^3/\\text{h}$, $3000\\ \\text{mg}/\\text{L}$; Hour 6: $80\\ \\text{m}^3/\\text{h}$, $2200\\ \\text{mg}/\\text{L}$; Hour 7: $50\\ \\text{m}^3/\\text{h}$, $1800\\ \\text{mg}/\\text{L}$; Hour 8: $70\\ \\text{m}^3/\\text{h}$, $2100\\ \\text{mg}/\\text{L}$. The downstream biological treatment plant requires a constant average flow rate $\\bar{Q}$. (a) Calculate the total 8-hour volume $V_{tot}$, the constant pumped outflow rate $\\bar{Q}$ (in $\\text{m}^3/\\text{h}$), and the flow-weighted average influent COD concentration $\\overline{\\text{COD}}$. (b) Determine the minimum active equalization basin storage capacity $V_{eq}$ (in $\\text{m}^3$) required to balance the hourly flow variations using cumulative volume mass analysis.",
                "hints": [
                    "Sum $Q_i$ and calculate $\\bar{Q} = V_{tot} / 8$.",
                    "Flow-weighted COD: $\\overline{\\text{COD}} = \\frac{\\sum (Q_i \\cdot COD_i)}{V_{tot}}$.",
                    "Cumulative volume difference: Track $\\Delta V_i = \\sum_{j=1}^i (Q_j - \\bar{Q})$. Required volume is $(\\Delta V)_{max} - (\\Delta V)_{min}$."
                ],
                "solution": """**Step 1: Calculate total volume and constant outflow rate $\\bar{Q}$**
Hourly flow rates: $[60, 90, 120, 140, 110, 80, 50, 70]\\ \\text{m}^3/\\text{h}$.
\\[
V_{tot} = 60 + 90 + 120 + 140 + 110 + 80 + 50 + 70 = 720\\ \\text{m}^3
\\]
The constant pumping rate over the 8-hour period:
\\[
\\bar{Q} = \\frac{720\\ \\text{m}^3}{8\\ \\text{h}} = 90.0\\ \\text{m}^3/\\text{h}
\\]

**Step 2: Calculate flow-weighted average COD concentration**
Total mass of COD entering:
\\[
M_{COD} = \\sum (Q_i \\times COD_i)
\\]
- Hour 1: $60 \\times 2500 = 150,000\\ \\text{g}$
- Hour 2: $90 \\times 3200 = 288,000\\ \\text{g}$
- Hour 3: $120 \\times 3800 = 456,000\\ \\text{g}$
- Hour 4: $140 \\times 4000 = 560,000\\ \\text{g}$
- Hour 5: $110 \\times 3000 = 330,000\\ \\text{g}$
- Hour 6: $80 \\times 2200 = 176,000\\ \\text{g}$
- Hour 7: $50 \\times 1800 = 90,000\\ \\text{g}$
- Hour 8: $70 \\times 2100 = 147,000\\ \\text{g}$
\\[
M_{COD} = 150 + 288 + 456 + 560 + 330 + 176 + 90 + 147 = 2,197,000\\ \\text{g} = 2,197\\ \\text{kg}
\\]
The flow-weighted concentration:
\\[
\\overline{\\text{COD}} = \\frac{2,197,000\\ \\text{g}}{720\\ \\text{m}^3} = 3,051.4\\ \\text{g}/\\text{m}^3 = 3,051.4\\ \\text{mg}/\\text{L}
\\]

**Step 3: Determine required equalization volume via mass curve analysis**
Calculate cumulative deviation from constant discharge ($Q_i - \\bar{Q}$):
- Hour 1: $60 - 90 = -30\\ \\text{m}^3 \\implies \\text{Cum} = -30\\ \\text{m}^3$
- Hour 2: $90 - 90 = 0\\ \\text{m}^3 \\implies \\text{Cum} = -30\\ \\text{m}^3$
- Hour 3: $120 - 90 = +30\\ \\text{m}^3 \\implies \\text{Cum} = 0\\ \\text{m}^3$
- Hour 4: $140 - 90 = +50\\ \\text{m}^3 \\implies \\text{Cum} = +50\\ \\text{m}^3$
- Hour 5: $110 - 90 = +20\\ \\text{m}^3 \\implies \\text{Cum} = +70\\ \\text{m}^3$ (Maximum surplus)
- Hour 6: $80 - 90 = -10\\ \\text{m}^3 \\implies \\text{Cum} = +60\\ \\text{m}^3$
- Hour 7: $50 - 90 = -40\\ \\text{m}^3 \\implies \\text{Cum} = +20\\ \\text{m}^3$
- Hour 8: $70 - 90 = -20\\ \\text{m}^3 \\implies \\text{Cum} = 0\\ \\text{m}^3$

The maximum cumulative excess: $(\\Delta V)_{max} = +70\\ \\text{m}^3$.
The maximum cumulative deficit: $(\\Delta V)_{min} = -30\\ \\text{m}^3$.
The minimum active equalization storage volume required:
\\[
V_{eq} = (\\Delta V)_{max} - (\\Delta V)_{min} = 70 - (-30) = 100\\ \\text{m}^3
\\]

**Conclusion**:
The average outflow is **$90.0\\ \\text{m}^3/\\text{h}$**, flow-weighted COD is **$3,051\\ \\text{mg}/\\text{L}$**, and minimum active basin capacity is **$100\\ \\text{m}^3$**."""
            },
            {
                "id": "prob_8_2",
                "tier": "Foundational",
                "title": "Coagulation-Flocculation Alum Dosing and Alkalinity Consumption",
                "statement": "An industrial wastewater stream of $Q = 2400\\ \\text{m}^3/\\text{day}$ is treated with commercial alum (hydrated aluminum sulfate, $\\text{Al}_2(\\text{SO}_4)_3 \\cdot 14\\text{H}_2\\text{O}$, molar mass $594.36\\ \\text{g}/\\text{mol}$) at an optimal coagulation dose of $80.0\\ \\text{mg}/\\text{L}$. Alum reacts quantitatively with natural bicarbonate alkalinity according to: $\\text{Al}_2(\\text{SO}_4)_3 \\cdot 14\\text{H}_2\\text{O} + 6\\text{HCO}_3^- \\rightarrow 2\\text{Al(OH)}_3\\text{(s)} + 3\\text{SO}_4^{2-} + 6\\text{CO}_2 + 14\\text{H}_2\\text{O}$. (a) Calculate the daily mass of alum consumed in kilograms per day. (b) Calculate the mass of alkalinity consumed per milligram of alum dosed, expressed as $\\text{mg } \\text{CaCO}_3 / \\text{mg alum}$ (molar mass $\\text{CaCO}_3 = 100.09\\ \\text{g}/\\text{mol}$). (c) If the raw wastewater has an initial alkalinity of $45.0\\ \\text{mg}/\\text{L}$ as $\\text{CaCO}_3$, calculate the residual alkalinity, and verify if hydrated lime ($\\text{Ca(OH)}_2$) addition is needed to maintain a minimum buffering reserve of $20.0\\ \\text{mg}/\\text{L}$ as $\\text{CaCO}_3$.",
                "hints": [
                    "Daily alum mass: $M_{alum} = Q \\times \\text{Dose}$.",
                    "Stoichiometry: $1\\ \\text{mol alum}$ consumes $6\\ \\text{mol } \\text{HCO}_3^-$ equivalent to $3\\ \\text{mol } \\text{CaCO}_3$ ($300.27\\ \\text{g}$).",
                    "Calculate alkalinity consumed $= \\text{Dose} \\times (\\text{ratio})$.",
                    "Compare residual alkalinity with 20 mg/L."
                ],
                "solution": """**Step 1: Calculate daily mass of commercial alum**
Given $Q = 2400\\ \\text{m}^3/\\text{day}$ and $\\text{Dose} = 80.0\\ \\text{mg}/\\text{L} = 80.0\\ \\text{g}/\\text{m}^3$:
\\[
M_{alum} = 2400\\ \\text{m}^3/\\text{day} \\times 80.0\\ \\text{g}/\\text{m}^3 = 192,000\\ \\text{g}/\\text{day} = 192.0\\ \\text{kg/day}
\\]

**Step 2: Calculate stoichiometric alkalinity consumption**
From the balanced chemical reaction:
\\[
\\text{Al}_2(\\text{SO}_4)_3 \\cdot 14\\text{H}_2\\text{O} + 6\\text{HCO}_3^- \\rightarrow 2\\text{Al(OH)}_3\\text{(s)} + 3\\text{SO}_4^{2-} + 6\\text{CO}_2 + 14\\text{H}_2\\text{O}
\\]
$1\\ \\text{mol of alum}$ ($594.36\\ \\text{g}$) consumes $6\\ \\text{mol of } \\text{HCO}_3^-$.
In standard environmental water quality units, alkalinity is reported as equivalent $\\text{CaCO}_3$.
Since $1\\ \\text{mol of } \\text{CaCO}_3$ ($100.09\\ \\text{g}$) neutralizes $2\\ \\text{mol of } H^+$ (or accepts $2\\ \\text{moles of charge}$):
\\[
6\\ \\text{mol } \\text{HCO}_3^- \\equiv 3\\ \\text{mol } \\text{CaCO}_3 = 3 \\times 100.09\\ \\text{g} = 300.27\\ \\text{g } \\text{CaCO}_3
\\]
The mass ratio of alkalinity consumption:
\\[
\\frac{\\text{Mass } \\text{CaCO}_3}{\\text{Mass alum}} = \\frac{300.27}{594.36} = 0.5052\\ \\text{mg } \\text{CaCO}_3 / \\text{mg alum}
\\]

**Step 3: Calculate alkalinity depletion and supplemental lime requirement**
Alum dose is $80.0\\ \\text{mg}/\\text{L}$:
\\[
\\Delta \\text{Alk} = 80.0\\ \\text{mg}/\\text{L alum} \\times 0.5052 = 40.42\\ \\text{mg}/\\text{L as } \\text{CaCO}_3
\\]
Residual alkalinity:
\\[
\\text{Alk}_{res} = \\text{Alk}_0 - \\Delta \\text{Alk} = 45.0 - 40.42 = 4.58\\ \\text{mg}/\\text{L as } \\text{CaCO}_3
\\]
Because the residual alkalinity ($4.58\\ \\text{mg}/\\text{L}$) falls far below the minimum safe buffering limit of $20.0\\ \\text{mg}/\\text{L}$, pH will drop sharply into the acidic range, impairing floc formation.
Alkalinity deficit to be made up by hydrated lime:
\\[
\\text{Deficit} = 20.0 - 4.58 = 15.42\\ \\text{mg}/\\text{L as } \\text{CaCO}_3
\\]

**Conclusion**:
The mill consumes **$192.0\\ \\text{kg/day}$ of alum**. Each mg of alum destroys **$0.505\\ \\text{mg } \\text{CaCO}_3$**, leaving a meager **$4.58\\ \\text{mg}/\\text{L}$ residual alkalinity**. Supplemental lime dosing of at least **$15.4\\ \\text{mg}/\\text{L as } \\text{CaCO}_3$** is mandatory."""
            },
            {
                "id": "prob_8_3",
                "tier": "Foundational",
                "title": "Tannery Chrome Reduction Stoichiometry via Sodium Metabisulfite",
                "statement": "Spent tannery chrome bath liquor has a volume of $V = 15.0\\ \\text{m}^3$ and contains hexavalent chromium at $[\text{Cr(VI)}] = 420.0\\ \\text{mg}/\\text{L}$. Reduction to trivalent chromium is carried out using commercial sodium metabisulfite ($\\text{Na}_2\\text{S}_2\\text{O}_5$, $96.0\\%$ purity, molar mass $190.11\\ \\text{g}/\\text{mol}$) under acidic conditions according to: $2\\text{Cr}_2\\text{O}_7^{2-} + 3\\text{S}_2\\text{O}_5^{2-} + 10\\text{H}^+ \\rightarrow 4\\text{Cr}^{3+} + 6\\text{SO}_4^{2-} + 5\\text{H}_2\\text{O}$ (noting that $1\\ \\text{mol } \\text{Cr}_2\\text{O}_7^{2-}$ contains $2\\ \\text{mol of Cr}$). (a) Calculate the total mass of $\\text{Cr(VI)}$ present in the batch in kilograms. (b) Determine the stoichiometric mass ratio of pure $\\text{Na}_2\\text{S}_2\\text{O}_5$ to $\\text{Cr(VI)}$ (in $\\text{g } \\text{Na}_2\\text{S}_2\\text{O}_5 / \\text{g Cr}$). (c) Calculate the actual required mass of commercial $96.0\\%$ metabisulfite including a $15\\%$ excess to drive the reaction to completion.",
                "hints": [
                    "Total Cr mass: $m_{Cr} = V \\times C$.",
                    "From stoichiometry: $4\\ \\text{mol Cr}$ ($4 \\times 52.00\\ \\text{g} = 208.0\\ \\text{g}$) requires $3\\ \\text{mol } \\text{Na}_2\\text{S}_2\\text{O}_5$ ($3 \\times 190.11\\ \\text{g} = 570.33\\ \\text{g}$).",
                    "Apply the $15\\%$ excess factor ($1.15$) and purity ($0.96$)."
                ],
                "solution": """**Step 1: Calculate total mass of $\\text{Cr(VI)}$**
Given $V = 15.0\\ \\text{m}^3 = 15,000\\ \\text{L}$ and $[\text{Cr(VI)}] = 420.0\\ \\text{mg}/\\text{L} = 0.420\\ \\text{g}/\\text{L}$:
\\[
m_{Cr} = 15,000\\ \\text{L} \\times 0.420\\ \\text{g}/\\text{L} = 6,300\\ \\text{g} = 6.300\\ \\text{kg of Cr(VI)}
\\]

**Step 2: Determine stoichiometric mass ratio**
From the balanced redox equation:
\\[
2\\text{Cr}_2\\text{O}_7^{2-} + 3\\text{S}_2\\text{O}_5^{2-} + 10\\text{H}^+ \\rightarrow 4\\text{Cr}^{3+} + 6\\text{SO}_4^{2-} + 5\\text{H}_2\\text{O}
\\]
$4\\ \\text{moles of Cr atoms}$ ($4 \\times 51.996\\ \\text{g}/\\text{mol} = 207.984\\ \\text{g}$) react with $3\\ \\text{moles of } \\text{Na}_2\\text{S}_2\\text{O}_5$ ($3 \\times 190.107\\ \\text{g}/\\text{mol} = 570.321\\ \\text{g}$).
The theoretical stoichiometric mass ratio:
\\[
\\text{Ratio} = \\frac{570.321\\ \\text{g } \\text{Na}_2\\text{S}_2\\text{O}_5}{207.984\\ \\text{g Cr}} = 2.7421\\ \\text{g } \\text{Na}_2\\text{S}_2\\text{O}_5 / \\text{g Cr}
\\]

**Step 3: Calculate actual required commercial reagent mass**
Theoretical pure mass:
\\[
m_{pure} = 6.300\\ \\text{kg Cr} \\times 2.7421 = 17.275\\ \\text{kg } \\text{Na}_2\\text{S}_2\\text{O}_5
\\]
Applying $15\\%$ excess ($1.15$) and accounting for $96.0\\%$ purity ($0.960$):
\\[
m_{commercial} = \\frac{17.275\\ \\text{kg} \\times 1.15}{0.960} = \\frac{19.866\\ \\text{kg}}{0.960} = 20.694\\ \\text{kg} \\approx 20.7\\ \\text{kg}
\\]

**Conclusion**:
The batch contains **$6.30\\ \\text{kg of Cr(VI)}$**, requiring **$20.7\\ \\text{kg}$** of commercial sodium metabisulfite for complete chemical reduction to harmless Cr(III)."""
            },
            {
                "id": "prob_8_4",
                "tier": "Intermediate",
                "title": "Lawrence-McCarty Activated Sludge Design for Textile Wastewater",
                "statement": "An activated sludge ETP treats textile effluent with flow rate $Q = 3600\\ \\text{m}^3/\\text{day}$ and influent soluble $\\text{BOD}_5$ $S_0 = 850\\ \\text{mg}/\\text{L}$. Environmental discharge regulations mandate effluent soluble BOD $S \\le 25\\ \\text{mg}/\\text{L}$. Biological kinetic parameters are: synthesis yield $Y = 0.50\\ \\text{g VSS}/\\text{g BOD}$, maximum utilization rate $k = 4.0\\ \\text{day}^{-1}$, half-velocity constant $K_s = 60\\ \\text{mg}/\\text{L}$, and endogenous decay coefficient $b = 0.060\\ \\text{day}^{-1}$. The target MLVSS concentration in the aeration tank is maintained at $X = 3000\\ \\text{mg}/\\text{L}$ ($3.0\\ \\text{kg}/\\text{m}^3$). (a) Calculate the minimum mean cell residence time (sludge age, $\\theta_c$) required to achieve $S = 25\\ \\text{mg}/\\text{L}$. (b) Calculate the required aeration basin volume $V$ (in $\\text{m}^3$) and hydraulic retention time $\\theta$ (in hours). (c) Calculate the food-to-microorganism ($F/M$) ratio and daily excess biological sludge production $P_x$ (in $\\text{kg VSS}/\\text{day}$).",
                "hints": [
                    "Invert Lawrence-McCarty equation for $\\theta_c$: $S = \\frac{K_s(1 + b \\theta_c)}{\\theta_c(Y k - b) - 1}$.",
                    "Compute $\\theta = \\frac{\\theta_c Y(S_0 - S)}{X(1 + b \\theta_c)}$, then $V = Q \\cdot \\theta$.",
                    "$F/M = \\frac{Q S_0}{V X}$ and $P_x = \\frac{V X}{\\theta_c}$."
                ],
                "solution": """**Step 1: Calculate required mean cell residence time $\\theta_c$**
From the Lawrence-McCarty substrate equation:
\\[
S = \\frac{K_s (1 + b \\theta_c)}{\\theta_c (Y k - b) - 1}
\\]
Given:
- $S = 25\\ \\text{mg}/\\text{L}$
- $K_s = 60\\ \\text{mg}/\\text{L}$
- $Y = 0.50$
- $k = 4.0\\ \\text{day}^{-1} \\implies Y k = (0.50)(4.0) = 2.0\\ \\text{day}^{-1}$
- $b = 0.060\\ \\text{day}^{-1} \\implies Y k - b = 2.0 - 0.060 = 1.940\\ \\text{day}^{-1}$

Rearranging to solve for $\\theta_c$:
\\[
S [\\theta_c (Y k - b) - 1] = K_s (1 + b \\theta_c)
\\]
\\[
25 [1.940 \\theta_c - 1] = 60 [1 + 0.060 \\theta_c]
\\]
\\[
48.50 \\theta_c - 25 = 60 + 3.60 \\theta_c
\\]
\\[
48.50 \\theta_c - 3.60 \\theta_c = 60 + 25
\\]
\\[
44.90 \\theta_c = 85 \\implies \\theta_c = \\frac{85}{44.90} = 1.893\\ \\text{days}
\\]
To ensure a robust safety factor against shock loads and provide excellent bio-flocculation, engineering practice applies a design factor of $3.5 \\times$:
\\[
\\theta_{c, design} = 3.5 \\times 1.893 = 6.626\\ \\text{days} \\approx 6.63\\ \\text{days}
\\]
At $\\theta_c = 6.63\\ \\text{days}$, effluent soluble BOD drops to:
\\[
S = \\frac{60 [1 + 0.060(6.63)]}{6.63(1.940) - 1} = \\frac{60(1.3978)}{12.862 - 1} = \\frac{83.87}{11.862} = 7.07\\ \\text{mg}/\\text{L} \\quad (\\ll 25\\ \\text{mg}/\\text{L})
\\]

**Step 2: Calculate aeration basin volume and hydraulic retention time**
Using the design sludge age $\\theta_c = 6.63\\ \\text{days}$ with $X = 3000\\ \\text{mg}/\\text{L}$, $S_0 = 850\\ \\text{mg}/\\text{L}$, and $S = 7.1\\ \\text{mg}/\\text{L}$:
\\[
\\theta = \\left( \\frac{\\theta_c}{X} \\right) \\left[ \\frac{Y (S_0 - S)}{1 + b \\theta_c} \\right]
\\]
\\[
\\theta = \\left( \\frac{6.63}{3000} \\right) \\left[ \\frac{0.50 (850 - 7.1)}{1 + 0.060(6.63)} \\right] = (0.00221) \\left[ \\frac{421.45}{1.3978} \\right] = (0.00221)(301.51) = 0.6663\\ \\text{days}
\\]
In hours:
\\[
\\theta = 0.6663 \\times 24\\ \\text{h} = 15.99\\ \\text{hours} \\approx 16.0\\ \\text{hours}
\\]
Aeration basin volume:
\\[
V = Q \\times \\theta = 3600\\ \\text{m}^3/\\text{day} \\times 0.6663\\ \\text{days} = 2,398.7\\ \\text{m}^3 \\approx 2,400\\ \\text{m}^3
\\]

**Step 3: Calculate $F/M$ ratio and daily sludge production $P_x$**
\\[
F/M = \\frac{Q S_0}{V X} = \\frac{3600\\ \\text{m}^3/\\text{day} \\times 0.850\\ \\text{kg}/\\text{m}^3}{2400\\ \\text{m}^3 \\times 3.0\\ \\text{kg}/\\text{m}^3} = \\frac{3060\\ \\text{kg BOD}/\\text{day}}{7200\\ \\text{kg MLVSS}} = 0.425\\ \\text{day}^{-1}
\\]
Daily biological excess waste sludge ($P_x$):
\\[
P_x = \\frac{V X}{\\theta_c} = \\frac{7200\\ \\text{kg VSS}}{6.63\\ \\text{days}} = 1,085.9\\ \\text{kg VSS/day}
\\]

**Conclusion**:
The system requires an aeration basin of **$2,400\\ \\text{m}^3$** ($HRT = 16.0\\ \\text{h}$), operating at an $F/M$ of **$0.425\\ \\text{day}^{-1}$**, producing **$1,086\\ \\text{kg VSS/day}$** of excess secondary sludge."""
            },
            {
                "id": "prob_8_5",
                "tier": "Intermediate",
                "title": "UASB Bioreactor Design and Methane Biogas Energy Yield",
                "statement": "An Upflow Anaerobic Sludge Blanket (UASB) reactor processes high-strength distillery wash: wastewater flow $Q = 1200\\ \\text{m}^3/\\text{day}$ with soluble COD $S_0 = 12,000\\ \\text{mg}/\\text{L}$ ($12.0\\ \\text{kg}/\\text{m}^3$). Design volumetric loading rate is $VLR = 8.0\\ \\text{kg COD}/(\\text{m}^3\\cdot\\text{day})$ with an achieved COD removal efficiency of $\\eta = 82.0\\%$. (a) Calculate the required active liquid volume of the UASB reactor $V$ and the hydraulic retention time $\\theta$ (in hours). (b) At standard conditions ($0^\\circ\\text{C}, 1\\ \\text{atm}$), $1.0\\ \\text{kg of COD}$ converted yields stoichiometrically $0.350\\ \\text{m}^3$ of pure methane gas ($CH_4$). Correcting to the mesophilic operating temperature of $35^\\circ\\text{C}$ ($308.15\\ \\text{K}$), calculate the daily volume of pure $CH_4$ produced in $\\text{m}^3/\\text{day}$. (c) If the biogas contains $65.0\\%\\ CH_4$ by volume and the lower heating value of methane is $35.8\\ \\text{MJ}/\\text{m}^3$ at $35^\\circ\\text{C}$, calculate the daily thermal energy recovery potential in gigajoules (GJ/day).",
                "hints": [
                    "Total daily COD load: $L_{COD} = Q \\times S_0$.",
                    "Reactor volume: $V = L_{COD} / VLR$.",
                    "COD removed: $\\Delta COD = L_{COD} \\times \\eta$.",
                    "Temperature correction: $V_{CH4}(35^\\circ\\text{C}) = V_{STP} \\times (308.15 / 273.15)$."
                ],
                "solution": """**Step 1: Calculate required UASB reactor volume and HRT**
Total daily COD mass loading:
\\[
L_{COD} = Q \\times S_0 = 1200\\ \\text{m}^3/\\text{day} \\times 12.0\\ \\text{kg}/\\text{m}^3 = 14,400\\ \\text{kg COD/day}
\\]
With design volumetric loading rate $VLR = 8.0\\ \\text{kg COD}/(\\text{m}^3\\cdot\\text{day})$:
\\[
V = \\frac{L_{COD}}{VLR} = \\frac{14,400\\ \\text{kg/day}}{8.0\\ \\text{kg}/(\\text{m}^3\\cdot\\text{day})} = 1,800\\ \\text{m}^3
\\]
Hydraulic retention time:
\\[
\\theta = \\frac{V}{Q} = \\frac{1800\\ \\text{m}^3}{1200\\ \\text{m}^3/\\text{day}} = 1.50\\ \\text{days} = 36.0\\ \\text{hours}
\\]

**Step 2: Calculate daily methane generation at $35^\\circ\\text{C}$**
Total COD destroyed:
\\[
\\Delta COD = L_{COD} \\times \\eta = 14,400\\ \\text{kg/day} \\times 0.820 = 11,808\\ \\text{kg COD removed/day}
\\]
At STP ($0^\\circ\\text{C}$, $1\\ \\text{atm}$), theoretical methane yield is $0.350\\ \\text{m}^3/\\text{kg COD}$:
\\[
V_{CH4, STP} = 11,808\\ \\text{kg/day} \\times 0.350\\ \\text{m}^3/\\text{kg} = 4,132.8\\ \\text{m}^3/\\text{day}
\\]
Adjusting for thermal expansion at $35^\\circ\\text{C}$ ($308.15\\ \\text{K}$):
\\[
V_{CH4, 35^\\circ C} = 4,132.8 \\times \\left( \\frac{308.15\\ \\text{K}}{273.15\\ \\text{K}} \\right) = 4,132.8 \\times 1.1281 = 4,662.3\\ \\text{m}^3/\\text{day}
\\]

**Step 3: Calculate energy generation potential**
Total biogas volume ($65.0\\%\\ CH_4$):
\\[
V_{biogas} = \\frac{4,662.3\\ \\text{m}^3/\\text{day}}{0.650} = 7,172.8\\ \\text{m}^3/\\text{day}
\\]
Daily thermal energy produced from methane ($LHV = 35.8\\ \\text{MJ}/\\text{m}^3$):
\\[
E_{thermal} = 4,662.3\\ \\text{m}^3/\\text{day} \\times 35.8\\ \\text{MJ}/\\text{m}^3 = 166,910\\ \\text{MJ/day} = 166.91\\ \\text{GJ/day}
\\]
In continuous thermal power equivalent ($1\\ \\text{day} = 86,400\\ \\text{s}$):
\\[
P = \\frac{166.91 \\times 10^9\\ \\text{J}}{86,400\\ \\text{s}} = 1.932 \\times 10^6\\ \\text{W} = 1.93\\ \\text{MW}_{th}
\\]

**Conclusion**:
The UASB volume is **$1,800\\ \\text{m}^3$** ($HRT = 36\\ \\text{h}$), generating **$4,662\\ \\text{m}^3/\\text{day}$ of pure methane**, yielding **$166.9\\ \\text{GJ/day}$** ($1.93\\ \\text{MW}$ thermal power)."""
            },
            {
                "id": "prob_8_6",
                "tier": "Intermediate",
                "title": "Advanced Oxidation Destruction Kinetics of Recalcitrant Azo Dyes",
                "statement": "The destruction of a recalcitrant textile azo dye (Reactive Red 120, $D$) in a Photo-Fenton batch reactor follows second-order kinetics with hydroxyl radicals: $-\\frac{d[D]}{dt} = k_{OH} [\\cdot OH]_{ss} [D]$, where the second-order rate constant is $k_{OH} = 4.80 \\times 10^9\\ \\text{M}^{-1}\\text{s}^{-1}$. In the illuminated reactor, steady-state hydroxyl radical concentration is maintained at $[\\cdot OH]_{ss} = 2.50 \\times 10^{-12}\\ \\text{M}$. (a) Calculate the pseudo-first-order rate constant $k_{obs}$ in $\\text{s}^{-1}$ and $\\text{min}^{-1}$. (b) Calculate the dye half-life $t_{1/2}$ in minutes. (c) If natural chloride ions present in the dyeing bath ($[Cl^-] = 0.050\\ \\text{M}$) scavenge hydroxyl radicals via $\\cdot OH + Cl^- \\rightarrow ClOH^{\\cdot-}$ ($k_{scav} = 4.30 \\times 10^9\\ \\text{M}^{-1}\\text{s}^{-1}$), depressing $[\\cdot OH]_{ss}$ by $70.0\\%$, calculate the new reaction time required to achieve $99.0\\%$ color removal.",
                "hints": [
                    "$k_{obs} = k_{OH} [\\cdot OH]_{ss}$.",
                    "Half-life: $t_{1/2} = \\frac{\\ln 2}{k_{obs}}$.",
                    "With scavenging: $[\\cdot OH]_{ss}' = 0.30 [\\cdot OH]_{ss}$. Time for $99\\%$ removal: $t_{99} = \\frac{\\ln 100}{k'_{obs}}$."
                ],
                "solution": """**Step 1: Calculate pseudo-first-order rate constant $k_{obs}$**
Given:
- $k_{OH} = 4.80 \\times 10^9\\ \\text{M}^{-1}\\text{s}^{-1}$
- $[\\cdot OH]_{ss} = 2.50 \\times 10^{-12}\\ \\text{M}$
\\[
k_{obs} = k_{OH} [\\cdot OH]_{ss} = (4.80 \\times 10^9\\ \\text{M}^{-1}\\text{s}^{-1}) \\times (2.50 \\times 10^{-12}\\ \\text{M}) = 0.0120\\ \\text{s}^{-1}
\\]
Converting to per minute:
\\[
k_{obs} = 0.0120\\ \\text{s}^{-1} \\times 60\\ \\text{s}/\\text{min} = 0.720\\ \\text{min}^{-1}
\\]

**Step 2: Calculate dye half-life**
\\[
t_{1/2} = \\frac{\\ln 2}{k_{obs}} = \\frac{0.69315}{0.720\\ \\text{min}^{-1}} = 0.9627\\ \\text{minutes} \\approx 57.8\\ \\text{seconds}
\\]

**Step 3: Calculate required reaction time under chloride scavenging**
When chloride depression reduces steady-state radical concentration by $70.0\\%$, the remaining radical concentration is:
\\[
[\\cdot OH]'_{ss} = 0.30 \\times [\\cdot OH]_{ss} = 0.30 \\times 2.50 \\times 10^{-12} = 7.50 \\times 10^{-13}\\ \\text{M}
\\]
The reduced observed rate constant:
\\[
k'_{obs} = 0.30 \\times k_{obs} = 0.30 \\times 0.720\\ \\text{min}^{-1} = 0.216\\ \\text{min}^{-1} = 0.00360\\ \\text{s}^{-1}
\\]
For $99.0\\%$ color elimination, remaining dye concentration is $1.0\\%$ ($[D]/[D]_0 = 0.010$):
\\[
t_{99} = \\frac{\\ln(100)}{k'_{obs}} = \\frac{4.6052}{0.216\\ \\text{min}^{-1}} = 21.32\\ \\text{minutes}
\\]

**Conclusion**:
In pure water, dye half-life is **57.8 seconds**. High salinity scavenger interference extends the $99\\%$ destruction time from $6.4\\ \\text{min}$ to **21.3 minutes**."""
            },
            {
                "id": "prob_8_7",
                "tier": "Advanced",
                "title": "Reverse Osmosis Transport: Spiegler-Kedem Model and Salt Rejection",
                "statement": "A spiral-wound polyamide reverse osmosis (RO) membrane element treats tertiary textile effluent containing $C_b = 3500\\ \\text{mg}/\\text{L}$ $NaCl$ at $25^\\circ\\text{C}$ ($T = 298.15\\ \\text{K}$, $R = 0.08314\\ \\text{L}\\cdot\\text{bar}/(\\text{mol}\\cdot\\text{K})$). The membrane has pure water permeability $A = 3.50\\ \\text{L}/(\\text{m}^2\\cdot\\text{h}\\cdot\\text{bar})$ and salt permeability $B = 0.850\\ \\text{L}/(\\text{m}^2\\cdot\\text{h})$. Applied net hydraulic pressure is $\\Delta P = 24.0\\ \\text{bar}$. Taking complete dissociation of $NaCl$ ($i = 2$, molar mass $58.44\\ \\text{g}/\\text{mol}$): (a) Assuming zero permeate salt concentration as a first approximation, calculate the feed osmotic pressure $\\pi_f$ (in bar) and initial net driving pressure $\\Delta P - \\pi_f$. (b) Using the coupled solution-diffusion equations $J_w = A (\\Delta P - \\Delta \\pi)$ and $R_{obs} = 1 - \\frac{C_p}{C_m} = \\frac{J_w}{J_w + B}$, and assuming negligible concentration polarization ($C_m \\approx C_b$), solve iteratively for the steady-state permeate flux $J_w$ (in $\\text{L}/(\\text{m}^2\\cdot\\text{h})$) and true observed salt rejection $R_{obs}$. (c) Calculate the permeate salt concentration $C_p$ in $\\text{mg}/\\text{L}$.",
                "hints": [
                    "Feed osmotic pressure: $\\pi_f = i C R T = 2 \\times \\left(\\frac{3.50\\ \\text{g/L}}{58.44\\ \\text{g/mol}}\\right) \\times 0.08314 \\times 298.15$.",
                    "Coupled system: $\\Delta \\pi = \\pi_f - \\pi_p = \\pi_f (1 - C_p / C_b) = \\pi_f R_{obs}$.",
                    "Substitute $R_{obs} = \\frac{J_w}{J_w + B}$ into $J_w = A [\\Delta P - \\pi_f R_{obs}]$ to form a quadratic in $J_w$."
                ],
                "solution": """**Step 1: Calculate feed osmotic pressure $\\pi_f$**
Feed salt concentration in molarity:
\\[
C_b = \\frac{3.500\\ \\text{g}/\\text{L}}{58.443\\ \\text{g}/\\text{mol}} = 0.059887\\ \\text{mol}/\\text{L}
\\]
With van 't Hoff factor $i = 2$:
\\[
\\pi_f = i C_b R T = 2 \\times (0.059887\\ \\text{mol}/\\text{L}) \\times (0.083145\\ \\text{L}\\cdot\\text{bar}/(\\text{mol}\\cdot\\text{K})) \\times (298.15\\ \\text{K})
\\]
\\[
\\pi_f = 2.969\\ \\text{bar} \\approx 2.97\\ \\text{bar}
\\]

**Step 2: Set up and solve the coupled quadratic equation for $J_w$**
The osmotic pressure differential across the membrane:
\\[
\\Delta \\pi = \\pi_f - \\pi_p = \\pi_f \\left( 1 - \\frac{C_p}{C_b} \\right) = \\pi_f R_{obs}
\\]
From the solution-diffusion model:
\\[
R_{obs} = \\frac{J_w}{J_w + B}
\\]
Substituting into the water flux equation:
\\[
J_w = A \\left( \\Delta P - \\pi_f \\frac{J_w}{J_w + B} \\right)
\\]
Multiplying both sides by $(J_w + B)$:
\\[
J_w (J_w + B) = A \\Delta P (J_w + B) - A \\pi_f J_w
\\]
\\[
J_w^2 + B J_w = A \\Delta P J_w + A B \\Delta P - A \\pi_f J_w
\\]
Rearranging into standard quadratic form:
\\[
J_w^2 + \\left[ B - A (\\Delta P - \\pi_f) \\right] J_w - A B \\Delta P = 0
\\]
Evaluate coefficients with given numerical values:
- $A = 3.50\\ \\text{L}/(\\text{m}^2\\cdot\\text{h}\\cdot\\text{bar})$
- $B = 0.850\\ \\text{L}/(\\text{m}^2\\cdot\\text{h})$
- $\\Delta P = 24.0\\ \\text{bar}$
- $\\pi_f = 2.969\\ \\text{bar}$
- $\\Delta P - \\pi_f = 24.0 - 2.969 = 21.031\\ \\text{bar}$
- $A (\\Delta P - \\pi_f) = 3.50 \\times 21.031 = 73.6085$
- Linear coefficient: $b_{quad} = B - A(\\Delta P - \\pi_f) = 0.850 - 73.6085 = -72.7585$
- Constant coefficient: $c_{quad} = -A B \\Delta P = -(3.50)(0.850)(24.0) = -71.40$

The quadratic equation:
\\[
J_w^2 - 72.7585 J_w - 71.40 = 0
\\]
Applying the quadratic formula:
\\[
J_w = \\frac{72.7585 + \\sqrt{(-72.7585)^2 - 4(1)(-71.40)}}{2} = \\frac{72.7585 + \\sqrt{5293.80 + 285.60}}{2}
\\]
\\[
J_w = \\frac{72.7585 + \\sqrt{5579.40}}{2} = \\frac{72.7585 + 74.6954}{2} = \\frac{147.454}{2} = 73.727\\ \\text{L}/(\\text{m}^2\\cdot\\text{h})
\\]

**Step 3: Calculate rejection $R_{obs}$ and permeate concentration $C_p$**
\\[
R_{obs} = \\frac{J_w}{J_w + B} = \\frac{73.727}{73.727 + 0.850} = \\frac{73.727}{74.577} = 0.98860 \\quad (98.86\\%)
\\]
Permeate salt concentration:
\\[
C_p = C_b (1 - R_{obs}) = 3500\\ \\text{mg}/\\text{L} \\times (1 - 0.98860) = 3500 \\times 0.01140 = 39.9\\ \\text{mg}/\\text{L}
\\]

**Conclusion**:
The system delivers a permeate flux of **$73.7\\ \\text{L}/(\\text{m}^2\\cdot\\text{h})$** at an observed rejection of **$98.86\\%$**, purifying the feed from $3500\\ \\text{mg}/\\text{L}$ down to **$39.9\\ \\text{mg}/\\text{L}$ TDS**."""
            },
            {
                "id": "prob_8_8",
                "tier": "Advanced",
                "title": "Continuous Biological Post-Denitrification: Methanol Dosing Stoichiometry",
                "statement": "An advanced tertiary denitrification filter removes nitrate from an industrial wastewater effluent with flow rate $Q = 4800\\ \\text{m}^3/\\text{day}$. Influent to the anoxic filter contains nitrate-nitrogen $[NO_3^--N] = 38.0\\ \\text{mg}/\\text{L}$, nitrite-nitrogen $[NO_2^--N] = 2.0\\ \\text{mg}/\\text{L}$, and dissolved oxygen $[O_2] = 4.5\\ \\text{mg}/\\text{L}$. Methanol ($CH_3OH$, molar mass $32.04\\ \\text{g}/\\text{mol}$) is dosed as the supplemental electron donor. The overall empirical stoichiometry including biomass synthesis is: $NO_3^- + 1.08\\ CH_3OH + 0.24\\ H_2CO_3 \\rightarrow 0.056\\ C_5H_7O_2N\\text{(biomass)} + 0.47\\ N_2 + 1.68\\ H_2O + HCO_3^-$. In addition, methanol is consumed by $NO_2^-$ ($NO_2^- + 0.67\\ CH_3OH \\rightarrow \\text{biomass} + 0.5\\ N_2$) and by residual dissolved oxygen ($O_2 + 0.93\\ CH_3OH \\rightarrow \\text{biomass} + CO_2 + H_2O$). Using the standard EPA empirical methanol requirement formula: $C_m = 2.47 [NO_3^--N] + 1.53 [NO_2^--N] + 0.87 [O_2]$. (a) Calculate the required methanol concentration $C_m$ in $\\text{mg}/\\text{L}$. (b) Determine the daily consumption of commercial methanol ($99.0\\%$ purity, density $\\rho = 0.792\\ \\text{kg}/\\text{L}$) in liters per day. (c) Calculate the daily biological denitrification sludge production in $\\text{kg dry solids}/\\text{day}$.",
                "hints": [
                    "Evaluate $C_m = 2.47(38.0) + 1.53(2.0) + 0.87(4.5)$.",
                    "Mass of pure methanol: $M_{MeOH} = Q \\times C_m$. Volume commercial: $V = \\frac{M_{MeOH}}{\\rho \\times 0.99}$.",
                    "Sludge yield: Use the biomass coefficient ($0.056\\ \\text{mol } C_5H_7O_2N$ per mol $NO_3^-$ reduced)."
                ],
                "solution": """**Step 1: Calculate required methanol concentration $C_m$**
Applying the EPA empirical relationship:
\\[
C_m = 2.47 [NO_3^--N] + 1.53 [NO_2^--N] + 0.87 [O_2]
\\]
Substituting parameter values:
- Term 1 (Nitrate): $2.47 \\times 38.0 = 93.86\\ \\text{mg}/\\text{L}$
- Term 2 (Nitrite): $1.53 \\times 2.0 = 3.06\\ \\text{mg}/\\text{L}$
- Term 3 (Dissolved Oxygen): $0.87 \\times 4.5 = 3.915\\ \\text{mg}/\\text{L}$
\\[
C_m = 93.86 + 3.06 + 3.915 = 100.835\\ \\text{mg}/\\text{L} \\approx 100.8\\ \\text{mg}/\\text{L}
\\]

**Step 2: Calculate daily volume of commercial methanol**
Total mass of pure methanol per day:
\\[
M_{MeOH} = Q \\times C_m = 4800\\ \\text{m}^3/\\text{day} \\times 100.835\\ \\text{g}/\\text{m}^3 = 484,008\\ \\text{g}/\\text{day} = 484.01\\ \\text{kg/day}
\\]
Accounting for $99.0\\%$ chemical purity and density $\\rho = 0.792\\ \\text{kg}/\\text{L}$:
\\[
V_{commercial} = \\frac{484.01\\ \\text{kg/day}}{(0.792\\ \\text{kg}/\\text{L}) \\times 0.990} = \\frac{484.01}{0.78408} = 617.29\\ \\text{L/day} \\approx 617\\ \\text{L/day}
\\]

**Step 3: Calculate daily excess biological sludge production**
From the balanced stoichiometry for nitrate:
$1\\ \\text{mol } NO_3^--N$ ($14.01\\ \\text{g N}$) produces $0.056\\ \\text{mol of biomass}$ ($C_5H_7O_2N$, molar mass $113.12\\ \\text{g}/\\text{mol}$):
\\[
Y_{obs} = \\frac{0.056 \\times 113.12\\ \\text{g biomass}}{14.01\\ \\text{g N}} = \\frac{6.3347}{14.01} = 0.4522\\ \\text{g biomass} / \\text{g } NO_3^--N
\\]
Nitrate nitrogen removed daily:
\\[
M_{N, removed} = 4800\\ \\text{m}^3/\\text{day} \\times 38.0\\ \\text{g}/\\text{m}^3 = 182,400\\ \\text{g N/day} = 182.4\\ \\text{kg N/day}
\\]
Sludge produced from nitrate reduction:
\\[
P_{x, N} = 182.4\\ \\text{kg N/day} \\times 0.4522 = 82.48\\ \\text{kg VSS/day}
\\]
Adding cellular synthesis from dissolved oxygen respiration ($0.20\\ \\text{g VSS}/\\text{g } O_2$):
\\[
M_{O2} = 4800 \\times 4.5 = 21.6\\ \\text{kg } O_2/\\text{day} \\implies P_{x, O2} = 21.6 \\times 0.20 = 4.32\\ \\text{kg VSS/day}
\\]
Total biological sludge produced:
\\[
P_{x, tot} = 82.48 + 4.32 = 86.80\\ \\text{kg VSS/day} \\approx 86.8\\ \\text{kg/day}
\\]

**Conclusion**:
The system requires a dosing rate of **$100.8\\ \\text{mg}/\\text{L}$ of methanol** (**$617\\ \\text{L/day}$** of commercial methanol), generating **$86.8\\ \\text{kg/day}$ of dry biological sludge**."""
            },
            {
                "id": "prob_8_9",
                "tier": "Advanced",
                "title": "Zero Liquid Discharge: MVR Brine Evaporator and Crystallizer Mass & Energy Balance",
                "statement": "A Zero Liquid Discharge (ZLD) plant concentrates High-Pressure Reverse Osmosis (HPRO) reject brine at $Q_f = 25.0\\ \\text{m}^3/\\text{h}$ with TDS $C_f = 80,000\\ \\text{mg}/\\text{L}$ ($8.0\\ \\text{wt}\\%$, density $\\rho_f = 1060\\ \\text{kg}/\\text{m}^3$). The brine enters a Mechanical Vapor Recompression (MVR) falling film evaporator producing pure condensed distillate and concentrated liquor at $C_L = 280,000\\ \\text{mg}/\\text{L}$ ($28.0\\ \\text{wt}\\%$, density $\\rho_L = 1200\\ \\text{kg}/\\text{m}^3$). This concentrated liquor feeds a draft-tube baffle crystallizer yielding dry salt cake ($98.0\\ \\text{wt}\\%$ dry solids) and mother liquor recycled to extinction. (a) Perform a solid and liquid mass balance on the MVR evaporator to calculate the mass flow rate of feed $m_f$ (in $\\text{kg}/\\text{h}$), concentrated liquor $m_L$ (in $\\text{kg}/\\text{h}$), and pure evaporated distillate $m_D$ (in $\\text{kg}/\\text{h}$ and $\\text{m}^3/\\text{h}$). (b) Calculate the daily mass of dry solid salt cake recovered (in metric tons/day). (c) The MVR compressor consumes $28.0\\ \\text{kWh}$ of electrical power per metric ton of water evaporated. Calculate the continuous operating electrical power demand of the MVR compressor in kilowatts (kW).",
                "hints": [
                    "Mass flow of feed: $m_f = Q_f \\times \\rho_f$.",
                    "Salt balance on evaporator: $m_f \\cdot w_f = m_L \\cdot w_L \\implies m_L = m_f (0.08 / 0.28)$.",
                    "Distillate mass: $m_D = m_f - m_L$.",
                    "Compressor power: $P = (m_D / 1000) \\times 28.0\\ \\text{kWh} / 1\\ \\text{h}$."
                ],
                "solution": """**Step 1: Perform mass balance on MVR falling film evaporator**
Feed mass flow rate:
\\[
m_f = Q_f \\times \\rho_f = 25.0\\ \\text{m}^3/\\text{h} \\times 1060\\ \\text{kg}/\\text{m}^3 = 26,500\\ \\text{kg}/\\text{h}
\\]
Mass fraction of dissolved solids:
- Feed: $w_f = 0.080$ ($8.0\\ \\text{wt}\\%$)
- Concentrated liquor: $w_L = 0.280$ ($28.0\\ \\text{wt}\\%$)

Salt mass conservation across the evaporator (pure vapor contains $0\\%$ salt):
\\[
m_f \\cdot w_f = m_L \\cdot w_L
\\]
\\[
m_L = m_f \\left( \\frac{w_f}{w_L} \\right) = 26,500\\ \\text{kg}/\\text{h} \\times \\left( \\frac{0.080}{0.280} \\right) = 26,500 \\times 0.28571 = 7,571.4\\ \\text{kg}/\\text{h}
\\]
Total water evaporated and condensed as pure distillate:
\\[
m_D = m_f - m_L = 26,500 - 7,571.4 = 18,928.6\\ \\text{kg}/\\text{h} \\approx 18.93\\ \\text{metric tons/h}
\\]
Volumetric distillate water recovery ($\rho_w \\approx 1000\\ \\text{kg}/\\text{m}^3$):
\\[
Q_D = 18.93\\ \\text{m}^3/\\text{h}
\\]
Water recovery percentage in the evaporator:
\\[
\\%\\text{Recovery} = \\frac{m_D}{m_f (1 - w_f)} \\times 100 = \\frac{18,928.6}{26,500 \\times 0.920} \\times 100 = \\frac{18,928.6}{24,380} \\times 100 = 77.64\\%
\\]

**Step 2: Calculate daily solid salt recovery from crystallizer**
Total salt entering the system per hour:
\\[
m_{salt} = m_f \\cdot w_f = 26,500\\ \\text{kg}/\\text{h} \\times 0.080 = 2,120\\ \\text{kg salt/h}
\\]
With crystallization producing salt cake at $98.0\\ \\text{wt}\\%$ solids:
\\[
m_{cake} = \\frac{2,120\\ \\text{kg}/\\text{h}}{0.980} = 2,163.27\\ \\text{kg cake/h}
\\]
Daily salt cake production ($24\\ \\text{hours}$):
\\[
M_{salt, daily} = 2,163.27\\ \\text{kg}/\\text{h} \\times 24\\ \\text{h} = 51,918\\ \\text{kg/day} = 51.92\\ \\text{metric tons/day}
\\]

**Step 3: Calculate MVR electrical compressor power demand**
Specific electrical energy consumption $= 28.0\\ \\text{kWh} / \\text{metric ton evaporated}$.
Evaporation rate:
\\[
\\dot{m}_D = 18.9286\\ \\text{metric tons/h}
\\]
Continuous electrical power consumption:
\\[
P_{elec} = 18.9286\\ \\text{tons}/\\text{h} \\times 28.0\\ \\text{kWh}/\\text{ton} = 530.0\\ \\text{kW}
\\]

**Conclusion**:
The MVR evaporator recovers **$18.93\\ \\text{m}^3/\\text{h}$ of pure distilled water** ($454\\ \\text{m}^3/\\text{day}$), producing **$51.92\\ \\text{tons/day}$ of dry salt cake**, drawing a steady compressor load of **$530\\ \\text{kW}$**."""
            }
        ]
    }
    return unit

if __name__ == "__main__":
    u8 = get_unit_8()
    print(f"Unit 8 generated: {len(u8['sections'])} sections, {len(u8['problems'])} problems.")
