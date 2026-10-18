# -*- coding: utf-8 -*-
"""
expand_industrial_problem8.py
Injects Problem 8 across all 10 units of Industrial Chemistry.
Brings total problems from 70 to 80.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def inject_problem_8(units):
    prob8_dict = {
        "unit-1-textiles-and-dyes": {
            "id": "prob-1-8",
            "problemNumber": "1.8",
            "title": "Reactive Dye Fixation Efficiency & Fenton Effluent Decolorization",
            "difficulty": "Medium",
            "statement": r"""A textile dyeing plant colors $1,000\text{ kg}$ of cotton fabric with a vinyl sulfone reactive dye.
- The dye bath initially contains $40.0\text{ kg}$ of pure reactive dye ($M = 650.0\text{ g/mol}$) in $10,000\text{ L}$ of water.
- At completion of dyeing, $85.0\%$ of the initial dye has exhausted onto the fabric.
- Of the exhausted dye, $78.0\%$ undergoes covalent fixation with cellulose; the remaining $22.0\%$ undergoes irreversible hydrolysis into inactive hydrolyzed dye and is washed off in the rinse baths.
- All spent dye bath liquor and washings are combined into a centralized wastewater equalization tank totaling $25.0\text{ m}^3$ of effluent.
- A Fenton advanced oxidation reactor ($\text{Fe}^{2+} / \text{H}_2\text{O}_2$) treats the effluent at $\text{pH } 3.0$. Full chromophore decolorization requires a stoichiometric ratio of $12.0\text{ moles of H}_2\text{O}_2$ ($34.01\text{ g/mol}$) per mole of residual dye molecule.

1. Calculate the mass of dye covalently fixed onto the cotton fabric ($m_{\text{fixed}}$ in $\text{kg}$) and the net overall fixation efficiency on total starting dye.
2. Determine the total mass and moles of residual dye present in the wastewater effluent.
3. Calculate the required mass of $35.0\text{ wt}\%\text{ aqueous H}_2\text{O}_2$ solution needed to decolorize the effluent.""",
            "solution": r"""### Step 1: Covalent Dye Fixation & Overall Efficiency
Initial dye: $m_0 = 40.0\text{ kg}$.
Exhausted dye onto fiber:
$$m_{\text{exh}} = 0.850 \times 40.0\text{ kg} = 34.0\text{ kg}$$
Covalently fixed dye:
$$m_{\text{fixed}} = 0.780 \times 34.0\text{ kg} = 26.52\text{ kg}$$
Overall fixation efficiency on total dye charged:
$$T_{\text{overall}} = \frac{m_{\text{fixed}}}{m_0} \times 100\% = \frac{26.52\text{ kg}}{40.0\text{ kg}} \times 100\% = 66.30\%$$
The plant fixes **$26.52\text{ kg}$ of dye** ($66.3\%$ overall efficiency).

### Step 2: Residual Dye in Wastewater
Unexhausted dye left in bath:
$$m_{\text{unexh}} = 40.0 - 34.0 = 6.00\text{ kg}$$
Hydrolyzed dye washed off fiber:
$$m_{\text{hydrolyzed}} = 34.0 - 26.52 = 7.48\text{ kg}$$
Total residual dye in effluent:
$$m_{\text{waste}} = 6.00 + 7.48 = 13.48\text{ kg}$$
Moles of residual dye in effluent ($M = 650.0\text{ g/mol}$):
$$n_{\text{waste}} = \frac{13.48 \times 10^3\text{ g}}{650.0\text{ g/mol}} = 20.738\text{ mol}$$

### Step 3: Fenton Hydrogen Peroxide Requirement
Stoichiometric $\text{H}_2\text{O}_2$ required:
$$n_{\text{H}_2\text{O}_2} = 12.0 \times 20.738\text{ mol} = 248.86\text{ mol}$$
Mass of pure $\text{H}_2\text{O}_2$:
$$m_{\text{pure H}_2\text{O}_2} = 248.86\text{ mol} \times 34.015\text{ g/mol} = 8,465\text{ g} = 8.465\text{ kg}$$
Mass of $35.0\text{ wt}\%\text{ H}_2\text{O}_2$ commercial solution:
$$m_{\text{sol}} = \frac{8.465\text{ kg}}{0.350} = 24.186\text{ kg} \approx 24.19\text{ kg}$$

The wastewater treatment requires **$24.2\text{ kg}$ of $35\%\text{ H}_2\text{O}_2$ solution** to fully decolorize the residual dye.""",
            "hints": ["Calculate fixed dye as Initial * Exhaustion * Fixation.", "Waste dye is total dye minus fixed dye."]
        },

        "unit-2-fertilizer-industries": {
            "id": "prob-2-8",
            "problemNumber": "2.8",
            "title": "Fluid-Bed Urea Granulation Droplet Solidification & Growth Balance",
            "difficulty": "Medium",
            "statement": r"""A fluid-bed urea granulation unit produces $\dot{m}_{\text{granules}} = 50.0\text{ metric tons/h}$ of commercial spherical urea granules ($99.8\text{ wt}\%\text{ urea}$, $\rho_{\text{urea}} = 1,320\text{ kg/m}^3$) with an average diameter of $d_p = 3.20\text{ mm}$.
- Recycled undersized solid seed particles entering the fluid bed have an average diameter of $d_{\text{seed}} = 1.60\text{ mm}$.
- Molten concentrated urea melt ($99.5\text{ wt}\%$ melt at $138^\circ\text{C}$) is sprayed continuously over the seeds.
- The granules discharge at $95^\circ\text{C}$.
- Latent heat of crystallization of urea is $\Delta H_{\text{cryst}} = 245\text{ kJ/kg}$.
- Specific heat of solid urea is $c_p = 1.45\text{ kJ/(kg}\cdot\text{K)}$.
- Heat loss through the granulator walls is $4.0\%$ of the total heat released.

1. Assuming spherical geometry, calculate the mass ratio of final product granule to seed particle ($m_{\text{product}} / m_{\text{seed}}$).
2. Determine the required hourly recycle rate of seed particles ($\text{metric tons/h}$) and the spray feed rate of molten urea melt.
3. Calculate the thermal cooling duty ($\text{kW}$) that must be removed by fluidizing air.""",
            "solution": r"""### Step 1: Single Particle Mass Growth Ratio
Mass of a sphere is proportional to diameter cubed ($m \propto d^3$):
$$\frac{m_{\text{product}}}{m_{\text{seed}}} = \left(\frac{d_p}{d_{\text{seed}}}\right)^3 = \left(\frac{3.20\text{ mm}}{1.60\text{ mm}}\right)^3 = 2^3 = 8.00$$
Each seed particle gains $7.00\times$ its initial mass from sprayed melt coatings.

### Step 2: Seed Recycle & Melt Spray Rates
Total product granule rate: $\dot{m}_{\text{product}} = 50.0\text{ metric tons/h}$.
Seed recycle rate required:
$$\dot{m}_{\text{seed}} = \frac{\dot{m}_{\text{product}}}{8.00} = \frac{50.0\text{ t/h}}{8.00} = 6.25\text{ metric tons/h}$$
Molten urea spray rate required:
$$\dot{m}_{\text{spray}} = \dot{m}_{\text{product}} - \dot{m}_{\text{seed}} = 50.0 - 6.25 = 43.75\text{ metric tons/h} = 43,750\text{ kg/h}$$

### Step 3: Cooling Duty Removed by Air
Sensible cooling of melt from $138^\circ\text{C}$ to $95^\circ\text{C}$ ($\Delta T = 43\text{ K}$) plus latent crystallization:
$$\Delta h_{\text{solidification}} = \Delta H_{\text{cryst}} + c_p \cdot \Delta T = 245 + 1.45(43) = 245 + 62.35 = 307.35\text{ kJ/kg}$$
Total heat released by sprayed melt:
$$\dot{Q}_{\text{released}} = 43,750\text{ kg/h} \times 307.35\text{ kJ/kg} = 1.34466 \times 10^7\text{ kJ/h}$$
Minus $4.0\%$ wall losses ($0.96\times$ removed by air):
$$\dot{Q}_{\text{air}} = 0.96 \times 1.34466 \times 10^7 = 1.29087 \times 10^7\text{ kJ/h}$$
In thermal kilowatts ($\text{kW}$):
$$\dot{Q}_{\text{cooling}} = \frac{1.29087 \times 10^7\text{ kJ/h}}{3,600\text{ s/h}} = 3,585.75\text{ kW} \approx 3.59\text{ MW}$$

The unit requires **$6.25\text{ t/h}$ seed recycle**, sprays **$43.75\text{ t/h}$ melt**, and fluidizing air removes **$3.59\text{ MW}$** of cooling heat.""",
            "hints": ["Volume ratio scales as cube of diameter.", "Sensible heat is c_p * Delta_T; add crystallization enthalpy."]
        },

        "unit-3-sugar-and-starch": {
            "id": "prob-3-8",
            "problemNumber": "3.8",
            "title": "Simulated Moving Bed (SMB) Chromatographic HFCS-55 Formulation",
            "difficulty": "Hard",
            "statement": r"""A corn sweetener refinery operates a continuous Simulated Moving Bed (SMB) chromatographic separation unit to manufacture beverage-grade High-Fructose Corn Syrup (HFCS-55, $55.0\text{ wt}\%\text{ fructose}$, $41.0\text{ wt}\%\text{ glucose}$, $4.0\text{ wt}\%\text{ oligosaccharides}$ on dry solids).
- The feed entering the SMB unit is enzymatically isomerized syrup (HFCS-42) containing $42.0\text{ wt}\%\text{ fructose}$ and $58.0\text{ wt}\%\text{ non-fructose sugars}$ at a flow rate of $\dot{m}_{\text{feed}} = 20.0\text{ metric tons/h}$ (dry solids).
- The SMB unit separates the feed into:
  - **Extract stream**: Enriched fructose containing $90.0\text{ wt}\%\text{ fructose}$ and $10.0\text{ wt}\%\text{ glucose}$.
  - **Raffinate stream**: Enriched glucose containing $10.0\text{ wt}\%\text{ fructose}$ and $90.0\text{ wt}\%\text{ glucose}$ (recycled back to the isomerization reactors).
- A portion of the $90.0\text{ wt}\%$ fructose extract is blended with bypass $42.0\text{ wt}\%$ syrup to formulate the commercial **HFCS-55 product**.

1. Apply component mass balances across the SMB unit to calculate the dry solids mass flow rates of the Extract and Raffinate streams in metric tons per hour.
2. Determine the fructose recovery efficiency in the Extract stream.
3. Calculate the blending ratio (mass of $90\%$ Extract to mass of bypass $42\%$ syrup) required to produce the $55.0\text{ wt}\%\text{ fructose}$ product.""",
            "solution": r"""### Step 1: SMB Material Balance
Let $E$ be the Extract flow rate and $R$ be the Raffinate flow rate (dry tons/h).
Total mass balance:
$$E + R = 20.0\text{ metric tons/h} \implies R = 20.0 - E$$
Fructose mass balance:
$$0.90 \cdot E + 0.10 \cdot R = 0.42 \times 20.0 = 8.40\text{ metric tons/h}$$
Substitute $R = 20.0 - E$:
$$0.90 \cdot E + 0.10(20.0 - E) = 8.40$$
$$0.90 \cdot E + 2.00 - 0.10 \cdot E = 8.40$$
$$0.80 \cdot E = 8.40 - 2.00 = 6.40$$
$$E = \frac{6.40}{0.80} = 8.00\text{ metric tons/h}$$
$$R = 20.00 - 8.00 = 12.00\text{ metric tons/h}$$

The SMB produces **$8.00\text{ metric tons/h}$ Extract** and **$12.00\text{ metric tons/h}$ Raffinate**.

### Step 2: Fructose Recovery Efficiency
Fructose in Extract:
$$m_{\text{fructose, extract}} = 0.90 \times 8.00 = 7.20\text{ metric tons/h}$$
Total fructose entering in feed:
$$m_{\text{fructose, feed}} = 8.40\text{ metric tons/h}$$
$$\% \text{ Recovery} = \frac{7.20\text{ t}}{8.40\text{ t}} \times 100\% = 85.71\%$$

### Step 3: Blending for HFCS-55
Let $m_E$ be mass of $90\%$ extract blended with $m_B$ of $42\%$ bypass syrup to yield $55\%$ product:
$$0.90 \cdot m_E + 0.42 \cdot m_B = 0.55 \cdot (m_E + m_B)$$
$$0.90 \cdot m_E - 0.55 \cdot m_E = 0.55 \cdot m_B - 0.42 \cdot m_B$$
$$0.35 \cdot m_E = 0.13 \cdot m_B$$
$$\frac{m_E}{m_B} = \frac{0.13}{0.35} \approx 0.3714$$
Or in percentage:
$$\% \text{ Extract in blend} = \frac{0.13}{0.13 + 0.35} \times 100\% = \frac{0.13}{0.48} \times 100\% = 27.08\%$$
Blending requires **$0.371\text{ parts}$ of $90\%$ Extract per $1.0\text{ part}$ of $42\%$ syrup** ($27.1\text{ wt}\%$ extract).""",
            "hints": ["Set up simultaneous equations for total mass and fructose mass.", "Use the blending lever rule to determine HFCS-55 proportions."]
        },

        "unit-4-cement-and-lime": {
            "id": "prob-4-8",
            "problemNumber": "4.8",
            "title": "Limestone Calcined Clay Cement (LC3) Carbon Footprint Mitigation",
            "difficulty": "Easy",
            "statement": r"""A cement manufacturing corporation evaluates transitioning an OPC plant to Limestone Calcined Clay Cement ($\text{LC}^3$).
Baseline Ordinary Portland Cement (OPC) production:
- Clinker factor: $95.0\text{ wt}\%$ clinker ($5.0\text{ wt}\%$ gypsum).
- Specific $\text{CO}_2$ emissions: $860.0\text{ kg CO}_2\text{ / metric ton OPC}$.
$\text{LC}^3$ formulation:
- $50.0\text{ wt}\%$ Clinker
- $30.0\text{ wt}\%$ Calcined Clay (Metakaolin)
- $15.0\text{ wt}\%$ Uncalcined Limestone
- $5.0\text{ wt}\%$ Gypsum
Emission factors for individual materials:
- Clinker manufacturing: $850.0\text{ kg CO}_2\text{ / ton clinker}$
- Clay calcination ($750^\circ\text{C}$ in gas calciner): $180.0\text{ kg CO}_2\text{ / ton calcined clay}$
- Uncalcined limestone grinding: $15.0\text{ kg CO}_2\text{ / ton limestone}$
- Gypsum handling: $10.0\text{ kg CO}_2\text{ / ton gypsum}$

1. Calculate the specific embodied $\text{CO}_2$ emissions per metric ton of $\text{LC}^3$ cement produced.
2. Determine the percentage $\text{CO}_2$ emission reduction achieved per ton of cement compared to baseline OPC.
3. If an industrial plant produces $2.0 \times 10^6\text{ metric tons/year}$ of cement, calculate the total annual $\text{CO}_2$ avoided in metric tons.""",
            "solution": r"""### Step 1: Specific $\text{CO}_2$ Emissions of $\text{LC}^3$
Sum the weighted emissions of all components per metric ton ($1,000\text{ kg}$) of $\text{LC}^3$:
- Clinker ($50.0\%$): $0.50 \times 850.0 = 425.00\text{ kg CO}_2$
- Calcined clay ($30.0\%$): $0.30 \times 180.0 = 54.00\text{ kg CO}_2$
- Limestone ($15.0\%$): $0.15 \times 15.0 = 2.25\text{ kg CO}_2$
- Gypsum ($5.0\%$): $0.05 \times 10.0 = 0.50\text{ kg CO}_2$
Total specific emissions:
$$E_{\text{LC}^3} = 425.00 + 54.00 + 2.25 + 0.50 = 481.75\text{ kg CO}_2\text{/metric ton LC}^3$$

### Step 2: Percentage Carbon Reduction
$$\% \text{ Reduction} = \frac{E_{\text{OPC}} - E_{\text{LC}^3}}{E_{\text{OPC}}} \times 100\% = \frac{860.0 - 481.75}{860.0} \times 100\% = \frac{378.25}{860.0} \times 100\% = 43.98\%$$
Transitioning to $\text{LC}^3$ slashes carbon intensity by **$44.0\%$**.

### Step 3: Total Annual Emissions Avoided
For $2,000,000\text{ metric tons/year}$:
$$\Delta E_{\text{annual}} = 2,000,000\text{ tons} \times 0.37825\text{ tons CO}_2\text{/ton} = 756,500\text{ metric tons CO}_2\text{/year}$$

The plant eliminates **$756,500\text{ metric tons}$ of $\text{CO}_2$ emissions annually**.""",
            "hints": ["Multiply each ingredient mass fraction by its specific emission factor.", "Annual avoided CO2 equals delta per ton times total annual output."]
        },

        "unit-5-soaps-and-detergents": {
            "id": "prob-5-8",
            "problemNumber": "5.8",
            "title": "Multi-Enzyme Detergent Wash Kinetics & Protease Soil Hydrolysis",
            "difficulty": "Medium",
            "statement": r"""A concentrated liquid laundry detergent contains an engineered subtilisin bacterial alkaline protease ($0.80\text{ wt}\%$, enzyme concentration $[E] = 5.0\times 10^{-7}\text{ M}$ in the wash liquor).
During the main wash cycle at $30^\circ\text{C}$ and $\text{pH } 9.0$, hydrolysis of insoluble proteinaceous peptide bonds follows Michaelis-Menten kinetics:
$$v = \frac{V_{\max} [S]}{K_m + [S]} = \frac{k_{\text{cat}} [E] [S]}{K_m + [S]}$$
- Catalytic turnover number: $k_{\text{cat}} = 120.0\text{ s}^{-1}$ ($7,200\text{ min}^{-1}$)
- Michaelis constant: $K_m = 2.50 \times 10^{-4}\text{ M}$
- Initial peptide bond substrate concentration on the soiled test swatch is $[S]_0 = 1.00 \times 10^{-3}\text{ M}$.

1. Calculate the maximum enzymatic velocity ($V_{\max}$) in $\text{mol/(L}\cdot\text{min)}$.
2. Determine the initial reaction velocity ($v_0$) in $\text{mol/(L}\cdot\text{min)}$.
3. If an alternative low-temperature cold-active mutant enzyme achieves $k_{\text{cat}} = 280.0\text{ s}^{-1}$ and $K_m = 1.80 \times 10^{-4}\text{ M}$, calculate the percentage increase in initial stain removal rate.""",
            "solution": r"""### Step 1: Maximum Reaction Velocity ($V_{\max}$)
$$V_{\max} = k_{\text{cat}} \cdot [E] = 7,200\text{ min}^{-1} \times (5.0 \times 10^{-7}\text{ M}) = 3.60 \times 10^{-3}\text{ M/min} = 3.60\text{ mmol/(L}\cdot\text{min)}$$

### Step 2: Initial Reaction Velocity ($v_0$)
At $[S]_0 = 1.00 \times 10^{-3}\text{ M}$:
$$v_0 = \frac{V_{\max} [S]_0}{K_m + [S]_0} = \frac{3.60 \times 10^{-3} \times 1.00 \times 10^{-3}}{2.50 \times 10^{-4} + 1.00 \times 10^{-3}} = \frac{3.60 \times 10^{-6}}{1.25 \times 10^{-3}} = 2.88 \times 10^{-3}\text{ M/min}$$
The initial velocity is **$2.88\text{ mmol/(L}\cdot\text{min)}$**.

### Step 3: Mutant Enzyme Rate Comparison
For mutant enzyme ($k_{\text{cat}} = 280\text{ s}^{-1} = 16,800\text{ min}^{-1}$, $K_m = 1.80 \times 10^{-4}\text{ M}$):
$$V_{\max, \text{mutant}} = 16,800\text{ min}^{-1} \times (5.0 \times 10^{-7}\text{ M}) = 8.40 \times 10^{-3}\text{ M/min}$$
$$v_{0, \text{mutant}} = \frac{8.40 \times 10^{-3} \times 1.00 \times 10^{-3}}{1.80 \times 10^{-4} + 1.00 \times 10^{-3}} = \frac{8.40 \times 10^{-6}}{1.18 \times 10^{-3}} = 7.1186 \times 10^{-3}\text{ M/min}$$
Percentage acceleration in soil removal:
$$\% \text{ Increase} = \frac{7.1186 - 2.8800}{2.8800} \times 100\% = \frac{4.2386}{2.8800} \times 100\% = 147.17\%$$

The cold-active mutant enzyme delivers a **$147.2\%$ faster initial stain removal rate**.""",
            "hints": ["V_max equals k_cat times [E].", "Initial rate v_0 = (V_max * [S]) / (K_m + [S])."]
        },

        "unit-6-pulp-and-paper": {
            "id": "prob-6-8",
            "problemNumber": "6.8",
            "title": "Cellulose Nanocrystal (CNC) Acid Hydrolysis Mass Yield",
            "difficulty": "Easy",
            "statement": r"""A biorefinery pilot plant produces Cellulose Nanocrystals (CNC) from bleached softwood Kraft dissolving pulp.
- The digester charges $100.0\text{ kg}$ of bone-dry cellulose pulp ($\text{crystallinity } X_c = 68.0\%$).
- The reaction uses $64.0\text{ wt}\%\text{ aqueous H}_2\text{SO}_4$ at an acid-to-pulp mass ratio of $10.0 : 1.0$ at $45^\circ\text{C}$ for $45\text{ minutes}$.
- The strong acid completely hydrolyzes the amorphous domains into soluble glucose/cellobiose, while $92.0\%$ of the initial crystalline cellulose core is recovered intact as crystalline nanorods.
- Centrifugation, membrane diafiltration, and freeze-drying yield dry CNC powder.

1. Calculate the mass of crystalline cellulose and amorphous cellulose initially present in the $100.0\text{ kg}$ pulp charge.
2. Determine the dry mass of purified CNCs produced in kilograms and the overall percentage process yield on starting dry pulp.
3. Calculate the total mass of $64.0\text{ wt}\%\text{ H}_2\text{SO}_4$ acid solution required for the reaction batch.""",
            "solution": r"""### Step 1: Initial Crystalline & Amorphous Fractions
In $100.0\text{ kg}$ of dry pulp ($X_c = 68.0\%$):
- Crystalline cellulose: $m_{\text{cryst}} = 0.680 \times 100.0\text{ kg} = 68.0\text{ kg}$.
- Amorphous cellulose: $m_{\text{amorph}} = 100.0 - 68.0 = 32.0\text{ kg}$.

### Step 2: CNC Production & Process Yield
With $92.0\%$ crystalline recovery:
$$m_{\text{CNC}} = 0.920 \times 68.0\text{ kg} = 62.56\text{ kg}$$
Overall process mass yield on raw pulp:
$$\% \text{ Yield} = \frac{62.56\text{ kg}}{100.0\text{ kg}} \times 100\% = 62.56\%$$
The plant produces **$62.56\text{ kg}$ of pure CNC powder** ($62.6\%$ yield).

### Step 3: Acid Solution Requirement
At an acid-to-pulp ratio of $10.0 : 1.0$:
$$m_{\text{acid sol}} = 10.0 \times 100.0\text{ kg} = 1,000.0\text{ kg}$$
The batch requires **$1,000\text{ kg}$** of $64\text{ wt}\%\text{ H}_2\text{SO}_4$ solution.""",
            "hints": ["Multiply pulp mass by crystallinity fraction, then by 0.92 recovery.", "Acid solution mass is pulp mass multiplied by 10."]
        },

        "unit-7-glass-and-ceramics": {
            "id": "prob-7-8",
            "problemNumber": "7.8",
            "title": "Lithium Aluminosilicate (LAS) Glass-Ceramic Crystallization Kinetics (JMAK)",
            "difficulty": "Hard",
            "statement": r"""A lithium aluminosilicate precursor glass plate is heat-treated at $780^\circ\text{C}$ to crystallize $\beta$-quartz solid solution.
Phase transformation follows the Johnson-Mehl-Avrami-Kolmogorov (JMAK) rate equation:
$$X(t) = 1 - \exp\left[ - (k \cdot t)^n \right]$$
where $X(t)$ is fractional crystalline volume, $k$ is the reaction rate constant in $\text{min}^{-1}$, and $n$ is the Avrami exponent.
- Experimental X-ray diffraction measurements at $780^\circ\text{C}$ show:
  - After $t_1 = 15.0\text{ minutes}$, crystallization is $X_1 = 0.200$ ($20.0\%$).
  - After $t_2 = 30.0\text{ minutes}$, crystallization reaches $X_2 = 0.650$ ($65.0\%$).

1. Linearize the JMAK equation to determine the Avrami exponent $n$ and the rate constant $k$.
2. Based on classical nucleation theory (for 3D spherical growth from pre-existing fixed nuclei, $n = 3$; for constant nucleation rate, $n = 4$), deduce the nucleation mechanism.
3. Calculate the heat-treatment time required to achieve $95.0\%$ target crystallinity ($X = 0.950$).""",
            "solution": r"""### Step 1: Linearization of JMAK Equation
Rearranging the JMAK relation:
$$1 - X = \exp\left[ - (k \cdot t)^n \right] \implies \ln(1 - X) = - (k \cdot t)^n$$
$$\ln\left( -\ln(1 - X) \right) = n \ln k + n \ln t$$
For the two experimental data points:
- At $t_1 = 15.0\text{ min}$, $1 - X_1 = 0.800$:
  $$Y_1 = \ln(-\ln 0.800) = \ln(0.223144) = -1.5000$$
- At $t_2 = 30.0\text{ min}$, $1 - X_2 = 0.350$:
  $$Y_2 = \ln(-\ln 0.350) = \ln(1.04982) = +0.04862$$

Calculate the Avrami exponent $n$:
$$n = \frac{Y_2 - Y_1}{\ln t_2 - \ln t_1} = \frac{0.04862 - (-1.5000)}{\ln(30.0) - \ln(15.0)} = \frac{1.54862}{\ln 2} = \frac{1.54862}{0.69315} = 2.234 \approx 2.23$$
Now compute $k$:
$$\ln k = \frac{Y_1 - n \ln t_1}{n} = \frac{-1.5000 - 2.234 \ln(15.0)}{2.234} = \frac{-1.5000 - 2.234(2.70805)}{2.234} = \frac{-1.5000 - 6.0498}{2.234} = -3.3795$$
$$k = e^{-3.3795} = 0.03406\text{ min}^{-1}$$

### Step 2: Nucleation Mechanism Deduction
An Avrami exponent $n \approx 2.0 - 2.5$ signifies diffusion-controlled three-dimensional crystal growth originating from a fixed, finite number of pre-existing heterogeneous nuclei (nucleated by $\text{TiO}_2/\text{ZrO}_2$ nanoparticles during the prior $650^\circ\text{C}$ thermal nucleation hold), with negligible ongoing nucleation at $780^\circ\text{C}$.

### Step 3: Time to Reach $95.0\%$ Crystallinity
For $X = 0.950$, $1 - X = 0.050$:
$$\ln(-\ln 0.050) = \ln(2.99573) = 1.0972$$
Using the linearized equation:
$$n \ln t = \ln(-\ln(1 - X)) - n \ln k = 1.0972 - 2.234(-3.3795) = 1.0972 + 7.550 = 8.6472$$
$$\ln t = \frac{8.6472}{2.234} = 3.8707$$
$$t = e^{3.8707} \approx 47.98\text{ minutes}$$

Achieving $95.0\%$ crystallization requires **$48.0\text{ minutes}$** of isothermal heat treatment.""",
            "hints": ["Double natural logarithm linearizes JMAK: ln(-ln(1 - X)) vs ln(t).", "Slope gives Avrami exponent n."]
        },

        "unit-8-caustic-chlorine": {
            "id": "prob-8-8",
            "problemNumber": "8.8",
            "title": "Oxygen-Depolarized Cathode (ODC) Voltage & Energy Conservation",
            "difficulty": "Easy",
            "statement": r"""A chlor-alkali plant operates at an electrical current of $I = 100\text{ kA}$ ($100,000\text{ A}$) to produce $100\%\text{ pure NaOH}$ ($40.00\text{ g/mol}$) at $\eta = 96.0\%$ current efficiency ($F = 96,485\text{ C/mol}$).
1. In a conventional hydrogen-evolving membrane cell, the operational cell voltage is $U_1 = 3.050\text{ V}$.
2. In an advanced Oxygen-Depolarized Cathode (ODC) cell, pure oxygen gas is supplied to the cathode, reducing the operational cell voltage to $U_2 = 2.050\text{ V}$.
Industrial electricity costs $\$0.080\text{ per kWh}$.

1. Calculate the hourly direct-current electrical power consumption of a single cell under:
   - Conventional cell ($U_1 = 3.050\text{ V}$).
   - ODC cell ($U_2 = 2.050\text{ V}$).
2. Determine the specific direct-current energy consumption per metric ton of pure $\text{NaOH}$ for both technologies ($\text{kWh/t NaOH}$).
3. Calculate the percentage electrical energy savings and the annual electricity cost savings per cell (operating $8,400\text{ hours/year}$).""",
            "solution": r"""### Step 1: Hourly Electrical Power per Cell
Power is $P = U \times I$:
- **Conventional Cell**:
  $$P_1 = 3.050\text{ V} \times 100,000\text{ A} = 305,000\text{ W} = 305.0\text{ kW}$$
- **ODC Cell**:
  $$P_2 = 2.050\text{ V} \times 100,000\text{ A} = 205,000\text{ W} = 205.0\text{ kW}$$

### Step 2: Specific Energy Consumption per Metric Ton NaOH
Hourly NaOH production per cell ($M = 40.00\text{ g/mol}$):
$$\dot{n}_{\text{NaOH}} = \frac{100,000\text{ C/s} \times 3,600\text{ s/h} \times 0.960}{96,485\text{ C/mol}} = 3,582.0\text{ mol/h}$$
$$\dot{m}_{\text{NaOH}} = 3,582.0\text{ mol/h} \times 0.04000\text{ kg/mol} = 143.28\text{ kg/h} = 0.14328\text{ metric tons/h}$$

Specific energy consumption ($w_{\text{spec}} = P / \dot{m}$):
- **Conventional**:
  $$w_{\text{spec}, 1} = \frac{305.0\text{ kW}}{0.14328\text{ t/h}} = 2,128.7\text{ kWh/metric ton NaOH}$$
- **ODC Cell**:
  $$w_{\text{spec}, 2} = \frac{205.0\text{ kW}}{0.14328\text{ t/h}} = 1,430.8\text{ kWh/metric ton NaOH}$$

### Step 3: Savings Analysis
Percentage energy savings:
$$\% \text{ Savings} = \frac{3.050 - 2.050}{3.050} \times 100\% = \frac{1.000}{3.050} \times 100\% = 32.79\%$$
Annual electrical energy saved per cell ($8,400\text{ operating hours}$):
$$\Delta E = (305.0 - 205.0\text{ kW}) \times 8,400\text{ h} = 100.0\text{ kW} \times 8,400\text{ h} = 840,000\text{ kWh/year}$$
Annual financial savings per cell:
$$\text{Cost Savings} = 840,000\text{ kWh} \times \$0.080\text{/kWh} = \$67,200\text{/cell/year}$$

ODC technology slashes power consumption by **$32.8\%$**, saving **$\$67,200\text{ per cell annually}$**.""",
            "hints": ["Power is U * I in kW.", "Specific energy is Power divided by mass production rate."]
        },

        "unit-9-petroleum-and-fuels": {
            "id": "prob-9-8",
            "problemNumber": "9.8",
            "title": "Sustainable Aviation Fuel (SAF) HEFA Processing Yields & Hydrogen Duty",
            "difficulty": "Medium",
            "statement": r"""A bio-refinery converts Used Cooking Oil (UCO, pure triglyceride of oleic acid, triolein $\text{C}_{57}\text{H}_{104}\text{O}_6$, $M = 885.4\text{ g/mol}$) into Sustainable Aviation Fuel (SAF) via the HEFA process.
- Plant throughput: $\dot{m}_{\text{feed}} = 50.0\text{ metric tons/h}$ of triolein ($56.47\text{ kmol/h}$).
- Complete Hydrodeoxygenation (HDO) reaction:
  $$\text{C}_{57}\text{H}_{104}\text{O}_6 + 15\text{H}_2 \longrightarrow 3\text{C}_{18}\text{H}_{38} + \text{C}_3\text{H}_8 + 6\text{H}_2\text{O}$$
  Molar masses: $\text{H}_2 = 2.016$, $n\text{-octadecane C}_{18}\text{H}_{38} = 254.5\text{ g/mol}$, propane $\text{C}_3\text{H}_8 = 44.1\text{ g/mol}$, $\text{H}_2\text{O} = 18.02\text{ g/mol}$.
- In the subsequent hydroisomerization and cracking stage, $n$-octadecane yields:
  - $65.0\text{ wt}\%\text{ SAF (kerosene cut)}$
  - $20.0\text{ wt}\%\text{ renewable diesel}$
  - $15.0\text{ wt}\%\text{ renewable naphtha / LPG}$
  consuming an additional $0.50\text{ wt}\%\text{ H}_2$ on octadecane.

1. Calculate the mass of pure hydrogen consumed by the HDO stage per hour in $\text{kg/h}$.
2. Determine the hourly production rate of $n$-octadecane paraffin intermediate in metric tons per hour.
3. Calculate the hourly production rate of finished Sustainable Aviation Fuel (SAF) in metric tons per hour and the overall process mass yield on raw oil.""",
            "solution": r"""### Step 1: Hydrogen Consumed in HDO
Moles of triolein fed per hour:
$$\dot{n}_{\text{triolein}} = 56.471\text{ kmol/h}$$
Stoichiometric $\text{H}_2$ consumed ($15\text{ mol H}_2\text{ / mol triolein}$):
$$\dot{n}_{\text{H}_2, \text{HDO}} = 15 \times 56.471 = 847.065\text{ kmol/h}$$
Mass of $\text{H}_2$:
$$\dot{m}_{\text{H}_2, \text{HDO}} = 847.065\text{ kmol/h} \times 2.016\text{ kg/kmol} = 1,707.68\text{ kg/h} \approx 1.708\text{ metric tons/h}$$

### Step 2: Production of $n$-Octadecane
From stoichiometry, $1\text{ mol triolein} \to 3\text{ mol C}_{18}\text{H}_{38}$:
$$\dot{n}_{\text{octadecane}} = 3 \times 56.471 = 169.413\text{ kmol/h}$$
Mass of $n$-octadecane:
$$\dot{m}_{\text{octadecane}} = 169.413\text{ kmol/h} \times 254.5\text{ kg/kmol} = 43,115.6\text{ kg/h} \approx 43.116\text{ metric tons/h}$$
(Theoretical mass yield of paraffin intermediate $= 43.12 / 50.0 = 86.23\%$).

### Step 3: Finished SAF Production Rate
SAF yield from octadecane is $65.0\text{ wt}\%$:
$$\dot{m}_{\text{SAF}} = 0.650 \times 43.116\text{ metric tons/h} = 28.025\text{ metric tons/h}$$
Overall mass yield of SAF on raw cooking oil:
$$\% \text{ Yield}_{\text{SAF}} = \frac{28.025\text{ t/h}}{50.00\text{ t/h}} \times 100\% = 56.05\%$$

The plant consumes **$1.71\text{ t/h}$ of $\text{H}_2$** in HDO to yield **$28.0\text{ metric tons/h}$** of finished Sustainable Aviation Fuel ($56.1\text{ wt}\%$ overall yield).""",
            "hints": ["Each mole of triglyceride consumes 15 moles of H2 and yields 3 moles of octadecane.", "SAF is 65% of the produced octadecane mass."]
        },

        "unit-10-metallurgy-and-steel": {
            "id": "prob-10-8",
            "problemNumber": "10.8",
            "title": "100% Pure Hydrogen Direct Reduction (H2-DRI) Gas Consumption & Water Vapor Balance",
            "difficulty": "Medium",
            "statement": r"""A green steel plant operates an industrial shaft furnace utilizing $100\%$ electrolytic green hydrogen ($\text{H}_2$, $2.016\text{ g/mol}$) to reduce pure hematite pellets ($\text{Fe}_2\text{O}_3$, $159.69\text{ g/mol}$) to metallic sponge iron ($\text{Fe}$, $55.85\text{ g/mol}$).
The endothermic shaft reduction reaction is:
$$\text{Fe}_2\text{O}_3(s) + 3\text{H}_2(g) \longrightarrow 2\text{Fe}(s) + 3\text{H}_2\text{O}(g) \quad \Delta H_{298}^\circ = +98.8\text{ kJ/mol Fe}_2\text{O}_3$$
- The plant produces $\dot{m}_{\text{DRI}} = 100.0\text{ metric tons/h}$ of metallic iron ($1,790.5\text{ kmol/h Fe}$).
- In the shaft furnace, thermodynamic equilibrium and gas channeling limit single-pass hydrogen conversion to $\alpha_{\text{pass}} = 30.0\%$. Unreacted gas is cooled, condensed to remove water, reheated, and recycled.
- Latent heat of condensation of water is $\Delta H_{\text{vap}} = 2,260\text{ kJ/kg}$.

1. Calculate the stoichiometric consumption of pure hydrogen gas per hour in $\text{kg/h}$ and STP volumetric flow rate ($\text{Nm}^3\text{/h}$, $22.414\text{ Nm}^3\text{/kmol}$).
2. Determine the total circulating hydrogen gas feed rate entering the shaft tuyeres ($\text{Nm}^3\text{/h}$).
3. Calculate the hourly generation rate of water vapor in metric tons per hour and the heat released when this water is condensed from the recycle gas loop ($\text{MW}$).""",
            "solution": r"""### Step 1: Stoichiometric Hydrogen Consumption
Hourly iron production:
$$\dot{n}_{\text{Fe}} = \frac{100,000\text{ kg/h}}{55.85\text{ kg/kmol}} = 1,790.51\text{ kmol/h}$$
Stoichiometric $\text{H}_2$ required ($1.5\text{ mol H}_2\text{ / mol Fe}$):
$$\dot{n}_{\text{H}_2, \text{consumed}} = 1.5 \times 1,790.51 = 2,685.77\text{ kmol/h}$$
Mass of pure hydrogen consumed:
$$\dot{m}_{\text{H}_2} = 2,685.77\text{ kmol/h} \times 2.016\text{ kg/kmol} = 5,414.5\text{ kg/h} \approx 5.415\text{ metric tons/h}$$
Volumetric consumption at STP:
$$\dot{V}_{\text{H}_2, \text{STP}} = 2,685.77\text{ kmol/h} \times 22.414\text{ Nm}^3\text{/kmol} = 60,198.8\text{ Nm}^3\text{/h} \approx 60,200\text{ Nm}^3\text{/h}$$

### Step 2: Circulating Hydrogen Gas Flow
At $30.0\%$ single-pass conversion:
$$\dot{V}_{\text{H}_2, \text{circ}} = \frac{60,198.8\text{ Nm}^3\text{/h}}{0.300} = 200,662.7\text{ Nm}^3\text{/h} \approx 200,663\text{ Nm}^3\text{/h}$$

### Step 3: Water Vapor Generation & Condensation Enthalpy
From stoichiometry, moles of $\text{H}_2\text{O}$ vapor produced equals moles of $\text{H}_2$ consumed:
$$\dot{n}_{\text{H}_2\text{O}} = 2,685.77\text{ kmol/h}$$
Mass of water produced:
$$\dot{m}_{\text{H}_2\text{O}} = 2,685.77\text{ kmol/h} \times 18.015\text{ kg/kmol} = 48,384.1\text{ kg/h} \approx 48.38\text{ metric tons/h}$$
Latent condensation heat duty:
$$\dot{Q}_{\text{cond}} = 48,384.1\text{ kg/h} \times 2,260\text{ kJ/kg} = 1.0935 \times 10^8\text{ kJ/h}$$
In thermal megawatts ($\text{MW}$):
$$\dot{Q}_{\text{thermal}} = \frac{1.0935 \times 10^8\text{ kJ/h}}{3,600\text{ s/h}} = 30,374.5\text{ kW} \approx 30.37\text{ MW}$$

The furnace consumes **$5.42\text{ t/h}$ of $\text{H}_2$**, circulates **$200,663\text{ Nm}^3\text{/h}$ of gas**, and produces **$48.38\text{ t/h}$ of clean water**, releasing **$30.37\text{ MW}$** of recoverable condensation heat.""",
            "hints": ["Stoichiometric H2 is 1.5 moles per mole of metallic Fe.", "Circulating gas equals consumed gas divided by 0.30 pass conversion."]
        }
    }

    # Inject into each unit
    for u in units:
        uid = u["id"]
        if uid in prob8_dict:
            has_prob8 = any(p["id"] == prob8_dict[uid]["id"] for p in u["problems"])
            if not has_prob8:
                u["problems"].append(prob8_dict[uid])

    return units
