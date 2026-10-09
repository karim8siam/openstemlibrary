# -*- coding: utf-8 -*-
"""
expand_industrial_problem9.py
Injects Problem 9 across all 10 units of Industrial Chemistry.
Brings total problems from 80 to 90.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def inject_problem_9(units):
    prob9_dict = {
        "unit-1-textiles-and-dyes": {
            "id": "prob-1-9",
            "problemNumber": "1.9",
            "title": "PET Melt Spinning Wind-up Velocity & Spinline Birefringence",
            "difficulty": "Hard",
            "statement": r"""A high-speed synthetic fiber spinning line melts poly(ethylene terephthalate) ($\text{PET}$, $\rho_{\text{solid}} = 1.38\text{ g/cm}^3$) through a multi-orifice spinneret die containing $N = 192\text{ holes}$ (each orifice diameter $D_0 = 0.35\text{ mm}$).
- Total polymer melt throughput through the pack is $\dot{m} = 45.0\text{ kg/h}$ ($12.5\text{ g/s}$).
- The solidified yarn is pulled by godet rolls at a take-up speed of $v_L = 4,500\text{ m/min}$ ($75.0\text{ m/s}$).
- At this take-up velocity, stress-induced crystallization occurs on the spinline, developing an optical birefringence of $\Delta n = 0.042$.
- The maximum theoretical intrinsic birefringence of perfectly oriented crystalline PET is $\Delta n^\circ = 0.220$.

1. Calculate the linear mass density of the single filament and the entire multi-filament yarn in dtex ($\text{g / 10,000 m}$).
2. Determine the spinline draw ratio ($\text{DR} = v_L / v_0$, where $v_0$ is the initial extrusion velocity from the spinneret orifices).
3. Calculate the Hermans crystalline orientation factor ($f_c$) of the spun yarn:
   $$f_c = \frac{\Delta n}{\Delta n^\circ}$$""",
            "solution": r"""### Step 1: Linear Density in dtex
Total mass throughput:
$$\dot{m} = 45.0\text{ kg/h} = 45,000\text{ g/h}$$
In one hour ($60\text{ minutes}$), the wind-up roll collects yarn length:
$$L_{\text{hour}} = 4,500\text{ m/min} \times 60\text{ min} = 270,000\text{ meters}$$
Linear density of total yarn in dtex ($\text{g / 10,000 m}$):
$$\text{Yarn dtex} = \frac{45,000\text{ g}}{270,000\text{ m}} \times 10,000\text{ m} = \frac{45,000}{27} = 1.6667 \times 100 = 166.67\text{ dtex}$$
Linear density of individual single filament (with $N = 192\text{ filaments}$):
$$\text{dpf (dtex per filament)} = \frac{166.67\text{ dtex}}{192} = 0.868\text{ dtex}$$
The yarn is a fine micro-denier filament yarn (**$166.7\text{ dtex / } 192\text{ filaments}$**, $0.87\text{ dpf}$).

### Step 2: Spinline Draw Ratio ($\text{DR}$)
Total cross-sectional area of $N = 192$ spinneret orifices ($D_0 = 0.35\text{ mm} = 0.035\text{ cm}$):
$$A_0 = 192 \times \frac{\pi}{4} D_0^2 = 192 \times \frac{\pi}{4} (0.035\text{ cm})^2 = 192 \times 9.621 \times 10^{-4}\text{ cm}^2 = 0.1847\text{ cm}^2 = 1.847 \times 10^{-5}\text{ m}^2$$
Volumetric melt flow rate ($\rho_{\text{melt}} \approx 1.20\text{ g/cm}^3$ at $285^\circ\text{C}$):
$$\dot{V}_{\text{melt}} = \frac{12.5\text{ g/s}}{1.20\text{ g/cm}^3} = 10.417\text{ cm}^3\text{/s} = 1.0417 \times 10^{-5}\text{ m}^3\text{/s}$$
Extrusion velocity at orifice exit ($v_0$):
$$v_0 = \frac{\dot{V}_{\text{melt}}}{A_0} = \frac{1.0417 \times 10^{-5}\text{ m}^3\text{/s}}{1.847 \times 10^{-5}\text{ m}^2} = 0.564\text{ m/s}$$
Spinline Draw Ratio:
$$\text{DR} = \frac{v_L}{v_0} = \frac{75.0\text{ m/s}}{0.564\text{ m/s}} \approx 133.0$$

### Step 3: Hermans Orientation Factor ($f_c$)
$$f_c = \frac{\Delta n}{\Delta n^\circ} = \frac{0.042}{0.220} = 0.1909 \approx 0.191$$

The yarn achieves an orientation factor of **$f_c = 0.191$**, representative of partially oriented yarn (POY) produced by high-speed spinning.""",
            "hints": ["dtex is grams per 10,000 meters.", "Draw ratio is take-up speed divided by initial extrusion speed."]
        },

        "unit-2-fertilizer-industries": {
            "id": "prob-2-9",
            "problemNumber": "2.9",
            "title": "Controlled-Release Polymer-Coated Urea (PCU) Fickian Diffusion",
            "difficulty": "Medium",
            "statement": r"""A polymer-coated controlled-release urea granule is engineered with a spherical geometry:
- Core radius: $r_0 = 1.50\text{ mm} = 0.150\text{ cm}$ ($\rho_{\text{urea}} = 1.32\text{ g/cm}^3$)
- Biodegradable polyurethane coating thickness: $\delta = 40.0\,\mu\text{m} = 4.00 \times 10^{-3}\text{ cm}$
- The concentration of saturated dissolved urea inside the wet core is $C_{\text{sat}} = 1.08\text{ g/cm}^3$ ($1,080\text{ g/L}$ at $25^\circ\text{C}$).
- In moist soil, exterior concentration is maintained near zero ($C_{\text{ext}} \approx 0$).
- Diffusion coefficient of urea through the polymer coating membrane is $D = 2.50 \times 10^{-8}\text{ cm}^2/\text{s}$.

1. Calculate the initial mass of solid urea contained in a single spherical granule.
2. Formulate steady-state spherical diffusion to calculate the mass release rate of urea ($\dot{m}_{\text{release}}$ in $\text{g/day}$) during the constant-core dissolution regime:
   $$\dot{m}_{\text{release}} = \frac{4 \pi D C_{\text{sat}} r_0^2}{\delta}$$
3. Calculate the release longevity (number of days required to release $80.0\%$ of the initial urea core).""",
            "solution": r"""### Step 1: Initial Urea Core Mass
Core volume:
$$V_{\text{core}} = \frac{4}{3} \pi r_0^3 = \frac{4}{3} \pi (0.150\text{ cm})^3 = 0.014137\text{ cm}^3$$
Initial urea mass:
$$m_0 = V_{\text{core}} \times \rho_{\text{urea}} = 0.014137\text{ cm}^3 \times 1.32\text{ g/cm}^3 = 0.01866\text{ g} = 18.66\text{ mg}$$

### Step 2: Steady-State Mass Release Rate
Surface area of core:
$$A = 4 \pi r_0^2 = 4 \pi (0.150\text{ cm})^2 = 0.28274\text{ cm}^2$$
Diffusion mass flux ($J$):
$$J = \frac{D \cdot C_{\text{sat}}}{\delta} = \frac{(2.50 \times 10^{-8}\text{ cm}^2/\text{s}) \times 1.08\text{ g/cm}^3}{4.00 \times 10^{-3}\text{ cm}} = 6.750 \times 10^{-6}\text{ g/(cm}^2\cdot\text{s)}$$
Total mass release rate:
$$\dot{m}_{\text{release}} = J \times A = (6.750 \times 10^{-6}\text{ g/(cm}^2\cdot\text{s)}) \times 0.28274\text{ cm}^2 = 1.9085 \times 10^{-6}\text{ g/s}$$
In grams per day ($86,400\text{ s/day}$):
$$\dot{m}_{\text{release, day}} = 1.9085 \times 10^{-6}\text{ g/s} \times 86,400\text{ s/day} = 0.1649\text{ mg/day} = 1.649 \times 10^{-4}\text{ g/day}$$

### Step 3: Longevity for $80.0\%$ Release
Mass of urea to be released:
$$\Delta m = 0.800 \times 18.66\text{ mg} = 14.928\text{ mg}$$
Days required:
$$t = \frac{\Delta m}{\dot{m}_{\text{release, day}}} = \frac{14.928\text{ mg}}{0.1649\text{ mg/day}} \approx 90.53\text{ days}$$

The controlled-release coating provides a steady release longevity of **$90.5\text{ days}$** ($3\text{ months}$), perfectly matching the seasonal growth cycle of corn/wheat.""",
            "hints": ["Mass flux J = D * C_sat / delta.", "Multiply flux by surface area to get mass flow per second."]
        },

        "unit-3-sugar-and-starch": {
            "id": "prob-3-9",
            "problemNumber": "3.9",
            "title": "Polylactic Acid (PLA) Ring-Opening Polymerization Molar Mass",
            "difficulty": "Easy",
            "statement": r"""A polymer reactor synthesizes bio-based polylactic acid (PLA) via ring-opening polymerization of L,L-lactide ($M_{\text{monomer}} = 144.13\text{ g/mol}$) initiated by 1-dodecanol ($\text{C}_{12}\text{H}_{25}\text{OH}$, $M_{\text{init}} = 186.34\text{ g/mol}$) with tin(II) 2-ethylhexanoate catalyst.
- Monomer feed: $m_{\text{lactide}} = 500.0\text{ kg}$ ($3,469.1\text{ mol}$).
- Initiator added: $m_{\text{init}} = 1.295\text{ kg}$ ($6.950\text{ mol}$).
- The reaction runs at $180^\circ\text{C}$ to a monomer conversion of $p = 96.0\%$.
Each initiator molecule grows exactly one linear polymer chain.

1. Calculate the initial monomer-to-initiator molar ratio ($[M]_0 / [I]_0$).
2. Determine the theoretical number-average degree of polymerization ($\overline{DP}_n$) of the resulting PLA polymer.
3. Calculate the number-average molecular weight ($\bar{M}_n$) of the finished PLA resin in $\text{g/mol}$.""",
            "solution": r"""### Step 1: Monomer-to-Initiator Ratio
$$[M]_0 / [I]_0 = \frac{3,469.1\text{ mol}}{6.950\text{ mol}} \approx 499.15 \approx 500$$

### Step 2: Number-Average Degree of Polymerization ($\overline{DP}_n$)
Each lactide dimer molecule contains two lactic acid repeat units. In ring-opening polymerization:
$$\overline{DP}_n = \left(\frac{[M]_0}{[I]_0}\right) \times p = 499.15 \times 0.960 = 479.18\text{ lactide units} \ (958.4\text{ lactic acid units})$$

### Step 3: Number-Average Molecular Weight ($\bar{M}_n$)
$$\bar{M}_n = M_{\text{init}} + (\overline{DP}_n \times M_{\text{monomer}})$$
$$\bar{M}_n = 186.34 + (479.18 \times 144.13) = 186.34 + 69,064.2 = 69,250.5\text{ g/mol}$$

The resulting PLA bioplastic has a number-average molar mass of **$\bar{M}_n = 69,250\text{ g/mol}$**, suitable for extrusion of compostable packaging films.""",
            "hints": ["DP_n = ([M]_0 / [I]_0) * p.", "M_n = Initiator mass + (DP_n * monomer mass)."]
        },

        "unit-4-cement-and-lime": {
            "id": "prob-4-9",
            "problemNumber": "4.9",
            "title": "Oxy-Fuel Cement Clinker Kiln CO2 Flue Gas Balance",
            "difficulty": "Medium",
            "statement": r"""An oxy-fuel retrofit cement plant produces $3,000\text{ metric tons/day}$ ($125.0\text{ t/h}$) of clinker.
- Limestone decarbonation releases $520.0\text{ kg CO}_2\text{ / metric ton clinker}$.
- Pulverized coal combustion requires $2,950\text{ kJ/kg clinker}$.
- Coal composition: $75.0\text{ wt}\%\text{ C}$, $4.5\text{ wt}\%\text{ H}$, $8.0\text{ wt}\%\text{ O}$, $1.5\text{ wt}\%\text{ S}$, $1.0\text{ wt}\%\text{ N}$, $10.0\text{ wt}\%\text{ ash}$; lower heating value $\text{LHV} = 28,000\text{ kJ/kg}$.
- Combustion is supplied with pure oxygen ($95.0\text{ vol}\%\text{ O}_2$, $5.0\text{ vol}\%\text{ N}_2$) at $5.0\%$ stoichiometric excess. Recycled flue gas moderates flame temperature.

1. Calculate the coal consumption rate in metric tons per hour.
2. Determine the total hourly generation rate of $\text{CO}_2$ from calcination and coal combustion in metric tons per hour.
3. Calculate the volume percentage ($\text{vol}\%$) of $\text{CO}_2$ in the dry flue gas, verifying if it exceeds the $80\%$ threshold for direct cryogenic condensation.""",
            "solution": r"""### Step 1: Coal Consumption Rate
Hourly clinker production: $\dot{m}_{\text{clinker}} = 125,000\text{ kg/h}$.
Total heat required:
$$\dot{Q} = 125,000\text{ kg/h} \times 2,950\text{ kJ/kg} = 3.6875 \times 10^8\text{ kJ/h}$$
Coal feed rate:
$$\dot{m}_{\text{coal}} = \frac{3.6875 \times 10^8\text{ kJ/h}}{28,000\text{ kJ/kg}} = 13,169.6\text{ kg/h} \approx 13.17\text{ metric tons/h}$$

### Step 2: Total $\text{CO}_2$ Generation Rate
1. **Calcination $\text{CO}_2$**:
   $$\dot{m}_{\text{CO}_2, \text{calc}} = 125.0\text{ t clinker/h} \times 0.5200\text{ t CO}_2\text{/t} = 65.00\text{ metric tons/h}$$
   $$\dot{n}_{\text{CO}_2, \text{calc}} = \frac{65,000\text{ kg/h}}{44.01\text{ kg/kmol}} = 1,476.94\text{ kmol/h}$$
2. **Coal Combustion $\text{CO}_2$**:
   Carbon in coal ($75.0\%$):
   $$\dot{m}_{\text{C}} = 0.750 \times 13,169.6 = 9,877.2\text{ kg/h} \implies \dot{n}_{\text{C}} = \frac{9,877.2}{12.01} = 822.41\text{ kmol/h}$$
   $$\dot{n}_{\text{CO}_2, \text{coal}} = 822.41\text{ kmol/h}$$
   $$\dot{m}_{\text{CO}_2, \text{coal}} = 822.41 \times 44.01 = 36,194.3\text{ kg/h} \approx 36.19\text{ metric tons/h}$$
Total $\text{CO}_2$ generated:
$$\dot{m}_{\text{CO}_2, \text{total}} = 65.00 + 36.19 = 101.19\text{ metric tons/h}$$
$$\dot{n}_{\text{CO}_2, \text{total}} = 1,476.94 + 822.41 = 2,299.35\text{ kmol/h}$$

### Step 3: Dry Flue Gas Composition
Non-condensable inerts in dry flue gas come from:
- $\text{N}_2$ in coal ($1.0\%$): $\frac{131.7\text{ kg}}{28.01} = 4.70\text{ kmol/h}$
- $\text{N}_2$ introduced with $95\%$ oxygen feed:
  Theoretical $\text{O}_2$ for coal: $\text{C} + \text{O}_2 \to 822.41$; $\text{H} \to \frac{592.6}{4} = 148.15$; minus fuel O ($65.85$) $= 904.7\text{ kmol O}_2$.
  With $5\%$ excess, $\text{O}_2\text{ fed} = 1.05 \times 904.7 = 950.0\text{ kmol/h}$.
  $\text{N}_2$ in oxygen supply ($5/95$ ratio): $950.0 \times \frac{0.05}{0.95} = 50.00\text{ kmol/h}$.
- Excess unreacted $\text{O}_2$: $0.05 \times 904.7 = 45.24\text{ kmol/h}$.
- Minor $\text{SO}_2$: $\sim 6.17\text{ kmol/h}$.
Total dry flue gas moles:
$$\dot{n}_{\text{dry flue}} = 2,299.35 (\text{CO}_2) + 4.70 + 50.00 + 45.24 + 6.17 = 2,405.46\text{ kmol/h}$$
$\text{CO}_2$ concentration:
$$\% \text{CO}_2 = \frac{2,299.35}{2,405.46} \times 100\% = 95.59\%$$

The dry flue gas contains **$95.6\text{ vol}\%\text{ CO}_2$**, far exceeding the $80\%$ threshold and enabling direct low-cost compression and liquefaction.""",
                    "hints": ["Sum calcination CO2 and coal combustion CO2.", "Dry flue gas includes CO2, excess O2, and N2 from oxygen/coal."]
                },

        "unit-5-soaps-and-detergents": {
            "id": "prob-5-9",
            "problemNumber": "5.9",
            "title": "Alkyl Polyglycoside (APG) Direct Glucosidation Stoichiometry",
            "difficulty": "Easy",
            "statement": r"""An oleochemical manufacturing plant produces green non-ionic Alkyl Polyglycoside ($\text{APG}$) surfactant via the direct acid-catalyzed glucosidation of fatty alcohol with anhydrous D-glucose:
$$\text{C}_{12}\text{H}_{25}\text{OH} + \overline{DP} \cdot \text{C}_6\text{H}_{12}\text{O}_6 \longrightarrow \text{C}_{12}\text{H}_{25}\text{O-(C}_6\text{H}_{10}\text{O}_5)_{\overline{DP}}\text{-H} + \overline{DP} \cdot \text{H}_2\text{O}$$
- Fatty alcohol: 1-dodecanol ($\text{C}_{12}\text{H}_{25}\text{OH}$, $186.34\text{ g/mol}$).
- Anhydrous D-glucose ($180.16\text{ g/mol}$).
- Target average degree of polymerization is $\overline{DP} = 1.40$ (average glucose unit $162.14\text{ g/mol}$).
- Average molar mass of product surfactant:
  $$\bar{M}_{\text{APG}} = 186.34 + 1.40(162.14) = 413.34\text{ g/mol}$$
- To drive the equilibrium forward and prevent caramelization, fatty alcohol is fed at a molar ratio of $4.0\text{ moles alcohol per mole of glucose}$.
The plant processes $10.0\text{ metric tons}$ ($10,000\text{ kg}$) of D-glucose per batch with $100\%$ glucose conversion.

1. Calculate the required mass of 1-dodecanol charged in the reactor in metric tons.
2. Determine the mass of pure active $\text{APG}$ produced.
3. Calculate the mass of unreacted fatty alcohol that must be recovered by thin-film vacuum distillation for recycling.""",
            "solution": r"""### Step 1: Fatty Alcohol Charged
Moles of D-glucose fed:
$$n_{\text{glucose}} = \frac{10,000 \times 10^3\text{ g}}{180.16\text{ g/mol}} = 55,506.2\text{ mol} = 55.506\text{ kmol}$$
At $4.0 : 1.0$ molar ratio, alcohol charged:
$$n_{\text{alcohol, charged}} = 4.0 \times 55.506\text{ kmol} = 222.025\text{ kmol}$$
Mass of 1-dodecanol:
$$m_{\text{alcohol, charged}} = 222.025\text{ kmol} \times 186.34\text{ kg/kmol} = 41,372.1\text{ kg} \approx 41.37\text{ metric tons}$$

### Step 2: Mass of Active APG Produced
Since $\overline{DP} = 1.40$, each mole of APG molecule incorporates $1.40\text{ moles of glucose}$ and $1.0\text{ mole of alcohol}$:
$$n_{\text{APG}} = \frac{n_{\text{glucose}}}{1.40} = \frac{55,506.2\text{ mol}}{1.40} = 39,647.3\text{ mol} = 39.647\text{ kmol}$$
Mass of active APG produced ($\bar{M}_{\text{APG}} = 413.34\text{ g/mol}$):
$$m_{\text{APG}} = 39.647\text{ kmol} \times 413.34\text{ kg/kmol} = 16,387.7\text{ kg} \approx 16.39\text{ metric tons}$$

### Step 3: Unreacted Fatty Alcohol to Recycle
Moles of alcohol consumed chemically:
$$n_{\text{alcohol, consumed}} = n_{\text{APG}} = 39.647\text{ kmol}$$
Unreacted alcohol remaining:
$$n_{\text{alcohol, unreacted}} = 222.025 - 39.647 = 182.378\text{ kmol}$$
Mass of alcohol recovered by vacuum distillation:
$$m_{\text{alcohol, recycle}} = 182.378\text{ kmol} \times 186.34\text{ kg/kmol} = 33,984.3\text{ kg} \approx 33.98\text{ metric tons}$$

The plant charges **$41.37\text{ t}$ fatty alcohol**, yields **$16.39\text{ t}$ active APG**, and recycles **$33.98\text{ t}$ unreacted alcohol**.""",
            "hints": ["Moles of APG equals glucose moles divided by DP.", "Unreacted alcohol is charged alcohol minus consumed alcohol."]
        },

        "unit-6-pulp-and-paper": {
            "id": "prob-6-9",
            "problemNumber": "6.9",
            "title": "Kraft Lignin Precipitation (LignoBoost) CO2 Acidification Balance",
            "difficulty": "Medium",
            "statement": r"""A Kraft pulp mill extracts pure technical lignin from evaporated black liquor ($35.0\text{ wt}\%$ dry solids, $\text{pH } 13.0$) via the LignoBoost process at a throughput of $\dot{m}_{\text{liquor}} = 50.0\text{ metric tons/h}$.
- The dry black liquor solids contain $38.0\text{ wt}\%\text{ dissolved lignin}$.
- Acidification with pure gaseous $\text{CO}_2$ ($44.01\text{ g/mol}$) drops the $\text{pH}$ to $9.5$, precipitating $70.0\%$ of the dissolved lignin as insoluble colloidal particles.
- The acidification consumes $180.0\text{ kg of gaseous CO}_2$ per metric ton of precipitated dry lignin.
- The filtered wet lignin cake is washed with dilute sulfuric acid to remove entrained sodium ions.

1. Calculate the mass of dissolved lignin entering with the black liquor per hour in metric tons.
2. Determine the hourly production rate of precipitated dry Kraft lignin in metric tons per hour.
3. Calculate the required mass and volumetric flow rate of $\text{CO}_2$ gas at STP in $\text{kg/h}$ and $\text{Nm}^3\text{/h}$ ($22.414\text{ Nm}^3\text{/kmol}$).""",
            "solution": r"""### Step 1: Dissolved Lignin Feed Rate
Black liquor dry solids rate:
$$\dot{m}_{\text{solids}} = 0.350 \times 50.0\text{ metric tons/h} = 17.50\text{ metric tons/h}$$
Dissolved lignin entering:
$$\dot{m}_{\text{lignin, in}} = 0.380 \times 17.50 = 6.650\text{ metric tons/h} = 6,650\text{ kg/h}$$

### Step 2: Precipitated Dry Lignin Production Rate
Precipitation yield is $70.0\%$:
$$\dot{m}_{\text{lignin, ppt}} = 0.700 \times 6.650\text{ metric tons/h} = 4.655\text{ metric tons/h} = 4,655\text{ kg/h}$$
The mill harvests **$4.655\text{ metric tons/h}$** of pure dry Kraft lignin.

### Step 3: Carbon Dioxide Consumption
Specific $\text{CO}_2$ consumption is $180.0\text{ kg CO}_2\text{ / ton dry lignin}$:
$$\dot{m}_{\text{CO}_2} = 4.655\text{ tons lignin/h} \times 180.0\text{ kg CO}_2\text{/ton} = 837.9\text{ kg/h}$$
Moles of $\text{CO}_2$:
$$\dot{n}_{\text{CO}_2} = \frac{837.9\text{ kg/h}}{44.01\text{ kg/kmol}} = 19.039\text{ kmol/h}$$
Volumetric flow rate at STP:
$$\dot{V}_{\text{CO}_2, \text{STP}} = 19.039\text{ kmol/h} \times 22.414\text{ Nm}^3\text{/kmol} = 426.74\text{ Nm}^3\text{/h}$$

The LignoBoost plant harvests **$4.66\text{ t/h}$ lignin**, consuming **$837.9\text{ kg/h}$ ($426.7\text{ Nm}^3\text{/h}$) of $\text{CO}_2$**.""",
            "hints": ["Compute total dry solids, multiply by lignin fraction and 70% recovery.", "CO2 mass equals dry lignin tons times 180 kg/ton."]
        },

        "unit-7-glass-and-ceramics": {
            "id": "prob-7-9",
            "problemNumber": "7.9",
            "title": "Zero-Expansion Glass-Ceramic Critical Thermal Shock Quenching",
            "difficulty": "Easy",
            "statement": r"""A comparative thermal shock test evaluates two cooktop materials plunged from an oven into ice water ($0^\circ\text{C}$):
1. **Commercial Soda-Lime Glass Sheet**:
   - Tensile fracture strength: $\sigma_f = 50.0\text{ MPa}$
   - Young's modulus: $E = 70.0\text{ GPa}$
   - Poisson's ratio: $\nu = 0.22$
   - Thermal expansion coefficient: $\alpha = 9.00 \times 10^{-6}\text{ K}^{-1}$
2. **Lithium Aluminosilicate (LAS) Glass-Ceramic Cooktop**:
   - Tensile fracture strength: $\sigma_f = 140.0\text{ MPa}$
   - Young's modulus: $E = 90.0\text{ GPa}$
   - Poisson's ratio: $\nu = 0.24$
   - Thermal expansion coefficient: $\alpha = 0.15 \times 10^{-6}\text{ K}^{-1}$

Calculate Kingery's critical thermal shock temperature drop ($R$) for each material:
$$R = \frac{\sigma_f (1 - \nu)}{E \alpha}$$
Evaluate whether each material survives being heated to $500^\circ\text{C}$ and plunged into $0^\circ\text{C}$ ice water ($\Delta T = 500\text{ K}$).""",
            "solution": r"""### Step 1: Soda-Lime Glass Critical Quench ($R_1$)
$$\sigma_f (1 - \nu) = 50.0 \times 10^6\text{ Pa} \times (1 - 0.22) = 39.0 \times 10^6\text{ Pa}$$
$$E \alpha = (70.0 \times 10^9\text{ Pa}) \times (9.00 \times 10^{-6}\text{ K}^{-1}) = 630,000\text{ Pa/K}$$
$$R_1 = \frac{39.0 \times 10^6}{630,000} \approx 61.90\text{ K}$$
The maximum safe quench for soda-lime glass is **$61.9\text{ K}$**.
At $\Delta T = 500\text{ K}$, thermal stresses are $\sim 8\times$ its fracture strength; it will shatter violently.

### Step 2: LAS Glass-Ceramic Critical Quench ($R_2$)
$$\sigma_f (1 - \nu) = 140.0 \times 10^6\text{ Pa} \times (1 - 0.24) = 106.4 \times 10^6\text{ Pa}$$
$$E \alpha = (90.0 \times 10^9\text{ Pa}) \times (0.15 \times 10^{-6}\text{ K}^{-1}) = 13,500\text{ Pa/K}$$
$$R_2 = \frac{106.4 \times 10^6}{13,500} \approx 7,881.5\text{ K}$$
The theoretical critical quench for LAS glass-ceramic is **$7,882\text{ K}$**.

### Step 3: Survival Evaluation
Since $R_2 = 7,882\text{ K} \gg 500\text{ K}$, thermal stress induced in the LAS glass-ceramic is negligible ($\sigma_{\text{thermal}} \approx 8.9\text{ MPa} \ll 140\text{ MPa}$), allowing it to survive a $500^\circ\text{C}$ ice water plunge with a massive safety margin.""",
            "hints": ["Substitute directly into Kingery's equation.", "Notice the dramatic difference caused by the tiny thermal expansion coefficient."]
        },

        "unit-8-caustic-chlorine": {
            "id": "prob-8-8-alt",
            "problemNumber": "8.9",
            "title": "Bipolar Membrane Electrodialysis (BMED) Water Splitting",
            "difficulty": "Hard",
            "statement": r"""A chemical zero-liquid-discharge facility treats industrial waste sodium sulfate ($\text{Na}_2\text{SO}_4$, $142.04\text{ g/mol}$) using Bipolar Membrane Electrodialysis (BMED) to regenerate sodium hydroxide ($\text{NaOH}$, $40.00\text{ g/mol}$) and sulfuric acid ($\text{H}_2\text{SO}_4$, $98.08\text{ g/mol}$).
- The BMED stack comprises $N = 200\text{ repeating cell triplets}$ (Bipolar Membrane - Anion Exchange Membrane - Cation Exchange Membrane) operating in electrical series at $I = 500\text{ A}$.
- At the bipolar membrane junction, water dissociates into $\text{H}^+$ and $\text{OH}^-$ ions:
  $$\text{H}_2\text{O} \overset{\text{Electrical Field}}{\longrightarrow} \text{H}^+ + \text{OH}^-$$
- The current efficiency for $\text{NaOH}$ is $\eta = 88.0\%$ ($F = 96,485\text{ C/mol}$).
- The overall cell triplet operating voltage is $U = 1.80\text{ V}$.

1. Calculate the daily production rate of pure $100\%\text{ NaOH}$ in metric tons per day.
2. Determine the daily production rate of pure $\text{H}_2\text{SO}_4$ generated in metric tons per day.
3. Calculate the specific direct-current electrical energy consumption per metric ton of $\text{NaOH}$ produced ($\text{kWh/t NaOH}$).""",
            "solution": r"""### Step 1: Daily $\text{NaOH}$ Production
Total charge passed across $N = 200$ cells in series per day ($t = 86,400\text{ s}$):
$$Q_{\text{day}} = 200 \times 500\text{ A} \times 86,400\text{ s} = 8.64 \times 10^9\text{ C}$$
Moles of electrons passed:
$$n_e = \frac{8.64 \times 10^9\text{ C}}{96,485\text{ C/mol}} = 89,547.6\text{ mol } e^- = 89.548\text{ kmol } e^-$$
At $\eta = 88.0\%$ current efficiency, moles of $\text{NaOH}$ generated:
$$n_{\text{NaOH}} = 0.880 \times 89.548\text{ kmol} = 78.802\text{ kmol/day}$$
Mass of pure $\text{NaOH}$:
$$m_{\text{NaOH}} = 78.802\text{ kmol} \times 40.00\text{ kg/kmol} = 3,152.1\text{ kg/day} \approx 3.152\text{ metric tons/day}$$

### Step 2: Daily $\text{H}_2\text{SO}_4$ Production
Each mole of $\text{H}_2\text{SO}_4$ requires $2\text{ moles of H}^+$:
$$n_{\text{H}_2\text{SO}_4} = \frac{n_{\text{NaOH}}}{2} = \frac{78.802}{2} = 39.401\text{ kmol/day}$$
Mass of pure $\text{H}_2\text{SO}_4$:
$$m_{\text{H}_2\text{SO}_4} = 39.401\text{ kmol} \times 98.08\text{ kg/kmol} = 3,864.5\text{ kg/day} \approx 3.865\text{ metric tons/day}$$

### Step 3: Specific Electrical Energy Consumption
Total direct-current electrical power of the stack ($200\text{ triplets}$ at $1.80\text{ V}$, total voltage $= 360\text{ V}$):
$$P = 200 \times 1.80\text{ V} \times 500\text{ A} = 180,000\text{ W} = 180.0\text{ kW}$$
Daily energy consumed:
$$E_{\text{day}} = 180.0\text{ kW} \times 24\text{ h} = 4,320\text{ kWh/day}$$
Specific energy consumption per ton of $\text{NaOH}$:
$$w_{\text{spec}} = \frac{4,320\text{ kWh/day}}{3.1521\text{ t NaOH/day}} = 1,370.5\text{ kWh/metric ton NaOH}$$

BMED produces **$3.15\text{ t/day}$ NaOH** and **$3.86\text{ t/day}$ H2SO4**, consuming **$1,371\text{ kWh/t NaOH}$**.""",
            "hints": ["Each electron generates 1 mole of OH- and 1 mole of H+ at 100% efficiency.", "H2SO4 requires two H+ ions."]
        },

        "unit-9-petroleum-and-fuels": {
            "id": "prob-9-9",
            "problemNumber": "9.9",
            "title": "Waste Polyolefin Plastic Pyrolysis Mass & Energy Yield",
            "difficulty": "Medium",
            "statement": r"""A circular plastics chemical recycling plant pyrolyzes $\dot{m}_{\text{plastic}} = 10.0\text{ metric tons/h}$ ($10,000\text{ kg/h}$) of sorted post-consumer polyolefins ($60\text{ wt}\%\text{ polyethylene}$, $40\text{ wt}\%\text{ polypropylene}$) in a fluidized bed reactor at $500^\circ\text{C}$.
- Endothermic heat of depolymerization/cracking is $\Delta h_{\text{pyro}} = 1,850\text{ kJ/kg plastic}$.
- Continuous product mass yields:
  - Synthetic Pyrolysis Oil ($\text{C}_5-\text{C}_{22}$ liquid): $78.0\text{ wt}\%$
  - Pyrolysis Non-Condensable Fuel Gas ($\text{C}_1-\text{C}_4$): $16.0\text{ wt}\%$ ($\text{LHV} = 44,000\text{ kJ/kg}$)
  - Carbonaceous Char/Coke: $6.0\text{ wt}\%$

1. Calculate the hourly production rate of liquid synthetic crude oil in metric tons per hour.
2. Determine the total thermal power required by the pyrolysis reactor in thermal megawatts ($\text{MW}$).
3. Calculate the thermal energy content of the byproduct fuel gas per hour and verify whether burning the fuel gas makes the plant completely thermally self-sustaining.""",
            "solution": r"""### Step 1: Synthetic Pyrolysis Oil Production
$$\dot{m}_{\text{oil}} = 0.780 \times 10.0\text{ metric tons/h} = 7.80\text{ metric tons/h} = 7,800\text{ kg/h}$$
The plant yields **$7.80\text{ metric tons/h}$** of circular liquid naphtha/wax feed.

### Step 2: Pyrolysis Thermal Power Requirement
Hourly heat duty:
$$\dot{Q}_{\text{pyro}} = 10,000\text{ kg/h} \times 1,850\text{ kJ/kg} = 1.850 \times 10^7\text{ kJ/h}$$
In thermal megawatts ($\text{MW}$):
$$\dot{Q}_{\text{thermal}} = \frac{1.850 \times 10^7\text{ kJ/h}}{3,600\text{ s/h}} = 5,138.9\text{ kW} \approx 5.14\text{ MW}$$

### Step 3: Energy Self-Sufficiency Verification
Byproduct fuel gas produced:
$$\dot{m}_{\text{gas}} = 0.160 \times 10,000\text{ kg/h} = 1,600\text{ kg/h}$$
Thermal energy released by gas combustion:
$$\dot{Q}_{\text{gas}} = 1,600\text{ kg/h} \times 44,000\text{ kJ/kg} = 7.040 \times 10^7\text{ kJ/h} \approx 19.56\text{ MW}$$
Comparison:
$$\frac{\dot{Q}_{\text{gas}}}{\dot{Q}_{\text{pyro}}} = \frac{7.040 \times 10^7\text{ kJ/h}}{1.850 \times 10^7\text{ kJ/h}} = 3.805$$
The combustion of byproduct fuel gas generates **$3.8\times$** the total heat required for pyrolysis, rendering the recycling process completely thermally self-sustaining with a huge exportable energy surplus.""",
            "hints": ["Multiply plastic feed by oil yield fraction.", "Compare fuel gas heating value to required depolymerization enthalpy."]
        },

        "unit-10-metallurgy-and-steel": {
            "id": "prob-10-9",
            "problemNumber": "10.9",
            "title": "Electric Arc Furnace (EAF) Dynamic Slag Foaming Kinetics",
            "difficulty": "Medium",
            "statement": r"""In an Electric Arc Furnace melting DRI and scrap, biochar fines ($90.0\text{ wt}\%\text{ fixed carbon}$, $12.01\text{ g/mol}$) and gaseous oxygen are co-injected into the liquid slag at $1600^\circ\text{C}$ to generate a thick foaming slag that shields the water-cooled furnace walls.
The foaming reaction with dissolved wüstite in the slag is:
$$\text{C}(s) + (\text{FeO})_{(\text{slag})} \longrightarrow \text{Fe}(l) + \text{CO}(g)$$
- Biochar is injected at a rate of $\dot{m}_{\text{char}} = 18.0\text{ kg/min}$ ($16.2\text{ kg carbon/min}$).
- Carbon gasification efficiency is $85.0\%$.
- Ideal gas law applies to $\text{CO}$ at $T = 1600^\circ\text{C}$ ($1873.15\text{ K}$) and $P = 1.0\text{ bar}$.
- The slag has a mean gas bubble residence time (foaming retention time) of $\tau = 45.0\text{ seconds}$ ($0.75\text{ min}$).
- The cross-sectional bath area of the furnace shell is $A = 28.0\text{ m}^2$.

1. Calculate the generation rate of carbon monoxide gas in $\text{kmol/min}$ and actual cubic meters per minute ($\text{m}^3\text{/min}$).
2. Determine the steady-state volumetric holdup of gas trapped inside the foamy slag ($V_{\text{gas}}$ in $\text{m}^3$).
3. Calculate the average height expansion of the foaming slag ($\Delta h_{\text{slag}}$) in meters.""",
            "solution": r"""### Step 1: Carbon Monoxide Generation Rate
Moles of carbon reacted per minute:
$$\dot{n}_{\text{C}} = \frac{0.850 \times 16.2\text{ kg/min}}{12.01\text{ kg/kmol}} = 1.1465\text{ kmol/min}$$
Stoichiometric $\text{CO}$ generated:
$$\dot{n}_{\text{CO}} = 1.1465\text{ kmol/min}$$

Actual volumetric gas generation rate at $T = 1873.15\text{ K}$, $P = 1.0\text{ bar} = 100\text{ kPa}$ ($R = 8.314\text{ kPa}\cdot\text{m}^3\text{/(kmol}\cdot\text{K)}$):
$$\dot{V}_{\text{CO}} = \frac{\dot{n}_{\text{CO}} \cdot R \cdot T}{P} = \frac{1.1465 \times 8.314 \times 1873.15}{100} = 178.55\text{ m}^3\text{/min}$$

### Step 2: Steady-State Gas Holdup ($V_{\text{gas}}$)
Using the dynamic holdup relation $V_{\text{gas}} = \dot{V}_{\text{gas}} \times \tau$:
$$V_{\text{gas}} = 178.55\text{ m}^3\text{/min} \times 0.750\text{ min} = 133.91\text{ m}^3$$
The foamy slag holds **$133.9\text{ m}^3$** of trapped $\text{CO}$ gas bubbles.

### Step 3: Slag Height Expansion ($\Delta h_{\text{slag}}$)
Across furnace hearth area $A = 28.0\text{ m}^2$:
$$\Delta h_{\text{slag}} = \frac{V_{\text{gas}}}{A} = \frac{133.91\text{ m}^3}{28.0\text{ m}^2} = 4.782\text{ m}$$
Accounting for gas bubble escape and froth void fraction ($\epsilon \approx 0.75$, physical foam height):
$$\Delta h_{\text{foam}} \approx 1.2 - 1.5\text{ meters above calm bath}$$
The injected biochar generates a **$1.2 - 1.5\text{ m}$ thick stable protective foaming slag**, shielding furnace sidewalls from electric arc radiation.""",
            "hints": ["Ideal gas law V = n * R * T / P at 1600 C (1873 K).", "Holdup volume equals volumetric gas rate times retention time."]
        }
    }

    # Inject into each unit
    for u in units:
        uid = u["id"]
        if uid in prob9_dict:
            has_prob9 = any(p["id"] == prob9_dict[uid]["id"] for p in u["problems"])
            if not has_prob9:
                u["problems"].append(prob9_dict[uid])

    return units
