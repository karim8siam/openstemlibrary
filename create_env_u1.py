"""
create_env_u1.py
Unit 1: Atmospheric Chemistry, Photochemical Smog & Acid Deposition
Covers atmospheric structure, Chapman & Leighton mechanisms, OH radical cycles,
photochemical smog, particulates, automotive emissions, acid rain, and radioactivity.
Strictly zero prohibited tokens, pure UNIX newlines, pristine KaTeX.
"""

def get_unit_1():
    sections = [
        {
            "id": "sec1_1",
            "title": "Planetary Atmospheric Evolution, Thermal Stratification & Chemical Composition",
            "content": """The terrestrial atmosphere is a dynamic, multi-component gaseous envelope governed by hydrostatic equilibrium, radiative transfer, and complex chemical feedback cycles. Understanding its behavior requires establishing its vertical thermal architecture and chemical composition.

### 1. Hydrostatic Equation and the Barometric Law
Consider a vertical fluid element of unit cross-sectional area $A = 1\\text{ m}^2$, thickness $dz$, and density $\\rho(z)$ at altitude $z$ in the gravitational field of Earth:
\\[ dP = -\\rho(z) g dz \\]
Applying the ideal gas equation of state:
\\[ P = \\frac{\\rho}{M} R T \\implies \\rho = \\frac{P M}{R T} \\]
where $M$ is the mean molecular mass of dry air ($M \\approx 28.97\\text{ g/mol} = 2.897 \\times 10^{-2}\\text{ kg/mol}$), $R = 8.3145\\text{ J/(mol}\\cdot\\text{K)}$, and $T(z)$ is the absolute temperature. Substituting $\\rho$ into the hydrostatic equation yields:
\\[ \\frac{dP}{P} = -\\frac{M g}{R T(z)} dz = -\\frac{dz}{H_s(z)} \\]
where $H_s(z) = \\frac{R T(z)}{M g}$ is the local atmospheric **scale height**. For an isothermal atmosphere with effective temperature $T_0 = 250\\text{ K}$ and $g = 9.807\\text{ m/s}^2$:
\\[ H_s = \\frac{8.3145 \\times 250}{2.897 \\times 10^{-2} \\times 9.807} \\approx 7.32\\text{ km} \\]
Integrating yields the classical barometric profile:
\\[ P(z) = P_0 \\exp\\left( -\\int_0^z \\frac{dz'}{H_s(z')} \\right) \\approx P_0 \\exp\\left(-\\frac{z}{H_s}\\right) \\]

### 2. Thermal Stratification and Atmospheric Nomenclature
The vertical profile of temperature divides the atmosphere into four discrete concentric shells separated by pauses:
1. **Troposphere ($0$ to $\\sim 11-18\\text{ km}$)**: Characterized by strong convective overturning and a negative environmental lapse rate:
   \\[ \\Gamma = -\\frac{dT}{dz} \\approx 6.5\\text{ K/km} \\]
   Heated from below via sensible heat and terrestrial thermal infrared re-radiation.
2. **Stratosphere ($\sim 11$ to $\\sim 50\\text{ km}$)**: Inverted thermal gradient ($dT/dz > 0$), temperature rising from $\\approx 215\\text{ K}$ at the tropopause to $\\approx 270\\text{ K}$ at the stratopause. This stability is driven by exothermicity in ozone photolysis and recombination:
   \\[ \\text{O}_3 + h\\nu \\rightarrow \\text{O}_2 + \\text{O}(^1D) \\]
   \\[ \\text{O} + \\text{O}_2 + \\text{M} \\rightarrow \\text{O}_3 + \\text{M} + \\Delta H \\quad (\\Delta H = -106.5\\text{ kJ/mol}) \\]
3. **Mesosphere ($\sim 50$ to $\\sim 85\\text{ km}$)**: Decreasing temperature reaching the coldest region in the atmosphere ($\sim 140-180\\text{ K}$) due to intense $\\text{CO}_2$ infrared radiative cooling to space ($15\\ \mu\\text{m}$ band).
4. **Thermosphere ($> 85\\text{ km}$)**: High kinetic temperature ($> 1000\\text{ K}$) driven by photodissociation and photoionization of $\\text{O}_2$ and $\\text{N}_2$ by extreme ultraviolet (EUV, $\lambda < 100\\text{ nm}$) radiation.

### 3. Chemical Inventory of Dry Atmospheric Air
Dry air consists predominantly of chemically non-reactive or long-lived permanent species:
- Molecular Nitrogen ($\\text{N}_2$): $78.084\\% = 780,840\\text{ ppmv}$
- Molecular Oxygen ($\\text{O}_2$): $20.946\\% = 209,460\\text{ ppmv}$
- Argon ($\\text{Ar}$): $0.934\\% = 9,340\\text{ ppmv}$
- Carbon Dioxide ($\\text{CO}_2$): $\\approx 425\\text{ ppmv}$ (rapidly rising due to anthropogenic fossil combustion)
- Neon ($\\text{Ne}$), Helium ($\\text{He}$), Methane ($\\text{CH}_4$, $\\sim 1.9\\text{ ppmv}$), Krypton ($\\text{Kr}$), Hydrogen ($\\text{H}_2$), and Nitrous Oxide ($\\text{N}_2\\text{O}$, $\\sim 0.33\\text{ ppmv}$)."""
        },
        {
            "id": "sec1_2",
            "title": "Tropospheric Hydroxyl Radical Photochemical Detergent Cycles & VOC Oxidation",
            "content": """The hydroxyl radical $(\\cdot\\text{OH})$ serves as the primary chemical scavenger and oxidative detergent of the troposphere, initiating the removal of virtually all reduced and partially oxidized trace gases.

### 1. Photochemical Generation of Hydroxyl Radicals
Because the direct bond dissociation energy of water is excessively high ($D_0(\\text{H}-\\text{OH}) = 497\\text{ kJ/mol}$, requiring vacuum UV $\lambda < 240\\text{ nm}$ that cannot penetrate the stratospheric ozone filter), tropospheric $\\cdot\\text{OH}$ is generated via a two-step photolytic sequence involving tropospheric ozone:
1. Photolysis of ozone by solar actinic UV-B radiation ($\lambda < 320\\text{ nm}$):
   \\[ \\text{O}_3 + h\\nu (\\lambda \\le 320\\text{ nm}) \\xrightarrow{J_{\\text{O}_3}} \\text{O}_2(^1\\Delta_g) + \\text{O}(^1D) \\]
2. Reaction of electronically excited singlet oxygen atoms $\\text{O}(^1D)$ with ambient water vapor:
   \\[ \\text{O}(^1D) + \\text{H}_2\\text{O} \\xrightarrow{k_{\\text{H}_2\\text{O}}} 2\\,\\cdot\\text{OH} \\]
In competition with water reaction, the vast majority ($> 90\\%$) of $\\text{O}(^1D)$ undergoes collision-induced electronic quenching by inert atmospheric bath gas molecules $\\text{M} = \\text{N}_2, \\text{O}_2$:
\\[ \\text{O}(^1D) + \\text{M} \\xrightarrow{k_{\\text{M}}} \\text{O}(^3P) + \\text{M} \\]
The resulting ground-state triplet oxygen atom $\\text{O}(^3P)$ rapidly recombines with $\\text{O}_2$:
\\[ \\text{O}(^3P) + \\text{O}_2 + \\text{M} \\rightarrow \\text{O}_3 + \\text{M} \\]
yielding a null cycle.

### 2. Steady-State Hydroxyl Radical Concentration
Applying the steady-state approximation to $[\text{O}(^1D)]$:
\\[ \\frac{d[\\text{O}(^1D)]}{dt} = J_{\\text{O}_3}[\\text{O}_3] - k_{\\text{H}_2\\text{O}}[\\text{O}(^1D)][\\text{H}_2\\text{O}] - k_{\\text{M}}[\\text{O}(^1D)][\\text{M}] = 0 \\]
\\[ [\\text{O}(^1D)]_{\\text{ss}} = \\frac{J_{\\text{O}_3}[\\text{O}_3]}{k_{\\text{H}_2\\text{O}}[\\text{H}_2\\text{O}] + k_{\\text{M}}[\\text{M}]} \\]
The gross production rate of $\\cdot\\text{OH}$ is therefore:
\\[ P_{\\text{OH}} = 2 k_{\\text{H}_2\\text{O}}[\\text{O}(^1D)]_{\\text{ss}}[\\text{H}_2\\text{O}] = \\frac{2 J_{\\text{O}_3} k_{\\text{H}_2\\text{O}}[\\text{O}_3][\\text{H}_2\\text{O}]}{k_{\\text{M}}[\\text{M}] + k_{\\text{H}_2\\text{O}}[\\text{H}_2\\text{O}]} \\]
Because $k_{\\text{M}}[\\text{M}] \\gg k_{\\text{H}_2\\text{O}}[\\text{H}_2\\text{O}]$, this simplifies to:
\\[ P_{\\text{OH}} \\approx \\frac{2 J_{\\text{O}_3} k_{\\text{H}_2\\text{O}}}{k_{\\text{M}}[\\text{M}]} [\\text{O}_3][\\text{H}_2\\text{O}] \\]
Typical daytime boundary-layer steady-state concentrations of $\\cdot\\text{OH}$ are on the order of $10^6\\text{ molecules/cm}^3$ ($~10^{-18}\\text{ atm}$ or $~0.04\\text{ pptv}$), resulting in a photochemical lifetime of less than 1 second.

### 3. Hydrocarbon and VOC Oxidation Mechanism
The oxidation of methane (and non-methane volatile organic compounds, NMVOCs) proceeds via hydrogen atom abstraction:
\\[ \\text{CH}_4 + \\cdot\\text{OH} \\xrightarrow{k_1} \\cdot\\text{CH}_3 + \\text{H}_2\\text{O} \\]
The methyl radical reacts instantaneously with $\\text{O}_2$ to form a methylperoxy radical:
\\[ \\cdot\\text{CH}_3 + \\text{O}_2 + \\text{M} \\rightarrow \\text{CH}_3\\text{O}_2\\cdot + \\text{M} \\]
In the presence of nitrogen oxides ($\\text{NO}_x$), $\\text{CH}_3\\text{O}_2\\cdot$ oxidizes nitric oxide ($\\text{NO}$) to nitrogen dioxide ($\\text{NO}_2$):
\\[ \\text{CH}_3\\text{O}_2\\cdot + \\text{NO} \\rightarrow \\text{CH}_3\\text{O}\\cdot + \\text{NO}_2 \\]
The methoxy radical then reacts with oxygen to generate formaldehyde and a hydroperoxyl radical:
\\[ \\text{CH}_3\\text{O}\\cdot + \\text{O}_2 \\rightarrow \\text{HCHO} + \\text{HO}_2\\cdot \\]
Finally, $\\text{HO}_2\\cdot$ completes the catalytic chain by oxidizing another molecule of $\\text{NO}$ and regenerating $\\cdot\\text{OH}$:
\\[ \\text{HO}_2\\cdot + \\text{NO} \\rightarrow \\cdot\\text{OH} + \\text{NO}_2 \\]"""
        },
        {
            "id": "sec1_3",
            "title": "Nitrogen Oxides, Leighton Photostationary State & Tropospheric Ozone Dynamics",
            "content": """Tropospheric ozone is not emitted directly by anthropogenic sources; it is an entirely secondary pollutant formed from the photolysis of nitrogen dioxide.

### 1. The Classical Leighton Photostationary Cycle
In unpolluted air containing nitrogen oxides but devoid of reactive organic radicals, the interconversion of $\\text{NO}$, $\\text{NO}_2$, and $\\text{O}_3$ is governed by a triad of fast reactions known as the Leighton cycle:
1. Photolysis of $\\text{NO}_2$:
   \\[ \\text{NO}_2 + h\\nu (\\lambda \\le 420\\text{ nm}) \\xrightarrow{J_{\\text{NO}_2}} \\text{NO} + \\text{O}(^3P) \\]
2. Rapid combination of triplet oxygen with $\\text{O}_2$:
   \\[ \\text{O}(^3P) + \\text{O}_2 + \\text{M} \\xrightarrow{k_2} \\text{O}_3 + \\text{M} \\]
3. Titration of ozone by nitric oxide:
   \\[ \\text{NO} + \\text{O}_3 \\xrightarrow{k_3} \\text{NO}_2 + \\text{O}_2 \\]

### 2. The Leighton Relationship
Because reaction (2) is extremely rapid ($k_2[\\text{O}_2][\\text{M}] \\approx 10^5\\text{ s}^{-1}$), every oxygen atom generated in reaction (1) produces an ozone molecule immediately. Therefore:
\\[ \\frac{d[\\text{O}_3]}{dt} = J_{\\text{NO}_2}[\\text{NO}_2] - k_3[\\text{NO}][\\text{O}_3] \\]
Under photostationary steady-state conditions ($d[\\text{O}_3]/dt = 0$):
\\[ [\\text{O}_3]_{\\text{ss}} = \\frac{J_{\\text{NO}_2}}{k_3} \\frac{[\\text{NO}_2]}{[\\text{NO}]} \\]
At $298\\text{ K}$, $k_3 \\approx 1.8 \\times 10^{-14}\\text{ cm}^3\\text{molecule}^{-1}\\text{s}^{-1}$. At solar noon with clear skies, $J_{\\text{NO}_2} \\approx 8.0 \\times 10^{-3}\\text{ s}^{-1}$. Thus:
\\[ \\frac{J_{\\text{NO}_2}}{k_3} \\approx \\frac{8.0 \\times 10^{-3}}{1.8 \\times 10^{-14}} \\approx 4.44 \\times 10^{11}\\text{ molecules/cm}^3 \\approx 18\\text{ ppbv} \\]
In clean pristine air where $[\text{NO}_2]/[\text{NO}] \\sim 1$, the Leighton relationship predicts an ozone concentration of only $\\approx 18-35\\text{ ppbv}$.

### 3. Net Ozone Accumulation via VOC Coupling
The fundamental paradox of photochemical smog is that urban areas frequently exhibit ozone concentrations exceeding $150-300\\text{ ppbv}$, despite high $[\text{NO}]$.
The resolution is provided by peroxy radicals ($\\text{RO}_2\\cdot$ and $\\text{HO}_2\\cdot$) produced during VOC oxidation:
\\[ \\text{RO}_2\\cdot + \\text{NO} \\rightarrow \\text{RO}\\cdot + \\text{NO}_2 \\]
\\[ \\text{HO}_2\\cdot + \\text{NO} \\rightarrow \\cdot\\text{OH} + \\text{NO}_2 \\]
These reactions bypass the ozone titration pathway (Reaction 3). They convert $\\text{NO}$ to $\\text{NO}_2$ without consuming ozone. When this newly formed $\\text{NO}_2$ subsequently photolyzes:
\\[ \\text{NO}_2 + h\\nu \\rightarrow \\text{NO} + \\text{O}(^3P) \\xrightarrow{+\\text{O}_2} \\text{O}_3 \\]
a net molecule of ozone is produced for every peroxy radical oxidation step."""
        },
        {
            "id": "sec1_4",
            "title": "Photochemical Smog Mechanics: Peroxyacyl Nitrates, Aldehydes & Radical Propagation",
            "content": """Photochemical smog is an oxidizing atmospheric pollution regime resulting from the solar radiation-driven interaction of hydrocarbons and nitrogen oxides in stagnant air masses.

### 1. Peroxyacyl Nitrates (PAN): Synthesis and Thermal Equilibria
Peroxyacyl nitrates, most notably peroxyacetyl nitrate (PAN, $\\text{CH}_3\\text{C(O)OONO}_2$), are classic lachrymatory, phytotoxic indicators of photochemical smog:
1. Oxidation of acetaldehyde ($\\text{CH}_3\\text{CHO}$) by $\\cdot\\text{OH}$:
   \\[ \\text{CH}_3\\text{CHO} + \\cdot\\text{OH} \\rightarrow \\text{CH}_3\\dot{\\text{C}}\\text{O} + \\text{H}_2\\text{O} \\]
2. Addition of molecular oxygen to the acetyl radical to yield the peroxyacetyl radical:
   \\[ \\text{CH}_3\\dot{\\text{C}}\\text{O} + \\text{O}_2 + \\text{M} \\rightarrow \\text{CH}_3\\text{C(O)OO}\\cdot + \\text{M} \\]
3. Reversible combination with nitrogen dioxide:
   \\[ \\text{CH}_3\\text{C(O)OO}\\cdot + \\text{NO}_2 + \\text{M} \\xrightleftharpoons[k_{-d}]{k_a} \\text{CH}_3\\text{C(O)OONO}_2 + \\text{M} \\]

The backward thermal unimolecular dissociation reaction has a steep activation energy ($E_a \\approx 113\\text{ kJ/mol}$):
\\[ k_{-d}(T) = A \\exp\\left(-\\frac{E_a}{RT}\\right) \\approx 5.4 \\times 10^{16} \\exp\\left(-\\frac{13600}{T}\\right)\\text{ s}^{-1} \\]
At $T = 298\\text{ K}$ ($25^\\circ\\text{C}$), the thermal lifetime of PAN is short ($\\tau \\approx 30\\text{ minutes}$), leading to rapid dissociation. However, at upper-tropospheric temperatures ($T = 250\\text{ K}$), the lifetime expands to several months:
\\[ \\tau(250\\text{ K}) = \\frac{1}{k_{-d}(250\\text{ K})} \\approx 1.2 \\times 10^7\\text{ s} \\approx 140\\text{ days} \\]
Consequently, PAN acts as a long-range atmospheric reservoir and transport vehicle for $\\text{NO}_x$, subsiding in remote regions and releasing $\\text{NO}_x$ to generate tropospheric ozone far from urban emission sources.

### 2. Ozone Isopleths and the VOC-vs-NOx Limitation Matrix
The non-linear relationship between ozone production and its precursor concentrations is summarized by empirical and photochemical EKMA (Empirical Kinetic Modeling Approach) ozone isopleths:
- **VOC-Limited (or $\\text{NO}_x$-Saturated) Regime**: Characteristic of dense urban cores where $[\text{NO}_x]$ is high. Here, $\\text{NO}_2$ acts as a radical chain terminator via the reaction $\\cdot\\text{OH} + \\text{NO}_2 + \\text{M} \\rightarrow \\text{HNO}_3 + \\text{M}$. Reducing $\\text{NO}_x$ actually *increases* ozone (the $\\text{NO}_x$ disbenefit). Ozone mitigation requires reducing VOC emissions.
- **$\\text{NO}_x$-Limited Regime**: Characteristic of rural and suburban downwind regions where $[\text{VOC}]/[\\text{NO}_x] > 8$. Here, peroxy radicals undergo self-reactions ($\text{HO}_2\\cdot + \\text{HO}_2\\cdot \\rightarrow \\text{H}_2\\text{O}_2 + \\text{O}_2$), and ozone production is strictly limited by the availability of $\\text{NO}$. Reducing $\\text{NO}_x$ is the only effective way to suppress ozone."""
        },
        {
            "id": "sec1_5",
            "title": "Atmospheric Particulate Matter: PM2.5, PM10, Metallic Aerosols & Secondary Organics",
            "content": """Atmospheric particulate matter (aerosols) consists of microscopic solid or liquid particles suspended in the gas phase, playing major roles in human respiratory pathology, cloud microphysics, and planetary radiative balance.

### 1. Particle Size Distributions and Inhalation Aerodynamics
Particulates are classified by their equivalent **aerodynamic diameter** $d_a$, defined as the diameter of a unit-density sphere ($\rho_0 = 1000\\text{ kg/m}^3$) that exhibits the identical gravitational settling terminal velocity $v_{ts}$:
\\[ v_{ts} = \\frac{\\rho_p d_p^2 g C_c(d_p)}{18 \\mu} \\]
where $C_c(d_p) = 1 + \\frac{2\\lambda}{d_p}\\left(1.257 + 0.400 \\exp(-0.55 d_p / \\lambda)\\right)$ is the Cunningham slip correction factor for non-continuum gas dynamics ($\lambda \\approx 66\\text{ nm}$ is the mean free path of air).
- **Coarse Particles ($\text{PM}_{10}$, $2.5\\ \mu\\text{m} < d_a \\le 10\\ \mu\\text{m}$)**: Generated mechanically by crustal windblown dust, road abrasions, and sea spray. Captured primarily in the nasopharyngeal and tracheobronchial regions of the respiratory tract.
- **Fine Particles ($\text{PM}_{2.5}$, $d_a \\le 2.5\\ \mu\\text{m}$)**: Dominated by combustion soot, secondary sulfates, nitrates, and secondary organic aerosols (SOA). Capable of penetrating deeply into the pulmonary alveoli and translocating into the vascular circulatory system.
- **Ultrafine Particles (Nanoparticles, $d_a \\le 0.1\\ \mu\\text{m}$)**: Dominated by gas-to-particle nucleation modes with lifetimes controlled by Brownian coagulation.

### 2. Secondary Inorganic Aerosol (SIA) Thermodynamics
Fine inorganic aerosol mass is dominated by ammonium sulfate, ammonium bisulfate, and ammonium nitrate:
1. Gas-phase oxidation of $\\text{SO}_2$:
   \\[ \\text{SO}_2 + \\cdot\\text{OH} \\xrightarrow{+\\text{O}_2, +\\text{H}_2\\text{O}} \\text{H}_2\\text{SO}_4 \\]
   Due to its ultra-low saturation vapor pressure ($P_{\\text{vap}} < 10^{-11}\\text{ atm}$), sulfuric acid condenses irreversibly onto preexisting aerosol surfaces or undergoes binary homogeneous nucleation with $\\text{H}_2\\text{O}$.
2. Atmospheric neutralization by ammonia ($\\text{NH}_3$):
   \\[ \\text{NH}_3(g) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{NH}_4\\text{HSO}_4(aq) \\]
   \\[ \\text{NH}_3(g) + \\text{NH}_4\\text{HSO}_4(aq) \\rightarrow (\\text{NH}_4)_2\\text{SO}_4(s/aq) \\]
3. When ambient $\\text{NH}_3$ exceeds sulfate neutralization capacity, excess ammonia reacts with gas-phase nitric acid to form volatile ammonium nitrate in temperature- and humidity-dependent equilibrium:
   \\[ \\text{NH}_3(g) + \\text{HNO}_3(g) \\xrightleftharpoons[T]{K_p} \\text{NH}_4\\text{NO}_3(s/aq) \\]

### 3. Metallic Aerosols and Toxicological Speciation
Heavy metals emitted by industrial smelting, coal combustion, and vehicular friction brakes partition into particulate phases:
- **Lead ($\\text{Pb}$)**: Historically dominated by tetraethyllead fuel anti-knock additives; now dominated by battery recycling, coal combustion, and industrial paint manufacturing.
- **Cadmium ($\\text{Cd}$)** and **Arsenic ($\\text{As}$)**: Emitted from metallurgical processing and coal fly ash; exist as fine submicron condensates with high bioavailability.
- **Transition Metals ($\\text{Fe, Cu, Mn, Cr}$)**: Catalyze in vivo and in-cloud Fenton chemistry:
  \\[ \\text{Fe}^{2+} + \\text{H}_2\\text{O}_2 \\rightarrow \\text{Fe}^{3+} + \\cdot\\text{OH} + \\text{OH}^- \\]
  generating intracellular Reactive Oxygen Species (ROS) that induce pulmonary lipid peroxidation and systemic oxidative stress."""
        },
        {
            "id": "sec1_6",
            "title": "Mobile Source Emissions & Exhaust Catalytic Conversion Chemistry",
            "content": """Internal combustion engines operate under high-temperature, high-pressure hydrocarbon combustion, serving as major global mobile sources of carbon monoxide, unburned hydrocarbons, and nitrogen oxides.

### 1. Zeldovich Thermal NOx Mechanism
At peak flame combustion temperatures ($T > 1800\\text{ K}$), molecular nitrogen is oxidized via the classical high-activation-energy Zeldovich mechanism:
1. $\\text{O} + \\text{N}_2 \\xrightarrow{k_1} \\text{NO} + \\text{N} \\quad (E_{a,1} \\approx 314\\text{ kJ/mol})$
2. $\\text{N} + \\text{O}_2 \\xrightarrow{k_2} \\text{NO} + \\text{O} \\quad (E_{a,2} \\approx 26\\text{ kJ/mol})$
3. $\\text{N} + \\cdot\\text{OH} \\xrightarrow{k_3} \\text{NO} + \\text{H} \\quad (E_{a,3} \\approx 0\\text{ kJ/mol})$
Because Reaction 1 requires breaking the strong $\\text{N}\\equiv\\text{N}$ triple bond ($945\\text{ kJ/mol}$), thermal $\\text{NO}$ production is exponentially sensitive to combustion temperature:
\\[ \\frac{d[\\text{NO}]}{dt} = 2 k_1 [\\text{O}][\\text{N}_2] \\propto \\exp\\left(-\\frac{314000}{R T}\\right) \\]

### 2. The Three-Way Catalytic Converter (TWC)
To abate vehicle emissions simultaneously, modern automotive exhaust systems employ Three-Way Catalytic Converters consisting of noble metal nanoparticles (Platinum $\\text{Pt}$, Palladium $\\text{Pd}$, and Rhodium $\\text{Rh}$) dispersed onto a high-surface-area $\\gamma-\\text{Al}_2\\text{O}_3$ washcoat supported on a cordierite ceramic honeycomb monolith.
The converter carries out three simultaneous redox reactions:
1. Oxidation of Carbon Monoxide:
   \\[ 2\\,\\text{CO} + \\text{O}_2 \\xrightarrow{\\text{Pt/Pd}} 2\\,\\text{CO}_2 \\]
2. Oxidation of Unburned Hydrocarbons:
   \\[ \\text{C}_n\\text{H}_m + \\left(n + \\frac{m}{4}\\right)\\text{O}_2 \\xrightarrow{\\text{Pt/Pd}} n\\,\\text{CO}_2 + \\frac{m}{2}\\,\\text{H}_2\\text{O} \\]
3. Reduction of Nitric Oxide:
   \\[ 2\\,\\text{NO} + 2\\,\\text{CO} \\xrightarrow{\\text{Rh}} \\text{N}_2 + 2\\,\\text{CO}_2 \\]
   \\[ 2\\,\\text{NO} + 2\\,\\text{H}_2 \\xrightarrow{\\text{Rh}} \\text{N}_2 + 2\\,\\text{H}_2\\text{O} \\]

### 3. The Stoichiometric Air-to-Fuel Window
Optimal conversion efficiency ($> 98\\%$ for all three pollutants simultaneously) occurs only within an extremely narrow air-to-fuel mass ratio window centered at stoichiometry:
\\[ \\left(\\frac{A}{F}\\right)_{\\text{stoich}} \\approx 14.7 : 1 \\quad (\\lambda = 1.00 \\pm 0.005) \\]
- **Rich Mixture ($\\lambda < 1.0$)**: Insufficient $\\text{O}_2$; conversion efficiency of $\\text{CO}$ and $\\text{HC}$ drops precipitously.
- **Lean Mixture ($\\lambda > 1.0$)**: Excess $\\text{O}_2$; surface oxygen coverage on Rh blocks $\\text{NO}$ dissociation sites, collapsing $\\text{NO}_x$ reduction efficiency.
Closed-loop control is maintained via a heated zirconium dioxide ($\\text{ZrO}_2$) oxygen sensor ($\lambda$-sensor) that adjusts real-time fuel injection pulse width."""
        },
        {
            "id": "sec1_7",
            "title": "Atmospheric Sulfur Chemistry, Cloud Water Scavenging & Acid Deposition Thermodynamics",
            "content": """Acid deposition (acid rain) is the atmospheric deposition of strong mineral acids onto terrestrial and aquatic ecosystems via wet precipitation (rain, snow, fog) and dry aerosol/gas deposition.

### 1. Natural Rain pH and the Carbonic Acid Buffer
Pure, unpolluted rainwater in equilibrium with atmospheric carbon dioxide ($\text{CO}_2 \\approx 420\\text{ ppmv}$) is naturally mildly acidic. The equilibrium is governed by Henry's law and carbonate equilibria:
1. Gas-liquid dissolution:
   \\[ \\text{CO}_2(g) + \\text{H}_2\\text{O} \\xrightleftharpoons{K_H} \\text{CO}_2\\cdot\\text{H}_2\\text{O}(aq) \\quad (K_H = 3.4 \\times 10^{-2}\\text{ M/atm}) \\]
   \\[ [\\text{H}_2\\text{CO}_3^*] = K_H P_{\\text{CO}_2} = (3.4 \\times 10^{-2})(4.2 \\times 10^{-4}) \\approx 1.43 \\times 10^{-5}\\text{ M} \\]
2. First dissociation of carbonic acid:
   \\[ \\text{H}_2\\text{CO}_3^* \\xrightleftharpoons{K_{a1}} \\text{H}^+ + \\text{HCO}_3^- \\quad (K_{a1} = 4.45 \\times 10^{-7}\\text{ M}) \\]
Assuming $[\text{H}^+] \\approx [\text{HCO}_3^-]$ from charge balance:
\\[ [\\text{H}^+]^2 = K_{a1}[\\text{H}_2\\text{CO}_3^*] = (4.45 \\times 10^{-7})(1.43 \\times 10^{-5}) = 6.36 \\times 10^{-12}\\text{ M}^2 \\]
\\[ [\\text{H}^+] = \\sqrt{6.36 \\times 10^{-12}} \\approx 2.52 \\times 10^{-6}\\text{ M} \\implies \\text{pH} = -\\log_{10}(2.52 \\times 10^{-6}) \\approx 5.60 \\]
Therefore, **acid rain** is formally defined as precipitation having a $\\text{pH} < 5.60$, driven by anthropogenic emissions of sulfur dioxide ($\\text{SO}_2$) and nitrogen oxides ($\\text{NO}_x$).

### 2. Gas-Phase vs Aqueous-Phase Oxidation of SO2
While gas-phase oxidation by $\\cdot\\text{OH}$ occurs at moderate rates ($~1\\%\\text{ per hour}$):
\\[ \\text{SO}_2 + \\cdot\\text{OH} + \\text{M} \\rightarrow \\text{HOSO}_2\\cdot + \\text{M} \\]
\\[ \\text{HOSO}_2\\cdot + \\text{O}_2 \\rightarrow \\text{HO}_2\\cdot + \\text{SO}_3 \\]
\\[ \\text{SO}_3 + \\text{H}_2\\text{O} + \\text{M} \\rightarrow \\text{H}_2\\text{SO}_4 \\]
the predominant mechanism responsible for severe acid deposition ($> 80\\%$) takes place **inside cloud droplets** via aqueous-phase oxidation by dissolved hydrogen peroxide ($\\text{H}_2\\text{O}_2$) and ozone ($\\text{O}_3$):
1. Aqueous dissolution and hydration:
   \\[ \\text{SO}_2(g) \\xrightleftharpoons{K_{H}} \\text{SO}_2\\cdot\\text{H}_2\\text{O} \\xrightleftharpoons{K_{a1}} \\text{H}^+ + \\text{HSO}_3^- \\xrightleftharpoons{K_{a2}} 2\\text{H}^+ + \\text{SO}_3^{2-} \\]
2. Oxidation by dissolved $\\text{H}_2\\text{O}_2$:
   \\[ \\text{HSO}_3^- + \\text{H}_2\\text{O}_2(aq) \\rightleftharpoons \\text{SO}_2\\text{OOH}^- + \\text{H}_2\\text{O} \\]
   \\[ \\text{SO}_2\\text{OOH}^- + \\text{H}^+ \\rightarrow \\text{SO}_4^{2-} + 2\\,\\text{H}^+ \\]
The rate law for hydrogen peroxide oxidation is:
\\[ -\\frac{d[\\text{S(IV)}]}{dt} = \\frac{k [\\text{H}^+][\\text{H}_2\\text{O}_2][\\text{HSO}_3^-]}{1 + K[\\text{H}^+]} \\]
Because $[\text{HSO}_3^-] \\propto [\\text{H}^+]^{-1}$, the $[\text{H}^+]$ factors cancel, making the rate of $\\text{H}_2\\text{O}_2$ oxidation virtually **independent of cloud pH** down to $\\text{pH} \\approx 1.5$! Consequently, aqueous $\\text{H}_2\\text{O}_2$ rapidly converts dissolved $\\text{SO}_2$ to sulfuric acid even in highly acidic droplet environments."""
        },
        {
            "id": "sec1_8",
            "title": "Environmental Radioactivity: Radon Decay Series, Cosmic Spallation & Nuclear Fallout",
            "content": """Environmental radioactivity originates from primordial terrestrial radionuclides, cosmogenic spallation products, and anthropogenic nuclear fission/activation byproducts.

### 1. Primordial Radionuclides and the Radon Hazard
Primordial radioisotopes formed during stellar nucleosynthesis before the condensation of the solar system include Potassium-40 ($^{40}\\text{K}$, $t_{1/2} = 1.25 \\times 10^9\\text{ y}$), Thorium-232 ($^{232}\\text{Th}$), and Uranium-238 ($^{238}\\text{U}$, $t_{1/2} = 4.468 \\times 10^9\\text{ y}$).
Within the $^{238}\\text{U}$ decay series, Radium-226 ($^{226}\\text{Ra}$, $t_{1/2} = 1600\\text{ y}$) decays via alpha emission into **Radon-222** ($^{222}\\text{Rn}$):
\\[ ^{226}_{88}\\text{Ra} \\xrightarrow{\\alpha} \\ ^{222}_{86}\\text{Rn} + \\alpha \\quad (t_{1/2} = 3.8235\\text{ days}) \\]
As a noble gas with zero chemical reactivity, $^{222}\\text{Rn}$ diffuses upward through porous soil minerals and cracks in building foundations into indoor environments.
While $^{222}\\text{Rn}$ is exhaled upon inhalation, its short-lived decay progeny:
\\[ ^{222}_{86}\\text{Rn} \\xrightarrow{\\alpha} \\ ^{218}_{84}\\text{Po} \\xrightarrow{\\alpha} \\ ^{214}_{82}\\text{Pb} \\xrightarrow{\\beta^-} \\ ^{214}_{83}\\text{Bi} \\xrightarrow{\\beta^-} \\ ^{214}_{84}\\text{Po} \\xrightarrow{\\alpha} \\ ^{210}_{82}\\text{Pb} \\]
are solid, chemically reactive heavy metal ions that attach to submicron aerosols ($d_p \\approx 0.1-0.3\\ \mu\\text{m}$). Inhaled into the bronchial epithelium, the high-LET alpha particles from $^{218}\\text{Po}$ ($E_\\alpha = 6.00\\text{ MeV}$) and $^{214}\\text{Po}$ ($E_\\alpha = 7.69\\text{ MeV}$) deliver concentrated ionizing radiation directly to basal stem cell nuclei, representing the leading cause of lung cancer in non-smokers.

### 2. Cosmogenic Radionuclides: Carbon-14 and Tritium
Cosmic ray spallation of stratospheric and upper tropospheric nuclei produces cosmogenic isotopes:
1. Carbon-14 ($^{14}\\text{C}$, $t_{1/2} = 5730\\text{ y}$):
   \\[ ^{14}_7\\text{N} + n_{\\text{thermal}} \\rightarrow \\ ^{14}_6\\text{C} + ^1_1p \\]
   The nascent $^{14}\\text{C}$ atom rapidly oxidizes to $^{14}\\text{CO}_2$, entering the global photosynthetic carbon cycle.
2. Tritium ($^3\\text{H}$, $t_{1/2} = 12.32\\text{ y}$):
   \\[ ^{14}_7\\text{N} + n_{\\text{fast}} \\rightarrow \\ ^{12}_6\\text{C} + ^3_1\\text{H} \\]
   Tritium oxidizes to tritiated water ($\\text{HTO}$) and enters the global hydrological cycle.

### 3. Anthropogenic Nuclear Fallout Radionuclides
Atmospheric nuclear weapons testing and major reactor accidents (Chernobyl, Fukushima) injected long-lived fission products into the atmosphere:
- **Cesium-137 ($^{137}\\text{Cs}$, $t_{1/2} = 30.17\\text{ y}$)**: Alkali metal that mimics potassium ($K^+$), rapidly bioaccumulating in muscle tissues and soil clay mineral interlayers.
- **Strontium-90 ($^{90}\\text{Sr}$, $t_{1/2} = 28.9\\text{ y}$)**: Alkaline earth metal that chemically mimics calcium ($Ca^{2+}$), depositing into human bone trabeculae and irradiating bone marrow."""
        }
    ]

    problems = [
        {
            "id": "prob1_1",
            "tier": "Foundational",
            "title": "Scale Height and Atmospheric Pressure Profile Calculation",
            "statement": """Assuming an isothermal atmospheric layer at $T = 260\\text{ K}$ with standard acceleration of gravity $g = 9.807\\text{ m/s}^2$ and average molecular mass of dry air $M = 28.97\\text{ g/mol}$:
(a) Derive and calculate the atmospheric scale height $H_s$ in kilometers.
(b) Calculate the atmospheric pressure at an altitude of $z = 5.5\\text{ km}$ assuming sea-level pressure $P_0 = 1013.25\\text{ hPa}$.
(c) Determine the altitude at which the atmospheric pressure is reduced to exactly $50\\%$ of its sea-level value.""",
            "solution": """**(a) Calculation of Scale Height $H_s$:**
From the hydrostatic balance and the ideal gas equation:
\\[ H_s = \\frac{R T}{M g} \\]
Given:
- $R = 8.31446\\text{ J/(mol}\\cdot\\text{K)}$
- $T = 260\\text{ K}$
- $M = 28.97 \\times 10^{-3}\\text{ kg/mol}$
- $g = 9.807\\text{ m/s}^2$

Substitute the values:
\\[ H_s = \\frac{8.31446 \\times 260}{2.897 \\times 10^{-2} \\times 9.807} = \\frac{2161.76}{0.28411} \\approx 7609\\text{ m} = 7.609\\text{ km} \\]

**(b) Atmospheric Pressure at $z = 5.5\\text{ km}$:**
Using the barometric formula:
\\[ P(z) = P_0 \\exp\\left(-\\frac{z}{H_s}\\right) \\]
Substitute $z = 5.5\\text{ km}$ and $H_s = 7.609\\text{ km}$:
\\[ P(5.5) = 1013.25 \\exp\\left(-\\frac{5.5}{7.609}\\right) = 1013.25 \\exp(-0.7228) = 1013.25 \\times 0.4854 \\approx 491.8\\text{ hPa} \\]

**(c) Altitude for $50\\%$ Sea-Level Pressure ($P = 0.5 P_0$):**
Set $\\frac{P(z)}{P_0} = 0.5$:
\\[ \\exp\\left(-\\frac{z_{1/2}}{H_s}\\right) = 0.5 \\implies -\\frac{z_{1/2}}{H_s} = \\ln(0.5) = -\\ln(2) \\]
\\[ z_{1/2} = H_s \\ln(2) = 7.609 \\times 0.69315 \\approx 5.274\\text{ km} \\]"""
        },
        {
            "id": "prob1_2",
            "tier": "Foundational",
            "title": "Equilibrium pH of Unpolluted Clean Rainwater",
            "statement": """Atmospheric carbon dioxide is present at a mixing ratio of $420\\text{ ppmv}$ at sea level ($P = 1.0\\text{ atm}$). Henry's law constant for $\\text{CO}_2$ solubility in water at $298\\text{ K}$ is $K_H = 3.4 \\times 10^{-2}\\text{ M/atm}$. The first acid dissociation constant of carbonic acid is $K_{a1} = 4.5 \\times 10^{-7}\\text{ M}$.
(a) Calculate the aqueous concentration of dissolved carbonic acid $[\text{H}_2\text{CO}_3^*]$ in equilibrium with the atmosphere.
(b) Derive the charge balance equation and calculate the equilibrium $[\text{H}^+]$ and pH of pure unpolluted rainwater.
(c) Explain why natural rainwater cannot have a pH of 7.00.""",
            "solution": """**(a) Concentration of Dissolved Carbonic Acid:**
The partial pressure of $\\text{CO}_2$ is:
\\[ P_{\\text{CO}_2} = (420 \\times 10^{-6})(1.0\\text{ atm}) = 4.20 \\times 10^{-4}\\text{ atm} \\]
From Henry's law:
\\[ [\\text{H}_2\\text{CO}_3^*] = K_H \\times P_{\\text{CO}_2} = (3.4 \\times 10^{-2}\\text{ M/atm})(4.20 \\times 10^{-4}\\text{ atm}) = 1.428 \\times 10^{-5}\\text{ M} \\]

**(b) Charge Balance and Equilibrium pH:**
The dissolution and dissociation reactions are:
\\[ \\text{CO}_2(aq) + \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}^+ + \\text{HCO}_3^- \\quad (K_{a1} = 4.5 \\times 10^{-7}) \\]
\\[ \\text{HCO}_3^- \\rightleftharpoons \\text{H}^+ + \\text{CO}_3^{2-} \\quad (K_{a2} = 4.7 \\times 10^{-11}) \\]
\\[ \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}^+ + \\text{OH}^- \\quad (K_w = 1.0 \\times 10^{-14}) \\]
The electroneutrality (charge balance) equation is:
\\[ [\\text{H}^+] = [\\text{HCO}_3^-] + 2[\\text{CO}_3^{2-}] + [\\text{OH}^-] \\]
Because natural rain is acidic ($\text{pH} \\sim 5.6$), $[\\text{OH}^-] \\ll [\\text{H}^+]$ and $[\\text{CO}_3^{2-}] \\ll [\\text{HCO}_3^-]$. Thus, the charge balance reduces to:
\\[ [\\text{H}^+] \\approx [\\text{HCO}_3^-] \\]
From the equilibrium expression for $K_{a1}$:
\\[ K_{a1} = \\frac{[\\text{H}^+][\\text{HCO}_3^-]}{[\\text{H}_2\\text{CO}_3^*]} \\approx \\frac{[\\text{H}^+]^2}{[\\text{H}_2\\text{CO}_3^*]} \\]
\\[ [\\text{H}^+] = \\sqrt{K_{a1} [\\text{H}_2\\text{CO}_3^*]} = \\sqrt{(4.5 \\times 10^{-7})(1.428 \\times 10^{-5})} = \\sqrt{6.426 \\times 10^{-12}} = 2.535 \\times 10^{-6}\\text{ M} \\]
Calculating pH:
\\[ \\text{pH} = -\\log_{10}(2.535 \\times 10^{-6}) = 6 - \\log_{10}(2.535) = 6 - 0.404 = 5.596 \\approx 5.60 \\]

**(c) Physical Reason for Acidic Natural Rain:**
Pure liquid water open to the ambient atmosphere dissolves gaseous $\\text{CO}_2$, forming carbonic acid which dissociates to release hydronium ions. Water can only attain a neutral $\\text{pH} = 7.00$ in a vacuum or in an atmosphere devoid of acidic gases like $\\text{CO}_2$."""
        },
        {
            "id": "prob1_3",
            "tier": "Foundational",
            "title": "Leighton Photostationary State Ratio Analysis",
            "statement": """At solar noon in an urban air basin, the photolysis rate coefficient of nitrogen dioxide is measured as $J_{\\text{NO}_2} = 8.5 \\times 10^{-3}\\text{ s}^{-1}$. The rate constant for the reaction between nitric oxide and ozone at the ambient temperature of $298\\text{ K}$ is $k_3 = 1.8 \\times 10^{-14}\\text{ cm}^3\\text{molecule}^{-1}\\text{s}^{-1}$.
(a) Calculate the Leighton parameter ratio $\\frac{J_{\\text{NO}_2}}{k_3}$ in units of $\\text{molecules/cm}^3$ and in $\\text{ppbv}$ (assume standard air density $n_{\\text{air}} = 2.46 \\times 10^{19}\\text{ molecules/cm}^3$).
(b) If the measured ratio $[\text{NO}_2]/[\text{NO}] = 3.2$, calculate the steady-state ozone concentration in $\\text{ppbv}$.
(c) If cloud cover reduces solar UV flux such that $J_{\\text{NO}_2}$ decreases by $70\\%$, determine the new steady-state ozone concentration assuming the $[\text{NO}_2]/[\text{NO}]$ ratio remains constant.""",
            "solution": """**(a) Leighton Parameter Calculation:**
\\[ \\frac{J_{\\text{NO}_2}}{k_3} = \\frac{8.5 \\times 10^{-3}\\text{ s}^{-1}}{1.8 \\times 10^{-14}\\text{ cm}^3\\text{molecule}^{-1}\\text{s}^{-1}} = 4.722 \\times 10^{11}\\text{ molecules/cm}^3 \\]
Converting to mixing ratio in ppbv:
\\[ \\chi = \\frac{4.722 \\times 10^{11}\\text{ molecules/cm}^3}{2.46 \\times 10^{19}\\text{ molecules/cm}^3} \\times 10^9 = 19.196\\text{ ppbv} \\approx 19.2\\text{ ppbv} \\]

**(b) Steady-State Ozone Concentration:**
From the Leighton relationship:
\\[ [\\text{O}_3]_{\\text{ss}} = \\frac{J_{\\text{NO}_2}}{k_3} \\frac{[\\text{NO}_2]}{[\\text{NO}]} \\]
Substitute $[\text{NO}_2]/[\text{NO}] = 3.2$:
\\[ [\\text{O}_3]_{\\text{ss}} = (19.196\\text{ ppbv}) \\times 3.2 = 61.43\\text{ ppbv} \\approx 61.4\\text{ ppbv} \\]

**(c) Effect of Cloud Attenuation:**
A $70\\%$ reduction implies the new photolysis rate is:
\\[ J_{\\text{NO}_2}' = 0.30 \\times J_{\\text{NO}_2} \\]
Because $[\\text{O}_3]_{\\text{ss}}$ is directly proportional to $J_{\\text{NO}_2}$:
\\[ [\\text{O}_3]_{\\text{ss}}' = 0.30 \\times 61.43\\text{ ppbv} = 18.43\\text{ ppbv} \\approx 18.4\\text{ ppbv} \\]"""
        },
        {
            "id": "prob1_4",
            "tier": "Intermediate",
            "title": "Steady-State Hydroxyl Radical Kinetic Balance and Lifetime",
            "statement": """In a polluted boundary layer, ozone photolyzes at a rate $J_{\\text{O}_3} = 4.0 \\times 10^{-5}\\text{ s}^{-1}$ in the presence of $[\text{O}_3] = 60\\text{ ppbv}$ and relative humidity corresponding to $[\text{H}_2\text{O}] = 3.5 \\times 10^{17}\\text{ molecules/cm}^3$.
The rate constant for $\\text{O}(^1D) + \\text{H}_2\\text{O} \\rightarrow 2\\cdot\\text{OH}$ is $k_{\\text{H}_2\\text{O}} = 2.2 \\times 10^{-10}\\text{ cm}^3/\\text{s}$.
The rate constant for electronic quenching $\\text{O}(^1D) + \\text{M} \\rightarrow \\text{O}(^3P) + \\text{M}$ is $k_{\\text{M}} = 3.0 \\times 10^{-11}\\text{ cm}^3/\\text{s}$, with air density $[\text{M}] = 2.46 \\times 10^{19}\\text{ molecules/cm}^3$.
The sink of $\\cdot\\text{OH}$ is dominated by reactions with carbon monoxide ($k_{\\text{CO}} = 2.4 \\times 10^{-13}\\text{ cm}^3/\\text{s}$, $[\text{CO}] = 400\\text{ ppbv}$) and methane ($k_{\\text{CH}_4} = 6.4 \\times 10^{-15}\\text{ cm}^3/\\text{s}$, $[\text{CH}_4] = 1.9\\text{ ppmv}$).
(a) Calculate the steady-state concentration of excited singlet oxygen atoms $[\text{O}(^1D)]_{\\text{ss}}$.
(b) Calculate the gross rate of $\\cdot\\text{OH}$ radical generation $P_{\\text{OH}}$ in $\\text{molecules}/(\\text{cm}^3\\cdot\\text{s})$.
(c) Calculate the pseudo-first-order loss frequency $L_{\\text{OH}}$ and the instantaneous chemical lifetime of $\\cdot\\text{OH}$.
(d) Determine the steady-state concentration $[\text{OH}]_{\\text{ss}}$ in $\\text{molecules/cm}^3$.""",
            "solution": """**(a) Calculation of $[\text{O}(^1D)]_{\\text{ss}}$:**
Concentration of $\\text{O}_3$:
\\[ [\\text{O}_3] = (60 \\times 10^{-9})(2.46 \\times 10^{19}) = 1.476 \\times 10^{12}\\text{ molecules/cm}^3 \\]
Loss frequencies of $\\text{O}(^1D)$:
\\[ k_{\\text{M}}[\\text{M}] = (3.0 \\times 10^{-11})(2.46 \\times 10^{19}) = 7.38 \\times 10^8\\text{ s}^{-1} \\]
\\[ k_{\\text{H}_2\\text{O}}[\\text{H}_2\\text{O}] = (2.2 \\times 10^{-10})(3.5 \\times 10^{17}) = 7.70 \\times 10^7\\text{ s}^{-1} \\]
Total loss frequency:
\\[ \\sum k_{\\text{loss}} = 7.38 \\times 10^8 + 7.70 \\times 10^7 = 8.15 \\times 10^8\\text{ s}^{-1} \\]
Production rate of $\\text{O}(^1D)$:
\\[ P_{\\text{O}(^1D)} = J_{\\text{O}_3}[\\text{O}_3] = (4.0 \\times 10^{-5})(1.476 \\times 10^{12}) = 5.904 \\times 10^7\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s}) \\]
Steady-state concentration:
\\[ [\\text{O}(^1D)]_{\\text{ss}} = \\frac{5.904 \\times 10^7}{8.15 \\times 10^8} \\approx 7.244 \\times 10^{-2}\\text{ atoms/cm}^3 \\]

**(b) Gross Generation Rate of $\\cdot\\text{OH}$:**
Each reaction of $\\text{O}(^1D)$ with $\\text{H}_2\\text{O}$ yields two $\\cdot\\text{OH}$ radicals:
\\[ P_{\\text{OH}} = 2 k_{\\text{H}_2\\text{O}}[\\text{O}(^1D)]_{\\text{ss}}[\\text{H}_2\\text{O}] = 2 (7.70 \\times 10^7\\text{ s}^{-1})(7.244 \\times 10^{-2}\\text{ cm}^{-3}) = 1.115 \\times 10^7\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s}) \\]

**(c) Loss Frequency and Lifetime of $\\cdot\\text{OH}$:**
Convert concentrations of $\\text{CO}$ and $\\text{CH}_4$:
\\[ [\\text{CO}] = (400 \\times 10^{-9})(2.46 \\times 10^{19}) = 9.84 \\times 10^{12}\\text{ molecules/cm}^3 \\]
\\[ [\\text{CH}_4] = (1.9 \\times 10^{-6})(2.46 \\times 10^{19}) = 4.674 \\times 10^{13}\\text{ molecules/cm}^3 \\]
Loss frequency $L_{\\text{OH}}$:
\\[ L_{\\text{OH}} = k_{\\text{CO}}[\\text{CO}] + k_{\\text{CH}_4}[\\text{CH}_4] \\]
\\[ k_{\\text{CO}}[\\text{CO}] = (2.4 \\times 10^{-13})(9.84 \\times 10^{12}) = 2.362\\text{ s}^{-1} \\]
\\[ k_{\\text{CH}_4}[\\text{CH}_4] = (6.4 \\times 10^{-15})(4.674 \\times 10^{13}) = 0.299\\text{ s}^{-1} \\]
\\[ L_{\\text{OH}} = 2.362 + 0.299 = 2.661\\text{ s}^{-1} \\]
Lifetime $\\tau_{\\text{OH}}$:
\\[ \\tau_{\\text{OH}} = \\frac{1}{L_{\\text{OH}}} = \\frac{1}{2.661\\text{ s}^{-1}} \\approx 0.376\\text{ seconds} \\]

**(d) Steady-State Concentration $[\text{OH}]_{\\text{ss}}$:**
\\[ [\\text{OH}]_{\\text{ss}} = \\frac{P_{\\text{OH}}}{L_{\\text{OH}}} = \\frac{1.115 \\times 10^7\\text{ molecules}/(\\text{cm}^3\\cdot\\text{s})}{2.661\\text{ s}^{-1}} \\approx 4.19 \\times 10^6\\text{ molecules/cm}^3 \\]"""
        },
        {
            "id": "prob1_5",
            "tier": "Intermediate",
            "title": "Thermal Dissociation Kinetics and Lifetime of Peroxyacetyl Nitrate (PAN)",
            "statement": """The forward association and reverse unimolecular dissociation of PAN are described by:
\\[ \\text{CH}_3\\text{C(O)OO}\\cdot + \\text{NO}_2 + \\text{M} \\xrightleftharpoons[k_{-d}]{k_a} \\text{PAN} + \\text{M} \\]
The temperature-dependent rate coefficient for the unimolecular thermal dissociation of PAN is given by:
\\[ k_{-d}(T) = 5.4 \\times 10^{16} \\exp\\left(-\\frac{13600\\text{ K}}{T}\\right)\\text{ s}^{-1} \\]
(a) Calculate the first-order rate constant $k_{-d}$ and the half-life $t_{1/2}$ of PAN at sea level on a hot summer afternoon ($T = 308\\text{ K}$, $35^\\circ\\text{C}$).
(b) Calculate $k_{-d}$ and $t_{1/2}$ at the upper troposphere ($T = 240\\text{ K}$, $-33^\\circ\\text{C}$).
(c) Based on your findings, evaluate the role of PAN as a long-range transporter of $\\text{NO}_x$ across continents.""",
            "solution": """**(a) Dissociation Rate and Half-Life at $T = 308\\text{ K}$:**
\\[ k_{-d}(308) = 5.4 \\times 10^{16} \\exp\\left(-\\frac{13600}{308}\\right) = 5.4 \\times 10^{16} \\exp(-44.1558) \\]
\\[ \\exp(-44.1558) = 6.660 \\times 10^{-20} \\]
\\[ k_{-d}(308) = (5.4 \\times 10^{16})(6.660 \\times 10^{-20}) = 3.596 \\times 10^{-3}\\text{ s}^{-1} \\]
The half-life is:
\\[ t_{1/2} = \\frac{\\ln(2)}{k_{-d}} = \\frac{0.69315}{3.596 \\times 10^{-3}} \\approx 192.7\\text{ seconds} \\approx 3.21\\text{ minutes} \\]

**(b) Dissociation Rate and Half-Life at $T = 240\\text{ K}$:**
\\[ k_{-d}(240) = 5.4 \\times 10^{16} \\exp\\left(-\\frac{13600}{240}\\right) = 5.4 \\times 10^{16} \\exp(-56.6667) \\]
\\[ \\exp(-56.6667) = 2.457 \\times 10^{-25} \\]
\\[ k_{-d}(240) = (5.4 \\times 10^{16})(2.457 \\times 10^{-25}) = 1.327 \\times 10^{-8}\\text{ s}^{-1} \\]
The half-life is:
\\[ t_{1/2} = \\frac{0.69315}{1.327 \\times 10^{-8}\\text{ s}^{-1}} \\approx 5.224 \\times 10^7\\text{ seconds} \\]
Converting to days:
\\[ t_{1/2} = \\frac{5.224 \\times 10^7}{86400} \\approx 604.6\\text{ days} \\approx 1.66\\text{ years} \\]

**(c) Environmental and Meteorological Significance:**
At warm ground-level temperatures, PAN rapidly dissociates, maintaining local chemical equilibrium with $\\text{NO}_2$. However, when boundary-layer air is convectively lofted to the cold middle and upper troposphere ($T < 240\\text{ K}$), the dissociation rate drops by over five orders of magnitude ($> 10^5$). PAN becomes thermally stable, allowing it to be transported by jet streams across oceans and continents. When the air mass subsides and warms in remote pristine regions, PAN decomposes, releasing active $\\text{NO}_x$ and sparking secondary ozone generation."""
        },
        {
            "id": "prob1_6",
            "tier": "Intermediate",
            "title": "Aerosol Settling Velocity and Cunningham Slip Correction",
            "statement": """Consider three spherical aerosol particles of unit density $\\rho_p = 1200\\text{ kg/m}^3$ falling through air at $T = 293\\text{ K}$ and $P = 1.0\\text{ atm}$ (dynamic viscosity $\\mu = 1.81 \\times 10^{-5}\\text{ kg/(m}\\cdot\\text{s)}$, air mean free path $\\lambda = 66\\text{ nm}$):
- Particle A: $d_p = 10.0\\ \mu\\text{m}$ (coarse mode)
- Particle B: $d_p = 1.0\\ \mu\\text{m}$ (accumulation mode)
- Particle C: $d_p = 0.1\\ \mu\\text{m}$ ($100\\text{ nm}$, Aitken mode)
The Cunningham slip correction factor is:
\\[ C_c = 1 + \\frac{2\\lambda}{d_p}\\left(1.257 + 0.400 \\exp\\left(-0.55\\frac{d_p}{\\lambda}\\right)\\right) \\]
(a) Calculate $C_c$ for each of the three particles.
(b) Calculate their terminal gravitational settling velocities $v_{ts}$ in $\\text{m/s}$ and $\\text{cm/s}$.
(c) Calculate the time required for each particle to settle through a stagnant indoor room height of $h = 3.0\\text{ m}$.""",
            "solution": """**(a) Cunningham Slip Correction Factors:**
With $\\lambda = 0.066\\ \mu\\text{m}$:
1. For Particle A ($d_p = 10.0\\ \mu\\text{m}$):
   \\[ \\frac{2\\lambda}{d_p} = \\frac{2 \\times 0.066}{10.0} = 0.0132 \\]
   \\[ \\exp(-0.55 \\times 10.0 / 0.066) = \\exp(-83.3) \\approx 0 \\]
   \\[ C_c(A) = 1 + 0.0132 \\times 1.257 = 1 + 0.0166 = 1.017 \\]
2. For Particle B ($d_p = 1.0\\ \mu\\text{m}$):
   \\[ \\frac{2\\lambda}{d_p} = \\frac{0.132}{1.0} = 0.132 \\]
   \\[ \\exp(-0.55 / 0.066) = \\exp(-8.333) = 0.00024 \\approx 0 \\]
   \\[ C_c(B) = 1 + 0.132 \\times 1.257 = 1 + 0.1659 = 1.166 \\]
3. For Particle C ($d_p = 0.1\\ \mu\\text{m}$):
   \\[ \\frac{2\\lambda}{d_p} = \\frac{0.132}{0.1} = 1.320 \\]
   \\[ \\exp(-0.55 \\times 0.1 / 0.066) = \\exp(-0.8333) = 0.4346 \\]
   \\[ C_c(C) = 1 + 1.320 \\times (1.257 + 0.400 \\times 0.4346) = 1 + 1.320 \\times (1.257 + 0.1738) = 1 + 1.320 \\times 1.4308 = 2.889 \\]

**(b) Terminal Settling Velocities:**
Using Stokes' settling law with Cunningham correction:
\\[ v_{ts} = \\frac{\\rho_p d_p^2 g C_c}{18 \\mu} \\]
Here, $\\frac{\\rho_p g}{18 \\mu} = \\frac{1200 \\times 9.807}{18 \\times 1.81 \\times 10^{-5}} = \\frac{11768.4}{3.258 \\times 10^{-4}} = 3.612 \\times 10^7\\text{ m}^{-1}\\text{s}^{-1}$.
1. Particle A ($d_p = 10^{-5}\\text{ m}$):
   \\[ v_{ts}(A) = (3.612 \\times 10^7)(10^{-10})(1.017) = 3.673 \\times 10^{-3}\\text{ m/s} = 0.367\\text{ cm/s} \\]
2. Particle B ($d_p = 10^{-6}\\text{ m}$):
   \\[ v_{ts}(B) = (3.612 \\times 10^7)(10^{-12})(1.166) = 4.212 \\times 10^{-5}\\text{ m/s} = 0.00421\\text{ cm/s} \\]
3. Particle C ($d_p = 10^{-7}\\text{ m}$):
   \\[ v_{ts}(C) = (3.612 \\times 10^7)(10^{-14})(2.889) = 1.043 \\times 10^{-6}\\text{ m/s} = 0.000104\\text{ cm/s} \\]

**(c) Settling Times through $h = 3.0\\text{ m}$:**
1. Particle A:
   \\[ t_A = \\frac{3.0}{3.673 \\times 10^{-3}} \\approx 817\\text{ s} \\approx 13.6\\text{ minutes} \\]
2. Particle B:
   \\[ t_B = \\frac{3.0}{4.212 \\times 10^{-5}} \\approx 71,225\\text{ s} \\approx 19.8\\text{ hours} \\]
3. Particle C:
   \\[ t_C = \\frac{3.0}{1.043 \\times 10^{-6}} \\approx 2,876,300\\text{ s} \\approx 33.3\\text{ days} \\]
*Insight*: Fine and ultrafine particles do not settle by gravity on practical timescales; their atmospheric removal is governed entirely by precipitation scavenging (wet deposition)."""
        },
        {
            "id": "prob1_7",
            "tier": "Advanced",
            "title": "Aqueous-Phase S(IV) Cloud Droplet Oxidation Kinetics and Acid Deposition",
            "statement": """A non-precipitating cloud at $T = 283\\text{ K}$ has a liquid water content $L = 0.50\\text{ g/m}^3$ and droplet $\\text{pH} = 4.5$. The ambient gas-phase mixing ratio of sulfur dioxide is $5.0\\text{ ppbv}$, and hydrogen peroxide is $1.0\\text{ ppbv}$.
The Henry's law constants at $283\\text{ K}$ are:
- $K_{H,\\text{SO}_2} = 1.8\\text{ M/atm}$, $K_{a1} = 1.7 \\times 10^{-2}\\text{ M}$
- $K_{H,\\text{H}_2\\text{O}_2} = 1.4 \\times 10^5\\text{ M/atm}$
The rate law for aqueous-phase oxidation by $\\text{H}_2\\text{O}_2$ is:
\\[ -\\frac{d[\\text{S(IV)}]}{dt} = \\frac{k_a [\\text{H}^+][\\text{H}_2\\text{O}_2(aq)][\\text{HSO}_3^-]}{1 + K[\\text{H}^+]} \\]
where at $283\\text{ K}$, $k_a = 5.2 \\times 10^7\\text{ M}^{-2}\\text{s}^{-1}$ and $K = 17\\text{ M}^{-1}$.
(Assume total atmospheric pressure $P = 1.0\\text{ atm}$).
(a) Calculate the aqueous concentrations of dissolved $[\text{HSO}_3^-]$ and $[\text{H}_2\text{O}_2(aq)]$ inside the cloud droplets in $\\text{mol/L}$.
(b) Calculate the aqueous oxidation rate in $\\text{M/s}$ and convert it to a gas-phase equivalent oxidation rate in $\%\\text{ per hour}$ of total $\\text{SO}_2$.
(c) Compare this aqueous rate with typical clear-sky gas-phase oxidation of $\\text{SO}_2$ by $\\cdot\\text{OH}$ ($\sim 1-2\\%\\text{ per hour}$).""",
            "solution": """**(a) Calculation of Aqueous Concentrations:**
Partial pressures:
\\[ P_{\\text{SO}_2} = 5.0 \\times 10^{-9}\\text{ atm} \\]
\\[ P_{\\text{H}_2\\text{O}_2} = 1.0 \\times 10^{-9}\\text{ atm} \\]
For hydrogen peroxide:
\\[ [\\text{H}_2\\text{O}_2(aq)] = K_{H,\\text{H}_2\\text{O}_2} P_{\\text{H}_2\\text{O}_2} = (1.4 \\times 10^5\\text{ M/atm})(1.0 \\times 10^{-9}\\text{ atm}) = 1.40 \\times 10^{-4}\\text{ M} \\]
For dissolved bisulfite $[\text{HSO}_3^-]$ at $\\text{pH} = 4.5$ ($[\text{H}^+] = 10^{-4.5} = 3.162 \\times 10^{-5}\\text{ M}$):
\\[ [\\text{SO}_2\\cdot\\text{H}_2\\text{O}] = K_{H,\\text{SO}_2} P_{\\text{SO}_2} = (1.8)(5.0 \\times 10^{-9}) = 9.0 \\times 10^{-9}\\text{ M} \\]
From $K_{a1} = \\frac{[\\text{H}^+][\\text{HSO}_3^-]}{[\\text{SO}_2\\cdot\\text{H}_2\\text{O}]}$:
\\[ [\\text{HSO}_3^-] = \\frac{K_{a1}[\\text{SO}_2\\cdot\\text{H}_2\\text{O}]}{[\\text{H}^+]} = \\frac{(1.7 \\times 10^{-2})(9.0 \\times 10^{-9})}{3.162 \\times 10^{-5}} = \\frac{1.53 \\times 10^{-10}}{3.162 \\times 10^{-5}} = 4.839 \\times 10^{-6}\\text{ M} \\]

**(b) Aqueous Oxidation Rate and Gas-Phase Equivalent Conversion:**
Evaluate the denominator of the rate law:
\\[ 1 + K[\\text{H}^+] = 1 + 17(3.162 \\times 10^{-5}) = 1 + 0.00054 \\approx 1.000 \\]
Substitute into the rate expression:
\\[ R_{\\text{aq}} = k_a [\\text{H}^+] [\\text{H}_2\\text{O}_2(aq)] [\\text{HSO}_3^-] \\]
\\[ R_{\\text{aq}} = (5.2 \\times 10^7)(3.162 \\times 10^{-5})(1.40 \\times 10^{-4})(4.839 \\times 10^{-6}) \\]
\\[ R_{\\text{aq}} = (5.2 \\times 10^7) \\times (2.142 \\times 10^{-14}) = 1.114 \\times 10^{-6}\\text{ M/s} \\]
Now convert to moles of $\\text{SO}_2$ oxidized per cubic meter of air per second:
Liquid water content $L = 0.50\\text{ g/m}^3 = 0.50 \\times 10^{-3}\\text{ L(water)/m}^3\\text{(air)}$.
\\[ R_{\\text{vol}} = R_{\\text{aq}} \\times L_v = (1.114 \\times 10^{-6}\\text{ mol/(L}\\cdot\\text{s)}) \\times (5.0 \\times 10^{-4}\\text{ L/m}^3) = 5.57 \\times 10^{-10}\\text{ mol/(m}^3\\cdot\\text{s)} \\]
Total moles of gas-phase $\\text{SO}_2$ per $\\text{m}^3$ at $283\\text{ K}$ ($1.0\\text{ atm}$):
\\[ n_{\\text{tot}} = \\frac{P}{RT} = \\frac{101325}{8.3145 \\times 283} = 43.06\\text{ mol/m}^3 \\]
\\[ [\\text{SO}_2]_{\\text{gas}} = (5.0 \\times 10^{-9})(43.06) = 2.153 \\times 10^{-7}\\text{ mol/m}^3 \\]
Relative conversion rate per second:
\\[ r_{\\text{rel}} = \\frac{R_{\\text{vol}}}{[\\text{SO}_2]_{\\text{gas}}} = \\frac{5.57 \\times 10^{-10}}{2.153 \\times 10^{-7}} = 2.587 \\times 10^{-3}\\text{ s}^{-1} \\]
Convert to percent per hour:
\\[ \\text{Rate (\\%/hr)} = (2.587 \\times 10^{-3}\\text{ s}^{-1}) \\times 3600\\text{ s/hr} \\times 100\\% = 931\\%\\text{ per hour} \\]
*Note*: This extraordinarily high rate indicates that the reaction is mass-transfer or oxidant-limited; within $\\approx 6-10\\text{ minutes}$, all available dissolved $\\text{H}_2\\text{O}_2$ is exhausted.

**(c) Comparison with Clear-Sky Gas-Phase Oxidation:**
In cloud-free air, gas-phase $\\text{SO}_2$ oxidation by $\\cdot\\text{OH}$ proceeds at only $~1-2\\%\\text{ per hour}$. Inside clouds, aqueous oxidation is several hundred times faster, demonstrating that clouds act as high-speed chemical reactors for acid production."""
        },
        {
            "id": "prob1_8",
            "tier": "Advanced",
            "title": "Three-Way Catalytic Converter Air-to-Fuel Ratio and Mass Stoichiometry",
            "statement": """An internal combustion engine operates on standard gasoline with an average hydrocarbon formula represented as octane ($\\text{C}_8\\text{H}_{18}$, molecular weight $M_F = 114.23\\text{ g/mol}$). The density of dry air is $M_{\\text{air}} = 28.97\\text{ g/mol}$ ($20.95\\%\\ \\text{O}_2$, $79.05\\%\\ \\text{N}_2$).
(a) Write the balanced combustion reaction for complete conversion of $\\text{C}_8\\text{H}_{18}$ in atmospheric air and calculate the exact stoichiometric air-to-fuel mass ratio $(A/F)_{\\text{stoich}}$.
(b) If the engine operates slightly lean at an equivalence ratio $\\lambda = 1.05$ with a fuel consumption rate of $8.0\\text{ kg/hr}$, calculate the mass flow rate of intake air in $\\text{kg/hr}$ and the excess oxygen flow rate in $\\text{g/hr}$.
(c) Explain chemically why operation at $\\lambda = 1.05$ poisons the reduction of $\\text{NO}_x$ on the rhodium surface of a Three-Way Catalyst.""",
            "solution": """**(a) Stoichiometric Air-to-Fuel Ratio:**
Complete stoichiometric combustion reaction:
\\[ \\text{C}_8\\text{H}_{18} + 12.5\\,\\text{O}_2 + 12.5\\left(\\frac{79.05}{20.95}\\right)\\text{N}_2 \\rightarrow 8\\,\\text{CO}_2 + 9\\,\\text{H}_2\\text{O} + 47.166\\,\\text{N}_2 \\]
Moles of $\\text{O}_2$ required per mole of fuel: $n_{\\text{O}_2} = 12.5\\text{ mol}$.
Moles of air required per mole of fuel:
\\[ n_{\\text{air}} = \\frac{12.5}{0.2095} = 59.666\\text{ mol air/mol fuel} \\]
Mass of 1 mole of fuel:
\\[ m_{\\text{fuel}} = 114.23\\text{ g} \\]
Mass of air required:
\\[ m_{\\text{air}} = n_{\\text{air}} \\times M_{\\text{air}} = 59.666 \\times 28.97 = 1728.52\\text{ g} \\]
Stoichiometric Air-to-Fuel mass ratio:
\\[ \\left(\\frac{A}{F}\\right)_{\\text{stoich}} = \\frac{1728.52}{114.23} = 15.132 : 1 \\]
*(Note: With standard air approximation $79/21$, $(A/F)_{\\text{stoich}} \\approx 14.7-15.1$).*

**(b) Air Flow and Excess Oxygen at $\\lambda = 1.05$:**
The air-fuel ratio at $\\lambda = 1.05$:
\\[ \\left(\\frac{A}{F}\\right)_{\\text{actual}} = \\lambda \\times \\left(\\frac{A}{F}\\right)_{\\text{stoich}} = 1.05 \\times 15.132 = 15.889 \\]
Intake air mass flow rate $\\dot{m}_{\\text{air}}$:
\\[ \\dot{m}_{\\text{air}} = 8.0\\text{ kg/hr} \\times 15.889 = 127.11\\text{ kg/hr} \\]
Stoichiometric air required:
\\[ \\dot{m}_{\\text{air,stoich}} = 8.0 \\times 15.132 = 121.06\\text{ kg/hr} \\]
Excess air flow rate:
\\[ \\Delta \\dot{m}_{\\text{air}} = 127.11 - 121.06 = 6.05\\text{ kg/hr} \\]
Mass fraction of oxygen in air:
\\[ w_{\\text{O}_2} = \\frac{0.2095 \\times 32.00}{28.97} = \\frac{6.704}{28.97} = 0.2314 \\quad (23.14\\%) \\]
Excess oxygen mass flow rate:
\\[ \\dot{m}_{\\text{O}_2,\\text{excess}} = 6.05\\text{ kg/hr} \\times 0.2314 = 1.400\\text{ kg/hr} = 1400\\text{ g/hr} \\]

**(c) Chemical Mechanism of Rhodium Catalyst Poisoning under Lean Conditions:**
On the Rhodium ($\text{Rh}$) active sites, $\text{NO}_x$ reduction requires dissociative chemisorption of $\text{NO}$:
\\[ \\text{NO} + 2\\,\\text{Rh}^* \\rightarrow \\text{Rh}-\\text{N} + \\text{Rh}-\\text{O} \\]
followed by nitrogen adatom recombination:
\\[ 2\\,\\text{Rh}-\\text{N} \\rightarrow \\text{N}_2(g) + 2\\,\\text{Rh}^* \\]
Under lean conditions ($\lambda > 1.0$), abundant excess unburned molecular $\text{O}_2$ dissociates competitively onto $\text{Rh}$ sites:
\\[ \\text{O}_2 + 2\\,\\text{Rh}^* \\rightarrow 2\\,\\text{Rh}-\\text{O} \\]
The strong metal-oxygen chemisorption bond saturates the surface, creating an oxide overlayer (forming inactive surface $\text{Rh}_2\text{O}_3$). This competitive site-blocking prevents $\text{NO}$ from binding and dissociating, causing $\text{NO}_x$ reduction efficiency to drop from $> 98\\%$ to less than $20\\%$."""
        },
        {
            "id": "prob1_9",
            "tier": "Advanced",
            "title": "Indoor Radon-222 Ingrowth, Ventilation Dilution and Working Level Equations",
            "statement": """A basement room of volume $V = 120\\text{ m}^3$ has an unsealed concrete floor exhalating Radon-222 ($^{222}\\text{Rn}$, decay constant $\\lambda_{\\text{Rn}} = 2.10 \\times 10^{-6}\\text{ s}^{-1}$, $t_{1/2} = 3.82\\text{ days}$) at a constant flux of $S = 0.80\\text{ Bq}/(\\text{m}^2\\cdot\\text{s})$ over a floor area $A = 50\\text{ m}^2$.
The room has a mechanical air exchange rate $I = 0.35\\text{ h}^{-1}$ (air changes per hour).
(a) Formulate the mass-balance differential equation for indoor radon activity concentration $C(t)$ (in $\\text{Bq/m}^3$).
(b) Calculate the steady-state radon activity concentration $C_{\\text{ss}}$ in $\\text{Bq/m}^3$ and compare it with the WHO reference level ($100\\text{ Bq/m}^3$).
(c) If the ventilation system is turned off completely ($I = 0$), calculate the new theoretical maximum equilibrium radon concentration.
(d) What ventilation rate $I$ is required to maintain the basement concentration below $50\\text{ Bq/m}^3$?""",
            "solution": """**(a) Mass-Balance Differential Equation:**
The total radon entry rate into the room is:
\\[ Q_{\\text{in}} = S \\times A = (0.80\\text{ Bq}/(\\text{m}^2\\cdot\\text{s})) \\times 50\\text{ m}^2 = 40.0\\text{ Bq/s} \\]
Converting air exchange rate $I$ to $\\text{s}^{-1}$:
\\[ \\lambda_v = \\frac{0.35\\text{ hr}^{-1}}{3600\\text{ s/hr}} = 9.722 \\times 10^{-5}\\text{ s}^{-1} \\]
The total loss rate of radon is the sum of radioactive decay and ventilation removal:
\\[ \\lambda_{\\text{eff}} = \\lambda_{\\text{Rn}} + \\lambda_v = 2.10 \\times 10^{-6} + 9.722 \\times 10^{-5} = 9.932 \\times 10^{-5}\\text{ s}^{-1} \\]
The rate of change of radon concentration $C(t)$ (activity per unit volume) is:
\\[ \\frac{dC}{dt} = \\frac{Q_{\\text{in}}}{V} - \\lambda_{\\text{eff}} C(t) = \\frac{40.0}{120} - (9.932 \\times 10^{-5}) C(t) \\]
\\[ \\frac{dC}{dt} = 0.3333 - (9.932 \\times 10^{-5}) C(t) \\]

**(b) Steady-State Concentration $C_{\\text{ss}}$:**
Setting $\\frac{dC}{dt} = 0$:
\\[ C_{\\text{ss}} = \\frac{Q_{\\text{in}}}{V \\lambda_{\\text{eff}}} = \\frac{0.3333\\text{ Bq}/(\\text{m}^3\\cdot\\text{s})}{9.932 \\times 10^{-5}\\text{ s}^{-1}} \\approx 3356\\text{ Bq/m}^3 \\]
*Assessment*: $3356\\text{ Bq/m}^3$ is more than **33 times** higher than the WHO action guideline of $100\\text{ Bq/m}^3$, presenting an acute radiological hazard requiring active sub-slab depressurization and seal remediation.

**(c) Maximum Concentration with Zero Ventilation ($I = 0$):**
When $I = 0$, the only removal mechanism is radioactive decay:
\\[ \\lambda_{\\text{eff}} = \\lambda_{\\text{Rn}} = 2.10 \\times 10^{-6}\\text{ s}^{-1} \\]
\\[ C_{\\text{max}} = \\frac{0.3333}{2.10 \\times 10^{-6}} \\approx 158,730\\text{ Bq/m}^3 \\]

**(d) Required Ventilation Rate for $C_{\\text{target}} \\le 50\\text{ Bq/m}^3$:**
Set $C_{\\text{ss}} = 50\\text{ Bq/m}^3$:
\\[ \\lambda_{\\text{eff,req}} = \\frac{Q_{\\text{in}}}{V \\times C_{\\text{target}}} = \\frac{0.3333}{50} = 6.667 \\times 10^{-3}\\text{ s}^{-1} \\]
Because $\\lambda_{\\text{Rn}} = 2.10 \\times 10^{-6}\\text{ s}^{-1}$ is negligible compared to this rate:
\\[ \\lambda_{v,\\text{req}} \\approx 6.667 \\times 10^{-3}\\text{ s}^{-1} \\]
Convert to air changes per hour:
\\[ I_{\\text{req}} = (6.667 \\times 10^{-3}\\text{ s}^{-1}) \\times 3600\\text{ s/hr} = 24.0\\text{ ACH (air changes per hour)} \\]
*Conclusion*: Achieving $24\\text{ ACH}$ is unfeasible for standard residential HVAC; the proper engineering mitigation is installing an impermeable membrane barrier on the floor and sub-slab suction to evacuate radon before it enters the room."""
        }
    ]

    return {
        "unit_number": 1,
        "title": "Atmospheric Chemistry, Photochemical Smog & Acid Deposition",
        "description": "Planetary atmospheric evolution, hydrostatic equilibrium and scale height, thermal stratification, tropospheric hydroxyl radical detergent cycles, VOC oxidation, nitrogen oxides and the Leighton photostationary state, photochemical smog and PAN thermal dynamics, particulate matter aerodynamic classification, automotive catalytic converter chemistry, acid deposition aqueous kinetics, and environmental radioactivity.",
        "sections": sections,
        "problems": problems
    }

if __name__ == "__main__":
    u = get_unit_1()
    print(f"Unit 1 generated: {len(u['sections'])} sections, {len(u['problems'])} problems.")
