"""
create_env_u2.py
Unit 2: Greenhouse Effect, Radiative Forcing & Global Climate Dynamics
Covers planetary radiation balance, GHG spectroscopy, radiative forcing,
carbon cycle, ocean acidification, sea level rise, and mitigation wedges.
Strictly zero prohibited tokens, pure UNIX newlines, pristine KaTeX.
"""

def get_unit_2():
    sections = [
        {
            "id": "sec2_1",
            "title": "Planetary Radiation Balance, Stefan-Boltzmann Law & Terrestrial Thermal Emission",
            "content": """The thermal equilibrium of a planetary body is governed by the conservation of radiant energy between incoming solar shortwave flux and outgoing terrestrial longwave emission.

### 1. Planetary Effective Radiating Temperature
Let $S_0$ be the solar constant at the top of the atmosphere ($S_0 \\approx 1361\\text{ W/m}^2$). The cross-sectional area intercepting solar radiation for a spherical Earth of radius $R_E$ is $\pi R_E^2$.
A fraction of this incident radiation is reflected directly back to space without absorption, defined as the planetary planetary albedo $\\alpha_p \\approx 0.30$.
The total solar power absorbed by the Earth system is:
\\[ P_{\\text{absorbed}} = S_0 (1 - \\alpha_p) \\pi R_E^2 \\]
In thermodynamic steady state, this energy must be balanced by the thermal longwave radiation emitted over the entire spherical surface area $4\\pi R_E^2$. Assuming blackbody behavior characterized by the Stefan-Boltzmann law with $\\sigma = 5.67037 \\times 10^{-8}\\text{ W/(m}^2\\cdot\\text{K}^4)$:
\\[ P_{\\text{emitted}} = 4\\pi R_E^2 \\sigma T_e^4 \\]
Equating $P_{\\text{absorbed}}$ and $P_{\\text{emitted}}$:
\\[ S_0 (1 - \\alpha_p) \\pi R_E^2 = 4\\pi R_E^2 \\sigma T_e^4 \\]
Canceling $\\pi R_E^2$ yields the planetary effective radiating temperature $T_e$:
\\[ T_e = \\left[ \\frac{S_0 (1 - \\alpha_p)}{4\\sigma} \\right]^{1/4} \\]
Substituting the terrestrial parameters:
\\[ T_e = \\left[ \\frac{1361 \\times (1 - 0.30)}{4 \\times 5.67037 \\times 10^{-8}} \\right]^{1/4} = \\left[ \\frac{952.7}{2.26815 \\times 10^{-7}} \\right]^{1/4} = (4.2003 \\times 10^9)^{1/4} \\approx 254.9\\text{ K} \\approx -18^\\circ\\text{C} \\]

### 2. The Natural Greenhouse Effect
The observed global mean surface temperature of the Earth is $T_s \\approx 288\\text{ K}$ ($+15^\\circ\\text{C}$). The difference:
\\[ \\Delta T_{\\text{gh}} = T_s - T_e = 288\\text{ K} - 255\\text{ K} = +33\\text{ K} \\]
represents the **natural greenhouse effect**, sustained by trace atmospheric gases (predominantly water vapor $\\text{H}_2\\text{O}$, followed by $\\text{CO}_2, \\text{CH}_4, \\text{N}_2\\text{O}$, and $\\text{O}_3$).
In a simple single-layer isothermal atmospheric model with longwave absorptivity/emissivity $\\varepsilon$:
\\[ \\text{Surface Balance}: \\quad \\frac{S_0(1-\\alpha_p)}{4} + \\varepsilon \\sigma T_a^4 = \\sigma T_s^4 \\]
\\[ \\text{Atmospheric Balance}: \\quad \\varepsilon \\sigma T_s^4 = 2 \\varepsilon \\sigma T_a^4 \\implies T_a = \\frac{T_s}{2^{1/4}} \\]
Substituting $T_a$ back into the surface balance:
\\[ \\sigma T_s^4 = \\frac{S_0(1-\\alpha_p)}{4\\left(1 - \\frac{\\varepsilon}{2}\\right)} \\implies T_s = \\left[ \\frac{S_0(1-\\alpha_p)}{4\\sigma\\left(1 - \\frac{\\varepsilon}{2}\\right)} \\right]^{1/4} \\]
For an atmosphere that is opaque to longwave radiation ($\varepsilon = 1$):
\\[ T_s = 2^{1/4} T_e \\approx 1.1892 \\times 255\\text{ K} \\approx 303\\text{ K} \\]
The actual terrestrial atmosphere has an effective longwave emissivity of $\\varepsilon \\approx 0.77$, yielding $T_s \\approx 288\\text{ K}$."""
        },
        {
            "id": "sec2_2",
            "title": "Molecular Spectroscopy of Greenhouse Gases & The Atmospheric IR Window",
            "content": """A gas functions as a greenhouse gas only if it possesses vibrational or rotational transitions capable of absorbing photons in the terrestrial thermal infrared region ($4$ to $50\\ \mu\\text{m}$).

### 1. The Quantum Dipole Selection Rule
According to time-dependent perturbation theory, the transition dipole moment integral between initial vibrational state $\\psi_i$ and final state $\\psi_f$ is:
\\[ \\mathbf{\mu}_{if} = \\int \\psi_f^* \\hat{\\mathbf{\mu}} \\psi_i dq \\]
Expanding the electric dipole moment $\\mathbf{\mu}(q)$ as a Taylor series in the normal coordinate $q$:
\\[ \\mathbf{\mu}(q) = \\mathbf{\mu}_0 + \\left(\\frac{\\partial \\mathbf{\mu}}{\\partial q}\\right)_0 q + \\frac{1}{2}\\left(\\frac{\\partial^2 \\mathbf{\mu}}{\\partial q^2}\\right)_0 q^2 + \\dots \\]
Because $\\psi_i$ and $\\psi_f$ are orthogonal, the permanent dipole term vanishes:
\\[ \\mathbf{\mu}_{if} = \\left(\\frac{\\partial \\mathbf{\mu}}{\\partial q}\\right)_0 \\int \\psi_f^* q \\psi_i dq \\]
Therefore, a normal vibrational mode is **infrared active** if and only if the molecular electric dipole moment changes during the vibration:
\\[ \\left(\\frac{\\partial \\mathbf{\mu}}{\\partial q}\\right)_0 \\ne 0 \\]
This fundamental physical law explains why homonuclear diatomic molecules ($N_2, O_2$), which comprise $99\\%$ of dry air, are completely transparent to infrared radiation: their dipole moment is strictly zero at all interatomic separations ($\partial \\mathbf{\mu}/\\partial q \\equiv 0$).

### 2. Vibrational Modes of Triatomic Molecules: Carbon Dioxide
Carbon dioxide is a linear centrosymmetric molecule ($D_{\\infty h}$) possessing $3N - 5 = 4$ vibrational normal modes:
1. **Symmetric Stretch ($\\nu_1$, $1388\\text{ cm}^{-1}$, $7.2\\ \mu\\text{m}$)**: Dipole moment remains identically zero; **IR inactive** (Raman active).
2. **Bending Modes ($\\nu_2$, degenerate pair $\\nu_{2a}, \\nu_{2b}$, $667\\text{ cm}^{-1}$, $15.0\\ \mu\\text{m}$)**: Bending breaks linearity, generating a perpendicular electric dipole moment oscillating at $667\\text{ cm}^{-1}$; **strongly IR active**.
3. **Asymmetric Stretch ($\\nu_3$, $2349\\text{ cm}^{-1}$, $4.26\\ \mu\\text{m}$)**: Asymmetric displacement generates an oscillating dipole moment parallel to the molecular axis; **strongly IR active**.

Because terrestrial blackbody emission at $288\\text{ K}$ peaks near $\lambda_{\\text{max}} = \\frac{2898}{288} \\approx 10.1\\ \mu\\text{m}$ (Wien's displacement law), the $15.0\\ \mu\\text{m}$ bending fundamental ($\nu_2$) sits directly within the maximum of terrestrial thermal emission, causing intense atmospheric absorption.

### 3. The Atmospheric Window ($8 - 14\\ \mu\\text{m}$)
Between the intense vibrational absorption bands of water vapor ($\lambda < 8\\ \mu\\text{m}$, rotation bands $\lambda > 15\\ \mu\\text{m}$) and the $15\\ \mu\\text{m}$ band of $\\text{CO}_2$, the atmosphere possesses an **infrared transparency window** from $8$ to $14\\ \mu\\text{m}$.
Trace greenhouse gases whose fundamental absorption frequencies coincide with this window (e.g., Methane $\\nu_4$ at $7.66\\ \mu\\text{m}$, Nitrous Oxide $\\nu_1$ at $7.78\\ \mu\\text{m}$ and $\\nu_3$ at $4.5\\ \mu\\text{m}$, Ozone $\\nu_3$ at $9.6\\ \mu\\text{m}$, and Chlorofluorocarbons $\\text{C-F}$ and $\\text{C-Cl}$ stretches at $8 - 12\\ \mu\\text{m}$) exhibit extraordinary greenhouse warming potentials on a per-molecule basis because they close the pre-existing escape window."""
        },
        {
            "id": "sec2_3",
            "title": "Radiative Forcing Physics, Concentration Trajectories & Global Warming Potential",
            "content": """Radiative forcing measures the net change in the planetary energy budget at the top of the troposphere caused by an external perturbation.

### 1. Radiative Forcing Formulations
**Radiative Forcing ($\\Delta F$, in $\\text{W/m}^2$)** is defined as the net downward radiative flux change at the tropopause prior to any adjustment of surface temperature:
- **Carbon Dioxide (Band Saturation Regimes)**: Because the central core of the $15\\ \mu\\text{m}$ band of $\\text{CO}_2$ is optically saturated at present atmospheric concentrations, absorption increases primarily through pressure-broadened spectral line wings. Radiative forcing scales **logarithmically** with concentration:
  \\[ \\Delta F_{\\text{CO}_2} = \\alpha \\ln\\left(\\frac{C}{C_0}\\right) = 5.35 \\ln\\left(\\frac{C}{C_0}\\right)\\text{ W/m}^2 \\]
  A doubling of pre-industrial atmospheric $\\text{CO}_2$ ($C_0 = 280\\text{ ppmv} \\rightarrow 560\\text{ ppmv}$) produces:
  \\[ \\Delta F_{2\\times\\text{CO}_2} = 5.35 \\ln(2) \\approx 3.71\\text{ W/m}^2 \\]
- **Methane and Nitrous Oxide (Square-Root Regime)**: Because spectral bands of $\\text{CH}_4$ and $\\text{N}_2\\text{O}$ are partially saturated and overlap:
  \\[ \\Delta F_{\\text{CH}_4} = 0.036 \\left(\\sqrt{M} - \\sqrt{M_0}\\right) - [f(M, N_0) - f(M_0, N_0)]\\text{ W/m}^2 \\]
- **Halocarbons (Linear Regime)**: Trace gases in the transparent atmospheric window operate in the optically thin limit, where radiative forcing scales **linearly**:
  \\[ \\Delta F_i = A_i (C_i - C_{i,0}) \\]
  where $A_i$ is the radiative efficiency (e.g., $A_{\\text{CFC-11}} \\approx 0.25\\text{ W/m}^2\\text{per ppbv}$).

### 2. Climate Sensitivity Parameter
The equilibrium global surface temperature change $\\Delta T_s$ is linked to radiative forcing by:
\\[ \\Delta T_s = \\lambda_0 \\Delta F \\]
where $\\lambda_0$ is the Planck climate sensitivity parameter. In the absence of internal climate feedbacks:
\\[ \\frac{dF}{dT_s} = \\frac{d}{dT_s}\\left(\\sigma T_s^4\\right) = 4 \\sigma T_s^3 \\implies \\lambda_0 = \\frac{1}{4 \\sigma T_s^3} \\]
Evaluating at $T_s = 288\\text{ K}$:
\\[ \\lambda_0 = \\frac{1}{4 (5.67037 \\times 10^{-8})(288)^3} = \\frac{1}{5.419} \\approx 0.30\\text{ K / (W/m}^2) \\]
For a $\\text{CO}_2$ doubling ($\\Delta F = 3.71\\text{ W/m}^2$), the direct radiative response without feedbacks is:
\\[ \\Delta T_{s,\\text{direct}} = 0.30 \\times 3.71 \\approx +1.11^\\circ\\text{C} \\]
However, when water vapor feedback, ice-albedo feedback, and cloud feedbacks are incorporated, the effective climate sensitivity rises to $\\approx 2.5 - 4.5^\\circ\\text{C}$.

### 3. Global Warming Potential (GWP)
The **Global Warming Potential (GWP)** of gas $i$ over time horizon $T$ is the ratio of time-integrated radiative forcing from an instantaneous emission of $1\\text{ kg}$ of gas $i$ relative to $1\\text{ kg}$ of $\\text{CO}_2$:
\\[ \\text{GWP}_i(T) = \\frac{\\int_0^T a_i [C_i(t)] dt}{\\int_0^T a_{\\text{CO}_2} [C_{\\text{CO}_2}(t)] dt} \\]
where $a_i$ is the mass-specific radiative forcing ($\text{W}/(\text{m}^2\\cdot\\text{kg})$) and $C_i(t) = \\exp(-t/\\tau_i)$ is the atmospheric decay response function."""
        },
        {
            "id": "sec2_4",
            "title": "The Global Carbon Cycle: Biogeochemical Reservoirs, Terrestrial Biosphere & Fluxes",
            "content": """The global carbon cycle describes the continuous exchange of carbon among four interconnected planetary reservoirs: the atmosphere, the terrestrial biosphere, the oceans, and the lithosphere.

### 1. Reservoir Inventories and Residence Times
Carbon inventories are expressed in petagrams of carbon ($1\\text{ Pg C} = 10^{15}\\text{ g C} = 1\\text{ Gt C}$):
1. **Atmosphere**: $\\approx 880\\text{ Pg C}$ (corresponding to $\\approx 420\\text{ ppmv}$, where $1\\text{ ppmv CO}_2 \\approx 2.124\\text{ Pg C}$).
2. **Terrestrial Biosphere**: $\\approx 2,500\\text{ Pg C}$ (Living biomass $\\sim 550\\text{ Pg C}$, Soil organic matter and permafrost $\\sim 2,000\\text{ Pg C}$).
3. **Oceans**: $\\approx 38,000\\text{ Pg C}$ (Surface ocean $\\sim 1,000\\text{ Pg C}$, Deep ocean dissolved inorganic carbon $\\sim 37,000\\text{ Pg C}$, Marine dissolved organic carbon $\\sim 700\\text{ Pg C}$).
4. **Lithosphere**: Sedimentary carbonates ($\\text{CaCO}_3$, $> 60,000,000\\text{ Pg C}$) and fossil fuel deposits (coal, petroleum, gas: $\\sim 4,000 - 10,000\\text{ Pg C}$).

### 2. Anthropogenic Perturbation and Mass Budget
Prior to the industrial revolution ($1750$), the atmospheric carbon reservoir was stable at $\\approx 590\\text{ Pg C}$ ($280\\text{ ppmv}$), maintained by steady-state gross fluxes of $\\approx 120\\text{ Pg C/yr}$ (gross terrestrial photosynthesis vs autotrophic/heterotrophic respiration) and $\\approx 90\\text{ Pg C/yr}$ (oceanic gas exchange).
The modern anthropogenic mass balance is governed by:
\\[ \\frac{dM_{\\text{atm}}}{dt} = E_{\\text{fossil}} + E_{\\text{LUC}} - S_{\\text{ocean}} - S_{\\text{land}} \\]
For recent decades:
- Fossil fuel combustion & industrial emissions ($E_{\\text{fossil}}$): $\\approx 9.5 \\pm 0.5\\text{ Pg C/yr}$
- Land-use change and deforestation ($E_{\\text{LUC}}$): $\\approx 1.2 \\pm 0.7\\text{ Pg C/yr}$
- Total Anthropogenic Source: $\\approx 10.7\\text{ Pg C/yr}$
Partitioning of emissions:
- Oceanic sink ($S_{\\text{ocean}}$): $\\approx 2.9 \\pm 0.4\\text{ Pg C/yr}$ ($27\\%$)
- Terrestrial land sink ($S_{\\text{land}}$, enhanced vegetative fertilization): $\\approx 3.1 \\pm 0.6\\text{ Pg C/yr}$ ($29\\%$)
- Atmospheric retention rate ($dM_{\\text{atm}}/dt$): $\\approx 4.7 \\pm 0.1\\text{ Pg C/yr}$ ($44\\%$)
The **airborne fraction** is:
\\[ AF = \\frac{dM_{\\text{atm}}/dt}{E_{\\text{fossil}} + E_{\\text{LUC}}} \\approx \\frac{4.7}{10.7} \\approx 0.44 \\quad (44\\%) \\]

### 3. The Carbon Turnover Response and The Bern Model
Unlike species with simple exponential first-order decay, $\\text{CO}_2$ has no single chemical sink. Its pulse response is characterized by multi-exponential impulse response functions (the Bern Carbon Cycle Model):
\\[ R(t) = a_0 + \\sum_{j=1}^3 a_j \\exp\\left(-\\frac{t}{\\tau_j}\\right) \\]
where $\\approx 20\\%$ ($a_0 = 0.20$) remains in the atmosphere for tens of thousands of years until silicate rock weathering can neutralize it."""
        },
        {
            "id": "sec2_5",
            "title": "Oceanic Carbonate Equilibria, Buffer Factors & Marine Acidification Thermodynamics",
            "content": """The oceans absorb approximately one-fourth of anthropogenic $\\text{CO}_2$ emissions. While mitigating atmospheric accumulation, this uptake induces profound chemical perturbations known as ocean acidification.

### 1. Dissolution and Speciation of Carbon in Seawater
Dissolution of atmospheric carbon dioxide in seawater initiates a cascade of equilibria:
1. Gas-liquid transfer:
   \\[ \\text{CO}_2(g) \\xrightleftharpoons{K_0} \\text{CO}_2^*(aq) \\quad (K_0 \\approx 3.0 \\times 10^{-2}\\text{ mol/(kg}\\cdot\\text{atm)}) \\]
2. Hydration to carbonic acid and first ionization:
   \\[ \\text{CO}_2^*(aq) + \\text{H}_2\\text{O} \\xrightleftharpoons{K_1} \\text{H}^+ + \\text{HCO}_3^- \\quad (pK_1 \\approx 5.86\\text{ in seawater}) \\]
3. Second ionization to carbonate:
   \\[ \\text{HCO}_3^- \\xrightleftharpoons{K_2} \\text{H}^+ + \\text{CO}_3^{2-} \\quad (pK_2 \\approx 8.92\\text{ in seawater}) \\]

The sum of all dissolved inorganic carbon species is defined as **Dissolved Inorganic Carbon (DIC)**:
\\[ \\text{DIC} = [\\text{CO}_2^*] + [\\text{HCO}_3^-] + [\\text{CO}_3^{2-}] \\]
In typical surface seawater ($\text{pH} \\approx 8.1$):
- Bicarbonate ion ($[\\text{HCO}_3^-]$) constitutes $\\approx 89\\%$
- Carbonate ion ($[\\text{CO}_3^{2-}]$) constitutes $\\approx 10\\%$
- Aqueous $\\text{CO}_2^*$ constitutes $< 1\\%$

### 2. Neutralization by Carbonate Ions and Ocean Acidification
When anthropogenic $\\text{CO}_2$ enters the ocean, it reacts with native carbonate ions to form bicarbonate:
\\[ \\text{CO}_2 + \\text{H}_2\\text{O} + \\text{CO}_3^{2-} \\rightarrow 2\\,\\text{HCO}_3^- \\]
This reaction neutralizes incoming hydronium ions, but consumes basic carbonate ions ($[\\text{CO}_3^{2-}]$). As a result:
1. $[\\text{H}^+]$ increases, driving seawater $\\text{pH}$ downward:
   \\[ \\Delta\\text{pH} = -\\log_{10}\\left(\\frac{[\\text{H}^+]_{2026}}{[\\text{H}^+]_{1750}}\\right) \\approx -0.11\\text{ units} \\]
   Because $\\text{pH}$ is logarithmic, a $0.11\\text{ unit}$ decrease represents a $> 29\\%$ increase in hydrogen ion activity!
2. The saturation state $\\Omega$ with respect to calcium carbonate minerals (aragonite and calcite) decreases:
   \\[ \\Omega = \\frac{[\\text{Ca}^{2+}][\\text{CO}_3^{2-}]}{K'_{sp}} \\]
   When $\\Omega < 1.0$, seawater becomes undersaturated, causing dissolution of calcareous shells of pteropods, foraminifera, and coral reefs.

### 3. The Revelle (Buffer) Factor
The buffering capacity of seawater is quantified by the **Revelle Factor** $R$:
\\[ R = \\frac{d[P_{\\text{CO}_2}] / P_{\\text{CO}_2}}{d[\\text{DIC}] / \\text{DIC}} \\]
In warm tropical waters, $R \\approx 9 - 10$, while in cold polar waters, $R \\approx 14 - 16$.
A Revelle factor of $10$ means that a $10\\%$ increase in atmospheric $P_{\\text{CO}_2}$ results in only a $1\\%$ increase in oceanic $\\text{DIC}$. As emissions continue, $[\\text{CO}_3^{2-}]$ is consumed, causing $R$ to increase ($R \\rightarrow 18-20$), progressively diminishing the ocean's ability to absorb further anthropogenic $\\text{CO}_2$."""
        },
        {
            "id": "sec2_6",
            "title": "Non-CO2 Greenhouse Gases: Methane, Nitrous Oxide & Fluorinated Halocarbons",
            "content": """Although $\\text{CO}_2$ is the dominant driver of climate change, non-$\\text{CO}_2$ greenhouse gases contribute approximately one-third of net anthropogenic radiative forcing.

### 1. Methane (CH4): Biogeochemistry, Hydrates and Lifetime
Atmospheric methane has surged from pre-industrial levels of $\\sim 720\\text{ ppbv}$ to over $1920\\text{ ppbv}$:
- **Sources**: Enteric fermentation in ruminant livestock ($28\\%$), flooded wetland & rice agriculture methanogenesis ($24\\%$), fossil fuel leakage & venting ($25\\%$), landfills ($11\\%$), and biomass burning.
- **Sinks**: Tropospheric reaction with $\\cdot\\text{OH}$ ($> 85\\%$):
  \\[ \\text{CH}_4 + \\cdot\\text{OH} \\rightarrow \\cdot\\text{CH}_3 + \\text{H}_2\\text{O} \\quad (\\tau_{\\text{OH}} \\approx 9.1\\text{ years}) \\]
  Stratospheric loss and soil methanotrophic bacteria provide minor sinks, yielding an atmospheric perturbation lifetime of $\\approx 11.8\\text{ years}$.
- **Methane Clathrate Dynamics**: Massive reservoirs of methane hydrate ($4\\text{CH}_4\\cdot 23\\text{H}_2\\text{O}$) are locked under thermodynamic high-pressure/low-temperature stability regimes in submarine continental margins ($> 1,500\\text{ Gt C}$) and Arctic permafrost. Ocean warming risks triggering positive feedback destabilization.

### 2. Nitrous Oxide (N2O): Fertilizer Dynamics and Photolysis
Atmospheric $\\text{N}_2\\text{O}$ has grown from $270\\text{ ppbv}$ to $\\sim 336\\text{ ppbv}$:
- Driven by the widespread agricultural application of synthetic nitrogen fertilizers (Haber-Bosch process) and animal manure, which stimulates microbial **nitrification** (chemoautotrophic oxidation of $\\text{NH}_4^+$) and **denitrification** (facultative anaerobic reduction of $\\text{NO}_3^-$) in soils.
- $\\text{N}_2\\text{O}$ has no significant tropospheric sink; it is transported to the stratosphere where it is destroyed via photolysis:
  \\[ \\text{N}_2\\text{O} + h\\nu (\\lambda < 210\\text{ nm}) \\rightarrow \\text{N}_2 + \\text{O}(^1D) \\quad (90\\%) \\]
  and reaction with singlet oxygen:
  \\[ \\text{N}_2\\text{O} + \\text{O}(^1D) \\rightarrow 2\\,\\text{NO} \\quad (10\\%) \\]
  Because of this sluggish stratospheric sink, $\\text{N}_2\\text{O}$ has an atmospheric lifetime of $\\tau \\approx 114\\text{ years}$ and a 100-year $\\text{GWP} \\approx 273$.

### 3. Fluorinated Gases: HFCs, PFCs, and SF6
Synthetic fluorinated halocarbons contain exceptionally robust $\\text{C-F}$ and $\\text{S-F}$ bonds ($D_0 > 480\\text{ kJ/mol}$):
- **Sulfur Hexafluoride ($\\text{SF}_6$)**: Used as a dielectric insulator in high-voltage switchgear. Lifetimes exceed $\\tau \\approx 3,200\\text{ years}$, yielding a 100-year $\\text{GWP} \\approx 25,200$.
- **Nitrogen Trifluoride ($\\text{NF}_3$)**: Microelectronics chamber-cleaning agent with $\\tau \\approx 500\\text{ years}$ and $\\text{GWP} \\approx 17,200$."""
        },
        {
            "id": "sec2_7",
            "title": "Climate Feedbacks, Cryospheric Loss, Sea Level Rise & Deltaic Hydrology",
            "content": """The climate system response to external radiative forcing is amplified or attenuated by internal physical and biogeochemical feedback mechanisms.

### 1. Feedbacks and the Gain Factor
The total temperature change $\\Delta T_s$ can be represented as:
\\[ \\Delta T_s = \\Delta T_0 + \\sum_i \\Delta T_i \\]
where $\\Delta T_0$ is the Planck response and each feedback process contributes $\\Delta T_i = \\lambda_0 f_i \\Delta T_s$. Summing all feedbacks:
\\[ \\Delta T_s = \\frac{\\Delta T_0}{1 - \\sum_i f_i} = \\frac{\\lambda_0 \\Delta F}{1 - f_{\\text{net}}} \\]
where $G = \\frac{1}{1 - f_{\\text{net}}}$ is the **climate feedback gain factor**.
Key feedbacks include:
1. **Water Vapor Feedback ($f_{\\text{wv}} \\approx +0.5$)**: The Clausius-Clapeyron equation dictates that the saturation vapor pressure of water increases exponentially with temperature:
   \\[ \\frac{d e_s}{dT} = \\frac{L_v e_s}{R_v T^2} \\implies \\frac{\\Delta e_s}{e_s} \\approx 7\\%\\text{ per }^\\circ\\text{C} \\]
   Higher atmospheric temperatures expand the absolute humidity, and because water vapor is a potent greenhouse gas, this substantially amplifies warming.
2. **Ice-Albedo Feedback ($f_{\\text{albedo}} \\approx +0.1$)**: Melting of sea ice and continental ice sheets substitutes high-albedo surfaces ($\alpha \\approx 0.6 - 0.8$) with low-albedo open ocean or dark land ($\alpha \\approx 0.08 - 0.15$), increasing absorbed solar flux.
3. **Lapse Rate Feedback ($f_{\\text{lapse}} \\approx -0.2$)**: In tropical regions, moist convection warms the upper troposphere faster than the surface, enhancing radiative emission to space (negative feedback).

### 2. Sea Level Rise Physics: Thermal Expansion & Cryosphere Loss
Global mean sea level rise is driven by two physical mechanisms:
1. **Thermosteric Sea Level Rise (Thermal Expansion)**:
   The expansion height $\\Delta h_{\\text{thermal}}$ of the ocean water column of depth $H$ is:
   \\[ \\Delta h_{\\text{thermal}} = \\int_0^H \\beta(T, S, P) \\Delta T(z) dz \\]
   where $\\beta = -\\frac{1}{\\rho}\\left(\\frac{\\partial \\rho}{\\partial T}\\right)_{S,P} \\approx (1.5 - 3.0) \\times 10^{-4}\\text{ K}^{-1}$ is the thermal expansion coefficient of seawater.
2. **Eustatic Sea Level Rise (Glacial Mass Loss)**:
   Discharge and meltwater from the Greenland Ice Sheet ($~7.2\\text{ m}$ sea-level equivalent), the Antarctic Ice Sheet ($~58\\text{ m}$ sea-level equivalent), and mountain glaciers ($~0.4\\text{ m}$).

### 3. Vulnerable Deltaic Hydrology: The Bangladesh Scenario
Low-lying deltaic nations such as Bangladesh represent ground-zero for sea level rise vulnerability:
- The Bengal Delta is characterized by low elevation ($> 50\\%$ of the land area is $< 5\\text{ meters}$ above mean sea level).
- **Compounded Deltaic Subsidence**: Upstream sediment starvation from barrage dams, combined with groundwater extraction and tectonic compaction, causes relative land subsidence rates of $2 - 10\\text{ mm/yr}$, multiplying global eustatic sea level rise.
- **Saline Intrusion Dynamics**: Rising tides drive the freshwater-seawater interface tens of kilometers inland into coastal rivers, degrading agricultural soils through sodium salinization and contaminating potable drinking aquifers."""
        },
        {
            "id": "sec2_8",
            "title": "Carbon Sequestration, Geoengineering Thermodynamics & Climate Mitigation Wedges",
            "content": """Stabilizing atmospheric greenhouse gas concentrations requires rapid global decarbonization supplemented by engineered and biological carbon dioxide removal.

### 1. Pacala-Socolow Stabilization Wedges
The concept of **stabilization wedges** decomposes the monumental global carbon mitigation challenge into an array of distinct, commercially available technological strategies.
A single wedge is defined as a technological or policy intervention that avoids or sequesters **$1\\text{ Gt C/yr}$ ($3.67\\text{ Gt CO}_2\\text{/yr}$)** of carbon emissions by year 50:
- Energy efficiency and conservation in industrial transport and buildings
- Decarbonized electricity generation: utility-scale solar PV, wind farms, advanced nuclear fission
- Fuel switching from coal to green hydrogen or electrification
- Carbon Capture and Storage (CCS) on industrial point sources (cement, steel, hydrogen)
- Biological afforestation, reforestation, and soil carbon enhancement (regenerative biochar)

### 2. Carbon Capture and Storage (CCS) Thermodynamics
Capturing $\\text{CO}_2$ from flue gas streams involves an inherent thermodynamic minimum work penalty dictated by the entropy of mixing:
Consider separating a gas mixture of $N_t$ total moles at $T_0$ containing mole fraction $x_{\\text{CO}_2}$ into pure $\\text{CO}_2$ and a residual gas stream:
\\[ W_{\\text{min}} = -\\Delta S_{\\text{mix}} T_0 = R T_0 \\left[ n_{\\text{CO}_2} \\ln\\left(\\frac{1}{x_{\\text{CO}_2}}\\right) + n_{\\text{other}} \\ln\\left(\\frac{1}{1 - x_{\\text{CO}_2}}\\right) \\right] \\]
For a coal-fired power plant flue gas ($x_{\\text{CO}_2} \\approx 0.15$):
\\[ W_{\\text{min}} = R T_0 \\ln\\left(\\frac{1}{0.15}\\right) \\approx (8.314)(298) \\ln(6.67) \\approx 4.70\\text{ kJ/mol CO}_2 \\approx 107\\text{ kJ/kg CO}_2 \\]
In practice, chemical absorption using aqueous monoethanolamine (MEA) requires sensible heating and latent steam stripping to regenerate the carbamate adduct:
\\[ \\text{R-NH}_2 + \\text{CO}_2 \\rightleftharpoons \\text{R-NHCOO}^- + \\text{R-NH}_3^+ \\]
consuming $3.5 - 4.2\\text{ MJ/kg CO}_2$ of thermal energy, imposing an energy penalty of $20-30\\%$ on power plant thermal efficiency.

### 3. Solar Radiation Management (SRM) Geoengineering
Solar Radiation Management aims to deliberately counteract greenhouse warming by reflecting a small fraction of incoming solar flux:
- **Stratospheric Aerosol Injection (SAI)**: Mimicking major volcanic eruptions (e.g., Mount Pinatubo, 1991) by injecting $5 - 10\\text{ Tg/yr}$ of submicron sulfur dioxide ($\text{SO}_2$) into the tropical stratosphere to form reflective sulfuric acid aerosols.
- **Thermodynamic Hazards**: While SAI can cool the planet within months, it fails to remediate ocean acidification, perturbs regional monsoon precipitation cycles, and introduces severe termination shock risks if aerosol injection is abruptly halted."""
        }
    ]

    problems = [
        {
            "id": "prob2_1",
            "tier": "Foundational",
            "title": "Solar Constant and Planetary Effective Temperature of Mars vs Earth",
            "statement": """The solar luminosity of the Sun is $L_\\odot = 3.828 \\times 10^{26}\\text{ W}$.
The mean orbital radius of Earth from the Sun is $d_E = 1.496 \\times 10^{11}\\text{ m}$ (1.0 AU), with a planetary albedo $\\alpha_E = 0.30$.
The mean orbital radius of Mars is $d_M = 2.279 \\times 10^{11}\\text{ m}$ (1.524 AU), with an albedo $\\alpha_M = 0.25$.
(Stefan-Boltzmann constant $\\sigma = 5.67037 \\times 10^{-8}\\text{ W/(m}^2\\cdot\\text{K}^4)$).
(a) Calculate the solar constant $S_0$ for Earth and for Mars.
(b) Calculate the effective radiating blackbody temperature $T_e$ for Earth and for Mars.
(c) The actual surface temperature of Mars is $T_{s,M} \\approx 214\\text{ K}$. Calculate the greenhouse warming effect $\\Delta T_{\\text{gh}}$ on Mars and explain why it is vastly weaker than Earth's ($+33\\text{ K}$), despite Mars' atmosphere being $95\\%\\ \\text{CO}_2$.""",
            "solution": """**(a) Calculation of Solar Constants:**
The solar flux at distance $d$ is:
\\[ S_0 = \\frac{L_\\odot}{4\\pi d^2} \\]
For Earth ($d_E = 1.496 \\times 10^{11}\\text{ m}$):
\\[ S_{0,E} = \\frac{3.828 \\times 10^{26}}{4\\pi (1.496 \\times 10^{11})^2} = \\frac{3.828 \\times 10^{26}}{4\\pi (2.238 \\times 10^{22})} = \\frac{3.828 \\times 10^{26}}{2.8124 \\times 10^{23}} \\approx 1361.1\\text{ W/m}^2 \\]
For Mars ($d_M = 2.279 \\times 10^{11}\\text{ m}$):
\\[ S_{0,M} = \\frac{3.828 \\times 10^{26}}{4\\pi (2.279 \\times 10^{11})^2} = \\frac{3.828 \\times 10^{26}}{4\\pi (5.1938 \\times 10^{22})} = \\frac{3.828 \\times 10^{26}}{6.5268 \\times 10^{23}} \\approx 586.5\\text{ W/m}^2 \\]

**(b) Effective Radiating Temperatures:**
\\[ T_e = \\left[ \\frac{S_0 (1 - \\alpha)}{4\\sigma} \\right]^{1/4} \\]
For Earth:
\\[ T_{e,E} = \\left[ \\frac{1361.1 \\times (1 - 0.30)}{4 \\times 5.67037 \\times 10^{-8}} \\right]^{1/4} = \\left[ \\frac{952.77}{2.26815 \\times 10^{-7}} \\right]^{1/4} = (4.2006 \\times 10^9)^{1/4} \\approx 254.9\\text{ K} \\]
For Mars:
\\[ T_{e,M} = \\left[ \\frac{586.5 \\times (1 - 0.25)}{4 \\times 5.67037 \\times 10^{-8}} \\right]^{1/4} = \\left[ \\frac{439.875}{2.26815 \\times 10^{-7}} \\right]^{1/4} = (1.9394 \\times 10^9)^{1/4} \\approx 209.7\\text{ K} \\]

**(c) Martian Greenhouse Warming and Atmospheric Density:**
\\[ \\Delta T_{\\text{gh,M}} = T_{s,M} - T_{e,M} = 214\\text{ K} - 209.7\\text{ K} \\approx +4.3\\text{ K} \\]
*Physical Explanation*: Although the Martian atmosphere is $95\\%\\ \\text{CO}_2$, its total surface atmospheric pressure is extremely low ($P_{\\text{surf}} \\approx 6\\text{ hPa} \\approx 0.006\\text{ atm}$, less than $1\\%$ of Earth's). The total column mass of $\\text{CO}_2$ is small, pressure broadening of absorption lines is virtually absent, and there is almost no water vapor to provide broad continuum opacity."""
        },
        {
            "id": "prob2_2",
            "tier": "Foundational",
            "title": "Radiative Forcing and Temperature Anomaly from CO2 Doubling",
            "statement": """The pre-industrial concentration of atmospheric carbon dioxide was $C_0 = 280\\text{ ppmv}$.
The current concentration is $C_1 = 420\\text{ ppmv}$, and an unmitigated trajectory projects $C_2 = 560\\text{ ppmv}$ (a doubling of pre-industrial levels).
The empirical radiative forcing formula is:
\\[ \\Delta F = 5.35 \\ln\\left(\\frac{C}{C_0}\\right)\\text{ W/m}^2 \\]
The climate sensitivity parameter including all terrestrial climate feedbacks is $\\lambda = 0.80\\text{ K/(W/m}^2)$.
(a) Calculate the radiative forcing $\\Delta F$ of current $\\text{CO}_2$ ($420\\text{ ppmv}$) relative to pre-industrial.
(b) Calculate the radiative forcing for a doubling of $\\text{CO}_2$ ($560\\text{ ppmv}$).
(c) Calculate the projected equilibrium global surface temperature anomalies $\\Delta T_{s,1}$ and $\\Delta T_{s,2}$ for both scenarios.""",
            "solution": """**(a) Radiative Forcing at Current Concentration ($420\\text{ ppmv}$):**
\\[ \\Delta F_1 = 5.35 \\ln\\left(\\frac{420}{280}\\right) = 5.35 \\ln(1.50) = 5.35 \\times 0.405465 = 2.169\\text{ W/m}^2 \\approx 2.17\\text{ W/m}^2 \\]

**(b) Radiative Forcing for Doubling of $\\text{CO}_2$ ($560\\text{ ppmv}$):**
\\[ \\Delta F_2 = 5.35 \\ln\\left(\\frac{560}{280}\\right) = 5.35 \\ln(2.00) = 5.35 \\times 0.693147 = 3.708\\text{ W/m}^2 \\approx 3.71\\text{ W/m}^2 \\]

**(c) Equilibrium Global Surface Temperature Anomalies:**
Using $\\Delta T_s = \\lambda \\Delta F$:
For current concentration:
\\[ \\Delta T_{s,1} = 0.80\\text{ K/(W/m}^2) \\times 2.169\\text{ W/m}^2 \\approx +1.735^\\circ\\text{C} \\approx +1.74^\\circ\\text{C} \\]
For doubling of $\\text{CO}_2$:
\\[ \\Delta T_{s,2} = 0.80\\text{ K/(W/m}^2) \\times 3.708\\text{ W/m}^2 \\approx +2.966^\\circ\\text{C} \\approx +2.97^\\circ\\text{C} \\]
*(Note: Observed transient warming is lower than equilibrium warming due to large thermal inertia of the deep oceans).*"""
        },
        {
            "id": "prob2_3",
            "tier": "Foundational",
            "title": "Global Carbon Mass Inventory and Airborne Fraction",
            "statement": """Global annual emissions of carbon dioxide from fossil fuel combustion and cement production are $E_{\\text{fossil}} = 36.6\\text{ Gt CO}_2\\text{/yr}$, and emissions from land-use change are $E_{\\text{LUC}} = 4.4\\text{ Gt CO}_2\\text{/yr}$.
(Molecular weight of $\\text{C} = 12.011\\text{ g/mol}$, $\\text{O} = 15.999\\text{ g/mol}$).
(a) Convert total annual emissions from $\\text{Gt CO}_2$ to petagrams of carbon ($\\text{Pg C}$).
(b) Annual measurements show that atmospheric $\\text{CO}_2$ is currently increasing at a rate of $2.40\\text{ ppmv/yr}$. Knowing that the total mass of the Earth's dry atmosphere is $M_{\\text{atm}} = 5.148 \\times 10^{18}\\text{ kg}$ with mean molecular mass $M_{\\text{air}} = 28.97\\text{ g/mol}$, calculate the mass of carbon added to the atmosphere annually in $\\text{Pg C/yr}$.
(c) Calculate the atmospheric airborne fraction (AF).""",
            "solution": """**(a) Conversion of Emissions to $\\text{Pg C}$:**
Total emissions:
\\[ E_{\\text{tot}} = 36.6 + 4.4 = 41.0\\text{ Gt CO}_2\\text{/yr} \\]
Mass fraction of carbon in $\\text{CO}_2$:
\\[ f_{\\text{C}} = \\frac{12.011}{12.011 + 2(15.999)} = \\frac{12.011}{44.009} = 0.27292 \\]
Total carbon emitted:
\\[ E_{\\text{C}} = 41.0\\text{ Gt CO}_2 \\times 0.27292 = 11.19\\text{ Gt C/yr} = 11.19\\text{ Pg C/yr} \\]

**(b) Mass of Carbon Added to Atmosphere:**
Total moles of air in the atmosphere:
\\[ N_{\\text{air}} = \\frac{5.148 \\times 10^{18}\\text{ kg}}{2.897 \\times 10^{-2}\\text{ kg/mol}} = 1.777 \\times 10^{20}\\text{ moles of air} \\]
For an increase of $1\\text{ ppmv}$ ($10^{-6}$ mole fraction):
\\[ \\Delta n_{\\text{CO}_2}(1\\text{ ppmv}) = 10^{-6} \\times 1.777 \\times 10^{20} = 1.777 \\times 10^{14}\\text{ moles of C} \\]
Mass of carbon per 1 ppmv:
\\[ m_{\\text{C}}(1\\text{ ppmv}) = (1.777 \\times 10^{14}\\text{ mol})(12.011 \\times 10^{-3}\\text{ kg/mol}) = 2.1344 \\times 10^{12}\\text{ kg} = 2.134\\text{ Pg C} \\]
For an observed annual rate of $2.40\\text{ ppmv/yr}$:
\\[ \\Delta M_{\\text{atm,annual}} = 2.40 \\times 2.1344 = 5.123\\text{ Pg C/yr} \\]

**(c) Airborne Fraction (AF):**
\\[ AF = \\frac{\\Delta M_{\\text{atm}}}{E_{\\text{C}}} = \\frac{5.123\\text{ Pg C/yr}}{11.19\\text{ Pg C/yr}} = 0.4578 \\approx 45.8\\% \\]
*Interpretation*: Approximately $46\\%$ of human carbon emissions accumulate in the atmosphere, while the remaining $54\\%$ is assimilated by the land biosphere and oceanic carbonate sinks."""
        },
        {
            "id": "prob2_4",
            "tier": "Intermediate",
            "title": "Global Warming Potential (GWP) Integration for Methane",
            "statement": """The radiative efficiency of methane is $a_{\\text{CH}_4} = 3.88 \\times 10^{-4}\\text{ W/(m}^2\\cdot\\text{ppb)}$ and for carbon dioxide is $a_{\\text{CO}_2} = 1.37 \\times 10^{-5}\\text{ W/(m}^2\\cdot\\text{ppb)}$.
Atmospheric methane decays via pseudo-first-order kinetics with an effective perturbation lifetime $\\tau_{\\text{CH}_4} = 11.8\\text{ years}$.
Carbon dioxide decay can be modeled by a simplified impulse response function:
\\[ R_{\\text{CO}_2}(t) = 0.217 + 0.259 \\exp\\left(-\\frac{t}{172.9}\\right) + 0.338 \\exp\\left(-\\frac{t}{18.51}\\right) + 0.186 \\exp\\left(-\\frac{t}{1.186}\\right) \\]
(where $t$ is in years).
(Molecular weights: $M_{\\text{CH}_4} = 16.04\\text{ g/mol}$, $M_{\\text{CO}_2} = 44.01\\text{ g/mol}$).
(a) Convert the radiative efficiencies of both gases to units of $\\text{W}/(\\text{m}^2\\cdot\\text{kg})$ in the atmosphere.
(b) Calculate the absolute cumulative radiative forcing of an instantaneous emission of $1\\text{ kg}$ of $\\text{CH}_4$ over a 20-year time horizon.
(c) Given that the cumulative radiative forcing for $1\\text{ kg}$ of $\\text{CO}_2$ over 20 years is $\\text{AGWP}_{\\text{CO}_2}(20) = 2.49 \\times 10^{-14}\\text{ W}\\cdot\\text{yr}/(\\text{m}^2\\cdot\\text{kg})$, calculate the 20-year GWP of methane ($\text{GWP}_{20}$).""",
            "solution": """**(a) Mass-Specific Radiative Efficiencies:**
From atmospheric mass $M_{\\text{atm}} = 5.148 \\times 10^{18}\\text{ kg}$ and $M_{\\text{air}} = 28.97\\text{ g/mol}$:
$1\\text{ ppb}$ of gas $i$ corresponds to:
\\[ m_i(1\\text{ ppb}) = 10^{-9} \\times \\frac{M_{\\text{atm}}}{M_{\\text{air}}} \\times M_i \\]
For $\\text{CH}_4$:
\\[ m_{\\text{CH}_4}(1\\text{ ppb}) = 10^{-9} \\times \\left(\\frac{5.148 \\times 10^{18}}{28.97 \\times 10^{-3}}\\right) \\times (16.04 \\times 10^{-3}) = 2.8504 \\times 10^9\\text{ kg} \\]
Mass-specific radiative efficiency $\\alpha_{\\text{CH}_4}$:
\\[ \\alpha_{\\text{CH}_4} = \\frac{a_{\\text{CH}_4}}{m_{\\text{CH}_4}(1\\text{ ppb})} = \\frac{3.88 \\times 10^{-4}\\text{ W/m}^2}{2.8504 \\times 10^9\\text{ kg}} = 1.3612 \\times 10^{-13}\\text{ W}/(\\text{m}^2\\cdot\\text{kg}) \\]
For $\\text{CO}_2$:
\\[ m_{\\text{CO}_2}(1\\text{ ppb}) = 10^{-9} \\times \\left(\\frac{5.148 \\times 10^{18}}{28.97 \\times 10^{-3}}\\right) \\times (44.01 \\times 10^{-3}) = 7.8206 \\times 10^9\\text{ kg} \\]
\\[ \\alpha_{\\text{CO}_2} = \\frac{1.37 \\times 10^{-5}}{7.8206 \\times 10^9} = 1.7518 \\times 10^{-15}\\text{ W}/(\\text{m}^2\\cdot\\text{kg}) \\]

**(b) Absolute Cumulative Radiative Forcing for $\\text{CH}_4$ over $T = 20\\text{ years}$:**
The decay of methane is exponential: $C(t) = C_0 \\exp(-t/\\tau)$ with $\\tau = 11.8\\text{ yr}$.
\\[ \\text{AGWP}_{\\text{CH}_4}(20) = \\int_0^{20} \\alpha_{\\text{CH}_4} \\exp\\left(-\\frac{t}{11.8}\\right) dt = \\alpha_{\\text{CH}_4} \\times 11.8 \\left[ 1 - \\exp\\left(-\\frac{20}{11.8}\\right) \\right] \\]
Calculate the integral:
\\[ 1 - \\exp(-1.6949) = 1 - 0.1836 = 0.8164 \\]
\\[ \\int_0^{20} \\exp(-t/11.8) dt = 11.8 \\times 0.8164 = 9.6335\\text{ years} \\]
Now calculate $\\text{AGWP}_{\\text{CH}_4}(20)$ including indirect effects (tropospheric $\\text{O}_3$ and stratospheric $\\text{H}_2\\text{O}$ production amplify methane forcing by a factor of $\\approx 1.65$):
\\[ \\text{AGWP}_{\\text{CH}_4,\\text{direct}} = (1.3612 \\times 10^{-13}) \\times 9.6335 = 1.3113 \\times 10^{-12}\\text{ W}\\cdot\\text{yr}/(\\text{m}^2\\cdot\\text{kg}) \\]
Including standard indirect climate feedback factor $1.65$:
\\[ \\text{AGWP}_{\\text{CH}_4,\\text{total}}(20) = 1.3113 \\times 10^{-12} \\times 1.65 = 2.164 \\times 10^{-12}\\text{ W}\\cdot\\text{yr}/(\\text{m}^2\\cdot\\text{kg}) \\]

**(c) 20-Year Global Warming Potential ($\text{GWP}_{20}$):**
\\[ \\text{GWP}_{20}(\\text{CH}_4) = \\frac{\\text{AGWP}_{\\text{CH}_4}(20)}{\\text{AGWP}_{\\text{CO}_2}(20)} = \\frac{2.164 \\times 10^{-12}}{2.49 \\times 10^{-14}} \\approx 86.9 \\approx 87 \\]
*Significance*: Over a 20-year window, emitting $1\\text{ kg}$ of methane warms the climate **87 times** more than emitting $1\\text{ kg}$ of carbon dioxide, highlighting methane abatement as the highest-leverage near-term climate intervention."""
        },
        {
            "id": "prob2_5",
            "tier": "Intermediate",
            "title": "Ocean Acidification and Carbonate Mineral Saturation Thermodynamics",
            "statement": """Surface seawater at $T = 298\\text{ K}$ has total salinity $S = 35$, a calcium concentration $[\text{Ca}^{2+}] = 0.0102\\text{ mol/kg}$, and an apparent solubility product for aragonite $K'_{sp,\\text{arag}} = 6.60 \\times 10^{-7}\\text{ mol}^2/\\text{kg}^2$.
In pre-industrial seawater ($\text{pH} = 8.25$), the dissolved carbonate concentration was $[\text{CO}_3^{2-}] = 2.40 \\times 10^{-4}\\text{ mol/kg}$.
Under a high-emission future scenario, absorption of $\\text{CO}_2$ drops the $\\text{pH}$ to $7.80$, decreasing carbonate ion concentration to $[\text{CO}_3^{2-}] = 7.50 \\times 10^{-5}\\text{ mol/kg}$.
(a) Calculate the aragonite saturation state $\\Omega_{\\text{arag}}$ for pre-industrial seawater.
(b) Calculate the aragonite saturation state $\\Omega_{\\text{arag}}$ under the acidified scenario.
(c) Calculate the Gibbs free energy change of aragonite dissolution:
\\[ \\text{CaCO}_3(\\text{aragonite}) \\rightleftharpoons \\text{Ca}^{2+} + \\text{CO}_3^{2-} \\]
in $\\text{kJ/mol}$ for both states, and determine whether aragonite dissolution is thermodynamically spontaneous in either case.""",
            "solution": """**(a) Pre-Industrial Aragonite Saturation State:**
The saturation state $\\Omega_{\\text{arag}}$ is defined as:
\\[ \\Omega_{\\text{arag}} = \\frac{[\\text{Ca}^{2+}][\\text{CO}_3^{2-}]}{K'_{sp,\\text{arag}}} \\]
Substitute the pre-industrial values:
\\[ \\Omega_{\\text{arag,pre}} = \\frac{(0.0102\\text{ mol/kg})(2.40 \\times 10^{-4}\\text{ mol/kg})}{6.60 \\times 10^{-7}\\text{ mol}^2/\\text{kg}^2} = \\frac{2.448 \\times 10^{-6}}{6.60 \\times 10^{-7}} \\approx 3.709 \\]
Because $\\Omega > 1.0$, seawater was supersaturated, favoring calcification.

**(b) Acidified Future Aragonite Saturation State:**
Substitute the acidified concentration:
\\[ \\Omega_{\\text{arag,acid}} = \\frac{(0.0102)(7.50 \\times 10^{-5})}{6.60 \\times 10^{-7}} = \\frac{7.65 \\times 10^{-7}}{6.60 \\times 10^{-7}} \\approx 1.159 \\]
*Analysis*: The saturation state has fallen from $3.71$ down to $1.16$, approaching the critical threshold of undersaturation ($\Omega = 1.0$).

**(c) Gibbs Free Energy of Dissolution:**
For the dissolution reaction $\\text{CaCO}_3 \\rightleftharpoons \\text{Ca}^{2+} + \\text{CO}_3^{2-}$, the ion activity product quotient is $Q = [\\text{Ca}^{2+}][\\text{CO}_3^{2-}]$, and $K = K'_{sp}$:
\\[ \\Delta G = R T \\ln\\left(\\frac{Q}{K}\\right) = R T \\ln(\\Omega) \\]
For dissolution to be spontaneous, $\\Delta G_{\\text{dissolution}} < 0$, which requires $\\Omega < 1.0$.
1. Pre-industrial:
   \\[ \\Delta G_{\\text{pre}} = (8.3145\\text{ J/(mol}\\cdot\\text{K)})(298.15\\text{ K}) \\ln(3.709) = (2479.0) \\times (1.3107) = +3249\\text{ J/mol} = +3.25\\text{ kJ/mol} \\]
   Because $\\Delta G > 0$, aragonite dissolution is non-spontaneous (shells are thermodynamically protected).
2. Acidified state:
   \\[ \\Delta G_{\\text{acid}} = 2479.0 \\ln(1.159) = 2479.0 \\times (0.1475) = +365.8\\text{ J/mol} = +0.37\\text{ kJ/mol} \\]
   While still marginally positive in bulk warm surface water, localized cold polar waters with higher $\\text{CO}_2$ solubility drop $\\Omega < 1.0$ ($\Delta G < 0$), causing spontaneous corrosive dissolution of living pteropod shells."""
        },
        {
            "id": "prob2_6",
            "tier": "Intermediate",
            "title": "Thermosteric Sea Level Rise from Oceanic Heat Uptake",
            "statement": """Over a 50-year period, the Earth's climate system accumulates an average top-of-atmosphere net energy imbalance of $\\Delta F_{\\text{net}} = 0.85\\text{ W/m}^2$. Approximately $90\\%$ of this excess heat is sequestered by the global oceans.
The total surface area of the global oceans is $A_{\\text{ocean}} = 3.61 \\times 10^{14}\\text{ m}^2$.
Assume that the sequestered heat is uniformly absorbed throughout the upper ocean to a depth of $H = 700\\text{ m}$.
Average properties of seawater in this layer:
- Density $\\rho = 1025\\text{ kg/m}^3$
- Specific heat capacity $c_p = 3990\\text{ J/(kg}\\cdot\\text{K)}$
- Thermal expansion coefficient $\\beta = 2.10 \\times 10^{-4}\\text{ K}^{-1}$
(Earth's total surface area $A_E = 5.10 \\times 10^{14}\\text{ m}^2$).
(a) Calculate the total excess heat energy $Q_{\\text{ocean}}$ absorbed by the ocean over the 50-year period.
(b) Calculate the average temperature increase $\\Delta T_{\\text{ocean}}$ of the upper $700\\text{ m}$ water layer.
(c) Calculate the resulting thermosteric (thermal expansion) sea level rise $\\Delta h$ in centimeters.""",
            "solution": """**(a) Total Heat Energy Absorbed by the Oceans:**
Total energy absorbed by Earth over $\\Delta t = 50\\text{ years} = 50 \\times 3.15576 \\times 10^7\\text{ s} = 1.5779 \\times 10^9\\text{ s}$:
\\[ Q_{\\text{Earth}} = \\Delta F_{\\text{net}} \\times A_E \\times \\Delta t \\]
\\[ Q_{\\text{Earth}} = (0.85\\text{ W/m}^2) \\times (5.10 \\times 10^{14}\\text{ m}^2) \\times (1.5779 \\times 10^9\\text{ s}) = 6.840 \\times 10^{23}\\text{ Joules} \\]
Since $90\\%$ enters the oceans:
\\[ Q_{\\text{ocean}} = 0.90 \\times 6.840 \\times 10^{23} = 6.156 \\times 10^{23}\\text{ Joules} \\]

**(b) Average Temperature Increase of Upper 700 m:**
Total mass of the upper $700\\text{ m}$ ocean:
\\[ M_{\\text{water}} = \\rho \\times A_{\\text{ocean}} \\times H \\]
\\[ M_{\\text{water}} = (1025\\text{ kg/m}^3) \\times (3.61 \\times 10^{14}\\text{ m}^2) \\times (700\\text{ m}) = 2.590 \\times 10^{20}\\text{ kg} \\]
Heat capacity of this layer:
\\[ C_{\\text{layer}} = M_{\\text{water}} \\times c_p = (2.590 \\times 10^{20}\\text{ kg})(3990\\text{ J/(kg}\\cdot\\text{K)}) = 1.0335 \\times 10^{24}\\text{ J/K} \\]
Temperature increase:
\\[ \\Delta T_{\\text{ocean}} = \\frac{Q_{\\text{ocean}}}{C_{\\text{layer}}} = \\frac{6.156 \\times 10^{23}\\text{ J}}{1.0335 \\times 10^{24}\\text{ J/K}} \\approx 0.5956\\text{ K} \\approx 0.60^\\circ\\text{C} \\]

**(c) Thermosteric Sea Level Rise:**
Using the thermal expansion equation:
\\[ \\Delta h = \\beta \\times H \\times \\Delta T_{\\text{ocean}} \\]
Substitute the values:
\\[ \\Delta h = (2.10 \\times 10^{-4}\\text{ K}^{-1}) \\times (700\\text{ m}) \\times (0.5956\\text{ K}) \\]
\\[ \\Delta h = 0.147 \\times 0.5956 = 0.08755\\text{ m} \\approx 8.76\\text{ cm} \\]
*Conclusion*: Thermal expansion alone accounts for nearly $9\\text{ cm}$ of sea level rise over 50 years, compounded further by continental ice sheet melting."""
        },
        {
            "id": "prob2_7",
            "tier": "Advanced",
            "title": "Thermodynamic Minimum Separation Work for Carbon Capture",
            "statement": """A fossil-fuel combustion flue gas stream at $T_0 = 298.15\\text{ K}$ and total pressure $P_0 = 1.0\\text{ atm}$ has a volumetric composition of $14.0\\%\\ \\text{CO}_2$ and $86.0\\%\\ \\text{N}_2$.
(a) Derive the expression for the thermodynamic minimum work of separation $W_{\\text{min}}$ per mole of pure $\\text{CO}_2$ captured from an ideal binary gas mixture at constant temperature and pressure.
(b) Calculate $W_{\\text{min}}$ in $\\text{kJ/mol CO}_2$ and in $\\text{kJ/kg CO}_2$ for capturing $100\\%$ of the $\\text{CO}_2$ from this flue gas.
(c) Direct Air Capture (DAC) extracts $\\text{CO}_2$ directly from ambient air where $x_{\\text{CO}_2} = 420\\text{ ppmv} = 0.00042$. Calculate $W_{\\text{min}}$ for DAC in $\\text{kJ/kg CO}_2$.
(d) Explain thermodynamically why DAC requires substantially greater energy input than post-combustion capture.""",
            "solution": """**(a) Derivation of Minimum Separation Work:**
The entropy of mixing for $n_1$ moles of gas 1 and $n_2$ moles of gas 2 at constant $T$ and $P$ is:
\\[ \\Delta S_{\\text{mix}} = -R [n_1 \\ln(x_1) + n_2 \\ln(x_2)] \\]
The minimum work required to reverse the mixing process and obtain separated pure gases is equal to the change in Gibbs free energy:
\\[ W_{\\text{min}} = \\Delta G_{\\text{sep}} = -T_0 \\Delta S_{\\text{mix}} = R T_0 [n_1 \\ln(x_1) + n_2 \\ln(x_2)] \\quad (\\text{where work input is positive}) \\]
Per mole of $\\text{CO}_2$ (species 1, with $x_1 = x_{\\text{CO}_2}$ and $n_2/n_1 = (1 - x_1)/x_1$):
\\[ w_{\\text{min}} = -R T_0 \\left[ \\ln(x_1) + \\frac{1 - x_1}{x_1} \\ln(1 - x_1) \\right] \\]
For dilute mixtures where $x_1 \\ll 1$, $\\ln(1 - x_1) \\approx -x_1$, so the second term approaches $\\frac{1 - x_1}{x_1}(-x_1) = -(1 - x_1) \\approx -1$.
Hence:
\\[ w_{\\text{min}} = R T_0 \\left[ \\ln\\left(\\frac{1}{x_1}\\right) - (1 - x_1) \\right] \\]

**(b) Flue Gas Capture ($x_{\\text{CO}_2} = 0.14$):**
Substitute $x_1 = 0.14$ and $T_0 = 298.15\\text{ K}$ ($R T_0 = 2.479\\text{ kJ/mol}$):
\\[ w_{\\text{min}} = -2.479 \\left[ \\ln(0.14) + \\frac{0.86}{0.14} \\ln(0.86) \\right] \\]
\\[ \\ln(0.14) = -1.9661 \\]
\\[ \\frac{0.86}{0.14} \\ln(0.86) = 6.1429 \\times (-0.1508) = -0.9265 \\]
\\[ w_{\\text{min}} = -2.479 [-1.9661 - 0.9265] = -2.479 [-2.8926] = +7.171\\text{ kJ/mol CO}_2 \\]
Converting to $\\text{kJ/kg CO}_2$ ($M = 44.01\\text{ g/mol}$):
\\[ w_{\\text{min}} = \\frac{7.171\\text{ kJ/mol}}{0.04401\\text{ kg/mol}} \\approx 162.9\\text{ kJ/kg CO}_2 \\]

**(c) Direct Air Capture ($x_{\\text{CO}_2} = 0.00042$):**
Substitute $x_1 = 0.00042$:
\\[ \\ln(0.00042) = -7.7753 \\]
\\[ \\frac{1 - 0.00042}{0.00042} \\ln(1 - 0.00042) \\approx -1.000 \\]
\\[ w_{\\text{min}} = -2.479 [-7.7753 - 1.000] = -2.479 [-8.7753] = +21.754\\text{ kJ/mol CO}_2 \\]
Converting to $\\text{kJ/kg CO}_2$:
\\[ w_{\\text{min}} = \\frac{21.754}{0.04401} \\approx 494.3\\text{ kJ/kg CO}_2 \\]

**(d) Thermodynamic Comparison:**
The minimum thermodynamic work for DAC ($494\\text{ kJ/kg}$) is more than **3.0 times higher** than flue gas capture ($163\\text{ kJ/kg}$) solely due to entropic dilution. Furthermore, to capture $1\\text{ ton}$ of $\\text{CO}_2$, a DAC contactor must process over $1.8\\text{ million cubic meters}$ of air, imposing enormous parasitic fan energy and capital footprint penalties."""
        },
        {
            "id": "prob2_8",
            "tier": "Advanced",
            "title": "Climate Feedback Parameter and Effective Climate Sensitivity",
            "statement": """The zero-feedback Planck climate response is $\\lambda_0 = 0.31\\text{ K/(W/m}^2)$.
Empirical climate models estimate the individual feedback parameters as:
- Water vapor feedback: $f_{\\text{wv}} = +0.48$
- Lapse rate feedback: $f_{\\text{lr}} = -0.22$
- Surface albedo feedback: $f_{\\text{alb}} = +0.10$
- Cloud feedback: $f_{\\text{cld}} = +0.18$
(a) Calculate the net feedback parameter $f_{\\text{net}}$ and the climate feedback gain factor $G$.
(b) Calculate the effective climate sensitivity parameter $\\lambda_{\\text{eff}}$ in $\\text{K/(W/m}^2)$.
(c) Calculate the equilibrium surface warming for a doubling of atmospheric $\\text{CO}_2$ ($\\Delta F_{2\\times} = 3.71\\text{ W/m}^2$) with and without the feedback mechanisms.
(d) If melting Arctic permafrost contributes an additional biogeochemical greenhouse feedback $f_{\\text{permafrost}} = +0.12$, calculate the new equilibrium climate warming."""
            ,"solution": """**(a) Net Feedback Parameter and Gain Factor:**
\\[ f_{\\text{net}} = f_{\\text{wv}} + f_{\\text{lr}} + f_{\\text{alb}} + f_{\\text{cld}} \\]
Substitute the given values:
\\[ f_{\\text{net}} = (+0.48) + (-0.22) + (+0.10) + (+0.18) = +0.54 \\]
The climate feedback gain factor $G$ is:
\\[ G = \\frac{1}{1 - f_{\\text{net}}} = \\frac{1}{1 - 0.54} = \\frac{1}{0.46} \\approx 2.1739 \\]

**(b) Effective Climate Sensitivity Parameter:**
\\[ \\lambda_{\\text{eff}} = G \\times \\lambda_0 = 2.1739 \\times 0.31\\text{ K/(W/m}^2) \\approx 0.6739\\text{ K/(W/m}^2) \\]

**(c) Equilibrium Surface Warming for $\\Delta F = 3.71\\text{ W/m}^2$:**
1. Zero-feedback Planck warming:
   \\[ \\Delta T_0 = \\lambda_0 \\Delta F = 0.31 \\times 3.71 \\approx +1.15^\\circ\\text{C} \\]
2. Total equilibrium warming with feedbacks:
   \\[ \\Delta T_s = \\lambda_{\\text{eff}} \\Delta F = 0.6739 \\times 3.71 \\approx +2.50^\\circ\\text{C} \\]
*Result*: Climate feedbacks more than double ($2.17\\times$) the raw Planck temperature response.

**(d) Impact of Additional Permafrost Methane Feedback:**
New net feedback parameter:
\\[ f_{\\text{net}}' = 0.54 + 0.12 = +0.66 \\]
New gain factor:
\\[ G' = \\frac{1}{1 - 0.66} = \\frac{1}{0.34} \\approx 2.9412 \\]
New effective sensitivity:
\\[ \\lambda_{\\text{eff}}' = 2.9412 \\times 0.31 \\approx 0.9118\\text{ K/(W/m}^2) \\]
New equilibrium surface temperature rise:
\\[ \\Delta T_s' = 0.9118 \\times 3.71 \\approx +3.38^\\circ\\text{C} \\]
*Warning*: Non-linear biogeochemical feedbacks dramatically elevate warming risks as $f_{\\text{net}} \\rightarrow 1$."""
        },
        {
            "id": "prob2_9",
            "tier": "Advanced",
            "title": "Ocean Carbonate System Revelle Factor Calculus",
            "statement": """Seawater in chemical equilibrium with atmospheric carbon dioxide has total dissolved inorganic carbon $\\text{DIC} = 2.050 \\times 10^{-3}\\text{ mol/kg}$, total alkalinity $\\text{Alk} = 2.300 \\times 10^{-3}\\text{ eq/kg}$, and an ambient $P_{\\text{CO}_2} = 400\\text{ \mu atm}$.
The carbonate species concentrations are:
- $[\\text{CO}_2^*] = 1.20 \\times 10^{-5}\\text{ mol/kg}$
- $[\\text{HCO}_3^-] = 1.838 \\times 10^{-3}\\text{ mol/kg}$
- $[\\text{CO}_3^{2-}] = 2.000 \\times 10^{-4}\\text{ mol/kg}$
The analytical formulation of the Revelle factor $R$ derived from the carbonate equilibrium conditions at constant total alkalinity is given by:
\\[ R = \\frac{d\\ln P_{\\text{CO}_2}}{d\\ln [\\text{DIC}]} = \\frac{[\\text{DIC}]}{[\\text{CO}_2^*]} \\times \\left[ 1 + \\frac{4[\\text{CO}_3^{2-}]}{[\\text{HCO}_3^-]} + \\frac{[\\text{CO}_3^{2-}]}{[\\text{CO}_2^*]} \\right]^{-1} \\]
(a) Evaluate the Revelle factor $R$ for this seawater parcel.
(b) If atmospheric $P_{\\text{CO}_2}$ increases by $25\\%$ (from $400$ to $500\\ \mu\\text{atm}$), calculate the percentage increase in seawater dissolved inorganic carbon $[\text{DIC}]$.
(c) As more $\\text{CO}_2$ is absorbed, $[\text{CO}_3^{2-}]$ decreases to $1.20 \\times 10^{-4}\\text{ mol/kg}$ and $[\text{CO}_2^*]$ rises to $1.80 \\times 10^{-5}\\text{ mol/kg}$. Re-evaluate $R$ and describe the feedback on future ocean carbon uptake.""",
            "solution": """**(a) Calculation of Initial Revelle Factor $R$:**
Given:
- $[\\text{DIC}] = 2.050 \\times 10^{-3}\\text{ mol/kg}$
- $[\\text{CO}_2^*] = 1.20 \\times 10^{-5}\\text{ mol/kg}$
- $[\\text{HCO}_3^-] = 1.838 \\times 10^{-3}\\text{ mol/kg}$
- $[\\text{CO}_3^{2-}] = 2.000 \\times 10^{-4}\\text{ mol/kg}$

First evaluate the ratio $[\\text{DIC}] / [\\text{CO}_2^*]$:
\\[ \\frac{[\\text{DIC}]}{[\\text{CO}_2^*]} = \\frac{2.050 \\times 10^{-3}}{1.20 \\times 10^{-5}} = 170.833 \\]
Next evaluate the terms inside the brackets:
\\[ \\frac{4[\\text{CO}_3^{2-}]}{[\\text{HCO}_3^-]} = \\frac{4(2.000 \\times 10^{-4})}{1.838 \\times 10^{-3}} = \\frac{8.000 \\times 10^{-4}}{1.838 \\times 10^{-3}} \\approx 0.4353 \\]
\\[ \\frac{[\\text{CO}_3^{2-}]}{[\\text{CO}_2^*]} = \\frac{2.000 \\times 10^{-4}}{1.20 \\times 10^{-5}} \\approx 16.6667 \\]
Sum of terms:
\\[ 1 + 0.4353 + 16.6667 = 18.102 \\]
Calculate $R$:
\\[ R = \\frac{170.833}{18.102} \\approx 9.437 \\approx 9.44 \\]

**(b) Percentage Increase in Seawater DIC:**
From the definition of the Revelle factor:
\\[ \\frac{\\Delta [\\text{DIC}]}{[\\text{DIC}]} = \\frac{1}{R} \\frac{\\Delta P_{\\text{CO}_2}}{P_{\\text{CO}_2}} \\]
For a $25\\%$ increase in atmospheric $P_{\\text{CO}_2}$ ($\\frac{\\Delta P_{\\text{CO}_2}}{P_{\\text{CO}_2}} = +25\\%$):
\\[ \\frac{\\Delta [\\text{DIC}]}{[\\text{DIC}]} = \\frac{25\\%}{9.44} \\approx 2.65\\% \\]
*Insight*: A large $25\\%$ surge in atmospheric $\\text{CO}_2$ translates into only a $2.65\\%$ increase in total oceanic carbon due to buffer resistance.

**(c) Re-evaluation under Acidified Depleted Carbonate Conditions:**
New parameters:
- $[\\text{CO}_3^{2-}] = 1.20 \\times 10^{-4}\\text{ mol/kg}$
- $[\\text{CO}_2^*] = 1.80 \\times 10^{-5}\\text{ mol/kg}$
- $[\\text{HCO}_3^-] \\approx 1.95 \\times 10^{-3}\\text{ mol/kg}$
- $[\\text{DIC}] \\approx 2.088 \\times 10^{-3}\\text{ mol/kg}$

Evaluate the new terms:
\\[ \\frac{[\\text{DIC}]}{[\\text{CO}_2^*]} = \\frac{2.088 \\times 10^{-3}}{1.80 \\times 10^{-5}} = 116.00 \\]
\\[ \\frac{4[\\text{CO}_3^{2-}]}{[\\text{HCO}_3^-]} = \\frac{4(1.20 \\times 10^{-4})}{1.95 \\times 10^{-3}} = 0.2462 \\]
\\[ \\frac{[\\text{CO}_3^{2-}]}{[\\text{CO}_2^*]} = \\frac{1.20 \\times 10^{-4}}{1.80 \\times 10^{-5}} = 6.667 \\]
Sum inside brackets:
\\[ 1 + 0.2462 + 6.667 = 7.913 \\]
New Revelle factor:
\\[ R' = \\frac{116.00}{7.913} \\approx 14.66 \\]
*Conclusion*: As the ocean acidifies and consumes its carbonate buffer, the Revelle factor rises from $9.44$ to $14.66$. This weakening of the chemical buffer means the ocean becomes progressively less effective at absorbing additional fossil fuel emissions, accelerating the airborne accumulation of $\\text{CO}_2$."""
        }
    ]

    return {
        "unit_number": 2,
        "title": "Greenhouse Effect, Radiative Forcing & Global Climate Dynamics",
        "description": "Planetary radiation balance, Stefan-Boltzmann blackbody physics, molecular vibrational infrared spectroscopy of greenhouse gases, the atmospheric IR window, radiative forcing logarithmic and square-root scaling, climate sensitivity, global carbon cycle reservoir mass balances, oceanic carbonate chemistry and ocean acidification thermodynamics, non-CO2 greenhouse gases, climate feedbacks, thermosteric sea level rise, and carbon capture thermodynamics.",
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u = get_unit_2()
    print(f"Unit 2 generated: {len(u['sections'])} sections, {len(u['problems'])} problems.")
