# -*- coding: utf-8 -*-
"""
build_industrial_units_4_5_6.py
Builds Units 4, 5, and 6 for Industrial Chemistry (#48).
7 comprehensive sections & 7 solved problems per unit.
Strictly Zero Course Numbers, Codes, Credit Formulas, or Examination Marks.
"""

def get_units_4_5_6():
    units = [
        # =========================================================================
        # UNIT 4: CEMENT AND LIME INDUSTRIES
        # =========================================================================
        {
            "id": "unit-4-cement-and-lime",
            "unitNumber": 4,
            "title": "Unit 4: Cement and Lime Industries: Silicate Thermochemistry & Clinker Kinetics",
            "leadSummary": "Comprehensive chemical and industrial treatment of hydraulic cement and lime manufacture: raw material moduli (LSF, SM, AM), kiln thermochemistry, solid-state reactions forming alite and belite, Bogue's phase calculations, cement hydration mechanics and ettringite/C-S-H crystallization, suspension preheater rotary kilns, lime calcination dissociation thermodynamics, and slaking engineering.",
            "simulations": ["sim_ind_cement_rotary_kiln_profile"],
            "sections": [
                {
                    "id": "sec-4-1",
                    "secNumber": "4.1",
                    "title": "Raw Materials & Chemical Composition of Portland Cement: Moduli & Control Ratios",
                    "content": r"""Portland cement is a finely pulverized hydraulic mineral binder produced by sintering an intimate blend of calcareous materials (limestone, chalk, marl) and argillaceous materials (clay, shale, slate, blast-furnace slag) at temperatures up to $1450^\circ\text{C}$, followed by intergrinding the resultant clinker with $3 - 5\text{ wt}\%$ calcium sulfate dihydrate (gypsum, $\text{CaSO}_4\cdot 2\text{H}_2\text{O}$) to control flash setting.

### Oxide Composition Spectrum
Commercial Ordinary Portland Cement (OPC, ASTM Type I / EN 197-1 CEM I) exhibits a tightly controlled bulk oxide composition (expressed in standard cement chemistry notation where $\text{C} = \text{CaO}$, $\text{S} = \text{SiO}_2$, $\text{A} = \text{Al}_2\text{O}_3$, $\text{F} = \text{Fe}_2\text{O}_3$, $\text{M} = \text{MgO}$, $\bar{\text{S}} = \text{SO}_3$, $\text{H} = \text{H}_2\text{O}$, $\bar{\text{C}} = \text{CO}_2$):

| Oxide Component | Cement Notation | Mass Percentage Range ($\text{wt}\%$) | Typical Target Value ($\text{wt}\%$) |
|---|---|---|---|
| Calcium Oxide ($\text{CaO}$) | $\text{C}$ | $60.0 - 67.0\%$ | $64.5\%$ |
| Silicon Dioxide ($\text{SiO}_2$) | $\text{S}$ | $18.0 - 24.0\%$ | $21.2\%$ |
| Aluminum Oxide ($\text{Al}_2\text{O}_3$) | $\text{A}$ | $3.5 - 8.0\%$ | $5.4\%$ |
| Iron(III) Oxide ($\text{Fe}_2\text{O}_3$) | $\text{F}$ | $1.5 - 5.0\%$ | $3.2\%$ |
| Magnesium Oxide ($\text{MgO}$) | $\text{M}$ | $0.5 - 4.0\%$ | $1.8\%$ |
| Sulfur Trioxide ($\text{SO}_3$) | $\bar{\text{S}}$ | $1.5 - 3.5\%$ | $2.6\%$ |
| Potassium Oxide ($\text{K}_2\text{O}$) & Sodium Oxide ($\text{Na}_2\text{O}$) | $\text{N} + \text{K}$ | $0.2 - 1.2\%$ | $0.6\%$ |
| Loss on Ignition (LOI) | — | $0.5 - 3.0\%$ | $1.2\%$ |
| Insoluble Residue (IR) | — | $0.1 - 1.5\%$ | $0.4\%$ |
| Free Lime ($\text{CaO}_{\text{free}}$) | — | $0.5 - 1.5\%$ | $0.8\%$ |

### Chemical Moduli & Proportioning Parameters
To maintain kiln burnability, phase equilibrium, and optimal compressive strength development, raw meal proportioning relies on rigorous stoichiometric control indices:

1. **Lime Saturation Factor ($\text{LSF}$)**:
   The ratio of actual effective $\text{CaO}$ to the theoretical maximum $\text{CaO}$ that can chemically combine with $\text{SiO}_2$, $\text{Al}_2\text{O}_3$, and $\text{Fe}_2\text{O}_3$ under kiln equilibrium conditions to yield tricalcium silicate ($\text{C}_3\text{S}$), tricalcium aluminate ($\text{C}_3\text{A}$), and tetracalcium aluminoferrite ($\text{C}_4\text{AF}$):
   $$\text{LSF} = \frac{\% \text{CaO} - 0.7(\% \text{SO}_3)}{2.8(\% \text{SiO}_2) + 1.2(\% \text{Al}_2\text{O}_3) + 0.65(\% \text{Fe}_2\text{O}_3)}$$
   For modern precalciner kilns, $\text{LSF}$ is typically targeted between $0.92$ and $0.98$ ($92\% - 98\%$). An $\text{LSF} > 1.00$ results in uncombined free lime ($\text{CaO}_{\text{free}}$) in the clinker, inducing unsoundness and late destructive expansion, whereas an $\text{LSF} < 0.88$ leads to low $\text{C}_3\text{S}$ content and impaired 28-day hydraulic strength.

2. **Silica Modulus ($\text{SM}$ or $\text{SR}$)**:
   Defines the ratio of solid-state structural forming silica to liquid-phase fluxing agents:
   $$\text{SM} = \frac{\% \text{SiO}_2}{\% \text{Al}_2\text{O}_3 + \% \text{Fe}_2\text{O}_3}$$
   Standard target: $2.2 - 2.8$. A high silica ratio ($\text{SM} > 3.0$) makes the raw mix hard to burn due to a deficit of molten liquid flux at $1350 - 1450^\circ\text{C}$, leading to excessive fuel consumption and slow alite formation. A low silica ratio ($\text{SM} < 1.9$) generates excessive liquid flux, promoting heavy clinker ring formation and kiln refractory coating damage.

3. **Alumina Modulus ($\text{AM}$ or $\text{AR}$)**:
   Governs the ratio of aluminum oxide to iron oxide, dictating liquid melt viscosity and ferrite phase composition:
   $$\text{AM} = \frac{\% \text{Al}_2\text{O}_3}{\% \text{Fe}_2\text{O}_3}$$
   Standard range: $1.3 - 2.2$. When $\text{AM} = 0.64$, all $\text{Al}_2\text{O}_3$ is theoretically bound as brownmillerite ($\text{C}_4\text{AF}$), yielding zero tricalcium aluminate ($\text{C}_3\text{A}$), typical for high sulfate-resisting cement (Type V). An elevated $\text{AM} > 2.5$ yields high $\text{C}_3\text{A}$, accelerating early hydration, rapid heat release, but increasing vulnerability to external sulfate attack."""
                },
                {
                    "id": "sec-4-2",
                    "secNumber": "4.2",
                    "title": "Manufacturing Processes: Dry vs Wet Kilns & Suspension Preheater Precalciners",
                    "content": r"""The industrial manufacturing of Portland cement has evolved through three historical technological eras:
1. **The Wet Process**: Raw materials are ground with $30 - 42\text{ wt}\%$ water to form a pumpable slurry. While wet grinding ensures intimate particle blending and hom*ogeneity, vaporizing this water inside the kiln consumes massive thermal energy ($5,000 - 6,500\text{ kJ/kg clinker}$), making it economically obsolete.
2. **The Long Dry Process**: Raw materials are dried and pulverized into dry raw meal ($< 12\%\text{ retained on }90\,\mu\text{m}$ sieve) before feeding into a long rotary kiln. Specific heat consumption drops to $4,000 - 4,800\text{ kJ/kg clinker}$.
3. **Dry Process with Multi-Stage Cyclone Preheater & Precalciner (NSP System)**: Modern benchmark technology. Dry raw meal descends counter-currently through 4 to 6 cyclone stages against ascending exhaust gases ($950^\circ\text{C} \to 300^\circ\text{C}$). Over $90 - 95\%$ of limestone decarbonation takes place in an inline or separate-line precalciner vessel in $2 - 4\text{ seconds}$ before entering a compact rotary kiln. Heat consumption plummets to $2,900 - 3,200\text{ kJ/kg clinker}$.

```
                 MODERN PRECALCINER ROTARY KILN SYSTEM
       Raw Meal Feed
            │
            ▼
     ┌─────────────┐ <── Exhaust Gas (~320°C) to Raw Mill / Baghouse
     │ Cyclone C1  │
     └──────┬──────┘
            ▼
     ┌─────────────┐
     │ Cyclone C2  │
     └──────┬──────┘
            ▼
     ┌─────────────┐
     │ Cyclone C3  │
     └──────┬──────┘
            ▼
     ┌─────────────┐
     │ Cyclone C4  │
     └──────┬──────┘
            │
            ▼
   ┌─────────────────┐ <── Tertiary Air Duct (heated air from cooler ~850°C)
   │   PRECALCINER   │ <── Secondary Fuel Injection (60% total plant fuel)
   │  (~880 - 920°C) │     >90% CaCO3 -> CaO + CO2 in 3 seconds!
   └────────┬────────┘
            ▼
     ┌─────────────┐
     │ Bottom Cycl.│
     └──────┬──────┘
            │ Decarbonated Hot Meal (~860°C)
            ▼
   ┌────────────────────────────────────────────────────────┐
   │            ROTARY KILN (Length 50-70 m, Slope 3-4%)    │ <── Main Burner Pipe
   │  Calcination ──> Transition ──> Sintering/Burning Zone │     (Coal/Gas + Primary Air)
   │  (900°C)        (1200°C)        (1450°C Liquid Phase)  │     Flame Temp ~1900-2000°C
   └───────────────────────────┬────────────────────────────┘
                               ▼ Clinker Granules (~1400°C)
                     ┌───────────────────┐
                     │ GRATE COOLER      │ ──> Air to Precalciner (Tertiary)
                     │ (Air Quenching)   │ ──> Air to Kiln (Secondary)
                     └─────────┬─────────┘
                               ▼ Cooled Clinker (~80-100°C) to Grinding Mill
```

### Suspension Cyclone Separation Aerodynamics
In each cyclone stage, the raw meal particles are dispersed into the high-velocity flue gas duct, achieve thermal equilibrium with the gas in less than $0.5\text{ seconds}$, and are subsequently centrifuged against the cyclone cone wall:
$$v_{\text{terminal}} = \frac{d_p^2 (\rho_p - \rho_g) g}{18 \mu_g}$$
The separation efficiency in modern low-pressure-drop cyclones exceeds $92 - 97\%$, maximizing interstage thermal regeneration without exceeding $4.5 - 6.0\text{ kPa}$ overall system draft pressure drop."""
                },
                {
                    "id": "sec-4-3",
                    "secNumber": "4.3",
                    "title": "Clinkering Thermochemistry: Solid-State Reactions & Liquid Phase Sintering",
                    "content": r"""As the raw meal descends through the preheater, precalciner, and rotary kiln, it undergoes a sequential cascade of endothermic and exothermic phase transformations driven by rising temperature:

### 1. Preheating & Clay Dehydroxylation ($100 - 800^\circ\text{C}$)
- **Free moisture evaporation** ($100 - 150^\circ\text{C}$):
  $$\text{H}_2\text{O}_{\text{(absorbed)}} \longrightarrow \text{H}_2\text{O}_{(g)} \quad (\Delta H > 0)$$
- **Kaolinite dehydroxylation & metakaolin formation** ($500 - 650^\circ\text{C}$):
  $$\text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4 \longrightarrow \text{Al}_2\text{O}_3\cdot 2\text{SiO}_2 + 2\text{H}_2\text{O}_{(g)}$$
  Metakaolin subsequently collapses into an amorphous spinel-like aluminosilicate mixture and free reactive silica ($\text{SiO}_2$).

### 2. Calcination of Limestone ($750 - 950^\circ\text{C}$)
The intensely endothermic dissociation of calcite:
$$\text{CaCO}_3(s) \rightleftharpoons \text{CaO}(s) + \text{CO}_2(g) \quad \Delta H_{298}^\circ = +178.2\text{ kJ/mol} \quad (+3,180\text{ kJ/kg }\text{CaO})$$
Thermodynamic equilibrium partial pressure of $\text{CO}_2$ over $\text{CaCO}_3$ is governed by the relation:
$$\ln p_{\text{CO}_2} = -\frac{19,750}{T} + 17.65 \quad (p_{\text{CO}_2}\text{ in atm, }T\text{ in K})$$
At $T = 898^\circ\text{C}$ ($1171\text{ K}$), $p_{\text{CO}_2} = 1.0\text{ atm}$. In modern precalciners operating with $20 - 30\%\text{ CO}_2$ in the combustion atmosphere, dissociation occurs vigorously at $850 - 900^\circ\text{C}$.

### 3. Solid-State Belite & Intermediate Phase Formation ($800 - 1250^\circ\text{C}$)
Free $\text{CaO}$ reacts in the solid phase with dehydroxylated silica and alumina at interparticle contact points:
- Monocalcium aluminate and dicalcium ferrite formation:
  $$\text{CaO} + \text{Al}_2\text{O}_3 \longrightarrow \text{CaO}\cdot\text{Al}_2\text{O}_3 \quad (\text{CA})$$
  $$2\text{CaO} + \text{Fe}_2\text{O}_3 \longrightarrow 2\text{CaO}\cdot\text{Fe}_2\text{O}_3 \quad (\text{C}_2\text{F})$$
- Dicalcium silicate (belite, $\beta\text{-C}_2\text{S}$) synthesis:
  $$2\text{CaO} + \text{SiO}_2 \longrightarrow 2\text{CaO}\cdot\text{SiO}_2 \quad (\text{C}_2\text{S}) \quad \Delta H < 0 \text{ (exothermic, }\approx -125\text{ kJ/kg)}$$
- Tetracalcium aluminoferrite (brownmillerite, $\text{C}_4\text{AF}$):
  $$4\text{CaO} + \text{Al}_2\text{O}_3 + \text{Fe}_2\text{O}_3 \longrightarrow 4\text{CaO}\cdot\text{Al}_2\text{O}_3\cdot\text{Fe}_2\text{O}_3 \quad (\text{C}_4\text{AF})$$

### 4. Liquid-Phase Sintering (Clinkering/Burning Zone: $1300 - 1450^\circ\text{C}$)
At $T \approx 1338^\circ\text{C}$ (eutectic temperature in the quaternary $\text{CaO}-\text{SiO}_2-\text{Al}_2\text{O}_3-\text{Fe}_2\text{O}_3$ system with alkali/magnesium fluxes), the aluminate and ferrite phases melt completely into a low-viscosity liquid phase ($20 - 28\text{ wt}\%$ of total meal).
- **Alite ($\text{C}_3\text{S}$) Dissolution-Precipitation Crystallization**:
  Solid $\text{C}_2\text{S}$ and solid $\text{CaO}$ dissolve into the mobile aluminate-ferrite melt, diffuse across the liquid layer, and react to precipitate euhedral tricalcium silicate crystals:
  $$\text{C}_2\text{S}_{(\text{dissolved})} + \text{CaO}_{(\text{dissolved})} \overset{\text{Liquid Melt}}{\rightleftharpoons} \text{C}_3\text{S}_{(\text{crystalline})}$$
  The rate of alite growth is governed by the Noyes-Whitney dissolution-diffusion equation:
  $$\frac{d[\text{C}_3\text{S}]}{dt} = \frac{D \cdot A}{\delta} (C_{\text{sat}} - C_b)$$
  where $D$ is the ionic diffusion coefficient of $\text{Ca}^{2+}$ in the silicate-aluminate melt ($\sim 10^{-6}\text{ cm}^2/\text{s}$ at $1450^\circ\text{C}$), $A$ is interfacial area, $\delta$ is boundary melt layer thickness, and $(C_{\text{sat}} - C_b)$ is thermodynamic supersaturation.

### 5. Rapid Quenching in Grate Cooler ($1400^\circ\text{C} \to 100^\circ\text{C}$)
Rapid cooling by high-pressure air blasts frozen in the high-temperature alite crystal structure (preventing reversible decomposition $\text{C}_3\text{S} \to \text{C}_2\text{S} + \text{CaO}_{\text{free}}$ below $1250^\circ\text{C}$) and prevents inversion of metastable monoclinic $\beta\text{-C}_2\text{S}$ into hydraulically inert $\gamma\text{-C}_2\text{S}$ (which exhibits a $12\%$ volume expansion that pulverizes clinker into dusting powder)."""
                },
                {
                    "id": "sec-4-4",
                    "secNumber": "4.4",
                    "title": "Bogue's Equations & Mineralogical Phase Distribution (C3S, C2S, C3A, C4AF)",
                    "content": r"""The physical, rheological, and mechanical performance of Portland cement is fundamentally governed not by elemental oxide assays, but by the relative proportions of its four crystalline clinker mineral phases:
1. **Alite (Tricalcium Silicate, $\text{C}_3\text{S}$)**: $3\text{CaO}\cdot\text{SiO}_2$ ($M = 228.32\text{ g/mol}$). Constitutes $50 - 70\%$ of clinker. Hydrates rapidly; responsible for early strength development ($1 - 28\text{ days}$).
2. **Belite (Dicalcium Silicate, $\text{C}_2\text{S}$)**: $2\text{CaO}\cdot\text{SiO}_2$ ($M = 172.24\text{ g/mol}$). Constitutes $15 - 30\%$ of clinker. Hydrates slowly; responsible for progressive long-term strength gain ($> 28\text{ days}$ to 1 year).
3. **Tricalcium Aluminate ($\text{C}_3\text{A}$)**: $3\text{CaO}\cdot\text{Al}_2\text{O}_3$ ($M = 270.20\text{ g/mol}$). Constitutes $5 - 12\%$ of clinker. Hydrates violently with massive heat release; vulnerable to sulfate crystallization attack.
4. **Tetracalcium Aluminoferrite (Brownmillerite, $\text{C}_4\text{AF}$)**: $4\text{CaO}\cdot\text{Al}_2\text{O}_3\cdot\text{Fe}_2\text{O}_3$ ($M = 485.96\text{ g/mol}$). Constitutes $5 - 15\%$ of clinker. Low hydraulic activity; acts as a flux in the kiln and confers grey color to cement.

### Derivation of Bogue's Mineralogical Equations
Developed by Robert Herman Bogue (1929) at the National Bureau of Standards, these stoichiometric equations assume equilibrium clinker crystallization where all $\text{Fe}_2\text{O}_3$ combines first with $\text{Al}_2\text{O}_3$ and $\text{CaO}$ to form $\text{C}_4\text{AF}$:

1. **Tetracalcium Aluminoferrite ($\text{C}_4\text{AF}$)**:
   Molar masses: $\text{Fe}_2\text{O}_3 = 159.69$, $\text{C}_4\text{AF} = 485.96$.
   $$\% \text{C}_4\text{AF} = \frac{485.96}{159.69} \times \% \text{Fe}_2\text{O}_3 = 3.043 \times \% \text{Fe}_2\text{O}_3$$

2. **Tricalcium Aluminate ($\text{C}_3\text{A}$)**:
   The amount of $\text{Al}_2\text{O}_3$ consumed by $\text{C}_4\text{AF}$ is $\frac{101.96}{159.69} \times \% \text{Fe}_2\text{O}_3 = 0.6385 \times \% \text{Fe}_2\text{O}_3$.
   Remaining free $\text{Al}_2\text{O}_3$ available for $\text{C}_3\text{A}$:
   $$\text{Al}_2\text{O}_{3, \text{free}} = \% \text{Al}_2\text{O}_3 - 0.6385 \times \% \text{Fe}_2\text{O}_3$$
   Molar ratio $\frac{\text{C}_3\text{A}}{\text{Al}_2\text{O}_3} = \frac{270.20}{101.96} = 2.650$.
   $$\% \text{C}_3\text{A} = 2.650 \times \left(\% \text{Al}_2\text{O}_3 - 0.6385 \times \% \text{Fe}_2\text{O}_3\right) = 2.650 \times \% \text{Al}_2\text{O}_3 - 1.692 \times \% \text{Fe}_2\text{O}_3$$

3. **Tricalcium Silicate ($\text{C}_3\text{S}$)** and **Dicalcium Silicate ($\text{C}_2\text{S}$)**:
   $\text{CaO}$ consumed by non-silicate phases:
   - In $\text{CaSO}_4$ (from gypsum/fuels): $\frac{56.08}{80.06} \times \% \text{SO}_3 = 0.700 \times \% \text{SO}_3$
   - In $\text{C}_4\text{AF}$: $\frac{4 \times 56.08}{159.69} \times \% \text{Fe}_2\text{O}_3 = 1.405 \times \% \text{Fe}_2\text{O}_3$
   - In $\text{C}_3\text{A}$: $\frac{3 \times 56.08}{101.96} \times \text{Al}_2\text{O}_{3, \text{free}} = 1.650 \times (\% \text{Al}_2\text{O}_3 - 0.6385 \times \% \text{Fe}_2\text{O}_3) = 1.650 \times \% \text{Al}_2\text{O}_3 - 1.054 \times \% \text{Fe}_2\text{O}_3$
   Combining $\text{CaO}$ balance with silica balance ($\% \text{SiO}_2 = \frac{60.08}{228.32}\% \text{C}_3\text{S} + \frac{60.08}{172.24}\% \text{C}_2\text{S}$) yields the canonical Bogue equations:
   $$\% \text{C}_3\text{S} = 4.071(\% \text{CaO} - \% \text{CaO}_{\text{free}}) - 7.600(\% \text{SiO}_2) - 6.718(\% \text{Al}_2\text{O}_3) - 1.430(\% \text{Fe}_2\text{O}_3) - 2.852(\% \text{SO}_3)$$
   $$\% \text{C}_2\text{S} = 2.867(\% \text{SiO}_2) - 0.7544(\% \text{C}_3\text{S})$$
   or directly:
   $$\% \text{C}_2\text{S} = -3.071(\% \text{CaO} - \% \text{CaO}_{\text{free}}) + 8.602(\% \text{SiO}_2) + 5.068(\% \text{Al}_2\text{O}_3) + 1.079(\% \text{Fe}_2\text{O}_3) + 2.152(\% \text{SO}_3)$$"""
                },
                {
                    "id": "sec-4-5",
                    "secNumber": "4.5",
                    "title": "Cement Hydration Kinetics, Setting & Hardening: Ettringite & C-S-H Gel Mechanics",
                    "content": r"""Hydration is an exothermic, dissolution-precipitation reaction transforming anhydrous mineral clinker grains into an interlocking cohesive matrix of calcium silicate hydrate gel and crystalline hydration products:

### 1. Tricalcium Aluminate Hydration & Gypsum Retardation
In the absence of gypsum, $\text{C}_3\text{A}$ reacts violently with water within minutes (flash set):
$$\text{C}_3\text{A} + 6\text{H}_2\text{O} \longrightarrow \text{C}_3\text{AH}_6 \quad (\Delta H = -900\text{ J/g})$$
Interground gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$) rapidly dissolves, releasing $\text{Ca}^{2+}$ and $\text{SO}_4^{2-}$ ions that react with $\text{C}_3\text{A}$ to form needle-shaped **ettringite** (AFt phase):
$$\text{C}_3\text{A} + 3(\text{CaSO}_4\cdot 2\text{H}_2\text{O}) + 26\text{H}_2\text{O} \longrightarrow \text{Ca}_6\text{Al}_2(\text{SO}_4)_3(\text{OH})_{12}\cdot 26\text{H}_2\text{O} \quad (\text{Ettringite})$$
Ettringite needles precipitate as a passivating diffusion barrier on the $\text{C}_3\text{A}$ crystal surface, retarding rapid aluminate hydration and keeping the cement slurry plastic and workable for $2 - 4\text{ hours}$ (dormant induction period). Once sulfate ions in the pore solution are depleted, remaining $\text{C}_3\text{A}$ reacts with ettringite to form hexagonal plate **monosulfoaluminate** (AFm phase):
$$\text{C}_3\text{A} + \text{Ca}_6\text{Al}_2(\text{SO}_4)_3(\text{OH})_{12}\cdot 26\text{H}_2\text{O} + 4\text{H}_2\text{O} \longrightarrow 3\left[\text{Ca}_4\text{Al}_2(\text{SO}_4)(\text{OH})_{12}\cdot 6\text{H}_2\text{O}\right]$$

### 2. Silicate Hydration & C-S-H Gel Crystallization
The fundamental engineering strength of concrete is derived from the hydration of alite ($\text{C}_3\text{S}$) and belite ($\text{C}_2\text{S}$):
$$2\text{C}_3\text{S} + 11\text{H}_2\text{O} \longrightarrow \text{C}_{3.4}\text{S}_2\text{H}_8 \ (\text{C-S-H gel}) + 2.6\text{Ca(OH)}_2 \ (\text{Portlandite})$$
$$2\text{C}_2\text{S} + 9\text{H}_2\text{O} \longrightarrow \text{C}_{3.4}\text{S}_2\text{H}_8 \ (\text{C-S-H gel}) + 0.6\text{Ca(OH)}_2$$

### Five Stages of Isothermal Calorimetry Hydration Curve
Isothermal calorimetry identifies five distinct thermodynamic hydration regimes:
1. **Stage I: Initial Pre-Induction Heat Burst ($0 - 15\text{ min}$)**: Instantaneous wetting, congruent ionic dissolution ($\text{Ca}^{2+}, \text{OH}^-, \text{SO}_4^{2-}$), and initial ettringite nucleation.
2. **Stage II: Dormant (Induction) Period ($15\text{ min} - 3\text{ h}$)**: Pore fluid reaches supersaturation ($\text{Ca}^{2+} \approx 20 - 30\text{ mmol/L}$); dissolution rate reaches a local minimum. Concrete remains pumpable and workable.
3. **Stage III: Acceleration Period ($3 - 12\text{ h}$)**: Heterogeneous nucleation and rapid crystallization of nanoporous, high-surface-area ($100 - 300\text{ m}^2/\text{g}$) **Calcium Silicate Hydrate (C-S-H)** gel fibrils, and hexagonal prisms of **Portlandite** ($\text{Ca(OH)}_2$). Initial set (loss of plasticity) and final set (solid rigidity) occur here.
4. **Stage IV: Deceleration Period ($12 - 24\text{ h}$)**: C-S-H shells around clinker grains coalesce. Hydration shifts from a chemical dissolution-controlled mechanism to a diffusion-limited transport regime.
5. **Stage V: Diffusion-Controlled Steady State ($> 24\text{ h}$ to months)**: Slow diffusion of water molecules and calcium ions through the dense C-S-H matrix, steadily filling capillary porosity and increasing compressive strength up to $50 - 100\text{ MPa}$."""
                },
                {
                    "id": "sec-4-6",
                    "secNumber": "4.6",
                    "title": "Special Cements & Concrete Durability: Pozzolanic, Slag & Sulfate Resistant Systems",
                    "content": r"""Modifying clinker mineralogy and incorporating Supplementary Cementitious Materials (SCMs) creates specialized cement systems engineered for aggressive industrial environments:

### 1. High Sulfate-Resisting Portland Cement (ASTM Type V)
Standard cements placed in groundwater or soils rich in sulfate ions ($\text{SO}_4^{2-}$) suffer catastrophic expansion, cracking, and spalling. External sulfate reacts with monosulfoaluminate (AFm) and portlandite to crystallize secondary expansive ettringite:
$$\text{Ca}_4\text{Al}_2(\text{SO}_4)(\text{OH})_{12}\cdot 6\text{H}_2\text{O} + 2\text{Ca}^{2+} + 2\text{SO}_4^{2-} + 20\text{H}_2\text{O} \longrightarrow \text{Ca}_6\text{Al}_2(\text{SO}_4)_3(\text{OH})_{12}\cdot 26\text{H}_2\text{O}$$
Because ettringite crystals occupy over $130\%$ of the molar volume of the original reactants, massive internal crystallization pressure ($> 50\text{ MPa}$) pulverizes the cement paste. By restricting clinker $\text{C}_3\text{A} \le 5.0\text{ wt}\%$ and $2\text{C}_3\text{A} + \text{C}_4\text{AF} \le 25.0\text{ wt}\%$, sulfate-resistant cement eliminates the aluminate source required for secondary ettringite formation.

### 2. Pozzolanic & Slag Blended Cements (CEM II, III, IV)
Supplementary cementitious materials include:
- **Fly Ash (Pulverized Coal Combustion Ash, Class F & C)**
- **Ground Granulated Blast-Furnace Slag (GGBS, vitreous latent hydraulic binder)**
- **Silica Fume (Microsilica, amorphous $\text{SiO}_2 > 85\%$, specific surface $> 20,000\text{ m}^2/\text{kg}$)**
- **Metakaolin (Calcined clay, $\text{Al}_2\text{O}_3\cdot 2\text{SiO}_2$)**

### The Pozzolanic Reaction Mechanism
Pozzolans possess no intrinsic cementitious value on their own, but when finely divided, their amorphous silicate network reacts chemically with liberated, non-cohesive portlandite ($\text{Ca(OH)}_2$) in the presence of water to generate additional secondary C-S-H gel:
$$\text{Ca(OH)}_2 + \text{SiO}_{2, \text{amorphous}} + \text{H}_2\text{O} \longrightarrow \text{C-S-H gel}$$
This reaction densifies the microstructure, consumes alkaline calcium hydroxide (mitigating acid leaching), and subdivides continuous capillary pores ($> 50\text{ nm}$) into ultra-fine gel pores ($< 5\text{ nm}$), reducing chloride and water permeability by $1 - 2$ orders of magnitude."""
                },
                {
                    "id": "sec-4-7",
                    "secNumber": "4.7",
                    "title": "Lime Production Technology: Limestone Calcination, Quicklime & Slaked Lime Engineering",
                    "content": r"""The industrial lime sector produces two primary chemical commodities: **Quicklime** (calcium oxide, $\text{CaO}$) and **Slaked / Hydrated Lime** (calcium hydroxide, $\text{Ca(OH)}_2$), utilizing vertical shaft kilns or horizontal rotary kilns.

### 1. Calcination Chemical Thermodynamics
High-purity limestone ($\text{CaCO}_3 > 95\%$) decomposes endothermically:
$$\text{CaCO}_3(s) \rightleftharpoons \text{CaO}(s) + \text{CO}_2(g) \quad \Delta H_{298}^\circ = +178.2\text{ kJ/mol}$$
Standard Gibbs free energy change as a function of temperature:
$$\Delta G^\circ(T) = 178,200 - 160.5 \cdot T \quad (\text{J/mol})$$
Setting $\Delta G^\circ(T) = 0$ yields the equilibrium decomposition temperature at standard atmospheric pressure ($p_{\text{CO}_2} = 1.0\text{ bar}$):
$$T_{\text{calc}} = \frac{178,200\text{ J/mol}}{160.5\text{ J/(mol}\cdot\text{K)}} \approx 1110.3\text{ K} \approx 837^\circ\text{C}$$

### 2. Kiln Technologies & Reactivity Grades
- **Soft-Burned Lime ($900 - 1050^\circ\text{C}$)**: Produced with short residence time. High specific surface area ($2.0 - 4.0\text{ m}^2/\text{g}$), high porosity ($50 - 60\%$), and violent, highly exothermic reactivity during slaking ($T$ reaches $100^\circ\text{C}$ within $60\text{ seconds}$).
- **Hard-Burned Lime ($1200 - 1350^\circ\text{C}$)**: Extended sintering induces recrystallization and crystal lattice grain coarsening ($\text{CaO}$ crystallites grow from $0.5\,\mu\text{m}$ to $> 10\,\mu\text{m}$). Surface area collapses ($< 0.5\text{ m}^2/\text{g}$); slaking reactivity is drastically suppressed (requires $10 - 30\text{ minutes}$ to react). Used in basic oxygen steelmaking furnaces where explosive slaking must be avoided.

### 3. Slaking Engineering (Hydrator Reactor)
Quicklime is slaked with water in an agitated, multi-stage continuous hydrator:
$$\text{CaO}(s) + \text{H}_2\text{O}(l) \longrightarrow \text{Ca(OH)}_2(s) \quad \Delta H_{298}^\circ = -65.2\text{ kJ/mol} \quad (-1,164\text{ kJ/kg }\text{CaO})$$
Because the reaction is vigorously exothermic, excess water vaporizes as steam, blowing out ultra-fine hydrated lime particles that expand to $2.5\times$ the original volume of the quicklime, producing dry superfine $\text{Ca(OH)}_2$ powder ($> 95\%\text{ passing }45\,\mu\text{m}$)."""
                }
            ],
            "problems": [
                {
                    "id": "prob-4-1",
                    "problemNumber": "4.1",
                    "title": "Bogue Clinker Mineralogical Phase Calculation",
                    "difficulty": "Medium",
                    "statement": r"""A chemical laboratory analyzes an industrial clinker sample by X-ray fluorescence (XRF) and reports the following mass percentages:
$$\text{CaO} = 65.20\%, \quad \text{SiO}_2 = 21.40\%, \quad \text{Al}_2\text{O}_3 = 5.60\%, \quad \text{Fe}_2\text{O}_3 = 3.10\%, \quad \text{SO}_3 = 0.80\%, \quad \text{CaO}_{\text{free}} = 1.00\%$$
1. Calculate the mass percentages of the four Bogue mineralogical phases: $\text{C}_3\text{S}$, $\text{C}_2\text{S}$, $\text{C}_3\text{A}$, and $\text{C}_4\text{AF}$.
2. Verify the mass conservation sum of the mineral phases plus free lime and calcium sulfate.
3. Determine whether this clinker complies with ASTM Type I Portland cement specifications.""",
                    "solution": r"""### Step 1: Compute Mineralogical Phases via Bogue Equations
Effective lime available for silicate/aluminate clinkering:
$$\text{CaO}_{\text{eff}} = \text{CaO} - \text{CaO}_{\text{free}} = 65.20 - 1.00 = 64.20\%$$

**1. Tetracalcium Aluminoferrite ($\text{C}_4\text{AF}$)**:
$$\% \text{C}_4\text{AF} = 3.043 \times \% \text{Fe}_2\text{O}_3 = 3.043 \times 3.10 = 9.43\%$$

**2. Tricalcium Aluminate ($\text{C}_3\text{A}$)**:
$$\% \text{C}_3\text{A} = 2.650 \times \% \text{Al}_2\text{O}_3 - 1.692 \times \% \text{Fe}_2\text{O}_3$$
$$\% \text{C}_3\text{A} = 2.650 \times 5.60 - 1.692 \times 3.10 = 14.840 - 5.245 = 9.595 \approx 9.60\%$$

**3. Tricalcium Silicate ($\text{C}_3\text{S}$)**:
$$\% \text{C}_3\text{S} = 4.071(\% \text{CaO}_{\text{eff}}) - 7.600(\% \text{SiO}_2) - 6.718(\% \text{Al}_2\text{O}_3) - 1.430(\% \text{Fe}_2\text{O}_3) - 2.852(\% \text{SO}_3)$$
$$\% \text{C}_3\text{S} = 4.071(64.20) - 7.600(21.40) - 6.718(5.60) - 1.430(3.10) - 2.852(0.80)$$
$$\% \text{C}_3\text{S} = 261.358 - 162.640 - 37.621 - 4.433 - 2.282 = 54.38\%$$

**4. Dicalcium Silicate ($\text{C}_2\text{S}$)**:
$$\% \text{C}_2\text{S} = 2.867(\% \text{SiO}_2) - 0.7544(\% \text{C}_3\text{S})$$
$$\% \text{C}_2\text{S} = 2.867(21.40) - 0.7544(54.382) = 61.354 - 41.026 = 20.33\%$$

### Step 2: Mass Conservation Verification
- $\text{C}_3\text{S} = 54.38\%$
- $\text{C}_2\text{S} = 20.33\%$
- $\text{C}_3\text{A} = 9.60\%$
- $\text{C}_4\text{AF} = 9.43\%$
- $\text{CaSO}_4 = \frac{136.14}{80.06} \times 0.80 = 1.36\%$
- $\text{CaO}_{\text{free}} = 1.00\%$
$$\text{Sum} = 54.38 + 20.33 + 9.60 + 9.43 + 1.36 + 1.00 = 96.10\%$$
The remaining $3.90\%$ represents minor oxides ($\text{MgO}, \text{K}_2\text{O}, \text{Na}_2\text{O}, \text{TiO}_2$).

### Step 3: ASTM Type I Compliance
ASTM Type I standard requires $\text{C}_3\text{S} \ge 50\%$, $\text{C}_3\text{A} \le 15\%$, and $\text{CaO}_{\text{free}} \le 1.5\%$. This clinker satisfies all criteria with $\text{C}_3\text{S} = 54.4\%$ and $\text{C}_3\text{A} = 9.6\%$, indicating high early strength and normal setting characteristics.""",
                    "hints": ["Subtract free lime from total CaO first.", "Fe2O3 is completely consumed by C4AF before C3A is calculated."]
                },
                {
                    "id": "prob-4-2",
                    "problemNumber": "4.2",
                    "title": "Raw Meal Moduli Optimization (LSF, SM, AM)",
                    "difficulty": "Medium",
                    "statement": r"""A cement plant blends pure limestone ($\text{CaCO}_3$), high-silica sandstone, and bauxitic clay. The target raw meal clinker moduli are:
$$\text{LSF} = 0.960, \quad \text{SM} = 2.500, \quad \text{AM} = 1.800$$
The calcined ash analysis of the raw mix (excluding $\text{CO}_2$ loss on ignition) has $\text{SO}_3 = 0.00\%$.
1. Express $\text{CaO}$ and $\text{SiO}_2$ as mathematical functions of $\text{Al}_2\text{O}_3$ and $\text{Fe}_2\text{O}_3$.
2. Given that $\text{Fe}_2\text{O}_3 = 3.00\text{ wt}\%$, determine the exact required percentages of $\text{Al}_2\text{O}_3$, $\text{SiO}_2$, and $\text{CaO}$ in the ignited meal.""",
                    "solution": r"""### Step 1: Formulate Moduli Equations
From the definition of Alumina Modulus ($\text{AM}$):
$$\text{AM} = \frac{\% \text{Al}_2\text{O}_3}{\% \text{Fe}_2\text{O}_3} = 1.800 \implies \% \text{Al}_2\text{O}_3 = 1.800 \times \% \text{Fe}_2\text{O}_3$$

From the definition of Silica Modulus ($\text{SM}$):
$$\text{SM} = \frac{\% \text{SiO}_2}{\% \text{Al}_2\text{O}_3 + \% \text{Fe}_2\text{O}_3} = 2.500 \implies \% \text{SiO}_2 = 2.500 \times (\% \text{Al}_2\text{O}_3 + \% \text{Fe}_2\text{O}_3)$$

From the definition of Lime Saturation Factor ($\text{LSF}$):
$$\text{LSF} = \frac{\% \text{CaO}}{2.8(\% \text{SiO}_2) + 1.2(\% \text{Al}_2\text{O}_3) + 0.65(\% \text{Fe}_2\text{O}_3)} = 0.960$$
$$\% \text{CaO} = 0.960 \times \left[2.8(\% \text{SiO}_2) + 1.2(\% \text{Al}_2\text{O}_3) + 0.65(\% \text{Fe}_2\text{O}_3)\right]$$

### Step 2: Solve with $\text{Fe}_2\text{O}_3 = 3.00\text{ wt}\%$
1. **Aluminum oxide**:
   $$\% \text{Al}_2\text{O}_3 = 1.800 \times 3.00\% = 5.40\%$$

2. **Silicon dioxide**:
   $$\% \text{SiO}_2 = 2.500 \times (5.40 + 3.00) = 2.500 \times 8.40 = 21.00\%$$

3. **Calcium oxide**:
   $$\text{Denominator} = 2.8(21.00) + 1.2(5.40) + 0.65(3.00)$$
   $$\text{Denominator} = 58.80 + 6.48 + 1.95 = 67.23$$
   $$\% \text{CaO} = 0.960 \times 67.23 = 64.54\%$$

The optimal clinker target composition is:
- **$\text{CaO} = 64.54\%$**
- **$\text{SiO}_2 = 21.00\%$**
- **$\text{Al}_2\text{O}_3 = 5.40\%$**
- **$\text{Fe}_2\text{O}_3 = 3.00\%$**
Sum of four major oxides $= 64.54 + 21.00 + 5.40 + 3.00 = 93.94\%$, leaving $6.06\%$ for $\text{MgO}$, alkalis, and sulfate.""",
                    "hints": ["Work sequentially: AM gives Al2O3, SM gives SiO2, and LSF yields CaO."]
                },
                {
                    "id": "prob-4-3",
                    "problemNumber": "4.3",
                    "title": "Rotary Kiln Mass and Energy Balance with Precalciner",
                    "difficulty": "Hard",
                    "statement": r"""A modern precalciner cement production line produces $\dot{m}_{\text{clinker}} = 5,000\text{ metric tons/day}$ of clinker ($208.33\text{ t/h}$).
- The raw meal feed rate is $1.55\text{ t dry meal / t clinker}$.
- Limestone calcination inside the precalciner and kiln requires $\Delta H_{\text{calc}} = 1,780\text{ kJ/kg clinker}$.
- Clinkering formation reactions (liquid phase exothermic sintering) release $-420\text{ kJ/kg clinker}$.
- Kiln shell radiation and convection thermal loss is $380\text{ kJ/kg clinker}$.
- Preheater exhaust flue gas heat loss at $320^\circ\text{C}$ is $850\text{ kJ/kg clinker}$.
- Clinker cooler exhaust air loss is $340\text{ kJ/kg clinker}$.
- Pulverized coal has a lower heating value $\text{LHV} = 27,500\text{ kJ/kg}$.

1. Calculate the net specific thermal energy consumption per kilogram of clinker ($q_{\text{spec}}$ in $\text{kJ/kg clinker}$).
2. Determine the coal consumption rate in metric tons per hour.
3. If $60\%$ of the fuel is fired in the precalciner and $40\%$ in the main kiln burner, find the hourly coal feed rate to each combustion chamber.""",
                    "solution": r"""### Step 1: Specific Thermal Energy Consumption ($q_{\text{spec}}$)
Sum all energy requirements and heat losses per kg of clinker:
$$q_{\text{spec}} = \Delta H_{\text{calc}} + \Delta H_{\text{sinter}} + q_{\text{radiation}} + q_{\text{preheater gas}} + q_{\text{cooler air}}$$
$$q_{\text{spec}} = 1,780 - 420 + 380 + 850 + 340 = 2,930\text{ kJ/kg clinker}$$
This matches the benchmark performance of a modern 5-stage preheater precalciner kiln ($2,900 - 3,000\text{ kJ/kg}$).

### Step 2: Total Hourly Coal Consumption
Hourly clinker production:
$$\dot{m}_{\text{clinker}} = 208.33\text{ t/h} = 208,333\text{ kg/h}$$
Total thermal heat firing rate:
$$\dot{Q}_{\text{thermal}} = \dot{m}_{\text{clinker}} \times q_{\text{spec}} = 208,333\text{ kg/h} \times 2,930\text{ kJ/kg} = 6.1042 \times 10^8\text{ kJ/h}$$
Coal consumption rate:
$$\dot{m}_{\text{coal}} = \frac{\dot{Q}_{\text{thermal}}}{\text{LHV}} = \frac{6.1042 \times 10^8\text{ kJ/h}}{27,500\text{ kJ/kg}} = 22,197\text{ kg/h} \approx 22.20\text{ metric tons/h}$$

### Step 3: Fuel Distribution
- **Precalciner ($60\%$)**:
  $$\dot{m}_{\text{coal, precalc}} = 0.60 \times 22.20\text{ t/h} = 13.32\text{ metric tons/h}$$
- **Main Kiln Burner ($40\%$)**:
  $$\dot{m}_{\text{coal, kiln}} = 0.40 \times 22.20\text{ t/h} = 8.88\text{ metric tons/h}$$

The plant fires **$13.32\text{ t/h}$** into the precalciner and **$8.88\text{ t/h}$** through the main kiln burner pipe.""",
                    "hints": ["Net heat = (Endothermic calcination - exothermic sintering) + all thermal losses.", "Divide total heat by lower heating value of coal."]
                },
                {
                    "id": "prob-4-4",
                    "problemNumber": "4.4",
                    "title": "Limestone Decomposition Pressure & Dissociation Temperature",
                    "difficulty": "Easy",
                    "statement": r"""The equilibrium decomposition of calcite follows:
$$\text{CaCO}_3(s) \rightleftharpoons \text{CaO}(s) + \text{CO}_2(g)$$
Experimental thermodynamic parameters are $\Delta H^\circ = +178.2\text{ kJ/mol}$ and $\Delta S^\circ = +160.5\text{ J/(mol}\cdot\text{K)}$.
1. Calculate the equilibrium partial pressure of $\text{CO}_2$ ($p_{\text{CO}_2}$) at $800^\circ\text{C}$ ($1073.15\text{ K}$) and at $950^\circ\text{C}$ ($1223.15\text{ K}$).
2. If flue gas inside a precalciner has a total pressure of $1.0\text{ bar}$ and contains $28.0\text{ vol}\%\text{ CO}_2$ ($p_{\text{CO}_2} = 0.28\text{ bar}$), calculate the minimum operating temperature required for limestone to decompose spontaneously.""",
                    "solution": r"""### Step 1: Equilibrium $p_{\text{CO}_2}$ Calculations
Using the thermodynamic relation $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ = -RT \ln K_p$, where $K_p = p_{\text{CO}_2} / p^\circ$:
$$\ln p_{\text{CO}_2} = -\frac{\Delta H^\circ}{RT} + \frac{\Delta S^\circ}{R}$$
Here $R = 8.314\text{ J/(mol}\cdot\text{K)}$.

- **At $T_1 = 800^\circ\text{C} = 1073.15\text{ K}$**:
  $$\ln p_{\text{CO}_2} = -\frac{178,200}{8.314 \times 1073.15} + \frac{160.5}{8.314} = -19.973 + 19.305 = -0.668$$
  $$p_{\text{CO}_2} = e^{-0.668} \approx 0.513\text{ bar}$$

- **At $T_2 = 950^\circ\text{C} = 1223.15\text{ K}$**:
  $$\ln p_{\text{CO}_2} = -\frac{178,200}{8.314 \times 1223.15} + \frac{160.5}{8.314} = -17.523 + 19.305 = +1.782$$
  $$p_{\text{CO}_2} = e^{1.782} \approx 5.94\text{ bar}$$

### Step 2: Minimum Decomposition Temperature for $p_{\text{CO}_2} = 0.28\text{ bar}$
$$\ln(0.28) = -\frac{178,200}{8.314 \cdot T} + \frac{160.5}{8.314}$$
$$-1.273 = -\frac{21,433.7}{T} + 19.305$$
$$\frac{21,433.7}{T} = 19.305 + 1.273 = 20.578$$
$$T = \frac{21,433.7}{20.578} = 1041.6\text{ K} \approx 768.4^\circ\text{C}$$

Limestone decomposes spontaneously in the precalciner at temperatures above **$768.4^\circ\text{C}$**.""",
                    "hints": ["Kp equals the partial pressure of CO2.", "Delta G = 0 defines equilibrium at that specific partial pressure."]
                },
                {
                    "id": "prob-4-5",
                    "problemNumber": "4.5",
                    "title": "Alite Hydration Stoichiometry & Portlandite Generation",
                    "difficulty": "Medium",
                    "statement": r"""A concrete mix contains $400\text{ kg}$ of pure Portland cement per cubic meter. The cement mineralogy consists of $60.0\text{ wt}\%\text{ C}_3\text{S}$ ($240\text{ kg}$) and $20.0\text{ wt}\%\text{ C}_2\text{S}$ ($80\text{ kg}$).
The stoichiometric hydration equations are:
$$2\text{C}_3\text{S} + 11\text{H}_2\text{O} \longrightarrow \text{C}_{3.4}\text{S}_2\text{H}_8 + 2.6\text{Ca(OH)}_2$$
$$2\text{C}_2\text{S} + 9\text{H}_2\text{O} \longrightarrow \text{C}_{3.4}\text{S}_2\text{H}_8 + 0.6\text{Ca(OH)}_2$$
Molar masses: $\text{C}_3\text{S} = 228.32\text{ g/mol}$, $\text{C}_2\text{S} = 172.24\text{ g/mol}$, $\text{Ca(OH)}_2 = 74.09\text{ g/mol}$.
1. Calculate the mass of calcium hydroxide (portlandite, $\text{Ca(OH)}_2$) generated per cubic meter of concrete after complete hydration.
2. If microsilica ($\text{SiO}_2 = 60.08\text{ g/mol}$) is blended to consume $80\%$ of this portlandite via the pozzolanic reaction:
   $$\text{Ca(OH)}_2 + \text{SiO}_2 + \text{H}_2\text{O} \longrightarrow \text{C-S-H}$$
   calculate the mass of silica fume required per cubic meter of concrete.""",
                    "solution": r"""### Step 1: Portlandite Generated by Complete Hydration
- **From $\text{C}_3\text{S}$ ($240\text{ kg}$)**:
  Moles of $\text{C}_3\text{S}$:
  $$n_{\text{C}_3\text{S}} = \frac{240,000\text{ g}}{228.32\text{ g/mol}} = 1,051.16\text{ mol}$$
  From stoichiometry, $1\text{ mol }\text{C}_3\text{S}$ produces $\frac{2.6}{2} = 1.30\text{ mol }\text{Ca(OH)}_2$:
  $$n_{\text{Ca(OH)}_2, \text{C}_3\text{S}} = 1.30 \times 1,051.16 = 1,366.51\text{ mol}$$

- **From $\text{C}_2\text{S}$ ($80\text{ kg}$)**:
  Moles of $\text{C}_2\text{S}$:
  $$n_{\text{C}_2\text{S}} = \frac{80,000\text{ g}}{172.24\text{ g/mol}} = 464.47\text{ mol}$$
  From stoichiometry, $1\text{ mol }\text{C}_2\text{S}$ produces $\frac{0.6}{2} = 0.30\text{ mol }\text{Ca(OH)}_2$:
  $$n_{\text{Ca(OH)}_2, \text{C}_2\text{S}} = 0.30 \times 464.47 = 139.34\text{ mol}$$

- **Total Portlandite Generated**:
  $$n_{\text{Ca(OH)}_2, \text{total}} = 1,366.51 + 139.34 = 1,505.85\text{ mol}$$
  $$m_{\text{Ca(OH)}_2} = 1,505.85\text{ mol} \times 74.09\text{ g/mol} = 111,568\text{ g} \approx 111.57\text{ kg/m}^3$$

### Step 2: Silica Fume Required for Pozzolanic Fixation
Target consumption: $80\%$ of total $\text{Ca(OH)}_2$:
$$n_{\text{Ca(OH)}_2, \text{target}} = 0.80 \times 1,505.85\text{ mol} = 1,204.68\text{ mol}$$
Stoichiometric ratio with $\text{SiO}_2$ is $1:1$:
$$n_{\text{SiO}_2} = 1,204.68\text{ mol}$$
Mass of pure reactive silica fume required:
$$m_{\text{SiO}_2} = 1,204.68\text{ mol} \times 60.08\text{ g/mol} = 72,377\text{ g} \approx 72.38\text{ kg/m}^3$$

The mix requires **$72.38\text{ kg}$** of active silica fume per $\text{m}^3$ of concrete ($18.1\text{ wt}\%$ cement replacement).""",
                    "hints": ["Convert kilograms to moles using molar masses.", "Account for stoichiometric coefficients 1.3 for C3S and 0.3 for C2S."]
                },
                {
                    "id": "prob-4-6",
                    "problemNumber": "4.6",
                    "title": "Quicklime Slaking Enthalpy & Steam Venting Balance",
                    "difficulty": "Medium",
                    "statement": r"""A lime hydration plant slakes $10.0\text{ metric tons/h}$ of pure quicklime ($\text{CaO}$, $56.08\text{ g/mol}$) with liquid water at $25^\circ\text{C}$ in an atmospheric continuous hydrator.
The slaking reaction is:
$$\text{CaO}(s) + \text{H}_2\text{O}(l) \longrightarrow \text{Ca(OH)}_2(s) \quad \Delta H_{\text{rxn}} = -65.2\text{ kJ/mol}$$
Molar mass of $\text{Ca(OH)}_2 = 74.09\text{ g/mol}$, $\text{H}_2\text{O} = 18.02\text{ g/mol}$.
- The dry hydrated lime powder product discharges at $100^\circ\text{C}$.
- Heat capacity of $\text{Ca(OH)}_2(s)$ is $c_p = 1.20\text{ kJ/(kg}\cdot\text{K)}$.
- Heat capacity of liquid water is $c_p = 4.184\text{ kJ/(kg}\cdot\text{K)}$.
- Latent heat of vaporization of water at $100^\circ\text{C}$ is $\Delta H_{\text{vap}} = 2,257\text{ kJ/kg}$.
- Ambient thermal heat loss from the hydrator shell is $5.0\%$ of the reaction enthalpy.

1. Calculate the total heat generated by the slaking reaction per hour ($\text{GJ/h}$).
2. Determine the sensible heat required to warm the hydrated lime powder from $25^\circ\text{C}$ to $100^\circ\text{C}$.
3. Calculate the mass of water vaporized as steam per hour to dissipate the excess heat.
4. Determine the total water feed rate (stoichiometric water + vaporized water) in metric tons per hour.""",
                    "solution": r"""### Step 1: Slaking Heat Generation Rate
Moles of $\text{CaO}$ fed per hour:
$$n_{\text{CaO}} = \frac{10,000 \times 10^3\text{ g}}{56.08\text{ g/mol}} = 1.7832 \times 10^5\text{ mol/h}$$
Total reaction enthalpy released:
$$\dot{Q}_{\text{gen}} = 1.7832 \times 10^5\text{ mol/h} \times 65.2\text{ kJ/mol} = 1.1626 \times 10^7\text{ kJ/h} = 11.626\text{ GJ/h}$$

### Step 2: Sensible Heat in Hydrated Lime Powder
Mass of dry $\text{Ca(OH)}_2$ produced:
$$\dot{m}_{\text{hydrate}} = 1.7832 \times 10^5\text{ mol/h} \times 74.09\text{ g/mol} = 1.3212 \times 10^7\text{ g/h} = 13,212\text{ kg/h}$$
Sensible heat to heat hydrate from $25^\circ\text{C}$ to $100^\circ\text{C}$ ($\Delta T = 75\text{ K}$):
$$\dot{Q}_{\text{sens, hydrate}} = 13,212\text{ kg/h} \times 1.20\text{ kJ/(kg}\cdot\text{K)} \times 75\text{ K} = 1.1891 \times 10^6\text{ kJ/h} = 1.189\text{ GJ/h}$$

### Step 3: Steam Evaporation & Heat Dissipation
Reactor shell heat loss:
$$\dot{Q}_{\text{loss}} = 0.05 \times 11.626\text{ GJ/h} = 0.5813\text{ GJ/h} = 5.813 \times 10^5\text{ kJ/h}$$
Net heat that must be removed by boiling water:
$$\dot{Q}_{\text{boil}} = \dot{Q}_{\text{gen}} - \dot{Q}_{\text{sens, hydrate}} - \dot{Q}_{\text{loss}}$$
$$\dot{Q}_{\text{boil}} = 11.626 - 1.189 - 0.581 = 9.856\text{ GJ/h} = 9.856 \times 10^6\text{ kJ/h}$$
Enthalpy to heat $1\text{ kg}$ liquid water from $25^\circ\text{C}$ to $100^\circ\text{C}$ and vaporize it at $100^\circ\text{C}$:
$$\Delta h_{\text{water}\to\text{steam}} = c_{p, \text{water}} \times (100 - 25) + \Delta H_{\text{vap}} = 4.184 \times 75 + 2,257 = 313.8 + 2,257 = 2,570.8\text{ kJ/kg}$$
Mass of water boiled to steam per hour:
$$\dot{m}_{\text{steam}} = \frac{9.856 \times 10^6\text{ kJ/h}}{2,570.8\text{ kJ/kg}} = 3,833.8\text{ kg/h} \approx 3.834\text{ metric tons/h}$$

### Step 4: Total Water Feed Rate
Stoichiometric water consumed chemically:
$$\dot{m}_{\text{water, rxn}} = 1.7832 \times 10^5\text{ mol/h} \times 18.02\text{ g/mol} = 3,213.3\text{ kg/h} = 3.213\text{ metric tons/h}$$
Total water feed required:
$$\dot{m}_{\text{water, total}} = \dot{m}_{\text{water, rxn}} + \dot{m}_{\text{steam}} = 3,213.3 + 3,833.8 = 7,047.1\text{ kg/h} \approx 7.05\text{ metric tons/h}$$

The plant feeds **$7.05\text{ metric tons/h}$** of water to produce **$13.21\text{ t/h}$** of dry hydrate while venting **$3.83\text{ t/h}$** of steam.""",
                    "hints": ["Slaking heat is balanced by hydrate sensible warming, wall loss, and water boiling.", "Total water is reaction water plus evaporated water."]
                },
                {
                    "id": "prob-4-7",
                    "problemNumber": "4.7",
                    "title": "Grinding Clinker with Gypsum: Specific Surface & Set Regulation",
                    "difficulty": "Easy",
                    "statement": r"""A ball mill finish grinding circuit grinds clinker ($\rho_{\text{clinker}} = 3.15\text{ g/cm}^3$) with gypsum to produce Ordinary Portland Cement.
The target Blaine specific surface area is $S_w = 360\text{ m}^2/\text{kg}$ ($3,600\text{ cm}^2/\text{g}$).
1. Assuming uniform spherical particles, calculate the Sauter mean diameter ($d_{32}$) of the cement grains in micrometers.
2. The clinker contains $10.5\text{ wt}\%\text{ C}_3\text{A}$ ($M = 270.20\text{ g/mol}$). To prevent flash setting, gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$, $M = 172.17\text{ g/mol}$) must be added at a molar ratio of $0.60\text{ mol gypsum}$ per mole of $\text{C}_3\text{A}$. Calculate the required mass percentage of gypsum in the cement blend.""",
                    "solution": r"""### Step 1: Sauter Mean Diameter ($d_{32}$)
Blaine specific surface area per unit volume ($S_v$):
$$S_v = S_w \times \rho = 3,600\text{ cm}^2/\text{g} \times 3.15\text{ g/cm}^3 = 11,340\text{ cm}^{-1}$$
For spherical particles, specific surface area relates to Sauter mean diameter by:
$$S_v = \frac{6}{d_{32}} \implies d_{32} = \frac{6}{S_v}$$
$$d_{32} = \frac{6}{11,340\text{ cm}^{-1}} = 5.291 \times 10^{-4}\text{ cm} = 5.29\,\mu\text{m}$$
The equivalent Sauter mean diameter is **$5.29\,\mu\text{m}$**.

### Step 2: Gypsum Mass Percentage Calculation
In $100\text{ g}$ of clinker:
$$m_{\text{C}_3\text{A}} = 10.5\text{ g}$$
Moles of $\text{C}_3\text{A}$:
$$n_{\text{C}_3\text{A}} = \frac{10.5\text{ g}}{270.20\text{ g/mol}} = 0.03886\text{ mol}$$
Required moles of gypsum:
$$n_{\text{gypsum}} = 0.60 \times 0.03886\text{ mol} = 0.02332\text{ mol}$$
Mass of gypsum to add per $100\text{ g}$ clinker:
$$m_{\text{gypsum}} = 0.02332\text{ mol} \times 172.17\text{ g/mol} = 4.014\text{ g}$$
Mass percentage of gypsum in the final cement blend:
$$\% \text{ Gypsum} = \frac{4.014\text{ g}}{100\text{ g} + 4.014\text{ g}} \times 100\% = \frac{4.014}{104.014} \times 100\% = 3.86\%$$

The cement blend must contain **$3.86\text{ wt}\%$ gypsum**.""",
                    "hints": ["Sauter diameter d_32 = 6 / (rho * S_w).", "Calculate moles of C3A, multiply by 0.60, then convert to gypsum grams."]
                }
            ]
        },

        # =========================================================================
        # UNIT 5: SOAPS AND DETERGENTS INDUSTRIES
        # =========================================================================
        {
            "id": "unit-5-soaps-and-detergents",
            "unitNumber": 5,
            "title": "Unit 5: Soaps and Detergents: Saponification, Phase Equilibria & Surfactant Engineering",
            "leadSummary": "Comprehensive physical chemistry and process engineering of soaps and synthetic surfactants: triglyceride saponification kinetics, continuous multi-stage centrifugal technologies (Sharples, DeLaval, Mazzoni), ternary soap-water-electrolyte phase equilibria (neat soap, middle soap, nigre), glycerol multi-effect recovery, linear alkylbenzene sulfonate (LABS) falling film reactor engineering, detergent builders, CMC thermodynamics, and biodegradability.",
            "simulations": ["sim_ind_soap_saponification_reactor"],
            "sections": [
                {
                    "id": "sec-5-1",
                    "secNumber": "5.1",
                    "title": "Chemistry of Triglycerides, Fatty Acid Blends & Alkaline Saponification Mechanisms",
                    "content": r"""Soaps are sodium or potassium salts of long-chain aliphatic carboxylic acids ($\text{C}_{12} - \text{C}_{18}$). Industrial soap formulations utilize blended natural triacylglycerols derived from animal tallow (primarily oleic, palmitic, and stearic acids) and vegetable oils (coconut oil, palm kernel oil, babassu oil rich in lauric and myristic acids).

### Triglyceride Feedstock Fatty Acid Profiles
The physical texture, lathering volume, and solubility of soap are governed by the fatty acid distribution:
- **Tallow ($75 - 85\%$)**: Provides hardness, long-lasting bar durability, and creaminess:
  - Stearic acid ($\text{C}_{17}\text{H}_{35}\text{COOH}$, 18:0): saturated, high melting point ($69.6^\circ\text{C}$).
  - Palmitic acid ($\text{C}_{15}\text{H}_{31}\text{COOH}$, 16:0): saturated, melting point $62.9^\circ\text{C}$.
  - Oleic acid ($\text{C}_{17}\text{H}_{33}\text{COOH}$, 18:1 cis-9): monounsaturated, adds softness and solubility.
- **Coconut / Palm Kernel Oil ($15 - 25\%$)**: Provides instant wetting, cold-water solubility, and voluminous, fluffy lather:
  - Lauric acid ($\text{C}_{11}\text{H}_{23}\text{COOH}$, 12:0): short chain, rapid micellization.
  - Myristic acid ($\text{C}_{13}\text{H}_{27}\text{COOH}$, 14:0).

### Stepwise Alkaline Saponification Mechanism
Saponification is the base-catalyzed hydrolysis of triglyceride ester bonds by nucleophilic acyl substitution ($\text{B}_{\text{AC}}2$):

```
     CH2-O-CO-R1                           CH2-OH
     │                                     │
     CH-O-CO-R2   +  3 NaOH  ──>  3 R-COONa  +  CH-OH
     │             (Heat, Cat.)   (Sodium      │
     CH2-O-CO-R3                   Soap)       CH2-OH
    (Triglyceride)                            (Glycerol)
```

The reaction proceeds via three consecutive reversible elementary steps:
$$\text{Triglyceride} + \text{OH}^- \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} \text{Diglyceride} + \text{Soap}$$
$$\text{Diglyceride} + \text{OH}^- \underset{k_{-2}}{\overset{k_2}{\rightleftharpoons}} \text{Monoglyceride} + \text{Soap}$$
$$\text{Monoglyceride} + \text{OH}^- \underset{k_{-3}}{\overset{k_3}{\rightleftharpoons}} \text{Glycerol} + \text{Soap}$$

### Kinetic Autocatalysis & Mass Transfer Barrier
Because neat molten fat and concentrated aqueous sodium hydroxide ($30 - 50\text{ wt}\%\text{ NaOH}$) are mutually immiscible, the initial reaction rate is limited by interfacial mass transfer. However, as soap molecules are synthesized, they act as powerful emulsifiers, lowering interfacial tension from $> 30\text{ mN/m}$ to $< 2\text{ mN/m}$, dramatically increasing the specific interfacial contact area $a$. Consequently, saponification exhibits distinct **autocatalytic sigmoidal kinetics**:
$$r_{\text{sap}} = - \frac{d[\text{TG}]}{dt} = k \cdot a \cdot [\text{TG}] [\text{NaOH}]$$
Once an emulsion is established at $90 - 105^\circ\text{C}$, the reaction reaches completion in a few minutes."""
                },
                {
                    "id": "sec-5-2",
                    "secNumber": "5.2",
                    "title": "Industrial Saponification Technologies: Batch Pan Boiling vs Continuous Centrifugal Systems",
                    "content": r"""The industrial manufacturing of soap has evolved from laborious multi-day batch boiling in huge kettles to automated continuous, high-pressure centrifugal systems:

### 1. The Full-Boiled Batch Kettle Process
A classical 5-stage operation conducted in open steel pans holding $20 - 100\text{ tons}$ of fat:
1. **Killing (Saponification)**: Fat is boiled with open steam coils while feeding dilute caustic soda ($10 - 15\%\text{ NaOH}$) until $95\%$ of fat is saponified.
2. **Graining (Salting Out)**: Coarse dry sodium chloride ($\text{NaCl}$) or saturated brine is shoveled into the boiling kettle until the electrolyte concentration reaches $6 - 8\text{ wt}\%$. The soap insolubilizes, separating into a buoyant, curdy solid layer and an underlying aqueous brine phase containing $8 - 10\%$ glycerol (spent lye).
3. **Washing (Lye Extraction)**: The spent lye is drained from the kettle bottom, and fresh water and brine are introduced to extract remaining dissolved glycerol from the curd.
4. **Fitting (Finishing)**: Water is carefully boiled into the curd to adjust electrolyte concentration to approximately $0.5 - 1.0\%\text{ NaCl}$. Under this condition, the mass separates into two equilibrium liquid phases: an upper pure **Neat Soap** layer ($65 - 70\%$ soap) and a lower **Nigre** layer ($30 - 40\%$ soap, rich in impurities, iron soaps, and coloring matter).
5. **Settling**: The kettle rests for $24 - 48\text{ hours}$ to allow gravimetric phase stratification before skimming neat soap.

### 2. Modern Continuous Saponification Technologies
- **Sharples Process**: Uses 4 to 5 counter-current mixing stages coupled to high-speed disc-stack centrifuges ($5,000 - 6,000\times g$). Fresh caustic and salt wash water flow counter-current to the fat/soap stream, achieving $> 99.8\%$ saponification and extracting $> 98\%$ of glycerol in $2\text{ hours}$ residence time, yielding spent lye containing $15 - 20\%$ glycerol.
- **DeLaval Centripure Process**: Employs an enclosed, hermetic reactor operating under pressure ($3 - 4\text{ bar}$, $120^\circ\text{C}$) where fat and $50\%\text{ NaOH}$ are continuously recirculated with a high-shear pump, flashing into a hermetic separator.
- **Mazzoni SC Continuous Saponification**: Utilizes an autoclave reactor with an inline turbine mixer at $130 - 140^\circ\text{C}$ ($4 - 5\text{ bar}$). Saponification reaches completion in under $10\text{ minutes}$, with neat soap continuously vacuum flash-dried."""
                },
                {
                    "id": "sec-5-3",
                    "secNumber": "5.3",
                    "title": "Phase Equilibria of Soap-Water-Electrolyte Systems: Neat Soap, Middle Soap, Nigre & Salt Curd",
                    "content": r"""The physical behavior and separation of soap during manufacture is governed by the ternary phase diagram of the **Sodium Soap – Water – Sodium Chloride** system (pioneered by James William McBain):

```
                         Soap (100%)
                             /\
                            /  \
                           /    \
                          / Neat \
                         /  Soap  \
                        / (Lamellar\
                       /   Liquid)  \
                      /              \
                     / Middle   Salt  \
                    /  Soap     Curd   \
                   / (Hexag.)  (Solid)  \
                  /                      \
                 /   Nigre                \
                /  (Dilute)                \
               /____________________________\
       Water (100%)                      NaCl (100%)
```

### Major Thermodynamic Phases
1. **Neat Soap ($L_\alpha$ phase)**:
   A birefringent, lyotropic **lamellar liquid crystal** consisting of parallel bilayers of oriented soap molecules separated by thin intervening water sheets ($30 - 35\text{ wt}\%\text{ H}_2\text{O}$, $65 - 70\text{ wt}\%\text{ Soap}$, $0.3 - 0.8\text{ wt}\%\text{ NaCl}$). At $80 - 100^\circ\text{C}$, neat soap flows as a pumpable, non-Newtonian pseudoplastic liquid.
2. **Middle Soap ($H_1$ phase)**:
   A rigid, unworkable **hexagonal liquid crystal** phase formed at lower soap concentrations ($30 - 50\text{ wt}\%\text{ Soap}$) and very low salt levels ($< 0.2\%\text{ NaCl}$). Cylindrical micelles pack into a hexagonal array. Middle soap exhibits immense viscosity and elastic consistency—it cannot be pumped or stirred and represents a catastrophic operational hazard ("gel freeze") in an industrial kettle or pipe.
3. **Nigre ($L_1$ phase)**:
   An isotropic, dilute micellar liquid phase containing $30 - 45\text{ wt}\%\text{ Soap}$, high water ($55 - 70\%$), and higher salt concentration ($1.0 - 2.0\%\text{ NaCl}$). Because impurities, oxidized dirt, and polyvalent metal soaps are more soluble in nigre than in the dense neat soap crystal lattice, nigre acts as a chemical purification scavenger.
4. **Curd Soap**:
   A hydrated crystalline solid mesh formed at high electrolyte levels ($\text{NaCl} > 6 - 8\%$). The presence of high sodium ions collapses the electrostatic double layer, forcing soap molecules out of solution via the **salting-out effect**."""
                },
                {
                    "id": "sec-5-4",
                    "secNumber": "5.4",
                    "title": "Glycerol Recovery, Concentration & Multi-Effect Vacuum Distillation",
                    "content": r"""Glycerol (propane-1,2,3-triol, $\text{CH}_2\text{OH}-\text{CHOH}-\text{CH}_2\text{OH}$, $M = 92.09\text{ g/mol}$) is the principal high-value byproduct of soap manufacturing, representing approximately $10 - 11\text{ wt}\%$ of the starting neutral triglyceride mass.

### 1. Spent Lye Chemical Treatment
Crude spent lye discharged from the graining and washing stages contains $8 - 15\text{ wt}\%\text{ glycerol}$, $8 - 12\text{ wt}\%\text{ NaCl}$, $0.2 - 0.5\text{ wt}\%$ dissolved soap, and suspended proteinaceous impurities:
1. **Acidification & Flocculation**: The alkaline lye is neutralized with hydrochloric acid ($\text{HCl}$) or sulfuric acid to $\text{pH } 4.5 - 5.0$, converting dissolved sodium soap into insoluble free fatty acid scum.
2. **Coagulation**: Aluminum sulfate ($\text{Al}_2(\text{SO}_4)_3$) or iron(III) chloride ($\text{FeCl}_3$) is added. Insoluble aluminum hydroxide / basic iron soaps precipitate, sweeping out colloidal impurities and coloring matter:
   $$\text{Al}^{3+} + 3\text{OH}^- \longrightarrow \text{Al(OH)}_3 \downarrow$$
3. **Plate-and-Frame Filtration**: The precipitated floc is filtered, yielding a sparkling clear, pale-amber treated lye.

### 2. Multi-Effect Evaporation & Salt Separation
The treated lye is concentrated in a double- or triple-effect forced-circulation evaporator under vacuum:
- As water evaporates, the solubility limit of sodium chloride in aqueous glycerol is exceeded, causing salt crystals to precipitate vigorously.
- The evaporator bottoms pass through continuous conical salt catchers and centrifuges, recovering dry $\text{NaCl}$ cake that is recycled back to the soap graining kettles.
- Evaporation continues until the liquid reaches **$80 - 88\text{ wt}\%$ glycerol** (known as **Crude Soap-Lye Glycerin**), with specific gravity $\approx 1.25\text{ g/cm}^3$.

### 3. High-Vacuum Flash Distillation & Decolorization
Because glycerol decomposes thermally at its atmospheric boiling point ($290^\circ\text{C}$) to form toxic acrolein ($\text{CH}_2\text{=CH-CHO}$):
$$\text{C}_3\text{H}_8\text{O}_3 \overset{\Delta}{\longrightarrow} \text{CH}_2\text{=CH-CHO} + 2\text{H}_2\text{O}$$
purification must be executed under deep vacuum ($5 - 10\text{ mbar}$, $160 - 180^\circ\text{C}$) in a packed distillation column with direct steam injection. The distilled glycerol is condensed, deodorized, and percolated through activated carbon beds, producing **$99.5 - 99.8\%$ USP / Chemically Pure (CP) Glycerol**."""
                },
                {
                    "id": "sec-5-5",
                    "secNumber": "5.5",
                    "title": "Soap Finishing Engineering: Vacuum Spray Drying, Milling, Extrusion & Plodding",
                    "content": r"""Molten neat soap leaving the continuous saponification plant at $65 - 70\text{ wt}\%$ fatty acid salt and $30 - 35\text{ wt}\%$ water must be dried, blended, homogenized, and compacted into solid consumer toilet soap bars containing $12 - 14\text{ wt}\%$ moisture.

```
                     MAZZONI SOAP FINISHING LINE
  Neat Soap (~90°C)
       │
       ▼
  ┌──────────────┐
  │ Heat Exch.   │ (Preheat to 130-140°C under pressure)
  └──────┬───────┘
         ▼
  ┌──────────────────────┐
  │ VACUUM SPRAY DRYER   │ <── Vacuum (~30-40 mbar)
  │ (Rotating Scrapers)  │     Water flashes into vapor!
  └──────────┬───────────┘
             ▼ Soap Noodles (~12-14% H2O, ~40°C)
  ┌──────────────────────┐
  │ AMALGAMATOR / MIXER  │ <── Perfume (1%), Dyes (0.1%), Titanium Dioxide (TiO2)
  └──────────┬───────────┘
             ▼
  ┌──────────────────────┐
  │ THREE-ROLL MILL      │ (High-shear refining: orienting crystal phase)
  └──────────┬───────────┘
             ▼
  ┌──────────────────────┐
  │ TWO-STAGE DUPLEX     │ ── Stage 1: Shredder & Vacuum Deaeration
  │ VACUUM PLODDER       │ ── Stage 2: Extrusion Screw through Heated Die
  └──────────┬───────────┘
             ▼ Continuous Dense Soap Billet
  ┌──────────────────────┐
  │ CUTTER & STAMPER     │ ──> Branded Finished Toilet Soap Bars!
  └──────────────────────┘
```

### 1. Vacuum Spray Drying (Mazzoni Process)
Neat soap is heated under pressure to $130 - 140^\circ\text{C}$ in a shell-and-tube heat exchanger and sprayed through rotating atomizing nozzles into an evacuated chamber ($30 - 50\text{ mbar}$). Water flashes off instantly as vapor, cooling the falling soap particles to $35 - 40^\circ\text{C}$. Rotating internal scraper blades sweep the semi-solid soap flakes from the chamber walls down into an discharge vacuum plodder, forming soap "noodles."

### 2. High-Shear Milling & Phase Inversion
In toilet soap manufacture, the noodles are blended with fragrances ($0.5 - 1.5\%$), optical brighteners, preservatives (BHT, EDTA), and opacifiers ($\text{TiO}_2$) in an amalgamator, then passed through chilled **three-roll mills** running at differential speeds ($1:2:4$). The intense compressive shear forces convert the fragile, coarse **$\omega$-phase** and **$\delta$-phase** soap crystals into the ductile, silky, lather-rich **$\beta$-phase** crystal polymorph.

### 3. Duplex Vacuum Plodding & Extrusion
The milled soap enters a two-stage plodder equipped with an intermediate vacuum chamber. Trapped air bubbles are evacuated under $20\text{ mbar}$ vacuum (preventing internal fissure voids and cracking). A motorized extrusion auger compresses the soap under $30 - 50\text{ bar}$ through a heated nozzle die ($45 - 55^\circ\text{C}$), producing a continuous, glassy, dense billet that is cut and pressed into bars."""
                },
                {
                    "id": "sec-5-6",
                    "secNumber": "5.6",
                    "title": "Synthetic Surfactants: Classification & Linear Alkylbenzene Sulfonate (LABS) Manufacture",
                    "content": r"""Surfactants (Surface Active Agents) are amphiphilic molecules possessing a hydrophobic non-polar hydrocarbon tail and a hydrophilic polar head.

### Classification of Surfactants
1. **Anionic**: Hydrophilic head bears a negative net charge in aqueous solution:
   - Linear Alkylbenzene Sulfonates ($\text{LABS}$, $\text{R-C}_6\text{H}_4-\text{SO}_3^-\text{Na}^+$).
   - Sodium Lauryl Ether Sulfate ($\text{SLES}$, $\text{CH}_3(\text{CH}_2)_{11}(\text{OCH}_2\text{CH}_2)_n\text{OSO}_3^-\text{Na}^+$).
   - Primary Alkyl Sulfates ($\text{SLS}$, $\text{C}_{12}\text{H}_{25}\text{OSO}_3^-\text{Na}^+$).
2. **Nonionic**: Hydrophilic head possesses no electrical charge; water solubility arises from hydrogen bonding with polyether dipoles:
   - Alcohol Ethoxylates ($\text{AEO}$, $\text{R-O-(CH}_2\text{CH}_2\text{O)}_n\text{H}$, $n = 7 - 9$).
   - Alkylpolyglucosides ($\text{APG}$, renewable sugar surfactants).
3. **Cationic**: Hydrophilic head carries a net positive charge (used in fabric softeners and disinfectants):
   - Quaternary Ammonium Chlorides (e.g., Cetyltrimethylammonium bromide, $\text{CTAB}$).
4. **Zwitterionic / Amphoteric**: Bears both positive and negative charges depending on solution $\text{pH}$:
   - Cocamidopropyl Betaine ($\text{CAPB}$, used in mild baby shampoos).

### Linear Alkylbenzene Sulfonation (LABS) Engineering
The dominant synthetic surfactant worldwide is Sodium Linear Alkylbenzene Sulfonate ($\text{NaLAS}$), synthesized by reacting linear alkylbenzene ($\text{LAB}$, alkyl chain $\text{C}_{10} - \text{C}_{13}$, average $M \approx 240\text{ g/mol}$) with gaseous sulfur trioxide ($\text{SO}_3$):

```
             C12H25                                C12H25
               │                                     │
             ┌─┴─┐                                 ┌─┴─┐
            ╱     ╲    +   SO3 (gas)     ──>      ╱     ╲
            │     │    (diluted in dry air)        │     │
            ╲     ╱                                ╲     ╱
             └───┘                                  └───┘
                                                      │
                                                     SO3H  (LABSA)
```

### Falling Film Reactor Technology
The sulfonation reaction is violently exothermic ($\Delta H_{\text{rxn}} = -170\text{ kJ/mol}$) and instantaneous:
$$\text{LAB} + \text{SO}_3 \longrightarrow \text{LABSA} \quad (\Delta H = -170\text{ kJ/mol})$$
To prevent localized charring, darkening, and dialkyl sulfone byproduct formation, the reaction is conducted in a **multi-tube falling film reactor** (e.g., Ballestra Multitube or Desmet Chemithon):
- Pure $\text{LAB}$ flows down the inner walls of vertical stainless steel tubes ($6\text{ m}$ length) as an ultra-thin liquid film ($0.1 - 0.2\text{ mm}$ thickness).
- Dry gaseous $\text{SO}_3$ diluted to $4 - 5\text{ vol}\%$ in refrigerated, bone-dry air (dew point $< -60^\circ\text{C}$) enters co-currently at high linear velocity ($30 - 40\text{ m/s}$).
- Chilled cooling water circulating in the reactor shell maintains film temperature at $45 - 55^\circ\text{C}$.
- The acid effluent enters a continuous neutralizer with aqueous $\text{NaOH}$:
  $$\text{R-C}_6\text{H}_4-\text{SO}_3\text{H} + \text{NaOH} \longrightarrow \text{R-C}_6\text{H}_4-\text{SO}_3^-\text{Na}^+ + \text{H}_2\text{O}$$
yielding a straw-yellow, highly active surfactant paste ($70\text{ wt}\%\text{ NaLAS}$)."""
                },
                {
                    "id": "sec-5-7",
                    "secNumber": "5.7",
                    "title": "Detergent Builders, Formulations & Environmental Eutrophication / Biodegradability",
                    "content": r"""A heavy-duty laundry detergent powder or liquid is a sophisticated multi-component chemical formulation where surfactants represent only $15 - 25\%$ of the total formulation. The bulk of the performance is contributed by **builders**, **chelating agents**, **bleaching systems**, and **functional additives**.

### Role and Classification of Detergent Builders
Water hardness ions ($\text{Ca}^{2+}$ and $\text{Mg}^{2+}$) precipitate anionic surfactants as insoluble lime scum, completely destroying foaming and detergency:
$$2\text{R-SO}_3^-\text{Na}^+ + \text{Ca}^{2+} \longrightarrow (\text{R-SO}_3)_2\text{Ca} \downarrow + 2\text{Na}^+$$
Builders sequester hardness cations, provide alkaline buffering ($\text{pH } 9.5 - 10.5$), disperse soil particles, and prevent soil redeposition:
1. **Sodium Tripolyphosphate ($\text{STPP}$, $\text{Na}_5\text{P}_3\text{O}_{10}$)**:
   Historically the most effective builder, forming soluble hexadentate chelation complexes:
   $$\text{P}_3\text{O}_{10}^{5-} + \text{Ca}^{2+} \rightleftharpoons [\text{Ca}(\text{P}_3\text{O}_{10})]^{3-}$$
2. **Zeolite A (Sodium Aluminosilicate, $\text{Na}_{12}(\text{AlO}_2)_{12}(\text{SiO}_2)_{12}\cdot 27\text{H}_2\text{O}$)**:
   Insoluble microporous cage with a pore aperture of $4.2\text{ \AA}$, engineered to exchange internal $\text{Na}^+$ ions for external $\text{Ca}^{2+}$ ions via ion-exchange kinetics.
3. **Polycarboxylates & Citrates**:
   Copolymers of acrylic and maleic acid ($M_w \approx 4,000 - 10,000\text{ g/mol}$) act as threshold anti-incrustation crystal growth inhibitors.
4. **Sodium Carbonate (Soda Ash, $\text{Na}_2\text{CO}_3$) & Sodium Silicate ($\text{Na}_2\text{O}\cdot 2\text{SiO}_2$)**:
   Provide alkaline buffering, prevent machine corrosion, and enhance powder granule crispness.

### Environmental Eutrophication & Phosphorus Bans
Excessive discharge of phosphate-rich laundry effluents into freshwater bodies causes **eutrophication**:
- Phosphorus is the limiting macronutrient in freshwater aquatic ecosystems. High phosphate runoff triggers catastrophic algal blooms (cyanobacteria).
- As algae die, aerobic heterotrophic bacteria decompose the biomass, consuming dissolved oxygen:
  $$\text{Biomass} + \text{O}_2 \longrightarrow \text{CO}_2 + \text{H}_2\text{O} \quad (\text{Hypoxia/Anoxia})$$
- Massive fish kills and dead zones result. Consequently, global regulations have mandated zero-phosphate laundry powders, replacing $\text{STPP}$ with Zeolite A / polycarboxylate / soda ash combinations.

### Surfactant Biodegradability: Linear vs Branched Chains
In the 1960s, early synthetic detergents formulated with Branched Alkylbenzene Sulfonate (tetrapropylene benzene sulfonate, TPBS) caused massive persistent white foam banks across rivers and sewage treatment facilities:
- Tertiary carbon branch points ($\text{-C(CH}_3)_2\text{-}$) physically block microbial $\beta$-oxidation enzymes.
- Modern environmental regulations mandate **Linear Alkylbenzene Sulfonates (LAS)**, which undergo complete primary microbial degradation ($> 99\%$ within 7 days) via sequential $\omega$-oxidation followed by $\beta$-oxidation."""
                }
            ],
            "problems": [
                {
                    "id": "prob-5-1",
                    "problemNumber": "5.1",
                    "title": "Saponification Value & Theoretical Glycerol Yield of Triglycerides",
                    "difficulty": "Easy",
                    "statement": r"""A soap manufacturer analyzes a blended fat charge consisting of $80.0\text{ wt}\%$ beef tallow and $20.0\text{ wt}\%$ coconut oil.
- Beef tallow has an average Saponification Value ($\text{SV}$) of $198.0\text{ mg KOH / g fat}$.
- Coconut oil has an average Saponification Value of $255.0\text{ mg KOH / g fat}$.
Molar masses: $\text{KOH} = 56.11\text{ g/mol}$, $\text{NaOH} = 40.00\text{ g/mol}$, $\text{Glycerol} = 92.09\text{ g/mol}$.
1. Calculate the weighted Saponification Value of the blended fat.
2. Determine the mass of pure sodium hydroxide ($\text{NaOH}$) required to completely saponify $50.0\text{ metric tons}$ of this fat blend.
3. Calculate the theoretical yield of glycerol produced in metric tons.""",
                    "solution": r"""### Step 1: Weighted Saponification Value
$$\text{SV}_{\text{blend}} = 0.80 \times 198.0 + 0.20 \times 255.0 = 158.4 + 51.0 = 209.4\text{ mg KOH / g fat}$$

### Step 2: Mass of $\text{NaOH}$ Required
Conversion from $\text{KOH}$ to $\text{NaOH}$ stoichiometry:
$$\text{Mass ratio } \frac{\text{NaOH}}{\text{KOH}} = \frac{40.00}{56.11} = 0.71289$$
Specific $\text{NaOH}$ consumption:
$$\text{NaOH factor} = 209.4\text{ mg KOH / g fat} \times 0.71289\text{ mg NaOH / mg KOH} = 149.28\text{ mg NaOH / g fat} = 0.14928\text{ kg NaOH / kg fat}$$
Total pure $\text{NaOH}$ required for $50.0\text{ metric tons}$ ($50,000\text{ kg}$) of fat:
$$m_{\text{NaOH}} = 50,000\text{ kg} \times 0.14928 = 7,464.0\text{ kg} \approx 7.464\text{ metric tons}$$

### Step 3: Theoretical Glycerol Yield
Every $3\text{ moles of KOH}$ ($3 \times 56.11 = 168.33\text{ g KOH}$) correspond to the saponification of 1 triglyceride molecule and liberation of $1\text{ mole of glycerol}$ ($92.09\text{ g}$):
$$\text{Glycerol yield per g KOH} = \frac{92.09}{168.33} = 0.54708\text{ g glycerol / g KOH}$$
Total $\text{KOH}$ equivalent for $50,000\text{ kg}$ fat:
$$m_{\text{KOH equiv}} = 50,000\text{ kg} \times 0.2094\text{ kg KOH / kg fat} = 10,470\text{ kg KOH}$$
Theoretical glycerol yield:
$$m_{\text{glycerol}} = 10,470\text{ kg KOH} \times 0.54708 = 5,727.9\text{ kg} \approx 5.728\text{ metric tons}$$

The reaction requires **$7.464\text{ metric tons}$ of $\text{NaOH}$** and yields **$5.728\text{ metric tons}$ of glycerol** ($11.46\text{ wt}\%$ of fat mass).""",
                    "hints": ["Multiply KOH saponification value by ratio 40.00/56.11 for NaOH.", "3 moles of alkali liberate 1 mole of glycerol."]
                },
                {
                    "id": "prob-5-2",
                    "problemNumber": "5.2",
                    "title": "Continuous Saponification CSTR Material Balance & Residence Time",
                    "difficulty": "Medium",
                    "statement": r"""A continuous Mazzoni saponification reactor operates at steady state at $125^\circ\text{C}$ and $4.0\text{ bar}$.
- Fat feed rate is $\dot{m}_{\text{fat}} = 6,000\text{ kg/h}$ (average molar mass of triglyceride $\bar{M}_{\text{TG}} = 860\text{ g/mol}$).
- Aqueous sodium hydroxide ($48.0\text{ wt}\%\text{ NaOH}$, density $\rho = 1.51\text{ g/cm}^3$) is fed at a $2.0\%$ stoichiometric excess.
- Water/brine recycle is adjusted so that the exiting crude neat soap emulsion contains $32.0\text{ wt}\%\text{ water}$.
- Saponification conversion is $99.5\%$.
- Effective liquid reaction volume inside the agitated reactor is $V = 3.50\text{ m}^3$, and average emulsion density is $\rho_{\text{emulsion}} = 980\text{ kg/m}^3$.

1. Calculate the required mass feed rate of $48.0\text{ wt}\%\text{ NaOH}$ solution in $\text{kg/h}$.
2. Determine the mean hydrodynamic residence time ($\tau$) of the reactor in minutes.
3. Calculate the neat soap production rate in metric tons per hour.""",
                    "solution": r"""### Step 1: Caustic Soda Feed Rate
Moles of triglyceride fed per hour:
$$\dot{n}_{\text{TG}} = \frac{6,000 \times 10^3\text{ g/h}}{860\text{ g/mol}} = 6,976.7\text{ mol/h}$$
Theoretical moles of $\text{NaOH}$ required ($3\text{ mol NaOH / mol TG}$):
$$\dot{n}_{\text{NaOH, theo}} = 3 \times 6,976.7 = 20,930.2\text{ mol/h}$$
With $2.0\%$ stoichiometric excess ($1.02\times$):
$$\dot{n}_{\text{NaOH, actual}} = 1.02 \times 20,930.2 = 21,348.8\text{ mol/h}$$
Mass of pure $\text{NaOH}$ ($40.00\text{ g/mol}$):
$$\dot{m}_{\text{NaOH, pure}} = 21,348.8\text{ mol/h} \times 40.00\text{ g/mol} = 853.95\text{ kg/h}$$
Mass feed rate of $48.0\text{ wt}\%$ caustic solution:
$$\dot{m}_{\text{caustic sol}} = \frac{853.95\text{ kg/h}}{0.480} = 1,779.06\text{ kg/h} \approx 1,779.1\text{ kg/h}$$

### Step 2: Mean Residence Time ($\tau$)
Total mass holdup inside the reactor:
$$M_{\text{reactor}} = V \times \rho_{\text{emulsion}} = 3.50\text{ m}^3 \times 980\text{ kg/m}^3 = 3,430\text{ kg}$$
To calculate total mass throughput, let us sum inputs.
Total dry solids (fat + pure NaOH excess):
Fat: $6,000\text{ kg/h}$. Saponification consumes fat and NaOH to yield soap ($6,350\text{ kg/h}$) and glycerol ($642\text{ kg/h}$), totaling $6,992\text{ kg/h}$ reaction mass + excess NaOH ($17\text{ kg/h}$) $= 7,009\text{ kg/h}$ dry organics/salts.
If the emulsion is adjusted to $32.0\text{ wt}\%\text{ moisture}$, dry solids represent $68.0\text{ wt}\%$:
$$\dot{m}_{\text{total emulsion}} = \frac{7,009\text{ kg/h}}{0.680} \approx 10,307\text{ kg/h}$$
Mean hydrodynamic residence time:
$$\tau = \frac{M_{\text{reactor}}}{\dot{m}_{\text{total emulsion}}} = \frac{3,430\text{ kg}}{10,307\text{ kg/h}} = 0.3328\text{ h} \approx 19.97\text{ minutes}$$
The mean residence time is **$20.0\text{ minutes}$**.

### Step 3: Neat Soap Production Rate
The reactor continuously yields **$10.31\text{ metric tons/h}$** of neat soap emulsion.""",
                    "hints": ["Calculate moles of fat, multiply by 3, apply the 1.02 excess factor.", "Residence time tau = holdup mass / mass flow rate."]
                },
                {
                    "id": "prob-5-3",
                    "problemNumber": "5.3",
                    "title": "Ternary Phase Split: Neat Soap vs Nigre Gravimetric Balance",
                    "difficulty": "Hard",
                    "statement": r"""In a soap kettle finishing (fitting) operation, $40.0\text{ metric tons}$ of grained soap curd is adjusted with water and salt at $95^\circ\text{C}$ to induce phase splitting into upper Neat Soap and lower Nigre.
Analytical composition of the total fitted kettle contents:
- Total Soap ($S$): $54.0\text{ wt}\%$
- Electrolyte ($\text{NaCl}$): $0.90\text{ wt}\%$
- Water ($W$): $45.10\text{ wt}\%$

At $95^\circ\text{C}$, the equilibrium phase boundaries determine that:
- **Neat Soap Phase** contains: $66.0\text{ wt}\%\text{ Soap}$, $0.50\text{ wt}\%\text{ NaCl}$, $33.50\text{ wt}\%\text{ Water}$.
- **Nigre Phase** contains: $34.0\text{ wt}\%\text{ Soap}$, $1.56\text{ wt}\%\text{ NaCl}$, $64.44\text{ wt}\%\text{ Water}$.

1. Apply the lever rule across the soap balance to determine the mass of Neat Soap and Nigre produced in metric tons.
2. Verify the mass conservation of $\text{NaCl}$ and Water across the two phases.
3. Calculate the percentage of total fatty matter recovered in the purified Neat Soap layer.""",
                    "solution": r"""### Step 1: Mass Balance via Lever Rule
Let $m_N$ be the mass of Neat Soap and $m_g$ be the mass of Nigre.
Total mass balance:
$$m_N + m_g = 40.0\text{ metric tons}$$
Total Soap mass balance:
$$0.660 \cdot m_N + 0.340 \cdot m_g = 0.540 \times 40.0 = 21.60\text{ metric tons}$$
Substitute $m_g = 40.0 - m_N$:
$$0.660 \cdot m_N + 0.340(40.0 - m_N) = 21.60$$
$$0.660 \cdot m_N + 13.60 - 0.340 \cdot m_N = 21.60$$
$$0.320 \cdot m_N = 21.60 - 13.60 = 8.00$$
$$m_N = \frac{8.00}{0.320} = 25.00\text{ metric tons}$$
$$m_g = 40.00 - 25.00 = 15.00\text{ metric tons}$$

The kettle yields **$25.0\text{ metric tons}$ of Neat Soap** and **$15.0\text{ metric tons}$ of Nigre**.

### Step 2: Verification of Electrolyte & Water Balances
- **$\text{NaCl}$ Balance**:
  - Total in kettle $= 0.0090 \times 40.0 = 0.360\text{ tons}$
  - In Neat Soap $= 0.0050 \times 25.00 = 0.125\text{ tons}$
  - In Nigre $= 0.0156 \times 15.00 = 0.234\text{ tons}$
  - Sum $= 0.125 + 0.234 = 0.359\text{ tons} \approx 0.360\text{ tons}$ (Check!)
- **Water Balance**:
  - Total in kettle $= 0.4510 \times 40.0 = 18.04\text{ tons}$
  - In Neat Soap $= 0.3350 \times 25.00 = 8.375\text{ tons}$
  - In Nigre $= 0.6444 \times 15.00 = 9.666\text{ tons}$
  - Sum $= 8.375 + 9.666 = 18.041\text{ tons} \approx 18.04\text{ tons}$ (Check!)

### Step 3: Fatty Matter Recovery
Soap recovered in Neat Soap:
$$m_{\text{soap, neat}} = 0.660 \times 25.0 = 16.50\text{ metric tons}$$
$$\% \text{ Recovery} = \frac{16.50\text{ t}}{21.60\text{ t}} \times 100\% = 76.39\%$$

**$76.4\%$** of the total soap is harvested as pure Neat Soap; the remaining $23.6\%$ in the Nigre is recycled to the next boiling cycle.""",
                    "hints": ["Set up simultaneous equations for total mass and soap mass.", "Verify using NaCl and water balances."]
                },
                {
                    "id": "prob-5-4",
                    "problemNumber": "5.4",
                    "title": "Glycerol Triple-Effect Evaporator & Salt Crystallization Balance",
                    "difficulty": "Hard",
                    "statement": r"""A spent lye treatment plant feeds $\dot{m}_{\text{feed}} = 20,000\text{ kg/h}$ of treated dilute lye into a triple-effect evaporator.
- Feed composition: $10.0\text{ wt}\%\text{ glycerol}$, $10.0\text{ wt}\%\text{ NaCl}$, and $80.0\text{ wt}\%\text{ water}$.
- Product concentrated crude glycerin: $82.0\text{ wt}\%\text{ glycerol}$, $8.0\text{ wt}\%\text{ NaCl}$, and $10.0\text{ wt}\%\text{ water}$.
- Crystalline $\text{NaCl}$ salt cake discharged from the salt catchers is $96.0\text{ wt}\%\text{ pure NaCl}$ and $4.0\text{ wt}\%\text{ entrained brine}$ (assume entrained brine has the product composition: $82\%$ glycerol, $8\%$ salt, $10\%$ water).
Assume zero glycerol loss in overhead condensates.

1. Calculate the production rate of concentrated crude glycerin ($\text{kg/h}$).
2. Calculate the mass of dry crystallized $\text{NaCl}$ recovered per hour.
3. Determine the total water evaporation rate ($\text{kg/h}$) and the steam economy if the triple-effect evaporator consumes $5,400\text{ kg/h}$ of live motive steam.""",
                    "solution": r"""### Step 1: Glycerol Mass Balance & Production Rates
Glycerol entering in feed:
$$\dot{m}_{\text{gly, in}} = 0.100 \times 20,000\text{ kg/h} = 2,000\text{ kg/h}$$
Salt entering in feed:
$$\dot{m}_{\text{salt, in}} = 0.100 \times 20,000\text{ kg/h} = 2,000\text{ kg/h}$$
Water entering in feed:
$$\dot{m}_{\text{water, in}} = 0.800 \times 20,000\text{ kg/h} = 16,000\text{ kg/h}$$

Let $P$ be the crude glycerin product rate ($\text{kg/h}$) and $S_c$ be the salt cake discharge rate ($\text{kg/h}$).
The salt cake contains:
- Pure crystallized $\text{NaCl}$: $0.96 \cdot S_c$
- Entrained liquid: $0.04 \cdot S_c$ (which has $82\%$ glycerol, $8\%$ salt, $10\%$ water)
Total glycerol leaving the system is in $P$ and in the entrained liquid of $S_c$:
$$\dot{m}_{\text{gly, out}} = 0.82 \cdot P + 0.82(0.04 \cdot S_c) = 0.82(P + 0.04 S_c) = 2,000\text{ kg/h}$$
$$P + 0.04 S_c = \frac{2,000}{0.82} = 2,439.02\text{ kg/h} \quad \text{--- (Eq. 1)}$$

Now write the total salt balance:
$$\dot{m}_{\text{salt, out}} = 0.08 \cdot P + \left[0.96 \cdot S_c + 0.08(0.04 \cdot S_c)\right] = 2,000\text{ kg/h}$$
$$0.08 \cdot P + (0.96 + 0.0032) S_c = 2,000$$
$$0.08 \cdot P + 0.9632 \cdot S_c = 2,000 \quad \text{--- (Eq. 2)}$$

From Eq. 1: $P = 2,439.02 - 0.04 S_c$. Substitute into Eq. 2:
$$0.08(2,439.02 - 0.04 S_c) + 0.9632 S_c = 2,000$$
$$195.12 - 0.0032 S_c + 0.9632 S_c = 2,000$$
$$0.9600 \cdot S_c = 2,000 - 195.12 = 1,804.88$$
$$S_c = \frac{1,804.88}{0.9600} = 1,880.08\text{ kg/h}$$
Now compute $P$:
$$P = 2,439.02 - 0.04(1,880.08) = 2,439.02 - 75.20 = 2,363.82\text{ kg/h}$$

- Crude glycerin product rate $= \mathbf{2,363.8\text{ kg/h}}$.
- Salt cake discharge rate $= \mathbf{1,880.1\text{ kg/h}}$ (containing $1,804.9\text{ kg/h}$ pure crystal $\text{NaCl}$).

### Step 2: Water Evaporation Rate & Steam Economy
Water leaving in product $P$:
$$\dot{m}_{\text{water, } P} = 0.10 \times 2,363.82 = 236.38\text{ kg/h}$$
Water leaving in salt cake:
$$\dot{m}_{\text{water, } S_c} = 0.10(0.04 \times 1,880.08) = 7.52\text{ kg/h}$$
Total water leaving as liquid $= 236.38 + 7.52 = 243.90\text{ kg/h}$.
Total water evaporated as steam ($V$):
$$V = \dot{m}_{\text{water, in}} - \dot{m}_{\text{water, liquid}} = 16,000.0 - 243.9 = 15,756.1\text{ kg/h}$$

Steam Economy:
$$\text{Steam Economy} = \frac{\text{Mass of water evaporated}}{\text{Mass of motive steam supplied}} = \frac{15,756.1\text{ kg/h}}{5,400.0\text{ kg/h}} = 2.918 \approx 2.92$$
The evaporator achieves a steam economy of **$2.92\text{ kg vapor / kg steam}$**, perfectly consistent with a triple-effect system.""",
                    "hints": ["Write simultaneous balances for glycerol and salt.", "Steam economy is total evaporated water divided by live motive steam."]
                },
                {
                    "id": "prob-5-5",
                    "problemNumber": "5.5",
                    "title": "Linear Alkylbenzene Sulfonation Kinetics & Falling Film Reactor",
                    "difficulty": "Medium",
                    "statement": r"""A continuous falling film sulfonation reactor synthesizes linear alkylbenzene sulfonic acid ($\text{LABSA}$) from $\text{LAB}$ ($M_{\text{LAB}} = 240.4\text{ g/mol}$) and dry gaseous $\text{SO}_3$ ($M_{\text{SO}_3} = 80.06\text{ g/mol}$).
$$\text{LAB} + \text{SO}_3 \longrightarrow \text{LABSA} \quad (M_{\text{LABSA}} = 320.46\text{ g/mol}) \quad \Delta H_{\text{rxn}} = -170.0\text{ kJ/mol}$$
- Plant production rate of pure active $\text{LABSA}$ is $4,000\text{ kg/h}$.
- $\text{LAB}$ conversion is $98.5\%$.
- A stoichiometric molar ratio of $\text{SO}_3 : \text{LAB} = 1.04 : 1.00$ is supplied.
- $\text{SO}_3$ gas is diluted to $4.50\text{ vol}\%$ in dry air at $1.20\text{ bar}$ absolute and $40^\circ\text{C}$.
- Cooling water in the reactor jacket enters at $22^\circ\text{C}$ and exits at $32^\circ\text{C}$ ($c_p = 4.184\text{ kJ/(kg}\cdot\text{K)}$).

1. Calculate the required mass feed rate of $\text{LAB}$ in $\text{kg/h}$.
2. Determine the volumetric flow rate of the $\text{SO}_3$-air process gas mixture at entry conditions in $\text{Nm}^3\text{/h}$ and actual $\text{m}^3\text{/h}$.
3. Calculate the total heat generated by the sulfonation reaction ($\text{kW}$) and the required cooling water flow rate in $\text{m}^3\text{/h}$.""",
                    "solution": r"""### Step 1: $\text{LAB}$ Feed Rate
Moles of active $\text{LABSA}$ produced per hour:
$$\dot{n}_{\text{LABSA}} = \frac{4,000 \times 10^3\text{ g/h}}{320.46\text{ g/mol}} = 12,482.06\text{ mol/h}$$
At $98.5\%$ conversion, moles of $\text{LAB}$ fed:
$$\dot{n}_{\text{LAB}} = \frac{12,482.06\text{ mol/h}}{0.985} = 12,672.14\text{ mol/h}$$
Mass feed rate of $\text{LAB}$:
$$\dot{m}_{\text{LAB}} = 12,672.14\text{ mol/h} \times 240.4\text{ g/mol} = 3,046,382\text{ g/h} \approx 3,046.4\text{ kg/h}$$

### Step 2: $\text{SO}_3$-Air Volumetric Flow Rate
Moles of $\text{SO}_3$ supplied ($1.04\times \text{LAB}$):
$$\dot{n}_{\text{SO}_3} = 1.04 \times 12,672.14 = 13,179.03\text{ mol/h}$$
At standard temperature and pressure ($0^\circ\text{C}$, $1\text{ atm}$, $22.414\text{ Nm}^3\text{/kmol}$):
$$\dot{V}_{\text{SO}_3, \text{STP}} = 13.179\text{ kmol/h} \times 22.414\text{ Nm}^3\text{/kmol} = 295.40\text{ Nm}^3\text{/h}$$
Since $\text{SO}_3$ is $4.50\text{ vol}\%$ of the dry air mixture:
$$\dot{V}_{\text{gas, STP}} = \frac{295.40\text{ Nm}^3\text{/h}}{0.0450} = 6,564.44\text{ Nm}^3\text{/h}$$

Actual volumetric flow rate at $T = 40^\circ\text{C} = 313.15\text{ K}$ and $P = 1.20\text{ bar} = 1.1843\text{ atm}$:
$$\dot{V}_{\text{actual}} = \dot{V}_{\text{STP}} \times \left(\frac{T}{273.15}\right) \times \left(\frac{1.000}{P}\right)$$
$$\dot{V}_{\text{actual}} = 6,564.44 \times \left(\frac{313.15}{273.15}\right) \times \left(\frac{1.00}{1.1843}\right) = 6,564.44 \times 1.1464 \times 0.8444 = 6,354.7\text{ m}^3\text{/h}$$

### Step 3: Reaction Enthalpy & Cooling Water Flow
Rate of $\text{LABSA}$ formation is $12,482.06\text{ mol/h}$:
$$\dot{Q}_{\text{rxn}} = 12,482.06\text{ mol/h} \times 170.0\text{ kJ/mol} = 2.12195 \times 10^6\text{ kJ/h}$$
Converting to thermal power ($\text{kW}$):
$$\dot{Q}_{\text{thermal}} = \frac{2.12195 \times 10^6\text{ kJ/h}}{3,600\text{ s/h}} = 589.43\text{ kW}$$
Cooling water flow rate ($\Delta T = 32 - 22 = 10\text{ K}$):
$$\dot{m}_{\text{water}} = \frac{\dot{Q}_{\text{rxn}}}{c_p \cdot \Delta T} = \frac{2.12195 \times 10^6\text{ kJ/h}}{4.184\text{ kJ/(kg}\cdot\text{K)} \times 10\text{ K}} = 50,715.8\text{ kg/h} \approx 50.72\text{ m}^3\text{/h}$$

The reactor generates **$589.4\text{ kW}$** of thermal heat, removed by **$50.7\text{ m}^3\text{/h}$** of cooling water.""",
                    "hints": ["Compute moles of active acid, apply conversion to get LAB feed.", "Ideal gas law converts moles to actual cubic meters."]
                },
                {
                    "id": "prob-5-6",
                    "problemNumber": "5.6",
                    "title": "Total Fatty Matter (TFM) and Free Caustic Alkali Determination",
                    "difficulty": "Easy",
                    "statement": r"""A quality control chemist analyzes a commercial laundry soap bar:
1. **Total Fatty Matter (TFM)**: A $5.000\text{ g}$ soap sample is dissolved in hot distilled water, acidified with $25.0\text{ mL}$ of $2.00\text{ M HCl}$ to liberate free fatty acids, and extracted with petroleum ether. The ether extract is dried and evaporated, yielding $3.820\text{ g}$ of fatty acids.
2. **Free Caustic Alkali**: A separate $10.000\text{ g}$ soap sample is dissolved in neutralized absolute ethanol. Barium chloride solution is added to precipitate carbonates. The filtered solution requires $2.40\text{ mL}$ of $0.100\text{ M HCl}$ to reach the phenolphthalein end point.
Molar mass: $\text{NaOH} = 40.00\text{ g/mol}$.

1. Calculate the percentage of Total Fatty Matter ($\text{TFM}$) in the soap bar.
2. Calculate the mass percentage of Free Caustic Alkali expressed as $\% \text{NaOH}$.
3. Based on BIS/ISO standard specifications (Grade 1 toilet soap requires $\text{TFM} \ge 76.0\%$, Free Caustic $\le 0.05\%$; Grade 3 laundry soap requires $\text{TFM} \ge 60.0\%$, Free Caustic $\le 0.10\%$), classify the soap grade.""",
                    "solution": r"""### Step 1: Total Fatty Matter ($\text{TFM}$)
$$\% \text{TFM} = \frac{\text{Mass of extracted fatty acids}}{\text{Mass of soap sample}} \times 100\%$$
$$\% \text{TFM} = \frac{3.820\text{ g}}{5.000\text{ g}} \times 100\% = 76.40\%$$

### Step 2: Free Caustic Alkali Calculation
Moles of $\text{HCl}$ consumed:
$$n_{\text{HCl}} = 2.40 \times 10^{-3}\text{ L} \times 0.100\text{ mol/L} = 2.40 \times 10^{-4}\text{ mol}$$
Equivalent mass of free $\text{NaOH}$:
$$m_{\text{NaOH}} = 2.40 \times 10^{-4}\text{ mol} \times 40.00\text{ g/mol} = 9.60 \times 10^{-3}\text{ g} = 9.60\text{ mg}$$
Mass percentage of Free Caustic Alkali:
$$\% \text{ Free Caustic NaOH} = \frac{9.60 \times 10^{-3}\text{ g}}{10.000\text{ g}} \times 100\% = 0.096\%$$

### Step 3: Grade Classification
- The soap has $\text{TFM} = 76.40\%$ (which satisfies Grade 1 requirement $\ge 76.0\%$).
- However, its Free Caustic Alkali is $0.096\%$, which exceeds the strict toilet soap Grade 1 limit ($\le 0.05\%$) but falls within the laundry soap Grade 3 limit ($\le 0.10\%$).
Therefore, the product is classified as a **High-TFM Laundry Soap Bar (Grade 3)**.""",
                    "hints": ["TFM is directly mass of fatty acids divided by sample mass.", "Free caustic moles equals HCl titration moles."]
                },
                {
                    "id": "prob-5-7",
                    "problemNumber": "5.7",
                    "title": "Critical Micelle Concentration (CMC) & Gibbs Surface Excess",
                    "difficulty": "Hard",
                    "statement": r"""Surface tension measurements of aqueous Sodium Dodecyl Sulfate ($\text{SDS}$, $M = 288.38\text{ g/mol}$) solutions at $25^\circ\text{C}$ ($298.15\text{ K}$) yield the following behavior:
- Below the Critical Micelle Concentration ($\text{CMC}$), the surface tension drops linearly with $\ln C$ according to:
  $$\frac{d\gamma}{d\ln C} = -17.50\text{ mN/m} = -0.01750\text{ N/m}$$
- Above $C = 8.20\text{ mM}$, surface tension becomes constant at $\gamma_{\text{plateau}} = 38.5\text{ mN/m}$.
The Gibbs adsorption isotherm for an unbuffered $1:1$ ionic surfactant ($\text{Na}^+\text{DS}^-$) is:
$$\Gamma = - \frac{1}{2RT} \left(\frac{d\gamma}{d\ln C}\right)$$
where $R = 8.314\text{ J/(mol}\cdot\text{K)}$ and $N_A = 6.022 \times 10^{23}\text{ molecules/mol}$.

1. Identify the Critical Micelle Concentration ($\text{CMC}$) in $\text{mM}$ and $\text{g/L}$.
2. Calculate the maximum surface excess concentration ($\Gamma_{\max}$) in $\text{mol/m}^2$.
3. Determine the minimum area occupied per surfactant molecule ($A_{\min}$) at the air-water interface in square angstroms ($\text{\AA}^2$).""",
                    "solution": r"""### Step 1: Critical Micelle Concentration ($\text{CMC}$)
From the breakpoint in the surface tension plot:
$$\text{CMC} = 8.20\text{ mM} = 8.20 \times 10^{-3}\text{ mol/L}$$
In grams per liter:
$$\text{CMC} = 8.20 \times 10^{-3}\text{ mol/L} \times 288.38\text{ g/mol} = 2.365\text{ g/L}$$

### Step 2: Maximum Surface Excess Concentration ($\Gamma_{\max}$)
Using the $1:1$ ionic Gibbs equation:
$$\Gamma_{\max} = - \frac{1}{2 R T} \left(\frac{d\gamma}{d\ln C}\right)$$
Substitute numerical values:
$$\Gamma_{\max} = - \frac{1}{2 \times 8.314 \times 298.15} \times (-0.01750)$$
$$\Gamma_{\max} = \frac{0.01750}{4,957.6} = 3.530 \times 10^{-6}\text{ mol/m}^2$$
The surface excess concentration is **$3.53 \times 10^{-6}\text{ mol/m}^2$**.

### Step 3: Area Occupied per Surfactant Molecule ($A_{\min}$)
The area occupied per molecule is the reciprocal of surface excess times Avogadro's number:
$$A_{\min} = \frac{1}{N_A \cdot \Gamma_{\max}}$$
$$A_{\min} = \frac{1}{(6.022 \times 10^{23}\text{ molecules/mol}) \times (3.530 \times 10^{-6}\text{ mol/m}^2)}$$
$$A_{\min} = \frac{1}{2.1258 \times 10^{18}\text{ molecules/m}^2} = 4.704 \times 10^{-19}\text{ m}^2\text{/molecule}$$
Converting from $\text{m}^2$ to $\text{\AA}^2$ ($1\text{ \AA}^2 = 10^{-20}\text{ m}^2$):
$$A_{\min} = 4.704 \times 10^{-19} \times 10^{20} = 47.04\text{ \AA}^2$$

The average cross-sectional packing area per SDS molecule is **$47.0\text{ \AA}^2$**, characteristic of an electrostatically repelling anionic sulfate headgroup.""",
                    "hints": ["Remember factor of 2 in denominator for 1:1 ionic surfactant.", "A_min = 1 / (N_A * Gamma_max), with 1 A^2 = 10^-20 m^2."]
                }
            ]
        },

        # =========================================================================
        # UNIT 6: PULP AND PAPER INDUSTRIES
        # =========================================================================
        {
            "id": "unit-6-pulp-and-paper",
            "unitNumber": 6,
            "title": "Unit 6: Pulp and Paper Industries: Wood Chemistry, Kraft Cycle & Sheet Forming",
            "leadSummary": "Comprehensive industrial treatment of fibrous lignocellulosic raw materials, Kraft (sulfate), sulfite, and soda chemical pulping chemistries, continuous Kamyr digester dynamics, closed-loop chemical recovery (black liquor multi-effect evaporation, Tomlinson recovery boiler smelt reduction, green liquor causticizing, rotary lime reburning kiln), ECF/TCF pulp bleaching, and Fourdrinier paper machine dewatering and drying engineering.",
            "simulations": ["sim_ind_kraft_recovery_boiler_cycle"],
            "sections": [
                {
                    "id": "sec-6-1",
                    "secNumber": "6.1",
                    "title": "Wood Chemistry & Lignocellulosic Architecture: Cellulose, Hemicellulose & Lignin",
                    "content": r"""Wood is an anisotropic, cellular natural composite engineered from three principal biopolymer fractions arranged within concentric plant cell walls (middle lamella, primary wall, and secondary wall layers $S_1, S_2, S_3$):

### 1. Cellulose ($40 - 45\text{ wt}\%$)
The structural skeleton of the fiber wall. A linear syndiotactic hom*opolymer of $\beta\text{-D-glucopyranose}$ residues linked exclusively via $\beta\text{-(1}\to\text{4)-glycosidic}$ bonds. Each anhydroglucose repeat unit ($\text{C}_6\text{H}_{10}\text{O}_5$, $M_0 = 162.14\text{ g/mol}$) is rotated $180^\circ$ relative to its neighbor, forming cellobiose repeat units:
- Native wood cellulose exhibits a high degree of polymerization ($\overline{DP}_n \approx 10,000$).
- Intramolecular hydrogen bonds ($\text{O(3)-H}\cdots\text{O(5)}$ and $\text{O(2)-H}\cdots\text{O(6)}$) stiffen the glucan chains into rigid, straight ribbons.
- Intermolecular hydrogen bonds pack parallel chains into crystalline elementary microfibrils ($3 - 5\text{ nm}$ width), conferring immense tensile strength ($> 1,000\text{ MPa}$).

### 2. Hemicellulose ($20 - 30\text{ wt}\%$)
Heterogeneous, branched, low-molecular-weight polysaccharides ($\overline{DP}_n \approx 100 - 200$) acting as a matrix compatibilizer between cellulose microfibrils and lignin:
- **Softwoods (Gymnosperms, conifers)**: Predominantly **Galactoglucomannans** ($15 - 20\%$, linear backbone of $\beta\text{-(1}\to\text{4)}$-linked D-mannose and D-glucose, acetylated, with $\alpha\text{-(1}\to\text{6)}$-D-galactose side branches) and **Arabinoglucuronoxylan** ($5 - 10\%$).
- **Hardwoods (Angiosperms, deciduous)**: Predominantly **$O$-Acetyl-4-$O$-methylglucuronoxylan** ($20 - 35\%$, linear $\beta\text{-(1}\to\text{4)}$-D-xylose backbone substituted with $4\text{-O-methyl-}\alpha\text{-D-glucuronic acid}$ residues) and **Glucomannan** ($2 - 5\%$).

### 3. Lignin ($20 - 30\text{ wt}\%$)
A three-dimensional, amorphous, highly crosslinked polyphenolic macromolecule that permeates the middle lamella and secondary cell walls, cementing fibers together and providing compressive strength and hydrophobicity. Lignin is biosynthesized via enzymatic dehydrogenative polymerization of three phenylpropane monolignol precursors:
1. **$p$-Coumaryl alcohol** $\longrightarrow$ $p$-Hydroxyphenyl ($\text{H}$) units.
2. **Coniferyl alcohol** $\longrightarrow$ Guaiacyl ($\text{G}$) units (dominant in softwoods, $> 95\%$).
3. **Sinapyl alcohol** $\longrightarrow$ Syringyl ($\text{S}$) units (hardwoods contain approximately equal mixtures of $\text{G}$ and $\text{S}$ units).

The monolignols are interconnected by diverse carbon-oxygen and carbon-carbon covalent linkages:
- $\beta\text{-O-4}$ (arylglycerol-$\beta$-aryl ether, constitutes $50 - 65\%$ of all linkages; most easily cleaved in chemical pulping).
- $\alpha\text{-O-4}$ ether linkages.
- $\beta\text{-5}$ (phenylcoumaran, $10 - 12\%$).
- $5\text{-5}^\prime$ (biphenyl, $5 - 10\%$).
- $\beta\text{-}\beta^\prime$ (resinol, $3 - 5\%$)."""
                },
                {
                    "id": "sec-6-2",
                    "secNumber": "6.2",
                    "title": "Chemical Pulping Principles: Kraft (Sulfate), Sulfite, and Soda Chemistries",
                    "content": r"""The primary objective of chemical pulping is to selectively dissolve and extract the inter-fiber lignin binder (delignification) while minimizing depolymerization of cellulose, thereby releasing intact, flexible, high-strength cellulosic fibers.

### Comparison of Principal Pulping Technologies

| Parameter | Kraft (Sulfate) Process | Sulfite Process | Soda Process |
|---|---|---|---|
| **Active Cooking Chemicals** | $\text{NaOH} + \text{Na}_2\text{S}$ | $\text{H}_2\text{SO}_3 + \text{HSO}_3^-$ ($\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Na}^+, \text{NH}_4^+$) | $\text{NaOH}$ alone |
| **Cooking pH Range** | Strongly Alkaline ($\text{pH } 13 - 14$) | Strongly Acidic to Neutral ($\text{pH } 1.5 - 7$) | Strongly Alkaline ($\text{pH } 13 - 14$) |
| **Cooking Temperature** | $165 - 175^\circ\text{C}$ | $130 - 150^\circ\text{C}$ | $160 - 175^\circ\text{C}$ |
| **Cooking Pressure** | $7 - 9\text{ bar}$ | $5 - 7\text{ bar}$ | $7 - 9\text{ bar}$ |
| **Raw Material Versatility** | Universal (all softwoods, hardwoods, bamboo, bagasse) | Restricted (resin-poor woods, spruce, fir, birch) | Non-wood annual plants (straw, bagasse) |
| **Pulp Strength** | Outstanding (Highest tensile & burst) | Moderate (Lower tear strength) | Weak to Moderate |
| **Chemical Recovery** | Closed-loop cyclic recovery ($> 97\%$) | Complex (Magnesium-base only) | Feasible |

### The Kraft Cleavage Mechanism
The Kraft process relies on hydrosulfide ions ($\text{HS}^-$) acting as potent nucleophiles to accelerate the cleavage of ether linkages without excessive carbohydrate degradation:
1. Hydroxide ion ($\text{OH}^-$) deprotonates phenolic hydroxyl groups, generating a phenolate anion.
2. The phenolate induces neighboring-group expulsion of water or alcohol from the $\alpha$-carbon, forming a strained **quinone methide** intermediate.
3. Hydrosulfide ion ($\text{HS}^-$) nucleophilically attacks the quinone methide $\alpha$-position, creating a reactive benzylic thiol.
4. Intramolecular nucleophilic attack of the thiolate sulfur on the adjacent $\beta$-carbon cleaves the critical $\beta\text{-O-4}$ ether bond, fragmenting the lignin polymer into soluble phenolate fragments and liberating an episulfide intermediate:

```
    Quinone Methide  +  HS⁻  ──>  Benzylic Thiol  ──>  Intramolecular S attack
                                                       cleaves β-O-4 bond!
                                                       Fragments lignin into
                                                       alkali-soluble phenolate
```

Without $\text{HS}^-$ (as in the pure soda process), quinone methides undergo rapid alkali-induced condensation with adjacent aromatic rings, forming refractory carbon-carbon bonds that arrest delignification."""
                },
                {
                    "id": "sec-6-3",
                    "secNumber": "6.3",
                    "title": "Industrial Kraft Pulping: White Liquor Terms, Sulfidity & Kamyr Continuous Digester",
                    "content": r"""In industrial Kraft pulping, cooking chemical concentrations are standardized by expressing all sodium salts in terms of equivalent sodium oxide ($\text{Na}_2\text{O}$, $M = 61.98\text{ g/mol}$) or sodium hydroxide ($\text{NaOH}$, $M = 40.00\text{ g/mol}$):

### Canonical White Liquor Terminology
1. **Total Titratable Alkali ($\text{TTA}$)**:
   $$\text{TTA} = [\text{NaOH}] + [\text{Na}_2\text{S}] + [\text{Na}_2\text{CO}_3] \quad (\text{expressed as g/L }\text{Na}_2\text{O})$$
2. **Active Alkali ($\text{AA}$)**:
   Chemical species directly contributing to alkaline cooking:
   $$\text{AA} = [\text{NaOH}] + [\text{Na}_2\text{S}] \quad (\text{as g/L }\text{Na}_2\text{O})$$
3. **Effective Alkali ($\text{EA}$)**:
   Takes into account that sodium sulfide hydrolyzes to liberate only one equivalent of hydroxide:
   $$\text{Na}_2\text{S} + \text{H}_2\text{O} \rightleftharpoons \text{NaOH} + \text{NaHS}$$
   $$\text{EA} = [\text{NaOH}] + \frac{1}{2}[\text{Na}_2\text{S}] \quad (\text{as g/L }\text{Na}_2\text{O})$$
4. **Sulfidity ($\% S$)**:
   The percentage of active alkali represented by sodium sulfide:
   $$\% S = \frac{[\text{Na}_2\text{S}]}{[\text{NaOH}] + [\text{Na}_2\text{S}]} \times 100\% = \frac{[\text{Na}_2\text{S}]}{\text{AA}} \times 100\%$$
   Optimal Kraft sulfidity ranges between $25\%$ and $35\%$.
5. **Causticity ($\% C$)**:
   Efficiency of sodium carbonate conversion in the recausticizing plant:
   $$\% C = \frac{[\text{NaOH}]}{[\text{NaOH}] + [\text{Na}_2\text{CO}_3]} \times 100\%$$

### The H-Factor Kinetics Concept
Delignification in a Kraft digester depends non-linearly on cooking temperature and residence time. Kenneth Vroom (1957) synthesized these variables into a single dimensionless kinetic parameter, the **$H\text{-Factor}$**, by integrating relative reaction rates based on the Arrhenius equation with an activation energy $E_a = 134.0\text{ kJ/mol}$:
$$k_{\text{rel}}(T) = \exp\left[\frac{E_a}{R}\left(\frac{1}{373.15} - \frac{1}{T}\right)\right] = \exp\left[43.2 - \frac{16,113}{T}\right] \quad (T\text{ in K})$$
$$H = \int_0^t k_{\text{rel}}(T) \, dt$$
At $100^\circ\text{C}$ ($373.15\text{ K}$), $k_{\text{rel}} = 1.0$. At $170^\circ\text{C}$ ($443.15\text{ K}$), $k_{\text{rel}} \approx 870$. An entire cooking schedule (heating ramp + cooking plateau) yielding an $H\text{-factor}$ of $1200 - 1800$ ensures reproducible target Kappa numbers regardless of minor steam temperature variations."""
                },
                {
                    "id": "sec-6-4",
                    "secNumber": "6.4",
                    "title": "The Kraft Chemical Recovery Loop: Black Liquor Evaporation & Tomlinson Recovery Boiler",
                    "content": r"""The Kraft process owes its overwhelming global dominance to its closed-loop chemical recovery cycle, which achieves $> 97\%$ recovery of sodium and sulfur cooking chemicals while generating massive surplus electrical power and high-pressure steam from lignin combustion:

```
                      THE KRAFT CHEMICAL RECOVERY CYCLE
   Wood Chips + White Liquor (NaOH + Na2S)
         │
         ▼
  ┌──────────────┐
  │ DIGESTER     │ ──> Brownstock Pulp to Bleaching / Papermaking
  └──────┬───────┘
         ▼ Weak Black Liquor (~15% solids)
  ┌──────────────┐
  │ MULTI-EFFECT │ ──> Condensate to Washers
  │ EVAPORATORS  │
  └──────┬───────┘
         ▼ Heavy Black Liquor (~70-80% solids)
  ┌────────────────────────────────────────────────────────┐
  │ TOMLINSON RECOVERY BOILER                              │ <── Na2SO4 Make-up
  │                                                        │ ──> High-Pressure Steam (80 bar)
  │ Upper: Steam Generating Tubes & Superheaters (Combustion)│ ──> Power Turbines
  │ Lower: Reducing Char Bed (950-1050°C)                 │
  │        Na2SO4 + 2 C ──> Na2S + 2 CO2 (Smelt Reduction) │
  └──────────────────────────┬─────────────────────────────┘
                             ▼ Molten Smelt (Na2S + Na2CO3 at ~850°C)
  ┌──────────────────────────┴─────────────────────────────┐
  │ SMELT DISSOLVER (Water / Weak Wash)                    │
  └──────────────────────────┬─────────────────────────────┘
                             ▼ Raw Green Liquor
  ┌──────────────────────────┴─────────────────────────────┐
  │ CAUSTICIZING PLANT (Slaker + Causticizers + Lime Kiln) │
  └──────────────────────────┬─────────────────────────────┘
                             ▼ Regenerated White Liquor (NaOH + Na2S) back to Digester!
```

### 1. Multiple-Effect Black Liquor Evaporation
Weak black liquor discharged from brownstock washing contains $14 - 17\text{ wt}\%$ dissolved solids (organics: lignin, hemicellulose breakdown acids; inorganics: $\text{Na}_2\text{CO}_3, \text{Na}_2\text{SO}_4, \text{Na}_2\text{S}$). It is concentrated to **$70 - 80\text{ wt}\%$ dry solids** in a 6- or 7-effect falling-film evaporator train, reaching high solids to enable stable combustion in the recovery furnace.

### 2. Tomlinson Recovery Boiler Thermochemistry
The concentrated heavy black liquor is sprayed through oscillating splash-plate nozzles into the furnace of a massive recovery boiler operating under two distinct chemical zones:
- **Lower Reducing Zone (Char Bed at $950 - 1050^\circ\text{C}$)**:
  Under substoichiometric primary air, carbon in the char bed acts as a powerful reducing agent, converting oxidized sodium sulfate back into sodium sulfide:
  $$\text{Na}_2\text{SO}_4 + 2\text{C} \longrightarrow \text{Na}_2\text{S} + 2\text{CO}_2 \quad (\Delta H = +175.7\text{ kJ/mol})$$
  $$\text{Na}_2\text{SO}_4 + 4\text{C} \longrightarrow \text{Na}_2\text{S} + 4\text{CO} \quad (\Delta H = +568.0\text{ kJ/mol})$$
  Sodium carbonate melts without reduction ($T_{\text{melt}} = 851^\circ\text{C}$). The resulting molten mixture of $\text{Na}_2\text{S}$ ($25 - 30\text{ mol}\%$) and $\text{Na}_2\text{CO}_3$ ($70 - 75\text{ mol}\%$) forms red-hot liquid **smelt** at $850^\circ\text{C}$ that drains continuously through water-cooled smelt spouts.
- **Upper Oxidizing Zone ($1100 - 1200^\circ\text{C}$)**:
  Secondary and tertiary air jets inject oxygen to burn volatile pyrolysis gases ($\text{CO}, \text{H}_2, \text{CH}_4$, and organic vapors), releasing intense thermal energy to superheater tubes, producing high-pressure steam ($60 - 100\text{ bar}$, $450 - 500^\circ\text{C}$) that drives turbo-generators."""
                },
                {
                    "id": "sec-6-5",
                    "secNumber": "6.5",
                    "title": "Green Liquor Clarification, Recausticizing Chemistries & Lime Reburning Kiln",
                    "content": r"""The molten smelt flowing from the recovery boiler spouts is shattered with high-pressure steam jets and dissolved in weak wash water inside the agitated smelt dissolving tank:
$$\text{Smelt } (\text{Na}_2\text{S} + \text{Na}_2\text{CO}_3) + \text{H}_2\text{O} \longrightarrow \text{Green Liquor}$$
The resulting solution is emerald green due to colloidal iron sulfide ($\text{FeS}$) complexes.

### 1. Dreg Separation & Slaker-Causticizer Chemistry
1. **Green Liquor Clarification**: Heavy insoluble particles ("dregs": unburned carbon, iron sulfide, silica) are removed in a rake clarifier or pressurized disc filter.
2. **Lime Slaking & Causticizing**: The clarified green liquor enters an agitated slaker vessel where reburned quicklime ($\text{CaO}$) is added:
   - **Exothermic Slaking Reaction**:
     $$\text{CaO}(s) + \text{H}_2\text{O}(l) \rightleftharpoons \text{Ca(OH)}_2(s) \quad (\Delta H = -65.2\text{ kJ/mol})$$
   - **Causticizing Equilibrium Reaction**:
     $$\text{Ca(OH)}_2(s) + \text{Na}_2\text{CO}_3(aq) \rightleftharpoons 2\text{NaOH}(aq) + \text{CaCO}_3(s) \downarrow \quad (\Delta H = -8.8\text{ kJ/mol})$$
     Sodium sulfide ($\text{Na}_2\text{S}$) passes through completely unaffected, while $\text{Na}_2\text{CO}_3$ is converted into active $\text{NaOH}$, regenerating **White Liquor**.

### Thermodynamic Equilibrium & Causticizing Efficiency
The causticizing reaction is reversible and limited by the solubility product ratio of $\text{Ca(OH)}_2$ and $\text{CaCO}_3$:
$$K_c = \frac{[\text{OH}^-]^2}{[\text{CO}_3^{2-}]} = \frac{K_{\text{sp, Ca(OH)}_2}}{K_{\text{sp, CaCO}_3}} \approx \frac{5.5 \times 10^{-6}}{3.8 \times 10^{-9}} \approx 1,450$$
As white liquor total titratable alkali ($\text{TTA}$) increases, the high concentration of $[\text{OH}^-]$ drives the equilibrium backward, suppressing causticizing efficiency ($\text{CE}$):
$$\text{CE} = \frac{[\text{NaOH}]}{[\text{NaOH}] + [\text{Na}_2\text{CO}_3]} \times 100\%$$
In industrial practice, $\text{CE}$ is limited to $80 - 85\%$ to prevent unreacted slaked lime ("free lime") from blinding the lime mud filters.

### 2. Lime Mud Dewatering & Rotary Lime Reburning Kiln
The precipitated calcium carbonate mud ($\text{CaCO}_3$) is separated from white liquor in precoat vacuum drum filters, washed, and fed at $75 - 80\text{ wt}\%$ dry solids into a rotary lime reburning kiln ($70 - 110\text{ m}$ length) fired by natural gas, fuel oil, or gasified biomass:
$$\text{CaCO}_3(s) \overset{900 - 1100^\circ\text{C}}{\longrightarrow} \text{CaO}(s) + \text{CO}_2(g)$$
The calcined quicklime is discharged and pneumatically conveyed back to the slaker, closing the inorganic lime cycle."""
                },
                {
                    "id": "sec-6-6",
                    "secNumber": "6.6",
                    "title": "Pulp Bleaching Technologies: ECF (ClO2) & TCF (Oxygen, Ozone, Peroxide) Engineering",
                    "content": r"""Unbleached Kraft pulp retains a dark brown appearance (ISO brightness $25 - 35\%$) due to residual modified lignin ($3 - 5\text{ wt}\%$ of dry pulp) containing chromophoric quinones, quinone methides, and conjugated stilbene structures. Bleaching achieves an ISO brightness $> 88 - 90\%$ through selective oxidative delignification and chromophore destruction.

### Evolution from Elemental Chlorine to ECF & TCF
- **Elemental Chlorine Bleaching ($C\text{-}E\text{-}H\text{-}D$)**: Historically used molecular chlorine ($\text{Cl}_2$) at acidic $\text{pH}$. Electrophilic aromatic substitution generated toxic, bioaccumulative polychlorinated dibenzo-$p$-dioxins ($2,3,7,8\text{-TCDD}$), dibenzofurans, and absorbable organic halides ($\text{AOX}$), leading to global environmental bans.
- **Elemental Chlorine-Free (ECF)**: Replaces $\text{Cl}_2$ with chlorine dioxide ($\text{ClO}_2$). Operates as a selective one-electron oxidant, eliminating dioxin formation and cutting $\text{AOX}$ by $> 90\%$.
- **Totally Chlorine-Free (TCF)**: Eliminates all chlorine-containing compounds, using oxygen ($\text{O}$), ozone ($\text{Z}$), and hydrogen peroxide ($\text{P}$).

### Modern Bleaching Stage Chemistries
1. **Oxygen Delignification ($\text{O}$-Stage, $90 - 105^\circ\text{C}$, $4 - 6\text{ bar O}_2$, $\text{pH } 11 - 12$)**:
   Removes $40 - 50\%$ of residual lignin prior to the bleach plant. Oxygen reacts with phenolate anions to form hydroperoxide radicals, initiating oxidative aromatic ring cleavage into dicarboxylic acids (muconic acid derivatives).
2. **Chlorine Dioxide Stage ($\text{D}$-Stage, $70 - 80^\circ\text{C}$, $\text{pH } 2.5 - 3.5$)**:
   $$\text{Lignin} + \text{ClO}_2 \longrightarrow \text{Chlorite} \ (\text{ClO}_2^-) + \text{Oxidized Quinoid Lignin} \longrightarrow \text{Water-soluble muconic esters}$$
   Chlorine dioxide is manufactured on-site (Erco R8 or SVP-Lurgi process) by reducing sodium chlorate ($\text{NaClO}_3$) with methanol or hydrogen peroxide in sulfuric acid:
   $$\text{NaClO}_3 + \frac{1}{6}\text{CH}_3\text{OH} + \frac{1}{2}\text{H}_2\text{SO}_4 \longrightarrow \text{ClO}_2 + \frac{1}{2}\text{Na}_2\text{SO}_4 + \frac{1}{6}\text{CO}_2 + \frac{7}{6}\text{H}_2\text{O}$$
3. **Alkaline Extraction Stage ($\text{E}$-Stage, reinforced with $\text{O}_2$ and $\text{H}_2\text{O}_2$, $\text{EOP}$)**:
   Extracts solubilized oxidized lignin fragments with aqueous $\text{NaOH}$ while peroxide cleaves stubborn carbonyl chromophores."""
                },
                {
                    "id": "sec-6-7",
                    "secNumber": "6.7",
                    "title": "Papermaking Engineering: Fourdrinier Machine, Dewatering & Drying Heat Balances",
                    "content": r"""The papermaking machine transforms a dilute fiber suspension ($0.5 - 1.0\text{ wt}\%$ fibers in water) into a dry, smooth, continuous web of paper ($92 - 95\text{ wt}\%$ dry matter) at linear speeds exceeding $1,200 - 2,000\text{ m/min}$ ($70 - 120\text{ km/h}$).

```
                         THE FOURDRINIER PAPER MACHINE
  Stock Approach (0.8% solids)
       │
       ▼
  ┌──────────────┐
  │ HEADBOX      │ (Slice Jet Velocity Matching Wire Speed)
  └──────┬───────┘
         ▼
  ┌────────────────────────────────────────────────────────┐
  │ FORMING SECTION (Fourdrinier Wire)                     │ ──> Gravity / Foil Dewatering
  │ (Continuous moving bronze or synthetic mesh)           │ ──> Suction Vacuum Boxes
  └──────────────────────────┬─────────────────────────────┘
                             ▼ Wet Paper Web (~20% solids)
  ┌────────────────────────────────────────────────────────┐
  │ PRESS SECTION (Shoe Press / Roll Presses)             │ ──> Mechanical Expressing of Water
  │ (Felt-supported nip under 5-10 MPa pressure)           │     (Web reaches ~45-50% solids)
  └──────────────────────────┬─────────────────────────────┘
                             ▼ Web (~45-50% solids)
  ┌────────────────────────────────────────────────────────┐
  │ DRYER SECTION (40-60 Steam-Heated Drying Cylinders)    │ ──> Condensing Steam (2-5 bar)
  │ (Enclosed hood, ventilation air removal of steam)      │     Evaporates water to 93-95% solids!
  └──────────────────────────┬─────────────────────────────┘
                             ▼
  ┌──────────────┐
  │ CALENDER     │ (Heated Steel Rolls: Compacting, Caliper Control & Gloss)
  └──────┬───────┘
         ▼
  ┌──────────────┐
  │ REEL / WINDER│ ──> Jumbo Paper Rolls (Parent Reel)
  └──────────────┘
```

### The Three Progressive Dewatering Sections
1. **Forming (Wire) Section ($0.8\% \to 20\%$ solids)**:
   The pressurized **headbox** discharges an ultra-uniform turbulent jet of dilute stock through a precision slice opening onto a rapidly traveling endless loop of synthetic woven wire. Water drains gravimetrically through hydrofoils, vacuum suction boxes, and the couch roll, forming an interconnected, non-woven fiber mat. Dewatering cost is lowest here ($< 1\%$ total energy).
2. **Press Section ($20\% \to 45 - 50\%$ solids)**:
   The wet sheet is conveyed between continuous absorbent synthetic felts through rotating press nips (modern shoe presses exert pressures up to $5 - 10\text{ MPa}$ over an extended nip shoe width of $250\text{ mm}$). Water is mechanically expressed out of the sheet into the felt pores. Removing $1\text{ kg}$ of water mechanically consumes only $5 - 10\%$ of the energy required to evaporate it thermally.
3. **Dryer Section ($45\% \to 94\%$ solids)**:
   The remaining water ($1.0 - 1.2\text{ kg water / kg dry paper}$) cannot be expelled mechanically due to capillary retention within fiber lumen and cell wall micro-pores. The sheet snakes over $40 - 60$ cast-iron steam-heated drying cylinders ($1.5 - 1.8\text{ m}$ diameter) heated by condensing saturated steam ($2 - 5\text{ bar}$, $120 - 150^\circ\text{C}$). Steam consumption in the dryer section typically averages $1.3 - 1.8\text{ kg steam / kg water evaporated}$."""
                }
            ],
            "problems": [
                {
                    "id": "prob-6-1",
                    "problemNumber": "6.1",
                    "title": "Kraft Digester White Liquor Terms & Alkali Balance",
                    "difficulty": "Easy",
                    "statement": r"""A chemical pulp mill laboratory analyzes a white liquor sample and reports the following concentrations:
- $[\text{NaOH}] = 80.00\text{ g/L}$ (as $\text{NaOH}$)
- $[\text{Na}_2\text{S}] = 39.00\text{ g/L}$ (as $\text{Na}_2\text{S}$)
- $[\text{Na}_2\text{CO}_3] = 21.20\text{ g/L}$ (as $\text{Na}_2\text{CO}_3$)
Molar masses: $\text{Na}_2\text{O} = 61.98\text{ g/mol}$, $\text{NaOH} = 40.00\text{ g/mol}$, $\text{Na}_2\text{S} = 78.04\text{ g/mol}$, $\text{Na}_2\text{CO}_3 = 105.99\text{ g/mol}$.

1. Convert each salt concentration into equivalent $\text{g/L as Na}_2\text{O}$.
2. Calculate the Total Titratable Alkali ($\text{TTA}$), Active Alkali ($\text{AA}$), and Effective Alkali ($\text{EA}$) in $\text{g/L as Na}_2\text{O}$.
3. Calculate the Sulfidity ($\% S$) and Causticity ($\% C$) of this white liquor.""",
                    "solution": r"""### Step 1: Conversion to Equivalent $\text{Na}_2\text{O}$
Conversion factors:
- For $\text{NaOH}$: $\frac{M_{\text{Na}_2\text{O}}}{2 \times M_{\text{NaOH}}} = \frac{61.98}{80.00} = 0.77475$
- For $\text{Na}_2\text{S}$: $\frac{M_{\text{Na}_2\text{O}}}{M_{\text{Na}_2\text{S}}} = \frac{61.98}{78.04} = 0.79421$
- For $\text{Na}_2\text{CO}_3$: $\frac{M_{\text{Na}_2\text{O}}}{M_{\text{Na}_2\text{CO}_3}} = \frac{61.98}{105.99} = 0.58477$

Concentrations as $\text{Na}_2\text{O}$:
$$[\text{NaOH}]_{\text{as Na}_2\text{O}} = 80.00 \times 0.77475 = 61.98\text{ g/L}$$
$$[\text{Na}_2\text{S}]_{\text{as Na}_2\text{O}} = 39.00 \times 0.79421 = 30.97\text{ g/L}$$
$$[\text{Na}_2\text{CO}_3]_{\text{as Na}_2\text{O}} = 21.20 \times 0.58477 = 12.40\text{ g/L}$$

### Step 2: Compute Alkali Parameters
1. **Total Titratable Alkali ($\text{TTA}$)**:
   $$\text{TTA} = [\text{NaOH}] + [\text{Na}_2\text{S}] + [\text{Na}_2\text{CO}_3] = 61.98 + 30.97 + 12.40 = 105.35\text{ g/L as Na}_2\text{O}$$
2. **Active Alkali ($\text{AA}$)**:
   $$\text{AA} = [\text{NaOH}] + [\text{Na}_2\text{S}] = 61.98 + 30.97 = 92.95\text{ g/L as Na}_2\text{O}$$
3. **Effective Alkali ($\text{EA}$)**:
   $$\text{EA} = [\text{NaOH}] + \frac{1}{2}[\text{Na}_2\text{S}] = 61.98 + \frac{30.97}{2} = 61.98 + 15.485 = 77.47\text{ g/L as Na}_2\text{O}$$

### Step 3: Sulfidity ($\% S$) and Causticity ($\% C$)
- **Sulfidity**:
  $$\% S = \frac{[\text{Na}_2\text{S}]}{\text{AA}} \times 100\% = \frac{30.97}{92.95} \times 100\% = 33.32\%$$
- **Causticity**:
  $$\% C = \frac{[\text{NaOH}]}{[\text{NaOH}] + [\text{Na}_2\text{CO}_3]} \times 100\% = \frac{61.98}{61.98 + 12.40} \times 100\% = \frac{61.98}{74.38} \times 100\% = 83.33\%$$

The liquor has **$\text{TTA} = 105.4\text{ g/L}$**, **$\text{AA} = 93.0\text{ g/L}$**, **$\text{EA} = 77.5\text{ g/L}$**, **Sulfidity $= 33.3\%$**, and **Causticity $= 83.3\%$**.""",
                    "hints": ["Each conversion factor is ratio of molar mass of Na2O to molar mass of salt.", "EA takes half of Na2S."]
                },
                {
                    "id": "prob-6-2",
                    "problemNumber": "6.2",
                    "title": "H-Factor Kinetic Integration for Kamyr Continuous Digester",
                    "difficulty": "Medium",
                    "statement": r"""A continuous digester cooking softwood chips operates with the Vroom relative rate equation:
$$k_{\text{rel}}(T) = \exp\left[43.20 - \frac{16,113}{T}\right] \quad (T\text{ in K})$$
A cooking cycle follows this thermal trajectory:
1. Heating ramp from $140^\circ\text{C}$ ($413.15\text{ K}$) to $170^\circ\text{C}$ ($443.15\text{ K}$) linearly over $45\text{ minutes}$ (average relative rate approximated by Simpson's rule at $140^\circ\text{C}$, $155^\circ\text{C}$, $170^\circ\text{C}$).
2. Isothermal cooking zone at constant $170^\circ\text{C}$ for $t_{\text{cook}}\text{ minutes}$.

If the target Kappa number requires a total $H\text{-Factor} = 1,400\text{ hours}_{\text{equivalent}}$:
1. Calculate the relative reaction rate $k_{\text{rel}}$ at $140^\circ\text{C}$, $155^\circ\text{C}$, and $170^\circ\text{C}$.
2. Determine the $H\text{-Factor}$ accumulated during the 45-minute heating ramp.
3. Calculate the required isothermal cooking residence time ($t_{\text{cook}}$) in minutes.""",
                    "solution": r"""### Step 1: Relative Reaction Rates ($k_{\text{rel}}$)
- **At $140^\circ\text{C} = 413.15\text{ K}$**:
  $$43.20 - \frac{16,113}{413.15} = 43.20 - 38.999 = 4.201 \implies k_{\text{rel}}(140) = e^{4.201} \approx 66.75$$
- **At $155^\circ\text{C} = 428.15\text{ K}$**:
  $$43.20 - \frac{16,113}{428.15} = 43.20 - 37.634 = 5.566 \implies k_{\text{rel}}(155) = e^{5.566} \approx 261.39$$
- **At $170^\circ\text{C} = 443.15\text{ K}$**:
  $$43.20 - \frac{16,113}{443.15} = 43.20 - 36.360 = 6.840 \implies k_{\text{rel}}(170) = e^{6.840} \approx 934.49$$

### Step 2: $H\text{-Factor}$ Accumulated During Heating Ramp
Using Simpson's $1/3$ rule for the $\Delta t = 45\text{ min} = 0.75\text{ h}$ ramp with step $h = 0.375\text{ h}$:
$$H_{\text{ramp}} = \frac{h}{3} \left[k_{\text{rel}}(140) + 4 \cdot k_{\text{rel}}(155) + k_{\text{rel}}(170)\right]$$
$$H_{\text{ramp}} = \frac{0.375}{3} \left[66.75 + 4(261.39) + 934.49\right]$$
$$H_{\text{ramp}} = 0.125 \left[66.75 + 1045.56 + 934.49\right] = 0.125 \times 2,046.80 = 255.85$$
The heating ramp contributes **$255.9$** to the $H\text{-factor}$.

### Step 3: Isothermal Residence Time at $170^\circ\text{C}$
Remaining $H\text{-factor}$ required:
$$H_{\text{iso}} = H_{\text{target}} - H_{\text{ramp}} = 1,400.0 - 255.85 = 1,144.15$$
During isothermal hold at $170^\circ\text{C}$:
$$H_{\text{iso}} = k_{\text{rel}}(170) \times t_{\text{iso}} \implies t_{\text{iso}} = \frac{H_{\text{iso}}}{k_{\text{rel}}(170)}$$
$$t_{\text{iso}} = \frac{1,144.15}{934.49} = 1.22435\text{ hours} = 1.22435 \times 60\text{ min} \approx 73.46\text{ minutes}$$

The digester requires **$73.5\text{ minutes}$** of isothermal cooking at $170^\circ\text{C}$.""",
                    "hints": ["Convert time from minutes to hours when calculating H-factor.", "Subtract ramp H-factor from total target H-factor."]
                },
                {
                    "id": "prob-6-3",
                    "problemNumber": "6.3",
                    "title": "Tomlinson Recovery Boiler Smelt Stoichiometry & Reduction Efficiency",
                    "difficulty": "Medium",
                    "statement": r"""A Kraft pulp mill fires $1,500\text{ metric tons/day}$ ($62.5\text{ t/h}$) of heavy black liquor solids ($75.0\text{ wt}\%$ dry solids) into a Tomlinson recovery boiler.
The black liquor dry solids assay:
- Carbon ($\text{C}$): $35.0\text{ wt}\%$
- Hydrogen ($\text{H}$): $3.5\text{ wt}\%$
- Oxygen ($\text{O}$): $34.5\text{ wt}\%$
- Sodium ($\text{Na}$): $19.0\text{ wt}\%$
- Sulfur ($\text{S}$): $5.0\text{ wt}\%$
- Inerts: $3.0\text{ wt}\%$

Molar masses: $\text{Na} = 22.99\text{ g/mol}$, $\text{S} = 32.06\text{ g/mol}$, $\text{Na}_2\text{S} = 78.04\text{ g/mol}$, $\text{Na}_2\text{SO}_4 = 142.04\text{ g/mol}$, $\text{Na}_2\text{CO}_3 = 105.99\text{ g/mol}$.
The molten smelt leaving the furnace has a **Reduction Efficiency ($\text{RE}$)** of $94.0\%$, defined as:
$$\text{RE} = \frac{\text{mol Na}_2\text{S}}{\text{mol Na}_2\text{S} + \text{mol Na}_2\text{SO}_4} \times 100\%$$
Assuming all sulfur entering ends up in the smelt as either $\text{Na}_2\text{S}$ or $\text{Na}_2\text{SO}_4$, and all remaining sodium forms $\text{Na}_2\text{CO}_3$:
1. Calculate the molar flow rate of total sulfur and sodium entering the boiler per hour ($\text{kmol/h}$).
2. Determine the production rates of $\text{Na}_2\text{S}$, $\text{Na}_2\text{SO}_4$, and $\text{Na}_2\text{CO}_3$ in the molten smelt in metric tons per hour.""",
                    "solution": r"""### Step 1: Input Molar Flow Rates
Total dry solids feed rate:
$$\dot{m}_{\text{solids}} = 62.5\text{ metric tons/h} = 62,500\text{ kg/h}$$
Sulfur input:
$$\dot{m}_{\text{S}} = 0.050 \times 62,500 = 3,125\text{ kg/h} \implies \dot{n}_{\text{S}} = \frac{3,125\text{ kg/h}}{32.06\text{ kg/kmol}} = 97.473\text{ kmol/h}$$
Sodium input:
$$\dot{m}_{\text{Na}} = 0.190 \times 62,500 = 11,875\text{ kg/h} \implies \dot{n}_{\text{Na}} = \frac{11,875\text{ kg/h}}{22.99\text{ kg/kmol}} = 516.529\text{ kmol/h}$$

### Step 2: Smelt Component Rates
All sulfur enters as $\text{Na}_2\text{S}$ ($94\%$) and $\text{Na}_2\text{SO}_4$ ($6\%$):
$$\dot{n}_{\text{Na}_2\text{S}} = 0.940 \times 97.473 = 91.625\text{ kmol/h}$$
$$\dot{n}_{\text{Na}_2\text{SO}_4} = 0.060 \times 97.473 = 5.848\text{ kmol/h}$$

Mass flow rates of sulfide and sulfate:
$$\dot{m}_{\text{Na}_2\text{S}} = 91.625\text{ kmol/h} \times 78.04\text{ kg/kmol} = 7,150.4\text{ kg/h} \approx 7.150\text{ metric tons/h}$$
$$\dot{m}_{\text{Na}_2\text{SO}_4} = 5.848\text{ kmol/h} \times 142.04\text{ kg/kmol} = 830.6\text{ kg/h} \approx 0.831\text{ metric tons/h}$$

Now compute sodium consumed by sulfur compounds:
$$\dot{n}_{\text{Na, consumed}} = 2 \times \dot{n}_{\text{Na}_2\text{S}} + 2 \times \dot{n}_{\text{Na}_2\text{SO}_4} = 2(91.625 + 5.848) = 2 \times 97.473 = 194.946\text{ kmol/h}$$
Remaining sodium available for $\text{Na}_2\text{CO}_3$:
$$\dot{n}_{\text{Na, carbonate}} = 516.529 - 194.946 = 321.583\text{ kmol/h}$$
Moles of $\text{Na}_2\text{CO}_3$ formed:
$$\dot{n}_{\text{Na}_2\text{CO}_3} = \frac{321.583}{2} = 160.792\text{ kmol/h}$$
Mass flow rate of sodium carbonate:
$$\dot{m}_{\text{Na}_2\text{CO}_3} = 160.792\text{ kmol/h} \times 105.99\text{ kg/kmol} = 17,042.3\text{ kg/h} \approx 17.042\text{ metric tons/h}$$

The molten smelt discharges:
- **$\text{Na}_2\text{S} = 7.15\text{ metric tons/h}$**
- **$\text{Na}_2\text{SO}_4 = 0.83\text{ metric tons/h}$**
- **$\text{Na}_2\text{CO}_3 = 17.04\text{ metric tons/h}$**
Total smelt rate $= 25.02\text{ metric tons/h}$.""",
                    "hints": ["Total sulfur is partitioned 94% into Na2S and 6% into Na2SO4.", "Remaining sodium after accounting for sulfur forms Na2CO3."]
                },
                {
                    "id": "prob-6-4",
                    "problemNumber": "6.4",
                    "title": "Recausticizing Plant Lime Mud Balance & Causticizing Efficiency",
                    "difficulty": "Medium",
                    "statement": r"""A causticizing plant receives green liquor containing $120.0\text{ g/L total Na}_2\text{O}$ at a volumetric flow rate of $150.0\text{ m}^3\text{/h}$.
- In the green liquor, sodium carbonate constitutes $[\text{Na}_2\text{CO}_3] = 85.0\text{ g/L as Na}_2\text{O}$ ($1.371\text{ kmol/m}^3$).
- The causticizing reaction achieves a Causticizing Efficiency ($\text{CE}$) of $82.0\%$:
  $$\text{Ca(OH)}_2 + \text{Na}_2\text{CO}_3 \rightleftharpoons 2\text{NaOH} + \text{CaCO}_3 \downarrow$$
- The lime fed from the reburning kiln contains $90.0\text{ wt}\%\text{ active CaO}$ ($56.08\text{ g/mol}$) and is added at a $5.0\%$ stoichiometric excess over the reacted $\text{Na}_2\text{CO}_3$.
Molar mass of $\text{CaCO}_3 = 100.09\text{ g/mol}$.

1. Calculate the moles of $\text{Na}_2\text{CO}_3$ converted to $\text{NaOH}$ per hour.
2. Determine the required hourly feed rate of reburned quicklime in metric tons per hour.
3. Calculate the mass of dry calcium carbonate lime mud ($\text{CaCO}_3$) precipitated per hour.""",
                    "solution": r"""### Step 1: Moles of $\text{Na}_2\text{CO}_3$ Converted
Total $\text{Na}_2\text{CO}_3$ entering per hour:
$$\dot{n}_{\text{carbonate, in}} = 150.0\text{ m}^3\text{/h} \times 1.3714\text{ kmol/m}^3 = 205.71\text{ kmol/h}$$
At $\text{CE} = 82.0\%$, the reacted carbonate is:
$$\dot{n}_{\text{carbonate, reacted}} = 0.820 \times 205.71\text{ kmol/h} = 168.68\text{ kmol/h}$$

### Step 2: Reburned Quicklime Feed Rate
Stoichiometric $\text{CaO}$ required is $1:1$ with reacted carbonate:
$$\dot{n}_{\text{CaO, theo}} = 168.68\text{ kmol/h}$$
With $5.0\%$ stoichiometric excess ($1.05\times$):
$$\dot{n}_{\text{CaO, actual}} = 1.05 \times 168.68 = 177.11\text{ kmol/h}$$
Mass of pure $\text{CaO}$:
$$\dot{m}_{\text{CaO, pure}} = 177.11\text{ kmol/h} \times 56.08\text{ kg/kmol} = 9,932.3\text{ kg/h}$$
Since the reburned lime is $90.0\text{ wt}\%$ active:
$$\dot{m}_{\text{lime}} = \frac{9,932.3\text{ kg/h}}{0.90} = 11,035.9\text{ kg/h} \approx 11.04\text{ metric tons/h}$$

### Step 3: Precipitated Lime Mud ($\text{CaCO}_3$)
Every mole of reacted $\text{Na}_2\text{CO}_3$ yields $1\text{ mole of CaCO}_3$:
$$\dot{n}_{\text{CaCO}_3} = 168.68\text{ kmol/h}$$
Mass of dry $\text{CaCO}_3$ precipitated:
$$\dot{m}_{\text{CaCO}_3} = 168.68\text{ kmol/h} \times 100.09\text{ kg/kmol} = 16,883.2\text{ kg/h} \approx 16.88\text{ metric tons/h}$$

The plant feeds **$11.04\text{ metric tons/h}$** of reburned lime and discharges **$16.88\text{ metric tons/h}$** of precipitated $\text{CaCO}_3$ lime mud.""",
                    "hints": ["Reacted carbonate equals entering carbonate times CE.", "Lime mass is active CaO divided by 0.90 purity."]
                },
                {
                    "id": "prob-6-5",
                    "problemNumber": "6.5",
                    "title": "Chlorine Dioxide (ClO2) Bleaching & AOX Elimination",
                    "difficulty": "Easy",
                    "statement": r"""A bleach plant treats $1,000\text{ metric tons/day}$ ($41.67\text{ t/h}$) of oven-dry oxygen-delignified Kraft pulp.
- The unbleached pulp has a Kappa number $\kappa_1 = 12.0$.
- The Kappa number measures residual lignin content according to the empirical relationship:
  $$\% \text{ Residual Lignin} \approx 0.15 \times \text{Kappa}$$
- The first chlorine dioxide stage ($D_0$) applies an active chlorine factor ($\text{KF}$) of $0.20$, where:
  $$\% \text{ Equivalent Cl}_2 \text{ on pulp} = \text{KF} \times \text{Kappa}$$
- In oxidation stoichiometry, $1\text{ kg of ClO}_2$ ($67.45\text{ g/mol}$) provides $2.63\text{ kg of equivalent active chlorine}$ ($\text{Cl}_2$, $70.90\text{ g/mol}$) because chlorine shifts from oxidation state $+4$ to $-1$ ($5\text{ electrons}$):
  $$\text{ClO}_2 + 5e^- + 4\text{H}^+ \longrightarrow \text{Cl}^- + 2\text{H}_2\text{O}$$

1. Calculate the equivalent active chlorine required on dry pulp as a percentage.
2. Determine the hourly consumption rate of pure $\text{ClO}_2$ in kilograms per hour.
3. Compare the theoretical chlorine atom incorporation into organochlorines ($\text{AOX}$) between $\text{Cl}_2$ ($10\text{ wt}\%$ conversion to AOX) and $\text{ClO}_2$ ($< 0.8\text{ wt}\%$ conversion to AOX).""",
                    "solution": r"""### Step 1: Active Chlorine Charge on Pulp
$$\% \text{ Equivalent Cl}_2 = \text{KF} \times \text{Kappa} = 0.20 \times 12.0 = 2.40\% \text{ on pulp}$$

### Step 2: Hourly $\text{ClO}_2$ Consumption Rate
Hourly pulp production:
$$\dot{m}_{\text{pulp}} = 41.67\text{ metric tons/h} = 41,667\text{ kg/h}$$
Equivalent active chlorine required per hour:
$$\dot{m}_{\text{act Cl}_2} = 0.0240 \times 41,667\text{ kg/h} = 1,000.0\text{ kg/h}$$
Since $1\text{ kg of ClO}_2 = 2.63\text{ kg of active Cl}_2$:
$$\dot{m}_{\text{ClO}_2} = \frac{1,000.0\text{ kg/h}}{2.63} = 380.23\text{ kg/h}$$
The mill consumes **$380.2\text{ kg/h}$ of pure $\text{ClO}_2$**.

### Step 3: AOX Discharge Comparison
- Under legacy molecular chlorine ($\text{Cl}_2$), $10\%$ of the applied $1,000\text{ kg/h}$ chlorine was bound into toxic chlorolignin:
  $$\text{AOX}_{\text{legacy}} = 0.10 \times 1,000.0 = 100.0\text{ kg organochlorines/h} \quad (2.4\text{ kg AOX / t pulp})$$
- Under modern $\text{ClO}_2$ (ECF), less than $0.8\%$ of chlorine is bound:
  $$\text{AOX}_{\text{ECF}} \le 0.008 \times 1,000.0 = 8.0\text{ kg organochlorines/h} \quad (\le 0.19\text{ kg AOX / t pulp})$$
Switching to ECF reduces bioaccumulative toxic AOX discharge by **over $92\%$**.""",
                    "hints": ["Percent chlorine equals KF times Kappa.", "Divide equivalent chlorine mass by 2.63 to find ClO2 mass."]
                },
                {
                    "id": "prob-6-6",
                    "problemNumber": "6.6",
                    "title": "Fourdrinier Press Section Mechanical Expressing & Energy Savings",
                    "difficulty": "Medium",
                    "statement": r"""A high-speed paper machine produces $\dot{m}_{\text{paper}} = 30.0\text{ metric tons/h}$ of finished paper containing $5.0\text{ wt}\%\text{ moisture}$ ($95.0\text{ wt}\%\text{ bone-dry fibers}$).
1. The paper web leaves the wire forming section entering the press section at $20.0\text{ wt}\%\text{ dry solids}$.
2. A conventional roll press dewaters the sheet to $42.0\text{ wt}\%\text{ dry solids}$ before entering the steam dryer cylinders.
3. An upgraded extended-nip shoe press dewaters the sheet to $48.0\text{ wt}\%\text{ dry solids}$.
- Evaporating water in the steam dryer consumes $1.40\text{ kg of saturated steam per kg of water evaporated}$.
- Steam cost is $\$35.00\text{ per metric ton of steam}$.

1. Calculate the bone-dry fiber production rate in $\text{kg/h}$.
2. Calculate the mass of water entering the dryer section per hour under:
   - Conventional roll press ($42.0\%$ solids).
   - Shoe press ($48.0\%$ solids).
3. Determine the reduction in water evaporated in the dryer section ($\text{kg/h}$).
4. Calculate the annual steam cost savings (operating $8,400\text{ hours/year}$).""",
                    "solution": r"""### Step 1: Bone-Dry Fiber Production Rate
$$\dot{m}_{\text{dry fiber}} = 0.950 \times 30,000\text{ kg/h} = 28,500\text{ kg/h}$$

### Step 2: Water Entering the Dryer Section
- **Under Conventional Roll Press ($42.0\%\text{ solids}$)**:
  Total wet web mass:
  $$M_{\text{web, 42\%}} = \frac{28,500\text{ kg/h}}{0.420} = 67,857.1\text{ kg/h}$$
  Water in web entering dryer:
  $$W_{42\%} = 67,857.1 - 28,500 = 39,357.1\text{ kg/h}$$

- **Under Extended-Nip Shoe Press ($48.0\%\text{ solids}$)**:
  Total wet web mass:
  $$M_{\text{web, 48\%}} = \frac{28,500\text{ kg/h}}{0.480} = 59,375.0\text{ kg/h}$$
  Water in web entering dryer:
  $$W_{48\%} = 59,375.0 - 28,500 = 30,875.0\text{ kg/h}$$

### Step 3: Reduction in Water Evaporation
Water remaining in final paper product ($5.0\%\text{ moisture}$):
$$W_{\text{final}} = 0.050 \times 30,000\text{ kg/h} = 1,500\text{ kg/h}$$
- Evaporated with roll press: $39,357.1 - 1,500 = 37,857.1\text{ kg/h}$.
- Evaporated with shoe press: $30,875.0 - 1,500 = 29,375.0\text{ kg/h}$.
Reduction in water evaporation:
$$\Delta W_{\text{evap}} = 37,857.1 - 29,375.0 = 8,482.1\text{ kg/h} \approx 8.482\text{ metric tons/h}$$

### Step 4: Steam Consumption & Annual Financial Savings
Hourly steam savings:
$$\dot{m}_{\text{steam saved}} = 8.4821\text{ t water/h} \times 1.40\text{ t steam / t water} = 11.875\text{ metric tons steam/h}$$
Hourly financial savings:
$$\text{Savings/hour} = 11.875\text{ t/h} \times \$35.00\text{/t} = \$415.63\text{/h}$$
Annual savings for $8,400\text{ operating hours}$:
$$\text{Annual Savings} = \$415.63\text{/h} \times 8,400\text{ h/yr} = \$3,491,250\text{/year}$$

Upgrading to an extended-nip shoe press saves **$8.48\text{ t/h}$ of water evaporation** and yields **$\$3,491,250\text{ per year}$** in thermal energy savings.""",
                    "hints": ["Calculate wet sheet mass as dry fiber mass divided by solids fraction.", "Water mass is wet mass minus dry fiber mass."]
                },
                {
                    "id": "prob-6-7",
                    "problemNumber": "6.7",
                    "title": "Rotary Lime Reburning Kiln Thermal Efficiency & Specific Fuel Consumption",
                    "difficulty": "Easy",
                    "statement": r"""A rotary lime kiln reburns lime mud ($\text{CaCO}_3$, $100.09\text{ g/mol}$) to produce $\dot{m}_{\text{lime}} = 200.0\text{ metric tons/day}$ ($8.333\text{ t/h}$) of product lime containing $92.0\text{ wt}\%\text{ active CaO}$ ($56.08\text{ g/mol}$).
- Theoretical endothermic enthalpy of calcination is $\Delta H_{\text{calc}} = 3,180\text{ kJ/kg active CaO}$.
- The lime mud feed contains $25.0\text{ wt}\%\text{ moisture}$ ($75.0\text{ wt}\%\text{ dry solids}$).
- Enthalpy to vaporize moisture and superheat steam to $250^\circ\text{C}$ in the kiln is $2,850\text{ kJ/kg water}$.
- Shell radiation and flue gas sensible heat losses total $1,250\text{ kJ/kg product lime}$.
- The kiln burns natural gas with lower heating value $\text{LHV} = 38,000\text{ kJ/Nm}^3$.

1. Calculate the active $\text{CaO}$ production rate in $\text{kg/h}$.
2. Determine the mass of water entering the kiln with the lime mud per hour.
3. Calculate the total hourly heat duty ($\text{GJ/h}$) and the specific natural gas consumption in $\text{Nm}^3\text{/metric ton of product lime}$.""",
                    "solution": r"""### Step 1: Active $\text{CaO}$ Production Rate
Hourly product lime rate:
$$\dot{m}_{\text{lime}} = 8.333\text{ t/h} = 8,333.3\text{ kg/h}$$
Active $\text{CaO}$ production rate:
$$\dot{m}_{\text{active CaO}} = 0.920 \times 8,333.3\text{ kg/h} = 7,666.7\text{ kg/h}$$

### Step 2: Moisture Entering with Lime Mud
Moles of $\text{CaO}$ produced per hour:
$$\dot{n}_{\text{CaO}} = \frac{7,666.7\text{ kg/h}}{56.08\text{ kg/kmol}} = 136.71\text{ kmol/h}$$
Dry $\text{CaCO}_3$ decomposed:
$$\dot{m}_{\text{CaCO}_3} = 136.71\text{ kmol/h} \times 100.09\text{ kg/kmol} = 13,683.3\text{ kg/h}$$
Including $8.0\%$ unreacted inerts in the product ($666.7\text{ kg/h}$), total dry solids feed:
$$\dot{m}_{\text{dry solids}} = 13,683.3 + 666.7 = 14,350.0\text{ kg/h}$$
Since the feed is $25.0\text{ wt}\%\text{ moisture}$ ($75.0\text{ wt}\%\text{ solids}$):
$$\dot{m}_{\text{water}} = 14,350.0 \times \left(\frac{0.250}{0.750}\right) = 4,783.3\text{ kg water/h}$$

### Step 3: Total Heat Duty & Gas Consumption
1. **Calcination heat**:
   $$\dot{Q}_{\text{calc}} = 7,666.7\text{ kg/h} \times 3,180\text{ kJ/kg} = 2.4380 \times 10^7\text{ kJ/h}$$
2. **Moisture evaporation heat**:
   $$\dot{Q}_{\text{evap}} = 4,783.3\text{ kg/h} \times 2,850\text{ kJ/kg} = 1.3632 \times 10^7\text{ kJ/h}$$
3. **Shell and gas heat losses**:
   $$\dot{Q}_{\text{loss}} = 8,333.3\text{ kg/h} \times 1,250\text{ kJ/kg} = 1.0417 \times 10^7\text{ kJ/h}$$
Total heat duty:
$$\dot{Q}_{\text{total}} = 2.4380 \times 10^7 + 1.3632 \times 10^7 + 1.0417 \times 10^7 = 4.8429 \times 10^7\text{ kJ/h} = 48.429\text{ GJ/h}$$

Natural gas consumption rate:
$$\dot{V}_{\text{gas}} = \frac{4.8429 \times 10^7\text{ kJ/h}}{38,000\text{ kJ/Nm}^3} = 1,274.45\text{ Nm}^3\text{/h}$$
Specific natural gas consumption per metric ton of lime:
$$v_{\text{spec}} = \frac{1,274.45\text{ Nm}^3\text{/h}}{8.333\text{ t/h}} = 152.94\text{ Nm}^3\text{/metric ton product lime}$$

The lime kiln consumes **$48.43\text{ GJ/h}$** of thermal energy, requiring **$152.9\text{ Nm}^3$ of natural gas per metric ton of lime**.""",
                    "hints": ["Sum calcination heat, water evaporation heat, and shell losses.", "Divide total heat by fuel heating value."]
                }
            ]
        }
    ]
    return units
