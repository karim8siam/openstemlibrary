"""
create_env_u3.py
Unit 3: Stratospheric Ozone Dynamics, Halogen Photochemistry & The Montreal Protocol
Covers Chapman cycle, catalytic halogen cycles, Rule of 90, CFC photolysis,
heterogeneous PSC chemistry, polar vortex dynamics, ODP, and Montreal treaties.
Strictly zero prohibited tokens, pure UNIX newlines, pristine KaTeX.
"""

def get_unit_3():
    sections = [
        {
            "id": "sec3_1",
            "title": "Stratospheric Photochemistry & The Classical Chapman Oxygen-Only Steady-State Cycle",
            "content": """The stratospheric ozone layer screens terrestrial life from lethal solar ultraviolet radiation ($\lambda < 290\\text{ nm}$). In 1930, Sydney Chapman formulated the first quantitative photochemical mechanism for atmospheric ozone.

### 1. The Four Elementary Chapman Reactions
The Chapman mechanism consists of four coupled photochemical and kinetic steps operating in an oxygen-only atmosphere:
1. **Photolytic Oxygen Dissociation (Initiation)**:
   Molecular oxygen is dissociated by high-energy solar UV-C radiation ($\lambda < 242\\text{ nm}$):
   \\[ \\text{O}_2 + h\\nu (\\lambda \\le 242\\text{ nm}) \\xrightarrow{J_1} 2\\,\\text{O}(^3P) \\]
2. **Ozone Synthesis (Fast Propagation)**:
   Ground-state triplet oxygen atoms combine with molecular oxygen in a termolecular reaction mediated by a collision bath partner $\\text{M} = \\text{N}_2, \\text{O}_2$:
   \\[ \\text{O}(^3P) + \\text{O}_2 + \\text{M} \\xrightarrow{k_2} \\text{O}_3 + \\text{M} \\]
3. **Ozone Photolysis (Fast Interconversion)**:
   Ozone absorbs actinic UV-B and UV-A radiation ($\lambda < 320\\text{ nm}$, Hartley and Huggins bands):
   \\[ \\text{O}_3 + h\\nu (\\lambda \\le 320\\text{ nm}) \\xrightarrow{J_3} \\text{O}_2 + \\text{O}(^1D) \\]
   followed by collision de-excitation $\\text{O}(^1D) + \\text{M} \\rightarrow \\text{O}(^3P) + \\text{M}$.
4. **Recombination Sink (Termination)**:
   Atomic oxygen recombines with ozone to regenerate two stable diatomic oxygen molecules:
   \\[ \\text{O} + \\text{O}_3 \\xrightarrow{k_4} 2\\,\\text{O}_2 \\]

### 2. Odd Oxygen Family (Ox) and Steady-State Derivation
Because reactions (2) and (3) interconvert atomic oxygen and ozone on a timescale of milliseconds without creating or destroying net oxygen valencies, we define the **odd oxygen family**:
\\[ [\\text{O}_x] \\equiv [\\text{O}] + [\\text{O}_3] \\approx [\\text{O}_3] \\]
(since $[\\text{O}_3] \\gg [\\text{O}]$ below $50\\text{ km}$).
The rapid cycling between $\\text{O}$ and $\\text{O}_3$ yields:
\\[ \\frac{d[\\text{O}]}{dt} = 2 J_1 [\\text{O}_2] + J_3 [\\text{O}_3] - k_2 [\\text{O}][\\text{O}_2][\\text{M}] - k_4 [\\text{O}][\\text{O}_3] \\approx 0 \\]
Since cycling is fast, $J_3 [\\text{O}_3] \\approx k_2 [\\text{O}][\\text{O}_2][\\text{M}]$, which gives the ratio of atomic oxygen to ozone:
\\[ \\frac{[\\text{O}]}{[\\text{O}_3]} = \\frac{J_3}{k_2 [\\text{O}_2][\\text{M}]} \\]
The net rate of change of odd oxygen is governed only by initiation and termination:
\\[ \\frac{d[\\text{O}_x]}{dt} = 2 J_1 [\\text{O}_2] - 2 k_4 [\\text{O}][\\text{O}_3] \\]
At photochemical steady state ($d[\\text{O}_x]/dt = 0$):
\\[ J_1 [\\text{O}_2] = k_4 [\\text{O}][\\text{O}_3] = k_4 \\left( \\frac{J_3 [\\text{O}_3]}{k_2 [\\text{O}_2][\\text{M}]} \\right) [\\text{O}_3] \\]
Solving for the steady-state ozone concentration:
\\[ [\\text{O}_3]_{\\text{Chapman}} = [\\text{O}_2] \\sqrt{\\frac{J_1 k_2 [\\text{M}]}{J_3 k_4}} \\]

### 3. The Chapman Model Discrepancy
While the Chapman model successfully predicts the altitude of the ozone maximum ($\sim 25-30\\text{ km}$), its predicted absolute column ozone abundance exceeds observed satellite measurements by a factor of **two to three**. This fundamental discrepancy proved that non-oxygen catalytic sinks must exist in the natural stratosphere."""
        },
        {
            "id": "sec3_2",
            "title": "Catalytic Ozone Destruction Cycles: HOx, NOx, ClOx, and BrOx Chain Propagation",
            "content": """The overprediction of stratospheric ozone by Chapman's mechanism was resolved by the discovery of catalytic chain cycles involving trace radical species ($X = \\cdot\\text{OH}, \\text{NO}\\cdot, \\text{Cl}\\cdot, \\text{Br}\\cdot$).

### 1. The Classical Catalytic Cycle I
Trace free radical species $X$ destroy odd oxygen through a two-step homogeneous catalytic cycle:
\\[ \\text{Step 1}: \\quad X + \\text{O}_3 \\xrightarrow{k_a} X\\text{O} + \\text{O}_2 \\]
\\[ \\text{Step 2}: \\quad X\\text{O} + \\text{O} \\xrightarrow{k_b} X + \\text{O}_2 \\]
\\[ \\text{Net Reaction}: \\quad \\text{O}_3 + \\text{O} \\rightarrow 2\\,\\text{O}_2 \\]
Because the catalyst radical $X$ is regenerated in Step 2, a single molecule can destroy upwards of $100,000$ ozone molecules before being deactivated into a reservoir species.
The effective odd oxygen loss rate catalyzed by $X$ is:
\\[ -\\left(\\frac{d[\\text{O}_3]}{dt}\\right)_X = 2 k_b [X\\text{O}][\\text{O}] \\]

### 2. The Four Major Catalytic Families
1. **The $\\text{HO}_x$ Cycle (Bates and Nicolet, 1950)**:
   Dominated by hydroxyl ($\cdot\\text{OH}$) and hydroperoxyl ($\\text{HO}_2\\cdot$) radicals generated from the oxidation of water vapor and methane:
   \\[ \\text{O}(^1D) + \\text{H}_2\\text{O} \\rightarrow 2\\,\\cdot\\text{OH} \\]
   Dominates ozone loss in the lower stratosphere ($< 20\\text{ km}$) and upper mesosphere ($> 50\\text{ km}$).
2. **The $\\text{NO}_x$ Cycle (Crutzen, 1970; Johnston, 1971)**:
   Dominated by nitric oxide ($\\text{NO}$) and nitrogen dioxide ($\\text{NO}_2$) produced by the reaction of nitrous oxide with singlet oxygen:
   \\[ \\text{N}_2\\text{O} + \\text{O}(^1D) \\rightarrow 2\\,\\text{NO} \\]
   The $\\text{NO}_x$ cycle accounts for $\\approx 70\\%$ of natural middle-stratosphere ($25-35\\text{ km}$) ozone destruction.
3. **The $\\text{ClO}_x$ Cycle (Molina and Rowland, 1974)**:
   Initiated by the anthropogenic emission and photolysis of chlorofluorocarbons (CFCs):
   \\[ \\text{Cl} + \\text{O}_3 \\rightarrow \\text{ClO} + \\text{O}_2 \\]
   \\[ \\text{ClO} + \\text{O} \\rightarrow \\text{Cl} + \\text{O}_2 \\]
4. **The $\\text{BrO}_x$ Cycle**:
   Bromine radicals (from methyl bromide $\\text{CH}_3\\text{Br}$ and halons) operate via cross-halogen coupling:
   \\[ \\text{ClO} + \\text{BrO} \\rightarrow \\text{Cl} + \\text{Br} + \\text{O}_2 \\]
   Bromine is $\\approx 60$ times more efficient at destroying ozone than chlorine on an atom-for-atom basis because bromine reservoir species are photochemically unstable."""
        },
        {
            "id": "sec3_3",
            "title": "Chlorofluorocarbons (CFCs): Industrial Chemistry & The Rule of 90 Nomenclature",
            "content": """Chlorofluorocarbons (CFCs) are fully halogenated synthetic hydrocarbons synthesized originally by Thomas Midgley Jr. (1928) as non-toxic, non-flammable volatile refrigerants, aerosol propellants, and electronic cleaning solvents.

### 1. The Rule of 90 for CFC, HCFC, and HFC Nomenclature
The standard chemical nomenclature for halogenated alkanes follows the **Rule of 90**:
Given a code number **CFC-$XYZ$** (or HCFC, HFC):
1. Add **90** to the number:
   \\[ N = XYZ + 90 \\]
2. The resulting three digits give the atomic stoichiometry:
   - First digit ($D_1$): Number of **Carbon** atoms ($C$)
   - Second digit ($D_2$): Number of **Hydrogen** atoms ($H$)
   - Third digit ($D_3$): Number of **Fluorine** atoms ($F$)
3. For an acyclic alkane derivative, the total valence saturation is $2C + 2$.
   The remaining valence positions are occupied by **Chlorine** atoms ($Cl$):
   \\[ Cl = (2C + 2) - H - F \\]
4. For cyclic derivatives, a prefix 'C' is added (e.g., C-318), and saturation is $2C$.
5. Isomers with identical formula are distinguished by lower-case letters ($a, b, c$), with the most symmetric isomer having no letter and increasingly asymmetric isomers receiving $a, b, c$.

### 2. Examples of the Rule of 90
- **CFC-11**:
  \\[ 11 + 90 = 101 \\implies C = 1, H = 0, F = 1 \\]
  \\[ Cl = 2(1) + 2 - 0 - 1 = 3 \\implies \\text{CFCl}_3 \\text{ (Trichlorofluoromethane)} \\]
- **CFC-12**:
  \\[ 12 + 90 = 102 \\implies C = 1, H = 0, F = 2 \\]
  \\[ Cl = 4 - 0 - 2 = 2 \\implies \\text{CF}_2\\text{Cl}_2 \\text{ (Dichlorodifluoromethane)} \\]
- **CFC-113**:
  \\[ 113 + 90 = 203 \\implies C = 2, H = 0, F = 3 \\]
  \\[ Cl = 2(2) + 2 - 0 - 3 = 3 \\implies \\text{C}_2\\text{F}_3\\text{Cl}_3 \\text{ (1,1,2-Trichloro-1,2,2-trifluoroethane)} \\]
- **HCFC-22**:
  \\[ 22 + 90 = 112 \\implies C = 1, H = 1, F = 2 \\]
  \\[ Cl = 4 - 1 - 2 = 1 \\implies \\text{CHF}_2\\text{Cl} \\text{ (Chlorodifluoromethane)} \\]
- **HFC-134a**:
  \\[ 134 + 90 = 224 \\implies C = 2, H = 2, F = 4 \\]
  \\[ Cl = 6 - 2 - 4 = 0 \\implies \\text{C}_2\\text{H}_2\\text{F}_4 \\text{ (1,1,1,2-Tetrafluoroethane, no chlorine!)} \\]

### 3. Halon Nomenclature
Fire-extinguishing bromocarbons are designated by four digits: **Halon-$C F Cl Br$**:
- **Halon-1211**: $C=1, F=2, Cl=1, Br=1 \\implies \\text{CF}_2\\text{ClBr}$ (Bromochlorodifluoromethane)
- **Halon-1301**: $C=1, F=3, Cl=0, Br=1 \\implies \\text{CF}_3\\text{Br}$ (Bromotrifluoromethane)
- **Halon-2402**: $C=2, F=4, Cl=0, Br=2 \\implies \\text{C}_2\\text{F}_4\\text{Br}_2$ (1,2-Dibromotetrafluoroethane)"""
        },
        {
            "id": "sec3_4",
            "title": "Photolytic Cleavage of Halocarbons & Stratospheric Halogen Reservoirs",
            "content": """Because fully halogenated CFCs lack $\\text{C-H}$ bonds, they are completely immune to tropospheric oxidation by $\\cdot\\text{OH}$ and have no oceanic dissolution sinks. They persist for $50 - 100+$ years, slowly ascending through the tropical tropopause into the stratosphere.

### 1. Stratospheric Photolysis
In the middle and upper stratosphere ($z > 25\\text{ km}$), CFCs encounter intense, unattenuated solar UV-C radiation in the quartz-UV window ($190 - 220\\text{ nm}$):
\\[ \\text{CF}_2\\text{Cl}_2 + h\\nu (\\lambda \\le 220\\text{ nm}) \\rightarrow \\text{CF}_2\\text{Cl}\\cdot + \\text{Cl}\\cdot \\]
\\[ \\text{CFCl}_3 + h\\nu (\\lambda \\le 220\\text{ nm}) \\rightarrow \\text{CFCl}_2\\cdot + \\text{Cl}\\cdot \\]
Subsequent rapid reaction of the haloalkyl radicals with oxygen liberates all remaining chlorine atoms as active chlorine free radicals.

### 2. Chlorine Deactivation into Reservoir Species
If all released chlorine remained in active forms ($\\text{Cl}\\cdot$ and $\\text{ClO}\\cdot$), the stratospheric ozone layer would have been destroyed completely within decades. Fortunately, active chlorine is rapidly sequestered into stable, non-ozone-destroying **reservoir species**:
1. Reaction with Methane to form Hydrogen Chloride ($\\text{HCl}$):
   \\[ \\text{Cl}\\cdot + \\text{CH}_4 \\xrightarrow{k_1} \\text{HCl} + \\cdot\\text{CH}_3 \\]
2. Reversible combination with Nitrogen Dioxide to form Chlorine Nitrate ($\\text{ClONO}_2$):
   \\[ \\text{ClO}\\cdot + \\text{NO}_2 + \\text{M} \\xrightarrow{k_2} \\text{ClONO}_2 + \\text{M} \\]
Under mid-latitude conditions, over **$99\\%$** of total stratospheric inorganic chlorine ($\\text{Cl}_y = [\\text{Cl}] + [\\text{ClO}] + [\\text{HCl}] + [\\text{ClONO}_2] + [\\text{HOCl}] + 2[\\text{Cl}_2\\text{O}_2]$) is tied up as unreactive $\\text{HCl}$ and $\\text{ClONO}_2$.

### 3. Reservoir Reactivation Pathways
Reservoirs are slowly converted back to active radicals in the gas phase:
\\[ \\text{HCl} + \\cdot\\text{OH} \\rightarrow \\text{Cl}\\cdot + \\text{H}_2\\text{O} \\]
\\[ \\text{ClONO}_2 + h\\nu \\rightarrow \\text{ClO}\\cdot + \\text{NO}_2 \\quad (\\text{or } \\text{Cl}\\cdot + \\text{NO}_3) \\]
In the normal stratosphere, a dynamic steady state maintains active chlorine at $\\sim 1\\%$ of total chlorine."""
        },
        {
            "id": "sec3_5",
            "title": "Heterogeneous Chemistry on Polar Stratospheric Clouds & Chlorine Activation",
            "content": """The catastrophic springtime depletion of Antarctic ozone—the 'Ozone Hole' discovered by Farman, Gardiner, and Shanklin (1985)—defied classical gas-phase kinetics. Its explanation required a paradigm shift: heterogeneous surface catalysis on Polar Stratospheric Clouds (PSCs).

### 1. Polar Stratospheric Cloud (PSC) Microphysics
During the polar winter, the absence of sunlight and strong radiative cooling drop stratospheric temperatures below $195\\text{ K}$ ($-78^\\circ\\text{C}$):
- **Type I PSCs ($T < 195\\text{ K}$)**: Composed of solid crystalline **Nitric Acid Trihydrate (NAT, $\\text{HNO}_3\\cdot 3\\text{H}_2\\text{O}$)** or supercooled ternary solutions (STS, $\\text{HNO}_3 / \\text{H}_2\\text{SO}_4 / \\text{H}_2\\text{O}$).
- **Type II PSCs ($T < 188\\text{ K}$)**: Composed of pure water ice crystals.

### 2. Heterogeneous Chlorine Activation Reactions
On the solid and liquid surfaces of PSC particles, inert chlorine reservoirs react rapidly via surface-catalyzed heterogeneous reactions:
1. Primary Activation Reaction:
   \\[ \\text{HCl}(s) + \\text{ClONO}_2(g) \\xrightarrow{\\text{PSC surface}} \\text{Cl}_2(g) + \\text{HNO}_3(s) \\]
2. Hydrolysis of Chlorine Nitrate:
   \\[ \\text{ClONO}_2(g) + \\text{H}_2\\text{O}(s) \\xrightarrow{\\text{PSC surface}} \\text{HOCl}(g) + \\text{HNO}_3(s) \\]
3. Activation by Hypochlorous Acid:
   \\[ \\text{HCl}(s) + \\text{HOCl}(g) \\xrightarrow{\\text{PSC surface}} \\text{Cl}_2(g) + \\text{H}_2\\text{O}(s) \\]
4. Bromine Activation:
   \\[ \\text{HCl}(s) + \\text{BrONO}_2(g) \\xrightarrow{\\text{PSC surface}} \\text{BrCl}(g) + \\text{HNO}_3(s) \\]

### 3. Denoxification and Denitrification
These heterogeneous reactions have two profound chemical consequences:
- **Chlorine Activation**: The stable reservoirs $\\text{HCl}$ and $\\text{ClONO}_2$ are converted into molecular chlorine ($\\text{Cl}_2$), which builds up in darkness throughout the polar winter.
- **Denoxification**: Reactive $\\text{NO}_x$ is converted into solid $\\text{HNO}_3$ bound inside the PSC crystals.
- **Denitrification**: When large Type II ice crystals grow ($d_p > 10\\ \mu\\text{m}$), they gravitationally settle out of the stratosphere into the troposphere, physically removing reactive nitrogen. Without $\\text{NO}_2$ to reform $\\text{ClONO}_2$, active chlorine remains uninhibited for months."""
        },
        {
            "id": "sec3_6",
            "title": "Antarctic Polar Vortex Dynamics & The ClO Dimer Springtime Destruction Cycle",
            "content": """The springtime collapse of Antarctic ozone is driven by the dynamic confinement of the polar vortex and the Molina-Rowland ClO dimer catalytic cycle.

### 1. Dynamics of the Polar Vortex
During the austral autumn and winter (May to August), intense radiative cooling over the Antarctic continent produces a dense, sinking cold air mass surrounded by a high-velocity circumpolar westerly jet stream ($> 80\\text{ m/s}$) known as the **polar vortex**.
The vortex acts as an impermeable fluid-dynamical barrier, isolating the polar stratosphere and preventing the mixing of warm, ozone-rich air from mid-latitudes.

### 2. The ClO Dimer (Molina) Catalytic Cycle
When the Sun rises over Antarctica in early spring (September), molecular chlorine photolyzes within minutes:
\\[ \\text{Cl}_2 + h\\nu (\\text{visible}) \\rightarrow 2\\,\\text{Cl}\\cdot \\]
The chlorine radicals immediately react with ozone:
\\[ \\text{Cl}\\cdot + \\text{O}_3 \\rightarrow \\text{ClO}\\cdot + \\text{O}_2 \\]
Because atomic oxygen $[\text{O}]$ is extremely low in the cold lower stratosphere, the classical Chapman Step 2 ($\\text{ClO} + \\text{O} \\rightarrow \\text{Cl} + \\text{O}_2$) cannot operate.
Instead, ozone destruction proceeds through the **dichlorine dioxide (ClO dimer) cycle** discovered by Mario Molina:
1. Termolecular formation of the ClO dimer:
   \\[ \\text{ClO}\\cdot + \\text{ClO}\\cdot + \\text{M} \\xrightleftharpoons[k_{-1}]{k_1} \\text{ClOOCl} + \\text{M} \\]
2. Photolysis of dichlorine dioxide:
   \\[ \\text{ClOOCl} + h\\nu (\\lambda < 360\\text{ nm}) \\rightarrow \\text{ClOO}\\cdot + \\text{Cl}\\cdot \\]
3. Rapid thermal unimolecular dissociation of the chloroperoxy radical:
   \\[ \\text{ClOO}\\cdot + \\text{M} \\rightarrow \\text{Cl}\\cdot + \\text{O}_2 + \\text{M} \\]
4. Two ozone molecules consumed:
   \\[ 2\\,(\\text{Cl}\\cdot + \\text{O}_3 \\rightarrow \\text{ClO}\\cdot + \\text{O}_2) \\]
\\[ \\text{Net Cycle}: \\quad 2\\,\\text{O}_3 + h\\nu \\rightarrow 3\\,\\text{O}_2 \\]

### 3. Complete Ozone Annihilation in the Lower Stratosphere
Because the ClO dimer cycle requires **no atomic oxygen**, its rate scales quadratically with active chlorine:
\\[ -\\frac{d[\\text{O}_3]}{dt} = 2 k_1 [\\text{ClO}]^2 [\\text{M}] \\]
Between altitudes of $14\\text{ km}$ and $22\\text{ km}$, this catalytic chain reaction destroys ozone at rates exceeding **$1-2\\%\\text{ per day}$**, completely wiping out over $95\\%$ of all ozone in this layer by early October, creating the Antarctic Ozone Hole."""
        },
        {
            "id": "sec3_7",
            "title": "Ozone Depletion Potential (ODP) Formulations & DNA Photodamage Kinetics",
            "content": """Assessing the ecological impact of ozone-depleting halocarbons requires quantifying relative chemical destruction efficiencies and the biological action spectra of ultraviolet radiation.

### 1. Ozone Depletion Potential (ODP)
The **Ozone Depletion Potential (ODP)** of a halocarbon $i$ is defined as the total calculated steady-state column ozone destruction per unit mass of gas $i$ emitted to the atmosphere, normalized to that of **CFC-11** ($\\text{CFCl}_3$, defined as $\\text{ODP} \\equiv 1.0$):
\\[ \\text{ODP}_i = \\frac{\\Delta [\\text{O}_3]_i / m_i}{\\Delta [\\text{O}_3]_{\\text{CFC-11}} / m_{\\text{CFC-11}}} \\]
A semi-empirical approximation for species $i$ containing $n_{\\text{Cl}}$ chlorine atoms and $n_{\\text{Br}}$ bromine atoms is:
\\[ \\text{ODP}_i \\approx \\frac{M_{\\text{CFC-11}}}{M_i} \\frac{n_{\\text{Cl}} + \\alpha_{\\text{Br}} n_{\\text{Br}}}{3} \\frac{\\tau_i}{\\tau_{\\text{CFC-11}}} f_i \\]
where:
- $\\tau_i$ is the atmospheric lifetime
- $\\alpha_{\\text{Br}} \\approx 60$ is the bromine catalytic enhancement factor
- $f_i$ is the fractional release factor in the stratosphere

### 2. Biological UV Bands and DNA Photodamage
Solar ultraviolet radiation is divided into three wavebands:
- **UV-A ($315 - 400\\text{ nm}$)**: Transmitted freely through the atmosphere; causes cellular oxidative stress and photoaging.
- **UV-B ($280 - 315\\text{ nm}$)**: Strongly absorbed by ozone; biologically hazardous. A $1\\%$ decrease in column ozone yields a $\\approx 1.2 - 1.5\\%$ increase in ground-level UV-B irradiance.
- **UV-C ($100 - 280\\text{ nm}$)**: Completely blocked by stratospheric $\\text{O}_2$ and $\\text{O}_3$.

DNA absorption peaks near $260\\text{ nm}$ and extends into the UV-B band. Absorption induces photochemical dimerization of adjacent thymine or cytosine pyrimidine bases:
\\[ \\text{Thymine} + \\text{Thymine} + h\\nu (\\text{UV-B}) \\rightarrow \\text{Cyclobutane Pyrimidine Dimer (CPD)} \\]
as well as (6-4) photoproducts, halting DNA transcription and polymerase replication, leading to mutagenesis and basal/squamous cell carcinoma and malignant melanoma."""
        },
        {
            "id": "sec3_8",
            "title": "The Montreal Protocol, Global Phasedown Treaties & Hydrofluoroolefins (HFOs)",
            "content": """The global regulatory response to stratospheric ozone depletion is recognized as the most successful multilateral environmental treaty in human history.

### 1. The Montreal Protocol (1987) and Successive Amendments
Signed on September 16, 1987, the **Montreal Protocol on Substances that Deplete the Ozone Layer** established a binding international timetable to freeze and phase down production of CFCs and halons:
- **London Amendment (1990)**: Accelerated phaseout of CFCs, halons, and carbon tetrachloride ($\\text{CCl}_4$) by 2000 for developed nations.
- **Copenhagen Amendment (1992)**: Moved CFC phaseout forward to 1996 and introduced controls on hydrochlorofluorocarbons (HCFCs) and methyl bromide.
- **Beijing Amendment (1999)**: Imposed trade bans on bromochloromethane.
- **Kigali Amendment (2016)**: Extended the Montreal Protocol to phase down **hydrofluorocarbons (HFCs)**. While HFCs have $\\text{ODP} = 0$, they possess massive Global Warming Potentials ($> 1,000-14,000$). The Kigali Amendment will prevent up to $0.5^\\circ\\text{C}$ of warming by 2100.

### 2. Technological Succession of Halocarbon Replacements
The transition away from ozone-depleting substances proceeded across four technological generations:
1. **First Generation: CFCs (e.g., CFC-11, CFC-12)**
   - High ODP ($1.0$), high GWP ($4,750-10,900$), lifetimes $50-100\\text{ yr}$.
2. **Second Generation: HCFCs (e.g., HCFC-22, HCFC-141b)**
   - Contain $\\text{C-H}$ bonds, allowing partial tropospheric oxidation by $\\cdot\\text{OH}$.
   - Lower ODP ($0.05-0.11$), but still ozone-depleting; fully phased out.
3. **Third Generation: HFCs (e.g., HFC-134a, HFC-32, HFC-125)**
   - Contain no chlorine or bromine; $\\text{ODP} \\equiv 0$.
   - High GWP ($1,430$ for HFC-134a), contributing to climate forcing.
4. **Fourth Generation: Hydrofluoroolefins (HFOs, e.g., HFO-1234yf: $\\text{CF}_3\\text{CF}=\\text{CH}_2$)**
   - Contain a reactive $\\text{C}=\\text{C}$ double bond that reacts rapidly with tropospheric $\\cdot\\text{OH}$ ($\tau \\approx 11\\text{ days}$).
   - $\\text{ODP} \\equiv 0$ and $\\text{GWP} < 1$, providing an environmentally benign drop-in replacement for automotive air conditioning."""
        }
    ]

    problems = [
        {
            "id": "prob3_1",
            "tier": "Foundational",
            "title": "Rule of 90 Halocarbon Formula Elucidation",
            "statement": """Using the IUPAC Rule of 90 for halogenated refrigerants:
(a) Determine the complete chemical formula, systematic name, and structure of CFC-11, CFC-12, and CFC-113.
(b) Determine the complete chemical formula of HCFC-142b.
(c) Determine the chemical formula and structure of Halon-1211 and Halon-1301.""",
            "solution": """**(a) Formulation of CFC-11, CFC-12, and CFC-113:**
1. **CFC-11**:
   Add 90: $11 + 90 = 101$.
   - $C = 1$, $H = 0$, $F = 1$.
   - Chlorine atoms: $Cl = 2(1) + 2 - 0 - 1 = 3$.
   - Formula: $\\text{CCl}_3\\text{F}$ (Trichlorofluoromethane).
2. **CFC-12**:
   Add 90: $12 + 90 = 102$.
   - $C = 1$, $H = 0$, $F = 2$.
   - Chlorine atoms: $Cl = 4 - 0 - 2 = 2$.
   - Formula: $\\text{CCl}_2\\text{F}_2$ (Dichlorodifluoromethane).
3. **CFC-113**:
   Add 90: $113 + 90 = 203$.
   - $C = 2$, $H = 0$, $F = 3$.
   - Chlorine atoms: $Cl = 2(2) + 2 - 0 - 3 = 3$.
   - Formula: $\\text{C}_2\\text{Cl}_3\\text{F}_3$ (1,1,2-Trichloro-1,2,2-trifluoroethane).

**(b) Formulation of HCFC-142b:**
Add 90: $142 + 90 = 232$.
- $C = 2$, $H = 3$, $F = 2$.
- Chlorine atoms: $Cl = 2(2) + 2 - 3 - 2 = 1$.
- Formula: $\\text{C}_2\\text{H}_3\\text{ClF}_2$ (1-Chloro-1,1-difluoroethane, isomer 'b').

**(c) Formulation of Halon-1211 and Halon-1301:**
For Halons, digits represent $C - F - Cl - Br$:
1. **Halon-1211**:
   - $C = 1, F = 2, Cl = 1, Br = 1$.
   - Formula: $\\text{CF}_2\\text{ClBr}$ (Bromochlorodifluoromethane).
2. **Halon-1301**:
   - $C = 1, F = 3, Cl = 0, Br = 1$.
   - Formula: $\\text{CF}_3\\text{Br}$ (Bromotrifluoromethane)."""
        },
        {
            "id": "prob3_2",
            "tier": "Foundational",
            "title": "Chapman Steady-State Stratospheric Ozone Concentration",
            "statement": """At an altitude of $z = 30\\text{ km}$ in the tropical stratosphere, the ambient temperature is $T = 230\\text{ K}$ and air density is $[\text{M}] = 3.80 \\times 10^{17}\\text{ molecules/cm}^3$.
Oxygen comprises $21\\%$ of air ($[\text{O}_2] = 8.00 \\times 10^{16}\\text{ molecules/cm}^3$).
The Chapman reaction rate parameters at $230\\text{ K}$ are:
- $J_1 = 3.0 \\times 10^{-12}\\text{ s}^{-1}$ ($\text{O}_2$ photolysis)
- $J_3 = 6.0 \\times 10^{-4}\\text{ s}^{-1}$ ($\text{O}_3$ photolysis)
- $k_2 = 6.0 \\times 10^{-34}\\text{ cm}^6\\text{molecule}^{-2}\\text{s}^{-1}$ ($\text{O} + \text{O}_2 + \text{M} \\rightarrow \text{O}_3 + \text{M}$)
- $k_4 = 1.5 \\times 10^{-15}\\text{ cm}^3\\text{molecule}^{-1}\\text{s}^{-1}$ ($\text{O} + \text{O}_3 \\rightarrow 2\\text{O}_2$)
(a) Calculate the Chapman theoretical steady-state ozone concentration $[\text{O}_3]_{\\text{Chapman}}$ in $\\text{molecules/cm}^3$.
(b) Convert this concentration to a volume mixing ratio in $\\text{ppmv}$.
(c) The actual observed ozone concentration at this altitude is $[\text{O}_3]_{\\text{obs}} \\approx 3.2 \\times 10^{12}\\text{ molecules/cm}^3$. Calculate the percentage by which the Chapman model overestimates ozone, and identify the missing loss mechanism.""",
            "solution": """**(a) Calculation of $[\text{O}_3]_{\\text{Chapman}}$:**
From the Chapman analytical formula:
\\[ [\\text{O}_3] = [\\text{O}_2] \\sqrt{\\frac{J_1 k_2 [\\text{M}]}{J_3 k_4}} \\]
Evaluate the numerator inside the square root:
\\[ J_1 k_2 [\\text{M}] = (3.0 \\times 10^{-12})(6.0 \\times 10^{-34})(3.80 \\times 10^{17}) = 6.840 \\times 10^{-28}\\text{ s}^{-2} \\]
Evaluate the denominator inside the square root:
\\[ J_3 k_4 = (6.0 \\times 10^{-4})(1.5 \\times 10^{-15}) = 9.000 \\times 10^{-19}\\text{ cm}^3\\text{s}^{-2} \\]
Evaluate the quotient:
\\[ \\frac{J_1 k_2 [\\text{M}]}{J_3 k_4} = \\frac{6.840 \\times 10^{-28}}{9.000 \\times 10^{-19}} = 7.600 \\times 10^{-10} \\]
Take the square root:
\\[ \\sqrt{7.600 \\times 10^{-10}} \\approx 2.7568 \\times 10^{-5} \\]
Multiply by $[\\text{O}_2]$:
\\[ [\\text{O}_3]_{\\text{Chapman}} = (8.00 \\times 10^{16}\\text{ molecules/cm}^3)(2.7568 \\times 10^{-5}) = 2.205 \\times 10^{12}\\text{ molecules/cm}^3 \\]
*(At $30\\text{ km}$ peak conditions, Chapman yields $7-9 \\times 10^{12}$ when fully integrated across all solar zenith angles).*

**(b) Mixing Ratio in $\\text{ppmv}$:**
\\[ \\chi_{\\text{O}_3} = \\frac{[\\text{O}_3]}{[\\text{M}]} = \\frac{2.205 \\times 10^{12}}{3.80 \\times 10^{17}} \\approx 5.80 \\times 10^{-6} = 5.80\\text{ ppmv} \\]

**(c) Discrepancy with Observations:**
Global satellite measurements indicate that Chapman-only chemistry predicts roughly $2.5\\times$ more column ozone than is observed because it neglects catalytic chain cycles ($\\text{NO}_x, \\text{HO}_x, \\text{ClO}_x$, and $\\text{BrO}_x$), which account for over $70\\%$ of natural odd oxygen destruction."""
        },
        {
            "id": "prob3_3",
            "tier": "Foundational",
            "title": "Chlorine Catalytic Chain Length and Destruction Efficiency",
            "statement": """In the mid-latitude stratosphere at $35\\text{ km}$, a single chlorine radical $\\text{Cl}\\cdot$ is released via CFC photolysis.
The rate of ozone destruction in the catalytic cycle:
\\[ \\text{Cl} + \\text{O}_3 \\rightarrow \\text{ClO} + \\text{O}_2 \\quad (k_a = 2.8 \\times 10^{-11}\\text{ cm}^3/\\text{s}, [\\text{O}_3] = 2.0 \\times 10^{12}\\text{ cm}^{-3}) \\]
\\[ \\text{ClO} + \\text{O} \\rightarrow \\text{Cl} + \\text{O}_2 \\quad (k_b = 3.8 \\times 10^{-11}\\text{ cm}^3/\\text{s}, [\\text{O}] = 1.5 \\times 10^8\\text{ cm}^{-3}) \\]
The termination reaction deactivating $\\text{Cl}\\cdot$ into the $\\text{HCl}$ reservoir is:
\\[ \\text{Cl} + \\text{CH}_4 \\rightarrow \\text{HCl} + \\cdot\\text{CH}_3 \\quad (k_t = 1.0 \\times 10^{-13}\\text{ cm}^3/\\text{s}, [\\text{CH}_4] = 1.2 \\times 10^{11}\\text{ cm}^{-3}) \\]
(a) Determine which elementary reaction ($a$ or $b$) is the rate-determining step of the catalytic cycle.
(b) Calculate the turnover frequency (cycles per second) of the catalytic cycle.
(c) Calculate the chain length $\\nu$ (the average number of ozone molecules destroyed by one chlorine radical before it is terminated into $\\text{HCl}$).""",
            "solution": """**(a) Rate-Determining Step:**
Evaluate the pseudo-first-order frequencies for both steps:
For Step a:
\\[ r_a = k_a [\\text{O}_3] = (2.8 \\times 10^{-11}\\text{ cm}^3/\\text{s})(2.0 \\times 10^{12}\\text{ cm}^{-3}) = 56.0\\text{ s}^{-1} \\]
For Step b:
\\[ r_b = k_b [\\text{O}] = (3.8 \\times 10^{-11}\\text{ cm}^3/\\text{s})(1.5 \\times 10^8\\text{ cm}^{-3}) = 5.70 \\times 10^{-3}\\text{ s}^{-1} \\]
Because $r_b \\ll r_a$, **Step b** ($\\text{ClO} + \\text{O} \\rightarrow \\text{Cl} + \\text{O}_2$) is the **rate-determining step** by over four orders of magnitude! Most active chlorine resides as $\\text{ClO}$ rather than $\\text{Cl}$.

**(b) Turnover Frequency of the Catalytic Cycle:**
The overall catalytic cycle turnover frequency is determined by the rate-determining step:
\\[ \\nu_{\\text{cycle}} = r_b = 5.70 \\times 10^{-3}\\text{ cycles/s} \\]
*(One complete cycle takes $\\tau_{\\text{cycle}} = 1 / r_b \\approx 175\\text{ seconds}$).*

**(c) Catalytic Chain Length $\\nu$:**
The probability of termination per cycle is the ratio of the termination rate to the propagation rate:
Termination frequency of $\\text{Cl}$:
\\[ r_t = k_t [\\text{CH}_4] = (1.0 \\times 10^{-13}\\text{ cm}^3/\\text{s})(1.2 \\times 10^{11}\\text{ cm}^{-3}) = 1.20 \\times 10^{-2}\\text{ s}^{-1} \\]
Fraction of active chlorine in $\\text{Cl}$ form:
\\[ f_{\\text{Cl}} = \\frac{[\\text{Cl}]}{[\\text{Cl}] + [\\text{ClO}]} \\approx \\frac{r_b}{r_a} = \\frac{5.70 \\times 10^{-3}}{56.0} \\approx 1.018 \\times 10^{-4} \\]
The effective termination frequency of active chlorine ($\\text{ClO}_x$) is:
\\[ R_{\\text{term}} = r_t \\times f_{\\text{Cl}} = (1.20 \\times 10^{-2}\\text{ s}^{-1})(1.018 \\times 10^{-4}) = 1.222 \\times 10^{-6}\\text{ s}^{-1} \\]
The catalytic chain length is:
\\[ \\nu = \\frac{\\text{Rate of Ozone Loss}}{\\text{Rate of Termination}} = \\frac{\\nu_{\\text{cycle}}}{R_{\\text{term}}} = \\frac{5.70 \\times 10^{-3}\\text{ s}^{-1}}{1.222 \\times 10^{-6}\\text{ s}^{-1}} \\approx 4,664 \\approx 4.7 \\times 10^3 \\]
*(Over its active lifetime before irreversible removal to the troposphere, including reservoir re-activation by $\\cdot\\text{OH}$, a single chlorine atom destroys $\\sim 100,000$ ozone molecules).*"""
        },
        {
            "id": "prob3_4",
            "tier": "Intermediate",
            "title": "Heterogeneous PSC Chlorine Activation and Denitrification Stoichiometry",
            "statement": """Prior to polar sunrise over Antarctica, an isolated stratospheric vortex air parcel at $18\\text{ km}$ ($T = 190\\text{ K}$, $[\text{M}] = 2.0 \\times 10^{18}\\text{ molecules/cm}^3$) contains:
- Hydrogen chloride: $[\text{HCl}] = 1.80\\text{ ppbv}$
- Chlorine nitrate: $[\text{ClONO}_2] = 1.10\\text{ ppbv}$
- Water vapor: $[\text{H}_2\text{O}] = 4.0\\text{ ppmv}$
Type I PSCs form, driving the heterogeneous reaction:
\\[ \\text{HCl}(s) + \\text{ClONO}_2(g) \\rightarrow \\text{Cl}_2(g) + \\text{HNO}_3(s) \\]
and the secondary reaction:
\\[ \\text{H}_2\\text{O}(s) + \\text{ClONO}_2(g) \\rightarrow \\text{HOCl}(g) + \\text{HNO}_3(s) \\]
(a) Determine the limiting reactant and calculate the final concentrations (in ppbv) of $\\text{Cl}_2$, $\\text{ClONO}_2$, $\\text{HCl}$, and solid $\\text{HNO}_3$ produced.
(b) If $\\text{H}_2\\text{O}$ then reacts with any remaining $\\text{ClONO}_2$, determine the final concentration of $\\text{HOCl}$.
(c) When polar sunrise occurs, $\\text{Cl}_2$ is photolyzed quantitatively into active $\\text{Cl}\\cdot$ radicals. Calculate the concentration of active atomic chlorine produced in $\\text{molecules/cm}^3$.""",
            "solution": """**(a) Primary Heterogeneous Reaction Stoichiometry:**
The primary reaction is:
\\[ \\text{HCl}(s) + \\text{ClONO}_2(g) \\rightarrow \\text{Cl}_2(g) + \\text{HNO}_3(s) \\]
Initial concentrations:
- $[\text{HCl}]_0 = 1.80\\text{ ppbv}$
- $[\text{ClONO}_2]_0 = 1.10\\text{ ppbv}$

Because the stoichiometric ratio is $1:1$, $\\text{ClONO}_2$ is the **limiting reactant** ($1.10 < 1.80$).
- Extent of reaction: $\\xi = 1.10\\text{ ppbv}$.
Products and remaining reactants:
- $[\\text{Cl}_2] = 1.10\\text{ ppbv}$
- $[\\text{HNO}_3(s)] = 1.10\\text{ ppbv}$
- $[\\text{ClONO}_2] = 1.10 - 1.10 = 0.00\\text{ ppbv}$ (completely consumed)
- $[\\text{HCl}] = 1.80 - 1.10 = 0.70\\text{ ppbv}$ (unreacted excess)

**(b) Secondary Reaction with $\\text{H}_2\\text{O}$:**
Because all $\\text{ClONO}_2$ was consumed in the first reaction, $[\text{ClONO}_2] = 0$.
Therefore, the secondary hydrolysis reaction cannot proceed:
\\[ [\\text{HOCl}] = 0.00\\text{ ppbv} \\]

**(c) Concentration of Active Chlorine Radicals after Sunrise:**
Each molecule of $\\text{Cl}_2$ photolyzes to yield two chlorine atoms:
\\[ \\text{Cl}_2 + h\\nu \\rightarrow 2\\,\\text{Cl}\\cdot \\]
Mixing ratio of $\\text{Cl}\\cdot$:
\\[ \\chi_{\\text{Cl}} = 2 \\times [\\text{Cl}_2] = 2 \\times 1.10\\text{ ppbv} = 2.20\\text{ ppbv} \\]
Convert to absolute number density:
\\[ [\\text{Cl}\\cdot] = (2.20 \\times 10^{-9}) \\times (2.0 \\times 10^{18}\\text{ molecules/cm}^3) = 4.40 \\times 10^9\\text{ atoms/cm}^3 \\]
*Significance*: This massive surge of active chlorine (over $4 \\times 10^9\\text{ atoms/cm}^3$) in the absence of gaseous $\\text{NO}_2$ leads to immediate catalytic destruction of ozone via the ClO dimer cycle."""
        },
        {
            "id": "prob3_5",
            "tier": "Intermediate",
            "title": "Molina ClO Dimer Kinetics and Ozone Depletion Rate in the Polar Vortex",
            "statement": """During early October inside the Antarctic polar vortex at $18\\text{ km}$, active chlorine has accumulated such that $[\text{ClO}] = 1.50\\text{ ppbv}$ in an air density of $[\text{M}] = 2.10 \\times 10^{18}\\text{ molecules/cm}^3$ at $T = 195\\text{ K}$.
The rate-limiting step of the ClO dimer cycle is the termolecular formation of dichlorine dioxide:
\\[ \\text{ClO} + \\text{ClO} + \\text{M} \\xrightarrow{k_1} \\text{ClOOCl} + \\text{M} \\]
where at $195\\text{ K}$, $k_1 = 1.60 \\times 10^{-31}\\text{ cm}^6\\text{molecule}^{-2}\\text{s}^{-1}$.
Every turn of the ClO dimer cycle destroys exactly two ozone molecules:
\\[ -\\frac{d[\\text{O}_3]}{dt} = 2 k_1 [\\text{ClO}]^2 [\\text{M}] \\]
Assume sunlight is present for 12 hours per day.
The initial ambient ozone concentration is $[\text{O}_3]_0 = 2.00\\text{ ppmv}$.
(a) Calculate the daily rate of ozone destruction $-\\frac{d[\\text{O}_3]}{dt}$ in $\\text{molecules}/(\\text{cm}^3\\cdot\\text{day})$ and in $\\text{ppmv/day}$.
(b) Calculate the percentage of ozone destroyed per day.
(c) Assuming constant conditions, calculate how many days are required to deplete $90\\%$ of the local ozone layer.""",
            "solution": """**(a) Daily Ozone Destruction Rate:**
Convert concentrations to $\\text{molecules/cm}^3$:
\\[ [\\text{ClO}] = (1.50 \\times 10^{-9})(2.10 \\times 10^{18}) = 3.15 \\times 10^9\\text{ molecules/cm}^3 \\]
\\[ [\\text{M}] = 2.10 \\times 10^{18}\\text{ molecules/cm}^3 \\]
Rate of reaction during daylight:
\\[ -\\left(\\frac{d[\\text{O}_3]}{dt}\\right)_{\\text{sun}} = 2 k_1 [\\text{ClO}]^2 [\\text{M}] \\]
\\[ [\\text{ClO}]^2 = (3.15 \\times 10^9)^2 = 9.9225 \\times 10^{18}\\text{ cm}^{-6} \\]
\\[ -\\left(\\frac{d[\\text{O}_3]}{dt}\\right)_{\\text{sun}} = 2 (1.60 \\times 10^{-31})(9.9225 \\times 10^{18})(2.10 \\times 10^{18}) \\]
\\[ -\\left(\\frac{d[\\text{O}_3]}{dt}\\right)_{\\text{sun}} = (3.20 \\times 10^{-31})(2.0837 \\times 10^{37}) = 6.668 \\times 10^6\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s}) \\]
With 12 hours of sunlight per day ($t_{\\text{sun}} = 12 \\times 3600 = 43,200\\text{ s}$):
\\[ \\Delta [\\text{O}_3]_{\\text{day}} = (6.668 \\times 10^6\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s})) \\times 43,200\\text{ s} = 2.880 \\times 10^{11}\\text{ molecules}/(\\text{cm}^3\\cdot\\text{day}) \\]
Convert to mixing ratio:
\\[ \\Delta \\chi_{\\text{O}_3} = \\frac{2.880 \\times 10^{11}}{2.10 \\times 10^{18}} \\approx 1.371 \\times 10^{-7} = 0.1371\\text{ ppmv/day} \\]

**(b) Percentage Ozone Depleted per Day:**
Initial ozone:
\\[ [\\text{O}_3]_0 = 2.00\\text{ ppmv} \\]
\\[ \\% \\text{ Loss per day} = \\frac{0.1371\\text{ ppmv/day}}{2.00\\text{ ppmv}} \\times 100\\% \\approx 6.86\\%\\text{ per day} \\]

**(c) Time to Deplete $90\\%$ of Ozone:**
$90\\%$ depletion represents:
\\[ \\Delta [\\text{O}_3]_{90} = 0.90 \\times 2.00\\text{ ppmv} = 1.80\\text{ ppmv} \\]
Assuming a constant destruction rate:
\\[ t = \\frac{1.80\\text{ ppmv}}{0.1371\\text{ ppmv/day}} \\approx 13.1\\text{ days} \\]
*Insight*: Within less than two weeks, the ClO dimer cycle wipes out virtually all ozone in this polar stratospheric layer, explaining the sudden formation of the Ozone Hole in early spring."""
        },
        {
            "id": "prob3_6",
            "tier": "Intermediate",
            "title": "Semi-Empirical Ozone Depletion Potential (ODP) Calculation",
            "statement": """The semi-empirical Ozone Depletion Potential (ODP) of halocarbon $i$ is calculated using:
\\[ \\text{ODP}_i = \\frac{M_{\\text{CFC-11}}}{M_i} \\left( \\frac{n_{\\text{Cl}} + \\alpha_{\\text{Br}} n_{\\text{Br}}}{3} \\right) \\left( \\frac{\\tau_i}{\\tau_{\\text{CFC-11}}} \\right) \\frac{f_i}{f_{\\text{CFC-11}}} \\]
For benchmark CFC-11 ($\text{CFCl}_3$):
- Molecular weight $M_{\\text{CFC-11}} = 137.37\\text{ g/mol}$
- $n_{\\text{Cl}} = 3, n_{\\text{Br}} = 0$
- Lifetime $\\tau_{\\text{CFC-11}} = 52.0\\text{ years}$
- Fractional release factor $f_{\\text{CFC-11}} = 1.00$
Parameters for candidate compounds:
- **Halon-1301 ($\text{CF}_3\text{Br}$)**: $M = 148.91\\text{ g/mol}, n_{\\text{Cl}} = 0, n_{\\text{Br}} = 1, \\tau = 65.0\\text{ yr}, f = 0.28, \\alpha_{\\text{Br}} = 65$.
- **HCFC-22 ($\text{CHF}_2\text{Cl}$)**: $M = 86.47\\text{ g/mol}, n_{\\text{Cl}} = 1, n_{\\text{Br}} = 0, \\tau = 12.0\\text{ yr}, f = 0.35$.
- **HFC-134a ($\text{CH}_2\text{FCF}_3$ hold zero halogens)**: $n_{\\text{Cl}} = 0, n_{\\text{Br}} = 0$.
(a) Calculate the theoretical ODP of Halon-1301.
(b) Calculate the theoretical ODP of HCFC-22.
(c) State the ODP of HFC-134a and evaluate why switching from CFC-12 to HFC-134a solved the ozone depletion problem but posed a climate warming challenge.""",
            "solution": """**(a) ODP of Halon-1301 ($\text{CF}_3\text{Br}$):**
\\[ \\text{ODP} = \\left(\\frac{137.37}{148.91}\\right) \\left( \\frac{0 + 65(1)}{3} \\right) \\left( \\frac{65.0}{52.0} \\right) \\left(\\frac{0.28}{1.00}\\right) \\]
Evaluate term by term:
\\[ \\frac{137.37}{148.91} = 0.9225 \\]
\\[ \\frac{65}{3} = 21.667 \\]
\\[ \\frac{65.0}{52.0} = 1.250 \\]
Multiply all terms:
\\[ \\text{ODP} = 0.9225 \\times 21.667 \\times 1.250 \\times 0.28 = 24.985 \\times 0.28 \\approx 6.996 \\approx 7.0 \\]
*Note*: Because bromine is $65\\times$ more destructive than chlorine, Halon-1301 has an enormous ODP of $\\approx 7-10$, explaining why halons were phased out with high priority under the Montreal Protocol.

**(b) ODP of HCFC-22 ($\text{CHF}_2\text{Cl}$):**
\\[ \\text{ODP} = \\left(\\frac{137.37}{86.47}\\right) \\left( \\frac{1 + 0}{3} \\right) \\left( \\frac{12.0}{52.0} \\right) \\left(\\frac{0.35}{1.00}\\right) \\]
Evaluate term by term:
\\[ \\frac{137.37}{86.47} = 1.5886 \\]
\\[ \\frac{1}{3} = 0.3333 \\]
\\[ \\frac{12.0}{52.0} = 0.2308 \\]
Multiply all terms:
\\[ \\text{ODP} = 1.5886 \\times 0.3333 \\times 0.2308 \\times 0.35 = 0.5295 \\times 0.08077 \\approx 0.0428 \\approx 0.043 \\]
*(HCFC-22 has an ODP of $\\approx 0.04-0.05$, about $20\\times$ lower than CFC-11).*

**(c) Evaluation of HFC-134a:**
Because HFC-134a contains neither chlorine nor bromine ($n_{\\text{Cl}} = 0, n_{\\text{Br}} = 0$):
\\[ \\text{ODP}_{\\text{HFC-134a}} \\equiv 0.00 \\]
It poses zero threat to the stratospheric ozone layer. However, HFC-134a has a 100-year Global Warming Potential of $\\text{GWP} = 1430$, acting as a potent greenhouse gas. This necessitated the 2016 **Kigali Amendment** to phase down HFCs in favor of fourth-generation Hydrofluoroolefins (HFOs)."""
        },
        {
            "id": "prob3_7",
            "tier": "Advanced",
            "title": "Cross-Halogen ClO-BrO Catalytic Cycle Kinetics",
            "statement": """In the lower polar stratosphere, the cross-halogen cycle between chlorine monoxide and bromine monoxide provides an alternate pathway for ozone destruction that does not require atomic oxygen:
\\[ \\text{Step 1}: \\quad \\text{ClO} + \\text{BrO} \\xrightarrow{k_{1a}} \\text{Br} + \\text{Cl} + \\text{O}_2 \\quad (50\\%) \\]
\\[ \\text{Step 2}: \\quad \\text{ClO} + \\text{BrO} \\xrightarrow{k_{1b}} \\text{BrCl} + \\text{O}_2 \\quad (50\\%) \\]
\\[ \\text{followed by rapid photolysis of } \\text{BrCl} + h\\nu \\rightarrow \\text{Br} + \\text{Cl} \\]
\\[ \\text{Step 3}: \\quad \\text{Cl} + \\text{O}_3 \\rightarrow \\text{ClO} + \\text{O}_2 \\]
\\[ \\text{Step 4}: \\quad \\text{Br} + \\text{O}_3 \\rightarrow \\text{BrO} + \\text{O}_2 \\]
\\[ \\text{Net Reaction}: \\quad 2\\,\\text{O}_3 \\rightarrow 3\\,\\text{O}_2 \\]
At $T = 200\\text{ K}$, the overall rate constant is $k_1 = k_{1a} + k_{1b} = 1.50 \\times 10^{-11}\\text{ cm}^3\\text{molecule}^{-1}\\text{s}^{-1}$.
In a polar vortex air parcel with $[\text{M}] = 2.0 \\times 10^{18}\\text{ cm}^{-3}$:
- $[\text{ClO}] = 1.20\\text{ ppbv}$
- $[\text{BrO}] = 15.0\\text{ pptv}$
(a) Write the rate law for ozone destruction by this cycle.
(b) Calculate the instantaneous ozone loss rate in $\\text{molecules}/(\\text{cm}^3\\cdot\\text{s})$ and in $\\text{ppbv/hr}$.
(c) Compare this rate to the ClO dimer cycle operating in the same parcel ($k_{\\text{dimer}}[\\text{M}] = 3.20 \\times 10^{-13}\\text{ cm}^3/\\text{s}$) and determine the percentage contribution of bromine to total polar ozone destruction.""",
            "solution": """**(a) Rate Law for the ClO-BrO Cross Cycle:**
Each reaction of $\\text{ClO}$ with $\\text{BrO}$ destroys exactly two ozone molecules:
\\[ -\\left(\\frac{d[\\text{O}_3]}{dt}\\right)_{\\text{Cl-Br}} = 2 k_1 [\\text{ClO}][\\text{BrO}] \\]

**(b) Instantaneous Ozone Loss Rate:**
Convert concentrations to $\\text{molecules/cm}^3$:
\\[ [\\text{ClO}] = (1.20 \\times 10^{-9})(2.0 \\times 10^{18}) = 2.40 \\times 10^9\\text{ molecules/cm}^3 \\]
\\[ [\\text{BrO}] = (15.0 \\times 10^{-12})(2.0 \\times 10^{18}) = 3.00 \\times 10^7\\text{ molecules/cm}^3 \\]
Evaluate the rate:
\\[ -\\left(\\frac{d[\\text{O}_3]}{dt}\\right)_{\\text{Cl-Br}} = 2 (1.50 \\times 10^{-11}\\text{ cm}^3/\\text{s})(2.40 \\times 10^9\\text{ cm}^{-3})(3.00 \\times 10^7\\text{ cm}^{-3}) \\]
\\[ = (3.00 \\times 10^{-11}) \\times (7.20 \\times 10^{16}) = 2.160 \\times 10^6\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s}) \\]
Convert to $\\text{ppbv/hr}$:
\\[ \\text{Rate (ppbv/s)} = \\frac{2.160 \\times 10^6}{2.0 \\times 10^{18}} \\times 10^9 = 1.080 \\times 10^{-3}\\text{ ppbv/s} \\]
\\[ \\text{Rate (ppbv/hr)} = (1.080 \\times 10^{-3}\\text{ ppbv/s}) \\times 3600\\text{ s/hr} = 3.888\\text{ ppbv/hr} \\approx 3.89\\text{ ppbv/hr} \\]

**(c) Comparison with ClO Dimer Cycle:**
The ClO dimer loss rate is:
\\[ -\\left(\\frac{d[\\text{O}_3]}{dt}\\right)_{\\text{dimer}} = 2 (k_{\\text{dimer}}[\\text{M}]) [\\text{ClO}]^2 \\]
\\[ = 2 (3.20 \\times 10^{-13}\\text{ cm}^3/\\text{s}) (2.40 \\times 10^9\\text{ cm}^{-3})^2 \\]
\\[ = (6.40 \\times 10^{-13}) \\times (5.76 \\times 10^{18}) = 3.686 \\times 10^6\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s}) \\]
Total ozone destruction rate:
\\[ R_{\\text{total}} = R_{\\text{dimer}} + R_{\\text{Cl-Br}} = 3.686 \\times 10^6 + 2.160 \\times 10^6 = 5.846 \\times 10^6\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s}) \\]
Percentage contribution of the bromine cross-cycle:
\\[ \\%_{\\text{Br}} = \\frac{2.160 \\times 10^6}{5.846 \\times 10^6} \\times 100\\% \\approx 36.95\\% \\approx 37\\% \\]
*Conclusion*: Even though bromine is present at only $15\\text{ pptv}$ ($80\\times$ less abundant than chlorine), it accounts for nearly **$37\\%$** of total springtime polar ozone destruction due to the high rate constant $k_1$."""
        },
        {
            "id": "prob3_8",
            "tier": "Advanced",
            "title": "UV-B Radiative Transfer and DNA Action Spectrum Convolution",
            "statement": """Solar spectral irradiance at the top of the atmosphere at wavelength $\lambda = 305\\text{ nm}$ is $F_0 = 0.55\\text{ W}/(\\text{m}^2\\cdot\\text{nm})$.
The effective extinction of UV-B through the atmosphere is governed by the Beer-Lambert-Bouguer law:
\\[ F(\\lambda) = F_0(\\lambda) \\exp\\left( -\\frac{\\sigma_{\\text{O}_3}(\\lambda) \\Omega_{\\text{O}_3}}{\\cos\\theta_z} - \\tau_{\\text{Rayleigh}}(\\lambda) \\right) \\]
where:
- Solar zenith angle $\\theta_z = 30^\\circ$ ($\cos\\theta_z = 0.866$)
- Rayleigh optical depth $\\tau_{\\text{Rayleigh}}(305\\text{ nm}) = 1.05$
- Ozone absorption cross-section $\\sigma_{\\text{O}_3}(305\\text{ nm}) = 4.80 \\times 10^{-19}\\text{ cm}^2/\\text{molecule}$
- Column ozone $\\Omega_{\\text{O}_3}$ is measured in Dobson Units ($1\\text{ DU} = 2.687 \\times 10^{16}\\text{ molecules/cm}^2$).
(a) Calculate the ground-level spectral irradiance $F(305\\text{ nm})$ for an unperturbed ozone column $\\Omega_1 = 350\\text{ DU}$.
(b) Calculate $F(305\\text{ nm})$ during an Ozone Hole event with $\\Omega_2 = 150\\text{ DU}$.
(c) The biological DNA damage action weighting factor at $305\\text{ nm}$ is $\\epsilon_{\\text{DNA}}(305) = 1.80 \\times 10^{-3}\\text{ relative units}$. Calculate the biologically effective DNA damage irradiance $E_{\\text{eff}} = F \\times \\epsilon_{\\text{DNA}}$ for both cases and compute the percentage increase in DNA-damaging UV-B flux.""",
            "solution": """**(a) Ground-Level Irradiance for $\\Omega_1 = 350\\text{ DU}$:**
Convert Dobson Units to column number density:
\\[ \\Omega_1 = 350 \\times (2.687 \\times 10^{16}) = 9.4045 \\times 10^{18}\\text{ molecules/cm}^2 \\]
Ozone optical depth:
\\[ \\tau_{\\text{O}_3,1} = \\sigma_{\\text{O}_3} \\Omega_1 = (4.80 \\times 10^{-19}\\text{ cm}^2)(9.4045 \\times 10^{18}\\text{ cm}^{-2}) = 4.5142 \\]
Slant optical path:
\\[ \\tau_{\\text{slant},1} = \\frac{\\tau_{\\text{O}_3,1}}{\\cos\\theta_z} + \\tau_{\\text{Rayleigh}} = \\frac{4.5142}{0.866} + 1.05 = 5.2127 + 1.05 = 6.2627 \\]
Transmission:
\\[ T_1 = \\exp(-6.2627) = 1.906 \\times 10^{-3} \\]
Ground irradiance:
\\[ F_1(305\\text{ nm}) = F_0 \\times T_1 = (0.55\\text{ W}/(\\text{m}^2\\cdot\\text{nm})) \\times (1.906 \\times 10^{-3}) \\approx 1.048 \\times 10^{-3}\\text{ W}/(\\text{m}^2\\cdot\\text{nm}) \\]

**(b) Ground-Level Irradiance for $\\Omega_2 = 150\\text{ DU}$:**
Column density:
\\[ \\Omega_2 = 150 \\times (2.687 \\times 10^{16}) = 4.0305 \\times 10^{18}\\text{ molecules/cm}^2 \\]
Ozone optical depth:
\\[ \\tau_{\\text{O}_3,2} = (4.80 \\times 10^{-19})(4.0305 \\times 10^{18}) = 1.9346 \\]
Slant optical path:
\\[ \\tau_{\\text{slant},2} = \\frac{1.9346}{0.866} + 1.05 = 2.2340 + 1.05 = 3.2840 \\]
Transmission:
\\[ T_2 = \\exp(-3.2840) = 3.7478 \\times 10^{-2} \\]
Ground irradiance:
\\[ F_2(305\\text{ nm}) = 0.55 \\times (3.7478 \\times 10^{-2}) \\approx 2.061 \\times 10^{-2}\\text{ W}/(\\text{m}^2\\cdot\\text{nm}) \\]

**(c) Biologically Effective DNA Irradiance and Ratio:**
1. For $\\Omega = 350\\text{ DU}$:
   \\[ E_{\\text{eff},1} = (1.048 \\times 10^{-3}) \\times (1.80 \\times 10^{-3}) = 1.886 \\times 10^{-6}\\text{ W/m}^2 \\]
2. For $\\Omega = 150\\text{ DU}$:
   \\[ E_{\\text{eff},2} = (2.061 \\times 10^{-2}) \\times (1.80 \\times 10^{-3}) = 3.710 \\times 10^{-5}\\text{ W/m}^2 \\]
Ratio of increase:
\\[ \\frac{E_{\\text{eff},2}}{E_{\\text{eff},1}} = \\frac{3.710 \\times 10^{-5}}{1.886 \\times 10^{-6}} \\approx 19.67 \\]
*Result*: A reduction of column ozone from $350\\text{ DU}$ to $150\\text{ DU}$ causes a **$19.7\\text{-fold}$ ($1867\\%$) increase** in biologically damaging UV-B radiation at $305\\text{ nm}$, demonstrating the extreme exponential non-linearity of the ozone radiation shield."""
        },
        {
            "id": "prob3_9",
            "tier": "Advanced",
            "title": "Stratospheric Halon-1211 Lifetime and Atmospheric Burden Decay",
            "statement": """Following global compliance with the Montreal Protocol, emissions of Halon-1211 ($\\text{CF}_2\\text{ClBr}$) ceased. The global atmospheric burden of Halon-1211 decays according to first-order loss:
\\[ \\frac{dM}{dt} = -k_{\\text{tot}} M = -\\left( \\frac{1}{\\tau_{\\text{strat}}} + \\frac{1}{\\tau_{\\text{ocean}}} + \\frac{1}{\\tau_{h\\nu,\\text{trop}}} \\right) M \\]
The individual sink lifetimes are:
- Stratospheric photolysis: $\\tau_{\\text{strat}} = 24.0\\text{ years}$
- Ocean dissolution & hydrolysis: $\\tau_{\\text{ocean}} = 80.0\\text{ years}$
- Tropospheric direct photolysis: $\\tau_{h\\nu,\\text{trop}} = 45.0\\text{ years}$
At the phaseout freeze date, the global atmospheric burden was $M_0 = 85.0\\text{ Gg}$ ($85,000\\text{ metric tons}$).
(a) Calculate the total effective atmospheric lifetime $\\tau_{\\text{eff}}$ and the overall first-order decay rate constant $k_{\\text{tot}}$ in $\\text{yr}^{-1}$.
(b) Calculate the atmospheric burden $M(t)$ remaining after 10, 25, and 50 years.
(c) Calculate how many years are required for the global atmospheric burden of Halon-1211 to decline to less than $5\\%$ of its peak value.""",
            "solution": """**(a) Total Effective Atmospheric Lifetime:**
The total loss frequency is the sum of the reciprocal lifetimes:
\\[ \\frac{1}{\\tau_{\\text{eff}}} = \\frac{1}{\\tau_{\\text{strat}}} + \\frac{1}{\\tau_{\\text{ocean}}} + \\frac{1}{\\tau_{h\\nu,\\text{trop}}} \\]
Substitute the values:
\\[ \\frac{1}{\\tau_{\\text{eff}}} = \\frac{1}{24.0} + \\frac{1}{80.0} + \\frac{1}{45.0} \\]
\\[ \\frac{1}{24.0} = 0.041667\\text{ yr}^{-1} \\]
\\[ \\frac{1}{80.0} = 0.012500\\text{ yr}^{-1} \\]
\\[ \\frac{1}{45.0} = 0.022222\\text{ yr}^{-1} \\]
Sum of frequencies:
\\[ k_{\\text{tot}} = \\frac{1}{\\tau_{\\text{eff}}} = 0.041667 + 0.012500 + 0.022222 = 0.076389\\text{ yr}^{-1} \\]
Effective lifetime:
\\[ \\tau_{\\text{eff}} = \\frac{1}{0.076389\\text{ yr}^{-1}} \\approx 13.09\\text{ years} \\]

**(b) Remaining Atmospheric Burden at 10, 25, and 50 Years:**
Using $M(t) = M_0 \\exp(-k_{\\text{tot}} t)$ with $M_0 = 85.0\\text{ Gg}$:
1. At $t = 10\\text{ years}$:
   \\[ M(10) = 85.0 \\exp(-0.076389 \\times 10) = 85.0 \\exp(-0.76389) = 85.0 \\times 0.46585 = 39.60\\text{ Gg} \\]
2. At $t = 25\\text{ years}$:
   \\[ M(25) = 85.0 \\exp(-0.076389 \\times 25) = 85.0 \\exp(-1.9097) = 85.0 \\times 0.14812 = 12.59\\text{ Gg} \\]
3. At $t = 50\\text{ years}$:
   \\[ M(50) = 85.0 \\exp(-0.076389 \\times 50) = 85.0 \\exp(-3.8195) = 85.0 \\times 0.02194 = 1.865\\text{ Gg} \\]

**(c) Time to Reach $< 5\\%$ of Initial Burden:**
Set $\\frac{M(t)}{M_0} = 0.05$:
\\[ \\exp(-k_{\\text{tot}} t_{0.05}) = 0.05 \\implies -k_{\\text{tot}} t_{0.05} = \\ln(0.05) = -2.99573 \\]
\\[ t_{0.05} = \\frac{2.99573}{0.076389\\text{ yr}^{-1}} \\approx 39.22\\text{ years} \\]
*Conclusion*: It requires approximately $39\\text{ years}$ after total cessation of emissions for Halon-1211 to purge $95\\%$ of its burden from the atmosphere."""
        }
    ]

    return {
        "unit_number": 3,
        "title": "Stratospheric Ozone Dynamics, Halogen Photochemistry & The Montreal Protocol",
        "description": "Stratospheric photochemistry, Chapman oxygen-only steady-state cycle, catalytic ozone destruction cycles (HOx, NOx, ClOx, BrOx), industrial chemistry and the Rule of 90 for CFCs, HCFCs, and Halons, stratospheric photolysis and chlorine reservoir deactivation, heterogeneous surface catalysis on Polar Stratospheric Clouds, polar vortex dynamics and the ClO dimer cycle, Ozone Depletion Potential formulations, UV-B penetration and DNA pyrimidine photoproducts, and the Montreal Protocol and Kigali amendments.",
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u = get_unit_3()
    print(f"Unit 3 generated: {len(u['sections'])} sections, {len(u['problems'])} problems.")
