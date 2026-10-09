# -*- coding: utf-8 -*-
"""
expand_industrial_deep.py
Enriches sections across all 10 units of Industrial Chemistry with deep
process flowsheets, thermodynamic reference tables, and ASTM/ISO standard testing methods.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def enrich_deep_content(units):
    enrichments = {
        "unit-1-textiles-and-dyes": {
            "sec-1-1": r"""

### ASTM & ISO Standard Fiber Testing Protocols & Comparative Matrix
Industrial textile laboratories characterize fiber morphology and mechanical resilience under standard atmospheric conditions ($20 \pm 2^\circ\text{C}$, $65 \pm 4\%\text{ RH}$, ISO 139):
- **Linear Density (dtex / denier)**: ASTM D1577 (Vibroscope method or cut-and-weigh). $1\text{ dtex} = 1\text{ g / 10,000 m}$; $1\text{ denier} = 1\text{ g / 9,000 m}$.
- **Tenacity & Elongation**: ASTM D3822 (Single-fiber tensile test). Reported in $\text{cN/dtex}$ or $\text{g/den}$.
- **Moisture Regain**: ASTM D2654.
- **Birefringence & Hermans Orientation**: Polarized light microscopy using a Berek compensator:
  $$\Delta n = n_\parallel - n_\perp$$

| Fiber Type | Density ($\text{g/cm}^3$) | Standard Tenacity ($\text{cN/dtex}$) | Wet Tenacity Retained ($\%$) | Elongation at Break ($\%$) | Initial Modulus ($\text{cN/dtex}$) | Moisture Regain ($\%$) | Melting Point ($^\circ\text{C}$) |
|---|---|---|---|---|---|---|---|
| **Cotton (American Upland)** | $1.54$ | $2.6 - 3.5$ | $110 - 120\%$ | $6 - 10\%$ | $50 - 70$ | $8.5\%$ | Decomposes $> 240^\circ\text{C}$ |
| **Cultivated Silk (Mulberry)** | $1.34$ | $3.5 - 4.5$ | $85 - 90\%$ | $18 - 25\%$ | $75 - 90$ | $11.0\%$ | Decomposes $> 175^\circ\text{C}$ |
| **Merino Wool** | $1.31$ | $1.2 - 1.6$ | $75 - 85\%$ | $25 - 40\%$ | $20 - 35$ | $15.0 - 17.0\%$ | Decomposes $> 130^\circ\text{C}$ |
| **Viscose Rayon** | $1.52$ | $1.8 - 2.4$ | $50 - 60\%$ | $18 - 25\%$ | $40 - 55$ | $12.5 - 13.5\%$ | Decomposes $> 180^\circ\text{C}$ |
| **Nylon-6,6** | $1.14$ | $4.5 - 6.0$ | $85 - 90\%$ | $25 - 35\%$ | $25 - 40$ | $4.0 - 4.5\%$ | $255 - 260^\circ\text{C}$ |
| **Poly(ethylene terephthalate)** | $1.38$ | $4.5 - 6.5$ | $100\%$ | $20 - 30\%$ | $80 - 110$ | $0.4\%$ | $255 - 265^\circ\text{C}$ |
| **High-Tenacity Industrial PET** | $1.39$ | $7.5 - 8.8$ | $100\%$ | $12 - 16\%$ | $110 - 140$ | $0.4\%$ | $260^\circ\text{C}$ |
| **Polypropylene (Isotactic)** | $0.91$ | $3.5 - 5.5$ | $100\%$ | $20 - 35\%$ | $30 - 45$ | $< 0.05\%$ | $165 - 170^\circ\text{C}$ |
| **Polyacrylonitrile (Acrylic)** | $1.18$ | $2.2 - 3.2$ | $85 - 95\%$ | $20 - 30\%$ | $40 - 60$ | $1.5 - 2.0\%$ | Sticks $> 220^\circ\text{C}$ |
| **Para-Aramid (Kevlar-29)** | $1.44$ | $18.0 - 22.0$ | $100\%$ | $3.5 - 4.0\%$ | $500 - 650$ | $3.5 - 7.0\%$ | Carbonizes $> 500^\circ\text{C}$ |
| **Ultra-High Modulus Aramid (Kevlar-49)**| $1.45$ | $20.0 - 24.0$ | $100\%$ | $2.4 - 2.8\%$ | $850 - 980$ | $3.5\%$ | Carbonizes $> 500^\circ\text{C}$ |""",

            "sec-1-5": r"""

### PET Polycondensation Thermodynamic & Kinetic Parameters
The industrial melt synthesis of poly(ethylene terephthalate) from purified terephthalic acid (PTA) and ethylene glycol (EG) is governed by two sequential reaction regimes:
1. **Direct Esterification ($240 - 260^\circ\text{C}$, $1.0 - 3.0\text{ bar}$)**:
   $$\text{PTA} + 2\text{EG} \rightleftharpoons \text{BHET} + 2\text{H}_2\text{O} \quad (\Delta H^\circ = -13.8\text{ kJ/mol})$$
   Water is continuously fractionated overhead in a distillation column to prevent reverse hydrolysis.
2. **Melt Polycondensation ($275 - 290^\circ\text{C}$, deep vacuum $< 1.0\text{ mbar}$)**:
   $$n\text{BHET} \overset{\text{Sb}_2\text{O}_3 / \text{Ti(OR)}_4}{\rightleftharpoons} \text{PET} + (n-1)\text{EG} \quad (\Delta H^\circ = +11.2\text{ kJ/mol})$$
   Because the equilibrium constant is small ($K_c \approx 0.5 - 1.0$), driving the degree of polymerization to $\overline{DP}_n > 100$ requires reducing EG partial pressure below $0.5\text{ mbar}$ using continuous wiped-film disk ring finishers.

### Intrinsic Viscosity ($[\eta]$) & Mark-Houwink-Sakurada Mechanics
Polymer melt molecular weight is monitored in-line via capillary viscometry in a $60:40$ phenol/1,1,2,2-tetrachloroethane solvent mixture at $25^\circ\text{C}$:
$$[\eta] = K \cdot \bar{M}_v^a$$
For PET in phenol/tetrachloroethane at $25^\circ\text{C}$:
$$K = 4.68 \times 10^{-4}\text{ dL/g}, \quad a = 0.68$$
- Textile filament fiber target: $[\eta] = 0.62 - 0.66\text{ dL/g}$ ($\bar{M}_n \approx 18,000 - 22,000\text{ g/mol}$).
- High-tenacity tire cord / industrial filament: $[\eta] = 0.85 - 0.98\text{ dL/g}$ ($\bar{M}_n \approx 28,000 - 34,000\text{ g/mol}$).
- Beverage bottle-grade resin (solid-state polymerized, SSP): $[\eta] = 0.78 - 0.84\text{ dL/g}$."""
        },

        "unit-2-fertilizer-industries": {
            "sec-2-2": r"""

### Thermodynamic Parameters of the Haber-Bosch Reaction
The gas-phase synthesis of ammonia over promoted wüstite iron catalysts ($\text{Fe}_{1-x}\text{O} + \text{K}_2\text{O} + \text{Al}_2\text{O}_3 + \text{CaO}$):
$$\frac{1}{2}\text{N}_2(g) + \frac{3}{2}\text{H}_2(g) \rightleftharpoons \text{NH}_3(g) \quad \Delta H_{298}^\circ = -46.11\text{ kJ/mol}$$
Standard enthalpy and Gibbs free energy as functions of absolute temperature $T$ ($300 - 800\text{ K}$):
$$\Delta H^\circ(T) = -38,340 - 8.82 \cdot T - 0.0035 \cdot T^2 \quad (\text{J/mol NH}_3)$$
$$\Delta G^\circ(T) = -45,900 + 110.2 \cdot T \quad (\text{J/mol NH}_3)$$
Equilibrium constant $K_p$ obeys the Gillespie-Beattie thermodynamic equation:
$$\log_{10} K_p = \frac{2,189.8}{T} - 5.5684 + 0.000725 \cdot T \quad (T\text{ in K})$$
Industrial converters operating at $150\text{ bar}$ and $450^\circ\text{C}$ achieve an equilibrium ammonia concentration of $15 - 18\text{ mol}\%$, requiring multi-stage condensation and recycling of unreacted $\text{N}_2/\text{H}_2$.

### Temkin-Pyzhev Intrinsic Reaction Kinetics
The catalytic rate of ammonia synthesis over iron catalysts is governed by the Temkin-Pyzhev rate equation, derived from dissociative nitrogen chemisorption being the rate-determining step:
$$r = k_1 \, p_{\text{N}_2} \left(\frac{p_{\text{H}_2}^3}{p_{\text{NH}_3}^2}\right)^\alpha - k_2 \left(\frac{p_{\text{NH}_3}^2}{p_{\text{H}_2}^3}\right)^{1 - \alpha}$$
where $\alpha \approx 0.5$ (experimentally $0.45 - 0.75$), $k_1$ is the forward rate constant for nitrogen dissociative adsorption, and $k_2$ is the reverse desorption rate constant satisfying the thermodynamic consistency condition:
$$\frac{k_1}{k_2} = K_p^2$$""",

            "sec-2-4": r"""

### Wet-Process Phosphoric Acid Filter Cake Mechanics
The reaction of fluoroapatite with sulfuric acid in the dihydrate process ($75 - 80^\circ\text{C}$, $28 - 30\%\text{ P}_2\text{O}_5$):
$$\text{Ca}_{10}(\text{PO}_4)_6\text{F}_2 + 10\text{H}_2\text{SO}_4 + 20\text{H}_2\text{O} \longrightarrow 6\text{H}_3\text{PO}_4 + 10(\text{CaSO}_4\cdot 2\text{H}_2\text{O}) \downarrow + 2\text{HF} \uparrow$$
- **Crystallization Kinetics**: Sulfate supersaturation must be maintained within a narrow window ($1.5 - 2.5\%\text{ free H}_2\text{SO}_4$) to favor tabular, rhombic gypsum crystals ($50 - 150\,\mu\text{m}$) over needle-like crystals that blind filter cloths.
- **Tilting-Pan Vacuum Filtration (Bird-Prayon Filter)**: Cake is washed counter-currently across three stages with hot water ($60^\circ\text{C}$), achieving $\text{P}_2\text{O}_5$ washing recoveries exceeding **$99.2\%$**."""
        },

        "unit-3-sugar-and-starch": {
            "sec-3-2": r"""

### Multiple-Effect Evaporator Heat Transfer & Boiling Point Elevation Table
In sugarcane and beet sugar refining, thin juice is concentrated from $14 - 16^\circ\text{Brix}$ to $65 - 70^\circ\text{Brix}$ syrup across a quintuple-effect evaporator train:

| Evaporator Effect | Operating Pressure ($\text{bar abs}$) | Vapor Temp ($^\circ\text{C}$) | Juice Brix ($^\circ\text{Bx}$) | BPE ($\text{K}$) | Boiling Temp ($^\circ\text{C}$) | Overall $U$ ($\text{W/(m}^2\cdot\text{K)}$) |
|---|---|---|---|---|---|---|
| **Effect 1** | $2.05\text{ bar}$ | $121.0^\circ\text{C}$ | $18.5^\circ\text{Bx}$ | $0.6\text{ K}$ | $121.6^\circ\text{C}$ | $2,600\text{ W/(m}^2\cdot\text{K)}$ |
| **Effect 2** | $1.45\text{ bar}$ | $110.3^\circ\text{C}$ | $24.0^\circ\text{Bx}$ | $1.0\text{ K}$ | $111.3^\circ\text{C}$ | $2,100\text{ W/(m}^2\cdot\text{K)}$ |
| **Effect 3** | $0.98\text{ bar}$ | $99.1^\circ\text{C}$ | $32.5^\circ\text{Bx}$ | $1.8\text{ K}$ | $100.9^\circ\text{C}$ | $1,600\text{ W/(m}^2\cdot\text{K)}$ |
| **Effect 4** | $0.55\text{ bar}$ | $83.7^\circ\text{C}$ | $45.0^\circ\text{Bx}$ | $3.5\text{ K}$ | $87.2^\circ\text{C}$ | $1,100\text{ W/(m}^2\cdot\text{K)}$ |
| **Effect 5** | $0.20\text{ bar}$ | $60.1^\circ\text{C}$ | $68.0^\circ\text{Bx}$ | $8.4\text{ K}$ | $68.5^\circ\text{C}$ | $650\text{ W/(m}^2\cdot\text{K)}$ |

Boiling Point Elevation ($\text{BPE}$) of sugar solutions follows the empirical Dühring line relationship:
$$\text{BPE} = \frac{0.070 \cdot B}{100 - B} \cdot \left(\frac{T_{\text{sat}} + 273.15}{100}\right)^2 \quad (\text{K})$$
where $B$ is sucrose concentration in $^\circ\text{Brix}$ and $T_{\text{sat}}$ is saturation temperature of pure water in $^\circ\text{C}$.""",

            "sec-3-5": r"""

### Sucrose Hydrolysis (Inversion) Kinetics & Optical Mutarotation
During heating at acidic $\text{pH}$, sucrose hydrolyzes into equimolar D-glucose and D-fructose:
$$\text{C}_{12}\text{H}_{22}\text{O}_{11} + \text{H}_2\text{O} \overset{\text{H}^+ / \text{Invertase}}{\longrightarrow} \text{C}_6\text{H}_{12}\text{O}_6\text{ (D-Glucose)} + \text{C}_6\text{H}_{12}\text{O}_6\text{ (D-Fructose)}$$
- **Optical Inversion Phenomenon**:
  - Pure sucrose is dextrorotatory: $[\alpha]_D^{20} = +66.5^\circ$.
  - Inverted hydrolysate contains D-glucose ($[\alpha]_D^{20} = +52.7^\circ$) and strongly levorotatory D-fructose ($[\alpha]_D^{20} = -92.4^\circ$).
  - Net specific optical rotation shifts from positive to negative:
    $$[\alpha]_{D, \text{invert}}^{20} = \frac{+52.7^\circ + (-92.4^\circ)}{2} = -19.85^\circ$$
  This reversal of polarimetric sign from $+66.5^\circ \to -19.85^\circ$ designates the reaction as **sugar inversion**."""
        },

        "unit-4-cement-and-lime": {
            "sec-4-4": r"""

### Comprehensive Phase Equilibrium & Mineralogical Properties of Portland Clinker

| Clinker Phase | Formula | Crystal System | Density ($\text{g/cm}^3$) | Heat of Hydration ($\text{J/g}$) | Rate of Hydration | 28-Day Strength Contribution |
|---|---|---|---|---|---|---|
| **Alite ($\text{C}_3\text{S}$)** | $\text{Ca}_3\text{SiO}_5$ | Monoclinic / Triclinic | $3.15$ | $-500\text{ J/g}$ | Fast ($1 - 28\text{ d}$) | High ($70 - 80\text{ MPa}$) |
| **Belite ($\text{C}_2\text{S}$)** | $\text{Ca}_2\text{SiO}_4$ | Monoclinic ($\beta$) | $3.28$ | $-250\text{ J/g}$ | Slow ($28\text{ d} - 1\text{ yr}$) | Very High (Long-term) |
| **Aluminate ($\text{C}_3\text{A}$)** | $\text{Ca}_3\text{Al}_2\text{O}_6$ | Cubic | $3.03$ | $-850\text{ J/g}$ | Very Fast ($1 - 3\text{ d}$) | Low / Moderate |
| **Ferrite ($\text{C}_4\text{AF}$)** | $\text{Ca}_4\text{Al}_2\text{Fe}_2\text{O}_{10}$ | Orthorhombic | $3.77$ | $-420\text{ J/g}$ | Moderate | Low |

Free lime ($\text{CaO}_{\text{free}}$) in sound clinker is strictly maintained below $1.0 - 1.2\text{ wt}\%$ (measured by ethylene glycol extraction according to ASTM C114)."""
        },

        "unit-5-soaps-and-detergents": {
            "sec-5-3": r"""

### McBain Ternary Phase Boundaries of Sodium Palmitate - Water - NaCl at 90°C

| Equilibrium Phase | Region Name | Soap ($\text{wt}\%$) | Water ($\text{wt}\%$) | NaCl ($\text{wt}\%$) | Rheological Character |
|---|---|---|---|---|---|
| **$L_\alpha$** | Neat Soap | $65.0 - 70.0\%$ | $29.5 - 34.5\%$ | $0.3 - 0.7\%$ | Lamellar liquid crystal, pumpable |
| **$H_1$** | Middle Soap | $35.0 - 50.0\%$ | $49.8 - 64.9\%$ | $< 0.2\%$ | Hexagonal liquid crystal, unpumpable gel |
| **$L_1$** | Nigre | $30.0 - 42.0\%$ | $56.5 - 68.5\%$ | $1.2 - 2.2\%$ | Dilute isotropic micellar liquid |
| **Solid** | Curd Soap | $> 75.0\%$ | $< 18.0\%$ | $> 6.0\%$ | Hydrated crystalline fibrous curd |

Industrial saponification finishing operates strictly within the tie-line corridor connecting **Neat Soap** and **Nigre**, preventing accidental entry into the unpumpable **Middle Soap** region.""",

            "sec-5-7": r"""

### Detergent Builder Calcium Sequestration Stability Constants
The calcium binding capacity ($\text{mg CaCO}_3\text{ sequestered / g builder}$) governs water softening efficacy:

| Detergent Builder | Chemical Formula | Binding Mechanism | $\log K_{\text{Ca}}$ ($25^\circ\text{C}, \text{pH } 10$) | $\text{Ca}^{2+}$ Capacity ($\text{mg CaCO}_3\text{/g}$) | Environmental Impact |
|---|---|---|---|---|---|
| **Sodium Tripolyphosphate (STPP)** | $\text{Na}_5\text{P}_3\text{O}_{10}$ | Soluble Chelation | $6.50$ | $310\text{ mg/g}$ | High Eutrophication (Banned in laundry) |
| **Zeolite A** | $\text{Na}_{12}\text{Al}_{12}\text{Si}_{12}\text{O}_{48}\cdot 27\text{H}_2\text{O}$ | Heterogeneous Ion Exchange | $4.80$ | $175\text{ mg/g}$ | Zero toxicity, insoluble particulate |
| **Trisodium Citrate** | $\text{Na}_3\text{C}_6\text{H}_5\text{O}_7$ | Soluble Chelation | $3.50$ | $120\text{ mg/g}$ | Rapid 100% biodegradation |
| **Polycarboxylate (AA/MA)** | Copolymer Acrylic/Maleic | Crystal growth inhibition | $5.20$ | $260\text{ mg/g}$ | Persistent in sludge (Non-toxic) |
| **Sodium Carbonate (Soda Ash)** | $\text{Na}_2\text{CO}_3$ | Precipitation ($\text{CaCO}_3 \downarrow$)| — | $940\text{ mg/g}$ | Harmless mineral alkali |"""
        },

        "unit-6-pulp-and-paper": {
            "sec-6-4": r"""

### Tomlinson Recovery Boiler Smelt & Black Liquor Combustion Energy Balance
Concentrated black liquor dry solids ($75 - 80\text{ wt}\%$ dry matter) combust with an adiabatic lower heating value $\text{LHV} \approx 13,500 - 14,500\text{ kJ/kg dry solids}$:
- **Primary Air ($40 - 45\%$ total air)**: Injected directly at the hearth level at low velocity to maintain the reducing char bed temperature at $950 - 1050^\circ\text{C}$ ($\lambda_{\text{primary}} = 0.65 - 0.75$, substoichiometric).
- **Secondary Air ($30 - 35\%$)**: Injected above the char bed to burn volatile pyrolysis gases and stabilize the bed geometry.
- **Tertiary & Quaternary Air ($25 - 30\%$)**: Injected in the upper furnace at high velocity ($50 - 80\text{ m/s}$) to create intense turbulence, ensuring $100\%$ burnout of $\text{CO}$ and volatile sulfur species ($\text{H}_2\text{S}, \text{CH}_3\text{SH}$).
Superheated steam is generated at $450 - 490^\circ\text{C}$ and $60 - 90\text{ bar}$, generating $3.2 - 3.8\text{ tons of high-pressure steam per metric ton of black liquor dry solids}$."""
        },

        "unit-7-glass-and-ceramics": {
            "sec-7-3": r"""

### Float Glass Tin Bath Atmosphere & Defect Control
The molten tin bath ($50 - 65\text{ m}$ length, containing $150 - 250\text{ metric tons}$ of pure molten tin) operates under rigorous atmospheric protection:
- **Protective Gas Composition**: $95.0\text{ vol}\%\text{ N}_2 + 5.0\text{ vol}\%\text{ H}_2$ (purity $> 99.999\%$, dew point $< -60^\circ\text{C}$, oxygen content $< 2\text{ ppm}$).
- **Tin Oxidation Thermodynamics**:
  $$\text{Sn}(l) + \frac{1}{2}\text{O}_2(g) \rightleftharpoons \text{SnO}(g)$$
  $$\text{SnO}(g) + \frac{1}{2}\text{O}_2(g) \rightleftharpoons \text{SnO}_2(s) \downarrow$$
  Hydrogen in the atmosphere reduces tin oxide vapors back to metallic tin:
  $$\text{SnO}(g) + \text{H}_2(g) \rightleftharpoons \text{Sn}(l) + \text{H}_2\text{O}(g)$$
- **Tin Ingress (Bottom Surface Blooming)**: At $1000^\circ\text{C}$, stannous ions ($\text{Sn}^{2+}$) diffuse into the bottom surface of the glass ribbon via ion exchange with $\text{Na}^+$ ions to a depth of $5 - 20\,\mu\text{m}$. During subsequent thermal toughening ($650^\circ\text{C}$), stannous ions oxidize to $\text{Sn}^{4+}$, producing faint surface iridescence ("bloom")."""
        },

        "unit-8-caustic-chlorine": {
            "sec-8-3": r"""

### Complete Electrochemical Parameters of Modern Chlor-Alkali Membrane Cells

| Electrochemical Parameter | Symbol | Industrial Operating Range | Reference Target Value |
|---|---|---|---|
| **Current Density** | $j$ | $4.0 - 7.0\text{ kA/m}^2$ | $6.0\text{ kA/m}^2$ |
| **Operating Temperature** | $T$ | $85 - 92^\circ\text{C}$ | $88^\circ\text{C}$ |
| **Anolyte NaCl Concentration** | $[\text{NaCl}]_{\text{ano}}$ | $190 - 220\text{ g/L}$ | $205\text{ g/L}$ |
| **Catholyte NaOH Concentration**| $[\text{NaOH}]_{\text{cat}}$ | $32.0 - 35.0\text{ wt}\%$ | $33.5\text{ wt}\%$ |
| **Current Efficiency (NaOH)** | $\eta_{\text{NaOH}}$ | $95.5 - 97.5\%$ | $96.5\%$ |
| **Operating Cell Voltage** | $U_{\text{cell}}$ | $2.95 - 3.15\text{ V}$ | $3.02\text{ V}$ |
| **Specific Power Consumption** | $w_{\text{spec}}$ | $2,050 - 2,250\text{ kWh/t NaOH}$ | $2,120\text{ kWh/t NaOH}$ |
| **Membrane Service Life** | $\tau_{\text{mem}}$ | $3 - 5\text{ years}$ | $4\text{ years}$ |
| **Anode Coating Service Life** | $\tau_{\text{anode}}$ | $8 - 12\text{ years}$ | $10\text{ years}$ |"""
        },

        "unit-9-petroleum-and-fuels": {
            "sec-9-3": r"""

### FCC Zeolite Catalyst Deactivation & Vanadium/Nickel Metal Passivation
Cracking heavy residue feedstocks deposits heavy metals ($\text{Ni, V, Fe}$) onto the circulating zeolite catalyst particles:
- **Nickel Poisoning**: Deposited nickel acts as an aggressive dehydrogenation catalyst, increasing undesirable dry gas ($\text{H}_2, \text{CH}_4$) and coke yields at the expense of gasoline. Nickel is chemically passivated by injecting antimony or bismuth metallo-organic compounds into the feed:
  $$3\text{Ni} + 2\text{Sb} \longrightarrow \text{Ni}_3\text{Sb}_2 \quad (\text{Catalytically Inert Alloy})$$
- **Vanadium Destruction**: Under high-temperature oxidizing conditions in the regenerator ($700^\circ\text{C}$), vanadium oxidizes to volatile vanadic acid ($\text{H}_3\text{VO}_4$ or $\text{V}_2\text{O}_5$). Vanadic acid penetrates the zeolite pores, chemically attacking the framework $[\text{AlO}_4]^{5-}$ tetrahedra and collapsing the crystalline faujasite structure into amorphous silica-alumina. Vanadium is trapped by co-feeding magnesium/rare-earth titanate scavengers."""
        },

        "unit-10-metallurgy-and-steel": {
            "sec-10-3": r"""

### Standard Enthalpies & Free Energies of Iron Blast Furnace Reactions

| Reaction | $\Delta H_{298}^\circ$ ($\text{kJ/mol}$) | $\Delta G^\circ(1000\text{ K})$ ($\text{kJ/mol}$) | Reaction Type | Location in Furnace |
|---|---|---|---|---|
| **$\text{C} + \frac{1}{2}\text{O}_2 \to \text{CO}$** | $-110.5\text{ kJ}$ | $-200.3\text{ kJ}$ | Exothermic | Tuyere Raceway |
| **$\text{C} + \text{CO}_2 \rightleftharpoons 2\text{CO}$** | $+172.5\text{ kJ}$ | $-5.2\text{ kJ}$ | Intensely Endothermic | Lower Shaft / Bosh |
| **$3\text{Fe}_2\text{O}_3 + \text{CO} \to 2\text{Fe}_3\text{O}_4 + \text{CO}_2$** | $-52.8\text{ kJ}$ | $-72.1\text{ kJ}$ | Exothermic | Upper Shaft ($400 - 600^\circ\text{C}$) |
| **$\text{Fe}_3\text{O}_4 + \text{CO} \to 3\text{FeO} + \text{CO}_2$** | $+36.4\text{ kJ}$ | $+12.4\text{ kJ}$ | Endothermic | Middle Shaft ($600 - 800^\circ\text{C}$) |
| **$\text{FeO} + \text{CO} \rightleftharpoons \text{Fe} + \text{CO}_2$** | $-17.2\text{ kJ}$ | $-3.8\text{ kJ}$ | Exothermic | Shaft ($800 - 1000^\circ\text{C}$) |
| **$\text{FeO} + \text{C} \to \text{Fe} + \text{CO}$** | $+155.3\text{ kJ}$ | $-9.0\text{ kJ}$ | Strongly Endothermic | Bosh / Hearth ($> 1000^\circ\text{C}$) |
| **$\text{CaCO}_3 \rightleftharpoons \text{CaO} + \text{CO}_2$** | $+178.2\text{ kJ}$ | $+18.0\text{ kJ}$ | Endothermic | Middle Shaft ($800 - 900^\circ\text{C}$) |"""
        }
    }

    for u in units:
        uid = u["id"]
        if uid in enrichments:
            for s in u["sections"]:
                sid = s["id"]
                if sid in enrichments[uid]:
                    # Append enrichment if not already present
                    if "ASTM & ISO Standard" not in s["content"] and "Thermodynamic Parameters of the Haber-Bosch" not in s["content"] and "Multiple-Effect Evaporator Heat Transfer" not in s["content"] and "Comprehensive Phase Equilibrium" not in s["content"] and "McBain Ternary Phase Boundaries" not in s["content"] and "Tomlinson Recovery Boiler Smelt" not in s["content"] and "Float Glass Tin Bath Atmosphere" not in s["content"] and "Complete Electrochemical Parameters" not in s["content"] and "FCC Zeolite Catalyst Deactivation" not in s["content"] and "Standard Enthalpies & Free Energies" not in s["content"]:
                        s["content"] += enrichments[uid][sid]

    return units
