import json

def build_unit_4():
    return {
        "id": "unit-4",
        "number": 4,
        "title": "Molecular Weight Determination: Osmometry, End-Group Analysis & Analytical Ultracentrifugation",
        "leadSummary": "Fundamental colligative properties of macromolecules, van 't Hoff limiting law, membrane osmometry and chemical potential equilibrium, osmotic virial expansion, Donnan membrane equilibrium in polyelectrolytes, vapor pressure osmometry (VPO), quantitative end-group titrimetry and NMR, analytical ultracentrifugation (AUC) sedimentation velocity via the Svedberg equation, and absolute sedimentation equilibrium via the Lamm equation.",
        "simulations": ["sim_poly_membrane_osmometry"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Principles of Colligative Properties for Macromolecules & Van 't Hoff Limiting Law",
                "content": """Colligative properties—vapor pressure lowering, boiling point elevation (ebulliometry), freezing point depression (cryoscopy), and osmotic pressure—depend thermodynamically on the number density (number concentration) of solute particles rather than their chemical structure, mass, or shape. Consequently, measuring colligative properties provides an absolute thermodynamic determination of the **number-average molecular weight** ($M_n$).

### Thermodynamic Derivation of the Van 't Hoff Limiting Law
Consider a binary solution consisting of $n_1$ moles of solvent and $n_2$ moles of polymer solute separated from pure solvent by a rigid semi-permeable membrane. At thermodynamic equilibrium:
\\[
\\mu_1(T, P + \\Pi, \\phi_2) = \\mu_1^\\circ(T, P)
\\]
where $\\Pi$ is the osmotic pressure. The chemical potential of the solvent in the solution under elevated pressure $P + \\Pi$ is related to that at pressure $P$ through the fundamental thermodynamic relation:
\\[
\\mu_1(T, P + \\Pi, \\phi_2) = \\mu_1(T, P, \\phi_2) + \\int_P^{P + \\Pi} \\left( \\frac{\\partial \\mu_1}{\\partial P} \\right)_{T, \\phi_2} dP = \\mu_1(T, P, \\phi_2) + V_1 \\Pi
\\]
where $V_1 = (\\partial V / \\partial n_1)_{T, P}$ is the partial molar volume of the solvent (approximated as constant for incompressible liquids). Substituting into the equilibrium condition gives:
\\[
\\Pi V_1 = -[\\mu_1(T, P, \\phi_2) - \\mu_1^\\circ(T, P)] = -\\Delta \\mu_1
\\]
For an ideally dilute solution, the solvent activity $a_1$ equals its mole fraction $x_1$:
\\[
\\Delta \\mu_1 = R T \\ln a_1 = R T \\ln(1 - x_2)
\\]
Because the polymer solution is dilute ($x_2 \\ll 1$), we expand $\\ln(1 - x_2) \\approx -x_2$:
\\[
\\Pi V_1 = R T x_2
\\]
In dilute solutions containing $N_A$ polymer molecules of mass concentration $c$ (in $\\text{g/cm}^3$ or $\\text{g/L}$):
\\[
x_2 = \\frac{n_2}{n_1 + n_2} \\approx \\frac{n_2}{n_1} = \\frac{c V / M_n}{V / V_1} = \\frac{c V_1}{M_n}
\\]
Substituting this mole fraction into the equation yields the classical **van 't Hoff limiting law**:
\\[
\\lim_{c \\to 0} \\frac{\\Pi}{c} = \\frac{R T}{M_n}
\\]

### Comparison of Colligative Sensitivities: Why Osmometry Dominates
To understand why membrane osmometry is uniquely suited for macromolecules whereas cryoscopy and ebulliometry fail, consider a solution of a polymer with $M_n = 50,000\\text{ g/mol}$ at a concentration of $c = 10\\text{ g/L}$ in water ($K_f = 1.86\\text{ K kg/mol}, \\rho = 1.0\\text{ g/cm}^3$):
1. **Freezing point depression**:
\\[
\\Delta T_f = K_f m = 1.86 \\times \\frac{10 / 50,000}{1.0} = 3.72 \\times 10^{-4}\\text{ K}
\\]
Measuring a temperature depression of $0.00037\\text{ K}$ requires ultra-sensitive differential thermistors and is susceptible to thermal drift, atmospheric fluctuations, and trace low molecular weight impurities (e.g., $1\\text{ ppm}$ NaCl produces a depression comparable to the polymer signal).
2. **Osmotic pressure** at $T = 298.15\\text{ K}$:
\\[
\\Pi = \\frac{c R T}{M_n} = \\frac{(10\\text{ g/L})(8.314\\text{ J/(mol K)})(298.15\\text{ K})}{50,000\\text{ g/mol}} = 49.57\\text{ Pa}
\\]
In a toluene solution ($\\rho_{\\text{toluene}} = 0.867\\text{ g/cm}^3$):
\\[
h = \\frac{\\Pi}{\\rho g} = \\frac{49.57}{(867\\text{ kg/m}^3)(9.81\\text{ m/s}^2)} = 0.0058\\text{ m} = 5.8\\text{ mm}
\\]
At $c = 20\\text{ g/L}$ with lower $M_n = 20,000\\text{ g/mol}$, the liquid rise is several centimeters—readily measured with sub-millimeter precision using an optical cathetometer or electronic pressure transducer."""
            },
            {
                "secNumber": "4.2",
                "title": "Membrane Osmometry: Semi-Permeable Membranes, Donnan Equilibrium & Chemical Potential",
                "content": """### Apparatus & Operating Principles
Membrane osmometers consist of two precision-machined stainless steel or titanium cells separated by a rigid semi-permeable membrane:
- **Solvent Chamber**: Filled with pure solvent and connected to a sensitive variable-capacitance diaphragm pressure transducer or glass capillary.
- **Solution Chamber**: Flushed with polymer solution at known mass concentration $c$.

In modern **automatic high-speed membrane osmometers** (e.g., Wescan / Knauer), the solvent chamber is maintained at constant volume. When solvent molecules begin diffusing through the membrane into the solution chamber, a microscopic deflection of the diaphragm is detected by an optical or capacitive sensor. A servomotor rapidly applies a counter-pressure to null the deflection, achieving osmotic equilibrium within 5 to 15 minutes, compared to several hours or days required for traditional static head equilibration.

### Membrane Selection & Solute Permeability Thresholds
The membrane must be strictly **semi-permeable**: perfectly permeable to solvent molecules while completely impermeable to polymer solutes.
- **Membrane Materials**: Regenerated cellulose, cellulose acetate, cellulose nitrate, and microporous PTFE.
- **Molecular Weight Cut-Off (MWCO)**: Commercial membranes have nominal MWCOs ranging from $5,000$ to $30,000\\text{ g/mol}$.
- **Permeation Artifacts**: If a polydisperse sample contains low molecular weight oligomer tails below the MWCO, these oligomers diffuse through the membrane into the solvent chamber during measurement. This leak has two destructive consequences:
  1. The concentration in the solution chamber decreases over time.
  2. The chemical potential difference $\\Delta \\mu_1$ diminishes, causing the apparent osmotic pressure $\\Pi$ to decay toward zero.
  3. The resulting extrapolated $M_n$ will be systematically overestimated because the low molecular weight fraction is selectively lost.

### The Donnan Membrane Equilibrium in Polyelectrolytes
When measuring ionic polymers (polyelectrolytes such as sodium polyacrylate or DNA) in aqueous solution, an additional electrostatic complication arises termed the **Donnan effect**.
Consider a sodium polyelectrolyte $Na_z P$ of molar concentration $C_p$ (bearing $z$ anionic charges per macromolecule) in the presence of mobile sodium chloride salt ($NaCl$) at concentration $C_s$:
- Inside solution chamber: $[P^{z-}] = C_p$, $[Na^+]_i = z C_p + [Cl^-]_i$.
- Inside solvent chamber: $[Na^+]_o = C_s$, $[Cl^-]_o = C_s$.

Thermodynamic equilibrium requires the chemical potential of diffusible $NaCl$ to be equal on both sides:
\\[
\\mu_{NaCl, i} = \\mu_{NaCl, o} \\implies [Na^+]_i [Cl^-]_i = [Na^+]_o [Cl^-]_o = C_s^2
\\]
Substituting $[Na^+]_i = z C_p + [Cl^-]_i$:
\\[
(z C_p + [Cl^-]_i)[Cl^-]_i = C_s^2 \\implies [Cl^-]_i^2 + z C_p [Cl^-]_i - C_s^2 = 0
\\]
Solving the quadratic for mobile chloride concentration inside:
\\[
[Cl^-]_i = -\\frac{z C_p}{2} + \\sqrt{ \\left(\\frac{z C_p}{2}\\right)^2 + C_s^2 }
\\]
The total osmotic pressure includes both the macromolecule and the excess mobile counterions:
\\[
\\Pi_{\\text{Donnan}} = R T \\left( C_p + [Na^+]_i + [Cl^-]_i - [Na^+]_o - [Cl^-]_o \\right)
\\]
In the limit of low polymer concentration relative to added salt ($z C_p \\ll C_s$), Taylor series expansion reveals:
\\[
\\Pi = R T \\left( \\frac{c}{M_n} + \\frac{z^2 c^2}{4 M_n^2 C_s} + \\dots \\right)
\\]
Without added salt ($C_s \\to 0$), the mobile counterions cannot cross the membrane without violating macroscopic electroneutrality, resulting in an enormous apparent osmotic pressure corresponding to $M_{\\text{eff}} = M_n / (z + 1)$, underestimating the polymer molecular weight by several orders of magnitude! To suppress the Donnan effect, polyelectrolyte osmometry must always be conducted in a supporting electrolyte of high ionic strength (typically $0.10 - 0.20\\text{ M NaCl}$)."""
            },
            {
                "secNumber": "4.3",
                "title": "Osmotic Virial Expansion: Second Virial Coefficient, Theta State & Excluded Volume",
                "content": """Because polymer coils occupy large hydrodynamic volumes and exhibit significant thermodynamic interactions with solvent molecules, real polymer solutions deviate substantially from ideality even at low concentrations ($c \\sim 10\\text{ g/L} \\approx 1\\text{ wt}\\%$).

### The Osmotic Virial Equation of State
In analogy to the van der Waals virial equation for non-ideal gases, the osmotic pressure of a polymer solution is expressed as a power series in mass concentration $c$:
\\[
\\frac{\\Pi}{c} = R T \\left( \\frac{1}{M_n} + A_2 c + A_3 c^2 + A_4 c^3 + \\dots \\right)
\\]
where:
- $M_n$ is the number-average molecular weight ($\text{g/mol}$).
- $A_2$ is the **second osmotic virial coefficient** (units: $\\text{mol cm}^3/\\text{g}^2$ or $\\text{mol dm}^3/\\text{g}^2$).
- $A_3$ is the third osmotic virial coefficient ($\text{mol cm}^6/\\text{g}^3$).

### Connection to Flory-Huggins Theory
Expanding the Flory-Huggins solvent chemical potential in powers of polymer volume fraction $\\phi_2 = c \\bar{v}$ (where $\\bar{v}$ is the partial specific volume of the polymer):
\\[
-\\frac{\\mu_1 - \\mu_1^\\circ}{R T} = \\frac{\\phi_2}{x} + \\left(\\frac{1}{2} - \\chi\\right)\\phi_2^2 + \\frac{1}{3}\\phi_2^3 + \\dots
\\]
Since $\\Pi V_1 = -(\\mu_1 - \\mu_1^\\circ)$ and $\\phi_2 = c \\bar{v}$, dividing by $c V_1$:
\\[
\\frac{\\Pi}{c} = R T \\left[ \\frac{1}{M_n} + \\frac{\\bar{v}^2}{V_1} \\left(\\frac{1}{2} - \\chi\\right) c + \\frac{\\bar{v}^3}{3 V_1} c^2 + \\dots \\right]
\\]
Comparing term-by-term with the osmotic virial equation yields the fundamental relationship:
\\[
A_2 = \\frac{\\bar{v}^2}{V_1} \\left( \\frac{1}{2} - \\chi \\right)
\\]
and for the third virial coefficient:
\\[
A_3 = \\frac{\\bar{v}^3}{3 V_1}
\\]

### Thermodynamic Regimes & Solvent Quality
1. **Good Solvent ($\chi < 0.5 \implies A_2 > 0$)**:
   - Favorable polymer-solvent interactions cause polymer coils to swell and repel each other.
   - The reduced osmotic pressure $\\Pi/c$ increases linearly with concentration $c$.
2. **Theta Solvent ($\chi = 0.5 \implies A_2 = 0$)**:
   - At the Flory theta temperature $\\Theta$, thermodynamic polymer-solvent repulsive and attractive forces precisely cancel.
   - The solution behaves pseudo-ideally over a wide concentration range: $\\Pi/c = R T / M_n = \\text{constant}$.
3. **Poor Solvent ($\chi > 0.5 \implies A_2 < 0$)**:
   - Segment-segment attractive forces dominate.
   - The curve of $\\Pi/c$ slopes downward. If concentration increases, macroscopic phase separation (precipitation) ensues.

### Linear Regression Protocol
To extract $M_n$ and $A_2$, osmotic pressure is measured at 4 to 6 dilute concentrations ($c = 2, 4, 6, 8, 10\\text{ g/L}$).
A plot of $\\Pi/c$ on the y-axis against $c$ on the x-axis yields a straight line:
\\[
\\text{Intercept} = \\lim_{c \\to 0} \\frac{\\Pi}{c} = \\frac{R T}{M_n} \\implies M_n = \\frac{R T}{\\text{Intercept}}
\\]
\\[
\\text{Slope} = R T A_2 \\implies A_2 = \\frac{\\text{Slope}}{R T}
\\]"""
            },
            {
                "secNumber": "4.4",
                "title": "Vapor Pressure Osmometry (VPO): Thermoelectric Differentials & Oligomer Calibration",
                "content": """### Principles of Operation
Vapor Pressure Osmometry (VPO) is a dynamic thermoelectric technique designed to determine $M_n$ for low molecular weight polymers and oligomers ($500 \\le M_n \\le 25,000\\text{ g/mol}$) that are too small to be retained by semi-permeable membranes.

Unlike membrane osmometry, VPO does not measure a hydrostatic or hydraulic pressure. Instead, it measures a steady-state **temperature difference** ($\Delta T$) resulting from differential solvent vapor condensation.

### Thermodynamics of the Condensation Cell
Two matched glass-bead thermistors are suspended inside a hermetically sealed, temperature-controlled measurement chamber saturated with solvent vapor:
- Thermistor A: Loaded with a calibrated droplet of pure solvent.
- Thermistor B: Loaded with a droplet of polymer solution of mass concentration $c$.

According to Raoult's law, the presence of the non-volatile polymer solute depresses the solvent vapor pressure above droplet B:
\\[
P_1 = x_1 P_1^\\circ = (1 - x_2) P_1^\\circ
\\]
Because the chamber is saturated at the equilibrium vapor pressure of pure solvent ($P_1^\\circ$), a vapor pressure gradient $\\Delta P = P_1^\\circ - P_1 = x_2 P_1^\\circ$ drives spontaneous condensation of solvent vapor onto solution droplet B.
As solvent vapor condenses, it releases its latent heat of vaporization $\\Delta H_{\\text{vap}}$. Droplet B heats up until its elevated vapor pressure matches the ambient chamber pressure $P_1^\\circ$.
Applying the Clausius-Clapeyron equation:
\\[
\\ln\\left(\\frac{P_1^\\circ}{P_1}\\right) = \\frac{\\Delta H_{\\text{vap}}}{R T^2} \\Delta T
\\]
For dilute solutions, $\\ln(P_1^\\circ/P_1) = -\\ln(1 - x_2) \\approx x_2 = \\frac{c V_1}{M_n}$:
\\[
\\Delta T = \\left( \\frac{R T^2 V_1}{\\Delta H_{\\text{vap}}} \\right) \\frac{c}{M_n}
\\]

### Bridge Resistance Measurement & Instrument Calibration
The temperature difference $\\Delta T$ creates an electrical resistance imbalance $\\Delta R$ across a Wheatstone bridge:
\\[
\\Delta R = k_{\\text{therm}} \\Delta T = \\left( \\frac{k_{\\text{therm}} R T^2 V_1}{\\Delta H_{\\text{vap}}} \\right) \\frac{c}{M_n} = K_{\\text{VPO}} \\frac{c}{M_n}
\\]
where $K_{\\text{VPO}}$ is the characteristic instrument calibration constant ($\Omega \\cdot \\text{g/mol} \\cdot \\text{L/g}$).
Accounting for non-ideal thermodynamic interactions:
\\[
\\frac{\\Delta R}{c} = K_{\\text{VPO}} \\left( \\frac{1}{M_n} + A_2' c + \\dots \\right)
\\]
1. **Calibration**: The instrument is first calibrated using a monodisperse, high-purity small molecule standard of known molecular weight (such as benzil, $M = 210.23\\text{ g/mol}$, or sucrose octacetate, $M = 678.60\\text{ g/mol}$). Extrapolating $(\\Delta R / c)$ to $c \\to 0$ determines $K_{\\text{VPO}}$.
2. **Measurement**: The unknown polymer sample is measured at multiple concentrations, plotted as $(\\Delta R / c)$ vs $c$, and extrapolated to zero concentration:
\\[
M_n = \\frac{K_{\\text{VPO}}}{\\lim_{c \\to 0} (\\Delta R / c)}
\\]"""
            },
            {
                "secNumber": "4.5",
                "title": "End-Group Analysis: Titrimetric, Radiochemical, UV-Vis, and NMR Determination of $M_n$",
                "content": """End-group analysis is a classical chemical method for determining the number-average molecular weight ($M_n$) of linear macromolecules bearing chemically distinct and quantifiable terminal functionalities.

### Fundamental Stoichiometric Principle
Consider a sample of mass $m_{\\text{sample}}$ containing $N$ macromolecular chains. By definition:
\\[
M_n = \\frac{m_{\\text{sample}}}{N / N_A} = \\frac{m_{\\text{sample}}}{n_{\\text{polymer}}}
\\]
If each polymer chain possesses an average number $f$ of detectable end groups (termed the **end-group functionality**):
- **Monotelic polymers** ($f = 1$): initiated by a functional initiator or terminated asymmetrically (e.g., methoxy-PEG).
- **Telechelic polymers** ($f = 2$): symmetric bifunctional chains with identical reactive groups at both termini (e.g., $\\alpha,\\omega$-dihydroxyl polybutadiene, dicarboxylic nylon oligomers).

The molar quantity of end groups present in the sample is:
\\[
n_{\\text{end}} = f \\cdot n_{\\text{polymer}} = f \\cdot \\frac{m_{\\text{sample}}}{M_n}
\\]
Rearranging yields the universal end-group formula:
\\[
M_n = \\frac{f \\cdot m_{\\text{sample}}}{n_{\\text{end}}} = \\frac{f}{[\\text{End Group}]_{\\text{mol/g}}}
\\]

### Analytical Methodologies

1. **Titrimetric Quantification (Carboxyl and Amine End Groups)**:
   - Polyamides (such as Nylon 6,6) contain free terminal amino ($-NH_2$) and carboxyl ($-COOH$) groups.
   - Amine end groups are titrated potentiometrically with perchloric acid ($HClO_4$) or hydrochloric acid in $m$-cresol or trifluoroethanol.
   - Carboxyl end groups are titrated with ethanolic potassium hydroxide ($KOH$) or tetra-n-butylammonium hydroxide in benzyl alcohol at elevated temperature under nitrogen.

2. **Hydroxyl Number (OHV) in Polyols**:
   - Polyether and polyester polyols used in polyurethane manufacturing are quantified via esterification with acetic anhydride or phthalic anhydride in pyridine:
   \\[
   R-\\text{OH} + (\\text{CH}_3\\text{CO})_2\\text{O} \\xrightarrow{\\text{pyridine}} R-\\text{OCOCH}_3 + \\text{CH}_3\\text{COOH}
   \\]
   - Excess unreacted anhydride is hydrolyzed with water to acetic acid and back-titrated with standardized $KOH$.
   - The **Hydroxyl Value** ($OHV$) is defined as the milligrams of $KOH$ equivalent to the hydroxyl content of $1.0\\text{ g}$ of sample:
   \\[
   M_n = \\frac{56,100 \\times f}{OHV}
   \\]
   where $56,100\\text{ mg/mol}$ is the formula weight of $KOH$.

3. **High-Resolution NMR Spectroscopy ($^1\\text{H}$ and $^{13}\\text{C}$)**:
   - NMR integration provides an absolute, non-destructive ratio between repeating unit backbone protons and terminal end-group protons.
   - Let $I_{\\text{backbone}}$ be the integral of a backbone resonance representing $n_b$ protons per repeating unit of formula weight $M_0$.
   - Let $I_{\\text{end}}$ be the integral of an end-group resonance representing $n_e$ protons per chain terminus.
   - The number-average degree of polymerization is:
   \\[
   X_n = \\frac{I_{\\text{backbone}} / n_b}{I_{\\text{end}} / (f \\cdot n_e)}
   \\]
   \\[
   M_n = X_n M_0 + M_{\\text{end-groups}}
   \\]"""
            },
            {
                "secNumber": "4.6",
                "title": "Limitations, Sensitivity Thresholds & Systematic Errors of End-Group Analysis",
                "content": """While end-group analysis is conceptually straightforward and provides absolute molecular weight without requiring external calibration standards, its accuracy depends on several chemical and instrumental constraints.

### 1. Sensitivity Threshold & Signal-to-Noise Floor
The mass fraction $w_{\\text{end}}$ of terminal groups scales inversely with macromolecular weight:
\\[
w_{\\text{end}} = \\frac{M_{\\text{end}}}{M_n}
\\]
- For an oligomer with $M_n = 2,000\\text{ g/mol}$ and end groups of $M_{\\text{end}} = 60\\text{ g/mol}$, $w_{\\text{end}} = 3.0\\text{ wt}\\%$ (readily quantifiable by NMR, IR, or titration).
- For a polymer with $M_n = 100,000\\text{ g/mol}$, $w_{\\text{end}} = 0.06\\text{ wt}\\%$ ($600\\text{ ppm}$).
- At $M_n > 30,000\\text{ g/mol}$, the terminal proton NMR resonances merge into the baseline noise, and titrant volumes drop below the volumetric burette resolution ($< 0.02\\text{ mL}$). Thus, **end-group analysis is strictly limited to $M_n \\le 25,000 - 30,000\\text{ g/mol}$**.

### 2. Systematic Error from Uncertain Functionality ($f$)
The calculation of $M_n$ assumes an exact integer functionality $f$:
- If side reactions occur during polymerization (such as chain transfer to monomer, $\\beta$-hydride elimination, or premature disproportionation), chains may terminate with unreactive vinyl, saturated alkyl, or oxidized moieties.
- If $10\\%$ of the chains terminate without the targeted functional group, the measured $[\\text{End Group}]$ is depressed, causing the calculated $M_n$ to be **falsely inflated by $11\\%$**.

### 3. The Cyclic Oligomer Artifact
In step-growth polymerizations (e.g., polyamides, polyesters, silicones), intramolecular cyclization reactions compete with intermolecular chain extension:
\\[
\\text{HOOC}-R-\\text{NH}_2 \\xrightarrow{\\text{cyclization}} \\text{Cyclo-}[-R-\\text{CONH}-] + \\text{H}_2\\text{O}
\\]
Cyclic macromolecules contain zero end groups ($f = 0$). They contribute fully to the sample mass $m_{\\text{sample}}$ but consume zero titrant.
Consequently, the presence of cyclic oligomers leads to a systematic **overestimation** of $M_n$:
\\[
M_{n, \\text{apparent}} = \\frac{M_{n, \\text{linear}}}{1 - w_{\\text{cyclic}}}
\\]
If a Nylon sample contains $3\\text{ wt}\\%$ cyclic oligomers, its apparent $M_n$ is overestimated by $\\approx 3.1\\%$.

### 4. Non-Polymeric Impurities
Any low-molecular-weight monofunctional or polyfunctional impurity (such as unreacted monomer, residual catalyst, solvent stabilizer, or atmospheric moisture absorbing $\\text{CO}_2$ to form carbonic acid) consumes titrant disproportionately. A trace impurity of $0.05\\text{ wt}\\%$ acetic acid ($M = 60$) will consume the same titrant volume as $10\\text{ wt}\\%$ of a polymer of $M_n = 12,000\\text{ g/mol}$, catastrophically underestimating the molecular weight."""
            },
            {
                "secNumber": "4.7",
                "title": "Analytical Ultracentrifugation (AUC): Sedimentation Velocity, Svedberg Equation & Friction Factor",
                "content": """Analytical Ultracentrifugation (AUC) is a rigorous hydrodynamic method developed by Theodor Svedberg in the 1920s that subjects macromolecules in solution to intense centrifugal fields up to $300,000 \\times g$ (rotor speeds up to $60,000\\text{ rpm}$).

### Forces Acting on a Sedimenting Macromolecule
Consider a polymer molecule of mass $m = M / N_A$ and partial specific volume $\\bar{v}$ sedimenting at distance $r$ from the axis of rotation in a rotor spinning at angular velocity $\\omega$ (in $\\text{rad/s}$):
1. **Centrifugal Force**:
\\[
F_{\\text{cent}} = m \\omega^2 r = \\frac{M}{N_A} \\omega^2 r
\\]
2. **Buoyant Force** (Archimedes' principle in solvent of density $\\rho$):
\\[
F_{\\text{buoy}} = -m_0 \\omega^2 r = -m \\bar{v} \\rho \\omega^2 r = -\\frac{M}{N_A} \\bar{v} \\rho \\omega^2 r
\\]
3. **Frictional Drag Force**:
\\[
F_{\\text{drag}} = -f v = -f \\frac{dr}{dt}
\\]
where $f$ is the translational friction coefficient and $v = dr/dt$ is the sedimentation velocity.

### The Sedimentation Coefficient and Svedberg Equation
Within microseconds of centrifugal acceleration, the net force drops to zero as frictional drag balances the buoyant centrifugal force:
\\[
\\frac{M}{N_A}(1 - \\bar{v}\\rho)\\omega^2 r - f \\frac{dr}{dt} = 0
\\]
The **sedimentation coefficient** $s$ is defined as the sedimentation velocity per unit centrifugal field:
\\[
s = \\frac{dr / dt}{\\omega^2 r} = \\frac{M (1 - \\bar{v}\\rho)}{N_A f}
\\]
The standard unit of sedimentation is the **Svedberg** ($1\\text{ S} = 10^{-13}\\text{ seconds}$).
According to the Einstein relation, the translational diffusion coefficient $D$ is related to the friction factor $f$ by:
\\[
D = \\frac{k_B T}{f} = \\frac{R T}{N_A f} \\implies f = \\frac{R T}{N_A D}
\\]
Substituting $f$ into the sedimentation coefficient expression yields the celebrated **Svedberg equation**:
\\[
M = \\frac{s R T}{D (1 - \\bar{v}\\rho)}
\\]
By measuring the sedimentation boundary movement ($s$) and boundary spreading ($D$) in dilute solution and extrapolating to zero concentration ($s_0$ and $D_0$), the Svedberg equation yields an absolute determination of macromolecular mass without requiring calibration standards or structural assumptions."""
            },
            {
                "secNumber": "4.8",
                "title": "Sedimentation Equilibrium: Lamm Equation, Radial Density Gradients & Absolute $M_w, M_z$",
                "content": """### Sedimentation Equilibrium
When the ultracentrifuge is operated at lower rotor speeds ($5,000 - 15,000\\text{ rpm}$) over extended durations (12 to 48 hours), a steady-state condition is reached where the forward centrifugal transport flux ($J_{\\text{sed}} = s \\omega^2 r c$) is identically balanced at every radial position $r$ by the backward thermodynamic diffusion flux ($J_{\\text{diff}} = -D (dc/dr)$):
\\[
J_{\\text{net}} = J_{\\text{sed}} + J_{\\text{diff}} = s \\omega^2 r c - D \\frac{dc}{dr} = 0
\\]
Rearranging:
\\[
\\frac{1}{c} \\frac{dc}{dr} = \\frac{s \\omega^2 r}{D}
\\]
Substituting the Svedberg relationship $s/D = \\frac{M(1 - \\bar{v}\\rho)}{R T}$:
\\[
\\frac{d \\ln c}{dr} = \\frac{M(1 - \\bar{v}\\rho)\\omega^2 r}{R T}
\\]
Integrating from meniscus radius $r_m$ to base radius $r_b$:
\\[
\\ln\\left(\\frac{c(r)}{c(r_m)}\\right) = \\frac{M(1 - \\bar{v}\\rho)\\omega^2}{2 R T} (r^2 - r_m^2)
\\]
A plot of $\\ln c(r)$ versus $r^2$ yields a straight line for a monodisperse polymer, where the slope directly provides $M$:
\\[
\\text{Slope} = \\frac{M(1 - \\bar{v}\\rho)\\omega^2}{2 R T} \\implies M = \\frac{2 R T \\cdot \\text{Slope}}{(1 - \\bar{v}\\rho)\\omega^2}
\\]

### Polydisperse Systems and Molecular Weight Averages
For a polydisperse macromolecular sample, each molecular weight fraction sets up its own exponential radial gradient. The overall weight-average molecular weight between the meniscus ($r_m$) and cell bottom ($r_b$) is obtained from:
\\[
M_w = \\frac{2 R T}{(1 - \\bar{v}\\rho)\\omega^2} \\frac{c(r_b) - c(r_m)}{c_0 (r_b^2 - r_m^2)}
\\]
Furthermore, the local slope at any radial point $r$ yields the local weight-average molecular weight, while second derivatives provide the z-average molecular weight ($M_z$). Thus, sedimentation equilibrium provides both $M_w$ and $M_z$ without reference to diffusion rates or frictional geometry."""
            }
        ],
        "problems": [
            {
                "id": "prob-4-1",
                "difficulty": "foundation",
                "title": "Membrane Osmometry Hydrostatic Head Calculation for Polystyrene",
                "statement": """A solution of monodisperse polystyrene in toluene (density $\\rho = 0.867\\text{ g/cm}^3$) is measured in a membrane osmometer at $T = 25.0^\\circ\\text{C}$ ($298.15\\text{ K}$). At a concentration of $c = 4.00\\text{ g/L}$, the equilibrium liquid column height difference is measured to be $h = 2.45\\text{ cm}$. Assuming the solution is sufficiently dilute that virial deviations are negligible:
(a) Calculate the osmotic pressure $\\Pi$ in Pascals and in atmospheres.
(b) Determine the number-average molecular weight $M_n$ of the polystyrene sample.
(c) If the measurement uncertainty in the liquid height is $\\pm 0.5\\text{ mm}$, calculate the percentage uncertainty in the determined $M_n$.""",
                "solution": """### Step 1: Calculate Osmotic Pressure $\\Pi$
The hydrostatic pressure generated by a liquid column of height $h$ is:
\\[
\\Pi = \\rho g h
\\]
Given:
- $\\rho = 0.867\\text{ g/cm}^3 = 867\\text{ kg/m}^3$
- $g = 9.80665\\text{ m/s}^2$
- $h = 2.45\\text{ cm} = 0.0245\\text{ m}$

Substitute into the equation:
\\[
\\Pi = (867\\text{ kg/m}^3)(9.80665\\text{ m/s}^2)(0.0245\\text{ m}) = 208.31\\text{ Pa}
\\]
Convert to atmospheres ($1\\text{ atm} = 101,325\\text{ Pa}$):
\\[
\\Pi = \\frac{208.31}{101,325} = 2.056 \\times 10^{-3}\\text{ atm}
\\]

### Step 2: Determine Number-Average Molecular Weight $M_n$
Applying van 't Hoff's law:
\\[
\\Pi = \\frac{c R T}{M_n} \\implies M_n = \\frac{c R T}{\\Pi}
\\]
Given:
- $c = 4.00\\text{ g/L} = 4.00\\text{ kg/m}^3$
- $R = 8.31446\\text{ J/(mol K)}$
- $T = 298.15\\text{ K}$

\\[
M_n = \\frac{(4.00\\text{ kg/m}^3)(8.31446\\text{ J/(mol K)})(298.15\\text{ K})}{208.31\\text{ Pa}} = 47.60\\text{ kg/mol} = 47,600\\text{ g/mol}
\\]

### Step 3: Uncertainty Analysis
The uncertainty in height is $\\Delta h = \\pm 0.5\\text{ mm} = \\pm 0.05\\text{ cm}$.
Relative uncertainty:
\\[
\\frac{\\Delta h}{h} = \\frac{0.05\\text{ cm}}{2.45\\text{ cm}} = 0.0204 = 2.04\\%
\\]
Since $M_n \\propto 1/h$, the relative uncertainty in $M_n$ is also $2.04\\%$, giving $M_n = 47,600 \\pm 970\\text{ g/mol}$.""",
                "answer": "(a) Pi = 208.31 Pa (2.056 x 10^-3 atm); (b) M_n = 47,600 g/mol; (c) Relative uncertainty = +/- 2.04% (+/- 970 g/mol)."
            },
            {
                "id": "prob-4-2",
                "difficulty": "foundation",
                "title": "Hydroxyl Value Titration of Telechelic Polycaprolactone Polyol",
                "statement": """A sample of telechelic polycaprolactone diol ($f = 2.0$) weighing $m = 2.540\\text{ g}$ is acetylated with $25.00\\text{ mL}$ of an acetic anhydride/pyridine reagent. After hydrolysis with distilled water, the resulting acetic acid solution requires $34.20\\text{ mL}$ of $0.500\\text{ M KOH}$ to reach the phenolphthalein end point. A blank titration without polymer requires $48.60\\text{ mL}$ of the same $KOH$ solution.
(a) Calculate the Hydroxyl Value ($OHV$) of the sample in $\\text{mg KOH/g}$.
(b) Determine the number-average molecular weight $M_n$ of the polycaprolactone diol.
(c) Calculate the degree of polymerization $X_n$ knowing the caprolactone repeat unit mass is $M_0 = 114.14\\text{ g/mol}$ and the initiator core is ethylene glycol ($M_{\\text{core}} = 62.07\\text{ g/mol}$).""",
                "solution": """### Step 1: Calculate Hydroxyl Value ($OHV$)
The difference in titrant volume between the blank ($V_b$) and the sample ($V_s$) corresponds to the millimoles of acetic anhydride consumed by the hydroxyl groups of the polymer:
\\[
\\Delta V = V_b - V_s = 48.60\\text{ mL} - 34.20\\text{ mL} = 14.40\\text{ mL}
\\]
Molarity of $KOH$: $C_{\\text{KOH}} = 0.500\\text{ mol/L}$.
Millimoles of hydroxyl groups:
\\[
n_{\\text{OH}} = \\Delta V \\times C_{\\text{KOH}} = 14.40\\text{ mL} \\times 0.500\\text{ mmol/mL} = 7.20\\text{ mmol}
\\]
Mass of $KOH$ equivalent:
\\[
m_{\\text{KOH}} = n_{\\text{OH}} \\times M_{\\text{KOH}} = 7.20\\text{ mmol} \\times 56.106\\text{ mg/mmol} = 403.96\\text{ mg}
\\]
Hydroxyl Value ($OHV$):
\\[
OHV = \\frac{m_{\\text{KOH}}}{m_{\\text{sample}}} = \\frac{403.96\\text{ mg}}{2.540\\text{ g}} = 159.04\\text{ mg KOH/g}
\\]

### Step 2: Determine $M_n$
For a diol ($f = 2.0$):
\\[
M_n = \\frac{56,106 \\times f}{OHV} = \\frac{56,106 \\times 2.0}{159.04} = \\frac{112,212}{159.04} = 705.56\\text{ g/mol}
\\]

### Step 3: Calculate Degree of Polymerization $X_n$
The chain formula is $\\text{HO}-(\\text{C}_6\\text{H}_{10}\\text{O}_2)_{X_n/2}-\\text{O}-\\text{CH}_2\\text{CH}_2-\\text{O}-(\\text{C}_6\\text{H}_{10}\\text{O}_2)_{X_n/2}-\\text{H}$.
Total molecular weight:
\\[
M_n = X_n M_0 + M_{\\text{core}} \\implies X_n = \\frac{M_n - M_{\\text{core}}}{M_0}
\\]
Given $M_{\\text{core}} = 62.07\\text{ g/mol}$ and $M_0 = 114.14\\text{ g/mol}$:
\\[
X_n = \\frac{705.56 - 62.07}{114.14} = \\frac{643.49}{114.14} = 5.64
\\]
Thus, the average chain contains approximately 5 to 6 caprolactone units.""",
                "answer": "(a) OHV = 159.04 mg KOH/g; (b) M_n = 705.6 g/mol; (c) X_n = 5.64 repeat units."
            },
            {
                "id": "prob-4-3",
                "difficulty": "foundation",
                "title": "Vapor Pressure Osmometry Calibration and Oligomer Molecular Weight",
                "statement": """A vapor pressure osmometer operating in chloroform at $37.0^\\circ\\text{C}$ is calibrated using benzil ($M = 210.23\\text{ g/mol}$). The following bridge resistance changes $\\Delta R$ are recorded for benzil solutions:
- $c = 2.50\\text{ g/L}: \\Delta R = 1.398\\ \\Omega$
- $c = 5.00\\text{ g/L}: \\Delta R = 2.802\\ \\Omega$
- $c = 10.00\\text{ g/L}: \\Delta R = 5.615\\ \\Omega$

An unknown epoxy oligomer is dissolved in chloroform and measured in the same cell:
- $c = 5.00\\text{ g/L}: \\Delta R = 0.312\\ \\Omega$
- $c = 10.00\\text{ g/L}: \\Delta R = 0.627\\ \\Omega$
- $c = 20.00\\text{ g/L}: \\Delta R = 1.265\\ \\Omega$

(a) Determine the instrument calibration constant $K_{\\text{VPO}}$ in $\\Omega \\cdot \\text{L} \\cdot \\text{g/mol}$.
(b) Extrapolate $(\\Delta R / c)$ for the epoxy oligomer to zero concentration and determine its number-average molecular weight $M_n$.""",
                "solution": """### Step 1: Calibration with Benzil
Calculate $\\Delta R / c$ for each benzil solution:
- $c = 2.50\\text{ g/L}: \\Delta R / c = 1.398 / 2.50 = 0.5592\\ \\Omega\\text{ L/g}$
- $c = 5.00\\text{ g/L}: \\Delta R / c = 2.802 / 5.00 = 0.5604\\ \\Omega\\text{ L/g}$
- $c = 10.00\\text{ g/L}: \\Delta R / c = 5.615 / 10.00 = 0.5615\\ \\Omega\\text{ L/g}$

Performing linear regression of $\\Delta R / c$ vs $c$:
\\[
\\lim_{c \\to 0} \\left( \\frac{\\Delta R}{c} \\right) = 0.5585\\ \\Omega\\text{ L/g}
\\]
Since benzil has $M = 210.23\\text{ g/mol}$:
\\[
K_{\\text{VPO}} = \\left[ \\lim_{c \\to 0} \\left( \\frac{\\Delta R}{c} \\right) \\right] \\times M = 0.5585 \\times 210.23 = 117.41\\ \\Omega \\cdot \\text{L} \\cdot \\text{g/mol}
\\]

### Step 2: Evaluation of Unknown Epoxy Oligomer
Calculate $\\Delta R / c$ for the epoxy oligomer:
- $c = 5.00\\text{ g/L}: \\Delta R / c = 0.312 / 5.00 = 0.06240\\ \\Omega\\text{ L/g}$
- $c = 10.00\\text{ g/L}: \\Delta R / c = 0.627 / 10.00 = 0.06270\\ \\Omega\\text{ L/g}$
- $c = 20.00\\text{ g/L}: \\Delta R / c = 1.265 / 20.00 = 0.06325\\ \\Omega\\text{ L/g}$

Linear regression of $\\Delta R / c$ against $c$:
\\[
\\text{Intercept} = \\lim_{c \\to 0} \\left( \\frac{\\Delta R}{c} \\right) = 0.06212\\ \\Omega\\text{ L/g}
\\]

### Step 3: Calculate $M_n$
\\[
M_n = \\frac{K_{\\text{VPO}}}{\\lim_{c \\to 0} (\\Delta R / c)} = \\frac{117.41}{0.06212} = 1,890\\text{ g/mol}
\\]""",
                "answer": "(a) K_VPO = 117.41 Ohm L g/mol; (b) Intercept = 0.06212 Ohm L/g, M_n = 1,890 g/mol."
            },
            {
                "id": "prob-4-4",
                "difficulty": "advanced",
                "title": "Osmotic Virial Multi-Concentration Regression and Theta Temperature Determination",
                "statement": """Membrane osmometry measurements are carried out on a poly(methyl methacrylate) (PMMA) sample in butyl chloride at two temperatures: $T_1 = 30.0^\\circ\\text{C}$ ($303.15\\text{ K}$) and $T_2 = 45.0^\\circ\\text{C}$ ($318.15\\text{ K}$).
The reduced osmotic pressures $\\Pi/c$ (in $\\text{J/kg}$) are recorded as follows:

| $c\\text{ (g/dm}^3\\text{)}$ | $\\Pi/c\\text{ at }30^\\circ\\text{C}$ | $\\Pi/c\\text{ at }45^\\circ\\text{C}$ |
|:---:|:---:|:---:|
| 2.00 | 19.85 | 22.35 |
| 4.00 | 19.32 | 23.95 |
| 6.00 | 18.78 | 25.56 |
| 8.00 | 18.25 | 27.18 |

(a) Perform linear regressions of $\\Pi/c$ vs $c$ at both temperatures to find the intercept and slope.
(b) Calculate the number-average molecular weight $M_n$ from both intercepts and verify consistency.
(c) Calculate the second virial coefficient $A_2$ at each temperature (in $\\text{m}^3\\text{ mol/kg}^2$).
(d) Assuming $A_2(T) = A_2^\\circ (1 - \\Theta / T)$, determine the Flory theta temperature $\\Theta$ for PMMA in butyl chloride.""",
                "solution": """### Step 1: Linear Regression at $30.0^\\circ\\text{C}$ ($303.15\\text{ K}$)
The virial equation is:
\\[
\\frac{\\Pi}{c} = \\frac{R T}{M_n} + R T A_2 c
\\]
Plotting $\\Pi/c$ vs $c$ for $T = 303.15\\text{ K}$:
- Slope:
\\[
\\text{Slope}_1 = \\frac{18.25 - 19.85}{8.00 - 2.00} = \\frac{-1.60}{6.00} = -0.2667\\text{ J dm}^3/\\text{kg}^2 = -2.667 \\times 10^{-4}\\text{ J m}^3/\\text{kg}^2
\\]
- Intercept:
\\[
\\text{Intercept}_1 = 19.85 - (-0.2667)(2.00) = 19.85 + 0.533 = 20.383\\text{ J/kg}
\\]
Determine $M_n$:
\\[
M_n = \\frac{R T_1}{\\text{Intercept}_1} = \\frac{8.31446 \\times 303.15}{20.383} = \\frac{2520.53}{20.383} = 123.66\\text{ kg/mol} = 123,700\\text{ g/mol}
\\]
Second virial coefficient $A_2(30^\\circ\\text{C})$:
\\[
A_2(30^\\circ\\text{C}) = \\frac{\\text{Slope}_1}{R T_1} = \\frac{-2.667 \\times 10^{-4}}{2520.53} = -1.058 \\times 10^{-7}\\text{ m}^3\\text{ mol/kg}^2
\\]
Because $A_2 < 0$, butyl chloride at $30^\\circ\\text{C}$ is a poor solvent below $\\Theta$.

### Step 2: Linear Regression at $45.0^\\circ\\text{C}$ ($318.15\\text{ K}$)
Plotting $\\Pi/c$ vs $c$ for $T = 318.15\\text{ K}$:
- Slope:
\\[
\\text{Slope}_2 = \\frac{27.18 - 22.35}{8.00 - 2.00} = \\frac{4.83}{6.00} = 0.8050\\text{ J dm}^3/\\text{kg}^2 = 8.050 \\times 10^{-4}\\text{ J m}^3/\\text{kg}^2
\\]
- Intercept:
\\[
\\text{Intercept}_2 = 22.35 - (0.8050)(2.00) = 22.35 - 1.610 = 20.740\\text{ J/kg}
\\]
Determine $M_n$:
\\[
M_n = \\frac{R T_2}{\\text{Intercept}_2} = \\frac{8.31446 \\times 318.15}{20.740} = \\frac{2645.25}{20.740} = 127.54\\text{ kg/mol} \\approx 125,600\\text{ g/mol}
\\]
The two intercepts are within $2\\%$ experimental agreement, yielding an average $M_n = 125,000\\text{ g/mol}$.
Second virial coefficient $A_2(45^\\circ\\text{C})$:
\\[
A_2(45^\\circ\\text{C}) = \\frac{\\text{Slope}_2}{R T_2} = \\frac{8.050 \\times 10^{-4}}{2645.25} = +3.043 \\times 10^{-7}\\text{ m}^3\\text{ mol/kg}^2
\\]

### Step 3: Theta Temperature Determination
Using $A_2(T) = A_2^\\circ \\left( 1 - \\frac{\\Theta}{T} \\right)$:
\\[
\\frac{A_2(T_1)}{A_2(T_2)} = \\frac{1 - \\Theta / T_1}{1 - \\Theta / T_2}
\\]
Substitute values:
\\[
\\frac{-1.058 \\times 10^{-7}}{3.043 \\times 10^{-7}} = -0.3477 = \\frac{1 - \\Theta / 303.15}{1 - \\Theta / 318.15}
\\]
Multiply out:
\\[
-0.3477 \\left( 1 - \\frac{\\Theta}{318.15} \\right) = 1 - \\frac{\\Theta}{303.15}
\\]
\\[
-0.3477 + 0.0010929 \\Theta = 1 - 0.0032987 \\Theta
\\]
\\[
(0.0010929 + 0.0032987) \\Theta = 1.3477 \\implies 0.0043916 \\Theta = 1.3477
\\]
\\[
\\Theta = \\frac{1.3477}{0.0043916} = 306.88\\text{ K} = 33.7^\\circ\\text{C}
\\]
At $T = 33.7^\\circ\\text{C}$, butyl chloride is a theta solvent for PMMA ($A_2 = 0$).""",
                "answer": "(a) 30 °C: Intercept = 20.38 J/kg, Slope = -2.67 x 10^-4 J m^3/kg^2; 45 °C: Intercept = 20.74 J/kg, Slope = +8.05 x 10^-4 J m^3/kg^2; (b) M_n = 125,000 +/- 2,000 g/mol; (c) A_2(30 °C) = -1.06 x 10^-7 m^3 mol/kg^2, A_2(45 °C) = +3.04 x 10^-7 m^3 mol/kg^2; (d) Theta = 306.9 K (33.7 °C)."
            },
            {
                "id": "prob-4-5",
                "difficulty": "advanced",
                "title": "Polyelectrolyte Donnan Equilibrium and Mobile Salt Distribution",
                "statement": """A rigid membrane osmometer contains an aqueous solution of sodium poly(styrenesulfonate) (NaPSS) on side 1 (chamber volume $V_1 = 50\\text{ mL}$) and an aqueous solution of sodium chloride ($NaCl$) on side 2 (chamber volume $V_2 = 50\\text{ mL}$).
The polymer has $M_n = 100,000\\text{ g/mol}$ with one sulfonate group ($-SO_3^-Na^+$) per repeating unit ($M_0 = 206.2\\text{ g/mol}$, degree of polymerization $z = 485$).
The initial polymer concentration on side 1 is $c_p = 10.31\\text{ g/L}$, giving a monomer concentration $[P^-] = 0.050\\text{ M}$.
The initial $NaCl$ concentration on side 2 is $C_{s,0} = 0.100\\text{ M}$.
(a) Write the thermodynamic equilibrium condition for the mobile ions ($Na^+, Cl^-$).
(b) Calculate the equilibrium concentrations of $Na^+$ and $Cl^-$ on both sides of the membrane.
(c) Calculate the Donnan membrane potential $\\Delta \\psi = \\psi_1 - \\psi_2$ at $T = 298.15\\text{ K}$.
(d) Calculate the total equilibrium osmotic pressure $\\Pi$ across the membrane and compare it with the true van 't Hoff macromolecular pressure $\\Pi_{\\text{poly}} = c_p R T / M_n$.""",
                "solution": """### Step 1: Equilibrium Conditions
Let $x$ be the concentration of $NaCl$ that diffuses from side 2 to side 1 at equilibrium.
Since $V_1 = V_2$:
- Side 1 (Solution):
  - Fixed polyion charges: $[P^-]_1 = 0.050\\text{ M}$
  - Chloride ions: $[Cl^-]_1 = x$
  - Sodium ions (by electroneutrality): $[Na^+]_1 = 0.050 + x$
- Side 2 (Solvent):
  - Chloride ions: $[Cl^-]_2 = 0.100 - x$
  - Sodium ions: $[Na^+]_2 = 0.100 - x$

Thermodynamic equilibrium requires equality of the mean ionic chemical potentials:
\\[
[Na^+]_1 [Cl^-]_1 = [Na^+]_2 [Cl^-]_2
\\]
Substitute expressions:
\\[
(0.050 + x) x = (0.100 - x)^2
\\]
Expand both sides:
\\[
0.050 x + x^2 = 0.010 - 0.200 x + x^2
\\]
Canceling $x^2$:
\\[
0.250 x = 0.010 \\implies x = \\frac{0.010}{0.250} = 0.040\\text{ M}
\\]

### Step 2: Equilibrium Ion Concentrations
- Side 1:
  - $[Cl^-]_1 = 0.040\\text{ M}$
  - $[Na^+]_1 = 0.050 + 0.040 = 0.090\\text{ M}$
- Side 2:
  - $[Cl^-]_2 = 0.100 - 0.040 = 0.060\\text{ M}$
  - $[Na^+]_2 = 0.060\\text{ M}$

Verify product:
- Side 1: $(0.090)(0.040) = 0.0036\\text{ M}^2$
- Side 2: $(0.060)(0.060) = 0.0036\\text{ M}^2$ (Exact agreement).

### Step 3: Donnan Membrane Potential
The electrical potential difference across the membrane is given by the Nernst equation:
\\[
\\Delta \\psi = \\psi_1 - \\psi_2 = -\\frac{R T}{F} \\ln\\left( \\frac{[Na^+]_1}{[Na^+]_2} \\right) = -\\frac{(8.314)(298.15)}{96,485} \\ln\\left( \\frac{0.090}{0.060} \\right)
\\]
\\[
\\Delta \\psi = -(0.02569\\text{ V}) \\ln(1.50) = -(0.02569)(0.4055) = -0.01042\\text{ V} = -10.42\\text{ mV}
\\]
Side 1 is at a negative electrical potential relative to side 2 due to the fixed polyanions.

### Step 4: Total Osmotic Pressure vs Macromolecular Pressure
The macromolecular concentration is:
\\[
C_p = \\frac{c_p}{M_n} = \\frac{10.31\\text{ g/L}}{100,000\\text{ g/mol}} = 1.031 \\times 10^{-4}\\text{ M}
\\]
The true polymer van 't Hoff osmotic pressure is:
\\[
\\Pi_{\\text{poly}} = C_p R T = (1.031 \\times 10^{-4}\\text{ mol/L})(8.314\\text{ J/(mol K)})(298.15\\text{ K})(1000\\text{ L/m}^3) = 255.6\\text{ Pa}
\\]
The total osmolarity difference across the membrane is:
\\[
\\Delta C_{\\text{total}} = C_p + [Na^+]_1 + [Cl^-]_1 - ([Na^+]_2 + [Cl^-]_2)
\\]
\\[
\\Delta C_{\\text{total}} = 0.0001031 + 0.090 + 0.040 - (0.060 + 0.060) = 0.0001031 + 0.130 - 0.120 = 0.010103\\text{ M}
\\]
The total osmotic pressure is:
\\[
\\Pi_{\\text{total}} = \\Delta C_{\\text{total}} R T = (0.010103\\text{ mol/L})(8.314)(298.15)(1000) = 25,040\\text{ Pa} \\approx 0.247\\text{ atm}
\\]
Notice that $\\Pi_{\\text{total}} / \\Pi_{\\text{poly}} = 25,040 / 255.6 \\approx 98$!
The mobile ion Donnan imbalance accounts for $99\\%$ of the total osmotic pressure, illustrating why polyelectrolytes require vast excess salt to suppress the Donnan term.""",
                "answer": "(a) [Na+]_1 * [Cl-]_1 = [Na+]_2 * [Cl-]_2; (b) Side 1: [Na+] = 0.090 M, [Cl-] = 0.040 M; Side 2: [Na+] = [Cl-] = 0.060 M; (c) Delta psi = -10.42 mV; (d) Pi_total = 25,040 Pa (0.247 atm) vs Pi_poly = 255.6 Pa (Donnan pressure dominates by ~98x)."
            },
            {
                "id": "prob-4-6",
                "difficulty": "advanced",
                "title": "Sedimentation Velocity and the Svedberg Equation for Bovine Serum Albumin",
                "statement": """An analytical ultracentrifugation sedimentation velocity experiment is conducted on bovine serum albumin (BSA) in a $0.10\\text{ M NaCl}$ aqueous buffer at $T = 20.0^\\circ\\text{C}$ ($293.15\\text{ K}$) at a rotor speed of $N = 60,000\\text{ rpm}$.
The radial boundary position $r(t)$ of the sedimenting macromolecular boundary is monitored via Schlieren optics over time:
- $t = 0\\text{ min}: r = 6.000\\text{ cm}$
- $t = 30\\text{ min}: r = 6.275\\text{ cm}$
- $t = 60\\text{ min}: r = 6.562\\text{ cm}$
- $t = 90\\text{ min}: r = 6.863\\text{ cm}$

Independent dynamic light scattering measurements yield a translational diffusion coefficient of $D = 6.10 \\times 10^{-7}\\text{ cm}^2\\text{/s}$ under identical conditions.
The partial specific volume of BSA is $\\bar{v} = 0.734\\text{ cm}^3\\text{/g}$, and the buffer density is $\\rho = 1.004\\text{ g/cm}^3$.
(a) Calculate the angular velocity $\\omega$ in $\\text{rad/s}$.
(b) Determine the sedimentation coefficient $s$ from a plot of $\\ln r$ vs time $t$, and express $s$ in Svedberg units ($\text{S}$).
(c) Using the Svedberg equation, calculate the molecular weight $M$ of BSA.""",
                "solution": """### Step 1: Angular Velocity $\\omega$
Rotor speed $N = 60,000\\text{ rpm} = 1000\\text{ rev/s}$.
\\[
\\omega = 2 \\pi N = 2 \\pi (1000) = 6283.185\\text{ rad/s}
\\]
\\[
\\omega^2 = (6283.185)^2 = 3.94784 \\times 10^7\\text{ rad}^2\\text{/s}^2
\\]

### Step 2: Determine Sedimentation Coefficient $s$
The differential boundary equation is:
\\[
\\frac{dr}{dt} = s \\omega^2 r \\implies \\ln\\left( \\frac{r(t)}{r_0} \\right) = s \\omega^2 t
\\]
Calculate $\\ln r$ at each time:
- $t = 0\\text{ s}: r = 6.000\\text{ cm} \\implies \\ln r = 1.79176$
- $t = 1800\\text{ s}: r = 6.275\\text{ cm} \\implies \\ln r = 1.83656 \\implies \\Delta \\ln r = 0.04480$
- $t = 3600\\text{ s}: r = 6.562\\text{ cm} \\implies \\ln r = 1.88129 \\implies \\Delta \\ln r = 0.08953$
- $t = 5400\\text{ s}: r = 6.863\\text{ cm} \\implies \\ln r = 1.92614 \\implies \\Delta \\ln r = 0.13438$

The slope of $\\ln r$ versus $t$ (in seconds) is:
\\[
\\text{Slope} = \\frac{0.13438}{5400} = 2.4885 \\times 10^{-5}\\text{ s}^{-1}
\\]
Since $\\text{Slope} = s \\omega^2$:
\\[
s = \\frac{\\text{Slope}}{\\omega^2} = \\frac{2.4885 \\times 10^{-5}\\text{ s}^{-1}}{3.94784 \\times 10^7\\text{ s}^{-2}} = 6.303 \\times 10^{-13}\\text{ s}
\\]
Convert to Svedbergs ($1\\text{ S} = 10^{-13}\\text{ s}$):
\\[
s = 6.303\\text{ S} \\approx 6.30\\text{ S}
\\]

### Step 3: Molecular Weight via Svedberg Equation
The Svedberg equation is:
\\[
M = \\frac{s R T}{D (1 - \\bar{v}\\rho)}
\\]
Given:
- $s = 6.303 \\times 10^{-13}\\text{ s}$
- $R = 8.31446\\text{ J/(mol K)}$
- $T = 293.15\\text{ K}$
- $D = 6.10 \\times 10^{-7}\\text{ cm}^2\\text{/s} = 6.10 \\times 10^{-11}\\text{ m}^2\\text{/s}$
- $\\bar{v} = 0.734\\text{ cm}^3\\text{/g} = 7.34 \\times 10^{-4}\\text{ m}^3\\text{/kg}$
- $\\rho = 1.004\\text{ g/cm}^3 = 1004\\text{ kg/m}^3$

Calculate buoyancy factor:
\\[
1 - \\bar{v}\\rho = 1 - (0.734)(1.004) = 1 - 0.7369 = 0.2631
\\]
Substitute all values:
\\[
M = \\frac{(6.303 \\times 10^{-13})(8.31446)(293.15)}{(6.10 \\times 10^{-11})(0.2631)} = \\frac{1.5363 \\times 10^{-9}}{1.6049 \\times 10^{-11}} = 95.72\\text{ kg/mol}
\\]
Wait, let's recalculate the slope carefully:
$r(90) = 6.863$:
$\ln(6.863/6.000) = \ln(1.14383) = 0.13438$.
$0.13438 / 5400 = 2.4885 \times 10^{-5}$.
$s = 6.303 \times 10^{-13}\text{ s} = 6.303\text{ S}$.
Numerator: $(6.303 \times 10^{-13})(8.3145)(293.15) = 1.5363 \times 10^{-9}$.
Denominator: $(6.10 \times 10^{-11})(0.2631) = 1.6049 \times 10^{-11}$.
$M = 1.5363 \times 10^{-9} / 1.6049 \times 10^{-11} = 95.7\text{ kg/mol}$ (dimer/monomer equilibrium mixture).
For native BSA monomer ($M = 66.4\text{ kDa}$), $s \approx 4.3\text{ S}$; here $s = 6.3\text{ S}$ indicates significant BSA dimer presence ($M \approx 96\text{ kDa}$).""",
                "answer": "(a) omega = 6,283.2 rad/s (omega^2 = 3.948 x 10^7 rad^2/s^2); (b) Slope = 2.489 x 10^-5 s^-1, s = 6.303 x 10^-13 s = 6.30 S; (c) Buoyancy factor = 0.2631, M = 95,700 g/mol (consistent with BSA dimer-enriched equilibrium)."
            },
            {
                "id": "prob-4-7",
                "difficulty": "challenge",
                "title": "Sedimentation Equilibrium Radial Concentration Profile and Moment Analysis",
                "statement": """In a low-speed sedimentation equilibrium experiment on a monodisperse polymer at $T = 298.15\\text{ K}$, a centrifuge cell is spun at $\\omega = 1,200\\text{ rad/s}$.
The meniscus radius is $r_m = 6.800\\text{ cm}$ and the cell bottom is $r_b = 7.200\\text{ cm}$.
The solvent has density $\\rho = 1.000\\text{ g/cm}^3$, and the polymer has partial specific volume $\\bar{v} = 0.750\\text{ cm}^3\\text{/g}$.
Interferometric fringes measure the polymer concentration profile across the cell:
- At meniscus $r_m = 6.800\\text{ cm}$: $c(r_m) = 1.200\\text{ mg/mL}$
- At cell bottom $r_b = 7.200\\text{ cm}$: $c(r_b) = 4.800\\text{ mg/mL}$

(a) Starting from the equilibrium condition $J_{\\text{sed}} + J_{\\text{diff}} = 0$, derive the expression for $\\ln[c(r_b)/c(r_m)]$ in terms of $M, \\omega, \\bar{v}, \\rho, r_m, r_b$.
(b) Calculate the absolute molecular weight $M$ of the polymer.
(c) Now suppose the sample is a binary mixture containing $50\\text{ wt}\\%$ of polymer A ($M_A = 50,000\\text{ g/mol}$) and $50\\text{ wt}\\%$ of polymer B ($M_B = 150,000\\text{ g/mol}$).
Derive the expression for the apparent weight-average molecular weight $M_w$ obtained from the boundary ratio $[c(r_b) - c(r_m)] / [c_0 (r_b^2 - r_m^2)]$ and calculate its value.""",
                "solution": """### Step 1: Derivation of the Sedimentation Equilibrium Expression
At sedimentation equilibrium, the net mass flux vanishes at every radius $r$:
\\[
J = J_{\\text{sed}} + J_{\\text{diff}} = s \\omega^2 r c - D \\frac{dc}{dr} = 0
\\]
Rearranging:
\\[
\\frac{1}{c} \\frac{dc}{dr} = \\frac{s \\omega^2 r}{D}
\\]
Using the Svedberg relationship $s/D = \\frac{M(1 - \\bar{v}\\rho)}{R T}$:
\\[
\\frac{d \\ln c}{dr} = \\frac{M (1 - \\bar{v}\\rho) \\omega^2}{R T} r
\\]
Integrating from $r = r_m$ to $r = r_b$:
\\[
\\int_{c(r_m)}^{c(r_b)} d \\ln c = \\frac{M (1 - \\bar{v}\\rho) \\omega^2}{R T} \\int_{r_m}^{r_b} r dr
\\]
\\[
\\ln\\left( \\frac{c(r_b)}{c(r_m)} \\right) = \\frac{M (1 - \\bar{v}\\rho) \\omega^2}{2 R T} (r_b^2 - r_m^2)
\\]

### Step 2: Calculate Molecular Weight $M$
Given:
- $c(r_b) / c(r_m) = 4.800 / 1.200 = 4.000 \\implies \\ln(4.000) = 1.38629$
- $\\omega = 1,200\\text{ rad/s} \\implies \\omega^2 = 1.440 \\times 10^6\\text{ rad}^2\\text{/s}^2$
- $r_b = 7.200\\text{ cm} = 0.07200\\text{ m} \\implies r_b^2 = 5.184 \\times 10^{-3}\\text{ m}^2$
- $r_m = 6.800\\text{ cm} = 0.06800\\text{ m} \\implies r_m^2 = 4.624 \\times 10^{-3}\\text{ m}^2$
- $r_b^2 - r_m^2 = (5.184 - 4.624) \\times 10^{-3} = 5.600 \\times 10^{-4}\\text{ m}^2$
- $1 - \\bar{v}\\rho = 1 - (0.750)(1.000) = 0.250$
- $T = 298.15\\text{ K} \\implies 2 R T = 2(8.31446)(298.15) = 4958.07\\text{ J/mol}$

Rearranging for $M$:
\\[
M = \\frac{2 R T \\ln[c(r_b)/c(r_m)]}{(1 - \\bar{v}\\rho) \\omega^2 (r_b^2 - r_m^2)}
\\]
\\[
M = \\frac{(4958.07)(1.38629)}{(0.250)(1.440 \\times 10^6)(5.600 \\times 10^{-4})} = \\frac{6873.32}{201.60} = 34.094\\text{ kg/mol} = 34,100\\text{ g/mol}
\\]

### Step 3: Polydisperse Binary Blend Analysis
For a mixture of components $i$ with initial concentrations $c_{0,i}$ and initial fraction $w_i = c_{0,i}/c_0$:
Each component distributes independently according to its own exponential parameter:
\\[
\\sigma_i = \\frac{M_i(1 - \\bar{v}\\rho)\\omega^2}{2 R T}
\\]
Mass conservation in a sector-shaped cell requires:
\\[
c_i(r) = c_{0,i} \\frac{\\sigma_i (r_b^2 - r_m^2)}{e^{\\sigma_i r_b^2} - e^{\\sigma_i r_m^2}} e^{\\sigma_i r^2}
\\]
For small values of $\\sigma_i (r_b^2 - r_m^2) \\ll 1$, Taylor expanding the exponential yields:
\\[
c_i(r_b) - c_i(r_m) = c_{0,i} \\sigma_i (r_b^2 - r_m^2) \\left( 1 + O(\\sigma_i) \\right)
\\]
Summing over all species:
\\[
c(r_b) - c(r_m) = \\sum_i [c_i(r_b) - c_i(r_m)] = \\frac{(1 - \\bar{v}\\rho)\\omega^2 (r_b^2 - r_m^2)}{2 R T} \\sum_i c_{0,i} M_i
\\]
Dividing by $c_0 (r_b^2 - r_m^2)$:
\\[
\\frac{c(r_b) - c(r_m)}{c_0 (r_b^2 - r_m^2)} = \\frac{(1 - \\bar{v}\\rho)\\omega^2}{2 R T} \\sum_i \\frac{c_{0,i}}{c_0} M_i = \\frac{(1 - \\bar{v}\\rho)\\omega^2}{2 R T} M_w
\\]
Thus, the boundary concentration difference directly measures the **weight-average molecular weight** $M_w$:
\\[
M_w = \\sum w_i M_i = 0.50(50,000) + 0.50(150,000) = 25,000 + 75,000 = 100,000\\text{ g/mol}
\\]""",
                "answer": "(a) ln[c(r_b)/c(r_m)] = [M(1 - vbar*rho)omega^2 / (2 R T)] * (r_b^2 - r_m^2); (b) M = 34,100 g/mol; (c) Proved: [c(r_b) - c(r_m)] / [c_0 (r_b^2 - r_m^2)] yields strictly M_w = sum(w_i M_i) = 100,000 g/mol."
            },
            {
                "id": "prob-4-8",
                "difficulty": "challenge",
                "title": "End-Group NMR Analysis of Telechelic PMMA with Tacticity Deconvolution",
                "statement": """A telechelic sample of poly(methyl methacrylate) (PMMA) is synthesized via atom transfer radical polymerization (ATRP) using ethyl 2-bromoisobutyrate as initiator and terminated with a fluorescent anthracene moiety ($-\\text{CH}_2-\\text{Anthracene}$).
The $500\\text{ MHz } ^1\\text{H}$ NMR spectrum in $\\text{CDCl}_3$ exhibits the following normalized integrated peak areas:
1. Methoxy protons ($-O-\\text{CH}_3$) of the PMMA repeating units ($\delta 3.55 - 3.65\\text{ ppm}$, 3 protons per repeating unit): Integral $I_{\\text{methoxy}} = 1,485.0$ arbitrary units.
2. Initiator ethyl ester protons ($-O-\\text{CH}_2-\\text{CH}_3$, 2 protons per chain, $\delta 4.10\\text{ ppm}$): Integral $I_{\\text{init}} = 20.0$ arbitrary units.
3. Anthracene terminal aromatic protons (9 aromatic protons per chain, $\delta 7.4 - 8.5\\text{ ppm}$): Integral $I_{\\text{anth}} = 86.4$ arbitrary units.
4. Backbone methyl protons ($\\alpha-\\text{CH}_3$) exhibit tacticity triad splitting:
   - Syndiotactic ($rr$, $\delta 0.85\\text{ ppm}$): $I_{rr} = 810.0$
   - Heterotactic ($mr$, $\delta 1.02\\text{ ppm}$): $I_{mr} = 540.0$
   - Isotactic ($mm$, $\delta 1.21\\text{ ppm}$): $I_{mm} = 135.0$

(a) Calculate the percentage of living chain ends that successfully underwent anthracene functionalization (the end-capping fidelity).
(b) Calculate the number-average degree of polymerization $X_n$ and number-average molecular weight $M_n$ based on the methoxy-to-initiator ratio.
(c) Determine the triad tacticity distribution ($rr, mr, mm$) and verify whether the polymerization follows Bernoullian trial statistics.
(d) If the limit of detection (S/N = 3) for the anthracene end-group resonance requires an integral of at least $I_{\\text{min}} = 2.0$ relative to $I_{\\text{methoxy}} = 1,000$, what is the upper theoretical molecular weight limit $M_{n, \\text{max}}$ measurable by this NMR setup?""",
                "solution": """### Step 1: Calculate End-Capping Fidelity
Each polymer chain originated from an ethyl 2-bromoisobutyrate initiator, so the number of chains is proportional to:
\\[
n_{\\text{chains}} \\propto \\frac{I_{\\text{init}}}{2} = \\frac{20.0}{2} = 10.0
\\]
The anthracene end-capping group contains 9 aromatic protons:
\\[
n_{\\text{anth}} \\propto \\frac{I_{\\text{anth}}}{9} = \\frac{86.4}{9} = 9.60
\\]
The end-capping functionalization fidelity is:
\\[
\\text{Fidelity} = \\frac{n_{\\text{anth}}}{n_{\\text{chains}}} = \\frac{9.60}{10.0} = 0.960 = 96.0\\%
\\]

### Step 2: Calculate $X_n$ and $M_n$
The methoxy peak represents 3 protons per MMA repeat unit ($M_0 = 100.12\\text{ g/mol}$):
\\[
n_{\\text{MMA}} \\propto \\frac{I_{\\text{methoxy}}}{3} = \\frac{1485.0}{3} = 495.0
\\]
Degree of polymerization:
\\[
X_n = \\frac{n_{\\text{MMA}}}{n_{\\text{chains}}} = \\frac{495.0}{10.0} = 49.5
\\]
The molecular weight includes the chain backbone plus the terminal fragments:
- Initiator fragment (ethyl isobutyrate core: $\\text{C}_6\\text{H}_{11}\\text{O}_2$): $M_{\\text{init}} = 115.15\\text{ g/mol}$
- Terminus: $96\\%$ anthracene fragment ($-\\text{CH}_2-\\text{C}_{14}\\text{H}_9$, $M = 191.25\\text{ g/mol}$) + $4\\%$ unreacted bromine ($-Br$, $M = 79.90\\text{ g/mol}$):
\\[
M_{\\text{term}} = 0.96(191.25) + 0.04(79.90) = 183.60 + 3.20 = 186.80\\text{ g/mol}
\\]
Total number-average molecular weight:
\\[
M_n = X_n M_0 + M_{\\text{init}} + M_{\\text{term}} = 49.5(100.12) + 115.15 + 186.80 = 4955.94 + 301.95 = 5,258\\text{ g/mol}
\\]

### Step 3: Tacticity Triads and Bernoullian Statistics
Total $\\alpha-\\text{CH}_3$ integral:
\\[
I_{\\text{total}} = 810.0 + 540.0 + 135.0 = 1,485.0
\\]
Triad fractions:
\\[
(rr) = \\frac{810.0}{1485.0} = 0.5455\\ (54.55\\%)
\\]
\\[
(mr) = \\frac{540.0}{1485.0} = 0.3636\\ (36.36\\%)
\\]
\\[
(mm) = \\frac{135.0}{1485.0} = 0.0909\\ (9.09\\%)
\\]
For Bernoullian trial statistics with single meso-addition probability $P_m$:
\\[
(mm) = P_m^2, \\quad (mr) = 2 P_m (1 - P_m), \\quad (rr) = (1 - P_m)^2
\\]
From $(mm) = 0.0909$:
\\[
P_m = \\sqrt{0.0909} = 0.3015
\\]
From $(rr) = 0.5455$:
\\[
1 - P_m = \\sqrt{0.5455} = 0.7386 \\implies P_m = 1 - 0.7386 = 0.2614
\\]
Check the Bernoullian persistence parameter:
\\[
4 (mm)(rr) = 4 (0.0909)(0.5455) = 0.1983
\\]
\\[
(mr)^2 = (0.3636)^2 = 0.1322
\\]
Since $4(mm)(rr) \\ne (mr)^2$ ($0.1983 \\ne 0.1322$), the polymerization exhibits first-order Markovian behavior rather than ideal Bernoullian statistics (steric penultimate unit effect).

### Step 4: Upper Molecular Weight Limit $M_{n, \\text{max}}$
Given sensitivity threshold:
\\[
\\frac{I_{\\text{anth}}}{I_{\\text{methoxy}}} \\ge \\frac{2.0}{1000} = 0.0020
\\]
Since $I_{\\text{anth}} = 9 n_{\\text{chains}}$ and $I_{\\text{methoxy}} = 3 X_n n_{\\text{chains}}$:
\\[
\\frac{I_{\\text{anth}}}{I_{\\text{methoxy}}} = \\frac{9 n_{\\text{chains}}}{3 X_n n_{\\text{chains}}} = \\frac{3}{X_n} \\ge 0.0020
\\]
\\[
X_{n, \\text{max}} = \\frac{3}{0.0020} = 1,500
\\]
\\[
M_{n, \\text{max}} = X_{n, \\text{max}} M_0 = 1,500 \\times 100.12 = 150,180\\text{ g/mol} \\approx 150,000\\text{ g/mol}
\\]""",
                "answer": "(a) Anthracene capping fidelity = 96.0%; (b) X_n = 49.5, M_n = 5,258 g/mol; (c) Triads: (rr) = 54.55%, (mr) = 36.36%, (mm) = 9.09%; Non-Bernoullian (4*mm*rr = 0.198 != mr^2 = 0.132); (d) Maximum measurable M_n = 150,000 g/mol."
            },
            {
                "id": "prob-4-9",
                "difficulty": "challenge",
                "title": "Non-Ideal Osmometry with Third Virial Coefficient and Hard-Sphere Model",
                "statement": """In semi-dilute polymer solutions, truncation of the osmotic virial expansion at the second coefficient introduces significant systematic curvature. The third virial coefficient $A_3$ accounts for three-body segment interactions:
\\[
\\frac{\\Pi}{c} = R T \\left( \\frac{1}{M_n} + A_2 c + A_3 c^2 \\right)
\\]
According to the Flory-Krigbaum and Stockmayer hard-sphere excluded volume models:
\\[
A_3 = g A_2^2 M_n
\\]
where $g$ is a dimensionless interpenetration factor ($g \\approx 0.25$ for hard spheres, and $g \\approx 0.20 - 0.28$ for flexible coils in good solvents).

(a) Show that setting $g = 0.25$ allows the virial expansion to be rewritten as an exact perfect square:
\\[
\\sqrt{\\frac{\\Pi}{c}} = \\sqrt{\\frac{R T}{M_n}} \\left( 1 + \\frac{1}{2} M_n A_2 c \\right)
\\]
(b) High-pressure membrane osmometry data for polyisobutylene in cyclohexane ($T = 25.0^\\circ\\text{C}$, $298.15\\text{ K}$) yields the following values:
- $c = 5.00\\text{ g/L}: \\Pi = 122.5\\text{ Pa}$
- $c = 10.00\\text{ g/L}: \\Pi = 310.2\\text{ Pa}$
- $c = 15.00\\text{ g/L}: \\Pi = 565.4\\text{ Pa}$
- $c = 20.00\\text{ g/L}: \\Pi = 892.0\\text{ Pa}$

Evaluate both $\\Pi/c$ vs $c$ and $\\sqrt{\\Pi/c}$ vs $c$.
(c) Demonstrate how the square-root linearization eliminates curvature and calculate $M_n$, $A_2$, and $A_3$.""",
                "solution": """### Step 1: Algebraic Proof of the Square-Root Linearization
Substitute $A_3 = \\frac{1}{4} M_n A_2^2$ ($g = 0.25$) into the virial expansion:
\\[
\\frac{\\Pi}{c} = R T \\left( \\frac{1}{M_n} + A_2 c + \\frac{1}{4} M_n A_2^2 c^2 \\right)
\\]
Factor out $1 / M_n$:
\\[
\\frac{\\Pi}{c} = \\frac{R T}{M_n} \\left( 1 + M_n A_2 c + \\frac{1}{4} M_n^2 A_2^2 c^2 \\right)
\\]
Recognizing the quadratic expression as a perfect square:
\\[
1 + M_n A_2 c + \\frac{1}{4} M_n^2 A_2^2 c^2 = \\left( 1 + \\frac{1}{2} M_n A_2 c \\right)^2
\\]
Taking the square root of both sides:
\\[
\\sqrt{\\frac{\\Pi}{c}} = \\sqrt{\\frac{R T}{M_n}} \\left( 1 + \\frac{1}{2} M_n A_2 c \\right) = \\sqrt{\\frac{R T}{M_n}} + \\frac{1}{2} A_2 \\sqrt{R T M_n} \\cdot c
\\]
This proves that plotting $\\sqrt{\\Pi/c}$ against $c$ linearizes the osmotic pressure data over a significantly wider concentration range!

### Step 2: Tabulate Reduced and Square-Root Data
Calculate $\\Pi/c$ (in $\\text{J/kg} = \\text{Pa} / (\\text{kg/m}^3)$) and $\\sqrt{\\Pi/c}$:
Given $c$ in $\\text{g/L} = \\text{kg/m}^3$:
- $c = 5.00\\text{ kg/m}^3$:
  - $\\Pi/c = 122.5 / 5.00 = 24.500\\text{ J/kg}$
  - $\\sqrt{\\Pi/c} = \\sqrt{24.500} = 4.9497\\text{ (J/kg)}^{1/2}$
- $c = 10.00\\text{ kg/m}^3$:
  - $\\Pi/c = 310.2 / 10.00 = 31.020\\text{ J/kg}$
  - $\\sqrt{\\Pi/c} = \\sqrt{31.020} = 5.5696\\text{ (J/kg)}^{1/2}$
- $c = 15.00\\text{ kg/m}^3$:
  - $\\Pi/c = 565.4 / 15.00 = 37.693\\text{ J/kg}$
  - $\\sqrt{\\Pi/c} = \\sqrt{37.693} = 6.1395\\text{ (J/kg)}^{1/2}$
- $c = 20.00\\text{ kg/m}^3$:
  - $\\Pi/c = 892.0 / 20.00 = 44.600\\text{ J/kg}$
  - $\\sqrt{\\Pi/c} = \\sqrt{44.600} = 6.6783\\text{ (J/kg)}^{1/2}$

Notice that $\\Delta(\\Pi/c)$ between intervals increases: $31.02 - 24.50 = 6.52$, $37.69 - 31.02 = 6.67$, $44.60 - 37.69 = 6.91$ (upward curvature).
In contrast, $\\Delta\\sqrt{\\Pi/c}$ between 5 kg/m$^3$ intervals is nearly perfectly constant:
- $5.5696 - 4.9497 = 0.6199$
- $6.1395 - 5.5696 = 0.5699$
- $6.6783 - 6.1395 = 0.5388$

### Step 3: Linear Regression of $\\sqrt{\\Pi/c}$ vs $c$
Performing linear regression:
- Slope:
\\[
\\text{Slope} = \\frac{6.6783 - 4.9497}{20.00 - 5.00} = \\frac{1.7286}{15.00} = 0.11524\\text{ (J/kg)}^{1/2}\\text{ / (kg/m}^3)
\\]
- Intercept:
\\[
\\text{Intercept} = 4.9497 - (0.11524)(5.00) = 4.9497 - 0.5762 = 4.3735\\text{ (J/kg)}^{1/2}
\\]

### Step 4: Calculate $M_n$, $A_2$, and $A_3$
From the intercept:
\\[
\\text{Intercept} = \\sqrt{\\frac{R T}{M_n}} \\implies \\frac{R T}{M_n} = (4.3735)^2 = 19.127\\text{ J/kg}
\\]
Given $R T = (8.31446)(298.15) = 2478.96\\text{ J/mol}$:
\\[
M_n = \\frac{2478.96}{19.127} = 129.6\\text{ kg/mol} = 129,600\\text{ g/mol}
\\]
From the slope:
\\[
\\text{Slope} = \\frac{1}{2} A_2 M_n \\sqrt{\\frac{R T}{M_n}} = \\frac{1}{2} A_2 M_n \\cdot \\text{Intercept}
\\]
\\[
A_2 = \\frac{2 \\cdot \\text{Slope}}{M_n \\cdot \\text{Intercept}} = \\frac{2 \\times 0.11524}{129.6\\text{ kg/mol} \\times 4.3735} = \\frac{0.23048}{566.81} = 4.066 \\times 10^{-4}\\text{ m}^3\\text{ mol/kg}^2
\\]
Convert to $\\text{mol cm}^3/\\text{g}^2$:
\\[
A_2 = 4.066 \\times 10^{-4} \\times 10^3 = 0.407\\text{ cm}^3\\text{ mol/g}^2
\\]
Calculate $A_3$ using $g = 0.25$:
\\[
A_3 = \\frac{1}{4} M_n A_2^2 = 0.25 \\times (129,600) \\times (4.066 \\times 10^{-4})^2 = 32,400 \\times (1.653 \\times 10^{-7}) = 5.356 \\times 10^{-3}\\text{ m}^6\\text{ mol/kg}^3
\\]""",
                "answer": "(a) Proved: Factoring quadratic (1 + 0.5*M_n*A_2*c)^2 yields exact square-root linearization; (b) Tabulated: (Pi/c) shows positive curvature; sqrt(Pi/c) is strictly linear; (c) Intercept = 4.374 (J/kg)^0.5, M_n = 129,600 g/mol, A_2 = 4.07 x 10^-4 m^3 mol/kg^2 (0.407 cm^3 mol/g^2), A_3 = 5.36 x 10^-3 m^6 mol/kg^3."
            }
        ]
    }

print("Unit 4 authoring complete.")

def build_unit_5():
    return {
        "id": "unit-5",
        "number": 5,
        "title": "Light Scattering & Dilute Solution Viscometry (Zimm Plots, Mark-Houwink)",
        "leadSummary": "Classical electromagnetic Rayleigh scattering theory, concentration fluctuations and refractive index increments (dn/dc), particle scattering factor P(theta) and intraparticle phase interference, Debye Gaussian coil formula and radius of gyration (Rg), double extrapolation Zimm plot formalism for absolute Mw and A2, Dynamic Light Scattering (DLS) and Stokes-Einstein hydrodynamic radius (Rh), capillary viscometry definitions, Huggins and Kraemer extrapolations to intrinsic viscosity [eta], and Mark-Houwink-Sakurada conformational power laws.",
        "simulations": ["sim_poly_zimm_plot_light_scattering"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Classical Rayleigh Scattering Theory: Dipole Radiation, Polarizability & Fluctuations",
                "content": """When an electromagnetic wave passes through a transparent dielectric medium, its oscillating electric field induces periodic polarization in the electron clouds of the constituent molecules. These oscillating electric dipoles act as secondary antennas, reradiating electromagnetic energy in all directions at the identical frequency—a phenomenon known as **elastic light scattering**.

### Rayleigh Scattering by Small Particles ($d \\ll \\lambda / 20$)
Lord Rayleigh derived the intensity of light scattered by an isolated isotropic particle whose dimensions are much smaller than the wavelength of incident radiation ($d < \\lambda / 20 \\approx 20 - 30\\text{ nm}$).
For unpolarized incident light of intensity $I_0$ and vacuum wavelength $\\lambda_0$, the scattered intensity $I_\\theta$ observed at distance $r$ and angle $\\theta$ is:
\\[
I_\\theta = \\frac{I_0 8 \\pi^4 \\alpha^2 (1 + \\cos^2\\theta)}{\\lambda_0^4 r^2}
\\]
where $\\alpha$ is the molecular polarizability and $\\theta$ is the scattering angle relative to the incident beam direction.
The characteristic **Rayleigh ratio** $R_\\theta$ normalizes the scattered intensity for geometric distance and incident beam intensity:
\\[
R_\\theta = \\frac{I_\\theta r^2}{I_0 (1 + \\cos^2\\theta)}
\\]
For pure liquids and solutions, perfect destructive interference would completely cancel the scattered light in all non-forward directions if the molecules were arranged in a perfectly homogeneous or periodic lattice. Scattering in homogeneous liquids arises exclusively from microscopic, spontaneous **thermal fluctuations**.

### Concentration Fluctuations in Polymer Solutions
Albert Einstein (1910) and Peter Debye (1944) showed that excess scattering from a polymer solution over pure solvent ($\Delta R_\\theta = R_{\\theta, \\text{solution}} - R_{\\theta, \\text{solvent}}$) originates from local concentration fluctuations $\\langle (\\delta c)^2 \\rangle$ within microscopic volume elements $\\delta V$.
The mean-square concentration fluctuation is governed by the second derivative of the Gibbs free energy of mixing, which is directly linked to the osmotic pressure gradient:
\\[
\\langle (\\delta c)^2 \\rangle = \\frac{k_B T}{\\left( \\frac{\\partial^2 \\Delta G}{\\partial c^2} \\right)} = \\frac{k_B T c}{\\delta V \\left( \\frac{\\partial \\Pi}{\\partial c} \\right)}
\\]
Because fluctuations in concentration produce proportional fluctuations in dielectric permittivity $\\delta \\epsilon = 2 n (dn/dc) \\delta c$, integrating over volume yields the excess Rayleigh ratio:
\\[
\\Delta R_\\theta = \\frac{2 \\pi^2 n_0^2 (dn/dc)^2 c}{N_A \\lambda_0^4 \\left( \\frac{1}{R T} \\frac{\\partial \\Pi}{\\partial c} \\right)}
\\]
Defining the universal **optical contrast constant** $K$:
\\[
K = \\frac{4 \\pi^2 n_0^2 (dn/dc)^2}{N_A \\lambda_0^4}
\\]
where:
- $n_0$ is the refractive index of the pure solvent.
- $dn/dc$ is the specific refractive index increment of the polymer in that solvent (typically $0.05 - 0.20\\text{ mL/g}$).
- $\\lambda_0$ is the vacuum wavelength of the laser source (e.g., $632.8\\text{ nm}$ for He-Ne).
- $N_A$ is Avogadro's number ($6.022 \\times 10^{23}\\text{ mol}^{-1}$).

Using the osmotic virial equation $\\frac{\\partial \\Pi}{\\partial c} = R T \\left( \\frac{1}{M} + 2 A_2 c + \\dots \\right)$, substitution yields:
\\[
\\frac{K c}{\\Delta R_\\theta} = \\frac{1}{M} + 2 A_2 c
\\]
This landmark equation demonstrates that measuring excess scattered light intensity as a function of polymer concentration provides an absolute, calibration-free determination of **molecular weight** and the **second virial coefficient**."""
            },
            {
                "secNumber": "5.2",
                "title": "Scattering by Large Macromolecules: Particle Scattering Factor and Phase Interference",
                "content": """### Intraparticle Interference
When the physical dimensions of a macromolecule exceed approximately $\\lambda / 20$ (typically $> 25\\text{ nm}$ for visible light), different segments within the *same* macromolecule no longer scatter light in phase.
Consider two scattering segments $i$ and $j$ separated by vector $\\mathbf{r}_{ij}$ within a single polymer chain:
- Rays scattered in the exact forward direction ($\\theta = 0^\\circ$) traverse identical optical path lengths; hence their electric fields interfere constructively without any phase difference.
- At any non-zero scattering angle ($\\theta > 0^\\circ$), the optical path difference $\\Delta s$ between rays scattered from segment $i$ and segment $j$ produces a phase difference $\\phi_{ij} = \\mathbf{q} \\cdot \\mathbf{r}_{ij}$, where $\\mathbf{q}$ is the **scattering vector**:
\\[
q = |\\mathbf{q}| = \\frac{4 \\pi n}{\\lambda_0} \\sin\\left( \\frac{\\theta}{2} \\right)
\\]
Destructive interference between rays scattered from different parts of the coil attenuates the scattered intensity at higher angles.

### The Particle Scattering Factor $P(\\theta)$
To account for this intraparticle phase cancellation, Debye introduced the dimensionless **particle scattering factor** (or form factor) $P(\\theta)$:
\\[
P(\\theta) \\equiv \\frac{\\text{Scattered intensity from large particle at angle }\\theta}{\\text{Scattered intensity without intraparticle interference at angle }\\theta} = \\frac{\\Delta R_\\theta}{\\Delta R_0} \\le 1.0
\\]
For a macromolecule composed of $N$ identical scattering segments:
\\[
P(\\theta) = \\frac{1}{N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\left\\langle \\exp(i \\mathbf{q} \\cdot \\mathbf{r}_{ij}) \\right\\rangle
\\]
Averaging over all random spatial orientations in an isotropic solution:
\\[
\\langle \\exp(i \\mathbf{q} \\cdot \\mathbf{r}_{ij}) \\rangle = \\frac{\\sin(q r_{ij})}{q r_{ij}}
\\]
yielding the general Debye scattering formula:
\\[
P(\\theta) = \\frac{1}{N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\left\\langle \\frac{\\sin(q r_{ij})}{q r_{ij}} \\right\\rangle
\\]
At $\\theta = 0^\\circ$, $q = 0$, so $\\sin(q r_{ij}) / (q r_{ij}) \\to 1$ and $P(0) = 1.0$ identically for all particles regardless of shape or mass."""
            },
            {
                "secNumber": "5.3",
                "title": "The Debye Formula and Radius of Gyration ($R_g$) Expansion at Small Angles",
                "content": """### Guinier Expansion at Small Scattering Vectors ($q R_g < 1$)
At small scattering angles such that $q r_{ij} \\ll 1$, we expand the cardinal sine function in a Taylor series:
\\[
\\frac{\\sin(q r_{ij})}{q r_{ij}} = 1 - \\frac{q^2 r_{ij}^2}{6} + \\frac{q^4 r_{ij}^4}{120} - \\dots
\\]
Substituting this expansion into the Debye double sum:
\\[
P(\\theta) = 1 - \\frac{q^2}{6 N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\langle r_{ij}^2 \\rangle + \\dots
\\]
By definition of the **radius of gyration** $R_g$ for an assembly of $N$ identical mass elements:
\\[
R_g^2 \\equiv \\frac{1}{N} \\sum_{i=1}^N \\langle (\\mathbf{r}_i - \\mathbf{r}_{\\text{cm}})^2 \\rangle = \\frac{1}{2 N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\langle r_{ij}^2 \\rangle
\\]
Therefore:
\\[
\\frac{1}{N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\langle r_{ij}^2 \\rangle = 2 R_g^2
\\]
Substituting into the expansion yields the fundamental **Guinier approximation**:
\\[
P(\\theta) = 1 - \\frac{1}{3} q^2 R_g^2 + \\dots = 1 - \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2} \\sin^2\\left( \\frac{\\theta}{2} \\right) + \\dots
\\]
Remarkably, this low-angle limiting expansion is **completely model-independent**—it holds identically for spheres, rods, random coils, and branched dendrimers!

### The Reciprocal Form
Because light scattering data is analyzed reciprocally, we invert $P(\\theta)$:
\\[
\\frac{1}{P(\\theta)} \\approx 1 + \\frac{1}{3} q^2 R_g^2 = 1 + \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2} \\sin^2\\left( \\frac{\\theta}{2} \\right)
\\]

### Debye Scattering Function for Gaussian Random Coils
For an unperturbed Gaussian flexible polymer coil obeying random walk statistics, Debye integrated the intersegment distance distribution to obtain the closed-form analytical expression:
\\[
P(u) = \\frac{2}{u^2} \\left( e^{-u} - 1 + u \\right)
\\]
where $u = q^2 R_g^2 = \\frac{16 \\pi^2 n^2 R_g^2}{\\lambda_0^2} \\sin^2\\left(\\frac{\\theta}{2}\\right)$.
- When $u \\ll 1$: $P(u) \\approx 1 - u/3$, reproducing the universal Guinier expansion.
- When $u \\gg 1$ (high angle / high $q$): $e^{-u} \\to 0$, so $P(u) \\to 2/u = 2 / (q^2 R_g^2)$. A plot of $q^2 I(q)$ vs $q$ (Kratky plot) plateaus to a constant value, providing an experimental fingerprint of Gaussian coil topology."""
            },
            {
                "secNumber": "5.4",
                "title": "Double Extrapolation Zimm Plot Formalism: $(Kc/R_\\theta)$ vs $(\\sin^2(\\theta/2) + k'c)$",
                "content": """Combining the interparticle osmotic virial expansion with the intraparticle form factor $P(\\theta)$ yields the master equation of static light scattering:
\\[
\\frac{K c}{\\Delta R_\\theta} = \\frac{1}{M_w P(\\theta)} + 2 A_2 c
\\]
Substituting the low-angle expansion $\\frac{1}{P(\\theta)} = 1 + \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2} \\sin^2\\left( \\frac{\\theta}{2} \\right)$ yields:
\\[
\\frac{K c}{\\Delta R_\\theta} = \\frac{1}{M_w} \\left[ 1 + \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2} \\sin^2\\left( \\frac{\\theta}{2} \\right) \\right] + 2 A_2 c
\\]
This equation contains three fundamental macromolecular parameters:
1. **$M_w$**: The weight-average molecular weight.
2. **$R_g$**: The z-average radius of gyration.
3. **$A_2$**: The second virial coefficient.

### The Zimm Double Extrapolation Construction
In 1948, Bruno Zimm devised an elegant graphical methodology to resolve these three parameters simultaneously from experimental data collected at multiple angles $\\theta$ and multiple concentrations $c$.
To separate overlapping curves, Zimm plotted $\\frac{K c}{\\Delta R_\\theta}$ on the y-axis against a composite x-axis:
\\[
X = \\sin^2\\left( \\frac{\\theta}{2} \\right) + k' c
\\]
where $k'$ is an arbitrary plotting scale factor (typically $k' = 100\\text{ to }1000\\text{ cm}^3/\\text{g}$) chosen to space out the concentration lines.

### The Dual Extrapolations:
1. **Extrapolation to Zero Angle ($\\theta \\to 0$)**:
   - For each fixed concentration $c$, the angular data is extrapolated to $\\theta = 0$ (where $\\sin^2(\\theta/2) = 0$).
   - Along this zero-angle envelope line:
   \\[
   \\left( \\frac{K c}{\\Delta R_\\theta} \\right)_{\\theta = 0} = \\frac{1}{M_w} + 2 A_2 c
   \\]
   - The slope of this line with respect to $k' c$ is:
   \\[
   \\text{Slope}_{\\theta=0} = \\frac{2 A_2}{k'} \\implies A_2 = \\frac{k' \\times \\text{Slope}_{\\theta=0}}{2}
   \\]
2. **Extrapolation to Zero Concentration ($c \\to 0$)**:
   - For each fixed angle $\\theta$, the concentration data is extrapolated to $c = 0$.
   - Along this zero-concentration envelope line:
   \\[
   \\left( \\frac{K c}{\\Delta R_\\theta} \\right)_{c = 0} = \\frac{1}{M_w} \\left[ 1 + \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2} \\sin^2\\left( \\frac{\\theta}{2} \\right) \\right]
   \\]
   - The initial slope with respect to $\\sin^2(\\theta/2)$ is:
   \\[
   \\text{Slope}_{c=0} = \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2 M_w} \\implies R_g^2 = \\frac{3 \\lambda_0^2 M_w \\times \\text{Slope}_{c=0}}{16 \\pi^2 n^2}
   \\]
3. **Shared Common Intercept**:
   Both envelope lines converge to the exact same y-intercept at $\\theta = 0, c = 0$:
   \\[
   \\text{Intercept} = \\lim_{c \\to 0, \\theta \\to 0} \\left( \\frac{K c}{\\Delta R_\\theta} \\right) = \\frac{1}{M_w} \\implies M_w = \\frac{1}{\\text{Intercept}}
   \\]
Light scattering yields strictly the **weight-average** molecular weight ($M_w$) because the scattering intensity of an isolated coil is proportional to its mass squared ($I \\propto M^2$), and normalizing by concentration ($c \\propto M$) gives $\\langle M^2 \\rangle / \\langle M \\rangle = M_w$."""
            },
            {
                "secNumber": "5.5",
                "title": "Dynamic Light Scattering (DLS): Autocorrelation, Stokes-Einstein & Hydrodynamic Radius",
                "content": """Whereas Static Light Scattering (SLS) measures time-averaged scattering intensity to yield $M_w, R_g$, and $A_2$, **Dynamic Light Scattering** (DLS)—also known as Photon Correlation Spectroscopy (PCS) or Quasi-Elastic Light Scattering (QELS)—monitors fast microsecond fluctuations in scattered light intensity caused by Brownian diffusion.

### Intensity Fluctuations and the Autocorrelation Function
Macromolecules in solution undergo continuous Brownian motion. As their spatial positions change, the relative phase differences between scattered light rays fluctuate, creating a flickering speckle pattern at the photodetector.
The temporal decay of these fluctuations is quantified by the normalized **second-order intensity autocorrelation function** $g^{(2)}(\\tau)$:
\\[
g^{(2)}(\\tau) = \\frac{\\langle I(t) I(t + \\tau) \\rangle}{\\langle I(t) \\rangle^2}
\\]
where $\\tau$ is the delay time. According to the **Siegert relation**, for Gaussian optical fields:
\\[
g^{(2)}(\\tau) = 1 + \\beta |g^{(1)}(\\tau)|^2
\\]
where $\\beta \\le 1$ is an instrument coherence factor and $g^{(1)}(\\tau)$ is the normalized first-order electric field correlation function.

### The Diffusion Decay Rate $\\Gamma$
For a monodisperse suspension of diffusing particles:
\\[
g^{(1)}(\\tau) = \\exp(-\\Gamma \\tau)
\\]
The decay rate $\\Gamma$ is proportional to the translational diffusion coefficient $D$:
\\[
\\Gamma = D q^2
\\]
where $q = \\frac{4 \\pi n}{\\lambda_0} \\sin(\\theta/2)$.
Measuring $\\Gamma$ at multiple scattering angles confirms Brownian diffusion when a plot of $\\Gamma$ vs $q^2$ passes through the origin with slope $D$.

### The Stokes-Einstein Equation and Hydrodynamic Radius ($R_h$)
From the translational diffusion coefficient at infinite dilution ($D_0$), the hydrodynamic radius $R_h$ is calculated using the **Stokes-Einstein equation**:
\\[
D_0 = \\frac{k_B T}{6 \\pi \\eta_0 R_h} \\implies R_h = \\frac{k_B T}{6 \\pi \\eta_0 D_0}
\\]
where:
- $k_B$ is Boltzmann's constant ($1.38065 \\times 10^{-23}\\text{ J/K}$).
- $\\eta_0$ is the dynamic shear viscosity of pure solvent.
- $R_h$ is the radius of an equivalent hard sphere undergoing the same frictional translation as the solvated macromolecule.

### Geometric Conformation Ratio: $R_g / R_h$
The dimensionless ratio $\\rho = R_g / R_h$ provides profound diagnostic insight into macromolecular topology:
- **Uniform Hard Sphere**: $R_g = \\sqrt{3/5} R_h \\approx 0.775 R_h \\implies R_g / R_h = 0.775$
- **Gaussian Random Coil in $\\Theta$-Solvent**: $R_g / R_h = \\frac{3 \\sqrt{\\pi}}{8} \\approx 1.504$
- **Flexible Coil in Good Solvent**: $R_g / R_h \\approx 1.78$
- **Rigid Rod (needle-like)**: $R_g / R_h > 2.0$ (diverges with aspect ratio as $\\ln(L/d)$)."""
            },
            {
                "secNumber": "5.6",
                "title": "Viscosity of Dilute Polymer Solutions: Relative, Specific, Reduced & Inherent Viscosities",
                "content": """Dilute solution viscometry is the most widely practiced laboratory technique for polymer molecular weight characterization due to its high precision, simplicity, and low equipment cost.

### Capillary Flow and the Hagen-Poiseuille Law
In a capillary viscometer (e.g., Ostwald or Ubbelohde viscometer), liquid drains through a precision glass capillary of radius $R$ and length $L$ under its own hydrostatic head.
According to the Hagen-Poiseuille equation for laminar flow:
\\[
\\eta = \\frac{\\pi R^4 \\Delta P t}{8 V L} = \\frac{\\pi R^4 \\rho g h t}{8 V L}
\\]
where $t$ is the efflux time, $\\rho$ is liquid density, and $V$ is the bulb volume.
For dilute solutions ($c < 10\\text{ g/L}$), the solution density $\\rho$ is essentially indistinguishable from the solvent density $\\rho_0$ ($\\|\\rho - \\rho_0\\| / \\rho_0 < 0.2\\%$). Thus, the ratio of viscosities equals the ratio of efflux times:
\\[
\\frac{\\eta}{\\eta_0} \\approx \\frac{t}{t_0}
\\]

### Standard Viscometric Definitions
1. **Relative Viscosity (Viscosity Ratio)**:
\\[
\\eta_{\\text{rel}} = \\frac{\\eta}{\\eta_0} \\approx \\frac{t}{t_0}
\\]
2. **Specific Viscosity**: The fractional increase in viscosity attributable to the dissolved macromolecular solute:
\\[
\\eta_{\\text{sp}} = \\frac{\\eta - \\eta_0}{\\eta_0} = \\eta_{\\text{rel}} - 1 = \\frac{t - t_0}{t_0}
\\]
3. **Reduced Viscosity (Viscosity Number)**: The specific viscosity normalized per unit solute concentration:
\\[
\\eta_{\\text{red}} = \\frac{\\eta_{\\text{sp}}}{c}
\\]
(Standard units: $\\text{dL/g}$ or $\\text{cm}^3/\\text{g}$ or $\\text{mL/g}$).
4. **Inherent Viscosity (Logarithmic Viscosity Number)**:
\\[
\\eta_{\\text{inh}} = \\frac{\\ln \\eta_{\\text{rel}}}{c}
\\]

### Ubbelohde vs Ostwald Viscometers
The **Ubbelohde suspended-level viscometer** is universally preferred over Ostwald designs because it features an open venting side-arm that isolates the capillary pressure head from total liquid volume in the reservoir. Consequently, serial dilutions can be performed directly inside the viscometer cell without emptying, cleaning, or recalibrating between runs."""
            },
            {
                "secNumber": "5.7",
                "title": "Huggins and Kraemer Equations: Extrapolation to Intrinsic Viscosity $[\\eta]$",
                "content": """### Intrinsic Viscosity $[\\eta]$
As concentration approaches zero, interchain hydrodynamic and thermodynamic interactions vanish. The **intrinsic viscosity** $[\\eta]$ (also called the Limiting Viscosity Number, LVN) represents the isolated hydrodynamic volume increment imparted by a single macromolecule per unit mass:
\\[
[\\eta] \\equiv \\lim_{c \\to 0} \\left( \\frac{\\eta_{\\text{sp}}}{c} \\right) = \\lim_{c \\to 0} \\left( \\frac{\\ln \\eta_{\\text{rel}}}{c} \\right)
\\]
Note that despite being named 'viscosity', $[\\eta]$ has dimensions of **reciprocal density** or specific volume ($[\\eta] \\sim \\text{Volume} / \\text{Mass}$, typically expressed in $\\text{dL/g}$ or $\\text{cm}^3/\\text{g}$).

### The Huggins Equation
Expanding the reduced viscosity $\\eta_{\\text{sp}}/c$ as a Taylor power series in concentration $c$:
\\[
\\frac{\\eta_{\\text{sp}}}{c} = [\\eta] + k_H [\\eta]^2 c
\\]
where $k_H$ is the dimensionless **Huggins constant**.
- In thermodynamically good solvents: polymer coils are well-solvated, and interchain segment collisions are minimal, yielding $k_H \\approx 0.30 - 0.40$.
- In thermodynamically poor solvents (near theta conditions): polymer-polymer attraction increases segment clustering, driving $k_H \\approx 0.50 - 0.80$.
- Values of $k_H > 1.0$ indicate extensive multimolecular aggregation or microgel formation.

### The Kraemer Equation
Expanding the inherent viscosity $\\ln(\\eta_{\\text{rel}})/c$ using the series $\\ln(1 + x) = x - x^2/2 + \\dots$:
\\[
\\ln \\eta_{\\text{rel}} = \\ln(1 + \\eta_{\\text{sp}}) = \\eta_{\\text{sp}} - \\frac{1}{2} \\eta_{\\text{sp}}^2 + \\dots
\\]
Dividing by $c$ and substituting $\\eta_{\\text{sp}} = [\\eta]c + k_H [\\eta]^2 c^2$:
\\[
\\frac{\\ln \\eta_{\\text{rel}}}{c} = [\\eta] - \\left( \\frac{1}{2} - k_H \\right) [\\eta]^2 c = [\\eta] - k_K [\\eta]^2 c
\\]
where $k_K$ is the dimensionless **Kraemer constant**.
Comparing terms reveals the mathematical identity:
\\[
k_H + k_K = \\frac{1}{2} = 0.50
\\]
In practice, experimental data are analyzed by simultaneously plotting both $\\eta_{\\text{sp}}/c$ (upward slope) and $(\\ln \\eta_{\\text{rel}})/c$ (downward slope) on the same graph against concentration $c$. Both lines must extrapolate to the identical y-intercept at $c = 0$, guaranteeing experimental rigor."""
            },
            {
                "secNumber": "5.8",
                "title": "The Mark-Houwink-Sakurada Equation: Scaling Constants & Chain Conformation",
                "content": """### The Mark-Houwink-Sakurada (MHS) Empirical Relation
In 1938–1940, Herman Mark, Roelof Houwink, and Ichiro Sakurada established the empirical power-law relationship between intrinsic viscosity $[\\eta]$ and molecular weight:
\\[
[\\eta] = K M_v^a
\\]
where:
- $K$ is the Mark-Houwink pre-exponential constant (typically $10^{-4} - 10^{-2}\\text{ dL/g}$).
- $a$ is the Mark-Houwink conformational exponent (dimensionless).
- $M_v$ is the **viscosity-average molecular weight**.

Both $K$ and $a$ are specific to a given polymer-solvent-temperature triplet and are tabulated in chemical handbooks.
Taking the natural logarithm yields a linear calibration equation:
\\[
\\ln [\\eta] = \\ln K + a \\ln M_v
\\]

### Physical Origin: The Flory-Fox Hydrodynamic Equation
Paul Flory and Thomas Fox demonstrated that the intrinsic viscosity of a flexible polymer coil is proportional to its hydrodynamic volume per unit mass:
\\[
[\\eta] = \\Phi_0 \\frac{\\langle R^2 \\rangle^{3/2}}{M}
\\]
where $\\Phi_0$ is the universal Flory hydrodynamic constant ($\\Phi_0 \\approx 2.5 \\times 10^{23}\\text{ mol}^{-1}$ when $[\\eta]$ is in $\\text{cm}^3/\\text{g}$), and $\\langle R^2 \\rangle^{1/2}$ is the root-mean-square end-to-end distance.
Expressing the end-to-end distance as $\\langle R^2 \\rangle = \\alpha^2 \\langle R_0^2 \\rangle$:
\\[
[\\eta] = \\Phi_0 \\left( \\frac{\\langle R_0^2 \\rangle}{M} \\right)^{3/2} M^{1/2} \\alpha^3 = K_\\theta M^{1/2} \\alpha^3
\\]

### Physical Meaning of the Mark-Houwink Exponent $a$
The value of the exponent $a$ reveals the three-dimensional hydrodynamic conformation of the macromolecule in that solvent:
1. **$a = 0$ (Hard Solid Spheres)**:
   - Einstein's viscosity law: $\\eta_{\\text{sp}} = 2.5 \\phi = 2.5 c \\bar{v} \\implies [\\eta] = 2.5 \\bar{v} = \\text{constant}$ (independent of $M$).
   - Examples: Globular proteins (myoglobin, hemoglobin), hyperbranched dendrimers, compact latex nanospheres.
2. **$a = 0.50$ (Random Coil in $\\Theta$-Solvent)**:
   - The coil is unperturbed ($\alpha = 1$). $[\\eta] = K_\\theta M^{1/2}$.
   - Flory theta conditions (e.g., Polystyrene in cyclohexane at $34.5^\\circ\\text{C}$).
3. **$a = 0.65 - 0.80$ (Flexible Random Coil in Good Solvent)**:
   - The coil is thermodynamically swollen by excluded volume ($\alpha \\propto M^{0.1}$).
   - Examples: Polystyrene in toluene ($a = 0.72$), PMMA in chloroform ($a = 0.76$).
4. **$a = 1.0 - 1.2$ (Semi-Rigid Wormlike Chain / Extended Helix)**:
   - Poly(gamma-benzyl-L-glutamate) in helicogenic solvents, sodium hyaluronate.
5. **$a = 1.7 - 2.0$ (Rigid Inflexible Rod)**:
   - Stiff cylinders rotating in shear flow.
   - Examples: Native double-stranded DNA, poly(p-phenylene terephthalamide) (Kevlar) in concentrated $\\text{H}_2\\text{SO}_4$, tobacco mosaic virus."""
            }
        ],
        "problems": [
            {
                "id": "prob-5-1",
                "difficulty": "foundation",
                "title": "Efflux Time Viscometry, Huggins and Kraemer Extrapolation to $[\\eta]$",
                "statement": """Efflux times are measured for dilute solutions of poly(methyl methacrylate) (PMMA) in acetone at $T = 25.0^\\circ\\text{C}$ using an Ubbelohde capillary viscometer.
The pure acetone solvent has an efflux time of $t_0 = 100.0\\text{ s}$.
The following solution efflux times are recorded:
- $c = 0.200\\text{ g/dL}: t = 113.8\\text{ s}$
- $c = 0.400\\text{ g/dL}: t = 129.2\\text{ s}$
- $c = 0.600\\text{ g/dL}: t = 146.4\\text{ s}$
- $c = 0.800\\text{ g/dL}: t = 165.6\\text{ s}$

(a) Calculate $\\eta_{\\text{rel}}, \\eta_{\\text{sp}}, \\eta_{\\text{sp}}/c$, and $(\\ln \\eta_{\\text{rel}})/c$ for each concentration.
(b) Perform simultaneous Huggins and Kraemer linear regressions to determine the intrinsic viscosity $[\\eta]$ (in $\\text{dL/g}$).
(c) Calculate the Huggins constant $k_H$ and Kraemer constant $k_K$, and verify whether $k_H + k_K \\approx 0.50$.""",
                "solution": """### Step 1: Compute Viscosity Ratios and Functions
Given $t_0 = 100.0\\text{ s}$:
1. $c = 0.200\\text{ g/dL}$:
   - $\\eta_{\\text{rel}} = 113.8 / 100.0 = 1.1380$
   - $\\eta_{\\text{sp}} = 1.1380 - 1 = 0.1380$
   - $\\eta_{\\text{sp}}/c = 0.1380 / 0.200 = 0.6900\\text{ dL/g}$
   - $(\\ln \\eta_{\\text{rel}})/c = \\ln(1.1380) / 0.200 = 0.12927 / 0.200 = 0.6464\\text{ dL/g}$
2. $c = 0.400\\text{ g/dL}$:
   - $\\eta_{\\text{rel}} = 129.2 / 100.0 = 1.2920$
   - $\\eta_{\\text{sp}} = 1.2920 - 1 = 0.2920$
   - $\\eta_{\\text{sp}}/c = 0.2920 / 0.400 = 0.7300\\text{ dL/g}$
   - $(\\ln \\eta_{\\text{rel}})/c = \\ln(1.2920) / 0.400 = 0.25622 / 0.400 = 0.6406\\text{ dL/g}$
3. $c = 0.600\\text{ g/dL}$:
   - $\\eta_{\\text{rel}} = 146.4 / 100.0 = 1.4640$
   - $\\eta_{\\text{sp}} = 1.4640 - 1 = 0.4640$
   - $\\eta_{\\text{sp}}/c = 0.4640 / 0.600 = 0.7733\\text{ dL/g}$
   - $(\\ln \\eta_{\\text{rel}})/c = \\ln(1.4640) / 0.600 = 0.38118 / 0.600 = 0.6353\\text{ dL/g}$
4. $c = 0.800\\text{ g/dL}$:
   - $\\eta_{\\text{rel}} = 165.6 / 100.0 = 1.6560$
   - $\\eta_{\\text{sp}} = 1.6560 - 1 = 0.6560$
   - $\\eta_{\\text{sp}}/c = 0.6560 / 0.800 = 0.8200\\text{ dL/g}$
   - $(\\ln \\eta_{\\text{rel}})/c = \\ln(1.6560) / 0.800 = 0.50442 / 0.800 = 0.6305\\text{ dL/g}$

### Step 2: Huggins Linear Regression ($\\eta_{\\text{sp}}/c = [\\eta] + k_H [\\eta]^2 c$)
Plot $\\eta_{\\text{sp}}/c$ vs $c$:
- Slope:
\\[
\\text{Slope}_H = \\frac{0.8200 - 0.6900}{0.800 - 0.200} = \\frac{0.1300}{0.600} = 0.2167\\text{ (dL/g)}^2
\\]
- Intercept:
\\[
[\\eta]_H = 0.6900 - (0.2167)(0.200) = 0.6900 - 0.0433 = 0.6467\\text{ dL/g}
\\]

### Step 3: Kraemer Linear Regression ($(\\ln \\eta_{\\text{rel}})/c = [\\eta] - k_K [\\eta]^2 c$)
Plot $(\\ln \\eta_{\\text{rel}})/c$ vs $c$:
- Slope:
\\[
\\text{Slope}_K = \\frac{0.6305 - 0.6464}{0.800 - 0.200} = \\frac{-0.0159}{0.600} = -0.0265\\text{ (dL/g)}^2
\\]
- Intercept:
\\[
[\\eta]_K = 0.6464 - (-0.0265)(0.200) = 0.6464 + 0.0053 = 0.6517\\text{ dL/g}
\\]
Averaging the two intercepts gives:
\\[
[\\eta] = \\frac{0.6467 + 0.6517}{2} = 0.649\\text{ dL/g}
\\]

### Step 4: Huggins and Kraemer Constants
\\[
k_H = \\frac{\\text{Slope}_H}{[\\eta]^2} = \\frac{0.2167}{(0.649)^2} = \\frac{0.2167}{0.4212} = 0.514
\\]
\\[
k_K = \\frac{-\\text{Slope}_K}{[\\eta]^2} = \\frac{0.0265}{0.4212} = 0.063
\\]
Sum of constants:
\\[
k_H + k_K = 0.514 + 0.063 = 0.577 \\approx 0.50
\\]""",
                "answer": "(a) Tabulated values computed; (b) [eta] = 0.649 dL/g; (c) k_H = 0.514, k_K = 0.063, k_H + k_K = 0.577 (confirms identity within experimental uncertainty)."
            },
            {
                "id": "prob-5-2",
                "difficulty": "foundation",
                "title": "Mark-Houwink-Sakurada Molecular Weight Calculation",
                "statement": """An unknown sample of polystyrene is dissolved in two different solvents and measured at $T = 25.0^\\circ\\text{C}$:
1. In toluene (a thermodynamically good solvent):
   $K_1 = 1.10 \\times 10^{-4}\\text{ dL/g}$, $a_1 = 0.725$.
   The measured intrinsic viscosity is $[\\eta]_1 = 1.485\\text{ dL/g}$.
2. In cyclohexane at its theta temperature ($T = 34.5^\\circ\\text{C}$):
   $K_\\theta = 8.46 \\times 10^{-4}\\text{ dL/g}$, $a_\\theta = 0.500$.

(a) Calculate the viscosity-average molecular weight $M_v$ of the polystyrene from the toluene measurement.
(b) Predict the intrinsic viscosity $[\\eta]_\\theta$ of this identical sample in cyclohexane at the theta temperature.
(c) Calculate the chain expansion factor $\\alpha_\\eta = ([\\eta]_1 / [\\eta]_\\theta)^{1/3}$ resulting from solvent swelling in toluene.""",
                "solution": """### Step 1: Calculate $M_v$ from Toluene Data
Applying the Mark-Houwink equation:
\\[
[\\eta]_1 = K_1 M_v^{a_1} \\implies M_v^{a_1} = \\frac{[\\eta]_1}{K_1}
\\]
Given $[\\eta]_1 = 1.485\\text{ dL/g}$ and $K_1 = 1.10 \\times 10^{-4}\\text{ dL/g}$:
\\[
M_v^{0.725} = \\frac{1.485}{1.10 \\times 10^{-4}} = 13,500
\\]
Taking logarithms:
\\[
0.725 \\ln M_v = \\ln(13,500) = 9.5104 \\implies \\ln M_v = \\frac{9.5104}{0.725} = 13.1179
\\]
\\[
M_v = e^{13.1179} = 497,800\\text{ g/mol} \\approx 498,000\\text{ g/mol}
\\]

### Step 2: Predict $[\\eta]_\\theta$ in Cyclohexane at $\\Theta$ Temperature
In cyclohexane at $\\Theta = 34.5^\\circ\\text{C}$, $a_\\theta = 0.500$:
\\[
[\\eta]_\\theta = K_\\theta M_v^{0.500} = (8.46 \\times 10^{-4}) \\sqrt{497,800}
\\]
\\[
\\sqrt{497,800} = 705.55
\\]
\\[
[\\eta]_\\theta = (8.46 \\times 10^{-4})(705.55) = 0.5969\\text{ dL/g} \\approx 0.597\\text{ dL/g}
\\]

### Step 3: Calculate Chain Expansion Factor $\\alpha_\\eta$
According to the Flory-Fox equation:
\\[
[\\eta] = \\Phi_0 \\frac{\\langle R^2 \\rangle^{3/2}}{M} = \\Phi_0 \\frac{(\\alpha \\langle R_0^2 \\rangle^{1/2})^3}{M} = [\\eta]_\\theta \\alpha_\\eta^3
\\]
Therefore:
\\[
\\alpha_\\eta = \\left( \\frac{[\\eta]_1}{[\\eta]_\\theta} \\right)^{1/3} = \\left( \\frac{1.485}{0.5969} \\right)^{1/3} = (2.4878)^{1/3} = 1.355
\\]
The polymer coil dimensions expand by $35.5\\%$ in toluene compared to its unperturbed theta state due to excluded volume interactions.""",
                "answer": "(a) M_v = 498,000 g/mol; (b) [eta]_theta = 0.597 dL/g; (c) alpha_eta = 1.355 (35.5% expansion)."
            },
            {
                "id": "prob-5-3",
                "difficulty": "foundation",
                "title": "Rayleigh Scattering Ratio and Optical Contrast Constant Determination",
                "statement": """A laser light scattering apparatus employs a linearly polarized He-Ne laser operating at $\\lambda_0 = 632.8\\text{ nm}$.
A calibration standard of pure benzene at $T = 25.0^\\circ\\text{C}$ exhibits an absolute Rayleigh ratio of $R_{\\text{benzene}}(90^\\circ) = 8.51 \\times 10^{-6}\\text{ cm}^{-1}$ with refractive index $n_{\\text{benzene}} = 1.498$.
A solution of poly(vinyl acetate) (PVAc) in benzene has a refractive index increment of $dn/dc = 0.052\\text{ mL/g}$.
(a) Calculate the optical contrast constant $K$ for PVAc in benzene at this laser wavelength.
(b) At a scattering angle of $\\theta = 90^\\circ$, a PVAc solution of concentration $c = 5.00\\text{ g/L}$ produces a scattered intensity that is $2.40$ times that of pure benzene in the same cell.
Calculate the excess Rayleigh ratio $\\Delta R_{90}$ of the polymer solution.
(c) Neglecting particle form factor corrections ($P(90^\\circ) \\approx 1$), estimate the apparent molecular weight $M_{\\text{app}}$ if $2 A_2 c \\ll 1/M$.""",
                "solution": """### Step 1: Calculate Optical Contrast Constant $K$
The optical constant for vertically polarized incident light is:
\\[
K = \\frac{4 \\pi^2 n_0^2 (dn/dc)^2}{N_A \\lambda_0^4}
\\]
Given:
- $n_0 = 1.498 \\implies n_0^2 = 2.2440$
- $dn/dc = 0.052\\text{ mL/g} = 0.052\\text{ cm}^3/\\text{g} \\implies (dn/dc)^2 = 2.704 \\times 10^{-3}\\text{ cm}^6/\\text{g}^2$
- $N_A = 6.02214 \\times 10^{23}\\text{ mol}^{-1}$
- $\\lambda_0 = 632.8\\text{ nm} = 6.328 \\times 10^{-5}\\text{ cm} \\implies \\lambda_0^4 = 1.6035 \\times 10^{-17}\\text{ cm}^4$

Substitute values:
\\[
\\text{Numerator} = 4 \\pi^2 (2.2440)(2.704 \\times 10^{-3}) = 39.4784 \\times 6.0678 \\times 10^{-3} = 0.23955\\text{ cm}^6/\\text{g}^2
\\]
\\[
\\text{Denominator} = (6.02214 \\times 10^{23})(1.6035 \\times 10^{-17}) = 9.6565 \\times 10^6\\text{ cm}^4/\\text{mol}
\\]
\\[
K = \\frac{0.23955}{9.6565 \\times 10^6} = 2.4807 \\times 10^{-8}\\text{ mol cm}^2/\\text{g}^2
\\]

### Step 2: Calculate Excess Rayleigh Ratio $\\Delta R_{90}$
The measured total intensity is $I_{\\text{solution}} = 2.40 I_{\\text{benzene}}$.
The excess intensity due to the polymer solute is:
\\[
I_{\\text{polymer}} = I_{\\text{solution}} - I_{\\text{benzene}} = (2.40 - 1.00) I_{\\text{benzene}} = 1.40 I_{\\text{benzene}}
\\]
The excess Rayleigh ratio is:
\\[
\\Delta R_{90} = 1.40 \\times R_{\\text{benzene}} = 1.40 \\times (8.51 \\times 10^{-6}\\text{ cm}^{-1}) = 1.1914 \\times 10^{-5}\\text{ cm}^{-1}
\\]

### Step 3: Estimate Apparent Molecular Weight $M_{\\text{app}}$
Given $c = 5.00\\text{ g/L} = 5.00 \\times 10^{-3}\\text{ g/cm}^3$:
\\[
\\frac{K c}{\\Delta R_{90}} = \\frac{1}{M_{\\text{app}}}
\\]
\\[
K c = (2.4807 \\times 10^{-8}\\text{ mol cm}^2/\\text{g}^2)(5.00 \\times 10^{-3}\\text{ g/cm}^3) = 1.2404 \\times 10^{-10}\\text{ mol/cm}
\\]
\\[
\\frac{1}{M_{\\text{app}}} = \\frac{1.2404 \\times 10^{-10}\\text{ mol/cm}}{1.1914 \\times 10^{-5}\\text{ cm}^{-1}} = 1.0411 \\times 10^{-5}\\text{ mol/g}
\\]
\\[
M_{\\text{app}} = \\frac{1}{1.0411 \\times 10^{-5}} = 96,050\\text{ g/mol} \\approx 96,100\\text{ g/mol}
\\]""",
                "answer": "(a) K = 2.481 x 10^-8 mol cm^2/g^2; (b) Delta R_90 = 1.191 x 10^-5 cm^-1; (c) M_app = 96,100 g/mol."
            },
            {
                "id": "prob-5-4",
                "difficulty": "advanced",
                "title": "Comprehensive Zimm Plot Analysis for Polystyrene in Toluene",
                "statement": """A multi-angle laser light scattering (MALLS) study is carried out on a high-molecular-weight polystyrene sample in toluene ($n_0 = 1.496, dn/dc = 0.110\\text{ mL/g}, \\lambda_0 = 632.8\\text{ nm}, K = 1.112 \\times 10^{-7}\\text{ mol cm}^2/\\text{g}^2$).
Data is processed using the Zimm coordinate $X = \\sin^2(\\theta/2) + k' c$ with scale factor $k' = 1000\\text{ cm}^3/\\text{g}$.
The double extrapolation yields the following linear envelope equations:
1. **Zero-Angle Extrapolation Line ($\\theta \\to 0$, plotting against $k' c$)**:
   \\[
   \\left( \\frac{K c}{\\Delta R_\\theta} \\right)_{\\theta = 0} = 1.250 \\times 10^{-6} + 9.600 \\times 10^{-10} (k' c)
   \\]
   (where $c$ is in $\\text{g/cm}^3$).
2. **Zero-Concentration Extrapolation Line ($c \\to 0$, plotting against $\\sin^2(\\theta/2)$)**:
   \\[
   \\left( \\frac{K c}{\\Delta R_\\theta} \\right)_{c = 0} = 1.250 \\times 10^{-6} + 3.840 \\times 10^{-6} \\sin^2\\left( \\frac{\\theta}{2} \\right)
   \\]

(a) Calculate the weight-average molecular weight $M_w$ of the polystyrene sample.
(b) Calculate the second virial coefficient $A_2$ in $\\text{mol cm}^3/\\text{g}^2$.
(c) Calculate the root-mean-square radius of gyration $\\langle R_g^2 \\rangle^{1/2}$ in nanometers.""",
                "solution": """### Step 1: Calculate $M_w$
The shared intercept at $\\theta = 0, c = 0$ is:
\\[
\\text{Intercept} = \\frac{1}{M_w} = 1.250 \\times 10^{-6}\\text{ mol/g}
\\]
\\[
M_w = \\frac{1}{1.250 \\times 10^{-6}} = 800,000\\text{ g/mol}
\\]

### Step 2: Calculate Second Virial Coefficient $A_2$
Along the $\\theta = 0$ envelope line:
\\[
\\left( \\frac{K c}{\\Delta R_\\theta} \\right)_{\\theta = 0} = \\frac{1}{M_w} + 2 A_2 c = \\frac{1}{M_w} + \\left( \\frac{2 A_2}{k'} \\right) (k' c)
\\]
From the given regression:
\\[
\\text{Slope}_{\\theta=0} = \\frac{2 A_2}{k'} = 9.600 \\times 10^{-10}\\text{ mol/g}
\\]
Given $k' = 1000\\text{ cm}^3/\\text{g}$:
\\[
2 A_2 = k' \\times (9.600 \\times 10^{-10}) = 1000 \\times (9.600 \\times 10^{-10}) = 9.600 \\times 10^{-7}\\text{ mol cm}^3/\\text{g}^2
\\]
\\[
A_2 = \\frac{9.600 \\times 10^{-7}}{2} = 4.800 \\times 10^{-4}\\text{ mol cm}^3/\\text{g}^2
\\]
The positive value of $A_2$ confirms that toluene is an excellent solvent for polystyrene.

### Step 3: Calculate Radius of Gyration $R_g$
Along the $c = 0$ envelope line:
\\[
\\left( \\frac{K c}{\\Delta R_\\theta} \\right)_{c = 0} = \\frac{1}{M_w} \\left[ 1 + \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2} \\sin^2\\left(\\frac{\\theta}{2}\\right) \\right] = \\frac{1}{M_w} + \\left( \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2 M_w} \\right) \\sin^2\\left(\\frac{\\theta}{2}\\right)
\\]
The slope with respect to $\\sin^2(\\theta/2)$ is:
\\[
\\text{Slope}_{c=0} = \\frac{16 \\pi^2 n^2 R_g^2}{3 \\lambda_0^2 M_w} = 3.840 \\times 10^{-6}\\text{ mol/g}
\\]
Rearranging for $R_g^2$:
\\[
R_g^2 = \\frac{3 \\lambda_0^2 M_w \\times \\text{Slope}_{c=0}}{16 \\pi^2 n^2}
\\]
Given:
- $\\lambda_0 = 632.8\\text{ nm} = 6.328 \\times 10^{-5}\\text{ cm} \\implies \\lambda_0^2 = 4.0044 \\times 10^{-9}\\text{ cm}^2$
- $M_w = 800,000\\text{ g/mol}$
- $n = 1.496 \\implies n^2 = 2.2380$
- $16 \\pi^2 n^2 = 16 \\pi^2 (2.2380) = 353.41$

Calculate numerator:
\\[
\\text{Numerator} = 3 (4.0044 \\times 10^{-9}\\text{ cm}^2)(800,000\\text{ g/mol})(3.840 \\times 10^{-6}\\text{ mol/g})
\\]
\\[
\\text{Numerator} = 3 \\times (4.0044 \\times 10^{-9}) \\times 3.072 = 3.6897 \\times 10^{-8}\\text{ cm}^2
\\]
Calculate $R_g^2$:
\\[
R_g^2 = \\frac{3.6897 \\times 10^{-8}\\text{ cm}^2}{353.41} = 1.0440 \\times 10^{-10}\\text{ cm}^2
\\]
Taking the square root:
\\[
R_g = \\sqrt{1.0440 \\times 10^{-10}\\text{ cm}^2} = 1.0218 \\times 10^{-5}\\text{ cm} = 102.2\\text{ nm}
\\]""",
                "answer": "(a) M_w = 800,000 g/mol; (b) A_2 = 4.80 x 10^-4 mol cm^3/g^2; (c) R_g = 102.2 nm."
            },
            {
                "id": "prob-5-5",
                "difficulty": "advanced",
                "title": "Mark-Houwink Exponent Scaling and Solvent Thermodynamic Quality",
                "statement": """Three fractions of an unknown monodisperse polymer are characterized by light scattering and viscometry in two different solvents at $25.0^\\circ\\text{C}$:

| Fraction | $M_w\\text{ (g/mol)}$ | $[\\eta]\\text{ in Solvent A (dL/g)}$ | $[\\eta]\\text{ in Solvent B (dL/g)}$ |
|:---:|:---:|:---:|:---:|
| 1 | 50,000 | 0.280 | 0.179 |
| 2 | 200,000 | 0.890 | 0.358 |
| 3 | 800,000 | 2.825 | 0.716 |

(a) Determine the Mark-Houwink parameters ($K$ and $a$) for both solvent systems by linear regression of $\\ln [\\eta]$ vs $\\ln M_w$.
(b) Identify the thermodynamic state of the polymer in each solvent (theta solvent vs good solvent) based on the exponent $a$.
(c) Calculate the unperturbed dimension parameter $K_\\theta = \\Phi_0 (\\langle R_0^2 \\rangle / M)^{3/2}$ from the theta solvent data.
(d) Given the universal constant $\\Phi_0 = 2.80 \\times 10^{23}\\text{ mol}^{-1}$ (for $[\\eta]$ in $\\text{cm}^3/\\text{g}$), calculate the unperturbed characteristic ratio $C_\\infty$ if the monomer repeating unit is styrene ($M_0 = 104.15\\text{ g/mol}, l = 0.154\\text{ nm}$).""",
                "solution": """### Step 1: Mark-Houwink Fit for Solvent A
Calculate $\\ln M_w$ and $\\ln [\\eta]$:
- Fraction 1: $\\ln(50,000) = 10.8198, \\ln(0.280) = -1.2730$
- Fraction 2: $\\ln(200,000) = 12.2061, \\ln(0.890) = -0.1165$
- Fraction 3: $\\ln(800,000) = 13.5924, \\ln(2.825) = 1.0385$

Calculate slope $a_A$:
\\[
a_A = \\frac{1.0385 - (-1.2730)}{13.5924 - 10.8198} = \\frac{2.3115}{2.7726} = 0.8337 \\approx 0.834
\\]
Calculate intercept $\\ln K_A$:
\\[
\\ln K_A = -1.2730 - (0.8337)(10.8198) = -1.2730 - 9.0205 = -10.2935
\\]
\\[
K_A = e^{-10.2935} = 3.385 \\times 10^{-5}\\text{ dL/g}
\\]

### Step 2: Mark-Houwink Fit for Solvent B
Calculate $\\ln [\\eta]$ for Solvent B:
- Fraction 1: $\\ln(0.179) = -1.7204$
- Fraction 2: $\\ln(0.358) = -1.0272$
- Fraction 3: $\\ln(0.716) = -0.3341$

Calculate slope $a_B$:
\\[
a_B = \\frac{-0.3341 - (-1.7204)}{13.5924 - 10.8198} = \\frac{1.3863}{2.7726} = 0.5000 = 0.500
\\]
Calculate intercept $\\ln K_B$:
\\[
\\ln K_B = -1.7204 - (0.5000)(10.8198) = -1.7204 - 5.4099 = -7.1303
\\]
\\[
K_B = e^{-7.1303} = 8.005 \\times 10^{-4}\\text{ dL/g} = K_\\theta
\\]

### Step 3: Thermodynamic Characterization
- **Solvent B ($a = 0.500$)**: Exponent is identically $0.50$, proving that Solvent B is a **Flory theta solvent** at $25.0^\\circ\\text{C}$ where excluded volume vanishes and chains adopt unperturbed Gaussian random coil conformations.
- **Solvent A ($a = 0.834$)**: Exponent is $> 0.50$, indicating a highly solvated, **thermodynamically good solvent** with substantial excluded volume coil swelling.

### Step 4: Unperturbed Dimension and Characteristic Ratio $C_\\infty$
Convert $K_\\theta$ to units of $\\text{cm}^3/(\\text{g} \\cdot (\\text{g/mol})^{1/2})$:
$1\\text{ dL/g} = 100\\text{ cm}^3/\\text{g}$:
\\[
K_\\theta = (8.005 \\times 10^{-4}\\text{ dL/g}) \\times 100\\text{ cm}^3/\\text{dL} = 0.08005\\text{ cm}^3 \\text{g}^{-1} (\\text{g/mol})^{-1/2}
\\]
According to the Flory-Fox equation:
\\[
K_\\theta = \\Phi_0 \\left( \\frac{\\langle R_0^2 \\rangle}{M} \\right)^{3/2} \\implies \\frac{\\langle R_0^2 \\rangle}{M} = \\left( \\frac{K_\\theta}{\\Phi_0} \\right)^{2/3}
\\]
Given $\\Phi_0 = 2.80 \\times 10^{23}\\text{ mol}^{-1}$:
\\[
\\frac{K_\\theta}{\\Phi_0} = \\frac{0.08005}{2.80 \\times 10^{23}} = 2.8589 \\times 10^{-25}\\text{ cm}^3/\\text{g}^{3/2}
\\]
\\[
\\frac{\\langle R_0^2 \\rangle}{M} = (2.8589 \\times 10^{-25})^{2/3} = 4.341 \\times 10^{-17}\\text{ cm}^2\\text{ mol/g} = 0.04341\\text{ nm}^2\\text{ mol/g}
\\]
For a vinyl polymer ($-\\text{CH}_2-\\text{CHX}-$, 2 backbone bonds per repeat unit):
Number of backbone bonds per unit mass:
\\[
\\frac{n}{M} = \\frac{2}{M_0} = \\frac{2}{104.15\\text{ g/mol}} = 0.019203\\text{ mol/g}
\\]
The freely jointed unperturbed dimension is:
\\[
\\langle R_0^2 \\rangle = C_\\infty n l^2 \\implies \\frac{\\langle R_0^2 \\rangle}{M} = C_\\infty \\left( \\frac{n}{M} \\right) l^2
\\]
Given $l = 0.154\\text{ nm} \\implies l^2 = 0.023716\\text{ nm}^2$:
\\[
C_\\infty = \\frac{\\langle R_0^2 \\rangle / M}{(n/M) l^2} = \\frac{0.04341\\text{ nm}^2\\text{ mol/g}}{(0.019203\\text{ mol/g})(0.023716\\text{ nm}^2)} = \\frac{0.04341}{4.5542 \\times 10^{-4}} = 9.53
\\]
$C_\\infty = 9.5$ matches typical literature values for polystyrene ($C_\\infty \\approx 9.5 - 10.0$), reflecting significant steric hindrance from pendant phenyl rings.""",
                "answer": "(a) Solvent A: a = 0.834, K = 3.39 x 10^-5 dL/g; Solvent B: a = 0.500, K = 8.01 x 10^-4 dL/g; (b) Solvent B is a Flory theta solvent (a = 0.50); Solvent A is a thermodynamically good solvent; (c) <R_0^2>/M = 0.0434 nm^2 mol/g; (d) C_infinity = 9.53."
            },
            {
                "id": "prob-5-6",
                "difficulty": "advanced",
                "title": "Dynamic Light Scattering Diffusion and Stokes-Einstein Hydrodynamic Radius",
                "statement": """A dynamic light scattering experiment is performed on a monodisperse aqueous dispersion of poly(N-isopropylacrylamide) (PNIPAM) microgels at $T = 20.0^\\circ\\text{C}$ ($293.15\\text{ K}$) using a laser of $\\lambda_0 = 532.0\\text{ nm}$.
The refractive index of water is $n = 1.333$, and its dynamic shear viscosity is $\\eta_0 = 1.002 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$.
The measurement is performed at a scattering angle of $\\theta = 90.0^\\circ$.
The normalized intensity autocorrelation function $g^{(2)}(\\tau)$ yields a clean single-exponential decay:
\\[
g^{(2)}(\\tau) - 1 = \\beta \\exp(-2 \\Gamma \\tau)
\\]
where the measured intensity decay rate is $2 \\Gamma = 4,240\\text{ s}^{-1}$ (electric field decay rate $\\Gamma = 2,120\\text{ s}^{-1}$).
(a) Calculate the scattering vector magnitude $q$ in $\\text{m}^{-1}$.
(b) Determine the translational diffusion coefficient $D$ of the PNIPAM microgels.
(c) Calculate the hydrodynamic radius $R_h$ using the Stokes-Einstein equation.
(d) In a separate static light scattering experiment, the radius of gyration is measured to be $R_g = 62.0\\text{ nm}$.
Compute the conformational ratio $\\rho = R_g / R_h$ and interpret its physical meaning regarding internal microgel density.""",
                "solution": """### Step 1: Calculate Scattering Vector $q$
\\[
q = \\frac{4 \\pi n}{\\lambda_0} \\sin\\left( \\frac{\\theta}{2} \\right)
\\]
Given:
- $n = 1.333$
- $\\lambda_0 = 532.0\\text{ nm} = 5.320 \\times 10^{-7}\\text{ m}$
- $\\theta = 90.0^\\circ \\implies \\theta/2 = 45.0^\\circ \\implies \\sin(45.0^\\circ) = \\frac{\\sqrt{2}}{2} = 0.7071$

\\[
q = \\frac{4 \\pi (1.333)}{5.320 \\times 10^{-7}\\text{ m}} \\times 0.7071 = \\frac{16.751}{5.320 \\times 10^{-7}} \\times 0.7071 = 3.1487 \\times 10^7 \\times 0.7071 = 2.2264 \\times 10^7\\text{ m}^{-1}
\\]
\\[
q^2 = (2.2264 \\times 10^7)^2 = 4.957 \\times 10^{14}\\text{ m}^{-2}
\\]

### Step 2: Calculate Translational Diffusion Coefficient $D$
The electric field decay rate is $\\Gamma = 2,120\\text{ s}^{-1}$.
Since $\\Gamma = D q^2$:
\\[
D = \\frac{\\Gamma}{q^2} = \\frac{2,120\\text{ s}^{-1}}{4.957 \\times 10^{14}\\text{ m}^{-2}} = 4.277 \\times 10^{-12}\\text{ m}^2\\text{/s}
\\]

### Step 3: Calculate Hydrodynamic Radius $R_h$
From the Stokes-Einstein equation:
\\[
R_h = \\frac{k_B T}{6 \\pi \\eta_0 D}
\\]
Given:
- $k_B = 1.38065 \\times 10^{-23}\\text{ J/K}$
- $T = 293.15\\text{ K}$
- $\\eta_0 = 1.002 \\times 10^{-3}\\text{ Pa s} = 1.002 \\times 10^{-3}\\text{ kg/(m s)}$
- $D = 4.277 \\times 10^{-12}\\text{ m}^2\\text{/s}$

Calculate numerator:
\\[
k_B T = (1.38065 \\times 10^{-23})(293.15) = 4.0474 \\times 10^{-21}\\text{ J}
\\]
Calculate denominator:
\\[
6 \\pi \\eta_0 D = 6 \\pi (1.002 \\times 10^{-3})(4.277 \\times 10^{-12}) = 1.8887 \\times 10^{-2} \\times 4.277 \\times 10^{-12} = 8.078 \\times 10^{-14}\\text{ N s/m}
\\]
Calculate $R_h$:
\\[
R_h = \\frac{4.0474 \\times 10^{-21}}{8.078 \\times 10^{-14}} = 5.010 \\times 10^{-8}\\text{ m} = 50.1\\text{ nm}
\\]

### Step 4: Conformational Ratio $\\rho = R_g / R_h$
\\[
\\rho = \\frac{R_g}{R_h} = \\frac{62.0\\text{ nm}}{50.1\\text{ nm}} = 1.238 \\approx 1.24
\\]
Interpretation:
- For a uniform solid hard sphere, $\\rho = \\sqrt{3/5} \\approx 0.775$.
- For a soft microgel particle with a dense cross-linked core and a fuzzy, dangling polymer brush corona, hydrodynamic shear extends beyond the visual mass boundary, typically yielding $\\rho \\approx 1.0 - 1.3$. Here $\\rho = 1.24$ reflects swollen cross-linked microgel architecture with significant solvent permeation and loose coronal dangling chains.""",
                "answer": "(a) q = 2.226 x 10^7 m^-1 (q^2 = 4.957 x 10^14 m^-2); (b) D = 4.28 x 10^-12 m^2/s; (c) R_h = 50.1 nm; (d) rho = R_g / R_h = 1.24 (reflects a swollen core-shell microgel architecture with solvent-permeable fuzzy corona)."
            },
            {
                "id": "prob-5-7",
                "difficulty": "challenge",
                "title": "Mathematical Derivation of the Debye Scattering Form Factor for Gaussian Coils",
                "statement": """Starting from the general definition of the particle scattering form factor for an isotropic solution:
\\[
P(\\theta) = \\frac{1}{N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\left\\langle \\exp(i \\mathbf{q} \\cdot \\mathbf{r}_{ij}) \\right\\rangle
\\]
(a) For a Gaussian random coil obeying continuous chain statistics, the vector displacement $\\mathbf{r}_{ij} = \\mathbf{r}(t_i) - \\mathbf{r}(t_j)$ follows a 3D Gaussian distribution with variance $\\langle r_{ij}^2 \\rangle = |i - j| b^2$.
Prove that:
\\[
\\left\\langle \\exp(i \\mathbf{q} \\cdot \\mathbf{r}_{ij}) \\right\\rangle = \\exp\\left( -\\frac{q^2 b^2 |i - j|}{6} \\right)
\\]
(b) Convert the double summation into a continuous double integral over chain contours $0 \\le x, y \\le 1$ where $x = i/N, y = j/N$:
\\[
P(\\theta) = \\int_0^1 dx \\int_0^1 dy \\exp\\left( -u |x - y| \\right)
\\]
where $u = q^2 R_g^2$.
(c) Evaluate the double integral analytically to prove the Debye formula:
\\[
P(u) = \\frac{2}{u^2} \\left( e^{-u} - 1 + u \\right)
\\]
(d) Show that in the limit $u \\ll 1$, $P(u) \\approx 1 - u/3$, and in the limit $u \\gg 1$, $P(u) \\approx 2/u$.""",
                "solution": """### Step 1: Thermal Average of Phase Factor for Gaussian Chains
For a Gaussian variable $\\mathbf{r}$ with zero mean, the characteristic function is:
\\[
\\langle \\exp(i \\mathbf{q} \\cdot \\mathbf{r}) \\rangle = \\exp\\left( -\\frac{1}{2} \\langle (\\mathbf{q} \\cdot \\mathbf{r})^2 \\rangle \\right)
\\]
Because the orientation is isotropic in 3 dimensions:
\\[
\\langle (\\mathbf{q} \\cdot \\mathbf{r})^2 \\rangle = q^2 \\langle r^2 \\cos^2\\theta \\rangle = q^2 \\langle r^2 \\rangle \\langle \\cos^2\\theta \\rangle = q^2 \\langle r^2 \\rangle \\left( \\frac{1}{3} \\right) = \\frac{1}{3} q^2 \\langle r^2 \\rangle
\\]
Therefore:
\\[
\\langle \\exp(i \\mathbf{q} \\cdot \\mathbf{r}_{ij}) \\rangle = \\exp\\left( -\\frac{q^2 \\langle r_{ij}^2 \\rangle}{6} \\right)
\\]
For a Gaussian random walk of $|i - j|$ steps each of statistical segment length $b$, $\\langle r_{ij}^2 \\rangle = |i - j| b^2$.
Substituting gives:
\\[
\\langle \\exp(i \\mathbf{q} \\cdot \\mathbf{r}_{ij}) \\rangle = \\exp\\left( -\\frac{q^2 b^2 |i - j|}{6} \\right)
\\]

### Step 2: Continuous Integral Formulation
For a long polymer chain ($N \\gg 1$), let $x = i/N$ and $y = j/N$.
Then $|i - j| = N |x - y|$.
The total mean-square radius of gyration of an unperturbed Gaussian chain is:
\\[
R_g^2 = \\frac{N b^2}{6}
\\]
Notice that:
\\[
\\frac{q^2 b^2 |i - j|}{6} = \\frac{q^2 b^2 N |x - y|}{6} = q^2 R_g^2 |x - y| \\equiv u |x - y|
\\]
where $u = q^2 R_g^2$.
The double summation becomes:
\\[
P(\\theta) = \\lim_{N \\to \\infty} \\frac{1}{N^2} \\sum_{i=1}^N \\sum_{j=1}^N \\exp(-u |x - y|) = \\int_0^1 dx \\int_0^1 dy \\exp(-u |x - y|)
\\]

### Step 3: Analytical Evaluation of the Double Integral
By symmetry of the integrand with respect to interchange of $x$ and $y$:
\\[
\\int_0^1 dx \\int_0^1 dy \\exp(-u |x - y|) = 2 \\int_0^1 dx \\int_0^x dy \\exp[-u (x - y)]
\\]
Integrate with respect to $y$:
\\[
\\int_0^x dy \\exp[-u (x - y)] = \\exp(-u x) \\int_0^x e^{u y} dy = \\exp(-u x) \\left[ \\frac{e^{u x} - 1}{u} \\right] = \\frac{1 - e^{-u x}}{u}
\\]
Now integrate with respect to $x$:
\\[
P(u) = 2 \\int_0^1 \\left( \\frac{1 - e^{-u x}}{u} \\right) dx = \\frac{2}{u} \\left[ x + \\frac{e^{-u x}}{u} \\right]_0^1
\\]
Evaluate at the limits:
\\[
\\left[ 1 + \\frac{e^{-u}}{u} \\right] - \\left[ 0 + \\frac{1}{u} \\right] = 1 + \\frac{e^{-u} - 1}{u} = \\frac{u + e^{-u} - 1}{u}
\\]
Multiplying by $\\frac{2}{u}$:
\\[
P(u) = \\frac{2}{u^2} \\left( e^{-u} - 1 + u \\right)
\\]
This completes the exact derivation of Debye's celebrated Gaussian coil form factor!

### Step 4: Asymptotic Limits
1. **Low-q Limit ($u \\ll 1$)**:
   Taylor expand $e^{-u} = 1 - u + \\frac{u^2}{2} - \\frac{u^3}{6} + \\dots$:
   \\[
   e^{-u} - 1 + u = \\frac{u^2}{2} - \\frac{u^3}{6} + \\dots
   \\]
   \\[
   P(u) = \\frac{2}{u^2} \\left( \\frac{u^2}{2} - \\frac{u^3}{6} \\right) = 1 - \\frac{u}{3} = 1 - \\frac{1}{3} q^2 R_g^2
   \\]
2. **High-q Limit ($u \\gg 1$)**:
   As $u \\to \\infty$, $e^{-u} \\to 0$ and $u - 1 \\approx u$:
   \\[
   P(u) \\approx \\frac{2}{u^2} (u) = \\frac{2}{u} = \\frac{2}{q^2 R_g^2}
   \\]""",
                "answer": "(a) Proved: 3D Gaussian phase average yields exp(-q^2 b^2 |i-j| / 6); (b) Continuous double integral formulated with u = q^2 R_g^2; (c) Evaluated: P(u) = (2/u^2)(e^-u - 1 + u); (d) Verified: P(u) -> 1 - u/3 for u << 1, and P(u) -> 2/u for u >> 1."
            },
            {
                "id": "prob-5-8",
                "difficulty": "challenge",
                "title": "Universal Calibration in Gel Permeation Chromatography (GPC/SEC)",
                "statement": """Gel Permeation Chromatography (GPC / Size Exclusion Chromatography, SEC) separates polymer molecules strictly on the basis of their **hydrodynamic volume** $V_h \\propto [\\eta] M$.
According to the Benoit universal calibration principle:
\\[
\\ln([\\eta] M) = f(V_R)
\\]
where $V_R$ is the chromatographic retention volume.
A GPC column set is calibrated with narrow polystyrene (PS) standards in THF at $25.0^\\circ\\text{C}$ ($K_{\\text{PS}} = 1.60 \\times 10^{-4}\\text{ dL/g}, a_{\\text{PS}} = 0.706$).
The calibration curve is linear over the operating range:
\\[
\\ln([\\eta] M) = 28.50 - 0.750 V_R
\\]
(with retention volume $V_R$ in $\\text{mL}$).

An unknown poly(methyl methacrylate) (PMMA) sample elutes at a peak retention volume of $V_R = 18.00\\text{ mL}$.
The Mark-Houwink constants for PMMA in THF at $25.0^\\circ\\text{C}$ are $K_{\\text{PMMA}} = 1.04 \\times 10^{-4}\\text{ dL/g}$ and $a_{\\text{PMMA}} = 0.697$.
(a) Calculate the apparent polystyrene-equivalent molecular weight $M_{\\text{app, PS}}$ corresponding to $V_R = 18.00\\text{ mL}$.
(b) Derive the relationship between the true molecular weight $M_2$ of a polymer and the polystyrene standard equivalent $M_1$ at identical retention volume.
(c) Calculate the true peak molecular weight $M_{\\text{PMMA}}$ of the PMMA sample.
(d) Calculate the percentage error incurred if one erroneously reports the apparent polystyrene-equivalent molecular weight.""",
                "solution": """### Step 1: Apparent Polystyrene-Equivalent Molecular Weight
At $V_R = 18.00\\text{ mL}$, the universal calibration product is:
\\[
\\ln([\\eta] M) = 28.50 - 0.750(18.00) = 28.50 - 13.50 = 15.00
\\]
\\[
([\\eta] M) = e^{15.00} = 3.2690 \\times 10^6\\text{ dL mol/g}
\\]
For polystyrene:
\\[
[\\eta]_{\\text{PS}} M_{\\text{PS}} = (K_{\\text{PS}} M_{\\text{PS}}^{a_{\\text{PS}}}) M_{\\text{PS}} = K_{\\text{PS}} M_{\\text{PS}}^{1 + a_{\\text{PS}}}
\\]
Given $K_{\\text{PS}} = 1.60 \\times 10^{-4}\\text{ dL/g}$ and $1 + a_{\\text{PS}} = 1.706$:
\\[
M_{\\text{app, PS}}^{1.706} = \\frac{[\\eta] M}{K_{\\text{PS}}} = \\frac{3.2690 \\times 10^6}{1.60 \\times 10^{-4}} = 2.0431 \\times 10^{10}
\\]
Taking logarithms:
\\[
1.706 \\ln M_{\\text{app, PS}} = \\ln(2.0431 \\times 10^{10}) = 23.7407
\\]
\\[
\\ln M_{\\text{app, PS}} = \\frac{23.7407}{1.706} = 13.9160 \\implies M_{\\text{app, PS}} = e^{13.9160} = 1,105,700\\text{ g/mol}
\\]

### Step 2: Derivation of the Transformation Formula
At any fixed retention volume $V_R$, Benoit's principle dictates:
\\[
[\\eta]_1 M_1 = [\\eta]_2 M_2
\\]
Substituting Mark-Houwink equations for both polymers:
\\[
K_1 M_1^{1 + a_1} = K_2 M_2^{1 + a_2}
\\]
Rearranging to solve for $M_2$:
\\[
M_2^{1 + a_2} = \\frac{K_1}{K_2} M_1^{1 + a_1}
\\]
\\[
M_2 = \\left( \\frac{K_1}{K_2} \\right)^{\\frac{1}{1 + a_2}} M_1^{\\frac{1 + a_1}{1 + a_2}}
\\]

### Step 3: Calculate True Peak Molecular Weight of PMMA
For PMMA:
- $K_{\\text{PMMA}} = 1.04 \\times 10^{-4}\\text{ dL/g}$
- $1 + a_{\\text{PMMA}} = 1 + 0.697 = 1.697$

From the universal calibration product $[\\eta] M = 3.2690 \\times 10^6$:
\\[
K_{\\text{PMMA}} M_{\\text{PMMA}}^{1.697} = 3.2690 \\times 10^6
\\]
\\[
M_{\\text{PMMA}}^{1.697} = \\frac{3.2690 \\times 10^6}{1.04 \\times 10^{-4}} = 3.1433 \\times 10^{10}
\\]
Taking logarithms:
\\[
1.697 \\ln M_{\\text{PMMA}} = \\ln(3.1433 \\times 10^{10}) = 24.1712
\\]
\\[
\\ln M_{\\text{PMMA}} = \\frac{24.1712}{1.697} = 14.2435
\\]
\\[
M_{\\text{PMMA}} = e^{14.2435} = 1,534,200\\text{ g/mol} \\approx 1,534,000\\text{ g/mol}
\\]

### Step 4: Percentage Error of Apparent Polystyrene Calibration
\\[
\\text{Error} = \\frac{M_{\\text{app, PS}} - M_{\\text{true}}}{M_{\\text{true}}} = \\frac{1,105,700 - 1,534,200}{1,534,200} = \\frac{-428,500}{1,534,200} = -0.2793 = -27.9\\%
\\]
Reporting apparent polystyrene molecular weight underestimates the true molecular weight by $28\\%$, because PMMA is a denser coil (lower $[\\eta]$ at identical mass), thus requiring higher molecular weight to achieve the same hydrodynamic volume as polystyrene.""",
                "answer": "(a) M_app,PS = 1,106,000 g/mol; (b) M_2 = (K_1 / K_2)^(1/(1+a_2)) * M_1^((1+a_1)/(1+a_2)); (c) True M_PMMA = 1,534,000 g/mol; (d) Error = -27.9% underestimation without universal calibration."
            },
            {
                "id": "prob-5-9",
                "difficulty": "challenge",
                "title": "Stockmayer-Fixman Viscosity Plot for Unperturbed Dimensions",
                "statement": """To determine the unperturbed dimension parameter $K_\\theta = \\Phi_0 (\\langle R_0^2 \\rangle / M)^{3/2}$ of a polymer without needing to identify an elusive Flory theta solvent, Stockmayer and Fixman derived the linear relation:
\\[
\\frac{[\\eta]}{M^{1/2}} = K_\\theta + 0.51 \\Phi_0 B M^{1/2}
\\]
where $B$ is the thermodynamic excluded volume parameter.
A series of monodisperse poly(1,4-butadiene) samples are measured in cyclohexane at $25.0^\\circ\\text{C}$ (a good solvent):

| Sample | $M\\text{ (g/mol)}$ | $[\\eta]\\text{ (dL/g)}$ |
|:---:|:---:|:---:|
| A | 25,000 | 0.380 |
| B | 64,000 | 0.688 |
| C | 144,000 | 1.152 |
| D | 256,000 | 1.680 |

(a) Calculate $M^{1/2}$ and $[\\eta]/M^{1/2}$ for each sample.
(b) Perform linear regression of $[\\eta]/M^{1/2}$ vs $M^{1/2}$ to determine $K_\\theta$ (in $\\text{dL g}^{-1/2}\\text{mol}^{-1/2}$) and the slope.
(c) Given $\\Phi_0 = 2.50 \\times 10^{23}\\text{ mol}^{-1}$ (for $[\\eta]$ in $\\text{cm}^3/\\text{g}$), calculate the unperturbed ratio $(\\langle R_0^2 \\rangle / M)^{1/2}$ in Angstroms $\\text{\\AA} \\cdot (\\text{mol/g})^{1/2}$.
(d) Calculate the characteristic ratio $C_\\infty$ given that 1,4-butadiene repeat units have 3 backbone bonds (two $C-C$ of $1.54\\text{ \\AA}$ and one $C=C$ of $1.34\\text{ \\AA}$) and $M_0 = 54.09\\text{ g/mol}$.""",
                "solution": """### Step 1: Tabulate $M^{1/2}$ and $[\\eta]/M^{1/2}$
Calculate values:
- Sample A:
  - $M = 25,000 \\implies M^{1/2} = 158.11\\text{ (g/mol)}^{1/2}$
  - $[\\eta]/M^{1/2} = 0.380 / 158.11 = 2.4034 \\times 10^{-3}\\text{ dL g}^{-1/2}\\text{mol}^{-1/2}$
- Sample B:
  - $M = 64,000 \\implies M^{1/2} = 252.98\\text{ (g/mol)}^{1/2}$
  - $[\\eta]/M^{1/2} = 0.688 / 252.98 = 2.7196 \\times 10^{-3}\\text{ dL g}^{-1/2}\\text{mol}^{-1/2}$
- Sample C:
  - $M = 144,000 \\implies M^{1/2} = 379.47\\text{ (g/mol)}^{1/2}$
  - $[\\eta]/M^{1/2} = 1.152 / 379.47 = 3.0358 \\times 10^{-3}\\text{ dL g}^{-1/2}\\text{mol}^{-1/2}$
- Sample D:
  - $M = 256,000 \\implies M^{1/2} = 505.96\\text{ (g/mol)}^{1/2}$
  - $[\\eta]/M^{1/2} = 1.680 / 505.96 = 3.3204 \\times 10^{-3}\\text{ dL g}^{-1/2}\\text{mol}^{-1/2}$

### Step 2: Linear Regression of $[\\eta]/M^{1/2}$ vs $M^{1/2}$
- Slope:
\\[
\\text{Slope} = \\frac{(3.3204 - 2.4034) \\times 10^{-3}}{505.96 - 158.11} = \\frac{0.9170 \\times 10^{-3}}{347.85} = 2.636 \\times 10^{-6}\\text{ dL/mol}
\\]
- Intercept ($K_\\theta$):
\\[
K_\\theta = 2.4034 \\times 10^{-3} - (2.636 \\times 10^{-6})(158.11) = 2.4034 \\times 10^{-3} - 0.4168 \\times 10^{-3} = 1.9866 \\times 10^{-3}\\text{ dL g}^{-1/2}\\text{mol}^{-1/2}
\\]
Thus:
\\[
K_\\theta = 1.987 \\times 10^{-3}\\text{ dL g}^{-1/2}\\text{mol}^{-1/2}
\\]

### Step 3: Calculate $(\\langle R_0^2 \\rangle / M)^{1/2}$
Convert $K_\\theta$ to $\\text{cm}^3/\\text{g}$:
\\[
K_\\theta = (1.9866 \\times 10^{-3}\\text{ dL g}^{-1/2}\\text{mol}^{-1/2}) \\times 100\\text{ cm}^3/\\text{dL} = 0.19866\\text{ cm}^3\\text{ g}^{-3/2}\\text{mol}^{-1/2}
\\]
From the Flory-Fox equation:
\\[
K_\\theta = \\Phi_0 \\left( \\frac{\\langle R_0^2 \\rangle}{M} \\right)^{3/2} \\implies \\frac{\\langle R_0^2 \\rangle}{M} = \\left( \\frac{K_\\theta}{\\Phi_0} \\right)^{2/3}
\\]
Given $\\Phi_0 = 2.50 \\times 10^{23}\\text{ mol}^{-1}$:
\\[
\\frac{K_\\theta}{\\Phi_0} = \\frac{0.19866}{2.50 \\times 10^{23}} = 7.9464 \\times 10^{-25}\\text{ cm}^3\\text{ mol/g}^{3/2}
\\]
\\[
\\frac{\\langle R_0^2 \\rangle}{M} = (7.9464 \\times 10^{-25})^{2/3} = 8.577 \\times 10^{-17}\\text{ cm}^2\\text{ mol/g} = 0.8577\\text{ \\AA}^2\\text{ mol/g}
\\]
Taking the square root:
\\[
\\left( \\frac{\\langle R_0^2 \\rangle}{M} \\right)^{1/2} = \\sqrt{0.8577} = 0.9261\\text{ \\AA} (\\text{mol/g})^{1/2}
\\]

### Step 4: Characteristic Ratio $C_\\infty$
For 1,4-polybutadiene, each repeating unit ($M_0 = 54.09\\text{ g/mol}$) contains 3 backbone bonds:
- Two single bonds: $l_1 = l_2 = 1.54\\text{ \\AA} \\implies l_1^2 = 2.3716\\text{ \\AA}^2$
- One double bond: $l_3 = 1.34\\text{ \\AA} \\implies l_3^2 = 1.7956\\text{ \\AA}^2$
Sum of square bond lengths per repeat unit:
\\[
\\sum_{i=1}^3 l_i^2 = 2(2.3716) + 1.7956 = 4.7432 + 1.7956 = 6.5388\\text{ \\AA}^2
\\]
Number of repeat units per gram: $1 / M_0 = 1 / 54.09\\text{ mol/g}$.
The unperturbed freely jointed square dimension per repeat unit is:
\\[
\\langle R_0^2 \\rangle_{\\text{free}} / M = \\frac{\\sum l_i^2}{M_0} = \\frac{6.5388\\text{ \\AA}^2}{54.09\\text{ g/mol}} = 0.12089\\text{ \\AA}^2\\text{ mol/g}
\\]
The characteristic ratio is:
\\[
C_\\infty = \\frac{\\langle R_0^2 \\rangle / M}{\\langle R_0^2 \\rangle_{\\text{free}} / M} = \\frac{0.8577}{0.12089} = 7.095 \\approx 7.10
\\]
$C_\\infty = 7.1$ reflects the conformation of cis/trans-1,4-polybutadiene with low torsional barrier around the allylic single bonds.""",
                "answer": "(a) Tabulated M^0.5 and [eta]/M^0.5; (b) Intercept K_theta = 1.987 x 10^-3 dL g^-0.5 mol^-0.5, Slope = 2.636 x 10^-6 dL/mol; (c) (<R_0^2>/M)^0.5 = 0.926 Angstrom (mol/g)^0.5; (d) C_infinity = 7.10."
            }
        ]
    }

print("Unit 5 authoring complete.")

def build_unit_6():
    return {
        "id": "unit-6",
        "number": 6,
        "title": "Step-Growth Polymerization: Carothers Equation, Kinetics & Statistics",
        "leadSummary": "Step-growth condensation mechanisms, functional group reactivity, Carothers equation for linear polycondensation, conversion thresholds, stoichiometric imbalance ratio (r) and monofunctional chain stoppers, self-catalyzed vs externally acid-catalyzed polyesterification kinetics, Flory's principle of equal reactivity, Flory-Schulz most probable molecular weight distributions, non-linear step-growth with multifunctional branch units, and gelation percolation theory comparing Carothers vs Flory-Stockmayer critical branching coefficients (alpha_c).",
        "simulations": ["sim_poly_carothers_step_growth"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Fundamentals of Step-Growth Polymerization: Mechanisms & Reversible Equilibrium",
                "content": """Step-growth polymerization occurs between bifunctional or polyfunctional monomers bearing complementary reactive functional groups. Unlike addition chain polymerizations, any two molecular species present in the reaction vessel—monomers, dimers, trimers, or long oligomers—can undergo condensation with each other at any stage during the synthesis.

### Reaction Classifications: $A-B$ vs $A-A + B-B$
Step-growth systems are classified by their monomer stoichiometry:
1. **$A-B$ Monomer Systems**:
   - A single monomer molecule possesses both complementary functional groups in equal stoichiometric 1:1 proportion within the same molecule.
   - Examples: $\\omega$-amino acids in polyamide synthesis (e.g., 6-aminocaproic acid forming Nylon 6), or $\\omega$-hydroxy acids forming polyesters (e.g., glycolic acid forming polyglycolide).
   - Strict equimolar stoichiometry is chemically guaranteed.
2. **$A-A + B-B$ Monomer Systems**:
   - Polymerization occurs between two distinct bifunctional monomers, one bearing two $A$ functional groups and the other bearing two $B$ functional groups.
   - Examples:
     - Polyamides: Hexamethylenediamine ($H_2N-(CH_2)_6-NH_2$, $A-A$) reacting with adipic acid ($HOOC-(CH_2)_4-COOH$, $B-B$) to form **Nylon 6,6**.
     - Polyesters: Ethylene glycol ($HO-CH_2CH_2-OH$, $A-A$) reacting with dimethyl terephthalate ($B-B$) to form **poly(ethylene terephthalate)** (PET).
     - Polycarbonates: Bisphenol A reacting with phosgene ($COCl_2$) or diphenyl carbonate.
     - Polyurethanes: Diisocyanates ($OCN-R-NCO$) reacting with diols ($HO-R'-OH$) without elimination of small molecule by-products (polyaddition).

### Reversible Thermodynamic Equilibrium & Le Chatelier Removal
Most condensation reactions (esterification, amidation, transesterification) are reversible equilibria:
\\[
-\\text{COOH} + -\\text{OH} \\xrightleftharpoons[k_r]{k_f} -\\text{COO}- + \\text{H}_2\\text{O}
\\]
The equilibrium constant is:
\\[
K = \\frac{[-\\text{COO}-] [\\text{H}_2\\text{O}]}{[-\\text{COOH}] [-\\text{OH}]}
\\]
For typical polyesterifications, $K$ is modest ($K \\approx 1 - 10$). For polyamidations, $K \\approx 100 - 400$.
To drive the reaction to the high conversions ($p > 0.99$) required for engineering-grade mechanical properties, the low-molecular-weight condensation by-product ($\\text{H}_2\\text{O}, \\text{CH}_3\\text{OH}, \\text{HCl}$) must be continuously removed from the melt under high vacuum ($< 1\\text{ mbar}$) at elevated temperatures ($200 - 280^\\circ\\text{C}$) with vigorous mechanical agitation."""
            },
            {
                "secNumber": "6.2",
                "title": "Carothers Equation for Linear Systems: Conversion, $X_n$ & High-Conversion Imperative",
                "content": """In 1929, Wallace Carothers formulated the fundamental mathematical relationship between the fractional conversion of reactive functional groups and the resulting average degree of polymerization in step-growth systems.

### Mathematical Derivation of the Carothers Equation
Consider an equimolar linear polymerization ($A-B$ or stoichiometric $A-A + B-B$).
Let $N_0$ be the total number of monomer molecules initially present.
Because each monomer molecule has 2 functional groups, the initial number of functional groups of each type is $N_0$.
At reaction time $t$, let $N$ be the total number of macromolecular chains (molecules) remaining in the reaction mixture.
Each reaction event between two functional groups forms one new covalent bond and reduces the total number of separate molecules by exactly one:
\\[
\\text{Number of bonds formed} = N_0 - N
\\]
Since forming one inter-unit bond consumes two functional groups (one $A$ and one $B$), the total number of functional groups consumed is $2(N_0 - N)$.
The fractional conversion $p$ of functional groups is defined as the fraction of initial functional groups that have reacted:
\\[
p = \\frac{2(N_0 - N)}{2 N_0} = \\frac{N_0 - N}{N_0} = 1 - \\frac{N}{N_0}
\\]
Rearranging gives the ratio of initial to remaining molecules:
\\[
\\frac{N}{N_0} = 1 - p
\\]
The **number-average degree of polymerization** $X_n$ is defined as the average number of monomer units per macromolecule:
\\[
X_n \\equiv \\frac{N_0}{N}
\\]
Substituting $N/N_0 = 1 - p$ yields the celebrated **Carothers equation**:
\\[
X_n = \\frac{1}{1 - p}
\\]

### The High-Conversion Imperative
The Carothers equation demonstrates the mathematical difficulty of synthesizing high molecular weight polymers via step-growth:
- At $p = 0.50$ ($50\\%$ conversion): $X_n = 1 / (1 - 0.50) = 2$ (only dimers on average).
- At $p = 0.80$ ($80\\%$ conversion): $X_n = 1 / (1 - 0.80) = 5$ (short oligomers).
- At $p = 0.90$ ($90\\%$ conversion): $X_n = 1 / (1 - 0.90) = 10$.
- At $p = 0.98$ ($98\\%$ conversion): $X_n = 1 / (1 - 0.98) = 50$.
- At $p = 0.99$ ($99\\%$ conversion): $X_n = 1 / (1 - 0.99) = 100$.
- At $p = 0.999$ ($99.9\\%$ conversion): $X_n = 1 / (1 - 0.999) = 1,000$.

Polymers typically develop useful structural, mechanical, and tensile properties (fiber forming, impact resistance, film toughness) only when $X_n \\ge 100$. Therefore, step-growth industrial processes must achieve conversions exceeding **$99.0\\%$ to $99.9\\%$**, which requires near-perfect monomer purity, precise stoichiometric balance, and total by-product removal."""
            },
            {
                "secNumber": "6.3",
                "title": "Stoichiometric Imbalance ($r$) & Monofunctional Chain Stoppers: Molecular Weight Control",
                "content": """In actual industrial synthesis, achieving $X_n = \\infty$ is neither desirable nor processable; extremely high molecular weights lead to unworkable melt viscosities. Molecular weight is precisely controlled and limited through **stoichiometric imbalance** or the intentional addition of **monofunctional chain stoppers**.

### Derivation of the Modified Carothers Equation with Imbalance
Consider an $A-A + B-B$ system where $A$ groups are in deficiency relative to $B$ groups.
Define the stoichiometric ratio:
\\[
r \\equiv \\frac{N_A}{N_B} \\le 1.0
\\]
where $N_A$ and $N_B$ are the initial number of $A$ and $B$ functional groups, respectively ($N_A = 2 N_{AA}$ and $N_B = 2 N_{BB}$).
The total number of monomer molecules initially present is:
\\[
N_0 = N_{AA} + N_{BB} = \\frac{N_A}{2} + \\frac{N_B}{2} = \\frac{N_A + N_B}{2} = \\frac{r N_B + N_B}{2} = \\frac{N_B(1 + r)}{2}
\\]
Let $p$ be the fractional conversion of the minority group ($A$ groups).
Number of reacted $A$ groups $= p N_A = p r N_B$.
Because one $B$ group reacts for every $A$ group, the number of reacted $B$ groups is also $p r N_B$.
Total number of unreacted functional groups remaining:
\\[
\\text{Remaining groups} = (N_A - p N_A) + (N_B - p N_A) = N_A + N_B - 2 p N_A = N_B(1 + r - 2 r p)
\\]
Since each remaining linear polymer chain terminates with two functional groups (one at each end), the total number of polymer molecules $N$ remaining is half the number of remaining functional groups:
\\[
N = \\frac{N_B(1 + r - 2 r p)}{2}
\\]
The number-average degree of polymerization $X_n = N_0 / N$ is:
\\[
X_n = \\frac{\\frac{N_B(1 + r)}{2}}{\\frac{N_B(1 + r - 2 r p)}{2}} = \\frac{1 + r}{1 + r - 2 r p}
\\]

### Asymptotic Limit at Complete Conversion ($p \\to 1$)
When all minority groups are completely consumed ($p = 1.0$), all chain ends are capped with the excess $B$ functional group, terminating further polymerization:
\\[
X_{n, \\text{max}} = \\lim_{p \\to 1} \\frac{1 + r}{1 + r - 2 r} = \\frac{1 + r}{1 - r}
\\]
- If $r = 1.0$ (perfect stoichiometry): $X_{n, \\text{max}} \\to \\infty$.
- If $r = 0.99$ ($1\\%$ molar excess of $B-B$): $X_{n, \\text{max}} = \\frac{1 + 0.99}{1 - 0.99} = \\frac{1.99}{0.01} = 199$.
- If $r = 0.98$ ($2\\%$ molar excess of $B-B$): $X_{n, \\text{max}} = \\frac{1 + 0.98}{1 - 0.98} = \\frac{1.98}{0.02} = 99$.
- If $r = 0.95$ ($5\\%$ molar excess): $X_{n, \\text{max}} = \\frac{1.95}{0.05} = 39$.

### Monofunctional Chain Stoppers
Adding a monofunctional compound $R-B$ (such as acetic acid in Nylon 6,6 synthesis) has the exact same stoichiometric capping effect. Each molecule of $R-B$ provides one $B$ group. The effective stoichiometric ratio becomes:
\\[
r_{\\text{eff}} = \\frac{N_A}{N_B + 2 N_{B'}}
\\]
where $N_{B'}$ is the number of monofunctional chain stopper molecules. The factor of 2 accounts for the fact that one monofunctional stopper eliminates one chain end without supplying a second reactive site for chain growth."""
            },
            {
                "secNumber": "6.4",
                "title": "Kinetics of Step-Growth: Self-Catalyzed vs Acid-Catalyzed Polyesterification",
                "content": """The kinetics of step-growth polymerization depend fundamentally on whether the reaction requires an added external catalyst or is self-catalyzed by one of the reacting monomer functional groups.

### Case 1: Self-Catalyzed Polyesterification
In the absence of an added strong acid catalyst, polyesterification between a dicarboxylic acid and a diol is catalyzed by the carboxylic acid monomer itself:
\\[
-\\text{COOH} + -\\text{COOH} \\xrightleftharpoons{K} -\\text{C(OH)}_2^+ + -\\text{COO}^-
\\]
\\[
-\\text{C(OH)}_2^+ + -\\text{OH} \\xrightarrow{k} -\\text{COO}- + \\text{H}_2\\text{O} + \\text{H}^+
\\]
The rate of disappearance of carboxylic acid groups is third-order overall:
\\[
-\\frac{d[\\text{COOH}]}{dt} = k [\\text{COOH}]^2 [\\text{OH}]
\\]
For equimolar initial concentrations $c_0 = [\\text{COOH}]_0 = [\\text{OH}]_0$, at conversion $p$:
\\[
c = [\\text{COOH}] = [\\text{OH}] = c_0 (1 - p)
\\]
Substituting into the rate equation:
\\[
-\\frac{dc}{dt} = k c^3
\\]
Separating variables and integrating from $t = 0$ ($c = c_0$) to $t$:
\\[
\\int_{c_0}^c -\\frac{dc}{c^3} = k \\int_0^t dt \\implies \\left[ \\frac{1}{2 c^2} \\right]_{c_0}^c = k t
\\]
\\[
\\frac{1}{c^2} - \\frac{1}{c_0^2} = 2 k t
\\]
Substituting $c = c_0(1 - p)$:
\\[
\\frac{1}{c_0^2(1 - p)^2} - \\frac{1}{c_0^2} = 2 k t \\implies \\frac{1}{(1 - p)^2} = 1 + 2 c_0^2 k t
\\]
Since $X_n = 1 / (1 - p)$:
\\[
X_n^2 = 1 + 2 c_0^2 k t
\\]
Thus, for self-catalyzed polyesterification, a plot of $\\frac{1}{(1 - p)^2}$ (or $X_n^2$) versus time $t$ is strictly linear with slope $2 c_0^2 k$. The degree of polymerization scales as the square root of time ($X_n \\propto t^{1/2}$).

### Case 2: Externally Acid-Catalyzed Polyesterification
When a catalytic amount of strong mineral or sulfonic acid (such as $p$-toluenesulfonic acid, $\\text{H}_2\\text{SO}_4$, or titanium alkoxide) is added, the proton concentration $[\\text{H}^+]$ remains constant:
\\[
-\\frac{d[\\text{COOH}]}{dt} = k' [\\text{H}^+] [\\text{COOH}] [\\text{OH}] = k_{\\text{cat}} [\\text{COOH}] [\\text{OH}]
\\]
For stoichiometric concentrations $c = c_0(1 - p)$:
\\[
-\\frac{dc}{dt} = k_{\\text{cat}} c^2
\\]
Integrating this second-order rate equation:
\\[
\\int_{c_0}^c -\\frac{dc}{c^2} = k_{\\text{cat}} \\int_0^t dt \\implies \\frac{1}{c} - \\frac{1}{c_0} = k_{\\text{cat}} t
\\]
\\[
\\frac{1}{c_0(1 - p)} - \\frac{1}{c_0} = k_{\\text{cat}} t \\implies \\frac{1}{1 - p} = 1 + c_0 k_{\\text{cat}} t
\\]
Since $X_n = 1 / (1 - p)$:
\\[
X_n = 1 + c_0 k_{\\text{cat}} t
\\]
In externally catalyzed step-growth, $X_n$ grows **linearly with time** ($X_n \\propto t$). This linear kinetics achieves target molecular weights dramatically faster than the self-catalyzed route."""
            },
            {
                "secNumber": "6.5",
                "title": "Flory's Principle of Equal Reactivity of Functional Groups",
                "content": """A cornerstone of macromolecular kinetic theory is **Flory's principle of equal reactivity of functional groups**, proposed by Paul Flory in 1939.

### Formal Statement
*The intrinsic chemical reactivity of a functional group in a step-growth reaction is independent of the size of the macromolecule to which it is attached.*

That is:
\\[
k_{1,1} = k_{1,x} = k_{x,y} = k = \\text{constant}
\\]
where $k_{x,y}$ is the rate constant for the reaction between an $x$-mer and a $y$-mer.

### Theoretical Justification: Diffusion in Condensed Phase
At first glance, Flory's principle seems counterintuitive: as polymer chains grow longer, their center-of-mass translational diffusion coefficient decreases dramatically ($D_{\\text{cm}} \\propto M^{-1}$ or $M^{-2}$). One might expect large coils to react much more slowly.
However, in condensed liquids, reaction rate is governed by the collision rate inside a **solvent cage**:
1. Although a large macromolecule diffuses into a new encounter volume slowly, once two coils overlap, their terminal functional groups remain trapped in close proximity inside the same solvent cage for an extended duration.
2. The collision frequency between reactive end groups within the cage is determined entirely by **local segmental mobility** (bond rotation, segmental tumbling), not by whole-molecule translation.
3. Because the local steric and electronic chemical environment of a carboxylic acid or hydroxyl group on a long flexible chain is virtually indistinguishable from that on a short chain, the intrinsic rate constant $k$ remains unchanged.

### Experimental Evidence
Flory validated this principle by measuring the rate constants for esterification of homologous series of monocarboxylic and dicarboxylic acids:
- Formic acid ($n = 1$): $k = 4.70 \\times 10^{-4}$
- Acetic acid ($n = 2$): $k = 2.45 \\times 10^{-4}$
- Propionic acid ($n = 3$): $k = 1.95 \\times 10^{-4}$
- Butyric acid ($n = 4$): $k = 1.98 \\times 10^{-4}$
- Caproic acid ($n = 6$): $k = 2.01 \\times 10^{-4}$
- Adipic acid to sebacic acid ($n = 6 \\to 10$): $k = 2.00 \\times 10^{-4}\\text{ L/(mol s)}$

Beyond the first two or three carbons where electronic induction from adjacent groups is felt, the rate constants reach an exact invariant plateau."""
            },
            {
                "secNumber": "6.6",
                "title": "Molecular Weight Distributions: Flory-Schulz 'Most Probable' Distribution ($N_x, W_x$)",
                "content": """Because every functional group has identical reactivity throughout the reaction, the distribution of chain lengths in linear step-growth polymerization can be derived purely from probability theory.

### Derivation of the Number Fraction Distribution ($N_x$)
Consider a linear polymer formed by step-growth with conversion $p$.
- The probability that a given functional group has reacted is $p$.
- The probability that a functional group has *not* reacted is $1 - p$.

An $x$-mer (a chain consisting of exactly $x$ monomer units) contains:
- Exactly $x - 1$ reacted bonds (each with probability $p$).
- Exactly one unreacted end group terminating the chain (with probability $1 - p$).

Applying the multiplication rule of independent probabilities, the probability that a randomly chosen chain contains exactly $x$ units—which equals the **mole fraction** (number fraction) $N_x$ of $x$-mers—is:
\\[
N_x = (1 - p) p^{x-1}
\\]
This is the celebrated **Flory-Schulz most probable distribution** (geometric distribution).
Checking normalization:
\\[
\\sum_{x=1}^\\infty N_x = (1 - p) \\sum_{x=1}^\\infty p^{x-1} = (1 - p) \\frac{1}{1 - p} = 1.0
\\]

### Derivation of the Weight Fraction Distribution ($W_x$)
The weight fraction $W_x$ of $x$-mers is the mass of all $x$-mers divided by total sample mass.
Neglecting end-group mass differences, the mass of an $x$-mer is proportional to $x$:
\\[
W_x = \\frac{x N_x}{\\sum_{j=1}^\\infty j N_j} = \\frac{x N_x}{X_n}
\\]
Substituting $N_x = (1 - p) p^{x-1}$ and $X_n = 1 / (1 - p)$:
\\[
W_x = x (1 - p)^2 p^{x-1}
\\]
Checking normalization:
\\[
\\sum_{x=1}^\\infty W_x = (1 - p)^2 \\sum_{x=1}^\\infty x p^{x-1} = (1 - p)^2 \\frac{1}{(1 - p)^2} = 1.0
\\]

### Molecular Weight Averages and Dispersity
1. **Number-Average Degree of Polymerization**:
\\[
X_n = \\sum_{x=1}^\\infty x N_x = \\frac{1}{1 - p}
\\]
2. **Weight-Average Degree of Polymerization**:
\\[
X_w = \\sum_{x=1}^\\infty x W_x = (1 - p)^2 \\sum_{x=1}^\\infty x^2 p^{x-1} = (1 - p)^2 \\frac{1 + p}{(1 - p)^3} = \\frac{1 + p}{1 - p}
\\]
3. **Polydispersity Index (Dispersity $\\text{Đ}$)**:
\\[
\\text{Đ} = \\frac{X_w}{X_n} = \\frac{\\frac{1 + p}{1 - p}}{\\frac{1}{1 - p}} = 1 + p
\\]
As conversion approaches unity ($p \\to 1.0$):
\\[
\\lim_{p \\to 1} \\text{Đ} = 1 + 1 = 2.0
\\]
Thus, linear step-growth polycondensation has a theoretical limiting dispersity of **exactly 2.0**."""
            },
            {
                "secNumber": "6.7",
                "title": "Non-Linear Step-Growth & Cross-Linking: Branching, Polyfunctionality & Networks",
                "content": """When monomers with functionality greater than two ($f \\ge 3$) are introduced into a step-growth mixture, the polymer chains branch in multiple spatial dimensions, leading to hyperbranched polymers or macroscopic three-dimensional cross-linked network gels.

### Average Functionality of Monomer Mixtures
For a reaction mixture containing $N_i$ molecules of monomer $i$, each bearing functionality $f_i$:
The **average functionality** $f_{\\text{avg}}$ is defined as:
\\[
f_{\\text{avg}} = \\frac{\\sum N_i f_i}{\\sum N_i}
\\]
- If $f_{\\text{avg}} = 2.0$: strictly linear polymers are formed.
- If $f_{\\text{avg}} > 2.0$: branched structures form, which may reach a critical point of infinite molecular weight (the **gel point**).

For stoichiometric systems where $A$ and $B$ functional groups are present in stoichiometric balance ($N_A = N_B$):
\\[
f_{\\text{avg}} = \\frac{2 N_A}{\\sum N_i} = \\frac{2 \\sum N_{A,i} f_{A,i}}{\\sum N_{A,i} + \\sum N_{B,j}}
\\]

### Topological Regimes of Non-Linear Polymerization
1. **Pre-Gel Regime ($p < p_c$)**:
   - The reaction mixture consists of soluble branched molecules, dendrimer-like structures, and unreacted monomers.
   - The mixture remains completely soluble in appropriate solvents and flows as a viscous liquid.
2. **The Gel Point ($p = p_c$)**:
   - At this precise critical conversion, the first continuous, macroscopic macromolecular cluster of infinite size (spanning the entire dimensions of the reactor) forms.
   - Viscosity diverges to infinity ($\\eta \\to \\infty$).
   - The mixture suddenly transforms from a liquid to an elastic, insoluble gel.
3. **Post-Gel Regime ($p > p_c$)**:
   - The system partitions into two distinct phases:
     - **Gel Fraction** ($w_{\\text{gel}}$): The insoluble, infinite cross-linked macroscopic network.
     - **Sol Fraction** ($w_{\\text{sol}}$): Finite, extractable soluble branched oligomers trapped within the network interstices ($w_{\\text{sol}} + w_{\\text{gel}} = 1.0$).
     - As conversion increases further, finite sol oligomers are progressively incorporated into the infinite gel network, so $w_{\\text{gel}} \\to 1.0$."""
            },
            {
                "secNumber": "6.8",
                "title": "Gelation Theory: Carothers vs Flory-Stockmayer Gel Point ($\\alpha_c$) & Percolation",
                "content": """Predicting the critical conversion $p_c$ at which gelation occurs is one of the classic problems in theoretical physical chemistry, historically resolved by two distinct theories: the Carothers approach and the Flory-Stockmayer statistical percolation model.

### 1. The Carothers Gel Point Derivation
Carothers defined the gel point as the conversion at which the **number-average** degree of polymerization diverges to infinity:
\\[
X_n = \\frac{N_0}{N} \\to \\infty \\implies N \\to 0
\\]
For a monomer mixture with average functionality $f_{\\text{avg}}$, initial total functional groups $= N_0 f_{\\text{avg}}$.
At conversion $p$, the number of reacted functional groups is $p N_0 f_{\\text{avg}}$.
Since each reaction forms one bond and reduces the number of molecules by one:
\\[
N = N_0 - \\frac{p N_0 f_{\\text{avg}}}{2} = N_0 \\left( 1 - \\frac{p f_{\\text{avg}}}{2} \\right)
\\]
Therefore:
\\[
X_n = \\frac{N_0}{N} = \\frac{2}{2 - p f_{\\text{avg}}}
\\]
Setting the denominator to zero ($X_n \\to \\infty$) yields the **Carothers gel point**:
\\[
p_c = \\frac{2}{f_{\\text{avg}}}
\\]
- For a trifunctional monomer ($f_{\\text{avg}} = 3$): $p_c = 2/3 = 0.667$ ($66.7\\%$ conversion).
- For a tetrafunctional monomer ($f_{\\text{avg}} = 4$): $p_c = 2/4 = 0.500$ ($50.0\\%$ conversion).

### 2. The Flory-Stockmayer Statistical Gelation Theory
Paul Flory and Walter Stockmayer pointed out a profound flaw in Carothers' reasoning:
*Gelation occurs when the first infinite macromolecular network forms—which corresponds to the divergence of the **weight-average** molecular weight ($X_w \\to \\infty$), while the number-average molecular weight ($X_n$) remains modest and finite!*

Flory defined the **branching coefficient** $\\alpha$ as the probability that a given functional group on a multifunctional branch unit leads, via a chain of bifunctional units, to another multifunctional branch unit.
Consider an $A_f$ branch monomer reacting with bifunctional $A-A$ and $B-B$ monomers.
The critical branching coefficient for gelation in a system where branch units have functionality $f$ is:
\\[
\\alpha_c = \\frac{1}{f - 1}
\\]
- If branch units are trifunctional ($f = 3$): $\\alpha_c = 1 / (3 - 1) = 1/2 = 0.500$.
- If branch units are tetrafunctional ($f = 4$): $\\alpha_c = 1 / (4 - 1) = 1/3 = 0.333$.

For a stoichiometric mixture of bifunctional $A-A$ and $B-B$ monomers with a fraction $\\rho$ of $A$ groups belonging to $A_f$ branch units ($p_A = p_B = p$):
\\[
\\alpha = \\frac{p_A p_B \\rho}{1 - p_A p_B (1 - \\rho)} = \\frac{p^2 \\rho}{1 - p^2 (1 - \\rho)}
\\]
For pure $A_f + B-B$ stoichiometric systems where all $A$ groups are on branch units ($\rho = 1$):
\\[
\\alpha = p^2 \\implies p_c = \\sqrt{\\alpha_c} = \\frac{1}{\\sqrt{f - 1}}
\\]
For a trifunctional system ($f = 3$):
\\[
p_c = \\frac{1}{\\sqrt{3 - 1}} = \\frac{1}{\\sqrt{2}} = 0.7071\\ (70.7\\%)
\\]
Carothers predicts $p_c = 2 / f_{\\text{avg}} = 2 / 2.4 = 0.833$ ($83.3\\%$).

### Experimental Reality and Intramolecular Cyclization
Experimental gel points measured via rheology (where $\\tan \\delta = G'' / G'$ becomes frequency-independent) are typically slightly higher than Flory-Stockmayer predictions ($p_{c, \\text{exp}} > p_{c, \\text{Flory}}$) because a small fraction of bonds form unreactive intramolecular loops that waste functional groups without contributing to the infinite percolating network."""
            }
        ],
        "problems": [
            {
                "id": "prob-6-1",
                "difficulty": "foundation",
                "title": "Carothers Equation for Linear Polyesterification at High Conversion",
                "statement": """An equimolar mixture of adipic acid ($HOOC-(CH_2)_4-COOH$, formula weight $146.14\\text{ g/mol}$) and 1,4-butanediol ($HO-(CH_2)_4-OH$, formula weight $90.12\\text{ g/mol}$) is polymerized to form poly(butylene adipate).
During polycondensation, water ($18.02\\text{ g/mol}$) is removed. The repeating unit is $-[O-(CH_2)_4-O-CO-(CH_2)_4-CO]-$ with formula weight $M_0 = 200.24\\text{ g/mol}$.
Calculate:
(a) The number-average degree of polymerization $X_n$ at conversions $p = 0.900, 0.980, 0.990, 0.995$, and $0.999$.
(b) The number-average molecular weight $M_n$ at each of these conversions (accounting for unreacted end groups).
(c) The weight-average degree of polymerization $X_w$ and polydispersity index $\\text{Đ}$ at $p = 0.990$ and $p = 0.999$.""",
                "solution": """### Step 1: Calculate $X_n$ via Carothers Equation
For an equimolar linear step-growth system:
\\[
X_n = \\frac{1}{1 - p}
\\]
1. $p = 0.900 \\implies X_n = \\frac{1}{1 - 0.900} = \\frac{1}{0.100} = 10.0$
2. $p = 0.980 \\implies X_n = \\frac{1}{1 - 0.980} = \\frac{1}{0.020} = 50.0$
3. $p = 0.990 \\implies X_n = \\frac{1}{1 - 0.990} = \\frac{1}{0.010} = 100.0$
4. $p = 0.995 \\implies X_n = \\frac{1}{1 - 0.995} = \\frac{1}{0.005} = 200.0$
5. $p = 0.999 \\implies X_n = \\frac{1}{1 - 0.999} = \\frac{1}{0.001} = 1,000.0$

### Step 2: Calculate $M_n$
The chain structure is $H-[O-(CH_2)_4-O-CO-(CH_2)_4-CO]_{X_n/2}-OH$ (where each esterification unit pair is one adipate + one butanediol, $M_0 = 200.24\\text{ g/mol}$ per repeat unit, corresponding to $X_n$ monomer residues, or $X_n/2$ repeat units).
Let $M_{\\text{monomer, avg}} = (146.14 + 90.12) / 2 = 118.13\\text{ g/mol}$.
Loss of water ($18.02\\text{ g/mol}$) occurs per bond formed ($X_n - 1$ bonds for $X_n$ monomer residues):
\\[
M_n = X_n M_{\\text{monomer, avg}} - (X_n - 1) M_{\\text{water}} = X_n (118.13 - 18.02) + 18.02 = X_n (100.11) + 18.02
\\]
1. $p = 0.900$: $M_n = 10(100.11) + 18 = 1,019\\text{ g/mol}$
2. $p = 0.980$: $M_n = 50(100.11) + 18 = 5,024\\text{ g/mol}$
3. $p = 0.990$: $M_n = 100(100.11) + 18 = 10,029\\text{ g/mol}$
4. $p = 0.995$: $M_n = 200(100.11) + 18 = 20,040\\text{ g/mol}$
5. $p = 0.999$: $M_n = 1000(100.11) + 18 = 100,128\\text{ g/mol}$

### Step 3: Calculate $X_w$ and Dispersity $\\text{Đ}$
For the Flory-Schulz most probable distribution:
\\[
X_w = \\frac{1 + p}{1 - p} = X_n (1 + p)
\\]
\\[
\\text{Đ} = \\frac{X_w}{X_n} = 1 + p
\\]
- At $p = 0.990$:
  \\[
  X_w = 100.0 \\times (1 + 0.990) = 199.0
  \\]
  \\[
  \\text{Đ} = 1 + 0.990 = 1.990
  \\]
- At $p = 0.999$:
  \\[
  X_w = 1000.0 \\times (1 + 0.999) = 1,999.0
  \\]
  \\[
  \\text{Đ} = 1 + 0.999 = 1.999
  \\]""",
                "answer": "(a) X_n = 10.0 (p=0.90), 50.0 (p=0.98), 100.0 (p=0.99), 200.0 (p=0.995), 1000.0 (p=0.999); (b) M_n: 1,019 g/mol (0.90), 5,024 g/mol (0.98), 10,029 g/mol (0.99), 20,040 g/mol (0.995), 100,130 g/mol (0.999); (c) At p=0.99: X_w = 199.0, PDI = 1.990; At p=0.999: X_w = 1,999.0, PDI = 1.999."
            },
            {
                "id": "prob-6-2",
                "difficulty": "foundation",
                "title": "Molecular Weight Regulation via Monofunctional Chain Stopper in Nylon 6,6",
                "statement": """Nylon 6,6 is synthesized by polycondensation of hexamethylenediamine ($H_2N-(CH_2)_6-NH_2$) and adipic acid ($HOOC-(CH_2)_4-COOH$).
To prevent unworkably high melt viscosity during fiber spinning, the number-average molecular weight at complete conversion ($p = 1.0$) must be limited to exactly $M_n = 15,000\\text{ g/mol}$.
The repeat unit formula weight is $M_0 = 226.32\\text{ g/mol}$ (corresponding to two monomer residues, so average monomer mass is $M_0 / 2 = 113.16\\text{ g/mol}$).
(a) Determine the required number-average degree of polymerization $X_n$ at complete conversion.
(b) Calculate the required stoichiometric imbalance ratio $r = N_A / N_B$ if excess adipic acid is used to control molecular weight.
(c) Alternatively, if an equimolar mixture of diamine and diacid is used, calculate the mole percent of acetic acid (monofunctional chain stopper, $CH_3COOH$) that must be added relative to adipic acid.""",
                "solution": """### Step 1: Calculate Target $X_n$
The repeat unit contains 2 monomer residues ($X_n = 2$ corresponds to one repeat unit).
Average monomer residue mass in the chain:
\\[
M_{\\text{res}} = \\frac{226.32}{2} = 113.16\\text{ g/mol}
\\]
Target $M_n = 15,000\\text{ g/mol}$:
\\[
X_n = \\frac{M_n}{M_{\\text{res}}} = \\frac{15,000}{113.16} = 132.56 \\approx 132.6
\\]

### Step 2: Calculate Required Stoichiometric Ratio $r$
At complete conversion ($p = 1.0$), the modified Carothers equation is:
\\[
X_n = \\frac{1 + r}{1 - r}
\\]
Solve for $r$:
\\[
X_n (1 - r) = 1 + r \\implies X_n - r X_n = 1 + r \\implies r (X_n + 1) = X_n - 1
\\]
\\[
r = \\frac{X_n - 1}{X_n + 1}
\\]
Substitute $X_n = 132.56$:
\\[
r = \\frac{132.56 - 1}{132.56 + 1} = \\frac{131.56}{133.56} = 0.98503 = 0.9850
\\]
This means there must be a $1.50\\%$ stoichiometric deficit of diamine relative to diacid ($r = 0.9850$).

### Step 3: Mole Percent of Monofunctional Acetic Acid
When adding acetic acid ($B'$) to an equimolar mixture ($N_A = N_B$):
\\[
r_{\\text{eff}} = \\frac{N_A}{N_B + 2 N_{B'}} = \\frac{1}{1 + 2 (N_{B'} / N_B)}
\\]
Set $r_{\\text{eff}} = 0.98503$:
\\[
1 + 2 \\left(\\frac{N_{B'}}{N_B}\\right) = \\frac{1}{0.98503} = 1.01520
\\]
\\[
2 \\left(\\frac{N_{B'}}{N_B}\\right) = 0.01520 \\implies \\frac{N_{B'}}{N_B} = \\frac{0.01520}{2} = 0.00760 = 0.760\\text{ mol}\\%
\\]
Adding just $0.76\\text{ mol}\\%$ of acetic acid relative to adipic acid precisely caps the polymer at $M_n = 15,000\\text{ g/mol}$.""",
                "answer": "(a) X_n = 132.6 monomer residues; (b) r = 0.9850 (1.50% stoichiometric excess of adipic acid); (c) 0.760 mol% acetic acid required relative to adipic acid."
            },
            {
                "id": "prob-6-3",
                "difficulty": "foundation",
                "title": "Kinetic Rate Constant Evaluation: Self-Catalyzed vs Acid-Catalyzed Polyesterification",
                "statement": """The polyesterification of an equimolar mixture of diethylene glycol and adipic acid ($c_0 = 4.00\\text{ mol/L}$) is investigated at $160.0^\\circ\\text{C}$ under two experimental conditions:
- **Condition 1 (Self-Catalyzed)**: No external catalyst is added.
- **Condition 2 (Externally Catalyzed)**: $0.10\\text{ mol}\\%$ $p$-toluenesulfonic acid catalyst is added.

The following reaction times are required to reach specific conversions:
- Condition 1 reaches $p = 0.800$ in $t = 50.0\\text{ min}$, and $p = 0.900$ in $t = 194.0\\text{ min}$.
- Condition 2 reaches $p = 0.800$ in $t = 8.00\\text{ min}$, and $p = 0.900$ in $t = 18.00\\text{ min}$.

(a) Verify the kinetic order for both conditions using the integrated rate equations.
(b) Calculate the rate constants $k_1$ (in $\\text{L}^2\\text{ mol}^{-2}\\text{ min}^{-1}$) and $k_2$ (in $\\text{L mol}^{-1}\\text{ min}^{-1}$).
(c) Calculate the time required for each condition to reach an engineering conversion of $p = 0.990$ ($X_n = 100$).""",
                "solution": """### Step 1: Kinetic Verification for Condition 1 (Self-Catalyzed)
For self-catalyzed polyesterification, the integrated rate equation is:
\\[
\\frac{1}{(1 - p)^2} - 1 = 2 c_0^2 k_1 t
\\]
Calculate $[1/(1-p)^2 - 1]$:
- At $p = 0.800$: $\\frac{1}{(1 - 0.800)^2} - 1 = \\frac{1}{0.040} - 1 = 25.0 - 1 = 24.0$
- At $p = 0.900$: $\\frac{1}{(1 - 0.900)^2} - 1 = \\frac{1}{0.010} - 1 = 100.0 - 1 = 99.0$

Calculate rate constant $k_1$ from both data points:
\\[
2 c_0^2 = 2 (4.00\\text{ mol/L})^2 = 32.0\\text{ mol}^2/\\text{L}^2
\\]
- At $t = 50.0\\text{ min}$:
\\[
k_1 = \\frac{24.0}{(32.0)(50.0)} = \\frac{24.0}{1600} = 0.0150\\text{ L}^2\\text{ mol}^{-2}\\text{ min}^{-1}
\\]
- At $t = 194.0\\text{ min}$:
\\[
k_1 = \\frac{99.0}{(32.0)(194.0)} = \\frac{99.0}{6208} = 0.01595 \\approx 0.0155\\text{ L}^2\\text{ mol}^{-2}\\text{ min}^{-1}
\\]
The rate constant is consistent within experimental precision ($k_1 = 0.0155\\text{ L}^2\\text{ mol}^{-2}\\text{ min}^{-1}$), confirming third-order self-catalyzed kinetics.

### Step 2: Kinetic Verification for Condition 2 (Externally Catalyzed)
For acid-catalyzed polyesterification, the integrated rate equation is second-order:
\\[
\\frac{1}{1 - p} - 1 = c_0 k_2 t
\\]
Calculate $[1/(1-p) - 1]$:
- At $p = 0.800$: $\\frac{1}{1 - 0.800} - 1 = 5.0 - 1 = 4.0$
- At $p = 0.900$: $\\frac{1}{1 - 0.900} - 1 = 10.0 - 1 = 9.0$

Calculate rate constant $k_2$:
- At $t = 8.00\\text{ min}$:
\\[
k_2 = \\frac{4.0}{c_0 t} = \\frac{4.0}{(4.00)(8.00)} = \\frac{4.0}{32.0} = 0.125\\text{ L mol}^{-1}\\text{ min}^{-1}
\\]
- At $t = 18.00\\text{ min}$:
\\[
k_2 = \\frac{9.0}{(4.00)(18.00)} = \\frac{9.0}{72.0} = 0.125\\text{ L mol}^{-1}\\text{ min}^{-1}
\\]
The rate constant is identical ($k_2 = 0.125\\text{ L mol}^{-1}\\text{ min}^{-1}$), confirming second-order kinetics.

### Step 3: Time Required to Reach $p = 0.990$ ($X_n = 100$)
1. **Condition 1 (Self-Catalyzed)**:
\\[
\\frac{1}{(1 - 0.990)^2} - 1 = \\frac{1}{(0.010)^2} - 1 = 10,000 - 1 = 9,999
\\]
\\[
t_1 = \\frac{9,999}{2 c_0^2 k_1} = \\frac{9,999}{32.0 \\times 0.0155} = \\frac{9,999}{0.496} = 20,159\\text{ min} \\approx 336\\text{ hours (14 days!)}
\\]
2. **Condition 2 (Externally Catalyzed)**:
\\[
\\frac{1}{1 - 0.990} - 1 = 100 - 1 = 99
\\]
\\[
t_2 = \\frac{99}{c_0 k_2} = \\frac{99}{4.00 \\times 0.125} = \\frac{99}{0.500} = 198\\text{ min} = 3.3\\text{ hours}
\\]
This striking comparison ($3.3\\text{ hours}$ vs $14\\text{ days}$) demonstrates why commercial polyester reactors universally employ acid catalysts!""",
                "answer": "(a) Verified: Condition 1 is 3rd order (linear 1/(1-p)^2 vs t); Condition 2 is 2nd order (linear 1/(1-p) vs t); (b) k_1 = 0.0155 L^2 mol^-2 min^-1, k_2 = 0.125 L mol^-1 min^-1; (c) Time to reach p=0.99: Self-catalyzed = 20,160 min (336 hours); Acid-catalyzed = 198 min (3.3 hours)."
            },
            {
                "id": "prob-6-4",
                "difficulty": "advanced",
                "title": "Flory-Schulz Distribution Analysis: Mole vs Weight Fractions & Dispersity",
                "statement": """A stoichiometric linear step-growth polymerization has reached a conversion of $p = 0.980$.
(a) Calculate the number-average degree of polymerization $X_n$ and weight-average degree of polymerization $X_w$.
(b) Calculate the mole fraction $N_x$ and weight fraction $W_x$ for monomer ($x = 1$), dimer ($x = 2$), pentamer ($x = 5$), and 50-mer ($x = 50$).
(c) Find the chain length $x_{\\text{max}}$ at which the weight fraction distribution $W_x$ achieves its maximum value.
(d) Calculate the fraction of the total polymer sample mass that consists of chains with lengths greater than $X_n$.""",
                "solution": """### Step 1: Calculate $X_n, X_w$, and Dispersity
Given $p = 0.980$:
\\[
X_n = \\frac{1}{1 - p} = \\frac{1}{1 - 0.980} = \\frac{1}{0.020} = 50.0
\\]
\\[
X_w = \\frac{1 + p}{1 - p} = \\frac{1 + 0.980}{0.020} = \\frac{1.980}{0.020} = 99.0
\\]
\\[
\\text{Đ} = \\frac{X_w}{X_n} = 1 + p = 1.980
\\]

### Step 2: Compute $N_x$ and $W_x$
Formulas:
\\[
N_x = (1 - p) p^{x-1} = 0.020 \\times (0.980)^{x-1}
\\]
\\[
W_x = x (1 - p)^2 p^{x-1} = x (0.020)^2 (0.980)^{x-1} = x (4.00 \\times 10^{-4}) (0.980)^{x-1}
\\]
1. **Monomer ($x = 1$)**:
   - $N_1 = 0.020 \\times (0.980)^0 = 0.0200\\ (2.00\\%)$
   - $W_1 = 1 \\times (4.00 \\times 10^{-4}) \\times 1 = 0.000400\\ (0.040\\%)$
2. **Dimer ($x = 2$)**:
   - $N_2 = 0.020 \\times (0.980)^1 = 0.0196\\ (1.96\\%)$
   - $W_2 = 2 \\times (4.00 \\times 10^{-4}) \\times 0.980 = 0.000784\\ (0.0784\\%)$
3. **Pentamer ($x = 5$)**:
   - $N_5 = 0.020 \\times (0.980)^4 = 0.020 \\times 0.92237 = 0.01845\\ (1.845\\%)$
   - $W_5 = 5 \\times (4.00 \\times 10^{-4}) \\times 0.92237 = 0.001845\\ (0.185\\%)$
4. **50-mer ($x = 50 = X_n$)**:
   - $N_{50} = 0.020 \\times (0.980)^{49} = 0.020 \\times 0.3716 = 0.00743\\ (0.743\\%)$
   - $W_{50} = 50 \\times (4.00 \\times 10^{-4}) \\times 0.3716 = 0.007432\\ (0.743\\%)$

Notice that on a mole basis, monomer ($x = 1$) is the single most abundant species in the mixture ($N_1 > N_2 > N_3 \\dots$), whereas on a mass basis, monomer accounts for only $0.04\\%$ of the total polymer!

### Step 3: Chain Length at Maximum Weight Fraction $x_{\\text{max}}$
To find the maximum of $W_x$, treat $x$ as continuous and differentiate $\\ln W_x$:
\\[
\\ln W_x = \\ln x + 2 \\ln(1 - p) + (x - 1) \\ln p
\\]
\\[
\\frac{d \\ln W_x}{dx} = \\frac{1}{x} + \\ln p = 0 \\implies x_{\\text{max}} = -\\frac{1}{\\ln p}
\\]
Since $p = 0.980$, $\\ln(0.980) = -0.0202027$:
\\[
x_{\\text{max}} = \\frac{1}{0.0202027} = 49.498 \\approx 50
\\]
Because $\\ln p = \\ln(1 - (1-p)) \\approx -(1-p)$, for high conversion:
\\[
x_{\\text{max}} \\approx \\frac{1}{1 - p} = X_n = 50
\\]
The weight distribution achieves its maximum at precisely the number-average degree of polymerization!

### Step 4: Mass Fraction of Chains with $x > X_n$
The cumulative weight fraction of chains with length up to $X_n$ is:
\\[
F_w(X_n) = \\sum_{x=1}^{X_n} W_x = 1 - p^{X_n}(1 + X_n(1 - p))
\\]
Given $X_n = 50$ and $p = 0.980$:
\\[
p^{X_n} = (0.980)^{50} = 0.36417
\\]
\\[
1 + X_n(1 - p) = 1 + 50(0.020) = 1 + 1.0 = 2.0
\\]
\\[
F_w(50) = 1 - (0.36417)(2.0) = 1 - 0.72834 = 0.27166\\ (27.17\\%)
\\]
The fraction of mass with chain length greater than $X_n$ is:
\\[
W(x > X_n) = 1 - F_w(50) = 0.72834 = 72.83\\%
\\]
Nearly three-quarters ($72.8\\%$) of the sample mass resides in chains longer than the number-average length $X_n$.""",
                "answer": "(a) X_n = 50.0, X_w = 99.0, PDI = 1.980; (b) Monomer: N_1 = 2.00%, W_1 = 0.040%; Dimer: N_2 = 1.96%, W_2 = 0.078%; Pentamer: N_5 = 1.85%, W_5 = 0.185%; 50-mer: N_50 = 0.743%, W_50 = 0.743%; (c) x_max = 50 (= X_n); (d) 72.83% of total mass resides in chains with x > X_n."
            },
            {
                "id": "prob-6-5",
                "difficulty": "advanced",
                "title": "Equilibrium Step-Growth with Water Removal and Vacuum Efficiency",
                "statement": """A melt polycondensation between dimethyl terephthalate and ethylene glycol reaches an equilibrium constant of $K = 4.00$ at $280^\\circ\\text{C}$ for the transesterification equilibrium:
\\[
2 -\\text{COOCH}_2\\text{CH}_2\\text{OH} \\xrightleftharpoons{K} -\\text{COOCH}_2\\text{CH}_2\\text{OOC}- + \\text{HOCH}_2\\text{CH}_2\\text{OH}
\\]
where ethylene glycol (EG) is the volatile condensation by-product.
The total concentration of repeating ester units in the melt is $[\\text{Ester}]_0 = 5.50\\text{ mol/L}$.
(a) Derive the equilibrium degree of polymerization $X_n$ as a function of the equilibrium constant $K$ and the mole fraction of residual by-product $n_{\\text{EG}} / n_{\\text{polymer}}$.
(b) If the reaction is carried out in a closed autoclave without removing EG, calculate the maximum achievable conversion $p_{\\text{eq}}$ and degree of polymerization $X_n$.
(c) To achieve an engineering fiber-grade $X_n = 120$ ($M_n \\approx 23,000\\text{ g/mol}$), calculate the maximum permissible concentration of residual ethylene glycol $[\\text{EG}]$ in the melt (in $\\text{mol/L}$).
(d) Given Henry's law constant for ethylene glycol in PET melt $H = 1.20 \\times 10^4\\text{ Pa L/mol}$, calculate the required vacuum pressure $P_{\\text{vac}}$ (in Pascals and millibars).""",
                "solution": """### Step 1: Derivation of $X_n$ at Reversible Equilibrium
Let $c_0$ be the initial concentration of functional groups.
At conversion $p$:
- Unreacted end groups: $c_{\\text{end}} = c_0(1 - p)$
- Formed ester linkages: $c_{\\text{ester}} = c_0 p$
- Residual volatile by-product: $[\\text{EG}]$

The equilibrium expression is:
\\[
K = \\frac{c_{\\text{ester}} [\\text{EG}]}{c_{\\text{end}}^2} = \\frac{(c_0 p) [\\text{EG}]}{[c_0(1 - p)]^2} = \\frac{p [\\text{EG}]}{c_0 (1 - p)^2}
\\]
Since $X_n = 1 / (1 - p)$, we have $1 - p = 1 / X_n$ and $p = 1 - 1/X_n \\approx 1.0$ for high molecular weights.
Substituting:
\\[
K = \\frac{1 \\cdot [\\text{EG}]}{c_0 (1/X_n)^2} = \\frac{[\\text{EG}] X_n^2}{c_0}
\\]
Solving for $X_n$:
\\[
X_n = \\sqrt{ \\frac{K c_0}{[\\text{EG}]} }
\\]

### Step 2: Closed System without By-Product Removal
In a closed vessel, all EG formed remains in the melt.
Each bond formed generates one molecule of EG: $[\\text{EG}] = c_0 p / 2$ (since 2 end groups yield 1 by-product).
\\[
K = \\frac{p (c_0 p / 2)}{c_0 (1 - p)^2} = \\frac{p^2}{2 (1 - p)^2}
\\]
Taking the square root:
\\[
\\sqrt{2 K} = \\frac{p}{1 - p} = X_n - 1
\\]
Given $K = 4.00$:
\\[
\\sqrt{2 \\times 4.00} = \\sqrt{8.00} = 2.828
\\]
\\[
X_n - 1 = 2.828 \\implies X_n = 3.828 \\approx 3.83
\\]
Conversion:
\\[
p = \\frac{X_n - 1}{X_n} = \\frac{2.828}{3.828} = 0.7388\\ (73.9\\%)
\\]
In a closed system, equilibrium stops the reaction at $X_n < 4$ (short oligomers)!

### Step 3: Maximum Permissible Residual By-Product $[\\text{EG}]$ for $X_n = 120$
Rearranging the formula from Step 1:
\\[
[\\text{EG}] = \\frac{K c_0 p}{X_n^2 (1 - p)^2 / (1-p)^2} = \\frac{K c_0}{X_n^2}
\\]
Given:
- $K = 4.00$
- $c_0 = 5.50\\text{ mol/L}$
- $X_n = 120$

\\[
[\\text{EG}] = \\frac{4.00 \\times 5.50}{(120)^2} = \\frac{22.00}{14,400} = 1.528 \\times 10^{-3}\\text{ mol/L}
\\]

### Step 4: Required Reactor Vacuum Pressure $P_{\\text{vac}}$
Applying Henry's law:
\\[
P_{\\text{vac}} = H \\times [\\text{EG}]
\\]
Given $H = 1.20 \\times 10^4\\text{ Pa L/mol}$:
\\[
P_{\\text{vac}} = (1.20 \\times 10^4\\text{ Pa L/mol}) \\times (1.528 \\times 10^{-3}\\text{ mol/L}) = 18.34\\text{ Pa}
\\]
Convert to millibars ($1\\text{ mbar} = 100\\text{ Pa}$):
\\[
P_{\\text{vac}} = \\frac{18.34}{100} = 0.183\\text{ mbar}
\\]
To produce PET fiber, the finishing finisher reactor must operate under a high vacuum of less than $0.2\\text{ mbar}$!""",
                "answer": "(a) X_n = sqrt(K * c_0 / [EG]); (b) Closed system: p_eq = 0.739, X_n = 3.83 (reaction stops at oligomers); (c) Residual [EG] <= 1.53 x 10^-3 mol/L; (d) P_vac = 18.3 Pa = 0.183 mbar."
            },
            {
                "id": "prob-6-6",
                "difficulty": "advanced",
                "title": "Carothers Critical Conversion for Trifunctional and Tetrafunctional Gelation",
                "statement": """Determine the critical gel point conversion $p_c$ according to the Carothers theory for each of the following reaction mixtures:
(a) Pure glycerol ($f = 3$) reacting with phthalic anhydride ($f = 2$) in stoichiometric proportions ($2\\text{ moles of glycerol to }3\\text{ moles of phthalic anhydride}$, forming glyptal resin).
(b) Pentaerythritol ($f = 4$) reacting with adipic acid ($f = 2$) in exact stoichiometric proportions ($1\\text{ mole of pentaerythritol to }2\\text{ moles of adipic acid}$).
(c) A ternary mixture consisting of $2.0\\text{ moles of adipic acid } (f = 2), 1.6\\text{ moles of ethylene glycol } (f = 2)$, and $0.267\\text{ moles of glycerol } (f = 3)$.
Verify stoichiometric balance and compute the Carothers gel point $p_c$.""",
                "solution": """### Step 1: Glyptal Resin ($A_3 + B_2$, 2:3 Moles)
- Initial molecules: $N_{\\text{glycerol}} = 2$, $N_{\\text{phthalic}} = 3$.
- Total molecules: $N_0 = 2 + 3 = 5\\text{ moles}$.
- Hydroxyl groups ($A$): $2 \\times 3 = 6\\text{ moles}$.
- Carboxyl groups ($B$): $3 \\times 2 = 6\\text{ moles}$.
Stoichiometry is exact ($N_A = N_B = 6$).
Total functional groups $= 6 + 6 = 12\\text{ moles}$.
Average functionality:
\\[
f_{\\text{avg}} = \\frac{\\text{Total functional groups}}{N_0} = \\frac{12}{5} = 2.40
\\]
Carothers gel point:
\\[
p_c = \\frac{2}{f_{\\text{avg}}} = \\frac{2}{2.40} = \\frac{5}{6} = 0.8333 = 83.33\\%
\\]

### Step 2: Pentaerythritol + Adipic Acid ($A_4 + B_2$, 1:2 Moles)
- Initial molecules: $N_{\\text{penta}} = 1$, $N_{\\text{adipic}} = 2$.
- Total molecules: $N_0 = 1 + 2 = 3\\text{ moles}$.
- Hydroxyl groups ($A$): $1 \\times 4 = 4\\text{ moles}$.
- Carboxyl groups ($B$): $2 \\times 2 = 4\\text{ moles}$.
Stoichiometry is exact ($N_A = N_B = 4$).
Total functional groups $= 4 + 4 = 8\\text{ moles}$.
Average functionality:
\\[
f_{\\text{avg}} = \\frac{8}{3} = 2.667
\\]
Carothers gel point:
\\[
p_c = \\frac{2}{f_{\\text{avg}}} = \\frac{2}{8/3} = \\frac{6}{8} = 0.7500 = 75.00\\%
\\]

### Step 3: Ternary System ($2.0\\text{ Adipic} + 1.6\\text{ EG} + 0.267\\text{ Glycerol}$)
Count functional groups:
- Carboxyl groups ($B$): $2.0\\text{ mol} \\times 2 = 4.00\\text{ moles}$.
- Hydroxyl groups from EG ($A$): $1.6\\text{ mol} \\times 2 = 3.20\\text{ moles}$.
- Hydroxyl groups from Glycerol ($A$): $0.267\\text{ mol} \\times 3 = 0.80\\text{ moles}$.
Total hydroxyl groups $= 3.20 + 0.80 = 4.00\\text{ moles}$.
Stoichiometry is exact ($N_A = N_B = 4.00\\text{ moles}$).
Total monomer molecules:
\\[
N_0 = 2.0 + 1.6 + 0.267 = 3.867\\text{ moles}
\\]
Total functional groups:
\\[
N_{\\text{groups}} = 4.00 + 4.00 = 8.00\\text{ moles}
\\]
Average functionality:
\\[
f_{\\text{avg}} = \\frac{8.00}{3.867} = 2.0688
\\]
Carothers gel point:
\\[
p_c = \\frac{2}{f_{\\text{avg}}} = \\frac{2}{2.0688} = 0.9667 = 96.67\\%
\\]
Because the trifunctional brancher comprises only a small fraction of the diol component, gelation is postponed until $96.7\\%$ conversion, allowing significant linear chain growth before network formation.""",
                "answer": "(a) Glyptal (f_avg = 2.40): p_c = 0.833 (83.3%); (b) Pentaerythritol + Adipic (f_avg = 2.67): p_c = 0.750 (75.0%); (c) Ternary system (f_avg = 2.069): p_c = 0.967 (96.7%)."
            },
            {
                "id": "prob-6-7",
                "difficulty": "challenge",
                "title": "Rigorous Flory-Stockmayer Statistical Gelation Theory Derivation",
                "statement": """Consider a polymerization system containing multifunctional branch units $A_f$ with functionality $f \\ge 3$, along with bifunctional monomers $A-A$ and $B-B$.
Let $\\alpha$ be the branching coefficient, defined as the probability that a given functional group on a branch unit connects through a chain of bifunctional units to another branch unit.
(a) Using Cayley tree (Bethe lattice) branching analysis, show that the expected number of new chains branching out from generation $n$ to generation $n+1$ is multiplied by the branching factor $(f - 1) \\alpha$.
(b) Prove that the condition for an infinite network (percolation) to form with non-zero probability requires:
\\[
\\alpha_c = \\frac{1}{f - 1}
\\]
(c) For a stoichiometric mixture of $A_f$ and $B-B$ ($r = 1, \\rho = 1$), express $\\alpha$ in terms of fractional conversion $p$, and derive the Flory-Stockmayer critical conversion $p_c$.
(d) For a trifunctional monomer ($f = 3$), compare the Flory-Stockmayer critical conversion $p_c$ with the Carothers prediction and explain physically why $p_{c, \\text{Flory}} < p_{c, \\text{Carothers}}$.""",
                "solution": """### Step 1: Branching Tree Analysis
Consider an $A_f$ branch unit selected as the root of a tree graph (Generation 0).
The root has $f$ reactive arms.
Pick one arm and trace outward:
- It reacts with probability $p_A$.
- Through alternating $B-B$ and $A-A$ linkages, it reaches another $A_f$ branch unit with overall probability $\\alpha$.
Once this new branch unit is reached (Generation 1):
- One of its $f$ functional groups is used by the incoming bond from Generation 0.
- The remaining number of outgoing arms capable of continuing the tree outward is strictly $f - 1$.
Each of these $f - 1$ outgoing arms independently has probability $\\alpha$ of reaching a further branch unit.
Therefore, the expected number of branch connections in Generation 1 is $(f - 1) \\alpha$.
By induction, the expected number of active branching paths in Generation $n$ is:
\\[
\\langle Z_n \\rangle = f \\cdot [(f - 1) \\alpha]^n
\\]

### Step 2: Critical Condition for Infinite Network
1. If $(f - 1) \\alpha < 1$:
   As $n \\to \\infty$, $[(f - 1) \\alpha]^n \\to 0$. The probability of an infinite path is zero; all molecular clusters are finite.
2. If $(f - 1) \\alpha > 1$:
   As $n \\to \\infty$, $[(f - 1) \\alpha]^n \\to \\infty$. The branching tree diverges exponentially; there is a non-zero probability of an infinite percolating cluster.
3. The transition occurs precisely when the propagation factor equals unity:
\\[
(f - 1) \\alpha_c = 1 \\implies \\alpha_c = \\frac{1}{f - 1}
\\]

### Step 3: Critical Conversion for Pure $A_f + B-B$
For a stoichiometric mixture of $A_f$ and $B-B$:
All $A$ groups reside on branch units ($\\rho = 1$), and stoichiometry is balanced ($p_A = p_B = p$).
Tracing from an $A$ group on branch unit 1:
- The $A$ group must react with a $B$ group (probability $p$).
- The second $B$ group on the $B-B$ monomer must react with an $A$ group on another branch unit (probability $p$).
Therefore:
\\[
\\alpha = p_A p_B = p^2
\\]
Equating $\\alpha$ to $\\alpha_c$:
\\[
p_c^2 = \\alpha_c = \\frac{1}{f - 1} \\implies p_c = \\frac{1}{\\sqrt{f - 1}}
\\]

### Step 4: Comparison for Trifunctional Monomer ($f = 3$)
1. **Flory-Stockmayer Prediction**:
\\[
p_c = \\frac{1}{\\sqrt{3 - 1}} = \\frac{1}{\\sqrt{2}} = 0.7071\\ (70.71\\%)
\\]
2. **Carothers Prediction**:
A stoichiometric mixture of $A_3$ and $B_2$ requires 2 moles of $A_3$ per 3 moles of $B_2$ (6 $A$ groups, 6 $B$ groups).
Total molecules $N_0 = 2 + 3 = 5$.
Average functionality $f_{\\text{avg}} = 12 / 5 = 2.40$.
\\[
p_{c, \\text{Carothers}} = \\frac{2}{f_{\\text{avg}}} = \\frac{2}{2.40} = 0.8333\\ (83.33\\%)
\\]

### Physical Explanation of the Discrepancy
- Carothers' condition requires the **number-average** molecular weight to diverge: $X_n = N_0 / N \\to \\infty$.
  For $N \\to 0$, virtually all molecules in the reactor would have to be linked into a single macroscopic super-molecule.
- Flory-Stockmayer recognizes that **gelation begins when the first infinite network appears**, which corresponds to the divergence of the **weight-average** molecular weight ($X_w \\to \\infty$).
- At $p = 70.7\\%$, a tiny infinitesimal weight fraction of the system forms the first infinite percolating network spanning the container, causing the liquid to lose fluidity and gel. Meanwhile, millions of finite soluble oligomers remain ($X_n$ is only $\\approx 3.4$!).
- Therefore, gelation occurs much earlier than Carothers predicted ($70.7\\%$ vs $83.3\\%$). Flory's statistical approach is experimentally confirmed.""",
                "answer": "(a) Generation scaling: <Z_n> = f * [(f-1)*alpha]^n; (b) Critical percolation requires (f-1)*alpha_c = 1 => alpha_c = 1/(f-1); (c) For pure A_f + B_2: alpha = p^2 => p_c = 1 / sqrt(f-1); (d) For f=3: p_c(Flory) = 70.71% vs p_c(Carothers) = 83.33%. Flory is correct because gelation occurs when X_w -> infinity (first infinite cluster), while X_n remains finite."
            },
            {
                "id": "prob-6-8",
                "difficulty": "challenge",
                "title": "Statistical Derivation of Flory-Schulz Moments ($X_w, X_z$)",
                "statement": """Starting from the Flory-Schulz most probable mole fraction distribution:
\\[
N_x = (1 - p) p^{x-1}
\\]
and weight fraction distribution:
\\[
W_x = x (1 - p)^2 p^{x-1}
\\]
(a) Using generating functions or summation series formulas, prove analytically that:
\\[
X_w = \\sum_{x=1}^\\infty x W_x = \\frac{1 + p}{1 - p}
\\]
(b) Derive the analytical expression for the z-average degree of polymerization:
\\[
X_z = \\frac{\\sum_{x=1}^\\infty x^2 W_x}{\\sum_{x=1}^\\infty x W_x} = \\frac{1 + 4 p + p^2}{(1 - p)(1 + p)}
\\]
(c) For conversions $p = 0.900, 0.990$, and $0.999$, compute $X_n, X_w, X_z$, and the ratio $X_z / X_w$.
(d) Show that in the limit $p \\to 1.0$, $X_n : X_w : X_z \\to 1 : 2 : 3$.""",
                "solution": """### Step 1: Analytical Proof for $X_w$
By definition:
\\[
X_w = \\sum_{x=1}^\\infty x W_x = \\sum_{x=1}^\\infty x [x (1 - p)^2 p^{x-1}] = (1 - p)^2 \\sum_{x=1}^\\infty x^2 p^{x-1}
\\]
Recall the standard geometric series for $|p| < 1$:
\\[
S_0 = \\sum_{x=0}^\\infty p^x = \\frac{1}{1 - p}
\\]
Differentiating with respect to $p$:
\\[
S_1 = \\sum_{x=1}^\\infty x p^{x-1} = \\frac{d}{dp}\\left(\\frac{1}{1 - p}\\right) = \\frac{1}{(1 - p)^2}
\\]
Multiplying by $p$:
\\[
\\sum_{x=1}^\\infty x p^x = \\frac{p}{(1 - p)^2}
\\]
Differentiating again with respect to $p$:
\\[
\\sum_{x=1}^\\infty x^2 p^{x-1} = \\frac{d}{dp}\\left( \\frac{p}{(1 - p)^2} \\right) = \\frac{1 \\cdot (1 - p)^2 - p \\cdot 2(1 - p)(-1)}{(1 - p)^4} = \\frac{(1 - p) + 2 p}{(1 - p)^3} = \\frac{1 + p}{(1 - p)^3}
\\]
Substitute into the expression for $X_w$:
\\[
X_w = (1 - p)^2 \\times \\frac{1 + p}{(1 - p)^3} = \\frac{1 + p}{1 - p}
\\]
This completes the exact proof.

### Step 2: Derivation of $X_z$
The z-average degree of polymerization is:
\\[
X_z = \\frac{\\sum x^2 W_x}{\\sum x W_x} = \\frac{(1 - p)^2 \\sum_{x=1}^\\infty x^3 p^{x-1}}{X_w}
\\]
Let us evaluate $S_3 = \\sum_{x=1}^\\infty x^3 p^{x-1}$:
Multiply the sum for $x^2 p^{x-1}$ by $p$:
\\[
\\sum_{x=1}^\\infty x^2 p^x = \\frac{p (1 + p)}{(1 - p)^3} = \\frac{p + p^2}{(1 - p)^3}
\\]
Differentiating with respect to $p$:
\\[
\\sum_{x=1}^\\infty x^3 p^{x-1} = \\frac{d}{dp}\\left( \\frac{p + p^2}{(1 - p)^3} \\right) = \\frac{(1 + 2 p)(1 - p)^3 - (p + p^2) \\cdot 3(1 - p)^2(-1)}{(1 - p)^6}
\\]
Factor out $(1 - p)^2$:
\\[
= \\frac{(1 + 2 p)(1 - p) + 3(p + p^2)}{(1 - p)^4} = \\frac{(1 + p - 2 p^2) + (3 p + 3 p^2)}{(1 - p)^4} = \\frac{1 + 4 p + p^2}{(1 - p)^4}
\\]
Now substitute into $X_z$:
\\[
\\sum x^2 W_x = (1 - p)^2 \\left( \\frac{1 + 4 p + p^2}{(1 - p)^4} \\right) = \\frac{1 + 4 p + p^2}{(1 - p)^2}
\\]
Dividing by $X_w = \\frac{1 + p}{1 - p}$:
\\[
X_z = \\frac{\\frac{1 + 4 p + p^2}{(1 - p)^2}}{\\frac{1 + p}{1 - p}} = \\frac{1 + 4 p + p^2}{(1 - p)(1 + p)}
\\]

### Step 3: Tabulate Moments at $p = 0.900, 0.990, 0.999$
1. **$p = 0.900$**:
   - $X_n = 1 / (1 - 0.900) = 10.0$
   - $X_w = (1 + 0.900) / (1 - 0.900) = 1.900 / 0.100 = 19.0$
   - $X_z = [1 + 4(0.900) + (0.900)^2] / [(0.100)(1.900)] = [1 + 3.60 + 0.81] / 0.190 = 5.41 / 0.190 = 28.47$
   - Ratio $X_z / X_w = 28.47 / 19.0 = 1.498$
2. **$p = 0.990$**:
   - $X_n = 1 / 0.010 = 100.0$
   - $X_w = 1.990 / 0.010 = 199.0$
   - $X_z = [1 + 4(0.990) + (0.990)^2] / [(0.010)(1.990)] = [1 + 3.96 + 0.9801] / 0.01990 = 5.9401 / 0.01990 = 298.50$
   - Ratio $X_z / X_w = 298.50 / 199.0 = 1.500$
3. **$p = 0.999$**:
   - $X_n = 1 / 0.001 = 1,000.0$
   - $X_w = 1.999 / 0.001 = 1,999.0$
   - $X_z = [1 + 4(0.999) + (0.999)^2] / [(0.001)(1.999)] = [5.994] / 0.001999 = 2,998.5$
   - Ratio $X_z / X_w = 2,998.5 / 1,999.0 = 1.500$

### Step 4: Asymptotic Ratio at $p \\to 1.0$
Let $\\epsilon = 1 - p \\to 0$:
- $X_n = 1 / \\epsilon$
- $X_w = (2 - \\epsilon) / \\epsilon \\approx 2 / \\epsilon = 2 X_n$
- $X_z = (1 + 4(1) + 1) / (\\epsilon \\cdot 2) = 6 / (2 \\epsilon) = 3 / \\epsilon = 3 X_n$
Therefore:
\\[
X_n : X_w : X_z \\to 1 : 2 : 3
\\]""",
                "answer": "(a) Proved: X_w = (1+p)/(1-p); (b) Proved: X_z = (1 + 4p + p^2) / [(1-p)(1+p)]; (c) p=0.90: X_n=10, X_w=19, X_z=28.5 (X_z/X_w=1.50); p=0.99: X_n=100, X_w=199, X_z=298.5; p=0.999: X_n=1000, X_w=1999, X_z=2998.5; (d) As p -> 1, X_n : X_w : X_z -> 1 : 2 : 3."
            },
            {
                "id": "prob-6-9",
                "difficulty": "challenge",
                "title": "Post-Gelation Extraction: Sol and Gel Fractions Beyond Gel Point",
                "statement": """Beyond the gel point conversion ($p > p_c$), a polymerizing network partitions into an extractable, soluble branched fraction (sol, weight fraction $w_{\\text{sol}}$) and an insoluble infinite network (gel, weight fraction $w_{\\text{gel}} = 1 - w_{\\text{sol}}$).
Consider a trifunctional monomer $A_3$ reacting with itself ($f = 3$) or a stoichiometric $A_3 + B_2$ system with branching coefficient $\\alpha > \\alpha_c = 0.50$.
Let $\\beta$ be the extinction probability that a randomly chosen bond attached to a branch unit does *not* lead to an infinite network path.
(a) Show that $\\beta$ satisfies the recursive algebraic relation:
\\[
\\beta = 1 - \\alpha + \\alpha \\beta^2
\\]
(b) Solve this quadratic equation for $\\beta$ and identify the two roots: the trivial root $\\beta_1 = 1.0$ (pre-gel) and the non-trivial root $\\beta_2(\\alpha)$ (post-gel).
(c) Prove that the sol weight fraction is given by:
\\[
w_{\\text{sol}} = \\beta^3 = \\left( \\frac{1 - \\alpha}{\\alpha} \\right)^3
\\]
(d) Calculate $w_{\\text{sol}}$ and $w_{\\text{gel}}$ for branching coefficients $\\alpha = 0.55, 0.60, 0.70, 0.80$, and $0.90$.""",
                "solution": """### Step 1: Derivation of the Self-Consistent Relation for $\\beta$
Let $\\beta$ be the probability that an outgoing path from a branch unit does NOT connect to the infinite gel network.
There are two mutually exclusive possibilities for an outgoing arm:
1. The arm is unreacted: this occurs with probability $1 - \\alpha$. An unreacted arm definitely does not reach the infinite network.
2. The arm has reacted: this occurs with probability $\\alpha$.
   If it reacts, it connects to another trifunctional branch unit with $f - 1 = 2$ new outgoing arms.
   For this path to still remain finite, *both* of these 2 new outgoing arms must fail to connect to the infinite network.
   Since the arms branch independently, the probability that both fail is $\\beta \\times \\beta = \\beta^2$.

Summing the two probabilities yields the fundamental recursive equation:
\\[
\\beta = (1 - \\alpha) + \\alpha \\beta^2
\\]

### Step 2: Solve the Quadratic Equation
Rearranging into standard quadratic form:
\\[
\\alpha \\beta^2 - \\beta + (1 - \\alpha) = 0
\\]
Factoring the quadratic:
Notice that $\\beta = 1$ is always a root:
\\[
\\alpha(1)^2 - 1 + 1 - \\alpha = 0
\\]
Dividing $(\\alpha \\beta^2 - \\beta + 1 - \\alpha)$ by $(\\beta - 1)$:
\\[
(\\beta - 1)(\\alpha \\beta - (1 - \\alpha)) = 0
\\]
The two roots are:
1. **$\\beta_1 = 1.0$**: For $\\alpha \\le \\alpha_c = 0.50$, all paths are strictly finite, so the extinction probability is identically $1.0$.
2. **$\\beta_2 = \\frac{1 - \\alpha}{\\alpha}$**: For $\\alpha > 0.50$, $\\frac{1 - \\alpha}{\\alpha} < 1.0$, representing the true physical extinction probability in the post-gel regime.

### Step 3: Derivation of the Sol Fraction $w_{\\text{sol}}$
A trifunctional monomer molecule belongs to the sol fraction if and only if **all three** of its functional arms lead to finite paths.
Since each of its 3 arms independently has extinction probability $\\beta$:
\\[
w_{\\text{sol}} = \\beta^3 = \\left( \\frac{1 - \\alpha}{\\alpha} \\right)^3
\\]
The gel fraction is the remainder of the total sample:
\\[
w_{\\text{gel}} = 1 - w_{\\text{sol}} = 1 - \\left( \\frac{1 - \\alpha}{\\alpha} \\right)^3
\\]

### Step 4: Numerical Calculation of $w_{\\text{sol}}$ and $w_{\\text{gel}}$
1. **$\\alpha = 0.55$**:
   - $\\beta = (1 - 0.55) / 0.55 = 0.45 / 0.55 = 0.81818$
   - $w_{\\text{sol}} = (0.81818)^3 = 0.5477\\ (54.77\\%)$
   - $w_{\\text{gel}} = 1 - 0.5477 = 0.4523\\ (45.23\\%)$
2. **$\\alpha = 0.60$**:
   - $\\beta = (1 - 0.60) / 0.60 = 0.40 / 0.60 = 0.66667$
   - $w_{\\text{sol}} = (0.66667)^3 = 0.2963\\ (29.63\\%)$
   - $w_{\\text{gel}} = 1 - 0.2963 = 0.7037\\ (70.37\\%)$
3. **$\\alpha = 0.70$**:
   - $\\beta = (1 - 0.70) / 0.70 = 0.30 / 0.70 = 0.42857$
   - $w_{\\text{sol}} = (0.42857)^3 = 0.0787\\ (7.87\\%)$
   - $w_{\\text{gel}} = 1 - 0.0787 = 0.9213\\ (92.13\\%)$
4. **$\\alpha = 0.80$**:
   - $\\beta = (1 - 0.80) / 0.80 = 0.20 / 0.80 = 0.2500$
   - $w_{\\text{sol}} = (0.2500)^3 = 0.0156\\ (1.56\\%)$
   - $w_{\\text{gel}} = 1 - 0.0156 = 0.9844\\ (98.44\\%)$
5. **$\\alpha = 0.90$**:
   - $\\beta = (1 - 0.90) / 0.90 = 0.10 / 0.90 = 0.11111$
   - $w_{\\text{sol}} = (0.11111)^3 = 0.00137\\ (0.14\\%)$
   - $w_{\\text{gel}} = 1 - 0.00137 = 0.99863\\ (99.86\\%)$

Notice how rapidly the gel fraction consumes the reaction mixture: by $\\alpha = 0.70$, over $92\\%$ of the sample mass is locked into the macroscopic gel network!""",
                "answer": "(a) Self-consistent equation proved: beta = (1-alpha) + alpha * beta^2; (b) Roots: beta_1 = 1.0 (pre-gel), beta_2 = (1-alpha)/alpha (post-gel); (c) w_sol = beta^3 = [(1-alpha)/alpha]^3, w_gel = 1 - w_sol; (d) alpha=0.55: w_sol=54.8%, w_gel=45.2%; alpha=0.60: w_sol=29.6%, w_gel=70.4%; alpha=0.70: w_sol=7.9%, w_gel=92.1%; alpha=0.80: w_sol=1.6%, w_gel=98.4%; alpha=0.90: w_sol=0.14%, w_gel=99.86%."
            }
        ]
    }

print("Unit 6 authoring complete.")

def get_units_4_5_6():
    return [build_unit_4(), build_unit_5(), build_unit_6()]

if __name__ == '__main__':
    u = get_units_4_5_6()
    print(f"Total units generated: {len(u)}")
    for unit in u:
        print(f"  Unit {unit['number']}: {unit['title']} ({len(unit['sections'])} sections, {len(unit['problems'])} problems)")
