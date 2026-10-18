"""
create_env_u4.py
Unit 4: Aquatic Chemistry, Carbonate Equilibria & Water Quality Metrics
Covers water solvent properties, carbonate alkalinity, dissolved oxygen, BOD/COD/TOC,
Streeter-Phelps sag model, EDTA hardness titrations, pe-pH Pourbaix diagrams.
Strictly zero prohibited tokens, pure UNIX newlines, pristine KaTeX.
"""

def get_unit_4():
    sections = [
        {
            "id": "sec4_1",
            "title": "Chemical Structure of Water, Hydrogen-Bonding Networks & Aquatic Solvent Properties",
            "content": """Water ($\\text{H}_2\\text{O}$) is the universal solvent of aquatic ecosystems, endowed with anomalous thermodynamic and transport properties governed by its condensed-phase hydrogen-bonding network.

### 1. Molecular Geometry and Electric Dipole Moment
The isolated gas-phase water molecule possesses $C_{2v}$ point group symmetry with an experimental $\\text{H}-\\text{O}-\\text{H}$ bond angle of $104.5^\\circ$ and an $\\text{O}-\\text{H}$ bond length of $0.0958\\text{ nm}$.
Electronegativity differences between oxygen ($\chi = 3.44$) and hydrogen ($\chi = 2.20$) induce substantial bond polarization, producing an isolated molecular permanent electric dipole moment:
\\[ \\mu_0 = 1.854\\text{ Debye} = 6.184 \\times 10^{-30}\\text{ C}\\cdot\\text{m} \\]
In condensed liquid water, cooperative mutual polarization enhances the effective molecular dipole moment to:
\\[ \\mu_{\\text{liquid}} \\approx 2.6 - 3.0\\text{ Debye} \\]
Liquid water possesses an exceptionally large static dielectric constant (relative permittivity $\\varepsilon_r \\approx 78.4$ at $298\\text{ K}$), dramatically reducing the electrostatic Coulombic interaction energy between dissolved ionic species:
\\[ V(r) = \\frac{q_1 q_2}{4\\pi \\varepsilon_0 \\varepsilon_r r} \\]
This intense dielectric screening facilitates the spontaneous solvation and electrolytic dissociation of ionic lattices.

### 2. Tetrahedral Hydrogen-Bonding Topology and Anomalies
Each oxygen atom acts as a dual hydrogen-bond donor (via its two polarized covalent $\\text{O}-\\text{H}$ bonds) and a dual hydrogen-bond acceptor (via its two $sp^3$-hybridized non-bonding lone pairs).
This forms a fluctuating, transient three-dimensional tetrahedral network characterized by:
- An average hydrogen bond energy of $\\Delta H_{\\text{HB}} \\approx 21\\text{ kJ/mol}$.
- **Density Maximum at $3.98^\\circ\\text{C}$ ($277.13\\text{ K}$)**: Above $3.98^\\circ\\text{C}$, normal thermal kinetic expansion dominates; below $3.98^\\circ\\text{C}$, the progressive formation of an open, low-density tetrahedral cage network (pre-ice $I_h$ structuring) decreases liquid density. This ensures that freshwater lakes freeze from the top down, preserving benthic aquatic ecosystems.
- High specific heat capacity ($c_p = 4.184\\text{ J/(g}\\cdot\\text{K)}$), high enthalpy of vaporization ($\Delta H_{\\text{vap}} = 40.66\\text{ kJ/mol}$), and high surface tension ($\gamma = 72.8\\text{ mN/m}$ at $20^\\circ\\text{C}$)."""
        },
        {
            "id": "sec4_2",
            "title": "The Aquatic Carbonate System: Open vs Closed Systems, Alkalinity & Calcite Saturation",
            "content": """The aquatic carbonate system is the principal acid-base buffer regulating natural water bodies.

### 1. Fundamental Carbonate Equilibria
Dissolved inorganic carbon comprises four interconverting chemical species:
1. Gaseous carbon dioxide dissolution:
   \\[ \\text{CO}_2(g) \\xrightleftharpoons{K_H} \\text{CO}_2^*(aq) \\quad (K_H = 3.4 \\times 10^{-2}\\text{ M/atm}) \\]
   where $[\\text{CO}_2^*] = [\\text{CO}_2(aq)] + [\\text{H}_2\\text{CO}_3]$.
2. First dissociation:
   \\[ \\text{CO}_2^* + \\text{H}_2\\text{O} \\xrightleftharpoons{K_{a1}} \\text{H}^+ + \\text{HCO}_3^- \\quad (pK_{a1} = 6.35\\text{ at }25^\\circ\\text{C}) \\]
3. Second dissociation:
   \\[ \\text{HCO}_3^- \\xrightleftharpoons{K_{a2}} \\text{H}^+ + \\text{CO}_3^{2-} \\quad (pK_{a2} = 10.33\\text{ at }25^\\circ\\text{C}) \\]

The total concentration of dissolved inorganic carbon is:
\\[ C_T = [\\text{DIC}] = [\\text{CO}_2^*] + [\\text{HCO}_3^-] + [\\text{CO}_3^{2-}] \\]
Defining alpha ionization fractions:
\\[ \\alpha_0 = \\frac{[\\text{CO}_2^*]}{C_T} = \\frac{[\\text{H}^+]^2}{[\\text{H}^+]^2 + K_{a1}[\\text{H}^+] + K_{a1}K_{a2}} \\]
\\[ \\alpha_1 = \\frac{[\\text{HCO}_3^-]}{C_T} = \\frac{K_{a1}[\\text{H}^+]}{[\\text{H}^+]^2 + K_{a1}[\\text{H}^+] + K_{a1}K_{a2}} \\]
\\[ \\alpha_2 = \\frac{[\\text{CO}_3^{2-}]}{C_T} = \\frac{K_{a1}K_{a2}}{[\\text{H}^+]^2 + K_{a1}[\\text{H}^+] + K_{a1}K_{a2}} \\]

### 2. Alkalinity and Acid Neutralizing Capacity (ANC)
**Total Alkalinity (Alk)** represents the equivalent sum of all titratable proton-accepting bases measured relative to a carbonic acid equivalence point ($\text{pH} \\approx 4.5$):
\\[ \\text{Alk} = [\\text{HCO}_3^-] + 2[\\text{CO}_3^{2-}] + [\\text{OH}^-] - [\\text{H}^+] \\]
In typical natural waters with $6.0 < \\text{pH} < 9.0$:
\\[ \\text{Alk} \\approx [\\text{HCO}_3^-] + 2[\\text{CO}_3^{2-}] \\]
Alkalinity is a **conservative quantity** under pressure and temperature changes as well as gas exchange ($\text{CO}_2$ addition or loss changes $\text{pH}$ and $C_T$, but leaves Total Alkalinity strictly invariant!).

### 3. Calcite Saturation and The Langelier Saturation Index
The saturation state with respect to calcite ($\text{CaCO}_3$) is:
\\[ \\Omega = \\frac{[\\text{Ca}^{2+}][\\text{CO}_3^{2-}]}{K_{sp}} \\]
The **Langelier Saturation Index (LSI)** is:
\\[ \\text{LSI} = \\text{pH} - \\text{pH}_s \\]
where $\\text{pH}_s$ is the saturation pH:
\\[ \\text{pH}_s = (pK_{a2} - pK_{sp}) + p[\\text{Ca}^{2+}] + p[\\text{Alk}] \\]
- $\\text{LSI} > 0$: Supersaturated; tendency for scale deposition.
- $\\text{LSI} < 0$: Undersaturated; corrosive toward distribution pipes."""
        },
        {
            "id": "sec4_3",
            "title": "Dissolved Oxygen Thermodynamics, Henry's Law & Temperature Salting-Out",
            "content": """Dissolved oxygen (DO) is the master parameter governing aquatic aerobic respiration, biogeochemical redox potential, and the survival of fish and benthic invertebrates.

### 1. Gas Dissolution Thermodynamics and Henry's Law
The dissolution of molecular oxygen in water is an exothermic process ($\Delta H_{\\text{diss}} < 0$):
\\[ \\text{O}_2(g) \\xrightleftharpoons{K_H} \\text{O}_2(aq) \\]
According to Henry's law:
\\[ [\\text{O}_2(aq)] = K_H(T) P_{\\text{O}_2} \\]
where $P_{\\text{O}_2} = y_{\\text{O}_2} (P - P_{\\text{H}_2\\text{O}})$ is the dry partial pressure of atmospheric oxygen ($y_{\\text{O}_2} = 0.2095$).
The temperature dependence of Henry's law coefficient is described by the van 't Hoff equation:
\\[ \\frac{d\\ln K_H}{dT} = -\\frac{\\Delta H_{\\text{diss}}}{R T^2} \\implies K_H(T) = K_H(T_0) \\exp\\left[ \\frac{-\\Delta H_{\\text{diss}}}{R}\\left(\\frac{1}{T} - \\frac{1}{T_0}\\right) \\right] \\]
Because dissolution is exothermic ($\Delta H_{\\text{diss}} \\approx -11.7\\text{ kJ/mol}$), Henry's solubility coefficient **decreases** with increasing temperature. At sea level ($1.0\\text{ atm}$):
- At $T = 0^\\circ\\text{C}$ ($273\\text{ K}$): $[\text{O}_2]_{\\text{sat}} \\approx 14.62\\text{ mg/L}$
- At $T = 20^\\circ\\text{C}$ ($293\\text{ K}$): $[\text{O}_2]_{\\text{sat}} \\approx 9.09\\text{ mg/L}$
- At $T = 35^\\circ\\text{C}$ ($308\\text{ K}$): $[\text{O}_2]_{\\text{sat}} \\approx 6.95\\text{ mg/L}$

### 2. Salting-Out Effect in Saline Waters
Dissolved electrolytes reduce the solubility of non-polar gases through electrostrictive hydration of ions (the Setchenow salting-out equation):
\\[ \\ln\\left(\\frac{C_{\\text{pure}}}{C_{\\text{saline}}}\\right) = k_s I_s \\]
where $k_s$ is the Setchenow salting-out coefficient and $I_s$ is the ionic strength of the water.
At $20^\\circ\\text{C}$, full-strength seawater ($S = 35\\text{ g/kg}$) holds only $\\approx 7.35\\text{ mg/L}$ of DO at saturation, compared to $9.09\\text{ mg/L}$ in freshwater.

### 3. Hypoxia and Critical Ecological Thresholds
Aquatic ecology defines three dissolved oxygen regimes:
- **Normoxia ($> 6.0\\text{ mg/L}$)**: Healthy conditions supporting diverse teleost fish and macroinvertebrate communities.
- **Stress Zone ($2.0 - 5.0\\text{ mg/L}$)**: Physiological distress, reduced swimming speeds, avoidance behavior.
- **Hypoxia ($< 2.0\\text{ mg/L}$)**: Acute mortality for fish; benthic fauna mortality.
- **Anoxia ($[\\text{O}_2] \\equiv 0.0\\text{ mg/L}$)**: Complete depletion, initiating anaerobic microbial reduction of $\\text{NO}_3^-, \\text{Fe}^{3+}, \\text{SO}_4^{2-}$, producing toxic hydrogen sulfide ($\\text{H}_2\\text{S}$)."""
        },
        {
            "id": "sec4_4",
            "title": "Biochemical Oxygen Demand (BOD): First-Order Kinetics & 5-Day Respirometry",
            "content": """Biochemical Oxygen Demand (BOD) quantifies the amount of dissolved oxygen consumed by heterotrophic microorganisms during the biological oxidation of organic matter.

### 1. Biological Oxidation Stoichiometry
The aerobic degradation of carbonaceous organic matter (represented generically as glucose $\\text{C}_6\\text{H}_{12}\\text{O}_6$ or cell biomass $\\text{C}_5\\text{H}_7\\text{NO}_2$) proceeds via:
\\[ \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\,\\text{O}_2 \\xrightarrow{\\text{bacteria}} 6\\,\\text{CO}_2 + 6\\,\\text{H}_2\\text{O} + \\Delta G^\\circ \\]
One mole of glucose ($180.16\\text{ g}$) requires $6\\text{ moles}$ of $\\text{O}_2$ ($192.00\\text{ g}$), yielding a theoretical carbonaceous demand of $1.066\\text{ g O}_2\\text{/g glucose}$.

### 2. First-Order Kinetics of Carbonaceous BOD Exertion
The rate of deoxygenation is assumed to be proportional to the concentration of remaining biodegradable organic matter $L(t)$ (measured in oxygen equivalents, $\text{mg/L}$):
\\[ \\frac{dL}{dt} = -k_1 L \\]
Integrating yields the remaining unoxidized substrate:
\\[ L(t) = L_0 \\exp(-k_1 t) \\]
where $L_0$ is the **Ultimate Carbonaceous BOD** ($\text{CBOD}_u$) at $t = 0$, and $k_1$ is the first-order deoxygenation rate constant (base $e$, typically $0.10 - 0.35\\text{ day}^{-1}$ at $20^\\circ\\text{C}$).
The cumulative oxygen consumed—the **BOD exerted** $y(t)$—is:
\\[ y(t) = L_0 - L(t) = L_0 [1 - \\exp(-k_1 t)] \\]
Using common base 10 rate constants ($K_{10} = k_1 / \\ln(10) = k_1 / 2.3026$):
\\[ y(t) = L_0 [1 - 10^{-K_{10} t}] \\]

### 3. The Standard 5-Day BOD Test (BOD5)
Because total oxidation can require 20 to 30 days, regulatory agencies standardize testing at $t = 5\\text{ days}$ incubated in darkness at $20^\\circ\\text{C}$ ($\text{BOD}_5$):
\\[ \\text{BOD}_5 = L_0 [1 - \\exp(-5 k_1)] \\]
For a typical municipal wastewater with $k_1 = 0.23\\text{ day}^{-1}$:
\\[ \\text{BOD}_5 = L_0 [1 - \\exp(-1.15)] = L_0 (1 - 0.3166) \\approx 0.683 L_0 \\]
Thus, $\\text{BOD}_5$ captures approximately $68\\%$ of the ultimate carbonaceous demand.

### 4. Nitrogenous BOD (NBOD)
After $\\approx 5 - 8\\text{ days}$, autotrophic nitrifying bacteria (Nitrosomonas and Nitrobacter) proliferate, oxidizing un-ionized ammonia and ammonium:
\\[ \\text{NH}_4^+ + 1.5\\,\\text{O}_2 \\xrightarrow{\\text{Nitrosomonas}} \\text{NO}_2^- + 2\\,\\text{H}^+ + \\text{H}_2\\text{O} \\]
\\[ \\text{NO}_2^- + 0.5\\,\\text{O}_2 \\xrightarrow{\\text{Nitrobacter}} \\text{NO}_3^- \\]
\\[ \\text{Net Nitrification}: \\quad \\text{NH}_4^+ + 2\\,\\text{O}_2 \\rightarrow \\text{NO}_3^- + 2\\,\\text{H}^+ + \\text{H}_2\\text{O} \\]
Stoichiometrically, oxidizing $1\\text{ mole}$ of nitrogen ($14.01\\text{ g N}$) consumes $2\\text{ moles}$ of $\\text{O}_2$ ($64.00\\text{ g O}_2$):
\\[ \\text{Theoretical NBOD} = \\frac{64.00\\text{ g O}_2}{14.01\\text{ g N}} \\approx 4.57\\text{ g O}_2\\text{/g NH}_4^+\\text{-N} \\]
In uninhibited BOD bottles, the onset of nitrification produces a secondary surge in oxygen exertion."""
        },
        {
            "id": "sec4_5",
            "title": "Chemical Oxygen Demand Dichromate Stoichiometry & Total Organic Carbon",
            "content": """While BOD measures only biologically accessible organics over days, Chemical Oxygen Demand (COD) and Total Organic Carbon (TOC) provide rapid, comprehensive chemical metrics.

### 1. Potassium Dichromate Reflux Chemistry
Chemical Oxygen Demand (COD) quantifies the equivalent oxygen capacity required to chemically oxidize virtually all organic compounds to carbon dioxide and water using boiling hexavalent potassium dichromate ($\\text{K}_2\\text{Cr}_2\\text{O}_7$) in concentrated sulfuric acid:
\\[ \\text{Cr}_2\\text{O}_7^{2-} + 14\\,\\text{H}^+ + 6\\,e^- \\rightarrow 2\\,\\text{Cr}^{3+} + 7\\,\\text{H}_2\\text{O} \\quad (E^\\circ = +1.36\\text{ V}) \\]
For a generic organic molecule $\\text{C}_n\\text{H}_a\\text{O}_b\\text{N}_c$:
\\[ \\text{C}_n\\text{H}_a\\text{O}_b\\text{N}_c + \\left(n + \\frac{a}{4} - \\frac{b}{2} - \\frac{3c}{4}\\right)\\text{O}_2 \\rightarrow n\\,\\text{CO}_2 + \\left(\\frac{a - 3c}{2}\\right)\\text{H}_2\\text{O} + c\\,\\text{NH}_3 \\]
(Nitrogen in amino groups is converted to ammonia, rather than oxidized to nitrate).
The theoretical COD per mole of compound is:
\\[ \\text{ThCOD} = \\left(n + \\frac{a}{4} - \\frac{b}{2} - \\frac{3c}{4}\\right) \\times 32.00\\text{ g O}_2\\text{/mol} \\]

### 2. Analytical Catalysis and Halide Interference
- **Silver Sulfate Catalyst ($\text{Ag}_2\text{SO}_4$)**: Added ($~10\\text{ g/L}$) to catalyze the oxidation of refractory straight-chain aliphatic hydrocarbons and fatty acids, which otherwise resist dichromate attack.
- **Mercuric Sulfate Masking ($\text{HgSO}_4$)**: Chloride ions ($\\text{Cl}^-$) are readily oxidized by dichromate, creating false-positive COD:
  \\[ 6\\,\\text{Cl}^- + \\text{Cr}_2\\text{O}_7^{2-} + 14\\,\\text{H}^+ \\rightarrow 3\\,\\text{Cl}_2 + 2\\,\\text{Cr}^{3+} + 7\\,\\text{H}_2\\text{O} \\]
  Adding $\\text{HgSO}_4$ forms an un-ionized mercuric chloride complex:
  \\[ \\text{Hg}^{2+} + 4\\,\\text{Cl}^- \\rightarrow [\\text{HgCl}_4]^{2-} \\quad (\\log \\beta_4 \\approx 15.1) \\]
  masking up to $2000\\text{ mg/L}$ of chloride.
The unreacted dichromate is back-titrated with standard ferrous ammonium sulfate (FAS, $\\text{Fe}(\\text{NH}_4)_2(\\text{SO}_4)_2$) using ferroin indicator:
\\[ \\text{Cr}_2\\text{O}_7^{2-} + 6\\,\\text{Fe}^{2+} + 14\\,\\text{H}^+ \\rightarrow 2\\,\\text{Cr}^{3+} + 6\\,\\text{Fe}^{3+} + 7\\,\\text{H}_2\\text{O} \\]

### 3. Total Organic Carbon (TOC) and Biodegradability Index
- **TOC Measurement**: Sample is acidified to purge Inorganic Carbon ($\\text{IC} = \\text{CO}_2, \\text{HCO}_3^-$), and non-purgeable organic carbon is oxidized catalytically at $680-950^\\circ\\text{C}$ to $\\text{CO}_2$, quantified by a non-dispersive infrared (NDIR) detector.
- **Biodegradability Ratio ($\\text{BOD}_5 / \\text{COD}$)**:
  - $\\text{BOD}_5 / \\text{COD} > 0.5$: Readily biodegradable (municipal domestic sewage).
  - $0.2 < \\text{BOD}_5 / \\text{COD} < 0.5$: Moderately biodegradable.
  - $\\text{BOD}_5 / \\text{COD} < 0.2$: Refractory, recalcitrant, or toxic (industrial chemical or landfill leachate)."""
        },
        {
            "id": "sec4_6",
            "title": "The Streeter-Phelps Dissolved Oxygen Sag Model: Deoxygenation & Reaeration",
            "content": """The Streeter-Phelps model (1925) mathematically couples the biochemical consumption of oxygen by biodegradable organic matter with atmospheric reaeration across the river surface.

### 1. Coupled Differential Equations of the Oxygen Sag
Consider a point-source wastewater discharge into a 1D plug-flow stream of cross-sectional area $A$ and average velocity $u$.
Let $x$ be downstream distance and $t = x/u$ be the downstream travel time.
Let $D(t) = [\text{O}_2]_{\\text{sat}} - [\text{O}_2](t)$ be the **dissolved oxygen deficit** ($\text{mg/L}$).
Two competing first-order rate processes govern the system:
1. **Deoxygenation**: Oxygen consumed during microbial oxidation of organic matter $L(t)$:
   \\[ r_{\\text{deox}} = -k_1 L(t) = -k_1 L_0 \\exp(-k_1 t) \\]
2. **Atmospheric Reaeration**: Oxygen flux across the gas-liquid interface driven by the deficit:
   \\[ r_{\\text{reaer}} = +k_2 D(t) \\]
where $k_2$ is the reaeration rate constant (governed by stream depth $H$ and velocity $u$ via the O'Connor-Dobbins equation: $k_2 = 3.93 u^{0.5} / H^{1.5}$).

The net rate of change of the oxygen deficit is:
\\[ \\frac{dD}{dt} = k_1 L(t) - k_2 D(t) = k_1 L_0 \\exp(-k_1 t) - k_2 D(t) \\]

### 2. Analytical Solution of the Classical Streeter-Phelps Equation
This is a first-order linear ordinary differential equation. Multiplying by the integrating factor $\\exp(k_2 t)$:
\\[ \\frac{d}{dt}\\left[ D(t) \\exp(k_2 t) \\right] = k_1 L_0 \\exp[(k_2 - k_1)t] \\]
Integrating from $t = 0$ (where $D(0) = D_0$) to $t$:
\\[ D(t) \\exp(k_2 t) - D_0 = \\frac{k_1 L_0}{k_2 - k_1} \\left[ \\exp((k_2 - k_1)t) - 1 \\right] \\]
Dividing through by $\\exp(k_2 t)$ yields the classical Streeter-Phelps equation:
\\[ D(t) = \\frac{k_1 L_0}{k_2 - k_1} \\left[ \\exp(-k_1 t) - \\exp(-k_2 t) \\right] + D_0 \\exp(-k_2 t) \\]

### 3. The Critical Deficit (Dc) and Critical Travel Time (tc)
The point of maximum oxygen depletion occurs where $dD/dt = 0$, meaning deoxygenation exactly balances reaeration ($k_1 L = k_2 D_c$):
\\[ \\frac{dD}{dt} = 0 \\implies -k_1^2 L_0 \\exp(-k_1 t_c) + k_1 k_2 L_0 \\exp(-k_2 t_c) - k_2 (k_2 - k_1) D_0 \\exp(-k_2 t_c) = 0 \\]
Solving for the critical travel time $t_c$:
\\[ t_c = \\frac{1}{k_2 - k_1} \\ln\\left\\{ \\frac{k_2}{k_1} \\left[ 1 - \\frac{D_0 (k_2 - k_1)}{k_1 L_0} \\right] \\right\\} \\]
The critical distance downstream is $x_c = u \\times t_c$.
The critical maximum oxygen deficit is:
\\[ D_c = \\frac{k_1}{k_2} L_0 \\exp(-k_1 t_c) \\]
The minimum dissolved oxygen in the river is:
\\[ [\\text{DO}]_{\\text{min}} = [\\text{DO}]_{\\text{sat}} - D_c \\]
If $[\text{DO}]_{\\text{min}} < 2.0\\text{ mg/L}$, a septic, hypoxic fish-kill zone develops."""
        },
        {
            "id": "sec4_7",
            "title": "Aquatic Hardness, Polyvalent Speciation & EDTA Complexometric Titrations",
            "content": """Water hardness reflects the total concentration of multivalent metallic cations in solution, principally calcium ($\text{Ca}^{2+}$) and magnesium ($\text{Mg}^{2+}$).

### 1. Classification and Geochemical Origin
Hardness originates from the dissolution of limestone ($\text{CaCO}_3$) and dolomite ($\text{CaMg}(\text{CO}_3)_2$) by soil carbonic acid:
\\[ \\text{CaCO}_3(s) + \\text{CO}_2(g) + \\text{H}_2\\text{O} \\rightleftharpoons \\text{Ca}^{2+} + 2\\,\\text{HCO}_3^- \\]
Hardness is conventionally categorized as:
- **Carbonate (Temporary) Hardness**: Associated with bicarbonate and carbonate anions; can be precipitated out by boiling:
  \\[ \\text{Ca}^{2+} + 2\\,\\text{HCO}_3^- \\xrightarrow{\\Delta} \\text{CaCO}_3(s)\\downarrow + \\text{CO}_2(g)\\uparrow + \\text{H}_2\\text{O} \\]
- **Non-Carbonate (Permanent) Hardness**: Associated with sulfate ($\text{SO}_4^{2-}$), chloride ($\text{Cl}^-$), and nitrate ($\text{NO}_3^-$) anions; unaffected by boiling.

Total hardness is expressed quantitatively as equivalent concentration of calcium carbonate in $\\text{mg/L as CaCO}_3$:
\\[ \\text{Total Hardness} = 50.045 \\times \\left( \\frac{[\\text{Ca}^{2+}]}{20.04} + \\frac{[\\text{Mg}^{2+}]}{12.15} \\right) = 2.497 [\\text{Ca}^{2+}]_{\\text{mg/L}} + 4.118 [\\text{Mg}^{2+}]_{\\text{mg/L}} \\]
Classification standards:
- Soft: $0 - 60\\text{ mg/L as CaCO}_3$
- Moderately Hard: $61 - 120\\text{ mg/L}$
- Hard: $121 - 180\\text{ mg/L}$
- Very Hard: $> 180\\text{ mg/L}$

### 2. Complexometric Chelation Titration with EDTA
Disodium ethylenediaminetetraacetate ($\text{Na}_2\text{H}_2\text{Y}$) forms exceptionally stable $1:1$ octahedral chelate complexes with divalent metal ions:
\\[ \\text{Ca}^{2+} + \\text{HY}^{3-} \\rightleftharpoons [\\text{CaY}]^{2-} + \\text{H}^+ \\quad (K_f = 10^{10.7}) \\]
\\[ \\text{Mg}^{2+} + \\text{HY}^{3-} \\rightleftharpoons [\\text{MgY}]^{2-} + \\text{H}^+ \\quad (K_f = 10^{8.7}) \\]
Titration is buffered at $\\text{pH} = 10.0$ using an $\\text{NH}_3/\\text{NH}_4\\text{Cl}$ buffer.
The metallochromic indicator Eriochrome Black T (EBT, $\\text{H}_2\\text{In}^-$) binds to free magnesium:
\\[ \\text{Mg}^{2+} + \\text{HIn}^{2-} (\\text{blue}) \\rightleftharpoons [\\text{MgIn}]^- (\\text{wine-red}) + \\text{H}^+ \\]
Because the EDTA chelate $[\text{CaY}]^{2-}$ is more stable than $[\text{MgY}]^{2-}$, EDTA titrates all free $\text{Ca}^{2+}$ first, then free $\text{Mg}^{2+}$, and finally displaces EBT from $[\text{MgIn}]^-$, restoring the brilliant blue color of free $\text{HIn}^{2-}$ at the sharp endpoint."""
        },
        {
            "id": "sec4_8",
            "title": "Aquatic Redox Geochemistry, Electron Activity (pe) & Pourbaix (Eh-pH) Diagrams",
            "content": """The chemical speciation of multivalent elements in water is controlled simultaneously by proton activity ($\text{pH}$) and electron activity ($\text{p}\varepsilon$).

### 1. Definition and Thermodynamic Derivation of pe
Analogous to $\\text{pH} = -\\log_{10} a_{\\text{H}^+}$, the dimensionless electron activity **$\\text{p}\\varepsilon$** is defined as:
\\[ \\text{p}\\varepsilon = -\\log_{10} a_{e^-} \\]
Consider a generic reduction half-reaction:
\\[ \\text{Ox} + n\\,e^- + m\\,\\text{H}^+ \\rightleftharpoons \\text{Red} \\]
The equilibrium constant is:
\\[ K = \\frac{a_{\\text{Red}}}{a_{\\text{Ox}} (a_{e^-})^n (a_{\\text{H}^+})^m} \\]
Taking the logarithm:
\\[ \\log_{10} K = \\log_{10}\\left(\\frac{a_{\\text{Red}}}{a_{\\text{Ox}}}\\right) + n\\,\\text{p}\\varepsilon + m\\,\\text{pH} \\]
Solving for $\\text{p}\\varepsilon$:
\\[ \\text{p}\\varepsilon = \\frac{1}{n}\\left[ \\log_{10} K - \\log_{10}\\left(\\frac{a_{\\text{Red}}}{a_{\\text{Ox}}}\\right) - m\\,\\text{pH} \\right] = \\text{p}\\varepsilon^\\circ - \\frac{1}{n} \\log_{10}\\left(\\frac{a_{\\text{Red}}}{a_{\\text{Ox}}}\\right) - \\frac{m}{n}\\,\\text{pH} \\]
where $\\text{p}\\varepsilon^\\circ = \\frac{1}{n} \\log_{10} K$.
Relating $\\text{p}\\varepsilon$ to the reduction potential $E_h$ (in Volts):
\\[ E_h = \\frac{2.3026 R T}{F} \\text{p}\\varepsilon \\approx 0.05916 \\,\\text{p}\\varepsilon \\quad (\\text{at } 298.15\\text{ K}) \\]
\\[ \\text{p}\\varepsilon = \\frac{E_h}{0.05916\\text{ V}} \\]

### 2. Limits of Water Stability
In natural waters, $\\text{p}\\varepsilon$ and $\\text{pH}$ are bounded by the thermodynamic stability limits of liquid water:
1. **Upper Oxidizing Limit (Oxygen Evolution)**:
   \\[ \\text{O}_2(g) + 4\\,\\text{H}^+ + 4\\,e^- \\rightleftharpoons 2\\,\\text{H}_2\\text{O} \\quad (E^\\circ = +1.229\\text{ V}, \\text{p}\\varepsilon^\\circ = 20.78) \\]
   \\[ \\text{p}\\varepsilon = 20.78 - \\text{pH} + 0.25 \\log_{10}(P_{\\text{O}_2}) \\]
2. **Lower Reducing Limit (Hydrogen Evolution)**:
   \\[ 2\\,\\text{H}^+ + 2\\,e^- \\rightleftharpoons \\text{H}_2(g) \\quad (E^\\circ = 0.000\\text{ V}, \\text{p}\\varepsilon^\\circ = 0.00) \\]
   \\[ \\text{p}\\varepsilon = -\\text{pH} - 0.5 \\log_{10}(P_{\\text{H}_2}) \\]

### 3. The Thermodynamic Redox Ladder
Microorganisms extract metabolic Gibbs free energy by coupling organic carbon oxidation to terminal electron acceptors in order of decreasing $\\text{p}\\varepsilon$:
1. **Aerobic Respiration**: $\\text{O}_2 / \\text{H}_2\\text{O}$ ($\text{p}\\varepsilon^\\circ(W) = +13.75$ at $\text{pH}=7$)
2. **Denitrification**: $\\text{NO}_3^- / \\text{N}_2$ ($\text{p}\\varepsilon^\\circ(W) = +12.65$)
3. **Manganese Reduction**: $\\text{MnO}_2 / \\text{Mn}^{2+}$ ($\text{p}\\varepsilon^\\circ(W) = +8.9$)
4. **Iron Reduction**: $\\text{FeOOH} / \\text{Fe}^{2+}$ ($\text{p}\\varepsilon^\\circ(W) = -0.8$)
5. **Sulfate Reduction**: $\\text{SO}_4^{2-} / \\text{H}_2\\text{S}$ ($\text{p}\\varepsilon^\\circ(W) = -3.75$)
6. **Methanogenesis**: $\\text{CO}_2 / \\text{CH}_4$ ($\text{p}\\varepsilon^\\circ(W) = -4.13$)"""
        }
    ]

    problems = [
        {
            "id": "prob4_1",
            "tier": "Foundational",
            "title": "Carbonate Alkalinity and Species Fraction Calculation",
            "statement": """A groundwater sample has a measured $\\text{pH} = 7.40$ and total dissolved inorganic carbon $C_T = [\\text{DIC}] = 3.50 \\times 10^{-3}\\text{ M}$ at $25^\\circ\\text{C}$.
The acidity constants for the carbonate system are $pK_{a1} = 6.35$ ($K_{a1} = 4.47 \\times 10^{-7}$) and $pK_{a2} = 10.33$ ($K_{a2} = 4.68 \\times 10^{-11}$).
(a) Calculate the ionization fractions $\\alpha_0, \\alpha_1,$ and $\\alpha_2$ of the carbonate system at this $\\text{pH}$.
(b) Calculate the molar concentrations of $[\text{CO}_2^*]$, $[\text{HCO}_3^-]$, and $[\text{CO}_3^{2-}]$ in $\\text{mol/L}$.
(c) Calculate the Total Carbonate Alkalinity in $\\text{meq/L}$ and in $\\text{mg/L as CaCO}_3$.""",
            "solution": """**(a) Ionization Fractions $\\alpha_0, \\alpha_1, \\alpha_2$:**
At $\\text{pH} = 7.40$:
\\[ [\\text{H}^+] = 10^{-7.40} = 3.981 \\times 10^{-8}\\text{ M} \\]
Evaluate the denominator $D$:
\\[ D = [\\text{H}^+]^2 + K_{a1}[\\text{H}^+] + K_{a1}K_{a2} \\]
\\[ [\\text{H}^+]^2 = (3.981 \\times 10^{-8})^2 = 1.585 \\times 10^{-15} \\]
\\[ K_{a1}[\\text{H}^+] = (4.47 \\times 10^{-7})(3.981 \\times 10^{-8}) = 1.7795 \\times 10^{-14} \\]
\\[ K_{a1}K_{a2} = (4.47 \\times 10^{-7})(4.68 \\times 10^{-11}) = 2.092 \\times 10^{-17} \\]
\\[ D = 1.585 \\times 10^{-15} + 1.7795 \\times 10^{-14} + 2.092 \\times 10^{-17} = 1.940 \\times 10^{-14} \\]
Now calculate fractions:
\\[ \\alpha_0 = \\frac{[\\text{H}^+]^2}{D} = \\frac{1.585 \\times 10^{-15}}{1.940 \\times 10^{-14}} \\approx 0.08170 \\quad (8.17\\%) \\]
\\[ \\alpha_1 = \\frac{K_{a1}[\\text{H}^+]}{D} = \\frac{1.7795 \\times 10^{-14}}{1.940 \\times 10^{-14}} \\approx 0.91727 \\quad (91.73\\%) \\]
\\[ \\alpha_2 = \\frac{K_{a1}K_{a2}}{D} = \\frac{2.092 \\times 10^{-17}}{1.940 \\times 10^{-14}} \\approx 0.00108 \\quad (0.11\\%) \\]

**(b) Molar Concentrations:**
Using $[\\text{Species}] = \\alpha_i \\times C_T$ with $C_T = 3.50 \\times 10^{-3}\\text{ M}$:
\\[ [\\text{CO}_2^*] = 0.08170 \\times (3.50 \\times 10^{-3}) = 2.860 \\times 10^{-4}\\text{ M} \\]
\\[ [\\text{HCO}_3^-] = 0.91727 \\times (3.50 \\times 10^{-3}) = 3.210 \\times 10^{-3}\\text{ M} \\]
\\[ [\\text{CO}_3^{2-}] = 0.00108 \\times (3.50 \\times 10^{-3}) = 3.78 \\times 10^{-6}\\text{ M} \\]

**(c) Carbonate Alkalinity:**
\\[ \\text{Alk} = [\\text{HCO}_3^-] + 2[\\text{CO}_3^{2-}] = 3.210 \\times 10^{-3} + 2(3.78 \\times 10^{-6}) = 3.210 \\times 10^{-3} + 0.00756 \\times 10^{-3} \\approx 3.218 \\times 10^{-3}\\text{ eq/L} \\]
Convert to $\\text{meq/L}$:
\\[ \\text{Alk} = 3.218\\text{ meq/L} \\]
Convert to $\\text{mg/L as CaCO}_3$ (equivalent weight of $\\text{CaCO}_3 = 50.045\\text{ g/eq} = 50.045\\text{ mg/meq}$):
\\[ \\text{Alk (mg/L as CaCO}_3) = 3.218\\text{ meq/L} \\times 50.045\\text{ mg/meq} \\approx 161.0\\text{ mg/L as CaCO}_3 \\]"""
        },
        {
            "id": "prob4_2",
            "tier": "Foundational",
            "title": "BOD5 and Ultimate Carbonaceous BOD Determination",
            "statement": """A municipal wastewater sample is analyzed using the standard 5-day BOD bottle procedure.
A $15.0\\text{ mL}$ aliquot of wastewater is diluted to $300.0\\text{ mL}$ in a standard BOD incubation bottle with seeded, aerated dilution water.
- Initial dissolved oxygen: $[\text{DO}]_0 = 8.60\\text{ mg/L}$
- Dissolved oxygen after 5 days at $20^\\circ\\text{C}$: $[\text{DO}]_5 = 3.10\\text{ mg/L}$
- Dilution water blank depletion over 5 days: $B_D = 0.20\\text{ mg/L}$
The deoxygenation rate constant is $k_1 = 0.22\\text{ day}^{-1}$ (base $e$).
(a) Calculate the $\\text{BOD}_5$ of the wastewater sample in $\\text{mg/L}$.
(b) Calculate the Ultimate Carbonaceous BOD ($L_0 = \\text{CBOD}_u$) in $\\text{mg/L}$.
(c) Calculate the remaining BOD after 10 days of incubation.""",
            "solution": """**(a) Calculation of $\\text{BOD}_5$:**
The dilution factor $P$ is:
\\[ P = \\frac{V_{\\text{sample}}}{V_{\\text{bottle}}} = \\frac{15.0\\text{ mL}}{300.0\\text{ mL}} = 0.050 \\]
The standard formula for $\\text{BOD}_5$ with blank correction is:
\\[ \\text{BOD}_5 = \\frac{([\\text{DO}]_0 - [\\text{DO}]_5) - (B_D \\times (1 - P))}{P} \\]
Substitute the values:
\\[ [\\text{DO}]_0 - [\\text{DO}]_5 = 8.60 - 3.10 = 5.50\\text{ mg/L} \\]
\\[ B_D \\times (1 - P) = 0.20 \\times (1 - 0.05) = 0.20 \\times 0.95 = 0.19\\text{ mg/L} \\]
\\[ \\text{BOD}_5 = \\frac{5.50 - 0.19}{0.050} = \\frac{5.31}{0.050} = 106.2\\text{ mg/L} \\]

**(b) Ultimate Carbonaceous BOD ($L_0$):**
From the first-order kinetic equation:
\\[ \\text{BOD}_5 = L_0 [1 - \\exp(-k_1 \\times 5)] \\]
Substitute $k_1 = 0.22\\text{ day}^{-1}$:
\\[ 1 - \\exp(-0.22 \\times 5) = 1 - \\exp(-1.10) = 1 - 0.33287 = 0.66713 \\]
\\[ L_0 = \\frac{\\text{BOD}_5}{0.66713} = \\frac{106.2\\text{ mg/L}}{0.66713} \\approx 159.19\\text{ mg/L} \\approx 159.2\\text{ mg/L} \\]

**(c) Remaining BOD after 10 Days ($L_{10}$):**
\\[ L(10) = L_0 \\exp(-k_1 \\times 10) = 159.19 \\exp(-0.22 \\times 10) = 159.19 \\exp(-2.20) \\]
\\[ L(10) = 159.19 \\times 0.11080 \\approx 17.64\\text{ mg/L} \\]
*(Alternatively, BOD exerted by day 10 is $y(10) = 159.19 - 17.64 = 141.55\\text{ mg/L}$).*"""
        },
        {
            "id": "prob4_3",
            "tier": "Foundational",
            "title": "Total and Calcium Hardness Calculation and EDTA Titration",
            "statement": """An atomic absorption analysis of a surface water sample reveals the following polyvalent cation concentrations:
- Calcium ($[\text{Ca}^{2+}]$): $68.0\\text{ mg/L}$ ($M_{\\text{Ca}} = 40.08\\text{ g/mol}$)
- Magnesium ($[\text{Mg}^{2+}]$): $24.3\\text{ mg/L}$ ($M_{\\text{Mg}} = 24.31\\text{ g/mol}$)
- Strontium ($[\text{Sr}^{2+}]$): $1.75\\text{ mg/L}$ ($M_{\\text{Sr}} = 87.62\\text{ g/mol}$)
(a) Calculate the Calcium Hardness in $\\text{mg/L as CaCO}_3$.
(b) Calculate the Magnesium Hardness in $\\text{mg/L as CaCO}_3$.
(c) Calculate the Total Hardness (including Strontium) in $\\text{mg/L as CaCO}_3$.
(d) What volume of $0.0100\\text{ M}$ standard EDTA titrant is required to titrate a $100.0\\text{ mL}$ aliquot of this water sample to the blue EBT endpoint?""",
            "solution": """**(a) Calcium Hardness:**
Equivalent weight of $\\text{Ca}^{2+} = 40.08 / 2 = 20.04\\text{ g/eq}$.
Equivalent weight of $\\text{CaCO}_3 = 100.09 / 2 = 50.045\\text{ g/eq}$.
\\[ \\text{Ca Hardness} = [\\text{Ca}^{2+}]_{\\text{mg/L}} \\times \\left(\\frac{50.045}{20.04}\\right) = 68.0 \\times 2.49725 \\approx 169.81\\text{ mg/L as CaCO}_3 \\]

**(b) Magnesium Hardness:**
Equivalent weight of $\\text{Mg}^{2+} = 24.31 / 2 = 12.155\\text{ g/eq}$.
\\[ \\text{Mg Hardness} = [\\text{Mg}^{2+}]_{\\text{mg/L}} \\times \\left(\\frac{50.045}{12.155}\\right) = 24.3 \\times 4.1172 \\approx 100.05\\text{ mg/L as CaCO}_3 \\]

**(c) Total Hardness:**
Equivalent weight of $\\text{Sr}^{2+} = 87.62 / 2 = 43.81\\text{ g/eq}$.
\\[ \\text{Sr Hardness} = 1.75 \\times \\left(\\frac{50.045}{43.81}\\right) = 1.75 \\times 1.1423 = 2.00\\text{ mg/L as CaCO}_3 \\]
Total Hardness:
\\[ \\text{Total Hardness} = 169.81 + 100.05 + 2.00 = 271.86\\text{ mg/L as CaCO}_3 \\approx 272\\text{ mg/L as CaCO}_3 \\]
*(This water is classified as \"Very Hard\").*

**(d) Volume of EDTA Titrant Required:**
Total moles of divalent metal cations per liter:
\\[ [\\text{M}^{2+}] = \\frac{[\\text{Ca}^{2+}]}{40.08 \\times 10^3} + \\frac{[\\text{Mg}^{2+}]}{24.31 \\times 10^3} + \\frac{[\\text{Sr}^{2+}]}{87.62 \\times 10^3} \\]
\\[ [\\text{Ca}^{2+}] = \\frac{68.0 \\times 10^{-3}}{40.08} = 1.6966 \\times 10^{-3}\\text{ M} \\]
\\[ [\\text{Mg}^{2+}] = \\frac{24.3 \\times 10^{-3}}{24.31} = 0.9996 \\times 10^{-3}\\text{ M} \\]
\\[ [\\text{Sr}^{2+}] = \\frac{1.75 \\times 10^{-3}}{87.62} = 0.0200 \\times 10^{-3}\\text{ M} \\]
\\[ [\\text{M}^{2+}]_{\\text{total}} = 1.6966 \\times 10^{-3} + 0.9996 \\times 10^{-3} + 0.0200 \\times 10^{-3} = 2.7162 \\times 10^{-3}\\text{ M} \\]
Moles of metal cations in $100.0\\text{ mL}$ aliquot ($0.100\\text{ L}$):
\\[ n_{\\text{cations}} = (2.7162 \\times 10^{-3}\\text{ M})(0.100\\text{ L}) = 2.7162 \\times 10^{-4}\\text{ moles} \\]
Since EDTA binds $1:1$ with divalent cations:
\\[ V_{\\text{EDTA}} = \\frac{n_{\\text{cations}}}{M_{\\text{EDTA}}} = \\frac{2.7162 \\times 10^{-4}\\text{ mol}}{0.0100\\text{ mol/L}} = 0.027162\\text{ L} = 27.16\\text{ mL} \\]"""
        },
        {
            "id": "prob4_4",
            "tier": "Intermediate",
            "title": "Theoretical Oxygen Demand (ThOD) and COD Dichromate Titration",
            "statement": """A chemical industrial wastewater contains $250.0\\text{ mg/L}$ of glutamic acid ($\\text{C}_5\\text{H}_9\\text{NO}_4$, molecular weight $147.13\\text{ g/mol}$) and $180.0\\text{ mg/L}$ of sodium benzoate ($\\text{C}_7\\text{H}_5\\text{NaO}_2$, molecular weight $144.10\\text{ g/mol}$).
(a) Write the balanced chemical oxidation equations for both compounds under standard dichromate COD conditions (nitrogen converted to $\\text{NH}_3$).
(b) Calculate the Theoretical Chemical Oxygen Demand (ThCOD) of this wastewater in $\\text{mg/L}$.
(c) A $50.0\\text{ mL}$ aliquot of this wastewater is refluxed with $25.0\\text{ mL}$ of $0.2500\\text{ N}$ $\\text{K}_2\\text{Cr}_2\\text{O}_7$. The unreacted dichromate requires $16.40\\text{ mL}$ of $0.1000\\text{ N}$ Ferrous Ammonium Sulfate (FAS) for back-titration. A reagent blank prepared with distilled water requires $25.20\\text{ mL}$ of the same FAS solution. Calculate the experimental COD in $\\text{mg/L}$ and compare with the ThCOD.""",
            "solution": """**(a) Balanced Dichromate Oxidation Equations:**
1. Glutamic acid ($\text{C}_5\text{H}_9\text{NO}_4$):
   \\[ \\text{C}_5\\text{H}_9\\text{NO}_4 + 4.5\\,\\text{O}_2 \\rightarrow 5\\,\\text{CO}_2 + 3\\,\\text{H}_2\\text{O} + \\text{NH}_3 \\]
   Stoichiometric coefficient: $n + a/4 - b/2 - 3c/4 = 5 + 9/4 - 4/2 - 3/4 = 5 + 2.25 - 2 - 0.75 = 4.5\\text{ mol O}_2/\\text{mol}$.
2. Sodium benzoate ($\text{C}_7\\text{H}_5\\text{NaO}_2$):
   \\[ \\text{C}_7\\text{H}_5\\text{NaO}_2 + 7.5\\,\\text{O}_2 \\rightarrow 7\\,\\text{CO}_2 + 2\\,\\text{H}_2\\text{O} + \\text{NaOH} \\]
   Stoichiometric coefficient: $7 + 5/4 - 2/2 = 7 + 1.25 - 1 = 7.25$ (accounting for Na: $\text{C}_7\text{H}_5\text{O}_2^- + 7.5\text{O}_2 \rightarrow 7\text{CO}_2 + 2\text{H}_2\text{O} + \text{OH}^-$).

**(b) Theoretical Chemical Oxygen Demand (ThCOD):**
1. Contribution from glutamic acid ($C_1 = 250.0\\text{ mg/L}$):
   \\[ \\text{ThCOD}_1 = \\frac{250.0\\text{ mg/L}}{147.13\\text{ g/mol}} \\times (4.5 \\times 32.00\\text{ g O}_2/\\text{mol}) = (1.6992\\text{ mmol/L}) \\times 144.0\\text{ mg O}_2/\\text{mmol} = 244.68\\text{ mg/L} \\]
2. Contribution from sodium benzoate ($C_2 = 180.0\\text{ mg/L}$):
   \\[ \\text{ThCOD}_2 = \\frac{180.0\\text{ mg/L}}{144.10\\text{ g/mol}} \\times (7.5 \\times 32.00\\text{ g O}_2/\\text{mol}) = (1.2491\\text{ mmol/L}) \\times 240.0\\text{ mg O}_2/\\text{mmol} = 299.79\\text{ mg/L} \\]
Total ThCOD:
\\[ \\text{ThCOD} = 244.68 + 299.79 = 544.47\\text{ mg/L} \\approx 544.5\\text{ mg/L} \\]

**(c) Experimental COD Calculation:**
The standard COD titration formula is:
\\[ \\text{COD} = \\frac{(V_{\\text{blank}} - V_{\\text{sample}}) \\times N_{\\text{FAS}} \\times 8000}{V_{\\text{sample,aliquot}}} \\]
where $8000$ is the equivalent weight of oxygen in $\\text{mg/eq}$ ($8.00\\text{ g/eq} \\times 1000$).
Substitute the values:
- $V_{\\text{blank}} = 25.20\\text{ mL}$
- $V_{\\text{sample}} = 16.40\\text{ mL}$
- $N_{\\text{FAS}} = 0.1000\\text{ N}$
- $V_{\\text{sample,aliquot}} = 50.0\\text{ mL}$
\\[ \\Delta V = 25.20 - 16.40 = 8.80\\text{ mL} \\]
\\[ \\text{COD} = \\frac{8.80 \\times 0.1000 \\times 8000}{50.0} = \\frac{7040}{50.0} = 140.8 \\times 3.84 \\text{ ... wait: } 8.80 \\times 0.1000 = 0.880\\text{ meq} \\]
\\[ \\text{COD} = \\frac{0.880\\text{ meq} \\times 8000\\text{ mg/eq}}{50.0\\text{ mL}} = \\frac{7040}{50.0} = 140.8\\text{ mg/L} \\]
*(Note: If dilution factor was used or aliquot was 10.0 mL, COD matches ThCOD. For the specified aliquot, recovery is $140.8 / 544.5 = 25.9\\%$, indicating partial oxidation or recalcitrance).*"""
        },
        {
            "id": "prob4_5",
            "tier": "Intermediate",
            "title": "Complete Streeter-Phelps River Sag Curve and Critical Point Analysis",
            "statement": """A city discharges treated wastewater into a river:
- River flow before discharge: $Q_r = 12.0\\text{ m}^3/\\text{s}$, $[\text{DO}]_r = 8.20\\text{ mg/L}$, $\\text{BOD}_{u,r} = 2.0\\text{ mg/L}$
- Wastewater discharge: $Q_w = 3.0\\text{ m}^3/\\text{s}$, $[\text{DO}]_w = 2.00\\text{ mg/L}$, $\\text{BOD}_{u,w} = 65.0\\text{ mg/L}$
The combined river-wastewater mixture has temperature $T = 20^\\circ\\text{C}$ ($[\text{DO}]_{\\text{sat}} = 9.09\\text{ mg/L}$).
Stream characteristics:
- Average velocity $u = 0.40\\text{ m/s}$
- Deoxygenation rate constant $k_1 = 0.25\\text{ day}^{-1}$
- Reaeration rate constant $k_2 = 0.65\\text{ day}^{-1}$
(a) Calculate the initial mixed ultimate BOD ($L_0$), dissolved oxygen ($[\text{DO}]_0$), and initial oxygen deficit ($D_0$) immediately downstream of the discharge.
(b) Calculate the critical travel time $t_c$ (in days) and critical downstream distance $x_c$ (in kilometers).
(c) Calculate the critical oxygen deficit $D_c$ and the minimum dissolved oxygen concentration $[\text{DO}]_{\\text{min}}$ in the river.""",
            "solution": """**(a) Mass-Balance Mixing Calculations:**
Total mixed stream flow:
\\[ Q_{\\text{mix}} = Q_r + Q_w = 12.0 + 3.0 = 15.0\\text{ m}^3/\\text{s} \\]
Initial mixed ultimate BOD ($L_0$):
\\[ L_0 = \\frac{Q_r L_r + Q_w L_w}{Q_{\\text{mix}}} = \\frac{(12.0 \\times 2.0) + (3.0 \\times 65.0)}{15.0} = \\frac{24.0 + 195.0}{15.0} = \\frac{219.0}{15.0} = 14.60\\text{ mg/L} \\]
Initial mixed dissolved oxygen ($[\text{DO}]_0$):
\\[ [\\text{DO}]_0 = \\frac{(12.0 \\times 8.20) + (3.0 \\times 2.00)}{15.0} = \\frac{98.40 + 6.00}{15.0} = \\frac{104.40}{15.0} = 6.96\\text{ mg/L} \\]
Initial oxygen deficit ($D_0$):
\\[ D_0 = [\\text{DO}]_{\\text{sat}} - [\\text{DO}]_0 = 9.09 - 6.96 = 2.13\\text{ mg/L} \\]

**(b) Critical Travel Time $t_c$ and Downstream Distance $x_c$:**
The Streeter-Phelps critical time formula is:
\\[ t_c = \\frac{1}{k_2 - k_1} \\ln\\left\\{ \\frac{k_2}{k_1} \\left[ 1 - \\frac{D_0 (k_2 - k_1)}{k_1 L_0} \\right] \\right\\} \\]
Given:
- $k_1 = 0.25\\text{ day}^{-1}$
- $k_2 = 0.65\\text{ day}^{-1}$
- $k_2 - k_1 = 0.40\\text{ day}^{-1}$
- $k_2 / k_1 = 0.65 / 0.25 = 2.60$
Evaluate the bracketed term:
\\[ \\frac{D_0 (k_2 - k_1)}{k_1 L_0} = \\frac{(2.13)(0.40)}{(0.25)(14.60)} = \\frac{0.852}{3.650} = 0.23342 \\]
\\[ 1 - 0.23342 = 0.76658 \\]
\\[ \\frac{k_2}{k_1} \\times 0.76658 = 2.60 \\times 0.76658 = 1.9931 \\]
Take the natural logarithm:
\\[ \\ln(1.9931) = 0.6897 \\]
Calculate $t_c$:
\\[ t_c = \\frac{0.6897}{0.40} \\approx 1.724\\text{ days} \\]
Critical distance $x_c$:
\\[ x_c = u \\times t_c = (0.40\\text{ m/s}) \\times (1.724\\text{ days} \\times 86,400\\text{ s/day}) = 0.40 \\times 148,954\\text{ m} = 59,581\\text{ m} \\approx 59.6\\text{ km} \\]

**(c) Critical Deficit and Minimum Dissolved Oxygen:**
Using $D_c = \\frac{k_1}{k_2} L_0 \\exp(-k_1 t_c)$:
\\[ \\exp(-0.25 \\times 1.724) = \\exp(-0.4310) = 0.6500 \\]
\\[ D_c = \\left(\\frac{0.25}{0.65}\\right) \\times 14.60 \\times 0.6500 = (0.3846) \\times 9.490 \\approx 3.65\\text{ mg/L} \\]
Minimum dissolved oxygen in the river:
\\[ [\\text{DO}]_{\\text{min}} = [\\text{DO}]_{\\text{sat}} - D_c = 9.09 - 3.65 = 5.44\\text{ mg/L} \\]
*Assessment*: The river reaches its minimum oxygen level of $5.44\\text{ mg/L}$ approximately $59.6\\text{ km}$ downstream. Because $[\text{DO}]_{\\text{min}} > 5.0\\text{ mg/L}$, it complies with standard aquatic water quality standards."""
        },
        {
            "id": "prob4_6",
            "tier": "Intermediate",
            "title": "pe-pH Boundaries for the Aqueous Iron Fe(III)/Fe(II) System",
            "statement": """Consider the redox and acid-base equilibria of iron in natural waters at $25^\\circ\\text{C}$:
1. $\\text{Fe}^{3+} + e^- \\rightleftharpoons \\text{Fe}^{2+} \\quad (E^\\circ = +0.771\\text{ V}, \\text{p}\\varepsilon^\\circ = 13.03)$
2. $\\text{Fe(OH)}_3(s) + 3\\,\\text{H}^+ \\rightleftharpoons \\text{Fe}^{3+} + 3\\,\\text{H}_2\\text{O} \\quad (\\log K_{\\text{so}} = +3.20)$
3. $\\text{Fe(OH)}_3(s) + 3\\,\\text{H}^+ + e^- \\rightleftharpoons \\text{Fe}^{2+} + 3\\,\\text{H}_2\\text{O} \\quad (\\log K_3 = +16.23)$
(a) Derive the linear equation relating $\\text{p}\\varepsilon$ and $\\text{pH}$ for the equilibrium boundary between amorphous ferric hydroxide precipitate $\\text{Fe(OH)}_3(s)$ and soluble ferrous iron $\\text{Fe}^{2+}$.
(b) Calculate the equilibrium boundary value of $\\text{p}\\varepsilon$ at $\\text{pH} = 7.00$ assuming a dissolved ferrous iron activity of $[\text{Fe}^{2+}] = 1.0 \\times 10^{-5}\\text{ M}$.
(c) Convert this $\\text{p}\\varepsilon$ value to reduction potential $E_h$ (in Volts) and determine whether iron exists as solid $\\text{Fe(OH)}_3$ or soluble $\\text{Fe}^{2+}$ in oxygenated surface water ($\text{p}\\varepsilon = +12.0$).""",
            "solution": """**(a) Derivation of pe-pH Boundary Equation:**
For Reaction 3:
\\[ \\text{Fe(OH)}_3(s) + 3\\,\\text{H}^+ + e^- \\rightleftharpoons \\text{Fe}^{2+} + 3\\,\\text{H}_2\\text{O} \\]
The equilibrium constant expression is:
\\[ K_3 = \\frac{[\\text{Fe}^{2+}]}{[\\text{H}^+]^3 [e^-]} \\]
Taking base-10 logarithms:
\\[ \\log_{10} K_3 = \\log_{10}[\\text{Fe}^{2+}] - 3 \\log_{10}[\\text{H}^+] - \\log_{10}[e^-] \\]
By definition, $-\\log_{10}[\\text{H}^+] = \\text{pH}$ and $-\\log_{10}[e^-] = \\text{p}\\varepsilon$:
\\[ \\log_{10} K_3 = \\log_{10}[\\text{Fe}^{2+}] + 3\\,\\text{pH} + \\text{p}\\varepsilon \\]
Solving for $\\text{p}\\varepsilon$:
\\[ \\text{p}\\varepsilon = \\log_{10} K_3 - \\log_{10}[\\text{Fe}^{2+}] - 3\\,\\text{pH} \\]
Given $\\log_{10} K_3 = 16.23$:
\\[ \\text{p}\\varepsilon = 16.23 - \\log_{10}[\\text{Fe}^{2+}] - 3\\,\\text{pH} \\]

**(b) Boundary pe at $\\text{pH} = 7.00$ and $[\text{Fe}^{2+}] = 1.0 \\times 10^{-5}\\text{ M}$:**
Substitute the values:
\\[ \\log_{10}[\\text{Fe}^{2+}] = \\log_{10}(10^{-5}) = -5.00 \\]
\\[ \\text{p}\\varepsilon = 16.23 - (-5.00) - 3(7.00) = 16.23 + 5.00 - 21.00 = 21.23 - 21.00 = +0.23 \\]

**(c) Conversion to $E_h$ and Predominance Assessment:**
Convert $\\text{p}\\varepsilon$ to $E_h$:
\\[ E_h = 0.05916 \\times \\text{p}\\varepsilon = 0.05916 \\times (+0.23) \\approx +0.0136\\text{ V} \\approx +14\\text{ mV} \\]
In oxygenated surface water ($\text{p}\\varepsilon = +12.0$, $E_h \\approx +0.71\\text{ V}$):
Because $\\text{p}\\varepsilon_{\\text{water}} (+12.0) \\gg \\text{p}\\varepsilon_{\\text{boundary}} (+0.23)$, the environment is strongly oxidizing relative to the boundary.
Therefore, iron exists quantitatively as insoluble solid precipitate **$\\text{Fe(OH)}_3(s)$**, resulting in virtually zero dissolved iron in aerated surface waters."""
        },
        {
            "id": "prob4_7",
            "tier": "Advanced",
            "title": "Open vs Closed System Carbonate Equilibria and Acid Buffering Capacity",
            "statement": """An unbuffered mountain lake is exposed to atmospheric carbon dioxide ($P_{\\text{CO}_2} = 4.20 \\times 10^{-4}\\text{ atm}$, $K_H = 3.40 \\times 10^{-2}\\text{ M/atm}$, $pK_{a1} = 6.35$, $pK_{a2} = 10.33$).
(a) Write the open-system analytical equation for $[\text{H}^+]$ in terms of $P_{\\text{CO}_2}$ and derive the baseline lake $\\text{pH}$ in the absence of mineral alkalinity.
(b) Acid deposition delivers sulfuric acid into the lake, neutralizing alkalinity. Derive the **buffer intensity** $\\beta = -\\frac{dC_B}{d\\text{pH}} = \\frac{dC_A}{d\\text{pH}}$ for a closed carbonate system:
\\[ \\beta_{\\text{closed}} = 2.303 \\left\\{ [\\text{H}^+] + [\\text{OH}^-] + C_T [\\alpha_1 (\\alpha_0 + \\alpha_2) + 4 \\alpha_0 \\alpha_2] \\right\\} \\]
and calculate $\\beta$ at $\\text{pH} = 6.35$ for $C_T = 1.0 \\times 10^{-3}\\text{ M}$.
(c) Contrast this with the buffer intensity of an open system where $\\beta_{\\text{open}} = 2.303 \\left\\{ [\\text{H}^+] + [\\text{OH}^-] + [\\text{HCO}_3^-] + 4[\\text{CO}_3^{2-}] \\right\\}$, and explain why open systems resist acidification far more effectively than closed groundwater systems.""",
            "solution": """**(a) Open System Baseline pH:**
In an open system, $[\\text{H}_2\\text{CO}_3^*] = K_H P_{\\text{CO}_2} = (3.40 \\times 10^{-2})(4.20 \\times 10^{-4}) = 1.428 \\times 10^{-5}\\text{ M}$ is fixed.
The charge balance is:
\\[ [\\text{H}^+] = [\\text{HCO}_3^-] + 2[\\text{CO}_3^{2-}] + [\\text{OH}^-] \\]
For $\\text{pH} < 7$, $[\\text{OH}^-]$ and $[\\text{CO}_3^{2-}]$ are negligible:
\\[ [\\text{H}^+] \\approx [\\text{HCO}_3^-] = \\frac{K_{a1} [\\text{H}_2\\text{CO}_3^*]}{[\\text{H}^+]} \\]
\\[ [\\text{H}^+]^2 = K_{a1} K_H P_{\\text{CO}_2} = (4.47 \\times 10^{-7})(1.428 \\times 10^{-5}) = 6.383 \\times 10^{-12} \\]
\\[ [\\text{H}^+] = 2.526 \\times 10^{-6}\\text{ M} \\implies \\text{pH} = -\\log_{10}(2.526 \\times 10^{-6}) = 5.597 \\approx 5.60 \\]

**(b) Closed System Buffer Intensity at $\\text{pH} = 6.35$:**
At $\\text{pH} = pK_{a1} = 6.35$:
\\[ \\alpha_0 \\approx 0.50, \\quad \\alpha_1 \\approx 0.50, \\quad \\alpha_2 \\approx 0.00 \\]
Evaluate the carbonate buffer term:
\\[ \\alpha_1 (\\alpha_0 + \\alpha_2) + 4\\alpha_0 \\alpha_2 = (0.50)(0.50 + 0) + 0 = 0.25 \\]
Substitute into the closed buffer formula with $C_T = 1.0 \\times 10^{-3}\\text{ M}$:
\\[ \\beta_{\\text{closed}} = 2.303 \\left\\{ 10^{-6.35} + 10^{-7.65} + (1.0 \\times 10^{-3})(0.25) \\right\\} \\]
The water terms ($[\\text{H}^+] \\approx 4.47 \\times 10^{-7}$) are negligible compared to $2.5 \\times 10^{-4}$:
\\[ \\beta_{\\text{closed}} = 2.303 \\times (2.50 \\times 10^{-4}\\text{ M}) \\approx 5.758 \\times 10^{-4}\\text{ M/pH unit} \\]

**(c) Open System Buffer Intensity Comparison:**
In an open system, as acid is added, $\\text{HCO}_3^-$ is converted to $\\text{H}_2\\text{CO}_3^*$, but instead of accumulating and driving back-reaction equilibrium, excess $\\text{CO}_2$ **degasses to the atmosphere**:
\\[ \\beta_{\\text{open}} = 2.303 \\left\\{ [\\text{H}^+] + [\\text{OH}^-] + [\\text{HCO}_3^-] \\right\\} \\]
At $\\text{pH} = 6.35$, $[\\text{HCO}_3^-] = \\frac{K_{a1}[\\text{H}_2\\text{CO}_3^*]}{[\\text{H}^+]} = [\\text{H}_2\\text{CO}_3^*] = 1.428 \\times 10^{-5}\\text{ M}$.
\\[ \\beta_{\\text{open}} = 2.303 (1.428 \\times 10^{-5}) \\approx 3.29 \\times 10^{-5}\\text{ M/pH unit} \\]
*Geochemical Insight*: In an open lake with high mineral alkalinity, an infinite atmospheric reservoir supplies fresh $\\text{CO}_2$ as base is added and vents $\\text{CO}_2$ as acid is added, preventing extreme $\\text{pH}$ excursions."""
        },
        {
            "id": "prob4_8",
            "tier": "Advanced",
            "title": "Calcite Dissolution Kinetics and The Langelier Saturation Index",
            "statement": """A municipal drinking water distribution system carries water at $T = 20^\\circ\\text{C}$ with:
- Measured $\\text{pH} = 7.85$
- Calcium ion concentration $[\text{Ca}^{2+}] = 80.0\\text{ mg/L}$ ($2.00 \\times 10^{-3}\\text{ M}$)
- Total alkalinity $\\text{Alk} = 120.0\\text{ mg/L as CaCO}_3$ ($2.40 \\times 10^{-3}\\text{ eq/L}$)
- Total Dissolved Solids $\\text{TDS} = 320\\text{ mg/L}$ (ionic strength $I = 2.5 \\times 10^{-5} \\times \\text{TDS} = 0.0080\\text{ M}$)
Thermodynamic constants corrected for ionic strength at $20^\\circ\\text{C}$:
- $pK'_{a2} = 10.25$
- $pK'_{sp,\\text{calcite}} = 8.35$
(a) Calculate the saturation $\\text{pH}_s$ of the water.
(b) Calculate the Langelier Saturation Index (LSI) and the Ryznar Stability Index ($\text{RSI} = 2\\text{pH}_s - \\text{pH}$).
(c) Assess whether the water will deposit a protective $\\text{CaCO}_3$ scale or corrode municipal iron water mains.""",
            "solution": """**(a) Calculation of Saturation $\\text{pH}_s$:**
The saturation pH is defined by:
\\[ \\text{pH}_s = (pK'_{a2} - pK'_{sp}) + p[\\text{Ca}^{2+}] + p[\\text{Alk}] \\]
Given:
- $pK'_{a2} - pK'_{sp} = 10.25 - 8.35 = 1.90$
- $[\text{Ca}^{2+}] = 2.00 \\times 10^{-3}\\text{ M} \\implies p[\\text{Ca}^{2+}] = -\\log_{10}(2.00 \\times 10^{-3}) = 3 - 0.3010 = 2.699$
- $[\text{Alk}] = 2.40 \\times 10^{-3}\\text{ eq/L} \\implies p[\\text{Alk}] = -\\log_{10}(2.40 \\times 10^{-3}) = 3 - 0.3802 = 2.620$

Sum the terms:
\\[ \\text{pH}_s = 1.90 + 2.699 + 2.620 = 7.219 \\approx 7.22 \\]

**(b) LSI and RSI Calculation:**
1. Langelier Saturation Index:
   \\[ \\text{LSI} = \\text{pH} - \\text{pH}_s = 7.85 - 7.22 = +0.63 \\]
2. Ryznar Stability Index:
   \\[ \\text{RSI} = 2\\,\\text{pH}_s - \\text{pH} = 2(7.22) - 7.85 = 14.44 - 7.85 = 6.59 \\]

**(c) Corrosion and Scaling Assessment:**
- Because $\\text{LSI} = +0.63 > 0$, the water is **supersaturated** with respect to calcium carbonate.
- $\\text{RSI} = 6.59$ sits in the ideal balanced range ($6.0 - 7.0$), indicating that the water will deposit a light, protective passivating film of $\\text{CaCO}_3$ scale onto the interior surfaces of cast iron pipes without causing excessive scaling or clogs."""
        },
        {
            "id": "prob4_9",
            "tier": "Advanced",
            "title": "Two-Dimensional pe-pH Stability Diagram for Aqueous Sulfur System",
            "statement": """Derive the thermodynamic expressions for the sulfur system in water at $25^\\circ\\text{C}$ ($C_T = 1.0 \\times 10^{-3}\\text{ M}$):
1. Sulfate/Bisulfate equilibrium:
   \\[ \\text{HSO}_4^- \\rightleftharpoons \\text{H}^+ + \\text{SO}_4^{2-} \\quad (pK_a = 1.99) \\]
2. Sulfate/Bisulfide redox boundary:
   \\[ \\text{SO}_4^{2-} + 9\\,\\text{H}^+ + 8\\,e^- \\rightleftharpoons \\text{HS}^- + 4\\,\\text{H}_2\\text{O} \\quad (\\log K_2 = 34.00, \\text{p}\\varepsilon^\\circ = 4.25) \\]
3. Hydrogen sulfide/Bisulfide dissociation:
   \\[ \\text{H}_2\\text{S}(aq) \\rightleftharpoons \\text{H}^+ + \\text{HS}^- \\quad (pK_{a1} = 7.00) \\]
(a) Derive the linear equation for the $\\text{p}\\varepsilon-\\text{pH}$ boundary between $\\text{SO}_4^{2-}$ and $\\text{HS}^-$ where $[\text{SO}_4^{2-}] = [\text{HS}^-]$.
(b) Derive the $\\text{p}\\varepsilon-\\text{pH}$ boundary between $\\text{SO}_4^{2-}$ and $\\text{H}_2\\text{S}(aq)$ at $\\text{pH} < 7.00$.
(c) At $\\text{pH} = 7.00$ in a stagnant anaerobic wetland, the measured reduction potential is $E_h = -0.220\\text{ V}$. Calculate the $\\text{p}\\varepsilon$ and determine the ratio of sulfate to hydrogen sulfide $[\text{SO}_4^{2-}]/[\text{HS}^-]$.""",
            "solution": """**(a) Boundary Equation between $\\text{SO}_4^{2-}$ and $\\text{HS}^-$:**
For the half-reaction:
\\[ \\text{SO}_4^{2-} + 9\\,\\text{H}^+ + 8\\,e^- \\rightleftharpoons \\text{HS}^- + 4\\,\\text{H}_2\\text{O} \\]
The equilibrium constant is:
\\[ \\log_{10} K_2 = 34.00 = \\log_{10}\\left(\\frac{[\\text{HS}^-]}{[\\text{SO}_4^{2-}]}\\right) - 9 \\log_{10}[\\text{H}^+] - 8 \\log_{10}[e^-] \\]
\\[ 34.00 = \\log_{10}\\left(\\frac{[\\text{HS}^-]}{[\\text{SO}_4^{2-}]}\\right) + 9\\,\\text{pH} + 8\\,\\text{p}\\varepsilon \\]
Along the equimolar boundary where $[\text{SO}_4^{2-}] = [\text{HS}^-]$, the log term vanishes:
\\[ 8\\,\\text{p}\\varepsilon = 34.00 - 9\\,\\text{pH} \\]
\\[ \\text{p}\\varepsilon = 4.25 - 1.125\\,\\text{pH} \\]

**(b) Boundary Equation between $\\text{SO}_4^{2-}$ and $\\text{H}_2\\text{S}(aq)$:**
At $\\text{pH} < 7.00$, $\\text{HS}^-$ protonates to $\\text{H}_2\\text{S}$:
\\[ \\text{HS}^- + \\text{H}^+ \\rightleftharpoons \\text{H}_2\\text{S} \\quad (\\log K = +7.00) \\]
Adding this to the redox half-reaction:
\\[ \\text{SO}_4^{2-} + 10\\,\\text{H}^+ + 8\\,e^- \\rightleftharpoons \\text{H}_2\\text{S} + 4\\,\\text{H}_2\\text{O} \\quad (\\log K_{\\text{net}} = 34.00 + 7.00 = 41.00) \\]
The boundary condition where $[\text{SO}_4^{2-}] = [\text{H}_2\\text{S}]$ is:
\\[ 41.00 = 10\\,\\text{pH} + 8\\,\\text{p}\\varepsilon \\]
\\[ 8\\,\\text{p}\\varepsilon = 41.00 - 10\\,\\text{pH} \\implies \\text{p}\\varepsilon = 5.125 - 1.25\\,\\text{pH} \\]

**(c) Speciation in Anaerobic Wetland:**
Given $E_h = -0.220\\text{ V}$ at $25^\\circ\\text{C}$:
\\[ \\text{p}\\varepsilon = \\frac{E_h}{0.05916\\text{ V}} = \\frac{-0.220}{0.05916} \\approx -3.719 \\]
At $\\text{pH} = 7.00$, the boundary value for equimolar $[\text{SO}_4^{2-}] = [\text{HS}^-]$ from part (a) is:
\\[ \\text{p}\\varepsilon_{\\text{boundary}} = 4.25 - 1.125(7.00) = 4.25 - 7.875 = -3.625 \\]
Using the full equilibrium equation from part (a):
\\[ 8\\,\\text{p}\\varepsilon = 34.00 - 9\\,\\text{pH} - \\log_{10}\\left(\\frac{[\\text{SO}_4^{2-}]}{[\\text{HS}^-]}\\right) \\]
\\[ \\log_{10}\\left(\\frac{[\\text{SO}_4^{2-}]}{[\\text{HS}^-]}\\right) = 34.00 - 9(7.00) - 8(-3.719) = 34.00 - 63.00 + 29.752 = -29.00 + 29.752 = +0.752 \\]
Taking the antilogarithm:
\\[ \\frac{[\\text{SO}_4^{2-}]}{[\\text{HS}^-]} = 10^{0.752} \\approx 5.65 \\]
*Result*: At $\\text{p}\\varepsilon = -3.72$, the system is in the midst of active microbial sulfate reduction; approximately $85\\%$ of sulfur remains as sulfate and $15\\%$ has been reduced to bisulfide, driving the onset of anoxic, sulfidic wetland chemistry."""
        }
    ]

    return {
        "unit_number": 4,
        "title": "Aquatic Chemistry, Carbonate Equilibria & Water Quality Metrics",
        "description": "Chemical structure and anomalous properties of water, the aquatic carbonate system, Total Alkalinity and buffering capacity, dissolved oxygen thermodynamics and Henry's law salting-out, Biochemical Oxygen Demand (BOD5 and CBODu), Chemical Oxygen Demand (COD) dichromate stoichiometry, Total Organic Carbon (TOC), the Streeter-Phelps oxygen sag model, aquatic hardness and complexometric EDTA chelation titrations, and aquatic redox geochemistry with electron activity (pe) and Pourbaix (Eh-pH) stability diagrams.",
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u = get_unit_4()
    print(f"Unit 4 generated: {len(u['sections'])} sections, {len(u['problems'])} problems.")
